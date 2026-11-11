# Complex-Haar global two-copy purity: concentration and relaxation gate

Date: 2026-08-30

Status: proposer-side obstruction/reduction for the one-layer, same-tuple `n=2` problem.  No
canonical YAML is changed.  The global physical-output assertion remains **OPEN**.

All logarithms are base two unless `ln` is written explicitly.  Constants denoted `c_0,C_0` are
universal and their numerical values are irrelevant to the dimension comparison.

## 1. Setup and verdict

Let `U_1,...,U_m` be independent Haar unitaries in `U(d)` and let

\[
 C(X)_{v,w}=\frac1m\operatorname{Tr}(XU_w^*U_v)
\tag{1}
\]

be the complementary channel of the corresponding random-unitary channel.  Put

\[
 c=(1+\eta)^2,\qquad A=1+\frac{9c}{m},qquad
 T=\frac{A^2}{m^2}.
\tag{2}
\]

The global two-copy target is

\[
 \sup_{\psi\in\mathbb C^d\otimes\mathbb C^d,\ \|\psi\|=1}
 f_U(\psi)\le T,
 \qquad
 f_U(\psi)=\operatorname{Tr}
   [C^{\otimes2}(|\psi\rangle\langle\psi|)^2].
\tag{3}
\]

The conclusions are:

1. A direct fixed-state Haar concentration plus pure-state epsilon-net argument is quantitatively
   impossible with the standard Lipschitz tail.  The input metric entropy is
   `Theta(d^2 log(1/epsilon))`, while Haar concentration gives an exponent only linear in `d`.
   At the required purity resolution, the comparison is

   \[
    \exp\{\Theta(d^2\log m)-\Theta(d/m^5)\}.
   \tag{4}
   \]

2. Dropping the replica separability/diagonal-product constraint and bounding the full replica
   operator norm cannot work even with perfect concentration.  The relaxation value is
   deterministically at least

   \[
      \frac{2-1/m}{m^2},
   \tag{5}
   \]

   which exceeds `T` whenever `A^2<2-1/m`.  This includes `eta=0,m>=23` and the intended
   `ln m>18` regime for sufficiently small fixed `eta`.  This is a relaxation obstruction, **not**
   a physical-state counterexample.
3. A finite-level PPT/DPS computation has no dimension-uniform certification guarantee.  Because
   the exact cone is the Hartree/symmetric bosonic cone, the sharper available generic trace-norm
   de Finetti error is `O(d^2/k)` at extension level `k`; resolving an `O(m^-3)` margin therefore
   requires `k` on the order of `m^3d^2` even if a margin is granted.  The older ordinary
   permutation-invariant estimate `O(d^4/k)` is valid but non-sharp for this cone.
4. Low-Schmidt-rank nets reduce metric entropy from `Theta(d^2)` to `Theta(dr)`, but the standard
   Lipschitz tail is still too weak even at fixed `r>=1` for the enormous `m` used here.  Such a
   stratification becomes viable only after a stronger, entry-sensitive fixed-state moment bound.
5. The smallest clean replacement is an exact output-dual coefficient formulation.  Its
   coefficient net has dimension `m^4`, independent of `d`.  What is missing is a same-tuple,
   two-leg strong-norm estimate for a fixed scalar coefficient polynomial—not a net over input
   states and not an arbitrary growing cb amplification.

## 2. The target margin is only `Theta(m^-3)`

Every state on the `m^2`-dimensional output space has purity at least `1/m^2`.  Therefore even in
the optimistic situation in which every fixed input has Haar mean essentially equal to the
maximally mixed baseline, the largest available additive gap to the target is

\[
 s:=T-\frac1{m^2}
 =\frac{A^2-1}{m^2}
 =\frac{18c}{m^3}+\frac{81c^2}{m^4}.
\tag{6}
\]

Any pointwise concentration/net proof must work at deviation scale `t<=s/2=Theta(m^-3)`.  Taking
a larger `t` cannot certify (3), irrespective of the fixed-input mean calculation.

## 3. Exact Lipschitz costs

### 3.1 Dependence on the input vector

Let `rho_psi=|psi><psi|`.  Trace-norm contractivity and
`|Tr(sigma^2)-Tr(tau^2)|<=2||sigma-tau||_1` give

\[
 \begin{aligned}
 |f_U(\psi)-f_U(\phi)|
 &\le2\|C^{\otimes2}(\rho_\psi-\rho_\phi)\|_1\\
 &\le2\|\rho_\psi-\rho_\phi\|_1
 \le4\|\psi-\phi\|_2.
 \end{aligned}
\tag{7}
\]

Thus an input net must have Euclidean radius at most `epsilon=t/8` if its interpolation loss is to
be at most `t/2`.

### 3.2 Dependence on the Haar tuple

Use the Stinespring isometry

\[
 V_Ux=\frac1{\sqrt m}\sum_{i=1}^m U_ix\otimes|i\rangle.
\tag{8}
\]

For two tuples `U=(U_i)` and `V=(V_i)`, put

\[
 d_{\rm HS}(U,V)=
 \left(\sum_i\|U_i-V_i\|_2^2\right)^{1/2}.
\tag{9}
\]

Then

\[
 \|V_U-V_V\|_\infty
 \le\frac1{\sqrt m}d_{\rm HS}(U,V),
 \qquad
 \|V_U^{\otimes2}-V_V^{\otimes2}\|_\infty
 \le\frac2{\sqrt m}d_{\rm HS}(U,V).
\tag{10}
\]

The trace distance between the two complementary outputs is at most twice the isometry distance.
Applying the purity inequality once more yields

\[
 |f_U(\psi)-f_V(\psi)|
 \le\frac8{\sqrt m}d_{\rm HS}(U,V).
\tag{11}
\]

The function is invariant under independent scalar phases on the `U_i`, so the harmless central
`U(1)` directions can be removed.  Standard Haar concentration on the product of the resulting
projective/special unitary groups, with tensorized Hilbert--Schmidt metric, gives for fixed `psi`

\[
 \Pr\{|f_U(\psi)-\mathbb Ef_U(\psi)|>t\}
 \le2\exp\!\left(-c_0 mdt^2/64\right).
\tag{12}
\]

Only the scaling matters: the exponent is `Theta(md t^2)`, not `Theta(d^2t^2)`.

## 4. Full pure-state epsilon-net obstruction

The unit sphere of `C^(d^2)` has real dimension `2d^2-1`.  Its epsilon-covering and packing
numbers satisfy, up to universal constants,

\[
 \left(\frac{c_0}{\epsilon}\right)^{2d^2-1}
 \lesssim N(\epsilon)
 \lesssim
 \left(1+\frac2\epsilon\right)^{2d^2}.
\tag{13}
\]

Set `epsilon=t/8`.  Even granting the optimistic uniform mean bound

\[
 \mathbb Ef_U(\psi)\le T-2t
 \quad\text{for every fixed }\psi,
\tag{14}
\]

the direct union bound supplied by (12) is at best

\[
 2\exp\!\left[
  2d^2\log\!\left(1+\frac{16}{t}\right)
  -\frac{c_0mdt^2}{64}
 \right].
\tag{15}
\]

For every fixed `m,t>0`, the positive term is quadratic in `d` and the negative term is only
linear.  Hence (15) diverges rather than tending to zero as `d->infinity`.

At the actual target scale `t=Theta(m^-3)`,

\[
 \log N(t/8)=\Theta(d^2\log m),
 \qquad
 mdt^2=\Theta(d/m^5),
\tag{16}
\]

which is (4).  This remains a failure even though `m` is held fixed before `d->infinity`: increasing
`d` worsens the entropy/concentration ratio by another factor of `d`.

This proves a gate on the **method**, not on the truth of (3).  A special polynomial may have much
smaller tails than the generic Lipschitz inequality detects; such a result would need an additional
high-moment calculation.

## 5. Low-Schmidt-rank stratification

Identify `psi` with a `d x d` matrix of Frobenius norm one.  The set of Schmidt-rank-at-most-`r`
pure states has an epsilon-net of size

\[
 N_r(\epsilon)
 \le\left(\frac{C_0}{\epsilon}\right)^{4dr},
\tag{17}
\]

with the sharper manifold dimension `4dr-2r^2-2` away from lower-rank strata.  Combining (12)
with (17) gives exponent

\[
 4dr\log(C_0/t)-c_0mdt^2/64.
\tag{18}
\]

At `t=Theta(m^-3)`, the positive coefficient of `d` is `Theta(r log m)`, whereas the negative
coefficient is `Theta(m^-5)`.  For `ln m>18`, the standard Lipschitz concentration is therefore
too weak even for `r=1`.  Rank-one/separable inputs are safe for the separate deterministic reason
proved in `PRODUCT_HAAR_PHYSICAL_SELF_PURITY_N2_ANALYSIS_20260830.md`; (18) does not recover it.

A low-rank program becomes viable if one first proves an entry-sensitive tail of the form

\[
 \Pr\{f_U(\psi)-\mathbb Ef_U(\psi)>t\}
 \le \exp\!\left[-c_1d^2t^2/m^\alpha\right]
\tag{19}
\]

uniformly on fixed-rank inputs.  Then (17) closes for ranks

\[
 r\ll \frac{d t^2}{m^\alpha\log(C_0/t)};
\tag{20}
\]

at the target scale this is

\[
 r\ll\frac{d}{m^{\alpha+6}\log m}.
\tag{21}
\]

Thus a precise next lemma is: establish (19) by an order-controlled Weingarten/high-moment
calculation and thereby force every counterexample to have Schmidt rank diverging at least as fast
as the right side of (21).  Without such a tail upgrade, merely stratifying the net by Schmidt rank
does not help.

## 6. Replica operator and a deterministic relaxation obstruction

For the single complementary channel define the Hermitian replica operator on
`C^d tensor C^d`

\[
 R_U=\frac1{m^2}\sum_{v,w=1}^m
  U_w^*U_v\otimes U_v^*U_w.
\tag{22}
\]

After the fixed permutation that groups the first physical leg from the two replicas together, the
two-copy replica operator is exactly

\[
 Q_U\simeq R_U\otimes R_U.
\tag{23}
\]

The physical objective has the restricted form

\[
 f_U(\psi)=\langle\psi\otimes\psi,
 Q_U(\psi\otimes\psi)\rangle.
\tag{24}
\]

Dropping the diagonal-product/separability restriction replaces (24) by
`lambda_max(Q_U)=||R_U||_infty^2`.  This relaxation is deterministically too large.  Indeed, set
`B_{v,w}=U_w^*U_v`.  Cyclicity of trace gives

\[
 \frac1{d^2}\operatorname{Tr}(R_U^2)
 =\frac1{m^4d^2}\sum_{v,w,x,y}
  |\operatorname{Tr}(B_{v,w}B_{x,y})|^2.
\tag{25}
\]

Every summand is nonnegative.  There are two exact collision families:

- `v=w` and `x=y`, giving `m^2` terms with product `I`;
- `x=w` and `y=v`, giving `m^2` inverse-pair terms with product `I`.

Their intersection has `m` terms.  Keeping only their union in (25) yields

\[
 \frac1{d^2}\operatorname{Tr}(R_U^2)
 \ge\frac{2m^2-m}{m^4}
 =\frac{2-1/m}{m^2}.
\tag{26}
\]

Since `R_U` is Hermitian,

\[
 \boxed{
 \lambda_{\max}(Q_U)=\|R_U\|_\infty^2
 \ge\frac1{d^2}\operatorname{Tr}(R_U^2)
 \ge\frac{2-1/m}{m^2}.}
\tag{27}
\]

Consequently, whenever `A^2<2-1/m`, a proof of (3) cannot pass through the full operator norm of
`Q_U`.  Notice the distinction:

- Section 6 of `PRODUCT_HAAR_PHYSICAL_SELF_PURITY_N2_ANALYSIS_20260830.md` turned the same
  numerical threshold into a **physical Bell-input violation** only for simultaneously real
  tuples.
- Equation (27) holds for every complex tuple, but its maximizing replica vector need not equal
  `psi tensor psi` and need not be separable across the replica cut.  It is therefore only a strict
  relaxation gap.

There is a second warning against partial-transpose/cb relaxations.  Partial transpose on the
second factor of (22) gives

\[
 R_U^\Gamma=\frac1{m^2}\sum_{v,w}
 B_{v,w}\otimes\overline{B_{v,w}},
 \qquad
 R_U^\Gamma|\Omega_d\rangle=|\Omega_d\rangle.
\tag{28}
\]

Thus any upper bound that replaces the physical cone by `||R_U^Gamma||_infty` has a unit-size
direction, compared with the desired one-factor scale `A/m`.  Positivity and replica geometry
cannot be discarded.

## 7. Why ordinary matrix Bernstein does not repair the replica route

The `m^2` summands in (22), and the `m^4` summands in `Q_U`, are functions of only the same `m`
independent Haar matrices.  Treating them as independent summands is invalid.  Exposing the
`U_i` one at a time gives only `m` matrix-martingale increments; a bounded-difference estimate of
that kind has no improving sample count as `d->infinity`.  Haar manifold concentration can add a
dimension-`d` exponent, but it cannot change the deterministic lower bound (27).

The mean of the one-factor replica operator illustrates the correct scale but does not control its
norm:

\[
 \mathbb ER_U
 =\frac1m I+\frac{m-1}{md}F,
\tag{29}
\]

where `F` is the swap on `C^d tensor C^d`.  Hence `||E R_U||=1/m+O(1/d)`, while every realization
has the Hilbert--Schmidt/operator relaxation floor (27).  Concentration around the matrix mean in
operator norm is therefore false at the target-tight scale.  Quantitatively,

\[
 \|R_U-\mathbb ER_U\|_\infty
 \ge\frac{\sqrt{2-1/m}}m
 -\left(\frac1m+\frac{m-1}{md}\right),
\tag{29a}
\]

which approaches `(sqrt(2)-1)/m`, much larger than the `Theta(m^-2)` finite-model slack.

## 8. Separability, PPT, and DPS cost

The exact lifted optimization is over trace-one positive operators `X` on two replicas of the
`h=d^2` dimensional input, supported on the replica-symmetric subspace and separable across the
replica cut:

\[
 \max\ \operatorname{Tr}(Q_UX),
 \quad X\in\operatorname{Sep}(\mathbb C^h:\mathbb C^h),
 \quad X=P_{\rm sym}XP_{\rm sym}.
\tag{30}
\]

PPT and finite symmetric-extension constraints give valid upper relaxations, but no fixed level is
dimension-uniformly exact.  Here the exact cone is generated by Hartree powers
`|psi><psi| tensor |psi><psi|`, so its lifted states are supported on the fully symmetric bosonic
subspace.  The sharper bosonic/exchangeable finite de Finetti estimate has trace-distance error of
order

\[
 \inf_{\sigma\in\operatorname{Sep}}\|X-\sigma\|_1
 \le C_0\frac{h}{k}
 =C_0\frac{d^2}{k}.
\tag{31}
\]

Because `||Q_U||_infty<=1`, the same quantity bounds the additive objective error.  Even granting
a separable optimum below the target by the full available margin `s=Theta(m^-3)`, the generic
guarantee requires

\[
 k\gg m^3d^2.
\tag{32}
\]

The corresponding SDP dimension grows exponentially in `k`.  The older finite de Finetti theorem
for an ordinary permutation-invariant extension gives the weaker but still valid error
`O(h^2/k)=O(d^4/k)` and sufficient level `k>>m^3d^4`; it is not the sharp generic theorem for the
present bosonic cone.  Equation (32) is not a proof that a low PPT/DPS level fails on this special
random instance; it shows that even the sharper generic hierarchy convergence gives no fixed-level
dimension-uniform interface.  A successful low-level PPT argument would need a new
instance-specific dual certificate exploiting (24), not just the abstract hierarchy theorem.

## 9. Minimal viable replacement: dualize the output, not the input sphere

There is an exact way to avoid the `d^2` input entropy without passing to the false replica
operator-norm relaxation.  Put `N=C tensor C`.  Hilbert--Schmidt duality and positivity give

\[
 \begin{aligned}
 \sup_{\rho\in\mathcal D}\|N(\rho)\|_2
 &=\sup_{\substack{Y=Y^*\\\|Y\|_2=1}}
   \lambda_{\max}(N^*(Y))\\
 &=\sup_{\substack{Y=Y^*\\\|Y\|_2=1}}
   \|N^*(Y)\|_\infty,
 \end{aligned}
\tag{33}
\]

where the last equality uses the symmetry `Y -> -Y` in the outer supremum.  Explicitly,

\[
 N^*(Y)=\frac1{m^2}\sum_{v,a,w,b}
 Y_{(v,a),(w,b)}
 (U_v^*U_w)\otimes(U_a^*U_b),
\tag{34}
\]

up to a harmless transpose convention on `Y`.  Therefore (3) is equivalent to

\[
 \boxed{
 \sup_{\substack{Y=Y^*\\\|Y\|_2=1}}
 \|N^*(Y)\|_\infty\le\frac{A}{m}.}
\tag{35}
\]

The ambient real vector space of Hermitian scalar coefficients in `M_{m^2}` has dimension `m^4`,
and its unit sphere has intrinsic dimension `m^4-1`; both are fixed before `d->infinity`.  Since
`N^*` is unital completely positive,

\[
 \|N^*(Y-Y')\|_\infty
 \le\|Y-Y'\|_\infty\le\|Y-Y'\|_2.
\tag{36}
\]

An epsilon-net at the finite-model slack scale has size at most

\[
 \left(\frac{C_0}{\epsilon}\right)^{m^4},
 \qquad
 \epsilon\asymp\frac{9(c-1)}{m^2},
\tag{37}
\]

which is enormous in `m` but independent of `d`.  Thus pointwise convergence in `d`, followed by
a finite union, can genuinely uniformize (35).

The missing theorem is now sharply isolated:

> **Same-tuple two-leg scalar strong-norm lemma.**  For every fixed `m` and every fixed Hermitian
> `Y in M_(m^2)`, prove that the norm in (34), built from the same Haar tuple on both tensor legs,
> converges in probability to the corresponding `F_m x F_m` free/commuting coefficient norm,
> with the Collins--Youn two-copy bound; then uniformize over (37).

Bordenave--Collins tensor strong convergence with independently sampled tuples on the two legs
does not state this repeated-tuple lemma.  Conversely, (35) uses only fixed finite-dimensional
scalar coefficients.  It does not ask for an arbitrary matrix amplification growing with `d`, so
the physical/cb distinction remains intact.

## 10. Boundary of the result

- The Bell-frame calculation in `COMPLEX_HAAR_N2_BELL_FRAME_POTENTIAL_ANALYSIS_20260830.md`
  shows that one selected maximally entangled input is safe with high probability as `d->infinity`.
  It does not reduce the input entropy in (13).
- Equations (15), (18), and (27) close three tempting elementary routes: full pure-state net,
  low-rank net with generic Lipschitz tails, and unrestricted replica operator norm.
- Equations (19)--(21) state the minimum tail upgrade needed for a meaningful low-rank theorem.
- Equations (33)--(37) give the smallest all-input replacement presently visible.  Proving the
  same-tuple scalar strong-norm lemma would settle global one-layer `n=2` only; no inference to
  `n>=3` or the all-copy node is made.

## Primary sources and repository interfaces

1. Matthias Christandl, Robert Koenig, Graeme Mitchison, and Renato Renner, *One-and-a-half
   quantum de Finetti theorems*, arXiv:quant-ph/0602130, especially the sharper bosonic finite
   de Finetti scaling for symmetric support.
2. Jeronimo--Wu--Xu, arXiv:2608.02590, Corollary 3.7, for the `O(h/k)` trace-norm scale in the
   relevant symmetric/exchangeable formulation.
3. `PRODUCT_HAAR_PHYSICAL_SELF_PURITY_N2_ANALYSIS_20260830.md`, exact Gram, centered, and
   replica-separability formulations.
4. `COMPLEX_HAAR_N2_BELL_FRAME_POTENTIAL_ANALYSIS_20260830.md`, exact Bell-input Haar mean and
   tail.
5. `FINITE_DIMENSIONAL_UNBOUNDED_GAP_PROOF_20260829.md`, scalar coefficient compactness argument.
6. `FULL_SIZE_SELF_LEAKAGE_PARALLEL_ANALYSIS_20260830.md`, repeated-tuple and cb scope limits.
