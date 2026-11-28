<!-- part: cap-2 | num: 2 | label: CAPITOLO 2 | title: Matrici e algebra matriciale | refs: Fonti: Lezione 3 (12/10/2026, pp. 1–11) -->

<!-- section: sec-2-1 | num: 2.1 | title: Definizione formale di matrice e gruppo abeliano delle matrici | kind: section | part: cap-2 -->

### 1. Idea in parole semplici

Una **matrice** è semplicemente una **tabella rettangolare ordinata di numeri** (più in generale, di elementi di un campo $K$), organizzata in **$m$ righe orizzontali** e **$n$ colonne verticali**, esattamente come un foglio di calcolo.

Per indicare con precisione il contenuto di una casella senza ambiguità, servono due coordinate nello stesso ordine di sempre: prima il numero di **riga** ($i$) e poi il numero di **colonna** ($j$). Quando due matrici hanno esattamente le stesse dimensioni ($m \times n$), possiamo sommarle casella per casella: otteniamo così un vero **gruppo abeliano** $(K^{m,n}, +)$, del tutto analogo a quello dei numeri interi o reali.

### 2. Definizioni e enunciati precisi

Sia $(K, +, \cdot)$ un campo (ad esempio $K = \mathbb{R}$, il campo dei numeri reali) e siano $m, n \in \mathbb{Z}$ con $m > 0$ e $n > 0$ *(Lezione 3, p. 1)*.

:::def Definizione — Matrice e notazioni $K^{m,n}$ e $\operatorname{ent}_{ij}(A)$ (Lezione 3, p. 1)
Si chiama **matrice con $m$ righe ed $n$ colonne ad elementi nel campo $K$** una funzione:

$$\{1, \dots, m\} \times \{1, \dots, n\} \longrightarrow K$$

Poniamo inoltre:
- $K^{m,n} \stackrel{\text{DEF}}{=}$ insieme di tutte le matrici con $m$ righe ed $n$ colonne ad elementi in $K$.
- Per ogni $A \in K^{m,n}$, $\operatorname{ent}_{ij}(A) \stackrel{\text{DEF}}{=}$ elemento (*entrata*) di $A$ che si trova sulla riga $i$ e sulla colonna $j$ *(con $1 \le i \le m$ e $1 \le j \le n$)*.

Per rappresentare graficamente una matrice si utilizza una tabella racchiusa tra parentesi tonde, formata da $m$ righe ed $n$ colonne.
:::

:::def Definizione — Addizione tra matrici (Lezione 3, p. 2)
Siano $A \in K^{m,n}$ e $B \in K^{m,n}$ due matrici della **stessa taglia** $m \times n$. La matrice somma $A + B \in K^{m,n}$ è definita casella per casella ponendo:

$$\operatorname{ent}_{ij}(A + B) \stackrel{\text{DEF}}{=} \operatorname{ent}_{ij}(A) + \operatorname{ent}_{ij}(B) \qquad \forall i \in \{1,\dots,m\},\ \forall j \in \{1,\dots,n\}$$
:::

:::thm Proposizione — Struttura di gruppo abeliano di $(K^{m,n}, +)$ (Lezione 3, pp. 2–3)
Per ogni campo $K$ e ogni scelta di $m, n > 0$, la struttura $(K^{m,n}, +)$ è un **gruppo abeliano**.
- L'elemento neutro è la **matrice nulla** $O \in K^{m,n}$, avente tutti gli elementi uguali a $0 \in K$.
- L'inverso additivo (*opposto*) di $A \in K^{m,n}$ è la **matrice opposta** $-A \in K^{m,n}$, definita da:
    $$\operatorname{ent}_{ij}(-A) \stackrel{\text{DEF}}{=} -\operatorname{ent}_{ij}(A)$$
:::

### 3. Dimostrazioni

:::proof Dimostrazione — $(K^{m,n}, +)$ è un gruppo abeliano (Lezione 3, pp. 2–3)
**Idea di fondo:** poiché l'addizione tra matrici si calcola elemento per elemento dentro il campo $K$, essa eredita automaticamente tutte le proprietà del gruppo abeliano $(K, +)$.

Verifichiamo tutti e $5$ i requisiti di un gruppo abeliano *(cfr. Sezione 1.3)*:
1. **Operazione binaria interna:** prese $A, B \in K^{m,n}$, per ogni posto $(i,j)$ la somma $\operatorname{ent}_{ij}(A) + \operatorname{ent}_{ij}(B)$ appartiene ancora a $K$, quindi $A + B \in K^{m,n}$.
2. **Proprietà associativa:** per l'associatività dell'addizione in $K$, vale $(A + B) + C = A + (B + C)$ per ogni $A, B, C \in K^{m,n}$.
3. **Elemento neutro:** definiamo la **matrice nulla**
    $$O = \begin{pmatrix} 0 & 0 & \dots & 0 \\ 0 & 0 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 0 \end{pmatrix} \in K^{m,n}$$
    Sommando $0$ a ogni elemento di $A$ si riottiene $A$, quindi $A + O = O + A = A$ per ogni $A \in K^{m,n}$.
4. **Esistenza dell'inverso additivo (opposta):** per ogni $A \in K^{m,n}$ definiamo $-A$ ponendo $\operatorname{ent}_{ij}(-A) \stackrel{\text{DEF}}{=} -\operatorname{ent}_{ij}(A)$. Poiché $\operatorname{ent}_{ij}(A) + (-\operatorname{ent}_{ij}(A)) = 0$ in ogni casella, segue:
    $$A + (-A) = (-A) + A = O$$
5. **Proprietà commutativa:** per la commutatività di $+$ in $K$, si ha $\operatorname{ent}_{ij}(A+B) = \operatorname{ent}_{ij}(B+A)$, quindi $A + B = B + A$ per ogni $A, B \in K^{m,n}$.
:::

### 4. Esempi svolti

:::example Esempio 2.1.1 — Lettura degli indici $\operatorname{ent}_{ij}(A)$ (Lezione 3, p. 1)
Consideriamo la matrice reale con $2$ righe e $3$ colonne:

$$A = \begin{pmatrix} 2 & 3 & \sqrt{2} \\ 6 & -4 & 1 \end{pmatrix} \in \mathbb{R}^{2,3}$$

- $\operatorname{ent}_{13}(A)$ si trova sulla **riga $1$** e sulla **colonna $3$**: quindi $\operatorname{ent}_{13}(A) = \sqrt{2}$.
- $\operatorname{ent}_{22}(A)$ si trova sulla **riga $2$** e sulla **colonna $2$**: quindi $\operatorname{ent}_{22}(A) = -4$.
:::

:::example Esempio 2.1.2 — Addizione tra due matrici di $\mathbb{R}^{2,3}$ (Lezione 3, p. 2)
Siano:

$$A = \begin{pmatrix} 4 & 1 & -5 \\ 3 & 6 & 2 \end{pmatrix} \in \mathbb{R}^{2,3}, \qquad B = \begin{pmatrix} 1 & 2 & 6 \\ 5 & 1 & -4 \end{pmatrix} \in \mathbb{R}^{2,3}$$

Sommando i numeri nelle posizioni corrispondenti *(per esempio in $(1,1)$ abbiamo $4+1=5$, in $(1,2)$ abbiamo $1+2=3$)* otteniamo:

$$A + B = \begin{pmatrix} 4+1 & 1+2 & -5+6 \\ 3+5 & 6+1 & 2+(-4) \end{pmatrix} = \begin{pmatrix} 5 & 3 & 1 \\ 8 & 7 & -2 \end{pmatrix} \in \mathbb{R}^{2,3}$$
:::

:::example Esempio 2.1.3 — Matrice opposta $-A$ (Lezione 3, p. 3)
Sia $A = \begin{pmatrix} 5 & 1 & -3 \\ -6 & 8 & 2 \end{pmatrix} \in \mathbb{R}^{2,3}$. Cambiando il segno a tutte le entrate otteniamo la sua opposta:

$$-A = \begin{pmatrix} -5 & -1 & 3 \\ 6 & -8 & -2 \end{pmatrix}$$

Sommando le due matrici si verifica subito l'annullamento:

$$A + (-A) = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = O$$
:::

### 5. Errori comuni e trappole

1. **Scambiare l'indice di riga con quello di colonna in $\operatorname{ent}_{ij}(A)$**

    - *Sbagliato:* leggere $\operatorname{ent}_{13}(A)$ nell'Esempio 2.1.1 cercando la colonna $1$ e la riga $3$ (che neppure esiste!).
    - *Correzione:* il primo indice ($i$) è sempre la **riga**, il secondo indice ($j$) è sempre la **colonna** (*Regola "Riga prima, Colonna poi"*).

2. **Provare a sommare matrici di dimensioni diverse**

    - *Sbagliato:* cercare di calcolare $A + B$ quando $A \in \mathbb{R}^{2,3}$ e $B \in \mathbb{R}^{3,2}$.
    - *Correzione:* l'addizione è definita **solo** tra matrici aventi lo stesso numero di righe $m$ e lo stesso numero di colonne $n$.

### 6. Riepilogo

- Una matrice in $K^{m,n}$ è una funzione $\{1,\dots,m\}\times\{1,\dots,n\}\to K$ rappresentata in una tabella di $m$ righe e $n$ colonne.
- $\operatorname{ent}_{ij}(A)$ denota l'elemento sulla riga $i$ e colonna $j$.
- L'addizione tra matrici della stessa taglia $K^{m,n}$ somma le entrate corrispondenti.
- $(K^{m,n}, +)$ è un **gruppo abeliano** per ogni $m, n > 0$.
- L'elemento neutro è la matrice nulla $O$ e l'inverso additivo di $A$ è $-A$.

### 7. Esercizi

La Lezione 3 *(pp. 1–3)* non assegna esercizi per casa specifici su questo sottoparagrafo; gli esercizi ufficiali della Lezione 3 si trovano nelle sezioni [2.2](#sec-2-2) e [2.5](#sec-2-5).

<!-- section: sec-2-2 | num: 2.2 | title: Prodotto scalare per matrice e prodotto riga per colonna | kind: section | part: cap-2 -->

### 1. Idea in parole semplici

Nel mondo delle matrici esistono **due moltiplicazioni completamente diverse**, ed è fondamentale non confonderle mai:

1. **Prodotto di uno scalare per una matrice ($aA$):** moltiplichi tutti gli elementi della tabella per lo stesso numero $a$ (come scalare tutti i prezzi di un listino moltiplicandoli per $2$).
2. **Prodotto tra due matrici ($AB$, detto *riga per colonna*):** qui **non** moltiplichi casella per casella! Per trovare il numero al posto $(i,j)$ di $AB$, prendi l'intera **riga $i$** di $A$ e l'intera **colonna $j$** di $B$, moltiplichi i rispettivi elementi a coppie e sommi tutto. Perché le coppie combacino senza avanzi, il numero di colonne di $A$ deve essere uguale al numero di righe di $B$. Inoltre l'ordine conta: quasi sempre **$AB \neq BA$**.

### 2. Definizioni e enunciati precisi

:::def Definizione — Scalare e prodotto scalare per matrice (Lezione 3, p. 3)
- Si chiama **scalare** un elemento del campo $K$.
- Siano $a \in K$ e $A \in K^{m,n}$. La matrice $aA \in K^{m,n}$ è definita ponendo:
    $$\operatorname{ent}_{ij}(aA) \stackrel{\text{DEF}}{=} a\,\operatorname{ent}_{ij}(A)$$
:::

:::thm Proprietà del prodotto scalare per matrice (Lezione 3, p. 4)
Per ogni $a, b \in K$ e per ogni $M, N \in K^{m,n}$, valgono le $4$ proprietà:
1. $(a + b)M = aM + bM$ *(distributività rispetto alla somma di scalari)*;
2. $a(M + N) = aM + aN$ *(distributività rispetto alla somma di matrici)*;
3. $(ab)M = a(bM)$ *(associatività mista)*;
4. $1M = M$, dove $1$ è l'unità del campo $K$.
:::

:::def Definizione — Prodotto riga per colonna tra matrici (Lezione 3, pp. 4–5)
Siano $A \in K^{m,n}$ e $B \in K^{n,p}$ *(il numero di colonne $n$ di $A$ coincide con il numero di righe $n$ di $B$)*. Il **prodotto** $AB$ è una matrice di $K^{m,p}$ il cui elemento di posto $(i,j)$ è definito da:

$$\operatorname{ent}_{ij}(AB) \stackrel{\text{DEF}}{=} \sum_{r=1}^n \operatorname{ent}_{ir}(A)\,\operatorname{ent}_{rj}(B) \qquad (1 \le i \le m,\ 1 \le j \le p)$$
:::

Schema rapido di compatibilità delle dimensioni *(Lezione 3, p. 4)*:

$$(m \times \underbrace{n)\ \cdot\ (n}_{\text{devono coincidere!}} \times p) \longrightarrow (m \times p)$$

:::thm Proprietà del prodotto tra matrici (Lezione 3, pp. 5–6)
1. **Proprietà associativa:**
    $$(AB)C = A(BC) \qquad \forall A \in K^{m,n},\ \forall B \in K^{n,p},\ \forall C \in K^{p,q}$$
2. **Proprietà distributive** *(per matrici di dimensioni compatibili)*:

    - $(A + B)C = AC + BC \qquad \forall A, B \in K^{m,n},\ \forall C \in K^{n,p}$;
    - $A(B + C) = AB + AC \qquad \forall A \in K^{m,n},\ \forall B, C \in K^{n,p}$.

3. **Compatibilità con il prodotto per scalare:**
    $$(aM)N = a(MN) = M(aN) \qquad \forall a \in K,\ \forall M \in K^{m,n},\ \forall N \in K^{n,p}$$
4. **Non commutatività:** in generale, **il prodotto tra matrici non è commutativo**, cioè può accadere che $AB \neq BA$ anche quando entrambi i prodotti sono definiti *(Lezione 3, p. 5)*.
:::

### 3. Dimostrazioni

In questa sezione delle lezioni *(Lezione 3, pp. 3–6)* le proprietà vengono enunciate senza dimostrazione formale, mentre la **non commutatività** del prodotto tra matrici viene dimostrata esplicitamente mediante il controesempio svolto qui sotto (*Esempio 2.2.3*).

### 4. Esempi svolti

:::example Esempio 2.2.1 — Prodotto di uno scalare per una matrice (Lezione 3, p. 3)
Siano $K = \mathbb{R}$, $a = 2 \in K$ e

$$A = \begin{pmatrix} 2 & 3 \\ 1 & 9 \\ 6 & 2 \\ -3 & 5 \end{pmatrix} \in \mathbb{R}^{4,2}$$

Moltiplichiamo ogni entrata di $A$ per lo scalare $2$:

$$aA = 2 \begin{pmatrix} 2 & 3 \\ 1 & 9 \\ 6 & 2 \\ -3 & 5 \end{pmatrix} = \begin{pmatrix} 4 & 6 \\ 2 & 18 \\ 12 & 4 \\ -6 & 10 \end{pmatrix} \in \mathbb{R}^{4,2}$$
:::

:::note Nota sugli appunti originali (`Lez03`, p. 3)
Nel PDF manoscritto della Lezione 3, p. 3, nell'angolo in basso a destra del risultato di $2A$ è scritto per errore di calcolo `8` al posto di `10` (poiché $2 \cdot 5 = 10$). Qui abbiamo riportato il valore corretto `10`.
:::

:::example Esempio 2.2.2 — Prodotto riga per colonna $\mathbb{R}^{3,4} \cdot \mathbb{R}^{4,2} \to \mathbb{R}^{3,2}$ (Lezione 3, pp. 4–5)
Siano:

$$A = \begin{pmatrix} 1 & 2 & 1 & 0 \\ 3 & -1 & 2 & 1 \\ 2 & 1 & 1 & -1 \end{pmatrix} \in \mathbb{R}^{3,4}, \qquad B = \begin{pmatrix} 3 & 0 \\ 1 & 2 \\ 1 & -1 \\ -1 & 2 \end{pmatrix} \in \mathbb{R}^{4,2}$$

Poiché il numero di colonne di $A$ ($4$) è uguale al numero di righe di $B$ ($4$), il prodotto $AB$ esiste e appartiene a $\mathbb{R}^{3,2}$. Calcoliamo ciascuna delle $6$ entrate incrociando riga $i$ di $A$ e colonna $j$ di $B$:

- $\operatorname{ent}_{11}(AB) = 1\cdot 3 + 2\cdot 1 + 1\cdot 1 + 0\cdot(-1) = 3 + 2 + 1 + 0 = 6$
- $\operatorname{ent}_{12}(AB) = 1\cdot 0 + 2\cdot 2 + 1\cdot(-1) + 0\cdot 2 = 0 + 4 - 1 + 0 = 3$
- $\operatorname{ent}_{21}(AB) = 3\cdot 3 + (-1)\cdot 1 + 2\cdot 1 + 1\cdot(-1) = 9 - 1 + 2 - 1 = 9$
- $\operatorname{ent}_{22}(AB) = 3\cdot 0 + (-1)\cdot 2 + 2\cdot(-1) + 1\cdot 2 = 0 - 2 - 2 + 2 = -2$
- $\operatorname{ent}_{31}(AB) = 2\cdot 3 + 1\cdot 1 + 1\cdot 1 + (-1)\cdot(-1) = 6 + 1 + 1 + 1 = 9$
- $\operatorname{ent}_{32}(AB) = 2\cdot 0 + 1\cdot 2 + 1\cdot(-1) + (-1)\cdot 2 = 0 + 2 - 1 - 2 = -1$

Raccogliendo i risultati otteniamo:

$$AB = \begin{pmatrix} 6 & 3 \\ 9 & -2 \\ 9 & -1 \end{pmatrix} \in \mathbb{R}^{3,2}$$
:::

:::example Esempio 2.2.3 — Controesempio alla commutatività: $AB \neq BA$ (Lezione 3, p. 5)
Siano $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \in K^{2,2}$ e $B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \in K^{2,2}$. Calcoliamo entrambi i prodotti:

$$AB = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = B$$

$$BA = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = O$$

Poiché $B \neq O$, abbiamo trovato due matrici per cui $AB \neq BA$. Nota anche un altro fatto sorprendente: $B \neq O$ e $A \neq O$, eppure il loro prodotto $BA$ fa la matrice nulla $O$!
:::

### 5. Errori comuni e trappole

1. **Moltiplicare due matrici casella per casella**

    - *Sbagliato:* per due matrici $2\times 2$, calcolare $\operatorname{ent}_{ij}(AB)$ come $\operatorname{ent}_{ij}(A)\cdot\operatorname{ent}_{ij}(B)$.
    - *Correzione:* il prodotto tra matrici è **riga per colonna**, cioè $\sum_{r=1}^n \operatorname{ent}_{ir}(A)\operatorname{ent}_{rj}(B)$. Solo l'addizione si fa casella per casella!

2. **Usare le regole commutative dei numeri reali con le matrici**

    - *Sbagliato:* scrivere $(A+B)^2 = A^2 + 2AB + B^2$ oppure raccogliere $AB + BA = 2AB$.
    - *Correzione:* poiché in generale $AB \neq BA$, per le proprietà distributive si ha $(A+B)^2 = (A+B)(A+B) = A^2 + AB + BA + B^2$, e $AB + BA$ **non** si può sommare in $2AB$ se $A$ e $B$ non commutano!

3. **Dimenticare di controllare la compatibilità delle dimensioni**

    - *Sbagliato:* provare a calcolare $AB$ con $A \in \mathbb{R}^{3,4}$ e $B \in \mathbb{R}^{3,2}$, oppure tentare $BA$ nell'Esempio 2.2.2.
    - *Correzione:* nell'Esempio 2.2.2 $AB$ esiste ($\mathbb{R}^{3,4} \cdot \mathbb{R}^{4,2} \to \mathbb{R}^{3,2}$), ma $BA$ **non è proprio definito** ($\mathbb{R}^{4,2}$ ha $2$ colonne mentre $\mathbb{R}^{3,4}$ ha $3$ righe, e $2 \neq 3$).

### 6. Riepilogo

- Il prodotto scalare per matrice $aA$ moltiplica ogni entrata di $A$ per $a \in K$.
- Il prodotto $AB$ esiste solo se $A \in K^{m,n}$ e $B \in K^{n,p}$, e produce una matrice in $K^{m,p}$.
- Ogni entrata $\operatorname{ent}_{ij}(AB)$ è la somma dei prodotti tra riga $i$ di $A$ e colonna $j$ di $B$.
- Il prodotto tra matrici è associativo, distributivo rispetto a $+$, compatibile con gli scalari, ma **non è commutativo** ($AB \neq BA$ in generale).
- Può succedere che $BA = O$ pur essendo $A \neq O$ e $B \neq O$.

### 7. Esercizi

:::exercise Esercizio 2.2.1 (Esercizio per casa — Facile · Lezione 3, p. 5)
Siano:

$$A = \begin{pmatrix} 2 & 1 & 3 \\ 3 & 2 & 1 \end{pmatrix} \in \mathbb{R}^{2,3}, \qquad B = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix} \in \mathbb{R}^{3,2}$$

Calcolare $AB$ e $BA$.

:::note Nota sugli appunti originali (`Lez03`, p. 5)
Nel testo manoscritto dell'esercizio è scritto per refuso notazionale $B = \mathbb{R}^{3,2}$ anziché $B \in \mathbb{R}^{3,2}$.
:::

:::solution Soluzione spiegata passo-passo
**Ragionamento:** controlliamo prima le dimensioni di entrambi i prodotti.
- $A$ è $2\times 3$ e $B$ è $3\times 2$: poiché $3 = 3$, esiste $AB \in \mathbb{R}^{2,2}$.
- $B$ è $3\times 2$ e $A$ è $2\times 3$: poiché $2 = 2$, esiste anche $BA \in \mathbb{R}^{3,3}$.

**1. Calcoliamo $AB \in \mathbb{R}^{2,2}$:**
- $\operatorname{ent}_{11}(AB) = 2\cdot 1 + 1\cdot 2 + 3\cdot 3 = 2 + 2 + 9 = 13$
- $\operatorname{ent}_{12}(AB) = 2\cdot 4 + 1\cdot 5 + 3\cdot 6 = 8 + 5 + 18 = 31$
- $\operatorname{ent}_{21}(AB) = 3\cdot 1 + 2\cdot 2 + 1\cdot 3 = 3 + 4 + 3 = 10$
- $\operatorname{ent}_{22}(AB) = 3\cdot 4 + 2\cdot 5 + 1\cdot 6 = 12 + 10 + 6 = 28$

$$AB = \begin{pmatrix} 13 & 31 \\ 10 & 28 \end{pmatrix} \in \mathbb{R}^{2,2}$$

**2. Calcoliamo $BA \in \mathbb{R}^{3,3}$:**
- Riga 1 di $B$ con le tre colonne di $A$:

    - $1\cdot 2 + 4\cdot 3 = 2 + 12 = 14$
    - $1\cdot 1 + 4\cdot 2 = 1 + 8 = 9$
    - $1\cdot 3 + 4\cdot 1 = 3 + 4 = 7$

- Riga 2 di $B$ con le tre colonne di $A$:

    - $2\cdot 2 + 5\cdot 3 = 4 + 15 = 19$
    - $2\cdot 1 + 5\cdot 2 = 2 + 10 = 12$
    - $2\cdot 3 + 5\cdot 1 = 6 + 5 = 11$

- Riga 3 di $B$ con le tre colonne di $A$:

    - $3\cdot 2 + 6\cdot 3 = 6 + 18 = 24$
    - $3\cdot 1 + 6\cdot 2 = 3 + 12 = 15$
    - $3\cdot 3 + 6\cdot 1 = 9 + 6 = 15$

$$BA = \begin{pmatrix} 14 & 9 & 7 \\ 19 & 12 & 11 \\ 24 & 15 & 15 \end{pmatrix} \in \mathbb{R}^{3,3}$$

Osserva come in questo caso $AB$ e $BA$ non abbiano nemmeno lo stesso numero di righe e colonne!
:::
:::

<!-- section: sec-2-3 | num: 2.3 | title: Matrici quadrate, anello unitario e non invertibilità per n ≥ 2 | kind: section | part: cap-2 -->

### 1. Idea in parole semplici

Quando una matrice ha **lo stesso numero di righe e di colonne** ($m = n$), si dice **matrice quadrata** di ordine $n$. Nell'insieme $K^{n,n}$ puoi sommare e moltiplicare due matrici qualsiasi restando sempre in $K^{n,n}$.

Esiste anche una matrice speciale che fa esattamente da "numero $1$" nella moltiplicazione tra matrici: è la **matrice identica** $I$, che ha tutti $1$ sulla diagonale principale e $0$ altrove. Quindi $(K^{n,n}, +, \cdot)$ è un **anello unitario**. Ma attenzione alla differenza rispetto ai numeri reali o complessi: già per $n \ge 2$, non tutte le matrici non nulle hanno un'inversa! Proprio alla fine di questa sezione il docente lascia aperta la domanda cruciale che risolveremo nel Capitolo 3: **quali matrici in $K^{n,n}$ sono invertibili rispetto al prodotto?**

### 2. Definizioni e enunciati precisi

:::def Definizione — Matrice quadrata e matrice identica (Lezione 3, p. 6)
- Sia $A \in K^{m,n}$. La matrice $A$ si dice **quadrata** se $m = n$ *(cioè $A \in K^{n,n}$)*.
- Si chiama **matrice identica** di ordine $n$ la matrice $I \in K^{n,n}$ definita da:
    $$I = \begin{pmatrix} 1 & 0 & \dots & 0 \\ 0 & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 1 \end{pmatrix}, \qquad \operatorname{ent}_{ij}(I) \stackrel{\text{DEF}}{=} \begin{cases} 1 & \text{se } i = j \\ 0 & \text{se } i \neq j \end{cases}$$
:::

:::thm Proposizione e Osservazione — $(K^{n,n}, +, \cdot)$ è un anello unitario, ma non un corpo per $n \ge 2$ (Lezione 3, pp. 6–7)
1. $(K^{n,n}, +, \cdot)$ è un **anello unitario**, la cui unità moltiplicativa è la matrice identica $I$:
    $$AI = IA = A \qquad \forall A \in K^{n,n}$$
2. Per ogni $n \ge 2$, esistono matrici non nulle in $K^{n,n}$ che **non sono invertibili rispetto al prodotto**. Pertanto $(K^{n,n}, +, \cdot)$ **non è un corpo** per $n \ge 2$.
:::

### 3. Dimostrazioni

:::proof Dimostrazione 1 — $I$ è l'elemento neutro moltiplicativo di $(K^{n,n}, +, \cdot)$ (Lezione 3, p. 6)
**Idea di fondo:** dalle sezioni [2.1](#sec-2-1) e [2.2](#sec-2-2) sappiamo già che $(K^{n,n},+)$ è un gruppo abeliano, che il prodotto tra matrici è interno a $K^{n,n}$ ed è associativo, e che valgono le proprietà distributive. Per provare che $(K^{n,n},+,\cdot)$ è un anello unitario resta da dimostrare che $AI = IA = A$ sfruttando il fatto che $\operatorname{ent}_{rj}(I)$ vale $0$ per ogni $r \neq j$ e $1$ solo quando $r = j$.

Calcoliamo l'entrata di posto $(i,j)$ di $AI$: nella sommatoria sull'indice $r$ da $1$ a $n$, l'unico addendo con $\operatorname{ent}_{rj}(I) \neq 0$ si ha per $r = j$, quindi tutti gli altri termini si annullano:

$$\operatorname{ent}_{ij}(AI) = \sum_{r=1}^n \operatorname{ent}_{ir}(A)\operatorname{ent}_{rj}(I) = \operatorname{ent}_{ij}(A)\underbrace{\operatorname{ent}_{jj}(I)}_{1} = \operatorname{ent}_{ij}(A) \implies AI = A$$

Analogamente, in $IA$ l'unico addendo non nullo della somma si ha per $r = i$:

$$\operatorname{ent}_{ij}(IA) = \sum_{r=1}^n \operatorname{ent}_{ir}(I)\operatorname{ent}_{rj}(A) = \underbrace{\operatorname{ent}_{ii}(I)}_{1}\operatorname{ent}_{ij}(A) = \operatorname{ent}_{ij}(A) \implies IA = A$$

Dunque $I$ è l'unità di $(K^{n,n}, +, \cdot)$, che risulta un anello unitario.
:::

:::proof Dimostrazione 2 — Esistenza di matrici non nulle non invertibili per $n = 2$ (Lezione 3, p. 7)
**Idea di fondo:** usiamo una coppia di matrici non nulle $A, B \in K^{2,2}$ con prodotto nullo $BA = O$; se $A$ avesse un'inversa $A^{-1}$, moltiplicando a destra cancelleremmo $A$ e ricaveremmo l'assurdo $B = O$.

Consideriamo in $K^{2,2}$ le due matrici non nulle viste nell'Esempio 2.2.3:

$$A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \neq O$$

Sappiamo già che $BA = O$. Supponiamo **per assurdo** che $A$ sia invertibile in $K^{2,2}$, cioè che esista $A^{-1} \in K^{2,2}$ tale che $AA^{-1} = I$. Moltiplichiamo entrambi i membri di $BA = O$ a destra per $A^{-1}$:

$$BA = O \implies (BA)A^{-1} = OA^{-1} \implies B(AA^{-1}) = O \implies BI = O \implies B = O$$

Questo contraddice $B \neq O$, assurdo! Quindi $A$ non è invertibile in $K^{2,2}$ e $(K^{2,2},+,\cdot)$ non è un corpo *(lo stesso argomento si estende immediatamente a ogni $n \ge 2$ completando $A$ e $B$ con zeri nelle righe e colonne successive)*.
:::

### 4. Esempi svolti

:::example Esempio 2.3.1 — La matrice identica per $n=2$ e $n=3$ e il ruolo di $I$ (Lezione 3, pp. 6–7)
Per $n = 2$ e $n = 3$, le matrici identiche sono rispettivamente:

$$I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \in K^{2,2}, \qquad I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \in K^{3,3}$$

Con $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ e $B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, nell'anello $(K^{2,2}, +, \cdot)$ valgono $AB = B$, $BA = O$ e né $A$ né $B$ è invertibile.
:::

### 5. Errori comuni e trappole

1. **Applicare la legge di annullamento del prodotto alle matrici**

    - *Sbagliato:* da $BA = O$ concludere che $B = O$ oppure $A = O$.
    - *Correzione:* nell'anello $(K^{n,n},+,\cdot)$ per $n \ge 2$ esistono *divisori dello zero*: come visto nell'Esempio 2.2.3, $BA = O$ con $A \neq O$ e $B \neq O$.

2. **Confondere la matrice identica $I$ con la matrice di tutti $1$**

    - *Sbagliato:* credere che l'elemento neutro del prodotto in $K^{2,2}$ sia $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$.
    - *Correzione:* moltiplicando per $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ sommi gli elementi sulle colonne! L'elemento neutro è invece $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, che ha $1$ sulla diagonale principale e $0$ altrove.

3. **Sottovalutare il lato di moltiplicazione in $(K^{n,n},+,\cdot)$**

    - *Sbagliato:* nella dimostrazione $BA = O \implies B = O$, moltiplicare a sinistra per $A^{-1}$ pensando che faccia $(A^{-1} B)A$.
    - *Correzione:* poiché il prodotto non è commutativo, per cancellare $A$ che sta a **destra** di $B$ bisogna moltiplicare entrambi i membri per $A^{-1}$ a **destra**.

### 6. Riepilogo

- Una matrice con lo stesso numero di righe e colonne ($m = n$) si chiama **quadrata** di ordine $n$.
- $(K^{n,n}, +, \cdot)$ è un **anello unitario** con elemento neutro moltiplicativo $I$ ($\operatorname{ent}_{ij}(I)=1$ se $i=j$, $0$ se $i\neq j$).
- Per $n \ge 2$ il prodotto in $K^{n,n}$ non è commutativo e valgono divisori dello zero ($BA = O$ con $A, B \neq O$).
- Per $n \ge 2$, $(K^{n,n}, +, \cdot)$ **non è un corpo**: esistono matrici non nulle prive di inversa.
- Caratterizzare esattamente quali matrici quadrate siano invertibili è l'obiettivo del Capitolo 3.

### 7. Esercizi

La Lezione 3 *(pp. 6–7)* non assegna esercizi per casa specifici su `2.3`. Come verifica rapida, controlla manualmente che $\begin{pmatrix} 2 & -5 \\ 1 & 4 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2 & -5 \\ 1 & 4 \end{pmatrix}$.

<!-- section: sec-2-4 | num: 2.4 | title: Matrice trasposta, matrici simmetriche e antisimmetriche | kind: section | part: cap-2 -->

### 1. Idea in parole semplici

Fare la **trasposta** ${}^t A$ di una matrice $A$ significa **scambiare le righe con le colonne**: la prima riga diventa la prima colonna, la seconda riga diventa la seconda colonna, e così via. Se $A$ ha $m$ righe e $n$ colonne, ${}^t A$ avrà $n$ righe e $m$ colonne.

Quando $A$ è quadrata ($n \times n$), ${}^t A$ ha ancora la stessa taglia di $A$, quindi possiamo confrontarle direttamente:
- se ribaltandola resta uguale ($A = {}^t A$), $A$ è **simmetrica** (gli elementi sopra e sotto la diagonale sono speculari);
- se ribaltandola cambiano tutti i segni ($A = -{}^t A$), $A$ è **antisimmetrica**.

### 2. Definizioni e enunciati precisi

:::def Definizione — Matrice trasposta (Lezione 3, p. 8)
Sia $A \in K^{m,n}$. Si chiama **trasposta** di $A$ la matrice ${}^t A \in K^{n,m}$ così definita:

$$\operatorname{ent}_{ij}({}^t A) \stackrel{\text{DEF}}{=} \operatorname{ent}_{ji}(A) \qquad \forall i \in \{1,\dots,n\},\ \forall j \in \{1,\dots,m\}$$

La trasposizione definisce quindi un'operazione $K^{m,n} \xrightarrow{\text{trasp}} K^{n,m}$.
:::

:::thm Proprietà della trasposizione (Lezione 3, p. 8)
Valgono le seguenti $3$ proprietà:
1. ${}^t(A + B) = {}^t A + {}^t B \qquad \forall A, B \in K^{m,n}$;
2. ${}^t(aM) = a\,{}^t M \qquad \forall a \in K,\ \forall M \in K^{m,n}$;
3. ${}^t(AB) = {}^t B\,{}^t A \qquad \forall A \in K^{m,n},\ \forall B \in K^{n,p}$ *(attenzione all'inversione dell'ordine!)*.
:::

:::def Definizione — Matrici simmetriche e antisimmetriche (Lezione 3, p. 8)
Sia $A \in K^{n,n}$ una matrice quadrata *(così anche ${}^t A \in K^{n,n}$)*.
- $A$ si dice **simmetrica** se $A = {}^t A$.
- $A$ si dice **antisimmetrica** se $A = -{}^t A$.
:::

### 3. Dimostrazioni

In questa sezione delle lezioni *(Lezione 3, pp. 7–8)* le proprietà della trasposizione vengono enunciate direttamente e applicate negli esempi senza svolgere dimostrazioni.

### 4. Esempi svolti

:::example Esempio 2.4.1 — Trasposta di una matrice rettangolare (Lezione 3, p. 7)
Sia $A = \begin{pmatrix} 1 & 2 & 3 \\ 3 & 4 & 5 \end{pmatrix} \in \mathbb{R}^{2,3}$. Trasformando le $2$ righe nelle $2$ colonne otteniamo:

$${}^t A = \begin{pmatrix} 1 & 3 \\ 2 & 4 \\ 3 & 5 \end{pmatrix} \in \mathbb{R}^{3,2}$$
:::

:::example Esempio 2.4.2 — Matrice simmetrica (Lezione 3, p. 8)
La matrice

$$A = \begin{pmatrix} 1 & 3 & 4 \\ 3 & 5 & -6 \\ 4 & -6 & 3 \end{pmatrix} \in \mathbb{R}^{3,3}$$

è **simmetrica**, perché calcolando ${}^t A$ si riottiene identicamente $A$: osserva come $\operatorname{ent}_{12}=\operatorname{ent}_{21}=3$, $\operatorname{ent}_{13}=\operatorname{ent}_{31}=4$ e $\operatorname{ent}_{23}=\operatorname{ent}_{32}=-6$, mentre i numeri sulla diagonale ($1, 5, 3$) restano al proprio posto.
:::

:::example Esempio 2.4.3 — Matrice antisimmetrica (Lezione 3, p. 8)
La matrice

$$A = \begin{pmatrix} 0 & 2 & -5 \\ -2 & 0 & 4 \\ 5 & -4 & 0 \end{pmatrix} \in \mathbb{R}^{3,3}$$

è **antisimmetrica**: infatti

$${}^t A = \begin{pmatrix} 0 & -2 & 5 \\ 2 & 0 & -4 \\ -5 & 4 & 0 \end{pmatrix} \implies -{}^t A = \begin{pmatrix} 0 & 2 & -5 \\ -2 & 0 & 4 \\ 5 & -4 & 0 \end{pmatrix} = A$$

Nota che in tutti e tre i posti sulla diagonale compare $0$, perché ogni elemento diagonale deve soddisfare $a_{ii} = -a_{ii}$.
:::

### 5. Errori comuni e trappole

1. **Dimenticare di invertire l'ordine in ${}^t(AB)$**

    - *Sbagliato:* scrivere ${}^t(AB) = {}^t A\,{}^t B$.
    - *Correzione:* **${}^t(AB) = {}^t B\,{}^t A$**. Puoi verificarlo anche dalle dimensioni: se $A \in K^{m,n}$ e $B \in K^{n,p}$, allora $AB \in K^{m,p}$, quindi ${}^t(AB) \in K^{p,m}$. Ora ${}^t B \in K^{p,n}$ e ${}^t A \in K^{n,m}$, perciò il prodotto ${}^t B\,{}^t A$ è compatibile e ha proprio dimensione $p \times m$ (mentre ${}^t A\,{}^t B$ in generale non esiste neppure!).

2. **Mettere numeri non nulli sulla diagonale di una matrice antisimmetrica reale**

    - *Sbagliato:* proporre $A = \begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix}$ come matrice antisimmetrica.
    - *Correzione:* se $A = -{}^t A$, sulla diagonale si ha $a_{ii} = -a_{ii} \implies 2a_{ii} = 0$, che in $\mathbb{R}, \mathbb{Q}, \mathbb{C}$ forza sempre $a_{ii} = 0$.

### 6. Riepilogo

- La trasposta ${}^t A \in K^{n,m}$ scambia righe e colonne: $\operatorname{ent}_{ij}({}^t A) = \operatorname{ent}_{ji}(A)$.
- La trasposizione è lineare rispetto a somma e scalari: ${}^t(A+B) = {}^t A + {}^t B$ e ${}^t(aM) = a\,{}^t M$.
- La trasposta di un prodotto inverte i fattori: ${}^t(AB) = {}^t B\,{}^t A$.
- $A \in K^{n,n}$ è **simmetrica** se $A = {}^t A$.
- $A \in K^{n,n}$ è **antisimmetrica** se $A = -{}^t A$ (su $\mathbb{R}$, $\mathbb{Q}$, $\mathbb{C}$ la diagonale è tutta nulla).

### 7. Esercizi

La Lezione 3 *(pp. 7–8)* non assegna esercizi per casa su questo sottoparagrafo; per esercizio rapido, verifica ${}^t(AB) = {}^t B\,{}^t A$ usando le matrici $A$ e $B$ dell'Esempio 2.2.3.

<!-- section: sec-2-5 | num: 2.5 | title: Matrici triangolari, diagonali, scalari e traccia | kind: section | part: cap-2 -->

### 1. Idea in parole semplici

In ogni matrice quadrata $A \in K^{n,n}$, gli elementi con indice di riga uguale a quello di colonna ($a_{11}, a_{22}, \dots, a_{nn}$) formano la **diagonale principale**. A seconda di quanti zeri compaiono attorno a questa diagonale, distinguiamo quattro tipi speciali di matrici, disposti come scatole cinesi una dentro l'altra:

- **Triangolare superiore / inferiore:** tutti zeri da un solo lato della diagonale.
- **Diagonale:** tutti zeri sia sopra che sotto la diagonale.
- **Scalare:** diagonale con lo *stesso* numero $h$ ripetuto su tutta la diagonale ($hI$).

Infine, la **traccia** $\operatorname{tr} A$ riduce l'intera matrice quadrata a un solo scalare: la **somma** degli elementi sulla diagonale principale. Ha una proprietà quasi magica: $\operatorname{tr}(AB) = \operatorname{tr}(BA)$, anche quando $AB \neq BA$!

### 2. Definizioni e enunciati precisi

:::def Definizione — Matrici triangolari, diagonali e scalari (Lezione 3, pp. 9–10)
Sia $A \in K^{n,n}$ una matrice quadrata.
1. $A$ si dice **triangolare superiore** se tutti gli elementi sotto la diagonale principale sono nulli:
    $$\operatorname{ent}_{ij}(A) = 0 \qquad \forall i > j$$
2. $A$ si dice **triangolare inferiore** se tutti gli elementi sopra la diagonale principale sono nulli:
    $$\operatorname{ent}_{ij}(A) = 0 \qquad \forall i < j$$
3. $A$ si dice **diagonale** se è **sia** triangolare superiore **che** triangolare inferiore *(ossia $\operatorname{ent}_{ij}(A) = 0$ per ogni $i \neq j$)*.
4. $A$ si dice **matrice scalare** se è un multiplo della matrice identica, ovvero:
    $$A = hI, \qquad h \in K$$
:::

**Gerarchia delle matrici quadrate speciali *(Lezione 3, p. 10)*:**

$$\text{Matrice scalare} \implies \text{Matrice diagonale} \implies \text{Triangolare superiore e triangolare inferiore}$$

:::note Nota sugli appunti originali (`Lez03`, p. 10)
Nello schema riassuntivo viola a p. 10 della Lezione 3 è scritto *"MATRICE DIAGONALE $\Rightarrow$ TRIANG. SUP. O TRIANG. INF."*. Come indicato correttamente nella definizione formale a p. 9, una matrice diagonale è **sia** triangolare superiore **che** triangolare inferiore (quindi la congiunzione corretta è *"e"*, non *"o"*).
:::

:::def Definizione — Traccia di una matrice quadrata (Lezione 3, p. 10)
Sia $A \in K^{n,n}$. Si chiama **traccia** di $A$ la somma degli elementi della diagonale principale:

$$\operatorname{tr} A \stackrel{\text{DEF}}{=} \sum_{r=1}^n \operatorname{ent}_{rr}(A)$$
:::

:::thm Proprietà della traccia (Lezione 3, p. 10)
Valgono le seguenti $3$ proprietà:
1. $\operatorname{tr}(A + B) = \operatorname{tr} A + \operatorname{tr} B \qquad \forall A, B \in K^{n,n}$;
2. $\operatorname{tr}(aM) = a\operatorname{tr}(M) \qquad \forall a \in K,\ \forall M \in K^{n,n}$;
3. $\operatorname{tr}(AB) = \operatorname{tr}(BA) \qquad \forall A, B \in K^{n,n}$.
:::

### 3. Dimostrazioni

In questa sezione della Lezione 3 *(pp. 9–11)* le definizioni e le proprietà della traccia vengono presentate senza dimostrazione e illustrate tramite esempi ed esercizio di verifica.

### 4. Esempi svolti

:::example Esempio 2.5.1 — Matrici triangolari superiori e inferiori (Lezione 3, p. 9)
1. **Triangolare superiore ($i > j \implies \text{entrata} = 0$):**
    $$A = \begin{pmatrix} 4 & 6 & -3 & 1 \\ 0 & 3 & 5 & 2 \\ 0 & 0 & 7 & 1 \\ 0 & 0 & 0 & 6 \end{pmatrix}$$
    Gli elementi sulla **diagonale principale** sono $4, 3, 7, 6$; al di sotto della diagonale compaiono solo zeri.

2. **Triangolare inferiore ($i < j \implies \text{entrata} = 0$):**
    $$A = \begin{pmatrix} 8 & 0 & 0 & 0 \\ 1 & 4 & 0 & 0 \\ 3 & 2 & 1 & 0 \\ 5 & 2 & 5 & 7 \end{pmatrix}$$
    Gli elementi sulla **diagonale principale** sono $8, 4, 1, 7$; al di sopra della diagonale compaiono solo zeri.
:::

:::example Esempio 2.5.2 — Matrice diagonale e matrice scalare (Lezione 3, pp. 9–10)
- **Matrice diagonale:**
    $$A = \begin{pmatrix} 5 & 0 & 0 & 0 \\ 0 & 3 & 0 & 0 \\ 0 & 0 & -2 & 0 \\ 0 & 0 & 0 & 5 \end{pmatrix}$$
    Tutti gli elementi fuori dalla diagonale principale ($5, 3, -2, 5$) sono nulli.

- **Matrice scalare:**
    $$A = \begin{pmatrix} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3 \end{pmatrix} = 3I = 3\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$
    Qui tutti gli elementi sulla diagonale sono uguali tra loro ($3$) e tutti gli altri sono $0$.
:::

:::example Esempio 2.5.3 — Calcolo della traccia (Lezione 3, p. 10)
Sia $A = \begin{pmatrix} 3 & 5 & 2 \\ 4 & -2 & 6 \\ 2 & 1 & 1 \end{pmatrix}$. Sommando i soli elementi sulla diagonale principale ($3, -2, 1$) si ottiene:

$$\operatorname{tr} A = 3 + (-2) + 1 = 2$$
:::

### 5. Errori comuni e trappole

1. **Confondere triangolare superiore e triangolare inferiore**

    - *Sbagliato:* pensare che una matrice triangolare superiore abbia gli zeri *sopra* la diagonale.
    - *Correzione:* il nome indica **dove possono trovarsi i numeri non nulli**! Nella triangolare **superiore**, la parte non nulla forma un triangolo nella metà *superiore* (quindi gli zeri stanno sotto: $\operatorname{ent}_{ij}=0$ per $i>j$).

2. **Credere che la traccia sia moltiplicativa: $\operatorname{tr}(AB) = (\operatorname{tr} A)(\operatorname{tr} B)$**

    - *Sbagliato:* calcolare $\operatorname{tr}(AB)$ moltiplicando $\operatorname{tr} A$ per $\operatorname{tr} B$.
    - *Correzione:* falso! Ad esempio con $A = I_2$ e $B = I_2$, $\operatorname{tr}(I_2) = 2$, quindi $(\operatorname{tr} I_2)(\operatorname{tr} I_2) = 4$, mentre $\operatorname{tr}(I_2 \cdot I_2) = \operatorname{tr}(I_2) = 2$. La proprietà corretta è **$\operatorname{tr}(AB) = \operatorname{tr}(BA)$**.

### 6. Riepilogo

- In $A \in K^{n,n}$ gli elementi $\operatorname{ent}_{rr}(A)$ costituiscono la **diagonale principale**.
- **Triangolare superiore:** zeri sotto la diagonale ($i > j$); **triangolare inferiore:** zeri sopra ($i < j$).
- **Diagonale:** zeri ovunque fuori dalla diagonale; **scalare:** $A = hI$ ($h \in K$).
- La **traccia** $\operatorname{tr} A = \sum_{r=1}^n \operatorname{ent}_{rr}(A)$ somma gli elementi della diagonale principale.
- La traccia è lineare ($\operatorname{tr}(A+B) = \operatorname{tr} A + \operatorname{tr} B$, $\operatorname{tr}(aM)=a\operatorname{tr} M$) e ciclica ($\operatorname{tr}(AB) = \operatorname{tr}(BA)$).

### 7. Esercizi

:::exercise Esercizio 2.5.1 (Esercizio per casa — Facile · Lezione 3, p. 11)
Siano:

$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \qquad B = \begin{pmatrix} 5 & 1 \\ 2 & 3 \end{pmatrix}$$

Verificare che $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.

:::solution Soluzione spiegata passo-passo
**Ragionamento:** calcoliamo esplicitamente entrambi i prodotti riga per colonna $AB$ e $BA$, poi sommiamo le rispettive diagonali principali per confrontare le due tracce.

1. **Calcoliamo $AB$ e la sua traccia:**
    $$AB = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 5 & 1 \\ 2 & 3 \end{pmatrix} = \begin{pmatrix} 1\cdot 5 + 2\cdot 2 & 1\cdot 1 + 2\cdot 3 \\ 3\cdot 5 + 4\cdot 2 & 3\cdot 1 + 4\cdot 3 \end{pmatrix} = \begin{pmatrix} 9 & 7 \\ 23 & 15 \end{pmatrix}$$
    Quindi:
    $$\operatorname{tr}(AB) = 9 + 15 = 24$$

2. **Calcoliamo $BA$ e la sua traccia:**
    $$BA = \begin{pmatrix} 5 & 1 \\ 2 & 3 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 5\cdot 1 + 1\cdot 3 & 5\cdot 2 + 1\cdot 4 \\ 2\cdot 1 + 3\cdot 3 & 2\cdot 2 + 3\cdot 4 \end{pmatrix} = \begin{pmatrix} 8 & 14 \\ 11 & 16 \end{pmatrix}$$
    Quindi:
    $$\operatorname{tr}(BA) = 8 + 16 = 24$$

3. **Conclusione:** pur essendo $AB \neq BA$, si verifica $\operatorname{tr}(AB) = 24 = \operatorname{tr}(BA)$.
:::
:::
