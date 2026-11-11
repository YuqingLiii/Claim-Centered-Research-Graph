import WHGAP.«order-boundary»
import WHGAP.«private-boundary»
import WHGAP.«no-ascent-hierarchy»

/-!
# `WHGAP.SelfTest` (DAG protocol §7.3)

Decidable / rational checks that the *definitions* reproduce independently computed exact
values, and that the *identities* are non-vacuous at concrete rational points.  Everything
here closes by `norm_num`; nothing here is a node claim.

## Append-only finding (commission LEAN-1, derive-and-verify)

The commission proposed testing both forcing identities at `(x, p, d) = (2/5, 1/3, 2/5)`.
Independent evaluation (sympy, `artifacts/logs_whgap_lean_20260730/sympy_identity_check.log`)
shows that point is **degenerate for both**: `3p - 1 = 0` at `p = 1/3` and
`3d + 2x - 2 = 0` at `(x,d) = (2/5, 2/5)`, so each identity reads `0 = 0` there and would pass
even if the left-hand sides were mis-transcribed.  The point is kept (it is a legitimate
zero-locus check, and it is recorded as such) but two **non-degenerate** points are added for
each identity, where both sides are nonzero and equal.

The commission's parenthetical "`ε_c(9/20) = 1/13...`" is a typo corrected in the same
sentence of the commission itself; the value verified here is `ε_c(9/20) = 4/13`.
-/

namespace WHGAP.SelfTest

open WHGAP.Support

/-! ## Definition values at rational points -/

example : dOne (2 / 5) = 0 := by norm_num [dOne]
example : dOne (1 / 5) = 4 / 9 := by norm_num [dOne]
example : dOne (1 / 4) = 9 / 28 := by norm_num [dOne]
example : dOne (9 / 20) = -11 / 124 := by norm_num [dOne]

example : epsC (9 / 20) = 4 / 13 := by norm_num [epsC]
example : epsC (1 / 4) = 4 / 5 := by norm_num [epsC]
example : epsC (2 / 5) = 1 / 2 := by norm_num [epsC]
example : epsC (1 / 2) = 0 := by norm_num [epsC]

example : b (1 / 4) (1 / 5) = 1 / 4 := by norm_num [b]
example : e (1 / 4) (1 / 5) = 1 / 10 := by norm_num [e]
example : b (2 / 5) (1 / 2) = 2 / 5 := by norm_num [b]
example : e (2 / 5) (1 / 2) = 1 / 10 := by norm_num [e]

/-- `b(x, ε_c(x)/2) = (1-x)/2` at `x = 9/20`: `(1 - 9/20)/2 = 11/40`. -/
example : b (9 / 20) (epsC (9 / 20) / 2) = 11 / 40 := by norm_num [b, epsC]

/-- `e(x, ε_c(x)/2) = x(1-x)/(2(2-3x))` at `x = 9/20`: `(9/20)(11/20)/(2 · 13/20) = 99/520`. -/
example : e (9 / 20) (epsC (9 / 20) / 2) = 99 / 520 := by norm_num [e, epsC]

/-! ## Eigenvalue branches

**R12 minor m4 (2026-07-31).**  These used to test `WHGAP.«signed-lift-extension».lam5`/`lam3`,
a duplicate pair now deleted; they test the single surviving pair
`WHGAP.DefectChoi.lam5`/`lam3`, which is the one both the P2 sign theorems and the WP-A
spectrum core use. -/

example : DefectChoi.lam5 (1 / 4) = -6 := by
  norm_num [DefectChoi.lam5]

example : DefectChoi.lam3 (1 / 4) = -4 / 3 := by
  norm_num [DefectChoi.lam3]

example : DefectChoi.lam5 (1 / 2) = 0 := by
  norm_num [DefectChoi.lam5]

example : DefectChoi.lam3 (1 / 3) = 0 := by
  norm_num [DefectChoi.lam3]

/-! ## Forcing identities at rational points (degenerate + non-degenerate) -/

/-- Degenerate point from the commission: both sides vanish (`3p - 1 = 0`). -/
example : (3 * (1 / 3 : ℝ) - 1) ^ 2 * ((2 / 5 : ℝ) - 1) / (2 / 5) = 0 := by norm_num

/-- Non-degenerate check of `forcing_p` at `(x, p) = (1/4, 1/2)`: both sides `= -3/4`. -/
example :
    ((1 / 2 : ℝ) - 1) * ((1 / 4 : ℝ) - 1) * ((1 / 2 : ℝ) + 2 * (1 / 4) - 1) / (1 / 4)
      + 4 * (((1 / 4 : ℝ) - 1) * (2 * (1 / 2 : ℝ) ^ 2 + (1 / 2) * (1 / 4) - 2 * (1 / 2)
          + (1 / 4))) / (2 * (1 / 4))
      + 2 * (((1 / 4 : ℝ) - 1) * ((1 / 2 : ℝ) ^ 2 - (1 / 2) * (1 / 4) - 2 * (1 / 4) + 1))
          / (1 / 4)
      + 2 * (((1 / 4 : ℝ) - 1) * ((1 / 2 : ℝ) ^ 2 - (1 / 2) * (1 / 4) + 2 * (1 / 4) - 1))
          / (1 / 4)
    = -3 / 4 := by norm_num

example : (3 * (1 / 2 : ℝ) - 1) ^ 2 * ((1 / 4 : ℝ) - 1) / (1 / 4) = -3 / 4 := by norm_num

/-- Degenerate point from the commission for `forcing_d` (`3d + 2x - 2 = 0`). -/
example : -(3 * (2 / 5 : ℝ) + 2 * (2 / 5) - 2) ^ 2 / (2 / 5) = 0 := by norm_num

/-- Non-degenerate check of `forcing_d` at `(x, d) = (1/4, 1/3)`: both sides `= -1`. -/
example :
    2 * (-(9 * (1 / 3 : ℝ) ^ 2 + 4 * (1 / 3) * (1 / 4) - 8 * (1 / 3)
        + 4 * (1 / 4 : ℝ) ^ 2 - 8 * (1 / 4) + 4) / (2 * (1 / 4)))
      + 2 * (-(2 * (1 / 3 : ℝ) * (2 * (1 / 4) - 1)) / (1 / 4))
    = -1 := by norm_num

example : -(3 * (1 / 3 : ℝ) + 2 * (1 / 4) - 2) ^ 2 / (1 / 4) = -1 := by norm_num

/-! ## The `ε = 0` gap and the finite-`ε` factorization at rational points -/

/-- `2(1-x)(2x-1)/x` at `x = 9/20` equals `2 · (11/20) · (-1/10)/(9/20) = -11/45`. -/
example : 2 * (1 - (9 / 20 : ℝ)) * (2 * (9 / 20) - 1) / (9 / 20) = -11 / 45 := by norm_num

/-- `threshold_factorization` at `(x, ε) = (9/20, 1/10)` — both sides `= -297/4000`. -/
example :
    (9 / 20 : ℝ) * b (9 / 20) (1 / 10) - 2 * (1 - 3 * (9 / 20 : ℝ) / 2) ^ 2 * (1 - 1 / 10)
      = -297 / 4000 := by norm_num [b]

example :
    2 * (1 - (9 / 20 : ℝ)) * ((2 * (9 / 20 : ℝ) - 1) + (1 - 3 * (9 / 20 : ℝ) / 2) * (1 / 10))
      = -297 / 4000 := by norm_num

/-! ## `s*` and `Δ` sanity: the algebraic prefactor at a rational point -/

/-- The `Δ` prefactor `(1-2x)(1-x)/(2-3x)` at `x = 9/20` equals `11/130`. -/
example : (1 - 2 * (9 / 20 : ℝ)) * (1 - (9 / 20 : ℝ)) / (2 - 3 * (9 / 20 : ℝ)) = 11 / 130 := by
  norm_num

/-- `f 0 = 0` (the anchor of `f_pos`). -/
example : f 0 = 0 := by simp [f]

end WHGAP.SelfTest

