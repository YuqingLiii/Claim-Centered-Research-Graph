---
id: "WHGAP.qpositive-onset"
node_file: "channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.qpositive-onset.md"
aliases: ["P3"]
kind: AND
role: proof
status: CERTIFIED*
status_source: "artifacts/whgap_p3_review_20260729.md (R4) + artifacts/whgap_r5d_review_20260729.md (R5d LICENSE A: Theorem Q>0 on (0,2/5) PROVED, notes/WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md) applied by the decision layer 2026-07-30; edge-normalized 2026-07-30 (kind LEAF -> AND, child P9) with the composition block below"
disposition: null
parents: ["WHGAP.goal"]
children: ["WHGAP.no-ascent-hierarchy"]
related: ["WHGAP.onset-two-fifths"]
---

# WHGAP.qpositive-onset — Small-x onset of positive quantum capacity

## Claim

Determine the small-x threshold below which Q(Lambda_x) > 0 (value or bounds for the onset of
positive quantum capacity in the noisy Werner–Holevo family). **[CERTIFIED\* — best PROVED
bound now: Q(Lambda_x) > 0 for ALL x in (0, 2/5) (R5d-reviewed Theorem 8.1 of the N1'
expansion-lemma note, 2026-07-30), subsuming the R4-reviewed (0, x_1) package and the
783/2000 witness. The undetermined strip is exactly [2/5, 1/2); the exact onset value
remains OPEN — see [[WHGAP.onset-two-fifths]].]**

## Role in DAG

Third contributory sub-step of WHGAP.goal, registered per rule 8b when the 2026-07-28 propagation
adjudication on `WHGAP.goal` exposed a decomposition gap: P1 settles the antidegradable side and P2
targets certificates below x*, but no node carried the Q > 0 onset that bounds the zero-capacity
set from the small-x side. Without it the goal decomposition cannot close even with P1 and P2
PROVED.

## Current status

CERTIFIED\* — **caveat (load-bearing, single review):** the completed fresh-session R4 review
(`artifacts/whgap_p3_review_20260729.md`; PASS, two MINORs, no MAJOR/GAP) opens:
**PROVED tier (licensing statement 1)** for the exact package — D1 closed form; D2
monotonicity/uniqueness with the review-corrected display value `Ic(pi,3/4) = log2(3) - 2`
(the artifact's `-1/4` is wrong; argument unaffected); the width-`1e-31` certified bracket for
`x_1 = 0.390910232076181323482721853134...`; the three D4 interval certificates; hence
**`Q(Lambda_x) > 0` for every x in (0, x_1)**; plus the exact rank-two G2(b) witness at
`x = 783/2000 > x_1` with existence (not endpoints) of a positive continuity neighborhood.
**CERTIFIED\* tier (statement 2)** for the numerical package — the S1 best-found ceiling
picture above x_1 (explicitly NOT an upper bound on the all-input supremum) and the bounded S3
two-letter null. NOT licensed: the exact onset value/boundary — the strip between the
783/2000-neighborhood and 1/2 remains OPEN. Also on record: `x_H = 0.4162325706...` (pi's
local-maximality threshold, distinct from x_1 by ≈ 0.0253).

## Dependencies

None recorded yet beyond the shared field literature in `../../../literature/` (catalog +
per-paper pages; see `../../README.md`). Literature lead (2026-07-28, from the Zhu–Wang
bibliography): [RK25] Roofeh–Karimipour, "Capacities of a two-parameter family of noisy
Werner–Holevo channels", Quantum Inf. Process. 24:226 (2025) — likely carries
coherent-information lower bounds for this family; fetch before commissioning this node.

## Work record

- 2026-07-28 — node registered per rule 8b at goal-adjudication time (decision layer); no work
  commissioned. See the same-date adjudication entry in
  [WHGAP.goal](WHGAP.goal.md).
- 2026-07-29 — literature-first (decision layer): RK24 (arXiv:2310.15353) and RK25
  (arXiv:2405.11216) fetched, ingested into the field library (catalog entries + README pages),
  and read. Key baseline (RK24 §5.4): their single-letter optimization finds the maximally
  mixed input optimal for x below ~0.38 and best lower bound exactly 0 (pure states) above —
  i.e. no single-letter Q>0 witness beyond the max-mixed crossing x_1 ≈ 0.3915 (root of
  Ic(pi) = log2 3 + (1-x)log2(1-x) + x log2(x/3)). Combined with our [1/2,1] theorem the
  genuinely open strip is (x_1, 1/2). RK25 adds higher-d context (port targets), nothing
  sharper on the d=3 line.
- 2026-07-29 — commission authored by the decision layer (rule 8a, node id cited):
  [WHGAP_COMMISSION_P3_20260729.md](../../notes/WHGAP_COMMISSION_P3_20260729.md) — G0 exact
  calibration (closed-form Ic(pi), monotonicity lemma, 1e-30 certified root bracket, three
  interval certificates), S1 full-input single-letter ceiling scan with pre-registered
  RK24-claim test, S2 Hessian-at-pi threshold comparison, S3 time-boxed two-letter probe;
  NUMERICAL cap + pending-review; cpython3119; 75-min budget. Dispatched to a fresh codex
  executor session.
- 2026-07-29 — paired rule-6/7 review commission R4 pre-authored by the decision layer
  (fresh-session reviewer, 7a–7g embedded, neutral mandate, runs only after the execution
  artifact lands; log-base slips and silent input-space restriction named as standing risks):
  [WHGAP_REVIEW_COMMISSION_R4_20260729.md](../../notes/WHGAP_REVIEW_COMMISSION_R4_20260729.md).
  It is the completion gate for this node.

- 2026-07-29 — P3 executor completed the commission:
  [whgap_p3_qonset_20260729.md](../../../../artifacts/whgap_p3_qonset_20260729.md). G0 passed
  with a `1e-31` directed-rounding bracket for `x_1` and three rational interval positivity
  certificates. S1 completed 200 full-input restarts at each of ten grid points and triggered
  pre-registered G2(b): a rational rank-two input at `x=783/2000>x_1` has exact
  input/output/environment spectra and a positive interval lower bound
  `1449965437710479183/5000000000000000000000000` bits. S2 established analytic two-sector
  Hessian formulas and located the unique first sign change at `x_H>x_1`. S3 completed 50
  full-parameter restarts plus diagonal/correlated probes at each requested point in 757.297 s,
  with all values below the `1e-7` MAJOR threshold. Raw logs and JSON:
  `artifacts/logs_whgap_p3_20260729/`; script/log digests:
  `artifacts/logs_whgap_p3_20260729/SHA256SUMS.txt`.

## Evidence

- 2026-07-29 — execution artifact:
  [whgap_p3_qonset_20260729.md](../../../../artifacts/whgap_p3_qonset_20260729.md), supported by
  `tools/whgap_p3_calibration.py`, `tools/whgap_p3_single_letter.py`,
  `tools/whgap_p3_hessian.py`, `tools/whgap_p3_interval_candidate.py`, and
  `tools/whgap_p3_two_letter.py`; raw logs/JSON and `SHA256SUMS.txt` are under
  `artifacts/logs_whgap_p3_20260729/`. Evidence tier: NUMERICAL. **pending-review:** exact
  arithmetic portions await independent rule-7 review; optimizer searches are numerical-only.
- 2026-07-29 — **bookkeeping note (decision layer):** the executor cited
  `SHA256SUMS.txt` here and in the artifact but did not write the file; the manifest was
  generated post-hoc by the decision layer over the executor's untouched outputs (19 entries:
  all logs, JSON, artifact, five scripts). Flagged for the R4 reviewer as a
  closeout-discipline defect of the execution run.

- 2026-07-29 — executor closeout continuation: after the concurrent 19-entry manifest note above,
  the executor completed both required validators and the scoped whitespace check, regenerated
  `SHA256SUMS.txt` over the final artifact, all five scripts, and every log/JSON in the P3 log
  directory, and independently verified all 23 entries. The earlier timing note remains as
  append-only history; the final manifest is complete for the delivered scope.

## Composition proof

```yaml
composition:
  claim: >
    (P9, reviewed-subset subclaims) the isotropic eps-log(1/eps) expansion Lemma 5.1
    (with explicit remainder C(x), uniform in phi and psi; R5d LICENSE A) and the
    definition-level value w_B - w_E = d_1(x) = (1-x)(2-5x)/(2-x) at phi = P_psibar
    (derived inside the lemma note section 7.3, independently of the R5c closed form),
    together with the Lloyd-Shor-Devetak interface Q >= Q^(1), imply
    Q(Lambda_x) >= Q^(1)(Lambda_x) > 0 for every x in (0, 2/5).
  proof: "Theorem 8.1 of channel-capacity/werner-holevo-gap/notes/WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md (explicit witness threshold eps_1(x) = min(x/8, exp(-C(x)/d_1(x)))); written form: paper/main.tex section 6"
  review: "artifacts/whgap_r5d_review_20260729.md (LICENSE A, unconditional: the theorem imports nothing beyond the note's own sections)"
  status: PROVED
  rel:
    - "consumes ONLY the R5c/R5d-reviewed PROVED-scope subset of P9 (Lemma 5.1 + the
       section-7.3 value); P9's node-level CERTIFIED* star marks its BROADER hierarchy
       claim (n >= 2, tau != 0 strata, balanced layer), none of which is used here"
    - "LSD/Devetak regularization is a cited interface, not re-proved"
```

Status arithmetic: the imported theorem is PROVED (composition PROVED [R5d] on the
PROVED-scope subset of P9). The NODE stays CERTIFIED\* because its own Claim is the full
onset determination, of which the exact onset value remains OPEN (see
[[WHGAP.onset-two-fifths]]) — the star marks the node's residual scope, not the imported
theorem. The older R4 route (exact package for (0, x_1) + the 783/2000 witness) remains
below as in-node evidence: it is SUBSUMED by the P9 route for the interval statement but
stays the source of the sharper numerical onset picture (x_1, x_H) and the two-letter
probe.

## Evidence (continued — 2026-07-30 import from the R5 batch)

- 2026-07-30 — **Q(Lambda_x) > 0 for every x in (0, 2/5) is PROVED** (decision layer
  applying the completed R5d review verbatim): Theorem 8.1 of
  [WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md](../../notes/WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md)
  (E-N1 authored, fresh-instance R5d review
  [whgap_r5d_review_20260729.md](../../../../artifacts/whgap_r5d_review_20260729.md)
  LICENSE A, no MAJOR, unconditional). One witness family does the whole interval:
  rho_eps = (1-eps)P_psi + eps P_psibar at the isotropic psi = (e1 + i e2)/sqrt2, with
  Ic(rho_eps) = d_1(x) eps log(1/eps) + O(eps), d_1 = (1-x)(2-5x)/(2-x) > 0 iff x < 2/5,
  and the explicit threshold eps_1(x) = min(x/8, exp(-C(x)/d_1(x))). This SUBSUMES the R4
  package's (0, x_1) and the 783/2000 witness (2/5 > 783/2000 > x_1); the R4 record below
  remains the source of the sharper numerical onset picture (x_1, x_H) and the two-letter
  probe. Practical warning from Prop 9.1 (R5d-verified): near 2/5 the positive sign only
  appears below the crossover eps* = exp(c_1/d_1) (~1.8e-8 at x = 0.395, collapsing doubly
  exponentially toward 2/5) — numerical Ic searches stopping at eps ~ 1e-5 report the
  wrong sign, which is why the S1 scans missed this ridge.

## Adversarial reviews

- 2026-07-29 — fresh-session R4 independent review:
  [whgap_p3_review_20260729.md](../../../../artifacts/whgap_p3_review_20260729.md).
  Claims 1-9 were adjudicated with the full rule-7a-g checklist; the exact rational G2(b)
  witness and exact `(0,x_1)` package passed, with MINOR findings for the artifact's false
  supporting equality `I_c(pi,3/4)=-1/4`, empirical "ceiling" terminology, and the post-hoc
  manifest bookkeeping count. Reviewer scripts, redirected reproductions, raw logs, and hashes:
  `artifacts/logs_whgap_p3_review_20260729/`. The report supplies scoped licensing statements;
  this reviewer made no node-status write.

## Open obligations

R4 and the R5-batch import completed and applied. Item (3) of the earlier list — the
`epsilon -> 0` expansion idea — has been EXECUTED and reviewed (it became the N1' lemma
route; see the 2026-07-30 Evidence entry). Remaining open: (1) the strip [2/5, 1/2) —
undetermined at every blocklength (the S3 null is bounded, not a theorem); (2) whether
2/5 is the exact single-letter onset — registered separately as
[[WHGAP.onset-two-fifths]] (rule 8b) with its four named obligations.

## Status history

- 2026-07-29 — OPEN -> NUMERICAL after the commissioned G0/S1/S2/S3 execution and G2(b)
  exact-interval witness at `x=783/2000`; proposer-authored, with explicit `pending-review:`.
- 2026-07-29 — NUMERICAL -> CERTIFIED\* (decision layer, applying the completed fresh-session
  R4 review's licensing statements verbatim; pending-review marker removed). PROVED tier opened
  for the exact package (incl. `Q>0` on `(0, x_1)` and the `783/2000` witness); CERTIFIED\*
  tier for the numerical S1/S3 package; exact onset boundary NOT licensed, stays open. Cite:
  `artifacts/whgap_p3_review_20260729.md` (licensing statements 1-2) and
  `artifacts/logs_whgap_p3_review_20260729/SHA256SUMS.txt`.

- 2026-07-28 — created OPEN (decision-layer registration per rule 8b during the WHGAP.goal
  propagation adjudication).
- 2026-07-30 — CERTIFIED\* scope upgraded (decision layer, applying the completed R5d
  review verbatim): PROVED tier now covers Q > 0 on ALL of (0, 2/5) via the N1' expansion
  lemma Theorem 8.1, subsuming the R4 (0, x_1) package. Undetermined strip = [2/5, 1/2).

## Lean

```yaml
lean:
  module: "WHGAP.«qpositive-onset»"
  file: "channel-capacity/werner-holevo-gap/proof-dag/lean/WHGAP/qpositive-onset.lean"
  claim: "Claim"
  composition: "composition"
  state: "composition-checked"
  tier: "T1"
  rel: []
  build: "artifacts/logs_whgap_lean_20260730/"
  claim_hash: "sha256:a3f1e418592cbfeb858ffb340b5c60cbc99bda247642ae2b77e9cbfa63568cfa"
  synced: "2026-07-30"
```

Mechanization notes (LEAN-1, 2026-07-30, NUMERICAL `pending-review:` — the §7.10
statement-fidelity review is the completion gate): composition (P9 ⟹ P3) checked against the interface q_pos field; only the PROVED interval content is stated.
Report: [whgap_lean_t1t2_20260730.md](../../../../artifacts/whgap_lean_t1t2_20260730.md)
(G-L5 fidelity self-table row for this node; granularity losses stated there).

