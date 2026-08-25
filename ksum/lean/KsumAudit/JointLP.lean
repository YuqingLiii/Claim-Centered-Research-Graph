/-
current_claim_hash: sha256:19aa4b9b41e3cd4fc98755b31e9b47ae5d142320fa667e66fd36426082d06fbb

CURRENT CANONICAL CLAIM (verbatim from the node record):

  At the stated finite parameter sets, the exact rational joint-histogram LPs certify the listed separations as exact optima rather than one-sided bounds.

END CURRENT CANONICAL CLAIM

# `prop:joint-lp` — Exact finite joint-histogram separation, with DUAL certificates

DAG node: `KSUM.B4b.L2.JOINTLP` (`ksum/proof-dag/nodes/KSUM.B4b.L2.JOINTLP.yaml`).
claim_hash: sha256:19aa4b9b41e3cd4fc98755b31e9b47ae5d142320fa667e66fd36426082d06fbb

## Why this module exists (gap-closure batch 2, item H-6, 2026-08-01)

The node asserts exact rational LP **optima**. An optimum is a two-sided claim, so the proof record
delegates exact reconstruction to `ksum/tools/ksum_l2rr_exact_review.py`. The statement-fidelity review
therefore requested a dual certificate for each `(instance, degree, basis)` combination.

Those certificates now exist, recomputed exactly and independently by
`ksum/tools/ksum_jointlp_duals.py` (with `tools/exact_simplex.py`), archived at
`ksum/artifacts/logs_ksum_lean_gapclose2_20260731/jointlp_certificates.json`.  This module carries the
general duality lemma and the kernel-checked SUBSET of certificates named in
`ksum/artifacts/ksum_lean_gapclose2_20260731.md` §H-6.

## The program

Orbit variables `w : Fin W → ℚ` (one per orbit of the chosen basis, carrying the orbit's total
mass), constraints `M w = 0` (the falling-factorial moment rows of order `< d`) and `‖w‖₁ ≤ 1`;
maximize `⟨c, w⟩` where `c` is the orbit-mean of the ±1 sign function `F`.

## The certificate scheme

`OPT = min_y ‖c − Mᵀy‖_∞` is the LP dual.  A pair `(w, y)` with

  * `M w = 0`, `‖w‖₁ = 1`, `⟨c,w⟩ = B`  (primal attainment: `B` is achieved), and
  * `|c_j − (Mᵀy)_j| ≤ B` for every `j`  (dual certificate: `B` is an upper bound)

proves `B` is EXACTLY the optimum, by the two-line weak-duality computation below.  No LP solver
is trusted: the kernel re-checks finitely many rational identities.

House rules: no `sorry`, no `axiom`, no `native_decide`.
-/
import KsumAudit.ObstructionsCore

namespace KsumAudit.Obstructions.JointLP

open Finset

set_option linter.unusedSectionVars false

/-- The value set of the program: all `⟨c,w⟩` over feasible `w`. -/
def lpValues {W R : ℕ} (M : Fin R → Fin W → ℚ) (c : Fin W → ℚ) : Set ℚ :=
  {v | ∃ w : Fin W → ℚ, (∀ r, ∑ j, M r j * w j = 0) ∧ (∑ j, |w j|) ≤ 1
        ∧ v = ∑ j, c j * w j}

/-- **Weak duality.**  `⟨c,w⟩ = ⟨c − Mᵀy, w⟩ + ⟨y, Mw⟩ ≤ ‖c − Mᵀy‖_∞ ‖w‖₁`. -/
theorem lp_weak_duality {W R : ℕ} (M : Fin R → Fin W → ℚ) (c : Fin W → ℚ)
    (w : Fin W → ℚ) (y : Fin R → ℚ) (B : ℚ) (hB : 0 ≤ B)
    (hfeas : ∀ r, ∑ j, M r j * w j = 0)
    (hl1 : (∑ j, |w j|) ≤ 1)
    (hdual : ∀ j, |c j - ∑ r, M r j * y r| ≤ B) :
    (∑ j, c j * w j) ≤ B := by
  classical
  have hcross : ∑ j, (∑ r, M r j * y r) * w j = 0 := by
    have hexp : ∀ j : Fin W, (∑ r, M r j * y r) * w j = ∑ r, y r * (M r j * w j) := by
      intro j
      rw [Finset.sum_mul]
      exact Finset.sum_congr rfl fun r _ => by ring
    have : ∑ j, (∑ r, M r j * y r) * w j = ∑ r, y r * ∑ j, M r j * w j := by
      rw [Finset.sum_congr rfl (fun j (_ : j ∈ univ) => hexp j), Finset.sum_comm]
      exact Finset.sum_congr rfl fun r _ => (Finset.mul_sum _ _ _).symm
    rw [this]
    exact Finset.sum_eq_zero fun r _ => by rw [hfeas r, mul_zero]
  have hsplit : ∑ j, c j * w j = ∑ j, (c j - ∑ r, M r j * y r) * w j := by
    have : ∀ j : Fin W, c j * w j
        = (c j - ∑ r, M r j * y r) * w j + (∑ r, M r j * y r) * w j := fun j => by ring
    rw [Finset.sum_congr rfl (fun j (_ : j ∈ univ) => this j), Finset.sum_add_distrib, hcross,
      add_zero]
  rw [hsplit]
  calc ∑ j, (c j - ∑ r, M r j * y r) * w j
      ≤ ∑ j, B * |w j| := by
        refine Finset.sum_le_sum fun j _ => ?_
        calc (c j - ∑ r, M r j * y r) * w j
            ≤ |(c j - ∑ r, M r j * y r) * w j| := le_abs_self _
          _ = |c j - ∑ r, M r j * y r| * |w j| := abs_mul _ _
          _ ≤ B * |w j| := mul_le_mul_of_nonneg_right (hdual j) (abs_nonneg _)
    _ = B * ∑ j, |w j| := by rw [Finset.mul_sum]
    _ ≤ B * 1 := mul_le_mul_of_nonneg_left hl1 hB
    _ = B := mul_one B

/-- **The optimum, certified.**  A primal witness attaining `B` together with a dual vector
bounding the residual by `B` proves `B` is exactly the optimum. -/
theorem lp_optimum {W R : ℕ} (M : Fin R → Fin W → ℚ) (c : Fin W → ℚ)
    (w : Fin W → ℚ) (y : Fin R → ℚ) (B : ℚ) (hB : 0 ≤ B)
    (hfeas : ∀ r, ∑ j, M r j * w j = 0)
    (hl1 : (∑ j, |w j|) = 1)
    (hval : (∑ j, c j * w j) = B)
    (hdual : ∀ j, |c j - ∑ r, M r j * y r| ≤ B) :
    IsGreatest (lpValues M c) B := by
  refine ⟨⟨w, hfeas, le_of_eq hl1, hval.symm⟩, ?_⟩
  rintro v ⟨w', hf, hn, rfl⟩
  exact lp_weak_duality M c w' y B hB hf hn hdual


/-! ## The kernel-checked certificates

Data emitted by `ksum/tools/ksum_jointlp_emit_lean.py` from
`ksum/artifacts/logs_ksum_lean_gapclose2_20260731/jointlp_certificates.json`; every literal below is an
exact rational recomputed by `ksum/tools/ksum_jointlp_duals.py` and re-verified in the kernel by the
four goals of `lp_optimum`.

**Which cases, and why these.**  All 24 (instance, basis, degree) LPs of `prop:joint-lp` have
exact primal+dual certificates in the JSON; the six below are the ones that DECIDE display (39)
for two of its three rows, and they are kernel-checked here:

  * `(3,3,0)` single, degree 1 — optimum `2/3`, NOT `> 2/3`, so the single-histogram certified
    degree is `0` (optima are non-increasing in the degree, since a higher-degree feasible point
    is feasible at every lower degree);
  * `(3,3,0)` joint, degrees 2 and 3 — optima `1 > 2/3` and `1/2 ≤ 2/3`, so the joint certified
    degree is exactly `2`;
  * `(5,4,1)` single, degree 3 — optimum `11/21 ≤ 2/3`, so the single certified degree is `2`;
  * `(5,4,1)` joint, degrees 3 and 4 — optima `5/7 > 2/3` and `3/5 ≤ 2/3`, so the joint certified
    degree is exactly `3`.

Together these give machine-checked `0 vs 2` at `(3,3,0)` and `2 vs 3` at `(5,4,1)` — the first
and third rows of (39), including its sharpest separation.  The `(4,3,0)` row and the remaining
degrees are certified in the JSON with the same scheme but are not kernel-checked here (see the
artifact's §H-6 for the size table). -/

/-! ### `(N,q,t) = (3,3,0)`, `single` basis, degree 1: OPT = 2/3
    3 orbit columns, 1 moment rows. -/

/-- Objective column `c` (orbit means of `F`). -/
def c_s330_single_d1 : Fin 3 → ℚ := ![(-1/3 : ℚ), (1/3 : ℚ), (1 : ℚ)]

/-- Moment matrix `M` (rows = falling-factorial rows of order < 1). -/
def M_s330_single_d1 : Fin 1 → Fin 3 → ℚ := ![![(1 : ℚ), (1 : ℚ), (1 : ℚ)]]

/-- Primal witness `w`: feasible, unit `ℓ¹`, value 2/3. -/
def w_s330_single_d1 : Fin 3 → ℚ := ![(-1/2 : ℚ), (0 : ℚ), (1/2 : ℚ)]

/-- Dual certificate `y`: `‖c - Mᵀy‖_∞ ≤ 2/3`. -/
def y_s330_single_d1 : Fin 1 → ℚ := ![(1/3 : ℚ)]

theorem opt_s330_single_d1 :
    IsGreatest (lpValues M_s330_single_d1 c_s330_single_d1) ((2/3 : ℚ)) := by
  refine lp_optimum M_s330_single_d1 c_s330_single_d1 w_s330_single_d1 y_s330_single_d1 ((2/3 : ℚ))
    (by norm_num) ?_ ?_ ?_ ?_
  · intro r
    fin_cases r
    all_goals norm_num [M_s330_single_d1, w_s330_single_d1, Fin.sum_univ_succ]
  · norm_num [w_s330_single_d1, Fin.sum_univ_succ]
  · norm_num [c_s330_single_d1, w_s330_single_d1, Fin.sum_univ_succ]
  · intro j
    fin_cases j
    all_goals norm_num [c_s330_single_d1, M_s330_single_d1, y_s330_single_d1, Fin.sum_univ_succ]

/-! ### `(N,q,t) = (3,3,0)`, `joint` basis, degree 2: OPT = 1
    6 orbit columns, 3 moment rows. -/

/-- Objective column `c` (orbit means of `F`). -/
def c_s330_joint_d2 : Fin 6 → ℚ := ![(-1 : ℚ), (1 : ℚ), (-1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ)]

/-- Moment matrix `M` (rows = falling-factorial rows of order < 2). -/
def M_s330_joint_d2 : Fin 3 → Fin 6 → ℚ := ![![(1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ)], ![(3/2 : ℚ), (3/2 : ℚ), (1 : ℚ), (1 : ℚ), (1/2 : ℚ), (0 : ℚ)], ![(0 : ℚ), (0 : ℚ), (1 : ℚ), (1 : ℚ), (2 : ℚ), (3 : ℚ)]]

/-- Primal witness `w`: feasible, unit `ℓ¹`, value 1. -/
def w_s330_joint_d2 : Fin 6 → ℚ := ![(-1/2 : ℚ), (1/2 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)]

/-- Dual certificate `y`: `‖c - Mᵀy‖_∞ ≤ 1`. -/
def y_s330_joint_d2 : Fin 3 → ℚ := ![(0 : ℚ), (0 : ℚ), (0 : ℚ)]

theorem opt_s330_joint_d2 :
    IsGreatest (lpValues M_s330_joint_d2 c_s330_joint_d2) ((1 : ℚ)) := by
  refine lp_optimum M_s330_joint_d2 c_s330_joint_d2 w_s330_joint_d2 y_s330_joint_d2 ((1 : ℚ))
    (by norm_num) ?_ ?_ ?_ ?_
  · intro r
    fin_cases r
    all_goals norm_num [M_s330_joint_d2, w_s330_joint_d2, Fin.sum_univ_succ]
  · norm_num [w_s330_joint_d2, Fin.sum_univ_succ]
  · norm_num [c_s330_joint_d2, w_s330_joint_d2, Fin.sum_univ_succ]
  · intro j
    fin_cases j
    all_goals norm_num [c_s330_joint_d2, M_s330_joint_d2, y_s330_joint_d2, Fin.sum_univ_succ]

/-! ### `(N,q,t) = (3,3,0)`, `joint` basis, degree 3: OPT = 1/2
    6 orbit columns, 7 moment rows. -/

/-- Objective column `c` (orbit means of `F`). -/
def c_s330_joint_d3 : Fin 6 → ℚ := ![(-1 : ℚ), (1 : ℚ), (-1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ)]

/-- Moment matrix `M` (rows = falling-factorial rows of order < 3). -/
def M_s330_joint_d3 : Fin 7 → Fin 6 → ℚ := ![![(1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ)], ![(3/2 : ℚ), (3/2 : ℚ), (1 : ℚ), (1 : ℚ), (1/2 : ℚ), (0 : ℚ)], ![(0 : ℚ), (0 : ℚ), (1 : ℚ), (1 : ℚ), (2 : ℚ), (3 : ℚ)], ![(3 : ℚ), (1 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)], ![(0 : ℚ), (2 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ)], ![(0 : ℚ), (0 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (0 : ℚ)], ![(0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (2 : ℚ), (6 : ℚ)]]

/-- Primal witness `w`: feasible, unit `ℓ¹`, value 1/2. -/
def w_s330_joint_d3 : Fin 6 → ℚ := ![(1/8 : ℚ), (0 : ℚ), (-3/8 : ℚ), (0 : ℚ), (3/8 : ℚ), (-1/8 : ℚ)]

/-- Dual certificate `y`: `‖c - Mᵀy‖_∞ ≤ 1/2`. -/
def y_s330_joint_d3 : Fin 7 → ℚ := ![(-3/2 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (3/2 : ℚ), (0 : ℚ), (0 : ℚ)]

theorem opt_s330_joint_d3 :
    IsGreatest (lpValues M_s330_joint_d3 c_s330_joint_d3) ((1/2 : ℚ)) := by
  refine lp_optimum M_s330_joint_d3 c_s330_joint_d3 w_s330_joint_d3 y_s330_joint_d3 ((1/2 : ℚ))
    (by norm_num) ?_ ?_ ?_ ?_
  · intro r
    fin_cases r
    all_goals norm_num [M_s330_joint_d3, w_s330_joint_d3, Fin.sum_univ_succ]
  · norm_num [w_s330_joint_d3, Fin.sum_univ_succ]
  · norm_num [c_s330_joint_d3, w_s330_joint_d3, Fin.sum_univ_succ]
  · intro j
    fin_cases j
    all_goals norm_num [c_s330_joint_d3, M_s330_joint_d3, y_s330_joint_d3, Fin.sum_univ_succ]

/-! ### `(N,q,t) = (5,4,1)`, `single` basis, degree 3: OPT = 11/21
    6 orbit columns, 4 moment rows. -/

/-- Objective column `c` (orbit means of `F`). -/
def c_s541_single_d3 : Fin 6 → ℚ := ![(-1 : ℚ), (-1/3 : ℚ), (-1/3 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ)]

/-- Moment matrix `M` (rows = falling-factorial rows of order < 3). -/
def M_s541_single_d3 : Fin 4 → Fin 6 → ℚ := ![![(1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ)], ![(5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ)], ![(5 : ℚ), (3 : ℚ), (2 : ℚ), (3/2 : ℚ), (1 : ℚ), (1/2 : ℚ)], ![(0 : ℚ), (2/3 : ℚ), (1 : ℚ), (7/6 : ℚ), (4/3 : ℚ), (3/2 : ℚ)]]

/-- Primal witness `w`: feasible, unit `ℓ¹`, value 11/21. -/
def w_s541_single_d3 : Fin 6 → ℚ := ![(1/14 : ℚ), (0 : ℚ), (-1/2 : ℚ), (3/7 : ℚ), (0 : ℚ), (0 : ℚ)]

/-- Dual certificate `y`: `‖c - Mᵀy‖_∞ ≤ 11/21`. -/
def y_s541_single_d3 : Fin 4 → ℚ := ![(-32/21 : ℚ), (0 : ℚ), (0 : ℚ), (12/7 : ℚ)]

theorem opt_s541_single_d3 :
    IsGreatest (lpValues M_s541_single_d3 c_s541_single_d3) ((11/21 : ℚ)) := by
  refine lp_optimum M_s541_single_d3 c_s541_single_d3 w_s541_single_d3 y_s541_single_d3 ((11/21 : ℚ))
    (by norm_num) ?_ ?_ ?_ ?_
  · intro r
    fin_cases r
    all_goals norm_num [M_s541_single_d3, w_s541_single_d3, Fin.sum_univ_succ]
  · norm_num [w_s541_single_d3, Fin.sum_univ_succ]
  · norm_num [c_s541_single_d3, w_s541_single_d3, Fin.sum_univ_succ]
  · intro j
    fin_cases j
    all_goals norm_num [c_s541_single_d3, M_s541_single_d3, y_s541_single_d3, Fin.sum_univ_succ]

/-! ### `(N,q,t) = (5,4,1)`, `joint` basis, degree 3: OPT = 5/7
    10 orbit columns, 5 moment rows. -/

/-- Objective column `c` (orbit means of `F`). -/
def c_s541_joint_d3 : Fin 10 → ℚ := ![(-1 : ℚ), (1 : ℚ), (1 : ℚ), (-1 : ℚ), (1 : ℚ), (1 : ℚ), (-1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ)]

/-- Moment matrix `M` (rows = falling-factorial rows of order < 3). -/
def M_s541_joint_d3 : Fin 5 → Fin 10 → ℚ := ![![(1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ)], ![(5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ)], ![(5 : ℚ), (3 : ℚ), (2 : ℚ), (3 : ℚ), (3/2 : ℚ), (1 : ℚ), (2 : ℚ), (1 : ℚ), (3/2 : ℚ), (1/2 : ℚ)], ![(0 : ℚ), (2 : ℚ), (3 : ℚ), (0 : ℚ), (3/2 : ℚ), (2 : ℚ), (0 : ℚ), (1 : ℚ), (1/2 : ℚ), (3/2 : ℚ)], ![(0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (3/2 : ℚ), (3/2 : ℚ), (3/2 : ℚ), (3/2 : ℚ)]]

/-- Primal witness `w`: feasible, unit `ℓ¹`, value 5/7. -/
def w_s541_joint_d3 : Fin 10 → ℚ := ![(1/14 : ℚ), (0 : ℚ), (-1/14 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (-3/7 : ℚ), (0 : ℚ), (3/7 : ℚ), (0 : ℚ)]

/-- Dual certificate `y`: `‖c - Mᵀy‖_∞ ≤ 5/7`. -/
def y_s541_joint_d3 : Fin 5 → ℚ := ![(-12/7 : ℚ), (0 : ℚ), (0 : ℚ), (8/7 : ℚ), (20/21 : ℚ)]

theorem opt_s541_joint_d3 :
    IsGreatest (lpValues M_s541_joint_d3 c_s541_joint_d3) ((5/7 : ℚ)) := by
  refine lp_optimum M_s541_joint_d3 c_s541_joint_d3 w_s541_joint_d3 y_s541_joint_d3 ((5/7 : ℚ))
    (by norm_num) ?_ ?_ ?_ ?_
  · intro r
    fin_cases r
    all_goals norm_num [M_s541_joint_d3, w_s541_joint_d3, Fin.sum_univ_succ]
  · norm_num [w_s541_joint_d3, Fin.sum_univ_succ]
  · norm_num [c_s541_joint_d3, w_s541_joint_d3, Fin.sum_univ_succ]
  · intro j
    fin_cases j
    all_goals norm_num [c_s541_joint_d3, M_s541_joint_d3, y_s541_joint_d3, Fin.sum_univ_succ]

/-! ### `(N,q,t) = (5,4,1)`, `joint` basis, degree 4: OPT = 3/5
    10 orbit columns, 9 moment rows. -/

/-- Objective column `c` (orbit means of `F`). -/
def c_s541_joint_d4 : Fin 10 → ℚ := ![(-1 : ℚ), (1 : ℚ), (1 : ℚ), (-1 : ℚ), (1 : ℚ), (1 : ℚ), (-1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ)]

/-- Moment matrix `M` (rows = falling-factorial rows of order < 4). -/
def M_s541_joint_d4 : Fin 9 → Fin 10 → ℚ := ![![(1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ)], ![(5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ), (5/4 : ℚ)], ![(5 : ℚ), (3 : ℚ), (2 : ℚ), (3 : ℚ), (3/2 : ℚ), (1 : ℚ), (2 : ℚ), (1 : ℚ), (3/2 : ℚ), (1/2 : ℚ)], ![(0 : ℚ), (2 : ℚ), (3 : ℚ), (0 : ℚ), (3/2 : ℚ), (2 : ℚ), (0 : ℚ), (1 : ℚ), (1/2 : ℚ), (3/2 : ℚ)], ![(0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (1 : ℚ), (1 : ℚ), (3/2 : ℚ), (3/2 : ℚ), (3/2 : ℚ), (3/2 : ℚ)], ![(15 : ℚ), (6 : ℚ), (3/2 : ℚ), (6 : ℚ), (3/2 : ℚ), (0 : ℚ), (3/2 : ℚ), (0 : ℚ), (3/2 : ℚ), (0 : ℚ)], ![(0 : ℚ), (3 : ℚ), (9/2 : ℚ), (0 : ℚ), (3/2 : ℚ), (2 : ℚ), (0 : ℚ), (1/2 : ℚ), (0 : ℚ), (1/2 : ℚ)], ![(0 : ℚ), (0 : ℚ), (0 : ℚ), (3/2 : ℚ), (3/4 : ℚ), (1/2 : ℚ), (9/4 : ℚ), (5/4 : ℚ), (3/2 : ℚ), (1/2 : ℚ)], ![(0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (3/4 : ℚ), (1 : ℚ), (0 : ℚ), (1 : ℚ), (3/4 : ℚ), (7/4 : ℚ)]]

/-- Primal witness `w`: feasible, unit `ℓ¹`, value 3/5. -/
def w_s541_joint_d4 : Fin 10 → ℚ := ![(0 : ℚ), (1/30 : ℚ), (0 : ℚ), (-1/10 : ℚ), (0 : ℚ), (0 : ℚ), (-1/5 : ℚ), (0 : ℚ), (7/15 : ℚ), (-1/5 : ℚ)]

/-- Dual certificate `y`: `‖c - Mᵀy‖_∞ ≤ 3/5`. -/
def y_s541_joint_d4 : Fin 9 → ℚ := ![(-22/5 : ℚ), (0 : ℚ), (0 : ℚ), (8/5 : ℚ), (12/5 : ℚ), (4/15 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)]

theorem opt_s541_joint_d4 :
    IsGreatest (lpValues M_s541_joint_d4 c_s541_joint_d4) ((3/5 : ℚ)) := by
  refine lp_optimum M_s541_joint_d4 c_s541_joint_d4 w_s541_joint_d4 y_s541_joint_d4 ((3/5 : ℚ))
    (by norm_num) ?_ ?_ ?_ ?_
  · intro r
    fin_cases r
    all_goals norm_num [M_s541_joint_d4, w_s541_joint_d4, Fin.sum_univ_succ]
  · norm_num [w_s541_joint_d4, Fin.sum_univ_succ]
  · norm_num [c_s541_joint_d4, w_s541_joint_d4, Fin.sum_univ_succ]
  · intro j
    fin_cases j
    all_goals norm_num [c_s541_joint_d4, M_s541_joint_d4, y_s541_joint_d4, Fin.sum_univ_succ]


/-- The certification predicate of the manuscript: *"call the largest `d` whose exact optimum is
strictly greater than `2/3` the LP-certified degree"*.  Recorded so the `> 2/3` / `≤ 2/3` verdicts
below are read against the manuscript's own cut-off. -/
def CertifiesAt (B : ℚ) : Prop := (2:ℚ)/3 < B

#print axioms lp_weak_duality
#print axioms lp_optimum
#print axioms opt_s330_single_d1
#print axioms opt_s330_joint_d2
#print axioms opt_s330_joint_d3
#print axioms opt_s541_single_d3
#print axioms opt_s541_joint_d3
#print axioms opt_s541_joint_d4

end KsumAudit.Obstructions.JointLP
