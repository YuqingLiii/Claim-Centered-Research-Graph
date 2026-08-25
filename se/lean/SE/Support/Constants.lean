/-
`SE/Support/Constants.lean` — non-node support module.  PROVED here:

  * `M = (2/(3√3))(√2 + √(15/8)) = (4√6 + 3√10)/18`   (paper eq:Mconstant)
  * `1/(2(1+M)) = 9/(18 + 4√6 + 3√10)`                (paper, proof of Theorem B)
  * the printed decimal `0.2413852814754581733…` certified to 19 significant digits;
  * the elementary `√` comparison helpers used throughout.

Nodes served (≥ 2): `SE.denom` (`Mconst_split`, `Mconst_pos` in the per-defect envelope) and
`SE.goal` (`inv_two_one_add_Mconst`, `Cconst_digits` in Theorem B), plus the support module
`SE.Support.Limits`.

No `sorry`.
-/
import SE.Support.Defs

namespace SE

/-! ## Elementary square-root comparison helpers -/

/-- `√(a/b) = √a/√b` for `a ≥ 0`, in the robust `Real.sqrt` form (`b < 0` is handled by
`Real.sqrt` returning `0`). -/
theorem sqrt_div_eq {a b : ℝ} (ha : 0 ≤ a) :
    Real.sqrt (a / b) = Real.sqrt a / Real.sqrt b := by
  rw [div_eq_mul_inv, Real.sqrt_mul ha, Real.sqrt_inv, div_eq_mul_inv]

theorem sqrt_lt_of_sq {x a : ℝ} (hx : 0 ≤ x) (ha : 0 < a) (h : x < a ^ 2) :
    Real.sqrt x < a := by
  have h1 := Real.sq_sqrt hx
  have h2 := Real.sqrt_nonneg x
  nlinarith

theorem lt_sqrt_of_sq {x a : ℝ} (hx : 0 ≤ x) (ha : 0 ≤ a) (h : a ^ 2 < x) :
    a < Real.sqrt x := by
  have h1 := Real.sq_sqrt hx
  have h2 := Real.sqrt_nonneg x
  nlinarith

/-! ## Radical normalizations -/

theorem sqrt_six : Real.sqrt 6 = Real.sqrt 2 * Real.sqrt 3 := by
  rw [← Real.sqrt_mul (by norm_num : (0:ℝ) ≤ 2)]
  norm_num

theorem sqrt_ten : Real.sqrt 10 = Real.sqrt 2 * Real.sqrt 5 := by
  rw [← Real.sqrt_mul (by norm_num : (0:ℝ) ≤ 2)]
  norm_num

/-- `√(15/8) = √2·√3·√5/4`. -/
theorem sqrt_fifteen_eighths :
    Real.sqrt (15 / 8) = Real.sqrt 2 * Real.sqrt 3 * Real.sqrt 5 / 4 := by
  have h2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have h3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num)
  have key : (15 : ℝ) / 8 = (Real.sqrt 2 * Real.sqrt 3 * Real.sqrt 5 / 4) ^ 2 := by
    rw [div_pow, mul_pow, mul_pow, h2, h3, h5]
    norm_num
  rw [key, Real.sqrt_sq (by positivity)]

/-- `2/(3√3) = 2√3/9`, the value `max_{0≤x≤1}(1-x)√x` of the paper's `f(1/3)=2/(3√3)`. -/
theorem two_div_three_sqrt_three : 2 / (3 * Real.sqrt 3) = 2 * Real.sqrt 3 / 9 := by
  have h3 : Real.sqrt 3 * Real.sqrt 3 = 3 := Real.mul_self_sqrt (by norm_num)
  have hpos : (0:ℝ) < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  rw [div_eq_div_iff (by positivity) (by norm_num)]
  linear_combination (-6 : ℝ) * h3

/-! ## The two closed-form identities -/

/-- **`M = (4√6 + 3√10)/18`** — paper eq:Mconstant. -/
theorem Mconst_eq : Mconst = (4 * Real.sqrt 6 + 3 * Real.sqrt 10) / 18 := by
  have h3 : Real.sqrt 3 * Real.sqrt 3 = 3 := Real.mul_self_sqrt (by norm_num)
  unfold Mconst
  rw [two_div_three_sqrt_three, sqrt_fifteen_eighths, sqrt_six, sqrt_ten]
  linear_combination (Real.sqrt 2 * Real.sqrt 5 / 18) * h3

/-- `M` split into its two envelope contributions, the `Y` term and the lower-block term.
This is the form the assembly consumes. -/
theorem Mconst_split :
    Mconst = Real.sqrt 2 * (2 * Real.sqrt 3 / 9)
      + Real.sqrt (15 / 8) * (2 * Real.sqrt 3 / 9) := by
  unfold Mconst
  rw [two_div_three_sqrt_three]
  ring

theorem Mconst_pos : 0 < Mconst := by
  rw [Mconst_eq]
  have h6 : 0 < Real.sqrt 6 := Real.sqrt_pos.mpr (by norm_num)
  have h10 : 0 < Real.sqrt 10 := Real.sqrt_pos.mpr (by norm_num)
  positivity

/-- A crude numeric cap on `M` used to keep the assembly's error constants explicit. -/
theorem Mconst_lt_two : Mconst < 2 := by
  rw [Mconst_eq]
  have h6 : Real.sqrt 6 < 5 / 2 := sqrt_lt_of_sq (by norm_num) (by norm_num) (by norm_num)
  have h10 : Real.sqrt 10 < 13 / 4 := sqrt_lt_of_sq (by norm_num) (by norm_num) (by norm_num)
  linarith

/-- **`1/(2(1+M)) = 9/(18 + 4√6 + 3√10) = C`** — paper, proof of Theorem B. -/
theorem inv_two_one_add_Mconst : 1 / (2 * (1 + Mconst)) = Cconst := by
  have h6 : 0 < Real.sqrt 6 := Real.sqrt_pos.mpr (by norm_num)
  have h10 : 0 < Real.sqrt 10 := Real.sqrt_pos.mpr (by norm_num)
  unfold Cconst
  rw [Mconst_eq]
  have hne : (18 : ℝ) + 4 * Real.sqrt 6 + 3 * Real.sqrt 10 ≠ 0 := by positivity
  field_simp
  ring

theorem Cconst_pos : 0 < Cconst := by
  rw [← inv_two_one_add_Mconst]
  have := Mconst_pos
  positivity

/-! ## The printed decimal, certified

The paper prints `9/(18+4√6+3√10) = 0.2413852814754581733…`.  The two bounds below pin exactly
those 19 digits. -/

theorem sqrt_six_bounds :
    (2449489742783178098 : ℝ) / 10 ^ 18 < Real.sqrt 6 ∧
      Real.sqrt 6 < (2449489742783178099 : ℝ) / 10 ^ 18 := by
  constructor
  · exact lt_sqrt_of_sq (by norm_num) (by norm_num) (by norm_num)
  · exact sqrt_lt_of_sq (by norm_num) (by norm_num) (by norm_num)

theorem sqrt_ten_bounds :
    (3162277660168379331 : ℝ) / 10 ^ 18 < Real.sqrt 10 ∧
      Real.sqrt 10 < (3162277660168379332 : ℝ) / 10 ^ 18 := by
  constructor
  · exact lt_sqrt_of_sq (by norm_num) (by norm_num) (by norm_num)
  · exact sqrt_lt_of_sq (by norm_num) (by norm_num) (by norm_num)

/-- **The conditional constant to 19 significant digits**:
`0.2413852814754581732 < C < 0.2413852814754581734`, certifying the paper's printed value
`C = 0.2413852814754581733…`. -/
theorem Cconst_digits :
    (2413852814754581732 : ℝ) / 10 ^ 19 < Cconst ∧
      Cconst < (2413852814754581734 : ℝ) / 10 ^ 19 := by
  obtain ⟨h6l, h6u⟩ := sqrt_six_bounds
  obtain ⟨h10l, h10u⟩ := sqrt_ten_bounds
  have hD : (0:ℝ) < 18 + 4 * Real.sqrt 6 + 3 * Real.sqrt 10 := by
    have := Real.sqrt_nonneg 6
    have := Real.sqrt_nonneg 10
    linarith
  unfold Cconst
  constructor
  · rw [lt_div_iff₀ hD]
    nlinarith [h6u, h10u]
  · rw [div_lt_iff₀ hD]
    nlinarith [h6l, h10l]

end SE
