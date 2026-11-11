# WHGAP commission P2 — covariant signed-lift continuation past x = 1/2 (2026-07-28)

**Nodes (rule 8a):** target `WHGAP.signed-lift-extension`; parent recompute `WHGAP.goal` (stays OPEN
per the 2026-07-28 adjudication regardless of outcome). Do not touch any other node's status.
**Executor:** codex CLI, ONE sequential session, workspace-write sandbox, NO network.
**Python (every invocation):** `"C:<home>/cpython3119/python.exe"` — CPython 3.11.9 with the
pinned stack numpy 1.26.4, scipy 1.14.1, sympy 1.13.1, mpmath 1.3.0, cvxpy 1.6.0, scs 3.2.7
(sandbox-verified 2026-07-28; the WindowsApps store path is unresolvable in your sandbox — never
use it).
**Status discipline (rules 6/7):** this commission may write AT MOST `NUMERICAL` with an explicit
`pending-review:` marker on `WHGAP.signed-lift-extension`. NO CERTIFIED*/PROVED/REFUTED anywhere.
A separate rule-7 review commission decides completion later.

## Step -1 — mandatory pre-task reload

Execute `research/PRETASK_RELOAD_PROMPT.md` FIRST with {PROBLEM_DIR} =
`channel-capacity/werner-holevo-gap`, {NODE_ID} = `WHGAP.signed-lift-extension`, ROLE = executor.
Print the PRE-ACTION REPORT before any work. Disk overrides this commission on any conflict —
report, never silently resolve.

## Frozen conventions — use EXACTLY; deviation = STOP and report

Carried over from P1 (all six calibration facts C1–C6 passed exact verification and survived the
completed R1 review `artifacts/whgap_p1_review_20260728.md` — frozen inputs in reviewed scope):

- Family `Lambda_x(X) = (1-x) X + (x/2)(Tr(X) 1_3 - X^T)`; Kraus `K_0 = sqrt(1-x) 1_3`,
  `K_{mu+1} = sqrt(x/2) A_mu`, `(A_mu)_{jk} = epsilon_{mu j k}` (indices in {0,1,2});
  complementary `(Lambda_x^c(X))_{ab} = Tr(K_a X K_b^dag)` on `H_E = C^4`, a,b in {0..3}.
- `a(Y) := (Y_12 - Y_21, Y_20 - Y_02, Y_01 - Y_10)^T` (Zhu–Wang Eq. (4.8) ordering).
- Operator decomposition (their Eq. (4.2)): `X = (TrX/3) 1 + S + T`, `S^T = S` traceless,
  `T^T = -T`. Diagonal action: `Lambda_x` has eigenvalues `1` (scalar), `1 - 3x/2`
  (symmetric-traceless, dim 5), `1 - x/2` (skew, dim 3). Verify these from the definition.
- Zhu–Wang x=1/2 lift (their Eq. (4.12)):
  `J(Y) = (1/3) [[Tr Y, sqrt(2) a(Y)^T], [-sqrt(2) a(Y), 2 Tr(Y) 1_3 - Y - 2 Y^T]]`,
  adjoint preserving, `J^dag ∘ Lambda^c = Lambda` at x=1/2 (their Lemma 4.1), NOT positive.
- Defect (their Eqs. (4.18)–(4.20)): with the HS identification `E_jk <-> |j>|k>` of
  `L(H_B) ≅ H_B ⊗ H_B'`,
  `Delta(tau) = L_{Lambda(tau)} - J^dag ∘ L_{Lambda^c(tau)} ∘ J`, and at x=1/2 it equals
  `(2/9) sum_mu G_mu tau G_mu^dag`, `G_mu |i> = |i>|mu> + (1/2)|mu>|i> - (1/2) delta_{mu i} sum_j |j>|j>`;
  entrywise closed form in their Eq. (A.2).
- Sufficient criterion (their Theorem 3.3, generic in the channels; cite, do not re-prove):
  IF `M(1) ≻ 0`, `N(1) ≻ 0`, `J` adjoint-preserving with `J^dag ∘ N = M`, and
  `Delta_J(tau) = L_{M(tau)} - J^dag ∘ L_{N(tau)} ∘ J` is CP in `tau`, THEN `N ⪰_cBKM M`;
  their Lemma 3.2 + tensorization (HRSF22) then give `Q = P = 0` for M at every blocklength.
  For us `M = Lambda_x`, `N = Lambda_x^c`. Hypothesis 1 must be VERIFIED for general x
  (expect `Lambda_x(1) = 1`, `Lambda_x^c(1) = diag(3(1-x), x, x, x)`, both ≻ 0 on 0 < x < 1).
- Local literature: the Zhu–Wang PDF at
  `channel-capacity/literature/papers/zhu-wang-2026-quantum-incapacity/arxiv_2607.24693.pdf`
  (NOTE: encrypted with empty password — extract text via pypdf `decrypt('')` if needed; a
  plain-text extraction already exists at the decision layer, but re-derive all math from the
  frozen statements above, not from prose).

## New objects for this commission

- **General-x complementary channel (derive and verify exactly):**
  `Lambda_x^c(X) = [[(1-x) TrX, k(x) a(X)^T], [-k(x) a(X), (x/2)(TrX 1_3 - X^T)]]` with
  `k(x) = sqrt((1-x) x / 2)`; must reproduce their Eq. (4.9) at x=1/2. Derive the HS adjoint
  `(Lambda_x^c)^dag` (general-x analog of their Eq. (4.11)).
- **Equivariant lift ansatz (5 real parameters p, q, c1, c2, c3):**
  `J_x(Y) = [[p TrY, q a(Y)^T], [-q a(Y), c1 TrY 1_3 + c2 Y + c3 Y^T]]`.
  Real coefficients ⇒ adjoint preserving (verify symbolically via `a(Y^dag) = -conj(a(Y))`).
  At x=1/2 the Zhu–Wang J is `(p,q,c1,c2,c3) = (1/3, sqrt(2)/3, 2/3, -1/3, -2/3)`.
- **Residual family:** impose `J_x^dag ∘ Lambda_x^c = Lambda_x` symbolically. By Schur (scalar /
  vector / quint sectors) this is 3 linear equations in the 5 parameters ⇒ a 2-parameter residual
  family `J_{x,s1,s2}` (choose and DOCUMENT an explicit parameterization; verify the x=1/2 point
  recovers Zhu–Wang's values for specific (s1, s2)).
- **Defect Choi:** `C(x,s1,s2) := Choi(Delta_{J_x})` on `H_A ⊗ (H_B ⊗ H_B')`, 27×27, real
  symmetric with entries polynomial in (x, s1, s2) after clearing `k(x)` (verify only even powers
  of k survive, else keep `k` as a symbol with `k^2 = (1-x)x/2`). CP(Delta) <=> C ⪰ 0.
- **Spin-block reduction:** the diagonal SO(3) action on `3 ⊗ 3 ⊗ 3` decomposes as
  spin multiplicities {spin0: 1, spin1: 3, spin2: 2, spin3: 1}. Build EXACT rational/sqrt-free
  isometries onto multiplicity spaces (Appendix-B style); C block-diagonalizes into blocks of
  sizes 1, 3, 2, 1 (each spin's multiplicity space; entries symbolic in x, s1, s2).
  MANDATORY check: direct 27×27 congruence at sample rational points equals the block spectra.

## Step 0 — calibration gates (exact sympy)

- D1. General-x: `Lambda_x(1) = 1`; `Lambda_x^c(1) = diag(3(1-x), x, x, x)`; the three
  diagonal-action eigenvalues `(1, 1-3x/2, 1-x/2)`; `Lambda_x^c` reproduces Eq. (4.9) at x=1/2.
- D2. Ansatz adjoint-preservation (symbolic Y, general real parameters).
- D3. Intertwining solved: rank of the linear system = 3 for all x in (0,1) (or name the
  exceptional x); residual 2-parameter family explicit; x=1/2 recovers Zhu–Wang's J.
- D4. Defect Choi at x=1/2, Zhu–Wang (s1,s2): equals `(2/9) sum_mu Choi(G_mu · G_mu^dag)`
  entrywise (their Eq. (A.2)); PSD with rank exactly 3; spin blocks reproduce the same spectra.

**GATE G0:** ALL of D1–D4 exact -> proceed. ANY failure -> STOP, artifact naming the failure.

## Step 1 — exact feasibility region and x_max

- S1. Per-block PSD conditions: for each spin block, exact PSD characterization in (x, s1, s2)
  (1×1 and 2×2 blocks: sign/determinant conditions; 3×3: leading principal minors of a symmetric
  matrix are NOT a PSD test at boundary — use all principal minors or eigen/LDL reasoning; be
  exact).
- S2. **x_max computation:** `x_max = sup { x in [1/2, 1) : exists (s1,s2) with all blocks ⪰ 0 }`.
  Try full symbolic quantifier elimination first (resultants / discriminants / sympy solve on
  boundary systems). If symbolic x stalls (> ~15 min), fall back: exact per-x feasibility at the
  rational grid x in {1/2, 26/51, 13/25, 27/52, 27/50, 5/9, 4/7 - 1/1000, 4/7, 4/7 + 1/100, 3/5,
  2/3, 3/4} plus adaptive exact bisection on x_max to width <= 1/10^4, then NUMERICAL refinement
  of x_max to 1e-8 (scipy/mpmath on the block minimal-eigenvalue maximin). Log which route ran.
- S3. Also compute x_min (the lower reach below 1/2) on [1/4, 1/2] — same method, coarser grid.
- S4. At three certified interior rational points (choose in the feasible range, e.g. the largest
  feasible grid x): produce EXPLICIT exact rational (or minimal-surd) `(s1, s2)` together with
  exact PSD proofs of all four blocks (LDL/congruence over Q or Q(sqrt)) — these are the exact
  certificates that make the extension claim checkable without any solver.
- S5. Twirling-WLOG ingredients (verify exactly; the lemma write-up itself is decision-layer
  work, NOT yours to claim): (i) covariance identities `Lambda_x(O X O^T) = O Lambda_x(X) O^T`
  and `Lambda_x^c(O X O^T) = V(O) Lambda_x^c(X) V(O)^T` with an explicit `V(O)` you derive
  (attend to the epsilon-tensor det(O) twist), verified symbolically for a generic one-parameter
  rotation and for a generating set of the octahedral group; (ii) the congruence-convexity
  inequality `((J1+J2)/2)^dag L ((J1+J2)/2) ⪯ (J1^dag L J1 + J2^dag L J2)/2` for L = left
  multiplication by a PSD operator — symbolic proof via the expansion of
  `((J1-J2)/2)^dag L ((J1-J2)/2) ⪰ 0`, plus exact random-instance checks.

**GATE G1 (sanity):** x=1/2 is feasible (D4 point) AND feasibility is not empty on a right
neighborhood (x = 26/51 or finer) — otherwise the certificate is rigid at 1/2; record and go to
the artifact (this IS pre-registered outcome (c), not a failure).

**GATE G2 (pre-registered interpretations; STOP after artifact + node updates in every case):**
- (a) `x_max >= 4/7` (exact or numeric-with-exact-sample-certificates) -> finding: "covariant
  signed-lift certificates cover [1/2, 4/7]; gap closure candidate — pending review and
  decision-layer write-up of the generic-theorem application".
- (b) `1/2 < x_max < 4/7` -> finding: "signed-lift extension reaches exactly/numerically x_max;
  method delimited below 4/7" (record exact x_max if obtained).
- (c) feasibility only at x = 1/2 -> finding: "the Zhu–Wang certificate is rigid within the
  covariant family".

## Artifact and closeout (mandatory)

1. Artifact `artifacts/whgap_signed_lift_extension_20260728.md`: derivations summary (residual
   family), block structures, feasibility table over the grid, x_max (exact form if achieved,
   plus 1e-8 numeric), x_min, the three exact interior certificates (parameter values + block
   LDL data or a pointer to a machine-readable JSON), twirling-ingredient verification results,
   runtimes, and the G2 interpretation. Scripts under `tools/` (`whgap_p2_*.py`); ALL logs under
   `artifacts/logs_whgap_p2_20260728/` with `SHA256SUMS.txt` covering every script and log.
2. Node closeout per DAG protocol §5–§6: dated Work record + Evidence on
   `channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.signed-lift-extension.md`; status at
   most `NUMERICAL` + `pending-review:`; `WHGAP.goal` untouched (stays OPEN); sync NODE_INDEX row,
   mermaid label, outline, "Most recent change" in `notes/WERNER-HOLEVO-GAP_PROOF_DAG.md`.
3. Both validators exit 0 with the pinned interpreter:
   `tools/proof_dag_check.py --problem werner-holevo-gap` and `tools/literature_check.py`.
4. Print `FINAL: DONE` or `FINAL: FAILED — <reasons>`.

**Budget box:** <= 75 min compute total; any single symbolic step > 15 min -> switch to the
documented per-x fallback and note it. Two info-free cycles -> STOP and report
(capability-boundary stop-loss).

