/-
# Tier-3 (`KSUM.LEAN.T3.obstruction-theorems`) — shared finite substrate

This module carries ONLY the finite-linear-algebra vocabulary that the obstruction theorems of
`ksum/paper/ksum_small_alphabet.tex` §`sec:proof-search` are stated in:

  * `l1`      — the ℓ¹ norm of a signed measure on a finite configuration space,
  * `total`   — its total mass,
  * `signF`   — the ±1 indicator `F = 2·[YES] - 1` of the paper (`F = -1` on NO, `+1` on YES),
  * `corr`    — the pairing `⟨μ, F⟩`,
  * `ffMoment`/`PureHighDegree` — the falling-factorial occupancy moments of
    equation (38) and the paper's "pure high degree at least d".

There is deliberately NO quantum content and NO `QueryModel` interface anywhere in Tier 3:
every theorem downstream of this file is unconditional.

House rules (see `ksum/lean/README.md`): no `sorry`, no `axiom`.

Audit status: **ADOPTED 2026-07-30** by the T3 audit
(`ksum/artifacts/ksum_lean_T3_obstructions_20260730.md`).  This module states no paper theorem; it is
the shared vocabulary, and the audit's verdict on it is a definitional one (do the definitions
denote the paper's objects?), recorded in §2 of that artifact.
-/
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Data.Fintype.Pi
import Mathlib.Data.Nat.Choose.Vandermonde
import Mathlib.Tactic

namespace KsumAudit.Obstructions

open Finset

-- Section variables are carried on the simp lemmas below for uniformity of the API even where a
-- particular lemma does not use them.
set_option linter.unusedSectionVars false

/-! ## Signed measures on a finite configuration space -/

section Norms

variable {X : Type*} [Fintype X]

/-- ℓ¹ norm of a signed measure on a finite configuration space. -/
def l1 (μ : X → ℚ) : ℚ := ∑ x, |μ x|

/-- Total mass of a signed measure. -/
def total (μ : X → ℚ) : ℚ := ∑ x, μ x

/-- `F = 2·[YES] - 1`: the paper's `F_{N,q,t} ∈ {-1,+1}`, written against an explicit
NO-predicate.  `F = -1` exactly on NO. -/
def signF (no : X → Prop) [DecidablePred no] (x : X) : ℚ := if no x then -1 else 1

/-- The correlation `⟨μ, F⟩` of the paper. -/
def corr (no : X → Prop) [DecidablePred no] (μ : X → ℚ) : ℚ := ∑ x, μ x * signF no x

lemma l1_nonneg (μ : X → ℚ) : 0 ≤ l1 μ := Finset.sum_nonneg fun _ _ => abs_nonneg _

/-- `⟨μ,F⟩ = (total mass) - 2·(mass on NO)`.  This is the identity the obstruction proofs use. -/
lemma corr_eq_total_sub (no : X → Prop) [DecidablePred no] (μ : X → ℚ) :
    corr no μ = total μ - 2 * ∑ x ∈ univ.filter no, μ x := by
  have h : ∀ x : X, μ x * signF no x = μ x - 2 * (if no x then μ x else 0) := by
    intro x; simp only [signF]; split <;> ring
  simp only [corr, h, total]
  rw [Finset.sum_sub_distrib, ← Finset.mul_sum, Finset.sum_filter]

/-- When the total mass vanishes, `⟨μ,F⟩` is exactly `-2` times the NO mass. -/
lemma corr_of_total_zero (no : X → Prop) [DecidablePred no] (μ : X → ℚ)
    (h0 : total μ = 0) :
    corr no μ = -2 * ∑ x ∈ univ.filter no, μ x := by
  rw [corr_eq_total_sub, h0]; ring

end Norms

/-! ## Falling-factorial occupancy moments

`A` is the alphabet.  An *occupancy vector* is a function `A → ℕ`.  Equation (38) of the paper
pairs a signed measure supported on a finite set of occupancy vectors against the
falling-factorial rows `∏_a (n_a)_{α_a}`. -/

section Moments

variable {A : Type*} [Fintype A] [DecidableEq A]

/-- The falling-factorial row `∏_a (n_a)_{α_a}` evaluated at an occupancy vector `n`. -/
def ffRow (α : A → ℕ) (n : A → ℕ) : ℚ := ∏ a, ((n a).descFactorial (α a) : ℚ)

/-- The order `|α|` of a falling-factorial row. -/
def rowOrder (α : A → ℕ) : ℕ := ∑ a, α a

/-- The falling-factorial moment `M_μ(α) = ∑_n μ(n) ∏_a (n_a)_{α_a}` of equation (38),
for a measure carried by the finite index set `S` of occupancy vectors. -/
def ffMoment {ι : Type*} (S : Finset ι) (occ : ι → A → ℕ) (μ : ι → ℚ) (α : A → ℕ) : ℚ :=
  ∑ i ∈ S, μ i * ffRow α (occ i)

/-- "`μ` has pure high degree at least `d`": every falling-factorial row of order `< d` is
annihilated.  This is the paper's own phrase, resolved to equation (38). -/
def PureHighDegree {ι : Type*} (S : Finset ι) (occ : ι → A → ℕ) (μ : ι → ℚ) (d : ℕ) : Prop :=
  ∀ α : A → ℕ, rowOrder α < d → ffMoment S occ μ α = 0

/-- The degree-zero row is the constant `1`. -/
@[simp] lemma ffRow_zero (n : A → ℕ) : ffRow (fun _ => 0) n = 1 := by
  simp [ffRow]

lemma rowOrder_zero : rowOrder (fun _ : A => 0) = 0 := by simp [rowOrder]

/-- A nonnegative measure of total mass one has pure high degree `0` and no more:
its degree-zero moment is `1 ≠ 0`.  (This is the analytic content of transfer fact G3.) -/
lemma not_pureHighDegree_succ_of_moment_zero_ne_zero
    {ι : Type*} (S : Finset ι) (occ : ι → A → ℕ) (μ : ι → ℚ)
    (h : ffMoment S occ μ (fun _ => 0) ≠ 0) (d : ℕ) :
    ¬ PureHighDegree S occ μ (d + 1) := by
  intro hd
  exact h (hd (fun _ => 0) (by simp [rowOrder]))

end Moments

end KsumAudit.Obstructions
