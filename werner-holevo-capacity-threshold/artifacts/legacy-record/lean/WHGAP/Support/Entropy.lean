import WHGAP.Support.Basic
import Mathlib.Analysis.Matrix.Spectrum
import Mathlib.Analysis.SpecialFunctions.Log.NegMulLog

/-!
# WHGAP minimal von Neumann entropy layer (DAG protocol §7.3 support module, tier **T3**)

Serves the node module `WHGAP.«private-boundary»` (P14), where it discharges paper
**Lemma 7.1** (`lem:holevo`, `paper/main.tex` §7); it is also the natural home for the
B/E-side spectrum bridge that `WHGAP.Support.IcScalar` (P9) currently leaves in prose
(LEAN-2 WP-B report item 11).

**T3 authorization.**  DAG protocol §7.8 forbids starting a T3 (library-infrastructure)
layer without a lead directive.  The directive is quoted verbatim in the commission
`channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_LEAN2_20260731.md` (lead,
2026-07-31).

## SCOPE — read this before using `vnEntropy` anywhere

`vnEntropy` here is defined **only for real symmetric matrices**, as
`∑ i, Real.negMulLog (eigenvalue i)` with `Real.negMulLog y = -y log y` (natural log ⇒ nats).

* **Complex-Hermitian generality is NOT claimed.**  Nothing below is stated for
  `Matrix n n ℂ`.  The paper's output matrices at the §7 witness are *real* symmetric in the
  frame used here (this is checked, not assumed: `tools/whgap_lean2_wpc_check.py` gate G1
  rebuilds `Λ_x` and `Λ^c_x` from the Kraus operators and matches them entry by entry
  against the explicit matrices below).
* **This is not "the von Neumann entropy of a state".**  There is no positivity, no
  normalization and no density-matrix structure in the definition: `vnEntropy` is a number
  attached to a symmetric matrix.  `Real.negMulLog` is `0` at `0` and *negative* for
  arguments `> 1`, so for a non-state the value has no information-theoretic reading.
  Every theorem below is an algebraic identity between such numbers.
* **No channel exists in this development.**  The matrices are *defined* by the displays of
  paper Lemma 7.1 / Theorem 5.2; that those displays are the channel outputs is the sympy
  gate cited above, not Lean.

**Append-only note, 2026-08-01 (LEAN-5 WP-H).**  The complex-Hermitian layer now exists, in
the sibling module `WHGAP/Support/EntropyC.lean` (`vnEntropyC`, `eigenvaluesC_multiset_eq`,
`vnEntropyC_eq_sum_of_charpoly(_list)`), where it discharges `Trust.lean` residual (b) for
the §6 witness.  The "Complex-Hermitian generality is NOT claimed" sentence above **stays**:
it is the accurate record of what THIS module claims, and nothing here was restated over
`ℂ`.  The two layers are siblings — the P14 payoff chain below still runs through the real
one — and `EntropyC` imports this module, not the other way round.

## Contents

1. `vnEntropy` — the definition.
2. `vnEntropy_eq_sum_of_charpoly` — the workhorse: if `charpoly A = ∏ (X - C dᵢ)` then the
   entropy is `∑ negMulLog dᵢ`.  Everything else is a corollary.
   (a) `vnEntropy_diagonal` — an explicit diagonal matrix.
   (b) `vnEntropy_conj_orthogonal` / `vnEntropy_of_conj_diagonal` — invariance under
       conjugation.
   (c) `vnEntropy_fromBlocks_add` — block-diagonal additivity, plus the explicit `2 ⊕ 2`
       corollary `vnEntropy_two_by_two_blocks`.
3. `two_point_collapse` — the scalar identity behind Lemma 7.1's `χ = b f(u/b)`.
-/

namespace WHGAP.Support

open Matrix Polynomial

section General

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- **von Neumann entropy of a real symmetric matrix**, in nats:
`S(A) = ∑ᵢ negMulLog λᵢ(A) = -∑ᵢ λᵢ log λᵢ`, with `λ` the `Matrix.IsHermitian.eigenvalues`
of the supplied symmetry proof.  Real-symmetric scope only — see the module header. -/
noncomputable def vnEntropy {A : Matrix n n ℝ} (hA : A.IsHermitian) : ℝ :=
  ∑ i, Real.negMulLog (hA.eigenvalues i)

omit [Fintype n] [DecidableEq n] in
/-- A real matrix is `IsHermitian` exactly when it is symmetric. -/
theorem isHermitian_of_transpose {A : Matrix n n ℝ} (h : Aᵀ = A) : A.IsHermitian := by
  ext i j
  have : Aᵀ i j = A i j := by rw [h]
  simpa [Matrix.conjTranspose_apply, Matrix.transpose_apply] using this

/-- The eigenvalue *multiset* of a symmetric matrix whose characteristic polynomial is
presented in split form `∏ (X - C dᵢ)` is `d` itself.  This is the only place where the
`Matrix.IsHermitian.eigenvalues` indexing (an arbitrary sorted enumeration) is compared with
an explicitly given list; every later statement is order-free because it only ever sums a
function over the multiset. -/
theorem eigenvalues_multiset_eq {A : Matrix n n ℝ} (hA : A.IsHermitian) (d : n → ℝ)
    (h : A.charpoly = ∏ i, (X - C (d i))) :
    Multiset.map hA.eigenvalues Finset.univ.val = Multiset.map d Finset.univ.val := by
  have h1 : A.charpoly.roots = Multiset.map (RCLike.ofReal ∘ hA.eigenvalues) Finset.univ.val :=
    hA.roots_charpoly_eq_eigenvalues
  rw [RCLike.ofReal_real_eq_id, Function.id_comp] at h1
  have hmap : (fun i : n => (X - C (d i) : ℝ[X])) = (fun a : ℝ => X - C a) ∘ d := rfl
  have h2 : A.charpoly.roots = Multiset.map d Finset.univ.val := by
    rw [h, Finset.prod_eq_multiset_prod, hmap, ← Multiset.map_map,
      Polynomial.roots_multiset_prod_X_sub_C]
  rw [← h1, h2]

/-- **Workhorse.**  If the characteristic polynomial of a symmetric `A` splits as
`∏ᵢ (X - C dᵢ)` then `S(A) = ∑ᵢ negMulLog dᵢ`. -/
theorem vnEntropy_eq_sum_of_charpoly {A : Matrix n n ℝ} (hA : A.IsHermitian) (d : n → ℝ)
    (h : A.charpoly = ∏ i, (X - C (d i))) :
    vnEntropy hA = ∑ i, Real.negMulLog (d i) := by
  have hm := eigenvalues_multiset_eq hA d h
  have e1 : (fun i : n => Real.negMulLog (hA.eigenvalues i))
      = Real.negMulLog ∘ hA.eigenvalues := rfl
  have e2 : (fun i : n => Real.negMulLog (d i)) = Real.negMulLog ∘ d := rfl
  unfold vnEntropy
  rw [Finset.sum_eq_multiset_sum, Finset.sum_eq_multiset_sum, e1, e2,
    ← Multiset.map_map, ← Multiset.map_map, hm]

/-! ### (a) the diagonal case -/

/-- **(a)** The entropy of an explicit diagonal matrix is `∑ negMulLog` of its diagonal —
i.e. the eigenvalues of `diagonal d` are `d` as a multiset. -/
theorem vnEntropy_diagonal (d : n → ℝ) (hd : (Matrix.diagonal d).IsHermitian) :
    vnEntropy hd = ∑ i, Real.negMulLog (d i) :=
  vnEntropy_eq_sum_of_charpoly hd d (Matrix.charpoly_diagonal d)

/-! ### (b) invariance under conjugation -/

/-- Similarity invariance of the characteristic polynomial, in the weakest form we need:
a *one-sided* inverse `V * U = 1` suffices (`U` need not be orthogonal).  Route: Mathlib's
`Matrix.charpoly_mul_comm`. -/
theorem charpoly_conj (U V D : Matrix n n ℝ) (h : V * U = 1) :
    (U * D * V).charpoly = D.charpoly := by
  rw [Matrix.charpoly_mul_comm, ← Matrix.mul_assoc, h, Matrix.one_mul]

/-- Two symmetric matrices with the same characteristic polynomial have the same entropy. -/
theorem vnEntropy_congr_charpoly {A B : Matrix n n ℝ} (hA : A.IsHermitian) (hB : B.IsHermitian)
    (h : A.charpoly = B.charpoly) : vnEntropy hA = vnEntropy hB := by
  unfold vnEntropy
  rw [(hA.eigenvalues_eq_eigenvalues_iff hB).mpr h]

/-- **(b)** Invariance of the entropy under **orthogonal** conjugation, exactly as
commissioned: `U Uᵀ = 1 ⟹ S(U D Uᵀ) = S(D)`. -/
theorem vnEntropy_conj_orthogonal {U D : Matrix n n ℝ} (hU : U * Uᵀ = 1)
    (hD : D.IsHermitian) (hA : (U * D * Uᵀ).IsHermitian) :
    vnEntropy hA = vnEntropy hD := by
  refine vnEntropy_congr_charpoly hA hD ?_
  exact charpoly_conj U Uᵀ D (mul_eq_one_comm.mp hU)

/-- **(b′)** The form actually used by the payoff: if `A` is a rational similarity transform
of an explicit diagonal matrix, its entropy is the `negMulLog` sum of that diagonal.  Only
`V * U = 1` is required, so no square roots ever enter the certificates. -/
theorem vnEntropy_of_conj_diagonal {A U V : Matrix n n ℝ} (hA : A.IsHermitian) (d : n → ℝ)
    (hUV : V * U = 1) (hconj : U * Matrix.diagonal d * V = A) :
    vnEntropy hA = ∑ i, Real.negMulLog (d i) := by
  refine vnEntropy_eq_sum_of_charpoly hA d ?_
  rw [← hconj, charpoly_conj U V _ hUV, Matrix.charpoly_diagonal]

end General

/-! ### explicit small diagonal matrices in `!![…]` form

`Matrix.diagonal` does not reduce under the `!![…]`/`vecHead` simp set, so every explicit
certificate below is stated with literal matrices and converted here once and for all. -/

theorem diagonal_fin_two (a b : ℝ) :
    (Matrix.diagonal ![a, b] : Matrix (Fin 2) (Fin 2) ℝ) = !![a, 0; 0, b] := by
  ext i j; fin_cases i <;> fin_cases j <;> simp

theorem diagonal_fin_three (a b c : ℝ) :
    (Matrix.diagonal ![a, b, c] : Matrix (Fin 3) (Fin 3) ℝ) = !![a, 0, 0; 0, b, 0; 0, 0, c] := by
  ext i j; fin_cases i <;> fin_cases j <;> simp

theorem diagonal_fin_four (a b c d : ℝ) :
    (Matrix.diagonal ![a, b, c, d] : Matrix (Fin 4) (Fin 4) ℝ)
      = !![a, 0, 0, 0; 0, b, 0, 0; 0, 0, c, 0; 0, 0, 0, d] := by
  ext i j; fin_cases i <;> fin_cases j <;> simp

/-! ### (c) block-diagonal additivity -/

section Blocks

variable {m k : Type*} [Fintype m] [DecidableEq m] [Fintype k] [DecidableEq k]

/-- **(c)** Block-diagonal additivity: the entropy of `A ⊕ D` is `S(A) + S(D)`, provided both
blocks' characteristic polynomials are presented in split form. -/
theorem vnEntropy_fromBlocks_add {A : Matrix m m ℝ} {D : Matrix k k ℝ}
    (hAD : (Matrix.fromBlocks A 0 0 D).IsHermitian) (dA : m → ℝ) (dD : k → ℝ)
    (hA : A.charpoly = ∏ i, (X - C (dA i))) (hD : D.charpoly = ∏ i, (X - C (dD i))) :
    vnEntropy hAD = (∑ i, Real.negMulLog (dA i)) + ∑ i, Real.negMulLog (dD i) := by
  have hsplit : (Matrix.fromBlocks A 0 0 D).charpoly
      = ∏ i : m ⊕ k, (X - C (Sum.elim dA dD i)) := by
    rw [Matrix.charpoly_fromBlocks_zero₁₂, hA, hD, Fintype.prod_sum_type]
    rfl
  rw [vnEntropy_eq_sum_of_charpoly hAD (Sum.elim dA dD) hsplit, Fintype.sum_sum_type]
  rfl

/-- The commissioned explicit `2 ⊕ 2` instance of (c): a block-diagonal matrix whose two
`2×2` blocks are `!![a, 0; 0, c]` and `!![e, w; w, e]` has entropy
`negMulLog a + negMulLog c + negMulLog (e+w) + negMulLog (e-w)`.  This is precisely the
shape of the §7 environment output `Λ^c_x(ρ_ε ± tX)`. -/
theorem vnEntropy_two_by_two_blocks (a c e w : ℝ)
    (hAD : (Matrix.fromBlocks (!![a, 0; 0, c] : Matrix (Fin 2) (Fin 2) ℝ) 0 0
      (!![e, w; w, e] : Matrix (Fin 2) (Fin 2) ℝ)).IsHermitian) :
    vnEntropy hAD = (Real.negMulLog a + Real.negMulLog c)
      + (Real.negMulLog (e + w) + Real.negMulLog (e - w)) := by
  have h1 : (!![a, 0; 0, c] : Matrix (Fin 2) (Fin 2) ℝ).charpoly
      = ∏ i, (X - C (![a, c] i)) := by
    rw [← diagonal_fin_two a c]
    exact Matrix.charpoly_diagonal _
  have h2 : (!![e, w; w, e] : Matrix (Fin 2) (Fin 2) ℝ).charpoly
      = ∏ i, (X - C (![e + w, e - w] i)) := by
    have hUV : (!![1/2, 1/2; 1/2, -1/2] : Matrix (Fin 2) (Fin 2) ℝ) * !![1, 1; 1, -1] = 1 := by
      ext i j; fin_cases i <;> fin_cases j <;> norm_num [Matrix.mul_apply, Fin.sum_univ_two]
    have hconj : (!![1, 1; 1, -1] : Matrix (Fin 2) (Fin 2) ℝ) * Matrix.diagonal ![e + w, e - w]
        * !![1/2, 1/2; 1/2, -1/2] = !![e, w; w, e] := by
      rw [diagonal_fin_two]
      ext i j
      fin_cases i <;> fin_cases j <;>
        simp [Matrix.mul_apply, Fin.sum_univ_two] <;> ring
    rw [← hconj, charpoly_conj _ _ _ hUV, Matrix.charpoly_diagonal]
  rw [vnEntropy_fromBlocks_add hAD ![a, c] ![e + w, e - w] h1 h2]
  simp [Fin.sum_univ_two]

end Blocks

/-! ### the scalar collapse behind paper Lemma 7.1 -/

/-- **`two_point_collapse`.**  The entropy bookkeeping of a symmetric two-point ensemble whose
outputs commute and differ from the average only inside one degenerate `2×2` block:

`2 negMulLog b - negMulLog (b+u) - negMulLog (b-u) = b · f(u/b)`,

with `f s = (1+s) log(1+s) + (1-s) log(1-s)` the binary Holevo function of
`WHGAP.Support.f`.  This is the "for commuting arguments … the α-eigenvalue contributes 0"
computation of the proof of paper Lemma 7.1, isolated as a scalar identity. -/
theorem two_point_collapse {b u : ℝ} (hb : b ≠ 0) (hp : b + u ≠ 0) (hm : b - u ≠ 0) :
    2 * Real.negMulLog b - Real.negMulLog (b + u) - Real.negMulLog (b - u) = b * f (u / b) := by
  have h1 : 1 + u / b = (b + u) / b := by field_simp
  have h2 : 1 - u / b = (b - u) / b := by field_simp
  have l1 : Real.log ((b + u) / b) = Real.log (b + u) - Real.log b := Real.log_div hp hb
  have l2 : Real.log ((b - u) / b) = Real.log (b - u) - Real.log b := Real.log_div hm hb
  unfold f
  rw [h1, h2, l1, l2]
  simp only [Real.negMulLog]
  field_simp
  ring

end WHGAP.Support

