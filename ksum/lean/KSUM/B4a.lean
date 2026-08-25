/-
`KSUM/B4a.lean` — linked node module.

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : KSUM.B4a                        (alias `B4a`)
node file      : ksum/proof-dag/nodes/KSUM.B4a.yaml
decomposition / role    : none / proof
epistemic status (read from the node file on 2026-07-30): **PROVED**
                 (assessment source: current node record; "independent review2")
mechanization  : **stated** — this module states the Claim as a `Prop` and does NOT prove it.
claim_hash     : sha256:12b8db1548893a06701bd41c6baf3705ef796d94194c82bf7ee268f000d387ca
                 (byte convention: see `KSUM/A1a.lean`)

current_claim_hash: sha256:ef85eea2f26b73d1efb01943c1d5e868608aa1154c21b05fbacaa544d2f3c77c

CURRENT CANONICAL CLAIM (verbatim from the node record):

  For every epsilon>0 there exist C_epsilon>0 and N0 such that, for every N>=N0, every q>=2, and every target t, the bounded-error quantum query complexity of cyclic 2-Sum satisfies Q(2-Sum_(Z_q,t,N)) <= C_epsilon N^(1/2+epsilon) q^(1/4).

END CURRENT CANONICAL CLAIM

FROZEN CLAIM (verbatim from `claim.statement` in the node file):

  B4a: bounded-query ABI port to cyclic 2-Sum after fixed-point preprocessing
  O_epsilon(N^{1/2+epsilon}q^{1/4}) [PROVED · independent review2]
  integrated: paper thm:k2-upper + app:k2-upper

Manuscript: `thm:k2-upper`, `ksum/paper/ksum_small_alphabet.tex`, appendix
`app:k2-upper`.

════════════════════════════════════════════════════════════════════════════════════════════════
  PROSE ↔ `Claim` DIFF
════════════════════════════════════════════════════════════════════════════════════════════════

`Claim` renders the BOUND, `O_ε(N^{1/2+ε} q^{1/4})`, in explicit-constant form: for every `ε > 0`
there are a constant `C_ε > 0` and a threshold `N₀` beyond which the bound holds for every
`q ≥ 2` and every target `t`.  Note the quantifier order — `C_ε` and `N₀` may depend on `ε` but
not on `N`, `q`, `t` — which is exactly what `O_ε` means and is the point at which an upper bound
of this shape can silently leak.

**`q ≥ 2` ADDED 2026-07-31 (closeout item C-5; statement-fidelity review §10 caveat (1), the
review's single WIDER verdict).**  As first written this `Claim` quantified over every `q` with
`NeZero q`, i.e. it also asserted the bound at `q = 1`, where `thm:k2-upper` says nothing: the
manuscript's hypothesis is *"every integer `q ≥ 2`"*.  A hypothesis-side over-assumption is the
dangerous direction — it is an interface field that grants MORE than the cited theorem, so a
composition consuming it would be conditional on a statement the literature does not supply.  The
Lean interface is now exactly `thm:k2-upper`.  `KSUM.B4.composition` is unaffected: it invokes
this Claim only under `5 ≤ q`, which implies `2 ≤ q`.

`Claim` does NOT render the ALGORITHM ("bounded-query ABI port … after fixed-point
preprocessing").  This is deliberate and is the same scope decision tier T1 made for
`thm:k2-upper` (out of scope: "an algorithm; only its parameter arithmetic could be
formalized").  Consequently this module says nothing about how the bound is achieved, and a green
build here must not be read as auditing the algorithm.

`KSUM.B4`'s composition uses only the bound, so the omission does not weaken the composition.

No `sorry`.  No proof is offered.
-/
import KSUM.Interface

namespace KSUM.B4a

open KsumAudit

/-- **`KSUM.B4a`, formal Claim** — the `k = 2` upper bound `O_ε(N^{1/2+ε}·q^{1/4})`.
For every `ε > 0` there are `C_ε > 0` and `N₀` such that for all `N ≥ N₀`, every modulus `q ≥ 2`
and every target `t`, `Q(2Sum_{Z_q,t,N}) ≤ C_ε · N^{1/2+ε} · q^{1/4}`.

The `2 ≤ q` hypothesis is the manuscript's own (`thm:k2-upper`: "every integer `q ≥ 2`"); see the
header for why its 2026-07-31 addition matters. -/
def Claim (M : QueryModel) : Prop :=
  ∀ ε : ℝ, 0 < ε → ∃ Cε : ℝ, 0 < Cε ∧ ∃ N₀ : ℕ,
    ∀ (N q : ℕ) [NeZero q], N₀ ≤ N → 2 ≤ q → ∀ t : ZMod q,
      M.Q (twoSum (ZMod q) t N) ≤ Cε * (N : ℝ) ^ (1 / 2 + ε) * (q : ℝ) ^ (1 / 4 : ℝ)

end KSUM.B4a
