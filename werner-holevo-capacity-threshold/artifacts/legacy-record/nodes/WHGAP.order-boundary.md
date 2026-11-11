---
id: "WHGAP.order-boundary"
node_file: "channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.order-boundary.md"
aliases: ["P6"]
kind: AND
role: proof
status: PROVED
status_source: "R5b review 2026-07-29 (artifacts/whgap_r5b_review_20260729.md, LICENSE A: necessity theorem PROVED) + P2 for the holding side; applied by the decision layer 2026-07-29; numerical scan scoped per R5a (artifacts/whgap_r5a_review_20260729.md, FINDINGS); edge-normalized 2026-07-30 (kind LEAF -> AND, child P2; parent link to goal moved to related — the order boundary does not propagate to the Q-determination)"
disposition: null
parents: []
children: ["WHGAP.signed-lift-extension"]
related: ["WHGAP.goal", "WHGAP.relaxed-lift", "WHGAP.qpositive-onset", "WHGAP.private-boundary"]
---

# WHGAP.order-boundary — Where does the complete-BKM order break below 1/2?

## Claim

Determine the boundary x_B of the set {x : Lambda_x^c dominates Lambda_x in the complete
Bogoliubov–Kubo–Mori (cBKM) sense} within the strip (x_1, 1/2), where
x_1 = 0.390910... is the P3 max-mixed crossing. **[PROVED — ANSWERED: x_B = 1/2 exactly.
Domination FAILS for every x in (0, 1/2) (lead's analytic BKM-necessity witness; paper §5;
R5b review) and HOLDS on [1/2, 1) (P2/P4 signed lift). The cBKM and cRE domination sets both
equal [1/2, 1).]**

## Role in DAG

Decision-layer brainstorm 2026-07-29 (lead question: "is the signed-lift condition optimal?").
Framing: the ZW certificate chain passes through cBKM ⟹ cRE ⟹ complete-less-noisy ⟹
(tensorization) Q=P=0. Since Q > 0 on (0, x_1) (P3, PROVED scope), the cBKM order MUST fail
there; since our lift certifies it on [1/2, 1), it HOLDS there. If it breaks exactly at 1/2,
the signed-lift mechanism already captures the order's full reach on this family ("optimal in
effect"); if it survives on some (x_B, 1/2), that strip is certified terrain for STRICTLY
WEAKER certificates (see [[WHGAP.relaxed-lift]]), and Q = P = 0 would extend below 1/2 —
a result beyond Zhu–Wang's mechanism.

## Current status

PROVED (2026-07-29, decision layer applying the completed R5b review). The boundary question
is ANSWERED analytically: x_B = 1/2 exactly. The lead's witness pair
(rho_eps = diag(1-2eps, eps, eps), X = (E12+E21)/sqrt2) violates trivial-reference BKM
domination at every x < 1/2 with the explicit finite-eps threshold
eps_c(x) = 2(1-2x)/(2-3x) (R5b re-derived symbolically over all real x in (0,1/2) plus 11
exact rational instances); since cRE => trivial-reference BKM (second-order Hessian lemma,
paper §5) and cBKM => cRE, both complete orders FAIL on (0, 1/2); they HOLD on [1/2, 1) by
the P2/P4 signed lift. The P6 numerical scan survives as corroboration at the R5a-repaired
scope (below).

R5a-repaired scope for the numerical record (verbatim from
artifacts/whgap_r5a_review_20260729.md §10, adopted by the decision layer): cBKM-order
violation is independently confirmed at the eight displayed rational d_R = 1 grid points
7/20 ... 499/1000; P6's directed-interval bounds are semi-rigorous and stated to spurious
precision (R5a MAJOR-2), but R5a's independent exact-rational recomputation at 60/120/240
digits confirms strict negativity at 7/20, 12/25 and 499/1000 by two structurally
independent implementations. The four bisection points (999/2000 ... 7999/16000) are
double-precision search classifications only — NUMERICAL, not certified. The no-violation
side at x >= 1/2 is bounded-search evidence with effective resolution ~1e-7 (exact zero mode
Z ∝ sigma makes the -1e-9 floor sit inside the noise band); R5a's own high-precision
arbitration finds the true minimum at 11/20 and 1/2 to be exactly 0. The d_R >= 2 columns of
the E1 table are NOT evidence (R5a MAJOR-3: the embedding identity
g_{rho⊗theta}(P_r⊗Y) = p^{-1} g_theta(Y) shows the scan missed constructible witnesses by
ten orders of magnitude; root cause effective_steps = 2/0 for d_R = 2/3).

Key computational handle (decision layer): for faithful theta with spectrum
{lambda_i}, the BKM form is g_theta(Z) = sum_ij |Z_ij|^2 c(lambda_i, lambda_j) in theta's
eigenbasis, c(a,b) = log(a/b)/(a-b), c(a,a) = 1/a. So cBKM violation at reference R and
faithful sigma_RA is ONE generalized-eigenvalue test: T_N - T_M has a negative eigenvalue,
where T_N = (id_R⊗N)† Γ_{ω}^{-1} (id_R⊗N), ω = (id⊗N)(σ) (similarly T_M) — a
9 d_R^2-dimensional Hermitian eigenproblem per (x, sigma). Violations rationalize to
interval-certified witnesses (P3-style).

## Composition proof

```yaml
composition:
  claim: >
    (in-node necessity theorem, R5b-PROVED) the witness pair
    (rho_eps = diag(1-2eps, eps, eps), X = (E12+E21)/sqrt2) violates trivial-reference
    BKM domination strictly for every x in (0, 1/2) and 0 < eps < eps_c(x) =
    2(1-2x)/(2-3x); since cRE implies trivial-reference BKM (second-order Hessian
    lemma) and cBKM implies cRE, both complete orders FAIL on (0, 1/2);
    AND (P2, R2-PROVED-scope subclaim + ZW Thm 3.3 interface) the signed lift J_x has
    CP defect on [1/2, 1), so cBKM (hence cRE) HOLDS there.
    Therefore the cBKM and cRE domination sets both equal [1/2, 1): x_B = 1/2 exactly.
  proof: "paper/main.tex section 5 (Lemma lem:re-to-bkm, Theorem thm:necessity, Corollary cor:phase); in-node Evidence entries of 2026-07-29"
  review: "artifacts/whgap_r5b_review_20260729.md (LICENSE A; necessity PROVED, phase corollary PROVED given the P2/ZW holding side)"
  status: PROVED
  rel:
    - "consumes the R2-PROVED-scope region subclaim of P2 + the ZW Thm 3.3 interface for
       the holding side (same scoped-input note as on WHGAP.zero-capacity-application)"
    - "the P6 numerical scan is corroboration only, at the R5a-repaired scope (its three
       MAJORs recorded in Adversarial reviews); no part of the theorem rests on it"
```

## Dependencies

- P2 (the certificate side: cBKM holds on [1/2,1)); P3 (Q>0 on (0,x_1) forces violation
  there — calibration anchor for the scanner at e.g. x = 0.35).
- HRSF22 local PDF (order definitions; Lemma 2.1: classical references don't help — quantum
  R essential).

## Work record

- 2026-07-29 — node registered (rule 8b) at brainstorm time; commission
  [WHGAP_COMMISSION_P6_20260729.md](../../notes/WHGAP_COMMISSION_P6_20260729.md) authored the
  same day (E1 scan; gates pre-registered).
- 2026-07-29 - P6 E1 completed: 4,500 calibrated Cholesky restarts over d_R=1,2,3;
  G0a/G0b PASS; eight rational d_R=1 witnesses have negative 80-digit directed-interval
  upper bounds; warm bisection bracket [7999/16000,1/2]. Full record:
  [P6 artifact](../../../../artifacts/whgap_p6_relaxation_20260729.md), machine results and
  raw logs under `artifacts/logs_whgap_p6_20260729/`.

## Evidence

- 2026-07-29 - `NUMERICAL`, `pending-review:` P6 artifact
  [whgap_p6_relaxation_20260729.md](../../../../artifacts/whgap_p6_relaxation_20260729.md);
  exact machine record
  [e1_scan.json](../../../../artifacts/logs_whgap_p6_20260729/e1_scan.json) and
  [e1_certificates.json](../../../../artifacts/logs_whgap_p6_20260729/e1_certificates.json);
  provenance [SHA256SUMS.txt](../../../../artifacts/logs_whgap_p6_20260729/SHA256SUMS.txt).
  Licensed scope is numerical only: certified violations on the displayed rational grid
  and bounded-search no-violation evidence at/above 1/2.

- 2026-07-29 (late) — LEAD-SUPPLIED ANALYTIC NECESSITY WITNESS, decision-layer hand-verified:
  rho_eps = diag(1-2eps, eps, eps), X = (E12+E21)/sqrt2 (symmetric traceless, spin-2).
  Lambda(X) = (1-3x/2)X; the {1,2}-block common eigenvalue of Lambda(rho_eps) is
  b_eps = x/2 + (1-3x/2)eps, so g_B = (1-3x/2)^2/b_eps. For symmetric X the complement
  cross-block vanishes: Lambda^c(X) = 0 (+) (-x/2 X), with environment block eigenvalue
  e_eps = (x/2)(1-eps), so g_E = x/(2(1-eps)). Since (plain) RE domination forces BKM
  domination by the second-order expansion (Hessian of D), cRE requires g_E >= g_B; the
  eps->0 limit gives x/2 - (2/x)(1-3x/2)^2 = 2(1-x)(2x-1)/x >= 0, i.e. **x >= 1/2 is
  NECESSARY for Lambda^c >= Lambda in cRE/cBKM** — matching the P6 numerical bracket and
  explaining lambda_5 (the gap equals lambda_5/2; X lives in the spin-2 sector). Upgrade
  path: exact verification (P6b) + written lemma + review => the iff classification
  cBKM <=> cRE <=> signed-lift-certificate <=> x in [1/2, 1] on this family.

- 2026-07-29 (late) — exact-verification commission authored (rule 8a):
  [WHGAP_COMMISSION_P6B_20260729.md](../../notes/WHGAP_COMMISSION_P6B_20260729.md) — V1 the
  lead's witness chain incl. a finite-eps strict violation family and the lambda_5/2
  bookkeeping; V2 the isotropic D_psi(x) closed form and its exact threshold. Dispatched.

- 2026-07-29 (night) — P6b COMPLETED with the decision layer as hands-on executor (the
  commissioned Opus executor died twice on 529 overload and once on the session usage limit
  mid-repair; running the scripts consumes no LLM quota; the review gate is unchanged).
  **V1 PASS end to end** (both scripts exit 0): the lead's witness chain, the finite-eps
  strict violation family at every tested rational x < 1/2, and the lambda_5/2 bookkeeping
  are now EXACTLY verified. **V2 PASS after supersession:** the interrupted executor's
  v2_isotropic.py was defective in its own D/basis assembly (its d_1 = 1-x is impossible —
  it would put an ascent at proved-zero x); independent numeric arbitration confirmed the
  P9b values, and the replacement `tools/whgap_p6b_v2_fable.py` passes all six gates with
  the exact closed forms d_0 = -x(1-x)/(2-x), **d_1 = (1-x)(2-5x)/(2-x)**, d_2 = 0 —
  sign rule: d_1 > 0 iff x < 2/5. Artifact:
  [whgap_p6b_necessity_20260729.md](../../../../artifacts/whgap_p6b_necessity_20260729.md);
  logs + SHA256SUMS under `artifacts/logs_whgap_p6b_20260729/`. Consequence recorded at
  CONJECTURED tier on [[WHGAP.no-ascent-hierarchy]]: candidate exact single-letter onset
  x_D = 2/5 (would shrink the strip to [2/5, 1/2)); rests on the not-yet-reviewed N1'
  expansion lemma.

## Adversarial reviews

- 2026-07-29 — **R5a (fresh Opus instance, rule-7 complete): FINDINGS — 3 MAJOR + 8 minor**
  on the P6 numerical scan; the substantive negativity result stands (independently
  reproduced at 7/20, 12/25, 499/1000 from the exact rationals, two structurally
  independent BKM implementations, margins >= 1e7 x error). MAJOR-1: the four bisection
  points were never certified (double-precision classifications only) — the artifact's
  "Only the lower endpoint is a certified violation" is inverted. MAJOR-2: certify() routes
  rationals through float64+str(), so the recorded 80-digit intervals do NOT enclose the
  recorded rational objects; digits past ~13 are spurious. MAJOR-3: the d_R >= 2 scan
  columns carry no evidential weight (embedding identity shows missed witnesses by 10
  orders; script bug effective_steps = 2/0). Minors include: the -1e-9 no-violation floor
  sits inside the double-precision noise band (exact zero mode Z ∝ sigma; effective
  resolution ~1e-7); bracket phrasing presupposes unproved monotonicity in x; P6's
  SHA256SUMS.txt is CRLF (standing failure mode). Report:
  [whgap_r5a_review_20260729.md](../../../../artifacts/whgap_r5a_review_20260729.md);
  reviewer scripts/logs under `artifacts/logs_whgap_r5_20260729/`. Repaired scope adopted
  in Current status above; no completion tier opened by this review alone.
- 2026-07-29 — **R5b (fresh Opus instance, rule-7 complete): LICENSE A — the necessity
  chain is PROVED; NO MAJOR, 8 minors** (all paper-side wording/typing repairs). Reviewer
  rebuilt everything in an own script (57 gates, exit 0) from frozen conventions before
  reading authored code: witness computed in two basis orders; BKM form by two independent
  routes (divided differences + integral representation, < 1e-45 agreement); gap identity
  and sign; own finite-eps threshold eps_c(x) = 2(1-2x)/(2-3x) with exact rational strict
  violations at 11 rational x < 1/2 and symbolic coverage of all real x in (0, 1/2); the
  RE->BKM Hessian claim verified at seven configurations including a degenerate spectrum;
  the 27x27 defect Choi rebuilt from scratch at two x (spectrum 0^19, lambda_5^5,
  lambda_3^3 confirmed independently of the frozen theorem). Licensed verbatim: "necessity
  theorem PROVED (x >= 1/2 necessary for cRE, already with trivial reference, hence for
  cBKM); phase-classification corollary PROVED given frozen P2/P4". Noted scope limits:
  standard RE second-order expansion granted at VALUE level pending a literature cite;
  Remark rem:obstruction's structural reading NOT licensed; nothing licensed about Q below
  1/2 (that lives in P9/P3). Also caught: the R5 commission menu's "necessary for cBKM,
  hence for cRE" inverts the implication — the paper's direction is the licensed one.
  Report: [whgap_r5b_review_20260729.md](../../../../artifacts/whgap_r5b_review_20260729.md).
  Minors m1-m8 (faithfulness hypothesis in the lemma; display eps_c(x); degenerate-pair
  coupling note; number the cRE/cBKM definitions; cite the BKM-Hessian literature; soften
  the remark + state ||X||_HS = 1; verification-statement scope; 4/7 numerical caveat in
  the phase table) are owed to paper v4.

## Open obligations

Paper v4 must incorporate the R5b minors m1-m8. The P6 numerical artifact's over-claims
(MAJOR-1/2 wordings) are superseded by the R5a-repaired scope recorded above — the artifact
itself stays append-only. Optional (not commissioned): re-certify the four bisection points
with exact-rational pipelines; moot for the boundary question, which is now PROVED.

## Status history

- 2026-07-29 — created OPEN (decision-layer registration during the relaxation brainstorm).
- 2026-07-29 - OPEN -> NUMERICAL (`pending-review:`), proposer-authored P6 execution with
  command/log/script-hash provenance; no completion-tier claim.
- 2026-07-29 — NUMERICAL -> PROVED (decision layer, applying the completed R5b review's
  licensing statement verbatim + P2/P4 for the holding side; pending-review marker
  removed). x_B = 1/2 exactly; the cBKM/cRE domination sets equal [1/2, 1). The numerical
  scan record is re-scoped per R5a (FINDINGS; its three MAJORs recorded append-only above).

## Lean

```yaml
lean:
  module: "WHGAP.«order-boundary»"
  file: "channel-capacity/werner-holevo-gap/proof-dag/lean/WHGAP/order-boundary.lean"
  claim: "Claim"
  composition: "composition"
  state: "composition-checked"
  tier: "T2 (scalar core) / T1 (composition)"
  rel: ["hHolds (ZW certificate side)", "hFails (R5b necessity side)"]
  build: "artifacts/logs_whgap_lean3_20260801/"  # WP-F added the gB/gE/gE_lt_gB scalar layer
  claim_hash: "sha256:db0301276dd9cb7382a3553ab2cfc717a47cf104462987ecc912f6c64c69e611"
  synced: "2026-08-01 (post LEAN-3 WP-F, R13 m2)"
```

Mechanization notes (LEAN-1, 2026-07-30, NUMERICAL `pending-review:` — the §7.10
statement-fidelity review is the completion gate): scalar core PROVED outright (gap_identity, threshold_factorization, strict_violation_window at the exact eps_c(x)); cBKM is an abstract predicate — both order directions are explicit hypotheses.
Report: [whgap_lean_t1t2_20260730.md](../../../../artifacts/whgap_lean_t1t2_20260730.md)
(G-L5 fidelity self-table row for this node; granularity losses stated there).

