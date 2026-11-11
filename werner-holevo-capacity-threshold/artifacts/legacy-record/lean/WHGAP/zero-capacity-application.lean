import WHGAP.«signed-lift-extension»

/-!
# `WHGAP.zero-capacity-application` (P4)

* node id: `WHGAP.zero-capacity-application`
* node file:
  `channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.zero-capacity-application.md`
* epistemic status on disk (2026-07-30): **PROVED** (R3 licensing statement 1).
* mechanization state: `composition-checked` rel `{ZW Thm 3.3 / Lem 3.2 / Cor 3.7, BGSW25,
  HRSF22 Lem 3.1 via ZW, Llo97/Dev05}` — all four bundled in `CapacityInterface.zw_hrsf_zero`.
* DAG parent: `WHGAP.goal`; DAG child: `WHGAP.signed-lift-extension` (imported).

## Frozen Claim (verbatim from the node file, `## Claim` section)

For every x in [1/2, 1), Q(Lambda_x) = P(Lambda_x) = 0 — assembled from the R2-PROVED covariant
lift family (defect-PSD on [1/2,1), unique residual point) through the generic Zhu–Wang
machinery (Theorem 3.3, Lemma 3.2, Corollary 3.7) and HRSF22 hybrid tensorization, explicitly
discharging the seven obligations enumerated in R2 review claim 9. **[PROVED — R3 licensing
statement 1; provenance note: HRSF22 tensorization verified through the local Zhu–Wang
statement, no local HRSF22 copy audited. The [1/2,1] Corollary sits at CERTIFIED\* (RK24
endpoint cite-only); the (1/2,4/7) gap-closure substatement is inside the PROVED scope.]**

* frozen-claim SHA-256: `8be43283510eb60ce3f617da0df2fec2832c5b8e4f6f6b5a6ce52bd5973326da`

## Statement-fidelity note (G-L5)

`Claim I` is `∀ x ∈ [1/2, 1), Q x = 0 ∧ P x = 0` — the prose Claim's theorem, verbatim in
scope (half-open interval, both capacities).  Granularity loss: (i) "at every blocklength" is
invisible, because `Q`/`P` are already the regularized objects and `Qone`/`Pone` the one-shot
ones — the tensorization step lives *inside* the cited interface field `zw_hrsf_zero`, which
is precisely the honest place for it; (ii) the seven R2 obligations and the HRSF22-via-ZW
provenance note are documentation, not Lean content; (iii) the closed-interval Corollary
`[1/2,1]` (CERTIFIED\*, cite-only RK24 endpoint) is deliberately **not** stated, since its
endpoint rests on a citation this development does not carry.
-/

namespace WHGAP.«zero-capacity-application»

open WHGAP

/-- **P4 Claim, tier-1 form.**  `Q(Λ_x) = P(Λ_x) = 0` for every `x ∈ [1/2, 1)`. -/
def Claim (I : CapacityInterface) : Prop :=
  ∀ x : ℝ, 1 / 2 ≤ x → x < 1 → I.Q x = 0 ∧ I.P x = 0

/-- **Composition theorem for P4** (DAG protocol §7.4).  This is the R3-reviewed assembly
note's logic: P2 gives the CP-defect signed lift on `[1/2,1)`, and the cited Zhu–Wang /
HRSF22 criterion turns it into vanishing capacities. -/
theorem composition (I : CapacityInterface)
    (h2 : «signed-lift-extension».Claim I) : Claim I := by
  intro x hx1 hx2
  obtain ⟨-, -, hQ, hP⟩ := I.zw_hrsf_zero x (h2 x hx1 hx2)
  exact ⟨hQ, hP⟩

/-- The one-shot conclusion is also available from the same interface field, at every `x` in
the interval — recorded because the prose Claim's "at every blocklength" reading is what
`Qone`/`Pone` stand for. -/
theorem composition_one_shot (I : CapacityInterface)
    (h2 : «signed-lift-extension».Claim I) :
    ∀ x : ℝ, 1 / 2 ≤ x → x < 1 → I.Qone x = 0 ∧ I.Pone x = 0 := by
  intro x hx1 hx2
  obtain ⟨hQ1, hP1, -, -⟩ := I.zw_hrsf_zero x (h2 x hx1 hx2)
  exact ⟨hQ1, hP1⟩

end WHGAP.«zero-capacity-application»

