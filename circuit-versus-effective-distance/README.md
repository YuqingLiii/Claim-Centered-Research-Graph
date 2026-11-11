# Circuit versus effective distance

Problem P06. A closed-lift criterion for when the circuit distance equals the effective distance.

Entry node: [`CIRCDIST.lift`](proof-dag/nodes/CIRCDIST.lift.yaml). The [node index](proof-dag/NODE_INDEX.md) and [graph](proof-dag/GRAPH.mmd) are generated from [`proof-dag/nodes/`](proof-dag/nodes/).

Node files: 4 (4 belonging to this question).

## Origin

The four circuit-distance questions (P05-P08) were recorded as four roots of one project (`circdist`). Each is now a standalone project containing its own nodes, the dependency nodes its routes require, and every artifact and review those nodes link. Node IDs, claims and evidence levels are unchanged; structured evidence paths were rebased from `circdist/` to this directory ([`proof-dag/SOURCE_MAP.json`](proof-dag/SOURCE_MAP.json)). Paths quoted inside historical reports and hash-bound computation packages still use the `circdist/` prefix.

Large computation packages are included in part: raw execution-log subtrees, compressed solver/proof streams, bundled solver executables and package files over 1 MiB are omitted. They are listed in [`EVIDENCE_GAPS.yaml`](../EVIDENCE_GAPS.yaml); package checksum manifests therefore also name files that are not present here.

Validate from the repository root:

```sh
python3 tools/proof_dag_check.py --problem circuit-versus-effective-distance
python3 tools/evidence_closure_check.py
```
