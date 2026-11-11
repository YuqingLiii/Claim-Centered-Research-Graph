# Group-orbit Bell matrices

This project studies how finite group symmetry controls Bell/XOR vector
optima, optimal strategies, dimension requirements, and classical certification.
The classical-denominator and shifted-duplication continuation is summarized in
[`artifacts/classical-exploration-summary-20260907.md`](artifacts/classical-exploration-summary-20260907.md).
The preceding vector-optimum exploration is summarized in
[`artifacts/group-orbit-exploration-20260907.md`](artifacts/group-orbit-exploration-20260907.md).

The spectral upper bound and the paired-top-space factor criterion substantially
overlap Epping--Kampermann--Bruss (2013). The transitive-equivariant optimum
formula is a short symmetry corollary. They are organizing results, not a
claimed original solution; exact primary-source comparisons are in
[`artifacts/group-orbit-literature-positioning-20260907.md`](artifacts/group-orbit-literature-positioning-20260907.md).

The current exploration adds a balance-map uniqueness/rank criterion, an
explicit root-frame family requiring vector dimension r, near-saturation
estimates, and a quantitative loss for insufficient vector dimension.
Canonical assessments, independent reviews, and exact replay records determine
the evidence levels. Correctness review does not establish novelty.

Start from `GROTHORB.transitive-optimum`,
`GROTHORB.extremizer-classification`, `GROTHORB.balance-rigidity`,
`GROTHORB.root-frame-dimension`, or `GROTHORB.robust-dimension-gap`.
The R/C/H statement describes only invariant averaged weights, not all
extremizers. Vector dimension is distinct from minimum physical Hilbert-space
dimension. The general classical-value problem remains a research frontier.

For exact classical values, start from `GROTHORB.root-classical`,
`GROTHORB.root-extended-shift-window`, and `GROTHORB.d3-shift-envelope`.
The generic `GROTHORB.psd-antipodal-linear-window` certificate gives the
full-root affine value on 0<=lambda<=1/[2(r-1)] for all r>=3, expanding
the earlier sufficient `GROTHORB.root-small-shift` interval.
`GROTHORB.root-shift-window-maximality` proves this affine interval is exact,
while `GROTHORB.psd-antipodal-interior-equality` classifies all strict-interior
ordered optimizers. The post-window envelope, endpoint optimizer structure,
and novelty remain open.
`GROTHORB.antipodal-shift-comparison` and `GROTHORB.shift-duplication-gap`
separate unshifted root duplication from a subsequent diagonal modification.
The refuted whole-interval linear conjecture is retained, not erased.
The weighted-frame interface `GROTHORB.weighted-isotropic-optimum` and
minimum-setting construction `GROTHORB.minimum-settings-isotropic` have
passed scoped reviews, with direct prior-art overlap recorded separately.
`GROTHORB.minimal-setting-conditioning` and
`GROTHORB.minimal-conditioning-equality` describe a quantitative bound and
its exact attainment conditions. They do not assert a new construction,
attainability in every dimension, or physical self-testing.

Canonical claims live one per file in [`proof-dag/nodes/`](proof-dag/nodes/).
[`NODE_INDEX.md`](proof-dag/NODE_INDEX.md) and
[`GRAPH.mmd`](proof-dag/GRAPH.mmd) are generated. Long proofs and runs are
under [`artifacts/`](artifacts/), checkers under [`tools/`](tools/), and immutable
independent audits under [`reviews/`](reviews/). Historical proofs and the
failed commutant-only route are preserved.
