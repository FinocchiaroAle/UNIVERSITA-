<!-- part: cap-6 | num: 6 | label: CAPITOLO 6 | title: Applicazioni lineari, isomorfismi e cambi di base | refs: Fonti: Lezione 10 (9/11/2026, pp. 3–11), Lezione 11 (16/11/2026, pp. 1–10) e Lezione 12 (18/11/2026, pp. 1–2) -->

<!-- section: sec-6-1 | num: 6.1 | title: Applicazioni lineari, immagine e controimmagine di sottospazi | kind: section | part: cap-6 -->

### 1. Idea in parole semplici

Nel Capitolo 5 abbiamo costruito gli spazi vettoriali e i loro sottospazi. Ora vogliamo collegarli tra loro mediante funzioni speciali che **rispettino la struttura lineare**, cioè che non spezzino somme e moltiplicazioni per scalari: sono le **applicazioni lineari**.

Dire che una funzione $f : U \to V$ è lineare significa che *combinare prima e trasformare dopo* ($f(a_1 u_1 + a_2 u_2)$) produce esattamente lo stesso risultato di *trasformare prima e combinare dopo* ($a_1 f(u_1) + a_2 f(u_2)$). Grazie a questa proprietà, le applicazioni lineari mandano sempre l'origine di $U$ nell'origine di $V$ e trasformano sottospazi in sottospazi, sia in avanti ($f(W)$) che all'indietro ($f^{-1}(Z)$).

### 2. Definizioni e enunciati precisi

:::def Definizione — Applicazione lineare (Lezione 10, p. 3)
Siano $U$ e $V$ due $K$-spazi vettoriali e sia $f : U \to V$ una funzione. Diremo che $f$ è un'**applicazione lineare** se:

$$f(a_1 u_1 + a_2 u_2) = a_1 f(u_1) + a_2 f(u_2) \qquad \forall a_1, a_2 \in K,\ \forall u_1, u_2 \in U$$
:::

:::thm Proposizione — Immagine del vettore nullo (Lezione 10, p. 3)
Sia $f : U \to V$ un'applicazione lineare. Allora $f$ manda il vettore nullo di $U$ nel vettore nullo di $V$:

$$f(\underline{0}_U) = \underline{0}_V$$
:::

:::thm Proposizione — Immagine e controimmagine di sottospazi (Lezione 10, p. 4)
Sia $f : U \to V$ un'applicazione lineare.
1. Se $W \subseteq U$ è un sottospazio di $U$, allora l'**immagine di $W$**:
    $$f(W) \stackrel{\text{DEF}}{=} \{f(w) \mid w \in W\}$$
    è un **sottospazio di $V$**.
2. Se $Z \subseteq V$ è un sottospazio di $V$, allora la **controimmagine di $Z$**:
    $$f^{-1}(Z) \stackrel{\text{DEF}}{=} \{u \in U \mid f(u) \in Z\}$$
    è un **sottospazio di $U$**.
:::

### 3. Dimostrazioni

:::proof Dimostrazione 1 — $f(\underline{0}_U) = \underline{0}_V$ (Lezione 10, p. 3)
**Idea di fondo:** sfruttiamo $\underline{0}_U = \underline{0}_U + \underline{0}_U$ e la linearità per poi cancellare $f(\underline{0}_U)$ da entrambi i membri nel gruppo $(V, +)$.

Applicando la definizione di applicazione lineare con $a_1 = a_2 = 1$ e $u_1 = u_2 = \underline{0}_U$:

$$f(\underline{0}_U) = f(\underline{0}_U + \underline{0}_U) = f(\underline{0}_U) + f(\underline{0}_U)$$

Cancellando $f(\underline{0}_U)$ da entrambi i membri nell'uguaglianza $f(\underline{0}_U) = f(\underline{0}_U) + f(\underline{0}_U)$ si ottiene $\underline{0}_V = f(\underline{0}_U)$.
:::

:::proof Dimostrazione 2 — $f(W)$ è un sottospazio di $V$ (Lezione 10, p. 4)
**Idea di fondo:** verifichiamo i due requisiti del criterio di sottospazio su $f(W) \subseteq V$: la presenza di $\underline{0}_V$ segue dalla Proposizione precedente, mentre la chiusura rispetto alle combinazioni lineari usa direttamente la linearità di $f$ e la chiusura di $W$.

- **(1A) $\underline{0}_V \in f(W)$:** poiché $W$ è un sottospazio di $U$, si ha $\underline{0}_U \in W$, quindi $f(\underline{0}_U) \in f(W)$. Per la Dimostrazione 1, $f(\underline{0}_U) = \underline{0}_V$, dunque $\underline{0}_V \in f(W)$.
- **(1B) Chiusura rispetto alle combinazioni lineari:** siano $v_1, v_2 \in f(W)$ e $a_1, a_2 \in K$. Per definizione di $f(W)$ esistono $w_1, w_2 \in W$ tali che $v_1 = f(w_1)$ e $v_2 = f(w_2)$. Allora:
    $$a_1 v_1 + a_2 v_2 = a_1 f(w_1) + a_2 f(w_2) = f(\underbrace{a_1 w_1 + a_2 w_2}_{\in W}) \in f(W)$$
    *(poiché $W$ è sottospazio di $U$, la combinazione $a_1 w_1 + a_2 w_2$ appartiene a $W$).*

Dunque $f(W)$ è un sottospazio di $V$.
:::

:::proof Dimostrazione 3 — $f^{-1}(Z)$ è un sottospazio di $U$ (Lezione 10, pp. 4–5)
**Idea di fondo:** appartenere a $f^{-1}(Z)$ significa che l'*immagine* cade in $Z$. Quindi controlliamo che $f(\underline{0}_U)$ cada in $Z$ e che $f(a_1 u_1 + a_2 u_2)$ cada in $Z$.

- **(2A) $\underline{0}_U \in f^{-1}(Z)$:** dobbiamo verificare se $f(\underline{0}_U) \in Z$. Poiché $f(\underline{0}_U) = \underline{0}_V$ e $Z$ è sottospazio di $V$, si ha $\underline{0}_V \in Z$, quindi $\underline{0}_U \in f^{-1}(Z)$.
- **(2B) Chiusura rispetto alle combinazioni lineari:** siano $u_1, u_2 \in f^{-1}(Z)$ *(quindi $f(u_1) \in Z$ e $f(u_2) \in Z$)* e siano $a_1, a_2 \in K$. Calcoliamo l'immagine della combinazione lineare $a_1 u_1 + a_2 u_2$:
    $$f(a_1 u_1 + a_2 u_2) = a_1 \underbrace{f(u_1)}_{\in Z} + a_2 \underbrace{f(u_2)}_{\in Z} \in Z$$
    poiché $Z$ è sottospazio di $V$ e quindi è chiuso rispetto alle combinazioni lineari. Ne segue $a_1 u_1 + a_2 u_2 \in f^{-1}(Z)$.

Pertanto $f^{-1}(Z)$ è un sottospazio di $U$.
:::

### 4. Esempi svolti

In questa introduzione teorica della Lezione 10 *(pp. 3–5)* gli esempi concreti vengono subito sviluppati subito dopo la definizione di $\operatorname{Ker} f$ e $\operatorname{Im} f$ tramite le applicazioni matriciali $f_M(X) = MX$ nella Sezione [6.3](#sec-6-3). Un controesempio immediato di non linearità discende già dalla prima proposizione: se $f : \mathbb{R}^2 \to \mathbb{R}^2$ manda $(0,0)$ in $(1,0) \neq (0,0)$, allora $f$ non può essere lineare.

### 5. Errori comuni e trappole

1. **Pensare che $f^{-1}(Z)$ esista solo quando la funzione $f$ è invertibile**
    - *Sbagliato:* dire "non esiste $f^{-1}(\{(2,1,3)\})$ perché $\det M = 0$ e $f$ non è biettiva".
    - *Correzione:* la **controimmagine** $f^{-1}(Z) = \{u \in U \mid f(u) \in Z\}$ è un sottoinsieme del dominio $U$ definito per **qualsiasi** funzione, anche non iniettiva e non suriettiva (può avere un solo elemento, infiniti elementi oppure essere l'insieme vuoto $\emptyset$, come vedremo nella Sezione [6.3](#sec-6-3)).
2. **Dimenticare che solo la controimmagine di un sottospazio (come $\{\underline{0}_V\}$) è sottospazio, non quella di un singolo vettore non nullo**
    - *Sbagliato:* affermare che $f^{-1}(\{(1,2)\})$ è un sottospazio vettoriale.
    - *Correzione:* nella Proposizione, $Z$ deve essere un **sottospazio** di $V$: per $Z = \{\underline{0}_V\}$ la controimmagine è $\operatorname{Ker} f$ (sottospazio), mentre per $Z = \{v\}$ con $v \neq \underline{0}_V$ non contiene $\underline{0}_U$ (poiché $f(\underline{0}_U) = \underline{0}_V \neq v$).

### 6. Riepilogo

- $f : U \to V$ è **lineare** se $f(a_1 u_1 + a_2 u_2) = a_1 f(u_1) + a_2 f(u_2)$ per ogni $a_1, a_2 \in K$ e $u_1, u_2 \in U$.
- Ogni applicazione lineare soddisfa $f(\underline{0}_U) = \underline{0}_V$.
- L'immagine $f(W)$ di un sottospazio $W \subseteq U$ è un sottospazio di $V$.
- La controimmagine $f^{-1}(Z)$ di un sottospazio $Z \subseteq V$ è un sottospazio di $U$.

### 7. Esercizi

La Lezione 10 *(pp. 3–5)* non contiene esercizi per casa specifici su queste proprietà generali; gli esercizi operativi su nucleo, immagine e controimmagini iniziano dalla Sezione [6.3](#sec-6-3).

<!-- section: sec-6-2 | num: 6.2 | title: Nucleo, immagine, iniettività, suriettività e Teorema sulle dimensioni | kind: section | part: cap-6 -->

### 1. Idea in parole semplici

Dalla sezione precedente abbiamo visto che immagine di un sottospazio e controimmagine di un sottospazio sono ancora sottospazi. Scegliendo i due casi estremi possibili — tutto il dominio $W = U$ in partenza, e il solo vettore nullo $Z = \{\underline{0}_V\}$ in arrivo — otteniamo i due protagonisti assoluti di ogni applicazione lineare:
- l'**immagine** $\operatorname{Im} f = f(U) \subseteq V$: l'insieme di tutto ciò che $f$ riesce a "raggiungere" nel codominio; se $\operatorname{Im} f = V$, $f$ è **suriettiva**;
- il **nucleo** $\operatorname{Ker} f = f^{-1}(\{\underline{0}_V\}) \subseteq U$: l'insieme di tutti i vettori di partenza che $f$ "schiaccia" sullo zero; scoprire quanto è grande $\operatorname{Ker} f$ dice subito se $f$ è **iniettiva** (lo è se e solo se in $\operatorname{Ker} f$ c'è solo $\underline{0}_U$).

Il **Teorema sulle dimensioni** stabilisce un bilancio perfetto tra i due: la dimensione di partenza $\dim U$ si divide esattamente tra ciò che viene schiacciato ($\dim \operatorname{Ker} f$) e ciò che sopravvive in arrivo ($\dim \operatorname{Im} f$).

### 2. Definizioni e enunciati precisi

:::def Definizione — Immagine ($\operatorname{Im} f$), suriettività e nucleo ($\operatorname{Ker} f$) (Lezione 10, p. 5)
Sia $f : U \to V$ un'applicazione lineare.
1. Scegliendo $W = U$, il sottospazio $f(U) \subseteq V$ si chiama **immagine** della funzione e si indica con **$\operatorname{Im} f$**. Ricordiamo che $f$ si dice **suriettiva** se $\operatorname{Im} f = V$.
2. Scegliendo $Z = \{\underline{0}_V\}$, il sottospazio $f^{-1}(\{\underline{0}_V\}) \subseteq U$ si chiama **nucleo** dell'applicazione lineare e si indica con **$\operatorname{Ker} f$**:
    $$\operatorname{Ker} f \stackrel{\text{DEF}}{=} \{u \in U \mid f(u) = \underline{0}_V\}$$
:::

<svg class="svg-diagram" viewBox="0 0 660 225" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Schema grafico di nucleo Ker f e immagine Im f per f: U -> V">
  <rect x="0" y="0" width="660" height="225" rx="10" fill="#13161d"/>
  <!-- Dominio U -->
  <ellipse cx="155" cy="115" rx="115" ry="82" fill="#182032" stroke="#7cc4fa" stroke-width="2"/>
  <text x="58" y="34" fill="#7cc4fa" font-size="14" font-weight="bold" font-family="sans-serif">Dominio U</text>
  <!-- Ker f -->
  <ellipse cx="155" cy="128" rx="64" ry="42" fill="#2a1d3d" stroke="#c7b3ff" stroke-width="1.8"/>
  <circle cx="155" cy="128" r="4" fill="#e3e4eb"/>
  <text x="163" y="132" fill="#e3e4eb" font-size="12" font-family="sans-serif">0_U</text>
  <text x="155" y="108" text-anchor="middle" fill="#c7b3ff" font-size="13" font-weight="bold" font-family="sans-serif">Ker f</text>

  <!-- Codominio V -->
  <ellipse cx="505" cy="115" rx="115" ry="82" fill="#182032" stroke="#8ad8b0" stroke-width="2"/>
  <text x="572" y="34" fill="#8ad8b0" font-size="14" font-weight="bold" font-family="sans-serif">Codominio V</text>
  <!-- Im f -->
  <ellipse cx="505" cy="120" rx="76" ry="50" fill="#152b23" stroke="#8ad8b0" stroke-width="1.8" stroke-dasharray="5,3"/>
  <text x="505" y="92" text-anchor="middle" fill="#8ad8b0" font-size="13" font-weight="bold" font-family="sans-serif">Im f = f(U)</text>
  <circle cx="505" cy="135" r="4.5" fill="#f0c987"/>
  <text x="515" y="139" fill="#f0c987" font-size="12.5" font-weight="bold" font-family="sans-serif">0_V</text>

  <!-- Frecce -->
  <path d="M 275 88 Q 330 68 385 88" fill="none" stroke="#abc7ff" stroke-width="2.2"/>
  <polygon points="385,88 375,81 378,91" fill="#abc7ff"/>
  <text x="330" y="65" text-anchor="middle" fill="#abc7ff" font-size="13" font-weight="bold" font-family="sans-serif">f : U → V</text>

  <path d="M 218 132 Q 355 170 498 138" fill="none" stroke="#c7b3ff" stroke-width="1.6" stroke-dasharray="4,3"/>
  <polygon points="498,138 488,136 492,145" fill="#c7b3ff"/>
  <text x="332" y="172" text-anchor="middle" fill="#c7b3ff" font-size="11.5" font-family="sans-serif">tutto Ker f collassa in 0_V</text>
  <text x="330" y="208" text-anchor="middle" fill="#9397a6" font-size="11" font-family="sans-serif">dim U = dim Ker f + dim Im f   |   f iniettiva ⇔ Ker f = {0_U}</text>
</svg>

:::thm Proposizione — Caratterizzazione dell'iniettività tramite il nucleo (Lezione 10, p. 5)
Un'applicazione lineare $f : U \to V$ è **iniettiva** se e solo se:

$$\operatorname{Ker} f = \{\underline{0}_U\}$$
:::

:::thm Teorema sulle dimensioni (Lezione 10, p. 6; Lezione 11, p. 1)
Sia $f : U \to V$ un'applicazione lineare *(con $U$ spazio vettoriale finitamente generato)*. Allora:

$$\dim_K U = \dim_K \operatorname{Ker} f + \dim_K \operatorname{Im} f$$
:::

:::thm Corollario — Confronto tra dimensioni di $U$ e $V$ (Lezione 11, p. 2)
Sia $f : U \to V$ un'applicazione lineare *(tra spazi finitamente generati)*:
1. se $f$ è **iniettiva**, allora $\dim_K U \le \dim_K V$;
2. se $f$ è **suriettiva**, allora $\dim_K U \ge \dim_K V$;
3. se $f$ è un **isomorfismo** *(cioè biettiva)*, allora $\dim_K U = \dim_K V$.
:::

:::note Nota sugli appunti originali (`Lez10`, p. 6 e `Lez11`, p. 1–2)
Negli appunti il *Teorema sulle dimensioni* e il suo *Corollario* scrivono direttamente $\dim_K U, \dim_K V$ dando per sottinteso che gli spazi considerati siano **finitamente generati** (altrimenti le dimensioni non sarebbero numeri finiti). Qui abbiamo esplicitato l'ipotesi per piena precisione formale.
:::

### 3. Dimostrazioni

:::proof Dimostrazione 1 — $f$ è iniettiva $\iff \operatorname{Ker} f = \{\underline{0}_U\}$ (Lezione 10, p. 5)
**Idea di fondo:** la linearità trasforma ogni coppia di punti distinti o uguali $(u_1, u_2)$ con $f(u_1)=f(u_2)$ nella differenza $u_1 - u_2 \in \operatorname{Ker} f$! Così basta controllare che nessun vettore $\neq \underline{0}_U$ vada in $\underline{0}_V$.

- **($\Rightarrow$) Supponiamo che $f$ sia iniettiva:**
    Prendiamo un qualunque $u \in \operatorname{Ker} f$: per definizione $f(u) = \underline{0}_V$. D'altra parte sappiamo già che $f(\underline{0}_U) = \underline{0}_V$. Avendo $f(u) = f(\underline{0}_U)$ ed essendo $f$ iniettiva, deve essere $u = \underline{0}_U$. Quindi $\operatorname{Ker} f = \{\underline{0}_U\}$.
- **($\Leftarrow$) Supponiamo che $\operatorname{Ker} f = \{\underline{0}_U\}$:**
    Siano $u_1, u_2 \in U$ tali che $f(u_1) = f(u_2)$. Allora $f(u_1) - f(u_2) = \underline{0}_V$, e per la linearità di $f$ si ha $f(u_1 - u_2) = \underline{0}_V$. Ciò significa che $u_1 - u_2 \in \operatorname{Ker} f = \{\underline{0}_U\}$, dunque $u_1 - u_2 = \underline{0}_U \implies u_1 = u_2$. Pertanto $f$ è iniettiva.
:::

:::proof Dimostrazione 2 — Corollario sulle dimensioni (Lezione 11, p. 2)
**Idea di fondo:** sostituiamo nell'equazione $\dim_K U = \dim_K \operatorname{Ker} f + \dim_K \operatorname{Im} f$ le informazioni su $\operatorname{Ker} f$ (quando è iniettiva) e su $\operatorname{Im} f$ (quando è suriettiva), ricordando che $\operatorname{Im} f \subseteq V \implies \dim_K \operatorname{Im} f \le \dim_K V$.

Dalla formula $\dim_K U = \dim_K \operatorname{Ker} f + \dim_K \operatorname{Im} f$:
1. **Caso $f$ iniettiva:** si ha $\operatorname{Ker} f = \{\underline{0}_U\}$, quindi $\dim_K \operatorname{Ker} f = 0$. Dunque $\dim_K U = 0 + \dim_K \operatorname{Im} f = \dim_K \operatorname{Im} f \le \dim_K V$ *(poiché $\operatorname{Im} f$ è sottospazio di $V$)*.
2. **Caso $f$ suriettiva:** si ha $\operatorname{Im} f = V$, quindi $\dim_K U = \dim_K \operatorname{Ker} f + \dim_K V \ge \dim_K V$ *(poiché $\dim_K \operatorname{Ker} f \ge 0$)*.
3. **Caso $f$ isomorfismo:** $f$ è sia iniettiva che suriettiva, dunque valgono contemporaneamente $\dim_K U \le \dim_K V$ e $\dim_K U \ge \dim_K V$, da cui $\dim_K U = \dim_K V$.
:::

### 4. Esempi svolti

Tutte le applicazioni concrete di nucleo, immagine e Teorema sulle dimensioni svolte nelle Lezioni 10 e 11 utilizzano la famiglia modello $f_M(X) = MX$: le trovi raggruppate integralmente nella Sezione [6.3](#sec-6-3).

### 5. Errori comuni e trappole

1. **Scrivere $\operatorname{Ker} f = 0$ invece di $\operatorname{Ker} f = \{\underline{0}_U\}$**
    - *Sbagliato:* quando $\dim_K \operatorname{Ker} f = 0$, scrivere $\operatorname{Ker} f = 0$ oppure $\operatorname{Ker} f = \emptyset$.
    - *Correzione:* il nucleo è un **sottospazio vettoriale** del dominio $U$, non un numero e mai l'insieme vuoto! Quando la sua dimensione è $0$, esso contiene esattamente **un elemento** — il vettore nullo $\underline{0}_U$ — quindi si scrive **$\operatorname{Ker} f = \{\underline{0}_U\}$** *(es. $\{(0,0,0)\}$)*.
2. **Scambiare le disuguaglianze del Corollario (pensare che un'applicazione iniettiva richieda $\dim U \ge \dim V$)**
    - *Sbagliato:* credere che $\mathbb{R}^4 \to \mathbb{R}^3$ possa essere iniettiva.
    - *Correzione:* se parti da $\mathbb{R}^4$ e atterri in $\mathbb{R}^3$, per il Teorema sulle dimensioni $\dim \operatorname{Ker} f = 4 - \dim \operatorname{Im} f \ge 4 - 3 = 1$, quindi esiste sempre almeno una retta schiacciata in $\underline{0}$: un'applicazione $\mathbb{R}^4 \to \mathbb{R}^3$ non è **mai** iniettiva ($\dim U \le \dim V$ è necessario per l'iniettività!).

### 6. Riepilogo

- $\operatorname{Im} f = f(U) \subseteq V$; $f$ è **suriettiva** $\iff \operatorname{Im} f = V \iff \dim_K \operatorname{Im} f = \dim_K V$.
- $\operatorname{Ker} f = f^{-1}(\{\underline{0}_V\}) = \{u \in U \mid f(u) = \underline{0}_V\} \subseteq U$; $f$ è **iniettiva** $\iff \operatorname{Ker} f = \{\underline{0}_U\} \iff \dim_K \operatorname{Ker} f = 0$.
- **Teorema sulle dimensioni:** $\dim_K U = \dim_K \operatorname{Ker} f + \dim_K \operatorname{Im} f$.
- $f$ iniettiva $\implies \dim U \le \dim V$; $f$ suriettiva $\implies \dim U \ge \dim V$; $f$ isomorfismo $\implies \dim U = \dim V$.

### 7. Esercizi

La Lezione 10 *(pp. 5–6)* e la Lezione 11 *(pp. 1–2)* passano immediatamente allo studio operativo di $\operatorname{Ker} f_M$, $\operatorname{Im} f_M$ e controimmagini nella Sezione [6.3](#sec-6-3), dove trovi tutti i relativi esempi ed esercizi per casa.

<!-- section: sec-6-3 | num: 6.3 | title: Applicazioni associate a matrici (f_M), studio di nucleo, immagine e controimmagini | kind: section | part: cap-6 -->

### 1. Idea in parole semplici

Qual è la macchina più concreta per fabbricare applicazioni lineari tra spazi di vettori $K^n \to K^m$? Prendere una qualsiasi matrice $M \in K^{m,n}$ e moltiplicarla per il vettore colonna $X$: **$f_M(X) = MX$**.

La parte migliore è che per studiare completamente $f_M$ non serve inventare nulla di nuovo, basta riassumere due regole d'oro della Lezione 10 *(p. 8)*:
- **Nucleo $\operatorname{Ker} f_M$:** coincide esattamente con le soluzioni del sistema lineare omogeneo **$MX = \underline{0}$**, dunque $\dim \operatorname{Ker} f_M = n - \operatorname{rk} M$;
- **Immagine $\operatorname{Im} f_M$:** è generata esattamente dalle **colonne** di $M$ ($\mathcal{L}_C(M)$), dunque per Kronecker **$\dim \operatorname{Im} f_M = \operatorname{rk} M$**! Attento però: per semplificare i generatori di $\operatorname{Im} f_M$, devi lavorare sulle **colonne** di $M$ (riduzione per colonne), non sulle righe!

Infine, calcolare una **controimmagine** $f_M^{-1}(\{v\})$ significa semplicemente risolvere il sistema lineare $MX = v$: se $v \notin \operatorname{Im} f_M$ la controimmagine è $\emptyset$; altrimenti è formata da una soluzione particolare sommata al nucleo.

### 2. Definizioni e enunciati precisi

:::def Definizione — Applicazione lineare $f_M$ associata a una matrice $M$ (Lezione 10, p. 6)
Sia $M \in K^{m,n}$. Definiamo la funzione $f_M : K^n \to K^m$ ponendo:

$$f_M(X) \stackrel{\text{DEF}}{=} MX \qquad (\text{con } X \in K^{n,1},\ MX \in K^{m,1})$$
:::

:::thm Regole operative per lo studio di $f_M : K^n \to K^m$ (Lezione 10, pp. 6–8)
Per ogni $M \in K^{m,n}$:
1. $f_M$ è sempre un'**applicazione lineare**;
2. $\operatorname{Ker} f_M$ si calcola risolvendo il sistema omogeneo **$MX = \underline{0}$**, quindi $\dim_K \operatorname{Ker} f_M = n - \operatorname{rk} M$;
3. $\operatorname{Im} f_M = \mathcal{L}_C(M)$ *(è generata dalle **colonne** di $M$)*, quindi per il Teorema di Kronecker **$\dim_K \operatorname{Im} f_M = \operatorname{rk} M$**;
4. Per la controimmagine di un singolo vettore $v \in K^m$, $f_M^{-1}(\{v\}) = \{X \in K^n \mid MX = v\}$ è l'insieme delle soluzioni del sistema lineare completo $M|v$.
:::

### 3. Dimostrazioni

:::proof Dimostrazione — $f_M(X) = MX$ è un'applicazione lineare (Lezione 10, p. 6)
**Idea di fondo:** usiamo la proprietà distributiva a sinistra e la compatibilità con gli scalari del prodotto tra matrici.

Siano $a_1, a_2 \in K$ e $X_1, X_2 \in K^n = K^{n,1}$. Allora:

$$f_M(a_1 X_1 + a_2 X_2) = M(a_1 X_1 + a_2 X_2) = a_1(MX_1) + a_2(MX_2) = a_1 f_M(X_1) + a_2 f_M(X_2)$$

Dunque $f_M$ è lineare. *(Inoltre nell'Esempio di `Lez10` p. 7 mostra perché $\operatorname{Im} f_M$ è generata dalle colonne: $M X = x_1 C_1 + \dots + x_n C_n$, sicché ogni valore di $f_M$ è combinazione lineare delle colonne di $M$.)*
:::

### 4. Esempi svolti

:::example Esempio 6.3.1 — Quattro studi completi di $f_M$ con matrici numeriche (Lezione 10, pp. 6–10)
1. **Caso $\mathbb{R}^3 \to \mathbb{R}^2$ (pp. 6–7):** $M = \begin{pmatrix} 1 & 1 & 3 \\ 1 & 4 & 2 \end{pmatrix}$.
    - $\operatorname{Ker} f_M$: $\begin{pmatrix} 1 & 1 & 3 \\ 1 & 4 & 2 \end{pmatrix} \to \begin{pmatrix} 1 & 1 & 3 \\ 0 & 3 & -1 \end{pmatrix} \implies \operatorname{rk} M = 2$, $\dim_{\mathbb{R}} \operatorname{Ker} f_M = 3 - 2 = 1$. Con i minori a segno alterno: $d_1 = -10, d_2 = 1, d_3 = 3 \implies \operatorname{Ker} f_M = \mathcal{L}((-10, 1, 3))$.
    - $\operatorname{Im} f_M$: per il Teorema sulle dimensioni $\dim_{\mathbb{R}} \operatorname{Im} f_M = 3 - 1 = 2 = \dim_{\mathbb{R}} \mathbb{R}^2 \implies \operatorname{Im} f_M = \mathbb{R}^2$ e $f_M$ è **suriettiva** (non iniettiva).
2. **Caso $\mathbb{R}^2 \to \mathbb{R}^3$ (pp. 7–8):** $M = \begin{pmatrix} 1 & 1 \\ 1 & 4 \\ 3 & 2 \end{pmatrix}$.
    - $\operatorname{Im} f_M = \mathcal{L}((1,1,3), (1,4,2))$. Riduciamo **per colonne** ($C_2 \mapsto C_2 - C_1$): $\begin{pmatrix} \boxed{1} & 0 \\ 1 & \boxed{3} \\ 3 & -1 \end{pmatrix}$, quindi $\operatorname{rk} M = 2$, $\dim_{\mathbb{R}} \operatorname{Im} f_M = 2$ e una base di $\operatorname{Im} f_M$ è $\{(1,1,3), (0,3,-1)\}$ (non suriettiva).
    - $\operatorname{Ker} f_M$: $2 = \dim \operatorname{Ker} f_M + 2 \implies \dim \operatorname{Ker} f_M = 0 \implies \operatorname{Ker} f_M = \{(0,0)\}$: $f_M$ è **iniettiva**.
3. **Caso $\mathbb{R}^4 \to \mathbb{R}^3$ (pp. 8–9):** $M = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 1 & 1 & 5 & 2 \\ 2 & 3 & 8 & 6 \end{pmatrix}$.
    - Riduzione per righe per il rango e per $\operatorname{Ker} f_M$:
        $$\begin{pmatrix} 1 & 2 & 3 & 4 \\ 1 & 1 & 5 & 2 \\ 2 & 3 & 8 & 6 \end{pmatrix} \xrightarrow{\substack{R_2 \mapsto R_2 - R_1 \\ R_3 \mapsto R_3 - 2R_1}} \begin{pmatrix} 1 & 2 & 3 & 4 \\ 0 & -1 & 2 & -2 \\ 0 & -1 & 2 & -2 \end{pmatrix} \xrightarrow{R_3 \mapsto R_3 - R_2} \begin{pmatrix} \boxed{1} & 2 & 3 & 4 \\ 0 & \boxed{-1} & 2 & -2 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$
        Dunque $\operatorname{rk} M = 2 = \dim \operatorname{Im} f_M$ (non suriettiva). Poiché le prime due colonne contengono il minore non nullo $\det\begin{pmatrix} 1 & 2 \\ 1 & 1 \end{pmatrix} = -1 \neq 0$, esse sono linearmente indipendenti e quindi formano subito una base di $\operatorname{Im} f_M$: $\operatorname{Im} f_M = \mathcal{L}((1,1,2), (2,1,3))$.
    - $\dim_{\mathbb{R}} \operatorname{Ker} f_M = 4 - 2 = 2$ (non iniettiva). Dal sistema ridotto $\begin{cases} x+2y+3z+4t=0 \\ -y+2z-2t=0 \end{cases} \implies \begin{cases} y = 2z - 2t \\ x = -7z \end{cases}$, da cui $(-7z, 2z-2t, z, t) = z(-7,2,1,0) + t(0,-2,0,1)$: una base di $\operatorname{Ker} f_M$ è $\{(-7,2,1,0), (0,-2,0,1)\}$.
4. **Caso $\mathbb{R}^3 \to \mathbb{R}^4$ (pp. 9–10):** $M = \begin{pmatrix} 1 & 1 & 2 \\ 2 & 1 & 3 \\ 3 & 5 & 8 \\ 4 & 2 & 6 \end{pmatrix}$.
    - Riduciamo **per colonne**: $C_2 \mapsto C_2 - C_1$ e $C_3 \mapsto C_3 - 2C_1$ danno $\begin{pmatrix} 1 & 0 & 0 \\ 2 & -1 & -1 \\ 3 & 2 & 2 \\ 4 & -2 & -2 \end{pmatrix} \xrightarrow{C_3 \mapsto C_3 - C_2} \begin{pmatrix} \boxed{1} & 0 & 0 \\ 2 & \boxed{-1} & 0 \\ 3 & 2 & 0 \\ 4 & -2 & 0 \end{pmatrix}$. Quindi $\operatorname{rk} M = 2 = \dim \operatorname{Im} f_M$, $\dim \operatorname{Ker} f_M = 3 - 2 = 1$ (né iniettiva né suriettiva), e $\operatorname{Im} f_M = \mathcal{L}((1,2,3,4), (0,-1,2,-2))$.
    - Per $\operatorname{Ker} f_M$, poiché il minore delle prime $2$ righe vale $-1 \neq 0$, bastano le prime $2$ equazioni $\begin{pmatrix} 1 & 1 & 2 \\ 0 & -1 & -1 \end{pmatrix}$: con i minori a segno alterno $d_1=1, d_2=1, d_3=-1$, quindi $\operatorname{Ker} f_M = \mathcal{L}((1,1,-1))$.
:::

:::example Esempio 6.3.2 — Studio parametrico di $f_M : \mathbb{R}^3 \to \mathbb{R}^3$ (Lezione 10, pp. 10–11)
Sia $M = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 3 & 1 \\ 1 & 1 & h \end{pmatrix}$ con $h \in \mathbb{R}$.
- $\det M = 3h + 1 + 2 - 3 - 1 - 2h = h - 1 = 0 \iff h = 1$.
- **I caso ($h \neq 1$):** $\det M \neq 0 \implies \operatorname{rk} M = 3$, $\dim \operatorname{Im} f_M = 3 \implies \operatorname{Im} f_M = \mathbb{R}^3$, $\dim \operatorname{Ker} f_M = 0 \implies \operatorname{Ker} f_M = \{(0,0,0)\}$. Quindi $f_M$ è **biettiva** (un isomorfismo).
- **II caso ($h = 1$):** in $M = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 3 & 1 \\ 1 & 1 & 1 \end{pmatrix}$ il minore $\det\begin{pmatrix} 1 & 1 \\ 2 & 3 \end{pmatrix} = 1 \neq 0$, quindi $\operatorname{rk} M = 2$, $\dim \operatorname{Im} f_M = 2$ con $\operatorname{Im} f_M = \mathcal{L}((1,2,1), (1,3,1))$, e riducendo $\begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{pmatrix}$ i minori a segno alterno danno $d_1 = -2, d_2 = 1, d_3 = 1 \implies \operatorname{Ker} f_M = \mathcal{L}((-2,1,1))$.
:::

:::example Esempio 6.3.3 — Studio completo + controimmagine parametrica $f_M^{-1}(\{(2,1,3)\})$ (Lezione 11, pp. 2–4)
Sia $M = \begin{pmatrix} 2 & 1 & 3 \\ 1 & 1 & 2 \\ 3 & 4 & h \end{pmatrix}$, $f_M : \mathbb{R}^3 \to \mathbb{R}^3$ ($h \in \mathbb{R}$).

1. **Studio di $f_M$ (pp. 2–3):** $\det M = 2h + 6 + 12 - 9 - 16 - h = h - 7$.
    - **$h \neq 7$:** $\operatorname{rk} M = 3 \implies \operatorname{Im} f_M = \mathbb{R}^3$ (suriettiva) e $\dim \operatorname{Ker} f_M = 0$ (iniettiva), quindi $f_M$ è un **isomorfismo**.
    - **$h = 7$:** il minore $\det\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = 1 \neq 0$ dà $\operatorname{rk} M = 2$: $\operatorname{Im} f_M = \mathcal{L}((2,1,3), (1,1,4))$ ($\dim = 2$) e da $\begin{pmatrix} 2 & 1 & 3 \\ 1 & 1 & 2 \end{pmatrix}$ con minori a segno alterno $d_1=-1, d_2=-1, d_3=1$ segue $\operatorname{Ker} f_M = \mathcal{L}((-1,-1,1))$ ($\dim = 1$). Quindi per $h=7$ non è né iniettiva né suriettiva.

2. **Controimmagine $f_M^{-1}(\{(2,1,3)\})$ al variare di $h$ (pp. 3–4):**
    - **Per $h \neq 7$:** $f_M$ è un isomorfismo, quindi esiste un unico vettore. Poiché $(2,1,3)$ coincide esattamente con la **prima colonna** di $M$, vale $f_M(e_1) = (2,1,3)$, dunque:
        $$f_M^{-1}(\{(2,1,3)\}) = \{e_1\} = \{(1,0,0)\}$$
    - **Per $h = 7$:** risolviamo il sistema lineare $M|B$:
        $$\left(\begin{array}{ccc|c} 2 & 1 & 3 & 2 \\ 1 & 1 & 2 & 1 \\ 3 & 4 & 7 & 3 \end{array}\right) \xrightarrow{\substack{R_2 \mapsto R_2 - R_1 \\ R_3 \mapsto R_3 - 4R_1}} \left(\begin{array}{ccc|c} 2 & 1 & 3 & 2 \\ -1 & 0 & -1 & -1 \\ -5 & 0 & -5 & -5 \end{array}\right) \longrightarrow \left(\begin{array}{ccc|c} \boxed{2} & 1 & 3 & 2 \\ \boxed{1} & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right)$$
        Si ha $\operatorname{rk} A = \operatorname{rk}(A|B) = 2$: $\infty^1$ soluzioni. Da $x = 1 - z$ e $2(1-z)+y = -3z+2 \implies y = -z$:
        $$f_M^{-1}(\{(2,1,3)\}) = \{(1-z, -z, z) \mid z \in \mathbb{R}\} = \{(1,0,0) + z(-1,-1,1) \mid z \in \mathbb{R}\}$$
        *(Nota: ritroviamo esattamente la soluzione particolare $(1,0,0)$ più tutto il nucleo $\mathcal{L}((-1,-1,1))$!)*
:::

:::note Nota sugli appunti originali (`Lez11`, p. 3)
Nell'ultimo riquadro di p. 3 scrive per svista insiemistica $e_1 = f_M^{-1}(\{(2,1,3)\})$ dimenticando le graffe attorno a $e_1$: la scrittura esatta è $\{e_1\} = f_M^{-1}(\{(2,1,3)\})$, trattandosi di un sottoinsieme (singleton) di $\mathbb{R}^3$.
:::

:::example Esempio 6.3.4 — Altre due controimmagini da `Lez11` (pp. 4–6)
1. **Caso $\mathbb{R}^3 \to \mathbb{R}^2$ (pp. 4–5):** con $M = \begin{pmatrix} 1 & 3 & 4 \\ 2 & 5 & 1 \end{pmatrix}$, calcolare $f_M^{-1}(\{(1,3)\})$.
    - Poiché $\det\begin{pmatrix} 1 & 3 \\ 2 & 5 \end{pmatrix} = -1 \neq 0$, $\operatorname{rk} M = 2 \implies f_M$ è suriettiva (ogni vettore di $\mathbb{R}^2$ ha controimmagine non vuota con $\infty^1$ soluzioni).
    - Riduciamo: $\left(\begin{array}{ccc|c} 1 & 3 & 4 & 1 \\ 2 & 5 & 1 & 3 \end{array}\right) \xrightarrow{R_2 \mapsto R_2 - 2R_1} \left(\begin{array}{ccc|c} 1 & 3 & 4 & 1 \\ 0 & -1 & -7 & 1 \end{array}\right) \implies \begin{cases} y = -7z - 1 \\ x = 1 - 3(-7z-1) - 4z = 17z + 4 \end{cases}$.
    - Quindi $f_M^{-1}(\{(1,3)\}) = \{(4, -1, 0) + z(17, -7, 1) \mid z \in \mathbb{R}\}$.
2. **Caso $\mathbb{R}^4 \to \mathbb{R}^2$ parametrico (pp. 5–6):** con $M = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & h \end{pmatrix}$, calcolare $f_M^{-1}(\{(1,2)\})$ al variare di $h \in \mathbb{R}$.
    - Riducendo $R_2 \mapsto R_2 - R_1$: $\begin{pmatrix} 1 & 1 & 1 & 1 \\ 0 & 0 & 0 & h-1 \end{pmatrix}$.
    - **Se $h = 1$:** $\operatorname{rk} M = 1$, $\operatorname{Im} f_M = \mathcal{L}((1,1))$ e $(1,2) \notin \mathcal{L}((1,1))$, quindi **$f_M^{-1}(\{(1,2)\}) = \emptyset$**.
    - **Se $h \neq 1$:** $f_M$ è suriettiva ($\operatorname{rk} M = 2$); da $\left(\begin{array}{cccc|c} 1 & 1 & 1 & 1 & 1 \\ 0 & 0 & 0 & h-1 & 1 \end{array}\right)$ ricaviamo $t = \frac{1}{h-1}$ e $z = 1 - \frac{1}{h-1} - x - y = \frac{h-2}{h-1} - x - y$ (con $x, y$ libere):
        $$f_M^{-1}(\{(1,2)\}) = \left\{ x(1,0,-1,0) + y(0,1,-1,0) + \left(0,\ 0,\ \frac{h-2}{h-1},\ \frac{1}{h-1}\right) \;\middle|\; x, y \in \mathbb{R} \right\}$$
:::

### 5. Errori comuni e trappole

1. **Ridurre $M$ *per righe* e poi prendere le righe o le colonne modificate come base di $\operatorname{Im} f_M$**
    - *Sbagliato:* eseguire $R_2 \mapsto R_2 - R_1$ e poi dire che le colonne dell'ultima matrice ridotta generano $\operatorname{Im} f_M$.
    - *Correzione:* le operazioni sulle righe **cambiano** lo spazio delle colonne! Per avere una base di $\operatorname{Im} f_M$ hai due sole vie sicure:
        - o riduci **per colonne** ($C_i \mapsto C_i + a C_j$) tenendo le colonne non nulle ottenute, oppure
        - riduci per righe solo per individuare quali colonne contengono i pivot, ma poi metti nella base di $\operatorname{Im} f_M$ le **corrispondenti colonne originali** di $M$ (come fa il prof nell'Esempio 6.3.1(3))!
2. **Dire "studiare $f_M$" dimenticando uno dei pezzi richiesti**
    - *Sbagliato:* calcolare solo $\operatorname{Ker} f_M$ quando l'esercizio chiede *"studiare $f_M$"*.
    - *Correzione:* come esplicita il prof nella Lezione 10 *(p. 7)*, **"studiare $f$"** significa determinare: $\operatorname{rk} M$, $\dim \operatorname{Im} f_M$ + una base (e dire se è **suriettiva**), $\dim \operatorname{Ker} f_M$ + una base (e dire se è **iniettiva** o **biettiva/isomorfismo**).

### 6. Riepilogo

- $f_M : K^n \to K^m$, $f_M(X) = MX$, è lineare per ogni $M \in K^{m,n}$.
- $\operatorname{Ker} f_M$ è lo spazio delle soluzioni di $MX = \underline{0}$ ($\dim \operatorname{Ker} f_M = n - \operatorname{rk} M$).
- $\operatorname{Im} f_M = \mathcal{L}_C(M)$ ($\dim \operatorname{Im} f_M = \operatorname{rk} M$).
- "Studiare $f_M$" richiede sempre: $\operatorname{rk} M$, dimensioni e basi di $\operatorname{Im} f_M$ e $\operatorname{Ker} f_M$, iniettività e suriettività (al variare di eventuali parametri).
- $f_M^{-1}(\{v\})$ corrisponde alle soluzioni di $MX = v$: è vuoto se $v \notin \operatorname{Im} f_M$ ($\operatorname{rk} M < \operatorname{rk}(M|v)$).

### 7. Esercizi

:::exercise Esercizio 6.3.1 (Esercizio per casa 1 — Medio · Lezione 10, p. 11)
Sia:

$$M = \begin{pmatrix} 1 & 2 & 1 & 2 \\ 3 & 1 & 4 & 1 \\ 2 & -1 & 3 & h \end{pmatrix} \in \mathbb{R}^{3,4}, \qquad h \in \mathbb{R}$$

e sia $f_M : \mathbb{R}^4 \to \mathbb{R}^3$. Studiare $f_M$ al variare di $h \in \mathbb{R}$.

:::solution Soluzione spiegata passo-passo
**Ragionamento:** determiniamo $\operatorname{rk} M$ al variare di $h$ (riducendo per righe oppure usando il Teorema degli Orlati su un minore $2\times 2$ non nullo!), poi distinguiamo i casi per caratterizzare $\operatorname{Im} f_M$, $\operatorname{Ker} f_M$, iniettività e suriettività.

1. **Calcolo di $\operatorname{rk} M$ al variare di $h$:**
    Prendiamo il minore $2\times 2$ in alto a sinistra: $\det\begin{pmatrix} 1 & 2 \\ 3 & 1 \end{pmatrix} = 1 - 6 = -5 \neq 0$, quindi $\operatorname{rk} M \ge 2$ sempre. Calcoliamo i suoi due orlati di ordine $3$ *(con la colonna 3 e con la colonna 4)*:
    - orlato con la colonna $3$: $\det\begin{pmatrix} 1 & 2 & 1 \\ 3 & 1 & 4 \\ 2 & -1 & 3 \end{pmatrix} = 3 + 16 - 3 - 2 + 4 - 18 = 0$ *(infatti $R_2 - R_1 = (2, -1, 3, -1)$ coincide sulle prime $3$ entrate con $R_3$!)*;
    - orlato con la colonna $4$: $\det\begin{pmatrix} 1 & 2 & 2 \\ 3 & 1 & 1 \\ 2 & -1 & h \end{pmatrix} = h + 4 - 6 - 4 + 1 - 6h = -5h - 5 = -5(h + 1)$.

    L'unico orlato dipendente da $h$ si annulla per $-5(h+1) = 0 \iff h = -1$. *(Verifica rapida tramite riduzione: $R_3 \mapsto R_3 - (R_2 - R_1)$ trasforma la terza riga in $(0\ 0\ 0\ h+1)$!)*

2. **I caso ($h = -1$):**
    Tutti gli orlati sono nulli, quindi $\operatorname{rk} M = 2$:
    - **$\operatorname{Im} f_M$:** $\dim_{\mathbb{R}} \operatorname{Im} f_M = 2 < 3 \implies f_M$ **non è suriettiva**. Poiché il minore nelle prime $2$ colonne è $\neq 0$, una base di $\operatorname{Im} f_M$ è formata dalle prime due colonne di $M$:
        $$\operatorname{Im} f_M = \mathcal{L}\bigl((1, 3, 2),\ (2, 1, -1)\bigr)$$
    - **$\operatorname{Ker} f_M$:** $\dim_{\mathbb{R}} \operatorname{Ker} f_M = 4 - 2 = 2 \implies f_M$ **non è iniettiva**. Il sistema $MX = \underline{0}$ si riduce alle prime due equazioni ($R_2 \mapsto R_2 - 3R_1$):
        $$\begin{cases} x + 2y + z + 2t = 0 \\ -5y + z - 5t = 0 \end{cases} \implies \begin{cases} z = 5y + 5t \\ x = -2y - (5y + 5t) - 2t = -7y - 7t \end{cases}$$
        Con $y, t \in \mathbb{R}$ variabili libere, $(x,y,z,t) = y(-7, 1, 5, 0) + t(-7, 0, 5, 1)$, dunque:
        $$\operatorname{Ker} f_M = \mathcal{L}\bigl((-7, 1, 5, 0),\ (-7, 0, 5, 1)\bigr)$$

3. **II caso ($h \neq -1$):**
    Il secondo orlato vale $-5(h+1) \neq 0$, quindi $\operatorname{rk} M = 3$:
    - **$\operatorname{Im} f_M$:** $\dim_{\mathbb{R}} \operatorname{Im} f_M = 3 = \dim_{\mathbb{R}} \mathbb{R}^3 \implies$ **$\operatorname{Im} f_M = \mathbb{R}^3$** e **$f_M$ è suriettiva**.
    - **$\operatorname{Ker} f_M$:** $\dim_{\mathbb{R}} \operatorname{Ker} f_M = 4 - 3 = 1 \implies f_M$ **non è iniettiva** *(e non può mai esserlo perché $\dim \mathbb{R}^4 = 4 > 3$)*. Con $R_2 \mapsto R_2 - 3R_1$ e $R_3 \mapsto R_3 - (R_2 - R_1)$ si ottiene la terza equazione $(h+1)t = 0 \implies t = 0$. Le prime due equazioni diventano quindi $\begin{cases} z = 5y \\ x = -7y \end{cases}$:
        $$\operatorname{Ker} f_M = \mathcal{L}\bigl((-7, 1, 5, 0)\bigr)$$
    *(Verifica: $1(-7)+2(1)+1(5)+2(0)=0$, $3(-7)+1(1)+4(5)+0=0$, $2(-7)-1(1)+3(5)+h\cdot 0=0$ per ogni $h \in \mathbb{R}$!)*
:::
:::

:::exercise Esercizio 6.3.2 (Esercizio per casa 2 — Medio · Lezione 10, p. 11)
Sia:

$$M = \begin{pmatrix} h & 1 & 1 \\ 2 & h+1 & 2 \\ 1 & 1 & h \end{pmatrix} \in \mathbb{R}^{3,3}, \qquad h \in \mathbb{R}$$

e sia $f_M : \mathbb{R}^3 \to \mathbb{R}^3$. Studiare $f_M$ al variare di $h \in \mathbb{R}$.

:::solution Soluzione spiegata passo-passo
**Ragionamento:** trattandosi di un endomorfismo con matrice quadrata $3\times 3$, partiamo dal calcolo e dalla scomposizione di $\det M$ per separare subito il caso di isomorfismo ($\det M \neq 0$) dai valori critici.

1. **Determinante di $M$:**
    $$\det M = h^2(h+1) + 2 + 2 - (h+1) - 2h - 2h = h^3 + h^2 - 5h + 3$$
    Proviamo la radice $h = 1$: $1 + 1 - 5 + 3 = 0$. Dividendo con Ruffini per $(h-1)$: $h^3 + h^2 - 5h + 3 = (h-1)(h^2 + 2h - 3) = (h-1)(h-1)(h+3)$, ossia:
    $$\det M = (h - 1)^2 (h + 3)$$
    Dunque $\det M = 0 \iff h = 1 \text{ oppure } h = -3$.

2. **I caso ($h \neq 1$ e $h \neq -3$):**
    $\det M \neq 0 \implies \operatorname{rk} M = 3$. Pertanto:
    - $\dim_{\mathbb{R}} \operatorname{Im} f_M = 3 \implies \operatorname{Im} f_M = \mathbb{R}^3$ ($f_M$ **suriettiva**);
    - $\dim_{\mathbb{R}} \operatorname{Ker} f_M = 3 - 3 = 0 \implies \operatorname{Ker} f_M = \{(0,0,0)\}$ ($f_M$ **iniettiva**).
    Quindi $f_M$ è un **isomorfismo**.

3. **II caso ($h = 1$):**
    $M = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 2 & 2 \\ 1 & 1 & 1 \end{pmatrix}$ ha tutte e tre le righe proporzionali a $(1,1,1)$, dunque $\operatorname{rk} M = 1$ *(f_M non è né iniettiva né suriettiva)*.
    - $\operatorname{Im} f_M$: $\dim_{\mathbb{R}} \operatorname{Im} f_M = 1$, generata da qualsiasi colonna non nulla: $\operatorname{Im} f_M = \mathcal{L}((1, 2, 1))$.
    - $\operatorname{Ker} f_M$: $\dim_{\mathbb{R}} \operatorname{Ker} f_M = 3 - 1 = 2$; l'unica equazione indipendente è $x + y + z = 0 \implies x = -y - z$, quindi $(x,y,z) = y(-1,1,0) + z(-1,0,1)$:
        $$\operatorname{Ker} f_M = \mathcal{L}\bigl((-1, 1, 0),\ (-1, 0, 1)\bigr)$$

4. **III caso ($h = -3$):**
    $M = \begin{pmatrix} -3 & 1 & 1 \\ 2 & -2 & 2 \\ 1 & 1 & -3 \end{pmatrix}$. Poiché $\det\begin{pmatrix} -3 & 1 \\ 2 & -2 \end{pmatrix} = 6 - 2 = 4 \neq 0$ e $\det M = 0$, si ha $\operatorname{rk} M = 2$ *(né iniettiva né suriettiva)*.
    - $\operatorname{Im} f_M$: $\dim_{\mathbb{R}} \operatorname{Im} f_M = 2$; le prime due colonne sono indipendenti, quindi:
        $$\operatorname{Im} f_M = \mathcal{L}\bigl((-3, 2, 1),\ (1, -2, 1)\bigr)$$
    - $\operatorname{Ker} f_M$: $\dim_{\mathbb{R}} \operatorname{Ker} f_M = 3 - 2 = 1$. Usando le ultime due righe ridotte a $(2,-2,2)$ e $(1,1,-3)$ (dividendo la prima per $2$): $\begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -3 \end{pmatrix}$. Calcoliamo i minori a segno alterno:
        $$d_1 = \det\begin{pmatrix} -1 & 1 \\ 1 & -3 \end{pmatrix} = 2, \qquad d_2 = -\det\begin{pmatrix} 1 & 1 \\ 1 & -3 \end{pmatrix} = 4, \qquad d_3 = \det\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} = 2$$
        Dividendo $(2,4,2)$ per $2$, otteniamo:
        $$\operatorname{Ker} f_M = \mathcal{L}\bigl((1, 2, 1)\bigr)$$
        *(Verifica: $-3(1)+1(2)+1(1)=0$, $2(1)-2(2)+2(1)=0$, $1(1)+1(2)-3(1)=0$.)*
:::
:::

<!-- section: sec-6-4 | num: 6.4 | title: Isomorfismi, composizione di applicazioni lineari ed endomorfismi | kind: section | part: cap-6 -->

### 1. Idea in parole semplici

Tre concetti chiave della Lezione 11 completano il quadro strutturale delle applicazioni lineari:
1. **Isomorfismo:** un'applicazione lineare sia iniettiva che suriettiva (*biettiva*) trasforma due spazi vettoriali l'uno nell'altro senza perdere nessuna informazione, al punto che anche la sua funzione inversa $f^{-1}$ è lineare e due spazi isomorfi hanno sempre esattamente la stessa dimensione.
2. **Composizione ($g \circ f$):** applicare prima $f$ e poi $g$ dà ancora un'applicazione lineare. E per le applicazioni matriciali vale la regola d'oro che spiega il prodotto riga per colonna: comporre $f_M \circ f_N$ corrisponde esattamente a moltiplicare le matrici nell'ordine **$MN$**!
3. **Endomorfismo ($V \to V$):** quando dominio e codominio coincidono (in dimensione finita), iniettività e suriettività diventano **equivalenti**! Basta verificarne una per avere gratis anche l'altra (e quindi un isomorfismo).

### 2. Definizioni e enunciati precisi

:::def Definizione — Funzione biettiva e isomorfismo (Lezione 11, p. 1)
Una funzione $f : U \to V$ si dice **biettiva** se è sia iniettiva che suriettiva. Un'applicazione lineare biettiva si chiama **isomorfismo**.
:::

:::thm Proposizione — L'inversa di un isomorfismo (Lezione 11, p. 1)
Se $f : U \to V$ è un isomorfismo, allora anche la funzione inversa $f^{-1} : V \to U$ è un **isomorfismo**.
:::

:::thm Proposizione — Composizione di applicazioni lineari e prodotto di matrici (Lezione 11, pp. 6–7)
1. Se $U \xrightarrow{f} V \xrightarrow{g} W$ sono applicazioni lineari, allora la composizione $g \circ f : U \to W$ è un'**applicazione lineare**.
2. In particolare, per matrici compatibili $M \in K^{m,n}$ e $N \in K^{n,p}$ con $K^p \xrightarrow{f_N} K^n \xrightarrow{f_M} K^m$, vale:
    $$f_M \circ f_N = f_{MN}$$
    cioè la composizione delle applicazioni corrisponde al prodotto riga per colonna delle rispettive matrici *(attenzione: si esegue **prima** $N$ su $X$, poi $M$!)*.
:::

:::def Definizione e Proposizione — Endomorfismi (Lezione 11, pp. 7–8)
Si chiama **endomorfismo** un'applicazione lineare $f : V \to V$ dallo spazio vettoriale $V$ in se stesso.

Se $V$ è uno spazio vettoriale **finitamente generato** e $f : V \to V$ è un endomorfismo, allora:

$$f \text{ è iniettivo} \iff f \text{ è suriettivo}$$
:::

:::note Nota sugli appunti originali (`Lez11`, pp. 7–8)
1. Nell'enunciato sull'equivalenza iniettività $\iff$ suriettività per un endomorfismo (`Lez11`, p. 7), il prof omette per brevità l'ipotesi **«finitamente generato»** su $V$, che è necessaria affinché $\dim_K V$ sia un numero finito nell'applicazione del Teorema sulle dimensioni a p. 8 (su spazi di dimensione infinita l'equivalenza cade).
2. A p. 8 nella quarta formula scrive per piccolo lapsus grafico $\dim_f \operatorname{Im} f$ anziché $\dim_K \operatorname{Im} f$.
:::

### 3. Dimostrazioni

:::proof Dimostrazione 1 — $f^{-1}$ è un isomorfismo (Lezione 11, p. 1)
**Idea di fondo:** essendo $f$ biettiva, la funzione inversa $f^{-1}$ è automaticamente biettiva; per provare la linearità di $f^{-1}$ applichiamo $f$ ad ambo i membri sfruttando il fatto che $f$ è lineare e biettiva.

Dobbiamo dimostrare soltanto che $f^{-1}$ è un'applicazione lineare, cioè che $\forall a_1, a_2 \in K$ e $\forall v_1, v_2 \in V$:

$$f^{-1}(a_1 v_1 + a_2 v_2) = a_1 f^{-1}(v_1) + a_2 f^{-1}(v_2)$$

Per definizione di funzione inversa, poiché $f$ è iniettiva, questa uguaglianza equivale a provare che applicando $f$ a destra si ottiene $a_1 v_1 + a_2 v_2$. Calcoliamo infatti usando la linearità di $f$ e il fatto che $(f \circ f^{-1})(v_i) = v_i$:

$$f\bigl(a_1 f^{-1}(v_1) + a_2 f^{-1}(v_2)\bigr) = a_1 f\bigl(f^{-1}(v_1)\bigr) + a_2 f\bigl(f^{-1}(v_2)\bigr) = a_1 v_1 + a_2 v_2$$

Pertanto $f^{-1}$ è lineare e quindi è un isomorfismo.
:::

:::proof Dimostrazione 2 — La composizione $g \circ f$ è lineare e $f_M \circ f_N = f_{MN}$ (Lezione 11, p. 6)
**Idea di fondo:** srotoliamo $(g \circ f)(a_1 u_1 + a_2 u_2) = g(f(a_1 u_1 + a_2 u_2))$ portando fuori prima $a_1, a_2$ con la linearità di $f$ e poi con la linearità di $g$; per le matrici basta applicare l'associatività $M(NX) = (MN)X$.

1. Siano $a_1, a_2 \in K$ e $u_1, u_2 \in U$. Allora:
    $$(g \circ f)(a_1 u_1 + a_2 u_2) = g\bigl(f(a_1 u_1 + a_2 u_2)\bigr) \stackrel{f \text{ lin.}}{=} g\bigl(a_1 f(u_1) + a_2 f(u_2)\bigr) \stackrel{g \text{ lin.}}{=} a_1 g(f(u_1)) + a_2 g(f(u_2)) = a_1(g \circ f)(u_1) + a_2(g \circ f)(u_2)$$
2. Per ogni $X \in K^p = K^{p,1}$:
    $$(f_M \circ f_N)(X) = f_M(f_N(X)) = f_M(NX) = M(NX) = (MN)X = f_{MN}(X)$$
    Quindi $f_M \circ f_N = f_{MN}$.
:::

:::proof Dimostrazione 3 — Per un endomorfismo su $V$ fin. gen., iniettivo $\iff$ suriettivo (Lezione 11, pp. 7–8)
**Idea di fondo:** nel Teorema sulle dimensioni entrambi gli spazi valgono $V$, quindi $\dim_K V = \dim_K \operatorname{Ker} f + \dim_K \operatorname{Im} f$: azzerare $\dim_K \operatorname{Ker} f$ equivale esattamente a far coincidere $\dim_K \operatorname{Im} f$ con $\dim_K V$!

- **($\Rightarrow$) Supponiamo $f$ iniettivo:** allora $\operatorname{Ker} f = \{\underline{0}_V\}$, perciò $\dim_K \operatorname{Ker} f = 0$. Dal Teorema sulle dimensioni:
    $$\dim_K V = \underbrace{\dim_K \operatorname{Ker} f}_{0} + \dim_K \operatorname{Im} f \implies \dim_K V = \dim_K \operatorname{Im} f$$
    Poiché $\operatorname{Im} f$ è un sottospazio di $V$ della stessa dimensione di $V$, per la Proposizione della Sezione [5.5](#sec-5-5) segue $\operatorname{Im} f = V$, cioè $f$ è suriettivo.
- **($\Leftarrow$) Supponiamo $f$ suriettivo:** allora $\operatorname{Im} f = V$, quindi $\dim_K \operatorname{Im} f = \dim_K V$. Sostituendo nel Teorema sulle dimensioni:
    $$\dim_K V = \dim_K \operatorname{Ker} f + \dim_K V \implies \dim_K \operatorname{Ker} f = 0 \implies \operatorname{Ker} f = \{\underline{0}_V\}$$
    Dunque $f$ è iniettivo.
:::

### 4. Esempi svolti

:::example Esempio 6.4.1 — Matrice associata alla composizione $f_M \circ f_N$ (Lezione 11, p. 7)
Date $M = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 1 \end{pmatrix} \in \mathbb{R}^{2,3}$ ed $N = \begin{pmatrix} 1 & 1 & 1 & 4 \\ 2 & 0 & 1 & 3 \\ 5 & 1 & 1 & 2 \end{pmatrix} \in \mathbb{R}^{3,4}$, abbiamo $\mathbb{R}^4 \xrightarrow{f_N} \mathbb{R}^3 \xrightarrow{f_M} \mathbb{R}^2$. La matrice associata a $f_M \circ f_N : \mathbb{R}^4 \to \mathbb{R}^2$ è $MN \in \mathbb{R}^{2,4}$:

$$MN = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 & 4 \\ 2 & 0 & 1 & 3 \\ 5 & 1 & 1 & 2 \end{pmatrix} = \begin{pmatrix} 20 & 4 & 6 & 16 \\ 19 & 5 & 10 & 33 \end{pmatrix}$$

*(Controllo di una entrata: $\operatorname{ent}_{11}(MN) = 1+4+15=20$; $\operatorname{ent}_{24}(MN) = 16+15+2=33$.)*
:::

### 5. Errori comuni e trappole

1. **Moltiplicare le matrici nell'ordine di lettura della frase ("prima $f$, poi $g$") anziché $BA$**
    - *Sbagliato:* per calcolare $g \circ f$ dove $f$ ha matrice $A$ e $g$ ha matrice $B$, calcolare il prodotto $AB$.
    - *Correzione:* nella composizione $(g \circ f)(X) = g(f(X)) = B(AX) = (BA)X$, la prima funzione applicata a $X$ sta **più vicina a $X$**, quindi a **destra**! Pertanto $M(g \circ f) = BA$, non $AB$.
2. **Applicare "iniettivo $\iff$ suriettivo" a funzioni con dominio e codominio diversi**
    - *Sbagliato:* per $f : \mathbb{R}^2 \to \mathbb{R}^3$ trovare che è iniettiva e concludere che è un isomorfismo.
    - *Correzione:* l'equivalenza iniettiva $\iff$ suriettiva vale **esclusivamente per gli endomorfismi** ($V \to V$, stessa dimensione finita in partenza e in arrivo). Una funzione $\mathbb{R}^2 \to \mathbb{R}^3$ può essere iniettiva ma non è mai suriettiva!

### 6. Riepilogo

- Un'applicazione lineare biettiva si chiama **isomorfismo**; anche la sua inversa $f^{-1}$ è un isomorfismo.
- La composizione $g \circ f$ di due applicazioni lineari è lineare, e per applicazioni matriciali vale $f_M \circ f_N = f_{MN}$.
- Un **endomorfismo** è un'applicazione lineare $f : V \to V$.
- Per un endomorfismo su uno spazio $V$ finitamente generato, $f$ è iniettivo $\iff$ $f$ è suriettivo $\iff$ $f$ è un isomorfismo ($\iff \det M \neq 0$ se rappresentato da una matrice quadrata $M$).

### 7. Esercizi

:::exercise Esercizio 6.4.1 (Esercizio per casa — Medio · Lezione 11, p. 7)
Siano $\mathbb{R}^3 \xrightarrow{f} \mathbb{R}^2 \xrightarrow{g} \mathbb{R}^3$, con $f$ associata alla matrice $A = \begin{pmatrix} 1 & 1 & 2 \\ 3 & 1 & 4 \end{pmatrix}$ e $g$ associata alla matrice $B = \begin{pmatrix} 1 & 2 \\ 3 & 1 \\ 1 & 1 \end{pmatrix}$. Studiare l'applicazione lineare $g \circ f : \mathbb{R}^3 \to \mathbb{R}^3$.

:::solution Soluzione spiegata passo-passo
**Ragionamento:** per la regola di composizione $g \circ f = f_B \circ f_A = f_{BA}$. Calcoliamo quindi la matrice quadrata $C = BA \in \mathbb{R}^{3,3}$ e studiamo l'applicazione $f_C$ (rango, base e dimensione di $\operatorname{Im}(g\circ f)$ e di $\operatorname{Ker}(g\circ f)$, iniettività/suriettività).

1. **Calcolo della matrice associata $C = BA \in \mathbb{R}^{3,3}$:**
    $$C = BA = \begin{pmatrix} 1 & 2 \\ 3 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 & 2 \\ 3 & 1 & 4 \end{pmatrix} = \begin{pmatrix} 1\cdot 1 + 2\cdot 3 & 1\cdot 1 + 2\cdot 1 & 1\cdot 2 + 2\cdot 4 \\ 3\cdot 1 + 1\cdot 3 & 3\cdot 1 + 1\cdot 1 & 3\cdot 2 + 1\cdot 4 \\ 1\cdot 1 + 1\cdot 3 & 1\cdot 1 + 1\cdot 1 & 1\cdot 2 + 1\cdot 4 \end{pmatrix} = \begin{pmatrix} 7 & 3 & 10 \\ 6 & 4 & 10 \\ 4 & 2 & 6 \end{pmatrix}$$
    *(Osservazione teorica immediata: poiché $f$ passa attraverso $\mathbb{R}^2$, $\operatorname{rk}(BA)$ non può mai superare $2$, quindi $g \circ f$ non può essere un isomorfismo e avrà $\det C = 0$!)*

2. **Rango di $C$ e studio di $\operatorname{Im}(g \circ f)$:**
    Controlliamo il minore in alto a sinistra: $\det\begin{pmatrix} 7 & 3 \\ 6 & 4 \end{pmatrix} = 28 - 18 = 10 \neq 0$, quindi $\operatorname{rk} C \ge 2$. Calcoliamo $\det C$ *(o notiamo che la 3ª colonna è la somma delle prime due: $7+3=10$, $6+4=10$, $4+2=6$, quindi $C_3 = C_1 + C_2 \implies \det C = 0$!)*.
    Pertanto $\operatorname{rk} C = 2$.
    - $\dim_{\mathbb{R}} \operatorname{Im}(g \circ f) = 2 < 3 \implies$ **$g \circ f$ non è suriettiva**.
    - Poiché le prime due colonne di $C$ formano un minore $\neq 0$, esse costituiscono una base di $\operatorname{Im}(g \circ f)$:
        $$\operatorname{Im}(g \circ f) = \mathcal{L}\bigl((7, 6, 4),\ (3, 4, 2)\bigr)$$

3. **Studio di $\operatorname{Ker}(g \circ f)$:**
    Per il Teorema sulle dimensioni, $\dim_{\mathbb{R}} \operatorname{Ker}(g \circ f) = 3 - 2 = 1 \implies$ **$g \circ f$ non è iniettiva**.
    Scegliendo le prime due righe indipendenti $\begin{pmatrix} 7 & 3 & 10 \\ 6 & 4 & 10 \end{pmatrix}$, applichiamo i minori a segno alterno:
    $$d_1 = \det\begin{pmatrix} 3 & 10 \\ 4 & 10 \end{pmatrix} = 30 - 40 = -10, \qquad d_2 = -\det\begin{pmatrix} 7 & 10 \\ 6 & 10 \end{pmatrix} = -(70 - 60) = -10, \qquad d_3 = \det\begin{pmatrix} 7 & 3 \\ 6 & 4 \end{pmatrix} = 10$$
    Dividendo $(-10, -10, 10)$ per $10$ otteniamo la base semplicissima $\{(-1, -1, 1)\}$, ovvero:
    $$\operatorname{Ker}(g \circ f) = \mathcal{L}\bigl((-1, -1, 1)\bigr)$$
    *(Che si vede anche a colpo d'occhio: $C_3 = C_1 + C_2 \implies C_1 + C_2 - C_3 = \underline{0} \implies (-1,-1,1)$ annulla $C$!)*
:::
:::

<!-- section: sec-6-5 | num: 6.5 | title: Componenti rispetto a una base, matrice di passaggio e assegnazione su una base | kind: section | part: cap-6 -->

### 1. Idea in parole semplici

In uno spazio vettoriale con base $\mathcal{B} = \{v_1, \dots, v_n\}$, ogni vettore $v$ si può scrivere in **uno ed un solo modo** come $v = a_1 v_1 + \dots + a_n v_n$: la $n$-upla $(a_1, \dots, a_n)$ delle sue **componenti** funge da "coordinate" personalizzate rispetto al sistema di riferimento $\mathcal{B}$. Se poi cambiamo sistema di riferimento passando da una base $\mathcal{A}$ a una base $\mathcal{B}$, la tabella di conversione è una matrice quadrata invertibile chiamata **matrice del cambio di base** (o **matrice di passaggio**).

Infine, c'è un principio fondamentale che useremo di continuo negli esercizi d'esame del Capitolo 8: per conoscere un'intera applicazione lineare $f : U \to V$, **basta sapere dove manda i vettori di una sola base** $\{u_1, \dots, u_n\}$ di $U$! Se poi esprimiamo i vettori della base canonica $e_1, \dots, e_n$ in termini di $u_1, \dots, u_n$, per linearità troviamo subito le immagini $f(e_1), \dots, f(e_n)$, cioè proprio le **colonne** della matrice associata $A$!

### 2. Definizioni e enunciati precisi

:::def Definizione e Proposizione — Componenti di un vettore rispetto a una base (Lezione 11, p. 8)
Sia $V$ un $K$-spazio vettoriale finitamente generato e sia $\mathcal{B} = \{v_1, \dots, v_n\}$ una base di $V$. Ogni $v \in V$ si scrive come $v = \sum_{i=1}^n a_i v_i$ ($a_i \in K$).
- Gli scalari $(a_1, \dots, a_n)$ si chiamano **componenti del vettore $v$ rispetto alla base $\mathcal{B}$**.
- **Proposizione:** le componenti di un vettore $v$ rispetto a una base $\mathcal{B}$ sono **univocamente determinate**.
:::

:::def Definizione — Matrice del cambio di base (o matrice di passaggio) (Lezione 11, p. 9)
Siano $\mathcal{A} = \{u_1, \dots, u_n\}$ e $\mathcal{B} = \{v_1, \dots, v_n\}$ due basi dello spazio finitamente generato $V$. Scrivendo i vettori di una base come combinazioni lineari dei vettori dell'altra base *(mettendo i coefficienti per **colonna** negli esempi applicativi)*:

$$u_j = \sum_{i=1}^n a_{ij} v_i \qquad (1 \le j \le n)$$

la matrice $A = (a_{ij}) \in K^{n,n}$ si chiama **matrice del cambio di base** *(o **matrice di passaggio**)*. La matrice di passaggio inversa soddisfa $AB = I \iff A = B^{-1}$.
:::

:::note Nota sugli appunti originali (`Lez11`, p. 9 — CONTRASTO INTERNO definizione vs esempi)
A p. 9 della Lezione 11 compare una **discrepanza formale** tra la formula teorica generale e i due esempi svolti subito sotto alle pp. 9–10:
- nella formula teorica generale scrive $u_i = \sum_{j=1}^n a_{ij} v_j$ per $1 \le i \le n$ *(che disporrebbe le componenti dei vettori di $\mathcal{A}$ per **riga**)*;
- negli esempi concreti con $\mathcal{E} = \{e_1, e_2\}$ e $\mathcal{B} = \{v_1=(3,2),\ v_2=(1,1)\}$ (pp. 9–10) scrive $\begin{cases} v_1 = 3e_1 + 2e_2 \\ v_2 = 1e_1 + 1e_2 \end{cases} \implies A = \begin{pmatrix} 3 & 1 \\ 2 & 1 \end{pmatrix}$ e $\begin{cases} e_1 = v_1 - 2v_2 \\ e_2 = -v_1 + 3v_2 \end{cases} \implies B = \begin{pmatrix} 1 & -1 \\ -2 & 3 \end{pmatrix}$, disponendo dunque le coordinate dei nuovi vettori base per **colonna**!

Come si vede anche in tutta la Lezione 12 e nella diagonalizzazione (`Lez13`–`Lez14`), la convenzione effettiva usata negli esercizi del corso è **sempre per colonna** ($u_j = \sum_{i=1}^n a_{ij} v_i$, cioè le componenti di $v_1, v_2$ messe come colonne di $A$), coerente con l'azione a destra $f_M(X) = MX$.
:::

:::thm Proposizione — Esistenza e unicità dell'applicazione lineare su una base (Lezione 12, p. 1)
Siano $U$ e $V$ $K$-spazi vettoriali, sia $\mathcal{B} = \{u_1, \dots, u_n\}$ una **base** di $U$, e siano $v_1, \dots, v_n \in V$ vettori **qualsiasi**. Allora **esiste una ed una sola** applicazione lineare $f : U \to V$ tale che:

$$f(u_i) = v_i \qquad \text{per ogni } 1 \le i \le n$$
:::

### 3. Dimostrazioni

:::proof Dimostrazione — Unicità delle componenti rispetto a una base (Lezione 11, p. 8)
**Idea di fondo:** supponiamo che lo stesso vettore $v$ si possa scrivere con due liste di coefficienti $a_i$ e $b_i$; sottraendole otteniamo una combinazione lineare uguale al vettore nullo $\underline{0}_V$, e siccome i vettori di una base sono linearmente indipendenti, ogni differenza $a_i - b_i$ deve annullarsi.

Sia $v = \sum_{i=1}^n a_i v_i = \sum_{i=1}^n b_i v_i$. Portando tutto a sinistra otteniamo:

$$\sum_{i=1}^n a_i v_i - \sum_{i=1}^n b_i v_i = \underline{0}_V \implies \sum_{i=1}^n (a_i - b_i) v_i = \underline{0}_V$$

Ma $v_1, \dots, v_n$ formano una base e quindi sono linearmente indipendenti: l'unica loro combinazione nulla è quella con tutti scalari nulli. Pertanto $a_i - b_i = 0$ per ogni $1 \le i \le n$, ossia $a_i = b_i$ per ogni $i$.
:::

### 4. Esempi svolti

:::example Esempio 6.5.1 — Componenti di $v = (4,7)$ rispetto a $\mathcal{B} = \{(3,2), (1,1)\}$ e matrici di passaggio (Lezione 11, pp. 9–10)
1. **Calcolo delle componenti (p. 9):** data la base $\mathcal{B} = \{v_1, v_2\}$ con $v_1 = (3,2)$ e $v_2 = (1,1)$ in $\mathbb{R}^2$, vogliamo le componenti $(x,y)$ di $v = (4,7)$ rispetto a $\mathcal{B}$, cioè $(4,7) = x(3,2) + y(1,1)$:
    $$\begin{cases} 3x + y = 4 \\ 2x + y = 7 \end{cases} \implies \left(\begin{array}{cc|c} 3 & 1 & 4 \\ 2 & 1 & 7 \end{array}\right) \xrightarrow{R_2 \mapsto R_2 - R_1} \left(\begin{array}{cc|c} 3 & 1 & 4 \\ -1 & 0 & 3 \end{array}\right) \implies \begin{cases} x = -3 \\ -9 + y = 4 \implies y = 13 \end{cases}$$
    Le componenti di $v$ rispetto a $\mathcal{B}$ sono $(-3, 13)$, cioè $v = -3v_1 + 13v_2$.
2. **Matrici di passaggio inverse tra $\mathcal{E} = \{e_1, e_2\}$ e $\mathcal{B} = \{v_1, v_2\}$ (pp. 9–10):**
    - Esprimendo $\mathcal{B}$ in funzione di $\mathcal{E}$: $\begin{cases} v_1 = 3e_1 + 2e_2 \\ v_2 = 1e_1 + 1e_2 \end{cases} \implies$ matrice di passaggio $A = \begin{pmatrix} 3 & 1 \\ 2 & 1 \end{pmatrix}$.
    - Risolvendo il sistema per $e_1, e_2$: $v_1 - v_2 = (3e_1+2e_2)-(e_1+e_2) \dots$ più esattamente $2v_2 = 2e_1 + 2e_2 \implies v_1 - 2v_2 = e_1$, poi $e_2 = v_2 - e_1 = -v_1 + 3v_2$. Dunque:
        $$\begin{cases} e_1 = v_1 - 2v_2 \\ e_2 = -v_1 + 3v_2 \end{cases} \implies B = \begin{pmatrix} 1 & -1 \\ -2 & 3 \end{pmatrix}$$
    - Verifica che $AB = I$:
        $$\begin{pmatrix} 3 & 1 \\ 2 & 1 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ -2 & 3 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \iff A = B^{-1}$$
:::

:::example Esempio 6.5.2 — Determinare $A$ e la legge di $f : \mathbb{R}^2 \to \mathbb{R}^3$ data su una base non canonica (Lezione 12, pp. 1–2)
Sia $f : \mathbb{R}^2 \to \mathbb{R}^3$ l'applicazione lineare definita sulle immagini della base $\mathcal{B} = \{u_1, u_2\} = \{(1,1), (1,2)\}$:

$$\begin{cases} f(1,1) = (1,2,1) \\ f(1,2) = (3,1,2) \end{cases}$$

Determinare la matrice $A \in \mathbb{R}^{3,2}$ tale che $f = f_A$ e la legge $f(x,y)$.

1. **Verifichiamo che $\mathcal{B}$ è una base:** $u_1 = (1,1)$ e $u_2 = (1,2)$ sono linearmente indipendenti in numero pari a $\dim_{\mathbb{R}} \mathbb{R}^2 = 2$, quindi formano una base.
2. **Esprimiamo la base canonica $\mathcal{E} = \{e_1, e_2\}$ rispetto a $\{u_1, u_2\}$:**
    - $e_1 = xu_1 + yu_2$: $(1,0) = (x+y, x+2y) \implies \begin{cases} y = 1 - x \\ x + 2(1-x) = 0 \implies x = 2,\ y = -1 \end{cases} \implies e_1 = 2u_1 - u_2$.
    - $e_2 = xu_1 + yu_2$: $(0,1) = (x+y, x+2y) \implies \begin{cases} y = -x \\ x - 2x = 1 \implies x = -1,\ y = 1 \end{cases} \implies e_2 = -u_1 + u_2$.
3. **Calcoliamo $f(e_1)$ e $f(e_2)$ per linearità (le colonne di $A$!):**
    $$f(e_1) = f(2u_1 - u_2) = 2f(u_1) - f(u_2) = 2(1,2,1) - (3,1,2) = (2,4,2) - (3,1,2) = (-1, 3, 0)$$
    $$f(e_2) = f(-u_1 + u_2) = -f(u_1) + f(u_2) = -(1,2,1) + (3,1,2) = (2, -1, 1)$$
4. **Matrice associata $A$ e legge di $f$:**
    $$A = \begin{pmatrix} -1 & 2 \\ 3 & -1 \\ 0 & 1 \end{pmatrix}, \qquad f(x,y) = \begin{pmatrix} -1 & 2 \\ 3 & -1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} -x + 2y \\ 3x - y \\ y \end{pmatrix} \implies f(x,y) = (-x + 2y,\ 3x - y,\ y)$$
:::

### 5. Errori comuni e trappole

1. **Mettere come colonne di $A$ direttamente i vettori immagine $f(u_1), \dots, f(u_n)$**
    - *Sbagliato:* nell'Esempio 6.5.2 scrivere $A = \begin{pmatrix} 1 & 3 \\ 2 & 1 \\ 1 & 2 \end{pmatrix}$.
    - *Correzione:* le colonne della matrice $A$ (tale che $f = f_A$) sono sempre e solo **$f(e_1), f(e_2), \dots, f(e_n)$** (le immagini dei vettori della **base canonica**!), perché $A\begin{pmatrix} 1 \\ 0 \end{pmatrix}$ estrae proprio la prima colonna di $A$. Se ti sono dati $f(u_i)$ su un'altra base, devi prima ricavare gli $e_j$ come combinazione degli $u_i$ e calcolare $f(e_j)$ per linearità!
2. **Trasporre i vettori immagine scrivendoli per riga invece che per colonna dentro $A$**
    - *Sbagliato:* mettere $f(e_1)$ nella prima riga invece che nella prima colonna.
    - *Correzione:* siccome $f_A(X) = AX$ moltiplica $A$ a sinistra di una colonna $X = (x_1, \dots, x_n)^T = x_1 e_1 + \dots + x_n e_n$, si ha $AX = x_1 C_1 + \dots + x_n C_n$, quindi $C_j = f(e_j)$ è sempre la **colonna $j$-esima** di $A$.

### 6. Riepilogo

- Rispetto a una base $\mathcal{B} = \{v_1,\dots,v_n\}$, ogni vettore $v \in V$ ha **componenti uniche** $(a_1,\dots,a_n)$.
- Le matrici di passaggio tra due basi soddisfano $B = A^{-1}$ ($AB = I$) e negli esercizi si costruiscono disponendo le coordinate **per colonna**.
- Un'applicazione lineare $f : U \to V$ è **univocamente determinata** dai valori $f(u_1), \dots, f(u_n)$ assunti sui vettori di una qualsiasi base di $U$.
- Per trovare la matrice $A$ ($f = f_A$) date le immagini su una base $\{u_i\}$: esprimi ogni $e_j$ come combinazione lineare degli $u_i$, calcola $f(e_j)$ per linearità, e metti i risultati come colonne di $A$.

### 7. Esercizi

:::exercise Esercizio 6.5.1 (Esercizio per casa — Medio · Lezione 12, p. 2)
Siano assegnati i valori di un'applicazione lineare $f : \mathbb{R}^3 \to \mathbb{R}^4$:

$$f(1,1,1) = (2,1,1,0), \qquad f(3,1,1) = (0,0,0,1), \qquad f(1,0,1) = (1,1,0,2)$$

*(Nel testo viene già verificato che $\det\begin{pmatrix} 1 & 1 & 1 \\ 3 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix} = 1 + 1 - 1 - 3 = -2 \neq 0$, quindi $u_1=(1,1,1), u_2=(3,1,1), u_3=(1,0,1)$ formano una base di $\mathbb{R}^3$ ed esiste un'unica $f$ lineare che soddisfa tali assegnazioni.)*
Determinare la matrice $A \in \mathbb{R}^{4,3}$ tale che $f = f_A$ e scrivere la legge della funzione $f(x,y,z)$.

:::solution Soluzione spiegata passo-passo
**Ragionamento:** le $3$ colonne di $A$ sono $f(e_1)$, $f(e_2)$ e $f(e_3)$. Quindi esprimiamo ciascuno dei tre vettori canonici $e_1, e_2, e_3$ come combinazione lineare di $u_1=(1,1,1), u_2=(3,1,1), u_3=(1,0,1)$, calcoliamo poi $f(e_1), f(e_2), f(e_3)$ per linearità e li affianchiamo per colonna. *(Trucco rapido: confrontare direttamente le differenze tra $u_1, u_2, u_3$ evita quasi tutti i conti!)*

1. **Esprimiamo $e_1, e_2, e_3$ in termini di $u_1, u_2, u_3$:**
    - Osserva subito la differenza $u_2 - u_1 = (3,1,1) - (1,1,1) = (2,0,0) = 2e_1$:
        $$e_1 = -\frac{1}{2}u_1 + \frac{1}{2}u_2$$
    - Osserva la differenza $u_1 - u_3 = (1,1,1) - (1,0,1) = (0,1,0) = e_2$:
        $$e_2 = u_1 - u_3$$
    - Per $e_3 = (0,0,1)$, usiamo $u_3 = (1,0,1) = e_1 + e_3 \implies e_3 = u_3 - e_1$:
        $$e_3 = u_3 - \left(-\frac{1}{2}u_1 + \frac{1}{2}u_2\right) = \frac{1}{2}u_1 - \frac{1}{2}u_2 + u_3$$
    *(Ovviamente lo stesso identico risultato si ottiene riducendo con Gauss la matrice affiancata $(u_1\ u_2\ u_3 \mid I_3)$ o risolvendo i tre sistemi lineari.)*

2. **Calcoliamo le immagini $f(e_1)$, $f(e_2)$, $f(e_3)$ per linearità:**
    - $f(e_1) = -\frac{1}{2}f(u_1) + \frac{1}{2}f(u_2) = -\frac{1}{2}(2,1,1,0) + \frac{1}{2}(0,0,0,1) = \left(-1,\ -\frac{1}{2},\ -\frac{1}{2},\ \frac{1}{2}\right)$;
    - $f(e_2) = f(u_1) - f(u_3) = (2,1,1,0) - (1,1,0,2) = (1,\ 0,\ 1,\ -2)$;
    - $f(e_3) = \frac{1}{2}f(u_1) - \frac{1}{2}f(u_2) + f(u_3) = \left(1,\frac{1}{2},\frac{1}{2},0\right) - \left(0,0,0,\frac{1}{2}\right) + (1,1,0,2) = \left(2,\ \frac{3}{2},\ \frac{1}{2},\ \frac{3}{2}\right)$.

3. **Matrice associata $A \in \mathbb{R}^{4,3}$ e legge di $f$:**
    Disponiamo $f(e_1), f(e_2), f(e_3)$ come colonne di $A$:
    $$A = \begin{pmatrix} -1 & 1 & 2 \\ -\frac{1}{2} & 0 & \frac{3}{2} \\ -\frac{1}{2} & 1 & \frac{1}{2} \\ \frac{1}{2} & -2 & \frac{3}{2} \end{pmatrix}$$
    Moltiplicando $A$ per $(x,y,z)^T$ otteniamo la legge esplicita:
    $$f(x,y,z) = \left(-x + y + 2z,\quad -\frac{1}{2}x + \frac{3}{2}z,\quad -\frac{1}{2}x + y + \frac{1}{2}z,\quad \frac{1}{2}x - 2y + \frac{3}{2}z\right)$$

4. **Verifica sui tre vettori assegnati:**
    - $f(1,1,1) = (-1+1+2,\ -\frac{1}{2}+\frac{3}{2},\ -\frac{1}{2}+1+\frac{1}{2},\ \frac{1}{2}-2+\frac{3}{2}) = (2, 1, 1, 0)$ (OK);
    - $f(3,1,1) = (-3+1+2,\ -\frac{3}{2}+\frac{3}{2},\ -\frac{3}{2}+1+\frac{1}{2},\ \frac{3}{2}-2+\frac{3}{2}) = (0, 0, 0, 1)$ (OK);
    - $f(1,0,1) = (-1+2,\ -\frac{1}{2}+\frac{3}{2},\ -\frac{1}{2}+\frac{1}{2},\ \frac{1}{2}+\frac{3}{2}) = (1, 1, 0, 2)$ (OK).
:::
:::
