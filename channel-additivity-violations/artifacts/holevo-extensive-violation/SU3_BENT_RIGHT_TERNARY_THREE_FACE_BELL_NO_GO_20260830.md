# The bent-right ternary SU(3) three-face orientation has no Bell gap

Date: 2026-08-30

Status: proposer-side all-parameter theorem with an exact rational Bernstein/logarithm
certificate; independent review pending.

## Scope and fixed-three cover

Consider the bent face-base cluster

\[
((-3,3),(-1,2),(0,0)).
\]

The immutable `bent-right-ternary-fixed-three` configuration retains the original binary side
blocks at `(-2,3)` and `(0,2)` and the original ternary side block at `(1,0)`. Separate convexity
reduces every other input block to 24 correlated Gram endpoints while the three retained
original-side distributions remain unchanged. The two compactified Dynkin labels and four
retained weight coordinates give a six-dimensional compact box.

The phase-incidence audit used by the shared checker applies to this registered orientation, so
the endpoint Gram bound controls every allowed channel phase.

## Exact reconstruction and certificate

The checker clears the positive representation-dimension and shared-environment denominators,
then reconstructs and independently verifies over exact `Fraction` arithmetic:

- 24 cleared Gram endpoint polynomials of degree tuple `(12,12,2,2,2,2)`; and
- three retained original-side distributions of degree tuple `(5,5,1,1,1,1)`.

It compactifies the two unbounded nonnegative Dynkin-label residuals, forms exact rational
Bernstein control ratios, and adaptively bisects the six-dimensional cube. Directed rational
logarithm enclosures lower-bound the Bell-minus-twice-side entropy margin. A box is accepted only
after a strictly positive rigorous lower bound is obtained; the decimal printed below merely
renders that positive bound.

The exit-zero run certified 13,744 adaptive compact boxes. The smallest displayed certified
natural-log margin is strictly greater than

\[
4.870629792869\times 10^{-5},
\]

at the recorded compact box

\[
[1/8,1/4]\times[0,1/8]\times[0,1/8]\times
[5/8,3/4]\times[3/4,7/8]\times[0,1/4].
\]

No box reached maximum depth uncertified. Therefore this single bent-right orientation satisfies
the registered conjugate-Bell no-gap inequality for every admissible integer label, continuous
weight, and phase.

## Scope boundary and reproduction

This proposer-side certificate covers only the covariant qutrit conjugate-Bell route for the
bent-right ternary orientation. It does not establish any other orientation, the aggregate bent
parent, repeated-vertex or multiplicity cases, noncovariant channels, or non-Bell inputs. It is
`CONJECTURED`, not `PROVED`, until independent adversarial review checks the orientation mapping,
endpoint coverage, exact arithmetic, compact completeness, entropy bounds, and execution
provenance.

Reproduction command:

```text
python3 holevo-extensive-violation/tools/certify_su3_chain_three_face_sixdim_covers.py bent-right-ternary
```

The complete terminal transcript and source hashes are recorded in
`SU3_BENT_RIGHT_TERNARY_THREE_FACE_CERTIFICATE_20260830.txt`. The shared core's final sentence is
hard-coded as "input-centered triangular"; the command, immutable configuration, and all progress
prefixes identify the executed direction as `bent-right-ternary-fixed-three`.
