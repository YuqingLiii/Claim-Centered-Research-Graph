/-
`KsumAudit/RosmanisBarrier.lean` — tier **T2**, the Rosmanis barrier.

Proof-DAG node: `KSUM.LEAN.T2.rosmanis-kfloor` (registered OPEN under rule 8a, 2026-07-30).
This module is audit-tier content, NOT a DAG-node mirror (module names in the `KsumAudit` library
are Lean names, per `lakefile.lean`).

Manuscript target: `prop:rosmanis`, `ksum/paper/ksum_small_alphabet.tex`, `sec:barriers`,
subsection "Rosmanis's mechanism does not transfer".

  part (1)  orbit parametrization of the negative set `D₀`, and the orbit count `≥ 2`
  part (2)  regularity fails — the two explicit finite witnesses
  part (3)  positive blocks empty when `τ = 0`

**No `QueryModel`, no interface hypothesis: everything here is unconditional finite combinatorics.**

════════════════════════════════════════════════════════════════════════════════════════════════
  SCOPE — what is and is NOT formalized (read before citing this module)
════════════════════════════════════════════════════════════════════════════════════════════════

FORMALIZED, in the **orbit-proper** sense (not merely as an invariant-class statement):

* the characterization of `D₀` that the manuscript's proof runs on — *(a) each fixed-point value
  occurs at most once, (b) for each `2`-cycle only one of its two sides ever occurs*
  (`isNegative_iff`) — together with the bridge to the paper's own object,
  `D₀ = {x : 2Sum_{Z_q,t,N}(x) = 0}` (`isNegative_iff_twoSum_false`);
* the `S_N × C(σ)` ACTION itself, and the fact that it preserves `D₀` (`isNegative_act`);
* an action-INVARIANT (`valueCount_act`), from which *"`D₀` is never a single orbit"* / *"there are
  at least two orbits"* follows as a statement about GENUINE ORBITS, in both of the manuscript's
  branches: `m ≥ 2` (`two_orbits_of_two_cycles`) and `m = 1`, `τ ≥ 1`
  (`two_orbits_of_one_cycle`), assembled by `not_single_orbit`;
* part (3), `positive_blocks_empty`.

NOT FORMALIZED — declared, not silently omitted:

* the **bijection** `orbits ↔ {(f, λ)}` and the resulting **count formula** `Σ_f p_{≤m}(N-f)`.
  Only its consequence `≥ 2` is proved, and it is proved directly rather than by evaluating the
  formula.  Anyone needing the exact orbit count must NOT cite this module.
* part (2)'s **representation-theoretic** sentence (*"in a permutation module `C[X]` the
  multiplicity of the trivial representation equals the number of orbits"*).  Only part (2)'s two
  finite witnesses are mechanized (`existence_fails_q3`, `uniqueness_fails_q5`), which is exactly
  the split the node's Scope section asked for.
* the structure theorem `C(σ) ≅ (C₂ ≀ S_m) × S_τ`.  `Centralizer` below is the centralizer as
  DEFINED (permutations commuting with `σ`), which is what every proof here uses; the
  wreath-product identification is neither needed nor proved.

House rules: no `sorry`, no `axiom`, no `native_decide`.
-/
import KsumAudit.Defs
import Mathlib.Data.Fin.VecNotation
import Mathlib.Logic.Equiv.Basic

namespace KsumAudit
namespace Rosmanis

open Finset

variable {V : Type*} [DecidableEq V]

/-! ## 1. The negative set `D₀` -/

/-- `x` is a **negative** input for the involution `σ`: no two distinct positions carry a value
and its `σ`-partner.  For `σ(a) = t - a` this is exactly `2Sum_{G,t,N}(x) = 0`
(`isNegative_iff_twoSum_false`). -/
def IsNegative (σ : V → V) {N : ℕ} (x : Fin N → V) : Prop :=
  ∀ i j : Fin N, i ≠ j → x j ≠ σ (x i)

instance {σ : V → V} {N : ℕ} (x : Fin N → V) : Decidable (IsNegative σ x) := by
  unfold IsNegative; infer_instance

/-- The bridge to the paper's own object: `D₀` really is the negative set of `2Sum`. -/
theorem isNegative_iff_twoSum_false {q N : ℕ} (t : ZMod q) (x : Fin N → ZMod q) :
    IsNegative (fun a => t - a) x ↔ twoSum (ZMod q) t N x = false := by
  rw [Bool.eq_false_iff, Ne, twoSum_iff]
  constructor
  · rintro h ⟨i, j, hij, hsum⟩
    exact h i j hij (by rw [← hsum]; ring)
  · intro h i j hij hxj
    exact h ⟨i, j, hij, by rw [hxj]; ring⟩

/-- **`prop:rosmanis`(1), the characterization the manuscript's proof runs on.**
*"A string is negative iff (a) each fixed-point value occurs at most once (two equal fixed points
sum to `t`), and (b) for each `2`-cycle `{a, σ(a)}` only one of its two sides ever occurs."* -/
theorem isNegative_iff (σ : V → V) {N : ℕ} (x : Fin N → V) :
    IsNegative σ x ↔
      ((∀ i j : Fin N, i ≠ j → σ (x i) = x i → x j ≠ x i) ∧
        (∀ i j : Fin N, σ (x i) ≠ x i → x j ≠ σ (x i))) := by
  constructor
  · intro h
    refine ⟨fun i j hij hfix hxj => h i j hij (by rw [hfix]; exact hxj), fun i j hnf => ?_⟩
    by_cases hji : j = i
    · subst hji; exact fun hc => hnf hc.symm
    · exact h i j (Ne.symm hji)
  · rintro ⟨ha, hb⟩ i j hij
    by_cases hfix : σ (x i) = x i
    · rw [hfix]; exact ha i j hij hfix
    · exact hb i j hfix

/-! ## 2. The symmetry group `S_N × C(σ)` and its action on `D₀` -/

/-- `C(σ)`, the centralizer of the involution `σ` inside `Sym(V)`, as DEFINED (see the scope box:
the identification with `(C₂ ≀ S_m) × S_τ` is not formalized). -/
structure Centralizer (σ : V → V) where
  /-- the underlying value permutation -/
  toPerm : Equiv.Perm V
  /-- it commutes with `σ` -/
  comm : ∀ a, toPerm (σ a) = σ (toPerm a)

/-- The action of `S_N × C(σ)` on strings: `(π, ρ) · x = ρ ∘ x ∘ π`. -/
def act {σ : V → V} {N : ℕ} (π : Equiv.Perm (Fin N)) (ρ : Centralizer σ) (x : Fin N → V) :
    Fin N → V := fun i => ρ.toPerm (x (π i))

omit [DecidableEq V] in
/-- **The action preserves `D₀`** — the reason `S_N × C(σ)` is the relevant symmetry at all. -/
theorem isNegative_act {σ : V → V} {N : ℕ} (π : Equiv.Perm (Fin N)) (ρ : Centralizer σ)
    {x : Fin N → V} (hx : IsNegative σ x) : IsNegative σ (act π ρ x) := by
  intro i j hij hc
  simp only [act] at hc
  rw [← ρ.comm] at hc
  exact hx (π i) (π j) (fun h => hij (π.injective h)) (ρ.toPerm.injective hc)

/-! ## 3. An action invariant, and the count `≥ 2`

The manuscript's complete invariant is the pair `(f, λ)`.  Its `≥ 2` argument only ever separates
strings occupying ONE class from strings occupying TWO, so the coarser invariant "number of
distinct values" already does the whole job — and, unlike `(f, λ)`, it needs no partition API.
It is proved invariant, so the conclusions below are about genuine orbits. -/

/-- The number of distinct values a string takes. -/
def valueCount {N : ℕ} (x : Fin N → V) : ℕ := (Finset.univ.image x).card

/-- **`valueCount` is an `S_N × C(σ)`-invariant.** -/
theorem valueCount_act {σ : V → V} {N : ℕ} (π : Equiv.Perm (Fin N)) (ρ : Centralizer σ)
    (x : Fin N → V) : valueCount (act π ρ x) = valueCount x := by
  classical
  have himg : (Finset.univ.image fun i => x (π i)) = Finset.univ.image x := by
    apply Finset.Subset.antisymm
    · intro b hb
      simp only [Finset.mem_image, Finset.mem_univ, true_and] at hb ⊢
      obtain ⟨i, hi⟩ := hb
      exact ⟨π i, hi⟩
    · intro b hb
      simp only [Finset.mem_image, Finset.mem_univ, true_and] at hb ⊢
      obtain ⟨i, hi⟩ := hb
      exact ⟨π.symm i, by simpa using hi⟩
  have hcomp : (Finset.univ.image (act π ρ x))
      = (Finset.univ.image fun i => x (π i)).image ρ.toPerm := by
    rw [Finset.image_image]; rfl
  rw [valueCount, valueCount, hcomp, himg,
    Finset.card_image_of_injective _ ρ.toPerm.injective]

/-- Two strings with different `valueCount` lie in different orbits. -/
theorem not_same_orbit {σ : V → V} {N : ℕ} {x₁ x₂ : Fin N → V}
    (h : valueCount x₁ ≠ valueCount x₂) (π : Equiv.Perm (Fin N)) (ρ : Centralizer σ) :
    act π ρ x₁ ≠ x₂ := fun hc => h (by rw [← valueCount_act π ρ x₁, hc])

/-- **`D₀` is not a single orbit**, given any two negative strings with different `valueCount`. -/
theorem not_single_orbit {σ : V → V} {N : ℕ} {x₁ x₂ : Fin N → V}
    (h₁ : IsNegative σ x₁) (h₂ : IsNegative σ x₂) (hv : valueCount x₁ ≠ valueCount x₂) :
    ¬ ∃ x₀ : Fin N → V, IsNegative σ x₀ ∧
        ∀ x : Fin N → V, IsNegative σ x →
          ∃ (π : Equiv.Perm (Fin N)) (ρ : Centralizer σ), act π ρ x₀ = x := by
  rintro ⟨x₀, _, hall⟩
  obtain ⟨π₁, ρ₁, e₁⟩ := hall x₁ h₁
  obtain ⟨π₂, ρ₂, e₂⟩ := hall x₂ h₂
  exact hv (by rw [← e₁, ← e₂, valueCount_act, valueCount_act])

/-! ### The two manuscript witnesses -/

/-- `N` copies of a single value. -/
def constStr (N : ℕ) (a : V) : Fin N → V := fun _ => a

/-- `N-1` copies of `a` and one copy of `b`. -/
def oneOffStr (N : ℕ) (a b : V) : Fin N → V := fun i => if (i : ℕ) = 0 then b else a

theorem valueCount_constStr {N : ℕ} (hN : 0 < N) (a : V) : valueCount (constStr N a) = 1 := by
  classical
  have himg : (Finset.univ.image (constStr N a)) = {a} := by
    apply Finset.Subset.antisymm
    · intro c hc
      obtain ⟨_, _, hi⟩ := Finset.mem_image.mp hc
      simp [constStr] at hi
      simp [← hi]
    · intro c hc
      simp only [Finset.mem_singleton] at hc
      subst hc
      exact Finset.mem_image.mpr ⟨⟨0, hN⟩, Finset.mem_univ _, rfl⟩
  rw [valueCount, himg, Finset.card_singleton]

theorem valueCount_oneOffStr {N : ℕ} (hN : 2 ≤ N) {a b : V} (hab : b ≠ a) :
    valueCount (oneOffStr N a b) = 2 := by
  classical
  have h0 : (0 : ℕ) < N := by omega
  have h1 : (1 : ℕ) < N := by omega
  have himg : (Finset.univ.image (oneOffStr N a b)) = {b, a} := by
    apply Finset.Subset.antisymm
    · intro c hc
      obtain ⟨i, _, hi⟩ := Finset.mem_image.mp hc
      by_cases h : (i : ℕ) = 0
      · simp only [oneOffStr, if_pos h] at hi; simp [← hi]
      · simp only [oneOffStr, if_neg h] at hi; simp [← hi]
    · intro c hc
      simp only [Finset.mem_insert, Finset.mem_singleton] at hc
      rcases hc with rfl | rfl
      · exact Finset.mem_image.mpr ⟨⟨0, h0⟩, Finset.mem_univ _, by simp [oneOffStr]⟩
      · exact Finset.mem_image.mpr ⟨⟨1, h1⟩, Finset.mem_univ _, by simp [oneOffStr]⟩
  rw [valueCount, himg, Finset.card_pair_eq_two_iff.mpr hab]

omit [DecidableEq V] in
theorem isNegative_constStr {σ : V → V} {N : ℕ} {a : V} (ha : σ a ≠ a) :
    IsNegative σ (constStr N a) := fun _ _ _ hc => ha hc.symm

omit [DecidableEq V] in
theorem isNegative_oneOffStr {σ : V → V} {N : ℕ} {a b : V}
    (ha : σ a ≠ a) (hab : a ≠ σ b) (hba : b ≠ σ a) : IsNegative σ (oneOffStr N a b) := by
  intro i j hij hc
  simp only [oneOffStr] at hc
  by_cases hi : (i : ℕ) = 0 <;> by_cases hj : (j : ℕ) = 0
  · exact hij (Fin.ext (by omega))
  · rw [if_pos hi, if_neg hj] at hc; exact hab hc
  · rw [if_neg hi, if_pos hj] at hc; exact hba hc
  · rw [if_neg hi, if_neg hj] at hc; exact ha hc.symm

/-- The shared engine of the two branches. -/
theorem two_orbits_aux {σ : V → V} {N : ℕ} (hN : 2 ≤ N) {a b : V}
    (ha : σ a ≠ a) (hab : a ≠ σ b) (hba : b ≠ σ a) (hne : b ≠ a) :
    ∃ x₁ x₂ : Fin N → V, IsNegative σ x₁ ∧ IsNegative σ x₂ ∧
      (∀ (π : Equiv.Perm (Fin N)) (ρ : Centralizer σ), act π ρ x₁ ≠ x₂) ∧
      ¬ ∃ x₀ : Fin N → V, IsNegative σ x₀ ∧
          ∀ x : Fin N → V, IsNegative σ x →
            ∃ (π : Equiv.Perm (Fin N)) (ρ : Centralizer σ), act π ρ x₀ = x := by
  have hv : valueCount (constStr N a) ≠ valueCount (oneOffStr N a b) := by
    rw [valueCount_constStr (by omega), valueCount_oneOffStr hN hne]
    decide
  exact ⟨constStr N a, oneOffStr N a b, isNegative_constStr ha, isNegative_oneOffStr ha hab hba,
    fun π ρ => not_same_orbit hv π ρ,
    not_single_orbit (isNegative_constStr ha) (isNegative_oneOffStr ha hab hba) hv⟩

/-- **`prop:rosmanis`(1), branch `m ≥ 2`.**  *"`f = 0` with `λ = (N)` versus `λ = (N-1,1)` are two
orbits — concretely, `N` copies of one cycle's side versus `N-1` copies of that side and one copy
of a DIFFERENT cycle's side, both negative, as no cycle supplies both sides."* -/
theorem two_orbits_of_two_cycles {σ : V → V} (hσ : Function.Involutive σ) {N : ℕ} (hN : 2 ≤ N)
    {a b : V} (ha : σ a ≠ a) (hne : b ≠ a) (hne2 : b ≠ σ a) :
    ∃ x₁ x₂ : Fin N → V, IsNegative σ x₁ ∧ IsNegative σ x₂ ∧
      (∀ (π : Equiv.Perm (Fin N)) (ρ : Centralizer σ), act π ρ x₁ ≠ x₂) ∧
      ¬ ∃ x₀ : Fin N → V, IsNegative σ x₀ ∧
          ∀ x : Fin N → V, IsNegative σ x →
            ∃ (π : Equiv.Perm (Fin N)) (ρ : Centralizer σ), act π ρ x₀ = x :=
  two_orbits_aux hN ha (fun h => hne2 (by rw [h, hσ b])) hne2 hne

/-- **`prop:rosmanis`(1), branch `m = 1`** (which forces `τ = q - 2 ≥ 1`).  *"`f = 0`
(`λ = (N)`) versus `f = 1` (`λ = (N-1)`) are two orbits."*  `c` is the occupied fixed point. -/
theorem two_orbits_of_one_cycle {σ : V → V} (hσ : Function.Involutive σ) {N : ℕ} (hN : 2 ≤ N)
    {a c : V} (ha : σ a ≠ a) (hc : σ c = c) :
    ∃ x₁ x₂ : Fin N → V, IsNegative σ x₁ ∧ IsNegative σ x₂ ∧
      (∀ (π : Equiv.Perm (Fin N)) (ρ : Centralizer σ), act π ρ x₁ ≠ x₂) ∧
      ¬ ∃ x₀ : Fin N → V, IsNegative σ x₀ ∧
          ∀ x : Fin N → V, IsNegative σ x →
            ∃ (π : Equiv.Perm (Fin N)) (ρ : Centralizer σ), act π ρ x₀ = x := by
  have hca : c ≠ a := fun h => ha (by rw [← h]; exact hc)
  refine two_orbits_aux hN ha ?_ ?_ hca
  · rw [hc]; exact fun h => hca h.symm
  · intro h
    apply hca
    have hcc : σ c = σ (σ a) := by rw [h]
    rw [hc, hσ a] at hcc
    exact hcc

omit [DecidableEq V] in
/-- **`prop:rosmanis`(3), positive blocks empty.**  *"If `τ = 0` the positive-side building blocks
of [Rosmanis14] — inputs whose collision is a repeated value `x_i = x_j` — are empty."* -/
theorem positive_blocks_empty {σ : V → V} (hτ : ∀ a : V, σ a ≠ a) {N : ℕ} (x : Fin N → V)
    (i j : Fin N) (heq : x i = x j) : x j ≠ σ (x i) := by
  rw [← heq]
  exact fun h => hτ (x i) h.symm

/-! ## 4. Instantiation at `2Sum` over `Z_q` -/

theorem involutive_sub {q : ℕ} (t : ZMod q) : Function.Involutive (fun a : ZMod q => t - a) :=
  fun a => by simp

/-- **`prop:rosmanis`(1) for `2Sum_{Z_q,t,N}` itself: `D₀` is never a single orbit.**
Stated in the paper's own terms — the two witnesses are literally negative inputs of `2Sum`. -/
theorem twoSum_not_single_orbit {q : ℕ} [NeZero q] (t : ZMod q) {N : ℕ} (hN : 2 ≤ N)
    {a b : ZMod q} (ha : t - a ≠ a) (hne : b ≠ a) (hne2 : b ≠ t - a) :
    ∃ x₁ x₂ : Fin N → ZMod q,
      twoSum (ZMod q) t N x₁ = false ∧ twoSum (ZMod q) t N x₂ = false ∧
      (∀ (π : Equiv.Perm (Fin N)) (ρ : Centralizer (fun a : ZMod q => t - a)),
        act π ρ x₁ ≠ x₂) := by
  obtain ⟨x₁, x₂, h₁, h₂, hsep, _⟩ :=
    two_orbits_of_two_cycles (involutive_sub t) hN ha hne hne2
  exact ⟨x₁, x₂, (isNegative_iff_twoSum_false t x₁).mp h₁,
    (isNegative_iff_twoSum_false t x₂).mp h₂, hsep⟩

/-! ## 5. `prop:rosmanis`(2): the two finite regularity witnesses

Only these two are mechanized; the representation-theoretic sentence of part (2) is not (see the
scope box). -/

/-- **Existence fails already at `q = 3`.**  `G = Z_3`, `t = 0`, so `σ(a) = -a`, whose only fixed
point is `0` (hence `τ = 1`, `m = 1`).  Take `y = (a, b)` with `a = 0` the fixed point and `b = 1`
on the `2`-cycle; `y` is negative.  Transposing the two positions gives `(1, 0)`, and NO value map
commuting with `σ` realises it — *"such `ρ` preserves the fixed-point set and cannot send `a` to
`b`"*.  (Injectivity of `ρ` is not even needed: commuting with `σ` alone forces `ρ 0 = 0`.) -/
theorem existence_fails_q3 :
    (∀ a : ZMod 3, (-a = a) ↔ a = 0) ∧
    IsNegative (fun a : ZMod 3 => -a) (![0, 1] : Fin 2 → ZMod 3) ∧
    (∀ ρ : ZMod 3 → ZMod 3, (∀ a, ρ (-a) = -(ρ a)) →
      ¬ (∀ i : Fin 2, ρ ((![0, 1] : Fin 2 → ZMod 3) i) = (![1, 0] : Fin 2 → ZMod 3) i)) := by
  refine ⟨by decide, by decide, by decide⟩

/-- The transposed string used above really is `y ∘ (0 1)`. -/
theorem swapped_string_q3 :
    ∀ i : Fin 2, (![1, 0] : Fin 2 → ZMod 3) i
      = (![0, 1] : Fin 2 → ZMod 3) (Equiv.swap 0 1 i) := by decide

/-- The side-flip of the `2`-cycle `{2,3}` of `σ(a) = -a` on `Z_5`. -/
def flip23 : ZMod 5 → ZMod 5 := fun a => if a = 2 then 3 else if a = 3 then 2 else a

/-- **Uniqueness fails whenever `m ≥ 2`.**  `G = Z_5`, `t = 0`: `σ(a) = -a` has the single fixed
point `0` and the two `2`-cycles `{1,4}`, `{2,3}`, so `m = 2`.  For `N = 2`, `y = (1,1)` is
negative and is fixed (`π = id`) both by `ρ = id` and by the side-flip of the OTHER `2`-cycle —
two distinct elements of `C(σ)` matching the same position permutation. -/
theorem uniqueness_fails_q5 :
    IsNegative (fun a : ZMod 5 => -a) (![1, 1] : Fin 2 → ZMod 5) ∧
    Function.Injective flip23 ∧
    (∀ a : ZMod 5, flip23 (-a) = -(flip23 a)) ∧
    (∀ i : Fin 2, flip23 ((![1, 1] : Fin 2 → ZMod 5) i) = (![1, 1] : Fin 2 → ZMod 5) i) ∧
    flip23 ≠ id := by
  refine ⟨by decide, by decide, by decide, by decide, by decide⟩

/-- `Z_5` at `t = 0` really has `τ = 1` and `m = 2`, so `uniqueness_fails_q5` is in the branch it
claims to be in. -/
theorem q5_cycle_type : (Finset.univ.filter fun a : ZMod 5 => -a = a).card = 1 := by decide

/-! ## 6. Non-vacuity witnesses for the general theorems -/

/-- `twoSum_not_single_orbit` is non-vacuous: `q = 5`, `t = 0`, `a = 1`, `b = 2` satisfy its
hypotheses (`a` and `b` sit on different `2`-cycles). -/
theorem witness_two_cycles_q5 :
    ((0 : ZMod 5) - 1 ≠ 1) ∧ ((2 : ZMod 5) ≠ 1) ∧ ((2 : ZMod 5) ≠ (0 : ZMod 5) - 1) := by decide

/-- `two_orbits_of_one_cycle` is non-vacuous: `q = 3`, `t = 0`, `a = 1` on the unique `2`-cycle,
`c = 0` the fixed point. -/
theorem witness_one_cycle_q3 : ((0 : ZMod 3) - 1 ≠ 1) ∧ ((0 : ZMod 3) - 0 = 0) := by decide

end Rosmanis
end KsumAudit
