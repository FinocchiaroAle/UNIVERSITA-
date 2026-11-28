<!-- part: cap-4 | num: 4 | label: CAPITOLO 4 | title: Sistemi lineari e rango | refs: Fonti: Lezione 5 (19/10/2026, pp. 7–11), Lezione 6 (21/10/2026, pp. 1–5), Lezione 7 (26/10/2026, pp. 1–5) -->

<!-- section: sec-4-1 | num: 4.1 | title: Sistemi lineari in forma matriciale, Teorema e Regola di Cramer | kind: section | part: cap-4 -->

### 1. Idea in parole semplici

Un **sistema lineare** è un insieme di $m$ equazioni di primo grado in $n$ incognite (nessun quadrato come $x^2$, nessun prodotto come $xy$). Usando il prodotto riga per colonna tra matrici visto nel Capitolo 2, possiamo compattare l'intero sistema in una sola equazione matriciale elegante: **$AX = B$**, dove $A$ contiene i coefficienti, $X$ le incognite in colonna e $B$ i termini noti in colonna.

Il caso più fortunato e semplice è quello dei **sistemi di Cramer**: tante equazioni quante incognite ($A$ quadrata) e $\det A \neq 0$. Siccome $\det A \neq 0$ significa esattamente che $A$ è invertibile, per trovare la soluzione basterà moltiplicare per $A^{-1}$ ($X = A^{-1}B$), oppure usare la rapidissima **Regola di Cramer**, che calcola ogni singola incognita come rapporto tra due determinanti.

### 2. Definizioni e enunciati precisi

:::def Definizione — Sistema lineare e forma matriciale $AX = B$ (Lezione 5, pp. 7–8)
Sia $(K, +, \cdot)$ un campo. Si chiama **sistema lineare** un sistema di $m$ equazioni in $n$ incognite della forma:

$$\begin{cases} a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n = b_1 \\ a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n = b_2 \\ \vdots \\ a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n = b_m \end{cases} \qquad (a_{ij} \in K,\ b_j \in K)$$

dove $x_1, \dots, x_n$ sono le **incognite**, gli $a_{ij}$ sono i **coefficienti** e $b_1, \dots, b_m$ sono i **termini noti**. Ponendo:

$$A = (a_{ij}) \in K^{m,n} \text{ (matrice dei coefficienti)}, \qquad B = \begin{pmatrix} b_1 \\ \vdots \\ b_m \end{pmatrix} \in K^{m,1} \text{ (colonna dei termini noti)}, \qquad X = \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} \text{ (colonna delle incognite)}$$

il sistema si scrive in **forma matriciale** come:

$$AX = B$$

- Si chiama **soluzione** del sistema un elemento $\bar{X} \in K^{n,1}$ tale che $A\bar{X} = B$.
- **Risolvere** un sistema lineare significa determinare l'insieme di **tutte** le sue soluzioni.
- Un sistema si dice **risolubile** se esiste almeno una soluzione; altrimenti si dice **impossibile**.
:::

:::def Definizione — Sistema di Cramer (Lezione 5, p. 8)
Un sistema lineare $AX = B$ si dice **sistema di Cramer** se soddisfa entrambe le condizioni:
1. $A$ è una **matrice quadrata** ($A \in K^{n,n}$);
2. $\det A \neq 0$.
:::

:::thm Teorema di Cramer (Lezione 5, p. 8)
Un sistema di Cramer $AX = B$ ha **una ed una sola soluzione**, data da $X = A^{-1}B$.
:::

:::thm Regola di Cramer (Lezione 5, p. 10)
Sia $AX = B$ un sistema di Cramer e scriviamo $A = (C_1\ \dots\ C_n)$ per colonne. Indichiamo con $A_{(i)}$ la matrice ottenuta sostituendo la colonna $i$-esima di $A$ con la colonna $B$ dei termini noti:

$$A_{(i)} \stackrel{\text{DEF}}{=} (C_1\ \dots\ C_{i-1}\ B\ C_{i+1}\ \dots\ C_n)$$

Allora l'unica soluzione $\bar{X} = \begin{pmatrix} \bar{x}_1 \\ \vdots \\ \bar{x}_n \end{pmatrix}$ del sistema di Cramer ha componenti:

$$\bar{x}_i = \frac{\det A_{(i)}}{\det A} \qquad \forall i \in \{1, \dots, n\}$$
:::

### 3. Dimostrazioni

:::proof Dimostrazione — Teorema di Cramer (Lezione 5, p. 8)
**Idea di fondo:** dividiamo la prova in due passi: prima dimostriamo l'*unicità* (se una soluzione esiste, deve per forza coincidere con $A^{-1}B$ moltiplicando a sinistra per $A^{-1}$), poi dimostriamo l'*esistenza* (verifichiamo che $A^{-1}B$ soddisfa davvero $AX = B$).

Sia $AX = B$ un sistema di Cramer: dunque $A \in K^{n,n}$ e $\det A \neq 0$, quindi per il Teorema della sezione [3.4](#sec-3-4) $A$ è invertibile ed esiste $A^{-1} \in K^{n,n}$.

1. **Unicità:** se $X$ è una qualsiasi soluzione di $AX = B$, moltiplicando entrambi i membri a sinistra per $A^{-1}$ otteniamo:
    $$AX = B \implies A^{-1}(AX) = A^{-1}B \implies (A^{-1}A)X = A^{-1}B \implies IX = A^{-1}B \implies X = A^{-1}B$$
2. **Esistenza:** verifichiamo che il vettore colonna $\bar{X} = A^{-1}B$ è effettivamente soluzione del sistema:
    $$A\bar{X} = A(A^{-1}B) = (AA^{-1})B = IB = B$$

Pertanto la soluzione esiste ed è unica: $X = A^{-1}B$.
:::

### 4. Esempi svolti

:::example Esempio 4.1.1 — Un sistema impossibile (Lezione 5, p. 8)
Consideriamo:

$$\begin{cases} x_1 + x_2 = 1 \\ x_1 + x_2 = 2 \end{cases}, \qquad A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix},\quad B = \begin{pmatrix} 1 \\ 2 \end{pmatrix},\quad X = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$$

La stessa somma $x_1 + x_2$ non può valere contemporaneamente $1$ e $2$: questo sistema non ha soluzioni (è **impossibile**). Nota che infatti $\det A = 1 - 1 = 0$, quindi non è un sistema di Cramer.
:::

:::example Esempio 4.1.2 — Risoluzione tramite $A^{-1}$ di un sistema $2\times 2$ (Lezione 5, p. 9)
Risolvere:

$$\begin{cases} 2x + 3y = 1 \\ 5x + 8y = 2 \end{cases}$$

Abbiamo $A = \begin{pmatrix} 2 & 3 \\ 5 & 8 \end{pmatrix} \in \mathbb{R}^{2,2}$, con $\det A = 16 - 15 = 1 \neq 0$ (sistema di Cramer). Calcoliamo l'aggiunta e l'inversa:

$$A_{\text{AGG}} = {}^t\begin{pmatrix} 8 & -5 \\ -3 & 2 \end{pmatrix} = \begin{pmatrix} 8 & -3 \\ -5 & 2 \end{pmatrix} \implies A^{-1} = \begin{pmatrix} 8 & -3 \\ -5 & 2 \end{pmatrix}$$

Moltiplicando a sinistra entrambi i membri per $A^{-1}$:

$$\begin{pmatrix} 8 & -3 \\ -5 & 2 \end{pmatrix}\begin{pmatrix} 2 & 3 \\ 5 & 8 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 8 & -3 \\ -5 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ 2 \end{pmatrix} \implies \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 2 \\ -1 \end{pmatrix} \implies \bar{X} = \begin{pmatrix} 2 \\ -1 \end{pmatrix}$$
:::

:::example Esempio 4.1.3 — Sistema parametrico $2\times 2$ con $A^{-1}$ e con la Regola di Cramer (Lezione 5, pp. 9–11)
Risolvere al variare di $h \in \mathbb{R}$:

$$\begin{cases} hx + y = 1 \\ x + y = 2 \end{cases}$$

Qui $A = \begin{pmatrix} h & 1 \\ 1 & 1 \end{pmatrix}$ e $\det A = h - 1$. Quindi $\det A = 0 \iff h = 1$.

- **Per $h = 1$:** il sistema diventa $\begin{cases} x+y=1 \\ x+y=2 \end{cases}$, evidentemente impossibile (non risolubile).
- **Per $h \neq 1$ (sistema di Cramer):** esiste un'unica soluzione.
    - *Metodo 1 (via $A_{\text{AGG}}$ e $A^{-1}$, pp. 9–10):* $A_{\text{AGG}} = \begin{pmatrix} 1 & -1 \\ -1 & h \end{pmatrix}$; moltiplicando $AX=B$ a sinistra per $A_{\text{AGG}}$:
        $$\begin{pmatrix} h-1 & 0 \\ 0 & h-1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ -1 & h \end{pmatrix}\begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} -1 \\ 2h-1 \end{pmatrix} \implies \begin{cases} x = \frac{-1}{h-1} = \frac{1}{1-h} \\ y = \frac{2h-1}{h-1} \end{cases}$$
    - *Metodo 2 (Regola di Cramer, p. 11):* costruiamo $A_{(1)} = \begin{pmatrix} 1 & 1 \\ 2 & 1 \end{pmatrix}$ e $A_{(2)} = \begin{pmatrix} h & 1 \\ 1 & 2 \end{pmatrix}$, da cui $\det A_{(1)} = -1$ e $\det A_{(2)} = 2h - 1$, ritrovando subito:
        $$\bar{X} = \begin{pmatrix} \frac{-1}{h-1} \\ \frac{2h-1}{h-1} \end{pmatrix}$$
:::

### 5. Errori comuni e trappole

1. **Moltiplicare $B$ per $A^{-1}$ nell'ordine sbagliato: $X = B A^{-1}$**
    - *Sbagliato:* scrivere la formula risolutiva come $X = BA^{-1}$.
    - *Correzione:* siccome $B \in K^{n,1}$ è una matrice con $1$ colonna e $A^{-1} \in K^{n,n}$, il prodotto $B A^{-1}$ **non esiste neppure** (per $n > 1$)! Per cancellare $A$ a sinistra di $X$ devi moltiplicare a **sinistra**: $X = A^{-1}B$.
2. **Sostituire la riga $i$-esima al posto della colonna $i$-esima nella Regola di Cramer**
    - *Sbagliato:* in $A_{(i)}$ rimpiazzare la riga $i$ con $B$.
    - *Correzione:* nella Regola di Cramer *(Lezione 5, p. 10)* $A_{(i)}$ sostituisce la **colonna $i$-esima** $C_i$ con la colonna dei termini noti $B$.
3. **Concludere subito "impossibile" quando $\det A = 0$**
    - *Sbagliato:* dire che se $\det A = 0$ il sistema non ha soluzioni.
    - *Correzione:* quando $\det A = 0$ il sistema **non è di Cramer**, ma può essere tanto *impossibile* (come per $h=1$ nell'Esempio 4.1.3) quanto avere *infinite soluzioni* (come vedremo con Rouché-Capelli in [4.3](#sec-4-3)).

### 6. Riepilogo

- Ogni sistema lineare si compatta in forma matriciale come $AX = B$, con $A \in K^{m,n}$, $B \in K^{m,1}$, $X \in K^{n,1}$.
- Un sistema è **di Cramer** se $A$ è quadrata e $\det A \neq 0$.
- **Teorema di Cramer:** un sistema di Cramer ammette una ed una sola soluzione, $\bar{X} = A^{-1}B$.
- **Regola di Cramer:** l'$i$-esima componente dell'unica soluzione è $\bar{x}_i = \frac{\det A_{(i)}}{\det A}$, dove $A_{(i)}$ rimpiazza la colonna $i$ di $A$ con $B$.

### 7. Esercizi

:::exercise Esercizio 4.1.1 (Esercizio per casa — Medio · Lezione 5, p. 10)
Risolvere il sistema lineare, quando è un sistema di Cramer ($h \in \mathbb{R}$):

$$\begin{cases} hx + y + z = 3 \\ 2x + 3y + z = 2 \\ 4x + 2y + z = 2 \end{cases}$$

:::solution Soluzione spiegata passo-passo
**Ragionamento:** determiniamo prima per quali valori di $h \in \mathbb{R}$ vale $\det A \neq 0$ (condizione di Cramer), quindi applichiamo la Regola di Cramer calcolando $\det A_{(1)}$, $\det A_{(2)}$ e $\det A_{(3)}$.

1. **Matrice dei coefficienti $A$ e condizione di Cramer:**
    $$A = \begin{pmatrix} h & 1 & 1 \\ 2 & 3 & 1 \\ 4 & 2 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 3 \\ 2 \\ 2 \end{pmatrix}$$
    Calcoliamo $\det A$ sviluppando con Laplace lungo la prima riga:
    $$\det A = h(3 - 2) - 1(2 - 4) + 1(4 - 12) = h + 2 - 8 = h - 6$$
    Dunque $\det A \neq 0 \iff h \neq 6$: il sistema è **di Cramer per ogni $h \in \mathbb{R} \setminus \{6\}$**. *(Nota: per $h = 6$, la somma tra la prima e la seconda equazione sarebbe incompatibile o da studiare con il rango, ma qui il testo chiede esplicitamente il caso di Cramer $h \neq 6$).*

2. **Calcolo delle incognite con la Regola di Cramer ($h \neq 6$):**
    - Sostituiamo la colonna $1$ con $B$:
        $$A_{(1)} = \begin{pmatrix} 3 & 1 & 1 \\ 2 & 3 & 1 \\ 2 & 2 & 1 \end{pmatrix} \implies \det A_{(1)} = 3(3-2) - 1(2-2) + 1(4-6) = 3 - 0 - 2 = 1$$
        Quindi $\bar{x} = \frac{1}{h - 6}$.
    - Sostituiamo la colonna $2$ con $B$:
        $$A_{(2)} = \begin{pmatrix} h & 3 & 1 \\ 2 & 2 & 1 \\ 4 & 2 & 1 \end{pmatrix} \implies \det A_{(2)} = h(2-2) - 3(2-4) + 1(4-8) = 0 + 6 - 4 = 2$$
        Quindi $\bar{y} = \frac{2}{h - 6}$.
    - Sostituiamo la colonna $3$ con $B$:
        $$A_{(3)} = \begin{pmatrix} h & 1 & 3 \\ 2 & 3 & 2 \\ 4 & 2 & 2 \end{pmatrix} \implies \det A_{(3)} = h(6-4) - 1(4-8) + 3(4-12) = 2h + 4 - 24 = 2h - 20$$
        Quindi $\bar{z} = \frac{2h - 20}{h - 6}$.

3. **Verifica diretta per sostituzione nelle tre equazioni:**
    - Eq. 1: $\frac{h + 2 + 2h - 20}{h - 6} = \frac{3h - 18}{h - 6} = 3$.
    - Eq. 2: $\frac{2 + 6 + 2h - 20}{h - 6} = \frac{2h - 12}{h - 6} = 2$.
    - Eq. 3: $\frac{4 + 4 + 2h - 20}{h - 6} = \frac{2h - 12}{h - 6} = 2$.

Pertanto per $h \neq 6$ l'unica soluzione è $\bar{X} = \begin{pmatrix} \frac{1}{h-6} \\ \frac{2}{h-6} \\ \frac{2h-20}{h-6} \end{pmatrix}$.
:::
:::

<!-- section: sec-4-2 | num: 4.2 | title: Sottomatrici, minori, rango, matrici ridotte per righe e metodo di riduzione | kind: section | part: cap-4 -->

### 1. Idea in parole semplici

Cosa facciamo se una matrice $A$ **non è quadrata** (perché un sistema ha più equazioni che incognite o viceversa), oppure è quadrata ma ha **determinante nullo**? Serve una misura della "quantità reale di informazione indipendente" contenuta nella matrice: è il **rango** ($\operatorname{rk} A$).

Dire che $\operatorname{rk} A = r$ significa che la sotto-tabella quadrata più grande con determinante $\neq 0$ che riesci a ritagliare dentro $A$ ha taglia $r \times r$. Siccome calcolare tutti i possibili minori di una matrice grande sarebbe interminabile, il **metodo di riduzione** trasforma passo dopo passo $A$ combinando le righe fino a ottenere una **matrice ridotta per righe**, dove ogni riga non nulla ha un numero speciale (pivot) con soli zeri al di sotto: in quel formato il rango si legge a occhio nudo contando semplicemente le righe non nulle!

### 2. Definizioni e enunciati precisi

:::def Definizione — Sottomatrice, minore di ordine $r$ e rango di una matrice (Lezione 6, p. 1)
Sia $A \in K^{m,n}$.
- Scelti due sottoinsiemi di indici $I \subseteq \{1,\dots,m\}$ e $J \subseteq \{1,\dots,n\}$, la matrice:
    $$A_{I,J} \stackrel{\text{DEF}}{=} \{a_{ij} \mid i \in I \text{ e } j \in J\}$$
    si chiama **sottomatrice** di $A$ individuata da $I$ e $J$ *(cioè mantenendo solo le righe in $I$ e le colonne in $J$)*.
- Si chiama **minore di ordine $r$** di $A$ il determinante di una sottomatrice quadrata di $A$ di ordine $r$.
- Si chiama **rango** di $A$ *(denotato con $\operatorname{rk} A$)* l'**ordine massimo di un minore non nullo** di $A$ *(con la convenzione naturale $\operatorname{rk} O = 0$ per la matrice nulla)*.
:::

:::def Definizione — Matrice ridotta per righe ed elementi speciali (Lezione 6, p. 2)
Sia $A \in K^{m,n}$. Diremo che $A$ è **ridotta per righe** se in **ogni riga non nulla** di $A$ esiste un elemento non nullo (detto **elemento speciale**) al di sotto del quale vi sono **tutti zeri**.
:::

:::thm Proposizioni — Determinante delle triangolari, rango delle ridotte e metodo di riduzione (Lezione 6, pp. 2–4)
1. **Determinante di matrice triangolare (p. 2):** nelle matrici triangolari (superiori o inferiori) il determinante è uguale al **prodotto degli elementi sulla diagonale principale**.
2. **Rango di matrice ridotta per righe (p. 3):** il rango di una matrice ridotta per righe è uguale al **numero di righe non nulle**.
3. **Metodo di riduzione (p. 4):** ogni matrice $A \in K^{m,n}$ si può trasformare in una matrice ridotta per righe **senza alterare il rango**, mediante operazioni elementari sulle righe del tipo $R_i \mapsto R_i + aR_j$ ($a \in K$, $j \neq i$).
:::

:::note Nota sugli appunti originali (`Lez06`, pp. 1–4; `Lez07`, p. 1; `Lez10`, p. 1)
1. **Caso della matrice nulla:** `Lez06` p. 1 definisce $\operatorname{rk} A$ senza esplicitare a parte $\operatorname{rk} O = 0$ (dove non esistono minori non nulli).
2. **Riga nulla sopra righe non nulle:** la definizione di *matrice ridotta per righe* di `Lez06` p. 2 (diversamente dalla "forma a gradini canonica" di certi manuali) consente righe nulle in mezzo e permette di scegliere l'elemento speciale in qualsiasi colonna della riga, purché sotto di esso compaiano solo zeri.
3. **Altre operazioni elementari usate nel corso:** a `Lez06` p. 3 il docente enuncia soltanto $R_i \mapsto R_i + a R_j$, motivandone la validità dal fatto che "non altera il determinante". Si tenga presente *(a)* che per matrici rettangolari l'invarianza riguarda l'annullarsi simultaneo di tutti i minori di un dato ordine (quindi il rango), e *(b)* che nei lucidi successivi il prof usa legittimamente anche **riscalamenti** $R_i \mapsto c R_i$ con $c \neq 0$ (es. `Lez07` p. 1 e p. 4) e **scambi di righe** (es. `Lez10` p. 1) `[INTEGRAZIONE NON DALLE LEZIONI]`, poiché anch'essi conservano sempre il rango.
4. **Refuso aritmetico a `Lez06` p. 3 (riquadro verde):** nel calcolo dell'entrata $(4,4)$ scrive $7\cdot\frac{7}{6} - 11 = \frac{49 - 6}{6} = -\frac{17}{6}$; il numeratore esatto è $49 - 66 = -17$, quindi il risultato finale $-\frac{17}{6}$ riportato negli appunti è corretto.
:::

### 3. Dimostrazioni

Nella Lezione 6 *(pp. 2–3)* viene mostrata la giustificazione sul perché una matrice ridotta per righe ha rango uguale al numero $k$ delle sue righe non nulle: selezionando l'insieme $I$ delle $k$ righe non nulle e l'insieme $J$ delle colonne contenenti i $k$ elementi speciali (riordinabili in forma triangolare superiore con eventuali scambi di colonne, che al più cambiano segno al determinante), il minore risultante è $\pm$ il prodotto dei $k$ elementi speciali $\neq 0$, quindi $\operatorname{rk} A \ge k$; d'altra parte ogni sottomatrice di ordine $> k$ contiene almeno una riga interamente nulla e quindi ha determinante $0$, da cui $\operatorname{rk} A = k$.

### 4. Esempi svolti

:::example Esempio 4.2.1 — Sottomatrice, minore di ordine 2 e calcolo diretto di ranghi (Lezione 6, pp. 1–2)
1. **Sottomatrice:** data $A = \begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} & a_{15} \\ a_{21} & a_{22} & a_{23} & a_{24} & a_{25} \\ a_{31} & a_{32} & a_{33} & a_{34} & a_{35} \end{pmatrix} \in K^{3,5}$, scegliendo $I = \{1,3\}$ e $J = \{2,3,5\}$ si ottiene:
    $$A_{I,J} = \begin{pmatrix} a_{12} & a_{13} & a_{15} \\ a_{32} & a_{33} & a_{35} \end{pmatrix} \in K^{2,3}$$
2. **Minore di ordine $2$:** in $A = \begin{pmatrix} 1 & 2 & 3 & 2 & 5 \\ 4 & 1 & 1 & 2 & 8 \\ 6 & 3 & 2 & 4 & 1 \end{pmatrix} \in \mathbb{R}^{3,5}$, con $I = \{1,2\}$ e $J = \{4,5\}$ si ha $A_{\{1,2\},\{4,5\}} = \begin{pmatrix} 2 & 5 \\ 2 & 8 \end{pmatrix}$ e $\det\begin{pmatrix} 2 & 5 \\ 2 & 8 \end{pmatrix} = 16 - 10 = 6$: quindi $6$ è un minore di ordine $2$ di $A$.
3. **Tre calcoli di rango diretti (pp. 1–2):**
    - $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix} \in \mathbb{R}^{2,3}$: $\det\begin{pmatrix} 1 & 2 \\ 4 & 5 \end{pmatrix} = 5 - 8 = -3 \neq 0 \implies \operatorname{rk} A \ge 2$, e non esistono minori di ordine $3$, quindi **$\operatorname{rk} A = 2$**.
    - $A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{pmatrix} \in \mathbb{R}^{2,3}$: siccome $R_2 = 2R_1$, tutti i minori di ordine $2$ hanno una riga multipla dell'altra e sono nulli; essendoci l'elemento $1 \neq 0$, **$\operatorname{rk} A = 1$**.
    - $A = \begin{pmatrix} 1 & 3 & 2 & 5 & 1 \\ 4 & 1 & 1 & 1 & 3 \\ 5 & 4 & 3 & 6 & 4 \end{pmatrix}$: siccome $R_3 = R_1 + R_2$, tutti i minori di ordine $3$ sono nulli ($\operatorname{rk} A \le 2$), mentre $\det\begin{pmatrix} 1 & 3 \\ 4 & 1 \end{pmatrix} = 1 - 12 = -11 \neq 0$, quindi **$\operatorname{rk} A = 2$**.
:::

:::example Esempio 4.2.2 — Matrice ridotta per righe ed elementi speciali (Lezione 6, pp. 2–3)
Sia:

$$A = \begin{pmatrix} 1 & 2 & \boxed{5} & 3 & 4 & 8 & 4 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 4 & 5 & 0 & 3 & \boxed{8} & 9 & 3 \\ 9 & 0 & 0 & 2 & 0 & 3 & \boxed{4} \\ \boxed{1} & 5 & 0 & 5 & 0 & 2 & 0 \end{pmatrix} \in \mathbb{R}^{5,7}$$

Gli elementi riquadrati ($5, 8, 4, 1$) hanno tutti zeri sotto di sé nella propria colonna, quindi $A$ è **ridotta per righe**. Considerando righe $I = \{1,3,4,5\}$ e colonne $J = \{1,3,5,7\}$ degli elementi speciali:

$$A_{I,J} = \begin{pmatrix} 1 & 5 & 4 & 4 \\ 4 & 0 & 8 & 3 \\ 9 & 0 & 0 & 4 \\ 1 & 0 & 0 & 0 \end{pmatrix} \implies \det A_{I,J} = \pm\det\begin{pmatrix} 5 & 4 & 4 & 1 \\ 0 & 8 & 3 & 4 \\ 0 & 0 & 4 & 9 \\ 0 & 0 & 0 & 1 \end{pmatrix} = \pm 5\cdot 8\cdot 4\cdot 1 \neq 0$$

Poiché esiste un minore di ordine $4$ non nullo e la riga $2$ è nulla, **$\operatorname{rk} A = 4$** (uguale al numero delle righe non nulle).
:::

:::example Esempio 4.2.3 — Riduzione completa di una matrice $4\times 5$ (Lezione 6, p. 3)
Calcoliamo il rango di $A = \begin{pmatrix} 3 & 5 & \boxed{1} & 2 & 0 \\ 2 & 1 & 1 & 3 & 1 \\ 1 & 3 & -1 & 1 & 2 \\ -2 & 1 & 2 & 1 & 1 \end{pmatrix} \in \mathbb{R}^{4,5}$. Scegliamo come primo elemento speciale $1$ in posizione $(1,3)$ per azzerare tutta la colonna $3$:

1. $R_2 \mapsto R_2 - R_1$, $R_3 \mapsto R_3 + R_1$, $R_4 \mapsto R_4 - 2R_1$:
    $$\longrightarrow \begin{pmatrix} 3 & 5 & \boxed{1} & 2 & 0 \\ \boxed{-1} & -4 & 0 & 1 & 1 \\ 4 & 8 & 0 & 3 & 2 \\ -8 & -9 & 0 & -3 & 1 \end{pmatrix}$$
2. Scegliamo $-1$ in $(2,1)$ come elemento speciale e annulliamo i termini sottostanti nella colonna $1$ con $R_3 \mapsto R_3 + 4R_2$ e $R_4 \mapsto R_4 - 8R_2$:
    $$\longrightarrow \begin{pmatrix} 3 & 5 & \boxed{1} & 2 & 0 \\ \boxed{-1} & -4 & 0 & 1 & 1 \\ 0 & -8 & 0 & 7 & \boxed{6} \\ 0 & 23 & 0 & -11 & -7 \end{pmatrix}$$
3. Scegliamo $6$ in $(3,5)$ come terzo elemento speciale e annulliamo $-7$ sottostante tramite $R_4 \mapsto R_4 + \frac{7}{6}R_3$:
    - colonna $2$: $-8\cdot\frac{7}{6} + 23 = \frac{-56 + 138}{6} = \frac{82}{6}$;
    - colonna $4$: $7\cdot\frac{7}{6} - 11 = \frac{49 - 66}{6} = -\frac{17}{6}$;
    - colonna $5$: $6\cdot\frac{7}{6} - 7 = 0$.
    $$\longrightarrow \begin{pmatrix} 3 & 5 & \boxed{1} & 2 & 0 \\ \boxed{-1} & -4 & 0 & 1 & 1 \\ 0 & -8 & 0 & 7 & \boxed{6} \\ 0 & \boxed{\frac{82}{6}} & 0 & -\frac{17}{6} & 0 \end{pmatrix} \implies \operatorname{rk} A = 4$$
    *(La riga $4$ ha pivot $\frac{82}{6} \neq 0$ senza altri elementi sotto di sé: tutte e $4$ le righe sono non nulle, quindi $\operatorname{rk} A = 4$.)*
:::

### 5. Errori comuni e trappole

1. **Modificare due righe usandole reciprocamente nello stesso passo**
    - *Sbagliato:* eseguire simultaneamente $R_1 \mapsto R_1 + R_2$ e $R_2 \mapsto R_2 - R_1$ usando le *vecchie* righe in entrambe.
    - *Correzione:* `[INTEGRAZIONE NON DALLE LEZIONI]` usa sempre una **sola riga pivot fissa** (che resta intatta in quel passo) per azzerare tutte le altre righe, oppure applica le sostituzioni sequenzialmente una alla volta, così non rischi di rendere dipendenti due righe e abbassare artificialmente il rango!
2. **Scegliere un elemento speciale diverso da una colonna in cui compaiono valori non nulli sotto di esso**
    - *Sbagliato:* contare una riga non nulla credendo che sia ridotta quando sotto il suo pivot scelto c'è ancora un numero diverso da $0$.
    - *Correzione:* nella riga non nulla devi poter indicare **un** elemento non nullo nella cui colonna, **sotto** quella riga, ci siano esclusivamente zeri *(Lezione 6, p. 2)*.

### 6. Riepilogo

- Un **minore di ordine $r$** è il determinante di una sottomatrice quadrata $r \times r$; il **rango** $\operatorname{rk} A$ è l'ordine massimo di un minore non nullo (con $\operatorname{rk} O = 0$).
- Una matrice è **ridotta per righe** se ogni riga non nulla possiede un elemento non nullo (speciale) al di sotto del quale ci sono solo zeri.
- Il rango di una matrice ridotta per righe è il **numero delle sue righe non nulle**.
- Il **metodo di riduzione** trasforma qualsiasi $A \in K^{m,n}$ in una matrice ridotta per righe senza alterarne il rango.
- Il determinante di una matrice triangolare è il prodotto degli elementi sulla diagonale principale.

### 7. Esercizi

La Lezione 6 *(pp. 1–4)* applica immediatamente sottomatrici, minori e riduzione per righe agli esempi appena svolti sopra e al Teorema di Rouché-Capelli nella sezione successiva [4.3](#sec-4-3).

<!-- section: sec-4-3 | num: 4.3 | title: Matrice completa, Teorema di Rouché-Capelli e sistemi generali e parametrici | kind: section | part: cap-4 -->

### 1. Idea in parole semplici

Arriviamo ora al teorema centrale di tutto il capitolo sui sistemi lineari: il **Teorema di Rouché-Capelli**. Immagina il sistema $AX = B$ scritto come una matrice incompleta $A$ (solo i coefficienti) affiancata dalla colonna $B$ dei termini noti a formare la **matrice completa** $A|B$.

La domanda "il sistema ammette almeno una soluzione?" equivale esattamente a chiedere: *quando aggiungo la colonna $B$ ad $A$, il rango aumenta oppure resta uguale?*
- Se $\operatorname{rk} A < \operatorname{rk}(A|B)$, la colonna $B$ ha "introdotto una contraddizione" (come una riga `0 0 ... 0 | 1`): il sistema è **impossibile**.
- Se $\operatorname{rk} A = \operatorname{rk}(A|B) = r$, il sistema è **risolubile**! E quante soluzioni ha? Dipende da quanti parametri restano liberi, cioè dalla differenza **$n - r$** *(numero incognite meno rango)*: una sola soluzione se $n = r$, infinite ($\infty^{n-r}$) se $n > r$.

### 2. Definizioni e enunciati precisi

:::def Definizione — Matrice incompleta e matrice completa $A|B$ (Lezione 6, p. 4)
Dato un sistema lineare $AX = B$ con $A \in K^{m,n}$ e $B \in K^{m,1}$:
- $A$ si chiama **matrice dei coefficienti** o **matrice incompleta** del sistema;
- la matrice $A|B \in K^{m,n+1}$ ottenuta affiancando ad $A$ la colonna $B$ dei termini noti si chiama **matrice completa**.
:::

:::thm Teorema di Rouché-Capelli (Lezione 6, p. 4)
Un sistema lineare $AX = B$ è **risolubile** se e solo se:

$$\operatorname{rk} A = \operatorname{rk}(A|B)$$

*(La dimostrazione completa di questo teorema verrà svolta nella Lezione 9 utilizzando il Teorema di Kronecker: vedi Sezione [5.6](#sec-5-6).)*
:::

:::thm Proposizione — Numero di parametri liberi e $\infty^{n-r}$ soluzioni (Lezione 6, p. 4)
Sia $AX = B$ un sistema lineare risolubile con $A \in K^{m,n}$, e poniamo $r = \operatorname{rk} A = \operatorname{rk}(A|B)$. Le soluzioni del sistema dipendono da **$n - r$ parametri liberi**. Quindi:
1. se $n = r$, il sistema ha **una ed una sola soluzione**;
2. se $n > r$, il sistema ha **infinite soluzioni** dipendenti da $n - r$ parametri liberi (diremo che ci sono **$\infty^{n-r}$ soluzioni**).
:::

#### Riepilogo operativo in 4 passi *(Lezione 7, p. 5)*

<svg class="svg-diagram" viewBox="0 0 700 265" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Flusso operativo in 4 passi per risolvere AX=B con Rouché-Capelli">
  <rect x="0" y="0" width="700" height="265" rx="10" fill="#13161d"/>
  <rect x="20" y="24" width="150" height="58" rx="8" fill="#1e293b" stroke="#7cc4fa" stroke-width="1.6"/>
  <text x="95" y="47" text-anchor="middle" fill="#abc7ff" font-size="12" font-weight="bold" font-family="sans-serif">(1) Calcola rk A</text>
  <text x="95" y="65" text-anchor="middle" fill="#c2c5d0" font-size="11" font-family="sans-serif">matrice incompleta</text>

  <line x1="170" y1="53" x2="205" y2="53" stroke="#8d919e" stroke-width="1.8"/>
  <polygon points="205,53 196,48 196,58" fill="#8d919e"/>

  <rect x="205" y="24" width="160" height="58" rx="8" fill="#1e293b" stroke="#7cc4fa" stroke-width="1.6"/>
  <text x="285" y="47" text-anchor="middle" fill="#abc7ff" font-size="12" font-weight="bold" font-family="sans-serif">(2) Calcola rk(A|B)</text>
  <text x="285" y="65" text-anchor="middle" fill="#c2c5d0" font-size="11" font-family="sans-serif">matrice completa</text>

  <line x1="365" y1="53" x2="400" y2="53" stroke="#8d919e" stroke-width="1.8"/>
  <polygon points="400,53 391,48 391,58" fill="#8d919e"/>

  <rect x="400" y="24" width="280" height="58" rx="8" fill="#1f2333" stroke="#c7b3ff" stroke-width="1.6"/>
  <text x="540" y="47" text-anchor="middle" fill="#c7b3ff" font-size="12" font-weight="bold" font-family="sans-serif">(3) Rouché-Capelli: rk A = rk(A|B)?</text>
  <text x="540" y="65" text-anchor="middle" fill="#c2c5d0" font-size="11" font-family="sans-serif">Confronto (meglio su A|B già ridotta!)</text>

  <!-- Bivio NO -->
  <line x1="470" y1="82" x2="470" y2="122" stroke="#f3a1a8" stroke-width="1.8"/>
  <line x1="470" y1="122" x2="180" y2="122" stroke="#f3a1a8" stroke-width="1.8"/>
  <line x1="180" y1="122" x2="180" y2="152" stroke="#f3a1a8" stroke-width="1.8"/>
  <polygon points="180,152 175,143 185,143" fill="#f3a1a8"/>
  <text x="325" y="114" text-anchor="middle" fill="#f3a1a8" font-size="11.5" font-weight="bold" font-family="sans-serif">NO: rk A &lt; rk(A|B)</text>

  <rect x="55" y="152" width="250" height="86" rx="8" fill="#2a161b" stroke="#f3a1a8" stroke-width="1.6"/>
  <text x="180" y="182" text-anchor="middle" fill="#f3a1a8" font-size="13" font-weight="bold" font-family="sans-serif">SISTEMA IMPOSSIBILE</text>
  <text x="180" y="205" text-anchor="middle" fill="#e3e4eb" font-size="11.5" font-family="sans-serif">Nessuna soluzione (insieme vuoto ∅)</text>
  <text x="180" y="224" text-anchor="middle" fill="#9397a6" font-size="10.5" font-family="sans-serif">Fine immediata dello studio</text>

  <!-- Bivio SI -->
  <line x1="590" y1="82" x2="590" y2="122" stroke="#8ad8b0" stroke-width="1.8"/>
  <line x1="590" y1="122" x2="515" y2="122" stroke="#8ad8b0" stroke-width="1.8"/>
  <line x1="515" y1="122" x2="515" y2="152" stroke="#8ad8b0" stroke-width="1.8"/>
  <polygon points="515,152 510,143 520,143" fill="#8ad8b0"/>
  <text x="558" y="114" text-anchor="middle" fill="#8ad8b0" font-size="11.5" font-weight="bold" font-family="sans-serif">SÌ: rk A = rk(A|B) = r</text>

  <rect x="355" y="152" width="320" height="86" rx="8" fill="#13251f" stroke="#8ad8b0" stroke-width="1.6"/>
  <text x="515" y="177" text-anchor="middle" fill="#8ad8b0" font-size="12.5" font-weight="bold" font-family="sans-serif">(4) SISTEMA RISOLUBILE: calcola X</text>
  <text x="515" y="199" text-anchor="middle" fill="#e3e4eb" font-size="11.5" font-family="sans-serif">• n = r  ⇒ 1 unica soluzione (Cramer / sostituzione)</text>
  <text x="515" y="219" text-anchor="middle" fill="#e3e4eb" font-size="11.5" font-family="sans-serif">• n &gt; r ⇒ ∞ⁿ⁻ʳ soluzioni (n − r variabili libere)</text>
</svg>

### 3. Dimostrazioni

La dimostrazione del Teorema di Rouché-Capelli viene svolta dal docente dopo l'introduzione degli spazi delle colonne e del Teorema di Kronecker nella Sezione [5.6](#sec-5-6).

### 4. Esempi svolti

:::example Esempio 4.3.1 — Costruzione di $A|B$ (Lezione 6, p. 4)
Dato il sistema $\begin{cases} 2x + 3y + 4z = 5 \\ 3x + y + 6z = 1 \end{cases}$, la matrice completa è:

$$A|B = \left(\begin{array}{ccc|c} 2 & 3 & 4 & 5 \\ 3 & 1 & 6 & 1 \end{array}\right) \in \mathbb{R}^{2,4}$$
:::

:::example Esempio 4.3.2 — Sistema $2 \times 3$ con $\infty^1$ soluzioni (Lezione 6, p. 5)
Risolvere:

$$\begin{cases} 2x + 3y + 4z = 1 \\ 4x + y + 3z = 3 \end{cases}$$

1. **Ranghi e Rouché-Capelli:** in $A|B = \left(\begin{array}{ccc|c} 2 & 3 & 4 & 1 \\ 4 & 1 & 3 & 3 \end{array}\right)$, il minore $\det\begin{pmatrix} 2 & 3 \\ 4 & 1 \end{pmatrix} = 2 - 12 = -10 \neq 0$, quindi $\operatorname{rk} A = \operatorname{rk}(A|B) = 2$. Il sistema è risolubile! Con $n = 3$ variabili e $r = 2$, si hanno $n - r = 1$ parametro libero ($\infty^1$ soluzioni).
2. **Risoluzione portando la variabile libera $z$ a destra:**
    $$\begin{cases} 2x + 3y = 1 - 4z \\ 4x + y = 3 - 3z \end{cases}, \qquad C = \begin{pmatrix} 2 & 3 \\ 4 & 1 \end{pmatrix},\quad \det C = -10$$
    Applicando la Regola di Cramer in $x$ e $y$ *(considerando $z$ come parametro)*:
    $$x = -\frac{1}{10}\det\begin{pmatrix} 1-4z & 3 \\ 3-3z & 1 \end{pmatrix} = -\frac{1}{10}(1 - 4z - 9 + 9z) = -\frac{1}{10}(5z - 8) = \frac{8 - 5z}{10}$$
    $$y = -\frac{1}{10}\det\begin{pmatrix} 2 & 1-4z \\ 4 & 3-3z \end{pmatrix} = -\frac{1}{10}(6 - 6z - 4 + 16z) = -\frac{1}{10}(10z + 2) = -\frac{5z + 1}{5}$$
3. **Forma vettoriale generale ($z \in \mathbb{R}$):**
    $$X = \begin{pmatrix} \frac{8-5z}{10} \\ -\frac{5z+1}{5} \\ z \end{pmatrix} = \begin{pmatrix} \frac{4}{5} \\ -\frac{1}{5} \\ 0 \end{pmatrix} + z\begin{pmatrix} -\frac{1}{2} \\ -1 \\ 1 \end{pmatrix}$$
:::

:::example Esempio 4.3.3 — Sistema sovradeterminato $3 \times 2$ con soluzione unica (Lezione 7, p. 1)
Risolvere:

$$\begin{cases} x + 2y = 4 \\ 2x + y = 5 \\ 3x + y = 7 \end{cases}$$

Riduciamo per righe la matrice completa $A|B$:

$$\left(\begin{array}{cc|c} \boxed{1} & 2 & 4 \\ 2 & 1 & 5 \\ 3 & 1 & 7 \end{array}\right) \xrightarrow{\substack{R_2 \mapsto R_2 - 2R_1 \\ R_3 \mapsto R_3 - 3R_1}} \left(\begin{array}{cc|c} \boxed{1} & 2 & 4 \\ 0 & -3 & -3 \\ 0 & -5 & -5 \end{array}\right) \xrightarrow{\substack{R_2 \mapsto -\frac{1}{3}R_2 \\ R_3 \mapsto -\frac{1}{5}R_3}} \left(\begin{array}{cc|c} \boxed{1} & 2 & 4 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{array}\right) \xrightarrow{R_3 \mapsto R_3 - R_2} \left(\begin{array}{cc|c} \boxed{1} & 2 & 4 \\ 0 & \boxed{1} & 1 \\ 0 & 0 & 0 \end{array}\right)$$

Leggiamo entrambi i ranghi direttamente dall'ultima matrice: $\operatorname{rk} A = \operatorname{rk}(A|B) = 2 = n$, quindi il sistema ha una sola soluzione, letta dal sistema ridotto $\begin{cases} x+2y=4 \\ y=1 \end{cases} \implies \bar{X} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$.
:::

:::example Esempio 4.3.4 — Discussione parametrica $2\times 2$ completa (Lezione 7, pp. 1–3)
Risolvere al variare di $h \in \mathbb{R}$:

$$\begin{cases} x + hy = 2 \\ hx + y = 2 \end{cases}$$

1. **Matrice dei coefficienti e determinante:** $A = \begin{pmatrix} 1 & h \\ h & 1 \end{pmatrix}$, $\det A = 1 - h^2 = 0 \iff h = \pm 1$.
2. **I caso ($h \neq \pm 1$):** $\det A \neq 0 \implies \operatorname{rk} A = \operatorname{rk}(A|B) = 2 = n$: sistema di Cramer con soluzione unica:
    $$x = \frac{1}{1-h^2}\det\begin{pmatrix} 2 & h \\ 2 & 1 \end{pmatrix} = \frac{2-2h}{(1-h)(1+h)} = \frac{2}{1+h}, \qquad y = \frac{1}{1-h^2}\det\begin{pmatrix} 1 & 2 \\ h & 2 \end{pmatrix} = \frac{2-2h}{(1-h)(1+h)} = \frac{2}{1+h}$$
    cioè $\bar{X} = \frac{2}{1+h}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
3. **II caso ($h = -1$):** $A|B = \left(\begin{array}{cc|c} 1 & -1 & 2 \\ -1 & 1 & 2 \end{array}\right) \xrightarrow{R_2 \mapsto R_2 + R_1} \left(\begin{array}{cc|c} \boxed{1} & -1 & 2 \\ 0 & 0 & \boxed{4} \end{array}\right)$, perciò $\operatorname{rk} A = 1 < 2 = \operatorname{rk}(A|B)$: **non risolubile** (impossibile).
4. **III caso ($h = 1$):** $A|B = \left(\begin{array}{cc|c} 1 & 1 & 2 \\ 1 & 1 & 2 \end{array}\right) \xrightarrow{R_2 \mapsto R_2 - R_1} \left(\begin{array}{cc|c} \boxed{1} & 1 & 2 \\ 0 & 0 & 0 \end{array}\right)$, quindi $\operatorname{rk} A = \operatorname{rk}(A|B) = 1$ e si hanno $n - r = 1$ parametro libero ($\infty^1$ soluzioni). Il sistema equivale a $x + y = 2 \implies y = 2 - x$, da cui l'insieme delle soluzioni:
    $$\mathcal{S} = \left\{ \begin{pmatrix} 0 \\ 2 \end{pmatrix} + x\begin{pmatrix} 1 \\ -1 \end{pmatrix} \;\middle|\; x \in \mathbb{R} \right\}$$
:::

:::example Esempio 4.3.5 — Sistema parametrico $3 \times 3$ completo (Lezione 7, pp. 3–5, incluso il completamento richiesto a p. 5)
Risolvere al variare di $h \in \mathbb{R}$:

$$\begin{cases} (h-1)x + 3y + 2z = 5 \\ 2x + (h+4)y + 4z = 1 \\ x + 3y + hz = -4 \end{cases}$$

:::note Nota sugli appunti originali (`Lez07`, p. 3 e p. 5)
1. Nel testo della terza equazione a `Lez07` p. 3 manca per refuso grafico la lettera $z$ (è scritto $x + 3y + h = -4$); nella matrice $A|B$ scritta immediatamente sotto compare correttamente il coefficiente $h$ nella colonna di $z$ ($x + 3y + hz = -4$).
2. A p. 5 il docente termina la classificazione dei tre casi scrivendo **"COMPLETARE L'ESERCIZIO CALCOLANDO LE SOLUZIONI DEL SISTEMA"**: qui sotto riportiamo sia tutti i passi di classificazione svolti in aula sia il calcolo completo delle soluzioni mancanti nei casi $h \neq 2,-7$ e $h = -7$.
:::

1. **Determinante di $A$ e scomposizione di Ruffini:**
    $$\det A = (h-1)(h+4)h + 12 + 12 - 2(h+4) - 12(h-1) - 6h = h^3 + 3h^2 - 4h + 24 - 2h - 8 - 12h + 12 - 6h = h^3 + 3h^2 - 24h + 28$$
    Testiamo $h = 2$: $8 + 12 - 48 + 28 = 0$. Con Ruffini si fattorizza $h^3 + 3h^2 - 24h + 28 = (h - 2)(h^2 + 5h - 14)$; le radici di $h^2 + 5h - 14 = 0$ sono $h = \frac{-5 \pm 9}{2}$, ossia $2$ e $-7$, quindi:
    $$\det A = (h - 2)^2 (h + 7)$$
    Pertanto $\det A = 0 \iff h = 2 \text{ oppure } h = -7$.

2. **III caso ($h = 2$, svolto in aula p. 4–5):**
    $$A|B = \left(\begin{array}{ccc|c} 1 & 3 & 2 & 5 \\ 2 & 6 & 4 & 1 \\ 1 & 3 & 2 & -4 \end{array}\right) \xrightarrow{\substack{R_2 \mapsto R_2 - 2R_1 \\ R_3 \mapsto R_3 - R_1}} \left(\begin{array}{ccc|c} \boxed{1} & 3 & 2 & 5 \\ 0 & 0 & 0 & -9 \\ 0 & 0 & 0 & -9 \end{array}\right) \xrightarrow{\substack{R_2 \mapsto -\frac{1}{9}R_2 \\ R_3 \mapsto -\frac{1}{9}R_3 \\ \text{poi } R_3 \mapsto R_3 - R_2}} \left(\begin{array}{ccc|c} \boxed{1} & 3 & 2 & 5 \\ 0 & 0 & 0 & \boxed{1} \\ 0 & 0 & 0 & 0 \end{array}\right)$$
    Si ha $\operatorname{rk} A = 1 < 2 = \operatorname{rk}(A|B)$: per $h = 2$ il sistema **non ha soluzioni** (impossibile).

3. **II caso ($h = -7$, completamento di `Lez07` p. 4–5):**
    In aula $A|B$ viene ridotta a:
    $$A|B = \left(\begin{array}{ccc|c} -8 & 3 & 2 & 5 \\ 2 & -3 & 4 & 1 \\ 1 & 3 & -7 & -4 \end{array}\right) \xrightarrow{\substack{R_2 \mapsto 4R_2 + R_1 \\ R_3 \mapsto 8R_3 + R_1}} \left(\begin{array}{ccc|c} -8 & 3 & 2 & 5 \\ 0 & -9 & 18 & 9 \\ 0 & 27 & -54 & -27 \end{array}\right) \xrightarrow{\substack{R_2 \mapsto -\frac{1}{9}R_2,\ R_3 \mapsto \frac{1}{27}R_3 \\ \text{poi } R_3 \mapsto R_3 - R_2}} \left(\begin{array}{ccc|c} \boxed{-8} & 3 & 2 & 5 \\ 0 & \boxed{1} & -2 & -1 \\ 0 & 0 & 0 & 0 \end{array}\right)$$
    Quindi $\operatorname{rk} A = \operatorname{rk}(A|B) = 2$ e il sistema ha $\infty^{3-2} = \infty^1$ soluzioni. Ricaviamo le soluzioni esplicite usando $z \in \mathbb{R}$ come variabile libera:
    $$\begin{cases} -8x + 3y + 2z = 5 \\ y - 2z = -1 \end{cases} \implies \begin{cases} y = 2z - 1 \\ -8x + 3(2z - 1) + 2z = 5 \end{cases} \implies \begin{cases} y = 2z - 1 \\ -8x + 8z - 3 = 5 \end{cases} \implies \begin{cases} x = z - 1 \\ y = 2z - 1 \end{cases}$$
    L'insieme delle soluzioni per $h = -7$ è dunque:
    $$\mathcal{S} = \left\{ \begin{pmatrix} -1 \\ -1 \\ 0 \end{pmatrix} + z\begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} \;\middle|\; z \in \mathbb{R} \right\}$$

4. **I caso ($h \neq 2$ e $h \neq -7$, completamento con Cramer):**
    Il sistema è di Cramer e ammette un'unica soluzione. Calcoliamo i tre determinanti sostituendo le colonne con $B = (5, 1, -4)^T$:
    - $\det A_{(1)} = \det\begin{pmatrix} 5 & 3 & 2 \\ 1 & h+4 & 4 \\ -4 & 3 & h \end{pmatrix} = 5(h^2+4h-12) - 3(h+16) + 2(3+4h+16) = 5h^2 + 25h - 70 = 5(h-2)(h+7)$
    - $\det A_{(2)} = \det\begin{pmatrix} h-1 & 5 & 2 \\ 2 & 1 & 4 \\ 1 & -4 & h \end{pmatrix} = (h-1)(h+16) - 5(2h-4) + 2(-8-1) = h^2 + 5h - 14 = (h-2)(h+7)$
    - $\det A_{(3)} = \det\begin{pmatrix} h-1 & 3 & 5 \\ 2 & h+4 & 1 \\ 1 & 3 & -4 \end{pmatrix} = (h-1)(-4h-19) - 3(-8-1) + 5(6-h-4) = -4h^2 - 20h + 56 = -4(h-2)(h+7)$

    Dividendo per $\det A = (h-2)^2(h+7)$ si semplificano sia $(h-2)$ sia $(h+7)$, ottenendo l'unica soluzione:
    $$\bar{X} = \begin{pmatrix} \frac{5}{h-2} \\ \frac{1}{h-2} \\ \frac{-4}{h-2} \end{pmatrix}$$
:::

### 5. Errori comuni e trappole

1. **Calcolare separatamente $\operatorname{rk} A$ e $\operatorname{rk}(A|B)$ con due riduzioni diverse sprecando tempo**
    - *Sbagliato:* ridurre prima $A$, poi riscrivere da zero $A|B$ e ridurla da capo.
    - *Correzione:* **riduci direttamente la matrice completa $A|B$** *(come nell'Esempio 4.3.3 e 4.3.5)*: le operazioni elementari sulle righe agiscono contemporaneamente su $A$ (le prime $n$ colonne a sinistra della barra verticale) e su $A|B$ (tutte le $n+1$ colonne), così a fine riduzione leggi **entrambi i ranghi in un colpo solo**!
2. **Dimenticare di controllare $\operatorname{rk} A = \operatorname{rk}(A|B)$ e pensare che bastino le righe non nulle**
    - *Sbagliato:* vedere $2$ righe non nulle in $A|B$ e concludere subito che ci sono $n - 2$ parametri liberi.
    - *Correzione:* se nella riduzione compare una riga del tipo `(0 0 ... 0 | 1)`, essa conta nel rango di $A|B$ ma **non** in quello di $A$: quindi $\operatorname{rk} A < \operatorname{rk}(A|B)$ e il sistema non ha soluzioni!

### 6. Riepilogo

- La **matrice completa** $A|B \in K^{m,n+1}$ affianca alla matrice incompleta $A$ la colonna dei termini noti $B$.
- **Teorema di Rouché-Capelli:** $AX = B$ è risolubile $\iff \operatorname{rk} A = \operatorname{rk}(A|B)$.
- Se è risolubile con $r = \operatorname{rk} A = \operatorname{rk}(A|B)$ e $n$ incognite, ci sono $n - r$ **parametri liberi** ($\infty^{n-r}$ soluzioni se $n > r$, unica soluzione se $n = r$).
- **Strategia in 4 passi:** (1) $\operatorname{rk} A$; (2) $\operatorname{rk}(A|B)$; (3) confronto con Rouché-Capelli; (4) calcolo effettivo delle soluzioni.
- Per sistemi parametrici quadrati conviene quasi sempre partire studiando $\det A = 0$ per isolare subito il caso di Cramer ($\det A \neq 0$) dai pochi valori critici del parametro.

### 7. Esercizi

:::exercise Esercizio 4.3.1 (Esercizio per casa — Medio · Lezione 7, p. 5)
Risolvere al variare del parametro $h \in \mathbb{R}$ il seguente sistema lineare:

$$\begin{cases} x + y + z = 1 \\ 2x + 2y - z = 2 \\ x + 5z = 1 \\ y + 3z = h \end{cases}$$

:::solution Soluzione spiegata passo-passo
**Ragionamento:** abbiamo un sistema di $4$ equazioni in $n = 3$ incognite, quindi riduciamo direttamente per righe la matrice completa $A|B \in \mathbb{R}^{4,4}$ per leggere simultaneamente $\operatorname{rk} A$ e $\operatorname{rk}(A|B)$ al variare di $h$.

1. **Costruzione e riduzione della matrice completa $A|B$:**
    $$A|B = \left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 2 & 2 & -1 & 2 \\ 1 & 0 & 5 & 1 \\ 0 & 1 & 3 & h \end{array}\right)$$
    Eliminiamo la $x$ dalle righe $2$ e $3$ mediante $R_2 \mapsto R_2 - 2R_1$ e $R_3 \mapsto R_3 - R_1$:
    $$\longrightarrow \left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 0 & -3 & 0 \\ 0 & -1 & 4 & 0 \\ 0 & 1 & 3 & h \end{array}\right)$$
    Riscaliamo $R_2 \mapsto -\frac{1}{3}R_2$ per semplificare la seconda riga in $(0\ 0\ 1\mid 0)$ e sommiamo la riga $3$ alla riga $4$ ($R_4 \mapsto R_4 + R_3$) per eliminare la $y$:
    $$\longrightarrow \left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & -1 & 4 & 0 \\ 0 & 0 & 7 & h \end{array}\right)$$
    Ora annulliamo il $7$ in posizione $(4,3)$ mediante $R_4 \mapsto R_4 - 7R_2$:
    $$\longrightarrow \left(\begin{array}{ccc|c} \boxed{1} & 1 & 1 & 1 \\ 0 & 0 & \boxed{1} & 0 \\ 0 & \boxed{-1} & 4 & 0 \\ 0 & 0 & 0 & h \end{array}\right)$$

2. **Discussione dei ranghi con Rouché-Capelli:**
    Le prime tre righe di $A$ hanno già $3$ elementi speciali ($1$ in col. 1, $1$ in col. 3, $-1$ in col. 2 con tutti zeri sotto di sé), mentre la quarta riga della parte incompleta è $(0\ 0\ 0)$: quindi $\operatorname{rk} A = 3$ per qualunque $h \in \mathbb{R}$. Guardando la colonna completa:
    - **I caso ($h \neq 0$):** la quarta riga vale $(0\ 0\ 0 \mid h)$ con $h \neq 0$, quindi $\operatorname{rk}(A|B) = 4 \neq 3 = \operatorname{rk} A$. Il sistema è **impossibile** (non ammette soluzioni).
    - **II caso ($h = 0$):** la quarta riga è interamente nulla, quindi $\operatorname{rk} A = \operatorname{rk}(A|B) = 3 = n$. Il sistema è risolubile ed ammette **una ed una sola soluzione** ($n - r = 0$).

3. **Calcolo della soluzione unica nel caso $h = 0$:**
    Dal sistema ridotto:
    $$\begin{cases} z = 0 \\ -y + 4z = 0 \implies y = 0 \\ x + y + z = 1 \implies x = 1 \end{cases}$$
    La soluzione unica per $h = 0$ è dunque $\bar{X} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$ *(verificabile immediatamente sostituendo $x=1, y=0, z=0$ in tutte e 4 le equazioni iniziali)*.
:::
:::
