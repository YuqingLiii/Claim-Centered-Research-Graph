/-
`SE/denom/Phi/legal/omega/interface.lean` — linked node module.
This is obligation **H3** of the paper's Conjecture H.

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : SE.denom.Phi.legal.omega.interface      (alias `OMI`)
node file      : se/proof-dag/nodes/SE.denom.Phi.legal.omega.interface.yaml
decomposition / role    : none / proof
epistemic status (read from the node file on 2026-07-30): **CONJECTURED**
mechanization  : stated (hypothesis only — nothing is proved about it here)
claim_hash     : sha256:5d62b12d5112c0f004d75bf42f01143b1e3004825602d80a4bff9eb7f85f0fb7
                 (SHA-256 of the frozen Claim text quoted below, UTF-8, LF, stripped)

FROZEN CLAIM (verbatim from `claim` in the node record):

  SE.denom.Phi.legal.omega.interface — **H3, the ω-decay operator interface**, exactly
  the paper's hypothesis: for every admissible strict sector, (i) the exact sandwich
  `C_{λ,ξ}^* C_{λ,ξ} = C_{N,prob}^{1/2} · G_can^{λ,ξ} · C_{N,prob}^{1/2}` and (ii) the
  full-multiplicity NO polar `C_{N,prob} = r_top·ω · I_{H_ξ}` (acting as a scalar on every LR
  copy). Nothing more: the downstream `‖C_{j+1→j}‖ ≤ √(15/8)·r_top·√(j/(n−j))` bound and the
  Theorem-B constant belong to the PARENT node as consequences of H1∧H2∧H3∧H4.

  (Indentation added only to nest the quote inside this comment; the hash above is of the
  UNINDENTED node text.)

────────────────────────────────────────────────────────────────────────────────────────────────
TIER-1 SHADOW — what `Claim` below actually says.

`Claim` is the conjunction of the tier-1 shadows of (i) and (ii), matching the node's own two-part
statement:

* (i) the manuscript's proof of `lem:omega-lower` uses the exact sandwich only through
  `‖C_{λ,ξ}‖² ≤ ‖C_{N,prob}‖·‖𝖦_can^{λ,ξ}‖`, the submultiplicative consequence of the displayed
  identity.  That consequence — an INEQUALITY, weaker than the frozen identity — is what is
  assumed, so the implication again runs the safe way.
* (ii) `C_{N,prob} = r_top·ω·I` gives `‖C_{N,prob}‖ = r_top·ω`, an equality, stated as such.

`Claim` is a hypothesis. Nothing in this development proves it, and a green build says nothing
about its truth.

No `sorry`.
-/
import SE.Interface

namespace SE.denom.Phi.legal.omega.interface

section
variable (F : SE.SEFrame)

/-- **(H3)** tier-1 shadow of `SE.denom.Phi.legal.omega.interface`, both parts:

* `sandwich`: `‖C̃_{λ,ξ}‖² ≤ ‖C_{N,prob}‖·‖𝖦_can^{λ,ξ}‖` (consequence of the exact sandwich);
* `polar`: `‖C_{N,prob}‖ = r_top·ω` (the full-multiplicity NO polar). -/
def Claim : Prop :=
  (∀ n j s, F.admissible n j s →
      (F.csectS n j s) ^ 2 ≤ F.cnprobS n j s * F.gcanS n j s) ∧
    (∀ n j s, F.admissible n j s →
      F.cnprobS n j s = F.rtopS n j s * F.omegaS n j s)

end

end SE.denom.Phi.legal.omega.interface
