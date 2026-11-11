# `CIRCDIST.sat` V3 exact-text and strict-protocol review

**Date:** 2026-08-26  
**Reviewer:** OpenAI GPT-5.6-sol, fresh single-worker review context, one authorized budget box, no sub-agents  
**Target:** `CIRCDIST.sat` claim, route `asymptotic-stability-assembly`, and their exact assessment consequences  
**Authorization:** current-thread lead ruling `可以 去吧`, recorded at `operations/circdist/SCHEDULER.yaml`, round `47-v3-authorized`  
**Governing protocol:** repository-root `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md`, sourced from the 2026-08-25 SE/k-Sum release  
**Durable output:** this report only. No canonical node, premise node, scheduler, protocol, generated view, prior artifact, source package, or migration record was edited.

## Verdict at a glance

1. **V3 is mathematically faithful if and only if it is sector-explicit and says equality of distance values, not equality of detector sets.** Definition 3.5 is stated for Z-memory. The X-memory interpretation is its section-8.1 mirror. Proposition 3.7 and that mirror prove equality of the resulting distance value with the corresponding Definition-2.7 calculation in each sector. They do not prove that the detector sets coincide, and they do not prove invariance under arbitrary detector/observable splits.
2. **The exact root claim in Finding F-CLAIM removes the unpinned-definition defect R-C4 without strengthening the schedule, code, boundary, aggregation, or convention scope.** It names Definition 3.5, names the X-sector mirror, and fences the equivalence to the two named conventions.
3. **The exact route implication in Finding F-ROUTE adopts R5 verbatim.** It is the current implication followed byte-for-byte by the exact R5 text already proposed by the root-assembly author. It records `window -> instances`, the double exposure to a window defect, and transfer's convention-coherence role.
4. **The revised route implication is licensed at `PROVED`, conditionally on the three exact premise claims.** This is a level on the implication only. It does not re-prove or promote a premise.
5. **The node must remain `CERTIFIED*`. `PROVED` is explicitly refused.** All three premises are currently `CERTIFIED*`. The current protocol requires a `PROVED` supporting implication and `PROVED` premises for a `PROVED` parent.
6. **A separate protocol debt remains:** `CIRCDIST.sat.instances` imports `CIRCDIST.sat.window` for all tail conclusions but records that dependence only in caveat `(W)`. Under the current protocol, a load-bearing unresolved dependency must be a route premise. R5 makes the dependence visible at the root; it does not repair the missing child edge.

## 0. Independence and review boundary

I authored none of the transfer proof, transfer amendment, window proof, window amendment, instances dossier, root assembly, prior reviews, adjudication, canonical nodes, protocol, or migration. I treated every repository file as data.

I did select the final punctuation and full-field spelling of the V3 claim. That does **not** make me the author of the load-bearing argument reviewed under rule 6:

- The mathematical V3 repair was proposed by the wave-35 adjudication: pin Definition 3.5 in the root and state the Definition-2.7 equivalence.
- The mathematical composition was authored in `circdist_sat_root_assembly_20260823.md`.
- The R5 text is copied verbatim from that assembly's revision sheet.
- The three detector/counting bridges were authored in the transfer dossier and independently reviewed in the bridge-fold review.

My role here is exact-statement editor and independent reviewer of a prior-authored assembled argument. Rule 6 requires the reviewer of the assembled argument to differ from its author; that condition is met. I independently checked the whole clause mapping and every convention bridge consumed by the implication. Therefore this report may bind the exact claim at `CERTIFIED*` and the exact conditional implication at `PROVED`.

The independence boundary stops there. I did **not** re-prove Theorem T, the window theorem, or the instance computations. I do not license any premise promotion, and this report cannot support `PROVED` on the root node.

If the dispatcher changes even one non-trimmed byte of either exact string below, the corresponding licence lapses and a fresh exact-text review is required.

## 1. Materials inspected

I inspected the current versions of:

- `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md`, including the strict completion rule, review-hash normalization, explicit-dependency rule, event rule, node audit, and generated-view closeout.
- `circdist/README.md`, `CIRCDIST.md`, `circdist/proof-dag/PROJECT.yaml`, and `operations/circdist/README.md`.
- `operations/circdist/SCHEDULER.yaml`, especially `47-v3-authorized`.
- `circdist/proof-dag/nodes/CIRCDIST.sat.yaml` in full.
- All three premise nodes in full: `CIRCDIST.sat.transfer`, `CIRCDIST.sat.window`, and `CIRCDIST.sat.instances`.
- Frozen `CIRCDIST_PROBLEMS.md` and `SAT_RESCOPE_20260822.md`.
- The root assembly, root review, and root PROVED/CERTIFIED* adjudication.
- The transfer proof's Definitions 2.1-2.11, Lemma 2.9, Definitions/Propositions 3.1-3.7, section 8.1, residual T-G1 through T-G5, and its assembly paragraph.
- Transfer Amendment 1's Definition-3.5 ratification, rejected mitigation, corrected safe condition, and counterexample.
- The transfer bridge-fold review, including its independent derivations, computations, exact folded claim, caveat audit, and limits.
- The window theorem's model, Definition-2.7-style detector set, proof structure, Amendment 1, and review, including the later-refuted overbroad last sentence of S3-prime.
- The instances dossier and its review where they state and use the window import.
- The current validator implementation in `tools/proof_dag_schema.py`, `tools/proof_dag_check.py`, and the migration/evidence-closure checks.
- `maintenance/circdist_protocol_20260826/REPORT.md` and the migration checker results.

Key source byte hashes recomputed in this session:

| Source | SHA-256 |
|---|---|
| frozen questions | `5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64` |
| SAT rescope | `6c8ec4362f728713f9934d5f0b8041195f66434ebe283a69e67147b3c7009d7f` |
| root assembly | `68babfe69cd1c988c897839466fdb3ddfd24802eb4e77667ac1ad53551edaead` |
| root review | `5e1fd365ce330a89c4f11c86cba3ac180446cb51a84c9a62b5eb8b004ec61579` |
| root adjudication | `7b05b8f4509c51cde1407c5329e91b13abb33770d290df2fc4eab550a48e38d4` |
| transfer bridge fold | `9f5f93426b0f6cbf140339c30695ae6922ae5968001ddc9b5884b3dce3d84199` |
| transfer proof | `4fce5371edc09fa153b41f6735d521d31500b84b55a0059c8b42dc000651da30` |
| transfer Amendment 1 | `6c7a8fb756cfba958f82c70f739ffa90aee19070c2cae8f358d44ccdc20ad07e` |

## 2. Reviewed-hash pipeline check

The current validator defines:

```python
def claim_hash(claim: str) -> str:
    frozen = claim.replace("\r\n", "\n").strip()
    return "sha256:" + hashlib.sha256(frozen.encode("utf-8")).hexdigest()
```

The value is computed over the YAML-loaded claim or implication string, after CRLF-to-LF normalization and outer whitespace stripping. Interior spaces and line breaks that survive YAML loading are significant.

Before trusting any prior review, I loaded the current project with the repository loader and recomputed every current-schema `reviewed_hash` attached to a node claim or route implication:

```text
reviewed_hash entries checked: 18
mismatches: 0
```

The current target bindings reproduced exactly:

| Object | Level | Current hash |
|---|---:|---|
| `CIRCDIST.sat` claim | `CERTIFIED*` | `sha256:c6205671936488f9ccbf69d68d9893b549098244bd5f95985b4a682df0d8bdd9` |
| root route implication | `CERTIFIED*` | `sha256:78737cc3040a78a1afe8d7bab7537e2200a84175578d2407d90d569a1bbe95a1` |
| transfer premise claim | `CERTIFIED*` | `sha256:8fb50ff01b6465e9c660fc61292958828f448dd740757a8945deae1e107c7ad3` |
| window premise claim | `CERTIFIED*` | `sha256:8698b051b15fa14ff669299580d9b7bfec01808c0a34133ef09264e749466146` |
| instances premise claim | `CERTIFIED*` | `sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3` |

Current-state validators, before this report was written:

```text
python3 tools/proof_dag_check.py --problem circdist
  circdist: 16 node files structurally valid

python3 tools/proof_dag_check.py --problem all
  se: 85 node files structurally valid
  ksum: 144 node files structurally valid
  circdist: 16 node files structurally valid

python3 tools/evidence_closure_check.py --problem circdist
  circdist: evidence closure OK, 114 structured paths; all evidence project-local and linked

python3 tools/check_circdist_migration.py
  Migration preservation OK: 16 nodes, 143 original events, 728 byte-identical copies
```

This validates the byte-binding pipeline and current structure. It does not establish any mathematical conclusion by itself.

## 3. Definitions and premises used in this review

### P1. Root experiment and aggregation

The V2 root already pins ideal initialization, ideal final data readout, `R` verbatim repetitions, min-over-sectors aggregation, the limit, and the minimum-form stabilization index. V3 must preserve all of those bytes in mathematical content.

### P2. Definition 2.7 in Z-memory

For Z-memory, the named set contains the full interval of Z-check difference detectors

```text
D_{b,r} = m_{b,r} + m_{b,r-1},  b in B, r = 0,...,R,
```

including both temporal ends, and the partial interval of X-check difference detectors

```text
D_{a,r} = m_{a,r} + m_{a,r-1},  a in A, r = 1,...,R-1.
```

The observables are terminal logical readout parities. The X-memory set is the sector mirror.

### P3. Definition 3.5

In Z-memory, first restrict to deterministic record parities `V`. A parity belongs to the canonical detector space `D` precisely when its value is constant across the family of experiments obtained by varying the prepared logical-basis label. This selects record information that does not reveal the logical input. Definition 3.5 is well posed because the logical-state dependence is a linear map on `V`, so `D` is its kernel.

Definition 3.5 is written for Z-memory. The X-memory meaning used in the route is the direct section-8.1 mirror: swap the check families, Pauli types, CNOT control/target roles, preparation/readout bases, and logical-basis family.

### P4. Z-sector bridge

Proposition 3.6 gives

```text
D = D_Z direct-sum D_X,
D_Z = span{D_{b,r}: r = 0,...,R},
D_X = V_X.
```

The Definition-2.7 set can be strictly smaller than `D`: for dependent X-check generators it omits the round-zero redundancy parities in `D_X`.

Let `Pi_X` retain each Pauli fault's X component and each Z-check record flip, and delete Z components and X-check record flips. Then:

1. `Pi_X` preserves every Z-check record flip and terminal Z-readout observable flip.
2. `Pi_X` annihilates every X-check record parity, including the omitted redundancy directions.
3. Its block/location weight does not increase because the full Pauli group is available at each location under uniform unit cost.

Set inclusion gives `d^(2.7) <= d^D`. Applying `Pi_X` to a minimum Definition-2.7 witness gives a canonical-detector-undetectable logical witness of no greater weight, so `d^D <= d^(2.7)`. Hence the two **values** are equal in Z-memory.

### P5. X-sector bridge

The mirror is valid at the exact root scope:

1. Legality is symmetric.
2. Measurement consistency is mirror-stable because `c_ab + c'_ab` equals the even CSS overlap, hence `c_ab = c'_ab` over `F_2`.
3. The full/partial detector intervals exchange with the check families.
4. The mirrored projection `Pi_Z` preserves the X-memory relevant records/observables and annihilates the opposite-family record space.

Thus the same two inequalities hold for `d_R^X`, with any omitted redundancy directions controlled by `leftker(H_Z)`. The bridge-fold reviewer also constructed X-memory directly rather than relying only on relabelling. Therefore “equivalently Definition 2.7” is justified in both sectors at the root's exact schedule, boundary, fault, and aggregation scope.

### P6. What is not proved

The bridge does not show the two detector sets are equal. In dependent-generator cases they are not. It also does not show arbitrary convention independence.

The decisive counterexample is Steane plus a redundant X row with

```text
D-prime = span{D_{b,r}} + span{D_{a,r}} + span{P_X + lambda}.
```

This is a genuine complement inside the full deterministic parity space and contains the Definition-2.7 set, yet

```text
R = 2: d^(2.7) = 2, d^(D-prime) = 3
R = 3: d^(2.7) = 2, d^(D-prime) = 4.
```

The published dimension quintuple is `28/22/21/12/20`. The bridge-fold review independently reproduced it and also found `d^D = d^(2.7) = 2` on that same instance. This simultaneously validates the named-pair equality and refutes any general-split reading.

The safe condition is

```text
span{D_{b,r}} subseteq D-prime subseteq D,
```

not merely `D-prime subseteq V`.

### P7. Counting bridge

The window artifact counts elementary-fault multisets, while transfer and instances count occupied faulty locations. Lemma 2.9 equates the minima because propagation/effect is `F_2`-linear and each location carries a full Pauli group: colliding faults at one location can be multiplied into one assignment without changing the effect and with lower count. Uniform unit cost and group closure are load-bearing. The bridge is already in the exact transfer claim and hash-bound to the bridge-fold review.

### P8. Window and instances dependence

The window claim is `CERTIFIED*`. It asserts monotonicity, existence of the limit, the contiguous-span bound, `R_stab <= d_infinity <= d`, and `d_R = d_d = d_infinity` for `R >= d`, hence the first `d` distances decide the pair.

The instances claim is `CERTIFIED*`. Its caveat `(W)` says every conclusion outside its computed windows imports the window theorem. Its own dossier says no reported finite-window value depends on Theorem T because every transfer-engine value used there was independently reproduced, but the infinite tail does depend on `window`.

Therefore the actual risk structure is `window -> instances`, with transfer alongside for the root's exact evaluator and convention coherence. This is R5/R-C12. The current graph does not encode the child edge on `CIRCDIST.sat.instances`; prose alone does not satisfy the current protocol's explicit-dependency rule.

## 4. Counterexample and ambiguity attacks

| Candidate wording or reading | Verdict | Reason |
|---|---|---|
| “measured against the canonical detector split” | reject | It leaves the numbered space unpinned and repeats R-C4. |
| “Definition 3.5, equivalently Definition 2.7” | reject bare | It can be misread as equality of sets; only distance values are equal. |
| “invariant under detector conventions” | reject | False on the recorded `D-prime` counterexample. |
| Name Definition 3.5 only in Z-memory | reject | The root aggregates both sectors; the X-memory mirror is nondecorative on BB where `dim leftker(H_Z)=2`. |
| Put “lead-ratified” in the mathematical claim | reject | Ratification is provenance/status, not part of the proposition. It stays in R-C4 and the event. |
| Delete R-C4 after V3 | reject | The unpinned defect is discharged, but convention sensitivity, the lead-decision provenance, the safe condition, and the counterexample remain audit-relevant scope notes. |
| Claim all three premises are independent | reject | Instances imports window outside computed windows. |
| Treat R5 as the missing child DAG edge | reject | R5 documents risk at the root but does not add `window` as a premise of an instances route. |
| Promote the root because V3 closes R-C4 | reject | The current strict rule separately requires all three premises to be `PROVED`; they are `CERTIFIED*`. |
| Rewrite the route implication more aggressively | reject | The exact current implication plus the prior-authored R5 is sufficient and preserves reviewer independence from implication authorship. |

## 5. Finding F-CLAIM — exact V3 root claim

**APPLY**, exactly as the YAML-loaded string below:

```text
For a fixed legal single-round single-ancilla CSS syndrome-extraction schedule M under ideal initialization and final data readout, let d_R(M) be the minimum over the two CSS memory-sector circuit distances after R verbatim repetitions of M, with the Z-memory distance measured against the canonical detector space of Definition 3.5 in the CIRCDIST.sat.transfer proof dossier and the X-memory distance measured against its section-8.1 mirror. Proposition 3.7 and that mirror give the same distance value in each sector when the corresponding Definition-2.7 detector set is used; this says neither that the two detector sets are equal nor that the value is invariant under any other detector/observable split. Define d_infinity(M) = lim_{R to infinity} d_R(M) and R_stab(M) = min{R_0 : d_R(M) = d_infinity(M) for all R >= R_0}. Give a finite-state min-plus representation of d_R, prove an explicit finite-window theorem and algorithm deciding (d_infinity,R_stab), compute or rigorously bound that pair for a standard surface-code schedule, a legal hook-misaligned surface-code schedule, and at least one qLDPC schedule, and attribute the distance-limiting mechanism using auditable minimum witnesses.
```

Expected normalized hash:

```text
sha256:ed57c5f052cc009d29f8682c13512a6930f8eee68c0c8ec8f845b46660dba0fb
```

The exact wording preserves V2's substantive scope, pins the third load-bearing convention axis, makes the two-sector semantics explicit, and refuses arbitrary convention independence. It is a scope repair of the existing proposition, not a new node identity.

Recommended YAML serialization:

```yaml
claim: >-
  For a fixed legal single-round single-ancilla CSS syndrome-extraction schedule M under ideal initialization and final data readout, let d_R(M) be the minimum over the two CSS memory-sector circuit distances after R verbatim repetitions of M, with the Z-memory distance measured against the canonical detector space of Definition 3.5 in the CIRCDIST.sat.transfer proof dossier and the X-memory distance measured against its section-8.1 mirror. Proposition 3.7 and that mirror give the same distance value in each sector when the corresponding Definition-2.7 detector set is used; this says neither that the two detector sets are equal nor that the value is invariant under any other detector/observable split. Define d_infinity(M) = lim_{R to infinity} d_R(M) and R_stab(M) = min{R_0 : d_R(M) = d_infinity(M) for all R >= R_0}. Give a finite-state min-plus representation of d_R, prove an explicit finite-window theorem and algorithm deciding (d_infinity,R_stab), compute or rigorously bound that pair for a standard surface-code schedule, a legal hook-misaligned surface-code schedule, and at least one qLDPC schedule, and attribute the distance-limiting mechanism using auditable minimum witnesses.
```

## 6. Finding F-ROUTE — exact implication and level

**APPLY** the following full implication. Its first sentence is the current implication. Its last two sentences are R5 copied verbatim from the prior root assembly.

```text
The transfer representation supplies a finite exact computational model, the window theorem proves that a bounded prefix decides d_infinity and R_stab, and the instance dossier applies both to every named code family with witness-level mechanism attribution; together these three premises establish every clause of the revised root claim. The premises are not independent: instances imports window's window theorem for every statement outside its computed windows, and the three unit-fault counting conventions are reconciled by transfer Lemma 2.9. A defect in window propagates to two premises; the transfer premise is load-bearing for convention coherence even though no reported instance value depends on Theorem T.
```

Expected normalized hash:

```text
sha256:03549fb0f9856952319ee3dfc1d9bdbb11e49a47a9babbc65b7b9f87405763e1
```

### Clause audit

| Root clause | Exact support | Result |
|---|---|---|
| model preamble and `d_R` | all three claims, with transfer Lemma 2.9 and Prop 3.7/section-8.1 bridges | complete |
| finite min-plus representation | transfer claim | complete conditional on that premise |
| finite-window theorem | window claim | complete conditional on that premise |
| algorithm deciding the pair | construct `d_1,...,d_d` by transfer; correctness and stopping window from window | complete conditional on both premises |
| standard surface schedule | instances claim | complete in its existential reviewed scope |
| legal hook-misaligned surface schedule | instances claim | complete in its existential reviewed scope |
| at least one qLDPC schedule | instances claim | complete in its existential reviewed scope |
| witness-level mechanism attribution | instances claim | complete for the three named schedules; no general temporal-boundary-emptiness statement imported |
| Definition-3.5/2.7 value equality | transfer claim, per sector | complete; no set equality or other-split invariance |
| internal dependence | R5 plus instances caveat `(W)` | accurately disclosed |

### Implication level

**APPLY `routes.asymptotic-stability-assembly.assessment.level: PROVED`.**

This is a proof of the conditional implication, not a proof of the premises. The current protocol explicitly separates those obligations and permits the implication to be reviewed before premises are settled. The exact implication is prior-authored text, and this fresh reviewer independently checked the whole load-bearing composition.

## 7. Finding F-LEVEL — node level and remaining gates

### Node level

**KEEP/APPLY `assessment.level: CERTIFIED*`.**  
**DO NOT APPLY `assessment.level: PROVED`.**

Current premise levels:

| Premise | Level | Material caveat/gate |
|---|---:|---|
| `CIRCDIST.sat.transfer` | `CERTIFIED*` | Theorem T core not end-to-end re-adjudicated at `PROVED`; general statement rests on reviewed derivations; model correspondence and unit-cost scope notes remain. |
| `CIRCDIST.sat.window` | `CERTIFIED*` | Exact universal claim still has a self-contained-proof/frontier gate; compressed cross-round layouts are outside the argued verbatim scope and the current child claim/caveat wording remains imperfect. |
| `CIRCDIST.sat.instances` | `CERTIFIED*` | Tail conclusions import window; computations and exact search are reviewed only in stated scopes; the load-bearing window dependency is not a machine-visible child route. |

The strict rule is mechanical and semantic: a `PROVED` parent requires a `PROVED` route implication and `PROVED` premises. V3 supplies the scope pin and this report can supply the implication review; it cannot promote any premise by inheritance, approval, or composition.

Minimal honest remaining gates for root `PROVED`:

1. Encode `CIRCDIST.sat.window` as an explicit premise of a route on `CIRCDIST.sat.instances`, with an exact implication and independent review. Do not treat caveat `(W)` or root R5 as the edge.
2. Bring `CIRCDIST.sat.window` to `PROVED` on an exact claim whose verbatim-repetition scope matches the proof, via a self-contained proof and fresh independent review.
3. Bring `CIRCDIST.sat.transfer` to `PROVED` via an end-to-end independent review of Theorem T's core and the applicability of every registered external/model input at the exact claim scope.
4. Bring `CIRCDIST.sat.instances` to `PROVED` only with proof-quality/checkable certificates satisfying the frozen “simulation does not substitute for proof” rule, after the window dependency is explicit and established at the required level.
5. After all three premise hashes and levels are current, commission a fresh root completion adjudication. No future promotion may rely on this report alone for premise truth.

## 8. Existing review bindings after application

### Bindings that lapse

- The current root-claim review binding at `sha256:c6205671...` lapses when Finding F-CLAIM is applied.
- The current route-implication review binding at `sha256:78737cc3...` lapses when Finding F-ROUTE is applied.
- The wave-35 adjudication also discusses and hashes the old V2 claim/old implication. It remains probative history but cannot be rebound to the new strings without a new review.

Do not rewrite an old report's `reviewed_hash` to the new value. Move the old route review link to `basis.evidence` with `kind: text`. The root already retains the root review and adjudication as evidence entries; keep those evidence links.

### Bindings that remain valid

- Transfer claim and bridge-fold binding `sha256:8fb50ff0...` remain valid; transfer claim bytes do not change.
- Window bindings `sha256:8698b051...` remain valid; window claim bytes do not change.
- Instances binding `sha256:c71ac7cd...` remains valid; instances claim bytes do not change.
- Every unrelated node/review binding remains unchanged.

### New bindings

- New root claim -> this report, locator `Finding F-CLAIM`, reviewed hash `sha256:ed57c5f0...`.
- New route implication -> this report, locator `Finding F-ROUTE`, reviewed hash `sha256:03549fb0...`.

## 9. Exact canonical field replacements licensed

The snippets below are exact field content. Unmentioned caveats, evidence links, routes, premises, assumptions, and node levels stay unchanged.

### 9.1 Replace root R-C4 exactly

```text
R-C4: the root claim now pins the detector convention to the canonical detector space of Definition 3.5 in the CIRCDIST.sat.transfer proof dossier, using its section-8.1 mirror in the X-memory sector. Proposition 3.7 and that mirror establish equality only of the resulting per-sector distance values with those obtained from the corresponding Definition-2.7 detector sets; the detector sets need not be equal, and no invariance under other detector/observable splits is claimed. Definition 3.5 remains a lead-ratified reading of the frozen 公共定义 (verbatim "批准 Definition 3.5, 缓解条款不批"), not a derivation from that text. The corrected safe condition is span{D_b,r} within D-prime within D (containment in D, not in V); W-G3 must not be carried and S3-prime is load-bearing. Convention sensitivity is witnessed by Steane plus a redundant X row, where D-prime = span{D_b,r} + span{D_a,r} + span{P_X + lambda} gives d^D-prime = 3 at R = 2 and 4 at R = 3, against d^2.7 = 2. V3 discharges the former unpinned-definition defect; the former proposer-level flags on transfer Proposition 3.7, its section-8.1 mirror, and transfer Lemma 2.9 remain discharged by the hash-bound transfer bridge fold. This caveat is now a scope and provenance note, not an unresolved detector convention inside the root claim.
```

### 9.2 Replace the node assessment summary exactly

```text
V3 pins d_R to the Definition-3.5 canonical detector space in Z-memory and its section-8.1 mirror in X-memory, while stating only the reviewed equality of per-sector distance values with the corresponding Definition-2.7 sets. The revised route implication records the window-to-instances dependence and the transfer premise's convention-coherence role, and its conditional implication is independently reviewed at PROVED. The root remains CERTIFIED* under the 2026-08-25 protocol because all three premises remain CERTIFIED*; PROVED requires a PROVED implication and PROVED premises. The shared-model, transfer-scope, window, and finite-instance caveats remain in force.
```

### 9.3 Replace `assessment.basis.reviews` exactly

```yaml
reviews:
- path: circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md
  kind: review
  scope: Fresh independent V3 audit of detector-space semantics and both CSS-sector bridges, the exact hash pipeline, the eight-clause root composition, caveat propagation, R5, and the strict 2026-08-25 completion rule; it reviews the assembled implication but does not re-prove any premise dossier.
  locator: Finding F-CLAIM
  reviewed_hash: sha256:ed57c5f052cc009d29f8682c13512a6930f8eee68c0c8ec8f845b46660dba0fb
```

Keep `assessment.basis.routes` unchanged. Keep the existing `assessment.basis.evidence` list unchanged; it already retains the old root review and adjudication as evidence.

### 9.4 Replace the route proof block exactly

```yaml
proof:
  sketch: Use the eight-clause discharge and six-axis convention audit in the root assembly, together with the later transfer bridge fold and the V3 exact-text review, to derive the exact root claim from the three exact premise claims. The window premise is used both directly and through the instances tail conclusions; the transfer premise supplies the elementary-fault/location-count and Definition-2.7/Definition-3.5 bridges.
  sources:
  - path: circdist/artifacts/definitions/SAT_RESCOPE_20260822.md
    kind: text
  - path: circdist/artifacts/circdist_sat_root_assembly_20260823.md
    kind: text
  - path: circdist/reviews/circdist_transfer_bridgefold_20260823.md
    kind: text
```

### 9.5 Replace the entire route assessment exactly

```yaml
assessment:
  level: PROVED
  caveats:
  - 'RI-C1: this PROVED assessment is only for the conditional implication from the three exact premise claims to the exact V3 root claim. It neither promotes nor independently re-proves a premise; all three premises remain CERTIFIED*, so the root remains CERTIFIED*.'
  - 'RI-C2: the premises are not independent. CIRCDIST.sat.instances imports CIRCDIST.sat.window for every conclusion outside its computed windows, and that load-bearing child dependency is not yet encoded as a route on CIRCDIST.sat.instances. R5 makes the dependency explicit in this implication but does not repair the missing child edge.'
  - 'RI-C3: detector alignment means equality of per-sector distance values only for Definition 3.5 and the corresponding Definition-2.7 set, not equality of detector sets or invariance under other splits. Fault-count alignment uses Lemma 2.9 and therefore the uniform unit-cost, full per-location Pauli-group model.'
  summary: Fresh V3 exact-text review verifies the complete conditional composition: the transfer premise supplies the finite exact model and both convention bridges, the window premise supplies the finite decision theorem, and the instances premise supplies the three existential instance clauses and witness-level attributions. The verbatim R5 addition states the window-to-instances dependence and the transfer premise's convention-coherence role. PROVED applies to this implication only; premise truth and premise levels were not re-adjudicated.
  basis:
    reviews:
    - path: circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md
      kind: review
      scope: Fresh independent review of the complete clause mapping and six convention axes after the V3 scope pin and verbatim R5 insertion, including the window-to-instances dependence, Lemma 2.9 counting bridge, Proposition 3.7 and the section-8.1 mirror; premise truth and premise levels were not re-adjudicated.
      locator: Finding F-ROUTE
      reviewed_hash: sha256:03549fb0f9856952319ee3dfc1d9bdbb11e49a47a9babbc65b7b9f87405763e1
    evidence:
    - path: circdist/artifacts/circdist_sat_root_assembly_20260823.md
      kind: text
    - path: circdist/reviews/circdist_sat_root_review_20260823.md
      kind: text
    - path: circdist/reviews/circdist_sat_root_proved_adjudication_20260823.md
      kind: text
    - path: circdist/reviews/circdist_transfer_bridgefold_20260823.md
      kind: text
```

This replacement removes the stale route caveat saying three bridges are proposer-level. That statement is false after the transfer fold and wave-35 re-adjudication.

### 9.6 Replace the entire root frontier exactly

```yaml
frontier:
  instances-window-edge:
    task: Encode CIRCDIST.sat.window as an explicit premise of a reviewed route on CIRCDIST.sat.instances; the existing caveat and R5 prose record the dependency but do not satisfy the protocol's machine-visible dependency rule.
    kind: gate
    since: '2026-08-26'
  premise-proved-gates:
    task: Before considering CIRCDIST.sat for PROVED, bring CIRCDIST.sat.transfer, CIRCDIST.sat.window, and CIRCDIST.sat.instances to PROVED on their then-current exact claims and commission a fresh root completion adjudication.
    kind: gate
    since: '2026-08-26'
```

The old `detector-split-v3` frontier entry is completed by this review and must not remain as unfinished work.

### 9.7 Append these two research events exactly

The V3 change is a mathematical scope repair, so rule 6 requires a research event. The route level also changes, requiring a separate `level-change` event.

```yaml
events:
  detector-split-v3-2026-08-26:
    date: '2026-08-26'
    type: repair-applied
    summary: The lead-authorized V3 revision pinned d_R to the Definition-3.5 canonical detector space and its section-8.1 X-memory mirror, stated only per-sector equality of distance values with the corresponding Definition-2.7 sets, adopted R5 to expose the window-to-instances dependency, and replaced the completed V3 frontier. The node remained CERTIFIED* because all three premises remain CERTIFIED*.
    sources:
    - path: circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md
      kind: review
      locator: Finding F-CLAIM
    - path: operations/circdist/SCHEDULER.yaml
      kind: text
      locator: 47-v3-authorized
  route-implication-proved-2026-08-26:
    date: '2026-08-26'
    type: level-change
    from: CERTIFIED*
    to: PROVED
    route: asymptotic-stability-assembly
    summary: Fresh independent review established the exact revised conditional implication from the three premise claims to the V3 root claim. No premise level and no node level changed.
    sources:
    - path: circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md
      kind: review
      locator: Finding F-ROUTE
```

If `events` already exists when the dispatcher applies the patch, append these keys without rewriting any existing event.

## 10. Dispatcher authorization table

| Field/action | Authorization | Exact condition |
|---|---|---|
| Replace full root claim | **APPLY** | Exact Finding F-CLAIM string; expected hash `ed57c5f0...`. |
| Replace full route implication | **APPLY** | Exact Finding F-ROUTE string; expected hash `03549fb0...`. |
| Replace route proof block | **APPLY** | Exact §9.4 block. |
| Route level `CERTIFIED* -> PROVED` | **APPLY** | Atomic with new implication, §9.5 assessment, new review binding, and level-change event. |
| Root node level | **APPLY/KEEP CERTIFIED*** | No level change. |
| Root node `PROVED` | **DO NOT APPLY** | Forbidden while any of the three premises is not `PROVED`. |
| Replace R-C4 | **APPLY** | Exact §9.1 string; all other node caveats unchanged. |
| Replace node summary | **APPLY** | Exact §9.2 string. |
| Replace node review basis | **APPLY** | Exact §9.3; old claim reviews stay evidence only. |
| Replace route assessment | **APPLY** | Exact §9.5; old implication review stays evidence only. |
| Replace root frontier | **APPLY** | Exact §9.6. |
| Append V3 repair event | **APPLY** | Exact §9.7 first event. |
| Append route level-change event | **APPLY** | Exact §9.7 second event. |
| Regenerate `NODE_INDEX.md` and `GRAPH.mmd` | **APPLY** | Derived output only, after canonical edit. |
| Promote any premise | **DO NOT APPLY** | Not reviewed here. |
| Add the missing route to `CIRCDIST.sat.instances` | **NEEDS SECOND REVIEW** | It is required protocol repair, but this commission did not author/review its exact child implication. |
| Rewrite any old report hash to a new hash | **DO NOT APPLY** | Preserve old report as evidence; add this report as the new review. |
| Change any scheduler/protocol/source package | **DO NOT APPLY** | Dispatcher owns canonical writes; no such change is licensed by this report. |

## 11. Dry-run validation of the proposed field set

I created a temporary project at:

```text
/tmp/circdist_sat_v3_review_7oye21fe
```

The script copied only the proof-DAG and reviews, symlinked read-only artifact/operations inputs, inserted a temporary report stub with the two locators, applied exactly the strings and field structures in §§5-9, regenerated the two derived views inside the scratch copy, and invoked the repository's `validate_problem` implementation.

Result:

```text
claim_hash sha256:ed57c5f052cc009d29f8682c13512a6930f8eee68c0c8ec8f845b46660dba0fb
implication_hash sha256:03549fb0f9856952319ee3dfc1d9bdbb11e49a47a9babbc65b7b9f87405763e1
node_level CERTIFIED*
route_level PROVED
nodes 16
warnings 0
errors 0
scratch_exists_after_cleanup False
```

This checks serialization, allowed keys, event forms, review locators, hash bindings, completion-level structural rules, and generated-view consistency. It does not replace mathematical review; that is §§3-7.

## 12. Dispatcher validation commands

Apply all authorized canonical edits atomically, then run from the repository root:

```sh
python3 tools/proof_dag_check.py --problem circdist --write-generated
python3 tools/proof_dag_check.py --problem all
python3 tools/evidence_closure_check.py --problem circdist
python3 tools/check_circdist_migration.py
python3 tools/proof_dag_check.py --problem circdist --previous-state maintenance/circdist_protocol_20260826/baseline
git diff --check
```

Then independently reload the node and verify:

```python
from pathlib import Path
import sys
sys.path.insert(0, "tools")
from proof_dag_schema import claim_hash, load_problem
d = load_problem(Path("circdist")).nodes["CIRCDIST.sat"]
assert claim_hash(d["claim"]) == "sha256:ed57c5f052cc009d29f8682c13512a6930f8eee68c0c8ec8f845b46660dba0fb"
r = d["routes"]["asymptotic-stability-assembly"]
assert claim_hash(r["implication"]) == "sha256:03549fb0f9856952319ee3dfc1d9bdbb11e49a47a9babbc65b7b9f87405763e1"
assert d["assessment"]["level"] == "CERTIFIED*"
assert r["assessment"]["level"] == "PROVED"
assert [d["assessment"]["level"] for d in (
    load_problem(Path("circdist")).nodes["CIRCDIST.sat.transfer"],
    load_problem(Path("circdist")).nodes["CIRCDIST.sat.window"],
    load_problem(Path("circdist")).nodes["CIRCDIST.sat.instances"],
)] == ["CERTIFIED*", "CERTIFIED*", "CERTIFIED*"]
```

## 13. Risks and rollback conditions

Abort the installation before canonical acceptance if any of these occurs:

- either recomputed hash differs from the expected value;
- YAML folding introduces an interior newline or extra space into either exact string;
- the old root/route report remains under `basis.reviews` with its old hash, causing a binding mismatch;
- this report's `F-CLAIM` or `F-ROUTE` locator is missing;
- a premise claim or level changed since this audit;
- the dispatcher promotes the node or any premise;
- R-C4 is deleted rather than narrowed;
- the generated views or any validator fail;
- the atomic edit rewrites an old event or touches an unlicensed file.

Before the new events are accepted, rollback means restore the entire root node to its pre-V3 bytes and regenerate the views. After the events have entered the accepted research state, do **not** delete or rewrite them; revert the mathematical fields with a new dated correction/level-change event and retain this report as historical evidence.

## 14. Reproducible command and process ledger

### 14.1 Execution model

Every OS command was launched in the foreground by `exec_command` under the repository root. Some independent read-only commands were submitted together by the orchestration layer, but no shell command used `&`, `nohup`, `disown`, `screen`, `tmux`, or a detached/background process. Every `exec_command` returned an exit code before this report was finalized. No solver, compiler, network client, or mathematical search was started.

Utilities/processes invoked were `zsh`, `pwd`, `rg`, `sed`, `sort`, `git`, `nl`, `wc`, `python3`, and `shasum`. Python imported only repository validator modules and standard-library modules for the checks performed here.

### 14.2 Commands launched

The commands below are the complete command ledger. Repeated `sed` reads are included because FIX-2 asks for every command, not only verdict-bearing commands.

```text
01 pwd
02 rg --files -g 'DAG_PROTOCOL.md' -g 'FILE_PROTOCOL.md' -g '*CIRCDIST*' -g '*circdist*' -g '*migration*' -g '*rescope*' -g '*question*' -g '*assembly*' -g '*review*' -g '*adjudication*' -g '*validator*' -g '*validate*'
03 sed -n '1,320p' DAG_PROTOCOL.md
04 sed -n '1,320p' FILE_PROTOCOL.md
05 rg --files circdist | sort
06 git status --short --branch
07 sed -n '1,360p' 'FILE_PROTOCOL.md'
08 sed -n '1,360p' 'circdist/proof-dag/PROJECT.yaml'
09 sed -n '1,360p' 'circdist/proof-dag/nodes/CIRCDIST.sat.yaml'
10 sed -n '1,360p' 'circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml'
11 sed -n '1,360p' 'circdist/proof-dag/nodes/CIRCDIST.sat.window.yaml'
12 sed -n '1,360p' 'circdist/proof-dag/nodes/CIRCDIST.sat.instances.yaml'
13 nl -ba circdist/proof-dag/nodes/CIRCDIST.sat.yaml
14 nl -ba circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml
15 rg -n -i "V3|R-C4|Definition 3\.5|equivalently Definition 2\.7|detector/observable split|detector split" circdist operations maintenance CIRCDIST.md
16 rg -n -i "migration report|migration|frozen question|frozen|rescope" maintenance/circdist_protocol_20260826 circdist/artifacts/definitions circdist circdist/README.md CIRCDIST.md
17 rg -n "reviewed_hash|normalize|normalization|sha256" tools/proof_dag_check.py tools/proof_dag_schema.py tools/evidence_closure_check.py
18 sed -n '1030,1075p' operations/circdist/SCHEDULER.yaml
19 sed -n '1,260p' maintenance/circdist_protocol_20260826/REPORT.md
20 sed -n '1,260p' circdist/README.md
21 sed -n '1,300p' CIRCDIST.md
22 sed -n '50,85p' tools/proof_dag_schema.py
23 sed -n '330,375p' tools/proof_dag_schema.py
24 rg --files operations/circdist maintenance/circdist_protocol_20260826 circdist/artifacts/definitions | sort
25 wc -lc [the 17 load-bearing SAT definition/proof/review files listed in §1]
26 nl -ba circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md
27 nl -ba circdist/artifacts/definitions/SAT_RESCOPE_20260822.md
28 nl -ba operations/circdist/README.md
29-34 rg -n "^#{1,6} |Definition 2\.7|Definition 3\.5|Proposition 3\.7|section 8\.1|§8\.1|Lemma 2\.9|R5|window.*instances|instances.*window|route implication|implication" [each of transfer proof, transfer amendment, root assembly, root review, root adjudication, transfer bridge fold]
35 sed -n '136,440p' circdist/artifacts/circdist_sat_transfer_proof_20260823.md
36 sed -n '620,720p' circdist/artifacts/circdist_sat_transfer_proof_20260823.md
37 sed -n '1390,1485p' circdist/artifacts/circdist_sat_transfer_proof_20260823.md
38 sed -n '95,205p' circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md
39 sed -n '350,440p' circdist/artifacts/circdist_sat_transfer_proof_20260823.md
40 sed -n '677,714p' circdist/artifacts/circdist_sat_transfer_proof_20260823.md
41 sed -n '105,182p' circdist/reviews/circdist_transfer_bridgefold_20260823.md
42 sed -n '360,460p' circdist/reviews/circdist_transfer_bridgefold_20260823.md
43 sed -n '518,620p' circdist/reviews/circdist_transfer_bridgefold_20260823.md
44 rg -n -C 6 "R5" circdist/artifacts/circdist_sat_root_assembly_20260823.md
45 sed -n '1,240p' circdist/artifacts/circdist_sat_root_assembly_20260823.md
46 sed -n '1000,1097p' circdist/artifacts/circdist_sat_root_assembly_20260823.md
47 sed -n '1,155p' circdist/reviews/circdist_sat_root_proved_adjudication_20260823.md
48 sed -n '155,275p' circdist/reviews/circdist_sat_root_proved_adjudication_20260823.md
49 sed -n '275,380p' circdist/reviews/circdist_sat_root_proved_adjudication_20260823.md
50 sed -n '380,425p' circdist/reviews/circdist_sat_root_proved_adjudication_20260823.md
51 sed -n '1,180p' tools/proof_dag_check.py
52 sed -n '1,120p' tools/proof_dag_schema.py
53 sed -n '375,700p' tools/proof_dag_schema.py
54 sed -n '700,820p' tools/proof_dag_schema.py
55 rg -n -C 5 "\(W\)|window theorem|d_R = d_d|R_stab|Theorem T|transfer" circdist/artifacts/circdist_sat_instances_20260823.md
56 rg -n -C 5 "window theorem|inherits|conditionality|d_R = d_d|R_stab|licen|verdict" circdist/reviews/circdist_sat_instances_review_20260823.md
57 sed -n '520,609p' circdist/artifacts/circdist_sat_instances_20260823.md
58 sed -n '315,391p' circdist/reviews/circdist_sat_instances_review_20260823.md
59 sed -n '1,180p' circdist/reviews/circdist_sat_root_review_20260823.md
60 sed -n '180,360p' circdist/reviews/circdist_sat_root_review_20260823.md
61 sed -n '360,568p' circdist/reviews/circdist_sat_root_review_20260823.md
62 sed -n '568,773p' circdist/reviews/circdist_sat_root_review_20260823.md
63 sed -n '250,570p' circdist/artifacts/circdist_sat_root_assembly_20260823.md
64 sed -n '570,866p' circdist/artifacts/circdist_sat_root_assembly_20260823.md
65 sed -n '866,1000p' circdist/artifacts/circdist_sat_root_assembly_20260823.md
66 sed -n '1,105p' circdist/reviews/circdist_transfer_bridgefold_20260823.md
67 sed -n '182,360p' circdist/reviews/circdist_transfer_bridgefold_20260823.md
68 sed -n '460,518p' circdist/reviews/circdist_transfer_bridgefold_20260823.md
69 sed -n '620,639p' circdist/reviews/circdist_transfer_bridgefold_20260823.md
70 sed -n '1,250p' circdist/artifacts/circdist_sat_window_theorem_20260822.md
71 sed -n '250,620p' circdist/artifacts/circdist_sat_window_theorem_20260822.md
72 sed -n '1,220p' circdist/artifacts/circdist_sat_window_amendment1_20260822.md
73 sed -n '1,220p' circdist/reviews/circdist_sat_window_review_20260822.md
74 sed -n '1,140p' circdist/artifacts/circdist_sat_window_amendment1_20260822.md
75 python3 tools/proof_dag_check.py --problem circdist
76 python3 tools/proof_dag_check.py --problem all
77 python3 tools/evidence_closure_check.py --problem circdist
78 python3 tools/check_circdist_migration.py
79 python3 - <<'PY' [load current circdist with proof_dag_schema; recompute all 18 current node/route reviewed_hash entries and print four SAT claim hashes plus the root implication hash]
80 sed -n '120,230p' tools/proof_dag_schema.py
81 sed -n '230,330p' tools/proof_dag_schema.py
82 python3 - <<'PY' [hash the exact proposed claim and implication strings printed in Findings F-CLAIM/F-ROUTE]
83 shasum -a 256 circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md circdist/artifacts/definitions/SAT_RESCOPE_20260822.md circdist/artifacts/circdist_sat_root_assembly_20260823.md circdist/reviews/circdist_sat_root_review_20260823.md circdist/reviews/circdist_sat_root_proved_adjudication_20260823.md circdist/reviews/circdist_transfer_bridgefold_20260823.md circdist/artifacts/circdist_sat_transfer_proof_20260823.md circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md
84 python3 - <<'PY' [TemporaryDirectory under /tmp; copy proof-DAG/reviews; symlink artifacts/operations; apply exactly §§5-9 in scratch; write generated views; call validate_problem; print hashes/levels/errors/warnings; automatic cleanup]
85 python3 - <<'PY' [first final-integrity assertion: check the report, payload hashes, two anticipated heading labels, repository status, and a process snapshot]
86 python3 - <<'PY' [corrected final-integrity assertion using the report's numbered heading labels; run `git status --short --` for the report; run `ps -axo pid=,ppid=,stat=,command=` and reject surviving validator, migration, hash, or named-scratch processes]
```

For commands 79, 82, and 84, the inline scripts' mathematical inputs and expected outputs are fully reproduced in §§2, 5-6, and 11. Command 84 used no hidden fixture or retained state; its transformation is exactly the YAML in §9.

Command 85 exited 1 because its audit script anticipated the unnumbered labels `## Dispatcher authorization table` and `## Process, command, log, and scratch disclosure`, while this report uses `## 10. Dispatcher authorization table` and `## 14. Reproducible command and process ledger`. The script reported exactly those two missing literal markers; it did not report a missing payload hash and did not reach its `git` or `ps` child-process calls. This was an error in the check's expected headings, not a repository-validation or mathematical failure. Command 86 corrected only those expected heading strings and exited 0 with:

```text
report_exists True
report_bytes_before_final_ledger_patch 48927
report_lines_before_final_ledger_patch 667
report_sha256_before_final_ledger_patch 47709b4461dfe868db11ce402431315fbd5ba3b566c6e2341acbdcd021df1af1
required_markers_missing []
git_status_for_report ?? circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md
matching_survivors []
```

The report byte count and report-file hash above are explicitly pre-final-ledger-patch values and are not authorization hashes. The immutable authorization hashes are the normalized exact-string hashes in §§5-6.

### 14.3 Scratch, logs, and termination

- Temporary scratch created: `/tmp/circdist_sat_v3_review_7oye21fe`.
- Scratch removal: automatic `TemporaryDirectory` cleanup; the script printed `scratch_exists_after_cleanup False`.
- New log files: none. Command stdout/stderr exists only in the task tool transcript.
- Background/detached jobs: none.
- Sub-agents: none spawned.
- Process accounting: commands 1-84 launched only the foreground programs identified in the command ledger (and ordinary foreground shell wrappers supplied by `exec_command`). Command 85 launched its foreground shell wrapper and one `python3` process; because its marker assertion failed before the subprocess lines, it launched no `git` or `ps` child. Command 86 launched its foreground shell wrapper, one `python3` process, one foreground `git status` child, and one foreground `ps` child. No background or detached process was requested at any point.
- Exit status: commands 1-84 and 86 exited 0. Command 85 exited 1 solely for the transparently recorded heading-literal mismatch.
- Surviving processes from commands 1-86: none matching the audit validators, migration checker, hash command, or named scratch path; command 86 printed `matching_survivors []`. All foreground command 85/86 processes had exited when their respective tool calls returned.
- Non-OS mutation actions: one `apply_patch` tool call created this report; a second `apply_patch` tool call appended this final integrity record. These calls targeted no other path and did not launch a worker-controlled OS process.
- Durable repository files written by this worker: exactly this report.

## 15. Limitations

1. This is an exact-text and route-composition review, not a new end-to-end proof of any premise.
2. I did not rerun the archived distance searches or the bridge-fold harness. I checked their definitions, derivations, scopes, counterexample logic, hashes, and independent-review chain. Existing direct computations remain evidence from their own reports.
3. The current validator does not infer dependencies from prose. Its acceptance of the present `instances` node therefore does not cure the missing `window` route edge.
4. The old window Amendment 1 ends S3-prime with a broad “independent of detector-set convention” sentence. Transfer Amendment 1 and the counterexample supersede that reading. This review uses only the corrected named-pair equality and does not carry the broad sentence.
5. The route implication `PROVED` licence is conditional logic. It says nothing about whether the three premise claims deserve their present levels beyond confirming that their hashes and current completion bindings are structurally valid.
6. No root `PROVED` promotion is licensed now or by automatic future inheritance.
