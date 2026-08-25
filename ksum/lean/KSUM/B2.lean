/-
`KSUM/B2.lean` — linked node module.
**This module's `composition` theorem IS the node's composition proof** (the current composition-linking convention).

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : KSUM.B2                          (alias `B2`)
node file      : ksum/proof-dag/nodes/KSUM.B2.yaml
decomposition / role    : AND / proof     children: A2, KSUM.k3.donor
epistemic status (read from the node file on 2026-07-30): **OPEN**
                 (`= min(composition=CONJECTURED, A2=CONJECTURED, k3.donor=OPEN·PARKED)`)
mechanization  : **composition-checked**, relative to
                 rel = [KSUM.k3.donor — the walk-optimal small-range donor bound; it has NO node
                        module in this pass (LEAF, OPEN·PARKED) and enters as the explicitly
                        named hypothesis `DonorClaim` below;
                        the NOVELTY side condition of the node's own `composition.rel`, which is
                        NOT mechanized — see the named gap below]
claim_hash     : sha256:a25606dcdd3e07b9f93ba38e0ab0e352929a1d1a03687264d9ad49d0bd951e14
                 (byte convention: see `KSUM/A1a.lean`)

current_claim_hash: sha256:a25606dcdd3e07b9f93ba38e0ab0e352929a1d1a03687264d9ad49d0bd951e14

CURRENT CANONICAL CLAIM (verbatim from the node record):

  OR-2 (AND: encoding A2 proved; needs a WALK-OPTIMAL donor L2):
  CONDITIONAL k-COLLISION EMBEDDING
  (partial W floors do not discharge consequence; branch OPEN)

END CURRENT CANONICAL CLAIM

FROZEN CLAIM (verbatim from `claim.statement` in the node file):

  OR-2 (AND: encoding A2 proved; needs a WALK-OPTIMAL donor L2):
  CONDITIONAL k-COLLISION EMBEDDING
  (partial W floors do not discharge consequence; branch OPEN)

FROZEN COMPOSITION CLAIM (verbatim from the node's `composition.claim`):

  A2 (the exact query-free reduction k-partite k-collision -> kSum with q = Theta_k(R^{k-1}))
  AND k3.donor (a walk-optimal small-range k>=3 k-collision detection lower bound) together imply
  B2: a k-Sum lower bound at small alphabet matching the donor's exponent through the reduction.

FROZEN `composition.rel` (verbatim):

  the parameter matching between the donor's range R and the induced alphabet q =
  Theta_k(R^{k-1}) must land inside the donor's own validity window — this is a real constraint,
  not bookkeeping, and it is what killed the L2e/L2f partial floors (see KSUM.L2fC: R =
  Omega(n^2) forces q = Omega_k(N^{2(k-1)}), above N^{k-1}, where BS is already stronger)

════════════════════════════════════════════════════════════════════════════════════════════════
  NAMED GAP — `Claim` IS WEAKER THAN THE FROZEN PROSE, and deliberately so
════════════════════════════════════════════════════════════════════════════════════════════════

`Claim` renders the TRANSPORT only: any donor bound `L(n,R)` for `k`-partite `k`-collision moves
to `kSum` over `Z_q` at the induced modulus, losing at most the absolute factor `2`.  That is
what "matching the donor's exponent through the reduction" means quantitatively, and it is what
`KSUM.A2` actually buys.

It does **not** render the node's `rel`: that the induced `q = Θ_k(R^{k-1})` must land in the
regime where the resulting `kSum` bound is NEW (not already implied by Belovs–Špalek).  That
condition is a comparison against an external bound which this development does not carry, so it
cannot be stated here without inventing an interface for BS.  **Consequence: a green build of
`composition` proves the transport, NOT that the transported bound is new.**  This is precisely
the confusion that killed the L2e/L2f partial floors, so it is named here rather than left to be
inferred.  The fidelity review must record it, and no reader may cite this module as evidence
that `KSUM.B2` yields a new bound.

`KSUM.k3.donor` has no module in this pass (it is not in the commissioned module list), so its
claim enters as the explicitly named parameter `DonorClaim`.  That is a deviation from §7.3's
"a node module imports its status-propagating children" and is reported as such.

No `sorry`.
-/
import KSUM.A2

namespace KSUM.B2

open KsumAudit KSUM.Support

/-- The claim of `KSUM.k3.donor` (node `ksum/proof-dag/nodes/KSUM.k3.donor.yaml`, status
**OPEN · PARKED**), written out here because that node has no Lean module in this pass: a lower
bound `L(k,n,R)` for `k`-partite `k`-collision detection on `k` blocks of `n` elements with range
`R`.  "Walk-optimal at small range" is a property of the FUNCTION `L`, not of this statement —
which is exactly why the node's `rel` (the parameter-window constraint) is a separate obligation
and is not mechanized.

**2026-07-31 (gap-closure item L-6, statement-fidelity review §10 "KSUM composition layer"
caveat (2)).**  `L` used to be typed `ℕ → ℕ → ℝ`, with `k` bound by the `∀` but ABSENT from the
donor bound's arguments.  That demanded ONE bound uniform in `k`, which is strictly stronger than
`KSUM.k3.donor` (a `k`-collision bound is a bound *for each fixed `k`*, and the manuscript's whole
`k ≥ 3` discussion — `prop:kclaw-fillers`, `prop:kclaw-coloring`, the `n^{k/(k+1)}` target — is
`k`-indexed).  The review graded it "a real narrowing of `B2.Claim`".  `L` now carries its `k`
argument, so a donor family may depend on `k`, and `Claim` below quantifies over exactly the
donor families the node describes. -/
def DonorClaim (M : QueryModel) (L : ℕ → ℕ → ℕ → ℝ) : Prop :=
  ∀ k n R : ℕ, 3 ≤ k → 1 ≤ n → 2 ≤ R → L k n R ≤ M.Q (Coll k n R)

/-- **`KSUM.B2`, formal Claim** — the conditional embedding, as a transport statement: for every
donor bound `L` and every instance of the `lem:embed` data, the donor bound transports to `kSum`
at the induced modulus `q = (P+1)(M+1)`, losing only the absolute factor `2`.

Read with the named gap above: this is "the donor's exponent reaches `kSum`", not "the resulting
`kSum` bound is new".

`L` is `k`-indexed since the 2026-07-31 gap-closure batch; see `DonorClaim`. -/
def Claim (M : QueryModel) : Prop :=
  ∀ L : ℕ → ℕ → ℕ → ℝ, DonorClaim M L →
    ∀ D : EmbedData,
      L D.k D.n D.R / 2 ≤ M.Q (kSum (ZMod D.q) D.k 0 (D.k * D.n))

/-- **The composition proof of `KSUM.B2`, mechanized.**

The whole content is that `KSUM.A2`'s query-freeness clause is what lets a donor bound cross the
reduction at an absolute constant; the exactness clause is what makes the crossing legitimate
(the two problems are the same problem).

Note the hypothesis shape.  `Claim` is stated in the node's own CONDITIONAL form ("CONDITIONAL
k-COLLISION EMBEDDING"), so the second child, `KSUM.k3.donor`, appears as the ANTECEDENT of
`Claim` rather than as a hypothesis of this theorem.  The variant `composition_with_donor` below
is the same statement with both children as explicit hypotheses, matching the shape of the frozen
composition claim; the two are interderivable and both are recorded so that gate G-R3 can be
answered without a judgement call.

A green build of this theorem is a *run* under the current evidence-level rules and therefore evidence at
NUMERICAL tier at best.  It does NOT make `KSUM.B2` anything other than OPEN: no donor satisfying
`DonorClaim` at a walk-optimal small-range exponent is known, and the novelty side condition is
not even stated. -/
theorem composition (M : QueryModel) (hA2 : KSUM.A2.Claim M) : Claim M := by
  intro L hDonor D
  obtain ⟨-, hquery, -, -⟩ := hA2 D
  have hd := hDonor D.k D.n D.R D.hk D.hn D.hR
  have hchain : L D.k D.n D.R ≤ 2 * M.Q (kSum (ZMod D.q) D.k 0 (D.k * D.n)) := le_trans hd hquery
  linarith

/-- `A2 ∧ k3.donor ⇒ B2`, with **both** status-propagating children as explicit hypotheses —
the literal shape of the node's frozen composition claim. -/
theorem composition_with_donor (M : QueryModel) (hA2 : KSUM.A2.Claim M) (L : ℕ → ℕ → ℕ → ℝ)
    (hDonor : DonorClaim M L) (D : EmbedData) :
    L D.k D.n D.R / 2 ≤ M.Q (kSum (ZMod D.q) D.k 0 (D.k * D.n)) :=
  composition M hA2 L hDonor D

/-! ## Non-vacuity of the `k`-indexed `DonorClaim` (gap-closure item L-6)

The point of the retype is that the donor family may now depend on `k`.  A witness that only
exercised a `k`-constant `L` would leave that unchecked, so the witness below is genuinely
`k`-dependent — `L k n R = -(k : ℝ)` — and is discharged for `KsumAudit.demoModel`, the
consistency witness of `QueryModel`.  It is a *satisfiability* witness for the hypothesis, not
evidence for any donor bound: `demoQ` is not quantum query complexity. -/

private theorem demoQ_nonneg {Mlen : ℕ} {Alph : Fin Mlen → Type} [∀ i, Fintype (Alph i)]
    (f : ((i : Fin Mlen) → Alph i) → Bool) : 0 ≤ demoQ f := by
  by_cases h : ∀ y z, f y = f z
  · rw [demoQ_const f h]
  · rw [demoQ_nonconst f h]; positivity

/-- The `k`-indexed donor hypothesis is satisfiable, by a family that genuinely varies with `k`. -/
theorem demoDonor : DonorClaim demoModel (fun k _ _ => -(k : ℝ)) := by
  intro k n R hk _ _
  have h1 : -(k : ℝ) ≤ 0 := neg_nonpos.mpr (Nat.cast_nonneg k)
  exact le_trans h1 (demoQ_nonneg (Coll k n R))

/-- Consequently `Claim demoModel` has content at a concrete donor family: the transported bound
`-(k)/2 ≤ Q(kSum …)` holds at `KSUM.Support.demoEmbed` (`k = 3`, `q = 325`). -/
example (hA2 : KSUM.A2.Claim demoModel) :
    -((3 : ℕ) : ℝ) / 2 ≤ demoModel.Q (kSum (ZMod 325) 3 0 3) :=
  composition demoModel hA2 (fun k _ _ => -(k : ℝ)) demoDonor demoEmbed

#print axioms DonorClaim
#print axioms Claim
#print axioms composition
#print axioms composition_with_donor
#print axioms demoDonor

end KSUM.B2
