# Channel additivity violations

Problem P01. Holevo-capacity and minimum-output-entropy additivity of quantum channels: when it holds, how common violations are, and how large they can be.

This project combines the following research directions in one proof-DAG. Their node IDs keep their original prefixes, and their evidence is kept in per-direction subfolders of `artifacts/`, `reviews/` and `tools/`.

| Direction | Entry node | Nodes | Direction notes |
|---|---|---:|---|
| Holevo additivity equality (universality and the logical relations between pair, self and tensor-power additivity) | [`HAEQ.goal`](proof-dag/nodes/HAEQ.goal.yaml) | 8 | [`artifacts/holevo-additivity-equality/README.md`](artifacts/holevo-additivity-equality/README.md) |
| Counterexample prevalence (in what precise senses additivity counterexamples are many) | [`HCPREV.goal`](proof-dag/nodes/HCPREV.goal.yaml) | 19 | [`artifacts/holevo-counterexample-prevalence/README.md`](artifacts/holevo-counterexample-prevalence/README.md) |
| Extensive violation (whether finite-dimensional p = 1 violations can exceed constant scale or grow linearly) | [`HEXT.goal`](proof-dag/nodes/HEXT.goal.yaml) | 147 | [`artifacts/holevo-extensive-violation/README.md`](artifacts/holevo-extensive-violation/README.md) |

Total: 174 node files. The [node index](proof-dag/NODE_INDEX.md) and [graph](proof-dag/GRAPH.mmd) are generated from the canonical files in [`proof-dag/nodes/`](proof-dag/nodes/).

Each direction's original project notes are kept verbatim (with repaired navigation links) in its `artifacts/<direction>/README.md`. Paths quoted inside historical reports refer to the earlier per-direction layout; [`proof-dag/SOURCE_MAP.json`](proof-dag/SOURCE_MAP.json) translates them.

24 linked third-party papers are not redistributed here; they are listed with their arXiv identifiers in [`EVIDENCE_GAPS.yaml`](../EVIDENCE_GAPS.yaml) and reported by the validators as declared gaps.

Validate from the repository root:

```sh
python3 tools/proof_dag_check.py --problem channel-additivity-violations
python3 tools/evidence_closure_check.py
```
