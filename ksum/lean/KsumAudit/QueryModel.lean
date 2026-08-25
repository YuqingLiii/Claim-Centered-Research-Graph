/-
The abstract query-model interface for the machine-checked audit of

  `ksum/paper/ksum_small_alphabet.tex`

Proof-DAG node: `KSUM.LEAN.T1.k2-main-line` (registered OPEN under rule 8a, 2026-07-30).

EVERYTHING IN THIS FILE IS A HYPOTHESIS.  `Q` and the cited lower bounds are **fields of a
structure**, deliberately not `axiom`s: a field carries zero soundness risk (`#print axioms`
stays at Lean's three standard axioms, so the citation manifest is machine-checked), whereas a
bad `axiom` can silently prove `False`.  A theorem proved against `QueryModel` is exactly as
strong as the citations it names and not one notch stronger.  See
`ksum/proof-dag/nodes/KSUM.LEAN.yaml`, scope clause 1.

Alphabets are position-dependent (`Alph : Fin M → Type`).  This is *forced* by the paper:
`sec:prelim` fact (ii) allows the per-coordinate bijection to be "possibly different per
position, and possibly changing the alphabet", and the encoding `E` of `lem:encode` is genuinely
different on the two halves.  With a single alphabet, facts (i) and (ii) cannot be composed at
all (see `relabel_inj` below), because the codeword set of `E` is a *product* of two different
per-position value sets.

Alphabets live in `Type 0`.  Every alphabet in the paper is a finite set, so this is not a
restriction on the mathematics; it is recorded here so that the fidelity review can see it.
-/
import KsumAudit.Defs
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.Real.Sqrt

namespace KsumAudit

/-- The bounded-error quantum query model, as an interface.

Fields `restrict`, `relabel` are facts (i) and (ii) of `sec:prelim`.  Fields `abi` and `tani`
are Theorems `thm:abi` and `thm:tani`, imported as citations.  Fields `freeze` and `constQ` are
two further elementary facts: **explicitly recorded after external review** — they were findings F1 and F2 of
this audit, facts the paper used but did not state — and **stated in the manuscript as facts
(iii) and (iv) in the reviewed manuscript** (2026-07-31 manuscript-repair batch, items M-1/M-2).  They are
flagged individually below. -/
structure QueryModel where
  /-- `Q f` is the bounded-error quantum query complexity of the Boolean function `f` on
  length-`M` strings whose `i`-th letter ranges over the finite alphabet `Alph i`.
  LaTeX: `sec:prelim`, paragraph "Query model". -/
  Q : {M : ℕ} → {Alph : Fin M → Type} → [∀ i, Fintype (Alph i)] →
      (((i : Fin M) → Alph i) → Bool) → ℝ
  /-- **Fact (i), restriction** (`sec:prelim` item (i)): restricting the domain does not increase
  `Q`, "since an algorithm for `f` already solves `g` with the same queries".  The restriction is
  to a product subdomain `∏ i, D i`; the restricted function is then a function over the
  per-position alphabets `D i`.  (Every domain restriction performed in the paper is of this
  product shape: it restricts each position's value set separately.) -/
  restrict : ∀ {M : ℕ} {Alph : Fin M → Type} [∀ i, Fintype (Alph i)]
      (D : ∀ i, Finset (Alph i)) (f : ((i : Fin M) → Alph i) → Bool),
      Q (fun y : ((i : Fin M) → {a : Alph i // a ∈ D i}) => f (fun i => (y i : Alph i))) ≤ Q f
  /-- **Fact (ii), per-coordinate relabeling** (`sec:prelim` item (ii)): if `g(y) = f(φ(y))` with
  `φ(y)_i = φ_i(y_i)` for fixed bijections `φ_i` — *possibly different per position, and possibly
  changing the alphabet* — then `Q g ≤ 2 Q f`.  Only this direction is ever used, exactly as the
  paper states ("Every transfer in this paper invokes (ii) in the single direction"). -/
  relabel : ∀ {M : ℕ} {Alph Alph' : Fin M → Type} [∀ i, Fintype (Alph i)]
      [∀ i, Fintype (Alph' i)] (e : ∀ i, Alph' i ≃ Alph i)
      (f : ((i : Fin M) → Alph i) → Bool),
      Q (fun y => f (fun i => e i (y i))) ≤ 2 * Q f
  /-- **Frozen coordinate.**  `sec:prelim` facts **(i) + (iii)** composed at the last position:
  restrict to the product subdomain whose last factor is the singleton `{a}` (fact (i)), then
  delete that now-singleton coordinate (fact (iii), *singleton-coordinate deletion*).  Used by
  `lem:oddN` ("extend the encoding by one frozen coordinate of value `0`") and by the `sec:k3`
  freeze step, both of which now cite (i)+(iii) explicitly.
  **Explicitly recorded after external review:** this field was finding **F1** of the 2026-07-30 T1 audit, which
  reported that no such principle was stated and that fact (i) as *printed* did not type-check
  for it, because deleting a coordinate changes the input LENGTH.  The reviewed manuscript states fact (iii)
  with exactly that not-an-instance-of-(i) note (2026-07-31 manuscript-repair batch, item M-1),
  so F1 is DISCHARGED and this field is a cited preliminary fact. -/
  freeze : ∀ {M : ℕ} {Alph : Fin (M + 1) → Type} [∀ i, Fintype (Alph i)]
      (a : Alph (Fin.last M)) (f : ((i : Fin (M + 1)) → Alph i) → Bool),
      Q (fun y : ((i : Fin M) → Alph i.castSucc) => f (Fin.snoc y a)) ≤ Q f
  /-- **A constant function has query complexity `0`.**  `sec:prelim` fact **(iv)**; used by
  `thm:oabarrier` ("In both cases `Q = 0`"), whose proof now cites it.
  **Explicitly recorded after external review:** finding **F2** of the audit, until the reviewed manuscript added fact (iv)
  (2026-07-31 manuscript-repair batch, item M-2); F2 is DISCHARGED. -/
  constQ : ∀ {M : ℕ} {Alph : Fin M → Type} [∀ i, Fintype (Alph i)]
      (f : ((i : Fin M) → Alph i) → Bool) (b : Bool), (∀ y, f y = b) → Q f = 0
  /-- The absolute constant hidden in the `Ω(·)` of `thm:abi` / `thm:tani`.  Making it explicit
  is what removes the two-parameter (`n`, `κ`) ambiguity of the asymptotic statement. -/
  cABI : ℝ
  cABI_pos : 0 < cABI
  /-- **`thm:abi`** (Ambainis–Balodis–Iraids): for all `2 ≤ κ < n`,
  `Q(Claw_{n→κ}) = Ω(√n · κ^{1/6})`. -/
  abi : ∀ (n κ : ℕ), 2 ≤ κ → κ < n →
      cABI * Real.sqrt n * (κ : ℝ) ^ (1 / 6 : ℝ) ≤ Q (Claw n κ)
  /-- **`thm:tani`** (Tani): the same bound for all `2 ≤ κ ≤ 2n-1`.
  `κ ≤ 2n-1` is written `κ < 2*n`; over `ℕ` these are equivalent whenever `n ≥ 1`, and `κ ≥ 2`
  forces `n ≥ 1` in both readings, whereas the literal `κ ≤ 2*n - 1` would silently become
  `κ ≤ 0` at `n = 0` through truncated subtraction. -/
  tani : ∀ (n κ : ℕ), 2 ≤ κ → κ < 2 * n →
      cABI * Real.sqrt n * (κ : ℝ) ^ (1 / 6 : ℝ) ≤ Q (Claw n κ)

namespace QueryModel

/-- **Facts (i) and (ii) composed.**  A per-coordinate *injective* re-encoding — the map need not
be onto the target alphabet — costs at most the absolute factor `2`.

This is exactly the step performed inside the proof of `lem:encode` ("restrict `2Sum` to the
codeword subdomain `E([κ]^{2n})`; this can only lower complexity (fact (i)); on that subdomain
the displayed identity exhibits the restricted function as `Claw` read through the per-coordinate
bijection `E` onto its image, so importing the claw bound costs at most the absolute factor `2` of
fact (ii)").  It is a *theorem*, not a field: the audit therefore certifies that the encoding uses
nothing beyond the paper's two stated facts. -/
theorem relabel_inj (M : QueryModel) {N : ℕ} {Alph Alph' : Fin N → Type}
    [∀ i, Fintype (Alph i)] [∀ i, Fintype (Alph' i)]
    (φ : ∀ i, Alph' i → Alph i) (hφ : ∀ i, Function.Injective (φ i))
    (f : ((i : Fin N) → Alph i) → Bool) :
    M.Q (fun y => f (fun i => φ i (y i))) ≤ 2 * M.Q f := by
  classical
  set D : ∀ i, Finset (Alph i) := fun i => Finset.univ.image (φ i) with hD
  have hmem : ∀ i (a : Alph' i), φ i a ∈ D i := by
    intro i a; simp [hD]
  have hr : ∀ i, Function.Bijective (fun a : Alph' i => (⟨φ i a, hmem i a⟩ : {b : Alph i // b ∈ D i})) := by
    intro i
    refine ⟨fun a b hab => hφ i (congrArg Subtype.val hab), ?_⟩
    rintro ⟨b, hb⟩
    simp only [hD, Finset.mem_image, Finset.mem_univ, true_and] at hb
    obtain ⟨a, ha⟩ := hb
    exact ⟨a, by simp [ha]⟩
  calc M.Q (fun y => f (fun i => φ i (y i)))
      = M.Q (fun y : ((i : Fin N) → Alph' i) =>
          (fun z : ((i : Fin N) → {b : Alph i // b ∈ D i}) => f (fun i => (z i : Alph i)))
            (fun i => Equiv.ofBijective _ (hr i) (y i))) := rfl
    _ ≤ 2 * M.Q (fun z : ((i : Fin N) → {b : Alph i // b ∈ D i}) => f (fun i => (z i : Alph i))) :=
        M.relabel (Alph := fun i => {b : Alph i // b ∈ D i}) (Alph' := Alph')
          (fun i => Equiv.ofBijective _ (hr i)) (fun z => f (fun i => (z i : Alph i)))
    _ ≤ 2 * M.Q f := by linarith [M.restrict D f]

end QueryModel

end KsumAudit
