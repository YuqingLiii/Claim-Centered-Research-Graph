# Straight reduced-coordinate three-face certificate: depth-10 resolution blocker

Date: 2026-08-31

Status: exact-certificate attempt failed at the adaptive depth ceiling. The atomic orientation
remains `NUMERICAL`; this is not a mathematical counterexample.

## Scope

The attempted route is the registered reduced-coordinate fixed-three cover for

\[
((-2,4),(-1,2),(0,0)).
\]

It retains the original binary block at `(-1,4)`, ternary block at `(0,2)`, and binary block at
`(2,-2)`, while reducing the other blocks to 24 Gram endpoints. Exact reconstruction succeeded on
all three attempts: the Gram degree tuple was `(12,14,2,2,2,2)`, and the three retained-side
distributions had degree tuple `(6,6,1,1,1,1)`.

## Three depth ceilings reached

The unmodified registered command first reached depth 6. Runtime-only overrides then tested depth
7 and depth 10 without changing any public source file. Each run stopped at an uncertified box
whose six coordinate widths were exactly the reciprocal of the corresponding depth denominator.

| maximum depth | terminal lower-margin diagnostic | terminal compact box |
| --- | ---: | --- |
| 6 | `-2.48325593076882e-05` | `[63/64,1] x [45/64,23/32] x [1/2,33/64] x [3/4,49/64] x [57/64,29/32] x [3/4,49/64]` |
| 7 | `-2.0529833068348998e-05` | `[127/128,1] x [21/32,85/128] x [65/128,33/64] x [3/4,97/128] x [115/128,29/32] x [3/4,97/128]` |
| 10 | `-9.173335876151267e-06` | `[1023/1024,1] x [5/8,641/1024] x [65/128,521/1024] x [769/1024,385/512] x [917/1024,459/512] x [777/1024,389/512]` |

At depth 10 every interval has width `1/1024`. The adaptive checker therefore exhausted the
runtime ceiling before its rational Bernstein/logarithm enclosure became strictly positive. The
negative number is a lower-bound diagnostic for a whole box, not the actual entropy margin at a
point. Consequently this failed certificate route neither refutes the orientation claim nor
supplies a Bell-gap channel.

## Exact blocker and next safe route

Blindly increasing the uniform depth again is not an automatic resolution: the depth-10 replay
already required roughly four hours, the terminal lower enclosure remained negative, and the
subdivision cost can grow exponentially. A further attempt should first sharpen the local
Bernstein range or directed-log enclosure near the recorded compact-boundary box, or introduce a
targeted coordinate split/analytic boundary estimate. Until such a refinement produces a complete
exit-zero transcript, the stress result remains only `NUMERICAL`.

The commands, all processed/certified/pending checkpoints, exact `Fraction` boxes, diagnostics,
and exit statuses are preserved in
`SU3_STRAIGHT_REDUCED_COORDINATE_THREE_FACE_CERTIFICATE_FAILURE_20260831.txt`.
