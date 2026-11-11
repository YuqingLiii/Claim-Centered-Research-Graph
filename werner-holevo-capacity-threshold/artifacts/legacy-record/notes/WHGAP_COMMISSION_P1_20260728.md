# WHGAP commission P1 — calibration + exact antidegradability boundary x* (2026-07-28)

**Nodes (rule 8a):** target `WHGAP.antideg-boundary`; parent recompute `WHGAP.goal`.
`WHGAP.signed-lift-extension` is explicitly OUT of scope (separate later commission).
**Executor:** codex CLI, ONE sequential session, workspace-write sandbox, NO network.
**Python:** `"C:<home>/AppData/Local/Microsoft/WindowsApps/python.exe"` (bare `python` is Inkscape's).
Preinstalled, pinned: numpy 1.26.4, scipy 1.14.1, sympy 1.13.1, mpmath, cvxpy 1.6.0, scs 3.2.7.
**Status discipline (rules 6/7):** this commission may write AT MOST `NUMERICAL` with an explicit
`pending-review:` marker on `WHGAP.antideg-boundary`. NO CERTIFIED*/PROVED/REFUTED anywhere.
A separate rule-7 review commission decides completion later. Do not touch any other node's status.

## Step -1 — mandatory pre-task reload

Execute the standalone rules-reload prompt `research/PRETASK_RELOAD_PROMPT.md` FIRST, with
{PROBLEM_DIR} = `channel-capacity/werner-holevo-gap`, {NODE_ID} = `WHGAP.antideg-boundary`,
ROLE = executor. No work before its PRE-ACTION REPORT is produced; its folder-and-DAG maintenance
obligations bind this entire commission. Disk overrides this commission on any conflict.

## Frozen conventions — use EXACTLY; deviation = STOP and report, never improvise

- Qutrit computational basis `|0>,|1>,|2>`; matrix units `E_ij`.
- Family: `Lambda_x(X) = (1-x) X + (x/2) (Tr(X) 1_3 - X^T)`, `x in [0,1]`.
  Sanity identity: at `x=1/2` this equals Zhu–Wang's `Lambda(X) = X/2 + (Tr(X) 1 - X^T)/4`.
- Kraus: `K_0 = sqrt(1-x) * 1_3`; `K_{mu+1} = sqrt(x/2) * A_mu` (mu=0,1,2), `(A_mu)_{jk} = epsilon_{mu j k}`.
  Identities to verify: `sum_mu A_mu X A_mu^dag = Tr(X) 1 - X^T`; `sum_mu A_mu^dag A_mu = 2 * 1_3`.
- Complementary channel on `H_E = C^4`: `(Lambda_x^c(X))_{ab} = Tr(K_a X K_b^dag)`, a,b in {0,1,2,3}.
- Choi: `omega_x = (id_A ⊗ Lambda_x)(|Phi><Phi|)`, `|Phi> = (|00>+|11>+|22>)/sqrt(3)`; partial transpose `T_A`.
- Antidegradability criterion (FROZEN; Myhr–Lütkenhaus as used in arXiv:2607.24693 §5):
  `Lambda_x` antidegradable  <=>  exists `eta` on `A ⊗ B1 ⊗ B2` (27-dim) with
  `eta >= 0`, `(1_A ⊗ S_12) eta (1_A ⊗ S_12) = eta`, `Tr_{B2} eta = omega_x`.
- Local literature: `../literature/../..` — the Zhu–Wang PDF is at
  `channel-capacity/literature/papers/zhu-wang-2026-quantum-incapacity/arxiv_2607.24693.pdf`.
  RK24 (antidegradable for `x >= 4/7`): Roofeh–Karimipour, PRA 109, 052620 (2024) — cite only, PDF not local.

## Step 0 — calibration at x = 1/2 (script `tools/whgap_p0_calibration.py`; exact arithmetic where stated)

- C1. The two Kraus identities above — exact (sympy).
- C2. `Lambda(1) = 1`; `Lambda^c(1) = diag(3/2, 1/2, 1/2, 1/2)` — exact.
- C3. `spec(omega^{T_A}) = {1/4 (x5), 0 (x1), -1/12 (x3)}` — exact.
- C4. Zhu–Wang lift (their Eq. (4.12)): with `a(Y) = (Y_12 - Y_21, Y_20 - Y_02, Y_01 - Y_10)^T`,
  `J(Y) = (1/3) [[Tr Y, sqrt(2) a(Y)^T], [-sqrt(2) a(Y), 2 Tr(Y) 1_3 - Y - 2 Y^T]]`.
  Verify `J^dag ∘ Lambda^c = Lambda` on the full matrix-unit basis — exact.
  Verify `J(E_00) = (1/3) diag(1, -1, 2, 2)` is not PSD.
- C5. Defect factorization (their Eqs. (4.18)–(4.20)): `Delta(tau) = L_{Lambda(tau)} - J^dag ∘ L_{Lambda^c(tau)} ∘ J`
  equals `(2/9) sum_mu G_mu tau G_mu^dag`, `G_mu |i> = |i>|mu> + (1/2)|mu>|i> - (1/2) delta_{mu i} sum_j |j>|j>`.
  Verify entrywise on matrix units — exact. Verify `Tr(G_mu^dag G_nu) = 4 delta_{mu nu}`.
- C6. Witness (their §5): `w0 = (2 sqrt(3) - 4)/5`, `w1 = (2 sqrt(3) - 3)/5`,
  `W = w0 Phi + w1 P^- + P_st` with `P^- = (1 - F)/2`, `P_st = (1 + F)/2 - Phi`.
  Verify `Tr(W omega) = (4 sqrt(3) - 7)/10 < 0` — exact (sympy sqrt(3)).
  Verify `H = (1/2)(W_{AB1} ⊗ 1_{B2} + S_12 (W_{AB1} ⊗ 1_{B2}) S_12) >= 0` — exact (any exact PSD proof acceptable).

**GATE G0 (pre-registered):** ALL of C1–C6 pass exactly -> proceed to Step 1.
ANY failure -> STOP; write the artifact naming the failing check; do NOT run Step 1.

## Step 1 — antidegradability boundary scan (script `tools/whgap_p1_antideg_boundary.py`)

- S1. Feasibility test `F(x)`: the 27-dim symmetric-extension SDP above, solved as
  `t*(x) = max t s.t. eta >= t*I, swap-symmetry, Tr_{B2} eta = omega_x` (cvxpy + SCS).
  Antidegradable  <=>  `t*(x) >= 0` (within tolerance). Accept only clean solver status; on
  `inaccurate`, raise accuracy (`eps_abs/eps_rel` down to 1e-11) and re-solve; unresolvable -> record caveat.
- S2. **GATE G1 (endpoints):** `F(4/7)` feasible (`t* >= -1e-9`) AND `F(1/2)` infeasible (`t* < -1e-6`).
  Must match RK24 and Zhu–Wang. Fail -> STOP; no boundary claim.
- S3. Bisect `x*` in `[1/2, 4/7]` to `|Delta x| <= 1e-8`; log every `(x, t*(x), solver status, time)`.
- S4. Exactness attempt (best effort, record what succeeded):
  (a) rationalize `x*` (sympy nsimplify: rationals with denominator <= 200; quadratic surds);
  (b) feasibility certificate just above `x*`: round the SCS `eta` to rationals, project onto the
  affine constraints, exact PSD check (sympy LDL) — an exact antidegradability certificate;
  (c) infeasibility side: extract the SDP dual solution as a witness candidate and attempt exact
  rational verification.
- S5. Artifact `artifacts/whgap_antideg_boundary_20260728.md`: scan table, bracket, `x*` to 1e-8,
  rationalization outcome, certificate status, runtimes. All logs under
  `artifacts/logs_whgap_20260728/` with `SHA256SUMS.txt` covering every script and log.

**GATE G2 (interpretation, pre-registered):**
- `x* < 4/7 - 1e-6` -> finding: "antidegradable region extends below 4/7, boundary at x* (numeric)".
- `|x* - 4/7| <= 1e-6` -> finding: "4/7 numerically tight".
Either way: STOP after the artifact + node updates. No further exploration in this commission.

## Closeout (structure protocol §6; DAG protocol §5–§6) — mandatory

1. Append dated Work record + Evidence entries (artifact links) to
   `channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.antideg-boundary.md`.
2. If gates passed: set its status to `NUMERICAL` with `pending-review:` marker and
   `status_source` citing the artifact. `WHGAP.goal` recomputes (stays OPEN).
3. Sync NODE_INDEX row, mermaid label, outline, and the DAG doc's "Most recent change" line in the
   same change (`notes/WERNER-HOLEVO-GAP_PROOF_DAG.md`).
4. Run both validators; both MUST exit 0:
   `python tools/proof_dag_check.py --problem werner-holevo-gap` and `python tools/literature_check.py`.
5. Print `FINAL: DONE` or `FINAL: FAILED — <reasons>`.

**Budget box:** one sequential codex session; compute target <= 60 min; any single SDP solve > 5 min
-> drop to the documented accuracy ladder and note it. Two info-free cycles or budget breach -> STOP
and report (capability-boundary stop-loss).

## Environment addendum — 2026-07-28 (decision layer, after run 1)

Run 1 (log: `tmp/codex_whgap_p1_20260728.log`) STOPPED before G0: the pinned WindowsApps
`python.exe` is an app-execution alias that the codex sandbox token cannot resolve (Access denied);
a venv built from the store Python fails identically (its launcher chains back to the alias).
Fix — environment mechanics only, NO frozen mathematical convention touched: every python
invocation in this commission now uses

`"C:<home>/cpython3119/python.exe"`

— official CPython 3.11.9 (python.org build, NuGet package `python 3.11.9`) at a normal-ACL path,
with the IDENTICAL pinned stack installed and verified: numpy 1.26.4, scipy 1.14.1, sympy 1.13.1,
mpmath 1.3.0, cvxpy 1.6.0, scs 3.2.7. Sandbox execute probe: PASS (codex micro-session, 2026-07-28).
Run-1 standing: `tools/whgap_p0_calibration.py` was authored but NEVER executed — run 2 verifies it
against C1–C6, fixes if needed, then runs it. The run-1 artifact and node entries documenting the
environment failure are cited history — extend them; do not delete, rename, or overwrite run-1 text.

## Paired review (rule 6 — the completion gate)

After this commission completes, the paired review commission
[WHGAP_REVIEW_COMMISSION_R1_20260728.md](WHGAP_REVIEW_COMMISSION_R1_20260728.md) MUST be run as a
FRESH codex session (a session that did not author this work and is not told the wanted answer)
before any completion-tier status may be considered. Until that review is completed, archived, and
cited, everything produced here stays at NUMERICAL with the `pending-review:` marker.

