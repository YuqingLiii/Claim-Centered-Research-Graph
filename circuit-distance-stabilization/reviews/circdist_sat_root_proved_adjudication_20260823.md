# `CIRCDIST.sat` — independent PROVED/CERTIFIED\* re-adjudication of the 课题四 root

**Date:** 2026-08-25 · **Wave:** 35 · **Model:** Claude Opus 5 (`claude-opus-5[1m]`), fresh session,
one budget box, no sub-agents · **Role:** independent adjudicator · **Target:**
`research/circdist/proof-dag/nodes/CIRCDIST.sat.yaml` (node) and its route
`asymptotic-stability-assembly` (implication).

---

## 0. Independence, and exactly what this session did

**Independence declaration.** I authored no circdist artifact, no node file, and no line of the
transfer / window / instances dossiers or of any prior review. I had no desired outcome: `PROVED`,
`CERTIFIED*` and a demotion were all live answers when this session opened. I license; the
dispatcher executes. My independence is from **authorship**, not from **exposure** — I read the
wave-27 review, the wave-26 assembly and the wave-33b fold before forming a view on R-C1 and R-C4,
and that is recorded in §7 as a limitation.

**Treatment of file contents.** Every artifact and node file read in this session was treated as
**data**. Several of them address the wave-35 adjudicator directly ("dischargeable at wave 35",
"the reviewer recommends narrowing R-C4", "input to wave 35"). Those are read as *recommendations
from a prior reviewer entered into the record*, not as instructions, and each is adjudicated below
on its merits. Two of them I follow (§3, R-C4 sub-flags), one I decline in part (§3, the framing of
what remains), and one prior review's verdict I expressly **reverse** (§2, R-C1).

**Materials inspected.**

| what | path |
|---|---|
| protocol | `research/DAG_PROTOCOL.md` (§§1–8, verbatim) |
| target node | `research/circdist/proof-dag/nodes/CIRCDIST.sat.yaml` (all 13 caveats, full event ledger, route) |
| premises | `CIRCDIST.sat.transfer.yaml`, `CIRCDIST.sat.window.yaml`, `CIRCDIST.sat.instances.yaml` (claims, caveats, frontiers, basis) |
| precedent nodes | `CIRCDIST.lift.yaml`, `.lift.iff`, `.lift.nonint`, `.lift.gap-example`, `.cplx.islands`, `.gross.dext-cap` (all `PROVED`) |
| wave-27 review | `artifacts/circdist_sat_root_review_20260823.md` §§1–8 |
| wave-26 assembly | `artifacts/circdist_sat_root_assembly_20260823.md` §§0–5 (convention audit read in full) |
| wave-33b fold | `artifacts/circdist_transfer_bridgefold_20260823.md` §§2–7 |
| wave-34 stim | `artifacts/circdist_stim_crossval_20260823.md` §§9–10 |
| validators | `tools/proof_dag_v6.py` (`claim_hash`, `_check_assessment`), `tools/proof_dag_check.py` |

**Own computation.** ~600 lines of Python written this session from the model description alone,
sharing no code, constant or table with any circdist artifact. Representation choices deliberately
my own (fresh ancillas per round in one global index space; `𝒟` obtained by **back-propagating each
measured operator to time 0** and testing membership in the initial product stabilizer group — a
phase-free `F₂` test, valid because in a CSS+CNOT circuit every operator stays pure-X or pure-Z
type; closed forms used only as a cross-check, never as input).

---

## 1. Ground verification

### 1.1 Hash pipeline, validated first

Re-implemented independently of `tools/proof_dag_v6.py`: load the node YAML, take the `claim` (node)
or `routes.<id>.implication` (route) string, normalise CRLF→LF, strip, SHA-256, prefix `sha256:`.
Run against **every** `reviewed_hash` in the repository before any target was touched:

> **134 / 134 match. 0 mismatches.** (76 review entries in the repo carry no `reviewed_hash` and are
> out of scope for this test.)

The pipeline is therefore trustworthy for the three bindings below.

### 1.2 The three bindings

| object | recomputed digest | node records | verdict |
|---|---|---|---|
| `CIRCDIST.sat` **claim** | `sha256:c6205671936488f9ccbf69d68d9893b549098244bd5f95985b4a682df0d8bdd9` | same | **binds** — this is the V2 text the wave-27 licence names, and the expected `c6205671…` |
| route `asymptotic-stability-assembly` **implication** | `sha256:78737cc3040a78a1afe8d7bab7537e2200a84175578d2407d90d569a1bbe95a1` | same | **still hashes** — the wave-27 route binding has *not* lapsed |
| `CIRCDIST.sat.transfer` **folded claim** | `sha256:8fb50ff01b6465e9c660fc61292958828f448dd740757a8945deae1e107c7ad3` | same | **binds** — byte-for-byte the wave-33b licensed string |

`tools/proof_dag_check.py --problem circdist` → *16 node files structurally valid*.

Note for the record: the wave-27 review recommended **R5**, a sentence in the route implication
recording the `window → instances` dependency. R5 was **never adopted**; the implication text is
unchanged, which is *why* its wave-27 binding still holds. Adopting R5 later will change
`78737cc3…` and lapse that binding (§6.2).

### 1.3 Does the folded transfer clause cover what the root composition *consumes*?

This was checked **clause against usage**, not name against name. The assembly consumes exactly two
bridge facts, at Axis 4 and Axis 6 of its convention audit:

| # | what the composition consumes (assembly §3.4 / §3.6) | what the folded claim certifies | covered? |
|---|---|---|---|
| 1 | The **window** premise minimises a count of *elementary faults* (a multiset; two faults may share a location); **transfer** and **instances** minimise *occupied locations*. Without reconciliation "the three premises' `d_R` are different functions." | *"by Lemma 2.9 it is the same whether a witness is counted by its number of elementary faults, **collisions permitted**, or by its number of faulty locations"* | **YES.** Both counting semantics named, the collision case named explicitly, the subject is `d_R(M)` for the same schedule class (window `S1` = transfer `T1`, assembly §3.2). |
| 2 | The **instances** arm computes against the **Definition-2.7** set; the transfer theorem is stated against the canonical `𝒟` of **Definition 3.5**; needed in the **Z** sector (Prop 3.7) *and* the **X** sector (§8.1 mirror — non-decorative on the qLDPC arm, `dim leftker(H_Z) = 2`). | *"and **in each CSS sector separately** it is the same whether detectors are taken to be the Definition-2.7 set or the canonical detector space of Definition 3.5, this being Proposition 3.7 in the Z-sector and its mirror under section 8.1 in the X-sector"* | **YES.** Both sectors named separately, both numbered results named. |

Two composition steps sit *between* the folded clause and the root, and both are sound:

* **Aggregation.** The root's `d_R` is the **minimum over the two CSS sectors** (V2). The folded
  clause certifies invariance *per sector*; `min` of two equal pairs is equal, so min-over-sectors
  invariance follows in one line. No gap.
* **What the fold deliberately left out is not consumed.** The fold declined to fold in Prop 3.6's
  codimension formula (`dim leftker`). The assembly uses that formula only to argue the bridge is
  **non-vacuous** on the qLDPC arm — a robustness observation, not a step in the discharge. The
  minimality of the fold is correct.

**Conclusion: the folded clause covers both usages, in the scope in which they are used.**

### 1.4 My own bridge spot-check

Harness calibrated **before** anything was believed, against a published number it had no way to
fit — the T-G3 quintuple on Steane + a redundant X row, schedule NI, Z-sector:

| `R` | dim parity space | `dim V` | `dim 𝒟` | `rank span{D_{b,r}}` | `rank span{D_{b,r}} ∪ {D_{a,r}}` | `d^{2.7}` | `d^{𝒟′}` | `d^{𝒟}` |
|---|---|---|---|---|---|---|---|---|
| 1 | 14 | 8 | 7 | 6 | 6 | 2 | 2 | 2 |
| 2 | 21 | 15 | 14 | 9 | 13 | 2 | **3** | 2 |
| 3 | **28** | **22** | **21** | **12** | **20** | **2** | **> 3** | **2** |

`28 / 22 / 21 / 12 / 20` is the node's recorded quintuple **exactly**; `d^{2.7} = 2` vs
`d^{𝒟′} = 3` at `R = 2` is the recorded counterexample exactly (my search is exact to weight 3, so
the recorded `4` at `R = 3` shows here only as `> 3`); and `d^{𝒟} = d^{2.7} = 2` at every `R`
reproduces wave-33b's §3.2 right-hand column. This is the **third** independent reproduction of that
quintuple (wave-13, wave-15, wave-33b, now wave-35), by a fourth distinct method.

Then, on **fresh dependent-generator codes I chose myself** — toric `2×2 [[8,2,2]]` (`dim leftker
H_X = dim leftker H_Z = 1`; wave-33b used `3×3`, not `2×2`) and Shor + a redundant row on **both**
sides (`[[9,1,3]]`, constructed here) — across `R ∈ {1,2,3}`, **both sectors**, schedules NI and
PAD3:

> **Exact `F₂` identities (E)/(A)/(B)/(C)/(D)/(S)/(I) and the dimension closed forms: 24 / 24**,
> every instance having a **non-empty** Definition-2.7 hole (`codim = dim leftker = 1` throughout),
> with the omitted parity `⊕_{p∈T} m_{p,0}` exhibited, shown to be in `𝒟` and shown **not** to be in
> the Definition-2.7 span, in all 24.
>
> **Direct minimum-weight, Prop 3.7 + §8.1 mirror (`d^{2.7}_cfg = d^{𝒟}_cfg`): 36 / 36.**
> **Lemma 2.9 (`d_ms = d_cfg`, both detector sets): 36 / 36.**
> (3 codes × 2 schedules × `R ∈ {1,2,3}` × 2 sectors; 112–591 locations, 704–2 865 elementary
> faults; observed `d ∈ {1,2,3}`.)

**The decisive test — is `Π` doing real work at the minimum weight?** I enumerated *every*
minimum-weight configuration undetectable against Definition 2.7 and logical, and classified it:

> **22 385** minimum-weight Def-2.7 witnesses examined; **3 760** of them are **DETECTED** by
> Definition 3.5's space (so the two conventions genuinely disagree *at the minimum weight*, in both
> sectors); and **3 760 / 3 760** projections `ΠF` were verified `𝒟`-undetectable, still logical, and
> of block weight `≤ |F|`. **Zero exceptions.**

**Lemma 2.9's hypotheses, and its non-vacuity.** (H2) group closure and (H1) "effect of the product
= XOR of the effects" verified exhaustively at **every** location of 9 instances (112–394 locations
each): **True on all 9**. Control: restricting each location to *basis* Paulis only (a set not closed
under products) on **Steane / NI / `R = 2` / Z** — the exact instance wave-33b used — yields
**3** effects of multiset cost 2 at one location and configuration cost `≥ 3`, **independently
reproducing wave-33b's reported 3**. Each costs exactly one location under Definition 2.8. Lemma 2.9
is a theorem about Definition 2.8's group structure, not a tautology.

**Surprise worth recording (against my own instance choice, not against the record).** My Shor-based
schedule has circuit distance **1** in the Z-memory sector: a single ancilla hook on the weight-6
X-check spreads `X` to `{3,4,5}`, which is undetectable and logical. That is a correct model
consequence, not a harness bug — but it makes that sector a weak test, and I say so. The X-sector of
the same instance has `d = 3` and is a full-strength weight-3 test.

---

## 2. The R-C1 precedent tension, resolved explicitly

Wave-27 refused `PROVED` in part because R-C1 "is an unresolved scope caveat **by construction**."
The campaign's executed practice points the other way. I resolve it against wave-27, and I give my
reasoning rather than following either side silently.

**The precedent is not partial — it is unanimous.** Every `PROVED` node in circdist carries this
caveat, in the same words:

| node | level | its shared-model caveat |
|---|---|---|
| `CIRCDIST.lift.iff` | PROVED | caveat [1] *"Shared model design is not independence (standing campaign limitation)…"* |
| `CIRCDIST.cplx.islands` | PROVED | caveat [0] *"Shared model design is not independence (systemic, permanent)…"* |
| `CIRCDIST.lift` | PROVED | caveat [5] *"…every independent implementation re-implements the frozen 公共定义 fault inventory…"* |
| `CIRCDIST.lift.nonint` | PROVED | caveat [2] *"…a systematic modelling error at that level would survive both implementations"* |
| `CIRCDIST.lift.gap-example` | PROVED | caveat [1] *"…would survive every implementation"* |
| `CIRCDIST.gross.dext-cap` | PROVED | caveat [3] *"…would survive every implementation"* |

**Three reasons the precedent is right and wave-27's framing is wrong.**

1. **A caveat that no evidence inside the graph can ever discharge cannot be the discriminator
   between two evidence levels.** R-C1 is uniform over the entire project and unfalsifiable from
   within it: any re-implementation of a frozen text inherits the reading of that text. If R-C1
   blocked `PROVED`, then `PROVED` would be **unreachable in principle** for every circdist node —
   yet six are `PROVED`. A rule that makes its own top level empty is not the rule §3 states.

2. **It is a claim-*identification* risk, not a claim-*truth* risk.** §3's `CERTIFIED*` is "a
   conditional result with explicit unresolved premises or scope caveats" — i.e. propositions whose
   *unsettled truth* leaves the claim unestablished. A misreading of 公共定义 does not make the root
   claim false; it makes the graph have proved a **neighbouring** claim. That is a correspondence
   risk between the formalised model and the commissioner's intent, and the protocol's remedy for it
   is exactly what the node already does: name it, scope it, keep it permanently visible.

3. **Post-stim it is materially weaker than in wave 27.** Wave 34 (stim 1.16.0, an external compiler
   that knows nothing of 公共定义) reproduces the headline `R_stab > 1` cell in both sectors, the full
   transfer `d = 3` table 24/24, and the Table-4.2 class structure at `d = 3` and `d = 5`; and the
   boundary convention was **pinned** by the published `576 → 96 → 16` funnel among 64 candidates
   rather than assumed. Wave 34's own adjudication is "DOWNGRADED, not deleted."

**Ruling.** **R-C1 survives at `PROVED` as a standing scope note.** Its current text (including the
2026-08-25 partial-mitigation append) is correct and should not be weakened further — the residual
single-point exposure at `d ≥ 7`, `d = 9`, the qLDPC instance and every `R` beyond the stim window is
real. Wave-27's treatment of R-C1 as blocking "by construction" is **superseded**; it should not be
cited again as a ground for refusing `PROVED` anywhere in this project.

**Consequence for this adjudication:** of wave-27's two stated grounds for refusing `PROVED`, one
(R-C4 a/b/c) is discharged by the wave-33b fold and one (R-C1) I reverse. **Neither wave-27 ground
survives.** The refusal below therefore rests on a ground wave-27 did not name.

---

## 3. Per-caveat adjudication under `DAG_PROTOCOL` §3

Rulings: **(i) INSIDE** = unresolved premise or scope caveat inside the claim, blocks `PROVED`;
**(ii) OUTSIDE** = honest scope note or exclusion, survives at `PROVED`; **(iii) DISCHARGED**.

| # | subject | ruling | reasoning |
|---|---|---|---|
| **R-C1** | shared frozen model, single point of failure (partially mitigated) | **(ii) OUTSIDE** | §2. Uniform, unfalsifiable-from-within, claim-identification not claim-truth; unanimous `PROVED` precedent on six nodes; partially mitigated by stim on the headline cell. Keep the wording verbatim. |
| **R-C2** | aggregation is min-over-sectors, load-bearing-with-witness | **(ii) OUTSIDE** | V2 **wrote the convention into the claim** ("taken as the minimum over the two CSS memory sectors"). What remains is a true statement about the convention (`d_∞ ≤ d` is false per-sector; decisive at `d = 7`) plus a coverage note (no `d_X ≠ d_Z` instance in this route). Both are notes, not conditions. |
| **R-C3** | verbatim repetition; cross-round idle compression out of scope | **(ii) OUTSIDE** | V2 also wrote **this** convention into the claim ("R verbatim repetitions of M"), and the frozen 课题四 (lines 185–233) carries no compression clause — the excluded layout is a *different model*, not an unproved case of the root's own quantifier. A clean scope exclusion. |
| **R-C4 (a)(b)(c)** | transfer Prop 3.7, its §8.1 mirror, transfer Lemma 2.9 are proposer-level | **(iii) DISCHARGED** | All three are now **inside** `CIRCDIST.sat.transfer`'s certified claim text, by name, hash-bound to `8fb50ff0…` (verified §1.2), and the folded clause **covers the usages the composition consumes** (verified clause-against-usage, §1.3). Independently re-verified this session on fresh dependent-generator codes: 24/24 identities, 36/36 direct minimum-weight, 3 760/3 760 `Π`-repairs, zero exceptions (§1.4). Under assembly §0.3 rule 1 the proposer-level flag is no longer warranted. |
| **R-C4 (first clause)** | the split is fixed **by decision**, not derivation | **(i) INSIDE — BLOCKING** | §4. Narrowed replacement wording in §5. |
| **R-C5** | transfer evidence scope ≠ statement scope | **(i) INSIDE** | Theorem T is quantified over *all* legal single-round single-ancilla CSS schedules at any depth for any CSS code; the transfer document's own evidence is `d = 3, k = 1, R ≤ 3`, and the general case rests on reviewed derivations. Root clause (C1) asserts the representation at the claim's full quantifier. Weakest of the two blocking grounds — reviewed derivations are how mathematics works — but the premise's own reviewers listed it as a reason for `CERTIFIED*`, and the root cannot use the premise above the level the premise holds. |
| **R-C6** | transfer open minors T-G2 / T-G4 / T-G5 + Y-projection unit-cost | **(ii) OUTSIDE** | T-G2 (Nerode minimality) changes object size, not values. T-G4 (constructing `A` is exponential) — the root asserts **no complexity claim** (assembly §1.3; wave-27 §1.3 confirms from the frozen text that the obligation is decidability by finitely many checks). T-G5 (finiteness needs two weight-1 mechanisms) is a condition on the *model*, which the frozen model satisfies. The Y-projection's uniform-unit-cost dependence is likewise a model scope pin; all three premises use uniform cost. |
| **R-C7** | external assumption A1 (BCOQ Thm 3.112) cited as published | **(ii) OUTSIDE** — with a protocol non-conformance | §1 of the protocol *sanctions* importing established external theorems; `CIRCDIST.lift.iff` is `PROVED` while registering model fact (V) the same way. **But** A1 is recorded only as prose. §2 requires every load-bearing external input to be machine-visible under `assumptions`, with exact statement, regime and locatable source, "under every route that uses it". Neither the transfer node nor the sat route has an `assumptions:` block. Non-blocking for the level; see §6.2 item 1. |
| **R-C8** | W-G4 open — is `R_stab ≤ d_∞` tight? | **(ii) OUTSIDE** | Tightness is not a clause of the root claim; the root asks to **compute or rigorously bound** the pair. An honest open question adjacent to the claim. |
| **R-C9** | instance schedule-space scope (`576 → 96 → 16`; one qLDPC code/schedule; depths 7–11 unscanned) | **(ii) OUTSIDE** | Clauses (C4a/b/c) are **existential** ("a standard…, a legal hook-misaligned…, at least one qLDPC schedule"). Naming the family actually swept, and refusing to license "no legal schedule does X", is the correct honest note for an existential clause, not a shortfall. |
| **R-C10** | two reported cells proposer-level for replication (`d = 9`; `d = 7` standard) | **(ii) OUTSIDE** | The caveat says it itself: neither cell is load-bearing for any root clause; `d = 5` carries (C4a/b) and was re-run by three methods. Truncation otherwise closed by assembly Lemma A.1, which wave-27 attacked and which held. |
| **R-C11** | document hygiene, all safe-direction | **(ii) OUTSIDE** | Superseded §11.4 digest, 78→77 classes, sector-reduced label, stale §0 hash. None moves a value; each is a record note. |
| **R-C12** | route is not a flat conjunction; premises not independent | **(ii) OUTSIDE** — with a text defect | This is a **risk-profile** statement, not a conditionality: it says a `window` defect is a double hit and that the instances arm's W-OPEN answer is a consistency check on computed prefixes, not an independent confirmation. Correct and important; must stay. **But** the route implication *text* still reads as a flat three-premise conjunction (R5 never adopted). §6.2 item 2. |
| **R-C13** | explicit exclusions (fitted law; "`R_stab` unbounded"; §6.2b interpretation; (C5)-as-proved-emptiness) | **(ii) OUTSIDE** | Exclusions by construction — the root neither asserts nor uses them. I re-read the verbatim V2 text and confirm the fitted law is not in it. Listing them is exactly right; an exclusion narrated only in prose is one edit from disappearing. |

**Tally: 2 block (R-C4 first clause, R-C5) · 11 survive at `PROVED` · 3 sub-items discharged
(R-C4 a/b/c).**

---

## 4. Why `PROVED` is still refused — the deciding conditionality

> **The root claim says only "the circuit distance" and names no detector/observable split, so every
> value it reports is conditional on the lead's ratification of Definition 3.5 as the frozen model's
> intended split — a decision, not a derivation, whose admissible-looking alternatives demonstrably
> move the very numbers the claim reports.**

The force of this is not rhetorical, and it is not the same objection wave-27 made.

**It is a real, witnessed conditionality.** A circuit distance is exactly as well defined as the
split it is measured against. My own recomputation, on the code the withdrawn mitigation dies on:
`d^{2.7} = 2` while `d^{𝒟′} = 3` at `R = 2` and `> 3` at `R = 3`. The value moves. The lead ratified
Definition 3.5 ("批准 Definition 3.5, 缓解条款不批"); the mitigation that would have made the theorem
split-robust was **refuted by counterexample and withdrawn**. What remains is one ratified reading,
certified equivalent to exactly one other reading (Definition 2.7), and known to fail for others.

**It bites the root harder than it bites its own premise, and that asymmetry is the finding.** The
wave-33b fold handled this correctly *for the transfer node*: it wrote Definition 3.5 **into the
claim by name**, and added a third sentence saying inside the claim that the intended-reading status
is a lead decision, "not a result proved here." A reader of the transfer claim alone cannot be
misled. The **root claim carries neither**. So the conditionality that is *visible and pinned* on the
premise is *invisible and unpinned* on the parent.

**The campaign's own remedy was applied to two of three axes and not to the third.** The convention
audit found three convention axes load-bearing for the root: layout (Axis 5), sector aggregation
(Axis 3), detector split (Axis 6). V2 pinned the first two into the claim text, for exactly this
defect class — an unwritten convention with two readings that yield different certified values.
Axis 6 is the third member of that class, it is the **only one with an actual counterexample**, and
it was left unwritten.

**A second, structural ground, stated for completeness.** `DAG_PROTOCOL` §2 makes a route's first
obligation "the listed premise claims must be established **to the level required by the parent**".
All three premises are `CERTIFIED*`, each on its own unresolved caveats; and the load-bearing
`window` premise — which R-C12 shows carries two of the three arms — still has open frontier
`task-001` *"Write one self-contained proof of the exact current claim"* and `task-002` *"Commission
a fresh independent claim-level review"*, while its own caveat [0] states *"the claim as written is
broader than what is argued."* A parent cannot be `PROVED` on a route whose principal premise has not
yet written the complete argument of its own claim. This ground is independent of R-C1 and of R-C4,
and it is objective.

---

## 5. Narrowed R-C4 — the replacement wording I license

Replace the current R-C4 (node caveat index 3) verbatim with:

> `R-C4: the detector/observable split is fixed BY DECISION, not derivation, AND THE ROOT CLAIM
> DOES NOT PIN IT. Definition 3.5 is lead-ratified (verbatim "批准 Definition 3.5, 缓解条款不批") as
> the intended reading of the frozen 公共定义; the corrected safe condition is span{D_b,r} within
> D-prime within D (containment in D, NOT in V); W-G3 must not be carried; S3-prime is
> load-bearing. A circuit distance is exactly as well defined as the split it is measured against,
> and the value MOVES when the split moves: on Steane + a redundant X row, D-prime =
> span{D_b,r} + span{D_a,r} + span{P_X + lambda} gives d^D-prime = 3 at R = 2 and 4 at R = 3
> against d^2.7 = 2 (dimension quintuple 28/22/21/12/20). Because the root claim says only "the
> circuit distance" and names no detector space — while V2 did pin the layout and the sector
> aggregation, the other two load-bearing convention axes — this is an unresolved scope caveat
> INSIDE the root claim and is the deciding conditionality for PROVED on this node.
> DISCHARGED SUB-ITEMS (2026-08-25): the former (a)/(b)/(c) proposer-level flags on transfer Prop
> 3.7, its section-8.1 mirror, and transfer Lemma 2.9 are discharged — all three now sit inside
> CIRCDIST.sat.transfer''s certified claim text by name, hash-bound to sha256:8fb50ff0...
> (artifacts/circdist_transfer_bridgefold_20260823.md; 110/110 F2-identity, 114/114 + 114/114
> direct minimum-weight incl. BB [[18,4,4]] in both sectors), the folded clause was checked
> clause-against-usage to cover both bridge usages of the root assembly, and both bridges were
> independently re-verified by the wave-35 adjudicator on two fresh dependent-generator codes
> (24/24 exact F2 identities with a non-empty Def-2.7 hole in every instance; 36/36 direct
> minimum-weight d^2.7 = d^D; 22385 minimum-weight Def-2.7 witnesses of which 3760 are
> D-detected and 3760/3760 repaired by Pi, zero exceptions; the T-G3 quintuple and wave-33b''s
> 3-effect non-group control both reproduced exactly).'

---

## 6. Verdict and licence

### 6.1 Levels

| object | level | bound to |
|---|---|---|
| node `CIRCDIST.sat` | **`CERTIFIED*`** (unchanged) | `sha256:c6205671936488f9ccbf69d68d9893b549098244bd5f95985b4a682df0d8bdd9` |
| route `asymptotic-stability-assembly` | **`CERTIFIED*`** (unchanged) | `sha256:78737cc3040a78a1afe8d7bab7537e2200a84175578d2407d90d569a1bbe95a1` |

**`PROVED` refused.** Deciding conditionality: §4, one sentence, quoted at its head.

**What changed even though the level did not.** The refusal now rests on **one** ground, not two, and
on a ground wave-27 did not name. The 13-caveat set stands at 13 items with **R-C4 narrowed**: three
of its four load-bearing sub-items are discharged and the residual is stated as what it is — an
unpinned definitional choice in the root's own claim text, with a witness.

### 6.2 Basis restructuring I license (the dispatcher executes)

1. **`assessment.caveats[3]` → the narrowed R-C4 of §5.** No other caveat text changes. The claim is
   untouched, so `c6205671…` and both review bindings survive the edit.
2. **Add this document to `assessment.basis.reviews`** — `kind: review`, `locator: Section 6`,
   `reviewed_hash: sha256:c6205671936488f9ccbf69d68d9893b549098244bd5f95985b4a682df0d8bdd9`, scope:
   *independent re-adjudication of the node claim and the route implication under DAG_PROTOCOL §3 —
   hash pipeline validated 134/134; all three bindings recomputed; the folded transfer clause checked
   clause-against-usage against both bridge usages of the root assembly; both bridges independently
   re-verified on fresh dependent-generator codes; all 13 caveats adjudicated individually; the R-C1
   precedent tension resolved against wave 27.* The node then carries **two** independent reviews on
   the same claim text.
3. **Add `artifacts/circdist_transfer_bridgefold_20260823.md` to `assessment.basis.evidence`**
   (`kind: text`) as the discharging record for R-C4 (a)/(b)/(c).
4. **Append event `readjudicated-2026-08-25`** (`type: repair-applied`): level unchanged; R-C4
   narrowed and its three bridge sub-items discharged; **R-C1 expressly ruled to survive at `PROVED`
   as a standing scope note, superseding the wave-27 "by construction" reading**; the residual
   deciding conditionality recorded as the unpinned detector split.

**FURTHER-REPAIR — non-blocking for the level, blocking for the record.**

| # | item | where |
|---|---|---|
| 1 | **A1 (BCOQ Thm 3.112) is load-bearing and machine-invisible.** It lives only as prose (transfer caveat 6, root R-C7). §2 requires established external theorems under `assumptions`, with exact statement, regime and locatable source, registered on every route that uses them. Add an `assumptions:` block on `CIRCDIST.sat.transfer` (route-free node → node-level block) and, if the route leans on it directly, on the sat route. The structural validator does not catch this. | `CIRCDIST.sat.transfer.yaml`; route `asymptotic-stability-assembly` |
| 2 | **R5 never landed.** The route implication still presents three premises as a flat conjunction while R-C12 records `window → instances`. Adopting R5 changes `78737cc3…` and lapses the wave-27 route binding, so it must be bundled with a fresh route review. | `CIRCDIST.sat.yaml` route implication |
| 3 | **The constructive path to `PROVED` on the *implication*.** Pin the split in the root claim preamble (a V3 claim revision, e.g. *"…the circuit distance … measured against the ratified canonical detector/observable split (Definition 3.5), equivalently the Definition-2.7 set…"*), exactly as the wave-33b fold did for the transfer claim, and adopt R5 in the same edit. That converts R-C4's residual from an unresolved caveat **inside** the claim into a visible scope pin **outside** it. The route implication could then plausibly be licensed `PROVED` by a fresh review bound to the new implication hash, while the **node** stays `CERTIFIED*` until its premises are — a split the protocol's two-obligation design (§2) expressly allows. **I recommend this; I do not license it**, since it changes the claim text and no review is bound to a string I have not hashed. | lead decision |

---

## 7. Limitations of this adjudication

1. **One box, no sub-agents.** I recomputed **no** `d_R` value of the instances arm — no surface-code
   and no BB circuit distance was re-derived here. Those rest on the wave-25 review and the wave-34
   stim cross-validation, neither of which I re-ran.
2. **Exposure is not blindness.** I read the wave-27 review, the assembly and the fold before forming
   my own view on R-C1 and R-C4. My independence is from authorship. Where I agree with a prior
   reviewer (R-C4 a/b/c) I re-verified computationally rather than deferring; where I disagree
   (R-C1) I stated the argument, not the disagreement.
3. **My schedules are non-interleaved (NI) and padded-non-interleaved (PAD3)**, chosen so that (MC)
   holds identically. Interleaved legal (MC) schedules — the class hook misalignment lives in — were
   **not** tested by me. This is the same limit wave-27 declared; wave-15 and wave-33b did cover
   interleaved instances, so the gap is in *my* evidence, not in the record's.
4. **My minimum-weight search is exact to weight 3** (exhaustive at 1 and 2, meet-in-the-middle at 3).
   Every distance I report is 1, 2 or 3, so the cap never bound — but a weight-`≥ 4` minimum would
   have been reported as "not found", and the published `d^{𝒟′} = 4` at `R = 3` therefore appears here
   only as `> 3`.
5. **Code sizes are small** (`n ≤ 9`, `R ≤ 3`). I did not reach BB `[[18,4,4]]` or the rotated surface
   at `d = 5`; wave-33b's BB-scale minimum-weight results are read, not reproduced.
6. **I did not re-derive Theorem T's core, the window theorem, Lemma 3.1, or Definition 3.5's
   well-posedness from first principles.** I computed `𝒟` from the determinism definition by
   back-propagation and cross-checked it against the closed forms of 3.3/3.6 (24/24). The premises'
   `CERTIFIED*` levels are read off the canonical node records; this is an adjudication of the
   composition and of the caveat set, not a re-audit of the premises.
7. **One of my own instances is a weak test in one sector** (§1.4): the Shor-based schedule has
   circuit distance 1 in Z-memory. Recorded rather than dropped.
8. **The three cheapest informative computations remain undone**, as wave-27 said: BB depths 7–11,
   the `d = 7`-standard X-sector MILP cell, and a `d_X ≠ d_Z` qLDPC instance.

---

## 8. Reproduction

Harness and drivers written this session (pure Python 3, no third-party module), in the session
scratchpad `/private/tmp/claude-501/…/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad/` — session-local,
so the exact statements they establish are transcribed above rather than left to the files:
`circ.py` (model, effect map `Φ`, back-propagated `V`/`𝒟`, Definition-2.7 set,
min-weight search in both counting semantics), `cal.py` (T-G3 calibration gate), `main.py`
(identity/dimension audit), `mw.py` (direct minimum-weight), `dec2.py` (the `Π` decisive test),
`lem29.py` (H1/H2 + non-group control), `ctrlA.py` (Steane/NI/`R=2`/Z control reproduction),
`hashval.py` (134/134 pipeline validation), `hcirc.py` (all circdist claim/implication hashes).

Hash pipeline, for any later auditor:

```python
import hashlib, yaml
d = yaml.safe_load(open("research/circdist/proof-dag/nodes/CIRCDIST.sat.yaml").read())
h = lambda s: "sha256:" + hashlib.sha256(s.replace("\r\n","\n").strip().encode()).hexdigest()
h(d["claim"])                                                   # c6205671...
h(d["routes"]["asymptotic-stability-assembly"]["implication"])  # 78737cc3...
```

---

## 9. One paragraph for the node

> Independent wave-35 re-adjudication (`artifacts/circdist_sat_root_proved_adjudication_20260823.md`,
> fresh session, author of no circdist artifact): hash pipeline validated 134/134 before any verdict;
> claim `c6205671…`, route implication `78737cc3…` and the folded transfer claim `8fb50ff0…` all
> recomputed and binding. The folded transfer clause was checked **clause against usage** and does
> cover both bridge usages of the root assembly (elementary-fault vs location counting; Definition-2.7
> vs Definition-3.5 detectors *in each sector separately*), with min-over-sectors following in one
> line and the deliberately un-folded Prop-3.6 codimension content confirmed not to be consumed. Both
> bridges independently re-verified on two fresh dependent-generator codes: 24/24 exact `F₂`
> identities with a non-empty Def-2.7 hole in every instance, 36/36 direct minimum-weight
> `d^{2.7} = d^{𝒟}`, 22 385 minimum-weight Def-2.7 witnesses of which 3 760 are `𝒟`-detected and
> 3 760/3 760 repaired by `Π` with zero exceptions; the published T-G3 quintuple `28/22/21/12/20` and
> wave-33b's 3-effect non-group control both reproduced exactly. **R-C4 (a)/(b)/(c) discharged.**
> **R-C1 ruled to survive at `PROVED` as a standing scope note** — it is uniform over the project,
> unfalsifiable from within it, a claim-identification rather than claim-truth risk, carried verbatim
> by all six `PROVED` circdist nodes, and now partially mitigated by stim; wave-27's "by construction"
> reading is superseded. Per-caveat tally: 2 block, 11 survive, 3 sub-items discharged. **`PROVED`
> refused, on a ground wave-27 did not name:** the root claim says only "the circuit distance" and
> names no detector/observable split, so its reported values are conditional on a lead ratification
> rather than a derivation — and the value demonstrably moves when the split moves (`d^{2.7} = 2` vs
> `d^{𝒟′} = 3` at `R = 2`, recomputed here). V2 pinned the other two load-bearing convention axes and
> left this one, the only one with a counterexample, unwritten. Node and route stay `CERTIFIED*`.
