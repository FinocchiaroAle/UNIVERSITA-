(function () {
  "use strict";

  const BOOK = window.BOOK_DATA;
  if (!BOOK || !Array.isArray(BOOK.sections)) {
    document.getElementById("main-content").innerHTML =
      '<div style="padding:24px;color:#f3a1a8;">Errore: impossibile caricare <code>data/book-data.js</code>.</div>';
    return;
  }

  const secById = Object.create(null);
  const partById = Object.create(null);
  const secOrder = [];
  const partSecMeta = Object.create(null);

  (BOOK.parts || []).forEach((p) => {
    partById[p.id] = p;
  });
  BOOK.sections.forEach((s, idx) => {
    secById[s.id] = s;
    partSecMeta[s.id] = {
      idx,
      normTitle: normalizeStr(`${s.num} ${s.title}`),
    };
    secOrder.push(s.id);
  });

  const appendices = BOOK.sections.filter((s) => s.kind === "appendix");
  const introSec = secById["intro"] || null;

  // State
  let activePartFilter = "all";
  let modalScope = "all";
  let modalResults = [];
  let modalSelectedIdx = -1;
  let homeResults = [];
  let homeSelectedIdx = -1;
  let scrollObserver = null;

  // DOM refs
  const bodyEl = document.body;
  const menuBtn = document.getElementById("menu-btn");
  const drawerBackdrop = document.getElementById("drawer-backdrop");
  const drawerFilter = document.getElementById("drawer-filter");
  const drawerNav = document.getElementById("drawer-nav");
  const homeView = document.getElementById("home-view");
  const readerView = document.getElementById("reader-view");
  const backToTopBtn = document.getElementById("back-to-top");

  const openSearchBtn = document.getElementById("open-search-btn");
  const searchModal = document.getElementById("search-modal");
  const searchBackdrop = document.getElementById("search-modal-backdrop");
  const modalSearchInput = document.getElementById("modal-search-input");
  const closeSearchBtn = document.getElementById("close-search-btn");
  const modalScopeBar = document.getElementById("modal-scope-bar");
  const modalSearchMeta = document.getElementById("modal-search-meta");
  const modalSearchResults = document.getElementById("modal-search-results");

  function renderMath(el) {
    if (!el || typeof window.renderMathInElement !== "function") return;
    window.renderMathInElement(el, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false },
        { left: "\\[", right: "\\]", display: true },
        { left: "\\(", right: "\\)", display: false },
      ],
      throwOnError: false,
    });
  }

  function formatPagesShort(sec) {
    if (!sec.startPage) return "";
    if (!sec.endPage || sec.endPage <= sec.startPage) return `p. ${sec.startPage}`;
    return `p. ${sec.startPage}–${sec.endPage}`;
  }

  function formatPagesFull(sec) {
    if (!sec.startPage) return "Dispensa PDF";
    if (!sec.endPage || sec.endPage <= sec.startPage) return `Dispensa PDF · Pag. ${sec.startPage}`;
    return `Dispensa PDF · Pag. ${sec.startPage}–${sec.endPage}`;
  }

  function normalizeStr(str) {
    return (str || "")
      .toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/\s+/g, " ")
      .trim();
  }

  function escapeHtml(str) {
    return (str || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function escapeRegExp(str) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  function tokenizeQuery(q) {
    const n = normalizeStr(q);
    if (!n) return [];
    const raw = n.split(" ").filter(Boolean);
    return Array.from(new Set(raw));
  }

  function highlightSnippet(plainText, rawQuery) {
    const tokens = tokenizeQuery(rawQuery);
    const maxLen = 195;
    const normPlain = normalizeStr(plainText);

    let firstIdx = -1;
    for (const tok of tokens) {
      const i = normPlain.indexOf(tok);
      if (i !== -1 && (firstIdx === -1 || i < firstIdx)) {
        firstIdx = i;
      }
    }

    let snippet = plainText;
    if (plainText.length > maxLen) {
      const start = Math.max(0, firstIdx > 45 ? firstIdx - 45 : 0);
      const end = Math.min(plainText.length, start + maxLen);
      snippet = (start > 0 ? "…" : "") + plainText.slice(start, end).trim() + (end < plainText.length ? "…" : "");
    }

    let escaped = escapeHtml(snippet);
    if (!tokens.length) return escaped;

    const accentMap = {
      a: "[aàá]",
      e: "[eèé]",
      i: "[iìí]",
      o: "[oòó]",
      u: "[uùú]",
    };
    const patterns = tokens
      .filter((t) => t.length >= 1)
      .sort((a, b) => b.length - a.length)
      .map((t) =>
        escapeRegExp(t)
          .split("")
          .map((ch) => accentMap[ch] || ch)
          .join("")
      );
    if (!patterns.length) return escaped;
    const re = new RegExp(`(${patterns.join("|")})`, "gi");
    return escaped.replace(re, "<mark>$1</mark>");
  }

  const KIND_LABEL = {
    section: "Argomento",
    def: "Definizione",
    thm: "Teorema / Prop.",
    proof: "Dimostrazione",
    glossary: "Glossario",
    formula: "Formulario",
    heading: "Sottotitolo",
    table: "Tabella",
    exercise: "Esercizio",
    example: "Esempio",
    list: "Punto chiave",
    warn: "Errore comune",
    note: "Nota",
    tip: "Idea / Consiglio",
    text: "Testo",
  };

  function runSearch(rawQuery, scope) {
    const tokens = tokenizeQuery(rawQuery);
    const normQ = normalizeStr(rawQuery);
    if (!tokens.length) return { total: 0, items: [] };

    const results = [];

    // 1. Search section titles directly
    if (scope === "all" || scope === "heading") {
      for (const s of BOOK.sections) {
        const titleNorm = partSecMeta[s.id].normTitle;
        if (tokens.every((tok) => titleNorm.includes(tok))) {
          let score = 320;
          if (titleNorm.includes(normQ)) score += 120;
          if ((s.num || "").toLowerCase() === normQ) score += 250;
          results.push({
            secId: s.id,
            bid: "",
            kind: "section",
            secLabel: s.kind === "section" ? `${s.num} ${s.title}` : s.title,
            ctx: s.kind === "appendix" ? "Appendici" : (partById[s.partId] ? `${partById[s.partId].label} — ${partById[s.partId].title}` : "Introduzione"),
            text: `${s.num ? s.num + " — " : ""}${s.title}${s.startPage ? " (" + formatPagesShort(s) + ")" : ""}`,
            score,
          });
        }
      }
    }

    // 2. Search indexed blocks
    const blocks = BOOK.searchBlocks || [];
    for (let i = 0; i < blocks.length; i++) {
      const blk = blocks[i];
      if (scope === "ref") {
        const isRef =
          blk.k === "def" ||
          blk.k === "thm" ||
          blk.k === "glossary" ||
          blk.k === "formula" ||
          blk.s === "app-a" ||
          blk.s === "app-c";
        if (!isRef) continue;
      } else if (scope === "heading") {
        if (blk.k !== "heading") continue;
      } else if (scope === "ex") {
        if (blk.k !== "exercise" && blk.k !== "example") continue;
      }

      const sec = secById[blk.s];
      if (!sec) continue;

      const haystack = blk.n;
      let allMatch = true;
      for (let t = 0; t < tokens.length; t++) {
        if (!haystack.includes(tokens[t])) {
          allMatch = false;
          break;
        }
      }
      if (!allMatch) continue;

      let score = 70;
      if (blk.k === "def") score = 240;
      else if (blk.k === "thm") score = 225;
      else if (blk.k === "glossary") score = 220;
      else if (blk.k === "formula") score = 190;
      else if (blk.k === "heading") score = 160;
      else if (blk.k === "exercise") score = 120;
      else if (blk.k === "example") score = 110;
      else if (blk.k === "table") score = 105;
      else if (blk.k === "list") score = 85;

      const firstPos = haystack.indexOf(tokens[0]);
      if (firstPos >= 0 && firstPos < 28) score += 75;
      if (haystack.includes(normQ)) score += 65;

      if (tokens.length === 1 && tokens[0].length <= 16) {
        const wb = new RegExp(`(?:^|[^a-z0-9_])${escapeRegExp(tokens[0])}(?:$|[^a-z0-9_])`);
        if (wb.test(haystack)) score += 55;
      }

      results.push({
        secId: blk.s,
        bid: blk.b,
        kind: blk.k,
        secLabel: sec.kind === "section" ? `${sec.num} ${sec.title}` : (sec.kind === "appendix" ? `${sec.num} — ${sec.title}` : sec.title),
        ctx: blk.h || sec.title,
        text: blk.t,
        score,
      });
    }

    results.sort((a, b) => b.score - a.score);

    const seen = new Set();
    const deduped = [];
    for (const r of results) {
      const key = `${r.secId}:${r.bid}`;
      if (seen.has(key)) continue;
      seen.add(key);
      deduped.push(r);
    }

    return {
      total: deduped.length,
      items: deduped.slice(0, 45),
    };
  }

  function renderResultList(container, items, rawQuery, selectedIdx, onSelect) {
    if (!items.length) {
      container.innerHTML =
        '<div class="search-empty">Nessun risultato trovato. Prova con un termine diverso (es. <code>determinante</code>, <code>Rouché-Capelli</code>, <code>Grassmann</code>, <code>autovalore</code>, <code>diagonalizzabile</code>, <code>matrice inversa</code>).</div>';
      return;
    }

    container.innerHTML = items
      .map((it, idx) => {
        const href = buildResultHref(it.secId, it.bid, rawQuery);
        const cls = idx === selectedIdx ? "search-result-item selected" : "search-result-item";
        const kindLabel = KIND_LABEL[it.kind] || it.kind;
        const showCtx = it.ctx && it.ctx !== it.secLabel;
        return (
          `<a class="${cls}" href="${href}" data-ridx="${idx}" role="option" aria-selected="${idx === selectedIdx}">` +
          `<div class="sr-top">` +
          `<span class="sr-sec">${escapeHtml(it.secLabel)}</span>` +
          `<span class="sr-kind">${escapeHtml(kindLabel)}</span>` +
          `</div>` +
          (showCtx ? `<div class="sr-ctx">${escapeHtml(it.ctx)}</div>` : "") +
          `<div class="sr-snippet">${highlightSnippet(it.text, rawQuery)}</div>` +
          `</a>`
        );
      })
      .join("");

    container.querySelectorAll(".search-result-item").forEach((el) => {
      el.addEventListener("click", (e) => {
        if (onSelect) onSelect(e, el);
      });
    });
  }

  function buildResultHref(secId, bid, rawQuery) {
    const params = new URLSearchParams();
    if (bid) params.set("b", bid);
    if (rawQuery && rawQuery.trim()) params.set("q", rawQuery.trim());
    const qs = params.toString();
    return `#${secId}${qs ? "?" + qs : ""}`;
  }

  // ================= DRAWER =================
  function renderDrawer(activeSecId, filterText) {
    const ft = normalizeStr(filterText);

    const makeSecLink = (sec) => {
      const active = sec.id === activeSecId ? " active" : "";
      const numTxt = sec.kind === "section" ? sec.num : (sec.kind === "appendix" ? sec.num.replace("Appendice ", "App. ") : "Intro");
      return (
        `<a class="drawer-item${active}" href="#${sec.id}" data-sec-id="${sec.id}">` +
        `<span class="drawer-item-num">${escapeHtml(numTxt)}</span>` +
        `<span>${escapeHtml(sec.title)}</span>` +
        `</a>`
      );
    };

    const matchesFilter = (sec) => {
      if (!ft) return true;
      return partSecMeta[sec.id].normTitle.includes(ft);
    };

    let html = "";
    if (!ft) {
      html += `<a class="drawer-item${activeSecId === "home" ? " active" : ""}" href="#home"><span class="drawer-item-num">Home</span><span>Indice Generale</span></a>`;
      if (introSec) {
        html += makeSecLink(introSec);
      }
    } else if (introSec && matchesFilter(introSec)) {
      html += makeSecLink(introSec);
    }

    for (const part of BOOK.parts) {
      const partSecs = part.sectionIds.map((id) => secById[id]).filter(Boolean);
      const filteredSecs = partSecs.filter(matchesFilter);
      if (ft && !filteredSecs.length) continue;

      const containsActive = part.sectionIds.includes(activeSecId);
      const collapsedClass = !ft && activeSecId !== "home" && !containsActive ? " collapsed" : "";
      html +=
        `<div class="drawer-group${collapsedClass}" data-group="${part.id}">` +
        `<button class="drawer-group-btn" type="button">` +
        `<span>${escapeHtml(part.label)} · ${escapeHtml(part.title)}</span>` +
        `<svg class="drawer-group-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><polyline points="6 9 12 15 18 9"/></svg>` +
        `</button>` +
        `<div class="drawer-group-list">${filteredSecs.map(makeSecLink).join("")}</div>` +
        `</div>`;
    }

    const filteredApp = appendices.filter(matchesFilter);
    if (appendices.length && (!ft || filteredApp.length)) {
      const containsApp = appendices.some((a) => a.id === activeSecId);
      const collapsedClass = !ft && activeSecId !== "home" && !containsApp ? " collapsed" : "";
      html +=
        `<div class="drawer-group${collapsedClass}" data-group="appendices">` +
        `<button class="drawer-group-btn" type="button">` +
        `<span>Appendici (A–E)</span>` +
        `<svg class="drawer-group-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><polyline points="6 9 12 15 18 9"/></svg>` +
        `</button>` +
        `<div class="drawer-group-list">${filteredApp.map(makeSecLink).join("")}</div>` +
        `</div>`;
    }

    if (!html) {
      html = '<div class="search-empty">Nessun argomento trovato nell\'indice.</div>';
    }

    drawerNav.innerHTML = html;

    drawerNav.querySelectorAll(".drawer-group-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        btn.parentElement.classList.toggle("collapsed");
      });
    });

    drawerNav.querySelectorAll(".drawer-item").forEach((link) => {
      link.addEventListener("click", () => {
        if (window.innerWidth <= 1024) {
          closeMobileDrawer();
        }
      });
    });

    const activeLink = drawerNav.querySelector(".drawer-item.active");
    if (activeLink) {
      activeLink.scrollIntoView({ block: "nearest" });
    }
  }

  function isMobile() {
    return window.innerWidth <= 1024;
  }

  function closeMobileDrawer() {
    bodyEl.classList.remove("drawer-open-mobile");
    drawerBackdrop.hidden = true;
    menuBtn.setAttribute("aria-expanded", "false");
  }

  function toggleDrawer() {
    if (isMobile()) {
      const opening = !bodyEl.classList.contains("drawer-open-mobile");
      bodyEl.classList.toggle("drawer-open-mobile", opening);
      drawerBackdrop.hidden = !opening;
      menuBtn.setAttribute("aria-expanded", String(opening));
    } else {
      const collapsed = bodyEl.classList.toggle("drawer-collapsed");
      menuBtn.setAttribute("aria-expanded", String(!collapsed));
    }
  }

  // ================= HOME VIEW =================
  function renderHome() {
    readerView.hidden = true;
    homeView.hidden = false;
    document.title = `${BOOK.meta.title} — Indice & Ricerca`;

    const allLabel = `Tutte (${BOOK.parts.length} ${BOOK.parts.length === 1 ? "Capitolo" : "Capitoli"}${appendices.length ? " + Appendici" : ""})`;
    const partFilterButtons = [
      `<button class="filter-chip${activePartFilter === "all" ? " active" : ""}" data-pfilter="all" type="button">${escapeHtml(allLabel)}</button>`,
      ...BOOK.parts.map(
        (p) =>
          `<button class="filter-chip${activePartFilter === p.id ? " active" : ""}" data-pfilter="${p.id}" type="button">${escapeHtml(p.label)}</button>`
      ),
      ...(appendices.length
        ? [`<button class="filter-chip${activePartFilter === "appendices" ? " active" : ""}" data-pfilter="appendices" type="button">Appendici</button>`]
        : []),
    ].join("");

    const cardsHtml = [];

    for (const part of BOOK.parts) {
      if (activePartFilter !== "all" && activePartFilter !== part.id) continue;
      const partSecs = part.sectionIds.map((id) => secById[id]).filter(Boolean);
      const rows = partSecs
        .map(
          (s) =>
            `<a class="sec-row" href="#${s.id}">` +
            `<span class="sec-row-left">` +
            `<span class="sec-row-num">${escapeHtml(s.num)}</span>` +
            `<span class="sec-row-title">${escapeHtml(s.title)}</span>` +
            `</span>` +
            `<span class="sec-row-pages">${escapeHtml(formatPagesShort(s))}</span>` +
            `</a>`
        )
        .join("");

      cardsHtml.push(
        `<section class="part-card${BOOK.parts.length === 1 && !appendices.length ? " wide" : ""}">` +
        `<div class="part-card-head">` +
        `<span class="part-badge">${escapeHtml(part.label)}</span>` +
        `<h2 class="part-card-title">${escapeHtml(part.title)}</h2>` +
        (part.refs ? `<p class="part-card-refs">${part.refs}</p>` : "") +
        `</div>` +
        `<div class="sec-list">${rows}</div>` +
        `</section>`
      );
    }

    if (appendices.length && (activePartFilter === "all" || activePartFilter === "appendices")) {
      const appRows = appendices
        .map(
          (s) =>
            `<a class="sec-row" href="#${s.id}">` +
            `<span class="sec-row-left">` +
            `<span class="sec-row-num">${escapeHtml(s.num.replace("Appendice ", "App. "))}</span>` +
            `<span class="sec-row-title">${escapeHtml(s.title)}</span>` +
            `</span>` +
            `<span class="sec-row-pages">${escapeHtml(formatPagesShort(s))}</span>` +
            `</a>`
        )
        .join("");

      cardsHtml.push(
        `<section class="part-card wide">` +
        `<div class="part-card-head">` +
        `<span class="part-badge">APPENDICI A–E</span>` +
        `<h2 class="part-card-title">Formulario, Errori comuni, Glossario, Mappa Lezioni e Argomenti mancanti</h2>` +
        `</div>` +
        `<div class="sec-list">${appRows}</div>` +
        `</section>`
      );
    }

    const quickChips = [];
    if (secById["intro"]) {
      quickChips.push(`<a class="tonal-chip" href="#intro"><span class="tonal-chip-code">Intro</span> Come usare la dispensa</a>`);
    }
    if (BOOK.parts.length && secById[BOOK.parts[0].sectionIds[0]]) {
      const firstId = BOOK.parts[0].sectionIds[0];
      quickChips.push(`<a class="tonal-chip" href="#${firstId}"><span class="tonal-chip-code">Inizia</span> ${escapeHtml(BOOK.parts[0].label)}</a>`);
    }
    const appQuick = [
      ["app-a", "App. A", "Formulario"],
      ["app-b", "App. B", "Errori Comuni"],
      ["app-c", "App. C", "Glossario"],
      ["app-d", "App. D", "File → Sezione"],
      ["app-e", "App. E", "Non coperti"],
    ];
    for (const [id, code, label] of appQuick) {
      if (secById[id]) {
        quickChips.push(`<a class="tonal-chip" href="#${id}"><span class="tonal-chip-code">${code}</span> ${label}</a>`);
      }
    }
    quickChips.push(`<a class="tonal-chip" href="../dispensa_algebra_lineare.pdf" target="_blank" rel="noopener"><span class="tonal-chip-code">PDF</span> Apri PDF A4 (${BOOK.meta.totalPages || "?"} pp.)</a>`);

    homeView.innerHTML =
      `<header class="home-header">` +
      `<p class="home-eyebrow">${escapeHtml(BOOK.meta.course)}</p>` +
      `<h1 class="home-title">${escapeHtml(BOOK.meta.title)}</h1>` +
      `<p class="home-subtitle">${escapeHtml(BOOK.meta.subtitle)}</p>` +
      `<p class="home-attrib">${BOOK.meta.attribution}</p>` +
      `</header>` +
      `<div class="home-search-box">` +
      `<div class="home-search-field">` +
      `<svg class="search-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">` +
      `<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>` +
      `</svg>` +
      `<input id="home-search-input" class="home-search-input" type="search" placeholder="Cerca subito una definizione, un teorema, un esercizio o una notazione…" autocomplete="off">` +
      `<button id="home-search-clear" class="home-search-clear" type="button" hidden>Pulisci</button>` +
      `</div>` +
      `<div id="home-inline-results" class="home-inline-results" hidden></div>` +
      `</div>` +
      `<div class="quick-strip" aria-label="Strumenti di consultazione rapida">${quickChips.join("")}</div>` +
      `<div class="part-filter-bar" role="tablist" aria-label="Filtra per capitolo">${partFilterButtons}</div>` +
      `<div class="parts-grid">${cardsHtml.join("")}</div>`;

    renderMath(homeView);

    homeView.querySelectorAll(".filter-chip").forEach((btn) => {
      btn.addEventListener("click", () => {
        activePartFilter = btn.dataset.pfilter;
        renderHome();
      });
    });

    const homeInput = document.getElementById("home-search-input");
    const homeClear = document.getElementById("home-search-clear");
    const homeResBox = document.getElementById("home-inline-results");

    const updateHomeSearch = () => {
      const q = homeInput.value;
      const trimmed = q.trim();
      homeClear.hidden = !trimmed;
      if (!trimmed) {
        homeResBox.hidden = true;
        homeResBox.innerHTML = "";
        homeResults = [];
        homeSelectedIdx = -1;
        return;
      }
      const res = runSearch(trimmed, "all");
      homeResults = res.items;
      homeSelectedIdx = homeResults.length ? 0 : -1;
      homeResBox.hidden = false;
      const metaHtml = `<div class="search-meta">${res.total} risultat${res.total === 1 ? "o" : "i"}${res.total > res.items.length ? ` (mostrati i primi ${res.items.length})` : ""} · Usa ↑ ↓ e Invio</div><div id="home-res-list" class="search-results"></div>`;
      homeResBox.innerHTML = metaHtml;
      renderResultList(document.getElementById("home-res-list"), homeResults, trimmed, homeSelectedIdx);
    };

    homeInput.addEventListener("input", updateHomeSearch);
    homeClear.addEventListener("click", () => {
      homeInput.value = "";
      updateHomeSearch();
      homeInput.focus();
    });

    homeInput.addEventListener("keydown", (e) => {
      if (!homeResults.length) return;
      if (e.key === "ArrowDown") {
        e.preventDefault();
        homeSelectedIdx = Math.min(homeResults.length - 1, homeSelectedIdx + 1);
        syncSelected(document.getElementById("home-res-list"), homeSelectedIdx);
      } else if (e.key === "ArrowUp") {
        e.preventDefault();
        homeSelectedIdx = Math.max(0, homeSelectedIdx - 1);
        syncSelected(document.getElementById("home-res-list"), homeSelectedIdx);
      } else if (e.key === "Enter" && homeSelectedIdx >= 0) {
        e.preventDefault();
        const chosen = homeResults[homeSelectedIdx];
        window.location.hash = buildResultHref(chosen.secId, chosen.bid, homeInput.value);
      } else if (e.key === "Escape") {
        homeInput.value = "";
        updateHomeSearch();
      }
    });
  }

  function syncSelected(listEl, idx) {
    if (!listEl) return;
    listEl.querySelectorAll(".search-result-item").forEach((el, i) => {
      const sel = i === idx;
      el.classList.toggle("selected", sel);
      el.setAttribute("aria-selected", String(sel));
      if (sel) el.scrollIntoView({ block: "nearest" });
    });
  }

  // ================= READER VIEW =================
  function renderReader(secId, params) {
    const sec = secById[secId];
    if (!sec) {
      renderHome();
      return;
    }

    homeView.hidden = true;
    readerView.hidden = false;

    const fullTitle = sec.kind === "section"
      ? `${sec.num} ${sec.title}`
      : (sec.kind === "appendix" ? `${sec.num} — ${sec.title}` : sec.title);
    document.title = `${fullTitle} — Algebra Lineare`;

    const part = partById[sec.partId];
    const crumbMid = part
      ? `<span>/</span><span>${escapeHtml(part.label)}: ${escapeHtml(part.title)}</span>`
      : (sec.kind === "appendix" ? `<span>/</span><span>Appendici</span>` : "");

    const partBadge = part
      ? part.label
      : (sec.kind === "appendix" ? sec.num.toUpperCase() : "INTRODUZIONE");

    const tocHtml = sec.toc && sec.toc.length
      ? `<nav id="step-jump-bar" class="step-jump-bar" aria-label="Passi della sezione">` +
        sec.toc
          .map(
            (t, idx) =>
              `<a class="step-chip${idx === 0 ? " active" : ""}" href="#${sec.id}?step=${encodeURIComponent(t.id)}" data-step="${escapeHtml(t.id)}" title="${escapeHtml(t.title)}">${escapeHtml(t.short)}</a>`
          )
          .join("") +
        `</nav>`
      : "";

    const bid = params.get("b") || "";
    const query = params.get("q") || "";
    const stepTarget = params.get("step") || "";

    const hitBanner = query
      ? `<div class="hit-banner" id="hit-banner">` +
        `<span>Risultato ricerca per: <strong>${escapeHtml(query)}</strong></span>` +
        `<button class="hit-banner-btn" id="clear-hit-btn" type="button">Rimuovi evidenziazione</button>` +
        `</div>`
      : "";

    const curIdx = secOrder.indexOf(sec.id);
    const prevSec = curIdx > 0 ? secById[secOrder[curIdx - 1]] : null;
    const nextSec = curIdx >= 0 && curIdx < secOrder.length - 1 ? secById[secOrder[curIdx + 1]] : null;

    const prevCard = prevSec
      ? `<a class="pager-card prev" href="#${prevSec.id}">` +
        `<span class="pager-dir">← Precedente</span>` +
        `<span class="pager-title">${escapeHtml(prevSec.kind === "section" ? `${prevSec.num} ${prevSec.title}` : prevSec.title)}</span>` +
        `</a>`
      : `<div></div>`;

    const nextCard = nextSec
      ? `<a class="pager-card next" href="#${nextSec.id}">` +
        `<span class="pager-dir">Successivo →</span>` +
        `<span class="pager-title">${escapeHtml(nextSec.kind === "section" ? `${nextSec.num} ${nextSec.title}` : nextSec.title)}</span>` +
        `</a>`
      : `<div></div>`;

    readerView.innerHTML =
      `<div class="reader-breadcrumb">` +
      `<a href="#home">Home</a>` +
      crumbMid +
      `<span>/</span><span>${escapeHtml(sec.num || sec.title)}</span>` +
      `</div>` +
      `<header class="reader-header">` +
      `<div class="reader-meta-row">` +
      `<span class="meta-pill">${escapeHtml(partBadge)}</span>` +
      `<span class="meta-pages">${escapeHtml(formatPagesFull(sec))}</span>` +
      `</div>` +
      `<h1 class="reader-title">${escapeHtml(fullTitle)}</h1>` +
      `</header>` +
      tocHtml +
      hitBanner +
      `<div class="book-body" id="book-body">${sec.html}</div>` +
      `<nav class="reader-pager" aria-label="Navigazione tra sezioni">${prevCard}${nextCard}</nav>`;

    const bookBody = document.getElementById("book-body");

    // Render KaTeX formulas BEFORE search highlight / scroll
    renderMath(readerView);

    // Bind step jump chips smoothly without breaking hash routing
    readerView.querySelectorAll(".step-chip").forEach((chip) => {
      chip.addEventListener("click", (e) => {
        e.preventDefault();
        const tid = chip.dataset.step;
        const targetEl = document.getElementById(tid);
        if (targetEl) {
          targetEl.scrollIntoView({ behavior: "smooth", block: "start" });
          readerView.querySelectorAll(".step-chip").forEach((c) => c.classList.toggle("active", c === chip));
        }
      });
    });

    // Highlight search hits if navigated from search
    if (query) {
      const targetBlock = bid ? bookBody.querySelector(`[data-bid="${CSS.escape(bid)}"]`) : null;
      if (targetBlock) {
        targetBlock.classList.add("hit-focus");
        highlightInElement(targetBlock, query);
        requestAnimationFrame(() => {
          targetBlock.scrollIntoView({ behavior: "smooth", block: "center" });
        });
      } else {
        highlightInElement(bookBody, query);
      }

      const clearBtn = document.getElementById("clear-hit-btn");
      if (clearBtn) {
        clearBtn.addEventListener("click", () => {
          window.location.hash = `#${sec.id}`;
        });
      }
    } else if (stepTarget) {
      const targetEl = document.getElementById(stepTarget);
      if (targetEl) {
        requestAnimationFrame(() => targetEl.scrollIntoView({ behavior: "auto", block: "start" }));
      }
    } else {
      window.scrollTo({ top: 0, behavior: "auto" });
    }

    setupStepObserver(sec);
  }

  function highlightInElement(rootEl, rawQuery) {
    const tokens = tokenizeQuery(rawQuery);
    if (!tokens.length) return;
    const accentMap = { a: "[aàá]", e: "[eèé]", i: "[iìí]", o: "[oòó]", u: "[uùú]" };
    const patterns = tokens
      .sort((a, b) => b.length - a.length)
      .map((t) =>
        escapeRegExp(t)
          .split("")
          .map((ch) => accentMap[ch] || ch)
          .join("")
      );
    const re = new RegExp(`(${patterns.join("|")})`, "gi");

    const walker = document.createTreeWalker(rootEl, NodeFilter.SHOW_TEXT, {
      acceptNode(node) {
        if (!node.nodeValue || !node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        const parent = node.parentElement;
        if (!parent || parent.closest(".katex, .katex-mathml, .katex-html, svg, button, script, style, mark")) {
          return NodeFilter.FILTER_REJECT;
        }
        return NodeFilter.FILTER_ACCEPT;
      },
    });

    const nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);

    for (const node of nodes) {
      const txt = node.nodeValue;
      re.lastIndex = 0;
      if (!re.test(txt)) continue;
      re.lastIndex = 0;
      const frag = document.createDocumentFragment();
      let last = 0;
      let m;
      while ((m = re.exec(txt)) !== null) {
        if (m.index > last) {
          frag.appendChild(document.createTextNode(txt.slice(last, m.index)));
        }
        const mark = document.createElement("mark");
        mark.className = "search-hit";
        mark.textContent = m[0];
        frag.appendChild(mark);
        last = m.index + m[0].length;
      }
      if (last < txt.length) {
        frag.appendChild(document.createTextNode(txt.slice(last)));
      }
      node.parentNode.replaceChild(frag, node);
    }
  }

  function setupStepObserver(sec) {
    if (scrollObserver) {
      scrollObserver.disconnect();
      scrollObserver = null;
    }
    if (!sec.toc || !sec.toc.length || !("IntersectionObserver" in window)) return;

    const chipsById = Object.create(null);
    readerView.querySelectorAll(".step-chip").forEach((c) => {
      chipsById[c.dataset.step] = c;
    });

    scrollObserver = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            const id = entry.target.id;
            if (chipsById[id]) {
              Object.values(chipsById).forEach((c) => c.classList.remove("active"));
              chipsById[id].classList.add("active");
              chipsById[id].scrollIntoView({ block: "nearest", inline: "nearest" });
            }
          }
        }
      },
      { rootMargin: "-110px 0px -70% 0px", threshold: 0 }
    );

    sec.toc.forEach((t) => {
      const el = document.getElementById(t.id);
      if (el) scrollObserver.observe(el);
    });
  }

  // ================= GLOBAL SEARCH MODAL =================
  function openSearchModal() {
    searchModal.hidden = false;
    modalSearchInput.focus();
    modalSearchInput.select();
    updateModalSearch();
  }

  function closeSearchModal() {
    searchModal.hidden = true;
  }

  function updateModalSearch() {
    const q = modalSearchInput.value.trim();
    if (!q) {
      const secCount = BOOK.sections.length;
      const pagesCount = BOOK.meta.totalPages || 0;
      modalSearchMeta.textContent = `Digita per cercare nella dispensa (${pagesCount} pagine, ${secCount} sezioni).`;
      modalSearchResults.innerHTML =
        '<div class="search-empty">Suggerimenti: prova <code>gruppo abeliano</code>, <code>prodotto riga per colonna</code>, <code>trasposta</code>, <code>traccia</code>, <code>numeri complessi</code> o <code>Teorema Fondamentale</code>.</div>';
      modalResults = [];
      modalSelectedIdx = -1;
      return;
    }

    const res = runSearch(q, modalScope);
    modalResults = res.items;
    modalSelectedIdx = modalResults.length ? 0 : -1;
    modalSearchMeta.textContent = `${res.total} risultat${res.total === 1 ? "o" : "i"}${res.total > res.items.length ? ` (mostrati i primi ${res.items.length})` : ""} · ↑ ↓ Invio`;
    renderResultList(modalSearchResults, modalResults, q, modalSelectedIdx, () => {
      closeSearchModal();
    });
  }

  // ================= ROUTING =================
  function parseHash() {
    const raw = (window.location.hash || "#home").slice(1);
    const qMark = raw.indexOf("?");
    if (qMark === -1) {
      return { id: raw || "home", params: new URLSearchParams() };
    }
    return {
      id: raw.slice(0, qMark) || "home",
      params: new URLSearchParams(raw.slice(qMark + 1)),
    };
  }

  function handleRoute() {
    const { id, params } = parseHash();
    const targetId = secById[id] ? id : "home";
    renderDrawer(targetId, drawerFilter.value);
    if (targetId === "home") {
      renderHome();
      window.scrollTo({ top: 0, behavior: "auto" });
    } else {
      renderReader(targetId, params);
    }
  }

  // ================= EVENT LISTENERS =================
  menuBtn.addEventListener("click", toggleDrawer);
  drawerBackdrop.addEventListener("click", closeMobileDrawer);
  drawerFilter.addEventListener("input", () => {
    const { id } = parseHash();
    renderDrawer(secById[id] ? id : "home", drawerFilter.value);
  });

  openSearchBtn.addEventListener("click", openSearchModal);
  closeSearchBtn.addEventListener("click", closeSearchModal);
  searchBackdrop.addEventListener("click", closeSearchModal);
  modalSearchInput.addEventListener("input", updateModalSearch);

  modalScopeBar.querySelectorAll(".scope-chip").forEach((chip) => {
    chip.addEventListener("click", () => {
      modalScope = chip.dataset.scope;
      modalScopeBar.querySelectorAll(".scope-chip").forEach((c) => c.classList.toggle("active", c === chip));
      updateModalSearch();
      modalSearchInput.focus();
    });
  });

  modalSearchInput.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      e.preventDefault();
      closeSearchModal();
      return;
    }
    if (!modalResults.length) return;
    if (e.key === "ArrowDown") {
      e.preventDefault();
      modalSelectedIdx = Math.min(modalResults.length - 1, modalSelectedIdx + 1);
      syncSelected(modalSearchResults, modalSelectedIdx);
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      modalSelectedIdx = Math.max(0, modalSelectedIdx - 1);
      syncSelected(modalSearchResults, modalSelectedIdx);
    } else if (e.key === "Enter" && modalSelectedIdx >= 0) {
      e.preventDefault();
      const chosen = modalResults[modalSelectedIdx];
      closeSearchModal();
      window.location.hash = buildResultHref(chosen.secId, chosen.bid, modalSearchInput.value);
    }
  });

  document.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      openSearchModal();
      return;
    }
    if (e.key === "/" && searchModal.hidden) {
      const tag = document.activeElement ? document.activeElement.tagName : "";
      if (tag !== "INPUT" && tag !== "TEXTAREA") {
        e.preventDefault();
        openSearchModal();
        return;
      }
    }
    if (e.key === "Escape") {
      if (!searchModal.hidden) {
        closeSearchModal();
      } else if (bodyEl.classList.contains("drawer-open-mobile")) {
        closeMobileDrawer();
      }
    }
  });

  window.addEventListener("scroll", () => {
    backToTopBtn.hidden = window.scrollY < 360;
  }, { passive: true });

  backToTopBtn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  window.addEventListener("hashchange", handleRoute);
  window.addEventListener("resize", () => {
    if (!isMobile()) {
      closeMobileDrawer();
    }
  });

  if (isMobile()) {
    menuBtn.setAttribute("aria-expanded", "false");
  }
  handleRoute();
})();
