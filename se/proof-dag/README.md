# SE proof DAG

- [Node index](NODE_INDEX.md)
- [Generated graph](GRAPH.mmd)
- [Canonical node files](nodes/)

The current schema stores one stable YAML record per node. Each route is an
AND-hyperedge stored in the node it seeks to establish; its premises are
jointly required, while different routes are alternatives. Large proofs,
logs, reviews, and certificates remain in their stable locations and are
linked from the exact node or route assessment they support. The index and
graph are generated views.

Source locators of the form `BR:<line>` refer to line numbers in
`se/artifacts/references/BR_1310.5185v4_collision.tex`, the repository copy of the
Belovs--Rosmanis source used by these node records.

The retained certified intermediate result is recorded at `SE.br.cor16`; it is
listed here because it is a reusable output rather than a premise on the
currently registered route to `SE.goal`.

Run the repository validator from the root:

```text
python3 tools/proof_dag_check.py --problem se --write-generated
```
