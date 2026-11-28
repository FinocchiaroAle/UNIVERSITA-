#!/usr/bin/env python3
"""
Compilatore a sorgente unica per la dispensa di Algebra Lineare e Geometria.
Legge i file Markdown in dispensa/*.md e genera:
  1) dispensa_algebra_lineare.pdf (A4 via KaTeX + Chromium headless)
  2) sito/data/book-data.js (indice, contenuti HTML e searchBlocks per il sito statico)
  3) opzionalmente screenshot di verifica in scratch/ con --verify-screenshots
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import markdown
from bs4 import BeautifulSoup

ROOT_DIR = Path(__file__).resolve().parent
DISPENSA_DIR = ROOT_DIR / "dispensa"
SITO_DIR = ROOT_DIR / "sito"
DATA_JS_PATH = SITO_DIR / "data" / "book-data.js"
PDF_PATH = ROOT_DIR / "dispensa_algebra_lineare.pdf"
KATEX_DIR = SITO_DIR / "assets" / "katex"
TEMP_PRINT_DIR = Path("/tmp/algebra-lineare-print")
PRINT_HTML_PATH = TEMP_PRINT_DIR / "dispensa_print.html"
VENV_PYTHON = Path("/home/alessandro/.cache/algebra-pdf-venv/bin/python")
DEFAULT_SCREENSHOT_DIR = Path(
    "/home/alessandro/.gemini/antigravity/brain/83929f13-7ab0-419c-a1c6-2d8434f8c3ce/scratch"
)

PART_RE = re.compile(r"^<!--\s*(part:\s*.+?)\s*-->$", re.MULTILINE)
SECTION_RE = re.compile(r"^<!--\s*(section:\s*.+?)\s*-->$", re.MULTILINE)
OPEN_FENCE_RE = re.compile(r"^:::(def|thm|proof|note|warn|tip|exercise|example|solution)(?:\s+(.*))?$")
CLOSE_FENCE_RE = re.compile(r"^:::\s*$")

CALLOUT_LABELS = {
    "def": "DEFINIZIONE",
    "thm": "TEOREMA / PROPOSIZIONE",
    "proof": "DIMOSTRAZIONE",
    "note": "NOTA",
    "warn": "ATTENZIONE / ERRORE COMUNE",
    "tip": "CONSIGLIO / IDEA",
    "exercise": "ESERCIZIO",
    "example": "ESEMPIO SVOLTO",
    "solution": "SOLUZIONE PASSO-PASSO",
}


def parse_kv_meta(raw: str) -> dict[str, str]:
    """Parsa stringhe tipo 'key1: val1 | key2: val2'."""
    meta: dict[str, str] = {}
    for chunk in raw.split("|"):
        chunk = chunk.strip()
        if ":" not in chunk:
            continue
        k, v = chunk.split(":", 1)
        meta[k.strip()] = v.strip()
    return meta


def normalize_text(text: str) -> str:
    nfd = unicodedata.normalize("NFD", text or "")
    no_acc = "".join(ch for ch in nfd if unicodedata.category(ch) != "Mn")
    return re.sub(r"\s+", " ", no_acc.lower()).strip()


def latex_to_plain(text: str) -> str:
    """Converte formule LaTeX in testo leggibile per indici e snippet di ricerca."""
    def clean_math(m: re.Match[str]) -> str:
        s = m.group(1)
        replacements = [
            (r"\\mathbb\{R\}", "ℝ"),
            (r"\\mathbb\{C\}", "ℂ"),
            (r"\\mathbb\{Z\}", "ℤ"),
            (r"\\mathbb\{Q\}", "ℚ"),
            (r"\\mathbb\{K\}", "K"),
            (r"\\operatorname\{([^{}]+)\}", r"\1"),
            (r"\\mathcal\{([^{}]+)\}", r"\1"),
            (r"\\text\{([^{}]+)\}", r"\1"),
            (r"\\mathrm\{([^{}]+)\}", r"\1"),
            (r"\\stackrel\{\\text\{DEF\}\}\{=\}", "="),
            (r"\\underline\{0\}", "0_vett"),
            (r"\\in\b", "∈"),
            (r"\\notin\b", "∉"),
            (r"\\subseteq\b", "⊆"),
            (r"\\subset\b", "⊂"),
            (r"\\ne\b|\\neq\b", "≠"),
            (r"\\le\b|\\leq\b", "≤"),
            (r"\\ge\b|\\geq\b", "≥"),
            (r"\\implies\b", "⇒"),
            (r"\\iff\b", "⇔"),
            (r"\\forall\b", "∀"),
            (r"\\exists\b", "∃"),
            (r"\\times\b", "×"),
            (r"\\cdot\b", "·"),
            (r"\\pm\b", "±"),
            (r"\\bar\{([^{}]+)\}", r"\1̄"),
            (r"\\overline\{([^{}]+)\}", r"\1̄"),
            (r"\\sqrt\{([^{}]+)\}", r"√(\1)"),
            (r"\\frac\{([^{}]+)\}\{([^{}]+)\}", r"(\1)/(\2)"),
            (r"\\setminus\b", "∖"),
            (r"\\to\b|\\mapsto\b", "→"),
            (r"\\bigl\(|\\left\(", "("),
            (r"\\bigr\)|\\right\)", ")"),
            (r"\\bigl|\\bigr|\\left|\\right", ""),
            (r"\\\\", "; "),
        ]
        for pat, rep in replacements:
            s = re.sub(pat, rep, s)
        s = re.sub(r"\\[a-zA-Z]+", " ", s)
        s = s.replace("{", "").replace("}", "")
        return re.sub(r"\s+", " ", s).strip()

    out = re.sub(r"(?<!\\)\$\$(.+?)(?<!\\)\$\$", clean_math, text, flags=re.DOTALL)
    out = re.sub(r"(?<!\\)\$([^\n$]+?)(?<!\\)\$", clean_math, out)
    out = out.replace(r"\$", "$")
    return re.sub(r"\s+", " ", out).strip()


class ProtectedStore:
    """Protegge formule LaTeX e blocchi SVG durante il parsing Markdown."""

    def __init__(self) -> None:
        self.items: dict[str, tuple[str, str]] = {}
        self.counter = 0

    def protect(self, text: str, source_name: str) -> str:
        # 1. Proteggi SVG completi
        def repl_svg(m: re.Match[str]) -> str:
            key = f"@@SVG_BLOCK_{self.counter}@@"
            self.counter += 1
            self.items[key] = ("svg", m.group(0))
            return key

        text = re.sub(r"<svg\b[^>]*>.*?</svg>", repl_svg, text, flags=re.DOTALL)

        # 2. Proteggi math display $$...$$ preservando l'eventuale indentazione di lista
        def repl_disp(m: re.Match[str]) -> str:
            key = f"@@MATH_DISP_{self.counter}@@"
            self.counter += 1
            self.items[key] = ("disp", m.group(1).strip())
            return key

        text = re.sub(r"(?<!\\)\$\$(.+?)(?<!\\)\$\$", repl_disp, text, flags=re.DOTALL)

        # 3. Proteggi math inline $...$
        def repl_inl(m: re.Match[str]) -> str:
            key = f"@@MATH_INL_{self.counter}@@"
            self.counter += 1
            self.items[key] = ("inl", m.group(1).strip())
            return key

        text = re.sub(r"(?<!\\)\$([^\n$]+?)(?<!\\)\$", repl_inl, text)

        # Fail fast su eventuali $ rimasti spaiati
        leftover = re.findall(r"(?<!\\)\$", text)
        if leftover:
            raise ValueError(
                f"Trovato simbolo '$' spaiato/non chiuso in {source_name}. Controlla i delimitatori LaTeX."
            )

        return text

    def restore(self, html_str: str) -> str:
        # Se un blocco display è l'unico contenuto di un <p>, promuovilo a <div class="math-display">
        html_str = re.sub(
            r"<p>\s*(@@MATH_DISP_\d+@@)\s*</p>",
            r'<div class="math-display">\1</div>',
            html_str,
        )
        html_str = re.sub(
            r"<p>\s*(@@SVG_BLOCK_\d+@@)\s*</p>",
            r'\1',
            html_str,
        )
        for key, (kind, payload) in self.items.items():
            if kind == "svg":
                html_str = html_str.replace(key, payload)
            elif kind == "disp":
                escaped = html.escape(payload, quote=False)
                html_str = html_str.replace(key, f"$${escaped}$$")
            elif kind == "inl":
                escaped = html.escape(payload, quote=False)
                html_str = html_str.replace(key, f"${escaped}$")
        return html_str


LIST_ITEM_RE = re.compile(r"^(?:[-*+]|\d+\.)\s+")


def normalize_markdown_lists(raw_md: str) -> str:
    """Inserisce una riga vuota prima di un blocco lista che segue direttamente un paragrafo."""
    lines = raw_md.splitlines()
    out: list[str] = []
    in_fence = False
    for line in lines:
        s = line.strip()
        if s.startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence and out:
            prev = out[-1]
            prev_s = prev.strip()
            cur_lst = line.lstrip()
            if (
                prev_s
                and LIST_ITEM_RE.match(cur_lst)
                and not LIST_ITEM_RE.match(prev.lstrip())
                and not prev.startswith((" ", "\t", "|"))
                and not prev_s.startswith("#")
            ):
                out.append("")
        out.append(line)
    return "\n".join(out)


def render_markdown_fragment(text: str) -> str:
    """Converte un frammento Markdown (con blocchi :::...::: annidati) in HTML."""
    lines = text.splitlines()
    out_parts: list[str] = []
    md_buf: list[str] = []

    def flush_md() -> None:
        if not md_buf:
            return
        raw_md = "\n".join(md_buf).strip()
        md_buf.clear()
        if raw_md:
            normalized = normalize_markdown_lists(raw_md)
            converted = markdown.markdown(
                normalized,
                extensions=["tables", "fenced_code"],
                output_format="html5",
            )
            out_parts.append(converted)

    i = 0
    while i < len(lines):
        line = lines[i]
        m_open = OPEN_FENCE_RE.match(line.strip())
        if m_open:
            flush_md()
            kind = m_open.group(1)
            custom_title = (m_open.group(2) or "").strip()
            depth = 1
            inner_lines: list[str] = []
            i += 1
            while i < len(lines) and depth > 0:
                cur = lines[i]
                stripped = cur.strip()
                if OPEN_FENCE_RE.match(stripped):
                    depth += 1
                    inner_lines.append(cur)
                elif CLOSE_FENCE_RE.match(stripped):
                    depth -= 1
                    if depth > 0:
                        inner_lines.append(cur)
                else:
                    inner_lines.append(cur)
                i += 1
            if depth != 0:
                raise ValueError(f"Blocco :::{kind} non chiuso correttamente ('{custom_title}').")

            inner_html = render_markdown_fragment("\n".join(inner_lines))
            title_text = custom_title or CALLOUT_LABELS.get(kind, kind.upper())
            title_text = re.sub(r"`([^`]+)`", r"<code>\1</code>", title_text)

            if kind == "solution":
                out_parts.append(
                    f'<details class="solution-box" open>'
                    f'<summary>{title_text}</summary>'
                    f'<div class="solution-body">{inner_html}</div>'
                    f"</details>"
                )
            else:
                out_parts.append(
                    f'<aside class="callout callout-{kind}">'
                    f'<div class="callout-title">{title_text}</div>'
                    f'<div class="callout-body">{inner_html}</div>'
                    f"</aside>"
                )
        else:
            md_buf.append(line)
            i += 1

    flush_md()
    return "\n".join(out_parts)


def postprocess_section_html(
    sec_id: str, sec_kind: str, raw_html: str
) -> tuple[str, list[dict[str, str]], list[dict[str, str]]]:
    """
    Post-elabora HTML di una sezione:
      - verifica assenza di blocchi <pre> accidentali (da errata indentazione Markdown)
      - wrappa <table> in <div class="table-wrap">
      - aggiunge class="xref" ai link interni #sec-... / #app-...
      - evidenzia [INTEGRAZIONE NON DALLE LEZIONI]
      - assegna id="step-N" agli <h3> e costruisce toc
      - assegna data-bid="b-N" e genera searchBlocks
    """
    soup = BeautifulSoup(raw_html, "html.parser")

    pre_blocks = soup.find_all("pre")
    if pre_blocks:
        sample = re.sub(r"\s+", " ", pre_blocks[0].get_text(" ", strip=True))[:120]
        raise ValueError(
            f"Trovati {len(pre_blocks)} blocchi <pre> imprevisti in {sec_id}: {sample!r}. "
            "Controlla l'indentazione Markdown (usa 4 spazi per sottoliste, evita 4+ spazi per paragrafi spaiati)."
        )

    for tbl in soup.find_all("table"):
        if tbl.parent and "table-wrap" in (tbl.parent.get("class") or []):
            continue
        wrap = soup.new_tag("div", attrs={"class": "table-wrap"})
        tbl.wrap(wrap)

    for a in soup.find_all("a"):
        href = a.get("href") or ""
        if href.startswith("#sec-") or href.startswith("#app-") or href == "#intro":
            existing = a.get("class") or []
            if "xref" not in existing:
                a["class"] = [*existing, "xref"]

    # Evidenzia marker integrazioni esterne in nodi testuali sicuri
    marker = "[INTEGRAZIONE NON DALLE LEZIONI]"
    for text_node in list(soup.find_all(string=True)):
        if marker not in str(text_node):
            continue
        if text_node.parent and text_node.parent.name in ("script", "style", "code", "pre"):
            continue
        parts = str(text_node).split(marker)
        frag_nodes = []
        for idx, part in enumerate(parts):
            if part:
                frag_nodes.append(part)
            if idx < len(parts) - 1:
                badge = soup.new_tag("span", attrs={"class": "int-badge"})
                badge.string = marker
                frag_nodes.append(badge)
        text_node.replace_with(*frag_nodes)

    toc: list[dict[str, str]] = []
    short_map = {
        "1.": "1. Idea",
        "2.": "2. Definizioni",
        "3.": "3. Dimostrazioni",
        "4.": "4. Esempi",
        "5.": "5. Errori comuni",
        "6.": "6. Riepilogo",
        "7.": "7. Esercizi",
    }
    step_idx = 0
    for h3 in soup.find_all("h3"):
        step_idx += 1
        sid = f"step-{step_idx}"
        h3["id"] = sid
        full_title = re.sub(r"\s+", " ", h3.get_text(" ", strip=True))
        short = ""
        for prefix, label in short_map.items():
            if full_title.startswith(prefix):
                short = label
                break
        if not short:
            short = full_title if len(full_title) <= 24 else full_title[:23].rstrip() + "…"
        toc.append({"id": sid, "title": full_title, "short": short})

    search_blocks: list[dict[str, str]] = []
    bid_counter = 0
    current_heading = ""

    def next_bid() -> str:
        nonlocal bid_counter
        bid_counter += 1
        return f"b-{bid_counter}"

    def add_block(tag, kind: str, custom_txt: str | None = None) -> None:
        if tag.has_attr("data-bid"):
            return
        raw_txt = custom_txt if custom_txt is not None else tag.get_text(" ", strip=True)
        plain = latex_to_plain(raw_txt)
        if not plain or len(plain) < 2:
            return
        bid = next_bid()
        tag["data-bid"] = bid
        if not tag.has_attr("id") and kind == "heading":
            tag["id"] = bid
        block_kind = kind
        if sec_id == "app-a" and kind in ("table", "text", "def", "thm"):
            block_kind = "formula"
        elif sec_id == "app-c" and kind in ("table", "list", "text", "def"):
            block_kind = "glossary"
        search_blocks.append(
            {
                "s": sec_id,
                "b": bid,
                "k": block_kind,
                "h": current_heading,
                "t": plain,
                "n": normalize_text(plain),
            }
        )

    for el in soup.find_all(["h3", "h4", "aside", "p", "li", "tr"]):
        name = el.name
        if name == "h3":
            current_heading = re.sub(r"\s+", " ", el.get_text(" ", strip=True))
            el["data-bid"] = el.get("id") or next_bid()
            continue
        if name == "h4":
            current_heading = re.sub(r"\s+", " ", el.get_text(" ", strip=True))
            add_block(el, "heading")
            continue
        if name == "aside":
            classes = el.get("class") or []
            ckind = "note"
            for c in classes:
                if c.startswith("callout-"):
                    ckind = c.replace("callout-", "")
                    break
            add_block(el, ckind)
            continue
        if name == "tr":
            if el.find_parent("tbody"):
                add_block(el, "table")
            continue
        if name in ("p", "li"):
            if el.find_parent("aside") or (name == "p" and el.find_parent(["li", "td", "th"])):
                continue
            add_block(el, "list" if name == "li" else "text")

    return str(soup), toc, search_blocks


def load_dispensa(strict_xrefs: bool = False) -> tuple[list[dict], list[dict], list[dict]]:
    """Carica e parsa tutti i file dispensa/*.md in ordine."""
    md_files = sorted(DISPENSA_DIR.glob("*.md"))
    if not md_files:
        raise FileNotFoundError(f"Nessun file .md trovato in {DISPENSA_DIR}")

    parts: list[dict] = []
    parts_by_id: dict[str, dict] = {}
    sections: list[dict] = []
    all_search_blocks: list[dict] = []

    for md_path in md_files:
        raw_text = md_path.read_text(encoding="utf-8")

        for pm in PART_RE.finditer(raw_text):
            pmeta = parse_kv_meta(pm.group(1))
            pid = pmeta["part"]
            part_obj = {
                "id": pid,
                "num": int(pmeta["num"]) if pmeta.get("num", "").isdigit() else len(parts) + 1,
                "label": pmeta.get("label", f"CAPITOLO {len(parts) + 1}"),
                "title": pmeta.get("title", ""),
                "refs": html.escape(pmeta.get("refs", "")),
                "sectionIds": [],
            }
            parts.append(part_obj)
            parts_by_id[pid] = part_obj

        sec_matches = list(SECTION_RE.finditer(raw_text))
        for idx, sm in enumerate(sec_matches):
            smeta = parse_kv_meta(sm.group(1))
            start = sm.end()
            end = sec_matches[idx + 1].start() if idx + 1 < len(sec_matches) else len(raw_text)
            body_raw = raw_text[start:end].strip()

            sec_id = smeta["section"]
            sec_kind = smeta.get("kind", "section")
            part_id = smeta.get("part", "intro")

            store = ProtectedStore()
            protected = store.protect(body_raw, f"{md_path.name} ({sec_id})")
            frag_html = render_markdown_fragment(protected)
            restored_html = store.restore(frag_html)
            final_html, toc, s_blocks = postprocess_section_html(sec_id, sec_kind, restored_html)

            sec_obj = {
                "id": sec_id,
                "num": smeta.get("num", ""),
                "title": smeta.get("title", ""),
                "kind": sec_kind,
                "partId": part_id,
                "startPage": 0,
                "endPage": 0,
                "toc": toc,
                "html": final_html,
                "_source_file": md_path.name,
            }
            sections.append(sec_obj)
            all_search_blocks.extend(s_blocks)

            if part_id in parts_by_id:
                parts_by_id[part_id]["sectionIds"].append(sec_id)

    valid_ids = {s["id"] for s in sections} | {"home"}
    broken_xrefs: list[str] = []
    for s in sections:
        soup_chk = BeautifulSoup(s["html"], "html.parser")
        for a in soup_chk.find_all("a"):
            href = a.get("href") or ""
            if not href.startswith("#"):
                continue
            target = href[1:].split("?", 1)[0]
            if target.startswith("step-"):
                continue
            if target not in valid_ids:
                broken_xrefs.append(f"{s['id']} -> #{target}")
    if broken_xrefs:
        msg = "Link interni verso sezioni non ancora presenti: " + ", ".join(broken_xrefs)
        if strict_xrefs:
            raise ValueError(msg)
        print("AVVISO:", msg, file=sys.stderr)

    kind_rank = {"intro": 0, "section": 1, "appendix": 2}
    sections.sort(key=lambda s: kind_rank.get(s["kind"], 1))

    return parts, sections, all_search_blocks


def build_pdf_body_html(parts: list[dict], sections: list[dict]) -> str:
    """Costruisce l'HTML di stampa A4 (tema chiaro accademico) con KaTeX locale."""
    sec_by_id = {s["id"]: s for s in sections}
    intro_sec = sec_by_id.get("intro")
    appendices = [s for s in sections if s["kind"] == "appendix"]

    # Adatta HTML per PDF (<details class="solution-box"> -> <div class="solution-box-pdf">)
    def to_pdf_section_html(sec_html: str) -> str:
        soup = BeautifulSoup(sec_html, "html.parser")
        for det in soup.find_all("details", class_="solution-box"):
            wrap = soup.new_tag("div", attrs={"class": "solution-box-pdf"})
            summ = det.find("summary")
            if summ:
                title_div = soup.new_tag("div", attrs={"class": "solution-title-pdf"})
                for ch in list(summ.contents):
                    title_div.append(ch.extract())
                wrap.append(title_div)
                summ.decompose()
            body_div = det.find("div", class_="solution-body")
            if body_div:
                wrap.append(body_div.extract())
            else:
                for ch in list(det.contents):
                    wrap.append(ch.extract())
            det.replace_with(wrap)
        # Convert internal #sec-... links to #pdf-sec-...
        for a in soup.find_all("a"):
            href = a.get("href") or ""
            if href.startswith("#sec-") or href.startswith("#app-") or href == "#intro":
                a["href"] = "#pdf-" + href[1:]
        return str(soup)

    toc_entries: list[str] = []
    if intro_sec:
        toc_entries.append(
            f'<li class="toc-item toc-intro"><a href="#pdf-{intro_sec["id"]}">'
            f'<span>Introduzione — {html.escape(intro_sec["title"])}</span></a></li>'
        )
    for part in parts:
        toc_entries.append(
            f'<li class="toc-part"><strong>{html.escape(part["label"])} — {html.escape(part["title"])}</strong>'
            f'<ul class="toc-sub">'
        )
        for sid in part["sectionIds"]:
            s = sec_by_id.get(sid)
            if not s:
                continue
            toc_entries.append(
                f'<li><a href="#pdf-{s["id"]}">'
                f'<span class="toc-num">{html.escape(s["num"])}</span> '
                f'<span>{html.escape(s["title"])}</span></a></li>'
            )
        toc_entries.append("</ul></li>")
    if appendices:
        toc_entries.append('<li class="toc-part"><strong>Appendici</strong><ul class="toc-sub">')
        for s in appendices:
            toc_entries.append(
                f'<li><a href="#pdf-{s["id"]}">'
                f'<span class="toc-num">{html.escape(s["num"])}</span> — '
                f'<span>{html.escape(s["title"])}</span></a></li>'
            )
        toc_entries.append("</ul></li>")

    chapters_included = ", ".join(p["label"].title() for p in parts) or "Introduzione"
    if appendices:
        chapters_included += " + Appendici A–E"

    body_sections: list[str] = []
    if intro_sec:
        body_sections.append(
            f'<section class="pdf-section" id="pdf-{intro_sec["id"]}">'
            f'<div class="pdf-sec-kicker">INTRODUZIONE AL CORSO</div>'
            f'<h2 class="pdf-sec-title">{html.escape(intro_sec["title"])}</h2>'
            f'{to_pdf_section_html(intro_sec["html"])}'
            f"</section>"
        )

    for part in parts:
        body_sections.append(
            f'<div class="pdf-chapter-banner">'
            f'<div class="pdf-chapter-label">{html.escape(part["label"])}</div>'
            f'<h1 class="pdf-chapter-title">{html.escape(part["title"])}</h1>'
            + (f'<p class="pdf-chapter-refs">{part["refs"]}</p>' if part.get("refs") else "")
            + f"</div>"
        )
        for sid in part["sectionIds"]:
            s = sec_by_id.get(sid)
            if not s:
                continue
            body_sections.append(
                f'<section class="pdf-section" id="pdf-{s["id"]}">'
                f'<h2 class="pdf-sec-title"><span class="sec-marker-code">{html.escape(s["num"])}</span> {html.escape(s["title"])}</h2>'
                f'{to_pdf_section_html(s["html"])}'
                f"</section>"
            )

    if appendices:
        body_sections.append(
            '<div class="pdf-chapter-banner"><div class="pdf-chapter-label">APPENDICI</div>'
            '<h1 class="pdf-chapter-title">Formulario, Errori Comuni, Glossario e Mappa delle Lezioni</h1></div>'
        )
        for s in appendices:
            body_sections.append(
                f'<section class="pdf-section" id="pdf-{s["id"]}">'
                f'<h2 class="pdf-sec-title"><span class="sec-marker-code">{html.escape(s["num"])}</span> — {html.escape(s["title"])}</h2>'
                f'{to_pdf_section_html(s["html"])}'
                f"</section>"
            )

    katex_uri = KATEX_DIR.as_uri()
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <title>Algebra Lineare e Geometria — Dispensa di Studio</title>
  <link rel="stylesheet" href="{katex_uri}/katex.min.css">
  <style>
    @page {{
      size: A4;
      margin: 18mm 15mm 18mm 15mm;
    }}
    * {{ box-sizing: border-box; }}
    html, body {{
      margin: 0;
      padding: 0;
      font-family: 'Noto Sans', 'Liberation Sans', 'DejaVu Sans', sans-serif;
      font-size: 9.8pt;
      line-height: 1.54;
      color: #181c24;
      background: #ffffff;
    }}
    a {{ color: #1d4ed8; text-decoration: none; }}
    .cover-page {{
      min-height: 250mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 20mm 10mm 14mm;
      border: 1.5px solid #dbe3f0;
      border-radius: 10px;
      background: linear-gradient(180deg, #f8faff 0%, #ffffff 42%, #f9fafb 100%);
      page-break-after: always;
    }}
    .cover-eyebrow {{
      font-size: 8.5pt;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #1e40af;
      margin-bottom: 10px;
    }}
    .cover-title {{
      font-size: 27pt;
      line-height: 1.15;
      font-weight: 800;
      color: #0f172a;
      margin: 0 0 12px;
      letter-spacing: -0.02em;
    }}
    .cover-subtitle {{
      font-size: 13pt;
      color: #334155;
      margin: 0 0 22px;
      line-height: 1.4;
    }}
    .cover-meta-box {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-left: 4px solid #1d4ed8;
      border-radius: 6px;
      padding: 12px 16px;
      font-size: 9.4pt;
      color: #334155;
    }}
    .cover-meta-box p {{ margin: 4px 0; }}
    .cover-footer {{
      border-top: 1px solid #cbd5e1;
      padding-top: 12px;
      font-size: 8.6pt;
      color: #475569;
    }}
    .toc-page {{
      page-break-after: always;
    }}
    .toc-title {{
      font-size: 17pt;
      font-weight: 800;
      color: #0f172a;
      border-bottom: 2px solid #1d4ed8;
      padding-bottom: 6px;
      margin: 0 0 14px;
    }}
    .toc-list {{
      list-style: none;
      padding: 0;
      margin: 0;
    }}
    .toc-intro {{
      margin-bottom: 10px;
      font-weight: 700;
    }}
    .toc-part {{
      margin-bottom: 10px;
    }}
    .toc-part > strong {{
      display: block;
      color: #1e3a8a;
      font-size: 10.2pt;
      margin-bottom: 4px;
    }}
    .toc-sub {{
      list-style: none;
      padding-left: 14px;
      margin: 0;
    }}
    .toc-sub li {{
      margin: 3px 0;
      font-size: 9.3pt;
    }}
    .toc-num {{
      font-family: 'DejaVu Sans Mono', monospace;
      font-weight: 700;
      color: #1d4ed8;
      margin-right: 4px;
    }}
    .pdf-chapter-banner {{
      page-break-before: always;
      margin: 0 0 14px;
      padding: 12px 16px;
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      border-left: 5px solid #1d4ed8;
      border-radius: 6px;
      break-after: avoid;
    }}
    .pdf-chapter-label {{
      font-family: 'DejaVu Sans Mono', monospace;
      font-size: 8.2pt;
      font-weight: 700;
      color: #1d4ed8;
      letter-spacing: 0.06em;
    }}
    .pdf-chapter-title {{
      margin: 3px 0 4px;
      font-size: 16pt;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.25;
    }}
    .pdf-chapter-refs {{
      margin: 0;
      font-size: 8.5pt;
      color: #475569;
    }}
    .pdf-section {{
      margin-bottom: 22px;
    }}
    .pdf-sec-kicker {{
      font-family: 'DejaVu Sans Mono', monospace;
      font-size: 8pt;
      font-weight: 700;
      color: #1d4ed8;
      letter-spacing: 0.05em;
    }}
    .sec-marker-code {{
      font-family: 'DejaVu Sans Mono', monospace;
      color: #1d4ed8;
    }}
    h2.pdf-sec-title {{
      font-size: 13.5pt;
      font-weight: 800;
      color: #0f172a;
      margin: 12px 0 10px;
      padding-bottom: 5px;
      border-bottom: 1.5px solid #cbd5e1;
      break-after: avoid;
    }}
    h3 {{
      font-size: 10.8pt;
      font-weight: 700;
      color: #1e40af;
      margin: 14px 0 6px;
      break-after: avoid;
    }}
    h4 {{
      font-size: 9.8pt;
      font-weight: 700;
      color: #1e293b;
      margin: 10px 0 5px;
      break-after: avoid;
    }}
    p {{ margin: 0 0 7px; }}
    ul, ol {{ margin: 0 0 8px; padding-left: 18px; }}
    li {{ margin-bottom: 3px; }}
    code {{
      font-family: 'DejaVu Sans Mono', monospace;
      font-size: 8.6pt;
      background: #f1f5f9;
      padding: 1px 4px;
      border-radius: 3px;
      border: 1px solid #e2e8f0;
    }}
    pre {{
      white-space: pre-wrap;
      word-break: break-word;
      overflow-wrap: anywhere;
    }}
    .table-wrap {{
      margin: 10px 0 12px;
      break-inside: avoid;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 8.7pt;
    }}
    thead th {{
      background: #f1f5f9;
      color: #0f172a;
      font-weight: 700;
      text-align: left;
      padding: 6px 8px;
      border: 1px solid #cbd5e1;
    }}
    tbody td {{
      padding: 6px 8px;
      border: 1px solid #cbd5e1;
      vertical-align: top;
    }}
    tbody tr:nth-child(even) {{
      background: #f8fafc;
    }}
    .callout {{
      margin: 10px 0;
      padding: 9px 12px;
      border-radius: 6px;
      border: 1px solid #cbd5e1;
      border-left-width: 4px;
    }}
    .callout-def, .callout-thm, .callout-warn, .callout-note, .callout-tip {{
      break-inside: avoid;
    }}
    .callout-title {{
      font-family: 'Noto Sans', 'Liberation Sans', 'DejaVu Sans', sans-serif;
      font-size: 9pt;
      font-weight: 700;
      letter-spacing: 0.01em;
      margin-bottom: 4px;
      break-after: avoid;
    }}
    .callout-body > :last-child {{ margin-bottom: 0; }}
    .callout-def {{ background: #eff6ff; border-color: #bfdbfe; border-left-color: #2563eb; }}
    .callout-def .callout-title {{ color: #1d4ed8; }}
    .callout-thm {{ background: #f5f3ff; border-color: #ddd6fe; border-left-color: #7c3aed; }}
    .callout-thm .callout-title {{ color: #6d28d9; }}
    .callout-proof {{ background: #ecfdf5; border-color: #a7f3d0; border-left-color: #059669; }}
    .callout-proof .callout-title {{ color: #047857; }}
    .callout-warn {{ background: #fff1f2; border-color: #fecdd3; border-left-color: #e11d48; }}
    .callout-warn .callout-title {{ color: #be123c; }}
    .callout-note {{ background: #fffbeb; border-color: #fde68a; border-left-color: #d97706; }}
    .callout-note .callout-title {{ color: #b45309; }}
    .callout-tip {{ background: #f0fdf4; border-color: #bbf7d0; border-left-color: #16a34a; }}
    .callout-tip .callout-title {{ color: #15803d; }}
    .callout-exercise {{ background: #f0f9ff; border-color: #bae6fd; border-left-color: #0284c7; }}
    .callout-exercise .callout-title {{ color: #0369a1; }}
    .callout-example {{ background: #f8fafc; border-color: #cbd5e1; border-left-color: #334155; }}
    .callout-example .callout-title {{ color: #1e293b; }}

    .solution-box-pdf {{
      margin-top: 8px;
      padding: 7px 10px;
      border-radius: 5px;
      background: #ffffff;
      border: 1px solid #bae6fd;
    }}
    .solution-title-pdf {{
      font-weight: 700;
      font-size: 8.8pt;
      color: #0369a1;
      margin-bottom: 4px;
      border-bottom: 1px solid #e0f2fe;
      padding-bottom: 3px;
      break-after: avoid;
    }}
    .solution-body > :last-child {{ margin-bottom: 0; }}
    .int-badge {{
      font-family: 'DejaVu Sans Mono', monospace;
      font-size: 7.8pt;
      font-weight: 700;
      color: #92400e;
      background: #fef3c7;
      border: 1px solid #fcd34d;
      padding: 0 4px;
      border-radius: 3px;
    }}
    .math-display {{
      margin: 7px 0;
      break-inside: avoid;
    }}
    .katex {{ font-size: 1.0em; }}
    .svg-diagram {{
      display: block;
      max-width: 92%;
      height: auto;
      margin: 10px auto;
      background: #0f172a;
      border-radius: 6px;
      padding: 8px;
      break-inside: avoid;
    }}
  </style>
</head>
<body>
  <div class="cover-page">
    <div>
      <div class="cover-eyebrow">Università degli Studi di Catania · Informatica (Canale F–N) · A.A. 2026</div>
      <h1 class="cover-title">Algebra Lineare e Geometria</h1>
      <p class="cover-subtitle">Dispensa di Studio Completa, Dimostrazioni ed Esercizi Svolti dai Lucidi del Corso</p>
      <div class="cover-meta-box">
        <p><strong>Docente titolare:</strong> Prof. Giuseppe Zappalà</p>
        <p><strong>Fonte primaria:</strong> Raccolta delle 15 lezioni del corso (<code>Lez00</code>–<code>Lez14</code>)</p>
        <p><strong>Notazioni:</strong> Fedeli al 100% agli appunti del docente ($K^{{m,n}}$, $\\operatorname{{ent}}_{{ij}}(A)$, ${{}}^t A$, $\\operatorname{{rk}} A$, $\\mathcal{{L}}(S)$, $P_A(x)$, $V_\\lambda$)</p>
        <p><strong>Stato pubblicazione:</strong> {html.escape(chapters_included)}</p>
      </div>
    </div>
    <div class="cover-footer">
      <p><strong>Nota d'uso:</strong> Ogni argomento segue una struttura fissa in 7 passi (idea semplice, definizioni/teoremi, dimostrazioni viste a lezione, esempi svolti, errori comuni, riepilogo ed esercizi originali risolti passo-passo).</p>
    </div>
  </div>

  <div class="toc-page">
    <h1 class="toc-title">Indice Generale</h1>
    <ul class="toc-list">
      {"".join(toc_entries)}
    </ul>
  </div>

  {"".join(body_sections)}

  <script src="{katex_uri}/katex.min.js"></script>
  <script src="{katex_uri}/auto-render.min.js"></script>
  <script>
    window.__KATEX_DONE = false;
    window.__KATEX_ERROR_COUNT = 0;
    document.addEventListener("DOMContentLoaded", function () {{
      renderMathInElement(document.body, {{
        delimiters: [
          {{ left: "$$", right: "$$", display: true }},
          {{ left: "$", right: "$", display: false }},
          {{ left: "\\\\[", right: "\\\\]", display: true }},
          {{ left: "\\\\(", right: "\\\\)", display: false }}
        ],
        throwOnError: false
      }});
      window.__KATEX_ERROR_COUNT = document.querySelectorAll(".katex-error").length;
      window.__KATEX_DONE = true;
    }});
  </script>
</body>
</html>
"""


def render_pdf(
    parts: list[dict] | None = None,
    verify_screenshots: bool = False,
    screenshot_dir: Path | None = None,
) -> None:
    """Genera dispensa_algebra_lineare.pdf tramite Chromium headless verificando 0 errori KaTeX e JS."""
    if not VENV_PYTHON.exists():
        raise FileNotFoundError(f"Virtualenv Playwright mancante in {VENV_PYTHON}")

    shots_dir = screenshot_dir or DEFAULT_SCREENSHOT_DIR
    if verify_screenshots:
        shots_dir.mkdir(parents=True, exist_ok=True)

    latest_preview_id = "intro"
    if parts:
        last_secs = parts[-1].get("sectionIds") or []
        if len(last_secs) > 1:
            latest_preview_id = last_secs[1]
        elif last_secs:
            latest_preview_id = last_secs[0]

    header_tpl = (
        '<div style="width:100%;font-size:7.5px;color:#64748b;padding:0 15mm;'
        'display:flex;justify-content:space-between;font-family:sans-serif;">'
        '<span>Algebra Lineare e Geometria — Dispensa di Studio</span>'
        '<span>Prof. G. Zappalà (A.A. 2026)</span>'
        '</div>'
    )
    footer_tpl = (
        '<div style="width:100%;font-size:7.5px;color:#64748b;padding:0 15mm;'
        'display:flex;justify-content:space-between;font-family:sans-serif;">'
        '<span>Corso di Laurea in Informatica (F–N)</span>'
        '<span>Pagina <span class="pageNumber"></span> di <span class="totalPages"></span></span>'
        '</div>'
    )

    job_cfg = {
        "print_uri": PRINT_HTML_PATH.as_uri(),
        "pdf_path": str(PDF_PATH),
        "verify_shots": verify_screenshots,
        "shots_dir": str(shots_dir),
        "latest_preview_id": latest_preview_id,
        "header_tpl": header_tpl,
        "footer_tpl": footer_tpl,
    }

    runner_code = """
import json, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

cfg = json.loads(sys.stdin.read())
print_uri = cfg["print_uri"]
pdf_path = cfg["pdf_path"]
verify_shots = cfg["verify_shots"]
shots_dir = Path(cfg["shots_dir"])
latest_preview_id = cfg["latest_preview_id"]
header_tpl = cfg["header_tpl"]
footer_tpl = cfg["footer_tpl"]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    errors_pdf = []
    page.on("pageerror", lambda e: errors_pdf.append(str(e)))
    page.goto(print_uri, wait_until="load")
    page.wait_for_function("() => window.__KATEX_DONE === true")
    page.evaluate("() => document.fonts.ready")
    katex_errs = page.evaluate('''() => {
        const els = Array.from(document.querySelectorAll(".katex-error"));
        return els.map(e => ({ title: e.getAttribute("title"), text: e.textContent }));
    }''')
    if katex_errs or errors_pdf:
        print("PDF KaTeX/JS errors:", json.dumps({"katex": katex_errs, "js": errors_pdf}, ensure_ascii=False))
        browser.close()
        sys.exit(1)

    page.pdf(
        path=pdf_path,
        format="A4",
        margin={"top": "18mm", "bottom": "18mm", "left": "15mm", "right": "15mm"},
        print_background=True,
        display_header_footer=True,
        header_template=header_tpl,
        footer_template=footer_tpl,
    )
    if verify_shots:
        page.set_viewport_size({"width": 794, "height": 1123})
        page.screenshot(path=str(shots_dir / "pdf_cover_preview.png"))
        target_sec = page.locator(f"#pdf-{latest_preview_id}")
        if target_sec.count():
            step4 = target_sec.locator("h3").filter(has_text="4. Esempi").first
            if step4.count():
                step4.scroll_into_view_if_needed()
            else:
                target_sec.scroll_into_view_if_needed()
            page.screenshot(path=str(shots_dir / "pdf_latest_preview.png"))
    page.close()
    browser.close()
print("PDF_PLAYWRIGHT_OK")
"""
    res = subprocess.run(
        [str(VENV_PYTHON), "-c", runner_code],
        input=json.dumps(job_cfg),
        capture_output=True,
        text=True,
        check=False,
    )
    if res.returncode != 0:
        raise RuntimeError(
            f"Errore Playwright PDF (exit {res.returncode}):\nSTDOUT:\n{res.stdout}\nSTDERR:\n{res.stderr}"
        )


def verify_site(
    parts: list[dict],
    sections: list[dict],
    verify_screenshots: bool = False,
    screenshot_dir: Path | None = None,
) -> None:
    """Verifica tutte le viste del sito (dopo il popolamento di page mapping) e salva screenshot opzionali."""
    if not VENV_PYTHON.exists():
        raise FileNotFoundError(f"Virtualenv Playwright mancante in {VENV_PYTHON}")

    shots_dir = screenshot_dir or DEFAULT_SCREENSHOT_DIR
    if verify_screenshots:
        shots_dir.mkdir(parents=True, exist_ok=True)

    sec_ids = [s["id"] for s in sections]
    latest_preview_id = sec_ids[-1] if sec_ids else "home"
    if parts:
        last_secs = parts[-1].get("sectionIds") or []
        if len(last_secs) > 1:
            latest_preview_id = last_secs[1]
        elif last_secs:
            latest_preview_id = last_secs[0]

    job_cfg = {
        "site_uri": (SITO_DIR / "index.html").as_uri(),
        "sec_ids": sec_ids,
        "latest_preview_id": latest_preview_id,
        "verify_shots": verify_screenshots,
        "shots_dir": str(shots_dir),
    }

    runner_code = """
import json, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

cfg = json.loads(sys.stdin.read())
site_uri = cfg["site_uri"]
sec_ids = cfg["sec_ids"]
latest_preview_id = cfg["latest_preview_id"]
verify_shots = cfg["verify_shots"]
shots_dir = Path(cfg["shots_dir"])

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    sp = browser.new_page(viewport={"width": 1366, "height": 860})
    site_errs = []
    sp.on("pageerror", lambda e: site_errs.append(str(e)))
    sp.on("console", lambda msg: site_errs.append(msg.text) if msg.type == "error" else None)

    routes = ["home"] + sec_ids
    for r in routes:
        sp.goto(f"{site_uri}#{r}", wait_until="load")
        sp.wait_for_timeout(120)
        errs = sp.evaluate('''() => Array.from(document.querySelectorAll(".katex-error")).map(e => ({
            title: e.getAttribute("title"),
            text: e.textContent
        }))''')
        if errs:
            print(f"Site KaTeX errors on #{r}:", json.dumps(errs, ensure_ascii=False))
            browser.close()
            sys.exit(1)
        if verify_shots and r == "home":
            sp.screenshot(path=str(shots_dir / "site_home_desktop.png"))
        if verify_shots and r == latest_preview_id:
            sp.screenshot(path=str(shots_dir / "site_latest_desktop.png"))
            step4 = sp.locator("#step-4")
            if step4.count():
                step4.scroll_into_view_if_needed()
                sp.wait_for_timeout(80)
                sp.screenshot(path=str(shots_dir / "site_latest_math_desktop.png"))

    if verify_shots:
        mp = browser.new_page(viewport={"width": 390, "height": 844})
        mp.goto(f"{site_uri}#{latest_preview_id}", wait_until="load")
        mp.wait_for_timeout(120)
        step4 = mp.locator("#step-4")
        if step4.count():
            step4.scroll_into_view_if_needed()
            mp.wait_for_timeout(80)
        mp.screenshot(path=str(shots_dir / "site_latest_mobile.png"))
        mp.close()

    if site_errs:
        print("Site JS/Console errors:", json.dumps(site_errs, ensure_ascii=False))
        browser.close()
        sys.exit(1)

    browser.close()
print("SITE_PLAYWRIGHT_OK")
"""
    res = subprocess.run(
        [str(VENV_PYTHON), "-c", runner_code],
        input=json.dumps(job_cfg),
        capture_output=True,
        text=True,
        check=False,
    )
    if res.returncode != 0:
        raise RuntimeError(
            f"Errore Playwright Sito (exit {res.returncode}):\nSTDOUT:\n{res.stdout}\nSTDERR:\n{res.stderr}"
        )


def map_pdf_pages(sections: list[dict]) -> int:
    """Estrae il testo del PDF con pdftotext, verifica assenza di LaTeX grezzo e assegna startPage/endPage reali."""
    proc = subprocess.run(
        ["pdftotext", str(PDF_PATH), "-"],
        capture_output=True,
        text=True,
        check=True,
    )
    raw_tex_hits = re.findall(
        r"\\begin\{|\\end\{|\\stackrel\{|\\operatorname\{|\\mathbb\{|\\mathcal\{|\$\$",
        proc.stdout,
    )
    if raw_tex_hits:
        raise ValueError(
            f"Trovati frammenti LaTeX non renderizzati nel PDF ({len(raw_tex_hits)} occorrenze), "
            f"primo hit: {raw_tex_hits[0]!r}"
        )

    raw_pages = proc.stdout.split("\f")
    if raw_pages and not raw_pages[-1].strip():
        raw_pages.pop()
    total_pages = len(raw_pages)

    # Salta copertina e tutte le pagine dell'indice generale cercando il corpo dell'Introduzione
    norm_pages = [normalize_text(p) for p in raw_pages]

    search_from = 2 if total_pages >= 3 else 0
    found_intro = False
    for idx in range(1, min(10, total_pages)):
        if "introduzione al corso" in norm_pages[idx]:
            search_from = idx
            found_intro = True
    if not found_intro:
        for idx in range(1, min(10, total_pages)):
            if "indice generale" in norm_pages[idx]:
                search_from = idx + 1

    starts: list[int] = []
    cur_min = search_from
    for sec in sections:
        if sec["id"] == "intro":
            needle = normalize_text(sec["title"])
        elif sec["kind"] == "appendix":
            needle = normalize_text(f"{sec['num']} — {sec['title']}")
        else:
            needle = normalize_text(f"{sec['num']} {sec['title']}")

        found_page = cur_min + 1  # 1-based fallback
        for p_idx in range(cur_min, total_pages):
            if needle in norm_pages[p_idx]:
                found_page = p_idx + 1
                cur_min = p_idx
                break
        else:
            # Fallback più corto con titolo
            short_needle = normalize_text(sec["title"])
            for p_idx in range(cur_min, total_pages):
                if short_needle in norm_pages[p_idx]:
                    found_page = p_idx + 1
                    cur_min = p_idx
                    break
        starts.append(found_page)

    for i, sec in enumerate(sections):
        start_p = starts[i]
        if i + 1 < len(sections):
            next_p = starts[i + 1]
            end_p = max(start_p, next_p - 1 if next_p > start_p else start_p)
        else:
            end_p = max(start_p, total_pages)
        sec["startPage"] = start_p
        sec["endPage"] = end_p

    return total_pages


def write_book_data_js(
    parts: list[dict],
    sections: list[dict],
    search_blocks: list[dict],
    total_pages: int,
) -> None:
    clean_sections = []
    for s in sections:
        clean_sections.append(
            {
                "id": s["id"],
                "num": s["num"],
                "title": s["title"],
                "kind": s["kind"],
                "partId": s["partId"],
                "startPage": s["startPage"],
                "endPage": s["endPage"],
                "toc": s["toc"],
                "html": s["html"],
            }
        )

    book_data = {
        "meta": {
            "title": "Algebra Lineare e Geometria",
            "subtitle": "Dispensa Completa di Studio ed Esercizi Svolti (da Zero all'Esame)",
            "course": "CORSO UNIVERSITARIO · INFORMATICA (F–N) · A.A. 2026",
            "attribution": (
                "<strong>Basata integralmente sui 15 PDF delle lezioni del Prof. Giuseppe Zappalà "
                "(Università degli Studi di Catania — DMI), mantenendo ordine, notazioni ed esercizi del corso.</strong>"
            ),
            "totalPages": total_pages,
        },
        "parts": parts,
        "sections": clean_sections,
        "searchBlocks": search_blocks,
    }
    DATA_JS_PATH.parent.mkdir(parents=True, exist_ok=True)
    DATA_JS_PATH.write_text(
        "window.BOOK_DATA = " + json.dumps(book_data, ensure_ascii=False, separators=(",", ":")) + ";\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Compila PDF e sito di Algebra Lineare.")
    parser.add_argument(
        "--verify-screenshots",
        action="store_true",
        help="Salva screenshot di verifica di PDF e sito nella cartella scratch.",
    )
    parser.add_argument(
        "--strict-xrefs",
        action="store_true",
        help="Fallisce se esistono link interni (#sec-... / #app-...) verso sezioni mancanti.",
    )
    args = parser.parse_args()

    parts, sections, search_blocks = load_dispensa(strict_xrefs=args.strict_xrefs)
    TEMP_PRINT_DIR.mkdir(parents=True, exist_ok=True)
    PRINT_HTML_PATH.write_text(build_pdf_body_html(parts, sections), encoding="utf-8")

    # 1. Genera PDF e verifica 0 errori KaTeX / JS in stampa
    render_pdf(parts=parts, verify_screenshots=args.verify_screenshots)

    # 2. Mappa numeri di pagina reali dal PDF e genera book-data.js definitivo
    total_pages = map_pdf_pages(sections)
    write_book_data_js(parts, sections, search_blocks, total_pages=total_pages)

    # 3. Verifica tutte le viste del sito (ora con numeri di pagina popolati)
    verify_site(parts, sections, verify_screenshots=args.verify_screenshots)

    print(
        f"Build completata: {len(parts)} capitoli, {len(sections)} sezioni, "
        f"{len(search_blocks)} blocchi indicizzati, {total_pages} pagine PDF."
    )


if __name__ == "__main__":
    main()
