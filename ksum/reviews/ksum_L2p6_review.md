# Independent hostile review — KSUM.B4b.L2 phase 6

Date: 2026-07-19
Reviewer: fresh independent hostile reviewer; authored none of the target work; no wanted verdict
Network: not used
Commits: none
Scope: L2P6-G parts 1–3, held-out labels/values, exact positive-transfer gates,
preregistration, escape ledger, frozen outcome, cap-swept next obligation, and DAG synchronization

## Pre-action report

Before taking a status action, I reloaded from disk the research-structure protocol, the complete
proof-DAG protocol including rule 7, the node index, the full `KSUM.B4b.L2` record and parent
`KSUM.B4b`, the complete phase-6 report, all three proposer scripts, and the substantive phase-6
logs. I checked the frozen prediction, commands, all 20 manifest entries, output JSON/NPZ files,
and the executor transcript. I also reloaded the completed phase-2 through phase-5 reviews in the
exact M1/M2/L2P3/T1/T2/D10 scopes now used, the L33 node/note/completed review, the complete reviewed
L33 solver and expL extractor, the Front-L structure report, and the held-out expL data.

The worktree was already dirty. In particular, the target/index/legacy KSUM files were modified,
the phase-6 report/scripts/logs were untracked, and unrelated SE artifacts were modified or
untracked. I preserved those changes and made no commit.

Before opening the phase-6 report, I derived the Wedderburn gauge statement, the Reynolds fact, and
the positive-diagonal constant moment in my own notation and gave the derivation to the user. The
later disk archive is [ANCHORING_DERIVATION.txt](logs_ksum_L2p6r_20260719/ANCHORING_DERIVATION.txt);
its timestamp is not used to overstate the ordering evidence.

Fresh reviewer evidence:

- [exact rational reviewer](../tools/ksum_l2p6r_exact_review.py), with
  [output](logs_ksum_L2p6r_20260719/exact_review.json);
- [read-only held-out pipeline audit](../tools/ksum_l2p6r_pipeline_audit.py), with
  [output](logs_ksum_L2p6r_20260719/pipeline_audit.json);
- [commands](logs_ksum_L2p6r_20260719/COMMANDS.txt) and
  [review manifest](logs_ksum_L2p6r_20260719/SHA256SUMS.txt).

## Ruling

**L2P6-G1 (multiplicity gauge), G2 (direct-vector Reynolds zero), and G3 (positive
diagonal/Reynolds band zero) are PROVED components at the precise scopes below. The aggregate
L2P6-G remains CONJECTURED as a candidate obstruction, not a completion-tier theorem.**

The aggregate loses a tier because “optimizer-faithful, irrep-label-only spine+satellite transfer
class” is not a formula-defined class. The report proves facts about irrep labels and two natural
extraction maps; it does not show that those maps exhaust all signed, centered, off-diagonal, or
nonlinear uses of optimizer blocks. This is MAJOR D14. Accordingly, the phase is **BLOCKED/reviewed
only for the explicitly enumerated literal mechanism**: cross-`N` multiplicity coordinates inferred
from terminal irrep labels alone, direct satellite-vector Reynolds extraction, or the nonnegative
`Reynolds(diag A)/tr A` extraction. The frozen paradigm-level BLOCKED condition is not established.

The held-out labels, 91–92% basis-invariant diagnostics, two numerical Adv± values, and two exact
finite projector measures pass. They do not supply a no-refit closed-family capture or an exponent
claim. The L2 leaf remains **CONJECTURED**; `KSUM.B4b` and all ancestors remain **OPEN**.

## Rule-7 execution log

### 7a — type audit: EXECUTED

Let `G=S_N x C(sigma)`, `H=S_(N-1) x C(sigma)`, `X=Z_q^N`, and `V=R^X`, so
`dim V=q^N`. For an H-irrep `U_lambda` of dimension `d_lambda` occurring with multiplicity
`m_lambda`, write `M_lambda=R^(m_lambda)`.

| In-scope display | Domain, codomain, and dimension audit | Result |
|---|---|---|
| `V = direct_sum U_lambda tensor M_lambda` | `rho_H(h)` acts as `rho_lambda(h) tensor I_(m_lambda)` on a block of dimension `d_lambda m_lambda`. | PASS. |
| `End_H(V)=direct_sum I tensor End(M_lambda)` | Each reduced block is an `m_lambda x m_lambda` operator; the real symmetric PSD cone is `B_lambda in Sym_+(m_lambda)`. The reviewed L33 scope establishes real orthogonal types for these cyclic cases. | PASS. |
| `A_lambda=sum_j Q_(lambda,j) B_lambda Q_(lambda,j)^T` | `Q_(lambda,j):R^(m_lambda)->R^(q^N)` is a `q^N x m_lambda` isometry, `j=1,...,d_lambda`; each summand and `A_lambda` are in `Sym(R^(q^N))`. | PASS. |
| `Q_j -> Q_j O`, `B -> O^T B O` | `O:R^(m_lambda)->R^(m_lambda)` is orthogonal. Both replacements preserve dimensions and give exactly the same ambient `A_lambda`. | PASS. |
| `Q_j v` vector branch | `v in R^(m_lambda)` and `Q_j v in V`. For a nontrivial H-irrep this vector lies in an H-submodule with no fixed vector. `R_G:R^(q^N)->(R^(q^N))^G` is well defined and `R_G R_H=R_G`. | PASS. |
| operator ansatz | Each `v v^T` is in `Sym_+(m_lambda)`; summing its `d_lambda` frame lifts gives an H-commutant PSD operator when weights are nonnegative. It is an operator, not yet a measure vector. | PASS. |
| `diag`, Reynolds, trace chain | `diag:Sym(R^(q^N))->R^(q^N)`; `R_G:R^(q^N)->(R^(q^N))^G`; `tr:Sym(R^(q^N))->R`; division is legal for nonzero PSD `A` because `tr A>0`. The coordinate-basis diagonal is G-equivariant under permutation conjugation. | PASS. |
| `mu_A=R_G(diag A)/tr A` | `mu_A in (R^(q^N))^G`; it is entrywise nonnegative and has scalar `l1=sum mu_A=1`. | PASS. |
| degree-zero factorial moment | On strings, and after occupancy pushforward, the order-zero row is the all-ones functional, so `M_mu(0)=sum_x mu(x)=1`. A positive pure-high-degree band would require this row to vanish. | PASS; band is zero. |
| correlation | `F:X->{-1,+1}` and `<mu,F>` is a scalar. It can exceed `2/3` without repairing the failed constant row. | PASS. |

No constituent map is silently applied to an irrep-dimensional rather than multiplicity-dimensional
space. The report's correction from full `S_N` blocks to stabilizer `S_(N-1)` blocks is essential
and correct.

### 7b — regime-complete identity gates: EXECUTED

- Multiplicity one: the residual `O(1)={+1,-1}` sign gauge leaves the operator and squared
  coordinate unchanged; it does not create the material direction ambiguity seen at higher
  multiplicity.
- Multiplicity greater than one: the exact `2 x 2` rational rotation changes coordinate squares
  `(1,0)` to `(9/25,16/25)` while the ambient operator is identical.
- Trivial versus nontrivial vector: the exact `S_3` trivial vector survives Reynolds, whereas the
  standard vector `(1,-1,0)` averages to zero.
- Positive transfer on both sides of the correlation threshold: `(4,5,0)` has correlation `49/95`
  and `(5,5,0)` has `5/7>2/3`; both have constant moment one and band zero.
- Held-out cycle types: the read-only audit covers even-`q` `tau=2` at `(4,4,0)` and odd-`q`
  `tau=1` at `(4,5,0)`.

These are identity/formula gates, not only trace-label aggregates. No LR-coefficient regime is
claimed in phase 6; the relevant multiplicity split is `m_lambda=1` versus `m_lambda>1`.

### 7c — anchoring ban: EXECUTED

The pre-report derivation is summarized in the pre-action section and archived with the fresh run.
It independently obtained the same `QO/O^TBO` formula because that formula is forced by the
Wedderburn commutant. The review adds the missing distinction that a Gelfand–Tsetlin chain resolves
the irrep factor, not the multiplicity factor.

### 7d — no frozen-input immunity: EXECUTED

The L33 review was used only for exactness of the stabilizer-commutant reduction and numerical
scope of its solver. Phase 6 newly uses its frames as cross-`N` coordinates, so that aspect was
reopened here. The prior M2 and phase-4/5 reviews were used only for their hard class definitions;
membership of the positive fallback was checked afresh. The held-out certificate residuals were
recomputed from the stored multiplicity blocks rather than accepted from JSON.

### 7e — standing failure modes: EXECUTED

- **Type mismatch:** operator blocks, multiplicity vectors, ambient vectors, diagonals, occupancy
  moments, and scalar traces/correlations were separated above.
- **Top of range/caps:** band zero was checked at the constant row; the surviving obligation was
  swept at `q=5` and `q=N` below.
- **Soft class boundary:** found MAJOR D14. Three facts do not exhaust every optimizer-derived map.
- **Tautology:** the exact reviewer imports neither proposer code nor proposer JSON. The pipeline
  reviewer reconstructs `A`, all HLS equalities, diagonal bounds, block PSD, labels, and captures
  from the archived NPZ using the reviewed common solver only.
- **Threshold:** `49/95<2/3<5/7`; neither conclusion relies on equality at `2/3`.
- **Normalization factors:** the projector character factor, group orders, trace normalization,
  coset Reynolds factor `1/N`, and `l1` were reconstructed exactly.
- **Preregistration:** all 20 proposer manifest entries match. `predictions.txt` has SHA-256
  `859edd0889e4c82beeb1270912bf7c5b786b94ca1a2b109948c4cfef3b2da8a0`; disk times place it at
  `23:05:26Z`, before labels at `23:08:55Z`, held-outs at `23:10:15Z`/`23:12:17Z`, and the manifest
  at `23:16:38Z`. The executor transcript records the prediction diff before runs. This establishes
  available disk/transcript ordering, not unknowable off-record knowledge.

### 7f — value versus formula: EXECUTED

The exact reviewer verifies the printed finite projector formula by independent construction in
`Fraction` arithmetic. It does not read the proposer output. The held-out reviewer instead reuses
the reviewed L33 construction read-only and independently reconstructs the archived numerical
certificate; it verifies feasibility and the reported structural diagnostics, but numerical
optimality still rests on stored MOSEK `optimal` status plus the completed common-solver review.
Thus the former is formula-level verification; the latter is independent certificate
reconstruction, not a new solve or exact optimality certificate.

### 7g — quantifier hygiene: EXECUTED

- **Irrep-label-only:** only the terminal H-irrep pair is shared across parameters; no basis or
  coefficient law in `M_lambda` is supplied.
- **Direct vector extraction:** lift one multiplicity vector through one irrep frame and apply the
  full-group Reynolds projector.
- **Positive diagonal transfer:** exactly `R_G(diag A)/tr A` for nonzero PSD `A`.
- **Band zero:** the order-zero factorial moment is nonzero.
- **No-refit capture:** the frozen Frobenius residual of a closed family whose parameters were fit
  only on the four training instances. No such family was defined, so this number is undefined.

“Optimizer-faithful transfer class” has no comparably complete definition; that unresolved term is
the reason the aggregate theorem remains CONJECTURED.

## Target verdicts

### T1 — gauge ambiguity

**G1 PROVED as a component; PASS on the honesty call.**

For

`V|_H = direct_sum_lambda U_lambda tensor M_lambda`,

the commutant acts on `M_lambda`, and `O(M_lambda)` changes its coordinates without changing the
ambient operator. Terminal irrep labels therefore cannot specify the optimizer's internal
direction across `N`.

A symmetric-group Gelfand–Tsetlin/Jucys–Murphy chain does not close this gap: group-algebra elements
act on `U_lambda` and as identity on `M_lambda`. The reviewed solver's seeded group-algebra element
likewise leaves every multiplicity eigenspace unresolved; LAPACK may return a reproducible
implementation basis, but that is not a representation-canonical cross-`N` gauge. A fuller ambient
branching, Schur–Weyl/tableau, intertwiner, or joint-histogram harmonic construction could supply
extra multiplicity labels. That is a live canonical-basis method and is explicitly outside G1.

The report was right not to fabricate the preregistered no-refit capture: it had no frozen
cross-`N` coefficient law, and using each held-out eigenvector is a held-out refit. Its rank-one
numbers are correctly called oracle diagnostics, not gate passes.

### T2 — Reynolds zero

**G2 PROVED as a component.** For any finite group, Reynolds is the orthogonal projection onto the
trivial isotypic component. It kills a nontrivial irreducible by Schur orthogonality. More precisely
for these H-satellites, `R_G v=R_G R_H v=0`; this covers every named nontrivial satellite even
though L33 labels H rather than G. It does not kill the trivial spine and does not apply to
quadratic/operator extraction.

### T3 — positive-transfer band zero

**G3 PROVED as a component.** The complete type chain passes, and the conclusion is uniform in
`N,q,t`: every nonzero PSD `A` gives a nonnegative unit-mass `mu_A`, so its constant factorial
moment is one and its band is zero.

The report's hard-boundary paragraphs correctly leave genuinely signed recombinations open.
However, the aggregate “therefore” is too broad unless “construction” is explicitly restricted to
the two displayed transfers. For example, centering a diagonal already produces a signed zero-mass
vector (without proving any higher band or correlation), showing why positivity of `A` alone cannot
forbid every signed use of optimizer data. This is D14, not a defect in G3.

### T4 — held-out labels, values, and metric

**PASS as NUMERICAL structure evidence.** Fresh read-only reconstruction gives:

| case | Adv± stored / requested rounding | spine Frobenius | rank-one refit oracle | full equality residual | provenance |
|---|---:|---:|---:|---:|---|
| `(4,4,0)` | `3.001212274702435` / `3.00121227470243` | 91.2028976% | 91.0099841% | `1.20e-9` | command in JSON; log SHA `052122e2...`; extractor SHA `8873e72d...`; L33 SHA `940de0ce...` |
| `(4,5,0)` | `3.077867545916693` / `3.07786754591669` | 92.0082816% | 91.7773635% | `2.78e-10` | command in JSON; log SHA `eb7b6364...`; extractor SHA `8873e72d...`; L33 SHA `940de0ce...` |

All JSON/NPZ/log/script hashes match the proposer manifest. The natural matrices reconstruct with
maximum absolute error zero, every reduced block is numerically PSD, diagonal bounds are feasible,
and the top H-family is trivial with invariance residuals `9.16e-16` and `3.31e-15`. This
independently confirms the predicted leading labels. No exact SDP certificate or optimizer
uniqueness theorem is added.

The report's comparability caveat is correct. These 91–92% figures are squared-Frobenius mass or
rank-one projection diagnostics. L1's 38.90–62.83% is `optimum/T`, an objective-value ratio for a
feasible dual family. No numerical ordering follows. The preregistration sentence calling 75%
Frobenius capture “materially” above the L1 range is therefore a MINOR metric-description defect;
the final report explicitly retracts the comparison and makes no L1-beating claim.

### T5 — exact gates, escape ledger, classification, and obligation

**Finite formulas PROVED; escape ledger PASS with one counting correction; aggregate classification
limited by D14.** Fresh code independently gives:

| case | invariance | nonnegative | `l1` | constant | correlation | band |
|---|---|---|---:|---:|---:|---:|
| `(4,5,0)` | exact | yes | 1 | 1 | `49/95` | 0 |
| `(5,5,0)` | exact | yes | 1 | 1 | `5/7` | 0 |

Membership audit of the actual positive fallback:

- **M2:** outside, decisively, because every five-condition M2 component has total mass zero while
  this measure has mass one.
- **Phase-4 T1:** outside the formula-defined unaveraged zero-total sign-bit composition; there are
  no block sign variables.
- **Phase-4 T2:** no whole-pair/value-disjoint positional allocation is present. T2 is a mechanism
  boundary rather than an intrinsic set of measures.
- **Phase-5 T2:** no identical phase-3 blocks, common exact total, or raw product tensor is present;
  again the positive measure has nonzero total.
- **D10:** not a fifth proved obstruction class. It is the open normalization escape from T1.

Thus every named membership test passes, but the report's phrase “five old obstructions” is a
MINOR counting/scope defect: the reviewed record contains four proved obstruction classes here.
M1 and phase-5 T1 are positive tools, and D10 is an open gap. Moreover, being outside the old
classes is easy for this non-dual positive measure and is not evidence of a successful escape.

The frozen BLOCKED definition is met only after narrowing the outcome to the three literal branches
proved above. It is **not** met for an undefined paradigm-level optimizer-faithful class. The
aggregate L2P6-G therefore remains CONJECTURED; the leaf stays CONJECTURED.

The surviving door is genuine and should be stated as follows:

> Construct, for every sufficiently large `N`, odd `5<=q<=N`, and target, an exact ambiently
> defined multiplicity/branching basis (including phase/order/sign conventions and a cross-`N`
> coefficient law), and a signed operator-to-measure map in that basis producing an
> `S_N x C(sigma)`-invariant unit-`l1` measure with zero constant moment, correlation at least
> `2/3+delta`, and annihilation below
> `c0 min{sqrt(N) q^eta,N^(2/3)}` for fixed `eta in (1/6,1/4]`, `c0,delta>0`.

At fixed `q=5` the target is `Theta(sqrt(N))`; at `q=N` it is capped at `N^(2/3)`. G1 does not
apply because the basis supplies more than irrep labels, G2 does not apply because the map need not
be a direct vector Reynolds extraction, and G3 does not apply because the output is genuinely
signed rather than a normalized positive diagonal. The named door is therefore not closed by
parts 1–3.

## Defects and severity

### D14 — aggregate transfer class is not formula-defined (MAJOR)

The report turns three correct facts into a candidate theorem about an “optimizer-faithful,
irrep-label-only” class without proving that the two displayed extraction maps exhaust that class.
The hard-boundary paragraph acknowledges multiple omitted maps, which saves the broad L2 route but
also prevents promoting the aggregate obstruction. Repair: state G1–G3 separately and define the
BLOCKED selected mechanism as their explicit union.

### D15 — “five old obstructions” has no fifth proved class (MINOR)

The escape ledger has four named proved obstruction classes. D10 is an open escape; M1 and
phase-5 T1 are positive lemmas. This is bookkeeping, not a failure of any membership test.

### D16 — preregistered cross-metric comparison (MINOR, final report already corrected)

Squared-Frobenius capture and L1's objective ratio are incomparable without a theorem. The report's
metric warning is the correct final interpretation.

## What I did not check

- I did not construct the canonical multiplicity/branching basis or any signed optimizer-derived
  witness.
- I did not prove an `N`-growing band, cap-scale witness, or exponent consequence.
- I did not prove an obstruction for centered diagonals, signed sector combinations, nonlinear or
  off-diagonal extractions, arbitrary equivariant maps, or general joint-histogram witnesses.
- I did not rerun MOSEK. The held-out audit reconstructs archived feasibility and relies on the
  stored solver status and completed common-solver review for numerical optimality.
- I did not produce exact/interval SDP certificates or prove optimizer uniqueness.
- I did not re-review the older M1/M2/L2P3/phase-4/phase-5 claims outside the exact class-definition
  uses stated under rule 7d.
- I did not review even-`q` asymptotic obligations; `(4,4,0)` remains structure evidence only.
- I did not use the network or make a git commit.
