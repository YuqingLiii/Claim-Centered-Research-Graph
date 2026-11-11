# WHGAP commission P6b — exact verification of the analytic necessity structures (2026-07-29)

**Purpose:** the LEAD supplied an analytic BKM-necessity witness (hand-verified by the
decision layer) upgrading the P6 numerical bracket toward an iff theorem; P9b produced the
exact isotropic weight operator D_psi(9/20). This commission verifies BOTH structures
exactly at symbolic x and produces paper-grade (LaTeX-ready) lemma blocks for manuscript v3.

**Nodes (rule 8a):** `WHGAP.order-boundary` (V1) and `WHGAP.no-ascent-hierarchy` (V2) —
appends only on the latter (CONJECTURED is decision-layer-owned); the former may receive an
updated NUMERICAL + `pending-review:` evidence entry (no completion tier).
**Executor:** codex CLI, ONE sequential session, workspace-write, NO network.
**Python:** `"C:<home>/cpython3119/python.exe"`.

## Step -1 — mandatory pre-task reload

`research/PRETASK_RELOAD_PROMPT.md` with {PROBLEM_DIR} = `channel-capacity/werner-holevo-gap`,
{NODE_ID} = `WHGAP.order-boundary`, ROLE = executor. PRE-ACTION REPORT first.

## Frozen conventions

WHGAP standard family/Kraus/complement; natural logs; BKM weights
c(a,b) = (log a - log b)/(a-b), c(a,a) = 1/a.

## V1 — the lead's tau=1 BKM-necessity witness (treat every displayed step as a CLAIM)

With `rho_eps = diag(1-2eps, eps, eps)` and `X = (E12 + E21)/sqrt(2)`:
1. Verify symbolically (x, eps symbols): `Lambda_x(X) = (1 - 3x/2) X`;
   `Lambda_x(rho_eps)` is diagonal with the {1,2}-block common eigenvalue
   `b_eps = x/2 + (1 - 3x/2) eps`; `a(X) = 0` hence
   `Lambda_x^c(X) = 0 (+) (-(x/2) X)`; `Lambda_x^c(rho_eps)` is block diagonal
   `(1-x) (+) (x/2) diag(2eps, 1-eps, 1-eps)` with the relevant environment 2x2 block
   eigenvalue `e_eps = (x/2)(1-eps)`.
2. Verify the two BKM forms exactly: `g_B(eps) = (1-3x/2)^2 / b_eps` and
   `g_E(eps) = x / (2(1-eps))` (build the FULL 9x9 / 16x16 BKM forms from the definition in
   the output eigenbases and evaluate on the displayed operators — do not shortcut to the
   degenerate-block formula without verifying the operators are supported there).
3. Verify the limit identity: `g_E(0) - g_B(0) = x/2 - (2/x)(1 - 3x/2)^2
   = 2(1-x)(2x-1)/x` (exact factorization), and hence g_E(0) >= g_B(0) iff x >= 1/2 on (0,1).
4. FINITE-eps strictness: exhibit, for symbolic x in (0, 1/2), an explicit eps*(x) > 0
   (e.g. eps = (1-2x)... derive one) with `g_E(eps) < g_B(eps)` PROVEN as a symbolic
   inequality on the stated domain (so the witness is a bona fide finite violation family,
   not only a limit). Also verify `rho_eps` faithful and X traceless Hermitian.
5. Second-order bridge check (numeric, high precision): for 3 random faithful sigma and
   small t, confirm `D(Phi(sigma + tX') || Phi(sigma)) = (t^2/2) g_{Phi(sigma)}(Phi(X'))
   + O(t^3)` for both channels at 2 strip x values (validates the RE->BKM necessity step
   used in the write-up; the general lemma itself is decision-layer prose).
6. lambda_5 bookkeeping: verify `g_E(0) - g_B(0) = lambda_5(x)/2` exactly, and verify X is
   spin-2 (symmetric traceless).

## V2 — the isotropic weight operator D_psi(x) in closed form

For the canonical isotropic `psi = (0, 1, -i)/sqrt2` (and transported by one generic O(3)
rotation as a check): derive symbolically in x the 3x3 operator `D_psi(x) = M_B - M_E` in
the basis (e_0-type, psi-bar, psi) exactly as P9b defined it (w_B - w_E = Tr[D_psi phi]);
display its entries as rational functions of x; verify D_psi(9/20) = diag(-99/620,
-11/124, 0); determine EXACTLY the set {x in (0,1) : D_psi(x) <= 0} (eigenvalue sign
analysis — expect a closed-form threshold x_D; compare x_D with x_1 = 0.390910... and with
1/2; any of x_D < x_1, = x_1-related, or in the strip is a finding — pre-register: report
the exact threshold with NO interpretation beyond stating the comparison).

## Artifact and closeout

1. Artifact `artifacts/whgap_p6b_analytic_20260729.md` with LaTeX-ready lemma blocks for
   V1 (the witness lemma) and V2 (the D_psi landscape); machine JSON + logs +
   SHA256SUMS.txt under `artifacts/logs_whgap_p6b_20260729/`; scripts `tools/whgap_p6b_*.py`.
2. Node appends: `WHGAP.order-boundary` (V1 evidence; status stays NUMERICAL +
   pending-review) and `WHGAP.no-ascent-hierarchy` (V2 evidence; status untouched);
   sync the DAG doc "Most recent change".
3. Both validators exit 0. Print `FINAL: DONE` or `FINAL: FAILED — <reasons>`.

**Budget box:** <= 60 min; 15-min single-step rule; two info-free cycles -> STOP.

