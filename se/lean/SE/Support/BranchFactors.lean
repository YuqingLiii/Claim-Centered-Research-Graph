/-
`SE/Support/BranchFactors.lean` — non-node support module.  TIER 2.

Node served: `SE.formal.t2` (`se/proof-dag/nodes/SE.formal.t2.yaml`).
Node whose constants these are: `SE.denom.Phi.ambient` (PROVED on disk), whose tier-1 shadow is
the CITED field `SEFrame.Cited.cDiag_bound`.

PLACEMENT.  Same reasoning as coordinator ruling R1 (`SE/Support/Envelope.lean`): the node
`SE.denom.Phi.ambient` has no tier-1 rendering — its statement is about operator norms
(`‖T_k‖ = ‖W_{se,k}Φ_{se,k}‖`), and tier 2 still has no operator layer — so the node keeps
no `formalization` block and the ARITHMETIC inside its proof lives here, in a stable non-node home.

WHAT IS PROVED HERE, AND WHAT IS NOT.  These are the two numeric steps of the manuscript's
`lem:br-special-path` and `lem:phi-ambient`:

  * `((|P|+2)/2)·2^{-max(0,|P|-4)/2} ≤ 3` for every even `|P| ≥ 2`, with EQUALITY exactly at
    `|P| = 4` — the corrected BR special-path projection ratio, whose square root is the `√3` of
    `lem:br-special-path`;
  * `√(1/(m-2d+2) + 1/(m-2d+1)) ≤ √2/√(m-2d+1)` — the Cauchy–Schwarz closure of
    eq:br-completion-explicit — and the composition
    `√3 · √2/√(n-2(k-ℓ)+1) ≤ √6/√(n-2k+1)` for `0 ≤ ℓ ≤ k`, which is the final display of
    `lem:phi-ambient`'s proof.

This does NOT discharge `Cited.cDiag_bound`: the operator content of that field (the BR graph
decomposition, the row count, the Schur reduction selecting one `ℓ ∈ [0,k-1]`, and the
orthogonality of the second-half projectors) is representation-theoretic and stays cited.  What
tier 2 removes is the possibility that the CONSTANTS `√3`, `√2`, `√6` are arithmetic slips.

No `sorry`.
-/
import SE.Support.Defs
import SE.Support.Constants

namespace SE

/-! ## The BR special-path factor

`specialPathFactor` is indexed by the half-length `s = |P|/2`; `specialPathFactorLen` is the same
quantity written in `|P|` exactly as the manuscript displays it.  Truncated natural subtraction in
the exponent *is* `max(0, ·)`. -/

/-- The corrected BR special-path projection ratio at `|P| = 2s`:
`((|P|+2)/2)·2^{-max(0,|P|-4)/2} = (s+1)/2^{(s-2)_+}`. -/
noncomputable def specialPathFactor (s : ℕ) : ℝ := ((s : ℝ) + 1) / (2 : ℝ) ^ (s - 2)

/-- The same ratio in the manuscript's own variable `|P|`:
`((|P|+2)/2)·2^{-max(0,|P|-4)/2}`. -/
noncomputable def specialPathFactorLen (P : ℕ) : ℝ :=
  ((P : ℝ) + 2) / 2 / (2 : ℝ) ^ ((P - 4) / 2)

theorem specialPathFactorLen_two_mul (s : ℕ) :
    specialPathFactorLen (2 * s) = specialPathFactor s := by
  have hexp : (2 * s - 4) / 2 = s - 2 := by omega
  unfold specialPathFactorLen specialPathFactor
  rw [hexp]
  congr 1
  push_cast
  ring

/-- The integer heart: `s + 1 ≤ 3·2^{s-2}` for `s ≥ 2`. -/
theorem succ_le_three_mul_pow {s : ℕ} (hs : 2 ≤ s) : s + 1 ≤ 3 * 2 ^ (s - 2) := by
  induction s, hs using Nat.le_induction with
  | base => norm_num
  | succ m hm ih =>
      have h1 : m + 1 - 2 = (m - 2) + 1 := by omega
      rw [h1, pow_succ]
      omega

/-- Strictly, for `s ≥ 3`: `s + 1 < 3·2^{s-2}`. -/
theorem succ_lt_three_mul_pow {s : ℕ} (hs : 3 ≤ s) : s + 1 < 3 * 2 ^ (s - 2) := by
  induction s, hs using Nat.le_induction with
  | base => norm_num
  | succ m hm ih =>
      have h1 : m + 1 - 2 = (m - 2) + 1 := by omega
      rw [h1, pow_succ]
      omega

theorem two_pow_pos (m : ℕ) : (0 : ℝ) < (2 : ℝ) ^ m := by positivity

/-- **The special-path factor is at most 3** — `lem:br-special-path`, the bound whose square root
is the lemma's `√3`. -/
theorem specialPathFactor_le_three (s : ℕ) : specialPathFactor s ≤ 3 := by
  unfold specialPathFactor
  rw [div_le_iff₀ (two_pow_pos (s - 2))]
  rcases Nat.lt_or_ge s 2 with hs | hs
  · interval_cases s <;> norm_num
  · have h := succ_le_three_mul_pow hs
    have hcast : ((s + 1 : ℕ) : ℝ) ≤ ((3 * 2 ^ (s - 2) : ℕ) : ℝ) := by exact_mod_cast h
    push_cast at hcast
    linarith

/-- **The maximum is attained exactly at `|P| = 4`** (`s = 2`) — the manuscript's "whose maximum is
attained at `|P| = 4`".

(Tier-2 review fix F7, 2026-08-17: the needless hypothesis `1 ≤ s` is gone.  `spf 0 = 1 ≠ 3`, so
the `↔` holds at `s = 0` as well, and the statement is now unconditional in `s`.) -/
theorem specialPathFactor_eq_three_iff {s : ℕ} :
    specialPathFactor s = 3 ↔ s = 2 := by
  constructor
  · intro h
    by_contra hne
    rcases Nat.lt_or_ge s 3 with hlt | hge
    · -- `s ∈ {0, 1}` (`s = 2` is excluded)
      have hs01 : s = 0 ∨ s = 1 := by omega
      rcases hs01 with hs0 | hs1
      · rw [hs0] at h
        norm_num [specialPathFactor] at h
      rw [hs1] at h
      norm_num [specialPathFactor] at h
    · have hstrict : specialPathFactor s < 3 := by
        unfold specialPathFactor
        rw [div_lt_iff₀ (two_pow_pos (s - 2))]
        have hlt := succ_lt_three_mul_pow hge
        have hcast : ((s + 1 : ℕ) : ℝ) < ((3 * 2 ^ (s - 2) : ℕ) : ℝ) := by exact_mod_cast hlt
        push_cast at hcast
        linarith
      linarith
  · intro h
    subst h
    norm_num [specialPathFactor]

/-- The `|P|`-indexed form: for every even `|P| ≥ 2`,
`((|P|+2)/2)·2^{-max(0,|P|-4)/2} ≤ 3`, with equality exactly at `|P| = 4`. -/
theorem specialPathFactorLen_le_three {P : ℕ} (hP : 2 ≤ P) (hev : P % 2 = 0) :
    specialPathFactorLen P ≤ 3 ∧ (specialPathFactorLen P = 3 ↔ P = 4) := by
  obtain ⟨s, hs⟩ : ∃ s, P = 2 * s := ⟨P / 2, by omega⟩
  subst hs
  rw [specialPathFactorLen_two_mul]
  refine ⟨specialPathFactor_le_three s, ?_⟩
  rw [specialPathFactor_eq_three_iff]
  omega

/-- The square root form the manuscript uses: `√(((|P|+2)/2)·2^{-max(0,|P|-4)/2}) ≤ √3`. -/
theorem sqrt_specialPathFactor_le (s : ℕ) :
    Real.sqrt (specialPathFactor s) ≤ Real.sqrt 3 :=
  Real.sqrt_le_sqrt (specialPathFactor_le_three s)

/-! ## The two `Φ` completion branches

`lem:br-completion`, eq:br-completion-explicit: the `H₁` branch contributes `(m-2d+2)^{-1/2}`, the
`H₀` branch `(m-2d+1)^{-1/2}`, and orthogonality (Cauchy–Schwarz) turns the pair into
`√(1/(m-2d+2) + 1/(m-2d+1)) ≤ √2/√(m-2d+1)`. -/

/-- **The branch combination** of eq:br-completion-explicit, in the variable `x = m-2d+1 > 0`:
`√(1/(x+1) + 1/x) ≤ √2/√x`. -/
theorem branch_pair_le {x : ℝ} (hx : 0 < x) :
    Real.sqrt (1 / (x + 1) + 1 / x) ≤ Real.sqrt 2 / Real.sqrt x := by
  have hx1 : (0 : ℝ) < x + 1 := by linarith
  have hmono : 1 / (x + 1) ≤ 1 / x := by
    rw [div_le_div_iff₀ hx1 hx]
    linarith
  have hsum : 1 / (x + 1) + 1 / x ≤ 2 / x := by
    have : 1 / x + 1 / x = 2 / x := by ring
    linarith
  calc Real.sqrt (1 / (x + 1) + 1 / x) ≤ Real.sqrt (2 / x) := Real.sqrt_le_sqrt hsum
    _ = Real.sqrt 2 / Real.sqrt x := sqrt_div_eq (by norm_num)

/-- **The `Φ` ambient composition** — the final display of `lem:phi-ambient`'s proof:
`√3 · (√2/√a) ≤ √6/√b` whenever `0 < b ≤ a`.  The manuscript's instance is
`a = n-2(k-ℓ)+1 ≥ b = n-2k+1` (`0 ≤ ℓ ≤ k`), where the `√3` is `lem:br-special-path` and the
`√2/√a` is eq:br-completion-explicit. -/
theorem phi_branch_combine {a b : ℝ} (hb : 0 < b) (hab : b ≤ a) :
    Real.sqrt 3 * (Real.sqrt 2 / Real.sqrt a) ≤ Real.sqrt 6 / Real.sqrt b := by
  have hbs : (0 : ℝ) < Real.sqrt b := Real.sqrt_pos.mpr hb
  have has : Real.sqrt b ≤ Real.sqrt a := Real.sqrt_le_sqrt hab
  have hasp : (0 : ℝ) < Real.sqrt a := lt_of_lt_of_le hbs has
  have h6 : Real.sqrt 3 * Real.sqrt 2 = Real.sqrt 6 := by
    rw [sqrt_six]; ring
  have hrw : Real.sqrt 3 * (Real.sqrt 2 / Real.sqrt a) = Real.sqrt 6 / Real.sqrt a := by
    rw [← h6]; ring
  rw [hrw]
  exact div_le_div_of_nonneg_left (Real.sqrt_nonneg 6) hbs has

/-- The manuscript's instance, in `n`, `k`, `ℓ`: for `ℓ ≤ k` and `n - 2k + 1 > 0`,
`√3 · √2/√(n-2(k-ℓ)+1) ≤ √6/√(n-2k+1)`. -/
theorem phi_ambient_combine {n k l : ℕ} (hl : l ≤ k) (hpos : (0 : ℝ) < (n : ℝ) - 2 * (k : ℝ) + 1) :
    Real.sqrt 3 * (Real.sqrt 2 / Real.sqrt ((n : ℝ) - 2 * ((k : ℝ) - (l : ℝ)) + 1))
      ≤ Real.sqrt 6 / Real.sqrt ((n : ℝ) - 2 * (k : ℝ) + 1) := by
  have hlk : (l : ℝ) ≤ (k : ℝ) := by exact_mod_cast hl
  have hl0 : (0 : ℝ) ≤ (l : ℝ) := Nat.cast_nonneg l
  refine phi_branch_combine hpos ?_
  linarith

/-- The two steps composed, as `lem:phi-ambient` uses them: the special-path factor (at any even
`|P| ≥ 2`) times the completion pair is at most `√6/√(n-2k+1)`. -/
theorem phi_ambient_full {n k l : ℕ} {x : ℝ} (hl : l ≤ k)
    (hxeq : x = (n : ℝ) - 2 * ((k : ℝ) - (l : ℝ)) + 1)
    (hpos : (0 : ℝ) < (n : ℝ) - 2 * (k : ℝ) + 1) (s : ℕ) :
    Real.sqrt (specialPathFactor s) * Real.sqrt (1 / (x + 1) + 1 / x)
      ≤ Real.sqrt 6 / Real.sqrt ((n : ℝ) - 2 * (k : ℝ) + 1) := by
  have hlk : (l : ℝ) ≤ (k : ℝ) := by exact_mod_cast hl
  have hl0 : (0 : ℝ) ≤ (l : ℝ) := Nat.cast_nonneg l
  have hxb : (n : ℝ) - 2 * (k : ℝ) + 1 ≤ x := by rw [hxeq]; linarith
  have hx : (0 : ℝ) < x := by linarith
  have hxs : (0 : ℝ) < Real.sqrt x := Real.sqrt_pos.mpr hx
  have h1 : Real.sqrt (specialPathFactor s) ≤ Real.sqrt 3 := sqrt_specialPathFactor_le s
  have h2 : Real.sqrt (1 / (x + 1) + 1 / x) ≤ Real.sqrt 2 / Real.sqrt x := branch_pair_le hx
  have h2nn : (0 : ℝ) ≤ Real.sqrt (1 / (x + 1) + 1 / x) := Real.sqrt_nonneg _
  have hstep : Real.sqrt (specialPathFactor s) * Real.sqrt (1 / (x + 1) + 1 / x)
      ≤ Real.sqrt 3 * (Real.sqrt 2 / Real.sqrt x) := by
    have hA : Real.sqrt (specialPathFactor s) * Real.sqrt (1 / (x + 1) + 1 / x)
        ≤ Real.sqrt 3 * Real.sqrt (1 / (x + 1) + 1 / x) :=
      mul_le_mul_of_nonneg_right h1 h2nn
    have hB : Real.sqrt 3 * Real.sqrt (1 / (x + 1) + 1 / x)
        ≤ Real.sqrt 3 * (Real.sqrt 2 / Real.sqrt x) :=
      mul_le_mul_of_nonneg_left h2 (Real.sqrt_nonneg 3)
    linarith
  exact le_trans hstep (phi_branch_combine hpos hxb)

end SE
