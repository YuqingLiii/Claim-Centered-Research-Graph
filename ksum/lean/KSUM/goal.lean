/-
`KSUM/goal.lean` — linked node module.

**THIS MODULE IS INTENTIONALLY CLAIM-FREE.**

    -- lean: none — goal claim not yet frozen as a proposition (see node composition block)

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : KSUM.goal                        (alias `G`)
node file      : ksum/proof-dag/nodes/KSUM.goal.yaml
decomposition / role    : OR / proof                       children: B1, B2, B3, B4
epistemic status (read from the node file on 2026-07-30): **OPEN**
mechanization  : **none**, with the reason recorded here (the current composition-linking convention: "A non-formalized
                 node records `lean: none` with a reason.  Silence is invalid.")
claim_hash     : sha256:61adf0718c5e7228e5d6dd0b80d71983506483989632dbc91fddd7e83cc358a8
                 (byte convention: see `KSUM/A1a.lean`)

FROZEN CLAIM (verbatim from `claim.statement` in the node file):

  GOAL [OPEN]: reduce alphabet requirement in BS Ω(N^{k/(k+1)}) for fixed k≥3;
  find Q(N,k,q) between q=O(1) (Grover √N) and q≥n^k (BS tight)

════════════════════════════════════════════════════════════════════════════════════════════════
  WHY THERE IS NO `def Claim : Prop` HERE
════════════════════════════════════════════════════════════════════════════════════════════════

The frozen text is a **research target description, not a proposition**.  "Reduce alphabet
requirement" and "find `Q(N,k,q)`" have no truth value: the first names an improvement direction
without saying how far, the second names a quantity to determine without saying what about it is
asserted.  Two candidate readings are visible in the node's own route entries and they are NOT
equivalent:

  (a) `Q(kSum_{Z_q,t,N}) = Ω(N^{k/(k+1)})` for fixed `k ≥ 3` at alphabets far below the
      Belovs–Špalek requirement (this is the reading the `B1` route entry is killed against:
      *"B1's best output is the floor Ω_k(√N q^{1/6}), i.e. Ω_k(N^{2/3}) at q=Θ(N), and
      2/3 < k/(k+1) for every k ≥ 3"*);
  (b) determining `Q(N,k,q)` as a function on the whole intermediate range — a much stronger and
      much vaguer target.

**Writing a `Prop` here would be inventing the goal, not formalizing it.**  The formalization
synchronization rule requires the prose claim and Lean `Claim` to agree, and that check is impossible when
there is nothing to agree with.  The honest record is therefore `lean: none` plus the reason, and
the prerequisite is a mathematical decision by the lead, not an executor's guess.

The same defect used to be recorded one level down, on `KSUM.B1`, by the 2026-07-30 prose
composition pass: *"B1's Claim is a strategy description … not a proposition, so no route proof
`A1 ⇒ B1` can be stated.  Fix B1's Claim first."*  **That is no longer the state of B1**: the
review's §7.4 rewrite turned B1's Claim into a genuine proposition on 2026-07-30, and
`KSUM/B1.lean` now renders and proves it (gap-closure item L-7, 2026-07-31).  So the two nodes
have parted company — B1's Claim is statable and stated, `KSUM.goal`'s is neither — and the
argument above for `KSUM.goal` no longer has a companion one level down.

════════════════════════════════════════════════════════════════════════════════════════════════
  WHY THERE IS NO `composition_via_B2` THEOREM EITHER
════════════════════════════════════════════════════════════════════════════════════════════════

The commissioned fallback was a theorem SCHEMA over an explicit candidate goal proposition.  The
only schema available without inventing the goal is

    theorem composition_via_B2 (Goal : Prop) (route : KSUM.B2.Claim M → Goal)
        (hB2 : KSUM.B2.Claim M) : Goal := route hB2

which is modus ponens: it takes the route proof as a hypothesis and returns it applied.  It
carries no mathematics, and a green build of it would appear in the trust list next to the two
compositions that DO carry mathematics (`KSUM.A1.composition`, `KSUM.A2.composition`).  That
adjacency is itself the failure mode this layer exists to prevent, so the schema is deliberately
NOT declared.

What a real `composition_via_B2` would have to contain is on disk already, in prose, as the
manuscript's transfer calculus (`ksum/paper/ksum_small_alphabet.tex`, after
`lem:embed`): a donor bound `Ω(√n · R^c)` transports through `q = Θ_k(R^{k-1})` to
`Ω_k(√N · q^{c/(k-1)})`, which reaches `N^{k/(k+1)}` exactly when `c = (k-1)/(2(k+1))`.  That
exponent arithmetic IS statable and provable, and it is the natural next deliverable — but it
belongs to whichever proposition the lead freezes as the goal, and it is `KSUM.B2` content, not
`KSUM.goal` content.

════════════════════════════════════════════════════════════════════════════════════════════════
  THE NODE'S FOUR ROUTES, as read from disk on 2026-07-30 (recorded, not mechanized)
════════════════════════════════════════════════════════════════════════════════════════════════

  B1 → GOAL : route kill argued at proposer tier, REFUTED pending rule-6 review
              (`2/3 < k/(k+1)`; the gap is in the donor exponent `1/6`, not the encoding)
  B2 → GOAL : CONJECTURED, conditional on the one named hypothesis `KSUM.k3.donor`
              — the only live route.  Its child is mechanized: see `KSUM/B2.lean`.
  B3 → GOAL : route kill argued at proposer tier, REFUTED pending rule-6 review
              (constraint G11: no finite table of exact `Adv±` values implies a uniform exponent)
  B4 → GOAL : **RE-TYPED TO `related` ON 2026-07-30** — no longer a child.  GOAL is about fixed
              `k ≥ 3`, `B4` is about `k = 2`, no route proof `k=2 ⇒ k≥3` has ever been written or
              attempted, and the independent composition-layer review ENDORSED the re-typing
              (`ksum/reviews/ksum_composition_layer_review_20260730.md` §5.4).  `import KSUM.B4` was
              therefore REMOVED from this module in the same change (§7.6 check 6: the import
              graph must agree with `children`).  `KSUM/B4.lean` still mechanizes `B4`'s own AND
              composition; it says nothing about this edge and must not be read as evidence for
              it.  `KSUM.B4` remains in the build (it is reached from `KSUM/Trust.lean`, which
              prints its axioms).

No `sorry`, no `axiom`, and — deliberately — no theorem.
-/
import KSUM.B1
import KSUM.B2

/-
Intentionally empty: see the header.  The two imports record the DAG edges `goal → B1` and
`goal → B2` (§7.3: "the import graph is therefore the DAG") without asserting a route proof for
either.  `import KSUM.B1` was added 2026-07-31 with `KSUM/B1.lean` (gap-closure item L-7): B1 now
has a module, so the §7.6 check-6 import-graph agreement improves from 1 of 3 children to 2 of 3.
`goal → B3` remains un-imported because `KSUM.B3` still has no module (it was not in the
commissioned module list of any pass so far) — a DECLARED deviation, not an oversight.
`goal → B4` is gone: that edge was re-typed to `related` on 2026-07-30 and `B4` is no longer a
child.
-/
