# k-Sum L2 phase-28 analytic/numerical proposer — `q=N` two-reservoir construction

Date: 2026-07-21

Controlling node:
`KSUM.B4b.L2.ALT.correlation-tail-decoupled-two-reservoir`

Scope: the `q=N` endpoint with `D=Theta(N^(2/3))`; one formula-defined `C_t=Theta(N)`
correlation bridge and one formula-defined correlation-neutral `C_t=Theta(N^(4/3))` tail
reservoir.  No broad support search or LP is performed.

Tier: proposer derivation plus bounded exact checks; no independent review and no completion-tier
claim.

## Decision

**Decision B for the additive two-reservoir construction; the controlling node remains OPEN.**

There is a clean positive result: a parity reservoir on `L>D` equal-total switch pairs is legal,
has unit `l1`, is supported entirely at `C_t=Theta(N^(4/3))`, has zero label correlation, and
**exactly annihilates every actual orbit row of query degree below `D`**.  This is an exact
pre-limit identity, not a scalar-moment surrogate.

Combining it with the minimal `C_t=Theta(N)` YES/NO bridge gives

```text
l1=1,       correlation=3/4>2/3,       high-tail mass=1/4.   (28.1)
```

But exact moment cancellation fails already on the actual degree-two row `C_t`: the parity tail
annihilates it, while the bridge leaves a nonzero `Theta(N)` defect.

Making the high-tail component moment-bearing does not repair this separated-scale construction
with bounded TV.  Scalar powers of `C_t` are actual orbit rows.  A Chebyshev extrapolation from a
high band `[H,2H]`, `H=Theta(N^(4/3))`, down to the bridge scale `M=Theta(N)` forces any neutral
tail correction matching the bridge through degree `Theta(D)` to have TV `exp(Theta(D))`.

Thus exact actual-row cancellation, constant correlation, and constant high tail cannot all be
obtained by this additive low/high construction.  The obstruction is the scale gap, not the
existence of a neutral exact tail reservoir.

## 1. Endpoint parameters and legality

Take sufficiently large odd `N` and set

```text
D=floor(N^(2/3)),
L=D+1,
S=D,
R=N-2S-2L.                                                (28.2)
```

For all large `N`,

```text
R>0,
L+2<=(N-1)/2.                                             (28.3)
```

Thus the constructions below use at most the `q=N` endpoint's available `(N-1)/2`
nonfixed complementary value-pair types and have exact total occupancy `N`.

Constants can be inserted in front of `N^(2/3)` in (28.2), provided
`L>D` and `2S+2L=o(N)`; the unit-constant choice keeps the formulas transparent.

## 2. Exact correlation-neutral tail reservoir

Use `L` labeled switch pair-types.  Each switch has total occupancy two and takes one of the
states

```text
A=(0,2),       B=(1,1).                                  (28.4)
```

Add the fixed active core and unsplit filler

```text
core=(S,S),       filler=(0,R).                          (28.5)
```

For a labeled switch vector `omega in {A,B}^L`, let `H(omega)` be the resulting legal histogram.
Define the signed product functional

```text
eta_L=product_{i=1}^L (delta_A-delta_B)/2                (28.6)
```

and push it forward to unordered orbit histograms.  If exactly `z` switches are in state `B`,
the pushforward weight is

```text
t_z=(-1)^z binom(L,z)/2^L,       z=0,...,L.              (28.7)
```

All labeled configurations with the same `z` have the same histogram and the same sign, so no
absolute mass is lost under pushforward.  Therefore

```text
sum_z t_z=0,
sum_z |t_z|=1.                                           (28.8)
```

Every support point is YES because of the permanent core, and

```text
C_t(H_z)=S^2+z=Theta(N^(4/3)).                           (28.9)
```

Hence the signed tail reservoir `T_N` defined by (28.7) has

```text
||T_N||_1=1,
<T_N,label>=0,
tail(T_N)=1.                                             (28.10)
```

The second equality follows because the label is identically `+1` and the total signed mass is
zero.

## 3. Exact annihilation of every actual degree-`<D` orbit row

Lift an arbitrary actual orbit row of query degree `d<D` to the labeled switch space before the
unordered pushforward.  Expand its injection sum over target complementary pair-types.  Each
summand touches at most `d` distinct target slots, because touching a slot consumes at least one
queried variable.

Since

```text
d<D<L,                                                    (28.11)
```

every summand leaves at least one of the `L` switches untouched.  On an untouched switch the
local factor is the constant one, and

```text
int 1 d[(delta_A-delta_B)/2]=0.                          (28.12)
```

The product integral of that summand is therefore exactly zero.  This holds term by term,
regardless of how often a touched slot is queried, and regardless of whether the fixed core or
filler is used by the injection.  Summing and pushing forward gives

```text
<T_N,F_gamma>=0       for every actual orbit row
                      with query degree gamma<D.         (28.13)
```

This proof uses the actual injection-row type.  It does not replace the orbit span by arbitrary
coordinate polynomials.

As a scalar check, (28.13) contains the familiar finite-difference identities

```text
sum_{z=0}^L (-1)^z binom(L,z)z^j=0,       0<=j<L.       (28.14)
```

## 4. Minimal `O(N)` correlation bridge

Let

```text
M=floor(N/4).                                             (28.15)
```

Define two legal two-slot histograms

```text
X_N: (0,M+1), (0,N-M-1),       NO,
Y_N: (1,M),   (0,N-M-1),       YES.                     (28.16)
```

They have identical total occupancy and

```text
C_t(X_N)=0,
C_t(Y_N)=M=Theta(N).                                     (28.17)
```

The signed bridge

```text
B_N=(delta_{Y_N}-delta_{X_N})/2                          (28.18)
```

has

```text
sum B_N=0,       ||B_N||_1=1,       <B_N,label>=1.       (28.19)
```

It is the smallest formula-defined bridge with perfect raw correlation at the requested scale.
It is not claimed to annihilate the target moment space.

## 5. Raw two-reservoir mixture

Take a fixed mixing fraction `epsilon=1/4` and define

```text
W_N^(0)=(1-epsilon)B_N+epsilon T_N.                      (28.20)
```

The supports are disjoint for large `N`, so

```text
||W_N^(0)||_1
 =(1-epsilon)||B_N||_1+epsilon||T_N||_1=1.              (28.21)
```

Both components have zero total mass.  Equations (28.10) and (28.19) give

```text
<W_N^(0),label>=1-epsilon=3/4>2/3,                       (28.22)
```

and all of the `T_N` absolute mass lies at the desired target scale, so

```text
tail_{C_t=Theta(N^(4/3))}(W_N^(0))=epsilon=1/4.          (28.23)
```

Thus every normalization, legality, correlation, and tail gate passes exactly.

## 6. Immediate actual-moment failure

Phase 18 gave an exact collision-partition expansion placing every polynomial of degree `j` in
`C_t` inside the actual orbit span by query degree at most `2j`.  In particular, `C_t` itself is
an actual degree-two orbit-row combination.

The exact tail identity (28.13) gives

```text
<T_N,C_t>=0.                                              (28.24)
```

The bridge gives

```text
<B_N,C_t>=M/2.                                           (28.25)
```

Therefore

```text
<W_N^(0),C_t>
 =(1-epsilon)M/2=3M/8 !=0.                               (28.26)
```

The candidate fails exact annihilation already at query degree two.  The tail reservoir is “too
neutral”: because it annihilates every target row independently, it cannot correct any bridge
defect.

## 7. Could a moment-bearing neutral high tail repair the bridge?

Consider the most favorable scalar relaxation.  Let a correlation-neutral YES/YES tail
functional `U_N` have zero total mass and support only in

```text
H<=C_t<=2H,       H=Theta(N^(4/3)).                      (28.27)
```

Suppose it cancels the bridge's scalar moments through degree

```text
r=floor((D-1)/2)=Theta(N^(2/3)),                         (28.28)
```

which is necessary because all those powers of `C_t` are actual degree-`<D` rows.  After scaling
`y=C_t/H` and putting

```text
epsilon_N=M/H=Theta(N^(-1/3)),                          (28.29)
```

the moment equations require `U_N` to reproduce, up to a fixed nonzero mixture coefficient, the
functional

```text
p -> p(0)-p(epsilon_N)                                  (28.30)
```

on all polynomials of degree at most `r`.

Map `[1,2]` to `[-1,1]` by

```text
z(y)=2y-3                                                (28.31)
```

and choose `p_r(y)=T_r(z(y))`.  Then

```text
sup_{1<=y<=2}|p_r(y)|<=1,                               (28.32)
```

while

```text
|p_r(0)-p_r(epsilon_N)|
 =exp(Theta(r))                                         (28.33)
```

because both arguments lie strictly outside `[-1,1]`, their arcosh values differ by
`Theta(epsilon_N)`, and

```text
r epsilon_N=Theta(N^(1/3)) -> infinity.                 (28.34)
```

The moment representation and (28.32) force

```text
||U_N||_TV>=c|p_r(0)-p_r(epsilon_N)|
            =exp(Theta(D)),                             (28.35)

```

for a fixed `c>0` determined by the bridge mixture weight.  Thus no bounded-TV neutral corrector
confined to a constant-fraction `Theta(N^(4/3))` band can cancel even the scalar moment vector of
this bridge.

Since scalar powers are a subspace of the actual orbit rows, adding fixed-index and two-slot
requirements cannot remove this obstruction.

## 8. Bounded checks

Command:

```text
python ksum/tools/ksum_l2p28_qn_two_reservoir_check.py
```

Driver SHA-256:

```text
3ce5a279f058d7a4fc4a9d2c1566aac65cf8b82e4d8e0973f6466fa12ce70465
```

Raw log:
`ksum/artifacts/logs_ksum_L2p28_qN_two_reservoir_20260721/run.json`

For `N=1001,8001,64001`, the run verifies:

- exact legality and pair budgets;
- tail intervals `S^2<=C_t<=S^2+L`;
- the parity moments (28.14) through degree six are exactly zero;
- raw mixture correlation `0.75` and tail `0.25`;
- nonzero `C_t` defects `93.75,750,6000`;
- base-10 logarithms of the Chebyshev TV lower bound approximately
  `37.45,152.43,611.83`.

These checks exercise the displayed formulas directly.  They do not search for alternative
supports.

## 9. New escape generated and not tested

The obstruction generates one distinct escape:

> **multiscale moment-bearing neutral ladder** — replace the separated high-band corrector by a
> correlation-neutral YES/YES hierarchy whose `C_t` support connects `Theta(N)` continuously to
> `Theta(N^(4/3))`, so scalar moments are transported locally rather than by exponentially
> unstable extrapolation, while a parity component retains constant absolute high-tail mass.

This route is only named.  It was not constructed or tested.  Under DAG Rule 8 it requires a
canonical node before any follow-up work.

## 10. Gate ledger

| obligation | result |
|:---|:---|
| formula-defined `O(N)` correlation bridge | PASS: (28.15)-(28.19) |
| formula-defined neutral high-tail reservoir | PASS: (28.4)-(28.10) |
| tail actual rows degree `<D` | EXACTLY CANCELED: (28.13) |
| `l1=1` | PASS for raw mixture |
| correlation `>2/3` | PASS for raw mixture: `3/4` |
| constant `C_t=Theta(N^(4/3))` tail | PASS: `1/4` |
| joint scalar moment cancellation | FAIL already at `C_t` |
| joint fixed-index/two-slot actual rows | FAIL because scalar subspace fails |
| bounded-TV high-band correction | OBSTRUCTED for this bridge by (28.35) |
| exact final witness | NOT OBTAINED |

## 11. Scoped conclusion

At `q=N`, a correlation-neutral high-tail annihilator is easy to construct exactly: the parity
reservoir solves every actual moment equation below `D` and has perfect target-scale tail.  What
it cannot do is repair a low-scale correlation bridge.  Once the two reservoirs are separated by
the ratio `N^(1/3)` in `C_t`, matching their scalar moments through degree `Theta(N^(2/3))` has an
exponential TV cost.

This is Decision B for the additive separated-scale construction, not a global impossibility
result for multiscale coupled supports.  The controlling node remains open, and no `PROVED`,
`CERTIFIED*`, or `REFUTED` claim is made.
