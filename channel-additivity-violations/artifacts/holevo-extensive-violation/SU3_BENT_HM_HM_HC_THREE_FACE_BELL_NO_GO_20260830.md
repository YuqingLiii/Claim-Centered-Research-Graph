# The bent h/m, h/m, h/c three-face cluster has no Bell gap

Date: 2026-08-30

Status: proposer-side all-parameter theorem with an exact rational Bernstein/logarithm
certificate; independent review pending.

## Scope and cover

Consider the bent face-base cluster

\[
 ((-3,0),(-1,-1),(0,0)).
\]

Its labelled incidence union has seven input blocks and seven environment blocks.  Retain the
three original binary input blocks at offsets `(-2,0)`, `(1,0)`, and `(2,-2)`, whose branch sets
are respectively `h/m`, `h/m`, and `h/c`.  Their three independent interval coordinates, together
with the two compactified Dynkin labels, give a five-dimensional parameter box.

Separate convexity reduces every other input block to endpoints while preserving the original
three retained side outputs.  The complete endpoint set contains 36 correlated Gram branches.
The exact phase-incidence audit applies because no pair of input blocks in this union shares more
than one environment block, so all relevant Gram cross terms are phase independent.

## Exact reconstruction

Let `P,Q>=0` be the residual Dynkin labels above the smallest admissible base.  The checker clears
all representation-dimension and shared-environment denominators with a common positive
polynomial.  Exact tensor interpolation reconstructs and independently checks:

- 36 cleared Gram numerators of degree tuple `(14,12,2,2,2)`; and
- three retained original-side probability triples of degree tuple `(6,5,1,1,1)`.

The checker then compactifies the unbounded labels by

\[
 p=\frac{P}{P+1},\qquad q=\frac{Q}{Q+1},
\]

uses exact rational Bernstein control ratios to upper-bound every Gram endpoint and side
probability, and uses the repository's directed rational logarithm intervals to lower-bound the
isotropic Bell entropy.  The side entropy is always evaluated on the retained **original** channel
outputs; endpoint replacement channels are used only to upper-bound the Gram parameter, as
required by `SU3_FIXED_ORIGINAL_SIDE_ENDPOINT_LEMMA_20260830.md`.

## Certificate result

The adaptive subdivision certifies 3,435 five-dimensional boxes.  The smallest certified
natural-log margin is strictly greater than

\[
 1.891740238876\times10^{-5},
\]

attained in the recorded box

\[
 [1/8,1/4]\times[3/4,7/8]\times[1/2,5/8]
 \times[3/4,1]\times[3/4,1].
\]

No box reaches the maximum subdivision depth uncertified.  Therefore every channel in this
single bent orientation satisfies the conjugate-Bell no-gap inequality for all admissible integer
labels and continuous weights.

This result does not upgrade the aggregate bent-chain node: its other five orientation premises
remain separate.  It also says nothing about repeated vertices, multiplicity spaces,
noncovariant channels, or non-Bell joint inputs.

## Reproduction

The completed run used the original per-control `Fraction` backend already loaded before the
common-denominator optimization was introduced:

```sh
python3 holevo-extensive-violation/tools/certify_su3_bent_chain_hm_hm_hc_cover.py
```

The complete terminal transcript is
`holevo-extensive-violation/artifacts/SU3_BENT_HM_HM_HC_THREE_FACE_CERTIFICATE_20260830.txt`.
