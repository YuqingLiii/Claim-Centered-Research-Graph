# k-Sum L2 phase-29 analytic/numerical proposer — `q=N` multiscale neutral ladder

Date: 2026-07-21

Controlling node:
`KSUM.B4b.L2.ALT.multiscale-moment-bearing-neutral-ladder`

Scope: a legal discrete ladder from `C_t=Theta(N)` to `Theta(N^(4/3))`, neutral local rung
transports, a separate Phase-28 parity tail, and the full scalar/mixed actual-row requirement at
`D=Theta(N^(2/3))`.  No broad support search or LP is performed.

Tier: proposer derivation plus bounded formula checks; no independent review and no
completion-tier claim.

## Decision

**Decision B for every ladder whose first positive target count is `Theta(N)`; the controlling
node remains OPEN pending independent adjudication.**

A legal local ladder is easy to write, and its adjacent YES/YES differences are genuine
correlation-neutral moment-bearing rungs.  But allowing all intermediate scales between
`Theta(N)` and `Theta(N^(4/3))` does not remove the scalar gap from NO.

If all YES support satisfies

```text
A_N<=C_t<=B_N,
A_N=Theta(N),       B_N=Theta(N^(4/3)),                 (29.1)
```

then a Chebyshev polynomial of ordinary degree

```text
Theta(sqrt(B_N/A_N))=Theta(N^(1/6))                     (29.2)
```

approximates the NO indicator to error `1/4` on the *entire continuous interval* `[A_N,B_N]`.
Every polynomial of degree `r` in `C_t` is an actual orbit-row combination of query degree at
most `2r`.  Hence the separator sits at query degree `Theta(N^(1/6))=o(D)` and forces normalized
correlation at most `1/2`.

Using the full available scalar degree below `D` gives a stronger statement: any exact unit-TV
annihilator on this support has correlation `exp(-Theta(N^(1/2)))`.  Local scalar transport,
mixed multisymmetric correction, and the separate parity tail cannot alter this because the
scalar `C_t` rows are already a subspace of the actual moment system.

The scale ladder therefore starts much too far from the NO boundary.  A viable correlation
component must reach `C_t=O(1)` at this endpoint.

## 1. A formula-defined legal discrete ladder

Take sufficiently large odd `N` and set

```text
D=floor(N^(2/3)),
s_min=ceil(sqrt(N)),
s_max=D.                                                  (29.3)
```

For every integer `s_min<=s<=s_max`, define

```text
H_s: (s,s), (0,N-2s).                                    (29.4)
```

These are legal `q=N` histograms with two occupied complementary pair-types.  Since
`2s_max=O(N^(2/3))<N`, the filler is positive for all large `N`.  Every `H_s` is YES and

```text
C_t(H_s)=s^2.                                             (29.5)
```

Thus

```text
C_t(H_{s_min})=Theta(N),
C_t(H_{s_max})=Theta(N^(4/3)),                            (29.6)
```

and consecutive rungs differ by

```text
C_t(H_{s+1})-C_t(H_s)=2s+1.                              (29.7)
```

The neutral local transport on one rung is

```text
U_s=delta_{H_{s+1}}-delta_{H_s}.                         (29.8)
```

It has zero mass, zero label correlation because both endpoints are YES, and TV two.  For any
actual orbit row `F`,

```text
<U_s,F>=F(H_{s+1})-F(H_s),                               (29.9)
```

so a coefficient sequence `a_s` produces the discrete-divergence moment transport

```text
sum_s a_s[F(H_{s+1})-F(H_s)].                            (29.10)
```

This is a literal local scale ladder, not a separated high-band extrapolator.

## 2. Adding the exact parity tail

Independently add the Phase-28 parity tail `T_N`, built from `L>D` switches plus a permanent split
core.  It obeys exactly

```text
sum T_N=0,
||T_N||_1=1,
<T_N,label>=0,
<T_N,F_gamma>=0       for every degree gamma<D,         (29.11)
```

and all its support lies at `C_t=Theta(N^(4/3))`.

Consequently a fixed amount of `T_N` supplies constant *absolute* high-tail mass without changing
any ladder moment equation or label correlation.  This part of the decoupling remains valid.

The question is therefore whether a combination of NO mass and local rungs (29.8) can carry
constant correlation while annihilating all degree-`<D` rows.  The scalar answer is no.

## 3. Scalar Chebyshev separator for the entire ladder

Let a proposed signed witness `W_N` have unit TV, zero mass, and support on arbitrary NO orbits
with `C_t=0`, arbitrary ladder/neutral YES support satisfying (29.1), and the parity tail.  Enlarge
the actual YES support to the whole real interval `[A_N,B_N]`; a separator on that larger interval
also separates the original support.

Define

```text
y_N(x)=(A_N+B_N-2x)/(B_N-A_N),
y_{0,N}=y_N(0)=(A_N+B_N)/(B_N-A_N)>1.                   (29.12)
```

For

```text
r_N=ceil(arcosh(4)/arcosh(y_{0,N})),                    (29.13)

p_N(x)=T_{r_N}(y_N(x))/T_{r_N}(y_{0,N}),                (29.14)
```

one has

```text
p_N(0)=1,
|p_N(x)|<=1/4       for every x in [A_N,B_N].           (29.15)
```

Since

```text
arcosh(y_{0,N})
 =2sqrt(A_N/B_N)(1+o(1))
 =Theta(N^(-1/6)),                                      (29.16)
```

equation (29.13) gives `r_N=Theta(N^(1/6))`.

The collision-partition identity from Phase 18 places `p_N(C_t)` in the actual orbit span by
query degree at most `2r_N=o(D)`.  If `b=1[C_t=0]` and the label is `f=1-2b`, exact annihilation
and zero total mass imply

```text
|<W_N,f>|
 =2|<W_N,b-p_N(C_t)>|
 <=2||W_N||_1 ||b-p_N||_infinity
 <=1/2.                                                   (29.17)
```

This already contradicts the required strict correlation above `2/3`.

## 4. Full-cutoff exponential correlation bound

The constant-error separator understates the obstruction.  Put

```text
r=floor((D-1)/2),
Q_N(x)=T_r(y_N(x)).                                      (29.18)
```

Then `Q_N(C_t)` is still an actual degree-`<D` row combination,

```text
|Q_N(x)|<=1       on [A_N,B_N],                         (29.19)

Q_N(0)=cosh(r arcosh(y_{0,N})).                         (29.20)
```

Let `w_0` be the total signed mass of all NO support.  Because every NO orbit has `C_t=0`, exact
annihilation gives

```text
|w_0| Q_N(0)
 =|int_{YES} Q_N(C_t)dW_N|
 <=||W_N|_{YES}||_TV
 <=1.                                                     (29.21)
```

Zero mass gives `<W_N,f>=-2w_0`, hence

```text
|<W_N,f>|
 <=2/cosh(r arcosh(y_{0,N}))
 =exp[-Theta(D sqrt(A_N/B_N))]
 =exp[-Theta(N^(1/2))].                                  (29.22)
```

This applies to any sign pattern, any neutral rung coefficients, and any separately added parity
tail, provided every YES point remains above the `Theta(N)` gap.

## 5. Necessary first-positive scale

The same calculation gives a useful design condition.  Let `B_N=Theta(N^(4/3))` and target
cutoff `D=Theta(N^(2/3))`.  To prevent (29.22) from driving correlation to zero, it is necessary
that

```text
D sqrt(A_N/B_N)=O(1),                                   (29.23)
```

or equivalently

```text
A_N=O(B_N/D^2)=O(1).                                    (29.24)
```

Thus neither a `Theta(N)` nor even a growing first-positive target count is compatible with this
route.  The correlation bridge must include YES orbits with `C_t=O(1)`, while the independent
parity component may still supply constant mass at `Theta(N^(4/3))`.

## 6. Why mixed multisymmetric rows cannot rescue the ladder

On the explicit ladder (29.4), mixed actual rows are functions of the split core `(s,s)` and the
filler `N-2s`; the local differences (29.9) do carry those mixed moments.  A sufficiently large
linear system of rung coefficients could therefore be posed.

But every solution to the full mixed system must also solve its scalar subspace.  Equations
(29.17) and (29.22) use actual scalar-row combinations already present below the cutoff.  Adding
mixed constraints only shrinks the annihilating kernel and cannot increase its possible label
correlation.

Accordingly no mixed-moment right inverse, however well conditioned, can repair the
`C_t=Theta(N)` boundary gap in this node.

## 7. Bounded checks

Command:

```text
python ksum/tools/ksum_l2p29_qn_multiscale_ladder_check.py
```

Driver SHA-256:

```text
71adf46c9547caf1902ee2d114f2f211c0c44cf35ff1be0bad87b62316e22057
```

Raw log:
`ksum/artifacts/logs_ksum_L2p29_qN_multiscale_ladder_20260721/run.json`

For `N=1001,8001,64001,512001`, the formula ladder is legal.  The query degrees needed for the
error-`1/4` separator are respectively

```text
8,10,14,20,                                               (29.25)
```

while target cutoffs are

```text
100,400,1600,6400.                                       (29.26)
```

The corresponding full-cutoff base-10 correlation upper bounds have logarithms approximately

```text
-13.51,-38.97,-110.07,-311.56.                           (29.27)
```

These checks evaluate the displayed formulas and legality only; no alternative support was
searched.

## 8. New escape generated and not tested

The necessary scale (29.24) generates one distinct escape:

> **near-zero correlation bridge plus independent parity tail** — replace the `Theta(N)` bridge
> by a legal boundary-jet correlation component reaching `C_t=O(1)`, while retaining the exact
> correlation-neutral parity reservoir at `Theta(N^(4/3))`, and solve their remaining mixed
> cross-moment equations.

This route is only named.  It was not constructed or tested.  Under DAG Rule 8 it requires a
canonical node before follow-up work.

## 9. Gate ledger

| obligation | result |
|:---|:---|
| formula-defined local scale ladder | PASS: (29.3)-(29.10) |
| legality for all large odd `N` | PASS |
| separate exact parity tail | PASS from Phase 28 |
| constant absolute high tail | available from parity component |
| scalar moment transport with constant correlation | **OBSTRUCTED** by (29.17) |
| full-cutoff correlation | exponentially small by (29.22) |
| mixed actual rows | cannot repair scalar failure |
| bounded `l1`, correlation `>2/3`, exact moments | NOT OBTAINED |

## 10. Scoped conclusion

Localizing the transport in `C_t` removes the Phase-28 single-jump extrapolation, but it does not
remove the gap from NO.  A ladder beginning at `Theta(N)` is uniformly easy for actual scalar
orbit rows long before the target cutoff.  In fact the cutoff forces any constant-correlation
bridge to reach `C_t=O(1)`.

This is Decision B for the scale range stated by the node.  It is not a global obstruction to a
near-zero boundary bridge combined with the exact high-tail parity reservoir.  The controlling
node remains open, and no `PROVED`, `CERTIFIED*`, or `REFUTED` claim is made.
