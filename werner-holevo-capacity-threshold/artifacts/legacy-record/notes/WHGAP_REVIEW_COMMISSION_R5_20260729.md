# WHGAP review commission R5 (batch) — frozen 2026-07-29 (night, post quota-reset)

Commissioner: decision layer (Fable 5). Reviewers/executor: fresh Opus instances, one per
role, none of whom authored the reviewed work. Interpreter for ALL python:
`C:<home>/cpython3119/python.exe`. New scripts go under `tools/` named
`whgap_r5*_*.py` / `whgap_n1p_*.py`; logs under `artifacts/logs_whgap_r5_20260729/`
(create; end with a `SHA256SUMS.txt` written with LF line endings).

**Mandatory first step for every agent:** execute `research/PRETASK_RELOAD_PROMPT.md`
with {PROBLEM_DIR} = `channel-capacity/werner-holevo-gap`, {NODE_ID} as given per role
below, ROLE as given. Print the PRE-ACTION REPORT at the top of your report/note.

**Single-writer deviation (binding):** to avoid concurrent-write corruption, agents in
this batch do NOT edit node files, NODE_INDEX, or the DAG doc. You write ONLY your own
report/note artifact (immutable) and your own scripts/logs. The decision layer performs
the atomic node/index/DAG updates citing your artifacts immediately after the batch.
This deviation is commissioned here per protocol; note it in your PRE-ACTION REPORT.

## 1. Frozen conventions (identical to P1/P2/P6/P6b)

- Channel: Λ_x(Y) = (1−x)Y + (x/2)(Tr(Y)·1 − Y^T) on qutrits, x ∈ (0,1).
- Kraus: K_0 = sqrt(1−x)·1; K_{μ+1} = sqrt(x/2)·A_μ, (A_μ)_{jk} = ε_{μjk} (μ = 0,1,2).
- Complement (padded, 4-dim): Λ_x^c(Y)_{ab} = Tr(K_a Y K_b^†) = Tr(K_a Y K_b^T)
  (Kraus are real).
- BKM metric at faithful θ with eigendecomposition θ = Σ λ_i |i⟩⟨i|:
  g_θ(Z) = Σ_ij |⟨i|Z|j⟩|² c(λ_i, λ_j), c(a,b) = (log a − log b)/(a−b), c(a,a) = 1/a.
- Isotropy invariant τ(ψ) = |ψ^T ψ|; isotropic stratum τ = 0; canonical representative
  ψ = (e_1 + i e_2)/√2, with ψ̄ its entrywise conjugate.
- Coherent information Ic(ρ) = S(Λ(ρ)) − S(Λ^c(ρ)); Q ≥ Q^(1) = max_ρ Ic(ρ).

## 2. Standing failure-mode list (check each; report which you screened for)

1. sympy `.H` on real-symbolic matrices leaves unresolved `conjugate(sqrt(1−x))` — use
   `.T` for real matrices or strip I-free conjugates; verify any such stripping is sound.
2. WindowsApps store python is inaccessible in sandboxes — use the pinned interpreter.
3. Complement convention drift (3-dim vs padded 4-dim; sign of the a(Y) block; k factor).
4. Transpose vs conjugate-transpose in HS adjoints (real Kraus ⟹ K† = K^T, but only
   after types are audited).
5. `sorted()` on symbolic eigenvalues raises TypeError — sort strings, or subs first.
6. CRLF in SHA256SUMS breaks `sha256sum -c` — write LF.
7. Eigenvalue bookkeeping at degeneracies (divided differences c(a,b) as a→b; interval
   enclosures dividing by near-zero spectral gaps).
8. ε log ε bookkeeping: 0·log 0 = 0; kernel-cluster eigenvalues are ε·(compressed block)
   + O(ε²), and O(ε² log ε) = o(ε) — remainders must be controlled, not waved.
9. Anchoring: verifying a displayed value by re-running the author's script is NOT a
   review. Derive/compute independently FIRST, then compare.

## 3. Rule-7 embeds (binding on every review in this batch)

- **Type audit (7a):** state the type/dimension of every object in the reviewed claims
  (3×3 vs 4×4, state vs observable, superoperator vs matrix, adjoint convention).
- **c ≥ 2 identity gates (7b):** every algebraic identity you confirm must be checked at
  ≥ 2 independent parameter values (distinct rational x, and where relevant distinct ε
  or distinct ψ) OR fully symbolically — say which.
- **Anchoring ban (7c):** perform your own derivation/computation before reading the
  author's numbers; your report must show the independent path (own script, own
  coordinates or own basis where feasible).
- **Frozen-input scope (7d):** you may rely on: the P2/P4 reviewed results (signed-lift
  region = [1/2,1), Q = P = 0 on [1/2,1]), the P3 reviewed results (Q > 0 on (0, x_1),
  x_1 = 0.390910…), and the conventions in §1. Everything else in the repo has only the
  status written on its node — do not treat pending-review claims as established.
- **Standing failure modes (7e):** §2, item by item.
- **Value-vs-formula statement (7f):** for each claim, state explicitly whether you
  verified a VALUE (at specific points) or a FORMULA (identity in x), and what remains
  unverified.
- **Verdict discipline (7g):** your verdict picks exactly one licensing statement from
  your menu, or FINDINGS with an itemized MAJOR/minor list. You were given no desired
  outcome; the menus below are alternatives, not recommendations.

---

## R5a — review of P6 (cBKM order-boundary scan). NODE_ID = WHGAP.order-boundary

**Reviewed inputs (frozen):** `artifacts/whgap_p6_relaxation_20260729.md`;
`artifacts/logs_whgap_p6_20260729/e1_scan.json`, `e1_certificates.json`;
scripts `tools/whgap_p6_common.py`, `whgap_p6_e1_scan.py`, `whgap_p6_e1_certify.py`,
`whgap_p6_d2_soundness.py`, `whgap_p6_s3_feasibility.py` (read, do not re-run wholesale).

**Tasks:**
1. Methodology audit: the cBKM test statistic (T_{Λ^c} − T_Λ generalized eigenproblem),
   the conditioning floor, the restart taxonomy, the directed-interval certification
   route (eigenpair residual / spectral-gap enclosures; degenerate-pair handling).
2. Independent verification (own code, own route): pick ≥ 2 of the 8 rational d_R = 1
   witnesses — MUST include x = 499/1000 — load the rational state and eigendirection
   from `e1_certificates.json`, and recompute the Rayleigh quotient of the BKM
   difference form with your own implementation of c(λ_i,λ_j) at ≥ 60 digits (mpmath),
   confirming strict negativity with a margin you compute yourself.
3. Sanity anchors: your own quick check that at x = 11/20 (certified terrain, P2/P4)
   a short random search finds no violation below −10⁻⁹ (bounded search, ≤ 10 min).
4. Boundary interpretation audit: is the artifact's claim discipline correct (lower
   endpoint certified, upper side bounded-search only; no interpolation)?
   Compute budget ≤ 45 min total.

**Licensing menu:**
- (A) License `WHGAP.order-boundary` NUMERICAL → CERTIFIED\* with scope: "cBKM-order
  violation CERTIFIED at the displayed rational grid points and bisection points down to
  7999/16000 (directed-interval Rayleigh-quotient witnesses); the no-violation side at
  ≥ 1/2 and the bracket upper endpoint remain bounded-search NUMERICAL; exact x_B = 1/2
  is now separately PROVED-track via the P6b necessity theorem (out of this review's
  scope)."
- (B) FINDINGS (itemized MAJOR/minor).

**Report:** `artifacts/whgap_r5a_review_20260729.md`.

---

## R5b — review of P6b-V1 + the paper's necessity section. NODE_ID = WHGAP.order-boundary

**Reviewed inputs (frozen):** paper §5 of
`channel-capacity/werner-holevo-gap/paper/main.tex` (Lemma lem:re-to-bkm, Theorem
thm:necessity, Corollary cor:phase, Remark rem:obstruction); the lead's witness record
on the node (Evidence entry 2026-07-29 late); `artifacts/whgap_p6b_necessity_20260729.md`
§V1; scripts `tools/whgap_p6b_v1_witness.py`, `whgap_p6b_v1_bridge.py` (read them; your
own verification must be an independent script).

**Claims under review (the necessity chain):**
1. Lemma (cRE ⟹ cBKM, second order): if D(N(ρ+tZ)‖N(σ)) − D(M(ρ+tZ)‖M(σ))-type
   domination holds (plain RE domination with all references, as §5 states it), then the
   BKM forms dominate: g_E ≥ g_B on the tangent directions used. Audit the exact
   statement in the paper — the expansion of relative entropy to second order, whose
   Hessian at θ in direction Z is the BKM form; check hypotheses (faithfulness handling
   as ε → 0, differentiability, the direction class).
2. Witness computation: ρ_ε = diag(1−2ε, ε, ε), X = (E_12 + E_21)/√2:
   Λ_x(X) = (1 − 3x/2)X; complement cross-block vanishes for symmetric X and
   Λ_x^c(X) = 0 ⊕ (−x/2)X; g_B = (1 − 3x/2)²/b_ε with b_ε = x/2 + (1 − 3x/2)ε;
   g_E = x/(2(1−ε)); gap identity x/2 − (2/x)(1 − 3x/2)² = 2(1−x)(2x−1)/x.
3. Conclusion: x ≥ 1/2 is NECESSARY for Λ_x^c ⪰ Λ_x in cBKM (hence cRE); with P2/P4
   (frozen input) this yields the phase classification
   cBKM ⟺ cRE ⟺ signed-lift certificate ⟺ x ∈ [1/2, 1].
4. The finite-ε strict-violation family (removes any limit-interchange worry): audit
   that for each rational x < 1/2 there is an explicit ε(x) > 0 with strict BKM
   violation at faithful ρ_ε.
5. λ_5/2 bookkeeping (Remark): the ε → 0 gap equals half the multiplicity-five defect
   Choi eigenvalue 4(1−x)(2x−1)/x; X lies in the spin-2 sector.

**Independent path requirement:** rebuild the witness computation in your own script
(own basis order, own complement assembly from §1), symbolically in (x, ε) where
feasible; check identities per 7b; independently verify the second-order RE ⟹ BKM
expansion on a 2×2 or 3×3 toy example numerically (finite differences of relative
entropy vs the BKM form) at ≥ 2 parameter points, to confirm the Hessian claim.

**Licensing menu:**
- (A) License: "Theorem (necessity): x ≥ 1/2 is necessary for Λ_x^c ⪰_cBKM Λ_x, hence
  for ⪰_cRE — PROVED (written proof in paper §5, exact verification layer PASS,
  independently re-derived in this review); Corollary (phase classification) PROVED
  given frozen P2/P4."
- (B) FINDINGS (itemized MAJOR/minor; state exactly which link of the chain fails).

**Report:** `artifacts/whgap_r5b_review_20260729.md`.

---

## R5c — review of P6b-V2 + P9b digestion. NODE_ID = WHGAP.no-ascent-hierarchy

**Reviewed inputs (frozen):** `artifacts/whgap_p6b_necessity_20260729.md` §V2;
`tools/whgap_p6b_v2_fable.py` (read only); superseded `tools/whgap_p6b_v2_isotropic.py`
+ its failing log (append-only history); the P9b datum
`artifacts/logs_whgap_p9b_20260729/g0_repaired_derivation.json`; the node's
"Decision-layer digestion of P9b" and "P6b-V2 outcome" sections.

**Claims under review:**
1. Definitions: for isotropic ψ, w_B(ψ,φ) = ⟨ψ̄|Λ(φ)|ψ̄⟩, w_E(ψ,φ) = Tr[Π_E(ψ)Λ^c(φ)]
   with Π_E the orthogonal projector onto ker Λ^c(P_ψ) (dimension 2); the weight
   operator D = M_B − M_E with M_B = Λ†(P_ψ̄), M_E = Σ_ab K_a^T (Π_E)_ab K_b, so that
   w_B − w_E = Tr[D φ].
2. Closed forms: D is exactly diagonal in (e_3, ψ̄, ψ) with d_0 = −x(1−x)/(2−x),
   d_1 = (1−x)(2−5x)/(2−x), d_2 = 0; sign rule d_1 > 0 ⟺ x < 2/5; spec Λ(P_ψ) =
   {1−x/2, x/2, 0}; spec Λ^c(P_ψ) = {1−x/2, x/2, 0, 0}.
3. Supersession adjudication: the superseded script's d_1 = 1−x is genuinely wrong (its
   own assembly defect), and the arbitration logic (d_1 = 1−x > 0 would place a
   first-order ascent at proved-zero x ≥ 1/2 — impossible given the expansion lemma
   pattern) plus the numeric x = 9/20 datum diag(−99/620, −11/124, 0) settle it.
4. P9b digestion: (i) D(9/20) ⪯ 0 with ker D = span{ψ} IS the (N1'-a) inequality
   holding at 9/20 with an exact certificate; (ii) the balanced layer is empty there
   (Tr[Dφ] = 0 with D ⪯ 0 forces supp φ ⊆ ker D, i.e. φ = P_ψ); (iii) O(3)-orbit
   transitivity: every isotropic ψ is reachable from (e_1 + i e_2)/√2 by SO(3)×U(1),
   and channel covariance transports D_ψ unitarily, so ONE representative suffices.
   Verify (iii) yourself — it is load-bearing and so far only asserted.
5. Consistency: d_1 ≤ 0 on [2/5, 1) (no first-order isotropic ascent where Q = 0 is
   proved — necessary for coherence); x = 9/20 datum matches the closed form.

**Independent path requirement:** derive D by your OWN construction — e.g. compute
w_B(φ) and w_E(φ) directly as linear functionals on a Hermitian operator basis
(9 Gell-Mann-type directions), assemble D from those values symbolically or at ≥ 3
rational x, and independently fit/prove the closed forms; do NOT start from the
author's M_B/M_E formulas (derive the duality Tr[M_E φ] = Tr[Π_E Λ^c(φ)] yourself).

**Licensing menu:**
- (A) License: "the isotropic weight operator closed form (claims 1–2) is PROVED as an
  algebraic identity (symbolic or c ≥ 3 rational-point verification + own derivation);
  the supersession (claim 3) is correctly adjudicated; the digestion claims 4(i),(ii),
  (iii) hold."
- (B) FINDINGS (itemized MAJOR/minor).

**Report:** `artifacts/whgap_r5c_review_20260729.md`.

---

## E-N1 — executor: write the N1' expansion lemma. NODE_ID = WHGAP.no-ascent-hierarchy

**Role: executor** (this is authorship, not review; the note then goes to R5d fresh).

**Deliverable:** `channel-capacity/werner-holevo-gap/notes/WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md`
— a complete, self-contained rigorous proof note (statement–proof form, every remainder
explicit) of:

**Lemma (isotropic ε log ε expansion).** Let ψ = (e_1 + i e_2)/√2, P = |ψ⟩⟨ψ|, and let
φ be any qutrit state. Set ρ_ε = (1−ε)P + εφ. Then, as ε → 0⁺,
Ic(ρ_ε) = (w_B − w_E)·ε·log(1/ε) + O(ε),
with w_B, w_E as in R5c claim 1, and the O(ε) constant explicit in x and ‖φ‖.

**Theorem (single-letter positivity on (0, 2/5)).** For every x ∈ (0, 2/5),
Q(Λ_x) ≥ Q^(1)(Λ_x) > 0. Proof: take φ = P_ψ̄ = |ψ̄⟩⟨ψ̄|; then w_B − w_E = d_1 =
(1−x)(2−5x)/(2−x) > 0, and the Lemma gives Ic(ρ_ε) > 0 for small ε.
(You may CITE the R5c closed form as an input under review — mark it as such; your
lemma's proof must not depend on it beyond the final numerical value of w_B − w_E.)

**Proof route guidance (use or improve):**
- Base point: Λ(P) and Λ^c(P) are isospectral ({1−x/2, x/2, 0} up to padding zeros),
  so Ic(P) = 0 exactly.
- B side with φ = P_ψ̄ is EXACTLY diagonal: Λ has real coefficients, so
  Λ(P_ψ̄) = conj(Λ(P_ψ)); in the basis (ψ, ψ̄, e_3), Λ(ρ_ε) =
  diag((1−ε)(1−x/2), ε(1−x/2), x/2) — the B-side entropy is in closed form; verify.
- E side: Λ^c(ρ_ε) = (1−ε)Λ^c(P) + εΛ^c(P_ψ̄). Handle the 2-dim kernel cluster with
  explicit degenerate-perturbation bounds: if A ⪰ 0 has kernel K with spectral gap
  g > 0 and B is Hermitian, the eigenvalues of A + εB in the kernel cluster lie within
  ε·spec(Π_K B Π_K) ± C ε² for ε < g/(4‖B‖), with C explicit (prove your bound —
  Schur complement or resolvent; do not cite it as folklore). Then
  −λ log λ = εμ log(1/ε) − εμ log μ + O(ε² log(1/ε)) for λ = εμ + O(ε²), and 0 log 0 = 0
  degeneracies are handled.
- Alternative: if sympy gives exact 4×4 eigenvalues of Λ^c(ρ_ε) in (x, ε), an exact
  route may replace the perturbation bounds — but the written proof must then control
  the branches honestly.
- Include a numerical sanity table (own script `tools/whgap_n1p_sanity.py`): direct
  Ic(ρ_ε) at x ∈ {1/5, 0.395, 9/20} and ε ∈ {10⁻³, 10⁻⁴, 10⁻⁵}, confirming the sign
  pattern (+,+,−·or·0-ish respectively) and the ε log(1/ε) slope against d_1.
- State the corollary landscape honestly: this proves Q > 0 on (0, 2/5) (subsuming
  P3's (0, x_1) with a one-line witness!) and says NOTHING about [2/5, 1/2); the
  "exact onset x_D = 2/5" remains a conjecture about where THIS mechanism ends.

**Cap:** your note is authorship — it licenses nothing by itself; end status
suggestions at CONJECTURED/pending-review for R5d.

---

## R5d — fresh review of the E-N1 lemma note. NODE_ID = WHGAP.no-ascent-hierarchy

**Reviewed inputs (frozen):** the E-N1 note (path passed at dispatch); R5c's closed-form
review report IF already on disk (you may read its verdict but must not rely on it for
your own checks of the lemma's internal steps); the node file.

**Tasks:** full rule-7 review of the lemma note: every inequality and remainder bound
re-derived (7a–7g per §3); the perturbation bound proof checked line by line; the
B-side exact diagonalization verified symbolically; the sanity table reproduced with
YOUR OWN script at ≥ 2 of the 3 x-values; the theorem's dependence structure audited
(does it use only the closed-form value of w_B − w_E from R5c-scope, cleanly cited?).

**Licensing menu:**
- (A) License: "the expansion Lemma is PROVED; the Theorem Q(Λ_x) > 0 for all
  x ∈ (0, 2/5) is PROVED conditional only on the R5c closed form (unconditional if
  R5c verdict is A)."
- (B) FINDINGS (itemized MAJOR/minor).

**Report:** `artifacts/whgap_r5d_review_20260729.md`.

---

## Batch deliverable format

Each agent returns a structured verdict: {verdict: LICENSE_A | FINDINGS | DONE |
BLOCKED, summary, majors[], minors[], report_path}. Reports are immutable once written.
The decision layer will: adjudicate, perform all node/index/DAG/status updates citing
the reports, decide paper v4, run validators, and commit (local only; the user pushes).

