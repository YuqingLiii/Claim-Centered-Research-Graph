# k-Sum L2 phase-27 analytic/numerical proposer — phase-subexposed correlation reservoir

Date: 2026-07-21

Controlling node:
`KSUM.B4b.L2.ALT.phase-subexposed-correlation-reservoir`

Scope: characterize legal `q=5`, `K=2` strata invisible to every fixed positive-minority WKB
direction and test one formula-defined signed reservoir there.  No broad support search or LP is
performed.

Tier: proposer derivation plus bounded exact-kernel checks; no independent review and no
completion-tier claim.

## Decision

**Decision B for a correlation-carrying subexposed reservoir; the controlling node remains OPEN.**

The relevant legal strata are nonempty and large.  In particular, if two slots have macroscopic
totals bounded away from zero but at least one queried minority occupancy is `o(N)`, every WKB
direction with a fixed positive minority ratio is beaten by a macroscopic interior orbit.  At
`m=lambda D` the gap is `Theta(D log D)`.

A four-orbit formula-defined reservoir on such a stratum achieves, before enforcing all rows,

```text
normalized correlation =0.7536945813 >2/3,
normalized high-tail mass=0.6231527094,                 (27.1)
```

and exactly cancels the first three *polynomial* moments of `lambda`.

It nevertheless fails the actual orbit rows.  The boundary directions `beta=j/D ->0` retain the
order-one major-occupancy factor `exp(-t lambda)`.  The reservoir is therefore read by a Laplace
transform, not by its first few polynomial moments.  Its WKB-normalized defects converge to
nonzero constants, including a nonzero `j=0` defect.  Canceling that defect with macroscopic bulk
requires `Theta(1)` exposed signed mass and re-enters the Phase-26 obstruction.

More generally, uniqueness of the Laplace transform shows that a bounded-TV reservoir supported
at `lambda>=lambda_0>0` cannot look like NO for a continuum of fixed-index high-degree rows unless
its signed high-tail measure vanishes.  It may still carry *unsigned* high-tail mass through
positive/negative pairing, but then it cannot by itself carry constant correlation.

## 1. Macroscopic exposure classification

Write the four oriented occupancy fractions as

```text
x=(r_1/N,u_1/N,r_2/N,u_2/N),       x_c>=0,
sum_c x_c=1,                                             (27.2)
```

modulo within-slot and slot exchanges.  A two-slot WKB query with strictly positive scaled
exponents `theta_c` has leading phase

```text
Phi_theta(x)=sum_c theta_c log x_c.                     (27.3)
```

On the macroscopic simplex, strict concavity gives its unique oriented maximizer

```text
x_c=theta_c/sum_d theta_d.                              (27.4)
```

Thus every all-positive macroscopic orbit is exposed by choosing `theta` proportional to its
occupancy vector.  Conversely, any face on which a coordinate carrying a fixed positive exponent
is `o(1)` has phase `-infinity` in the macroscopic limit and cannot be exposed by that direction.

For a one-slot positive-minority row, the corresponding phase is

```text
alpha log q+beta log v,       q+v<=1,
alpha,beta>0.                                       (27.5)
```

Its maximum occurs at

```text
q=alpha/(alpha+beta),
v=beta/(alpha+beta),
q+v=1.                                                   (27.6)
```

Therefore a one-slot orbit is exposed only if that slot contains `1-o(1)` of all occupancy and
both sides are macroscopic.  Combining (27.4) and (27.6), an orbit is exposed by at least one
positive-minority `rho=1` or `rho=2` direction only in either of these cases:

1. one complementary-pair slot contains asymptotically all occupancy and is macroscopically
   split;
2. both slots are macroscopic and all four oriented cells queried with positive exponents are
   macroscopic.

Legal orbits outside these cases are universally subexposed for the fixed-positive-minority
direction class.  In particular, the regular transition face

```text
H_{sigma,lambda}:
tau_1=(lambda D,N sigma-lambda D),
tau_2=(0,N(1-sigma)),
delta<=sigma<=1-delta,
0<lambda=O(1),                                           (27.7)
```

is legal, YES, and subexposed for every such direction.

## 2. Quantitative phase gap

For `m=lambda D` and a fixed positive minority exponent `b=beta D`, the reservoir factor contains

```text
(m/N)^b=(lambda D/N)^{beta D}.                          (27.8)
```

Relative to the macroscopic optimizer (27.6),

```text
log(K_reservoir/K_max)
 =-beta D log(N/D)+O(D)
 =-beta D log D+O(D)                                    (27.9)
```

when `N=Theta(D^2)`.  This is stronger than an ordinary `exp(-cD)` phase gap.  The reservoir is
invisible to all WKB directions with `beta>=beta_0>0` after the exposed bulk is canceled.

For directions with a positive minority exponent on the unsplit second slot in (27.7), the row
is exactly zero rather than merely subexponential.

The characterization has an important boundary caveat: it is not uniform as `beta ->0`.  The
fixed-index regime `b=j=O(1)` is the boundary layer of direction space and is analyzed below.

## 3. Formula-defined four-orbit reservoir

Set `N=D^2`, take `D` divisible by `100`, and fix `sigma=1/2`.  Choose

```text
lambda=(1/50,1/5,2/5,7/10),                            (27.10)

H_i:
tau_1=(lambda_i D,N/2-lambda_i D),
tau_2=(0,N/2).                                           (27.11)
```

The comparison NO orbit is

```text
H_0: tau_1=(0,N/2), tau_2=(0,N/2).                     (27.12)
```

Let `w_i` be the Lagrange weights representing evaluation at zero on the four positive nodes:

```text
w_i=prod_{k!=i} (-lambda_k)/(lambda_i-lambda_k).        (27.13)
```

Explicitly,

```text
w=(3500/2907,-14/45,7/57,-4/255).                       (27.14)
```

They obey

```text
sum_i w_i=1,
sum_i w_i lambda_i^j=0,       j=1,2,3.                 (27.15)
```

Define the signed reservoir candidate

```text
mu_D=sum_i w_i delta_{H_i}-delta_{H_0}.                 (27.16)
```

It has zero total mass.  Every `H_i` is YES and has

```text
C_t=lambda_iD(N/2-lambda_iD)=Theta(ND)=omega(N),        (27.17)
```

whereas `H_0` is NO.  Its total variation and normalized statistics are

```text
sum_i|w_i|=1.6535947712,
||mu_D||_1=2.6535947712,

correlation(mu_D)=2/||mu_D||_1=0.7536945813,
tail(mu_D)=sum_i|w_i|/||mu_D||_1=0.6231527094.          (27.18)
```

Thus legality, zero mass, correlation, and high tail all pass before the remaining moment rows
are imposed.

## 4. Exact fixed-index row seen by the reservoir

Take `h=alpha D` with `alpha=3/4`, so `h>max_i lambda_iD`, and take a fixed minority index
`j=0,1,2,3`.  Put `n=N/2`.  The exact split-slot identity is

```text
2A_{h,j}(lambda_iD,n-lambda_iD)
 = (lambda_iD)_j(n-lambda_iD)_h.                        (27.19)
```

After the common tangential normalization by `(n)_h`, define

```text
R_0(D)
 :=sum_i w_i (n-lambda_iD)_h/(n)_h-1,                  (27.20)

R_j(D)
 :=sum_i w_i [(lambda_iD)_j/D^j]
              [(n-lambda_iD)_h/(n)_h],       j>=1.     (27.21)
```

Since

```text
(n-lambda D)_h/(n)_h
 ->exp(-2 alpha lambda),                                (27.22)
```

the limiting defects are

```text
R_0 ->sum_i w_i exp(-2alpha lambda_i)-1,
R_j ->sum_i w_i lambda_i^j exp(-2alpha lambda_i).       (27.23)
```

Polynomial cancellation (27.15) does not cancel these Laplace-weighted moments.

At `alpha=3/4`, the bounded run gives

```text
R_0 -> approximately -1.61e-4,
R_1 -> approximately  3.90e-4,
R_2 -> approximately -6.58e-4,
R_3 -> approximately  5.96e-4.                         (27.24)
```

The natural finite-row defect for `j>=1` is `D^{-j}R_j(D)`.  Hence:

- `j=0` leaves a constant defect;
- `j=1` leaves `Theta(D^{-1})`;
- `j=2` leaves `Theta(D^{-2})`;
- `j=3` is only `Theta(D^{-3})`, not `o(D^{-3})`.

The formula candidate therefore misses the requested canonical defect threshold even though it
cancels three raw powers of `lambda` exactly.

## 5. Laplace-transform obstruction

The preceding failure is not special to four nodes.  Let `eta_D` be a signed bounded-TV measure
on a fixed transition band `lambda in [lambda_0,Lambda]`, with `lambda_0>0`, and suppose it is
intended to replace a unit NO mass on a fixed regular tangential fiber.  The `j=0` high-degree rows
require

```text
int exp(-t lambda) d eta_D(lambda) ->1                 (27.25)
```

for a continuum of `t=alpha kappa^2/sigma>0`, while the constant row requires

```text
int d eta_D=1.                                          (27.26)
```

Every weak-* limit has support in `[lambda_0,infinity]` and bounded TV.  Analytic uniqueness of
the Laplace transform applied to (27.25)-(27.26) forces the limit to be `delta_0`, contradicting
that support.  Therefore the uniform `j=0` defect cannot tend to zero.

If support is allowed to approach zero, the same argument shows that every signed component which
actually carries the NO-matching mass concentrates at `lambda=0`.  A constant signed component
remaining at `lambda>=lambda_0` is detected by some fixed-index direction.

Thus a universally positive-`beta`-subexposed stratum is not invisible to the full orbit feature
space: the `beta=j/D` boundary layer recovers its Laplace transform.

## 6. Can exposed bulk cancel the defect?

The positive-`beta` reservoir contribution is superexponentially small relative to exposed bulk,
so those rows could in principle be canceled by tiny bulk adjustments.  The `j=0` defect (27.24)
is different: it is order one in its own WKB normalization.  Canceling it for a continuum of
`alpha` requires an order-one exposed bulk signed functional.

Phase 26 showed that an exposed family with order-one signed density either leaves an order-one
canonical defect or must pair positive and negative densities locally, making its signed mass
zero.  Therefore the proposed reservoir does not avoid the exposed-phase problem; its
fixed-index boundary rows feed an order-one defect back into it.

This conclusion is already present in the one-slot row subspace.  Two-slot rows cannot repair it.
For example, multiplying (27.19) by a high-only row on the unchanged unsplit second slot merely
multiplies (27.20)-(27.21) by a common nonzero factor.  Rows with positive minority degree on the
second slot vanish exactly, adding no corrective freedom.

## 7. What remains possible

The obstruction concerns *signed correlation mass* stored on a uniformly subexposed high-tail
stratum.  It does not forbid placing equal positive and negative YES mass there.  Such a paired
component can retain constant absolute high-tail mass while contributing zero to every signed
mass and label-correlation balance.

Therefore Phase 27 separates two jobs that this candidate tried to perform simultaneously:

```text
high-tail absolute mass: may live on a correlation-neutral subexposed reservoir;
signed YES/NO correlation: must be carried by a different boundary-layer component.   (27.27)
```

Whether the two components can be coupled through all fixed-index and two-slot equations remains
untested here.

## 8. Bounded numerical checks

Command:

```text
python ksum/tools/ksum_l2p27_subexposed_reservoir_check.py
```

Driver SHA-256:

```text
1d395c8d060b48106e4c9afa4c435104d18e8603035d2c63afe64be2ba7729f5
```

Raw log:
`ksum/artifacts/logs_ksum_L2p27_subexposed_reservoir_20260721/run.json`

For `D=100,200,400,800`, the positive-`beta` example had

```text
log(K_reservoir/K_max)
 =-95.74,-218.65,-492.21,-1094.78,                     (27.28)
```

and the ratio to `D log D` approached about `-0.20`, confirming (27.9).  Meanwhile the
WKB-normalized fixed-index defects approached the nonzero constants in (27.24).  The script also
checks the exact rational weights, correlation, tail, and raw polynomial moments.

These are value checks of the displayed formula, not a broader support search.

## 9. New escape generated and not tested

The analysis generates one distinct escape:

> **correlation/tail-decoupled two-reservoir coupling** — use a signed boundary-jet component for
> YES/NO correlation and a separately phase-paired, correlation-neutral subexposed component for
> constant absolute `C_t=omega(N)` tail, then solve only their cross-coupling fixed-index and
> two-slot equations.

This route is only named and was not constructed or tested.  Under DAG Rule 8 it needs a canonical
node before any follow-up work.

## 10. Gate ledger

| obligation | result |
|:---|:---|
| legal universally positive-`beta`-subexposed strata | CHARACTERIZED: (27.2)-(27.9) |
| explicit signed reservoir | CONSTRUCTED: (27.10)-(27.16) |
| zero mass, legality | PASS |
| normalized correlation `>2/3` before moments | PASS: `0.75369` |
| constant high tail before moments | PASS: `0.62315` |
| positive-`beta` subexposure | PASS with `Theta(D log D)` gap |
| fixed-index one-slot rows | FAIL: nonzero Laplace defects |
| canonical defect `o(D^-3)` | FAIL |
| bounded-TV exposed correction | NOT OBTAINED; order-one `j=0` defect |
| two-slot rows | inherit the one-slot failure |
| full node | NOT COMPLETION-ADJUDICATED |

## 11. Scoped conclusion

Subexposed high-tail strata exist, and they can support excellent raw correlation/tail numbers.
But “subexposed for every fixed positive minority direction” is not enough.  The full query family
contains the singular boundary `beta=j/D`, where fixed-index high-degree rows recover the
reservoir's Laplace transform.  A bounded-TV high-tail signed measure cannot imitate NO across
that continuum unless its signed mass collapses to `lambda=0`.

This is Decision B for a single reservoir asked to carry both correlation and tail.  It does not
rule out a correlation-neutral high-tail component coupled to a separate correlation witness.
The controlling node remains open, and no `PROVED`, `CERTIFIED*`, or `REFUTED` claim is made.
