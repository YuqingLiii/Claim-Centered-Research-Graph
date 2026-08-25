/-
`KSUM/A1a.lean` — linked node module.

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : KSUM.A1a                        (alias `A1a`)
node file      : ksum/proof-dag/nodes/KSUM.A1a.yaml
decomposition / role    : none / proof
epistemic status (read from the node file on 2026-07-30): **PROVED**
                 (assessment source: current node record)
mechanization  : **proved**, UNCONDITIONALLY (tier T2, 2026-07-30; WIDENED to every window target
                 by the R-A1-1/R-A1-3 repair batch, 2026-07-30) — `holds` below carries no
                 interface hypothesis (no `QueryModel` argument), so it is not even relative to
                 the cited bounds.  The mathematics is `KsumAudit.KFloor.core_reduction_at`
                 (`prop:core-even` + `lem:core-odd`) in `KsumAudit/T2KFloor.lean`.
claim_hash     : sha256:5a70591bb4e8d07997a719c63c5dceef47153056211e86bc494c249456a1e9e5

BYTE CONVENTION FOR `claim_hash` (identical in every node module of this layer): the text of the
node file's `## Claim` section — everything after the `## Claim` heading line and before the next
`## ` heading — encoded UTF-8, with LF line endings, with leading and trailing whitespace
stripped (Python `str.strip()`), hashed with SHA-256.

current_claim_hash: sha256:8c7ece4a3dee96320494bb19181234015db693e2eb828a680e628aabc6136696

CURRENT CANONICAL CLAIM (verbatim from the node record):

  For every window target t in [t0,t0+k), where t0=(k-2)(kK+1), the frozen-core reduction can use C0=floor(q/(k-1)) or a positive core summing to the target; when N-(k-2) is odd it also uses the parked coordinate v=t+(k-1)K+1, and all d>=1 bad patterns are excluded.

END CURRENT CANONICAL CLAIM

FROZEN CLAIM (verbatim from `claim.statement` in the node file):

  freeze a core of k−2 coords: CONSTANT C₀=⌊q/(k−1)⌋ (as authored) OR positive CORE summing to the
  target (kills all d≥1 bad patterns), PLUS the parked coordinate v=t+(k−1)K+1 when N−(k−2) is odd;
  valid at EVERY window target t ∈ [t₀, t₀+k) with t₀=(k−2)(kK+1), not merely at one
  [PROVED — both variants F1-verified; widened 2026-07-30 per review R-A1-1/R-A1-3]

  (Previous frozen text, superseded 2026-07-30 — kept so the earlier hash resolves:
   "freeze k−2 coords: CONSTANT C₀=⌊q/(k−1)⌋ (as authored) OR positive CORE summing to t
    (kills all d≥1 bad patterns) [PROVED — both variants F1-verified]",
   sha256:d9b25ae9c6d185de841bdd2c27d8f1a3d8758dee8e4ad7ba1fb4564b2ccf42db.)

Manuscript: `prop:core-even` (even live block) and `lem:core-odd` (odd live block, parked
coordinate), `ksum/paper/ksum_small_alphabet.tex`, appendix `app:k3`; construction item
(a) of `sec:k3`.

════════════════════════════════════════════════════════════════════════════════════════════════
  PROSE ↔ `Claim` DIFF — read before citing this module (rule 7e: "a `Claim : Prop` weaker than
  the frozen prose")
════════════════════════════════════════════════════════════════════════════════════════════════

`Claim` renders the CONSEQUENCE that `KSUM.A1`'s composition proof consumes, namely step 1 of
that proof: *"The residual decision problem on the remaining coordinates is `2Sum` at the shifted
target, and it is equivalent to the original: an unintended hit would have to use a bad pattern,
which A1a has excluded."*  Concretely: freezing a core `c` of `m ∈ {k-2, k-1}` coordinates turns
`kSum` at ANY window target `s` into `2Sum` at target `0` on the encoded live block.

Three deliberate differences from the prose, and all owed to the fidelity review:

1. **Existential in the core, not the two named witnesses.**  The prose names two constructions
   (the constant core `C₀ = ⌊q/(k-1)⌋` and the positive core summing to `t`).  `Claim` says only
   that SOME core works.  This is strictly weaker than the prose, i.e. the safe direction.
2. **Universal in the window target** *(this is the R-A1-3 repair, 2026-07-30)*.  `Claim`
   previously read `∃ t₀`, which is what the base-target formalization proved but NOT what the
   composition needs: `KSUM.A1c` delivers a window target chosen by the covering argument, not a
   target of `A1a`'s choosing, so an existential `t₀` was an over-strong premise attributed to
   `A1c` (all-pairs target transfer).  `Claim` now quantifies over every `s ∈ [t₀, t₀+k)`, the
   `k` consecutive residues `lem:transl-cover` covers each coset with, and the residual target
   stays fixed at `0`.
3. **Stated only on the encoded live block**, not on all of `(Fin (2n) → ZMod q)`.  This is
   mandatory, not a weakening: on *arbitrary* live values a `k`-subset consisting only of live
   coordinates can sum to `s`, which is precisely why `prop:core-even` restricts to the codeword
   subdomain.  Stating the identity on all inputs would state something FALSE.

**Window hypotheses — the manuscript's, not a convenient weakening.**  `Claim` carries
`2 ≤ κ` and `(k²-2)·κ + 2k-1 ≤ q`, which is verbatim `lem:core-odd`'s condition
`q ≥ (k²-2)K + 2k-1` with `K ≥ 2` (the harder of the two; `prop:core-even`'s
`q ≥ (k-1)(kK+2)` is weaker and is implied).  It is NOT the looser `2κ+1 ≤ q`.

This distinction is load-bearing and was got wrong in a first draft of this module, so it is
recorded: with `κ = ⌊(q-1)/2⌋` — the natural choice, and the one tier T1 uses for `k = 2` — the
manuscript's window reads `(k²-2)(q-1)/2 + 2k-1 ≤ q`, which is FALSE for every `k ≥ 3` and every
`q ≥ q₀(k)`.  Quantifying `Claim` over all `κ` with `2κ+1 ≤ q` would therefore have asserted the
frozen-core construction in a regime where the manuscript does not claim it, i.e. a hypothesis
STRONGER than the prose — the direction that silently turns a composition vacuous.  With the
window as stated, `KSUM.A1`'s composition must pick `κ = ⌊(q-2k+1)/(k²-2)⌋` exactly as
`thm:kfloor` does, and the two-sided estimate `q ≤ 2k²·κ` it then needs is proved there.

Note the pleasant consequence: `2 ≤ κ` together with this window is *equivalent* to
`q ≥ 2(k²-2) + 2k-1 = 2k²+2k-5 = q₀(k)`, which is exactly `KSUM.A1d`'s window floor.  The floor
`q₀(k)` is not an extra assumption; it is what "the core construction admits `K ≥ 2`" means.

No `sorry`.

**2026-07-30, tier T2 — the Claim is PROVED** (it was `stated` when this module was written).
The witnesses used are the manuscript's own: the frozen block is `KsumAudit.KFloor.coreVec`
(the `k-2` core coordinates all carrying `U = kK+1`, plus, when `m = k-1`, the parked coordinate
`v = t₀ + (k-1)K + 1`), and the target was the LEFT ENDPOINT `t₀ = (k-2)U` of both windows
`W_even` and `W_odd`.

**2026-07-30, repair batch (R-A1-1 + R-A1-3) — PROVED AT EVERY WINDOW TARGET.**  The T2 narrowing
("`core_reduction` is proved at the base target only") is now closed.  The general core is
`KsumAudit.KFloor.coreVecAt`: the manuscript's `c_i = U` for `i ≤ k-3` and
`c_{k-2} = t - (k-3)U`, which at `t = t₀ + r` reads `U + r`, plus the parked value
`v = t + (k-1)K + 1 = parkedVal + r`.  All four case bounds of `prop:core-even`/`lem:core-odd`
go through **with the same window hypothesis** `(k²-2)K + 2k-1 ≤ q`, because that hypothesis is
exactly the master inequality at the rightmost window target `r = k-1` (tight there).  The
base-target statement survives as the `r = 0` corollary `KsumAudit.KFloor.core_reduction`, so
nothing tier T2 proved was weakened or deleted.

Note this does NOT change the node's epistemic status (the current evidence-level rules): a green build is
evidence, never a status.
-/
import KSUM.Support.Freeze
import KsumAudit.T2KFloor

namespace KSUM.A1a

open KsumAudit KSUM.Support

/-- **`KSUM.A1a`, formal Claim** *(restated 2026-07-30 by the R-A1-1 / R-A1-3 repair batch: the
target is now universally quantified over the WINDOW, not existentially over one `t₀`).*

For every `k ≥ 3`, every claw alphabet size `κ ≥ 2` and modulus `q` inside `lem:core-odd`'s
window `(k²-2)·κ + 2k-1 ≤ q`, every core size `m ∈ {k-2, k-1}` — `k-2` in the even case of
`prop:core-even`, `k-1` in the parked-coordinate case of `lem:core-odd` — every live half-length
`n ≥ 2`, and **every window target** `s ∈ [t₀, t₀+k)` with `t₀ = (k-2)(kK+1)` the left endpoint
of `W_even`/`W_odd`, there are frozen core values `c : Fin m → ZMod q` such that, **on the
encoded live block**, `k`-Sum at `s` on `2n + m` coordinates agrees with `2`-Sum at `0` on the
`2n` live coordinates.

Read: *freezing the core kills every unintended `k`-subset, so the residual problem is exactly
the `k = 2` problem at target `0` — at every one of the `k` consecutive window targets that
`KSUM.A1c`'s covering statement can deliver.* -/
def Claim : Prop :=
  ∀ (k q n m κ s : ℕ) [NeZero q],
    3 ≤ k → k - 2 ≤ m → m ≤ k - 1 →
    2 ≤ κ → (k ^ 2 - 2) * κ + 2 * k - 1 ≤ q → 2 ≤ n →
    KsumAudit.KFloor.baseTarget k κ ≤ s → s < KsumAudit.KFloor.baseTarget k κ + k →
      ∃ c : Fin m → ZMod q,
        ∀ y : Fin (2 * n) → Fin κ,
          kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)
              (Fin.append (encode n (cyc q κ) y) c)
            = twoSum (ZMod q) 0 (2 * n) (encode n (cyc q κ) y)

/-- **`KSUM.A1a.Claim` holds, unconditionally, at every window target.**  The frozen block is the
manuscript's core at the target `s = t₀ + r`: the first `k-3` entries carry `U = kK+1`, the last
one carries `t - (k-3)U = U + r`, and — when `m = k-1` — the parked coordinate carries
`v = t + (k-1)K + 1`.  The mathematics is `prop:core-even` + `lem:core-odd`, formalized as
`KsumAudit.KFloor.core_reduction_at`.

Note which hypotheses of `Claim` the proof does **not** consume: neither `2 ≤ κ` nor `2 ≤ n` is
used (they are needed only where the claw bound is imported, i.e. in `KSUM.A1`'s composition),
so the identity proved here is strictly stronger than `Claim` demands. -/
theorem holds : Claim := by
  intro k q n m κ s _ hk hm1 hm2 _hκ hwin _hn hs1 hs2
  refine ⟨KsumAudit.KFloor.coreVecAt k κ q m (s - KsumAudit.KFloor.baseTarget k κ), fun y => ?_⟩
  have hs : KsumAudit.KFloor.baseTarget k κ + (s - KsumAudit.KFloor.baseTarget k κ) = s := by omega
  have h := KsumAudit.KFloor.core_reduction_at (k := k) (q := q) (n := n) (m := m) (κ := κ)
      (r := s - KsumAudit.KFloor.baseTarget k κ) hk hm1 hm2 hwin (by omega) y
  rwa [hs] at h

/-- The base window target `s = t₀`, i.e. exactly what tier T2 proved before this repair batch.
Kept under its own name because the T2 report cites that statement. -/
theorem holds_base (k q n m κ : ℕ) [NeZero q]
    (hk : 3 ≤ k) (hm1 : k - 2 ≤ m) (hm2 : m ≤ k - 1)
    (hwin : (k ^ 2 - 2) * κ + 2 * k - 1 ≤ q) (y : Fin (2 * n) → Fin κ) :
    kSum (ZMod q) k ((KsumAudit.KFloor.baseTarget k κ : ℕ) : ZMod q) (2 * n + m)
        (Fin.append (encode n (cyc q κ) y) (KsumAudit.KFloor.coreVec k κ q m))
      = twoSum (ZMod q) 0 (2 * n) (encode n (cyc q κ) y) :=
  KsumAudit.KFloor.core_reduction hk hm1 hm2 hwin y

/-- The same statement written through `KSUM.Support.frozen`, i.e. "the frozen `kSum`, evaluated
on the codeword block, is `2Sum` at `0`".  Purely a restatement — it is `Claim` composed with
`frozen_eq_append` — provided so that `KSUM.A1`'s composition can move between the two forms
without an ad-hoc rewrite. -/
theorem frozen_form (h : Claim) (k q n m κ s : ℕ) [NeZero q]
    (hk : 3 ≤ k) (hm1 : k - 2 ≤ m) (hm2 : m ≤ k - 1)
    (hκ2 : 2 ≤ κ) (hwin : (k ^ 2 - 2) * κ + 2 * k - 1 ≤ q) (hn : 2 ≤ n)
    (hs1 : KsumAudit.KFloor.baseTarget k κ ≤ s)
    (hs2 : s < KsumAudit.KFloor.baseTarget k κ + k) :
    ∃ c : Fin m → ZMod q,
      ∀ y : Fin (2 * n) → Fin κ,
        frozen m (kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)) c (encode n (cyc q κ) y)
          = twoSum (ZMod q) 0 (2 * n) (encode n (cyc q κ) y) := by
  obtain ⟨c, hc⟩ := h k q n m κ s hk hm1 hm2 hκ2 hwin hn hs1 hs2
  exact ⟨c, fun y => by rw [frozen_eq_append]; exact hc y⟩

end KSUM.A1a
