/-
`KSUM/A1b.lean` — linked node module.

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : KSUM.A1b                        (alias `A1b`)
node file      : ksum/proof-dag/nodes/KSUM.A1b.yaml
decomposition / role    : none / proof
epistemic status (read from the node file on 2026-07-30): **PROVED**
                 (assessment source: current node record)
mechanization  : **proved**, UNCONDITIONALLY — `holds` below carries no interface hypothesis
                 (no `QueryModel` argument), so it is not even relative to the cited bounds.
claim_hash     : sha256:827117dd6f3922068b5c99af16076b76a8a536970d9f7d6db19d3695c8c438ad
                 (byte convention: see `KSUM/A1a.lean`)

current_claim_hash: sha256:7c128111eadfd0f4a2874719517de3144cb6edb98032f30cd39fd2af0ff1f2c9

CURRENT CANONICAL CLAIM (verbatim from the node record):

  For all natural numbers n, kappa, and q with 2*kappa+1 <= q, and every y : Fin(2*n) -> Fin(kappa), the signed cyclic encoding E(y) := encode n (cyc q kappa) y satisfies 2-Sum_{Z_q,0,2n}(E(y)) = Claw_{n->kappa}(y). Thus the live instance has exactly 2*n coordinates and no unpaired live coordinate.

END CURRENT CANONICAL CLAIM

FROZEN CLAIM (verbatim from `claim.statement` in the node file):

  EVEN 2n-coord k=2 claw encoding on live part
  (no unpaired live coord) [PROVED]

Manuscript: `lem:encode`; construction item (b) of `sec:k3`.

════════════════════════════════════════════════════════════════════════════════════════════════
  PROSE ↔ `Claim` DIFF
════════════════════════════════════════════════════════════════════════════════════════════════

`Claim` is the encoding IDENTITY at even length `2n`: on the live block, `2Sum` at target `0`
read through the per-coordinate encoding `E` is exactly `Claw_{n→κ}`.  "No unpaired live
coordinate" is rendered by the length being literally `2 * n`; the odd/parked-coordinate variant
belongs to `KSUM.A1a` (`lem:core-odd`), not here.

`Claim` omits the manuscript's hypothesis `κ ≥ 2` — audit finding **F3**: it is not needed for
the identity, only where the claw bound is imported.  Omitting it makes `Claim` strictly
STRONGER than the prose, which is the safe direction for a statement that is proved, and the
dangerous direction for a hypothesis.  `KSUM.A1`'s composition supplies `2 ≤ κ` itself where it
calls `QueryModel.tani`, so nothing downstream leans on the omission.

This is the one leaf of the `A1` group that tier T1 already supplies a proof for
(`KsumAudit.twoSum_encode_cyc`), so per the commissioning rule it is proved here by reuse rather
than merely stated.

No `sorry`.
-/
import KSUM.Interface

namespace KSUM.A1b

open KsumAudit

/-- **`KSUM.A1b`, formal Claim.**  For `q ≥ 2κ+1` (any parity of `q`) and every live word `y` on
`2n` coordinates, `2Sum_{Z_q,0,2n}(E(y)) = Claw_{n→κ}(y)`. -/
def Claim : Prop :=
  ∀ (n κ q : ℕ), 2 * κ + 1 ≤ q →
    ∀ y : Fin (2 * n) → Fin κ,
      twoSum (ZMod q) 0 (2 * n) (encode n (cyc q κ) y) = Claw n κ y

/-- `KSUM.A1b.Claim` holds, unconditionally: it is `lem:encode`'s identity part, formalized for
tier T1 as `KsumAudit.twoSum_encode_cyc`. -/
theorem holds : Claim := fun n _κ _q hq y => twoSum_encode_cyc hq n y

end KSUM.A1b
