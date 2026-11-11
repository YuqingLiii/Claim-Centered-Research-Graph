# WHGAP commission LEAN-2 — closing the two project-specific Lean gaps + the minimal entropy layer (frozen 2026-07-31)

Commissioner: decision layer (Fable 5; statements and routes below are mine — derive and
verify, do not trust). Executors: fresh Opus 5 instances, ONE PER WORK PACKAGE,
dispatched SEQUENTIALLY (WP-A → WP-B → WP-C), each ending with a green build so the
decision layer can checkpoint-commit between packages. Node (rule 8a): the gap analysis
motivating this is recorded on `WHGAP.goal` (un-Leaned residue: the 27×27 spectrum
derivation; the eps-log-eps expansion; the entropy-collapse step).

**T3 AUTHORIZATION (protocol §7.8 requires a lead directive):** lead, 2026-07-31,
verbatim: 「建立吧 增就增加了 问题不大 你执行的时候交给opus」 — the minimal
quantum-entropy library layer (WP-C) is authorized.

**Mandatory first step (every WP):** `research/PRETASK_RELOAD_PROMPT.md` with
{PROBLEM_DIR} = `channel-capacity/werner-holevo-gap`, {NODE_ID} = `WHGAP.goal`, ROLE =
executor; then read `research/DAG_PROTOCOL.md` §7 and the project README. Single-writer
deviation binding (no node/index/DAG markdown). SCOPE: WHGAP paths only; never touch
`tools/proof_dag_check.py` or the se/ksum trees.

**Project:** `channel-capacity/werner-holevo-gap/proof-dag/lean/` (whgapDag; Lean
v4.31.0 + Mathlib v4.31.0 cache — do not rebuild Mathlib). Standing rules: NEVER
`sorry` (unclosable ⟹ explicit hypothesis parameter, documented); no `native_decide`;
frozen-claim hashes untouched unless a node Claim changes (they do not here); after
every package: full clean rebuild, `#print axioms` (three standard axioms only),
forbidden-construct scan, `tools/whgap_lean_freeze_claims.py --check`,
`tools/lean_dag_check.py --problem werner-holevo-gap` (the authoritative §7.6 gate),
run artifacts under `artifacts/logs_whgap_lean2_20260731/` (LF SHA256SUMS, append-named
per package), and an appended dated section in a shared report
`artifacts/whgap_lean2_20260731.md`. Interpreter for any sympy codegen:
`C:<home>/AppData/Local/Microsoft/WindowsApps/python.exe`.

---

## WP-A — the spectrum theorem's basis-free core, as a COMPLETE identity proof

**Target (extends `WHGAP/«signed-lift-extension».lean` or a new
`WHGAP/Support/DefectChoi.lean` serving it):** the annihilating identity and both trace
identities of paper Thm 3.3's proof, as identities in x on (0,1):

  C_x (C_x − λ₅(x)·1) (C_x − λ₃(x)·1) = 0,
  Tr C_x = 5λ₅ + 3λ₃,   Tr C_x² = 5λ₅² + 3λ₃²,
  with λ₅ = 4(1−x)(2x−1)/x, λ₃ = 16(1−x)(3x−1)/(9x).

These fix the spectrum {0^19, λ₅^5, λ₃^3} without any basis choice (given symmetry +
distinctness — the consequence layer is the stretch goal below).

**Frozen route (PIT — this makes it a complete proof, not sampling):**
1. Define M(x) := x·C_x with ENTRIES AS EXPLICIT POLYNOMIALS of degree ≤ 2 in x, via the
   forced-point master formula (paper App A, eq:master, the 15 delta patterns with their
   forced coefficients — multiply each displayed c_k by x and verify the result is a
   polynomial; cross-generate the table with sympy from the App A display and CHECK
   degree ≤ 2 before writing any Lean).
2. Clear denominators: the annihilator ⟺ M(M − p₅·1)(M − p₃·1) = 0 where
   p₅ := x·λ₅ = 4(1−x)(2x−1), p₃ := x·λ₃ = 16(1−x)(3x−1)/9 — both polynomials
   (deg 2). Every entry of the triple product is a polynomial of degree ≤ 6.
3. Evaluate the triple product at SEVEN distinct rationals (include the paper's sample
   points 26/51, 4/7, 3/4; avoid 0) in exact ℚ matrix arithmetic, entry-wise zero.
4. Conclude for ALL x by the interpolation lemma: a polynomial of natDegree ≤ 6
   vanishing at 7 distinct points is 0 (Mathlib:
   `Polynomial.eq_zero_of_natDegree_lt_card_of_eval_eq_zero` or equivalent — find the
   exact name). Same for the traces (deg ≤ 2 → 3 points; deg ≤ 4 → 5 points).
   Implementation freedom: you may represent per-entry polynomials via sympy-GENERATED
   Lean source (mechanical, auditable) if that is what makes the evaluations tractable;
   performance is the main risk — batch `norm_num`/`decide` prudently and time a pilot
   entry before generating 729.
5. **Stretch (do not force):** the consequence layer — C_x symmetric (entry-level check
   from the master formula) + annihilator + traces + λ₅ ≠ λ₃ ≠ 0 (generic x; state the
   coincidence points) ⟹ eigenvalue multiset = {0^19, λ₅^5, λ₃^3} via the spectral
   theorem for symmetric matrices and the 3-equation multiplicity solve.
**Degradation path (documented, never sorry):** if the 27×27 evaluations are
computationally infeasible in Lean, land (a) the three identities verified at the seven
points as standalone theorems + (b) the interpolation meta-lemma + (c) the degree-bound
statement as an explicit hypothesis `hdeg`, and SAY exactly which leg is conditional.

**Gate GA:** build green; the three identities' theorems have no hypotheses beyond
0 < x < 1 (or the documented hdeg degradation); axioms clean; lean_dag_check green.

---

## WP-B — the expansion theorem for the witness family, as scalar real analysis

**Target (extends `WHGAP/«no-ascent-hierarchy».lean` + `WHGAP/Support/IcScalar.lean`):**

1. Matrix identification layer (easy, do first): with β a variable, hβ : β² = x(1−x)/2 —
   the B-side output of the §6 witness is diagonal with entries
   ((1−ε)(1−x/2), ε(1−x/2), x/2) in the (ψ, ψ̄, e₃) frame (state as mulVec
   eigen-equations for the EXPLICIT 3×3 matrix); the E-side 4×4 splits into blocks
   A(ε) = !![1−x, −β(1−2ε); −β(1−2ε), x/2] (real stand-in, invariants already proved in
   LEAN-1) ⊕ B-block with entries giving spec {x(1−ε)/2, xε/2}; charpoly of A(ε) =
   X² − (1−x/2)X + 2x(1−x)ε(1−ε).
2. Define the scalar coherent information via `Real.negMulLog`:
   IcScalar x ε := [Σ negMulLog over the B-list] − [Σ negMulLog over the E-list], with
   λ±(x,ε) = ((1−x/2) ± √((1−x/2)² − 8x(1−x)ε(1−ε)))/2 (Real.sqrt is fine here — this
   is analysis, not identity-checking; prove the discriminant is ≥ 0 on the domain and
   λ± ≥ 0).
3. **MAIN THEOREM (must land):** ∀ x, 0 < x → x < 2/5 → ∃ ε, 0 < ε ∧ ε < 1 ∧
   0 < IcScalar x ε. Route guidance (mine — improve freely): the paper's leading-term
   argument with explicit bounds; key scalar facts: negMulLog(εc) = εc·log(1/(εc));
   λ₋ ∈ [detA/TrA, 2·detA/TrA]-type brackets via √(a²−b) ∈ [a − b/a, a] for
   0 ≤ b ≤ a²; the d₁ = (1−x)(2−5x)/(2−x) > 0 fact is already in the module. You do NOT
   need the uniform-in-φ remainder — one witness family, one explicit ε(x), suffices.
4. Wire it: replace/complement `exists_pos_of_expansion` so that P9's Lean content no
   longer NEEDS the abstract hexp for this family — the new theorem carries its own
   proof. hexp stays for the general statement; document the relation.
**Gate GB:** the main theorem lands sorry-free with hypotheses ONLY 0 < x < 2/5 (any
residual analytic step as a named explicit hypothesis is the documented degradation, and
the report must say precisely which inequality resisted); build green; axioms clean.

---

## WP-C — the minimal von Neumann entropy layer (T3, lead-authorized above)

**Target (new `WHGAP/Support/Entropy.lean` + extending `WHGAP/«private-boundary».lean`):**

1. Definition: for A : Matrix (Fin n) (Fin n) ℝ with hA : A.IsHermitian,
   vnEntropy hA := Σ i, Real.negMulLog (hA.eigenvalues i). (Real symmetric suffices for
   everything we touch; document that complex-Hermitian generality is NOT claimed.)
2. Core lemmas (in order of need):
   (a) eigenvalues of an explicit DIAGONAL matrix = its diagonal entries as a multiset
       (route: charpoly of diagonal = Π(X − dᵢ) + the Hermitian-eigenvalues/charpoly
       characterization; find the Mathlib API — `Matrix.charpoly_diagonal`?
       `Matrix.IsHermitian.eigenvalues`-vs-roots glue);
   (b) invariance under explicit orthogonal conjugation: for U with U·Uᵀ = 1,
       vnEntropy(U·D·Uᵀ) = vnEntropy(D) (route: charpoly invariance under conjugation);
   (c) block-diagonal additivity at the explicit 2⊕2 level.
3. **Payoff theorem (must land):** for the §7 witness ensembles — the four explicit
   commuting output matrices of paper Lemma 7.1 (B side: 3×3 diagonal-in-frame with
   entries {α, b±u}; E side: 4×4 with entries {1−x, xε, e±v}) —
   χ_B := vnEntropy(avg_B) − ½ vnEntropy(out_B₊) − ½ vnEntropy(out_B₋) = b·f(u/b), and
   χ_E = e·f(v/e), with f as in the existing module. This discharges paper Lemma 7.1 in
   Lean; `Claim_of_delta_le`'s hbridge then reduces to EXACTLY Devetak's formula
   (interface) — state that reduction as a new theorem and update the module docstring's
   honesty note accordingly.
4. If (a)/(b) resist the Mathlib API within budget: land the diagonal case completely
   and carry the conjugation lemma as an explicit hypothesis `hconj`, documented.
**Gate GC:** payoff theorem lands (unconditional, or conditional ONLY on the documented
hconj); build green; axioms clean; the P14 docstring/README honesty layer updated to the
new, smaller trust boundary.

---

Per-package return: {status, summary, built, sorry_count, axioms_clean, gate_ok,
conditional_hypotheses: [names], report_path}. Budget ≤ 120 min each. Review R12
(fresh instance, §7.10 + the new content) follows after all three land — commissioned
separately by the decision layer.

