# Connected three-face SU(3) Pieri clusters

Date: 2026-08-30

Status: exact proposer-side finite classification; independent review pending.

The bases of elementary six-edge Pieri faces lie on the triangular lattice with neighbor shifts

\[
 \pm(1,1),\qquad \pm(1,-2),\qquad \pm(2,-1).
\]

Enumerate every connected three-element subset containing the origin inside the two-step ball and
quotient only by overall translation. This is exhaustive because every connected three-vertex
graph has a vertex at distance at most two from a chosen origin. No Weyl or conjugation symmetry
is assumed.

There are exactly 11 translation classes:

- 3 straight chains;
- 6 bent chains whose endpoints are not adjacent;
- 2 triangles whose three face bases are mutually adjacent.

Every chain union has seven input vertices, seven environment vertices, and 16 distinct incidence
edges, with degree multiset `[2,2,2,2,2,3,3]` on both sides. The two triangular orientations are
not the same labelled bipartite union: one has seven inputs, six environments, and degrees
`degI=[2,2,2,2,2,2,3]`, `degE=[2,2,2,3,3,3]`; the other swaps those two multisets. Both have 15
distinct incidence edges.

The exact list and signatures are reproduced by

```sh
python3 holevo-extensive-violation/tools/classify_su3_three_face_clusters.py
```

This classification is only the combinatorial registry. It does not prove a Bell no-go theorem
for any three-face family. Each shape family must retain its branch orientation and be analyzed
without importing an unproved channel-level symmetry.
