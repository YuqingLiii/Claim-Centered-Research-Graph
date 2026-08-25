# k-Sum L2 balanced positive-split scalar-selector obstruction

Date: 2026-07-22

Controlling node:
`KSUM.B4b.L2.ALT.balanced-positive-split-weighted-dual-composition`

Scope: exactly the balanced component of the Phase-21/Phase-30 `q=N` support, with its `U`
total-two unit pair-types, `M` nearly equal bulk totals, and every positive unordered bulk split.
The dense component and any different balanced support are outside scope.

Tier: exact proposer-tier formula obstruction.  No numerical exponent inference is used, and no
completion-tier DAG status is claimed before a fresh independent Rule-7 review.

## Decision

**The exact candidate obstruction works.**  A degree-at-most-five polynomial in the slot total
separates the unit slots from every allowed bulk total.  It turns the full balanced histogram into
two actual multisymmetric statistics:

\[
 A=\hbox{number of active unit slots},
 \qquad
 G=\hbox{total target count contributed by active bulk slots}.
\tag{1}
\]

Their support has two simultaneous gaps:

\[
 A\in\{0,1,\ldots,U\},
 \qquad
 G\in\{0\}\cup[g_N,L^2],
 \qquad
 g_N=(1+o(1))\sqrt L.
\tag{2}
\]

Here the second interval is a containment, not a claim that every integer up to `L^2` is attained.
The lower gap is exact: `g_N` is the smallest positive value of `G`.

Anchored Chebyshev zero tests of degrees

\[
 n_A=\lfloor L^{1/3}\rfloor,
 \qquad
 n_G=\lfloor L^{7/8}\rfloor
\tag{3}
\]

produce one global histogram polynomial `Q_N` that equals one on every NO orbit and is `o(1)`
uniformly on every YES orbit.  Its strict actual weight satisfies

\[
 \operatorname{weight}(Q_N)
 \le 7(n_A+n_G)<D=\lfloor L/2\rfloor
\tag{4}
\]

for all sufficiently large admissible odd `N`, with every floor retained.  Consequently every
signed law `W` on this balanced support having zero mass, unit `l1`, and annihilating all actual
rows of weight `<D` obeys

\[
 |\langle W,1-2\mathbf1_{\rm NO}\rangle|=o(1).
\tag{5}
\]

In particular it cannot have correlation strictly above `2/3`.  This is a formula-level scoped
obstruction to the registered balanced-support node.  It does not apply to the full Phase-30
balanced/dense mixture: dense totals range far beyond the five roots used below.

## 1. Exact balanced support and the allowed bulk-total set

Let `N` tend to infinity through sufficiently large odd integers, put `q=N`, and define

\[
 \begin{aligned}
 m&=(N-1)/2,\\
 L&=\lfloor N^{2/3}\rfloor,\\
 D&=\lfloor L/2\rfloor,\\
 U&=\lceil2N^{1/3}\rceil,\\
 M&=L-U,\\
 S&=N-2U,\\
 a&=\lfloor S/M\rfloor,\\
 h&=S-Ma.
 \end{aligned}
\tag{6}
\]

The balanced bulk-composition set is

\[
 \mathcal C_N=
 \left\{s\in\mathbb Z^M:
 s_i=a+\delta_i,\ \delta_i\in\{-2,-1,0,1,2\},\
 \sum_i\delta_i=h\right\}.
\tag{7}
\]

It is nonempty because `0<=h<M`: take `h` deviations equal to one and all remaining deviations
zero.  Define the set of bulk totals that actually occur by

\[
 K_N=\{k\in\mathbb Z:\exists s\in\mathcal C_N,\ \exists i\in[M],\ s_i=k\}.
\tag{8}
\]

Then

\[
 \varnothing\ne K_N\subseteq\{a-2,a-1,a,a+1,a+2\},
 \qquad |K_N|\le5.
\tag{9}
\]

In fact equality holds in (9) once `M>=3`.  Fix any
`d in {-2,-1,0,1,2}`.  The remaining `M-1` deviations must sum to `h-d`; for
`0<=h<M` and `M>=3`, this integer lies in `[-2(M-1),2(M-1)]`.  Every integer in that interval is
a sum of `M-1` integers from `{-2,-1,0,1,2}`.  Thus every deviation `d` occurs in some composition,
so `K_N={a-2,a-1,a,a+1,a+2}` for all sufficiently large `N`.

The `U` unit pair-types all have total two.  Each is inactive in state `(0,2)` or active in state
`(1,1)`.  Conditional on a bulk total `s_i`, a bulk slot is inactive in state `(0,s_i)` or active
in any unordered split `(r,s_i-r)` with `1<=r<=floor(s_i/2)`.  The law's probabilities are
irrelevant to the support obstruction; only strict positivity of every stated choice is used.

The asymptotics in (6) give

\[
 L=N^{2/3}+O(1),\quad
 U=(2+o(1))\sqrt L,\quad
 M=(1-o(1))L,\quad
 S=(1-o(1))N,
\tag{10}
\]

and therefore

\[
 a=\left\lfloor\frac SM\right\rfloor=(1+o(1))\sqrt L.
\tag{11}
\]

In particular `min K_N>=a-2>2` for all sufficiently large `N`.  This all-large condition is
essential: if total two were also a bulk total, no polynomial could simultaneously take value one
there as a unit marker and zero there as a bulk marker.  That collision does not occur in the
claimed asymptotic domain.

## 2. One globally coherent interpolation polynomial

Define

\[
 w_N(s)=\prod_{k\in K_N}\frac{s-k}{2-k}.
\tag{12}
\]

Every denominator is a nonzero integer by `min K_N>2`.  The polynomial is fixed by `N` and the
support definition, not by a sampled composition, an ordering, a latent component label, or an
inactive slot's forgotten prospective split.  It has degree `|K_N|<=5` and obeys exactly

\[
 w_N(2)=1,
 \qquad
 w_N(k)=0\quad(k\in K_N).
\tag{13}
\]

For a histogram `H`, write its slot multiplicities as `H_(r,u)` and define

\[
 \begin{aligned}
 A(H)&=\sum_{r,u}H_{r,u}\,ru\,w_N(r+u),\\
 G(H)&=\sum_{r,u}H_{r,u}\,ru\,[1-w_N(r+u)].
 \end{aligned}
\tag{14}
\]

These are unordered-histogram functions.  Unused or inactive pair-types have `ru=0`, so the value
of `w_N` away from the occupied positive splits is harmless.  On the stated support, (13) gives

\[
 A=\sum_{i\text{ unit}}x_i,
 \qquad
 G=\sum_{i\text{ bulk}}x_i,
 \qquad
 x_i=r_i(s_i-r_i)\ \text{if active},
\tag{15}
\]

with `x_i=0` if inactive.  Thus no unit/bulk label needs to survive the histogram pushforward:
the disjoint total values make (14) perform that split globally.  Also `A+G=sum_i x_i` identically.

## 3. Exact support gaps

An active unit slot has `x_i=1`.  Hence

\[
 A\in\{0,1,\ldots,U\}.
\tag{16}
\]

Every value in (16) is attained: activate any prescribed number of unit slots and leave every
other slot inactive.

For a bulk total `k`, the positive products are `r(k-r)`,
`1<=r<=floor(k/2)`.  This function is increasing over the stated range, so its smallest value is
`k-1`, attained at `r=1`.  Put

\[
 g_N=\min_{k\in K_N}(k-1)=a-3.
\tag{17}
\]

If `G>0`, at least one active bulk slot contributes at least `g_N`, while if all bulk slots are
inactive then `G=0`.  Conversely, choose a composition containing a total that minimizes (17),
activate only that bulk slot with split `(1,k-1)`, and leave all other slots inactive.  Therefore
`g_N` is the exact smallest positive value of `G`.  Equations (9) and (11) give

\[
 g_N=a-3=(1+o(1))\sqrt L,
\tag{18}
\]

so in particular `g_N>=sqrt(L)/2` for all sufficiently large `N`.

For the upper bound, every positive bulk split obeys `r(s_i-r)<=s_i^2/4`.  Since
`sum_i s_i=S` and `s_i<=S/M+2`,

\[
 \begin{aligned}
 G
 &\le\frac14\sum_{i=1}^M s_i^2\\
 &\le\frac14\left(\frac SM+2\right)S\\
 &=\frac{S^2}{4M}+\frac S2
 =\left(\frac14+o(1)\right)L^2
 \le L^2
 \end{aligned}
\tag{19}
\]

for all sufficiently large `N`.  Combining (16)--(19),

\[
 A=0\ \hbox{or}\ 1\le A\le U,
 \qquad
 G=0\ \hbox{or}\ g_N\le G\le L^2.
\tag{20}
\]

Moreover a support point is NO exactly when `A=G=0`; every YES point is unit-only, bulk-only, or
mixed according as `(A>0,G=0)`, `(A=0,G>0)`, or `(A>0,G>0)`.

## 4. The two anchored Chebyshev factors

For real `0<ell<B` and integer `n>=1`, define

\[
 \mathcal Z_{n;\ell,B}(t)=
 \frac{T_n((B+\ell-2t)/(B-\ell))}
      {T_n((B+\ell)/(B-\ell))}.
\tag{21}
\]

The denominator is positive, `mathcal Z_(n;ell,B)(0)=1`, and for every real
`t in [ell,B]`,

\[
 |\mathcal Z_{n;\ell,B}(t)|
 \le\delta(n;\ell,B)
 :=\operatorname{sech}\!\left(
 n\operatorname{arcosh}\frac{B+\ell}{B-\ell}
 \right).
\tag{22}
\]

The exact identity

\[
 \operatorname{arcosh}\frac{B+\ell}{B-\ell}
 =2\operatorname{artanh}\sqrt{\ell/B}
 \ge2\sqrt{\ell/B}
\tag{23}
\]

will give the attenuation rates.

With the degrees in (3), set

\[
 Q_A=\mathcal Z_{n_A;1,U}(A),
 \qquad
 Q_G=\mathcal Z_{n_G;g_N,L^2}(G),
 \qquad
 Q_N=Q_AQ_G.
\tag{24}
\]

All denominators in (24) are positive for all large `N`, since `1<U` and
`0<g_N<L^2`.  By (10), (18), (22), and (23),

\[
 \begin{aligned}
 \delta_A
 &:=\delta(n_A;1,U)
 \le2\exp(-2n_A/\sqrt U)
 =\exp[-\Omega(L^{1/12})],\\
 \delta_G
 &:=\delta(n_G;g_N,L^2)
 \le2\exp(-2n_G\sqrt{g_N}/L)
 =\exp[-\Omega(L^{1/8})].
 \end{aligned}
\tag{25}
\]

The floors do not affect these exponents: for all large `L`,
`n_A>=L^(1/3)/2`, `n_G>=L^(7/8)/2`, `U<=4sqrt(L)`, and
`g_N>=sqrt(L)/2`.

On NO, both arguments in (24) are zero and hence `Q_N=1`.  In the three YES regimes, (20)--(22)
give

\[
 |Q_N|\le
 \begin{cases}
 \delta_A,&A>0,\ G=0,\\
 \delta_G,&A=0,\ G>0,\\
 \delta_A\delta_G,&A>0,\ G>0.
 \end{cases}
\tag{26}
\]

Therefore

\[
 \sup_{\rm YES}|Q_N|
 \le\varepsilon_N:=\max(\delta_A,\delta_G)=o(1).
\tag{27}
\]

This checks the unit-only, bulk-only, and mixed regimes separately.  No probabilistic tail estimate
is being substituted for a support-wide statement.

## 5. Full actual multisymmetric membership and strict weight

On the Phase-30 orbit space, write

\[
 p_{(j,b)}=\sum_i s_i^j x_i^b,
 \qquad
 \operatorname{weight}(p_{(j,b)})=j+2b.
\tag{28}
\]

If `w_N(s)=sum_(j=0)^k c_j s^j`, where `k=|K_N|<=5`, then (14) becomes

\[
 A=\sum_{j=0}^k c_jp_{(j,1)},
 \qquad
 G=p_{(0,1)}-A.
\tag{29}
\]

Thus every term of `A` or `G` has actual weight at most `k+2<=7`.  Expanding (24), every monomial
in `Q_N` has actual weight at most

\[
 7(n_A+n_G).
\tag{30}
\]

This is membership in the full actual multisymmetric row space, not merely a polynomial on ordered
latent coordinates: (29) uses global polarized power sums, and the Phase-30 definition includes
all products of those generators below the strict total-weight cutoff.  Equivalently, the usual
collision-partition expansion turns each product into actual injection rows.  In the range here,
the number of power-sum factors is at most `n_A+n_G=o(L)<m`, and the total query weight is below
`D<N`, so all falling-factorial normalizations and injection rows are in their stable nonzero
range.

The floor-sensitive strict inequality can be made explicit.  If `L>=56^8`, then

\[
 7L^{7/8}\le L/8,
 \qquad
 7L^{1/3}\le L/8.
\tag{31}
\]

Hence

\[
 7(n_A+n_G)
 \le7(L^{1/3}+L^{7/8})
 \le L/4
 <\lfloor L/2\rfloor=D.
\tag{32}
\]

The last inequality is strict for `L>4`.  Therefore `Q_N` belongs to the complete actual
weight-`<D` space for every sufficiently large admissible odd `N`.  Large interpolation
coefficients do not change this conclusion: row membership and the support identities depend on
polynomial weight and exact values, not coefficient norm.

## 6. Arbitrary-`l1` dual obstruction

Let `W` be any real signed law on the unordered balanced-support histograms such that

\[
 \sum_H|W(H)|=1,
 \qquad
 \sum_HW(H)P(H)=0
 \quad\hbox{for every actual }P\hbox{ of weight }<D.
\tag{33}
\]

The constant row is included, so (33) implies `sum_H W(H)=0`.  By Section 5 it also implies
`sum_H W(H)Q_N(H)=0`.  Put `b=1_NO` and `f=1-2b`.  Since `Q_N=1` on NO,

\[
 \begin{aligned}
 |\langle W,f\rangle|
 &=2\left|\sum_{H\in\mathrm{NO}}W(H)\right|\\
 &=2\left|\sum_{H\in\mathrm{YES}}W(H)Q_N(H)\right|\\
 &\le2\varepsilon_N\sum_{H\in\mathrm{YES}}|W(H)|\\
 &\le2\varepsilon_N=o(1).
 \end{aligned}
\tag{34}
\]

This bound is independent of how `W` was constructed, of the signs inside each histogram fiber,
and of the relative absolute mass assigned to the unit-only, bulk-only, and mixed regimes.  In
particular, it applies to nonfactorizable coefficient laws and to arbitrary unit-`l1`
normalizations.

For all sufficiently large `N`, the right side of (34) is strictly below `2/3`.  The registered
balanced support therefore cannot supply the required constant-correlation dual witness.

## 7. Gate ledger

| obligation | result |
|:---|:---|
| exact Phase-30 balanced support and all-large odd-`N` legality | **PASS** |
| one global allowed-total set `K_N` | **PASS**, nonempty and of size at most five |
| interpolation denominators | **PASS** once `min K_N>2` |
| histogram measurability after forgetting unit/bulk labels | **PASS** by (14) |
| `A` support | **PASS**, exactly every integer `0,...,U` |
| exact positive `G` gap | **PASS**, minimum `g_N=a-3=(1+o(1))sqrt(L)` |
| global positive `G` upper bound | **PASS**, `G<=L^2` |
| unit-only YES regime | **PASS**, attenuated by `Q_A` |
| bulk-only YES regime | **PASS**, attenuated by `Q_G` |
| mixed YES regime | **PASS**, attenuated by both factors |
| complete actual multisymmetric membership | **PASS** by (28)--(30) |
| strict weight `<D` with all floors | **PASS** by (31)--(32) |
| arbitrary signed law with unit `l1` | **PASS** by (34) |
| correlation strictly above `2/3` | **IMPOSSIBLE on this support**, proposer-tier pending review |
| full Phase-30 balanced/dense mixture | **OUT OF SCOPE** |
| every balanced positive-split support | **NOT CLAIMED** |

## 8. Scoped conclusion

The five-value bulk-total restriction creates a low-weight statistic that was absent from the
single scalar `C=sum_i x_i`: total two identifies unit slots exactly, while the fixed root set
identifies all bulk slots exactly.  After this split, the unit activation count has range only
`Theta(sqrt(L))`, and the first positive bulk target count is already `Theta(sqrt(L))` even though
its upper range is `Theta(L^2)`.  The two corresponding Chebyshev degrees are sublinear enough that
their product has strict actual weight below `D=floor(L/2)`.

Thus the registered Phase-30 balanced support collapses to the pair `(A,G)` for the zero-test
purpose, and one actual formula separates NO from its entire YES support with vanishing error.
No coefficient law on this exact support can retain constant normalized correlation while
annihilating every row below `D`.

The conclusion is deliberately scoped.  It neither obstructs the dense component nor a future
balanced support whose bulk totals occupy a growing set that cannot be removed by constant-degree
interpolation.  No successor calculation is performed here.
