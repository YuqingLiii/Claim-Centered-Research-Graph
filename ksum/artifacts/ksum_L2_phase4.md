# KSUM.B4b.L2 phase 4 — band-amplification obstruction

Date: 2026-07-19  
Route status: **CONJECTURED · phase-4 mathematics pending-review**  
Preregistered outcome: **BLOCKED**  
Scope: D7-repaired odd-`q` route, strict correlation `>2/3`; no even-`q` or exponent claim.

## Pre-action report and reload

This was a fresh execution with no wanted answer. Before preregistration or construction, the
executor reloaded the research-structure and proof-DAG protocols (including rule 6), the KSUM node
index, the complete `KSUM.B4b.L2` record and D7-repaired canonical obligation, parent `KSUM.B4b`,
the phase-2 and phase-3 reports and all four proposer scripts, and the completed phase-1, repair,
phase-2, phase-3, and earlier KSUM composition reviews. The paper's local encoding passages and all
locally indexed BKT/Sherstov-adjacent, Ambainis, collision, and Kutin records were inspected. The
worktree already contained unrelated dirty SE files and an automatically created phase-4 transcript;
they were preserved. No network or git commit was used.

The prediction file was written before either phase-4 script. It froze PROGRESS/PARTIAL/BLOCKED,
the absolute-value dual composition, its required one-sided property, the value-pair allocation,
the finite gate, and the suspected correlation loss:
[predictions](logs_ksum_L2p4_20260719/predictions.txt).

## Outcome

The selected dual block composition is **BLOCKED** by two exact structural facts.

1. The reviewed phase-3 inner is one-sided in the useful direction—positive dual mass occurs only
   on YES inputs—but for every block containing at least five complementary pairs it also has
   negative mass on YES inputs. If its correlation is `rho`, then under its absolute-mass law
   `Pr[block NO | dual sign = -1]=rho`. The standard OR composition multiplies these conditional
   probabilities, giving composed correlation

   ```text
   -2 Psi(-1,...,-1) product_j rho_j <= product_j rho_j.
   ```

   Every nontrivial logarithmic phase-3 block has `rho<=4/5`; two such blocks therefore have
   correlation at most `16/25<2/3`, regardless of the outer OR dual.

2. Excluding cross-block hits requires assigning each complementary `sigma`-pair wholly to one
   block. Hence `m r0 <= (q-1)/2` for `m` equal blocks with `r0` value pairs each. The inner band is
   only `2(1+floor(log_5 r0))`, so even a hypothetical outer degree `Omega(sqrt(m))` yields at best
   `Omega(sqrt(m)(1+log(q/m)))`. More importantly, `m=O(q)`: disjoint-value blocking cannot produce
   a `sqrt(N)` factor when `N/q` grows.

The candidate composition lemma and both obstructions have proposer proofs below and are
**CONJECTURED · pending-review** under rule 6. Exact finite runs are NUMERICAL evidence. The broad L2
route is not refuted; it needs a nonstandard composition that repairs false-negative accumulation,
or a construction allowing value reuse while controlling cross-block hits.

## C1 — inner one-sided audit

Write `r=(q-1)/2` and let the phase-3 outer support, in increasing order, be

```text
k_0=0, k_1=1, k_2=5, ..., k_h=5^(h-1).
```

The barycentric coefficient at `k_i` has sign `(-1)^(h-i)`. Orienting the common sign so the
`K=0` coefficient is negative makes the signs alternate

```text
-, +, -, +, ... .
```

Because fixed-point occupancy is at most one, `K=0` is the only NO layer and every `K>0` layer is
YES. Therefore, for every odd `q>=5`:

> **NO-correct / no-false-positive property.** Every supported NO input has negative dual weight,
> and every positive dual weight is on a YES input.

This is not sign perfection once `r>=5` (`q>=11`): the supported `K=5` YES layer is negative. For
`r<=4` (`q=5,7,9`), the support is only `{0,1}` and correlation is exactly one, explaining the
phase-3 finite gates.

Let `P=|mu|` and `S=sgn(mu)`. Zero total mass and unit `l1` give
`P[S=+1]=P[S=-1]=1/2`. The one-sided property gives `S=+1 => g=YES`. If
`rho=<mu,g>`, direct conditioning gives

```text
rho = Pr[g=NO | S=-1].
```

For a block with `r>=5`, the ratios of the `K=1` and `K=5` barycentric weights to the `K=0`
weight are at least `5/4` and `1/4`, respectively. Hence

```text
rho = 2|lambda_0| / sum_k |lambda_k| <= 2/(1+5/4+1/4) = 4/5.
```

Thus the exact one-sided property required by absolute-value composition holds, but its additional
high-accuracy requirement `rho=1-O(1/m)` does not.

## C2 — cross-block embedding and composition

### Cross-block soundness

Fix odd `q` and target `t`. The paper defines `sigma(a)=t-a` and observes that a 2-Sum hit is exactly
`x_j=sigma(x_i)` ([manuscript lines 136–143](../ksum/paper/ksum_small_alphabet.tex)).
Its `k=2` encoding proof isolates complementary value sets and proves that only the matched
cross-pair can hit ([lines 167–178](../ksum/paper/ksum_small_alphabet.tex)); the general
abelian version explicitly partitions nonfixed elements into pairs and records that a cross sum
hits iff the pair labels agree ([lines 212–223](../ksum/paper/ksum_small_alphabet.tex)).

Use that exact involution arithmetic rather than importing a higher-`k` window gadget. Partition a
chosen set of nonfixed `sigma`-pairs into `m` groups. A block may use both endpoints of its assigned
pairs and no other values; set the unique fixed-point occupancy to zero. Since the complement of
an endpoint is the other endpoint of the same assigned pair, a target-summing pair can never cross
two blocks. Consequently global 2-Sum is exactly `OR_m` of the block 2-Sum labels.

Omitting the fixed point is harmless for the phase-3 moment proof: a factorial row involving it is
zero, while all other rows factor over assigned pairs exactly as before. Each assigned pair still
needs total occupancy at least two. Fixed position/value partitions need not themselves be
`S_N x C(sigma)` invariant. Averaging over their group actions preserves annihilation and
correlation and can only decrease `l1`; normalizing the nonzero average restores `l1=1` and cannot
decrease positive correlation. This establishes the symmetry reduction at proposer level, but the
finite gate below is deliberately reported only at fixed-allocation pattern level.

The cost is unavoidable. If equal blocks receive `r0` pairs, then

```text
m r0 <= r=(q-1)/2.
```

Thus the blocks compete for the same alphabet budget; they are not independent copies using all
`q` values.

### Candidate lemma L2P4 — absolute-value composition

Let block `j` have a unit-`l1`, zero-total inner dual `mu_j`, pure high degree at least `d`, and the
NO-correct property above. Let `Psi` be any unit-`l1` outer signed measure on `{±1}^m`, with zero
total and pure high degree at least `D`. For `S_j=sgn(mu_j(x_j))`, define

```text
zeta(x_1,...,x_m) = 2^m Psi(S_1,...,S_m) product_j |mu_j(x_j)|.
```

Then, before symmetry averaging:

- `||zeta||_1=1`, because each `S_j` is uniform and the sign cells are disjoint;
- `zeta` annihilates every block-factorial monomial of total degree below `dD`; and
- for `rho_j=<mu_j,g_j>`, where the composed function is `OR_m(g_1,...,g_m)`,

  ```text
  <zeta,OR_m(g)> = -2 Psi(-1,...,-1) product_j rho_j.
  ```

For degree multiplication, condition on `S`. On a block whose local factorial order is below `d`,
the two conditional expectations agree because their difference is twice the corresponding inner
dual moment. If total order is below `dD`, fewer than `D` blocks can have local order at least `d`.
The conditional product is therefore a multilinear function of fewer than `D` sign bits and is
annihilated by `Psi`. This is the falling-factorial multiplicativity step; it does not substitute a
compressed-label degree.

For correlation, if any `S_j=+1`, one-sidedness makes the global OR deterministically YES. At
`S=(-1,...,-1)`, conditional independence makes global NO occur with probability
`product_j rho_j`, so its expected sign is `1-2 product_j rho_j`. Using `sum Psi=0` gives the
displayed identity. Finally, zero total plus unit `l1` implies
`|Psi(-1,...,-1)|<=1/2`, hence composed correlation is at most `product_j rho_j` after orientation.

This special case is derived here because no usable composition theorem is on disk. It is the
mathematical heart of the run and remains **CONJECTURED · pending-review**.

### Obstruction

If two or more blocks retain a logarithmic inner band, each must have at least five assigned pairs,
so each `rho_j<=4/5`. Candidate Lemma L2P4 then gives

```text
<zeta,OR_m(g)> <= (4/5)^2 = 16/25 < 2/3.
```

This holds for every outer OR dual, even a hypothetical one of pure degree `Omega(sqrt(m))` with
optimal mass at the all-NO point. Using blocks with fewer than five pairs makes `rho_j=1`, but their
inner degree is only two and the growing `log q` factor disappears. This is the preregistered
composition obstruction.

## Literature boundary

- The BKT claim table certifies only the explicit-dual `k`-distinctness theorem, with its exact
  locus at arXiv 1710.09079v3 Section 6, source lines 2103–2113 and informal lines 588–600; it
  contains no block-composition lemma ([BKT page, lines 10–16](../ksum/literature/bun-kothari-thaler-2018-dual-polynomials/README.md)). No BKT theorem is imported.
- Ambainis 2005 is a single-function range-transfer theorem requiring full `S_N x S_M` symmetry,
  at source lines 299–323 ([claim table, lines 10–17](../ksum/literature/ambainis-2005-small-range-symmetric/README.md)). It does not apply to this centralizer/block composition.
- The ABI page records a query-complexity pSearch composition in its lower-bound chain, not a dual
  block-composition theorem ([ABI page, lines 21–34](../ksum/literature/ambainis-balodis-iraids-2021-small-range-claw/README.md)). It is not imported.
- Kutin remains background-only with no verified local theorem locus ([Aaronson–Shi page, line 24](../ksum/literature/aaronson-shi-2004-collision-lower/README.md)).

Accordingly the special composition identity, degree multiplication, and loss formula are derived
from first principles above. The missing general OR-dual construction need not be filled to obtain
the obstruction, which holds for every possible outer dual.

## C3 — gates

### Exact finite gate

The smallest value-disjoint two-block instance is `(N,q,t,m)=(10,5,0,2)`: assign pair `(1,4)` to
one five-position block and `(2,3)` to the other, with fixed-point occupancy zero. Each block uses
the `r0=1` phase-3 endpoint `(I_5-A_5)/2`, which has degree two and correlation one.

The gate is **occupancy-pattern level**, not raw input level: there are `5^10=9,765,625` strings,
while the complete falling-factorial filtration has only 6 or 56 rows in the tested bands. The
reviewed query-degree map makes this an exact pattern-level check, but no fresh raw-string
enumeration or full symmetry average is claimed.

| outer | outer degree | composed band | rows | support | `l1` | correlation | `>2/3` | M2 gate |
|---|---:|---:|---:|---:|---:|---:|---|---|
| correlated, weights on `K=0,1` | 1 | 2 | 6 | 12 | 1 | 1 | PASS | outside M2: zero global `K=2` layer |
| parity | 2 | 4 | 56 | 16 | 1 | `1/2` | FAIL | inside M2: exactly the two-pair M1 product |

Every residual is exactly zero in `fractions.Fraction` arithmetic. Cross-block soundness is checked
from the declared `sigma`-pair allocation. This exhibits the obstruction already at the smallest
gate: the high-correlation outer does not amplify degree, while the degree-amplifying outer returns
to the reviewed M2 class and loses correlation.

| purpose | command | raw log | script SHA-256 |
|---|---|---|---|
| construct/check | `python ksum/tools/ksum_l2p4_block_composition.py --output ksum/artifacts/logs_ksum_L2p4_20260719/block_composition_results.json` | [log](logs_ksum_L2p4_20260719/block_composition.log) | `d4c688ef1036c4859a149e6b835f3b6cf861b2c9012bf5ec6678de5546cf075c` |
| independent reconstruction | `python ksum/tools/ksum_l2p4_exact_verify.py --input ksum/artifacts/logs_ksum_L2p4_20260719/block_composition_results.json` | [log](logs_ksum_L2p4_20260719/exact_verify.log) | `9c2a47730b0053aded0c65c7882a2bc28b92627b323343a05711f9d217cd3454` |

Full commands and hashes: [COMMANDS](logs_ksum_L2p4_20260719/COMMANDS.txt) and
[SHA-256 manifest](logs_ksum_L2p4_20260719/SHA256SUMS.txt).

### M2/D9 gate

The `q=5` correlated order-one object is genuinely outside the full five-condition M2 class: every
M2 member has nonzero mass on every global activity layer, while this object has no `K=2` mass.
This is exactly D9's valid `q>=5` invariant escape test. It has no block-count degree gain. The
parity object has the gain `2 x 2=4`, but it is `-kappa_5 tensor kappa_5`, hence satisfies all five
M2 conditions and has the forced correlation `1/2`. The gate therefore passes as an obstruction,
not as a successful amplifier.

### Cap sweep

Ignoring the correlation failure, an equal-block construction with an outer degree
`Omega(sqrt(m))` could state only

```text
Omega(sqrt(m) * (1+log((q-1)/(2m)))) ,    m <= (q-1)/2.
```

At the lower canonical endpoint `q=5`, `m<=2`, so this is `O(1)`, below both the Johnson
`N^(2/3)` cap and B4a's `N^(1/2+epsilon)5^(1/4)` bound for large `N`. At `q=N`, writing `y=m/N`
shows `sqrt(m)(1+log(N/m)) = sqrt(N) sqrt(y)(1+log(1/y))=O(sqrt(N))`; this is below
`N^(2/3)` and below B4a's `N^(3/4+epsilon)` endpoint. Thus the conditional band is cap-compatible
at both endpoints, but it cannot supply the canonical `sqrt(N)` side at fixed/small `q`.

## Recorded outcome and next candidate lemma

**BLOCKED for standard absolute-value OR dual block composition of the reviewed phase-3 kernel.**

Candidate lemma for the next review/repair:

> Any OR block composition whose inner dual has positive mass only on YES and conditional
> correctness `rho_j=Pr[NO|S=-]` has correlation at most `product_j rho_j`. Therefore constant
> correlation over growing `m` requires total false-negative error
> `sum_j(1-rho_j)=O(1)` (in particular `rho=1-O(1/m)` for identical blocks). The reviewed
> phase-3 logarithmic kernel has `rho<=4/5` as soon as its block contains five pairs.

A live repair must either construct a log-band inner with error `O(1/m)`, use a composition not
driven solely by inner sign bits, or permit value reuse with an exact mechanism suppressing
cross-block hits. None is supplied here.

## What was not checked

- No independent rule-6 review was performed; all new general phase-4 mathematics is pending-review.
- No general `Omega(sqrt(m))` OR dual was constructed, because the universal correlation obstruction
  applies before its detailed form matters and no usable theorem is on disk.
- No full input-level enumeration or exact norm after `S_N x C(sigma)` averaging was run; the finite
  gate is fixed-allocation pattern level, and the symmetry step is analytic/proposer-tier.
- No construction with reused values, cross-block cancellation, error-reduced inner kernel, or
  nonstandard outer composition was attempted.
- No cap-scale, `eta>1/6`, plateau, or exponent result was proved; the canonical obligation is unchanged.
- No even-`q` cycle type, additional target, or additional `(N,q,m)` point was checked.
- No network or git commit was used.
