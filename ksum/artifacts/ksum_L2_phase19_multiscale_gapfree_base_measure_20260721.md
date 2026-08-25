# k-Sum L2 phase-19 proposer analysis — multiscale gap-free `q=N` base measure

Date: 2026-07-21  
Controlling node:
`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.multiscale-gapfree-base-measure`  
Tier: proposer only; no independent review and no DAG status claim

## Decision

**B — an explicit multiscale law with genuinely small positive `C_t`, a distributed boundary,
and constant high-tail base mass is sharply falsified.**  The construction below removes the
positive-`C_t` gap that killed phase 18: its support contains every value `C_t=1,...,Theta(N^(2/3))`
already from unit split-pairs, while the remaining pairs use a closed heavy-tailed palette of
split scales extending to balanced products `Theta(N^(2/3))`.  Random exact total compositions
make the histogram law nonproduct and multidimensional, and balanced bulk splits give constant
mass at `C_t=Theta(N^(4/3))`.

Nevertheless, the positive one-slot products lie in only `O(log N)` formula-defined levels.
Lagrange interpolation therefore recovers the local active indicator as a degree-`O(log N)`
polynomial in `ru`.  The global NO label becomes an AND of `K=Theta(N^(2/3))` recovered indicators,
which an explicit degree-`O(sqrt(K))` Chebyshev polynomial approximates.  A collision-partition
expansion places the resulting composite polynomial in the *actual* orbit-feature span by query
degree `O(N^(1/3) log N)=o(N^(2/3))`.  Hence at every target cutoff
`D=Theta(N^(2/3))`, the phase-16 residual is zero or its normalized correlation is at most `1/2`.

This falsifies the finite split-palette heavy-tail mechanism.  It does not rule out a law with a
growing, sufficiently rich continuum of one-slot moment types for which active/inactive
interpolation itself costs `Omega(N^(1/3))` or more.

## 1. Endpoint parameters and exact legal total law

Take sufficiently large odd `N` and `q=N`.  Set

```text
m=(N-1)/2,
L=floor(N^(2/3)),
U=floor(L/4),
M=L-U,
N_bulk=N-2U,
a=floor(N_bulk/M),
h=N_bulk-Ma.                                                 (19.1)
```

There are `U` unit pair-types, each of fixed total `2`, and `M` bulk pair-types.  Draw the ordered
bulk total vector from

```text
C_bulk={s in Z^M:
        s_i=a+delta_i, delta_i in {-2,-1,0,1,2},
        sum_i delta_i=h}.                                    (19.2)
```

Since `0<=h<M`, this is nonempty: take `h` deviations equal to `1` and the rest `0`.  For every
choice in (19.2),

```text
2U+sum_i s_i=2U+Ma+h=N.                                     (19.3)
```

Moreover `a=Theta(N^(1/3))`; in particular, for all sufficiently large `N`, `a-2>=6`, the unit
and bulk totals are disjoint, and every occupied total is positive.  The number of occupied
pair-types is exactly

```text
K=U+M=L=Theta(N^(2/3)) <= m.                                (19.4)
```

Thus legality and rounding hold for every sufficiently large odd `N`, with no divisibility
subsequence and no reservoir pair.

## 2. Closed heavy-tailed split law

A unit pair of total `2` is independently

```text
(0,2) with probability 1/2,
(1,1) with probability 1/2.                                 (19.5)
```

For a bulk total `s`, define the deduplicated dyadic set

```text
D_s={2^j: j>=0 and 2^j<floor(s/2)},
r_bal=floor(s/2).                                           (19.6)
```

Conditional on its total, a bulk slot is independently

```text
(0,s)                         with probability 1/2,
(r_bal,s-r_bal)               with probability 1/4,
(r,s-r), r uniform in D_s     with total probability 1/4.  (19.7)
```

This is a single closed law.  The dyadic branch supplies split scales from `r=1` through a
constant fraction of `s`; the separate balanced atom ensures that the top scale has constant,
not logarithmically vanishing, probability.

Finally forget slot ordering.  The resulting positive histogram law has an explicit formula.
Let `H_(0,2),H_(1,1)` be the two unit-state multiplicities and let `H_tau` denote bulk-state
multiplicities.  Put

```text
w_s(0)=1/2,
w_s(r_bal)=1/4,
w_s(r)=1/(4|D_s|) for r in D_s.                             (19.8)
```

Then

```text
pi_(N,N)(H)
 = [U!/(H_(0,2)! H_(1,1)!)] [M!/product_(tau bulk) H_tau!]
   / |C_bulk|
   * (1/2)^U * product_(tau bulk) w_(s(tau))(r(tau))^(H_tau).
                                                                  (19.9)
```

The unit and bulk total ranges are disjoint, so the two factors are unambiguous.  Formula (19.9)
is exactly the pushforward of the labeled law and is strictly positive on its stated support.

The law is genuinely nonproduct: the bulk totals have nonzero marginal variance but their sum is
fixed exactly by (19.2), which independent coordinates cannot satisfy.  It is also genuinely
multidimensional.  The bulk total histogram varies, each slot has its own split scale, and neither
an activation count nor `C_t` determines the profile.

The NO boundary is distributed over every total histogram induced by (19.2): choose all unit and
bulk slots inactive.  Multiple unordered bulk-total count vectors occur for all large `M` (one may
replace two deviations `1,1` by `0,2`, or two `0,0` by `-1,1`, whenever the corresponding base
counts are available).

## 3. Small positive scales and constant high-tail base mass

Activating exactly `j` unit pairs and no bulk pair gives

```text
C_t=j,                 0<=j<=U.                             (19.10)
```

Every profile in (19.10) has positive probability.  Thus the support contains a gap-free initial
interval of length

```text
U=Theta(N^(2/3)),                                          (19.11)
```

including the smallest possible positive target count `C_t=1`.  The dyadic bulk branch adds a
closed ladder of intermediate one-slot products
`r(s-r)` from `Theta(N^(1/3))` through `Theta(N^(2/3))`.

The law simultaneously has constant high-tail mass.  Conditional on any total composition, each
bulk slot is balanced with probability `1/4`, independently.  If `B` is the number of balanced
bulk slots, then

```text
Pr[B>=M/8] >= 1-exp(-M/32).                                 (19.12)
```

For large `N`, every such slot contributes

```text
floor(s/2)ceil(s/2) >= (a-2)^2/5=Theta(N^(2/3)).            (19.13)
```

Therefore on the event in (19.12),

```text
C_t >= (M/8)(a-2)^2/5 = Theta(N^(4/3)).                    (19.14)
```

The deterministic upper bound is also `C_t=O(M(a+2)^2+U)=O(N^(4/3))`.  Hence the positive base
law places probability tending to one at the required high scale while retaining profiles at
every `C_t` from `1` through `Theta(N^(2/3))`.

This is still only a base-measure statement.  The next sections analyze the actual projection and
show that the desired residual does not survive.

## 4. Exact recovery of local activity from the finite product palette

Let

```text
X_N={ru>0: (r,u) occurs as one slot state in the support}.   (19.15)
```

The unit state contributes product `1`.  Bulk totals take only the five values
`a-2,...,a+2`; each has at most `ceil(log_2 a)+1` allowed positive splits.  Consequently

```text
J_N:=|X_N| <= 1+5(ceil(log_2 a)+1)=O(log N).                (19.16)
```

Define the explicit interpolation polynomial

```text
Q_N(x)=1-product_(c in X_N)(1-x/c).                         (19.17)
```

It has degree `J_N` and obeys exactly

```text
Q_N(0)=0,
Q_N(c)=1 for every c in X_N.                               (19.18)
```

For a histogram with slot products `x_i=r_i u_i`, the scalar

```text
A(H)=sum_i Q_N(x_i)                                        (19.19)
```

is therefore exactly the number of active split pair-types.  In particular,

```text
b(H)=1[H is NO]=1[A(H)=0].                                 (19.20)
```

This collapse was not built into the parametrization: profiles with the same `A` have many total
and split-scale configurations.  It is instead an algebraic consequence of using only
`O(log N)` distinct positive one-slot products.

## 5. Actual orbit-span cost of the interpolated statistic

The phase-18 collision-partition argument extends from powers of `C_t` to every symmetric
polynomial in the slot products.  Explicitly, a monomial symmetric term is a sum over injections
of products

```text
product_blocks (r_i u_i)^(ell_block).                       (19.21)
```

For each block,

```text
(ru)^ell
 =sum_(p=1)^ell sum_(q=1)^ell
    S(ell,p)S(ell,q)(r)_p(u)_q,                             (19.22)
```

and the symmetric coefficients let (19.22) be written using the legitimate orbit factors
`A_(p,q)=((r)_p(u)_q+(r)_q(u)_p)/2`.  Distinct blocks are assigned injectively to distinct target
slots.  Thus every symmetric polynomial of total `x`-degree `d` belongs to the actual orbit row
span generated by query degree at most `2d`.

The polynomial `A(H)` in (19.19) is symmetric and has `x`-degree at most `J_N`.  A degree-`r`
polynomial in `A` therefore lies in the actual orbit span by query degree at most

```text
2J_N r.                                                      (19.23)
```

This is a row-span statement, not an assertion that arbitrary coordinate cylinders are present.
All normalization denominators are nonzero in the range used below because
`J_N r=O(N^(1/3)log N)=o(N)` and the number of occupied source-pair patterns is at most that degree.

## 6. Chebyshev approximation and projection failure

For `L>=2`, define

```text
y_L(z)=(L+1-2z)/(L-1),
alpha_L=arcosh((L+1)/(L-1)),
r_L=ceil(arcosh(4)/alpha_L),
P_L(z)=T_(r_L)(y_L(z))/T_(r_L)(y_L(0)).                    (19.24)
```

Then `P_L(0)=1` and `|P_L(z)|<=1/4` for every integer `1<=z<=L`.  Also

```text
r_L=O(sqrt(L))=O(N^(1/3)).                                 (19.25)
```

By (19.20),

```text
||b-P_L(A)||_infinity <=1/4.                               (19.26)
```

Equations (19.16), (19.23), and (19.25) place `P_L(A)` in the actual orbit-feature space `V_D`
whenever

```text
D>2J_N r_L=O(N^(1/3)log N).                                (19.27)
```

In particular, (19.27) holds for every target cutoff `D>=cN^(2/3)` with fixed `c>0` and all
sufficiently large odd `N`.

Let `g=b-Proj_(V_D)^(L_2(pi))b` be the phase-16 residual.  If `g=0`, the normalized coefficient
law is unavailable.  Otherwise `W_pi=pi g/||g||_(1,pi)` has zero mass, unit `l1`, and annihilates
`P_L(A)`.  With `f=1-2b`,

```text
|<W_pi,f>|
 =2|<W_pi,b-P_L(A)>|
 <=2||b-P_L(A)||_infinity
 <=1/2 <2/3.                                                (19.28)
```

Equivalently,

```text
2||g||_(2,pi)^2/||g||_(1,pi) <=1/2,                        (19.29)
```

so the required strict residual inequality fails.  This controls the actual projection rather
than only the positive base mass.  Residual-weighted high-tail mass cannot rescue a coefficient
law whose total correlation is already below threshold.

## 7. Gate ledger

| Gate | Family (19.1)--(19.9) |
|---|---|
| one explicit positive all-large-odd-`N` law | **PASS** |
| exact `q=N` legality and rounding | **PASS** |
| `K=Theta(N^(2/3))` occupied pair-types | **PASS** |
| random exact total partitions | **PASS** |
| distributed NO boundary | **PASS** |
| no deterministic reservoir or one-parameter profile | **PASS** |
| smallest positive `C_t=1` | **PASS** |
| gap-free initial `C_t` interval | **PASS**, through `Theta(N^(2/3))` |
| explicit intermediate split scales | **PASS**, dyadic through balanced |
| constant base mass at `C_t=Theta(N^(4/3))` | **PASS** by (19.12)--(19.14) |
| no active-count/statistic collapse after restriction | **FAIL** by (19.17)--(19.20) |
| actual projection correlation above `2/3` | **FAIL**, at most `1/2` |
| residual-weighted high-tail mass | not needed after correlation failure |
| target cutoff `D=Theta(N^(2/3))` | **FAIL**, since the separator costs only `O(N^(1/3)log N)` |

## 8. Scoped conclusion

Adding unit pairs defeats the direct phase-18 `C_t`-gap separator, and the heavy-tailed split law
simultaneously supplies intermediate scales and a balanced high tail.  The family still fails
because its local positive-product palette has only logarithmic cardinality.  The actual orbit
rows interpolate the active indicator on that palette and then approximate the global boundary
AND far below the target degree.

For any continuation of this node, the relevant necessary condition is stronger than merely
including `C_t=1`: the number and algebraic complexity of residual-relevant one-slot product/moment
types must itself grow fast enough that local activity cannot be interpolated at cost
`o(N^(1/3))`.  This is a boundary for the present finite-palette family, not a proof that a richer
gap-free positive law cannot work.

No distinct escape route was analyzed or commissioned.  No `PROVED`, `CERTIFIED*`, `NUMERICAL`, or
`REFUTED` status is claimed.
