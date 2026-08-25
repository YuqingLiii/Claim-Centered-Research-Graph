# k-Sum L2 phase-11 web feasibility memo — variable pair totals

Date: 2026-07-21  
Controlling node: `KSUM.B4b.L2.ALT.multipair.variable-pair-totals`  
Tier: proposer only; no independent review

## Decision

**C — insufficient information, with the missing object isolated.** The full variable-total simplex
survives all support-level primal attacks tried in this pass, but the web proposer did not construct
the required nonseparable signed annihilator.

This is not a hardness result. The node remains OPEN.

## Exact orbit family

Let `q=2m+1`, omit the fixed point `t/2`, and occupy exactly `K<=m` nonfixed complementary value
pairs. There is no carrier. For each occupied pair use an unordered split `{r,u}`, with
`0<=r<=u` and `r+u>=1`. The full-group orbit coordinate is the histogram `H_{r,u}` satisfying

`sum_{r<=u} H_{r,u}=K`,

`sum_{r<=u} (r+u) H_{r,u}=N`.

The target-pair count is

`C_t(H)=sum_{1<=r<=u} r u H_{r,u}`.

The exact NO boundary is the full partition simplex `H_{0,s}=c_s`, where
`sum_s c_s=K` and `sum_s s c_s=N`. Thus, unlike every earlier fixed-total family, there is one NO
orbit for every partition of `N` into `K` positive pair totals.

An endpoint-compatible specialization proposed by the web pass is

`K_*(N,q)=min{(q-1)/2, max{2, floor(N^(2/3)/64)}}`.

This gives `K_*=2` at `q=5` and `K_*=Theta(N^(2/3))` at `q=N` and the odd-rounded crossover
`q=Theta(N^(1/(6 eta)))` for every fixed `eta in (1/6,1/4]`.

## Actual target-pair support

For fixed `(N,K)`, the attainable positive set contains the entire integer interval

`[1,N-K]`.

Its maximum is

`floor((N-K+1)^2/4)=Theta(N^2)`

for the endpoint choices. Balanced total occupancies and balanced internal splits give

`C_t >= (N^2/K-K)/4`.

Hence for `K=Theta(N^(2/3))` the support reaches `Theta(N^(4/3))`, while at `q=5`, `K=2`, it reaches
`Theta(N^2)`.

## Primal feasibility checks

- A univariate Chebyshev test in `C_t` over the observed range costs `O(N)` query degree, not
  `o(D_*)` at the capped endpoints.
- Collision count satisfies `2D+2C_t=sum_{r<=u}(r+u)^2 H_{r,u}`. The right side varies from
  `Theta(N^2/K)` to `Theta(N^2)` even on the NO boundary, so collision count does not eliminate the
  pair-total degrees of freedom.
- Occupied-side count and minority mass characterize the target set on this promise but are not
  low-degree query polynomials; no smaller-degree composition was obtained.
- The first four occupancy/factorial sums retain independent total-histogram variables rather than
  collapsing the support to a one-dimensional statistic.
- Approximate scale selection near the critical total `N^(1/3)` was estimated to cost order
  `N^(2/3)`, so the phase-10 selector attack no longer gives a strict obstruction.
- Direct Johnson-walk pair search gives `O(N^(2/3))`, matching the desired capped order. At `q=5`,
  the `K=2` promise gives an `O(sqrt N)` search, again matching the required endpoint order.

These are proposer conclusions. In particular, failure to find an `o(D_*)` approximant is not a
lower bound.

## Minimum missing equations

The missing local artifact is one explicit joint-histogram signed kernel

`W_{N,q}((H_{r,u})_{r<=u})`

with constants `delta,c_0,c'>0`, uniform in `N,q`, satisfying:

1. `sum_H |W_{N,q}(H)|=1` and `sum_H W_{N,q}(H)=0`;
2. `sum_H f_t(H) W_{N,q}(H) > 2/3+delta`;
3. `sum_H W_{N,q}(H) F_gamma(H)=0` for every symmetrized factorial monomial of query degree
   `|gamma|<c_0 D_*(N,q)`;
4. `sum_{C_t(H)>=c D_*^2} |W_{N,q}(H)| >= c'`;
5. every histogram in the support is legal at the endpoint pair budgets.

The available Bun–Thaler collision mechanism provides a useful template—signed orbit masses,
invalid-parameter correction, shared-boundary cancellation—but no formula was found that lifts its
low-dimensional orbit parameter to this unbounded-dimensional joint partition/split histogram while
improving the known small-range exponent `1/6`.

## Sources used only for orientation

The web pass checked facts already represented in the project: the polynomial method, Ambainis's
`O(N^(2/3))` element-distinctness walk (quant-ph/0311001), ABI small-range claw
(arXiv:2103.16390), Tani's multisymmetric analysis, and the Bun–Thaler collision dual
(arXiv:1503.07261). No completion-tier fact is inferred from this memo.

