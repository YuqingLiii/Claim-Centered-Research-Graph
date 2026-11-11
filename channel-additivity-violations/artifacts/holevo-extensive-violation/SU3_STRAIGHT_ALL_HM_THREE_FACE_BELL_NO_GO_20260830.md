# The straight all-h/m three-face cluster has no Bell gap

Date: 2026-08-30

Status: proposer-side all-parameter theorem with an exact rational Bernstein/logarithm
certificate; independent review pending.

## Scope and cover

Consider the translated straight face-base cluster

\[
 ((-4,2),(-2,1),(0,0)).
\]

Retain the three original binary input blocks at offsets `(-3,2)`, `(-1,1)`, and `(1,0)`.  All
three are `h/m` incidences.  Their three interval coordinates and the two compactified Dynkin
labels form a five-dimensional box.  Separate convexity reduces every other input block to 36
correlated Gram endpoints while leaving the three retained original-side distributions unchanged.

The exact phase-incidence audit applies: no relevant pair of input blocks has more than one
shared environment block, so the Gram upper bound is independent of all channel phases.

## Exact reconstruction and compactification

Let `P,Q>=0` be the residual integer labels above the smallest admissible base.  The checker clears
every representation-dimension and shared-environment denominator by a common positive
polynomial.  Exact tensor interpolation reconstructs and verifies:

- 36 cleared Gram numerators of degree tuple `(14,12,2,2,2)`; and
- three retained original-side probability triples of degree tuple `(6,6,1,1,1)`.

The substitutions

\[
 p={P\over P+1},\qquad q={Q\over Q+1}
\]

compactify the unbounded label quadrant.  Exact rational Bernstein control ratios upper-bound
each Gram endpoint and every retained side probability.  Directed rational logarithm intervals
then lower-bound the isotropic Bell entropy.  Replacement endpoints are used only for the Gram
upper bound; side entropies are always computed on the three retained **original** outputs.

## Certificate result

The adaptive subdivision certifies 4,165 five-dimensional boxes.  The smallest certified
natural-log margin is strictly greater than

\[
 2.347448147888\times10^{-5},
\]

in the recorded compact box

\[
 [1/4,3/8]\times[7/8,1]\times[1/4,3/8]
 \times[0,1/4]\times[1/2,3/4].
\]

No box reaches maximum depth uncertified.  Hence every channel in this single straight
orientation satisfies the registered conjugate-Bell no-gap inequality for every admissible
integer label and continuous weight.

This does not upgrade the aggregate straight-chain node: the other two straight orientations
remain independent premises.  It says nothing about repeated vertices, multiplicity spaces,
noncovariant channels, or non-Bell joint inputs.

## Reproduction

This completed process loaded the original per-control `Fraction` backend before the later
common-denominator optimization:

```text
python3 holevo-extensive-violation/tools/certify_su3_straight_chain_all_hm_cover.py
```

Complete terminal transcript:
`holevo-extensive-violation/artifacts/SU3_STRAIGHT_ALL_HM_THREE_FACE_CERTIFICATE_20260830.txt`.
