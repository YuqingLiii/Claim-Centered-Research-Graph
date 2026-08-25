# k-Sum L2 phase-27 analytic proposer — two-orientation shared-NO cascade

Date: 2026-07-21

Controlling node: `KSUM.B4b.L2.ALT.two-orientation-shared-no-cascade`

Scope: `q=5`, `K=2`, `D=Theta(sqrt N)`; exact paired split-opening family with both orientations
`s` and `N-s`.  No full-orbit LP.

Tier: proposer construction plus one exact rational self-check; no independent review and no
completion-tier claim.

## Decision

**Decision A — the shared-NO mechanism works at proposer tier.**

There is a formula-defined legal signed orbit measure which, for every sufficiently large odd
`N`, simultaneously has

```text
total mass                         0,
l1                                1,
annihilation degree               D=Theta(sqrt N),
normalized label correlation      >2/3,
absolute mass at C_t>=N/4         1/4.                  (27.1)
```

The construction has two exact components:

1. the Phase-25 quadratic corner bridge, normalized to `l1=1`, with correlation greater than
   `0.92` and no mass above `N/4` under the constants chosen here;
2. a new shared-NO null component, also normalized to `l1=1`, supported entirely on
   `C_t=Theta(N)` YES atoms, with zero label correlation.

Mixing them in proportions `3/4` and `1/4` gives tail mass exactly `1/4` and correlation greater
than `(3/4)(0.92)>2/3`.

The key is that coefficients of opposite sign on orientations `s` and `N-s` cancel their common
NO atom exactly.  What remains is a YES-to-YES signed transfer.  Its complete degree-`<D` moment
system has only about half the original rank after reflection, and an explicit barycentric kernel
solves it.

## 1. Shared-NO coefficient ledger

For

```text
J_s=delta_{H_+^(s)}-delta_{H_-^(s)},
H_+^(s)={(1,s-1),(0,N-s)},
H_-^(s)={(0,s),(0,N-s)},                                (27.2)
```

the reflected orientation satisfies

```text
H_-^(N-s)=H_-^(s).                                      (27.3)
```

Give `J_s` coefficient `a` and `J_(N-s)` coefficient `b`.  After merging identical orbit atoms,
the group is

```text
a delta_{H_+^(s)}
+b delta_{H_+^(N-s)}
-(a+b) delta_{H_-^(s)}.                                 (27.4)
```

Its exact orbit norm and label numerator are

```text
l1_group=|a|+|b|+|a+b|,
label_group=2(a+b).                                     (27.5)
```

Thus arbitrary NO cancellation is not free: taking `a=-b` also makes the group's label numerator
zero.  But it creates the useful label-null transfer

```text
a(delta_{H_+^(s)}-delta_{H_+^(N-s)}),                   (27.6)
```

whose entire norm lies on YES atoms.  If both orientations are macroscopic, all of that norm is
high-`C_t` tail mass.

## 2. Complete reflected moment system

Put

```text
x=s-1,
M=N-2.                                                   (27.7)
```

The reflected orientation has target-pair count

```text
x'=N-s-1=M-x.                                           (27.8)
```

Phase 25 proved that the exact orbit-row annihilation conditions for a coefficient vector in the
jump family are equivalent to

```text
sum_s lambda_s (s-1)_k=0,       1<=k<=m,
m=D-2.                                                   (27.9)
```

For the antisymmetric shared-NO choice

```text
lambda_s=b,
lambda_(N-s)=-b,                                        (27.10)
```

condition (27.9) becomes

```text
sum_j b_j F_k(x_j)=0,
F_k(x)=(x)_k-(M-x)_k,       1<=k<=m.                    (27.11)
```

Every `F_k` is antisymmetric about `M/2`.  With

```text
d=2x-M,
z=d^2,                                                   (27.12)
```

it has the exact form

```text
F_k(x)=d Q_k(z),
deg Q_k<=floor((k-1)/2).                                 (27.13)
```

Therefore all equations in (27.11) reduce to ordinary polynomial moments in `z` through degree

```text
r-1,       r=ceil(m/2).                                  (27.14)
```

This is the exact rank drop supplied by the shared-NO reflection.  It uses the complete actual
orbit-row system through the Phase-25 equivalence, not only the scalar `C_t` rows.

## 3. Explicit shared-NO tail kernel

Choose `r+1` consecutive integers

```text
x_j=floor(N/3)+j,       0<=j<=r,                         (27.15)
```

and define

```text
d_j=2x_j-M,
z_j=d_j^2.                                               (27.16)
```

For sufficiently large `N`, all `d_j` are nonzero and all `z_j` are distinct.  Let

```text
nu_j=1/product_{ell!=j}(z_j-z_ell),
b_j=nu_j/d_j.                                            (27.17)
```

The barycentric identity gives

```text
sum_j nu_j Q(z_j)=0       for every deg Q<=r-1.          (27.18)
```

Equations (27.13), (27.17), and (27.18) imply every condition in (27.11).  Hence

`lambda_(x_j+1)=b_j`, `lambda_(N-x_j-1)=-b_j` defines an exact annihilator for **all** orbit rows
of degree `<D`.

By (27.3), its NO coefficients cancel pairwise.  Its surviving orbit measure is

```text
K_raw=sum_j b_j
 (delta_{H_+^(x_j+1)}-delta_{H_+^(N-x_j-1)}).            (27.19)
```

Both target-pair counts `x_j` and `M-x_j` lie between `N/4` and `3N/4` for all sufficiently large
`N`.  Thus every atom of `K_raw` is a high-`C_t` YES atom.  Also

```text
total mass(K_raw)=0,
label numerator(K_raw)=0,
l1(K_raw)=2 sum_j|b_j|>0.                                (27.20)
```

Normalize (27.19) to obtain `K` with `l1(K)=1`.  It has tail mass one and correlation zero.

## 4. High-correlation corner bridge

Fix `h=64` and take

```text
m=D-2=floor(sqrt(N/512)),                                (27.21)
```

with an inconsequential bounded adjustment for very small `N`.  Then `D=Theta(sqrt N)` and

```text
64m^2<=N/8.                                              (27.22)
```

On the nodes

```text
s_j=2+64j^2,       0<=j<=m,                              (27.23)
```

use the exact quadratic coefficients

```text
lambda_0=1,
lambda_j=2(-1)^j (m!)^2/
 ((m-j)!(m+j)!(1+64j^2)),       1<=j<=m.                (27.24)
```

Phase 25 proved that these coefficients annihilate every actual row of degree `<D`.  All
`s_j<N/2`, so their YES and NO atoms are distinct and their exact normalized correlation is

```text
rho_B=|sum_j lambda_j|/sum_j|lambda_j|.                  (27.25)
```

The alternating magnitudes decrease, and

```text
rho_B
 >=(1-2/65)/(1+pi^2/192)
 >(63/65)/(101/96)
 =6048/6565
 >8/9.                                                   (27.26)
```

Here only the elementary bound `pi^2<10` was used in the second line.  Normalize the associated
orbit measure to obtain `B` with `l1(B)=1` and choose its global sign so its label correlation is
positive.  By (27.22), every bridge atom has `C_t<N/4` for sufficiently large `N`.

## 5. Final legal annihilator

Define

```text
W=(3/4)B+(1/4)K.                                        (27.27)
```

The two components have disjoint orbit supports: `B` lies below `N/4` in target-pair count, while
`K` lies above it.  Therefore norms and tail masses add exactly.  Both components have total mass
zero and annihilate all actual rows below `D`, so

```text
total mass(W)=0,
||W||_1=1,
F_<D W=0,
tail_{C_t>=N/4}(W)=1/4.                                 (27.28)
```

Since `K` has zero label numerator,

```text
corr(W)=(3/4)rho_B
       >(3/4)(6048/6565)
       =4536/6565
       >2/3.                                             (27.29)
```

Every orbit in (27.19), (27.23) is a legal two-slot `q=5` histogram with total occupancy exactly
`N`.  The formulas are integral before the rational weights are applied, so odd `N` requires no
rounding argument.

## 6. Exact finite self-check

The analytic identities were checked with exact rational arithmetic at

```text
N=20003, D=7, h=64.                                      (27.30)
```

The checker evaluates every raw `rho<=2` orbit row of total degree `<D`, not only the reduced
moment equations.  It returned

```text
bridge maximum exact row residual       0,
shared-NO maximum exact row residual     0,
merged shared-NO coefficient             0,
combined l1                              1,
combined tail mass                       1/4,
combined correlation
  114152177664/160381986377
  =0.7117518634... >2/3.                                 (27.31)
```

Reproduction:

```text
python ksum/tools/ksum_l2p27_shared_no_check.py \
  --N 20003 --D 7 --h 64 \
  --output ksum/artifacts/logs_ksum_L2p27_shared_no_20260721/run.json
```

Provenance:

```text
7D40BB5D97BCC5C59220FFCC7B9E3F0B4A3FC4658B06D6D601472BF41048DDA5
  ksum/tools/ksum_l2p27_shared_no_check.py
48BBAC269099C8C0426C79612989349326CD130D429FABE82B357D98300E789E
  ksum/artifacts/logs_ksum_L2p27_shared_no_20260721/run.json
```

This is a self-check of the displayed formulas, not an independent Rule-7 review.

## 7. Gate ledger

| obligation | result |
|:---|:---|
| merged shared-NO coefficient law | PASS: (27.4)-(27.6) |
| complete degree-`<D` moment reduction | PASS analytically: (27.9)-(27.14) |
| formula-defined shared-NO null kernel | PASS: (27.15)-(27.19) |
| legal odd-`N` orbit support | PASS by inspection of the formulas |
| total mass zero | PASS for both components |
| `l1=1` | PASS after explicit normalization |
| `D=Theta(sqrt N)` annihilation | PASS at proposer tier |
| correlation `>2/3` uniformly | PASS at proposer tier: lower bound (27.29) |
| constant `C_t=Theta(N)` tail | PASS: exactly `1/4` above `N/4` |
| exact finite raw-row self-check | PASS at `(N,D)=(20003,7)` |
| independent Rule-7 review | NOT DONE |

## 8. Scope and remaining obligations

This construction resolves the `q=5` endpoint inside the split-opening orbit family at proposer
tier.  It does not address the `q=N` endpoint, does not by itself provide a single endpoint-uniform
coefficient formula, and has not received an independent type/quantifier review.

No new escape direction was generated: the tested shared-NO mechanism itself succeeded.  No
`PROVED`, `CERTIFIED*`, or `REFUTED` status is claimed.
