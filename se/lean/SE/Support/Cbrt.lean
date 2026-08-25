/-
`SE/Support/Cbrt.lean` — non-node support module.  PROVED here: the integer
cube-root characterization of the taper length.

Nodes served (≥ 2): `SE.denom` (the taper window of `block_le`), `SE.goal`
(`rpow_sub_one_le_K`, the passage from `K` to `n^{1/3}`), and `SE.denom.assembly.envelope`
(`K_cube_le_real`).

A `sorry` here is a build failure by policy.  There is none.
-/
import SE.Support.Defs

namespace SE

/-! ## `K n` satisfies `K^3 ≤ n < (K+1)^3` -/

/-- Lower half of the characterization: `K n ^ 3 ≤ n`. -/
theorem K_pow_le (n : ℕ) : K n ^ 3 ≤ n :=
  Nat.findGreatest_spec (P := fun k => k ^ 3 ≤ n) (Nat.zero_le n) (by simp)

/-- `K n ≤ n`. -/
theorem K_le_self (n : ℕ) : K n ≤ n := Nat.findGreatest_le n

/-- Upper half of the characterization: `n < (K n + 1)^3`. -/
theorem lt_K_succ_pow (n : ℕ) : n < (K n + 1) ^ 3 := by
  by_cases h : K n + 1 ≤ n
  · have hg := Nat.findGreatest_is_greatest (P := fun k => k ^ 3 ≤ n) (Nat.lt_succ_self _) h
    exact Nat.lt_of_not_le hg
  · -- then `K n = n`, and `K n ^ 3 ≤ n` forces `n ≤ 1`
    have h1 : K n = n := le_antisymm (K_le_self n) (by omega)
    have h2 : n ^ 3 ≤ n := by have hk := K_pow_le n; rwa [h1] at hk
    have hn : n ≤ 1 := by
      by_contra hc
      have hc2 : 2 ≤ n := by omega
      have h2' : (n : ℤ) ^ 3 ≤ (n : ℤ) := by exact_mod_cast h2
      have hc' : (2 : ℤ) ≤ (n : ℤ) := by exact_mod_cast hc2
      nlinarith [h2', hc', sq_nonneg ((n : ℤ) - 1)]
    interval_cases n <;> decide

/-- Anything whose cube fits below `n` is at most `K n`. -/
theorem le_K {n k : ℕ} (h : k ^ 3 ≤ n) : k ≤ K n :=
  Nat.le_findGreatest (le_trans (Nat.le_self_pow (by norm_num) k) h) h

/-- In the active taper window `n ≥ 27` one has `K n ≥ 3`. -/
theorem three_le_K {n : ℕ} (hn : 27 ≤ n) : 3 ≤ K n :=
  le_K (le_trans (by norm_num : (3 : ℕ) ^ 3 ≤ 27) hn)

/-- In the active taper window `n ≥ 27` one has `9·K n ≤ n` (hence `K n < n` and `2·K n ≤ n`). -/
theorem nine_mul_K_le {n : ℕ} (hn : 27 ≤ n) : 9 * K n ≤ n := by
  have hK3 : 3 ≤ K n := three_le_K hn
  have h9 : 9 * K n ≤ K n ^ 3 := by
    calc 9 * K n = 3 * 3 * K n := by ring
      _ ≤ K n * K n * K n := Nat.mul_le_mul (Nat.mul_le_mul hK3 hK3) (le_refl _)
      _ = K n ^ 3 := by ring
  exact le_trans h9 (K_pow_le n)

/-- The characterization is *unique*: `K` is determined by `k^3 ≤ n < (k+1)^3`. -/
theorem K_unique {n k : ℕ} (h1 : k ^ 3 ≤ n) (h2 : n < (k + 1) ^ 3) : K n = k := by
  have hkn : k ≤ n := le_trans (Nat.le_self_pow (by norm_num) k) h1
  have hle : k ≤ K n := Nat.le_findGreatest hkn h1
  refine le_antisymm ?_ hle
  by_contra hc
  have hc' : k + 1 ≤ K n := by omega
  have hcube : (k + 1) ^ 3 ≤ K n ^ 3 := Nat.pow_le_pow_left hc' 3
  exact absurd (le_trans hcube (K_pow_le n)) (Nat.not_le.mpr h2)

/-! ## Bridge to the real cube root -/

private lemma rpow_cube_cancel {x : ℝ} (hx : 0 ≤ x) : (x ^ (3 : ℕ)) ^ ((1 : ℝ) / 3) = x := by
  rw [← Real.rpow_natCast x 3, ← Real.rpow_mul hx]
  norm_num

/-- `(K n : ℝ) ≤ n^{1/3}`. -/
theorem K_le_rpow (n : ℕ) : (K n : ℝ) ≤ (n : ℝ) ^ ((1 : ℝ) / 3) := by
  have h : ((K n : ℝ)) ^ (3 : ℕ) ≤ (n : ℝ) := by exact_mod_cast K_pow_le n
  calc (K n : ℝ) = (((K n : ℝ)) ^ (3 : ℕ)) ^ ((1 : ℝ) / 3) :=
        (rpow_cube_cancel (by positivity)).symm
    _ ≤ (n : ℝ) ^ ((1 : ℝ) / 3) := Real.rpow_le_rpow (by positivity) h (by norm_num)

/-- `n^{1/3} < K n + 1`. -/
theorem rpow_lt_K_succ (n : ℕ) : (n : ℝ) ^ ((1 : ℝ) / 3) < (K n : ℝ) + 1 := by
  have h : (n : ℝ) < ((K n : ℝ) + 1) ^ (3 : ℕ) := by exact_mod_cast lt_K_succ_pow n
  calc (n : ℝ) ^ ((1 : ℝ) / 3)
      < ((((K n : ℝ) + 1)) ^ (3 : ℕ)) ^ ((1 : ℝ) / 3) :=
        Real.rpow_lt_rpow (by positivity) h (by norm_num)
    _ = (K n : ℝ) + 1 := rpow_cube_cancel (by positivity)

/-- `K n` really is `⌊n^{1/3}⌋`: the combinatorial definition and the real-analytic one agree.
This is the definition self-test demanded by the node, at the level of `K`. -/
theorem K_eq_floor_rpow (n : ℕ) : K n = ⌊(n : ℝ) ^ ((1 : ℝ) / 3)⌋₊ := by
  symm
  rw [Nat.floor_eq_iff (by positivity)]
  exact ⟨K_le_rpow n, rpow_lt_K_succ n⟩

/-- The quantitative form used by the assembly: `n^{1/3} - 1 ≤ K n`. -/
theorem rpow_sub_one_le_K (n : ℕ) : (n : ℝ) ^ ((1 : ℝ) / 3) - 1 ≤ (K n : ℝ) := by
  have := rpow_lt_K_succ n
  linarith

/-- `(K n : ℝ)^3 ≤ n`, the real form of `K_pow_le`. -/
theorem K_cube_le_real (n : ℕ) : ((K n : ℝ)) ^ (3 : ℕ) ≤ (n : ℝ) := by
  exact_mod_cast K_pow_le n

end SE
