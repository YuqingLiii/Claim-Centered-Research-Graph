# k-Sum L2 phase-26 analytic proposer — overcomplete split-opening cascades

Date: 2026-07-21

Controlling node: `KSUM.B4b.L2.ALT.mesoscopic-split-opening-cascade`

Scope: overcomplete signed kernels in the exact paired family
`H_+^(s)-H_-^(s)` at `q=5`, `K=2`, `D=Theta(sqrt N)`.  No exhaustive LP.

Tier: proposer derivation only; no independent review and no completion-tier claim.

## Decision

**Decision C — overcompleteness beats the raw norm-versus-tail tradeoff, but not the full
correlation-plus-tail gate in the canonical paired orientation.**

The Phase-25 tradeoff is not universal at the level of coefficient norm and absolute tail mass.
An overcomplete support can superpose:

- a quadratic corner bridge with fixed `lambda_0=1` and `O(1)` coefficient `l1`; and
- a separately normalized arithmetic moment kernel wholly inside `s=Theta(N)`.

The resulting exact kernel has fixed corner coefficient, coefficient norm at most `2.103`, and
one half of its coefficient mass in the macroscopic tail.  On disjoint YES/NO pairs this is exactly
the exploratory `1/4` high-`C_t` orbit-mass gate.  Thus extra nullity genuinely removes the
minimal-ladder norm obstruction.

But a degree-`D-2` Chebyshev filter gives a uniform dual obstruction for **every** overcomplete
paired ladder in the canonical nonduplicating orientation `2<=s<N/2`: if at least half of the
coefficient `l1` mass is at `s=Theta(N)`, then normalized label correlation is at most

```text
1/2+exp(-Omega(D)).                                      (26.1)
```

It is therefore below `2/3` for all sufficiently large `N`.  The explicit bounded-norm
construction is real, but its tail component necessarily dilutes the correlation.

This memo does not cover simultaneous use of `s` and `N-s`, whose jumps share the same NO orbit.
That mechanism is named, but not tested, in Section 7.

## 1. Exact moment formulation

Retain the Phase-25 variables

```text
t=s-2,
mu_t=(t+1)lambda_t,
m=D-2.                                                   (26.2)
```

For the exact jump measure

```text
W_lambda=sum_t lambda_t
 (delta_{H_+^(t+2)}-delta_{H_-^(t+2)}),                  (26.3)
```

annihilation of every actual orbit row of degree `<D` is equivalent to

```text
sum_t mu_t P(t)=0       for every deg P<=m-1.            (26.4)
```

The coefficient norm and signed label numerator are

```text
L(lambda)=sum_t |lambda_t|
         =sum_t |mu_t|/(t+1),
S(lambda)=sum_t lambda_t.                                (26.5)
```

If all selected `s` lie below `N/2`, the YES and NO atoms are pairwise distinct.  Hence

```text
||W_lambda||_1=2L(lambda),
<label,W_lambda>=2S(lambda),
corr(W_lambda)=|S(lambda)|/L(lambda).                    (26.6)
```

Only the YES member of a pair has `C_t=s-1=t+1`.  Thus an orbit tail-mass requirement `1/4`
is equivalent to a coefficient tail fraction at least `1/2`.

## 2. The overcomplete norm-tail optimization has constant value

Fix the corner coefficient

```text
lambda_0=1,                                              (26.7)
```

and require

```text
sum_{t>=A_N}|lambda_t| >= L(lambda)/2,
A_N=Theta(N).                                            (26.8)
```

The lower bound is immediate.  Since the corner lies outside the tail,

```text
L(lambda)
 >=1+sum_{t>=A_N}|lambda_t|
 >=1+L(lambda)/2,
```

so

```text
L(lambda)>=2.                                            (26.9)
```

The next sections give a formula-defined exact kernel with

```text
L(lambda)<=2(1+pi^2/192)<2.103.                          (26.10)
```

Therefore the minimum coefficient norm in this overcomplete class is `Theta(1)`, tightly between
`2` and `2.103`.  Overcompleteness really does beat the exponential minimal-ladder cost.

## 3. Bounded-norm corner bridge

Choose `h=64` and an integer `m=D-2` satisfying

```text
64m^2 <= N/8.                                            (26.11)
```

This still gives `D=Theta(sqrt N)`.  On the quadratic nodes

```text
t_j=64j^2,       0<=j<=m,                               (26.12)
```

use the exact Phase-25 barycentric coefficients

```text
b_0=1,
b_j=2(-1)^j (m!)^2/
    ((m-j)!(m+j)!(1+64j^2)),       1<=j<=m.             (26.13)
```

They satisfy (26.4), have the fixed corner value `b_0=1`, and obey

```text
L_B:=sum_j|b_j|
 <=1+pi^2/192.                                           (26.14)
```

All bridge nodes satisfy `t_j<=N/8`, so none belongs to the macroscopic tail used below.

## 4. Independent exact macroscopic kernel

Let

```text
A=floor(N/3),
u_j=A+j,       0<=j<=m.                                 (26.15)
```

For sufficiently large `N`, these nodes lie below `N/2`, above `N/4`, and are disjoint from the
bridge.  The arithmetic barycentric kernel is

```text
a_j=(-1)^j binom(m,j)/(u_j+1).                           (26.16)
```

Indeed `(u_j+1)a_j=(-1)^j binom(m,j)` annihilates every polynomial in `u_j` of degree at most
`m-1`.  Thus (26.16) satisfies the same complete orbit equations (26.4).

Let

```text
L_A=sum_j|a_j|,
c=L_B/L_A,
lambda=b+c a.                                            (26.17)
```

The supports are disjoint, so this is an overcomplete exact kernel with

```text
lambda_0=1,
L(lambda)=L_B+cL_A=2L_B<=2(1+pi^2/192),                 (26.18)
```

and

```text
sum_{t>=N/4}|lambda_t|=cL_A=L_B=L(lambda)/2.             (26.19)
```

Equations (26.18)-(26.19) prove the claimed constant-norm, constant-tail construction.  Every
atom is a legal integer `q=5` orbit, including for odd `N`; no rounding is used.

This construction uses `2m+2=Theta(D)` nodes, only one node more than twice the moment rank.  The
improvement is caused by overcomplete nullity, not by a large finite search.

## 5. Polynomial dual filter for the entire canonical overcomplete class

Now let an arbitrary overcomplete paired kernel be supported in

```text
0<=t<=L_N,
L_N< N/2-2,                                              (26.20)
```

and call `[A_N,L_N]`, with `A_N/L_N` bounded away from zero and one, the macroscopic tail.

Map this tail interval to `[-1,1]`:

```text
x(t)=(2t-A_N-L_N)/(L_N-A_N).                             (26.21)
```

Define the degree-`m` polynomial

```text
R_m(t)=T_m(x(t))/T_m(x(-1)).                             (26.22)
```

It has three exact properties:

1. `R_m(-1)=1`.
2. `|R_m(t)|<=1` for every `0<=t<=L_N`.  On the tail this follows from
   `|T_m(x)|<=1`; before the tail, `x(t)<=-1` and its absolute Chebyshev value is monotone, with
   the largest value attained at the farther point `t=-1` used in the denominator.
3. On the tail,

```text
|R_m(t)|<=epsilon_m
 :=1/|T_m(x(-1))|
 <=2 exp(-m arcosh(chi)),                                (26.23)
```

where

```text
chi=(A_N+L_N+2)/(L_N-A_N)>1                              (26.24)
```

is bounded away from one.  Hence `epsilon_m=exp(-Omega(D))`.

Since `R_m(-1)=1`, the polynomial `1-R_m(t)` is divisible by `t+1`:

```text
1-R_m(t)=(t+1)P_{m-1}(t),
deg P_{m-1}<=m-1.                                       (26.25)
```

Insert `P_{m-1}` in the exact moment condition (26.4).  It gives

```text
sum_t lambda_t(1-R_m(t))=0,
S(lambda)=sum_t lambda_t R_m(t).                         (26.26)
```

If

```text
tau=sum_{tail}|lambda_t|/L(lambda),                      (26.27)
```

then (26.22)-(26.26) imply the universal bound

```text
corr(W_lambda)
 =|S(lambda)|/L(lambda)
 <=1-tau+epsilon_m tau.                                  (26.28)
```

At the required paired-orbit tail gate, `tau>=1/2`, so

```text
corr(W_lambda)
 <=1/2+epsilon_m/2
 =1/2+exp(-Omega(D))<2/3                                (26.29)
```

for every sufficiently large `N`.

This is a dual polynomial bound for the full overcomplete canonical paired class.  It does not
assume a minimal support, a sign pattern, a scale schedule, or the explicit construction of
Sections 3-4.

## 6. Interpretation

The overcomplete direct sum reveals why coefficient norm alone was the wrong final gate.
Additional nullity can store a bounded corner functional and an independently normalized tail
functional side by side.  But the macroscopic component is nearly invisible to the signed label
functional: `1/(t+1)` is exponentially well approximated on a separated macroscopic interval by
the degree allowed in (26.4).  The filter (26.22) converts that fact into the correlation loss
(26.29).

Thus:

```text
fixed corner + bounded l1 + constant tail:       ACHIEVABLE;
the same plus correlation >2/3:                  OBSTRUCTED
                                                  in the canonical paired orientation.  (26.30)
```

## 7. Newly named, untested escape

If both `s` and `N-s` are used, the two paired jumps have the same NO orbit

```text
H_-^(s)=H_-^(N-s),                                      (26.31)
```

while their YES orbits remain different.  Cancellation at this shared NO atom changes the exact
orbit `l1` norm and invalidates the disjoint-pair identity (26.6).  A
**two-orientation shared-NO cascade** is therefore a distinct possible escape from the scoped
bound (26.29).

This direction is named only.  No coefficients, moment kernel, norm bound, correlation estimate,
or finite test for it was attempted.  Under Rule 8 it requires a registered node before any such
work.

No other distinct escape was generated.

## 8. Gate ledger

| obligation | result |
|:---|:---|
| full overcomplete moment formulation | PASS: exact (26.4) |
| fixed corner coefficient | PASS: `lambda_0=1` |
| coefficient `l1=O(1)` | PASS: (26.18) |
| constant `C_t=Theta(N)` coefficient tail | PASS: one half, (26.19) |
| exploratory `1/4` orbit tail | PASS for disjoint paired atoms |
| correlation above `2/3` | FAIL for every canonical overcomplete paired ladder by (26.29) |
| all paired orientations including shared NO atoms | OPEN / not tested |
| non-paired orbit combinations | outside scope |

## Scoped conclusion

Overcompleteness decisively beats the Phase-25 minimal-support norm-tail tradeoff: the optimum
coefficient norm with fixed unit corner and one-half macroscopic coefficient tail is between `2`
and `2.103`, uniformly in `N`.  Nevertheless, the same polynomial moment duality supplies a
schedule-independent Chebyshev residual which caps correlation at
`1/2+exp(-Omega(D))` in the canonical paired orientation.  Hence overcompleteness alone does not
produce the required k-Sum discriminator.

This is Decision C rather than a completion-tier obstruction because the shared-NO two-orientation
class remains outside the proof.  No `PROVED`, `CERTIFIED*`, or `REFUTED` status is claimed.
