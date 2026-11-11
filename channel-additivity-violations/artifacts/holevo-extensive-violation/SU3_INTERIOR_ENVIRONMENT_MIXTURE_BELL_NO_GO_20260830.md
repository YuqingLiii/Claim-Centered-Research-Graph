# Interior irreducible-input SU(3) environment mixtures have no Bell gap

Date: 2026-08-30

Status: proposer-side all-parameter theorem with certified rational-log endpoint checks;
independent review pending.

This note proves the scalar inequality left open by the exact mixture reduction. Natural
logarithms are used for relative entropies; changing the base does not affect any comparison.

## Theorem

Let the qutrit output carry the fundamental representation of `SU(3)`, and let the input carry an
arbitrary interior irreducible representation `V_(r,s)`, `r,s>=1`. Allow an arbitrary covariant
channel obtained by mixing all three inequivalent irreducible Stinespring environments, with
arbitrary equivalent-copy multiplicity. Then

\[
 \boxed{
 2\overline S_{\min}(\Phi)
 \le2S_{\min}(\Phi)
 \le S\!\left((\Phi\otimes\bar\Phi)(\Omega_{\dim V_{(r,s)}})\right).}
\tag{1}
\]

Together with the boundary-mixture theorem, this closes every `SU(3)`-covariant qutrit-output
channel whose input representation is irreducible.

It does not cover a reducible input carrying cross-irrep coherences, a noncovariant qutrit Gram
factor, or a non-Bell collective input.

## 1. Exact classical reduction

Use the notation of the mixture-reduction node. The three extreme weights are `lambda`, their
dimension barycenter is `mu`, and a common highest-weight input has output distribution
`q=lambda K_(r,s)`. The Gram parameter is

\[
 t=\frac18\chi^2(\lambda\Vert\mu).
\tag{2}
\]

Let `u_3` and `u_9` be the uniform distributions on three and nine points. The Bell-minus-side
entropy difference for this explicit input is

\[
 B(t)-2H(q)
 =2D(q\Vert u_3)-D(P_t\Vert u_9),
\tag{3}
\]

where

\[
 P_t=\left(\frac{1+8t}{9},
 \underbrace{\frac{1-t}{9},\ldots,\frac{1-t}{9}}_{8\text{ times}}\right).
\tag{4}
\]

It is enough to prove that the right side of (3) is nonnegative.

## 2. Sharp qutrit relative-entropy/collision lemma

For every probability vector `q` on three points,

\[
 \boxed{
 D(q\Vert u_3)
 \ge\frac{2\ln2}{3}\chi^2(q\Vert u_3).}
\tag{5}
\]

The constant is sharp at permutations of `(2/3,1/6,1/6)`.

To prove (5), minimize the ratio of the two sides on the compact simplex, extending its value at
the uniform point by continuity. Lagrange multipliers show that an interior extremizer has at most
two distinct coordinates. Up to permutation its interior part therefore reduces to

\[
 q=\left(x,\frac{1-x}{2},\frac{1-x}{2}\right),
 \qquad0\le x\le1.
\tag{6}
\]

After substitution, (5) is

\[
 f(x):=
 x\ln(3x)+(1-x)\ln\!\left(\frac{3(1-x)}2\right)
 -\frac{\ln2}{3}(3x-1)^2\ge0.
\tag{7}
\]

Here

\[
 f'(x)=\ln\!\left(\frac{2x}{1-x}\right)-2\ln2(3x-1),
 \qquad
 f''(x)=\frac1{x(1-x)}-6\ln2.
\tag{8}
\]

The derivative has the three interior zeros `1/3`, `1/2`, and `2/3`; the monotonicity pattern
from (8), together with the two endpoints, gives `f>=0`. Equality occurs at `x=1/3` and `x=2/3`.

For a boundary vector `(x,1-x,0)`, put `y=2x-1`. The binary relative-entropy series gives

\[
 D(q\Vert u_3)
 =\ln\frac32+D_{\mathrm{bin}}(x\Vert1/2)
 \ge\ln\frac32+\frac{y^2}{2}+\frac{y^4}{12}.
\tag{9}
\]

Subtracting `(2 ln 2/3)chi^2`, the right side is minimized at `y^2=1` and remains positive because

\[
 \ln3+\frac7{12}-\frac73\ln2>0.
\tag{10}
\]

The rational-log checker certifies the last sign. This completes the boundary part of (5).

## 3. Uniform collision contraction of the triangular channel

For every `r,s>=1` and every mixture weight `lambda`, the highest-weight stochastic map obeys

\[
 \boxed{
 \chi^2(q\Vert u_3)\ge\frac85t.}
\tag{11}
\]

This is an exact two-by-two quadratic-form comparison. Write
`delta=lambda-mu=(a,b,-a-b)`. With `D` the two-column matrix
`(k_+-k_c,k_m-k_c)`, inequality (11) is positivity of

\[
 M=3D^TD-\frac15
 \begin{pmatrix}
 1/\mu_++1/\mu_c&1/\mu_c\\
 1/\mu_c&1/\mu_m+1/\mu_c
 \end{pmatrix}.
\tag{12}
\]

Its upper-left entry is positive: after removing its positive denominator, the numerator is

\[
 8r^2s^2+23r^2s+24r^2+8rs^3+26rs^2+28rs+6r-s^3-8s^2-21s-18.
\]

This numerator increases with `r`, and at `r=1` it is
`7s^3+26s^2+30s+12>0`. After removing positive denominator factors, the determinant is

\[
 8r^2s-4r^2+8rs^2-4rs-5r-4s^2-5s+6.
\tag{13}
\]

Expression (13) vanishes at `(1,1)` and is strictly increasing in each variable for `r,s>=1`:

\[
 \partial_r=16rs+8s^2-8r-4s-5>0,
 \qquad
 \partial_s=8r^2+16rs-4r-8s-5>0.
\tag{14}
\]

Hence `M` is positive semidefinite. The constant `8/5` is attained infinitesimally at `(1,1)`.

## 4. The region `0<=t<=2/3`

Combining (5) and (11) gives

\[
 2D(q\Vert u_3)
 \ge\frac{32\ln2}{15}t.
\tag{15}
\]

The function `D(P_t||u_9)` is convex and vanishes at zero, so its ratio to `t` is increasing. A
certified rational-log comparison at `t=2/3` gives

\[
 D(P_{2/3}\Vert u_9)
 <\frac{64\ln2}{45}
 =\frac{32\ln2}{15}\frac23.
\tag{16}
\]

Thus (3) is nonnegative throughout `0<=t<=2/3`.

The checker proves (16) using the rational atanh series for logarithms with an explicit positive
remainder bound; no floating-point sign decision is used.

## 5. The region `2/3<t<=7/8`

The extreme Gram values are `t_i=1/(8mu_i)-1/8`, and the quadratic expression (2) is convex in
`lambda`. The dimension weights obey

\[
 \mu_m\ge\frac16,
 \qquad
 \mu_c\ge\frac13,
 \qquad
 \mu_+\ge\frac18.
\tag{17}
\]

Moreover `mu_+>=8/45>3/19` when `r>=2`. Since `t>2/3` requires some `mu_i<3/19`, it forces
`r=1`. In that case `mu_m>=1/4` and `mu_c>=1/3`. Put `a=lambda_+`. Then

\[
 t\le\frac18\left(8a^2+4(1-a)^2-1\right)
 =\frac32a^2-a+\frac38.
\tag{18}
\]

Consequently

\[
 a\ge a_0(t):=\frac{1+\sqrt{6t-5/4}}3.
\tag{19}
\]

The first component of `q` is at least `a`; since `a>1/3`,

\[
 H(q)\le E(a):=
 H\!\left(a,\frac{1-a}{2},\frac{1-a}{2}\right),
\tag{20}
\]

and `E` decreases with `a`. Also `t<=7/8` by (17).

Partition `[2/3,7/8]` into

\[
 \left[\frac23,\frac34\right],
 \left[\frac34,\frac45\right],
 \left[\frac45,\frac56\right],
 \left[\frac56,\frac67\right],
 \left[\frac67,\frac78\right].
\tag{21}
\]

At their left endpoints, certified rational lower bounds for `a_0` are respectively

\[
 \frac{22}{25},\quad\frac{93}{100},\quad\frac{24}{25},
 \quad\frac{39}{40},\quad\frac{99}{100}.
\tag{22}
\]

Because `B` and `E` both decrease, each interval follows from comparing `B` at its right endpoint
with twice `E` at the corresponding rational bound in (22). The certified natural-log margins are
all positive; the smallest exceeds `0.09`. Hence (3) is positive also for `t>2/3`.

## 6. Consequence and exact boundary

Equations (15)--(22) prove the theorem. The earlier 3.21-million-point scan is now only an audit;
the conclusion no longer depends on its grid resolution.

The surviving `SU(3)`-covariant route would have to use a reducible input and exploit cross-irrep
coherences. Outside covariance, arbitrary nondepolarizing qutrit Gram factors remain open.
