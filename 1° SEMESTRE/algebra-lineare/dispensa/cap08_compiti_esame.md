<!-- part: cap-8 | num: 8 | label: CAPITOLO 8 | title: Compiti d'esame svolti e commentati | refs: Fonti: Lezione 13 (23/11/2026, pp. 10–13) e Lezione 14 (25/11/2026, pp. 1–8) -->

<!-- section: sec-8-1 | num: 8.1 | title: Compito del 26/1/2026: applicazione R³ → R⁵, controimmagine e diagonalizzabilità | kind: section | part: cap-8 -->

### 1. Idea in parole semplici

Questo è il primo dei tre compiti reali d'esame risolti dal docente in aula tra la fine della Lezione 13 e l'inizio della Lezione 14. È un banco di prova perfetto perché mette alla prova **tutti i pezzi principali del corso in un unico problema**:
1. nella **Parte (1)** un'applicazione $f : \mathbb{R}^3 \to \mathbb{R}^5$ è data sui vettori della base canonica con un parametro $h$, e chiede nucleo, immagine e poi la controimmagine di un vettore di $\mathbb{R}^5$ (che esiste soltanto per uno specifico valore $h = -2$!);
2. nella **Parte (2)** chiede di studiare la diagonalizzabilità su $\mathbb{R}$ di una matrice $3 \times 3$ parametrica, dove bisogna controllare sistematicamente tutte e tre le zone critiche: quando $\Delta < 0$ (radici complesse), quando la radice già nota $x=1$ si ripete ($h=0$), e quando $\Delta = 0$ crea un altro autovalore doppio ($h=-\frac{1}{4}$).

### 2. Definizioni e enunciati precisi

#### Testo completo del Compito del 26/1/2026 *(Lezione 13, p. 10; Lezione 14, p. 1)*

- **Quesito (1) *(Lezione 13, p. 10)*:** Determinare il nucleo e l'immagine dell'applicazione lineare $f : \mathbb{R}^3 \to \mathbb{R}^5$ definita per $h \in \mathbb{R}$ da:
    $$f(1,0,0) = (h,\ h+1,\ 1,\ 0,\ 1), \qquad f(0,1,0) = (1,\ h+1,\ h,\ 1-h,\ 1), \qquad f(0,0,1) = (1,\ 2,\ 1,\ h-1,\ 1)$$
    Calcolare inoltre $f^{-1}\bigl(\{(0, 1, 1, -2, -1)\}\bigr)$ al variare di $h \in \mathbb{R}$.
- **Quesito (2) *(Lezione 14, p. 1)*:** Studiare la diagonalizzabilità sul campo dei numeri reali $\mathbb{R}$ della matrice:
    $$A = \begin{pmatrix} 1 & 1 & 2 \\ h & 2 & 3 \\ 0 & 0 & 1 \end{pmatrix}, \qquad h \in \mathbb{R}$$

:::note Nota sugli appunti originali (`Lez13`, p. 10 e p. 12)
1. **Incongruenza trascrittiva sul vettore della controimmagine:** a p. 10 il testo manoscritto del quesito riporta `(0, 1, 1, -4, -1)` *(con quarta componente `-4`)*, mentre a p. 12 — sia nella consegna ripetuta in cima sia nella colonna dei termini noti e in tutte le riduzioni successive — compare ed è svolto coerentemente il vettore **`(0, 1, 1, -2, -1)`**. Qui riportiamo la versione svolta dal prof `(0, 1, 1, -2, -1)`.
2. **Refuso in riga 5, colonna 3 a `Lez13` p. 12:** nella riscrittura del sistema `MX = (0,1,1,-2,-1)^T` l'elemento in basso a destra $(5,3)$ di $M$ viene trascritto come `h` anziché `1`, ma immediatamente sotto (nella riduzione di `A|B`) il docente utilizza correttamente `1`, coerente con $f(0,0,1) = (1,2,1,h-1,1)$ di p. 10.
:::

### 3. Dimostrazioni

In questa sezione di esercitazione d'esame non vengono dimostrate nuove proposizioni astratte: si applicano direttamente i risultati dei Capitoli 4–7 (Teorema sulle dimensioni, riduzione per colonne e Rouché-Capelli, Teorema sulla diagonalizzabilità).

### 4. Esempi svolti

Lo svolgimento integrale dei due quesiti del Compito del 26/1/2026 (con il completamento della controimmagine per $h=-2$ richiesto a `Lez13` p. 13) è presentato passo dopo passo come Esercizio d'esame nella Sezione **7. Esercizi** qui sotto.

### 5. Errori comuni e trappole

1. **Dimenticare il caso in cui $x = 1$ coincide con una delle radici del fattore quadratico**
    - *Sbagliato:* nella Parte (2), da $P_A(x) = (1-x)(x^2 - 3x + 2 - h)$ controllare solo $\Delta = 4h + 1 \ge 0$ e concludere subito "diagonalizzabile per $h > -\frac{1}{4}$".
    - *Correzione:* oltre a $\Delta = 0$ ($h = -\frac{1}{4}$), bisogna sempre verificare **per quale $h$ la radice lineare già estratta ($x = 1$) annulla anche il fattore quadratico**! Sostituendo $x = 1$ in $x^2 - 3x + 2 - h = 0$ si scopre $h = 0$, dove $1$ diventa un autovalore con $m_1 = 2$ ma $g_1 = 1 < 2$!
2. **Svolgere le operazioni sulle colonne dentro una matrice ampliata $(M \mid v)$ mescolando $v$ con le colonne di $M$**
    - *Sbagliato:* se riduci $(M \mid v)$ con operazioni sulle **colonne** che modificano l'ultima colonna ($C_4 \mapsto C_4 + C_1$), continuare poi a leggere le soluzioni $x, y, z$ direttamente senza tenere conto che hai spostato $v$!
    - *Correzione:* le operazioni sulle **colonne** dentro $(M \mid v)$ servono lecitamente a calcolare $\operatorname{rk}(M \mid v)$ per verificare la *risolubilità* con Rouché-Capelli ($v \in \operatorname{Im} f$?), come fa il prof a `Lez13` p. 12. Ma per calcolare le componenti effettive $(x,y,z)$ della soluzione, conviene risolvere direttamente il sistema lineare rispetto alle incognite (riducendo eventualmente per **righe**)!

### 6. Riepilogo

- Per studiare un'applicazione assegnata sulla base canonica, disponi subito le immagini come **colonne** di $M \in \mathbb{R}^{5,3}$.
- Nel Quesito (1): per $h = 1$, $\operatorname{rk} M = 1 \implies \dim \operatorname{Im} f = 1$, $\dim \operatorname{Ker} f = 2$; per $h \neq 1$, $\operatorname{rk} M = 3 \implies f$ è iniettiva ($\operatorname{Ker} f = \{\underline{0}\}$).
- La controimmagine di $(0,1,1,-2,-1)$ è non vuota **solo per $h = -2$**, dove vale l'unico vettore $\left(-\frac{1}{3},\ -\frac{2}{3},\ 0\right)$.
- Nel Quesito (2): $A$ è diagonalizzabile su $\mathbb{R}$ **se e solo se $h > -\frac{1}{4}$ e $h \neq 0$** (per $h < -\frac{1}{4}$ mancano radici reali; per $h = -\frac{1}{4}$ si ha $g_{3/2}=1 < 2$; per $h = 0$ si ha $g_1 = 1 < 2$).

### 7. Esercizi

:::exercise Esercizio 8.1.1 — Svolgimento completo del Compito del 26/1/2026 (Lezione 13, pp. 10–13; Lezione 14, pp. 1–2)
Risolvere integralmente i due quesiti del Compito del 26/1/2026 enunciati nella Sezione 2, completando anche il calcolo esplicito del vettore controimmagine per $h = -2$ lasciato aperto alla fine di `Lez13` p. 13.

:::solution Soluzione spiegata passo-passo

#### Parte (1) — Studio di $f : \mathbb{R}^3 \to \mathbb{R}^5$ e controimmagine (`Lez13`, pp. 10–13)

1. **Matrice associata $M \in \mathbb{R}^{5,3}$ e riduzione per colonne:**
    Disponiamo $f(e_1), f(e_2), f(e_3)$ per colonna:
    $$M = \begin{pmatrix} h & 1 & 1 \\ h+1 & h+1 & 2 \\ 1 & h & 1 \\ 0 & 1-h & h-1 \\ 1 & 1 & 1 \end{pmatrix}$$
    Riduciamo per colonne (conservando $\operatorname{Im} f = \mathcal{L}_C(M)$!): prima $C_2 \mapsto C_2 - C_1$ e $C_3 \mapsto C_3 - C_1$, poi $C_3 \mapsto C_3 - C_2$ *(notando che $h - 1 - (1 - h) = 2h - 2 = 2(h-1)$)*:
    $$M \longrightarrow \begin{pmatrix} h & 1-h & 1-h \\ h+1 & 0 & 1-h \\ 1 & h-1 & 0 \\ 0 & 1-h & h-1 \\ 1 & 0 & 0 \end{pmatrix} \xrightarrow{C_3 \mapsto C_3 - C_2} \begin{pmatrix} h & \boxed{1-h} & 0 \\ h+1 & 0 & \boxed{1-h} \\ 1 & h-1 & 1-h \\ 0 & 1-h & 2(h-1) \\ \boxed{1} & 0 & 0 \end{pmatrix}$$
    Gli elementi speciali sono $(1)$ in riga $5$ col. $1$, $(1-h)$ in riga $1$ col. $2$, $(1-h)$ in riga $2$ col. $3$: dunque il punto critico è $1 - h = 0 \iff h = 1$.

2. **I caso ($h = 1$):**
    $M$ diventa $\begin{pmatrix} 1 & 0 & 0 \\ 2 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix}$, quindi $\operatorname{rk} M = 1$:
    - **$\operatorname{Im} f$:** $\dim_{\mathbb{R}} \operatorname{Im} f = 1$ e $\operatorname{Im} f = \mathcal{L}\bigl((1, 2, 1, 0, 1)\bigr)$.
    - **$\operatorname{Ker} f$:** $\dim_{\mathbb{R}} \operatorname{Ker} f = 3 - 1 = 2$. L'unica equazione indipendente è $x + y + z = 0 \implies z = -x - y$, quindi $(x,y,-x-y) = x(1,0,-1) + y(0,1,-1)$:
        $$\operatorname{Ker} f = \mathcal{L}\bigl((1, 0, -1),\ (0, 1, -1)\bigr)$$

3. **II caso ($h \neq 1$):**
    Dividendo $C_2$ e $C_3$ per $h - 1 \neq 0$, si ha $\operatorname{rk} M = 3$:
    - **$\operatorname{Im} f$:** $\dim_{\mathbb{R}} \operatorname{Im} f = 3$ (non suriettiva essendo $3 < 5$). Dalle colonne originali (o da quelle ridotte, che mostrano una base più semplice a `Lez13` p. 12):
        $$\operatorname{Im} f = \mathcal{L}\bigl((h,\ h+1,\ 1,\ 0,\ 1),\ (-1,\ 0,\ 1,\ -1,\ 0),\ (0,\ -1,\ -1,\ 2,\ 0)\bigr)$$
    - **$\operatorname{Ker} f$:** $\dim_{\mathbb{R}} \operatorname{Ker} f = 3 - 3 = 0 \implies \operatorname{Ker} f = \{(0, 0, 0)\}$ e **$f$ è iniettiva**.

4. **Studio della controimmagine $f^{-1}\bigl(\{(0, 1, 1, -2, -1)\}\bigr)$:**
    - **Se $h = 1$:** $(0, 1, 1, -2, -1)$ non è multiplo di $(1, 2, 1, 0, 1)$, quindi $f^{-1}(\{(0,1,1,-2,-1)\}) = \emptyset$.
    - **Se $h \neq 1$:** verifichiamo se $(0,1,1,-2,-1) \in \operatorname{Im} f$ confrontando $\operatorname{rk}(M \mid v)$ con $\operatorname{rk} M = 3$. Con le colonne semplificate di $M$:
        $$\left(\begin{array}{ccc|c} h & -1 & 0 & 0 \\ h+1 & 0 & -1 & 1 \\ 1 & 1 & -1 & 1 \\ 0 & -1 & 2 & -2 \\ 1 & 0 & 0 & -1 \end{array}\right) \xrightarrow{C_4 \mapsto C_4 + C_1} \left(\begin{array}{ccc|c} h & -1 & 0 & h \\ h+1 & 0 & -1 & h+2 \\ 1 & 1 & -1 & 2 \\ 0 & -1 & 2 & -2 \\ 1 & 0 & 0 & 0 \end{array}\right) \xrightarrow{\substack{C_3 \mapsto C_3 + 2C_2 \\ C_4 \mapsto C_4 - 2C_2}} \left(\begin{array}{ccc|c} h & -1 & -2 & h+2 \\ h+1 & 0 & -1 & \boxed{h+2} \\ 1 & 1 & \boxed{1} & 0 \\ 0 & \boxed{-1} & 0 & 0 \\ \boxed{1} & 0 & 0 & 0 \end{array}\right)$$
        - Se $h + 2 \neq 0$ (cioè $h \neq -2$), il rango di $(M \mid v)$ è $4 \neq 3$, quindi $f^{-1}(\{(0,1,1,-2,-1)\}) = \emptyset$.
        - **Se $h = -2$ (`Lez13` p. 13 — completamento esplicito):** allora $h + 2 = 0$, il rango di $(M \mid v)$ vale $3 = \operatorname{rk} M$, quindi la controimmagine è non vuota e formata da **un unico vettore** *(essendo $f$ iniettiva)*. Sostituiamo $h = -2$ nel sistema originale $MX = (0, 1, 1, -2, -1)^T$:
            $$\begin{cases} -2x + y + z = 0 \\ -x - y + 2z = 1 \\ x - 2y + z = 1 \\ 3y - 3z = -2 \\ x + y + z = -1 \end{cases}$$
            Sottraendo la 5ª equazione dalla 1ª si ottiene subito $-3x = 1 \implies x = -\frac{1}{3}$! Sostituendo $x = -\frac{1}{3}$ nella 4ª e nella 5ª equazione:
            $$\begin{cases} y + z = -1 - \left(-\frac{1}{3}\right) = -\frac{2}{3} \\ y - z = -\frac{2}{3} \end{cases}$$
            Sommando le due equazioni $2y = -\frac{4}{3} \implies y = -\frac{2}{3}$, e sottraendo $2z = 0 \implies z = 0$.
            *(Verifica su tutte e $5$ le equazioni: $-2(-1/3)-2/3+0 = 0$; $-(-1/3)-(-2/3)+0 = 1$; $-1/3-2(-2/3)+0 = 1$; $3(-2/3)-0 = -2$; $-1/3-2/3+0 = -1$!)*
            Dunque per $h = -2$:
            $$f^{-1}\bigl(\{(0, 1, 1, -2, -1)\}\bigr) = \left\{\left(-\frac{1}{3},\ -\frac{2}{3},\ 0\right)\right\}$$

---

#### Parte (2) — Diagonalizzabilità su $\mathbb{R}$ di $A$ (`Lez14`, pp. 1–2)

1. **Polinomio caratteristico di $A = \begin{pmatrix} 1 & 1 & 2 \\ h & 2 & 3 \\ 0 & 0 & 1 \end{pmatrix}$:**
    Sviluppando con il I Teorema di Laplace lungo la riga $3$:
    $$P_A(x) = \det\begin{pmatrix} 1-x & 1 & 2 \\ h & 2-x & 3 \\ 0 & 0 & 1-x \end{pmatrix} = (1-x)\det\begin{pmatrix} 1-x & 1 \\ h & 2-x \end{pmatrix} = (1-x)\bigl[(1-x)(2-x) - h\bigr] = (1-x)(x^2 - 3x + 2 - h)$$
    Una prima radice reale è sempre $x = 1$; le altre due vengono da $x^2 - 3x + 2 - h = 0$, il cui discriminante è:
    $$\Delta = 9 - 4(2 - h) = 4h + 1$$
    Le radici sono tutte reali $\iff 4h + 1 \ge 0 \iff h \ge -\frac{1}{4}$.

2. **Analisi dei quattro casi (`Lez14`, pp. 1–2):**
    - **I caso ($h < -\frac{1}{4}$):** $\Delta < 0$, quindi due radici non sono in $\mathbb{R}$. **$A$ non è diagonalizzabile su $\mathbb{R}$**.
    - **Controllo di $x = 1$ come radice multipla:** sostituiamo $x = 1$ in $x^2 - 3x + 2 - h = 0$: $1 - 3 + 2 - h = 0 \iff h = 0$.
        - **II caso ($h = 0$):** $x^2 - 3x + 2 = 0$ ha radici $1$ e $2$, quindi $P_A(x) = -(x-1)^2(x-2)$: $\lambda = 1$ ($m_1 = 2$) e $\lambda = 2$ ($m_2 = 1 = g_2$). Calcoliamo $g_1$:
            $$g_1 = 3 - \operatorname{rk}(A - I) = 3 - \operatorname{rk}\begin{pmatrix} 0 & 1 & 2 \\ 0 & 1 & 3 \\ 0 & 0 & 0 \end{pmatrix} = 3 - 2 = 1 < m_1 = 2$$
            *(poiché $\det\begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix} = 3 - 2 = 1 \neq 0$)*. Dunque per $h = 0$, **$A$ non è diagonalizzabile**.
    - **Controllo di $\Delta = 0$ (radici multiple nel fattore quadratico):** $4h + 1 = 0 \iff h = -\frac{1}{4}$.
        - **III caso ($h = -\frac{1}{4}$):** l'equazione diventa $x^2 - 3x + \frac{9}{4} = \left(x - \frac{3}{2}\right)^2 = 0$, quindi $P_A(x) = -(x-1)\left(x - \frac{3}{2}\right)^2$: $\lambda = 1$ ($m_1 = 1 = g_1$) e $\lambda = \frac{3}{2}$ ($m_{3/2} = 2$). Calcoliamo $g_{3/2}$:
            $$g_{3/2} = 3 - \operatorname{rk}\left(A - \frac{3}{2}I\right) = 3 - \operatorname{rk}\begin{pmatrix} -\frac{1}{2} & 1 & 2 \\ -\frac{1}{4} & \frac{1}{2} & 3 \\ 0 & 0 & -\frac{1}{2} \end{pmatrix} = 3 - 2 = 1 < m_{3/2} = 2$$
            *(poiché il minore in basso a destra $\det\begin{pmatrix} 1/2 & 3 \\ 0 & -1/2 \end{pmatrix} = -\frac{1}{4} \neq 0$)*. Dunque per $h = -\frac{1}{4}$, **$A$ non è diagonalizzabile**.
    - **IV caso ($h > -\frac{1}{4}$ e $h \neq 0$):** $\Delta > 0$ e nessuna radice coincide con $1$, quindi $P_A(x)$ possiede **$3$ radici reali e distinte** ($m_\lambda = g_\lambda = 1$ per ciascuna). **$A$ è diagonalizzabile su $\mathbb{R}$**.
:::
:::

<!-- section: sec-8-2 | num: 8.2 | title: Compito del 16/2/2026: endomorfismo parametrico, semplicità e base di autovettori | kind: section | part: cap-8 -->

### 1. Idea in parole semplici

Il secondo compito reale d'esame (`Lez14`, pp. 3–5) testa un'abilità complementare fondamentale: qui la funzione non è data tramite una matrice già scritta né sui soli vettori canonici, ma tramite la sua **formula esplicita su $(x,y,z)$**, cioè $f(x,y,z) = (\dots)$. Il primo passo è sempre leggere i coefficienti di $x, y, z$ nelle tre componenti per ricostruire la matrice associata $M(f)$.

In più, questo compito introduce un termine d'esame importantissimo da memorizzare a caratteri cubitali: quando il testo chiede di studiare la **semplicità** di un endomorfismo $f$, significa esattamente studiarne la **diagonalizzabilità**! Nel caso $h = 0$ proposto, i tre autovalori risultano subito distinti ($1, 2, 4$), quindi l'endomorfismo è immediatamente semplice e possiamo trovare facilmente la base di autovettori richiesta.

### 2. Definizioni e enunciati precisi

#### Testo completo del Compito del 16/2/2026 *(Lezione 14, pp. 3–4)*

Sia $f : \mathbb{R}^3 \to \mathbb{R}^3$ l'applicazione lineare definita al variare di $h \in \mathbb{R}$ da:

$$f(x,y,z) = \bigl(2x + hy,\quad (h-2)x + (h+1)y - 3z,\quad 2x - hy + 4z\bigr)$$

1. **Quesito (1):** Studiare $f$ al variare di $h \in \mathbb{R}$ *(cioè determinare dimensioni e basi di $\operatorname{Ker} f$ e $\operatorname{Im} f$, iniettività, suriettività / isomorfismo al variare di $h$)*.
2. **Quesito (2):** Studiare la **semplicità** di $f$ nel caso **$h = 0$** e, se possibile, determinare una **base di autovettori** di $\mathbb{R}^3$.

### 3. Dimostrazioni

Non sono richieste nuove dimostrazioni teoriche; ci si appoggia all'equivalenza **semplicità $\iff$ diagonalizzabilità** *(Sezione [7.4](#sec-7-4))*, al calcolo di $\det M$ e ai minori a segno alterno.

### 4. Esempi svolti

Lo svolgimento integrale di entrambi i quesiti del Compito del 16/2/2026 è presentato passo dopo passo nell'esercizio d'esame della Sezione **7. Esercizi**.

### 5. Errori comuni e trappole

1. **Scrivere $M(f)$ mettendo le espressioni delle componenti per colonna anziché per riga**
    - *Sbagliato:* vedere `2x + hy` nella prima componente e metterlo come prima *colonna* $\begin{pmatrix} 2 \\ h \\ 0 \end{pmatrix}$.
    - *Correzione:* la prima componente di $M\begin{pmatrix} x \\ y \\ z \end{pmatrix}$ è il prodotto della **prima riga** di $M$ per $\begin{pmatrix} x \\ y \\ z \end{pmatrix}$! Quindi i coefficienti di $(x,y,z)$ nella prima componente (`2, h, 0`) formano la **prima riga** di $M(f)$ (che equivale ovviamente a mettere $f(1,0,0), f(0,1,0), f(0,0,1)$ come colonne!).
2. **Fermarsi davanti alla parola "semplicità"**
    - *Sbagliato:* confondersi pensando a una proprietà diversa dagli autovalori e dalla diagonalizzabilità.
    - *Correzione:* nella terminologia del corso *(Lezione 14, p. 4)*, **"semplicità $\iff$ diagonalizzabilità"**!

### 6. Riepilogo

- Dalla legge $f(x,y,z) = (2x+hy,\ (h-2)x+(h+1)y-3z,\ 2x-hy+4z)$ si estrae $M(f) = \begin{pmatrix} 2 & h & 0 \\ h-2 & h+1 & -3 \\ 2 & -h & 4 \end{pmatrix}$.
- $\det M = -4(h^2 - h - 2) = -4(h + 1)(h - 2)$: per $h \neq -1, 2$ è un **isomorfismo** ($\operatorname{Ker} f = \{\underline{0}\}$, $\operatorname{Im} f = \mathbb{R}^3$).
- Per $h = -1$: $\dim \operatorname{Im} f = 2$ con base $\{(2,-3,2), (-1,0,1)\}$ e $\operatorname{Ker} f = \mathcal{L}((1,2,-1))$.
- Per $h = 2$: $\dim \operatorname{Im} f = 2$ con base $\{(1,0,1), (2,3,-2)\}$ e $\operatorname{Ker} f = \mathcal{L}((-1,1,1))$.
- Per $h = 0$: $P_M(x) = (2-x)(1-x)(4-x)$ ha $3$ radici distinte ($1, 2, 4$), quindi $f$ è **semplice** con base di autovettori $\{(0,1,0),\ (1,1,-1),\ (0,1,-1)\}$.

### 7. Esercizi

:::exercise Esercizio 8.2.1 — Svolgimento completo del Compito del 16/2/2026 (Lezione 14, pp. 3–5)
Risolvere entrambi i quesiti del Compito del 16/2/2026 enunciati nella Sezione 2.

:::solution Soluzione spiegata passo-passo

#### Parte (1) — Studio di $f$ al variare di $h \in \mathbb{R}$ (`Lez14`, pp. 3–4)

1. **Matrice associata $M = M(f)$ e calcolo di $\det M$:**
    Scriviamo i coefficienti di $x, y, z$ nelle tre righe *(equivale a $f(1,0,0), f(0,1,0), f(0,0,1)$ per colonna)*:
    $$M = M(f) = \begin{pmatrix} 2 & h & 0 \\ h-2 & h+1 & -3 \\ 2 & -h & 4 \end{pmatrix}$$
    Calcoliamo $\det M$:
    $$\det M = 8(h+1) - 6h + 0 - 0 - 6h - 4h(h-2) = 8h + 8 - 12h - 4h^2 + 8h = -4h^2 + 4h + 8 = -4(h^2 - h - 2)$$
    Risolviamo $\det M = 0 \iff h^2 - h - 2 = 0$: $\Delta = 1 + 8 = 9$, quindi $h = \frac{1 \pm 3}{2}$, cioè **$h = -1$** oppure **$h = 2$**.

2. **I caso ($h \neq -1$ e $h \neq 2$):**
    $\det M \neq 0 \implies \operatorname{rk} M = 3$. Pertanto:
    - $\operatorname{Im} f = \mathbb{R}^3$ ($\dim_{\mathbb{R}} \operatorname{Im} f = 3$, $f$ suriettiva);
    - $\operatorname{Ker} f = \{(0, 0, 0)\}$ ($\dim_{\mathbb{R}} \operatorname{Ker} f = 0$, $f$ iniettiva).
    Quindi per $h \neq -1, 2$ l'endomorfismo **$f$ è un isomorfismo**.

3. **II caso ($h = -1$):**
    $$M = \begin{pmatrix} 2 & -1 & 0 \\ -3 & 0 & -3 \\ 2 & 1 & 4 \end{pmatrix}$$
    Il minore in alto a sinistra vale $\det\begin{pmatrix} 2 & -1 \\ -3 & 0 \end{pmatrix} = -3 \neq 0$, quindi $\operatorname{rk} M = 2$: $\dim_{\mathbb{R}} \operatorname{Im} f = 2$ e $\dim_{\mathbb{R}} \operatorname{Ker} f = 1$ *(né iniettiva né suriettiva)*.
    - **$\operatorname{Im} f$:** le prime due colonne contengono il minore $\neq 0$, quindi formano una base:
        $$\operatorname{Im} f = \mathcal{L}\bigl((2, -3, 2),\ (-1, 0, 1)\bigr)$$
    - **$\operatorname{Ker} f$:** risolviamo il sistema formato dalle prime due righe indipendenti:
        $$\begin{cases} 2x - y = 0 \\ -3x - 3z = 0 \end{cases} \iff \begin{cases} y = 2x \\ z = -x \end{cases}$$
        Scegliendo $x = 1$ si ha $y = 2, z = -1$: dunque $\operatorname{Ker} f = \mathcal{L}\bigl((1, 2, -1)\bigr)$.

4. **III caso ($h = 2$):**
    $$M = \begin{pmatrix} 2 & 2 & 0 \\ 0 & 3 & -3 \\ 2 & -2 & 4 \end{pmatrix}$$
    Il minore in alto a sinistra vale $\det\begin{pmatrix} 2 & 2 \\ 0 & 3 \end{pmatrix} = 6 \neq 0$, quindi $\operatorname{rk} M = 2$: $\dim_{\mathbb{R}} \operatorname{Im} f = 2$ e $\dim_{\mathbb{R}} \operatorname{Ker} f = 1$.
    - **$\operatorname{Im} f$:** prendendo le prime due colonne (e dividendo la prima per $2$):
        $$\operatorname{Im} f = \mathcal{L}\bigl((2, 0, 2),\ (2, 3, -2)\bigr) = \mathcal{L}\bigl((1, 0, 1),\ (2, 3, -2)\bigr)$$
    - **$\operatorname{Ker} f$:** dalle prime due righe:
        $$\begin{cases} 2x + 2y = 0 \\ 3y - 3z = 0 \end{cases} \iff \begin{cases} x = -y \\ z = y \end{cases}$$
        Scegliendo $y = 1$ si ha $x = -1, z = 1$: dunque $\operatorname{Ker} f = \mathcal{L}\bigl((-1, 1, 1)\bigr)$.

---

#### Parte (2) — Semplicità di $f$ per $h = 0$ e base di autovettori (`Lez14`, pp. 4–5)

1. **Verifica della semplicità (diagonalizzabilità):**
    Sostituiamo $h = 0$ in $M$:
    $$M = \begin{pmatrix} 2 & 0 & 0 \\ -2 & 1 & -3 \\ 2 & 0 & 4 \end{pmatrix}$$
    Calcoliamo il polinomio caratteristico $P_M(x)$ sviluppando con Laplace lungo la prima riga:
    $$P_M(x) = \det\begin{pmatrix} 2-x & 0 & 0 \\ -2 & 1-x & -3 \\ 2 & 0 & 4-x \end{pmatrix} = (2-x)(1-x)(4-x)$$
    $P_M(x)$ ha **$3$ radici reali e distinte** ($\lambda_1 = 1$, $\lambda_2 = 2$, $\lambda_3 = 4$): ciascuna ha $m_\lambda = g_\lambda = 1$, quindi **$f$ è semplice** (e $M$ è simile a $D = \operatorname{diag}(1, 2, 4)$).

2. **Calcolo degli autospazi e della base di autovettori:**
    - **$V_1$ ($\lambda = 1$):** $(M - I)X = \underline{0} \iff \begin{pmatrix} 1 & 0 & 0 \\ -2 & 0 & -3 \\ 2 & 0 & 3 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \underline{0} \iff \begin{cases} x = 0 \\ 2x + 3z = 0 \end{cases} \implies \begin{cases} x = 0 \\ z = 0 \end{cases}$ (con $y$ libera!).
        Quindi $V_1 = \mathcal{L}\bigl((0, 1, 0)\bigr)$.
    - **$V_2$ ($\lambda = 2$):** $(M - 2I)X = \underline{0} \iff \begin{pmatrix} 0 & 0 & 0 \\ -2 & -1 & -3 \\ 2 & 0 & 2 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \underline{0} \iff \begin{cases} 2x + y + 3z = 0 \\ 2x + 2z = 0 \end{cases} \iff \begin{cases} z = -x \\ 2x + y - 3x = 0 \implies y = x \end{cases}$.
        Scegliendo $x = 1$: $V_2 = \mathcal{L}\bigl((1, 1, -1)\bigr)$.
    - **$V_4$ ($\lambda = 4$):** $(M - 4I)X = \underline{0} \iff \begin{pmatrix} -2 & 0 & 0 \\ -2 & -3 & -3 \\ 2 & 0 & 0 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \underline{0} \iff \begin{cases} x = 0 \\ 3y + 3z = 0 \implies y = -z \end{cases}$.
        Scegliendo $z = -1$ *(così $y = 1$)*: $V_4 = \mathcal{L}\bigl((0, 1, -1)\bigr)$.

    Unendo i tre autovettori otteniamo la base di $\mathbb{R}^3$ formata da autovettori:
    $$\mathcal{B} = \bigl\{(0, 1, 0),\ (1, 1, -1),\ (0, 1, -1)\bigr\}$$
:::
:::

<!-- section: sec-8-3 | num: 8.3 | title: Compito del 15/5/2026: trasposta, composizione e diagonalizzabilità parametrica | kind: section | part: cap-8 -->

### 1. Idea in parole semplici

Questo terzo e ultimo compito d'esame (`Lez14`, pp. 6–8) è un esercizio riepilogativo completo che collega **quattro capitoli del corso** in un colpo solo:
1. Nella **Parte (1)** parte da una matrice rettangolare $M \in \mathbb{R}^{3,4}$, ne chiede la **trasposta** ${}^t M \in \mathbb{R}^{4,3}$ (Capitolo 2) e lo studio dell'applicazione lineare $f : \mathbb{R}^3 \to \mathbb{R}^4$ associata a ${}^t M$ (Capitolo 6).
2. Nella **Parte (2)** introduce una seconda applicazione $g : \mathbb{R}^4 \to \mathbb{R}^3$ definita **su una base non canonica** (serve calcolare $g(1,0,0,0)$ per linearità!), chiede di comporre **$g \circ f : \mathbb{R}^3 \to \mathbb{R}^3$** moltiplicando le matrici $N = M(g)M(f)$, e infine di studiare la **diagonalizzabilità su $\mathbb{R}$ di $N$** (Capitolo 7).

A `Lez14` p. 8 il prof calcola il polinomio caratteristico $P_N(x) = (2-x)(x^2 + 4x + 5h - 30)$ e scrive *"COMPLETARE L'ESERCIZIO"*: noi svolgiamo tutto fino all'ultima disuguaglianza!

### 2. Definizioni e enunciati precisi

#### Testo completo del Compito del 15/5/2026 *(Lezione 14, pp. 6–7)*

- **Quesito (1):** Sia $M = \begin{pmatrix} 1 & 1 & 3 & 4 \\ 3 & 4 & 4 & h \\ 2 & h-3 & 1 & 2 \end{pmatrix} \in \mathbb{R}^{3,4}$ con $h \in \mathbb{R}$. Studiare l'applicazione lineare $f : \mathbb{R}^3 \to \mathbb{R}^4$ associata a **${}^t M$** *(ossia $M(f) = {}^t M$)*.
- **Quesito (2):** Sia $g : \mathbb{R}^4 \to \mathbb{R}^3$ l'applicazione lineare così definita sulla base $\{(1,1,3,4), (0,1,0,0), (0,0,1,0), (0,0,0,1)\}$ di $\mathbb{R}^4$:
    $$g(1,1,3,4) = (2,0,0), \qquad g(0,1,0,0) = (1,1,0), \qquad g(0,0,1,0) = (0,0,1), \qquad g(0,0,0,1) = (0,0,0)$$
    Studiare la **diagonalizzabilità** (su $\mathbb{R}$) dell'endomorfismo composto **$g \circ f : \mathbb{R}^3 \to \mathbb{R}^3$** al variare di $h \in \mathbb{R}$.

### 3. Dimostrazioni

Non sono previste dimostrazioni astratte in questa esercitazione d'esame; si applicano trasposizione, riduzione per colonne, assegnazione su una base, prodotto di matrici per la composizione $M(g\circ f) = M(g)M(f)$ e Teorema sulla diagonalizzabilità.

### 4. Esempi svolti

L'intero svolgimento commentato di entrambe le parti del Compito del 15/5/2026 (incluso il completamento completo della diagonalizzabilità di $g \circ f$) è riportato passo-passo qui sotto nella Sezione **7. Esercizi**.

### 5. Errori comuni e trappole

1. **Dimenticare di trasporre $M$ prima di studiare $f$**
    - *Sbagliato:* associare $f$ direttamente a $M \in \mathbb{R}^{3,4}$ ottenendo un'applicazione $\mathbb{R}^4 \to \mathbb{R}^3$.
    - *Correzione:* il testo dice esplicitamente *"associata a ${}^t M$"*! Quindi il dominio è $\mathbb{R}^3$, il codominio è $\mathbb{R}^4$, e si lavora su $M(f) = {}^t M \in \mathbb{R}^{4,3}$.
2. **Dimenticare di controllare i valori critici in cui $x = 2$ è radice doppia di $P_N(x)$ nel completamento**
    - *Sbagliato:* da $P_N(x) = (2-x)(x^2+4x+5h-30)$ imporre solo $\Delta/4 = 34 - 5h > 0 \implies h < \frac{34}{5}$.
    - *Correzione:* proprio come nel Compito 1 (`8.1`), ci sono **due** soglie critiche in cui compaiono autovalori multipli: $h = \frac{34}{5}$ ($\Delta = 0$, radice doppia $x = -2$) **e** $h = \frac{18}{5}$ ($x = 2$ è anche radice del fattore quadratico, diventando radice doppia!). In entrambi i casi bisogna calcolare $g_\lambda = 3 - \operatorname{rk}(N - \lambda I)$, e vedremo che in **entrambi** vale $g_\lambda = 1 < 2$!

### 6. Riepilogo

- $M(f) = {}^t M \in \mathbb{R}^{4,3}$ ha rango $3$ per $h \neq 6$ ($f$ **iniettiva**) e rango $2$ per $h = 6$ ($\operatorname{Im} f$ generata da 2 colonne, $\operatorname{Ker} f = \mathcal{L}((1,-1,1))$).
- Per trovare $M(g)$ occorre ricavare $e_1 = (1,1,3,4) - e_2 - 3e_3 - 4e_4 \implies g(e_1) = (1, -1, -3)$.
- La matrice della composizione è $N = M(g)M(f) = \begin{pmatrix} 2 & 7 & h-1 \\ 0 & 1 & h-5 \\ 0 & -5 & -5 \end{pmatrix}$.
- Il polinomio caratteristico è $P_N(x) = (2-x)(x^2 + 4x + 5h - 30)$ con $\Delta/4 = 34 - 5h$.
- $N = M(g \circ f)$ è diagonalizzabile su $\mathbb{R}$ **se e solo se $h < \frac{34}{5}$ e $h \neq \frac{18}{5}$**.

### 7. Esercizi

:::exercise Esercizio 8.3.1 — Svolgimento completo del Compito del 15/5/2026 (Lezione 14, pp. 6–8, incluso completamento)
Risolvere integralmente entrambi i quesiti del Compito del 15/5/2026, completando fino in fondo lo studio della diagonalizzabilità di $N = M(g \circ f)$ per tutti i valori reali di $h$.

:::solution Soluzione spiegata passo-passo

#### Parte (1) — Studio di $f : \mathbb{R}^3 \to \mathbb{R}^4$ associata a ${}^t M$ (`Lez14`, p. 6)

1. **Trasposta ${}^t M$ e calcolo del rango al variare di $h$:**
    $${}^t M = \begin{pmatrix} 1 & 3 & 2 \\ 1 & 4 & h-3 \\ 3 & 4 & 1 \\ 4 & h & 2 \end{pmatrix} \in \mathbb{R}^{4,3}$$
    Calcoliamo il determinante della sottomatrice $3\times 3$ formata dalle righe $1, 3, 4$:
    $$\det\begin{pmatrix} 1 & 3 & 2 \\ 3 & 4 & 1 \\ 4 & h & 2 \end{pmatrix} = 8 + 12 + 6h - 32 - h - 18 = 5h - 30 = 5(h - 6)$$
    Pertanto tale minore è nullo se e solo se $h = 6$.

2. **I caso ($h \neq 6$):**
    Poiché un minore $3\times 3$ è diverso da $0$, $\operatorname{rk} {}^t M = 3$:
    - $\dim_{\mathbb{R}} \operatorname{Im} f = 3$ (non suriettiva essendo $3 < 4$), con base data dalle $3$ colonne di ${}^t M$:
        $$\operatorname{Im} f = \mathcal{L}\bigl((1, 1, 3, 4),\ (3, 4, 4, h),\ (2, h-3, 1, 2)\bigr)$$
    - $\dim_{\mathbb{R}} \operatorname{Ker} f = 3 - 3 = 0 \implies \operatorname{Ker} f = \{(0, 0, 0)\}$ e **$f$ è iniettiva**.

3. **II caso ($h = 6$):**
    Riduciamo ${}^t M$ **per colonne** *(così da leggere simultaneamente $\operatorname{rk}$ e una base di $\operatorname{Im} f$)*:
    $${}^t M = \begin{pmatrix} 1 & 3 & 2 \\ 1 & 4 & 3 \\ 3 & 4 & 1 \\ 4 & 6 & 2 \end{pmatrix} \xrightarrow{\substack{C_2 \mapsto C_2 - 3C_1 \\ C_3 \mapsto C_3 - 2C_1}} \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 1 \\ 3 & -5 & -5 \\ 4 & -6 & -6 \end{pmatrix} \xrightarrow{C_3 \mapsto C_3 - C_2} \begin{pmatrix} \boxed{1} & 0 & 0 \\ 1 & \boxed{1} & 0 \\ 3 & -5 & 0 \\ 4 & -6 & 0 \end{pmatrix}$$
    *(Nota: nel manoscritto in basso a destra compare una lieve sbavatura sopra lo $0$ di posizione $(4,3)$, ma $C_3 - C_2 = 0$ esattamente.)*
    Dunque $\operatorname{rk} {}^t M = 2$:
    - **$\operatorname{Im} f$:** $\dim_{\mathbb{R}} \operatorname{Im} f = 2$ e $\operatorname{Im} f = \mathcal{L}\bigl((1, 1, 3, 4),\ (0, 1, -5, -6)\bigr)$ *(oppure le prime due colonne originali)*.
    - **$\operatorname{Ker} f$:** $\dim_{\mathbb{R}} \operatorname{Ker} f = 3 - 2 = 1$ (non iniettiva). Prendendo le prime due righe indipendenti $\begin{pmatrix} 1 & 3 & 2 \\ 1 & 4 & 3 \end{pmatrix}$ *(che hanno $\det\begin{pmatrix} 1 & 3 \\ 1 & 4 \end{pmatrix} = 1 \neq 0$)* e applicando i minori a segno alterno:
        $$d_1 = \det\begin{pmatrix} 3 & 2 \\ 4 & 3 \end{pmatrix} = 1, \qquad d_2 = -\det\begin{pmatrix} 1 & 2 \\ 1 & 3 \end{pmatrix} = -1, \qquad d_3 = \det\begin{pmatrix} 1 & 3 \\ 1 & 4 \end{pmatrix} = 1$$
        Pertanto $\operatorname{Ker} f = \mathcal{L}\bigl((1, -1, 1)\bigr)$.

---

#### Parte (2) — Composizione $g \circ f$ e diagonalizzabilità (`Lez14`, pp. 7–8 + completamento)

1. **Costruzione della matrice associata $M(g) \in \mathbb{R}^{3,4}$ (`Lez14`, p. 7):**
    Conosciamo già $g(e_2) = (1,1,0)$, $g(e_3) = (0,0,1)$ e $g(e_4) = (0,0,0)$. Ci manca $g(e_1) = g(1,0,0,0)$:
    $$(1,0,0,0) = a(1,1,3,4) + b(0,1,0,0) + c(0,0,1,0) + d(0,0,0,1) = (a,\ a+b,\ 3a+c,\ 4a+d)$$
    $$\implies \begin{cases} a = 1 \\ a + b = 0 \implies b = -1 \\ 3a + c = 0 \implies c = -3 \\ 4a + d = 0 \implies d = -4 \end{cases}$$
    Per linearità di $g$:
    $$g(1,0,0,0) = 1\cdot g(1,1,3,4) - 1\cdot g(0,1,0,0) - 3\cdot g(0,0,1,0) - 4\cdot g(0,0,0,1) = (2,0,0) - (1,1,0) - 3(0,0,1) - 4(0,0,0) = (1, -1, -3)$$
    Disponiamo $g(e_1), g(e_2), g(e_3), g(e_4)$ come colonne di $M(g)$:
    $$M(g) = \begin{pmatrix} 1 & 1 & 0 & 0 \\ -1 & 1 & 0 & 0 \\ -3 & 0 & 1 & 0 \end{pmatrix}$$

2. **Matrice della composizione $N = M(g \circ f) = M(g)M(f)$ e polinomio caratteristico (`Lez14`, p. 8):**
    $$N = M(g)M(f) = \begin{pmatrix} 1 & 1 & 0 & 0 \\ -1 & 1 & 0 & 0 \\ -3 & 0 & 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & 3 & 2 \\ 1 & 4 & h-3 \\ 3 & 4 & 1 \\ 4 & h & 2 \end{pmatrix} = \begin{pmatrix} 2 & 7 & h-1 \\ 0 & 1 & h-5 \\ 0 & -5 & -5 \end{pmatrix}$$
    Calcoliamo $P_N(x) = \det(N - xI)$ sviluppando con Laplace lungo la prima colonna:
    $$P_N(x) = \det\begin{pmatrix} 2-x & 7 & h-1 \\ 0 & 1-x & h-5 \\ 0 & -5 & -5-x \end{pmatrix} = (2-x)\det\begin{pmatrix} 1-x & h-5 \\ -5 & -5-x \end{pmatrix}$$
    $$= (2-x)\bigl[(1-x)(-5-x) + 5(h-5)\bigr] = (2-x)(-5 - x + 5x + x^2 + 5h - 25) = (2-x)(x^2 + 4x + 5h - 30)$$

3. **Completamento: discussione completa della diagonalizzabilità di $N$ su $\mathbb{R}$ al variare di $h$:**
    Una prima radice reale è sempre $x = 2$. Le altre due radici provengono da $x^2 + 4x + 5h - 30 = 0$, il cui discriminante ridotto vale:
    $$\frac{\Delta}{4} = 2^2 - (5h - 30) = 34 - 5h$$

    - **I caso ($h > \frac{34}{5}$):** $\frac{\Delta}{4} < 0 \implies$ due radici complesse non reali $\implies$ **$N$ non è diagonalizzabile su $\mathbb{R}$**.

    - **II caso ($h = \frac{34}{5}$, radici coincidenti in $\Delta = 0$):** il fattore quadratico diventa $x^2 + 4x + 4 = (x+2)^2$, quindi $P_N(x) = (2-x)(x+2)^2$. Gli autovalori sono $\lambda = 2$ ($m_2 = 1 = g_2$) e $\lambda = -2$ ($m_{-2} = 2$). Calcoliamo $g_{-2}$:
        $$N + 2I = \begin{pmatrix} 4 & 7 & \frac{34}{5} - 1 \\ 0 & 3 & \frac{34}{5} - 5 \\ 0 & -5 & -3 \end{pmatrix} = \begin{pmatrix} 4 & 7 & \frac{29}{5} \\ 0 & 3 & \frac{9}{5} \\ 0 & -5 & -3 \end{pmatrix}$$
        Poiché il minore $2\times 2$ delle prime due righe e prime due colonne vale $\det\begin{pmatrix} 4 & 7 \\ 0 & 3 \end{pmatrix} = 12 \neq 0$ *(mentre la riga $3$ è $-\frac{5}{3}R_2$ sulle ultime due colonne e il determinante di $N+2I$ è $0$)*, si ha $\operatorname{rk}(N + 2I) = 2$:
        $$g_{-2} = 3 - 2 = 1 < m_{-2} = 2$$
        Quindi per $h = \frac{34}{5}$, **$N$ non è diagonalizzabile**.

    - **III caso ($h = \frac{18}{5}$, quando $x = 2$ è radice multipla):** sostituiamo $x = 2$ nel fattore quadratico: $2^2 + 4(2) + 5h - 30 = 0 \iff 5h - 18 = 0 \iff h = \frac{18}{5}$. Per questo valore si ha $x^2 + 4x - 12 = (x-2)(x+6)$, dunque $P_N(x) = -(x-2)^2(x+6)$: gli autovalori sono $\lambda = 2$ ($m_2 = 2$) e $\lambda = -6$ ($m_{-6} = 1 = g_{-6}$). Calcoliamo $g_2$:
        $$N - 2I = \begin{pmatrix} 0 & 7 & \frac{18}{5} - 1 \\ 0 & -1 & \frac{18}{5} - 5 \\ 0 & -5 & -7 \end{pmatrix} = \begin{pmatrix} 0 & 7 & \frac{13}{5} \\ 0 & -1 & -\frac{7}{5} \\ 0 & -5 & -7 \end{pmatrix}$$
        Calcoliamo il minore $2\times 2$ in alto a destra: $\det\begin{pmatrix} 7 & \frac{13}{5} \\ -1 & -\frac{7}{5} \end{pmatrix} = -\frac{49}{5} + \frac{13}{5} = -\frac{36}{5} \neq 0$. Essendo la prima colonna tutta nulla, $\operatorname{rk}(N - 2I) = 2$:
        $$g_2 = 3 - 2 = 1 < m_2 = 2$$
        Quindi per $h = \frac{18}{5}$, **$N$ non è diagonalizzabile**.

    - **IV caso ($h < \frac{34}{5}$ e $h \neq \frac{18}{5}$):** $\frac{\Delta}{4} > 0$ e $x = 2$ non annulla il fattore quadratico, perciò $P_N(x)$ ammette **$3$ autovalori reali e distinti** (ciascuno con $m_\lambda = g_\lambda = 1$). Dunque **$N = M(g \circ f)$ è diagonalizzabile su $\mathbb{R}$**.
:::
:::
