# SU(3) straight/bent three-face full-incidence scan

Date: 2026-08-30

Status: numerical route selection only; **not a proof**.

## Scope

The scan exhausts the three translation classes of straight three-face chains and the six
translation classes of bent three-face chains, preserving every `h/m/c` incidence label.  For
each class it evaluates the full Bell-input Gram expression, every block-highest original side
output, and every fixed original-side cover of cardinality at most four.

The finite grid used base-label offsets

`0, 1, 2, 4, 8, 16, 32, 64`

in both Dynkin-label directions and 24,000 random simplex points per base-label pair (half
ordinary Dirichlet and half corner-biased Dirichlet).

## Results

- All nine chain classes have seven input and seven environment blocks.
- No sampled point survived the global original-side filter.  The smallest observed value of
  `Bell entropy - 2 min(original side entropies)` was approximately `0.318379419939` bit.
- A fixed two-side cover was not uniform on two of the nine classes and was numerically fragile
  on two further classes (`0.000516...` and `0.008252...` bit).
- Every class admitted a sampled-positive fixed three-side cover.  The nine worst sampled
  margins ranged from `0.189320346400` to `0.396614700117` bit.
- Fixed four-side covers increased the observed margins, but introduce an extra simplex variable.

The appropriate next proof route is therefore a **three-original-side cover**, with the other
four input blocks endpoint-reduced while retaining all environment-sharing Gram correlations.
Before exact certification, the selected covers must be stressed at highly asymmetric and very
large labels because a finite-label scan cannot control the compactified boundary.

## Large-label stress test

A second deterministic scan used 80,000 simplex samples per class and the Cartesian label-offset
set

`0, 1, 2, 4, 16, 64, 1024, 1000000`.

All nine selected fixed-three covers remained positive.  The smallest observed margin was
`0.093037809961` bit for the bent class `((-3,0),(-2,1),(0,0))` at the smallest allowed base
labels `(3,2)`.  The smallest observed margin among the three straight classes was
`0.182178187362` bit.  This materially reduces the risk of a simple asymptotic failure but remains
finite sampling, so the node status stays `NUMERICAL`.

## Per-class best fixed-three margins

| shape | translated face cluster | selected original input offsets | sampled worst margin (bit) |
|---|---|---|---:|
| straight | `((-4,2),(-2,1),(0,0))` | `((-3,2),(-1,1),(1,0))` | 0.292383097136 |
| bent | `((-3,0),(-2,1),(0,0))` | `((-1,-2),(-1,1),(1,0))` | 0.189320346400 |
| bent | `((-3,0),(-1,-1),(0,0))` | `((-2,0),(1,0),(2,-2))` | 0.350378981224 |
| bent | `((-3,3),(-2,1),(0,0))` | `((-2,3),(-1,1),(1,0))` | 0.396614700117 |
| bent | `((-3,3),(-1,2),(0,0))` | `((-2,3),(0,2),(1,0))` | 0.321362423608 |
| straight | `((-2,-2),(-1,-1),(0,0))` | `((0,-1),(1,0),(2,-2))` | 0.228763630677 |
| straight | `((-2,4),(-1,2),(0,0))` | `((-1,4),(0,2),(1,0))` | 0.220793643125 |
| bent | `((-1,-1),(-1,2),(0,0))` | `((0,2),(1,0),(2,-2))` | 0.356672211421 |
| bent | `((-1,-1),(0,-3),(0,0))` | `((-1,-2),(1,0),(2,-2))` | 0.241309954766 |

## Reproduction

Run:

```text
<home>/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  holevo-extensive-violation/tools/scan_su3_chain_three_face_clusters.py
```

The implementation is
`holevo-extensive-violation/tools/scan_su3_chain_three_face_clusters.py`.

The large-label pressure test is
`holevo-extensive-violation/tools/stress_su3_chain_three_face_fixed_three_covers.py`.

