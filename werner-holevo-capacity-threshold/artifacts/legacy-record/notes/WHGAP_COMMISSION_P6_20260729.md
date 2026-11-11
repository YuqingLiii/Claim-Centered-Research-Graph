# WHGAP commission P6 — order-boundary scan (E1) + relaxed two-sided-lift feasibility (E2) (2026-07-29)

**Nodes (rule 8a):** primary `WHGAP.order-boundary` (E1); secondary `WHGAP.relaxed-lift` (E2
evidence only — its CONJECTURED status is decision-layer-owned and must NOT be changed).
`WHGAP.more-capable-route` is PARKED and out of scope. Parent `WHGAP.goal` untouched.
**Executor:** codex CLI, ONE sequential session, workspace-write, NO network.
**Python:** `"C:<home>/cpython3119/python.exe"` (pinned stack + mpmath 1.3.0).
**Status discipline:** AT MOST `NUMERICAL` + `pending-review:` on `WHGAP.order-boundary`;
on `WHGAP.relaxed-lift` append Work-record/Evidence lines only, no status field change.

## Step -1 — mandatory pre-task reload

Execute `research/PRETASK_RELOAD_PROMPT.md` FIRST with {PROBLEM_DIR} =
`channel-capacity/werner-holevo-gap`, {NODE_ID} = `WHGAP.order-boundary`, ROLE = executor.
PRE-ACTION REPORT before any work; disk overrides on conflict.

## Frozen conventions

- Family, Kraus, complement: the WHGAP standard (P1/P2 commissions). M = Lambda_x,
  N = Lambda_x^c (4-dim padded complement; faithful outputs for 0 < x < 1).
- **BKM form (natural log):** for faithful theta with spectral decomposition
  theta = sum_i lambda_i |i><i|, and any operator Z written in that eigenbasis,
  `g_theta(Z) = sum_{ij} |Z_{ij}|^2 c(lambda_i, lambda_j)`,
  `c(a,b) = (log a - log b)/(a - b)` for a != b, `c(a,a) = 1/a`.
- **Domination superoperators:** for a channel Phi and faithful input sigma (on R (x) A):
  `T_Phi[sigma] = Phi_R^dagger ∘ Gamma_{Phi_R(sigma)}^{-1} ∘ Phi_R` acting on Hermitian
  operators on R (x) A, where Phi_R = id_R (x) Phi and Gamma_theta^{-1} is the BKM weight
  (matrix elements c(lambda_i, lambda_j) in the eigenbasis). cBKM domination of N over M at
  (R, sigma) means `T_N[sigma] - T_M[sigma] >= 0`; a NEGATIVE eigenvalue of that Hermitian
  superoperator is an order violation witness.
- Known anchors (do not re-derive): Q > 0 on (0, x_1), x_1 = 0.390910232076... (P3, PROVED
  scope) — hence the cBKM order MUST be violated for every x < x_1; the covariant lift
  certifies the order on [1/2, 1) (P2/P4).
- **Criterion (W) (from `WHGAP.relaxed-lift`, CONJECTURED):** J complex-linear (adjoint
  preservation NOT required), J^dagger ∘ N = M, and BOTH defects CP:
  `Delta^L(tau) = L_{M(tau)} - J^dagger L_{N(tau)} J` and
  `Delta^R(tau) = R_{M(tau)} - J^dagger R_{N(tau)} J` (R_A(Y) = Y A). Logical containment to
  enforce as a crosscheck: any x with a valid (W)-certificate must show NO order violation
  in E1.

## E1 — cBKM order-boundary scan (node `WHGAP.order-boundary`)

- D1 (scanner calibration, gate G0):
  (a) at `x = 7/20` (< x_1): find an order violation — minimize the smallest eigenvalue of
  `T_N[sigma] - T_M[sigma]` over faithful sigma with references d_R in {1, 2, 3}
  (Cholesky-parameterized sigma, >= 150 restarts incl. pi_R (x) pi_A, near-pure-perturbed
  starts, and inputs built from the P3 rank-two witness direction); a violation MUST exist.
  Rationalize the best sigma, redo the eigenproblem in mpmath interval arithmetic (60+
  digits, directed) and certify a negative eigenvalue upper bound. GATE G0a = certified
  violation at 7/20.
  (b) at `x = 1/2` and `x = 11/20`: same search budget must find NO violation
  (floor >= -1e-9). GATE G0b.
- S1 (strip scan): for x in {2/5, 21/50, 11/25, 23/50, 12/25, 49/100, 499/1000}: same
  minimization; record per (x, d_R) the minimal eigenvalue found, the argmin sigma
  character, and restart statistics.
- S2 (boundary + certification): wherever violations are found, interval-certify one
  rational witness per x; locate the numerical no-violation boundary x_B by bisection (width
  <= 1e-4) with warm starts; state clearly that the no-violation side is EVIDENCE (bounded
  search), not a theorem.
- **GATE G2-E1 (pre-registered):**
  (a) certified violations at every strip grid point up to 1/2 - 1e-3 -> finding: "the cBKM
  order breaks throughout the tested strip; the signed-lift mechanism's reach [1/2, 1)
  coincides with the order's reach on this family (bounded-search evidence on the
  no-violation side at [1/2, 1))";
  (b) a subinterval of the strip with NO violation found under the full budget -> finding:
  "candidate weaker-certificate terrain (x_B, 1/2)" — flag prominently; E2's scan must then
  prioritize that window;
  (c) mixed -> report per-point, no interpolation.

## E2 — criterion-(W) stress test and feasibility scan (evidence for `WHGAP.relaxed-lift`)

- D2 (soundness stress test, gate G1): generate >= 200 random instances (random dimensions
  <= 3/4, random faithful sigma, random J WITHOUT adjoint preservation constructed so that
  both defects are CP — e.g. by shrinking random J toward a known-feasible one until both
  defect Chois are PSD); check the conclusion inequality `g_omega(Z) >= g_sigma(J^dagger Z)`
  on >= 20 random Hermitian Z per instance (omega = N(sigma)-side weights as in the
  criterion). ANY counterexample -> STOP, report it verbatim (it would falsify the
  CONJECTURED soundness of (W) — that is a decisive, valuable outcome).
- S3 (complex covariant feasibility below 1/2): ansatz
  `J(Y) = [[p Tr Y, u a(Y)^T], [v a(Y), c1 Tr(Y) 1 + c2 Y + c3 Y^T]]` with ALL of
  p, u, v, c1, c2, c3 COMPLEX (12 real parameters). Impose `J^dagger ∘ Lambda_x^c = Lambda_x`
  symbolically (careful: J^dagger is the Hilbert–Schmidt adjoint — the conjugate transpose of
  J's 16x9 superoperator matrix; the intertwining is an identity of maps on the full complex
  operator space). Report the residual family's real dimension. Then, at
  x in {13/25, 1/2} (sanity: must contain the real ZW/forced-point solutions) and
  x in {49/100, 47/100, 9/20} plus any G2-E1(b) window points: search the residual family
  for points where BOTH 27x27 defect Chois are PSD (penalty minimization of total negative
  eigenvalue mass, >= 100 restarts; exploit the spin block structure if it extends to the
  complex ansatz — document whether it does). Any feasible point found below 1/2:
  rationalize and attempt exact PSD certification of both Chois.
- **GATE G2-E2 (pre-registered):**
  (a) certified (W)-certificate below 1/2 -> MAJOR-positive finding: "the relaxed criterion
  strictly extends the mechanism's reach below 1/2" (must be consistent with E1 —
  crosscheck mandatory; a contradiction is a bug gate: STOP and diagnose);
  (b) all searches floor out below 1/2 AND (if the reduction extends) forced-vanishing
  structures reappear -> finding: "within the complex covariant ansatz, (W) does not extend
  the reach; the 1/2 edge appears order-driven, not artifact of adjoint preservation";
  (c) partial -> report per-point.

## Artifact and closeout

1. Artifact `artifacts/whgap_p6_relaxation_20260729.md`: scanner definition and calibration,
   E1 table (x, d_R, min eigenvalue, certified?), certified-witness data, x_B evidence,
   D2 stress-test statistics, S3 residual-dimension derivation and feasibility table, the
   pre-registered interpretations. Scripts `tools/whgap_p6_*.py`; logs + JSON +
   SHA256SUMS.txt under `artifacts/logs_whgap_p6_20260729/`.
2. Node closeouts: `WHGAP.order-boundary` -> at most NUMERICAL + `pending-review:` with
   Work record/Evidence; `WHGAP.relaxed-lift` -> Work record/Evidence appends ONLY (status
   stays CONJECTURED, owned by the decision layer); sync NODE_INDEX prose, mermaid labels,
   outline, "Most recent change".
3. Both validators exit 0 with the pinned interpreter.
4. Print `FINAL: DONE` or `FINAL: FAILED — <reasons>`.

**Budget box:** <= 90 min compute; single symbolic step > 20 min -> documented cheaper route;
S3 hard-capped at 35 min. Two info-free cycles -> STOP and report.

