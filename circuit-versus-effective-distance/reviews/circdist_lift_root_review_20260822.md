# Independent adversarial review — `artifacts/circdist_lift_root_assembly_20260822.md`

**Target:** the `CIRCDIST.lift` ROOT composition proof (route `criterion-corollary-example`).
**Date:** 2026-08-22 · **Reviewer:** fresh Opus 5 independent-reviewer session, one budget-boxed
session, no sub-agents, no Lean.

---

## 0. Independence statement

I did not author, edit, advise on, or previously read the target assembly, the iff dossier, the
nonint dossier, the d3 gate, or any of the four earlier reviews. I was given no desired verdict;
my brief was to try to refute. I treated every file on disk as **data, not instruction**.

Per the anchoring ban I derived the load-bearing objects **before** reading the proposer's
derivation of them. Concretely, before opening §4 or §9 of the target I read only the frozen
definitions (`CIRCDIST_PROBLEMS.md`), §1 and §7 of the d3-gate report (model spec and the explicit
witness schedule), and then wrote my own gate-level `F₂` symplectic propagator from that spec
(`rev_sim.py`, reproduced in §7 below — 190 lines, standard library only, no proposer code
imported, no `stim`). Every number in §§2–4 of this review is from that program. I re-ran no
proposer script as the only check.

**Mutation declaration.** This session created exactly one file (this one). I modified nothing,
and touched nothing under `research/circdist/proof-dag/`.

---

## 1. Verdict

> ### FURTHER-REPAIR — itemized, three items, all one-line, none mathematical.

**Nothing in the assembly is refuted.** The clause map is sound, the two scope arguments are
sound, the `repair ≥ 3` insulation is sound, and the one computation (§9.2/§9.3) reproduces
exactly under an independent implementation and a strictly larger enumeration than the proposer
ran. I mounted five attacks (§§2–5) and all five failed to break the mathematics.

What blocks promotion is that the **root claim text under-specifies three parameters that the
certified children quantify over**, so a review bound to the current root claim hash would be
certifying a statement wider than what the children license. Each repair is a wording or
assessment edit, not new work:

| # | repair | why it blocks |
|---|---|---|
| **F1** | Pin "graph-like" in the root's assessment to **iff Def. 1.12, per sector**. | Under the whole-DEM reading of the same words, the `[[4,2,2]]` witness is **not** graph-like — I exhibit an elementary fault firing **4** detectors (§3.3). C5's descent then fails and the root is unsatisfiable as written. |
| **F2** | Carry the certified theorem's **`R ≥ d`** hypothesis into the root claim or its caveats. | Thm 5.7 as certified reads "…and `R ≥ d`". The root claim has no `R` quantifier at all, and §6 of the assembly does not carry it forward (§4.2 below). |
| **F3** | Fix the assembly's own §0.1 trip-wire, which currently **fires**. | 1 of the 14 recorded input hashes no longer reproduces (§2.1). The document says "If any hash above fails to reproduce, this assembly is void until re-derived." Literally read, the assembly is presently self-voided. |

After F1–F3 the assembly clears for root promotion **to the `CERTIFIED*` ceiling and no higher**;
I concur with the assembly's own ceiling argument and with C-R1 as the binding cap.

**VALUE vs PRINTED-DERIVATION (rule 7f), stated per item:**

| finding | value | printed derivation |
|---|---|---|
| Claim-hash freshness of the three children (§2.2) | **CORRECT** | **CORRECT** |
| §0.1 fourteen-hash chain (§2.1) | **13/14 correct; 1 stale** | trip-wire mis-specified (binds node bytes, should bind the claim) |
| Clause map C1–C5 (§3.1) | **CORRECT** | **CORRECT** — I re-derived Thm 5.7 from the child claim text myself before reading §2.1 |
| Graph-likeness of `[[4,2,2]]` under Def. 1.12 (§3.2) | **CORRECT** | **CORRECT**, and the schedule-independence argument is stronger than the scan, as claimed |
| Graph-likeness under the whole-DEM reading (§3.3) | **the words admit a reading under which it is FALSE** | not addressed |
| Steane non-graph-like (§3.4) | **CORRECT** | correct verdict, **non-conservative bound**: their inventory reports `max = 3`, the true raw-fault max is `4` |
| §9.3 criterion-predicts-witness table (§3.5) | **CORRECT, all 8 rows** | **CORRECT** |
| `repair ≥ 3` insulation (§4.1) | **CORRECT** | **CORRECT** |
| `R ≥ d` (§4.2) | correct inside §2.1 | **dropped** between §2.1 and §6 |
| R4's rationale (iii) (§5) | **OVERSTATED** | argument (iii) does not survive the min-over-sectors convention |
| C-R2 stack identity (§6) | flagged, not resolved — correct posture | **containment is right in §6.1, overstated in SCHEDULER round 12** |

---

## 2. Item 1 — hashes and claim-hash binding, checked myself

### 2.1 The fourteen input hashes of §0.1

Recomputed with `shasum -a 256` on current bytes. **Thirteen reproduce exactly.** One does not:

```text
recorded  64963af70bf27195987bc3ce58319b36d24aeb66ce975823f334779e13223de5
current   01f6a8887021446947d09ec6414b5dc17da11b1415118156449f830a15a97c59
file      research/circdist/proof-dag/nodes/CIRCDIST.lift.yaml
```

**Diagnosis (benign, but the trip-wire is wrong).** The drift is caused by the assembly's *own*
registration: the root node gained the `root-assembly-2026-08-22` event after the assembly
computed its hash. The node's **claim** is untouched — I verified it still hashes to
`sha256:ccad7fa605be1ae14a2dbc1d6c5758300bb8a5f0a3023fcef84725be40e78d8a`, exactly the value §0.2
records.

So the *substance* is fine and the *rule* is broken: a proof-DAG node file is append-only and
**gains events by design**, so binding an assembly's validity to the node's whole-file digest
guarantees the trip-wire fires on the first event that registers the assembly itself. This also
makes §8 checklist item 1 ("Recompute all fourteen hashes") unrunnable as written — the very first
item a root reviewer is told to run now fails, on a change that means nothing.

**F3.** Replace the node-file entries in §0.1 with **claim hashes** (which are the objects the
protocol binds — DAG_PROTOCOL §5 step 5), and keep whole-file digests only for the artifacts,
which are immutable. One-line edit; no mathematics moves.

### 2.2 Claim-hash freshness (the precondition of the whole assembly)

I did not read §9.1's code. I wrote my own loader against the repository convention as implemented
in `tools/proof_dag_v6.py::claim_hash` (`sha256(claim.replace("\r\n","\n").strip().utf-8)`), read
each node's `claim` field with `yaml.safe_load`, and compared against the `reviewed_hash` recorded
in that node's own `basis.reviews` entry:

```text
CIRCDIST.lift.iff          sha256:c3a841984a07038dfbe3390f0b25cca633d04877ff92fb04bd0e3eaf480f0061  MATCH
CIRCDIST.lift.nonint       sha256:864bcc604035c7124b7fa23977e00375862520a28f347d092453ddd89b6fed4e  MATCH
CIRCDIST.lift.gap-example  sha256:487340464e4d0c6b6820d134e40bcda128ed400f131806fe091deedd64a5769c  MATCH
CIRCDIST.lift  (root)      sha256:ccad7fa605be1ae14a2dbc1d6c5758300bb8a5f0a3023fcef84725be40e78d8a  (no review linked; correct — root is CONJECTURED)
```

**CONFIRMED.** All three reviews are still bound to the claim text the assembly composes, and all
three children are still `CERTIFIED*` with no REFUTE or FURTHER-REPAIR event after 2026-08-20.
§8 items 1 (claim half) and 2 pass.

---

## 3. Item 1/2 — the clause map and the graph-like descent

### 3.1 Clause map: no silent strengthening found

I did the derivation before reading §2.1. Given only the **certified claim text** of
`CIRCDIST.lift.iff` —

> "d_circ equals the minimum over nontrivial effective logicals gamma of the length of the shortest
> closed spacetime lift of gamma, with an intrinsic zero-voltage/monodromy condition characterizing
> same-weight liftability"

— the root's C1 follows without importing anything: since `ℓ(γ) ≥ |γ|` always, and
`d_circ = min_γ ℓ(γ)` while `d_eff = min_γ |γ|`, we get
`d_circ = d_eff ⟺ ∃γ` with `|γ| = d_eff` and `ℓ(γ) = |γ|`, and the second clause of the child
claim converts `ℓ(γ) = |γ|` into the zero-voltage condition **at minimum weight**, which is exactly
where it is needed. That is Thm 5.7, reached from the claim text alone. **No strengthening.**

Checked clause by clause against the certified texts and their caveats:

* **C1, C2, C3** — inside `lift.iff`'s certified claim. C3's realisation (`repair(γ) = 0`) is the
  same clause of the same claim. The minimum-weight qualifier is respected throughout; the
  assembly explicitly refuses the fixed-non-minimal-`γ` reading (§2.3, carried as C-O1). Correct:
  Amendment 1 §7 item 3 does leave that proviso open, and C1–C3 never need it.
* **C4** — the assembly's split into a *certified weaker reading* (nonint Thm 7.1) and a
  *proposer-level literal-corollary reading* (iff §5.11) is the honest call, and the flag that
  §5.11 is **not named in either child's claim text** is exactly the kind of thing a careless
  assembly would have swallowed. I checked: §5.11 is indeed absent from both claim fields.
* **C5** — discharged from `lift.gap-example`'s certified existence claim, **conditional on the
  graph-like descent**, which is §3.2–§3.3 below.

**Attack that failed.** I looked for a clause quietly relying on the retracted `R_sat ≤ d`, on the
original Def. 5.1, on the unreproduced large scans (`3855/3855`, `98811`, `321059/321059`), or on
general `d_∞`. I found none: `grep` over the assembly turns up each of these only inside §5.1 and
§6.4, i.e. only where it is being *excluded*. §8 item 4 passes.

### 3.2 The `[[4,2,2]]` graph-likeness computation, re-verified independently and more widely

The proposer's §9.2 enumerates an **abstracted one-round inventory** (39 residual-class faults per
sector). I did not use it. I built the actual depth-7 circuit and enumerated **every raw
elementary fault of the frozen model** (ancilla prep `X/Y/Z`; all 15 non-identity two-qubit Paulis
after each of the 8 CNOTs; `X/Y/Z` on every idle qubit at every step; every measurement flip) for
`R = 2,3,4,5` — 412 to 1030 faults per sector — and read off the sector-restricted detector weight
of each DEM column.

First, the model checks that make the comparison meaningful (all mine, all reproduced):

```text
(MC) count for the single pair (a,b) = 2  (even)                            -> schedule is legal
retracted depth-5 recon circuit: (MC) violated on (a,b)                     -> correctly retracted
interleaved witness   d_eff = 1, d_circ = 2 at R = 1,2,3,4,5, both sectors  -> matches child claim
non-interleaved partner (identical within-check orders)  d_circ = 1         -> matches child claim
```

Then the graph-likeness result, under the assembly's stated Definition 1.12
(`|u| + |u+s| ≤ 2` in a sector — equivalently, the fault's weight on that sector's detectors):

```text
[[4,2,2]] depth-7 MC interleaved witness, sector-restricted detector-weight histogram
   Z-memory  R=2 {0:130, 1:216, 2: 66}   R=3 {0:195, 1:324, 2: 99}
             R=4 {0:260, 1:432, 2:132}   R=5 {0:325, 1:540, 2:165}
   X-memory  R=2 {0:126, 1:220, 2: 66}   R=3 {0:189, 1:330, 2: 99}
             R=4 {0:252, 1:440, 2:132}   R=5 {0:315, 1:550, 2:165}
   max sector detector weight = 2 everywhere        ->  GRAPH-LIKE, both sectors
```

**CONFIRMED**, over an enumeration roughly 10–26× larger than the proposer's and at four round
counts rather than one round.

The **schedule-independence argument is also correct and is indeed stronger than the scan**: the
campaign's `[[4,2,2]]` has `|𝒜| = |ℬ| = 1`, so in the Z-memory sector the detector algebra is
`F₂` and `|u| ≤ 1`, `|u+s| ≤ 1` identically — for *every* schedule, not merely the three
survivors. §8 item 6(i) passes.

### 3.3 …but "graph-like" is not pinned, and the other reading kills C5 — **F1**

This is the one place where the assembly's words leave a door open, and it is the highest-value
finding in this review because C5 is the **existential** clause and existentials do not restrict.

Definition 1.12 is **sector-indexed** — the iff document says so verbatim: "`M` is *graph-like*
(in the Z-memory sector) if…". The root claim's own words are not: "In **graph-like detector
error models** with fixed boundaries". Under the ordinary whole-DEM reading of those words — every
elementary fault of the memory experiment fires at most 2 detectors of that experiment — the
`[[4,2,2]]` witness **is not graph-like**. From my enumeration of the same circuit, same model,
`R = 3`, Z-memory, full detector set:

```text
full-DEM detector-weight histogram, [[4,2,2]] witness, Z-memory, R = 3
   {0: 64, 1: 294, 2: 204, 3: 52, 4: 4}          <- 56 faults fire 3 or 4 detectors

explicit weight-4 fault:
   round 1, after the CNOT at t1 (control q0, target ancilla b), Pauli I(x)Y
   fires  D_{b,1}, D_{a,1}, D_{b,2}, D_{a,2}
```

The mechanism is not exotic: in a Z-memory experiment the X-check detectors `D_{a,r}` are present
and are flipped by `Z`-type error, so any fault with both an `X` and a `Z` component (a `Y`, or a
mixed two-qubit Pauli — all of which the frozen §1.3 fault model includes) hits both sectors at
once. I verified that every one of the 14 distinct `≥3`-weight columns is the `F₂` sum of two
graph-like columns, so the DEM is *decomposable*; but decomposability is a weaker property than
Def. 1.12, and it is not what the root claim says either.

**Consequence.** The graph-like descent of C5 is established **only** under the per-sector reading.
The assembly states Def. 1.12 at the head of §4.1, so this is not a silent strengthening — but it
never records that the reading is a *choice that changes the answer*, and §4.4's flat "are
graph-like in both sectors" plus §8 item 6's "If (i) fails, C5 is undischarged" invite a later
reader to take the whole-DEM reading and conclude the opposite.

**F1 (required).** The root's assessment must state: *"'graph-like' is `CIRCDIST.lift.iff`
Definition 1.12, a per-sector condition on the sector's own detectors; the memory experiment's
full DEM is not graph-like in this sense and is not claimed to be."* One sentence. Without it the
root claim, read plainly, has **no** certified witness for its existential clause.

This is a **type-audit** finding (rule 7a): graph-likeness has type `(schedule, sector) → bool`,
and the root claim uses it as though it had type `(model) → bool`.

### 3.4 Steane's non-graph-likeness — correct verdict, non-conservative bound

The assembly reports `max(|u| + |u+s|) = 3` for Steane Z-memory, from qubit 6 lying in all three
Z-checks. I rebuilt the depth-8 Steane witness from the d3-gate schedule and enumerated the raw
faults:

```text
Steane [[7,1,3]] depth-8 witness, sector-restricted detector-weight histograms
   Z-memory  R=2 {0:366, 1:192, 2:402, 3:112, 4: 32}     max = 4
   X-memory  R=2 {0:358, 1:220, 2:414, 3: 96, 4: 16}     max = 4
```

Verdict unchanged (**not graph-like**, so it cannot be cited as a graph-like witness — §4.4 is
right). But the printed bound is **not conservative**: the abstracted inventory reports 3 where the
actual fault set reaches 4, because a single two-qubit Pauli can contribute an `X` part on both the
data qubit and the ancilla. Since §9.2 is used to establish a *maximum*, an inventory that can
undercount the maximum is the wrong instrument. It happens not to matter here (3 > 2 already
decides it) and it does not matter for `[[4,2,2]]` (whose bound is structural, `|ℬ| = 1`), so this
is a **note, not a repair**. It would matter for any future code where the inventory returned
exactly 2.

### 3.5 §9.3 — the criterion predicting the witness, fully reproduced

I computed the Z-sector residual classes and their **full voltage spectra** from my propagator,
independently of the proposer's Prop. 1.13 inventory. All eight rows match §9.3 exactly:

```text
E = []          U(E) = {0,1}   s = 0   lambda = 0
E = [0]         U(E) = {0,1}   s = 1   lambda = 1
E = [1]         U(E) = {0,1}   s = 1   lambda = 0
E = [2]         U(E) = {0,1}   s = 1   lambda = 1
E = [3]         U(E) = {0,1}   s = 1   lambda = 0
E = [2,3]       U(E) = {1}     s = 0   lambda = 1     <- unique weight-1 effective logical, RIGID
E = [1,2,3]     U(E) = {1}     s = 1   lambda = 1
E = [0,1,2,3]   U(E) = {0}     s = 0   lambda = 0     (improper hook; s = 0, lambda = 0, as L3 says)
```

So `repair(γ) = 1 ≠ 0` for the unique minimum-weight `γ`, Thm 5.7 forces `d_circ > d_eff`, Thm
5.6(c) forces `ℓ(γ) = 2`, and my exhaustive enumeration measures `d_circ = 2` at `R = 1..5`.
**CONFIRMED**, value and printed derivation.

This table is also the cleanest independent evidence for **R2**: six of the eight residual classes
have `|U(E)| = 2`. The voltage of a residual is genuinely a **set**, not a scalar, so the root
claim's "zero time-direction voltage" is a type error and R2's rewording is not cosmetic.

---

## 4. Item 3 — the `repair ≥ 3` insulation

### 4.1 No clause needs the excluded regime — CONFIRMED

I re-derived the key step rather than reading it: the `(⟹)` direction of C1 needs no hypothesis on
`repair` for a structural reason the assembly states and I confirm — if `d_circ = d_eff` then a
minimum-weight undetectable logical has weight exactly `d_eff`, so the weight loss under `π₁` is
zero, so the repair certificate it induces has weight zero. `repair ≥ 3` **cannot co-occur with
the equality**, so the regime the certification excludes is disjoint from the regime the root
claim is about. C2 is likewise proved from 5.3′/5.4(1), never from the sandwich. C4 has
`repair ≡ 0`. C5's two instances sit at `repair = 1`, which I confirmed for `[[4,2,2]]` in §3.5.

The absence claim in §5.2 is also **properly scoped** — it names the five clauses, the readings,
and the method (trace each clause to a numbered result, read its hypothesis row). Under this
project's evidence-asymmetry rule that is the right way to state an absence, and I could not break
it. §8 item 7 passes.

§5.3's insulation of the *identity* reading of C2 from the *algorithm* reading is correct and, in
my judgement, the single most useful paragraph in the document: the two readings really are one
comma apart, and only the first is certified.

### 4.2 But a hypothesis is dropped between §2.1 and §6 — **F2**

The assembly's own restatement of the certified criterion (§2.1) reads:

> "For every legal, measurement-consistent single-ancilla CSS schedule `M`, **and `R ≥ d`**,
> `d_circ(C_R(M)) = d_eff(M) ⟺ ∃γ ∈ L_eff` with `|γ| = d_eff(M)` and `repair(γ) = 0`."

I checked the source: iff CONJECTURED 5.7 does carry `R ≥ d`. But:

* the **root claim** has no `R` quantifier and no `C_R(M)` — it says "characterizes when
  `d_circ = d_eff`", unrestricted;
* the **`lift.iff` child claim** has no `R` quantifier either;
* §6 of the assembly — the section whose entire job is "every caveat carried forward, none may be
  dropped by a promotion of the root" — lists C-R1..3, C-M1..6, C-S1..3, C-O1..6 and **`R ≥ d` is
  in none of them**. It appears once, in §2.1, and never again.

This is exactly the failure mode §0.3 was written to prevent, applied to the assembly itself. I
probed for a live counterexample and did not find one at `d = 2`: my enumeration gives
`d_circ = 2` for the interleaved witness and `1` for its non-interleaved partner at `R = 1` as
well as `R ≥ 2`, so `R ≥ d` is not demonstrably load-bearing *on this instance*. That does not
discharge it — a hypothesis of the certified theorem is a hypothesis of anything assembled from
it, and `d_R` is only known to be non-increasing and constant for `R ≥ d`.

**F2 (required).** Either add `R ≥ d` (equivalently: "`d_circ` means `d_circ(C_R(M))` for
`R ≥ d`") to the root claim, or add it to §6 as **C-M7** and to the root's caveats. This is a
second **type-audit** finding: `d_circ` has type `(circuit) → ℤ`, the circuit is `C_R(M)`, and the
root claim never binds `R`.

---

## 5. Item 4 — the R1–R6 decision sheet

One line of reasoning each, as commissioned. Two AMENDs, four AGREEs, plus two additions.

| # | verdict | reasoning |
|---|---|---|
| **R1** — bind "proven" to the `CERTIFIED*` ceiling | **AGREE** (take the reword, not the assessment note) | A conjunction cannot exceed its weakest premise and all three premises are starred; and an assessment note does not travel with the claim hash, whereas the word "proven" travels with every citation — so prefer "an independently reviewed necessary-and-sufficient structural criterion". |
| **R2** — voltage is a SET; reword to minimal repair cost; record that only the chain-complex disjunct is delivered | **AGREE** | Independently confirmed by my own §3.5 computation: six of the eight residual classes of the certified witness have `\|U(E)\| = 2`, so "zero voltage" attaches to no scalar and the liftability condition is a minimum over a spectrum — a type error, not a stylistic one; and the "graph-covering / voltage-graph / chain-complex" disjunction should record which disjuncts are unavailable, since a disjunctive claim silently invites the wrong one. |
| **R3** — insulate C2's identity reading (assessment-only, no claim change) | **AGREE, with F2 folded in** | Correct as written and correctly hash-neutral; the same sentence should carry the `R ≥ d` hypothesis (§4.2), since both are "what the certified theorem actually quantifies over" and both are currently invisible at the root. |
| **R4** — do not drop "graph-like" until `lift.iff` is re-widened and re-reviewed | **AMEND** — right conclusion, one wrong supporting argument | The sequencing is right and decisive (dropping it would make the root wider than its load-bearing child's certified scope). But argument (iii) — "the restriction excludes the campaign's best evidence" — does not survive: under the campaign's own convention that a circuit's distance is the minimum over the two memory sectors (d3-gate §1.4, restated in its §5.2 "so `min(d_circ^Z, d_circ^X) = 2` for this circuit"), the Steane instance has `d_eff = 2` in **both** sectors and `min(d_circ) = 2`, so it is **not a circuit-level `d_circ > d_eff` witness at all** — I reproduced Z-sector `(2,3)` and X-sector `(2,2)` independently. The `[[4,2,2]]` witness, by contrast, has `d_eff = 1 < 2 = d_circ` in **both** sectors. So the graph-like restriction is not discarding the better witness; the witness that survives is the one that is robust to the sector convention, which is an argument *for* the current claim, not against it. Re-file (iii) as: the restriction excludes the campaign's only `d = 3` instance and its only `g(C) = 1` datum, which is a loss of *informativeness*, not of *satisfiability*. |
| **R5** — pin how C4 is discharged | **AGREE, and recommend option (a)** | The root's text is "recovers the non-interleaved equality as a corollary", and `lift.nonint`'s certified claim says exactly "derived (not assumed) from the framework" — that discharges the clause as written, at certified level, today; option (b) buys the literal-corollary reading at the cost of a new claim edit plus a new review of iff §5.11, for no gain in the root's actual words. |
| **R6** — amend the route's "definitional bookkeeping" gloss | **AMEND** — accept, and widen | Both stated corrections are right (C5 needed a real computation; formalization consistency turned up a genuine `R_sat` contradiction that took two amendment rounds). The replacement text should additionally say that the assembly inherits **two silent hypotheses**, `(MC)` and `R ≥ d`, because "bookkeeping" is precisely the word that lets hypotheses evaporate — which is how `R ≥ d` was lost between §2.1 and §6. |
| **R7 (new)** — pin "graph-like" to Def. 1.12, per sector | **PROPOSE — required (F1)** | Without it the root's existential clause has no certified witness under the plain reading of its own words; see §3.3 and the exhibited weight-4 fault. |
| **R8 (new)** — re-base §0.1's trip-wire on claim hashes for node files | **PROPOSE — required (F3)** | Node files are append-only and gain events by design, so a whole-file digest trip-wire self-fires; it already has (§2.1). |

---

## 6. Item 5 — C-R2 stack-identity adjudication

> ### Verdict: **UNDETERMINABLE-FROM-DISK** — with the balance of evidence favouring the self-report, and one containment correction that matters more than the verdict.

### 6.1 What the disk actually says

The completion review that carries `lift.iff`'s promotion,
`artifacts/circdist_amendments2_review_20260820.md`, opens:

> "**Reviewer/session:** `/root/amendment2_reviewer`, fresh single-worker review session, no
> sub-agents, within the commissioned 0.5-session box.
> **Model identity available to the session:** Codex, GPT-5-based."

Every other review in the campaign self-identifies as Opus:

> `circdist_lift_proofs_review_20260820.md`: "**Role:** fresh Opus 5 independent reviewer"
> `circdist_amendments_review_20260820.md`: "Reviewer: fresh Opus 5 session, 2026-08-20"
> `circdist_numerical_review_20260820.md`: "**Reviewer:** fresh Opus 5 session"
> `circdist_islands_review_20260820.md`, `circdist_islandv_review_20260820.md`,
> `circdist_sbbcert_review_20260820.md`: same formula.

And the lead's records treat the chain as same-stack:

> `CIRCDIST.lift.iff.yaml` caveat: "Single same-stack independent review chain; no cross-stack or
> human verification yet."
> `SCHEDULER.yaml` header: "Dispatcher: Fable 5 (supervision + decisions). Workers: Opus 5."
> `SCHEDULER.yaml` round 10: "dispatch the final 0.5-session independent Amendment-2 review" — no
> stack change recorded.

### 6.2 The forensic probe, and why it is inconclusive

I ran a format/provenance probe over all seven circdist reviews plus the assembly. The
amendment-2 review is a clear outlier on five independent axes: it is the only file using
trailing-double-space markdown line breaks (3 occurrences), the only one citing a `/root/…`
session path, the only one with **zero** CJK characters (every other circdist artifact quotes the
Chinese frozen definitions), the only one with zero `·` separators, and it has the lowest
em-dash density in the set.

**But that signature is a harness signature, not a model signature.** Searching the whole
repository for `/root/` reviewer paths turns up two pre-existing artifacts from a different
project and an earlier month:

> `artifacts/ksum_L2_phase27_shared_no_rule7_review_20260721.md`: "Reviewer: fresh independent
> instance `/root/phase27_shared_no_rule7_review`"
> `artifacts/ksum_L3_..._rule7_hostile_baseline_20260722.md`: "Reviewer: fresh independent Rule-7
> instance `/root/pieri_scalars_rule7_review`"

Both carry **exactly the same 3 trailing-whitespace line breaks** and the same `/root/<name>`
instance convention, and **neither declares any model**. So this repository has run "fresh
independent instance" reviewers out of a `/root/…` container since at least 2026-07-21, under a
convention that does not record model identity. The formatting outlier therefore establishes *a
different reviewer harness*, which was already known, and establishes nothing about weights.

There is **no independent provenance on disk**: the circdist artifacts are untracked
(`git status` shows every one as `??`), so there is no commit author; `artifacts/codex_runs/`
contains only July LLM-discovery logs unrelated to circdist; and no session transcript, dispatch
receipt, or process log exists for any circdist session.

That leaves exactly one direct statement about model identity anywhere on disk — the review's own
— and one contrary record — the lead's node caveat. The two are not of equal evidential weight in
the same way: the lead's "same-stack" caveat appears to be an **inherited default** from
`SCHEDULER.yaml`'s standing "Workers: Opus 5" header rather than a determination, since nothing on
disk shows the lead ever checked, and `SCHEDULER.yaml` round 12 records the discrepancy as *newly
noticed* on 2026-08-22. Conversely the self-report is hedged in its own wording — "model identity
**available to the session**" describes what the session's environment told it, which is a claim
about branding as much as about weights.

**Therefore: UNDETERMINABLE-FROM-DISK.** A star must not be lifted on a self-report, and the
assembly's §6.1 posture — "treats the self-report as *data inside a file*, not as a verified fact
about which model executed" — is the correct one and should be adopted verbatim by the lead.
Resolution requires an out-of-band record the lead holds (dispatch receipt, billing or session
log). I recommend the lead answer it directly rather than commissioning further disk forensics:
I have now exhausted what disk forensics can say.

### 6.3 The containment correction — this matters more than the verdict

`SCHEDULER.yaml` round-12 outcomes record the flag as:

> "if true the review chain is CROSS-stack and star prospects change project-wide"

**That overstates it, and the assembly's §6.1 is the accurate version.** Star-lifting attaches to
the review that carries a node's *completion*, and only two nodes link this file:

* `CIRCDIST.lift.iff` — `basis.reviews` lists **only** `circdist_amendments2_review_20260820.md`;
* `CIRCDIST.cplx.islands` — the other target of that review (and it did **not** promote).

`CIRCDIST.lift.nonint` is certified by `circdist_lift_proofs_review_20260820.md` and
`CIRCDIST.lift.gap-example` by `circdist_numerical_review_20260820.md`, **both Opus-self-declared**.
So even under a CROSS-STACK resolution:

* at most **one** node in this subtree (`lift.iff`) becomes star-liftable;
* the **root's star is not liftable either way**, because the root is a conjunction and two of its
  three children remain single-same-stack under C-R1;
* "project-wide" is wrong: no `se`, `ksum`, `whgap`, `gross`, or `sat` node links this file.

The lead's decision sheet should record the narrow version. The practical upshot is small: the
root's ceiling is `CERTIFIED*` under **both** resolutions of C-R2, so C-R2 does not gate this
promotion and should not be allowed to hold it up.

---

## 7. Reviewer's code

`rev_sim.py` — written from `CIRCDIST_PROBLEMS.md` 公共定义 and d3-gate §1.2–§1.5 before reading
§4 or §9 of the target. Python 3, standard library only. Pauli tracking over `F₂`:
`CNOT(c,t): x_t ^= x_c ; z_c ^= z_t`. X-check ancilla prep `|+⟩`, control, measured in X (outcome
flipped by `z_anc`); Z-check ancilla prep `|0⟩`, target, measured in Z (outcome flipped by
`x_anc`); ancilla reset each round. Z-memory: ideal `|0⟩^n`, ideal Z readout (readout of `q`
flipped by `x_q`); X-memory dual. Detectors: `D_{prim,0} = m_0`; `D_{g,r} = m_r + m_{r-1}` for
`r ≥ 1` on both primal and dual checks; terminal `D_{prim,R} = m_{R-1} + ⊕_{q ∈ supp} readout(q)`.
Faults: prep `X/Y/Z`; all 15 non-identity two-qubit Paulis after each CNOT; `X/Y/Z` on every qubit
idle at a step; one classical flip per recorded outcome. `d_circ` by DEM-column de-duplication,
then weight-1 (empty mask, observable 1), weight-2 (equal masks, different observable), weight-3
(meet-in-the-middle over pairwise mask sums).

Validation before use, all against facts I had not yet seen derived in the target: `(MC)` count 2
for the witness pair; `(MC)` violated for the retracted depth-5 recon circuit; interleaved witness
`(d_eff, d_circ) = (1, 2)`; non-interleaved partner `(1, 1)`; Steane witness Z-sector `(2, 3)` and
X-sector `(2, 2)`, with `150/286` distinct DEM columns at `R = 2/3` against the d3-gate's
`149/285` — a one-column difference in the Z sector from an idle-slot convention, with **every
distance identical**, which I record as a known, benign implementation gap rather than a finding.

**Limitation, inherited (the target's own C-O2, and it binds me too).** My simulator is
independent in its code but not in its *model design*: it enumerates the same fault locations and
uses the same detector definitions as the documents it checks, because both come from the same
frozen spec. A systematic modelling error against `stim`'s conventions would survive my checks as
it survived theirs. `stim` was not available to this session; I did not install it.

---

## 8. Summary for the dispatcher

* **Root promotion:** **FURTHER-REPAIR**, three one-line items — **F1** pin "graph-like" to
  Def. 1.12 per sector (else C5 has no witness under the plain reading; explicit weight-4 fault in
  §3.3); **F2** carry `R ≥ d` into the claim or the caveats (dropped between §2.1 and §6);
  **F3** re-base §0.1's node-file trip-wire on claim hashes (it currently fires, §2.1). After
  those, **clears to `CERTIFIED*` and no higher**.
* **Nothing refuted.** Clause map, scope arguments, `repair ≥ 3` insulation, and both computations
  survive independent reconstruction; §9.3 reproduces row for row; the `[[4,2,2]]` graph-likeness
  result reproduces under a 10–26× larger enumeration and its schedule-independence argument is
  sound.
* **Decision sheet:** R1 AGREE · R2 AGREE · R3 AGREE (fold in `R ≥ d`) · R4 **AMEND** (right
  conclusion, argument (iii) fails under the min-over-sectors convention — Steane is not a
  circuit-level witness) · R5 AGREE, take option (a) · R6 **AMEND** (also name `(MC)` and
  `R ≥ d`) · **R7** and **R8** proposed as required (= F1, F3).
* **C-R2:** **UNDETERMINABLE-FROM-DISK.** The only model-identity statement on disk is the
  review's own; the `/root/` + formatting signature is a *harness* signature shared with July
  `ksum` Rule-7 reviewers and carries no model information; there is no git author, no run log, no
  transcript. **Containment correction:** at most `CIRCDIST.lift.iff` is affected, the root's star
  is not liftable under either resolution, and `SCHEDULER.yaml` round 12's "project-wide" should be
  narrowed. **C-R2 does not gate this promotion.**
