/-
`SE/Support/RhoEnvelope.lean` — non-node support module.  TIER 2 / TIER 2b.

Node served: `SE.formal.t2` (`se/proof-dag/nodes/SE.formal.t2.yaml`).
Nodes served (≥ 2): `SE.denom` (`block_le`, `dNorm_le`) and `SE.denom.Phi.legal.tame`
(`composition`, `gcan_le`, `csect_le`), which is why this is `Support/` and not a node module.

WHAT THIS FILE DOES.  It holds every DISCHARGED field of the tier-1 trust interface.  The names are
the SAME names the tier-1 chain calls (so every call site is unchanged, `hC.name n … args`), but
they are now THEOREMS proved from the definitional fields `Cited.rho_isGreatest`,
`Cited.sector_hook`, `Cited.admissible_window` plus the arithmetic of `SE/Support/Hook.lean` and
`SE/Support/Omega.lean`, instead of fields of the `Cited` structure.

  tier 1 (2026-07-30)                            tier 2 / 2b (2026-08-17)
  ────────────────────────────────────           ────────────────────────────────────
  Cited.rho_ge_one      assumed                  theorem (this file, tier 2a)
  Cited.rho_le          assumed                  theorem (this file, tier 2a)
  Cited.rhoConst_nonneg assumed                  theorem `SE.rhoConst_nonneg`  (tier 2a)
  SEFrame.rhoConst      abstract carrier field    `noncomputable def SE.rhoConst : ℝ := 4`
  Cited.rtop_le_rho     assumed                  theorem (this file, TIER 2b)
  Cited.rtop_pos        assumed                  theorem (this file, TIER 2b)
  Cited.omega_le        assumed                  theorem (this file, TIER 2b)
  Cited.omega_pos       assumed                  theorem (this file, TIER 2b)
                                                 ⟵ fields: `rho_isGreatest` (definitional; the
                                                   `IsGreatest` sharpening of tier 2a's
                                                   `rho_hook`), `sector_hook` (definitional),
                                                   `admissible_window` (definitional)

NO WEAKENING.  Every one of the eight theorems below has the tier-1 field's conclusion verbatim.
Two carry an added binder, both DECLARED:
* `rho_ge_one` narrows to the taper window `d < K n`, where both of its call sites live
  (`SE.denom.block_le`, `SE.denom.Phi.legal.tame.composition`);
* nothing else changes scope: `rtop_le_rho`, `rtop_pos`, `omega_le` and `omega_pos` keep their
  tier-1 binders `∀ n j s, F.admissible n j s → …` EXACTLY, because `admissible_window` supplies
  the window `1 ≤ j`, `3j ≤ n` from admissibility itself.

No `sorry`.
-/
import SE.Interface
import SE.Support.Hook
import SE.Support.Omega

namespace SE

namespace SEFrame.Cited

variable {F : SE.SEFrame}

/-! ## The hook envelope of `ρ_d` (tier 2a) -/

/-- **Hook envelope, lower half** — paper eq:rho-asymp, `1 ≤ ρ_d`.  PROVED at tier 2: every
factor of the explicit hook product is `≥ 1` (`SE.one_le_rtopHook`).

This was the tier-1 CITED field `Cited.rho_ge_one`; the name is kept so the tier-1 call sites are
unchanged, and the only added binder is the taper window they already carry. -/
theorem rho_ge_one (hC : F.Cited) (n d : ℕ) (hd : d < K n) : 1 ≤ F.rho n d := by
  have hdn : d < n := lt_of_lt_of_le hd (K_le_self n)
  obtain ⟨L, t, hcol, heq⟩ := (hC.rho_isGreatest n d hdn).1
  rw [heq]
  exact one_le_rtopHook (by omega) hcol.length_le

/-- **Hook envelope, upper half** — paper eq:rho-asymp,
`ρ_d ≤ exp(d(d-1)/(2(2n-d+1)) + d/(2n-2d+1)) = 1 + O(n^{-1/3})` uniformly for `d < K n`.
PROVED at tier 2, with the implied constant `SE.rhoConst = 4`: `SE.log_rtopHook_le` gives the
manuscript's exponent, `SE.hookExponent_le_inv_K` bounds it by `1/K n` on the taper window, and
`e^E ≤ 1/(1-E) ≤ 1+2E` with `n^{1/3} < K n + 1 ≤ 2·K n` closes it (`SE.rtopHook_le_envelope`).

This was the tier-1 CITED field `Cited.rho_le`, with the abstract `F.rhoConst` in place of `4`. -/
theorem rho_le (hC : F.Cited) (n d : ℕ) (hd : d < K n) :
    F.rho n d ≤ 1 + rhoConst / (n : ℝ) ^ ((1 : ℝ) / 3) := by
  have hdn : d < n := lt_of_lt_of_le hd (K_le_self n)
  obtain ⟨L, t, hcol, heq⟩ := (hC.rho_isGreatest n d hdn).1
  rw [heq]
  exact rtopHook_le_envelope hcol hd

/-! ## The sector scalars (tier 2b)

`admissible_window` turns admissibility into the manuscript's own window `1 ≤ j`, `3j ≤ n`, hence
`6j ≤ q = 2n` and `j < n`; `sector_hook` evaluates the sector's `r_top` and `ω` as the explicit
hook expressions; the four theorems are then the arithmetic of `SE/Support/Hook.lean` and
`SE/Support/Omega.lean`. -/

/-- The window an admissible sector carries, in the two forms the hook lemmas want. -/
theorem sector_window (hC : F.Cited) (n j : ℕ) (s : F.Sector n j) (hs : F.admissible n j s) :
    1 ≤ j ∧ 6 * j ≤ 2 * n ∧ j < n := by
  obtain ⟨hj1, hj3⟩ := hC.admissible_window n j s hs
  exact ⟨hj1, by omega, by omega⟩

/-- **`ρ_j` is the maximum over shapes** — paper eq:rtop, `r_top(2n,j,θ) ≤ ρ_j = max_{θ⊢j} r_top`.
PROVED at tier 2b: the sector's own shape puts `r_top(2n,j,θ)` into `SE.rtopHookSet n j`, and
`Cited.rho_isGreatest` says `ρ_j` dominates that set.

This was the tier-1 CITED field `Cited.rtop_le_rho`, with its binders unchanged. -/
theorem rtop_le_rho (hC : F.Cited) (n j : ℕ) (s : F.Sector n j) (hs : F.admissible n j s) :
    F.rtopS n j s ≤ F.rho n j := by
  obtain ⟨-, -, hjn⟩ := hC.sector_window n j s hs
  obtain ⟨hcol, hrtop, -⟩ := hC.sector_hook n j s hs
  exact (hC.rho_isGreatest n j hjn).2
    ⟨F.shapeLen n j s, F.shapeCol n j s, hcol, hrtop⟩

/-- **`0 < r_top`** — paper eq:rtop.  PROVED at tier 2b: every factor of the explicit hook product
is `≥ 1` on the window `2j < q` (`SE.rtopHook_pos`).

This was the tier-1 CITED field `Cited.rtop_pos`, with its binders unchanged. -/
theorem rtop_pos (hC : F.Cited) (n j : ℕ) (s : F.Sector n j) (hs : F.admissible n j s) :
    0 < F.rtopS n j s := by
  obtain ⟨-, -, hjn⟩ := hC.sector_window n j s hs
  obtain ⟨hcol, hrtop, -⟩ := hC.sector_hook n j s hs
  rw [hrtop]
  exact rtopHook_pos (by omega) hcol.length_le

/-- **The `ω` range, upper half** — paper eq:omega-range, `ω ≤ j/(q-2j) = j/(2(n-j))`, which the
manuscript calls "the reviewed-proved range" and which the human cross-stack review
(`se/reviews/se_human_review_20260719.md`) confirmed.  PROVED at tier 2b from the hook ratio
`p₀` and the telescoping majorant `∏(1-1/h_c) ≤ (A+a-θ₁)/(A+a)` (`SE.omegaHook_le`).

This was the tier-1 CITED field `Cited.omega_le`, with its binders and its right-hand side
unchanged. -/
theorem omega_le (hC : F.Cited) (n j : ℕ) (s : F.Sector n j) (hs : F.admissible n j s) :
    F.omegaS n j s ≤ (j : ℝ) / (2 * ((n : ℝ) - (j : ℝ))) := by
  obtain ⟨hj1, hq6, -⟩ := hC.sector_window n j s hs
  obtain ⟨hcol, -, homega⟩ := hC.sector_hook n j s hs
  have hbound := omegaHook_le (q := 2 * n) (j := j) (L := F.shapeLen n j s)
    (t := F.shapeCol n j s) hj1 hq6 hcol
  have hden : ((2 * n : ℕ) : ℝ) - 2 * (j : ℝ) = 2 * ((n : ℝ) - (j : ℝ)) := by
    push_cast
    ring
  rw [hden] at hbound
  rw [homega]
  exact hbound

/-- **The `ω` range, lower half, in the form the interface uses** — paper eq:omega-range,
`j/q ≤ ω`, hence `0 < ω` for `j ≥ 1` (which admissibility gives).  PROVED at tier 2b
(`SE.omegaHook_pos`, from `SE.le_omegaHook`).

This was the tier-1 CITED field `Cited.omega_pos`, with its binders unchanged. -/
theorem omega_pos (hC : F.Cited) (n j : ℕ) (s : F.Sector n j) (hs : F.admissible n j s) :
    0 < F.omegaS n j s := by
  obtain ⟨hj1, hq6, -⟩ := hC.sector_window n j s hs
  obtain ⟨hcol, -, homega⟩ := hC.sector_hook n j s hs
  rw [homega]
  exact omegaHook_pos hj1 hq6 hcol

/-- The lower half of eq:omega-range itself, as proved at tier 2b: `j/q = j/(2n) ≤ ω`.  Not a
tier-1 field (the interface only ever needed positivity), recorded because it is the OTHER half of
the manuscript's two-sided range and it is what makes `omega_pos` true rather than assumed. -/
theorem le_omega (hC : F.Cited) (n j : ℕ) (s : F.Sector n j) (hs : F.admissible n j s) :
    (j : ℝ) / (2 * (n : ℝ)) ≤ F.omegaS n j s := by
  obtain ⟨hj1, hq6, -⟩ := hC.sector_window n j s hs
  obtain ⟨hcol, -, homega⟩ := hC.sector_hook n j s hs
  have hbound := le_omegaHook (q := 2 * n) (j := j) (L := F.shapeLen n j s)
    (t := F.shapeCol n j s) hj1 hq6 hcol
  have hden : ((2 * n : ℕ) : ℝ) = 2 * (n : ℝ) := by push_cast; ring
  rw [hden] at hbound
  rw [homega]
  exact hbound

end SEFrame.Cited

end SE
