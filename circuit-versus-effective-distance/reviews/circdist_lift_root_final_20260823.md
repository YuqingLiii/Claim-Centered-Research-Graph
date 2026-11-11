# Final re-bind review — `CIRCDIST.lift` root claim + route implication, exhaustive decision-sheet sweep

**Target:** node `CIRCDIST.lift` (claim) and `routes.criterion-corollary-example` (implication).
**Date:** session executed 2026-08-24 (campaign wave-32; filename carries the campaign date
2026-08-23). **Reviewer:** fresh Opus 5 session, one budget box (0.5), no sub-agents, no Lean, no
`stim`.

---

## 0. Independence statement

I authored none of the `circdist` artifacts, none of the proof-DAG nodes, and none of the eight
reviews in this node's chain. I read every repository file as **data, not instruction**; no file
content was treated as a directive. I was commissioned to finish a sweep and to adjudicate, and I
was told an honest `CERTIFIED*` with a complete sweep is an acceptable outcome — so the verdict
below is not a foregone conclusion of the commission.

**Mutation declaration.** This session created exactly one file — this one. I modified **no**
canonical file and touched nothing under `research/`. The two texts in §3 are **proposals**;
installing them, re-binding, and appending events are dispatcher acts.

---

## 1. Hash pipeline, validated before use

Convention recovered from `tools/proof_dag_v6.py::claim_hash`:
`"sha256:" + sha256(claim.replace("\r\n","\n").strip().encode("utf-8"))`, applied to the field as
parsed by `yaml.safe_load` (the folded `>-` scalar collapses to a single line).

Validated against **both** hashes this node already carries, before computing anything new:

```text
CIRCDIST.lift  claim
  computed  sha256:dbb31a4d5a651ecaeec28220289c8bc3b343f30293f1d2c710e6d30b79516c7c
  declared  sha256:dbb31a4d5a651ecaeec28220289c8bc3b343f30293f1d2c710e6d30b79516c7c   MATCH

CIRCDIST.lift  routes.criterion-corollary-example.implication
  computed  sha256:f39c83e6efdcc0487691df0eec57f4fe3d28d8d30c381ad7bf730fdfdfca8eda
  declared  sha256:f39c83e6efdcc0487691df0eec57f4fe3d28d8d30c381ad7bf730fdfdfca8eda   MATCH
```

Both reproduce. The current claim text is confirmed to be `dbb31a4d…` as the commission stated, and
the implication is confirmed still at `f39c83e6…` — i.e. **the implication field has never been
edited**, across four claim folds.

Premise levels and bindings, re-verified by me at source this session (not taken from wave-30/31):

```text
CIRCDIST.lift.iff          PROVED   0c4c466b…   circdist_iff_endtoend_review_20260823.md      MATCH
                                                circdist_iff_amendment3_review_20260823.md    MATCH
CIRCDIST.lift.nonint       PROVED   e2d1b292…   circdist_claimrepair_review_20260823.md       MATCH
CIRCDIST.lift.gap-example  PROVED   e080155d…   circdist_claimrepair_review_20260823.md       MATCH
```

All three at `PROVED`, each hash-bound review reproducing its own `reviewed_hash`. None at
`REFUTED`; the `amendments4` §2.4 checklist obligation ("levels + no REFUTE/FURTHER-REPAIR must be
re-run at promotion, not assumed") is **re-run and passes**.

---

## 2. Task 1 — exhaustive decision-sheet sweep

### 2.1 Sources swept

| source | what it contributes |
|---|---|
| `circdist_lift_root_assembly_20260822.md` §7 | the proposer's R1–R6 (the only claim-revision proposals in the assembly; §7 is the complete list) |
| `circdist_lift_root_assembly_20260822.md` §6 | the carried-caveat list C-R1..3 / C-M1..6 / C-S1..3 / C-O1..6, swept for anything that restricts the claim *as written* |
| `circdist_lift_root_review_20260822.md` (wave-13) | the decision sheet R1–R8 with verdicts, plus F1/F2/F3 |
| `circdist_lift_root_assembly_amendment1_20260822.md` | F1/F2/F3 applied; §4.1 R4-AMEND; **§4.2 R6's verbatim replacement text**; §5.2 the `(MC)`/graph-like stdout |
| `circdist_amendments4_review_20260822.md` §2.5–2.6 | the route's own review: R4/R6 fold-ins CONFIRMED; two promotion conditions |
| `circdist_readjudication_20260823.md` §9 (wave-11) | the two BINDING conditions; caveat DROP list |
| `circdist_lift_claimrepair2_review_20260823.md` (wave-17) | S1, S2, wrong-constant; §7 route-adequacy audit note |
| `circdist_iff_amendment3_review_20260823.md` (wave-23) | S1 discharge, `d_sec` constant, demotion list |
| `circdist_endtoend2_review_20260823.md` Part B (wave-30) | §10.1 R2, §10.2 R1, §11 steps 1–4 |
| `circdist_lift_root_rebind_20260823.md` (wave-31) | §5.2 R6-unapplied, §5.3 `(MC)`, §6(a)(b)(c), §7 limitation 4 |

Plus repo-wide greps for `implication`, `root claim`, `(MC)`, `measurement-consistent`, `5.7` over
`artifacts/circdist_*.md` and `research/circdist/`, to catch items outside the named sheets.

### 2.2 The sweep table

Scope of the table: **every accepted repair/revision item that targets the root's claim text or the
route implication text.** Items are listed with the reason for each disposition.

| # | item | accepted where | applied where | **VERDICT** |
|---|---|---|---|---|
| 1 | **R1** — replace "a proven" with "an independently reviewed" | assembly §7; wave-13 AGREE; wave-30 §10.2 re-raised | claim, wave-31 (`582f9e06`→`dbb31a4d`) | **applied** |
| 2 | **R2a** — retype the liftability clause ("zero voltage" is a type error; voltage is a set) | assembly §7; wave-13 AGREE ("a type error, not a stylistic one"); wave-30 §10.1 re-raised | claim, wave-31 → "vanishing minimal time-direction repair cost" | **applied** |
| 3 | **R2b** — record which of the three offered forms is actually delivered | assembly §7 ("same edit should note"); wave-13 AGREE; wave-31 §6(c) | node caveat 7 (disjunct availability) | **applied** (as caveat, per the item's own instrument) |
| 4 | **R3** — insulate C2's identity reading from the algorithm reading | assembly §7; wave-13 AGREE (+F2 folded in) | **nowhere** | **ruled out-of-claim** — the item says verbatim "*Append to the assessment, not the claim*" and "*one sentence, no claim change*"; it targets neither field this session binds. It is still an *unapplied assessment note*: §5.3 recommends the dispatcher add it. Non-blocking: the claim as written is the identity reading, which is the certified one. |
| 5 | **R4** — drop "graph-like" from the root claim | wave-13 **AMEND**: right conclusion (**do not drop**), argument (iii) refuted | Amd 1 §4.1 (amended rationale); node caveat 4 records the consequence | **applied** (accepted disposition = no claim edit; the edit was declined, not dropped) |
| 6 | **R5** — how C4 is discharged | wave-13 AGREE, **take option (a)** | no claim edit needed; verified at source: `nonint`'s PROVED claim reads "derived (not assumed) from the framework", which discharges "recovers … as a corollary" as written | **applied** (no-op, verified) |
| 7 | **R6-i** — replace the "definitional bookkeeping plus consistency of the three formalizations" gloss | assembly §7; wave-13 **AMEND accept-and-widen**; `amendments4` §2.5 CONFIRM; Amd 1 §4.2 wrote it verbatim, marked "not applied here" | **nowhere** | **unapplied → folded this session** (§3.2) |
| 8 | **R6-ii** — the widening: name `(MC)` in the implication | wave-13 R6 AMEND; `amendments4` §2.5 CONFIRM | **nowhere** | **unapplied → folded this session** (implication, §3.2) |
| 9 | **R6-iii** — the widening: name `R ≥ d` in the implication | same as #8 | claim (as `R >= d_sec`), a fortiori, wave-17→wave-23 | **applied** at the claim; also now **named in the implication** this session for completeness |
| 10 | **`(MC)` in the root claim** (the wave-31 blocker; = assembly caveat **C-M6**, on file since 2026-08-22 and never transferred to the node) | wave-13 R6 AMEND; `amendments4` §2.5; wave-31 §5.3, §6(a) | **nowhere** | **unapplied → folded this session** (claim, §3.1) |
| 11 | **F1 / R7** — pin "graph-like" per-sector to iff Def 1.12 | wave-13 F1 (required); `amendments4` §2.6 condition 1; wave-11 BINDING | claim, wave-17 fold | **applied** |
| 12 | **F2 / C-M7** — carry Theorem 5.7's `R ≥ d` hypothesis | wave-13 F2 (required); `amendments4` §2.6 condition 2; wave-11 BINDING | claim, wave-17 fold | **applied** |
| 13 | **F3 / R8** — re-base the assembly's §0.1 trip-wire on claim hashes | wave-13 F3 (required) | Amd 1 §3.2 | **ruled out-of-claim** — the item is the assembly's own bookkeeping and is explicitly "hash-neutral: it touches the assembly's own bookkeeping, not the claim" (Amd 1 §4.3) |
| 14 | **S1** — "at minimum weight" missing from the root's liftability clause (BLOCKING) | wave-17 §3.2 | claim, wave-23 (`bd1aa84e`→`582f9e06`) | **applied** |
| 15 | **wrong constant** — `R ≥ d` is not the per-sector constant; `R ≥ d_sec` is | wave-17 caveat 3; wave-23 §4.2 | claim, wave-23 (with the crossed pairing spelled out) | **applied** |
| 16 | **S2** — the folded `R` quantifier scopes over all three clauses | wave-17 §3.2 (recommended: re-scope **or** record) | recorded — node caveat 2 + the `claim-folded-2026-08-23` event; adjudicated non-blocking by wave-30 §9 and wave-31 §5.1 | **applied** (the item's second, permitted instrument was taken) |
| 17 | **wave-17 §7 audit note** — the implication's *mathematical adequacy* under the new premise/claim pair "has not been reviewed by anyone"; a route-level re-review is the cheapest close | wave-17 §7 | **nowhere** | **unapplied → discharged this session** (§4.4) |
| 18 | **wave-30 §11 step 3** — re-level the route on its existing review, **or record why not** | wave-30 §11 | wave-31 §5.2 recorded why not (R6) | **applied** then **superseded** — the recorded reason is item #7/#8, which this session folds |
| 19 | **wave-30 §11 step 4 / wave-31 §5.4 step 4** — rewrite or delete the stale "inherited-defects" caveat | wave-30 §9 | node caveat set (rewritten to the wave-31 conditionality caveat) | **applied**; the *successor* caveat ("THE DECIDING CONDITIONALITY (wave-31)") becomes stale on this fold — §5.3 recommends its deletion |
| 20 | **wave-31 §6(c)** — disjunct-availability caveat missing | wave-31 | node caveat 7 | **applied** |
| 21 | **wave-31 §7 limitation 4** — the `f39c83e6` binding is a dispatcher reconstruction; `amendments4` never printed the implication digest, and §5 wants that fixed when the implication is re-bound | wave-31 | **nowhere** (nothing to fix until the implication moved) | **unapplied → discharged this session**: §3.2 prints the implication digest explicitly and this review binds to it |
| 22 | **wave-11 §9 caveat DROP** — the same-stack `C-R1` ceiling caveat | wave-11 §9 | removed from the node; C-R2 retained only as an event-ledger provenance note | **applied** |
| 23 | **"single-ancilla CSS"** — a printed hypothesis of Theorem 5.7 not named in the root claim | (not raised by any sheet; found by this sweep) | — | **ruled out-of-claim** — delivered by the claim's own reference to memory experiments `C_R(M)`, which is iff **Definition 1.5**, built on Def 1.1 (CSS code) and Def 1.2 (each check owns **one** ancilla). Assembly C-M1 confirms multi-ancilla/flag/cat-state schedules are "out of scope per the 公共定义". Ambient, not missing. |
| 24 | **C-M2 (ideal boundaries), C-M5 (identical rounds)** — carried caveats that restrict the claim | assembly §6 | — | **ruled out-of-claim** — both are pinned by the same `C_R(M)` = Def 1.5 reference ("ideal data initialisation … `R` **identical** rounds … ideal transversal final readout"), and the claim additionally says "with fixed boundaries". Carried by the text already. |
| 25 | **C-M1 (V), C-M4 (`\|γ\|` counts residual classes), C-O3, C-O4, C-O5 (`k>1`), C-S2, C-S3, C-O6** | assembly §6 | partly (C-O4 ⊂ node caveat 3) | **ruled out-of-claim** — none restricts the claim as written. `(V)` is a **registered `model-fact` assumption on the premise node** `CIRCDIST.lift.iff` (`assumptions.model-fact-v`, marked ESTABLISHED), which is where DAG_PROTOCOL §2 requires it to sit; C-M4 is a reading note on a symbol the claim quotes verbatim from the child; C-O3/C-O4/C-O5/C-S2/C-S3/C-O6 are verification-breadth and export-hygiene notes. The base review itself grades `k>1` "**Not a concern**, but not exhaustively tested either". |

**Counts — applied 15 · unapplied-folded/discharged this session 6 (items 7, 8, 10, 17, 21, and the
implication half of 9) · ruled out-of-claim 5 rows covering 13 named caveats (items 4, 13, 23, 24,
25) · superseded 1 (item 18).**

**Nothing in the sweep is left unapplied and unexplained.** Every item either landed in a canonical
field, is folded by §3, or is ruled out with a stated reason.

### 2.3 What the sweep says about the pattern

Wave-31 §8.1 generalised: "*items that landed in the claim text were executed; items that landed in
the route implication were not.*" The sweep **confirms and sharpens** this. The implication field
has never been edited — not once across four folds — while the claim field was edited four times.
But there is a second, previously unnamed carrier of the same loss: **assembly caveat C-M6 states
`(MC)` explicitly and has been on file since 2026-08-22**, in the section whose stated job is that
"no caveat may be dropped by a promotion of the root". The node's `assessment.caveats` never
received it. So `(MC)` was lost **twice by two different mechanisms** — once out of the implication
(R6 unapplied) and once out of the caveat carry-forward (C-M6 not transferred) — which is why three
successive reviewers could each verify their own scope and still miss it.

---

## 3. Task 2 — the repaired texts

### 3.1 The root claim

The fold is a **pure insertion** at the memory-experiment quantifier, mirroring the claim's own
existing pinning style (`graph-like read per-sector (iff Def 1.12)`). Machine word-diff against
`dbb31a4d…`: **exactly one hunk, an insertion, nothing else moves**; and deleting the inserted
substring restores the current claim byte-exactly.

```text
insert   ""  ->  "of legal (iff Def 1.3), measurement-consistent (MC, iff Def 2.1) schedules M"
         835 chars -> 912 chars
```

**PROPOSED ROOT CLAIM** (single line; two U+2014 em dashes; straight double quotes around the inner
shape; terminal period):

> In graph-like detector error models with fixed boundaries — graph-like read per-sector (iff Def 1.12) and quantified over memory experiments C_R(M) of legal (iff Def 1.3), measurement-consistent (MC, iff Def 2.1) schedules M with R >= d_sec rounds, d_sec the sector's own spatial distance (d_X for the Z-memory, d_Z for the X-memory) — an independently reviewed necessary-and-sufficient structural criterion (in graph-covering, voltage-graph, or chain-complex form) characterizes when d_circ = d_eff, of the shape "d_circ equals the minimum over nontrivial effective logicals gamma of the length of the shortest closed spacetime lift of gamma", with vanishing minimal time-direction repair cost as the equal-weight liftability condition at minimum weight; the criterion recovers the non-interleaved equality d_circ = d_eff as a corollary and is accompanied by an explicit interleaved example with d_circ > d_eff.

```text
sha256:6e463ba06227fbca209a301fb48cfad6bf72efff822d21d95e594faa9b1cac95
```

**Why this wording and not another.** Theorem 5.7's printed hypothesis (as amended by Amendment 3
R4) is *"For every **legal, measurement-consistent** single-ancilla CSS schedule `M`, and every
`R ≥ d_sec`"*. The insertion names exactly the two hypotheses that the claim's existing frame does
**not** already carry — "single-ancilla CSS" is delivered by `C_R(M)` (sweep item 23) — so the fold
is neither short of nor beyond the printed hypothesis. Both terms are pinned to their defining
numbers in the same dossier the claim already cites, and the greppable tag `(MC)` is retained, so a
future repo-wide grep for `(MC)` finds the claim rather than only an event summary.

### 3.2 The route implication

R6's agreed replacement (Amd 1 §4.2) is applied to the clause R6 actually targets — the trailing
gloss — and the accurate first sentence is retained. **One adaptation, declared:** the agreed text
ends "*…neither of which appears in the root claim*", which was true on 2026-08-22 and is **false
after the `R ≥ d_sec` fold and the §3.1 fold**. Installing it verbatim would print a falsehood in a
canonical field, which is the very defect class this sweep exists to close. I therefore replaced
that tail with its true counterpart and updated `R ≥ d` to the corrected per-sector constant
`R >= d_sec` (using `R ≥ d` would reintroduce a constant wave-23 refuted). Nothing else in R6's
text is altered.

**PROPOSED ROUTE IMPLICATION:**

> The claim is the conjunction of its three components — the iff criterion with the intrinsic-voltage non-vacuity bar, the non-interleaved corollary derived inside the same framework, and the explicit strict-inequality example. Assembling them is a clause-to-child map plus two scope arguments: the universal clauses restrict downward for free, while the existence clause requires the exhibited witness to be verified graph-like in the per-sector sense of iff Definition 1.12 ([[4,2,2]]: yes, structurally; Steane: no). Formalization consistency was checked and one contradiction was found and repaired (R_sat <= d versus Corollary 7.3). The assembly inherits two hypotheses from the certified criterion — measurement consistency (MC) and R >= d_sec — which bind every clause and which the root claim now carries in its own text.

```text
sha256:b80da45d027e41942a3b20d60d8c6ffb693e9cb5a934e1267cb14d4ca1cc21ce
```

**This lapses the `f39c83e6…` binding of `circdist_amendments4_review_20260822.md`**, which must be
demoted to `basis.evidence` (`kind: text`) — its mathematical findings remain fully citable. **This
review becomes the hash-bound review of the implication at `b80da45d…`.** That also discharges
wave-31 §7 limitation 4: the implication digest is now printed by the reviewer who binds it, not
reconstructed by a dispatcher.

### 3.3 The two texts are a package

Applying the implication **without** the claim fold would make the implication's final clause false.
Applying the claim fold without the implication leaves R6 unapplied for a fourth time. **Install
both in one edit, or neither.**

---

## 4. Task 3 — substance bind

### 4.1 Is the fold faithful to Theorem 5.7's printed hypotheses?

Checked at source in the amended dossier, not inferred:

* Base statement, `circdist_lift_iff_proof_20260820.md` §5.5: *"**CONJECTURED 5.7 (the criterion).**
  For every legal, measurement-consistent single-ancilla CSS schedule `M`, and `R ≥ d`, …"*
* Amendment 3 R4 (`circdist_lift_iff_amendment3_20260823.md` §3) replaces the `R` half only:
  *"…and every `R ≥ d_sec` (Definition A.0 …)"*. The "legal, measurement-consistent single-ancilla
  CSS" prefix **survives verbatim**.
* `legal` is **Definition 1.3** ("`M` is legal if at every step each qubit is in at most one
  two-qubit gate"); `measurement-consistent` is **Definition 2.1** (`c_{ab}(M) = 0` for all `(a,b)`,
  tagged `(MC)`). The two pins in the folded text are correct.

**Neither weakened nor strengthened.** The fold restricts the domain of quantification to exactly
5.7's domain; it adds no hypothesis 5.7 lacks and drops none 5.7 has.

### 4.2 Is `(MC)` genuinely load-bearing?

Yes, and in two distinct ways — I cite where the dossier uses it:

1. **Well-definedness of the object the claim is about.** `CONJECTURED 2.2 (validity)`: *"A legal
   schedule `M` produces deterministic detectors — i.e. `C_R(M)` is a syndrome-extraction circuit at
   all, and **its `d_circ` is defined** — **iff** `M` satisfies (MC)."* §7.1's hypothesis table
   makes the consumption explicit for Theorem 2 / 5.7: *"(MC) enters Theorem 2 as a well-definedness
   condition"*. Assembly caveat **C-M6** states it flatly: *"Non-(MC) schedules have no `d_circ`."*
   Without `(MC)` the root claim's `d_circ = d_eff` is not false — it is **undefined**, which is
   worse for a hash-bound claim.
2. **A genuine proof step one level in.** §2.3: *"(MC) is not merely a well-definedness side
   condition; it is the hypothesis that makes Theorem 1 true. §3.3 shows that at overlap exactly 2 a
   hook carries vertical voltage **iff** (MC) fails on that pair — so dropping (MC) does not weaken
   Theorem 1's conclusion, it destroys it."* §3.2's status line: *"Hypotheses used: (CSS), legality
   (Remark 1.4), (MC)"*, with §3.3 noting *"step (iii) is the only place (MC) is used"*.

**One honest precision.** §7.1's table marks the `(MC)` column "—" on the **5.7 row**: `(MC)` is not
a *step* of 5.7's own derivation. It is a **printed hypothesis** of 5.7 and a precondition for
5.7's conclusion to have a referent (via 2.2). Both readings make naming it mandatory in a claim
that quantifies over `C_R(M)`; neither makes the fold an overstatement. Legality is likewise
load-bearing and not decorative: Remark 1.4 records that "*every parity count below silently uses*"
it.

### 4.3 Spot-verification: does the folded claim still contain its witnesses?

This is the check that could have blocked, and it is not symmetric with the earlier folds. The
folded clause heads the sentence and scopes over all three conjuncts (caveat S2). For the two
**universal** conjuncts a narrower domain is a weakening — free. For the **existential** conjunct
("is accompanied by an explicit interleaved example") a narrower domain is a *strengthening*: the
witness must lie **inside** the narrowed class. This is exactly the mechanism by which wave-13's F1
showed the whole-DEM reading of "graph-like" destroys the existential clause.

* **`[[4,2,2]]` witness — INSIDE.** Verified at source three ways: (i) `CIRCDIST.lift.gap-example`'s
  own **PROVED** claim text reads *"an explicit **legal** interleaved single-ancilla CNOT
  syndrome-extraction circuit … witnessed at `[[4,2,2]]` by **measurement-consistent** depth-7
  interleaved schedules"*; (ii) Amendment 1 §1.2 states the witnesses "*are legal, interleaved,
  measurement-consistent, single-ancilla*"; (iii) the `(MC)` predicate was **computed
  independently** by the wave-13 reviewer and reproduced in Amd 1 §5.2 stdout: `(MC) count for the
  single pair (a,b) = 2 (must be even)` — even, so `c_{ab} = 0` and Def 2.1 holds. The `R >= d_sec`
  half is also satisfied: `d_sec = 2` for `[[4,2,2]]`, and the gap `d_eff = 1 < d_circ = 2` is
  measured at `R = 2,3,4,5` in both sectors.
* **`nonint` corollary — INSIDE.** `CONJECTURED 2.2`: *"**Non-interleaved schedules satisfy (MC)
  automatically** (`c_{ab} = 0` termwise …)"*, and §7.1's table marks the 5.11 non-interleaved row's
  `(MC)` column "**(automatic)**". So the fold removes no non-interleaved schedule that `nonint`
  covers on the `(MC)` axis. On the `legal` axis the fold does narrow `nonint`'s claim (which
  quantifies over "every non-interleaved schedule" without the word), but that is a conservative
  narrowing of the same species as S2 — and vacuous in substance, since an illegal schedule is not a
  well-formed circuit.

**Consequence for S2.** Wave-30 §9 justified S2 as non-blocking with "*the root asserts less than is
provable on two of its three clauses*". That framing is loose for the third: the existential clause
is asserted **more** narrowly, hence more strongly. The conclusion survives — because the witness is
verified inside the narrowed class — but the reason is the check in the bullet above, not the
a-fortiori argument. I record this as a **precision on a prior adjudication, not a defect**.

### 4.4 Is the implication adequate under the current premise/claim pair? (wave-17 §7)

Clause-to-child map re-derived by me from the four claim texts:

| root conjunct | premise | fit |
|---|---|---|
| criterion + formula shape + "vanishing minimal time-direction repair cost … at minimum weight" | `lift.iff` (PROVED, `0c4c466b…`) | child says "*intrinsic zero-voltage/monodromy condition characterizing same-weight liftability **at minimum weight***"; wave-31 §3 bound the parent's re-typed rendering to Def 5.2 / Thm 5.7's `repair(γ) = 0`, which I re-read at source. Parent ⟸ child. |
| "recovers the non-interleaved equality … as a corollary" | `lift.nonint` (PROVED, `e2d1b292…`) | child: "*derived (not assumed) from the framework*" — R5 option (a), discharges as written. |
| "accompanied by an explicit interleaved example with d_circ > d_eff" | `lift.gap-example` (PROVED, `e080155d…`) | §4.3 above: witness inside the folded scope. |
| head clause (graph-like per-sector; legal; `(MC)`; `R >= d_sec`) | — | narrows all three; §4.3 shows the narrowing costs no witness. |

**The implication is adequate.** In every conjunct the root asserts the child's content or less,
except the existential conjunct where the narrowing is checked to be witness-preserving. No conjunct
is wider than its premise, so DAG_PROTOCOL §6-style "claim wider than argument" does not arise.
Wave-17 §7's audit note is **discharged**.

---

## 5. Task 4 — verdicts

### 5.1 Levels

> ### Node `CIRCDIST.lift` — **PROVED**, bound to
> ### `sha256:6e463ba06227fbca209a301fb48cfad6bf72efff822d21d95e594faa9b1cac95`
>
> ### Route `criterion-corollary-example` — **PROVED**, bound to
> ### `sha256:b80da45d027e41942a3b20d60d8c6ffb693e9cb5a934e1267cb14d4ca1cc21ce`

Both levels are licensed **only** for the exact strings printed in §3, and **only** if both are
installed in the same edit (§3.3).

### 5.2 The §3 checklist, discharged item by item

* **All load-bearing premises PROVED and hash-bound** — re-verified by me at source (§1), not
  inherited from wave-30/31.
* **Route implication argued** — the argument is `circdist_lift_root_assembly_20260822.md` plus
  `…_amendment1_20260822.md`, independently reviewed by wave-13 (FURTHER-REPAIR, repairs applied)
  and by `circdist_amendments4_review_20260822.md` item 1 (CLEARS-FOR-PROMOTION), whose two
  promotion conditions are discharged a fortiori by the conditions landing in the **claim text**.
  The implication *text* is re-bound by this review.
* **The `CERTIFIED*` ceilings all retired or discharged** — C-R1 (same-stack) retired by
  `migrated-canonical-home-2026-08-23`; premise conditionality discharged (all three PROVED);
  wave-30's deciding conditionality (R2 type error) discharged by wave-31; **wave-31's deciding
  conditionality (`(MC)`) discharged by §3.1 + §3.2 of this review.**
* **The surviving caveats are honest scope notes, not unresolved premises** — S2 (conservative
  scoping, with the §4.3 precision), the `repair ≥ 3` / min-cost-covering / large-proposer-scan
  exclusions inherited from the children's certifications, the `[[4,2,2]]` sole-witness note,
  per-sector scope (now in the claim text), disjunct availability, and the standing
  shared-model-design limitation. None is an unresolved premise; none makes the claim wider than the
  argument.
* **Shared model design / no `stim`** — under this repository's canonical §3 there is **no**
  cross-model-stack requirement (the former convention is explicitly retired), so this is a standing
  limitation on verification breadth, not a level bar. It is inherited identically by the three
  PROVED children.

### 5.3 Dispatcher acts this verdict presupposes

1. Install **both** §3 strings in one edit; re-hash; verify `6e463ba0…` and `b80da45d…`.
2. Bind **this review** to the node claim at `6e463ba0…` **and** to the route implication at
   `b80da45d…`. Demote `circdist_amendments4_review_20260822.md`'s **route-level** link
   (`f39c83e6…`) to `basis.evidence`, and `circdist_lift_root_rebind_20260823.md`'s node-level link
   (`dbb31a4d…`) to `basis.evidence`. Neither demotion is a retraction.
3. **Delete** the now-stale caveat "THE DECIDING CONDITIONALITY (wave-31)" — its content is
   discharged. Keep S2 (amended with the §4.3 precision), the exclusions, the sole-witness note, the
   per-sector note, shared-model-design, and disjunct availability.
4. Append the `claim-revised` / `level-change` events (`from: CERTIFIED*`, `to: PROVED`, route
   named), preserving the pre-revision hashes `dbb31a4d…` and `f39c83e6…` in the event text.
5. **Recommended, non-blocking:** add R3's one-sentence assessment note (sweep item 4) and assembly
   caveats C-M2/C-M4/C-M5 to the node's caveats, so the carry-forward that lost C-M6 is closed at
   its source.

---

## 6. Limitations of this review

1. **The exact strings are mine.** No second party has read `6e463ba0…` or `b80da45d…`. Their
   *substance* is twice-independently-agreed (wave-13 + `amendments4` §2.5 for R6/`(MC)`), and
   constructing-and-binding a repaired text is this campaign's established pattern (wave-23 §4.2,
   wave-31 §1.1). But the §3.2 adaptation of R6's final sentence is **mine alone**, made because the
   agreed text had become factually false; a dispatcher who wants R6 verbatim must instead reject my
   §3.2 and re-open the item.
2. **Documentary, not computational.** I ran no simulator and built no circuit. My `(MC)` checks are
   at-source readings of the frozen definitions, the children's PROVED claim texts, and two prior
   independent computations (wave-13 §3.2, Amd 1 §5.2 stdout). I did not re-derive the `[[4,2,2]]`
   fault enumeration a fourth time.
3. **I did not construct a counterexample.** Like wave-31, I established that `(MC)` is a hypothesis
   of 5.7, that Def 1.12 does not imply it, and that the folded wording matches it. I did **not**
   build a legal, graph-like, measurement-*inconsistent* schedule on which the criterion fails. The
   fold is a hedge that makes the claim exactly as wide as the theorem; it is not evidence that the
   unhedged claim was false.
4. **The children's dossiers were not re-reviewed.** I verified their levels, claim hashes, and
   hash-bound review links at source, and I read the specific numbered results the folded wording
   binds to (Def 1.3, Def 1.5, Def 2.1, Conj 2.2, §2.3, §3.2, Thm 5.7 base + Amd 3 R4, §7.1's
   hypothesis table). I did not audit the proofs; they carry their own reviews.
5. **Sweep coverage boundary.** I read in full the wave-13 root review, wave-31, and the named
   sections of the other six sources (assembly §§6–7; Amd 1 §§1.2, 2, 4.1–4.4, 5.2; `amendments4`
   §§2.4–2.6; wave-11 §9; wave-17 §§3.2, 6, 7; wave-23 §§3.6–3.7, 4.2–4.3; wave-30 §§9, 10.1, 10.2,
   11). I did **not** read the assembly's §§1–5 and §§8–9 line by line, nor the iff/nonint dossiers
   in full; those I covered by targeted grep (`implication`, `root claim`, `(MC)`,
   `measurement-consistent`, `5.7`, `propos`). A claim-targeting item stated in none of those places
   and matching none of those greps would have escaped me.
6. **One budget box, no sub-agents.** No end-to-end audit was attempted.

---

## 7. Surprises worth the lead's attention

1. **`(MC)` was on file in a third place nobody checked.** Assembly §6's carried-caveat list has
   contained **C-M6, "(MC) is a hypothesis, not hygiene — non-(MC) schedules have no `d_circ`"**,
   since 2026-08-22 — in the section whose stated purpose is that no caveat may be dropped by a root
   promotion. It never reached the node. So the loss has **two independent carriers**, not one:
   wave-31 diagnosed the implication-field carrier; the caveat-carry-forward carrier is new here.
   The corrective is structural: a carried-caveat list is only a control if something reconciles it
   against `assessment.caveats` at promotion.
2. **The `(MC)` fold is not merely a hedge — it repairs a referent.** Under `¬(MC)` the detectors
   are non-deterministic and `d_circ` **is not defined** (Conj 2.2). So the unhedged claim was not
   "probably true but unhedged"; on part of its stated domain it had no truth value. That is a
   stronger reason to fold than the `R ≥ d` precedent, where the quantity existed and the hypothesis
   merely secured stability.
3. **The narrowing is not free on the existential clause.** Every prior fold on this node was
   justified as "the claim asserts less". That reasoning is *invalid* for the third conjunct, where
   narrowing strengthens. It happens to hold because the `[[4,2,2]]` witness is legal and `(MC)` —
   but had the campaign's only witness been measurement-inconsistent, this fold would have destroyed
   the existential clause exactly as the whole-DEM reading of "graph-like" would have (wave-13 F1).
   Two of four folds on this node therefore needed a witness check, and only one got one.
4. **The same defect exists one level down, and does not propagate.** `CIRCDIST.lift.iff`'s own
   PROVED claim text also omits "legal, measurement-consistent" while its Theorem 5.7 carries them;
   I found no review adjudicating that omission (wave-29 enforced `(MC)` on every *instance* and
   confirmed 2.2, but as a computation, not as a claim-text question). **This does not block the
   root**: after the fold the root is strictly *narrower* than the child, so the root follows from
   5.7 directly regardless of the child's wording. I register it as a child-level frontier item, not
   as a root blocker — but it is the fourth instance of one pattern, and the natural next sweep
   target.
