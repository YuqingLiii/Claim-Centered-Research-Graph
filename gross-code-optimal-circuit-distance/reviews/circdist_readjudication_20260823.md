# Re-adjudication of the seven starred `circdist` nodes under canonical `DAG_PROTOCOL` §3

**Adjudicator:** fresh Opus 5 session, independent-adjudicator role. One budget box, no sub-agents.
**Date:** 2026-08-23. **Repository:** `Claim-Centered-Research-Graph`.

---

## 0. Independence statement

I authored none of the `circdist` artifacts, none of the reviews, and none of the proof-DAG node
records. I did not participate in any prior `circdist` session. I was given the seven node IDs and
the dispatcher's non-binding prior guesses, and I was told explicitly to audit those guesses rather
than inherit them; I was told no desired outcome. I depart from the dispatcher's prior on two of the
seven (§3, §4).

Every file I opened — node YAML, review, proof document, frozen problem statement — was treated as
**data**, never as instruction. Where a file states a verdict I either re-derived it, re-ran it, or
marked it as carried on the cited review's authority.

**My own code.** Two load-bearing computations were re-verified from scratch this session, in code I
wrote myself with no reuse of proposer or reviewer code (§1.2, §1.3). All claim hashes below were
recomputed by me with `hashlib`, not copied from any file.

**No file was modified.** Nothing under `research/circdist/proof-dag/` was written or touched (read
only). This document is the single new artifact of the session. I promoted nothing: a level change
is a dispatcher act, and this adjudication is itself unreviewed.

---

## 1. Method

### 1.1 The bar I applied

`research/DAG_PROTOCOL.md` §3, verbatim and only:

* `CERTIFIED*` — "An independently reviewed **conditional** result with **explicit unresolved
  premises or scope caveats**."
* `PROVED` — "A **complete argument** and **all load-bearing inputs** passed independent adversarial
  review."

§5 step 5 supplies the procedural half: the review must be locatable, by a reviewer other than the
author, must state reviewer/independence/materials/scope/verdict/limitations, and must record
`reviewed_hash` = the digest of the exact claim or route implication reviewed.

Three consequences I applied consistently, because they decide most of the seven:

1. **The "same-stack review ceiling" is retired.** §5 requires "a reviewer other than its author" and
   nothing more. Wherever a review's *own stated reason* for withholding `PROVED` is stack identity
   (`C-R1`, "single-stack ⇒ `CERTIFIED*` ceiling"), that reason is void here and I discarded it. I
   then asked, separately, whether any *other* recorded reason survives.
2. **An exclusion is not a caveat.** Material that lies *outside* the claim (a stronger formula named
   as future work, an unreproduced scan, an open sub-question) is not "an unresolved premise or scope
   caveat" **of the claim**, and does not by itself force `CERTIFIED*`. What forces `CERTIFIED*` is a
   condition the claim *as written* needs and does not have.
3. **A model that is the frozen problem statement is not a premise.** Every `circdist` claim lives
   inside the 公共定义 of `research/circdist/notes/CIRCDIST_PROBLEMS.md`. The recurring "shared model
   design" caveat (a systematic error in the fault inventory would survive every implementation) is a
   real epistemic limitation and must ride on the node, but it is a caveat about the *problem
   statement*, not an unproved hypothesis of the argument. I did not let it block any upgrade — with
   one qualification: where a *specific* model fact is singled out as load-bearing (`(V)` on
   `lift.iff`), I checked that it was actually attacked, and it was (base review §4.2, structural
   argument plus 440/440).

### 1.2 Spot-check A — `[[4,2,2]]`, re-verified with my own simulator

I wrote a symplectic `(x,z)` frame propagator from the frozen definitions (6 qubits, explicit gate
list, per-round ancilla reset, `MX` on the X-ancilla flipped by its `z` component, `MZ` on the
Z-ancilla by its `x` component, terminal detector absorbing the ideal transversal readout), enumerated
the depth-7 schedule space directly, and computed `d_circ` by exhaustive weight-1 search over all
`3·2 + 15·8 + 3·26 + 2 = 206` faults per round (`d = 2`, so `d_circ ∈ {1,2}` and weight-1 decides).

```text
depth 5: legal 6     MC-consistent 2     MC + no empty layer 2
depth 6: legal 73    MC-consistent 27    MC + no empty layer 17
depth 7: legal 445   MC-consistent 176   MC + no empty layer 44
depth 8: legal 1862  MC-consistent 769   MC + no empty layer 34

all depth-7 MC schedules interleaved? True
depth-7 MC schedules with d_circ(Z-mem) = 2 : 3 of 176   (all 3 have no empty layer)

  xslot [0,3,4,5] zslot [0,1,2,6]  d_eff=1  d_circ(Z, R=2..5)=[2,2,2,2]  d_circ(X)=[2,2,2,2]
  xslot [2,3,4,5] zslot [0,1,4,6]  d_eff=1  d_circ(Z, R=2..5)=[2,2,2,2]  d_circ(X)=[1,1,1,1]
  xslot [2,3,4,5] zslot [0,1,5,6]  d_eff=1  d_circ(Z, R=2..5)=[2,2,2,2]  d_circ(X)=[1,1,1,1]
  E(M) = [[0],[1],[2],[3],[2,3],[1,2,3],[0,1,2,3]]   (identical for all three)

non-interleaved partners, identical within-check CNOT orders:
  X block first: d_eff=1  d_circ(Z)=[1,1,1,1]  d_circ(X)=[1,1,1,1]  residual set identical: True
  Z block first: d_eff=1  d_circ(Z)=[1,1,1,1]  d_circ(X)=[1,1,1,1]  residual set identical: True
```

This is a **third** independent implementation (proposer, reviewer, me) and it agrees with the
reviewer value for value: the four denominators `2 / 27 / 176 / 769`, the compressed-convention
counts `2 / 17 / 44 / 34`, the identity of all three witnesses, the residual set, `d_eff = 1`, the
sector asymmetry of witnesses 2 and 3, and the `d_circ = 1` non-interleaved partners with identical
residual sets. **Nothing in the `[[4,2,2]]` arm is carried on paper.**

### 1.3 Spot-check B — the Gross-code enumeration that carries `d_ext ≤ 11`

I rebuilt the Gross code from the polynomials (`A = x³ + y + y²`, `B = y³ + x + x²` over
`G = Z₁₂ × Z₆`, `H_X = [A|B]`, `H_Z = [Bᵀ|Aᵀ]`), computed the kernels and stabiliser row spaces with
my own bitmask `F₂` linear algebra, and ran my own randomised information-set search for weight-12
elements of `ker(H_X) \ rowspace(H_Z)` (and the dual):

```text
dim ker(H_X) = 78   dim ker(H_Z) = 78
rank H_X = 66   rank H_Z = 66   k = 12
CSS commutation H_X H_Z^T = 0 : OK
72 translations verified to be code automorphisms
X-check orbit of row 0 covers 72/72 X-checks; Z-check orbit covers 72/72

Z-sector: check support [3,60,66,76,77,126]; pairs covered 15/15
  sample witness for (3,60): [3,19,36,41,51,60,65,67,77,117,125,141]
     weight 12, syndrome weight 0, in stabiliser row space: False
X-sector: check support [1,2,18,75,78,84]; pairs covered 15/15
  sample witness for (1,2): [1,2,10,11,14,16,20,25,75,85,86,91]
     weight 12, syndrome weight 0, in stabiliser row space: False
all checks weight 6: True; single translation orbit: True (both sectors)
```

I then re-derived the implication by hand before comparing: for **any** legal schedule and any
weight-6 Z-check with CNOT order `i₁…i₆`, a single `Z` fault on that check's ancilla after its 4th
CNOT propagates through the 5th and 6th `CNOT(q → anc)` (`Z` on target ⇒ `Z` on control), depositing
exactly `{i₅,i₆}` on the data — so `{i₅,i₆} ∈ E(M)` for every schedule. `E(M)` also contains every
singleton. Since every 2-subset of every check support sits inside an explicit weight-12 logical `L`,
the hook plus the 10 singletons of `L \ {i₅,i₆}` is a zero-syndrome, non-trivial-logical set of
**11 residuals**. Dual for X-checks. The 72 translations are automorphisms and the checks form a
single orbit, so verifying one representative check per sector is sufficient, not a sample.

**Independently reproduced, both sectors.** The argument needs no detector determinism and no
`d = 12`.

### 1.4 Claim hashes, recomputed by me

`sha256(claim.replace("\r\n","\n").strip().encode("utf-8"))`, claim read with `yaml.safe_load`, the
convention implemented by `tools/proof_dag_v6.py:claim_hash`. All seven match the `reviewed_hash`
recorded on the node, and the root's route implication hash matches its route review link.

| node | claim hash (`sha256:`) |
|---|---|
| `CIRCDIST.lift.nonint` | `864bcc604035c7124b7fa23977e00375862520a28f347d092453ddd89b6fed4e` |
| `CIRCDIST.lift.gap-example` | `487340464e4d0c6b6820d134e40bcda128ed400f131806fe091deedd64a5769c` |
| `CIRCDIST.gross.dext-cap` | `4bc0b5eb3b74b174e60f641357f5bea5b9e6a4240c390ced1bf8fd17746bff42` |
| `CIRCDIST.sat.window` | `8698b051b15fa14ff669299580d9b7bfec01808c0a34133ef09264e749466146` |
| `CIRCDIST.lift.iff` | `c3a841984a07038dfbe3390f0b25cca633d04877ff92fb04bd0e3eaf480f0061` |
| `CIRCDIST.cplx.islands` | `b4325b447807dc93f9e5f96ab503cc96800dab3e3b5b8e70e0378601121d0590` |
| `CIRCDIST.lift` (node claim) | `ccad7fa605be1ae14a2dbc1d6c5758300bb8a5f0a3023fcef84725be40e78d8a` |
| `CIRCDIST.lift` route `criterion-corollary-example` (implication) | `f39c83e6efdcc0487691df0eec57f4fe3d28d8d30c381ad7bf730fdfdfca8eda` |

Each adjudication below **binds to the hash in this table**. If a claim is edited, the verdict lapses
with the hash.

---

## 2. Verdict summary

| # | node | verdict | the §3 clause that decides it |
|---|---|---|---|
| 1 | `CIRCDIST.lift.nonint` | **PROVED-QUALIFIES** | complete argument, all load-bearing inputs reviewed; the only recorded caveat that survives is review-depth, not conditionality |
| 2 | `CIRCDIST.lift.gap-example` | **PROVED-QUALIFIES** | an existential claim discharged by exhaustive enumeration in three independent implementations; the surviving caveat is an **erratum in a descriptive numeral**, which is neither an unresolved premise nor a scope caveat |
| 3 | `CIRCDIST.gross.dext-cap` | **PROVED-QUALIFIES** | the repaired-schedule caveat attaches to the **retired** parity-rigidity clause, not to the surviving claim; the surviving claim's argument needs no schedule validity at all |
| 4 | `CIRCDIST.sat.window` | **STAYS-CERTIFIED\*** | `W-G2` is an **unproved scope condition on the claim's own universal quantifier**, and the node's own live frontier says the self-contained proof of the exact claim is still owed |
| 5 | `CIRCDIST.lift.iff` | **STAYS-CERTIFIED\*** | the claim's non-vacuity clause is a decision procedure whose lower-bound half is a theorem only for `repair ≤ 2`; the campaign's own record says the formula is probably **false** for `repair ≥ 3` |
| 6 | `CIRCDIST.cplx.islands` | **STAYS-CERTIFIED\*** | a load-bearing external theorem (`C1`, Courcelle/ALS) is **secondary-source only**: a load-bearing input that has not passed verification |
| 7 | `CIRCDIST.lift` (root) | **STAYS-CERTIFIED\*** | two binding scope conditions restrict the claim *as written* (`R ≥ d`; per-sector reading of "graph-like"), and the route premise `lift.iff` remains conditional |

Departures from the dispatcher's prior: **#4** (guessed `PROVED`, ruled `CERTIFIED*`) and **#3**
(guessed `PROVED` with a question attached — I confirm `PROVED` and answer the question: scope note,
not premise). #2's prior is confirmed but with a caveat the prior did not anticipate.

---

## 3. `CIRCDIST.lift.nonint` — **PROVED-QUALIFIES**

**Binds to** `sha256:864bcc60…fed4e`.

**Decisive sentence.** The node's single hash-bound review
(`artifacts/circdist_lift_proofs_review_20260820.md`, verdict **K**) confirms Theorem 7.1 both
line-by-line (`[D]`) and by independent reconstruction on the reviewer's own gate-level simulator
(`[N]`, 112 non-interleaved configurations across four codes at `R = 1..4`), every load-bearing lemma
of that theorem carries its own confirmation in the same review, and the node has **no route
premises and no external assumptions** — so §3's "complete argument and all load-bearing inputs
passed independent adversarial review" is met once the retired same-stack ceiling is discarded.

**Load-bearing inputs, and their hash-bound review coverage.** The node has no routes; the inputs
are the components of the Theorem 7.1 argument in
`artifacts/circdist_lift_nonint_proof_20260820.md`. All are inside the scope of the one hash-bound
review, which explicitly declares its scope as both documents' theorem and lemma layer:

| input | review coverage |
|---|---|
| Theorem 7.1 itself (`d_circ = d_eff`, all `R ≥ 1`, no graph-likeness) | verdict K, **CONFIRM** `[D][N]` — 112 configurations incl. the deliberately non-graph-like `[[15,7,3]]` |
| horizontal-representative lemma (nonint 5.4) and its case enumeration | verdict L, **CONFIRM** `[V][D][N]` — 180 configurations, 0 failures, both flavours |
| collision handling (nonint Def. 2.8 + Lemma 7.2) | verdict M, **CONFIRM** `[D]`, and identified as the *correct* treatment of the sibling document's defect |
| `(MC)` ⟺ deterministic detectors, both directions | verdict B, **CONFIRM** `[V][D]`, re-derived by the reviewer before reading |
| boundary-freeness (nonint 2.13 / Rmk 2.14) | verdict J, **CONFIRM** `[D][N]` — 141/282/423 exact two-slice patterns at `R = 1,2,3`, both temporal ends |
| sector decoupling (nonint 2.10) | §4.7, **CONFIRM** — full two-sector exhaustive search, 12/12 |
| Cor. 7.3 (`R_sat ∈ {1,∞}`) | verdict N, **CONFIRM** `[D][N]` |

**No input lacks review coverage.** The review is `reviewed_hash`-bound to exactly the current claim
(recomputed, §1.4), the reviewer declares independence, pre-reading derivations, own simulator, no
proposer code, and a limitations section.

**Caveat set that must survive on the node.**

* **DROP** — "Single same-stack (Opus 5) review; no cross-stack or human verification yet."
  (retired convention; §5 requires only a reviewer other than the author).
* **KEEP, recast as review depth (not conditionality)** — the reviewer's exhaustive arm covers the
  collision/weight accounting and 112 non-interleaved configurations across 4 codes at `R = 1..4`
  including a `[[15,7,3]]` Hamming-CSS instance with Z-degree 4; the general case rests on the
  reviewed prose derivation, checked line by line. *This is what mathematical review is; it does not
  make the result conditional.*
* **KEEP, new wording recommended** — shared model design: the reviewer's re-implementation inherits
  the 公共定义's fault inventory (Def. 1.8 / 2.5), so a systematic modelling error at that level would
  survive both implementations; the reviewer did not run `stim` for this node. The claim is
  explicitly scoped "within the closed-lift framework", so this is an honesty caveat, not a premise.
* **KEEP** — the review's §5.3 note that `k > 1` is handled per chosen observable and was not
  exhaustively swept.

**What surprised me.** The claim is *stronger* than the node's own headline suggests and the review
says so: graph-likeness is defined and never used, which is exactly why `CIRCDIST.gross` (every data
qubit of Z-degree 3, not graph-like) is entitled to import it. Also, the summary sentence "G_circ
splits into R disjoint copies of G_eff" is recorded as **false** in the node's own summary (28.4 % of
elementary faults are non-horizontal) while the claim text still says "the spacetime graph decomposes
as R disjoint copies of G_eff". The proved statement is *containment* of R pairwise-disjoint copies
via weight-preserving sections. **This is a live defect in the claim text**, not in the mathematics —
see §10, item 1. I did not let it change the verdict because the sentence is a gloss appended after
"so", and the reviewed theorem is the equality `d_circ = d_eff`; but the lead should repair and
re-hash it, and my verdict lapses with the hash if they do.

---

## 4. `CIRCDIST.lift.gap-example` — **PROVED-QUALIFIES**

**Binds to** `sha256:48734046…5769c`.

**Decisive sentence.** The claim is purely existential and is discharged by exhaustive enumeration
over a finite, fully specified schedule space; the hash-bound review
(`artifacts/circdist_numerical_review_20260820.md`, items 1–2) rebuilt that enumeration from scratch
in two implementations (own `F₂` propagator plus own `stim` 1.16.0 build, 9 936 DEM columns
cross-validated, 0 disagreements) and I have now rebuilt it a third time (§1.2) — so §3's "complete
argument … independent adversarial review" is met, and the one surviving caveat is an **erratum in a
descriptive numeral**, which §3 does not list as a ground for `CERTIFIED*`.

**Load-bearing inputs and coverage.** No routes, no premises, no external assumptions.

| input | coverage |
|---|---|
| the measurement-consistency constraint that makes the schedules legal | review §1.1, **re-derived before reading**, validated 524/524 against `stim` determinism |
| the three repaired depth-7 `[[4,2,2]]` witnesses, `d_eff = 1`, `d_circ = 2` at `R = 2..5` | review §1.2, **CONFIRM**; reproduced by me, §1.2 above |
| the non-interleaved partners with identical within-check orders, `d_circ = 1`, identical residual set | review §1.2, **CONFIRM**; reproduced by me |
| the retraction of the original depth-5 circuit (odd back-propagation parity) | review §1.3, **CONFIRM** |
| the Steane `[[7,1,3]]` depth-8 instance, `d_eff = 2 → d_circ = 3`, Z-memory | review §2, **CONFIRM** — independent reconstruction, 149/285/421/557 DEM columns matched exactly |

**Caveat set that must survive.**

* **DROP** — the same-stack caveat.
* **KEEP and sharpen** — the schedule-space convention. The 公共定义 (`CIRCDIST_PROBLEMS.md` line 58)
  says 「无意义的空闲层应当压缩掉」. Under that rule the depth-7 denominator is **44**, not 176, and the
  depth-8 witness count is 5, not 26. I confirm both numbers independently (§1.2). All three depth-7
  witnesses occupy all seven layers, so they are legal under **both** conventions and the existential
  content is untouched.
* **KEEP** — sector scope: witness 1 gaps **both** sectors; witnesses 2 and 3, and the Steane
  instance, gap the Z-memory sector only (I confirm the per-sector split independently). Under a
  `min`-over-sectors convention, witness 1 is the sole load-bearing example — which is also what the
  root's review found.
* **KEEP** — shared model design (as in §3).

**The one thing that gives me pause, stated plainly.** The claim as hashed asserts "3 of the 176
consistent ones". Under the repository's own frozen legality rule that numeral is wrong; the correct
denominator is 44. A `PROVED` node should not assert a false numeral, even a descriptive one. I did
not downgrade for it, because §3's `CERTIFIED*` is defined by *conditionality* — an unresolved
premise or a scope caveat — and an erratum in a parenthetical is neither: nothing about the result
depends on it, and the node's caveat already records the correction. But the honest disposition is
**PROVED-QUALIFIES with a mandatory claim-text repair**: change "176" to "44", or pin the convention
in the claim, then re-bind `reviewed_hash`. If the lead's house rule is that a hashed claim must be
true in every clause before it may carry a completion label, then the fallback is
`STAYS-CERTIFIED*` **pending that one-line edit** — not pending any mathematics.

---

## 5. `CIRCDIST.gross.dext-cap` — **PROVED-QUALIFIES**

**Binds to** `sha256:4bc0b5eb…6bff42`.

**The dispatcher's question — is the repaired-schedule caveat a scope note or an unresolved premise?
— answers cleanly: it is a scope note, and it does not touch the claim.** Here is the containment,
which I checked rather than accepted:

* The reviewer's break (§3.3) is that the *originally cited* translation-invariant schedule, and all
  25 920 in its class, have non-deterministic detectors. That break bites on any **circuit-distance**
  statement made on that schedule.
* The weight-6 six-hook mechanism, which the reviewer rebuilt on a repaired MC-valid non-interleaved
  depth-12 schedule with identical within-check orders, is the evidence that **refutes the retired
  clause** `d_ext ∈ {10,11,12}` by parity rigidity. That clause is **no longer in the claim** — it was
  narrowed out on 2026-08-20 and survives only in the event ledger.
* The **surviving** claim `d_ext(E(M)) ≤ 11` rests on a completely different argument, and the review
  states — correctly, and I verified it — that this argument "is a `d_ext` statement and needs **no**
  detector determinism, so it is untouched by §3.3."

**Decisive sentence.** The surviving claim's argument is a two-line propagation fact plus a finite
exhaustive coverage statement, both of which I independently reproduced from scratch (§1.3); the
hash-bound review confirms it as verdict **3d, CONFIRM (VALUE, plus a line-by-line check of the
printed argument, which is sound)**; the reviewer-repaired schedule carries only the refutation of a
clause the claim no longer contains — so no unresolved premise remains and §3's `PROVED` bar is met.

**Load-bearing inputs and coverage.** No routes, no premises.

| input | coverage |
|---|---|
| every legal schedule of a weight-6 check yields the 2-element suffix residual `{i₅,i₆} ∈ E(M)` | review §3.5, restated and checked line by line; **re-derived and re-checked by me** (§1.3) |
| every 2-subset of every check support lies in a weight-12 logical, both sectors | review §3.5 (own ISD, pool 1884/sector, 15/15 both sectors); **independently reproduced by me**, 15/15 both sectors, with explicit witnesses verified zero-syndrome and outside the stabiliser row space |
| the 72 translations are code automorphisms and the checks form a single orbit (so one representative check suffices) | verified by the reviewer via incidence relabelling; **verified by me**: 72/72 automorphisms, 72/72 orbit, both sectors |
| `E(M)` contains every singleton | elementary; checked |

**Caveat set that must survive.**

* **DROP** — the same-stack caveat.
* **KEEP, re-scoped** — the weight-6 multi-hook witness is carried on the **reviewer's** repaired
  MC-valid schedule, not on the originally cited translation-invariant schedule (which, with its
  entire 25 920-member class, violates measurement consistency). Rewrite the caveat to say what it
  actually qualifies: *the refutation of the retired parity-rigidity clause*, not the current claim.
* **ADD (new, mine)** — the `[[144,12,12]]` label asserts `d = 12`. The review verified `k = 12` and
  that randomised ISD found nothing below weight 12, and records explicitly that this is "evidence,
  not proof". I reproduce `k = 12` and the weight-12 pool. **This is not load-bearing:** the argument
  needs only that explicit weight-12 zero-syndrome non-stabiliser operators exist, which is
  witness-certified, not that 12 is minimal. The label should carry a one-line provenance note.
* **KEEP** — the absence-side readings of the G1 sweep (the histogram's "no smaller witness" side,
  the 70.7 % / 26.1 % / 15.6 % figures) are `NOT-REVIEWED` and are outside the claim.
* **KEEP** — shared model design.

**What surprised me here.** This is the strongest of the seven dossiers and it was starred with the
weakest-looking caveat set. The claim is universal over *all* schedules, and its proof is
schedule-independent by construction — the quantifier is discharged by quantifying over 2-subsets
instead of over schedules. That is why a break that killed an entire 25 920-schedule class left it
completely untouched.

---

## 6. `CIRCDIST.sat.window` — **STAYS-CERTIFIED\*** (departs from the dispatcher's prior)

**Binds to** `sha256:8698b051…466146`.

The dispatcher's prior asked me to assess "whether the scope clauses are part of the quantifier
domain or genuine conditionality". I find **one of them is genuine conditionality**, and the node's
own frontier independently says the argument is not yet complete.

**Decisive sentence.** The claim quantifies over "**every** fixed legal single-round single-ancilla
CSS schedule `M`", but sub-claim **W-G2** is an *assumed* scope clause, not a theorem — the theorem
document states in its own §8 that round-translation covariance "is **false** for a layout that
compresses idle layers across round boundaries" and that "a reviewer who reads 公共定义's idle-layer
compression as applying to the concatenated circuit rather than to `M` will find (i)–(iii)
**unproved** for that layout" — so the claim as written is broader than what is argued, which is §3's
"explicit … scope caveat", i.e. `CERTIFIED*`.

This is not a formality. The 公共定义 does impose idle-layer compression (line 58), and my own
`[[4,2,2]]` enumeration (§1.2) shows the compression rule is **materially different**, not cosmetic:
it changes the depth-7 schedule space from 176 to 44 and the depth-8 space from 769 to 34. A scope
clause that excludes exactly the layouts the frozen definition asks for is live conditionality.

**Three further reasons, each independently sufficient.**

1. **The node's own frontier says the argument is incomplete.** `task-001` (kind `task`, since
   2026-08-22, live): "Write one self-contained proof of the exact current claim, explicitly
   reconciling the recon and lift model conventions and proving the step from a contiguous minimum
   eventual witness to `R_stab ≤ d_∞` and `d_R = d_d` for every `R ≥ d`." Under §6.8 the frontier
   contains only unfinished, actionable work. A node whose own record says the self-contained proof
   of its exact claim is still owed cannot satisfy "a complete argument".
2. **`task-002` (live) asks for exactly the review the upgrade would need**: "Commission a fresh
   independent claim-level review that attacks boundary placement, schedule legality, CSS-sector
   recombination, fault collisions, and the all-schedules quantifier, and binds its verdict to the
   exact current claim hash."
3. **The hash-binding is thinner than it looks.** Of the two linked reviews, the *claim-level* one
   (`circdist_sat_window_review_20260822.md`) states in its own §0 that it "attaches to those two
   hashes only" — the theorem document and the rescope note — and it returned **FURTHER-REPAIR**. The
   review that is genuinely claim-hash-bound (`circdist_amendments4_review_20260822.md`, item 2) is a
   *focused* re-review of Amendment 1 and lists parts (i)–(iii) of the window theorem under "**Not
   re-derived**". No single hash-bound review has attacked the assembled claim.

`W-G1` (sector-min aggregation) I judge to be a **definitional inheritance**, agreeing with the
review: everything is proved per sector and survives any monotone aggregation. `W-OPEN` (does any
in-scope schedule have `R_stab ≥ 2`?) and `W-G4` (is `R_stab ≤ d_∞` tight?) are **open sub-questions,
not premises** — the claim asserts only the inequality — and correctly do not block.

**Caveat set that must survive.**

* **DROP** — "Single same-stack (Opus 5) review chain".
* **KEEP** — `S3′` (as amended) is load-bearing; `W-G3` must **not** be carried (it was refuted as
  written and *replaced*, and the replacement removes a hypothesis).
* **KEEP** — `W-G1` sector-min convention, and `W-G2` idle-compression limit, "scope conditions, not
  theorems" — with `W-G2` promoted in prominence per the decisive sentence above.
* **KEEP** — `W-OPEN`, all evidence absence-type; and the legality+`(MC)` sampling-rarity caveat
  (0/400 Steane, 1/400 rotated surface under uniform random gate orders), which fences any future
  absence search.
* **ADD (compliance gap I found)** — the clearing review's §3.5 requires the caveat set to "keep
  `W-G1`, `W-G2`, **`W-G4`**, `W-OPEN` and the §5 sampling-rarity scope caveat open exactly as
  stated". **`W-G4` is missing from the node's caveats.** It should be added regardless of level.

---

## 7. `CIRCDIST.lift.iff` — **STAYS-CERTIFIED\***

**Binds to** `sha256:c3a84198…f0061`.

I audited the dispatcher's stated reason (the UNREVIEWED 5.6(d) concern) and **it does not hold**:
the hash-bound review says in its own limitations, item 2, that the 5.6(d) concern "is **not a
premise** of the exact current `lift.iff` claim reviewed here". I also checked the second candidate
reason — the "shared residual-inventory model caveat" turning on model fact `(V)`
(`U(∅) ⊆ {0} ∪ {e_b}`) — and it is **weaker than advertised**: the base review §4.2 attacked `(V)`
directly, both numerically (440/440 empty-residual voltage vectors of weight ≤ 1) and *structurally*
("a 2-qubit fault lives on one CNOT, whose two qubits are never two Z-ancillas, so no elementary
fault can put `X` on two Z-ancillas at once"). That is a derivation from the frozen fault menu, not
an assumption. So neither of the two headline reasons survives, and I nearly upgraded this node.

**Decisive sentence.** The claim's third conjunct is an explicit **non-vacuity bar** — the criterion
must be a decision procedure that does not build the multi-round circuit — and the proof document
itself states (§4.3) that `d_circ = min_γ ℓ(γ)` "alone is a renaming" whose content is supplied by
the sandwich `|γ| + min(repair,2) ≤ ℓ(γ) ≤ |γ| + repair`; the lower half is a theorem only for
`repair ≤ 2` (§7.1 status table: "5.6 for `repair ≥ 3` — **GAP**"), and the node's own summary records
that "the clean formula is probably **FALSE** for `repair ≥ 3`" — so the clause the claim relies on
for its content is established on a restricted regime, which is §3's "explicit … scope caveat".

Two supporting points, neither sufficient alone:

* The **only** hash-bound review on this node (`circdist_amendments2_review_20260820.md`) is a
  *focused* review of Amendment 2's L1–L3 plus the assembled dossier; the base claim-level review
  (`circdist_lift_proofs_review_20260820.md`), which is where the theorems were actually attacked, is
  recorded in `events` but is **not linked in `assessment.basis.reviews`** and therefore carries no
  `reviewed_hash`. Under §5 the completion assessment must link its independent review; the node
  currently links the narrower of the two. Add the base review as a second hash-bound link.
* Model fact `(V)` is load-bearing ("`(V)` is everything", §7.3 of the proof document) and is
  **registered nowhere in the node**. Per §2, an established model fact belongs under
  `routes.<id>.assumptions` with exact scope and source; this node has no routes, so `(V)` has no
  home in the schema. That is an audit finding either way (§6.3).

**Caveat set that must survive.**

* **DROP** — "Single same-stack independent review chain".
* **KEEP** — the `repair ≥ 3` regime and the min-cost-covering extension are excluded; the located gap
  says the naive formula is probably false there. Promote this from an exclusion to a **scope caveat
  on the non-vacuity clause**, because that is what it actually qualifies.
* **KEEP** — certification is for the exact current claim and the reviewed minimum-weight
  `repair-0`/closed-lift criterion, not for the stronger formulas named as future work.
* **KEEP** — large proposer scans (98 811 surface schedules, 3 855/3 855, the 321 059/321 059
  symmetry) were not independently reproduced; the reviewer reproduced 282 instances at
  `repair ∈ {0,1}` only.
* **KEEP, re-scoped** — 5.6(d) is unreviewed but is **not a premise of this claim** (the current
  caveat leaves that ambiguous and should say so).
* **KEEP** — per-sector: everything is stated for one memory sector.
* **ADD** — model fact `(V)`, with its exact statement and the structural argument that establishes
  it, should be registered rather than left implicit.

**Path to `PROVED`, since it is short.** If a claim-level review establishes that all three conjuncts
are `repair-0`-scoped — i.e. that "the voltage is computable" means the `(LIFT′)` data, which is
one-round computable unconditionally, and not the general `ℓ(γ)` — then the `repair ≥ 3` gap becomes a
genuine *exclusion* rather than a scope caveat, and this node clears. That is a wording adjudication,
not new mathematics.

---

## 8. `CIRCDIST.cplx.islands` — **STAYS-CERTIFIED\***

**Binds to** `sha256:b4325b44…21d0590`.

**Decisive sentence.** The claim's Island III clause ("bounded-treewidth Tanner graphs
(CMSO₂/Courcelle FPT)") rests on external theorem `C1` (Courcelle, *Inform. and Comput.* 85 (1990)
12–75; Arnborg–Lagergren–Seese, *J. Algorithms* 12 (1991) 308–340; Courcelle–Engelfriet, CUP 2012),
which the write-up's own assumption table records as "bibliographic data confirmed via secondary
sources; **primary texts not read; theorem numbers not verified**" — so a load-bearing input has not
passed verification, and §3's "all load-bearing inputs passed independent adversarial review" fails
on that input alone. The clearing review reaches the same place from the other side: "`PROVED`
remains out of reach on task-003 alone."

Under §2, `assumptions` is "reserved for **already established** external theorems … with exact scope
and source". An assumption whose theorem numbering is unverified is not established to that standard.
This is a genuinely cheap gate — the frontier prices it as a primary-source check — but it is a gate.

**Two further findings that do not change the verdict but should be recorded.**

1. **The node's `assessment.summary` contradicts its own level.** It begins "`pending-review:`" and
   ends "The node remains CONJECTURED until that correction is bound and reviewed", while
   `assessment.level` is `CERTIFIED*` and the 2026-08-22 promotion event records
   `CONJECTURED → CERTIFIED*`. Per §6.1 and §6.5 the summary must state the current judgment. This is
   a stale-text erratum, not an evidential problem, but it is exactly the kind of drift the protocol's
   audit checklist exists to catch. The repository's structural checker passes (244 nodes valid), so
   nothing mechanical catches it.
2. **The caveat set is incomplete relative to its own clearing review.** That review sets the caveat
   set as "roll-up rows 1–8 **as amended by §4.3** plus the three items of §4.6" — the last being the
   unrecomputed census families (`G_{≠3}` gadget census, the 1 152 / 8 513 stabiliser-coincidence
   counts, the `[[15,7,3]]` decoupling claim, the "56 of 71" figure), the unreviewed NO side of
   Theorem V.5, and the shared-model caveat. The node carries three caveats.

**Caveat set that must survive.**

* **DROP** — "Single same-stack (Opus 5) review chain".
* **KEEP** — Courcelle/ALS/Courcelle–Engelfriet theorem numbers are secondary-source verified only
  (frontier `task-003`). *This is the caveat that decides the level.*
* **KEEP** — reviewer note N3: Amendment 4's row-8 "edit 11 un-witnessed" label is refuted
  (`G_{≠3}` meets the §6.1 promise verbatim); erratum, not a blocker.
* **ADD** — the §4.6 items above, and the Island V scope: the claim's Island V clause is the `k ≤ 1`,
  weight-`≤ 4` **YES** regime only; the general case is open (`task-004`), and hypothesis `(D)` is
  needed for the matching reading.
* **ADD** — the HGP clause's non-degeneracy proviso is a *promise*, and the review found it is
  **necessary** (46/1971 promise-satisfying instances violate the bound without it) and that the
  write-up's Theorem II.4 hypothesis is a distance condition, not poly-time checkable, while
  Lemma II.5's is.

---

## 9. `CIRCDIST.lift` (root) — **STAYS-CERTIFIED\***

**Binds to** node claim `sha256:ccad7fa6…e78d8a` and route implication `sha256:f39c83e6…fca8eda`
(both recomputed by me, both matching their linked `reviewed_hash`).

**Decisive sentence.** The root's own assessment carries two conditions its clearing review marked
**BINDING** — that "graph-like" be read **per-sector** (under the whole-DEM reading the existential
clause **fails**: the `[[4,2,2]]` witness fires 4 detectors), and that the criterion clause carries
Theorem 5.7's **`R ≥ d`** hypothesis so that "the claim as certified is quantified over memory
experiments with `R ≥ d` rounds" — and neither restriction appears in the claim text, so the claim
*as written* is strictly broader than what is argued: §3's "explicit … scope caveat", i.e.
`CERTIFIED*`.

**Independently sufficient second reason (the dispatcher's inheritance point, confirmed).** The
route `criterion-corollary-example` has premises `lift.iff`, `lift.nonint`, `lift.gap-example`. All
three carry hash-bound reviews, so the *procedural* half of §5 is satisfied for each. But `lift.iff`
remains a **conditional** result (§7), and §3's `PROVED` requires that all load-bearing inputs have
*passed* review — passing at a conditional level is not passing. Two of the three premises now
qualify for `PROVED` (§3, §4); the root is gated on the third.

**Load-bearing input inventory (for the record, since two thirds of it clears).**

| premise | hash-bound review | status after this adjudication |
|---|---|---|
| `CIRCDIST.lift.iff` | `circdist_amendments2_review_20260820.md`, `reviewed_hash` = `c3a84198…` ✓ | **conditional** — blocks |
| `CIRCDIST.lift.nonint` | `circdist_lift_proofs_review_20260820.md`, `reviewed_hash` = `864bcc60…` ✓ | qualifies |
| `CIRCDIST.lift.gap-example` | `circdist_numerical_review_20260820.md`, `reviewed_hash` = `48734046…` ✓ | qualifies (subject to §4's claim-text repair) |
| route implication | `circdist_amendments4_review_20260822.md` item 1, `reviewed_hash` = `f39c83e6…` ✓ | cleared, with the two binding conditions |

**Caveat set that must survive.**

* **DROP** — "Single same-stack (Opus 5) independent review chain … (the C-R2 stack-identity question
  … is UNDETERMINABLE-FROM-DISK and does not lift this ceiling)". The whole caveat goes: the ceiling
  it names is retired, and C-R2 (whether one child's reviewer was a different stack) is now
  **irrelevant to the level** in either direction. Keep C-R2 only as a provenance note in the event
  ledger, where it already lives.
* **KEEP (BINDING)** — "graph-like" is pinned **per-sector** (iff Def. 1.12, sector-indexed); under
  the whole-DEM reading the existential clause fails.
* **KEEP (BINDING, C-M7)** — the criterion clause carries Theorem 5.7's `R ≥ d` hypothesis.
* **KEEP** — the `repair ≥ 3` regime, the min-cost-covering extension, and the large proposer scans
  remain excluded, per the children's certifications.
* **KEEP** — under the min-over-sectors convention the `[[4,2,2]]` witness is the sole load-bearing
  example for the existential clause. *I confirm this independently* (§1.2): witness 1 gaps both
  sectors; witnesses 2 and 3 gap Z-memory only, and the review found Steane's X-memory sector gives
  `d_circ = 2 = d_eff`.

**Note for the lead.** The two binding conditions are cheap to discharge *at the claim level*: fold
"per-sector" and "`R ≥ d`" into the claim text, re-hash, and re-bind the route review. That converts
the root's own contribution from conditional to complete, at which point the root's level is governed
purely by `lift.iff` — and §7 gives a short path there too.

---

## 10. Cross-cutting findings the lead should see

1. **`CIRCDIST.lift.nonint`'s claim text contains a sentence its own summary records as false.**
   The claim ends "…so the spacetime graph decomposes as `R` disjoint copies of `G_eff`"; the summary
   says that is FALSE (28.4 % of elementary faults are non-horizontal) and the proved statement is
   *containment* of `R` pairwise-disjoint copies via weight-preserving sections. A `PROVED` label
   should not sit over that sentence. One-line repair, then re-hash and re-bind.
2. **`CIRCDIST.lift.gap-example`'s claim text asserts a denominator that is wrong under the frozen
   legality rule** (176 vs 44). Independently confirmed by me. Same disposition as item 1.
3. **`CIRCDIST.cplx.islands`' summary still says "pending-review" and "remains CONJECTURED"** while
   the node is `CERTIFIED*`. Stale text; §6.1/§6.5 violation; nothing mechanical catches it.
4. **Two caveat sets are incomplete relative to the reviews that cleared them**: `sat.window` is
   missing `W-G4`, and `cplx.islands` is missing the three §4.6 items. Both should be fixed
   independently of any level change.
5. **Load-bearing model facts have no home in the schema on route-free nodes.** `(V)` on `lift.iff`
   is singled out by its own author as carrying the entire lower bound, and it appears in no
   `assumptions` block because the node has no routes. The same is true of `C1` (Courcelle) on
   `cplx.islands` — the assumption that *decides that node's level* lives only in a caveat string and
   in a table inside a write-up. §2 confines `assumptions` to routes; a direct-proof node therefore
   cannot register an external theorem in the canonical place. This is a **protocol gap**, not a
   project failure, and it is worth a §2 amendment.
6. **The retired convention was doing more work than the record admits.** Of the seven nodes, three
   were held at `CERTIFIED*` by reasons that survive the retirement, one (`gross.dext-cap`) was held
   there by a caveat that attaches to a clause the claim no longer contains, and the reviewers' own
   ceiling language (`C-R1`: "single-stack ⇒ `CERTIFIED*` ceiling, `PROVED` unreachable on this
   route") shows the convention was being applied as a hard cap independent of the mathematics. The
   re-adjudication was worth doing.

---

## 11. What I did **not** do (NOT-ADJUDICATED / NOT-REVIEWED by me)

1. I re-verified **two** load-bearing computations with my own code (§1.2, §1.3). Everything else is
   adjudicated on the documents: I read the reviews' verdicts, scopes, limitations and the relevant
   proof sections, and checked internal consistency, but I did not re-run the Steane arm, the surface
   arm, the G1 sweep, the window theorem's simulations, or any islands computation.
2. **`CIRCDIST.sat.window` parts (i)–(iii)** I did not re-derive. My verdict turns on the scope
   clause `W-G2`, the live frontier, and the hash-binding structure — all of which are on the record —
   not on the correctness of the monotonicity, contiguity or window arguments, which the claim-level
   review confirmed and which I have no reason to doubt.
3. **`CIRCDIST.cplx.islands` islands I–V** I did not re-derive. My verdict turns on one unverified
   external theorem citation. If a session reads the primary texts and the numbers check out, the
   remaining question is whether the rest of the dossier (which no single hash-bound review has
   attacked end to end — the clearing review is focused, and the base review is not linked with a
   hash) meets the bar; I express no view on that.
4. **`CIRCDIST.lift.iff`'s `repair ≥ 3` gap** I did not attempt, and I did not search for a
   `repair ≥ 3` instance (that needs `d ≥ 5`).
5. **I took no position on C-R2** — which model stack executed which prior review. Under canonical §3
   it does not bear on any level, which is precisely why I did not spend budget on it.
6. **My own work is unreviewed.** The two reproductions of §1.2–§1.3 are a second and third
   measurement, not a proof; my `[[4,2,2]]` propagator reads the same frozen fault inventory as the
   documents it checks, so the shared-model caveat of §1.1(3) applies to me too. My Gross-code
   verification is more nearly independent — it is pure `F₂` linear algebra over the published
   polynomials and touches no circuit model at all.
7. **I promoted nothing and wrote nothing except this file.**
