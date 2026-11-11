# WHGAP commission P9b — repaired no-ascent hierarchy on the isotropic stratum (2026-07-29)

**Context:** P9-E1's pre-registered G0 gate correctly caught two defects in the original N1
(generic-pure spectrum; degenerate allowed set). The decision layer repaired the formulation
on the isotropic stratum (see the dated N1' section of the node). This commission verifies
and scans N1'.

**Nodes (rule 8a):** primary `WHGAP.no-ascent-hierarchy` (status CONJECTURED is
decision-layer-owned — append Work-record/Evidence only). Parent `WHGAP.goal` untouched.
**Executor:** codex CLI, ONE sequential session, workspace-write, NO network.
**Python:** `"C:<home>/cpython3119/python.exe"`.

## Step -1 — mandatory pre-task reload

`research/PRETASK_RELOAD_PROMPT.md` with {PROBLEM_DIR} = `channel-capacity/werner-holevo-gap`,
{NODE_ID} = `WHGAP.no-ascent-hierarchy`, ROLE = executor. PRE-ACTION REPORT first.

## Frozen conventions

WHGAP standard family/Kraus/complement; natural logs. Isotropy invariant
`tau(psi) = |psi^T psi|`. The N1' claims (from the node — CLAIMS to verify, not truths):
- At tau = 0: spec Lambda(P) = {1-x/2, x/2, 0} (kernel = span{psi-bar});
  spec Lambda^c(P) = {1-x/2, x/2, 0, 0} (kernel K_E two-dimensional).
- Weights `w_B = <psi-bar|Lambda(phi)|psi-bar>`, `w_E = Tr[Pi_E Lambda^c(phi)]`;
  `Ic((1-eps)P + eps phi) = (w_B - w_E) eps log(1/eps) + O(eps)`.
- (N1'-a): Q^{(1)} = 0 forces w_B <= w_E for all isotropic psi and all states phi.
Anchors: x_1 = 0.390910232076...; P3's witness base v = (0, 1/sqrt2, -i/sqrt2) (check
v^T v = 0 exactly).

## Deliverables

- **G0' (repaired derivation gate, exact + numeric):**
  (i) symbolic verification of both tau = 0 spectra for a PARAMETERIZED isotropic family
  (not one sample): construct the general isotropic pure state via psi = (u + i v)/sqrt2
  with u, v real orthonormal (verify tau = 0), plus 3 random numeric isotropic samples;
  (ii) exact tau-generic cross-check: for tau in {1, 1/2, 0} display spec Lambda(P) and
  confirm it interpolates (the P9 failure sample (1, i, 1)/sqrt3 must reproduce its observed
  spectrum; compute its tau);
  (iii) epsilon-fit: at x = 9/20, for >= 5 random (isotropic psi, phi) pairs with
  w_B != w_E, fit Ic(rho_eps) against (w_B - w_E) eps log(1/eps) + c eps over
  eps in [1e-9, 1e-4] and confirm the leading coefficient to >= 6 digits; for >= 3 balanced
  pairs (construct w_B = w_E by mixing), confirm the log-term cancels (fit residual slope
  finite).
  GATE: all pass -> proceed; any fail -> STOP with the failing datum (that again falsifies
  the decision layer's repair — a valuable outcome).
- **S1' ((N1'-a) scan, n = 1):** at x in {77/200 (anchor: violation SHOULD appear near
  P3's witness geometry — check), 2/5, 21/50, 11/25, 23/50, 12/25, 49/100, 1/2, 11/20
  (anchors: must hold)}: maximize `w_B - w_E` over isotropic psi (4 real params) and states
  phi (8 params), >= 200 restarts incl. P3-geometry starts. Any positive max in the strip:
  rationalize (psi, phi), certify w_B - w_E > 0 exactly (these are ALGEBRAIC quantities —
  exact rational/surd arithmetic, no interval needed unless surds get heavy), and then
  CONFIRM the implied ascent by exact-interval Ic evaluation at a small explicit eps
  (P3-grade). **A certified strip violation = MAJOR strip-resolving finding (Q > 0 there).**
- **S2' (balanced layer, best effort within 20 min):** derive c_1 on the balanced set
  symbolically (support-block Frechet derivative + kernel-block entropy pieces); verify
  against the numeric fits from G0'(iii); scan max c_1 over balanced directions at
  x in {21/50, 23/50, 49/100}. Document precisely what is derived vs numerically observed.
- **S3' (n = 2 isotropic layer, hard-capped 30 min):** isotropic-entangled psi_2
  (tau_2 = |psi_2^T psi_2| = 0; include tensor products of 1-copy isotropic states AND
  genuinely entangled isotropic psi_2, e.g. Schmidt-rank 2/3 constructions), exact kernel
  projectors of Lambda^{tensor 2}(P_2) and (Lambda^c)^{tensor 2}(P_2) per psi_2, scan
  w_B^(2) - w_E^(2) at x in {21/50, 23/50, 49/100}; same certification duty on any positive.
- **Pre-registered interpretations (G2):** (a) certified strip violation at any layer ->
  MAJOR (Q > 0 at that x); (b) all floors -> bounded-null: "N1' holds across the searched
  strip; hierarchy consistent with Q = 0 there"; (c) G0' failure -> repair falsified, STOP.

## Artifact and closeout

1. Artifact `artifacts/whgap_p9b_noascent_20260729.md` (tables, certified data, derivation
   record); scripts `tools/whgap_p9b_*.py`; logs + JSON + SHA256SUMS.txt under
   `artifacts/logs_whgap_p9b_20260729/`.
2. Node: Work-record/Evidence appends on `WHGAP.no-ascent-hierarchy` (status stays
   CONJECTURED); sync NODE_INDEX prose, mermaid, outline, "Most recent change".
3. Both validators exit 0 (pinned interpreter).
4. `FINAL: DONE` or `FINAL: FAILED — <reasons>`.

**Budget box:** <= 75 min compute; 20-min single-step rule; caps as stated. Two info-free
cycles -> STOP and report.

