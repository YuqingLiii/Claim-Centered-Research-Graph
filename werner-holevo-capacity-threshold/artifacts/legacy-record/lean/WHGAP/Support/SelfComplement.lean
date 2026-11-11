import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic

/-!
# `WHGAP.Support.SelfComplement` — the `x = 1` self-complementarity display (paper Lemma 4.1)

DAG protocol §7.3 support module (LEAN-3 WP-F item 2, 2026-08-01).  Serves the node
`WHGAP.zero-capacity-application` (P4), whose Corollary closes the endpoint `x = 1`, and
through it `WHGAP.goal`; it is imported by no node module (nothing downstream *needs* it —
see the scope block), so the §7.6 import-graph = children check is unaffected.

## What is formalized

Paper **Lemma 4.1** (`lem:x1`, `channel-capacity/werner-holevo-gap/paper/main.tex`) opens with
the entrywise display

    (Λ₁^{c,min}(X))_{μν} = ½ Tr(A_μ X A_ν†) = ½ (δ_{μν} Tr X − (Xᵀ)_{μν}) = (Λ₁(X))_{μν},

for the **minimal** Stinespring representation of the `x = 1` Werner–Holevo channel
`Λ₁(X) = ½(Tr(X)·𝟙 − Xᵀ)`: Kraus operators `A_μ/√2` with a **three**-dimensional environment,
`(A_μ)_{jk} = ε_{μjk}` the Levi-Civita matrices.  That display — *exactly* it, nothing more —
is `lamCmin_apply` and `lamCmin_eq_lamOne` below.  The `√2`'s of the Kraus operators cancel
against each other into the single factor `½`, which is why the identity is a pure `ring`
statement on `3×3` matrices with no square root anywhere.

`Λ_1` and `Λ₁^{c,min}` are taken over **ℝ**.  The paper writes `A_ν†`; the `A_μ` are real, so
`A_ν† = A_νᵀ` and the real statement is the full content of the display for real `X`.  (For
complex `X` the identity is the same `ring` fact applied to real and imaginary parts
separately, since the map is real-linear in the entries of `X`; that extension is *not*
formalized here.)

One transcription check of the Levi-Civita table ships with the module: `A_transpose`
(`A_μᵀ = −A_μ`, the antisymmetry that characterizes `ε_{μjk}` in `(j,k)`).  The stronger
contraction identity `∑_μ A_μ X A_μᵀ = Tr(X)·𝟙 − Xᵀ` of `eq:kraus` is **not** formalized
(it was dropped on build cost); note that `lamCmin_eq_lamOne` below is itself a sharp check of
the same table, since a mistranscribed `ε` would break it.

## SCOPE — what this does NOT establish

1. **The capacity conclusion of Lemma 4.1 stays an interface.**  The Lemma's payoff is
   "`J = id` is adjoint preserving, intertwines exactly, has identically vanishing (so
   trivially completely positive) defect, `Λ₁(𝟙) = 𝟙 ≻ 0`, hence Theorem `thm:zw` gives
   `P(Λ₁) = Q(Λ₁) = 0`".  Theorem `thm:zw` is the cited external Zhu–Wang result, carried in
   this development as the opaque field `zw_hrsf_zero` of `WHGAP.CapacityInterface`.  Nothing
   here touches `Q`, `P`, `Qone`, `Pone`.
2. **There is still no channel here.**  `LamOne` and `LamCmin` are two explicit `3×3` matrix
   *functions*; complete positivity, the Stinespring dilation, minimality of the
   representation, and the notion of "complementary channel" are all absent.  In particular
   the word *minimal* in "minimal Stinespring representation" is not formalized: the module
   posits the three-dimensional Kraus set and checks the display it satisfies.
3. **The degeneration of the padded presentation is not formalized.**  The paper's remark
   that the `4`-dimensional presentation `eq:comp` degenerates at `x = 1` (`K₀ = 0`,
   `Λ^c_1(𝟙) = diag(0,1,1,1)` not faithful) is not represented.
-/

namespace WHGAP.Support.SelfComplement

open Matrix

/-- `A_0`, `(A_0)_{jk} = ε_{0jk}`. -/
def A0 : Matrix (Fin 3) (Fin 3) ℝ := !![0, 0, 0; 0, 0, 1; 0, -1, 0]

/-- `A_1`, `(A_1)_{jk} = ε_{1jk}`. -/
def A1 : Matrix (Fin 3) (Fin 3) ℝ := !![0, 0, -1; 0, 0, 0; 1, 0, 0]

/-- `A_2`, `(A_2)_{jk} = ε_{2jk}`. -/
def A2 : Matrix (Fin 3) (Fin 3) ℝ := !![0, 1, 0; -1, 0, 0; 0, 0, 0]

/-- The Levi-Civita matrices `(A_μ)_{jk} = ε_{μjk}` (paper `eq:kraus`; indices run over
`{0,1,2}`).  The Kraus operators of the minimal `x = 1` representation are `A_μ/√2`. -/
def A : Fin 3 → Matrix (Fin 3) (Fin 3) ℝ := ![A0, A1, A2]

@[simp] lemma A_zero : A 0 = A0 := rfl
@[simp] lemma A_one : A 1 = A1 := rfl
@[simp] lemma A_two : A 2 = A2 := rfl

/-- The `x = 1` Werner–Holevo channel `Λ₁(X) = ½(Tr(X)·𝟙 − Xᵀ)`. -/
noncomputable def LamOne (X : Matrix (Fin 3) (Fin 3) ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  (1 / 2 : ℝ) • (X.trace • (1 : Matrix (Fin 3) (Fin 3) ℝ) - Xᵀ)

/-- The complement of `Λ₁` in its **minimal** (three-dimensional environment) Stinespring
representation: `(Λ₁^{c,min}(X))_{μν} = Tr((A_μ/√2) X (A_ν/√2)ᵀ) = ½ Tr(A_μ X A_νᵀ)`. -/
noncomputable def LamCmin (X : Matrix (Fin 3) (Fin 3) ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  Matrix.of fun μ ν => (1 / 2 : ℝ) * (A μ * X * (A ν)ᵀ).trace

/-- Transcription check: each `A_μ` is antisymmetric (`ε_{μjk}` is antisymmetric in `j,k`). -/
theorem A_transpose (μ : Fin 3) : (A μ)ᵀ = -A μ := by
  fin_cases μ <;> ext j k <;> fin_cases j <;> fin_cases k <;>
    simp [A0, A1, A2, Matrix.transpose_apply]

set_option maxHeartbeats 1000000 in
/-- **Paper Lemma 4.1, the entrywise display.**  `½ Tr(A_μ X A_νᵀ) = ½(δ_{μν} Tr X − (Xᵀ)_{μν})`
for every real `3×3` matrix `X` and all `μ, ν`. -/
theorem lamCmin_apply (X : Matrix (Fin 3) (Fin 3) ℝ) (μ ν : Fin 3) :
    (1 / 2 : ℝ) * (A μ * X * (A ν)ᵀ).trace
      = (1 / 2 : ℝ) * ((if μ = ν then X.trace else 0) - Xᵀ μ ν) := by
  fin_cases μ <;> fin_cases ν <;>
    simp only [Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three,
      Matrix.transpose_apply] <;>
    simp [A, A0, A1, A2] <;> ring

set_option maxHeartbeats 1000000 in
/-- **Paper Lemma 4.1, self-complementarity.**  In its minimal Stinespring representation the
`x = 1` Werner–Holevo channel equals its own complement: `Λ₁^{c,min}(X) = Λ₁(X)` for every
real `3×3` matrix `X`.  Consequently the identity lift `J = id` intertwines exactly and its
defect vanishes identically — but the capacity conclusion drawn from that in the paper is the
cited Zhu–Wang theorem, not this file (see the SCOPE block). -/
theorem lamCmin_eq_lamOne (X : Matrix (Fin 3) (Fin 3) ℝ) : LamCmin X = LamOne X := by
  ext μ ν
  have h := lamCmin_apply X μ ν
  unfold LamCmin LamOne
  simp only [Matrix.of_apply, Matrix.smul_apply, Matrix.sub_apply, Matrix.one_apply,
    smul_eq_mul]
  rw [h]
  by_cases hμν : μ = ν <;> simp [hμν, Matrix.transpose_apply]

/-- The defect of the identity lift vanishes identically: `Λ₁^{c,min} − Λ₁ = 0`. -/
theorem defect_identity_zero (X : Matrix (Fin 3) (Fin 3) ℝ) : LamCmin X - LamOne X = 0 := by
  rw [lamCmin_eq_lamOne, sub_self]

end WHGAP.Support.SelfComplement

