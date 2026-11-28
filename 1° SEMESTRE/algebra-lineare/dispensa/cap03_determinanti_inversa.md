<!-- part: cap-3 | num: 3 | label: CAPITOLO 3 | title: Determinanti e matrice inversa | refs: Fonti: Lezione 4 (14/10/2026, pp. 1–6) e Lezione 5 (19/10/2026, pp. 1–6) -->

<!-- section: sec-3-1 | num: 3.1 | title: Permutazioni, segno, prodotto dedotto e definizione di determinante | kind: section | part: cap-3 -->

### 1. Idea in parole semplici

Nel Capitolo 2 abbiamo visto che non tutte le matrici quadrate non nulle sono invertibili, e abbiamo lasciato aperta la domanda chiave: *esiste un numero calcolabile direttamente da una matrice quadrata $M$ che ci dica subito se $M$ è invertibile oppure no?*

Questo numero esiste e si chiama **determinante** di $M$ ($\det M$). Per costruirlo da zero in modo rigoroso per qualsiasi dimensione $n \times n$, il docente parte da un'idea combinatoria elegante: scegliere un elemento da **ogni riga** e da **ogni colonna**, senza mai prendere due elementi sulla stessa riga o sulla stessa colonna. Ogni scelta possibile corrisponde a un rimescolamento — una **permutazione** $\sigma$ dei numeri $\{1, \dots, n\}$ —, moltiplichiamo gli $n$ numeri scelti (il **prodotto dedotto** $p_\sigma$), gli diamo un segno $+$ o $-$ a seconda che lo scambio sia *pari* o *dispari*, e sommiamo tutti gli $n!$ termini così ottenuti.

### 2. Definizioni e enunciati precisi

:::def Definizione — Permutazione e insieme $S_n$ (Lezione 4, p. 1)
Sia $A$ un insieme. Si chiama **permutazione** su $A$ una funzione biettiva $\sigma : A \to A$.

Quando $A = \{1, \dots, n\}$ con $n \in \mathbb{Z}$, $n > 0$, indichiamo con $S_n$ l'insieme di tutte le permutazioni su $A$. Se $A$ è finito, $|A|$ denota la cardinalità (numero di elementi) di $A$.
:::

:::thm Osservazione — Cardinalità di $S_n$ e fattoriale (Lezione 4, p. 1)
Se $A = \{1, \dots, n\}$, allora $|A| = n$ e il numero totale di permutazioni è **$n$ fattoriale**:

$$|S_n| = n! = 1 \cdot 2 \cdot \dots \cdot n$$

Ad esempio: $1! = 1$, $2! = 1 \cdot 2 = 2$, $3! = 1 \cdot 2 \cdot 3 = 6$, $4! = 1 \cdot 2 \cdot 3 \cdot 4 = 24$.
:::

:::def Definizione — Classe (pari/dispari) e segno di una permutazione (Lezione 4, p. 2)
Sia $\sigma \in S_n$.
- Diremo che $\sigma$ è di **classe pari** se con un numero **pari** di scambi è possibile trasformarla nella permutazione identità $\operatorname{id}_A = (1, 2, \dots, n)$; altrimenti $\sigma$ si dice di **classe dispari**.
- Si chiama **segno** di $\sigma$ la funzione:

$$\operatorname{sgn}(\sigma) \stackrel{\text{DEF}}{=} \begin{cases} 1 & \text{se } \sigma \text{ è di classe pari} \\ -1 & \text{se } \sigma \text{ è di classe dispari} \end{cases}$$
:::

:::def Definizione — Prodotto dedotto e determinante di $M \in K^{n,n}$ (Lezione 4, p. 2)
Sia $M \in K^{n,n}$ una matrice quadrata, e poniamo per brevità $m_{ij} \stackrel{\text{DEF}}{=} \operatorname{ent}_{ij}(M)$.
- Per ogni $\sigma \in S_n$, si chiama **prodotto dedotto** associato a $\sigma$ lo scalare:

$$p_\sigma \stackrel{\text{DEF}}{=} m_{1\sigma(1)} m_{2\sigma(2)} \cdots m_{n\sigma(n)}$$

- Si chiama **determinante** di $M$ lo scalare:

$$\det M \stackrel{\text{DEF}}{=} \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\, p_\sigma$$
:::

:::note Nota sugli appunti originali (`Lez04`, pp. 2–3 — righe invisibili nell'esportazione PDF)
Nel PDF esportato della Lezione 4, alcune brevi formule risultano scomparse/bianche al fondo di p. 2 e in cima a p. 3:
1. a p. 2, subito dopo $\det M \stackrel{\text{DEF}}{=}$, manca la somma esplicita $\sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\, p_\sigma$;
2. in fondo a p. 2, davanti a `; det M = m_{11}`, manca l'intestazione del caso base $n = 1,\ M = (m_{11}) \in K^{1,1}$;
3. in cima a p. 3, sopra il primo esempio $2\times 2$, manca la formula generale per $n = 2$: $\det \begin{pmatrix} m_{11} & m_{12} \\ m_{21} & m_{22} \end{pmatrix} = m_{11}m_{22} - m_{12}m_{21}$.

Tutte e tre le formule sono qui ricostruite fedelmente in base agli esempi subito adiacenti e al caso $n=3$ di p. 3.
:::

### 3. Dimostrazioni

In questa prima parte della Lezione 4 *(pp. 1–2)* vengono poste le definizioni combinatorie preliminari senza dimostrazioni (le prime dimostrazioni sulle proprietà del determinante seguono nella sezione [3.2](#sec-3-2)).

### 4. Esempi svolti

:::example Esempio 3.1.1 — Tutte le permutazioni di $S_3$ e i loro segni (Lezione 4, pp. 1–2)
Per $n = 3$, $A = \{1,2,3\}$ e $|S_3| = 3! = 6$. Scrivendo ciascuna biiezione $\sigma$ come terna $(\sigma(1), \sigma(2), \sigma(3))$:
- $\operatorname{id}_A = (1, 2, 3)$ *(0 scambi $\implies$ pari, $\operatorname{sgn} = +1$)*;
- $(1, 3, 2)$ *(1 scambio tra $2$ e $3$ $\implies$ dispari, $\operatorname{sgn} = -1$)*;
- $(3, 2, 1)$ *(1 scambio tra $1$ e $3$ $\implies$ dispari, $\operatorname{sgn} = -1$)*;
- $(2, 1, 3)$ *(1 scambio tra $1$ e $2$ $\implies$ dispari, $\operatorname{sgn} = -1$)*;
- $(2, 3, 1)$ *(2 scambi: $(2,3,1)\to(1,3,2)\to(1,2,3)$ $\implies$ pari, $\operatorname{sgn} = +1$)*;
- $(3, 1, 2)$ *(2 scambi: $(3,1,2)\to(1,3,2)\to(1,2,3)$ $\implies$ pari, $\operatorname{sgn} = +1$)*.

In sintesi:
$$S_3 = \{\underset{+}{(1,2,3)},\ \underset{-}{(1,3,2)},\ \underset{-}{(3,2,1)},\ \underset{-}{(2,1,3)},\ \underset{+}{(2,3,1)},\ \underset{+}{(3,1,2)}\}$$
:::

:::example Esempio 3.1.2 — Classe pari di una permutazione in $S_6$ (Lezione 4, p. 1)
Sia $\sigma = (6, 4, 1, 5, 2, 3) \in S_6$. Portiamo gli elementi al loro posto mediante scambi successivi:
1. scambio $6 \leftrightarrow 1$: $(6,4,1,5,2,3) \to (1,4,6,5,2,3)$;
2. scambio $4 \leftrightarrow 2$: $(1,4,6,5,2,3) \to (1,2,6,5,4,3)$;
3. scambio $6 \leftrightarrow 3$: $(1,2,6,5,4,3) \to (1,2,3,5,4,6)$;
4. scambio $5 \leftrightarrow 4$: $(1,2,3,5,4,6) \to (1,2,3,4,5,6)$.

Poiché abbiamo ottenuto l'identità con $4$ scambi (numero pari), $\sigma$ è di **classe pari** ($\operatorname{sgn}(\sigma) = 1$).
:::

:::example Esempio 3.1.3 — Calcolo di un prodotto dedotto $p_\sigma$ in $K^{6,6}$ (Lezione 4, p. 2)
Sia $M \in K^{6,6}$ e consideriamo la permutazione $\sigma = (5, 1, 3, 4, 2, 6) \in S_6$, cioè $\sigma(1)=5, \sigma(2)=1, \sigma(3)=3, \sigma(4)=4, \sigma(5)=2, \sigma(6)=6$. Il prodotto dedotto associato è:

$$p_\sigma = m_{15} m_{21} m_{33} m_{44} m_{52} m_{66}$$
:::

### 5. Errori comuni e trappole

1. **Dimenticare che il determinante è definito solo per matrici quadrate**
    - *Sbagliato:* cercare di calcolare $\det A$ per una matrice rettangolare $A \in \mathbb{R}^{2,3}$.
    - *Correzione:* nella definizione *(Lezione 4, p. 2)* è richiesto $M \in K^{n,n}$. Una matrice non quadrata ha eventualmente **minori** (determinanti di sue sottomatrici quadrate, Cap. 4), ma non ha un determinante globale.

2. **Sbagliare gli indici nel prodotto dedotto $p_\sigma$**
    - *Sbagliato:* scrivere $m_{\sigma(1)1} m_{\sigma(2)2}\cdots$ oppure ripetere la stessa colonna due volte.
    - *Correzione:* per definizione *(Lezione 4, p. 2)* la riga avanza sempre ordinata da $1$ a $n$ e la colonna è $\sigma(i)$: $p_\sigma = m_{1\sigma(1)} m_{2\sigma(2)} \cdots m_{n\sigma(n)}$. Essendo $\sigma$ biettiva, compaiono tutte le $n$ righe e tutte le $n$ colonne una sola volta.

3. **Pensare che conti la scelta specifica degli scambi**
    - *Sbagliato:* temere che un modo diverso di riordinare $\sigma$ in $(1,\dots,n)$ cambi la sua classe da pari a dispari.
    - *Correzione:* `[INTEGRAZIONE NON DALLE LEZIONI]` pur potendo usare più scambi, la **parità** (pari vs dispari) del numero di scambi necessari per raggiungere l'identità è un invariante univoco di $\sigma$.

### 6. Riepilogo

- Una **permutazione** su $\{1,\dots,n\}$ è una funzione biettiva su $\{1,\dots,n\}$; il loro insieme $S_n$ ha $|S_n| = n!$ elementi.
- $\sigma \in S_n$ ha segno $\operatorname{sgn}(\sigma) = 1$ se trasformabile nell'identità con un numero **pari** di scambi, $-1$ se **dispari**.
- Il **prodotto dedotto** di $\sigma$ in $M \in K^{n,n}$ è $p_\sigma = m_{1\sigma(1)} m_{2\sigma(2)} \cdots m_{n\sigma(n)}$.
- Il **determinante** è la somma pesata col segno su tutte le permutazioni: $\det M = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\, p_\sigma$.
- In $S_3$ sono pari $(1,2,3), (2,3,1), (3,1,2)$ e dispari $(1,3,2), (3,2,1), (2,1,3)$.

### 7. Esercizi

Questa sezione introduce le definizioni preliminari alla formula del determinante; gli esercizi operativi di calcolo della Lezione 4 (incluso l'*Esercizio per casa* su $S_4$) sono raccolti nella sezione successiva [3.2](#sec-3-2).

<!-- section: sec-3-2 | num: 3.2 | title: Calcolo del determinante per n = 1, 2, 3 e proprietà sulle colonne | kind: section | part: cap-3 -->

### 1. Idea in parole semplici

Usare la definizione combinatoria con tutti gli $n!$ termini diventa subito scomodo al crescere di $n$ (per $n=4$ sono $24$ prodotti, per $n=5$ sono già $120$!). Per i casi piccoli ($n=1,2,3$) conviene imparare a colpo d'occhio le formule dirette; per i casi grandi servono invece delle **regole di semplificazione** sulle colonne.

Queste regole dicono essenzialmente due cose: primo, il determinante si comporta in modo lineare colonna per colonna (**multilinearità**) e si annulla se due colonne sono uguali o proporzionali (**alternanza**); secondo, aggiungere a una colonna un multiplo di un'altra **non cambia il determinante**, così possiamo fabbricare tanti zeri nella matrice prima di calcolarlo!

### 2. Definizioni e enunciati precisi

#### Formule esplicite per $n = 1, 2, 3$ *(Lezione 4, pp. 2–3)*

- **$n = 1$:** se $M = (m_{11}) \in K^{1,1}$, allora $\det M = m_{11}$.
- **$n = 2$:** se $M = \begin{pmatrix} m_{11} & m_{12} \\ m_{21} & m_{22} \end{pmatrix} \in K^{2,2}$, allora:
  $$\det M = m_{11}m_{22} - m_{12}m_{21}$$
- **$n = 3$:** se $M = \begin{pmatrix} m_{11} & m_{12} & m_{13} \\ m_{21} & m_{22} & m_{23} \\ m_{31} & m_{32} & m_{33} \end{pmatrix} \in K^{3,3}$, sviluppando $\sum_{\sigma \in S_3} \operatorname{sgn}(\sigma)p_\sigma$:
  $$\det M = p_{(1,2,3)} + p_{(2,3,1)} + p_{(3,1,2)} - p_{(1,3,2)} - p_{(3,2,1)} - p_{(2,1,3)}$$
  $$= m_{11}m_{22}m_{33} + m_{12}m_{23}m_{31} + m_{13}m_{21}m_{32} - m_{11}m_{23}m_{32} - m_{13}m_{22}m_{31} - m_{12}m_{21}m_{33}$$

:::def Definizione — Combinazione lineare di matrici (Lezione 4, p. 4)
Sia $(K, +, \cdot)$ un campo, siano $a, b \in K$ e $M, N \in K^{m,n}$. La matrice $aM + bN \in K^{m,n}$ si chiama **combinazione lineare** delle matrici $M$ ed $N$.
:::

Indichiamo le colonne di $M \in K^{n,n}$ scrivendo $M = (C_1\ C_2\ \dots\ C_n)$, dove ogni $C_i \in K^{n,1}$.

:::thm Proprietà fondamentali dei determinanti rispetto alle colonne (Lezione 4, pp. 4–6)
1. **Proprietà di multilinearità:** se nella posizione $i$-esima sostituiamo la colonna con una combinazione lineare $aD + bE$ ($a, b \in K$, $D, E \in K^{n,1}$), allora:
    $$\det(C_1\ \dots\ C_{i-1}\ (aD + bE)\ C_{i+1}\ \dots\ C_n) = a\det(C_1\ \dots\ C_{i-1}\ D\ C_{i+1}\ \dots\ C_n) + b\det(C_1\ \dots\ C_{i-1}\ E\ C_{i+1}\ \dots\ C_n)$$
2. **Proprietà di alternanza:** il determinante di una matrice con **due colonne uguali** è nullo ($\det M = 0$).
3. **Determinante dell'identità:** $\det I = 1$, dove $I \in K^{n,n}$ è la matrice identica.
4. **Proprietà 1 (dipendenza lineare):** se in una matrice una colonna è combinazione lineare di altre due colonne, il determinante è nullo.
5. **Proprietà 2 (scambio di colonne):** se scambiamo di posto due colonne, il determinante cambia segno.
6. **Proprietà 3 (operazione elementare di tipo III):** se in una matrice sostituiamo una colonna con la stessa colonna sommata ad un multiplo di un'altra colonna ($C_i \mapsto C_i + k C_j$ con $j \neq i$), il determinante **non cambia**.
:::

:::note Nota pratica sugli appunti originali (`Lez04`, p. 6 vs proprietà trasposta)
Le proprietà viste a lezione sulle colonne valgono analogamente anche sulle **righe** *(come il prof userà presto nel Teorema di Laplace in Lezione 5 e nel metodo di riduzione di Gauss in Lezione 6)*. Inoltre `[INTEGRAZIONE NON DALLE LEZIONI]` la regola mnemonica dei colori per $n=3$ usata dal prof a p. 3 equivale esattamente alla **regola di Sarrus**.
:::

### 3. Dimostrazioni

:::proof Dimostrazione 1 — Determinante della matrice identica: $\det I = 1$ (Lezione 4, p. 5)
**Idea di fondo:** nella matrice identica $I$, su ogni riga c'è esattamente un solo $1$ (sulla diagonale, cioè alla colonna $i$) e tutti gli altri elementi sono $0$. Quindi qualunque permutazione diversa dall'identità pesca almeno uno zero e annulla il suo prodotto dedotto.

Nella definizione $\det I = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\, \operatorname{ent}_{1\sigma(1)}(I)\cdots\operatorname{ent}_{n\sigma(n)}(I)$, per ottenere un prodotto diverso da zero dobbiamo avere $\operatorname{ent}_{i\sigma(i)}(I) \neq 0$ per ogni $i \in \{1,\dots,n\}$, il che accade se e solo se $\sigma(i) = i$ per ogni $i$, cioè $\sigma = \operatorname{id}$. L'unico prodotto dedotto non nullo è quindi $p_{\operatorname{id}} = 1 \cdot 1 \cdots 1 = 1$, associato alla permutazione identità che ha $\operatorname{sgn}(\operatorname{id}) = 1$. Pertanto $\det I = 1$.
:::

:::proof Dimostrazione 2 — Proprietà 1: colonna combinazione lineare di altre due $\implies \det M = 0$ (Lezione 4, p. 5)
**Idea di fondo:** spezziamo il determinante tramite la **multilinearità** in due determinanti ciascuno con due colonne uguali, che poi spariscono grazie all'**alternanza**.

Sia $M = (C_1\ \dots\ C_n)$ e supponiamo che la colonna $i$-esima sia combinazione lineare di due altre colonne $C_h$ e $C_k$ ($h \neq i$, $k \neq i$): $C_i = aC_h + bC_k$. Applicando la multilinearità rispetto alla colonna $i$-esima:

$$\det(C_1\ \dots\ aC_h + bC_k\ \dots\ C_n) = a\underbrace{\det(C_1\ \dots\ C_h\ \dots\ C_n)}_{= 0 \text{ (perché } C_h \text{ è ripetuta)}} + b\underbrace{\det(C_1\ \dots\ C_k\ \dots\ C_n)}_{= 0 \text{ (perché } C_k \text{ è ripetuta)}} = 0$$

Per la proprietà di alternanza entrambi i termini si annullano, quindi $\det M = 0$.
:::

:::proof Dimostrazione 3 — Proprietà 2: scambio di due colonne cambia il segno (Lezione 4, p. 6)
**Idea di fondo:** costruiamo ad arte una matrice con **due colonne identiche** uguali alla somma $D + E$ delle colonne da scambiare. Per alternanza il suo determinante è $0$; sviluppandolo per multilinearità restano solo i due determinanti con $D$ ed $E$ scambiate!

Consideriamo la matrice $(C_1\ \dots\ D+E\ \dots\ D+E\ \dots\ C_n)$ in cui la somma $D + E$ compare in entrambe le posizioni. Per alternanza il suo determinante è zero. Applicando la multilinearità prima sulla prima occorrenza di $D + E$ e poi sulla seconda:

$$0 = \det(C_1\ \dots\ D+E\ \dots\ D+E\ \dots\ C_n)$$
$$= \det(C_1\ \dots\ D\ \dots\ D+E\ \dots\ C_n) + \det(C_1\ \dots\ E\ \dots\ D+E\ \dots\ C_n)$$
$$= \underbrace{\det(C_1\ \dots\ D\ \dots\ D\ \dots\ C_n)}_{=0} + \det(C_1\ \dots\ D\ \dots\ E\ \dots\ C_n) + \det(C_1\ \dots\ E\ \dots\ D\ \dots\ C_n) + \underbrace{\det(C_1\ \dots\ E\ \dots\ E\ \dots\ C_n)}_{=0}$$

Restano solo i due termini centrali, dunque:
$$\det(C_1\ \dots\ D\ \dots\ E\ \dots\ C_n) = -\det(C_1\ \dots\ E\ \dots\ D\ \dots\ C_n)$$
:::

:::note Nota sulle dimostrazioni delle lezioni (`Lez04`, p. 6)
Per la **Proprietà 3** ($C_i \mapsto C_i + k C_j$), la dimostrazione segue immediatamente dalle proprietà appena provate *(scrivendo $\det(\dots, C_i + k C_j, \dots) = \det(\dots, C_i, \dots) + k\det(\dots, C_j, \dots)$ in cui il secondo determinante è $0$ per alternanza avendo due volte $C_j$)* `[INTEGRAZIONE NON DALLE LEZIONI]`, mentre a p. 6 il docente illustra la proprietà direttamente mediante un esempio numerico.
:::

### 4. Esempi svolti

:::example Esempio 3.2.1 — Determinanti $2\times 2$ e $3\times 3$ (Lezione 4, p. 3)
1. **Caso $2\times 2$:** per $M = \begin{pmatrix} 2 & 3 \\ 5 & -1 \end{pmatrix}$ si ha $\det M = 2\cdot(-1) - 3\cdot 5 = -2 - 15 = -17$.
2. **Caso $3\times 3$ (a):** per $M = \begin{pmatrix} 2 & 1 & -1 \\ 1 & 3 & 1 \\ -1 & 1 & -2 \end{pmatrix} \in \mathbb{R}^{3,3}$:
    - termini con segno $+$: $2\cdot 3\cdot(-2) + 1\cdot 1\cdot(-1) + (-1)\cdot 1\cdot 1 = -12 - 1 - 1$;
    - termini con segno $-$: $-((-1)\cdot 3\cdot(-1)) - (1\cdot 1\cdot(-2)) - (1\cdot 1\cdot 2) = -3 + 2 - 2$.
    Sommando: $\det M = -12 - 1 - 1 - 3 + 2 - 2 = -17$.
3. **Caso $3\times 3$ (b):** per $M = \begin{pmatrix} 2 & 1 & 3 \\ 1 & 5 & 6 \\ 1 & 2 & 3 \end{pmatrix}$:
    $$\det M = 2\cdot 5\cdot 3 + 1\cdot 6\cdot 1 + 3\cdot 1\cdot 2 - 3\cdot 5\cdot 1 - 6\cdot 2\cdot 2 - 1\cdot 1\cdot 3 = 30 + 6 + 6 - 15 - 24 - 3 = 0$$
:::

:::example Esempio 3.2.2 — Combinazione lineare di matrici e multilinearità (Lezione 4, p. 4)
1. **Combinazione lineare di matrici:** con $a = 2, b = 3$ e $M = \begin{pmatrix} 1 & 2 \\ 0 & 1 \\ 3 & 1 \end{pmatrix}$, $N = \begin{pmatrix} 5 & 1 \\ -2 & 3 \\ 1 & 4 \end{pmatrix}$:
    $$aM + bN = 2\begin{pmatrix} 1 & 2 \\ 0 & 1 \\ 3 & 1 \end{pmatrix} + 3\begin{pmatrix} 5 & 1 \\ -2 & 3 \\ 1 & 4 \end{pmatrix} = \begin{pmatrix} 2 & 4 \\ 0 & 2 \\ 6 & 2 \end{pmatrix} + \begin{pmatrix} 15 & 3 \\ -6 & 9 \\ 3 & 12 \end{pmatrix} = \begin{pmatrix} 17 & 7 \\ -6 & 11 \\ 9 & 14 \end{pmatrix} = P$$
    Quindi $P$ è combinazione lineare di $M$ ed $N$.
2. **Multilinearità:** presa $M = \begin{pmatrix} 1 & 16 \\ -1 & 9 \end{pmatrix} \in \mathbb{R}^{2,2}$, osserviamo che la seconda colonna è $2\begin{pmatrix} 2 \\ 3 \end{pmatrix} + 3\begin{pmatrix} 4 \\ 1 \end{pmatrix}$:
    - calcolo diretto: $\det M = 9 + 16 = 25$;
    - per multilinearità: $\det M = 2\det\begin{pmatrix} 1 & 2 \\ -1 & 3 \end{pmatrix} + 3\det\begin{pmatrix} 1 & 4 \\ -1 & 1 \end{pmatrix} = 2(3+2) + 3(1+4) = 2\cdot 5 + 3\cdot 5 = 10 + 15 = 25$.
:::

:::example Esempio 3.2.3 — Applicazioni delle Proprietà di alternanza, 1 e 3 (Lezione 4, pp. 5–6)
1. **Colonne uguali (p. 5):** $M = \begin{pmatrix} 3 & 1 & 3 \\ 5 & 4 & 5 \\ 8 & 9 & 8 \end{pmatrix}$ ha $C_1 = C_3 \implies \det M = 0$ *(controllo diretto: $3\cdot 4\cdot 8 + 5\cdot 9\cdot 3 + 5\cdot 1\cdot 8 - 8\cdot 4\cdot 3 - 5\cdot 9\cdot 3 - 5\cdot 1\cdot 8 = 0$)*.
2. **Esercizio svolto in classe su alternanza (p. 5):** in $M = \begin{pmatrix} 2 & 1 & 3 \\ 1 & 5 & 6 \\ 1 & 2 & 3 \end{pmatrix}$ vale $C_3 = C_1 + C_2$, quindi:
    $$\det(C_1\ C_2\ C_1 + C_2) = \det(C_1\ C_2\ C_1) + \det(C_1\ C_2\ C_2) = 0 + 0 = 0$$
3. **Colonna combinazione lineare di altre due (pp. 5–6):** in $M = \begin{pmatrix} 1 & 2 & -4 \\ 3 & 1 & 3 \\ 1 & 4 & -10 \end{pmatrix}$ la terza colonna è $2\begin{pmatrix} 1 \\ 3 \\ 1 \end{pmatrix} - 3\begin{pmatrix} 2 \\ 1 \\ 4 \end{pmatrix} = \begin{pmatrix} -4 \\ 3 \\ -10 \end{pmatrix}$, dunque $\det M = 0$.
4. **Semplificazione senza alterare il determinante (p. 6):** partendo da $M = \begin{pmatrix} 1 & 2 & 1 \\ 3 & 1 & 2 \\ 5 & 1 & 2 \end{pmatrix}$ ed eseguendo l'operazione $C_3 \mapsto C_3 - C_1$, si ottiene $C_3 - C_1 = \begin{pmatrix} 0 \\ -1 \\ -3 \end{pmatrix}$, quindi $M' = \begin{pmatrix} 1 & 2 & 0 \\ 3 & 1 & -1 \\ 5 & 1 & -3 \end{pmatrix}$ ha esattamente $\det M = \det M'$.
:::

### 5. Errori comuni e trappole

1. **Estrarre lo scalare da tutta la matrice invece che da una sola colonna (confondere $\det(kA)$ con $k\det A$)**
    - *Sbagliato:* scrivere $\det(kA) = k\det A$ per una matrice $n \times n$.
    - *Correzione:* il determinante è lineare **in ciascuna colonna separatamente** (multilinearità). Se moltiplichi *tutte e $n$ le colonne* per $k$, ogni colonna contribuisce un fattore $k$: per $n \times n$ si ha $\det(kA) = k^n \det A$!
2. **Applicare la regola dei "segni incrociati" $3\times 3$ alle matrici $4\times 4$**
    - *Sbagliato:* calcolare un determinante $4\times 4$ prendendo solo le 4 diagonali discendenti e le 4 ascendenti ($8$ termini).
    - *Correzione:* la regola rapida a 6 termini vale **solo per $n=3$** (perché $3! = 6 = 3+3$). Già per $n=4$ esistono $4! = 24$ termini distinti, e non si possono ottenere con semplici diagonali! Per $n \ge 4$ si usano i **teoremi di Laplace** (Sezione [3.3](#sec-3-3)) o la **riduzione**.
3. **Confondere la sostituzione $C_i \mapsto C_i + k C_j$ con $C_i \mapsto 2C_i + k C_j$**
    - *Sbagliato:* sostituire $C_3$ con $2C_3 - C_1$ pensando che il determinante resti invariato.
    - *Correzione:* il coefficiente davanti alla colonna modificata $C_i$ deve essere **$1$** ($C_i \mapsto C_i + k C_j$, $j\neq i$). Se moltiplichi $C_3$ per $2$, raddoppi anche il determinante.

### 6. Riepilogo

- Formule rapide: $n=1 \implies \det(m_{11})=m_{11}$; $n=2 \implies m_{11}m_{22}-m_{12}m_{21}$; $n=3 \implies$ somma dei 6 prodotti dedotti con i segni di $S_3$.
- **Multilinearità:** il determinante è lineare rispetto a ciascuna colonna singolarmente presa; **Alternanza:** due colonne uguali danno $\det = 0$.
- $\det I = 1$; se una colonna è combinazione lineare di altre due, $\det M = 0$.
- Scambiando due colonne il determinante **cambia segno**.
- Sostituendo $C_i \mapsto C_i + k C_j$ ($j \neq i$) il determinante **non cambia**.

### 7. Esercizi

:::exercise Esercizio 3.2.1 (Esercizio per casa — Medio · Lezione 4, p. 3)
Sia $n = 4$ e sia $M = (m_{ij}) \in K^{4,4}$ ($|S_4| = 24$). Scrivere la formula esplicita di $\det M$.

:::solution Soluzione spiegata passo-passo
**Ragionamento:** per la definizione $\det M = \sum_{\sigma \in S_4} \operatorname{sgn}(\sigma)\, m_{1\sigma(1)} m_{2\sigma(2)} m_{3\sigma(3)} m_{4\sigma(4)}$, dobbiamo elencare tutte le $4! = 24$ permutazioni $\sigma \in S_4$, determinarne la parità (contando gli scambi necessari a tornare a $(1,2,3,4)$) e sommare i corrispondenti $24$ prodotti dedotti ($12$ con segno $+$ e $12$ con segno $-$).

**1. Le $12$ permutazioni di classe pari ($\operatorname{sgn}(\sigma) = +1$):**
- $(1,2,3,4)$ *(0 scambi)*, $(1,3,4,2)$ *(2 scambi)*, $(1,4,2,3)$ *(2 scambi)*,
- $(2,1,4,3)$ *(2 scambi)*, $(2,3,1,4)$ *(2 scambi)*, $(2,4,3,1)$ *(2 scambi)*,
- $(3,1,2,4)$ *(2 scambi)*, $(3,2,4,1)$ *(2 scambi)*, $(3,4,1,2)$ *(2 scambi)*,
- $(4,1,3,2)$ *(2 scambi)*, $(4,2,1,3)$ *(2 scambi)*, $(4,3,2,1)$ *(2 scambi)*.

**2. Le $12$ permutazioni di classe dispari ($\operatorname{sgn}(\sigma) = -1$):**
- $(1,2,4,3)$ *(1 scambio)*, $(1,3,2,4)$ *(1 scambio)*, $(1,4,3,2)$ *(1 scambio)*,
- $(2,1,3,4)$ *(1 scambio)*, $(2,3,4,1)$ *(3 scambi)*, $(2,4,1,3)$ *(3 scambi)*,
- $(3,1,4,2)$ *(3 scambi)*, $(3,2,1,4)$ *(1 scambio)*, $(3,4,2,1)$ *(3 scambi)*,
- $(4,1,2,3)$ *(3 scambi)*, $(4,2,3,1)$ *(1 scambio)*, $(4,3,1,2)$ *(3 scambi)*.

**3. Formula esplicita completa di $\det M$ (tutti i $24$ termini):**
$$\begin{aligned}
\det M =\; & m_{11}m_{22}m_{33}m_{44} + m_{11}m_{23}m_{34}m_{42} + m_{11}m_{24}m_{32}m_{43} \\
& + m_{12}m_{21}m_{34}m_{43} + m_{12}m_{23}m_{31}m_{44} + m_{12}m_{24}m_{33}m_{41} \\
& + m_{13}m_{21}m_{32}m_{44} + m_{13}m_{22}m_{34}m_{41} + m_{13}m_{24}m_{31}m_{42} \\
& + m_{14}m_{21}m_{33}m_{42} + m_{14}m_{22}m_{31}m_{43} + m_{14}m_{23}m_{32}m_{41} \\
& - m_{11}m_{22}m_{34}m_{43} - m_{11}m_{23}m_{32}m_{44} - m_{11}m_{24}m_{33}m_{42} \\
& - m_{12}m_{21}m_{33}m_{44} - m_{12}m_{23}m_{34}m_{41} - m_{12}m_{24}m_{31}m_{43} \\
& - m_{13}m_{21}m_{34}m_{42} - m_{13}m_{22}m_{31}m_{44} - m_{13}m_{24}m_{32}m_{41} \\
& - m_{14}m_{21}m_{32}m_{43} - m_{14}m_{22}m_{33}m_{41} - m_{14}m_{23}m_{31}m_{42}
\end{aligned}$$
:::
:::

<!-- section: sec-3-3 | num: 3.3 | title: Teorema di Binet, cofattori e Teoremi di Laplace | kind: section | part: cap-3 -->

### 1. Idea in parole semplici

Abbiamo appena visto quanto sarebbe faticoso calcolare un determinante $4 \times 4$ usando tutti i $24$ termini della definizione. Fortunatamente esistono due strumenti potenti che trasformano il calcolo del determinante in un'operazione algebrica gestibile:

1. Il **Teorema di Binet** ci dice che il determinante rispetta il prodotto tra matrici: $\det(AB) = (\det A)(\det B)$. Non serve moltiplicare due grandi matrici per sapere il determinante del loro prodotto!
2. I **Teoremi di Laplace** riducono un determinante $n \times n$ a una somma di determinanti $(n-1) \times (n-1)$ più piccoli, scegliendo a nostro piacere la riga o la colonna più ricca di zeri (sviluppo di Laplace), mentre moltiplicare gli elementi di una riga per i cofattori di un'**altra** riga produce sempre esattamente $0$ (proprietà decisiva per costruire la matrice inversa nella sezione [3.4](#sec-3-4)).

### 2. Definizioni e enunciati precisi

:::thm Teorema di Binet (Lezione 5, p. 1)
Siano $A, B \in K^{n,n}$. Allora:

$$\det(AB) = (\det A)(\det B)$$
:::

:::def Definizione — Sottomatrice $A_{(i,j)}$ e cofattore $\operatorname{cof}_{i,j}(A)$ (Lezione 5, p. 1)
Sia $A \in K^{n,n}$ e siano $i, j \in \{1, \dots, n\}$.
- Indichiamo con $A_{(i,j)} \in K^{n-1,n-1}$ la matrice quadrata ottenuta da $A$ **eliminando la riga $i$ e la colonna $j$**.
- Si chiama **cofattore** *(o **complemento algebrico**)* di posto $(i,j)$ lo scalare:

$$\operatorname{cof}_{i,j}(A) \stackrel{\text{DEF}}{=} (-1)^{i+j} \det A_{(i,j)}$$
:::

*Trucco per il segno $(-1)^{i+j}$:* alterna a scacchiera partendo da $+$ in alto a sinistra $\begin{pmatrix} + & - & + & \dots \\ - & + & - & \dots \\ + & - & + & \dots \\ \vdots & \vdots & \vdots & \ddots \end{pmatrix}$ *(pari $\implies +$, dispari $\implies -$)*.

:::thm Primo Teorema di Laplace (Lezione 5, p. 2)
Sia $A \in K^{n,n}$. La somma dei prodotti degli elementi di una riga (o di una colonna) per i rispettivi cofattori è uguale al determinante di $A$:

$$\det A = \sum_{r=1}^n \operatorname{ent}_{ir}(A)\operatorname{cof}_{ir}(A) \qquad \text{(sviluppo lungo la riga } i\text{)}$$

$$\det A = \sum_{r=1}^n \operatorname{ent}_{rj}(A)\operatorname{cof}_{rj}(A) \qquad \text{(sviluppo lungo la colonna } j\text{)}$$
:::

:::thm Secondo Teorema di Laplace (Lezione 5, p. 2)
Sia $A \in K^{n,n}$. La somma dei prodotti degli elementi di una riga (o di una colonna) per i cofattori di un'**altra** riga (o colonna) fa zero:

$$\sum_{r=1}^n \operatorname{ent}_{ir}(A)\operatorname{cof}_{jr}(A) = 0 \qquad \text{se } i \neq j \quad \text{(righe diverse)}$$

$$\sum_{r=1}^n \operatorname{ent}_{ri}(A)\operatorname{cof}_{rj}(A) = 0 \qquad \text{se } i \neq j \quad \text{(colonne diverse)}$$
:::

### 3. Dimostrazioni

Nella Lezione 5 *(pp. 1–3)* il Teorema di Binet e il Primo e Secondo Teorema di Laplace vengono enunciati e applicati operativamente senza dimostrazione.

### 4. Esempi svolti

:::example Esempio 3.3.1 — Eliminazione di riga e colonna e calcolo di un cofattore (Lezione 5, pp. 1–2)
Consideriamo la matrice:

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 3 & 2 & 1 \end{pmatrix} \in \mathbb{R}^{3,3}$$

Scegliamo $i = 2$ e $j = 3$. Eliminando la riga $2$ e la colonna $3$ rimane la matrice $2 \times 2$:

$$A_{(2,3)} = \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix}$$

Calcoliamo il cofattore di posto $(2,3)$:

$$\operatorname{cof}_{2,3}(A) = (-1)^{2+3}\det \begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} = (-1)^5 (1\cdot 2 - 2\cdot 3) = -(2 - 6) = 4$$
:::

:::example Esempio 3.3.2 — Verifica del Primo e Secondo Teorema di Laplace (Lezione 5, pp. 2–3)
Consideriamo la matrice:

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 3 & 2 & -1 \end{pmatrix}$$

1. **Calcolo diretto (3×3):** $\det A = -5 + 36 + 24 - 45 - 12 + 8 = 6$.
2. **Primo Teorema di Laplace lungo la riga $1$:** prendiamo gli elementi $(1, 2, 3)$ della prima riga e moltiplichiamoli per i cofattori della riga $1$ *(segni $+, -, +$)*:
    $$\det A = 1\cdot\det\begin{pmatrix} 5 & 6 \\ 2 & -1 \end{pmatrix} - 2\det\begin{pmatrix} 4 & 6 \\ 3 & -1 \end{pmatrix} + 3\det\begin{pmatrix} 4 & 5 \\ 3 & 2 \end{pmatrix}$$
    $$= (-5 - 12) - 2(-4 - 18) + 3(8 - 15) = -17 + 44 - 21 = 6$$
    Il risultato coincide con il calcolo diretto!
3. **Secondo Teorema di Laplace con le righe $2$ e $1$:** prendiamo gli elementi della **riga $2$** $(4, 5, 6)$ e li moltiplichiamo per i cofattori della **riga $1$** *(i tre determinanti calcolati qui sopra con i segni $+, -, +$)*:
    $$4\det\begin{pmatrix} 5 & 6 \\ 2 & -1 \end{pmatrix} - 5\det\begin{pmatrix} 4 & 6 \\ 3 & -1 \end{pmatrix} + 6\det\begin{pmatrix} 4 & 5 \\ 3 & 2 \end{pmatrix}$$
    $$= 4(-5 - 12) - 5(-4 - 18) + 6(8 - 15) = 4(-17) - 5(-22) + 6(-7) = -68 + 110 - 42 = 0$$
    Come previsto dal Secondo Teorema di Laplace, la somma vale esattamente $0$.
:::

### 5. Errori comuni e trappole

1. **Dimenticare il segno $(-1)^{i+j}$ nel cofattore $\operatorname{cof}_{i,j}(A)$**
    - *Sbagliato:* nell'Esempio 3.3.1 calcolare $\operatorname{cof}_{2,3}(A) = \det\begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix} = -4$.
    - *Correzione:* il cofattore include sempre il segno a scacchiera $(-1)^{i+j}$. Poiché $2+3=5$ è dispari, il segno cambia da $-4$ a $+4$.
2. **Estendere Binet alla somma: credere che $\det(A+B) = \det A + \det B$**
    - *Sbagliato:* spezzare $\det(A+B)$ come $\det A + \det B$.
    - *Correzione:* Binet vale **solo per il prodotto** $\det(AB) = (\det A)(\det B)$. Per la somma in generale $\det(A+B) \neq \det A + \det B$ (esempio immediato: $\det(I_2 + I_2) = \det(2I_2) = 4$, mentre $\det I_2 + \det I_2 = 1 + 1 = 2$).

### 6. Riepilogo

- **Teorema di Binet:** $\det(AB) = (\det A)(\det B)$ per tutte le matrici quadrate $A, B \in K^{n,n}$.
- $A_{(i,j)} \in K^{n-1,n-1}$ si ottiene cancellando riga $i$ e colonna $j$ di $A$; il cofattore è $\operatorname{cof}_{i,j}(A) = (-1)^{i+j}\det A_{(i,j)}$.
- **I Teorema di Laplace:** $\det A$ è la somma dei prodotti degli elementi di una riga/colonna per i **propri** cofattori.
- **II Teorema di Laplace:** la somma dei prodotti degli elementi di una riga/colonna per i cofattori di un'**altra** riga/colonna fa sempre **$0$**.

### 7. Esercizi

:::exercise Esercizio 3.3.1 (Esercizio per casa — Facile · Lezione 5, p. 1)
Siano:

$$A = \begin{pmatrix} 2 & 3 \\ 4 & 5 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & -1 \\ 2 & 1 \end{pmatrix}$$

Verificare il Teorema di Binet ($\det(AB) = (\det A)(\det B)$).

:::solution Soluzione spiegata passo-passo
**Ragionamento:** calcoliamo $\det A$ e $\det B$ separatamente e facciamo il prodotto degli scalari; poi calcoliamo la matrice prodotto $AB$ riga per colonna e infine il suo determinante, confrontando i due valori.

1. **Determinanti dei singoli fattori:**
    $$\det A = 2\cdot 5 - 3\cdot 4 = 10 - 12 = -2$$
    $$\det B = 1\cdot 1 - (-1)\cdot 2 = 1 + 2 = 3$$
    Il prodotto dei due determinanti è:
    $$(\det A)(\det B) = (-2)\cdot 3 = -6$$

2. **Prodotto riga per colonna $AB$ e suo determinante:**
    $$AB = \begin{pmatrix} 2 & 3 \\ 4 & 5 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} 2\cdot 1 + 3\cdot 2 & 2\cdot(-1) + 3\cdot 1 \\ 4\cdot 1 + 5\cdot 2 & 4\cdot(-1) + 5\cdot 1 \end{pmatrix} = \begin{pmatrix} 8 & 1 \\ 14 & 1 \end{pmatrix}$$
    Calcoliamo il determinante di $AB$:
    $$\det(AB) = 8\cdot 1 - 1\cdot 14 = 8 - 14 = -6$$

3. **Conclusione:** $\det(AB) = -6 = (\det A)(\det B)$, il Teorema di Binet è verificato.
:::
:::

<!-- section: sec-3-4 | num: 3.4 | title: Matrice dei cofattori, aggiunta, criterio di invertibilità e calcolo di A⁻¹ | kind: section | part: cap-3 -->

### 1. Idea in parole semplici

Eccoci alla risposta finale alla domanda lasciata in sospeso nel Capitolo 2: **come si capisce se una matrice quadrata $A$ è invertibile, e come si calcola $A^{-1}$?**

Se riuniamo tutti i cofattori di $A$ in una matrice $A_{\text{COF}}$ e ne facciamo la trasposta (chiamata **matrice aggiunta** $A_{\text{AGG}} = {}^t A_{\text{COF}}$), moltiplicando $A \cdot A_{\text{AGG}}$ accade qualcosa di straordinario grazie ai due Teoremi di Laplace: sulla diagonale (dove riga e colonna coincidono) compare $\det A$ per il I Teorema di Laplace, mentre fuori dalla diagonale compaiono solo zeri per il II Teorema di Laplace! Quindi $A \cdot A_{\text{AGG}} = (\det A)I$. Da qui basta dividere per $\det A$ (quando $\det A \neq 0$) per ottenere la formula esplicita dell'inversa!

### 2. Definizioni e enunciati precisi

:::def Definizione — Matrice dei cofattori e matrice aggiunta (Lezione 5, p. 3)
Sia $A \in K^{n,n}$.
- Si chiama **matrice dei cofattori** di $A$ la matrice $A_{\text{COF}} \in K^{n,n}$ definita da:
    $$\operatorname{ent}_{ij}(A_{\text{COF}}) \stackrel{\text{DEF}}{=} \operatorname{cof}_{ij}(A)$$
- Si chiama **matrice aggiunta** di $A$ la trasposta della matrice dei cofattori:
    $$A_{\text{AGG}} \stackrel{\text{DEF}}{=} {}^t A_{\text{COF}}$$
:::

:::thm Proposizione — Identità fondamentale con la matrice aggiunta (Lezione 5, p. 4)
Per ogni matrice quadrata $A \in K^{n,n}$ vale:

$$A A_{\text{AGG}} = A_{\text{AGG}} A = (\det A) I$$
:::

:::thm Teorema — Criterio di invertibilità e formula della matrice inversa (Lezione 5, p. 5)
Sia $A \in K^{n,n}$. Allora:

$$A \text{ è invertibile} \iff \det A \neq 0$$

Inoltre, se $\det A \neq 0$, la matrice inversa è data esplicitamente da:

$$A^{-1} = (\det A)^{-1} A_{\text{AGG}} = \frac{1}{\det A}\, {}^t A_{\text{COF}}$$
:::

### 3. Dimostrazioni

:::proof Dimostrazione 1 — $A A_{\text{AGG}} = A_{\text{AGG}} A = (\det A) I$ (Lezione 5, p. 4)
**Idea di fondo:** calcoliamo la generica entrata $(i,j)$ del prodotto $A A_{\text{AGG}}$: la trasposizione dentro $A_{\text{AGG}} = {}^t A_{\text{COF}}$ trasforma gli indici $(r,j)$ in $(j,r)$, facendoci ricadere esattamente nella forma dei due Teoremi di Laplace!

**(1) Proviamo $A A_{\text{AGG}} = (\det A) I$:**
Per definizione di prodotto riga per colonna, di trasposta e di matrice dei cofattori:

$$\operatorname{ent}_{ij}(A A_{\text{AGG}}) = \sum_{r=1}^n \operatorname{ent}_{ir}(A)\operatorname{ent}_{rj}(A_{\text{AGG}}) = \sum_{r=1}^n \operatorname{ent}_{ir}(A)\operatorname{ent}_{rj}({}^t A_{\text{COF}})$$
$$= \sum_{r=1}^n \operatorname{ent}_{ir}(A)\operatorname{ent}_{jr}(A_{\text{COF}}) = \sum_{r=1}^n \operatorname{ent}_{ir}(A)\operatorname{cof}_{jr}(A)$$

Per i due Teoremi di Laplace *(Sezione [3.3](#sec-3-3))*, questa somma vale:
- $\det A$ se $i = j$ *(I Teorema di Laplace lungo la riga $i$)*;
- $0$ se $i \neq j$ *(II Teorema di Laplace tra la riga $i$ e la riga $j$)*.

Questa è esattamente la matrice scalare $\operatorname{ent}_{ij}\bigl((\det A)I\bigr)$, quindi $A A_{\text{AGG}} = (\det A)I$.

**(2)** La dimostrazione di $A_{\text{AGG}} A = (\det A) I$ è del tutto analoga *(utilizzando gli sviluppi rispetto alle colonne nei due Teoremi di Laplace)*.
:::

:::proof Dimostrazione 2 — $A$ è invertibile $\iff \det A \neq 0$ (Lezione 5, p. 5)
**Idea di fondo:** per il verso ($\Rightarrow$) applichiamo il Teorema di Binet a $AB = I$; per il verso ($\Leftarrow$) partiamo dalla Proposizione 1 e dividiamo tutto per lo scalare non nullo $\det A$.

- **($\Rightarrow$) Supponiamo che $A$ sia invertibile:** allora esiste $B \in K^{n,n}$ tale che $AB = BA = I$. Applicando il determinante ad ambo i membri e usando il Teorema di Binet e $\det I = 1$:
    $$\det(AB) = \det I \implies (\det A)(\det B) = 1 \implies \det A \neq 0$$
    *(infatti in un campo $K$, un prodotto non può fare $1$ se uno dei fattori è $0$)*.

- **($\Leftarrow$) Supponiamo che $\det A \neq 0$:** poiché $\det A$ appartiene a $K \setminus \{0\}$, esiste il suo inverso scalare $(\det A)^{-1}$. Partiamo dall'identità della Proposizione 1:
    $$A A_{\text{AGG}} = A_{\text{AGG}} A = (\det A) I$$
    Moltiplichiamo tutti i membri per $(\det A)^{-1}$ *(sfruttando $(aM)N = M(aN) = a(MN)$)*:
    $$(\det A)^{-1} A A_{\text{AGG}} = (\det A)^{-1} A_{\text{AGG}} A = I$$
    $$A\bigl[(\det A)^{-1} A_{\text{AGG}}\bigr] = \bigl[(\det A)^{-1} A_{\text{AGG}}\bigr] A = I$$
    Per definizione di matrice inversa segue che $A$ è invertibile e $A^{-1} = (\det A)^{-1} A_{\text{AGG}}$.
:::

### 4. Esempi svolti

:::example Esempio 3.4.1 — Caso generale $2 \times 2$ e verifica di $A A_{\text{AGG}}$ (Lezione 5, pp. 3–4)
Sia $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in K^{2,2}$. Calcoliamo i 4 cofattori:
- $\operatorname{cof}_{11}(A) = +d$, $\operatorname{cof}_{12}(A) = -c$;
- $\operatorname{cof}_{21}(A) = -b$, $\operatorname{cof}_{22}(A) = +a$.

Pertanto:

$$A_{\text{COF}} = \begin{pmatrix} d & -c \\ -b & a \end{pmatrix}, \qquad A_{\text{AGG}} = {}^t A_{\text{COF}} = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

*(Trucco visivo per il $2\times 2$:* nell'aggiunta si **scambiano** i due elementi sulla diagonale principale $a \leftrightarrow d$ e si **cambia segno** ai due fuori diagonale $b \mapsto -b, c \mapsto -c$!)*
Verifichiamo il prodotto $A A_{\text{AGG}}$:

$$\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \begin{pmatrix} ad-bc & 0 \\ 0 & ad-bc \end{pmatrix} = (\det A)\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = (\det A)I$$
:::

:::example Esempio 3.4.2 — Invertibilità parametrica $2\times 2$ e calcolo di $A^{-1}$ (Lezione 5, pp. 5–6)
Sia $A = \begin{pmatrix} 1 & 2 \\ 3 & h \end{pmatrix} \in \mathbb{R}^{2,2}$. Determinare i valori di $h$ per cui $A$ è invertibile e calcolarne l'inversa.

1. **Condizione di invertibilità:** $\det A = h - 6$, quindi $\det A = 0 \iff h = 6$.
    - Per $h = 6$, la matrice **non è invertibile**.
    - Per $h \neq 6$, la matrice **è invertibile**.
2. **Calcolo di $A^{-1}$ per $h \neq 6$:**
    $$A_{\text{COF}} = \begin{pmatrix} h & -3 \\ -2 & 1 \end{pmatrix}, \qquad A_{\text{AGG}} = {}^t A_{\text{COF}} = \begin{pmatrix} h & -2 \\ -3 & 1 \end{pmatrix}$$
    $$A^{-1} = \frac{1}{h - 6}\begin{pmatrix} h & -2 \\ -3 & 1 \end{pmatrix} = \begin{pmatrix} \frac{h}{h-6} & \frac{-2}{h-6} \\ \frac{-3}{h-6} & \frac{1}{h-6} \end{pmatrix}$$
:::

:::note Nota sugli appunti originali (`Lez05`, p. 6)
In fondo alla prima matrice scritta esplicitamente a p. 6 (entrata $(2,1)$ di $A^{-1}$), nel PDF manoscritto compare il refuso $\frac{-3}{h-1}$ anziché $\frac{-3}{h-6}$, subito dopo aver scritto correttamente $\frac{1}{h-6}\begin{pmatrix} h & -2 \\ -3 & 1 \end{pmatrix}$. Qui sopra è riportato il valore esatto $\frac{-3}{h-6}$.
:::

:::example Esempio 3.4.3 — Invertibilità parametrica $3\times 3$ e calcolo di $A^{-1}$ (Lezione 5, p. 6)
Sia $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 3 & 2 & h \end{pmatrix} \in \mathbb{R}^{3,3}$. Determinare per quali $h$ è invertibile e calcolare $A^{-1}$.

1. **Determinante:**
    $$\det A = 5h + 36 + 24 - 45 - 12 - 8h = -3h + 3 = 3(1-h)$$
    Quindi $\det A = 0 \iff h = 1$: per $h = 1$ $A$ **non è invertibile**; per $h \neq 1$ $A$ **è invertibile**.
2. **Matrice dei cofattori ($h \neq 1$):** calcoliamo tutti i $9$ cofattori con i segni della scacchiera $\begin{pmatrix} + & - & + \\ - & + & - \\ + & - & + \end{pmatrix}$:
    - riga 1: $+(5h-12)$, $-(4h-18)=18-4h$, $+(8-15)=-7$;
    - riga 2: $-(2h-6)=6-2h$, $+(h-9)$, $-(2-6)=4$;
    - riga 3: $+(12-15)=-3$, $-(6-12)=6$, $+(5-8)=-3$.
    Quindi:
    $$A_{\text{COF}} = \begin{pmatrix} 5h-12 & 18-4h & -7 \\ 6-2h & h-9 & 4 \\ -3 & 6 & -3 \end{pmatrix}$$
3. **Trasposizione e divisione per $\det A = 3(1-h)$:**
    $$A_{\text{AGG}} = {}^t A_{\text{COF}} = \begin{pmatrix} 5h-12 & 6-2h & -3 \\ 18-4h & h-9 & 6 \\ -7 & 4 & -3 \end{pmatrix} \implies A^{-1} = \frac{1}{3(1-h)} \begin{pmatrix} 5h-12 & 6-2h & -3 \\ 18-4h & h-9 & 6 \\ -7 & 4 & -3 \end{pmatrix}$$
:::

### 5. Errori comuni e trappole

1. **Dimenticare di trasporre $A_{\text{COF}}$**
    - *Sbagliato:* scrivere $A^{-1} = \frac{1}{\det A} A_{\text{COF}}$.
    - *Correzione:* la formula è $A^{-1} = \frac{1}{\det A} A_{\text{AGG}}$, dove **$A_{\text{AGG}} = {}^t A_{\text{COF}}$**! Senza trasposizione, l'entrata $(i,j)$ di $A \cdot A_{\text{COF}}$ non applica Laplace alla riga $i$ con la colonna $j$ correttamente e non produce $(\det A)I$.
2. **Fare errori sui segni a scacchiera nei cofattori delle posizioni $(1,2), (2,1), (2,3), (3,2)$**
    - *Sbagliato:* dimenticare il $-$ davanti al minore di posizione $(2,1)$ o $(1,2)$, lasciando ad esempio $2h-6$ invece di $6-2h$.
    - *Correzione:* scrivere prima la griglia dei segni $+, -, + / -, +, - / +, -, +$ sopra i $9$ calcoli e verificare sempre la diagonale del prodotto $AA^{-1} = I$ su almeno una riga-colonna!

### 6. Riepilogo

- $A_{\text{COF}}$ ha entrata $(i,j)$ uguale a $\operatorname{cof}_{ij}(A) = (-1)^{i+j}\det A_{(i,j)}$; la matrice aggiunta è $A_{\text{AGG}} = {}^t A_{\text{COF}}$.
- Identità fondamentale: $A A_{\text{AGG}} = A_{\text{AGG}} A = (\det A)I$.
- **Teorema di invertibilità:** $A \in K^{n,n}$ è invertibile $\iff \det A \neq 0$.
- Formula dell'inversa (per $\det A \neq 0$): $A^{-1} = (\det A)^{-1} A_{\text{AGG}}$.
- Per il $2\times 2$ $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ con $ad-bc \neq 0$, l'inversa è $\frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.

### 7. Esercizi

:::exercise Esercizio 3.4.1 (Esercizio per casa — Medio · Lezione 5, p. 6)
Sia:

$$A = \begin{pmatrix} h & 2 & 3 \\ 0 & 1-h & 4 \\ 0 & 0 & 1 \end{pmatrix}$$

Calcolare, se possibile, l'inversa di $A$ (al variare di $h \in \mathbb{R}$).

:::solution Soluzione spiegata passo-passo
**Ragionamento:** prima calcoliamo $\det A$ per individuare i valori del parametro $h$ che rendono $A$ invertibile ($\det A \neq 0$). Poi, per tali valori, costruiamo $A_{\text{COF}}$, la trasponiamo in $A_{\text{AGG}}$ e dividiamo per $\det A$, verificando infine $A A^{-1} = I$.

1. **Calcolo di $\det A$ e discussione di invertibilità:**
    $A$ è triangolare superiore, quindi il determinante (calcolabile anche direttamente con il I Teorema di Laplace sulla colonna $1$ o riga $3$) è il prodotto degli elementi diagonali:
    $$\det A = h(1-h)\cdot 1 = h(1-h)$$
    Quindi $\det A = 0 \iff h = 0 \text{ oppure } h = 1$.
    - Per $h = 0$ e per $h = 1$, la matrice **non è invertibile**.
    - Per $h \neq 0$ e $h \neq 1$, la matrice **è invertibile**.

2. **Calcolo dei $9$ cofattori per $h \neq 0, 1$:**
    - $\operatorname{cof}_{11} = +\det\begin{pmatrix} 1-h & 4 \\ 0 & 1 \end{pmatrix} = 1-h$
    - $\operatorname{cof}_{12} = -\det\begin{pmatrix} 0 & 4 \\ 0 & 1 \end{pmatrix} = 0$
    - $\operatorname{cof}_{13} = +\det\begin{pmatrix} 0 & 1-h \\ 0 & 0 \end{pmatrix} = 0$
    - $\operatorname{cof}_{21} = -\det\begin{pmatrix} 2 & 3 \\ 0 & 1 \end{pmatrix} = -2$
    - $\operatorname{cof}_{22} = +\det\begin{pmatrix} h & 3 \\ 0 & 1 \end{pmatrix} = h$
    - $\operatorname{cof}_{23} = -\det\begin{pmatrix} h & 2 \\ 0 & 0 \end{pmatrix} = 0$
    - $\operatorname{cof}_{31} = +\det\begin{pmatrix} 2 & 3 \\ 1-h & 4 \end{pmatrix} = 8 - 3(1-h) = 3h + 5$
    - $\operatorname{cof}_{32} = -\det\begin{pmatrix} h & 3 \\ 0 & 4 \end{pmatrix} = -4h$
    - $\operatorname{cof}_{33} = +\det\begin{pmatrix} h & 2 \\ 0 & 1-h \end{pmatrix} = h(1-h)$

    Pertanto:
    $$A_{\text{COF}} = \begin{pmatrix} 1-h & 0 & 0 \\ -2 & h & 0 \\ 3h+5 & -4h & h(1-h) \end{pmatrix}$$

3. **Matrice aggiunta e matrice inversa:**
    Trasponiamo $A_{\text{COF}}$ per ottenere $A_{\text{AGG}} = {}^t A_{\text{COF}}$:
    $$A_{\text{AGG}} = \begin{pmatrix} 1-h & -2 & 3h+5 \\ 0 & h & -4h \\ 0 & 0 & h(1-h) \end{pmatrix}$$
    Dividendo per $\det A = h(1-h)$:
    $$A^{-1} = \frac{1}{h(1-h)} \begin{pmatrix} 1-h & -2 & 3h+5 \\ 0 & h & -4h \\ 0 & 0 & h(1-h) \end{pmatrix} = \begin{pmatrix} \frac{1}{h} & \frac{-2}{h(1-h)} & \frac{3h+5}{h(1-h)} \\ 0 & \frac{1}{1-h} & \frac{-4}{1-h} \\ 0 & 0 & 1 \end{pmatrix}$$

4. **Verifica rapida su $A A^{-1}$:**
    - Riga $1$ di $A$ per colonna $3$ di $A^{-1}$: $h\cdot\frac{3h+5}{h(1-h)} + 2\cdot\frac{-4}{1-h} + 3\cdot 1 = \frac{3h+5 - 8 + 3 - 3h}{1-h} = \frac{0}{1-h} = 0$.
    - Riga $1$ di $A$ per colonna $2$ di $A^{-1}$: $h\cdot\frac{-2}{h(1-h)} + 2\cdot\frac{1}{1-h} + 0 = 0$.
    - Gli elementi diagonali valgono $h\cdot\frac{1}{h} = 1$, $(1-h)\cdot\frac{1}{1-h} = 1$, $1\cdot 1 = 1$. Quindi $A A^{-1} = I$ è verificata!
:::
:::
