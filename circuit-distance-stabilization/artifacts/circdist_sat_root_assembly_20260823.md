# `CIRCDIST.sat` — the root composition proof, assembled

**Node:** `CIRCDIST.sat` (root, revised question 4) · **Date:** 2026-08-23 · **Role:** Opus 5
executor, proposer. **Box:** one session, stop-loss binding. No sub-agents. No Lean. No proof-DAG
object touched. Canonical files under `research/circdist/proof-dag/` were read only.

**What this document is.** The parent obligation of the route `asymptotic-stability-assembly` is
the implication

> `CIRCDIST.sat.transfer` **and** `CIRCDIST.sat.window` **and** `CIRCDIST.sat.instances`
> jointly establish the `CIRCDIST.sat` root claim.

The node records that implication as a blueprint plus one explicit obligation: *"audit that their
boundary, schedule-legality, CSS-sector, and unit-fault conventions agree."* All three premises are
now `CERTIFIED*` with hash-bound reviews, so the blueprint is executable for the first time. This
document executes it: it restates the root claim, splits it into clauses, maps each clause onto the
**certified claim text** of the premise that discharges it, records for every computed instance the
**R-window the pair was actually computed on** and what decides the tail beyond it, performs the
convention audit on six axes (the four the route names, plus idle-compression and the
detector/observable split, which the wave-11–25 record shows are where this campaign's convention
slips actually live), composes the three caveat sets into the root's inherited conditionality, and
ends with a revision sheet for the lead and the checklist a completion review of the **root** must
run.

**Epistemic ceiling (binding on every line below).** Nothing here is labelled `PROVED` or
`CERTIFIED*`. The assembly argument is **CONJECTURED**; the one computation is **NUMERICAL** with
its code inline (§8). This session is a proposer and cannot grant itself a completion level. The
three premises' `CERTIFIED*` levels are read off the canonical node records; this document does not
re-certify them, does not re-review their contents, and does not propose a level change. The
promotion gate for this route is the independent review of *this* document.

**Three findings stated up front.**

1. **The route is not a flat conjunction.** `CIRCDIST.sat.instances` caveat **(W)** states that its
   own `d_∞`/`R_stab` readings *import* `CIRCDIST.sat.window`. So the AND-route is really
   `window → instances`, plus `transfer` alongside. A defect in `window` propagates into
   `instances` and the two are not independent evidence. The route implication text says
   "together these three premises establish"; it does not say this. §0.4, revision **R5**.

2. **The root claim's own definition of `R_stab` is off by one** against the definition all three
   premises use. The root says *"`R_stab(M)` the first round **after which** the sequence is
   identically `d_∞(M)`"*; the premises use `R_stab = min{R_0 : d_R = d_∞ ∀ R ≥ R_0}`. On the
   campaign's headline cell (rotated surface `d = 5`, class D, `d_R = 4,3,3,3,…`) the premises
   return `R_stab = 2` and the root's wording returns `1`. This is wording-level and repairable;
   it is also exactly the number the campaign's headline discovery is about. §5, revision **R3**.

3. **The claim-level decision procedure is weaker than the campaign needs, and one lemma fixes
   it.** The window premise's *claim text* carries the fixed window ("the first `d` distances
   decide both"); the strictly better adaptive rule of its Corollary 5.4 is document-level and
   therefore not usable by this assembly under the usage rule of §0.3. Two reported cells
   (`d = 7` standard, `d = 9` class D) were computed on windows shorter than `d`. §2.6 derives
   **Lemma A.1** — *if `d_{R*} = v` for some computed `R* ≥ v − 1`, then `d_∞ = v` and
   `R_stab = min{R : d_R = v}`* — from the window premise's **claim text alone**. It closes the
   truncation on every reported cell except one (`d = 7` standard, X-sector), which needs a single
   further MILP cell. §2.6, §5 residual **G3**.

---

## 0. Inputs, hash chain, and what "may be used"

### 0.1 Bound inputs

Recomputed from the current bytes this session (`shasum -a 256`; sizes in bytes / lines):

```text
root node   research/circdist/proof-dag/nodes/CIRCDIST.sat.yaml
            1ba58fe2c38983d1455a16abd16a2ace38cb79e0f5682b03331dbc0a6cbfbe39    8723 B,  153 L
premises    research/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml
            21c48be606f5bb4c65a506016dab81ebc6b4dddce71a3eae93bfa1025ab3ff7c   12369 B,  186 L
            research/circdist/proof-dag/nodes/CIRCDIST.sat.window.yaml
            cec9c0ae1d62e9e8416f5122f4a75864619935a011435f5bd34d7955886b58b4   13611 B,  226 L
            research/circdist/proof-dag/nodes/CIRCDIST.sat.instances.yaml
            3a58fba4552977cfabb162896177dce3f980af78f33472416edbd63df15efc19    9169 B,  150 L

transfer    artifacts/circdist_sat_transfer_proof_20260823.md
            4fce5371edc09fa153b41f6735d521d31500b84b55a0059c8b42dc000651da30   90772 B, 1485 L
            artifacts/circdist_sat_transfer_review_20260823.md
            a9afbf93713634237dfcb795d98e71072537e7370a3fa675dcdf1ac766110003   30725 B,  452 L
            artifacts/circdist_sat_transfer_amendment1_20260823.md
            6c7a8fb756cfba958f82c70f739ffa90aee19070c2cae8f358d44ccdc20ad07e   61291 B, 1024 L
            artifacts/circdist_sat_transfer_rereview_20260823.md          (clearing review)
            3cc2b5784951b14b3ae534de5be1a5f3b3a303a1cc30fc539b04eab7c9a45a44   25369 B,  424 L

window      artifacts/circdist_sat_window_theorem_20260822.md
            487acf030bc4385ab367e5c7b27a0e2015bae4055f16ba61100ea85866d37e1b   57788 B,  932 L
            artifacts/circdist_sat_window_review_20260822.md
            219a756e9e366d74cd6d4b13ff91bdb8394ed35f5c922d3f864b176fcf697226   22060 B,  342 L
            artifacts/circdist_sat_window_amendment1_20260822.md
            295e1635cc7a27c6ca43d88e7a9303c5bbfac96aeaecb1d2fee1a5cad4ac9799   27426 B,  457 L
            artifacts/circdist_amendments4_review_20260822.md             (clearing review, item 2)
            49484a887416bf43649c4e7b45c65f7cb04328311989f1cafb56a4b2eac24763   35745 B,  544 L

instances   artifacts/circdist_sat_instances_20260823.md
            8984df0c51311f4ad80dd12fff58ac46829d5e4bd05b160122538ae9d415c3aa   40238 B,  609 L
            artifacts/circdist_sat_instances_review_20260823.md           (clearing review)
            1e215a06ac276f3416f3506889fa9b04e0a5eeb38028e6caf7eba503fd7d9b25   23784 B,  391 L

context     artifacts/circdist_readjudication_20260823.md                 (wave-11, §6)
            cec9c7ca489f85d215bfe06a880576ba7a2efc69ed41156ec3920f0854b914a2   43345 B,  616 L
            artifacts/circdist_lift_iff_amendment3_20260823.md            (cor73-sector-flag source)
            e35324bfdf16d49e2b3a1bc4297d7fbed4feb0ce412b9ecec9b3fcc4cfd9e28c   75528 B, 1388 L
            artifacts/circdist_lift_claimrepair2_review_20260823.md       (wg1-witnessed source)
            9a0d3378e3fbc655114593cc52417b006fc51d2e5b3f57be43fef4373271cfc7   32656 B,  476 L
            artifacts/circdist_sat_recon_20260820.md                      (round-1 recon)
            bde5d9e2fd686936305255ba7cd5ed7398930981130e4f5b8a21f798d5c063e9   45217 B,  697 L

frozen      research/circdist/notes/CIRCDIST_PROBLEMS.md                  (not modified)
            5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64   10199 B,  243 L
            research/circdist/notes/SAT_RESCOPE_20260822.md               (not modified)
            6c8ec4362f728713f9934d5f0b8041195f66434ebe283a69e67147b3c7009d7f    6112 B,   98 L
```

Two chain notes, both expected and both recorded rather than repaired:

* The instances dossier's own §0 declares the window theorem at `487acf03…` and the transfer proof
  at `4fce5371…`; **both reproduce exactly** against the bytes above. Its declared *node* hash is
  stale (the node has since taken two append-only events) — that is the instances review's Defect 3
  and is the designed trip-wire behaviour, not a fault.
* The transfer proof's §0 declares a `§11.4` program digest that Amendment 1 supersedes. Carried
  as a caveat (§4, **R-C11**), not treated as a chain break.

If any hash above fails to reproduce, this assembly is void until re-derived.

### 0.2 Claim-hash verification of the three premises (the precondition, verified)

Under the repository convention — `tools/proof_dag_v6.py::claim_hash`, i.e.
`sha256(claim.replace("\r\n","\n").strip().encode("utf-8"))` — recomputed this session from the
current node bytes (code in §8.1):

| premise | level | recomputed claim hash | recorded `reviewed_hash` | verdict |
|---|---|---|---|---|
| `CIRCDIST.sat.transfer` | CERTIFIED\* | `sha256:eb50730d33e716c1…d9896ca5` | `eb50730d33e716c1…d9896ca5` | **MATCH** |
| `CIRCDIST.sat.window` | CERTIFIED\* | `sha256:8698b051b15fa14f…49466146` | `8698b051b15fa14f…49466146` (both linked reviews) | **MATCH** |
| `CIRCDIST.sat.instances` | CERTIFIED\* | `sha256:c71ac7cdbd8ddea9…6e22ec5f3` | `c71ac7cdbd8ddea9…6e22ec5f3` | **MATCH** |

**No mismatch. The assembly proceeds.** This is a precondition, not a decoration: it establishes
that the claim text each clearing review bound itself to is still the claim text this document
composes. Full digests:

```text
CIRCDIST.sat.transfer   sha256:eb50730d33e716c13be3d46fa92afab98a9e223aa2ac46aff960a9fcd9896ca5
CIRCDIST.sat.window     sha256:8698b051b15fa14ff669299580d9b7bfec01808c0a34133ef09264e749466146
CIRCDIST.sat.instances  sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3
```

The root's own current claim hashes to

```text
CIRCDIST.sat            sha256:5f6e79d8b5c1f08ba0c050921b27521b977a36a953f53628832392c74372e007
```

If any revision of §5 is adopted, that value changes and any review bound to the old value lapses.
The root carries no `reviewed_hash` today, so nothing lapses on adoption *now* — which is the
cheapest moment to adopt R1–R3.

### 0.3 The usage rule this document obeys

**Only what a review certified may be used, and only in the scope in which it was certified.**
Concretely:

1. A premise discharges a root clause only via that premise's **canonical claim text**, not via an
   arbitrary numbered result inside its artifact. Where a numbered result is needed that is *not*
   named in the premise's claim, this document says so explicitly and marks the step
   proposer-level. This bites in exactly two places and both are flagged: the window premise's
   adaptive halting rule (Corollary 5.4, **not in the claim**, §2.3) and the transfer premise's
   Proposition 3.7 (detector-convention bridge, **not in the claim**, §3.6).
2. The three nodes' `caveats` lists and the three clearing reviews' licence sections are hard
   boundaries. Nothing outside them is imported.
3. Where a base document and an amendment conflict, the amendment governs: Transfer Amendment 1
   governs the transfer proof on T-G3(a), Remark 6.5, the block-mirror labels and F4/F5; Window
   Amendment 1 governs the window theorem on S3′ and W-G5. Two base-document statements are
   therefore **not used anywhere below**: the transfer proof's original T-G3 mitigation *"any `𝒟`
   between Def-2.7 and `V` leaves the theorem intact"* (refuted by counterexample and withdrawn),
   and the window theorem's original scope clause S3 *"enlarging the detector set can only decrease
   `d_circ`"* (struck by its review, replaced by S3′).
4. Numbers are quoted from the artifacts, not recomputed here, except for the two independent
   checks of §8 which are labelled NUMERICAL and carry their code.

### 0.4 Finding 1, expanded: the route's internal dependency

`CIRCDIST.sat.instances` caveat **(W)**, verbatim: *"The `R_stab` and `d_∞` readings import the
window theorem (`d_R = d_d` for `R ≥ d`) from `CIRCDIST.sat.window`, itself CERTIFIED\* — this node
inherits that conditionality."* The instances dossier fences it the same way in its §7(W), and its
review re-fences it in licence item 1.

Consequences the route implication does not currently state:

* The three premises are **not** three independent supports. The dependency graph inside the route
  is `window → instances`, with `transfer` alongside and used by neither as a load-bearing input
  (instances §7(T): *"no reported number depends on Theorem T"*).
* Therefore the root's conditionality is **not** the union of three independent risks; a window
  defect is a double hit. It also means a reviewer who attacks `window` is attacking two of the
  three premises at once — which is the efficient attack and should be said so in the route text.
* In the other direction the dependency is *bounded and measured*: instances §7(W) and its review
  both record that inside the computed window nothing is imported, and the review re-exhibited
  `d_R ≤ d` by explicit construction rather than by import. §2.6 quantifies exactly how far the
  import reaches on each cell.

Revision **R5** proposes one sentence in the route implication recording this.

---

## 1. The root claim, restated exactly and split

### 1.1 Verbatim

From `research/circdist/proof-dag/nodes/CIRCDIST.sat.yaml`, field `claim`, reflowed only:

> For a fixed legal single-round single-ancilla CSS syndrome-extraction schedule M under ideal
> initialization and final data readout, let d_R(M) be the circuit distance after R repeated
> rounds, d_infinity(M) = lim_{R to infinity} d_R(M), and R_stab(M) the first round after which the
> sequence is identically d_infinity(M). Give a finite-state min-plus representation of d_R, prove
> an explicit finite-window theorem and algorithm deciding (d_infinity,R_stab), compute or
> rigorously bound that pair for a standard surface-code schedule, a legal hook-misaligned
> surface-code schedule, and at least one qLDPC schedule, and attribute the distance-limiting
> mechanism using auditable minimum witnesses.

### 1.2 The eight clauses

Splitting is an interpretive act, so it is done once, here, and every later section refers to these
labels. The split follows the claim's own punctuation; the preamble is given its own label because
it carries three definitions that the rest of the claim presupposes.

| clause | text | kind |
|---|---|---|
| **(C0)** | the model preamble: fixed **legal single-round single-ancilla CSS** schedule `M`, **ideal initialization and final data readout**, `d_R(M)` = circuit distance after `R` repeated rounds, `d_∞ = lim_R d_R`, `R_stab` = first round after which the sequence is identically `d_∞` | definitional; presupposes the limit exists |
| **(C1)** | give a **finite-state min-plus representation** of `d_R` | existential, constructive |
| **(C2)** | prove an **explicit finite-window theorem** | universal |
| **(C3)** | …**and algorithm deciding** `(d_∞, R_stab)` | constructive |
| **(C4a)** | **compute or rigorously bound** the pair for a **standard surface-code schedule** | existential, computational |
| **(C4b)** | …for a **legal hook-misaligned surface-code schedule** | existential, computational |
| **(C4c)** | …for **at least one qLDPC schedule** | existential, computational |
| **(C5)** | **attribute the distance-limiting mechanism using auditable minimum witnesses** | interpretive + computational |

### 1.3 What is *not* in the root claim

Recorded because the campaign's most eye-catching results sit here and must not be smuggled into
the discharge:

* **The fitted law `d_R = max(d − R, (d+1)/2)`, `R_stab = (d−1)/2` is NOT part of the claim.**
  Confirmed by inspection of the verbatim text: the claim asks for *the pair* for three named
  schedules, not for a law in `d`. It stays `CONJECTURED` on the instances node and composes into
  the root as an explicit exclusion (§4, **absorbed A2**), not as a caveat on a delivered clause.
* **"Two independent methods where feasible" is NOT part of the root claim.** It is a clause of
  the *instances premise's* claim. The instances premise therefore over-delivers relative to the
  root on method count, and a root clause is not damaged where only one method ran. §2.4 records
  method counts anyway, because they are the difference between a strong and a bare discharge.
* **"`R_stab` is unbounded" is NOT part of the claim** — it is a consequence of the fitted law.
* **No complexity claim.** "Explicit … algorithm" is discharged by an algorithm that terminates
  with a proof of correctness; both premises' constructions are exponential in the code parameters
  (transfer **T-G4**) and neither claims otherwise. §5, revision **R6**.

---

## 2. Clause-by-clause discharge

### 2.0 (C0) — the model preamble

**Discharged, with one wording defect and one scope pin.**

| preamble element | premise carrying it | status |
|---|---|---|
| legal single-round single-ancilla CSS schedule | window scope **S1** = transfer scope **T1** (verbatim same class); instances **(C3)** | **aligned**, §3.2 |
| ideal initialization and final data readout | window Def 1.7/1.8; transfer Def 2.6; instances **(C4)** | **aligned**, §3.1 |
| `d_R(M)` = circuit distance after `R` repeated rounds | window Def 1.12; transfer Def 2.11; instances **(C1)** | aligned **under the verbatim-repetition reading**, §3.5 |
| `d_∞ = lim_R d_R` **exists** | window claim, part (i): `d_{R+1} ≤ d_R`, "the limit `d_∞(M)` exists" | **discharged** — this is not free, and the window premise is what makes the root's own definition well-posed |
| `R_stab` = "first round after which the sequence is identically `d_∞`" | window claim: `R_stab(M) ≤ d_∞(M)` presupposes the premises' `min{R_0 : d_R = d_∞ ∀R ≥ R_0}` | **off by one**, Finding 2, revision **R3** |

The off-by-one, concretely. On the campaign's headline cell (rotated surface `d = 5`, class D,
both sectors) the computed sequence is `d_R = 4, 3, 3, 3, 3, 3, 3` for `R = 1..7`.

* Premises' definition: `min{R_0 : d_R = 3 ∀ R ≥ R_0} = 2`.
* Root's wording, read literally: the first round *after which* the sequence is identically `3` is
  round **1** (after round 1: `d_2, d_3, … = 3`).

The two definitions differ by exactly one whenever `R_stab ≥ 2`, i.e. on precisely the class of
schedules this campaign discovered. Every certified statement — `R_stab ≤ d_∞ ≤ d`, the headline
`R_stab = 2/3/4`, the conjectured `(d−1)/2` — uses the premises' definition. The repair is to
replace the root's clause by the premises' formula verbatim; it is wording-level, and adopting it
costs nothing today because the root carries no hash-bound review.

**Scope pin (C0), non-negotiable:** the root's "`R` repeated rounds" is read as **`R` verbatim
repetitions of the one-round block `M`**, which is window Def 1.7 and transfer Def 2.6. See §3.5:
this reading is not merely convenient, it is the reading under which all three premises are
statements about the same object, and it is also the reading the root's own phrase most naturally
bears. Revision **R1** makes it explicit.

### 2.1 (C1) — finite-state min-plus representation

**Discharged by `CIRCDIST.sat.transfer`, at CERTIFIED\*, with the evidence-scope caveat carried.**

The transfer claim text delivers (C1) word for word:

> …there is an explicitly constructible finite min-plus transfer system `(u,A,v)` such that
> `d_R(M) = u^T min-plus A^R min-plus v` for every `R`, with the two CSS sectors, boundary
> conditions, unreachable states, and logical terminal condition represented exactly.

Every noun of (C1) is matched: *finite-state* (`Σ = F₂^n/S_X` per sector, finite), *min-plus*
(explicit `⊙`), *representation of `d_R`* (an identity for every `R`, not an asymptotic), and the
claim's own "explicitly constructible" answers the root's "give".

**What is fully discharged.** The representation itself, for the whole schedule class of T1 — any
depth, interleaved or not, dependent generating sets allowed, both CSS sectors.

**What is discharged only conditionally, and must be carried:**

* **Evidence scope ≠ statement scope** (transfer caveat 4, verbatim): the theorem is stated for
  arbitrary legal single-round single-ancilla CSS schedules, but the *document's* computational
  evidence covers `d = 3, k = 1, R ≤ 3` (one `k = 2` instance for the fault dictionary only), no
  qLDPC instance; the general case rests on the reviewed derivations. **The assembly carries this
  caveat honestly and does not launder it** — but it also records a fact the transfer node's caveat
  predates: the instances premise independently corroborated Theorem T at **`d = 5`** (all 16
  legal+(MC) uniform schedules, both sectors, `R = 1..7`) and on the **BB `[[18,4,4]]`** code
  (`k = 4`, dependent generating sets of rank 7 in 9 checks — independently re-verified this
  session, §8.2 — under a `T = 12` non-interleaved schedule), in every case with method **T**
  agreeing with **S** (stim) and/or **M** (MILP), which do not use Theorem T. That is corroboration
  of a wider evidence scope, **not** an extension of the proof; the general case still rests on the
  reviewed derivations. §5, revision **R4**.
* **T-G3 is closed by decision, not by derivation** (transfer caveat 1). The canonical
  detector/observable split is Definition 3.5, ratified by the lead as the intended reading of the
  frozen 公共定义; the withdrawn mitigation is not used anywhere here (§0.3 rule 3). See §3.6.
* **Open minors T-G1/G2/G4/G5**, the Y-projection's dependence on the uniform unit-cost Pauli
  model, and external assumption A1 (BCOQ Thm 3.112, min-plus eventual periodicity, cited as
  published and not re-derived). None of these changes a value of `d_R`; T-G2 (state-space
  minimality) and T-G4 (cost of building `A`) change only the *size* of the object one must build,
  which is exactly what stopped method **T** at `d = 7` in the instances arm.

### 2.2 (C2) — explicit finite-window theorem

**Discharged by `CIRCDIST.sat.window`, at CERTIFIED\*, with W-G2 as the deciding conditionality.**

The window claim text delivers (C2) with room to spare: monotonicity, existence of the limit,
contiguity of minimum witnesses with span at most their weight, and

> …therefore `R_stab(M) ≤ d_∞(M) ≤ d` and `d_R(M) = d_d(M) = d_∞(M)` for all `R ≥ d`; hence the
> first `d` distances decide both `d_∞` and `R_stab`.

The root asks for an **explicit** window. The window is `B = d` — explicit, and (this is the part
the frozen 课题四 asked for and did not get from the pumping route) **with no dependence on the
cross-round state-space dimension `r`**. The frozen text asked for "一个明确可计算的函数 `B(r,d)`";
the delivered answer is the constant function `B(r,d) = d`. That is a strictly stronger discharge
than the frozen minimum acceptance, and it should be said so.

**Carried conditionalities:**

* **W-G2 is the deciding conditionality** (window caveat 1, adjudicated wave 11): the claim
  quantifies over *every* fixed legal schedule, but round-translation covariance fails for layouts
  that compress idle layers across round boundaries, and the theorem's own §8 leaves parts (i)–(iii)
  unproved for that layout. §3.5 audits this against the instances schedules and reports a
  provenance finding that bears directly on how severely the **root** inherits it.
* **W-G1 is LOAD-BEARING-WITH-WITNESS**: the `d_∞ ≤ d` clause is **false** under a per-sector
  reading and survives only under min-over-sectors. §3.3 verifies this against the instances data,
  with a correction to how the instances dossier characterises its own witness.
* **W-G4 open**: is `R_stab ≤ d_∞` tight? The instances arm *gains data, not closure* (the wave-25
  reviewer's words): the observed ratio `R_stab/d_∞ = (d−1)/(d+1) → 1`, so the bound is
  asymptotically tight **if** the conjectured law holds — and the law is the conjectured part.
* **W-G3 must not be carried** (window caveat 2, explicit): refuted as written and replaced by
  S3′, and the replacement *removes* a hypothesis. §0.3 rule 3 enforces this.

### 2.3 (C3) — algorithm deciding `(d_∞, R_stab)`

**Discharged, jointly, with a precision note that matters for §2.6.**

(C3) needs two things: a decision procedure with a correctness proof, and a way to evaluate its
inputs. They come from different premises.

| ingredient | source | in the premise's **claim text**? |
|---|---|---|
| the procedure and its correctness: `d_∞ = d_d`; `R_stab = min{R ∈ {1..d} : d_R = d_d}` | window claim, final clause: *"the first `d` distances decide both"* | **yes** |
| an exact evaluator for each `d_R` | transfer claim: `d_R = u ⊙ A^{⊙R} ⊙ v` with `(u,A,v)` **explicitly constructible** | **yes** |
| the strictly better adaptive rule (halt at the first `R` with `R ≥ d_R`) | window theorem **Corollary 5.4** | **NO — document-level only** |

So (C3) is discharged at claim level by the **fixed** window: `d` circuit-distance computations on
circuits of at most `d` rounds, no circuit longer than `d` rounds ever constructed. The adaptive
rule is real and is proved in the window document, but it is not in the certified claim, so this
assembly may not lean on it (§0.3 rule 1). §2.6 shows why that restriction is not merely pedantic:
two reported instance cells were computed on windows shorter than `d`, and under claim-text-only
material the fixed rule does not reach them.

Precision note for the lead: "algorithm" here means *terminating with a correctness proof*, not
*efficient*. Building `A` is exponential in the code parameters (T-G4, which explicitly does **not**
assert NP-hardness and explicitly flags the Vardy / Kapshikar–Kundu citations as unverified and
distinct from the decoding results). Revision **R6**.

### 2.4 (C4a/b/c) — the three named instances, with their R-windows

**All three arms delivered, at CERTIFIED\*, with per-cell scope recorded.**

The root asks to "compute **or rigorously bound**" the pair for one standard surface schedule, one
legal hook-misaligned surface schedule, and at least one qLDPC schedule. The instances claim text
delivers all three and more. The table below is the thing the root clause actually needs and that
no premise states in one place: **for each cell, the R-window on which the pair was computed, the
methods that ran, and what licenses the tail beyond that window.**

"Decided at" = the smallest `R*` at which claim-text-only material (window claim + Lemma A.1 of
§2.6) fixes the pair. `d + 2` is the instances arm's own target window.

| cell | sector(s) | computed R-window | methods | decided at `R*` | pair `(d_∞, R_stab)` | root clause |
|---|---|---|---|---|---|---|
| rotated surface `d = 3`, standard (class A) | Z, X | `1..5` | T, S | `2` | `(3, 1)` | **C4a** |
| rotated surface `d = 5`, standard (class A) | Z, X | `1..7` | T, S (+M, B on decisive members) | `4` | `(5, 1)` | **C4a** |
| rotated surface `d = 7`, standard | Z | `1..6` (MILP), `≤2` (stim) | M, S | `6` (exactly tight) | `(7, 1)` **Z-sector** | bonus |
| rotated surface `d = 7`, standard | X | `1..5` (MILP), `≤2` (stim) | M, S | **not reached** (needs `R* ≥ 6`) | **undecided** | residual **G3** |
| rotated surface `d = 5`, class D (doubly misaligned) | Z, X | `1..7` | **T, S, M, B** (four) | `2` | `(3, 2)` | **C4b** ← headline |
| rotated surface `d = 7`, class D | Z, X | `1..9` | S, M | `3` | `(4, 3)` | C4b |
| rotated surface `d = 7`, classes B, C (singly misaligned) | the *reduced* sector (B: X, C: Z) | `1..9` complete by both methods; the unreduced sector `≤5` (M) / `≤2` (S) | S, M | `3` | `(4, 2)` | C4b |
| rotated surface `d = 9`, class D | Z | `1..7` | M; stim `R ≤ 3` | `4` | `(5, 4)` | bonus, proposer-level |
| rotated surface `d = 9`, class D | X | `1..6` | M | `4` | `(5, 4)` | bonus, proposer-level |
| BB `[[18,4,4]]` qLDPC, schedule NI, `T = 12` | Z, X | `1..6` (`= d + 2`) | T, S, M (Z); T, S (X) | `2` | `(3, 1)` | **C4c** |

**(C4a) standard surface — DISCHARGED.** The root needs one standard schedule; `d = 3` and `d = 5`
each deliver `(d, 1)` on a window reaching `d + 2`, by two independent methods, and both were
independently re-run by the wave-25 reviewer ("CONFIRM at `d = 3, 5`"). The `d = 7` standard cell is
a bonus that the reviewer explicitly did **not** check and that §2.6 leaves undecided in the
X-sector; nothing in (C4a) depends on it.

**(C4b) legal hook-misaligned surface — DISCHARGED, and it is the campaign's discovery.** The
`d = 5` class-D cell is the load-bearing one: `d_R = 4,3,3,3,3,3,3` over `R = 1..7` in **both**
sectors, four independent methods (own min-plus transfer engine; stim's own DEM search; exact
MILP on an independently built spacetime matrix; exhaustive weight-`≤3` enumeration against
criterion (W) at `R = 1`), an audited weight-3 two-round minimum witness recomputed from raw
locations by round-by-round propagation, and stim's *own* independently produced witness likewise
spanning two rounds. The wave-25 reviewer rebuilt the legality+(MC) space (`576 → 96 → 16`, member
indices matching) and re-derived the cell by three independent methods plus a fourth forward-replay
witness audit. **The schedule is legal and (MC)-satisfying**, which is what makes it an instance of
(C4b) rather than a curiosity: §3.2 audits that "legal" means the same thing in all three premises.

**(C4c) qLDPC — DISCHARGED, with the scope stated.** Bivariate-bicycle `[[18,4,4]]`,
`l = m = 3`, `A = 1 + y + x`, `B = 1 + y + x²y`, `H_X = [A|B]`, `H_Z = [Bᵀ|Aᵀ]`; non-interleaved
schedule NI at `T = 12`, legal and (MC); `(d_∞, R_stab) = (3, 1)` over `R = 1..6 = d + 2` by three
methods in the Z-sector and two in the X-sector. I re-derived the code parameters independently
this session (§8.2): `n = 18`, `rank H_X = rank H_Z = 7` of 9 checks, all check weights 6, all qubit
degrees 3, `k = 4`, `d_X = d_Z = 4`. This is the arm that exercises **dependent generating sets**
(`dim leftker(H_X) = 2`), i.e. precisely the case the surface arm never touches and that scope
clause T0 flags — see §3.6, where that fact turns out to be load-bearing for the convention audit.
Scope, stated because the premise states it: one code, one schedule; the depth-6 `(MC)`-emptiness
by-product (`518400 → 25920 → 0`, exhaustive, and re-derived in closed form as `C(6,3)·(3!)⁴` by
the reviewer) is for this code and this monomial-slot family only; depths 7–11 were never scanned.

**What (C4) does *not* deliver, stated plainly:** a second qLDPC code; a qLDPC instance with
`d_X ≠ d_Z` (which is exactly what the W-G1 flag asks a reviewer to probe); an interleaved
(MC)-satisfying schedule for the BB code; any hook-misaligned schedule outside the uniform
`S₄ × S₄` family (instances caveat N2 — no statement of the form "no legal schedule does X" is
licensed); and independent review of the `d = 9` and `d = 7`-standard cells.

### 2.5 (C5) — mechanism attribution with auditable minimum witnesses

**Discharged for a representative of each named family; not delivered for every computed cell.**

The instances claim text carries the attribution obligation with the same four-way mechanism split
the frozen 课题四 asks for. Method: **exclusion by restricted exact optimisation**, not by
sampling. For each cell the same MILP is re-solved under three restrictions — *single-round*,
*no-hook*, *need-meas* — and a restricted optimum **strictly above** `d_R` licenses the
corresponding exclusion, exhaustively over the whole fault model up to the cap `cap = d`, not over
a sample. Cells where the restricted value merely *equals* `d_R` license nothing, and the artifact
bolds only the strict ones. That is the right epistemics for an absence claim and it is what the
route's "auditable" asks for.

| root-clause instance | attribution row exists? | mechanism label |
|---|---|---|
| standard surface (`d = 5`, both sectors) | yes | **single-round bulk**: bare data-qubit string; hooks *not* needed; measurement faults **excluded** (`need-meas > cap`) |
| hook-misaligned surface (`d = 5` class D, `R ≥ 2`, both sectors) | yes | **mixed multi-round, hook-driven, measurement-free**: every minimum witness spans `≥ 2` rounds *and* uses a hook fault, and none uses a measurement fault |
| qLDPC BB `[[18,4,4]]` (both sectors) | yes | **single-round hook/bulk**: hook required, measurement excluded, one round suffices |

Auditable witnesses: an audited minimum witness is exported for **every** reported
`(instance, sector, R)` cell, each passed through an auditor that re-derives, *from the raw fault
locations only*, the flip of every detector `D_{b,r}` for `r = 0..R`, the flip of every observable,
and the count of distinct locations. All report `undetectable = True`, `logical = True`, and a
distinct-location count equal to the claimed weight. The wave-25 reviewer audited two printed
witnesses as genuine and reproduced two exclusion claims by an independent exhaustive route.

**Partial coverage, stated exactly:**

* Table 6.2 has 11 rows, and they are exactly the `(instance, sector, R)` cells whose restricted
  MILPs completed. **Missing:** `d = 7` class D X-sector (not started), `d = 7` standard beyond
  `R = 3`, all of `d = 9`, and the `d = 3` cells. The root clause survives because each named
  family has a completed representative; the *instances* claim's "for each instance" is the wider
  obligation and it is met for every **reported** instance's witnesses but not for every cell's
  **exclusions**.
* The reviewer confirmed attribution "on the cells I re-ran… Not all 11 rows of Table 6.2 were
  re-run" — Table 6.2 was reproduced for `d = 5` class D `R = 1,2,3` (Z) only.
* **The temporal-boundary mechanism is excluded by an argument, not by a computation.** The
  dossier's reasoning is that with ideal initialisation and ideal terminal readout the round-0
  detector `D_{b,0} = m_{b,0}` is absolute and `D_{b,R}` is closed by the readout, so a witness
  cannot start or end for free; the supporting evidence is that every minimum witness found is
  freely translatable in time. **Status of that reading: CONJECTURED**, by the dossier's own label,
  and the absence of a boundary-limited instance is an absence claim over the small scanned
  schedule set. The root's (C5) is discharged as *"attribute the mechanism for these instances"*,
  which is what is delivered; it would **not** be discharged if read as *"prove the boundary
  mechanism is empty in this model"*. §5 residual **G4**.
* The `6.2b` account of *why* `R_stab > 1` happens (hooks buy two steps of the logical string for
  one unit of weight; the per-round record-flip budget caps how many hook shortcuts one round can
  pay for) is labelled by its own author as **an interpretation of computed numbers, not a proof**.
  It is not used anywhere in this assembly.

### 2.6 Lemma A.1 — closing the truncated cells from claim-text material only

**Status: CONJECTURED (proposer-level, this session). Uses only the window premise's certified
claim text.**

*Motivation.* Two reported cells were computed on `R`-windows shorter than `d`: `d = 7` standard
(reached `R ≤ 6`) and `d = 9` class D (reached `R ≤ 7`). The window claim's in-claim decision
procedure is the **fixed** window — "the first `d` distances decide both" — which for `d = 9` wants
`d_1 … d_9`. The strictly better adaptive rule (halt at the first `R` with `R ≥ d_R`, which fires at
`R = 5` on both cells) lives in the window *document*, not in its *claim*, so §0.3 rule 1 forbids
this assembly from using it. The gap is closed by the following, which uses only two clauses of the
window claim: `d_{R+1}(M) ≤ d_R(M)` and `R_stab(M) ≤ d_∞(M)`.

> **Lemma A.1 (one round earlier than the in-claim window).** Let `M` be in the window claim's
> scope. Suppose `d_{R*}(M) = v` for some `R*` with `R* ≥ v − 1`. Then
> ```
>       d_∞(M) = v      and      R_stab(M) = min{ R : d_R(M) = v } .
> ```

*Derivation.* By monotonicity (`d_{R+1} ≤ d_R`, window claim part (i)) the sequence is
non-increasing, so `d_∞ = min_R d_R ≤ d_{R*} = v`. Suppose `d_∞ ≤ v − 1`. By the window claim's
`R_stab ≤ d_∞` we get `R_stab ≤ v − 1 ≤ R*`; by the definition of `R_stab`, `d_R = d_∞` for every
`R ≥ R_stab`, and `R* ≥ R_stab`, so `d_{R*} = d_∞ ≤ v − 1 < v`, contradicting `d_{R*} = v`. Hence
`d_∞ = v`. For the second equality: `R_stab = min{R_0 : d_R = d_∞ ∀ R ≥ R_0}`, and by monotonicity
`d_{R_0} = d_∞` already implies `d_R = d_∞` for all `R ≥ R_0`, so the set is an up-set and its
minimum is `min{R : d_R = v}`. ∎

*Relation to what already exists.* The in-claim fixed rule needs the prefix to reach `R = d`;
Corollary 5.4 (document-level) needs `R* ≥ d_{R*}`; Lemma A.1 needs `R* ≥ d_{R*} − 1`. It is one
round better than the adaptive rule and derived from claim text only. It is **not** a new
mathematical idea — it is Corollary 5.4's pigeonhole read one step tighter — and it is offered as
assembly bookkeeping, not as a result.

*What it closes.* Applying it to the reported prefixes:

| cell | prefix used | `v` | `R*` | `R* ≥ v − 1`? | conclusion |
|---|---|---|---|---|---|
| `d = 7` standard, **Z** | `7,7,7,7,7,7` (`R = 1..6`) | 7 | 6 | `6 ≥ 6` ✔ (tight) | `d_∞^Z = 7`, first-`R`-at-7 `= 1` |
| `d = 7` standard, **X** | `7,7,7,7,7` (`R = 1..5`) | 7 | 5 | `5 ≥ 6` ✘ | **undecided** |
| `d = 9` class D, **Z** | `8,7,6,5,5,5,5` (`R = 1..7`) | 5 | 4 | `4 ≥ 4` ✔ | `(5, 4)` |
| `d = 9` class D, **X** | `8,7,6,5,5,5` (`R = 1..6`) | 5 | 4 | `4 ≥ 4` ✔ | `(5, 4)` |
| every other cell of §2.4 | as tabulated | — | — | ✔ | as tabulated |

So the **truncation** gap on the `d = 9` cell is closed at claim level; what remains on that cell is
the **independent-replication** gap (the wave-25 reviewer confirmed `d_1 = 8` only, and their `R = 2`
run did not finish). Those are two different deficiencies and the instances node caveat, which says
only "remain proposer-level", conflates them. Revision **R7**.

The one cell Lemma A.1 does not reach is `d = 7` standard in the X-sector, and therefore the
`d = 7` standard pair under min-over-sectors. **Cheapest fix: one further MILP cell, `d_6^X`.**
Alternative fix: prove that the standard rotated-surface schedule is self-mirror under the
`𝒜 ↔ ℬ`, `X ↔ Z`, control ↔ target involution, which would transport the Z-sector result; the
instances tables report identical sequences in both sectors for that schedule but do not prove the
symmetry. Residual **G3**.

### 2.7 Discharge summary

| clause | premise(s) | discharge | residual |
|---|---|---|---|
| **C0** model preamble | window (limit exists), all three (model) | **full**, under the verbatim-repetition pin | off-by-one in the root's `R_stab` wording (**R3**); layout pin should be explicit (**R1**) |
| **C1** min-plus representation | transfer | **full at claim level** | evidence-vs-statement scope; T-G3 closed by decision; T-G1/G2/G4/G5 |
| **C2** finite-window theorem | window | **full**, and stronger than the frozen `B(r,d)` request (`B = d`, no `r`) | W-G2 (deciding); W-G1 (load-bearing-with-witness); W-G4 open |
| **C3** algorithm | window (procedure) + transfer (evaluator) | **full at claim level**, via the *fixed* window | adaptive rule is document-level only; no complexity claim (**R6**) |
| **C4a** standard surface | instances | **full** at `d = 3, 5`, reviewed | `d = 7` standard undecided in X-sector (**G3**) |
| **C4b** hook-misaligned surface | instances | **full**, four methods, reviewed | scope is the uniform `S₄ × S₄` family only (N2) |
| **C4c** qLDPC | instances | **full**, three methods, reviewed | one code, one schedule; no `d_X ≠ d_Z` qLDPC (N3) |
| **C5** mechanism attribution | instances | **full for one representative of each named family** | not all cells; boundary-emptiness reading is CONJECTURED (**G4**) |

**Every clause of the root claim is discharged by a CERTIFIED\* premise.** No clause is left
undischarged. What the root inherits is conditionality, not a hole — with the single exception of
the (C0) wording defect, which is a defect in the root's own text rather than in any premise.

---

## 3. Convention-alignment audit

This is the route implication's stated obligation: *"audit that their boundary, schedule-legality,
CSS-sector, and unit-fault conventions agree."* Two further axes are added because the wave-11
through wave-25 record shows convention slips are this campaign's dominant defect class and both of
these have already produced one refutation apiece: **idle compression** (W-G2, which the wave-11
re-adjudication made the deciding conditionality) and the **detector/observable split** (W-G3
refuted as written; T-G3 the transfer review's sharpest gap).

Verdicts are **ALIGNED** / **ALIGNED VIA A BRIDGE** (they agree, but only because some premise
proves they do — the bridge is then itself load-bearing) / **MISMATCH**.

### 3.1 Axis 1 — boundary convention · **ALIGNED**

| premise | statement |
|---|---|
| window | Def 1.7 (ideal init `\|0⟩^{⊗n}` / `\|+⟩^{⊗n}`, ideal transversal readout), Def 1.8 (`m_{b,−1} := 0`, `m_{b,R} := ⊕_{q∈supp(b)} ρ_q`), Def 1.9 (`D_{b,r}` for `r ∈ {0,…,R}` — **full interval, none missing at either end**; `D_{a,r}` for `r ∈ {1,…,R−1}`) |
| transfer | Def 2.6 and Def 2.7, **identical in content and nearly verbatim**, including the parenthetical that `D_{a,0}` does not exist because the round-0 X-outcome is uniformly random |
| instances | (C4): `w = 2` detector window with **both** temporal boundaries, `D_{b,r} = m_{b,r} + m_{b,r−1}` for `r = 0..R` with `m_{b,−1} = 0` and `m_{b,R} = ⊕ρ_q`, plus `D_{a,r}` for `r = 1..R−1`; data initialisation and terminal readout ideal |

Same object, three times. The window theorem flags this convention as *"the theorem's central
hypothesis"* and states that parts (i) and (ii) are **false** without it. The instances review
probed it hostilely and independently confirmed the flag: dropping `D_{b,0}` (unknown-initialisation
reading) or dropping `D_{b,R}` (no terminal closure) collapses `d_R` to **1 for every schedule**.
So the boundary convention is massively load-bearing in absolute terms — and, as the reviewer then
observes, it acts through *identical code* on every schedule, so it cannot manufacture a *difference
between two schedules*, which is what `R_stab > 1` consists of. That is the correct reading and the
assembly adopts it.

**No mismatch.**

### 3.2 Axis 2 — schedule legality, including (MC) · **ALIGNED**

| premise | legality | (MC) |
|---|---|---|
| window | Def 1.3 (one ancilla per check, prepared once, measured once, one CNOT per data qubit in the support, no flags/cat states/repeats/regenerating-set changes) + Def 1.4 (at every step each physical qubit in at most one two-qubit gate) | Def 1.5: `c_{ab}(M) := #{q ∈ supp(a) ∩ supp(b) : t(q→b) < t(a→q)} mod 2 = 0` for all pairs; Standing fact 1.6 proves legality ⟹ deterministic detectors **iff** (MC) |
| transfer | Def 2.3 + Def 2.4, same words | Def 2.5, **same formula character for character**, plus a one-line re-derivation that `c_{ab} + c'_{ab} ≡ 0` by (CSS), hence **(MC) is mirror-symmetric and selects the same schedule class in both sectors** |
| instances | (C3): legal — one two-qubit gate per qubit per step, every required CNOT exactly once, one ancilla per check, no flags/cat states | (C3): measurement-consistent with the **same formula**; both checked at construction time, and every reported schedule carries `legal = True, (MC) = True` in the logs |

The `c_{ab}` formula is identical in all three. The scope clauses match too: window **S1** and
transfer **T1** both quantify over *all* `(Q, M)` with `Q` CSS, `k ≥ 1`, `M` legal and
measurement-consistent — any depth, interleaved or not, graph-like or not, any check weights, and
(T1 makes this explicit, T0 more so) dependent generating sets allowed. Graph-likeness is never
used by either. The instances arm admits only schedules passing exactly this test, and the wave-25
reviewer **rebuilt the legality+(MC) space from the definitions** (`576 → 96 → 16` with member
indices matching, and `518400 → 25920 → 0` for the BB depth-6 family) rather than trusting the
proposer's filter.

**No mismatch.** One note in the assembly's favour: transfer Def 2.5's mirror-symmetry observation
is what lets a single (MC) test serve both sectors, which is silently assumed by the instances
arm's per-sector tables; it is proved, not assumed.

### 3.3 Axis 3 — CSS-sector aggregation · **ALIGNED**, and materially decisive

| premise | statement | epistemic status of the convention |
|---|---|---|
| window | scope **S4**: `d_R(M) := min(d_R^Z, d_R^X)`; everything in §2–§5 proved per sector, §5.3 assembles | **W-G1**, upgraded to **LOAD-BEARING-WITH-WITNESS** by `wg1-witnessed-2026-08-23` |
| transfer | scope **T3**: the identification of 公共定义's `d_circ(C(M))` with `min(d_R^Z, d_R^X)` is *"an inherited convention (the window theorem's W-G1), not a result of this document"*; §3–§7, §9 per sector, §8 assembles | inherited, explicitly |
| instances | **(C1)**: aggregation is min-over-sectors, everywhere, citing both `wg1-witnessed-2026-08-23` and `cor73-sector-flag-2026-08-23`; **every table prints both sectors separately as well as the minimum** | stated per table |

**Three-way agreement, and the cross-node flags are honoured.** The `cor73-sector-flag` event on the
root requires that "the instances arm and the root assembly must state the aggregation convention
explicitly wherever `d_eff` or `d_R` appears" — the instances arm does (C1, and both sectors in
every table); this document does (here, and in every table of §2.4 and §2.6).

**Verification of task item (a): does min-over-sectors save the `d_∞ ≤ d` clause, on the class-B
member with `d^Z = 5`, `d^X = 3`?** Checked, and the honest answer needs two sentences rather than
one.

* The instances arm's own witness is rotated surface `d = 5`, member **[0]** (class B, X-aligned /
  Z-misaligned): `d_R^Z = 5` and `d_R^X = 3` for every `R ≤ 7`. The wave-25 reviewer re-derived it
  independently (`R = 1..5`) and confirmed it.
* **This witness does not itself violate `d_∞ ≤ d` under a per-sector reading**, and the assembly
  should not claim it does: here `d = min(d_X, d_Z) = 5` and both sector values (`5` and `3`) are
  `≤ 5`. What it witnesses is that the two sectors **genuinely separate at the circuit level**, so
  the aggregation convention is not vacuous — the *reported* `d_∞` is `3` under min and would be `5`
  under a Z-sector reading.
* The witness that the `d_∞ ≤ d` clause is **false** under a per-sector reading is the **wave-17
  lift review's** `n = 6` CSS witness (`d_X = 3`, `d_Z = 2`, `d = 2`, graph-like, non-interleaved,
  `d_circ(Z-mem) = 3 > d`), recorded on the window node by `wg1-witnessed-2026-08-23` and on the
  root by `cor73-sector-flag-2026-08-23`. It is **not** in the instances data at all — the surface
  and BB instances all have `d_X = d_Z`, and instances caveat N3 records that a `d_X ≠ d_Z` qLDPC
  instance "was **not** delivered — see §8", flagging this exact hole.

So: **min-over-sectors saves the clause, but the instances arm is not the thing that shows it needs
saving.** The saving witness lives in the lift subtree and reaches this route as a cross-node flag.
That is a legitimate provenance — the flags are recorded with attribution on both nodes — but a
root reviewer should know that the `d_∞ ≤ d` clause's decisive counterexample and the campaign's
computed instance data are **disjoint bodies of evidence**, and that no instance in this route has
`d_X ≠ d_Z`.

**A sharper decisiveness fact the premises state less loudly.** The instances dossier motivates C1
with the `d = 5` class-B member, where the convention changes the reported `d_∞` (`3` vs `5`) but
*not* `R_stab` (`1` either way). At `d = 7` the convention changes **`R_stab` itself**: classes B
and C each have one sector constant at `7` (per-sector `R_stab = 1`) and the other at `5,4,4,4,…`
(class B: Z constant, X reduced; class C: the mirror), so min-over-sectors gives `5,4,4,…` and
**`R_stab = 2`**. Under a single-sector reading the count changes: min-over-sectors gives
`R_stab ≥ 2` for **twelve** of the sixteen legal+(MC) members (classes B, C, D), whereas a Z-only
reading gives it for **eight** (classes C, D) and an X-only reading for eight (classes B, D). So
the convention does not merely relabel a `d_∞`; it decides `R_stab` for four of the sixteen
members either way. The headline itself is aggregation-robust — class D has `R_stab ≥ 2` in **both** sectors
independently at `d = 5, 7, 9` — but the *breadth* of the finding ("twelve of the sixteen") is not.
Worth stating in the instances node caveat; revision **R8**.

**No mismatch.**

### 3.4 Axis 4 — unit-fault model · **ALIGNED VIA A BRIDGE**

| premise | fault locations | weight |
|---|---|---|
| window | Def 1.10: single-qubit Pauli on an ancilla immediately after preparation; any of the 15 non-identity two-qubit Paulis after a CNOT; a single-qubit Pauli on any qubit at any step at which it is not in a two-qubit gate; a classical flip of one recorded outcome. Init and readout ideal. Propagation `F₂`-symplectic; ancilla frames zeroed after each round's measurement | *"Every elementary fault has weight 1; `\|F\|` counts **elementary faults**"* |
| transfer | Def 2.8: **the same taxonomy**, phrased as locations each carrying a group | `\|F\| :=` #{**locations** assigned a non-identity element} |
| instances | (C4): **the same taxonomy**, with "every (qubit, layer) at which the qubit is idle and every ancilla immediately after preparation" spelled out | *"`\|F\|` counts faulty **locations**"* |

The taxonomies agree item for item. The **counting conventions do not agree on their face**: the
window premise minimises a count of elementary faults (a multiset, in which two faults may share a
location), the other two minimise a count of occupied locations. These are a priori different
minima.

**The bridge is transfer Lemma 2.9** (collision handling): the record-flip vector and observable
flip are `F₂`-linear in the assignments, so for any target effect,
`min{|S| : S a multiset of elementary faults with total effect e} = min{|F| : F a configuration
with effect e}` — merge two faults sharing a location into the product, and the weight drops by 1
or 2 while the effect is unchanged. Lemma 2.9 also notes that exact per-round additivity
(`|⊔_r S_r| = Σ_r |S_r|`) needs the location set to be **partitioned by round**, which is scope
clause T2 — i.e. the same clause as W-G2 (§3.5).

**Verdict: ALIGNED, but only because one premise proves it, and the proving premise is not the one
that needs it.** The window premise standing alone carries a latent counting ambiguity that its own
document never resolves; the resolution lives in the transfer document, which the window premise
does not cite (nor could it — the transfer document is later). This is not a mismatch and it moves
no value, but it is a real structural dependency that the route implication does not mention and a
root reviewer should verify: **the three premises agree on `|F|` because of transfer Lemma 2.9.**
Revision **R5** (same sentence as the `window → instances` dependency) should record it.

*Also carried:* transfer caveat 3 — the Y-projection step of the transfer proof needs the **uniform
unit-cost** Pauli fault model of 公共定义; a non-uniform cost model would reopen it. All three
premises use uniform unit cost, so no mismatch arises inside the route; the caveat is about models
outside it.

### 3.5 Axis 5 — idle-layer compression (W-G2 / T2) · **ALIGNED**, plus a provenance finding

This is the axis the wave-11 re-adjudication made the window premise's *deciding* conditionality,
so it gets the closest reading.

**What each premise says.**

* **window**, scope clause **S2**: "verbatim repetition" is used with force — the fault locations of
  round `r` are in `R`-independent bijection with those of round `r'`. It *"**fails** if a compiler
  merges the tail of round `r` with the head of round `r+1` (cross-round idle-layer compression),
  which is therefore outside the scope; the 公共定义's instruction to compress meaningless idle
  layers is read as **within-round** compression, applied once to `M` before `C_R(M)` is formed."*
  §8's **W-G2** repeats this and adds the honest sentence: a reviewer who reads the compression
  instruction as applying to the concatenated circuit *"will find (i)–(iii) unproved for that
  layout."*
* **transfer**, scope clause **T2**: verbatim the same, including *"fails for cross-round idle-layer
  compression, which is out of scope"*, and **T-G1** names it *"this is the window theorem's W-G2,
  inherited verbatim."*
* **instances**, convention **(C2)**: stated per instance — rotated-surface uniform family `T = 4`,
  **zero** layers with no CNOT at all; BB `[[18,4,4]]` schedule NI `T = 12`, **zero** layers with no
  CNOT at all (each carries 9 CNOTs). *"No instance in this document contains a globally idle layer,
  so the compression clause is satisfied without any reduction step."* Individual qubits idling
  inside a layer are fault locations and are included in every method.

**Verdict: the three premises adopt the same reading and are mutually consistent.** The instances
arm's check ("no globally idle layer") is exactly the *within-round* compression test that S2/T2
specify, applied to `M` before `C_R(M)` is formed. **No mismatch.**

Three things a root reviewer needs on top of that, and only the first is comfortable.

**(i) Provenance finding — "公共定义 line 58" is a misattribution, and it cuts in the assembly's
favour.** All three premises, and the wave-11 re-adjudication, cite the idle-compression instruction
as **公共定义 line 58** (window S2 and W-G2; transfer T-G1; instances C2 quotes it as
`公共定义 line 58: "无意义的空闲层应当压缩掉"`; the window node's caveat 1 says *"公共定义 line 58
itself imposes idle-layer compression"*). Checked against the frozen bytes
(`CIRCDIST_PROBLEMS.md`, `5f6dc37f…`): the 公共定义 block is **lines 14–41**. **Line 58 sits inside
课题一** (the Gross-code problem), as the last bullet of the list defining `S_Gross`, the admissible
schedule set *for that problem*. **课题四 (lines 185–233) contains no idle-compression clause at
all**, and the rescope note `SAT_RESCOPE_20260822.md`, which is the root's governing text, does not
introduce one.

Consequences, stated carefully because this is a finding that *weakens a caveat*, which is the
direction that deserves the most suspicion:

* It does **not** dissolve W-G2. W-G2 is a scope condition on the *window claim's own universal
  quantifier* ("every fixed legal schedule"), and that quantifier is the window premise's to
  defend regardless of where the compression instruction lives.
* It **does** bear on how severely the **root** inherits W-G2. The root claim's own words are
  *"the circuit distance after `R` repeated rounds"*. "Repeated rounds" is the verbatim-repetition
  layout — it is the reading S2/T2 adopt, the reading `C_R(M)` denotes in all three premises, and
  the reading the frozen 课题四 uses (*"将同一轮 `M` 重复 `R` 次"* — repeat the **same round** `R`
  times). No frozen text applicable to question 4 asks for cross-round compression. So the root's
  `d_R` is the verbatim-repetition `d_R`, W-G2's excluded layout is a *different model* rather than
  an unproved case of the root's own model, and the root inherits W-G2 as a **scope pin** rather
  than as an unproved case of its own quantifier.
* **This is a lead question, not a proposer decision.** The wave-11 adjudication kept the window
  node at CERTIFIED\* on four independently sufficient grounds, of which W-G2 was only the first;
  grounds (2), (3) and (4) (frontier task-001 and task-002 still owed; no single hash-bound review
  has attacked the assembled claim) are untouched by anything here. **Nothing in this finding
  licenses a level change on the window node**, and this document proposes none. Revision **R9**
  proposes only that the three premises' caveat texts cite the clause by its true location, and
  that the lead rule on whether question 4 inherits 课题一's compression bullet at all.

**(ii) The qLDPC `T = 12` schedule is where the excluded reading would bite hardest — and where the
exclusion is best justified.** The BB schedule NI is a two-block layout: X-check CNOTs in layers
0–5, Z-check CNOTs in layers 6–11, `T = 12`. With 36 qubits (18 data, 9 X-ancillas, 9 Z-ancillas)
and 108 CNOTs, a density bound puts the minimum conceivable depth at 6, so `T = 12` is **twice the
density-minimal depth**, and every data qubit idles in 3 of the 6 layers of each block. It is
precisely the layout a compiler applying a compression instruction to the *concatenated* circuit
would attack, by pulling round `r+1`'s X-CNOTs into round `r`'s Z-block.

Two facts make the exclusion defensible rather than convenient, and both should be in the record:

* *Within* the scanned family, `T = 12` is not slack that (C2) is ignoring: **all 25 920 legal
  depth-6 monomial-slot schedules for this code fail (MC)**, exhaustively, and the wave-25 reviewer
  reproduced that exhaustively *and* re-derived it in closed form as `C(6,3)·(3!)⁴`. Depth 6 is
  empty, not merely unexplored.
* Cross-round compression of a **non-interleaved** schedule necessarily *interleaves* it: moving a
  round-`r+1` X-CNOT before a round-`r` Z-CNOT on a shared data qubit changes `c_{ab}` across the
  boundary. The compressed circuit is therefore a **different schedule**, generally with different
  (MC) status — not the same circuit written more tightly. That is a positive argument for S2's
  within-round reading on this instance, not merely a scope disclaimer.

*Honest limit of both:* depths **7 through 11** for this code were never scanned (instances caveat
N3), so *"`T = 12` is the compressed depth for BB `[[18,4,4]]`"* is **not** established. What is
established is (C2) as verified — no globally idle layer — which is weaker. §5 residual **G5**.

**(iii) Compression is material, and that is why (i) and (ii) are not hand-waving.** The wave-11
adjudicator's own enumeration: compressing a depth-7 `[[4,2,2]]` layout takes the search space from
176 to 44, and depth-8 from 769 to 34. Idle locations are fault locations; removing them removes
fault paths and can move `d_R`. Any future document that adopts the concatenated-circuit reading is
computing a different number, and must say so.

### 3.6 Axis 6 (added) — the detector/observable split · **ALIGNED VIA A BRIDGE**, load-bearing on the qLDPC arm

Not named in the route implication, added because it produced one refutation on each of two nodes
(window W-G3 refuted as written; transfer T-G3, the transfer review's sharpest gap) and because
`d_circ` is a *function of* this choice.

| premise | detector space used | status |
|---|---|---|
| window | Def 1.9's set, with scope **S3**; the original S3 (*"enlarging the detector set can only decrease `d_circ`"*) was **struck by the review**; **S3′** installed by Amendment 1 and reproduced 18/18 by an independent CHP-simulator method | **S3′ load-bearing** (window caveat 2) |
| transfer | **Definition 3.5** — a deterministic parity is a detector iff its value is the same for every prepared logical basis state — **ratified by the lead** as the intended reading of 公共定义; Prop 3.6 gives `𝒟_Z = span{D_{b,r}}` (**equality**) and `span{D_{a,r}} ⊆ 𝒟_X` with codimension `dim leftker(H_X)` | **T-G3 closed by decision, not derivation** (transfer caveat 1); corrected safe condition `span{D_{b,r}} ⊆ 𝒟' ⊆ 𝒟` |
| instances | Def-2.7's set, explicitly (C4) | inherits |

**The bridge is transfer Proposition 3.7**: `d_R^Z` computed against the canonical `𝒟` of Def 3.5
**equals** `d_R^Z` computed against the Def-2.7 set. Without it, the instances arm computes against
one detector space while the transfer theorem is stated against another, and the two are known to
differ in general — the T-G3 counterexample (Steane + a redundant X-check) gives `d^{2.7} = 2`
against `d^{𝒟'} = 3` at `R = 2` and `4` at `R = 3`, with the dimension quintuple `28/22/21/12/20`
confirmed by the wave-15 re-reviewer using a propagator sharing no code with the document. The
counterexample's `𝒟'` is not contained in `𝒟` (it absorbs an observable direction), which is exactly
why the withdrawn mitigation ("any `𝒟` between Def-2.7 and `V`") was refuted and the installed
condition is containment in `𝒟`, not in `V`.

**Prop 3.7 is not in the transfer premise's claim text.** Under §0.3 rule 1 the assembly must
therefore mark this step **proposer-level**: the claim-level alignment of the instances arm's
detector convention with the ratified canonical split rests on a numbered result inside the transfer
document, cleared by its reviews but not named in its claim. Flagged rather than laundered.

**This bridge is load-bearing on the qLDPC arm, not decorative.** I verified independently this
session (§8.2) that BB `[[18,4,4]]` has 9 X-checks of rank 7, so `dim leftker(H_X) = 2`: the Def-2.7
detector set **omits a genuine 2-dimensional space of redundancy parities** `⊕_{a∈T} m_{a,0}`, which
are deterministic even though each `m_{a,0}` is individually uniform. Prop 3.6 says exactly this and
Prop 3.7 says exactly why it does not move `d_R^Z` (the sector-decoupled witness flips no X-check
record at all, so it annihilates those directions too). Two further independent supports:

* the instances review's hostile probe 1 — **adding** the omitted `D_{a,0}` to the surface instances
  left `d_R` unchanged at `4, 3, 3`;
* the review's qLDPC verdict — the BB arm is *"robust to the omitted redundancy detectors"*.

**No mismatch, and the alignment is checked three ways.** But note the asymmetry the transfer
document itself flags and that a root reviewer should re-check: the Z-side has no analogous hole
(the absolute round-0 detector `D_{b,0}` puts every Z-side redundancy parity into the Def-2.7 span
automatically), so the whole subtlety sits on the X-side, which is exactly the side the surface
instances cannot exercise because their generating sets are independent.

### 3.7 Findings of the convention audit

| # | axis | finding | severity |
|---|---|---|---|
| **F1** | boundary | three-way verbatim agreement; hostile probes confirm the convention is absolutely load-bearing but cannot manufacture a between-schedule difference | none (clean) |
| **F2** | legality + (MC) | identical `c_{ab}` formula and identical scope quantifiers in all three; the (MC) space was rebuilt from the definitions by the reviewer | none (clean) |
| **F3** | sector aggregation | aligned; the instances arm's stated witness shows sector **separation**, not a `d_∞ ≤ d` violation — the violating witness lives in the lift subtree and no instance in this route has `d_X ≠ d_Z`; and at `d = 7` the convention changes a reported **`R_stab`**, not merely a `d_∞` | **note + R8** |
| **F4** | unit fault | aligned **only via transfer Lemma 2.9**, which reconciles the window premise's "count elementary faults" with the other two premises' "count occupied locations"; the reconciling lemma lives outside the premise that needs it | **structural, R5** |
| **F5** | idle compression | three-way aligned on the within-round reading; but the clause is cited by all three as "公共定义 line 58" and line 58 is in **课题一**, not the 公共定义 block, and 课题四 has no compression clause — which bears on how severely the **root** inherits W-G2 | **provenance, R9; lead question** |
| **F6** | detector/observable split | aligned **only via transfer Prop 3.7**, which is not in the transfer claim text (marked proposer-level); load-bearing on the qLDPC arm, where `dim leftker(H_X) = 2` (verified this session) | **structural, proposer-level step** |

**No axis is a mismatch.** Two (F4, F6) are alignments that hold *because a premise proves them*,
and in both cases the proving premise is the transfer node — which is otherwise the premise the
route leans on least. That is the audit's main structural result: **the transfer premise is
load-bearing for the route's convention coherence even though no reported instance number depends on
Theorem T.** A reviewer tempted to treat `transfer` as the detachable third premise should not.

---

## 4. The assembled caveat set

### 4.1 The ceiling

All three premises are `CERTIFIED*`. A parent cannot outrank its weakest premise, so **the root's
ceiling on this route is `CERTIFIED*`** — an independently reviewed conditional result with explicit
unresolved premises or scope caveats. `PROVED` is not reachable on this route while any premise is
starred, and independently of that, the wave-25 reviewer refused `PROVED` for `instances` on
grounds that apply verbatim to the root: this is in part an outcome whose content is computation,
and 公共定义 states that numerical simulation never substitutes for proof.

### 4.2 Composition

The three premises carry **15** caveats (transfer 6, window 4, instances 5). They compose into
**11** root caveats: **3 absorbed**, **4 cross-cutting merges** (one premise caveat splits across
two of them), and **1 newly named** by this assembly because no single premise lists it.

**Absorbed — they do not surface at the root:**

| # | premise caveat | why absorbed |
|---|---|---|
| **A1** | instances **(W)** — "the `R_stab`/`d_∞` readings import the window theorem, itself CERTIFIED\*" | **route-internal.** The root already carries `window` as a premise, so this is not an extra external conditionality; it becomes the structural note of §0.4 (the route is not a flat conjunction) rather than a caveat. Recorded, not double-counted. |
| **A2** | instances — "the fitted law `d_R = max(d − R, (d+1)/2)`, `R_stab = (d−1)/2` stays CONJECTURED" | **out of claim.** §1.3 confirms the law is not part of the root claim. It composes as an explicit **exclusion**: the root neither asserts nor needs it. |
| **A3** | window — "W-OPEN answered positively at REVIEWED level (wave 24/25)" | **status note, not a limitation.** It records that the window premise's sharpest open sub-question was settled *by the instances premise*, and that the window theorem survived its first nontrivial stress test (`R_stab ≤ d_∞ ≤ d` on every computed cell). Composes as supporting evidence. |

**Cross-cutting — one convention, several names, merged:**

| # | root caveat | composed from |
|---|---|---|
| **R-C1** | **The shared frozen-model design is a single point of failure.** All three premises restate the *same* 公共定义 model and none re-derives it: transfer **T-G1** says so explicitly ("not re-derived here; imported"), the window's Definitions 1.1–1.12 are that model, and the instances arm's C1–C4 restate them again. A single misreading of 公共定义 invalidates all three premises simultaneously, and no amount of cross-checking between them would detect it. | *newly named by this assembly* (transfer T-G1 is the closest existing text) |
| **R-C2** | **Aggregation is min-over-sectors**, load-bearing-with-witness; the `d_∞ ≤ d` clause is false per-sector; decisive for a reported `R_stab` at `d = 7`; no instance in this route has `d_X ≠ d_Z`. | window caveat 2 (W-G1 part) + transfer T3 + instances C1 + the two cross-node flags |
| **R-C3** | **The layout is verbatim repetition**; cross-round idle compression is a different model and is out of scope; the frozen provenance of the compression instruction is 课题一, not 公共定义 (§3.5(i)). | window caveat 1 (W-G2) + transfer T-G1's T2 clause + instances C2 |
| **R-C4** | **The detector/observable split is fixed by decision, not derivation**: Def 3.5 ratified by the lead; corrected safe condition `span{D_{b,r}} ⊆ 𝒟' ⊆ 𝒟` (containment in `𝒟`, **not** in `V`); the instances arm's Def-2.7 set is reconciled to it by transfer Prop 3.7, a step this assembly marks proposer-level; S3′ load-bearing; W-G3 must **not** be carried. | transfer caveat 1 + window caveat 2 (S3′ part) + instances C4 |

**Composing singly:**

| # | root caveat | from |
|---|---|---|
| **R-C5** | **Transfer evidence scope ≠ statement scope.** Theorem T is stated for all legal single-round single-ancilla CSS schedules; the transfer *document's* evidence is `d = 3, k = 1, R ≤ 3` (plus one `k = 2` fault-dictionary instance), no qLDPC. The general case rests on the reviewed derivations. Partially relieved — **as corroboration only** — by the instances arm's independent agreement at `d = 5` (16 schedules) and on BB `[[18,4,4]]` (`k = 4`, dependent generators). | transfer caveat 4 |
| **R-C6** | **Transfer open minors:** T-G2 (is `Σ` Nerode-minimal? — changes object size, not values), T-G4 (constructing `A` is exponential; no NP-hardness asserted; the Vardy / Kapshikar–Kundu citations are flagged unverified), T-G5 (finiteness needs two weight-1 mechanisms), and the Y-projection's dependence on the **uniform unit-cost** Pauli model. | transfer caveats 2 and 3 |
| **R-C7** | **External assumption A1** — BCOQ Thm 3.112 (min-plus eventual periodicity), cited as published, not independently re-derived. | transfer caveat 6 |
| **R-C8** | **W-G4 open** — is `R_stab ≤ d_∞` tight? Gains data from the instances arm (observed ratio `(d−1)/(d+1) → 1`), gains no closure; tightness is asymptotic **iff** the conjectured law holds, and the law is the conjectured part. | window caveat 3 |
| **R-C9** | **Instance schedule-space scope (N2/N3):** the hook-misaligned family is the uniform `S₄ × S₄` space only (`576 → 96 → 16`); no "no legal schedule does X" statement is licensed; the qLDPC arm is one code, one schedule, with depths 7–11 unscanned and no `d_X ≠ d_Z` instance. | instances caveats 2 and (N3, via the dossier) |
| **R-C10** | **Two reported cells are proposer-level for replication:** `d = 9` (`R_stab = 4`) and `d = 7` standard — the wave-25 reviewer re-ran `d = 5` fully by three methods, `d = 7` misaligned, and the qLDPC arm, but confirmed only `d_1 = 8` at `d = 9` and did not check `d = 7` standard. (Their *truncation* is separately closed by Lemma A.1, §2.6, except `d = 7` standard X-sector.) Neither cell is load-bearing for any root clause. | instances caveat 3 |
| **R-C11** | **Document hygiene, all safe-direction, none moving a value:** the transfer proof's §11.4 program digest is superseded by Amendment 1's repaired program (the original defective program hashes to the document's own declared digest, so the defect was in the published code, not in transcription); the instances errata (78 → 77 one-round effect classes; the §2 "classes" column is the sector-reduced count; the §0 node hash is stale). | transfer caveat 5 + instances caveat 5 |

### 4.3 What the root's conditionality amounts to, in one paragraph

Conditional on: the frozen 公共定义 model being read as all three premises read it (**R-C1**); the
aggregation being min-over-sectors (**R-C2**); `C_R(M)` being `R` verbatim repetitions of `M`
(**R-C3**); the detector/observable split being the lead-ratified Definition 3.5, with the
instances arm's Def-2.7 computations reconciled to it by transfer Prop 3.7 (**R-C4**); and one
published external theorem (**R-C7**) — the root claim's eight clauses are each discharged by a
`CERTIFIED*` premise. The generality of clause (C1) rests on reviewed derivations rather than on
evidence at the stated scope (**R-C5**); four transfer minors and one window question remain open
without touching any value (**R-C6**, **R-C8**); the instance clauses are discharged inside stated
schedule-space scopes (**R-C9**) with two non-load-bearing cells at proposer level (**R-C10**); and
three documentation defects are recorded (**R-C11**). The fitted growth law and the "`R_stab`
unbounded" reading are **not** part of the claim and are not used (**A2**).

---

## 5. Honest gaps, and the revision sheet for the lead

### 5.1 Residual gaps — root-claim clauses no premise fully discharges

| # | gap | which clause | severity | cheapest close |
|---|---|---|---|---|
| **G1** | **The root's `R_stab` definition is off by one** against the definition every premise uses and every certified result is about. | **C0** | **wording, but on the campaign's headline number** | adopt **R3** |
| **G2** | The route implication says the three premises "together establish" the claim, without recording that **instances imports window** (so a window defect is a double hit) or that the **unit-fault counting conventions agree only via transfer Lemma 2.9**. | route text | structural | adopt **R5** |
| **G3** | **`d = 7` standard is undecided in the X-sector** (computed `R ≤ 5`; Lemma A.1 needs `R* ≥ 6`), hence undecided under min-over-sectors. Does **not** touch (C4a), which is discharged at `d = 3, 5`. | bonus cell | low | one MILP cell `d_6^X`; or prove the standard schedule is self-mirror |
| **G4** | **Mechanism-attribution completeness.** The root's (C5) is discharged for one representative of each named family. Not discharged: exclusions for all 11 Table-6.2 cells (X-sector `d = 7` class D never started; `d = 7` standard beyond `R = 3`; all of `d = 9`; all of `d = 3`), and the **temporal-boundary emptiness** reading, which the dossier itself labels **CONJECTURED**. | **C5** | low for (C5) as written; **would be high** if (C5) were read as "prove the boundary mechanism is empty" | state the reading in the claim (**R10**), or run the missing restricted MILPs |
| **G5** | **"`T = 12` is the compressed depth for BB `[[18,4,4]]`" is not established** — depth 6 is exhaustively (MC)-empty, but depths 7–11 were never scanned. What is verified is only "no globally idle layer". | **C4c**, via R-C3 | low | scan depths 7–11, or state the weaker verified property in the caveat |
| **G6** | **The `d_∞ ≤ d` clause's decisive counterexample and this route's instance data are disjoint bodies of evidence**; no instance in the route has `d_X ≠ d_Z`, which is exactly what the W-G1 flag asks a reviewer to probe. | **C2/C4c** | medium for a *reviewer*, low for the *claim* | deliver a hypergraph-product qLDPC instance with `d_X ≠ d_Z` (already instances frontier work) |
| **G7** | **Neither the transfer nor the window premise has had a hash-bound review that attacked its assembled claim end to end.** For window this is the wave-11 adjudication's grounds (3)–(4) and its live frontier task-001/task-002; for transfer, the clearing review was a *focused* re-review of Amendment 1. | C1, C2 | this is what keeps both at CERTIFIED\* | window frontier task-001 + task-002; it is not this assembly's to close |

**Explicit confirmations requested in the brief:**

* **The fitted law is NOT part of the claim** — confirmed by inspection of the verbatim root text
  (§1.3). It composes as absorbed item **A2**.
* **"Two independent methods where feasible" is NOT part of the root claim** — confirmed; it is a
  clause of the instances premise's claim. Where it matters is *within* that premise, and the
  honest statement there is: two-or-more methods ran on every cell that carries a root clause
  (`d = 3, 5` standard: T, S; `d = 5` class D: T, S, M, B; BB: T, S, M / T, S), while the cells
  with a single method are exactly the two non-load-bearing ones (`d = 9`: MILP, with stim only to
  `R ≤ 3`; `d = 7` standard X-sector beyond stim's reach). "Where feasible" is honestly used:
  method **T** is *infeasible* at `d = 7` (`|Σ| = 2^{25}`, dictionary index space `2^{49}`) and the
  dossier records that as a limit rather than working around it.

### 5.2 Revision sheet (lead approval required; R1–R3 change the root claim hash)

Precedent: the `CIRCDIST.lift` root assembly's §7 sheet, and the lead's ratification pattern on
transfer T-G3.

| # | target | proposed change | why | class |
|---|---|---|---|---|
| **R1** | root claim | "…the circuit distance after `R` repeated rounds" → "…after **`R` verbatim repetitions of `M`**" | pins the layout convention all three premises assume (R-C3 / W-G2 / T2); the frozen 课题四's own words are 将同一轮 `M` 重复 `R` 次 | wording |
| **R2** | root claim | after "let `d_R(M)` be the circuit distance", insert "**taken as the minimum over the two CSS memory sectors**" | the aggregation is load-bearing-with-witness and decisive for a reported `R_stab` (§3.3); the root is currently silent while all three premises fix it | wording |
| **R3** | root claim | "`R_stab(M)` the first round after which the sequence is identically `d_∞(M)`" → "`R_stab(M) := min{R_0 : d_R(M) = d_∞(M)` for all `R ≥ R_0}`" | **off by one** against every premise and every certified number (§2.0); returns `1` where the premises return `2` on the headline cell | wording, **defect repair** |
| **R4** | transfer node caveat 4 | append: "Independent corroboration of Theorem T now also covers `d = 5` (16 legal+(MC) uniform schedules, both sectors) and BB `[[18,4,4]]` (`k = 4`, dependent generating sets, `T = 12`), via `CIRCDIST.sat.instances`; this widens the *corroboration* scope, not the *proof* scope." | the caveat's parenthetical "no qLDPC instance" predates the instances arm and now understates the evidence | accuracy |
| **R5** | route implication (`asymptotic-stability-assembly`) | add: "The premises are not independent: `instances` imports `window`'s window theorem for every statement outside its computed windows, and the three unit-fault counting conventions are reconciled by transfer Lemma 2.9. A defect in `window` propagates to two premises; the transfer premise is load-bearing for convention coherence even though no reported instance value depends on Theorem T." | §0.4, F4, F6 | structural |
| **R6** | root claim **or** root assessment | record that "algorithm" means terminating-with-correctness, not efficient; building `A` is exponential (T-G4) and **no** hardness claim is made | prevents a complexity claim being read in | clarification |
| **R7** | instances node caveat 3 | split "remain proposer-level" into its two distinct deficiencies: **(a)** truncation of the computed window — now closed for `d = 9` by Lemma A.1 (§2.6), still open for `d = 7` standard X-sector; **(b)** independent replication — open for both cells | the node conflates them; only (b) survives for `d = 9` | accuracy |
| **R8** | instances node caveat / dossier C1 | record that at `d = 7` the aggregation convention changes a reported **`R_stab`**, not merely a `d_∞` as the `d = 5` class-B motivation suggests: min-over-sectors gives `R_stab ≥ 2` for twelve of the sixteen legal+(MC) members, a single-sector reading for eight (class B is reduced in X only, class C in Z only) | strengthens the stated justification for C1 | accuracy |
| **R9** | window caveat 1, transfer T-G1, instances C2 | cite the idle-compression instruction by its true location — **课题一's `S_Gross` bullet (line 58)**, not 公共定义 (lines 14–41) — and **ask the lead to rule** whether question 4 inherits it at all | §3.5(i); currently a shared misattribution across three nodes and one adjudication | provenance; **lead question** |
| **R10** | root claim **or** instances claim | state that mechanism attribution is *"for each reported instance"*, and that the emptiness of the temporal-boundary mechanism is an **interpretation of computed witnesses (CONJECTURED)**, not a proved exclusion | (C5) is discharged under the first reading and not under the second (§2.5, G4) | clarification |

**R1–R3 change the root claim hash** (currently `sha256:5f6e79d8…4372e007`). Adopting them now costs
nothing, because the root carries no hash-bound review yet; adopting them *after* this assembly is
reviewed would lapse that review. **The cheap ordering is: lead rules on R1–R3, then the assembly
review is commissioned against the revised claim.**

### 5.3 What this document does *not* propose

Per the brief and per §0.3: **no level change is proposed here.** The route may rise to
`CONJECTURED`-with-complete-blueprint or to `NUMERICAL` pending the assembly review, and the root
node's ceiling on this route is `CERTIFIED*` (§4.1) — but the promotion gate is the **independent
review of this assembly**, in the next wave, and that review's verdict is not this session's to
anticipate. Nothing above licenses a level change on any of the three premises either; in
particular §3.5(i) is a provenance finding and a lead question, and the wave-11 adjudication's
grounds (2)–(4) for holding `window` at `CERTIFIED*` are untouched by it.

---

## 6. Checklist for the completion review of the root

A reviewer of this assembly should attack, in this order:

1. **Re-verify the three claim hashes** (§0.2, code in §8.1) against the node bytes at review time.
   If any has drifted, the composition is void until re-derived — the premises' clearing reviews
   bind to the claim text, not to the node.
2. **Attack Lemma A.1** (§2.6). It is the one new mathematical step in this document, it is
   proposer-level, and two reported cells rest on it. Check in particular that it uses **only** the
   window premise's claim text (`d_{R+1} ≤ d_R` and `R_stab ≤ d_∞`) and not Corollary 5.4.
3. **Attack the clause split** (§1.2). Splitting is interpretive; a different split could hide an
   undischarged obligation. In particular test whether (C5) can be read as demanding a *proved*
   exclusion of the temporal-boundary mechanism (G4) and whether (C3) can be read as demanding
   efficiency (R6).
4. **Re-run the convention audit independently** (§3), especially the two bridges: transfer
   Lemma 2.9 (fault counting, F4) and transfer Prop 3.7 (detector convention, F6). Both are
   alignments that *hold because a premise proves them*; if either proof fails, two premises stop
   describing the same object.
5. **Check §3.5(i) against the frozen bytes yourself.** It is a finding that weakens a caveat,
   which is the direction most in need of adversarial reading. `CIRCDIST_PROBLEMS.md` is
   `5f6dc37f…`; the 公共定义 block is lines 14–41; line 58 is the last bullet of 课题一's `S_Gross`
   list; 课题四 is lines 185–233.
6. **Probe the `d_X ≠ d_Z` hole** (G6). No instance in this route has it, and it is exactly what
   the W-G1 flag asks for. A qLDPC instance with `d_X ≠ d_Z` is the single most informative missing
   computation for the root.
7. **Verify the caveat composition** (§4.2) is neither lossy nor inflationary: check the three
   absorptions in particular, since absorbing a caveat is how conditionality goes missing.
8. **Do not accept the fitted law, "`R_stab` unbounded", or the `6.2b` mechanism story anywhere in
   the discharge.** None is used above; verify that.

---

## 7. One paragraph for the node

The revised fourth question's root claim splits into eight clauses, and each is discharged by one of
three `CERTIFIED*` premises whose claim hashes were recomputed and matched this session: the
transfer premise supplies the finite-state min-plus representation `d_R = u ⊙ A^{⊙R} ⊙ v` with both
CSS sectors, boundary vectors and terminal condition represented exactly; the window premise supplies
monotonicity, the existence of `d_∞`, contiguity, and the explicit window `B = d` with no dependence
on the cross-round state-space dimension, together with the in-claim decision procedure "the first
`d` distances decide both"; and the instances premise supplies the three named pairs — standard
rotated surface `(d, 1)` at `d = 3, 5`, a **legal, (MC)-satisfying, deliberately hook-misaligned**
surface schedule with `(3, 2)` at `d = 5` by four independent methods (the first `R_stab > 1` in the
campaign, refuting single-round dominance by construction), and bivariate-bicycle `[[18,4,4]]` under
a `T = 12` non-interleaved schedule with `(3, 1)` — each with audited minimum witnesses and
mechanism labels established by exhaustive restricted exact optimisation rather than by sampling.
The six-axis convention audit finds **no mismatch**: boundary, legality-with-(MC), and
min-over-sectors aggregation are verbatim-identical across the three premises, and idle compression
is read the same way by all three; the two remaining axes align **via bridges the transfer premise
proves** (Lemma 2.9 reconciles fault counting; Proposition 3.7 reconciles the instances arm's
Definition-2.7 detector set with the lead-ratified canonical split), which makes the transfer premise
load-bearing for the route's coherence even though no reported instance value depends on Theorem T.
Fifteen premise caveats compose into eleven root caveats with three absorbed; the root's ceiling on
this route is `CERTIFIED*`. Three things are owed to the lead: the root's own `R_stab` definition is
**off by one** against the definition every certified result uses; the route implication does not
record that `instances` imports `window`; and the idle-compression clause that W-G2 is about is cited
by three nodes as 公共定义 line 58 when line 58 is in 课题一 and 课题四 has no such clause — a
provenance question that bears on how severely the root inherits W-G2 and that only the lead can
settle.

---

## 8. Reproduction

Two computations were run this session. Both are **NUMERICAL** and neither is load-bearing for any
discharge above except where cited.

### 8.1 Claim-hash verification (§0.2)

```python
import yaml, hashlib, pathlib
def ch(c):                                      # tools/proof_dag_v6.py::claim_hash
    return 'sha256:' + hashlib.sha256(c.replace('\r\n','\n').strip().encode('utf-8')).hexdigest()
base = pathlib.Path('research/circdist/proof-dag/nodes')
expect = {
 'CIRCDIST.sat.transfer':  'sha256:eb50730d33e716c13be3d46fa92afab98a9e223aa2ac46aff960a9fcd9896ca5',
 'CIRCDIST.sat.window':    'sha256:8698b051b15fa14ff669299580d9b7bfec01808c0a34133ef09264e749466146',
 'CIRCDIST.sat.instances': 'sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3',
}
for nid in ['CIRCDIST.sat'] + list(expect):
    d = yaml.safe_load((base / (nid + '.yaml')).read_text())
    print(nid, ch(d['claim']), 'MATCH' if expect.get(nid) == ch(d['claim']) else 'root/mismatch')
```

Output: three `MATCH`, and the root at `sha256:5f6e79d8b5c1f08b…4372e007`.

### 8.2 Independent re-derivation of the qLDPC code parameters (§2.4, §3.6)

Built `A = 1 + y + x`, `B = 1 + y + x²y` as `3×3`-bicirculants over `F₂` (`l = m = 3`,
`n = 2lm = 18`), `H_X = [A|B]`, `H_Z = [Bᵀ|Aᵀ]`; verified `H_X H_Zᵀ = 0`; computed ranks by
Gauss–Jordan over `F₂`; computed `d_X`, `d_Z` by exhausting `ker H_Z` and `ker H_X` (`2^{11}` each)
against `rowsp H_X`, `rowsp H_Z`. No code from the instances arm was read or reused.

```text
CSS commute HX HZ^T == 0 : True
n 18   rank HX 7   rank HZ 7   k 4
check weights HX [6]  HZ [6]        qubit degrees HX [3]  HZ [3]
dX 4   dZ 4   d 4
dim leftker(HX) 2     dim leftker(HZ) 2
```

This reproduces the instances dossier's `[[18,4,4]]`, "9 checks of rank 7", weight-6 checks and
degree-3 qubits exactly. The line the audit uses is the last one: `dim leftker(H_X) = 2 ≠ 0`, so the
Definition-2.7 detector set genuinely omits a 2-dimensional space of redundancy parities on this
instance, and transfer Proposition 3.6/3.7 is load-bearing there rather than vacuous (§3.6).

*What this does not check:* the BB schedule NI, its legality/(MC), any `d_R`, or any value in
Table 5.3. Those were re-verified by the wave-25 reviewer, not by me.
