/-
`KSUM/A2a.lean` — linked node module.

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : KSUM.A2a                        (alias `A2a`)
node file      : ksum/proof-dag/nodes/KSUM.A2a.yaml
decomposition / role    : none / proof
epistemic status (read from the node file on 2026-07-30): **PROVED**
                 (assessment source: current node record)
mechanization  : **stated** — this module states the Claim as a `Prop` and does NOT prove it.
claim_hash     : sha256:4cb82063f7261252ec1de025f8d1f8a7ee317b344d59e8d77ce459594c799f72
                 (byte convention: see `KSUM/A1a.lean`)

current_claim_hash: sha256:ef7049893c485b6afd214496ec087fcae198ac7ab7371e80152ba05971f41f14

CURRENT CANONICAL CLAIM (verbatim from the node record):

  For k≥3 and R≥2, let ω=2R−1, define u_j=ω^{j−1} for 1≤j≤k−1 and u_k=−(ω^{k−1}−1)/(ω−1), and set P=k(R−1)(ω^{k−1}−1)/(ω−1), M=((2k+1)^{k−1}−1)/2, and V=P+1. Define w_j=V(2k+1)^{j−1} for 1≤j≤k−1, w_k=−Σ_{j<k}w_j, and q=(P+1)(M+1). These are the complete payload, tag, and modulus formulas used by Lemma lem:embed.

END CURRENT CANONICAL CLAIM

FROZEN CLAIM (verbatim from `claim.statement` in the node file):

  complete payload/tag formulas u_j=ω^{j−1}, u_k=−(ω^{k−1}−1)/(ω−1),
  w_j=V·(2k+1)^{j−1}; modulus q=(P+1)(M+1) [PROVED]

Manuscript: `lem:embed` / `prop:embed` (good pattern `μ = (1,…,1)`),
`ksum/paper/ksum_small_alphabet.tex`, appendix `app:embed`.

════════════════════════════════════════════════════════════════════════════════════════════════
  PROSE ↔ `Claim` DIFF
════════════════════════════════════════════════════════════════════════════════════════════════

The frozen prose names the payload/tag FORMULAS.  `Claim` renders what `KSUM.A2`'s composition
consumes from them — its step 1, *"Completeness … every collision maps to a `k`-subset summing to
the target"*: the encoding of `lem:embed` sends every genuine `k`-partite `k`-collision to a
`k`-subset summing to `0`.

* The formulas themselves are carried by `KSUM.Support.EmbedData` (the `enc` field and the
  arithmetic fields `k_dvd_P`, `two_mul_Mv`, `P_lower`, `P_upper`), each with its manuscript
  citation.  `Claim` is therefore stated *for every* `EmbedData`, which is how a reduction lemma
  reads: the payload/tag assignment is data, and completeness is a property of it.
* `Claim` is the ONE direction (collision ⇒ hit).  The converse is `KSUM.A2b`.  Splitting them
  this way is the node graph's own split, and it is what makes `KSUM.A2` a genuine AND rather
  than a decorative one.
* `Claim` does NOT re-state the closing coefficient `u_k = -∑_{j<k} u_j`; that identity is what
  makes the good-pattern payloads telescope to `0` and is internal to the (unmechanized) proof.
  A reader must not conclude from this module that the telescoping was checked.

No `sorry`.  No proof is offered: `KSUM.A2a` is prose-PROVED with an archived 2026-07-19 review.
-/
import KSUM.Support.Embed

namespace KSUM.A2a

open KsumAudit KSUM.Support

/-- **`KSUM.A2a`, formal Claim** — completeness of the `lem:embed` reduction.
For the payload/tag data of `lem:embed`, every `k`-partite `k`-collision instance that HAS a
collision is mapped to a `kSum` instance that HAS a `k`-subset summing to the target `0`. -/
def Claim : Prop :=
  ∀ (D : EmbedData) (g : Fin (D.k * D.n) → Fin D.R),
    Coll D.k D.n D.R g = true →
      kSum (ZMod D.q) D.k 0 (D.k * D.n) (D.encodeInst g) = true

end KSUM.A2a
