# WHGAP commission P5 — paper-grade derivation package for the certificate core (2026-07-29)

**Purpose:** external paper audit #2 (archived:
`artifacts/whgap_external_review_chatgpt_paper_20260729.md`) passed the mathematics but ruled
the manuscript **Major Revision**: the central computations are declared, not proven, in the
text. This commission generates the EXACT, DISPLAYABLE derivation data that the decision layer
will transcribe into the revised appendices. It creates NO new mathematics and NO status
changes — it is exposition data for content already PROVED-licensed by R2
(`artifacts/whgap_p2_review_20260728.md`, licensing statements 1–2).

**Nodes (rule 8a):** content node `WHGAP.signed-lift-extension` (whose R2-PROVED core is being
expounded); deliverable registered as Evidence there and on `WHGAP.goal` (paper evidence). DO
NOT touch any node's status. **Executor:** codex CLI, ONE sequential session, workspace-write,
NO network. **Python:** `"C:<home>/cpython3119/python.exe"` (pinned stack).

## Step -1 — mandatory pre-task reload

Execute `research/PRETASK_RELOAD_PROMPT.md` FIRST with {PROBLEM_DIR} =
`channel-capacity/werner-holevo-gap`, {NODE_ID} = `WHGAP.signed-lift-extension`,
ROLE = executor. PRE-ACTION REPORT before any work; disk overrides on conflict.

## Frozen conventions

Exactly the P2 commission's (`WHGAP_COMMISSION_P2_20260728.md`): family, Kraus, complement
with `beta = k = sqrt(x(1-x)/2)`, `a(Y)`, the five-parameter ansatz, the residual family in
`(p, d)` with `d = 2*beta*q` (equivalently the `(s1,s2)` chart; STATE the chart you use and
the conversion), row-major HS identification `E_ij <-> |i>|j>`, unnormalized input-leg-first
Choi `C = sum_ij |i><j| (x) Delta(E_ij)`. Forced point: `p = 1/3`, `d = 2(1-x)/3`.

## Deliverables (every item EXACT sympy, with a per-item verification gate)

- **P5.1 Entrywise closed form.** Determine the exact coefficients `c_k(x; p, d)` in the
  covariant pattern expansion of the defect Choi entries
  `C[(i,b,b'),(j,r,s)] = sum_k c_k * P_k(i,b,b'; j,r,s)`, where `{P_k}` are the fifteen
  products of three Kronecker deltas pairing the six indices. Method: set up the exact linear
  system over the 729 entries at symbolic `(x, p, d)` and solve; if the fifteen patterns do
  not span, report the residual structure honestly (name any extra needed patterns) — do NOT
  force a fit. GATE V1: the fitted expansion reproduces ALL 729 entries symbolically, both
  for the general residual family and specialized to the forced point. Output the formula in
  LaTeX-ready form (analog of Zhu–Wang Eq. (A.2)).
- **P5.2 Forcing identities as displayed computations.** Using P5.1 (or direct contraction),
  produce the two-to-four-line displayed evaluations of
  `<v_p, C v_p> = -((1-x)/x)(3p-1)^2` and `<v_d, C v_d> = -(1/x)(3d-2(1-x))^2`
  (`v_p = |0>_A (x) sum_j |jj>`, `v_d = |0>_A|12> + |1>_A|02>`): list exactly which Choi
  entries contribute to each quadratic form (indices + coefficients from P5.1) and the
  resulting scalar algebra. GATE V2: the displayed entry lists sum symbolically to the stated
  closed forms.
- **P5.3 Spin-adapted bases and reduced blocks.** Explicit multiplicity-space column vectors
  `U_j` (27 x m_j, m = 1,3,2,1 for spins 0..3) with INTEGER entries, each column written in
  ket notation (short sums of |i>|b>|b'>); Gram matrices `G_j = U_j^T U_j`; the four reduced
  blocks `B_j = U_j^T C U_j` as displayed matrices over Q(x, p, d), and their forced-point
  specializations. GATE V3: sum_j m_j (2j+1) = 27; the U_j columns are SO(3)
  highest-weight-consistent (verify they are annihilated/raised correctly by L_+ =
  sum of raising generators, or verify the Casimir eigenvalue j(j+1) exactly); and the direct
  27x27 characteristic polynomial equals the product over j of det(B_j - z G_j)^{2j+1} /
  det(G_j)^{2j+1} normalization — state and verify the exact pencil identity you use.
- **P5.4 Spectrum closure at the forced point.** From the forced-point blocks: the rank-one
  factorizations `B_1 = d_1(x) l_1 l_1^T`, `B_2 = d_2(x) l_2 l_2^T` (display d_j(x) and the
  integer vectors l_j), and the derivation of the two Choi eigenvalues
  `lambda_5 = 4(1-x)(2x-1)/x` (multiplicity 5) and `lambda_3 = 16(1-x)(3x-1)/(9x)`
  (multiplicity 3) via the generalized pencils `B_j - z G_j` — make the Gram bookkeeping
  explicit (this is where a factor slip would hide). GATE V4: annihilating polynomial
  `C(C - lambda_5)(C - lambda_3) = 0` symbolically, plus `Tr C = 5 lambda_5 + 3 lambda_3`
  and `Tr C^2 = 5 lambda_5^2 + 3 lambda_3^2`.
- **P5.5 Certificate congruence data.** At `x = 26/51, 4/7, 3/4`: the full exact data —
  `(s1, s2)` and `(p, q, d)`, all four `B_j` with `G_j`, the rank-one `(d_j, l_j)` pairs, and
  the per-point eigenvalues — as both displayed tables and machine-readable JSON. GATE V5:
  per-point direct/pencil spectrum identity.
- **P5.6 Verification-statement metadata.** A table of SHA-256 hashes of every P5 script and
  of the four campaign scripts the paper's verification statement will cite
  (`tools/whgap_p2_exact.py`, `tools/whgap_p2_feasibility.py`, `tools/whgap_fable_audit.py`,
  `tools/whgap_fable_audit_ext.py`), plus interpreter and library versions.

## Artifact and closeout

1. Human-readable artifact `artifacts/whgap_p5_derivation_package_20260729.md` with ALL
   displayed formulas in LaTeX-ready blocks (the decision layer will transcribe them into the
   paper's appendices), gates V1–V5 results, and runtimes. Machine data
   `artifacts/logs_whgap_p5_20260729/derivation_package.json`. Scripts `tools/whgap_p5_*.py`;
   all logs + SHA256SUMS.txt under `artifacts/logs_whgap_p5_20260729/`.
2. Node updates: append dated Evidence entries (NO status changes) to
   `WHGAP.signed-lift-extension` and a Work-record line to `WHGAP.goal`; sync the DAG doc's
   "Most recent change" line. Statuses everywhere UNTOUCHED.
3. Both validators exit 0 with the pinned interpreter.
4. Print `FINAL: DONE` or `FINAL: FAILED — <reasons>`.

**Budget box:** <= 75 min compute; any symbolic step > 15 min -> switch to a documented
lower-cost route (e.g. fit at 5 rational x and verify the resulting closed form symbolically)
and note it. Two info-free cycles -> STOP and report.

