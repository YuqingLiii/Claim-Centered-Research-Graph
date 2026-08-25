# k-Sum L2 phase-23 analysis — non-scalar critical residual structure

Date: 2026-07-21  
Controlling node:
`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.multiscale-gapfree-base-measure.critical-dense-palette-residual-window`  
Tier: proposer structural analysis plus finite numerical attribution; no independent review

## Decision

**C — the responsible non-scalar feature is identified, and the full projection has an exact
multisymmetric moment-operator representation, but no asymptotic diagonalization or typed
`D=L/2` approximant closes the window.**

At `N=27,D=4`, the entire full-orbit row space has the five-dimensional invariant basis

```text
1,
C   =sum_i x_i,
S2  =sum_i s_i^2,
S3  =sum_i s_i^3,
M1  =sum_i s_i x_i,       s_i=r_i+u_i, x_i=r_i u_i.         (23.1)
```

The mixed moment `M1`, not the pure total moments, causes the threshold crossing:

```text
span{1,C}        correlation 0.6792618832,
span{1,C,S2}                 0.6804826693,
span{1,C,S3}                 0.6804999411,
span{1,C,M1}                 0.5954005611,
full space                   0.5861085065.                  (23.2)
```

Thus the Phase-22 non-scalar effect is concretely the correlation between target-pair production
`x_i` and its pair total `s_i`.

At `N=33,D=5`, the scalar span already falls below threshold, but mixed moments continue the drop.
The exact eleven-dimensional basis adds

```text
S4=sum s_i^4, M2=sum s_i^2 x_i, X2=sum x_i^2,
S2^2, S2*C, C^2.                                            (23.3)
```

Here scalar `{1,C,C^2}` gives `0.5168254835`, adding `M1` gives `0.5079947622`, and the full basis
gives `0.4705055710`.  Relative to the degree-three subspace, `C^2` and then the mixed `M2` are the
largest single degree-four changes.  The normalized correlation is not monotone under enlarging a
projection space, so these are attribution gates, not an orthogonal variance decomposition.

## 1. Why (23.1)--(23.3) are the full orbit spaces

For one unordered split, the orientation-invariant polynomial ring is

```text
R[r,u]^(r<->u)=R[s,x],       s=r+u, x=ru,                   (23.4)
```

with weighted degrees

```text
wt(s)=1, wt(x)=2.                                            (23.5)
```

The orbit factor

```text
A_(alpha,beta)(r,u)
 =((r)_alpha(u)_beta+(r)_beta(u)_alpha)/2                  (23.6)
```

is a symmetric polynomial of weight `alpha+beta`.  Conversely, the falling-factorial change of
basis is triangular relative to the monomial symmetric functions
`r^alpha u^beta+r^beta u^alpha`; hence all one-slot polynomials in `s,x` of weight `<D` are in the
span of (23.6).

Symmetrizing over target slots gives the multisymmetric algebra.  Define polarized power sums

```text
p_(a,b)=sum_i s_i^a x_i^b,        wt p_(a,b)=a+2b.          (23.7)
```

Collision partitions of query blocks produce products of these power sums, and Möbius inversion
between unrestricted and injective slot assignments reverses the construction.  Therefore, in
the stable range `D<m` and `D<N`,

> the actual orbit-feature span `V_D` is exactly the restriction of the multisymmetric
> polynomials in the slot pairs `(s_i,x_i)` having weighted degree `<D`.

The identity `p_(1,0)=sum_i s_i=N` removes all factors of the first total power sum.

For `D=4`, the remaining monomials have basis exactly (23.1).  For `D=5`, the six new weight-four
monomials are exactly (23.3), giving eleven dimensions.  The independent raw injection-tensor
calculation has ranks `5` and `11`, and projection onto these invariant bases reproduces the raw
correlations to `3e-15`.  This is both a type check and a no-row-loss check.

## 2. Feature attribution details

The finite attribution uses the exact Phase-21 mixture, merges component overlap before
projection, and evaluates invariant families in `L_2(pi)`.

### `N=27,L=9,D=4`

| Feature family | rank | normalized correlation |
|---|---:|---:|
| `1,C` | 2 | 0.6792618832 |
| `1,C,S2` | 3 | 0.6804826693 |
| `1,C,S3` | 3 | 0.6804999411 |
| `1,C,M1` | 3 | 0.5954005611 |
| `1,C,S2,S3` | 4 | 0.6789056553 |
| `1,C,S2,M1` | 4 | 0.5873206357 |
| `1,C,S3,M1` | 4 | 0.5864556434 |
| full invariant basis | 5 | 0.5861085065 |
| raw orbit coefficients | 5 | 0.5861085065 |

The pure total profile by itself does essentially nothing at this size.  The single mixed power
sum `M1` accounts for almost the entire non-scalar change.

### `N=33,L=10,D=5`

| Feature family | normalized correlation |
|---|---:|
| scalar `1,C,C^2` | 0.5168254835 |
| scalar plus `M1` | 0.5079947622 |
| degree-`<4` basis `1,C,S2,S3,M1` | 0.5797486617 |
| degree-`<4` basis plus `M2` | 0.5533487897 |
| degree-`<4` basis plus `C^2` | 0.4957076593 |
| full invariant basis | 0.4705055710 |
| raw orbit coefficients | 0.4705055710 |

At this cutoff, the scalar quadratic is already strong; the mixed hierarchy `M1,M2,...` supplies
additional genuinely non-scalar leverage.  Pure `S_k` and `X2` additions are much weaker singly.

## 3. Exact projection operator for general cutoff

The invariant description gives a closed, typed operator even when no diagonal form is known.
Let `Lambda_D` index products

```text
P_lambda=product_j p_(a_j,b_j),
sum_j(a_j+2b_j)<D,                                         (23.8)
```

modulo `p_(1,0)=N` and the ordinary finite-slot relations.  In the stable range, these products
may be replaced by a standard multisymmetric monomial basis.  Define

```text
G_D(lambda,mu)=E_pi[P_lambda P_mu],
v_D(lambda)=E_pi[b P_lambda].                               (23.9)
```

Then

```text
c_D=G_D^dagger v_D,
g_D(H)=b(H)-sum_lambda c_D(lambda)P_lambda(H),               (23.10)
```

and the exact phase-16 gates are

```text
Corr_D=2 E_pi[g_D^2]/E_pi[|g_D|],
Tail_D(T)=E_pi[|g_D|1[C_t>=T]]/E_pi[|g_D|].                 (23.11)
```

The types are explicit:

```text
G_D : R^(Lambda_D) -> R^(Lambda_D),
v_D,c_D in R^(Lambda_D),
g_D in R^S.                                                 (23.12)
```

The Phase-21 overlap causes no correction in (23.9): expectation under the mixture is exactly the
half-sum of component expectations.  It does matter in (23.10)--(23.11), because an overlapping
histogram is one domain point with the summed positive mass, not two orthogonal component copies.

## 4. Closed collision-partition formulas for the Gram entries

The entries of (23.9) are formula-defined rather than LP-selected.  Conditional on a total vector
`s`, define the local split moments

```text
mu_b^(component)(s)=E[x^b | s],       b>=1.                 (23.13)
```

For the dense component,

```text
mu_b^dense(s)=(s-1)^b/2.                                   (23.14)
```

For a balanced bulk slot,

```text
mu_b^bal(s)
 =[1/(2 floor(s/2))] sum_(r=1)^(floor(s/2)) [r(s-r)]^b,     (23.15)
```

and for a unit slot `mu_b^unit=1/2`.  Products of power sums expand over set partitions of their
factor labels.  Each collision block assigned to one slot contributes

```text
s^(sum a_j) mu_(sum b_j)(s),                               (23.16)
```

and distinct blocks are injected into distinct slots.  Averaging the resulting finite sums over
the exact total-composition laws gives every entry of `G_D` and `v_D`.

On NO profiles all `x_i=0`.  Hence `v_D(lambda)=0` whenever `P_lambda` contains any mixed factor
with `b_j>0`; only pure-total columns have a direct NO moment.  Mixed columns such as `M1` still
change the projection through their Gram coupling to the constant and pure columns.  This explains
why `M1` can be load-bearing even though it vanishes identically on the NO boundary.

## 5. Why this does not yet close `D=L/2`

Equations (23.8)--(23.16) are an exact representation, but they expose three genuine obstacles to
an asymptotic theorem.

1. **Growing collision-partition rank.**  At `D=L/2`, `Lambda_D` contains colored partitions of
   all weights below a linear cutoff.  Its dimension grows superpolynomially in any fixed moment
   truncation.  The five- and eleven-dimensional closures at `D=4,5` do not persist.

2. **No common orthogonal basis for the mixture.**  The balanced component has deterministic unit
   slots plus narrowly distributed bulk totals and broad split laws.  The dense component has a
   capped exact-composition total law and a two-point split law.  Their conditional moment
   operators (23.14)--(23.15) are not simultaneously diagonal.  The mixture Gram matrix is a sum
   of two differently diagonalizable operators; overlap forbids replacing it with an orthogonal
   direct sum.

3. **The target gates are not spectral-only.**  Even asymptotics for `G_D^dagger v_D` would first
   control `E[g_D^2]`.  Correlation and high-tail mass require the pointwise sign/absolute-value
   quantities `E|g_D|` and `E[|g_D|1_tail]`.  These are not determined by eigenvalues or finitely
   many limiting moments.  The finite `M1` effect is precisely a warning that low-dimensional
   scalar closures miss the sign geometry.

A tempting componentwise construction—use the Phase-20 approximant on `pi_bal` and a scalar
approximant on `pi_dense`—is not typed as a single element of `V_D` unless one also supplies a
low-degree polynomial selector for the two overlapping supports.  No such selector was obtained;
treating the mixture as disjoint would repeat the exact overlap error ruled out in Phase 22.

## 6. Gate ledger

| Gate | Result |
|---|---|
| concrete `N=27` non-scalar culprit | **PASS**: `M1=sum s_i x_i` |
| concrete `N=33` non-scalar hierarchy | **PASS**: principally `M1,M2` beyond scalar powers |
| raw-orbit versus invariant-span equality | **PASS NUMERICALLY**, ranks and projections agree |
| typed general multisymmetric projection operator | **PASS** by (23.8)--(23.12) |
| closed component moment formulas | **PASS** by (23.13)--(23.16) |
| asymptotic diagonalization at `D=L/2` | **OPEN** |
| typed non-scalar approximant below cutoff | **OPEN** |
| analytic correlation or tail verdict | **OPEN** |

## 7. Provenance

Attribution driver:
[ksum/tools/ksum_l2p23_feature_attribution.py](../tools/ksum_l2p23_feature_attribution.py)

Archived output:
[run.json](logs_ksum_L2p23_feature_attribution_20260721/run.json)

Command:

```text
python ksum/tools/ksum_l2p23_feature_attribution.py --Ns 27 33
```

Driver SHA-256:

```text
e4df57cbbc7bd56e2132ffcaf9e24c7287dbf8e017f5da0da44e213f0402174c
```

The driver uses the exact Phase-22 mixture enumerator and full raw orbit generator, then compares
them with independently evaluated invariant bases.  It passed `py_compile`, JSON validation, and
the scoped diff check.

## 8. Scoped conclusion

The finite mystery is resolved: `M1=sum_i s_i r_i u_i` is the feature that first defeats the
scalar-only picture, and its higher mixed-moment relatives persist at the next cutoff.  The full
orbit span is exactly a weighted multisymmetric polynomial space, so the asymptotic problem can be
stated as the explicit growing Gram projection (23.9)--(23.11), with component moments given by
collision partitions.

What remains is not a missing feature formula.  It is the inversion and sign control of a growing,
non-simultaneously-diagonalizable mixture moment operator at weight `D=L/2`.  No valid asymptotic
correlation or residual-tail conclusion follows from the present finite ranks.  The node therefore
remains Decision C / OPEN.

No distinct escape route was tested or commissioned.  No `PROVED`, `CERTIFIED*`, `NUMERICAL`, or
`REFUTED` DAG status is claimed.
