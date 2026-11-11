# Exact proposer-side certificate: bent-left ternary SU(3) three-face orientation

Date: 2026-08-30

Status: exact proposer-side certificate, pending independent review. The atomic orientation node
is assessed `CONJECTURED`, not `PROVED`; no other orientation and no parent conjunction is closed
by this artifact.

## Statement certified by the run

For the bent cluster

\[
((-3,3),(-2,1),(0,0)),
\]

the fixed-three cover retaining the binary side at `(-2,3)`, ternary side at `(-1,1)`, and binary
side at `(1,0)` has strictly positive Bell-minus-twice-side entropy margin on the complete compact
six-variable parameter cube. The endpoint reduction contains the exact 24 Gram patterns specified
by the immutable driver configuration.

## Certificate mechanism

The driver selects `bent-left-ternary-fixed-three` and delegates to the rational/Bernstein core.
The core:

1. constructs the exact labelled SU(3) union and its 24 Gram endpoints;
2. reconstructs the Gram and retained-side rational functions over `Fraction` arithmetic and
   checks the interpolants at independent rational points;
3. compactifies both highest-weight label coordinates and forms common-denominator Bernstein
   controls in all six variables;
4. adaptively bisects the compact cube, using rigorous rational range enclosures plus directed
   entropy bounds; and
5. accepts a box only when the certified natural-log lower margin is strictly positive.

No floating-point comparison is used to decide box acceptance. The printed decimal margin is only
a rendering of the already positive rigorous lower bound.

## Terminal verdict

The completed exit-zero run certified 21,058 compact boxes. Its smallest displayed certified
natural-log margin was greater than

\[
6.340626717749\times10^{-8}.
\]

The exact terminal record, command, parameter box and source hashes are in
`SU3_BENT_LEFT_TERNARY_EXACT_RUN_20260830.txt`.

That run record now contains the complete local import closure, not only the driver and core.
Every recorded source mtime predates process launch. The shared core's final human-readable line
is hard-coded as "input-centered triangular"; the command and all configuration-specific progress
lines correctly identify `bent-left-ternary-fixed-three`, so this label defect does not alter the
executed configuration or certificate arithmetic.

## Scope boundary

This is one atomic bent-left ternary orientation. It does not certify bent-right,
bent-central, straight-ternary, straight-reduced-coordinate, the input-centered triangle, or the
aggregate bent/straight SU(3) claims. Independent adversarial review of the code path, orientation
mapping, exact arithmetic and completeness is required before `PROVED` promotion.
