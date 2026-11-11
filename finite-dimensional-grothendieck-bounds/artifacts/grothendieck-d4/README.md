# Dimension-four Grothendieck candidate

This directory is the canonical claim-centered record for the symmetric
dimension-four Grothendieck candidate with archived matrix hash
`sha256:5fc272a61a97c0aa9f42ef86266756500401c701a6f33a3b30bde4dbe6f113e5`.

The canonical project layout is:

- [`proof-dag/nodes/`](../../proof-dag/nodes) for one stable YAML record per claim;
- [`proof-dag/NODE_INDEX.md`](../../proof-dag/NODE_INDEX.md) and
  [`proof-dag/GRAPH.mmd`](../../proof-dag/GRAPH.mmd) for generated views;
- [`artifacts/`](.) for node-linked derivations, run records, and certificates;
- [`tools/`](../../tools/grothendieck-d4) for node-linked exact replay programs; and
- [`reviews/`](../../reviews/grothendieck-d4) for independent reviews.

Begin with `GROTHD4.goal` for the unrestricted target and
`GROTHD4.fixed-support.upper` for the strongest currently closed subproblem.

The original `.mat` instance has now been recovered and frozen locally.  A
compact exact checker reconstructs its rank-four Gram matrix over
`Q(sqrt(5))`, verifies the exact dimension-four value and archived sign
witness, proves that this Gram space is the strict top eigenspace of `A`, and
the certificate note gives explicit two-qubit measurements.

The headline Grothendieck lower bound is **not** currently proved: the sole
load-bearing mathematical gap is the global classical upper bound
`omega_1(A) <= C`.  The recovered restricted degree-four dual families do not
close that gap.  Moreover, the archived 746825-coordinate feasibility system
searches for a separating pseudoexpectation: feasibility would obstruct a
degree-four SOS proof rather than establish the upper bound.  The corrected
duality directions are recorded in
`artifacts/d4-duality-direction-audit-20260829.md`.

The archived complementary 217+83 support cell is now closed at author level
by two exact p-cut certificates together with the exact q-block LDL
certificate. This proves the candidate upper bound and equality classification
inside that one frozen support split. It does **not** cover sign pairs that
move coordinates between the p and q supports, and no independent review has
promoted the result above `CONJECTURED`.

The quickest entry points are:

- `artifacts/d4-exact-instance-certificate-20260829.md` for the exact argument;
- `artifacts/d4-spectral-geometry-reduction-20260829.md` for the exact top-space reduction;
- `artifacts/d4-pcut-triangle-cover-20260830.md` for the fixed-support p-cut certificate;
- `tools/h4_exact_instance_checker.py` for the compact replay;
- `tools/h4_pcut_triangle_cover_checker.py` and
  `tools/h4_pcut_twohop_checker.py` for two fixed-support replays;
- `proof-dag/nodes/GROTHD4.classical.upper.yaml` for the remaining obstruction.
