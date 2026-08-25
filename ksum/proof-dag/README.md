# KSUM proof DAG

- [Node index](NODE_INDEX.md)
- [Generated graph](GRAPH.mmd)
- [Canonical node files](nodes/)

The current schema stores one stable YAML record per node. Each route is an
AND-hyperedge stored in the node it seeks to establish; its premises are
jointly required, while different routes are alternatives. Large proofs,
logs, reviews, and certificates remain in their stable locations and are
linked from the exact node or route assessment they support. The index and
graph are generated views.

The principal delivered theorem is recorded at `KSUM.A1d`; it is listed here
because it is a completed output of the campaign rather than a premise on the
still-open route to `KSUM.goal`.

Run the repository validator from the root:

```text
python3 tools/proof_dag_check.py --problem ksum --write-generated
```
