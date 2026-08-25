/-
`SE/Support/Telescope.lean` — non-node support module.  TIER 2.

Node served: `SE.formal.t2` (`se/proof-dag/nodes/SE.formal.t2.yaml`).
Nodes served (≥ 2, which is why this is `Support/` and not a node module): every hook-product
estimate of `SE/Support/Hook.lean` and `SE/Support/Omega.lean`, hence
`SE.denom.assembly.envelope`, `SE.denom.Phi.legal.tame` and `SE.denom` downstream.

WHAT THIS FILE IS.  Two telescoping product identities over `ℝ`, in the two orientations the hook
products need:

  `∏_{i ∈ Ico a b} f i / f (i+1) = f a / f b`,     `∏_{i ∈ Ico a b} f (i+1) / f i = f b / f a`,

with the `Finset.range` specializations.  `ℝ` is not a multiplicative group, so Mathlib's
`Finset.prod_range_div` does not apply; the nonvanishing hypothesis is carried explicitly and the
proofs are inductions.

No `sorry`.
-/
import SE.Support.Defs

namespace SE

/-- Telescoping over `Finset.Ico`, descending orientation:
`∏_{i ∈ Ico a b} f i / f (i+1) = f a / f b`. -/
theorem prod_Ico_ratio {f : ℕ → ℝ} {a b : ℕ} (hab : a ≤ b)
    (hf : ∀ i, a ≤ i → i ≤ b → f i ≠ 0) :
    ∏ i ∈ Finset.Ico a b, (f i / f (i + 1)) = f a / f b := by
  induction b, hab using Nat.le_induction with
  | base => simpa using (div_self (hf a (le_refl a) (le_refl a))).symm
  | succ m hm ih =>
      have hfm : f m ≠ 0 := hf m hm (by omega)
      have hfm1 : f (m + 1) ≠ 0 := hf (m + 1) (by omega) (by omega)
      rw [Finset.prod_Ico_succ_top hm, ih fun i hi him => hf i hi (by omega)]
      field_simp

/-- Telescoping over `Finset.Ico`, ascending orientation:
`∏_{i ∈ Ico a b} f (i+1) / f i = f b / f a`. -/
theorem prod_Ico_ratio' {f : ℕ → ℝ} {a b : ℕ} (hab : a ≤ b)
    (hf : ∀ i, a ≤ i → i ≤ b → f i ≠ 0) :
    ∏ i ∈ Finset.Ico a b, (f (i + 1) / f i) = f b / f a := by
  induction b, hab using Nat.le_induction with
  | base => simpa using (div_self (hf a (le_refl a) (le_refl a))).symm
  | succ m hm ih =>
      have hfm : f m ≠ 0 := hf m hm (by omega)
      have hfa : f a ≠ 0 := hf a (le_refl a) (by omega)
      rw [Finset.prod_Ico_succ_top hm, ih fun i hi him => hf i hi (by omega)]
      field_simp

/-- Telescoping over `Finset.range`, descending orientation. -/
theorem prod_range_ratio {f : ℕ → ℝ} {L : ℕ} (hf : ∀ i, i ≤ L → f i ≠ 0) :
    ∏ i ∈ Finset.range L, (f i / f (i + 1)) = f 0 / f L := by
  rw [Finset.range_eq_Ico]
  exact prod_Ico_ratio (Nat.zero_le L) fun i _ hi => hf i hi

/-- Telescoping over `Finset.range`, ascending orientation. -/
theorem prod_range_ratio' {f : ℕ → ℝ} {L : ℕ} (hf : ∀ i, i ≤ L → f i ≠ 0) :
    ∏ i ∈ Finset.range L, (f (i + 1) / f i) = f L / f 0 := by
  rw [Finset.range_eq_Ico]
  exact prod_Ico_ratio' (Nat.zero_le L) fun i _ hi => hf i hi

end SE
