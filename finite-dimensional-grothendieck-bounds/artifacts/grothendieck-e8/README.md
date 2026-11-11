# E8 Grothendieck candidate

This directory records a self-contained exact E8-root-system witness with
`omega_8 = 9240`, `omega_1 = 6104`, and ratio
`165/109 = 1.513761467889...`.

The canonical record is split between one-claim YAML files in
[`proof-dag/nodes/`](../../proof-dag/nodes), generated
[`NODE_INDEX.md`](../../proof-dag/NODE_INDEX.md) and [`GRAPH.mmd`](../../proof-dag/GRAPH.mmd),
node-linked evidence in [`artifacts/`](.), replay programs in
[`tools/`](../../tools/grothendieck-e8), and independent reviews in [`reviews/`](../../reviews/grothendieck-e8).

Start from [the exact certificate](e8-exact-certificate-20260829.md)
or node `GROTHE8.goal`.  The Bell matrix is
`B = 3G - 13I` on the 120 positive E8 roots.  Two structurally different exact
checkers reproduce the root-poset certificate; the second also verifies the
tight frame, vector value, and explicit `A1+A6` equality witness.  A 16-dimensional
maximally entangled state and four-qubit Clifford observables give the physical
realization.

The headline remains `CONJECTURED`, not `PROVED`, because the current proof and
both implementations have not yet received an independent adversarial review.
