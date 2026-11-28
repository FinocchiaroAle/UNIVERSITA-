<!-- section: intro | num: Intro | title: Introduzione al corso e guida alla dispensa | kind: intro | part: intro -->

Benvenuto. Questa dispensa è stata scritta per permetterti di studiare e preparare da solo l'esame di **Algebra Lineare e Geometria** (Corso di Laurea in Informatica, canale F–N, A.A. 2026), partendo da zero e arrivando fino agli esercizi d'esame completi.

Tutte le definizioni, gli enunciati, l'ordine degli argomenti, le notazioni e gli esercizi provengono **direttamente dai 15 PDF delle lezioni** del **Prof. Giuseppe Zappalà** (`Lez00`–`Lez14`).

### 1. Informazioni sul corso e modalità d'esame (Lezione 0, pp. 1–2)

| Voce | Dettaglio ufficiale (`Lez00`) |
| :--- | :--- |
| **Docente** | Prof. Giuseppe Zappalà |
| **Email** | `giuseppe.zappala@unict.it` |
| **Pagina Web** | `www.dmi.unict.it/zappalag` |
| **Canale Teams** | Codice `j0veyzu` |
| **Ricevimento** | Su appuntamento tramite email |
| **Prova scritta** | Durata **1 ora e mezza**, **4 esercizi** (2 di Algebra Lineare e 2 di Geometria); ammissione all'orale con punteggio minimo **12/30**; risultati sulla pagina web del docente |
| **Prova orale** | Circa una settimana dopo la prova scritta |
| **Prove in itinere** | Non previste |

:::tip Raccomandazioni del docente (Lezione 0, p. 2)
1. **Seguire tutte le lezioni** (qui hai ogni singolo passaggio ricostruito in ordine).
2. **Studiare volta per volta**, senza accumulare gli argomenti prima dell'appello.
3. **Sostenere l'esame nella I sessione**, quando i concetti e le tecniche di calcolo sono ancora freschi.
:::

#### Programma ufficiale del corso (`Lez00`, p. 1)

Il programma indicato nella presentazione introduttiva è diviso in due blocchi:

- **Algebra Lineare** *(coperto al 100% in questa dispensa, nell'ordine effettivo delle lezioni `Lez01`–`Lez14`)*:

    1. Strutture algebriche
    2. Matrici
    3. Determinanti
    4. Spazi vettoriali
    5. Sistemi lineari
    6. Applicazioni lineari
    7. Diagonalizzazione degli endomorfismi

- **Geometria** *(non presente nei 15 PDF forniti; vedi riepilogo trasparente nell'Appendice E)*:

    1. Geometria lineare sul piano
    2. Geometria lineare nello spazio
    3. Coniche

:::note Nota sull'ordine tra programma e lezioni
Nel programma sintetico di `Lez00` p. 1 *Spazi vettoriali* compare al punto 4 prima di *Sistemi lineari* (punto 5). Nel corso effettivo delle lezioni il docente affronta invece prima i **sistemi lineari e il rango** (`Lez05`–`Lez07`) e subito dopo gli **spazi vettoriali** (`Lez07`–`Lez09`). Questa dispensa segue fedelmente l'ordine reale delle lezioni.
:::

### 2. Come è organizzato ogni argomento (i 7 passi fissi)

Ogni sottoparagrafo di studio segue sempre la stessa scaletta in **7 passi**, così sai subito dove cercare ciò che ti serve:

1. **Idea in parole semplici**: il concetto spiegato con parole quotidiane e, quando aiuta, un'analogia concreta.
2. **Definizioni e enunciati precisi**: tutte le definizioni, proposizioni, teoremi e notazioni ufficiali con il riferimento preciso *(Lezione X, p. Y)*. Eventuali brevissimi chiarimenti esterni indispensabili per la leggibilità sono sempre marcati `[INTEGRAZIONE NON DALLE LEZIONI]`.
3. **Dimostrazioni**: solo quelle svolte a lezione, introdotte dall'idea chiave prima dei calcoli.
4. **Esempi svolti**: tutti gli esempi risolti in aula dal docente, spiegati passo dopo passo.
5. **Errori comuni e trappole**: gli sbagli tipici all'esame, sempre nel formato *Sbagliato → Correzione*.
6. **Riepilogo**: al massimo 5 punti chiave per il ripasso rapido.
7. **Esercizi**: esclusivamente gli esercizi originali presenti nei PDF del professore (inclusi tutti gli *Esercizi per casa* e i completamenti richiesti a lezione), con la soluzione completa spiegata.

:::note Gestione trasparente di refusi e lacune degli appunti
Quando nei PDF manoscritti compare un refuso di calcolo, un simbolo mancante nell'esportazione grafica (come accade in `Lez04`, pp. 2–3) o una piccola difformità notazionale (come in `Lez11`, p. 9), il testo corretto viene accompagnato da un box **Nota sugli appunti originali** che segnala esattamente cosa c'è sul PDF originale e come leggerlo senza dubbi.
:::

### 3. Tabella delle notazioni del Prof. Zappalà

È molto importante usare **esattamente le notazioni del docente** all'esame scritto e orale: molti libri usano simboli diversi, ma qui manteniamo sempre quelli delle lezioni.

| Concetto | Notazione del corso (usata qui) | Notazioni alternative comuni (da non confondere) |
| :--- | :--- | :--- |
| Spazio delle matrici $m \times n$ su $K$ | $K^{m,n}$, $\mathbb{R}^{m,n}$ | $M_{m,n}(K)$, $\mathcal{M}_{m\times n}(K)$ |
| Elemento di posto $(i,j)$ della matrice $A$ | $\operatorname{ent}_{ij}(A)$ (o $m_{ij}, a_{ij}$) | $[A]_{ij}$, $A_{ij}$ |
| Matrice trasposta di $A$ | ${}^t A$ | $A^T$, $A^\top$ |
| Matrice dei cofattori e matrice aggiunta | $A_{\text{COF}}$, $A_{\text{AGG}} = {}^t A_{\text{COF}}$ | $\operatorname{cof}(A)$, $\operatorname{adj}(A)$ |
| Traccia e rango di una matrice | $\operatorname{tr} A$, $\operatorname{rk} A$ | $\operatorname{Tr}(A)$, $\operatorname{rg}(A)$ |
| Vettore nullo (in uno spazio $U$ o $V$) | $\underline{0}$, $\underline{0}_U$, $\underline{0}_V$ | $\mathbf{0}$, $0_V$ |
| Sottospazio generato da $S$ | $\mathcal{L}(S)$, $\mathcal{L}(v_1, \dots, v_r)$ | $\operatorname{Span}(S)$, $\langle v_1, \dots, v_r \rangle$ |
| Spazio delle righe e delle colonne | $\mathcal{L}_R(A)$, $\mathcal{L}_C(A)$ | $\operatorname{Row}(A)$, $\operatorname{Col}(A)$ |
| Applicazione lineare associata a $M$ | $f_M(X) = MX$, matrice $M(f)$ | $L_A$, $[f]$ |
| Nucleo e immagine | $\operatorname{Ker} f$, $\operatorname{Im} f$ | $N(f)$, $\mathcal{R}(f)$ |
| Dimensione su campo $K$ | $\dim_K V$, $\dim_{\mathbb{R}} U$ | $\dim(V)$ |
| Polinomio caratteristico di $A$ | $P_A(x) = \det(A - xI)$ | $\det(xI - A)$, $p_A(\lambda)$ |
| Molteplicità algebrica e geometrica | $m_\lambda$, $g_\lambda$ | $\mu_a(\lambda)$, $\mu_g(\lambda)$ |
| Autospazio relativo all'autovalore $\lambda$ | $V_\lambda = \operatorname{Ker}(f_A - \lambda \operatorname{id})$ | $E_\lambda$ |
