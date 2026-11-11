# Finite-dimensional Grothendieck bounds

Problem P11. Finite-dimensional real Grothendieck constants and the Bell-inequality matrices that witness them.

This project combines the following research directions in one proof-DAG. Their node IDs keep their original prefixes, and their evidence is kept in per-direction subfolders of `artifacts/`, `reviews/` and `tools/`.

| Direction | Entry node | Nodes | Direction notes |
|---|---|---:|---|
| Dimension-four candidate, with the fixed-support subtheorem | [`GROTHD4.goal`](proof-dag/nodes/GROTHD4.goal.yaml), [`GROTHD4.fixed-support.upper`](proof-dag/nodes/GROTHD4.fixed-support.upper.yaml), [`GROTHD4.cut.affine-equality-terminals`](proof-dag/nodes/GROTHD4.cut.affine-equality-terminals.yaml), [`GROTHD4.spectral.exact-spectrum`](proof-dag/nodes/GROTHD4.spectral.exact-spectrum.yaml), [`GROTHD4.spectral.top-energy-bound`](proof-dag/nodes/GROTHD4.spectral.top-energy-bound.yaml) | 46 | [`artifacts/grothendieck-d4/README.md`](artifacts/grothendieck-d4/README.md) |
| E8 candidate certificate | [`GROTHE8.goal`](proof-dag/nodes/GROTHE8.goal.yaml), [`GROTHE8.measurements`](proof-dag/nodes/GROTHE8.measurements.yaml) | 9 | [`artifacts/grothendieck-e8/README.md`](artifacts/grothendieck-e8/README.md) |

Total: 55 node files. The [node index](proof-dag/NODE_INDEX.md) and [graph](proof-dag/GRAPH.mmd) are generated from the canonical files in [`proof-dag/nodes/`](proof-dag/nodes/).

Each direction's original project notes are kept verbatim (with repaired navigation links) in its `artifacts/<direction>/README.md`. Paths quoted inside historical reports refer to the earlier per-direction layout; [`proof-dag/SOURCE_MAP.json`](proof-dag/SOURCE_MAP.json) translates them.

Validate from the repository root:

```sh
python3 tools/proof_dag_check.py --problem finite-dimensional-grothendieck-bounds
python3 tools/evidence_closure_check.py
```
