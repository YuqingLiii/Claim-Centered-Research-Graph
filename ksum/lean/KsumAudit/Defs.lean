/-
Definitions for the machine-checked audit of

  `ksum/paper/ksum_small_alphabet.tex`

Proof-DAG node: `KSUM.LEAN.T1.k2-main-line` (registered OPEN under rule 8a, 2026-07-30).

This file contains ONLY definitions and their elementary characterizations.  It deliberately
mentions no query-complexity interface: everything here is finite combinatorics that the kernel
checks unconditionally.

House rule (see `ksum/lean/README.md`): no hypothesis of a paper theorem may be hidden
inside a definition.  In particular `E` (the encoding, `encode` below) is defined for *every*
`q` and `κ`; the paper's hypothesis `q ≥ 2κ+1` appears only in the hypotheses of `lem:encode`.
-/
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Fin.Tuple.Basic
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Combinatorics.Pigeonhole

namespace KsumAudit

/-! ## The problems (`sec:prelim`, paragraph "Problems") -/

/-- `kSum_{G,t,N}(x) = 1` iff some `k`-subset of the positions has values summing to `t`.
LaTeX: `sec:prelim`, the display defining `\kSum`. -/
def kSum (G : Type*) [AddCommMonoid G] [DecidableEq G] (k : ℕ) (t : G) (N : ℕ) :
    (Fin N → G) → Bool :=
  fun x => decide (∃ S : Finset (Fin N), S.card = k ∧ ∑ i ∈ S, x i = t)

/-- `2Sum_{G,t,N}`, the `k = 2` specialization of `kSum`. -/
def twoSum (G : Type*) [AddCommMonoid G] [DecidableEq G] (t : G) (N : ℕ) :
    (Fin N → G) → Bool :=
  kSum G 2 t N

/-- The `k = 2` case unfolded: a hit is a pair of **distinct** positions whose values sum to `t`. -/
theorem twoSum_eq_decide {G : Type*} [AddCommMonoid G] [DecidableEq G] (t : G) (N : ℕ)
    (x : Fin N → G) :
    twoSum G t N x = decide (∃ i j : Fin N, i ≠ j ∧ x i + x j = t) := by
  rw [twoSum, kSum]
  refine decide_eq_decide.mpr ⟨?_, ?_⟩
  · rintro ⟨S, hcard, hsum⟩
    obtain ⟨a, b, hab, rfl⟩ := Finset.card_eq_two.mp hcard
    exact ⟨a, b, hab, by rwa [Finset.sum_pair hab] at hsum⟩
  · rintro ⟨i, j, hij, hsum⟩
    exact ⟨{i, j}, Finset.card_eq_two.mpr ⟨i, j, hij, rfl⟩, by rwa [Finset.sum_pair hij]⟩

theorem twoSum_iff {G : Type*} [AddCommMonoid G] [DecidableEq G] (t : G) (N : ℕ)
    (x : Fin N → G) :
    twoSum G t N x = true ↔ ∃ i j : Fin N, i ≠ j ∧ x i + x j = t := by
  rw [twoSum_eq_decide, decide_eq_true_eq]

/-! ## The two halves of a length-`2n` string -/

/-- Position `i` of the first half, as a position of a length-`2n` string. -/
def lo (n : ℕ) (i : Fin n) : Fin (2 * n) := ⟨(i : ℕ), by have := i.isLt; omega⟩

/-- Position `j` of the second half, as a position of a length-`2n` string. -/
def hi (n : ℕ) (j : Fin n) : Fin (2 * n) := ⟨n + (j : ℕ), by have := j.isLt; omega⟩

@[simp] theorem lo_val (n : ℕ) (i : Fin n) : ((lo n i : Fin (2 * n)) : ℕ) = (i : ℕ) := rfl
@[simp] theorem hi_val (n : ℕ) (j : Fin n) : ((hi n j : Fin (2 * n)) : ℕ) = n + (j : ℕ) := rfl

theorem lo_lt (n : ℕ) (i : Fin n) : ((lo n i : Fin (2 * n)) : ℕ) < n := i.isLt
theorem le_hi (n : ℕ) (j : Fin n) : n ≤ ((hi n j : Fin (2 * n)) : ℕ) := by simp

theorem lo_ne_hi (n : ℕ) (i j : Fin n) : lo n i ≠ hi n j := by
  intro h
  have := congrArg (fun p : Fin (2 * n) => (p : ℕ)) h
  simp only [lo_val, hi_val] at this
  have := i.isLt
  omega

/-- Every position of a length-`2n` string lies in the first or in the second half. -/
theorem lo_or_hi (n : ℕ) (p : Fin (2 * n)) :
    (∃ i : Fin n, p = lo n i) ∨ (∃ j : Fin n, p = hi n j) := by
  have hp := p.isLt
  by_cases h : (p : ℕ) < n
  · exact Or.inl ⟨⟨(p : ℕ), h⟩, by apply Fin.ext; simp [lo]⟩
  · refine Or.inr ⟨⟨(p : ℕ) - n, by omega⟩, ?_⟩
    apply Fin.ext; simp [hi]; omega

/-- The length-`2n` string obtained by concatenating `f` and `g`. -/
def pairUp {α : Type*} (n : ℕ) (f g : Fin n → α) : Fin (2 * n) → α :=
  fun p => if h : (p : ℕ) < n then f ⟨(p : ℕ), h⟩ else g ⟨(p : ℕ) - n, by have := p.isLt; omega⟩

@[simp] theorem pairUp_lo {α : Type*} (n : ℕ) (f g : Fin n → α) (i : Fin n) :
    pairUp n f g (lo n i) = f i := by
  simp only [pairUp, lo_val, dif_pos i.isLt]

@[simp] theorem pairUp_hi {α : Type*} (n : ℕ) (f g : Fin n → α) (j : Fin n) :
    pairUp n f g (hi n j) = g j := by
  have hj := j.isLt
  simp only [pairUp, hi_val]
  rw [dif_neg (by omega)]
  congr 1
  apply Fin.ext
  simp

/-! ## The claw function (`sec:prelim`, Definition "Claw") -/

/-- `Claw_{n→κ} : [κ]^{2n} → {0,1}` reads its input as a pair `f, g : [n] → [κ]` and evaluates
to `1` iff `f(i) = g(j)` for some `i, j`.  LaTeX: `sec:prelim`, Definition (Claw).
The paper's alphabet `[κ] = {1,…,κ}` is modelled by `Fin κ`; only equality of alphabet letters
is ever used, so the choice of names is immaterial. -/
def Claw (n κ : ℕ) : (Fin (2 * n) → Fin κ) → Bool :=
  fun y => decide (∃ i j : Fin n, y (lo n i) = y (hi n j))

@[simp] theorem Claw_pairUp (n κ : ℕ) (f g : Fin n → Fin κ) :
    Claw n κ (pairUp n f g) = decide (∃ i j : Fin n, f i = g j) := by
  simp [Claw]

/-! ## The encoding `E` (`lem:encode`, `thm:main-general`)

`encode` is written once for an arbitrary finite abelian group `G` and an arbitrary injection
`s : Fin κ → G`; `lem:encode` is the instance `G = ZMod q`, `s a = a+1`, and `thm:main-general`
is the instance where `s` enumerates a set of representatives of the pairs `{a, -a}`.
No hypothesis on `s` is built into the definition. -/

/-- The per-position value map of the encoding: the first half uses `s`, the second half `-s`.
LaTeX: `E(f,g) = (f(1),…,f(n), -g(1),…,-g(n))`. -/
def encMap {G : Type*} [AddGroup G] {κ : ℕ} (n : ℕ) (s : Fin κ → G) :
    Fin (2 * n) → Fin κ → G :=
  fun p a => if (p : ℕ) < n then s a else -(s a)

/-- The encoding `E`, as a per-coordinate map of strings. -/
def encode {G : Type*} [AddGroup G] {κ : ℕ} (n : ℕ) (s : Fin κ → G)
    (y : Fin (2 * n) → Fin κ) : Fin (2 * n) → G :=
  fun p => encMap n s p (y p)

@[simp] theorem encode_lo {G : Type*} [AddGroup G] {κ : ℕ} (n : ℕ) (s : Fin κ → G)
    (y : Fin (2 * n) → Fin κ) (i : Fin n) : encode n s y (lo n i) = s (y (lo n i)) := by
  simp [encode, encMap, i.isLt]

@[simp] theorem encode_hi {G : Type*} [AddGroup G] {κ : ℕ} (n : ℕ) (s : Fin κ → G)
    (y : Fin (2 * n) → Fin κ) (j : Fin n) : encode n s y (hi n j) = -(s (y (hi n j))) := by
  have hj := j.isLt
  simp only [encode, encMap, hi_val]
  rw [if_neg (by omega)]

/-- The concrete cyclic value set of `lem:encode`: `s a = a + 1 ∈ {1,…,κ} ⊆ ZMod q`. -/
def cyc (q κ : ℕ) : Fin κ → ZMod q := fun a => (((a : ℕ) + 1 : ℕ) : ZMod q)

/-! ## Element distinctness and index-1 orthogonal arrays (`thm:oabarrier`) -/

/-- The `k = 2` orthogonal-array problem attached to a relation `T` on the alphabet:
a hit is a pair of distinct positions whose values are `T`-related.
LaTeX: `sec:barriers`, "a hit is `x_S ∈ T_S`". -/
def twoOAProblem {Alph : Type*} (T : Alph → Alph → Prop) [DecidableRel T] (N : ℕ) :
    (Fin N → Alph) → Bool :=
  fun x => decide (∃ i j : Fin N, i ≠ j ∧ T (x i) (x j))

/-- Index-1 for a `k = 2` array: fixing one of the two coordinates leaves exactly one completion.
LaTeX: `sec:barriers`, "fixing any `k-1` coordinates leaves exactly one completion". -/
def IsIndexOne2 {Alph : Type*} (T : Alph → Alph → Prop) : Prop :=
  (∀ a : Alph, ∃! b : Alph, T a b) ∧ (∀ b : Alph, ∃! a : Alph, T a b)

/-- Element distinctness: the orthogonal-array problem for the diagonal array `T = {(x,x)}`. -/
def ED (N q : ℕ) : (Fin N → Fin q) → Bool := twoOAProblem (· = ·) N

end KsumAudit
