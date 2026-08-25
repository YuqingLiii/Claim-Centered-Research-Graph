# k-Sum L2 phase-25 analytic proposer — mesoscopic split-opening cascade

Date: 2026-07-21

Controlling node: `KSUM.B4b.L2.ALT.mesoscopic-split-opening-cascade`

Scope: `q=5`, `K=2`, `D=Theta(sqrt N)`; only the exact paired jump family
`H_+^(s)-H_-^(s)` from Phase 24.  No full-orbit LP or support search.

Tier: proposer derivation only; no independent review and no completion-tier claim.

## Decision

**Decision B — the canonical mesoscopic ladders exhibit a sharp norm-versus-tail obstruction.**

The exact jump-family annihilation problem reduces completely to a one-variable
falling-factorial moment kernel.  This makes three natural ladders exactly solvable:

1. A dyadic/geometric ladder has only `O(log N)` nodes and therefore has no nonzero kernel for
   `D=Theta(sqrt N)`.
2. A degree-sized arithmetic ladder reaching `s=Theta(N)` has a unique finite-difference kernel.
   It gives constant macroscopic tail fraction, but fixing the `s=2` coefficient to one costs
   `exp(Theta(D))/N` in `l1` norm.
3. A degree-sized quadratic ladder `s_j=2+h j^2` has a unique closed-form barycentric kernel with
   uniformly bounded `l1` norm relative to its `s=2` coefficient.  But its coefficient mass at
   `s=Theta(N)` is `exp(-Theta(D))`.

Thus inserting intermediate scales does avoid the Phase-24 exponential amplification **or** keep
a constant `C_t=Theta(N)` tail, depending on the schedule, but neither tested formula-defined
cascade does both.  This is a scoped obstruction for the canonical minimal ladders, not a theorem
against every overcomplete or non-paired cascade.

## 1. Exact reduction of every jump-family row

Recall

```text
H_+^(s)={(1,s-1),(0,N-s)},       C_t=s-1,
H_-^(s)={(0,s),(0,N-s)},         C_t=0,                 (25.1)
```

and let `Delta_s(phi)=phi(H_+^(s))-phi(H_-^(s))` for an actual orbit row `phi`.
Phase 24 showed

```text
Delta_s(z,w)
 =-(z-w)^2 sum_{j=0}^{s-2}(1+z)^(s-2-j)(1+w)^j.         (25.2)
```

Every coefficient of local query degree `e` is therefore a polynomial in `s` of degree at most
`e-1`, vanishing at `s=1`; hence it is `(s-1)` times a polynomial of degree at most `e-2`.

For a two-slot row of total query degree `e+c<D`, the other slot is the unsplit filler and
contributes `(N-s)_c`, a polynomial of degree `c` in `s`.  Consequently, for every actual row of
degree `<D`,

```text
Delta_s(phi)=(s-1) R_phi(s-2),
deg R_phi <= D-3.                                       (25.3)
```

Conversely, the one-sided local rows give

```text
Delta_s(0,a)=-a(s-1)_(a-1),       2<=a<D,               (25.4)
```

so they span `(s-1)` times every polynomial in `s-2` of degree at most `D-3`.

For

```text
W_lambda=sum_s lambda_s
 (delta_{H_+^(s)}-delta_{H_-^(s)}),                     (25.5)
```

put

```text
t=s-2,       mu_s=(s-1)lambda_s=(t+1)lambda_s.          (25.6)
```

Equations (25.3)-(25.4) prove the exact equivalence

```text
W_lambda annihilates all orbit rows of degree <D
iff
sum_s mu_s P(t_s)=0 for every polynomial deg P<=D-3.    (25.7)
```

Thus the two-slot filler rows add no hidden conditions inside this paired family.  The problem is
exactly a weighted univariate cubature kernel, with coefficient norm

```text
||lambda||_1=sum_s |mu_s|/(t_s+1).                       (25.8)
```

When all used `s` lie below `N/2`, the YES and NO orbit atoms in (25.5) are distinct, so

```text
||W_lambda||_1=2||lambda||_1,
<label,W_lambda>=2 sum_s lambda_s.                       (25.9)
```

The absolute mass on high-`C_t` YES atoms is the corresponding high-`s` coefficient mass; NO
partners have `C_t=0`.

## 2. General minimal-ladder kernel

Write

```text
m=D-2.                                                   (25.10)
```

The constraints in (25.7) have dimension `m`.  On `m+1` distinct ladder nodes
`t_0,...,t_m`, their nullspace is one-dimensional.  The unique kernel, up to scale, is the
barycentric vector

```text
mu_j = C / product_{k!=j}(t_j-t_k),
lambda_j = mu_j/(t_j+1).                                 (25.11)
```

After fixing `lambda_0=1` at the corner node `t_0=0`, (25.11) is also the unique feasible vector
and hence automatically has the minimum `l1` norm on that fixed minimal support.  This lets us
compare schedules without an LP.

## 3. Sparse dyadic or fixed-ratio geometric ladder: infeasible

Take, for example,

```text
t_j=2^j,    0<=j<=floor(log_2 N),                        (25.12)
```

together with the corner node `t=0`.  Any fixed-ratio geometric schedule has `O(log N)` distinct
legal nodes before reaching `Theta(N)`.  For `D=Theta(sqrt N)`, this is eventually fewer than the
`m=D-2` independent constraints in (25.7).

The rectangular Vandermonde matrix has full column rank, so its kernel is zero.  Equivalently,
the minimum `l1` norm subject to `lambda_0=1` is infinite because the constraints are infeasible.
Merely listing one node per scale is not a cascade kernel; every viable ladder needs
`Omega(D)` distinct nodes.

## 4. Arithmetic full-range ladder: tail survives, norm explodes

Let

```text
t_j=Hj,       0<=j<=m,
H=floor(cN/m) for a fixed 0<c<1/2,                       (25.13)
```

with a harmless final adjustment of `H` so `t_m+2<N/2`.  This is a degree-sized densification of
the scale bridge, ending at `Theta(N)` while keeping all paired atoms distinct.

The barycentric formula gives, after `lambda_0=1`,

```text
mu_j=(-1)^j binom(m,j),
lambda_j=(-1)^j binom(m,j)/(Hj+1).                       (25.14)
```

Therefore

```text
L_arith:=||lambda||_1
 =sum_{j=0}^m binom(m,j)/(Hj+1).                         (25.15)
```

Since `Hj+1<=Theta(N)` and a constant fraction of binomial mass lies in
`j in [m/3,2m/3]`,

```text
L_arith >= 2^(m-O(1))/Theta(N)
          =exp(Theta(D))/N.                              (25.16)
```

The trivial upper bound `L_arith<=2^m` shows that the growth is exponential in `D`.  Moreover,
the same central binomial range has

```text
C_t=t_j+1=Theta(Hm)=Theta(N),                            (25.17)
```

so a constant fraction of the coefficient `l1` mass lies on high-`C_t` YES atoms.  After
normalization, this schedule keeps a constant macroscopic tail but makes the corner coefficient
at most `N exp(-Theta(D))`.

The signed label correlation of this kernel is also exponentially small.  Indeed,

```text
sum_j lambda_j
 = (1/H) B(1/H,m+1),                                    (25.18)
```

by the beta-integral identity, whereas (25.15) is exponential.  This strengthens, but is not
needed for, the norm obstruction.

## 5. Quadratic multiscale ladder: norm stays bounded, tail disappears

Fix an integer `h>=1` and choose

```text
t_j=h j^2,       0<=j<=m,                               (25.19)
```

with `hm^2<=cN` for some fixed `0<c<1/2`.  Taking
`D=m+2=Theta(sqrt N)` makes this a legal exact ladder.  It begins with bounded and mesoscopic
scales and reaches `Theta(N)`.

The products in (25.11) are explicit:

```text
product_{k!=0}(0-k^2)=(-1)^m(m!)^2,
|product_{k!=j}(j^2-k^2)|=(m-j)!(m+j)!/2,   j>=1.       (25.20)
```

After fixing `lambda_0=1`, the unique coefficients are

```text
lambda_0=1,
lambda_j=2(-1)^j q_{m,j}/(1+h j^2),
q_{m,j}=(m!)^2/((m-j)!(m+j)!),       1<=j<=m.           (25.21)
```

Because `0<q_{m,j}<=1`,

```text
||lambda||_1
 <=1+2 sum_{j>=1}1/(1+h j^2)
 <=1+pi^2/(3h).                                         (25.22)
```

So this genuine multiscale cascade eliminates the exponential coefficient amplification.

But it does so by suppressing the far scales.  From

```text
q_{m,j}
 =product_{ell=0}^{j-1}(m-ell)/(m+ell+1)
 <=exp(-j^2/(2m)),                                      (25.23)
```

every macroscopic node `t_j>=alpha N` has `j>=gamma m` for a fixed `gamma>0`, and therefore

```text
sum_{t_j>=alpha N}|lambda_j|
 <=2m exp(-gamma^2 m/2)
 =exp(-Theta(D)).                                       (25.24)
```

Since the total norm is at least one, the normalized high-`C_t` tail fraction vanishes
exponentially.  The quadratic ladder keeps a nonnegligible corner jet, but does not transport its
mass to the normal layer.

For completeness, the alternating label correlation can be bounded from below when `h` is large:
the terms in (25.21) decrease in magnitude, hence

```text
|sum_j lambda_j|/sum_j|lambda_j|
 >=(1-2/(1+h))/(1+pi^2/(3h)).                            (25.25)
```

For example `h=64` makes the right side greater than `0.92`.  Thus the failure of this schedule
is specifically the high-`C_t` tail, not necessarily corner correlation.

## 6. Why superposing a separate tail kernel does not repair the stated gate

One can place an independent arithmetic finite-difference kernel entirely in a macroscopic
interval and add it to the quadratic corner kernel.  This preserves exact annihilation and makes
the coefficient norm finite after separate normalization.  It does not provide the required
combined discriminator within this paired family:

- every paired jump contributes equal absolute mass to one YES and one NO atom;
- hence a unit-`l1` tail-only paired kernel has at most `1/2` high-`C_t` mass;
- obtaining high-`C_t` mass at least `1/4` requires the tail-only component to occupy at least
  half of the total `l1` budget;
- its correlation is exponentially small by the same beta-integral argument as (25.18).

For the exploratory `1/4` tail gate used in the finite endpoint checks, a disjoint tail component
must therefore consume at least half of the total norm.  Even granting correlation one to the
remaining corner component, the combined correlation is at most `1/2+exp(-Theta(D))`, below
`2/3`.  This is not a universal upper bound on every superposition, but it shows that the obvious
disjoint direct sum does not simultaneously meet the known gates.

## 7. Gate ledger

| tested obligation | result |
|:---|:---|
| exact reduction of all jump-family rows | PASS: (25.3)-(25.7) |
| dyadic/fixed-ratio ladder | FAIL: too few nodes, zero kernel |
| arithmetic degree-sized ladder | exact kernel, but `l1/lambda_0=exp(Theta(D))/N` |
| arithmetic high-`C_t` tail | PASS at coefficient-fraction level |
| quadratic degree-sized ladder | exact kernel and bounded `l1/lambda_0` |
| quadratic high-`C_t` tail | FAIL: `exp(-Theta(D))` |
| bounded norm and constant tail on one tested ladder | FAIL |
| correlation above `2/3` plus tail gate | FAIL for the tested constructions |
| universal obstruction to overcomplete cascades | NOT CLAIMED |

## 8. Scoped conclusion

For the exact split-opening family, `D=Theta(sqrt N)` annihilation is precisely a weighted
one-variable moment problem.  A sparse geometric hierarchy is dimensionally impossible.  Once
the hierarchy is densified to the necessary `Theta(D)` nodes, the two simplest analytic node
geometries sit on opposite sides of a sharp tradeoff:

```text
full-range arithmetic nodes:  constant tail, exponential corner cost;
quadratically clustered nodes: bounded corner cost, exponential tail loss.   (25.26)
```

The mesoscopic idea therefore does not yet supply the required legal discriminator.  The node
remains open because this memo does not optimize over redundant ladders with more than `D-1`
nodes, nor over non-paired orbit combinations.

No distinct escape was generated beyond those already contained in the controlling node.  No
`PROVED`, `CERTIFIED*`, or `REFUTED` status is claimed.
