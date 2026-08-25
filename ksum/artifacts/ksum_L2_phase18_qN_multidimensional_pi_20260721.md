# k-Sum L2 phase-18 proposer analysis — a multidimensional balanced `q=N` base law

Date: 2026-07-21  
Controlling node:
`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel`  
Tier: proposer only; no independent review and no DAG status claim

## Decision

**B — a concrete genuinely multidimensional law is sharply falsified by a support-level
`C_t` Chebyshev obstruction.**  The law below has random pair totals, independently random
balanced split proportions conditional on those totals, a distributed NO boundary, exact endpoint
legality, and overwhelmingly large base-measure mass at `C_t=Theta(N^(4/3))`.  Its labeled lift is
nonproduct because the random totals obey an exact global composition constraint.

The obstruction is not the phase-17 deterministic activation/reservoir parametrization.  There
are growing numbers of total and split coordinates.  Instead, every nonzero split on this support
has product `ru=Omega(N^(2/3))`, while total `C_t` is at most `O(N^(4/3))`.  A Chebyshev polynomial
of degree `O(N^(1/3))` therefore separates `C_t=0` from the whole YES support.  A direct collision-
partition expansion shows that every polynomial of degree `j` in `C_t` belongs to the actual orbit
row span by query degree at most `2j`.  At `D=Theta(N^(2/3))`, the phase-16 residual is consequently
either zero or has normalized correlation at most `1/2`.

Thus balanced random totals and split proportions still fail if the support leaves a polynomially
large gap between `C_t=0` and the first YES layer.  This is not an impossibility result for measures
whose residual-relevant mass also reaches much smaller positive `C_t`.

## 1. Exact legal support with random totals

Take sufficiently large odd `N`, set `q=N`, and define

```text
m=(N-1)/2,
L=floor(N^(2/3)),
t=floor(N/L),
h=N-Lt.                                                       (18.1)
```

Thus `0<=h<L`.  Let the ordered total-composition set be

```text
C_(N,L)={s in Z^L:
         s_i=t+delta_i, delta_i in {-2,-1,0,1,2},
         sum_i delta_i=h}.                                    (18.2)
```

It is nonempty for every `N`: take `h` coordinates with `delta_i=1` and the rest with
`delta_i=0`.  For all large `N`, `t>=6`, so every total is positive.  Every `s in C_(N,L)` satisfies

```text
sum_i s_i=Lt+h=N,
t-2<=s_i<=t+2.                                                (18.3)
```

For an integer total `s`, define the balanced active-split set

```text
B_s={r in Z: ceil(s/3)<=r<=floor(s/2)}.                        (18.4)
```

It is nonempty in the stated range.  A slot of total `s_i` is either inactive with unordered split
`(0,s_i)`, or active with split `(r_i,s_i-r_i)` for some `r_i in B_(s_i)`.  Let `S_(N,L)` be the set
of unordered histograms obtained from all such ordered choices.

Every profile is legal without a reservoir or divisibility subsequence: it has exactly `L`
positive occupied complementary pair-types, total occupancy `N`, and `L<=m` for all sufficiently
large `N`.  The totals and split ratios vary in growing numbers of coordinates; neither the
histogram nor its target-pair count determines the underlying total/split vector.

The NO boundary is distributed.  For every composition in (18.2), setting all its splits inactive
gives a NO profile.  These do not collapse to one histogram: even after quotienting by slot
permutations, the five possible total values admit multiple count vectors satisfying the two
constraints on their size and sum.  Active profiles add independently varying balanced split
states on top of this boundary.

## 2. Formula-defined positive nonproduct law

Define a labeled generative law as follows:

1. draw `s` uniformly from `C_(N,L)`;
2. independently for each slot, declare it inactive with probability `1/2`;
3. otherwise declare it active and draw `r_i` uniformly from `B_(s_i)`;
4. forget the slot ordering and retain only the split histogram.

This gives a formula-defined strictly positive law on `S_(N,L)`.  If `H_tau` is the multiplicity
of split state `tau=(r,s-r)` in an unordered histogram `H`, its exact mass is

```text
pi_(N,N)(H)
 = [L! / product_tau H_tau!]
   / [|C_(N,L)| 2^L product_(tau active in H) |B_(s(tau))|^(H_tau)].
                                                                  (18.5)
```

All ordered representatives have the same product weight, so (18.5) is exactly the pushforward
law and sums to one.

The labeled lift is genuinely nonproduct.  Its totals satisfy `sum_i s_i=N` almost surely while
each marginal total has nonzero variance for large `L` (the set (18.2) contains nontrivial
zero-sum deviation moves).  Independent coordinates with that marginal variance would give a
positive variance for their sum, a contradiction.  This dependence is intrinsic to the random
composition and is present before quotienting by permutations.  Unlike phase 17, there is no
single activation count that determines the profile, and there is no deterministic reservoir.

## 3. Balanced high-`C_t` base tail

Write `x_i=r_i(s_i-r_i)` for an active slot and `x_i=0` for an inactive slot.  When active,
(18.3)--(18.4) imply

```text
x_i >= s_i^2/6 >= (t-2)^2/6 =: Delta_N,                    (18.6)
x_i <= s_i^2/4 <= (t+2)^2/4.                               (18.7)
```

The number `A` of active slots is exactly `Binomial(L,1/2)`, independently of the chosen total
composition.  Hence

```text
Pr[A>=L/3] >= 1-exp(-L/36).                                 (18.8)
```

On that event,

```text
(L/3) Delta_N <= C_t=sum_i x_i <= L(t+2)^2/4.              (18.9)
```

Since `t=Theta(N/L)=Theta(N^(1/3))`, both ends of (18.9) are constant multiples of
`N^2/L=Theta(N^(4/3))`.  Thus the positive base law has probability tending to one, not merely a
fixed constant, on balanced high-`C_t` profiles.  This does not by itself imply a residual-weighted
tail bound.

## 4. Orbit-span lemma: powers of `C_t` cost query degree at most twice their degree

The obstruction needs actual orbit rows, not a larger polynomial space.  Let an arbitrary legal
ordered split list be `tau_i=(r_i,u_i)` and put `x_i=r_i u_i`, so `C_t=sum_i x_i`.

For each integer `j>=1`, expand

```text
(C_t)^j = sum_(phi:[j]->[m]) product_(a=1)^j x_(phi(a)).     (18.10)
```

Group maps `phi` by the set partition of `[j]` induced by equality of target slots.  A block of
size `ell` assigned to slot `i` contributes

```text
x_i^ell=(r_i u_i)^ell
       =sum_(a=1)^ell sum_(b=1)^ell
          S(ell,a)S(ell,b)(r_i)_a(u_i)_b,                   (18.11)
```

where `S(ell,a)` are Stirling numbers of the second kind.  The coefficient in (18.11) is symmetric
in `a,b`, so the expression is a linear combination of the legitimate unordered one-slot factors

```text
A_(a,b)(r,u)=((r)_a(u)_b+(r)_b(u)_a)/2.                     (18.12)
```

Different blocks are assigned to distinct target slots.  Summing those assignments is exactly an
injection tensor of the phase-12/16 type.  Its total query degree is at most

```text
sum_blocks (a_block+b_block) <= 2 sum_blocks |block|=2j.     (18.13)
```

All normalizing factors are nonzero when `2j<=N` and the number of blocks is at most `m`.
Consequently, without assuming any special support,

> every polynomial in `C_t` of ordinary degree at most `j` lies in the actual orbit-feature span
> generated by query degrees at most `2j`.

For the degree used below, `j=O(sqrt(L))=O(N^(1/3))`, so both range conditions hold for all large
odd `N`.  This derivation directly constructs the required row combination and does not replace
the orbit span by arbitrary coordinate polynomials.

## 5. Explicit support-level Chebyshev approximant

Every YES profile in `S_(N,L)` has

```text
Delta_N <= C_t <= M_N:=L(t+2)^2/4,                           (18.14)
```

while every NO profile has `C_t=0`.  For `t>=6`,

```text
Delta_N >= t^2/24,
M_N <= 9Lt^2/16,
M_N/Delta_N <= (27/2)L.                                    (18.15)
```

Map the YES interval to `[-1,1]` by

```text
y(x)=(M_N+Delta_N-2x)/(M_N-Delta_N),
y_0=y(0)=(M_N+Delta_N)/(M_N-Delta_N)>1.                     (18.16)
```

Set

```text
r_N=ceil(arcosh(4)/arcosh(y_0)),
p_N(x)=T_(r_N)(y(x))/T_(r_N)(y_0).                          (18.17)
```

Then `p_N(0)=1`, and `|p_N(x)|<=1/4` throughout
`[Delta_N,M_N]`.  Moreover

```text
r_N=O(sqrt(M_N/Delta_N))=O(sqrt(L))=O(N^(1/3)).             (18.18)
```

Let `b(H)=1[H is NO]=1[C_t(H)=0]`.  Equations (18.14)--(18.17) give the uniform support bound

```text
||b-p_N(C_t)||_infinity <= 1/4.                             (18.19)
```

By the orbit-span lemma, `p_N(C_t)` belongs to `V_D` whenever `2r_N<D`.  Every cutoff
`D>=cN^(2/3)` with fixed `c>0` satisfies this for all sufficiently large `N`.

## 6. Projection-residual and correlation failure

Let

```text
g=b-Proj_(V_D)^(L_2(pi)) b                                 (18.20)
```

be the phase-16 residual for the law (18.5).  If `g=0`, no normalized signed law is produced.
Otherwise define `W_pi=pi g/||g||_(1,pi)`.  It has unit `l1`, zero mass, and annihilates `V_D`,
including `p_N(C_t)`.  For the label `f=1-2b`,

```text
|<W_pi,f>|
 =2|<W_pi,b>|
 =2|<W_pi,b-p_N(C_t)>|
 <=2||b-p_N(C_t)||_infinity
 <=1/2 <2/3.                                                (18.21)
```

Equivalently, the exact phase-16 residual formula obeys

```text
2||g||_(2,pi)^2 / ||g||_(1,pi) <= 1/2,                     (18.22)
```

so the required strict inequality
`3||g||_(2,pi)^2>||g||_(1,pi)` cannot hold.  This bound is analytic, uniform in the detailed
weights of (18.5), and uses the actual orbit span.

The residual-weighted high-`C_t` gate does not need a separate decision because the correlation
gate already fails by a fixed margin.  The contrast is informative: almost all positive
base-measure mass lies at the desired tail scale, but the gap between the NO boundary and the
first YES layer makes the label too easy for the orbit rows.

## 7. Gate ledger

| Gate | Family (18.1)--(18.5) |
|---|---|
| formula-defined strictly positive law | **PASS** |
| genuinely multidimensional random totals and splits | **PASS** |
| nonproduct dependence | **PASS** by the exact composition constraint |
| distributed NO boundary | **PASS** |
| exact odd-`q=N` legality and rounding | **PASS** for all sufficiently large odd `N` |
| occupied pair count `K=Theta(N^(2/3))` | **PASS**, with `K=L` |
| base mass at `C_t=Theta(N^(4/3))` | **PASS**, probability at least `1-exp(-L/36)` |
| no deterministic activation/reservoir parametrization | **PASS** |
| actual orbit-span control | **PASS** by (18.10)--(18.13) |
| correlation strictly above `2/3` | **FAIL**, at most `1/2` |
| residual-weighted high-`C_t` mass | not needed after correlation failure |
| target cutoff `D=Theta(N^(2/3))` | **FAIL** for every fixed positive cutoff constant |

## 8. Scoped conclusion

This multidimensional family removes the main artificiality of phase 17: totals fluctuate under a
global composition law, balanced split proportions fluctuate independently, and the NO boundary
contains many histograms.  It still fails because its first positive `C_t` value is already
`Omega(N^(2/3))`.  The actual orbit rows can then resolve the scalar gap using only
`O(N^(1/3))` query degree, far below the target cutoff.

For this selective-projection route, a viable base law cannot put all residual-relevant YES mass
on uniformly balanced splits.  It must somehow retain substantial residual complexity near much
smaller positive `C_t` while also retaining constant residual-weighted mass at
`C_t=Theta(N^(4/3))`.  That is a necessary design constraint, not a new construction analyzed here.

No genuinely distinct route was generated, commissioned, or tested in this pass.  No `PROVED`,
`CERTIFIED*`, `NUMERICAL`, or `REFUTED` status is claimed.
