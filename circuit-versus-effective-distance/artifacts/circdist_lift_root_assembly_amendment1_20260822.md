# Amendment 1 to `circdist_lift_root_assembly_20260822.md`

**Node:** `CIRCDIST.lift` (root) · **Date:** 2026-08-22 · **Role:** Opus 5 executor, amendment
author applying the repairs registered by the independent root review. **Box:** one session,
stop-loss binding. No sub-agents. No Lean. No proof-DAG object touched. This file is
**append-only** and changes no prior artifact.

**What this amendment is.** The independent review
`artifacts/circdist_lift_root_review_20260822.md` returned **FURTHER-REPAIR** on three itemized
points (F1, F2, F3), refuted nothing, and amended two entries of the assembly's own revision sheet
(R4, R6). This file applies exactly those repairs, in the reviewer's scope, with before/after text
for each, and re-verifies locally every computation the repairs rest on. **On the points below,
this amendment governs the assembly; everywhere else the assembly stands unchanged.**

**Epistemic ceiling (binding on every line).** Nothing here is labelled PROVED or `CERTIFIED*`.
The assembly argument remains **CONJECTURED**; the computations of §5 are **NUMERICAL** with their
code inline. This session is an amendment author, not a reviewer, and cannot grant a completion
level. The three children's `CERTIFIED*` levels are read off the canonical node records and are
neither re-certified nor re-reviewed here. The review that commissioned these repairs is treated as
**data in a file**, not as certification of anything.

---

## 0. Hash chain

### 0.1 Amended predecessor and commissioning review

```text
amended predecessor
  artifacts/circdist_lift_root_assembly_20260822.md
  SHA-256  275a8c2cdce003277abe9e0e6dfed057f4f91cd00238fc9805ff360c58a8aa46
  size     59855 bytes, 930 lines

commissioning review (data, not certification)
  artifacts/circdist_lift_root_review_20260822.md
  SHA-256  a6fbf42e5f1f65c7c3c2731185dcbcd898e74b919bda4fdc85bde39e98a93b7c
  size     34013 bytes, 497 lines
```

If either hash fails to reproduce, this amendment is void until re-derived against the changed
input.

### 0.2 Claim-hash binding of the four nodes (this is the trip-wire — see §3)

Recomputed this session under the repository convention
`sha256(claim.replace("\r\n","\n").strip().encode("utf-8"))`, read with `yaml.safe_load` from the
node's `claim` field:

| node | level | claim hash | equals the `reviewed_hash` in its own `basis.reviews`? |
|---|---|---|---|
| `CIRCDIST.lift` (root) | CONJECTURED | `sha256:ccad7fa605be1ae14a2dbc1d6c5758300bb8a5f0a3023fcef84725be40e78d8a` | n/a — no review linked (correct for a CONJECTURED root) |
| `CIRCDIST.lift.iff` | CERTIFIED\* | `sha256:c3a841984a07038dfbe3390f0b25cca633d04877ff92fb04bd0e3eaf480f0061` | **yes** |
| `CIRCDIST.lift.nonint` | CERTIFIED\* | `sha256:864bcc604035c7124b7fa23977e00375862520a28f347d092453ddd89b6fed4e` | **yes** |
| `CIRCDIST.lift.gap-example` | CERTIFIED\* | `sha256:487340464e4d0c6b6820d134e40bcda128ed400f131806fe091deedd64a5769c` | **yes** |

All three children are still `CERTIFIED*` with no REFUTE or FURTHER-REPAIR event recorded after
2026-08-20. Every clause map of the assembly's §2 therefore still composes the claim text its
reviews bound themselves to.

### 0.3 What this amendment may and may not do

It applies the review's F1/F2/F3 and folds in its R4-AMEND/R6-AMEND. It introduces **no new
mathematical content**, imports nothing from outside the children's certified scope, and proposes
no claim edit that the review did not license. Where the review recorded a *note* rather than a
*repair* (its §3.4 non-conservative-inventory observation), this amendment records it as a note and
does not act on it.

---

## 1. F1 — "graph-like" is pinned to iff Definition 1.12, **per sector**

### 1.1 The defect, in the reviewer's words and mine

The root claim opens "In **graph-like detector error models** with fixed boundaries". The assembly
states iff Definition 1.12 at the head of §4.1 and then writes, in §4.4, "are graph-like in both
sectors". Definition 1.12 is **sector-indexed**; the root claim's English is not. Under the
ordinary whole-DEM reading of the root's own words — *every elementary fault of the memory
experiment fires at most two detectors of that experiment* — the `[[4,2,2]]` witness is **not**
graph-like, and C5, the assembly's only existential clause, then has no certified witness at all.

This is a type audit: graph-likeness has type `(schedule, sector) → bool` and the root claim uses it
as though it had type `(model) → bool`. Existential clauses do not restrict downward, so this is the
one place in the assembly where an ambiguity changes the answer rather than merely the wording.

**Independently reproduced here (§5.2).** Building the depth-7 witness gate-by-gate from the frozen
fault model and reading off the *full* Z-memory detector set of the memory experiment (Z-check
detectors `D_{b,r}`, `r ∈ {0,…,R}`, **and** X-check detectors `D_{a,r}`, `r ∈ {1,…,R−1}`), at
`R = 3`:

```text
full-DEM detector-weight histogram   {0: 64, 1: 294, 2: 204, 3: 52, 4: 4}
                                     -> 56 faults fire 3 or 4 detectors, max = 4
explicit weight-4 fault              round 1, after the CNOT (control q0, target anc(b)) at t = 1,
                                     Pauli I(x)Y  ->  fires D_{b,1}, D_{a,1}, D_{b,2}, D_{a,2}
sector-restricted (Z-check detectors only, = Definition 1.12)
                                     R=2 {0:130, 1:216, 2:66}   R=3 {0:195, 1:324, 2:99}
                                     R=4 {0:260, 1:432, 2:132}  R=5 {0:325, 1:540, 2:165}
                                     max = 2 everywhere  ->  GRAPH-LIKE per sector
```

These are the review's §3.2/§3.3 numbers, value for value, from an implementation written for this
amendment (§5.2). The mechanism is not exotic: in a Z-memory experiment the X-check detectors
`D_{a,r}` are present and are flipped by `Z`-type error, so any fault carrying both an `X` and a `Z`
component — a `Y`, or a mixed two-qubit Pauli, both inside the frozen model — hits both sectors at
once.

### 1.2 The pin (governing)

> **Governing reading.** Throughout the root claim, its assessment, and the assembly, **"graph-like"
> means `CIRCDIST.lift.iff` Definition 1.12: a *per-sector* condition, `|u(f)| + |u(f)+s(f)| ≤ 2`
> for every elementary fault `f`, on that sector's own detectors.** The memory experiment's **full**
> DEM — both sectors' detectors together — is **not** graph-like in this sense for the `[[4,2,2]]`
> witness, and is **not claimed to be**. No statement of the root, this assembly, or this amendment
> may be read as an assertion about the full DEM.

Two consequences the record must carry:

* The full DEM of the `[[4,2,2]]` witness is *decomposable* — the review reports that each of its 14
  distinct `≥3`-weight columns is the `F₂` sum of two graph-like columns — but **decomposability is
  strictly weaker than Definition 1.12 and is not what the root claim says either**. Nothing below
  uses decomposability.
* Anyone re-running the assembly's §8 item 6(i) must run it **per sector**. Run against the full
  detector set it returns FALSE, and the false conclusion "C5 is undischarged" follows.

### 1.3 The C5 descent paragraph, reworked

The assembly's §4.4 block is replaced, in the pinned reading, by:

> **Assembly step (CONJECTURED), amended.** C5 is discharged **inside the root's graph-like
> restriction, read per sector (Definition 1.12),** by the `[[4,2,2]]` family alone. Those witnesses
> are legal, interleaved, measurement-consistent, single-ancilla, carry the frozen memory-experiment
> boundaries, have `d_circ = 2 > 1 = d_eff`, and are graph-like **in each sector separately** — all
> certified except the graph-likeness, which is NUMERICAL (assembly §9.2; re-verified per sector and
> at `R = 2,3,4,5` in §5.2 here).
>
> The per-sector reading is **load-bearing, not stylistic**: under the whole-DEM reading of the same
> English the same witness fires four detectors on a single elementary fault (§1.1), the descent
> fails, and the root claim as written has no certified witness for its existential clause. The
> reason the per-sector answer is nonetheless robust is **structural, not a lucky scan**: the
> campaign's `[[4,2,2]]` has `|𝒜| = |ℬ| = 1`, so in the Z-memory sector the detector algebra is
> `F₂` and `|u| ≤ 1`, `|u+s| ≤ 1` identically, for **every** schedule; the X-memory sector is the
> mirror. The scan corroborates that argument rather than establishing it.
>
> The **Steane** witness is not graph-like in either sector and therefore corroborates only the
> unrestricted reading of C5. It must not be cited as a graph-like example. (What that costs the
> record is restated in §4.1 below, which corrects the assembly's original account of the cost.)

### 1.4 A note the review recorded and this amendment does **not** act on

The review's §3.4 observes that the assembly's abstracted one-round inventory reports
`max(|u| + |u+s|) = 3` for Steane Z-memory where the raw fault set reaches `4`, because a single
two-qubit Pauli can contribute an `X` part on both the data qubit and the ancilla. The **verdict is
unchanged** (Steane is not graph-like; `3 > 2` already decides it) and the `[[4,2,2]]` bound is
structural rather than scan-derived, so the review filed this as a note, not a repair. It is carried
here as a note with one forward-looking consequence: *an inventory that can undercount a maximum is
the wrong instrument for establishing a maximum*, and any future code whose inventory returns
exactly `2` must be re-checked against raw faults before being called graph-like.

---

## 2. F2 — the certified theorem's `R ≥ d` hypothesis is carried forward

### 2.1 The defect

The assembly's own restatement of the certified criterion (§2.1) reads

> "For every legal, measurement-consistent single-ancilla CSS schedule `M`, **and `R ≥ d`**,
> `d_circ(C_R(M)) = d_eff(M)` ⟺ `∃γ ∈ L_eff` with `|γ| = d_eff(M)` and `repair(γ) = 0`."

`R ≥ d` appears there once and **never again**: not in the root claim (which has no `R` quantifier
and no `C_R(M)` at all), not in the `lift.iff` child claim, and not in the assembly's §6 —
the section whose entire job is that no caveat may be dropped by a promotion of the root. This is
the failure mode the assembly's §0.3 was written to prevent, applied to the assembly itself, and it
is a second type audit: `d_circ` has type `(circuit) → ℤ`, the circuit is `C_R(M)`, and nothing at
the root binds `R`.

The review probed for a live counterexample at `d = 2` and found none — its enumeration gives
`d_circ = 2` for the interleaved witness and `1` for its non-interleaved partner at `R = 1` as well
as `R ≥ 2`, so `R ≥ d` is not demonstrably load-bearing *on this instance*. **That does not
discharge it.** A hypothesis of the certified theorem is a hypothesis of anything assembled from it,
and `d_R` is only known to be non-increasing and constant for `R ≥ d`.

### 2.2 The repair: a new carried caveat

Added to the assembly's §6.2 list, and binding exactly as C-M1…C-M6 bind:

> **C-M7. `R ≥ d` is a hypothesis of the certified criterion.** `CIRCDIST.lift.iff`'s Theorem 5.7 as
> amended reads "for every legal, measurement-consistent single-ancilla CSS schedule `M`, **and
> `R ≥ d`**". Every clause of the root that cites the criterion therefore inherits it: wherever the
> root says `d_circ`, read `d_circ(C_R(M))` **for `R ≥ d`**. The general `R`-dependence is not
> settled by anything the root composes: what is on the record is that `d_R(M)` is non-increasing in
> `R` and constant for `R ≥ d` (assembly §3.3), so an unquantified `d_circ` is well defined only in
> that regime. No instance in this campaign exhibits `d_R` varying below `R = d`, and that absence
> is **evidence, not proof**, and is confined to `d ∈ {2,3}`.

### 2.3 Where the root claim needs an `R` quantifier remark

The reviewer left the choice of instrument to the lead and this amendment does not make it. The two
admissible acts, stated so the lead can pick one:

* **(a) claim edit** — add "for `R ≥ d`" (equivalently "`d_circ` means `d_circ(C_R(M))` for
  `R ≥ d`") to the root claim, immediately at the phrase "characterizes when `d_circ = d_eff`",
  which is the point of use. This **changes the root's claim hash** away from
  `sha256:ccad7fa6…e78d8a` and lapses any review bound to the old text; and
* **(b) assessment-only** — carry C-M7 verbatim in the root's assessment caveats, hash-neutral.

The review's R3 verdict folds F2 into the same sentence that insulates C2's identity reading, on the
ground that both are "what the certified theorem actually quantifies over" and both are currently
invisible at the root; that pairing is adopted here. **If the lead takes (b), the sentence appended
to the assessment must name `R ≥ d` explicitly** — this amendment's whole point is that a
hypothesis carried only inside a restatement is a hypothesis that will be lost again.

---

## 3. F3 — the §0.1 trip-wire is rebound to claim hashes

### 3.1 The defect: the trip-wire fires, and would fire again

The assembly's §0.1 records fourteen whole-file digests and says: *"If any hash above fails to
reproduce, this assembly is void until re-derived."* Recomputed this session on current bytes:

```text
13/14 reproduce exactly.

research/circdist/proof-dag/nodes/CIRCDIST.lift.yaml
   recorded by the assembly   64963af70bf27195987bc3ce58319b36d24aeb66ce975823f334779e13223de5
   computed by the review     01f6a8887021446947d09ec6414b5dc17da11b1415118156449f830a15a97c59
   computed now (7657 B)      84178f08c086ed4d2abb86e65d4966da27ebfa433b486312facf92f78b5749f1
```

Three different digests for the same node in three sessions, while the node's **claim** hashes to
`sha256:ccad7fa6…e78d8a` in all three. The drift is caused by the assembly's own registration and by
the review's: a proof-DAG node file is append-only and **gains events by design**, so binding an
assembly's validity to a node's whole-file digest guarantees that the trip-wire fires on the first
event that registers the assembly itself, and again on the event that registers its review. The
substance is untouched; the rule is wrong. It also makes the assembly's §8 checklist item 1
("Recompute all fourteen hashes") unrunnable as written: the very first thing a root reviewer is
told to do now fails, twice over, on changes that mean nothing.

### 3.2 The repair (governing)

> **§0.1 is rebound.** For **proof-DAG node files**, the assembly's trip-wire binds the node's
> **claim hash** — the object the protocol binds, `DAG_PROTOCOL` §5 step 5 — and not the node file's
> byte digest. The four claim hashes are those tabulated in §0.2 above. For **artifacts and frozen
> notes**, which are immutable append-only files, the whole-file digests of §0.1 stand unchanged and
> all ten of them reproduce.
>
> The void condition is restated accordingly: *this assembly is void until re-derived if any of the
> four claim hashes of §0.2, or any of the ten artifact/frozen-note digests of §0.1, fails to
> reproduce.* A node file that has merely gained an event does **not** void it.
>
> The assembly's §8 checklist item 1 is amended to the same effect: recompute the ten artifact
> digests and the four claim hashes; do not require node-file byte digests to reproduce.

### 3.3 What this does not weaken

Claim-hash binding is **narrower in bytes and no weaker in force** for what the assembly actually
does: every clause of §2 is discharged through a child's *canonical claim text* (the assembly's own
usage rule, §0.3 item 1), and the `reviewed_hash` recorded in each child's `basis.reviews` is a
claim hash. Nothing in the assembly consumes a node file's non-claim fields except the level and
event fields, which §0.2 and the assembly's §8 item 2 check directly and which this amendment
re-checked (§0.2: all three children still `CERTIFIED*`, no REFUTE or FURTHER-REPAIR after
2026-08-20).

---

## 4. Revision-sheet section: the review's R4-AMEND and R6-AMEND, folded in

The assembly's §7 is a list of proposals to the lead; none is applied by the assembly or by this
amendment. The review AGREED with R1, R2, R3 (with F2 folded in — see §2.3), and R5 (recommending
option (a)), and **AMENDED R4 and R6**. Those two amendments are recorded here as the governing
text of the corresponding §7 entries, and the review's two new proposals are recorded as R7/R8.

### 4.1 R4 — right conclusion, one wrong supporting argument (**AMENDED**)

**Conclusion unchanged and undisturbed:** do **not** drop "graph-like" from the root claim until
`CIRCDIST.lift.iff`'s own claim is re-widened and re-reviewed. The sequencing argument is decisive —
dropping the restriction would make the root claim strictly wider than its load-bearing child's
certified scope.

**Argument (iii) is withdrawn.** The assembly wrote that the restriction "excludes the campaign's
best evidence" because the Steane instance (`d = 3`, `g(C) = 1`) is not graph-like. That does not
survive the campaign's own sector convention. Under min-over-sectors (d3-gate §1.4, restated in its
§5.2), a circuit's distance is the minimum over the two memory sectors, and the reviewer reproduced
Steane independently at Z-sector `(d_eff, d_circ) = (2,3)` and X-sector `(2,2)` — so
`min(d_circ^Z, d_circ^X) = 2 = d_eff` and **the Steane instance is not a circuit-level
`d_circ > d_eff` witness at all**. The `[[4,2,2]]` witness, by contrast, has `d_eff = 1 < 2 = d_circ`
in **both** sectors. The graph-like restriction is therefore not discarding a better witness; the
witness that survives it is the one that is robust to the sector convention, which is an argument
*for* the current claim, not against it.

*Provenance, stated precisely:* the Steane per-sector values `(2,3)` and `(2,2)` are the reviewer's
own reproduction (review §5, §7). **This amendment did not re-derive them**; the `[[4,2,2]]` numbers
in §1.1 and §5.2 are this session's own. Nothing in §1–§3 depends on the Steane values.

**Replacement text for §7 R4's argument (iii):**

> (iii) the restriction excludes the campaign's only `d = 3` instance and its only `g(C) = 1` datum
> — a loss of **informativeness**, not of **satisfiability**. It does not exclude a circuit-level
> `d_circ > d_eff` witness, because under the campaign's min-over-sectors convention the Steane
> instance is not one (`min(d_circ) = 2 = d_eff`).

The assembly's §4.4 closing sentence ("the restriction is discarding the campaign's best evidence
for its own root claim") is likewise amended to: *the restriction is discarding the campaign's most
informative instance, but not a circuit-level witness; C5 remains satisfied by the witness that is
robust to the sector convention.*

### 4.2 R6 — accept and widen (**AMENDED**)

Both corrections the assembly proposed to the route's `implication` gloss stand: C5 needed a genuine
computation to descend into the graph-like restriction, and "consistency of the three
formalizations" was not free — it turned up a real `R_sat` contradiction that took two amendment
rounds and two independent reviews to settle. The review's widening is adopted: **the replacement
text must also name the two silent hypotheses the assembly inherits**, because "bookkeeping" is
precisely the word that lets hypotheses evaporate — which is how `R ≥ d` was lost between the
assembly's §2.1 and its §6 (§2 above).

**Replacement text for the route's `implication` (proposal to the lead; not applied here):**

> "Assembly is a clause-to-child map plus two scope arguments: the universal clauses restrict
> downward for free, while the existence clause requires the exhibited witness to be verified
> graph-like **in the per-sector sense of iff Definition 1.12** (`[[4,2,2]]`: yes, structurally;
> Steane: no). Formalization consistency was checked and one contradiction was found and repaired
> (`R_sat ≤ d` versus Corollary 7.3). The assembly inherits **two silent hypotheses from the
> certified criterion — measurement consistency (MC) and `R ≥ d`** — both of which bind every clause
> and neither of which appears in the root claim."

### 4.3 R7 and R8 (new, proposed by the review as required; = F1 and F3)

* **R7 — pin "graph-like" to Definition 1.12, per sector.** Required. Applied as a governing reading
  in §1.2. If the lead prefers it in the claim text rather than the assessment, the minimal edit is
  "in detector error models that are graph-like **in each CSS sector**", which changes the root's
  claim hash.
* **R8 — re-base §0.1's trip-wire on claim hashes for node files.** Required. Applied in §3.2.
  Hash-neutral: it touches the assembly's own bookkeeping, not the claim.

### 4.4 The C-R2 adjudication — recorded, not resolved

The review's verdict on the review-stack discrepancy is **UNDETERMINABLE-FROM-DISK**, with the
balance of evidence favouring the self-report, and it makes one **containment correction** that this
amendment records because it bears on what the root's promotion may claim:

* star-lifting attaches to the review that carries a node's completion, and only `CIRCDIST.lift.iff`
  (and `CIRCDIST.cplx.islands`, which did not promote) links the file in question. So **at most one
  node in this subtree becomes star-liftable** under a cross-stack resolution;
* the **root's star is not liftable either way**, because the root is a conjunction and two of its
  three children remain single-same-stack under C-R1;
* "project-wide" (as `SCHEDULER.yaml` round 12 records the flag) is too wide: no `se`, `ksum`,
  `whgap`, `gross`, or `sat` node links that file.

**Consequently C-R2 does not gate this promotion**: the root's ceiling is `CERTIFIED*` under both
resolutions. C-R2 stays on the caveat list of assembly §6.1 exactly as written, with the assembly's
posture — treat the self-report as data inside a file, not as a verified fact about which model
executed — unchanged. This amendment resolves nothing about model identity and is not evidence
either way.

---

## 5. NUMERICAL — local verification for this amendment

Python 3, standard library only, exact over `F₂`. No `stim`, no external libraries, no proposer or
reviewer code imported or executed. **Inherited limitation (assembly C-O2, and it binds this
amendment too):** this code is independent in its implementation but not in its *model design* — it
enumerates the fault locations and uses the detector definitions of the same frozen spec, so a
systematic modelling error against `stim`'s conventions would survive it as it survived the
documents it checks.

### 5.1 Hash chain and claim hashes (§0.2, §3.1)

```python
import hashlib, yaml

NODES = ['CIRCDIST.lift', 'CIRCDIST.lift.iff', 'CIRCDIST.lift.nonint',
         'CIRCDIST.lift.gap-example']
for nid in NODES:
    b = open('research/circdist/proof-dag/nodes/%s.yaml' % nid, 'rb').read()
    d = yaml.safe_load(b.decode('utf-8'))
    claim = hashlib.sha256(
        d['claim'].replace('\r\n', '\n').strip().encode('utf-8')).hexdigest()
    print('%-26s %-12s claim sha256:%s' % (nid, d['assessment']['level'], claim))
    print('%-26s %-12s file  %s  %d B' % ('', '', hashlib.sha256(b).hexdigest(), len(b)))

RECORDED = { ... }   # the fourteen path -> digest pairs printed verbatim in assembly §0.1
ok = 0
for path, recorded in RECORDED.items():
    cur = hashlib.sha256(open(path, 'rb').read()).hexdigest()
    ok += (cur == recorded)
    if cur != recorded:
        print('STALE %s\n      current %s' % (path, cur))
print('Sec 0.1 whole-file digests reproducing: %d/%d' % (ok, len(RECORDED)))
```

Output (verbatim; `RECORDED` filled in with the fourteen pairs copied from assembly §0.1):

```text
CIRCDIST.lift              CONJECTURED  claim sha256:ccad7fa605be1ae14a2dbc1d6c5758300bb8a5f0a3023fcef84725be40e78d8a
                                        file  84178f08c086ed4d2abb86e65d4966da27ebfa433b486312facf92f78b5749f1  7657 B
CIRCDIST.lift.iff          CERTIFIED*   claim sha256:c3a841984a07038dfbe3390f0b25cca633d04877ff92fb04bd0e3eaf480f0061
                                        file  6f6ea03fe546775f4447707c10fc3e0b26b67a941646f81445f5867b01b22c23  11275 B
CIRCDIST.lift.nonint       CERTIFIED*   claim sha256:864bcc604035c7124b7fa23977e00375862520a28f347d092453ddd89b6fed4e
                                        file  2675c3b6027e41719c3e6933b260f6ca8f4fadf3b68d55ffd85962221e33ee90  5420 B
CIRCDIST.lift.gap-example  CERTIFIED*   claim sha256:487340464e4d0c6b6820d134e40bcda128ed400f131806fe091deedd64a5769c
                                        file  67c0e106cac34ed73a9e0cf1e19783ba58b10f7d0a6a7d69b495d896f715106f  6421 B
STALE research/circdist/proof-dag/nodes/CIRCDIST.lift.yaml
      current 84178f08c086ed4d2abb86e65d4966da27ebfa433b486312facf92f78b5749f1
Sec 0.1 whole-file digests reproducing: 13/14
```

The single stale entry is the root node file, whose **claim** hash is unchanged: this is the F3
finding, reproduced (§3.1).

### 5.2 `[[4,2,2]]` depth-7 witness: full DEM versus per-sector (§1.1)

Gate-level `F₂` symplectic propagation, `CNOT(c,t): x_t ^= x_c ; z_c ^= z_t`. Ancilla `anc(a)`
prepared `|+⟩` and measured in `X` (its outcome is flipped by `z_{anc(a)}`); `anc(b)` prepared `|0⟩`
and measured in `Z` (flipped by `x_{anc(b)}`); ancillas reset each round. Z-memory: ideal `|0⟩^{⊗4}`
initialisation, ideal terminal `Z` readout. Detectors as in the frozen convention:
`D_{b,0} = m_{b,0}`; `D_{b,r} = m_{b,r} + m_{b,r−1}` for `1 ≤ r ≤ R−1`;
`D_{b,R} = m_{b,R−1} + ⊕_{q} readout(q)`; `D_{a,r} = m_{a,r} + m_{a,r−1}` for `1 ≤ r ≤ R−1` (no
`D_{a,0}`: the round-0 `X` outcome is random). Faults (frozen model, unit weight): ancilla prep
`X/Y/Z`; all 15 non-identity two-qubit Paulis after each of the 8 CNOTs; `X/Y/Z` on every qubit idle
at a step; one classical flip per recorded outcome — **206 raw faults per round**.

Schedule: the d3-gate witness used by assembly §9.2, `t(a→q) = {0:0, 1:3, 2:4, 3:5}`,
`t(q→b) = {2:0, 0:1, 1:2, 3:6}`, depth 7.

```python
TA = {0:0, 1:3, 2:4, 3:5}                      # t(a -> q)
TB = {2:0, 0:1, 1:2, 3:6}                      # t(q -> b)
T, DATA, A_ANC, B_ANC = 7, [0,1,2,3], 'A', 'B'
gates = [[] for _ in range(T)]
for q,t in TA.items(): gates[t].append((A_ANC, q))     # X-check ancilla controls data
for q,t in TB.items(): gates[t].append((q, B_ANC))     # data controls Z-check ancilla
busy  = [set(u for g in gates[t] for u in g) for t in range(T)]
QUBITS = DATA + [A_ANC, B_ANC]
PAULI1 = ['X','Y','Z']
PAULI2 = [(p,q) for p in 'IXYZ' for q in 'IXYZ' if (p,q) != ('I','I')]
xz = lambda p: {'I':(0,0),'X':(1,0),'Y':(1,1),'Z':(0,1)}[p]

def run(R, f):
    x = {q:0 for q in DATA}; z = {q:0 for q in DATA}; ma, mb = [], []
    for r in range(R):
        x[A_ANC]=z[A_ANC]=x[B_ANC]=z[B_ANC]=0; ca=cb=0
        if f and f[0]==r and f[1]=='prep':
            dx,dz = xz(f[3]); x[f[2]] ^= dx; z[f[2]] ^= dz
        for t in range(T):
            for (c,tg) in gates[t]:
                x[tg] ^= x[c]; z[c] ^= z[tg]
                if f and f[0]==r and f[1]=='cnot' and f[2]==(c,tg) and f[3]==t:
                    dx,dz = xz(f[4][0]); x[c]  ^= dx; z[c]  ^= dz
                    dx,dz = xz(f[4][1]); x[tg] ^= dx; z[tg] ^= dz
            if f and f[0]==r and f[1]=='idle' and f[2]==t:
                dx,dz = xz(f[4]); x[f[3]] ^= dx; z[f[3]] ^= dz
        fa, fb = z[A_ANC], x[B_ANC]                    # X-basis anc(a); Z-basis anc(b)
        if f and f[0]==r and f[1]=='cflip':
            ca, cb = (1,0) if f[2]=='a' else (0,1)
        ma.append(fa ^ ca); mb.append(fb ^ cb)
    return ma, mb, [x[q] for q in DATA]

def detectors(R, ma, mb, ro):
    D = [('b',0,mb[0])]
    D += [('b',r,mb[r]^mb[r-1]) for r in range(1,R)]
    D += [('b',R, mb[R-1] ^ ro[0]^ro[1]^ro[2]^ro[3])]
    D += [('a',r,ma[r]^ma[r-1]) for r in range(1,R)]
    return D

def all_faults(R):
    out = []
    for r in range(R):
        out += [(r,'prep',anc,p) for anc in (A_ANC,B_ANC) for p in PAULI1]
        for t in range(T):
            out += [(r,'cnot',g,t,pq) for g in gates[t] for pq in PAULI2]
            out += [(r,'idle',t,u,p) for u in QUBITS if u not in busy[t] for p in PAULI1]
        out += [(r,'cflip','a'), (r,'cflip','b')]
    return out

print("(MC) count for the single pair (a,b) =",
      sum(1 for q in DATA if TB[q] < TA[q]), "(must be even)")
for R in (2,3,4,5):
    full, sect, w4 = {}, {}, None
    for f in all_faults(R):
        D = detectors(R, *run(R, f))
        wf = sum(v for (_k,_r,v) in D); ws = sum(v for (k,_r,v) in D if k=='b')
        full[wf] = full.get(wf,0)+1; sect[ws] = sect.get(ws,0)+1
        if wf >= 4 and w4 is None: w4 = (f, [(k,rr) for (k,rr,v) in D if v])
    print("R=%d faults=%4d  full-DEM %s max=%d | sector %s max=%d GRAPH-LIKE=%s"
          % (R, len(all_faults(R)), dict(sorted(full.items())), max(full),
             dict(sorted(sect.items())), max(sect), max(sect) <= 2))
    if w4: print("      weight->=4 fault:", w4[0], "fires", w4[1])
```

```text
(MC) count for the single pair (a,b) = 2 (must be even)
R=2 faults= 412  full-DEM {0: 57, 1: 209, 2: 123, 3: 23} max=3 | sector {0: 130, 1: 216, 2: 66} max=2 GRAPH-LIKE=True
R=3 faults= 618  full-DEM {0: 64, 1: 294, 2: 204, 3: 52, 4: 4} max=4 | sector {0: 195, 1: 324, 2: 99} max=2 GRAPH-LIKE=True
      weight->=4 fault: (1, 'cnot', (0, 'B'), 1, ('I', 'Y')) fires [('b', 1), ('b', 2), ('a', 1), ('a', 2)]
R=4 faults= 824  full-DEM {0: 71, 1: 379, 2: 285, 3: 81, 4: 8} max=4 | sector {0: 260, 1: 432, 2: 132} max=2 GRAPH-LIKE=True
      weight->=4 fault: (1, 'cnot', (0, 'B'), 1, ('I', 'Y')) fires [('b', 1), ('b', 2), ('a', 1), ('a', 2)]
R=5 faults=1030  full-DEM {0: 78, 1: 464, 2: 366, 3: 110, 4: 12} max=4 | sector {0: 325, 1: 540, 2: 165} max=2 GRAPH-LIKE=True
      weight->=4 fault: (1, 'cnot', (0, 'B'), 1, ('I', 'Y')) fires [('b', 1), ('b', 2), ('a', 1), ('a', 2)]
```

**Search scope.** Complete over the frozen model's raw elementary faults for **this one schedule**,
Z-memory sector, `R ∈ {2,3,4,5}` (412–1030 faults); it is **not** a scan over other schedules or
codes, and it computes detector weights only — no distance is computed here, and none is needed for
F1. The sector-restricted maxima agree with the review's §3.2 table row for row; the full-DEM
histogram and the named weight-4 fault agree with its §3.3 exactly, from an independent
implementation.

---

## 6. What this amendment does **not** do

1. **It promotes nothing.** The root stays as the dispatcher finds it. F1/F2/F3 are applied as
   governing text of an append-only amendment; the root's completion review (assembly §8, amended
   at items 1 and 6 by §3.2 and §1.2 here) is a separate act by an independent session.
2. **It applies no claim revision.** §2.3 and §4 record proposals; every one is a dispatcher act,
   and the claim-text options in §2.3(a) and §4.3 R7 would change the root's claim hash away from
   `sha256:ccad7fa6…e78d8a` and lapse any review bound to the old text.
3. **It re-reviews no child**, re-derives no certified result, and imports nothing from outside the
   children's certified claim scope. The `repair ≥ 3` exclusion, the min-cost-covering extension,
   5.6(d), `d_∞`, the `321059/321059` symmetry, and `k > 1` are untouched.
4. **It does not resolve C-R2** and is not evidence about which model executed any review.
5. **It does not act on the review's §3.4 note** beyond recording it (§1.4).
6. **It modifies no existing file** and touched nothing under `research/circdist/proof-dag/`. Files
   created by this session: this one and two sibling amendments
   (`artifacts/circdist_sat_window_amendment1_20260822.md`,
   `artifacts/circdist_cplx_islands_amendment4_20260822.md`), each answering its own review.

**Level ceiling, unchanged.** With three `CERTIFIED*` children, an amendment-author-written repair,
and C-R1, the maximum the root can reach on this route remains `CERTIFIED*`, and only after an
independent review of the assembly **as amended by this file**. `PROVED` is unreachable on this
route.
