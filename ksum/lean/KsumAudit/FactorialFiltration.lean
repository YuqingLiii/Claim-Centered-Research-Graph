/-
# `lem:factorial-filtration` — Falling-factorial query filtration

LaTeX: `ksum/paper/ksum_small_alphabet.tex`, label `lem:factorial-filtration`, line 754,
displayed equation (38).
DAG node: `KSUM.B4b.L2.FILT` (`ksum/proof-dag/nodes/KSUM.B4b.L2.FILT.yaml`), status
CERTIFIED\* (unchanged by this module — a green build is evidence, never a status, §7.1).
claim_hash: sha256:81a77aaa32ac935912076ca4491a57bd499912545c6ff3dcc74db21dd88e218a

current_claim_hash: sha256:255bacdab3755cf79ff7dc736f0c64f79d776ea54637d019f9f5bc6abb570b6e

CURRENT CANONICAL CLAIM (verbatim from the node record):

  After symmetrization, every degree-d query polynomial on Z_q^N lies in the span of falling-factorial joint occupancy statistics of total degree at most d.

END CURRENT CANONICAL CLAIM

FROZEN CLAIM (verbatim from `claim.statement` in the node file):

  `lem:factorial-filtration` of `ksum/paper/ksum_small_alphabet.tex` (line ~754): degree-`d`
  query polynomials on `Z_q^N`, after symmetrization, land in the span of falling-factorial joint
  occupancy statistics of total degree `≤ d`. This is the bridge that converts every "pure high
  degree" statement about occupancy rows in §`sec:proof-search` into a statement about **query**
  degree — without it, [M1 / pair-tensor annihilation](KSUM.B4b.L2.M1.yaml) is a theorem about labeled
  pair-state rows, not about query polynomials.

PROSE ↔ Lean DIFF.  The node's Claim states one inclusion ("land in the span of"); the manuscript
states the IFF, and `factorial_filtration` below proves the iff, so the Lean is if anything
stronger than the node text.  The Lean is stated for an arbitrary finite alphabet `A` rather than
`Z_q` specifically — the alphabet plays no role — and there is no `def Claim : Prop`: this is a
`KsumAudit` manuscript-facing module, not a `KSUM` node-mirroring one, so the node's `lean.claim`
is `null` and the theorem name is recorded under `lean.composition`.

Written for gap-closure item **L-1** of the 2026-07-31 commission, which cites the
statement-fidelity review (`ksum/reviews/ksum_lean_statement_fidelity_review_20260731.md` §6.B):
*"`lem:factorial-filtration` — NOT FORMALIZED … this is the bridge that makes `thm:pair-tensor`
and `thm:tilted-log-band` statements about QUERY degree; its absence is the root cause of the T3
headline NARROWER."*

## The quantifier structure the LaTeX asserts (written out BEFORE formalizing)

∀ finite alphabet `A`, ∀ length `N`, ∀ `S_N`-invariant signed measure `μ` on `A^N`, ∀ `d`:

  `μ` annihilates every query polynomial of degree below `d`
    ⟺  `∑_x μ(x) ∏_{a∈A} (n_a(x))_{α_a} = 0` for every `α ∈ Z_{≥0}^A` with `|α| < d`.

Both directions, as an iff.  The manuscript's proof is three sentences and each is formalized:

  * *"A compatible one-hot monomial on `m` distinct queried positions, after averaging over `S_N`,
    is `∏_a (n_a)_{α_a} / (N)_m` with `|α| = m`."* — `descFactorial_mul_pair` below, in the
    denominator-free form `(N)_m · ⟨μ, monomial⟩ = ⟨μ, ∏_a (n_a)_{α_a}⟩`.  **The normalization
    `(N)_m` is present and is load-bearing**: it is exactly the number of injections
    `Fin m ↪ Fin N` (`sum_hotMon` + `Fintype.card_embedding_eq`), and the ⟸ direction divides by
    it — legitimately, since `m ≤ N` whenever an injection exists.
  * *"Repeated variables at one position reduce by idempotence, and incompatible symbols give
    zero."* — discharged by the index set of a monomial (see the DEFINITIONAL NOTE): a monomial is
    indexed by an INJECTION `Fin m ↪ Fin N` together with a symbol word `Fin m → A`, so a repeated
    position cannot occur and a position carrying two symbols is not expressible.  That is the
    standard multilinear normal form for one-hot variables.
  * *"Pairing an invariant measure against a polynomial is unchanged by averaging that polynomial
    over `S_N`."* — `pair_hotMon_const`: `S_N`-invariance makes `⟨μ, monomial⟩` depend only on the
    symbol word, not on which positions carry it.

## DEFINITIONAL NOTE (rule 7g: every term of art resolves)

The manuscript does not print a definition of "query polynomial"; the proof of
`lem:factorial-filtration` supplies it, by working with *"a compatible one-hot monomial on `m`
distinct queried positions"*.  So:

  * a **query monomial of degree `m`** is `∏_{l<m} [x_{ι l} = a_l]` for an injection
    `ι : Fin m ↪ Fin N` and a word `a : Fin m → A`  (`hotMon`);
  * a **query polynomial of degree below `d`** is a finite `ℚ`-linear combination of query
    monomials of degree `< d`;
  * "`μ` annihilates" it means `∑_x μ(x) p(x) = 0`.

`AnnihilatesQueryBelow` quantifies over monomials only; `annihilates_linear_combination` proves
this is equivalent to annihilating every linear combination, so nothing is lost.

## SCOPE

Everything here is unconditional finite combinatorics over `ℚ`: no `QueryModel`, no quantum
content, no `sorry`, no `axiom`, no `native_decide`.  The alphabet is an arbitrary
`Fintype` + `DecidableEq` in `Type` (universe `0`), which is where every application lives
(`ZMod q`, `Fin q`); the universe restriction is only so that `Σ s : A, Fin (α s)` may be used as
a word index in `exists_word`.
-/
import KsumAudit.ObstructionsCore
import Mathlib.Data.Fintype.CardEmbedding
import Mathlib.Logic.Equiv.Fintype

namespace KsumAudit.Obstructions.Filtration

open Finset KsumAudit.Obstructions

set_option linter.unusedSectionVars false

variable {A : Type} [Fintype A] [DecidableEq A] {N : ℕ}

/-! ## Vocabulary -/

/-- The occupancy `n_a(x) = |{i : x_i = a}|` of the manuscript. -/
def occ (x : Fin N → A) (a : A) : ℕ := (univ.filter (fun i => x i = a)).card

/-- The symbol multiplicity vector `α` of a word: `α_s = |{l : a_l = s}|`.  The manuscript's
`|α| = m` is `rowOrder (wordType a) = m` (`rowOrder_wordType`). -/
def wordType {m : ℕ} (a : Fin m → A) (s : A) : ℕ := (univ.filter (fun l => a l = s)).card

/-- A **query monomial**: the one-hot product `∏_l [x_{ι l} = a_l]` on the `m` distinct queried
positions `ι 0, …, ι (m-1)`.  Its degree is `m`. -/
def hotMon {m : ℕ} (ι : Fin m ↪ Fin N) (a : Fin m → A) (x : Fin N → A) : ℚ :=
  ∏ l, (if x (ι l) = a l then (1 : ℚ) else 0)

/-- The pairing `⟨μ, f⟩ = ∑_x μ(x) f(x)`. -/
def pair (μ f : (Fin N → A) → ℚ) : ℚ := ∑ x, μ x * f x

/-- The falling-factorial row `∏_a (n_a(x))_{α_a}` read on strings (the integrand of (38)).  It is
`KsumAudit.Obstructions.ffRow` composed with `occ`. -/
def ffStr (α : A → ℕ) (x : Fin N → A) : ℚ := ffRow α (occ x)

/-- `μ` is `S_N`-invariant: relabeling the POSITIONS does not change it. -/
def SNInvariant (μ : (Fin N → A) → ℚ) : Prop :=
  ∀ (π : Equiv.Perm (Fin N)) (x : Fin N → A), μ (fun i => x (π i)) = μ x

/-- "`μ` annihilates every query polynomial of degree below `d`" — the manuscript's phrase,
resolved to query monomials (see `annihilates_linear_combination`). -/
def AnnihilatesQueryBelow (μ : (Fin N → A) → ℚ) (d : ℕ) : Prop :=
  ∀ (m : ℕ), m < d → ∀ (ι : Fin m ↪ Fin N) (a : Fin m → A), pair μ (hotMon ι a) = 0

/-- Equation (38) itself: every falling-factorial moment of order `< d` vanishes. -/
def FactorialMomentsVanishBelow (μ : (Fin N → A) → ℚ) (d : ℕ) : Prop :=
  ∀ α : A → ℕ, rowOrder α < d → pair μ (ffStr α) = 0

/-- **Occupancy is `S_N`-invariant** — the reason every function of the occupancy vector is an
`S_N`-invariant measure (`SNInvariant_of_occ`), which is how the manuscript's invariant measures
are built. -/
theorem occ_comp_perm (π : Equiv.Perm (Fin N)) (x : Fin N → A) :
    occ (fun i => x (π i)) = occ x := by
  funext s
  unfold occ
  rw [Finset.card_filter, Finset.card_filter]
  exact Fintype.sum_equiv π _ _ (fun _ => rfl)

/-- Every function of the occupancy vector is `S_N`-invariant. -/
theorem SNInvariant_of_occ (f : (A → ℕ) → ℚ) : SNInvariant (N := N) (fun x => f (occ x)) := by
  intro π x
  show f (occ (fun i => x (π i))) = f (occ x)
  rw [occ_comp_perm π x]

/-- Occupancies sum to the length. -/
theorem occ_total (x : Fin N → A) : ∑ s, occ x s = N := by
  have h := Finset.card_eq_sum_card_fiberwise
    (f := x) (s := (univ : Finset (Fin N))) (t := (univ : Finset A))
    (fun i _ => Finset.mem_univ (x i))
  simpa [occ] using h.symm

/-- `|wordType a| = m`. -/
theorem rowOrder_wordType {m : ℕ} (a : Fin m → A) : rowOrder (wordType a) = m := by
  have h := Finset.card_eq_sum_card_fiberwise
    (f := a) (s := (univ : Finset (Fin m))) (t := (univ : Finset A))
    (fun l _ => Finset.mem_univ (a l))
  simpa [rowOrder, wordType] using h.symm

/-- Annihilating every monomial of degree `< d` is the same as annihilating every `ℚ`-linear
combination of them, i.e. every query polynomial of degree `< d`.  Recorded so that the
simplification in `AnnihilatesQueryBelow` is not mistaken for a weakening. -/
theorem annihilates_linear_combination (μ : (Fin N → A) → ℚ) (d : ℕ)
    (h : AnnihilatesQueryBelow μ d) {ι : Type*} (T : Finset ι) (deg : ι → ℕ)
    (emb : ∀ j, Fin (deg j) ↪ Fin N) (wrd : ∀ j, Fin (deg j) → A) (coef : ι → ℚ)
    (hdeg : ∀ j ∈ T, deg j < d) :
    pair μ (fun x => ∑ j ∈ T, coef j * hotMon (emb j) (wrd j) x) = 0 := by
  have hswap : pair μ (fun x => ∑ j ∈ T, coef j * hotMon (emb j) (wrd j) x)
      = ∑ j ∈ T, coef j * pair μ (hotMon (emb j) (wrd j)) := by
    unfold pair
    have hpt : ∀ x : Fin N → A, μ x * (∑ j ∈ T, coef j * hotMon (emb j) (wrd j) x)
        = ∑ j ∈ T, coef j * (μ x * hotMon (emb j) (wrd j) x) := by
      intro x
      rw [Finset.mul_sum]
      exact Finset.sum_congr rfl fun j _ => by ring
    rw [Finset.sum_congr rfl (fun x (_ : x ∈ univ) => hpt x), Finset.sum_comm]
    exact Finset.sum_congr rfl fun j _ => by rw [Finset.mul_sum]
  rw [hswap]
  exact Finset.sum_eq_zero fun j hj => by rw [h (deg j) (hdeg j hj) (emb j) (wrd j), mul_zero]

/-! ## Step 1 — the counting identity

`∑_{ι : Fin m ↪ Fin N} ∏_l [x_{ι l} = a_l] = ∏_s (n_s(x))_{α_s}`.

The valid injections split, symbol by symbol, into independent injections of the `α_s` positions
carrying `s` into the `n_s` positions of `x` that hold `s`; there are `(n_s)_{α_s}` of those. -/

/-- The valid injections factor as a product over symbols. -/
def validEquiv {m : ℕ} (a : Fin m → A) (x : Fin N → A) :
    {ι : Fin m ↪ Fin N // ∀ l, x (ι l) = a l} ≃
      (∀ s : A, ({l : Fin m // a l = s} ↪ {i : Fin N // x i = s})) where
  toFun ι := fun s =>
    ⟨fun l => ⟨ι.1 l.1, by rw [ι.2 l.1, l.2]⟩, by
      intro l l' h
      exact Subtype.ext (ι.1.injective (congrArg Subtype.val h))⟩
  invFun F :=
    ⟨⟨fun l => (F (a l) ⟨l, rfl⟩).1, by
        intro l l' h
        have key : ∀ (s s' : A) (_ : s = s') (u : Fin m) (hu : a u = s) (hu' : a u = s'),
            ((F s ⟨u, hu⟩ : {i : Fin N // x i = s}) : Fin N)
              = ((F s' ⟨u, hu'⟩ : {i : Fin N // x i = s'}) : Fin N) := by
          intro s s' hs u hu hu'
          subst hs
          rfl
        have hb : ((F (a l) ⟨l, rfl⟩ : {i : Fin N // x i = a l}) : Fin N)
            = ((F (a l') ⟨l', rfl⟩ : {i : Fin N // x i = a l'}) : Fin N) := h
        have hxl : x ((F (a l) ⟨l, rfl⟩).1) = a l := (F (a l) ⟨l, rfl⟩).2
        have hxl' : x ((F (a l') ⟨l', rfl⟩).1) = a l' := (F (a l') ⟨l', rfl⟩).2
        have haa : a l = a l' := by rw [← hxl, ← hxl', hb]
        have h1 : ((F (a l) ⟨l, rfl⟩ : {i : Fin N // x i = a l}) : Fin N)
            = ((F (a l') ⟨l, haa⟩ : {i : Fin N // x i = a l'}) : Fin N) :=
          key (a l) (a l') haa l rfl haa
        have h2 : (F (a l') ⟨l, haa⟩ : {i : Fin N // x i = a l'})
            = (F (a l') ⟨l', rfl⟩ : {i : Fin N // x i = a l'}) := Subtype.ext (by rw [← h1, hb])
        exact congrArg Subtype.val ((F (a l')).injective h2)⟩,
      fun l => (F (a l) ⟨l, rfl⟩).2⟩
  left_inv := by
    intro ι
    apply Subtype.ext
    apply Function.Embedding.ext
    intro l
    rfl
  right_inv := by
    intro F
    funext s
    apply Function.Embedding.ext
    rintro ⟨u, hu⟩
    apply Subtype.ext
    have key : ∀ (s s' : A) (_ : s = s') (u : Fin m) (hu : a u = s) (hu' : a u = s'),
        ((F s ⟨u, hu⟩ : {i : Fin N // x i = s}) : Fin N)
          = ((F s' ⟨u, hu'⟩ : {i : Fin N // x i = s'}) : Fin N) := by
      intro s s' hs u hu hu'
      subst hs
      rfl
    exact key (a u) s hu u rfl hu

/-- The number of placements of a fixed symbol word that are satisfied by `x`, counted symbol by
symbol: `∏_s (n_s(x))_{α_s}`. -/
theorem card_valid {m : ℕ} (a : Fin m → A) (x : Fin N → A) :
    Fintype.card {ι : Fin m ↪ Fin N // ∀ l, x (ι l) = a l}
      = ∏ s, (occ x s).descFactorial (wordType a s) := by
  rw [Fintype.card_congr (validEquiv a x), Fintype.card_pi]
  refine Finset.prod_congr rfl fun s _ => ?_
  rw [Fintype.card_embedding_eq, Fintype.card_subtype, Fintype.card_subtype]
  rfl

/-- **The counting identity.**  Summing a query monomial over ALL placements of a fixed symbol
word reproduces the falling-factorial row of that word's type. -/
theorem sum_hotMon {m : ℕ} (a : Fin m → A) (x : Fin N → A) :
    ∑ ι : Fin m ↪ Fin N, hotMon ι a x = ffStr (wordType a) x := by
  have hind : ∀ ι : Fin m ↪ Fin N,
      hotMon ι a x = if (∀ l, x (ι l) = a l) then (1 : ℚ) else 0 := by
    intro ι
    unfold hotMon
    by_cases h : ∀ l, x (ι l) = a l
    · rw [if_pos h]
      exact Finset.prod_eq_one fun l _ => if_pos (h l)
    · rw [if_neg h]
      rw [not_forall] at h
      obtain ⟨l, hl⟩ := h
      exact Finset.prod_eq_zero (Finset.mem_univ l) (if_neg hl)
  rw [Finset.sum_congr rfl (fun ι (_ : ι ∈ univ) => hind ι), ← Finset.sum_filter,
    Finset.sum_const, nsmul_eq_mul, mul_one, ← Fintype.card_subtype, card_valid a x]
  unfold ffStr ffRow
  push_cast
  rfl

/-! ## Step 2 — `S_N`-invariance makes the pairing depend only on the word -/

/-- The manuscript's *"pairing an invariant measure against a polynomial is unchanged by averaging
that polynomial over `S_N`"*, in its sharp form: for an `S_N`-invariant `μ` the pairing with a
query monomial does not depend on WHICH `m` distinct positions are queried. -/
theorem pair_hotMon_const {μ : (Fin N → A) → ℚ} (hμ : SNInvariant μ) {m : ℕ} (a : Fin m → A)
    (ι ι' : Fin m ↪ Fin N) : pair μ (hotMon ι a) = pair μ (hotMon ι' a) := by
  obtain ⟨σ, hσ⟩ :=
    Equiv.Perm.exists_extending_pair (α := Fin m) (β := Fin N) ι ι' ι.injective ι'.injective
  have hbij : Function.Bijective (fun (x : Fin N → A) (i : Fin N) => x (σ i)) := by
    refine ⟨fun x y h => ?_, fun y => ⟨fun i => y (σ.symm i), ?_⟩⟩
    · funext i
      have := congrFun h (σ.symm i)
      simpa using this
    · funext i
      simp
  have hmove : ∑ x : Fin N → A, μ (fun i => x (σ i)) * hotMon ι a (fun i => x (σ i))
      = ∑ y : Fin N → A, μ y * hotMon ι a y :=
    Fintype.sum_bijective (fun (x : Fin N → A) (i : Fin N) => x (σ i)) hbij _ _ (fun _ => rfl)
  have hleft : ∀ x : Fin N → A,
      μ (fun i => x (σ i)) * hotMon ι a (fun i => x (σ i)) = μ x * hotMon ι' a x := by
    intro x
    rw [hμ σ x]
    congr 1
    unfold hotMon
    refine Finset.prod_congr rfl fun l _ => ?_
    show (if x (σ (ι l)) = a l then (1 : ℚ) else 0) = if x (ι' l) = a l then (1 : ℚ) else 0
    rw [hσ l]
  rw [pair, pair, ← hmove]
  exact Finset.sum_congr rfl fun x _ => hleft x

/-! ## Step 3 — the normalization `(N)_m` -/

/-- **The `(N)_m` identity of the manuscript's proof, in denominator-free form.**
For an `S_N`-invariant `μ`, at ANY placement `ι` of the word `a`,

    `(N)_m · ⟨μ, ∏_l [x_{ι l} = a_l]⟩ = ⟨μ, ∏_s (n_s)_{α_s}⟩`,   `α = wordType a`.

`(N)_m = |Fin m ↪ Fin N|` is the count the manuscript divides by; it is written on the left so the
identity is unconditional (no `m ≤ N` hypothesis, no division). -/
theorem descFactorial_mul_pair {μ : (Fin N → A) → ℚ} (hμ : SNInvariant μ) {m : ℕ}
    (a : Fin m → A) (ι : Fin m ↪ Fin N) :
    (N.descFactorial m : ℚ) * pair μ (hotMon ι a) = pair μ (ffStr (wordType a)) := by
  have hexpand : pair μ (ffStr (wordType a)) = ∑ ι' : Fin m ↪ Fin N, pair μ (hotMon ι' a) := by
    unfold pair
    have hpt : ∀ x : Fin N → A, μ x * ffStr (wordType a) x
        = ∑ ι' : Fin m ↪ Fin N, μ x * hotMon ι' a x := by
      intro x
      rw [← sum_hotMon a x, Finset.mul_sum]
    rw [Finset.sum_congr rfl (fun x (_ : x ∈ univ) => hpt x), Finset.sum_comm]
  rw [hexpand, Finset.sum_congr rfl (fun ι' (_ : ι' ∈ univ) => pair_hotMon_const hμ a ι' ι),
    Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
  congr 1
  rw [Fintype.card_embedding_eq, Fintype.card_fin, Fintype.card_fin]

/-! ## Step 4 — every symbol multiplicity vector is realized by a word -/

/-- Every `α : A → ℕ` is the type of a word of length `|α|`.  (Needed for the ⟹ direction: the
falling-factorial rows of order `< d` are exactly the rows of the words of degree `< d`.) -/
theorem exists_word (α : A → ℕ) : ∃ a : Fin (rowOrder α) → A, wordType a = α := by
  have hcard : Fintype.card (Σ s : A, Fin (α s)) = rowOrder α := by
    rw [Fintype.card_sigma]
    exact Finset.sum_congr rfl fun s _ => Fintype.card_fin (α s)
  set e : (Σ s : A, Fin (α s)) ≃ Fin (rowOrder α) := Fintype.equivFinOfCardEq hcard with he
  refine ⟨fun i => (e.symm i).1, ?_⟩
  funext s
  have hsub : Fintype.card {i : Fin (rowOrder α) // (e.symm i).1 = s}
      = Fintype.card {z : (Σ s' : A, Fin (α s')) // z.1 = s} :=
    Fintype.card_congr (Equiv.subtypeEquiv e.symm (fun _ => Iff.rfl))
  have hsigma : ∑ s' : A, ∑ _k : Fin (α s'), (if s' = s then (1 : ℕ) else 0)
      = ∑ z : (Σ s' : A, Fin (α s')), (if z.1 = s then (1 : ℕ) else 0) := by
    rw [Finset.sum_sigma' (univ : Finset A) (fun s' => (univ : Finset (Fin (α s'))))
      (fun s' (_ : Fin (α s')) => if s' = s then (1 : ℕ) else 0), Finset.univ_sigma_univ]
  have hfib : Fintype.card {z : (Σ s' : A, Fin (α s')) // z.1 = s} = α s := by
    rw [Fintype.card_subtype, Finset.card_filter, ← hsigma]
    rw [Finset.sum_congr rfl (fun s' (_ : s' ∈ univ) =>
      show (∑ _k : Fin (α s'), (if s' = s then (1 : ℕ) else 0)) = if s' = s then α s' else 0 by
        rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, smul_eq_mul]
        split <;> simp)]
    simp
  unfold wordType
  rw [← Fintype.card_subtype, hsub, hfib]

/-! ## `lem:factorial-filtration` -/

/-- A row of order above the length is identically zero: some symbol must be over-demanded. -/
theorem ffStr_eq_zero_of_lt {α : A → ℕ} (h : N < rowOrder α) (x : Fin N → A) : ffStr α x = 0 := by
  have hocc : ∑ s, occ x s = N := occ_total x
  have hex : ∃ s, occ x s < α s := by
    by_contra hc
    simp only [not_exists, not_lt] at hc
    have hle : ∑ s, α s ≤ ∑ s, occ x s := Finset.sum_le_sum fun s _ => hc s
    rw [hocc] at hle
    exact absurd hle (Nat.not_le.mpr h)
  obtain ⟨s, hs⟩ := hex
  unfold ffStr ffRow
  refine Finset.prod_eq_zero (Finset.mem_univ s) ?_
  rw [Nat.descFactorial_eq_zero_iff_lt.mpr hs]
  norm_num

/-- **`lem:factorial-filtration`** (paper line 754, equation (38)), both directions.

Let `μ` be an `S_N`-invariant signed measure on `A^N`.  Then `μ` annihilates every query
polynomial of degree below `d` **if and only if** every falling-factorial occupancy moment of
order below `d` vanishes.

* (⟹) `∏_a (n_a)_{α_a}` IS a query polynomial of degree `|α|` — it is the sum of the one-hot
  monomials of a word of type `α` over all `(N)_{|α|}` placements (`sum_hotMon`, `exists_word`).
  When `|α| > N` the row is identically zero (`ffStr_eq_zero_of_lt`), so that case is free.
* (⟸) here invariance and the normalization enter: `(N)_m ⟨μ, monomial⟩ = ⟨μ, row⟩`
  (`descFactorial_mul_pair`), and `(N)_m ≠ 0` because a monomial of degree `m` exists only when
  `m ≤ N`. -/
theorem factorial_filtration (μ : (Fin N → A) → ℚ) (hμ : SNInvariant μ) (d : ℕ) :
    AnnihilatesQueryBelow μ d ↔ FactorialMomentsVanishBelow μ d := by
  constructor
  · intro h α hα
    by_cases hmN : rowOrder α ≤ N
    · obtain ⟨a, ha⟩ := exists_word α
      let ι : Fin (rowOrder α) ↪ Fin N :=
        ⟨fun i => ⟨i.1, lt_of_lt_of_le i.2 hmN⟩, by
          intro i j hij
          have hb : (⟨i.1, lt_of_lt_of_le i.2 hmN⟩ : Fin N)
              = ⟨j.1, lt_of_lt_of_le j.2 hmN⟩ := hij
          have hval : (i : ℕ) = (j : ℕ) := congrArg (fun z : Fin N => z.val) hb
          exact Fin.ext hval⟩
      have hkey := descFactorial_mul_pair hμ a ι
      rw [ha] at hkey
      rw [← hkey, h (rowOrder α) hα ι a, mul_zero]
    · unfold pair
      exact Finset.sum_eq_zero fun x _ => by
        rw [ffStr_eq_zero_of_lt (Nat.not_le.mp hmN) x, mul_zero]
  · intro h m hm ι a
    have hmN : m ≤ N := by
      have hcle := Fintype.card_le_of_injective ι ι.injective
      simpa using hcle
    have hne : (N.descFactorial m : ℚ) ≠ 0 := by
      have hnz : N.descFactorial m ≠ 0 := by
        intro hz
        exact absurd (Nat.descFactorial_eq_zero_iff_lt.mp hz) (Nat.not_lt.mpr hmN)
      exact_mod_cast hnz
    have hkey := descFactorial_mul_pair hμ a ι
    rw [h (wordType a) (by rw [rowOrder_wordType]; exact hm)] at hkey
    exact (mul_eq_zero.mp hkey).resolve_left hne

/-! ## The uniform orbit lift — from an occupancy-level measure to a measure on `A^N`

This is the second half of the `lem:factorial-filtration` bridge, and the piece named as NOT
formalized in `KsumAudit/ObstructionsPairTensor.lean` (*"the uniform lift of an occupancy weight
to its `S_N` STRING orbit, and hence `S_N`-invariance on `Z_q^N`"*, *"the pushforward … the `ℓ¹`
identity is not proved here"*) and in `KsumAudit/ObstructionsBandMult.lean` (the occupancy
pushforward of an `S_N`-averaged product).

Given a signed measure `ν` on occupancy vectors, `uniformLift ν` spreads `ν n` uniformly over the
`S_N`-orbit `{x : occ x = n}`.  Three facts, all proved below:

  * it is `S_N`-invariant (it is a function of `occ`);
  * its pushforward under `occ` is `ν` restricted to the achievable occupancy vectors — so every
    occupancy-level pairing lifts verbatim (`sum_uniformLift_comp`);
  * its `ℓ¹` norm equals `ν`'s (`l1_uniformLift`), so a unit-`ℓ¹` occupancy measure lifts to a
    unit-`ℓ¹` measure on `A^N`.  This is exactly the pushforward `ℓ¹` identity the fidelity review
    recorded as missing. -/

section Lift

variable [DecidableEq (A → ℕ)]

/-- The achievable occupancy vectors of length `N`. -/
def occImage : Finset (A → ℕ) := univ.image (occ (A := A) (N := N))

/-- The `S_N`-orbit of strings with a given occupancy vector. -/
def occFiber (n : A → ℕ) : Finset (Fin N → A) := univ.filter (fun x => occ x = n)

theorem occFiber_card_pos {n : A → ℕ} (hn : n ∈ occImage (A := A) (N := N)) :
    0 < (occFiber (A := A) (N := N) n).card := by
  obtain ⟨x, _, hx⟩ := Finset.mem_image.mp hn
  exact Finset.card_pos.mpr ⟨x, Finset.mem_filter.mpr ⟨Finset.mem_univ x, hx⟩⟩

/-- The **uniform orbit lift**: `ν n` spread evenly over the strings of occupancy `n`. -/
noncomputable def uniformLift (ν : (A → ℕ) → ℚ) (x : Fin N → A) : ℚ :=
  ν (occ x) / ((occFiber (A := A) (N := N) (occ x)).card : ℚ)

/-- The lift is `S_N`-invariant, because it is a function of the occupancy vector. -/
theorem uniformLift_SNInvariant (ν : (A → ℕ) → ℚ) :
    SNInvariant (N := N) (uniformLift ν) :=
  SNInvariant_of_occ (fun n => ν n / ((occFiber (A := A) (N := N) n).card : ℚ))

/-- **The pushforward identity.**  Pairing the lift against any function of the occupancy vector
reproduces the occupancy-level pairing against `ν`; the orbit sizes cancel exactly.  (This is the
"hypergeometric block split cancels the block multinomial orbit sizes" step, isolated.) -/
theorem sum_uniformLift_comp (ν : (A → ℕ) → ℚ) (g : (A → ℕ) → ℚ) :
    ∑ x : Fin N → A, uniformLift ν x * g (occ x) = ∑ n ∈ occImage (A := A) (N := N), ν n * g n := by
  rw [← Finset.sum_fiberwise_of_maps_to (s := (univ : Finset (Fin N → A)))
      (t := occImage (A := A) (N := N)) (g := occ (A := A) (N := N))
      (fun x _ => Finset.mem_image_of_mem _ (Finset.mem_univ x))
      (fun x => uniformLift ν x * g (occ x))]
  refine Finset.sum_congr rfl fun n hn => ?_
  have hpos : 0 < (occFiber (A := A) (N := N) n).card := occFiber_card_pos hn
  have hnz : (occFiber (A := A) (N := N) n).card ≠ 0 := by omega
  have hne : ((occFiber (A := A) (N := N) n).card : ℚ) ≠ 0 := by exact_mod_cast hnz
  have hconst : ∀ x ∈ univ.filter (fun x : Fin N → A => occ x = n),
      uniformLift ν x * g (occ x)
        = ν n / ((occFiber (A := A) (N := N) n).card : ℚ) * g n := by
    intro x hx
    have hxo : occ x = n := (Finset.mem_filter.mp hx).2
    unfold uniformLift
    rw [hxo]
  rw [Finset.sum_congr rfl hconst, Finset.sum_const,
    show (univ.filter (fun x : Fin N → A => occ x = n)).card
      = (occFiber (A := A) (N := N) n).card from rfl, nsmul_eq_mul]
  field_simp

/-- **The pushforward `ℓ¹` identity.**  The lift has exactly the `ℓ¹` norm of `ν`. -/
theorem l1_uniformLift (ν : (A → ℕ) → ℚ) :
    ∑ x : Fin N → A, |uniformLift ν x| = ∑ n ∈ occImage (A := A) (N := N), |ν n| := by
  rw [← Finset.sum_fiberwise_of_maps_to (s := (univ : Finset (Fin N → A)))
      (t := occImage (A := A) (N := N)) (g := occ (A := A) (N := N))
      (fun x _ => Finset.mem_image_of_mem _ (Finset.mem_univ x))
      (fun x => |uniformLift ν x|)]
  refine Finset.sum_congr rfl fun n hn => ?_
  have hpos : 0 < (occFiber (A := A) (N := N) n).card := occFiber_card_pos hn
  have hnz : (occFiber (A := A) (N := N) n).card ≠ 0 := by omega
  have hne : ((occFiber (A := A) (N := N) n).card : ℚ) ≠ 0 := by exact_mod_cast hnz
  have hnn : (0 : ℚ) ≤ ((occFiber (A := A) (N := N) n).card : ℚ) := by positivity
  have hconst : ∀ x ∈ univ.filter (fun x : Fin N → A => occ x = n),
      |uniformLift ν x| = |ν n| / ((occFiber (A := A) (N := N) n).card : ℚ) := by
    intro x hx
    have hxo : occ x = n := (Finset.mem_filter.mp hx).2
    unfold uniformLift
    rw [hxo, abs_div, abs_of_nonneg hnn]
  rw [Finset.sum_congr rfl hconst, Finset.sum_const,
    show (univ.filter (fun x : Fin N → A => occ x = n)).card
      = (occFiber (A := A) (N := N) n).card from rfl, nsmul_eq_mul]
  field_simp

/-- **The bridge, assembled.**  An occupancy-level signed measure whose falling-factorial moments
of order `< d` all vanish lifts to an `S_N`-invariant signed measure on `A^N` that annihilates
every QUERY polynomial of degree `< d`, with the same `ℓ¹` norm.

This is `lem:factorial-filtration` used in the direction the manuscript uses it: the
`thm:pair-tensor` / `thm:tilted-log-band` constructions are built at occupancy level, and this is
what turns their occupancy-moment statements into query-degree statements. -/
theorem annihilates_query_of_occ_moments (ν : (A → ℕ) → ℚ) (d : ℕ)
    (h : ∀ α : A → ℕ, rowOrder α < d →
      ∑ n ∈ occImage (A := A) (N := N), ν n * ffRow α n = 0) :
    AnnihilatesQueryBelow (N := N) (uniformLift ν) d
      ∧ (∑ x : Fin N → A, |uniformLift ν x| = ∑ n ∈ occImage (A := A) (N := N), |ν n|) := by
  refine ⟨(factorial_filtration (uniformLift ν) (uniformLift_SNInvariant ν) d).mpr ?_,
    l1_uniformLift ν⟩
  intro α hα
  unfold pair
  rw [show (∑ x : Fin N → A, uniformLift ν x * ffStr α x)
      = ∑ x : Fin N → A, uniformLift ν x * ffRow α (occ x) from rfl,
    sum_uniformLift_comp ν (ffRow α)]
  exact h α hα

end Lift

/-! ## The convolution reduction of `lem:band-multiplication`  (gap-closure batch 2, item H-4(b))

The manuscript *derives* `ν = μ₁ * ⋯ * μ_m` from *"form the product of the uniformly orbit-lifted
block measures, average over `S_N`, take the occupancy pushforward"*; the Lean development instead
*defines* `ν` to be the convolution (`ObstructionsBandMult.band_add`).  Batch 1 proved the
orbit-size cancellation (`sum_uniformLift_comp`, above) and named the exact residual:

> the block splitting `A^{N₁+N₂} ≃ A^{N₁} × A^{N₂}` (as an `Equiv`), occupancy additivity across
> it (`occ (append y z) = occ y + occ z`), and the resulting identity
> `push (uniformLift ν₁ ⊗ uniformLift ν₂) = ν₁ * ν₂`.

All three are proved below.  No multinomial coefficient appears anywhere — that is the point of
`sum_uniformLift_comp`.

What is still NOT here: the `S_N`-average operator itself, i.e. the passage from the product of
lifts (which is only `S_{N₁} × S_{N₂}`-invariant) to an `S_N`-invariant measure with the SAME
occupancy pushforward.  `sum_prod_uniformLift` shows the pushforward is the convolution, and
`occ_comp_perm` shows the pushforward is unchanged by any position permutation, so the averaging
step changes nothing at occupancy level; making that a Lean theorem needs the averaging operator
and the fact that `S_N` acts transitively on strings of fixed occupancy. -/

section Convolution

variable {N₁ N₂ : ℕ}

/-- **The block splitting `A^{N₁+N₂} ≃ A^{N₁} × A^{N₂}`**, as an `Equiv`, realized by
`Fin.append`. -/
def splitEquiv (A : Type) (N₁ N₂ : ℕ) :
    (Fin (N₁ + N₂) → A) ≃ (Fin N₁ → A) × (Fin N₂ → A) where
  toFun x := (fun i => x (Fin.castAdd N₂ i), fun i => x (Fin.natAdd N₁ i))
  invFun p := Fin.append p.1 p.2
  left_inv x := by
    funext i
    induction i using Fin.addCases with
    | left i => exact Fin.append_left _ _ i
    | right i => exact Fin.append_right _ _ i
  right_inv p := by
    refine Prod.ext (funext fun i => ?_) (funext fun i => ?_)
    · exact Fin.append_left _ _ i
    · exact Fin.append_right _ _ i

@[simp] lemma splitEquiv_symm_apply (p : (Fin N₁ → A) × (Fin N₂ → A)) :
    (splitEquiv A N₁ N₂).symm p = Fin.append p.1 p.2 := rfl

/-- **Occupancy is additive across the block splitting**: `occ (append y z) = occ y + occ z`. -/
theorem occ_append (y : Fin N₁ → A) (z : Fin N₂ → A) :
    occ (Fin.append y z) = occ y + occ z := by
  funext a
  simp only [occ, Finset.card_filter, Pi.add_apply]
  rw [Fin.sum_univ_add]
  congr 1
  · exact Finset.sum_congr rfl fun i _ => by rw [Fin.append_left]
  · exact Finset.sum_congr rfl fun i _ => by rw [Fin.append_right]

variable [DecidableEq (A → ℕ)]

/-- **The convolution reduction, proved.**  The occupancy pushforward of the PRODUCT of two
uniformly orbit-lifted block measures is the convolution `ν₁ * ν₂`: paired against an arbitrary
test function `g` of the occupancy vector,
`∑_x (Λ₁ ⊗ Λ₂)(x)·g(occ x) = ∑_{n₁}∑_{n₂} ν₁(n₁)ν₂(n₂)·g(n₁+n₂)`. -/
theorem sum_prod_uniformLift (ν₁ ν₂ : (A → ℕ) → ℚ) (g : (A → ℕ) → ℚ) :
    ∑ x : Fin (N₁ + N₂) → A,
        (uniformLift ν₁ ((splitEquiv A N₁ N₂ x).1) * uniformLift ν₂ ((splitEquiv A N₁ N₂ x).2))
          * g (occ x)
      = ∑ n₁ ∈ occImage (A := A) (N := N₁), ν₁ n₁ *
          ∑ n₂ ∈ occImage (A := A) (N := N₂), ν₂ n₂ * g (n₁ + n₂) := by
  classical
  have hre : ∑ x : Fin (N₁ + N₂) → A,
      (uniformLift ν₁ ((splitEquiv A N₁ N₂ x).1) * uniformLift ν₂ ((splitEquiv A N₁ N₂ x).2))
        * g (occ x)
      = ∑ p : (Fin N₁ → A) × (Fin N₂ → A),
          (uniformLift ν₁ p.1 * uniformLift ν₂ p.2) * g (occ p.1 + occ p.2) := by
    refine Fintype.sum_equiv (splitEquiv A N₁ N₂) _ _ fun x => ?_
    have hx : (splitEquiv A N₁ N₂).symm (splitEquiv A N₁ N₂ x) = x := (splitEquiv A N₁ N₂).symm_apply_apply x
    have hocc : occ x = occ ((splitEquiv A N₁ N₂ x).1) + occ ((splitEquiv A N₁ N₂ x).2) := by
      conv_lhs => rw [← hx]
      rw [splitEquiv_symm_apply, occ_append]
    rw [hocc]
  rw [hre, Fintype.sum_prod_type]
  have hinner : ∀ y : Fin N₁ → A,
      ∑ z : Fin N₂ → A, (uniformLift ν₁ y * uniformLift ν₂ z) * g (occ y + occ z)
        = uniformLift ν₁ y * ∑ n₂ ∈ occImage (A := A) (N := N₂), ν₂ n₂ * g (occ y + n₂) := by
    intro y
    rw [← sum_uniformLift_comp ν₂ (fun n => g (occ y + n)), Finset.mul_sum]
    exact Finset.sum_congr rfl fun z _ => by ring
  rw [Finset.sum_congr rfl (fun y (_ : y ∈ univ) => hinner y)]
  exact sum_uniformLift_comp ν₁ (fun n₁ => ∑ n₂ ∈ occImage (A := A) (N := N₂), ν₂ n₂ * g (n₁ + n₂))

/-- The `ℓ¹` norm of the lifted product is the product of the `ℓ¹` norms — so the normalization
step of `lem:band-multiplication` clause (c) is legal on the lifted object too. -/
theorem l1_prod_uniformLift (ν₁ ν₂ : (A → ℕ) → ℚ) :
    ∑ x : Fin (N₁ + N₂) → A,
        |uniformLift ν₁ ((splitEquiv A N₁ N₂ x).1) * uniformLift ν₂ ((splitEquiv A N₁ N₂ x).2)|
      = (∑ n₁ ∈ occImage (A := A) (N := N₁), |ν₁ n₁|)
          * ∑ n₂ ∈ occImage (A := A) (N := N₂), |ν₂ n₂| := by
  classical
  have hre : ∑ x : Fin (N₁ + N₂) → A,
      |uniformLift ν₁ ((splitEquiv A N₁ N₂ x).1) * uniformLift ν₂ ((splitEquiv A N₁ N₂ x).2)|
      = ∑ p : (Fin N₁ → A) × (Fin N₂ → A), |uniformLift ν₁ p.1| * |uniformLift ν₂ p.2| :=
    Fintype.sum_equiv (splitEquiv A N₁ N₂) _ _ fun x => abs_mul _ _
  rw [hre, Fintype.sum_prod_type, ← l1_uniformLift ν₁, ← l1_uniformLift ν₂, Finset.sum_mul_sum]

/-- The moment form the manuscript consumes: the falling-factorial moments of the lifted product
are exactly the moments of the convolution, which is what makes
`ObstructionsBandMult.band_add`'s conclusion a statement about the constructed object. -/
theorem moment_prod_uniformLift (ν₁ ν₂ : (A → ℕ) → ℚ) (α : A → ℕ) :
    ∑ x : Fin (N₁ + N₂) → A,
        (uniformLift ν₁ ((splitEquiv A N₁ N₂ x).1) * uniformLift ν₂ ((splitEquiv A N₁ N₂ x).2))
          * ffStr α x
      = ∑ n₁ ∈ occImage (A := A) (N := N₁), ν₁ n₁ *
          ∑ n₂ ∈ occImage (A := A) (N := N₂), ν₂ n₂ * ffRow α (n₁ + n₂) :=
  sum_prod_uniformLift ν₁ ν₂ (ffRow α)

/-! ### Non-vacuity for the convolution reduction -/

/-- `occ_append`, computed: appending the one-letter strings `0` and `1` over the alphabet
`Fin 2` gives occupancy `(1,1)`, which is `(1,0) + (0,1)`. -/
example : ∀ a : Fin 2,
    occ (A := Fin 2) (N := 1 + 1) (Fin.append ![(0 : Fin 2)] ![(1 : Fin 2)]) a
      = occ (A := Fin 2) (N := 1) ![(0 : Fin 2)] a
        + occ (A := Fin 2) (N := 1) ![(1 : Fin 2)] a := by decide

/-- The occupancy of that appended string is genuinely `(1,1)` — the identity above is not
`0 = 0`. -/
example : occ (A := Fin 2) (N := 1 + 1) (Fin.append ![(0 : Fin 2)] ![(1 : Fin 2)]) 0 = 1
    ∧ occ (A := Fin 2) (N := 1 + 1) (Fin.append ![(0 : Fin 2)] ![(1 : Fin 2)]) 1 = 1 := by
  decide

/-- `splitEquiv` really is the block splitting: it recovers the two halves. -/
example : (splitEquiv (Fin 2) 1 1 (Fin.append ![(0 : Fin 2)] ![(1 : Fin 2)]))
    = (![(0 : Fin 2)], ![(1 : Fin 2)]) := by
  have h := (splitEquiv (Fin 2) 1 1).apply_symm_apply (![(0 : Fin 2)], ![(1 : Fin 2)])
  rw [splitEquiv_symm_apply] at h
  exact h

/-- Non-vacuity for `sum_prod_uniformLift` / `l1_prod_uniformLift`: at the one-letter alphabet
with `N₁ = N₂ = 1` every fiber is a singleton, so both sides of the pushforward identity are
`ν₁·ν₂·g` — nonzero for `ν₁ = ν₂ = g = 1`. -/
example : ∑ x : Fin (1 + 1) → Fin 1,
      (uniformLift (fun _ => (1:ℚ)) ((splitEquiv (Fin 1) 1 1 x).1)
        * uniformLift (fun _ => (1:ℚ)) ((splitEquiv (Fin 1) 1 1 x).2)) * (1:ℚ)
    = 1 := by
  rw [sum_prod_uniformLift (ν₁ := fun _ => (1:ℚ)) (ν₂ := fun _ => (1:ℚ)) (g := fun _ => (1:ℚ))]
  have h1 : occImage (A := Fin 1) (N := 1) = {fun _ => 1} := by decide
  rw [h1]
  norm_num

end Convolution

/-! ## Non-vacuity witnesses

The statement is about `S_N`-invariant measures, and the `d = 0` case is trivially true of
everything, so the witnesses below exercise a genuinely nonzero measure at a genuinely positive
band. -/

section Witness

/-- Alphabet `Fin 2`, length `2`: `μ = +1` on the two constant strings and `-1` on the two mixed
strings, written as a function of the occupancy vector so that `S_2`-invariance is by
construction. -/
private def wf (n : Fin 2 → ℕ) : ℚ := if n 0 = 1 then -1 else 1

private def wμ : (Fin 2 → Fin 2) → ℚ := fun x => wf (occ x)

private theorem wμ_inv : SNInvariant wμ := SNInvariant_of_occ wf

/-- Explicit enumeration of `(Fin 2 → Fin 2)`, so that the numeric checks below reduce without
going through the `Multiset.Pi` machinery of the Pi-`Fintype` instance. -/
private theorem sum_two (g : (Fin 2 → Fin 2) → ℚ) :
    ∑ x : Fin 2 → Fin 2, g x = g ![0, 0] + g ![0, 1] + g ![1, 0] + g ![1, 1] := by
  have hEq := Fintype.sum_equiv (finTwoArrowEquiv (Fin 2))
    g (fun p : Fin 2 × Fin 2 => g ![p.1, p.2]) (fun x => by
      congr 1
      funext i
      fin_cases i <;> rfl)
  rw [hEq, Fintype.sum_prod_type, Fin.sum_univ_two, Fin.sum_univ_two, Fin.sum_univ_two]
  ring

private theorem wμ_row (α : Fin 2 → ℕ) (x : Fin 2 → Fin 2) :
    ffStr α x = ((occ x 0).descFactorial (α 0) : ℚ) * ((occ x 1).descFactorial (α 1) : ℚ) := by
  simp [ffStr, ffRow, Fin.prod_univ_two]

private theorem occ_vals :
    occ (![0, 0] : Fin 2 → Fin 2) 0 = 2 ∧ occ (![0, 0] : Fin 2 → Fin 2) 1 = 0 ∧
    occ (![0, 1] : Fin 2 → Fin 2) 0 = 1 ∧ occ (![0, 1] : Fin 2 → Fin 2) 1 = 1 ∧
    occ (![1, 0] : Fin 2 → Fin 2) 0 = 1 ∧ occ (![1, 0] : Fin 2 → Fin 2) 1 = 1 ∧
    occ (![1, 1] : Fin 2 → Fin 2) 0 = 0 ∧ occ (![1, 1] : Fin 2 → Fin 2) 1 = 2 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> decide

/-- `μ = +1` on the constant strings, `-1` on the mixed ones. -/
private theorem wμ_vals :
    wμ ![0, 0] = 1 ∧ wμ ![0, 1] = -1 ∧ wμ ![1, 0] = -1 ∧ wμ ![1, 1] = 1 := by
  obtain ⟨a0, _, b0, _, c0, _, d0, _⟩ := occ_vals
  refine ⟨?_, ?_, ?_, ?_⟩ <;> unfold wμ wf
  · rw [a0]; norm_num
  · rw [b0]; norm_num
  · rw [c0]; norm_num
  · rw [d0]; norm_num

/-- Order-`< 2` moments all vanish: only `α = (0,0), (1,0), (0,1)` are in range. -/
private theorem wμ_moments : FactorialMomentsVanishBelow wμ 2 := by
  intro α hα
  have hlt : α 0 + α 1 < 2 := by simpa [rowOrder, Fin.sum_univ_two] using hα
  have hpt : ∀ x : Fin 2 → Fin 2, wμ x * ffStr α x
      = wμ x * (((occ x 0).descFactorial (α 0) : ℚ) * ((occ x 1).descFactorial (α 1) : ℚ)) :=
    fun x => by rw [wμ_row α x]
  obtain ⟨a0, a1, b0, b1, c0, c1, d0, d1⟩ := occ_vals
  obtain ⟨w00, w01, w10, w11⟩ := wμ_vals
  unfold pair
  rw [Finset.sum_congr rfl (fun x (_ : x ∈ univ) => hpt x), sum_two,
    a0, a1, b0, b1, c0, c1, d0, d1, w00, w01, w10, w11]
  rcases (show (α 0 = 0 ∧ α 1 = 0) ∨ (α 0 = 1 ∧ α 1 = 0) ∨ (α 0 = 0 ∧ α 1 = 1) by omega)
    with ⟨h0, h1⟩ | ⟨h0, h1⟩ | ⟨h0, h1⟩ <;> rw [h0, h1] <;> norm_num

/-- **The ⟸ direction at a concrete nonzero measure**: the vanishing of the order-`< 2`
falling-factorial moments really does deliver annihilation of every query monomial of degree
`< 2`. -/
example : AnnihilatesQueryBelow wμ 2 := (factorial_filtration wμ wμ_inv 2).mpr wμ_moments

/-- …and the band is EXACTLY `2`, so nothing above is vacuous: the order-`2` moment
`∑_x μ(x) (n_0(x))_2` is `2 ≠ 0`. -/
example : pair wμ (ffStr (fun s => if s = 0 then 2 else 0)) = 2 := by
  have hpt : ∀ x : Fin 2 → Fin 2, wμ x * ffStr (fun s => if s = 0 then 2 else 0) x
      = wμ x * (((occ x 0).descFactorial 2 : ℚ) * ((occ x 1).descFactorial 0 : ℚ)) :=
    fun x => by rw [wμ_row (fun s => if s = 0 then 2 else 0) x]; norm_num
  obtain ⟨a0, a1, b0, b1, c0, c1, d0, d1⟩ := occ_vals
  obtain ⟨w00, w01, w10, w11⟩ := wμ_vals
  unfold pair
  rw [Finset.sum_congr rfl (fun x (_ : x ∈ univ) => hpt x), sum_two,
    a0, a1, b0, b1, c0, c1, d0, d1, w00, w01, w10, w11]
  norm_num

end Witness

#print axioms occ_total
#print axioms annihilates_linear_combination
#print axioms card_valid
#print axioms sum_hotMon
#print axioms pair_hotMon_const
#print axioms descFactorial_mul_pair
#print axioms exists_word
#print axioms rowOrder_wordType
#print axioms ffStr_eq_zero_of_lt
#print axioms factorial_filtration
#print axioms occ_comp_perm
#print axioms SNInvariant_of_occ
#print axioms sum_uniformLift_comp
#print axioms l1_uniformLift
#print axioms annihilates_query_of_occ_moments
#print axioms occ_append
#print axioms sum_prod_uniformLift
#print axioms l1_prod_uniformLift
#print axioms moment_prod_uniformLift

end KsumAudit.Obstructions.Filtration
