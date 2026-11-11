import WHGAP.Support.Entropy
import WHGAP.Support.Channel

/-!
# WHGAP complex-Hermitian entropy layer (DAG protocol §7.3 support module, tier **T3**)

Commissioned by
`channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_LEAN5_P15B_20260801.md`,
Track H (LEAN-5 WP-H).  This module closes the last *named* Lean residue of `Trust.lean`:
residual **(b)**, "same characteristic polynomial ⟹ same von Neumann entropy" over `ℂ`.

`WHGAP.Support.Entropy` defines `vnEntropy` for **real symmetric** matrices only, and its
module header says so.  The §6 witness outputs of `WHGAP.Support.Channel` §8 are genuinely
complex Hermitian, so that layer does not apply to them.  Here the same construction is
re-run over `ℂ` — `Matrix.IsHermitian.eigenvalues` is `RCLike`-generic in Mathlib, so the
definition has the identical shape — and the two `LEAN-4 WP-G` charpolys are turned into
the entropy statement they were written for.

## SCOPE — what this module does and does not claim

* `vnEntropyC hA = ∑ i, Real.negMulLog (hA.eigenvalues i)` is the **von Neumann entropy in
  nats** of the Hermitian eigenvalue enumeration.  As in the real layer, there is **no
  positivity, no normalization and no density-matrix structure** in the definition:
  `Real.negMulLog` is `0` at `0` and negative above `1`, so for a non-state the number has
  no information-theoretic reading.  Every statement below is an algebraic identity.
* The eigenvalue *enumeration* is Mathlib's arbitrary (antitone) one.  Nothing here sorts,
  separates or names individual eigenvalues: the bridge is at the level of the eigenvalue
  **multiset**, so repeated eigenvalues are handled with no side condition.  (Pre-verified:
  gate GH2c exhibits a genuinely degenerate point, `ε = 1/2`, where the identity still
  holds.)
* **What is still NOT in Lean after this module** (unchanged by it): that `LamCK` is *the*
  complementary channel of `Lam` (no complete positivity, no Stinespring dilation in this
  development), and the coding theorems — `IcLB`/`lsd_devetak`/`q_pos_of_ic_pos` remain
  interface fields.  See `WHGAP/Trust.lean`, section 2026-08-01 (LEAN-5 WP-H).

## Contents

1. `vnEntropyC` — the definition.
2. `charpolyC_roots_of_prod`, `eigenvaluesC_multiset_of_roots`,
   `eigenvaluesC_multiset_eq(_list)` — the multiset bridge.  The `ofReal` layer is stripped
   with `Complex.ofReal_injective` (the real layer instead rewrites with
   `RCLike.ofReal_real_eq_id`, which is unavailable over `ℂ`).
3. `vnEntropyC_eq_sum_of_charpoly` and `vnEntropyC_eq_sum_of_charpoly_list` — the workhorse
   in the two shapes; `charpolyC_list_length` records that the list form is not vacuous.
4. `IcScalar_eq_vnEntropyC_diff` — **the payoff**: the scalar `IcScalar x ε` of
   `WHGAP.Support.IcScalar` IS `S(Λ_x(ρ_ε)) − S(Λ^c_x(ρ_ε))` for the Kraus-built §6 witness
   outputs.
-/

namespace WHGAP.Support

open Matrix Polynomial

section General

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- **von Neumann entropy of a complex Hermitian matrix**, in nats:
`S(A) = ∑ᵢ negMulLog λᵢ(A) = -∑ᵢ λᵢ log λᵢ`, with `λ` the `Matrix.IsHermitian.eigenvalues`
of the supplied Hermiticity proof (a real-valued function — Mathlib's `eigenvalues` is
`RCLike`-generic and lands in `ℝ`).  Same definition shape as the real-symmetric
`WHGAP.Support.vnEntropy`; see the module header for the scope. -/
noncomputable def vnEntropyC {A : Matrix n n ℂ} (hA : A.IsHermitian) : ℝ :=
  ∑ i, Real.negMulLog (hA.eigenvalues i)

/-- The roots of a product `∏ (X − C ↑aᵢ)` over a multiset of REAL numbers are those reals,
cast to `ℂ`. -/
theorem charpolyC_roots_of_prod (m : Multiset ℝ) :
    ((m.map (fun a : ℝ => X - C ((a : ℂ)))).prod).roots
      = m.map (fun a : ℝ => ((a : ℂ))) := by
  have hcomp : (fun a : ℝ => (X - C ((a : ℂ)) : ℂ[X]))
      = (fun z : ℂ => X - C z) ∘ (fun a : ℝ => ((a : ℂ))) := rfl
  rw [hcomp, ← Multiset.map_map, Polynomial.roots_multiset_prod_X_sub_C]

/-- If the charpoly roots of a Hermitian complex matrix are the `ℂ`-image of a real multiset
`m`, then the eigenvalue multiset **is** `m`.  This is the complex analogue of
`WHGAP.Support.eigenvalues_multiset_eq`; the only difference is the last step, where the
real proof rewrites `RCLike.ofReal_real_eq_id` and here the `ofReal` layer is stripped by
injectivity instead. -/
theorem eigenvaluesC_multiset_of_roots {A : Matrix n n ℂ} (hA : A.IsHermitian) (m : Multiset ℝ)
    (h : A.charpoly.roots = m.map (fun a : ℝ => ((a : ℂ)))) :
    Multiset.map hA.eigenvalues Finset.univ.val = m := by
  have h1 : A.charpoly.roots
      = Multiset.map (fun a : ℝ => ((a : ℂ)))
          (Multiset.map hA.eigenvalues Finset.univ.val) := by
    rw [Multiset.map_map]
    exact hA.roots_charpoly_eq_eigenvalues
  exact Multiset.map_injective Complex.ofReal_injective (h1.symm.trans h)

/-- Multiset form of the eigenvalue bridge, from a split charpoly. -/
theorem eigenvaluesC_multiset_eq_multiset {A : Matrix n n ℂ} (hA : A.IsHermitian) (m : Multiset ℝ)
    (h : A.charpoly = (m.map (fun a : ℝ => X - C ((a : ℂ)))).prod) :
    Multiset.map hA.eigenvalues Finset.univ.val = m :=
  eigenvaluesC_multiset_of_roots hA m (by rw [h, charpolyC_roots_of_prod])

/-- **`eigenvaluesC_multiset_eq`.**  If the characteristic polynomial of a complex Hermitian
`A` splits as `∏ᵢ (X − C ↑dᵢ)` over a REAL vector `d`, the eigenvalue multiset is the `d`
multiset.  No ordering is asserted anywhere. -/
theorem eigenvaluesC_multiset_eq {A : Matrix n n ℂ} (hA : A.IsHermitian) (d : n → ℝ)
    (h : A.charpoly = ∏ i, (X - C ((d i : ℂ)))) :
    Multiset.map hA.eigenvalues Finset.univ.val = Multiset.map d Finset.univ.val := by
  refine eigenvaluesC_multiset_eq_multiset hA (Multiset.map d Finset.univ.val) ?_
  rw [h, Finset.prod_eq_multiset_prod, Multiset.map_map]
  rfl

/-- **Workhorse (Fin-indexed).**  A complex Hermitian matrix whose charpoly splits over a
real vector `d` has entropy `∑ᵢ negMulLog dᵢ`. -/
theorem vnEntropyC_eq_sum_of_charpoly {A : Matrix n n ℂ} (hA : A.IsHermitian) (d : n → ℝ)
    (h : A.charpoly = ∏ i, (X - C ((d i : ℂ)))) :
    vnEntropyC hA = ∑ i, Real.negMulLog (d i) := by
  have hm := eigenvaluesC_multiset_eq hA d h
  have e1 : (fun i : n => Real.negMulLog (hA.eigenvalues i))
      = Real.negMulLog ∘ hA.eigenvalues := rfl
  have e2 : (fun i : n => Real.negMulLog (d i)) = Real.negMulLog ∘ d := rfl
  unfold vnEntropyC
  rw [Finset.sum_eq_multiset_sum, Finset.sum_eq_multiset_sum, e1, e2,
    ← Multiset.map_map, ← Multiset.map_map, hm]

/-- **Workhorse (list form).**  Exactly the shape produced by `LEAN-4 WP-G`
(`Channel.specB_charpoly_list`, `Channel.specE_charpoly_list`):
`A.charpoly = (l.map (fun a : ℝ => X − C ↑a)).prod ⟹ S(A) = (l.map negMulLog).sum`. -/
theorem vnEntropyC_eq_sum_of_charpoly_list {A : Matrix n n ℂ} (hA : A.IsHermitian) (l : List ℝ)
    (h : A.charpoly = ((l.map fun a : ℝ => X - C ((a : ℂ))).prod)) :
    vnEntropyC hA = (l.map Real.negMulLog).sum := by
  have hmul : A.charpoly = (((l : Multiset ℝ).map fun a : ℝ => X - C ((a : ℂ))).prod) := by
    rw [h, Multiset.map_coe, Multiset.prod_coe]
  have hm := eigenvaluesC_multiset_eq_multiset hA (l : Multiset ℝ) hmul
  have e1 : (fun i : n => Real.negMulLog (hA.eigenvalues i))
      = Real.negMulLog ∘ hA.eigenvalues := rfl
  unfold vnEntropyC
  rw [Finset.sum_eq_multiset_sum, e1, ← Multiset.map_map, hm]
  rw [Multiset.map_coe]
  rfl

/-- **Length forcing for the list form** (a NECESSARY condition on the hypothesis): a list
satisfying the hypothesis of `vnEntropyC_eq_sum_of_charpoly_list` necessarily has length
`Fintype.card n`, so the hypothesis is not satisfiable by a mismatched list — and the length
fact needs no separate assumption.

*Headline corrected 2026-08-01 per R15 m4* (it previously read "Non-vacuity of the list form
(DAG §7.10.5)", which overreached): this theorem EXCLUDES bad lists, it does not exhibit a
good one, so it is not by itself a §7.10.5 satisfiability statement.  Genuine non-vacuity is
witnessed by the payoff below, which applies `vnEntropyC_eq_sum_of_charpoly_list` at both
arities — `specB` (3 reals, `Matrix (Fin 3) (Fin 3) ℂ`) and `specE` (4 reals,
`Matrix (Fin 4) (Fin 4) ℂ`) — and, at the interface level, by `WHGAP/Model.lean` §3c. -/
theorem charpolyC_list_length {A : Matrix n n ℂ} (hA : A.IsHermitian) (l : List ℝ)
    (h : A.charpoly = ((l.map fun a : ℝ => X - C ((a : ℂ))).prod)) :
    l.length = Fintype.card n := by
  have hmul : A.charpoly = (((l : Multiset ℝ).map fun a : ℝ => X - C ((a : ℂ))).prod) := by
    rw [h, Multiset.map_coe, Multiset.prod_coe]
  have hm := eigenvaluesC_multiset_eq_multiset hA (l : Multiset ℝ) hmul
  have := congrArg Multiset.card hm
  simpa [Finset.card_univ] using this.symm

/-- Two complex Hermitian matrices with the same characteristic polynomial have the same
entropy (the complex analogue of `vnEntropy_congr_charpoly`; Mathlib's
`eigenvalues_eq_eigenvalues_iff` is already `RCLike`-generic). -/
theorem vnEntropyC_congr_charpoly {A B : Matrix n n ℂ} (hA : A.IsHermitian) (hB : B.IsHermitian)
    (h : A.charpoly = B.charpoly) : vnEntropyC hA = vnEntropyC hB := by
  unfold vnEntropyC
  rw [(hA.eigenvalues_eq_eigenvalues_iff hB).mpr h]

end General

/-! ## The payoff: `IcScalar` IS an entropy difference of the Kraus-built §6 outputs -/

/-- **`IcScalar_eq_vnEntropyC_diff`.**  For real parameters on the physical domain
`0 ≤ x ≤ 1`, with `β` any square root of `x(1−x)/2`:

`IcScalar x ε = S(Λ_x(ρ_ε)) − S(Λ^c_x(ρ_ε))`,

where both entropies are von Neumann entropies (nats) of the COMPLEX Hermitian outputs
built in `WHGAP.Support.Channel` §8 and `IcScalar` is the scalar of
`WHGAP.Support.IcScalar`, defined as a `Real.negMulLog` sum over the two explicit
eigenvalue lists `specB`, `specE`.

This is exactly the passage that `Trust.lean` listed as residual (b)'s remaining glue:
"same characteristic polynomial ⟹ same `vnEntropy`, over `ℂ`".  The hypotheses are only
the ones the WP-G list lemmas carry.

*Scope, unchanged by this theorem:* `Λ^c` here is `LamC`, the `eq:comp` block form that
`Channel.LamCK_eq` identifies with the matrix of Kraus overlaps `Tr(K_a X K_bᵀ)`.  That
this map is *the* complementary channel is a Stinespring statement and remains outside
Lean. -/
theorem IcScalar_eq_vnEntropyC_diff {x : ℝ} (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (ε β : ℝ)
    (hβ : β ^ 2 = x * (1 - x) / 2) :
    IcScalar x ε
      = vnEntropyC (Channel.LamWit_isHermitian x ε)
        - vnEntropyC (Channel.LamCWit_isHermitian x ε β) := by
  have hB : vnEntropyC (Channel.LamWit_isHermitian x ε)
      = ((specB x ε).map Real.negMulLog).sum :=
    vnEntropyC_eq_sum_of_charpoly_list _ _ (Channel.specB_charpoly_list x ε)
  have hE : vnEntropyC (Channel.LamCWit_isHermitian x ε β)
      = ((specE x ε).map Real.negMulLog).sum :=
    vnEntropyC_eq_sum_of_charpoly_list _ _ (Channel.specE_charpoly_list hx0 hx1 ε β hβ)
  rw [hB, hE, IcScalar]

end WHGAP.Support

