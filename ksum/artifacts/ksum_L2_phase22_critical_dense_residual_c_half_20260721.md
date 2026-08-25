# k-Sum L2 phase-22 numerical analysis — critical dense residual at `c=1/2`

Date: 2026-07-21  
Controlling node:
`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.multiscale-gapfree-base-measure.critical-dense-palette-residual-window`  
Tier: proposer numerical discriminator; no independent review and no DAG status claim

## Decision

**C / NUMERICAL — the full actual orbit projection crosses below `2/3` in the two largest exact
finite mixture instances, but the available sizes do not justify an asymptotic verdict.**

At `D=floor(L/2)` for the exact phase-21 mixture, the normalized projection-residual correlations
are

```text
N=15, L= 6, D=3:  0.6948730742
N=21, L= 7, D=3:  0.8042336153
N=27, L= 9, D=4:  0.5861085065
N=33, L=10, D=5:  0.4705055710.                           (22.1)
```

The `N=27,33` values are below `2/3` by visible margins.  At `N=27`, the projection onto only the
available scalar `C_t` powers still has correlation `0.6792618832>2/3`, whereas the full orbit
projection has `0.5861085065`.  Thus the finite rejection at that size genuinely uses non-scalar
orbit rows; it is not a replay of the phase-21 scalar Chebyshev calculation.

The sequence is nonmonotone, the cutoff jumps discretely, and `N=15,21` have only one bulk slot in
the balanced component.  No typed analytic approximant, asymptotic residual lower bound, or
asymptotic high-tail theorem was obtained.  The correct conclusion is therefore an informative
finite falsifier at two sizes and a sharpened warning about non-scalar rows, not Decision B for
the asymptotic family.

## 1. Exact finite law and overlap handling

For each odd `N`, the driver instantiates the phase-21 definitions verbatim:

```text
L=floor(N^(2/3)),
D=floor(L/2),
pi=(pi_bal+pi_dense)/2.                                     (22.2)
```

The balanced component uses

```text
U=ceil(2N^(1/3)), M=L-U,
U unit total-2 slots,
M bulk totals in {a-2,...,a+2} with exact occupancy N,
inactive probability 1/2 and all positive unordered splits sharing probability 1/2.  (22.3)
```

The dense component uses all exact compositions

```text
2<=s_i<=L+1, sum_i s_i=N,                                  (22.4)
```

and independently chooses `(0,s_i)` or `(1,s_i-1)` with probability `1/2` each.

Both components are first pushed to unordered split histograms with their exact multinomial
weights.  The domain is then the *union* `S=S_bal union S_dense`, and overlap is combined before
projection:

```text
pi(H)=(pi_bal(H)+pi_dense(H))/2.                            (22.5)
```

No histogram in the intersection is duplicated as a separate coordinate.  The finite overlap
ledger is:

| `N` | `|S_dense|` | `|S_bal|` | `|S|` | overlap count | dense mass on overlap | balanced mass on overlap |
|---:|---:|---:|---:|---:|---:|---:|
| 15 | 48 | 18 | 54 | 12 | 0.1071428571 | 0.7500000000 |
| 21 | 412 | 35 | 447 | 0 | 0 | 0 |
| 27 | 1494 | 798 | 2068 | 224 | 0.0656763096 | 0.4279057018 |
| 33 | 7748 | 1520 | 9044 | 224 | 0.0043616978 | 0.3132716049 |

The zero overlap at `N=21` is real: its single balanced bulk total is `9`, while the dense cap is
`L+1=8`.  Each component mass independently sums to `1.0` in every run, before applying (22.5).

## 2. Full actual orbit-feature space

For every nonzero complementary source-pair pattern

```text
kappa=(alpha,beta),
0<=alpha<=beta,
1<=alpha+beta<D,                                            (22.6)
```

the one-slot factor is

```text
A_kappa(r,u)=((r)_alpha(u)_beta+(r)_beta(u)_alpha)/2.        (22.7)
```

For a histogram `H`, the driver expands the entire truncated slot product

```text
P_H(z)=product_slots (1+sum_kappa z_kappa A_kappa(r,u))     (22.8)
```

and retains every coefficient whose weighted degree is `<D`.  If `p` is the number of retained
coefficient keys, define the evaluation map

```text
E_D : R^p -> R^S,
(E_D c)(H)=sum_key c_key [z_key]P_H(z).                     (22.9)
```

The weighted projection is the ordinary least-squares projection of the NO indicator `b` onto
`range(E_D)` in `L_2(pi)`.  Equivalently, the phase-16 feature matrix is `A=E_D^T`.

This construction does not lose full-orbit rows:

- the coefficients in (22.8) are precisely all injection tensors of weighted query degree `<D`;
- restricting to `alpha<=beta` removes only the duplicate orientation of the symmetric factor
  (22.7);
- rows involving the fixed value symbol are identically zero and are omitted;
- the phase-12 denominators `((m)_rho(N)_d)^(-1)` are nonzero and depend only on the row, so using
  raw coefficients changes row scaling but not the row span;
- dependent coefficient columns are retained for construction and removed only by the weighted
  numerical rank calculation.

Thus the finite calculation projects onto the full actual orbit span in the stated odd-`q=N`
model, not onto arbitrary cylinders and not onto a scalar summary.

## 3. Typed projection and residual quantities

Let `n=|S|`.  Numerically,

```text
E_D in R^(n x p),
diag(sqrt(pi))E_D in R^(n x p),
b,g,W_pi in R^n.                                            (22.10)
```

After column scaling, the driver solves

```text
c_*=argmin_c ||diag(sqrt(pi))(b-E_D c)||_2,
g=b-E_D c_*,
W_pi(H)=pi(H)g(H)/||g||_(1,pi).                             (22.11)
```

It reports the exact phase-16 scalar

```text
corr=2||g||_(2,pi)^2/||g||_(1,pi),                          (22.12)
```

and residual absolute tail mass

```text
Tail=sum_(C_t>=T_bal/2) pi(H)|g(H)|/||g||_(1,pi),           (22.13)
```

where `T_bal` is the exact maximum balanced-component `C_t` at that finite `N`.

The matrix dimensions and numerical ranks are:

| `N` | `n` | raw columns `p` | weighted rank | nullity `n-rank` | smallest retained singular value |
|---:|---:|---:|---:|---:|---:|
| 15 | 54 | 5 | 3 | 51 | 0.0646725009 |
| 21 | 447 | 5 | 3 | 444 | 0.1649441740 |
| 27 | 2068 | 10 | 5 | 2063 | 0.0148993548 |
| 33 | 9044 | 21 | 11 | 9033 | 0.0038669655 |

The solve uses double-precision SVD with relative cutoff `1e-11`.  The displayed threshold margins
at `N=27,33` are much larger than this numerical cutoff, but this is not a rational or interval
certificate.

## 4. Full-orbit versus scalar `C_t` projection

As a control, the driver separately projects onto

```text
span{1,C_t,...,C_t^r},       r=floor((D-1)/2),              (22.14)
```

the scalar subspace known to fit within query degree `<D`.  Results are:

| `N` | `D` | full-orbit corr | scalar max power | scalar corr | full minus scalar |
|---:|---:|---:|---:|---:|---:|
| 15 | 3 | 0.6948730742 | 1 | 0.6952152930 | -0.0003422188 |
| 21 | 3 | 0.8042336153 | 1 | 0.7864114845 | +0.0178221308 |
| 27 | 4 | 0.5861085065 | 1 | 0.6792618832 | -0.0931533767 |
| 33 | 5 | 0.4705055710 | 2 | 0.5168254835 | -0.0463199126 |

The normalized residual correlation is a ratio, so enlarging the projection space need not change
it monotonically; `N=21` illustrates this.  The important discriminator is `N=27`: scalar rows
alone remain above `2/3`, while the full actual row span moves below it.  Any asymptotic analysis
of the `c=1/2` window must therefore control non-scalar multisymmetric rows and cannot stop at the
phase-21 `C_t` constant calculation.

## 5. Residual tail and gate table

| `N` | full corr | `T_bal` | residual mass at `C_t>=T_bal/2` |
|---:|---:|---:|---:|
| 15 | 0.6948730742 | 11 | 0.1558995763 |
| 21 | 0.8042336153 | 26 | 0.0981188749 |
| 27 | 0.5861085065 | 26 | 0.1866694613 |
| 33 | 0.4705055710 | 39 | 0.1300077331 |

The finite residual does retain visible high-tail absolute mass in every instance, between about
`0.098` and `0.187`.  There is no monotone trend and `T_bal/2` at these small sizes is only a scaled
proxy for the asymptotic `Theta(N^(4/3))` threshold.  These values therefore do not prove a
constant asymptotic tail.

The requested alternatives resolve as follows:

| Gate | Result |
|---|---|
| typed analytic non-scalar approximant below `D=L/2` | **OPEN** |
| analytic correlation `>2/3` | **OPEN** and contradicted at `N=27,33` finitely |
| analytic residual high-tail bound | **OPEN** |
| exact finite mixture construction including overlap | **PASS** |
| full actual orbit-feature projection, no scalar reduction | **PASS NUMERICALLY** |
| finite corr `>2/3` | PASS at `N=15,21`; FAIL at `N=27,33` |
| finite visible residual tail | PASS numerically, without asymptotic inference |

## 6. Provenance and reproducibility

Driver:
[ksum/tools/ksum_l2p22_critical_dense_residual.py](../tools/ksum_l2p22_critical_dense_residual.py)

Raw archived output:
[run.json](logs_ksum_L2p22_critical_dense_20260721/run.json)

Command:

```text
python ksum/tools/ksum_l2p22_critical_dense_residual.py --Ns 15 21 27 33
```

Driver SHA-256:

```text
d11627702e81aff7f2f19142099adf3d88342281c0a4b50db4c19ef8a9be7e91
```

The driver passed `python -m py_compile`; the scoped diff check for the driver, log, and memo passed.

## 7. Scoped conclusion

At `c=1/2`, the phase-21 critical mixture is not supported by a stable finite trend toward
correlation above `2/3`.  The two largest feasible full-orbit instances fall below threshold, and
one of them (`N=27`) does so only after genuinely non-scalar rows are included.  This materially
narrows the open constant window: a proof attempt must understand the full multisymmetric
projection, not just sharpen the scalar Chebyshev constant.

The data still do not identify a formula-defined non-scalar approximant or an asymptotic limit.
The cutoff and balanced bulk dimension change discontinuously across these small instances, so
extrapolation would be unsound.  The node should remain open with Decision C / NUMERICAL evidence.

No distinct escape route was tested or commissioned.  No `PROVED`, `CERTIFIED*`, or `REFUTED`
status is claimed.
