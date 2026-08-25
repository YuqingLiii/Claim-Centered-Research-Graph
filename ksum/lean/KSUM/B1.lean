/-
`KSUM/B1.lean` — linked node module.
**This module's `composition_via_*` theorems ARE the node's route proofs** (the current composition-linking convention).

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : KSUM.B1                          (alias `B1`)
node file      : ksum/proof-dag/nodes/KSUM.B1.yaml
decomposition / role    : OR / proof      children: L11, L12, A1
epistemic status (read from the node file on 2026-07-31): **CONJECTURED**
                 (`status_source`: mechanical §1 recompute after A1 → PROVED; the route proof
                 `A1 ⇒ B1` was recorded there as "statable and near-trivial but unwritten".
                 A green build here is EVIDENCE for a pending review, NOT a status — §7.1.)
mechanization  : **proved** relative to
                 rel = [QueryModel.restrict (= sec:prelim fact (i));
                        QueryModel.relabel  (= sec:prelim fact (ii));
                        QueryModel.freeze   (= sec:prelim facts (i)+(iii) composed at the last
                                               position — coordinate freezing; STATED in the
                                               manuscript in the reviewed manuscript, explicitly recorded after external review
                                               as audit finding F1)]
                 — note `QueryModel.abi`/`tani` are **NOT** used: B1's Claim is the REDUCTION,
                 not the numeric floor, so no imported claw bound enters.
claim_hash     : sha256:aa3244091213ff586fd57c90572a5796a37b25c4b43fca71de4efe41d60a2fa5
                 (byte convention: see `KSUM/A1a.lean`)

current_claim_hash: sha256:aa3244091213ff586fd57c90572a5796a37b25c4b43fca71de4efe41d60a2fa5

CURRENT CANONICAL CLAIM (verbatim from the node record):

  For every fixed `k ≥ 3` there is a frozen-coordinate reduction — a core of `k−2` coordinates (plus
  one parked coordinate when `N−(k−2)` is odd) together with the `k=2` claw encoding on the `2m` live
  coordinates — such that `Q(kSum_{Z_q,t,N}) = Ω(Q(Claw_{m→K}))` for every target `t`, every `K ≥ 2`
  and every `q ≥ (k²−2)K+2k−1`.

  *(Claim rewritten 2026-07-30 per the composition-layer review §7.4 — the previous text, kept for
  history, was a strategy description, not a proposition: "OR-1: FROZEN-COORDINATE REDUCTION (freeze
  k−2 coords, embed proved k=2 claw→2-Sum into live coords)". The rewrite is what `A1` delivers, and
  it makes the `A1 ⇒ B1` route entry statable — near-trivial, which is the honest state of that
  edge.)*

END CURRENT CANONICAL CLAIM

FROZEN CLAIM (verbatim from `claim.statement` in the node file):

  For every fixed `k ≥ 3` there is a frozen-coordinate reduction — a core of `k−2` coordinates
  (plus one parked coordinate when `N−(k−2)` is odd) together with the `k=2` claw encoding on the
  `2m` live coordinates — such that `Q(kSum_{Z_q,t,N}) = Ω(Q(Claw_{m→K}))` for every target `t`,
  every `K ≥ 2` and every `q ≥ (k²−2)K+2k−1`.

  *(Claim rewritten 2026-07-30 per the composition-layer review §7.4 — the previous text, kept for
  history, was a strategy description, not a proposition: "OR-1: FROZEN-COORDINATE REDUCTION
  (freeze k−2 coords, embed proved k=2 claw→2-Sum into live coords)". The rewrite is what `A1`
  delivers, and it makes the `A1 ⇒ B1` route entry statable — near-trivial, which is the honest
  state of that edge.)*

════════════════════════════════════════════════════════════════════════════════════════════════
  PROSE ↔ `Claim` DIFF  (read before citing this module)
════════════════════════════════════════════════════════════════════════════════════════════════

* `Ω(·)` is made EXPLICIT: `∃ C > 0, Q(Claw_{n→K}) ≤ C · Q(kSum_{Z_q,t,N})`, with `C` allowed to
  depend on `k` only (`holds` delivers the absolute `C = 4`, so even that dependence is unused).
  The `∃ C` is placed OUTSIDE the quantifiers over `N`, `q`, `K`, `t`, i.e. the constant is
  uniform in all of them — the strong reading of `Ω(·)`, and the one the prose intends.
* The prose writes `m` for the claw list length AND uses `m` for nothing else; the Lean writes
  `n` for the claw list length and `m` for the CORE size (`m ∈ {k-2, k-1}`), matching
  `KSUM/A1a.lean` and `KsumAudit/T2KFloor.lean`.  The prose's "`2m` live coordinates" is the
  Lean's `2 * n`, and its `Claw_{m→K}` is `Claw n K`.
* The prose leaves the length hypothesis implicit ("a core of `k−2` coordinates … together with
  the claw encoding on the live coordinates" presupposes there are enough coordinates for both).
  The Lean carries it explicitly as `k + 3 ≤ N`, which is exactly what forces the live half-length
  `n ≥ 2` that `KSUM.A1a.Claim` requires.  **This is a hypothesis the prose does not print**; it
  is NARROWER, hence safe, and it is queued for the delta-fidelity review.
* The core-size clause "`k−2` coordinates plus one parked coordinate when `N−(k−2)` is odd" is
  rendered as the EXISTENTIAL `∃ n m, k-2 ≤ m ∧ m ≤ k-1 ∧ N = 2n + m`, i.e. the split is
  delivered, not assumed.  Which of the two values `m` takes is determined by the parity of
  `N - (k-2)`, exactly as the prose says, and the proof exhibits it.
* `q ≥ (k²−2)K+2k−1` and `K ≥ 2` are the prose's own hypotheses, verbatim.

════════════════════════════════════════════════════════════════════════════════════════════════
  THE `A1 ⇒ B1` ROUTE — and a FINDING about it (queued for the delta-fidelity review)
════════════════════════════════════════════════════════════════════════════════════════════════

The node's `composition` block records the route as *"B1's new Claim is what A1 delivers"*.  That
sentence is true of **`KSUM.A1`'s PROOF** and false of **`KSUM.A1`'s CLAIM**:

    KSUM.A1.Claim = KSUM.A1d.Claim = "∃ C_k, c_k, A, B, N₀ > 0 such that for N ≥ N₀,
                                      q₀(k) ≤ q ≤ C_k·N and every t,
                                      A·√N·q^{1/6} ≤ Q(kSum) (and the N^{2/3} plateau)"

is a NUMERIC FLOOR.  A floor on `Q(kSum)` says nothing about `Q(Claw_{n→K})`, so it cannot
re-derive the reduction that produced it: `KSUM.A1.Claim M → Claim M` is **not** an implication
one can prove.  The DAG therefore does not register that artificial edge.

The route that actually runs is `composition_via_frozen_core_reduction`: it takes **A1's own three children**
`A1a`, `A1b`, `A1c` — the identical hypothesis set as `KSUM.A1.composition` (gate G-R3) — and
produces `Claim`.  In other words the `A1` box on the DAG is shared machinery, and both `A1d`'s
floor and `B1`'s reduction are outputs of it; the drawn edge `A1 → B1` is an edge between
BRANCHES, not between the two nodes' Claims.  **Recorded as a finding, not repaired here:**
repairing it is a graph decision (re-typing the edge, or restating one of the two Claims), which
is a lead call, not an executor's.

The other two routes, `L11` and `L12`, have no `composition_via_*` theorem: both children are
REFUTED · DEAD (reviewed), so `min(child, route)` is REFUTED whatever the route says, and the
node file records that no route proof will be written.  Their node files carry the matching
`lean: none` justification.

════════════════════════════════════════════════════════════════════════════════════════════════
  WHAT A GREEN BUILD HERE DOES NOT ESTABLISH
════════════════════════════════════════════════════════════════════════════════════════════════

Nothing about `KSUM.goal`.  The `B1 → GOAL` route is argued REFUTED on that node
(`2/3 < k/(k+1)`): the reduction below is exactly as strong as the claw donor plugged into it, and
the best donor on disk (`thm:abi`/`thm:tani`, `κ^{1/6}`) yields `Ω_k(N^{2/3})` at `q = Θ(N)`,
short of `N^{k/(k+1)}` for every `k ≥ 3`.  This module makes that arithmetic *visible* — the
reduction is unconditional in the donor — and changes it not at all.

No `sorry`, no `axiom`, no `native_decide`.
-/
import KSUM.A1a
import KSUM.A1b
import KSUM.A1c

namespace KSUM.B1

open KsumAudit KSUM.Support

/-- **`KSUM.B1`, formal Claim** (`ksum/proof-dag/nodes/KSUM.B1.yaml`, frozen 2026-07-30).

For every fixed `k ≥ 3` there is a constant `C > 0` such that, for every length `N ≥ k+3`, every
claw alphabet `K ≥ 2`, every modulus `q ≥ (k²-2)K + 2k-1` and every target `t ∈ Z_q`, the input
splits as `N = 2n + m` with a core of `m ∈ {k-2, k-1}` coordinates (the second value being the
parked coordinate of `lem:core-odd`, taken exactly when `N - (k-2)` is odd) and

    `Q(Claw_{n→K}) ≤ C · Q(kSum_{Z_q,t,N})`,

which is the manuscript's `Q(kSum_{Z_q,t,N}) = Ω(Q(Claw_{n→K}))` with the implied constant
exhibited.  See the PROSE ↔ `Claim` DIFF in the header. -/
def Claim (M : QueryModel) : Prop :=
  ∀ k : ℕ, 3 ≤ k →
    ∃ C : ℝ, 0 < C ∧
      ∀ (N q K : ℕ) [NeZero q], 2 ≤ K → (k ^ 2 - 2) * K + 2 * k - 1 ≤ q → k + 3 ≤ N →
        ∀ t : ZMod q,
          ∃ n m : ℕ, 2 ≤ n ∧ k - 2 ≤ m ∧ m ≤ k - 1 ∧ N = 2 * n + m ∧
            M.Q (Claw n K) ≤ C * M.Q (kSum (ZMod q) k t N)

/-- **The `A1`-branch route proof, at A1's own hypothesis set** (the identical three children as
`KSUM.A1.composition`, gate G-R3): `A1a ∧ A1b ∧ A1c ⇒ B1`.

Steps, in the order `KSUM.A1.composition` runs them, minus its step 4 (the exponent arithmetic,
which is where `A1d`'s floor — and only it — needs `QueryModel.tani`):

0. **Cover the target (A1c).**  For the given `t`, the coset-covering Claim produces a window
   target `s ∈ [t₀, t₀+k)` with `s = t + k·a` and `Q(kSum_s) ≤ C₁·Q(kSum_t)`.
1. **Freeze the core (A1a) at that window target.**  A core `c : Fin m → Z_q`, `m ∈ {k-2, k-1}`,
   for which `kSum` at `s` on the encoded live block is `2Sum` at `0`.
2. **Encode (A1b).**  On the `2n` live coordinates, `2Sum` at `0` read through `E` is `Claw`.
3. **Transfer.**  `E` is a per-coordinate injection, so `sec:prelim` facts (i)+(ii) cost the
   absolute factor `2` (`QueryModel.relabel_inj`); freezing `m` coordinates costs nothing
   (`KSUM.Support.Q_frozen_le`, i.e. `m` applications of the `freeze` field = facts (i)+(iii);
   originally the unstated F1 field, stated in the manuscript in the reviewed manuscript).

Chaining 0–3 gives `Q(Claw_{n→K}) ≤ 2·C₁·Q(kSum_t)`, so `C = 2·C₁`.  No claw lower bound is
imported anywhere, which is why this statement is unconditional in the donor. -/
theorem composition_via_frozen_core_reduction (M : QueryModel)
    (hA1a : KSUM.A1a.Claim) (hA1b : KSUM.A1b.Claim) (hA1c : KSUM.A1c.Claim M) : Claim M := by
  obtain ⟨C, hCpos, hcover⟩ := hA1c
  intro k hk
  refine ⟨2 * C, by linarith, ?_⟩
  intro N q K _inst hK hwin hN t
  have hk2 : 9 ≤ k ^ 2 := by
    have h := Nat.pow_le_pow_left hk 2
    simpa using h
  -- split `N = 2n + m` with `k-2 ≤ m ≤ k-1`: `m = k-2` (even live block) or `m = k-1` (parked)
  obtain ⟨n, m, hm1, hm2, rfl⟩ :
      ∃ n m : ℕ, k - 2 ≤ m ∧ m ≤ k - 1 ∧ N = 2 * n + m :=
    ⟨(N - (k - 2)) / 2, (k - 2) + (N - (k - 2)) % 2, by omega, by omega, by omega⟩
  have hn : 2 ≤ n := by omega
  have hwinlin : 7 * K ≤ (k ^ 2 - 2) * K := Nat.mul_le_mul (by omega) (le_refl K)
  have hqK : 2 * K + 1 ≤ q := by omega
  -- 0. cover the target (A1c, coset-covering form)
  obtain ⟨_a, s, hs1, hs2, _hcoset, hliftq⟩ := hcover k (2 * n + m) q K hk hwin t
  -- 1. freeze the core AT THAT WINDOW TARGET (A1a)
  obtain ⟨c, hcore⟩ :=
    KSUM.A1a.frozen_form hA1a k q n m K s hk hm1 hm2 hK hwin hn hs1 hs2
  -- 1 + 2: `Claw = (frozen kSum) ∘ E`  (A1a and A1b)
  have hclaw_eq : (fun y : Fin (2 * n) → Fin K =>
      frozen m (kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)) c
        (fun p => encMap n (cyc q K) p (y p)))
      = Claw n K := by
    funext y
    change frozen m (kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)) c
      (encode n (cyc q K) y) = Claw n K y
    rw [hcore y, hA1b n K q hqK y]
  -- 3. transfer: facts (i) + (ii) cost the factor 2, freezing costs nothing
  have htrans : M.Q (Claw n K)
      ≤ 2 * M.Q (frozen m (kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)) c) := by
    have key := M.relabel_inj (Alph := fun _ : Fin (2 * n) => ZMod q)
      (Alph' := fun _ : Fin (2 * n) => Fin K) (fun p => encMap n (cyc q K) p)
      (encMap_injective n (cyc q K) (cyc_injective hqK))
      (frozen m (kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)) c)
    rwa [hclaw_eq] at key
  have hfrz : M.Q (frozen m (kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)) c)
      ≤ M.Q (kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)) :=
    Q_frozen_le M (G := ZMod q) (nlive := 2 * n) m
      (kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)) c
  refine ⟨n, m, hn, hm1, hm2, rfl, ?_⟩
  calc M.Q (Claw n K)
      ≤ 2 * M.Q (frozen m (kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)) c) := htrans
    _ ≤ 2 * M.Q (kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)) := by linarith
    _ ≤ 2 * (C * M.Q (kSum (ZMod q) k t (2 * n + m))) := by linarith
    _ = 2 * C * M.Q (kSum (ZMod q) k t (2 * n + m)) := by ring

/-- **`KSUM.B1.Claim` holds relative to the interface** (§7.4: "once all necessary children have
closed proofs, an optional `holds : Claim` composes them").

All three inputs are theorems — `KSUM.A1a.holds` (every window target), `KSUM.A1b.holds`,
`KSUM.A1c.holds` (coset covering) — so the delivered constant is the absolute `C = 2 · 2 = 4`.

What remains relative is exactly the interface: `M.restrict`/`M.relabel` are `sec:prelim` facts
(i)/(ii) and `M.freeze` is coordinate freezing = facts (i)+(iii) composed (originally the unstated
principle F1; stated in the manuscript in the reviewed manuscript).  `M.abi`/`M.tani` are NOT used.  A theorem
proved against an abstract interface is exactly as strong as the results that interface cites, and
not one notch stronger. -/
theorem holds (M : QueryModel) : Claim M :=
  composition_via_frozen_core_reduction M KSUM.A1a.holds KSUM.A1b.holds (KSUM.A1c.holds M)

/-! ## Non-vacuity witnesses

The hypotheses of `Claim` are satisfiable at concrete parameters, and the delivered split is the
`m = k-1` (parked-coordinate) branch, so the witness exercises `lem:core-odd` and not only
`prop:core-even`. -/

/-- Smallest legal modulus at `k = 3, K = 2`: `q₀(3) = (3²-2)·2 + 2·3 - 1 = 19`, at length
`N = 10`.  The split delivered is `n = 4`, `m = 2 = k-1` (parked coordinate present, since
`N - (k-2) = 9` is odd). -/
example : ∃ C : ℝ, 0 < C ∧ ∀ t : ZMod 19,
    ∃ n m : ℕ, 2 ≤ n ∧ 1 ≤ m ∧ m ≤ 2 ∧ 10 = 2 * n + m ∧
      demoModel.Q (Claw n 2) ≤ C * demoModel.Q (kSum (ZMod 19) 3 t 10) := by
  obtain ⟨C, hC, h⟩ := holds demoModel 3 (by norm_num)
  exact ⟨C, hC, fun t => h 10 19 2 (by norm_num) (by norm_num) (by norm_num) t⟩

/-- The even branch too: `N = 11`, `N - (k-2) = 10` even, so `m = 1 = k-2` and `n = 5`. -/
example : ∃ C : ℝ, 0 < C ∧ ∀ t : ZMod 19,
    ∃ n m : ℕ, 2 ≤ n ∧ 1 ≤ m ∧ m ≤ 2 ∧ 11 = 2 * n + m ∧
      demoModel.Q (Claw n 2) ≤ C * demoModel.Q (kSum (ZMod 19) 3 t 11) := by
  obtain ⟨C, hC, h⟩ := holds demoModel 3 (by norm_num)
  exact ⟨C, hC, fun t => h 11 19 2 (by norm_num) (by norm_num) (by norm_num) t⟩

#print axioms Claim
#print axioms composition_via_frozen_core_reduction
#print axioms holds

end KSUM.B1
