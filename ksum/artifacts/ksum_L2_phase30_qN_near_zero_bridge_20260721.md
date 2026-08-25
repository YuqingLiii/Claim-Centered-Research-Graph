# k-Sum L2 phase-30 final bounded attempt — `q=N` near-zero bridge

Date: 2026-07-21

Controlling node:
`KSUM.B4b.L2.ALT.near-zero-bridge-independent-parity-tail`

Scope: one explicit formula-defined critical bridge whose `C_t` support reaches one and extends to
`Theta(N^(4/3))`, its complete growing mixed orbit projection at
`D=floor(floor(N^(2/3))/2)`, and an independent exact parity tail.  No broad support search or new
projection LP is performed.

Tier: exact proposer formulation plus reuse of archived bounded full-orbit projection data; no
independent review and no completion-tier claim.

## Decision

**Decision C — the requested exact coefficient law exists and cancels the complete growing mixed
orbit span, but the decisive asymptotic correlation inequality is a true formulation gap.**

Use the Phase-21 critical dense-palette support as the near-zero bridge.  It has
`Theta(D)` occupied pair levels, contains `C_t=1`, contains every scalar target count through
`Theta(N^(4/3))` in one component, and has a dense local product palette.  Define its signed
coefficients by the exact weighted projection of the NO indicator onto the full actual orbit
span.  This produces an explicit Gram-pseudoinverse coefficient law that annihilates every
fixed-index, two-slot, and higher injection row below `D`—not merely scalar powers of `C_t`.

Couple it on a disjoint support to the Phase-28 parity tail.  The parity tail independently
annihilates the same full row space and places all its absolute mass at
`C_t=Theta(N^(4/3))`.  Therefore the coupled law has, exactly,

```text
zero mass,
l1=1,
all actual moments below D equal to zero,
tail >=epsilon                                             (30.1)
```

for any fixed mixing constant `epsilon>0`.

The only remaining gate is

```text
Corr_bridge > (2/3)/(1-epsilon).                          (30.2)
```

For `epsilon=0.01`, the threshold is `0.6734006734`.  Existing exact-support numerical
projections pass this coupled threshold at `N=15,21` and fail it at `N=27,33`; the sequence is
nonmonotone and too small for an asymptotic verdict.  Phase 23 identifies the mixed moment
`sum_i s_i r_i u_i` as the first feature causing a finite threshold crossing and gives the exact
growing colored-partition Gram operator, but no asymptotic inversion or sign/`l1` control.

Thus the final bounded attempt does not lack a support, coefficient law, exact moment identity,
or tail mechanism.  It lacks a proof of one explicit residual inequality for a growing
multisymmetric projection.  No additional escape is named because no genuinely different route
was generated.

## 1. Critical bridge support

Take sufficiently large odd `N` and define

```text
L=floor(N^(2/3)),
D=floor(L/2),
U=ceil(2N^(1/3)),
M=L-U.                                                     (30.3)
```

The bridge base law is the exact mixture

```text
pi_N=(pi_bal+pi_dense)/2                                  (30.4)
```

from Phase 21, with overlapping histograms merged before assigning (30.4).

Its balanced component uses:

- `U` total-two unit pair-types, each in `(0,2)` or `(1,1)`;
- `M` bulk pair-types whose positive totals form an exact composition of `N-2U`, each total lying
  within two of its mean;
- conditional split law: inactive `(0,s)` with probability `1/2`, otherwise uniformly one of all
  positive unordered splits of total `s`.

Its dense component uses:

- exactly `L` positive pair totals satisfying `2<=s_i<=L+1` and `sum_i s_i=N`;
- conditional state `(0,s_i)` or `(1,s_i-1)`, each with probability `1/2`.

Both exact composition laws are uniform before their split choices and are pushed forward to
unordered histograms with their multinomial multiplicities.  This is a fully formula-defined
positive law on legal `q=N` orbits.

## 2. Required near-zero, multiscale, and palette properties

The bridge has the structural properties requested in Phase 30.

### Near-zero boundary

Activating one unit pair and leaving every other pair inactive gives

```text
C_t=1.                                                     (30.5)
```

All-inactive choices give distributed NO support with `C_t=0`.

### Continuous scalar scale

For every fixed balanced total vector, the unit pairs fill the gaps between consecutive bulk
split products.  The Phase-21 interval induction gives

```text
{C_t on that fiber}={0,1,...,T(s)},                       (30.6)
```

and for a maximizing composition

```text
T_N=(1/4+o(1))L^2=Theta(N^(4/3)).                        (30.7)
```

Thus one component reaches every scalar level from zero to the high scale, not merely a geometric
subsequence.

### Dense mixed palette

The dense component can prescribe a coordinate total `s=c+1` for every `1<=c<=L`; activating it
in state `(1,c)` gives local product

```text
ru=c.                                                      (30.8)
```

Hence the local positive product palette contains the full interval `{1,...,L}`.  Pair totals and
split products vary across `L=Theta(D)` coordinates under exact global composition constraints.
The support is not a one-parameter activation family.

## 3. Full actual mixed orbit space

For one unordered target slot put

```text
s_i=r_i+u_i,       x_i=r_i u_i.                           (30.9)
```

The exact actual degree-`<D` orbit span is the restriction of the multisymmetric polynomial space
generated by polarized power sums

```text
p_(a,b)=sum_i s_i^a x_i^b,
weight(p_(a,b))=a+2b,                                    (30.10)
```

and their products of total weight below `D`, modulo `p_(1,0)=N` and finite-slot relations.  This
is equivalent, by the falling-factorial triangular transform and collision-partition inversion,
to all actual fixed-index and multi-slot injection rows below the query cutoff.

Let `Lambda_D` index any spanning family

```text
P_lambda=product_j p_(a_j,b_j),
sum_j(a_j+2b_j)<D.                                       (30.11)
```

The size of `Lambda_D` grows with colored partitions; it is not held fixed in this construction.

## 4. Exact bridge coefficient law

Let

```text
b(H)=1[H is NO],

G_D(lambda,mu)=E_pi[P_lambda P_mu],
v_D(lambda)=E_pi[b P_lambda].                            (30.12)
```

Define

```text
c_D=G_D^dagger v_D,

g_D(H)=b(H)-sum_lambda c_D(lambda)P_lambda(H),

Z_D=E_pi[|g_D|].                                         (30.13)
```

If `Z_D=0`, this bridge is unavailable.  Otherwise set

```text
W_bridge(H)=pi(H)g_D(H)/Z_D.                             (30.14)
```

Equations (30.12)-(30.14) are a formula-defined coefficient law.  Every Gram entry is an explicit
finite collision-partition sum under the two exact composition laws.  No support coefficient is
chosen by an LP or post-hoc search.

Weighted orthogonality gives, exactly,

```text
sum_H W_bridge(H)P_lambda(H)=0       for all lambda,
sum_H W_bridge(H)=0,
||W_bridge||_1=1.                                        (30.15)
```

Since (30.11) spans the actual orbit rows, (30.15) proves exact annihilation of the complete
growing mixed orbit system.

The normalized bridge correlation is the explicit residual quantity

```text
C_N
 :=|<W_bridge,1-2b>|
 =2 E_pi[g_D^2]/E_pi[|g_D|].                             (30.16)
```

No tail estimate for `g_D` is needed in the coupled construction below.

## 5. Independent exact parity tail

Let

```text
J=D+1,
S=D,
R=N-2S-2J.                                                (30.17)
```

Use `J` labeled switches with states `(0,2)` and `(1,1)`, a permanent split core `(S,S)`, and an
unsplit filler `(0,R)`.  Push forward the signed product

```text
product_{i=1}^J (delta_(0,2)-delta_(1,1))/2.             (30.18)
```

As proved in Phase 28, the resulting `T_N` satisfies

```text
sum T_N=0,
||T_N||_1=1,
<T_N,label>=0,
<T_N,F_gamma>=0       for every actual degree gamma<D,  (30.19)

C_t in [S^2,S^2+J]=Theta(N^(4/3))                       (30.20)
```

on every support point.

For all large `N`, the bridge has exactly `L` occupied pair-types while the parity support has
`J+2=D+3`, so their supports are disjoint.  Both are within the `(N-1)/2` pair budget and have
positive fillers.

## 6. Exact coupled witness conditional on one inequality

Fix any constant `0<epsilon<1/3`; below take `epsilon=0.01`.  Define on the disjoint union

```text
W_N=(1-epsilon)W_bridge+epsilon T_N.                     (30.21)
```

Equations (30.15) and (30.19) give the exact identities

```text
sum W_N=0,
||W_N||_1=(1-epsilon)+epsilon=1,
<W_N,F_gamma>=0       for every actual degree gamma<D.  (30.22)
```

The parity component supplies

```text
Tail_N(C_t=Theta(N^(4/3)))>=epsilon.                     (30.23)
```

Because it is correlation-neutral,

```text
Corr(W_N)=(1-epsilon)C_N.                                (30.24)
```

Thus the entire endpoint theorem for this construction is equivalent to the single asymptotic
gate

```text
Z_D>0,
C_N>2/[3(1-epsilon)].                                    (30.25)
```

At `epsilon=0.01`, the numerical threshold is

```text
C_N>0.6734006734006733.                                  (30.26)
```

Every other requested property is already exact or has a fixed constant margin.

## 7. Why the remaining gate is genuinely non-scalar

At `D=4`, the full actual invariant space already contains

```text
1,
C=sum_i x_i,
S2=sum_i s_i^2,
S3=sum_i s_i^3,
M1=sum_i s_i x_i.                                        (30.27)
```

In the archived `N=27` critical mixture, scalar `{1,C}` gives correlation `0.6792618832`, above
the uncoupled `2/3` threshold.  Adding `M1` reduces it to `0.5954005611`, and the full space gives
`0.5861085065`.  Thus a scalar Chebyshev analysis cannot establish (30.25).

For general `D`, (30.12) is indexed by growing colored partitions.  The balanced and dense
component moment operators have different conditional split laws and are not simultaneously
diagonalizable.  Even an eigenvalue analysis would control `E[g_D^2]` but not the absolute-value
denominator `E|g_D|` in (30.16).  The missing result is therefore exactly:

```text
an asymptotic inversion plus sign/l1 theorem for (G_D,v_D)
at D=floor(L/2).                                         (30.28)
```

This is a well-typed statement, but no formula reducing it to a fixed-rank or separable operator
was found.

## 8. Bounded finite coupling check

No new projection solve was run.  The archived Phase-22 full-orbit projections were coupled
arithmetically to `epsilon=0.01`.

Command:

```text
python ksum/tools/ksum_l2p30_qn_near_zero_bridge_coupling.py
```

Driver SHA-256:

```text
a9978c4c7c5f1a47cc86f2850c06a0bbbd5940eb24b3ebb663d534ed6a2c6096
```

Raw log:
`ksum/artifacts/logs_ksum_L2p30_qN_near_zero_bridge_20260721/run.json`

Source projection log:
`ksum/artifacts/logs_ksum_L2p22_critical_dense_20260721/run.json`

The arithmetic results are:

| `N` | `L` | `D` | bridge correlation | coupled correlation |
|---:|---:|---:|---:|---:|
| 15 | 6 | 3 | 0.6948730742 | 0.6879243435 |
| 21 | 7 | 3 | 0.8042336153 | 0.7961912792 |
| 27 | 9 | 4 | 0.5861085065 | 0.5802474214 |
| 33 | 10 | 5 | 0.4705055710 | 0.4658005153 |

The first two arithmetic values pass (30.26); the last two fail.  These tiny cutoffs change rank
and support structure discontinuously and do not determine the asymptotic sign of (30.25).  The
`N=15` row should be read only as coupling arithmetic: asymptotic bridge/tail support disjointness
is guaranteed for large `N`, not asserted for that smallest instance.

## 9. Exact achievements and open gate

| obligation | result |
|:---|:---|
| legal near-zero-to-high bridge | PASS |
| `Theta(D)` pair levels and dense local palette | PASS |
| formula-defined coefficient law | PASS: (30.12)-(30.14) |
| complete scalar + mixed actual moments | EXACTLY CANCELED by (30.15) |
| independent exact parity tail | PASS |
| coupled zero mass and `l1=1` | PASS |
| constant high-tail mass | PASS: at least `epsilon` |
| correlation `>2/3` | equivalent to (30.25), **OPEN** |
| asymptotic `Z_D>0` | OPEN |
| growing Gram inversion and `l1` sign control | OPEN |

## 10. Final scoped conclusion

This final attempt reaches the exact formulation frontier.  A fully explicit legal support, a
formula-defined full-mixed coefficient law, and an independent exact high-tail reservoir are all
available.  Coupling them preserves every moment and normalization gate exactly.  The endpoint
would close if and only if the critical projection residual satisfies the fixed-margin inequality
(30.25).

No derivation presently controls that growing multisymmetric residual, and the available finite
values cross the threshold in both directions.  The correct verdict is Decision C: a true
asymptotic Gram-inversion/sign-geometry gap, not a missing scalar ladder and not a vague request
for more search.

No genuinely distinct escape route was generated in this bounded attempt, so none is named or
commissioned.  The controlling node remains open, and no `PROVED`, `CERTIFIED*`, or `REFUTED`
claim is made.
