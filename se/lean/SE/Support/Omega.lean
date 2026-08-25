/-
`SE/Support/Omega.lean` — non-node support module.  TIER 2b.

Node served: `SE.formal.t2` (`se/proof-dag/nodes/SE.formal.t2.yaml`), frontier task-003.
Nodes whose tier-1 CITED fields this file discharges (≥ 2, which is why this is `Support/` and not
a node module): `SE.denom.Phi.legal.tame` (the fields `Cited.omega_le` and `Cited.omega_pos` are
consumed by `tame.gcan_le` and `tame.csect_le`) and, through `SE/Interface.lean`, every node
downstream of it (`SE.denom`, `SE.br`, `SE.goal`).

WHAT THIS FILE IS.  Tier 1 CITED the manuscript's `ω`-range eq:omega-range,

  `j/q ≤ ω ≤ j/(q-2j)`,       `ω = (1-p₀)/p₀`,   `p₀ = f^{(q-j-1,θ)}/f^{(q-j,θ)}`,

as two assumptions about an abstract real `F.omegaS`.  Tier 2b replaces them by ARITHMETIC: `p₀` is
DEFINED here by its hook ratio in the conjugate coordinates of `SE.IsColumnData`, and the two-sided
range is then proved.

THE DEFINITION.  With `λ = (q-j,θ)`, the first-row hooks of `λ` are `h_c = q-j-c+1+θ'_c`
(`SE.rowHook`, at the index `i = c-1`), the hooks of the remaining rows are exactly the hooks of
`θ`, and the first-row hooks of `λ⁻ = (q-j-1,θ)` are `h_c - 1`.  The `θ`-hooks therefore cancel in
the ratio and the Frame–Robinson–Thrall hook-length formula gives

  `p₀ = (1/q) · ∏_{c=1}^{q-j} h_c / ∏_{c=1}^{q-j-1} (h_c - 1)`      (`SE.p0Hook`)

— the hook ratio written out, with `q!/(q-1)! = q` the only surviving factorial.  This is the ONE
external fact this file cites (the same citation as `Cited.rho_isGreatest`); everything
below it is proved.

THE TWO REGROUPINGS.  `h_{q-j} = 1` kills the top factor of the numerator, so

  `1/p₀ = q · ∏_{c=1}^{q-j-1}(1 - 1/h_c)`,

and the factors with `c > θ₁` have `θ'_c = 0`, hence `1 - 1/h_c = (q-j-c)/(q-j-c+1)`, which
TELESCOPES over `Finset.Ico θ₁ (q-j-1)` to `1/(q-j-θ₁)`.  What is left is the form the bounds want:

  `1/p₀ = q/(q-j-θ₁) · ∏_{c=1}^{θ₁}(1 - 1/h_c)`,      `ω = 1/p₀ - 1`.

THE TWO MAJORANTS.  Both are telescoping and neither MAJORANT STEP is lossy — each is an equality
at `j = 1`, so no step of the form `∏(1-x_c) ≤ exp(-Σx_c)` is admissible.  That is a statement about
the STEPS, and it does NOT say that both ENDS of the resulting range are tight.  They are not:
the UPPER bound `ω ≤ j/(q-2j)` IS attained — at `j = 1`, `θ = (1)`, `ω = 1/(q-2) = j/(q-2j)` exactly
— while the LOWER bound `j/q ≤ ω` is attained NOWHERE.  Already at `j = 1` its exact value
`1/(q-2)` strictly exceeds `1/q`, and one exact-rational sweep (re-run and
reproduced; independently corroborated by the task-013 review's own branching-rule sweep)
(`tools/se_hook_definition_crosscheck.py`: 1782 range checks, and the 35183-check run recorded in
`se/artifacts/logs_se_lean_t2b_20260817/definition_crosscheck.txt`) found 0 cases attaining it against
55 attaining the upper end.  `j/q` is therefore a SAFE BUT LOOSE floor; what the development needs
from it is only positivity (`SE.SEFrame.Cited.omega_pos`, via `.le_omega`), never tightness:

  * `θ'_c ≥ 1` gives `h_c ≥ q-j-c+2`, hence `∏(1-1/h_c) ≥ (A-θ₁+1)/(A+1)` with `A = q-j`, and
    `j/q ≤ ω` reduces to `q² ≥ s(q+j-j²)` with `s = A-θ₁ ≤ A-1`;
  * `θ'_c ≤ θ'_1 = a` gives `h_c ≤ q-j-c+1+a`, hence `∏(1-1/h_c) ≤ (A+a-θ₁)/(A+a)`, and
    `ω ≤ j/(q-2j)` reduces to `A(j² - θ₁a) + j²(a - θ₁) ≥ 0`, which holds because a partition of
    `j` has `a + θ₁ ≤ j+1` (`SE.IsColumnData.head_add_length_le`) and because `A ≥ 5j` on the
    manuscript's window `n ≥ 3j`, `q = 2n`.

WINDOW.  Everything is stated for `1 ≤ j` and `6j ≤ q`, i.e. exactly the manuscript's `j = k-1 ≥ 1`
and `n ≥ 3j` at `q = 2n` (paper, before eq:strict-sector).

No `sorry`, no `axiom`, no `native_decide`.
-/
import SE.Support.Hook

namespace SE

/-! ## The hook ratio `p₀` and `ω = (1-p₀)/p₀` -/

/-- The first-row hooks of `λ = (q-j,θ)` in the conjugate coordinates `t i = θ'_{i+1}`:
`rowHook q j t i = q-j-i+θ'_{i+1}`, i.e. the hook `h_c = q-j-c+1+θ'_c` at `c = i+1`. -/
noncomputable def rowHook (q j : ℕ) (t : ℕ → ℕ) (i : ℕ) : ℝ :=
  (q : ℝ) - (j : ℝ) - (i : ℝ) + (t i : ℝ)

/-- **The hook ratio** `p₀ = f^{(q-j-1,θ)}/f^{(q-j,θ)}` of paper eq:parameters-can, evaluated by
the hook-length formula: the `θ`-hooks cancel, the first-row hooks of `λ⁻` are `h_c - 1`, and
`(q-1)!/q! = 1/q`. -/
noncomputable def p0Hook (q j : ℕ) (t : ℕ → ℕ) : ℝ :=
  1 / (q : ℝ) * ((∏ i ∈ Finset.range (q - j), rowHook q j t i)
    / ∏ i ∈ Finset.range (q - j - 1), (rowHook q j t i - 1))

/-- **`ω = (1-p₀)/p₀`**, paper eq:parameters-can. -/
noncomputable def omegaHook (q j : ℕ) (t : ℕ → ℕ) : ℝ :=
  (1 - p0Hook q j t) / p0Hook q j t

/-! ## The two pieces of pure real arithmetic

Isolated so that the polynomial content of eq:omega-range is visible on its own. -/

/-- The lower half of eq:omega-range as a polynomial inequality: `q²(s+1) ≥ (q+j)(A+1)s` for
`A = q-j`, `1 ≤ s ≤ A-1`, `1 ≤ j`, `6j ≤ q`.  It is `q² ≥ s(q+j-j²)`, and `j ≤ j²`, `s ≤ q-j-1`
give it with room to spare. -/
theorem omega_lower_core {q j s : ℝ} (hj : 1 ≤ j) (hq : 6 * j ≤ q) (hs1 : 1 ≤ s)
    (hsA : s ≤ q - j - 1) :
    (q + j) * ((q - j) + 1) * s ≤ q ^ 2 * (s + 1) := by
  have hq6 : (6 : ℝ) ≤ q := by linarith
  have hjj : j ≤ j ^ 2 := by nlinarith
  have hs0 : (0 : ℝ) ≤ s := by linarith
  -- `s(j - j²) ≤ 0`
  have h1 : s * (j - j ^ 2) ≤ 0 := mul_nonpos_of_nonneg_of_nonpos hs0 (by linarith)
  -- `s·q ≤ (q-j-1)q ≤ q² - q(j+1)`
  have h2 : s * q ≤ (q - j - 1) * q := by
    have : (0 : ℝ) < q := by linarith
    exact mul_le_mul_of_nonneg_right hsA this.le
  nlinarith

/-- The upper half of eq:omega-range as a polynomial inequality:
`A(j² - L·a) + j²(a - L) ≥ 0`, in the cross-multiplied form
`(A²-j²)(A+a-L) ≤ A(A-L)(A+a)`, for a shape of `j` (`1 ≤ a`, `1 ≤ L`, `a+L ≤ j+1`) on the window
`A ≥ 5j`.  Equality holds exactly at `j = 1` (`a = L = 1`), which is why no lossy step is
admissible.  (`1 ≤ j` is not a hypothesis because `1 ≤ a`, `1 ≤ L` and `a + L ≤ j + 1` already
force it.) -/
theorem omega_upper_core {A a L j : ℝ} (ha : 1 ≤ a) (hL : 1 ≤ L) (haL : a + L ≤ j + 1)
    (hA : 5 * j ≤ A) :
    (A ^ 2 - j ^ 2) * (A + a - L) ≤ A * (A - L) * (A + a) := by
  have hApos : (0 : ℝ) < A := by linarith
  -- `4·L·a ≤ (a+L)² ≤ (j+1)²`, hence `4(j² - L·a) ≥ (j-1)(3j+1) ≥ 0`
  have hsq : 4 * (L * a) ≤ (a + L) ^ 2 := by nlinarith [sq_nonneg (a - L)]
  have haL0 : (0 : ℝ) ≤ a + L := by linarith
  have hsq2 : (a + L) ^ 2 ≤ (j + 1) ^ 2 := by nlinarith
  have hgap : (j - 1) * (3 * j + 1) ≤ 4 * (j ^ 2 - L * a) := by nlinarith
  have hgap0 : (0 : ℝ) ≤ j ^ 2 - L * a := by nlinarith
  -- `L - a ≤ j - 1`
  have hdiff : L - a ≤ j - 1 := by linarith
  -- `A(j² - L·a) ≥ 5j(j² - L·a) ≥ (5/4)j(j-1)(3j+1) ≥ j²(j-1) ≥ j²(L-a)`
  have hstep1 : 5 * j * (j ^ 2 - L * a) ≤ A * (j ^ 2 - L * a) :=
    mul_le_mul_of_nonneg_right hA hgap0
  have hstep2 : j ^ 2 * (L - a) ≤ j ^ 2 * (j - 1) := by nlinarith
  have hstep3 : j ^ 2 * (j - 1) ≤ 5 * j * (j ^ 2 - L * a) := by nlinarith
  nlinarith

/-! ## The reduction of `p₀` to its `θ₁` nontrivial factors -/

section Reduce

variable {q j L : ℕ} {t : ℕ → ℕ}

/-- On the window, `θ₁ ≤ q-j-1`: there is at least one first-row hook beyond the shape. -/
theorem length_le_window (hj : 1 ≤ j) (hq : 6 * j ≤ q) (hcol : IsColumnData L t j) :
    L ≤ q - j - 1 := by
  have := hcol.length_le
  omega

/-- `1 ≤ θ₁` when `1 ≤ j`. -/
theorem one_le_length (hj : 1 ≤ j) (hcol : IsColumnData L t j) : 1 ≤ L := by
  rcases Nat.eq_zero_or_pos L with rfl | h
  · have := hcol.sum_eq
    simp at this
    omega
  · exact h

/-- Every first-row hook indexed below `q-j` is positive.  (No window hypothesis is needed:
`i < q - j` in `ℕ` already forces `i + j < q`.) -/
theorem rowHook_pos {i : ℕ} (hi : i < q - j) :
    0 < rowHook q j t i := by
  have hcast : (i : ℝ) + 1 ≤ (q : ℝ) - (j : ℝ) := by
    have h1 : i + 1 + j ≤ q := by omega
    have h2 : ((i + 1 + j : ℕ) : ℝ) ≤ (q : ℝ) := by exact_mod_cast h1
    push_cast at h2
    linarith
  have h0 : (0 : ℝ) ≤ (t i : ℝ) := Nat.cast_nonneg _
  simp only [rowHook]
  linarith

/-- Every hook of `λ⁻` indexed below `q-j-1` is positive: `h_c - 1 = q-j-c+θ'_c > 0`.  (Again no
window hypothesis is needed.) -/
theorem rowHook_sub_one_pos {i : ℕ} (hi : i < q - j - 1) :
    0 < rowHook q j t i - 1 := by
  have hcast : (i : ℝ) + 2 ≤ (q : ℝ) - (j : ℝ) := by
    have h1 : i + 2 + j ≤ q := by omega
    have h2 : ((i + 2 + j : ℕ) : ℝ) ≤ (q : ℝ) := by exact_mod_cast h1
    push_cast at h2
    linarith
  have h0 : (0 : ℝ) ≤ (t i : ℝ) := Nat.cast_nonneg _
  simp only [rowHook]
  linarith

/-- The top first-row hook is trivial: `h_{q-j} = 1`, because `θ'_{q-j} = 0`. -/
theorem rowHook_top (hj : 1 ≤ j) (hq : 6 * j ≤ q) (hcol : IsColumnData L t j) :
    rowHook q j t (q - j - 1) = 1 := by
  have hvan : t (q - j - 1) = 0 := hcol.vanish _ (length_le_window hj hq hcol)
  have hcast : (((q - j - 1 : ℕ)) : ℝ) = (q : ℝ) - (j : ℝ) - 1 := by
    have h1 : j + 1 ≤ q := by omega
    have : ((q - j - 1 : ℕ) : ℝ) + ((j : ℝ) + 1) = (q : ℝ) := by
      have : (q - j - 1) + (j + 1) = q := by omega
      have h2 : (((q - j - 1) + (j + 1) : ℕ) : ℝ) = (q : ℝ) := by exact_mod_cast this
      push_cast at h2
      linarith
    linarith
  simp only [rowHook, hvan, hcast]
  norm_num

/-- `p₀`, with its numerator's trivial top factor removed and the ratio taken factorwise. -/
theorem p0Hook_eq_prod (hj : 1 ≤ j) (hq : 6 * j ≤ q) (hcol : IsColumnData L t j) :
    p0Hook q j t = 1 / (q : ℝ) * ∏ i ∈ Finset.range (q - j - 1),
        (rowHook q j t i / (rowHook q j t i - 1)) := by
  have hgen : ∀ M : ℕ, q - j = M + 1 →
      ∏ i ∈ Finset.range (q - j), rowHook q j t i = ∏ i ∈ Finset.range M, rowHook q j t i := by
    intro M hM
    rw [hM, Finset.prod_range_succ]
    have hMv : M = q - j - 1 := by omega
    rw [hMv, rowHook_top hj hq hcol, mul_one]
  have hnum := hgen (q - j - 1) (by omega)
  simp only [p0Hook, hnum, Finset.prod_div_distrib]

/-- **The reduced form of `p₀`**: `p₀ = 1/(q/(q-j-θ₁) · ∏_{c≤θ₁}(1-1/h_c))`.  This is the second
regrouping of the header: the factors beyond the shape telescope over `Finset.Ico θ₁ (q-j-1)`. -/
theorem p0Hook_eq_inv (hj : 1 ≤ j) (hq : 6 * j ≤ q) (hcol : IsColumnData L t j) :
    p0Hook q j t
      = 1 / ((q : ℝ) / ((q : ℝ) - (j : ℝ) - (L : ℝ))
          * ∏ i ∈ Finset.range L, (1 - 1 / rowHook q j t i)) := by
  set M : ℕ := q - j - 1 with hM
  have hLM : L ≤ M := length_le_window hj hq hcol
  have hqpos : (0 : ℝ) < (q : ℝ) := by
    have : 0 < q := by omega
    exact_mod_cast this
  -- the real value of the two endpoints
  have hMcast : ((M : ℕ) : ℝ) = (q : ℝ) - (j : ℝ) - 1 := by
    have h1 : (M + (j + 1) : ℕ) = q := by omega
    have h2 : (((M + (j + 1) : ℕ)) : ℝ) = (q : ℝ) := by exact_mod_cast h1
    push_cast at h2
    linarith
  have hLcast : (0 : ℝ) < (q : ℝ) - (j : ℝ) - (L : ℝ) := by
    have h1 : (L : ℝ) + 1 ≤ (q : ℝ) - (j : ℝ) := by
      have h2 : L + 1 + j ≤ q := by omega
      have h3 : ((L + 1 + j : ℕ) : ℝ) ≤ (q : ℝ) := by exact_mod_cast h2
      push_cast at h3
      linarith
    linarith
  -- factorwise reciprocal
  have hfac : ∀ i ∈ Finset.range M,
      rowHook q j t i / (rowHook q j t i - 1) = (1 - 1 / rowHook q j t i)⁻¹ := by
    intro i hi
    have hi' : i < M := Finset.mem_range.mp hi
    have h1 : 0 < rowHook q j t i := rowHook_pos (by omega)
    have h2 : 0 < rowHook q j t i - 1 := rowHook_sub_one_pos (by omega)
    have heq : 1 - 1 / rowHook q j t i = (rowHook q j t i - 1) / rowHook q j t i := by
      field_simp
    rw [heq, inv_div]
  -- the tail telescopes
  have htail : ∏ i ∈ Finset.Ico L M, (1 - 1 / rowHook q j t i)
      = 1 / ((q : ℝ) - (j : ℝ) - (L : ℝ)) := by
    set f : ℕ → ℝ := fun i => (q : ℝ) - (j : ℝ) - (i : ℝ) with hf
    have hfpos : ∀ i, L ≤ i → i ≤ M → 0 < f i := by
      intro i _ hiM
      have h1 : (i : ℝ) ≤ (M : ℝ) := by exact_mod_cast hiM
      simp only [hf]
      rw [hMcast] at h1
      linarith
    have hstep : ∀ i ∈ Finset.Ico L M, (1 - 1 / rowHook q j t i) = f (i + 1) / f i := by
      intro i hi
      obtain ⟨hiL, hiM⟩ := Finset.mem_Ico.mp hi
      have hvan : t i = 0 := hcol.vanish i hiL
      have hrow : rowHook q j t i = f i := by
        simp only [rowHook, hf, hvan]
        norm_num
      have hfi : 0 < f i := hfpos i hiL (by omega)
      have hfi1 : f (i + 1) = f i - 1 := by
        simp only [hf]; push_cast; ring
      rw [hrow, hfi1]
      field_simp
    rw [Finset.prod_congr rfl hstep,
      prod_Ico_ratio' hLM fun i hi hiM => ne_of_gt (hfpos i hi hiM)]
    simp only [hf, hMcast]
    rw [show (q : ℝ) - (j : ℝ) - ((q : ℝ) - (j : ℝ) - 1) = 1 from by ring]
  -- assemble
  have hsplit : ∏ i ∈ Finset.range M, (1 - 1 / rowHook q j t i)
      = (∏ i ∈ Finset.range L, (1 - 1 / rowHook q j t i))
        * ∏ i ∈ Finset.Ico L M, (1 - 1 / rowHook q j t i) := by
    rw [Finset.range_eq_Ico, Finset.range_eq_Ico,
      ← Finset.prod_Ico_consecutive _ (Nat.zero_le L) hLM]
  have hPpos : 0 < ∏ i ∈ Finset.range L, (1 - 1 / rowHook q j t i) := by
    refine Finset.prod_pos fun i hi => ?_
    have hi' : i < L := Finset.mem_range.mp hi
    have h1 : 0 < rowHook q j t i := rowHook_pos (by omega)
    have h2 : 0 < rowHook q j t i - 1 := rowHook_sub_one_pos (by omega)
    have : 1 - 1 / rowHook q j t i = (rowHook q j t i - 1) / rowHook q j t i := by field_simp
    rw [this]
    positivity
  rw [p0Hook_eq_prod hj hq hcol, Finset.prod_congr rfl hfac, Finset.prod_inv_distrib,
    hsplit, htail]
  have hqne : (q : ℝ) ≠ 0 := ne_of_gt hqpos
  have hsne : (q : ℝ) - (j : ℝ) - (L : ℝ) ≠ 0 := ne_of_gt hLcast
  have hPne : (∏ i ∈ Finset.range L, (1 - 1 / rowHook q j t i)) ≠ 0 := ne_of_gt hPpos
  field_simp

end Reduce

/-! ## The two-sided range of paper eq:omega-range -/

section Range

variable {q j L : ℕ} {t : ℕ → ℕ}

/-- The first telescoping majorant, from `θ'_c ≥ 1`:
`∏_{c≤θ₁}(1-1/h_c) ≥ (A-θ₁+1)/(A+1)`, `A = q-j`. -/
theorem prod_ge_lower (hj : 1 ≤ j) (hq : 6 * j ≤ q) (hcol : IsColumnData L t j) :
    ((q : ℝ) - (j : ℝ) - (L : ℝ) + 1) / ((q : ℝ) - (j : ℝ) + 1)
      ≤ ∏ i ∈ Finset.range L, (1 - 1 / rowHook q j t i) := by
  have hLj : L ≤ j := hcol.length_le
  set g : ℕ → ℝ := fun i => (q : ℝ) - (j : ℝ) - (i : ℝ) + 1 with hg
  have hgpos : ∀ i, i ≤ L → 0 < g i := by
    intro i hi
    have h1 : (i : ℝ) ≤ (L : ℝ) := by exact_mod_cast hi
    have h2 : (L : ℝ) + 1 ≤ (q : ℝ) - (j : ℝ) := by
      have h3 : L + 1 + j ≤ q := by omega
      have h4 : ((L + 1 + j : ℕ) : ℝ) ≤ (q : ℝ) := by exact_mod_cast h3
      push_cast at h4
      linarith
    simp only [hg]
    linarith
  have hterm : ∀ i ∈ Finset.range L, g (i + 1) / g i ≤ 1 - 1 / rowHook q j t i := by
    intro i hi
    have hi' : i < L := Finset.mem_range.mp hi
    have hgi : 0 < g i := hgpos i (by omega)
    have hgi1 : g (i + 1) = g i - 1 := by simp only [hg]; push_cast; ring
    have h1 : 0 < rowHook q j t i := rowHook_pos (by omega)
    have hti : (1 : ℝ) ≤ (t i : ℝ) := by exact_mod_cast hcol.pos i hi'
    have hrow : g i ≤ rowHook q j t i := by
      simp only [hg, rowHook]
      linarith
    have hinv : 1 / rowHook q j t i ≤ 1 / g i := by
      rw [div_le_div_iff₀ h1 hgi]
      linarith
    have : g (i + 1) / g i = 1 - 1 / g i := by
      rw [hgi1]
      field_simp
    rw [this]
    linarith
  have hnn : ∀ i ∈ Finset.range L, (0 : ℝ) ≤ g (i + 1) / g i := by
    intro i hi
    have hi' : i < L := Finset.mem_range.mp hi
    have hgi : 0 < g i := hgpos i (by omega)
    have hgi1 : 0 < g (i + 1) := hgpos (i + 1) (by omega)
    positivity
  calc ((q : ℝ) - (j : ℝ) - (L : ℝ) + 1) / ((q : ℝ) - (j : ℝ) + 1)
      = g L / g 0 := by simp [hg]
    _ = ∏ i ∈ Finset.range L, (g (i + 1) / g i) :=
        (prod_range_ratio' fun i hi => ne_of_gt (hgpos i hi)).symm
    _ ≤ ∏ i ∈ Finset.range L, (1 - 1 / rowHook q j t i) := Finset.prod_le_prod hnn hterm

/-- The second telescoping majorant, from `θ'_c ≤ θ'_1 = a`:
`∏_{c≤θ₁}(1-1/h_c) ≤ (A+a-θ₁)/(A+a)`, `A = q-j`. -/
theorem prod_le_upper (hj : 1 ≤ j) (hq : 6 * j ≤ q) (hcol : IsColumnData L t j) :
    (∏ i ∈ Finset.range L, (1 - 1 / rowHook q j t i))
      ≤ ((q : ℝ) - (j : ℝ) + (t 0 : ℝ) - (L : ℝ)) / ((q : ℝ) - (j : ℝ) + (t 0 : ℝ)) := by
  have hLj : L ≤ j := hcol.length_le
  set g : ℕ → ℝ := fun i => (q : ℝ) - (j : ℝ) + (t 0 : ℝ) - (i : ℝ) with hg
  have hL1 : (L : ℝ) + 1 ≤ (q : ℝ) - (j : ℝ) := by
    have h3 : L + 1 + j ≤ q := by omega
    have h4 : ((L + 1 + j : ℕ) : ℝ) ≤ (q : ℝ) := by exact_mod_cast h3
    push_cast at h4
    linarith
  have ht0 : (0 : ℝ) ≤ (t 0 : ℝ) := Nat.cast_nonneg _
  have hgpos : ∀ i, i ≤ L → 0 < g i := by
    intro i hi
    have h1 : (i : ℝ) ≤ (L : ℝ) := by exact_mod_cast hi
    simp only [hg]
    linarith
  have hterm : ∀ i ∈ Finset.range L, 1 - 1 / rowHook q j t i ≤ g (i + 1) / g i := by
    intro i hi
    have hi' : i < L := Finset.mem_range.mp hi
    have hgi : 0 < g i := hgpos i (by omega)
    have hgi1 : g (i + 1) = g i - 1 := by simp only [hg]; push_cast; ring
    have h1 : 0 < rowHook q j t i := rowHook_pos (by omega)
    have hti : (t i : ℝ) ≤ (t 0 : ℝ) := by exact_mod_cast hcol.le_head i
    have hrow : rowHook q j t i ≤ g i := by
      simp only [hg, rowHook]
      linarith
    have hinv : 1 / g i ≤ 1 / rowHook q j t i := by
      rw [div_le_div_iff₀ hgi h1]
      linarith
    have : g (i + 1) / g i = 1 - 1 / g i := by
      rw [hgi1]
      field_simp
    rw [this]
    linarith
  have hnn : ∀ i ∈ Finset.range L, (0 : ℝ) ≤ 1 - 1 / rowHook q j t i := by
    intro i hi
    have hi' : i < L := Finset.mem_range.mp hi
    have h1 : 0 < rowHook q j t i := rowHook_pos (by omega)
    have h2 : 0 < rowHook q j t i - 1 := rowHook_sub_one_pos (by omega)
    have heq : 1 - 1 / rowHook q j t i = (rowHook q j t i - 1) / rowHook q j t i := by field_simp
    rw [heq]
    positivity
  calc (∏ i ∈ Finset.range L, (1 - 1 / rowHook q j t i))
      ≤ ∏ i ∈ Finset.range L, (g (i + 1) / g i) := Finset.prod_le_prod hnn hterm
    _ = g L / g 0 := prod_range_ratio' fun i hi => ne_of_gt (hgpos i hi)
    _ = ((q : ℝ) - (j : ℝ) + (t 0 : ℝ) - (L : ℝ)) / ((q : ℝ) - (j : ℝ) + (t 0 : ℝ)) := by
        simp [hg]

/-- `ω = q/(q-j-θ₁)·∏_{c≤θ₁}(1-1/h_c) - 1`: the reduced form of `ω` itself. -/
theorem omegaHook_eq (hj : 1 ≤ j) (hq : 6 * j ≤ q) (hcol : IsColumnData L t j) :
    omegaHook q j t
      = (q : ℝ) / ((q : ℝ) - (j : ℝ) - (L : ℝ))
          * (∏ i ∈ Finset.range L, (1 - 1 / rowHook q j t i)) - 1 := by
  have hqpos : (0 : ℝ) < (q : ℝ) := by
    have : 0 < q := by omega
    exact_mod_cast this
  have hLcast : (0 : ℝ) < (q : ℝ) - (j : ℝ) - (L : ℝ) := by
    have h2 : L + 1 + j ≤ q := by
      have := hcol.length_le
      omega
    have h3 : ((L + 1 + j : ℕ) : ℝ) ≤ (q : ℝ) := by exact_mod_cast h2
    push_cast at h3
    linarith
  have hPpos : 0 < ∏ i ∈ Finset.range L, (1 - 1 / rowHook q j t i) := by
    refine Finset.prod_pos fun i hi => ?_
    have hi' : i < L := Finset.mem_range.mp hi
    have hLj := hcol.length_le
    have h1 : 0 < rowHook q j t i := rowHook_pos (by omega)
    have h2 : 0 < rowHook q j t i - 1 := rowHook_sub_one_pos (by omega)
    have heq : 1 - 1 / rowHook q j t i = (rowHook q j t i - 1) / rowHook q j t i := by field_simp
    rw [heq]
    positivity
  have hXpos : 0 < (q : ℝ) / ((q : ℝ) - (j : ℝ) - (L : ℝ))
      * ∏ i ∈ Finset.range L, (1 - 1 / rowHook q j t i) := by positivity
  have hgen : ∀ X : ℝ, X ≠ 0 → (1 - 1 / X) / (1 / X) = X - 1 := by
    intro X hX
    field_simp
  simp only [omegaHook, p0Hook_eq_inv hj hq hcol]
  exact hgen _ (ne_of_gt hXpos)

/-- **The lower half of eq:omega-range**: `j/q ≤ ω`. -/
theorem le_omegaHook (hj : 1 ≤ j) (hq : 6 * j ≤ q) (hcol : IsColumnData L t j) :
    (j : ℝ) / (q : ℝ) ≤ omegaHook q j t := by
  have hqpos : (0 : ℝ) < (q : ℝ) := by
    have : 0 < q := by omega
    exact_mod_cast this
  have hLj : L ≤ j := hcol.length_le
  have hjr : (1 : ℝ) ≤ (j : ℝ) := by exact_mod_cast hj
  have hqr : 6 * (j : ℝ) ≤ (q : ℝ) := by
    have : ((6 * j : ℕ) : ℝ) ≤ (q : ℝ) := by exact_mod_cast hq
    push_cast at this
    linarith
  have hL1 : (1 : ℝ) ≤ (L : ℝ) := by
    have := one_le_length hj hcol
    exact_mod_cast this
  have hLub : (L : ℝ) ≤ (j : ℝ) := by exact_mod_cast hLj
  have hs1 : (1 : ℝ) ≤ (q : ℝ) - (j : ℝ) - (L : ℝ) := by linarith
  have hsA : (q : ℝ) - (j : ℝ) - (L : ℝ) ≤ (q : ℝ) - (j : ℝ) - 1 := by linarith
  have hA1 : (0 : ℝ) < (q : ℝ) - (j : ℝ) + 1 := by linarith
  -- the majorant
  have hstep : ((q : ℝ) / ((q : ℝ) - (j : ℝ) - (L : ℝ)))
        * (((q : ℝ) - (j : ℝ) - (L : ℝ) + 1) / ((q : ℝ) - (j : ℝ) + 1))
      ≤ ((q : ℝ) / ((q : ℝ) - (j : ℝ) - (L : ℝ)))
        * ∏ i ∈ Finset.range L, (1 - 1 / rowHook q j t i) :=
    mul_le_mul_of_nonneg_left (prod_ge_lower hj hq hcol) (by positivity)
  -- the polynomial core
  have hcore : ((j : ℝ) / (q : ℝ) + 1)
      ≤ ((q : ℝ) / ((q : ℝ) - (j : ℝ) - (L : ℝ)))
        * (((q : ℝ) - (j : ℝ) - (L : ℝ) + 1) / ((q : ℝ) - (j : ℝ) + 1)) := by
    rw [div_add' _ _ _ (ne_of_gt hqpos), div_mul_div_comm,
      div_le_div_iff₀ hqpos (by positivity)]
    have hc := omega_lower_core (s := (q : ℝ) - (j : ℝ) - (L : ℝ)) hjr hqr hs1 hsA
    nlinarith [hc]
  rw [omegaHook_eq hj hq hcol]
  linarith

/-- **The upper half of eq:omega-range**: `ω ≤ j/(q-2j)`. -/
theorem omegaHook_le (hj : 1 ≤ j) (hq : 6 * j ≤ q) (hcol : IsColumnData L t j) :
    omegaHook q j t ≤ (j : ℝ) / ((q : ℝ) - 2 * (j : ℝ)) := by
  have hqpos : (0 : ℝ) < (q : ℝ) := by
    have : 0 < q := by omega
    exact_mod_cast this
  have hLj : L ≤ j := hcol.length_le
  have hjr : (1 : ℝ) ≤ (j : ℝ) := by exact_mod_cast hj
  have hqr : 6 * (j : ℝ) ≤ (q : ℝ) := by
    have : ((6 * j : ℕ) : ℝ) ≤ (q : ℝ) := by exact_mod_cast hq
    push_cast at this
    linarith
  have hL1 : (1 : ℝ) ≤ (L : ℝ) := by
    have := one_le_length hj hcol
    exact_mod_cast this
  have hLub : (L : ℝ) ≤ (j : ℝ) := by exact_mod_cast hLj
  have ha1 : (1 : ℝ) ≤ (t 0 : ℝ) := by
    have := hcol.pos 0 (one_le_length hj hcol)
    exact_mod_cast this
  have haL : (t 0 : ℝ) + (L : ℝ) ≤ (j : ℝ) + 1 := by
    have := hcol.head_add_length_le (one_le_length hj hcol)
    have hc : ((t 0 + L : ℕ) : ℝ) ≤ ((j + 1 : ℕ) : ℝ) := by exact_mod_cast this
    push_cast at hc
    linarith
  have hA5 : 5 * (j : ℝ) ≤ (q : ℝ) - (j : ℝ) := by linarith
  have hs1 : (1 : ℝ) ≤ (q : ℝ) - (j : ℝ) - (L : ℝ) := by linarith
  have hBpos : (0 : ℝ) < (q : ℝ) - (j : ℝ) + (t 0 : ℝ) := by linarith
  have hqj2 : (0 : ℝ) < (q : ℝ) - 2 * (j : ℝ) := by linarith
  -- the majorant
  have hstep : ((q : ℝ) / ((q : ℝ) - (j : ℝ) - (L : ℝ)))
        * ∏ i ∈ Finset.range L, (1 - 1 / rowHook q j t i)
      ≤ ((q : ℝ) / ((q : ℝ) - (j : ℝ) - (L : ℝ)))
        * (((q : ℝ) - (j : ℝ) + (t 0 : ℝ) - (L : ℝ)) / ((q : ℝ) - (j : ℝ) + (t 0 : ℝ))) :=
    mul_le_mul_of_nonneg_left (prod_le_upper hj hq hcol) (by positivity)
  -- the polynomial core
  have hcore : ((q : ℝ) / ((q : ℝ) - (j : ℝ) - (L : ℝ)))
        * (((q : ℝ) - (j : ℝ) + (t 0 : ℝ) - (L : ℝ)) / ((q : ℝ) - (j : ℝ) + (t 0 : ℝ)))
      ≤ (j : ℝ) / ((q : ℝ) - 2 * (j : ℝ)) + 1 := by
    rw [div_add' _ _ _ (ne_of_gt hqj2), div_mul_div_comm,
      div_le_div_iff₀ (by positivity) hqj2]
    have hc := omega_upper_core (A := (q : ℝ) - (j : ℝ)) (a := (t 0 : ℝ)) (L := (L : ℝ))
      (j := (j : ℝ)) ha1 hL1 haL hA5
    nlinarith [hc]
  rw [omegaHook_eq hj hq hcol]
  linarith

/-- **`0 < ω`** on the window — the field `Cited.omega_pos`, from the lower half of the range. -/
theorem omegaHook_pos (hj : 1 ≤ j) (hq : 6 * j ≤ q) (hcol : IsColumnData L t j) :
    0 < omegaHook q j t := by
  have hqpos : (0 : ℝ) < (q : ℝ) := by
    have : 0 < q := by omega
    exact_mod_cast this
  have hjr : (1 : ℝ) ≤ (j : ℝ) := by exact_mod_cast hj
  have h : (0 : ℝ) < (j : ℝ) / (q : ℝ) := by positivity
  exact lt_of_lt_of_le h (le_omegaHook hj hq hcol)

end Range

end SE
