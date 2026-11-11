# WHGAP commission LEAN-3 — formalize the remaining gaps (frozen 2026-08-01)

Commissioner: decision layer. Lead directive 2026-08-01: continue formalizing the
residual gaps notwithstanding diminishing returns (「形式化一下啊」). Executors: fresh
Opus 5, one per work package, SEQUENTIAL (WP-F → WP-E → WP-D), checkpoint commits by the
decision layer between packages. Node (rule 8a): `WHGAP.goal` (the un-Leaned-residue
analysis and every honesty note this closes are recorded there and in Trust.lean's
"Definitional-identification residuals" section).

Standing rules (same as LEAN-2): pre-task reload with {NODE_ID} = WHGAP.goal; DAG
protocol §7 read in full; NEVER sorry (unclosable ⟹ named explicit hypothesis,
documented); no native_decide; WHGAP paths only; single-writer deviation; per-package
closeout = clean rebuild + #print axioms (3 standard only) + forbidden scan +
freeze-check + lean_dag_check green + logs under `artifacts/logs_whgap_lean3_20260801/`
(LF-normalized SHA ledger WITH the convention header, per R12 m7) + appended dated
section in `artifacts/whgap_lean3_20260801.md`. Commit subjects by the decision layer
will say "machine-checked", never "PROVED" (R12 m8). Performance discipline: pilot-time
any 27×27 kernel reduction before committing to a route (WP-A precedent: 6m25s per
product — the routes below are designed to avoid all large products; if you must exceed
ONE such product, stop and document).

---

## WP-F — small closures (hours; do first)

1. **hsq discharged:** prove `f_ge_sq : ∀ s, 0 ≤ s → s < 1 → s^2 ≤ f s` (route:
   g(s) = f(s) − s², g(0) = 0, deriv g = log(1+s) − log(1−s) − 2s ≥ 0 via the same
   StrictMonoOn machinery f_pos used; or any sound route). Then restate
   `Delta_lower_bound` UNCONDITIONALLY and remove hsq from Trust.lean's census
   (append-only note of the removal).
2. **Lemma 4.1 algebraic core (the x = 1 self-complementarity):** with the minimal Kraus
   set A_μ/√2 (3-dim environment), prove the entrywise identity
   (Λ₁^{c,min}(X))_{μν} = ½ Tr(A_μ X A_νᵀ) = (Λ₁(X))_{μν} for all X — pure ring on 3×3.
   New small module or extend Support. Scope note: this machine-checks the paper's
   Lemma 4.1 DISPLAY; the capacity conclusion via the ZW interface stays interface.
3. **§5 witness scalars (cheap, optional if time):** the trivial-reference BKM values of
   the necessity witness as scalar definitions per the paper's eigenbasis formula:
   g_B = (1−3x/2)²/b_ε, g_E = x/(2(1−ε)), and the finite-ε strict-violation inequality
   x·b_ε − 2(1−3x/2)²(1−ε) < 0 for 0 < ε < ε_c(x) (the factorization is already in the
   order-boundary module — wire, don't duplicate).

## WP-E — the eigenvalue multiset, completed (charpoly route via small certificates)

**Target:** `charpoly_Cmat : (Cmat x).charpoly = X^19 * (X − C λ₅)^5 * (X − C λ₃)^3`
for all x ≠ 0 — closing R12 m6's spectral-theorem residual and upgrading the WP-A core
to the full multiset statement (valid at ALL x including the coincidence points, where
the multiset merges consistently).

**Frozen route (small certificates only — no large kernel products):**
1. sympy-compute a RATIONAL kernel basis K (27×19) with V₅ᵀK = 0 and V₃ᵀK = 0
   (both SMALL decidable checks: 5×19 and 3×19 zeros), plus an explicit rational S⁻¹ for
   S := [W₅ | V₃ | K].
2. Q₅S and Q₃S need NO big products: Q₅W₅ = W₅ and Q₃W₅ = 0 follow from the EXISTING
   small certificates (V₅ᵀW₅ = 12·𝟙, V₃ᵀW₅ = 0); Q₅V₃ = 0, Q₃V₃ = V₃ likewise
   (V₅ᵀV₃ = 0, V₃ᵀV₃ = 16·𝟙); Q₅K = Q₃K = 0 from step 1's certificates. Hence
   C·S = S·D with D = diag(λ₅𝟙₅, λ₃𝟙₃, 0₁₉) by the WP-A decomposition — matrix algebra,
   no entrywise 27×27 reduction.
3. The ONE allowed expensive step: certify S⁻¹·S = 𝟙 (a single rational 27×27 product;
   pilot-time it; if > ~8 min, generate the 729 entry checks by codegen + batched
   norm_num instead of decide).
4. charpoly invariance under similarity (find the Mathlib lemma; fallback: det
   multiplicativity over ℝ[X] with the explicit S, S⁻¹) + charpoly of the explicit
   diagonal = the product. Update multiplicity_unique's docstring: the previously
   unformalized step is NOW formalized; the {1/3, 1/2, 5/6} exclusion note becomes moot
   for the charpoly statement (say so).

## WP-D — the identification layer (the big one; closes Trust's three definitional residuals)

**Target module `WHGAP/Support/Channel.lean` + wiring:** define IN LEAN, as explicit
finite linear algebra: the Kraus set (K₀ = t·𝟙, K_{μ+1} = s·A_μ with hs : s² = x/2,
ht : t² = 1−x; A_μ the Levi-Civita matrices); Λ_x(X) := Σ K_a X K_aᵀ (real X suffices —
verify against the closed form (1−x)X + (x/2)(Tr X·𝟙 − Xᵀ) as an entrywise lemma);
the padded complement Λ^c(X)_{ab} := Tr(K_a X K_bᵀ) (4×4; verify the block closed form
eq:comp with β = s·t); the forced-point lift J (block form eq:Jintro with q carried
under hq : 9q² = 2(1−x)/x → as rational combinations of s, t — derive the right chart);
the HS adjoint J†; the defect Δ_J(τ)(Y) = Λ(τ)·Y − J†(Λ^c(τ)·J(Y)); its Choi on the
existing Fin 27 index encoding. Then prove:
1. **`choi_defect_eq_Cmat`** : the Choi of Δ_J at the forced point equals
   `DefectChoi.Cmat x` — entrywise (this is EXACTLY the bridge R12 verified 729/729 in
   sympy; sympy-codegen the entry goals; the s,t,q dependencies must cancel to rational
   functions — if an entry resists field_simp+ring, check the chart before suspecting
   the math).
2. **`outB_eq / outE_eq`** : the §7 ensemble outputs — Λ(ρ_ε ± tX) and Λ^c(ρ_ε ± tX)
   for the DIAGONAL witness ρ_ε = diag(1−2ε, ε, ε), X = (E₁₂+E₂₁)/√2 (carry r with
   hr : r² = 2) — equal «private-boundary».outB/outE entrywise. This DISCHARGES
   residual (c) of Trust's definitional-identification section.
3. **`specB_charpoly / specE_charpoly`** : the §6 witness outputs Λ(ρ_ε), Λ^c(ρ_ε) for
   ρ_ε = (1−ε)P_ψ + εP_ψ̄ (COMPLEX matrices — work over ℂ here; the P_ψ entries are
   explicit) have charpoly = Π(X − λᵢ) over IcScalar's eigenvalue lists. This discharges
   residual (b) at the charpoly level (the entropy layer stays real-symmetric; state the
   remaining glue honestly: "spectrum-as-multiset ⟹ vnEntropy value" for the complex
   case is NOT re-proved — scope note).
4. Update Trust.lean's residuals section: (a) Cmat ↔ defect Choi = CLOSED (item 1);
   (c) outB/outE = CLOSED (item 2); (b) specB/specE = closed at charpoly level with the
   stated complex-entropy glue note. Update the README's "what a green build does NOT
   establish" list accordingly — the coding-theorem interfaces and §4 entropy assembly
   remain, and SAY SO.

Budgets: WP-F ≤ 60 min; WP-E ≤ 90 min; WP-D ≤ 150 min. Per-package return
{status, summary, built, sorry_count, axioms_clean, gate_ok, conditional_hypotheses,
report_path}. R13 (fresh §7.10 review of the whole LEAN-3 batch) follows, commissioned
by the decision layer.

