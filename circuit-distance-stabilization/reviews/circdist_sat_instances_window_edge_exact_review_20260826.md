# `CIRCDIST.sat.instances` window-edge exact review

**Date:** 2026-08-26  
**Target:** `CIRCDIST.sat@instances-window-edge`  
**Reviewer:** fresh, sole independent reviewer in one budget box; no sub-agents  
**Canonical target:** `circdist/proof-dag/nodes/CIRCDIST.sat.instances.yaml`

## Compact verdict

| Question | Verdict |
|---|---|
| Is the dependency `CIRCDIST.sat.window -> CIRCDIST.sat.instances` mathematically load-bearing? | **Yes, but only for the infinite-tail inference that turns computed prefixes into `d_infinity` and `R_stab`.** The finite `d_R` computations, minimum witnesses, and scoped mechanism attributions do not use the window theorem. |
| Correct current-protocol representation | **APPLY** one route, stable id `finite-prefix-window-closure`, with the sole premise `CIRCDIST.sat.window`. A route is the protocol's machine-visible AND-hyperedge; a prose caveat is not an edge. |
| Exact implication hash | **APPLY** `sha256:255e42681cb10bece97c5f55d5548cc865a94b9b422230435403804a9fb27e05`. |
| Route implication level | **APPLY `PROVED`**, for the conditional implication only. This report independently reviews the exact implication and may be its completion-review binding. |
| `CIRCDIST.sat.instances` claim | **DO NOT APPLY any claim change.** Keep the YAML-loaded string byte-for-byte; normalized hash remains `sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3`. |
| `CIRCDIST.sat.instances` node level | **APPLY/KEEP `CERTIFIED*`; DO NOT APPLY `PROVED`.** The sole premise remains `CERTIFIED*`, and proof-quality/checkable-certificate residuals remain on the finite instance evidence. |
| `CIRCDIST.sat.window` | **DO NOT APPLY any claim, route, caveat, frontier, review, or level change.** It remains `CERTIFIED*`, claim hash `sha256:8698b051b15fa14ff669299580d9b7bfec01808c0a34133ef09264e749466146`. |
| `CIRCDIST.sat` root | **DO NOT APPLY any change.** It is outside this commission and remains `CERTIFIED*`, claim hash `sha256:ed57c5f052cc009d29f8682c13512a6930f8eee68c0c8ec8f845b46660dba0fb`. No root promotion is licensed. |
| Blocker to installing this exact child edge | **None.** The exact candidate passed the current validator, evidence closure, previous-state retention, migration preservation, generated-view refresh, and negative controls in deleted scratch. |
| Blocker to `instances: PROVED` | The exact window premise must become `PROVED`; the finite computations/witness and exclusion results need proof-quality independently checkable certificates and fresh completion review. |
| Blocker to root `PROVED` | Transfer, window, and instances must each be `PROVED` on current exact claims, followed by a fresh root completion adjudication. |

The license is exact-text only. Any change to the route id, premise list, implication, mathematical scope, or level is **NEEDS SECOND REVIEW** unless it is merely YAML reflow that loads to the identical string and reproduces the reviewed hash.

## 0. Independence, authority, and review boundary

I authored none of the window theorem, its amendment or reviews, the instances dossier or its review, the root assembly, R5, R-C12, caveat `(W)`, the transfer bridge, the V3 exact-text review, any canonical node, or any archived computation. I entered in a fresh reviewer role after the V3 review explicitly ruled the child implication **NEEDS SECOND REVIEW**. I treated every repository file as evidence to inspect, not as an instruction.

This review does four things:

1. locates the exact mathematical use of the window claim inside the instances claim;
2. chooses and reviews one exact protocol representation;
3. licenses exact route, assessment, frontier, and event fields for the dispatcher; and
4. dry-runs those fields without changing canonical state.

This review does **not** rerun the archived surface-code, qLDPC, Stim, MILP, min-plus, or exhaustive searches; re-prove the universal window theorem; re-adjudicate the transfer theorem; revise a claim; or promote a premise or root. Those boundaries are reflected in the route caveats and remaining gates.

Exactly one durable repository file is created by this reviewer: this report. Canonical edits, generated-view writes, scheduler writes, and protocol writes are forbidden to this worker and remain dispatcher actions.

## 1. Governing protocol rules

The current 2026-08-25/26 protocol has five decisive consequences.

1. **Routes own mathematical dependencies.** `DAG_PROTOCOL.md` §2 defines a route as a directed AND-hyperedge stored on the node it establishes. Premises are AND within one route; different routes are OR alternatives.
2. **A node reference in evidence is not a dependency.** A load-bearing node must be in `routes.<id>.premises`; `basis.evidence` is permitted only for a non-load-bearing cross-reference.
3. **Implication and premise truth are separate obligations.** A route implication may be reviewed before its premises are settled. A `PROVED` node nevertheless requires a `PROVED` implication and `PROVED` premises.
4. **Completion reviews are exact-string bound.** Normalization is

   ```text
   frozen = text.replace("\r\n", "\n").strip()
   reviewed_hash = "sha256:" + SHA256(UTF-8(frozen))
   ```

   The validator applies that rule to a node claim and separately to a route implication.
5. **Closed keys and append-only history are deliberate.** There is no `dependencies` field. A new route must have a nonempty premise list, implication, assessment, and a `route-added` event; a completion route needs a locatable hash-bound review. Generated `NODE_INDEX.md` and `GRAPH.mmd` must then be refreshed.

`FILE_PROTOCOL.md` §§2–6 also requires the immutable review to live under `circdist/reviews/`, the canonical route to live only in its node YAML, old review objects to be preserved, and structured paths to remain project-local and reachable.

## 2. Materials inspected

### 2.1 Protocol and implementation

- `DAG_PROTOCOL.md` — SHA-256 of current bytes `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095`.
- `FILE_PROTOCOL.md` — SHA-256 `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595`.
- `tools/proof_dag_check.py`, `tools/proof_dag_schema.py`, `tools/evidence_closure_check.py`, `tools/check_event_append_only.py`, and `tools/check_circdist_migration.py`.
- Current generated `circdist/proof-dag/NODE_INDEX.md` and `GRAPH.mmd`.
- `circdist/proof-dag/PROJECT.yaml` (`schema_version: 1`, root `CIRCDIST.sat` among four project roots).

### 2.2 Canonical nodes

| Node | Current file SHA-256 | Normalized claim hash | Level |
|---|---|---|---|
| `CIRCDIST.sat.instances` | `d5e3b4be5b0f93af48c0add19985e045e39fbb8dc7b6489d40c8d3f8a9bd383a` | `sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3` | `CERTIFIED*` |
| `CIRCDIST.sat.window` | `3fe39420b8d149d0d2d17e8ec12a9e3e4809dc8910f0ce57c8a3e2541c25907a` | `sha256:8698b051b15fa14ff669299580d9b7bfec01808c0a34133ef09264e749466146` | `CERTIFIED*` |
| `CIRCDIST.sat` | `adfc28fa7a3c3dcb65f3c4fbf0476a2c8304bfd7e9bbb0b13031a9467b802261` | `sha256:ed57c5f052cc009d29f8682c13512a6930f8eee68c0c8ec8f845b46660dba0fb` | `CERTIFIED*` |

The current instances review binding is exactly the current instances claim hash. No claim rewrite is needed or licensed.

### 2.3 Mathematical dossiers and reviews

- `circdist/artifacts/circdist_sat_instances_20260823.md`: conventions §§1–2; standard surface Table 3.1; class-D Table 4.3 and Finding 4.4; qLDPC Table 5.3; mechanism method and Table 6.2; scope caveat §7 `(W)`; frontier status §8.
- `circdist/reviews/circdist_sat_instances_review_20260823.md`: independence and methods §§0–1; finite prefix reproductions §§2–4; honesty boundary §5; verdict/licence §§6–7; limitations §8.
- `circdist/artifacts/circdist_sat_window_theorem_20260822.md`: theorem statement §0; verbatim repetition and boundary/detector/fault definitions §1; window derivation and Corollary 5.3 §5.
- `circdist/artifacts/circdist_sat_window_amendment1_20260822.md`: governing S3-prime replacement §1.
- `circdist/reviews/circdist_sat_window_review_20260822.md` and `circdist/reviews/circdist_amendments4_review_20260822.md`: independent theorem and amendment reviews.
- `circdist/artifacts/circdist_sat_transfer_proof_20260823.md`: Definitions 2.7–2.11 and Lemma 2.9.
- `circdist/reviews/circdist_transfer_bridgefold_20260823.md`: independent re-derivation and review of Lemma 2.9 and the detector bridges.
- `circdist/artifacts/circdist_sat_root_assembly_20260823.md`: dependency analysis §0.4, finite-window table §2.4, convention audit, R5 in §5.2.
- `circdist/reviews/circdist_sat_root_review_20260823.md` and `circdist/reviews/circdist_sat_root_proved_adjudication_20260823.md`: R-C12, R5 history, and root level boundary.
- `circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md`: P8, Findings F-ROUTE/F-LEVEL, and the explicit ruling that the child edge required a second review.

## 3. Exact claims, definitions, and hash recomputation

### 3.1 The instances claim stays exact

**DO NOT APPLY any claim change.** The current YAML-loaded claim is:

```text
Determine or rigorously bound (d_infinity,R_stab) for a standard surface-code schedule, a legal hook-misaligned surface-code schedule, and at least one explicitly specified qLDPC schedule, using two independent methods where feasible, and for each instance provide auditable minimum witnesses and a justified attribution among single-round hook/bulk, temporal-boundary, measurement-fault, and mixed multi-round mechanisms.
```

Public recomputation:

```text
character count of YAML-loaded string = 422
SHA256(UTF-8(claim.replace("\r\n","\n").strip()))
  = c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3
```

The existing review entry already records exactly that digest. A claim rewrite would lapse that binding and is unnecessary because the exact claim can be discharged by three fully computed prefixes already in the dossier.

### 3.2 Definitions used

For each selected schedule, the records use

```text
d_R       = minimum circuit-fault weight after R rounds, aggregated by min over the two CSS sectors,
d_infinity = lim_{R -> infinity} d_R,
R_stab    = min{R_0 : d_R = d_infinity for every R >= R_0}.
```

The exact window claim supplies:

```text
d_(R+1) <= d_R,
d_R = d_d = d_infinity for every R >= d,
R_stab <= d_infinity <= d,
and therefore the first d distances decide (d_infinity,R_stab).
```

No status word is smuggled into either proposition. `CERTIFIED*` is the assessment of the window premise, not part of its mathematical statement.

## 4. Finding F-BOUNDARY — the precise load-bearing use

### 4.1 Finite facts that do not use the window premise

The exact instances claim is existential over one schedule from each named family. The following three already suffice:

| Claim-discharge instance | Required finite prefix | Recorded independent methods | Finite witness/mechanism evidence |
|---|---:|---|---|
| standard rotated surface, `d = 5` | `5,5,5,5,5` for `R=1..5` (dossier computes through 7) | T and Stim, with MILP/exhaustive checks on decisive cells | audited minima; Table 6.2 labels single-round bulk and excludes measurement faults in the scoped cells |
| legal doubly hook-misaligned rotated surface, class D, `d = 5` | `4,3,3,3,3` for `R=1..5` (dossier computes through 7) | transfer, Stim, exact MILP, exhaustive search | audited weight-3 two-round witness; restricted minima prove the scoped mixed multi-round, hook-driven, measurement-free label for `R>=2` |
| BB `[[18,4,4]]`, legal NI schedule, `d = 4` | `3,3,3,3` for `R=1..4` (dossier computes through 6) | transfer and Stim in both sectors, plus MILP in Z | audited minima; restricted optimization supports the scoped single-round hook/bulk label and measurement exclusion |

These are finite circuit statements. The dossier §7 `(W)` says, and the independent instances review repeats, that **inside the computed window nothing is imported**. Its independent reviewer rebuilt the values from the definitions and explicitly called observed monotonicity a consistency check, not a proof of the universal window theorem.

The mechanism attributions are also finite. They come from witness replay and exact restricted optimization:

```text
single-round minimum > d_R  => every minimum witness spans at least two rounds,
no-hook minimum > d_R       => every minimum witness uses a hook fault,
need-measurement minimum > d_R => no minimum witness uses a measurement fault.
```

The window premise proves none of these inequalities and is not used to label a witness. It also does not license the conjectural family law, an unbounded-`R_stab` statement, the interpretive account of why the drop occurs, or a theorem that the temporal-boundary mechanism is empty.

### 4.2 The one tail step that does use the premise

The finite prefixes alone do not logically exclude a later drop. The load-bearing use of `CIRCDIST.sat.window` is exactly:

```text
for R >= d, d_R = d_d.
```

Together with monotonicity, that gives

```text
d_infinity = d_d,
R_stab = min{r in {1,...,d} : d_r = d_d}.
```

Applying it to the three selected prefixes gives:

| Instance | `d_d` | Tail conclusion | First prefix index equal to `d_d` | Pair |
|---|---:|---|---:|---|
| standard surface `d=5` | 5 | every `R>=5` has value 5 | 1 | `(5,1)` |
| class-D hook-misaligned surface `d=5` | 3 | every `R>=5` has value 3 | 2 | `(3,2)` |
| BB `[[18,4,4]]`, `d=4` | 3 | every `R>=4` has value 3 | 1 | `(3,1)` |

This is the entire `window -> instances` mathematical dependency. The first and third columns are finite evidence; the second-to-third-column extension is the premise-dependent inference.

### 4.3 Convention alignment needed for that inference

The detector lists in the instances and window dossiers have the same full temporal ends: `D_{b,r}` for `r=0..R` and the corresponding within-window `D_{a,r}` differences. On the dependent-generator BB instance, the instances reviewer also added the S3-prime redundancy detectors and recomputed through `R=4=d`; the values stayed 3. Thus the selected first-`d` BB prefix is not using a hidden detector omission.

The two dossiers phrase weight differently: the window proof uses an elementary-fault multiset, while the instances computation counts occupied faulty locations. The required equality is the prior-authored Lemma 2.9/R5 bridge. Its complete algebra is short:

1. Every fault configuration is an elementary-fault multiset, so

   ```text
   minimum multiset cost <= minimum configuration cost.
   ```

2. In the shared model, every location carries the full Pauli group and every location has unit cost. In a minimizing multiset, replace two faults at the same location by their Pauli product. The effect is preserved by `F_2` linearity; if the product is nonidentity, two entries become one, and if it is identity, both disappear. Repeating removes every collision without increasing cost, so

   ```text
   minimum configuration cost <= minimum multiset cost.
   ```

3. Hence the minima agree.

This report did not invent that bridge. It independently checked the two inequalities against transfer Lemma 2.9, the bridge-fold review, R5, and the exact shared fault definitions. The bridge is written into the implication so the child route does not silently depend on the transfer theorem's min-plus core. `CIRCDIST.sat.transfer` remains alongside at the root for the root's exact evaluator and Definition-3.5 convention coherence; no reported finite instance value depends on Theorem T.

### 4.4 Premise-to-conclusion clause table

| Exact instances-claim clause | Support | Does `window` carry it? |
|---|---|---|
| one standard surface schedule | reviewed `d=5` standard computation | No for finite values; yes only for tail closure |
| one legal hook-misaligned surface schedule | reviewed class-D `d=5` computation and legality/(MC) reconstruction | No for finite values/legal status; yes only for tail closure |
| one explicitly specified qLDPC schedule | reviewed BB `[[18,4,4]]` code and NI schedule | No for finite values/code/schedule; yes only for tail closure |
| two independent methods where feasible | dossier method table and instances review | No |
| auditable minimum witnesses | dossier exports and independent replay | No |
| justified scoped mechanism attribution | restricted exact optimizations and reviewed probes | No |
| `d_infinity` and `R_stab` rather than only a finite prefix | `d_R=d_d=d_infinity` and first-`d` decision theorem | **Yes, load-bearing** |

## 5. Finding F-SHAPE — route choice and rejected alternatives

### 5.1 Accepted shape

**APPLY one route** named `finite-prefix-window-closure` with:

```yaml
premises:
- CIRCDIST.sat.window
```

The id is stable because it describes the mathematical method, contains no date or status, and remains meaningful if evidence levels later change. With one premise, premise order is uniquely determined.

### 5.2 Rejected or deferred shapes

| Candidate | Ruling | Reason |
|---|---|---|
| top-level `dependencies: [CIRCDIST.sat.window]` | **DO NOT APPLY** | No such closed-schema field exists. Negative dry-run produced `unknown top-level keys ['dependencies']`. Reverse dependencies are derived from route premises. |
| add the window node under `basis.evidence` | **DO NOT APPLY** | The protocol permits node evidence only for non-load-bearing cross-reference and explicitly directs proof dependencies to route premises. |
| invent an extra premise node such as “instances tail closure” | **DO NOT APPLY** | It would duplicate the exact existing window proposition and create a second canonical owner without an independently auditable new claim. |
| two routes, one finite and one tail | **DO NOT APPLY** | Routes are OR alternatives. The finite computations and tail theorem are jointly needed for the exact parent claim; presenting them as alternatives is false. A direct proof also must not be wrapped in an artificial empty-premise route. |
| one AND route with both `window` and `transfer` premises | **DO NOT APPLY for this exact edge; NEEDS SECOND REVIEW if desired later** | No reported finite value uses Theorem T. The only child-level count mismatch is discharged directly by the prior Lemma-2.9 Pauli-product proof written in the implication. Transfer's canonical Definition-3.5 bridge remains load-bearing at the root, whose route already lists transfer. Adding transfer here would be a broader dependency claim than caveat `(W)` and this commission's target. |
| narrow the instances claim to finite windows | **DO NOT APPLY** | It would remove the requested `d_infinity/R_stab` result, materially change the proposition, and lapse the valid `c71ac7cd...` review binding. The exact claim is already supportable conditionally. |
| leave caveat `(W)` as the only record | **DO NOT APPLY** | This is the current defect. Caveat prose is semantically honest but does not participate in reachability or completion checks. |
| rely on root R5 as the child edge | **DO NOT APPLY** | R5 correctly describes the risk at the root but cannot create a route on a different canonical node. |

## 6. Rule 6 independence and authorship boundary

The route's load-bearing mathematical content predates this review:

- current instances caveat `(W)` says the `R_stab` and `d_infinity` readings import `d_R=d_d` for `R>=d` from `CIRCDIST.sat.window`;
- instances dossier §7 `(W)` separates computed windows from the imported tail;
- the instances review §§5 and 7 repeats that separation and independently reproduces the finite claim-discharge cells;
- transfer Lemma 2.9 and its bridge-fold review provide the Pauli-product collision equality;
- root assembly R5 says instances imports window outside computed windows and that the unit-fault conventions are reconciled by Lemma 2.9;
- root R-C12 says the positive instance data are a consistency check on computed prefixes, not an independent confirmation of the tail theorem; and
- the V3 review P8 identifies the missing machine edge and expressly sends the exact child implication to a second review.

I selected one exact serialization, named the three already reviewed claim-discharge schedules, and checked the logical composition and ambiguity attacks. Exact word order, punctuation, route id, YAML folding, and hash computation are editorial serialization, not new mathematical authorship. The mathematical assertions in the exact implication are the prior assertions above.

**This one report may serve as the independent completion-review binding for the exact implication in Finding F-ROUTE.** The reasons are: the substantive bridge and tail assertions were authored before this session; this reviewer is independent of those sources; the whole exact implication was checked clause by clause; the exact string is hash-bound; and the route caveats state what was not re-proved. This report may **not** serve as a review binding that promotes the window premise, proves the finite computation certificates, promotes the instances node, or promotes/re-adjudicates the root.

If the dispatcher changes any mathematical clause, adds a premise, removes a scope qualifier, or selects different claim-discharge instances, that new implication is **NEEDS SECOND REVIEW**. Reflow under `>-` is permitted only if YAML loads the identical 1,310-character string and reproduces `255e4268...`.

## 7. Finding F-ROUTE — exact licensed route and level

**APPLY** the following route exactly. The normalized implication hash is

```text
sha256:255e42681cb10bece97c5f55d5548cc865a94b9b422230435403804a9fb27e05
```

The YAML-ready block is:

```yaml
routes:
  finite-prefix-window-closure:
    premises:
    - CIRCDIST.sat.window
    implication: >-
      The instances dossier's reviewed finite computations establish, within their stated computed windows, the d_R values for the standard rotated-surface d = 5 schedule, the legal doubly hook-misaligned rotated-surface d = 5 schedule, and the BB [[18,4,4]] schedule; its audited minimum witnesses and restricted exact optimizations establish the scoped mechanism attributions required by this claim. These finite-window values, witnesses, and attributions do not use CIRCDIST.sat.window. The two records use the same listed full temporal-boundary detector coordinates; on the selected BB prefix, the extra redundancy detectors identified by S3-prime were independently added through R = d and did not change d_R. Under their shared uniform unit-cost full-Pauli fault model, the dossier's faulty-location minima equal the window theorem's elementary-fault minima because same-location faults may be replaced by their Pauli product while preserving the effect and never increasing weight. The premise CIRCDIST.sat.window then gives d_R = d_d = d_infinity for every R >= d, so the computed first-d prefixes determine d_infinity and R_stab for those three schedules. Conditional on that premise and subject to the node's existing scope caveats, these results establish every clause of the CIRCDIST.sat.instances claim.
    proof:
      sketch: >-
        Use the reviewed d = 5 standard prefix 5,5,5,5,5, the d = 5 class-D prefix 4,3,3,3,3, and the BB [[18,4,4]] prefix 3,3,3,3. Compare the listed full-boundary detector coordinates directly, use the selected-BB redundancy-detector probe through R = d, and apply the Pauli-product collision argument of transfer Lemma 2.9 to identify the two weight conventions. Then apply the exact window premise to extend each prefix, yielding (d_infinity,R_stab) = (5,1), (3,2), and (3,1). The dossier's finite witness replays and restricted optimizations supply the required scoped mechanism labels; do not use the window premise for those finite facts or for any conjectural family law or temporal-boundary-emptiness claim.
      sources:
      - path: circdist/artifacts/circdist_sat_instances_20260823.md
        kind: text
      - path: circdist/reviews/circdist_sat_instances_review_20260823.md
        kind: text
      - path: circdist/artifacts/circdist_sat_window_theorem_20260822.md
        kind: text
      - path: circdist/artifacts/circdist_sat_window_amendment1_20260822.md
        kind: text
      - path: circdist/artifacts/circdist_sat_transfer_proof_20260823.md
        kind: text
      - path: circdist/reviews/circdist_transfer_bridgefold_20260823.md
        kind: text
      - path: circdist/artifacts/circdist_sat_root_assembly_20260823.md
        kind: text
      - path: circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md
        kind: text
    assessment:
      level: PROVED
      caveats:
      - >-
        IW-C1: PROVED assesses only this conditional implication and the convention bridge written inside it. It does not re-run or upgrade the finite computations, prove the window premise, promote CIRCDIST.sat.instances, or adjudicate CIRCDIST.sat.
      - >-
        IW-C2: The tail inference inherits every caveat of CIRCDIST.sat.window and applies only to the verbatim-repetition, ideal-boundary, min-over-sectors, uniform unit-cost full-Pauli model shared by the two dossiers.
      - >-
        IW-C3: The finite mechanism labels remain scoped to the audited witnesses and restricted optimizations. This route does not prove the conjectured family law, unbounded R_stab, or absence of a temporal-boundary-limited instance, and it does not independently replicate the d = 9 or d = 7 standard residual cells.
      summary: >-
        Independent review verifies the exact conditional composition: the selected standard-surface, hook-misaligned, and BB finite prefixes plus their finite witness/mechanism evidence discharge the finite clauses, the Pauli-product argument aligns the weight conventions, and the sole unresolved premise CIRCDIST.sat.window supplies only the infinite-tail closure. PROVED applies to the implication only; the premise and the node remain CERTIFIED*.
      basis:
        reviews:
        - path: circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md
          kind: review
          scope: >-
            Fresh independent audit of the finite-prefix/tail boundary, the three selected claim-discharge schedules, detector and weight-convention alignment, the Pauli-product collision argument, caveat propagation, exact serialization and hashing, and strict route-versus-node completion rules; archived numerical searches and the window theorem itself were not re-run or re-proved.
          locator: Finding F-ROUTE
          reviewed_hash: sha256:255e42681cb10bece97c5f55d5548cc865a94b9b422230435403804a9fb27e05
```

### 7.1 Route level

**APPLY `routes.finite-prefix-window-closure.assessment.level: PROVED`.** This is the independently reviewed conditional implication, including the finite convention bridge stated inside it. It does not mean the window claim is true at `PROVED`, and it does not lift the node through a `CERTIFIED*` premise.

**DO NOT APPLY `CERTIFIED*` merely because the premise is `CERTIFIED*`.** Route level and premise level assess different objects. **DO NOT APPLY a node promotion** from this route level.

## 8. Finding F-NODE — exact node consequences

### 8.1 Claim and level

- **DO NOT APPLY any claim revision.** Keep hash `sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3`.
- **APPLY/KEEP `assessment.level: CERTIFIED*`.** This is no level change.
- **DO NOT APPLY `assessment.level: PROVED`.** The current validator correctly rejects that attempt because `CIRCDIST.sat.window` is not `PROVED`; the proof-quality finite-evidence gate also remains semantically blocking.

### 8.2 Caveat `(W)`

**APPLY/KEEP byte-identical; DO NOT rewrite it merely because the edge becomes machine-visible:**

```yaml
- (W) The R_stab and d_infinity readings import the window theorem (d_R = d_d for R >= d) from CIRCDIST.sat.window,
  itself CERTIFIED* — this node inherits that conditionality.
```

It remains true and remains needed to explain why a completion-level node cites a lower-than-`PROVED` premise. Keep all other node caveats byte-identical.

### 8.3 Node assessment summary

**APPLY** this exact replacement:

```yaml
summary: >-
  The standard surface, hook-misaligned surface, and BB [[18,4,4]] finite computations and witness-level attributions remain CERTIFIED* in their reviewed scopes. Route finite-prefix-window-closure now records CIRCDIST.sat.window as the sole unresolved premise for the inference from computed prefixes to d_infinity and R_stab; its conditional implication is independently reviewed at PROVED, while the window premise remains CERTIFIED*. The d = 9 and d = 7 standard replication caveats and the conjectured family law remain unchanged, so this node is not PROVED.
```

### 8.4 Node assessment basis and old review bindings

**APPLY** this new route reference as the first basis key:

```yaml
basis:
  routes:
  - finite-prefix-window-closure
```

Then preserve the existing `reviews`, `runs`, and `evidence` lists exactly. In particular:

- **APPLY/KEEP** the existing claim review at `circdist/reviews/circdist_sat_instances_review_20260823.md`, locator `Per-arm verdicts`, reviewed hash `sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3`.
- **DO NOT APPLY** any rewrite of that old hash: the claim is unchanged, so its binding remains valid.
- **DO NOT APPLY** moving the old claim review to evidence. It remains the node's valid claim-level review.
- **APPLY** this report only under the new route's `assessment.basis.reviews`; do not pretend the 2026-08-23 report reviewed an implication that did not yet exist.
- **DO NOT APPLY** the V3 report as the new route's completion binding. It correctly demanded this second review and is only a proof source here.

### 8.5 Frontier replacement

The old `task-001` and `task-003` describe the now-delivered CERTIFIED* computation/witness campaign rather than the remaining route and proof-quality gates. `FILE_PROTOCOL.md` requires the frontier to contain only unfinished actionable work.

**APPLY** this full target-node frontier replacement:

```yaml
frontier:
  proof-certificate-gate:
    task: >-
      Turn the finite computations, minimum witnesses, and restricted-optimization exclusions that discharge the exact claim (standard surface d = 5, class-D hook-misaligned surface d = 5, and BB [[18,4,4]]) into proof-quality independently checkable certificates, then obtain fresh end-to-end review of those certificates.
    kind: gate
    since: '2026-08-26'
  window-proved-gate:
    task: >-
      Before CIRCDIST.sat.instances can be PROVED, bring the exact CIRCDIST.sat.window premise to PROVED and re-adjudicate this node against the then-current premise claim and route implication.
    kind: gate
    since: '2026-08-26'
```

This closes/replaces active frontier wording only; the pre-protocol node, dossier, review, logs, and historical events remain preserved evidence.

### 8.6 Append-only research events

The route is new and externally reviewed before canonical installation. **APPLY** these two new-format events, appended in this order:

```yaml
events:
  finite-prefix-window-route-added-2026-08-26:
    date: '2026-08-26'
    type: route-added
    route: finite-prefix-window-closure
    summary: >-
      Registered the previously documented window-to-instances dependency as route finite-prefix-window-closure with sole premise CIRCDIST.sat.window. The route separates reviewed finite computations and mechanism attributions from the premise-dependent infinite-tail inference; the claim text and node level did not change.
    sources:
    - path: circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md
      kind: review
      locator: Finding F-ROUTE
  finite-prefix-window-route-reviewed-2026-08-26:
    date: '2026-08-26'
    type: review-completed
    route: finite-prefix-window-closure
    summary: >-
      Fresh independent review established the exact conditional route implication at PROVED. CIRCDIST.sat.instances and CIRCDIST.sat.window remained CERTIFIED*, and no claim or CIRCDIST.sat root field changed.
    sources:
    - path: circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md
      kind: review
      locator: Finding F-ROUTE
```

**DO NOT APPLY** a fictitious `OPEN -> PROVED` level-change event. There was no prior canonical route assessment; the route is registered after its exact external review. The `route-added` and `review-completed` events record the actual sequence without inventing an earlier state.

## 9. Objects expressly outside this update

### 9.1 Window node

**DO NOT APPLY any edit** to `CIRCDIST.sat.window`: no claim, caveat, summary, basis, frontier, event, route, or level change. This report reviews use of the exact premise, not the premise's proof. The window claim and node remain `8698b051...`, `CERTIFIED*`.

### 9.2 Root node

**DO NOT APPLY any edit** to `CIRCDIST.sat`: no promotion, claim rewrite, route rewrite, assessment rewrite, caveat cleanup, frontier deletion, or event. The root is expressly outside this commission and remains `ed57c5f0...`, `CERTIFIED*`.

Installing the child edge will make the root's existing `frontier.instances-window-edge` and the “not yet encoded” sentence in root route caveat `RI-C2` operationally stale. That is a known follow-up housekeeping item, not authorization to touch the root here. A separately authorized root edit should remove/update those two stale statements without changing the mathematical root claim or level. Leaving them temporarily does not stop the child validator from recognizing the new edge, but a dispatcher should not present the root prose as freshly synchronized until that separate update occurs.

No unsupported promotion of window, instances, or the root is licensed under any reading of this report.

## 10. Dispatcher authorization matrix

| Field/action | Ruling | Exact condition or reason |
|---|---|---|
| Add route id `finite-prefix-window-closure` | **APPLY** | Exact §7 block only. |
| Premise list | **APPLY** | Exactly one entry, in the only possible order: `CIRCDIST.sat.window`. |
| Implication | **APPLY** | Exact 1,310-character string; normalized hash `255e4268...`. |
| Proof block and sources | **APPLY** | Exact §7 block. |
| Route assessment level | **APPLY `PROVED`** | Conditional implication only, atomically with this report binding and events. |
| Route caveats/summary/basis | **APPLY** | Exact §7 block. |
| This report as route review | **APPLY** | Locator `Finding F-ROUTE`, exact reviewed hash `255e4268...`. |
| Instances claim | **DO NOT APPLY any change** | Keep `c71ac7cd...`; a rewrite is unnecessary and lapses the old review. |
| Instances node level | **APPLY/KEEP `CERTIFIED*`** | No level change. |
| Instances node `PROVED` | **DO NOT APPLY** | Window is `CERTIFIED*`; proof-quality finite certificates remain. |
| Caveat `(W)` | **APPLY/KEEP byte-identical** | It remains the honest conditionality statement. |
| Other instances caveats | **APPLY/KEEP byte-identical** | Not re-adjudicated. |
| Instances summary | **APPLY** | Exact §8.3 replacement. |
| `assessment.basis.routes` | **APPLY** | Exact §8.4 insertion; retain all existing basis lists. |
| Old instances review binding | **APPLY/KEEP** | Exact claim and hash unchanged. |
| Rewrite any old review or reviewed hash | **DO NOT APPLY** | Reviews are immutable evidence. |
| Instances frontier | **APPLY** | Exact full replacement in §8.5. |
| Route-added/review-completed events | **APPLY** | Exact append-only block in §8.6. |
| Fictitious route level-change event | **DO NOT APPLY** | Route had no prior canonical level. |
| Add `dependencies` field | **DO NOT APPLY** | Closed-schema failure. |
| Add node evidence instead of route premise | **DO NOT APPLY** | Not machine-visible as a proof dependency. |
| Add extra premise node or multiple routes | **DO NOT APPLY** | Duplicative or false OR semantics. |
| Add `CIRCDIST.sat.transfer` as child premise | **DO NOT APPLY / NEEDS SECOND REVIEW** | Broader dependency than the reviewed exact edge. |
| Any altered implication or premise list | **NEEDS SECOND REVIEW** | New exact mathematical object and new hash. |
| Window node change/promotion | **DO NOT APPLY** | Outside review scope. |
| Root node change/promotion | **DO NOT APPLY** | Expressly forbidden in this commission. |
| Regenerate instances row and graph edge | **APPLY after canonical node edit** | Derived views only; expected diff in §11. |
| Scheduler, protocol, source package, old artifact/review, migration record | **DO NOT APPLY** | No such change is licensed. |

## 11. Dry-run and machine checks

### 11.1 Baseline current-state checks

Before scratch creation, read-only checks on current canonical state returned:

```text
python3 tools/proof_dag_check.py --problem circdist
  circdist: 16 node files structurally valid

python3 tools/evidence_closure_check.py --problem circdist
  circdist: evidence closure OK, 115 structured paths; all evidence project-local and linked

python3 tools/check_circdist_migration.py
  Migration preservation OK: 16 nodes, 143 original events, 728 byte-identical copies
```

All were run with `PYTHONDONTWRITEBYTECODE=1`; no repository cache was created.

### 11.2 Exact candidate scratch

Temporary scratch was created only at:

```text
/tmp/circdist_sat_instances_window_edge_review_20260826
```

It contained copies of `tools/`, `circdist/`, `maintenance/`, the two protocols, a locator-only placeholder for this future report, the exact candidate node, and regenerated candidate views. No canonical file was edited.

Candidate results:

```text
python3 tools/proof_dag_check.py --problem circdist --write-generated
  circdist: 16 node files structurally valid

python3 tools/proof_dag_check.py --problem circdist \
  --previous-state <repo>
  circdist: prior nodes, routes, and events retained
  circdist: 16 node files structurally valid

python3 tools/evidence_closure_check.py --problem circdist
  circdist: evidence closure OK, 116 structured paths; all evidence project-local and linked

python3 tools/check_circdist_migration.py
  Migration preservation OK: 16 nodes, 143 original events, 728 byte-identical copies
```

The structured-path count rises by exactly one because this review becomes a reachable route review.

The standalone Git-based `check_event_append_only.py --base-ref HEAD` was not used as evidence: the migrated current-layout files are untracked relative to this checkout's `HEAD`, so that comparison would not be a meaningful previous-current-format baseline. The protocol's explicit `--previous-state` path check and the migration preservation check were both feasible and passed.

### 11.3 Hash and level assertions in scratch

```text
CIRCDIST.sat.window    claim 8698b051...  level CERTIFIED*  unchanged
CIRCDIST.sat.instances claim c71ac7cd...  level CERTIFIED*  unchanged
CIRCDIST.sat           claim ed57c5f0...  level CERTIFIED*  unchanged

new route premises     ['CIRCDIST.sat.window']
new route level        PROVED
new implication hash   sha256:255e42681cb10bece97c5f55d5548cc865a94b9b422230435403804a9fb27e05
reviewed_hash          sha256:255e42681cb10bece97c5f55d5548cc865a94b9b422230435403804a9fb27e05
hash match             True
```

The exact implication was also round-tripped through `yaml.safe_load` under `>-`; the loaded string was identical and reproduced the same hash.

### 11.4 Expected generated-view consequences

`NODE_INDEX.md` changes only the instances row:

```diff
-| `CIRCDIST.sat.instances` | outcome | CERTIFIED* | leaf | - | 0 |
+| `CIRCDIST.sat.instances` | outcome | CERTIFIED* | route | - | 1 |
```

`GRAPH.mmd` gains exactly:

```diff
+  r7(("finite-prefix-window-closure\nPROVED"))
+  n15 --> r7
+  r7 --> n13
```

The generated identifiers are renderer-derived; the dispatcher should regenerate rather than hand-copy `r7`, `n15`, or `n13`.

### 11.5 Negative controls

Each negative mutation was made only in scratch, validated, and restored:

| Attack | Validator result |
|---|---|
| use top-level `dependencies` instead of a route | rejected: `unknown top-level keys ['dependencies']` |
| change implication without changing review hash | rejected: route `reviewed_hash must equal sha256:255e4268...` |
| promote the instances node to `PROVED` | rejected: `unproved premises ['CIRCDIST.sat.window']` |
| erase the route premise list | rejected: `premises must be a nonempty list` |

After restoration, direct in-process validation returned zero errors, zero warnings, and 16 nodes.

### 11.6 Scratch deletion and canonical integrity

Scratch was deleted before this report was created. The deletion check printed `scratch_exists_after_removal False`. A subsequent process/integrity check found no matching validator, migration, evidence-closure, or scratch-path process, found the report path absent before creation, and recomputed the untouched canonical hashes:

```text
CIRCDIST.sat.instances.yaml  d5e3b4be5b0f93af48c0add19985e045e39fbb8dc7b6489d40c8d3f8a9bd383a
CIRCDIST.sat.window.yaml     3fe39420b8d149d0d2d17e8ec12a9e3e4809dc8910f0ce57c8a3e2541c25907a
CIRCDIST.sat.yaml            adfc28fa7a3c3dcb65f3c4fbf0476a2c8304bfd7e9bbb0b13031a9467b802261
NODE_INDEX.md                609e7bdc29e0a5c29e2201bed0c8a616b9777d7239e68b3d708cc601e5f6c2db
GRAPH.mmd                    29bef181c1b629c7b93ad1e57c11de18d43b161667bde8157efc7ecbab06b456
matching survivors          []
```

## 12. Minimal remaining gates

### 12.1 For `CIRCDIST.sat.instances: PROVED`

1. Bring `CIRCDIST.sat.window` to `PROVED` on an exact claim whose verbatim-repetition, boundary, sector aggregation, detector, and fault-cost scope matches this route. Its current self-contained-proof/frontier and scope residuals remain; this edge does not close them.
2. Turn the selected finite computations into proof-quality, independently checkable certificates. At minimum this must cover the lower-bound/exhaustiveness side of the three selected prefixes, the exported minimum witnesses, and each mechanism-exclusion inequality used by the exact claim. A simulation agreement by itself remains insufficient under the existing instances review ruling.
3. Obtain a fresh end-to-end completion review of the assembled instances node after those certificates and the then-current window premise exist. The reviewer must check the exact claim hash, route implication hash, premise claim/scope, and caveat discharge.
4. Only then may a dispatcher consider a node level-change event to `PROVED`. If the claim or implication changes, the corresponding old hash binding remains evidence but cannot license the new string.

The route implication need not be re-reviewed merely because a premise's level rises, provided the implication string and mathematical scope remain exact. A changed window claim or changed shared model does require re-adjudication of applicability even if the route implication bytes stay fixed.

### 12.2 For `CIRCDIST.sat: PROVED`

After instances is `PROVED`, the root still needs:

1. `CIRCDIST.sat.transfer: PROVED` on its exact then-current claim and inputs;
2. `CIRCDIST.sat.window: PROVED`;
3. `CIRCDIST.sat.instances: PROVED`;
4. synchronized root housekeeping for the now-installed child edge; and
5. a fresh independent root completion adjudication after all premise hashes, levels, and scopes are current.

The root's existing route implication is `PROVED`, but that conditional composition cannot promote non-`PROVED` premises. This report is not a substitute for the fresh root adjudication.

## 13. Limitations

1. I did not rerun the 247-file proposer package, the 29-file independent review package, Stim, HiGHS, the min-plus engine, or exhaustive witness searches. I inspected their stated methods, exact finite outputs used for the route, scope fences, and the prior independent review chain.
2. I did not re-prove the universal window theorem. The route is conditional on its exact claim and therefore may be `PROVED` while the premise remains `CERTIFIED*`.
3. I independently checked the finite-to-tail logic, the Pauli-product collision proof, the selected-prefix arithmetic, detector-scope bridge used by BB through `R=d`, route semantics, hash binding, and machine validation. Structural validators cannot determine mathematical truth or reviewer independence; those are supplied by this report's public audit.
4. The exact instances claim's phrase “for each instance” is discharged here by the three selected claim-witness schedules, not by every bonus table row. This matches the existential family clauses and preserves the node's explicit `d=9` and `d=7` standard caveats.
5. Because the commission forbids changing the root, its existing missing-edge frontier text and `RI-C2` sentence will become stale after dispatcher application. That separate bookkeeping debt is disclosed, not silently repaired.
6. No conclusion here supports arbitrary detector-split invariance, non-uniform fault costs, a non-group location fault set, cross-round idle compression, the conjectured family law, or global absence of temporal-boundary-limited schedules.

## 14. FIX-2 command, scratch, process, and mutation accounting

### 14.1 Execution model

- One reviewer session only; **no sub-agents**, delegation, background jobs, detached jobs, shell job control, or handed-off processes.
- Every OS command ran in the foreground through the ordinary `exec_command` shell wrapper with `login: false`.
- Commands using Python started one foreground `python3` process. Unless separately named below, those scripts used only in-process standard-library/PyYAML operations and started no child process.
- No command wrote a repository log. Command stdout/stderr exists only in the tool transcript.

### 14.2 Complete command ledger

1. `python3 - <<'PY'` — print working directory and inventory protocol/node/review/artifact/validator paths.
2. `python3 - <<'PY'` — compute byte counts, SHA-256 values, symlink flags, and inodes for core inputs.
3. `python3 - <<'PY'` — inventory `tools/`, `circdist/tools/`, and migration-maintenance files.
4. `python3 - <<'PY'` — read protocols, manifest, and three target nodes (stdout was tool-truncated; no process survived).
5. `python3 - <<'PY'` — read manifest and exact instances/window nodes with line numbers.
6. `python3 - <<'PY'` — index headings and F-ROUTE/F-LEVEL/R5/second-review locators in the V3 report.
7. `python3 - <<'PY'` — read V3 P8, F-ROUTE, F-LEVEL, authorization, and FIX-2 sections.
8. `python3 - <<'PY'` — read `FILE_PROTOCOL.md` with line numbers.
9. `python3 - <<'PY'` — locate hash/review/route/previous-state rules across protocol and validator sources.
10. `python3 - <<'PY'` — read validator, schema, evidence-closure, and migration implementation ranges.
11. `python3 - <<'PY'` — inspect existing route-added/review-completed patterns and single-premise PROVED routes.
12. `python3 - <<'PY'` — index relevant headings/terms across instances, window, root assembly/reviews/adjudication (stdout tool-truncated only).
13. `python3 - <<'PY'` — read the load-bearing instances dossier sections and finite tables.
14. `python3 - <<'PY'` — read the independent instances review, licence, caveats, and limitations.
15. `python3 - <<'PY'` — read the window theorem, amendment, and review sections (stdout tool-truncated only).
16. `python3 - <<'PY'` — locate and read root R5/window-to-instances contexts (stdout tool-truncated only).
17. `python3 - <<'PY'` — list all current circdist route ids, premises, and levels.
18. `python3 - <<'PY'` — read the exact transfer claim, caveats, level, summary, and frontier.
19. `python3 - <<'PY'` — read Lemma 2.9, detector bridges, and bridge-fold review contexts (stdout tool-truncated only).
20. `python3 - <<'PY'` — recompute instances claim hash and an initial candidate implication hash/YAML round trip.
21. `python3 - <<'PY'` — read governing S3-prime amendment lines 24–150.
22. `python3 - <<'PY'` — recompute the final exact implication's 1,310-character hash and YAML round trip.
23. `git status --short --untracked-files=all` — read pre-existing dirty/untracked state; this started one foreground `git` process under the shell wrapper and modified nothing (stdout tool-truncated only).
24. `PYTHONDONTWRITEBYTECODE=1 python3 tools/proof_dag_check.py --problem circdist` — baseline structural validation.
25. `PYTHONDONTWRITEBYTECODE=1 python3 tools/evidence_closure_check.py --problem circdist` — baseline evidence closure.
26. `PYTHONDONTWRITEBYTECODE=1 python3 tools/check_circdist_migration.py` — baseline migration preservation.
27. `PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'` — create disclosed scratch, copy required trees, write locator placeholder, install exact candidate node in scratch.
28. `PYTHONDONTWRITEBYTECODE=1 python3 tools/proof_dag_check.py --problem circdist --write-generated` in scratch — regenerate scratch views and validate.
29. `PYTHONDONTWRITEBYTECODE=1 python3 tools/proof_dag_check.py --problem circdist --previous-state <repo>` in scratch — retention validation.
30. `PYTHONDONTWRITEBYTECODE=1 python3 tools/evidence_closure_check.py --problem circdist` in scratch — candidate closure validation.
31. `PYTHONDONTWRITEBYTECODE=1 python3 tools/check_circdist_migration.py` in scratch — candidate migration preservation.
32. `PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'` — assert unchanged claims/levels, route/review hash match, and print generated diffs.
33. `PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'` — run four negative validator mutations in scratch and restore the positive candidate.
34. `PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'` — print the exact unsupported-`dependencies` error and restore scratch.
35. `python3 - <<'PY'` — inspect `check_event_append_only.py` CLI lines 180–209.
36. `PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'` — print exact YAML-ready route, assessment, frontier, and event structures from scratch.
37. `python3 - <<'PY'` — remove `/tmp/circdist_sat_instances_window_edge_review_20260826`; printed `False` for survival.
38. `python3 - <<'PY'` — recompute untouched canonical hashes, check report absence before creation, scratch absence, and matching processes. This Python process started one foreground `ps -axo pid=,ppid=,command=` child and waited for it; output `matching_survivors []`.
39. `python3 - <<'PY'` — first post-report integrity attempt. It tried to read the commissioned absolute report path, failed with `FileNotFoundError`, and exited 1 before reaching its declared `ps` subprocess or any write. This exposed that the path-relative `apply_patch` call had placed the report under the conversation working directory rather than the commissioned repository.
40. `python3 - <<'PY'` — search only the commissioned repository and conversation working tree for the exact report basename; found one misplaced 52,578-byte copy and no commissioned-path copy.
41. `python3 - <<'PY'` — atomically move that sole copy to the exact commissioned path and remove the two empty transient directories `discovery-new-algorithms/circdist/reviews` and `discovery-new-algorithms/circdist`; confirmed source absent and target present.
42. `python3 - <<'PY'` — update this sole report's FIX-2 ledger to disclose commands 39–41 and predeclare command 43; no other file is written.
43. Final post-report read-only integrity command, declared before execution: `python3 - <<'PY'` to hash this report, verify scratch and the misplaced path remain absent, verify the five canonical hashes from §11.6 remain unchanged, and run/wait for one foreground `ps -axo pid=,ppid=,command=` child. Its outputs are returned in the dispatcher handoff; it makes no write.

### 14.3 Scratch and logs

- Scratch created: `/tmp/circdist_sat_instances_window_edge_review_20260826`.
- Scratch contents created by this worker: copies of `tools/`, `circdist/`, `maintenance/`, `DAG_PROTOCOL.md`, `FILE_PROTOCOL.md`; one placeholder review; one modified candidate node; regenerated candidate views. All were outside the repository root.
- Scratch deletion: command 37 used `shutil.rmtree`; command 38 confirmed the path was absent.
- Durable scratch survivors: none.
- Path-resolution incident: the non-OS `apply_patch` call initially created this report at `<home>/Documents/Codex/2026-08-07/i-have-connected-an-old-windows/outputs/Windows-SSD-Recovery-2026-08-07/Research-Projects/discovery-new-algorithms/circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md`, outside the commissioned repository. Command 39 caught the absence at the target path; command 40 located the sole misplaced copy; command 41 moved it to the exact commissioned path and removed both empty transient directories. No misplaced file or directory survived. This was a transient path mistake, not an undisclosed second durable artifact.
- New log files: none.
- Background/detached processes: none requested or started.

### 14.4 Process and mutation accounting

- Commands 1–22 and 35–37 launched only their foreground shell wrappers and one foreground `python3` each.
- Command 23 launched its foreground wrapper and one foreground `git` child.
- Commands 24–34 launched their foreground wrappers and one foreground `python3` each; the validators and in-process schema calls started no reviewer-controlled subprocess.
- Command 38 launched its foreground wrapper, one `python3`, and one waited-for foreground `ps` child. It found no surviving audit process.
- Command 39 launched its foreground wrapper and one `python3`; it exited 1 at `read_bytes()` before starting the planned `ps` child and made no write.
- Commands 40–42 each launched their foreground wrappers and one `python3`; command 41 moved the sole report and removed empty transient directories, and command 42 edited only this report.
- Command 43 is the final post-report OS check and is predeclared above; it launches one foreground wrapper, one `python3`, and one waited-for foreground `ps` child, and makes no write.
- Non-OS mutation action: one path-relative `apply_patch` tool call created the report text at the conversation working directory. The tool call targeted no pre-existing file, but its resolved location was wrong; commands 39–41 detected and corrected that mistake. No second copy survives.
- Durable repository files written by this reviewer at handoff: exactly `circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md` in the commissioned repository.
- Canonical nodes, protocols, scheduler, existing artifacts/reviews, migration records, source packages, and generated views written by this reviewer: **none**.

