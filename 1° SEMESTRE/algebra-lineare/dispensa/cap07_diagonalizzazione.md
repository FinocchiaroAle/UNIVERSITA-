<!-- part: cap-7 | num: 7 | label: CAPITOLO 7 | title: Similitudine, autovalori e diagonalizzazione | refs: Fonti: Lezione 12 (18/11/2026, pp. 3–8), Lezione 13 (23/11/2026, pp. 1–10) e Lezione 14 (25/11/2026, p. 4) -->

<!-- section: sec-7-1 | num: 7.1 | title: Similitudine tra matrici | kind: section | part: cap-7 -->

### 1. Idea in parole semplici

In Algebra Lineare, le matrici più semplici su cui calcolare potenze, determinanti e sistemi sono senza dubbio le **matrici diagonali**, dove sopravvivono numeri solo sulla diagonale principale. Purtroppo una matrice $A \in K^{n,n}$ scelta a caso ha elementi quasi ovunque.

Quando due matrici quadrate $A$ e $B$ rappresentano la *stessa* trasformazione lineare vista in due basi diverse (cioè sono legate da un cambio di base tramite una matrice invertibile $P$: $A = P^{-1}BP$), le chiamiamo **matrici simili**. Come scopriremo in questo capitolo, la similitudine divide l'intero universo delle matrici quadrate in "famiglie" (è una **relazione di equivalenza**), e l'obiettivo della **diagonalizzazione** sarà capire quando nella famiglia di $A$ abita una matrice diagonale $D$!

### 2. Definizioni e enunciati precisi

:::def Definizione — Matrici simili (Lezione 12, p. 3)
Siano $A, B \in K^{n,n}$. Diremo che **$A$ è simile a $B$** se esiste una matrice invertibile $P \in K^{n,n}$ tale che:

$$A = P^{-1} B P$$
:::

:::thm Proposizione — La similitudine è una relazione di equivalenza (Lezione 12, pp. 3–4)
La relazione di similitudine su $K^{n,n}$ è una **relazione di equivalenza**, cioè per ogni $A, B, C \in K^{n,n}$ gode delle $3$ proprietà:
1. **Riflessiva:** $A$ è simile ad $A$;
2. **Simmetrica:** se $A$ è simile a $B$, allora $B$ è simile ad $A$;
3. **Transitiva:** se $A$ è simile a $B$ e $B$ è simile a $C$, allora $A$ è simile a $C$.
:::

### 3. Dimostrazioni

:::proof Dimostrazione — La relazione di similitudine su $K^{n,n}$ è una relazione di equivalenza (Lezione 12, pp. 3–4)
**Idea di fondo:** per la riflessiva basta prendere $P = I$; per la simmetrica si isola $B$ ponendo $Q = P^{-1}$ (che resta invertibile!); per la transitiva si sostituisce $B$ dentro $A$ usando la proprietà $(QP)^{-1} = P^{-1}Q^{-1}$.

1. **Proprietà riflessiva:** sia $A \in K^{n,n}$. Poiché la matrice identica $I$ è invertibile ($I^{-1} = I$), vale:
    $$A = I^{-1} A I \implies A \text{ è simile ad } A$$
2. **Proprietà simmetrica:** siano $A, B \in K^{n,n}$ tali che $A$ è simile a $B$. Esiste dunque una matrice invertibile $P \in K^{n,n}$ con $A = P^{-1} B P$. Moltiplicando prima a sinistra per $P$ e poi a destra per $P^{-1}$:
    $$PA = B P \implies P A P^{-1} = B$$
    Poniamo $Q \stackrel{\text{DEF}}{=} P^{-1}$ *(che è a sua volta invertibile con $Q^{-1} = (P^{-1})^{-1} = P$)*. Allora:
    $$B = Q^{-1} A Q \implies B \text{ è simile ad } A$$
3. **Proprietà transitiva:** siano $A, B, C \in K^{n,n}$ e supponiamo che $A$ sia simile a $B$ e $B$ sia simile a $C$. Esistono quindi matrici invertibili $P, Q \in K^{n,n}$ tali che:
    $$A = P^{-1} B P \qquad \text{e} \qquad B = Q^{-1} C Q$$
    Sostituiamo l'espressione di $B$ nella prima uguaglianza e ricordiamo la regola $(QP)^{-1} = P^{-1}Q^{-1}$ *(dimostrata nella Sezione [1.2](#sec-1-2) per i monoidi!)*:
    $$A = P^{-1}(Q^{-1} C Q)P = (P^{-1}Q^{-1})\, C\, (QP) = (QP)^{-1}\, C\, (QP)$$
    Ponendo $T \stackrel{\text{DEF}}{=} QP$ *(prodotto di due matrici invertibili, quindi anch'essa invertibile con $\det T = (\det Q)(\det P) \neq 0$)*, segue $A = T^{-1} C T$, quindi $A$ è simile a $C$.
:::

:::note Nota sugli appunti originali (`Lez12`, pp. 3–4)
Nella dimostrazione della proprietà simmetrica e transitiva il prof utilizza implicitamente il fatto che se $P$ e $Q$ sono invertibili, allora anche $Q = P^{-1}$ e $T = QP$ sono invertibili (per $P^{-1}$ l'inversa è $P$; per $QP$ l'inversa è $P^{-1}Q^{-1}$).
:::

### 4. Esempi svolti

:::example Esempio 7.1.1 — Verificare che $A = \begin{pmatrix} -1 & -2 \\ 3 & 4 \end{pmatrix}$ è simile a $D = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$ (Lezione 12, p. 3)
Consideriamo $D = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$ e $P = \begin{pmatrix} 3 & 2 \\ 1 & 1 \end{pmatrix}$.
1. Controlliamo che $P$ è invertibile: $\det P = 3 - 2 = 1 \neq 0$, dunque:
    $$P^{-1} = \frac{1}{\det P} P_{\text{AGG}} = 1 \cdot {}^t\begin{pmatrix} 1 & -1 \\ -2 & 3 \end{pmatrix} = \begin{pmatrix} 1 & -2 \\ -1 & 3 \end{pmatrix}$$
2. Calcoliamo $A = P^{-1} D P$:
    $$A = \begin{pmatrix} 1 & -2 \\ -1 & 3 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 3 & 2 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -4 \\ -1 & 6 \end{pmatrix}\begin{pmatrix} 3 & 2 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 3 - 4 & 2 - 4 \\ -3 + 6 & -2 + 6 \end{pmatrix} = \begin{pmatrix} -1 & -2 \\ 3 & 4 \end{pmatrix}$$

Pertanto la matrice $\begin{pmatrix} -1 & -2 \\ 3 & 4 \end{pmatrix}$ è simile alla matrice diagonale $\begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$.
:::

### 5. Errori comuni e trappole

1. **Dimenticare che $P$ deve essere invertibile nella definizione di similitudine**
    - *Sbagliato:* scrivere che $A$ è simile a $B$ se $PA = BP$ per una qualsiasi matrice $P$ (anche con $P = O$).
    - *Correzione:* la definizione esige **$P$ invertibile** ($\det P \neq 0$) e $A = P^{-1}BP$. Se $P = O$ sarebbe $OA = BO$ sempre vero per tutte le matrici $A$ e $B$!
2. **Invertire erroneamente $(QP)^{-1} = Q^{-1}P^{-1}$**
    - *Sbagliato:* scrivere $P^{-1}Q^{-1} = (PQ)^{-1}$ e quindi bloccarsi in $P^{-1}Q^{-1} C QP$.
    - *Correzione:* per l'inverso di un prodotto in un monoide *(Sezione [1.2](#sec-1-2))*, l'ordine si capovolge: $P^{-1}Q^{-1} = (QP)^{-1}$, che combacia esattamente con il fattore $QP$ a destra di $C$.

### 6. Riepilogo

- $A, B \in K^{n,n}$ sono **simili** se esiste $P \in K^{n,n}$ invertibile tale che $A = P^{-1}BP$.
- La similitudine è una **relazione di equivalenza** su $K^{n,n}$ (riflessiva, simmetrica, transitiva).
- In virtù della simmetria, dire "$A$ è simile a $B$" o "$B$ è simile ad $A$" è equivalente (sostituendo $P$ con $P^{-1}$).

### 7. Esercizi

Nella Lezione 12 *(pp. 3–4)* la similitudine viene introdotta con l'Esempio 7.1.1; gli esercizi operativi su polinomio caratteristico, autovalori e similitudine con matrici diagonali si trovano nelle sezioni [7.2](#sec-7-2), [7.3](#sec-7-3) e [7.4](#sec-7-4).

<!-- section: sec-7-2 | num: 7.2 | title: Polinomio caratteristico e invarianza per similitudine | kind: section | part: cap-7 -->

### 1. Idea in parole semplici

Come facciamo a capire se due matrici possono essere simili senza dover andare a tentoni cercando una matrice invertibile $P$ tra le infinite possibili? Serve un'"impronta digitale" che **resti identica** ogni volta che passiamo da $B$ a una matrice simile $A = P^{-1}BP$.

Questa impronta digitale è un polinomio di grado $n$ costruito sottraendo la variabile $x$ dalla diagonale di $A$ e calcolandone il determinante: si chiama **polinomio caratteristico** **$P_A(x) = \det(A - xI)$**. Dimostreremo subito via Binet che **matrici simili hanno lo stesso identico polinomio caratteristico** (e quindi anche la stessa traccia e lo stesso determinante!). Ma attenzione all'insidia inversa: avere lo stesso polinomio caratteristico è condizione *necessaria*, **non** sufficiente per la similitudine!

### 2. Definizioni e enunciati precisi

:::def Definizione — Polinomio caratteristico $P_A(x)$ (Lezione 12, p. 4)
Sia $A \in K^{n,n}$ e sia $x$ una variabile. Si chiama **polinomio caratteristico** di $A$ il polinomio:

$$P_A(x) \stackrel{\text{DEF}}{=} \det(A - xI)$$
:::

#### Formule esplicite del polinomio caratteristico per $n = 2, 3, 4$ *(Lezione 12, pp. 4–5)*

- **$n = 2$:** per $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in K^{2,2}$:
    $$P_A(x) = \det\begin{pmatrix} a-x & b \\ c & d-x \end{pmatrix} = x^2 - (\operatorname{tr} A)x + \det A$$
- **$n = 3$:** per $A = (a_{ij}) \in K^{3,3}$:
    $$P_A(x) = -x^3 + (\operatorname{tr} A)x^2 - (t_2 A)x + \det A$$
    dove $t_2 A$ è la **somma dei tre minori principali di ordine $2$** di $A$ *(ottenuti eliminando rispettivamente riga/colonna 3, riga/colonna 2, riga/colonna 1)*:
    $$t_2 A = \det\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} + \det\begin{pmatrix} a_{11} & a_{13} \\ a_{31} & a_{33} \end{pmatrix} + \det\begin{pmatrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{pmatrix}$$
- **$n = 4$:** analogamente i segni alternano partendo da $(-1)^n$:
    $$P_A(x) = x^4 - (\operatorname{tr} A)x^3 + (t_2 A)x^2 - (t_3 A)x + \det A$$

:::thm Proposizione — Invarianza del polinomio caratteristico per similitudine (Lezione 12, p. 6)
Siano $A, B \in K^{n,n}$. Se $A$ è **simile** a $B$, allora hanno lo stesso polinomio caratteristico:

$$P_A(x) = P_B(x)$$

*(Attenzione: il **viceversa non vale**: esistono matrici con lo stesso polinomio caratteristico che **non** sono simili!)*
:::

### 3. Dimostrazioni

:::proof Dimostrazione 1 — $A$ simile a $B \implies P_A(x) = P_B(x)$ (Lezione 12, p. 6)
**Idea di fondo:** riscriviamo $xI$ usando il trucco $P^{-1}(xI)P = xI$, raccogliamo $P^{-1}$ a sinistra e $P$ a destra dentro $\det(P^{-1}BP - xI)$, e poi spacchiamo tutto con il Teorema di Binet!

Poiché $A$ è simile a $B$, esiste una matrice invertibile $P \in K^{n,n}$ tale che $A = P^{-1} B P$. Osservando che $P^{-1}(xI)P = x P^{-1} I P = x P^{-1} P = xI$, calcoliamo $P_A(x)$ usando le proprietà distributive del prodotto tra matrici e poi il **Teorema di Binet** *(Sezione [3.3](#sec-3-3))*:

$$\begin{aligned}
P_A(x) &= \det(A - xI) = \det(P^{-1}BP - xI) = \det\bigl(P^{-1}BP - P^{-1}(xI)P\bigr) \\
&= \det\bigl[P^{-1}(B - xI)P\bigr] = (\det P^{-1})\,[\det(B - xI)]\,(\det P) \\
&= (\det P^{-1})(\det P)\,[\det(B - xI)] = \det(P^{-1}P)\,[\det(B - xI)] \\
&= \underbrace{(\det I)}_{= 1}\,\det(B - xI) = P_B(x)
\end{aligned}$$
:::

:::proof Dimostrazione 2 — Controesempio al viceversa tramite dimostrazione per assurdo (Lezione 12, p. 6)
**Idea di fondo:** prendiamo la matrice nulla $O$ e la matrice $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$; entrambe hanno polinomio caratteristico $x^2$, ma l'unica matrice simile a $O$ è $O$ stessa!

Consideriamo $O = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$ e $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$. I loro polinomi caratteristici coincidono:

$$P_O(x) = \det\begin{pmatrix} -x & 0 \\ 0 & -x \end{pmatrix} = x^2, \qquad P_A(x) = \det\begin{pmatrix} -x & 1 \\ 0 & -x \end{pmatrix} = x^2$$

Tuttavia $A$ **non è simile ad $O$**. Infatti, supponiamo **per assurdo** che $A$ sia simile ad $O$: allora esisterebbe $P$ invertibile tale che $A = P^{-1} O P = O$, ma $A \neq O$, assurdo!
:::

### 4. Esempi svolti

:::example Esempio 7.2.1 — Calcolo di $P_A(x)$ per $n = 2$ e $n = 3$ (Lezione 12, pp. 5–6)
1. **Caso $2\times 2$ (p. 5):** $A = \begin{pmatrix} 1 & 3 \\ 4 & 1 \end{pmatrix}$.
    - Calcolo diretto: $P_A(x) = \det\begin{pmatrix} 1-x & 3 \\ 4 & 1-x \end{pmatrix} = (1-x)^2 - 12 = x^2 - 2x + 1 - 12 = x^2 - 2x - 11$.
    - Verifica con traccia e determinante: $\operatorname{tr} A = 1 + 1 = 2$, $\det A = 1 - 12 = -11 \implies x^2 - 2x - 11$.
2. **Caso $3\times 3$ con formula di traccia e minori principali $t_2 A$ (pp. 5–6):** $A = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 2 & 1 \\ 3 & 1 & 1 \end{pmatrix}$.
    - $\operatorname{tr} A = 1 + 2 + 1 = 4$;
    - $t_2 A = \det\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} + \det\begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix} + \det\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = (2 - 1) + 1 + (2 - 1) = 3$;
    - $\det A = 2 + 3 + 0 - 0 - 1 - 1 = 3$.
    Sostituendo in $P_A(x) = -x^3 + (\operatorname{tr} A)x^2 - (t_2 A)x + \det A$ si ottiene:
    $$P_A(x) = -x^3 + 4x^2 - 3x + 3$$
:::

### 5. Errori comuni e trappole

1. **Sbagliare i segni alternati nella formula $n=3$: $-x^3 + (\operatorname{tr} A)x^2 - (t_2 A)x + \det A$**
    - *Sbagliato:* usare $+x^3 - (\operatorname{tr} A)x^2 + (t_2 A)x - \det A$ confondendosi con $\det(xI - A)$.
    - *Correzione:* con la definizione ufficiale del corso $P_A(x) = \det(A - xI)$, i termini diagonali sono $(a_{ii} - x)$, quindi il termine di grado $3$ ha sempre il segno **$-x^3$** per $n=3$, **$\operatorname{tr} A$ ha segno $+$**, **$t_2 A$ ha segno $-$**, e **$\det A$ ha segno $+$** *(comodo controllo: per $x = 0$, $P_A(0) = \det(A - 0\cdot I) = \det A$!)*
2. **Dimenticare il minore $(1,3)$ dentro $t_2 A$**
    - *Sbagliato:* sommare solo il blocco $2\times 2$ in alto a sinistra e quello in basso a destra.
    - *Correzione:* i minori principali di ordine $2$ di una $3\times 3$ sono **tre** (corrispondenti alle tre coppie di indici uguali: $\{1,2\}$, $\{1,3\}$ e $\{2,3\}$).

### 6. Riepilogo

- Il **polinomio caratteristico** di $A \in K^{n,n}$ è $P_A(x) \stackrel{\text{DEF}}{=} \det(A - xI)$.
- Per $n=2$: $P_A(x) = x^2 - (\operatorname{tr} A)x + \det A$.
- Per $n=3$: $P_A(x) = -x^3 + (\operatorname{tr} A)x^2 - (t_2 A)x + \det A$, dove $t_2 A$ è la somma dei $3$ minori principali di ordine $2$.
- **Teorema:** se $A$ è simile a $B$, allora $P_A(x) = P_B(x)$ *(ma il viceversa è falso!)*.

### 7. Esercizi

La Lezione 12 *(pp. 4–6)* applica il polinomio caratteristico negli Esempi 7.2.1 e passa immediatamente nella sezione [7.3](#sec-7-3) al legame con **autovalori e autovettori** (con l'esercizio svolto di `Lez12`, p. 8).

<!-- section: sec-7-3 | num: 7.3 | title: Autovalori, autovettori, autospazi e molteplicità | kind: section | part: cap-7 -->

### 1. Idea in parole semplici

Applicando una matrice $A$ ai vettori di $K^n$ tramite $f_A(v) = Av$, di solito ogni vettore viene ruotato e allungato in una nuova direzione. Ma esistono quasi sempre alcune direzioni privilegiate lungo le quali $f_A$ **non ruota il vettore**: si limita a moltiplicarlo per uno scalare $\lambda$ ($f_A(v) = \lambda v$)!

- Il fattore di scala $\lambda \in K$ si chiama **autovalore** (ed è esattamente una radice del polinomio caratteristico $P_A(x)$!);
- ogni vettore non nullo $v \neq \underline{0}$ che mantiene la propria direzione sotto $A$ è un **autovettore** relativo a $\lambda$;
- insieme al vettore nullo, tutti gli autovettori di uno stesso $\lambda$ formano il sottospazio chiamato **autospazio** $V_\lambda$.

Ogni autovalore possiede due contatori: la **molteplicità algebrica $m_\lambda$** (quante volte compare come radice in $P_A(x)$) e la **molteplicità geometrica $g_\lambda$** (la dimensione del suo autospazio $V_\lambda$). Vale sempre $1 \le g_\lambda \le m_\lambda$, e il pareggio perfetto $g_\lambda = m_\lambda$ sarà il segreto della diagonalizzabilità!

### 2. Definizioni e enunciati precisi

:::def Definizione — Matrice diagonalizzabile, autovalore e autovettore (Lezione 12, p. 7)
- Sia $A \in K^{n,n}$. Diremo che $A$ è **diagonalizzabile** se $A$ è **simile ad una matrice diagonale**.
- Sia $A \in K^{n,n}$, $f_A : K^n \to K^n$ l'applicazione associata ad $A$, e sia $\lambda \in K$. Diremo che $\lambda$ è un **autovalore** di $A$ se esiste un vettore **$v \in K^n$ con $v \neq \underline{0}$** tale che:
    $$f_A(v) = \lambda v$$
- Se $\lambda$ è un autovalore di $A$, ogni vettore $v \in K^n$ con **$v \neq \underline{0}$** tale che $f_A(v) = \lambda v$ si chiama **autovettore** associato all'autovalore $\lambda$.
:::

:::thm Proposizioni — Autovalori delle matrici diagonali e caratterizzazione tramite $P_A(x)$ (Lezione 12, pp. 7–8; Lezione 13, p. 1)
1. **Matrice diagonale (`Lez12`, p. 7):** se $D = \begin{pmatrix} \lambda_1 & 0 & \dots & 0 \\ 0 & \lambda_2 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \lambda_n \end{pmatrix}$ è diagonale, allora gli elementi diagonali $\lambda_1, \dots, \lambda_n \in K$ sono autovalori di $D$ *(con autovettori i vettori della base canonica $e_1, \dots, e_n$)*.
2. **Caratterizzazione algebrica (`Lez12`, p. 8):** sia $A \in K^{n,n}$. Allora:
    $$\lambda \in K \text{ è un autovalore di } A \iff \lambda \text{ è soluzione (radice) di } P_A(x) = 0$$
:::

:::def Definizione — Molteplicità algebrica ($m_\lambda$), autospazio ($V_\lambda$) e molteplicità geometrica ($g_\lambda$) (Lezione 13, pp. 1–3)
Sia $A \in K^{n,n}$ e sia $\lambda \in K$ un autovalore di $A$:
- Si chiama **molteplicità algebrica** di $\lambda$ *(denotata con **$m_\lambda$**)* la sua molteplicità come radice del polinomio caratteristico *(cioè l'esponente $r \ge 1$ in $P_A(x) = (x - \lambda)^r Q(x)$ con $Q(\lambda) \neq 0$)*.
- Si chiama **autospazio** associato all'autovalore $\lambda$ il sottoinsieme:
    $$V_\lambda \stackrel{\text{DEF}}{=} \{v \in K^n \mid f_A(v) = \lambda v\} = \operatorname{Ker}(f_A - \lambda \operatorname{id})$$
    che è un sottospazio di $K^n$ *(corrispondente alle soluzioni del sistema omogeneo $(A - \lambda I)X = \underline{0}$)*.
- Si chiama **molteplicità geometrica** di $\lambda$ *(denotata con **$g_\lambda$**)* la dimensione dell'autospazio:
    $$g_\lambda \stackrel{\text{DEF}}{=} \dim_K V_\lambda = n - \operatorname{rk}(A - \lambda I)$$
:::

:::thm Proposizione — Disuguaglianza tra molteplicità geometrica e algebrica (Lezione 13, pp. 3, 5)
Per ogni $A \in K^{n,n}$ e per ogni autovalore $\lambda \in K$ di $A$, vale sempre:

$$1 \le g_\lambda \le m_\lambda$$

*(In particolare, se un autovalore è **semplice**, cioè $m_\lambda = 1$, allora automaticamente si ha **$g_\lambda = 1 = m_\lambda$** senza bisogno di calcolare il rango!)*
:::

### 3. Dimostrazioni

Nelle Lezioni 12 *(pp. 7–8)* e 13 *(pp. 1–3)* il docente dimostra direttamente la Proposizione sugli autovalori delle matrici diagonali nel caso $2\times 2$ $D = \begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix}$ verificando $f_D(e_1) = \begin{pmatrix} a \\ 0 \end{pmatrix} = a e_1$ e $f_D(e_2) = \begin{pmatrix} 0 \\ b \end{pmatrix} = b e_2$, mentre la caratterizzazione $P_A(\lambda)=0$, l'essere $V_\lambda = \operatorname{Ker}(f_A - \lambda \operatorname{id})$ un sottospazio, e le relazioni $g_\lambda = n - \operatorname{rk}(A - \lambda I) \le m_\lambda$ vengono enunciate e applicate senza dimostrazioni formali.

### 4. Esempi svolti

:::example Esempio 7.3.1 — Autovalori della matrice $A$ già vista nell'Esempio 7.1.1 (Lezione 12, pp. 7–8)
Riprendiamo $A = \begin{pmatrix} -1 & -2 \\ 3 & 4 \end{pmatrix}$ (che avevamo visto simile a $D = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$, quindi è diagonalizzabile):

$$P_A(x) = \det\begin{pmatrix} -1-x & -2 \\ 3 & 4-x \end{pmatrix} = (-1-x)(4-x) + 6 = x^2 - 3x + 2$$

Risolviamo $P_A(x) = 0 \iff x^2 - 3x + 2 = 0$: $\Delta = 9 - 8 = 1$, da cui $x = \frac{3 \pm 1}{2}$, quindi gli autovalori di $A$ sono $\lambda_1 = 1$ e $\lambda_2 = 2$ — esattamente gli elementi diagonali della matrice $D$!
:::

:::example Esempio 7.3.2 — Calcolo completo di $m_\lambda$ e $g_\lambda$ per una triangolare $3 \times 3$ (Lezione 13, pp. 2–4)
Consideriamo:

$$A = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix} \in \mathbb{R}^{3,3}$$

1. **Polinomio caratteristico e molteplicità algebriche:** essendo triangolare superiore,
    $$P_A(x) = \det\begin{pmatrix} 1-x & 1 & 1 \\ 0 & 1-x & 1 \\ 0 & 0 & 2-x \end{pmatrix} = (1-x)^2 (2-x)$$
    Le radici sono:
    - $\lambda = 1$ con molteplicità algebrica **$m_1 = 2$**;
    - $\lambda = 2$ con molteplicità algebrica **$m_2 = 1$**.
2. **Molteplicità geometriche con $g_\lambda = 3 - \operatorname{rk}(A - \lambda I)$:**
    - Per $\lambda = 1$:
        $$g_1 = 3 - \operatorname{rk}(A - 1\cdot I) = 3 - \operatorname{rk}\begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{pmatrix}$$
        Il minore riquadrato nelle colonne $2, 3$ e righe $1, 2$ è $\det\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = 1 \neq 0$ (e la colonna $1$ è tutta nulla), dunque $\operatorname{rk}(A - I) = 2$ e **$g_1 = 3 - 2 = 1$** ($< m_1$).
    - Per $\lambda = 2$:
        $$g_2 = 3 - \operatorname{rk}(A - 2I) = 3 - \operatorname{rk}\begin{pmatrix} -1 & 1 & 1 \\ 0 & -1 & 1 \\ 0 & 0 & 0 \end{pmatrix} = 3 - 2 = 1$$
    In conclusione: per $\lambda = 1$ si ha $m_1 = 2, g_1 = 1$; per $\lambda = 2$ si ha $m_2 = 1, g_2 = 1$.
:::

### 5. Errori comuni e trappole

1. **Dire che il vettore nullo $\underline{0}$ è un autovettore**
    - *Sbagliato:* scrivere nella base di $V_\lambda$ anche il vettore $(0,0,0)$ o dire che $\underline{0}$ è autovettore perché $A\underline{0} = \lambda\underline{0}$.
    - *Correzione:* nella definizione di autovalore e autovettore *(Lezione 12, p. 7)* è imposto esplicitamente **$v \neq \underline{0}$**! Il vettore nullo $\underline{0}$ appartiene sì all'*autospazio* $V_\lambda$ (che è un sottospazio vettoriale), ma **non è un autovettore**.
2. **Calcolare $g_\lambda$ risolvendo $AX = \underline{0}$ invece di $(A - \lambda I)X = \underline{0}$**
    - *Sbagliato:* dimenticare di sottrarre $\lambda$ sulla diagonale principale quando si costruisce $V_\lambda$.
    - *Correzione:* $V_\lambda = \operatorname{Ker}(f_A - \lambda \operatorname{id})$, quindi la matrice del sistema omogeneo per trovare gli autovettori relativi a $\lambda$ è sempre **$A - \lambda I$** (sottrai $\lambda$ da tutti e soli gli elementi della diagonale principale!).

### 6. Riepilogo

- $A$ è **diagonalizzabile** se è simile a una matrice diagonale $D$.
- $\lambda \in K$ è **autovalore** di $A$ se $\exists v \neq \underline{0}$ con $f_A(v) = \lambda v$ $\iff P_A(\lambda) = 0$.
- La **molteplicità algebrica** $m_\lambda$ è la molteplicità di $\lambda$ come radice di $P_A(x)$.
- L'**autospazio** è $V_\lambda = \operatorname{Ker}(f_A - \lambda \operatorname{id})$ (soluzioni di $(A - \lambda I)X = \underline{0}$); la **molteplicità geometrica** è $g_\lambda = \dim_K V_\lambda = n - \operatorname{rk}(A - \lambda I)$.
- Vale sempre $1 \le g_\lambda \le m_\lambda$ *(in particolare $m_\lambda = 1 \implies g_\lambda = 1$)*.

### 7. Esercizi

Le Lezioni 12 e 13 applicano immediatamente le definizioni di autovalori, autospazi e molteplicità $m_\lambda, g_\lambda$ negli esempi svolti qui sopra (`Esempio 7.3.1` ed `Esempio 7.3.2`) e nei quattro esercizi completi sulla diagonalizzazione della sezione finale [7.4](#sec-7-4).

<!-- section: sec-7-4 | num: 7.4 | title: Teorema sulla diagonalizzabilità (semplicità), calcolo di P e D | kind: section | part: cap-7 -->

### 1. Idea in parole semplici

Eccoci al traguardo del capitolo: quando possiamo "raddrizzare" una matrice quadrata $A$ fino a trasformarla in una matrice diagonale $D$?

Il **Teorema sulla diagonalizzabilità** fissa **due sole condizioni** da controllare:
1. Il polinomio caratteristico $P_A(x)$ non deve avere radici "fuori campo" (se lavoriamo su $K = \mathbb{R}$, **tutte** le sue radici devono essere reali — per esempio $x^2 + 1 = 0$ blocca subito tutto!).
2. Per ogni autovalore $\lambda$, la molteplicità geometrica deve raggiungere quella algebrica: **$g_\lambda = m_\lambda$** (ricorda che per gli autovalori con $m_\lambda = 1$ è già garantito!).

Se entrambe le condizioni passano, come costruiamo concretamente $P$ e $D$? Facilissimo: uniamo le basi di tutti gli autospazi $V_\lambda$ in una **base di autovettori**, mettiamo questi autovettori come **colonne di $P$**, e nell'ordine corrispondente mettiamo i relativi autovalori sulla diagonale di **$D$**: avremo subito $P^{-1} A P = D$! *(Nota d'esame importante: in `Lez14`, p. 4 il docente ricorda che **"semplicità" di un endomorfismo è sinonimo di "diagonalizzabilità"**!)*

### 2. Definizioni e enunciati precisi

:::thm Teorema sulla diagonalizzabilità / semplicità (Lezione 13, p. 4; Lezione 14, p. 4)
Sia $A \in K^{n,n}$. La matrice $A$ è **diagonalizzabile** (su $K$) se e solo se valgono entrambe le condizioni:
1. **tutte le radici** del polinomio caratteristico $P_A(x)$ appartengono al campo $K$;
2. per ogni autovalore $\lambda$ di $A$, la molteplicità geometrica uguaglia la molteplicità algebrica:
    $$g_\lambda = m_\lambda \qquad \forall \lambda \text{ autovalore di } A$$

*(Nota terminologica d'esame, `Lez14` p. 4: studiare la **semplicità** di un endomorfismo $f : V \to V$ significa esattamente studiare la **diagonalizzabilità** della sua matrice associata: **$\text{semplicità} \iff \text{diagonalizzabilità}$**.)*
:::

:::note Nota sugli appunti originali (`Lez13`, pp. 4–6 — convenzione $A = P^{-1}DP$ vs $P^{-1}AP = D$)
- A p. 4 il docente richiama la definizione di diagonalizzabilità scrivendo $A = P^{-1} D P$.
- Subito dopo, nell'esercizio svolto alle pp. 5–6, costruisce la matrice $P$ disponendo una base di autovettori **per colonna** $(v_1\ v_2\ v_3)$ e scrive correttamente **$P^{-1} A P = D$** $\iff AP = PD$ *(che corrisponde ad $A = P D P^{-1}$, equivalente a $A = Q^{-1} D Q$ ponendo $Q = P^{-1}$ per la simmetria della similitudine!)*.

All'esame, mettere una base di autovettori nelle **colonne di $P$** verifica sempre **$P^{-1} A P = D$** (ovvero $AP = PD$), con sulla diagonale di $D$ gli autovalori nello stesso ordine delle colonne di $P$.
:::

### 3. Dimostrazioni

Nella Lezione 13 *(pp. 4–6)* il Teorema sulla diagonalizzabilità viene enunciato senza dimostrazione astratta; viene però esplicitamente dimostrata mediante calcolo matriciale la verifica $P^{-1} A P = D \iff AP = PD$ nel primo esercizio svolto (`Esempio 7.4.1`).

### 4. Esempi svolti

:::example Esempio 7.4.1 — Diagonalizzazione completa della matrice $3 \times 3$ di tutti $1$ (Lezione 13, pp. 4–6)
Diagonalizzare, se possibile, su $\mathbb{R}$ la matrice:

$$A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix} \in \mathbb{R}^{3,3}$$

1. **Polinomio caratteristico e autovalori:**
    Abbiamo $\operatorname{tr} A = 3$, $t_2 A = 0 + 0 + 0 = 0$ e $\det A = 0$, quindi:
    $$P_A(x) = -x^3 + 3x^2 = -x^2(x - 3)$$
    Le radici sono tutte reali: $\lambda_1 = 0$ con $m_0 = 2$ e $\lambda_2 = 3$ con $m_3 = 1$.
2. **Controllo delle molteplicità geometriche:**
    - Poiché $m_3 = 1$, automaticamente **$g_3 = 1 = m_3$** *(dato che $1 \le g_3 \le m_3$)*.
    - Per $\lambda = 0$: $g_0 = 3 - \operatorname{rk}(A - 0I) = 3 - 1 = 2 = m_0$.
    Tutte le radici sono in $\mathbb{R}$ e $g_\lambda = m_\lambda$ per ogni autovalore: **$A$ è diagonalizzabile**!
3. **Basi degli autospazi e costruzione di $P$ e $D$:**
    - **$V_0$ ($\lambda = 0$):** $\begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \underline{0} \iff x + y + z = 0 \implies z = -x - y$. Quindi $(x, y, -x-y) = x(1,0,-1) + y(0,1,-1)$: base di $V_0$ è $v_1 = (1,0,-1)$, $v_2 = (0,1,-1)$.
    - **$V_3$ ($\lambda = 3$):** $(A - 3I)X = \underline{0} \iff \begin{pmatrix} -2 & 1 & 1 \\ 1 & -2 & 1 \\ 1 & 1 & -2 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \underline{0}$. Con le prime $2$ righe $\begin{pmatrix} -2 & 1 & 1 \\ 1 & -2 & 1 \end{pmatrix}$, i minori a segno alterno danno $d_1 = 3, d_2 = 3, d_3 = 3 \implies$ scegliendo $v_3 = (1,1,1)$ si ha $V_3 = \mathcal{L}((1,1,1))$.
    - **Base di autovettori $\mathcal{B}$, matrici $P$ e $D$:**
        $$P = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ -1 & -1 & 1 \end{pmatrix}, \qquad D = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 3 \end{pmatrix} \implies P^{-1} A P = D$$
    - **Verifica ($P^{-1}AP = D \iff AP = PD$):**
        $$AP = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ -1 & -1 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 3 \\ 0 & 0 & 3 \\ 0 & 0 & 3 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ -1 & -1 & 1 \end{pmatrix}\begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 3 \end{pmatrix} = PD$$
:::

:::note Nota sugli appunti originali (`Lez13`, p. 6)
All'inizio di p. 6, subito dopo aver risolto il sistema per $V_3$, il PDF manoscritto scrive per svista di trascrizione **$V_0 = \mathcal{L}((1,1,1))$** al posto di **$V_3 = \mathcal{L}((1,1,1))$** (subito dopo infatti indica il vettore correttamente con $v_3 = (1,1,1)$ e lo abbina all'autovalore $3$ in $D$).
:::

:::example Esempio 7.4.2 — Due esempi classici di matrici NON diagonalizzabili su $\mathbb{R}$ (Lezione 13, p. 7)
1. **Fallisce la condizione (2): $g_\lambda < m_\lambda$:** sia $A = \begin{pmatrix} 4 & 1 \\ 0 & 4 \end{pmatrix} \in \mathbb{R}^{2,2}$.
    - $P_A(x) = \det\begin{pmatrix} 4-x & 1 \\ 0 & 4-x \end{pmatrix} = (4-x)^2 \implies$ unico autovalore $\lambda = 4$ con $m_4 = 2$ (radici tutte in $\mathbb{R}$).
    - $g_4 = 2 - \operatorname{rk}(A - 4I) = 2 - \operatorname{rk}\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = 2 - 1 = 1 < m_4 = 2$: dunque $A$ **non è diagonalizzabile**.
2. **Fallisce la condizione (1): radici non in $K = \mathbb{R}$:** sia $A = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \in \mathbb{R}^{2,2}$ (con $K = \mathbb{R}$).
    - $P_A(x) = \det\begin{pmatrix} -x & 1 \\ -1 & -x \end{pmatrix} = x^2 + 1$.
    - L'equazione $x^2 + 1 = 0$ non ha soluzioni in $\mathbb{R}$: le radici del polinomio caratteristico ($\pm i$) non stanno in $K = \mathbb{R}$, quindi $A$ **non è diagonalizzabile su $\mathbb{R}$**. *(Nota: su $K = \mathbb{C}$ avrebbe invece $2$ autovalori distinti $i$ e $-i$, e quindi su $\mathbb{C}$ sarebbe diagonalizzabile!)*
:::

:::example Esempio 7.4.3 — Diagonalizzazione $3 \times 3$ con autovalore doppio $\lambda = 2$ e Ruffini (Lezione 13, pp. 8–10)
Diagonalizzare, se possibile, la matrice:

$$A = \begin{pmatrix} 3 & 2 & 3 \\ -1 & 0 & -3 \\ 1 & 2 & 5 \end{pmatrix} \in \mathbb{R}^{3,3}$$

1. **Polinomio caratteristico:**
    - $\operatorname{tr} A = 3 + 0 + 5 = 8$;
    - $t_2 A = \det\begin{pmatrix} 3 & 2 \\ -1 & 0 \end{pmatrix} + \det\begin{pmatrix} 3 & 3 \\ 1 & 5 \end{pmatrix} + \det\begin{pmatrix} 0 & -3 \\ 2 & 5 \end{pmatrix} = 2 + 12 + 6 = 20$;
    - $\det A = 0 - 6 - 6 - 0 + 18 + 10 = 16$.
    Quindi $P_A(x) = -x^3 + 8x^2 - 20x + 16$.
    Cerchiamo le radici di $x^3 - 8x^2 + 20x - 16 = 0$: per $x = 2$ si ha $8 - 32 + 40 - 16 = 0$. Con Ruffini scomponiamo in $P_A(x) = -(x-2)(x^2 - 6x + 8)$; le radici di $x^2 - 6x + 8 = 0$ sono $x = 3 \pm 1 \in \{2, 4\}$, quindi:
    $$P_A(x) = -(x - 2)^2 (x - 4)$$
    Autovalori: $\lambda = 2$ ($m_2 = 2$) e $\lambda = 4$ ($m_4 = 1 = g_4$).
2. **Controllo di $g_2$:**
    $$g_2 = 3 - \operatorname{rk}(A - 2I) = 3 - \operatorname{rk}\begin{pmatrix} 1 & 2 & 3 \\ -1 & -2 & -3 \\ 1 & 2 & 3 \end{pmatrix} = 3 - 1 = 2 = m_2$$
    Tutte le radici sono reali e $g_\lambda = m_\lambda$: **$A$ è diagonalizzabile**!
3. **Basi degli autospazi e costruzione di $P$ e $D$:**
    - **$V_2$:** dalla riga $x + 2y + 3z = 0 \implies x = -2y - 3z$: una base di $V_2$ è $\{v_1, v_2\} = \{(-2,1,0),\ (-3,0,1)\}$.
    - **$V_4$:** $(A - 4I) = \begin{pmatrix} -1 & 2 & 3 \\ -1 & -4 & -3 \\ 1 & 2 & 1 \end{pmatrix} \xrightarrow{\substack{R_2 \mapsto R_2 - R_1 \\ R_3 \mapsto R_3 + R_1}} \begin{pmatrix} -1 & 2 & 3 \\ 0 & -6 & -6 \\ 0 & 4 & 4 \end{pmatrix} \longrightarrow \begin{pmatrix} -1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix}$. Da $y = -z$ e $-x + 2(-z) + 3z = 0 \implies x = z$ *(oppure in funzione di $y$: $x=-y, z=-y$, quindi $(-y, y, -y) = -y(1,-1,1)$)*: una base di $V_4$ è $\{v_3\} = \{(1,-1,1)\}$.
    - **Matrici finali:**
        $$D = \begin{pmatrix} 2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 4 \end{pmatrix}, \qquad P = \begin{pmatrix} -2 & -3 & 1 \\ 1 & 0 & -1 \\ 0 & 1 & 1 \end{pmatrix} \implies P^{-1} A P = D$$
:::

:::note Nota sugli appunti originali (`Lez13`, p. 8)
Nel primo determinante del calcolo di $t_2 A$ è scritto $-3$ anziché $3$ in posizione $(1,1)$ della sottomatrice, ma il valore del minore calcolato subito dopo ($2$) è corretto perché $3\cdot 0 - 2(-1) = +2$.
:::

### 5. Errori comuni e trappole

1. **Controllare solo $g_\lambda = m_\lambda$ dimenticando di verificare che le radici stiano in $K$**
    - *Sbagliato:* su $\mathbb{R}$, trovare $P_A(x) = -(x-1)(x^2+1)$ e dire "1 ha $m_1=g_1=1$, quindi è diagonalizzabile".
    - *Correzione:* la condizione **(1)** del Teorema sulla diagonalizzabilità *(Lezione 13, p. 4)* esige che **tutte** le radici di $P_A(x)$ appartengano al campo $K$: su $\mathbb{R}$, un fattore quadratico con $\Delta < 0$ rende automaticamente la matrice **non diagonalizzabile**!
2. **Sbagliare l'allineamento tra le colonne di $P$ e la diagonale di $D$**
    - *Sbagliato:* mettere nella prima colonna di $P$ un autovettore di $\lambda = 3$ e mettere $0$ in posizione $(1,1)$ di $D$.
    - *Correzione:* $AP = PD$ significa che la $j$-esima colonna di $P$ viene moltiplicata per il $j$-esimo numero diagonale di $D$: ogni autovettore nella colonna $j$ di $P$ deve corrispondere esattamente all'autovalore nella posizione $(j,j)$ di $D$!

### 6. Riepilogo

- **Teorema sulla diagonalizzabilità:** $A \in K^{n,n}$ è diagonalizzabile (sinonimo: **semplice**) $\iff$ tutte le radici di $P_A(x)$ stanno in $K$ **e** $g_\lambda = m_\lambda$ per ogni autovalore $\lambda$.
- Se tutte le $n$ radici di $P_A(x)$ sono in $K$ e sono **distinte**, allora $m_\lambda = g_\lambda = 1$ per tutte: la matrice è **automaticamente diagonalizzabile**.
- Per trovare $P$ e $D$ ($P^{-1}AP = D$): trova una base per ogni autospazio $V_\lambda$, metti tutti gli $n$ autovettori come **colonne di $P$**, e scrivi sulla diagonale di $D$ i rispettivi autovalori nello stesso ordine.
- Per controllare i conti senza calcolare $P^{-1}$: verifica che **$AP = PD$** (e $\det P \neq 0$).

### 7. Esercizi

La Lezione 13 *(pp. 4–10)* presenta e risolve i quattro esercizi completi riportati sopra (`Esempi 7.4.1–7.4.3`), prima di passare subito all'esame reale del 26/1/2026: tutti gli **esercizi e problemi d'esame completi** sulla diagonalizzazione parametrica, la semplicità e la composizione sono trattati integralmente passo-passo nel prossimo Capitolo 8!
