/-
# `lem:band-multiplication` — Band multiplication under `S_N` averaging

LaTeX: `ksum/paper/ksum_small_alphabet.tex`, label `lem:band-multiplication`, line 944,
displayed equation (45).
DAG node: `KSUM.B4b.L2.BANDMULT` (`ksum/proof-dag/nodes/KSUM.B4b.L2.BANDMULT.yaml`, PROVED).

## The quantifier structure the LaTeX asserts (written out BEFORE formalizing)

∀ finite alphabets `A`; ∀ `m`; ∀ NONZERO signed measures `μ_j` on the occupancy vectors of fixed
total `N_j`; ∀ orders `d_j` such that `μ_j` annihilates every falling-factorial row below order
`d_j`:  let `ν` be the global occupancy pushforward of the `S_N`-average of the product of the
uniformly orbit-lifted block measures (`N = ∑_j N_j`).  Then
  (a) `ν` is nonzero,
  (b) `ν` annihilates every falling-factorial row below `∑_j d_j`,
  (c) hence normalizing by its actual `ℓ¹` norm is legal and preserves the band,
  (d) if the block measures are invariant under a common value group, so is the normalized
      average.

## SCOPE — what is and is not formalized here (read together with the artifact)

Formalized in full:

  * `descFactorial_add`, the falling-factorial Vandermonde identity that drives equation (45);
  * clause (b) — "annihilation bands ADD" — for two blocks, at FULL generality in the alphabet,
    both block index types, both occupancies, both measures and both orders `d₁, d₂`;
  * the three-block case, obtained by composing the two-block theorem;
  * **the general `m`-block statement, `band_add_fin`** (added by the 2026-07-30 T3 audit): for
    EVERY `m`, every family of block index types `I : Fin m → Type`, occupancies, measures and
    orders `d : Fin m → ℕ`, the `m`-fold convolution annihilates every falling-factorial row of
    order below `∑_i d i`.  This is the paper's own quantifier ("blocks `j ∈ [m]`", bands
    `∑_j d_j`); before the audit only `m = 2, 3` were stated, which was NARROWER than both the
    LaTeX and the node claim of `KSUM.B4b.L2.BANDMULT`;
  * clause (c): rescaling by any constant preserves every vanishing moment.

**2026-07-31 gap-closure batch 1, item L-2.**  Clauses (a) and (d) are now PROVED, in the
`Nonzero` and `ValueGroup` sections below:

  * clause (a) is the paper's own integral-domain argument, formalized: the generating polynomial
    of an occupancy measure is an element of `MvPolynomial A ℚ` (`genPoly`), its coefficients ARE
    the occupancy pushforward (`coeff_genPoly`), the generating polynomial of a convolution is the
    PRODUCT of the generating polynomials (`genPoly_mul`), and `MvPolynomial A ℚ` is an integral
    domain — so a convolution of measures with nonzero pushforward has nonzero pushforward
    (`push_conv_ne_zero`);
  * clause (d) is `isValueInvariant_conv`, with the measure-level consequence
    `moment_of_isValueInvariant` (invariance really does transport to the moments) and
    `isValueInvariant_smul` (rescaling, i.e. clause (c)'s normalization, preserves it).

NOT formalized (reported, not worked around):

  * the reduction "`S_N`-average of the orbit-lifted product has occupancy pushforward equal to
    the CONVOLUTION `μ₁ * ⋯ * μ_m`" (the paper's hypergeometric block split).  The convolution is
    taken here as the definition of `ν`, exactly as the paper's own displayed computation (45)
    does.  **Half of this is now on disk**: `KsumAudit/FactorialFiltration.lean` proves the uniform
    orbit lift and its pushforward / `ℓ¹` identities (`sum_uniformLift_comp`, `l1_uniformLift`),
    which is the "orbit sizes cancel" step in isolation.  What remains is the block splitting
    `A^{N₁+N₂} ≃ A^{N₁} × A^{N₂}` together with occupancy additivity across it; the precise
    residual statement is recorded in `ksum/artifacts/ksum_lean_gapclose1_20260731.md`.
-/
import KsumAudit.ObstructionsCore
import Mathlib.Algebra.MvPolynomial.Basic

namespace KsumAudit.Obstructions.BandMult

open Finset KsumAudit.Obstructions

set_option linter.unusedSectionVars false

/-! ## The falling-factorial Vandermonde identity behind equation (45) -/

/-- `(x+y)_k = ∑_{p+q=k} C(k,p) (x)_p (y)_q`: the falling-factorial Vandermonde. -/
theorem descFactorial_add (x y k : ℕ) :
    (x + y).descFactorial k
      = ∑ pq ∈ Finset.antidiagonal k,
          (k.choose pq.1) * x.descFactorial pq.1 * y.descFactorial pq.2 := by
  rw [Nat.descFactorial_eq_factorial_mul_choose, Nat.add_choose_eq, Finset.mul_sum]
  refine Finset.sum_congr rfl fun pq hpq => ?_
  obtain ⟨p, q⟩ := pq
  have hpq' : p + q = k := Finset.mem_antidiagonal.mp hpq
  have hp : p ≤ k := by omega
  have hq : q = k - p := by omega
  have hk : k.choose p * Nat.factorial p * Nat.factorial q = Nat.factorial k := by
    rw [hq]; exact Nat.choose_mul_factorial_mul_factorial hp
  rw [Nat.descFactorial_eq_factorial_mul_choose, Nat.descFactorial_eq_factorial_mul_choose]
  calc Nat.factorial k * (x.choose p * y.choose q)
      = (k.choose p * Nat.factorial p * Nat.factorial q) * (x.choose p * y.choose q) := by
        rw [hk]
    _ = k.choose p * (Nat.factorial p * x.choose p) * (Nat.factorial q * y.choose q) := by ring

/-! ## Occupancy moments -/

variable {A : Type*} [Fintype A] [DecidableEq A]

/-- The falling-factorial moment `M_μ(α) = ∑_i μ(i) ∏_a (n_a(i))_{α_a}` of equation (45). -/
def moment {I : Type*} [Fintype I] (occ : I → A → ℕ) (μ : I → ℚ) (α : A → ℕ) : ℚ :=
  ∑ i, μ i * ∏ a, ((occ i a).descFactorial (α a) : ℚ)

/-- The order `|α|` of a falling-factorial row. -/
def order (α : A → ℕ) : ℕ := ∑ a, α a

/-! ## Clause (b): annihilation bands add -/

/-- **`lem:band-multiplication`, two blocks.**
If block `1` annihilates every row below order `d₁` and block `2` every row below order `d₂`,
then their convolution annihilates every row below order `d₁ + d₂`.  Fully quantified over the
alphabet, both index types, both occupancies, both measures and both orders. -/
theorem band_add {I J : Type*} [Fintype I] [Fintype J]
    (occ₁ : I → A → ℕ) (μ₁ : I → ℚ) (occ₂ : J → A → ℕ) (μ₂ : J → ℚ) (d₁ d₂ : ℕ)
    (h₁ : ∀ α, order α < d₁ → moment occ₁ μ₁ α = 0)
    (h₂ : ∀ β, order β < d₂ → moment occ₂ μ₂ β = 0)
    (γ : A → ℕ) (hγ : order γ < d₁ + d₂) :
    moment (fun p : I × J => fun a => occ₁ p.1 a + occ₂ p.2 a)
      (fun p : I × J => μ₁ p.1 * μ₂ p.2) γ = 0 := by
  classical
  set P : Finset (∀ _ : A, ℕ × ℕ) := Fintype.piFinset (fun a => Finset.antidiagonal (γ a)) with hP
  set C : (∀ _ : A, ℕ × ℕ) → ℚ := fun π => ∏ a, ((γ a).choose (π a).1 : ℚ) with hC
  set U : (∀ _ : A, ℕ × ℕ) → I → ℚ :=
    fun π i => ∏ a, ((occ₁ i a).descFactorial (π a).1 : ℚ) with hU
  set V : (∀ _ : A, ℕ × ℕ) → J → ℚ :=
    fun π j => ∏ a, ((occ₂ j a).descFactorial (π a).2 : ℚ) with hV
  have hexp : ∀ (i : I) (j : J),
      (∏ a, (((occ₁ i a + occ₂ j a).descFactorial (γ a) : ℕ) : ℚ))
        = ∑ π ∈ P, C π * U π i * V π j := by
    intro i j
    have hstep : ∀ a : A, (((occ₁ i a + occ₂ j a).descFactorial (γ a) : ℕ) : ℚ)
        = ∑ pq ∈ Finset.antidiagonal (γ a), (((γ a).choose pq.1 : ℚ)
            * ((occ₁ i a).descFactorial pq.1 : ℚ) * ((occ₂ j a).descFactorial pq.2 : ℚ)) := by
      intro a
      rw [descFactorial_add]
      push_cast
      rfl
    rw [Finset.prod_congr rfl (fun a (_ : a ∈ univ) => hstep a), Finset.prod_univ_sum]
    refine Finset.sum_congr rfl fun π _ => ?_
    rw [hC, hU, hV]
    rw [Finset.prod_mul_distrib, Finset.prod_mul_distrib]
  have key : moment (fun p : I × J => fun a => occ₁ p.1 a + occ₂ p.2 a)
      (fun p : I × J => μ₁ p.1 * μ₂ p.2) γ
      = ∑ π ∈ P, C π * moment occ₁ μ₁ (fun a => (π a).1)
          * moment occ₂ μ₂ (fun a => (π a).2) := by
    simp only [moment, Fintype.sum_prod_type]
    calc ∑ i : I, ∑ j : J, (μ₁ i * μ₂ j) *
            ∏ a, (((occ₁ i a + occ₂ j a).descFactorial (γ a) : ℕ) : ℚ)
        = ∑ i : I, ∑ j : J, ∑ π ∈ P, (μ₁ i * μ₂ j) * (C π * U π i * V π j) := by
          refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
          rw [hexp i j, Finset.mul_sum]
      _ = ∑ i : I, ∑ π ∈ P, ∑ j : J, (μ₁ i * μ₂ j) * (C π * U π i * V π j) :=
          Finset.sum_congr rfl fun i _ => Finset.sum_comm
      _ = ∑ π ∈ P, ∑ i : I, ∑ j : J, (μ₁ i * μ₂ j) * (C π * U π i * V π j) := Finset.sum_comm
      _ = ∑ π ∈ P, C π * (∑ i : I, μ₁ i * U π i) * (∑ j : J, μ₂ j * V π j) := by
          refine Finset.sum_congr rfl fun π _ => ?_
          rw [mul_assoc, Finset.sum_mul_sum, Finset.mul_sum]
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [Finset.mul_sum]
          exact Finset.sum_congr rfl fun j _ => by ring
  rw [key]
  refine Finset.sum_eq_zero fun π hπ => ?_
  have hmem : ∀ a, (π a).1 + (π a).2 = γ a := fun a =>
    Finset.mem_antidiagonal.mp (Fintype.mem_piFinset.mp hπ a)
  have hord : order (fun a => (π a).1) + order (fun a => (π a).2) = order γ := by
    simp only [order, ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun a _ => hmem a
  rcases Nat.lt_or_ge (order (fun a => (π a).1)) d₁ with h | h
  · rw [h₁ _ h]; ring
  · have hb : order (fun a => (π a).2) < d₂ := by omega
    rw [h₂ _ hb]; ring

/-- **`lem:band-multiplication`, three blocks**, obtained by composing the two-block theorem.
(Superseded in generality by `band_add_fin` below; retained because it is the shape the paper's
own three-block applications use.) -/
theorem band_add_three {I J K : Type*} [Fintype I] [Fintype J] [Fintype K]
    (occ₁ : I → A → ℕ) (μ₁ : I → ℚ) (occ₂ : J → A → ℕ) (μ₂ : J → ℚ)
    (occ₃ : K → A → ℕ) (μ₃ : K → ℚ) (d₁ d₂ d₃ : ℕ)
    (h₁ : ∀ α, order α < d₁ → moment occ₁ μ₁ α = 0)
    (h₂ : ∀ α, order α < d₂ → moment occ₂ μ₂ α = 0)
    (h₃ : ∀ α, order α < d₃ → moment occ₃ μ₃ α = 0)
    (γ : A → ℕ) (hγ : order γ < d₁ + d₂ + d₃) :
    moment (fun p : (I × J) × K => fun a => (occ₁ p.1.1 a + occ₂ p.1.2 a) + occ₃ p.2 a)
      (fun p : (I × J) × K => (μ₁ p.1.1 * μ₂ p.1.2) * μ₃ p.2) γ = 0 :=
  band_add (fun p : I × J => fun a => occ₁ p.1 a + occ₂ p.2 a)
    (fun p : I × J => μ₁ p.1 * μ₂ p.2) occ₃ μ₃ (d₁ + d₂) d₃
    (fun α hα => band_add occ₁ μ₁ occ₂ μ₂ d₁ d₂ h₁ h₂ α hα) h₃ γ hγ

/-! ## Clause (b) at the paper's own quantifier: `m` blocks, `m` arbitrary -/

/-- **`lem:band-multiplication`, general `m`.**

For EVERY `m`, every family of block index types `I : Fin m → Type`, every family of occupancy
maps, every family of signed block measures, and every family of orders `d : Fin m → ℕ`: if block
`i` annihilates every falling-factorial row of order below `d i`, then the `m`-fold convolution
(configuration space `∀ i, I i`; occupancy the coordinatewise sum; measure the product)
annihilates every falling-factorial row of order below `∑ i, d i`.

This is the paper's displayed clause (b) at its own quantifier.  Proof: induction on `m`, the
inductive step being exactly `band_add` applied to (block `0`) against (the convolution of the
remaining `m` blocks), transported along `Fin.consEquiv`. -/
theorem band_add_fin :
    ∀ (m : ℕ) (I : Fin m → Type) [∀ i, Fintype (I i)]
      (occ : ∀ i, I i → A → ℕ) (μ : ∀ i, I i → ℚ) (d : Fin m → ℕ),
      (∀ (i : Fin m) (α : A → ℕ), order α < d i → moment (occ i) (μ i) α = 0) →
      ∀ γ : A → ℕ, order γ < ∑ i, d i →
      moment (fun p : (∀ i, I i) => fun a => ∑ i, occ i (p i) a)
        (fun p : (∀ i, I i) => ∏ i, μ i (p i)) γ = 0 := by
  intro m
  induction m with
  | zero =>
      intro I _ occ μ d h γ hγ
      simp only [Finset.univ_eq_empty, Finset.sum_empty] at hγ
      exact absurd hγ (Nat.not_lt_zero _)
  | succ m ih =>
      intro I _ occ μ d h γ hγ
      have key := band_add (A := A) (occ 0) (μ 0)
        (fun p : (∀ i : Fin m, I i.succ) => fun a => ∑ i, occ i.succ (p i) a)
        (fun p : (∀ i : Fin m, I i.succ) => ∏ i, μ i.succ (p i))
        (d 0) (∑ i : Fin m, d i.succ)
        (fun α hα => h 0 α hα)
        (fun β hβ => ih (fun i => I i.succ) (fun i => occ i.succ) (fun i => μ i.succ)
          (fun i => d i.succ) (fun i α hα => h i.succ α hα) β hβ)
        γ (by rw [Fin.sum_univ_succ] at hγ; exact hγ)
      rw [← key]
      refine (Fintype.sum_equiv (Fin.consEquiv I) _ _ ?_).symm
      intro z
      obtain ⟨x, p⟩ := z
      simp [Fin.consEquiv, Fin.prod_univ_succ, Fin.sum_univ_succ]

/-! ## Clause (c): rescaling is legal and preserves the band -/

theorem moment_const_mul {I : Type*} [Fintype I] (occ : I → A → ℕ) (μ : I → ℚ) (c : ℚ)
    (α : A → ℕ) : moment occ (fun i => c * μ i) α = c * moment occ μ α := by
  simp only [moment, Finset.mul_sum]
  exact Finset.sum_congr rfl fun i _ => by ring

/-- Normalizing by any constant (in particular by the actual `ℓ¹` norm) preserves every
vanishing moment, so it preserves the band. -/
theorem band_preserved_by_scaling {I : Type*} [Fintype I] (occ : I → A → ℕ) (μ : I → ℚ)
    (d : ℕ) (h : ∀ α, order α < d → moment occ μ α = 0) (c : ℚ) :
    ∀ α, order α < d → moment occ (fun i => c * μ i) α = 0 := by
  intro α hα
  rw [moment_const_mul, h α hα, mul_zero]

/-! ## Clause (a): the convolution is nonzero — the paper's integral-domain argument

The paper: *"Convolution is nonzero because the finite generating polynomials of the nonzero `μ_j`
have nonzero product in an integral domain."*  The generating polynomial of an occupancy measure
`(occ, μ)` is `∑_i μ_i ∏_a X_a^{occ_i(a)} ∈ MvPolynomial A ℚ`; its coefficient at the monomial `n`
is the OCCUPANCY PUSHFORWARD `∑_{i : occ i = n} μ_i`, which is what "`ν ≠ 0`" is about (the
index-level product measure is trivially nonzero; the content is that no cancellation collapses the
pushforward). -/

section Nonzero

/-- The occupancy pushforward: the total weight carried by a given occupancy vector. -/
def push {I : Type*} [Fintype I] [DecidableEq (A → ℕ)] (occ : I → A → ℕ) (μ : I → ℚ)
    (n : A → ℕ) : ℚ :=
  ∑ i ∈ univ.filter (fun i => occ i = n), μ i

/-- The generating polynomial `∑_i μ_i ∏_a X_a^{occ_i(a)}` of the paper's proof. -/
noncomputable def genPoly {I : Type*} [Fintype I] (occ : I → A → ℕ) (μ : I → ℚ) :
    MvPolynomial A ℚ :=
  ∑ i, MvPolynomial.monomial (Finsupp.equivFunOnFinite.symm (occ i)) (μ i)

private lemma equivFunOnFinite_symm_add (m n : A → ℕ) :
    (Finsupp.equivFunOnFinite.symm (fun a => m a + n a) : A →₀ ℕ)
      = Finsupp.equivFunOnFinite.symm m + Finsupp.equivFunOnFinite.symm n := by
  ext a
  simp

/-- **The coefficients of the generating polynomial ARE the occupancy pushforward.** -/
theorem coeff_genPoly {I : Type*} [Fintype I] [DecidableEq (A → ℕ)] (occ : I → A → ℕ) (μ : I → ℚ)
    (n : A → ℕ) :
    MvPolynomial.coeff (Finsupp.equivFunOnFinite.symm n) (genPoly occ μ) = push occ μ n := by
  unfold genPoly push
  rw [MvPolynomial.coeff_sum, Finset.sum_filter]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [MvPolynomial.coeff_monomial]
  by_cases h : occ i = n
  · rw [if_pos h, if_pos (by rw [h])]
  · rw [if_neg h, if_neg]
    intro hc
    exact h (Finsupp.equivFunOnFinite.symm.injective hc)

/-- **The generating polynomial of a convolution is the product of the generating polynomials.** -/
theorem genPoly_mul {I J : Type*} [Fintype I] [Fintype J]
    (occ₁ : I → A → ℕ) (μ₁ : I → ℚ) (occ₂ : J → A → ℕ) (μ₂ : J → ℚ) :
    genPoly (fun p : I × J => fun a => occ₁ p.1 a + occ₂ p.2 a) (fun p : I × J => μ₁ p.1 * μ₂ p.2)
      = genPoly occ₁ μ₁ * genPoly occ₂ μ₂ := by
  unfold genPoly
  rw [Finset.sum_mul_sum, Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
  rw [MvPolynomial.monomial_mul, equivFunOnFinite_symm_add]

/-- A measure has a nonzero pushforward exactly when its generating polynomial is nonzero. -/
theorem push_ne_zero_iff {I : Type*} [Fintype I] [DecidableEq (A → ℕ)]
    (occ : I → A → ℕ) (μ : I → ℚ) :
    (∃ n, push occ μ n ≠ 0) ↔ genPoly occ μ ≠ 0 := by
  constructor
  · rintro ⟨n, hn⟩ h0
    apply hn
    rw [← coeff_genPoly occ μ n, h0, MvPolynomial.coeff_zero]
  · intro h
    obtain ⟨d, hd⟩ := MvPolynomial.ne_zero_iff.mp h
    refine ⟨Finsupp.equivFunOnFinite d, ?_⟩
    rw [← coeff_genPoly occ μ (Finsupp.equivFunOnFinite d)]
    simpa using hd

/-- **`lem:band-multiplication`, clause (a).**  The convolution of two occupancy measures with
nonzero pushforward has nonzero pushforward — so its `ℓ¹` norm is positive and the normalization
of clause (c) is legal.  This is the paper's integral-domain argument, verbatim. -/
theorem push_conv_ne_zero {I J : Type*} [Fintype I] [Fintype J] [DecidableEq (A → ℕ)]
    (occ₁ : I → A → ℕ) (μ₁ : I → ℚ) (occ₂ : J → A → ℕ) (μ₂ : J → ℚ)
    (h₁ : ∃ n, push occ₁ μ₁ n ≠ 0) (h₂ : ∃ n, push occ₂ μ₂ n ≠ 0) :
    ∃ n, push (fun p : I × J => fun a => occ₁ p.1 a + occ₂ p.2 a)
      (fun p : I × J => μ₁ p.1 * μ₂ p.2) n ≠ 0 := by
  rw [push_ne_zero_iff] at h₁ h₂ ⊢
  rw [genPoly_mul]
  exact mul_ne_zero h₁ h₂

end Nonzero

/-! ## Clause (d): invariance under a common value group

*"If the block measures are invariant under a common value group, so is the normalized average."*
A value-group element is a permutation `σ` of the alphabet; a block measure is `σ`-invariant when
relabelling the alphabet by `σ` is realized by a relabelling of its own carrier. -/

section ValueGroup

/-- `(occ, μ)` is invariant under the value-alphabet permutation `σ`. -/
def IsValueInvariant {I : Type*} [Fintype I] (occ : I → A → ℕ) (μ : I → ℚ)
    (σ : Equiv.Perm A) : Prop :=
  ∃ e : I ≃ I, (∀ i, μ (e i) = μ i) ∧ (∀ i a, occ (e i) a = occ i (σ a))

/-- **`lem:band-multiplication`, clause (d).**  If both block measures are invariant under the same
value-group element, so is their convolution. -/
theorem isValueInvariant_conv {I J : Type*} [Fintype I] [Fintype J]
    (occ₁ : I → A → ℕ) (μ₁ : I → ℚ) (occ₂ : J → A → ℕ) (μ₂ : J → ℚ) (σ : Equiv.Perm A)
    (h₁ : IsValueInvariant occ₁ μ₁ σ) (h₂ : IsValueInvariant occ₂ μ₂ σ) :
    IsValueInvariant (fun p : I × J => fun a => occ₁ p.1 a + occ₂ p.2 a)
      (fun p : I × J => μ₁ p.1 * μ₂ p.2) σ := by
  obtain ⟨e₁, hμ₁, ho₁⟩ := h₁
  obtain ⟨e₂, hμ₂, ho₂⟩ := h₂
  refine ⟨e₁.prodCongr e₂, fun p => ?_, fun p a => ?_⟩
  · show μ₁ (e₁ p.1) * μ₂ (e₂ p.2) = μ₁ p.1 * μ₂ p.2
    rw [hμ₁, hμ₂]
  · show occ₁ (e₁ p.1) a + occ₂ (e₂ p.2) a = occ₁ p.1 (σ a) + occ₂ p.2 (σ a)
    rw [ho₁, ho₂]

/-- Clause (d) survives clause (c)'s rescaling: the `ℓ¹` normalization is a scalar multiple. -/
theorem isValueInvariant_smul {I : Type*} [Fintype I] (occ : I → A → ℕ) (μ : I → ℚ)
    (σ : Equiv.Perm A) (c : ℚ) (h : IsValueInvariant occ μ σ) :
    IsValueInvariant occ (fun i => c * μ i) σ := by
  obtain ⟨e, hμ, ho⟩ := h
  refine ⟨e, fun i => ?_, ho⟩
  show c * μ (e i) = c * μ i
  rw [hμ]

/-- Value invariance is not a formal decoration: it transports to the falling-factorial moments,
which is what the band statement is about. -/
theorem moment_of_isValueInvariant {I : Type*} [Fintype I] (occ : I → A → ℕ) (μ : I → ℚ)
    (σ : Equiv.Perm A) (h : IsValueInvariant occ μ σ) (α : A → ℕ) :
    moment occ μ (fun a => α (σ a)) = moment occ μ α := by
  obtain ⟨e, hμ, ho⟩ := h
  unfold moment
  rw [← Fintype.sum_equiv e (fun i => μ (e i) * ∏ a, ((occ (e i) a).descFactorial (α (σ a)) : ℚ))
    (fun i => μ i * ∏ a, ((occ i a).descFactorial (α (σ a)) : ℚ)) (fun i => rfl)]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [hμ]
  congr 1
  rw [Finset.prod_congr rfl (fun a (_ : a ∈ univ) => by rw [ho i a])]
  exact Fintype.prod_equiv σ _ _ (fun a => rfl)

end ValueGroup

/-! ## Non-vacuity witness

Alphabet `Fin 1`; one block with occupancies `0, 1` and weights `+1, -1`.  Its band is EXACTLY
one (the degree-zero moment vanishes, the degree-one moment does not), so `band_add` applies with
`d₁ = d₂ = 1` and its hypotheses are satisfiable with a genuinely nonzero measure. -/

section Witness

private def wOcc : Fin 2 → Fin 1 → ℕ := fun i _ => (i : ℕ)
private def wMu : Fin 2 → ℚ := ![1, -1]

private lemma wBand : ∀ α : Fin 1 → ℕ, order α < 1 → moment wOcc wMu α = 0 := by
  intro α hα
  have h0 : α 0 = 0 := by
    simp only [order, Fin.sum_univ_one] at hα
    omega
  simp [moment, Fin.sum_univ_two,h0, wOcc, wMu]

/-- The block measure is genuinely nonzero: its order-one moment is `-1 ≠ 0`, so the band `d = 1`
is tight and the hypotheses of `band_add` are not vacuous. -/
private lemma wNonzero : moment wOcc wMu (fun _ => 1) = -1 := by
  simp [moment, Fin.sum_univ_two,wOcc, wMu]

example : moment wOcc wMu (fun _ => 1) ≠ 0 := by rw [wNonzero]; norm_num

/-- Two such blocks annihilate every row of order below `2`. -/
example (γ : Fin 1 → ℕ) (hγ : order γ < 2) :
    moment (fun p : Fin 2 × Fin 2 => fun a => wOcc p.1 a + wOcc p.2 a)
      (fun p : Fin 2 × Fin 2 => wMu p.1 * wMu p.2) γ = 0 :=
  band_add wOcc wMu wOcc wMu 1 1 wBand wBand γ hγ

/-- Non-vacuity of the general-`m` theorem: five copies of the same nonzero block annihilate
every row of order below `5`, and the hypothesis family is inhabited. -/
example (γ : Fin 1 → ℕ) (hγ : order γ < 5) :
    moment (fun p : (∀ _ : Fin 5, Fin 2) => fun a => ∑ i : Fin 5, wOcc (p i) a)
      (fun p : (∀ _ : Fin 5, Fin 2) => ∏ i : Fin 5, wMu (p i)) γ = 0 := by
  refine band_add_fin 5 (fun _ => Fin 2) (fun _ => wOcc) (fun _ => wMu) (fun _ => 1)
    (fun _ α hα => wBand α hα) γ ?_
  simpa using hγ

/-- The one-block witness has a genuinely nonzero occupancy pushforward. -/
private lemma wPush_ne_zero : push wOcc wMu (fun _ => 0) ≠ 0 := by
  have hfil : (univ.filter (fun i : Fin 2 => wOcc i = (fun _ => 0))) = {0} := by decide
  unfold push
  rw [hfil, Finset.sum_singleton]
  norm_num [wMu]

/-- Clause (a) is not vacuous: the one-block witness has nonzero pushforward, hence so does its
self-convolution — whose band is `1 + 1 = 2` by `band_add`. -/
example : ∃ n, push (fun p : Fin 2 × Fin 2 => fun a => wOcc p.1 a + wOcc p.2 a)
    (fun p : Fin 2 × Fin 2 => wMu p.1 * wMu p.2) n ≠ 0 :=
  push_conv_ne_zero wOcc wMu wOcc wMu ⟨fun _ => 0, wPush_ne_zero⟩ ⟨fun _ => 0, wPush_ne_zero⟩

/-- Clause (d) is not vacuous: over the one-letter alphabet the only value permutation is the
identity, the witness block is invariant under it, and the convolution therefore is too. -/
example : IsValueInvariant (fun p : Fin 2 × Fin 2 => fun a => wOcc p.1 a + wOcc p.2 a)
    (fun p : Fin 2 × Fin 2 => wMu p.1 * wMu p.2) (1 : Equiv.Perm (Fin 1)) :=
  isValueInvariant_conv wOcc wMu wOcc wMu 1
    ⟨Equiv.refl _, fun _ => rfl, fun _ _ => rfl⟩ ⟨Equiv.refl _, fun _ => rfl, fun _ _ => rfl⟩

end Witness

#print axioms push
#print axioms genPoly
#print axioms coeff_genPoly
#print axioms genPoly_mul
#print axioms push_ne_zero_iff
#print axioms push_conv_ne_zero
#print axioms isValueInvariant_conv
#print axioms isValueInvariant_smul
#print axioms moment_of_isValueInvariant
#print axioms descFactorial_add
#print axioms band_add
#print axioms band_add_three
#print axioms band_add_fin
#print axioms moment_const_mul
#print axioms band_preserved_by_scaling

end KsumAudit.Obstructions.BandMult
