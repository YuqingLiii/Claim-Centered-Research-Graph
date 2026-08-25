/-
`SE/Support/Hook.lean` — non-node support module.  TIER 2.

Node served: `SE.formal.t2` (`se/proof-dag/nodes/SE.formal.t2.yaml`).
Nodes whose tier-1 CITED fields this file discharges (≥ 2, which is why this is `Support/` and
not a node module): `SE.denom.assembly.envelope` (the hook envelope `ρ_d = 1 + O(n^{-1/3})`,
paper eq:rho-asymp, previously `Cited.rho_ge_one` / `Cited.rho_le`), and, through
`SE/Interface.lean`, `SE.denom` and `SE.denom.Phi.legal.tame`, which consume the envelope.

WHAT THIS FILE IS.  Tier 1 carried the hook envelope as an ASSUMPTION about an abstract real
`F.rho`.  Tier 2 replaces that assumption by ARITHMETIC: `r_top` is DEFINED here by the explicit
hook product of the manuscript's eq:rtop, and the envelope is then proved.

  `r_top(q,d,θ) = q^d f^θ / (d! f^{(q-d,θ)})`            (paper eq:rtop)
                = q^d/(q)_d · ∏_{c=1}^{θ₁} (1 + θ'_c/(q-d-c+1))   (hook-length formula)

The second line is `SE.rtopHook` below, written in the CONJUGATE coordinates `t i = θ'_{i+1}`
(`IsColumnData`).  The identity between the two lines is the Frame–Robinson–Thrall hook-length
formula applied to `λ = (q-d,θ)`, whose first-row hooks are `q-d-c+1+θ'_c` and whose remaining
hooks are exactly the hooks of `θ`; it is the ONE external fact this tier cites, and it enters
`SE/Interface.lean` as the single field `Cited.rho_isGreatest` (nothing quantitative is assumed
there; tier 2b sharpened tier 2a's `Cited.rho_hook` into the `IsGreatest` form).

TRUST.  No `sorry`, no `axiom`, no `native_decide`.  Mathlib v4.31.0 has `YoungDiagram` but no
hook-length formula, no Specht modules and no Littlewood–Richardson rule, so the hook-length
formula cannot be proved here; it is cited, and every consequence of it below is proved.
-/
import SE.Support.Defs
import SE.Support.Cbrt
import SE.Support.Telescope

namespace SE

/-! ## Shapes in conjugate coordinates

A partition `θ ⊢ d` enters the hook product only through its conjugate `θ'` and its first row
length `θ₁`.  `IsColumnData L t d` says: `t i = θ'_{i+1}` for `i < L`, `L = θ₁`.  The three facts
used below — positivity, `Σ θ'_c = d`, and `θ'_c ≤ θ'_1` — hold for the conjugate of every
partition, so nothing about the shape is assumed beyond what a shape is. -/

/-- The conjugate coordinates of a partition `θ ⊢ d` with first row `θ₁ = L`:
`t i = θ'_{i+1}` for `i < L` and `t i = 0` beyond. -/
structure IsColumnData (L : ℕ) (t : ℕ → ℕ) (d : ℕ) : Prop where
  /-- Every column of `θ` inside the first row is nonempty. -/
  pos : ∀ i, i < L → 1 ≤ t i
  /-- There is no column beyond the first row. -/
  vanish : ∀ i, L ≤ i → t i = 0
  /-- `θ'` is non-increasing, so every column is at most as tall as the first. -/
  le_head : ∀ i, t i ≤ t 0
  /-- `θ` has `d` boxes. -/
  sum_eq : ∑ i ∈ Finset.range L, t i = d

namespace IsColumnData

variable {L : ℕ} {t : ℕ → ℕ} {d : ℕ}

/-- `θ₁ ≤ d`: the first row of a partition of `d` has at most `d` boxes. -/
theorem length_le (h : IsColumnData L t d) : L ≤ d := by
  have hle : ∑ _i ∈ Finset.range L, 1 ≤ ∑ i ∈ Finset.range L, t i :=
    Finset.sum_le_sum fun i hi => h.pos i (Finset.mem_range.mp hi)
  rw [h.sum_eq] at hle
  simpa using hle

/-- `θ'_1 ≤ d`: the first column of a partition of `d` has at most `d` boxes. -/
theorem head_le (h : IsColumnData L t d) : t 0 ≤ d := by
  rcases Nat.eq_zero_or_pos L with rfl | hL
  · simp [h.vanish 0 (le_refl 0)]
  · have hmem : 0 ∈ Finset.range L := Finset.mem_range.mpr hL
    have := Finset.single_le_sum (f := t) (fun i _ => Nat.zero_le (t i)) hmem
    simpa [h.sum_eq] using this

/-- `d ≤ θ₁ · θ'_1`: a partition of `d` fits in its bounding rectangle. -/
theorem le_length_mul_head (h : IsColumnData L t d) : d ≤ L * t 0 := by
  have : ∑ i ∈ Finset.range L, t i ≤ ∑ _i ∈ Finset.range L, t 0 :=
    Finset.sum_le_sum fun i _ => h.le_head i
  simpa [h.sum_eq, Finset.sum_const, mul_comm] using this

/-- `θ'_1 + θ₁ ≤ d + 1`: the first row and the first column of a partition of `d` overlap in
exactly one box. -/
theorem head_add_length_le (h : IsColumnData L t d) (hL : 1 ≤ L) : t 0 + L ≤ d + 1 := by
  have hsplit : ∑ i ∈ Finset.range L, t i
      = t 0 + ∑ i ∈ Finset.Ico 1 L, t i := by
    rw [Finset.range_eq_Ico, ← Finset.sum_eq_sum_Ico_succ_bot hL]
  have hlow : ∑ _i ∈ Finset.Ico 1 L, 1 ≤ ∑ i ∈ Finset.Ico 1 L, t i :=
    Finset.sum_le_sum fun i hi => h.pos i (Finset.mem_Ico.mp hi).2
  have hcard : ∑ _i ∈ Finset.Ico 1 L, 1 = L - 1 := by
    simp [Finset.sum_const, Nat.card_Ico]
  rw [hcard] at hlow
  have := h.sum_eq
  rw [hsplit] at this
  omega

end IsColumnData

/-! ## The explicit hook product `r_top`

`rtopHook q d L t` is the right-hand side of eq:rtop after the hook-length formula:
`q^d/(q)_d · ∏_{c=1}^{θ₁}(1 + θ'_c/(q-d-c+1))`, in the conjugate coordinates `t i = θ'_{i+1}`
(so the `c`-th factor is the `i = c-1` factor and `q-d-c+1 = q-d-i`). -/

/-- **The explicit hook product** of paper eq:rtop,
`r_top(q,d,θ) = q^d/(q)_d · ∏_{c=1}^{θ₁}(1 + θ'_c/(q-d-c+1))`.  `(q)_d` is
`Nat.descFactorial q d = q(q-1)⋯(q-d+1)`. -/
noncomputable def rtopHook (q d L : ℕ) (t : ℕ → ℕ) : ℝ :=
  (q : ℝ) ^ d / (q.descFactorial d : ℝ) *
    ∏ i ∈ Finset.range L, (1 + (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ)))

/-- `(q)_d = ∏_{i<d}(q-i)` over `ℝ`, for `d ≤ q`. -/
theorem cast_descFactorial_eq_prod {q d : ℕ} (h : d ≤ q) :
    ((q.descFactorial d : ℕ) : ℝ) = ∏ i ∈ Finset.range d, ((q : ℝ) - (i : ℝ)) := by
  induction d with
  | zero => simp
  | succ m ih =>
      have hm : m ≤ q := le_trans (Nat.le_succ m) h
      have hcast : ((q - m : ℕ) : ℝ) = (q : ℝ) - (m : ℝ) := by
        push_cast [Nat.cast_sub hm]; ring
      rw [Nat.descFactorial_succ, Finset.prod_range_succ, ← ih hm, Nat.cast_mul, hcast]
      ring

/-- The rising-factorial factor of `r_top`, as a product: `q^d/(q)_d = ∏_{i<d} q/(q-i)`. -/
theorem rise_eq_prod {q d : ℕ} (h : d ≤ q) :
    (q : ℝ) ^ d / (q.descFactorial d : ℝ)
      = ∏ i ∈ Finset.range d, ((q : ℝ) / ((q : ℝ) - (i : ℝ))) := by
  rw [Finset.prod_div_distrib, cast_descFactorial_eq_prod h, Finset.prod_const,
    Finset.card_range]

/-! ### Positivity of the factors on the window `2d < q` -/

section Window

variable {q d L : ℕ} {t : ℕ → ℕ}

theorem rise_den_pos (hq : 2 * d < q) {i : ℕ} (hi : i < d) : (0 : ℝ) < (q : ℝ) - (i : ℝ) := by
  have h1 : (i : ℝ) < (q : ℝ) := by
    have : i < q := by omega
    exact_mod_cast this
  linarith

theorem hook_den_pos (hq : 2 * d < q) (hL : L ≤ d) {i : ℕ} (hi : i < L) :
    (0 : ℝ) < (q : ℝ) - (d : ℝ) - (i : ℝ) := by
  have h : (i : ℝ) + (d : ℝ) < (q : ℝ) := by
    have : i + d < q := by omega
    exact_mod_cast this
  linarith

theorem one_le_rise_factor (hq : 2 * d < q) {i : ℕ} (hi : i < d) :
    (1 : ℝ) ≤ (q : ℝ) / ((q : ℝ) - (i : ℝ)) := by
  have hden := rise_den_pos hq hi
  rw [le_div_iff₀ hden]
  have : (0 : ℝ) ≤ (i : ℝ) := Nat.cast_nonneg i
  linarith

theorem one_le_hook_factor (hq : 2 * d < q) (hL : L ≤ d) {i : ℕ} (hi : i < L) :
    (1 : ℝ) ≤ 1 + (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ)) := by
  have hden := hook_den_pos hq hL hi
  have : (0 : ℝ) ≤ (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ)) :=
    div_nonneg (Nat.cast_nonneg _) hden.le
  linarith

/-- **`1 ≤ r_top`** — the lower half of paper eq:rho-asymp, at the level of a single shape.
Every factor of the hook product is `≥ 1`. -/
theorem one_le_rtopHook (hq : 2 * d < q) (hL : L ≤ d) : (1 : ℝ) ≤ rtopHook q d L t := by
  have hdq : d ≤ q := by omega
  have h1 : (1 : ℝ) ≤ ∏ i ∈ Finset.range d, ((q : ℝ) / ((q : ℝ) - (i : ℝ))) := by
    calc (1 : ℝ) = ∏ _i ∈ Finset.range d, (1 : ℝ) := by simp
      _ ≤ _ := Finset.prod_le_prod (fun i _ => zero_le_one)
              (fun i hi => one_le_rise_factor hq (Finset.mem_range.mp hi))
  have h2 : (1 : ℝ) ≤ ∏ i ∈ Finset.range L, (1 + (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ))) := by
    calc (1 : ℝ) = ∏ _i ∈ Finset.range L, (1 : ℝ) := by simp
      _ ≤ _ := Finset.prod_le_prod (fun i _ => zero_le_one)
              (fun i hi => one_le_hook_factor hq hL (Finset.mem_range.mp hi))
  rw [rtopHook, rise_eq_prod hdq]
  nlinarith

theorem rtopHook_pos (hq : 2 * d < q) (hL : L ≤ d) : (0 : ℝ) < rtopHook q d L t :=
  lt_of_lt_of_le zero_lt_one (one_le_rtopHook hq hL)

end Window

/-! ## The maximizing shape — `ρ_d = max_{θ⊢d} r_top(2n,d,θ)` is attained at the single row

TIER 2b (2026-08-17, node `SE.formal.t2` frontier task-004).  Paper eq:rtop DEFINES `ρ_d` as a
maximum over the partitions of `d`.  Tier 2a assumed only that the maximum is attained somewhere
(`Cited.rho_hook`, existence form); the field `Cited.rtop_le_rho` — "`r_top(2n,j,θ) ≤ ρ_j` for the
sector's own shape" — needs the OTHER half, that `ρ_d` dominates EVERY shape.  Both halves together
are `IsGreatest`, and they are available here as arithmetic, because the maximizer is explicit:

  `∏_{c=1}^{θ₁}(1 + θ'_c/(q-d-c+1)) ≤ (q-d+1)/(q-2d+1) = ∏_{c=1}^{d}(1 + 1/(q-d-c+1))`,

the right-hand side being the single row `θ = (d)` (conjugate `θ' = (1,…,1)`).  The proof is one
telescoping majorant: with `A = q-d` and the partial sums `S_i = θ'_1+…+θ'_i`,

  `1 + θ'_{i+1}/(A-i) ≤ (A-S_i+1)/(A-S_{i+1}+1)`,

which holds because `S_{i+1} ≥ i+1` (every column inside the first row is nonempty), and the
right-hand side telescopes to `(A+1)/(A-d+1)` since `S_0 = 0` and `S_{θ₁} = d`.  No lossy step. -/

/-- The single-row shape `θ = (d)` in conjugate coordinates: `θ'_c = 1` for `c ≤ d`.  It is the
maximizer of the hook product (`SE.rtopHook_le_rowShape`). -/
def rowShape (d : ℕ) : ℕ → ℕ := fun i => if i < d then 1 else 0

theorem rowShape_isColumnData (d : ℕ) : IsColumnData d (rowShape d) d where
  pos := by intro i hi; simp [rowShape, hi]
  vanish := by
    intro i hi
    simp only [rowShape]
    rw [if_neg (by omega : ¬ i < d)]
  le_head := by
    intro i
    rcases Nat.eq_zero_or_pos d with rfl | hd
    · simp [rowShape]
    · simp only [rowShape, if_pos hd]
      split_ifs <;> simp
  sum_eq := by
    rw [Finset.sum_congr rfl
      (fun i hi => by simp only [rowShape]; rw [if_pos (Finset.mem_range.mp hi)])]
    simp

section Row

variable {q d L : ℕ} {t : ℕ → ℕ}

/-- The single row's own hook product, telescoped:
`∏_{i<d}(1 + 1/(q-d-i)) = (q-d+1)/(q-2d+1)`. -/
theorem prod_rowShape (hq : 2 * d < q) :
    ∏ i ∈ Finset.range d, (1 + ((rowShape d i : ℕ) : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ)))
      = ((q : ℝ) - (d : ℝ) + 1) / ((q : ℝ) - 2 * (d : ℝ) + 1) := by
  have hd2 : (0 : ℝ) < (q : ℝ) - 2 * (d : ℝ) + 1 := by
    have h : ((2 * d : ℕ) : ℝ) < (q : ℝ) := by exact_mod_cast hq
    push_cast at h; linarith
  set f : ℕ → ℝ := fun i => (q : ℝ) - (d : ℝ) - (i : ℝ) + 1 with hf
  have hfpos : ∀ i, i ≤ d → 0 < f i := by
    intro i hi
    have hid : (i : ℝ) ≤ (d : ℝ) := by exact_mod_cast hi
    simp only [hf]
    linarith
  have hstep : ∀ i ∈ Finset.range d,
      (1 + ((rowShape d i : ℕ) : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ))) = f i / f (i + 1) := by
    intro i hi
    have hi' : i < d := Finset.mem_range.mp hi
    have hden : (0 : ℝ) < (q : ℝ) - (d : ℝ) - (i : ℝ) := by
      have : (i : ℝ) + 1 ≤ (d : ℝ) := by exact_mod_cast (by omega : i + 1 ≤ d)
      linarith
    have hfi1 : f (i + 1) = (q : ℝ) - (d : ℝ) - (i : ℝ) := by
      simp only [hf]; push_cast; ring
    have hrow : ((rowShape d i : ℕ) : ℝ) = 1 := by
      simp only [rowShape, if_pos hi']; norm_num
    rw [hfi1, hrow]
    simp only [hf]
    field_simp
  rw [Finset.prod_congr rfl hstep, prod_range_ratio fun i hi => ne_of_gt (hfpos i hi)]
  simp only [hf, Nat.cast_zero, sub_zero]
  rw [show (q : ℝ) - (d : ℝ) - (d : ℝ) + 1 = (q : ℝ) - 2 * (d : ℝ) + 1 from by ring]

/-- **The hook product is maximized by the single row** — the telescoping majorant described in the
section header. -/
theorem prod_le_prod_rowShape (hq : 2 * d < q) (hcol : IsColumnData L t d) :
    ∏ i ∈ Finset.range L, (1 + (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ)))
      ≤ ((q : ℝ) - (d : ℝ) + 1) / ((q : ℝ) - 2 * (d : ℝ) + 1) := by
  have hL : L ≤ d := hcol.length_le
  have hd2 : (0 : ℝ) < (q : ℝ) - 2 * (d : ℝ) + 1 := by
    have h : ((2 * d : ℕ) : ℝ) < (q : ℝ) := by exact_mod_cast hq
    push_cast at h; linarith
  -- the partial sums `S_i` of the conjugate shape
  have hpsum_le : ∀ i, i ≤ L → (∑ k ∈ Finset.range i, t k) ≤ d := by
    intro i hi
    calc (∑ k ∈ Finset.range i, t k) ≤ ∑ k ∈ Finset.range L, t k :=
          Finset.sum_le_sum_of_subset
            (fun x hx => Finset.mem_range.mpr (lt_of_lt_of_le (Finset.mem_range.mp hx) hi))
      _ = d := hcol.sum_eq
  have hpsum_ge : ∀ i, i ≤ L → i ≤ ∑ k ∈ Finset.range i, t k := by
    intro i hi
    have : ∑ _k ∈ Finset.range i, 1 ≤ ∑ k ∈ Finset.range i, t k :=
      Finset.sum_le_sum fun k hk => hcol.pos k (lt_of_lt_of_le (Finset.mem_range.mp hk) hi)
    simpa using this
  set g : ℕ → ℝ :=
    fun i => (q : ℝ) - (d : ℝ) - ((∑ k ∈ Finset.range i, t k : ℕ) : ℝ) + 1 with hg
  have hgpos : ∀ i, i ≤ L → 0 < g i := by
    intro i hi
    have h1 : ((∑ k ∈ Finset.range i, t k : ℕ) : ℝ) ≤ (d : ℝ) := by
      exact_mod_cast hpsum_le i hi
    simp only [hg]
    linarith
  have hterm : ∀ i ∈ Finset.range L,
      (1 + (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ))) ≤ g i / g (i + 1) := by
    intro i hi
    have hi' : i < L := Finset.mem_range.mp hi
    have hB : (0 : ℝ) < (q : ℝ) - (d : ℝ) - (i : ℝ) := by
      have : (i : ℝ) + 1 ≤ (d : ℝ) := by exact_mod_cast (by omega : i + 1 ≤ d)
      linarith
    have hg1 : 0 < g (i + 1) := hgpos (i + 1) (by omega)
    have hS1 : (i : ℝ) + 1 ≤ ((∑ k ∈ Finset.range (i + 1), t k : ℕ) : ℝ) :=
      calc (i : ℝ) + 1 = ((i + 1 : ℕ) : ℝ) := by push_cast; ring
        _ ≤ ((∑ k ∈ Finset.range (i + 1), t k : ℕ) : ℝ) :=
            Nat.cast_le.mpr (hpsum_ge (i + 1) (by omega))
    have hgle : g (i + 1) ≤ (q : ℝ) - (d : ℝ) - (i : ℝ) := by
      simp only [hg]; linarith
    have hdiff : g i - g (i + 1) = (t i : ℝ) := by
      simp only [hg, Finset.sum_range_succ]
      push_cast
      ring
    have hu : (0 : ℝ) ≤ (t i : ℝ) := Nat.cast_nonneg _
    have hkey : (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ)) * g (i + 1) ≤ (t i : ℝ) := by
      rw [div_mul_eq_mul_div, div_le_iff₀ hB]
      nlinarith
    have hexp : (1 + (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ))) * g (i + 1)
        = g (i + 1) + (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ)) * g (i + 1) := by ring
    rw [le_div_iff₀ hg1, hexp]
    linarith
  have hnn : ∀ i ∈ Finset.range L,
      (0 : ℝ) ≤ 1 + (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ)) := by
    intro i hi
    have hi' : i < L := Finset.mem_range.mp hi
    have hB : (0 : ℝ) < (q : ℝ) - (d : ℝ) - (i : ℝ) := by
      have : (i : ℝ) + 1 ≤ (d : ℝ) := by exact_mod_cast (by omega : i + 1 ≤ d)
      linarith
    have : (0 : ℝ) ≤ (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ)) :=
      div_nonneg (Nat.cast_nonneg _) hB.le
    linarith
  calc ∏ i ∈ Finset.range L, (1 + (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ)))
      ≤ ∏ i ∈ Finset.range L, (g i / g (i + 1)) := Finset.prod_le_prod hnn hterm
    _ = g 0 / g L := prod_range_ratio fun i hi => ne_of_gt (hgpos i hi)
    _ = ((q : ℝ) - (d : ℝ) + 1) / ((q : ℝ) - 2 * (d : ℝ) + 1) := by
        have h0 : g 0 = (q : ℝ) - (d : ℝ) + 1 := by simp [hg]
        have hLL : g L = (q : ℝ) - 2 * (d : ℝ) + 1 := by
          simp only [hg, hcol.sum_eq]; ring
        rw [h0, hLL]

/-- **`r_top(q,d,θ) ≤ r_top(q,d,(d))` for every shape `θ ⊢ d`** on the window `2d < q`. -/
theorem rtopHook_le_rowShape (hq : 2 * d < q) (hcol : IsColumnData L t d) :
    rtopHook q d L t ≤ rtopHook q d d (rowShape d) := by
  have hpre : (0 : ℝ) ≤ (q : ℝ) ^ d / (q.descFactorial d : ℝ) := by positivity
  simp only [rtopHook]
  rw [prod_rowShape hq]
  exact mul_le_mul_of_nonneg_left (prod_le_prod_rowShape hq hcol) hpre

end Row

/-- `ρ_d` of paper eq:rtop, evaluated: the maximum of the explicit hook product over the shapes of
`d` (attained at the single row, `SE.rtopHook_le_rowShape`). -/
noncomputable def rhoHook (n d : ℕ) : ℝ := rtopHook (2 * n) d d (rowShape d)

/-- The set whose maximum paper eq:rtop calls `ρ_d = max_{θ⊢d} r_top(2n,d,θ)`, written in the
conjugate coordinates of `SE.IsColumnData`. -/
def rtopHookSet (n d : ℕ) : Set ℝ :=
  {r | ∃ (L : ℕ) (t : ℕ → ℕ), IsColumnData L t d ∧ r = rtopHook (2 * n) d L t}

/-- **`ρ_d` is a genuine maximum** — `IsGreatest`, i.e. both the attainment tier 2a assumed and the
domination `Cited.rtop_le_rho` needs, for every `d < n`. -/
theorem isGreatest_rtopHookSet {n d : ℕ} (hd : d < n) :
    IsGreatest (rtopHookSet n d) (rhoHook n d) := by
  refine ⟨⟨d, rowShape d, rowShape_isColumnData d, rfl⟩, ?_⟩
  rintro r ⟨L, t, hcol, rfl⟩
  exact rtopHook_le_rowShape (by omega) hcol

/-! ## The one-defect completion identity `r_{j+1}(λ) = j·r_top(q,j,θ)`

Paper `lem:phi-diag`, the display after eq:rd: with `λ = (q-j,θ)` and `q-j > θ₁`, formula eq:rd at
`d = j+1` has only its `t = j` and `t = j+1` terms, and removing the row `(q-j-1)` leaves `θ` plus
one incomparable box, so `f^{λ/(q-j-1)} = (j+1)f^θ`.  What remains is the CANCELLATION
`q^{j+1} - q^j(q-j) = j·q^j`, which is what `rdSucc_eq_mul_rtop` proves.

The two combinatorial inputs — the vanishing of the `t < j` skew-tableau terms and
`f^{λ/(q-j-1)} = (j+1)f^θ` — are external (they are about skew standard tableaux, absent from
Mathlib v4.31.0); they appear as the SHAPE of the expression on the left, not as assumptions
hidden inside the arithmetic.  Nothing downstream of `theoremB` consumes this identity: at tier 1
the estimate it supports, paper eq:phi-oldlower, is the unconditional `n^{1/6}` route
(`SE.br.cor16`), not the conditional Theorem B route.  It is proved here because the node
`SE.formal.t2` names it. -/

/-- **The one-defect completion identity** — paper `lem:phi-diag`:
`r_{j+1}(λ) = j·r_top(q,j,θ)` for `λ = (q-j,θ)`.

The left-hand side is eq:rd at `d = j+1` after its two surviving terms are written out, with
`f^{λ/(q-j-1)} = (j+1)f^θ` substituted in the `t = j+1` term and `f^{λ/(q-j)} = f^θ`,
`binom(q-j,1) = q-j` in the `t = j` term; the right-hand side is `j` times
`r_top = q^j f^θ/(j! f^λ)` (eq:rtop).  Pure arithmetic: `(j+1)! = (j+1)·j!` and
`q^{j+1} - q^j(q-j) = j·q^j`. -/
theorem rdSucc_eq_mul_rtop (q j : ℕ) (fThe fLam : ℝ) (hLam : fLam ≠ 0) :
    ((q : ℝ) ^ (j + 1) * (((j : ℝ) + 1) * fThe) / (Nat.factorial (j + 1) : ℝ)
        - (q : ℝ) ^ j * ((q : ℝ) - (j : ℝ)) * fThe / (Nat.factorial j : ℝ)) / fLam
      = (j : ℝ) * ((q : ℝ) ^ j * fThe / ((Nat.factorial j : ℝ) * fLam)) := by
  have hfac : (Nat.factorial (j + 1) : ℝ) = ((j : ℝ) + 1) * (Nat.factorial j : ℝ) := by
    rw [Nat.factorial_succ]
    push_cast
    ring
  have hj0 : (Nat.factorial j : ℝ) ≠ 0 := by
    exact_mod_cast Nat.factorial_ne_zero j
  have hj1 : ((j : ℝ) + 1) ≠ 0 := by positivity
  rw [hfac]
  field_simp
  ring

/-- The same identity with the right-hand side written as the explicit hook product: whenever the
hook-length formula identifies `r_top(q,j,θ)` with `SE.rtopHook q j θ₁ θ'` (the hypothesis is a
PARAMETER, the current formalization trust-boundary rule — it is the same citation as `Cited.rho_isGreatest`), the one-defect
completion factor is exactly `j·rtopHook`. -/
theorem rdSucc_eq_mul_rtopHook {q j L : ℕ} {t : ℕ → ℕ} {fThe fLam : ℝ} (hLam : fLam ≠ 0)
    (hhook : rtopHook q j L t = (q : ℝ) ^ j * fThe / ((Nat.factorial j : ℝ) * fLam)) :
    ((q : ℝ) ^ (j + 1) * (((j : ℝ) + 1) * fThe) / (Nat.factorial (j + 1) : ℝ)
        - (q : ℝ) ^ j * ((q : ℝ) - (j : ℝ)) * fThe / (Nat.factorial j : ℝ)) / fLam
      = (j : ℝ) * rtopHook q j L t := by
  rw [hhook]
  exact rdSucc_eq_mul_rtop q j fThe fLam hLam

/-! ## The log envelope of paper eq:rho-asymp

`log r_top ≤ d(d-1)/(2(q-d+1)) + d/(q-2d+1)`, i.e. exactly the exponent the manuscript displays
in eq:rho-asymp at `q = 2n`.  Both summands come from `log(1+x) ≤ x`: the first from
`log(q/(q-i)) ≤ i/(q-i) ≤ i/(q-d+1)` summed by `Σ_{i<d} i = d(d-1)/2`, the second from
`log(1+θ'_c/(q-d-c+1)) ≤ θ'_c/(q-d-c+1) ≤ θ'_c/(q-2d+1)` summed by `Σ_c θ'_c = d`. -/

/-- `Σ_{i<d} i = d(d-1)/2` over `ℝ`. -/
theorem sum_range_cast_id (d : ℕ) :
    ∑ i ∈ Finset.range d, (i : ℝ) = (d : ℝ) * ((d : ℝ) - 1) / 2 := by
  induction d with
  | zero => simp
  | succ m ih =>
      rw [Finset.sum_range_succ, ih]
      push_cast
      ring

/-- The exponent of paper eq:rho-asymp: `E(q,d) = d(d-1)/(2(q-d+1)) + d/(q-2d+1)`. -/
noncomputable def hookExponent (q d : ℕ) : ℝ :=
  (d : ℝ) * ((d : ℝ) - 1) / (2 * ((q : ℝ) - (d : ℝ) + 1)) + (d : ℝ) / ((q : ℝ) - 2 * (d : ℝ) + 1)

section LogBound

variable {q d L : ℕ} {t : ℕ → ℕ}

/-- **The log envelope, uniformly in the shape**: `log r_top(q,d,θ) ≤ E(q,d)`, paper
eq:rho-asymp's exponent. -/
theorem log_rtopHook_le (hq : 2 * d < q) (hcol : IsColumnData L t d) :
    Real.log (rtopHook q d L t) ≤ hookExponent q d := by
  have hL : L ≤ d := hcol.length_le
  have hdq : d ≤ q := by omega
  have hd1pos : (0 : ℝ) < (q : ℝ) - (d : ℝ) + 1 := by
    have : (d : ℝ) < (q : ℝ) := by exact_mod_cast (by omega : d < q)
    linarith
  have hd2pos : (0 : ℝ) < (q : ℝ) - 2 * (d : ℝ) + 1 := by
    have h : ((2 * d : ℕ) : ℝ) < (q : ℝ) := by exact_mod_cast hq
    push_cast at h
    linarith
  -- the two products, each positive
  set A : ℝ := ∏ i ∈ Finset.range d, ((q : ℝ) / ((q : ℝ) - (i : ℝ))) with hA
  set B : ℝ := ∏ i ∈ Finset.range L, (1 + (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ))) with hB
  have hApos : (0 : ℝ) < A := by
    rw [hA]
    exact Finset.prod_pos fun i hi =>
      lt_of_lt_of_le zero_lt_one (one_le_rise_factor hq (Finset.mem_range.mp hi))
  have hBpos : (0 : ℝ) < B := by
    rw [hB]
    exact Finset.prod_pos fun i hi =>
      lt_of_lt_of_le zero_lt_one (one_le_hook_factor (t := t) hq hL (Finset.mem_range.mp hi))
  -- first sum
  have hsum1 : Real.log A ≤ (d : ℝ) * ((d : ℝ) - 1) / (2 * ((q : ℝ) - (d : ℝ) + 1)) := by
    have hlog : Real.log A = ∑ i ∈ Finset.range d, Real.log ((q : ℝ) / ((q : ℝ) - (i : ℝ))) := by
      rw [hA]
      exact Real.log_prod fun i hi =>
        ne_of_gt (lt_of_lt_of_le zero_lt_one (one_le_rise_factor hq (Finset.mem_range.mp hi)))
    have hterm : ∀ i ∈ Finset.range d,
        Real.log ((q : ℝ) / ((q : ℝ) - (i : ℝ)))
          ≤ (i : ℝ) / ((q : ℝ) - (d : ℝ) + 1) := by
      intro i hi
      have hi' : i < d := Finset.mem_range.mp hi
      have hden := rise_den_pos hq hi'
      have hlt : Real.log ((q : ℝ) / ((q : ℝ) - (i : ℝ)))
          ≤ (q : ℝ) / ((q : ℝ) - (i : ℝ)) - 1 :=
        Real.log_le_sub_one_of_pos (lt_of_lt_of_le zero_lt_one (one_le_rise_factor hq hi'))
      have heq : (q : ℝ) / ((q : ℝ) - (i : ℝ)) - 1 = (i : ℝ) / ((q : ℝ) - (i : ℝ)) := by
        field_simp
        ring
      have hmono : (i : ℝ) / ((q : ℝ) - (i : ℝ)) ≤ (i : ℝ) / ((q : ℝ) - (d : ℝ) + 1) := by
        refine div_le_div_of_nonneg_left (Nat.cast_nonneg i) hd1pos ?_
        have : (i : ℝ) + 1 ≤ (d : ℝ) := by exact_mod_cast (by omega : i + 1 ≤ d)
        linarith
      calc Real.log ((q : ℝ) / ((q : ℝ) - (i : ℝ)))
          ≤ (q : ℝ) / ((q : ℝ) - (i : ℝ)) - 1 := hlt
        _ = (i : ℝ) / ((q : ℝ) - (i : ℝ)) := heq
        _ ≤ (i : ℝ) / ((q : ℝ) - (d : ℝ) + 1) := hmono
    calc Real.log A = ∑ i ∈ Finset.range d, Real.log ((q : ℝ) / ((q : ℝ) - (i : ℝ))) := hlog
      _ ≤ ∑ i ∈ Finset.range d, (i : ℝ) / ((q : ℝ) - (d : ℝ) + 1) :=
        Finset.sum_le_sum hterm
      _ = (∑ i ∈ Finset.range d, (i : ℝ)) / ((q : ℝ) - (d : ℝ) + 1) := by
        rw [← Finset.sum_div]
      _ = (d : ℝ) * ((d : ℝ) - 1) / (2 * ((q : ℝ) - (d : ℝ) + 1)) := by
        rw [sum_range_cast_id]
        field_simp
  -- second sum
  have hsum2 : Real.log B ≤ (d : ℝ) / ((q : ℝ) - 2 * (d : ℝ) + 1) := by
    have hlog : Real.log B
        = ∑ i ∈ Finset.range L, Real.log (1 + (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ))) := by
      rw [hB]
      exact Real.log_prod fun i hi =>
        ne_of_gt (lt_of_lt_of_le zero_lt_one
          (one_le_hook_factor (t := t) hq hL (Finset.mem_range.mp hi)))
    have hterm : ∀ i ∈ Finset.range L,
        Real.log (1 + (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ)))
          ≤ (t i : ℝ) / ((q : ℝ) - 2 * (d : ℝ) + 1) := by
      intro i hi
      have hi' : i < L := Finset.mem_range.mp hi
      have hden := hook_den_pos hq hL hi'
      have hlt : Real.log (1 + (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ)))
          ≤ (1 + (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ))) - 1 :=
        Real.log_le_sub_one_of_pos
          (lt_of_lt_of_le zero_lt_one (one_le_hook_factor (t := t) hq hL hi'))
      have hmono : (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ))
          ≤ (t i : ℝ) / ((q : ℝ) - 2 * (d : ℝ) + 1) := by
        refine div_le_div_of_nonneg_left (Nat.cast_nonneg _) hd2pos ?_
        have : (i : ℝ) + 1 ≤ (d : ℝ) := by exact_mod_cast (by omega : i + 1 ≤ d)
        linarith
      have : Real.log (1 + (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ)))
          ≤ (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ)) := by linarith
      exact le_trans this hmono
    have hsumt : ∑ i ∈ Finset.range L, (t i : ℝ) = (d : ℝ) := by
      have := hcol.sum_eq
      calc ∑ i ∈ Finset.range L, (t i : ℝ) = ((∑ i ∈ Finset.range L, t i : ℕ) : ℝ) := by
            push_cast; ring
        _ = (d : ℝ) := by rw [this]
    calc Real.log B
        = ∑ i ∈ Finset.range L, Real.log (1 + (t i : ℝ) / ((q : ℝ) - (d : ℝ) - (i : ℝ))) := hlog
      _ ≤ ∑ i ∈ Finset.range L, (t i : ℝ) / ((q : ℝ) - 2 * (d : ℝ) + 1) := Finset.sum_le_sum hterm
      _ = (∑ i ∈ Finset.range L, (t i : ℝ)) / ((q : ℝ) - 2 * (d : ℝ) + 1) := by
        rw [← Finset.sum_div]
      _ = (d : ℝ) / ((q : ℝ) - 2 * (d : ℝ) + 1) := by rw [hsumt]
  -- combine
  have hprod : rtopHook q d L t = A * B := by rw [rtopHook, rise_eq_prod hdq, hA, hB]
  rw [hprod, Real.log_mul (ne_of_gt hApos) (ne_of_gt hBpos), hookExponent]
  linarith

end LogBound

/-! ## From the log envelope to `1 + C·n^{-1/3}` -/

/-- `exp x ≤ 1/(1-x)` for `x < 1` — the manuscript's `e^x ≤ 1/(1-x)` step. -/
theorem exp_le_inv_one_sub {x : ℝ} (hx : x < 1) : Real.exp x ≤ 1 / (1 - x) := by
  have h1 : (0 : ℝ) < 1 - x := by linarith
  have h2 : (1 : ℝ) - x ≤ Real.exp (-x) := by
    have := Real.add_one_le_exp (-x)
    linarith
  have h3 : Real.exp (-x) = 1 / Real.exp x := by
    rw [Real.exp_neg, one_div]
  have hex : (0 : ℝ) < Real.exp x := Real.exp_pos x
  rw [h3] at h2
  rw [le_div_iff₀ h1]
  rw [le_div_iff₀ hex] at h2
  linarith

/-- `r ≤ 1 + 2E` from `log r ≤ E` and `0 ≤ E ≤ 1/2`: the numeric closure
`e^E ≤ 1/(1-E) ≤ 1+2E`. -/
theorem le_one_add_two_mul_of_log_le {r E : ℝ} (hr : 0 < r) (hlog : Real.log r ≤ E)
    (hE0 : 0 ≤ E) (hE : E ≤ 1 / 2) : r ≤ 1 + 2 * E := by
  have h1 : r ≤ Real.exp E := by
    rw [← Real.exp_log hr]
    exact Real.exp_le_exp.mpr hlog
  have h2 : Real.exp E ≤ 1 / (1 - E) := exp_le_inv_one_sub (by linarith)
  have h3 : (0 : ℝ) < 1 - E := by linarith
  have h4 : 1 / (1 - E) ≤ 1 + 2 * E := by
    rw [div_le_iff₀ h3]
    nlinarith
  linarith

/-! ## The hook envelope on the taper window

The manuscript's `ρ_d = 1 + O(n^{-1/3})` (eq:rho-asymp), with the `O(·)` named.  On the taper
window `q = 2n`, `0 ≤ d < K n = ⌊n^{1/3}⌋` the exponent obeys `E(2n,d) ≤ 1/K n`, because
`K³ ≤ n` makes both `K²/n` and `K/n` at most `1/K`; then `e^E ≤ 1 + 2E` and
`n^{1/3} < K + 1 ≤ 2K` give the stated constant. -/

/-- The implied constant of the hook envelope, paper eq:rho-asymp's `O(n^{-1/3})`, made
explicit: `r_top ≤ 1 + 4·n^{-1/3}` uniformly on the taper window.  (Tier 1 carried this as the
abstract carrier field `SEFrame.rhoConst`.) -/
noncomputable def rhoConst : ℝ := 4

theorem rhoConst_nonneg : (0 : ℝ) ≤ rhoConst := by norm_num [rhoConst]

theorem hookExponent_nonneg {q d : ℕ} (hq : 2 * d < q) : 0 ≤ hookExponent q d := by
  have hd1pos : (0 : ℝ) < (q : ℝ) - (d : ℝ) + 1 := by
    have : (d : ℝ) < (q : ℝ) := by exact_mod_cast (by omega : d < q)
    linarith
  have hd2pos : (0 : ℝ) < (q : ℝ) - 2 * (d : ℝ) + 1 := by
    have h : ((2 * d : ℕ) : ℝ) < (q : ℝ) := by exact_mod_cast hq
    push_cast at h
    linarith
  have hnum : (0 : ℝ) ≤ (d : ℝ) * ((d : ℝ) - 1) := by
    rcases Nat.eq_zero_or_pos d with rfl | hd
    · norm_num
    · have : (1 : ℝ) ≤ (d : ℝ) := by exact_mod_cast hd
      nlinarith
  have hd0 : (0 : ℝ) ≤ (d : ℝ) := Nat.cast_nonneg d
  unfold hookExponent
  have t1 : (0 : ℝ) ≤ (d : ℝ) * ((d : ℝ) - 1) / (2 * ((q : ℝ) - (d : ℝ) + 1)) :=
    div_nonneg hnum (by linarith)
  have t2 : (0 : ℝ) ≤ (d : ℝ) / ((q : ℝ) - 2 * (d : ℝ) + 1) := div_nonneg hd0 hd2pos.le
  linarith

/-- **The exponent on the taper window**: `E(2n,d) ≤ 1/K n` for `0 ≤ d < K n`. -/
theorem hookExponent_le_inv_K {n d : ℕ} (hd : d < K n) :
    hookExponent (2 * n) d ≤ 1 / (K n : ℝ) := by
  have hK1 : 1 ≤ K n := by omega
  have hKn : K n ≤ n := K_le_self n
  have hn1 : 1 ≤ n := le_trans hK1 hKn
  have hk1 : (1 : ℝ) ≤ (K n : ℝ) := by exact_mod_cast hK1
  have hkpos : (0 : ℝ) < (K n : ℝ) := by linarith
  rcases Nat.eq_zero_or_pos d with rfl | hd1
  · have : hookExponent (2 * n) 0 = 0 := by
      unfold hookExponent
      norm_num
    rw [this]
    positivity
  -- `d ≥ 1` forces `K ≥ 2`, hence `n ≥ K³ ≥ 4K` and `2K² ≤ n`
  have hK2 : 2 ≤ K n := by omega
  have hcube : (K n) ^ 3 ≤ n := K_pow_le n
  have h4K : 4 * K n ≤ n := by
    have : 4 * K n ≤ (K n) ^ 3 := by
      calc 4 * K n ≤ (K n) * (K n) * (K n) := by
            have := hK2
            nlinarith
        _ = (K n) ^ 3 := by ring
    omega
  have h2Ksq : 2 * (K n) ^ 2 ≤ n := by
    have : 2 * (K n) ^ 2 ≤ (K n) ^ 3 := by
      have := hK2
      nlinarith
    omega
  set k : ℝ := (K n : ℝ) with hkdef
  set N : ℝ := (n : ℝ) with hNdef
  set D : ℝ := (d : ℝ) with hDdef
  have hk2 : (2 : ℝ) ≤ k := by rw [hkdef]; exact_mod_cast hK2
  have hD1 : (1 : ℝ) ≤ D := by rw [hDdef]; exact_mod_cast hd1
  have hDk : D ≤ k - 1 := by
    have : (d : ℝ) + 1 ≤ (K n : ℝ) := by exact_mod_cast (by omega : d + 1 ≤ K n)
    rw [hDdef, hkdef]; linarith
  have hNk3 : k ^ 3 ≤ N := by rw [hkdef, hNdef]; exact_mod_cast hcube
  have h4kN : 4 * k ≤ N := by
    rw [hkdef, hNdef]
    have : ((4 * K n : ℕ) : ℝ) ≤ (n : ℝ) := by exact_mod_cast h4K
    push_cast at this
    linarith
  have h2kN : 2 * k ^ 2 ≤ N := by
    rw [hkdef, hNdef]
    have : ((2 * (K n) ^ 2 : ℕ) : ℝ) ≤ (n : ℝ) := by exact_mod_cast h2Ksq
    push_cast at this
    linarith
  have hNpos : (0 : ℝ) < N := by nlinarith
  have hden1 : (0 : ℝ) < 2 * (2 * N - D + 1) := by nlinarith
  have hden2 : (0 : ℝ) < 2 * N - 2 * D + 1 := by nlinarith
  have hcast : hookExponent (2 * n) d
      = D * (D - 1) / (2 * (2 * N - D + 1)) + D / (2 * N - 2 * D + 1) := by
    unfold hookExponent
    rw [hDdef, hNdef]
    push_cast
    ring
  rw [hcast]
  -- each summand is at most `1/(2k)`
  have e1 : D * (D - 1) / (2 * (2 * N - D + 1)) ≤ 1 / (2 * k) := by
    rw [div_le_div_iff₀ hden1 (by linarith)]
    nlinarith [sq_nonneg (k - D), sq_nonneg k, sq_nonneg D]
  have e2 : D / (2 * N - 2 * D + 1) ≤ 1 / (2 * k) := by
    rw [div_le_div_iff₀ hden2 (by linarith)]
    nlinarith
  have hhalf : 1 / (2 * k) + 1 / (2 * k) = 1 / k := by
    field_simp
    norm_num
  linarith

/-- **The hook envelope, tier 2**: for every shape `θ ⊢ d` and every `d < K n = ⌊n^{1/3}⌋`,
`r_top(2n,d,θ) ≤ 1 + 4·n^{-1/3}` — paper eq:rho-asymp's `ρ_d ≤ 1 + O(n^{-1/3})`, proved, with the
implied constant `SE.rhoConst = 4`. -/
theorem rtopHook_le_envelope {n d L : ℕ} {t : ℕ → ℕ} (hcol : IsColumnData L t d)
    (hd : d < K n) : rtopHook (2 * n) d L t ≤ 1 + rhoConst / (n : ℝ) ^ ((1 : ℝ) / 3) := by
  have hK1 : 1 ≤ K n := by omega
  have hKn : K n ≤ n := K_le_self n
  have hn1 : 1 ≤ n := le_trans hK1 hKn
  have hdn : d < n := lt_of_lt_of_le hd hKn
  have hq : 2 * d < 2 * n := by omega
  have hL : L ≤ d := hcol.length_le
  have hE0 : 0 ≤ hookExponent (2 * n) d := hookExponent_nonneg hq
  have hEK : hookExponent (2 * n) d ≤ 1 / (K n : ℝ) := hookExponent_le_inv_K hd
  have hk1 : (1 : ℝ) ≤ (K n : ℝ) := by exact_mod_cast hK1
  have hkpos : (0 : ℝ) < (K n : ℝ) := by linarith
  -- `E ≤ 1/2`: at `d = 0` the exponent vanishes, and `d ≥ 1` forces `K ≥ 2`
  have hEhalf : hookExponent (2 * n) d ≤ 1 / 2 := by
    rcases Nat.eq_zero_or_pos d with rfl | hd1
    · have h0 : hookExponent (2 * n) 0 = 0 := by unfold hookExponent; norm_num
      rw [h0]; norm_num
    · have hK2 : (2 : ℝ) ≤ (K n : ℝ) := by exact_mod_cast (by omega : 2 ≤ K n)
      have : 1 / (K n : ℝ) ≤ 1 / 2 := by
        rw [div_le_div_iff₀ hkpos (by norm_num)]
        linarith
      linarith
  -- the numeric closure
  have hr : rtopHook (2 * n) d L t ≤ 1 + 2 * hookExponent (2 * n) d :=
    le_one_add_two_mul_of_log_le (rtopHook_pos hq hL) (log_rtopHook_le hq hcol) hE0 hEhalf
  -- `2/K ≤ 4/n^{1/3}`, because `n^{1/3} < K + 1 ≤ 2K`
  have hrpow : (0 : ℝ) < (n : ℝ) ^ ((1 : ℝ) / 3) := by
    have : (0 : ℝ) < (n : ℝ) := by exact_mod_cast hn1
    positivity
  have hlt : (n : ℝ) ^ ((1 : ℝ) / 3) < 2 * (K n : ℝ) := by
    have := rpow_lt_K_succ n
    linarith
  have hstep : 2 * (1 / (K n : ℝ)) ≤ rhoConst / (n : ℝ) ^ ((1 : ℝ) / 3) := by
    rw [rhoConst, mul_one_div, div_le_div_iff₀ hkpos hrpow]
    linarith
  have : 2 * hookExponent (2 * n) d ≤ 2 * (1 / (K n : ℝ)) := by linarith
  linarith

end SE
