# k-Sum L2 phase-14 proposer audit — multiple alternants and distributed NO boundary

Date: 2026-07-21  
Controlling node: `KSUM.B4b.L2.ALT.multipair.variable-pair-totals`  
Tier: proposer only; no independent review  
Scope: no DAG status change; this memo tests only the formula classes displayed below

## Decision

**B — the minimal quadratic-corrected multi-alternant fails an exact cross-moment gate.**
Distributing the NO coefficient among arbitrarily many boundary partitions cannot repair the
failure, because every orbit moment that queries both sides of a complementary pair vanishes on
the entire NO boundary.

There are two exact versions of the obstruction.

1. For two one-active-pair components, cancelling the degree-two target-pair moment leaves the
   degree-three residual

   `p_1 p_2 (s_1-s_2)/2`.

   If the active totals are made equal to kill it, the degree-four `(2,2)` residual is
   `p_1 p_2(p_1-p_2)`. Hence all three gates force the same unordered split, at which point the
   YES signed mass, and therefore the correlation, is zero.
2. The cheapest repair is to repeat one common active split in different numbers of pairs. It
   cancels every one-pair cross moment after the quadratic correction, but the degree-four
   two-pair injection row leaves the exact residual `ab(a-b)`. With more active-count levels, all
   cross-injection rows reduce to falling-factorial moments `(j)_rho`; the construction is then a
   univariate OR dual in the active-pair count. Consecutive levels have correlation `2^{-R}`, and
   arbitrary levels are capped at `R=O(sqrt K)` by the standard Chebyshev approximant to OR.

This is a scoped obstruction, not an obstruction to arbitrary joint-histogram weights.

## Exact cross moments and the boundary-blindness fact

Write an occupied unordered split as `tau=(r,u)`, with total `s=r+u` and product `p=ru`. For a
single queried complementary source-pair type, the exact phase-12 feature is

`A_{alpha,beta}(r,u)=((r)_alpha (u)_beta+(r)_beta (u)_alpha)/2`.

The first three cross features needed here are

```text
A_11(r,u) = p,
A_12(r,u) = p(s-2)/2,
A_22(r,u) = p(p-s+1).
```

They occur at query degrees `2,3,4`. For every NO split `(0,s)` all three are zero. More generally,
`A_{alpha,beta}(0,s)=0` whenever `alpha,beta>=1`. Consequently, if `B_lambda` is any NO histogram
associated with any partition `lambda` of `N` into `K` positive totals, then every cross moment in
this memo is zero on `B_lambda`. Changing the number of boundary partitions or their coefficients
cannot affect these equations.

## Attempt 1: two one-active-pair alternants

Take two legal YES profiles `Y_1,Y_2`. Profile `Y_i` has one active split
`tau_i=(r_i,u_i)` and `K-1` unsplit occupied pairs; their positive totals are chosen to make the
total occupancy exactly `N`. Let `s_i=r_i+u_i` and `p_i=r_i u_i>0`. Consider the most general
two-component formula with an arbitrary distributed boundary correction,

`W_raw = c_1 delta_{Y_1}+c_2 delta_{Y_2}+sum_lambda b_lambda delta_{B_lambda}`.

The zero-mass gate only says

`sum_lambda b_lambda=-(c_1+c_2)`.

The degree-two gate is boundary-blind and says `c_1p_1+c_2p_2=0`. Up to an overall scalar, its
unique nonzero solution is

`(c_1,c_2)=(p_2,-p_1)`.

The next cross row is therefore

```text
c_1 A_12(tau_1)+c_2 A_12(tau_2)
  = p_1 p_2 (s_1-s_2)/2.                         (14.1)
```

Thus genuinely different active totals fail already at query degree three. If `s_1=s_2=s` is
imposed as an explicit cubic correction, the degree-four row becomes

```text
c_1 A_22(tau_1)+c_2 A_22(tau_2)
  = p_1 p_2(p_1-p_2).                             (14.2)
```

Passing it forces `p_1=p_2`. The unordered integer split is determined by the roots of
`z^2-sz+p=0`, so `tau_1=tau_2`. Then `c_1+c_2=0`. Since all `Y_i` are YES and every `B_lambda` is
NO, zero total mass gives

`<W_raw,f_t>=2(c_1+c_2)=0`

for the `+1/-1` label convention. The normalized correlation is exactly zero. This disposes of
the minimal two-alternant formula before any pure-side moment rows need to be considered.

### Concrete `q=5` specialization

With `K=m=2`, let

```text
Y_a = {(1,a-1),(0,N-a)},
Y_b = {(1,b-1),(0,N-b)},       2<=a<b<=N-1.
```

The quadratic correction has coefficients `(b-1,-(a-1))`; its cubic residual is exactly

`(a-1)(b-1)(a-b)/2`.

Arbitrary coefficients on the NO partition histograms cannot change it. Before the cubic gate,
this raw measure could have normalized correlation as large as `(b-a)/(b-1)` and constant mass on
the larger-`C_t` atom (for example, `(a-1)/(b-1)=1/4` gives correlation `3/4` and tail mass `1/8`
under the minimum-`l1` boundary correction). Hence (14.1), rather than normalization or the tail
gate, is the first exact failure of this specialization.

## Attempt 2: repair all one-pair rows by repeating one split type

The smallest way around (14.1)-(14.2) is to use a common active split `tau=(r,u)` and let the number
of active copies vary. For `1<=j<=K`, define the legal profile `H_j` to have `j` copies of `tau` and
`K-j` unsplit occupied pairs. The unsplit totals absorb `N-j(r+u)`; legality requires

`N-j(r+u)>=K-j`

when `j<K`, and equality `N=j(r+u)` when `j=K`. Every one-pair cross feature is `j` times the same
number, so the two-level weights

`(c_a,c_b)=(b,-a)`, `1<=a<b<=K`,

kill the degree-two row and, simultaneously, all one-pair cross rows.

Now query `rho` distinct complementary source-pair types and request one occurrence from each side
of every type. The total query degree is `2rho`. The exact phase-12 orbit formula gives

```text
F_rho(H_j)
  = (j)_rho p^rho / ((m)_rho (N)_{2rho}).          (14.3)
```

At `rho=2`, the corrected two-level residual, after deleting the common positive denominator, is

```text
b(a)_2-a(b)_2 = ab(a-b),                           (14.4)
```

which is nonzero. Thus the repair fails at query degree four. At `q=5`, the only choice is
`(a,b)=(1,2)`; even before (14.4), its best possible normalized correlation is `1/2`.

## More than two levels: the exact formula and its hard boundary

For coefficients `c_j` supported on any active-count levels `J subseteq {1,...,K}`, all rows (14.3)
below query degree `D` require

`sum_{j in J} c_j (j)_rho=0` for `1<=rho<=R=floor((D-1)/2)`.       (14.5)

The NO coefficients can enforce zero total mass, but cannot enter (14.5). They also cannot improve
normalization: if `S=sum_j c_j`, then `sum_lambda |b_lambda|>=|S|`, and therefore

`corr(W) <= 2|S|/(sum_j |c_j|+|S|)`.               (14.6)

For the minimal consecutive support `j=1,...,R+1`, the unique alternant (up to scale) is

`c_j=(-1)^(R+1-j) binom(R+1,j)`.

It satisfies (14.5), has `|S|=1` and `sum|c_j|=2^(R+1)-1`, so even the optimal boundary placement
gives

`corr(W)=2^{-R}`.                                  (14.7)

Spreading the NO mass over more partitions only increases or preserves the denominator in (14.6).
For nonconsecutive levels, (14.5) is precisely the dual system for approximating the predicate
`1[j>0]` on `{0} union J`. A constant-error Chebyshev polynomial for OR on `{0,...,K}` has degree
`O(sqrt K)`. Hence no unit-`l1` solution of (14.5) can have correlation greater than `2/3` once
`R` exceeds a constant multiple of `sqrt K`.

At the large-`q` endpoint, `K=Theta(N^(2/3))` and the desired annihilation band has
`D=Theta(N^(2/3))`, so `R=Theta(K)`, far beyond `O(sqrt K)`. The same family can be perfectly legal
and can reach the required tail scale: choosing `s=Theta(N^(1/3))`, a balanced split has
`p=Theta(N^(2/3))`, and, on the divisibility-compatible subsequence `N=Ks`, `H_K` has
`C_t=Theta(N^(4/3))`. Likewise the `q=5` common-type specialization is legal on `N=2s`; for other
`N`, the unsplit-remainder construction is legal whenever `j<K`, while the `j=K` profile requires
an additional unequal-total repair and returns to (14.1)-(14.2). Thus legal high-tail instances
exist, but the displayed formula is not an all-`N` construction even before the decisive
correlation/moment failure.

## Gate ledger

| Gate | Result for the displayed formula class |
|---|---|
| legal orbits | PASS on the displayed occupancy/divisibility regimes; not an all-`N` family |
| zero total mass | PASS by choosing boundary coefficients with sum `-sum c_j` |
| unit `l1` | PASS by normalization, but normalization exposes (14.6) |
| correlation `>2/3` | FAIL for `q=5` repeated-type repair; FAIL asymptotically after the required active-count moment band |
| degree-two gate | PASS by the displayed two-component correction |
| degree-three gate | FAIL for distinct active totals by (14.1) |
| degree-four gate | FAIL after the minimal equal-total or repeated-type repairs by (14.2) or (14.4) |
| all low-degree moments | FAIL already on the cross subfamily; pure-side rows were not needed |
| constant high-`C_t` mass | compatible before the moment failure; explicit endpoint scalings are given above |
| distributed NO boundary | cannot affect any failing cross row and cannot improve `l1` |

## Exact hard boundary and untested remainder

The hard boundary established at proposer tier is:

> A bounded collection of one-active-pair alternants cannot survive degrees `2,3,4`; repairing it
> by a common split type and multiple active-count levels reduces the exact cross-moment system to
> a univariate OR dual, whose correlation is incompatible with the target band. Arbitrarily
> distributing the NO mass does not change either conclusion.

This does **not** cover a growing-rank family in which each profile contains several genuinely
different split types and the complete cross-injection tensors are moment-matched without becoming
a function of active-pair count. That would be a genuinely different mechanism. Under Rule 8, no
analysis of it was started here. Suggested node id, if the lead chooses to register it before any
commission:

`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.growing-rank-moment-design`.

No `PROVED`, `CERTIFIED*`, or `REFUTED` conclusion is claimed.
