# The bent c/m, h/m, h/c three-face cluster has no Bell gap

Date: 2026-08-30

Status: proposer-side all-parameter theorem with an exact rational Bernstein/logarithm
certificate; independent review pending.

## Scope and cover

Consider the bent three-face cluster

\[
 ((-1,-1),(0,-3),(0,0)).
\]

Retain the three original binary input blocks at offsets `(-1,-2)`, `(1,0)`, and `(2,-2)`, with
incidence types `c/m`, `h/m`, and `h/c`.  Their three interval coordinates and the two compactified
Dynkin labels form a five-dimensional box.  Separate convexity reduces every other input block to
36 correlated Gram endpoints while leaving these three retained original-side distributions
unchanged.

The exact phase-incidence audit applies: the registered Bell Gram upper bound is independent of
all channel phases for this orientation.

## Exact reconstruction and compactification

Let `P,Q>=0` denote the residual integer labels above the smallest admissible base.  The checker
clears all representation-dimension and shared-environment denominators by a common positive
polynomial.  Exact tensor interpolation reconstructs and verifies:

- 36 cleared Gram numerators of degree tuple `(12,14,2,2,2)`; and
- three retained original-side probability triples of degree tuple `(6,5,1,1,1)`.

The substitutions

\[
 p={P\over P+1},\qquad q={Q\over Q+1}
\]

compactify the unbounded label quadrant.  Exact rational Bernstein control ratios bound every
Gram endpoint and retained side probability.  Directed rational logarithm intervals then
lower-bound the isotropic Bell entropy.  Replacement endpoints are used only for the Gram upper
bound; side entropies are always evaluated on the retained original outputs.

## Certificate result

The adaptive subdivision certifies 10,783 five-dimensional boxes.  The smallest certified
natural-log margin is strictly greater than

\[
 4.648873074005\times10^{-7},
\]

in the compact box

\[
 [3/4,7/8]\times[1/4,1/2]\times[1/4,1/2]
 \times[3/4,1]\times[3/4,1].
\]

No box reaches maximum depth uncertified.  Hence every channel in this single bent orientation
satisfies the registered conjugate-Bell no-gap inequality for every admissible integer label and
continuous weight.

This does not upgrade the aggregate chain or three-face conjunction nodes: the remaining
orientations are independent premises.  It says nothing about repeated vertices, multiplicity
spaces, noncovariant channels, or non-Bell joint inputs.

## Reproduction

```text
python3 holevo-extensive-violation/tools/certify_su3_bent_chain_cm_hm_hc_cover.py
```

Terminal certificate:
`holevo-extensive-violation/artifacts/SU3_BENT_CM_HM_HC_THREE_FACE_CERTIFICATE_20260830.txt`.
