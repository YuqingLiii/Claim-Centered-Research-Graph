/-
`SE/denom/Phi/legal/gram/interface.lean` — linked node module.
This is obligation **H2** of the paper's Conjecture H.

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : SE.denom.Phi.legal.gram.interface      (alias `GRAMI`)
node file      : se/proof-dag/nodes/SE.denom.Phi.legal.gram.interface.yaml
decomposition / role    : none / proof
epistemic status (read from the node file on 2026-07-30): **CONJECTURED**
mechanization  : stated (hypothesis only — nothing is proved about it here)
claim_hash     : sha256:f8848b614b32dec79f3ca65ee5acd43777762429d490232490c17d1dbb40f0d7
                 (SHA-256 of the frozen Claim text quoted below, UTF-8, LF, stripped)

FROZEN CLAIM (verbatim from `claim` in the node record):

  SE.denom.Phi.legal.gram.interface — **H2, the canonical-coefficient interface
  identity, in the TYPED (Schur-lifted) form**: for every admissible strict sector,

  `G_can^full |_{H_ξ} = I_{V_κ⊗V_ν} ⊗ [ r_top(q,j,θ) / (B_θ(q)²·ω) ] · M_ξ`

  as operators on the whole H-isotypic carrier `H_ξ = V_κ⊗V_ν⊗C^c`, all `c` copies carried by the
  single multiplicity trace `𝔪_ξ`, no lost factor `c`. (This is the paper's H2 with the
  `I_{V_κ⊗V_ν}` lift restored per external review T2-G2 — the lift the paper's own eq:Htwirl
  carries and eq:gcan1/gcan2 had dropped.)

  (Indentation added only to nest the quote inside this comment; the hash above is of the
  UNINDENTED node text.)

────────────────────────────────────────────────────────────────────────────────────────────────
TIER-1 SHADOW — what `Claim` below actually says, and the ONE THING IT LOSES.

Taking operator norms of the frozen identity and using `‖Id ⊗ X‖ = ‖X‖` gives the scalar identity
`‖𝖦_can^{λ,ξ}‖ = [r_top/(B_θ(q)²·ω)]·‖M_ξ‖`, which is what `Claim` states and what the assembly
consumes.

**The Schur lift `I_{V_κ⊗V_ν} ⊗ (·)` — the exact type-level content that external review finding
T2-G2 restored — is INVISIBLE in this shadow**, because it acts as an isometry on norms.  A
MIS-TYPED H2 (the failure mode that six same-stack reviews missed and one cross-stack review
caught) would therefore NOT be caught by this development.  Catching it needs tier 3
(hook length formula, Littlewood–Richardson/Pieri), which is not started.

`Claim` is a hypothesis. Nothing in this development proves it, and a green build says nothing
about its truth.

No `sorry`.
-/
import SE.Interface

namespace SE.denom.Phi.legal.gram.interface

section
variable (F : SE.SEFrame)

/-- **(H2)** tier-1 shadow of `SE.denom.Phi.legal.gram.interface`: for every admissible strict
sector, `‖𝖦_can^{λ,ξ}‖ = [r_top(q,j,θ)/(B_θ(q)²·ω)]·‖M_ξ‖`.

The `I_{V_κ⊗V_ν}` lift of the frozen Claim is not representable here — see the module header. -/
def Claim : Prop :=
  ∀ n j s, F.admissible n j s →
    F.gcanS n j s
      = F.rtopS n j s / ((F.btheS n j s) ^ 2 * F.omegaS n j s) * F.mxiS n j s

end

end SE.denom.Phi.legal.gram.interface
