# WHGAP P6b — exact verification: necessity witness (V1) + isotropic weight operator (V2) (2026-07-29)

**Executor identity (recorded honestly):** the commissioned Opus executor was killed twice by
API overload (529) and once by the session usage limit, mid-way through repairing V2's
conjugation trap; the DECISION LAYER completed execution directly (running scripts costs no
LLM quota). The rule-6/7 review gate is unchanged and still owed to a fresh instance. All
intermediate failures are retained append-only.

## V1 — the lead's analytic BKM-necessity witness: PASS (both scripts, exit 0)

`tools/whgap_p6b_v1_witness.py` (V1_1..V1_6 all PASS) and `tools/whgap_p6b_v1_bridge.py`
(PASS), logs `logs_whgap_p6b_20260729/v1_witness.log`, `v1_bridge.log`. Verified exactly:
the witness pair rho_eps = diag(1-2eps, eps, eps), X = (E12+E21)/sqrt2; Lambda_x(X) =
(1-3x/2) X; the complement cross-block vanishing and Lambda_x^c(X) = 0 ⊕ (-x/2) X; the BKM
weights g_B = (1-3x/2)^2 / (x/2 + (1-3x/2) eps) and g_E = x/(2(1-eps)); the eps->0 gap
identity x/2 - (2/x)(1-3x/2)^2 = 2(1-x)(2x-1)/x; a finite-eps STRICT violation family at
every tested rational x < 1/2; and the lambda_5/2 bookkeeping (the gap equals half the
multiplicity-five defect eigenvalue; the witness lives in the spin-2 sector). This is the
exact-verification layer under the paper's Theorem 5.2 / Corollary 5.3.

## V2 — isotropic weight operator D_psi(x): PASS after supersession

The interrupted executor's `tools/whgap_p6b_v2_isotropic.py` was found DEFECTIVE in its own
D/basis assembly: after the decision layer cleared its conjugation artifacts (append-only
history: two failing runs in `logs_whgap_p6b_20260729/v2_isotropic.log`), it produced
d_1 = 1-x — which would imply an N1'-ascent at proved-zero x, impossible. Independent
numeric arbitration (numpy eigh, x = 9/20) gave d_1 = -0.0887096774 = -11/124 EXACTLY
matching the earlier P9b datum and the closed-form claim. The decision layer then wrote the
replacement `tools/whgap_p6b_v2_fable.py` (exact sympy, orthogonal Gram-Schmidt kernel
projector, real-adjoint discipline, I-free-conjugate stripping documented in-code):
**all six gates PASS** (`logs_whgap_p6b_20260729/v2_fable.log`, `v2_fable_results.json`):

- spec Lambda_x(P_psi) = {1-x/2, x/2, 0} at the isotropic psi = (e1 + i e2)/sqrt2; E-kernel
  dimension 2 with verified orthogonal projector Pi_E;
- D = M_B - M_E is EXACTLY diagonal in (e3, psi-bar, psi) with
  **d_0 = -x(1-x)/(2-x) (strictly negative on (0,1)), d_1 = (1-x)(2-5x)/(2-x), d_2 = 0**;
- sign rule d_1 (2-x)/(1-x) = 2-5x: **d_1 > 0 iff x < 2/5**;
- x = 9/20 crosscheck: diag(-99/620, -11/124, 0) — matches P9b.

## Consequence recorded (CONJECTURED tier — pending the N1' expansion lemma's review)

Since max_phi (w_B - w_E) = max(d_0, d_1, d_2) = d_1 for x < 2/5, the first-order isotropic
ascent of the (reviewed-pending) N1' expansion exists exactly for x < 2/5:
**candidate exact single-letter onset x_D = 2/5**, implying Q(Lambda_x) > 0 for every
x in (0, 2/5) — which would shrink the open strip to [2/5, 1/2) (width 0.1) and explain why
P3's optimizer missed the narrow isotropic ridge at 0.395 < 2/5. This implication rests on
the epsilon-log-epsilon expansion (hand-derived; kernel-plunge and fit checks passed in P9;
NOT yet independently reviewed) — it is NOT promoted beyond CONJECTURED here.

## Provenance

Scripts: whgap_p6b_v1_witness.py, whgap_p6b_v1_bridge.py, whgap_p6b_v2_isotropic.py
(superseded, retained), whgap_p6b_v2_fable.py. Logs + JSON + SHA256SUMS.txt in
`logs_whgap_p6b_20260729/`. Interpreter C:<home>/cpython3119/python.exe throughout.

