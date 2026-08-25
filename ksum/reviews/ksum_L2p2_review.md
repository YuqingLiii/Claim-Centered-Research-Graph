# Independent hostile review — KSUM.B4b.L2 phase 2

Date: 2026-07-19  
Reviewer: fresh independent completing reviewer; authored none of the target work; no wanted verdict  
Network: not used  
Commits: none  
Scope: phase-2 annihilation/norm/invariance lemma, tensor-correlation obstruction, finite instances,
preregistration, G11, route scope, and status synchronization

## Pre-action report

Before changing any reviewed status, I reloaded from disk the research-structure protocol, the
proof-DAG protocol including completion rule 6, the KSUM node index, the complete KSUM.B4b.L2 node
and its D7-repaired canonical obligation, parent KSUM.B4b, the full phase-2 report, both proposer
scripts, and the substantive contents and provenance of the complete phase-2 log directory. I also
read the phase-1 query-degree/moment-map derivation and its completed review, the cap repair and its
completed review, and the current whole-DAG and prover-prompt views. No network was used.

The pre-action worktree was already heavily dirty, including pre-existing KSUM node/view changes,
the untracked phase-2 report/scripts/logs, unrelated SE work, and generated artifacts. I preserved
those changes and made no commit.

Fresh reviewer code and outputs:

- [exact finite verifier](../tools/ksum_l2p2r_exact_verify.py) and
  [output](logs_ksum_L2p2r_20260719/exact_review.json);
- [product-obstruction stress test](../tools/ksum_l2p2r_product_obstruction.py) and
  [output](logs_ksum_L2p2r_20260719/product_obstruction.json);
- [commands](logs_ksum_L2p2r_20260719/COMMANDS.txt) and
  [SHA-256 manifest](logs_ksum_L2p2r_20260719/SHA256SUMS.txt).

## Ruling

**M1 PROVED as a general structural claim. M2 PROVED for the precisely defined locally
zero-balanced sign-separated product class. M3 PASS. The L2 route remains CONJECTURED.**

The phase-2 work really does remove the conditioning-preservation sub-obligation for its explicit
kernel: cancellation is proved separately on every exact-total pair-size slice before any mixture.
It also proves an exact correlation obstruction for the intended factorized class. It does not
construct the cap-scale witness, does not prove an exponent lower bound, and does not obstruct a
correlated outer signed kernel. The next route obligation is stated precisely below.

## M1 — annihilation, norm, and invariance

**Verdict: PROVED (general odd `q`, every `N>=q`, every target).**

Let `q` be odd. The involution `sigma(a)=t-a` has one fixed point `f` and
`r=(q-1)/2` two-cycles. On a two-cycle with fixed total `s>=2`, write `A_s` for the symmetric axis
probability and `I_s` for the symmetric central interior probability from the report, and set

`kappa_s=(I_s-A_s)/2`.

The four local identities follow coefficientwise:

- total mass: `(1-1)/2=0`;
- first `i` moment: `(s/2-s/2)/2=0`;
- first `j` moment: the same;
- `l1`: the axis and interior supports are disjoint, so `(1+1)/2=1`.

These are precisely the falling-factorial moments for local total order 0 and 1: `1`, `i`, and
`j`. Fix a labeled pair-total vector `s=(s_1,...,s_r)` with each `s_c>=2` and sum `N-1`, and put
one item at `f`. For a falling-factorial occupancy monomial with exponent vector `alpha`, its value
factors into the fixed-point factor and the `r` local factors

`(n_(a_c))_(alpha_(a_c)) (n_(b_c))_(alpha_(b_c))`.

If `|alpha|<2r=q-1`, some pair has local order below 2. Its local expectation is one of the three
zero moments above, so the complete tensor expectation is zero. This argument is valid for each
fixed `s` separately. Each such tensor is already supported on `sum_a n_a=N`; consequently the
subsequent probability mixture over balanced labeled size vectors cannot reintroduce a residual.
This is a proof of exact-total cancellation, not an assumption that ordinary probabilistic
conditioning preserves moments.

The filtration is the correct query-degree filtration. A compatible one-hot monomial on `m`
distinct queried positions, after `S_N` averaging, is

`prod_a (n_a)_(alpha_a) / (N)_m`, with `sum_a alpha_a=m`.

Repeated same-position variables reduce by idempotence and incompatible symbols give zero. Since
the measure is `S_N`-invariant, pairing against an arbitrary degree-`m` query polynomial equals
pairing against its domain average. Thus all factorial rows of total order below `q-1` span all
query-polynomial restrictions in that degree without loss; no compressed-label polynomial degree
is substituted.

For norm, every fixed-size tensor has norm `prod_c ||kappa_(s_c)||_1=1`. Distinct labeled size
vectors have disjoint support because the pair totals recover the vector. A probability mixture
therefore has exact norm one, and uniform lifting of an occupancy weight to its string orbit
preserves its absolute mass.

For invariance, uniform lifting gives `S_N`. The centralizer of an odd-`q` involution fixes `f`,
permutes the `r` two-cycles, and independently swaps their endpoints. Each `kappa_s` is swap
symmetric and the balanced size-vector law is invariant under pair permutations. Hence the lifted
measure is exactly `S_N x C(sigma)` invariant.

### Fresh finite checks

The fresh verifier imports neither proposer code nor proposer JSON. It reconstructed the measures,
checked every target at both `(N,q)` values, and at the commissioned `t=0` representatives checked
the lifted string measure against every compatible raw one-hot monomial below the claimed degree.

| case | factorial rows | raw one-hot rows | strings | centralizer | `l1` | correlation |
|---|---:|---:|---:|---:|---:|---:|
| `(5,5,0)` | 56 | 1,526 | 3,125 | 8 | 1 | `1/2` |
| `(7,3,0)` | 4 | 22 | 2,187 | 2 | 1 | `1` |

Every residual is exactly zero in `fractions.Fraction` arithmetic. All eight target checks pass.

## M2 — exact tensor-correlation obstruction

**Verdict: PROVED for the class below; exact formula, not merely a bound.**

The report's phrase “pure sign-separated tensor” is too broad if read without its nearby
zero-moment qualifier. The theorem proved by the calculation is about this exact class:

1. the fixed point has occupancy at most one, so global NO means every two-cycle is on its axis;
2. every product component contains one nonzero local signed factor per two-cycle;
3. after a harmless local sign orientation, each factor is nonpositive on its axis, nonnegative on
   its interior, and has zero total mass;
4. arbitrary local shapes, pair totals, and nonzero scales are allowed; and
5. sign-aligned positive mixtures of such products are allowed, including the report's
   permutation-invariant mixture over pair-size vectors.

For local factor `c`, let `a_c>0` be the absolute axis mass. Zero total and sign separation force
interior mass `+a_c`, axis mass `-a_c`, and local `l1=2a_c`. The raw product has norm
`prod_c 2a_c`. After normalization, the absolute all-axis mass is therefore

`prod_c a_c / prod_c (2a_c) = 2^(-r)`.

Orient the global sign so the all-axis/NO mass is `-2^(-r)`. The product's total mass is zero because
every local total is zero. With `F=-1` on NO and `+1` on YES,

`<mu,F> = sum mu - 2 sum_NO mu = 2^(1-r) = 2^(1-(q-1)/2)`.

This is exact and independent of local shape, scale, pair total, or any extra first/higher moment
cancellations. Sign-aligned positive mixtures retain the same norm sign pattern, NO-mass ratio,
and correlation. The fresh stress test verifies 12 unequal-shape/unequal-scale products and four
overlapping positive mixtures for `r=1,2,3,4` exactly.

Consequently every member of this precisely defined class has correlation at most `1/2` for odd
`q>=5` and cannot meet the strict `>2/3` route threshold. This obstruction does **not** cover a
signed/correlated outer combination that cancels moments globally without imposing zero constant
mass on every local factor, nor any other nonfactorizing joint-histogram kernel. Those are genuine
escapes, not counterexamples to the theorem.

### Defect D8 — family label ambiguity (MINOR, repaired in synchronized views)

The report headline sometimes abbreviates the killed class to “pure sign-separated tensor ansatz.”
Taken literally, that could include products lacking per-factor zero constant moment, for which the
formula is not forced. The report's proof and preregistration do state the missing qualifier
(independent balancing in every complementary pair), so this is a naming/scope defect rather than a
mathematical gap. The canonical node and synchronized views now use “fully locally zero-balanced
sign-separated product class,” with the five conditions above controlling the review ruling.

Severity: **MINOR**. It does not change M2's proved status within its intended class and does not
change the route-level status.

## M3 — preregistration, G11, status, and odd-q scope

**Verdict: PASS.**

- All seven submitted hashes match `SHA256SUMS.txt`. The manifest lists the frozen prediction first.
  Filesystem times place `predictions.txt` at `19:45:12Z`, the two proposer scripts at
  `19:46:10Z`/`19:46:13Z`, the outputs at `19:46:19Z`, and the manifest at `19:47:05Z`. The executor
  transcript independently records the prediction-file diff before either script diff and records
  execution only afterward. This establishes ordering on the available disk/transcript record; it
  is not a claim about unknowable off-record knowledge.
- `BLOCKED` was a frozen outcome and explicitly covered a coefficientwise product-kernel subclass.
  The exact theorem above blocks that registered subclass at the correlation gate for every odd
  `q>=5`, regardless of how many additional local moments it cancels. `BLOCKED`, rather than
  `PROGRESS` or `PARTIAL`, follows the frozen definitions.
- The report labels finite checks as machinery evidence only, makes no fit or exponent inference,
  and repeatedly preserves G11. PASS.
- Before this review, `CONJECTURED · pending-review` was accurate: the route had a repaired
  conjectural canonical obligation and new proposer-authored phase-2 mathematics. After this
  completed review, M1 and M2 are proved component claims, but the route itself remains
  `CONJECTURED` because the cap-scale correlated witness is unbuilt.
- The construction and obstruction use only odd `q`, for which `sigma` has one fixed point and all
  targets are translation-equivalent. No even-`q` cycle type is claimed. This matches the D7-repaired
  canonical obligation.

## Cap sweep and next open obligation

No target was strengthened. For fixed `eta in (1/6,1/4]`, retain

`L_eta(N,q)=min{sqrt(N) q^eta, N^(2/3)}`

on odd `5<=q<=N`. It is automatically at most the Johnson `N^(2/3)` cap. Also
`L_eta<=sqrt(N)q^eta<=sqrt(N)q^(1/4)`, so it stays below the reviewed B4a
`N^(1/2+epsilon)q^(1/4)` upper bound. The crossover remains exactly
`q=N^(1/(6eta))`; at `eta=1/4` it is `q=N^(2/3)`. Restricting to odd `q` changes none of these
inequalities.

The next open obligation is:

> Find fixed `eta in (1/6,1/4]`, `c0>0`, `delta in (0,1/3)`, and `N0` such that for every
> `N>=N0`, every odd `5<=q<=N`, and every target, there is a unit-`l1`,
> `S_N x C(sigma)`-invariant signed measure with correlation at least `2/3+delta` that annihilates
> every query polynomial below `c0 L_eta(N,q)`, using a genuinely correlated outer coefficient
> array that cancels moments globally rather than belonging to the fully locally zero-balanced
> sign-separated product/positive-mixture class proved obstructed above.

This remains a conjectural construction problem. The optional even-`q` strengthening remains out of
scope.

## What I did not check

- I did not construct a correlated outer kernel or prove the canonical cap-scale witness lemma.
- I did not prove an `eta>1/6` lower bound, a plateau theorem, or any exponent consequence.
- I did not review even-`q` targets or cycle types.
- I did not rerun the expensive optimizer extraction, add finite optimizer points, or create a
  one-input/held-out discriminator.
- I did not independently re-prove the Johnson or B4a algorithms; I checked the already reviewed
  on-disk quantified caps and reran their algebra against the unchanged target.
- I did not import any BKT, Ambainis, or Kutin lemma, and did not use the network.
