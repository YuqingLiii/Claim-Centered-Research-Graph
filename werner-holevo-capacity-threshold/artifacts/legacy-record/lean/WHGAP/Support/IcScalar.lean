import WHGAP.Support.Basic
import Mathlib.Analysis.SpecialFunctions.Log.NegMulLog
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.LinearAlgebra.Matrix.Charpoly.Coeff
import Mathlib.Data.Matrix.Block

/-!
# WHGAP scalar coherent information of the §6 witness family (DAG protocol §7.3 support module)

**Serves** the node modules `WHGAP.«no-ascent-hierarchy»` (P9) and, through it,
`WHGAP.«qpositive-onset»` (P3).  Commissioned by
`channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_LEAN2_20260731.md`, work
package **B**.  No node Claim lives in this file.

## The witness family

Paper §6 (`lem:exactspec`, `thm:positivity`) and §§7–8 of
`notes/WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md`: with `ψ = (e₁ + i e₂)/√2`,
`ρ_ε = (1-ε) P_ψ + ε P_ψ̄`, the two outputs of the noisy Werner–Holevo channel `Λ_x` and of
its complement are **exactly** diagonalizable in closed form,

* B side, in the orthonormal frame `(ψ, ψ̄, e₃)`:
  `Λ(ρ_ε) = diag((1-ε)(1-x/2), ε(1-x/2), x/2)` — note (7.1);
* E side, in the index split `{0,3} ⊔ {1,2}`:  `Λ^c(ρ_ε) = A(ε) ⊕ B(ε)` with
  `A(ε) = [[1-x, -iβ(1-2ε)], [iβ(1-2ε), x/2]]`, `β = √(x(1-x)/2)`, and
  `B(ε) = (x/4)[[1, -i(1-2ε)], [i(1-2ε), 1]]` — note (7.3), whence
  `spec A(ε) = {λ±}` with `λ± = ((1-x/2) ± √((1-x/2)² - 8x(1-x)ε(1-ε)))/2` and
  `spec B(ε) = {x(1-ε)/2, xε/2}` — note (7.4).

## Honesty note (what is and is not formalized here)

There is **no channel** in this development (project README, scope item 1).  `BOut`,
`blockA`, `blockB`, `EOut` are *defined* by the displays above; that they are the outputs of
`Λ_x` and `Λ_x^c` at `ρ_ε` is the note's gates **G2/G3** (exact symbolic computation from the
Kraus operators), not Lean.  What Lean checks here is (i) that those explicit matrices really
carry the stated eigen-data, and (ii) the **entire real-analytic positivity argument** for the
resulting scalar `IcScalar`.

**Pointer note, appended 2026-08-01 (LEAN-4/LEAN-5; applied per R15 m5).  The paragraph
immediately above is kept unedited as history, but two of its clauses are now weaker than
what the tree proves** — it was written before `WHGAP/Support/Channel.lean` existed:

* *the spectra identification is now IN LEAN.*  `Channel.specB_charpoly_list` and
  `Channel.specE_charpoly_list` (LEAN-4 WP-G) prove that the characteristic polynomials of
  the genuinely complex outputs `Λ_x(ρ_ε) = Channel.Lam x (Channel.rhoWit ε)` and
  `Λ^c_x(ρ_ε) = Channel.LamC x β (Channel.rhoWit ε)` split over exactly the two lists
  `specB`, `specE` defined below; `Channel.specB_charpoly_kraus`/`specE_charpoly_kraus` say
  the same of the Kraus sum `LamK` and the Kraus-overlap complement `LamCK`.  So "gates
  G2/G3, not Lean" no longer describes the *spectra*;
* *the entropy passage is now IN LEAN.*  `WHGAP.Support.IcScalar_eq_vnEntropyC_diff`
  (LEAN-5 WP-H, `WHGAP/Support/EntropyC.lean`) proves
  `IcScalar x ε = vnEntropyC (Λ_x(ρ_ε)) − vnEntropyC (Λ^c_x(ρ_ε))` for `0 ≤ x ≤ 1` and any
  `β` with `β² = x(1−x)/2`, so the scalar defined here IS the von Neumann entropy difference
  of those outputs, not merely a formula matching them numerically.  `Trust.lean` records
  residual (b) as DISCHARGED on this basis.

What is still NOT in Lean, and still qualifies reading `IcScalar` as a coherent information,
is unchanged and interface-tier: that `LamCK` is *the* complementary channel of `Lam`
(Stinespring/dilation) and LSD/Devetak achievability — `WHGAP/Interface.lean`.  The
`BOut`/`blockA`/`blockB`/`EOut` matrices below remain *definitions* in this module; they are
the real-symmetric stand-ins described in the next paragraph, and it is `Channel.LamWit_eq`/
`LamCWit_eq` — not these — that carry the identification.

`blockA`/`blockB` are **real symmetric stand-ins** for the Hermitian blocks: the off-diagonal
entries of the true blocks are `∓iβ(1-2ε)` resp. `∓i(x/4)(1-2ε)`, and only their *moduli*
enter trace, determinant and characteristic polynomial, so the real forms carry the same
spectrum — but they are not the Hermitian matrices themselves.  `β` is carried as a variable
constrained only by `hβ : β² = x(1-x)/2`, so no `Real.sqrt` enters the identity layer.

`Real.sqrt` **is** used from `discE` onwards: that layer is analysis, not identity checking,
and the discriminant nonnegativity `0 ≤ discE` is proved on the whole domain.

## The main theorem

`exists_eps_IcScalar_pos` : `∀ x, 0 < x → x < 2/5 → ∃ ε, 0 < ε ∧ ε < 1 ∧ 0 < IcScalar x ε`,
sorry-free and with **no hypothesis beyond `0 < x < 2/5`**.  This is the Lean form of paper
Theorem `thm:positivity` / Theorem 8.1 of the N1′ note, *for this one witness family*, and it
replaces the abstract expansion hypothesis `hexp` of
`WHGAP.«no-ascent-hierarchy».exists_pos_of_expansion` by a carried proof.

### Route (executor's; deviates from the commission's suggested bracketing — see the report)

Write `β = 1 - x/2`, `c = x/2`, `μ_A = 2x(1-x)/β`, and split the seven `negMulLog` terms as

    Ic = [nml((1-ε)β) - nml(λ₊)]                       (G2)
       + [nml(εβ) - nml(cε) - nml(λ₋)]                 (G1)
       + [nml(c)  - nml(c(1-ε))]                       (G3)

Then, for `0 < x < 2/5` and `0 < ε ≤ 1/3`:

* **G3 ≥ 0** from `nml(c(1-ε)) = (1-ε) nml c + c nml(1-ε)`, `nml(1-ε) ≤ ε` and `c ≤ e⁻¹`;
* **G2 ≥ 0** because `λ₊ ≥ (1-ε)β ≥ e⁻¹` and `nml` is antitone on `[e⁻¹, ∞)`;
* **G1 ≥ d₁(x)·nml ε - 2ε** from `λ₋ ≤ μ_A ε ≤ e⁻¹`, `nml` monotone on `(0, e⁻¹]`,
  `nml(ab) = b nml a + a nml b`, `nml β ≥ 0`, `nml c ≤ 1`, `nml μ_A ≤ 1`, and the identity
  `(1-x) - μ_A(x) = d₁(x) = (1-x)(2-5x)/(2-x)`.

The witness is the explicit `ε(x) = min(1/3, exp(-3/d₁(x)))`, which gives
`Ic ≥ ε(3 - 2) = ε > 0`.  Two exact algebraic identities carry the eigenvalue bookkeeping:
`discE = (1-3x/2)² + 2x(1-x)(1-2ε)²` (whence `discE ≥ 0` everywhere) and
`discE - β²(1-2ε)² = 4ε(1-ε)(1-3x/2)²` (whence `λ₋ ≤ εβ`).
-/

namespace WHGAP.Support

open Real

/-! ## 1. The matrix identification layer (paper Lemma 6.1 / note §7.1–§7.2) -/

/-- The B-side output `Λ(ρ_ε)` of the §6 witness, in the orthonormal frame `(ψ, ψ̄, e₃)`
(note (7.1)).  Diagonal, exactly, for all `ε`. -/
noncomputable def BOut (x ε : ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  !![(1 - ε) * (1 - x / 2), 0, 0;
     0, ε * (1 - x / 2), 0;
     0, 0, x / 2]

/-- The `ψ` frame vector is an eigenvector of `BOut` with eigenvalue `(1-ε)(1-x/2)`. -/
theorem BOut_mulVec_psi (x ε : ℝ) :
    (BOut x ε).mulVec ![1, 0, 0] = ((1 - ε) * (1 - x / 2)) • ![1, 0, 0] := by
  funext i
  fin_cases i <;> simp [BOut, Matrix.mulVec, dotProduct, Fin.sum_univ_three]

/-- The `ψ̄` frame vector is an eigenvector of `BOut` with eigenvalue `ε(1-x/2)`. -/
theorem BOut_mulVec_psibar (x ε : ℝ) :
    (BOut x ε).mulVec ![0, 1, 0] = (ε * (1 - x / 2)) • ![0, 1, 0] := by
  funext i
  fin_cases i <;> simp [BOut, Matrix.mulVec, dotProduct, Fin.sum_univ_three]

/-- The `e₃` frame vector is an eigenvector of `BOut` with eigenvalue `x/2`. -/
theorem BOut_mulVec_e3 (x ε : ℝ) :
    (BOut x ε).mulVec ![0, 0, 1] = (x / 2) • ![0, 0, 1] := by
  funext i
  fin_cases i <;> simp [BOut, Matrix.mulVec, dotProduct, Fin.sum_univ_three]

/-- `Tr Λ(ρ_ε) = 1` — the B-side output is a state for every `ε`. -/
theorem BOut_trace (x ε : ℝ) : Matrix.trace (BOut x ε) = 1 := by
  simp [BOut, Matrix.trace, Matrix.diag, Fin.sum_univ_three]
  ring

/-- The `{0,3}` block `A(ε)` of the E-side output (note (7.3)), as the **real symmetric
stand-in**: `β` is a variable, constrained only by `β² = x(1-x)/2`. -/
noncomputable def blockA (x ε β : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![1 - x, -(β * (1 - 2 * ε)); -(β * (1 - 2 * ε)), x / 2]

/-- The `{1,2}` block `B(ε)` of the E-side output (note (7.3)), real symmetric stand-in. -/
noncomputable def blockB (x ε : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![x / 4, -(x / 4 * (1 - 2 * ε)); -(x / 4 * (1 - 2 * ε)), x / 4]

/-- The E-side output `Λ^c(ρ_ε)`, exhibited as the block-diagonal matrix `A(ε) ⊕ B(ε)` in
the index split `{0,3} ⊔ {1,2}` (note (7.3)). -/
noncomputable def EOut (x ε β : ℝ) : Matrix (Fin 2 ⊕ Fin 2) (Fin 2 ⊕ Fin 2) ℝ :=
  Matrix.fromBlocks (blockA x ε β) 0 0 (blockB x ε)

/-- All eight cross-block entries of the E-side output vanish (note (7.3), gate G3). -/
theorem EOut_offBlock_zero (x ε β : ℝ) (i j : Fin 2) :
    EOut x ε β (Sum.inl i) (Sum.inr j) = 0 ∧ EOut x ε β (Sum.inr i) (Sum.inl j) = 0 := by
  constructor <;> simp [EOut]

/-- `Tr Λ^c(ρ_ε) = 1` — the E-side output is a state for every `ε`. -/
theorem EOut_trace (x ε β : ℝ) : Matrix.trace (EOut x ε β) = 1 := by
  simp [EOut, blockA, blockB, Matrix.trace, Matrix.diag, Fintype.sum_sum_type,
    Fin.sum_univ_two]
  ring

/-- **The characteristic polynomial of the `A(ε)` block** (commissioned form):
`charpoly A(ε) = X² - (1 - x/2) X + 2x(1-x)ε(1-ε)`, with `β` carried as a variable. -/
theorem blockA_charpoly (x ε β : ℝ) (hβ : β ^ 2 = x * (1 - x) / 2) :
    (blockA x ε β).charpoly =
      Polynomial.X ^ 2 - Polynomial.C (1 - x / 2) * Polynomial.X
        + Polynomial.C (2 * x * (1 - x) * ε * (1 - ε)) := by
  rw [Matrix.charpoly_fin_two]
  have ht : (blockA x ε β).trace = 1 - x / 2 := by
    simp [blockA, Matrix.trace_fin_two_of]; ring
  have hd : (blockA x ε β).det = 2 * x * (1 - x) * ε * (1 - ε) := by
    rw [blockA, Matrix.det_fin_two_of]
    linear_combination (-(1 - 2 * ε) ^ 2) * hβ
  rw [ht, hd]

/-- The `(1,-1)` direction is an eigenvector of the `B(ε)` block with eigenvalue
`x(1-ε)/2` (note (7.4)). -/
theorem blockB_mulVec_large (x ε : ℝ) :
    (blockB x ε).mulVec ![1, -1] = (x * (1 - ε) / 2) • ![1, -1] := by
  funext i
  fin_cases i <;>
    simp [blockB, Matrix.mulVec, dotProduct, Fin.sum_univ_two] <;> ring

/-- The `(1,1)` direction is an eigenvector of the `B(ε)` block with eigenvalue
`xε/2` (note (7.4)). -/
theorem blockB_mulVec_small (x ε : ℝ) :
    (blockB x ε).mulVec ![1, 1] = (x * ε / 2) • ![1, 1] := by
  funext i
  fin_cases i <;>
    simp [blockB, Matrix.mulVec, dotProduct, Fin.sum_univ_two] <;> ring

/-! ## 2. The scalar spectra and `IcScalar` -/

/-- The discriminant of the `A(ε)` block: `(1-x/2)² - 8x(1-x)ε(1-ε)`. -/
noncomputable def discE (x ε : ℝ) : ℝ := (1 - x / 2) ^ 2 - 8 * x * (1 - x) * ε * (1 - ε)

/-- The exact SOS form of the discriminant.  Everything about `discE ≥ 0` follows. -/
theorem discE_eq (x ε : ℝ) :
    discE x ε = (1 - 3 * x / 2) ^ 2 + 2 * x * (1 - x) * (1 - 2 * ε) ^ 2 := by
  unfold discE; ring

/-- `0 ≤ discE x ε` on the physical domain `0 ≤ x ≤ 1` (all `ε`). -/
theorem discE_nonneg {x : ℝ} (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (ε : ℝ) : 0 ≤ discE x ε := by
  rw [discE_eq]
  have : 0 ≤ 2 * x * (1 - x) := by nlinarith
  nlinarith [sq_nonneg (1 - 3 * x / 2), sq_nonneg (1 - 2 * ε)]

/-- The large eigenvalue of the `A(ε)` block. -/
noncomputable def lamP (x ε : ℝ) : ℝ := ((1 - x / 2) + Real.sqrt (discE x ε)) / 2

/-- The small eigenvalue of the `A(ε)` block. -/
noncomputable def lamM (x ε : ℝ) : ℝ := ((1 - x / 2) - Real.sqrt (discE x ε)) / 2

/-- The B-side spectrum of `Λ(ρ_ε)` as an explicit list (note (7.1)). -/
noncomputable def specB (x ε : ℝ) : List ℝ := [(1 - ε) * (1 - x / 2), ε * (1 - x / 2), x / 2]

/-- The E-side spectrum of `Λ^c(ρ_ε)` as an explicit list (note (7.3)/(7.4)). -/
noncomputable def specE (x ε : ℝ) : List ℝ :=
  [lamP x ε, lamM x ε, (x / 2) * (1 - ε), (x / 2) * ε]

/-- **The scalar coherent information** `Ic(ρ_ε) = S(Λ(ρ_ε)) - S(Λ^c(ρ_ε))` of the §6
witness family, as a sum of `Real.negMulLog` over the two explicit eigenvalue lists (nats). -/
noncomputable def IcScalar (x ε : ℝ) : ℝ :=
  ((specB x ε).map Real.negMulLog).sum - ((specE x ε).map Real.negMulLog).sum

/-- `IcScalar` written out term by term. -/
theorem IcScalar_eq (x ε : ℝ) :
    IcScalar x ε =
      (Real.negMulLog ((1 - ε) * (1 - x / 2)) + Real.negMulLog (ε * (1 - x / 2))
        + Real.negMulLog (x / 2))
      - (Real.negMulLog (lamP x ε) + Real.negMulLog (lamM x ε)
        + Real.negMulLog ((x / 2) * (1 - ε)) + Real.negMulLog ((x / 2) * ε)) := by
  simp [IcScalar, specB, specE]
  ring

/-! ## 3. Eigenvalue bookkeeping -/

section Spectrum

variable {x ε : ℝ}

theorem lamP_add_lamM (x ε : ℝ) : lamP x ε + lamM x ε = 1 - x / 2 := by
  unfold lamP lamM; ring

theorem lamP_mul_lamM (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (ε : ℝ) :
    lamP x ε * lamM x ε = 2 * x * (1 - x) * ε * (1 - ε) := by
  have hs : Real.sqrt (discE x ε) ^ 2 = discE x ε :=
    Real.sq_sqrt (discE_nonneg hx0 hx1 ε)
  unfold lamP lamM
  have : ((1 - x / 2) + Real.sqrt (discE x ε)) * ((1 - x / 2) - Real.sqrt (discE x ε)) / 4
      = ((1 - x / 2) ^ 2 - Real.sqrt (discE x ε) ^ 2) / 4 := by ring
  rw [show ((1 - x / 2) + Real.sqrt (discE x ε)) / 2 * (((1 - x / 2) - Real.sqrt (discE x ε)) / 2)
      = ((1 - x / 2) ^ 2 - Real.sqrt (discE x ε) ^ 2) / 4 by ring, hs]
  unfold discE; ring

/-- `λ₊ ≥ λ₋` and both are real: `√discE ≤ 1 - x/2`. -/
theorem sqrt_discE_le (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1) :
    Real.sqrt (discE x ε) ≤ 1 - x / 2 := by
  have hb : (0:ℝ) ≤ 1 - x / 2 := by linarith
  have hle : discE x ε ≤ (1 - x / 2) ^ 2 := by
    have hnn : 0 ≤ 8 * x * (1 - x) * ε * (1 - ε) :=
      mul_nonneg (mul_nonneg (mul_nonneg (by linarith : (0:ℝ) ≤ 8 * x)
        (by linarith : (0:ℝ) ≤ 1 - x)) hε0) (by linarith : (0:ℝ) ≤ 1 - ε)
    unfold discE; linarith
  calc Real.sqrt (discE x ε) ≤ Real.sqrt ((1 - x / 2) ^ 2) := Real.sqrt_le_sqrt hle
    _ = 1 - x / 2 := by rw [Real.sqrt_sq hb]

/-- **`λ₋ ≤ εβ`** — the key exact bracket, from `discE - β²(1-2ε)² = 4ε(1-ε)(1-3x/2)² ≥ 0`. -/
theorem lamM_le_eps_beta (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1) :
    lamM x ε ≤ ε * (1 - x / 2) := by
  have hkey : ((1 - x / 2) * (1 - 2 * ε)) ^ 2 ≤ discE x ε := by
    unfold discE
    nlinarith [sq_nonneg (1 - 3 * x / 2), mul_nonneg hε0 (by linarith : (0:ℝ) ≤ 1 - ε),
      sq_nonneg (1 - 2 * ε)]
  have h1 : (1 - x / 2) * (1 - 2 * ε) ≤ Real.sqrt (discE x ε) := by
    calc (1 - x / 2) * (1 - 2 * ε) ≤ |(1 - x / 2) * (1 - 2 * ε)| := le_abs_self _
      _ = Real.sqrt (((1 - x / 2) * (1 - 2 * ε)) ^ 2) := (Real.sqrt_sq_eq_abs _).symm
      _ ≤ Real.sqrt (discE x ε) := Real.sqrt_le_sqrt hkey
  unfold lamM
  linarith

/-- `λ₊ ≥ (1-ε)β`. -/
theorem lamP_ge (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1) :
    (1 - ε) * (1 - x / 2) ≤ lamP x ε := by
  have h := lamM_le_eps_beta (x := x) (ε := ε) hε0 hε1
  have hs := lamP_add_lamM x ε
  nlinarith [h, hs]

/-- `λ₋ ≥ 0`. -/
theorem lamM_nonneg (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1) :
    0 ≤ lamM x ε := by
  have := sqrt_discE_le hx0 hx1 hε0 hε1
  unfold lamM; linarith

/-- `λ₋ > 0` strictly, on the open domain. -/
theorem lamM_pos (hx0 : 0 < x) (hx1 : x < 1) (hε0 : 0 < ε) (hε1 : ε < 1) :
    0 < lamM x ε := by
  have h1x : (0:ℝ) < 1 - x := by linarith
  have h1e : (0:ℝ) < 1 - ε := by linarith
  have hprod := lamP_mul_lamM hx0.le hx1.le ε
  have hD : 0 < 2 * x * (1 - x) * ε * (1 - ε) :=
    mul_pos (mul_pos (mul_pos (by linarith : (0:ℝ) < 2 * x) h1x) hε0) h1e
  have hM := lamM_nonneg hx0.le hx1.le hε0.le hε1.le
  rcases hM.lt_or_eq with h | h
  · exact h
  · exfalso
    rw [← h, mul_zero] at hprod
    linarith

/-- **`λ₋ ≤ μ_A ε`** with `μ_A = 2x(1-x)/(1-x/2)`: the *sharp* leading bracket, obtained from
`λ₊λ₋ = D` and `λ₊ ≥ (1-ε)β`.  This is what makes the leading coefficient exactly `d₁(x)`. -/
theorem lamM_le_muA (hx0 : 0 < x) (hx1 : x < 1) (hε0 : 0 < ε) (hε1 : ε < 1) :
    lamM x ε ≤ 2 * x * (1 - x) / (1 - x / 2) * ε := by
  have hb : (0:ℝ) < 1 - x / 2 := by linarith
  have hprod := lamP_mul_lamM hx0.le hx1.le ε
  have hPge := lamP_ge (x := x) (ε := ε) hε0.le hε1.le
  have hM := lamM_nonneg hx0.le hx1.le hε0.le hε1.le
  have h1e : (0:ℝ) < 1 - ε := by linarith
  -- λ₋ · (1-ε)β ≤ λ₋ λ₊ = 2x(1-x)ε(1-ε)
  have hstep : lamM x ε * ((1 - ε) * (1 - x / 2)) ≤ 2 * x * (1 - x) * ε * (1 - ε) := by
    calc lamM x ε * ((1 - ε) * (1 - x / 2)) ≤ lamM x ε * lamP x ε :=
          mul_le_mul_of_nonneg_left hPge hM
      _ = 2 * x * (1 - x) * ε * (1 - ε) := by rw [mul_comm]; exact hprod
  rw [div_mul_eq_mul_div, le_div_iff₀ hb]
  nlinarith [hstep, h1e]

end Spectrum

/-! ## 4. Two elementary `negMulLog` monotonicity facts

Both are proved from `Real.log_le_sub_one_of_pos` alone. -/

/-- `negMulLog` is antitone on `[e⁻¹, ∞)`. -/
theorem negMulLog_antitone {s t : ℝ} (hs : Real.exp (-1) ≤ s) (hst : s ≤ t) :
    Real.negMulLog t ≤ Real.negMulLog s := by
  have hs0 : 0 < s := lt_of_lt_of_le (Real.exp_pos _) hs
  have ht0 : 0 < t := lt_of_lt_of_le hs0 hst
  have hlogs : (-1 : ℝ) ≤ Real.log s := by
    have h := Real.log_le_log (Real.exp_pos (-1)) hs
    rwa [Real.log_exp] at h
  have hkey : Real.log s - Real.log t ≤ s / t - 1 := by
    have h := Real.log_le_sub_one_of_pos (div_pos hs0 ht0)
    rwa [Real.log_div hs0.ne' ht0.ne'] at h
  have h1 : t - s ≤ t * (Real.log t - Real.log s) := by
    have hm := mul_le_mul_of_nonneg_left hkey ht0.le
    have he : t * (s / t - 1) = s - t := by field_simp
    rw [he] at hm
    linarith
  have h2 : -(t - s) ≤ (t - s) * Real.log s := by nlinarith [sub_nonneg.mpr hst]
  simp only [Real.negMulLog, neg_mul]
  nlinarith [h1, h2]

/-- `negMulLog` is monotone on `(0, e⁻¹]`. -/
theorem negMulLog_mono {s t : ℝ} (hs : 0 < s) (hst : s ≤ t) (ht : t ≤ Real.exp (-1)) :
    Real.negMulLog s ≤ Real.negMulLog t := by
  have ht0 : 0 < t := lt_of_lt_of_le hs hst
  have hlogt : Real.log t ≤ -1 := by
    have h := Real.log_le_log ht0 ht
    rwa [Real.log_exp] at h
  have hkey : Real.log t - Real.log s ≤ t / s - 1 := by
    have h := Real.log_le_sub_one_of_pos (div_pos ht0 hs)
    rwa [Real.log_div ht0.ne' hs.ne'] at h
  have h1 : s * (Real.log t - Real.log s) ≤ t - s := by
    have hm := mul_le_mul_of_nonneg_left hkey hs.le
    have he : s * (t / s - 1) = t - s := by field_simp
    rw [he] at hm
    exact hm
  have h2 : (t - s) * Real.log t ≤ -(t - s) := by nlinarith [sub_nonneg.mpr hst]
  simp only [Real.negMulLog, neg_mul]
  nlinarith [h1, h2]

/-- `e⁻¹ < 2/5`. -/
theorem exp_neg_one_lt : Real.exp (-1) < 2 / 5 := by
  rw [Real.exp_neg]
  have h : (2.7182818283 : ℝ) < Real.exp 1 := Real.exp_one_gt_d9
  have hpos : (0:ℝ) < Real.exp 1 := Real.exp_pos 1
  rw [inv_lt_comm₀ hpos (by norm_num)]
  linarith

/-- `1/3 < e⁻¹`. -/
theorem exp_neg_one_gt : (1:ℝ) / 3 < Real.exp (-1) := by
  rw [Real.exp_neg]
  have h : Real.exp 1 < 2.7182818286 := Real.exp_one_lt_d9
  have hpos : (0:ℝ) < Real.exp 1 := Real.exp_pos 1
  rw [lt_inv_comm₀ (by norm_num) hpos]
  linarith

/-! ## 5. The three group bounds -/

section Groups

variable {x ε : ℝ}

/-- **G3 ≥ 0**: `nml(x/2) - nml((x/2)(1-ε)) ≥ 0` for `0 < x/2 ≤ e⁻¹` and `0 ≤ ε ≤ 1`. -/
theorem group3_nonneg (hx0 : 0 < x) (hxe : x / 2 ≤ Real.exp (-1))
    (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1) :
    0 ≤ Real.negMulLog (x / 2) - Real.negMulLog ((x / 2) * (1 - ε)) := by
  have hc0 : (0:ℝ) < x / 2 := by linarith
  have hmul : Real.negMulLog ((x / 2) * (1 - ε))
      = (1 - ε) * Real.negMulLog (x / 2) + (x / 2) * Real.negMulLog (1 - ε) :=
    Real.negMulLog_mul _ _
  have hone : Real.negMulLog (1 - ε) ≤ ε := by
    have h := Real.negMulLog_le_one_sub_self (x := 1 - ε) (by linarith)
    linarith
  -- nml c - c = -c (log c + 1) ≥ 0 because log c ≤ -1
  have hlogc : Real.log (x / 2) ≤ -1 := by
    have h := Real.log_le_log hc0 hxe
    rwa [Real.log_exp] at h
  have hnml : x / 2 ≤ Real.negMulLog (x / 2) := by
    simp only [Real.negMulLog, neg_mul]
    nlinarith [hlogc, hc0]
  rw [hmul]
  nlinarith [hone, hnml, hc0, hε0]

/-- **G2 ≥ 0**: `nml((1-ε)β) - nml(λ₊) ≥ 0`. -/
theorem group2_nonneg (hx0 : 0 < x) (hx25 : x < 2 / 5) (hε0 : 0 < ε) (hε3 : ε ≤ 1 / 3) :
    0 ≤ Real.negMulLog ((1 - ε) * (1 - x / 2)) - Real.negMulLog (lamP x ε) := by
  have hlow : Real.exp (-1) ≤ (1 - ε) * (1 - x / 2) := by
    have h1 : (2:ℝ) / 3 ≤ 1 - ε := by linarith
    have h2 : (4:ℝ) / 5 < 1 - x / 2 := by linarith
    have : (2:ℝ) / 5 ≤ (1 - ε) * (1 - x / 2) := by nlinarith
    linarith [exp_neg_one_lt]
  have hle := lamP_ge (x := x) (ε := ε) hε0.le (by linarith : ε ≤ 1)
  linarith [negMulLog_antitone hlow hle]

/-- **G1 lower bound**: `nml(εβ) - nml(cε) - nml(λ₋) ≥ d₁(x)·nml ε - 2ε`. -/
theorem group1_lower (hx0 : 0 < x) (hx25 : x < 2 / 5) (hε0 : 0 < ε) (hε3 : ε ≤ 1 / 3) :
    dOne x * Real.negMulLog ε - 2 * ε ≤
      Real.negMulLog (ε * (1 - x / 2)) - Real.negMulLog ((x / 2) * ε)
        - Real.negMulLog (lamM x ε) := by
  have hx1 : x < 1 := by linarith
  have hε1 : ε < 1 := by linarith
  have hb : (0:ℝ) < 1 - x / 2 := by linarith
  set μ : ℝ := 2 * x * (1 - x) / (1 - x / 2) with hμdef
  have hμ0 : 0 ≤ μ := by
    rw [hμdef]; positivity
  have hμ1 : μ ≤ 1 := by
    rw [hμdef, div_le_one hb]; nlinarith
  -- λ₋ ≤ με ≤ e⁻¹
  have hMle : lamM x ε ≤ μ * ε := lamM_le_muA hx0 hx1 hε0 hε1
  have hMpos : 0 < lamM x ε := lamM_pos hx0 hx1 hε0 hε1
  have hμε : μ * ε ≤ Real.exp (-1) := by
    have : μ * ε ≤ 1 * (1 / 3) := by
      apply mul_le_mul hμ1 hε3 hε0.le zero_le_one
    linarith [exp_neg_one_gt]
  have hstep : Real.negMulLog (lamM x ε) ≤ Real.negMulLog (μ * ε) :=
    negMulLog_mono hMpos hMle hμε
  -- expand the three products
  have e1 : Real.negMulLog (ε * (1 - x / 2))
      = (1 - x / 2) * Real.negMulLog ε + ε * Real.negMulLog (1 - x / 2) :=
    Real.negMulLog_mul _ _
  have e2 : Real.negMulLog ((x / 2) * ε)
      = ε * Real.negMulLog (x / 2) + (x / 2) * Real.negMulLog ε :=
    Real.negMulLog_mul _ _
  have e3 : Real.negMulLog (μ * ε) = ε * Real.negMulLog μ + μ * Real.negMulLog ε :=
    Real.negMulLog_mul _ _
  -- the three constant-order bounds
  have hbeta : 0 ≤ Real.negMulLog (1 - x / 2) :=
    Real.negMulLog_nonneg (by linarith) (by linarith)
  have hcbd : Real.negMulLog (x / 2) ≤ 1 := by
    have := Real.negMulLog_le_one_sub_self (x := x / 2) (by linarith)
    linarith
  have hμbd : Real.negMulLog μ ≤ 1 := by
    have := Real.negMulLog_le_one_sub_self (x := μ) hμ0
    linarith
  -- the leading-coefficient identity (1-x) - μ = d₁(x)
  have hid : (1 - x / 2) - x / 2 - μ = dOne x := by
    rw [hμdef, dOne]
    have h1 : (1 - x / 2) ≠ 0 := ne_of_gt hb
    have h2 : (2 - x) ≠ 0 := by intro h; linarith
    field_simp
    ring
  have hA : 0 ≤ ε * Real.negMulLog (1 - x / 2) := mul_nonneg hε0.le hbeta
  have hB : ε * Real.negMulLog (x / 2) ≤ ε * 1 := mul_le_mul_of_nonneg_left hcbd hε0.le
  have hC : ε * Real.negMulLog μ ≤ ε * 1 := mul_le_mul_of_nonneg_left hμbd hε0.le
  have hid2 : dOne x * Real.negMulLog ε
      = (1 - x / 2) * Real.negMulLog ε - x / 2 * Real.negMulLog ε
        - μ * Real.negMulLog ε := by
    rw [← hid]; ring
  rw [e1, e2]
  linarith [hstep, e3, hA, hB, hC, hid2]

end Groups

/-! ## 6. The main theorem -/

/-- **The uniform lower bound.**  For `0 < x < 2/5` and `0 < ε ≤ 1/3`,
`IcScalar x ε ≥ d₁(x)·negMulLog ε - 2ε`, with `d₁(x) = (1-x)(2-5x)/(2-x)` the isotropic
first-order weight (`WHGAP.Support.dOne`).  All three group bounds are unconditional on
this domain. -/
theorem IcScalar_lower_bound {x ε : ℝ} (hx0 : 0 < x) (hx25 : x < 2 / 5)
    (hε0 : 0 < ε) (hε3 : ε ≤ 1 / 3) :
    dOne x * Real.negMulLog ε - 2 * ε ≤ IcScalar x ε := by
  have hxe : x / 2 ≤ Real.exp (-1) := by linarith [exp_neg_one_gt]
  have g3 := group3_nonneg hx0 hxe hε0.le (by linarith)
  have g2 := group2_nonneg hx0 hx25 hε0 hε3
  have g1 := group1_lower hx0 hx25 hε0 hε3
  rw [IcScalar_eq]
  linarith

/-- **MAIN THEOREM (WP-B).**  For every `x ∈ (0, 2/5)` there is an `ε ∈ (0,1)` with
`IcScalar x ε > 0`: the §6 witness family has strictly positive coherent information
throughout `(0, 2/5)`.

Sorry-free, and with **no hypothesis beyond `0 < x < 2/5`** — in particular no abstract
expansion hypothesis.  The witness is explicit: `ε(x) = min(1/3, exp(-3/d₁(x)))`, the Lean
analogue of the threshold `ε₁(x)` of Theorem 8.1 of
`notes/WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md` (with a cheaper constant: `3` in place of
the note's `C(x)`, because the bound proved here already absorbs the remainder). -/
theorem exists_eps_IcScalar_pos (x : ℝ) (hx0 : 0 < x) (hx25 : x < 2 / 5) :
    ∃ ε : ℝ, 0 < ε ∧ ε < 1 ∧ 0 < IcScalar x ε := by
  have hd : 0 < dOne x := by
    have h2x : (0:ℝ) < 2 - x := by linarith
    unfold dOne
    exact div_pos (by nlinarith) h2x
  set ε : ℝ := min (1 / 3) (Real.exp (-(3 / dOne x))) with hεdef
  have hE : 0 < Real.exp (-(3 / dOne x)) := Real.exp_pos _
  have hε0 : 0 < ε := lt_min (by norm_num) hE
  have hε3 : ε ≤ 1 / 3 := min_le_left _ _
  have hε1 : ε < 1 := by linarith
  refine ⟨ε, hε0, hε1, ?_⟩
  have hbound := IcScalar_lower_bound hx0 hx25 hε0 hε3
  -- log ε ≤ -3/d₁, hence d₁ · nml ε = -d₁ ε log ε ≥ 3ε
  have hlog : Real.log ε ≤ -(3 / dOne x) := by
    have h := Real.log_le_log hε0 (min_le_right (1 / 3) (Real.exp (-(3 / dOne x))))
    rwa [Real.log_exp] at h
  have hkey : 3 * ε ≤ dOne x * Real.negMulLog ε := by
    simp only [Real.negMulLog, neg_mul]
    have hmul : dOne x * (ε * Real.log ε) ≤ dOne x * (ε * -(3 / dOne x)) := by
      apply mul_le_mul_of_nonneg_left _ hd.le
      exact mul_le_mul_of_nonneg_left hlog hε0.le
    have hval : dOne x * (ε * -(3 / dOne x)) = -(3 * ε) := by
      field_simp
    rw [hval] at hmul
    linarith
  linarith

end WHGAP.Support

