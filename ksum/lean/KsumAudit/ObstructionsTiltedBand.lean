/-
# `thm:tilted-log-band` — Tilted log-band witness (the outer functional, DERIVED)

LaTeX: `ksum/paper/ksum_small_alphabet.tex`, label `thm:tilted-log-band`, line 895,
displayed equations (41)–(44).
DAG node: `KSUM.B4b.L2.L2P3` (`ksum/proof-dag/nodes/KSUM.B4b.L2.L2P3.yaml`, PROVED).

## The quantifier structure the LaTeX asserts (written out BEFORE formalizing)

∀ odd `q ≥ 3`, ∀ `N ≥ q`, ∀ `t ∈ ℤ_q`:  ∃ an `S_N × C(σ)`-invariant signed measure `μ` with
`‖μ‖₁ = 1` such that `⟨μ, F⟩ ≥ 437/581 > 3/4` and every query polynomial of degree
`< 2(1 + ⌊log₅((q-1)/2)⌋)` is annihilated.

## SCOPE — what is now DERIVED, and what is still assumed (gap-closure batch 2, 2026-08-01)

The paper's proof has two halves: an **outer functional** on the activity layers
`T_m = {0,1,5,…,5^{m-1}}`, and the **inner pair tensor** that carries it (`thm:pair-tensor`),
glued by `lem:factorial-filtration`.  Batch 1 proved the glue
(`KsumAudit.FactorialFiltration`); this file now proves the OUTER HALF outright, where before it
took the paper's two displayed bounds as hypotheses.

DERIVED here from the construction (42), nothing assumed:

  * `tnode` / `lam` — the node set `T_m` and the divided-difference coefficients (42), defined,
    not postulated;
  * `tilt_annihilates_low_degree` — `∑_{k ∈ T_m} λ_k p(k) = 0` for every `p` of degree `< m`
    (the paper's "there are `m+1` nodes in `T_m`, so divided differences give …"), via
    `Lagrange.coeff_eq_sum`;
  * `lam_ratio` — the ratio computation **(44)**, `|λ_{5^j}|/|λ_0| = A_j·C_{m-1-j}`, with
    `A_j = ∏_{d≤j}(5^d-1)^{-1}` and `C_h = ∏_{d≤h}(1-5^{-d})^{-1}` defined as the paper defines
    them;
  * `Cfac_le` — **`C_h ≤ 25/19`**, from the cited Weierstrass inequality (peeling the `d=1`
    factor exactly, which is what makes `25/19` rather than the cruder `4/3` come out);
  * `sum_Afac_le` — **`∑_j A_j ≤ 29/23`**, from `A_0 = 1`, `A_1 = 1/4` and the ratio bound
    `A_{j+1}/A_j ≤ 1/24` for `j ≥ 1`;
  * `tilt_corr_eq` / `tilt_corr_ge` — equation **(43)** evaluated at the constructed `λ`, and
    the resulting `⟨μ,F⟩ ≥ 437/581 > 3/4` **with no hypothesis at all**;
  * `tilt_rho_le_four_fifths` — the same quantity is `≤ 4/5` for `m ≥ 2`, which is the
    `ρ_j ≤ 4/5` step consumed by `thm:block-obstruction` clause (iii).

STILL NOT formalized (reported, not worked around):

  * the inner object: the exact-total pair tensor of `thm:pair-tensor` as a measure on `ℤ_q^N`,
    the transfer from the activity-layer functional to the falling-factorial band
    (`deg p < 2m ⇒ activity degree < m`), and the `ℓ¹`/invariance bookkeeping.  Consequently the
    LaTeX theorem as a whole — an existence statement about a measure on `ℤ_q^N` — is still not a
    theorem of this file; what is a theorem is every arithmetic and combinatorial ingredient the
    paper's proof of it uses, `m` being `1 + ⌊log₅ r⌋`.
-/
import KsumAudit.ObstructionsCore
import Mathlib.LinearAlgebra.Lagrange

namespace KsumAudit.Obstructions.TiltedBand

open Finset KsumAudit.Obstructions

set_option linter.unusedSectionVars false

/-- The elementary inequality cited in the proof of `thm:tilted-log-band`:
`∏_i (1 - x_i) ≥ 1 - ∑_i x_i` for `x_i ∈ [0,1]`. -/
theorem one_sub_sum_le_prod_one_sub {ι : Type*} [DecidableEq ι] (s : Finset ι) (x : ι → ℚ)
    (h0 : ∀ i ∈ s, 0 ≤ x i) (h1 : ∀ i ∈ s, x i ≤ 1) :
    1 - ∑ i ∈ s, x i ≤ ∏ i ∈ s, (1 - x i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | insert a s ha ih =>
      have h0' : ∀ i ∈ s, 0 ≤ x i := fun i hi => h0 i (Finset.mem_insert_of_mem hi)
      have h1' : ∀ i ∈ s, x i ≤ 1 := fun i hi => h1 i (Finset.mem_insert_of_mem hi)
      have hsum_nonneg : 0 ≤ ∑ i ∈ s, x i := Finset.sum_nonneg h0'
      have hxa0 : 0 ≤ x a := h0 a (Finset.mem_insert_self a s)
      have hxa1 : x a ≤ 1 := h1 a (Finset.mem_insert_self a s)
      rw [Finset.sum_insert ha, Finset.prod_insert ha]
      have hIH := ih h0' h1'
      nlinarith [hIH, hsum_nonneg, hxa0, hxa1]

/-- **`thm:tilted-log-band`, the closing numeric chain.**
With `C_h ≤ 25/19` and `∑_j A_j ≤ 29/23` (both nonnegative), the correlation
`2/(1 + C·S)` of equation (43) is at least `437/581`. -/
theorem tilt_corr_lower_bound (C S : ℚ) (hC0 : 0 ≤ C) (hC : C ≤ 25/19)
    (hS0 : 0 ≤ S) (hS : S ≤ 29/23) :
    (437:ℚ)/581 ≤ 2 / (1 + C * S) := by
  have hCS : 0 ≤ C * S := mul_nonneg hC0 hS0
  have hden : (0:ℚ) < 1 + C * S := by linarith
  rw [le_div_iff₀ hden]
  nlinarith [hC, hS, hC0, hS0]

/-- `437/581 > 3/4`, with the exact gap `5/2324` displayed in the paper. -/
theorem tilt_gap : (437:ℚ)/581 - 3/4 = 5/2324 ∧ (3:ℚ)/4 < 437/581 := by
  constructor <;> norm_num

/-- Assembled: any correlation of the displayed form `2/(1 + C·S)` with the paper's two bounds
exceeds the load-bearing `3/4` threshold. -/
theorem tilt_corr_gt_three_quarters (C S : ℚ) (hC0 : 0 ≤ C) (hC : C ≤ 25/19)
    (hS0 : 0 ≤ S) (hS : S ≤ 29/23) :
    (3:ℚ)/4 < 2 / (1 + C * S) :=
  lt_of_lt_of_le tilt_gap.2 (tilt_corr_lower_bound C S hC0 hC hS0 hS)

/-! ## The construction (42): the nodes `T_m` and the divided-difference coefficients

`T_m = {0, 1, 5, …, 5^{m-1}}` has `m+1` elements; we index it by `range (m+1)`, node `0` being
the paper's `k = 0` layer (the only NO layer) and node `i+1` being `k = 5^i`. -/

/-- The node `T_m` at index `i`: `tnode 0 = 0` and `tnode (i+1) = 5^i`. -/
def tnode (i : ℕ) : ℚ := if i = 0 then 0 else 5 ^ (i - 1)

@[simp] lemma tnode_zero : tnode 0 = 0 := by simp [tnode]

@[simp] lemma tnode_succ (i : ℕ) : tnode (i + 1) = 5 ^ i := by simp [tnode]

lemma tnode_pos_of_ne_zero {i : ℕ} (hi : i ≠ 0) : 0 < tnode i := by
  obtain ⟨j, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hi
  rw [tnode_succ]; positivity

theorem tnode_injective : Function.Injective tnode := by
  intro a b hab
  rcases Nat.eq_zero_or_pos a with rfl | ha <;> rcases Nat.eq_zero_or_pos b with rfl | hb
  · rfl
  · rw [tnode_zero] at hab; exact absurd hab (tnode_pos_of_ne_zero hb.ne').ne
  · rw [tnode_zero] at hab; exact absurd hab.symm (tnode_pos_of_ne_zero ha.ne').ne
  · obtain ⟨a', rfl⟩ := Nat.exists_eq_succ_of_ne_zero ha.ne'
    obtain ⟨b', rfl⟩ := Nat.exists_eq_succ_of_ne_zero hb.ne'
    rw [tnode_succ, tnode_succ] at hab
    have hn : (5:ℕ) ^ a' = 5 ^ b' := by exact_mod_cast hab
    have := Nat.pow_right_injective (by norm_num) hn
    omega

/-- **Equation (42).**  The divided-difference coefficients
`λ_k = (∏_{u ∈ T_m, u ≠ k} (k - u))⁻¹` on the node set `T_m`, indexed by `range (m+1)`.
(This is `Lagrange.nodalWeight (range (m+1)) tnode`.) -/
noncomputable def lam (m i : ℕ) : ℚ := ∏ j ∈ (range (m + 1)).erase i, (tnode i - tnode j)⁻¹

/-- **The divided-difference property the paper cites**: *"there are `m+1` nodes in `T_m`, so
divided differences give `∑_{k ∈ T_m} λ_k p(k) = 0` for every polynomial `p` of degree below
`m`."*  Proved, not assumed: the sum is the `X^m`-coefficient of the interpolant, and a
polynomial of degree `< m` has none. -/
theorem tilt_annihilates_low_degree (m : ℕ) (P : Polynomial ℚ) (hP : P.degree < (m : ℕ)) :
    ∑ i ∈ range (m + 1), P.eval (tnode i) * lam m i = 0 := by
  classical
  have hcard : (range (m + 1)).card = m + 1 := Finset.card_range _
  have hlt : P.degree < ((range (m + 1)).card : ℕ) := by
    rw [hcard]
    exact lt_of_lt_of_le hP (by exact_mod_cast Nat.le_succ m)
  have hsum := Lagrange.coeff_eq_sum (v := tnode) (s := range (m + 1))
    tnode_injective.injOn hlt
  rw [hcard, Nat.add_sub_cancel, Polynomial.coeff_eq_zero_of_degree_lt hP] at hsum
  have hrw : ∀ i ∈ range (m + 1), P.eval (tnode i) * lam m i
      = P.eval (tnode i) / ∏ j ∈ (range (m + 1)).erase i, (tnode i - tnode j) := by
    intro i _
    rw [lam, Finset.prod_inv_distrib, div_eq_mul_inv]
  rw [Finset.sum_congr rfl hrw, ← hsum]

/-! ## The two constants of equation (44), and the products they abbreviate -/

/-- `Q_j = ∏_{d=1}^{j} (5^d - 1)`, the denominator common to `A_j` and `C_j`. -/
def Qprod (j : ℕ) : ℚ := ∏ d ∈ range j, ((5:ℚ) ^ (d + 1) - 1)

/-- **Equation (44)**, `A_j = ∏_{d=1}^{j} (5^d - 1)^{-1}`. -/
def Afac (j : ℕ) : ℚ := ∏ d ∈ range j, ((5:ℚ) ^ (d + 1) - 1)⁻¹

/-- **Equation (44)**, `C_h = ∏_{d=1}^{h} (1 - 5^{-d})^{-1}`. -/
def Cfac (h : ℕ) : ℚ := ∏ d ∈ range h, (1 - ((5:ℚ) ^ (d + 1))⁻¹)⁻¹

lemma Qprod_pos (j : ℕ) : 0 < Qprod j :=
  Finset.prod_pos fun d _ => by
    have : (1:ℚ) < 5 ^ (d + 1) := one_lt_pow₀ (by norm_num) (Nat.succ_ne_zero d)
    linarith

lemma Afac_eq_inv (j : ℕ) : Afac j = (Qprod j)⁻¹ := by
  rw [Afac, Qprod, Finset.prod_inv_distrib]

lemma Afac_pos (j : ℕ) : 0 < Afac j := by
  rw [Afac_eq_inv]; exact inv_pos.mpr (Qprod_pos j)

lemma Cfac_eq (h : ℕ) : Cfac h = 5 ^ (∑ x ∈ range (h + 1), x) / Qprod h := by
  have hfac : ∀ d : ℕ, (1 - ((5:ℚ) ^ (d + 1))⁻¹)⁻¹ = 5 ^ (d + 1) / ((5:ℚ) ^ (d + 1) - 1) := by
    intro d
    have h5 : (0:ℚ) < 5 ^ (d + 1) := by positivity
    have h1 : (1:ℚ) < 5 ^ (d + 1) := one_lt_pow₀ (by norm_num) (Nat.succ_ne_zero d)
    rw [show (1:ℚ) - ((5:ℚ) ^ (d + 1))⁻¹ = ((5:ℚ) ^ (d + 1) - 1) / 5 ^ (d + 1) by field_simp,
      inv_div]
  rw [Cfac, Finset.prod_congr rfl (fun d _ => hfac d), Finset.prod_div_distrib, ← Qprod]
  congr 1
  rw [← Finset.prod_pow_eq_pow_sum, Finset.prod_range_succ']
  simp

/-- `5^{-(d+1)} ≤ 1/5`. -/
lemma inv_pow_le (d : ℕ) : ((5:ℚ) ^ (d + 1))⁻¹ ≤ 1 / 5 := by
  have h5 : (0:ℚ) < 5 ^ (d + 1) := by positivity
  rw [inv_le_comm₀ h5 (by norm_num : (0:ℚ) < 1 / 5)]
  have hp : (5:ℚ) ^ (0 + 1) ≤ 5 ^ (d + 1) := pow_le_pow_right₀ (by norm_num) (by omega)
  norm_num at hp ⊢
  linarith

/-- Every factor of `C_h` is at least `1`. -/
lemma one_le_Cfac_factor (d : ℕ) : (1:ℚ) ≤ (1 - ((5:ℚ) ^ (d + 1))⁻¹)⁻¹ := by
  have h5 : (0:ℚ) < 5 ^ (d + 1) := by positivity
  have hinv : (0:ℚ) < ((5:ℚ) ^ (d + 1))⁻¹ := inv_pos.mpr h5
  have hx := inv_pow_le d
  have hpos : (0:ℚ) < 1 - ((5:ℚ) ^ (d + 1))⁻¹ := by linarith
  calc (1:ℚ) = (1 - ((5:ℚ) ^ (d + 1))⁻¹)⁻¹ * (1 - ((5:ℚ) ^ (d + 1))⁻¹) :=
        (inv_mul_cancel₀ hpos.ne').symm
    _ ≤ (1 - ((5:ℚ) ^ (d + 1))⁻¹)⁻¹ * 1 :=
        mul_le_mul_of_nonneg_left (by linarith) (inv_pos.mpr hpos).le
    _ = (1 - ((5:ℚ) ^ (d + 1))⁻¹)⁻¹ := mul_one _

lemma Cfac_ge_one (h : ℕ) : 1 ≤ Cfac h :=
  Finset.one_le_prod fun d _ => one_le_Cfac_factor d

lemma Cfac_pos (h : ℕ) : 0 < Cfac h := lt_of_lt_of_le one_pos (Cfac_ge_one h)

/-- `C_h ≥ 5/4` as soon as `h ≥ 1`: the `d = 1` factor alone is `(1-1/5)^{-1} = 5/4`, and every
later factor is `≥ 1`.  This is the paper's *"the `K=1` … absolute weight is at least `5/4` times
the `K=0` weight"*. -/
lemma Cfac_ge_five_fourths {h : ℕ} (hh : 1 ≤ h) : 5 / 4 ≤ Cfac h := by
  obtain ⟨h', rfl⟩ : ∃ h', h = h' + 1 := ⟨h - 1, by omega⟩
  rw [Cfac, Finset.prod_range_succ']
  have hrest : (1:ℚ) ≤ ∏ d ∈ range h', (1 - ((5:ℚ) ^ (d + 1 + 1))⁻¹)⁻¹ :=
    Finset.one_le_prod fun d _ => one_le_Cfac_factor (d + 1)
  have hzero : (1 - ((5:ℚ) ^ (0 + 1))⁻¹)⁻¹ = 5 / 4 := by norm_num
  rw [hzero]
  nlinarith [hrest]

/-! ### `C_h ≤ 25/19` — the cited Weierstrass estimate, with the `d = 1` factor peeled

Applying `∏(1-x_i) ≥ 1 - ∑x_i` to `d = 1 … h` directly gives only `C_h ≤ 4/3`.  The paper's
`25/19` comes from taking the `d = 1` factor exactly and estimating the tail
`∑_{d ≥ 2} 5^{-d} = 1/20`. -/

/-- The exact geometric tail `∑_{d < n} 5^{-(d+2)} = 1/20 - 1/(20·5^n)`. -/
lemma tail_geom (n : ℕ) :
    ∑ d ∈ range n, ((5:ℚ) ^ (d + 2))⁻¹ = 1 / 20 - 1 / (20 * 5 ^ n) := by
  induction n with
  | zero => norm_num
  | succ n ih =>
      rw [Finset.sum_range_succ, ih]
      have h5 : (0:ℚ) < 5 ^ n := by positivity
      field_simp
      ring

lemma tail_geom_le (n : ℕ) : ∑ d ∈ range n, ((5:ℚ) ^ (d + 2))⁻¹ ≤ 1 / 20 := by
  rw [tail_geom]
  have h5 : (0:ℚ) < 5 ^ n := by positivity
  have : 0 < (20:ℚ) * 5 ^ n := by positivity
  have : 0 ≤ 1 / ((20:ℚ) * 5 ^ n) := by positivity
  linarith

/-- **`C_h ≤ 25/19`** — the first of the paper's two displayed bounds, DERIVED. -/
theorem Cfac_le (h : ℕ) : Cfac h ≤ 25 / 19 := by
  have hprod : (19:ℚ) / 25 ≤ ∏ d ∈ range h, (1 - ((5:ℚ) ^ (d + 1))⁻¹) := by
    rcases Nat.eq_zero_or_pos h with rfl | hh
    · norm_num
    · obtain ⟨h', rfl⟩ : ∃ h', h = h' + 1 := ⟨h - 1, by omega⟩
      rw [Finset.prod_range_succ']
      have hW := one_sub_sum_le_prod_one_sub (range h') (fun d => ((5:ℚ) ^ (d + 2))⁻¹)
        (fun d _ => by positivity)
        (fun d _ => by
          have h1 : (1:ℚ) ≤ 5 ^ (d + 2) := one_le_pow₀ (by norm_num)
          rw [inv_le_one₀ (by positivity)]
          exact h1)
      have htail := tail_geom_le h'
      have hzero : (1 - ((5:ℚ) ^ (0 + 1))⁻¹) = 4 / 5 := by norm_num
      have hrest : (19:ℚ) / 20 ≤ ∏ d ∈ range h', (1 - ((5:ℚ) ^ (d + 1 + 1))⁻¹) := by
        have : ∀ d : ℕ, (1 - ((5:ℚ) ^ (d + 1 + 1))⁻¹) = (1 - ((5:ℚ) ^ (d + 2))⁻¹) := by
          intro d; norm_num
        rw [Finset.prod_congr rfl (fun d _ => this d)]
        linarith
      rw [hzero]
      nlinarith [hrest]
  have hpos : (0:ℚ) < ∏ d ∈ range h, (1 - ((5:ℚ) ^ (d + 1))⁻¹) := by linarith
  have : Cfac h = (∏ d ∈ range h, (1 - ((5:ℚ) ^ (d + 1))⁻¹))⁻¹ := by
    rw [Cfac, Finset.prod_inv_distrib]
  rw [this, inv_eq_one_div, div_le_div_iff₀ hpos (by norm_num)]
  linarith

/-! ### `∑_j A_j ≤ 29/23` — `A_0 = 1`, `A_1 = 1/4`, and every later ratio at most `1/24` -/

@[simp] lemma Afac_zero : Afac 0 = 1 := by simp [Afac]

@[simp] lemma Afac_one : Afac 1 = 1 / 4 := by norm_num [Afac]

lemma Afac_succ (j : ℕ) : Afac (j + 1) = Afac j * ((5:ℚ) ^ (j + 1) - 1)⁻¹ := by
  rw [Afac, Afac, Finset.prod_range_succ]

/-- `A_{j+2} ≤ (1/96)·(1/24)^j`: `A_2 = 1/96` and every later ratio is at most `1/24`. -/
lemma Afac_tail_le (j : ℕ) : Afac (j + 2) ≤ (1 / 96) * (1 / 24 : ℚ) ^ j := by
  induction j with
  | zero => norm_num [Afac]
  | succ j ih =>
      have hstep : ((5:ℚ) ^ (j + 2 + 1) - 1)⁻¹ ≤ 1 / 24 := by
        have h1 : (24:ℚ) ≤ 5 ^ (j + 2 + 1) - 1 := by
          have : (5:ℚ) ^ (1 + 1) ≤ 5 ^ (j + 2 + 1) := pow_le_pow_right₀ (by norm_num) (by omega)
          norm_num at this ⊢
          linarith
        rw [inv_le_comm₀ (by linarith) (by norm_num)]
        norm_num
        linarith
      have hpos := (Afac_pos (j + 2)).le
      have h24 : (24:ℚ) ≤ 5 ^ (j + 2 + 1) - 1 := by
        have : (5:ℚ) ^ (1 + 1) ≤ 5 ^ (j + 2 + 1) := pow_le_pow_right₀ (by norm_num) (by omega)
        norm_num at this ⊢
        linarith
      have hinv : (0:ℚ) ≤ ((5:ℚ) ^ (j + 2 + 1) - 1)⁻¹ := by
        exact le_of_lt (inv_pos.mpr (by linarith))
      calc Afac (j + 1 + 2) = Afac (j + 2) * ((5:ℚ) ^ (j + 2 + 1) - 1)⁻¹ := by
            rw [show j + 1 + 2 = (j + 2) + 1 from rfl, Afac_succ]
        _ ≤ ((1 / 96) * (1 / 24 : ℚ) ^ j) * (1 / 24) := by
            exact mul_le_mul ih hstep hinv (by positivity)
        _ = (1 / 96) * (1 / 24 : ℚ) ^ (j + 1) := by ring

/-- The geometric partial sums `∑_{j<n}(1/24)^j = (24/23)(1 - (1/24)^n)`. -/
lemma geom24 (n : ℕ) : ∑ j ∈ range n, (1 / 24 : ℚ) ^ j = 24 / 23 - (24 / 23) * (1 / 24) ^ n := by
  induction n with
  | zero => norm_num
  | succ n ih => rw [Finset.sum_range_succ, ih]; ring

/-- **`∑_j A_j ≤ 29/23`** — the second of the paper's two displayed bounds, DERIVED.
`1 + 1/4 + (1/96)·(24/23) = 29/23`. -/
theorem sum_Afac_le (m : ℕ) : ∑ j ∈ range m, Afac j ≤ 29 / 23 := by
  match m with
  | 0 => norm_num
  | 1 => norm_num [Finset.sum_range_one]
  | (m' + 2) =>
      rw [Finset.sum_range_succ', Finset.sum_range_succ']
      have htail : ∑ j ∈ range m', Afac (j + 1 + 1) ≤ ∑ j ∈ range m', (1 / 96) * (1 / 24 : ℚ) ^ j :=
        Finset.sum_le_sum fun j _ => by
          rw [show j + 1 + 1 = j + 2 from rfl]; exact Afac_tail_le j
      have hgeom : ∑ j ∈ range m', (1 / 96) * (1 / 24 : ℚ) ^ j ≤ 1 / 92 := by
        rw [← Finset.mul_sum, geom24]
        have : (0:ℚ) ≤ (24 / 23) * (1 / 24 : ℚ) ^ m' := by positivity
        nlinarith
      have h0 : Afac 0 = 1 := Afac_zero
      have h1 : Afac (0 + 1) = 1 / 4 := by norm_num [Afac]
      rw [h0, h1]
      linarith

/-! ## The ratio computation (44), from the products themselves

`|λ_{5^i}|/|λ_0| = A_i·C_{m-1-i}`.  Everything below is the paper's own cancellation of common
powers of five, done as a product identity rather than asserted. -/

/-- `|λ_k|` as the reciprocal of a product of absolute node differences. -/
noncomputable def dpr (m i : ℕ) : ℚ := ∏ j ∈ (range (m + 1)).erase i, |tnode i - tnode j|

lemma abs_lam (m i : ℕ) : |lam m i| = (dpr m i)⁻¹ := by
  rw [lam, dpr, Finset.abs_prod, ← Finset.prod_inv_distrib]
  exact Finset.prod_congr rfl fun j _ => abs_inv _

/-- The exponent bookkeeping of (44): `∑_{x<i+h+1} x = i + ∑_{x<i} x + i·h + ∑_{x<h+1} x`. -/
lemma exponent_identity (i h : ℕ) :
    ∑ x ∈ range (i + h + 1), x
      = i + (∑ x ∈ range i, x) + i * h + (∑ x ∈ range (h + 1), x) := by
  induction h with
  | zero =>
      have e1 : ∑ x ∈ range (i + 0 + 1), x = (∑ x ∈ range i, x) + i := by
        rw [show i + 0 + 1 = i + 1 from rfl, Finset.sum_range_succ]
      have e2 : ∑ x ∈ range (0 + 1), x = 0 := by simp
      rw [e1, e2]
      omega
  | succ h ih =>
      have e1 : ∑ x ∈ range (i + (h + 1) + 1), x
          = (∑ x ∈ range (i + h + 1), x) + (i + h + 1) := by
        rw [show i + (h + 1) + 1 = (i + h + 1) + 1 from by omega, Finset.sum_range_succ]
      have e2 : ∑ x ∈ range (h + 1 + 1), x = (∑ x ∈ range (h + 1), x) + (h + 1) :=
        Finset.sum_range_succ _ _
      have e3 : i * (h + 1) = i * h + i := by ring
      rw [e1, ih, e2, e3]
      omega

/-- `|λ_0|⁻¹ = 5^{0+1+⋯+(m-1)}`: the node `0` row of (44). -/
theorem dpr_zero (m : ℕ) : dpr m 0 = 5 ^ (∑ x ∈ range m, x) := by
  classical
  have hset : (range (m + 1)).erase 0 = Finset.Ico 1 (m + 1) := by
    ext j
    simp only [Finset.mem_erase, Finset.mem_range, Finset.mem_Ico]
    omega
  rw [dpr, hset, Finset.prod_Ico_eq_prod_range, ← Finset.prod_pow_eq_pow_sum]
  have hm : m + 1 - 1 = m := by omega
  rw [hm]
  refine Finset.prod_congr rfl fun e _ => ?_
  rw [show 1 + e = e + 1 from Nat.add_comm 1 e, tnode_succ, tnode_zero, zero_sub, abs_neg]
  exact abs_of_pos (by positivity)

/-- `|λ_{5^i}|⁻¹`, computed: `5^{i + ∑_{x<i}x + i·h}·Q_i·Q_h` with `h = m-1-i`. -/
theorem dpr_succ {m i : ℕ} (hi : i < m) :
    dpr m (i + 1)
      = 5 ^ (i + (∑ x ∈ range i, x) + i * (m - 1 - i)) * (Qprod i * Qprod (m - 1 - i)) := by
  classical
  set h := m - 1 - i with hh
  have hm : m = i + h + 1 := by omega
  have hsplit : (range (m + 1)).erase (i + 1) = range (i + 1) ∪ Finset.Ico (i + 2) (m + 1) := by
    ext j
    simp only [Finset.mem_erase, Finset.mem_range, Finset.mem_union, Finset.mem_Ico]
    omega
  have hdisj : Disjoint (range (i + 1)) (Finset.Ico (i + 2) (m + 1)) := by
    rw [Finset.disjoint_left]
    intro a ha hb
    simp only [Finset.mem_range] at ha
    simp only [Finset.mem_Ico] at hb
    omega
  rw [dpr, hsplit, Finset.prod_union hdisj]
  -- the lower part
  have hlow : ∏ j ∈ range (i + 1), |tnode (i + 1) - tnode j|
      = 5 ^ (i + ∑ x ∈ range i, x) * Qprod i := by
    rw [Finset.prod_range_succ']
    have hterm : ∀ j ∈ range i, |tnode (i + 1) - tnode (j + 1)|
        = 5 ^ j * ((5:ℚ) ^ (i - 1 - j + 1) - 1) := by
      intro j hj
      simp only [Finset.mem_range] at hj
      rw [tnode_succ, tnode_succ]
      have hji : (5:ℚ) ^ j ≤ 5 ^ i := pow_le_pow_right₀ (by norm_num) (by omega)
      rw [abs_of_nonneg (by linarith)]
      have hexp : i = j + (i - 1 - j + 1) := by omega
      rw [show (5:ℚ) ^ i = 5 ^ j * 5 ^ (i - 1 - j + 1) by rw [← pow_add, ← hexp]]
      ring
    have hzero : |tnode (i + 1) - tnode 0| = (5:ℚ) ^ i := by
      rw [tnode_succ, tnode_zero, sub_zero]
      exact abs_of_pos (by positivity)
    have hrefl : ∏ j ∈ range i, ((5:ℚ) ^ (i - 1 - j + 1) - 1) = Qprod i := by
      rw [Qprod]
      exact Finset.prod_range_reflect (fun d => (5:ℚ) ^ (d + 1) - 1) i
    rw [Finset.prod_congr rfl hterm, Finset.prod_mul_distrib, hzero, hrefl,
      Finset.prod_pow_eq_pow_sum]
    ring
  -- the upper part
  have hup : ∏ j ∈ Finset.Ico (i + 2) (m + 1), |tnode (i + 1) - tnode j|
      = 5 ^ (i * h) * Qprod h := by
    rw [Finset.prod_Ico_eq_prod_range]
    have hcard : m + 1 - (i + 2) = h := by omega
    rw [hcard]
    have hterm : ∀ e ∈ range h, |tnode (i + 1) - tnode (i + 2 + e)|
        = 5 ^ i * ((5:ℚ) ^ (e + 1) - 1) := by
      intro e _
      rw [tnode_succ, show i + 2 + e = (i + 1 + e) + 1 from by omega, tnode_succ]
      have hle : (5:ℚ) ^ i ≤ 5 ^ (i + 1 + e) := pow_le_pow_right₀ (by norm_num) (by omega)
      rw [abs_of_nonpos (by linarith), neg_sub]
      rw [show (5:ℚ) ^ (i + 1 + e) = 5 ^ i * 5 ^ (e + 1) by rw [← pow_add]; ring_nf]
      ring
    rw [Finset.prod_congr rfl hterm, Finset.prod_mul_distrib, Finset.prod_const,
      Finset.card_range, ← pow_mul, Qprod]
  rw [hlow, hup]
  ring

/-- **Equation (44), DERIVED**: `|λ_{5^i}| = |λ_0|·A_i·C_{m-1-i}`. -/
theorem lam_ratio {m i : ℕ} (hi : i < m) :
    |lam m (i + 1)| = |lam m 0| * (Afac i * Cfac (m - 1 - i)) := by
  set h := m - 1 - i with hh
  have hm : m = i + h + 1 := by omega
  have hQi := Qprod_pos i
  have hQh := Qprod_pos h
  rw [abs_lam, abs_lam, dpr_zero, dpr_succ hi, ← hh, Afac_eq_inv, Cfac_eq]
  rw [hm, exponent_identity i h]
  have h5 : ∀ n : ℕ, (0:ℚ) < 5 ^ n := fun n => by positivity
  field_simp
  ring

/-! ## Equation (43): the correlation of the constructed witness -/

/-- The paper's `Z = ∑_k |λ_k|`. -/
noncomputable def Znorm (m : ℕ) : ℚ := ∑ i ∈ range (m + 1), |lam m i|

/-- The sum `∑_{j<m} A_j C_{m-1-j}` of (44) that (43) is expressed through. -/
noncomputable def Ssum (m : ℕ) : ℚ := ∑ j ∈ range m, Afac j * Cfac (m - 1 - j)

lemma abs_lam_zero_pos (m : ℕ) : 0 < |lam m 0| := by
  rw [abs_lam]
  exact inv_pos.mpr (by rw [dpr_zero]; positivity)

lemma Znorm_eq (m : ℕ) : Znorm m = |lam m 0| * (1 + Ssum m) := by
  have h : ∑ i ∈ range m, |lam m (i + 1)| = |lam m 0| * Ssum m := by
    rw [Ssum, Finset.mul_sum]
    exact Finset.sum_congr rfl fun j hj => lam_ratio (Finset.mem_range.mp hj)
  rw [Znorm, Finset.sum_range_succ', h]
  ring

lemma Ssum_nonneg (m : ℕ) : 0 ≤ Ssum m :=
  Finset.sum_nonneg fun j _ => mul_nonneg (Afac_pos j).le (Cfac_pos _).le

lemma Znorm_pos (m : ℕ) : 0 < Znorm m := by
  rw [Znorm_eq]
  exact mul_pos (abs_lam_zero_pos m) (by linarith [Ssum_nonneg m])

/-- The `K = 1` weight ratio of `thm:block-obstruction` clause (iii):
`|λ_1| ≥ (5/4)|λ_0|` for `m ≥ 2`.  Immediate from (44) and `C_h ≥ 5/4`. -/
lemma abs_lam_one_ge {m : ℕ} (hm : 2 ≤ m) : 5 / 4 * |lam m 0| ≤ |lam m 1| := by
  have h := lam_ratio (m := m) (i := 0) (by omega)
  rw [h, Afac_zero, one_mul, Nat.sub_zero]
  have hc : (5:ℚ) / 4 ≤ Cfac (m - 1) := Cfac_ge_five_fourths (by omega)
  nlinarith [abs_lam_zero_pos m]

/-- The `K = 5` weight ratio of clause (iii): `|λ_5| ≥ (1/4)|λ_0|` for `m ≥ 2`.
Immediate from (44) with `A_1 = 1/4` and `C_h ≥ 1`. -/
lemma abs_lam_two_ge {m : ℕ} (hm : 2 ≤ m) : 1 / 4 * |lam m 0| ≤ |lam m 2| := by
  have h := lam_ratio (m := m) (i := 1) (by omega)
  rw [h, Afac_one]
  have hc : (1:ℚ) ≤ Cfac (m - 1 - 1) := Cfac_ge_one _
  nlinarith [abs_lam_zero_pos m]

/-- **Equation (43), evaluated at the constructed coefficients.**
`⟨μ,F⟩ = 2|λ_0|/∑_k|λ_k| = 2/(1 + ∑_j A_j C_{m-1-j})`. -/
theorem tilt_corr_eq (m : ℕ) : 2 * |lam m 0| / Znorm m = 2 / (1 + Ssum m) := by
  have h0 := abs_lam_zero_pos m
  have hS := Ssum_nonneg m
  rw [Znorm_eq]
  rw [div_eq_div_iff (by positivity) (by positivity)]
  ring

/-- `∑_j A_j C_{m-1-j} ≤ (25/19)(29/23)`: the two derived bounds combined. -/
theorem Ssum_le (m : ℕ) : Ssum m ≤ (25 / 19) * (29 / 23) := by
  have hle : Ssum m ≤ ∑ j ∈ range m, Afac j * (25 / 19) := by
    refine Finset.sum_le_sum fun j _ => ?_
    exact mul_le_mul_of_nonneg_left (Cfac_le _) (Afac_pos j).le
  have hsum := sum_Afac_le m
  have hnn : (0:ℚ) ≤ ∑ j ∈ range m, Afac j := Finset.sum_nonneg fun j _ => (Afac_pos j).le
  rw [← Finset.sum_mul] at hle
  nlinarith

/-- **`thm:tilted-log-band` (41), for the constructed outer functional, UNCONDITIONALLY.**
`⟨μ,F⟩ = 2/(1 + ∑_j A_j C_{m-1-j}) ≥ 437/581 > 3/4`, with no hypothesis: the two bounds
`C_h ≤ 25/19` and `∑_j A_j ≤ 29/23` are `Cfac_le` and `sum_Afac_le`, both proved above. -/
theorem tilt_corr_ge (m : ℕ) :
    (437:ℚ) / 581 ≤ 2 * |lam m 0| / Znorm m ∧ (3:ℚ) / 4 < 2 * |lam m 0| / Znorm m := by
  have hS := Ssum_nonneg m
  have hSle := Ssum_le m
  have hden : (0:ℚ) < 1 + Ssum m := by linarith
  have hmain : (437:ℚ) / 581 ≤ 2 / (1 + Ssum m) := by
    rw [le_div_iff₀ hden]
    nlinarith
  rw [tilt_corr_eq m]
  exact ⟨hmain, lt_of_lt_of_le tilt_gap.2 hmain⟩

/-- **`thm:block-obstruction` clause (iii): `ρ_j ≤ 4/5`, DERIVED from the tilted inner.**

The paper: *"For the tilted inner with support `{0,1,5,…}`, the `K=1` and `K=5` absolute weights
are at least `5/4` and `1/4` times the `K=0` weight, so `ρ ≤ 2/(1 + 5/4 + 1/4) = 4/5`."*  Both
weight ratios are `lam_ratio` at `i = 0` and `i = 1` together with `C_h ≥ 5/4` (`h ≥ 1`) and
`C_h ≥ 1`; `ρ = 2|W_0| = 2|λ_0|/Z` is the paper's own identification of the conditional NO
probability with the all-axis layer weight, `K=0` being the only NO layer.  `m ≥ 2` is exactly
the paper's *"containing at least five complementary pairs"* (`r ≥ 5 ⇒ m = 1 + ⌊log₅ r⌋ ≥ 2`). -/
theorem tilt_rho_le_four_fifths {m : ℕ} (hm : 2 ≤ m) : 2 * |lam m 0| / Znorm m ≤ 4 / 5 := by
  have h0 := abs_lam_zero_pos m
  have hS : (3:ℚ) / 2 ≤ Ssum m := by
    have hsub : ({0, 1} : Finset ℕ) ⊆ range m := by
      intro j hj
      simp only [Finset.mem_insert, Finset.mem_singleton] at hj
      simp only [Finset.mem_range]
      rcases hj with rfl | rfl <;> omega
    have hnn : ∀ j ∈ range m, j ∉ ({0, 1} : Finset ℕ) → 0 ≤ Afac j * Cfac (m - 1 - j) :=
      fun j _ _ => mul_nonneg (Afac_pos j).le (Cfac_pos _).le
    have hle : ∑ j ∈ ({0, 1} : Finset ℕ), Afac j * Cfac (m - 1 - j) ≤ Ssum m :=
      Finset.sum_le_sum_of_subset_of_nonneg hsub hnn
    rw [Finset.sum_insert (by norm_num), Finset.sum_singleton] at hle
    have e0 : Afac 0 * Cfac (m - 1 - 0) = Cfac (m - 1) := by simp
    have e1 : Afac 1 * Cfac (m - 1 - 1) = (1 / 4) * Cfac (m - 2) := by
      rw [Afac_one, show m - 1 - 1 = m - 2 from by omega]
    have c0 : (5:ℚ) / 4 ≤ Cfac (m - 1) := Cfac_ge_five_fourths (by omega)
    have c1 : (1:ℚ) ≤ Cfac (m - 2) := Cfac_ge_one _
    rw [e0, e1] at hle
    linarith
  rw [tilt_corr_eq m, div_le_div_iff₀ (by linarith) (by norm_num)]
  linarith

/-! ## Non-vacuity witnesses -/

/-- The bounds are attainable: at `C = 25/19`, `S = 29/23` the value is exactly `437/581`. -/
example : (2:ℚ) / (1 + (25/19) * (29/23)) = 437/581 := by norm_num

example : (1:ℚ) - (1/4 + 1/4) ≤ (1 - 1/4) * (1 - 1/4) := by norm_num

private lemma erase0 : (range 3).erase 0 = ({1, 2} : Finset ℕ) := by decide
private lemma erase1 : (range 3).erase 1 = ({0, 2} : Finset ℕ) := by decide
private lemma erase2 : (range 3).erase 2 = ({0, 1} : Finset ℕ) := by decide

/-- The smallest instance the `ρ ≤ 4/5` clause covers, `m = 2` (`T_2 = {0,1,5}`), computed from
the definition (42): `λ_0 = 1/5`, `λ_1 = -1/4`, `λ_5 = 1/20`. -/
theorem lam_two_values : lam 2 0 = 1 / 5 ∧ lam 2 1 = -(1 / 4) ∧ lam 2 2 = 1 / 20 := by
  refine ⟨?_, ?_, ?_⟩
  · rw [lam, erase0, Finset.prod_pair (by norm_num)]; norm_num [tnode]
  · rw [lam, erase1, Finset.prod_pair (by norm_num)]; norm_num [tnode]
  · rw [lam, erase2, Finset.prod_pair (by norm_num)]; norm_num [tnode]

/-- `Z = 1/5 + 1/4 + 1/20 = 1/2` at `m = 2`. -/
theorem Znorm_two : Znorm 2 = 1 / 2 := by
  obtain ⟨e0, e1, e2⟩ := lam_two_values
  rw [Znorm, show (2:ℕ) + 1 = 3 from rfl]
  rw [show (range 3) = ({0, 1, 2} : Finset ℕ) from by decide]
  rw [Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_singleton,
    e0, e1, e2]
  norm_num

/-- **The `4/5` bound of clause (iii) is TIGHT at `m = 2`**: `2|λ_0|/Z = 4/5` exactly, and the
correlation lower bound `437/581` is met with room (`437/581 < 4/5`). -/
theorem tilt_corr_two : 2 * |lam 2 0| / Znorm 2 = 4 / 5 := by
  rw [Znorm_two, lam_two_values.1]
  norm_num

/-- The `m = 2` node set really is `{0, 1, 5}`. -/
example : (tnode 0, tnode 1, tnode 2) = ((0:ℚ), 1, 5) := by norm_num [tnode]

/-- Equation (44) at `m = 2`, `i = 0`: `|λ_1|/|λ_0| = A_0·C_1 = 5/4`. -/
example : Afac 0 * Cfac 1 = 5 / 4 := by norm_num [Afac, Cfac]

/-- Equation (44) at `m = 2`, `i = 1`: `|λ_5|/|λ_0| = A_1·C_0 = 1/4`. -/
example : Afac 1 * Cfac 0 = 1 / 4 := by norm_num [Afac, Cfac]

#print axioms one_sub_sum_le_prod_one_sub
#print axioms tilt_corr_lower_bound
#print axioms tilt_gap
#print axioms tilt_corr_gt_three_quarters
#print axioms tnode_injective
#print axioms tilt_annihilates_low_degree
#print axioms Cfac_le
#print axioms sum_Afac_le
#print axioms lam_ratio
#print axioms tilt_corr_eq
#print axioms tilt_corr_ge
#print axioms tilt_rho_le_four_fifths
#print axioms abs_lam_one_ge
#print axioms abs_lam_two_ge
#print axioms lam_two_values
#print axioms Znorm_two
#print axioms tilt_corr_two

end KsumAudit.Obstructions.TiltedBand
