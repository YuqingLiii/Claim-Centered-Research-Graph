import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic

/-!
# WHGAP shared definitions (DAG protocol §7.3 support module)

Serves the node modules `WHGAP.«order-boundary»` (P6), `WHGAP.«private-boundary»` (P14),
`WHGAP.«no-ascent-hierarchy»` (P9) and the self tests.  Everything here is a *definition*
plus the smallest sign facts about those definitions; no node claim lives in this file.

All scalars are the ones that appear in the frozen prose of
`channel-capacity/werner-holevo-gap/notes/WHGAP_P12A_PRIVATE_BOUNDARY_20260730.md`
(as quoted on `WHGAP.private-boundary`) and paper §5:

* `b x ε = x/2 + (1 - 3x/2) ε`   — the receiver-side scalar,
* `e x ε = (x/2)(1 - ε)`         — the environment-side scalar,
* `u x t r = t (1 - 3x/2)/r`     — receiver-side off-diagonal, `r` standing for `√2`,
* `v x t r = t x/(2 r)`          — environment-side off-diagonal,
* `epsC x  = 2(1-2x)/(2-3x)`     — the finite-ε BKM violation threshold of paper §5,
* `dOne x  = (1-x)(2-5x)/(2-x)`  — the isotropic first-order weight of the N1' note,
* `f s     = (1+s) log(1+s) + (1-s) log(1-s)` — the binary Holevo function.

**Square roots.**  `√2` is never written inside an algebraic identity: it enters as a
variable `r` carrying the hypotheses `0 < r` and `r ^ 2 = 2`, so that every identity closes
by `field_simp`/`ring` with no `Real.sqrt` simp lemmas in the loop.  Only the two *concrete*
definitions `sStar` and `Delta` mention `Real.sqrt 2`, and they are connected to the
`r`-parameterized lemmas by `Real.sq_sqrt`.
-/

namespace WHGAP.Support

open Real

/-- Receiver-side scalar `b(x,ε) = x/2 + (1 - 3x/2) ε`. -/
noncomputable def b (x ε : ℝ) : ℝ := x / 2 + (1 - 3 * x / 2) * ε

/-- Environment-side scalar `e(x,ε) = (x/2)(1 - ε)`. -/
noncomputable def e (x ε : ℝ) : ℝ := (x / 2) * (1 - ε)

/-- Receiver-side off-diagonal `u(x,t) = t (1 - 3x/2)/√2`, with `r` standing for `√2`. -/
noncomputable def u (x t r : ℝ) : ℝ := t * (1 - 3 * x / 2) / r

/-- Environment-side off-diagonal `v(x,t) = t x/(2√2)`, with `r` standing for `√2`. -/
noncomputable def v (x t r : ℝ) : ℝ := t * x / (2 * r)

/-- The finite-ε BKM violation threshold `ε_c(x) = 2(1-2x)/(2-3x)` (paper §5, R5b). -/
noncomputable def epsC (x : ℝ) : ℝ := 2 * (1 - 2 * x) / (2 - 3 * x)

/-- The isotropic first-order weight `d₁(x) = (1-x)(2-5x)/(2-x)` (N1' note, R5c closed form). -/
noncomputable def dOne (x : ℝ) : ℝ := (1 - x) * (2 - 5 * x) / (2 - x)

/-- The binary Holevo function `f(s) = (1+s) log(1+s) + (1-s) log(1-s)` (natural log ⇒ nats). -/
noncomputable def f (s : ℝ) : ℝ := (1 + s) * Real.log (1 + s) + (1 - s) * Real.log (1 - s)

/-- The coinciding Holevo argument `s*(x) = (1-2x)/(√2 (1-x))`. -/
noncomputable def sStar (x : ℝ) : ℝ := (1 - 2 * x) / (Real.sqrt 2 * (1 - x))

/-- The closed-form private-information gap
`Δ(x) = [(1-2x)(1-x)/(2-3x)] · f(s*(x))` of `WHGAP.private-boundary`. -/
noncomputable def Delta (x : ℝ) : ℝ := ((1 - 2 * x) * (1 - x) / (2 - 3 * x)) * f (sStar x)

section Denominators

variable {x : ℝ}

lemma two_sub_three_x_pos (hx0 : 0 < x) (hx : x < 1 / 2) : 0 < 2 - 3 * x := by linarith

lemma two_sub_three_x_ne (hx0 : 0 < x) (hx : x < 1 / 2) : (2 - 3 * x) ≠ 0 :=
  ne_of_gt (two_sub_three_x_pos hx0 hx)

lemma one_sub_x_pos (hx0 : 0 < x) (hx : x < 1 / 2) : 0 < 1 - x := by linarith

lemma one_sub_x_ne (hx0 : 0 < x) (hx : x < 1 / 2) : (1 - x) ≠ 0 :=
  ne_of_gt (one_sub_x_pos hx0 hx)

lemma one_sub_two_x_pos (hx : x < 1 / 2) : 0 < 1 - 2 * x := by linarith

/-- The same nonvanishing fact in the shape `ring_nf` produces (`2 - x * 3`).  `field_simp`
matches its side conditions syntactically after normalization, so both orientations must be
available in context; keeping this as a named lemma avoids silently unfinished `field_simp`
goals (a real failure observed while developing this file). -/
lemma two_sub_x_three_ne (hx0 : 0 < x) (hx : x < 1 / 2) : (2 - x * 3) ≠ 0 := by
  intro h; linarith

/-- `ε_c(x) (2 - 3x) = 2(1 - 2x)` — the cleared form of the threshold definition. -/
lemma epsC_mul_denom (hx0 : 0 < x) (hx : x < 1 / 2) :
    epsC x * (2 - 3 * x) = 2 * (1 - 2 * x) := by
  have h23 : (2 - 3 * x) ≠ 0 := two_sub_three_x_ne hx0 hx
  have h23' : (2 - x * 3) ≠ 0 := two_sub_x_three_ne hx0 hx
  unfold epsC
  field_simp

end Denominators

/-- `√2` as an `r` with the two hypotheses used by every `r`-parameterized identity. -/
lemma sqrt_two_spec : 0 < Real.sqrt 2 ∧ (Real.sqrt 2) ^ 2 = 2 := by
  refine ⟨Real.sqrt_pos.mpr (by norm_num), ?_⟩
  rw [Real.sq_sqrt] <;> norm_num

end WHGAP.Support

