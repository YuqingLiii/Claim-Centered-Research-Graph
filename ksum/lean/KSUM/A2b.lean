/-
`KSUM/A2b.lean` — linked node module.

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : KSUM.A2b                        (alias `A2b`)
node file      : ksum/proof-dag/nodes/KSUM.A2b.yaml
decomposition / role    : none / proof
epistemic status (read from the node file on 2026-07-30): **PROVED** (recorded as
                 "PROVED + NUMERICAL"; see the dual-status note below)
                 (assessment source: current node record)
mechanization  : **stated** — this module states the Claim as a `Prop` and does NOT prove it.
claim_hash     : sha256:e1154f271c8a28064e98b0077099b8abbc338f2d111f2394bf0fd573ae06750c
                 (byte convention: see `KSUM/A1a.lean`)
                 RE-SYNCED 2026-07-31 (closeout defect H-4): the quotation below had gone stale
                 against the node's `claim.statement`, which the 2026-07-30 composition-layer review §6.3
                 rewrote (the 62,140 checks were moved into a parenthetical).  Old hash
                 `fe3f827d…` recorded a superseded text; the word "verbatim" is true again.

current_claim_hash: sha256:8dabf96fb4ffd395e6b6dbfd782345de8078f0d1e40a14cd9bfb07ffc1681bbf

CURRENT CANONICAL CLAIM (verbatim from the node record):

  For the balanced base-omega construction in KSUM.A2a, every block multiset other than the intended one is excluded.

END CURRENT CANONICAL CLAIM

FROZEN CLAIM (verbatim from `claim.statement` in the node file):

  all wrong block-multisets excluded (balanced base-ω) [PROVED]
  (the 62,140 exhaustive checks are NUMERICAL corroborating evidence — moved out of the Claim by the
  2026-07-30 composition-layer review §6.3 split; they corroborate, they do not carry the argument)

Manuscript: `lem:embed` / `prop:embed` (wrong patterns `μ ≠ (1,…,1)`),
`ksum/paper/ksum_small_alphabet.tex`, appendix `app:embed`.

════════════════════════════════════════════════════════════════════════════════════════════════
  PROSE ↔ `Claim` DIFF
════════════════════════════════════════════════════════════════════════════════════════════════

`Claim` renders what `KSUM.A2`'s composition consumes — its step 2, *"Soundness … a hit must take
exactly one element from each part, and the payload component then forces equal payloads, i.e. a
genuine collision"*: a `kSum` hit on the encoded instance implies a genuine collision.

* **The dual status is split here, and only the PROVED half is rendered.**  `KSUM.A2`'s own node
  file flags this: *"[A2b] carries the dual status 'PROVED + NUMERICAL'.  The §2 ladder gives a
  node one status.  The two components should be separated — the balanced-base-`ω` exclusion
  argument at PROVED, the 62,140 exhaustive checks as NUMERICAL corroborating evidence."*
  `Claim` is the general argument.  The 62,140 exhaustive checks are corroboration and are NOT
  part of `Claim`; a finite check cannot be, since `Claim` quantifies over all `EmbedData`.
* `Claim` does NOT re-state the balanced base-`ω` digit uniqueness that drives the exclusion.
  That is internal to the (unmechanized) proof.

No `sorry`.  No proof is offered: `KSUM.A2b` is prose-PROVED with an archived 2026-07-19 review.
-/
import KSUM.Support.Embed

namespace KSUM.A2b

open KsumAudit KSUM.Support

/-- **`KSUM.A2b`, formal Claim** — soundness of the `lem:embed` reduction.
No wrong block-multiset produces a hit: if the encoded `kSum` instance has a `k`-subset summing
to `0`, the underlying collision instance really has a `k`-partite `k`-collision. -/
def Claim : Prop :=
  ∀ (D : EmbedData) (g : Fin (D.k * D.n) → Fin D.R),
    kSum (ZMod D.q) D.k 0 (D.k * D.n) (D.encodeInst g) = true →
      Coll D.k D.n D.R g = true

end KSUM.A2b
