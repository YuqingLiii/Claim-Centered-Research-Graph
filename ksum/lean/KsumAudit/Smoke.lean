/-
Gate G-L1 smoke test: confirm that the Mathlib substrate the k-Sum audit actually needs
is present and usable in this build environment.

The three imports below are exactly the three pillars of Tier 1:
  * `ZMod q` arithmetic with a `q`-dependent characteristic  (the encoding lemma),
  * `Finset` existential/counting reasoning                   (hits, orbits, pigeonhole),
  * `Real.rpow` with fractional exponents                     (the `q^(1/6)` bookkeeping).

Nothing here is mathematical content of the paper; it is an environment probe.
-/
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Finset.Card
import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace KsumAudit.Smoke

/-- `ZMod` substrate, natural form: a value strictly inside the window `(0, q)` does not
vanish mod `q`.  This is the "within the first half" case of the encoding lemma. -/
example (q a : ℕ) (ha : 0 < a) (ha' : a < q) : (a : ZMod q) ≠ 0 := by
  rw [Ne, ZMod.natCast_eq_zero_iff]
  exact Nat.not_dvd_of_pos_of_lt ha ha'

/-- `ZMod` substrate, integer form: this is the shape the cross-half case needs, where the
difference `f i - g j` lives in `[-(κ-1), κ-1]` and vanishes mod `q` iff it is `0`. -/
example (q : ℕ) (a : ℤ) (h₁ : -(q : ℤ) < a) (h₂ : a < q) : (a : ZMod q) = 0 ↔ a = 0 := by
  rw [ZMod.intCast_zmod_eq_zero_iff_dvd]
  constructor
  · intro h; rcases h with ⟨c, rfl⟩; rcases eq_or_ne c 0 with rfl | hc
    · ring
    · exfalso
      rcases lt_or_gt_of_ne hc with hc' | hc'
      · nlinarith [Int.add_one_le_iff.mpr hc', (by positivity : (0:ℤ) ≤ (q:ℤ))]
      · nlinarith [Int.add_one_le_iff.mpr (by omega : (0:ℤ) < c), (by positivity : (0:ℤ) ≤ (q:ℤ))]
  · rintro rfl; exact dvd_zero _

/-- `Finset` substrate: pigeonhole in the exact form used by the orthogonal-array barrier
(`q < N` forces a repeat, hence element distinctness is identically true). -/
example {N q : ℕ} (f : Fin N → Fin q) (h : q < N) : ∃ i j, i ≠ j ∧ f i = f j := by
  have : ¬ Function.Injective f := by
    intro hinj
    have := Fintype.card_le_of_injective f hinj
    simp only [Fintype.card_fin] at this
    omega
  rw [Function.not_injective_iff] at this
  obtain ⟨i, j, hfe, hne⟩ := this
  exact ⟨i, j, hne, hfe⟩

/-- `rpow` substrate: fractional-exponent monotonicity, the shape in which `κ ≥ q/3`
is pushed through `κ^(1/6)` in the main theorem. -/
example {a b : ℝ} (ha : 0 ≤ a) (hab : a ≤ b) : a ^ (1/6 : ℝ) ≤ b ^ (1/6 : ℝ) :=
  Real.rpow_le_rpow ha hab (by norm_num)

end KsumAudit.Smoke
