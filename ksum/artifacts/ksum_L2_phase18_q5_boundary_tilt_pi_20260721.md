# k-Sum L2 phase-18 proposer analysis — q=5 boundary and Christoffel tilts

Date: 2026-07-21  
Controlling node:
`KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel`  
Tier: proposer analysis and float64 diagnostics; no independent review and no DAG status claim

## Decision

**B — none of the tested formula-defined repairs simultaneously fixes sign purity and preserves a
quarter of the residual mass at high `C_t` once the sampled cutoff grows.**

The tested laws all remain inside the phase-16 weighted-projection normal form and are strictly
positive on every legal q=5 orbit.  They include

1. symmetric Dirichlet--multinomial laws with
   `alpha(N)=N^-1,N^-1/2,1,N^1/2,N`;
2. exact or square-root reweighting of the `C_t=0` boundary;
3. distance-to-boundary weights `(1+C_t)^(-beta)`;
4. one-step up- and down-tilts by the explicit Christoffel kernel
   `K_D^{pi_1}(H,H)`.

At `D=ceil(sqrt(N))`, `N=8,12,16,20,24,32,40,50,64`, no named schedule passes both gates
uniformly across the sample.  The sole named-schedule simultaneous pass is the small
`alpha=N^-1/2,N=8,D=3` case; it already fails at `N=12,D=4`.  The gates are

```text
correlation > 2/3,
Tail_pi(N^(3/2)/4) >= 1/4.                                      (18.1)
```

There are isolated small passes for members of the wider parameter grid (`N=8` and `N=16`), but
none at `N=12,20,24,32,40,50,64`.  At `N=64`, the best grid correlation subject to the tail gate is
only `0.5553`.  This is a **sharp finite numerical falsification of the displayed schedules and
grid**, not an asymptotic theorem for every possible `alpha(N,D)` or tilt.  The controlling node
therefore remains OPEN.

The observed mechanism is a clean tradeoff.  Moving mass toward `C_t=0` can raise correlation at
small cutoffs, but reduces the high-`C_t` residual mass.  Moving toward the balanced interior makes
the tail excellent and the correlation collapse.  The Christoffel tilts move along the same
tradeoff rather than escaping it.

## 1. Common legal law and varying Dirichlet parameter

Use the phase-17 legal count space

```text
Lambda_N={n in Z_+^4: sum n_j=N,
          n_1+n_2>=1, n_3+n_4>=1}
```

and quotient by `G=S_2 wr S_2`.  For every `alpha>0`, define

```text
pi_{N,alpha}(G n)
 proportional to
 sum_{n' in G n} product_{j=1}^4 Gamma(n'_j+alpha)/n'_j!.        (18.2)
```

This is the symmetric Dirichlet--multinomial orbit pushforward conditioned only on the legal
`K=2` support.  It is positive everywhere and is independent of any LP or signed witness.

The two pointwise parameter limits explain the numerical directions.  With `N` fixed:

- as `alpha->0`, a count vector with `k` positive coordinates has relative leading order
  `alpha^{-(4-k)}`; legality forces `k>=2`, and the `k=2` leading stratum is exactly NO.  Thus
  `pi_{N,alpha}(NO)->1`;
- as `alpha->infinity`, (18.2) tends the uniform four-category multinomial law conditioned on
  legality, hence concentrates toward the balanced interior as `N` grows.

These fixed-`N` limits do not prove the joint regimes `alpha=N^-1` or `alpha=N`; they only identify
why the two schedules pull toward opposite ends of (18.1).

The five explicit target-scale schedules were

```text
alpha=N^-1, N^-1/2, 1, N^1/2, N.                                (18.3)
```

At `N=64,D=8` their `(correlation, tail)` values are respectively

```text
(0.5691,0.2309), (0.5553,0.2522), (0.3306,0.5478),
(0.0147,0.9913), (0.0013,0.9993).                               (18.4)
```

The first schedule misses the tail gate; the other four miss correlation.  In particular, merely
letting the symmetric Dirichlet parameter tend to zero or infinity did not repair the phase-17
sign-purity failure.

## 2. Explicit boundary tilts

Let `pi_1` be the uniform-composition orbit law and

```text
delta_N=pi_1(NO)=24/((N+1)(N+6)),
b(H)=1[C_t(H)=0].                                                (18.5)
```

Two label-boundary tilts are

```text
pi_N^(rho)(H)
 proportional to pi_1(H) lambda_N^{rho b(H)},
lambda_N=(1-delta_N)/delta_N,
rho in {1/2,1}.                                                  (18.6)
```

At `rho=1`, the new base law puts exactly half its probability on NO.  Formula (18.6) is explicit;
it uses only the known orbit label and closed form (18.5), not an optimizer.  Nevertheless at
`N=64,D=8` its two residual correlations are `0.3304` and `0.3302`, essentially the un-tilted
`0.3306`, with tail masses `0.5484` and `0.5488`.  Balancing the base labels does not balance the
projected residual signs.

A label-free distance tilt is

```text
pi_{N,beta}^{Ct}(H)
 proportional to pi_1(H)(1+C_t(H))^{-beta},
beta in {1/2,1}.                                                 (18.7)
```

At `N=64,D=8`, `beta=1/2` gives `(0.4425,0.3989)` and `beta=1` gives
`(0.5617,0.2439)`.  The stronger tilt raises correlation but crosses below the tail gate before
reaching `2/3`.

## 3. Explicit Christoffel/leverage tilts

Let `Phi_D(H)` be any row basis of the actual orbit-feature space and set

```text
G_D=sum_H pi_1(H) Phi_D(H)Phi_D(H)^T,
K_D(H,H)=Phi_D(H)^T G_D^dagger Phi_D(H),
R=rank(G_D).                                                     (18.8)
```

Both objects are finite sums of the formula-defined phase-16 features.  No linear program, label
optimization, or `|W_*|` appears.  The one-step laws tested were

```text
pi_N^up(H)   proportional to pi_1(H)(1+K_D(H,H)/R),
pi_N^down(H) proportional to pi_1(H)/(1+K_D(H,H)/R).             (18.9)
```

They remain strictly positive on the whole legal orbit space.  At `N=64,D=8`, the up-tilt gives
`(correlation,tail)=(0.4322,0.4307)` and the down-tilt gives `(0.2550,0.6428)`.  Upweighting leverage
improves sign purity somewhat at the expense of tail; downweighting leverage does the reverse.
Neither comes close to both gates.

## 4. Combined DM-times-boundary grid

To check whether the named schedules merely skipped a narrow window, the same computation tested

```text
pi_{alpha,beta}(H)
 proportional to pi_{N,alpha}(H)(1+C_t(H))^{-beta},              (18.10)

alpha in {N^-1,N^-1/2,0.1,0.25,0.5,1,2},
beta  in {0,0.25,0.5,0.75,1,1.25,1.5}.                          (18.11)
```

Coincident alpha values were removed, so each `N` has at most 49 distinct grid points.  The best
correlation among points satisfying the tail-quarter gate was:

| `N` | `D` | best correlation | alpha | beta | tail | number passing both gates |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 3 | 0.6684 | `N^-1/2` | 0 | 0.2736 | 1 |
| 12 | 4 | 0.6176 | 1 | 0 | 0.2605 | 0 |
| 16 | 4 | 0.6814 | 0.5 | 0 | 0.2536 | 2 |
| 20 | 5 | 0.5299 | `N^-1/2` | 0 | 0.2582 | 0 |
| 24 | 5 | 0.5643 | 0.25 | 0 | 0.2580 | 0 |
| 32 | 6 | 0.5834 | `N^-1/2` | 0 | 0.2574 | 0 |
| 40 | 7 | 0.4956 | 0.1 | 0 | 0.2703 | 0 |
| 50 | 8 | 0.5226 | 0.5 | 0.5 | 0.2528 | 0 |
| 64 | 8 | 0.5553 | `N^-1/2` | 0 | 0.2522 | 0 |

The two passes occur only at repeated low integer cutoffs `D=3,4`; none survives the next cutoff
jumps.  This reproduces the sawtooth already seen in phases 14--17 and supplies no stable
formula-defined witness.

The grid optimum is used only as a diagnostic upper envelope of the tested finite set.  Choosing
its maximizing parameters from the output would not be a preregistered formula and is not proposed
as a witness.

## 5. Numerical provenance and checks

The driver constructs all actual q=5 orbit rows of weighted degree `<D`, forms every stated weight
directly, and recomputes the phase-16 weighted projection separately for each law.  It does not call
an LP solver.  Numerical ranks at `D=3,4,5,6,7,8` are respectively `3,4,8,10,16,20`, matching the
archived feature-rank pattern.  Across all named variants the largest weighted-orthogonality
residual is `7.7e-15`.

- Driver: `ksum/tools/ksum_l2p18_q5_boundary_tilts.py`, SHA-256
  `1d2d09a7714cee02bfcfeb2daa6829e59a3c15d27b0358894392029dbbd0f3`.
- JSON: `ksum/artifacts/logs_ksum_L2p18_q5_boundary_tilts_20260721.json`, SHA-256
  `6eb6c98d736176869c6d74342ad677a0fa468daf536abe0f971a4ec78c7f2192`.
- Arithmetic: float64 SVD; the JSON is numerical evidence only.
- Tail threshold: `C_t>=N^(3/2)/4`, which is `omega(N)` and `o(N^2)`.
- Support: every law is positive on every legal `K=2` orbit; no illegal empty-pair orbit is used.

## 6. Exact scope and remaining question

### Analytic facts established here

- Equations (18.2), (18.6)--(18.10) define strictly positive legal laws without LP output or
  `|W_*|`.
- For fixed `N`, the limits `alpha->0` and `alpha->infinity` move the base measure respectively
  toward the NO two-coordinate stratum and the conditioned multinomial interior.

### Numerical facts established here

- None of the five schedules (18.3), two boundary balances, two fixed `C_t` tilts, or two
  Christoffel tilts passes both gates uniformly across the sample.  The only named-schedule
  simultaneous pass is `alpha=N^-1/2,N=8,D=3`.
- The finite combined grid has no simultaneous pass for any sampled `N>=20`.

### Not established

- There is no analytic no-go for every joint schedule `alpha(N,D)` or `beta(N,D)` at
  `D=c sqrt(N)`.
- The finite grid does not exclude a parameter window between its points.
- A quarter tail mass is a strong concrete gate; failure of that gate alone does not prove that
  every weaker interpretation of “non-negligible” fails.
- No monotonicity across integer cutoffs is asserted.
- The selective-orbit-tensor node remains OPEN and needs independent Rule-7 review before any
  completion-tier status.

The evidence says that a useful next base law must change more than a one-parameter symmetric
radial weighting: it must control the joint signs of several orbit coordinates while keeping mass
in both low- and high-`C_t` YES regions.  That observation may suggest a genuinely distinct route,
but Rule 8 requires such a route to be registered before it is formulated or tested; none was
invented or tested in this pass.
