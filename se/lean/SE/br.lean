/-
`SE/br.lean` — linked node module.
Branch A: the tapered BR witness restricted to legal `q = 2n` — numerator over denominator.

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : SE.br      (alias `BR`)
node file      : se/proof-dag/nodes/SE.br.yaml
decomposition / role    : AND / proof
children       : def, num, denom (three)
epistemic status (read from the node file on 2026-07-30): **OPEN**
composition status on the node: **PROVED** ("one division; the executed instance is
                 certification A.33, confirmed by the second external review without reservation")
mechanization  : composition-checked, relative to Cited + denom.Claim
claim_hash     : sha256:2e795bb6962a6da9ebcd384fc11801f7940abc727a2fda6e38388d1744c16735
                 (SHA-256 of the frozen Claim text quoted below, UTF-8, LF, stripped)

FROZEN CLAIM (verbatim from `claim` in the node record):

  SE.br — Branch A: BR tapered witness restricted to legal q=2n (AND)

────────────────────────────────────────────────────────────────────────────────────────────────
WHAT `Claim` BELOW RENDERS.  The node's prose composition block concludes

  `‖Γ_n‖ / max_i ‖Γ_n∘Δ_i‖ ≥ K/C = Ω(n^{1/3})`;

`Claim` states exactly that RATIO bound, quantitatively (`C = 2·envBound ρ_const n`, explicit,
`n ≥ 27`).  It deliberately stops at the ratio: the passage ratio → `Adv±` is the cited
Høyer–Lee–Špalek adversary interface and belongs to the GOAL route proof
(`SE.goal.composition_via_br`), exactly as the prose composition block on `SE.goal.yaml` draws the
boundary.

────────────────────────────────────────────────────────────────────────────────────────────────
PREMISE DECLARATION (the current DAG premise rules; same mechanism as rulings R3/R4).

Children and how each enters `composition`:

  * `denom` — CHILD, consumed as `denom.Claim` (the only Claim parameter);
  * `num`   — CHILD, node `SE.br.num` (PROVED on disk): enters as the CITED field
              `Cited.numerator` (`‖Γ_n‖ ≥ K`, paper `lem:numerator`).  Tier 1 has no `Γ_n`
              matrix, so the PROVED lemma is cited, not reproved;
  * `def`   — CHILD, node `SE.br.def` (PROVED on disk): the construction of `Γ_n` itself has no
              tier-1 rendering (no operator layer).  Its content enters twice: the abstract
              carrier fields (`gammaNorm`, `maskNorm`) stand in for the constructed matrix, and
              the nonzero-mask fact is the CITED field `Cited.maskNorm_pos` (the exact
              `(2n-1)/(2n)` row norm, certification "Independent-construction checks").

Declared here, in `SE/Trust.lean` §D, and in the node's `lean.rel` field.

No `sorry`.  A green build says the DIVISION is machine-checked; ALL the difficulty sits in its
inputs (node file: "A green composition with an open input proves nothing about the node").
-/
import SE.denom

namespace SE.br

section
variable (F : SE.SEFrame)

/-- The node's Lean claim — the RATIO bound of the node's composition block, with the explicit
denominator constant: **`K/(2·envBound) ≤ ‖Γ_n‖ / max_i ‖Γ_n∘Δ_i‖`** for `n ≥ 27`.
The step from this ratio to `Adv±` is the goal route's cited interface, not part of this node. -/
def Claim : Prop :=
  ∀ n : ℕ, 27 ≤ n →
    (SE.K n : ℝ) / (2 * SE.envBound SE.rhoConst n) ≤ F.gammaNorm n / F.maskNorm n

end

section
variable {F : SE.SEFrame}

/-- **The node's composition theorem** (§7.4): Cited ∧ denom ⟹ `Claim` — the "one division" of
the node's prose block (`‖Γ_n‖ ≥ K` cited from `num`, `maskNorm > 0` cited from `def`,
`maskNorm ≤ 2·envBound` from the `denom` child). -/
theorem composition (hC : F.Cited) (hdenom : denom.Claim F) : Claim F := by
  intro n hn
  have hE : 0 < SE.envBound SE.rhoConst n := envBound_pos SE.rhoConst_nonneg hn
  have hE2 : (0 : ℝ) < 2 * SE.envBound SE.rhoConst n := by linarith
  have hmpos : 0 < F.maskNorm n := hC.maskNorm_pos n (by omega)
  have hmask : F.maskNorm n ≤ 2 * SE.envBound SE.rhoConst n := hdenom n hn
  have hnum : (SE.K n : ℝ) ≤ F.gammaNorm n := hC.numerator n
  have hK0 : (0 : ℝ) ≤ (SE.K n : ℝ) := Nat.cast_nonneg _
  rw [div_le_div_iff₀ hE2 hmpos]
  nlinarith [mul_nonneg hE2.le (sub_nonneg.mpr hnum), mul_nonneg hK0 (sub_nonneg.mpr hmask)]

end

end SE.br
