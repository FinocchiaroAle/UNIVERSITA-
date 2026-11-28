<!-- part: cap-5 | num: 5 | label: CAPITOLO 5 | title: Spazi vettoriali, sottospazi, basi e dimensione | refs: Fonti: Lezione 7 (26/10/2026, pp. 6–11), Lezione 8 (28/10/2026, pp. 1–9), Lezione 9 (4/11/2026, pp. 1–9) e Lezione 10 (9/11/2026, pp. 1–3) -->

<!-- section: sec-5-1 | num: 5.1 | title: K-spazi vettoriali e legge di annullamento del prodotto | kind: section | part: cap-5 -->

### 1. Idea in parole semplici

Nel Capitolo 2 abbiamo visto due operazioni fondamentali sulle matrici $K^{m,n}$: si possono **sommare** tra loro (formando un gruppo abeliano) e si possono **moltiplicare per uno scalare** di $K$. I matematici hanno notato che le stesse identiche proprietà compaiono dappertutto: nei vettori del piano $\mathbb{R}^2$, nelle terne $\mathbb{R}^3$, nelle soluzioni di un sistema omogeneo, nei polinomi!

Nasce così il concetto unificante di **$K$-spazio vettoriale**: qualsiasi insieme $V$ dove puoi sommare elementi (*vettori*) e scalarli con numeri del campo $K$ (*scalari*) rispettando le $4$ regole naturali di buon comportamento. Una conseguenza immediata e utilissima di questi assiomi è la **legge di annullamento del prodotto** scalare-vettore: $av = \underline{0}$ se e solo se è nullo lo scalare $a$ oppure è nullo il vettore $v$ (a differenza di quanto succedeva nel prodotto tra due matrici!).

### 2. Definizioni e enunciati precisi

:::def Definizione — $K$-spazio vettoriale (Lezione 7, p. 6)
Sia $(K, +, \cdot)$ un campo e sia $(V, +)$ un gruppo abeliano. Chiameremo **scalari** gli elementi di $K$ e **vettori** gli elementi di $V$.

Diremo che $V$ è un **$K$-spazio vettoriale** se esiste un'operazione di prodotto tra uno scalare ed un vettore:

$$K \times V \longrightarrow V$$

che gode delle seguenti $4$ proprietà:
1. $(a + b)v = av + bv \qquad \forall a, b \in K,\ \forall v \in V$;
2. $a(u + v) = au + av \qquad \forall a \in K,\ \forall u, v \in V$;
3. $(ab)v = a(bv) \qquad \forall a, b \in K,\ \forall v \in V$;
4. $1v = v \qquad \forall v \in V$, dove $1$ è l'unità del campo $K$.
:::

**Notazioni ufficiali *(Lezione 7, pp. 6–7)*:**
Sia $V$ un $K$-spazio vettoriale:
- con $0$ indichiamo l'elemento neutro di $K$ rispetto all'addizione *(lo scalare zero)*;
- con $1$ indichiamo l'elemento neutro di $K$ rispetto alla moltiplicazione *(l'unità di $K$)*;
- con $\underline{0}$ indichiamo l'elemento neutro di $(V, +)$, chiamato **vettore nullo** *(spesso indicato più esplicitamente con $\underline{0}_V$ quando convivono più spazi vettoriali)*.

:::thm Proposizione — Legge di annullamento del prodotto in un $K$-spazio vettoriale (Lezione 7, p. 7)
Sia $V$ un $K$-spazio vettoriale, sia $a \in K$ e sia $v \in V$. Allora:

$$av = \underline{0} \iff a = 0 \text{ oppure } v = \underline{0}$$
:::

### 3. Dimostrazioni

:::proof Dimostrazione — Legge di annullamento del prodotto: $av = \underline{0} \iff a = 0 \lor v = \underline{0}$ (Lezione 7, p. 7)
**Idea di fondo:** nel verso ($\Leftarrow$) sfruttiamo $0 = 0 + 0$ e $\underline{0} = \underline{0} + \underline{0}$ con le proprietà distributive (1) e (2) per cancellare un termine uguale da ambo i lati. Nel verso ($\Rightarrow$), se $a \neq 0$, essendo $K$ un campo possiamo moltiplicare entrambi i lati per $a^{-1}$.

- **($\Leftarrow$) Se $a = 0$ oppure $v = \underline{0}$:**
    - Se $a = 0$, usando la proprietà (1) e $0 = 0 + 0$ in $K$:
        $$0v = (0 + 0)v = 0v + 0v$$
        Cancellando $0v$ in entrambi i membri nel gruppo $(V, +)$ si ottiene $\underline{0} = 0v$.
    - Se $v = \underline{0}$, usando la proprietà (2) e $\underline{0} = \underline{0} + \underline{0}$ in $V$:
        $$a\underline{0} = a(\underline{0} + \underline{0}) = a\underline{0} + a\underline{0}$$
        Cancellando $a\underline{0}$ in entrambi i membri si ottiene $\underline{0} = a\underline{0}$.

- **($\Rightarrow$) Supponiamo che $av = \underline{0}$:**
    - Se $a = 0$, la tesi ($a = 0$ oppure $v = \underline{0}$) è già verificata.
    - Se $a \neq 0$, poiché $K$ è un campo, $a$ è invertibile ed esiste $a^{-1} \in K$. Moltiplichiamo entrambi i membri di $av = \underline{0}$ per $a^{-1}$:
        $$a^{-1}(av) = a^{-1}\underline{0} \implies (a^{-1}a)v = \underline{0} \quad \text{(per la prop. 3 e la prima parte)}$$
        $$\implies 1v = \underline{0} \implies v = \underline{0} \quad \text{(per la prop. 4)}$$
:::

### 4. Esempi svolti

:::example Esempio 5.1.1 — Gli spazi di matrici $K^{m,n}$ e di $n$-uple $K^n$ (Lezione 7, pp. 6–7; Lezione 9, p. 2)
- Per ogni campo $K$ e per ogni $m, n > 0$, l'insieme **$K^{m,n}$** dotato dell'addizione tra matrici e del prodotto di uno scalare per una matrice è un $K$-spazio vettoriale: nella Sezione [2.1](#sec-2-1) abbiamo provato che $(K^{m,n}, +)$ è un gruppo abeliano e nella Sezione [2.2](#sec-2-2) abbiamo elencato esattamente i $4$ assiomi del prodotto scalare per matrice!
- In particolare, scegliendo $m = 1$ (o $n = 1$), lo spazio **$K^n = K^{1,n}$** (oppure $K^{n,1}$) delle $n$-uple di elementi di $K$ (come $\mathbb{R}^2, \mathbb{R}^3, \mathbb{R}^4$) è un $K$-spazio vettoriale.
:::

### 5. Errori comuni e trappole

1. **Confondere lo scalare $0 \in K$ con il vettore nullo $\underline{0} \in V$**
    - *Sbagliato:* scrivere $a = \underline{0}$ o $0 \cdot v = 0$ in $\mathbb{R}^3$ dimenticando che il risultato è una terna $(0,0,0)$.
    - *Correzione:* il prodotto $av$ sta sempre nello spazio vettoriale **$V$**, quindi $0v$ è il **vettore nullo $\underline{0}$** (per esempio $(0,0,0)$ in $\mathbb{R}^3$, o la matrice nulla $O$ in $K^{m,n}$), mai un semplice numero!
2. **Pensare che il prodotto in un $K$-spazio vettoriale significhi moltiplicare due vettori**
    - *Sbagliato:* cercare assiomi su "$u \cdot v$" per due vettori $u, v \in V$.
    - *Correzione:* la definizione di spazio vettoriale prevede l'addizione interna $V \times V \to V$ e il prodotto esterno $K \times V \to V$ (scalare $\times$ vettore); in generale non c'è alcun prodotto tra due vettori.

### 6. Riepilogo

- Un **$K$-spazio vettoriale** è un gruppo abeliano $(V,+)$ dotato di un prodotto $K \times V \to V$ con i $4$ assiomi (due distributività, associatività mista e $1v = v$).
- Si distingue sempre lo scalare $0 \in K$ dal **vettore nullo** $\underline{0} \in V$.
- $K^{m,n}$ (e in particolare $K^n$) è l'esempio modello di $K$-spazio vettoriale.
- **Legge di annullamento del prodotto:** $av = \underline{0} \iff a = 0$ oppure $v = \underline{0}$.

### 7. Esercizi

La Lezione 7 *(pp. 6–7)* non contiene esercizi numerici per casa su questa parte introduttiva; il primo esercizio sugli spazi vettoriali e i sottospazi compare immediatamente nella sezione successiva [5.2](#sec-5-2).

<!-- section: sec-5-2 | num: 5.2 | title: Sottospazi vettoriali, sistemi omogenei, intersezione e somma | kind: section | part: cap-5 -->

### 1. Idea in parole semplici

Dentro un grande spazio vettoriale $V$ (come tutto lo spazio $\mathbb{R}^3$), alcuni sottoinsiemi speciali $S \subseteq V$ — ad esempio un piano o una retta **passanti per l'origine** $(0,0,0)$ — formano essi stessi uno spazio vettoriale in miniatura usando le stesse identiche operazioni di $V$: sono i **sottospazi vettoriali**.

Per verificare se $S \subseteq V$ è un sottospazio, non serve ricontrollare da zero tutti gli assiomi: basta un test lampo in **2 passi** (*criterio di sottospazio*): contiene l'origine $\underline{0}$, ed è chiuso rispetto a combinazioni lineari $as_1 + bs_2$. Scopriamo inoltre tre modi sicuri per fabbricare sottospazi: risolvere un sistema omogeneo $AX = \underline{0}$, fare l'intersezione $U \cap W$ e fare la somma $U + W$.

### 2. Definizioni e enunciati precisi

:::def Definizione — Sottospazio vettoriale (Lezione 7, p. 8)
Sia $V$ un $K$-spazio vettoriale e sia $S \subseteq V$. Diremo che $S$ è un **sottospazio** di $V$ se $S$ è un $K$-spazio vettoriale rispetto alle stesse operazioni definite in $V$.
:::

:::thm Proposizione — Criterio di riconoscimento dei sottospazi (Lezione 7, p. 8)
Sia $V$ un $K$-spazio vettoriale e sia $S \subseteq V$. Allora $S$ è un sottospazio di $V$ se e solo se valgono entrambe le condizioni:
1. $\underline{0} \in S$;
2. $S$ è **"chiuso" rispetto alle combinazioni lineari**, cioè $\forall a, b \in K$ e $\forall s_1, s_2 \in S$, risulta $a s_1 + b s_2 \in S$.
:::

:::thm Proposizione — Spazio delle soluzioni di un sistema omogeneo, intersezione e somma di sottospazi (Lezione 7, pp. 9–10; Lezione 8, p. 1)
1. **Sistemi lineari omogenei (`Lez07`, p. 9):** sia $A \in K^{m,n}$. L'insieme delle soluzioni del sistema omogeneo $AX = \underline{0}$:
    $$S = \{ X \in K^{n,1} = K^n \mid AX = \underline{0} \}$$
    è un **sottospazio** di $K^n$.
2. **Intersezione (`Lez07`, p. 10):** se $U$ e $W$ sono sottospazi di $V$, allora l'intersezione $U \cap W$ è un **sottospazio** di $V$.
3. **Somma (`Lez08`, p. 1):** siano $U$ e $W$ due sottospazi di $V$. Definiamo la **somma** dei due sottospazi come:
    $$U + W \stackrel{\text{DEF}}{=} \{ u + w \mid u \in U \text{ e } w \in W \}$$
    Allora $U + W$ è un **sottospazio** di $V$.
:::

### 3. Dimostrazioni

:::proof Dimostrazione 1 — Le soluzioni di $AX = \underline{0}$ formano un sottospazio di $K^n$ (Lezione 7, p. 9)
**Idea di fondo:** verifichiamo le due condizioni del criterio di sottospazio usando la linearità del prodotto matrice-colonna.

Sia $S = \{ X \in K^{n,1} \mid AX = \underline{0} \}$ con $A \in K^{m,n}$.
1. **$\underline{0} \in S$:** poiché $A\underline{0} = \underline{0}$, il vettore nullo soddisfa l'equazione e quindi $\underline{0} \in S$.
2. **Chiusura rispetto alle combinazioni lineari:** siano $X_1, X_2 \in S$ (dunque $AX_1 = \underline{0}$ e $AX_2 = \underline{0}$) e $a, b \in K$. Calcoliamo $A(aX_1 + bX_2)$ usando distributività e compatibilità con gli scalari:
    $$A(aX_1 + bX_2) = a(AX_1) + b(AX_2) = a\underline{0} + b\underline{0} = \underline{0} \implies aX_1 + bX_2 \in S$$

Dunque $S$ è un sottospazio di $K^n$.
:::

:::proof Dimostrazione 2 — $U \cap W$ è un sottospazio di $V$ (Lezione 7, p. 10)
**Idea di fondo:** un elemento appartiene a $U \cap W$ se e solo se sta sia in $U$ che in $W$; poiché entrambi sono sottospazi, entrambi contengono $\underline{0}$ ed entrambi trattengono le combinazioni lineari.

Siano $U$ e $W$ sottospazi di $V$:
1. Poiché $U$ e $W$ sono sottospazi, $\underline{0} \in U$ e $\underline{0} \in W$, quindi $\underline{0} \in U \cap W$.
2. Siano $a, b \in K$ e $v_1, v_2 \in U \cap W$: allora $v_1, v_2 \in U$ e $v_1, v_2 \in W$.
    - Poiché $U$ è sottospazio, $av_1 + bv_2 \in U$;
    - poiché $W$ è sottospazio, $av_1 + bv_2 \in W$.
    Di conseguenza $av_1 + bv_2 \in U \cap W$. Quindi $U \cap W$ è un sottospazio di $V$.
:::

:::proof Dimostrazione 3 — $U + W$ è un sottospazio di $V$ (Lezione 8, p. 1)
**Idea di fondo:** scriviamo $\underline{0}$ come $\underline{0} + \underline{0}$ e raggruppiamo opportunamente i termini di $U$ insieme a quelli di $U$, e i termini di $W$ insieme a quelli di $W$.

1. **$\underline{0} \in U + W$:** per ipotesi $U$ e $W$ sono sottospazi di $V$, quindi $\underline{0} \in U$ e $\underline{0} \in W$. Scrivendo $\underline{0} = \underbrace{\underline{0}}_{\in U} + \underbrace{\underline{0}}_{\in W}$, segue che $\underline{0} \in U + W$.
2. **Chiusura rispetto alle combinazioni lineari:** siano $a, b \in K$ e $v_1, v_2 \in U + W$. Per definizione esistono $u_1, u_2 \in U$ e $w_1, w_2 \in W$ tali che $v_1 = u_1 + w_1$ e $v_2 = u_2 + w_2$. Calcoliamo:
    $$av_1 + bv_2 = a(u_1 + w_1) + b(u_2 + w_2) = \underbrace{(au_1 + bu_2)}_{\in U} + \underbrace{(aw_1 + bw_2)}_{\in W} \in U + W$$
    *(infatti $au_1 + bu_2 \in U$ perché $U$ è sottospazio, e $aw_1 + bw_2 \in W$ perché $W$ è sottospazio)*.

Pertanto $U + W$ è un sottospazio di $V$.
:::

:::note Nota sugli appunti originali (`Lez07`, pp. 10–11)
1. A p. 10 nella penultima riga della Dimostrazione 2 scrive «$U$ è sottospazio $\implies av_1 + bv_2 \in V$»: si tratta di una svista grafica per $av_1 + bv_2 \in U$.
2. A p. 11, nell'esempio su $U \cap W$, scrive due volte $(x,y,z) \in \mathbb{R}$ anziché $(x,y,z) \in \mathbb{R}^3$ nella definizione degli insiemi $U$ e $W$ (subito prima di dire correttamente «è un sottospazio di $\mathbb{R}^3$»).
:::

### 4. Esempi svolti

:::example Esempio 5.2.1 — Due non-sottospazi di $\mathbb{R}^2$ (Lezione 7, pp. 8–9)
1. **Esempio 1 (p. 8):** sia $S = \{(x,y) \in \mathbb{R}^2 \mid x + y = 1\}$. Controlliamo la condizione (1): $\underline{0} = (0,0) \notin S$ perché $0 + 0 = 0 \neq 1$. Dunque $S$ **non è un sottospazio** di $\mathbb{R}^2$.
2. **Esempio 2 (p. 9):** sia $S = \{(x,y) \in \mathbb{R}^2 \mid x^2 - y = 0\}$. Qui $\underline{0} = (0,0) \in S$ perché $0^2 - 0 = 0$, quindi la condizione (1) passa! Controlliamo però la (2): $s_1 = (1,1) \in S$ ($1^2 - 1 = 0$), ma moltiplicando per $2$ si ha $2s_1 = (2,2) \notin S$ perché $2^2 - 2 = 2 \neq 0$. Dunque $S$ non è chiuso rispetto alle combinazioni lineari e **non è un sottospazio** di $\mathbb{R}^2$.
:::

:::example Esempio 5.2.2 — Sottospazio descritto da un sistema lineare omogeneo in $\mathbb{R}^3$ (Lezione 7, pp. 9–11)
Consideriamo in $\mathbb{R}^3$:

$$S = \{(x,y,z) \in \mathbb{R}^3 \mid x + y + z = 0,\ 2x - y + z = 0\}$$

Esso è l'intersezione $U \cap W$ dei due sottospazi $U = \{(x,y,z)\in\mathbb{R}^3 \mid x+y+z=0\}$ e $W = \{(x,y,z)\in\mathbb{R}^3 \mid 2x-y+z=0\}$ *(p. 11)*, nonché lo spazio delle soluzioni di $A X = \underline{0}$ con $A = \begin{pmatrix} 1 & 1 & 1 \\ 2 & -1 & 1 \end{pmatrix}$ *(p. 9)*: dunque $S$ è un sottospazio di $\mathbb{R}^3$. Risolviamolo *(p. 10)*:

$$\begin{cases} x + y + z = 0 \\ 2x - y + z = 0 \end{cases} \iff \begin{cases} x + (2x+z) + z = 0 \\ y = 2x + z \end{cases} \iff \begin{cases} 3x + 2z = 0 \\ y = 2x + z \end{cases} \iff \begin{cases} z = -\frac{3}{2}x \\ y = 2x - \frac{3}{2}x = \frac{x}{2} \end{cases}$$

Quindi:

$$S = \left\{ \left(x,\ \frac{x}{2},\ -\frac{3}{2}x\right) \;\middle|\; x \in \mathbb{R} \right\} = \left\{ \frac{1}{2}x\,(2, 1, -3) \;\middle|\; x \in \mathbb{R} \right\}$$

cioè $S$ è l'insieme di **tutti i multipli** del vettore $(2, 1, -3)$.
:::

### 5. Errori comuni e trappole

1. **Fermarsi dopo aver verificato che $\underline{0} \in S$**
    - *Sbagliato:* vedere $(0,0) \in S$ in $x^2 - y = 0$ (Esempio 5.2.1) e concludere subito che $S$ è un sottospazio.
    - *Correzione:* la condizione $\underline{0} \in S$ serve solo a *escludere* subito i non-sottospazi come $x+y=1$; per dimostrare che $S$ **è** un sottospazio bisogna sempre provare anche la chiusura per combinazioni lineari $as_1 + bs_2 \in S$.
2. **Confondere l'unione $U \cup W$ con la somma $U + W$**
    - *Sbagliato:* pensare che se $U$ e $W$ sono sottospazi, allora anche l'unione insiemistica $U \cup W$ sia un sottospazio.
    - *Correzione:* l'intersezione $U \cap W$ e la **somma** $U + W$ sono sempre sottospazi, mentre l'unione $U \cup W$ in generale **non** è chiusa per somma (ad esempio due rette distinte in $\mathbb{R}^2$ per l'origine: la somma di un punto su una retta e un punto sull'altra esce da entrambe le rette, ma sta in $U + W$).

### 6. Riepilogo

- $S \subseteq V$ è un **sottospazio** di $V$ $\iff \underline{0} \in S$ e $as_1 + bs_2 \in S$ per tutti gli $a,b \in K$, $s_1, s_2 \in S$.
- Se un sistema omogeneo o un insieme di equazioni contiene termini noti non nulli (es. $x+y=1$) o termini non lineari (es. $x^2-y=0$), non è un sottospazio.
- L'insieme delle soluzioni di qualunque sistema lineare omogeneo $AX = \underline{0}$ è un sottospazio di $K^n$.
- L'intersezione $U \cap W$ di sottospazi è un sottospazio di $V$.
- La somma $U + W = \{u+w \mid u\in U, w\in W\}$ di sottospazi è un sottospazio di $V$.

### 7. Esercizi

La Lezione 7 *(pp. 8–11)* e l'inizio della Lezione 8 *(p. 1)* illustrano i sottospazi tramite gli esempi svolti appena esaminati (`Esempio 5.2.1` ed `Esempio 5.2.2`); gli esercizi per casa sulle nozioni introdotte con i sottospazi sono assegnati subito dopo l'introduzione di generatori e basi nelle sezioni [5.4](#sec-5-4), [5.5](#sec-5-5) e [5.7](#sec-5-7).

<!-- section: sec-5-3 | num: 5.3 | title: Combinazioni lineari, sottospazio generato, generatori e indipendenza lineare | kind: section | part: cap-5 -->

### 1. Idea in parole semplici

Nel sottospazio dell'Esempio 5.2.2 abbiamo visto che tutti i vettori di $S$ erano semplicemente i multipli di un unico vettore $(2,1,-3)$. Questo ci dà l'idea fondamentale di come si "generano" gli spazi vettoriali a partire da pochi mattoni:

- Fare una **combinazione lineare** significa mescolare alcuni vettori moltiplicandoli per numeri e sommandoli: $a_1 v_1 + \dots + a_r v_r$.
- L'insieme di tutte le possibili combinazioni lineari di un sottoinsieme $S$ forma il **sottospazio generato** $\mathcal{L}(S)$.
- Un insieme di **generatori** basta a ricostruire l'intero spazio $V$; ma se dentro quell'elenco ci sono "doppioni" ottenibili dagli altri (vettori **linearmente dipendenti**), li possiamo scartare fino a restare con un gruppo essenziale in cui nessuno è superfluo (**linearmente indipendenti** / **insieme libero**).

### 2. Definizioni e enunciati precisi

:::def Definizione — Combinazione lineare e sottospazio generato $\mathcal{L}(S)$ (Lezione 8, pp. 1–2)
Sia $V$ un $K$-spazio vettoriale.
- Dati scalari $a_1, \dots, a_r \in K$ e vettori $v_1, \dots, v_r \in V$, il vettore
    $$a_1 v_1 + \dots + a_r v_r = \sum_{i=1}^r a_i v_i$$
    si chiama **combinazione lineare** dei vettori $v_1, \dots, v_r$.
- Dato un sottoinsieme non vuoto $S \subseteq V$ ($S \neq \emptyset$), poniamo:
    $$\mathcal{L}(S) \stackrel{\text{DEF}}{=} \{\text{tutte le possibili combinazioni lineari di vettori appartenenti ad } S\}$$
    Quindi $v \in \mathcal{L}(S) \iff v = \sum_{i=1}^r a_i s_i$ per opportuni $s_i \in S$ e $a_i \in K$.
:::

:::thm Proposizione — $\mathcal{L}(S)$ è un sottospazio di $V$ (Lezione 8, p. 2)
Sia $V$ un $K$-spazio vettoriale e sia $S \subseteq V$ con $S \neq \emptyset$. Allora $\mathcal{L}(S)$ è un **sottospazio** di $V$.
:::

:::def Definizione — Insieme di generatori e spazio finitamente generato (Lezione 8, p. 4)
Sia $V$ un $K$-spazio vettoriale e sia $S \subseteq V$, $S \neq \emptyset$.
- Se $V = \mathcal{L}(S)$, allora $S$ è detto **insieme di generatori** di $V$.
- Diremo che $V$ è **finitamente generato** se $V = \mathcal{L}(S)$ con $S$ **insieme finito**, cioè quando $V$ può essere generato da un numero finito di vettori.
:::

:::def Definizione — Dipendenza e indipendenza lineare, insieme libero (Lezione 8, p. 5)
Sia $V$ un $K$-spazio vettoriale e siano $v_1, \dots, v_r \in V$.
- Diremo che $v_1, \dots, v_r$ sono **linearmente dipendenti** se esistono scalari $a_1, \dots, a_r \in K$, **non tutti nulli**, tali che:
    $$a_1 v_1 + \dots + a_r v_r = \underline{0}$$
- Altrimenti *(cioè se l'unico modo per ottenere $\underline{0}$ è scegliere $a_1 = a_2 = \dots = a_r = 0$)* si diranno **linearmente indipendenti**.
- Un sottoinsieme $S \subseteq V$ si dice **insieme libero** se i vettori di $S$ sono linearmente indipendenti.
:::

:::thm Criterio di indipendenza lineare (Lezione 8, p. 6)
Sia $V$ un $K$-spazio vettoriale e siano $v_1, \dots, v_r \in V$. I vettori $v_1, \dots, v_r$ sono **linearmente indipendenti** se e solo se:
1. $v_1 \neq \underline{0}$;
2. $v_i \notin \mathcal{L}(v_1, \dots, v_{i-1}) \qquad \text{per ogni } 2 \le i \le r$.
:::

### 3. Dimostrazioni

:::proof Dimostrazione — $\mathcal{L}(S)$ è un sottospazio di $V$ (Lezione 8, p. 2)
**Idea di fondo:** essendo $S \neq \emptyset$, peschiamo un qualsiasi elemento $s \in S$ e lo moltiplichiamo per $0 \in K$ per avere $\underline{0} \in \mathcal{L}(S)$; poi prendiamo due combinazioni lineari finite in $\mathcal{L}(S)$, le moltiplichiamo per $a_1, a_2 \in K$ e le sommiamo ottenendo un'unica combinazione lineare di elementi di $S$.

1. **$\underline{0} \in \mathcal{L}(S)$:** poiché $S \neq \emptyset$, esiste almeno un vettore $s \in S$. Prendendo lo scalare $0 \in K$, abbiamo $0s = \underline{0} \in \mathcal{L}(S)$.
2. **Chiusura rispetto alle combinazioni lineari:** siano $\alpha_1, \alpha_2 \in K$ *(indichiamo così i due scalari esterni per distinguerli dai coefficienti interni di $v_1$)* e siano $v_1, v_2 \in \mathcal{L}(S)$. Allora $v_1 = \sum_{i=1}^r a_i s_i$ e $v_2 = \sum_{j=1}^h b_j t_j$ con $s_i, t_j \in S$ e $a_i, b_j \in K$. Calcoliamo:
    $$\alpha_1 v_1 + \alpha_2 v_2 = \alpha_1 \sum_{i=1}^r a_i s_i + \alpha_2 \sum_{j=1}^h b_j t_j = \sum_{i=1}^r (\alpha_1 a_i)s_i + \sum_{j=1}^h (\alpha_2 b_j)t_j \in \mathcal{L}(S)$$
    poiché è ancora una combinazione lineare finita di elementi di $S$.

Pertanto $\mathcal{L}(S)$ è un sottospazio di $V$.
:::

:::note Nota sugli appunti originali (`Lez08`, p. 2 e p. 5)
1. A p. 2 nei lucidi il docente scrive sia i due coefficienti esterni che la prima sommatoria con i nomi $a_1, a_2$ e $a_i$ (ponendo $a_1 v_1 + a_2 v_2 = a_1 \sum a_i s_i + \dots$): nella nostra dimostrazione abbiamo chiamato $\alpha_1, \alpha_2$ i due coefficienti esterni così da evitare qualsiasi omonimia con gli $a_i$.
2. A p. 5, Esempio 1, l'equazione di dipendenza tra $v_1=(1,2,3)$ e $v_2=(2,4,6)$ ha avuto una correzione manoscritta dal prof sul segno davanti a $v_2$: la combinazione corretta è $2v_1 - v_2 = \underline{0}$.
:::

### 4. Esempi svolti

:::example Esempio 5.3.1 — Combinazione lineare e passaggio forma parametrica $\to$ cartesiana (Lezione 8, pp. 2–4)
1. **Combinazione lineare in $\mathbb{R}^3$ (p. 2):** con $a_1 = 2, a_2 = 5$, $v_1 = (1,1,0)$ e $v_2 = (0,1,1)$:
    $$a_1 v_1 + a_2 v_2 = 2(1,1,0) + 5(0,1,1) = (2,2,0) + (0,5,5) = (2,7,5)$$
    Quindi $(2,7,5) \in \mathcal{L}((1,1,0), (0,1,1))$.
2. **Sottospazio generato da un vettore (p. 3):** per $S = \{v\}$ con $v = (1,2,2) \in \mathbb{R}^3$:
    $$\mathcal{L}((1,2,2)) = \{a(1,2,2) \mid a \in \mathbb{R}\} = \{(a, 2a, 2a) \mid a \in \mathbb{R}\}$$
    Per passare alle equazioni cartesiane poniamo $(x,y,z) = (a, 2a, 2a)$ ed eliminiamo il parametro $a$:
    $$\begin{cases} x = a \\ y = 2a \\ z = 2a \end{cases} \implies \begin{cases} x = a \\ y = 2x \\ z = 2x \end{cases} \implies \begin{cases} 2x - y = 0 \\ 2x - z = 0 \end{cases}$$
    Quindi $\mathcal{L}((1,2,2)) = \left\{(x,y,z) \in \mathbb{R}^3 \;\middle|\; \begin{pmatrix} 2 & -1 & 0 \\ 2 & 0 & -1 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}\right\}$.
3. **Sottospazio generato da due vettori (p. 3):** con $v_1 = (1,1,0)$ e $v_2 = (0,1,1)$ in $\mathbb{R}^3$:
    $$\mathcal{L}(v_1, v_2) = \{a(1,1,0) + b(0,1,1) \mid a,b \in \mathbb{R}\} = \{(a, a+b, b) \mid a,b \in \mathbb{R}\}$$
    Eliminando $a$ e $b$: $\begin{cases} x = a \\ y = a + b \\ z = b \end{cases} \implies y = x + z$, cioè $\mathcal{L}(v_1, v_2) = \{(x,y,z) \in \mathbb{R}^3 \mid x - y + z = 0\}$.
4. **Generatori ridondanti (p. 4):** se $v_1 = (2,1,1)$ e $v_2 = 2v_1 = (4,2,2)$, allora $\mathcal{L}(v_1, v_2) = \mathcal{L}(v_1, 2v_1) = \mathcal{L}(v_1)$.
:::

:::example Esempio 5.3.2 — $K^{2,3}$ e $K^{m,n}$ sono finitamente generati (Lezione 8, p. 4)
In $V = K^{2,3}$, consideriamo le $6$ matrici elementari aventi $1$ in una sola entrata e $0$ altrove:

$$E_{11}=\begin{pmatrix}1&0&0\\0&0&0\end{pmatrix},\ E_{12}=\begin{pmatrix}0&1&0\\0&0&0\end{pmatrix},\ E_{13}=\begin{pmatrix}0&0&1\\0&0&0\end{pmatrix},\ E_{21}=\begin{pmatrix}0&0&0\\1&0&0\end{pmatrix},\ E_{22}=\begin{pmatrix}0&0&0\\0&1&0\end{pmatrix},\ E_{23}=\begin{pmatrix}0&0&0\\0&0&1\end{pmatrix}$$

Ogni matrice $A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{pmatrix} \in K^{2,3}$ si scrive come $A = a_{11}E_{11} + a_{12}E_{12} + a_{13}E_{13} + a_{21}E_{21} + a_{22}E_{22} + a_{23}E_{23}$. Dunque $\mathcal{B} = \{E_{11},\dots,E_{23}\}$ genera $K^{2,3}$, che è **finitamente generato** da $6$ matrici *(e in generale $K^{m,n}$ è finitamente generato da $mn$ matrici $E_{rs}$)*.
:::

:::example Esempio 5.3.3 — Tre esempi su dipendenza e indipendenza lineare (Lezione 8, p. 5)
1. $v_1 = (1,2,3)$, $v_2 = (2,4,6)$ in $\mathbb{R}^3$: poiché $v_2 = 2v_1 \implies 2v_1 - v_2 = \underline{0}$ (coefficienti $2, -1$ non tutti nulli), $v_1, v_2$ sono **linearmente dipendenti**.
2. $v_1 = (1,1,0)$, $v_2 = (0,1,1)$, $v_3 = v_1 + v_2 = (1,2,1)$: poiché $v_1 + v_2 - v_3 = \underline{0}$ (coefficienti $1, 1, -1$), $v_1, v_2, v_3$ sono **linearmente dipendenti**.
3. $v_1 = (1,1,0)$, $v_2 = (0,1,1)$: verifichiamo se $\{v_1, v_2\}$ è libero ponendo $av_1 + bv_2 = \underline{0}$:
    $$a(1,1,0) + b(0,1,1) = (0,0,0) \iff (a, a+b, b) = (0,0,0) \iff \begin{cases} a = 0 \\ a + b = 0 \\ b = 0 \end{cases} \iff \begin{cases} a = 0 \\ b = 0 \end{cases}$$
    L'unica combinazione lineare che dà $\underline{0}$ è quella con tutti coefficienti nulli: dunque $v_1, v_2$ sono **linearmente indipendenti** (`{v_1, v_2}` è un **insieme libero**).
:::

### 5. Errori comuni e trappole

1. **Verificare la dipendenza lineare trovando una combinazione non nulla *solo su alcune componenti***
    - *Sbagliato:* dire che $v_1=(1,1,0)$ e $v_2=(1,0,1)$ sono dipendenti perché $1\cdot 1 + (-1)\cdot 1 = 0$ sulla prima coordinata.
    - *Correzione:* l'equazione $a_1 v_1 + \dots + a_r v_r = \underline{0}$ è un'uguaglianza di **vettori** (quindi deve valere su *tutte* le coordinate contemporaneamente con gli stessi scalari $a_1, \dots, a_r$).
2. **Dimenticare che il vettore nullo rende subito dipendente qualsiasi insieme che lo contenga**
    - *Sbagliato:* scrivere che $\{\underline{0}, (1,0)\}$ o $\{(0,0)\}$ è linearmente indipendente.
    - *Correzione:* per il Criterio di indipendenza lineare *(Lezione 8, p. 6)*, già il primo vettore deve essere $v_1 \neq \underline{0}$: se $\underline{0}$ è nell'insieme, basta prendere il coefficiente $1$ davanti a $\underline{0}$ (e $0$ davanti agli altri) per ottenere $1\cdot\underline{0} = \underline{0}$ con un coefficiente non nullo!

### 6. Riepilogo

- Una **combinazione lineare** ha la forma $\sum_{i=1}^r a_i v_i$; tutte le combinazioni lineari di $S \neq \emptyset$ formano il sottospazio generato $\mathcal{L}(S)$.
- $S$ è un **insieme di generatori** di $V$ se $V = \mathcal{L}(S)$; $V$ è **finitamente generato** se ha un insieme finito di generatori.
- $v_1,\dots,v_r$ sono **linearmente dipendenti** se $\sum a_i v_i = \underline{0}$ con qualche $a_i \neq 0$; altrimenti sono **linearmente indipendenti** (*insieme libero*).
- **Criterio di indipendenza:** $v_1, \dots, v_r$ sono liberi $\iff v_1 \neq \underline{0}$ e $v_i \notin \mathcal{L}(v_1,\dots,v_{i-1})$ per $2 \le i \le r$.

### 7. Esercizi

La Lezione 8 *(pp. 1–6)* non assegna esercizi per casa su questo sottoparagrafo; tutti i concetti di insieme libero e generatori vengono combinati nell'argomento **basi e prolungamento** della sezione [5.4](#sec-5-4), che contiene l'esercizio per casa ufficiale di `Lez08`.

<!-- section: sec-5-4 | num: 5.4 | title: Basi, base canonica, scarti successivi e prolungamento a una base | kind: section | part: cap-5 -->

### 1. Idea in parole semplici

Una **base** di uno spazio vettoriale $V$ è l'equilibrio perfetto: contiene **abbastanza** vettori da poter generare tutto $V$ ($V = \mathcal{L}(\mathcal{B})$), ma **nessun** vettore superfluo ($\mathcal{B}$ è un insieme libero).

Come si ottiene concretamente una base? Abbiamo due algoritmi costruttivi complementari visti in aula:
1. Se parti da troppi vettori che già generano $V$ (**insieme di generatori**), usi il **metodo degli scarti successivi**: scorri la lista da sinistra a destra e butti via ogni vettore che si può scrivere come combinazione dei precedenti.
2. Se invece hai troppo pochi vettori ma già **indipendenti** (un **insieme libero** $L$), li metti in testa alla lista, ci accodi una base conosciuta (come la base canonica $\mathcal{E}$) e applichi gli scarti successivi: nessuno dei vettori iniziali verrà mai scartato, e quelli superstiti completeranno $L$ a una base (**prolungamento**)!

### 2. Definizioni e enunciati precisi

:::def Definizione — Base di uno spazio vettoriale e basi canoniche (Lezione 8, pp. 6–7)
Sia $V$ un $K$-spazio vettoriale e sia $\mathcal{B} \subseteq V$. Diremo che $\mathcal{B}$ è una **base** di $V$ se $\mathcal{B}$ è un **insieme libero di generatori** di $V$ *(cioè $\mathcal{B}$ è linearmente indipendente e $V = \mathcal{L}(\mathcal{B})$)*.

- **Base canonica di $K^n$ (p. 6):** $\mathcal{E} = \{e_1, \dots, e_n\}$ con $e_1 = (1,0,\dots,0),\ e_2 = (0,1,0,\dots,0),\ \dots,\ e_n = (0,\dots,0,1)$. Si ha $|\mathcal{E}| = n$.
- **Base canonica di $K^{m,n}$ (p. 7):** $\mathcal{E} = \{E_{rs} \mid 1 \le r \le m,\ 1 \le s \le n\}$, dove $E_{rs}$ è la matrice avente $\operatorname{ent}_{ij}(E_{rs}) = 1$ se $(i,j) = (r,s)$ e $0$ altrove. Si ha $|\mathcal{E}| = mn$.
:::

:::thm Proposizioni — Metodo degli scarti successivi e prolungamento di un insieme libero (Lezione 8, pp. 7–8)
1. **Metodo degli scarti successivi (p. 7):** sia $V$ un $K$-spazio vettoriale finitamente generato e sia $G \subseteq V$ un insieme di generatori finito. Allora **$G$ contiene una base di $V$**.
2. **Prolungamento ad una base (p. 8):** sia $V$ un $K$-spazio vettoriale finitamente generato e sia $L \subseteq V$ un insieme libero finito. Allora **$L$ si può estendere ad una base $\mathcal{B}$ di $V$**.
:::

### 3. Dimostrazioni

:::proof Dimostrazione 1 — Metodo degli scarti successivi (Lezione 8, p. 7)
**Idea di fondo:** esaminiamo i generatori uno per uno nell'ordine dato e applichiamo passo dopo passo il *Criterio di indipendenza lineare* (`v_i ∉ L(...)`): scartare un vettore che già sta nello span dei precedenti non riduce il sottospazio generato, mentre garantisce che i vettori tenuti siano linearmente indipendenti!

Sia $G = \{v_1, \dots, v_s\}$ un insieme finito di generatori di $V$. Procediamo ordinatamente da $v_1$ a $v_s$:
- **Passo $1$ (su $v_1 \in G$):**
    - se $v_1 = \underline{0}$, lo **scartiamo**;
    - se $v_1 \neq \underline{0}$, lo **teniamo**.
- **Passo $2$:** se $v_1$ è stato tenuto, esaminiamo $v_2$:
    - se $v_2 \in \mathcal{L}(v_1)$, lo **scartiamo**;
    - se $v_2 \notin \mathcal{L}(v_1)$, lo **teniamo**.
- **Passi successivi ($i = 3, \dots, s$):** si controlla se $v_i$ appartiene al sottospazio generato dai vettori tenuti fino a quel momento: se sì, si scarta *(perché è combinazione lineare dei precedenti, quindi la sua rimozione non altera $\mathcal{L}(G) = V$)*; altrimenti si tiene.

Alla fine della procedura, l'insieme $\mathcal{B}$ dei vettori rimasti genera ancora tutto $V$ e soddisfa entrambe le condizioni del Criterio di indipendenza lineare *(Sezione [5.3](#sec-5-3))*, quindi $\mathcal{B}$ è una **base** di $V$ contenuta in $G$.
:::

:::proof Dimostrazione 2 — Prolungamento di un insieme libero ad una base (Lezione 8, p. 8)
**Idea di fondo:** accodiamo a $L$ un insieme finito di generatori di $V$ e facciamo partire gli scarti successivi mettendo i vettori di $L$ **all'inizio** della lista.

Sia $L = \{u_1, \dots, u_r\}$ l'insieme libero dato, e sia $G = \{v_1, \dots, v_s\}$ un insieme finito di generatori di $V$ *(esiste perché $V$ è finitamente generato)*. Consideriamo l'insieme di generatori $\{u_1, \dots, u_r, v_1, \dots, v_s\}$ e applichiamo il **metodo degli scarti successivi** alla lista ordinata:

$$u_1,\ \dots,\ u_r,\ v_1,\ \dots,\ v_s$$

Poiché $u_1, \dots, u_r$ sono già linearmente indipendenti, per il Criterio di indipendenza lineare **nessuno degli $u_i$ potrà mai essere scartato** nei primi $r$ passi! Pertanto tutti gli eventuali scarti avverranno soltanto tra i $v_j$. Alla fine della procedura otterremo una base $\mathcal{B}$ di $V$ contenente $\{u_1, \dots, u_r\} = L$.
:::

### 4. Esempi svolti

:::example Esempio 5.4.1 — Estendere $L = \{(2,1,0), (1,1,0)\}$ ad una base di $\mathbb{R}^3$ (Lezione 8, pp. 8–9)
Sia $L = \{u_1, u_2\}$ con $u_1 = (2,1,0)$ e $u_2 = (1,1,0)$. È evidente che $L$ è un insieme libero *(poiché $(2,1,0)$ non è multiplo di $(1,1,0)$)* e la base canonica $\mathcal{E} = \{e_1, e_2, e_3\}$ genera $\mathbb{R}^3$. Applichiamo gli scarti successivi alla lista:

$$(2,1,0),\ (1,1,0),\ (1,0,0),\ (0,1,0),\ (0,0,1)$$

1. **$u_1, u_2$:** linearmente indipendenti $\implies$ li teniamo entrambi.
2. **Controlliamo $e_1 \stackrel{?}{\in} \mathcal{L}((2,1,0), (1,1,0))$:**
    $$(1,0,0) = x(2,1,0) + y(1,1,0) \iff \begin{cases} 2x + y = 1 \\ x + y = 0 \\ 0 = 0 \end{cases} \implies \begin{cases} x = 1 \\ y = -1 \end{cases}$$
    Poiché $e_1 = u_1 - u_2 \in \mathcal{L}(u_1, u_2)$, **scartiamo $e_1$**.
3. **Controlliamo $e_2 \stackrel{?}{\in} \mathcal{L}(u_1, u_2)$:**
    $$(0,1,0) = x(2,1,0) + y(1,1,0) \iff \begin{cases} 2x + y = 0 \\ x + y = 1 \\ 0 = 0 \end{cases} \implies \begin{cases} 2x + 1 - x = 0 \\ y = 1 - x \end{cases} \implies \begin{cases} x = -1 \\ y = 2 \end{cases}$$
    Poiché $e_2 = -u_1 + 2u_2 \in \mathcal{L}(u_1, u_2)$, **scartiamo $e_2$**.
4. **Controlliamo $e_3 \stackrel{?}{\in} \mathcal{L}(u_1, u_2)$:**
    $$(0,0,1) = x(2,1,0) + y(1,1,0) \iff \begin{cases} 2x + y = 0 \\ x + y = 0 \\ 0 = 1 \end{cases}$$
    La terza equazione dà $0 = 1$ (assurdo!): dunque $e_3 \notin \mathcal{L}(u_1, u_2)$ e **teniamo $e_3$**.

Pertanto $\mathcal{B} = \{u_1, u_2, e_3\} = \{(2,1,0), (1,1,0), (0,0,1)\}$ è una base di $\mathbb{R}^3$ che estende $L$.
:::

### 5. Errori comuni e trappole

1. **Nel prolungamento, mettere $G$ davanti a $L$ negli scarti successivi**
    - *Sbagliato:* ordinare la lista come $e_1, e_2, e_3, u_1, u_2$.
    - *Correzione:* se metti la base canonica $\mathcal{E}$ all'inizio, $e_1, e_2, e_3$ vengono tutti tenuti subito e poi scarti $u_1$ e $u_2$ — finendo con $\mathcal{E}$ invece che con un'estensione di $L$! I vettori di $L$ devono stare **sempre per primi** *(Lezione 8, p. 8)*.
2. **Dimenticare di controllare la dipendenza dei vettori aggiunti anche rispetto a quelli già tenuti prima**
    - *Sbagliato:* per verificare se tenere $e_3$, controllare solo $e_3 \in \mathcal{L}(L)$ dimenticando un vettore $e_1$ già tenuto al passo precedente.
    - *Correzione:* ogni nuovo candidato $v_j$ va testato contro **tutti** i vettori tenuti fino a quel momento ($L$ più gli eventuali $e_k$ tenuti in precedenza!).

### 6. Riepilogo

- Una **base** di $V$ è un insieme libero (linearmente indipendente) di generatori di $V$.
- La **base canonica** di $K^n$ è $\mathcal{E}=\{e_1,\dots,e_n\}$ ($n$ vettori); quella di $K^{m,n}$ è $\mathcal{E}=\{E_{rs}\}$ ($mn$ matrici).
- **Metodo degli scarti successivi:** da qualsiasi insieme finito di generatori si estrae una base scartando via via $\underline{0}$ e ogni vettore che sia combinazione dei precedenti.
- **Prolungamento:** ogni insieme libero finito $L$ in uno spazio finitamente generato si estende a una base applicando gli scarti successivi a $L$ seguito da una lista di generatori (tipicamente la base canonica).

### 7. Esercizi

:::exercise Esercizio 5.4.1 (Esercizio per casa — Medio · Lezione 8, p. 9)
Siano $u_1 = (1,1,1,0)$ e $u_2 = (1,0,2,1)$ in $\mathbb{R}^4$.
1. Provare che $L = \{u_1, u_2\}$ è un insieme libero di $\mathbb{R}^4$.
2. Estendere $L$ ad una base di $\mathbb{R}^4$.

:::solution Soluzione spiegata passo-passo
**Ragionamento:** prima risolviamo $a u_1 + b u_2 = \underline{0}$ per mostrare che $a = b = 0$ (oppure il criterio di indipendenza); poi applichiamo il metodo degli scarti successivi alla lista $u_1, u_2, e_1, e_2, e_3, e_4$ in $\mathbb{R}^4$.

**1. Verifica che $L = \{u_1, u_2\}$ è un insieme libero:**
Poniamo $a(1,1,1,0) + b(1,0,2,1) = (0,0,0,0)$:

$$(a+b,\ a,\ a+2b,\ b) = (0,0,0,0) \iff \begin{cases} a + b = 0 \\ a = 0 \\ a + 2b = 0 \\ b = 0 \end{cases} \implies a = 0,\ b = 0$$

L'unica combinazione nulla è quella con coefficienti tutti nulli, quindi $u_1$ e $u_2$ sono **linearmente indipendenti** ($L$ è libero).

**2. Estensione a una base di $\mathbb{R}^4$ con il metodo degli scarti successivi:**
Consideriamo la lista di generatori di $\mathbb{R}^4$:

$$u_1 = (1,1,1,0),\quad u_2 = (1,0,2,1),\quad e_1 = (1,0,0,0),\quad e_2 = (0,1,0,0),\quad e_3 = (0,0,1,0),\quad e_4 = (0,0,0,1)$$

- **Passi 1–2 ($u_1, u_2$):** già provati linearmente indipendenti, li **teniamo entrambi**.
- **Passo 3 (su $e_1$):** verifichiamo se $e_1 \in \mathcal{L}(u_1, u_2)$:
    $$(1,0,0,0) = x(1,1,1,0) + y(1,0,2,1) \iff \begin{cases} x + y = 1 \\ x = 0 \\ x + 2y = 0 \\ y = 0 \end{cases}$$
    Dalla 2ª e 4ª equazione $x = 0, y = 0$, che sostituite nella 1ª danno $0 = 1$ (impossibile!). Quindi $e_1 \notin \mathcal{L}(u_1, u_2)$ e **teniamo $e_1$**.
- **Passo 4 (su $e_2$):** verifichiamo se $e_2 \in \mathcal{L}(u_1, u_2, e_1)$:
    $$(0,1,0,0) = x(1,1,1,0) + y(1,0,2,1) + z(1,0,0,0) \iff \begin{cases} x + y + z = 0 \\ x = 1 \\ x + 2y = 0 \\ y = 0 \end{cases}$$
    Dalla 2ª equazione $x = 1$ e dalla 4ª equazione $y = 0$, ma sostituendole nella 3ª equazione otteniamo $1 + 0 = 0$ (assurdo!). Quindi $e_2 \notin \mathcal{L}(u_1, u_2, e_1)$ e **teniamo $e_2$**.
- *(Osservazione conclusiva — verifica rapida che bastano già $4$ vettori, oppure continuazione sugli ultimi due vettori):* con i $4$ vettori $\{u_1, u_2, e_1, e_2\}$ abbiamo costruito un insieme libero di $4$ elementi in $\mathbb{R}^4$: infatti disponendoli in matrice e calcolandone il determinante:
    $$\det\begin{pmatrix} 1 & 1 & 1 & 0 \\ 1 & 0 & 2 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix} = \det\begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix} = 1 \neq 0$$
    Per completezza controlliamo anche che $e_3$ ed $e_4$ si scartino: infatti $e_3 = u_1 - e_1 - e_2$ ed $e_4 = u_2 - e_1 - 2e_3 = u_2 - 2u_1 + e_1 + 2e_2 \in \mathcal{L}(u_1, u_2, e_1, e_2)$.

Pertanto $\mathcal{B} = \{u_1, u_2, e_1, e_2\} = \{(1,1,1,0),\ (1,0,2,1),\ (1,0,0,0),\ (0,1,0,0)\}$ è una **base di $\mathbb{R}^4$** che estende $L$.
:::
:::

<!-- section: sec-5-5 | num: 5.5 | title: Lemma di Steinitz, dimensione e Formula di Grassmann | kind: section | part: cap-5 -->

### 1. Idea in parole semplici

Abbiamo visto che in $\mathbb{R}^4$ qualsiasi base sembra avere esattamente $4$ vettori, e in $K^{m,n}$ esattamente $mn$ matrici. È un caso, o **tutte** le basi di uno stesso spazio vettoriale hanno sempre lo stesso identico numero di elementi?

Il **Lemma di Steinitz** risponde una volta per tutte con una legge di ferro: *un insieme di vettori liberi non può mai avere più elementi di un insieme di generatori* ($|L| \le |G|$). Applicato due volte a due basi diverse, dimostra che esse hanno **sempre lo stesso numero di elementi**, chiamato **dimensione** dello spazio ($\dim_K V$). Da lì, la **Formula di Grassmann** ci dà il bilancio perfetto tra somme e intersezioni di sottospazi, identico al principio di inclusione-esclusione degli insiemi: $\dim(U+W) = \dim U + \dim W - \dim(U \cap W)$.

### 2. Definizioni e enunciati precisi

:::thm Lemma di Steinitz (Lezione 9, p. 1)
Sia $V$ un $K$-spazio vettoriale finitamente generato, sia $G \subseteq V$ un insieme finito di generatori di $V$ e sia $L \subseteq V$ un insieme libero in $V$. Allora:

$$|L| \le |G|$$

*(Il numero di elementi in $L$ è minore o uguale al numero di elementi in $G$.)*
:::

:::thm Corollario e Definizione — Dimensione $\dim_K V$ (Lezione 9, pp. 1–2)
- **Corollario:** sia $V$ un $K$-spazio vettoriale finitamente generato e siano $\mathcal{B}_1, \mathcal{B}_2$ due basi qualsiasi di $V$. Allora $|\mathcal{B}_1| = |\mathcal{B}_2|$.
- **Definizione di dimensione:** si chiama **dimensione** di $V$ *(denotata con $\dim_K V$)* il numero di elementi di una sua qualsiasi base.
:::

:::thm Proposizione — Dimensione di un sottospazio (Lezione 9, p. 2)
Sia $V$ un $K$-spazio vettoriale finitamente generato e sia $W \subseteq V$ un sottospazio. Allora:
1. $\dim_K W \le \dim_K V$;
2. $\dim_K W = \dim_K V \iff W = V$.
:::

:::thm Formula di Grassmann (Lezione 9, p. 2)
Sia $V$ un $K$-spazio vettoriale finitamente generato e siano $U \subseteq V$, $W \subseteq V$ due suoi sottospazi. Allora:

$$\dim_K(U + W) = \dim_K U + \dim_K W - \dim_K(U \cap W)$$
:::

### 3. Dimostrazioni

:::proof Dimostrazione — Tutte le basi di $V$ hanno la stessa cardinalità (Lezione 9, p. 1)
**Idea di fondo:** ogni base è *contemporaneamente* un insieme libero e un insieme di generatori; applicando due volte il Lemma di Steinitz a ruoli invertiti si ottengono le due disuguaglianze $|\mathcal{B}_1| \le |\mathcal{B}_2|$ e $|\mathcal{B}_2| \le |\mathcal{B}_1|$.

Siano $\mathcal{B}_1$ e $\mathcal{B}_2$ due basi di $V$ *(si noti che per Steinitz risultano entrambe finite essendo $V$ finitamente generato)*. Applicando il Lemma di Steinitz:
- $\mathcal{B}_1$ è un insieme libero e $\mathcal{B}_2$ è un insieme di generatori $\implies |\mathcal{B}_1| \le |\mathcal{B}_2|$;
- d'altra parte, $\mathcal{B}_2$ è un insieme libero e $\mathcal{B}_1$ è un insieme di generatori $\implies |\mathcal{B}_2| \le |\mathcal{B}_1|$.

Mettendo insieme le due disuguaglianze segue necessariamente $|\mathcal{B}_1| = |\mathcal{B}_2|$.
:::

:::note Nota sugli appunti originali (`Lez09`, pp. 1–3)
1. Il Lemma di Steinitz, la Proposizione sulla dimensione dei sottospazi e la Formula di Grassmann vengono presentati senza dimostrazione *(mentre il Corollario è dimostrato)*.
2. **Refuso notazionale (`Lez09`, p. 3 in fondo):** nell'esempio su $U \cap W$ in $\mathbb{R}^3$, nell'ultima riga scrive $\dim_K(U \cap W) = \dim_K U + \dim_K W - \dim_K(U+W)$ usando il pedice generico $K$ anziché $\mathbb{R}$ già usato nelle righe superiori.
:::

### 4. Esempi svolti

:::example Esempio 5.5.1 — Dimensioni degli spazi modello $K^{m,n}$, $K^n$, $K^3$ (Lezione 9, pp. 1–2)
1. In $V = K^{m,n}$, la base canonica $\mathcal{E} = \{E_{ij} \mid 1 \le i \le m,\ 1 \le j \le n\}$ ha $|\mathcal{E}| = mn$, quindi **$\dim_K K^{m,n} = mn$**.
2. In particolare, per $V = K^n = K^{1,n}$ si ha **$\dim_K K^n = n$** *(per $n = 3$, $\mathcal{E} = \{(1,0,0), (0,1,0), (0,0,1)\} \implies \dim_K K^3 = 3$)*.
:::

:::example Esempio 5.5.2 — Prima applicazione di Grassmann in $\mathbb{R}^3$ (Lezione 9, pp. 2–3)
Siano $U = \mathcal{L}((1,1,1), (0,2,5))$ e $W = \mathcal{L}((1,1,1), (0,1,7))$ sottospazi di $\mathbb{R}^3$.
- I due generatori di $U$ sono linearmente indipendenti (non proporzionali), quindi $\dim_{\mathbb{R}} U = 2$; analogamente $\dim_{\mathbb{R}} W = 2$.
- Il sottospazio somma è generato dall'unione dei generatori (eliminando il doppione $(1,1,1)$):
    $$U + W = \mathcal{L}((1,1,1), (0,2,5), (0,1,7))$$
    Controlliamo l'indipendenza lineare con il criterio:
    - $v_1 = (1,1,1) \neq (0,0,0)$;
    - $v_2 = (0,2,5) \notin \mathcal{L}(v_1)$ *(altrimenti $(0,2,5) = (x,x,x) \implies x=0, 2, 5$, impossibile)*;
    - $v_3 = (0,1,7) \notin \mathcal{L}(v_1, v_2)$ *(altrimenti $(0,1,7) = x(1,1,1) + y(0,2,5) \implies x=0,\ 2y=1 \implies y=\frac{1}{2}$ e $5y=7 \implies y=\frac{7}{5}$, assurdo)*.
    Dunque $\{v_1, v_2, v_3\}$ è una base di $U+W \implies \dim_{\mathbb{R}}(U + W) = 3$ (e quindi $U + W = \mathbb{R}^3$).
- Per la **Formula di Grassmann**:
    $$\dim_{\mathbb{R}}(U \cap W) = \dim_{\mathbb{R}} U + \dim_{\mathbb{R}} W - \dim_{\mathbb{R}}(U + W) = 2 + 2 - 3 = 1$$
    Siccome $(1,1,1)$ appartiene ovviamente sia ad $U$ sia a $W$, genera un sottospazio di dimensione $1$ contenuto in $U \cap W$: quindi $U \cap W = \mathcal{L}((1,1,1))$.
:::

:::example Esempio 5.5.3 — Calcolo completo di $U+W$ e $U\cap W$ passando alle equazioni (Lezione 10, pp. 1–2)
Siano $U = \mathcal{L}((1,1,2), (0,2,5))$ e $W = \mathcal{L}((3,3,1), (1,2,7))$ sottospazi di $\mathbb{R}^3$. Calcolare $U + W$ e $U \cap W$.

*(Nota metodologica: questo esercizio usa già il Teorema di Kronecker e il passaggio alle equazioni cartesiane mediante determinanti/Orlati e minori a segno alterno, approfonditi sistematicamente nelle sezioni [5.6](#sec-5-6) e [5.7](#sec-5-7).)*

1. **Dimensioni di $U$ e $W$:**
    - $\dim_{\mathbb{R}} U = \operatorname{rk}\begin{pmatrix} 1 & 1 & 2 \\ 0 & 2 & 5 \end{pmatrix} = 2$.
    - Riduciamo la matrice di $W$ scambiando le due righe per avere $1$ in testa:
        $$\operatorname{rk}\begin{pmatrix} 3 & 3 & 1 \\ 1 & 2 & 7 \end{pmatrix} = \operatorname{rk}\begin{pmatrix} 1 & 2 & 7 \\ 3 & 3 & 1 \end{pmatrix} = \operatorname{rk}\begin{pmatrix} \boxed{1} & 2 & 7 \\ 0 & \boxed{-3} & -20 \end{pmatrix} = 2$$
        Dunque $\dim_{\mathbb{R}} W = 2$ e $W = \mathcal{L}((1,2,7), (0,3,20))$ *(cambiando segno alla seconda riga)*.

2. **Calcolo di $U + W$ e sua dimensione:**
    $U + W = \mathcal{L}((1,1,2), (0,2,5), (1,2,7), (0,3,20))$. Riduciamo per righe la matrice dei $4$ generatori:
    $$\begin{pmatrix} 1 & 1 & 2 \\ 0 & 2 & 5 \\ 1 & 2 & 7 \\ 0 & 3 & 20 \end{pmatrix} \xrightarrow{R_3 \mapsto R_3 - R_1} \begin{pmatrix} 1 & 1 & 2 \\ 0 & 2 & 5 \\ 0 & 1 & 5 \\ 0 & 3 & 20 \end{pmatrix} \xrightarrow{\substack{R_3 \mapsto 2R_3 - R_2 \\ \text{poi } R_3 \leftrightarrow R_3,\ R_4 \mapsto 3R_2 - 2R_4}} \begin{pmatrix} 1 & 1 & 2 \\ 0 & 2 & 5 \\ 0 & 0 & -5 \\ 0 & 0 & -10 \end{pmatrix} \longrightarrow \begin{pmatrix} \boxed{1} & 1 & 2 \\ 0 & \boxed{2} & 5 \\ 0 & 0 & \boxed{1} \\ 0 & 0 & 0 \end{pmatrix}$$
    Pertanto $\dim_{\mathbb{R}}(U + W) = 3 = \dim_{\mathbb{R}}\mathbb{R}^3 \implies$ **$U + W = \mathbb{R}^3$**.

3. **Dimensione di $U \cap W$ (Grassmann) ed equazioni cartesiane (p. 2):**
    Per Grassmann, $\dim_{\mathbb{R}}(U \cap W) = 2 + 2 - 3 = 1$. Ricaviamo le equazioni cartesiane di $U$ e $W$ imponendo che $(x,y,z)$ sia combinazione dei rispettivi $2$ generatori *(cioè $\det = 0$)*:
    - **Equazione di $U$:**
        $$\det\begin{pmatrix} x & y & z \\ 1 & 1 & 2 \\ 0 & 2 & 5 \end{pmatrix} = 0 \iff x(5-4) - y(5-0) + z(2-0) = 0 \iff x - 5y + 2z = 0$$
    - **Equazione di $W$:**
        $$\det\begin{pmatrix} x & y & z \\ 1 & 2 & 7 \\ 0 & 3 & 20 \end{pmatrix} = 0 \iff x(40-21) - y(20-0) + z(3-0) = 0 \iff 19x - 20y + 3z = 0$$
    - **Sistema per $U \cap W$:**
        $$U \cap W : \begin{cases} x - 5y + 2z = 0 \\ 19x - 20y + 3z = 0 \end{cases}$$
        Riduciamo $A = \begin{pmatrix} 1 & -5 & 2 \\ 19 & -20 & 3 \end{pmatrix}$ con $R_2 \mapsto R_2 - 4R_1$ *(per annullare la colonna di $y$)*: otteniamo $\begin{pmatrix} 1 & -5 & 2 \\ 15 & 0 & -5 \end{pmatrix} \xrightarrow{R_2 \mapsto \frac{1}{5}R_2} \begin{pmatrix} 1 & -5 & 2 \\ 3 & 0 & -1 \end{pmatrix}$. Calcolando i minori di ordine $2$ a segno alterno:
        $$d_1 = \det\begin{pmatrix} -5 & 2 \\ 0 & -1 \end{pmatrix} = 5, \qquad d_2 = -\det\begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix} = 7, \qquad d_3 = \det\begin{pmatrix} 1 & -5 \\ 3 & 0 \end{pmatrix} = 15$$
        Una soluzione non nulla è $(5, 7, 15)$, e poiché $\dim_{\mathbb{R}}(U \cap W) = 1$, concludiamo:
        $$U \cap W = \mathcal{L}((5, 7, 15))$$
:::

### 5. Errori comuni e trappole

1. **Pensare che un insieme libero di $3$ vettori in $\mathbb{R}^3$ possa non generare tutto $\mathbb{R}^3$**
    - *Sbagliato:* calcolare separatamente la base e chiedersi se $3$ vettori indipendenti generano $\mathbb{R}^3$.
    - *Correzione:* `[INTEGRAZIONE NON DALLE LEZIONI]` in uno spazio di dimensione $n$, se hai $n$ vettori linearmente indipendenti, prolungandoli non puoi aggiungere nessun altro vettore (per Steinitz qualsiasi insieme libero ha al più $n$ elementi): quindi formano **già automaticamente una base**!
2. **Dimenticare il segno meno davanti a $\dim_K(U \cap W)$ nella Formula di Grassmann**
    - *Sbagliato:* scrivere $\dim(U+W) = \dim U + \dim W + \dim(U\cap W)$.
    - *Correzione:* l'intersezione $U \cap W$ viene contata *due volte* nella somma $\dim U + \dim W$ (una volta dentro $U$ e una volta dentro $W$), quindi va **sottratta** una volta: $\dim(U+W) = \dim U + \dim W - \dim(U\cap W)$.

### 6. Riepilogo

- **Lemma di Steinitz:** ogni insieme libero $L$ ha al più tanti elementi quanti ne ha un insieme di generatori $G$ ($|L| \le |G|$).
- Tutte le basi di uno stesso spazio vettoriale finitamente generato hanno la stessa cardinalità, chiamata **dimensione** ($\dim_K V$).
- $\dim_K K^{m,n} = mn$ e $\dim_K K^n = n$.
- Se $W \subseteq V$ è sottospazio, $\dim_K W \le \dim_K V$, con uguaglianza se e solo se $W = V$.
- **Formula di Grassmann:** $\dim_K(U+W) = \dim_K U + \dim_K W - \dim_K(U \cap W)$.

### 7. Esercizi

:::exercise Esercizio 5.5.1 (Esercizio per casa — Medio/Difficile · Lezione 10, p. 3)
Siano $U$ e $W$ i seguenti sottospazi di $\mathbb{R}^5$:

$$U = \mathcal{L}\bigl((1,2,1,2,1),\ (0,1,2,3,2)\bigr)$$
$$W = \bigl\{(x,y,z,t,u) \in \mathbb{R}^5 \;\big|\; x+y+z+t+u = 0,\ y+2z+3t+2u = 0,\ z+4t+u = 0\bigr\}$$

Calcolare $U + W$ e $U \cap W$ (determinandone dimensione e base).

:::solution Soluzione spiegata passo-passo
**Ragionamento:** poiché $U$ è dato tramite generatori e $W$ tramite equazioni cartesiane, abbiamo due strategie complementari perfette: (1) ricaviamo subito una base di $W$ risolvendo il sistema omogeneo per trovare poi $\dim(U+W)$ e $U+W$; (2) sostituiamo il vettore generico $au_1 + bu_2$ di $U$ direttamente dentro le equazioni di $W$ per trovare $U \cap W$, e incrociamo i risultati con la Formula di Grassmann!

1. **Dimensione di $U$ e base di $W$:**
    - I due vettori $u_1 = (1,2,1,2,1)$ e $u_2 = (0,1,2,3,2)$ non sono proporzionali, quindi formano una base di $U$: **$\dim_{\mathbb{R}} U = 2$**.
    - La matrice dei coefficienti di $W$ è già triangolare superiore con $3$ righe e $3$ elementi speciali $1$ sulla diagonale:
        $$A_W = \begin{pmatrix} 1 & 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 3 & 2 \\ 0 & 0 & 1 & 4 & 1 \end{pmatrix}$$
        Dunque $\operatorname{rk} A_W = 3$ e $\dim_{\mathbb{R}} W = 5 - 3 = 2$. Risolviamo il sistema scegliendo $t, u \in \mathbb{R}$ come variabili libere:
        - dalla 3ª eq.: $z = -4t - u$;
        - dalla 2ª eq.: $y = -2z - 3t - 2u = -2(-4t - u) - 3t - 2u = 8t + 2u - 3t - 2u = 5t$;
        - dalla 1ª eq.: $x = -y - z - t - u = -5t - (-4t - u) - t - u = -2t$.
        Pertanto $(x,y,z,t,u) = t(-2, 5, -4, 1, 0) + u(0, 0, -1, 0, 1)$, e una base di $W$ è $\{w_1, w_2\}$ con:
        $$w_1 = (-2, 5, -4, 1, 0), \qquad w_2 = (0, 0, -1, 0, 1)$$
        *(Verifica rapida: per $w_1$: $-2+5-4+1+0=0$, $5-8+3+0=0$, $-4+4+0=0$; per $w_2$: $-1+1=0$, $-2+2=0$, $-1+1=0$.)*

2. **Calcolo di $U \cap W$:**
    Un generico vettore $v \in U$ ha la forma $v = a(1,2,1,2,1) + b(0,1,2,3,2) = (a,\ 2a+b,\ a+2b,\ 2a+3b,\ a+2b)$ con $a, b \in \mathbb{R}$. Imponiamo che $v \in W$ sostituendolo nelle tre equazioni di $W$:
    $$\begin{cases} a + (2a+b) + (a+2b) + (2a+3b) + (a+2b) = 0 \\ (2a+b) + 2(a+2b) + 3(2a+3b) + 2(a+2b) = 0 \\ (a+2b) + 4(2a+3b) + (a+2b) = 0 \end{cases} \iff \begin{cases} 7a + 8b = 0 \\ 12a + 18b = 0 \\ 10a + 16b = 0 \end{cases}$$
    Dalla 2ª equazione ($2a + 3b = 0 \implies a = -\frac{3}{2}b$) sostituita nella 1ª otteniamo $7\left(-\frac{3}{2}b\right) + 8b = -\frac{5}{2}b = 0 \implies b = 0$ e quindi anche $a = 0$.
    Dunque l'unico vettore comune a $U$ e $W$ è il vettore nullo:
    $$U \cap W = \{(0, 0, 0, 0, 0)\} = \{\underline{0}\}, \qquad \dim_{\mathbb{R}}(U \cap W) = 0$$

3. **Calcolo di $U + W$ e verifica con la Formula di Grassmann:**
    Per Grassmann:
    $$\dim_{\mathbb{R}}(U + W) = \dim_{\mathbb{R}} U + \dim_{\mathbb{R}} W - \dim_{\mathbb{R}}(U \cap W) = 2 + 2 - 0 = 4$$
    Poiché $U + W = \mathcal{L}(u_1, u_2, w_1, w_2)$ ha $4$ generatori in tutto e dimensione $4$, i $4$ vettori $\{u_1, u_2, w_1, w_2\}$ sono **linearmente indipendenti** e formano direttamente una base di $U + W$!
    *(Possiamo verificarlo riducendo la matrice avente $u_1, u_2, w_1, w_2$ come righe:
    $$\begin{pmatrix} 1 & 2 & 1 & 2 & 1 \\ 0 & 1 & 2 & 3 & 2 \\ -2 & 5 & -4 & 1 & 0 \\ 0 & 0 & -1 & 0 & 1 \end{pmatrix} \xrightarrow{R_3 \mapsto R_3 + 2R_1} \begin{pmatrix} 1 & 2 & 1 & 2 & 1 \\ 0 & 1 & 2 & 3 & 2 \\ 0 & 9 & -2 & 5 & 2 \\ 0 & 0 & -1 & 0 & 1 \end{pmatrix} \xrightarrow{R_3 \mapsto R_3 - 9R_2} \begin{pmatrix} 1 & 2 & 1 & 2 & 1 \\ 0 & 1 & 2 & 3 & 2 \\ 0 & 0 & -20 & -22 & -16 \\ 0 & 0 & -1 & 0 & 1 \end{pmatrix} \xrightarrow{R_3 \mapsto R_3 - 20R_4} \begin{pmatrix} \boxed{1} & 2 & 1 & 2 & 1 \\ 0 & \boxed{1} & 2 & 3 & 2 \\ 0 & 0 & 0 & \boxed{-22} & -36 \\ 0 & 0 & \boxed{-1} & 0 & 1 \end{pmatrix}$$
    tutte e $4$ le righe hanno elementi speciali distinti, quindi $\dim_{\mathbb{R}}(U+W) = 4$.)*
    In sintesi:
    - $U + W = \mathcal{L}\bigl((1,2,1,2,1),\ (0,1,2,3,2),\ (-2,5,-4,1,0),\ (0,0,-1,0,1)\bigr)$ *(sottospazio di dimensione $4$ di $\mathbb{R}^5$)*;
    - $U \cap W = \{(0,0,0,0,0)\}$ *(sottospazio banale di dimensione $0$)*.
:::
:::

<!-- section: sec-5-6 | num: 5.6 | title: Spazio delle righe e delle colonne, Teorema di Kronecker e dimostrazione di Rouché-Capelli | kind: section | part: cap-5 -->

### 1. Idea in parole semplici

Questo sottoparagrafo getta il ponte definitivo tra la teoria delle **matrici/sistemi** (Capitoli 2–4) e la teoria degli **spazi vettoriali** (Capitolo 5). Ogni matrice $A \in K^{m,n}$ genera due sottospazi gemelli: lo spazio generato dalle sue righe ($\mathcal{L}_R(A) \subseteq K^n$) e quello generato dalle sue colonne ($\mathcal{L}_C(A) \subseteq K^m$).

Sembra incredibile, visto che vivono in ambienti diversi ($K^n$ e $K^m$), eppure il **Teorema di Kronecker** garantisce che hanno **sempre esattamente la stessa dimensione**, e quella dimensione coincide con il **rango** $\operatorname{rk} A$! Questo risultato elegante regala immediatamente la **dimostrazione completa del Teorema di Rouché-Capelli** lasciata in sospeso nel Capitolo 4: dire che $AX = B$ ha soluzione vuol dire esattamente che $B$ si può scrivere come combinazione lineare delle colonne di $A$, cioè $B \in \mathcal{L}_C(A)$!

### 2. Definizioni e enunciati precisi

:::def Definizione — Spazio delle righe $\mathcal{L}_R(A)$ e spazio delle colonne $\mathcal{L}_C(A)$ (Lezione 9, p. 4)
Sia $A \in K^{m,n}$, scritta per righe e per colonne come:

$$A = \begin{pmatrix} R_1 \\ \vdots \\ R_m \end{pmatrix} = (C_1\ \dots\ C_n) \qquad (R_i \in K^n,\ C_j \in K^m)$$

- Si chiama **spazio delle righe** di $A$ il sottospazio di $K^n$ generato dalle righe:
    $$\mathcal{L}_R(A) \stackrel{\text{DEF}}{=} \mathcal{L}(R_1, \dots, R_m) \subseteq K^n$$
- Si chiama **spazio delle colonne** di $A$ il sottospazio di $K^m$ generato dalle colonne:
    $$\mathcal{L}_C(A) \stackrel{\text{DEF}}{=} \mathcal{L}(C_1, \dots, C_n) \subseteq K^m$$
:::

:::thm Teorema di Kronecker (Lezione 9, p. 4)
Per ogni matrice $A \in K^{m,n}$:

$$\dim_K \mathcal{L}_R(A) = \dim_K \mathcal{L}_C(A) = \operatorname{rk} A$$
:::

### 3. Dimostrazioni

:::proof Dimostrazione — Teorema di Rouché-Capelli via Kronecker (Lezione 9, pp. 4–5)
**Idea di fondo:** riscriviamo il prodotto $AX = B$ come combinazione lineare delle colonne di $A$: $x_1 C_1 + \dots + x_n C_n = B$. Quindi $AX = B$ è risolubile se e solo se $B$ appartiene allo spazio delle colonne $\mathcal{L}(C_1, \dots, C_n)$, cioè se e solo se l'aggiunta di $B$ ai generatori non fa crescere né il sottospazio generato né (per Kronecker) la sua dimensione (il rango)!

Scriviamo $A \in K^{m,n}$ per colonne come $A = (C_1\ \dots\ C_n)$ ed $X = \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}$. Per la definizione del prodotto riga per colonna, l'equazione matriciale $AX = B$ si riscrive nella forma vettoriale:

$$x_1 C_1 + \dots + x_n C_n = B$$

- **($\Rightarrow$) Supponiamo che $AX = B$ sia risolubile:**
    Esiste almeno una soluzione $\bar{X} = (\bar{x}_1, \dots, \bar{x}_n)^T$ tale che $\bar{x}_1 C_1 + \dots + \bar{x}_n C_n = B$, quindi $B \in \mathcal{L}(C_1, \dots, C_n)$. Poiché $B$ è già combinazione lineare di $C_1, \dots, C_n$, aggiungerlo non cambia lo spazio generato:
    $$\mathcal{L}(C_1, \dots, C_n) = \mathcal{L}(C_1, \dots, C_n, B)$$
    Passando alle dimensioni e applicando il **Teorema di Kronecker** ad $A$ e ad $A|B$:
    $$\dim_K \mathcal{L}(C_1, \dots, C_n) = \dim_K \mathcal{L}(C_1, \dots, C_n, B) \implies \operatorname{rk} A = \operatorname{rk}(A|B)$$

- **($\Leftarrow$) Supponiamo che $\operatorname{rk} A = \operatorname{rk}(A|B)$:**
    Per il Teorema di Kronecker abbiamo:
    $$\dim_K \mathcal{L}(C_1, \dots, C_n) = \dim_K \mathcal{L}(C_1, \dots, C_n, B)$$
    Osserviamo inoltre che $\mathcal{L}(C_1, \dots, C_n) \subseteq \mathcal{L}(C_1, \dots, C_n, B)$ *(cioè il primo è un sottospazio del secondo)* avente la **stessa dimensione**. Per la Proposizione della Sezione [5.5](#sec-5-5), due sottospazi uno dentro l'altro con uguale dimensione coincidono:
    $$\mathcal{L}(C_1, \dots, C_n) = \mathcal{L}(C_1, \dots, C_n, B)$$
    Di conseguenza $B \in \mathcal{L}(C_1, \dots, C_n)$, quindi esistono scalari $\bar{x}_1, \dots, \bar{x}_n \in K$ tali che $B = \bar{x}_1 C_1 + \dots + \bar{x}_n C_n$, ossia $\bar{X} = \begin{pmatrix} \bar{x}_1 \\ \vdots \\ \bar{x}_n \end{pmatrix}$ è una soluzione del sistema. Il sistema $AX = B$ è dunque risolubile.
:::

### 4. Esempi svolti

:::example Esempio 5.6.1 — Spazio delle righe e delle colonne di una $2 \times 3$ (Lezione 9, p. 4)
Sia:

$$A = \begin{pmatrix} 2 & 1 & 4 \\ 3 & 2 & 5 \end{pmatrix} \in \mathbb{R}^{2,3}$$

- Lo **spazio delle righe** vive in $\mathbb{R}^3$: $\mathcal{L}_R(A) = \mathcal{L}\bigl((2,1,4),\ (3,2,5)\bigr) \subseteq \mathbb{R}^3$.
- Lo **spazio delle colonne** vive in $\mathbb{R}^2$: $\mathcal{L}_C(A) = \mathcal{L}\bigl((2,3),\ (1,2),\ (4,5)\bigr) \subseteq \mathbb{R}^2$.

Poiché $\det\begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix} = 4 - 3 = 1 \neq 0$, si ha $\operatorname{rk} A = 2$; quindi, per il Teorema di Kronecker, entrambi i sottospazi hanno dimensione $2$ (in particolare $\mathcal{L}_C(A) = \mathbb{R}^2$).
:::

### 5. Errori comuni e trappole

1. **Scambiare lo spazio ambiente di $\mathcal{L}_R(A)$ con quello di $\mathcal{L}_C(A)$ per una matrice rettangolare**
    - *Sbagliato:* con $A \in \mathbb{R}^{2,3}$, scrivere che $\mathcal{L}_R(A)$ è un sottospazio di $\mathbb{R}^2$.
    - *Correzione:* se $A$ è $m \times n$, ogni riga ha $n$ componenti (sta in **$K^n$**), mentre ogni colonna ha $m$ componenti (sta in **$K^m$**). Il fatto che $\dim_K\mathcal{L}_R(A) = \dim_K\mathcal{L}_C(A) = \operatorname{rk} A$ dice che hanno lo stesso numero di vettori nella base, **non** che vivano nello stesso spazio!
2. **Dimenticare che le operazioni elementari sulle colonne servono per $\mathcal{L}_C(A)$ e quelle sulle righe per $\mathcal{L}_R(A)$**
    - *Sbagliato:* ridurre *per righe* una matrice e poi prendere le righe ridotte come base dello spazio delle *colonne*.
    - *Correzione:* le operazioni sulle righe conservano lo **spazio delle righe** (e il rango!), ma **cambiano** lo spazio delle colonne! Per trovare una base di $\mathcal{L}_C(A)$, riduci per **colonne** oppure tieni le colonne *originali* corrispondenti ai pivot (lo vedremo applicatissimo nel Capitolo 6!).

### 6. Riepilogo

- Per $A \in K^{m,n}$, lo spazio delle righe è $\mathcal{L}_R(A) = \mathcal{L}(R_1,\dots,R_m) \subseteq K^n$, e lo spazio delle colonne è $\mathcal{L}_C(A) = \mathcal{L}(C_1,\dots,C_n) \subseteq K^m$.
- **Teorema di Kronecker:** $\dim_K \mathcal{L}_R(A) = \dim_K \mathcal{L}_C(A) = \operatorname{rk} A$.
- Come applicazione immediata si dimostra il **Teorema di Rouché-Capelli**: $AX = B$ è risolubile $\iff B \in \mathcal{L}_C(A) \iff \dim \mathcal{L}_C(A) = \dim \mathcal{L}_C(A|B) \iff \operatorname{rk} A = \operatorname{rk}(A|B)$.
- Il Teorema di Kronecker implica anche che il rango si può calcolare indifferentemente sia riducendo per righe sia riducendo per colonne.

### 7. Esercizi

Nella Lezione 9 *(pp. 4–5)* questo sottoparagrafo ospita il Teorema di Kronecker e la dimostrazione di Rouché-Capelli; gli esercizi operativi su dimensione, basi ed equazioni minimali mediante Kronecker e Orlati sono raccolti subito dopo nella sezione [5.7](#sec-5-7).

<!-- section: sec-5-7 | num: 5.7 | title: Sistemi omogenei, minori a segno alterno, Teorema degli Orlati ed equazioni di sottospazi | kind: section | part: cap-5 -->

### 1. Idea in parole semplici

In un corso universitario di Algebra Lineare, quasi ogni esercizio di esame su spazi vettoriali e autospazi richiede uno di questi **due passaggi opposti**:
1. **Dalle equazioni cartesiane $\to$ a una base:** hai un sottospazio scritto come sistema omogeneo $AX = \underline{0}$. La dimensione è subito $n - \operatorname{rk} A$, e se sei nel caso comodissimo di **dim = 1** in $\mathbb{R}^3$ ($2$ equazioni indipendenti in $3$ incognite) c'è una scorciatoia fulminea: i **$3$ minori di ordine $2$ presi a segno alterno** $(d_1, d_2, d_3)$ forniscono istantaneamente un vettore di base senza nemmeno fare sostituzioni!
2. **Dai generatori $\to$ alle equazioni cartesiane minimali:** hai un sottospazio generato da $r$ vettori indipendenti e vuoi le sue equazioni cartesiane $ax+by+\dots=0$. Grazie al **Teorema degli Orlati** (che controlla il rango ampliando *solo* un minore iniziale non nullo di ordine $r$ anziché tutti i minori del mondo!), basta imporre che gli **orlati** di ordine $r+1$ costruiti aggiungendo la riga delle incognite $(x, y, z, \dots)$ abbiano determinante nullo!

### 2. Definizioni e enunciati precisi

:::def Definizione e Proposizione — Sistemi lineari omogenei e dimensione (Lezione 9, pp. 5–6)
Un sistema lineare della forma $AX = \underline{0}$ (con $A \in K^{m,n}$) si chiama **sistema lineare omogeneo** *(ed è sempre risolubile perché ammette almeno $X = \underline{0}$)*. L'insieme delle sue soluzioni $S = \{ X \in K^{n,1} \mid AX = \underline{0} \}$ è un sottospazio di $K^n$ di dimensione:

$$\dim_K S = n - \operatorname{rk} A$$
:::

:::thm Metodo rapido dei minori a segno alterno per $\operatorname{rk} A = 2$ in $\mathbb{R}^3$ (Lezione 9, p. 7)
Se un sottospazio $W \subseteq \mathbb{R}^3$ è definito da due equazioni lineari omogenee indipendenti con matrice $A \in \mathbb{R}^{2,3}$ ($\operatorname{rk} A = 2$, quindi $\dim_{\mathbb{R}} W = 1$), una base di $W$ è data dal vettore $(d_1, d_2, d_3)$, dove:
- $d_1 = +\det(\text{minore ottenuto eliminando la colonna } 1)$;
- $d_2 = -\det(\text{minore ottenuto eliminando la colonna } 2)$;
- $d_3 = +\det(\text{minore ottenuto eliminando la colonna } 3)$.
:::

:::def Definizione — Orlato di un minore (Lezione 9, p. 8)
Sia $A \in K^{m,n}$ e sia $M$ un minore di $A$ di ordine $r$. Si chiama **orlato** di $M$ un minore di $A$, di ordine $r + 1$, contenente $M$ *(cioè ottenuto aggiungendo alla sottomatrice di $M$ una riga e una colonna fra le rimanenti di $A$)*.
:::

:::thm Teorema degli Orlati (Lezione 9, p. 8)
Sia $A \in K^{m,n}$. Allora $\operatorname{rk} A = r$ se e solo se:
1. esiste un minore $M$ di $A$ di ordine $r$ **non nullo** *(ovvero $M \neq 0$)*;
2. **tutti** gli orlati di $M$ *(di ordine $r + 1$)* sono nulli.
:::

:::note Nota sugli appunti originali (`Lez09`, p. 8 e p. 9)
1. **Omissione nel Teorema degli Orlati (`Lez09`, p. 8):** nella condizione (1) del teorema nei lucidi è scritto *"Esiste un minore $M$ di $A$ di ordine $r$"*, dimenticando per svista l'aggettivo essenziale **"non nullo"** ($M \neq 0$). Ovviamente senza $M \neq 0$ il teorema sarebbe falso: ogni matrice di rango $< r$ avrebbe un minore nullo di ordine $r$ con tutti i suoi orlati nulli! Qui sopra abbiamo ripristinato la condizione esatta.
2. **Refuso nell'Esercizio 5 (`Lez09`, p. 9):** il testo scrive *"Sia $W = \mathcal{L}((1,1,1,2),(0,3,5,7))$ sottospazio di $\mathbb{R}^5$"* anziché **$\mathbb{R}^4$**. Poiché i due generatori hanno $4$ componenti e lo svolgimento imposta subito $(x,y,z,t) \in W$, lo spazio ambiente esatto è $\mathbb{R}^4$.
:::

### 3. Dimostrazioni

Nella Lezione 9 *(pp. 5–9)* sia la formula $\dim_K S = n - \operatorname{rk} A$, sia il metodo dei minori a segno alterno, sia il Teorema degli Orlati vengono enunciati direttamente e illustrati mediante cinque esercizi guidati in aula.

### 4. Esempi svolti

:::example Esempio 5.7.1 — Dimensione e base da 1 equazione in $\mathbb{R}^3$ (Esercizio 1, Lezione 9, p. 6)
Sia $W = \{(x,y,z) \in \mathbb{R}^3 \mid x + 2y + 3z = 0\}$. Calcolare dimensione e base di $W$.

- La matrice del sistema è $A = (1\ 2\ 3) \in \mathbb{R}^{1,3}$, quindi $\operatorname{rk} A = 1$ e $\dim_{\mathbb{R}} W = 3 - 1 = 2$.
- Esplicitiamo $x = -2y - 3z$ scegliendo $y, z$ come variabili libere:
    $$(x,y,z) = (-2y - 3z,\ y,\ z) = y(-2, 1, 0) + z(-3, 0, 1)$$
    Una base di $W$ è $\mathcal{B} = \{(-2, 1, 0),\ (-3, 0, 1)\}$.
:::

:::example Esempio 5.7.2 — Riduzione vs minori a segno alterno in $\mathbb{R}^3$ (Esercizio 2, Lezione 9, pp. 6–7)
Sia $W = \{(x,y,z) \in \mathbb{R}^3 \mid x + y + 2z = 0,\ x + 4y + 5z = 0\}$.

- **Metodo 1 (riduzione per righe, pp. 6–7):**
    $$A = \begin{pmatrix} 1 & 1 & 2 \\ 1 & 4 & 5 \end{pmatrix} \xrightarrow{R_2 \mapsto R_2 - R_1} \begin{pmatrix} 1 & 1 & 2 \\ 0 & 3 & 3 \end{pmatrix} \xrightarrow{R_2 \mapsto \frac{1}{3}R_2} \begin{pmatrix} \boxed{1} & 1 & 2 \\ 0 & \boxed{1} & 1 \end{pmatrix} \implies \operatorname{rk} A = 2 \implies \dim_{\mathbb{R}} W = 3 - 2 = 1$$
    Dal sistema ridotto $y = -z$, $x = -z$: $(x,y,z) = z(-1,-1,1) \implies$ base $\mathcal{B} = \{(-1,-1,1)\}$.
- **Metodo 2 (minori di ordine $2$ a segno alterno, p. 7):** direttamente su $A = \begin{pmatrix} 1 & 1 & 2 \\ 1 & 4 & 5 \end{pmatrix}$:
    $$d_1 = \det\begin{pmatrix} 1 & 2 \\ 4 & 5 \end{pmatrix} = 5 - 8 = -3, \qquad d_2 = -\det\begin{pmatrix} 1 & 2 \\ 1 & 5 \end{pmatrix} = -(5 - 2) = -3, \qquad d_3 = \det\begin{pmatrix} 1 & 1 \\ 1 & 4 \end{pmatrix} = 4 - 1 = 3$$
    Una base di $W$ è $\{(-3,-3,3)\}$, oppure dividendo per $3$ otteniamo ancora $\mathcal{B}' = \{(-1,-1,1)\}$.
:::

:::example Esempio 5.7.3 — Dimensione e base in $\mathbb{R}^4$ (Esercizio 3, Lezione 9, pp. 7–8)
Sia $W = \{(x,y,z,t) \in \mathbb{R}^4 \mid x+2y+3z+4t=0,\ x+3y+5z+t=0\}$.

$$A = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 1 & 3 & 5 & 1 \end{pmatrix} \xrightarrow{R_2 \mapsto R_2 - R_1} \begin{pmatrix} \boxed{1} & 2 & 3 & 4 \\ 0 & \boxed{1} & 2 & -3 \end{pmatrix} \implies \operatorname{rk} A = 2 \implies \dim_{\mathbb{R}} W = 4 - 2 = 2$$

Con $z, t$ variabili libere: $\begin{cases} y = -2z + 3t \\ x = -2(-2z + 3t) - 3z - 4t = z - 10t \end{cases}$. Dunque $(x,y,z,t) = z(1,-2,1,0) + t(-10,3,0,1)$ e una base di $W$ è $\mathcal{B} = \{(1,-2,1,0),\ (-10,3,0,1)\}$.
:::

:::example Esempio 5.7.4 — Equazioni minimali mediante gli Orlati in $\mathbb{R}^3$ e in $\mathbb{R}^4$ (Esercizi 4 e 5, Lezione 9, pp. 8–9)
1. **Esercizio 4 (in $\mathbb{R}^3$, pp. 8–9):** trovare un sistema minimale di equazioni di $W = \mathcal{L}((1,2,1), (2,5,3))$.
    - $\dim_{\mathbb{R}} W = \operatorname{rk}\begin{pmatrix} 1 & 2 & 1 \\ 2 & 5 & 3 \end{pmatrix} = \operatorname{rk}\begin{pmatrix} \boxed{1} & 2 & 1 \\ 0 & \boxed{1} & 1 \end{pmatrix} = 2$ (quindi serve $3 - 2 = 1$ equazione).
    - Per Kronecker, $(x,y,z) \in W \iff \det\begin{pmatrix} x & y & z \\ 1 & 2 & 1 \\ 0 & 1 & 1 \end{pmatrix} = 0$. Sviluppando lungo la prima riga:
        $$x\det\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} - y\det\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} + z\det\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = 0 \implies x - y + z = 0$$
2. **Esercizio 5 (in $\mathbb{R}^4$, p. 9):** trovare un sistema minimale di equazioni di $W = \mathcal{L}((1,1,1,2), (0,3,5,7))$.
    - $\dim_{\mathbb{R}} W = \operatorname{rk}\begin{pmatrix} \boxed{1} & 1 & 1 & 2 \\ 0 & \boxed{3} & 5 & 7 \end{pmatrix} = 2$ (quindi servono $4 - 2 = 2$ equazioni indipendenti).
    - Prendiamo il minore non nullo $M = \det\begin{pmatrix} 1 & 1 \\ 0 & 3 \end{pmatrix} = 3 \neq 0$ nelle prime due colonne; per il **Teorema degli Orlati**, $(x,y,z,t) \in W \iff \operatorname{rk}\begin{pmatrix} x & y & z & t \\ 1 & 1 & 1 & 2 \\ 0 & 3 & 5 & 7 \end{pmatrix} = 2 \iff$ si annullano i **due** orlati di $M$ ottenuti orlando con la riga $(x,y,z,t)$ e con la colonna $3$ oppure $4$:
        $$\begin{cases} \det\begin{pmatrix} x & y & z \\ 1 & 1 & 1 \\ 0 & 3 & 5 \end{pmatrix} = 0 \\ \det\begin{pmatrix} x & y & t \\ 1 & 1 & 2 \\ 0 & 3 & 7 \end{pmatrix} = 0 \end{cases} \iff \begin{cases} 2x - 5y + 3z = 0 \\ x - 7y + 3t = 0 \end{cases}$$
:::

### 5. Errori comuni e trappole

1. **Dimenticare il segno meno centrale nei minori a segno alterno $(d_1, d_2, d_3)$**
    - *Sbagliato:* scrivere $(d_1, d_2, d_3) = (M_1, M_2, M_3)$ senza cambiare il segno a $d_2$.
    - *Correzione:* i segni alterni sono **$+,\ -,\ +$**: quindi $d_2 = -\det(\text{sottomatrice senza col. 2})$. Se il segno è sbagliato, basta sostituire nell'equazione per accorgersene subito!
2. **Orlando una sottomatrice per trovare le equazioni cartesiane, scegliere un minore di partenza che vale $0$**
    - *Sbagliato:* usare sempre e automaticamente le prime $r$ colonne della matrice dei generatori senza verificare che il minore $r \times r$ sia $\neq 0$.
    - *Correzione:* il Teorema degli Orlati *(Lezione 9, p. 8)* richiede tassativamente un minore di ordine $r$ **non nullo**. Se le prime $r$ colonne hanno determinante $0$, scegli un altro blocco di $r$ colonne linearmente indipendenti (come faremo nell'Esercizio 5.7.2 con le colonne $1, 2, 3$!).

### 6. Riepilogo

- Per un sistema omogeneo $AX = \underline{0}$ ($A \in K^{m,n}$), lo spazio $S$ delle soluzioni ha dimensione $\dim_K S = n - \operatorname{rk} A$.
- Se $\dim_{\mathbb{R}} S = 1$ in $\mathbb{R}^3$ ($\operatorname{rk} A = 2$), una base è subito $(d_1, d_2, d_3)$ (minori di ordine $2$ a segno alterno $+, -, +$).
- Un **orlato** di un minore $M$ di ordine $r$ è un minore di ordine $r+1$ che contiene $M$.
- **Teorema degli Orlati:** $\operatorname{rk} A = r \iff$ esiste un minore $M$ di ordine $r$ **non nullo** e **tutti** gli orlati di $M$ sono nulli.
- Per trovare un sistema minimale di $n - r$ equazioni di un sottospazio $r$-dimensionale in $K^n$, si sceglie un minore non nullo $M$ di ordine $r$ sui generatori e si pongono $= 0$ gli $n - r$ orlati ottenuti aggiungendo la riga $(x_1, \dots, x_n)$ e ciascuna delle colonne restanti.

### 7. Esercizi

:::exercise Esercizio 5.7.1 (Esercizio per casa — Medio · Lezione 9, p. 8)
Sia $W$ il sottospazio di $\mathbb{R}^3$ definito da:

$$W = \{(x,y,z) \in \mathbb{R}^3 \mid x + y + z = 0,\ 3x + 2y + z = 0,\ 5x + 8y + hz = 0\}$$

Calcolare la dimensione ed una base di $W$ al variare di $h \in \mathbb{R}$.

:::solution Soluzione spiegata passo-passo
**Ragionamento:** la dimensione è $3 - \operatorname{rk} A$, dove $A \in \mathbb{R}^{3,3}$ è la matrice dei coefficienti. Calcoliamo prima $\det A$ per separare il caso $\operatorname{rk} A = 3$ (solo $\underline{0}$) dal caso $\det A = 0$ ($\operatorname{rk} A \le 2$).

1. **Matrice dei coefficienti e calcolo di $\det A$:**
    $$A = \begin{pmatrix} 1 & 1 & 1 \\ 3 & 2 & 1 \\ 5 & 8 & h \end{pmatrix}$$
    Sviluppiamo il determinante:
    $$\det A = 2h + 5 + 24 - 10 - 8 - 3h = -h + 11$$
    Pertanto $\det A = 0 \iff h = 11$.

2. **I caso ($h \neq 11$):**
    $\det A \neq 0 \implies \operatorname{rk} A = 3$. Quindi:
    $$\dim_{\mathbb{R}} W = 3 - 3 = 0 \implies W = \{(0, 0, 0)\}$$
    Lo spazio banale $\{\underline{0}\}$ **non ha una base non vuota** *(convenzionalmente $\mathcal{B} = \emptyset$, $\dim_{\mathbb{R}} W = 0$)*.

3. **II caso ($h = 11$):**
    Poiché il minore in alto a sinistra $\det\begin{pmatrix} 1 & 1 \\ 3 & 2 \end{pmatrix} = 2 - 3 = -1 \neq 0$ e $\det A = 0$, si ha $\operatorname{rk} A = 2$, dunque:
    $$\dim_{\mathbb{R}} W = 3 - 2 = 1$$
    Poiché le prime due equazioni hanno rango $2$, la terza è combinazione lineare delle prime due *(infatti $5x+8y+11z = 14(x+y+z) - 3(3x+2y+z)$)*, e $W$ coincide con le soluzioni di $\begin{cases} x+y+z=0 \\ 3x+2y+z=0 \end{cases}$. Calcoliamo i minori di ordine $2$ a segno alterno sulla sottomatrice $\begin{pmatrix} 1 & 1 & 1 \\ 3 & 2 & 1 \end{pmatrix}$:
    $$d_1 = \det\begin{pmatrix} 1 & 1 \\ 2 & 1 \end{pmatrix} = 1 - 2 = -1, \qquad d_2 = -\det\begin{pmatrix} 1 & 1 \\ 3 & 1 \end{pmatrix} = -(1 - 3) = 2, \qquad d_3 = \det\begin{pmatrix} 1 & 1 \\ 3 & 2 \end{pmatrix} = 2 - 3 = -1$$
    Una base di $W$ è quindi $\mathcal{B} = \{(-1, 2, -1)\}$ *(oppure $\{(1, -2, 1)\}$)*:
    - verifica rapida nelle 3 equazioni per $(1,-2,1)$: $1-2+1=0$, $3-4+1=0$, $5-16+11=0$!
:::
:::

:::exercise Esercizio 5.7.2 (Esercizio per casa — Medio · Lezione 9, p. 9)
Sia $W = \mathcal{L}\bigl((1,1,1,1,1),\ (0,2,3,3,2),\ (0,0,1,1,4)\bigr)$ sottospazio di $\mathbb{R}^5$. Calcolare un sistema di equazioni minimale di $W$.

:::solution Soluzione spiegata passo-passo
**Ragionamento:** determiniamo prima la dimensione $r = \dim_{\mathbb{R}} W$ con il Teorema di Kronecker e scegliamo un minore non nullo di ordine $r$; poi applichiamo il Teorema degli Orlati aggiungendo la riga delle incognite $(x,y,z,t,u) \in \mathbb{R}^5$ per ottenere le $5 - r$ equazioni minimali.

1. **Dimensione di $W$ e scelta del minore non nullo $M$:**
    Scriviamo i tre generatori come righe della matrice $G \in \mathbb{R}^{3,5}$:
    $$G = \begin{pmatrix} \boxed{1} & 1 & 1 & 1 & 1 \\ 0 & \boxed{2} & 3 & 3 & 2 \\ 0 & 0 & \boxed{1} & 1 & 4 \end{pmatrix}$$
    La matrice è già ridotta per righe con $3$ elementi speciali ($1, 2, 1$), dunque **$\dim_{\mathbb{R}} W = \operatorname{rk} G = 3$**. Ne segue che un sistema minimale di equazioni cartesiane di $W$ in $\mathbb{R}^5$ sarà composto da $5 - 3 = 2$ equazioni.

    Prendiamo il minore $3 \times 3$ formato dalle prime tre colonne ($x, y, z$), che è triangolare superiore non nullo:
    $$M = \det\begin{pmatrix} 1 & 1 & 1 \\ 0 & 2 & 3 \\ 0 & 0 & 1 \end{pmatrix} = 1\cdot 2\cdot 1 = 2 \neq 0$$

2. **Applicazione del Teorema degli Orlati:**
    Un punto $(x,y,z,t,u) \in \mathbb{R}^5$ appartiene a $W$ se e solo se la matrice ampliata $4 \times 5$ continua ad avere rango $3$, cioè (per il Teorema degli Orlati applicato a $M \neq 0$) se e solo se si annullano i **due orlati** di ordine $4$ ottenuti orlando $M$ con la riga $(x,y,z,t,u)$ e rispettivamente con la colonna $4$ ($t$) e la colonna $5$ ($u$):

    - **Prima equazione (orlando con la colonna $4$ di $t$):**
        $$\det\begin{pmatrix} x & y & z & t \\ 1 & 1 & 1 & 1 \\ 0 & 2 & 3 & 3 \\ 0 & 0 & 1 & 1 \end{pmatrix} = 0$$
        Osserva che nella sottomatrice la colonna $3$ e la colonna $4$ hanno le ultime tre entrate uguali $(1,3,1)^T$! Se sottraiamo la colonna $3$ dalla colonna $4$ ($C_4 \mapsto C_4 - C_3$, il determinante non cambia!), otteniamo subito:
        $$\det\begin{pmatrix} x & y & z & t-z \\ 1 & 1 & 1 & 0 \\ 0 & 2 & 3 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix} = -(t-z)\det\begin{pmatrix} 1 & 1 & 1 \\ 0 & 2 & 3 \\ 0 & 0 & 1 \end{pmatrix} = -2(t-z) = 0 \iff z - t = 0$$
        *(Sviluppando con Laplace lungo la prima riga si ottiene ugualmente $0\cdot x - 0\cdot y + 2z - 2t = 0 \iff z - t = 0$.)*

    - **Seconda equazione (orlando con la colonna $5$ di $u$):**
        $$\det\begin{pmatrix} x & y & z & u \\ 1 & 1 & 1 & 1 \\ 0 & 2 & 3 & 2 \\ 0 & 0 & 1 & 4 \end{pmatrix} = 0$$
        Sviluppiamo con il Primo Teorema di Laplace lungo la prima riga:
        $$x\det\begin{pmatrix} 1 & 1 & 1 \\ 2 & 3 & 2 \\ 0 & 1 & 4 \end{pmatrix} - y\det\begin{pmatrix} 1 & 1 & 1 \\ 0 & 3 & 2 \\ 0 & 1 & 4 \end{pmatrix} + z\det\begin{pmatrix} 1 & 1 & 1 \\ 0 & 2 & 2 \\ 0 & 0 & 4 \end{pmatrix} - u\det\begin{pmatrix} 1 & 1 & 1 \\ 0 & 2 & 3 \\ 0 & 0 & 1 \end{pmatrix} = 0$$
        Calcoliamo i $4$ determinanti $3\times 3$:
        - coeff. di $x$: $1(12-2) - 2(4-1) = 10 - 6 = 4$;
        - coeff. di $y$: $-(12 - 2) = -10$;
        - coeff. di $z$: $+(8) = 8$;
        - coeff. di $u$: $-(2) = -2$.
        Quindi $4x - 10y + 8z - 2u = 0$, che dividendo per $2$ si semplifica in:
        $$2x - 5y + 4z - u = 0$$

3. **Sistema minimale di equazioni di $W$ e verifica sui $3$ generatori:**
    $$\begin{cases} z - t = 0 \\ 2x - 5y + 4z - u = 0 \end{cases}$$
    Verifichiamo sui $3$ vettori generatori:
    - $(1,1,1,1,1)$: $1-1=0$ e $2-5+4-1=0$ (OK);
    - $(0,2,3,3,2)$: $3-3=0$ e $0-10+12-2=0$ (OK);
    - $(0,0,1,1,4)$: $1-1=0$ e $0-0+4-4=0$ (OK).
:::
:::
