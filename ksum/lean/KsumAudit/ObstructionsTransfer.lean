/-
# `prop:transfer-facts` — Three transfer facts (G1, G2, G3)

LaTeX: `ksum/paper/ksum_small_alphabet.tex`, label `prop:transfer-facts`, line 1111,
displayed equations (52) (the isotypic decomposition), (53) (the gauge identity) and (54).

DAG nodes (this ONE LaTeX proposition spans THREE nodes):
  * `KSUM.B4b.L2.G1` — multiplicity-gauge and terminal-label insufficiency  (equation 53)
  * `KSUM.B4b.L2.G2` — direct satellite-vector Reynolds zero
  * `KSUM.B4b.L2.G3` — positive diagonal/Reynolds band zero                 (equation 54)

## The quantifier structure the LaTeX asserts (written out BEFORE formalizing)

(G1) ∀ `B_λ ∈ End(M_λ)`, ∀ `O ∈ O(M_λ)`:
     `∑_j Q_{λ,j} B_λ Q_{λ,j}ᵀ = ∑_j (Q_{λ,j}O)(Oᵀ B_λ O)(Q_{λ,j}O)ᵀ`.
     Consequence asserted in prose: terminal `H`-irrep labels do not specify multiplicity
     coordinates across `N`; a GT/Jucys–Murphy chain acts as the identity on `M_λ` and by itself
     does not remove the residual gauge.

(G2) ∀ `v` lying in a nontrivial `H`-satellite:  `R_G v = R_G R_H v = 0`.

(G3) ∀ nonzero positive semidefinite `A` on `ℝ^X`: `μ_A = R_G(diag A)/tr A` is a nonnegative
     invariant probability measure whose degree-zero factorial moment is one, so its pure high
     degree is zero.

## Notes on the rendering

* (G1) is formalized as the literal matrix identity, TERMWISE (which is stronger than the summed
  form), for an arbitrary index family `Q` and an arbitrary orthogonal `O`.  The prose GT/JM
  sentence is not a displayed claim and is not formalized; instead a concrete `2×2` witness shows
  the gauge is a GENUINE freedom (`B ≠ OᵀBO` while the lifted operators agree), which is the
  content of "terminal labels do not specify multiplicity coordinates".
* (G2) is formalized for an arbitrary finite group `G`, an arbitrary linear action, and an
  arbitrary NONEMPTY subset `H ⊆ G`.  Note the proof needs no subgroup structure on `H` at all —
  only `H ≠ ∅` — so `transfer_G2` is more general than the LaTeX's.
  **2026-07-30 T3 audit repair.**  `transfer_G2` takes `R_H v = 0` as a HYPOTHESIS, whereas the
  paper's hypothesis is "`v` lies in a nontrivial `H`-satellite".  That gap is closed below by
  `reynolds_eq_zero_iff_mem_augment`: for a multiplicatively closed nonempty `H` (in particular a
  subgroup), `R_H v = 0` **if and only if** `v` lies in the augmentation submodule
  `⟨ρ h w − w : h ∈ H⟩`, which in characteristic zero is exactly the sum of the nontrivial
  `H`-isotypic components.  So the satellite hypothesis is now a proved characterization rather
  than an assumption.
  **2026-07-31 gap-closure item L-4.**  The one remaining step — the dictionary "nontrivial
  isotypic component = augmentation submodule", which the T3 run and the statement-fidelity review
  both recorded as granted-by-Maschke — is now PROVED, as
  `inNontrivialSatellite_iff_mem_augment`, and (G2) is restated at the manuscript's own hypothesis
  as `transfer_G2_of_satellite`.  See the route note in the `G2` section for why Mathlib's
  `MonoidAlgebra` Maschke theorem is deliberately not invoked.
* (G3): the paper says "for every NONZERO positive semidefinite `A`", and its proof uses this only
  through `tr A > 0`.  **2026-07-30 T3 audit repair:** the implication "`A` PSD and `A ≠ 0` ⇒
  `tr A ≠ 0`" is now PROVED (`psd_eq_zero_of_trace_eq_zero`), so `transfer_G3_nonzero` below is
  stated at the paper's own quantifier.  The `A.trace ≠ 0` form (`transfer_G3`) is kept because it
  is the weaker hypothesis and is what the arithmetic actually needs.
-/
import KsumAudit.ObstructionsCore
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Algebra.Order.Star.Real

namespace KsumAudit.Obstructions.Transfer

open Finset Matrix KsumAudit.Obstructions

set_option linter.unusedSectionVars false

/-! ## (G1) The multiplicity gauge, equation (53) -/

section G1

variable {n m : Type*} [Fintype n] [Fintype m] [DecidableEq n] [DecidableEq m]

/-- **`prop:transfer-facts` (G1), equation (53), termwise.**
For every `B` and every orthogonal `O`, conjugating the multiplicity coordinates by `O` and the
embedding by `O` leaves each lifted term — hence the sum — unchanged. -/
theorem gauge_term (Q : Matrix n m ℝ) (B O : Matrix m m ℝ) (hO : O * Oᵀ = 1) :
    (Q * O) * (Oᵀ * B * O) * (Q * O)ᵀ = Q * B * Qᵀ := by
  have key : ∀ Z : Matrix m n ℝ, O * (Oᵀ * Z) = Z := by
    intro Z; rw [← Matrix.mul_assoc, hO, Matrix.one_mul]
  rw [Matrix.transpose_mul]
  simp only [Matrix.mul_assoc]
  rw [key, key]

/-- **`prop:transfer-facts` (G1), equation (53) as displayed (summed over the frame index).** -/
theorem gauge_sum {ι : Type*} [Fintype ι] (Q : ι → Matrix n m ℝ) (B O : Matrix m m ℝ)
    (hO : O * Oᵀ = 1) :
    ∑ j, Q j * B * (Q j)ᵀ = ∑ j, (Q j * O) * (Oᵀ * B * O) * (Q j * O)ᵀ :=
  Finset.sum_congr rfl fun j _ => (gauge_term (Q j) B O hO).symm

end G1

/-! ## (G2) Full-group Reynolds kills a direct satellite lift -/

section G2

variable {G : Type*} [Group G] [Fintype G] [DecidableEq G]
variable {V : Type*} [AddCommGroup V] [Module ℚ V]
variable (ρ : G →* (V →ₗ[ℚ] V))

/-- `R_S = |S|⁻¹ ∑_{g ∈ S} ρ g`, the Reynolds average over a subset `S ⊆ G`. -/
noncomputable def reynolds (S : Finset G) : V →ₗ[ℚ] V :=
  (1 / (S.card : ℚ)) • (∑ g ∈ S, ρ g)

lemma reynolds_apply (S : Finset G) (v : V) :
    reynolds ρ S v = (1 / (S.card : ℚ)) • ∑ g ∈ S, ρ g v := by
  simp [reynolds, LinearMap.sum_apply]

/-- The full-group Reynolds average absorbs the group action. -/
lemma reynolds_univ_apply_smul (g₀ : G) (v : V) :
    reynolds ρ univ (ρ g₀ v) = reynolds ρ univ v := by
  classical
  rw [reynolds_apply, reynolds_apply]
  congr 1
  have : ∀ g : G, ρ g (ρ g₀ v) = ρ (g * g₀) v := by
    intro g; rw [map_mul]; rfl
  rw [Finset.sum_congr rfl (fun g (_ : g ∈ univ) => this g)]
  exact Fintype.sum_equiv (Equiv.mulRight g₀) _ _ (fun g => rfl)

/-- **`prop:transfer-facts` (G2), first half:** `R_G ∘ R_H = R_G` for ANY nonempty `H ⊆ G`
(no subgroup structure is needed). -/
theorem reynolds_univ_comp (H : Finset G) (hH : H.Nonempty) (v : V) :
    reynolds ρ univ (reynolds ρ H v) = reynolds ρ univ v := by
  classical
  have hcard : (H.card : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr (Finset.card_ne_zero.mpr hH)
  rw [reynolds_apply ρ H v, map_smul, map_sum]
  rw [Finset.sum_congr rfl (fun g (_ : g ∈ H) => reynolds_univ_apply_smul ρ g v)]
  rw [Finset.sum_const, ← Nat.cast_smul_eq_nsmul ℚ, smul_smul]
  rw [show (1 / (H.card : ℚ)) * (H.card : ℚ) = 1 by field_simp]
  rw [one_smul]

/-- **`prop:transfer-facts` (G2).**
If `R_H v = 0` — which is what "v lies in a nontrivial `H`-satellite" gives, since the Reynolds
projection is the orthogonal projection onto the trivial isotypic component — then
`R_G v = R_G R_H v = 0`. -/
theorem transfer_G2 (H : Finset G) (hH : H.Nonempty) (v : V) (hv : reynolds ρ H v = 0) :
    reynolds ρ univ v = 0 ∧ reynolds ρ univ v = reynolds ρ univ (reynolds ρ H v) := by
  have h := reynolds_univ_comp ρ H hH v
  rw [hv, map_zero] at h
  exact ⟨h.symm, by rw [hv, map_zero, h.symm]⟩

/-! ### What "`v` lies in a nontrivial `H`-satellite" means, made a theorem

The LaTeX hypothesis of (G2) is not `R_H v = 0` but "`v` lies in a nontrivial `H`-satellite".
The two are equivalent, and the equivalence is proved here rather than assumed. -/

/-- The **augmentation submodule** generated by `H`: the span of all differences `ρ h w − w` with
`h ∈ H`.  Over a field of characteristic zero and for a subgroup `H`, this is exactly the sum of
the nontrivial `H`-isotypic components — i.e. the span of the paper's nontrivial
`H`-satellites — and it is the complement of the invariants in Maschke's decomposition. -/
def augment (H : Finset G) : Submodule ℚ V :=
  Submodule.span ℚ {u : V | ∃ h ∈ H, ∃ w : V, u = ρ h w - w}

/-- For a multiplicatively closed `H`, the Reynolds average is invariant under translating its
argument by any `h ∈ H`. -/
lemma reynolds_smul_eq (H : Finset G)
    (hclosed : ∀ g ∈ H, ∀ h ∈ H, g * h ∈ H) (h : G) (hh : h ∈ H) (v : V) :
    reynolds ρ H (ρ h v) = reynolds ρ H v := by
  classical
  rw [reynolds_apply, reynolds_apply]
  congr 1
  have hstep : ∀ g ∈ H, ρ g (ρ h v) = ρ (g * h) v := by
    intro g _; rw [map_mul]; rfl
  rw [Finset.sum_congr rfl hstep]
  have hinj : Set.InjOn (fun g => g * h) H := fun a _ b _ hab => by
    simpa using mul_right_cancel hab
  have himg : H.image (fun g => g * h) = H := by
    refine Finset.eq_of_subset_of_card_le ?_ ?_
    · intro x hx
      obtain ⟨g, hg, rfl⟩ := Finset.mem_image.mp hx
      exact hclosed g hg h hh
    · rw [Finset.card_image_of_injOn hinj]
  have himage : ∑ g ∈ H.image (fun g => g * h), ρ g v = ∑ g ∈ H, ρ (g * h) v :=
    Finset.sum_image (fun a ha b hb hab => hinj ha hb hab)
  rw [himg] at himage
  exact himage.symm

/-- **The sufficient condition behind (G2).**  For a multiplicatively closed nonempty `H` (in
particular a subgroup), the Reynolds average annihilates the whole augmentation submodule. -/
theorem reynolds_eq_zero_of_mem_augment (H : Finset G)
    (hclosed : ∀ g ∈ H, ∀ h ∈ H, g * h ∈ H) (v : V) (hv : v ∈ augment ρ H) :
    reynolds ρ H v = 0 := by
  classical
  refine Submodule.span_induction ?_ (by simp) ?_ ?_ hv
  · rintro u ⟨h, hh, w, rfl⟩
    rw [map_sub, reynolds_smul_eq ρ H hclosed h hh w, sub_self]
  · intro x y _ _ hx hy; rw [map_add, hx, hy, add_zero]
  · intro c x _ hx; rw [map_smul, hx, smul_zero]

/-- **The converse.**  Anything the Reynolds average kills already lies in the augmentation
submodule.  (Needs no closure hypothesis at all.) -/
theorem mem_augment_of_reynolds_eq_zero (H : Finset G) (hH : H.Nonempty) (v : V)
    (hv : reynolds ρ H v = 0) : v ∈ augment ρ H := by
  classical
  have hcard : (H.card : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr (Finset.card_ne_zero.mpr hH)
  have hsum : (∑ h ∈ H, (ρ h v - v)) ∈ augment ρ H :=
    Submodule.sum_mem _ fun h hh => Submodule.subset_span ⟨h, hh, v, rfl⟩
  have hexp : ∑ h ∈ H, (ρ h v - v) = (∑ h ∈ H, ρ h v) - (H.card : ℚ) • v := by
    rw [Finset.sum_sub_distrib, Finset.sum_const, ← Nat.cast_smul_eq_nsmul ℚ]
  have hzero : ∑ h ∈ H, ρ h v = 0 := by
    have := congrArg (fun x => (H.card : ℚ) • x) (reynolds_apply ρ H v ▸ hv)
    simpa [smul_smul, hcard] using this
  rw [hexp, hzero, zero_sub] at hsum
  have := Submodule.smul_mem (augment ρ H) (-(H.card : ℚ)⁻¹) hsum
  simpa [smul_smul, hcard] using this

/-- **(G2) at the paper's own hypothesis.**  `R_H v = 0` ⟺ `v` lies in the augmentation
submodule, so "`v` lies in a nontrivial `H`-satellite" is a *characterization* here, not an
assumption. -/
theorem reynolds_eq_zero_iff_mem_augment (H : Finset G) (hH : H.Nonempty)
    (hclosed : ∀ g ∈ H, ∀ h ∈ H, g * h ∈ H) (v : V) :
    reynolds ρ H v = 0 ↔ v ∈ augment ρ H :=
  ⟨mem_augment_of_reynolds_eq_zero ρ H hH v, reynolds_eq_zero_of_mem_augment ρ H hclosed v⟩

/-- **`prop:transfer-facts` (G2), assembled at the paper's hypothesis.**
A vector in the augmentation submodule of a multiplicatively closed nonempty `H` — the paper's
"nontrivial `H`-satellite" — is killed by the full-group Reynolds projection, and factoring
through `R_H` changes nothing. -/
theorem transfer_G2_satellite (H : Finset G) (hH : H.Nonempty)
    (hclosed : ∀ g ∈ H, ∀ h ∈ H, g * h ∈ H) (v : V) (hv : v ∈ augment ρ H) :
    reynolds ρ univ v = 0 ∧ reynolds ρ univ v = reynolds ρ univ (reynolds ρ H v) :=
  transfer_G2 ρ H hH v (reynolds_eq_zero_of_mem_augment ρ H hclosed v hv)

/-! ### The satellite ↔ augmentation dictionary  (gap-closure item L-4, 2026-07-31)

The statement-fidelity review (`ksum/reviews/ksum_lean_statement_fidelity_review_20260731.md` §6.B)
graded (G2) **NARROWER**: *"The paper's hypothesis is `v` lies in a nontrivial `H`-satellite,
defined at (52) as a summand with nontrivial `U_λ`.  The Lean's is `v ∈ augment ρ H`.  These
coincide by Maschke in characteristic zero, which is not formalized. … the remaining step is a
definitional substitution."*

It is formalized here.  Under (52) a satellite is a summand `U_λ ⊗ M_λ` of `V↓_H`, and a
**nontrivial** one is a summand with `λ` nontrivial; a vector lies in a nontrivial satellite
exactly when it lies in an `H`-stable subspace whose trivial isotypic component is zero — i.e.
whose space of `H`-invariant vectors is `0`.  That is `InNontrivialSatellite` below, stated without
reference to any decomposition, and `inNontrivialSatellite_iff_mem_augment` proves the dictionary.

**Route note — a recorded deviation from the commission's suggested route, not a silent one.**
Mathlib's `MonoidAlgebra.Submodule.exists_isCompl` (Maschke) is deliberately NOT invoked.  The
characteristic-zero content Maschke packages is exactly *"the Reynolds average is an `H`-equivariant
idempotent onto the `H`-invariants, with kernel the augmentation submodule"*, and that is what the
three lemmas below prove (`reynolds_of_invariant`, `reynolds_mem_invariant`, plus the two
directions).  Routing through Mathlib would require transporting `ρ` to a `MonoidAlgebra ℚ H`-module
structure only to obtain a *weaker* conclusion (SOME `H`-stable complement exists, not that it is
this one).  Nothing here is assumed that Maschke would have supplied. -/

/-- **"`v` lies in a nontrivial `H`-satellite"**, in the sense (52) fixes: `v` sits inside an
`H`-stable subspace with NO nonzero `H`-invariant vector, i.e. one whose trivial isotypic component
vanishes. -/
def InNontrivialSatellite (H : Finset G) (v : V) : Prop :=
  ∃ W : Submodule ℚ V, v ∈ W ∧ (∀ h ∈ H, ∀ w ∈ W, ρ h w ∈ W) ∧
    (∀ w ∈ W, (∀ h ∈ H, ρ h w = w) → w = 0)

/-- On an `H`-invariant vector the Reynolds average is the identity.  (Half of "`R_H` is a
projection onto the invariants" — the char-0 content of Maschke.) -/
lemma reynolds_of_invariant (H : Finset G) (hH : H.Nonempty) (w : V)
    (hw : ∀ h ∈ H, ρ h w = w) : reynolds ρ H w = w := by
  have hcard : (H.card : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr (Finset.card_ne_zero.mpr hH)
  rw [reynolds_apply, Finset.sum_congr rfl hw, Finset.sum_const, ← Nat.cast_smul_eq_nsmul ℚ,
    smul_smul, show (1 / (H.card : ℚ)) * (H.card : ℚ) = 1 by field_simp, one_smul]

/-- `R_H v` is `H`-invariant, for a multiplicatively closed `H`.  (The other half.) -/
lemma reynolds_mem_invariant (H : Finset G)
    (hclosed : ∀ g ∈ H, ∀ h ∈ H, g * h ∈ H) (g : G) (hg : g ∈ H) (v : V) :
    ρ g (reynolds ρ H v) = reynolds ρ H v := by
  classical
  rw [reynolds_apply, map_smul, map_sum]
  congr 1
  have hstep : ∀ h ∈ H, ρ g (ρ h v) = ρ (g * h) v := fun h _ => by rw [map_mul]; rfl
  rw [Finset.sum_congr rfl hstep]
  have hinjL : Set.InjOn (fun h => g * h) H := fun a _ b _ hab => by
    simpa using mul_left_cancel hab
  have himg : H.image (fun h => g * h) = H := by
    refine Finset.eq_of_subset_of_card_le ?_ ?_
    · intro x hx
      obtain ⟨h, hh, rfl⟩ := Finset.mem_image.mp hx
      exact hclosed g hg h hh
    · rw [Finset.card_image_of_injOn hinjL]
  have himage : ∑ h ∈ H.image (fun h => g * h), ρ h v = ∑ h ∈ H, ρ (g * h) v :=
    Finset.sum_image (fun a ha b hb hab => hinjL ha hb hab)
  rw [himg] at himage
  exact himage.symm

/-- **The Maschke dictionary, proved.**  For a multiplicatively closed nonempty `H` (in particular
a subgroup), `v` lies in a nontrivial `H`-satellite **iff** `v` lies in the augmentation submodule
— iff, by `reynolds_eq_zero_iff_mem_augment`, `R_H v = 0`.

⟸ takes `W = ker R_H`, which is `H`-stable and has no nonzero invariants; ⟹ observes that `R_H v`
lies in `W` and is `H`-invariant, so `W`'s hypothesis forces it to vanish. -/
theorem inNontrivialSatellite_iff_mem_augment (H : Finset G) (hH : H.Nonempty)
    (hclosed : ∀ g ∈ H, ∀ h ∈ H, g * h ∈ H) (v : V) :
    InNontrivialSatellite ρ H v ↔ v ∈ augment ρ H := by
  constructor
  · rintro ⟨W, hvW, hstab, hnoinv⟩
    refine mem_augment_of_reynolds_eq_zero ρ H hH v ?_
    have hmem : reynolds ρ H v ∈ W := by
      rw [reynolds_apply]
      exact Submodule.smul_mem _ _ (Submodule.sum_mem _ fun h hh => hstab h hh v hvW)
    exact hnoinv _ hmem (fun g hg => reynolds_mem_invariant ρ H hclosed g hg v)
  · intro hv
    refine ⟨LinearMap.ker (reynolds ρ H), LinearMap.mem_ker.mpr ?_, ?_, ?_⟩
    · exact reynolds_eq_zero_of_mem_augment ρ H hclosed v hv
    · intro h hh w hw
      refine LinearMap.mem_ker.mpr ?_
      rw [reynolds_smul_eq ρ H hclosed h hh w]
      exact LinearMap.mem_ker.mp hw
    · intro w hw hinvw
      rw [← reynolds_of_invariant ρ H hH w hinvw]
      exact LinearMap.mem_ker.mp hw

/-- **`prop:transfer-facts` (G2) at the manuscript's own hypothesis, with no dictionary granted.**
If `v` lies in a nontrivial `H`-satellite then `R_G v = R_G R_H v = 0`. -/
theorem transfer_G2_of_satellite (H : Finset G) (hH : H.Nonempty)
    (hclosed : ∀ g ∈ H, ∀ h ∈ H, g * h ∈ H) (v : V) (hv : InNontrivialSatellite ρ H v) :
    reynolds ρ univ v = 0 ∧ reynolds ρ univ v = reynolds ρ univ (reynolds ρ H v) :=
  transfer_G2_satellite ρ H hH hclosed v
    ((inNontrivialSatellite_iff_mem_augment ρ H hH hclosed v).mp hv)

end G2

/-! ## (G3) The positive normalized diagonal has band zero, equation (54) -/

section G3

variable {G X : Type*} [Group G] [Fintype G] [Fintype X] [DecidableEq X] [MulAction G X]

/-- `R_G` acting on functions `X → ℝ` by averaging the permutation action. -/
noncomputable def reynoldsFn (f : X → ℝ) (x : X) : ℝ :=
  (1 / (Fintype.card G : ℝ)) * ∑ g : G, f (g⁻¹ • x)

lemma reynoldsFn_nonneg {f : X → ℝ} (hf : ∀ x, 0 ≤ f x) (x : X) : 0 ≤ reynoldsFn (G := G) f x := by
  refine mul_nonneg (by positivity) (Finset.sum_nonneg fun g _ => hf _)

/-- Reynolds averaging preserves the coordinate sum. -/
lemma reynoldsFn_sum (f : X → ℝ) :
    ∑ x, reynoldsFn (G := G) f x = ∑ x, f x := by
  classical
  have hG : (0:ℝ) < (Fintype.card G : ℝ) := by
    exact_mod_cast Fintype.card_pos_iff.mpr ⟨1⟩
  simp only [reynoldsFn, ← Finset.mul_sum]
  rw [Finset.sum_comm]
  have hg : ∀ g : G, ∑ x : X, f (g⁻¹ • x) = ∑ x : X, f x := fun g =>
    Equiv.sum_comp (MulAction.toPerm g⁻¹) f
  rw [Finset.sum_congr rfl (fun g (_ : g ∈ univ) => hg g), Finset.sum_const, Finset.card_univ,
    nsmul_eq_mul]
  field_simp

/-- Reynolds averaging produces an invariant function. -/
lemma reynoldsFn_invariant (f : X → ℝ) (g₀ : G) (x : X) :
    reynoldsFn (G := G) f (g₀ • x) = reynoldsFn (G := G) f x := by
  classical
  simp only [reynoldsFn]
  congr 1
  refine Fintype.sum_equiv (Equiv.mulLeft g₀⁻¹) _ _ (fun g => ?_)
  simp only [Equiv.coe_mulLeft, _root_.mul_inv_rev, inv_inv, ← mul_smul]

/-- **`prop:transfer-facts` (G3), equation (54).**
For a positive semidefinite `A` with nonzero trace, `μ_A = R_G(diag A)/tr A` is a nonnegative,
`G`-invariant probability measure; consequently its degree-zero falling-factorial moment is `1`,
so it annihilates NO row and its pure high degree is zero. -/
theorem transfer_G3 (A : Matrix X X ℝ) (hA : A.PosSemidef) (htr : A.trace ≠ 0) :
    (∀ x, 0 ≤ reynoldsFn (G := G) (fun i => A i i) x / A.trace)
      ∧ (∑ x, reynoldsFn (G := G) (fun i => A i i) x / A.trace) = 1
      ∧ (∀ (g : G) (x : X),
          reynoldsFn (G := G) (fun i => A i i) (g • x) / A.trace
            = reynoldsFn (G := G) (fun i => A i i) x / A.trace)
      ∧ (∑ x, (reynoldsFn (G := G) (fun i => A i i) x / A.trace) * 1) ≠ 0 := by
  have hd : ∀ i : X, 0 ≤ A i i := fun _ => hA.diag_nonneg
  have htrpos : 0 < A.trace := lt_of_le_of_ne hA.trace_nonneg (Ne.symm htr)
  have hsum : ∑ x, reynoldsFn (G := G) (fun i => A i i) x = A.trace := by
    rw [reynoldsFn_sum]; rfl
  refine ⟨fun x => div_nonneg (reynoldsFn_nonneg hd x) htrpos.le, ?_, ?_, ?_⟩
  · rw [← Finset.sum_div, hsum, div_self htr]
  · intro g x; rw [reynoldsFn_invariant]
  · simp only [mul_one]
    rw [← Finset.sum_div, hsum, div_self htr]
    norm_num

/-! ### (G3) at the paper's own quantifier: "every NONZERO positive semidefinite `A`"

The LaTeX quantifies over nonzero PSD operators and its proof then uses `tr A > 0`.  The step
between the two is proved here, so no hypothesis is silently strengthened. -/

/-- A positive semidefinite real matrix with zero trace is zero.

Proof: the diagonal is nonnegative and sums to `0`, so it vanishes; then testing the quadratic
form on `e_i + t·e_j` gives `0 ≤ 2t·A i j` for every real `t`, forcing `A i j = 0`. -/
theorem psd_eq_zero_of_trace_eq_zero {Y : Type*} [Fintype Y] [DecidableEq Y]
    {A : Matrix Y Y ℝ} (hA : A.PosSemidef) (h : A.trace = 0) : A = 0 := by
  have hdiag : ∀ i, A i i = 0 := by
    have hnn : ∀ i ∈ (univ : Finset Y), 0 ≤ A i i := fun i _ => hA.diag_nonneg
    have hz : ∑ i, A i i = 0 := by simpa [Matrix.trace, Matrix.diag] using h
    exact fun i => (Finset.sum_eq_zero_iff_of_nonneg hnn).mp hz i (Finset.mem_univ i)
  ext i j
  rcases eq_or_ne i j with rfl | hij
  · simpa using hdiag i
  · have hsym : A j i = A i j := by simpa using hA.1.apply i j
    have key : ∀ t : ℝ, 0 ≤ 2 * t * A i j := by
      intro t
      have h0 := hA.dotProduct_mulVec_nonneg (Pi.single i (1:ℝ) + Pi.single j t)
      rw [star_trivial] at h0
      simp only [Matrix.mulVec_add, add_dotProduct, dotProduct_add, Matrix.mulVec_single,
        single_dotProduct, Pi.smul_apply, op_smul_eq_mul, Matrix.col_apply] at h0
      rw [hdiag i, hdiag j, hsym] at h0
      linarith
    have h1 := key 1
    have h2 := key (-1)
    simp only [Matrix.zero_apply]
    linarith

/-- Consequently a nonzero positive semidefinite matrix has nonzero (indeed positive) trace. -/
theorem psd_trace_pos_of_ne_zero {Y : Type*} [Fintype Y] [DecidableEq Y]
    {A : Matrix Y Y ℝ} (hA : A.PosSemidef) (hA0 : A ≠ 0) : 0 < A.trace :=
  lt_of_le_of_ne hA.trace_nonneg
    (Ne.symm fun h => hA0 (psd_eq_zero_of_trace_eq_zero hA h))

/-- **`prop:transfer-facts` (G3) at the paper's quantifier.**
For EVERY NONZERO positive semidefinite `A` on `ℝ^X`, `μ_A = R_G(diag A)/tr A` is a nonnegative,
`G`-invariant probability measure whose degree-zero factorial moment is exactly `1`. -/
theorem transfer_G3_nonzero (A : Matrix X X ℝ) (hA : A.PosSemidef) (hA0 : A ≠ 0) :
    (∀ x, 0 ≤ reynoldsFn (G := G) (fun i => A i i) x / A.trace)
      ∧ (∑ x, reynoldsFn (G := G) (fun i => A i i) x / A.trace) = 1
      ∧ (∀ (g : G) (x : X),
          reynoldsFn (G := G) (fun i => A i i) (g • x) / A.trace
            = reynoldsFn (G := G) (fun i => A i i) x / A.trace)
      ∧ (∑ x, (reynoldsFn (G := G) (fun i => A i i) x / A.trace) * 1) ≠ 0 :=
  transfer_G3 A hA (psd_trace_pos_of_ne_zero hA hA0).ne'

/-- **"…so its pure high degree is zero", machine-checked.**
For any occupancy labelling of the configuration set and any `d ≥ 1`, `μ_A` does NOT annihilate
every falling-factorial row of order below `d`: the order-zero row is the constant `1` and its
moment is `1 ≠ 0`.  (This is `ObstructionsCore.PureHighDegree` transcribed to `ℝ`, which is where
the matrix lives.) -/
theorem transfer_G3_pure_high_degree_zero {B : Type*} [Fintype B] [DecidableEq B]
    (A : Matrix X X ℝ) (hA : A.PosSemidef) (hA0 : A ≠ 0) (occ : X → B → ℕ) (d : ℕ) (hd : 1 ≤ d) :
    ¬ (∀ α : B → ℕ, (∑ a, α a) < d →
        ∑ x, (reynoldsFn (G := G) (fun i => A i i) x / A.trace)
          * ∏ a, ((occ x a).descFactorial (α a) : ℝ) = 0) := by
  intro hband
  have h0 := hband (fun _ => 0) (by simp only [Finset.sum_const_zero]; omega)
  simp only [Nat.descFactorial_zero, Nat.cast_one, Finset.prod_const_one, mul_one] at h0
  exact (transfer_G3_nonzero (G := G) A hA hA0).2.2.2 (by simpa using h0)

end G3

/-! ## Non-vacuity witnesses -/

section Witness

/-- (G1) The gauge is a GENUINE freedom, not a triviality: at `m = 2` with `O` the swap and
`B = diag(1,0)`, the conjugate `OᵀBO = diag(0,1)` is a DIFFERENT multiplicity operator, yet the
lifted term is literally the same.  This is the content of "terminal `H`-irrep labels do not
specify multiplicity coordinates". -/
example :
    let O : Matrix (Fin 2) (Fin 2) ℝ := !![0, 1; 1, 0]
    let B : Matrix (Fin 2) (Fin 2) ℝ := !![1, 0; 0, 0]
    O * Oᵀ = 1 ∧ Oᵀ * B * O ≠ B := by
  refine ⟨?_, ?_⟩
  · ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two]
  · intro h
    have := congrFun (congrFun h 0) 0
    simp [Matrix.mul_apply, Fin.sum_univ_two] at this

/-- (G1) and with that `O`, the lifted terms genuinely agree for every `Q`. -/
example (Q : Matrix (Fin 3) (Fin 2) ℝ) :
    let O : Matrix (Fin 2) (Fin 2) ℝ := !![0, 1; 1, 0]
    let B : Matrix (Fin 2) (Fin 2) ℝ := !![1, 0; 0, 0]
    (Q * O) * (Oᵀ * B * O) * (Q * O)ᵀ = Q * B * Qᵀ := by
  refine gauge_term Q _ _ ?_
  ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two]

/-- (G3) Non-vacuity: the identity matrix on a two-point set is PSD with nonzero trace, so the
hypotheses of `transfer_G3` are jointly satisfiable. -/
example : (1 : Matrix (Fin 2) (Fin 2) ℝ).PosSemidef ∧ (1 : Matrix (Fin 2) (Fin 2) ℝ).trace ≠ 0 := by
  refine ⟨Matrix.PosSemidef.one, ?_⟩
  simp [Matrix.trace, Matrix.diag]

/-- (G3) Non-vacuity at the paper's quantifier: the identity is PSD and nonzero, so
`transfer_G3_nonzero`'s hypotheses are jointly satisfiable, and its trace is genuinely positive. -/
example : (0:ℝ) < (1 : Matrix (Fin 2) (Fin 2) ℝ).trace :=
  psd_trace_pos_of_ne_zero Matrix.PosSemidef.one (by
    intro h
    have := congrFun (congrFun h 0) 0
    simp at this)

/-- (G2) Non-vacuity witness: the SIGN representation of `S₂` on `ℚ`.  Here the whole space is a
nontrivial satellite, so the augmentation submodule contains a NONZERO vector and the Reynolds
projection genuinely kills something. -/
private def signRep : Equiv.Perm (Fin 2) →* (ℚ →ₗ[ℚ] ℚ) where
  toFun g := ((Equiv.Perm.sign g : ℤ) : ℚ) • LinearMap.id
  map_one' := by ext; simp
  map_mul' g h := by ext; simp [mul_comm]

private lemma univ_perm_closed :
    ∀ g ∈ (univ : Finset (Equiv.Perm (Fin 2))), ∀ h ∈ (univ : Finset (Equiv.Perm (Fin 2))),
      g * h ∈ (univ : Finset (Equiv.Perm (Fin 2))) := fun _ _ _ _ => Finset.mem_univ _

/-- The generator `ρ(swap)·1 − 1 = −2` is a NONZERO member of the augmentation submodule. -/
private lemma neg_two_mem_augment :
    (-2 : ℚ) ∈ augment signRep (univ : Finset (Equiv.Perm (Fin 2))) := by
  refine Submodule.subset_span ⟨Equiv.swap 0 1, Finset.mem_univ _, 1, ?_⟩
  simp [signRep, Equiv.Perm.sign_swap (by decide : (0 : Fin 2) ≠ 1)]
  norm_num

/-- Hence the Reynolds projection kills a nonzero vector — `transfer_G2_satellite` is not
vacuous, and neither is the characterization. -/
example : reynolds signRep (univ : Finset (Equiv.Perm (Fin 2))) (-2 : ℚ) = 0
    ∧ (-2 : ℚ) ≠ 0 :=
  ⟨reynolds_eq_zero_of_mem_augment signRep _ univ_perm_closed _ neg_two_mem_augment, by norm_num⟩

example : reynolds signRep (univ : Finset (Equiv.Perm (Fin 2))) (-2 : ℚ) = 0
    ∧ reynolds signRep (univ : Finset (Equiv.Perm (Fin 2))) (-2 : ℚ)
        = reynolds signRep univ (reynolds signRep univ (-2 : ℚ)) := by
  have h := transfer_G2_satellite signRep (univ : Finset (Equiv.Perm (Fin 2)))
    ⟨1, Finset.mem_univ _⟩ univ_perm_closed (-2 : ℚ) neg_two_mem_augment
  exact ⟨h.1, by rw [h.1, map_zero]⟩

/-- (G2) at the manuscript's own hypothesis, non-vacuously: `-2` is a NONZERO vector lying in a
nontrivial satellite of the sign representation (the whole line is one — the sign rep has no
invariants), so `transfer_G2_of_satellite` is not about an empty class. -/
example : InNontrivialSatellite signRep (univ : Finset (Equiv.Perm (Fin 2))) (-2 : ℚ)
    ∧ (-2 : ℚ) ≠ 0 :=
  ⟨(inNontrivialSatellite_iff_mem_augment signRep (univ : Finset (Equiv.Perm (Fin 2)))
      ⟨1, Finset.mem_univ _⟩ univ_perm_closed (-2 : ℚ)).mpr neg_two_mem_augment, by norm_num⟩

example : reynolds signRep (univ : Finset (Equiv.Perm (Fin 2))) (-2 : ℚ) = 0 :=
  (transfer_G2_of_satellite signRep (univ : Finset (Equiv.Perm (Fin 2)))
    ⟨1, Finset.mem_univ _⟩ univ_perm_closed (-2 : ℚ)
    ((inNontrivialSatellite_iff_mem_augment signRep _ ⟨1, Finset.mem_univ _⟩
      univ_perm_closed _).mpr neg_two_mem_augment)).1

end Witness

#print axioms InNontrivialSatellite
#print axioms reynolds_of_invariant
#print axioms reynolds_mem_invariant
#print axioms inNontrivialSatellite_iff_mem_augment
#print axioms transfer_G2_of_satellite
#print axioms gauge_term
#print axioms gauge_sum
#print axioms reynolds_univ_comp
#print axioms transfer_G2
#print axioms reynolds_smul_eq
#print axioms reynolds_eq_zero_of_mem_augment
#print axioms mem_augment_of_reynolds_eq_zero
#print axioms reynolds_eq_zero_iff_mem_augment
#print axioms transfer_G2_satellite
#print axioms reynoldsFn_sum
#print axioms reynoldsFn_invariant
#print axioms transfer_G3
#print axioms psd_eq_zero_of_trace_eq_zero
#print axioms psd_trace_pos_of_ne_zero
#print axioms transfer_G3_nonzero
#print axioms transfer_G3_pure_high_degree_zero

end KsumAudit.Obstructions.Transfer
