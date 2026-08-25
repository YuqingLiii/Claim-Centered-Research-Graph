/-
`SE/Support/Envelope.lean` — non-node support module.  PROVED here: the
elementary envelope calculus behind the paper's eq:final-envelope.

  * `(1-x)√x ≤ 2√3/9 = 2/(3√3)` for `x ≥ 0`  (paper §9: `f(x)=(1-x)√x`, `f(1/3)=2/(3√3)`);
  * its three discrete instances: the `Y` term, the diagonal-`Φ` term, and the lower-block term
    of eq:final-envelope.

Direct consumer: the node module `SE/denom.lean` (`SE.denom.composition`, via `block_le`);
`SE.one_sub_mul_sqrt_le` is additionally cited by `SE/Trust.lean` and re-checked in
`SE/SelfTest.lean`.

PLACEMENT (coordinator ruling R1, 2026-07-30).  This content previously sat in
`SE/denom/assembly/envelope.lean`, a node-shaped path for the node `SE.denom.assembly.envelope`
(alias `ENV`).  That was a mis-siting: ENV's frozen Claim is the finite NUMERICAL hook-envelope
check `ρ_{n,k} ≤ R_{n,k}` (in-spec max 16/15, 0 violations / 32612 tuples), which is
representation-theoretic data with no tier-1 rendering — its tier-1 shadow enters as the CITED
fields `SE.SEFrame.Cited.rho_ge_one` / `rho_le` (paper eq:rho-asymp).  A node module whose `Claim`
cannot mirror the frozen prose violates the anti-drift checks (§7.6), so the ENV node records
no `formalization` block and this calculus lives here as plain support.  By §7.3's letter, single-consumer
lemmas could live inside `SE/denom.lean`; they are kept here by the same ruling so the ENV record
has a stable non-node home to point at and `SE/denom.lean` stays at composition altitude.

Imports the node module `SE.denom.taper` for the `α`-value lemmas (`alpha_nonneg`, `alpha_le_K`,
`alpha_antitone`); that import does not create a node-graph edge (this is not a node module).

No `sorry`.
-/
import SE.Support.Defs
import SE.Support.Constants
import SE.Support.Limits
import SE.denom.taper

namespace SE

/-! ## The continuous envelope `max_{x ≥ 0} (1-x)√x = 2/(3√3)` -/

/-- The exact factorization behind the maximum: for `s = √3`,
`t³ - t + 2s/9 = (t - s/3)²(t + 2s/3)`.  The double root at `t = 1/√3` is the maximizer
`x = t² = 1/3` of the paper's `f'(x) = (1-3x)/(2√x)`. -/
theorem cubic_factor (t : ℝ) :
    t ^ 3 - t + 2 * Real.sqrt 3 / 9
      = (t - Real.sqrt 3 / 3) ^ 2 * (t + 2 * Real.sqrt 3 / 3) := by
  have h3 : Real.sqrt 3 * Real.sqrt 3 = 3 := Real.mul_self_sqrt (by norm_num)
  linear_combination (t / 3 - 2 * Real.sqrt 3 / 27) * h3

/-- **`(1-x)·√x ≤ 2√3/9` for every `x ≥ 0`.**  This is the paper's
`max_{0≤x≤1} f(x) = f(1/3) = 2/(3√3)` (`SE.two_div_three_sqrt_three` converts the constant);
it holds for `x > 1` too, where the left-hand side is negative. -/
theorem one_sub_mul_sqrt_le {x : ℝ} (hx : 0 ≤ x) :
    (1 - x) * Real.sqrt x ≤ 2 * Real.sqrt 3 / 9 := by
  have ht0 : 0 ≤ Real.sqrt x := Real.sqrt_nonneg x
  have htx : Real.sqrt x ^ 2 = x := Real.sq_sqrt hx
  have hs : 0 < Real.sqrt 3 := Real.sqrt_pos.mpr (by norm_num)
  have hfac : 0 ≤ Real.sqrt x ^ 3 - Real.sqrt x + 2 * Real.sqrt 3 / 9 := by
    rw [cubic_factor]
    have h1 : (0 : ℝ) ≤ Real.sqrt x + 2 * Real.sqrt 3 / 3 := by positivity
    positivity
  nlinarith [hfac, htx, ht0]

/-! ## The `Y`-channel term (eq:final-envelope, second summand) -/

/-- `α_d·√(d/n) ≤ 2√3/9`, using only `K³ ≤ n`.  No error term: the inequality is exact,
because `K³ ≤ n` is exactly what makes `(K-d)√(d/n) ≤ (1-x)√x` at `x = d/K`. -/
theorem alpha_mul_sqrt_div_le {n Kv d : ℕ} (hKn : ((Kv : ℝ)) ^ (3 : ℕ) ≤ (n : ℝ))
    (hd : d < Kv) :
    alpha Kv d * Real.sqrt ((d : ℝ) / (n : ℝ)) ≤ 2 * Real.sqrt 3 / 9 := by
  have hKvN : 0 < Kv := by omega
  have hKv : (0 : ℝ) < (Kv : ℝ) := by exact_mod_cast hKvN
  have hd0 : (0 : ℝ) ≤ (d : ℝ) := Nat.cast_nonneg d
  have hdle : (d : ℝ) ≤ (Kv : ℝ) := by exact_mod_cast le_of_lt hd
  have hcube : (0 : ℝ) < ((Kv : ℝ)) ^ (3 : ℕ) := by positivity
  have hn : (0 : ℝ) < (n : ℝ) := lt_of_lt_of_le hcube hKn
  have halpha : alpha Kv d = (Kv : ℝ) - (d : ℝ) := by
    unfold alpha
    exact_mod_cast Nat.cast_sub (le_of_lt hd)
  have hAnn : (0 : ℝ) ≤ (Kv : ℝ) - (d : ℝ) := by linarith
  have h1 : Real.sqrt ((d : ℝ) / (n : ℝ)) ≤ Real.sqrt ((d : ℝ) / ((Kv : ℝ)) ^ (3 : ℕ)) := by
    apply Real.sqrt_le_sqrt
    rw [div_le_div_iff₀ hn hcube]
    exact mul_le_mul_of_nonneg_left hKn hd0
  have hsqK : Real.sqrt (((Kv : ℝ)) ^ (3 : ℕ)) = (Kv : ℝ) * Real.sqrt (Kv : ℝ) := by
    rw [show ((Kv : ℝ)) ^ (3 : ℕ) = ((Kv : ℝ)) ^ (2 : ℕ) * (Kv : ℝ) by ring,
      Real.sqrt_mul (by positivity), Real.sqrt_sq hKv.le]
  have hsqKpos : (0 : ℝ) < Real.sqrt (Kv : ℝ) := Real.sqrt_pos.mpr hKv
  have h2 : ((Kv : ℝ) - (d : ℝ)) * Real.sqrt ((d : ℝ) / ((Kv : ℝ)) ^ (3 : ℕ))
      = (1 - (d : ℝ) / (Kv : ℝ)) * Real.sqrt ((d : ℝ) / (Kv : ℝ)) := by
    rw [sqrt_div_eq hd0, sqrt_div_eq hd0, hsqK]
    field_simp
  calc alpha Kv d * Real.sqrt ((d : ℝ) / (n : ℝ))
      = ((Kv : ℝ) - (d : ℝ)) * Real.sqrt ((d : ℝ) / (n : ℝ)) := by rw [halpha]
    _ ≤ ((Kv : ℝ) - (d : ℝ)) * Real.sqrt ((d : ℝ) / ((Kv : ℝ)) ^ (3 : ℕ)) :=
        mul_le_mul_of_nonneg_left h1 hAnn
    _ = (1 - (d : ℝ) / (Kv : ℝ)) * Real.sqrt ((d : ℝ) / (Kv : ℝ)) := h2
    _ ≤ 2 * Real.sqrt 3 / 9 := one_sub_mul_sqrt_le (by positivity)

/-! ## The lower-block term (eq:final-envelope, fourth summand) -/

/-- `α_{d+1}·√(d/(n-d)) ≤ (2√3/9)·√(n/(n-K))`.  The distortion factor `√(n/(n-K))` is the only
loss relative to the `Y` term; it tends to `1`. -/
theorem alpha_succ_mul_sqrt_lower_le {n Kv d : ℕ} (hKn : ((Kv : ℝ)) ^ (3 : ℕ) ≤ (n : ℝ))
    (hd : d < Kv) (hlt : (Kv : ℝ) < (n : ℝ)) :
    alpha Kv (d + 1) * Real.sqrt ((d : ℝ) / ((n : ℝ) - (d : ℝ)))
      ≤ (2 * Real.sqrt 3 / 9) * distort n Kv := by
  have hKvN : 0 < Kv := by omega
  have hKv : (0 : ℝ) < (Kv : ℝ) := by exact_mod_cast hKvN
  have hn : (0 : ℝ) < (n : ℝ) := lt_trans hKv hlt
  have hd0 : (0 : ℝ) ≤ (d : ℝ) := Nat.cast_nonneg d
  have hdK : (d : ℝ) ≤ (Kv : ℝ) := by exact_mod_cast le_of_lt hd
  have hnd : (0 : ℝ) < (n : ℝ) - (d : ℝ) := by linarith
  have hnK : (0 : ℝ) < (n : ℝ) - (Kv : ℝ) := by linarith
  have hsplit : (d : ℝ) / ((n : ℝ) - (d : ℝ))
      = ((d : ℝ) / (n : ℝ)) * ((n : ℝ) / ((n : ℝ) - (d : ℝ))) := by
    field_simp
  have hratio : (n : ℝ) / ((n : ℝ) - (d : ℝ)) ≤ (n : ℝ) / ((n : ℝ) - (Kv : ℝ)) := by
    rw [div_le_div_iff₀ hnd hnK]
    nlinarith
  have hsq : Real.sqrt ((d : ℝ) / ((n : ℝ) - (d : ℝ)))
      ≤ Real.sqrt ((d : ℝ) / (n : ℝ)) * distort n Kv := by
    rw [hsplit, Real.sqrt_mul (by positivity)]
    exact mul_le_mul_of_nonneg_left (Real.sqrt_le_sqrt hratio) (Real.sqrt_nonneg _)
  have hmono : alpha Kv (d + 1) ≤ alpha Kv d := alpha_antitone (Nat.le_succ d)
  have hY := alpha_mul_sqrt_div_le hKn hd
  calc alpha Kv (d + 1) * Real.sqrt ((d : ℝ) / ((n : ℝ) - (d : ℝ)))
      ≤ alpha Kv d * (Real.sqrt ((d : ℝ) / (n : ℝ)) * distort n Kv) := by
        apply mul_le_mul hmono hsq (Real.sqrt_nonneg _) (alpha_nonneg _ _)
    _ = (alpha Kv d * Real.sqrt ((d : ℝ) / (n : ℝ))) * distort n Kv := by ring
    _ ≤ (2 * Real.sqrt 3 / 9) * distort n Kv :=
        mul_le_mul_of_nonneg_right hY (distort_nonneg n Kv)

/-! ## The diagonal-`Φ` term (eq:final-envelope, third summand) -/

/-- `√6·α_d/√(n-2d+1) ≤ errDiag n K` for every `d < K`: the diagonal-`Φ` term is uniformly
bounded by its value at `d = K`, which is `O(K/√n) = O(n^{-1/6})`. -/
theorem diag_term_le {n Kv d : ℕ} (hd : d < Kv) (hpos : (0 : ℝ) < (n : ℝ) - 2 * (Kv : ℝ) + 1) :
    Real.sqrt 6 * alpha Kv d / Real.sqrt ((n : ℝ) - 2 * (d : ℝ) + 1) ≤ errDiag n Kv := by
  have hdK : (d : ℝ) ≤ (Kv : ℝ) := by exact_mod_cast le_of_lt hd
  have hpos' : (0 : ℝ) < (n : ℝ) - 2 * (d : ℝ) + 1 := by linarith
  have hs1 : (0 : ℝ) < Real.sqrt ((n : ℝ) - 2 * (Kv : ℝ) + 1) := Real.sqrt_pos.mpr hpos
  have hs2 : (0 : ℝ) < Real.sqrt ((n : ℝ) - 2 * (d : ℝ) + 1) := Real.sqrt_pos.mpr hpos'
  have hsle : Real.sqrt ((n : ℝ) - 2 * (Kv : ℝ) + 1)
      ≤ Real.sqrt ((n : ℝ) - 2 * (d : ℝ) + 1) := Real.sqrt_le_sqrt (by linarith)
  have hnum : Real.sqrt 6 * alpha Kv d ≤ Real.sqrt 6 * (Kv : ℝ) :=
    mul_le_mul_of_nonneg_left (alpha_le_K Kv d) (Real.sqrt_nonneg 6)
  have hnum0 : (0 : ℝ) ≤ Real.sqrt 6 * alpha Kv d :=
    mul_nonneg (Real.sqrt_nonneg 6) (alpha_nonneg _ _)
  unfold errDiag
  rw [div_le_div_iff₀ hs2 hs1]
  nlinarith [hnum, hnum0, hsle, hs1.le, hs2.le,
    mul_nonneg (Real.sqrt_nonneg 6) (Nat.cast_nonneg (α := ℝ) Kv)]

end SE
