# k-Sum L2 phase-24 analytic feasibility audit — stratified boundary-jet Remez system

Date: 2026-07-21

Controlling node:
`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.moving-remez-cubature.label-aware-fekete-basis-exchange.continuation-seeded-block-fekete.continuum-limit-remez-support-flow.stratified-boundary-jet-remez-system`

Scope: analytic `q=5`, `K=2`, `D=Theta(sqrt N)` feasibility and discrete/asymptotic
duality bridge; no enlarged finite search and no DAG edit

Tier: independent proposer-tier audit; no Rule-7 review and no completion-tier claim

## Decision

**Decision B (scoped no-go for the four-stratum system as presently specified).**

The finite primal, dual, and complementary-slackness equations have a clean typed formulation.
There is also a precise sufficient lifting theorem: a stratified limiting annihilator with fixed
correlation and tail margins yields legal exact finite annihilators if its discretization has
uniformly small moment defect and that defect admits an `l1`-small exact correction. Together with
a global dual-recovery condition, this gives convergence of the finite strong-duality values.

However, the four named strata

```text
macroscopic bulk / C_t=Theta(N) normal layer / NO face / O(1) corners
```

are not a sequentially complete blow-up of the legal orbit space. Legal YES orbits occur at every
intermediate scale. In particular, `C_t=Theta(D)=Theta(sqrt N)` atoms are invisible both to the
normal coordinate `xi=D^2 C_t/N^2` and to the `O(1)` corner coordinates, even though actual
degree-`Theta(D)` falling-factorial rows sharply distinguish them. There is a second uncovered
family with `N << C_t << N^2`, lying between the normal layer and macroscopic bulk. Consequently
the four-stratum model cannot supply the uniform kernel convergence or the global dual inequality
on **every** legal orbit that a strong-duality bridge requires.

There is an independent exactness obstruction: convergence of leading sector kernels does not
allow approximate moment cancellation to be rounded into exact cancellation unless a quantitative
right-inverse/condition-number bound is proved. The WKB leading system can lose finite rank in its
limit. Thus leading kernels plus post-hoc rounding are insufficient even on the four retained
sectors.

This does **not** prove that the finite `q=5` dual object does not exist, and it does not rule out a
richer stratified construction. It rules out treating exactly the four listed sectors, with only
leading kernel matching, as a regime-complete primal/dual limit.

## 1. Exact finite typed primal and dual

Let `Omega_N` be the finite set of legal unordered `q=5`, `K=2` orbit histograms, and let

```text
E_N = R^{Omega_N},
E_N^* = R^{Omega_N},
```

paired by `<h,w>=sum_{H in Omega_N} h(H)w(H)`. Equip `E_N` with `l1` and `E_N^*` with `l_infinity`.
Let `V_N=V_{<D}` be the actual degree-`<D` orbit-row span and choose any row basis
`phi_{N,1},...,phi_{N,r_N}` containing the constant function. Nonzero rescaling of individual
rows is allowed and does not change the annihilator. Define

```text
A_N : E_N -> R^{r_N},
(A_N w)_j = sum_H phi_{N,j}(H) w(H),

A_N^* : R^{r_N} -> E_N^*,
(A_N^* c)(H) = sum_j c_j phi_{N,j}(H).                 (24.1)
```

Because the displayed rows are a basis, `A_N` has full row rank and is surjective;
`im(A_N^*)=V_N`. For the label `f_N=+1` on YES and `f_N=-1` on NO, finite-dimensional LP duality
gives

```text
epsilon_N
 = max { <f_N,w> : w in E_N, A_N w=0, ||w||_1<=1 }
 = min { ||f_N-A_N^*c||_infinity : c in R^{r_N} }.     (24.2)
```

The first program is the signed annihilator; the second is uniform approximation by the actual
orbit span. If `f_N` is not in `V_N`, an optimal nonzero `w_N` can be oriented so that
`<f_N,w_N>=epsilon_N` and has `||w_N||_1=1`. Since the constant row lies in `V_N`,
`A_Nw_N=0` also gives exact zero total mass.

If `(w_N,c_N)` is an optimal pair and
`e_N=f_N-A_N^*c_N`, equality in Holder's inequality gives the exact complementarity law

```text
e_N(H)=epsilon_N sign(w_N(H)) whenever w_N(H)!=0,
|e_N(H)|<=epsilon_N for every H in Omega_N.             (24.3)
```

Conversely, (24.3), `A_Nw_N=0`, and `||w_N||_1=1` certify equality in (24.2). This is the typed
version of the finite Remez equations. The required high-tail gate is a separate property of the
primal witness,

```text
sum_{H:C_t(H) in [aN,bN]} |w_N(H)| >= c_0             (24.4)
```

for fixed `0<a<b<infinity` (or the project's chosen one-sided threshold). It is not implied by
strong duality or complementarity.

## 2. A correctly typed stratified limiting pair

Suppose a proposed blow-up is a compact Hausdorff space

```text
X = X_bulk disjoint-union X_layer disjoint-union X_NO disjoint-union X_corner.   (24.5)
```

The sectors must remain topologically disjoint. Then the limiting label `f_infinity`, equal to
`+1` on YES sectors and `-1` on the NO sector, is continuous. Gluing the YES layer to its NO
boundary in the topology would recreate the Phase-23 discontinuity and force the uniform dual
error to be at least one.

Let `K_theta in C(X)` be all limiting falling-factorial kernels, including every required jet and
birth coordinate, and define the closed feature space

```text
V_infinity = closure(span({1} union {K_theta : theta in Theta})) in C(X).        (24.6)
```

The limiting primal lives in `M(X)=C(X)^*`, the finite signed regular measures, not in a space of
ordinary bulk densities:

```text
epsilon_infinity
 = sup { integral f_infinity dnu : nu annihilates V_infinity,
                                      ||nu||_TV<=1 }
 = dist_C(X)(f_infinity,V_infinity).                    (24.7)
```

The equality is exact Hahn-Banach duality for the quotient `C(X)/V_infinity`; it needs no informal
exchange of limits. If a primal/dual optimum `(nu,Q)` exists, equality again implies

```text
f_infinity-Q=epsilon_infinity sign(dnu/d|nu|)  |nu|-almost everywhere,
|f_infinity-Q|<=epsilon_infinity on X.          (24.8)
```

Matching between strata belongs in the definition of the kernels and of `V_infinity`, not in a
topological identification that makes `f_infinity` discontinuous. This distinction is necessary
for a meaningful limiting strong-duality pair.

Equation (24.7) by itself does not prove the tail gate. A candidate must additionally satisfy

```text
|nu|(T_layer)>=c_0+gamma,                               (24.9)
```

where `T_layer` is a buffered compact subset corresponding to `C_t in [aN,bN]` and `gamma>0` is a
fixed margin.

## 3. Sufficient discrete lifting theorem

The following condition is sufficient to turn a stratified solution into the requested exact
finite object.

For each `N`, choose a normed moment space `Y_N=R^{r_N}` and use the exact map
`A_N:E_N->Y_N` from (24.1), with whatever nonzero row normalizations make the limiting kernels
finite. Assume a limiting candidate `nu` with

```text
||nu||_TV=1,
nu annihilates V_infinity,
integral f_infinity dnu >= 2/3+gamma,
|nu|(T_layer)>=c_0+gamma.                               (24.10)
```

Assume there are legal atomic discretizations `tilde w_N in E_N` and linear correction maps
`R_N:Y_N->E_N` such that

```text
||tilde w_N||_1 -> 1,
<f_N,tilde w_N> -> integral f_infinity dnu,
tail(tilde w_N) -> |nu|(T_layer),

A_N R_N y = y for every y in Y_N,
||R_N A_N tilde w_N||_1 -> 0.                           (24.11)
```

Then

```text
w_N^raw = tilde w_N - R_N A_N tilde w_N                (24.12)
```

is supported on legal finite orbits and satisfies `A_N w_N^raw=0` **exactly**. After division by
`||w_N^raw||_1`, it has zero mass, unit `l1`, all degree-`<D` moments zero, correlation strictly
above `2/3`, and tail at least `c_0` for every sufficiently large `N`. Indeed, label correlation
and tail absolute mass each change by at most the `l1` norm of the correction, while the
normalizing denominator tends to one.

A convenient stronger, checkable version of the last line in (24.11) is

```text
||A_N tilde w_N||_{Y_N} <= eta_N,
||R_N||_{Y_N->l1} eta_N -> 0.                           (24.13)
```

This is the missing condition-number gate. Approximate sector cancellation without (24.13) does
not imply exact finite cancellation.

To bridge not merely one witness but the strong-duality **value**, one also needs global dual
recovery: for every `Q in V_infinity` and every `delta>0`, there must be `p_N in V_N` such that

```text
sup_{H in Omega_N} |(f_N-p_N)(H)
                    -(f_infinity-Q)(iota_N(H))| <= delta+o_N(1),  (24.14)
```

for a label-preserving embedding `iota_N` defined on every legal orbit. Primal recovery (24.11) gives
`liminf epsilon_N>=epsilon_infinity`; (24.14) gives
`limsup epsilon_N<=epsilon_infinity`. Hence the finite strong-duality values converge and (24.8)
is a genuine asymptotic complementarity law rather than a formal analogy.

## 4. Why leading kernels do not provide exactness

Uniform convergence of rescaled rows is not enough to prove (24.11). The elementary matrices

```text
B_N = [[1,1],[0,delta_N]],   delta_N>0, delta_N->0,      (24.15)
```

have trivial finite kernels, while their entrywise limit has kernel spanned by `(1,-1)`. Thus a
perfect limiting annihilator can have no finite exact lift. Equivalently, every right inverse of
`B_N` has norm at least of order `1/delta_N`.

The same logical danger is present in the Phase-23 WKB equations: a common leading exponential
phase can cancel while order-one, polynomially small, or exponentially small falling-factorial
terms retain the finite rank. A valid sector construction must either give exact identities before
the limit or prove the quantitative correction bound (24.13). “Solve the leading system and round”
does neither.

## 5. The four listed strata do not cover the legal orbit space

Consider the legal `q=5`, `K=2` histograms

```text
H_N(t) = {(1,t),(0,N-t-1)},       1<=t<=N-2.             (24.16)
```

They have `C_t(H_N(t))=t`. Take `D=kappa sqrt N+O(1)` and `t_N=lambda D` with fixed
`lambda>0`. Then

```text
C_t=Theta(sqrt N),
xi=D^2 C_t/N^2=Theta(N^{-1/2})->0,                       (24.17)
```

but the split occupancy `t_N` diverges. These atoms are not on the NO face, not `O(1)` corners,
not in the `xi=Theta(1)` normal layer, and not in macroscopic bulk.

They cannot be harmlessly collapsed into the corner or NO sector. Fix `0<alpha<1`. For the
degree-`a=floor(alpha D)>=2` one-slot query, the exact feature is

```text
A_{0,a}(1,t)=((t)_a+(1)_a)/2=(t)_a/2.                   (24.18)
```

It is exactly zero for `t<a` and nonzero for `t>=a`. Hence two sequences with
`t_N=(alpha/2)D` and `t_N=2alpha D` both have `xi->0` and both escape every `O(1)` corner chart,
yet an actual allowed row distinguishes them exactly. The proposed four-sector topology either
has no destination for these sequences (so it is not compact/exhaustive) or forces them into the
same NO/corner boundary while losing a genuine finite feature direction. Recovering that lost
direction would require another jet scale and the stable-exactor analysis of Section 3; it is not
part of the present four-sector system.

There is also a missing super-normal family. Let

```text
G_N = {(floor(N^(3/4)),floor(N^(3/4))),
       (0,N-2 floor(N^(3/4)))}.                          (24.19)
```

Then `C_t(G_N)=Theta(N^(3/2))`, so `y=C_t/N^2->0` while `xi=Theta(N^(1/2))->infinity`.
It is neither `y=Theta(1)` bulk nor `xi=Theta(1)` normal layer. More generally the legal grid has
families at `C_t=N^beta` for a continuum of `0<beta<2`.

The first missing family already suffices for the scoped no-go. Even if a primal witness chooses
support only in the four named sectors, a Remez dual certificate must satisfy its global inequality
on the orbits (24.16). Thus the omission cannot be repaired by declaring intermediate orbits
inactive.

## 6. Gate ledger

| obligation | result |
|:---|:---|
| exact finite primal/dual types | PASS: (24.1)-(24.2) |
| finite complementarity/equioscillation | PASS: (24.3) |
| meaningful stratified strong duality | PASS conditionally when the disjoint blow-up is compact and `V_infinity` is closed as in (24.5)-(24.8) |
| `l1=1`, exact annihilation, correlation and tail lift | SUFFICIENT CONDITION: (24.10)-(24.13) |
| exactness from leading WKB kernels alone | FAIL: rank-loss example (24.15) |
| coverage of every legal `q=5` orbit by the four strata | FAIL: (24.16)-(24.19) |
| global dual recovery on every legal orbit | FAIL for the present four-sector topology by (24.18) |
| constant `C_t=Theta(N)` residual tail | compatible with the normal layer, but no candidate measure or bound is supplied |
| formula-defined correlation above `2/3` | OPEN; no candidate solving (24.10) is supplied |
| exact lattice realization | OPEN; requires the stable exactor gate (24.13) or an exact pre-limit identity |

## 7. Scoped conclusion and one untested escape name

The four-stratum proposal is structurally compatible with a typed Hahn-Banach primal/dual pair,
and (24.10)-(24.13) state a sufficient route from such a pair to legal exact finite annihilators.
But exactly those four strata are not regime-complete. They miss query-visible intermediate
occupancy scales, so they cannot support the global dual recovery needed to transfer strong
duality. Leading-order matching also lacks the quantitative exactor required for exact finite
moments.

The underlying finite route remains open. A distinct possible repair is an **iterated multiscale
boundary compactification with a uniformly stable exactor**. This phrase is only a name generated
by the audit; no construction, kernel, feasibility calculation, or test of that repair was
performed. Under DAG Rule 8 it must be registered before any future work.

No `PROVED`, `CERTIFIED*`, `NUMERICAL`, or `REFUTED` status is claimed.
