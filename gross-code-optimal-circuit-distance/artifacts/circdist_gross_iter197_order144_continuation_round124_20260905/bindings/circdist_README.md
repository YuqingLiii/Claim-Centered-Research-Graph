# QEC circuit-distance research

This is the current home of the four circdist questions, organized using the
same protocol as the SE/k-Sum release at `f9249e93` (2026-08-25).
The 2026-08-26 migration changes record layout, not mathematical conclusions.

| Question | Entry node | Recorded state |
|---|---|---|
| Gross-code optimal distance | [CIRCDIST.gross](proof-dag/nodes/CIRCDIST.gross.yaml) | D* ∈ {11,12} unresolved; candidate route CERTIFIED* |
| Closed-lift criterion | [CIRCDIST.lift](proof-dag/nodes/CIRCDIST.lift.yaml) | PROVED in the exact stated scope |
| Eff-Preserve complexity | [CIRCDIST.cplx](proof-dag/nodes/CIRCDIST.cplx.yaml) | Four-island result PROVED; full classification unresolved |
| Repeated-round stability | [CIRCDIST.sat](proof-dag/nodes/CIRCDIST.sat.yaml) | CERTIFIED*; detector-split V3 awaits approval |

Read the node assessment and its caveats for the authoritative state. This table
is an orientation summary, not a separate source of status.

## Records

- [Node index](proof-dag/NODE_INDEX.md) and [graph](proof-dag/GRAPH.mmd) are generated views.
- [Nodes](proof-dag/nodes/) own claims, routes, assessments and pending actions.
- [Reviews](reviews/) are immutable project-level reports; node links select the
  relevant finding and bind the exact reviewed claim or implication.
- [Artifacts](artifacts/) contain the proofs, amendments, computations and logs.
- [Frozen questions](artifacts/definitions/CIRCDIST_PROBLEMS.md) and
  [question-4 rescope](artifacts/definitions/SAT_RESCOPE_20260822.md) remain byte-identical.
- [Original node dossiers](artifacts/history/pre_protocol_20260826/nodes/) retain
  all 143 old events, including legacy event types, with no rewritten dates,
  summaries or historical paths. Each current node links its own original dossier.
- [Historical path map](artifacts/history/PATH_MAP.json) resolves old references
  inside immutable reports. Reports and hash-bound log packages were not edited
  merely to modernize their internal filenames.

The old `research/circdist/` is a frozen source snapshot, not a second editable
graph. Scheduling and budgets are separately maintained in
[`operations/circdist/`](../operations/circdist/README.md); the migration does not
authorize new research spending, change sat V3, or dispatch workers.

## Validation

From the repository root:

```sh
python3 tools/proof_dag_check.py --problem circdist
python3 tools/evidence_closure_check.py --problem circdist
python3 tools/check_circdist_migration.py
python3 tools/proof_dag_check.py --problem circdist --previous-state maintenance/circdist_protocol_20260826/baseline
```

Use `--write-generated` only after an authorized record edit. The migration check
verifies archived originals, statements, routes, levels, review metadata and
budget preservation. The `--previous-state` check starts at the new-format
baseline; it does **not** pretend the old and new event schemas are identical.
Neither check establishes the truth of a proof.

Historical computation packages include their original source files and checksum
manifests. Their temporary absolute paths and unavailable dependencies may need
repair before a future rerun. The migration verifies file preservation; it does
not claim to have reproduced those computations.

See the [migration record](../maintenance/circdist_protocol_20260826/REPORT.md)
for scope, exact changes and verification results.
