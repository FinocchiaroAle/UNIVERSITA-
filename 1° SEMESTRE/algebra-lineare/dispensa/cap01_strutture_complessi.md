<!-- part: cap-1 | num: 1 | label: CAPITOLO 1 | title: Strutture algebriche e campo dei numeri complessi | refs: Fonti: Lezione 1 (senza data, pp. 1–8), Lezione 2 (7/10/2026, pp. 1–8) -->

<!-- section: sec-1-1 | num: 1.1 | title: Insiemi numerici, prodotto cartesiano e operazioni binarie interne | kind: section | part: cap-1 -->

### 1. Idea in parole semplici

Prima di parlare di matrici, vettori ed equazioni, l'Algebra Lineare parte da una domanda semplicissima: **che cos'è davvero un'operazione matematica?**

Quando fai $2 + 3 = 5$, stai prendendo **due numeri** messi in un certo ordine, cioè la coppia $(2,3)$, e stai producendo **un nuovo numero** nello stesso insieme, cioè $5$. Pensa a una macchina con due bocchette d'ingresso e un'unica uscita: inserisci due elementi di un insieme $A$ e la macchina restituisce ancora un elemento di $A$. Se la macchina è definita su tutti i possibili ingressi e non "esce mai" dall'insieme $A$, allora hai costruito una **struttura algebrica** elementare.

:::note Nota sugli appunti originali (`Lez01`, p. 1)
La Lezione 1 è l'unica lezione di teoria nei file forniti a non riportare una data nell'intestazione (la Lezione 2 inizia il 7/10/2026).
:::

### 2. Definizioni e enunciati precisi

Richiamiamo prima i tre insiemi numerici di partenza *(Lezione 1, p. 1)*:

- **Numeri interi:** $\mathbb{Z} = \{0, \pm 1, \pm 2, \dots\}$.
- **Numeri razionali:** $\mathbb{Q} = \{\text{tutte le frazioni}\}$ *(numeri esprimibili come rapporto di interi con denominatore non nullo)*.
- **Numeri reali:** $\mathbb{R}$.

Una **coppia ordinata** $(a,b)$ è una lista di due elementi in cui conta l'ordine: in generale $(a,b) \neq (b,a)$ se $a \neq b$.

:::def Definizione — Prodotto cartesiano (Lezione 1, p. 1)
Siano $A$ e $B$ due insiemi. Si chiama **prodotto cartesiano** di $A$ per $B$ l'insieme di tutte le coppie ordinate con il primo elemento in $A$ e il secondo in $B$:

$$A \times B \stackrel{\text{DEF}}{=} \{(a,b) \mid a \in A,\ b \in B\}$$
:::

:::def Definizione — Operazione binaria interna e notazione (Lezione 1, p. 2)
Sia $A$ un insieme. Si chiama **operazione binaria interna** su $A$ una funzione

$$A \times A \xrightarrow{f} A$$

Se $(a,b) \in A \times A$ (quindi $a \in A$ e $b \in A$), il suo risultato $f((a,b)) \in A$ si indica in notazione infissa con un simbolo di operazione $*$ scrivendo:

$$a * b \stackrel{\text{DEF}}{=} f((a,b))$$
:::

La parola **binaria** indica che l'operazione prende *due* operandi alla volta; la parola **interna** indica che il risultato resta *dentro* lo stesso insieme $A$ (si dice anche che $A$ è chiuso rispetto all'operazione).

:::def Definizione — Struttura algebrica (Lezione 1, p. 2)
Si chiama **struttura algebrica** un insieme su cui sono definite delle operazioni.
:::

### 3. Dimostrazioni

In questa sezione introduttiva delle lezioni *(Lezione 1, pp. 1–2)* non sono presenti dimostrazioni: vengono poste le definizioni di base che useremo immediatamente dalla sezione seguente.

### 4. Esempi svolti

:::example Esempio 1.1.1 — Operazioni su $\mathbb{Z}$ come funzioni (Lezione 1, p. 1)
Presi $2 \in \mathbb{Z}$ e $3 \in \mathbb{Z}$:
- l'**addizione** associa alla coppia $(2,3) \in \mathbb{Z} \times \mathbb{Z}$ il numero $2 + 3 = 5 \in \mathbb{Z}$, cioè $(2,3) \mapsto 5$;
- la **moltiplicazione** associa alla coppia $(2,3) \in \mathbb{Z} \times \mathbb{Z}$ il numero $2 \times 3 = 6 \in \mathbb{Z}$, cioè $(2,3) \mapsto 6$.

Poiché somma e prodotto di due numeri interi danno sempre un numero intero, sia $+$ che $\times$ sono operazioni binarie interne su $\mathbb{Z}$.
:::

:::example Esempio 1.1.2 — Calcolo esplicito di un prodotto cartesiano (Lezione 1, p. 2)
Siano $A = \{1, 2, 3\}$ e $B = \{3, 5\}$. Per elencare tutti gli elementi di $A \times B$ fissiamo ciascun elemento di $A$ e lo accoppiamo con ogni elemento di $B$:

$$A \times B = \{(1,3),\ (1,5),\ (2,3),\ (2,5),\ (3,3),\ (3,5)\}$$

Poiché $A$ ha $3$ elementi e $B$ ha $2$ elementi, il prodotto cartesiano contiene $3 \cdot 2 = 6$ coppie ordinate.
:::

### 5. Errori comuni e trappole

1. **Confondere il prodotto cartesiano $A \times B$ con un insieme di insiemi $\{a,b\}$**
    - *Sbagliato:* scrivere $(1,3) = (3,1)$ o pensare che in $(a,b)$ l'ordine non conti.
    - *Correzione:* nell'esempio 1.1.2 la coppia $(3,5)$ appartiene ad $A \times B$, ma $(5,3)$ **non** appartiene ad $A \times B$ perché $5 \notin A$. Nelle coppie ordinate l'ordine è essenziale.
2. **Dimenticare la parola "interna" in operazione binaria interna**
    - *Sbagliato:* affermare che la divisione $\div$ sia un'operazione binaria interna su $\mathbb{Z}$ o che la sottrazione sia interna su $\mathbb{N}$.
    - *Correzione:* in $\mathbb{Z}$, $1 \div 2 = \frac{1}{2} \notin \mathbb{Z}$; il risultato esce dall'insieme, quindi $\div$ non è un'operazione binaria interna su $\mathbb{Z}$.

### 6. Riepilogo

- Gli insiemi numerici di base richiamati sono $\mathbb{Z}$ (interi), $\mathbb{Q}$ (razionali) e $\mathbb{R}$ (reali).
- Il prodotto cartesiano $A \times B$ raccoglie tutte le coppie ordinate $(a,b)$ con $a \in A$ e $b \in B$.
- Un'operazione binaria interna su $A$ è una funzione $f: A \times A \to A$, scritta $a * b = f((a,b))$.
- "Interna" significa che operando su due elementi di $A$ si resta sempre in $A$.
- Un insieme dotato di una o più operazioni si chiama **struttura algebrica**.

### 7. Esercizi

Le lezioni *(Lezione 1, pp. 1–2)* non assegnano esercizi per casa specifici su questo primo sottoparagrafo introduttivo; gli esercizi ufficiali del Capitolo 1 si trovano nelle sezioni [1.5](#sec-1-5) e [1.6](#sec-1-6). Per prendere dimestichezza, prova a scrivere per esteso $B \times A$ con gli insiemi dell'Esempio 1.1.2 e verifica che è diverso da $A \times B$.

<!-- section: sec-1-2 | num: 1.2 | title: Magma, semigruppo, monoide: elemento neutro e elemento inverso | kind: section | part: cap-1 -->

### 1. Idea in parole semplici

Un insieme con una sola operazione può essere "selvaggio" oppure molto ordinato. Per descrivere quanto è ordinato, i matematici procedono a gradini:

- Al gradino base c'è il **magma**: hai solo l'operazione, senza garanzie.
- Se puoi spostare le parentesi nei calcoli senza cambiare il risultato, sali al **semigruppo**.
- Se c'è anche un elemento "trasparente" che lascia tutto invariato (come lo $0$ per la somma o l'$1$ per il prodotto), sali al **monoide**.
- A questo punto puoi chiederti se ogni mossa ha una "mossa contraria" che ti riporta all'elemento neutro: quello è l'**inverso**.

### 2. Definizioni e enunciati precisi

:::def Definizione — Magma (Lezione 1, p. 2)
Si chiama **magma** la struttura algebrica $(A,*)$ costituita da un insieme $A$ su cui è definita una operazione binaria interna $*$.
:::

:::def Definizione — Proprietà associativa (Lezione 1, p. 3)
Sia $(A,*)$ un magma. Diremo che l'operazione $*$ gode della **proprietà associativa** se

$$(a * b) * c = a * (b * c) \qquad \forall a,b,c \in A$$
:::

:::def Definizione — Elemento neutro (Lezione 1, p. 3)
Sia $(A,*)$ un magma. Diremo che l'operazione $*$ ha **elemento neutro** se esiste un elemento $e \in A$ tale che

$$a * e = e * a = a \qquad \forall a \in A$$
:::

**Osservazione *(Lezione 1, p. 3)*:** per l'addizione l'elemento neutro è $e = 0$; per la moltiplicazione l'elemento neutro è $e = 1$.

:::thm Proposizione — Unicità dell'elemento neutro (Lezione 1, p. 3)
Sia $(A,*)$ un magma. Se esiste l'elemento neutro, esso è **unico**.
:::

:::def Definizione — Semigruppo e Monoide (Lezione 1, p. 4)
- Si chiama **semigruppo** un magma $(A,*)$ la cui operazione $*$ è associativa.
- Si chiama **monoide** un semigruppo $(A,*)$ in cui esiste l'elemento neutro.
:::

:::def Definizione — Elemento invertibile e inverso (Lezione 1, pp. 4–5)
Sia $(A,*)$ un monoide con elemento neutro $e$, e sia $a \in A$. Diremo che $a$ è **invertibile** se $\exists b \in A$ tale che

$$a * b = b * a = e$$

L'elemento $b$ è detto un **inverso** di $a$. Quando l'inverso è unico, lo si indica con il simbolo $a^{-1}$, sicché:

$$a * a^{-1} = a^{-1} * a = e$$
:::

:::thm Proposizione — Unicità dell'inverso in un monoide (Lezione 1, p. 4)
Sia $(A,*)$ un monoide. Se $a \in A$ è invertibile, allora $a$ ha **un unico inverso**.
:::

:::thm Proposizione — Inverso del prodotto in un monoide (Lezione 1, p. 5)
Sia $(A,*)$ un monoide e siano $a, b \in A$ due elementi invertibili. Allora anche $a * b$ è invertibile e vale la formula di inversione dell'ordine:

$$(a * b)^{-1} = b^{-1} * a^{-1}$$
:::

### 3. Dimostrazioni

:::proof Dimostrazione 1 — Unicità dell'elemento neutro in un magma (Lezione 1, p. 3)
**Idea di fondo:** supponiamo per assurdo o per ipotesi di avere due elementi neutri diversi $e$ ed $e'$, poi confrontiamo il prodotto $e * e'$ sfruttando la neutralità di ciascuno dei due.

Siano $e, e' \in A$ due elementi neutri del magma $(A,*)$. Allora:
- essendo $e$ elemento neutro a sinistra, $e * e' = e'$;
- essendo $e'$ elemento neutro a destra, $e * e' = e$.

Poiché $e * e'$ è un unico elemento di $A$, segue immediatamente $e = e'$.
:::

:::proof Dimostrazione 2 — Unicità dell'inverso in un monoide (Lezione 1, p. 4)
**Idea di fondo:** prendiamo due presunti inversi $x$ e $y$ di $a$ e valutiamo l'espressione a tre fattori $x * a * y$ in due modi diversi usando la proprietà associativa.

Siano $x \in A$ e $y \in A$ due inversi di $a$. Poiché $(A,*)$ è un monoide, vale la proprietà associativa:

$$(x * a) * y = x * (a * y)$$

Calcoliamo separatamente i due membri:
- $(x * a) * y = e * y = y$ *(perché $x$ è inverso di $a$ ed $e$ è neutro)*;
- $x * (a * y) = x * e = x$ *(perché $y$ è inverso di $a$ ed $e$ è neutro)*.

Uguagliando i due risultati otteniamo $x = y$. L'inverso di $a$ è dunque unico.
:::

:::proof Dimostrazione 3 — Formula dell'inverso del prodotto: $(a * b)^{-1} = b^{-1} * a^{-1}$ (Lezione 1, p. 5)
**Idea di fondo:** per dimostrare che $b^{-1} * a^{-1}$ è l'unico inverso di $a * b$, basta moltiplicarlo sia a destra sia a sinistra per $a * b$ e verificare che in entrambi i casi si ottiene l'elemento neutro $e$.

Verifichiamo i due versi sfruttando la proprietà associativa del monoide:

1. Moltiplicazione a destra:
$$(a * b) * (b^{-1} * a^{-1}) = a * (b * b^{-1}) * a^{-1} = (a * e) * a^{-1} = a * a^{-1} = e$$

2. Moltiplicazione a sinistra:
$$(b^{-1} * a^{-1}) * (a * b) = b^{-1} * (a^{-1} * a) * b = (b^{-1} * e) * b = b^{-1} * b = e$$

Pertanto $b^{-1} * a^{-1}$ soddisfa la definizione di inverso di $a * b$; per l'unicità dell'inverso segue $(a * b)^{-1} = b^{-1} * a^{-1}$.
:::

### 4. Esempi svolti

:::example Esempio 1.2.1 — Verifica numerica di associatività e neutro (Lezione 1, p. 3)
Nell'addizione ordinaria:
- **Associatività:** calcoliamo $(2+3)+4$ e $2+(3+4)$:
    $$(2+3)+4 = 5+4 = 9, \qquad 2+(3+4) = 2+7 = 9$$
    I due risultati coincidono.
- **Elemento neutro:** $5 + 0 = 5$ e $0 + 5 = 5$, quindi $0$ è l'elemento neutro dell'addizione.
:::

:::example Esempio 1.2.2 — Il monoide additivo $(\mathbb{Z}, +)$ e l'inverso additivo (Lezione 1, p. 4)
La struttura $(\mathbb{Z}, +)$ è un **monoide**:
1. $+$ è un'operazione binaria interna su $\mathbb{Z}$;
2. l'addizione è associativa;
3. esiste l'elemento neutro, che è $0 \in \mathbb{Z}$.

Prendiamo $2 \in \mathbb{Z}$: poiché $2 + (-2) = (-2) + 2 = 0$, l'elemento $-2 \in \mathbb{Z}$ è l'**inverso additivo** (o *opposto*) di $2$.
:::

### 5. Errori comuni e trappole

1. **Scambiare l'ordine in $(a * b)^{-1}$**
    - *Sbagliato:* scrivere $(a * b)^{-1} = a^{-1} * b^{-1}$ in un monoide generico.
    - *Correzione:* $(a * b)^{-1} = b^{-1} * a^{-1}$. Se l'operazione non è commutativa (come accadrà prestissimo con il prodotto tra matrici nel Capitolo 2!), invertire l'ordine è obbligatorio: pensa al gesto di mettere prima le calze ($a$) e poi le scarpe ($b$); per disfare tutto devi togliere prima le scarpe ($b^{-1}$) e poi le calze ($a^{-1}$).
2. **Controllare l'elemento neutro o l'inverso da un solo lato**
    - *Sbagliato:* verificare solo $a * e = a$ o solo $a * b = e$.
    - *Correzione:* se l'operazione non è commutativa, la definizione richiede **entrambi i lati**: $a * e = e * a = a$ e $a * b = b * a = e$.
3. **Confondere la notazione astratta $a^{-1}$ con il reciproco aritmetico $1/a$**
    - *Sbagliato:* in $(\mathbb{Z}, +)$, pensare che l'inverso di $2$ sia $1/2$.
    - *Correzione:* $a^{-1}$ indica l'inverso rispetto all'operazione $*$ del monoide considerato. In $(\mathbb{Z}, +)$ il simbolo $2^{-1}$ rappresenterebbe l'inverso additivo $-2$ (anche se per l'addizione si usa di norma $-a$).

### 6. Riepilogo

- Un **magma** $(A,*)$ è un insieme con una operazione binaria interna.
- Un **semigruppo** è un magma associativo: $(a*b)*c = a*(b*c)$.
- Un **monoide** è un semigruppo con elemento neutro $e$ ($a*e=e*a=a$), che se esiste è **unico**.
- In un monoide, un eventuale inverso $a^{-1}$ ($a*a^{-1}=a^{-1}*a=e$) è **unico**.
- L'inverso di un prodotto inverte l'ordine dei fattori: $(a * b)^{-1} = b^{-1} * a^{-1}$.

### 7. Esercizi

Le lezioni *(Lezione 1, pp. 2–5)* non contengono esercizi per casa specifici su questo sottoparagrafo; tutti i concetti vengono applicati immediatamente negli esempi della sezione [1.3](#sec-1-3) e negli esercizi di [1.5](#sec-1-5) e [1.6](#sec-1-6).

<!-- section: sec-1-3 | num: 1.3 | title: Gruppi e gruppi abeliani | kind: section | part: cap-1 -->

### 1. Idea in parole semplici

Un **gruppo** è un monoide in cui nessuno resta bloccato: per *ogni* elemento esiste sempre l'operazione inversa che lo riporta all'elemento neutro. Se poi l'ordine con cui applichi l'operazione a due elementi è indifferente (cioè puoi scambiare $a$ e $b$), il gruppo si chiama **abeliano** (in onore del matematico Niels Henrik Abel) o *commutativo*.

### 2. Definizioni e enunciati precisi

:::def Definizione — Gruppo (Lezione 1, p. 5)
Si chiama **gruppo** un monoide $(A,*)$ in cui **ogni** elemento è invertibile.
:::

Srotolando tutte le definizioni precedenti, $(A,*)$ è un gruppo se e solo se soddisfa $4$ assiomi:
1. $*$ è un'operazione binaria interna su $A$;
2. $*$ è associativa;
3. esiste l'elemento neutro $e \in A$;
4. $\forall a \in A,\ \exists a^{-1} \in A$ tale che $a * a^{-1} = a^{-1} * a = e$.

:::def Definizione — Gruppo abeliano (Lezione 1, p. 5)
Un gruppo $(A,*)$ si dice **abeliano** se l'operazione $*$ gode della **proprietà commutativa**, ovvero se:

$$a * b = b * a \qquad \forall a, b \in A$$
:::

| Struttura $(A,*)$ | Interna su $A$ | Associativa | Elemento neutro $e$ | Tutti invertibili | Commutativa |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Magma** | Sì | — | — | — | — |
| **Semigruppo** | Sì | Sì | — | — | — |
| **Monoide** | Sì | Sì | Sì | — | — |
| **Gruppo** | Sì | Sì | Sì | Sì | — |
| **Gruppo abeliano** | Sì | Sì | Sì | Sì | Sì |

### 3. Dimostrazioni

In questa sezione delle lezioni *(Lezione 1, pp. 5–6)* non sono svolte dimostrazioni astratte aggiuntive: la teoria viene applicata direttamente attraverso i sei esempi fondamentali riportati qui sotto.

### 4. Esempi svolti

:::example Esempio 1.3.1 — $(\mathbb{Z}, +)$ è un gruppo abeliano (Lezione 1, p. 6)
Verifichiamo una per una tutte le proprietà richieste:
- **(a)** l'addizione è un'operazione binaria interna su $\mathbb{Z}$ (somma di due interi è un intero);
- **(b)** l'addizione è associativa;
- **(c)** esiste l'elemento neutro, che è lo zero $0 \in \mathbb{Z}$;
- **(d)** $\forall n \in \mathbb{Z}$, l'inverso di $n$ è $-n \in \mathbb{Z}$, quindi ogni elemento è invertibile;
- **(e)** l'addizione è commutativa ($m + n = n + m$).

Quindi $(\mathbb{Z}, +)$ è un **gruppo abeliano**.
:::

:::example Esempio 1.3.2 — $(\mathbb{Z}, \times)$ è un monoide, ma NON è un gruppo (Lezione 1, p. 6)
Controlliamo le condizioni su $(\mathbb{Z}, \times)$:
- **(a)** la moltiplicazione è un'operazione binaria interna su $\mathbb{Z}$;
- **(b)** la moltiplicazione è associativa;
- **(c)** esiste l'elemento neutro, che è $1 \in \mathbb{Z}$.

Fino qui $(\mathbb{Z}, \times)$ è dunque un **monoide**. Tuttavia **non è un gruppo**: prendiamo per esempio $2 \in \mathbb{Z}$; non esiste alcun numero intero $x \in \mathbb{Z}$ tale che $2 \times x = 1$ (la soluzione $1/2$ non sta in $\mathbb{Z}$). Basta un solo elemento non invertibile perché la struttura non sia un gruppo.
:::

:::example Esempio 1.3.3 — Gruppi abeliani su $\mathbb{Q}$ e $\mathbb{R}$ (Lezione 1, p. 6)
Le quattro strutture seguenti sono tutte **gruppi abeliani**:
- **(3)** $(\mathbb{Q}, +)$ *(neutro $0$, inverso di $q$ è $-q$)*;
- **(4)** $(\mathbb{Q} \setminus \{0\}, \times)$ *(neutro $1$, inverso di $p/q \neq 0$ è $q/p$)*;
- **(5)** $(\mathbb{R}, +)$ *(neutro $0$, inverso di $x$ è $-x$)*;
- **(6)** $(\mathbb{R} \setminus \{0\}, \times)$ *(neutro $1$, inverso di $x \neq 0$ è $1/x$)*.

Nota perché negli esempi moltiplicativi **(4)** e **(6)** bisogna **togliere lo $0$**: lo zero non ha mai inverso moltiplicativo!
:::

### 5. Errori comuni e trappole

1. **Scrivere che $(\mathbb{Q}, \times)$ o $(\mathbb{R}, \times)$ è un gruppo**
    - *Sbagliato:* dimenticare di escludere lo $0$ nell'insieme di sostegno per la moltiplicazione.
    - *Correzione:* $(\mathbb{R}, \times)$ è solo un monoide commutativo, perché $0 \cdot x = 0 \neq 1$ per ogni $x \in \mathbb{R}$. Solo $(\mathbb{R} \setminus \{0\}, \times)$ e $(\mathbb{Q} \setminus \{0\}, \times)$ sono gruppi abeliani.
2. **Pensare che $(\mathbb{Z}, -)$ (con la sottrazione) sia un gruppo**
    - *Sbagliato:* dire che la sottrazione su $\mathbb{Z}$ forma un gruppo perché ogni numero ha l'opposto.
    - *Correzione:* la sottrazione **non è associativa**! Per esempio $(10 - 5) - 2 = 3$, ma $10 - (5 - 2) = 7$. Non è neanche un semigruppo.

### 6. Riepilogo

- Un **gruppo** è un monoide in cui ogni elemento è invertibile.
- Un **gruppo abeliano** è un gruppo in cui vale anche la proprietà commutativa $a * b = b * a$.
- $(\mathbb{Z}, +)$, $(\mathbb{Q}, +)$ e $(\mathbb{R}, +)$ sono gruppi abeliani.
- $(\mathbb{Z}, \times)$ è solo un monoide (ad esempio $2$ non è invertibile in $\mathbb{Z}$).
- Per la moltiplicazione servono gli insiemi senza zero: $(\mathbb{Q} \setminus \{0\}, \times)$ e $(\mathbb{R} \setminus \{0\}, \times)$ sono gruppi abeliani.

### 7. Esercizi

Le lezioni *(Lezione 1, pp. 5–6)* non assegnano esercizi per casa specifici su questo sottoparagrafo; come verifica personale, controlla tutti i 5 assiomi su $(\mathbb{Q} \setminus \{0\}, \times)$ seguendo il modello dell'Esempio 1.3.1.

<!-- section: sec-1-4 | num: 1.4 | title: Anelli, anelli unitari, corpi e campi | kind: section | part: cap-1 -->

### 1. Idea in parole semplici

Finora abbiamo studiato insiemi con **una** sola operazione. Ma negli insiemi numerici più utili (come $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, e tra poco i numeri complessi $\mathbb{C}$ e le matrici quadrate $K^{n,n}$) convivono **due** operazioni: una *addizione* ($+$) e una *moltiplicazione* ($\cdot$), collegate tra loro dalla proprietà distributiva.

A seconda di quanto è "comoda" la moltiplicazione, otteniamo quattro strutture sempre più ricche:
- **Anello**: puoi sempre sommare, sottrarre ($-a$) e moltiplicare in modo associativo, con la proprietà distributiva.
- **Anello unitario**: c'è anche l'unità $1$ per la moltiplicazione (ma non è detto che tutti gli elementi $\neq 0$ siano invertibili, come succede in $\mathbb{Z}$ o nelle matrici).
- **Corpo**: tutti gli elementi diversi da $0$ hanno l'inverso moltiplicativo (ma il prodotto può ancora non essere commutativo).
- **Campo**: è il massimo della comodità algebrica — tutti gli elementi $\neq 0$ sono invertibili *e* la moltiplicazione è commutativa (es. $\mathbb{Q}, \mathbb{R}, \mathbb{C}$).

### 2. Definizioni e enunciati precisi

Consideriamo un insieme $A$ su cui sono definite due operazioni binarie interne: $+$ (*addizione*) e $\cdot$ (*moltiplicazione*), denotate dalla terna $(A, +, \cdot)$ *(Lezione 1, p. 7)*.

:::def Definizione — Anello (Lezione 1, p. 7)
Diremo che $(A, +, \cdot)$ è un **anello** se:
1. $(A, +)$ è un gruppo abeliano;
2. $(A, \cdot)$ è un semigruppo *(cioè $\cdot$ è associativa)*;
3. valgono le **proprietà distributive**:

    - **(3A)** $a \cdot (b + c) = a \cdot b + a \cdot c \quad \forall a,b,c \in A$;
    - **(3B)** $(a + b) \cdot c = a \cdot c + b \cdot c \quad \forall a,b,c \in A$.
:::

**Notazioni nell'anello *(Lezione 1, p. 7)*:**
- L'elemento neutro dell'addizione si indica con $0$ (**zero**).
- $\forall a \in A$, l'inverso di $a$ rispetto all'addizione (detto *opposto*) si indica con $-a$, quindi $a + (-a) = (-a) + a = 0$.

:::def Definizione — Anello unitario (Lezione 1, pp. 7–8; Lezione 2, p. 1)
Si chiama **anello unitario** un anello $(A, +, \cdot)$ in cui esiste l'elemento neutro per la moltiplicazione, che si indica con $1$ (**unità**):

$$a \cdot 1 = 1 \cdot a = a \qquad \forall a \in A$$

Se $a \in A$ è invertibile rispetto alla moltiplicazione, il suo inverso moltiplicativo si indica con $a^{-1}$, quindi $a \cdot a^{-1} = a^{-1} \cdot a = 1$.
:::

:::thm Proposizione e Osservazione sullo zero negli anelli (Lezione 1, p. 8)
1. **Legge di annullamento con lo zero:** Sia $(A, +, \cdot)$ un anello. Allora:
    $$a \cdot 0 = 0 \cdot a = 0 \qquad \forall a \in A$$
2. **Non invertibilità dello zero:** In un anello unitario $(A, +, \cdot)$ avente più di un elemento, si ha $0 \neq 1$ e **lo zero $0$ non è invertibile** rispetto alla moltiplicazione.
:::

:::def Definizione — Corpo (Lezione 2, p. 1)
Si chiama **corpo** un anello unitario $(A, +, \cdot)$ tale che ogni elemento non nullo è invertibile rispetto alla moltiplicazione:

$$\forall a \in A,\ a \neq 0 \implies a \text{ è invertibile rispetto a } \cdot$$
:::

:::def Definizione — Campo (Lezione 2, p. 1)
Si chiama **campo** un corpo $(A, +, \cdot)$ in cui l'operazione di moltiplicazione è commutativa ($a \cdot b = b \cdot a\ \forall a,b \in A$).
:::

| Struttura $(A,+,\cdot)$ | $(A,+)$ gruppo abeliano | $(A,\cdot)$ associativa + distrib. | Esiste unità $1$ | $\forall a \neq 0,\ \exists a^{-1}$ | $\cdot$ commutativa | Esempio dalle lezioni |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Anello** | Sì | Sì | — | — | — | *(anello generale)* |
| **Anello unitario** | Sì | Sì | Sì | — | — | $(\mathbb{Z},+,\cdot)$, $(K^{n,n},+,\cdot)$ |
| **Corpo** | Sì | Sì | Sì | Sì | — | *(struttura non commutativa)* |
| **Campo** | Sì | Sì | Sì | Sì | Sì | $(\mathbb{Q},+,\cdot)$, $(\mathbb{R},+,\cdot)$, $(\mathbb{C},+,\cdot)$ |

### 3. Dimostrazioni

:::proof Dimostrazione — In ogni anello $a \cdot 0 = 0 \cdot a = 0$ e non invertibilità di $0$ (Lezione 1, p. 8)
**Idea di fondo:** lo zero è definito dall'addizione ($0 + 0 = 0$). Per farlo interagire con il prodotto $\cdot$ usiamo proprio la proprietà distributiva, scrivendo $0 = 0 + 0$ e poi cancellando un addendo sommando l'opposto.

**(1) Dimostriamo che $a \cdot 0 = 0$:**
Partiamo da $a \cdot 0$ e sostituiamo $0$ con $0 + 0$:

$$a \cdot 0 = a \cdot (0 + 0) = a \cdot 0 + a \cdot 0 \qquad \text{(per distributività 3A)}$$

Sappiamo che $(A,+)$ è un gruppo abeliano, quindi l'elemento $a \cdot 0$ possiede un opposto $-(a \cdot 0)$. Sommiamolo a destra a entrambi i membri e applichiamo l'associatività di $+$:

$$a \cdot 0 + (-(a \cdot 0)) = a \cdot 0 + \bigl(a \cdot 0 + (-(a \cdot 0))\bigr) \implies 0 = a \cdot 0 + 0 \implies a \cdot 0 = 0$$

**(2) Dimostriamo che $0 \cdot a = 0$:**
In modo analogo usiamo la distributività a destra (3B):

$$0 \cdot a = (0 + 0) \cdot a = 0 \cdot a + 0 \cdot a$$

Sommando a entrambi i membri l'opposto $-(0 \cdot a)$ otteniamo:

$$0 \cdot a + (-(0 \cdot a)) = 0 \cdot a + \bigl(0 \cdot a + (-(0 \cdot a))\bigr) \implies 0 = 0 \cdot a + 0 \implies 0 \cdot a = 0$$

**Osservazione sullo zero non invertibile:** se esistesse $x \in A$ con $0 \cdot x = 1$, poiché per la parte (2) vale $0 \cdot x = 0$, seguirebbe $0 = 1$. In tal caso per ogni $a \in A$ si avrebbe $a = a \cdot 1 = a \cdot 0 = 0$, quindi $A = \{0\}$ avrebbe un solo elemento. Se $A$ ha almeno due elementi ($0 \neq 1$), $0$ non può essere invertibile.
:::

### 4. Esempi svolti

:::example Esempio 1.4.1 — $(\mathbb{Z}, +, \cdot)$ è un anello unitario, ma NON è un corpo (Lezione 2, p. 1)
In $(\mathbb{Z}, +, \cdot)$:
- $(\mathbb{Z}, +)$ è un gruppo abeliano *(Esempio 1.3.1)*;
- la moltiplicazione è associativa, distributiva rispetto a $+$ e ha l'unità $1 \in \mathbb{Z}$.

Quindi $(\mathbb{Z}, +, \cdot)$ è un **anello unitario** (e anche commutativo). Tuttavia **non è un corpo** perché l'elemento non nullo $2 \in \mathbb{Z}$ non è invertibile rispetto alla moltiplicazione: l'equazione $2x = 1$ è impossibile su $\mathbb{Z}$.
:::

:::example Esempio 1.4.2 — Campi razionali e reali (Lezione 2, p. 1)
- $(\mathbb{Q}, +, \cdot)$ è un **campo**, detto *campo dei numeri razionali*.
- $(\mathbb{R}, +, \cdot)$ è un **campo**, detto *campo dei numeri reali*.

In entrambi i casi $(\mathbb{Q},+)$ e $(\mathbb{R},+)$ sono gruppi abeliani, $(\mathbb{Q}\setminus\{0\}, \cdot)$ e $(\mathbb{R}\setminus\{0\}, \cdot)$ sono gruppi abeliani (quindi ogni elemento $\neq 0$ è invertibile e $\cdot$ è commutativo), e valgono le proprietà distributive.
:::

### 5. Errori comuni e trappole

1. **Dimenticare la distributività tra $+$ e $\cdot$**
    - *Sbagliato:* dire che $(A,+,\cdot)$ è un anello solo perché $(A,+)$ è un gruppo abeliano e $(A,\cdot)$ è un semigruppo.
    - *Correzione:* senza le proprietà distributive **(3A)** e **(3B)** le due operazioni sarebbero completamente slegate! Ad esempio, nella dimostrazione di $a \cdot 0 = 0$ la distributività è il passaggio decisivo.
2. **Scambiare "anello unitario commutativo" con "campo"**
    - *Sbagliato:* pensare che $\mathbb{Z}$ sia un campo perché il prodotto tra interi è commutativo ed esiste $1$.
    - *Correzione:* in un **campo**, oltre alla commutatività del prodotto e all'unità $1$, *ogni* elemento non nullo deve avere l'inverso moltiplicativo nell'insieme. $\mathbb{Z}$ fallisce per $2, 3, -5, \dots$ (solo $1$ e $-1$ sono invertibili in $\mathbb{Z}$).

### 6. Riepilogo

- Un **anello** $(A,+,\cdot)$ ha $(A,+)$ gruppo abeliano, $(A,\cdot)$ semigruppo e entrambe le proprietà distributive.
- In ogni anello vale $a \cdot 0 = 0 \cdot a = 0$; se $|A| > 1$, allora $0 \neq 1$ e $0$ non è invertibile.
- Un **anello unitario** possiede l'elemento neutro $1$ per la moltiplicazione (es. $\mathbb{Z}$).
- Un **corpo** è un anello unitario in cui ogni $a \neq 0$ ha inverso moltiplicativo $a^{-1}$.
- Un **campo** è un corpo con moltiplicazione commutativa (es. $\mathbb{Q}, \mathbb{R}, \mathbb{C}$).

### 7. Esercizi

Le lezioni *(Lezione 1, pp. 7–8; Lezione 2, p. 1)* non assegnano esercizi per casa specifici su questo sottoparagrafo; per fissare i concetti, verifica direttamente con un calcolo numerico su $(\mathbb{Z},+,\cdot)$ tutte le proprietà della definizione di anello unitario e spiega perché non è un campo.

<!-- section: sec-1-5 | num: 1.5 | title: Il campo dei numeri complessi ℂ: costruzione su ℝ², forma algebrica, coniugato e modulo | kind: section | part: cap-1 -->

### 1. Idea in parole semplici

Nel campo dei numeri reali $\mathbb{R}$, nessun numero elevato al quadrato fa $-1$ (perché il quadrato di un numero reale è sempre $\ge 0$). Per risolvere equazioni come $x^2 + 1 = 0$, costruiamo un campo più grande, il campo dei **numeri complessi** $\mathbb{C}$.

Invece di inventare dal nulla un numero "misterioso", il metodo più rigoroso visto a lezione consiste nell'usare semplicemente le **coppie ordinate di numeri reali** $(a,b) \in \mathbb{R}^2$, cioè i punti del piano cartesiano, scegliendo una moltiplicazione "furba":

$$(a,b) \cdot (c,d) = (ac - bd,\ ad + bc)$$

Con questa regola, il punto $(0,1)$ sull'asse verticale — chiamato **unità immaginaria** $i$ — ha proprio quadrato $(0,1)\cdot(0,1) = (-1,0)$, che corrisponde al numero reale $-1$! Da lì, ogni punto $(a,b)$ si scrive nella familiare **forma algebrica** $a + bi$, mentre la geometria del piano ci regala subito il **coniugato** $\bar{z}$ (il simmetrico rispetto all'asse reale) e il **modulo** $|z|$ (la distanza dall'origine).

### 2. Definizioni e enunciati precisi

:::def Definizione — L'insieme $\mathbb{C} = \mathbb{R}^2$ e le sue operazioni (Lezione 2, p. 2)
Poniamo come insieme sostegno il prodotto cartesiano $\mathbb{C} \stackrel{\text{DEF}}{=} \mathbb{R} \times \mathbb{R} = \mathbb{R}^2$. Date due coppie $(a,b) \in \mathbb{R}^2$ e $(c,d) \in \mathbb{R}^2$, definiamo:
1. **Addizione:**
    $$(a,b) + (c,d) \stackrel{\text{DEF}}{=} (a+c,\ b+d)$$
2. **Moltiplicazione:**
    $$(a,b) \cdot (c,d) \stackrel{\text{DEF}}{=} (ac - bd,\ ad + bc)$$
:::

:::thm Proposizione — $(\mathbb{R}^2, +, \cdot)$ è un campo (Lezione 2, pp. 2–4)
La struttura algebrica $\mathbb{C} = (\mathbb{R}^2, +, \cdot)$ è un **campo**, detto **campo dei numeri complessi**, con:
- elemento neutro dell'addizione: $0 = (0,0)$, opposto di $(a,b)$: $-(a,b) = (-a,-b)$;
- elemento neutro della moltiplicazione (unità): $1 = (1,0)$;
- inverso moltiplicativo di ogni $(a,b) \neq (0,0)$:
    $$(a,b)^{-1} = \left(\frac{a}{a^2+b^2},\ \frac{-b}{a^2+b^2}\right)$$
:::

:::def Definizione — Unità immaginaria e forma algebrica (Lezione 2, pp. 4–5)
Poniamo:

$$i \stackrel{\text{DEF}}{=} (0,1) \in \mathbb{C}$$

Poiché $i^2 = (0,1)\cdot(0,1) = (-1,0) = -(1,0) = -1$ e identificando ogni coppia $(a,0)$ con il numero reale $a$ (sicché $\mathbb{R} \subset \mathbb{C}$), ogni numero complesso $z = (a,b)$ si esprime in modo unico nella **forma algebrica**:

$$(a,b) = (a,0) + (b,0)(0,1) = a + bi$$
:::

:::def Definizione — Parte reale, parte immaginaria, coniugato e modulo (Lezione 2, p. 5)
Sia $z = a + bi \in \mathbb{C}$ con $a, b \in \mathbb{R}$. Si definiscono:
- **Parte reale di $z$:** $\operatorname{Re} z \stackrel{\text{DEF}}{=} a \in \mathbb{R}$;
- **Parte immaginaria di $z$:** $\operatorname{Im} z \stackrel{\text{DEF}}{=} b \in \mathbb{R}$;
- **Coniugato di $z$:** $\bar{z} \stackrel{\text{DEF}}{=} a - bi$;
- **Modulo di $z$:** $|z| \stackrel{\text{DEF}}{=} \sqrt{a^2 + b^2} \in \mathbb{R}_0^+$ *(numero reale maggiore o uguale a $0$)*.
:::

<svg class="svg-diagram" viewBox="0 0 640 310" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Piano complesso con z = a + bi, modulo |z| e coniugato z̄ = a - bi">
  <rect x="0" y="0" width="640" height="310" rx="10" fill="#13161d"/>
  <!-- Assi -->
  <line x1="60" y1="155" x2="585" y2="155" stroke="#8d919e" stroke-width="1.6"/>
  <polygon points="585,155 575,150 575,160" fill="#8d919e"/>
  <line x1="210" y1="285" x2="210" y2="22" stroke="#8d919e" stroke-width="1.6"/>
  <polygon points="210,22 205,32 215,32" fill="#8d919e"/>
  <!-- Etichette assi -->
  <text x="530" y="176" fill="#9397a6" font-size="13" font-family="sans-serif">Asse reale x</text>
  <text x="220" y="34" fill="#9397a6" font-size="13" font-family="sans-serif">y (asse immaginario)</text>
  <!-- Punti base -->
  <circle cx="210" cy="155" r="4" fill="#e3e4eb"/>
  <text x="194" y="173" fill="#e3e4eb" font-size="13" font-family="monospace">0</text>
  <circle cx="285" cy="155" r="4" fill="#abc7ff"/>
  <text x="279" y="173" fill="#abc7ff" font-size="12" font-family="monospace">1=(1,0)</text>
  <circle cx="210" cy="105" r="4" fill="#abc7ff"/>
  <text x="148" y="110" fill="#abc7ff" font-size="12" font-family="monospace">i=(0,1)</text>
  <!-- Punto z = a + bi -->
  <line x1="210" y1="68" x2="430" y2="68" stroke="#64748b" stroke-width="1.2" stroke-dasharray="5,4"/>
  <line x1="430" y1="68" x2="430" y2="242" stroke="#64748b" stroke-width="1.2" stroke-dasharray="5,4"/>
  <!-- Vettore |z| -->
  <line x1="210" y1="155" x2="430" y2="68" stroke="#f0c987" stroke-width="2.4"/>
  <text x="315" y="99" fill="#f0c987" font-size="14" font-weight="bold" font-family="serif">|z| = √(a² + b²)</text>
  <!-- Punto z e proiezioni -->
  <circle cx="430" cy="68" r="5" fill="#7cc4fa"/>
  <text x="440" y="65" fill="#7cc4fa" font-size="14" font-weight="bold" font-family="sans-serif">z = a + bi</text>
  <circle cx="430" cy="155" r="3.5" fill="#e3e4eb"/>
  <text x="436" y="148" fill="#c2c5d0" font-size="13" font-family="sans-serif">Re z = a</text>
  <circle cx="210" cy="68" r="3.5" fill="#e3e4eb"/>
  <text x="122" y="72" fill="#c2c5d0" font-size="13" font-family="sans-serif">(0, Im z) = bi</text>
  <!-- Punto z coniugato -->
  <line x1="210" y1="242" x2="430" y2="242" stroke="#64748b" stroke-width="1.2" stroke-dasharray="5,4"/>
  <line x1="210" y1="155" x2="430" y2="242" stroke="#c7b3ff" stroke-width="1.6" stroke-dasharray="4,3"/>
  <circle cx="430" cy="242" r="5" fill="#c7b3ff"/>
  <text x="440" y="246" fill="#c7b3ff" font-size="14" font-weight="bold" font-family="sans-serif">z̄ = a - bi</text>
  <text x="124" y="246" fill="#9397a6" font-size="12" font-family="sans-serif">-bi</text>
</svg>

:::thm Proposizione — Somma, prodotto con il coniugato e formula rapida di $z^{-1}$ (Lezione 2, p. 6)
Sia $z = a + bi \in \mathbb{C}$. Valgono le tre proprietà:
1. $z + \bar{z} = 2a = 2\operatorname{Re} z$;
2. $z\bar{z} = a^2 + b^2 = |z|^2$;
3. se $z \neq 0$, allora $\frac{z\bar{z}}{|z|^2} = 1$, dunque l'inverso moltiplicativo si calcola con:
   $$z^{-1} = \frac{\bar{z}}{|z|^2}$$
:::

### 3. Dimostrazioni

:::proof Dimostrazione 1 — $(\mathbb{R}^2, +, \cdot)$ è un campo (Lezione 2, pp. 2–4)
**Idea di fondo:** verifichiamo esplicitamente gli assiomi di campo sulle coppie $(a,b)$: prima la struttura additiva, poi unità e commutatività del prodotto, infine il calcolo dell'inverso moltiplicativo risolvendo un sistema lineare $2 \times 2$.

- **Gruppo abeliano additivo:** l'addizione $(a,b) + (c,d) = (a+c, b+d)$ eredita da $(\mathbb{R},+)$ chiusura, associatività e commutatività; l'elemento neutro è $0 = (0,0)$ e l'opposto di $(a,b)$ è $-(a,b) = (-a,-b)$. Quindi $(\mathbb{R}^2,+)$ è un gruppo abeliano.
- **Unità moltiplicativa:** poniamo $1 = (1,0)$. Per ogni $(a,b) \in \mathbb{R}^2$ si ha:
  $$(a,b)\cdot(1,0) = (a\cdot 1 - b\cdot 0,\ a\cdot 0 + b\cdot 1) = (a,b)$$
  $$(1,0)\cdot(a,b) = (1\cdot a - 0\cdot b,\ 1\cdot b + 0\cdot a) = (a,b)$$
- **Commutatività del prodotto:** confrontiamo $(a,b)\cdot(c,d)$ e $(c,d)\cdot(a,b)$ usando la commutatività di $\mathbb{R}$:
  $$(a,b)\cdot(c,d) = (ac - bd,\ ad + bc)$$
  $$(c,d)\cdot(a,b) = (ca - db,\ da + cb) = (ac - bd,\ ad + bc)$$
- **Esistenza dell'inverso moltiplicativo:** sia $(a,b) \in \mathbb{R}^2$ con $(a,b) \neq (0,0)$ *(quindi $a^2 + b^2 \neq 0$)*. Cerchiamo $(x,y) \in \mathbb{R}^2$ tale che $(a,b)\cdot(x,y) = (1,0)$, ovvero $(ax - by,\ bx + ay) = (1,0)$, che equivale al sistema lineare:
    $$\begin{cases} ax - by = 1 \\ bx + ay = 0 \end{cases}$$
    Moltiplichiamo la prima equazione per $a$ e la seconda per $b$:
    $$\begin{cases} a^2 x - aby = a \\ b^2 x + aby = 0 \end{cases}$$
    Sommando le due equazioni i termini $\mp aby$ si semplificano:
    $$(a^2 + b^2)x = a \implies x = \frac{a}{a^2 + b^2}$$
    Sostituendo $x$ nella prima equazione otteniamo:
    $$a\frac{a}{a^2+b^2} - by = 1 \implies by = \frac{a^2}{a^2+b^2} - 1 = \frac{a^2 - a^2 - b^2}{a^2+b^2} = -\frac{b^2}{a^2+b^2} \implies y = -\frac{b}{a^2+b^2}$$
    Dunque per ogni $(a,b) \neq (0,0)$ esiste l'inverso $(a,b)^{-1} = \left(\frac{a}{a^2+b^2}, -\frac{b}{a^2+b^2}\right)$.
:::

:::note Nota sugli appunti originali (`Lez02`, p. 3)
1. Nell'ultimo passaggio dell'inverso ($by = -\frac{b^2}{a^2+b^2} \implies y = -\frac{b}{a^2+b^2}$) nei lucidi si divide implicitamente per $b$ (assumendo $b \neq 0$). Se invece $b = 0$, poiché $(a,b) \neq (0,0)$ deve essere $a \neq 0$: la seconda equazione $ay = 0$ dà subito $y = 0$, e la formula $\left(\frac{a}{a^2+b^2}, \frac{-b}{a^2+b^2}\right) = \left(\frac{1}{a}, 0\right)$ rimane validissima anche in questo caso.
2. `[INTEGRAZIONE NON DALLE LEZIONI]` Per completezza formale, negli appunti la verifica dell'associatività di $\cdot$ e della proprietà distributiva è lasciata sottintesa: entrambe seguono sviluppando algebricamente i prodotti su $\mathbb{R}$.
:::

:::proof Dimostrazione 2 — Somma e prodotto con il coniugato (Lezione 2, p. 6)
**Idea di fondo:** applichiamo direttamente le definizioni di $\bar{z}$, $i^2 = -1$ e $|z| = \sqrt{a^2+b^2}$.

Sia $z = a + bi$ con $a,b \in \mathbb{R}$, quindi $\bar{z} = a - bi$:
1. $z + \bar{z} = (a + bi) + (a - bi) = 2a = 2\operatorname{Re} z$.
2. $z\bar{z} = (a + bi)(a - bi) = a^2 - abi + abi - b^2 i^2 = a^2 - b^2(-1) = a^2 + b^2 = |z|^2$.
3. Se $z \neq 0$, allora $|z|^2 = a^2 + b^2 > 0$; dividendo per $|z|^2$ nell'identità (2) otteniamo $z \cdot \frac{\bar{z}}{|z|^2} = 1$, cioè $z^{-1} = \frac{\bar{z}}{|z|^2}$.
:::

### 4. Esempi svolti

:::example Esempio 1.5.1 — Addizione e moltiplicazione di coppie in $\mathbb{C}$ (Lezione 2, p. 2)
Presi $z_1 = (2,1)$ e $z_2 = (3,7)$:
- $(2,1) + (3,7) = (2+3,\ 1+7) = (5,8)$;
- $(2,1) \cdot (3,7) = (2\cdot 3 - 1\cdot 7,\ 2\cdot 7 + 1\cdot 3) = (6 - 7,\ 14 + 3) = (-1, 17)$.
:::

:::example Esempio 1.5.2 — Calcolo dell'inverso in forma di coppia e in forma algebrica (Lezione 2, pp. 4, 6)
1. **Con le coppie *(Lezione 2, p. 4)*:** calcoliamo $(2,3)^{-1}$. Qui $a = 2, b = 3$, quindi $a^2 + b^2 = 2^2 + 3^2 = 13$:
    $$(2,3)^{-1} = \left(\frac{2}{2^2 + 3^2},\ \frac{-3}{2^2 + 3^2}\right) = \left(\frac{2}{13},\ -\frac{3}{13}\right)$$
2. **In forma algebrica *(Lezione 2, p. 6)*:** calcoliamo $(2+3i)^{-1}$. Abbiamo $z = 2 + 3i$, $\bar{z} = 2 - 3i$ e $|z|^2 = 2^2 + 3^2 = 13$, perciò:
    $$z^{-1} = \frac{\bar{z}}{|z|^2} = \frac{2 - 3i}{13} = \frac{2}{13} - \frac{3}{13}i$$
    I due metodi danno ovviamente lo stesso numero complesso!
:::

### 5. Errori comuni e trappole

1. **Includere la $i$ dentro $\operatorname{Im} z$**
    - *Sbagliato:* per $z = 2 + 3i$, scrivere $\operatorname{Im} z = 3i$.
    - *Correzione:* la definizione precisa *(Lezione 2, p. 5)* stabilisce che **$\operatorname{Im} z \in \mathbb{R}$**. Quindi per $z = 2 + 3i$ si ha $\operatorname{Im} z = 3$ (il coefficiente reale davanti a $i$, non $3i$!).
2. **Mettere la $i$ dentro la formula del modulo $|z|$**
    - *Sbagliato:* scrivere $|a + bi| = \sqrt{a^2 + (bi)^2} = \sqrt{a^2 - b^2}$.
    - *Correzione:* $|z| = \sqrt{a^2 + b^2} \in \mathbb{R}_0^+$ *(Lezione 2, p. 5)*, applicando il teorema di Pitagora ai cateti reali $a$ e $b$. Con il segno $-$ si potrebbero avere radici di numeri negativi!
3. **Fare il prodotto componente per componente come nell'addizione**
    - *Sbagliato:* calcolare $(a,b)\cdot(c,d) = (ac, bd)$.
    - *Correzione:* la regola è $(ac - bd,\ ad + bc)$, perché in forma algebrica $(a+bi)(c+di) = ac + adi + bci + bdi^2 = (ac-bd) + (ad+bc)i$.

### 6. Riepilogo

- $\mathbb{C} = \mathbb{R}^2$ con somma componente per componente e prodotto $(a,b)\cdot(c,d) = (ac-bd, ad+bc)$ è un **campo**.
- L'unità immaginaria è $i = (0,1)$, con $i^2 = -1$; ogni numero si scrive in forma algebrica $z = a + bi$ ($\mathbb{R} \subset \mathbb{C}$).
- Per $z = a + bi$: $\operatorname{Re} z = a \in \mathbb{R}$, $\operatorname{Im} z = b \in \mathbb{R}$, $\bar{z} = a - bi$, $|z| = \sqrt{a^2+b^2} \in \mathbb{R}_0^+$.
- Identità fondamentali con il coniugato: $z + \bar{z} = 2\operatorname{Re} z$ e $z\bar{z} = |z|^2$.
- Formula rapida per l'inverso di $z \neq 0$: $z^{-1} = \frac{\bar{z}}{|z|^2}$.

### 7. Esercizi

:::exercise Esercizio 1.5.1 (Esercizio per casa — Facile · Lezione 2, p. 6)
Sia $z = 1 + 5i \in \mathbb{C}$. Calcolare $z^{-1}$.

:::solution Soluzione spiegata passo-passo
**Ragionamento:** usiamo la formula rapida $z^{-1} = \frac{\bar{z}}{|z|^2}$ appena dimostrata.

1. Individuiamo parte reale e immaginaria: $a = 1$, $b = 5$.
2. Scriviamo il coniugato: $\bar{z} = 1 - 5i$.
3. Calcoliamo il quadrato del modulo: $|z|^2 = 1^2 + 5^2 = 1 + 25 = 26$.
4. Dividiamo $\bar{z}$ per $|z|^2$:
    $$z^{-1} = \frac{1 - 5i}{26} = \frac{1}{26} - \frac{5}{26}i$$
5. *Verifica rapida:* $(1+5i)\left(\frac{1}{26} - \frac{5}{26}i\right) = \frac{1 - 25i^2}{26} = \frac{1+25}{26} = 1$.
:::
:::

:::exercise Esercizio 1.5.2 (Esercizio per casa — Medio · Lezione 2, p. 6)
Sia $z = 1 + i \in \mathbb{C}$. Calcolare $z^4$.

:::solution Soluzione spiegata passo-passo
**Ragionamento:** invece di espandere la quarta potenza con il binomio di Newton, conviene calcolare prima $z^2$ e poi sfruttare $z^4 = (z^2)^2$.

1. Calcoliamo $z^2$:
    $$z^2 = (1 + i)^2 = 1 + 2i + i^2 = 1 + 2i - 1 = 2i$$
    *(Osservazione: il termine reale $1$ e $i^2 = -1$ si elidono, lasciando un numero immaginario puro!)*
2. Eleviamo ancora al quadrato:
    $$z^4 = (z^2)^2 = (2i)^2 = 4i^2 = 4(-1) = -4$$

Quindi $(1+i)^4 = -4$.
:::
:::

<!-- section: sec-1-6 | num: 1.6 | title: Equazioni di secondo grado, Teorema Fondamentale dell'Algebra e fattorizzazione di polinomi | kind: section | part: cap-1 -->

### 1. Idea in parole semplici

In $\mathbb{R}$, un'equazione di secondo grado con discriminante negativo ($\Delta < 0$, come $x^2 + 1 = 0$ o $x^2 - 4x + 13 = 0$) non ha soluzioni, e il corrispondente polinomio non si può spezzare in fattori più piccoli.

Nel campo complesso $\mathbb{C}$ tutto si sblocca: ogni numero negativo ha radici quadrate immaginarie (per esempio $-9 = (3i)^2$), quindi **ogni equazione di II grado ha soluzioni in $\mathbb{C}$**. Anzi, se i coefficienti sono reali e le radici non sono reali, arrivano sempre **a coppie coniugate** $z$ e $\bar{z}$. Il **Teorema Fondamentale dell'Algebra** estende questa proprietà a polinomi di qualsiasi grado: in $\mathbb{C}$ ogni polinomio non costante si fattorizza interamente in fattori di primo grado.

### 2. Definizioni e enunciati precisi

:::thm Proprietà — Relazione radici-coefficienti per il II grado (Lezione 2, pp. 6–7)
Sviluppando il prodotto $(x - \alpha)(x - \beta) = x^2 - (\alpha + \beta)x + \alpha\beta$, se $x^2 + bx + c = 0$ è un'equazione di II grado monica *(coefficiente $1$ davanti a $x^2$)*:
- $c = \alpha\beta$ è il **prodotto delle radici**;
- $b = -(\alpha + \beta)$ è l'**opposto della somma delle radici**.

In particolare, per ogni $z = a + bi \in \mathbb{C}$, i numeri $z$ e $\bar{z}$ sono le due soluzioni dell'equazione a coefficienti reali:

$$x^2 - 2(\operatorname{Re} z)x + |z|^2 = 0$$
:::

:::thm Teorema Fondamentale dell'Algebra (Lezione 2, p. 7)
Sia $P(x) = 0$ un'equazione algebrica a coefficienti reali *(con $\deg P \ge 1$)*. Allora:
1. $P(x) = 0$ ha sempre almeno una soluzione nel campo complesso $\mathbb{C}$;
2. in particolare, $P(x)$ si può sempre scomporre nel **prodotto di fattori lineari** (cioè di primo grado) in $\mathbb{C}$.
:::

:::note Nota sugli appunti originali (`Lez02`, p. 7)
1. Negli appunti il Teorema Fondamentale dell'Algebra è enunciato per $P(x)=0$ a coefficienti reali senza scrivere esplicitamente $\deg P \ge 1$: naturalmente il polinomio deve avere grado almeno $1$ (un polinomio costante non nullo come $P(x)=5$ non ha radici).
2. `[INTEGRAZIONE NON DALLE LEZIONI]` Il Teorema Fondamentale dell'Algebra vale più in generale per qualsiasi polinomio di grado $\ge 1$ anche a **coefficienti complessi**, e a lezione viene dato senza dimostrazione.
:::

### 3. Dimostrazioni

:::proof Verifica — Equazione quadratica con radici coniugate $z$ e $\bar{z}$ (Lezione 2, pp. 6–7)
**Idea di fondo:** sostituiamo $\alpha = z$ e $\beta = \bar{z}$ nella relazione radici-coefficienti $(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \alpha\beta$ usando le identità già provate nella Sezione 1.5.

Dalla Proposizione della Sezione 1.5 sappiamo che per $z = a + bi \in \mathbb{C}$:
- somma delle radici: $z + \bar{z} = 2\operatorname{Re} z$;
- prodotto delle radici: $z\bar{z} = |z|^2$.

Pertanto il polinomio monico che si annulla in $z$ e $\bar{z}$ è:

$$(x - z)(x - \bar{z}) = x^2 - (z + \bar{z})x + z\bar{z} = x^2 - 2(\operatorname{Re} z)x + |z|^2$$

Entrambi i coefficienti $-2\operatorname{Re} z$ e $|z|^2$ sono reali, quindi $z$ e $\bar{z}$ sono soluzioni dell'equazione reale $x^2 - 2(\operatorname{Re} z)x + |z|^2 = 0$.
:::

### 4. Esempi svolti

:::example Esempio 1.6.1 — Costruire l'equazione di II grado date le radici reali (Lezione 2, p. 7)
Troviamo l'equazione di II grado che ha come soluzioni $\alpha = 2$ e $\beta = 3$:
- $\alpha + \beta = 2 + 3 = 5$;
- $\alpha\beta = 2 \cdot 3 = 6$.

L'equazione è $x^2 - 5x + 6 = 0$. Verifichiamolo con la formula risolutiva: $\Delta = (-5)^2 - 4(1)(6) = 25 - 24 = 1$, da cui $x = \frac{5 \pm 1}{2}$, ossia $x = 2$ e $x = 3$.
:::

:::example Esempio 1.6.2 — Equazione di II grado con radici complesse coniugate (Lezione 2, p. 7)
Prendiamo $z = 2 + 3i$, quindi $\bar{z} = 2 - 3i$:
- $z + \bar{z} = 2\operatorname{Re} z = 4$;
- $z\bar{z} = |z|^2 = 2^2 + 3^2 = 13$.

Dunque $2 + 3i$ e $2 - 3i$ sono le soluzioni di $x^2 - 4x + 13 = 0$. Verifichiamo risolvendola con la formula ridotta:

$$\frac{\Delta}{4} = (-2)^2 - 13 = 4 - 13 = -9 = (3i)^2 \implies x = 2 \pm 3i$$

Le soluzioni sono esattamente $2 + 3i$ e $2 - 3i$.
:::

:::example Esempio 1.6.3 — Fattorizzazione completa di $P(x) = x^4 + 1$ in $\mathbb{C}$ (Lezione 2, p. 8)
Vogliamo scomporre $P(x) = x^4 + 1$ in fattori lineari complessi. In $\mathbb{R}$ sembra irriducibile, ma possiamo aggiungere e togliere il doppio prodotto $2x^2$ per completare un quadrato:

$$x^4 + 1 = x^4 + 2x^2 + 1 - 2x^2 = (x^2 + 1)^2 - (\sqrt{2}x)^2$$

Usando la differenza di quadrati $A^2 - B^2 = (A + B)(A - B)$ otteniamo due fattori reali di II grado (entrambi con $\Delta < 0$):

$$x^4 + 1 = (x^2 + \sqrt{2}x + 1)(x^2 - \sqrt{2}x + 1)$$

Ora risolviamo in $\mathbb{C}$ ciascuno dei due fattori:

1. $x^2 + \sqrt{2}x + 1 = 0$: $\Delta = 2 - 4 = -2 = (\sqrt{2}i)^2$, quindi
    $$x = \frac{-\sqrt{2} \pm \sqrt{2}i}{2} \implies \beta = -\frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2}i, \quad \bar{\beta} = -\frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2}i$$
2. $x^2 - \sqrt{2}x + 1 = 0$: $\Delta = 2 - 4 = -2 = (\sqrt{2}i)^2$, quindi
    $$x = \frac{\sqrt{2} \pm \sqrt{2}i}{2} \implies \alpha = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2}i, \quad \bar{\alpha} = \frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2}i$$

La fattorizzazione in fattori lineari complessi è dunque:

$$x^4 + 1 = (x - \alpha)(x - \bar{\alpha})(x - \beta)(x - \bar{\beta})$$
:::

### 5. Errori comuni e trappole

1. **Sbagliare il segno nella somma delle radici**
    - *Sbagliato:* se le radici di $x^2 + bx + c = 0$ sono $\alpha$ e $\beta$, scrivere $b = \alpha + \beta$.
    - *Correzione:* ricordando $(x-\alpha)(x-\beta) = x^2 - (\alpha+\beta)x + \alpha\beta$, il coefficiente $b$ è l'**opposto** della somma: $b = -(\alpha + \beta)$.
2. **Arrendersi davanti a $\Delta < 0$ o a $x^4 + 1$**
    - *Sbagliato:* fermarsi dicendo "$\Delta = -9$, quindi non ci sono soluzioni" oppure lasciare $x^4 + 1$ non scomposto.
    - *Correzione:* su $\mathbb{C}$, $-d = (\sqrt{d}\,i)^2$ per ogni $d > 0$: ogni polinomio a coefficienti reali di grado $\ge 1$ si scompone interamente in fattori di grado $1$ in $\mathbb{C}$ (e in fattori di grado $1$ o $2$ in $\mathbb{R}$).

### 6. Riepilogo

- In $x^2 + bx + c = 0$ vale sempre $b = -(\alpha+\beta)$ e $c = \alpha\beta$.
- Un numero complesso $z$ e il suo coniugato $\bar{z}$ risolvono l'equazione reale $x^2 - 2(\operatorname{Re} z)x + |z|^2 = 0$.
- Per il **Teorema Fondamentale dell'Algebra**, ogni equazione $P(x)=0$ ($\deg P \ge 1$) a coefficienti reali ha almeno una soluzione in $\mathbb{C}$.
- Di conseguenza ogni polinomio $P(x)$ si fattorizza completamente in fattori lineari su $\mathbb{C}$.
- Per fattorizzare polinomi reali di grado $3$ o $4$, si cercano prima eventuali fattori reali (es. raccoglimenti, prodotti notevoli, Ruffini) e poi si risolvono i fattori quadratici con $\Delta < 0$ in $\mathbb{C}$.

### 7. Esercizi

:::exercise Esercizio 1.6.1 (Esercizio per casa — Medio · Lezione 2, p. 8)
Fattorizzare il polinomio $P(x) = x^3 - 1$ nel prodotto di fattori lineari su $\mathbb{C}$.

:::solution Soluzione spiegata passo-passo
**Ragionamento:** individuiamo prima la radice reale evidente $x = 1$ scomponendo la differenza di cubi, poi troviamo le due radici complesse coniugate del fattore quadratico residuo.

1. Scomponiamo la differenza di cubi $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$ con $a = x$ e $b = 1$:
    $$x^3 - 1 = (x - 1)(x^2 + x + 1)$$
2. Il primo fattore $(x - 1)$ è già lineare. Risolviamo in $\mathbb{C}$ l'equazione $x^2 + x + 1 = 0$:
    $$\Delta = 1^2 - 4(1)(1) = 1 - 4 = -3 = (\sqrt{3}\,i)^2$$
    $$x = \frac{-1 \pm \sqrt{3}\,i}{2}$$
3. Ponendo $\alpha = -\frac{1}{2} + \frac{\sqrt{3}}{2}i$ e $\bar{\alpha} = -\frac{1}{2} - \frac{\sqrt{3}}{2}i$, il fattore quadratico diventa $(x - \alpha)(x - \bar{\alpha})$.
4. Unendo tutti i fattori otteniamo la scomposizione lineare completa in $\mathbb{C}$:
    $$x^3 - 1 = (x - 1)(x - \alpha)(x - \bar{\alpha}) = (x - 1)\left(x + \frac{1}{2} - \frac{\sqrt{3}}{2}i\right)\left(x + \frac{1}{2} + \frac{\sqrt{3}}{2}i\right)$$
:::
:::
