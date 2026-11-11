---
id: "WHGAP.antideg-boundary"
node_file: "channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.antideg-boundary.md"
aliases: ["P1"]
kind: LEAF
role: proof
status: CERTIFIED*
status_source: "artifacts/whgap_p1_review_20260728.md (licensing statement) applied by the decision layer 2026-07-28; execution evidence artifacts/whgap_antideg_boundary_20260728.md"
disposition: null
parents: []
children: []
related: ["WHGAP.goal"]
---

# WHGAP.antideg-boundary — Exact antidegradability boundary x*

## Claim

Compute the exact antidegradability boundary x* of Lambda_x via the symmetric-extension SDP characterization (Myhr–Lutkenhaus), and decide whether x* < 4/7. **[CERTIFIED\* — narrow scope: only "4/7 numerically tight (1e-6)" is licensed; exact boundary = GAP; see caveat]**

## Role in DAG

First bounded sub-step of WHGAP.goal; deterministic outcome (SDP feasibility scan + rationalization).

## Current status

CERTIFIED\* — **caveat (load-bearing, single review):** the licensed statement is ONLY
**"4/7 is numerically tight under the pre-registered 1e-6 meaning"**, resting on the reviewer's
OWN independent implementation of the frozen swap-invariant SDP (18+9 blocks AND full 27×27,
agreeing) with operational support-margin bracket `[0.5714285629136222, 4/7]` (width 8.51e-9).
NOT licensed: the exact boundary value (GAP — no exact primal/dual certificate on either side),
the proposer's displayed `t*(x)` table and solver-sign bracket (**MAJOR** — the run-2 script
restricted `eta` to the 18-dim bosonic sector `A⊗Sym²(B)`, a strictly stronger criterion than the
frozen 18+9 swap-invariant one; e.g. correct `t*(1/2) = -4.6296e-4 ≈ -1/2160` vs the displayed
`-6.9444e-4 ≈ -1/1440`), and any monotone/unique-boundary quantifier (undefined in scope).
Structural fact found by the review: on the frozen full SDP, `t*(x) <= 0` identically (omega_x has
a 5-dim kernel), so raw-sign bisection is ill-posed; the meaningful margin lives on
`supp(omega_x) ⊗ B2`. Eight untested regimes listed in the review cap the tier at CERTIFIED\*.
C1–C5 PASS independently; C6 mathematical claims PASS (independent exact congruence, rank 24)
with MINOR on the run-2 script's unproved spin-block recoupling linkage.

## Dependencies

None recorded yet beyond the shared field literature in `../../../literature/` (catalog + per-paper pages; see `../../README.md`).

## Work record

- 2026-07-28 — node registered at problem-scaffold creation (rule 8); no work commissioned yet.
- 2026-07-28 — commission prompt authored by the decision layer (rule 8a, node id cited):
  [WHGAP_COMMISSION_P1_20260728.md](../../notes/WHGAP_COMMISSION_P1_20260728.md) — calibration gate
  G0 (six exact Zhu–Wang ground truths) + symmetric-extension SDP boundary scan with pre-registered
  gates G1/G2; NUMERICAL cap + pending-review. Execution environment pinned (numpy 1.26.4,
  scipy 1.14.1, sympy 1.13.1, cvxpy 1.6.0, scs 3.2.7). Awaiting lead go.
- 2026-07-28 — paired rule-6/7 review commission authored (fresh-session reviewer, 7a–7g embedded,
  neutral mandate): [WHGAP_REVIEW_COMMISSION_R1_20260728.md](../../notes/WHGAP_REVIEW_COMMISSION_R1_20260728.md).
  It is the completion gate for this node; runs after the execution commission's artifact lands.
- 2026-07-28 — P1 execution stopped before gate G0: the commission-pinned Python executable
  `C:<home>/AppData/Local/Microsoft/WindowsApps/python.exe` could not be resolved or accessed.
  Frozen conventions forbid substituting another interpreter, so C1–C6 were not evaluated, Step 1
  was not run, and no boundary claim was made. See the
  [execution artifact](../../../../artifacts/whgap_antideg_boundary_20260728.md) and
  [raw invocation record](../../../../artifacts/logs_whgap_20260728/whgap_p0_calibration.log).
- 2026-07-28 — run 2 used the commission's environment addendum interpreter
  `C:<home>/cpython3119/python.exe` with the pinned stack. The existing calibration script
  was audited against C1–C6; two Appendix-B spin-block entries were corrected and its failure
  path was made append-only. The first C6 implementation attempt timed out in a redundant
  27-by-27 symbolic characteristic-polynomial expansion after C1–C5 passed; the final exact
  spin-block implementation passed C1–C6 in 5.592 s. See the
  [final calibration log](../../../../artifacts/logs_whgap_20260728/whgap_p0_calibration_run2_final.log)
  and the preserved [timed-out attempt log](../../../../artifacts/logs_whgap_20260728/whgap_p0_calibration_run2.log).
- 2026-07-28 — G1 passed with `t*(1/2)=-6.944444443839e-04` and
  `t*(4/7)=9.912112677079e-13` after the accuracy ladder. Bisection produced a solver-sign
  bracket `[0.571428384100, 0.571428392615]` of width `8.515e-09`; terminal signs were at the
  `10^-12` solver floor, so G2 supports only **"4/7 numerically tight"** within its `1e-6`
  comparison tolerance. Rational projection and dual extraction produced no exact certificate.
  See the append-only [execution artifact](../../../../artifacts/whgap_antideg_boundary_20260728.md),
  [SDP log](../../../../artifacts/logs_whgap_20260728/whgap_p1_antideg_boundary.log), and
  [full scan CSV](../../../../artifacts/logs_whgap_20260728/whgap_p1_scan.csv).

## Evidence

- 2026-07-28 — capability-boundary evidence only (not mathematical evidence):
  [P1 stopped-run artifact](../../../../artifacts/whgap_antideg_boundary_20260728.md);
  [SHA-256 manifest](../../../../artifacts/logs_whgap_20260728/SHA256SUMS.txt).
- 2026-07-28 — NUMERICAL evidence (run 2):
  [append-only artifact](../../../../artifacts/whgap_antideg_boundary_20260728.md);
  [exact G0 log](../../../../artifacts/logs_whgap_20260728/whgap_p0_calibration_run2_final.log);
  [SDP stdout log](../../../../artifacts/logs_whgap_20260728/whgap_p1_antideg_boundary.log);
  [solve table](../../../../artifacts/logs_whgap_20260728/whgap_p1_scan.csv);
  [machine summary](../../../../artifacts/logs_whgap_20260728/whgap_p1_summary.json);
  [SHA-256 manifest](../../../../artifacts/logs_whgap_20260728/SHA256SUMS.txt).

## Adversarial reviews

- 2026-07-28 - fresh-session rule-7 review completed:
  [WHGAP P1 independent review](../../../../artifacts/whgap_p1_review_20260728.md).
  Overall verdict: **MAJOR** on the proposer's 18-dimensional SDP restriction
  and its displayed `t*(x)`/solver-sign bracket; the review independently
  corroborates only the narrower statement "4/7 numerically tight" at
  `CERTIFIED*` scope, while exact equality and the full node claim remain
  unlicensed. No status write was made by the reviewer. Review scripts, raw
  logs, reproduction, and hashes:
  [review manifest](../../../../artifacts/logs_whgap_review_20260728/SHA256SUMS.txt).

## Open obligations

Remaining open aspects of the claim (any promotion beyond the certified narrow scope requires new
work + a fresh review): (1) exact boundary identification — an exact rational/algebraic primal
extension at/above 4/7 AND an exact dual infeasibility witness below it (both attempts failed;
review GAP); (2) monotone/unique-boundary quantifier (define x* = inf{x : antidegradable} and
prove single transition); (3) the review's eight untested regimes (alternate clean solver,
second exact-algebra stack, complex-Hermitian run, local RK24 re-review, ...). The run-2 script's
18-dim restriction defect stands MAJOR-flagged; any reuse of `tools/whgap_p1_antideg_boundary.py`
must first repair the SDP to the frozen 18+9 swap-invariant formulation.

## Status history

- 2026-07-28 — created OPEN (problem scaffold, lead directive; carried over from the same-day field-level scaffold).
- 2026-07-28 — remained OPEN; P1 stopped before G0 because the frozen pinned interpreter was
  inaccessible. No numerical or completion-tier status was licensed.
- 2026-07-28 — OPEN -> NUMERICAL (proposer-writable evidence tier only): run 2 passed G0/G1/G2
  and supports "4/7 numerically tight"; exact certification failed and independent review is
  pending. Cite: `artifacts/whgap_antideg_boundary_20260728.md`, run logs, and SHA-256 manifest.
- 2026-07-28 — NUMERICAL -> CERTIFIED\* (decision layer, applying the completed fresh-session
  rule-7 review's licensing statement verbatim; pending-review marker removed). Certified scope:
  ONLY "4/7 numerically tight (1e-6)" on the reviewer's independent full swap-invariant
  implementation and operational bracket `[0.5714285629136222, 4/7]`. Explicitly unlicensed:
  exact boundary (GAP), proposer t*(x) table and solver-sign bracket (MAJOR: 18-dim bosonic
  restriction of the frozen 18+9 swap-invariant SDP), PROVED at any scope. Cite:
  `artifacts/whgap_p1_review_20260728.md` (licensing statement + §7b/§7e) and
  `artifacts/logs_whgap_review_20260728/SHA256SUMS.txt`.

## Lean

`lean: none` — settled numerical result; no scalar core worth mechanizing at this tier. (Recorded per DAG_PROTOCOL §7.4: silence is invalid; added 2026-07-30 applying R11 m9.)

