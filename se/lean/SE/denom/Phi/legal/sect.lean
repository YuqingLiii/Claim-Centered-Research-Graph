/-
`SE/denom/Phi/legal/sect.lean` — linked node module.
This is obligation **H4** of the paper's Conjecture H — the one that was MISSING until 2026-07-29.

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : SE.denom.Phi.legal.sect      (alias `SECT`)
node file      : se/proof-dag/nodes/SE.denom.Phi.legal.sect.yaml
decomposition / role    : none / proof
epistemic status (read from the node file on 2026-07-30): **OPEN**
mechanization  : stated (hypothesis only — nothing is proved about it here)
claim_hash     : sha256:11131e8cf92d4988213466c621c6bfa53148f177d303066942100a561b9899d5
                 (SHA-256 of the frozen Claim text quoted below, UTF-8, LF, stripped)

FROZEN CLAIM (verbatim from `claim` in the node record):

  SE.denom.Phi.legal.sect — **H4: exhaustive Schur sectorization of the actual legal lower
  block.** For every active `j`, the actual legal lower block `C_{j+1→j}` is an intertwiner for
  `S_q` and the fixed-query-position subgroup `H = S_{n-1}×S_n`, and on the actual legal NO/YES
  spaces it admits an ORTHOGONAL, EXHAUSTIVE decomposition

  `C_{j+1→j} ≅ ⊕_{λ=(q−j,θ)} I_{S^λ} ⊗ ⊕_{ξ=(κ,ν) admissible} ( I_{V_κ⊗V_ν} ⊗ C̃_{λ,ξ} )`

  with NO residual sectors, where the `c×c` blocks of H2/H3 are exactly the Gram/NO-polar blocks of
  these `C̃_{λ,ξ}`; consequently `‖C_{j+1→j}‖ = max_{λ,ξ} ‖C̃_{λ,ξ}‖`, uniformly for every LR
  multiplicity `c ≥ 1`. (Frozen statement as supplied by the external review T3-G1; the Schur
  identity lift `I_{V_κ⊗V_ν} ⊗ (·)` is the same lift H2 requires per T2-G2.)

  (Indentation added only to nest the quote inside this comment; the hash above is of the
  UNINDENTED node text.)

────────────────────────────────────────────────────────────────────────────────────────────────
TIER-1 SHADOW — what `Claim` below actually says, and what it LOSES.
(Re-quantified 2026-07-30 per §7.10 review finding F1, `se/reviews/se_lean_t1_review_20260730.md`.)

**Quantifier scope.**  The frozen Claim asserts the sectorization "for every ACTIVE `j`".
"Active `j`" is a term of art that resolves through the manuscript: Conjecture H's preamble fixes
`j ≥ 1` and `n ≥ 3j` (`se_explicit_witness.tex`, `conj:H` preamble), and the proposition that
consumes H4 (`lem:omega-lower` (ii)) is scoped `1 ≤ j < K−1`.  `Claim` below is therefore
quantified over EXACTLY that window — `1 ≤ j`, `3j ≤ n`, `j < K n − 1` — so that the frozen Claim
implies the shadow.  (An earlier revision of this module quantified over ALL `(n, j)`, which the
frozen Claim does not cover at `j = 0` or `j ≥ K−1`; that over-quantification was review finding
F1 and is corrected here.  The node file itself is unchanged; the hash above still matches.)

**What is asserted in the window.**  Only the `≤` half of the frozen displayed consequence: if
every admissible sector compression at level `j` is bounded by `B ≥ 0`, then so is the global
legal lower block.  **"Orthogonal, exhaustive, no residual sectors" degenerates to that
one-directional bound**, so a NON-EXHAUSTIVE H4 would not be caught here — the missing-sector
failure mode survives this development untouched.  At an in-window level with no admissible
sector the premise is vacuous and the shadow forces `‖C_{j+1→j}‖ ≤ 0`; that is the correct
reading of the frozen Claim there (an exhaustive decomposition over an empty sector set is the
zero block).

**Load-bearing demonstration.**  Removing the `h4` parameter from
`SE.denom.Phi.legal.tame.composition`'s binder list makes it fail to elaborate; at full strength,
the §7.10 review's counter-model (`bigLowerFrame`, review §V5) exhibits a frame satisfying
`Cited ∧ H1 ∧ H2 ∧ H3` on which `tame.Claim` is FALSE — H4 is genuinely load-bearing, which is
external review finding T3-G1 rendered mechanically.

`Claim` is a hypothesis. Nothing in this development proves it, and a green build says nothing
about its truth.

No `sorry`.
-/
import SE.Interface

namespace SE.denom.Phi.legal.sect

section
variable (F : SE.SEFrame)

/-- **(H4)** tier-1 shadow of `SE.denom.Phi.legal.sect`, quantified over the frozen Claim's
active window `1 ≤ j`, `3j ≤ n`, `j < K n − 1` (see the module header for the resolution of
"active `j`"): there, the sector compressions control the global legal lower block — if
`‖C̃_{λ,ξ}‖ ≤ B` for every admissible sector `ξ` at level `j` (and `B ≥ 0`), then
`‖C_{j+1→j}‖ ≤ B`. -/
def Claim : Prop :=
  ∀ n j B, 1 ≤ j → 3 * j ≤ n → j < SE.K n - 1 → 0 ≤ B →
    (∀ s, F.admissible n j s → F.csectS n j s ≤ B) → F.cLower n j ≤ B

end

end SE.denom.Phi.legal.sect
