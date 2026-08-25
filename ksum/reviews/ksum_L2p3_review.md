# Independent hostile review — KSUM.B4b.L2 phase 3

Date: 2026-07-19  
Reviewer: fresh independent completing reviewer; authored none of the target work; no wanted verdict  
Network: not used  
Commits: none  
Scope: tilted-product construction, M2 escape, divided-difference annihilation, correlation,
quantifiers, preregistration, G11, stop rule, and DAG/status synchronization

## Pre-action report

Before any status action I reloaded from disk the research-structure protocol, the proof-DAG
protocol including completion rule 6, the KSUM node index, the complete `KSUM.B4b.L2` node and its
D7-repaired canonical odd-`q` obligation, parent `KSUM.B4b`, the complete phase-3 report, both
phase-3 proposer scripts, and every substantive file in the phase-3 log directory. I also reloaded
the completed phase-2 review and its five-condition definition of M2, and checked the earlier
falling-factorial/query-degree map and the current whole-DAG and prover-prompt views. No network was
used.

The worktree was already heavily dirty, with the phase-3 work and much earlier KSUM and unrelated SE
work uncommitted or untracked. I preserved those changes and made no commit.

Fresh reviewer code imports neither proposer script nor proposer JSON:

- [outer-functional and M2 audit](../tools/ksum_l2p3r_outer_audit.py), with
  [exact output](logs_ksum_L2p3r_20260719/outer_audit.log);
- [finite occupancy/string reconstruction](../tools/ksum_l2p3r_finite_verify.py), with
  [exact output](logs_ksum_L2p3r_20260719/finite_verify.log);
- [commands](logs_ksum_L2p3r_20260719/COMMANDS.txt) and
  [SHA-256 manifest](logs_ksum_L2p3r_20260719/SHA256SUMS.txt).

## Ruling

**The phase-3 L2P3 logarithmic-band lemma is PROVED as a component claim, with one MINOR endpoint
repair to the M2-escape wording. The L2 route remains CONJECTURED.**

For every odd `q>=3`, every `N>=q`, and every target `t`, the recorded construction is
`S_N x C(sigma)` invariant, has `l1=1`, annihilates every query polynomial of degree below

`d=2(1+floor(log_5((q-1)/2)))`,

and has correlation at least `437/581>3/4=2/3+1/12`. The band is a sufficient lower bound on pure
high degree; neither the report nor this review proves it tight. It is logarithmic in `q`, has no
growing `N` component, and does not approach the canonical cap-scale obligation.

The only defect is that the report says the construction escapes M2 for all odd `q>=3`. It does so
for `q>=5`. At `q=3` there is one pair, the outer weights are `(-1/2,+1/2)`, and the construction is
exactly the reviewed M1 product, hence is inside M2. This endpoint exception does not affect the
lemma: M2's correlation obstruction equals one at `q=3` and poses no barrier there.

## 1. Escape from the complete M2 class

**Verdict: PASS for `q>=5`; MINOR scope defect at `q=3`, repaired in the canonical views.**

Rechecking all five conditions:

1. The fixed point has occupancy exactly one. Thus condition 1 holds, and NO is precisely the
   all-axis event `K=0`.
2. In the displayed pattern expansion there is one nonzero local factor on every pair. Condition 2
   alone is not the escape.
3. Those displayed factors are the probability measures `A_s` or `I_s`, each of total mass one;
   they are not themselves locally zero-total sign-separated factors. Thus the displayed
   decomposition does not satisfy condition 3. This observation alone would not exclude an
   equivalent alternative M2 representation.
4. Condition 4 is permissive: arbitrary shapes, totals, and scales are allowed. It neither excludes
   nor rescues the construction.
5. The outer divided-difference coefficients form a signed correlated combination, not a
   sign-aligned positive mixture. This is the intended violation, but it must be made
   representation-independent.

The representation-independent obstruction is the aggregate `K`-layer signature. In every M2
product component, conditions 2 and 3 force nonzero axis and interior absolute mass on every pair.
Consequently every layer `K=0,...,r` has nonzero signed mass, with the common alternating product
sign. A sign-aligned positive mixture cannot cancel any such layer. Pair permutations, endpoint
swaps, and target-conjugating relabelings preserve `K` and therefore preserve this fact.

For every `r>=2`, the phase-3 construction has zero mass at `K=2`, because its support is
`{0,1,5,25,...}`. Hence no allowable relabeling can turn it into any member of the complete M2 class.
For `r=1`, however, the support is all of `{0,1}` and the weights are the M1 signs; the construction
is an M2 member. The fresh outer audit verifies this boundary exactly.

### Defect D9 — M2 escape overclaimed at the `q=3` endpoint (MINOR)

The report's unrestricted statement “violates M2 condition 5” is false at `q=3`, and its original
five-condition discussion did not prove non-representability under relabeling. The corrected
statement is: **the family genuinely escapes the entire M2 class for odd `q>=5`; at `q=3` it is the
in-class M1 endpoint.** The zero `K=2` layer proves the first clause invariantly.

Severity: **MINOR**. The component lemma, its uniform correlation, its annihilation band, and the
canonical route (which starts at odd `q>=5`) are unchanged.

## 2. Annihilation band

**Verdict: PASS.**

Write `r=(q-1)/2`, `m=1+floor(log_5 r)`, and

`T_m={0,1,5,...,5^(m-1)}`.

There are `m+1` distinct nodes. The barycentric weights

`lambda_k = 1 / product_(u in T_m, u!=k)(k-u)`

are the order-`m` divided-difference coefficients. Therefore

`sum_(k in T_m) lambda_k p(k)=0`

for every polynomial `p` of degree `<m`. Uniformly distributing aggregate layer weight over the
`binom(r,k)` indicator patterns converts a named `j`-pair monomial to `(k)_j/(r)_j`; hence the outer
functional annihilates every multilinear polynomial in `z` of degree `<m`.

Now fix one exact pair-total vector. A falling-factorial occupancy monomial factors over pairs. On a
pair of local order zero or one, `A_s` and `I_s` have the same total mass and both coordinate means,
so its conditional expectation is independent of `z_c`. Dependence on `z_c` can occur only at local
order at least two. Total occupancy order `<2m` therefore leaves fewer than `m` `z`-dependent pairs;
the conditional expectation is a multilinear polynomial of degree `<m` and the outer functional
kills it. This is proved on each exact-total slice before the balanced mixture, so conditioning does
not reintroduce a residual.

The earlier reviewed filtration is used consistently. An `S_N`-averaged compatible one-hot monomial
of query degree `a` is a nonzero constant times a falling-factorial occupancy monomial of total
order `a`; repeated same-position variables reduce by idempotence and incompatible labels vanish.
Thus there is no degree loss in lifting the result to all query polynomials below `2m`.

The `log_5` comes exactly from the number of geometric support points that fit in `0<=K<=r`:
`1,5,...,5^(m-1)<=r<5^m`. Base five is also what makes the correlation estimate exceed `3/4`; the
logarithmic band is sufficient, not asserted tight. Equivalently, multiplying the M1 parity
functional by

`Q(K)=product_(ell in {0,...,r}\T_m)(K-ell)`

uses degree `r-m`, and

`Q(k)=(-1)^(r-k) r! lambda_k/binom(r,k)`.

The parity outer order `r` consequently retains order `m`, matching the direct argument.

## 3. Correlation and exact finite gates

**Verdict: PASS.**

The outer constant moment vanishes, so the signed measure has total mass zero. Since the fixed point
has occupancy one, `K=0` is the only NO layer and is oriented negative. Disjoint pattern and
pair-total supports give exact `l1=1`, hence

`<mu,F>=2|lambda_0|/sum_k |lambda_k|`.

For the nonzero node `k=5^j`, exact cancellation of common powers of five gives

`|lambda_(5^j)|/|lambda_0| = A_j C_(m-1-j)`,

where `A_j=product_(d=1)^j(5^d-1)^(-1)` and
`C_h=product_(d=1)^h(1-5^(-d))^(-1)`. Separating the `d=1` term and using
`product(1-x_i)>=1-sum x_i` gives `C_h<=25/19`. Also

`sum_(j>=0) A_j <= 1+1/4+(1/96)/(1-1/24)=29/23`.

Thus `sum_j |lambda_(5^j)|/|lambda_0|<=725/437` and

`<mu,F> >= 2/(1+725/437)=437/581`.

The strict comparison is exact:

`437/581 - 3/4 = 5/2324 > 0`.

Therefore the fixed choice `delta=1/12` satisfies the required strict inequality
`<mu,F> > 2/3+delta`; no equality endpoint is used.

The fresh finite reconstruction checked every target, not only the preregistered representatives:

| `(N,q)` | targets | factorial rows/target | raw one-hot rows/target | `l1` | correlation | result |
|---|---:|---:|---:|---:|---:|---|
| `(5,5)` | 5 | 6 | 26 | `1` | `1` | PASS |
| `(7,3)` | 3 | 4 | 22 | `1` | `1` | PASS |

Every residual is zero in `fractions.Fraction` arithmetic, and centralizer orders are respectively
8 and 2. Correlation one is expected at both gates: each has `m=1`, so the outer support is only
`{0,1}` with weights `(-1/2,+1/2)`. The loss begins when `r>=5` adds `K=5`; exact correlations for
successive support sizes begin `1, 4/5, 16/21, 992/1315, ...` and decrease toward approximately
`0.75249`. The proved `437/581` is a slightly weaker uniform bound; its loss comes from bounding
all `C_h` by `25/19` and the infinite `A_j` tail by `29/23`, not from either finite gate.

## 4. Quantifiers, invariance, and caps

**Verdict: PASS.**

- The proof and construction use odd `q`, where `sigma(a)=t-a` has one fixed point and `r`
  two-cycles. No even-`q` claim is made.
- The formula is defined for every target. C7's translation equivalence supplies the all-`t`
  conjugacy, and the fresh finite code also checks every target directly.
- `N>=q=2r+1` is used only to choose exact pair totals `s_c>=2` summing to `N-1`. It ensures disjoint
  axis/interior support. The annihilation degree depends only on `q`; the construction does not
  engage or improve the `sqrt(N)` side of the canonical target.
- Uniform `S_N` lifting gives position invariance. Endpoint symmetry, exchangeable outer weights,
  and a pair-permutation-invariant size-vector mixture give the full `C(sigma)` invariance.
- The logarithmic band is far below
  `min{sqrt(N)q^eta,N^(2/3)}` for the canonical fixed `eta>1/6` regime. It violates neither the
  Johnson `N^(2/3)` cap nor B4a. The report does not infer a cap-scale or exponent result.

## 5. Preregistration, PROGRESS, G11, and stop rule

**Verdict: PASS, subject only to D9's endpoint wording repair.**

- All seven phase-3 manifest hashes match current disk contents. The manifest lists the frozen
  prediction first. Filesystem times place `predictions.txt` at `20:09:15Z`, the proposer scripts at
  `20:12:26Z` and `20:12:29Z`, outputs at `20:12:49Z`/`20:12:50Z`, and the manifest at `20:14:44Z`.
  The executor transcript records the prediction diff before either script diff and the run only
  afterward. This proves ordering on the available disk/transcript record, not unknowable
  off-record knowledge.
- The frozen PROGRESS definition is met: there is an explicit outer-correlated family for general
  odd `q` (genuinely outside M2 on the canonical `q>=5` range), a proved growing annihilation band,
  a proved `q`-independent strict margin, and exact rational verification at both required points.
- G11 is respected. The finite points verify machinery and exact finite claims; the general lemma is
  analytic, and no exponent trend is inferred from the finite values.
- The commissioned stop rule fired after mechanism (a). The report explicitly discloses that the
  few-pair and BKT-style mechanisms (b)/(c) were not attempted and imports no unreviewed composition
  theorem.
- Under DAG rule 6, this completed independent review licenses **PROVED** for the L2P3 component
  lemma. It does not license PROVED for the route-level L2 leaf, whose cap-scale claim remains open.

## Next obligation and cap sweep

The route remains **CONJECTURED**. The next obligation is to amplify the now-reviewed logarithmic
band toward polynomial scale while also engaging the untouched `sqrt(N)` side:

> Find fixed `eta in (1/6,1/4]`, `c0>0`, `delta in (0,1/3)`, and `N0` such that for every
> `N>=N0`, every odd `5<=q<=N`, and every target, an `S_N x C(sigma)`-invariant unit-`l1` signed
> measure has correlation at least `2/3+delta` and annihilates every query polynomial below
> `c0 min{sqrt(N)q^eta,N^(2/3)}`.

This statement is unchanged by the review. It is capped by `N^(2/3)` by definition. Since
`eta<=1/4`, it is also at most `sqrt(N)q^(1/4)`, below the reviewed B4a
`N^(1/2+epsilon)q^(1/4)` cap. The crossover is `q=N^(1/(6eta))`, and at `eta=1/4` it is
`q=N^(2/3)`. The current `O(log q)` band supplies neither polynomial-`q` amplification nor any
`sqrt(N)` growth.

## What I did not check

- I did not construct the cap-scale witness, amplify the logarithmic band, or engage the `sqrt(N)`
  side.
- I did not prove an `eta>1/6` lower bound, a plateau theorem, or an exponent consequence.
- I did not review even-`q` targets or cycle types.
- I did not prove the stated `2m` band is tight or locate the first surviving query polynomial.
- I did not rerun optimizer extraction, add larger occupancy/string finite instances, or re-audit the
  Johnson and B4a algorithms themselves; I only checked the unchanged cap algebra.
- I did not attempt mechanisms (b) or (c), import BKT, Ambainis, or Kutin, or use the network.
