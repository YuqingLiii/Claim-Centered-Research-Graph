/-
`SE/denom/Phi/legal/trace/t6.lean` — linked node module.
This is obligation **H1** of the paper's Conjecture H.

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : SE.denom.Phi.legal.trace.t6      (alias `T6`)
node file      : se/proof-dag/nodes/SE.denom.Phi.legal.trace.t6.yaml
decomposition / role    : none / proof
epistemic status (read from the node file on 2026-07-30): **OPEN**
mechanization  : stated (hypothesis only — nothing is proved about it here)
claim_hash     : sha256:5c485604043a9c72f2c29ec2e23b051884a27e9e6b22c86993a320951231b0bd
                 (SHA-256 of the frozen Claim text quoted below, UTF-8, LF, stripped)

FROZEN CLAIM (verbatim from `claim.statement` in the node file):

  For every admissible strict sector, prove the multiplicity-block PSD bound

  `M_xi <= (15/4) B_theta(q)^2 omega I_c`.

  Here the raw physical joint trace is

  `J = omega^2 rawT_a + rawT_b = d Tr(M_xi)`,

  with `d=f^kappa f^nu`. A sufficient scalar target is

  `(CT) J <= (15/4) B_theta(q)^2 omega d`,

  and the stronger assembly target is

  `(JT) J <= B_theta(q)^2 T (omega^2+1/(delta_min+1))`.

  All physical long-tail and tail-tail cross terms vanish because the output
  projectors are orthogonal. T6 is therefore a weighted joint-energy route, not
  a cross-term-cancellation route.

  (Indentation added only to nest the quote inside this comment; the hash above is of the
  UNINDENTED node text.)

────────────────────────────────────────────────────────────────────────────────────────────────
TIER-1 SHADOW — what `Claim` below actually says.

Tier 1 has no operator layer (`SE.SEFrame` is real-valued), so the PSD statement
`M_ξ ⪯ (15/4)·B_θ(q)²·ω·I_c` is represented by its NORM consequence
`‖M_ξ‖ ≤ (15/4)·B_θ(q)²·ω`, which — together with `M_ξ ⪰ 0`, carried as the cited field
`SE.SEFrame.Cited.mxi_nonneg` — is exactly what the assembly consumes.  The implication runs the
SAFE way: the frozen Claim implies this shadow, so a theorem proved from the shadow is proved from
the Claim.  The converse fails.

The joint-trace identity `J = ω² rawT_a + rawT_b = d·Tr(M_ξ)` and the scalar targets `(CT)`/`(JT)`
are NOT representable at tier 1 (they need the TRACE of the block, not its norm) and are therefore
NOT assumed here; the assembly does not use them.

`Claim` is a hypothesis. Nothing in this development proves it, and a green build says nothing
about its truth.

No `sorry`.
-/
import SE.Interface

namespace SE.denom.Phi.legal.trace.t6

section
variable (F : SE.SEFrame)

/-- **(H1)** tier-1 shadow of `SE.denom.Phi.legal.trace.t6`: for every admissible strict sector,
`‖M_ξ‖ ≤ (15/4)·B_θ(q)²·ω`. -/
def Claim : Prop :=
  ∀ n j s, F.admissible n j s →
    F.mxiS n j s ≤ 15 / 4 * (F.btheS n j s) ^ 2 * F.omegaS n j s

end

end SE.denom.Phi.legal.trace.t6
