# KSUM.B4b.L2 phase 3 — correlated outer kernel

Date: 2026-07-19  
Route status: **CONJECTURED · phase-3 mathematics pending-review**  
Preregistered outcome: **PROGRESS**  
Scope: D7-repaired odd-`q` route only; no even-`q` claim and no exponent inference (G11).

## Pre-action reload

Before phase-3 candidate work, the executor reloaded the research-structure and proof-DAG protocols
(including rule 6), the KSUM node index, the complete `KSUM.B4b.L2` work record and canonical
odd-`q` obligation, its status-propagating ancestors, the completed phase-1, corrected-repair, and
phase-2 L2 reviews, and the reviewed U1 cap artifact. The complete phase-2 report and both scripts,
the substantive phase-2 run files, manifests, and transcript provenance events were also inspected.
No network or git commit was used. The worktree was already heavily dirty; pre-existing changes were
preserved.

The phase-3 prediction file was written before either phase-3 script. It froze PROGRESS/PARTIAL/
BLOCKED, the mechanism order, the finite gate, and M2 condition 5 as the intended escape:
[predictions](logs_ksum_L2p3_20260719/predictions.txt).

## Outcome

The first mechanism, a global-statistic tilted product, survives its exact finite gate and has a
complete proposer proof for a general band growing with `q`. Consequently the commissioned stop
rule fires before the few-pair and BKT-style mechanisms.

For odd `q`, put `r=(q-1)/2` and

```text
m = 1 + floor(log_5 r).
```

The construction has unit `l1`, is `S_N x C(sigma)` invariant, annihilates every query polynomial
of degree below `2m`, and has correlation strictly greater than `3/4`. Thus it exceeds
`2/3+delta` with the fixed choice `delta=1/12`. The band

```text
2(1 + floor(log_5((q-1)/2)))
```

grows with `q`, so this is **PROGRESS under the frozen phase-3 definition**. It is far below the
canonical cap-scale target and proves no exponent consequence. Under DAG rule 6, all new general
mathematics remains **CONJECTURED · pending-review**; the exact runs are NUMERICAL evidence.

## 1. Construction

Fix odd `q`, `N>=q`, and target `t`. Let `sigma(a)=t-a`, let `f` be its unique fixed point, and let
`(a_c,b_c)`, `1<=c<=r`, be the complementary pairs. Put exactly one item at `f`. As in reviewed M1,
choose a permutation-invariant mixture of balanced exact pair-total vectors

```text
s=(s_1,...,s_r),   s_c>=2,   sum s_c=N-1.
```

On the slice `i+j=s`, let `A_s` be the symmetric axis probability and `I_s` the symmetric central
interior probability from phase 2. They have the same total mass and the same two coordinate means.

For an active-pair indicator `z in {0,1}^r`, use `I_(s_c)` when `z_c=1` and `A_(s_c)` when `z_c=0`.
Write `K=|z|`. Define

```text
T_m = {0,1,5,...,5^(m-1)},
lambda_k = 1 / product_(u in T_m, u!=k) (k-u)       (k in T_m).
```

Multiply all `lambda_k` by one common sign so `lambda_0<0`, normalize by
`Z=sum_(k in T_m)|lambda_k|`, and put aggregate signed mass `W_k=lambda_k/Z` on layer `K=k`,
uniformly over its `binom(r,k)` indicator strings. Layers outside `T_m` have weight zero. Average
the resulting product probabilities over the balanced size-vector orbit, then lift each occupancy
weight uniformly to its `S_N` string orbit.

This is a tilt of the reviewed M1 product by one global statistic. Indeed, the M1 point coefficient
on `z` is proportional to `(-1)^(r-K)`. If

```text
Q(K) = product_(ell in {0,...,r} minus T_m) (K-ell),
```

then `deg Q=r-m` and the identity

```text
Q(k) = (-1)^(r-k) r! lambda_k / binom(r,k)
```

shows that multiplying the M1 product by `Q(K)` gives exactly the outer layer weights above, up to
one global normalization. The general degradation is explicit: a degree-`d` tilt of the parity
outer functional retains outer moment order at least `r-d`; here `d=r-m`, so the M1 query band
`2r=q-1` becomes `2m`. The loss is quantified exactly; the retained band is logarithmic rather than
cap-scale.

## 2. M2 forbidden-class gate

The reviewed M2 class has five conditions:

1. fixed-point occupancy at most one, so global NO is the all-axis event;
2. every product component has one nonzero local signed factor on every two-cycle;
3. after local orientation, each factor is axis-nonpositive, interior-nonnegative, and has zero
   total mass;
4. arbitrary local shapes, pair totals, and nonzero scales are permitted; and
5. only sign-aligned positive mixtures of those products are added.

The phase-3 construction is **not** in this class because it violates the preregistered condition
**5**. Its outer divided-difference coefficients alternate in sign and correlate all pairs through
`K`; layers not in `T_m` are cancelled to zero. A sign-aligned positive mixture of M2 products has
the common nonzero product sign pattern and cannot perform those cross-layer signed cancellations.
Conditions 1 and 4 remain compatible with the construction, while the M1 factors under the tilt
supply the local axis/interior primitives. The violation of condition 5 alone is enough for gate (i).

## 3. General odd-q lemma (proposer proof; pending review)

### Lemma L2P3

For every odd `q>=3`, every `N>=q`, and every target `t`, the construction above is
`S_N x C(sigma)` invariant, has `l1=1`, has correlation greater than `3/4`, and annihilates every
query polynomial of degree below

```text
2(1 + floor(log_5((q-1)/2))).
```

### Outer cancellation

The divided-difference identity gives

```text
sum_(k in T_m) lambda_k p(k) = 0
```

for every univariate polynomial `p` of degree below `m`. Under the uniform measure on the layer
`K=k`, an indicator monomial on `j` named pairs has expectation `(k)_j/(r)_j`. Hence the signed
outer measure annihilates every multilinear function of `z` of degree below `m`.

Consider an occupancy falling-factorial monomial. On pair `c`, if its local order is zero or one,
its expectations under `A_(s_c)` and `I_(s_c)` agree because those probabilities have equal mass
and coordinate means. Only pairs of local order at least two can make the conditional expectation
depend on `z_c`. If the total occupancy degree is below `2m`, fewer than `m` pairs have local order
at least two. The product conditional expectation is therefore a multilinear function of fewer
than `m` outer indicators and is annihilated. This holds on each exact pair-total vector before
mixing. The reviewed falling-factorial/query-degree map then lifts the result, without degree loss,
to every query polynomial below degree `2m`.

### Norm and invariance

Axis and interior supports are disjoint on each pair. Distinct indicator patterns are therefore
disjoint, and distinct labeled size vectors are disjoint because their pair totals recover the
vector. Each conditional product has probability mass one, so the lifted measure has

```text
||mu||_1 = sum_k |W_k| = 1.
```

Endpoint-swap symmetry of `A_s,I_s`, exchangeability of `W` over pair indicators, invariance of the
balanced size-vector law under pair permutations, and uniform `S_N` lifting prove
`S_N x C(sigma)` invariance.

### Uniform correlation bound

The total signed mass is zero by the outer constant-moment identity. Because the fixed point has
occupancy one, the only NO layer in the support is `K=0`, whose weight is negative. Therefore

```text
<mu,F> = -2 W_0 = 2 |lambda_0| / sum_k |lambda_k|.
```

For `k=5^j`, put

```text
R_j = |lambda_(5^j)|/|lambda_0|
    = A_j C_(m-1-j),
A_j = product_(d=1)^j (5^d-1)^(-1),
C_h = product_(d=1)^h (1-5^(-d))^(-1).
```

The elementary product inequality `product(1-x_i)>=1-sum x_i` gives

```text
C_h <= (5/4) / (1-sum_(d>=2)5^(-d)) = 25/19.
```

Also `A_0=1`, `A_1=1/4`, and every multiplier after the first is at most `1/24`, so

```text
sum_(j>=0) A_j <= 1 + 1/4 + 1/92 = 29/23.
```

Consequently

```text
sum_j R_j <= (25/19)(29/23) = 725/437,
<mu,F> >= 2/(1+725/437) = 437/581 > 3/4 = 2/3+1/12.
```

This proves the claimed fixed positive margin at the proposer level.

## 4. Exact finite gate

Both scripts use `fractions.Fraction`. The constructor checked every target; the second script
independently parsed every output weight, rebuilt all factorial moments, recomputed norm and
correlation, and checked the full alphabet centralizer.

| `(N,q)` | targets | band | rows per target | `l1` | correlation | centralizer | result |
|---|---:|---:|---:|---:|---:|---:|---|
| `(5,5)` | all 5 | degree `<2` | 6 | `1` | `1` | order 8 | PASS |
| `(7,3)` | all 3 | degree `<2` | 4 | `1` | `1` | order 2 | PASS |

Every rational residual is exactly zero. Correlation is strictly greater than `2/3` at both
commissioned points. Gate (ii) passes, so the general lemma in section 3 was attempted.

| purpose | command | raw log | script SHA-256 |
|---|---|---|---|
| construct/check | `python ksum/tools/ksum_l2p3_tilted_outer.py --output ksum/artifacts/logs_ksum_L2p3_20260719/tilted_outer_results.json` | [log](logs_ksum_L2p3_20260719/tilted_outer.log) | `ad5840bfd01e07f0e8abf294cdb850089bc3763ad2ad051fcab7432e27626490` |
| independent reconstruction | `python ksum/tools/ksum_l2p3_exact_verify.py --input ksum/artifacts/logs_ksum_L2p3_20260719/tilted_outer_results.json` | [log](logs_ksum_L2p3_20260719/exact_verify.log) | `635941cb8ec0054bdf40cde17d60a3b05cc7090614d52c6b7c19d614651a779b` |

Full commands and hashes: [COMMANDS](logs_ksum_L2p3_20260719/COMMANDS.txt),
[SHA-256 manifest](logs_ksum_L2p3_20260719/SHA256SUMS.txt), and
[machine-readable witnesses](logs_ksum_L2p3_20260719/tilted_outer_results.json).

## 5. Outcome, G11, and remaining gap

The outcome is **PROGRESS**, exactly as preregistered: an explicit correlated construction has a
general odd-`q` proposer proof of a growing annihilation band and a uniform correlation margin, and
both finite gates pass exactly. This is not completion of L2. The logarithmic band is much smaller
than `c0 min{sqrt(N)q^eta,N^(2/3)}` for every fixed `eta>1/6`; it therefore cannot imply the desired
query lower-bound exponent. G11 remains binding: the `(5,5)` and `(7,3)` runs verify machinery and
the stated finite claims only.

The next mathematical obligation is to replace the geometric divided-difference outer functional
by a cap-scale outer dual, or compose a stronger inner kernel, while retaining a fixed `>2/3`
correlation margin. The canonical odd-`q` cap-swept obligation is unchanged.

## What was not checked

- No fresh independent rule-6 review was performed; Lemma L2P3 remains CONJECTURED/pending-review.
- No cap-scale, `eta>1/6`, plateau, or exponent statement was proved.
- No even-`q` target or cycle type was considered.
- The few-pair and BKT-style candidates were not attempted because the commissioned stop rule fired
  at the first mechanism. Accordingly no BKT composition theorem was imported or re-audited.
- No raw string-level one-hot enumeration was rerun; the exact factorial gate uses the independently
  reviewed query-degree map, and the verifier checked all factorial rows in the claimed finite band.
- No optimizer extraction, held-out discriminator, or additional finite point was run.
- No network or git commit was used.
