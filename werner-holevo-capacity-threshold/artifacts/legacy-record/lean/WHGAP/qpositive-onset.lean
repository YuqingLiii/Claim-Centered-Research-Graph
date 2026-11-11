import WHGAP.«no-ascent-hierarchy»

/-!
# `WHGAP.qpositive-onset` (P3)

* node id: `WHGAP.qpositive-onset`
* node file: `channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.qpositive-onset.md`
* epistemic status on disk (2026-07-30): **CERTIFIED\***; its imported theorem
  (`Q > 0` on `(0, 2/5)`) is PROVED (R5d, LICENSE A).
* mechanization state: `composition-checked` rel `{LSD/Devetak via the interface}`.
* DAG parent: `WHGAP.goal`; DAG child: `WHGAP.no-ascent-hierarchy` (imported).

## Frozen Claim (verbatim from the node file, `## Claim` section)

Determine the small-x threshold below which Q(Lambda_x) > 0 (value or bounds for the onset of
positive quantum capacity in the noisy Werner–Holevo family). **[CERTIFIED\* — best PROVED
bound now: Q(Lambda_x) > 0 for ALL x in (0, 2/5) (R5d-reviewed Theorem 8.1 of the N1'
expansion-lemma note, 2026-07-30), subsuming the R4-reviewed (0, x_1) package and the
783/2000 witness. The undetermined strip is exactly [2/5, 1/2); the exact onset value
remains OPEN — see [[WHGAP.onset-two-fifths]].]**

* frozen-claim SHA-256: `a3f1e418592cbfeb858ffb340b5c60cbc99bda247642ae2b77e9cbfa63568cfa`

## Statement-fidelity note (G-L5)

The prose Claim is a *determination* task ("determine the small-x threshold"), whose current
PROVED content is the interval statement `Q(Λ_x) > 0 for all x ∈ (0, 2/5)`.  `Claim I` below
is exactly that interval statement.  Granularity loss: the node's residual scope — the exact
onset value, the `x_1`/`x_H` numerics, the two-letter null — is not represented at all;
`WHGAP.onset-two-fifths` carries the onset question separately.

`composition` is the Lean translation of the node's `composition:` block: it consumes the
P9 tier-1 shadow and the interface's LSD/Devetak achievability field, and nothing else.
-/

namespace WHGAP.«qpositive-onset»

open WHGAP

/-- **P3 Claim, tier-1 form.**  `Q(Λ_x) > 0` for every `x ∈ (0, 2/5)`. -/
def Claim (I : CapacityInterface) : Prop :=
  ∀ x : ℝ, 0 < x → x < 2 / 5 → 0 < I.Q x

/-- **Composition theorem for P3** (DAG protocol §7.4).  P9's positive coherent-information
witnesses plus the cited LSD/Devetak achievability give `Q > 0` on the whole interval. -/
theorem composition (I : CapacityInterface)
    (h9 : «no-ascent-hierarchy».Claim I) : Claim I := by
  intro x hx0 hx
  obtain ⟨c, hc, hIc⟩ := h9 x hx0 hx
  exact I.q_pos_of_ic_pos x c hc hIc

end WHGAP.«qpositive-onset»

