# Contributing

Changes should preserve the one-node/one-file contract and evidence links.

1. Read [the file protocol](FILE_PROTOCOL.md) and
   [the DAG protocol](DAG_PROTOCOL.md).
2. Update the canonical YAML node that owns the claim or route.
3. Store long proofs, reviews, programs, or outputs separately and link them from the exact
   assessment they support.
4. Update a linked Lean formalization and claim hash when applicable, or mark it stale.
5. Regenerate the graph views and validate both projects:

```bash
python tools/proof_dag_check.py --problem se --write-generated
python tools/proof_dag_check.py --problem ksum --write-generated
```

Do not submit generated caches, raw agent transcripts, credentials, or evidence that is not linked
from a canonical node.
