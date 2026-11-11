import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.Tactic

/-!
# WHGAP defect-Choi spectrum core (DAG protocol §7.3 support module)

**Serves** the node module `WHGAP.«signed-lift-extension»` (P2) — the 27×27 defect Choi
matrix `C_x` of the residual family at the forced point is that node's central object —
and, through it, `WHGAP.«zero-capacity-application»` (P4).  Commissioned by
`channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_LEAN2_20260731.md`, work
package A.  No node Claim lives in this file: it is a definition plus the *basis-free
algebraic core* of paper Theorem 3.3's proof.

**R12 minor m4 (2026-07-31): the "serves P2" relation is now a real dependency.**  Until this
repair, `WHGAP.«signed-lift-extension»` imported this module but used nothing from it, keeping
its own duplicate `lam5`/`lam3`.  Those duplicates were deleted; `lam5_nonneg_iff`,
`lam3_nonneg_iff` and `defect_eigenvalues_sign` of that node module are now stated about
`DefectChoi.lam5`/`lam3` below, so there is one definition of each branch in the whole tree and
no drift hazard.

## What is defined

`Cmat x` is the 27×27 real matrix given **entry by entry** by the master formula of paper
Appendix A (`eq:master`), specialized to the forced point `p = 1/3`, `d = 2(1-x)/3` — i.e.
the fifteen Kronecker-delta patterns pairing the row index `(i,b,b')` with the column index
`(j,r,s)`, each weighted by the corresponding entry of the "forced value" column of the
Appendix A table.  Indices are packed as `(i,b,b') ↦ 9i + 3b + b' : Fin 27`.

## What is proved (unconditionally, for every real `x ≠ 0`)

* `Cmat_eq`         — the spectral decomposition `C_x = λ₅(x) Q₅ + λ₃(x) Q₃` in the
                      denominator-cleared integer form
                      `C_x = (λ₅/12) R₅ + (λ₃/16) R₃`;
* `annihilator`     — `C_x (C_x − λ₅·1) (C_x − λ₃·1) = 0`;
* `trace_Cmat`      — `Tr C_x = 5λ₅ + 3λ₃`;
* `trace_Cmat_sq`   — `Tr C_x² = 5λ₅² + 3λ₃²`;
* `Cmat_symm`       — `C_xᵀ = C_x`;
* `multiplicity_unique` — the consequence layer: for `λ₅, λ₃ ≠ 0` and `λ₅ ≠ λ₃` the two
                      trace identities force the multiplicities `(5, 3)` (and hence
                      `19` zeros), which together with the annihilator and symmetry is
                      exactly the spectrum statement `{0^19, λ₅^5, λ₃^3}` — **subject to the
                      three scope qualifications on that lemma's own docstring (R12 m6): the
                      symmetric-diagonalizability step is not formalized here, the
                      implication needs `x ∉ {1/3, 1/2, 5/6}`, and `m5`, `m3` are real
                      coefficients, not natural-number multiplicities**;
* `lam5_eq_zero_iff`, `lam3_eq_zero_iff`, `lam5_eq_lam3_iff` — the three coincidence
                      points `x = 1/2`, `x = 1/3`, `x = 5/6` at which that hypothesis fails;
* `sample_26_51`, `sample_4_7`, `sample_3_4` — the three Appendix C sample points, with
                      their exact rational eigenvalues;
* **`charpoly_Cmat` (LEAN-3 WP-E, 2026-08-01)** — the eigenvalue multiset as a single
                      polynomial identity, with **no side condition whatsoever**:
                      `charpoly (Cmat x) = X¹⁹ (X − C λ₅)⁵ (X − C λ₃)³` for every real `x`.
                      This SUPERSEDES the `multiplicity_unique` route for the multiset
                      statement: it needs neither the unformalized symmetric-diagonalizability
                      step nor the exclusion of the coincidence points, and it covers `x = 1/2`
                      (`charpoly_half`: `X²⁴(X − 8/9)³`, i.e. the eigenvalue multiset
                      `{0²⁴, (8/9)³}`).  **Corrected 2026-08-01 (R13 MAJOR-2): this line used
                      to read "i.e. the paper's `rank C = 3`", which does not follow — a
                      charpoly does not determine a rank.  See `rank_Cmat_half` below;**
* **`Cmat_half_factor`, `V3R_Cmat_half_V3R`, `rank_Cmat_half` (LEAN-3.2, 2026-08-01)** —
                      **`rank (Cmat (1/2)) = 3`**, paper Theorem 3.3(2) at the physically
                      decisive point, proved from the rank factorization `A₃ = V₃V₃ᵀ` with
                      `V₃ᵀV₃ = 16·1₃` and NOT inferred from `charpoly_half`.

with `λ₅(x) = 4(1−x)(2x−1)/x` and `λ₃(x) = 16(1−x)(3x−1)/(9x)`.

## Method (deviation from the commissioned route — see the WP-A report)

The commission froze a polynomial-identity-testing route (evaluate the denominator-cleared
triple product at seven rational points, conclude by interpolation).  A timed pilot showed
that **one** 27×27 integer matrix product costs 6 min 24 s of kernel reduction here, so the
frozen route (three products per point × seven points) was not affordable.  What is
implemented instead is strictly stronger and needs **no** degree bound, no sampling and no
`hdeg` hypothesis: the fifteen forced coefficients are shown (by sympy, then re-derived in
Lean by `ring`) to be constant combinations `c_k(x) = a_k λ₅(x) + b_k λ₃(x)`, so that
`C_x = λ₅ Q₅ + λ₃ Q₃` with `Q₅ = R₅/12`, `Q₃ = R₃/16` **independent of `x`**; and the two
integer matrices are given explicit rank factorizations `R₅ = W₅ V₅ᵀ`, `R₃ = V₃ V₃ᵀ` with
`V₅ᵀW₅ = 12·1₅`, `V₃ᵀV₃ = 16·1₃`, `V₅ᵀV₃ = 0`, `V₃ᵀW₅ = 0`.  Idempotency, orthogonality and
the traces then follow by matrix algebra (`Matrix.trace_mul_comm`) from four *small*
decidable checks (5×5, 3×3, 5×3, 3×5) plus two 729-entry factorization checks.  The
identity is thereby proved for **all** `x ≠ 0`, not at sample points.

## Honesty note (§7.9 scope)

This file checks the **displayed entrywise formula** of Appendix A and its algebraic
consequences.  It does **not** construct the channel `Λ_x`, its complement, the signed lift,
or the defect map: that `Cmat x` really is the defect Choi matrix of the residual family is
*not* checked here and remains a prose/sympy result (P2, R2-reviewed; the 729-entry
agreement of `eq:master` with the independent direct construction is re-verified as gate V1
of `tools/whgap_lean2_wpa_codegen.py`).  Nor is the `SO(3)` spin reduction, the Gram data
`4/25`, `1/3`, or the Zhu–Wang factorization at `x = 1/2` formalized.  A green build here
establishes the spectrum theorem's **basis-free core**, conditional on nothing.
-/

set_option maxHeartbeats 1000000
set_option maxRecDepth 20000

namespace WHGAP.DefectChoi

open Matrix

/-- Packed tensor index: `(i, b, b') ↦ 9i + 3b + b'`. -/
abbrev Idx := Fin 27

/-- First (`A`-leg) component of a packed index. -/
def leg1 (I : Idx) : ℕ := I.val / 9
/-- Second (`B`-leg) component of a packed index. -/
def leg2 (I : Idx) : ℕ := I.val / 3 % 3
/-- Third (`B'`-leg) component of a packed index. -/
def leg3 (I : Idx) : ℕ := I.val % 3

/-- Kronecker delta on the unpacked legs. -/
def dl (a b : ℕ) : ℤ := if a = b then 1 else 0

/-- The fifteen delta patterns of paper Appendix A `eq:master`, in the table's own order
`k = 1, …, 15`; row index `(i,b,b')`, column index `(j,r,s)`.  Any other `k` gives `0`. -/
def pat (k : ℕ) (I J : Idx) : ℤ :=
  let i := leg1 I; let b := leg2 I; let bp := leg3 I
  let j := leg1 J; let r := leg2 J; let s := leg3 J
  match k with
  | 1  => dl i b  * dl bp j  * dl r s     -- δ_ib  δ_b'j δ_rs
  | 2  => dl i b  * dl bp r  * dl j s     -- δ_ib  δ_b'r δ_js
  | 3  => dl i b  * dl bp s  * dl j r     -- δ_ib  δ_b's δ_jr
  | 4  => dl i bp * dl b j   * dl r s     -- δ_ib' δ_bj  δ_rs
  | 5  => dl i bp * dl b r   * dl j s     -- δ_ib' δ_br  δ_js
  | 6  => dl i bp * dl b s   * dl j r     -- δ_ib' δ_bs  δ_jr
  | 7  => dl i j  * dl b bp  * dl r s     -- δ_ij  δ_bb' δ_rs
  | 8  => dl i j  * dl b r   * dl bp s    -- δ_ij  δ_br  δ_b's
  | 9  => dl i j  * dl b s   * dl bp r    -- δ_ij  δ_bs  δ_b'r
  | 10 => dl i r  * dl b bp  * dl j s     -- δ_ir  δ_bb' δ_js
  | 11 => dl i r  * dl b j   * dl bp s    -- δ_ir  δ_bj  δ_b's
  | 12 => dl i r  * dl b s   * dl bp j    -- δ_ir  δ_bs  δ_b'j
  | 13 => dl i s  * dl b bp  * dl j r     -- δ_is  δ_bb' δ_jr
  | 14 => dl i s  * dl b j   * dl bp r    -- δ_is  δ_bj  δ_b'r
  | 15 => dl i s  * dl b r   * dl bp j    -- δ_is  δ_br  δ_b'j
  | _  => 0

/-! ## The two eigenvalue branches (paper Theorem 3.3) -/

/-- `λ₅(x) = 4(1−x)(2x−1)/x`, the spin-2 branch (multiplicity 5). -/
noncomputable def lam5 (x : ℝ) : ℝ := 4 * (1 - x) * (2 * x - 1) / x

/-- `λ₃(x) = 16(1−x)(3x−1)/(9x)`, the spin-1 branch (multiplicity 3). -/
noncomputable def lam3 (x : ℝ) : ℝ := 16 * (1 - x) * (3 * x - 1) / (9 * x)

/-- The fifteen forced-point coefficients `c_k(x)` of the Appendix A table
(`p = 1/3`, `d = 2(1−x)/3`), transcribed verbatim from its "forced value" column. -/
noncomputable def cco (x : ℝ) : ℕ → ℝ
  | 1  =>   2 * (x - 1) * (3 * x - 1) / (9 * x)
  | 2  => -(2 * (x - 1) * (3 * x - 1)) / (9 * x)
  | 3  => -(4 * (x - 1) * (3 * x - 1)) / (9 * x)
  | 4  => -((x - 1) * (15 * x - 8)) / (9 * x)
  | 5  =>   (x - 1) * (15 * x - 8) / (9 * x)
  | 6  => -(2 * (x - 1) * (3 * x - 1)) / (9 * x)
  | 7  =>   (x - 1) * (15 * x - 8) / (9 * x)
  | 8  => -(4 * (x - 1) * (2 * x - 1)) / (3 * x)
  | 9  => -(2 * (x - 1) * (2 * x - 1)) / (3 * x)
  | 10 => -((x - 1) * (15 * x - 8)) / (9 * x)
  | 11 =>   4 * (x - 1) * (2 * x - 1) / (3 * x)
  | 12 =>   2 * (x - 1) * (2 * x - 1) / (3 * x)
  | 13 =>   2 * (x - 1) * (3 * x - 1) / (9 * x)
  | 14 =>   2 * (x - 1) * (2 * x - 1) / (3 * x)
  | 15 => -(2 * (x - 1) * (2 * x - 1)) / (3 * x)
  | _  => 0

/-- **The defect Choi matrix at the forced point**, entry by entry from `eq:master`. -/
noncomputable def Cmat (x : ℝ) : Matrix Idx Idx ℝ := Matrix.of fun I J =>
  cco x 1 * (pat 1 I J : ℝ) + cco x 2 * (pat 2 I J : ℝ) + cco x 3 * (pat 3 I J : ℝ)
  + cco x 4 * (pat 4 I J : ℝ) + cco x 5 * (pat 5 I J : ℝ) + cco x 6 * (pat 6 I J : ℝ)
  + cco x 7 * (pat 7 I J : ℝ) + cco x 8 * (pat 8 I J : ℝ) + cco x 9 * (pat 9 I J : ℝ)
  + cco x 10 * (pat 10 I J : ℝ) + cco x 11 * (pat 11 I J : ℝ) + cco x 12 * (pat 12 I J : ℝ)
  + cco x 13 * (pat 13 I J : ℝ) + cco x 14 * (pat 14 I J : ℝ) + cco x 15 * (pat 15 I J : ℝ)

/-! ## The two `x`-independent projection carriers, in integer form -/

/-- `R₅ = 12 Q₅`: the spin-2 projection, cleared of denominators. -/
def R5 : Matrix Idx Idx ℤ := Matrix.of fun I J =>
  3 * pat 4 I J - 3 * pat 5 I J - 3 * pat 7 I J + 4 * pat 8 I J + 2 * pat 9 I J
  + 3 * pat 10 I J - 4 * pat 11 I J - 2 * pat 12 I J - 2 * pat 14 I J + 2 * pat 15 I J

/-- `R₃ = 16 Q₃`: the spin-1 projection, cleared of denominators. -/
def R3 : Matrix Idx Idx ℤ := Matrix.of fun I J =>
  -2 * pat 1 I J + 2 * pat 2 I J + 4 * pat 3 I J - pat 4 I J + pat 5 I J
  + 2 * pat 6 I J + pat 7 I J - pat 10 I J - 2 * pat 13 I J

/-- Integer basis of the range of `R₅` (five pairwise orthogonal columns). -/
def V5 : Matrix Idx (Fin 5) ℤ :=
  !![0, 0, 0, 0, 0;
    0, 0, 0, 0, 0;
    0, 0, 0, 0, 0;
    1, 0, 0, 0, 0;
    0, 1, 0, 0, 0;
    0, 0, 2, 0, 0;
    0, 0, 0, 1, 0;
    0, 0, 1, 0, 1;
    0, -1, 0, 0, 0;
    -1, 0, 0, 0, 0;
    0, -1, 0, 0, 0;
    0, 0, -2, 0, 0;
    0, 0, 0, 0, 0;
    0, 0, 0, 0, 0;
    0, 0, 0, 0, 0;
    0, 0, -1, 0, 1;
    0, 0, 0, -1, 0;
    1, 0, 0, 0, 0;
    0, 0, 0, -1, 0;
    0, 0, -1, 0, -1;
    0, 1, 0, 0, 0;
    0, 0, 1, 0, -1;
    0, 0, 0, 1, 0;
    -1, 0, 0, 0, 0;
    0, 0, 0, 0, 0;
    0, 0, 0, 0, 0;
    0, 0, 0, 0, 0]

/-- `W₅ = V₅ E₅` with `E₅ = diag(3,3,1,3,3)`: the column rescaling that makes
`V₅ᵀ W₅ = 12·1₅`. -/
def W5 : Matrix Idx (Fin 5) ℤ :=
  !![0, 0, 0, 0, 0;
    0, 0, 0, 0, 0;
    0, 0, 0, 0, 0;
    3, 0, 0, 0, 0;
    0, 3, 0, 0, 0;
    0, 0, 2, 0, 0;
    0, 0, 0, 3, 0;
    0, 0, 1, 0, 3;
    0, -3, 0, 0, 0;
    -3, 0, 0, 0, 0;
    0, -3, 0, 0, 0;
    0, 0, -2, 0, 0;
    0, 0, 0, 0, 0;
    0, 0, 0, 0, 0;
    0, 0, 0, 0, 0;
    0, 0, -1, 0, 3;
    0, 0, 0, -3, 0;
    3, 0, 0, 0, 0;
    0, 0, 0, -3, 0;
    0, 0, -1, 0, -3;
    0, 3, 0, 0, 0;
    0, 0, 1, 0, -3;
    0, 0, 0, 3, 0;
    -3, 0, 0, 0, 0;
    0, 0, 0, 0, 0;
    0, 0, 0, 0, 0;
    0, 0, 0, 0, 0]

/-- Integer basis of the range of `R₃` (three pairwise orthogonal columns of equal norm). -/
def V3 : Matrix Idx (Fin 3) ℤ :=
  !![2, 0, 0;
    0, 2, 0;
    0, 0, 2;
    0, 1, 0;
    -1, 0, 0;
    0, 0, 0;
    0, 0, 1;
    0, 0, 0;
    -1, 0, 0;
    0, -1, 0;
    1, 0, 0;
    0, 0, 0;
    2, 0, 0;
    0, 2, 0;
    0, 0, 2;
    0, 0, 0;
    0, 0, 1;
    0, -1, 0;
    0, 0, -1;
    0, 0, 0;
    1, 0, 0;
    0, 0, 0;
    0, 0, -1;
    0, 1, 0;
    2, 0, 0;
    0, 2, 0;
    0, 0, 2]

/-- The diagonal rescaling `E₅ = diag(3,3,1,3,3)`. -/
def E5 : Matrix (Fin 5) (Fin 5) ℤ :=
  !![3, 0, 0, 0, 0;
    0, 3, 0, 0, 0;
    0, 0, 1, 0, 0;
    0, 0, 0, 3, 0;
    0, 0, 0, 0, 3]

/-! ### The six decidable certificate identities -/

theorem V5T_W5 : V5ᵀ * W5 = (12 : ℤ) • (1 : Matrix (Fin 5) (Fin 5) ℤ) := by
  ext i j; revert i j; decide

theorem V3T_V3 : V3ᵀ * V3 = (16 : ℤ) • (1 : Matrix (Fin 3) (Fin 3) ℤ) := by
  ext i j; revert i j; decide

theorem V5T_V3 : V5ᵀ * V3 = 0 := by ext i j; revert i j; decide

theorem V3T_W5 : V3ᵀ * W5 = 0 := by ext i j; revert i j; decide

theorem W5_eq : W5 = V5 * E5 := by ext i j; revert i j; decide

theorem E5_symm : E5ᵀ = E5 := by ext i j; revert i j; decide

theorem R5_factor : R5 = W5 * V5ᵀ := by ext i j; revert i j; decide

theorem R3_factor : R3 = V3 * V3ᵀ := by ext i j; revert i j; decide

/-! ### Consequences over `ℤ`: two orthogonal (scaled) idempotents -/

theorem R5_sq : R5 * R5 = (12 : ℤ) • R5 := by
  rw [R5_factor]
  calc W5 * V5ᵀ * (W5 * V5ᵀ) = W5 * ((V5ᵀ * W5) * V5ᵀ) := by simp only [Matrix.mul_assoc]
    _ = W5 * (((12 : ℤ) • (1 : Matrix (Fin 5) (Fin 5) ℤ)) * V5ᵀ) := by rw [V5T_W5]
    _ = (12 : ℤ) • (W5 * V5ᵀ) := by
        rw [Matrix.smul_mul, Matrix.one_mul, Matrix.mul_smul]

theorem R3_sq : R3 * R3 = (16 : ℤ) • R3 := by
  rw [R3_factor]
  calc V3 * V3ᵀ * (V3 * V3ᵀ) = V3 * ((V3ᵀ * V3) * V3ᵀ) := by simp only [Matrix.mul_assoc]
    _ = V3 * (((16 : ℤ) • (1 : Matrix (Fin 3) (Fin 3) ℤ)) * V3ᵀ) := by rw [V3T_V3]
    _ = (16 : ℤ) • (V3 * V3ᵀ) := by
        rw [Matrix.smul_mul, Matrix.one_mul, Matrix.mul_smul]

theorem R5_R3 : R5 * R3 = 0 := by
  rw [R5_factor, R3_factor]
  calc W5 * V5ᵀ * (V3 * V3ᵀ) = W5 * ((V5ᵀ * V3) * V3ᵀ) := by simp only [Matrix.mul_assoc]
    _ = 0 := by rw [V5T_V3]; simp

theorem R3_R5 : R3 * R5 = 0 := by
  rw [R5_factor, R3_factor]
  calc V3 * V3ᵀ * (W5 * V5ᵀ) = V3 * ((V3ᵀ * W5) * V5ᵀ) := by simp only [Matrix.mul_assoc]
    _ = 0 := by rw [V3T_W5]; simp

theorem R5_trace : R5.trace = 60 := by
  rw [R5_factor, Matrix.trace_mul_comm, V5T_W5, Matrix.trace_smul, Matrix.trace_one]
  simp

theorem R3_trace : R3.trace = 48 := by
  rw [R3_factor, Matrix.trace_mul_comm, V3T_V3, Matrix.trace_smul, Matrix.trace_one]
  simp

theorem R5_symm : R5ᵀ = R5 := by
  rw [R5_factor, W5_eq]
  rw [Matrix.transpose_mul, Matrix.transpose_transpose, Matrix.transpose_mul, E5_symm]
  simp [Matrix.mul_assoc]

theorem R3_symm : R3ᵀ = R3 := by
  rw [R3_factor, Matrix.transpose_mul, Matrix.transpose_transpose]

/-! ### Transport to `ℝ` -/

/-- The `ℤ → ℝ` entrywise cast of a 27×27 integer matrix. -/
noncomputable def toR (M : Matrix Idx Idx ℤ) : Matrix Idx Idx ℝ := M.map (Int.castRingHom ℝ)

@[simp] theorem toR_apply (M : Matrix Idx Idx ℤ) (I J : Idx) :
    toR M I J = ((M I J : ℤ) : ℝ) := rfl

theorem toR_mul (A B : Matrix Idx Idx ℤ) : toR (A * B) = toR A * toR B :=
  Matrix.map_mul

theorem toR_zsmul (c : ℤ) (A : Matrix Idx Idx ℤ) : toR (c • A) = (c : ℝ) • toR A := by
  ext I J
  simp only [toR_apply, Matrix.smul_apply, smul_eq_mul, Int.cast_mul]

theorem toR_zero : toR (0 : Matrix Idx Idx ℤ) = 0 := by ext I J; simp

theorem toR_trace (A : Matrix Idx Idx ℤ) : (toR A).trace = (A.trace : ℝ) := by
  simp [Matrix.trace, Matrix.diag]

theorem toR_transpose (A : Matrix Idx Idx ℤ) : toR Aᵀ = (toR A)ᵀ := by ext I J; simp

/-- `A := 12 Q₅` over `ℝ`. -/
noncomputable abbrev A5 : Matrix Idx Idx ℝ := toR R5
/-- `B := 16 Q₃` over `ℝ`. -/
noncomputable abbrev A3 : Matrix Idx Idx ℝ := toR R3

theorem A5_sq : A5 * A5 = (12 : ℝ) • A5 := by
  rw [← toR_mul, R5_sq, toR_zsmul]; norm_num

theorem A3_sq : A3 * A3 = (16 : ℝ) • A3 := by
  rw [← toR_mul, R3_sq, toR_zsmul]; norm_num

theorem A5_A3 : A5 * A3 = 0 := by rw [← toR_mul, R5_R3, toR_zero]

theorem A3_A5 : A3 * A5 = 0 := by rw [← toR_mul, R3_R5, toR_zero]

theorem A5_trace : A5.trace = 60 := by rw [toR_trace, R5_trace]; norm_num

theorem A3_trace : A3.trace = 48 := by rw [toR_trace, R3_trace]; norm_num

theorem A5_symm : A5ᵀ = A5 := by rw [← toR_transpose, R5_symm]

theorem A3_symm : A3ᵀ = A3 := by rw [← toR_transpose, R3_symm]

/-! ## The spectral decomposition of `C_x` -/

/-- **The decomposition.**  For every `x ≠ 0`, the defect Choi matrix at the forced point is
`λ₅(x)` times a rank-5 projection plus `λ₃(x)` times a rank-3 projection, both independent
of `x`.  This is the whole content of paper Theorem 3.3, in basis-free form. -/
theorem Cmat_eq (x : ℝ) (hx : x ≠ 0) :
    Cmat x = (lam5 x / 12) • A5 + (lam3 x / 16) • A3 := by
  ext I J
  simp only [Cmat, R5, R3, A5, A3, Matrix.of_apply, Matrix.add_apply, Matrix.smul_apply,
    toR_apply, smul_eq_mul, cco, lam5, lam3]
  push_cast
  field_simp
  ring

/-! ### The generic two-projection algebra -/

private theorem sq_decomp {A B : Matrix Idx Idx ℝ} {p q a b : ℝ}
    (hA : A * A = p • A) (hB : B * B = q • B) (hAB : A * B = 0) (hBA : B * A = 0) :
    (a • A + b • B) * (a • A + b • B) = (a * a * p) • A + (b * b * q) • B := by
  simp only [Matrix.add_mul, Matrix.mul_add, Matrix.smul_mul, Matrix.mul_smul, hA, hB, hAB,
    hBA, smul_zero, add_zero, zero_add, smul_smul]
  module

private theorem triple_zero {A B : Matrix Idx Idx ℝ} {p q a b : ℝ}
    (hA : A * A = p • A) (hB : B * B = q • B) (hAB : A * B = 0) (hBA : B * A = 0) :
    (a • A + b • B) * ((a • A + b • B) - (p * a) • (1 : Matrix Idx Idx ℝ))
      * ((a • A + b • B) - (q * b) • (1 : Matrix Idx Idx ℝ)) = 0 := by
  have h2 : (a • A + b • B) * ((a • A + b • B) - (p * a) • (1 : Matrix Idx Idx ℝ))
      = (b * b * q - p * a * b) • B := by
    rw [Matrix.mul_sub, sq_decomp hA hB hAB hBA]
    simp only [Matrix.mul_smul, Matrix.mul_one]
    module
  have h3 : B * ((a • A + b • B) - (q * b) • (1 : Matrix Idx Idx ℝ)) = 0 := by
    simp only [Matrix.mul_sub, Matrix.mul_add, Matrix.mul_smul, Matrix.mul_one, hB, hBA,
      smul_zero, zero_add, smul_smul]
    module
  rw [h2, Matrix.smul_mul, h3, smul_zero]

/-! ### The three identities of paper Theorem 3.3 -/

/-- **Annihilating identity.**  `C_x (C_x − λ₅·1)(C_x − λ₃·1) = 0` for every `x ≠ 0`. -/
theorem annihilator (x : ℝ) (hx : x ≠ 0) :
    Cmat x * (Cmat x - lam5 x • (1 : Matrix Idx Idx ℝ))
      * (Cmat x - lam3 x • (1 : Matrix Idx Idx ℝ)) = 0 := by
  have h5 : lam5 x = 12 * (lam5 x / 12) := by ring
  have h3 : lam3 x = 16 * (lam3 x / 16) := by ring
  rw [Cmat_eq x hx]
  rw [show lam5 x • (1 : Matrix Idx Idx ℝ) = (12 * (lam5 x / 12)) • (1 : Matrix Idx Idx ℝ)
        from by rw [← h5],
      show lam3 x • (1 : Matrix Idx Idx ℝ) = (16 * (lam3 x / 16)) • (1 : Matrix Idx Idx ℝ)
        from by rw [← h3]]
  exact triple_zero A5_sq A3_sq A5_A3 A3_A5

/-- **First trace identity.**  `Tr C_x = 5λ₅ + 3λ₃`. -/
theorem trace_Cmat (x : ℝ) (hx : x ≠ 0) :
    (Cmat x).trace = 5 * lam5 x + 3 * lam3 x := by
  rw [Cmat_eq x hx, Matrix.trace_add, Matrix.trace_smul, Matrix.trace_smul, A5_trace, A3_trace]
  simp only [smul_eq_mul]
  ring

/-- **Second trace identity.**  `Tr C_x² = 5λ₅² + 3λ₃²`. -/
theorem trace_Cmat_sq (x : ℝ) (hx : x ≠ 0) :
    (Cmat x * Cmat x).trace = 5 * lam5 x ^ 2 + 3 * lam3 x ^ 2 := by
  rw [Cmat_eq x hx, sq_decomp A5_sq A3_sq A5_A3 A3_A5, Matrix.trace_add, Matrix.trace_smul,
    Matrix.trace_smul, A5_trace, A3_trace]
  simp only [smul_eq_mul]
  ring

/-- `C_x` is symmetric — the remaining hypothesis of the spectral theorem for real
symmetric matrices. -/
theorem Cmat_symm (x : ℝ) (hx : x ≠ 0) : (Cmat x)ᵀ = Cmat x := by
  rw [Cmat_eq x hx, Matrix.transpose_add, Matrix.transpose_smul, Matrix.transpose_smul,
    A5_symm, A3_symm]

/-! ## Consequence layer: the multiplicities are forced -/

/-- **Multiplicity solve.**  If two candidate multiplicities reproduce both trace values for
a pair of distinct nonzero eigenvalues, they are `5` and `3`.  Together with `annihilator`
(the spectrum is contained in `{0, λ₅, λ₃}`) and `Cmat_symm` (so `C_x` is diagonalizable
with real eigenvalues and `27` of them counted with multiplicity), this is exactly the
spectrum statement `{0^19, λ₅^5, λ₃^3}` of paper Theorem 3.3.

**SUPERSEDED FOR THE MULTISET STATEMENT (LEAN-3 WP-E, 2026-08-01).**  The spectral conclusion
is now available *directly and unconditionally* as `charpoly_Cmat` at the bottom of this file:
`charpoly (Cmat x) = X¹⁹ (X − C λ₅ x)⁵ (X − C λ₃ x)³` for every real `x`.  That identity
closes qualification 1 below (the symmetric-diagonalizability step is **no longer used**: the
multiplicities come out of the rectangular Weinstein–Aronszajn identity, and `Cmat_symm` is
not an input to it) and qualification 2 (the coincidence-point remark is **moot** for the
charpoly statement — at `x ∈ {1/3, 1/2, 5/6}` the multiset simply merges and the polynomial
identity still holds, see `charpoly_half`).  `multiplicity_unique` is retained as the record
of the trace-based argument, and its three qualifications below still describe *that* route
exactly; they no longer describe what the file establishes about the spectrum.

**Scope qualifications of THIS lemma's own route (R12 minor m6, added 2026-07-31).**  Three,
all of them limits on what the sentence above may be read as claiming:

1. **The symmetric-diagonalizability step is NOT formalized here.**  "Real symmetric ⟹
   orthogonally diagonalizable with `27` real eigenvalues, so `Tr C = ∑ λᵢ` and
   `Tr C² = ∑ λᵢ²`" is the bridge from `Cmat_symm` + the two trace identities to the
   hypotheses `e1`, `e2` below, and it is used *outside* Lean; nothing in this file supplies
   it.  What is proved here is only the arithmetic that follows once `e1` and `e2` are
   granted.
2. **The implication needs `x ∉ {1/3, 1/2, 5/6}`.**  The hypotheses `h5 : l5 ≠ 0`,
   `h3 : l3 ≠ 0`, `hne : l5 ≠ l3` fail exactly at those three points
   (`lam5_eq_zero_iff`, `lam3_eq_zero_iff`, `lam5_eq_lam3_iff` below), so the multiplicity
   conclusion does **not** cover the physically decisive point `x = 1/2` at which the paper
   claims `rank C = 3`.  *(That rank claim is now proved at `x = 1/2` by `rank_Cmat_half`
   below — LEAN-3.2, 2026-08-01 — by a route that uses neither this lemma nor
   diagonalizability.)*
3. **`m5`, `m3` are real coefficients, not natural-number multiplicities.**  The lemma is a
   statement in `ℝ` about the unique solution of a 2×2 linear system; that the solution is an
   integer pair is a conclusion of the arithmetic, not an assumption about counting. -/
theorem multiplicity_unique {l5 l3 m5 m3 : ℝ} (h5 : l5 ≠ 0) (h3 : l3 ≠ 0) (hne : l5 ≠ l3)
    (e1 : m5 * l5 + m3 * l3 = 5 * l5 + 3 * l3)
    (e2 : m5 * l5 ^ 2 + m3 * l3 ^ 2 = 5 * l5 ^ 2 + 3 * l3 ^ 2) :
    m5 = 5 ∧ m3 = 3 := by
  have key : (m3 - 3) * (l3 * (l3 - l5)) = 0 := by linear_combination e2 - l5 * e1
  have hm3 : m3 = 3 := by
    rcases mul_eq_zero.1 key with h | h
    · linarith
    · exact absurd h (mul_ne_zero h3 (sub_ne_zero.2 (Ne.symm hne)))
  refine ⟨?_, hm3⟩
  have : (m5 - 5) * l5 = 0 := by rw [hm3] at e1; linarith
  rcases mul_eq_zero.1 this with h | h
  · linarith
  · exact absurd h h5

/-! ### The three coincidence points at which `multiplicity_unique` does not apply -/

theorem lam5_eq_zero_iff {x : ℝ} (hx : 0 < x) (hx1 : x < 1) : lam5 x = 0 ↔ x = 1 / 2 := by
  rw [lam5, div_eq_zero_iff]
  constructor
  · rintro (h | h)
    · rcases mul_eq_zero.1 h with h' | h'
      · rcases mul_eq_zero.1 h' with h'' | h'' <;> [linarith; linarith]
      · linarith
    · linarith
  · rintro rfl; norm_num

theorem lam3_eq_zero_iff {x : ℝ} (hx : 0 < x) (hx1 : x < 1) : lam3 x = 0 ↔ x = 1 / 3 := by
  rw [lam3, div_eq_zero_iff]
  constructor
  · rintro (h | h)
    · rcases mul_eq_zero.1 h with h' | h'
      · rcases mul_eq_zero.1 h' with h'' | h'' <;> [linarith; linarith]
      · linarith
    · linarith
  · rintro rfl; norm_num

theorem lam5_eq_lam3_iff {x : ℝ} (hx : 0 < x) (hx1 : x < 1) :
    lam5 x = lam3 x ↔ x = 5 / 6 := by
  rw [lam5, lam3]
  rw [div_eq_div_iff (by linarith) (by linarith)]
  constructor
  · intro h
    have key : 4 * x * (1 - x) * (6 * x - 5) = 0 := by linear_combination h
    rcases mul_eq_zero.1 key with h' | h'
    · rcases mul_eq_zero.1 h' with h'' | h''
      · rcases mul_eq_zero.1 h'' with h3 | h3 <;> linarith
      · linarith
    · linarith
  · rintro rfl; norm_num

/-! ### The three Appendix C sample points -/

theorem sample_26_51 :
    Cmat (26 / 51) * (Cmat (26 / 51) - (50 / 663 : ℝ) • (1 : Matrix Idx Idx ℝ))
      * (Cmat (26 / 51) - (200 / 221 : ℝ) • (1 : Matrix Idx Idx ℝ)) = 0 := by
  have h1 : lam5 (26 / 51 : ℝ) = 50 / 663 := by rw [lam5]; norm_num
  have h2 : lam3 (26 / 51 : ℝ) = 200 / 221 := by rw [lam3]; norm_num
  rw [← h1, ← h2]
  exact annihilator _ (by norm_num)

theorem sample_4_7 :
    Cmat (4 / 7) * (Cmat (4 / 7) - (3 / 7 : ℝ) • (1 : Matrix Idx Idx ℝ))
      * (Cmat (4 / 7) - (20 / 21 : ℝ) • (1 : Matrix Idx Idx ℝ)) = 0 := by
  have h1 : lam5 (4 / 7 : ℝ) = 3 / 7 := by rw [lam5]; norm_num
  have h2 : lam3 (4 / 7 : ℝ) = 20 / 21 := by rw [lam3]; norm_num
  rw [← h1, ← h2]
  exact annihilator _ (by norm_num)

theorem sample_3_4 :
    Cmat (3 / 4) * (Cmat (3 / 4) - (2 / 3 : ℝ) • (1 : Matrix Idx Idx ℝ))
      * (Cmat (3 / 4) - (20 / 27 : ℝ) • (1 : Matrix Idx Idx ℝ)) = 0 := by
  have h1 : lam5 (3 / 4 : ℝ) = 2 / 3 := by rw [lam5]; norm_num
  have h2 : lam3 (3 / 4 : ℝ) = 20 / 27 := by rw [lam3]; norm_num
  rw [← h1, ← h2]
  exact annihilator _ (by norm_num)

/-! ## The characteristic polynomial (LEAN-3 WP-E)

The consequence layer above reaches the eigenvalue MULTISET only through a step that is not
formalized (real symmetric ⟹ orthogonally diagonalizable, so that the two trace identities
read as `∑ λᵢ` and `∑ λᵢ²`).  This section removes that step entirely by computing the
characteristic polynomial outright:

    charpoly (Cmat x) = X ^ 19 * ((X - C λ₅(x)) ^ 5 * (X - C λ₃(x)) ^ 3)      for EVERY x.

The route needs **no new certificate and no large matrix product**.  The `WP-A`
decomposition `C_x = (λ₅/12) W₅V₅ᵀ + (λ₃/16) V₃V₃ᵀ` is already a **rank-8 factorization**
`C_x = F_x G` through the eight-dimensional index type `Fin 5 ⊕ Fin 3`, with

    F_x = [ (λ₅/12) W₅ | (λ₃/16) V₃ ]   (27×8),      G = [ V₅ | V₃ ]ᵀ   (8×27),

and the *reversed* product is **diagonal**, by exactly the four small decidable certificates
`V₅ᵀW₅ = 12·1`, `V₃ᵀV₃ = 16·1`, `V₅ᵀV₃ = 0`, `V₃ᵀW₅ = 0` already proved above:

    G F_x = diag(λ₅·1₅, λ₃·1₃)   (8×8).

Mathlib's rectangular Weinstein–Aronszajn identity `Matrix.charpoly_mul_comm_of_le` then
gives `charpoly (F_x G) = X^(27−8) · charpoly (G F_x)`, and the 8×8 charpoly is the product
of the two scalar blocks.  The `19` is therefore *derived* (`27 − 8`), not assumed, and the
statement holds at the coincidence points `x ∈ {1/3, 1/2, 5/6}` as well, where the multiset
simply merges.
-/

/-- Entrywise `ℤ → ℝ` cast for matrices with arbitrary (possibly rectangular) index types.
(`toR` above is the square `Idx × Idx` special case and is kept as it is used throughout.) -/
noncomputable def mapR {m n : Type*} (M : Matrix m n ℤ) : Matrix m n ℝ :=
  M.map (Int.castRingHom ℝ)

@[simp] theorem mapR_apply {m n : Type*} (M : Matrix m n ℤ) (i : m) (j : n) :
    mapR M i j = ((M i j : ℤ) : ℝ) := rfl

theorem mapR_mul {l m n : Type*} [Fintype m] (A : Matrix l m ℤ) (B : Matrix m n ℤ) :
    mapR (A * B) = mapR A * mapR B := Matrix.map_mul

theorem mapR_transpose {m n : Type*} (A : Matrix m n ℤ) : mapR Aᵀ = (mapR A)ᵀ := by
  ext i j; simp [mapR]

theorem mapR_zsmul {m n : Type*} (c : ℤ) (A : Matrix m n ℤ) :
    mapR (c • A) = (c : ℝ) • mapR A := by
  ext i j; simp [mapR]

theorem mapR_one {n : Type*} [DecidableEq n] : mapR (1 : Matrix n n ℤ) = 1 := by
  ext i j; by_cases h : i = j <;> simp [mapR, Matrix.one_apply, h]

/-- `V₅` over `ℝ`. -/
noncomputable abbrev V5R : Matrix Idx (Fin 5) ℝ := mapR V5
/-- `W₅` over `ℝ`. -/
noncomputable abbrev W5R : Matrix Idx (Fin 5) ℝ := mapR W5
/-- `V₃` over `ℝ`. -/
noncomputable abbrev V3R : Matrix Idx (Fin 3) ℝ := mapR V3

/-! ### The four small certificates, transported to `ℝ` -/

theorem cert_V5R_W5R : V5Rᵀ * W5R = (12 : ℝ) • (1 : Matrix (Fin 5) (Fin 5) ℝ) := by
  rw [← mapR_transpose, ← mapR_mul, V5T_W5, mapR_zsmul, mapR_one]
  norm_num

theorem cert_V3R_V3R : V3Rᵀ * V3R = (16 : ℝ) • (1 : Matrix (Fin 3) (Fin 3) ℝ) := by
  rw [← mapR_transpose, ← mapR_mul, V3T_V3, mapR_zsmul, mapR_one]
  norm_num

theorem cert_V5R_V3R : V5Rᵀ * V3R = 0 := by
  rw [← mapR_transpose, ← mapR_mul, V5T_V3]
  ext i j; simp [mapR]

theorem cert_V3R_W5R : V3Rᵀ * W5R = 0 := by
  rw [← mapR_transpose, ← mapR_mul, V3T_W5]
  ext i j; simp [mapR]

theorem A5_eq : A5 = W5R * V5Rᵀ := by
  show mapR R5 = _
  rw [R5_factor, mapR_mul, mapR_transpose]

theorem A3_eq : A3 = V3R * V3Rᵀ := by
  show mapR R3 = _
  rw [R3_factor, mapR_mul, mapR_transpose]

/-! ### The rank-8 factorization -/

/-- The 27×8 left factor `F_x = [ (λ₅/12) W₅ | (λ₃/16) V₃ ]`. -/
noncomputable def Fmat (x : ℝ) : Matrix Idx (Fin 5 ⊕ Fin 3) ℝ := Matrix.of fun I j =>
  Sum.elim (fun k => (lam5 x / 12) * W5R I k) (fun k => (lam3 x / 16) * V3R I k) j

/-- The 8×27 right factor `G = [ V₅ | V₃ ]ᵀ` (independent of `x`). -/
noncomputable def Gmat : Matrix (Fin 5 ⊕ Fin 3) Idx ℝ := Matrix.of fun j I =>
  Sum.elim (fun k => V5R I k) (fun k => V3R I k) j

/-- `F_x G = C_x`: the WP-A decomposition, read as a rank-8 factorization. -/
theorem Fmat_mul_Gmat (x : ℝ) (hx : x ≠ 0) : Fmat x * Gmat = Cmat x := by
  rw [Cmat_eq x hx, A5_eq, A3_eq]
  ext I J
  simp only [Matrix.mul_apply, Fmat, Gmat, Matrix.of_apply, Fintype.sum_sum_type,
    Sum.elim_inl, Sum.elim_inr, Matrix.add_apply, Matrix.smul_apply, smul_eq_mul,
    Matrix.transpose_apply, Finset.mul_sum]
  congr 1 <;> exact Finset.sum_congr rfl fun k _ => by ring

/-- Helper: contract a column sum of the shape appearing in `G F_x`. -/
private theorem col_contract {n p : Type*}
    (A : Matrix Idx n ℝ) (B : Matrix Idx p ℝ) (c : ℝ) (M : Matrix n p ℝ)
    (hM : Aᵀ * B = M) (k : n) (k' : p) :
    ∑ I : Idx, A I k * (c * B I k') = c * M k k' := by
  rw [← hM, Matrix.mul_apply, Finset.mul_sum]
  exact Finset.sum_congr rfl fun I _ => by simp [Matrix.transpose_apply]; ring

/-- **The reversed product is diagonal**: `G F_x = diag(λ₅·1₅, λ₃·1₃)`, an 8×8 identity
that uses only the four small certificates.  This is the whole reason no 27×27 product is
needed anywhere in the charpoly proof. -/
theorem Gmat_mul_Fmat (x : ℝ) :
    Gmat * Fmat x
      = Matrix.fromBlocks (lam5 x • (1 : Matrix (Fin 5) (Fin 5) ℝ)) 0 0
          (lam3 x • (1 : Matrix (Fin 3) (Fin 3) ℝ)) := by
  ext j j'
  cases j with
  | inl k =>
    cases j' with
    | inl k' =>
      simp only [Matrix.mul_apply, Gmat, Fmat, Matrix.of_apply, Sum.elim_inl,
        Matrix.fromBlocks_apply₁₁]
      rw [col_contract V5R W5R (lam5 x / 12) _ cert_V5R_W5R k k']
      simp only [Matrix.smul_apply, smul_eq_mul]
      ring
    | inr k' =>
      simp only [Matrix.mul_apply, Gmat, Fmat, Matrix.of_apply, Sum.elim_inl, Sum.elim_inr,
        Matrix.fromBlocks_apply₁₂]
      rw [col_contract V5R V3R (lam3 x / 16) _ cert_V5R_V3R k k']
      simp
  | inr k =>
    cases j' with
    | inl k' =>
      simp only [Matrix.mul_apply, Gmat, Fmat, Matrix.of_apply, Sum.elim_inl, Sum.elim_inr,
        Matrix.fromBlocks_apply₂₁]
      rw [col_contract V3R W5R (lam5 x / 12) _ cert_V3R_W5R k k']
      simp
    | inr k' =>
      simp only [Matrix.mul_apply, Gmat, Fmat, Matrix.of_apply, Sum.elim_inr,
        Matrix.fromBlocks_apply₂₂]
      rw [col_contract V3R V3R (lam3 x / 16) _ cert_V3R_V3R k k']
      simp only [Matrix.smul_apply, smul_eq_mul]
      ring

/-- `charpoly (c·1ₙ) = (X − C c)ⁿ`. -/
private theorem charpoly_smul_one {n : ℕ} (c : ℝ) :
    (c • (1 : Matrix (Fin n) (Fin n) ℝ)).charpoly
      = (Polynomial.X - Polynomial.C c) ^ n := by
  have h : c • (1 : Matrix (Fin n) (Fin n) ℝ) = Matrix.diagonal (fun _ => c) := by
    ext i j; by_cases h : i = j <;> simp [h]
  rw [h, Matrix.charpoly_diagonal, Finset.prod_const, Finset.card_univ, Fintype.card_fin]

set_option maxRecDepth 400000 in
/-- **The characteristic polynomial, for every `x ≠ 0`.**  The `19` is `27 − 8`, produced by
the rectangular Weinstein–Aronszajn identity, not assumed.

(`maxRecDepth` is raised locally: rewriting inside `charpoly` forces the elaborator through
the `Fintype.card Idx = 27` reduction.) -/
theorem charpoly_Cmat_of_ne_zero (x : ℝ) (hx : x ≠ 0) :
    (Cmat x).charpoly
      = Polynomial.X ^ 19 * ((Polynomial.X - Polynomial.C (lam5 x)) ^ 5
          * (Polynomial.X - Polynomial.C (lam3 x)) ^ 3) := by
  have hcard : Fintype.card (Fin 5 ⊕ Fin 3) ≤ Fintype.card Idx := by simp
  have hGF : (Gmat * Fmat x).charpoly
      = (Polynomial.X - Polynomial.C (lam5 x)) ^ 5
        * (Polynomial.X - Polynomial.C (lam3 x)) ^ 3 := by
    rw [Gmat_mul_Fmat x, Matrix.charpoly_fromBlocks_zero₁₂, charpoly_smul_one,
      charpoly_smul_one]
  have hFG : (Fmat x * Gmat).charpoly = (Cmat x).charpoly := by rw [Fmat_mul_Gmat x hx]
  have h := Matrix.charpoly_mul_comm_of_le (Fmat x) Gmat hcard
  rw [hFG, hGF] at h
  rw [h]
  norm_num

/-- At `x = 0` every forced coefficient is a fraction with denominator `9x` or `3x`, so
Lean's division convention makes `C₀` the zero matrix. -/
theorem Cmat_zero : Cmat 0 = 0 := by
  ext I J
  simp [Cmat, cco]

theorem lam5_zero : lam5 0 = 0 := by simp [lam5]

theorem lam3_zero : lam3 0 = 0 := by simp [lam3]

set_option maxRecDepth 400000 in
/-- **`charpoly_Cmat` — the WP-E target, with NO side condition at all.**

    (Cmat x).charpoly = X ^ 19 * ((X − C λ₅ x) ^ 5 * (X − C λ₃ x) ^ 3)   for all real x.

*Honest reading of the `x = 0` case.*  For `x ≠ 0` this is the mathematical statement, valid
at the coincidence points too (there the multiset merges: at `x = 1/2` the identity reads
`X²⁴(X − C λ₃)³`, at `x = 1/3` it reads `X²²(X − C λ₅)⁵`, at `x = 5/6` the two factors join
into a single eighth power).  At `x = 0` both sides degenerate to `X²⁷` *because of Lean's
junk convention* `a / 0 = 0` — `Cmat 0 = 0` and `λ₅ 0 = λ₃ 0 = 0` — so that point carries no
mathematical content and is included only so that the statement needs no hypothesis; `x = 0`
is outside the physical parameter range `(0, 1)` anyway. -/
theorem charpoly_Cmat (x : ℝ) :
    (Cmat x).charpoly
      = Polynomial.X ^ 19 * ((Polynomial.X - Polynomial.C (lam5 x)) ^ 5
          * (Polynomial.X - Polynomial.C (lam3 x)) ^ 3) := by
  rcases eq_or_ne x 0 with rfl | hx
  · rw [Cmat_zero, lam5_zero, lam3_zero]
    have h0 : (0 : Matrix Idx Idx ℝ) = (0 : ℝ) • (1 : Matrix (Fin 27) (Fin 27) ℝ) := by simp
    rw [h0, charpoly_smul_one]
    simp
    ring
  · exact charpoly_Cmat_of_ne_zero x hx

/-- The three Appendix C sample points again, now at charpoly level: the eigenvalue column
of the paper's table is the multiset `{0¹⁹, λ₅⁵, λ₃³}` with the stated rational values. -/
theorem charpoly_sample_26_51 :
    (Cmat (26 / 51)).charpoly
      = Polynomial.X ^ 19 * ((Polynomial.X - Polynomial.C (50 / 663 : ℝ)) ^ 5
          * (Polynomial.X - Polynomial.C (200 / 221 : ℝ)) ^ 3) := by
  have h1 : lam5 (26 / 51 : ℝ) = 50 / 663 := by rw [lam5]; norm_num
  have h2 : lam3 (26 / 51 : ℝ) = 200 / 221 := by rw [lam3]; norm_num
  rw [← h1, ← h2]; exact charpoly_Cmat _

theorem charpoly_sample_4_7 :
    (Cmat (4 / 7)).charpoly
      = Polynomial.X ^ 19 * ((Polynomial.X - Polynomial.C (3 / 7 : ℝ)) ^ 5
          * (Polynomial.X - Polynomial.C (20 / 21 : ℝ)) ^ 3) := by
  have h1 : lam5 (4 / 7 : ℝ) = 3 / 7 := by rw [lam5]; norm_num
  have h2 : lam3 (4 / 7 : ℝ) = 20 / 21 := by rw [lam3]; norm_num
  rw [← h1, ← h2]; exact charpoly_Cmat _

theorem charpoly_sample_3_4 :
    (Cmat (3 / 4)).charpoly
      = Polynomial.X ^ 19 * ((Polynomial.X - Polynomial.C (2 / 3 : ℝ)) ^ 5
          * (Polynomial.X - Polynomial.C (20 / 27 : ℝ)) ^ 3) := by
  have h1 : lam5 (3 / 4 : ℝ) = 2 / 3 := by rw [lam5]; norm_num
  have h2 : lam3 (3 / 4 : ℝ) = 20 / 27 := by rw [lam3]; norm_num
  rw [← h1, ← h2]; exact charpoly_Cmat _

set_option maxRecDepth 400000 in
/-- **The physically decisive point.**  At `x = 1/2` (`λ₅ = 0`, `λ₃ = 8/9`) the
characteristic polynomial is `X²⁴(X − 8/9)³`, i.e. the eigenvalue multiset is
`{0²⁴, (8/9)³}`.

*Scope (R13 MAJOR-2, 2026-08-01).*  A characteristic polynomial does **not** by itself
determine the rank — `X²⁴(X − 8/9)³` is equally the charpoly of a matrix with a nontrivial
nilpotent part at `0`.  The paper's `rank C_{1/2} = 3` is proved separately and
unconditionally by `rank_Cmat_half` below, from the rank factorization `A₃ = V₃V₃ᵀ` with
`V₃ᵀV₃ = 16·1₃`; it is **not** an inference from this theorem. -/
theorem charpoly_half :
    (Cmat (1 / 2)).charpoly
      = Polynomial.X ^ 24 * (Polynomial.X - Polynomial.C (8 / 9 : ℝ)) ^ 3 := by
  have h1 : lam5 (1 / 2 : ℝ) = 0 := by rw [lam5]; norm_num
  have h2 : lam3 (1 / 2 : ℝ) = 8 / 9 := by rw [lam3]; norm_num
  rw [charpoly_Cmat, h1, h2]
  simp
  ring

/-! ### The rank at `x = 1/2` (LEAN-3.2, R13 MAJOR-2)

`charpoly_half` gives the eigenvalue multiset, not the rank.  The rank statement of paper
Theorem 3.3(2) is proved here directly, from the integer rank factorization already in this
file: at `x = 1/2` we have `λ₅ = 0`, so `Cmat_eq` collapses to `C = (λ₃/16)·A₃` with
`A₃ = V₃V₃ᵀ` (`A3_eq`), and the small certificate `V₃ᵀV₃ = 16·1₃` (`cert_V3R_V3R`) sandwiches
`C` between two rank-3 objects. -/

/-- At `x = 1/2` the defect Choi matrix is the rank factorization `((1/18)·V₃)·V₃ᵀ`
(`λ₅(1/2) = 0`, `λ₃(1/2)/16 = 1/18`). -/
theorem Cmat_half_factor :
    Cmat (1 / 2 : ℝ) = ((1 / 18 : ℝ) • V3R) * V3Rᵀ := by
  have h1 : lam5 (1 / 2 : ℝ) = 0 := by rw [lam5]; norm_num
  have h2 : lam3 (1 / 2 : ℝ) = 8 / 9 := by rw [lam3]; norm_num
  rw [Cmat_eq (1 / 2 : ℝ) (by norm_num), h1, h2, A3_eq, Matrix.smul_mul]
  norm_num

/-- A nonzero scalar multiple of `1₃` is a unit. -/
private theorem isUnit_smul_one_three {c : ℝ} (hc : c ≠ 0) :
    IsUnit (c • (1 : Matrix (Fin 3) (Fin 3) ℝ)) := by
  rw [Matrix.isUnit_iff_isUnit_det, Matrix.det_smul, Matrix.det_one, mul_one]
  exact isUnit_iff_ne_zero.2 (pow_ne_zero _ hc)

/-- The sandwich `V₃ᵀ C_{1/2} V₃ = (128/9)·1₃`, an invertible 3×3 matrix. -/
theorem V3R_Cmat_half_V3R :
    V3Rᵀ * Cmat (1 / 2 : ℝ) * V3R = (128 / 9 : ℝ) • (1 : Matrix (Fin 3) (Fin 3) ℝ) := by
  have hVU : V3Rᵀ * ((1 / 18 : ℝ) • V3R)
      = (16 / 18 : ℝ) • (1 : Matrix (Fin 3) (Fin 3) ℝ) := by
    rw [Matrix.mul_smul, cert_V3R_V3R, smul_smul]; norm_num
  have hassoc : V3Rᵀ * (((1 / 18 : ℝ) • V3R) * V3Rᵀ) * V3R
      = (V3Rᵀ * ((1 / 18 : ℝ) • V3R)) * (V3Rᵀ * V3R) := by
    simp only [Matrix.mul_assoc]
  rw [Cmat_half_factor, hassoc, hVU, cert_V3R_V3R, Matrix.smul_mul, Matrix.mul_smul,
    Matrix.one_mul, smul_smul]
  norm_num

/-- **Paper Theorem 3.3(2) at the physically decisive point: `rank C_{1/2} = 3`.**

Upper bound: `C_{1/2} = ((1/18)V₃)·V₃ᵀ` factors through `ℝ³`.
Lower bound: `V₃ᵀ C_{1/2} V₃ = (128/9)·1₃` is invertible, and rank cannot increase under
multiplication on either side.

This is the statement `charpoly_half` does **not** give (R13 MAJOR-2).

Scope note (R14 m5): this machine-checks the rank conjunct of paper Thm 3.3(2) AT
x = 1/2 only; the companion conjunct rank C_x = 8 on (1/2,1) is NOT formalized
(R14 verified it exactly at 4/7, 26/51, 49/100). -/
theorem rank_Cmat_half : (Cmat (1 / 2 : ℝ)).rank = 3 := by
  have hupper : (Cmat (1 / 2 : ℝ)).rank ≤ 3 := by
    rw [Cmat_half_factor]
    calc (((1 / 18 : ℝ) • V3R) * V3Rᵀ).rank
        ≤ ((1 / 18 : ℝ) • V3R).rank := Matrix.rank_mul_le_left _ _
      _ ≤ Fintype.card (Fin 3) := Matrix.rank_le_card_width _
      _ = 3 := by simp
  have hunit : ((128 / 9 : ℝ) • (1 : Matrix (Fin 3) (Fin 3) ℝ)).rank = 3 := by
    rw [Matrix.rank_of_isUnit _ (isUnit_smul_one_three (by norm_num))]
    simp
  have hlower : 3 ≤ (Cmat (1 / 2 : ℝ)).rank := by
    rw [← hunit, ← V3R_Cmat_half_V3R]
    calc (V3Rᵀ * Cmat (1 / 2 : ℝ) * V3R).rank
        ≤ (V3Rᵀ * Cmat (1 / 2 : ℝ)).rank := Matrix.rank_mul_le_left _ _
      _ ≤ (Cmat (1 / 2 : ℝ)).rank := Matrix.rank_mul_le_right _ _
  omega

end WHGAP.DefectChoi

