<!-- section: app-a | num: Appendice A | title: Formulario compatto (definizioni, formule e teoremi principali) | kind: appendix | part: appendices -->

Questo formulario riunisce tutte le definizioni, formule operative e i teoremi essenziali del corso, nell'esatta notazione del Prof. Giuseppe Zappalà, con rimando rapido alle rispettive sezioni.

### Strutture algebriche e $\mathbb{C}$ *(Capitolo 1)*

| Concetto / Formula | Enunciato sintetico | Rif. |
| :--- | :--- | :---: |
| **Magma $\subset \dots \subset$ Gruppo abeliano** | Magma (interna) $\to$ Semigruppo (associativa) $\to$ Monoide (neutro $e$) $\to$ Gruppo (tutti invertibili) $\to$ Abeliano (commutativa) | [1.2](#sec-1-2), [1.3](#sec-1-3) |
| **Inverso di un prodotto in un monoide** | $(a * b)^{-1} = b^{-1} * a^{-1}$ | [1.2](#sec-1-2) |
| **Anello $\subset \dots \subset$ Campo** | Anello (`(A,+)` ab., `(A,·)` semigr., distrib.) $\to$ Unitario ($1$) $\to$ Corpo ($\forall a\neq 0\ \exists a^{-1}$) $\to$ Campo (`·` commut.) | [1.4](#sec-1-4) |
| **Moltiplicazione in $\mathbb{C} = \mathbb{R}^2$** | $(a,b)\cdot(c,d) = (ac-bd,\ ad+bc)$; $i = (0,1)$, $i^2 = -1$, $z = a+bi$ | [1.5](#sec-1-5) |
| **Coniugato, modulo e inverso** | $\bar{z} = a-bi$, $|z| = \sqrt{a^2+b^2}$, $z+\bar{z} = 2\operatorname{Re} z$, $z\bar{z} = |z|^2$, $z^{-1} = \frac{\bar{z}}{|z|^2}$ | [1.5](#sec-1-5) |
| **II grado e TFA** | $x^2 - (\alpha+\beta)x + \alpha\beta = 0$; $(x-z)(x-\bar{z}) = x^2 - 2(\operatorname{Re} z)x + |z|^2$; ogni polinomio reale ($\deg\ge 1$) si fattorizza in fattori lineari su $\mathbb{C}$ | [1.6](#sec-1-6) |

### Matrici, determinanti e inversa *(Capitoli 2 e 3)*

| Concetto / Formula | Enunciato sintetico | Rif. |
| :--- | :--- | :---: |
| **Prodotto riga per colonna** | $A \in K^{m,n}$, $B \in K^{n,p} \implies AB \in K^{m,p}$ con $\operatorname{ent}_{ij}(AB) = \sum_{r=1}^n \operatorname{ent}_{ir}(A)\operatorname{ent}_{rj}(B)$ ($AB \neq BA$ in gen.) | [2.2](#sec-2-2) |
| **Trasposta ${}^t A$** | $\operatorname{ent}_{ij}({}^t A) = \operatorname{ent}_{ji}(A)$; ${}^t(AB) = {}^t B\, {}^t A$; simmetrica ($A={}^t A$), antisimmetrica ($A=-{}^t A$) | [2.4](#sec-2-4) |
| **Traccia** | $\operatorname{tr} A = \sum_{r=1}^n \operatorname{ent}_{rr}(A)$; lineare e $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ | [2.5](#sec-2-5) |
| **Determinante** | $\det M = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) m_{1\sigma(1)}\cdots m_{n\sigma(n)}$; $n=2$: $m_{11}m_{22}-m_{12}m_{21}$ | [3.1](#sec-3-1), [3.2](#sec-3-2) |
| **Proprietà sulle colonne** | Multilineare; due colonne uguali (o una cl di altre) $\implies 0$; scambio cambia segno; $C_i \mapsto C_i + k C_j$ non altera $\det$ | [3.2](#sec-3-2) |
| **Binet e Laplace** | $\det(AB) = (\det A)(\det B)$; $\operatorname{cof}_{i,j}(A) = (-1)^{i+j}\det A_{(i,j)}$; I Laplace $= \det A$, II Laplace ($i\neq j$) $= 0$ | [3.3](#sec-3-3) |
| **Invertibilità e inversa** | $A_{\text{AGG}} = {}^t A_{\text{COF}}$; $A A_{\text{AGG}} = (\det A)I$; $A$ invertibile $\iff \det A \neq 0 \implies A^{-1} = (\det A)^{-1}A_{\text{AGG}}$ | [3.4](#sec-3-4) |

### Sistemi lineari e rango *(Capitolo 4)*

| Concetto / Formula | Enunciato sintetico | Rif. |
| :--- | :--- | :---: |
| **Teorema e Regola di Cramer** | $A \in K^{n,n}$ e $\det A \neq 0 \implies$ unica soluzione $\bar{X} = A^{-1}B$ con $\bar{x}_i = \frac{\det A_{(i)}}{\det A}$ | [4.1](#sec-4-1) |
| **Rango $\operatorname{rk} A$** | Ordine massimo di un minore non nullo ($\operatorname{rk} O = 0$); su matrice ridotta per righe = numero di righe non nulle | [4.2](#sec-4-2) |
| **Teorema di Rouché-Capelli** | $AX = B$ risolubile $\iff \operatorname{rk} A = \operatorname{rk}(A|B) = r$; se risolubile, $\infty^{n-r}$ soluzioni ($1$ se $n=r$) | [4.3](#sec-4-3) |

### Spazi vettoriali e applicazioni lineari *(Capitoli 5 e 6)*

| Concetto / Formula | Enunciato sintetico | Rif. |
| :--- | :--- | :---: |
| **Criterio di sottospazio** | $S \subseteq V$ sottospazio $\iff \underline{0} \in S$ e $as_1 + bs_2 \in S$ $\forall a,b \in K$, $\forall s_1,s_2 \in S$ | [5.2](#sec-5-2) |
| **Criterio di indipendenza** | $v_1,\dots,v_r$ liberi $\iff v_1 \neq \underline{0}$ e $v_i \notin \mathcal{L}(v_1,\dots,v_{i-1})$ per $2 \le i \le r$ | [5.3](#sec-5-3) |
| **Base e dimensione** | Insieme libero di generatori; per Steinitz tutte le basi hanno $|B| = \dim_K V$; $\dim_K K^{m,n} = mn$, $\dim_K K^n = n$ | [5.4](#sec-5-4), [5.5](#sec-5-5) |
| **Formula di Grassmann** | $\dim_K(U+W) = \dim_K U + \dim_K W - \dim_K(U\cap W)$ | [5.5](#sec-5-5) |
| **Kronecker & sistemi omogenei** | $\dim_K \mathcal{L}_R(A) = \dim_K \mathcal{L}_C(A) = \operatorname{rk} A$; $\dim_K\{X \mid AX=\underline{0}\} = n - \operatorname{rk} A$ | [5.6](#sec-5-6), [5.7](#sec-5-7) |
| **Teorema degli Orlati** | $\operatorname{rk} A = r \iff \exists$ minore $M$ di ordine $r$ **non nullo** e tutti i suoi orlati di ordine $r+1$ sono nulli | [5.7](#sec-5-7) |
| **Nucleo, immagine, dimensioni** | $f$ lineare $\implies f(\underline{0}_U)=\underline{0}_V$; $f$ iniettiva $\iff \operatorname{Ker} f = \{\underline{0}_U\}$; $\dim_K U = \dim_K \operatorname{Ker} f + \dim_K \operatorname{Im} f$ | [6.1](#sec-6-1), [6.2](#sec-6-2) |
| **Studio di $f_M(X)=MX$** | $\operatorname{Ker} f_M$: soluzioni di $MX=\underline{0}$; $\operatorname{Im} f_M = \mathcal{L}_C(M)$ ($\dim = \operatorname{rk} M$) | [6.3](#sec-6-3) |
| **Composizione ed endomorfismi** | $f_M \circ f_N = f_{MN}$; su $V$ fin. gen., endomorfismo iniettivo $\iff$ suriettivo $\iff$ isomorfismo | [6.4](#sec-6-4) |

### Similitudine, autovalori e diagonalizzazione *(Capitolo 7)*

| Concetto / Formula | Enunciato sintetico | Rif. |
| :--- | :--- | :---: |
| **Similitudine & Pol. caratt.** | $A = P^{-1}BP$ ($P$ invertibile); $P_A(x) = \det(A - xI)$; $A$ simile a $B \implies P_A(x) = P_B(x)$ *(non vale $\Leftarrow$!)* | [7.1](#sec-7-1), [7.2](#sec-7-2) |
| **Formule $P_A(x)$ ($n=2,3$)** | $n=2$: $x^2 - (\operatorname{tr} A)x + \det A$; $n=3$: $-x^3 + (\operatorname{tr} A)x^2 - (t_2 A)x + \det A$ | [7.2](#sec-7-2) |
| **Autospazio e molteplicità** | $V_\lambda = \operatorname{Ker}(f_A - \lambda \operatorname{id})$; $1 \le g_\lambda = n - \operatorname{rk}(A - \lambda I) \le m_\lambda$ | [7.3](#sec-7-3) |
| **Criterio di diagonalizzabilità** | $A$ diagonalizzabile (*semplice*) $\iff$ tutte le radici di $P_A(x)$ stanno in $K$ **e** $g_\lambda = m_\lambda\ \forall\lambda$; $P^{-1}AP = D$ ($P$ ha autovettori per colonna) | [7.4](#sec-7-4) |

<!-- section: app-b | num: Appendice B | title: Errori più comuni e trappole d'esame | kind: appendix | part: appendices -->

Questa raccolta condensa tutte le trappole ricorrenti segnalate nelle lezioni del corso, nello schema diretto *Sbagliato $\to$ Correzione*.

### Capitolo 1 — Strutture algebriche e $\mathbb{C}$

1. **$(a*b)^{-1} = a^{-1}*b^{-1}$** *(Sbagliato)* $\to$ **$(a*b)^{-1} = b^{-1}*a^{-1}$** *(Correzione)*: in un monoide o nelle matrici l'ordine si inverte sempre ([1.2](#sec-1-2)).
2. **$a*e = a$ da un solo lato / togliere $0$ dimenticato** *(Sbagliato)* $\to$ verificare sempre **entrambi** i lati quando $*$ non è commutativa; ricordare che $(\mathbb{R},\times)$ non è gruppo perché $0$ non è invertibile, serve $\mathbb{R}\setminus\{0\}$ ([1.2](#sec-1-2), [1.3](#sec-1-3)).
3. **$\operatorname{Im}(2+3i) = 3i$ oppure $|a+bi| = \sqrt{a^2+(bi)^2}$** *(Sbagliato)* $\to$ $\operatorname{Im} z = 3 \in \mathbb{R}$ (senza la $i$) e $|z| = \sqrt{a^2+b^2} \in \mathbb{R}_0^+$ ([1.5](#sec-1-5)).

### Capitolo 2 — Matrici

4. **Usare $\operatorname{ent}_{ji}$ o regole commutative $(A+B)^2 = A^2+2AB+B^2$** *(Sbagliato)* $\to$ in $\operatorname{ent}_{ij}(A)$ il primo indice è sempre la **riga**, e $(A+B)^2 = A^2 + AB + BA + B^2$ perché in generale $AB \neq BA$ ([2.1](#sec-2-1), [2.2](#sec-2-2)).
5. **Da $BA = O$ dedurre $B=O$ o $A=O$, oppure dimenticare l'inversione in ${}^t(AB)$** *(Sbagliato)* $\to$ esistono divisori dello zero per $n \ge 2$ ([2.3](#sec-2-3)); vale sempre ${}^t(AB) = {}^t B\,{}^t A$ ([2.4](#sec-2-4)) e $\operatorname{tr}(AB) = \operatorname{tr}(BA) \neq (\operatorname{tr} A)(\operatorname{tr} B)$ ([2.5](#sec-2-5)).

### Capitolo 3 — Determinanti e matrice inversa

6. **$\det(kA) = k\det A$ o $\det(A+B) = \det A + \det B$** *(Sbagliato)* $\to$ il determinante è multilineare colonna per colonna: $\det(kA) = k^n \det A$ per $A \in K^{n,n}$, mentre per somme in generale $\det(A+B) \neq \det A + \det B$ ([3.2](#sec-3-2), [3.3](#sec-3-3)).
7. **Dimenticare $(-1)^{i+j}$ in $A_{\text{COF}}$ o la trasposizione in $A_{\text{AGG}}$** *(Sbagliato)* $\to$ scrivere la scacchiera dei segni sui cofattori e ricordare sempre $A^{-1} = (\det A)^{-1}\,{}^t A_{\text{COF}}$ ([3.3](#sec-3-3), [3.4](#sec-3-4)).

### Capitolo 4 — Sistemi lineari e rango

8. **Scrivere $X = B A^{-1}$ o sostituire la riga $i$ in Cramer** *(Sbagliato)* $\to$ per Cramer l'ordine è $X = A^{-1}B$ e $A_{(i)}$ rimpiazza la **colonna** $i$ con $B$; inoltre $\det A = 0$ non implica automaticamente "impossibile" (può avere $\infty^{n-r}$ soluzioni!) ([4.1](#sec-4-1)).
9. **Contare le righe di $A|B$ senza controllare $(0\dots 0\mid 1)$** *(Sbagliato)* $\to$ prima verifica sempre Rouché-Capelli ($\operatorname{rk} A = \operatorname{rk}(A|B)$), riducendo la matrice completa $A|B$ in un solo passaggio ([4.3](#sec-4-3)).

### Capitolo 5 — Spazi vettoriali

10. **Fermarsi a $\underline{0} \in S$ o scartare i vettori iniziali $L$ nel prolungamento** *(Sbagliato)* $\to$ per i sottospazi occorre sempre anche la chiusura $as_1+bs_2 \in S$ ([5.2](#sec-5-2)); nel prolungamento $L$ va sempre messo **in testa** prima dei generatori $\mathcal{E}$ ([5.4](#sec-5-4)).
11. **Omettere "non nullo" negli Orlati o il segno meno in $d_2$** *(Sbagliato)* $\to$ il minore iniziale $M$ di ordine $r$ deve essere $M \neq 0$, e i minori a segno alterno hanno segni **$+,\ -,\ +$** ([5.7](#sec-5-7)).

### Capitolo 6 — Applicazioni lineari

12. **Prendere colonne dopo riduzione per righe per $\operatorname{Im} f_M$ o invertire $M(g \circ f)$** *(Sbagliato)* $\to$ per una base di $\operatorname{Im} f_M$ riduci **per colonne** oppure prendi le **colonne originali** di $M$ in corrispondenza dei pivot ([6.3](#sec-6-3)); nella composizione l'ordine matriciale è sempre $M(g \circ f) = M(g)M(f)$ ([6.4](#sec-6-4)).
13. **Mettere direttamente $f(u_i)$ come colonne di $M(f)$ quando $u_i \neq e_i$** *(Sbagliato)* $\to$ le colonne di $M(f)$ sono esclusivamente le immagini della **base canonica** $f(e_1),\dots,f(e_n)$, ricavate per linearità esprimendo gli $e_j$ sugli $u_i$ ([6.5](#sec-6-5)).

### Capitoli 7 e 8 — Autovalori e diagonalizzazione

14. **Credere $P_A = P_B \implies A$ simile a $B$, o ammettere $\underline{0}$ come autovettore** *(Sbagliato)* $\to$ il viceversa non vale (es. $O$ vs $\begin{pmatrix}0&1\\0&0\end{pmatrix}$); gli autovettori hanno per definizione $v \neq \underline{0}$ ([7.2](#sec-7-2), [7.3](#sec-7-3)).
15. **Dimenticare radici non reali o valori di coincidenza tra radice lineare e fattore quadratico** *(Sbagliato)* $\to$ su $\mathbb{R}$, $\Delta < 0$ blocca subito la diagonalizzabilità; quando $P_A(x) = (c-x)(x^2+\dots)$, oltre a $\Delta = 0$ controlla **sempre** anche il valore di $h$ che rende $x = c$ radice del secondo fattore ([7.4](#sec-7-4), [8.1](#sec-8-1), [8.3](#sec-8-3)).

<!-- section: app-c | num: Appendice C | title: Glossario alfabetico dei termini del corso | kind: appendix | part: appendices -->

| Termine / Simbolo | Definizione sintetica | Rif. |
| :--- | :--- | :---: |
| **Anello / Anello unitario** | Struttura $(A,+,\cdot)$ con $(A,+)$ gruppo abeliano, $(A,\cdot)$ semigruppo e distributività; unitario se possiede $1$ | [1.4](#sec-1-4) |
| **Applicazione lineare** | Funzione $f:U\to V$ tra $K$-spazi vettoriali tale che $f(a_1 u_1 + a_2 u_2) = a_1 f(u_1) + a_2 f(u_2)$ | [6.1](#sec-6-1) |
| **Autospazio ($V_\lambda$)** | Sottospazio $\operatorname{Ker}(f_A - \lambda \operatorname{id}) = \{v \in K^n \mid f_A(v) = \lambda v\}$ | [7.3](#sec-7-3) |
| **Autovalore / Autovettore** | Scalare $\lambda \in K$ e vettore $v \neq \underline{0}$ tali che $f_A(v) = \lambda v$ | [7.3](#sec-7-3) |
| **Base ($\mathcal{B}$)** | Sottoinsieme libero (linearmente indipendente) e insieme di generatori dello spazio vettoriale $V$ | [5.4](#sec-5-4) |
| **Campo $(K,+,\cdot)$** | Corpo con moltiplicazione commutativa ($\mathbb{Q}, \mathbb{R}, \mathbb{C}$) | [1.4](#sec-1-4) |
| **Cofattore ($\operatorname{cof}_{i,j}(A)$)** | Scalare $(-1)^{i+j}\det A_{(i,j)}$, dove $A_{(i,j)}$ elimina riga $i$ e colonna $j$ | [3.3](#sec-3-3) |
| **Combinazione lineare** | Vettore della forma $\sum_{i=1}^r a_i v_i$ (o matrice $aM + bN$) con $a_i \in K$ | [3.2](#sec-3-2), [5.3](#sec-5-3) |
| **Componenti rispetto a $\mathcal{B}$** | Unica $n$-upla $(a_1,\dots,a_n) \in K^n$ tale che $v = \sum_{i=1}^n a_i v_i$ | [6.5](#sec-6-5) |
| **Coniugato ($\bar{z}$) e Modulo ($|z|$)** | Per $z=a+bi$: $\bar{z}=a-bi$ e $|z|=\sqrt{a^2+b^2}$ | [1.5](#sec-1-5) |
| **Controimmagine ($f^{-1}(Z)$)** | $\{u \in U \mid f(u) \in Z\}$; definita per ogni funzione $f:U\to V$ e $Z \subseteq V$ | [6.1](#sec-6-1), [6.3](#sec-6-3) |
| **Corpo** | Anello unitario in cui ogni elemento $\neq 0$ ha inverso moltiplicativo | [1.4](#sec-1-4) |
| **Determinante ($\det M$)** | $\sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) m_{1\sigma(1)}\cdots m_{n\sigma(n)}$ per $M \in K^{n,n}$ | [3.1](#sec-3-1) |
| **Diagonalizzabile / Semplice** | Matrice quadrata (o endomorfismo) simile a una matrice diagonale | [7.3](#sec-7-3), [7.4](#sec-7-4) |
| **Dimensione ($\dim_K V$)** | Cardinalità comune di tutte le basi di uno spazio finitamente generato | [5.5](#sec-5-5) |
| **Elemento neutro ($e$) / Inverso ($a^{-1}$)** | $a*e=e*a=a$; $a*b=b*a=e$ in un monoide | [1.2](#sec-1-2) |
| **Elemento speciale** | Elemento $\neq 0$ in una riga di matrice ridotta con soli zeri al di sotto nella propria colonna | [4.2](#sec-4-2) |
| **Endomorfismo** | Applicazione lineare $f:V\to V$ di uno spazio vettoriale in se stesso | [6.4](#sec-6-4) |
| **Finitamente generato** | Spazio generato da un sottoinsieme finito ($V=\mathcal{L}(S)$ con $|S|<\infty$) | [5.3](#sec-5-3) |
| **Gruppo / Gruppo abeliano** | Monoide in cui ogni elemento è invertibile; abeliano se anche commutativo | [1.3](#sec-1-3) |
| **Immagine ($\operatorname{Im} f$)** | Sottospazio $f(U) \subseteq V$ costituito da tutti i valori assunti da $f$ | [6.2](#sec-6-2) |
| **Insieme libero / Lin. indipendenti** | Vettori tali che $\sum a_i v_i = \underline{0} \implies a_1=\dots=a_r=0$ | [5.3](#sec-5-3) |
| **Isomorfismo** | Applicazione lineare biettiva (sia iniettiva che suriettiva) | [6.4](#sec-6-4) |
| **Magma** | Insieme $A$ dotato di un'operazione binaria interna $*$ | [1.2](#sec-1-2) |
| **Matrice aggiunta ($A_{\text{AGG}}$)** | Trasposta della matrice dei cofattori: $A_{\text{AGG}} = {}^t A_{\text{COF}}$ | [3.4](#sec-3-4) |
| **Matrice completa ($A|B$)** | Matrice in $K^{m,n+1}$ ottenuta affiancando $B$ ad $A$ in $AX=B$ | [4.3](#sec-4-3) |
| **Matrice diagonale / scalare** | Diagonale: $\operatorname{ent}_{ij}=0$ per $i\neq j$; scalare: $hI$ ($h \in K$) | [2.5](#sec-2-5) |
| **Matrice identica ($I$)** | Matrice quadrata con $1$ sulla diagonale e $0$ altrove | [2.3](#sec-2-3) |
| **Matrice simmetrica / antisimmetrica** | Simmetrica se $A={}^t A$; antisimmetrica se $A=-{}^t A$ | [2.4](#sec-2-4) |
| **Matrice trasposta (${}^t A$)** | Matrice in $K^{n,m}$ con righe e colonne scambiate rispetto ad $A \in K^{m,n}$ | [2.4](#sec-2-4) |
| **Minore di ordine $r$ / Orlato** | Determinante di sottomatrice quadrata $r\times r$; orlato = minore $(r+1)\times(r+1)$ che lo contiene | [4.2](#sec-4-2), [5.7](#sec-5-7) |
| **Molteplicità algebrica ($m_\lambda$) / geometrica ($g_\lambda$)** | $m_\lambda$ = molteplicità di $\lambda$ come radice di $P_A(x)$; $g_\lambda = \dim_K V_\lambda$ | [7.3](#sec-7-3) |
| **Monoide / Semigruppo** | Semigruppo: magma associativo; monoide: semigruppo con elemento neutro | [1.2](#sec-1-2) |
| **Nucleo ($\operatorname{Ker} f$)** | Sottospazio $f^{-1}(\{\underline{0}_V\}) = \{u\in U \mid f(u)=\underline{0}_V\}$ | [6.2](#sec-6-2) |
| **Operazione binaria interna** | Funzione $A \times A \to A$ | [1.1](#sec-1-1) |
| **Permutazione ($S_n$) / Segno ($\operatorname{sgn}$)** | Funzione biettiva su $\{1,\dots,n\}$; segno $=+1$ se pari, $-1$ se dispari | [3.1](#sec-3-1) |
| **Polinomio caratteristico ($P_A(x)$)** | $P_A(x) = \det(A - xI)$ per $A \in K^{n,n}$ | [7.2](#sec-7-2) |
| **Rango ($\operatorname{rk} A$)** | Ordine massimo di un minore non nullo di $A$ | [4.2](#sec-4-2) |
| **Similitudine** | $A$ simile a $B$ se $\exists P$ invertibile tale che $A = P^{-1}BP$ | [7.1](#sec-7-1) |
| **Sistema di Cramer** | Sistema $AX=B$ con $A$ quadrata e $\det A \neq 0$ | [4.1](#sec-4-1) |
| **Sottospazio generato ($\mathcal{L}(S)$)** | Insieme di tutte le combinazioni lineari di vettori di $S \neq \emptyset$ | [5.3](#sec-5-3) |
| **Spazio delle righe / colonne** | $\mathcal{L}_R(A) \subseteq K^n$, $\mathcal{L}_C(A) \subseteq K^m$ | [5.6](#sec-5-6) |
| **Traccia ($\operatorname{tr} A$)** | Somma degli elementi sulla diagonale principale di $A \in K^{n,n}$ | [2.5](#sec-2-5) |

<!-- section: app-d | num: Appendice D | title: Tabella completa file delle lezioni -> sezione | kind: appendix | part: appendices -->

### Mappatura completa dei 15 PDF del corso (`Lez00`–`Lez14`, 130 pagine totali)

| File delle lezioni | Data | Pag. | Contenuto originale | Sezioni della dispensa |
| :--- | :---: | :---: | :--- | :--- |
| `Lez00_ALinGe_inf_(F-N)_2026.pdf` | — | 2 | Programma ufficiale, contatti docente, modalità d'esame | [Introduzione](#intro), [Appendice E](#app-e) |
| `Lez01_ALinGe_inf_(F-N)_2026.pdf` | *n.d.* | 8 | Insiemi, $A \times B$, operazioni, magma/semigruppo/monoide (pp. 1–5); gruppi e gruppi abeliani (pp. 5–6); anelli e anelli unitari (pp. 7–8) | [1.1](#sec-1-1), [1.2](#sec-1-2), [1.3](#sec-1-3), [1.4](#sec-1-4) |
| `Lez02_ALinGe_inf_(F-N)_2026.pdf` | 7/10/2026 | 8 | Corpi e campi (p. 1); $\mathbb{C} = \mathbb{R}^2$, forma algebrica, $\bar{z}, |z|, z^{-1}$ (pp. 2–6); II grado, TFA e fattorizzazione polinomi (pp. 6–8) | [1.4](#sec-1-4), [1.5](#sec-1-5), [1.6](#sec-1-6) |
| `Lez03_ALinGe_inf_(F-N)_2026.pdf` | 12/10/2026 | 11 | $K^{m,n}$, $(K^{m,n},+)$ (pp. 1–3); scalare $\cdot$ matrice, prodotto riga per colonna (pp. 3–6); matrici quadrate e $I$ (pp. 6–7); trasposta, simmetriche/antisimmetriche (pp. 7–8); triangolari, diagonali, scalari, $\operatorname{tr} A$ (pp. 9–11) | [2.1](#sec-2-1), [2.2](#sec-2-2), [2.3](#sec-2-3), [2.4](#sec-2-4), [2.5](#sec-2-5) |
| `Lez04_ALinGe_inf_(F-N)_2026.pdf` | 14/10/2026 | 6 | Permutazioni $S_n$, segno, $p_\sigma$, $\det M$ (pp. 1–2); calcolo per $n=1,2,3$ e proprietà sulle colonne con dimostrazioni (pp. 2–6) | [3.1](#sec-3-1), [3.2](#sec-3-2) |
| `Lez05_ALinGe_inf_(F-N)_2026.pdf` | 19/10/2026 | 11 | Binet, cofattori, I e II Laplace (pp. 1–3); $A_{\text{COF}}$, $A_{\text{AGG}}$, $\det A \neq 0 \iff$ inv. (pp. 3–6); sistemi $AX=B$, Teorema e Regola di Cramer (pp. 7–11) | [3.3](#sec-3-3), [3.4](#sec-3-4), [4.1](#sec-4-1) |
| `Lez06_ALinGe_inf_(F-N)_2026.pdf` | 21/10/2026 | 5 | Sottomatrici, minori, $\operatorname{rk} A$, ridotte per righe, riduzione (pp. 1–4); $A|B$, Rouché-Capelli e $\infty^{n-r}$ soluzioni (pp. 4–5) | [4.2](#sec-4-2), [4.3](#sec-4-3) |
| `Lez07_ALinGe_inf_(F-N)_2026.pdf` | 26/10/2026 | 11 | Sistemi parametrici e riepilogo in 4 passi (pp. 1–5); $K$-spazi vettoriali e legge di annullamento (pp. 6–7); sottospazi, $AX=\underline{0}$, $U \cap W$ (pp. 8–11) | [4.3](#sec-4-3), [5.1](#sec-5-1), [5.2](#sec-5-2) |
| `Lez08_ALinGe_inf_(F-N)_2026.pdf` | 28/10/2026 | 9 | Somma $U+W$ (p. 1); combinazioni lineari, $\mathcal{L}(S)$, generatori, dipendenza/indipendenza lineare (pp. 1–6); basi, $\mathcal{E}$, scarti successivi, prolungamento (pp. 6–9) | [5.2](#sec-5-2), [5.3](#sec-5-3), [5.4](#sec-5-4) |
| `Lez09_ALinGe_inf_(F-N)_2026.pdf` | 4/11/2026 | 9 | Lemma di Steinitz, $\dim_K V$, Grassmann (pp. 1–3); $\mathcal{L}_R, \mathcal{L}_C$, Kronecker e dimostrazione di Rouché-Capelli (pp. 4–5); sistemi omogenei, $d_1,d_2,d_3$, Teorema degli Orlati (pp. 5–9) | [5.5](#sec-5-5), [5.6](#sec-5-6), [5.7](#sec-5-7) |
| `Lez10_ALinGe_inf_(F-N)_2026.pdf` | 9/11/2026 | 11 | Esercizio completo $U+W, U\cap W$ e casa $\mathbb{R}^5$ (pp. 1–3); applicazioni lineari, $f(W), f^{-1}(Z)$ (pp. 3–5); $\operatorname{Im} f, \operatorname{Ker} f$, Teorema sulle dimensioni (pp. 5–6); applicazioni $f_M$ (pp. 6–11) | [5.5](#sec-5-5), [6.1](#sec-6-1), [6.2](#sec-6-2), [6.3](#sec-6-3) |
| `Lez11_ALinGe_inf_(F-N)_2026.pdf` | 16/11/2026 | 10 | Isomorfismi, $f^{-1}$, corollario dimensioni (pp. 1–2); studio e controimmagini $f_M^{-1}(\{v\})$ (pp. 2–6); composizione $f_{MN}$, endomorfismi (pp. 6–8); componenti e cambio base (pp. 8–10) | [6.2](#sec-6-2), [6.3](#sec-6-3), [6.4](#sec-6-4), [6.5](#sec-6-5) |
| `Lez12_ALinGe_inf_(F-N)_2026.pdf` | 18/11/2026 | 8 | Esistenza/unicità di $f$ su una base (pp. 1–2); similitudine (pp. 3–4); $P_A(x)$ e invarianza (pp. 4–6); diagonalizzabilità, autovalori e autovettori (pp. 7–8) | [6.5](#sec-6-5), [7.1](#sec-7-1), [7.2](#sec-7-2), [7.3](#sec-7-3) |
| `Lez13_ALinGe_inf_(F-N)_2026.pdf` | 23/11/2026 | 13 | $m_\lambda$, $V_\lambda$, $g_\lambda$, $g_\lambda \le m_\lambda$ (pp. 1–4); Teorema sulla diagonalizzabilità ed esercizi (pp. 4–10); Compito 26/1/2026 parte 1 (pp. 10–13) | [7.3](#sec-7-3), [7.4](#sec-7-4), [8.1](#sec-8-1) |
| `Lez14_ALinGe_inf_(F-N)_2026.pdf` | 25/11/2026 | 8 | Compito 26/1/2026 parte 2 (pp. 1–2); Compito 16/2/2026 con *semplicità* (pp. 3–5); Compito 15/5/2026 (pp. 6–8) | [7.4](#sec-7-4), [8.1](#sec-8-1), [8.2](#sec-8-2), [8.3](#sec-8-3) |

### Inventario completo degli *Esercizi per casa* e dei *Completamenti* risolti

- **Tutti gli *Esercizi per casa* originali (18 quesiti distribuiti tra `Lez02` e `Lez12`, risolti integralmente):**
    1. `Lez02`, p. 6 ($\times 2$): $(1+5i)^{-1}$ e $(1+i)^4$ $\to$ [1.5](#sec-1-5)
    2. `Lez02`, p. 8: fattorizzazione di $x^3 - 1$ su $\mathbb{C}$ $\to$ [1.6](#sec-1-6)
    3. `Lez03`, p. 5: calcolo di $AB$ e $BA$ $\to$ [2.2](#sec-2-2)
    4. `Lez03`, p. 11: verifica $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ $\to$ [2.5](#sec-2-5)
    5. `Lez04`, p. 3: formula esplicita di $\det M$ per $n = 4$ ($|S_4| = 24$) $\to$ [3.2](#sec-3-2)
    6. `Lez05`, p. 1: verifica del Teorema di Binet $\to$ [3.3](#sec-3-3)
    7. `Lez05`, p. 6: calcolo di $A^{-1}$ per matrice triangolare $3\times 3$ parametrica $\to$ [3.4](#sec-3-4)
    8. `Lez05`, p. 10: sistema lineare $3\times 3$ parametrico di Cramer $\to$ [4.1](#sec-4-1)
    9. `Lez07`, p. 5: sistema $4 \times 3$ parametrico con Rouché-Capelli $\to$ [4.3](#sec-4-3)
    10. `Lez08`, p. 9: indipendenza e prolungamento a base di $\mathbb{R}^4$ $\to$ [5.4](#sec-5-4)
    11. `Lez09`, p. 8: dimensione e base di $W \subseteq \mathbb{R}^3$ al variare di $h$ $\to$ [5.7](#sec-5-7)
    12. `Lez09`, p. 9: equazioni minimali in $\mathbb{R}^5$ con Teorema degli Orlati $\to$ [5.7](#sec-5-7)
    13. `Lez10`, p. 3: calcolo di $U+W$ e $U\cap W$ in $\mathbb{R}^5$ $\to$ [5.5](#sec-5-5)
    14. `Lez10`, p. 11 ($\times 2$): studio parametrico di $f_M : \mathbb{R}^4 \to \mathbb{R}^3$ e $f_M : \mathbb{R}^3 \to \mathbb{R}^3$ $\to$ [6.3](#sec-6-3)
    15. `Lez11`, p. 7: studio di $g \circ f : \mathbb{R}^3 \to \mathbb{R}^3$ $\to$ [6.4](#sec-6-4)
    16. `Lez12`, p. 2: matrice $A \in \mathbb{R}^{4,3}$ e legge di $f$ assegnata su una base $\to$ [6.5](#sec-6-5)
- **3 Esercizi lasciati da completare dal prof a fine lezione (completati integralmente):**
    1. `Lez07`, p. 5 (soluzioni esplicite per $h \neq 2, -7$ e $h = -7$) $\to$ [4.3](#sec-4-3)
    2. `Lez13`, p. 13 (vettore unico $(-\frac{1}{3}, -\frac{2}{3}, 0)$ nella controimmagine per $h = -2$) $\to$ [8.1](#sec-8-1)
    3. `Lez14`, p. 8 (discussione completa di diagonalizzabilità di $N = M(g\circ f)$ per ogni $h \in \mathbb{R}$) $\to$ [8.3](#sec-8-3)

### Registro completo di refusi, lacune grafiche e contrasti negli appunti originali

| Fonte | Problema rilevato nei PDF | Correzione adottata | Sez. |
| :--- | :--- | :--- | :---: |
| `Lez02`, pp. 3, 7 | Div. per $b$ implicita ($b\neq 0$); manca $\deg P \ge 1$ nel TFA | Caso $b=0$ distinto; ipotesi esplicitata | [1.5](#sec-1-5), [1.6](#sec-1-6) |
| `Lez03`, pp. 3, 5, 10 | $2\cdot 5 = 8$ invece di $10$; $B=\mathbb{R}^{3,2}$; «o» invece di «e» nello schema | $10$, $B\in\mathbb{R}^{3,2}$, «triang. sup. e inf.» | [2.2](#sec-2-2), [2.5](#sec-2-5) |
| `Lez04`, pp. 2–3 | Righe invisibili nell'export PDF ($\sum \operatorname{sgn} p_\sigma$, $n=1$, $n=2$) | Formule ricostruite fedelmente | [3.1](#sec-3-1) |
| `Lez05`, p. 6 | Denominatore $(2,1)$ scritto $h-1$ anziché $h-6$ in $A^{-1}$ | Corretto in $\frac{-3}{h-6}$ | [3.4](#sec-3-4) |
| `Lez06`, pp. 1, 3 | Non esplicita $\operatorname{rk} O = 0$; riquadro `49-6` invece di `49-66` | Chiarito $\operatorname{rk} O = 0$ e $49-66 = -17$ | [4.2](#sec-4-2) |
| `Lez07`, pp. 3, 10–11 | Manca `z` in 3ª eq. (`x+3y+h=-4`); $av_1+bv_2\in V$; $(x,y,z)\in\mathbb{R}$ | Ripristinati $hz$, $\in U$, $\in \mathbb{R}^3$ | [4.3](#sec-4-3), [5.2](#sec-5-2) |
| `Lez09`, pp. 3, 8, 9 | $\dim_K$ invece di $\dim_{\mathbb{R}}$; manca **«non nullo»** negli Orlati; Eserc. 5 scrive $\mathbb{R}^5$ per $\mathbb{R}^4$ | Aggiunto «non nullo» e corretto $\mathbb{R}^4$ | [5.5](#sec-5-5), [5.7](#sec-5-7) |
| `Lez10`, p. 6; `Lez11`, pp. 3, 7–9 | Ipotesi fin. gen. sottintesa; $e_1 = f_M^{-1}(\dots)$; $\dim_f$; **contrasto riga/colonna** nel cambio base | Segnalato contrasto: esercizi usano colonne | [6.2](#sec-6-2)–[6.5](#sec-6-5) |
| `Lez13`, pp. 4–6, 8, 10, 12 | $A=P^{-1}DP$ vs $P^{-1}AP=D$; $V_0$ invece di $V_3$; `-3` nel $1^\circ$ minore; `-4` vs `-2` e `h` vs `1` in Compito 26/1 | Segnalate tutte le sviste nei box Nota | [7.4](#sec-7-4), [8.1](#sec-8-1) |

<!-- section: app-e | num: Appendice E | title: Argomenti del programma non coperti dalle lezioni | kind: appendix | part: appendices -->

Nella prima pagina del materiale introduttivo (`Lez00_ALinGe_inf_(F-N)_2026.pdf`, p. 1), il Prof. Giuseppe Zappalà presenta il programma completo del corso annuale suddiviso in due moduli principali: **Algebra Lineare** e **Geometria**.

### 1. Confronto tra programma ufficiale (`Lez00`) e PDF disponibili (`Lez01`–`Lez14`)

- **Algebra Lineare (7 argomenti — COPERTO AL 100%):**
    Tutti e sette i punti elencati in `Lez00` sono trattati interamente nei 14 fascicoli delle lezioni `Lez01`–`Lez14` e sviluppati nei Capitoli 1–8 di questa dispensa:
    1. *Strutture algebriche* $\to$ [Capitolo 1](#sec-1-1)
    2. *Matrici* $\to$ [Capitolo 2](#sec-2-1)
    3. *Determinanti* $\to$ [Capitolo 3](#sec-3-1)
    4. *Sistemi lineari* $\to$ [Capitolo 4](#sec-4-1)
    5. *Spazi vettoriali* $\to$ [Capitolo 5](#sec-5-1)
    6. *Applicazioni lineari* $\to$ [Capitolo 6](#sec-6-1)
    7. *Diagonalizzazione degli endomorfismi* $\to$ [Capitolo 7](#sec-7-1) e [Capitolo 8](#sec-8-1)

- **Ordine effettivo di svolgimento:**
    In `Lez00` p. 1 *Spazi vettoriali* compare prima di *Sistemi lineari*, ma nella didattica reale il docente tratta prima *Sistemi lineari e rango* (`Lez05`–`Lez07`, pp. 7–5) e subito dopo *Spazi vettoriali* (`Lez07`–`Lez09`). La dispensa rispetta l'ordine effettivo delle lezioni.

### 2. Elenco degli argomenti del programma NON presenti nei 15 PDF

L'intero secondo modulo indicato nel programma di `Lez00`, p. 1 — **Geometria** — non compare nei 15 file PDF forniti (`/home/alessandro/Downloads/Lezioni_2026/` si conclude al termine dell'Algebra Lineare il 25/11/2026 con `Lez14`):

1. **Geometria lineare sul piano** *(rette nel piano, posizioni reciproche, parallelismo e perpendicolarità, distanze, fasci — non presente nei PDF)*;
2. **Geometria lineare nello spazio** *(piani e rette nello spazio, condizioni di incidenza/parallelismo/ortogonalità — non presente nei PDF)*;
3. **Coniche** *(equazioni canoniche e classificazione di ellisse, parabola, iperbole — non presente nei PDF)*.

:::note Politica di trasparenza della dispensa
In coerenza con la scelta di basare questa risorsa **rigorosamente ed esclusivamente sui 15 PDF ufficiali del corso**, i tre argomenti di *Geometria* non sono stati integrati da fonti esterne. Se il docente fornirà in seguito le lezioni relative alla parte di Geometria, sarà possibile aggiungerle come Capitolo 9 senza toccare l'impianto dei Capitoli 1–8.
:::
