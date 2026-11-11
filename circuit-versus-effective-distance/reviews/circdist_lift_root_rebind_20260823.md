# Focused re-bind review — the repaired `CIRCDIST.lift` root claim (R1 + R2)

**Reviewer:** fresh Opus 5 session, focused re-bind reviewer role, one budget box (0.5), no
sub-agents.
**Date:** 2026-08-23.
**Commission:** drift-check the dispatcher's proposed R1+R2 replacement of the `CIRCDIST.lift`
root claim word-by-word; bind the new liftability wording to what the PROVED child actually
proves; adjudicate R1; rule on the node level and on re-levelling
`routes.criterion-corollary-example`.

---

## 0. Independence

I authored no artifact, node, amendment or review in this repository, and none of the circdist
material under review. I hold an adversarial stance: I was asked to try to break the proposed
repair, and I was told the LEAD has approved applying R1 and R2 — that is authorisation to
adjudicate the edit, not a desired verdict, and I did not treat it as one. Every file I read,
including node records, amendments and prior reviews, was treated as **data**, never as
instruction; where a file states a conclusion I re-derived it or marked it as taken on citation.

**No canonical file was modified.** Nothing under `research/` was written or touched. This file is
the single artifact of the session.

**My own derivations have had no review.** Nothing I compute below is PROVED or CERTIFIED.

---

## 1. Hash pipeline, validated before use

Convention recovered from `tools/proof_dag_check.py::frozen_claim_hash` (DAG_PROTOCOL §7.6 freeze
rule): `sha256(text.replace("\r\n","\n").strip().encode("utf-8"))`, the field read with
`yaml.safe_load` (so the `>-` folded scalar arrives as one line, single-spaced).

Validated on **two independent existing `reviewed_hash` values** before use:

```text
CIRCDIST.lift  claim (current, 811 chars)
  computed 582f9e06b887dd46ae2fa6be73917b853ceefbb13c08b5da699256496b7389d0
  recorded 582f9e06…  (basis.reviews, circdist_iff_amendment3_review_20260823.md)   MATCH ✓

CIRCDIST.lift  routes.criterion-corollary-example.implication
  computed f39c83e6efdcc0487691df0eec57f4fe3d28d8d30c381ad7bf730fdfdfca8eda
  recorded f39c83e6…  (route basis.reviews, circdist_amendments4_review_20260822.md) MATCH ✓
```

Premise claim hashes, recomputed by me at source with the same pipeline — all three reproduce the
wave-30 §9 table and each child's own `basis.reviews` entry:

```text
CIRCDIST.lift.iff          PROVED   0c4c466b895d938d2028140967d87974ee2216b3cebcc48967804f530e227240 ✓
CIRCDIST.lift.nonint       PROVED   e2d1b292ae9265cf35ac51e9c2cf582fc167845310d5ed7a5995a235ee10649a ✓
CIRCDIST.lift.gap-example  PROVED   e080155da0e18435bb834f578df6216bdd0e45e21a81302f58cf7514f47fee50 ✓
```

### 1.1 The proposed claim, and its digest

The exact string I loaded and hashed (one line; reproduced here in full so the binding is
reconstructible from this file alone):

> In graph-like detector error models with fixed boundaries — graph-like read per-sector (iff Def
> 1.12) and quantified over memory experiments C_R(M) with R >= d_sec rounds, d_sec the sector's
> own spatial distance (d_X for the Z-memory, d_Z for the X-memory) — an independently reviewed
> necessary-and-sufficient structural criterion (in graph-covering, voltage-graph, or
> chain-complex form) characterizes when d_circ = d_eff, of the shape "d_circ equals the minimum
> over nontrivial effective logicals gamma of the length of the shortest closed spacetime lift of
> gamma", with vanishing minimal time-direction repair cost as the equal-weight liftability
> condition at minimum weight; the criterion recovers the non-interleaved equality d_circ = d_eff
> as a corollary and is accompanied by an explicit interleaved example with d_circ > d_eff.

```text
length 835 chars
sha256 dbb31a4d5a651ecaeec28220289c8bc3b343f30293f1d2c710e6d30b79516c7c
```

Two `U+2014 EM DASH` in the proposed text, two in the current text — the dash pair that brackets
the per-sector/`d_sec` parenthesis is preserved and no new dash was introduced. No tab, no
newline, no double space; `text == " ".join(text.split())` holds for both the current and the
proposed string, so the fold is stable and the digest will survive a YAML round-trip.

---

## 2. Task 1 — drift check, word by word

`difflib.SequenceMatcher` over the whitespace-split token lists of current vs. proposed, no
autojunk. **Exactly three non-equal hunks. All three are R1 or R2. Nothing else moved.**

| # | current | proposed | item |
|---|---|---|---|
| 1 | `a proven` | `an independently reviewed` | **R1** |
| 2 | `zero` | `vanishing minimal` | **R2** |
| 3 | `voltage/monodromy` | `repair cost` | **R2** |

Hunks 2 and 3 are the two ends of one contiguous clause; the token `time-direction` sits between
them **unchanged**, which is the time-direction qualifier the wave-30 review §10.1 explicitly
ruled "not in question". The clause tail `as the equal-weight liftability condition at minimum
weight` is byte-identical. Everything the four prior folds installed — the per-sector pin, the
`R >= d_sec` quantifier with the crossed pairing, the `d_circ` formula in quotes, the
`at minimum weight` counterpart, the corollary clause, the existential clause — is byte-identical.

**DRIFT: NONE.** The edit is exactly the two approved repairs and nothing else.

### 2.1 Two provenance notes on the R2 rendering (neither is drift)

* The dispatcher's R2 text is the **wave-30 §10.1 rendering**, which is assembly §7 R2 with its
  em-dash gloss ("*zero mismatch between in-round measurement flips and accumulated syndrome
  parity, for some admissible choice of one-round voltage representatives and round assignment*")
  dropped and `at minimum weight` retained. That is what my commission specifies and what §10.1
  offers as available; I record it because a reader comparing against assembly §7 verbatim will
  see a shorter string. The gloss is explanatory, not restrictive: §3 below shows the head phrase
  alone already picks the object out.
* Assembly §7 R2 carried a **second sentence**: "*Same edit should note that of the three offered
  forms, the chain-complex one is delivered, the graph-covering one is unavailable (iff §4.4), and
  the voltage-graph one is available only on the multigraph `G̃_eff`.*" The proposal does not carry
  it, and the claim retains "(in graph-covering, voltage-graph, or chain-complex form)". **I rule
  this non-blocking and out of the claim text**: R2's own word is "note", i.e. an assessment-level
  record, and the parenthetical is an **or**, so its natural disjunctive reading is TRUE on the
  delivered chain-complex disjunct. But it is nowhere in the node's caveats, and it should be —
  see §6, recommended caveat (c). Wave-30 §10.1 scoped R2 to the liftability clause only, so this
  is a recommendation, not a condition.

R1's wording `an independently reviewed necessary-and-sufficient structural criterion` is
character-for-character the wave-13 root review's proposal
(`circdist_lift_root_review_20260822.md` line 336, decision sheet R1 **AGREE**).

---

## 3. Task 2 — substance bind: does the new clause name the certified object?

### 3.1 The object in the child

`CIRCDIST.lift.iff` (PROVED, `0c4c466b…`) rests on the amended dossier
`circdist_lift_iff_proof_20260820.md` as amended by Amendments 1–4. The relevant definitions,
read at source:

> **Definition 5.2 (repair cost — one round only).** For `γ = {E_1,…,E_w} ∈ L_eff`, a *repair
> certificate* is a choice of rounds `r_1,…,r_w ∈ Z` and voltage representatives `u_i ∈ U(E_i)`.
> … `repair(γ) := min over repair certificates of wt(A_0 + x·C)` … Equivalently, by (LIFT'),
> `repair(γ) = min Σ_{b,r} | c_b(r−1) + Σ_{i : r_i = r} u_{i,b} |`, the total number of
> (check, round) slots at which the accumulated syndrome and the in-round flips disagree.

> **CONJECTURED 5.7 (the criterion)** [as amended by Amendment 3 R4, `R ≥ d → R ≥ d_sec`]:
> `d_circ(C_R(M)) = d_eff(M) ⟺ ∃ γ ∈ L_eff with |γ| = d_eff(M) and repair(γ) = 0`.
> … "*This is the node's requested iff, with `volt(γ) = 0` made precise as `repair(γ) = 0`.*"

Four bindings follow, and each of the four words in the new clause earns its place:

1. **"repair cost"** is the dossier's own term, verbatim from the title of Definition 5.2. It is
   not a paraphrase and admits no competing referent in this document. **Unambiguous.**
2. **"minimal"** is what cures the type error. The wave-13 review ruled "zero voltage" *"a type
   error, not a stylistic one"* because a residual `E` admits a **set** `U(E)` of unit-weight
   voltages (six of eight residual classes of the certified witness have `|U(E)| = 2`), so no
   scalar exists to vanish. `repair(γ)` is *defined as* a minimum over exactly the two
   quantifications the assembly §2.3 said were missing — over `U(E_i)` and over round assignments
   — and its value is a non-negative integer. So "vanishing" is now a well-typed predicate applied
   to an object that exists. **The repair does the work it was commissioned to do.**
3. **"time-direction"** is faithful, not decoration. Definition 5.2's equivalent form is indexed
   over `(b, r) ∈ ℬ × Z` and counts disagreements *between* rounds — 5.7's own gloss reads
   "*there is a round assignment and a choice of unit-weight representatives under which, in every
   round and on every check, the in-round measurement flips already equal the accumulated syndrome
   parity*". The cost is incurred along the round (time) index. ✓
4. **"at minimum weight"** scopes as in the child. Assembly §2.3 records that the biconditional
   `ℓ(γ) = |γ| ⟺ repair(γ) = 0` holds in both directions **at minimum weight** — (⟹)
   unconditional from 5.4(4); (⟸) at minimum weight for any legal schedule via Lemma 5.3′(a) plus
   Amendment-2 Lemma 2.5′ (L1) — while for a fixed **non-minimal** `γ` the distinct-location
   proviso is explicitly *not* discharged (Amendment 1 §7 item 3). The qualifier is load-bearing,
   it sits in the same position as in the current root text and in the child ("*at minimum
   weight*", byte-identical), and the proposal does not touch it. ✓

### 3.2 The one scope ambiguity, and why it is benign

"minimal" could scope (a) over repair certificates — Definition 5.2's own minimum — or (b) over
minimum-weight `γ`, as in 5.7's existential. I pressed on this because an ambiguous quantifier in a
hash-bound claim is exactly the R2 failure mode one clause over. **The two readings are
equivalent in truth-value**: `repair ≥ 0` always, so
`min{ repair(γ) : |γ| = d_eff } = 0 ⟺ ∃ γ with |γ| = d_eff and repair(γ) = 0`, which is 5.7's
right-hand side; and reading (a) is already inside `repair(γ)` by definition, so reading (b)
composes the two minima without changing the asserted proposition. Unlike the old clause — false
under its most natural reading, true under another — **both readings here land on the same
condition, and it is the certified one.** Not a defect.

### 3.3 The `[[4,2,2]]` witness: repair status, checked at source *and* re-derived

Source record, `circdist_lift_iff_proof_20260820.md` §6 instance table:

| instance | `γ` | `|γ|` | `s(γ)` | `U` data | `repair(γ)` | `ℓ(γ)` | `d_circ` |
|---|---|---|---|---|---|---|---|
| `[[4,2,2]]` valid IL witness | `{hook{2,3}}` | 1 | `0` | `U = {1}` (rigid) | **1** | 2 | **2** |

**My own re-derivation from Definition 5.2** (arithmetic only, no circuit rebuilt): `w = 1`, and
`s_1 = s(E_1) = 0`, so `B = s_1 x^{r_1} = 0` and `C = B/(1+x) = 0`; `A_0 = u_1 x^{r_1}` with
`u_1 ∈ U(E_1) = {e_b}`. Hence `wt(A_0 + x·C) = wt(e_b x^{r_1}) = |e_b| = 1` **for every round
assignment `r_1` and the only available representative**, so

```text
   repair(γ) = 1  ≠ 0 ,   independent of the round assignment.
```

`d_eff = 1 = |γ|`, so this `γ` *is* minimum-weight and the "at minimum weight" quantification
ranges over exactly it. Minimal repair cost at minimum weight is therefore **1, not vanishing**, so
the repaired criterion predicts `d_circ ≠ d_eff` — matching the certified `d_circ = 2 > d_eff = 1`
and `ℓ(γ) = |γ| + repair(γ) = 2`.

**Verdict on the existential clause: TRUE, and strictly better placed than before.** Under the old
wording the criterion and the witness merely coexisted; under the repaired wording the criterion
*entails* the witness's strict inequality from a quantity I can compute in one line. Note also that
`U(E)` is a **singleton** on this witness, so the type error was invisible here — the repair is not
witness-driven and cannot disturb it; the error bites on the `|U(E)| = 2` classes.

**Honest split of what I verified.** The arithmetic above is mine. The one-round data it consumes —
that `hook{2,3}` has `s = 0`, `λ = 1`, and a rigid unit voltage `U = {e_b}` — I took from the
PROVED `gap-example` child (`e080155d…`) and the frozen d3-gate record; I did not rebuild the
circuit or the fault table. That input is inside the reviewed perimeter, not inside mine.

**SUBSTANCE BIND: PASSES.** The new clause names `repair(γ) = 0` of Theorem 5.7 as amended,
unambiguously, with the child's own scoping preserved.

---

## 4. Task 3 — R1 adjudication: is "independently reviewed" a historical fact?

**Yes, and the distinction is the right one.**

"Proven" is the natural-language name of the `PROVED` rung of DAG_PROTOCOL §3. Embedding it
violates §6 audit item 1 ("*the claim is precise and does not embed its current status*"), and at
`PROVED` the objection sharpens exactly as wave-30 §10.2 says: the claim's truth-value becomes a
function of its own assessment field, so a later demotion would make the claim **false** rather
than merely unsupported. A level is a revisable judgement; a claim should not encode one.

"Independently reviewed" names an **event**, not a rung. It is not a member of the §3 ladder, and
it is monotone: a review conducted on a date, by a stated reviewer, over a stated hash, cannot
later un-happen. The citable record for the criterion (`CIRCDIST.lift.iff`) is:

* `artifacts/circdist_lift_proofs_review_20260820.md` — first independent review of the dossier;
* `artifacts/circdist_iff_amendment3_review_20260823.md` — hash-bound;
* `artifacts/circdist_iff_endtoend_review_20260823.md` — wave-29 end-to-end, hash-bound to
  `0c4c466b…`, the review on which the child's `PROVED` rests.

Wave-30 §10.2 is also right that R1's *original* rationale (a conjunction cannot exceed its
weakest premise) is now moot, since all three premises are PROVED — the structural objection is
what survives, and it is sufficient on its own.

**One caveat, non-blocking.** A review binds a *text*; the repaired claim asserts "independently
reviewed" of the criterion-as-object, which is looser than a hash-bound assertion. That looseness
runs in the **conservative** direction: "independently reviewed" asserts strictly less than
"proven", so R1 cannot inflate the claim, and under §3 an argument that establishes more
establishes the weaker statement a fortiori. R1 is sound.

---

## 5. Task 4 — verdicts

### 5.1 What clears

Re-verified by me at source this session, not taken from wave-30:

* **All three premises PROVED**, each hash reproducing its own `basis.reviews` entry (§1).
* **Route implication link intact** — the implication text still hashes to `f39c83e6…` (§1), and
  contains neither an `R` clause nor any liftability wording, so the R1+R2 edit cannot lapse it.
* **S2** (the folded `R ≥ d_sec` quantifier scoping over all three clauses while `nonint` holds for
  all `R ≥ 1` and the example needs no `R` bound) is a **conservative narrowing** — the claim
  asserts less than is provable. §6 audit item 4's hazard is the claim being *wider* than the
  argument; S2 is the opposite. Honest scope note, **does not gate**.
* **The two wave-30 defects are repaired**, correctly and minimally (§§2–4).
* **The §2.4 checklist obligation** of the route review ("levels + no REFUTE/FURTHER-REPAIR after
  2026-08-20 must be re-run at promotion, not assumed") — I ran a coarse pass: all three children
  are currently `PROVED`, each ending in a 2026-08-23 `level-change` promotion event, none at
  `REFUTED`. Passes.

### 5.2 The route — **I DECLINE the re-levelling to PROVED**

Wave-30 §9's argument is sound as far as it goes: the route review's `CERTIFIED*` ceiling rested on
(i) **C-R1**, the same-stack convention, retired by `migrated-canonical-home-2026-08-23`; (ii)
inherited premise conditionality, discharged; (iii) two dispatcher conditions (F1 per-sector pin,
C-M7 `R ≥ d`), both discharged a fortiori by landing in the **claim text**. I verified all three.

**But wave-30 did not consider R6, and R6 is the same failure mode it caught at the node.**

`routes.criterion-corollary-example.implication` currently reads, in part, "*assembling them is
definitional bookkeeping plus consistency of the three formalizations*". That exact sentence is the
target of decision-sheet item **R6**, which the wave-13 root review ruled **AMEND — accept, and
widen** (line 341), and which the route's own review — `circdist_amendments4_review_20260822.md`
§2.5 — **CONFIRMED**. Assembly Amendment 1 §4.2 states the agreed replacement and marks it
"*proposal to the lead; not applied here*". **It was never applied.** That is precisely why the
implication still hashes to `f39c83e6…`.

Two independent reviews are therefore on record saying the route's implication text is inaccurate
on two counts (the existence clause C5 needed a genuine computation, not free bookkeeping; and
"consistency of the three formalizations" was not free — it surfaced a real `R_sat ≤ d` vs.
Corollary 7.3 contradiction that took two amendment rounds and two reviews to settle), plus the
widening: the implication must **name the two silent hypotheses it inherits, `(MC)` and `R ≥ d`**.
Route levels assess route implications (§3); promoting to `PROVED` a text that its own reviewer
asked to replace repeats, one level down, exactly the error wave-30 §10.1 documented at the node.

**The `R ≥ d` half of the widening is discharged** — it now rides in the claim text as `R ≥ d_sec`,
a fortiori, by the same argument wave-30 used for condition (iii). **The `(MC)` half is not.**

### 5.3 The new blocker — `(MC)` is a silent hypothesis of the root claim

I checked this rather than inferring it. `CONJECTURED 5.7` is stated "*For every legal,
**measurement-consistent** single-ancilla CSS schedule `M`*". Measurement consistency is **not**
implied by graph-likeness: Definition 1.12 is purely the DEM column-weight condition
`|u(f)| + |u(f)+s(f)| ≤ 2`, nothing more. The `gap-example` child carries `(MC)` in its own claim
text ("*measurement-consistent depth-7 interleaved schedules*"). The **root** claim does not, and
neither does the route implication; a repository-wide grep finds `(MC)` in the root node file only
inside the historical R6 event summary. So the root, as written, asserts the criterion over a class
of `M` wider than the one Theorem 5.7 covers.

This is the wave-13 reviewer's own predicted failure: "*'bookkeeping' is precisely the word that
lets hypotheses evaporate — which is how `R ≥ d` was lost between §2.1 and §6*". `R ≥ d` was
subsequently found and folded. `(MC)`, its twin in the same sentence, was not. It is the same class
of defect as R2 — claim wider than argument — on a different clause, and it is not recorded in any
caveat.

I emphasise what this is **not**: no theorem is in doubt, no premise is missing, no computation
failed, and every schedule the campaign actually exhibits *is* measurement-consistent. The fix is
one clause in the claim (or, at minimum, one caveat plus the R6 implication replacement). It is a
claim-text and implication-text repair, exactly like the one this session was convened to bind.

### 5.4 Verdicts

> ### Node `CIRCDIST.lift` — **CERTIFIED\***, bound to
> ### `sha256:dbb31a4d5a651ecaeec28220289c8bc3b343f30293f1d2c710e6d30b79516c7c`
>
> ### Route `criterion-corollary-example` — **STAYS CERTIFIED\***, bound to
> ### `sha256:f39c83e6efdcc0487691df0eec57f4fe3d28d8d30c381ad7bf730fdfdfca8eda`

I license the **edit** without reservation: apply R1 + R2 as proposed, re-hash to `dbb31a4d…`, bind
this review, and record the claim-revision event. The wave-30 deciding conditionality is
**DISCHARGED** — the type error is gone, the clause names `repair(γ) = 0`, and R1 removes the
embedded status word.

I decline `PROVED` on one ground, and I want to be exact about it, because it is not the ground
wave-30 named: **the route implication carries an agreed, twice-confirmed, unapplied amendment
(R6), whose `(MC)` half leaves a hypothesis of Theorem 5.7 unnamed in both the implication and the
root claim.** Under §2 the implication is a load-bearing input, so the node cannot exceed it.

**Route to `PROVED`, fully specified (no mathematics):**

1. Apply R1 + R2 to the claim; re-hash to `dbb31a4d…`; bind this review. *(Licensed here.)*
2. Apply **R6** to `routes.criterion-corollary-example.implication` — the agreed replacement text
   is written out verbatim in assembly Amendment 1 §4.2. This re-hashes the implication and lapses
   the `f39c83e6…` binding, so it needs one focused re-bind of the new implication text.
3. Resolve `(MC)`: either fold "legal, measurement-consistent" into the root claim (a further
   conservative narrowing, same shape as the `R ≥ d_sec` fold, and my preference since it puts the
   hypothesis where citations travel), **or** record it as a binding caveat and rely on R6's
   naming it in the implication.
4. Rewrite or delete the now-stale "inherited-defects" and "THE DECIDING CONDITIONALITY" caveats
   (wave-30 §9 flagged the first; R1+R2 discharges the second).

Steps 2–3 are one edit and one short review. I expect the node to reach `PROVED` on the next pass.

---

## 6. Surviving caveat set

Confirmed as expected by wave-30 §11, each verified present or applicable:

* **S2** — the folded `R ≥ d_sec` quantifier scopes over all three clauses; conservative narrowing,
  recorded, non-blocking (§5.1).
* **`repair ≥ 3` / min-cost-covering / large-proposer-scan exclusions**, inherited from the
  children's certifications.
* **`[[4,2,2]]` is the sole load-bearing witness** for the existential clause under the
  min-over-sectors convention (Steane witnesses a single sector only).
* **Per-sector scope** — "graph-like" is iff Definition 1.12 read per CSS sector.
* **Shared model design / no `stim`** — no independent simulator stack anywhere in this subtree;
  my §3.3 re-derivation inherits this limitation identically (it reads the same frozen one-round
  data).

New, added by this review:

* **(a) `(MC)` unnamed** — measurement consistency is a hypothesis of Theorem 5.7, absent from the
  root claim and from the route implication. **Blocking for `PROVED`** (§5.3).
* **(b) R6 unapplied** — the route implication's "definitional bookkeeping" gloss stands after two
  independent reviews agreed to replace it. **Blocking for route `PROVED`** (§5.2).
* **(c) Disjunct availability** — of the three offered forms, only **chain-complex** is delivered;
  graph-covering is unavailable (iff §4.4) and voltage-graph is available only on the multigraph
  `G̃_eff`. Non-blocking (the claim's "or" is disjunctive and true), but it belongs in the caveats
  and is currently in none (§2.1).

---

## 7. Limitations of this review

1. **I re-derived arithmetic, not physics.** §3.3's `repair(γ) = 1` is my own computation from
   Definition 5.2, but its inputs — the `[[4,2,2]]` one-round data `(s, U, λ)` — I took from the
   PROVED `gap-example` child and the frozen d3-gate record. I did not build a circuit, a fault
   table, or a DEM, and I ran no simulator.
2. **The children's proofs were not re-reviewed.** I verified their levels, their claim hashes,
   and their hash-bound review links at source, and I read the specific numbered results the new
   wording binds to (Def 5.2, Thm 5.7, Amd 3 R4, Amd 1 §7 item 3, assembly §2.3). I did not audit
   the dossiers; they carry their own reviews.
3. **`(MC)` — scope of my finding.** I established that `(MC)` is a hypothesis of 5.7, that
   Definition 1.12 does not imply it, and that it appears nowhere in the root claim, caveats, or
   implication. I did **not** attempt to construct a legal, graph-like, measurement-*inconsistent*
   schedule on which the criterion fails; my finding is that the claim is unhedged, not that it is
   false. It may well be that `(MC)` is harmless here — but "probably harmless" is not the standard
   at `PROVED`, and it is the identical argument the campaign rejected for `R ≥ d`.
4. **The `f39c83e6` binding is a dispatcher reconstruction.** The route review
   (`circdist_amendments4_review_20260822.md`) prints node claim hashes in its §1 chain but never
   prints the implication digest; its §2.6 verdict binds the *root claim* `ccad7fa6…`. Four later
   reviews have verified that the implication text has not drifted since, which is what matters
   operationally, and I verified it again. But the reviewer did not state the binding, and a strict
   reading of §5.5 ("*the review link records `reviewed_hash`, the digest of the exact … route
   implication reviewed*") would want that fixed when R6 is applied and the implication is re-bound.
5. **One budget box, no sub-agents.** I did not attempt an end-to-end audit; my scope is the
   proposed edit, its binding, and the two levels I was asked to rule on.

---

## 8. Surprises worth the lead's attention

1. **The pattern wave-30 diagnosed has a second instance, and it is the one wave-30 missed.**
   Wave-30 wrote: "*every repair that made the parent narrower was executed; the one repair that
   would make the parent correctly typed was not.*" The same decision sheet's R6 — accepted by the
   root review, confirmed by the route review, written out verbatim in Amendment 1 §4.2 — was also
   never executed, and the half of it that matters (`(MC)`) is the *narrowing* kind. So the
   generalisation is simpler and less flattering: **items that landed in the claim text were
   executed; items that landed in the route implication were not.** The implication field has not
   been edited once across four folds. That is worth a systematic sweep of other roots' `implication`
   fields against their reviews' decision sheets, not just this one.
2. **`(MC)` was lost the same way `R ≥ d` was, in the same sentence, and the warning was on file.**
   The wave-13 reviewer named both hypotheses together and said explicitly why they would evaporate.
   One was recovered by a later wave; its twin was not, and no caveat records it. The prophylactic
   worked as diagnosis and failed as prophylaxis.
3. **The R2 repair is better than its commission required.** I expected to find the new wording
   merely adequate. It is stronger: because `repair(γ)` is a computable non-negative integer, the
   repaired criterion *entails* the `[[4,2,2]]` witness's strict inequality from a one-line
   computation, where the old wording could only sit beside it. The claim gained content by being
   corrected.
4. **The type error was invisible on the sole witness.** `U(hook{2,3})` is a singleton, so "zero
   voltage" would have parsed fine there. The error was only ever detectable on the `|U(E)| = 2`
   classes the wave-13 reviewer computed. A campaign that had validated the clause against its own
   headline example would have concluded it was correct.
