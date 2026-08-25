# k-Sum L2 phase-25 analytic audit — uniformly stable exactor

Date: 2026-07-21

Controlling node:
`KSUM.B4b.L2.ALT.iterated-multiscale-boundary-compactification`

Scope: only the exact-correction/right-inverse problem for `q=5`, `K=2`,
`D=Theta(sqrt N)`; no full correlation LP, no support search, and no DAG edit

Tier: proposer-tier functional analysis; no independent Rule-7 review and no completion-tier claim

## Decision

**Decision C — there is a norm-sharp nonlinear exactor and a concrete polynomial-norm linear
exactor, but neither converts the presently available leading multiscale cancellation into a small
finite correction. A Chebyshev gate gives a constant lower-bound obstruction to naive normal-layer
rounding.**

The basis-independent moment defect of a candidate signed measure `mu` is

```text
delta_N(mu)
 = sup{|<p,mu>| : p in V_<D, ||p||_{infinity,Omega_N}<=1}.        (25.1)
```

Its exact meaning is

```text
delta_N(mu)=inf{||mu-w||_1 : w annihilates V_<D}.                 (25.2)
```

Thus a total-variation-small exact correction exists with sharp constant one if and only if
`delta_N(mu)=o(1)`. This is a metric, generally nonlinear Hahn-Banach exactor; no fixed basis or
condition number is hidden in the statement.

For a fully linear mechanism, a discrete Fekete basis of the complete orbit feature space gives an
explicit right inverse of canonical norm at most

```text
r_N=dim V_<D=D^3/48+O(D^2).                                      (25.3)
```

It therefore corrects a candidate by `o(1)` whenever the canonical defect is `o(D^-3)`. This is a
concrete, finite, testable sufficient condition, though not a uniform `O(1)` bound.

The obstruction is also concrete. A signed pair between a NO orbit and a YES orbit with
`C_t=cN` has perfect label correlation and the desired normal-layer tail, but its defect (25.1) is
bounded below by a positive constant. The witness is a degree-`<D` Chebyshev polynomial in `C_t`.
Hence atom-by-atom NO-to-normal rounding cannot be repaired with vanishing `l1` cost; cancellation
must already hold collectively for the full moving polynomial unit ball.

This does not exclude a jointly matched multiscale construction. It identifies its exact stable
lifting gate and shows that fixed leading kernels or coordinatewise moment errors are insufficient.

## 1. Canonical type of the exactor

Let `Omega_N` be the finite legal orbit set and let `V_N=V_<D` be the actual orbit-row space,
viewed as a subspace of `C(Omega_N)=l_infinity(Omega_N)`. Write

```text
J_N : V_N -> l_infinity(Omega_N)                         inclusion,
A_N=J_N^* : l_1(Omega_N) -> V_N^*,
(A_N mu)(p)=<p,mu>.                                      (25.4)
```

The codomain carries its canonical dual norm

```text
||ell||_{V_N^*}=sup{|ell(p)|: p in V_N, ||p||_infinity<=1}.       (25.5)
```

This formulation is invariant under all changes and nonzero rescalings of the row basis. In these
types, an exactor is a selection `R_N:V_N^*->l_1(Omega_N)` satisfying

```text
A_N R_N ell=ell.                                        (25.6)
```

If linearity is required, the minimum possible norm of `R_N` is exactly the projection constant of
`V_N` in `l_infinity(Omega_N)`. Indeed, `A_NR_N=I` implies

```text
R_N^* J_N=I_{V_N},
P_N=J_N R_N^*:l_infinity(Omega_N)->J_N(V_N)              (25.7)
```

is a projection with `||P_N||<=||R_N||`. Conversely, the adjoint of any projection onto `J_N(V_N)`
gives a right inverse of the same norm. Therefore “uniformly bounded linear exactor” is a
projection-constant claim about the complete moving polynomial space, not merely a bound on an
inverse evaluation matrix in a convenient coordinate system.

## 2. Sharp nonlinear exact correction

For any candidate `mu in l_1(Omega_N)`, define `delta_N(mu)=||A_Nmu||_{V_N^*}` as in (25.1).
The map `A_N` is the quotient map dual to the isometric inclusion `J_N`. Hahn-Banach gives

```text
||ell||_{V_N^*}
 = min{||rho||_1 : rho in l_1(Omega_N), A_Nrho=ell}.     (25.8)
```

Apply (25.8) to `ell=A_Nmu`. A minimizer `rho_N` exists because all spaces are finite. Then

```text
w_N=mu-rho_N,
A_Nw_N=0,
||rho_N||_1=delta_N(mu).                                 (25.9)
```

Taking the infimum over exact `w_N` proves (25.2). Thus (25.9) is a norm-one set-valued exactor.
If `||mu||_1=1`, correlation and absolute tail mass each change by at most `delta_N(mu)` before the
final normalization. Consequently fixed positive correlation and tail margins survive whenever

```text
delta_N(mu)=o(1).                                        (25.10)
```

This is the strongest basis-independent correction statement possible: by (25.2), no exactor can
move `mu` by less than `delta_N(mu)`.

The limitation is equally exact. Weak convergence against each fixed polynomial, or cancellation
of each fixed limiting kernel, does not imply (25.10), because the supremum in (25.1) ranges over
an `N`-dependent degree-`<D` unit ball.

## 3. Concrete Fekete-Lagrange linear exactor

The canonical nonlinear minimizer in (25.8) need not have a closed formula. A concrete linear
alternative can be built without solving the correlation LP.

Let `r_N=dim V_N`, choose any algebraic basis `P_1,...,P_{r_N}`, and choose an ordered legal orbit
set

```text
S_N=(H_1,...,H_{r_N})
```

maximizing the absolute evaluation determinant

```text
|det(P_j(H_i))_{i,j=1}^{r_N}|                           (25.11)
```

over all ordered `r_N`-tuples; break ties lexicographically. This definition is basis-independent
up to a common nonzero determinant factor. Let `L_i in V_N` be the fundamental Lagrange functions

```text
L_i(H_j)=1[i=j].                                         (25.12)
```

Replacing `H_i` by an arbitrary legal orbit `H` in (25.11) and using determinant maximality gives

```text
|L_i(H)|<=1 for every H in Omega_N.                      (25.13)
```

Define

```text
R_N^F ell = sum_{i=1}^{r_N} ell(L_i) delta_{H_i}.        (25.14)
```

Then, for every `p in V_N`, Lagrange interpolation gives

```text
<p,R_N^F ell>=sum_i ell(L_i)p(H_i)=ell(p),
```

so `A_NR_N^F=I` exactly. From (25.13),

```text
||R_N^F ell||_1
 <=sum_i ||ell||_{V_N^*}||L_i||_infinity
 <=r_N||ell||_{V_N^*}.                                  (25.15)
```

Phase 23 identified

```text
r_N=D^3/48+O(D^2),                                      (25.16)
```

so (25.14) is a concrete right inverse with `O(D^3)` canonical norm. Applied to a candidate `mu`,
it yields the exact legal correction

```text
rho_N^F=R_N^F A_Nmu,
||rho_N^F||_1<=r_N delta_N(mu).                          (25.17)
```

Hence

```text
delta_N(mu)=o(D^-3)                                      (25.18)
```

is a directly testable sufficient gate for this fully linear exactor.

If the moment space is instead assigned the moving coordinate norm
`||ell||=sum_i|ell(L_i)|`, (25.14) has norm exactly one. That statement is algebraically true but
does not establish asymptotic stability: the difficult quantity has merely moved into the norm of
the defect. Equations (25.1), (25.15), and (25.17) keep the conditioning visible.

The Fekete set is used only as an analytic exactor support. No determinant search was run, and it
is not proposed as the correlation witness or as a replacement for the finite correlation LP.

## 4. Constant lower bound for naive normal-layer rounding

Let

```text
T_N=max_{H in Omega_N} C_t(H)=N^2/4+O(N).                (25.19)
```

Phase 23's invariant algebra implies that every polynomial in `C_t` of ordinary degree at most

```text
m=floor((D-1)/2)                                         (25.20)
```

belongs to `V_N`: `C_t` has query weight two. For any integer `0<=j<=m`, define

```text
p_{N,j}(H)=T_j(1-2C_t(H)/T_N),                           (25.21)
```

where `T_j` is the Chebyshev polynomial. Since `0<=C_t<=T_N`,

```text
p_{N,j} in V_N,
||p_{N,j}||_{infinity,Omega_N}<=1.                       (25.22)
```

Fix `0<c<1` and take the legal orbits

```text
H_N^0={(0,N-1),(0,1)},                  C_t=0, label=-1,
H_N^c={(1,floor(cN)),(0,N-floor(cN)-1)}, C_t=floor(cN), label=+1. (25.23)
```

The signed pair

```text
mu_N=(delta_{H_N^c}-delta_{H_N^0})/2                    (25.24)
```

has zero total mass, unit `l1`, label correlation one, and absolute mass `1/2` at
`C_t=Theta(N)`. It is the simplest possible normal-layer collision.

Assume along a subsequence `D/sqrt N->kappa>0`. For `j_N=floor(theta m)` with fixed
`0<theta<=1`, the endpoint asymptotics give

```text
p_{N,j_N}(H_N^0)=1,
p_{N,j_N}(H_N^c)->cos(2 theta kappa sqrt(c)).             (25.25)
```

Choose `theta` so that the displayed cosine is not one. By (25.1), (25.22), and (25.24),

```text
liminf_N delta_N(mu_N)
 >= |1-cos(2 theta kappa sqrt(c))|/2
 >0.                                                     (25.26)
```

Combining (25.2) and (25.26), **every** exact degree-`<D` annihilator remains a fixed positive
`l1` distance from this pair. No choice of linear right inverse, basis, or lattice tie-breaking can
repair it with `o(1)` mass.

This is not a no-go for a distributed normal layer. It proves that normal YES/NO atoms must satisfy
the Chebyshev boundary profile collectively before exact correction is attempted. Fixed-polynomial
weak cancellation and atomwise rounding do not meet the canonical gate (25.10).

## 5. Rank obstruction for a fixed number of boundary rays

A second simple obstruction concerns exactor support. The full moment rank is

```text
r_N=Theta(D^3)=Theta(N^(3/2)).                            (25.27)
```

The one-dimensional ray `H_N(t)` in (25.23) has only `O(N)` legal lattice points. Any correction
operator supported on a fixed number of such one-parameter rays therefore has image dimension at
most `O(N)`, strictly below `r_N`. It cannot be a right inverse of the full orbit moment map.

Thus adding finitely many one-dimensional intermediate-scale charts can repair the Phase-24
coverage picture but cannot by itself supply a full exactor. A valid linear exactor needs a
genuinely higher-dimensional legal support or a number of rays growing at least as
`Omega(sqrt N)`.

## 6. Gate ledger

| obligation | result |
|:---|:---|
| basis-independent defect norm | PASS: (25.1), (25.4)-(25.5) |
| exact `l1` distance to the annihilator | PASS: Hahn-Banach identity (25.2), (25.8)-(25.9) |
| norm-one exact correction mechanism | PASS as a nonlinear/set-valued existence theorem |
| concrete linear right inverse | PASS: Fekete-Lagrange map (25.11)-(25.15) |
| canonical linear norm bound | PASS: at most `r_N=O(D^3)` |
| sufficient small-defect gate | PASS: `delta_N=o(D^-3)` for the displayed linear exactor; `delta_N=o(1)` for the minimal nonlinear exactor |
| uniform `O(1)` linear right inverse | OPEN: equivalent to a uniform projection-constant bound for `V_N` |
| leading/fixed-kernel cancellation implies small canonical defect | FAIL; the unit ball moves with `D` |
| atomwise NO/normal rounding | OBSTRUCTED by the constant Chebyshev lower bound (25.26) |
| fixed finite collection of one-dimensional exactor charts | FAIL by rank (25.27) |
| formula-defined correlation and tail witness | NOT ADDRESSED in this exactor-only phase |

## 7. Scoped conclusion

The exactor question has a clean answer once its norm is stated. In the canonical quotient norm,
there is always a norm-sharp exact correction, and the correction cost is exactly
`delta_N(mu)`. A discrete Fekete-Lagrange construction gives a fully linear exactor with explicit
`O(D^3)` norm. Therefore exact lifting is reduced to a precise uniform residual problem rather
than an unspecified rounding step.

The current multiscale program has not established the needed residual estimate. In fact, the
Chebyshev test (25.26) shows that the most tempting normal-layer two-atom collision has constant
canonical defect despite perfect label correlation and tail. Any successful construction must
cancel the complete moving degree-`<D` unit ball collectively and, for a linear Fekete correction,
to accuracy `o(D^-3)`.

No additional distinct escape route was generated in this phase. No `PROVED`, `CERTIFIED*`,
`NUMERICAL`, or `REFUTED` status is claimed.
