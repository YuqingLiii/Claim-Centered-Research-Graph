/-
# `thm:block-obstruction` — Unaveraged sign-bit composition and value budget

LaTeX: `ksum/paper/ksum_small_alphabet.tex`, label `thm:block-obstruction`, line 1021,
displayed equations (48) (the class), (49) (the correlation identity) and (50) (the value budget).

DAG nodes (this ONE LaTeX theorem spans TWO nodes):
  * `KSUM.B4b.L2.T4`   — "unaveraged sign-bit composition bound"  (equations 48–49)
  * `KSUM.B4b.L2.VBUD` — "value-budget obstruction"               (equation 50)

## The quantifier structure the LaTeX asserts (written out BEFORE formalizing)

Part A (T4).  ∀ `m` blocks; ∀ unit-ℓ¹ zero-total inner measures `μ_j` on the block supports with
positive inner mass only on YES inputs; ∀ unit-ℓ¹ zero-total outer signed measures `Ψ` on
`{-1,+1}^m`; letting `ρ_j = P_j[NO | S_j = -1]` with `P_j = |μ_j|`, `S_j = sgn μ_j`, and
`ζ` the fixed-allocation UNAVERAGED measure (48):
  (i)  if `Ψ` has pure high degree `D` and every `μ_j` has pure high degree ≥ `d`,
       then `ζ` has pure high degree ≥ `dD`;
  (ii) `⟨ζ, OR_m⟩ = -2 Ψ(-1,…,-1) ∏_j ρ_j`, hence `|⟨ζ,OR_m⟩| ≤ ∏_j ρ_j`;
  (iii) for a logarithmic inner with at least five complementary pairs, `ρ_j ≤ 4/5`, so two such
       blocks have correlation ≤ `16/25 < 2/3` before averaging.

Part B (VBUD).  ∀ allocations of COMPLETE complementary value pairs to at most one positional
block each, with block `j` receiving `r_j` pairs: `∑_j r_j ≤ (q-1)/2`, and `m r_0 ≤ (q-1)/2` for
`m` equal blocks; hence this whole-pair allocation cannot produce `√N` growth at fixed `q`.

## Terminology resolved from the source (rule 7g)

`OR_m(g_1,…,g_m)` is described as "+1 unless every block label is -1".  "Block label" is
AMBIGUOUS in isolation — it could be the sign bit `S_j` or the YES/NO label of `x_j`.  The proof
disambiguates it ("If any `S_j=+1`, the block is certainly YES … the global NO probability is
`∏_j ρ_j`"): `OR_m` is the ±1 indicator of the COMPOSED problem, i.e. `-1` exactly when every
block input is NO.  That is the reading formalized here, and it is recorded as a finding.

Clause (i) is rendered with the query row abstracted to a PRODUCT of per-block rows with a
per-block order `ord j`; that is exactly the structure of a query row on a fixed-allocation
composed input, and the paper's "`μ_j` has pure high degree ≥ d" enters as `hlight`.
-/
import KsumAudit.ObstructionsCore
import KsumAudit.ObstructionsTiltedBand

namespace KsumAudit.Obstructions.Block

open Finset KsumAudit.Obstructions

set_option linter.unusedSectionVars false

/-! ## Two indicator-product identities used to factorize block sums -/

section Indicators

variable {J : Type*} [Fintype J] [DecidableEq J]

lemma prod_ite_forall (p : J → Prop) [DecidablePred p] :
    (∏ j, (if p j then (1:ℚ) else 0)) = if (∀ j, p j) then 1 else 0 := by
  by_cases h : ∀ j, p j
  · rw [if_pos h]
    exact Finset.prod_eq_one fun j _ => if_pos (h j)
  · rw [if_neg h]
    rw [not_forall] at h
    obtain ⟨j, hj⟩ := h
    exact Finset.prod_eq_zero (Finset.mem_univ j) (if_neg hj)

lemma prod_ite_funext (u v : J → Bool) :
    (∏ j, (if u j = v j then (1:ℚ) else 0)) = if u = v then 1 else 0 := by
  rw [prod_ite_forall (fun j => u j = v j)]
  by_cases h : u = v
  · rw [if_pos h, if_pos (fun j => by rw [h])]
  · rw [if_neg h, if_neg]
    intro hc; exact h (funext hc)

end Indicators

/-! ## The block factorization lemma

Everything in Part A is an instance of: a sum over block tuples of an outer function of the sign
vector times a product of per-block weights factorizes into a sum over sign vectors of products
of per-cell block masses. -/

section Factorization

variable {J : Type*} [Fintype J] [DecidableEq J]
variable {X : J → Type*} [∀ j, Fintype (X j)] [∀ j, DecidableEq (X j)]

lemma sum_blockwise (σ : ∀ j, X j → Bool) (P : ∀ j, X j → ℚ) (G : (J → Bool) → ℚ) :
    ∑ x : (∀ j, X j), G (fun j => σ j (x j)) * ∏ j, P j (x j)
      = ∑ s : J → Bool, G s * ∏ j, ∑ y ∈ univ.filter (fun y => σ j y = s j), P j y := by
  classical
  have key : ∀ s : J → Bool, (∏ j, ∑ y ∈ univ.filter (fun y => σ j y = s j), P j y)
      = ∑ x : (∀ j, X j), (if (fun j => σ j (x j)) = s then (1:ℚ) else 0) * ∏ j, P j (x j) := by
    intro s
    have h1 : ∀ j : J, (∑ y ∈ univ.filter (fun y => σ j y = s j), P j y)
        = ∑ y, (if σ j y = s j then (1:ℚ) else 0) * P j y := by
      intro j
      rw [Finset.sum_filter]
      exact Finset.sum_congr rfl fun y _ => by split <;> simp
    rw [Finset.prod_congr rfl (fun j (_ : j ∈ univ) => h1 j), Finset.prod_univ_sum,
      Fintype.piFinset_univ]
    refine Finset.sum_congr rfl fun x _ => ?_
    rw [Finset.prod_mul_distrib, prod_ite_funext]
  have step1 : ∀ x : (∀ j, X j), G (fun j => σ j (x j))
      = ∑ s : J → Bool, (if (fun j => σ j (x j)) = s then G s else 0) := by
    intro x
    rw [Finset.sum_ite_eq univ (fun j => σ j (x j)) G]
    simp
  calc ∑ x : (∀ j, X j), G (fun j => σ j (x j)) * ∏ j, P j (x j)
      = ∑ x : (∀ j, X j), ∑ s : J → Bool,
          (if (fun j => σ j (x j)) = s then G s else 0) * ∏ j, P j (x j) := by
        refine Finset.sum_congr rfl fun x _ => ?_
        rw [← Finset.sum_mul, ← step1 x]
    _ = ∑ s : J → Bool, ∑ x : (∀ j, X j),
          (if (fun j => σ j (x j)) = s then G s else 0) * ∏ j, P j (x j) := Finset.sum_comm
    _ = ∑ s : J → Bool, G s * ∑ x : (∀ j, X j),
          (if (fun j => σ j (x j)) = s then (1:ℚ) else 0) * ∏ j, P j (x j) := by
        refine Finset.sum_congr rfl fun s _ => ?_
        rw [Finset.mul_sum]
        refine Finset.sum_congr rfl fun x _ => ?_
        split <;> ring
    _ = ∑ s : J → Bool, G s * ∏ j, ∑ y ∈ univ.filter (fun y => σ j y = s j), P j y := by
        refine Finset.sum_congr rfl fun s _ => by rw [key s]

end Factorization

/-! ## Part A: the fixed-allocation unaveraged sign-bit composition (node `KSUM.B4b.L2.T4`) -/

section PartA

variable {J : Type*} [Fintype J] [DecidableEq J]
variable {X : J → Type*} [∀ j, Fintype (X j)] [∀ j, DecidableEq (X j)]
variable (μ : ∀ j, X j → ℚ)
variable (blockNO : ∀ j, X j → Prop) [∀ j, DecidablePred (blockNO j)]

/-- `S_j = -1`, i.e. the inner measure is negative at this block input. -/
def sgnNeg (j : J) (y : X j) : Bool := decide (μ j y < 0)

/-- `P_j = |μ_j|`. -/
def blockP (j : J) (y : X j) : ℚ := |μ j y|

/-- The paper's hypotheses on a single inner block measure. -/
structure IsInnerBlock (j : J) : Prop where
  unit : ∑ y, |μ j y| = 1
  zeroTotal : ∑ y, μ j y = 0
  /-- "positive inner mass occurs only on YES inputs" -/
  posYes : ∀ y, 0 < μ j y → ¬ blockNO j y

/-- The paper's hypotheses on the outer measure `Ψ`. -/
structure IsOuter (Ψ : (J → Bool) → ℚ) : Prop where
  unit : ∑ s, |Ψ s| = 1
  zeroTotal : ∑ s, Ψ s = 0

/-- The fixed-allocation, UNAVERAGED measure of equation (48):
`ζ(x₁,…,x_m) = 2^m Ψ(S₁,…,S_m) ∏_j |μ_j(x_j)|`. -/
def zeta (Ψ : (J → Bool) → ℚ) (x : ∀ j, X j) : ℚ :=
  2 ^ (Fintype.card J) * Ψ (fun j => sgnNeg μ j (x j)) * ∏ j, blockP μ j (x j)

lemma filter_false_eq {j : J} :
    (univ.filter (fun y => sgnNeg μ j y = false))
      = univ.filter (fun y => ¬ (sgnNeg μ j y = true)) := by
  apply Finset.filter_congr; intro y _; cases sgnNeg μ j y <;> simp

/-- `P_j[S_j = -1] = 1/2`: the sign vector is uniform under `P₁⊗⋯⊗P_m`. -/
lemma cell_neg_half {j : J} (h : IsInnerBlock μ blockNO j) :
    ∑ y ∈ univ.filter (fun y => sgnNeg μ j y = true), blockP μ j y = 1 / 2 := by
  classical
  have hsplit : (∑ y ∈ univ.filter (fun y => sgnNeg μ j y = true), blockP μ j y)
      + ∑ y ∈ univ.filter (fun y => ¬ (sgnNeg μ j y = true)), blockP μ j y
      = ∑ y, blockP μ j y := Finset.sum_filter_add_sum_filter_not _ _ _
  have hneg : ∑ y ∈ univ.filter (fun y => sgnNeg μ j y = true), μ j y
      = -∑ y ∈ univ.filter (fun y => sgnNeg μ j y = true), blockP μ j y := by
    rw [← Finset.sum_neg_distrib]
    refine Finset.sum_congr rfl fun y hy => ?_
    have hlt : μ j y < 0 := by
      have := (Finset.mem_filter.mp hy).2
      simpa [sgnNeg] using this
    simp only [blockP]
    rw [abs_of_neg hlt, neg_neg]
  have hpos : ∑ y ∈ univ.filter (fun y => ¬ (sgnNeg μ j y = true)), μ j y
      = ∑ y ∈ univ.filter (fun y => ¬ (sgnNeg μ j y = true)), blockP μ j y := by
    refine Finset.sum_congr rfl fun y hy => ?_
    have hnn : ¬ (μ j y < 0) := by
      have := (Finset.mem_filter.mp hy).2
      simpa [sgnNeg] using this
    simp only [blockP]
    rw [abs_of_nonneg (not_lt.mp hnn)]
  have h0 : (∑ y ∈ univ.filter (fun y => sgnNeg μ j y = true), μ j y)
      + ∑ y ∈ univ.filter (fun y => ¬ (sgnNeg μ j y = true)), μ j y = 0 := by
    rw [Finset.sum_filter_add_sum_filter_not, h.zeroTotal]
  rw [hneg, hpos] at h0
  have hunit : ∑ y, blockP μ j y = 1 := by simp only [blockP]; exact h.unit
  rw [hunit] at hsplit
  linarith

lemma cell_pos_half {j : J} (h : IsInnerBlock μ blockNO j) :
    ∑ y ∈ univ.filter (fun y => sgnNeg μ j y = false), blockP μ j y = 1 / 2 := by
  classical
  have hsplit : (∑ y ∈ univ.filter (fun y => sgnNeg μ j y = true), blockP μ j y)
      + ∑ y ∈ univ.filter (fun y => ¬ (sgnNeg μ j y = true)), blockP μ j y
      = ∑ y, blockP μ j y := Finset.sum_filter_add_sum_filter_not _ _ _
  have hunit : ∑ y, blockP μ j y = 1 := by simp only [blockP]; exact h.unit
  have h2 := cell_neg_half μ blockNO h
  rw [filter_false_eq]
  rw [hunit, h2] at hsplit
  linarith

/-- On the `S_j = +1` cell no NO input carries mass: positive inner mass sits on YES inputs and
zero inner mass contributes nothing.  This is the step that kills every sign vector other than
`(-1,…,-1)`. -/
lemma cell_pos_no_zero {j : J} (h : IsInnerBlock μ blockNO j) (row : X j → ℚ) :
    ∑ y ∈ univ.filter (fun y => sgnNeg μ j y = false ∧ blockNO j y),
      blockP μ j y * row y = 0 := by
  classical
  refine Finset.sum_eq_zero fun y hy => ?_
  obtain ⟨hs, hno⟩ := (Finset.mem_filter.mp hy).2
  have hnn : ¬ (μ j y < 0) := by simpa [sgnNeg] using hs
  have hz : μ j y = 0 := by
    rcases (not_lt.mp hnn).lt_or_eq with hlt | heq
    · exact absurd hno (h.posYes y hlt)
    · exact heq.symm
  simp only [blockP, hz]
  simp

/-- The conditional NO probability `ρ_j = P_j[NO | S_j = -1]` of the paper. -/
noncomputable def rho (j : J) : ℚ :=
  (∑ y ∈ univ.filter (fun y => sgnNeg μ j y = true ∧ blockNO j y), blockP μ j y) /
    (∑ y ∈ univ.filter (fun y => sgnNeg μ j y = true), blockP μ j y)

lemma rho_eq {j : J} (h : IsInnerBlock μ blockNO j) :
    rho μ blockNO j
      = 2 * ∑ y ∈ univ.filter (fun y => sgnNeg μ j y = true ∧ blockNO j y), blockP μ j y := by
  rw [rho, cell_neg_half μ blockNO h]; ring

lemma rho_nonneg {j : J} (h : IsInnerBlock μ blockNO j) : 0 ≤ rho μ blockNO j := by
  rw [rho_eq μ blockNO h]
  have hs : (0:ℚ) ≤ ∑ y ∈ univ.filter (fun y => sgnNeg μ j y = true ∧ blockNO j y),
      blockP μ j y := Finset.sum_nonneg fun y _ => abs_nonneg _
  linarith

/-- **`thm:block-obstruction` (49), the exact correlation identity.**
`⟨ζ, OR_m⟩ = -2 Ψ(-1,…,-1) ∏_j ρ_j`. -/
theorem block_obstruction_corr
    (hμ : ∀ j, IsInnerBlock μ blockNO j)
    (Ψ : (J → Bool) → ℚ) (hΨ : IsOuter Ψ)
    (noG : (∀ j, X j) → Prop) [DecidablePred noG]
    (hnoG : ∀ x, noG x ↔ ∀ j, blockNO j (x j)) :
    corr noG (zeta μ Ψ) = -2 * Ψ (fun _ => true) * ∏ j, rho μ blockNO j := by
  classical
  -- total mass of ζ is zero
  have htotal : total (zeta μ Ψ) = 0 := by
    have hz : ∀ x : (∀ j, X j), zeta μ Ψ x
        = 2 ^ (Fintype.card J) *
          (Ψ (fun j => sgnNeg μ j (x j)) * ∏ j, blockP μ j (x j)) := by
      intro x; simp only [zeta]; ring
    rw [total, Finset.sum_congr rfl (fun x (_ : x ∈ univ) => hz x), ← Finset.mul_sum,
      sum_blockwise (sgnNeg μ) (blockP μ) Ψ]
    have hhalf : ∀ (j : J) (b : Bool),
        (∑ y ∈ univ.filter (fun y => sgnNeg μ j y = b), blockP μ j y) = 1/2 := by
      intro j b
      cases b with
      | true => exact cell_neg_half μ blockNO (hμ j)
      | false => exact cell_pos_half μ blockNO (hμ j)
    have hc : ∀ s : J → Bool,
        (∏ j, ∑ y ∈ univ.filter (fun y => sgnNeg μ j y = s j), blockP μ j y)
          = (1/2 : ℚ) ^ (Fintype.card J) := by
      intro s
      rw [Finset.prod_congr rfl (fun j (_ : j ∈ univ) => hhalf j (s j)), Finset.prod_const,
        Finset.card_univ]
    rw [Finset.sum_congr rfl (fun s (_ : s ∈ univ) => by rw [hc s]), ← Finset.sum_mul,
      hΨ.zeroTotal]
    ring
  -- mass on the global NO event
  have hfacT : ∀ j : J, (∑ y ∈ univ.filter (fun y => sgnNeg μ j y = true),
      blockP μ j y * (if blockNO j y then (1:ℚ) else 0)) = rho μ blockNO j / 2 := by
    intro j
    have hrw : (∑ y ∈ univ.filter (fun y => sgnNeg μ j y = true),
          blockP μ j y * (if blockNO j y then (1:ℚ) else 0))
        = ∑ y ∈ univ.filter (fun y => sgnNeg μ j y = true ∧ blockNO j y), blockP μ j y := by
      rw [Finset.sum_filter, Finset.sum_filter]
      refine Finset.sum_congr rfl fun y _ => ?_
      by_cases h1 : sgnNeg μ j y = true <;> by_cases h2 : blockNO j y <;> simp [h1, h2]
    rw [hrw, rho_eq μ blockNO (hμ j)]; ring
  have hfacF : ∀ j : J, (∑ y ∈ univ.filter (fun y => sgnNeg μ j y = false),
      blockP μ j y * (if blockNO j y then (1:ℚ) else 0)) = 0 := by
    intro j
    have hrw : (∑ y ∈ univ.filter (fun y => sgnNeg μ j y = false),
          blockP μ j y * (if blockNO j y then (1:ℚ) else 0))
        = ∑ y ∈ univ.filter (fun y => sgnNeg μ j y = false ∧ blockNO j y),
            blockP μ j y * (fun _ => (1:ℚ)) y := by
      rw [Finset.sum_filter, Finset.sum_filter]
      refine Finset.sum_congr rfl fun y _ => ?_
      by_cases h1 : sgnNeg μ j y = false <;> by_cases h2 : blockNO j y <;> simp [h1, h2]
    rw [hrw]
    exact cell_pos_no_zero μ blockNO (hμ j) (fun _ => 1)
  have hno : ∑ x ∈ univ.filter noG, zeta μ Ψ x = Ψ (fun _ => true) * ∏ j, rho μ blockNO j := by
    have hind : ∀ x : (∀ j, X j),
        (if noG x then (1:ℚ) else 0) = ∏ j, (if blockNO j (x j) then (1:ℚ) else 0) := by
      intro x
      rw [prod_ite_forall (fun j => blockNO j (x j))]
      by_cases h : ∀ j, blockNO j (x j)
      · rw [if_pos ((hnoG x).mpr h), if_pos h]
      · rw [if_neg (fun hc => h ((hnoG x).mp hc)), if_neg h]
    have hstep : ∑ x ∈ univ.filter noG, zeta μ Ψ x
        = 2 ^ (Fintype.card J) * ∑ x : (∀ j, X j),
            Ψ (fun j => sgnNeg μ j (x j)) *
              ∏ j, (blockP μ j (x j) * (if blockNO j (x j) then (1:ℚ) else 0)) := by
      rw [Finset.sum_filter, Finset.mul_sum]
      refine Finset.sum_congr rfl fun x _ => ?_
      rw [Finset.prod_mul_distrib, ← hind x]
      simp only [zeta]
      split <;> ring
    rw [hstep, sum_blockwise (sgnNeg μ) (fun j y => blockP μ j y *
      (if blockNO j y then (1:ℚ) else 0)) Ψ]
    have honly : ∀ s : J → Bool, s ≠ (fun _ => true) →
        Ψ s * ∏ j, (∑ y ∈ univ.filter (fun y => sgnNeg μ j y = s j),
          blockP μ j y * (if blockNO j y then (1:ℚ) else 0)) = 0 := by
      intro s hs
      obtain ⟨j, hj⟩ : ∃ j, s j = false := by
        by_contra hcon
        rw [not_exists] at hcon
        exact hs (funext fun j => by
          cases hsj : s j with
          | true => rfl
          | false => exact absurd hsj (hcon j))
      have hzero : (∑ y ∈ univ.filter (fun y => sgnNeg μ j y = s j),
          blockP μ j y * (if blockNO j y then (1:ℚ) else 0)) = 0 := by
        rw [hj]; exact hfacF j
      rw [Finset.prod_eq_zero (Finset.mem_univ j) hzero, mul_zero]
    rw [Finset.sum_eq_single (fun _ => true) (fun s _ hs => honly s hs) (by simp)]
    rw [Finset.prod_congr rfl (fun j (_ : j ∈ univ) => hfacT j), Finset.prod_div_distrib,
      Finset.prod_const, Finset.card_univ]
    field_simp
  rw [corr_of_total_zero _ _ htotal, hno]
  ring

/-- `2|Ψ(s₀)| ≤ 1` for any single sign vector, from unit ℓ¹ norm and zero total. -/
lemma two_abs_le_one (Ψ : (J → Bool) → ℚ) (hΨ : IsOuter Ψ) (s₀ : J → Bool) :
    2 * |Ψ s₀| ≤ 1 := by
  classical
  have hsplit : Ψ s₀ + ∑ s ∈ univ.erase s₀, Ψ s = ∑ s, Ψ s :=
    Finset.add_sum_erase univ Ψ (Finset.mem_univ s₀)
  have habs : |Ψ s₀| + ∑ s ∈ univ.erase s₀, |Ψ s| = ∑ s, |Ψ s| :=
    Finset.add_sum_erase univ (fun s => |Ψ s|) (Finset.mem_univ s₀)
  rw [hΨ.zeroTotal] at hsplit
  rw [hΨ.unit] at habs
  have h1 : |Ψ s₀| = |∑ s ∈ univ.erase s₀, Ψ s| := by
    have hneg : Ψ s₀ = -∑ s ∈ univ.erase s₀, Ψ s := by linarith
    rw [hneg, abs_neg]
  have h2 : |∑ s ∈ univ.erase s₀, Ψ s| ≤ ∑ s ∈ univ.erase s₀, |Ψ s| :=
    Finset.abs_sum_le_sum_abs _ _
  rw [h1]
  linarith

/-- **`thm:block-obstruction` (49), the bound.**  `|⟨ζ,OR_m⟩| ≤ ∏_j ρ_j`. -/
theorem block_obstruction_bound
    (hμ : ∀ j, IsInnerBlock μ blockNO j)
    (Ψ : (J → Bool) → ℚ) (hΨ : IsOuter Ψ)
    (noG : (∀ j, X j) → Prop) [DecidablePred noG]
    (hnoG : ∀ x, noG x ↔ ∀ j, blockNO j (x j)) :
    |corr noG (zeta μ Ψ)| ≤ ∏ j, rho μ blockNO j := by
  rw [block_obstruction_corr μ blockNO hμ Ψ hΨ noG hnoG]
  have hprod : 0 ≤ ∏ j, rho μ blockNO j :=
    Finset.prod_nonneg fun j _ => rho_nonneg μ blockNO (hμ j)
  have h2 := two_abs_le_one Ψ hΨ (fun _ => true)
  calc |(-2 : ℚ) * Ψ (fun _ => true) * ∏ j, rho μ blockNO j|
      = (2 * |Ψ (fun _ => true)|) * ∏ j, rho μ blockNO j := by
        rw [abs_mul, abs_mul, abs_neg, abs_two, abs_of_nonneg hprod]
    _ ≤ 1 * ∏ j, rho μ blockNO j := mul_le_mul_of_nonneg_right h2 hprod
    _ = ∏ j, rho μ blockNO j := one_mul _

/-! ### The pure-high-degree clause of `thm:block-obstruction` -/

/-- `Ψ` annihilates every outer function depending on fewer than `D` sign coordinates
(equivalently, every multilinear sign polynomial of degree `< D`). -/
def OuterPureHighDegree (Ψ : (J → Bool) → ℚ) (D : ℕ) : Prop :=
  ∀ T : Finset J, T.card < D → ∀ f : (J → Bool) → ℚ,
    (∀ s s' : J → Bool, (∀ j ∈ T, s j = s' j) → f s = f s') → ∑ s, Ψ s * f s = 0

/-- **`thm:block-obstruction`, the band clause.**  A product row whose per-block orders sum to
less than `d·D` is annihilated by `ζ`.

Note: the proof needs only `hlight` (which is what "every `μ_j` has pure high degree at least
`d`" supplies) — the inner-block sign conditions `_hμ` are carried for fidelity to the paper's
class but are not used, so the Lean statement is if anything stronger than the LaTeX's. -/
theorem block_obstruction_band
    (_hμ : ∀ j, IsInnerBlock μ blockNO j)
    (Ψ : (J → Bool) → ℚ) (d D : ℕ) (_hd : 1 ≤ d)
    (hΨdeg : OuterPureHighDegree Ψ D)
    (row : ∀ j, X j → ℚ) (ord : J → ℕ)
    (hlight : ∀ j, ord j < d → ∑ y, μ j y * row j y = 0)
    (htotal : ∑ j, ord j < d * D) :
    ∑ x : (∀ j, X j), zeta μ Ψ x * ∏ j, row j (x j) = 0 := by
  classical
  set T : Finset J := univ.filter (fun j => d ≤ ord j) with hT
  have hTcard : T.card < D := by
    have hsum : ∑ _j ∈ T, d ≤ ∑ j ∈ T, ord j :=
      Finset.sum_le_sum fun j hj => (Finset.mem_filter.mp hj).2
    have hle : ∑ j ∈ T, ord j ≤ ∑ j, ord j :=
      Finset.sum_le_sum_of_subset (Finset.filter_subset _ _)
    rw [Finset.sum_const, smul_eq_mul] at hsum
    have h1 : T.card * d < D * d := by
      rw [Nat.mul_comm D d]
      exact lt_of_le_of_lt (le_trans hsum hle) htotal
    exact lt_of_mul_lt_mul_right h1 (Nat.zero_le d)
  set A : ∀ _ : J, Bool → ℚ := fun j b =>
    ∑ y ∈ univ.filter (fun y => sgnNeg μ j y = b), blockP μ j y * row j y with hA
  have hlightA : ∀ j, ord j < d → A j true = A j false := by
    intro j hj
    have h0 := hlight j hj
    have hsplit : (∑ y ∈ univ.filter (fun y => sgnNeg μ j y = true), μ j y * row j y)
        + ∑ y ∈ univ.filter (fun y => ¬ (sgnNeg μ j y = true)), μ j y * row j y
        = ∑ y, μ j y * row j y := Finset.sum_filter_add_sum_filter_not _ _ _
    have hneg : ∑ y ∈ univ.filter (fun y => sgnNeg μ j y = true), μ j y * row j y
        = -A j true := by
      simp only [hA]
      rw [← Finset.sum_neg_distrib]
      refine Finset.sum_congr rfl fun y hy => ?_
      have hlt : μ j y < 0 := by
        have := (Finset.mem_filter.mp hy).2; simpa [sgnNeg] using this
      simp only [blockP]
      rw [abs_of_neg hlt]; ring
    have hposc : ∑ y ∈ univ.filter (fun y => ¬ (sgnNeg μ j y = true)), μ j y * row j y
        = A j false := by
      simp only [hA]
      rw [filter_false_eq]
      refine Finset.sum_congr rfl fun y hy => ?_
      have hnn : ¬ (μ j y < 0) := by
        have := (Finset.mem_filter.mp hy).2; simpa [sgnNeg] using this
      simp only [blockP]
      rw [abs_of_nonneg (not_lt.mp hnn)]
    rw [hneg, hposc, h0] at hsplit
    linarith
  have hz : ∀ x : (∀ j, X j), zeta μ Ψ x * ∏ j, row j (x j)
      = 2 ^ (Fintype.card J) *
        (Ψ (fun j => sgnNeg μ j (x j)) * ∏ j, (blockP μ j (x j) * row j (x j))) := by
    intro x; simp only [zeta]; rw [Finset.prod_mul_distrib]; ring
  rw [Finset.sum_congr rfl (fun x (_ : x ∈ univ) => hz x), ← Finset.mul_sum,
    sum_blockwise (sgnNeg μ) (fun j y => blockP μ j y * row j y) Ψ]
  have hfin : ∑ s : J → Bool, Ψ s * ∏ j, A j (s j) = 0 := by
    refine hΨdeg T hTcard (fun s => ∏ j, A j (s j)) ?_
    intro s s' hss
    refine Finset.prod_congr rfl fun j _ => ?_
    by_cases hj : j ∈ T
    · rw [hss j hj]
    · have hlt : ord j < d := by
        simp only [hT, Finset.mem_filter, Finset.mem_univ, true_and, not_le] at hj
        exact hj
      cases hb : s j <;> cases hb' : s' j <;> simp [hlightA j hlt]
  rw [hfin, mul_zero]

/-- **Clause (i), the linearity step** (gap-closure item L-3, 2026-07-31, PARTIAL).

The statement-fidelity review (`ksum/reviews/ksum_lean_statement_fidelity_review_20260731.md` §6.B)
found that `block_obstruction_band` proves clause (i) only for query rows that are PRODUCTS
`∏_j row_j` of per-block rows, whereas the paper asserts *"`ζ` has pure high degree at least `dD`"*,
i.e. annihilation of EVERY row of total order `< dD`; and observed that *"a general row is a linear
combination of such products (Vandermonde), so the gap is closable by linearity — but it is not
closed in Lean"*.

This theorem is the linearity half, proved: `ζ` annihilates every `ℚ`-linear combination of
product rows whose per-block orders obey the same hypotheses.  What it does NOT supply is the
multivariate Vandermonde expansion exhibiting a general falling-factorial row on the composed input
as such a combination — for `m > 2` blocks that needs an `m`-fold generalization of
`KsumAudit.Obstructions.BandMult.descFactorial_add`, indexed by the splittings
`α = α^{(1)} + ⋯ + α^{(m)}`, which is not on disk.  With that identity in hand this theorem closes
clause (i) immediately, since every splitting has `∑_j |α^{(j)}| = |α| < dD`.  Recorded as the
precise residual gap. -/
theorem block_obstruction_band_combination
    (_hμ : ∀ j, IsInnerBlock μ blockNO j)
    (Ψ : (J → Bool) → ℚ) (d D : ℕ) (hd : 1 ≤ d)
    (hΨdeg : OuterPureHighDegree Ψ D)
    {ι : Type*} (T : Finset ι) (coef : ι → ℚ) (rows : ι → ∀ j, X j → ℚ) (ord : ι → J → ℕ)
    (hlight : ∀ i ∈ T, ∀ j, ord i j < d → ∑ y, μ j y * rows i j y = 0)
    (htotal : ∀ i ∈ T, ∑ j, ord i j < d * D)
    (R : (∀ j, X j) → ℚ) (hR : ∀ x, R x = ∑ i ∈ T, coef i * ∏ j, rows i j (x j)) :
    ∑ x : (∀ j, X j), zeta μ Ψ x * R x = 0 := by
  classical
  have hpt : ∀ x : (∀ j, X j), zeta μ Ψ x * R x
      = ∑ i ∈ T, coef i * (zeta μ Ψ x * ∏ j, rows i j (x j)) := by
    intro x
    rw [hR x, Finset.mul_sum]
    exact Finset.sum_congr rfl fun i _ => by ring
  rw [Finset.sum_congr rfl (fun x (_ : x ∈ univ) => hpt x), Finset.sum_comm]
  refine Finset.sum_eq_zero fun i hi => ?_
  rw [← Finset.mul_sum,
    block_obstruction_band μ blockNO _hμ Ψ d D hd hΨdeg (rows i) (ord i)
      (hlight i hi) (htotal i hi), mul_zero]

end PartA

/-! ## `ρ_j ≤ 4/5` for a logarithmic inner with at least five complementary pairs -/

section RhoBound

/-- The arithmetic of the paper's `ρ ≤ 2/(1 + 5/4 + 1/4) = 4/5` step: the `K=1` and `K=5`
absolute weights are at least `5/4` and `1/4` times the `K=0` weight, and the weights sum to 1. -/
theorem rho_le_four_fifths {ι : Type*} [DecidableEq ι] (S : Finset ι) (w : ι → ℚ)
    (hw : ∀ i ∈ S, 0 ≤ w i) (i0 i1 i5 : ι)
    (h0 : i0 ∈ S) (h1 : i1 ∈ S) (h5 : i5 ∈ S)
    (h01 : i0 ≠ i1) (h05 : i0 ≠ i5) (h15 : i1 ≠ i5)
    (hZ : ∑ i ∈ S, w i = 1)
    (hr1 : 5 / 4 * w i0 ≤ w i1) (hr5 : 1 / 4 * w i0 ≤ w i5) :
    2 * w i0 ≤ 4 / 5 := by
  classical
  have hsub : ({i0, i1, i5} : Finset ι) ⊆ S := by
    intro i hi
    simp only [Finset.mem_insert, Finset.mem_singleton] at hi
    rcases hi with rfl | rfl | rfl <;> assumption
  have hle : ∑ i ∈ ({i0, i1, i5} : Finset ι), w i ≤ ∑ i ∈ S, w i :=
    Finset.sum_le_sum_of_subset_of_nonneg hsub (fun i hi _ => hw i hi)
  rw [Finset.sum_insert (by simp [h01, h05]), Finset.sum_insert (by simp [h15]),
    Finset.sum_singleton, hZ] at hle
  linarith

/-- Two blocks with `ρ_j ≤ 4/5` have correlation at most `16/25 < 2/3` before averaging. -/
theorem two_block_corr_lt_two_thirds (ρ₀ ρ₁ : ℚ) (h₀ : 0 ≤ ρ₀) (_h₁ : 0 ≤ ρ₁)
    (hb₀ : ρ₀ ≤ 4/5) (hb₁ : ρ₁ ≤ 4/5) : ρ₀ * ρ₁ ≤ 16/25 ∧ (16:ℚ)/25 < 2/3 := by
  refine ⟨by nlinarith, by norm_num⟩

/-! ### The tilted inner SUPPLIES `ρ ≤ 4/5` — clause (iii)'s missing link

Gap-closure batch 2, item H-3(iii), 2026-08-01.  The statement-fidelity review
(`ksum/reviews/ksum_lean_statement_fidelity_review_20260731.md` §6.B) graded clause (iii) NARROWER
because *"`rho_le_four_fifths` is a pure arithmetic lemma about three weights with two ratio
hypotheses … the link from the tilted inner to `ρ_j ≤ 4/5` is therefore not established"*, and
recorded that this was *"consistently with `thm:tilted-log-band` itself being unformalized"*.

`KsumAudit.Obstructions.TiltedBand` now defines the divided-difference coefficients (42) and
derives the ratio computation (44), so the two ratio hypotheses are theorems (`abs_lam_one_ge`,
`abs_lam_two_ge`) and the link below is the paper's own three-weight argument, instantiated. -/

open KsumAudit.Obstructions.TiltedBand in
/-- **The paper's `ρ ≤ 2/(1 + 5/4 + 1/4) = 4/5`, DERIVED from the tilted inner.**

The normalized absolute divided-difference weights `W_k = |λ_k|/Z` of `thm:tilted-log-band`
satisfy the hypotheses of `rho_le_four_fifths` at `K = 0, 1, 5`, so `ρ = 2W_0 ≤ 4/5`, for every
`m ≥ 2` — which is exactly the paper's *"a logarithmic inner from Theorem `thm:tilted-log-band`
containing at least five complementary pairs"* (`r ≥ 5 ⇒ m = 1 + ⌊log₅ r⌋ ≥ 2`).

This routes through `rho_le_four_fifths` deliberately: the point is that the manuscript's own
three-weight step is the one that closes, on the manuscript's own weights. -/
theorem tilted_rho_le_four_fifths {m : ℕ} (hm : 2 ≤ m) :
    2 * (|lam m 0| / Znorm m) ≤ 4 / 5 := by
  classical
  have hZ : 0 < Znorm m := Znorm_pos m
  refine rho_le_four_fifths (Finset.range (m + 1)) (fun i => |lam m i| / Znorm m)
    (fun i _ => div_nonneg (abs_nonneg _) hZ.le) 0 1 2
    (Finset.mem_range.mpr (by omega)) (Finset.mem_range.mpr (by omega))
    (Finset.mem_range.mpr (by omega)) (by norm_num) (by norm_num) (by norm_num) ?_ ?_ ?_
  · rw [← Finset.sum_div, show ∑ i ∈ Finset.range (m + 1), |lam m i| = Znorm m from rfl]
    exact div_self hZ.ne'
  · rw [← mul_div_assoc, div_le_div_iff₀ hZ hZ]
    have := abs_lam_one_ge hm
    nlinarith
  · rw [← mul_div_assoc, div_le_div_iff₀ hZ hZ]
    have := abs_lam_two_ge hm
    nlinarith

end RhoBound

/-! ## Clause (iii) of Part A, wired to the correlation identity

The draft proved the correlation identity, the `ρ ≤ 4/5` arithmetic and the `16/25 < 2/3`
arithmetic as three separate facts.  The paper states clause (iii) as a single sentence about the
composed measure, so it is assembled here (2026-07-30 T3 audit). -/

section TwoBlocks

variable {X : Fin 2 → Type*} [∀ j, Fintype (X j)] [∀ j, DecidableEq (X j)]
variable (μ : ∀ j, X j → ℚ)
variable (blockNO : ∀ j, X j → Prop) [∀ j, DecidablePred (blockNO j)]

/-- **`thm:block-obstruction`, clause (iii).**  If two blocks each have conditional NO probability
`ρ_j ≤ 4/5` — which is what a logarithmic phase-3 inner with at least five complementary pairs
supplies (`rho_le_four_fifths`) — then the UNAVERAGED sign-bit composition has correlation at most
`16/25`, which is strictly below the `2/3` threshold the polynomial method needs. -/
theorem block_obstruction_two_blocks
    (hμ : ∀ j, IsInnerBlock μ blockNO j)
    (Ψ : (Fin 2 → Bool) → ℚ) (hΨ : IsOuter Ψ)
    (noG : (∀ j, X j) → Prop) [DecidablePred noG]
    (hnoG : ∀ x, noG x ↔ ∀ j, blockNO j (x j))
    (hρ : ∀ j, rho μ blockNO j ≤ 4/5) :
    |corr noG (zeta μ Ψ)| ≤ 16/25 ∧ (16:ℚ)/25 < 2/3 := by
  have hb := block_obstruction_bound μ blockNO hμ Ψ hΨ noG hnoG
  have h0 : 0 ≤ rho μ blockNO 0 := rho_nonneg μ blockNO (hμ 0)
  have h1 : 0 ≤ rho μ blockNO 1 := rho_nonneg μ blockNO (hμ 1)
  have hprod : ∏ j, rho μ blockNO j = rho μ blockNO 0 * rho μ blockNO 1 := Fin.prod_univ_two _
  rw [hprod] at hb
  exact ⟨le_trans hb (two_block_corr_lt_two_thirds _ _ h0 h1 (hρ 0) (hρ 1)).1, by norm_num⟩

open KsumAudit.Obstructions.TiltedBand in
/-- **`thm:block-obstruction`, clause (iii), with `ρ_j ≤ 4/5` DERIVED rather than assumed**
(gap-closure batch 2, item H-3(iii)).

Same conclusion as `block_obstruction_two_blocks`, but the `4/5` hypothesis is replaced by the
manuscript's own description of the blocks: *"a logarithmic inner from
Theorem `thm:tilted-log-band` containing at least five complementary pairs"*, rendered as
`m ≥ 2` together with the paper's identification of the conditional NO probability with twice the
all-axis outer weight, `ρ_j = 2|W_0| = 2|λ_0|/Z` (the `K = 0` layer is the inner's only NO layer;
`thm:tilted-log-band`'s own proof, equation (43)).

The identification remains an explicit hypothesis, because reading `ρ_j` off the tilted measure
requires the inner pair tensor as a measure on `ℤ_q^N`, which is not formalized (see the scope
note in `ObstructionsTiltedBand`).  What was a *numeric* assumption (`ρ_j ≤ 4/5`) is now a
*structural* one (which measure the block carries). -/
theorem block_obstruction_two_blocks_tilted
    (hμ : ∀ j, IsInnerBlock μ blockNO j)
    (Ψ : (Fin 2 → Bool) → ℚ) (hΨ : IsOuter Ψ)
    (noG : (∀ j, X j) → Prop) [DecidablePred noG]
    (hnoG : ∀ x, noG x ↔ ∀ j, blockNO j (x j))
    {m : ℕ} (hm : 2 ≤ m)
    (hident : ∀ j, rho μ blockNO j = 2 * (|lam m 0| / Znorm m)) :
    |corr noG (zeta μ Ψ)| ≤ 16 / 25 ∧ (16:ℚ) / 25 < 2 / 3 :=
  block_obstruction_two_blocks μ blockNO hμ Ψ hΨ noG hnoG
    (fun j => by rw [hident j]; exact tilted_rho_le_four_fifths hm)

end TwoBlocks

/-! ## Part B: the value budget, equation (50) (node `KSUM.B4b.L2.VBUD`) -/

section ValueBudget

variable {J : Type*} [Fintype J] [DecidableEq J] {V : Type*} [DecidableEq V]

/-- **`thm:block-obstruction` (50), first inequality.**
Complete nonfixed σ-pairs are disjoint resources: if each block receives a set of complete
complementary value pairs, and no pair goes to two blocks, then `∑_j r_j ≤ (q-1)/2`. -/
theorem value_budget (pairs : Finset V) (B : J → Finset V)
    (hsub : ∀ j, B j ⊆ pairs)
    (hdisj : ∀ j k : J, j ≠ k → Disjoint (B j) (B k)) :
    ∑ j, (B j).card ≤ pairs.card := by
  classical
  have hpw : ((univ : Finset J) : Set J).PairwiseDisjoint B :=
    fun j _ k _ hjk => hdisj j k hjk
  rw [← Finset.card_biUnion hpw]
  exact Finset.card_le_card (Finset.biUnion_subset.mpr fun j _ => hsub j)

/-- **`thm:block-obstruction` (50), second inequality:** `m·r₀ ≤ (q-1)/2` for `m` equal blocks. -/
theorem value_budget_equal (pairs : Finset V) (B : J → Finset V) (r₀ : ℕ)
    (hsub : ∀ j, B j ⊆ pairs)
    (hdisj : ∀ j k : J, j ≠ k → Disjoint (B j) (B k))
    (hcard : ∀ j, (B j).card = r₀) :
    Fintype.card J * r₀ ≤ pairs.card := by
  have h := value_budget pairs B hsub hdisj
  rwa [Finset.sum_congr rfl (fun j (_ : j ∈ univ) => hcard j), Finset.sum_const,
    Finset.card_univ, smul_eq_mul] at h

/-- **`thm:block-obstruction`:** "this whole-pair allocation cannot produce the required `√N`
growth at fixed `q`."  Formally: the number of blocks is bounded by `(q-1)/2`, a quantity in
which `N` does not appear at all. -/
theorem block_count_bounded_by_q (pairs : Finset V) (B : J → Finset V) (r₀ : ℕ)
    (hr₀ : 1 ≤ r₀)
    (hsub : ∀ j, B j ⊆ pairs)
    (hdisj : ∀ j k : J, j ≠ k → Disjoint (B j) (B k))
    (hcard : ∀ j, (B j).card = r₀) :
    Fintype.card J ≤ pairs.card := by
  have h := value_budget_equal pairs B r₀ hsub hdisj hcard
  calc Fintype.card J = Fintype.card J * 1 := (Nat.mul_one _).symm
    _ ≤ Fintype.card J * r₀ := Nat.mul_le_mul_left _ hr₀
    _ ≤ pairs.card := h

/-- **`thm:block-obstruction` (50) written with the paper's own right-hand side `(q-1)/2`,
and the conclusion the paper draws from it.**

The draft left the instantiation `|pairs| = (q-1)/2` to the reader, so no theorem in it mentioned
`q` at all; this states equation (50) literally, plus the sentence that follows it — the block
count is bounded by a quantity in which `N` does not occur, so this allocation cannot track any
growth in `N` at fixed `q`.  (Added by the 2026-07-30 T3 audit.) -/
theorem value_budget_q (q : ℕ) (pairs : Finset V) (hpairs : pairs.card = (q - 1) / 2)
    (B : J → Finset V) (r₀ : ℕ) (hr₀ : 1 ≤ r₀)
    (hsub : ∀ j, B j ⊆ pairs)
    (hdisj : ∀ j k : J, j ≠ k → Disjoint (B j) (B k))
    (hcard : ∀ j, (B j).card = r₀) :
    (∑ j, (B j).card ≤ (q - 1) / 2)
      ∧ (Fintype.card J * r₀ ≤ (q - 1) / 2)
      ∧ (Fintype.card J ≤ (q - 1) / 2) :=
  ⟨hpairs ▸ value_budget pairs B hsub hdisj,
   hpairs ▸ value_budget_equal pairs B r₀ hsub hdisj hcard,
   hpairs ▸ block_count_bounded_by_q pairs B r₀ hr₀ hsub hdisj hcard⟩

end ValueBudget

/-! ## Non-vacuity witnesses -/

section Witness

/-- Part A witness: two blocks, each with state space `Fin 2` (`0` = NO, carrying inner mass
`-1/2`; `1` = YES, carrying inner mass `+1/2`).  Then `ρ_j = 1`, so the hypotheses of
`block_obstruction_corr` are all satisfiable and its conclusion is not vacuous. -/
private def wμ : ∀ _ : Fin 2, Fin 2 → ℚ := fun _ y => if y = 0 then -(1/2) else 1/2

private def wNO : ∀ _ : Fin 2, Fin 2 → Prop := fun _ y => y = 0

instance instWNODec (j : Fin 2) : DecidablePred (wNO j) := fun y => decEq y 0

private lemma wμ_isInner (j : Fin 2) : IsInnerBlock wμ wNO j where
  unit := by rw [Fin.sum_univ_two]; norm_num [wμ]
  zeroTotal := by rw [Fin.sum_univ_two]; norm_num [wμ]
  posYes := by
    intro y hy
    simp only [wNO]
    by_cases h : y = 0
    · rw [h] at hy; norm_num [wμ] at hy
    · exact h

private lemma wρ (j : Fin 2) : rho wμ wNO j = 1 := by
  rw [rho_eq wμ wNO (wμ_isInner j)]
  have hf : (univ.filter (fun y : Fin 2 => sgnNeg wμ j y = true ∧ wNO j y)) = {0} := by
    ext y; fin_cases y <;> simp [sgnNeg, wNO, wμ]
  rw [hf]
  simp [blockP, wμ]

/-- Non-vacuity for Part A. -/
example : ∀ j : Fin 2, rho wμ wNO j = 1 := wρ

/-- Non-vacuity for Part A's correlation identity: with the two witness blocks and the outer
measure `Ψ = (1/2, -1/2, 0, 0)` — unit ℓ¹, zero total — the composed correlation is exactly `-1`,
which is `-2·Ψ(-1,-1)·ρ₀ρ₁` with `ρ₀ = ρ₁ = 1`.  So `block_obstruction_corr` is not vacuous. -/
private def wΨ : (Fin 2 → Bool) → ℚ := fun s => if s 0 = true ∧ s 1 = true then 1/2
  else if s 0 = false ∧ s 1 = false then -(1/2) else 0

/-- The four sign vectors on two blocks, enumerated once. -/
private lemma sum_signVec (f : (Fin 2 → Bool) → ℚ) :
    ∑ s : (Fin 2 → Bool), f s
      = f ![false, false] + f ![false, true] + f ![true, false] + f ![true, true] := by
  have h : (univ : Finset (Fin 2 → Bool))
      = {![false, false], ![false, true], ![true, false], ![true, true]} := by decide
  rw [h, Finset.sum_insert (by decide), Finset.sum_insert (by decide),
    Finset.sum_insert (by decide), Finset.sum_singleton]
  ring

private lemma wΨ_isOuter : IsOuter wΨ where
  unit := by rw [sum_signVec]; norm_num [wΨ]
  zeroTotal := by rw [sum_signVec]; norm_num [wΨ]

example : corr (fun x : (∀ _ : Fin 2, Fin 2) => ∀ j, wNO j (x j)) (zeta wμ wΨ) = -1 := by
  rw [block_obstruction_corr wμ wNO wμ_isInner wΨ wΨ_isOuter _ (fun _ => Iff.rfl)]
  rw [Fin.prod_univ_two, wρ 0, wρ 1]
  norm_num [wΨ]

/-- Non-vacuity for clause (iii): the `4/5` hypothesis is satisfiable — a block whose NO layer
carries absolute weight `2/5` of the negative cell has `ρ = 4/5` exactly. -/
example : (0:ℚ) ≤ 4/5 ∧ ((4:ℚ)/5) * (4/5) = 16/25 := ⟨by norm_num, by norm_num⟩

/-! ### Witness for `block_obstruction_two_blocks_tilted` (gap-closure batch 2)

The identification hypothesis `ρ_j = 2|λ_0|/Z` is satisfiable, and at the tight point `m = 2`
its value is `4/5`.  Blocks: state space `Fin 3` with inner masses `(-2/5, -1/10, +1/2)`, the
first state being the NO layer.  Unit `ℓ¹`, zero total, positive mass on a YES state; the
negative cell carries `1/2` of which `2/5` is NO, so `ρ = 2·(2/5) = 4/5 = 2|λ_0|/Z` at `m = 2`. -/

private def tμ : ∀ _ : Fin 2, Fin 3 → ℚ :=
  fun _ y => if (y : ℕ) = 0 then -(2/5) else if (y : ℕ) = 1 then -(1/10) else 1/2

private def tNO : ∀ _ : Fin 2, Fin 3 → Prop := fun _ y => y = 0

instance instTNODec (j : Fin 2) : DecidablePred (tNO j) := fun y => decEq y 0

private lemma tμ_isInner (j : Fin 2) : IsInnerBlock tμ tNO j where
  unit := by rw [Fin.sum_univ_three]; norm_num [tμ]
  zeroTotal := by rw [Fin.sum_univ_three]; norm_num [tμ]
  posYes := by
    intro y hy
    simp only [tNO]
    fin_cases y
    · norm_num [tμ] at hy
    · decide
    · decide

private lemma tρ (j : Fin 2) : rho tμ tNO j = 4 / 5 := by
  rw [rho_eq tμ tNO (tμ_isInner j)]
  have hf : (univ.filter (fun y : Fin 3 => sgnNeg tμ j y = true ∧ tNO j y)) = {0} := by
    ext y; fin_cases y <;> simp [sgnNeg, tNO, tμ]
  rw [hf]
  norm_num [blockP, tμ]

open KsumAudit.Obstructions.TiltedBand in
/-- Non-vacuity for `block_obstruction_two_blocks_tilted`: at `m = 2` every hypothesis holds
for the `Fin 3` witness blocks, and the identification `ρ_j = 2|λ_0|/Z` is an equality of the
value `4/5`. -/
example : ∀ j : Fin 2, rho tμ tNO j = 2 * (|lam 2 0| / Znorm 2) := by
  intro j
  rw [tρ j, ← tilt_corr_two, mul_div_assoc]

open KsumAudit.Obstructions.TiltedBand in
example : |corr (fun x : (∀ _ : Fin 2, Fin 3) => ∀ j, tNO j (x j)) (zeta tμ wΨ)| ≤ 16 / 25
    ∧ (16:ℚ) / 25 < 2 / 3 :=
  block_obstruction_two_blocks_tilted tμ tNO tμ_isInner wΨ wΨ_isOuter _ (fun _ => Iff.rfl)
    (m := 2) (by norm_num) (fun j => by rw [tρ j, ← tilt_corr_two, mul_div_assoc])

/-- Non-vacuity for Part B: two blocks each receiving one of two available pairs. -/
example : ∑ j : Fin 2, ((fun j : Fin 2 => ({j} : Finset (Fin 2))) j).card ≤
    (Finset.univ : Finset (Fin 2)).card := by
  refine value_budget Finset.univ (fun j => {j}) (fun j => Finset.subset_univ _) ?_
  intro j k hjk
  simp [hjk]

/-- Non-vacuity for the `q`-indexed budget at `q = 5`: two available pairs, two blocks of one
pair each, and the conclusion `m ≤ 2 = (q-1)/2` holds with `N` nowhere in sight. -/
example : (∑ j : Fin 2, (({j} : Finset (Fin 2))).card ≤ (5 - 1) / 2)
    ∧ (Fintype.card (Fin 2) * 1 ≤ (5 - 1) / 2)
    ∧ (Fintype.card (Fin 2) ≤ (5 - 1) / 2) := by
  refine value_budget_q 5 Finset.univ (by decide) (fun j => {j}) 1 (by norm_num)
    (fun j => Finset.subset_univ _) ?_ (fun j => Finset.card_singleton j)
  intro j k hjk
  simp [hjk]

end Witness

#print axioms block_obstruction_corr
#print axioms block_obstruction_bound
#print axioms block_obstruction_band
#print axioms block_obstruction_band_combination
#print axioms rho_le_four_fifths
#print axioms two_block_corr_lt_two_thirds
#print axioms tilted_rho_le_four_fifths
#print axioms block_obstruction_two_blocks
#print axioms block_obstruction_two_blocks_tilted
#print axioms value_budget
#print axioms value_budget_equal
#print axioms block_count_bounded_by_q
#print axioms value_budget_q

end KsumAudit.Obstructions.Block
