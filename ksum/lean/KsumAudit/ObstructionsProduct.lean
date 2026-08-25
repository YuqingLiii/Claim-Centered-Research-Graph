/-
# `thm:product-obstruction` — Locally balanced sign-separated products

LaTeX: `ksum/paper/ksum_small_alphabet.tex`, Theorem "Locally balanced sign-separated
products", label `thm:product-obstruction`, line 983, displayed equation (47).
DAG node: `KSUM.B4b.L2.M2` (`ksum/proof-dag/nodes/KSUM.B4b.L2.M2.yaml`, status PROVED).

## The quantifier structure the LaTeX asserts (written out BEFORE formalizing)

∀ odd `q ≥ 5`, ∀ `N ≥ 1`, ∀ `t ∈ ℤ_q`, with `r = (q-1)/2`,
∀ signed measures `μ` on `ℤ_q^N` in the five-condition class

  (1) fixed-point occupancy at most one, **so NO is the all-axis event**;
  (2) every product component has one nonzero local signed factor on every nonfixed pair;
  (3) after a local sign orientation, every factor is nonpositive on its axis, nonnegative in
      its interior, and has total mass zero;
  (4) local shapes, nonzero scales, pair totals, and support sizes are ARBITRARY;
  (5) only nonnegative mixtures of products with the common axis/interior sign pattern are taken:

  after unit-ℓ¹ normalization and global sign orientation,
  `⟨μ, F⟩ = 2^{1-r} = 2^{1-(q-1)/2} ≤ 1/2`.

Note this is an EQUALITY: no member of the class beats `2^{1-r}` and none falls below it.

## How each clause is rendered here

* the `r` nonfixed σ-pairs → an arbitrary finite index type `ι`, `Fintype.card ι = r`;
* clause 4 ("local shapes, nonzero scales, pair totals, support sizes arbitrary") → an
  ARBITRARY family of finite local state types `Ω c` with an ARBITRARY decidable predicate
  `axis c` marking the one-sided (axis) local states.  Nothing about `ℤ_q`, occupancy numbers,
  `N` or `t` is used anywhere below — which is precisely what clause 4 grants;
* clause 3 → the `IsLocalFactor` structure; clause 2 → its `nonzero` field;
* clause 1 → deliberately NOT baked into a definition.  It appears as the explicit hypothesis
  `hNO : ∀ x, no x ↔ ∀ c, axis c (x c)` relating an abstract NO-predicate to the all-axis
  event, so the reader can see exactly what condition 1 buys;
* clause 5 → `product_obstruction_mixture`.
-/
import KsumAudit.ObstructionsCore

namespace KsumAudit.Obstructions.Product

open Finset KsumAudit.Obstructions

set_option linter.unusedSectionVars false

variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {Ω : ι → Type*} [∀ c, Fintype (Ω c)] [∀ c, DecidableEq (Ω c)]

/- `axis c` marks the one-sided ("axis") local states of nonfixed σ-pair `c`; its complement is
the "interior" (two-sided, i.e. hit) local states. -/
variable (axis : ∀ c, Ω c → Prop) [∀ c, DecidablePred (axis c)]

/-- Clauses 2–3 of the class of `thm:product-obstruction`, for a single local factor:
after the local sign orientation the factor is nonpositive on the axis, nonnegative in the
interior, has total mass zero, and is not identically zero. -/
structure IsLocalFactor (c : ι) (g : Ω c → ℚ) : Prop where
  axis_nonpos : ∀ ω, axis c ω → g ω ≤ 0
  interior_nonneg : ∀ ω, ¬ axis c ω → 0 ≤ g ω
  total_zero : ∑ ω, g ω = 0
  nonzero : ∃ ω, g ω ≠ 0

/-- The product measure `⨂_c f_c` on the configuration space `∀ c, Ω c`. -/
def prodMeasure (f : ∀ c, Ω c → ℚ) (x : ∀ c, Ω c) : ℚ := ∏ c, f c (x c)

/-- The absolute axis mass `a_c` of a local factor. -/
def axisMass (c : ι) (g : Ω c → ℚ) : ℚ := ∑ ω ∈ univ.filter (axis c), -g ω

/-- `∏_c a_c`, the quantity the whole obstruction is expressed in. -/
def prodAxisMass (f : ∀ c, Ω c → ℚ) : ℚ := ∏ c, axisMass axis c (f c)

/-! ## Local consequences of clauses 2–3 -/

section LocalFacts

variable {axis} {c : ι} {g : Ω c → ℚ}

lemma axis_sum_eq (_hg : IsLocalFactor axis c g) :
    ∑ ω ∈ univ.filter (axis c), g ω = -axisMass axis c g := by
  simp only [axisMass, Finset.sum_neg_distrib, neg_neg]

/-- Clause 3 (nonpositive on the axis) makes `a_c ≥ 0`. -/
lemma axisMass_nonneg (hg : IsLocalFactor axis c g) : 0 ≤ axisMass axis c g :=
  Finset.sum_nonneg fun ω hω => by
    have := hg.axis_nonpos ω (Finset.mem_filter.mp hω).2; linarith

/-- Clause 3 (zero total mass) forces the interior mass to be exactly `+a_c`. -/
lemma interior_sum_eq (hg : IsLocalFactor axis c g) :
    ∑ ω ∈ univ.filter (fun ω => ¬ axis c ω), g ω = axisMass axis c g := by
  have hsplit : (∑ ω ∈ univ.filter (axis c), g ω)
      + ∑ ω ∈ univ.filter (fun ω => ¬ axis c ω), g ω = ∑ ω, g ω :=
    Finset.sum_filter_add_sum_filter_not _ _ _
  rw [axis_sum_eq hg, hg.total_zero] at hsplit
  linarith

/-- Clause 3 forces the local ℓ¹ norm to be exactly `2 a_c`. -/
lemma l1_local (hg : IsLocalFactor axis c g) :
    ∑ ω, |g ω| = 2 * axisMass axis c g := by
  have hsplit : (∑ ω ∈ univ.filter (axis c), |g ω|)
      + ∑ ω ∈ univ.filter (fun ω => ¬ axis c ω), |g ω| = ∑ ω, |g ω| :=
    Finset.sum_filter_add_sum_filter_not _ _ _
  have h1 : ∑ ω ∈ univ.filter (axis c), |g ω| = axisMass axis c g := by
    rw [axisMass]
    refine Finset.sum_congr rfl fun ω hω => ?_
    rw [abs_of_nonpos (hg.axis_nonpos ω (Finset.mem_filter.mp hω).2)]
  have h2 : ∑ ω ∈ univ.filter (fun ω => ¬ axis c ω), |g ω| = axisMass axis c g := by
    rw [← interior_sum_eq hg]
    refine Finset.sum_congr rfl fun ω hω => ?_
    rw [abs_of_nonneg (hg.interior_nonneg ω (Finset.mem_filter.mp hω).2)]
  rw [h1, h2] at hsplit
  linarith

/-- Clause 2 (a nonzero local factor) forces `a_c > 0`. -/
lemma axisMass_pos (hg : IsLocalFactor axis c g) : 0 < axisMass axis c g := by
  rcases (axisMass_nonneg hg).lt_or_eq with h | h
  · exact h
  · exfalso
    obtain ⟨ω₀, hω₀⟩ := hg.nonzero
    have hax : ∑ ω ∈ univ.filter (axis c), -g ω = 0 := by rw [← axisMass]; exact h.symm
    have haxz : ∀ ω ∈ univ.filter (axis c), -g ω = 0 := by
      refine (Finset.sum_eq_zero_iff_of_nonneg ?_).mp hax
      intro ω hω
      have := hg.axis_nonpos ω (Finset.mem_filter.mp hω).2; linarith
    have hint : ∑ ω ∈ univ.filter (fun ω => ¬ axis c ω), g ω = 0 := by
      rw [interior_sum_eq hg]; exact h.symm
    have hintz : ∀ ω ∈ univ.filter (fun ω => ¬ axis c ω), g ω = 0 := by
      refine (Finset.sum_eq_zero_iff_of_nonneg ?_).mp hint
      intro ω hω
      exact hg.interior_nonneg ω (Finset.mem_filter.mp hω).2
    by_cases hc : axis c ω₀
    · exact hω₀ (by have := haxz ω₀ (Finset.mem_filter.mpr ⟨Finset.mem_univ _, hc⟩); linarith)
    · exact hω₀ (hintz ω₀ (Finset.mem_filter.mpr ⟨Finset.mem_univ _, hc⟩))

end LocalFacts

lemma prodAxisMass_pos (f : ∀ c, Ω c → ℚ) (hf : ∀ c, IsLocalFactor axis c (f c)) :
    0 < prodAxisMass axis f :=
  Finset.prod_pos fun c _ => axisMass_pos (hf c)

/-! ## Factorization of the three global quantities -/

lemma noEvent_eq_piFinset :
    (univ.filter (fun x : (∀ c, Ω c) => ∀ c, axis c (x c)))
      = Fintype.piFinset (fun c => univ.filter (axis c)) := by
  ext x; simp [Fintype.mem_piFinset]

/-- Mass of a product measure on the all-axis event is `(-1)^r ∏_c a_c`. -/
lemma noMass_prodMeasure (f : ∀ c, Ω c → ℚ) (hf : ∀ c, IsLocalFactor axis c (f c)) :
    ∑ x ∈ univ.filter (fun x : (∀ c, Ω c) => ∀ c, axis c (x c)), prodMeasure f x
      = (-1) ^ (Fintype.card ι) * prodAxisMass axis f := by
  rw [noEvent_eq_piFinset]
  simp only [prodMeasure]
  rw [← Finset.prod_univ_sum]
  have hax : ∀ c : ι, ∑ ω ∈ univ.filter (axis c), f c ω = -axisMass axis c (f c) :=
    fun c => axis_sum_eq (hf c)
  rw [Finset.prod_congr rfl (fun c _ => hax c), Finset.prod_neg, Finset.card_univ]
  rfl

/-- The ℓ¹ norm of a product measure is `2^r ∏_c a_c`. -/
lemma l1_prodMeasure (f : ∀ c, Ω c → ℚ) (hf : ∀ c, IsLocalFactor axis c (f c)) :
    l1 (prodMeasure f) = 2 ^ (Fintype.card ι) * prodAxisMass axis f := by
  have h : ∏ c, ∑ ω ∈ (univ : Finset (Ω c)), |f c ω|
      = ∑ x ∈ Fintype.piFinset (fun c => (univ : Finset (Ω c))), ∏ c, |f c (x c)| :=
    Finset.prod_univ_sum _ _
  have hl : l1 (prodMeasure f) = ∏ c, ∑ ω, |f c ω| := by
    rw [l1, h, Fintype.piFinset_univ]
    refine Finset.sum_congr rfl fun x _ => ?_
    simp only [prodMeasure]
    exact Finset.abs_prod _ _
  rw [hl, Finset.prod_congr rfl (fun c (_ : c ∈ univ) => l1_local (hf c)),
    Finset.prod_mul_distrib, Finset.prod_const, Finset.card_univ]
  rfl

/-- The total mass of a product measure vanishes as soon as there is at least one pair. -/
lemma total_prodMeasure_eq_zero (f : ∀ c, Ω c → ℚ) (hf : ∀ c, IsLocalFactor axis c (f c))
    (hι : Nonempty ι) : total (prodMeasure f) = 0 := by
  have h : ∏ c, ∑ ω ∈ (univ : Finset (Ω c)), f c ω
      = ∑ x ∈ Fintype.piFinset (fun c => (univ : Finset (Ω c))), ∏ c, f c (x c) :=
    Finset.prod_univ_sum _ _
  have hl : total (prodMeasure f) = ∏ c, ∑ ω, f c ω := by
    rw [total, h, Fintype.piFinset_univ]; rfl
  obtain ⟨c₀⟩ := hι
  rw [hl]
  exact Finset.prod_eq_zero (Finset.mem_univ c₀) (hf c₀).total_zero

/-! ## The obstruction -/

/-- **`thm:product-obstruction`, exact-value form.**

The correlation of a class member is exactly `-2·(-1)^r·∏_c a_c` and its ℓ¹ norm is exactly
`2^r·∏_c a_c`, with `∏_c a_c > 0`. -/
theorem product_obstruction_exact
    (no : (∀ c, Ω c) → Prop) [DecidablePred no]
    (hNO : ∀ x : (∀ c, Ω c), no x ↔ ∀ c, axis c (x c))
    (f : ∀ c, Ω c → ℚ) (hf : ∀ c, IsLocalFactor axis c (f c))
    (hι : Nonempty ι) :
    corr no (prodMeasure f) = -2 * (-1) ^ (Fintype.card ι) * prodAxisMass axis f
      ∧ l1 (prodMeasure f) = 2 ^ (Fintype.card ι) * prodAxisMass axis f
      ∧ 0 < prodAxisMass axis f := by
  refine ⟨?_, l1_prodMeasure axis f hf, prodAxisMass_pos axis f hf⟩
  have hfilter : (univ.filter no) = univ.filter (fun x : (∀ c, Ω c) => ∀ c, axis c (x c)) := by
    ext x; simp [hNO x]
  rw [corr_of_total_zero _ _ (total_prodMeasure_eq_zero axis f hf hι), hfilter,
    noMass_prodMeasure axis f hf]
  ring

/-- **`thm:product-obstruction`, ratio form.**  `|⟨μ,F⟩| · 2^r = 2‖μ‖₁`. -/
theorem product_obstruction_ratio
    (no : (∀ c, Ω c) → Prop) [DecidablePred no]
    (hNO : ∀ x : (∀ c, Ω c), no x ↔ ∀ c, axis c (x c))
    (f : ∀ c, Ω c → ℚ) (hf : ∀ c, IsLocalFactor axis c (f c))
    (hι : Nonempty ι) :
    |corr no (prodMeasure f)| * 2 ^ (Fintype.card ι) = 2 * l1 (prodMeasure f) := by
  obtain ⟨hc, hn, hp⟩ := product_obstruction_exact axis no hNO f hf hι
  rw [hc, hn]
  have habs : |(-2 : ℚ) * (-1) ^ (Fintype.card ι) * prodAxisMass axis f|
      = 2 * prodAxisMass axis f := by
    rw [abs_mul, abs_of_pos hp, abs_mul, abs_neg, abs_two, abs_pow, abs_neg, abs_one, one_pow,
      mul_one]
  rw [habs]; ring

/-- The ratio form `|v|·2^r = 2` is the value form `|v| = 2^{1-r}`.  (Shared by the single-product
and the mixture statements so that both really do deliver the paper's displayed value.) -/
private lemma abs_eq_two_pow_one_sub {v : ℚ} {r : ℕ} (h : |v| * 2 ^ r = 2) :
    |v| = 2 ^ (1 - (r : ℤ)) := by
  rw [zpow_sub₀ (by norm_num : (2:ℚ) ≠ 0), zpow_one, zpow_natCast]
  field_simp
  linarith [h]

/-- **`thm:product-obstruction`, the paper's displayed equation (47).**
After unit-ℓ¹ normalization, `|⟨μ,F⟩| = 2^{1-r}`. -/
theorem product_obstruction_normalized
    (no : (∀ c, Ω c) → Prop) [DecidablePred no]
    (hNO : ∀ x : (∀ c, Ω c), no x ↔ ∀ c, axis c (x c))
    (f : ∀ c, Ω c → ℚ) (hf : ∀ c, IsLocalFactor axis c (f c))
    (hι : Nonempty ι)
    (hnorm : l1 (prodMeasure f) = 1) :
    |corr no (prodMeasure f)| = 2 ^ (1 - (Fintype.card ι : ℤ)) := by
  have h := product_obstruction_ratio axis no hNO f hf hι
  rw [hnorm, mul_one] at h
  exact abs_eq_two_pow_one_sub h

/-- **`thm:product-obstruction`, the literal `q`-indexed reading.**
`q ≥ 5` odd, `r = (q-1)/2` pairs: the class value is `2^{1-(q-1)/2} ≤ 1/2`. -/
theorem product_obstruction_q
    (q : ℕ) (hq5 : 5 ≤ q) (hr : Fintype.card ι = (q - 1) / 2)
    (no : (∀ c, Ω c) → Prop) [DecidablePred no]
    (hNO : ∀ x : (∀ c, Ω c), no x ↔ ∀ c, axis c (x c))
    (f : ∀ c, Ω c → ℚ) (hf : ∀ c, IsLocalFactor axis c (f c))
    (hnorm : l1 (prodMeasure f) = 1) :
    |corr no (prodMeasure f)| = 2 ^ (1 - (((q - 1) / 2 : ℕ) : ℤ))
      ∧ |corr no (prodMeasure f)| ≤ 1 / 2 := by
  have hr2 : 2 ≤ (q - 1) / 2 := by omega
  have hι : Nonempty ι := by
    rw [← Fintype.card_pos_iff, hr]; omega
  have hval := product_obstruction_normalized axis no hNO f hf hι hnorm
  rw [hr] at hval
  refine ⟨hval, ?_⟩
  rw [hval]
  have hle : (1 : ℤ) - (((q - 1) / 2 : ℕ) : ℤ) ≤ -1 := by
    have : (2 : ℤ) ≤ (((q - 1) / 2 : ℕ) : ℤ) := by exact_mod_cast hr2
    omega
  calc (2:ℚ) ^ (1 - (((q - 1) / 2 : ℕ) : ℤ)) ≤ 2 ^ (-1 : ℤ) :=
        zpow_le_zpow_right₀ (by norm_num) hle
    _ = 1 / 2 := by norm_num

/-! ## Clause 5: nonnegative sign-aligned mixtures -/

/-- Every product in the class has the SAME sign at every configuration, namely
`(-1)^{#axis coordinates}` — independent of which factors are used.  This is exactly the
"common axis/interior sign pattern" of clause 5. -/
lemma sign_aligned (f : ∀ c, Ω c → ℚ) (hf : ∀ c, IsLocalFactor axis c (f c))
    (x : ∀ c, Ω c) :
    0 ≤ (-1 : ℚ) ^ (univ.filter (fun c => axis c (x c))).card * prodMeasure f x := by
  classical
  have hrw : ((-1 : ℚ) ^ (univ.filter (fun c => axis c (x c))).card) * prodMeasure f x
      = ∏ c, (if axis c (x c) then -(f c (x c)) else f c (x c)) := by
    have hpt : ∀ c : ι, (if axis c (x c) then -(f c (x c)) else f c (x c))
        = (if axis c (x c) then (-1 : ℚ) else 1) * f c (x c) := by
      intro c; split <;> ring
    rw [Finset.prod_congr rfl (fun c _ => hpt c), Finset.prod_mul_distrib]
    congr 1
    rw [Finset.prod_ite, Finset.prod_const, Finset.prod_const_one, mul_one]
  rw [hrw]
  refine Finset.prod_nonneg fun c _ => ?_
  by_cases h : axis c (x c)
  · simp only [h, if_true]
    have := (hf c).axis_nonpos (x c) h; linarith
  · simp only [h, if_false]
    exact (hf c).interior_nonneg (x c) h

private lemma abs_eq_sign_mul {e a : ℚ} (he : e = 1 ∨ e = -1) (h : 0 ≤ e * a) : |a| = e * a := by
  rcases he with he | he
  · rw [he, one_mul]; rw [he, one_mul] at h; exact abs_of_nonneg h
  · rw [he]; rw [he] at h; rw [abs_of_nonpos (by linarith)]; ring

private lemma abs_sum_of_aligned {K : Type*} [Fintype K]
    {e : ℚ} (he : e = 1 ∨ e = -1) (lam : K → ℚ) (hlam : ∀ k, 0 ≤ lam k)
    (g : K → ℚ) (hg : ∀ k, 0 ≤ e * g k) :
    |∑ k, lam k * g k| = ∑ k, lam k * |g k| := by
  have h2 : 0 ≤ e * ∑ k, lam k * g k := by
    rw [Finset.mul_sum]
    refine Finset.sum_nonneg fun k _ => ?_
    have hre : e * (lam k * g k) = lam k * (e * g k) := by ring
    rw [hre]; exact mul_nonneg (hlam k) (hg k)
  rw [abs_eq_sign_mul he h2, Finset.mul_sum]
  exact Finset.sum_congr rfl fun k _ => by rw [abs_eq_sign_mul he (hg k)]; ring

/-- **`thm:product-obstruction`, clause 5.**
An arbitrary nonnegative mixture of products from the class obeys the identical
`|⟨μ,F⟩| · 2^r = 2‖μ‖₁`.  (Together with `product_obstruction_normalized`'s arithmetic this is
the `2^{1-r}` value for the whole class, mixtures included.) -/
theorem product_obstruction_mixture
    {K : Type*} [Fintype K]
    (no : (∀ c, Ω c) → Prop) [DecidablePred no]
    (hNO : ∀ x : (∀ c, Ω c), no x ↔ ∀ c, axis c (x c))
    (lam : K → ℚ) (hlam : ∀ k, 0 ≤ lam k)
    (f : K → ∀ c, Ω c → ℚ) (hf : ∀ k c, IsLocalFactor axis c (f k c))
    (hι : Nonempty ι) :
    |corr no (fun x => ∑ k, lam k * prodMeasure (f k) x)| * 2 ^ (Fintype.card ι)
      = 2 * l1 (fun x => ∑ k, lam k * prodMeasure (f k) x) := by
  classical
  set ν : (∀ c, Ω c) → ℚ := fun x => ∑ k, lam k * prodMeasure (f k) x with hνdef
  set A : K → ℚ := fun k => prodAxisMass axis (f k) with hAdef
  have hApos : ∀ k, 0 < A k := fun k => prodAxisMass_pos axis (f k) (hf k)
  -- ℓ¹ norm of the mixture: no cancellation, because all products share one sign pattern
  have hl1 : l1 ν = ∑ k, lam k * (2 ^ (Fintype.card ι) * A k) := by
    have hx : ∀ x, |ν x| = ∑ k, lam k * |prodMeasure (f k) x| := by
      intro x
      have hecases : ((-1 : ℚ) ^ (univ.filter (fun c => axis c (x c))).card) = 1
          ∨ ((-1 : ℚ) ^ (univ.filter (fun c => axis c (x c))).card) = -1 := by
        rcases Nat.even_or_odd (univ.filter (fun c => axis c (x c))).card with h | h
        · exact Or.inl h.neg_one_pow
        · exact Or.inr h.neg_one_pow
      exact abs_sum_of_aligned hecases lam hlam (fun k => prodMeasure (f k) x)
        (fun k => sign_aligned axis (f k) (hf k) x)
    rw [l1]
    simp only [hx]
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun k _ => ?_
    rw [← Finset.mul_sum, ← l1_prodMeasure axis (f k) (hf k)]
    rfl
  -- NO mass of the mixture: all terms carry the same sign `(-1)^r`
  have hfilter : (univ.filter no) = univ.filter (fun x : (∀ c, Ω c) => ∀ c, axis c (x c)) := by
    ext x; simp [hNO x]
  have hno : ∑ x ∈ univ.filter no, ν x = (-1) ^ (Fintype.card ι) * ∑ k, lam k * A k := by
    rw [hfilter, hνdef]
    rw [Finset.sum_comm]
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun k _ => ?_
    rw [← Finset.mul_sum, noMass_prodMeasure axis (f k) (hf k)]
    ring
  have htot : total ν = 0 := by
    rw [total, hνdef, Finset.sum_comm]
    refine Finset.sum_eq_zero fun k _ => ?_
    rw [← Finset.mul_sum]
    have : ∑ x, prodMeasure (f k) x = 0 := total_prodMeasure_eq_zero axis (f k) (hf k) hι
    rw [this, mul_zero]
  have hcorr : corr no ν = -2 * ((-1) ^ (Fintype.card ι) * ∑ k, lam k * A k) := by
    rw [corr_of_total_zero _ _ htot, hno]
  have hsum_nonneg : 0 ≤ ∑ k, lam k * A k :=
    Finset.sum_nonneg fun k _ => mul_nonneg (hlam k) (hApos k).le
  rw [hcorr, hl1]
  have habs : |(-2 : ℚ) * ((-1) ^ (Fintype.card ι) * ∑ k, lam k * A k)|
      = 2 * ∑ k, lam k * A k := by
    rw [abs_mul, abs_mul, abs_neg, abs_two, abs_pow, abs_neg, abs_one, one_pow, one_mul,
      abs_of_nonneg hsum_nonneg]
  rw [habs]
  rw [Finset.mul_sum]
  rw [Finset.mul_sum]
  rw [Finset.sum_mul]
  refine Finset.sum_congr rfl fun k _ => ?_
  ring

/-- **`thm:product-obstruction`, clause 5 at the paper's displayed VALUE.**

An arbitrary nonnegative sign-aligned mixture, after unit-ℓ¹ normalization, has
`|⟨μ,F⟩| = 2^{1-r}` — the identical value a single product has.  Mixing buys nothing, which is
what the paper's "sign-aligned positive mixtures retain the same sign pattern, norm ratio, and
correlation" asserts.  (Added by the 2026-07-30 T3 audit: the draft stated clause 5 only in the
ratio form, so the *class value* — the actual content of equation (47) for mixtures — was not
machine-checked.) -/
theorem product_obstruction_mixture_normalized
    {K : Type*} [Fintype K]
    (no : (∀ c, Ω c) → Prop) [DecidablePred no]
    (hNO : ∀ x : (∀ c, Ω c), no x ↔ ∀ c, axis c (x c))
    (lam : K → ℚ) (hlam : ∀ k, 0 ≤ lam k)
    (f : K → ∀ c, Ω c → ℚ) (hf : ∀ k c, IsLocalFactor axis c (f k c))
    (hι : Nonempty ι)
    (hnorm : l1 (fun x => ∑ k, lam k * prodMeasure (f k) x) = 1) :
    |corr no (fun x => ∑ k, lam k * prodMeasure (f k) x)| = 2 ^ (1 - (Fintype.card ι : ℤ)) := by
  have h := product_obstruction_mixture axis no hNO lam hlam f hf hι
  rw [hnorm, mul_one] at h
  exact abs_eq_two_pow_one_sub h

/-- **`thm:product-obstruction` for mixtures, the literal `q`-indexed reading.**
`q ≥ 5`, `r = (q-1)/2` pairs: every unit-ℓ¹ sign-aligned mixture in the class has value
`2^{1-(q-1)/2} ≤ 1/2`. -/
theorem product_obstruction_mixture_q
    {K : Type*} [Fintype K]
    (q : ℕ) (hq5 : 5 ≤ q) (hr : Fintype.card ι = (q - 1) / 2)
    (no : (∀ c, Ω c) → Prop) [DecidablePred no]
    (hNO : ∀ x : (∀ c, Ω c), no x ↔ ∀ c, axis c (x c))
    (lam : K → ℚ) (hlam : ∀ k, 0 ≤ lam k)
    (f : K → ∀ c, Ω c → ℚ) (hf : ∀ k c, IsLocalFactor axis c (f k c))
    (hnorm : l1 (fun x => ∑ k, lam k * prodMeasure (f k) x) = 1) :
    |corr no (fun x => ∑ k, lam k * prodMeasure (f k) x)| = 2 ^ (1 - (((q - 1) / 2 : ℕ) : ℤ))
      ∧ |corr no (fun x => ∑ k, lam k * prodMeasure (f k) x)| ≤ 1 / 2 := by
  have hr2 : 2 ≤ (q - 1) / 2 := by omega
  have hι : Nonempty ι := by rw [← Fintype.card_pos_iff, hr]; omega
  have hval := product_obstruction_mixture_normalized axis no hNO lam hlam f hf hι hnorm
  rw [hr] at hval
  refine ⟨hval, ?_⟩
  rw [hval]
  have hle : (1 : ℤ) - (((q - 1) / 2 : ℕ) : ℤ) ≤ -1 := by
    have : (2 : ℤ) ≤ (((q - 1) / 2 : ℕ) : ℤ) := by exact_mod_cast hr2
    omega
  calc (2:ℚ) ^ (1 - (((q - 1) / 2 : ℕ) : ℤ)) ≤ 2 ^ (-1 : ℤ) :=
        zpow_le_zpow_right₀ (by norm_num) hle
    _ = 1 / 2 := by norm_num

/-! ## Non-vacuity witness

`r = 2` (i.e. `q = 5`), local state space `Fin 2` on each pair (state `0` = axis,
state `1` = interior), local factor `(-1/2, +1/2)`.  Every hypothesis of
`product_obstruction_q` is discharged by computation, and the conclusion evaluates to
`|⟨μ,F⟩| = 1/2 = 2^{1-2}`, so the theorem is not vacuously true. -/

section Witness

/-- Witness local state space: `0` is the axis state, `1` the interior state. -/
private def wAxis : ∀ _ : Fin 2, Fin 2 → Prop := fun _ ω => ω = 0

instance instWAxisDec (c : Fin 2) : DecidablePred (wAxis c) := fun ω => decEq ω 0

/-- Witness local factor: mass `-1/2` on the axis, `+1/2` in the interior. -/
private def wF : ∀ _ : Fin 2, Fin 2 → ℚ := fun _ ω => if ω = 0 then -(1/2) else 1/2

private lemma wFilter (c : Fin 2) : (univ.filter (wAxis c)) = {0} := by
  ext ω; fin_cases ω <;> simp [wAxis]

private lemma wF_isLocalFactor (c : Fin 2) : IsLocalFactor wAxis c (wF c) where
  axis_nonpos := by intro ω hω; simp only [wAxis] at hω; subst hω; norm_num [wF]
  interior_nonneg := by
    intro ω hω; simp only [wAxis] at hω; simp only [wF, if_neg hω]; norm_num
  total_zero := by rw [Fin.sum_univ_two]; norm_num [wF]
  nonzero := ⟨0, by norm_num [wF]⟩

private lemma wAxisMass (c : Fin 2) : axisMass wAxis c (wF c) = 1 / 2 := by
  rw [axisMass, wFilter c]; norm_num [wF]

private lemma wProdAxisMass : prodAxisMass wAxis wF = 1 / 4 := by
  rw [prodAxisMass, Fin.prod_univ_two, wAxisMass, wAxisMass]; norm_num

private lemma wF_l1 : l1 (prodMeasure wF) = 1 := by
  rw [l1_prodMeasure wAxis wF wF_isLocalFactor, wProdAxisMass, Fintype.card_fin]
  norm_num

/-- Non-vacuity: all hypotheses of the obstruction hold at `q = 5`, `r = 2`, and the value is
exactly `1/2`. -/
example :
    |corr (fun x : Fin 2 → Fin 2 => ∀ c, wAxis c (x c)) (prodMeasure wF)| = 1 / 2 := by
  have h := (product_obstruction_q (ι := Fin 2) (Ω := fun _ => Fin 2) wAxis 5 (by norm_num)
      (by norm_num) (fun x => ∀ c, wAxis c (x c)) (fun _ => Iff.rfl) wF wF_isLocalFactor
      wF_l1).1
  rw [h]; norm_num

/-- Non-vacuity for the MIXTURE statements: the one-term mixture `λ = 1` over `K = Fin 1` is a
class member with unit norm, and the mixture theorem returns the same `1/2`. -/
private lemma wMix_l1 : l1 (fun x : Fin 2 → Fin 2 => ∑ _k : Fin 1, (1:ℚ) * prodMeasure wF x) = 1 := by
  simpa using wF_l1

example :
    |corr (fun x : Fin 2 → Fin 2 => ∀ c, wAxis c (x c))
      (fun x => ∑ _k : Fin 1, (1:ℚ) * prodMeasure wF x)| = 1 / 2 := by
  have h := (product_obstruction_mixture_q (ι := Fin 2) (Ω := fun _ => Fin 2) (K := Fin 1)
      wAxis 5 (by norm_num) (by norm_num) (fun x => ∀ c, wAxis c (x c)) (fun _ => Iff.rfl)
      (fun _ => 1) (fun _ => by norm_num) (fun _ => wF) (fun _ => wF_isLocalFactor)
      wMix_l1).1
  rw [h]; norm_num

end Witness

#print axioms product_obstruction_exact
#print axioms product_obstruction_ratio
#print axioms product_obstruction_normalized
#print axioms product_obstruction_q
#print axioms product_obstruction_mixture
#print axioms product_obstruction_mixture_normalized
#print axioms product_obstruction_mixture_q

end KsumAudit.Obstructions.Product
