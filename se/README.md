# Minimal-alphabet Set Equality

This directory contains the public research record for Set Equality at
alphabet size `q = 2n`.

- [`proof-dag/NODE_INDEX.md`](proof-dag/NODE_INDEX.md) is the generated claim index.
- [`proof-dag/GRAPH.mmd`](proof-dag/GRAPH.mmd) is the generated graph view.
- [`proof-dag/nodes/`](proof-dag/nodes/) contains the 85 canonical node records.
- [`lean/`](lean/) contains the linked Lean development.
- [`reviews/`](reviews/) contains project-level external reviews.
- [`artifacts/`](artifacts/) contains the linked proofs, runs, and counterexamples.
- [`tools/`](tools/) contains the node-linked finite envelope, matrix, and MDH structure checkers.

Begin with node `SE.goal` for the original target, `SE.br.cor16` for the
unconditional lower bound, and `SE.goal.conditional-optimal` for the conditional
optimal-order consequence.  Evidence and reviews are reached through the
structured links in those node files.

The envelope checker uses only the Python standard library. The two matrix
checkers additionally require NumPy; their node-linked rerun report gives
commands, tested versions, outputs, and the finite scope of each check.
The [MDH reproduction record](artifacts/mdh_reproduction_20260825.md) gives
the restored structure-check commands, input data, and one unresolved
disagreement with the old dimension dictionary. Its full checker reports
that disagreement with a nonzero exit code.
