# d=4 complementary-support leakage: an exact Hadamard-coupling lemma

Status: **new exact partial theorem, not a proof of the classical upper
bound**.  This note records (i) the exact spectral cancellation required by
the archived equality witness and (ii) a finite exact proof that the top
rank-four and bottom rank-sixteen eigenspaces cannot have disjoint coordinate
supports.  The resulting quantitative inequality is universal for
complementary ternary supports, but its present constants do not close
`GROTHD4.classical.spectral-gap`.

The companion exact checker is
`grothendieck-d4/tools/h4_complementary_leakage_checker.py`.  Its canonical
claim records remain author-level and await independent review.

## 1. Setup

Let $A$ be the frozen $300\times300$ integer Bell matrix.  Write

\[
 \lambda=5132744330206382+2356560241063596\sqrt5
\]

for its largest eigenvalue, let $E=P/75$ be the corresponding rank-four
orthogonal projector, and let $F$ be the rank-sixteen projector for the
most-negative eigenvalue $-\rho$, where

\[
 \rho=\frac{a+\sqrt D}{2},\qquad
 a=6416438611362062,
\]

\[
 D=27825235685041889271593617164468.
\]

For signs $x,y\in\{\pm1\}^{300}$, put

\[
 p=\frac{x+y}{2},\qquad q=\frac{x-y}{2}.
\]

Then $p,q\in\{-1,0,1\}^{300}$, their supports are complementary, and

\[
 p_iq_i=0,qquad p_i^2+q_i^2=1,qquad
 x^TAy=p^TAp-q^TAq.                                      \tag{1.1}
\]

This form exposes the required joint restriction: $p$ wants to concentrate
in $E$, while $q$ wants to concentrate in $F$, but the coordinatewise
constraint $p\circ q=0$ couples those two optimizations.

## 2. Exact ledger for the archived witness

For the archived equality witness, the checker proves

\[
 |\operatorname{supp}p|=217,\qquad
 |\operatorname{supp}q|=83,                               \tag{2.1}
\]

and

\[
 p^TEp=\frac{2173+966\sqrt5}{25}
       \simeq173.3216666505919,
\]

\[
 q^TEq=\frac{9-\sqrt5}{25}
       \simeq0.2705572809000.                              \tag{2.2}
\]

The bottom eigenspace values can also be recovered without a floating-point
eigendecomposition.  Let $Q$ be the rational spectral projector onto both
roots of

\[
 f_4(t)=t^2+at+b,qquad
 b=3336362192084004310572308931844.
\]

The exact Krylov computation gives

\[
 (p^TQp,p^TAQp)
 =\left(\frac{308}{25},-\frac{1544279284652142236}{25}\right),
\]

\[
 (q^TQq,q^TAQq)
 =\left(\frac{4636}{75},-\frac{26246003593099047412}{75}\right). \tag{2.3}
\]

If $(q_0,q_1)=(z^TQz,z^TAQz)$, solving the two-root spectral system gives
the exact formula

\[
 \rho z^TFz=-\frac{q_1}{2}
 -\frac{2bq_0+aq_1}{2D}\sqrt D.                            \tag{2.4}
\]

In particular,

\[
 p^TFp\simeq10.3772635385104,qquad
 q^TFq\simeq59.6530261026690,                              \tag{2.5}
\]

where the displayed decimals are only annotations; (2.3)--(2.4) are the
certificate.

Let

\[
 C=2081044153087351400
\]

be the archived classical value.  The two favorable primary contributions
overshoot $C$ by

\[
 \Delta_{\rm dom}
 =\lambda p^TEp+\rho q^TFq-C,
\]

with the exact isolating interval

\[
 70591592261534099<\Delta_{\rm dom}
                  <70591592261534100.                     \tag{2.6}
\]

Putting the same two projectors on the opposite supports cancels

\[
 \Delta_{\rm opp}=\rho p^TFp+\lambda q^TEq,
\]

where

\[
 63476762038688220<\Delta_{\rm opp}
                  <63476762038688221.                     \tag{2.7}
\]

Thus the other ten spectral blocks must supply the additional exact net
correction

\[
 7114830222845879
 <\Delta_{\rm dom}-\Delta_{\rm opp}
 <7114830222845880.                                       \tag{2.8}
\]

The opposite-support primary terms already account for approximately
$89.92\%$ of the favorable overshoot.  Consequently, an argument which
controls only $p^TEp$ and $q^TFq$ independently misses the main mechanism:
the equality witness uses a large *joint* primary cancellation and still
needs a non-negligible ten-block correction.

## 3. No zero divisors for the $E$-$F$ Hadamard coupling

### Theorem 3.1 (proved exactly)

For every nonzero $e\in\operatorname{range}(E)$ and every nonzero
$f\in\operatorname{range}(F)$,

\[
                         e\circ f\ne0.                     \tag{3.1}
\]

In fact, the same conclusion holds when $f$ is a nonzero eigenvector of
$A$ from any eigenspace.

### Exact finite proof

Choose a Gram realization $P_{ij}=\langle u_i,u_j\rangle$ with
$u_i\in\mathbb R^4$.  The coordinates of any $e\in\operatorname{range}E$
have the form $e_i=c\langle u_i,v\rangle$.  Hence its zero set

\[
 Z(e)=\{i:e_i=0\}
\]

is the set of orbit vectors contained in a subspace of dimension at most
three.  It is therefore the Gram-flat closure of an independent singleton,
pair, or triple.

The checker enumerates the H4 permutation orbits of all such bases:

* 18 pair orbits;
* 714 triple orbits, of which 7 are dependent;
* 726 independent spanning-flat representatives in total, including the
  singleton orbit.

All Gram determinants and closures are computed in
$\mathbb Q(\sqrt5)$.  Their sizes and representative counts are

\[
\begin{array}{c|rrrrrrrrrrrr}
|Z|&1&2&3&4&5&6&7&9&10&12&27&30\\ \hline
\#&1&11&83&88&37&76&52&94&34&54&122&74.
\end{array}                                                \tag{3.2}
\]

For every representative $Z$, the integer matrix $A[Z^c,Z]$ has full
column rank.  This is certified by row reduction modulo the prime
$1000003$; nonzero maximal minors modulo a prime are also nonzero over the
integers.

If an $A$-eigenvector $f$ were supported on $Z$, the eigenvector
equation on $Z^c$ would give

\[
                    A[Z^c,Z]f_Z=0,
\]

and full column rank would force $f_Z=0$.  Finally,
$e\circ f=0$ implies $\operatorname{supp}f\subseteq Z(e)$, yielding the
contradiction.  This proves (3.1).

### Corollary 3.2 (an exact positive coupling constant)

Compactness and Theorem 3.1 imply

\[
 c_{EF}:=\min_{\substack{e\in E,\ f\in F\\
                         \|e\|_2=\|f\|_2=1}}
                    \|e\circ f\|_2^2>0.                  \tag{3.3}
\]

This definition is exact.  The finite flat computation proves strict
positivity, but does **not** yet provide a useful rational lower bound for
$c_{EF}$.

## 4. A universal complementary-support leakage inequality

### Theorem 4.1 (proved)

Let $p,q\in\{-1,0,1\}^{300}$ have complementary supports, and put

\[
 s=\|p\|_2^2,\quad t=\|q\|_2^2=300-s,\quad
 \alpha=p^TEp,\quad \beta=q^TFq.
\]

Then

\[
\boxed{
 \sqrt{c_{EF}\alpha\beta}
 \le
 \sqrt{\frac{\alpha(t-\beta)}{75}}
 +2\sqrt{\frac{\beta(s-\alpha)}{75}}
 +\sqrt{(s-\alpha)(t-\beta)} .}                           \tag{4.1}
\]

In particular, if $s,t>0$, simultaneous perfect concentration
$\alpha=s$ and $\beta=t$ is impossible.

### Proof

Set

\[
 e=Ep,\quad a=p-e,\qquad f=Fq,\quad b=q-f.
\]

Orthogonality of the spectral projectors gives

\[
 \|e\|_2^2=\alpha,\quad \|a\|_2^2=s-\alpha,
 \quad\|f\|_2^2=\beta,\quad \|b\|_2^2=t-\beta.           \tag{4.2}
\]

Signed-H4 transitivity makes the diagonals of $E$ and $F$ constant.
Using their ranks gives

\[
 E_{ii}=\frac1{75},\qquad F_{ii}=\frac4{75}.              \tag{4.3}
\]

Therefore every vector in the corresponding ranges obeys

\[
 \|e\|_\infty\le\frac{\|e\|_2}{\sqrt{75}},\qquad
 \|f\|_\infty\le\frac{2\|f\|_2}{\sqrt{75}}.             \tag{4.4}
\]

Since $p\circ q=0$, expansion gives

\[
 e\circ f=-(e\circ b+a\circ f+a\circ b).
\]

The triangle inequality, (4.4), and
$\|a\circ b\|_2\le\|a\|_2\|b\|_2$ bound the right-hand side by the
right-hand side of (4.1).  Definition (3.3) bounds the left-hand side below
by $\sqrt{c_{EF}\alpha\beta}$.  This proves the claim.

Theorem 4.1 is a Clebsch--Gordan/Hadamard coupling constraint: it is not
obtainable from separate one-vector projector-energy bounds.  It is also
strict in the exact direction required by the complementary-support
reduction.

## 5. What is closed, and the smallest remaining gate

### Closed in this note

1. The archived $217+83$ support split and all four primary projector
   energies are recovered exactly.
2. The required residual ten-block correction is isolated to a unit interval,
   (2.8).
3. A finite H4-flat computation proves that the bilinear map
   $E\times F\to\mathbb R^{300}$, $(e,f)\mapsto e\circ f$, has no zero
   divisors.
4. The universal strict leakage inequality (4.1) holds for every
   complementary ternary pair.

### Still open

The current proof of $c_{EF}>0$ is qualitative, and the last term in (4.1)
uses the very loose estimate
$\|a\circ b\|_2\le\|a\|_2\|b\|_2$.  At the archived witness, both defects
matter: neither $p$ nor $q$ is close enough to perfect concentration for
(4.1), as written, to recover the $7.1148\times10^{15}$ correction in
(2.8).

The smallest plausible next certificate is therefore one of the following:

* an explicit rational lower bound for $c_{EF}$, together with a sharper
  complementary-support bound on $a\circ b$; or
* the degree-twelve nonradial H4 invariant/CG block which controls the mixed
  fourth-order quantity $\|Ep\circ Fq\|_2^2$ directly in terms of
  $(s,t,\alpha,\beta)$ and one finite orbit statistic.

Either route must be benchmarked against (2.8), not merely against the
independent inequalities $p^TEp\le s$ and $q^TFq\le t$.  This is the
remaining publishable lemma boundary exposed by the exact calculation.
