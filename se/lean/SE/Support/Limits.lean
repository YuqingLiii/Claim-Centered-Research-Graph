/-
`SE/Support/Limits.lean` — non-node support module.  PROVED here: the `o(1)`
bookkeeping of the assembly.

The paper writes `‖D‖ ≤ 1 + M + o(1)` (eq:Dfinal) and `K = (1-o(1))n^{1/3}`.  This file makes
both explicit: `errEnv n (K n) ≤ 5·n^{-1/6}` for `n ≥ 27`, hence `errEnv → 0` and
`envBound c → 1 + M`.  It also carries the elementary positivity facts about `errDiag`, `distort`
and `envBound` that both `SE.denom` and `SE.goal` consume.

Nodes served (≥ 2): `SE.denom` (`envBound_pos`, `errEnv_nonneg'`), `SE.goal`
(`tendsto_envBound`, `tendsto_one_div_rpow`, `envBound_pos`), and
`SE.denom.assembly.envelope` (`distort_nonneg`, `one_le_distort`, `errDiag_nonneg`).

No `sorry`.
-/
import SE.Support.Defs
import SE.Support.Cbrt
import SE.Support.Constants

open Filter Topology

namespace SE

/-! ## Elementary facts about the error functions -/

theorem distort_nonneg (n Kv : ℕ) : 0 ≤ distort n Kv := Real.sqrt_nonneg _

/-- `√(n/(n-K)) ≥ 1`: the lower-block distortion factor is a genuine loss, never a gain. -/
theorem one_le_distort {n Kv : ℕ} (h : (Kv : ℝ) < (n : ℝ)) : 1 ≤ distort n Kv := by
  have hnK : (0 : ℝ) < (n : ℝ) - (Kv : ℝ) := by linarith
  have hKv : (0 : ℝ) ≤ (Kv : ℝ) := Nat.cast_nonneg Kv
  have h1 : (1 : ℝ) ≤ (n : ℝ) / ((n : ℝ) - (Kv : ℝ)) := by
    rw [le_div_iff₀ hnK]
    linarith
  unfold distort
  calc (1 : ℝ) = Real.sqrt 1 := (Real.sqrt_one).symm
    _ ≤ Real.sqrt ((n : ℝ) / ((n : ℝ) - (Kv : ℝ))) := Real.sqrt_le_sqrt h1

theorem errDiag_nonneg {n Kv : ℕ} : 0 ≤ errDiag n Kv := by
  unfold errDiag
  positivity

/-! ## The scale `t = n^{1/6}` -/

section Scale

variable {n : ℕ}

private lemma t_pos (h : 1 ≤ n) : (0 : ℝ) < (n : ℝ) ^ ((1 : ℝ) / 6) := by
  have : (0 : ℝ) < (n : ℝ) := by exact_mod_cast h
  positivity

private lemma one_le_t (h : 1 ≤ n) : (1 : ℝ) ≤ (n : ℝ) ^ ((1 : ℝ) / 6) := by
  have h1 : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast h
  have := Real.rpow_le_rpow (x := (1 : ℝ)) (y := (n : ℝ)) (z := (1 : ℝ) / 6)
    (by norm_num) h1 (by norm_num)
  simpa using this

private lemma t_sq : ((n : ℝ) ^ ((1 : ℝ) / 6)) ^ (2 : ℕ) = (n : ℝ) ^ ((1 : ℝ) / 3) := by
  rw [← Real.rpow_natCast ((n : ℝ) ^ ((1 : ℝ) / 6)) 2,
    ← Real.rpow_mul (by positivity : (0 : ℝ) ≤ (n : ℝ))]
  norm_num

private lemma t_cube : ((n : ℝ) ^ ((1 : ℝ) / 6)) ^ (3 : ℕ) = Real.sqrt (n : ℝ) := by
  rw [← Real.rpow_natCast ((n : ℝ) ^ ((1 : ℝ) / 6)) 3,
    ← Real.rpow_mul (by positivity : (0 : ℝ) ≤ (n : ℝ)), Real.sqrt_eq_rpow]
  norm_num

end Scale

/-! ## The explicit `O(n^{-1/6})` bound on the envelope error -/

/-- **`errEnv n (K n) ≤ 5·n^{-1/6}`** for `n ≥ 27` — the paper's `o(1)` in eq:Dfinal, made
explicit.  The two contributions are the diagonal-`Φ` term (`≤ 4·n^{-1/6}`) and the lower-block
distortion (`≤ n^{-1/6}`). -/
theorem errEnv_le {n : ℕ} (hn : 27 ≤ n) :
    errEnv n (K n) ≤ 5 / (n : ℝ) ^ ((1 : ℝ) / 6) := by
  set t : ℝ := (n : ℝ) ^ ((1 : ℝ) / 6) with hts
  have hn1 : 1 ≤ n := by omega
  have ht0 : (0 : ℝ) < t := t_pos hn1
  have ht1 : (1 : ℝ) ≤ t := one_le_t hn1
  have htsq : t ^ (2 : ℕ) = (n : ℝ) ^ ((1 : ℝ) / 3) := t_sq
  have htcb : t ^ (3 : ℕ) = Real.sqrt (n : ℝ) := t_cube
  have hn0 : (0 : ℝ) < (n : ℝ) := by exact_mod_cast hn1
  have hK0 : (0 : ℝ) ≤ (K n : ℝ) := Nat.cast_nonneg _
  have hK2 : (K n : ℝ) ≤ t ^ (2 : ℕ) := by rw [htsq]; exact K_le_rpow n
  -- integer window facts
  have hKcube : K n ^ 3 ≤ n := K_pow_le n
  have hK3 : 3 ≤ K n := three_le_K hn
  have hK9 : 9 * K n ≤ n := nine_mul_K_le hn
  have hK4 : 4 * K n ≤ n := by omega
  have hK4' : 4 * (K n : ℝ) ≤ (n : ℝ) := by exact_mod_cast hK4
  ------------------------------------------------------------------
  -- Part A: the diagonal-`Φ` term
  ------------------------------------------------------------------
  have hhalf : (n : ℝ) / 2 ≤ (n : ℝ) - 2 * (K n : ℝ) + 1 := by linarith
  have hs2 : (0 : ℝ) < Real.sqrt 2 := Real.sqrt_pos.mpr (by norm_num)
  have hsn : Real.sqrt ((n : ℝ) / 2) = Real.sqrt (n : ℝ) / Real.sqrt 2 :=
    sqrt_div_eq hn0.le
  have hbig : (0 : ℝ) < Real.sqrt (n : ℝ) / Real.sqrt 2 := by
    have : (0 : ℝ) < Real.sqrt (n : ℝ) := Real.sqrt_pos.mpr hn0
    positivity
  have hden : Real.sqrt (n : ℝ) / Real.sqrt 2 ≤ Real.sqrt ((n : ℝ) - 2 * (K n : ℝ) + 1) := by
    rw [← hsn]; exact Real.sqrt_le_sqrt hhalf
  have hnum0 : (0 : ℝ) ≤ Real.sqrt 6 * (K n : ℝ) := by positivity
  have hA1 : errDiag n (K n) ≤ Real.sqrt 6 * (K n : ℝ) / (Real.sqrt (n : ℝ) / Real.sqrt 2) := by
    unfold errDiag
    rw [div_le_div_iff₀ (lt_of_lt_of_le hbig hden) hbig]
    exact mul_le_mul_of_nonneg_left hden hnum0
  have hA2 : Real.sqrt 6 * (K n : ℝ) / (Real.sqrt (n : ℝ) / Real.sqrt 2)
      = Real.sqrt 6 * Real.sqrt 2 * (K n : ℝ) / Real.sqrt (n : ℝ) := by
    have hsq : Real.sqrt (n : ℝ) ≠ 0 := ne_of_gt (Real.sqrt_pos.mpr hn0)
    field_simp
  have h6 : Real.sqrt 6 ≤ 5 / 2 := sqrt_lt_of_sq (by norm_num) (by norm_num) (by norm_num) |>.le
  have h2 : Real.sqrt 2 ≤ 3 / 2 := sqrt_lt_of_sq (by norm_num) (by norm_num) (by norm_num) |>.le
  have hc1 : Real.sqrt 6 * Real.sqrt 2 ≤ 15 / 4 := by
    nlinarith [h6, h2, Real.sqrt_nonneg 6, Real.sqrt_nonneg 2]
  have hA3 : Real.sqrt 6 * Real.sqrt 2 * (K n : ℝ) / Real.sqrt (n : ℝ) ≤ 4 / t := by
    rw [← htcb, div_le_div_iff₀ (by positivity) ht0]
    have e1 : Real.sqrt 6 * Real.sqrt 2 * (K n : ℝ) ≤ 15 / 4 * t ^ (2 : ℕ) := by
      have p1 : Real.sqrt 6 * Real.sqrt 2 * (K n : ℝ)
          ≤ Real.sqrt 6 * Real.sqrt 2 * t ^ (2 : ℕ) :=
        mul_le_mul_of_nonneg_left hK2 (by positivity)
      have p2 : Real.sqrt 6 * Real.sqrt 2 * t ^ (2 : ℕ) ≤ 15 / 4 * t ^ (2 : ℕ) :=
        mul_le_mul_of_nonneg_right hc1 (by positivity)
      linarith
    calc Real.sqrt 6 * Real.sqrt 2 * (K n : ℝ) * t
        ≤ 15 / 4 * t ^ (2 : ℕ) * t := mul_le_mul_of_nonneg_right e1 ht0.le
      _ = 15 / 4 * t ^ (3 : ℕ) := by ring
      _ ≤ 4 * t ^ (3 : ℕ) := by nlinarith [pow_pos ht0 3]
  have hA : errDiag n (K n) ≤ 4 / t := by
    calc errDiag n (K n) ≤ Real.sqrt 6 * (K n : ℝ) / (Real.sqrt (n : ℝ) / Real.sqrt 2) := hA1
      _ = Real.sqrt 6 * Real.sqrt 2 * (K n : ℝ) / Real.sqrt (n : ℝ) := hA2
      _ ≤ 4 / t := hA3
  ------------------------------------------------------------------
  -- Part B: the lower-block distortion
  ------------------------------------------------------------------
  have hnK : (0 : ℝ) < (n : ℝ) - (K n : ℝ) := by linarith
  have hsnle : Real.sqrt (n : ℝ) ≤ (n : ℝ) := by
    have h1 : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn1
    calc Real.sqrt (n : ℝ) ≤ Real.sqrt ((n : ℝ) ^ (2 : ℕ)) := Real.sqrt_le_sqrt (by nlinarith)
      _ = (n : ℝ) := Real.sqrt_sq hn0.le
  have hKt : (K n : ℝ) * t ≤ (n : ℝ) := by
    calc (K n : ℝ) * t ≤ t ^ (2 : ℕ) * t := mul_le_mul_of_nonneg_right hK2 ht0.le
      _ = t ^ (3 : ℕ) := by ring
      _ = Real.sqrt (n : ℝ) := htcb
      _ ≤ (n : ℝ) := hsnle
  have hratio : (n : ℝ) / ((n : ℝ) - (K n : ℝ)) ≤ 1 + 4 / (3 * t) := by
    rw [div_le_iff₀ hnK]
    have hKnt : (K n : ℝ) ≤ (n : ℝ) / t := by rw [le_div_iff₀ ht0]; exact hKt
    have h34 : 3 * (n : ℝ) / 4 ≤ (n : ℝ) - (K n : ℝ) := by linarith
    have hstep : 4 / (3 * t) * (3 * (n : ℝ) / 4) ≤ 4 / (3 * t) * ((n : ℝ) - (K n : ℝ)) :=
      mul_le_mul_of_nonneg_left h34 (by positivity)
    have hval : 4 / (3 * t) * (3 * (n : ℝ) / 4) = (n : ℝ) / t := by
      field_simp
    nlinarith [hstep, hval, hKnt]
  have hdist : distort n (K n) ≤ 1 + 2 / (3 * t) := by
    unfold distort
    have hsq : (n : ℝ) / ((n : ℝ) - (K n : ℝ)) ≤ (1 + 2 / (3 * t)) ^ 2 := by
      have hexp : (1 + 2 / (3 * t)) ^ 2 = 1 + 4 / (3 * t) + 4 / (9 * t ^ 2) := by
        field_simp; ring
      have hnn : (0 : ℝ) ≤ 4 / (9 * t ^ 2) := by positivity
      linarith [hratio, hexp.le, hexp.ge]
    calc Real.sqrt ((n : ℝ) / ((n : ℝ) - (K n : ℝ)))
        ≤ Real.sqrt ((1 + 2 / (3 * t)) ^ 2) := Real.sqrt_le_sqrt hsq
      _ = 1 + 2 / (3 * t) := Real.sqrt_sq (by positivity)
  have hcoef : Real.sqrt (15 / 8) * (2 * Real.sqrt 3 / 9) ≤ 1 := by
    have ha : Real.sqrt (15 / 8) ≤ 7 / 5 :=
      (sqrt_lt_of_sq (by norm_num) (by norm_num) (by norm_num)).le
    have hb : Real.sqrt 3 ≤ 9 / 5 :=
      (sqrt_lt_of_sq (by norm_num) (by norm_num) (by norm_num)).le
    nlinarith [ha, hb, Real.sqrt_nonneg (15 / 8), Real.sqrt_nonneg 3]
  have hB : Real.sqrt (15 / 8) * (2 * Real.sqrt 3 / 9) * (distort n (K n) - 1) ≤ 1 / t := by
    have hd0 : (0 : ℝ) ≤ distort n (K n) - 1 := by
      have : (K n : ℝ) < (n : ℝ) := by linarith
      linarith [one_le_distort (n := n) (Kv := K n) this]
    have hd1 : distort n (K n) - 1 ≤ 2 / (3 * t) := by linarith
    have hcnn : (0 : ℝ) ≤ Real.sqrt (15 / 8) * (2 * Real.sqrt 3 / 9) := by positivity
    calc Real.sqrt (15 / 8) * (2 * Real.sqrt 3 / 9) * (distort n (K n) - 1)
        ≤ 1 * (2 / (3 * t)) := by
          apply mul_le_mul hcoef hd1 hd0 (by norm_num)
      _ = 2 / (3 * t) := by ring
      _ ≤ 1 / t := by
          rw [div_le_div_iff₀ (by positivity : (0 : ℝ) < 3 * t) ht0]
          linarith
  ------------------------------------------------------------------
  unfold errEnv
  have : (4 : ℝ) / t + 1 / t = 5 / t := by ring
  linarith [hA, hB]

/-! ## The limits -/

/-- `n^{-r} → 0` for `r > 0`, in the `1/n^r` form the assembly uses. -/
theorem tendsto_one_div_rpow {r : ℝ} (hr : 0 < r) :
    Tendsto (fun n : ℕ => 1 / (n : ℝ) ^ r) atTop (𝓝 0) := by
  have h := (tendsto_rpow_neg_atTop hr).comp tendsto_natCast_atTop_atTop
  refine h.congr' ?_
  filter_upwards [eventually_ge_atTop 1] with n hn
  have hn0 : (0 : ℝ) ≤ (n : ℝ) := Nat.cast_nonneg n
  simp only [Function.comp_apply]
  rw [Real.rpow_neg hn0, one_div]

theorem errEnv_nonneg' {n : ℕ} (hn : 27 ≤ n) : 0 ≤ errEnv n (K n) := by
  have hKlt : (K n : ℝ) < (n : ℝ) := by
    have h9 := nine_mul_K_le hn
    have h3 := three_le_K hn
    have : K n < n := by omega
    exact_mod_cast this
  unfold errEnv
  have h1 : (0 : ℝ) ≤ errDiag n (K n) := errDiag_nonneg
  have h2 : (1 : ℝ) ≤ distort n (K n) := one_le_distort hKlt
  have hc : (0 : ℝ) ≤ Real.sqrt (15 / 8) * (2 * Real.sqrt 3 / 9) := by positivity
  have hprod := mul_nonneg hc (by linarith : (0 : ℝ) ≤ distort n (K n) - 1)
  linarith

theorem tendsto_errEnv : Tendsto (fun n : ℕ => errEnv n (K n)) atTop (𝓝 0) := by
  have hg : Tendsto (fun n : ℕ => 5 / (n : ℝ) ^ ((1 : ℝ) / 6)) atTop (𝓝 0) := by
    have h5 := (tendsto_one_div_rpow (r := (1 : ℝ) / 6) (by norm_num)).const_mul (5 : ℝ)
    rw [mul_zero] at h5
    exact h5.congr fun n => by rw [mul_one_div]
  refine squeeze_zero' (g := fun n : ℕ => 5 / (n : ℝ) ^ ((1 : ℝ) / 6)) ?_ ?_ hg
  · filter_upwards [eventually_ge_atTop 27] with n hn using errEnv_nonneg' hn
  · filter_upwards [eventually_ge_atTop 27] with n hn using errEnv_le hn

/-- **`envBound c n → 1 + M`** — the paper's eq:Dfinal, `‖D‖ ≤ 1 + M + o(1)`. -/
theorem tendsto_envBound (c : ℝ) : Tendsto (envBound c) atTop (𝓝 (1 + Mconst)) := by
  have hz : Tendsto (fun n : ℕ => c / (n : ℝ) ^ ((1 : ℝ) / 3)) atTop (𝓝 0) := by
    have h := (tendsto_one_div_rpow (r := (1 : ℝ) / 3) (by norm_num)).const_mul c
    rw [mul_zero] at h
    exact h.congr fun n => by rw [mul_one_div]
  have h1 : Tendsto (fun n : ℕ => 1 + c / (n : ℝ) ^ ((1 : ℝ) / 3)) atTop (𝓝 (1 + 0)) :=
    tendsto_const_nhds.add hz
  have h2 : Tendsto (fun n : ℕ => 1 + Mconst + errEnv n (K n)) atTop (𝓝 (1 + Mconst + 0)) :=
    tendsto_const_nhds.add tendsto_errEnv
  have h3 := h1.mul h2
  rw [show (1 + (0 : ℝ)) * (1 + Mconst + 0) = 1 + Mconst by ring] at h3
  exact h3.congr fun n => rfl

/-- `envBound c n > 0` for `n ≥ 27` and `c ≥ 0`: the denominator of Theorem B never vanishes. -/
theorem envBound_pos {c : ℝ} (hc : 0 ≤ c) {n : ℕ} (hn : 27 ≤ n) : 0 < envBound c n := by
  have h1 : (0 : ℝ) < (n : ℝ) ^ ((1 : ℝ) / 3) := by
    have : (0 : ℝ) < (n : ℝ) := by positivity
    positivity
  have h2 : 0 ≤ errEnv n (K n) := errEnv_nonneg' hn
  have h3 : 0 < Mconst := Mconst_pos
  unfold envBound
  have : (0 : ℝ) ≤ c / (n : ℝ) ^ ((1 : ℝ) / 3) := div_nonneg hc h1.le
  nlinarith

end SE
