# WHGAP commission P3 — small-x Q>0 onset: exact certified region + single-letter ceiling (2026-07-29)

**Nodes (rule 8a):** target `WHGAP.qpositive-onset`; parent `WHGAP.goal` untouched (stays OPEN).
**Executor:** codex CLI, ONE sequential session, workspace-write sandbox, NO network.
**Python (every invocation):** `"C:<home>/cpython3119/python.exe"` (CPython 3.11.9; pinned
numpy 1.26.4, scipy 1.14.1, sympy 1.13.1, mpmath 1.3.0, cvxpy 1.6.0, scs 3.2.7, pypdf 6.14.2).
**Status discipline (rules 6/7):** AT MOST `NUMERICAL` with `pending-review:` on the target node.
NO CERTIFIED*/PROVED/REFUTED anywhere. A paired rule-7 review decides completion later.

## Step -1 — mandatory pre-task reload

Execute `research/PRETASK_RELOAD_PROMPT.md` FIRST with {PROBLEM_DIR} =
`channel-capacity/werner-holevo-gap`, {NODE_ID} = `WHGAP.qpositive-onset`, ROLE = executor.
Print the PRE-ACTION REPORT before any work; disk overrides this commission — report conflicts.

## Frozen conventions

- Family, Kraus, complement: the WHGAP standard (P1/P2 commissions in this directory):
  `Lambda_x(X) = (1-x)X + (x/2)(Tr(X) 1_3 - X^T)`; `K_0 = sqrt(1-x) 1_3`,
  `K_{mu+1} = sqrt(x/2) A_mu`, `(A_mu)_{jk} = epsilon_{mu j k}`;
  `(Lambda_x^c(X))_{ab} = Tr(K_a X K_b^dag)` on C^4. For 0 < x < 1 both outputs of the
  identity are faithful (P2 gate D1, R2-reviewed).
- Coherent information `Ic(rho) = S(Lambda_x(rho)) - S(Lambda_x^c(rho))`, entropies in BITS
  (log base 2); state the nat<->bit conversion wherever used.
- Lower-bound principle (cite, do not re-prove): `Q(Lambda_x) >= Q1(Lambda_x) =
  sup_rho Ic(rho)` (Lloyd–Shor–Devetak; RK24 Eq. (66)-(67) conventions).
- Literature baseline (RK24 = local `channel-capacity/literature/papers/
  roofeh-karimipour-2024-noisy-werner-holevo/arxiv_2310.15353.pdf`, §5.4): their numerics find
  the optimal single-letter input is the maximally mixed state pi = 1/3 for x below ~0.38 and
  report best lower bound exactly 0 (pure states) above; treat as a CLAIM TO TEST, not truth.
- Known context from this campaign (do not re-derive): Q = P = 0 on [1/2, 1]
  (`WHGAP.zero-capacity-application`, PROVED via R3 + external review). P3 therefore concerns
  x in (0, 1/2) only.

## Step 0 — exact calibration (gate G0; sympy exact, mpmath interval where stated)

- D1. `Lambda_x(pi) = pi` and `Lambda_x^c(pi) = diag(1-x, x/3, x/3, x/3)` exactly (pi = 1_3/3);
  hence the EXACT closed form (bits)
  `Ic(pi, x) = log2(3) + (1-x) log2(1-x) + x log2(x/3)`.
- D2. Monotonicity lemma, exact: `d/dx Ic(pi,x) = log2( x / (3(1-x)) )`, strictly negative for
  `x < 3/4`. Hence Ic(pi,·) is strictly decreasing on (0, 3/4) and has a UNIQUE root x_1 there.
- D3. Certified root: bracket x_1 by exact sign evaluations at rational points using mpmath
  interval arithmetic (mpmath.iv, 60 digits): produce rationals a < x_1 < b with b - a <= 1e-30
  and PROVEN signs Ic(pi,a) > 0 > Ic(pi,b) (interval endpoints, directed rounding). Print x_1
  to 30 digits. Sanity: x_1 in (0.39, 0.392).
- D4. Three exact-interval positivity certificates: at x = 1/4, 1/3, 39/100, evaluate Ic(pi,x)
  in interval arithmetic and record a POSITIVE rational lower bound each (these certify
  Q(Lambda_x) > 0 there via the frozen lower-bound principle).

**GATE G0:** D1–D4 all pass -> proceed. Any failure -> STOP with artifact naming the failure.

## Step 1 — single-letter ceiling scan (S1) and local analysis (S2)

- S1. For each x in {2/5, 21/50, 11/25, 23/50, 12/25, 49/100, 499/1000} and additionally the
  transition bracket {77/200, 0.3915, 79/200}: numerically maximize Ic over ALL density
  matrices (parameterize rho = L L^dag / Tr(L L^dag), L complex lower-triangular, 17 real
  parameters — or an equivalent full parameterization; scipy minimize with >= 200 restarts per
  x: include pi, the RK24 diagonal ansatz diag(s, 1-2s, s) swept over s, random full-rank, and
  near-pure starts). Record: best Ic found, the argmax spectrum, solver diagnostics. Note:
  pure inputs have Ic = 0 exactly (output/environment isospectral) — treat values within
  1e-9 of 0 as the pure-state floor, not as positive findings.
- S2. Local analysis at pi, exact where feasible: the gradient of Ic at pi vanishes by
  covariance; compute the Hessian of Ic at pi (symbolically in x if tractable within 15 min,
  else exactly at the rational grid of S1): determine the exact threshold x_H where pi stops
  being a local maximum, and compare with x_1 (expect x_H = x_1 if the RK24 picture is right;
  any mismatch is a finding).
- S3. Two-letter probe (time-boxed <= 20 min total): at x in {21/50, 23/50, 49/100}, search
  for Ic(Lambda_x^{tensor 2}, rho_2) > 0 over structured families: (a) the 9-dim diagonal
  simplex in the computational product basis; (b) correlated perturbations of pi tensor pi;
  (c) >= 50 random full-parameter restarts on C^9 density matrices. Superadditivity floor:
  compare against 2 * (best single-letter at the same x). Pre-register: any value > 1e-7 with
  clean convergence -> flag MAJOR, re-verify at high precision and with an exact-arithmetic
  spot check of the candidate input; otherwise record the bounded null.

**GATE G2 (pre-registered interpretations; STOP after artifact + node updates):**
- (a) All S1 maxima above x_1 are at the pure-state floor (<= 1e-9) AND S3 null ->
  finding: "single-letter route certifies Q > 0 exactly on (0, x_1); the strip (x_1, 1/2)
  remains open at blocklengths <= 2 within budget".
- (b) Any certified Ic > 0 at some x > x_1 (any blocklength) -> finding: "certified Q > 0
  region extends beyond the max-mixed crossing"; produce an exact-interval certificate for at
  least one such x.
- (c) Any S1 maximum strictly ABOVE Ic(pi,x) for x < x_1 -> record (pi not globally optimal
  below threshold — contradicts RK24's picture; finding, not failure).

## Artifact and closeout (mandatory)

1. Artifact `artifacts/whgap_p3_qonset_20260729.md`: exact formulas and lemma, certified x_1
   bracket, the three interval certificates, S1 table (x, best Ic, argmax character), S2
   threshold comparison, S3 probe record, G2 interpretation. Scripts `tools/whgap_p3_*.py`;
   ALL logs under `artifacts/logs_whgap_p3_20260729/` with SHA256SUMS.txt covering every
   script and log.
2. Node closeout on `channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.qpositive-onset.md`:
   dated Work record + Evidence; status at most `NUMERICAL` + `pending-review:` (note in the
   status text which parts are exact-arithmetic grade awaiting review vs numerical-only);
   sync NODE_INDEX row, mermaid label, outline, "Most recent change" in
   `notes/WERNER-HOLEVO-GAP_PROOF_DAG.md`.
3. Both validators exit 0 with the pinned interpreter:
   `tools/proof_dag_check.py --problem werner-holevo-gap` and `tools/literature_check.py`.
4. Print `FINAL: DONE` or `FINAL: FAILED — <reasons>`.

**Budget box:** <= 75 min compute; single symbolic step > 15 min -> documented numeric
fallback; S3 hard-capped at 20 min. Two info-free cycles -> STOP and report.

