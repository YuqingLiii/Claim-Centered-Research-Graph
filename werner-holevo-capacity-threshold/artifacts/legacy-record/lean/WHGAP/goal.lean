import WHGAP.«qpositive-onset»
import WHGAP.«zero-capacity-application»
import WHGAP.«onset-two-fifths»

/-!
# `WHGAP.goal` (G) — the union assembly

* node id: `WHGAP.goal`
* node file: `channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.goal.md`
* epistemic status on disk (2026-07-30): **OPEN** — "resolved except on `[2/5, 1/2)`",
  the cap coming from the CONJECTURED child `WHGAP.onset-two-fifths`.
* mechanization state: `composition-checked`; `rel`: `P13` (its `Claim I S` is a hypothesis,
  exactly as the node's `composition.rel` says), plus `hS : S ⊆ [2/5, 1/2)`.
* DAG children (status-propagating, = this module's node imports): `WHGAP.qpositive-onset`,
  `WHGAP.zero-capacity-application`, `WHGAP.onset-two-fifths`.

## Frozen Claim (verbatim from the node file, `## Claim` section)

Determine {x : Q(Lambda_x) = 0} for the qutrit family Lambda_x(X) = (1-x) X + (x/2)(Tr(X) 1 - X^T); close the gap x in (1/2, 4/7). **[OPEN]**

* frozen-claim SHA-256: `f3a95693d4b0de4409d1fe4267e436bf3fe419f84b8a5fc2ebc6e06d6939ce99`

## Statement-fidelity note (G-L5)

`Claim I S` below is the *first* clause of the prose Claim — the determination
`{x ∈ (0,1) : Q(Λ_x) = 0} = [1/2, 1) ∪ S` — in the exact form the node's `composition:` block
states it.  Differences from the prose, all deliberate:

* the prose says "close the gap `x ∈ (1/2, 4/7)`" as a second clause; that substatement is
  strictly inside `[1/2,1)` and hence inside the `Claim`, so it is not stated separately;
* the `x = 1` endpoint is **excluded**: on disk it sits at CERTIFIED\* through a cite-only
  RK24 dependency (or the paper's Lemma 4.1), so it must not enter a machine-checked
  composition;
* `S` and the hypothesis `hS : S ⊆ [2/5, 1/2)` make the still-open strip visible in the
  theorem type instead of hiding it.

`composition` is a **complete, unconditional Lean proof of the assembly logic**: given the
three children's tier-1 Claims it derives the set equality outright.  It is *not* a proof of
the goal — the goal is OPEN precisely because `«onset-two-fifths».Claim I S` is a conjecture,
and it appears here as a hypothesis.
-/

namespace WHGAP.goal

open WHGAP

/-- **G Claim, tier-1 form.**  The zero-quantum-capacity set of the family on `(0,1)` is
`[1/2, 1) ∪ S`, where `S` is the (still undetermined) zero set inside the strip `[2/5, 1/2)`. -/
def Claim (I : CapacityInterface) (S : Set ℝ) : Prop :=
  {x : ℝ | x ∈ Set.Ioo (0:ℝ) 1 ∧ I.Q x = 0} = Set.Ico (1 / 2 : ℝ) 1 ∪ S

/-- **The goal composition theorem (MUST-LAND).**  `(0,1)` is the disjoint union of
`(0, 2/5)`, `[2/5, 1/2)` and `[1/2, 1)`; P3 empties the first piece, P4 fills the third, and
P13 identifies the second with `S`.  Proved outright from the three tier-1 Claims. -/
theorem composition (I : CapacityInterface) (S : Set ℝ)
    (hS : S ⊆ Set.Ico (2 / 5 : ℝ) (1 / 2))
    (h3 : «qpositive-onset».Claim I)
    (h4 : «zero-capacity-application».Claim I)
    (h13 : «onset-two-fifths».Claim I S) :
    Claim I S := by
  unfold Claim
  ext x
  simp only [Set.mem_setOf_eq, Set.mem_union, Set.mem_Ioo, Set.mem_Ico]
  constructor
  · rintro ⟨⟨hx0, hx1⟩, hQ⟩
    by_cases hlt : x < (1 / 2 : ℝ)
    · by_cases hlt2 : x < (2 / 5 : ℝ)
      · exact absurd hQ (h3 x hx0 hlt2).ne'
      · push_neg at hlt2
        exact Or.inr ((h13 x hlt2 hlt).mp hQ)
    · push_neg at hlt
      exact Or.inl ⟨hlt, hx1⟩
  · rintro (⟨hge, hx1⟩ | hxS)
    · exact ⟨⟨by linarith, hx1⟩, (h4 x hge hx1).1⟩
    · have hmem := hS hxS
      rw [Set.mem_Ico] at hmem
      obtain ⟨hge2, hlt⟩ := hmem
      exact ⟨⟨by linarith, by linarith⟩, (h13 x hge2 hlt).mpr hxS⟩

/-- Corollary of the same assembly, recorded because it is the sentence the manuscript
actually prints: if the strip turns out to be entirely zero-capacity (`S = [2/5, 1/2)`, the
`WHGAP.onset-two-fifths` conjecture), the zero set on `(0,1)` is `[2/5, 1)`. -/
theorem composition_conjectured (I : CapacityInterface)
    (h3 : «qpositive-onset».Claim I)
    (h4 : «zero-capacity-application».Claim I)
    (h13 : «onset-two-fifths».Claim I «onset-two-fifths».conjecturedS) :
    {x : ℝ | x ∈ Set.Ioo (0:ℝ) 1 ∧ I.Q x = 0} = Set.Ico (2 / 5 : ℝ) 1 := by
  have h := composition I «onset-two-fifths».conjecturedS (by
    unfold «onset-two-fifths».conjecturedS; exact subset_rfl) h3 h4 h13
  rw [Claim] at h
  rw [h]
  unfold «onset-two-fifths».conjecturedS
  ext x
  simp only [Set.mem_union, Set.mem_Ico]
  constructor
  · rintro (⟨h1, h2⟩ | ⟨h1, h2⟩) <;> constructor <;> linarith
  · rintro ⟨h1, h2⟩
    by_cases hlt : x < (1 / 2 : ℝ)
    · exact Or.inr ⟨h1, hlt⟩
    · push_neg at hlt
      exact Or.inl ⟨hlt, h2⟩

end WHGAP.goal

