# d=4 H4 spectral-gap: exact primary spectrum and moment bounds

Status: **partial theorem and route reduction, not a proof of the classical
upper bound**.  Every statement labelled “proved” below has an exact argument;
the final joint Fourier-profile inequality remains open.

This note addresses `GROTHD4.classical.spectral-gap` without changing any
canonical node.  The companion exact checker is
`grothendieck-d4/tools/h4_spectral_gap_checker.py`.

## 1. Exact twelve-value spectrum (proved)

Let (A) be the frozen (300\times300) integer matrix.  Its square-free
minimal polynomial is the product of the following six irreducible factors:

\[
\begin{aligned}
f_0(t)&=t+138661354237888,\\
f_1(t)&=t^2-10265488660412764t
 -1421816489542807475215868726156,\\
f_2(t)&=t^2+210061762674492t
 +9969780653922489971805459684,\\
f_3(t)&=t^2+375839439213876t
 -1102647072483179451883551606876,\\
f_4(t)&=t^2+6416438611362062t
 +3336362192084004310572308931844,\\
f_5(t)&=t^3-1705855162085280t^2
 -246398705402929136951530868420t\\
&\qquad+506733415307469348748117480555083324928345752.
\end{aligned}
\]

Their exponents in the characteristic polynomial are, respectively,

\[
                 8,\ 4,\ 48,\ 24,\ 16,\ 36.
\]

Thus the twelve eigenspace dimensions, one for each real root, are
(8), (4,4), (48,48), (24,24), (16,16), and (36,36,36).

### Exact proof certificate

Starting with the coordinate vector (e_0), compute (A^ke_0) with Python
arbitrary-precision integers.  The degree-twelve recurrence obtained from the
first 24 scalar moments annihilates the **entire vector**, not merely its first
coordinate.  The four frozen signed-H4 generators satisfy exactly

\[
 A_{p(i),p(j)}=s_i s_j A_{ij},
\]

and their permutation orbit of (0) has size 300.  Therefore the relation
(m(A)e_0=0) propagates to every coordinate vector and gives (m(A)=0).
The factorization above is square-free.  Finally, signed-H4 transitivity makes
the diagonal of every (A^k) constant, so
\(\operatorname{tr}(A^k)=300(A^k)_{00}\).  Newton sums for \(k=0,\ldots,5\)
give a nonsingular six-by-six integer system whose unique solution is the
listed characteristic exponents.  This is all replayed by the checker.

The positive root of (f_1) is exactly the already certified

\[
 \lambda=5132744330206382+2356560241063596\sqrt5.
\]

The other root of (f_1) is the Galois-conjugate rank-four eigenspace.

## 2. The true residual norm (proved)

Let \(E=P/75\).  After removing `range(E)`, the largest absolute eigenvalue is
the absolute value \(\rho\) of the more negative root of \(f_4\):

\[
 \rho=\frac{6416438611362062+
 \sqrt{27825235685041889271593617164468}}2,
\]

with exact isolating interval

\[
 5845700854670610.5<\rho<5845700854670611.
\]

Consequently

\[
             \|A-\lambda E\|_{\rm op}=\rho.
\]

This is substantially sharper than the previous exact absolute-row-sum
estimate (1.0134945\times10^{16}).  If (F) denotes the rank-sixteen
projector onto the eigenvalue (-\rho), then after removing both (E) and
(F), the remaining norm is the largest root (sigma) of (f_5), where

\[
 1671954910365626<\sigma<56846466952431285/34
                 <1671954910365627.
\]

All root ordering claims are certified by rational Sturm isolating intervals.

## 3. An exact H4 moment inequality for sign projections (proved)

Let (u_1,\ldots,u_{300}\in S^3) be any Gram realization of (P), so
(P_{ij}=\langle u_i,u_j\rangle).  For every unit (v\in\mathbb R^4), put
(t_i=\langle u_i,v\rangle).  The signed H4 orbit has the required even design
moments through degree 10.  One can see this without numerical coordinates:
the H4 invariant ring has basic degrees \(2,12,20,30\), so invariant forms of
even degree below 12 are scalar powers of \(\|v\|^2\).  Spherical averaging
fixes the scalars.  In particular,

\[
 \sum_i t_i^2=75,\qquad
 \sum_i t_i^4=\frac{75}{2},\qquad
 \sum_i t_i^6=\frac{375}{16}.
\]

For (0\le t\le1), the following pointwise polynomial majorant is exact:

\[
 t\le \frac{\sqrt5}{50}
       \left(32t^6-56t^4+46t^2+3\right).
\]

Indeed the right side minus (t) is

\[
 \frac{16\sqrt5}{25}
 \left(t-\frac{\sqrt5+1}{4}\right)^2
 \left(t-\frac{\sqrt5-1}{4}\right)^2
 \left(t^2+\sqrt5t+\frac32\right),
\]

which is nonnegative.  Applying it to (|t_i|) and using the three moment
identities yields

\[
                 \sum_i |t_i|\le60\sqrt5.
\]

For a sign vector (x), write (s=\sum_i x_i u_i).  If (s\ne0), choose
(v=s/\|s\|).  Then

\[
 \|s\|=\sum_i x_i\langle u_i,v\rangle
       \le\sum_i|t_i|\le60\sqrt5,
\]

and therefore

\[
       \boxed{\quad x^TEx=\|s\|^2/75<240.\quad}
\]

The inequality is strict.  Equality in the polynomial majorant would force
all (|t_i|) to lie in
({(\sqrt5-1)/4,(\sqrt5+1)/4}).  If (n) of them use the smaller value,
then

\[
 \sum_i t_i^2=
 \frac{900+(300-2n)\sqrt5}{8},
\]

which cannot equal 75 (its rational part is already (112.5)).

This is a genuine analytic sign-profile restriction.  It replaces the
trivial (x^TEx\le300) by a strict universal bound and uses no optimizer.

### A degree-ten strengthening (proved)

The same invariant argument gives all the even moments needed below:

\[
 \frac1{300}\sum_i t_i^{2j}
 =\frac{(1/2)_j}{(2)_j},\qquad j=0,1,\ldots,5.       \tag{3.1}
\]

These are the moments of the beta distribution
\(d\mu(z)\propto z^{-1/2}(1-z)^{1/2}dz\) on \([0,1]\), with
\(z=t^2\).  Its three-node Gaussian quadrature rule has

\[
 r_k=\cos^2\frac{k\pi}{7},\qquad
 w_k=\frac47\sin^2\frac{k\pi}{7},\qquad k=1,2,3.   \tag{3.2}
\]

Indeed the node polynomial is

\[
 64z^3-80z^2+24z-1=U_6(\sqrt z),
\]

and a direct trigonometric calculation verifies
\(\sum_k w_kr_k^j=(1/2)_j/(2)_j\) for \(j\le5\).

Let \(H\) be the degree-five Hermite interpolant to \(\sqrt z\) at the
three nodes, matching both value and derivative.  For \(z>0\), the Hermite
remainder has the sign

\[
 \sqrt z-H(z)
 =\frac{f^{(6)}(\xi)}{6!}\prod_{k=1}^3(z-r_k)^2\le0,
 \qquad f(z)=\sqrt z,\qquad f^{(6)}(z)<0.
\]

The inequality at \(z=0\) follows by continuity.  Thus (3.1), exactness of
the quadrature, and (3.2) give

\[
 \frac1{300}\sum_i|t_i|
 \le\sum_{k=1}^3w_k\sqrt{r_k}
 =\frac27\left(\cos\frac\pi7+\cos\frac{2\pi}7\right). \tag{3.3}
\]

Consequently every sign vector satisfies the sharper exact bound

\[
 x^TEx\le
 \frac{4800}{49}
 \left(\cos\frac\pi7+\cos\frac{2\pi}7\right)^2
 <228.                                                     \tag{3.4}
\]

For the last rational comparison, the squared cosine sum is the largest root
of

\[
 64u^3-224u^2+196u-49,
\]

and Sturm isolation gives
\(u<911/392<931/400\).  Substitution into (3.4) yields the displayed
strict inequality.  This upgrades \(x^TEx<240\) to \(x^TEx<228\) using only
exact H4 design theory and a finite interpolation identity.

## 4. Why these two advances do not yet close the classical bound

Combining only the rank-four energy bound with the exact residual norm gives

\[
 x^TAy\le
 \lambda\sqrt{a_xa_y}+
 \rho\sqrt{(300-a_x)(300-a_y)},
 \qquad a_z=z^TEz<228.
\]

Even this strengthening does not close the estimate.  Its boundary envelope
is \(228\lambda+72\rho\), approximately

\[
 2.7925859562201992\times10^{18},
\]

which exceeds \(C\) by approximately
\(7.115418031328478\times10^{17}\).  Thus the exact top-energy restriction
alone is insufficient.

Nor is it enough to split off the rank-sixteen (-\rho) block and apply
Cauchy independently on the remaining blocks.  This failure occurs already
on the archived equality witness.  Floating diagnostics (not a proof) give

| profile | archived `ax` | archived `by` |
|---|---:|---:|
| (\|Ez\|^2) | 171.5116977 | 175.6727502 |
| (\|Fz\|^2) | 70.1320736 | 69.9285057 |
| remaining energy | 58.3562287 | 54.3987442 |

and cross-correlations

\[
 \langle E x,E y\rangle\approx173.0511094,
 \qquad
 \langle F x,F y\rangle\approx-49.2757626.
\]

The three-block Cauchy envelope at this equality witness is about
(2.182361522\times10^{18}), already (1.01317\times10^{17}) above (C),
while the actual remaining spectral blocks cancel back to equality.  Hence a
one-vector energy profile, or independent blockwise Cauchy, discards essential
information.

## 5. Minimal remaining lemma

Let (E_1,\ldots,E_{12}) be the exact spectral projectors associated with the
twelve isolated roots (\theta_1,\ldots,\theta_{12}), with (E_1=E).  The
remaining publishable gate is now the finite joint Fourier statement

\[
 \boxed{
   \sum_{k=1}^{12}\theta_k
   \langle E_kx,E_ky\rangle\le C
   \quad\text{for all }x,y\in\{\pm1\}^{300}.
 }
\]

The useful narrowing is that the only large terms are the rank-four
(+\lambda) block and the rank-sixteen (-\rho) block; every other coefficient
has absolute value below (1.672\times10^{15}).  However, the archived equality
witness proves that the signed correlations of the smaller blocks, not merely
their energies, must be retained.

A next certificate should therefore target **joint block correlations**.  A
viable exact form is a finite family of H4 Reynolds/Clebsch--Gordan inequalities
in the scalars

\[
 c_k(x,y)=\langle E_kx,E_ky\rangle,
\]

with the Boolean identities (x_i^2=y_i^2=1) used before applying Cauchy.
The top-space sign-lock shortcut is not available: the archived equality
witness has dozens of exact sign disagreements with its top projection, as
recorded independently in the main audit.

## 6. Evaluation of the complementary-support \(p/q\) route

For signs \(x,y\), set

\[
 p=\frac{x+y}{2},\qquad q=\frac{x-y}{2}.
\]

Then \(p,q\in\{-1,0,1\}^{300}\), their supports are complementary, and
symmetry of \(A\) gives the exact identity

\[
                 x^TAy=p^TAp-q^TAq.                 \tag{6.1}
\]

This is a better structural starting point than treating \(x\) and \(y\)
independently: it exposes the cancellation between the positive spectrum seen
by \(p\) and the negative spectrum seen by \(q\).  In particular, if
\(s=|\operatorname{supp}p|\), the moment argument above immediately gives the
proved support-sensitive estimate

\[
 p^TEp\le \min\{s,228\},            \tag{6.2}
\]

and the same estimate with \(q\) and \(300-s\).  The first term in (6.2) is
just \(\|p\|_2^2=s\), while the second follows verbatim from the H4 polynomial
majorant because zero coordinates only decrease
\(\sum_i p_i\langle u_i,v\rangle\).

There is also an exact obstruction to strengthening this by using only the
five even moments (3.1).  The four-node Lobatto measure

\[
\begin{aligned}
\nu={}&\frac7{24}\delta_0
+\left(\frac{29}{84}+\frac{\sqrt7}{21}\right)
 \delta_{(5-\sqrt7)/12}\\
&+\left(\frac{29}{84}-\frac{\sqrt7}{21}\right)
 \delta_{(5+\sqrt7)/12}
+\frac1{56}\delta_1
\end{aligned}                                             \tag{6.3}
\]

satisfies, exactly,

\[
 \int z^j\,d\nu(z)=\frac{(1/2)_j}{(2)_j},
 \qquad j=0,\ldots,5.
\]

Moreover, mixing \((166/175)\nu\) with \((9/175)\mu\), where \(\mu\) is the
beta measure from (3.1), preserves every listed moment and puts mass

\[
 \frac{166}{175}\frac7{24}=\frac{83}{300}
\]

at zero.  Therefore the continuous relaxation that remembers only support
fraction and the degree-ten H4 design moments permits all \(83/300\) of the
complementary mass to have zero projection.  This does not construct a
300-point H4 counterexample, but it rigorously proves that a moment-dual
argument which discards equal-atom/orbit information cannot force the needed
leakage at the archived split \(217+83\).  The first available new scalar
information is the degree-twelve non-radial H4 invariant.

However, **upper bounds for the top projector on \(p\) and the most-negative
projector on \(q\), even if optimized exactly as functions of support size,
cannot by themselves prove the target**.  The archived equality witness has

\[
 |\operatorname{supp}p|=217,\qquad
 |\operatorname{supp}q|=83,
\]

and floating diagnostics give

\[
 p^TEp\approx173.3216667,\qquad p^TFp\approx10.3772635,
\]
\[
 q^TEq\approx0.2705573,\qquad q^TFq\approx59.6530261.
\]

Already the two dominant favorable contributions satisfy

\[
 \lambda p^TEp+\rho q^TFq
 \approx2.15163574535\times10^{18}>C
\]

by about \(7.06\times10^{16}\).  Thus a certificate that only upper-bounds
these two quantities has an envelope above \(C\) at an actual equality pair.
This is a numerical refutation of that proposed proof ansatz, not a theorem
about the optimizer.

The exact decomposition that must replace it is

\[
 p^TAp-q^TAq
 =\bigl(p^TA_+p+q^TA_-q\bigr)
  -\bigl(p^TA_-p+q^TA_+q\bigr),                    \tag{6.4}
\]

where \(A_+\) and \(A_-\) are the positive and absolute-negative spectral
parts of \(A\).  On the archived pair, the first parenthesis in (6.4) is
numerically about \(9.79\times10^{16}\) above \(C\); the second parenthesis
supplies exactly the indispensable correction.  Consequently the smallest
plausible new lemma is a **coupled complementary-support lower bound**

\[
 p^TA_-p+q^TA_+q\ \ge\
 \Phi_s\bigl(p^TEp,q^TFq,\text{further H4 profiles}\bigr), \tag{6.5}
\]

strong enough to cancel the excess in the corresponding upper bound for the
first parenthesis.  A bound depending only on \(s\) may still be too coarse;
the archived calculation shows that it must at least retain the two dominant
projector energies, and likely one or more Reynolds/Clebsch--Gordan coupling
invariants.  Once such a formula is derived, only the finite cases
\(s=0,\ldots,300\) remain.

Thus the \(p/q\) route remains promising, but its publishable core is not two
separate support-size projector bounds.  It is the forced spectral leakage in
(6.5), arising from the complementary Boolean supports.

## 7. What is theorem, observation, and open

- **Proved:** exact minimal polynomial, characteristic factor multiplicities,
  actual residual norm \(\rho\), post-rank-sixteen norm \(\sigma\), and
  \(x^TEx<228\) for every sign vector.
- **Numerical diagnostic only:** the displayed archived-witness block energies
  and correlations.  They are used only to refute overly coarse proof ansatzes.
- **Open:** a Boolean-valid joint inequality between the twelve block
  correlations strong enough to give (C), equivalently a coupled leakage
  inequality of the form (6.5).
