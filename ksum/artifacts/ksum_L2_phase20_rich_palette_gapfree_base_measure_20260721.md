# k-Sum L2 phase-20 proposer analysis — rich-palette gap-free `q=N` base measure

Date: 2026-07-21  
Controlling node:
`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.multiscale-gapfree-base-measure`  
Tier: proposer only; no independent review and no DAG status claim

## Decision

**B — a formula-defined law with `Omega(N^(1/3))` distinct positive one-slot products is still
sharply falsified.**  The law below retains the phase-19 gap-free unit layer and random exact bulk
total compositions, but replaces the logarithmic split palette by *every* unordered split
`1<=r<=floor(s/2)` of each bulk total.  Its support therefore has `Omega(N^(1/3))` distinct
one-slot products, small positive `C_t` through the high scale, a distributed NO boundary, and
constant high-tail base mass.

Exact interpolation of local activity now costs `Theta(N^(1/3))`, so the phase-19 interpolation
argument no longer gives `o(N^(1/3))` local degree.  However, the positive bulk products all lie
in one interval

```text
[Theta(N^(1/3)), Theta(N^(2/3))].
```

A Chebyshev polynomial approximates local activity on that interval using only
`O(N^(1/6) log N)` degree; a factor `(1-x)` simultaneously handles the unit product `x=1`
exactly.  Composing this robust local approximation with a degree-`O(sqrt(K))` boundary
discriminator produces an actual orbit-row polynomial of query degree

```text
O(N^(1/2) log N)=o(N^(2/3)).
```

Thus at every target cutoff `D=Theta(N^(2/3))`, the phase-16 projection residual is zero or its
normalized correlation is at most `1/2`.  Rich cardinality alone is insufficient: the local
positive moment types must also avoid a low-degree *approximate* separator from zero.

## 1. Exact legal random-total support

Take sufficiently large odd `N`, put `q=N`, and define

```text
m=(N-1)/2,
L=floor(N^(2/3)),
U=floor(L/4),
M=L-U,
N_bulk=N-2U,
a=floor(N_bulk/M),
h=N_bulk-Ma.                                                 (20.1)
```

Use `U` unit pair-types of total `2`.  Draw the ordered totals of the other `M` bulk pair-types
uniformly from

```text
C_bulk={s in Z^M:
        s_i=a+delta_i, delta_i in {-2,-1,0,1,2},
        sum_i delta_i=h}.                                    (20.2)
```

Since `0<=h<M`, (20.2) is nonempty by taking `h` deviations equal to `1` and the rest `0`.  Every
profile has

```text
2U+sum_i s_i=N,
K=U+M=L=Theta(N^(2/3))<=m.                                  (20.3)
```

Also `a=Theta(N^(1/3))`; for all sufficiently large `N`, `a-2>=6`, so all totals are positive and
the unit total `2` is disjoint from the five possible bulk totals.  This proves legality and
rounding for every sufficiently large odd `N`, without a reservoir or divisibility subsequence.

## 2. Rich split law and explicit histogram mass

Each unit pair independently takes

```text
(0,2) with probability 1/2,
(1,1) with probability 1/2.                                 (20.4)
```

Conditional on a bulk total `s`, independently choose

```text
(0,s)                         with probability 1/2,
(r,s-r), 1<=r<=floor(s/2)    each with probability
                               1/(2 floor(s/2)).             (20.5)
```

Then forget slot ordering.  This is one closed positive law.  If `H_tau` denotes split-state
multiplicity, its exact pushforward mass is

```text
pi_(N,N)(H)
 = [U!/(H_(0,2)!H_(1,1)!)] [M!/product_(tau bulk)H_tau!]
   / |C_bulk| * (1/2)^U
   * product_(tau bulk) w_(s(tau))(r(tau))^(H_tau),          (20.6)

w_s(0)=1/2,
w_s(r)=1/(2 floor(s/2)), 1<=r<=floor(s/2).                  (20.7)
```

The total ranges are disjoint, so the factors in (20.6) are unambiguous.  Every ordered
representative has the displayed product weight, proving normalization and strict positivity on
the stated support.

The law is nonproduct because the random bulk totals have nonzero marginal variance while their
sum is fixed by (20.2).  The NO boundary is distributed over all bulk total histograms arising
from (20.2).  Profiles are genuinely multidimensional: bulk totals and individual split ratios
vary, and neither `C_t` nor an activation count determines the histogram.

## 3. Gap-free small layer, rich one-slot types, and high tail

Activating exactly `j` unit pairs and leaving every bulk pair inactive gives

```text
C_t=j,                 0<=j<=U.                             (20.8)
```

Thus the positive support contains every integer from `1` through
`U=Theta(N^(2/3))`, including the smallest possible value.

For a fixed bulk total `s`, the products

```text
x_r=r(s-r),             1<=r<=floor(s/2),                  (20.9)
```

are strictly increasing in `r`.  The support contains the total `s=a`, so it contains at least
`floor(a/2)=Omega(N^(1/3))` distinct positive one-slot product values.  Across all bulk totals,

```text
a-3 <= x_r <= (a+2)^2/4.                                   (20.10)
```

This also verifies that exact activity interpolation is genuinely expensive here.  If a
polynomial `Q` satisfies `Q(0)=0` and `Q(c)=1` on all `J` distinct positive product values, then
`Q-1` has `J` distinct roots but is not the zero polynomial; hence `deg Q>=J=Omega(N^(1/3))`.

The base law also has a constant high tail.  For any bulk total, the probability of being active
with `r>=ceil(s/4)` is bounded below by a fixed constant (for example `1/6`) for all large `s`.
These events are independent conditional on the totals, and every such slot contributes at least
`s^2/8 >=(a-2)^2/8`.  A Chernoff bound therefore gives

```text
Pr[C_t >= (M/12)(a-2)^2/8] >=1-exp(-M/48).                 (20.11)
```

The lower threshold is `Theta(N^(4/3))`; the deterministic upper bound is also
`O(M(a+2)^2+U)=O(N^(4/3))`.  Hence base mass at the required scale tends to one while the support
simultaneously reaches `C_t=1`.

## 4. A low-degree approximate local-activity polynomial

Let `x=ru` be a one-slot product and define

```text
Lambda_N=a-3,
B_N=(a+2)^2/4,
epsilon_N=1/(10L).                                         (20.12)
```

All positive bulk products lie in `[Lambda_N,B_N]`.  Map this interval to `[-1,1]`:

```text
y(x)=(B_N+Lambda_N-2x)/(B_N-Lambda_N),
y_0=y(0)=(B_N+Lambda_N)/(B_N-Lambda_N)>1.                   (20.13)
```

Set

```text
d_N=ceil(arcosh((B_N+1)/epsilon_N)/arcosh(y_0)),
R_N(x)=T_(d_N)(y(x))/T_(d_N)(y_0),
q_N(x)=1-(1-x)R_N(x).                                      (20.14)
```

These formulas give exactly

```text
q_N(0)=0,
q_N(1)=1.                                                   (20.15)
```

For every positive bulk product `x`, `|R_N(x)|<=epsilon_N/(B_N+1)` and hence

```text
|q_N(x)-1|=|1-x||R_N(x)|<=epsilon_N.                        (20.16)
```

Since `B_N/Lambda_N=Theta(a)` and
`log((B_N+1)/epsilon_N)=O(log N)`, the Chebyshev degree is

```text
deg q_N=d_N+1=O(sqrt(a)log N)=O(N^(1/6)log N).              (20.17)
```

This is the decisive distinction between exact and approximate local recovery.  The support has
`Omega(a)` distinct products, but their separation from zero lets one approximate activity in
only `O(sqrt(a)log N)` degree.  The isolated unit product is handled exactly by the factor
`1-x` and does not enlarge the interval condition number.

## 5. Robust global boundary discriminator

For a histogram with all `m` slot products `x_i` (including zero unused and inactive slots), put

```text
A_tilde(H)=sum_i q_N(x_i),
A(H)=number of active occupied pair-types.                  (20.18)
```

Inactive and unused slots contribute zero exactly, unit active slots contribute one exactly, and
each bulk active slot has error at most `epsilon_N`.  Therefore

```text
|A_tilde-A|<=L epsilon_N=1/10.                              (20.19)
```

In particular, NO profiles have `A_tilde=0` exactly, while every YES profile satisfies

```text
A_tilde in [1/2,L+1/2].                                    (20.20)
```

Map the latter interval to `[-1,1]` by

```text
z_L(w)=(L+1-2w)/L,
z_0=z_L(0)=(L+1)/L,
r_L=ceil(arcosh(4)/arcosh(z_0)),
P_L(w)=T_(r_L)(z_L(w))/T_(r_L)(z_0).                       (20.21)
```

Then

```text
P_L(0)=1,
|P_L(w)|<=1/4 for w in [1/2,L+1/2],
r_L=O(sqrt(L))=O(N^(1/3)).                                 (20.22)
```

For `b(H)=1[H is NO]`, (20.20)--(20.22) give the uniform support approximation

```text
||b-P_L(A_tilde)||_infinity<=1/4.                           (20.23)
```

## 6. Actual orbit-span cost

The composite in (20.23) is not merely an arbitrary slot polynomial.  The collision-partition
identity used in phases 18--19 states that every symmetric polynomial in the slot products
`x_i=r_i u_i` of total `x`-degree `d` is a linear combination of actual injection-tensor orbit
rows of query degree at most `2d`.  Briefly, each collision block contributes

```text
(ru)^ell=sum_(p,q) S(ell,p)S(ell,q)(r)_p(u)_q,              (20.24)
```

whose symmetric coefficients are legitimate combinations of
`A_(p,q)=((r)_p(u)_q+(r)_q(u)_p)/2`; distinct blocks are injected into distinct target slots.

The statistic `A_tilde` is symmetric and has `x`-degree `d_N+1`.  Consequently
`P_L(A_tilde)` lies in the actual orbit-feature span by query degree at most

```text
2r_L(d_N+1)=O(N^(1/2)log N)=o(N^(2/3)).                    (20.25)
```

All source-pair and query-size range conditions hold because the right side is `o(N)` and
`o(m)`.  Thus for every cutoff `D>=cN^(2/3)` with fixed `c>0`, the approximant in (20.23) belongs
to `V_D` for all sufficiently large odd `N`.

## 7. Projection-residual correlation failure

Let `g=b-Proj_(V_D)^(L_2(pi))b` be the phase-16 residual.  If `g=0`, the normalized signed law is
not defined.  Otherwise set `W_pi=pi g/||g||_(1,pi)`.  It has zero mass, unit `l1`, and annihilates
`P_L(A_tilde)`.  With label `f=1-2b`,

```text
|<W_pi,f>|
 =2|<W_pi,b-P_L(A_tilde)>|
 <=2||b-P_L(A_tilde)||_infinity
 <=1/2 <2/3.                                                (20.26)
```

Equivalently, the exact phase-16 residual identity obeys

```text
2||g||_(2,pi)^2/||g||_(1,pi)<=1/2,                         (20.27)
```

so the required strict correlation gate fails.  This is an analytic control of the actual
projection, not a conclusion drawn from base support or tail mass.

## 8. Gate ledger

| Gate | Family (20.1)--(20.7) |
|---|---|
| one formula-defined positive law | **PASS** |
| exact odd-`q=N` legality and rounding | **PASS** |
| nonproduct random total law | **PASS** |
| distributed NO boundary | **PASS** |
| `K=Theta(N^(2/3))` | **PASS** |
| smallest positive `C_t=1` and gap-free initial interval | **PASS** |
| at least `Omega(N^(1/3))` positive one-slot product types | **PASS** |
| base mass at `C_t=Theta(N^(4/3))` | **PASS**, tending to one |
| exact local activity interpolation costs `Omega(N^(1/3))` | **PASS** |
| no low-degree approximate activity separator | **FAIL**, degree `O(N^(1/6)log N)` |
| actual projection correlation above `2/3` | **FAIL**, at most `1/2` |
| residual-weighted high-tail mass | not needed after correlation failure |
| target `D=Theta(N^(2/3))` | **FAIL**, separator degree is `o(N^(2/3))` |

## 9. Scoped conclusion

Phase 20 closes the simplest cardinality repair of phase 19.  Giving each bulk total every possible
split creates `Omega(N^(1/3))` distinct one-slot products, but those products remain uniformly
separated from zero by `Theta(N^(1/3))`.  Chebyshev approximation exploits that interval geometry
and recovers activity much more cheaply than exact interpolation.

A future candidate within this node would need residual-relevant one-slot moment types that are
not only numerous but also approach the inactive boundary across sufficiently many scales to make
*approximate* local activity cost `Omega(N^(1/3))`.  This is a necessary design condition, not a
new route analyzed here.

No distinct escape route was analyzed or commissioned.  No `PROVED`, `CERTIFIED*`, `NUMERICAL`, or
`REFUTED` status is claimed.
