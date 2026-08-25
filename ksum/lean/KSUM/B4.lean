/-
`KSUM/B4.lean` — linked node module.
**This module's `composition` theorem IS the node's composition proof** (the current composition-linking convention).

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : KSUM.B4                          (alias `B4`)
node file      : ksum/proof-dag/nodes/KSUM.B4.yaml
decomposition / role    : AND / proof     children: B4a, B4b
epistemic status (read from the node file on 2026-07-30): **OPEN**
                 (`= min(composition=CONJECTURED, B4a=PROVED, B4b=OPEN)`)
mechanization  : **composition-checked**, relative to
                 rel = [KSUM.B4b — the matching lower bound; it has NO node module in this pass
                        (it is an OR node with its own subtree) and enters as the explicitly
                        named hypothesis `B4bClaim` below]
claim_hash     : sha256:71c3023342716fabaec0e87f30972b145bf78405f5de9026f1c155958eec21af
                 (byte convention: see `KSUM/A1a.lean`)

current_claim_hash: sha256:44da23d6a8c52d7d9cea9e35ec17247ac39cbc1dbc43e6f06db8fb33dc5a94d7

CURRENT CANONICAL CLAIM (verbatim from the node record):

  OR-4 (AND internally): UPPER-BOUND / ALGORITHM SIDE — close the k=2 middle gap
  (B4a PROVED: upper q^1/4; lower q^1/6, so exponent matching remains)

END CURRENT CANONICAL CLAIM

FROZEN CLAIM (verbatim from `claim.statement` in the node file):

  OR-4 (AND internally): UPPER-BOUND / ALGORITHM SIDE — close the k=2 middle gap
  (B4a PROVED: upper q^1/4; lower q^1/6, so exponent matching remains) [OPEN]

FROZEN COMPOSITION CLAIM (verbatim from the node's `composition.claim`):

  B4a (the upper bound O_eps(N^{1/2+eps} q^{1/4})) AND B4b (a lower bound matching it) together
  imply B4: the k=2 exponent window at small alphabet is closed.

FROZEN `composition.rel` (verbatim):

  the two sides must be compared at the SAME (N,q) with the same normalization — the exponent
  window is two-parameter, and 'matching' means matching as a function of both N and q, not at
  one slice

════════════════════════════════════════════════════════════════════════════════════════════════
  HOW THE `rel` IS HONOURED — this is the whole content of the composition
════════════════════════════════════════════════════════════════════════════════════════════════

The node's prose is blunt about where this branch leaks: *"A route that improves the lower bound
at one slice of `q` (say `q = Θ(N^{2/3})`) does not close `B4`"*, and *"`ε` is not cosmetic …
'closed' means closed up to `N^{o(1)}`"*.  Both are enforced structurally here rather than in
prose:

* **Same `(N, q, t)`.**  In `Claim`, the two bounds sit under ONE `∀ (N q : ℕ) [NeZero q]
  … ∀ t`, so a lower bound valid only on a slice of `q` cannot instantiate `B4bClaim` and
  therefore cannot be composed.  A one-slice improvement is not even type-correct here.
  *(2026-07-30, R-B4-1: that shared quantifier is now `q` odd with `5 ≤ q ≤ N` — a REGIME, not a
  slice.  The distinction is the point: a regime is where both sides are stated and where the
  exponent question is open; a slice is a single `q = q(N)` curve inside it.  See `B4bClaim`.)*
* **`ε` survives.**  `Claim` quantifies `∀ ε > 0` on the OUTSIDE and keeps `N^{1/2+ε}` in the
  upper bound, so "closed" formally means "closed up to `N^{ε}` for every `ε`", never "equal".
* **Same normalization.**  Both sides are stated about the same `M.Q (twoSum (ZMod q) t N)`.

`KSUM.B4b` has no module in this pass — it is an OR node with a large subtree and is not in the
commissioned module list — so its claim enters as the explicitly named parameter `B4bClaim`,
whose statement is written out below rather than imported.  That is a deviation from §7.3's
"a node module imports its status-propagating children" and is reported as such.

No `sorry`.
-/
import KSUM.B4a

namespace KSUM.B4

open KsumAudit

/-- The claim of `KSUM.B4b` (node `ksum/proof-dag/nodes/KSUM.B4b.yaml`, status **OPEN**),
written out here because that node has no Lean module in this pass: a lower bound matching
`KSUM.B4a`'s upper bound, at the SAME `(N, q, t)`, with exponents `(1/2, 1/4)`.

**`q`-range restricted 2026-07-30 (review finding R-B4-1).**  As first written this demanded the
bound for EVERY `q` with `NeZero q`, which is not merely unmet but **unsatisfiable**: at
`q = 2, t = 0, N ≥ 3` pigeonhole gives `i ≠ j` with `x_i = x_j`, and `x_i + x_j = 2x_i = 0` in
`Z_2`, so `2Sum ≡ true` is constant and `Q = 0` in any faithful model, while the claim demands
`c·√N·2^{1/4} > 0`.  A vacuous hypothesis makes the composition below vacuous too, which is
exactly what §7.10(5) tells a reviewer to reject.

The regime chosen is the one the paper's matching claim lives in — `thm:main-odd`, i.e. **`q` odd
with `5 ≤ q ≤ N`** — and it is the intersection of the two sides' scopes: every registered `B4b`
route (`M1` and the `L2` group) is stated for odd `q` with `N ≥ q`, while `KSUM.B4a` holds for
all `q`, so restricting costs the upper side nothing.  `q ≤ N` also keeps the statement inside
the small-alphabet window this problem is about (`q ≥ N^k` is where Belovs–Špalek is already
tight).  A sandwich between differently-scoped sides is not a sandwich. -/
def B4bClaim (M : QueryModel) : Prop :=
  ∃ c : ℝ, 0 < c ∧ ∃ N₀ : ℕ,
    ∀ (N q : ℕ) [NeZero q], N₀ ≤ N → Odd q → 5 ≤ q → q ≤ N → ∀ t : ZMod q,
      c * (N : ℝ) ^ (1 / 2 : ℝ) * (q : ℝ) ^ (1 / 4 : ℝ) ≤ M.Q (twoSum (ZMod q) t N)

/-- **`KSUM.B4`, formal Claim** — "the `k = 2` exponent window at small alphabet is closed",
i.e. for every `ε > 0` the two bounds sandwich `Q(2Sum_{Z_q,t,N})` between
`c·N^{1/2}·q^{1/4}` and `C·N^{1/2+ε}·q^{1/4}` at the same `(N, q, t)`, **for `q` odd with
`5 ≤ q ≤ N`** (the `thm:main-odd` regime; see `B4bClaim` for why the unrestricted form was
vacuous).  The upper half continues to hold for every `q`; only the sandwich is scoped. -/
def Claim (M : QueryModel) : Prop :=
  ∀ ε : ℝ, 0 < ε → ∃ c C : ℝ, 0 < c ∧ 0 < C ∧ ∃ N₀ : ℕ,
    ∀ (N q : ℕ) [NeZero q], N₀ ≤ N → Odd q → 5 ≤ q → q ≤ N → ∀ t : ZMod q,
      c * (N : ℝ) ^ (1 / 2 : ℝ) * (q : ℝ) ^ (1 / 4 : ℝ) ≤ M.Q (twoSum (ZMod q) t N) ∧
        M.Q (twoSum (ZMod q) t N) ≤ C * (N : ℝ) ^ (1 / 2 + ε) * (q : ℝ) ^ (1 / 4 : ℝ)

/-- **The composition proof of `KSUM.B4`, mechanized.**  `B4a ∧ B4b ⇒ B4`: the sandwich, with the
two sides forced onto the same `(N, q, t)` by construction.

A green build of this theorem is a *run* under the current evidence-level rules and therefore evidence at
NUMERICAL tier at best.  It does NOT make `KSUM.B4` anything other than OPEN: `B4bClaim` is an
unmet hypothesis, which is exactly the state of the node. -/
theorem composition (M : QueryModel) (hB4a : KSUM.B4a.Claim M) (hB4b : B4bClaim M) :
    Claim M := by
  obtain ⟨c, hc, N₁, hlow⟩ := hB4b
  intro ε hε
  obtain ⟨Cε, hCε, N₂, hup⟩ := hB4a ε hε
  refine ⟨c, Cε, hc, hCε, max N₁ N₂, ?_⟩
  intro N q _inst hN hodd hq5 hqN t
  -- `KSUM.B4a.Claim` carries the manuscript's `q ≥ 2` since 2026-07-31 (closeout C-5); the
  -- sandwich is stated at `5 ≤ q`, which supplies it.  This is the whole cost of that repair.
  exact ⟨hlow N q (le_trans (le_max_left _ _) hN) hodd hq5 hqN t,
    hup N q (le_trans (le_max_right _ _) hN) (by omega) t⟩

/-! ## Non-vacuity of the sandwich: a model satisfying BOTH sides

**Closeout item C-4(b), 2026-07-31**, implementing the construction prescribed by the
statement-fidelity review `ksum/reviews/ksum_lean_statement_fidelity_review_20260731.md` §7.3.

`composition` above is machine-checked, but §7.10(5) asks the separate and much weaker question
whether it is about anything: **are `KSUM.B4a.Claim M` and `B4bClaim M` jointly satisfiable for
some `M : QueryModel` at all?**  Two hypotheses that cannot hold together make the composition
vacuous, and the review recorded that nothing on disk ruled this out — `KsumAudit.demoModel`
explicitly does NOT work, because its value `M^{2/3}` depends only on the input LENGTH and falls
below `c·N^{1/2}q^{1/4} ≈ c·N^{3/4}` when `q ≈ N`.

Note precisely what is and is not at issue.  Whether the true bounded-error quantum query
complexity satisfies `B4bClaim` is the **open `k = 2` lower bound** and nothing here bears on it.
What is settled below is that the sandwich's two sides are not contradictory, so `composition` is
not a proof about the empty set of models.

The witness is the review's own: an **alphabet-aware** measure

    Q(f) = 0                      if `f` is constant
    Q(f) = M^{1/2} · A^{1/4}      otherwise,

with `M` the input length and `A = max_i |Alph i|` the largest per-position alphabet.  It matches
the exponents of both sides exactly, which is why it satisfies them simultaneously with
`C_ε = c = 1`.  Like `demoModel` it is a *consistency* witness and is not quantum query
complexity; unlike `demoModel` it can see the alphabet, which is the whole point.

Two design notes, so that the witness is not mistaken for more than it is:

* `A` is `Nat.card`-based and therefore instance-free — no `Fintype` instance mismatch can make a
  step of the argument silently about a different cardinality;
* the witness satisfies `relabel` with constant `1`, so it exercises no part of the factor-2
  slack, exactly as the review observed for `demoModel`. -/

/-- The largest per-position alphabet size of a length-`M` input family (`0` when `M = 0`).
Defined through `Nat.card`, so it depends on no `Fintype` instance. -/
noncomputable def maxAlph {M : ℕ} (Alph : Fin M → Type) : ℕ :=
  Finset.univ.sup fun i => Nat.card (Alph i)

theorem maxAlph_const {M : ℕ} (hM : 1 ≤ M) (A : Type) :
    maxAlph (fun _ : Fin M => A) = Nat.card A := by
  simp only [maxAlph]
  exact Finset.sup_const ⟨⟨0, hM⟩, Finset.mem_univ _⟩ _

theorem maxAlph_subtype_le {M : ℕ} {Alph : Fin M → Type} [∀ i, Fintype (Alph i)]
    (D : ∀ i, Finset (Alph i)) :
    maxAlph (fun i => {a : Alph i // a ∈ D i}) ≤ maxAlph Alph := by
  simp only [maxAlph]
  refine Finset.sup_le fun i _ => le_trans ?_
    (Finset.le_sup (f := fun j => Nat.card (Alph j)) (Finset.mem_univ i))
  exact Nat.card_le_card_of_injective (fun a : {a : Alph i // a ∈ D i} => (a : Alph i))
    Subtype.val_injective

theorem maxAlph_equiv_le {M : ℕ} {Alph Alph' : Fin M → Type} (e : ∀ i, Alph' i ≃ Alph i) :
    maxAlph Alph' ≤ maxAlph Alph := by
  simp only [maxAlph]
  refine Finset.sup_le fun i _ => ?_
  rw [Nat.card_congr (e i)]
  exact Finset.le_sup (f := fun j => Nat.card (Alph j)) (Finset.mem_univ i)

theorem maxAlph_castSucc_le {M : ℕ} (Alph : Fin (M + 1) → Type) :
    maxAlph (fun i : Fin M => Alph i.castSucc) ≤ maxAlph Alph := by
  simp only [maxAlph]
  exact Finset.sup_le fun i _ =>
    Finset.le_sup (f := fun j => Nat.card (Alph j)) (Finset.mem_univ i.castSucc)

open Classical in
/-- The alphabet-aware consistency-witness complexity measure (review §7.3). -/
noncomputable def sandwichQ {M : ℕ} {Alph : Fin M → Type}
    (f : ((i : Fin M) → Alph i) → Bool) : ℝ :=
  if (∀ y z, f y = f z) then 0
  else (M : ℝ) ^ (1 / 2 : ℝ) * (maxAlph Alph : ℝ) ^ (1 / 4 : ℝ)

theorem sandwichQ_const {M : ℕ} {Alph : Fin M → Type} (f : ((i : Fin M) → Alph i) → Bool)
    (h : ∀ y z, f y = f z) : sandwichQ f = 0 := by
  classical
  simp only [sandwichQ]
  rw [if_pos h]

theorem sandwichQ_nonconst {M : ℕ} {Alph : Fin M → Type} (f : ((i : Fin M) → Alph i) → Bool)
    (h : ¬ ∀ y z, f y = f z) :
    sandwichQ f = (M : ℝ) ^ (1 / 2 : ℝ) * (maxAlph Alph : ℝ) ^ (1 / 4 : ℝ) := by
  classical
  simp only [sandwichQ]
  rw [if_neg h]

theorem sandwichQ_nonneg {M : ℕ} {Alph : Fin M → Type} (f : ((i : Fin M) → Alph i) → Bool) :
    0 ≤ sandwichQ f := by
  by_cases h : ∀ y z, f y = f z
  · exact le_of_eq (sandwichQ_const f h).symm
  · rw [sandwichQ_nonconst f h]; positivity

/-- The one monotonicity fact behind `restrict`, `relabel` and `freeze`: a derived function on a
shorter input over smaller alphabets, which is constant whenever the original is, cannot have a
larger witness value. -/
theorem sandwichQ_le_of {M M' : ℕ} {Alph : Fin M → Type} {Alph' : Fin M' → Type}
    {g : ((i : Fin M) → Alph i) → Bool} {f : ((i : Fin M') → Alph' i) → Bool}
    (hc : (∀ y z, f y = f z) → ∀ y z, g y = g z)
    (hM : M ≤ M') (hA : maxAlph Alph ≤ maxAlph Alph') :
    sandwichQ g ≤ sandwichQ f := by
  by_cases hg : ∀ y z, g y = g z
  · rw [sandwichQ_const g hg]; exact sandwichQ_nonneg f
  · rw [sandwichQ_nonconst g hg, sandwichQ_nonconst f (fun hf => hg (hc hf))]
    exact mul_le_mul
      (Real.rpow_le_rpow (by positivity) (by exact_mod_cast hM) (by norm_num))
      (Real.rpow_le_rpow (by positivity) (by exact_mod_cast hA) (by norm_num))
      (by positivity) (by positivity)

theorem sandwichQ_Claw {n κ : ℕ} (hκ : 2 ≤ κ) (hn : 1 ≤ n) :
    sandwichQ (Claw n κ) = ((2 * n : ℕ) : ℝ) ^ (1 / 2 : ℝ) * (κ : ℝ) ^ (1 / 4 : ℝ) := by
  rw [sandwichQ_nonconst _ (Claw_nonconst n κ hκ hn), maxAlph_const (by omega) (Fin κ),
    Nat.card_fin]

/-- The witness satisfies the claw bound of `thm:abi` / `thm:tani` with `cABI = 1`. -/
theorem claw_bound {n κ : ℕ} (hκ : 2 ≤ κ) (hn : 1 ≤ n) :
    (1 : ℝ) * Real.sqrt n * (κ : ℝ) ^ (1 / 6 : ℝ) ≤ sandwichQ (Claw n κ) := by
  rw [sandwichQ_Claw hκ hn, one_mul, Real.sqrt_eq_rpow]
  refine mul_le_mul ?_ ?_ (by positivity) (by positivity)
  · exact Real.rpow_le_rpow (by positivity)
      (by exact_mod_cast Nat.le_mul_of_pos_left n (by norm_num)) (by norm_num)
  · exact Real.rpow_le_rpow_of_exponent_le (by exact_mod_cast (by omega : 1 ≤ κ)) (by norm_num)

/-- `2Sum_{Z_q,t,N}` is genuinely nonconstant once `N ≥ 2` and `q ≥ 3`: a string with `x_0 = t`
and every other coordinate `0` is a YES instance, and a constant string at a value `v` with
`v + v ≠ t` is a NO instance.  (No oddness of `q` is needed for this; the `Odd q` of `B4bClaim`
is there for a different reason — it is the regime `thm:main-odd` states.) -/
theorem twoSum_nonconst {N q : ℕ} [NeZero q] (hN : 2 ≤ N) (hq : 3 ≤ q) (t : ZMod q) :
    ¬ ∀ y z : Fin N → ZMod q, twoSum (ZMod q) t N y = twoSum (ZMod q) t N z := by
  classical
  intro h
  have hi0 : (0 : ℕ) < N := by omega
  have hi1 : (1 : ℕ) < N := by omega
  have hne : (⟨0, hi0⟩ : Fin N) ≠ ⟨1, hi1⟩ := by simp [Fin.ext_iff]
  obtain ⟨v, hv⟩ : ∃ v : ZMod q, v + v ≠ t := by
    by_cases h0 : (0 : ZMod q) + 0 = t
    · refine ⟨1, ?_⟩
      rw [add_zero] at h0
      rw [← h0]
      have hcast : ((2 : ℕ) : ZMod q) = (1 : ZMod q) + 1 := by push_cast; ring
      have hval : ((2 : ℕ) : ZMod q).val = 2 := ZMod.val_natCast_of_lt (by omega)
      intro hzero
      rw [hcast, hzero] at hval
      simp at hval
    · exact ⟨0, h0⟩
  have hYes : twoSum (ZMod q) t N (fun i => if i = (⟨0, hi0⟩ : Fin N) then t else 0) = true := by
    rw [twoSum_eq_decide, decide_eq_true_eq]
    exact ⟨⟨0, hi0⟩, ⟨1, hi1⟩, hne, by simp [hne.symm]⟩
  have hNo : twoSum (ZMod q) t N (fun _ => v) = false := by
    rw [twoSum_eq_decide, decide_eq_false_iff_not]
    rintro ⟨i, j, -, hij⟩
    exact hv hij
  rw [h (fun i => if i = (⟨0, hi0⟩ : Fin N) then t else 0) (fun _ => v), hNo] at hYes
  exact Bool.noConfusion hYes

theorem sandwichQ_twoSum {N q : ℕ} [NeZero q] (hN : 1 ≤ N) (t : ZMod q)
    (h : ¬ ∀ y z, twoSum (ZMod q) t N y = twoSum (ZMod q) t N z) :
    sandwichQ (twoSum (ZMod q) t N) = (N : ℝ) ^ (1 / 2 : ℝ) * (q : ℝ) ^ (1 / 4 : ℝ) := by
  rw [sandwichQ_nonconst _ h, maxAlph_const hN (ZMod q), Nat.card_zmod]

/-- **`QueryModel` is inhabited by an alphabet-aware witness.**  All nine fields are discharged;
`relabel` holds with constant `1`, so the factor-2 slack is untested by this model. -/
noncomputable def sandwichModel : QueryModel where
  Q := fun f => sandwichQ f
  restrict := by
    intro M Alph inst D f
    exact sandwichQ_le_of (fun hf y z => hf _ _) (le_refl M) (maxAlph_subtype_le D)
  relabel := by
    intro M Alph Alph' inst inst' e f
    have h1 : sandwichQ (fun y => f fun i => e i (y i)) ≤ sandwichQ f :=
      sandwichQ_le_of (fun hf y z => hf _ _) (le_refl M) (maxAlph_equiv_le e)
    have h2 : (0 : ℝ) ≤ sandwichQ f := sandwichQ_nonneg f
    show sandwichQ (fun y => f fun i => e i (y i)) ≤ 2 * sandwichQ f
    linarith
  freeze := by
    intro M Alph inst a f
    exact sandwichQ_le_of (fun hf y z => hf _ _) (Nat.le_succ M) (maxAlph_castSucc_le Alph)
  constQ := by
    intro M Alph inst f b hb
    exact sandwichQ_const f (fun y z => by rw [hb y, hb z])
  cABI := 1
  cABI_pos := one_pos
  abi := by
    intro n κ h2 hn
    exact claw_bound h2 (by omega)
  tani := by
    intro n κ h2 hn
    exact claw_bound h2 (by omega)

/-- The witness satisfies the UPPER side, `KSUM.B4a.Claim`, with `C_ε = 1` and `N₀ = 1` — for
every `ε > 0`, since `N^{1/2} ≤ N^{1/2+ε}` at `N ≥ 1`. -/
theorem sandwich_B4a : KSUM.B4a.Claim sandwichModel := by
  intro ε hε
  refine ⟨1, one_pos, 1, ?_⟩
  intro N q _inst hN _hq t
  show sandwichQ (twoSum (ZMod q) t N) ≤ 1 * (N : ℝ) ^ (1 / 2 + ε) * (q : ℝ) ^ (1 / 4 : ℝ)
  by_cases h : ∀ y z, twoSum (ZMod q) t N y = twoSum (ZMod q) t N z
  · rw [sandwichQ_const _ h]
    positivity
  · rw [sandwichQ_twoSum hN t h, one_mul]
    refine mul_le_mul_of_nonneg_right ?_ (by positivity)
    exact Real.rpow_le_rpow_of_exponent_le (by exact_mod_cast hN) (by linarith)

/-- The witness satisfies the LOWER side, `B4bClaim`, with `c = 1`: in the regime `q` odd,
`5 ≤ q ≤ N`, the function is nonconstant, so its value is exactly `N^{1/2}q^{1/4}`. -/
theorem sandwich_B4b : B4bClaim sandwichModel := by
  refine ⟨1, one_pos, 0, ?_⟩
  intro N q _inst _hN _hodd hq5 hqN t
  have hnc := twoSum_nonconst (N := N) (q := q) (by omega) (by omega) t
  show (1 : ℝ) * (N : ℝ) ^ (1 / 2 : ℝ) * (q : ℝ) ^ (1 / 4 : ℝ) ≤ sandwichQ (twoSum (ZMod q) t N)
  rw [sandwichQ_twoSum (by omega) t hnc, one_mul]

/-- **`KSUM.B4.composition` is NOT vacuous.**  Its two hypotheses are jointly satisfiable, so the
sandwich is a statement about a nonempty class of models.  This says nothing about whether the
true `Q` satisfies them — `B4bClaim` is the open `k = 2` lower bound. -/
theorem sandwich_nonvacuous : Claim sandwichModel :=
  composition sandwichModel sandwich_B4a sandwich_B4b

end KSUM.B4
