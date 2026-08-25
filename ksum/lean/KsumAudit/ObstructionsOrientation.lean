/-
# `thm:orientation-obstruction` — Orientation coherence for identical common-total blocks

LaTeX: `ksum/paper/ksum_small_alphabet.tex`, label `thm:orientation-obstruction`,
line 1063, displayed bound (51).
DAG node: `KSUM.B4b.L2.ORIENT` (`ksum/proof-dag/nodes/KSUM.B4b.L2.ORIENT.yaml`, PROVED).

## The quantifier structure the LaTeX asserts (written out BEFORE formalizing)

∀ `q = 2r+1 ≥ 5`, ∀ `m ≥ 2`, ∀ `s ≥ 2`: for the SPECIFIC construction — every one of the `m`
positional blocks carries the same tilted pair construction of `thm:tilted-log-band` modified to
fixed-point occupancy zero, the same exact pair total `s` on every nonfixed pair, raw product
tensor, `S_N`-average with `N = mrs`, normalized by the actual post-average `ℓ¹` norm —

  (a) true NO incurs the EXACT orientation-coherence factor `2^{-r(m-1)}`, and
  (b) the normalized correlation is at most `1/2`
      (via `corr ≤ 2^{r+1-m(r+1)} |A_s|^{-rm}`, which is `≤ 1/8` for even `s` and `≤ 1/2` for
      odd `s`).

Unlike `thm:product-obstruction`, this is NOT a statement about a whole family: the measure is a
single named construction, quantified only over `(q, m, s)`.

## SCOPE OF THIS FORMALIZATION — read with the artifact

Two of the three ingredients are formalized here at full strength:

  * `orientation_coherence_factor` — clause (a).  The exact combinatorial factor.  "True NO
    requires … independently for each pair, all `m` uniform endpoint orientations to agree";
    that event has probability exactly `2^{-r(m-1)}`.
  * `orientation_bound_even` / `orientation_bound_odd_sq` / `orientation_corr_le_half` —
    the arithmetic of clause (b): given the paper's displayed bound (51) and its two cases for
    `|A_s|`, the numeric conclusions `≤ 1/8` and `≤ 1/2` follow, for ALL `r ≥ 2`, `m ≥ 2`.

**Gap-closure batch 2 (item H-2, 2026-08-01) closes the analytic step.**  What used to be
"NOT formalized — the analytic norm lower bound that PRODUCES (51)" is now proved, in four pieces:

  * `endpoint_even` / `endpoint_odd` — the phase choice.  At `θ = π/s` (even `s ≥ 2`) the axis
    value `A_s = cos(sθ)` is `-1` and the interior value `I_s = 1`, so `I_s = -A_s` and
    `|A_s| = 1`; at `θ = π/(s+1)` (odd `s ≥ 3`) one has `A_s = -cos θ`, `I_s = cos θ`, so again
    `I_s = -A_s`, and `|A_s| = cos(π/(s+1)) ≥ √2/2`, i.e. `A_s² ≥ 1/2`.
  * `blockFourier_eq` — the one-block Fourier modulus.  *"If `W_0` is the all-axis outer weight
    and `ρ = 2|W_0|`, the positive support nodes are odd and `∑_k W_k = 0, whence the one-block
    Fourier modulus is `ρ|A_s|^r`."*  Proved as an exact identity, `2W_0·A^r`.
  * `abs_pairing_le_l1` — the triangle inequality: pairing a signed measure against a
    modulus-one function is bounded by its `ℓ¹` norm.  This is what makes the bound survive the
    (possibly norm-reducing) `S_N` average: the phase evaluation is `S_N`-invariant.
  * `orientation_corr_le_half_even` / `_odd` — (51) assembled, in both of the paper's cases,
    giving `≤ 1/8` and `≤ 1/2` for all `r ≥ 2`, `m ≥ 2`.

STILL an explicit hypothesis, not formalized: that the *named construction*'s occupancy
generating polynomial IS this `φ` and that its `m`-fold convolution has one-block value
`2W_0·A^r` — the same modelling step the fidelity review already recorded as the (second-order)
narrowing on clause (a).  The measure on `ℤ_q^N` itself is `thm:pair-tensor` /
`thm:tilted-log-band` territory (see `ObstructionsTiltedBand`).
-/
import KsumAudit.ObstructionsCore
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.Complex.Norm

namespace KsumAudit.Obstructions.Orientation

open Finset KsumAudit.Obstructions

set_option linter.unusedSectionVars false

/-! ## Clause (a): the exact orientation-coherence factor `2^{-r(m-1)}` -/

/-- The coherent-orientation event for ONE pair: all `m` blocks pick the same endpoint
orientation of that pair. -/
def coherent (m : ℕ) : Finset (Fin m → Bool) :=
  univ.filter (fun w => ∀ i j, w i = w j)

/-- For `m ≥ 1` exactly two of the `2^m` orientation patterns on a pair are coherent. -/
lemma card_coherent {m : ℕ} (hm : 1 ≤ m) : (coherent m).card = 2 := by
  classical
  have hset : coherent m = {(fun _ => false), (fun _ => true)} := by
    ext w
    simp only [coherent, Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_insert,
      Finset.mem_singleton]
    constructor
    · intro h
      cases hw : w ⟨0, by omega⟩ with
      | false => exact Or.inl (funext fun i => by rw [h i ⟨0, by omega⟩, hw])
      | true => exact Or.inr (funext fun i => by rw [h i ⟨0, by omega⟩, hw])
    · rintro (rfl | rfl) <;> intro i j <;> rfl
  rw [hset]
  rw [Finset.card_insert_of_notMem (by
    simp only [Finset.mem_singleton]
    intro hc
    have := congrFun hc ⟨0, by omega⟩
    simp at this), Finset.card_singleton]

/-- **`thm:orientation-obstruction`, clause (a): the exact orientation-coherence factor.**

For `r` pairs each carrying `m` independent uniform endpoint orientations, the probability that
all `m` orientations agree on EVERY pair is exactly `2^{-r(m-1)}`. -/
theorem orientation_coherence_factor (r m : ℕ) (hm : 1 ≤ m) :
    ((Fintype.piFinset (fun _ : Fin r => coherent m)).card : ℚ) / ((2:ℚ) ^ (r * m))
      = 2 ^ (-((r : ℤ) * ((m : ℤ) - 1))) := by
  classical
  have hcard : (Fintype.piFinset (fun _ : Fin r => coherent m)).card = 2 ^ r := by
    rw [Fintype.card_piFinset]
    simp [card_coherent hm]
  rw [hcard]
  push_cast
  rw [div_eq_iff (by positivity), ← zpow_natCast (2:ℚ) r, ← zpow_natCast (2:ℚ) (r * m),
    ← zpow_add₀ (by norm_num : (2:ℚ) ≠ 0)]
  congr 1
  push_cast
  ring

/-- The number of orientation patterns on `r` pairs and `m` blocks is `2^{rm}`; the coherent
ones number `2^r`.  (Stated separately so the ratio above is auditable.) -/
theorem orientation_counts (r m : ℕ) (hm : 1 ≤ m) :
    (Fintype.piFinset (fun _ : Fin r => coherent m)).card = 2 ^ r
      ∧ (Fintype.piFinset (fun _ : Fin r => (univ : Finset (Fin m → Bool)))).card
          = 2 ^ (r * m) := by
  constructor
  · rw [Fintype.card_piFinset]; simp [card_coherent hm]
  · have hu : (univ : Finset (Fin m → Bool)).card = 2 ^ m := by simp
    rw [Fintype.card_piFinset]
    simp only [hu, Finset.prod_const, Finset.card_univ, Fintype.card_fin]
    rw [← pow_mul, Nat.mul_comm m r]

/-! ## Clause (b): the numeric conclusion of the displayed bound (51)

`corr ≤ 2^{r+1-m(r+1)} |A_s|^{-rm}` with `|A_s| = 1` for even `s` and `|A_s| ≥ 2^{-1/2}` for
odd `s`.  Both cases are treated for ALL `r ≥ 2` (i.e. `q ≥ 5`) and ALL `m ≥ 2`. -/

/-- Even `s`: `|A_s| = 1`, so the bound is `2^{r+1-m(r+1)} ≤ 1/8`. -/
theorem orientation_bound_even (r m : ℕ) (hr : 2 ≤ r) (hm : 2 ≤ m) :
    (2:ℚ) ^ ((r : ℤ) + 1 - (m : ℤ) * ((r : ℤ) + 1)) ≤ 1/8 := by
  have hR : (2 : ℤ) ≤ (r : ℤ) := by exact_mod_cast hr
  have hM : (2 : ℤ) ≤ (m : ℤ) := by exact_mod_cast hm
  have hexp : (r : ℤ) + 1 - (m : ℤ) * ((r : ℤ) + 1) ≤ -3 := by nlinarith
  calc (2:ℚ) ^ ((r : ℤ) + 1 - (m : ℤ) * ((r : ℤ) + 1)) ≤ 2 ^ (-3 : ℤ) :=
        zpow_le_zpow_right₀ (by norm_num) hexp
    _ = 1/8 := by norm_num

/-- Odd `s`: `|A_s| ≥ 2^{-1/2}`, hence `|A_s|^{-rm} ≤ 2^{rm/2}`.  Stated in SQUARED form so the
half-integer exponent never leaves `ℚ`: `(2^{r+1-m(r+1)} · 2^{rm/2})^2 = 2^{2(r+1-m(r+1))+rm}`. -/
theorem orientation_bound_odd_sq (r m : ℕ) (hr : 2 ≤ r) (hm : 2 ≤ m) :
    (2:ℚ) ^ (2 * ((r : ℤ) + 1 - (m : ℤ) * ((r : ℤ) + 1)) + (r : ℤ) * (m : ℤ)) ≤ 1/4 := by
  have hR : (2 : ℤ) ≤ (r : ℤ) := by exact_mod_cast hr
  have hM : (2 : ℤ) ≤ (m : ℤ) := by exact_mod_cast hm
  have hexp : 2 * ((r : ℤ) + 1 - (m : ℤ) * ((r : ℤ) + 1)) + (r : ℤ) * (m : ℤ) ≤ -2 := by
    nlinarith
  calc (2:ℚ) ^ (2 * ((r : ℤ) + 1 - (m : ℤ) * ((r : ℤ) + 1)) + (r : ℤ) * (m : ℤ))
      ≤ 2 ^ (-2 : ℤ) := zpow_le_zpow_right₀ (by norm_num) hexp
    _ = 1/4 := by norm_num

/-- Squared form to value form: a nonnegative correlation with `c² ≤ 1/4` is `≤ 1/2`. -/
theorem orientation_corr_le_half {c : ℚ} (hc : 0 ≤ c) (h : c ^ 2 ≤ 1/4) : c ≤ 1/2 := by
  nlinarith

/-- **`thm:orientation-obstruction`, clause (b), assembled.**
Given the paper's displayed bound (51) in either of its two cases, the normalized correlation is
at most `1/2` (indeed at most `1/8` in the even case) whenever `q = 2r+1 ≥ 5` and `m ≥ 2`. -/
theorem orientation_obstruction_half (r m : ℕ) (hr : 2 ≤ r) (hm : 2 ≤ m) (c : ℚ) (hc : 0 ≤ c)
    (hbound : c ≤ (2:ℚ) ^ ((r : ℤ) + 1 - (m : ℤ) * ((r : ℤ) + 1))
      ∨ c ^ 2 ≤ (2:ℚ) ^ (2 * ((r : ℤ) + 1 - (m : ℤ) * ((r : ℤ) + 1)) + (r : ℤ) * (m : ℤ))) :
    c ≤ 1/2 := by
  rcases hbound with h | h
  · have := orientation_bound_even r m hr hm
    linarith
  · exact orientation_corr_le_half hc (le_trans h (orientation_bound_odd_sq r m hr hm))

/-! ## The analytic step that PRODUCES (51)  (gap-closure batch 2, item H-2)

The paper: *"For the norm lower bound, evaluate the occupancy generating polynomial on endpoint
phases `(e^{iθ},e^{-iθ})`.  On one pair the axis value is `A_s = cos(sθ)`, while the interior
value is `I_s = 1` for even `s` and `I_s = cos θ` for odd `s`.  Taking `θ = π/s` for even `s` and
`θ = π/(s+1)` for odd `s` gives `I_s = -A_s`, with `|A_s| = 1` in the even case and
`|A_s| ≥ 2^{-1/2}` in the odd case."* -/

section Phases

open Real

/-- The axis value on one pair at endpoint phase `θ`: `A_s = cos(sθ)`. -/
noncomputable def axisVal (s : ℕ) (θ : ℝ) : ℝ := Real.cos (s * θ)

/-- The interior value on one pair at endpoint phase `θ`: `I_s = 1` for even `s`,
`I_s = cos θ` for odd `s`. -/
noncomputable def intVal (s : ℕ) (θ : ℝ) : ℝ := if Even s then 1 else Real.cos θ

/-- **Even `s`, `θ = π/s`:** `I_s = -A_s` and `|A_s| = 1`. -/
theorem endpoint_even {s : ℕ} (hs : 2 ≤ s) (he : Even s) :
    intVal s (π / s) = -axisVal s (π / s) ∧ |axisVal s (π / s)| = 1 := by
  have hs0 : (s : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
  have hA : axisVal s (π / s) = -1 := by
    rw [axisVal, mul_div_cancel₀ _ hs0, Real.cos_pi]
  refine ⟨?_, ?_⟩
  · rw [intVal, if_pos he, hA]; norm_num
  · rw [hA]; norm_num

/-- **Odd `s ≥ 3`, `θ = π/(s+1)`:** `I_s = -A_s`, and `A_s² ≥ 1/2` (the paper's
`|A_s| ≥ 2^{-1/2}`).  `s ≥ 3` is exactly what puts `θ = π/(s+1)` inside `[0, π/4]`. -/
theorem endpoint_odd {s : ℕ} (hs : 3 ≤ s) (ho : ¬ Even s) :
    intVal s (π / (s + 1)) = -axisVal s (π / (s + 1))
      ∧ 1 / 2 ≤ (axisVal s (π / (s + 1))) ^ 2 := by
  have hs1 : ((s : ℝ) + 1) ≠ 0 := by positivity
  have hkey : (s : ℝ) * (π / (s + 1)) = π - π / (s + 1) := by
    field_simp
    ring
  have hA : axisVal s (π / (s + 1)) = -Real.cos (π / (s + 1)) := by
    rw [axisVal, hkey, Real.cos_pi_sub]
  have hθ0 : 0 ≤ π / ((s : ℝ) + 1) := by positivity
  have hθ4 : π / ((s : ℝ) + 1) ≤ π / 4 := by
    have h4 : (4:ℝ) ≤ (s : ℝ) + 1 := by
      have : (3:ℝ) ≤ (s : ℝ) := by exact_mod_cast hs
      linarith
    have hπ := Real.pi_pos
    rw [div_le_div_iff₀ (by linarith) (by norm_num)]
    nlinarith
  have hcos : Real.sqrt 2 / 2 ≤ Real.cos (π / ((s : ℝ) + 1)) := by
    rw [← Real.cos_pi_div_four]
    exact Real.cos_le_cos_of_nonneg_of_le_pi hθ0 (by linarith [Real.pi_pos]) hθ4
  have hsq : Real.sqrt 2 * Real.sqrt 2 = 2 := Real.mul_self_sqrt (by norm_num)
  refine ⟨by rw [intVal, if_neg ho, hA]; ring, ?_⟩
  rw [hA]
  nlinarith [hcos, Real.sqrt_nonneg 2, hsq]

end Phases

/-! ### The one-block Fourier modulus -/

/-- The one-block Fourier value: a configuration in activity layer `k` contributes
`A^{r-k}·I^k`, and layer `k` carries total outer weight `W k`. -/
def blockFourier (r : ℕ) (A I : ℝ) (T : Finset ℕ) (W : ℕ → ℝ) : ℝ :=
  ∑ k ∈ T, W k * (A ^ (r - k) * I ^ k)

/-- **The paper's one-block Fourier modulus, as an exact identity.**
*"If `W_0` is the all-axis outer weight and `ρ = 2|W_0|`, the positive support nodes are odd and
`∑_k W_k = 0`, whence the one-block Fourier modulus is `ρ|A_s|^r`."*

With `I = -A` (the endpoint phase choice), every layer contributes `(-1)^k A^r`, the odd layers
cancel against `∑_k W_k = 0`, and the value is exactly `2W_0·A^r`. -/
theorem blockFourier_eq (r : ℕ) (A : ℝ) (T : Finset ℕ) (W : ℕ → ℝ)
    (h0 : 0 ∈ T) (hle : ∀ k ∈ T, k ≤ r) (hodd : ∀ k ∈ T, k ≠ 0 → Odd k)
    (hsum : ∑ k ∈ T, W k = 0) :
    blockFourier r A (-A) T W = 2 * W 0 * A ^ r := by
  classical
  have hterm : ∀ k ∈ T, W k * (A ^ (r - k) * (-A) ^ k) = W k * ((-1) ^ k * A ^ r) := by
    intro k hk
    have hpow : A ^ (r - k) * A ^ k = A ^ r := by
      rw [← pow_add, Nat.sub_add_cancel (hle k hk)]
    rw [neg_pow]
    calc W k * (A ^ (r - k) * ((-1) ^ k * A ^ k))
        = W k * ((-1) ^ k * (A ^ (r - k) * A ^ k)) := by ring
      _ = W k * ((-1) ^ k * A ^ r) := by rw [hpow]
  rw [blockFourier, Finset.sum_congr rfl hterm]
  have hsplit : ∑ k ∈ T, W k * ((-1:ℝ) ^ k * A ^ r)
      = W 0 * ((-1:ℝ) ^ (0:ℕ) * A ^ r)
        + ∑ k ∈ T.erase 0, W k * ((-1:ℝ) ^ k * A ^ r) :=
    (Finset.add_sum_erase T (fun k => W k * ((-1:ℝ) ^ k * A ^ r)) h0).symm
  have herase : ∑ k ∈ T.erase 0, W k * ((-1:ℝ) ^ k * A ^ r)
      = -((∑ k ∈ T.erase 0, W k) * A ^ r) := by
    rw [Finset.sum_mul, ← Finset.sum_neg_distrib]
    refine Finset.sum_congr rfl fun k hk => ?_
    have hk0 : k ≠ 0 := (Finset.mem_erase.mp hk).1
    have hoddk := hodd k (Finset.mem_erase.mp hk).2 hk0
    rw [hoddk.neg_one_pow]
    ring
  have hsum0 : ∑ k ∈ T.erase 0, W k = -W 0 := by
    have := Finset.add_sum_erase T W h0
    linarith [this.trans hsum]
  rw [hsplit, herase, hsum0]
  ring

/-! ### The triangle inequality that survives the `S_N` average -/

/-- **The paper's *"the triangle inequality lower-bounds the post-average norm"*.**
Pairing a signed measure against a function of modulus one is bounded by its `ℓ¹` norm.  This is
the step that makes the lower bound immune to the `S_N` average: the average may reduce the norm,
but it leaves the (invariant) phase evaluation untouched. -/
theorem abs_pairing_le_l1 {X : Type*} [Fintype X] (p : X → ℝ) (φ : X → ℂ)
    (hφ : ∀ x, ‖φ x‖ = 1) :
    ‖∑ x, (p x : ℂ) * φ x‖ ≤ ∑ x, |p x| := by
  calc ‖∑ x, (p x : ℂ) * φ x‖ ≤ ∑ x, ‖(p x : ℂ) * φ x‖ := norm_sum_le _ _
    _ = ∑ x, |p x| := by
        refine Finset.sum_congr rfl fun x _ => ?_
        rw [norm_mul, hφ x, mul_one, Complex.norm_real, Real.norm_eq_abs]

/-- The post-average `ℓ¹` norm is at least `ρ^m|A|^{rm}`, `ρ = 2|W₀|`: the triangle inequality
applied to the `m`-fold convolution's phase evaluation `(2W₀A^r)^m`. -/
theorem l1_ge_fourier {X : Type*} [Fintype X] (p : X → ℝ) (φ : X → ℂ)
    (hφ : ∀ x, ‖φ x‖ = 1) (r m : ℕ) (A W₀ : ℝ)
    (hfourier : ∑ x, (p x : ℂ) * φ x = (((2 * W₀ * A ^ r) ^ m : ℝ) : ℂ)) :
    (2 * |W₀|) ^ m * |A| ^ (r * m) ≤ ∑ x, |p x| := by
  have h := abs_pairing_le_l1 p φ hφ
  rw [hfourier, Complex.norm_real, Real.norm_eq_abs] at h
  have hbase : |2 * W₀ * A ^ r| = 2 * |W₀| * |A| ^ r := by
    rw [abs_mul, abs_mul, abs_pow]
    norm_num
  have hval : |(2 * W₀ * A ^ r) ^ m| = (2 * |W₀|) ^ m * |A| ^ (r * m) := by
    rw [abs_pow, hbase, mul_pow, ← pow_mul]
  rw [hval] at h
  exact h

/-! ### (51) assembled, in the paper's two cases -/

/-- Squares commute with natural powers: `(x^n)^2 = (x^2)^n`. -/
private lemma sq_pow_comm (x : ℝ) (n : ℕ) : (x ^ n) ^ 2 = (x ^ 2) ^ n := by
  rw [← pow_mul, ← pow_mul, Nat.mul_comm]

/-- **`thm:orientation-obstruction` clause (b), even `s`: `corr ≤ 1/8`, DERIVED.**

`num` is the exact NO numerator of clause (a), written without any negative exponent as
`num·2^{r(m-1)} = 2|W₀|^m`; `Z` is the post-average `ℓ¹` norm, bounded below by `l1_ge_fourier`
with `|A_s| = 1` (`endpoint_even`).  Then `corr = num/Z ≤ 2^{1-m-r(m-1)} ≤ 1/8`, for all
`r ≥ 2` (i.e. `q ≥ 5`) and all `m ≥ 2`. -/
theorem orientation_corr_le_half_even {r m : ℕ} (hr : 2 ≤ r) (hm : 2 ≤ m)
    {W₀ Z num : ℝ} (hW : W₀ ≠ 0)
    (hZ : (2 * |W₀|) ^ m * 1 ≤ Z)
    (hnum : num * 2 ^ (r * (m - 1)) = 2 * |W₀| ^ m) :
    num / Z ≤ 1 / 8 := by
  have hW0 : (0:ℝ) < |W₀| := abs_pos.mpr hW
  have hWm : (0:ℝ) < |W₀| ^ m := pow_pos hW0 m
  have hp : (0:ℝ) < 2 ^ (r * (m - 1)) := by positivity
  have hnum_pos : 0 < num := by
    by_contra hc
    push Not at hc
    nlinarith
  have hZeq : (2 * |W₀|) ^ m * 1 = 2 ^ m * |W₀| ^ m := by rw [mul_pow]; ring
  have hZpos : (0:ℝ) < Z := by
    refine lt_of_lt_of_le ?_ hZ
    rw [hZeq]; positivity
  have h4p : (4:ℝ) ≤ 2 ^ (r * (m - 1)) := by
    have hexp2 : 2 ≤ r * (m - 1) := by
      have h1 : 1 ≤ m - 1 := by omega
      have := Nat.mul_le_mul hr h1
      simpa using this
    have : (2:ℝ) ^ 2 ≤ 2 ^ (r * (m - 1)) := pow_le_pow_right₀ (by norm_num) hexp2
    linarith [this]
  have h4m : (4:ℝ) ≤ 2 ^ m := by
    have : (2:ℝ) ^ 2 ≤ 2 ^ m := pow_le_pow_right₀ (by norm_num) hm
    linarith [this]
  rw [div_le_div_iff₀ hZpos (by norm_num)]
  have hZ' : 2 ^ m * |W₀| ^ m ≤ Z := by rw [← hZeq]; exact hZ
  nlinarith [hnum, hZ', hWm, hp, h4p, h4m]

/-- **`thm:orientation-obstruction` clause (b), odd `s`: `corr ≤ 1/2`, DERIVED.**

Same as the even case but with `A² ≥ 1/2` (`endpoint_odd`) instead of `|A| = 1`.  The key bound
`2^{r(m-1)+m}|A|^{rm} ≥ 4` is obtained in SQUARED form so that no half-integer exponent ever
appears, exactly as `orientation_bound_odd_sq` does; the arithmetic that makes it work is
`rm + 4 ≤ 2r(m-1) + 2m`, i.e. `(r+2)(m-2) ≥ 0`.

`r ≥ 2` is carried as a hypothesis for scope alignment with the paper's `q = 2r+1 ≥ 5`; the
odd-case arithmetic in fact holds for every `r`, so this theorem is (harmlessly) stronger than
the displayed clause on that axis. -/
theorem orientation_corr_le_half_odd {r m : ℕ} (_hr : 2 ≤ r) (hm : 2 ≤ m)
    {A W₀ Z num : ℝ} (hW : W₀ ≠ 0) (hA : 1 / 2 ≤ A ^ 2)
    (hZ : (2 * |W₀|) ^ m * |A| ^ (r * m) ≤ Z)
    (hnum : num * 2 ^ (r * (m - 1)) = 2 * |W₀| ^ m) :
    num / Z ≤ 1 / 2 := by
  have hW0 : (0:ℝ) < |W₀| := abs_pos.mpr hW
  have hWm : (0:ℝ) < |W₀| ^ m := pow_pos hW0 m
  have hApos : (0:ℝ) < |A| := by
    rcases eq_or_ne A 0 with rfl | hne
    · exfalso; rw [show (0:ℝ) ^ 2 = 0 by ring] at hA; linarith
    · exact abs_pos.mpr hne
  have hp : (0:ℝ) < 2 ^ (r * (m - 1)) := by positivity
  have hnum_pos : 0 < num := by
    by_contra hc
    push Not at hc
    nlinarith
  have hZeq : (2 * |W₀|) ^ m * |A| ^ (r * m) = |W₀| ^ m * (2 ^ m * |A| ^ (r * m)) := by
    rw [mul_pow]; ring
  have hZpos : (0:ℝ) < Z := by
    refine lt_of_lt_of_le ?_ hZ
    rw [hZeq]; positivity
  -- the key product bound `2^{r(m-1)} · 2^m · |A|^{rm} ≥ 4`, proved through its square
  have hkey : (4:ℝ) ≤ 2 ^ (r * (m - 1)) * (2 ^ m * |A| ^ (r * m)) := by
    set P : ℝ := 2 ^ (r * (m - 1)) * (2 ^ m * |A| ^ (r * m)) with hP
    have hPpos : (0:ℝ) < P := by rw [hP]; positivity
    have hexp : r * m + 4 ≤ 2 * (r * (m - 1)) + 2 * m := by
      obtain ⟨m', rfl⟩ : ∃ m', m = m' + 2 := ⟨m - 2, by omega⟩
      have hsub : m' + 2 - 1 = m' + 1 := by omega
      rw [hsub]
      nlinarith
    have hpow2 : (2:ℝ) ^ (r * m + 4) ≤ 2 ^ (2 * (r * (m - 1)) + 2 * m) :=
      pow_le_pow_right₀ (by norm_num) hexp
    have hAsq : (1 / 2 : ℝ) ^ (r * m) ≤ (|A| ^ 2) ^ (r * m) :=
      pow_le_pow_left₀ (by norm_num) (by rw [sq_abs]; exact hA) _
    have hPsq : P ^ 2 = 2 ^ (2 * (r * (m - 1)) + 2 * m) * (|A| ^ 2) ^ (r * m) := by
      have e1 : ((2:ℝ) ^ (r * (m - 1))) ^ 2 = 2 ^ (2 * (r * (m - 1))) := by
        rw [← pow_mul, Nat.mul_comm]
      have e2 : ((2:ℝ) ^ m) ^ 2 = 2 ^ (2 * m) := by rw [← pow_mul, Nat.mul_comm]
      have e3 : (|A| ^ (r * m)) ^ 2 = (|A| ^ 2) ^ (r * m) := sq_pow_comm _ _
      rw [hP, mul_pow, mul_pow, e1, e2, e3, pow_add]
      ring
    have h16 : (16:ℝ) = 2 ^ (r * m + 4) * (1 / 2 : ℝ) ^ (r * m) := by
      have hinv : (1 / 2 : ℝ) ^ (r * m) = ((2:ℝ) ^ (r * m))⁻¹ := by rw [one_div, inv_pow]
      have h2 : (0:ℝ) < (2:ℝ) ^ (r * m) := by positivity
      rw [hinv, pow_add]
      field_simp
      norm_num
    have hsq : (16:ℝ) ≤ P ^ 2 := by
      rw [hPsq, h16]
      exact mul_le_mul hpow2 hAsq (by positivity) (by positivity)
    nlinarith [hsq, hPpos]
  rw [div_le_div_iff₀ hZpos (by norm_num)]
  have hZ' : |W₀| ^ m * (2 ^ m * |A| ^ (r * m)) ≤ Z := by rw [← hZeq]; exact hZ
  nlinarith [hnum, hZ', hWm, hp, hkey]

/-! ## Non-vacuity witnesses -/

/-- The smallest instance the theorem covers: `q = 5` (`r = 2`), `m = 2`.  The coherence factor
is `2^{-2} = 1/4` and the even-`s` bound is exactly `1/8`. -/
example : ((Fintype.piFinset (fun _ : Fin 2 => coherent 2)).card : ℚ) / ((2:ℚ) ^ (2 * 2))
    = 1/4 := by
  rw [orientation_coherence_factor 2 2 (by norm_num)]
  norm_num

example : (coherent 2).card = 2 := card_coherent (by norm_num)

example : (2:ℚ) ^ ((2 : ℤ) + 1 - (2 : ℤ) * ((2 : ℤ) + 1)) = 1/8 := by norm_num

/-! ### Witnesses for the analytic step (gap-closure batch 2) -/

/-- `endpoint_even` at the smallest even total `s = 2`: `θ = π/2`, `A_2 = cos π = -1`,
`I_2 = 1 = -A_2`. -/
example : axisVal 2 (Real.pi / 2) = -1 ∧ intVal 2 (Real.pi / 2) = 1 := by
  have h := endpoint_even (s := 2) (by norm_num) (by decide)
  refine ⟨?_, ?_⟩
  · have := h.2
    rw [abs_eq (by norm_num : (0:ℝ) ≤ 1)] at this
    rcases this with hh | hh
    · exfalso
      have hI := h.1
      rw [intVal, if_pos (by decide : Even 2), hh] at hI
      norm_num at hI
    · simpa using hh
  · rw [intVal, if_pos (by decide : Even 2)]

/-- `endpoint_odd` at the smallest odd total `s = 3`: `θ = π/4`, `A_3 = -√2/2`,
`I_3 = √2/2 = -A_3`, and `A_3² = 1/2` — the `≥ 1/2` bound is TIGHT at `s = 3`. -/
example : (axisVal 3 (Real.pi / 4)) ^ 2 = 1 / 2 := by
  have hkey : ((3:ℕ) : ℝ) * (Real.pi / 4) = Real.pi - Real.pi / 4 := by push_cast; ring
  rw [axisVal, hkey, Real.cos_pi_sub, Real.cos_pi_div_four]
  have hsq : Real.sqrt 2 * Real.sqrt 2 = 2 := Real.mul_self_sqrt (by norm_num)
  nlinarith [hsq]

/-- `blockFourier_eq` is not vacuous: the two-node support `T = {0,1}` with
`W_0 = -1/2`, `W_1 = 1/2` (unit `ℓ¹`, zero total, the nonzero node odd), `r = 2`, gives the
one-block value `2W_0A² = -A²`. -/
example (A : ℝ) : blockFourier 2 A (-A) ({0, 1} : Finset ℕ) (fun k => if k = 0 then -(1/2) else 1/2)
    = 2 * (-(1/2)) * A ^ 2 := by
  refine blockFourier_eq 2 A ({0, 1} : Finset ℕ) _ (by decide) (fun k hk => by
      fin_cases hk <;> norm_num) (fun k hk hk0 => by
      fin_cases hk
      · exact absurd rfl hk0
      · exact ⟨0, by norm_num⟩) ?_
  rw [Finset.sum_pair (by norm_num : (0:ℕ) ≠ 1)]
  norm_num

/-- `l1_ge_fourier` is not vacuous, and TIGHT: one configuration, `p = 1`, `φ = 1`, `r = m = 1`,
`A = 1`, `W₀ = 1/2` gives `(2|W₀|)^m|A|^{rm} = 1 = ∑|p|`. -/
example : (2 * |(1/2 : ℝ)|) ^ 1 * |(1:ℝ)| ^ (1 * 1) ≤ ∑ _x : Fin 1, |(1:ℝ)| := by
  refine l1_ge_fourier (fun _ : Fin 1 => (1:ℝ)) (fun _ => 1) (fun _ => by norm_num) 1 1 1 (1/2) ?_
  norm_num

/-- `orientation_corr_le_half_even` is TIGHT at `r = m = 2`: `W₀ = 1/2`, `Z = 1`,
`num = 1/8` gives exactly `1/8`. -/
example : (1/8 : ℝ) / 1 ≤ 1 / 8 :=
  orientation_corr_le_half_even (r := 2) (m := 2) (by norm_num) (by norm_num)
    (W₀ := 1/2) (by norm_num) (by norm_num) (by norm_num)

/-- `orientation_corr_le_half_odd` is not vacuous at `r = m = 2` with the tight `A² = 1/2`:
`|A|^{rm} = |A|^4 = 1/4`, `Z = (2·(1/2))²·(1/4) = 1/4`, `num = 1/8`, so `corr = 1/2` exactly. -/
example : (1/8 : ℝ) / (1/4) ≤ 1 / 2 := by
  have hA : |Real.sqrt 2 / 2| = Real.sqrt 2 / 2 :=
    abs_of_nonneg (by positivity)
  have hsq : Real.sqrt 2 * Real.sqrt 2 = 2 := Real.mul_self_sqrt (by norm_num)
  refine orientation_corr_le_half_odd (r := 2) (m := 2) (by norm_num) (by norm_num)
    (A := Real.sqrt 2 / 2) (W₀ := 1/2) (by norm_num) (by nlinarith [hsq]) ?_ (by norm_num)
  rw [hA]
  have h4 : (Real.sqrt 2 / 2) ^ (2 * 2) = 1 / 4 := by
    have : (Real.sqrt 2 / 2) ^ 2 = 1 / 2 := by nlinarith [hsq]
    calc (Real.sqrt 2 / 2) ^ (2 * 2) = ((Real.sqrt 2 / 2) ^ 2) ^ 2 := by rw [pow_mul]
      _ = 1 / 4 := by rw [this]; norm_num
  rw [h4]
  norm_num

#print axioms card_coherent
#print axioms orientation_coherence_factor
#print axioms orientation_counts
#print axioms orientation_bound_even
#print axioms orientation_bound_odd_sq
#print axioms orientation_obstruction_half
#print axioms endpoint_even
#print axioms endpoint_odd
#print axioms blockFourier_eq
#print axioms abs_pairing_le_l1
#print axioms l1_ge_fourier
#print axioms orientation_corr_le_half_even
#print axioms orientation_corr_le_half_odd

end KsumAudit.Obstructions.Orientation
