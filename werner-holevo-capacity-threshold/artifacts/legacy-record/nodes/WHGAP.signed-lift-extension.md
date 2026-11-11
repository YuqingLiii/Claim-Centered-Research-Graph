---
id: "WHGAP.signed-lift-extension"
node_file: "channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.signed-lift-extension.md"
aliases: ["P2"]
kind: LEAF
role: proof
status: CERTIFIED*
status_source: "artifacts/whgap_p2_review_20260728.md (licensing statements 1-3, PROVED scope on the certificate core) applied by the decision layer 2026-07-28; execution evidence artifacts/whgap_signed_lift_extension_20260728.md"
disposition: null
parents: ["WHGAP.zero-capacity-application", "WHGAP.order-boundary"]
children: []
related: ["WHGAP.goal"]
---

# WHGAP.signed-lift-extension — Signed-lift certificate continuation past x = 1/2

## Claim

The signed-lift CP-defect certificate extends to an interval x in [1/2, x_max] with x_max > 1/2, yielding Q(Lambda_x) = P(Lambda_x) = 0 there with exact rational certificates. **[CERTIFIED\* — certificate core PROVED-licensed by R2 (region [1/2,1), unique lift, exact certificates, twirling ingredients); the "yielding Q=P=0" clause is tracked at [[WHGAP.zero-capacity-application]]]**

## Role in DAG

Second bounded sub-step of WHGAP.goal.

## Current status

CERTIFIED\* — **caveat (load-bearing, single review):** the completed fresh-session R2 review
(`artifacts/whgap_p2_review_20260728.md`, claims 1–8 PASS, claim 9 PASS as hypothesis audit)
opens the completion gate at **PROVED** tier for three separately scoped subclaims:
(1) the exact covariant-family feasible-region theorem — within the frozen five-parameter real
O(3)-equivariant adjoint-preserving ansatz, the defect Choi is PSD exactly for `1/2 <= x < 1`,
at the unique residual point `s1=2(1-x)/(3x)`, `s2=(5x-2)/(3x)`;
(2) the three solver-free exact certificates at `x = 26/51, 4/7, 3/4`;
(3) the two twirling ingredients (O(3) covariance identities incl. the det twist; congruence
convexity) — explicitly NOT a full averaging/WLOG lemma.
NOT licensed: the zero-capacity conclusion `Q=P=0 on [1/2,1)` in this node's claim wording —
its assembly through the generic Zhu–Wang/HRSF22 theorems (seven audited obligations, review
claim 9) is registered as [[WHGAP.zero-capacity-application]] and pending there. The reviewer's
independent construction used different residual coordinates and different spin bases and
reproduced the identical region and certificates.

## Dependencies

None recorded yet beyond the shared field literature in `../../../literature/` (catalog + per-paper pages; see `../../README.md`).

## Work record

- 2026-07-28 — node registered at problem-scaffold creation (rule 8); no work commissioned yet.
- 2026-07-28 — decision layer read Zhu–Wang §3.3–§4.2 + §6 from the local PDF (empty-password
  encrypted; text extracted via pypdf): Theorem 3.3 hypotheses are channel-generic (faithfulness +
  adjoint-preserving intertwining lift + CP defect), so the only x-specific work is constructing
  J_x; the paper treats x=1/2 only, no extension attempted — the gap is unclaimed. Strategy fixed:
  5-parameter real equivariant ansatz, intertwining kills 3 params (Schur sectors), 2-parameter
  residual family, defect-Choi 27×27 spin-block reduction {1,3,2,1}-multiplicities → exact
  feasibility region and x_max; twirling-WLOG ingredients (channel covariance + congruence
  convexity) make covariant infeasibility method-delimiting, not merely ansatz-delimiting.
- 2026-07-28 — commission authored by the decision layer (rule 8a, node id cited):
  [WHGAP_COMMISSION_P2_20260728.md](../../notes/WHGAP_COMMISSION_P2_20260728.md) — gates G0
  (D1–D4 exact calibration incl. recovery of the x=1/2 lift inside the residual family), G1
  (right-neighborhood feasibility), G2 (pre-registered x_max interpretations (a)/(b)/(c));
  NUMERICAL cap + pending-review; cpython3119 interpreter; 75-min budget box. Dispatched to a
  fresh codex executor session.
- 2026-07-28 — P2 executor first exact-calibration run passed D1–D4 and printed `G0 PASS`,
  including entrywise equality with the rank-3 Zhu–Wang defect Choi and exact spin-spectrum
  reconstruction, then exited nonzero during JSON serialization of symbolic principal minors.
  This logging-layer failure is retained append-only in
  [`exact_calibration.log`](../../../../artifacts/logs_whgap_p2_20260728/exact_calibration.log);
  corrected rerun pending.
- 2026-07-28 — corrected exact-calibration rerun exited 0 with `G0 PASS`: D1–D4 all passed,
  the residual family has rank-three constraints and recovers Zhu–Wang at
  `(x,s1,s2)=(1/2,2/3,1/3)`, and the exact spin multiplicities are `{0:1,1:3,2:2,3:1}`.
  Raw log: [`exact_calibration_rerun.log`](../../../../artifacts/logs_whgap_p2_20260728/exact_calibration_rerun.log);
  machine-readable blocks: [`exact_blocks.json`](../../../../artifacts/logs_whgap_p2_20260728/exact_blocks.json).
- 2026-07-28 — first feasibility run retained append-only in
  [`feasibility.log`](../../../../artifacts/logs_whgap_p2_20260728/feasibility.log): it printed
  the four decisive negative-square principal minors, then stopped on a brittle object-equality
  assertion comparing SymPy's equivalent `solve` output; corrected rerun pending.
- 2026-07-28 — second feasibility run retained append-only in
  [`feasibility_rerun.log`](../../../../artifacts/logs_whgap_p2_20260728/feasibility_rerun.log):
  it derived the unique residual point and all four reduced blocks, then stopped on another
  structural-expression comparison (`-4(x-1)…` versus `4(1-x)…`); corrected equality test pending.
- 2026-07-28 — final exact-feasibility run exited 0 with G1 and G2(a): all-principal-minor
  elimination forces `s1=2(1-x)/(3x)`, `s2=(5x-2)/(3x)` and gives the exact feasible region
  `1/2 <= x < 1`, hence `x_max=sup=1` and `x_min=1/2`. The entire commissioned rational grid
  passed above `1/2`, the lower grid failed strictly below `1/2`, and exact certificates at
  `x=26/51, 4/7, 3/4` passed PSD plus direct-27-by-27/block characteristic-spectrum checks.
  Raw log: [`feasibility_final.log`](../../../../artifacts/logs_whgap_p2_20260728/feasibility_final.log);
  certificates: [`feasibility_certificates.json`](../../../../artifacts/logs_whgap_p2_20260728/feasibility_certificates.json).
- 2026-07-28 — first twirling run retained append-only in
  [`twirling.log`](../../../../artifacts/logs_whgap_p2_20260728/twirling.log): the generic-rotation
  Groebner reduction rejected symbolic `x` as a coefficient under its default integer domain;
  rerun with the expression domain pending.
- 2026-07-28 — corrected twirling run exited 0: covariance passed for a generic rotation and
  three octahedral generators (including `det=-1`) with
  `V(O)=diag(1,det(O)O)`; three exact congruence-convexity instances and the symbolic difference
  identity passed. Raw log: [`twirling_rerun.log`](../../../../artifacts/logs_whgap_p2_20260728/twirling_rerun.log);
  data: [`twirling_checks.json`](../../../../artifacts/logs_whgap_p2_20260728/twirling_checks.json).
- 2026-07-28 — final G0 provenance rerun exited 0 after adding an independent exact
  Kraus-to-complement reconstruction and matrix-unit verification of the displayed general-`x`
  Hilbert–Schmidt adjoint. D1–D4 and G0 passed unchanged. Raw log:
  [`exact_calibration_final.log`](../../../../artifacts/logs_whgap_p2_20260728/exact_calibration_final.log).

- 2026-07-28 — paired rule-6/7 review commission authored by the decision layer (fresh-session
  reviewer, 7a–7g embedded, neutral mandate, nine enumerated claims incl. the elimination logic,
  endpoint regimes, and the generic-theorem hypothesis audit):
  [WHGAP_REVIEW_COMMISSION_R2_20260728.md](../../notes/WHGAP_REVIEW_COMMISSION_R2_20260728.md).
  It is the completion gate for this node. Dispatched to a fresh codex reviewer session.

## Evidence

- 2026-07-29 - P5 exposition-data derivation package completed (NO new mathematics; NO status
  change): [paper-grade derivation package](../../../../artifacts/whgap_p5_derivation_package_20260729.md)
  with LaTeX-ready displays, supported by
  [machine JSON](../../../../artifacts/logs_whgap_p5_20260729/derivation_package.json),
  [verification metadata](../../../../artifacts/logs_whgap_p5_20260729/verification_metadata.json),
  raw logs and [SHA-256 manifest](../../../../artifacts/logs_whgap_p5_20260729/SHA256SUMS.txt),
  and `tools/whgap_p5_derivation.py` / `tools/whgap_p5_metadata.py`. Gates V1-V5 PASS:
  the covariant pattern fits all 729 entries generally and at the forced point; the forcing
  sums, integer spin bases/Gram pencils, rank-one spectrum bookkeeping, and all three exact
  certificate spectra verify symbolically. The generic direct symbolic 27-by-27 charpoly was
  stopped at the commissioned 15-minute limit; V3 used the documented exact SO(3)-isotypic
  pencil proof plus five exact general-chart direct charpoly checks. This is exposition
  evidence for the existing R2-PROVED core only and leaves `status: CERTIFIED*` untouched.

- 2026-07-29 — P5 exposition-data commission authored by the decision layer (rule 8a; NO new
  mathematics, NO status changes — paper-grade derivation package for the R2-PROVED core,
  triggered by external paper audit #2's Major Revision verdict):
  [WHGAP_COMMISSION_P5_20260729.md](../../notes/WHGAP_COMMISSION_P5_20260729.md). Queued
  behind P3/R4 (codex sequential constraint).
- 2026-07-28 — NUMERICAL evidence tier (unreviewed executor work):
  [P2 artifact](../../../../artifacts/whgap_signed_lift_extension_20260728.md);
  [exact calibration log](../../../../artifacts/logs_whgap_p2_20260728/exact_calibration_final.log);
  [exact feasibility log](../../../../artifacts/logs_whgap_p2_20260728/feasibility_final.log);
  [twirling log](../../../../artifacts/logs_whgap_p2_20260728/twirling_rerun.log);
  [exact block data](../../../../artifacts/logs_whgap_p2_20260728/exact_blocks.json);
  [three exact certificates](../../../../artifacts/logs_whgap_p2_20260728/feasibility_certificates.json);
  [SHA-256 manifest](../../../../artifacts/logs_whgap_p2_20260728/SHA256SUMS.txt).

## Adversarial reviews

- 2026-07-28 — EXTERNAL cross-vendor hostile-referee review (ChatGPT Pro, submitted by the
  lead; fourth verification layer): **PASS — no fatal flaw found**; all five claims PASS.
  Contributions: closed-form Choi spectrum {0^19, [4(1-x)(2x-1)/x]^5, [16(1-x)(3x-1)/(9x)]^3}
  (machine-confirmed: annihilating polynomial + trace multiplicities); explicit forcing vectors
  v_p, v_d (confirmed exactly); x=1 minimal-complement self-complementarity extending the
  capacity theorem to the closed interval [1/2,1] (confirmed); Claim-4 uniqueness must stay
  scoped to the five-REAL-parameter ansatz (complex Im(r) direction unclassified — folded into
  the WLOG-lemma obligation). Archive:
  [whgap_external_review_chatgpt_20260728.md](../../../../artifacts/whgap_external_review_chatgpt_20260728.md);
  verification log
  [fable_audit_ext.log](../../../../artifacts/logs_whgap_fable_audit_20260728/fable_audit_ext.log).
- 2026-07-28 — decision-layer cross-stack audit (Fable 5, lead-commissioned; a different
  model/vendor from the executor and R2 reviewer) — ALL PARTS PASS:
  [whgap_fable_audit_20260728.md](../../../../artifacts/whgap_fable_audit_20260728.md).
  Hand re-derivation of the intertwining system and forced point; third independent
  implementation (own bases, own concave-kernel-quadratic uniqueness route); exact region grid
  incl. 1/2 ± 1e-3 bracket and the -102/1225 witness at x = 49/100; entrywise Zhu–Wang rank-3
  recovery. Additional evidence only — no status change (P2 remains CERTIFIED\* per R2).
- 2026-07-28 - fresh-session R2 rule-7 review completed:
  [WHGAP P2 independent review](../../../../artifacts/whgap_p2_review_20260728.md).
  Claims 1-8 PASS; claim 9 PASS as a hypothesis audit only. The review opens the completion
  gate at PROVED scope for the exact covariant-family feasible-region theorem, the three exact
  certificates, and the two twirling ingredients, but not for a full averaging/WLOG lemma or
  the generic-theorem zero-capacity application. Consequently it does not license the full
  current node claim as worded. No status write was made by the reviewer. Independent scripts,
  raw logs, redirected unchanged proposer reproduction, and hashes:
  [review manifest](../../../../artifacts/logs_whgap_p2_review_20260728/SHA256SUMS.txt).

## Open obligations

R2 completed and applied. Remaining beyond this node's certified scope: (1) the zero-capacity
assembly — registered as [`WHGAP.zero-capacity-application`](WHGAP.zero-capacity-application.md)
with the seven audited obligations from review claim 9; (2) optional strengthening from
CERTIFIED\* toward an unstarred tier would need a second independent stack (different CAS) or a
human check; (3) the full averaging/WLOG lemma (non-equivariant infeasibility below 1/2) remains
unwritten — only its two ingredients are PROVED-licensed.

## Status history

- 2026-07-28 — created OPEN (problem scaffold, lead directive; carried over from the same-day field-level scaffold).
- 2026-07-28 — OPEN -> NUMERICAL (proposer-writable evidence tier only): exact G0/G1/G2(a)
  runs find the defect-PSD region `1/2 <= x < 1` and exact certificates at
  `x=26/51, 4/7, 3/4`. `pending-review:` no independent rule-7 review has completed.
  Cite: `artifacts/whgap_signed_lift_extension_20260728.md`, run logs, and SHA-256 manifest.
- 2026-07-28 — NUMERICAL -> CERTIFIED\* (decision layer, applying the completed fresh-session R2
  review's licensing statements verbatim; pending-review marker removed). PROVED tier opened for
  the three scoped subclaims (feasible-region theorem on the covariant family; three exact
  certificates; twirling ingredients); the zero-capacity clause of this node's claim is NOT
  licensed and is delegated to `WHGAP.zero-capacity-application`. Cite:
  `artifacts/whgap_p2_review_20260728.md` (Licensing statements 1–4) and
  `artifacts/logs_whgap_p2_review_20260728/SHA256SUMS.txt`.

## Lean

```yaml
lean:
  module: "WHGAP.«signed-lift-extension»"
  file: "channel-capacity/werner-holevo-gap/proof-dag/lean/WHGAP/signed-lift-extension.lean"
  claim: "Claim"
  composition: null  # leaf
  state: "stated"
  tier: "T2 (algebraic core proved) / T1 (Claim stated)"
  rel: []
  build: "artifacts/logs_whgap_lean3_20260801/"  # LEAN-3/3.2 batch; earlier evidence dirs retained
  claim_hash: "sha256:6283cddf584e71b7bad87ca1c9dd0a836c1b3e19242ea882fe1e560d149cf757"
  synced: "2026-08-01 (post LEAN-3.2, R13 m2)"
```

Mechanization notes (LEAN-1, 2026-07-30, NUMERICAL `pending-review:` — the §7.10
statement-fidelity review is the completion gate): Claim stated (certificate availability on [1/2,1)); the displayed algebraic core is PROVED outright (forcing_p, forcing_d, both defect-eigenvalue sign branches) — SignedLiftCP itself is opaque.
Report: [whgap_lean_t1t2_20260730.md](../../../../artifacts/whgap_lean_t1t2_20260730.md)
(G-L5 fidelity self-table row for this node; granularity losses stated there).

