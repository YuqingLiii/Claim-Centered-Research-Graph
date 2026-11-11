import WHGAP.Support.DefectChoi
import WHGAP.Support.IcScalar
import Mathlib.LinearAlgebra.Matrix.Hermitian

/-!
# WHGAP channel layer — Kraus set, complement, forced-point lift, defect (LEAN-3 WP-D;
# §8 the §6 witness spectra over ℂ, LEAN-4 WP-G)

**Serves** `WHGAP.«signed-lift-extension»` (P2) through `WHGAP.Support.DefectChoi`,
and `WHGAP.«private-boundary»` (P14's §7
ensemble).  Commissioned by
`channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_LEAN3_20260801.md`, work
package D.  No node Claim lives in this file.

## Why this module exists

Until 2026-08-01 there was **no channel** anywhere in this development: `Cmat`,
`BOut`/`EOut`, `outB`/`outE` were *definitions*, and the statement that they are the
objects the paper says they are ("the defect Choi matrix", "the channel outputs") was
carried entirely by exact sympy — the three
"definitional-identification residuals" (a), (b), (c) of `WHGAP/Trust.lean`.  This module
builds the channel as explicit finite linear algebra and closes them.

## What is defined

* `A μ` — the three Levi-Civita matrices `(A_μ)_{jk} = ε_{μjk}`;
* `K s t` — the Kraus set `K₀ = t·1`, `K_{μ+1} = s·A_μ` (`K_zero_eq`, `K_succ_eq`);
* `LamK s t X = Σ_a K_a X K_aᵀ`, and `Lam x X = (1−x)X + (x/2)(Tr X·1 − Xᵀ)`;
* `LamCK s t X` — the padded `4×4` complement `(Λ^c(X))_{ab} = Tr(K_a X K_bᵀ)`, and its
  block closed form `LamC x β X` (paper `eq:comp`, `β = s t`);
* `Jlift x q`, `Jdag x q` — the forced-point lift of paper `eq:Jintro` (`p = 1/3`,
  `d = 2(1−x)/3`) in the `q`-chart, and its Hilbert–Schmidt adjoint;
* `Defect x q τ Y = Λ(τ)·Y − J†(Λ^c(τ)·J(Y))` — the residual-family defect superoperator;
* `word k`, `defectClosed` — the fifteen bilinear words of `eq:master` and the closed form;
* `Emat`, `legA/legB/legC`, `choiOf` — the Choi matrix on the `Fin 27` packing of
  `WHGAP.Support.DefectChoi` (`(i,b,b') ↦ 9i + 3b + b'`).

## The chart (commission note: `q·β` rationalizes)

The lift's off-diagonal weight is `q = (1/3)√(2(1−x)/x) = t/(3s)`, so that

    β = s t = (3x/2)·q      and      9 x q² = 2(1−x)      and      q β = (1−x)/3 .

Hence **the whole construction is rational in the single parameter `q`** (`chart_beta`,
`chart_q`), and `9xq² = 2(1−x)` is equivalent to `x = 2/(9q²+2)` — which is how
`defect_eq` discharges every square root: it substitutes `x` away entirely, after which
each of the nine entry identities is a plain rational-function identity in `q` and the
eighteen entries of `τ, Y`, closed by `field_simp; ring` with **no** side relation left.

## What is proved

* `LamK_eq` — the Kraus sum equals the closed form (with `hs : s² = x/2`, `ht : t² = 1−x`);
* `LamK_tp` — `Σ_a K_aᵀ K_a = 1` (trace preservation);
* `LamCK_eq` — the `Tr(K_a X K_bᵀ)` complement equals the `eq:comp` block form;
* `Jdag_adjoint` — `⟪Z, J(Y)⟫ = ⟪J†(Z), Y⟫` (so `Jdag` really is the HS adjoint);
* `defect_eq` — the defect superoperator equals `Σ_k c_k(x)·W_k(τ,Y)`;
* `word_choi_*` — the fifteen words evaluate on `(E_ij, E_rs)` to the fifteen `pat` deltas;
* **`choi_defect_eq_Cmat`** — the Choi matrix of `Defect` **is** `DefectChoi.Cmat x`,
  all 729 entries, for every `x` and `q` with `9xq² = 2(1−x)`.  This is exactly the bridge
  that residual (a) of `Trust.lean` named as *not* checked in Lean;
* (§8, LEAN-4 WP-G) `Pwit_eq_outer`/`PwitBar_eq_outer` — the §6 projectors are the outer
  products of `ψ = (e₁ + i e₂)/√2` and `ψ̄`; `LamWit_eq`/`LamCWit_eq` — the two COMPLEX
  outputs `Λ_x(ρ_ε)` and `Λ^c_x(ρ_ε)` written out; and **`specB_charpoly`**,
  **`specE_charpoly`** — their characteristic polynomials, matching the two eigenvalue
  lists of `WHGAP.Support.IcScalar` (`specB_charpoly_list`, `specE_charpoly_list`), with
  the Kraus-level corollaries `specB_charpoly_kraus`, `specE_charpoly_kraus`.

## Honesty note (§7.9 scope) — what this does NOT do

1. `Λ_x` here is a **linear map on 3×3 matrices given by a Kraus sum**; complete
   positivity, the Stinespring dilation, the fact that `LamCK` is *the* complementary
   channel (rather than the matrix of Kraus overlaps that computes it), and every
   capacity are still absent.  There is still no coding theorem anywhere.
2. The **signed lift** `J` is checked here only as the linear map of `eq:Jintro`; that
   the residual family is `(Λ(τ)·, J†∘Λ^c(τ)·∘J)` and that PSD-ness of its defect Choi
   certifies `Q = P = 0` is the Zhu–Wang interface, unchanged.
3. `defect_eq`/`choi_defect_eq_Cmat` are identities for the **forced point** `p = 1/3`,
   `d = 2(1−x)/3` only; the forcing itself is `«signed-lift-extension».forcing_p/forcing_d`.
4. **The §6 eigen-data glue is now closed AT CHARPOLY LEVEL ONLY** (LEAN-4 WP-G,
   2026-08-01; §8 below).  *History, kept append-only: WP-D's item 3 did not land, and
   R13 MAJOR-1 struck a text here that had claimed it did and named two declarations —
   `specB_charpoly`, `specE_charpoly` — that did not then exist.  They exist now, and
   this item states exactly what they do and do not give.*

   **What is proved.**  Over `ℂ`, for the genuinely complex witness state
   `ρ_ε = (1−ε)P_ψ + εP_ψ̄` with `ψ = (e₁ + i e₂)/√2`:
   `charpoly Λ_x(ρ_ε) = (X − (1−ε)(1−x/2))(X − ε(1−x/2))(X − x/2)` (`specB_charpoly`) and
   `charpoly Λ^c_x(ρ_ε) = (X² − (1−x/2)X + 2x(1−x)ε(1−ε))(X − x(1−ε)/2)(X − xε/2)`
   (`specE_charpoly`, under `hβ : β² = x(1−x)/2`), together with the two statements in
   `IcScalar`-list form (`specB_charpoly_list`, `specE_charpoly_list`) and the Kraus-level
   corollaries.  The E-side statement is deliberately at the level of the **quadratic
   factor**: `λ±` involve `√discE`, and the charpoly-level statement needs no square root
   at all — which is exactly why this level was chosen.  `specE_charpoly_list`, which does
   name `lamP`/`lamM`, therefore carries the extra hypotheses `0 ≤ x ≤ 1`.

   **What is still missing — residual (b) of `WHGAP/Trust.lean` is REDUCED, not removed.**
   The remaining glue is named here explicitly: **"same characteristic polynomial ⟹ same
   von Neumann entropy" is NOT available for complex Hermitian matrices in this
   development.**  `WHGAP.Support.Entropy` builds `vnEntropy` (and
   `vnEntropy_congr_charpoly`, `vnEntropy_eq_sum_of_charpoly`) for **real symmetric**
   matrices over `ℝ` only; the §6 outputs proved Hermitian here
   (`LamWit_isHermitian`, `LamCWit_isHermitian`) are complex, and the real-symmetric
   layer does **not** apply to them verbatim — Mathlib's `IsHermitian.eigenvalues` and the
   `roots_charpoly` bridge would have to be re-run over `RCLike`/`ℂ`.  Until that layer
   exists, the passage from these two charpolys to `IcScalar x ε = S(Λ(ρ_ε)) − S(Λ^c(ρ_ε))`
   — and hence the reading of `IcScalar` as a coherent information — is not in Lean.  That
   passage, plus the achievability reading `hach`, is what residual (b) still carries.

   **AMENDMENT 2026-08-01 (LEAN-5 WP-H; applied per R15 MAJOR-1).  The paragraph
   immediately above is SUPERSEDED and is kept, unedited, as history** (same append-only
   discipline as the R13 history note in this item).  Three of its assertions are no longer
   true of this tree:

   1. *"residual (b) … is REDUCED, not removed"* — `WHGAP/Trust.lean`'s dated section
      "2026-08-01 (LEAN-5 WP-H) — residual (b): **DISCHARGED**" now records it as
      discharged, with explicit over-claim and under-claim guards.
   2. *"'same characteristic polynomial ⟹ same von Neumann entropy' is NOT available for
      complex Hermitian matrices in this development"* — it is available: it is
      `WHGAP.Support.vnEntropyC_congr_charpoly` in the new module
      `WHGAP/Support/EntropyC.lean`, which supplies the whole complex layer (`vnEntropyC`,
      the `ofReal`-injectivity eigenvalue-multiset bridge, and the Fin-indexed and list
      workhorses).
   3. *"Until that layer exists, the passage … is not in Lean"* — that passage is
      `WHGAP.Support.IcScalar_eq_vnEntropyC_diff` (same module):
      `IcScalar x ε = vnEntropyC (Λ_x(ρ_ε)) − vnEntropyC (Λ^c_x(ρ_ε))` for `0 ≤ x ≤ 1` and
      any `β` with `β² = x(1−x)/2`.  Its two load-bearing inputs are exactly the list-form
      charpolys proved in §8 of THIS file (`specB_charpoly_list`, `specE_charpoly_list`),
      so the identification is about `Lam`/`LamC` — and, through
      `specB_charpoly_kraus`/`specE_charpoly_kraus`, about the Kraus-built `LamK`/`LamCK`.

   **What still qualifies the reading of `IcScalar` as a coherent information is NOT
   residual (b).**  It is the two interface-tier items already listed in item 1 above:
   (i) that `LamCK` is *the* complementary channel of `Lam` (a Stinespring/dilation
   statement — this module has a Kraus sum and a matrix of Kraus overlaps, no complete
   positivity, no dilation theory, no channel object), and (ii) LSD/Devetak achievability.
   Both are cited interfaces in `WHGAP/Interface.lean` (`q_pos_of_ic_pos`, `lsd_devetak`)
   and neither is touched by LEAN-5.  Evidence tier of the LEAN-5 build: NUMERICAL
   (a green build is a run, DAG §2).

Pre-verification (all statements below were checked in exact sympy BEFORE any Lean was
written): `tools/whgap_lean3_wpd_check.py`, gates D0–D9e, log
`artifacts/logs_whgap_lean3_20260801/wpd_sympy_gates.txt`; for §8,
`tools/whgap_lean4_wpg_check.py`, gates G0–G13, log
`artifacts/logs_whgap_lean4_20260801/wpg_sympy_gates.txt`.
-/

set_option maxHeartbeats 4000000
set_option maxRecDepth 40000

namespace WHGAP.Support.Channel

open Matrix

/-! ## 1. The Kraus set (paper `eq:kraus`) -/

/-- The three Levi-Civita matrices `(A_μ)_{jk} = ε_{μjk}`. -/
def A {R : Type*} [Ring R] : Fin 3 → Matrix (Fin 3) (Fin 3) R
  | 0 => !![0, 0, 0; 0, 0, 1; 0, -1, 0]
  | 1 => !![0, 0, -1; 0, 0, 0; 1, 0, 0]
  | 2 => !![0, 1, 0; -1, 0, 0; 0, 0, 0]

/-- The Kraus set of `Λ_x`: `K₀ = t·1`, `K_{μ+1} = s·A_μ`, with `s² = x/2`, `t² = 1−x`. -/
def K {R : Type*} [Ring R] (s t : R) : Fin 4 → Matrix (Fin 3) (Fin 3) R
  | 0 => !![t, 0, 0; 0, t, 0; 0, 0, t]
  | 1 => !![0, 0, 0; 0, 0, s; 0, -s, 0]
  | 2 => !![0, 0, -s; 0, 0, 0; s, 0, 0]
  | 3 => !![0, s, 0; -s, 0, 0; 0, 0, 0]

variable {R : Type*} [Field R] [CharZero R]

omit [CharZero R] in
theorem K_zero_eq (s t : R) : K s t 0 = t • (1 : Matrix (Fin 3) (Fin 3) R) := by
  ext i j
  simp only [Matrix.smul_apply, Matrix.one_apply, smul_eq_mul]
  fin_cases i <;> fin_cases j <;> simp [K, Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons, Matrix.head_fin_const]

omit [CharZero R] in
theorem K_succ_eq (s t : R) (μ : Fin 3) : K s t μ.succ = s • (A μ : Matrix (Fin 3) (Fin 3) R) := by
  fin_cases μ <;> ext i j <;>
    (simp only [Matrix.smul_apply, smul_eq_mul]; fin_cases i <;> fin_cases j <;> simp [K, A, Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons, Matrix.head_fin_const])

/-- The Kraus sum `Σ_a K_a X K_aᵀ`. -/
def LamK (s t : R) (X : Matrix (Fin 3) (Fin 3) R) : Matrix (Fin 3) (Fin 3) R :=
  ∑ a : Fin 4, K s t a * X * (K s t a)ᵀ

/-- The closed form `Λ_x(X) = (1−x)X + (x/2)(Tr X·1 − Xᵀ)` (the paper's channel). -/
def Lam (x : R) (X : Matrix (Fin 3) (Fin 3) R) : Matrix (Fin 3) (Fin 3) R :=
  (1 - x) • X + (x / 2) • (X.trace • (1 : Matrix (Fin 3) (Fin 3) R) - Xᵀ)

omit [CharZero R] in
/-- The Kraus sum in terms of `s²`, `t²` alone — no hypothesis, pure `ring`. -/
theorem LamK_st (s t : R) (X : Matrix (Fin 3) (Fin 3) R) :
    LamK s t X = t ^ 2 • X + s ^ 2 • (X.trace • (1 : Matrix (Fin 3) (Fin 3) R) - Xᵀ) := by
  ext i j
  simp only [LamK, Matrix.sum_apply, Fin.sum_univ_four, Matrix.mul_apply, Matrix.transpose_apply,
    Fin.sum_univ_three, Matrix.add_apply, Matrix.smul_apply, Matrix.sub_apply, Matrix.one_apply,
    Matrix.trace, Matrix.diag, smul_eq_mul]
  fin_cases i <;> fin_cases j <;> simp [K, Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons, Matrix.head_fin_const] <;> ring

omit [CharZero R] in
/-- **The Kraus set represents the channel.** -/
theorem LamK_eq {s t x : R} (hs : s ^ 2 = x / 2) (ht : t ^ 2 = 1 - x)
    (X : Matrix (Fin 3) (Fin 3) R) : LamK s t X = Lam x X := by
  rw [LamK_st, hs, ht, Lam]

/-- Trace preservation: `Σ_a K_aᵀ K_a = 1`. -/
theorem LamK_tp {s t x : R} (hs : s ^ 2 = x / 2) (ht : t ^ 2 = 1 - x) :
    ∑ a : Fin 4, (K s t a)ᵀ * K s t a = (1 : Matrix (Fin 3) (Fin 3) R) := by
  have h : s ^ 2 + s ^ 2 + t ^ 2 = 1 := by rw [hs, ht]; ring
  ext i j
  simp only [Matrix.sum_apply, Fin.sum_univ_four, Matrix.mul_apply, Matrix.transpose_apply,
    Fin.sum_univ_three, Matrix.one_apply]
  fin_cases i <;> fin_cases j <;> simp [K, Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons, Matrix.head_fin_const] <;> linear_combination h

/-! ## 2. The padded complement (paper `eq:comp`) -/

/-- The antisymmetric part vector `a(X)_μ = Σ_{jk} ε_{μjk} X_{jk}`. -/
def aVec (X : Matrix (Fin 3) (Fin 3) R) : Fin 3 → R
  | 0 => X 1 2 - X 2 1
  | 1 => X 2 0 - X 0 2
  | 2 => X 0 1 - X 1 0

/-- The complement as the matrix of Kraus overlaps: `(Λ^c(X))_{ab} = Tr(K_a X K_bᵀ)`. -/
def LamCK (s t : R) (X : Matrix (Fin 3) (Fin 3) R) : Matrix (Fin 4) (Fin 4) R :=
  Matrix.of fun a b => (K s t a * X * (K s t b)ᵀ).trace

/-- The block closed form of `eq:comp` with general coefficients `a = t²`, `c = s²`,
`β = s t`. -/
def LamCgen (a c β : R) (X : Matrix (Fin 3) (Fin 3) R) : Matrix (Fin 4) (Fin 4) R :=
  !![a * X.trace,      β * aVec X 0,                β * aVec X 1,                β * aVec X 2;
     -(β * aVec X 0),  c * (X.trace - X 0 0),       c * (-X 1 0),                c * (-X 2 0);
     -(β * aVec X 1),  c * (-X 0 1),                c * (X.trace - X 1 1),       c * (-X 2 1);
     -(β * aVec X 2),  c * (-X 0 2),                c * (-X 1 2),                c * (X.trace - X 2 2)]

/-- The complement of `Λ_x` in the paper's frame: `β = √(x(1−x)/2)` enters as a parameter. -/
def LamC (x β : R) (X : Matrix (Fin 3) (Fin 3) R) : Matrix (Fin 4) (Fin 4) R :=
  LamCgen (1 - x) (x / 2) β X

omit [CharZero R] in
theorem LamCK_st (s t : R) (X : Matrix (Fin 3) (Fin 3) R) :
    LamCK s t X = LamCgen (t ^ 2) (s ^ 2) (s * t) X := by
  ext i j
  simp only [LamCK, Matrix.of_apply, Matrix.trace, Matrix.diag, Fin.sum_univ_three,
    Matrix.mul_apply, Matrix.transpose_apply]
  fin_cases i <;> fin_cases j <;>
    simp [K, LamCgen, aVec, Matrix.trace, Matrix.diag, Fin.sum_univ_three, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons, Matrix.head_fin_const] <;> ring

omit [CharZero R] in
/-- **The Kraus overlaps give the `eq:comp` complement.** -/
theorem LamCK_eq {s t x : R} (hs : s ^ 2 = x / 2) (ht : t ^ 2 = 1 - x)
    (X : Matrix (Fin 3) (Fin 3) R) : LamCK s t X = LamC x (s * t) X := by
  rw [LamCK_st, hs, ht, LamC]

/-! ## 3. The forced-point lift (paper `eq:Jintro` at `p = 1/3`, `d = 2(1−x)/3`) -/

/-- The lift `J` of `eq:Jintro` at the forced point, in the `q`-chart:
`p = 1/3`, `c₁ = 2(1−x)/(3x)`, `c₂ = 1 − 4(1−x)/(3x)`, `c₃ = −2(1−x)/(3x)`. -/
noncomputable def Jlift (x q : ℝ) (Y : Matrix (Fin 3) (Fin 3) ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  let c1 : ℝ := 2 * (1 - x) / (3 * x)
  let c2 : ℝ := 1 - 4 * (1 - x) / (3 * x)
  let c3 : ℝ := -(2 * (1 - x) / (3 * x))
  !![Y.trace / 3,       q * aVec Y 0,  q * aVec Y 1,  q * aVec Y 2;
     -(q * aVec Y 0),   c1 * Y.trace + c2 * Y 0 0 + c3 * Y 0 0,
                        c2 * Y 0 1 + c3 * Y 1 0,
                        c2 * Y 0 2 + c3 * Y 2 0;
     -(q * aVec Y 1),   c2 * Y 1 0 + c3 * Y 0 1,
                        c1 * Y.trace + c2 * Y 1 1 + c3 * Y 1 1,
                        c2 * Y 1 2 + c3 * Y 2 1;
     -(q * aVec Y 2),   c2 * Y 2 0 + c3 * Y 0 2,
                        c2 * Y 2 1 + c3 * Y 1 2,
                        c1 * Y.trace + c2 * Y 2 2 + c3 * Y 2 2]

/-- The index shift `Fin 3 → Fin 4`, `μ ↦ μ+1`, of the padded environment frame. -/
def sh : Fin 3 → Fin 4
  | 0 => 1
  | 1 => 2
  | 2 => 3

/-- The Hilbert–Schmidt adjoint of `Jlift`, written out. -/
noncomputable def Jdag (x q : ℝ) (Z : Matrix (Fin 4) (Fin 4) ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  let c1 : ℝ := 2 * (1 - x) / (3 * x)
  let c2 : ℝ := 1 - 4 * (1 - x) / (3 * x)
  let c3 : ℝ := -(2 * (1 - x) / (3 * x))
  let d : ℝ := Z 0 0 / 3 + c1 * (Z 1 1 + Z 2 2 + Z 3 3)
  Matrix.of fun j k =>
    (if j = k then d else 0) + c2 * Z (sh j) (sh k) + c3 * Z (sh k) (sh j)
      + q * ∑ i : Fin 3, (A i : Matrix (Fin 3) (Fin 3) ℝ) j k * (Z 0 (sh i) - Z (sh i) 0)

/-- `Jdag` really is the HS adjoint of `Jlift`. -/
theorem Jdag_adjoint (x q : ℝ) (Y : Matrix (Fin 3) (Fin 3) ℝ) (Z : Matrix (Fin 4) (Fin 4) ℝ) :
    (∑ a : Fin 4, ∑ b : Fin 4, Z a b * Jlift x q Y a b)
      = ∑ j : Fin 3, ∑ k : Fin 3, Jdag x q Z j k * Y j k := by
  simp [Jlift, Jdag, sh, A, aVec, Fin.sum_univ_four, Fin.sum_univ_three, Matrix.trace,
    Matrix.diag, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]
  ring

/-! ## 4. The chart: `β` and `q` are one parameter -/

/-- `β = s t = (3x/2) q` when `q = t/(3s)`. -/
theorem chart_beta {s t q x : ℝ} (hs : s ^ 2 = x / 2) (hq : 3 * s * q = t) :
    s * t = 3 * x * q / 2 := by
  have : x = 2 * s ^ 2 := by rw [hs]; ring
  subst this; linear_combination (-s) * hq

/-- `9 x q² = 2(1−x)` when `q = t/(3s)`, `s² = x/2`, `t² = 1−x`. -/
theorem chart_q {s t q x : ℝ} (hs : s ^ 2 = x / 2) (ht : t ^ 2 = 1 - x) (hq : 3 * s * q = t) :
    9 * x * q ^ 2 = 2 * (1 - x) := by
  linear_combination (-18 * q ^ 2) * hs + 2 * ht + (2 * (3 * s * q + t)) * hq

/-- `q β = (1−x)/3` — the rationalizing product named in the commission. -/
theorem chart_q_beta {q x : ℝ} (hq : 9 * x * q ^ 2 = 2 * (1 - x)) :
    q * (3 * x * q / 2) = (1 - x) / 3 := by linear_combination hq / 6

/-- The chart is inhabited on the physical range `0 < x < 1`. -/
theorem exists_chart {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    ∃ s t q : ℝ, s ≠ 0 ∧ s ^ 2 = x / 2 ∧ t ^ 2 = 1 - x ∧ 3 * s * q = t := by
  refine ⟨Real.sqrt (x / 2), Real.sqrt (1 - x), Real.sqrt (1 - x) / (3 * Real.sqrt (x / 2)),
    ?_, ?_, ?_, ?_⟩
  · exact ne_of_gt (Real.sqrt_pos.mpr (by linarith))
  · exact Real.sq_sqrt (by linarith)
  · exact Real.sq_sqrt (by linarith)
  · have h : Real.sqrt (x / 2) ≠ 0 := ne_of_gt (Real.sqrt_pos.mpr (by linarith))
    field_simp

/-! ## 5. The defect superoperator and its closed form -/

/-- `Δ_J(τ)(Y) = Λ(τ)·Y − J†(Λ^c(τ)·J(Y))`, at the forced point, in the `q`-chart
(`β = 3xq/2` by `chart_beta`). -/
noncomputable def Defect (x q : ℝ) (τ Y : Matrix (Fin 3) (Fin 3) ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  Lam x τ * Y - Jdag x q (LamC x (3 * x * q / 2) τ * Jlift x q Y)

/-- The fifteen bilinear words of `eq:master`, in the `pat` table's own order. -/
def word (k : ℕ) (τ Y : Matrix (Fin 3) (Fin 3) ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  match k with
  | 1 => Y.trace • τ
  | 2 => τ * Yᵀ
  | 3 => τ * Y
  | 4 => Y.trace • τᵀ
  | 5 => Y * τᵀ
  | 6 => Yᵀ * τᵀ
  | 7 => (τ.trace * Y.trace) • (1 : Matrix (Fin 3) (Fin 3) ℝ)
  | 8 => τ.trace • Y
  | 9 => τ.trace • Yᵀ
  | 10 => (τ * Yᵀ).trace • (1 : Matrix (Fin 3) (Fin 3) ℝ)
  | 11 => τᵀ * Y
  | 12 => Yᵀ * τ
  | 13 => (τ * Y).trace • (1 : Matrix (Fin 3) (Fin 3) ℝ)
  | 14 => τᵀ * Yᵀ
  | 15 => Y * τ
  | _ => 0

/-- The closed form `Σ_k c_k(x) W_k(τ,Y)`, with `c_k` the Appendix A forced column
(`WHGAP.DefectChoi.cco`). -/
noncomputable def defectClosed (x : ℝ) (τ Y : Matrix (Fin 3) (Fin 3) ℝ) :
    Matrix (Fin 3) (Fin 3) ℝ :=
  DefectChoi.cco x 1 • word 1 τ Y + DefectChoi.cco x 2 • word 2 τ Y
  + DefectChoi.cco x 3 • word 3 τ Y + DefectChoi.cco x 4 • word 4 τ Y
  + DefectChoi.cco x 5 • word 5 τ Y + DefectChoi.cco x 6 • word 6 τ Y
  + DefectChoi.cco x 7 • word 7 τ Y + DefectChoi.cco x 8 • word 8 τ Y
  + DefectChoi.cco x 9 • word 9 τ Y + DefectChoi.cco x 10 • word 10 τ Y
  + DefectChoi.cco x 11 • word 11 τ Y + DefectChoi.cco x 12 • word 12 τ Y
  + DefectChoi.cco x 13 • word 13 τ Y + DefectChoi.cco x 14 • word 14 τ Y
  + DefectChoi.cco x 15 • word 15 τ Y

/-- **The defect superoperator equals the `eq:master` closed form.**  Nine entry
identities; the substitution `x = 2/(9q²+2)` (equivalent to `9xq² = 2(1−x)`) removes every
square root, after which each entry is a rational-function identity in `q` alone. -/
theorem defect_eq {x q : ℝ} (hq : 9 * x * q ^ 2 = 2 * (1 - x))
    (τ Y : Matrix (Fin 3) (Fin 3) ℝ) : Defect x q τ Y = defectClosed x τ Y := by
  have hd : (9 * q ^ 2 + 2 : ℝ) ≠ 0 := by positivity
  have hx : x = 2 / (9 * q ^ 2 + 2) := by
    field_simp
    linear_combination hq
  subst hx
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [Defect, defectClosed, Lam, LamC, LamCgen, Jlift, Jdag, sh, word, aVec, A,
      DefectChoi.cco, Matrix.mul_apply, Matrix.trace, Matrix.diag, Matrix.one_apply,
      Fin.sum_univ_three, Fin.sum_univ_four, Matrix.cons_val_two, Matrix.cons_val_three,
      Matrix.head_cons, Matrix.tail_cons] <;>
    field_simp <;> ring

/-! ## 6. The Choi matrix on the `Fin 27` packing -/

/-- The matrix unit `E_{ij}`. -/
def Emat (i j : Fin 3) : Matrix (Fin 3) (Fin 3) ℝ :=
  Matrix.of fun a b => (if i = a then (1 : ℝ) else 0) * (if j = b then 1 else 0)

/-- First leg of the packed index `(i,b,b') ↦ 9i + 3b + b'`, as a `Fin 3`. -/
def legA (I : Fin 27) : Fin 3 := ⟨I.val / 9, by have := I.isLt; omega⟩
/-- Second leg. -/
def legB (I : Fin 27) : Fin 3 := ⟨I.val / 3 % 3, by have := I.isLt; omega⟩
/-- Third leg. -/
def legC (I : Fin 27) : Fin 3 := ⟨I.val % 3, by have := I.isLt; omega⟩

theorem legA_val (I : Fin 27) : (legA I).val = DefectChoi.leg1 I := rfl
theorem legB_val (I : Fin 27) : (legB I).val = DefectChoi.leg2 I := rfl
theorem legC_val (I : Fin 27) : (legC I).val = DefectChoi.leg3 I := rfl

theorem dl_cast (a b : Fin 3) :
    ((DefectChoi.dl a.val b.val : ℤ) : ℝ) = if a = b then 1 else 0 := by
  by_cases h : a = b
  · subst h; simp [DefectChoi.dl]
  · have : a.val ≠ b.val := fun hv => h (Fin.ext hv)
    simp [DefectChoi.dl, this, h]

/-- The Choi matrix of a bilinear map, on the `DefectChoi` index packing:
`C[(i,b,b'),(j,r,s)] = [F(E_ij)(E_rs)]_{b,b'}`. -/
noncomputable def choiOf
    (F : Matrix (Fin 3) (Fin 3) ℝ → Matrix (Fin 3) (Fin 3) ℝ → Matrix (Fin 3) (Fin 3) ℝ) :
    Matrix (Fin 27) (Fin 27) ℝ :=
  Matrix.of fun I J => F (Emat (legA I) (legA J)) (Emat (legB J) (legC J)) (legB I) (legC I)

section WordChoi

variable (I J : Fin 27)

private theorem emat_apply (i j a b : Fin 3) :
    Emat i j a b = (if i = a then (1 : ℝ) else 0) * (if j = b then 1 else 0) := rfl

private theorem emat_trace (i j : Fin 3) : (Emat i j).trace = if i = j then 1 else 0 := by
  simp only [Matrix.trace, Matrix.diag, Fin.sum_univ_three, emat_apply]
  fin_cases i <;> fin_cases j <;> norm_num [Fin.ext_iff]

private theorem emat_transpose (i j : Fin 3) : (Emat i j)ᵀ = Emat j i := by
  ext a b
  simp only [Matrix.transpose_apply, emat_apply]
  ring

private theorem emat_mul_apply (i j r s a b : Fin 3) :
    (Emat i j * Emat r s) a b
      = (if i = a then (1 : ℝ) else 0) * ((if j = r then 1 else 0) * (if s = b then 1 else 0)) := by
  rw [Matrix.mul_apply, Finset.sum_eq_single j]
  · simp only [emat_apply]
    rcases eq_or_ne j r with h2 | h2
    · subst h2; simp
    · simp [h2, Ne.symm h2]
  · intro c _ hc
    simp only [emat_apply]
    simp [Ne.symm hc]
  · simp

private theorem emat_mul_trace (i j r s : Fin 3) :
    (Emat i j * Emat r s).trace = (if j = r then 1 else 0) * (if s = i then 1 else 0) := by
  simp only [Matrix.trace, Matrix.diag, Fin.sum_univ_three, emat_mul_apply]
  fin_cases i <;> fin_cases j <;> fin_cases r <;> fin_cases s <;> norm_num [Fin.ext_iff]

/-- The word/pattern dictionary: each of the fifteen words evaluated on the matrix units
`(E_ij, E_rs)` reproduces the corresponding `pat` delta triple. -/
theorem word_choi (k : ℕ) (hk : 1 ≤ k) (hk' : k ≤ 15) :
    word k (Emat (legA I) (legA J)) (Emat (legB J) (legC J)) (legB I) (legC I)
      = ((DefectChoi.pat k I J : ℤ) : ℝ) := by
  interval_cases k <;>
    simp only [word, DefectChoi.pat, ← legA_val, ← legB_val, ← legC_val, Int.cast_mul,
      dl_cast, emat_trace, emat_transpose,
      emat_mul_apply, emat_mul_trace, emat_apply, Matrix.smul_apply, Matrix.one_apply,
      smul_eq_mul] <;>
    split_ifs <;> simp_all

end WordChoi

/-- **The bridge (residual (a) of `Trust.lean`).**  The Choi matrix of the residual-family
defect superoperator at the forced point **is** the Appendix A matrix `Cmat x`. -/
theorem choi_defect_eq_Cmat {x q : ℝ} (hq : 9 * x * q ^ 2 = 2 * (1 - x)) :
    choiOf (Defect x q) = DefectChoi.Cmat x := by
  ext I J
  simp only [choiOf, Matrix.of_apply, defect_eq hq, defectClosed, DefectChoi.Cmat,
    Matrix.add_apply, Matrix.smul_apply, smul_eq_mul]
  rw [word_choi I J 1 (by norm_num) (by norm_num), word_choi I J 2 (by norm_num) (by norm_num),
    word_choi I J 3 (by norm_num) (by norm_num), word_choi I J 4 (by norm_num) (by norm_num),
    word_choi I J 5 (by norm_num) (by norm_num), word_choi I J 6 (by norm_num) (by norm_num),
    word_choi I J 7 (by norm_num) (by norm_num), word_choi I J 8 (by norm_num) (by norm_num),
    word_choi I J 9 (by norm_num) (by norm_num), word_choi I J 10 (by norm_num) (by norm_num),
    word_choi I J 11 (by norm_num) (by norm_num), word_choi I J 12 (by norm_num) (by norm_num),
    word_choi I J 13 (by norm_num) (by norm_num), word_choi I J 14 (by norm_num) (by norm_num),
    word_choi I J 15 (by norm_num) (by norm_num)]

/-! ## 7. The §7 ensemble inputs (paper `eq:ens`) -/

/-- The §7 diagonal witness state `ρ_ε = diag(1−2ε, ε, ε)`. -/
def rhoDiag (ε : ℝ) : Matrix (Fin 3) (Fin 3) ℝ := !![1 - 2 * ε, 0, 0; 0, ε, 0; 0, 0, ε]

/-- The §7 displacement `X = (E₁₂ + E₂₁)/√2`, with `r` standing for `√2`. -/
noncomputable def Xwit (r : ℝ) : Matrix (Fin 3) (Fin 3) ℝ := !![0, 0, 0; 0, 0, 1 / r; 0, 1 / r, 0]

/-! ## 8. The §6 witness family over ℂ — residual (b) at charpoly level (LEAN-4 WP-G)

Commissioned by
`channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_LEAN4_R9_M6_20260801.md`,
Track G.  Everything here is over `ℂ`: the §6 witness state is genuinely complex, so the
real layer of `WHGAP.Support.IcScalar` (which carries real symmetric *stand-ins* for the
Hermitian blocks) cannot state it.

Pre-verification (exact sympy, run before any of this was written):
`tools/whgap_lean4_wpg_check.py`, gates G0–G13, log
`artifacts/logs_whgap_lean4_20260801/wpg_sympy_gates.txt`.
-/

section Witness

open Polynomial

/-- `ψ = (e₁ + i e₂)/r`, with `r` carried as a real variable constrained only by `r² = 2`
(the same device `IcScalar` uses for `β`: no `Real.sqrt` enters the identity layer). -/
noncomputable def psiWit (r : ℝ) : Fin 3 → ℂ := ![1 / (r : ℂ), Complex.I / (r : ℂ), 0]

/-- `P_ψ` for the §6 witness vector — the explicit entries `±1/2, ±i/2`. -/
noncomputable def Pwit : Matrix (Fin 3) (Fin 3) ℂ :=
  !![1 / 2, -(Complex.I / 2), 0; Complex.I / 2, 1 / 2, 0; 0, 0, 0]

/-- `P_ψ̄`, the complex conjugate projector. -/
noncomputable def PwitBar : Matrix (Fin 3) (Fin 3) ℂ :=
  !![1 / 2, Complex.I / 2, 0; -(Complex.I / 2), 1 / 2, 0; 0, 0, 0]

/-- `P_ψ = ψψ†` really is the outer product of `ψ = (e₁ + i e₂)/√2`. -/
theorem Pwit_eq_outer {r : ℝ} (hr : r ^ 2 = 2) :
    (Matrix.of fun j k => psiWit r j * (starRingEnd ℂ) (psiWit r k)) = Pwit := by
  have hrc : (r : ℂ) ^ 2 = 2 := by exact_mod_cast hr
  have hrne : (r : ℂ) ≠ 0 := by
    intro h; rw [h] at hrc; norm_num at hrc
  ext j k
  fin_cases j <;> fin_cases k <;>
    simp [psiWit, Pwit, map_div₀, Complex.conj_I, Complex.conj_ofReal, div_mul_div_comm] <;>
    field_simp <;>
    first
      | linear_combination hrc
      | linear_combination -hrc

/-- `P_ψ̄ = ψ̄ψ̄†`. -/
theorem PwitBar_eq_outer {r : ℝ} (hr : r ^ 2 = 2) :
    (Matrix.of fun j k => (starRingEnd ℂ) (psiWit r j) * psiWit r k) = PwitBar := by
  have hrc : (r : ℂ) ^ 2 = 2 := by exact_mod_cast hr
  have hrne : (r : ℂ) ≠ 0 := by
    intro h; rw [h] at hrc; norm_num at hrc
  ext j k
  fin_cases j <;> fin_cases k <;>
    simp [psiWit, PwitBar, map_div₀, Complex.conj_I, Complex.conj_ofReal, div_mul_div_comm] <;>
    field_simp <;>
    first
      | linear_combination hrc
      | linear_combination -hrc

/-- The §6 witness state `ρ_ε = (1−ε) P_ψ + ε P_ψ̄`. -/
noncomputable def rhoWit (ε : ℂ) : Matrix (Fin 3) (Fin 3) ℂ :=
  (1 - ε) • Pwit + ε • PwitBar

/-- `ρ_ε` written out. -/
theorem rhoWit_eq (ε : ℂ) :
    rhoWit ε =
      !![1 / 2, -(Complex.I * (1 - 2 * ε) / 2), 0;
         Complex.I * (1 - 2 * ε) / 2, 1 / 2, 0;
         0, 0, 0] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rhoWit, Pwit, PwitBar, smul_eq_mul, Matrix.cons_val_two,
      Matrix.head_cons, Matrix.tail_cons, Matrix.head_fin_const] <;> ring

theorem rhoWit_trace (ε : ℂ) : (rhoWit ε).trace = 1 := by
  rw [rhoWit_eq]
  simp [Matrix.trace, Matrix.diag, Fin.sum_univ_three, Matrix.cons_val_two, Matrix.head_cons,
    Matrix.tail_cons, Matrix.head_fin_const]
  ring

/-- For a real parameter `ε` the witness state is Hermitian (not merely symmetric). -/
theorem rhoWit_isHermitian (ε : ℝ) : (rhoWit (ε : ℂ)).IsHermitian := by
  rw [rhoWit_eq]
  unfold Matrix.IsHermitian
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.conjTranspose_apply, Complex.conj_I, Complex.conj_ofReal,
      Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons, Matrix.head_fin_const] <;>
    ring

/-! ### The two explicit outputs -/

/-- **The B-side output.**  `Λ_x(ρ_ε)` is the explicit `3×3` complex Hermitian matrix
of note (7.1) — in the STANDARD basis, where it is *not* diagonal; `IcScalar.BOut` is its
diagonal form in the `(ψ, ψ̄, e₃)` frame. -/
theorem LamWit_eq (x ε : ℂ) :
    Lam x (rhoWit ε) =
      !![(1 - x / 2) / 2, -(Complex.I * (1 - 2 * ε) * (1 - x / 2) / 2), 0;
         Complex.I * (1 - 2 * ε) * (1 - x / 2) / 2, (1 - x / 2) / 2, 0;
         0, 0, x / 2] := by
  rw [rhoWit_eq]
  ext i j
  simp only [Lam, Matrix.add_apply, Matrix.smul_apply, Matrix.sub_apply, Matrix.transpose_apply,
    Matrix.one_apply, Matrix.trace, Matrix.diag, Fin.sum_univ_three, smul_eq_mul]
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons, Matrix.head_fin_const] <;>
    ring

/-- **The E-side output.**  `Λ^c_x(ρ_ε)` is the explicit `4×4` complex Hermitian matrix
of note (7.3), block-diagonal in the index split `{0,3} ⊔ {1,2}`. -/
theorem LamCWit_eq (x ε β : ℂ) :
    LamC x β (rhoWit ε) =
      !![1 - x, 0, 0, -(Complex.I * β * (1 - 2 * ε));
         0, x / 4, -(Complex.I * (x / 4) * (1 - 2 * ε)), 0;
         0, Complex.I * (x / 4) * (1 - 2 * ε), x / 4, 0;
         Complex.I * β * (1 - 2 * ε), 0, 0, x / 2] := by
  rw [rhoWit_eq]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [LamC, LamCgen, aVec, Matrix.trace, Matrix.diag, Fin.sum_univ_three,
      Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons,
      Matrix.head_fin_const] <;> ring

theorem LamWit_isHermitian (x ε : ℝ) : (Lam (x : ℂ) (rhoWit (ε : ℂ))).IsHermitian := by
  rw [LamWit_eq]
  unfold Matrix.IsHermitian
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.conjTranspose_apply, Complex.conj_I, Complex.conj_ofReal,
      Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons, Matrix.head_fin_const] <;>
    ring

theorem LamCWit_isHermitian (x ε β : ℝ) :
    (LamC (x : ℂ) (β : ℂ) (rhoWit (ε : ℂ))).IsHermitian := by
  rw [LamCWit_eq]
  unfold Matrix.IsHermitian
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.conjTranspose_apply, Complex.conj_I, Complex.conj_ofReal,
      Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons,
      Matrix.head_fin_const]

/-! ### Charpoly plumbing (block splittings, and the `2×2` root form) -/

/-- The reindexing `Fin 3 ≃ Fin 2 ⊕ Fin 1` that splits off the `e₃` direction. -/
def split3 : Fin 3 ≃ (Fin 2 ⊕ Fin 1) where
  toFun := ![Sum.inl 0, Sum.inl 1, Sum.inr 0]
  invFun := Sum.elim ![0, 1] ![2]
  left_inv := by decide
  right_inv := by decide

/-- The reindexing `Fin 4 ≃ Fin 2 ⊕ Fin 2` that splits `{0,3} ⊔ {1,2}` — the block
structure of `Λ^c_x(ρ_ε)`. -/
def split4 : Fin 4 ≃ (Fin 2 ⊕ Fin 2) where
  toFun := ![Sum.inl 0, Sum.inr 0, Sum.inr 1, Sum.inl 1]
  invFun := Sum.elim ![0, 3] ![1, 2]
  left_inv := by decide
  right_inv := by decide

/-- Charpoly of a matrix that becomes block diagonal after reindexing. -/
theorem charpoly_of_reindex_blocks {n m k : Type*} [Fintype n] [DecidableEq n] [Fintype m]
    [DecidableEq m] [Fintype k] [DecidableEq k] {M : Matrix n n ℂ} {A : Matrix m m ℂ}
    {D : Matrix k k ℂ} (e : n ≃ (m ⊕ k))
    (h : Matrix.reindex e e M = Matrix.fromBlocks A 0 0 D) :
    M.charpoly = A.charpoly * D.charpoly := by
  rw [← Matrix.charpoly_reindex e M, h, Matrix.charpoly_fromBlocks_zero₁₂]

/-- The `1×1` charpoly. -/
theorem charpoly_fin_one_eq (d : ℂ) : (!![d] : Matrix (Fin 1) (Fin 1) ℂ).charpoly = X - C d := by
  have h : (!![d] : Matrix (Fin 1) (Fin 1) ℂ) = Matrix.diagonal ![d] := by
    ext i j; fin_cases i; fin_cases j; simp
  rw [h, Matrix.charpoly_diagonal]
  simp

/-- The `2×2` charpoly in split form, from trace and determinant. -/
theorem charpoly_fin_two_eq {M : Matrix (Fin 2) (Fin 2) ℂ} {u v : ℂ}
    (htr : M.trace = u + v) (hdet : M.det = u * v) :
    M.charpoly = (X - C u) * (X - C v) := by
  rw [Matrix.charpoly_fin_two, htr, hdet, map_add, map_mul]
  ring

/-- The `2×2` charpoly in unsplit (quadratic) form, from trace and determinant. -/
theorem charpoly_fin_two_quad {M : Matrix (Fin 2) (Fin 2) ℂ} {p q : ℂ}
    (htr : M.trace = p) (hdet : M.det = q) :
    M.charpoly = X ^ 2 - C p * X + C q := by
  rw [Matrix.charpoly_fin_two, htr, hdet]

/-! ### The two charpoly theorems (residual (b) at charpoly level) -/

/-- **`specB_charpoly`.**  The characteristic polynomial of the COMPLEX B-side output
`Λ_x(ρ_ε)` splits over the `IcScalar.specB` list:

`charpoly Λ_x(ρ_ε) = (X − (1−ε)(1−x/2))·(X − ε(1−x/2))·(X − x/2)`.

Stated for arbitrary `x, ε : ℂ` (a polynomial identity; the physical case is real). -/
theorem specB_charpoly (x ε : ℂ) :
    (Lam x (rhoWit ε)).charpoly =
      (X - C ((1 - ε) * (1 - x / 2))) * (X - C (ε * (1 - x / 2))) * (X - C (x / 2)) := by
  have hblk : Matrix.reindex split3 split3 (Lam x (rhoWit ε))
      = Matrix.fromBlocks
          (!![(1 - x / 2) / 2, -(Complex.I * (1 - 2 * ε) * (1 - x / 2) / 2);
              Complex.I * (1 - 2 * ε) * (1 - x / 2) / 2, (1 - x / 2) / 2]
            : Matrix (Fin 2) (Fin 2) ℂ) 0 0 (!![x / 2] : Matrix (Fin 1) (Fin 1) ℂ) := by
    rw [LamWit_eq]
    ext i j
    rcases i with i | i <;> rcases j with j | j <;> fin_cases i <;> fin_cases j <;>
      simp [Matrix.reindex, Matrix.submatrix, split3, Matrix.cons_val_two, Matrix.head_cons,
        Matrix.tail_cons, Matrix.head_fin_const]
  rw [charpoly_of_reindex_blocks split3 hblk, charpoly_fin_one_eq]
  have htr : (!![(1 - x / 2) / 2, -(Complex.I * (1 - 2 * ε) * (1 - x / 2) / 2);
      Complex.I * (1 - 2 * ε) * (1 - x / 2) / 2, (1 - x / 2) / 2]
        : Matrix (Fin 2) (Fin 2) ℂ).trace
      = (1 - ε) * (1 - x / 2) + ε * (1 - x / 2) := by
    simp [Matrix.trace_fin_two_of]; ring
  have hdet : (!![(1 - x / 2) / 2, -(Complex.I * (1 - 2 * ε) * (1 - x / 2) / 2);
      Complex.I * (1 - 2 * ε) * (1 - x / 2) / 2, (1 - x / 2) / 2]
        : Matrix (Fin 2) (Fin 2) ℂ).det
      = ((1 - ε) * (1 - x / 2)) * (ε * (1 - x / 2)) := by
    rw [Matrix.det_fin_two_of]
    linear_combination ((1 - 2 * ε) ^ 2 * (1 - x / 2) ^ 2 / 4) * Complex.I_sq
  rw [charpoly_fin_two_eq htr hdet]

/-- **`specE_charpoly`.**  The characteristic polynomial of the COMPLEX E-side output
`Λ^c_x(ρ_ε)`, in the **square-root-free** form: the `λ±` pair appears as the quadratic
factor, which is exactly why the charpoly level was chosen (the roots themselves need
`√discE`, which no Lean statement here contains).

`charpoly Λ^c_x(ρ_ε) = (X² − (1−x/2)X + 2x(1−x)ε(1−ε))·(X − x(1−ε)/2)·(X − xε/2)`. -/
theorem specE_charpoly {x ε β : ℂ} (hβ : β ^ 2 = x * (1 - x) / 2) :
    (LamC x β (rhoWit ε)).charpoly =
      (X ^ 2 - C (1 - x / 2) * X + C (2 * x * (1 - x) * ε * (1 - ε)))
        * (X - C (x * (1 - ε) / 2)) * (X - C (x * ε / 2)) := by
  have hblk : Matrix.reindex split4 split4 (LamC x β (rhoWit ε))
      = Matrix.fromBlocks
          (!![1 - x, -(Complex.I * β * (1 - 2 * ε));
              Complex.I * β * (1 - 2 * ε), x / 2] : Matrix (Fin 2) (Fin 2) ℂ) 0 0
          (!![x / 4, -(Complex.I * (x / 4) * (1 - 2 * ε));
              Complex.I * (x / 4) * (1 - 2 * ε), x / 4] : Matrix (Fin 2) (Fin 2) ℂ) := by
    rw [LamCWit_eq]
    ext i j
    rcases i with i | i <;> rcases j with j | j <;> fin_cases i <;> fin_cases j <;>
      simp [Matrix.reindex, Matrix.submatrix, split4, Matrix.cons_val_two, Matrix.cons_val_three,
        Matrix.head_cons, Matrix.tail_cons, Matrix.head_fin_const]
  rw [charpoly_of_reindex_blocks split4 hblk]
  have htrA : (!![1 - x, -(Complex.I * β * (1 - 2 * ε));
      Complex.I * β * (1 - 2 * ε), x / 2] : Matrix (Fin 2) (Fin 2) ℂ).trace = 1 - x / 2 := by
    simp [Matrix.trace_fin_two_of]; ring
  have hdetA : (!![1 - x, -(Complex.I * β * (1 - 2 * ε));
      Complex.I * β * (1 - 2 * ε), x / 2] : Matrix (Fin 2) (Fin 2) ℂ).det
      = 2 * x * (1 - x) * ε * (1 - ε) := by
    rw [Matrix.det_fin_two_of]
    linear_combination (β ^ 2 * (1 - 2 * ε) ^ 2) * Complex.I_sq - ((1 - 2 * ε) ^ 2) * hβ
  have htrD : (!![x / 4, -(Complex.I * (x / 4) * (1 - 2 * ε));
      Complex.I * (x / 4) * (1 - 2 * ε), x / 4] : Matrix (Fin 2) (Fin 2) ℂ).trace
      = x * (1 - ε) / 2 + x * ε / 2 := by
    simp [Matrix.trace_fin_two_of]; ring
  have hdetD : (!![x / 4, -(Complex.I * (x / 4) * (1 - 2 * ε));
      Complex.I * (x / 4) * (1 - 2 * ε), x / 4] : Matrix (Fin 2) (Fin 2) ℂ).det
      = (x * (1 - ε) / 2) * (x * ε / 2) := by
    rw [Matrix.det_fin_two_of]
    linear_combination ((x / 4) ^ 2 * (1 - 2 * ε) ^ 2) * Complex.I_sq
  rw [charpoly_fin_two_quad htrA hdetA, charpoly_fin_two_eq htrD hdetD]
  ring

/-! ### Corollaries: the same two statements about the KRAUS-defined objects -/

/-- `specB_charpoly` for the Kraus sum itself. -/
theorem specB_charpoly_kraus {s t x ε : ℂ} (hs : s ^ 2 = x / 2) (ht : t ^ 2 = 1 - x) :
    (LamK s t (rhoWit ε)).charpoly =
      (X - C ((1 - ε) * (1 - x / 2))) * (X - C (ε * (1 - x / 2))) * (X - C (x / 2)) := by
  rw [LamK_eq hs ht, specB_charpoly]

/-- `specE_charpoly` for the Kraus-overlap complement itself.  `β = s t` then satisfies
`β² = x(1−x)/2` automatically. -/
theorem specE_charpoly_kraus {s t x ε : ℂ} (hs : s ^ 2 = x / 2) (ht : t ^ 2 = 1 - x) :
    (LamCK s t (rhoWit ε)).charpoly =
      (X ^ 2 - C (1 - x / 2) * X + C (2 * x * (1 - x) * ε * (1 - ε)))
        * (X - C (x * (1 - ε) / 2)) * (X - C (x * ε / 2)) := by
  have hβ : (s * t) ^ 2 = x * (1 - x) / 2 := by
    have : (s * t) ^ 2 = s ^ 2 * t ^ 2 := by ring
    rw [this, hs, ht]; ring
  rw [LamCK_eq hs ht, specE_charpoly hβ]

/-! ### The tie to `IcScalar`'s two eigenvalue lists -/

/-- The B-side charpoly IS the product over `WHGAP.Support.specB` (cast to `ℂ`). -/
theorem specB_charpoly_list (x ε : ℝ) :
    (Lam (x : ℂ) (rhoWit (ε : ℂ))).charpoly
      = (((specB x ε).map fun z : ℝ => X - C (z : ℂ)).prod) := by
  rw [specB_charpoly]
  simp only [specB, List.map_cons, List.map_nil, List.prod_cons, List.prod_nil]
  push_cast
  ring

/-- The quadratic factor of the E-side charpoly is `(X − λ₊)(X − λ₋)` for
`WHGAP.Support.lamP`, `lamM` — the square roots reappear only here, and only on the
physical domain `0 ≤ x ≤ 1`. -/
theorem quad_eq_lamP_lamM {x : ℝ} (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (ε : ℝ) :
    (X ^ 2 - C ((1 : ℂ) - (x : ℂ) / 2) * X
        + C (2 * (x : ℂ) * (1 - (x : ℂ)) * (ε : ℂ) * (1 - (ε : ℂ))))
      = (X - C ((lamP x ε : ℝ) : ℂ)) * (X - C ((lamM x ε : ℝ) : ℂ)) := by
  have hsum : ((lamP x ε : ℝ) : ℂ) + ((lamM x ε : ℝ) : ℂ) = 1 - (x : ℂ) / 2 := by
    have := lamP_add_lamM x ε
    exact_mod_cast congrArg (fun y : ℝ => (y : ℂ)) this
  have hprod : ((lamP x ε : ℝ) : ℂ) * ((lamM x ε : ℝ) : ℂ)
      = 2 * (x : ℂ) * (1 - (x : ℂ)) * (ε : ℂ) * (1 - (ε : ℂ)) := by
    have := lamP_mul_lamM hx0 hx1 ε
    exact_mod_cast congrArg (fun y : ℝ => (y : ℂ)) this
  rw [← hsum, ← hprod, map_add, map_mul]
  ring

/-- **The E-side charpoly IS the product over `WHGAP.Support.specE`** (cast to `ℂ`), on the
physical domain.  This is the statement `IcScalar`'s honesty note left in prose. -/
theorem specE_charpoly_list {x : ℝ} (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (ε β : ℝ)
    (hβ : (β : ℝ) ^ 2 = x * (1 - x) / 2) :
    (LamC (x : ℂ) (β : ℂ) (rhoWit (ε : ℂ))).charpoly
      = (((specE x ε).map fun z : ℝ => X - C (z : ℂ)).prod) := by
  have hβc : ((β : ℂ)) ^ 2 = (x : ℂ) * (1 - (x : ℂ)) / 2 := by exact_mod_cast hβ
  rw [specE_charpoly hβc, quad_eq_lamP_lamM hx0 hx1 ε]
  simp only [specE, List.map_cons, List.map_nil, List.prod_cons, List.prod_nil]
  push_cast
  ring_nf

end Witness

end WHGAP.Support.Channel

