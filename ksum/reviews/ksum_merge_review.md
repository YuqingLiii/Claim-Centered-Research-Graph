# Independent integration review — KSUM journal expansion

Date: 2026-07-20
Reviewer: fresh independent reviewer; authored none of the integrated mathematics; no wanted verdict
Network: not used
Commits: none

Scope: only the journal-expansion additions in
`ksum/paper/ksum_small_alphabet.tex` (abstract/introduction additions, Sections 6--8),
the nine copied dual-polynomial scripts and their descriptions in
`ksum/paper/ancillary/README.md`, and the corresponding integration-status note.

## Pre-action report

Before judging or editing the integration, I reloaded through EOF from disk:

- `research/RESEARCH_STRUCTURE_PROTOCOL.md`;
- `DAG_PROTOCOL.md`, including every item of rule 7;
- `ksum/proof-dag/NODE_INDEX.md`;
- `ksum/proof-dag/nodes/KSUM.B4b.L2.yaml`;
- `ksum/proof-dag/nodes/KSUM.B4b.U1.yaml`.

I then read in full the user-designated source-of-truth reviews:

- `ksum/artifacts/ksum_L2p2_review.md`;
- `ksum/artifacts/ksum_L2p3_review.md`;
- `ksum/artifacts/ksum_L2p4_review.md`;
- `ksum/artifacts/ksum_L2p5_review.md`;
- `ksum/artifacts/ksum_L2p6_review.md`;
- `ksum/artifacts/ksum_B4bU1_review.md`.

For the finite LP proposition newly printed in Section 6, I additionally consulted its completed
source review, `ksum/artifacts/ksum_L2r_review.md`. I preserved the heavily dirty worktree and made no
commit. Unrelated KSUM and SE changes were not altered.

## Ruling

**PASS after minor integration-only repairs. Integration review completed.**

No substantive theorem, proposition, lemma, obstruction class, exponent claim, or cost-model claim
remains stronger than its reviewed source. The fixes made during review were definition,
quantifier, type, priority, and README-output wording fixes; they do not change any reviewed
mathematical scope or DAG status.

In particular:

- M2 has all five reviewed class conditions and is restricted to odd `q>=5`.
- L2P3 states only the reviewed logarithmic degree guarantee and correlation `>=437/581`; it makes
  no `sqrt(N)` or `q^eta` claim.
- Phase-4 T1 is restricted to the displayed fixed-allocation, unaveraged formula. The text
  expressly withholds the product bound after norm-changing averaging and renormalization.
- Phase-4 T2 is restricted to whole-complementary-pair allocation.
- The phase-5 orientation theorem is restricted to identical tilted blocks, one common exact
  total on every pair and block, a raw product tensor, exact averaging/normalization, and
  `N=mrs`.
- G1/G2/G3 are stated separately at their reviewed map/label scopes. The L2P6-G aggregate appears
  only as conjectural prose, with D14's non-exhaustiveness explicit.
- The U1 statement contains the `F_SC^charge` accounting hypotheses and twice says that it is not
  an algorithm-family composition lower bound or a quantum lower bound.

## Rule-7 execution log

### 7a — type audit: EXECUTED

Every new formal statement was audited.

| Statement | Type/domain/quantifier audit | Verdict |
|---|---|---|
| Falling-factorial filtration | `mu` is a signed vector on `Z_q^N`, invariant under the `S_N` permutation representation. Occupancy rows are scalars indexed by `alpha in N_0^q`; total falling-factorial order equals query degree after one-hot idempotence. | PASS. |
| Exact finite LP proposition | Both LPs are finite rational programs on invariant orbit weights. The certification predicate is strictly `optimum>2/3`; the three degree pairs `(0,2),(0,2),(2,3)` match the completed repair review. | PASS. |
| Pair-tensor theorem | Odd `q>=3`, `N>=q`, every `t`; measure lies in `R^{Z_q^N}`, has unit L1 norm and full `S_N x C(sigma)` invariance; the annihilation band is `<q-1`. | PASS. |
| Tilted log-band theorem | Odd `q>=3`, `N>=q`, every `t`; correlation and L1 are scalars; `p` is now explicitly a query polynomial; the guaranteed band is `2(1+floor(log_5((q-1)/2)))`. | PASS after a minor type clarification. |
| Band multiplication | Each block measure is now explicitly on a fixed-total occupancy slice; convolution lies on the global fixed-total slice, is nonzero, and has band at least the sum of block bands. | PASS after a minor type clarification. |
| M2 product obstruction | The paper now explicitly fixes `N,t` and the domain `Z_q^N`; odd `q>=5`, `r=(q-1)/2`, all five class conditions, unit-L1 normalization, and correlation `2^(1-r)` are present. | PASS. |
| Phase-4 T1/T2 | `mu_j` and `Psi` are unit-L1 zero-total signed measures on block support and the sign cube respectively; `zeta` is on the product support; the theorem is explicitly unaveraged. Pair counts `r_j`, block count `m`, and string length are not conflated. | PASS. |
| Phase-5 orientation theorem | `q=2r+1>=5`, `m>=2`, `s>=2`, identical blocks, fixed-point occupancy zero, common exact total, raw product, `S_N` average, actual post-average norm, and `N=mrs` are all explicit. | PASS. |
| G1/G2/G3 | `V=R^X`, `dim V=q^N`; `U_lambda` and `M_lambda` are irrep and multiplicity factors. The review added explicit embeddings `Q_(lambda,j):M_lambda->V`, `j<=dim U_lambda`, `B_lambda in End(M_lambda)`, and the typed Reynolds map. `diag A` is in `R^X`, and `tr A>0` for nonzero PSD `A`. | PASS after minor definition/type clarifications. |
| Charged model | `s,q,ell,b,m,a,c,rho,D,epsilon,theta` retain their cost/exponent roles. Depth and theta quantifiers, hard-profile residual charge, child-call charge, and all-range base uniformity are explicit. | PASS. |
| Section 8 target | Fixed `eta in (1/6,1/4]`, `c0>0`, `delta in (0,1/3)`, and `N0`; every large `N`, odd `5<=q<=N`, every `t`; full invariance, unit L1, correlation, and query-degree annihilation are explicit. | PASS after minor quantifier clarification. |

### 7b — no statement stronger than its review: EXECUTED

- M2: all five conditions occur at the theorem statement, not only in its proof; `q>=5` is
  explicit. Correlated signed outer combinations remain outside condition 5.
- Phase 3: D9 is respected. The construction exists at `q=3`, but the paper does not say it escapes
  M2 there; the M2 theorem starts at `q=5`.
- Phase 4: T1 is headed “Unaveraged” and tied to formula (48). Lines immediately after its proof
  state that the bound is not asserted after a norm-reducing group average. D10 remains open.
- Phase 5: the theorem carries identical blocks, one common exact total on every pair/block, the
  raw product tensor, and `N=mrs`. Unequal totals, nonidentical blocks, non-product couplings,
  correlated orientations, and alternative inners are expressly excluded.
- Phase 6: the aggregate “optimizer-faithful, irrep-label-only” assertion is identified as only a
  conjecture and not a formula-exhaustive class. It is not a theorem/proposition item.
- U1: every charged-accounting hypothesis from the certified review is printed. The paper calls it
  a cost-model statement and expressly excludes an algorithm-family or all-quantum lower bound.
- Tilted witness: wording was tightened from potentially exact-sounding “band” language to the
  **proved/displayed annihilation guarantee**. Nothing claims `sqrt(N)` growth or
  `q^eta`, `eta>1/6`, growth.

No substantive over-scope statement remains.

### 7c — anchoring ban/headline re-derivations: EXECUTED

The mandatory source scopes were read first, but I did not accept the integrated proofs or scripts
as verification. I reconstructed both headline claims algebraically in my own typed model before
assigning the verdict.

**Tilted log-band.** Put `r=(q-1)/2` and `h=1+floor(log_5 r)`. On every exact pair-total slice,
the axis and interior probability laws have equal mass and equal first coordinate moments. Hence a
factorial row can depend on an activity bit only after spending local order at least two. The
order-`h` divided-difference functional on `T={0,1,5,...,5^(h-1)}` annihilates every activity
polynomial of degree below `h`; therefore every occupancy/query row below `2h` vanishes. Disjoint
activity and pair-total supports give exact L1 norm one. Since the fixed point has occupancy one,
NO is exactly the `K=0` layer, so correlation is

`2|lambda_0| / sum_k |lambda_k|`.

For node `5^j`, the ratio is `A_j C_(h-1-j)`. Separating the first factor gives
`C_u<=25/19`; `A_0=1`, `A_1=1/4`, `A_2=1/96`, and the remaining geometric tail gives
`sum_j A_j<=29/23`. Thus correlation is at least

`2/(1+(25/19)(29/23))=437/581`,

and `437/581-3/4=5/2324`. This reconstruction depends on `q`, not on growing `N`.

**Orientation coherence.** With `m` identical blocks and one common exact total `s` on each of the
`r` pairs, every block has `rs` positions, hence `N=mrs`. Conditional on the all-axis layer, a
fixed pair's `m` independent endpoint orientations all agree with probability `2^(1-m)`; across
`r` pairs the exact factor is `2^(-r(m-1))`.

For the post-average norm, evaluate the occupancy generating polynomial at endpoint phases
`(exp(i theta),exp(-i theta))`. Choosing `theta=pi/s` for even `s` and `pi/(s+1)` for odd `s`
gives `I_s=-A_s`, with `|A_s|=1` or at least `2^(-1/2)`. All nonzero outer support nodes are odd
and the outer total is zero, so the one-block modulus is `rho|A_s|^r`; convolution raises it to
`rho^m|A_s|^(rm)`, which lower-bounds the post-average L1 norm. Dividing the exact NO numerator
gives

`corr <= 2^(r+1-m(r+1)) |A_s|^(-rm)`.

For even `s` the exponent is at most `-3`; for odd `s` it is at most `-1` after the
`2^(rm/2)` loss. Therefore correlation is at most `1/8` and `1/2`, respectively. No excluded
block/coupling class entered this derivation.

### 7d — frozen scopes: EXECUTED

The source reviews were authoritative only within their recorded uses. The paper's exact-total
mixing, query-degree filtration, phase-3 sign structure, phase-4 normalization boundary,
phase-5 Fourier map, phase-6 multiplicity factor, and U1 plateau quantifier were all reopened at
the granularity used by the integrated text. No prior PROVED/CERTIFIED* label was treated as
immunity for a wider parameter range or stronger map.

### 7e — standing failure modes and cap sweep: EXECUTED

- Normalization: the phase-4 numerator/norm distinction is explicit; phase 5 normalizes by the
  actual post-average norm; G3 divides only by positive `tr A`; M2 mixtures are sign-aligned.
- Type/dimension: block/pair/value/position indices and irrep/multiplicity/ambient spaces were
  separated. Minor missing definitions were repaired.
- Undefined terms: `pure high degree`, sign alignment, Reynolds projection, multiplicity
  embeddings, and nontrivial H-satellite now resolve in-paper.
- Family boundaries: all M2/T1/T2/orientation/G1--G3/U1 boundaries were checked against their
  completed reviews. D10 and D14 remain open where required.
- Value/formula: the copied scripts were SHA-compared and eight standard-library scripts were run;
  see 7f. The prose does not infer asymptotics from finite values.

Cap endpoints for the canonical target `L_eta=min{sqrt(N)q^eta,N^(2/3)}`:

- At `q=5`, `L_eta=Theta(sqrt(N))`, below the Johnson walk `O(N^(2/3))` and below B4a
  `O_epsilon(N^(1/2+epsilon)q^(1/4))`.
- At `q=N`, `L_eta=N^(2/3)` for every `eta>1/6`, equal to the Johnson exponent and below B4a's
  `N^(3/4+epsilon)` endpoint.
- For all intermediate `q`, the minimum enforces the walk cap and `eta<=1/4` enforces the B4a cap.

Other general claims:

- The pair tensor's formal `<q-1` annihilation band may exceed algorithmic caps, but for `q>=5`
  its reviewed correlation is at most `1/2`; it makes no complexity claim. At `q=3`, its band is
  constant.
- Band multiplication and phase-4 degree multiplication assert formal annihilation only; neither
  asserts cap-violating correlation.
- The tilted guarantee `2(1+floor(log_5((q-1)/2)))` is below `q^(2/3)<=N^(2/3)` and below
  `sqrt(N)q^(1/4)` throughout its range. It has no growing-N component.
- The phase-5 and G3 constructions fail the correlation or constant-moment gate, respectively.
- The charged recurrence meets the existing upper bound at the active crossover
  `q=N^(2/3)` and does not claim an unconditional cap.

The Section 8 open window is therefore cap-compatible and does not claim that D14's surviving maps
are exhausted.

### 7f — value versus formula: EXECUTED

Exact printed values match their reviewed sources:

- `437/581`, with exact margin `5/2324` over `3/4`;
- M2 correlation `2^(1-(q-1)/2)`;
- phase-4 `16/25<2/3`;
- held-out `Adv^+/-` values `3.001212274702435` at `(4,4,0)` and
  `3.077867545916693` at `(4,5,0)`;
- the finite LP optimum table and certified degrees match `ksum_L2r_review.md`.

The nine ancillary copies are byte-for-byte identical to their reviewed `tools/` originals:

| Script | SHA-256 | Match |
|---|---|---|
| `ksum_l2rr_exact_review.py` | `f1fbf18d86cb2a2b58ed5e68c5a823f5fe5db43e6b24c23deca0113f15930caa` | yes |
| `ksum_l2p2r_exact_verify.py` | `b9868f79eab8dbfa948476c415381e6b87366a01ba46048786c2d81a0f0001c1` | yes |
| `ksum_l2p2r_product_obstruction.py` | `331790333044abbebbb0e3b149b7760588fa6beae4bf814865c457cc594296da` | yes |
| `ksum_l2p3r_finite_verify.py` | `316349786b0e0f8ef4389d861a082046c6489fce079e63dc64b9d69c3ea39603` | yes |
| `ksum_l2p3r_outer_audit.py` | `eba17c0ceb2055097626742a247057465cd27348e03dd4857ea6fb9226af8125` | yes |
| `ksum_l2p4r_exact_review.py` | `a2d73be21a80f13fad5580545fe61e8afdfc7db54e512ad2a0d9021d6a8075dd` | yes |
| `ksum_l2p5r_exact_review.py` | `dde0338c984fb9ad4ef2099da325f851fcc8360f1e7b8d1861cee24e2f14c45a` | yes |
| `ksum_l2p5r_fourier_review.py` | `31c70fd00b338180f22a9fb8530bbc784ea4cf24e8a628159df091c1f1ac18f2` | yes |
| `ksum_l2p6r_exact_review.py` | `a01c87fe3b51489fae34e690283503286a351dc197f229e3930ff6bf91be106d` | yes |

The eight scripts requiring only the standard library ran successfully from the ancillary
directory. The two phase-2 scripts were run with their mandatory `--output` arguments; phase 4 was
run with optional `--output`; phase 6 was run with optional `--json`; the remaining four printed
JSON to stdout. All assertions/gates passed. The scripts independently reconstruct formulas or
objects as their headers claim; they do not import proposer modules/JSON.

`ksum_l2rr_exact_review.py` was not executable in the available interpreter because SymPy is not
installed. Its README dependency declaration, command form, source hash, cases, strict threshold,
and header were checked, and its reviewed exact output was compared with the paper. This is listed
again under “What I did not check”; it does not convert the prior finite review into a fresh run.

### 7g — terms of art: EXECUTED

All load-bearing terms now resolve in the paper: query degree via the one-hot/falling-factorial
filtration; LP-certified degree and its strict predicate; axis/interior/all-axis via pair
occupancy; pure high degree; sign-aligned mixture; fixed-allocation unaveraged composition;
whole-pair allocation; common exact pair total; orientation coherence; Reynolds projection;
nontrivial H-satellite; multiplicity embedding; charged model; range-independent base; and the
cap function `L_eta`.

The undefined aggregate phrase “optimizer-faithful, irrep-label-only” is intentionally identified
as non-formula-exhaustive and only conjectural; it is not used in a theorem statement.

## Integration fixes made

All were minor and are already applied:

1. `ksum_small_alphabet.tex`, abstract and tilted discussion (current lines near 38 and 849--855):
   replaced exact/priority-sounding “logarithmic pure high degree”, “first”, “its band is only”,
   and “exact band” wording by a logarithmic **proved/displayed annihilation guarantee**. Required
   weakening: do not imply the sufficient band was proved tight or establishes `q^eta` growth.
2. Same file, near the beginning of Section 6 and the tilted theorem: defined pure high degree and
   made `p` explicitly a query polynomial.
3. Same file, band multiplication and M2 statements: corrected the occupancy-measure type,
   supplied `N,t` and the string-measure domain, and resolved “sign-aligned”.
4. Same file, phase-5 theorem: clarified that it uses the tilted pair construction with
   fixed-point occupancy changed to zero, while retaining identical blocks/common exact
   total/raw-product/`N=mrs` scope.
5. Same file, transfer proposition: defined Reynolds projection, the multiplicity embeddings,
   `B_lambda`'s domain, and nontrivial H-satellite.
6. Same file, charged model and Section 8: made theta independent of epsilon; restored the exact
   `delta in (0,1/3)`, target, invariance, and query-polynomial quantifiers.
7. `ancillary/README.md`, JSON behavior paragraph: corrected the false claim that every script has
   a top-level `"verification":"PASS"` field. Phase 4 uses per-gate PASS fields and phase 6 exact
   booleans. Commands and dependency limits otherwise match the script headers.

There are **no unresolved substantive defects**.

## Per-section verdicts

- **Abstract/introduction additions: PASS after wording repair.** They describe a toolkit and
  scoped obstruction map, explicitly say the exponent gap remains open, and make no phase-6 or
  U1 overclaim.
- **Section 6 (dual toolkit): PASS after minor type/tightness wording repairs.** The finite LP,
  pair tensor, tilted witness, and band-multiplication statements match reviewed scopes.
- **Section 7 (scoped obstructions/design evidence): PASS.** M2, T1/T2/D10, phase-5 orientation,
  G1--G3/D14, U1, and the exact adversary values retain their hard boundaries.
- **Section 8 additions: PASS after quantifier repair.** The canonical target is odd-q/all-target,
  cap-compatible, and explicitly leaves every reviewed escape class open.
- **Ancillary README and nine copies: PASS with one disclosed runtime limitation.** All hashes
  match; eight scripts run and pass; the missing SymPy dependency prevented a ninth fresh run and
  is accurately declared.
- **Labels/references/build: PASS.** See compilation below.

## Compilation and reference check

From `ksum/paper` I ran:

```text
pdflatex -interaction=nonstopmode -halt-on-error ksum_small_alphabet.tex
bibtex ksum_small_alphabet
pdflatex -interaction=nonstopmode -halt-on-error ksum_small_alphabet.tex
pdflatex -interaction=nonstopmode -halt-on-error ksum_small_alphabet.tex
```

Result: **34 pages**, zero LaTeX/BibTeX errors, zero undefined references/citations, and zero
multiply-defined-label diagnostics. Three overfull-box warnings remain in pre-existing material
outside the integrated Sections 6--8; no new-section overfull warning remains.

## What I did not check

- I did not review unchanged mathematics outside the abstract/introduction additions and Sections
  6--8, except where needed for endpoint cap arithmetic and reference resolution.
- I did not rerun the SymPy LP reviewer because SymPy is absent from the available Python
  interpreter. I did not install packages or use the network.
- I did not rerun MOSEK, optimizer extraction, or the held-out numerical SDP pipeline. I checked
  the integrated values and caveats against the completed phase-6 review and ran the exact
  phase-6 transfer gates.
- I did not independently re-prove the Johnson walk or B4a algorithms; I checked the integrated
  claims against their reviewed quantified caps at both endpoints.
- I did not review even-`q` asymptotic witness obligations; the paper correctly leaves them outside
  the route-minimal Section 8 target.
- I did not claim the tilted `2m` guarantee or the phase-5 `1/2` bound is tight.

## Repository closeout

- `python tools/proof_dag_check.py --problem ksum`: PASS; 38 node files structurally valid. The
  checker printed its existing advisory warnings that the native B4b/L1/L2/L3 nodes are eligible
  for semantic checks.
- `python tools/literature_check.py`: PASS; 24 papers, schema v1.
- `git diff --check`: global exit 2 solely because the unrelated pre-existing modified file
  `ksum/artifacts/logs_se_frames3_20260719/codex_run.log` contains trailing whitespace. That user-owned
  SE log was not changed. A path-scoped `git diff --check` over every tracked file touched by this
  review passes, and a direct trailing-whitespace scan of this new review artifact passes.
