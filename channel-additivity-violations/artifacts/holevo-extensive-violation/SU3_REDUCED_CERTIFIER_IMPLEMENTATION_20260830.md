# SU(3) reduced-sector certifier implementation record

Date: 2026-08-30

Status: exact checker implementation and bounded smoke verification complete; **no full adaptive
certificate was run, and this record does not support a canonical-node assessment change**.

## 1. Linked implementation

This record implements the reduced routes proposed in
[SU3_REMAINING_ORIENTATION_PARALLEL_ANALYSIS_20260830.md](SU3_REMAINING_ORIENTATION_PARALLEL_ANALYSIS_20260830.md).
The exact checker is:

[certify_su3_reduced_sector_covers.py](../tools/certify_su3_reduced_sector_covers.py).

The tool link above is the canonical source for this implementation record.  No canonical YAML
node was modified.  The earlier floating-point route selector remains explicitly non-certificate:

[analyze_su3_remaining_orientation_shortcuts.py](../tools/analyze_su3_remaining_orientation_shortcuts.py).

## 2. Safety and execution boundary

The new checker defaults to:

1. exact rational reconstruction of every endpoint branch;
2. compactification and common-denominator Bernstein conversion;
3. exact construction and coverage validation of the requested initial sector boxes;
4. exact initial-box range assessment; and
5. an optional, explicitly bounded number of smoke-test de Casteljau splits.

It does **not** enter the adaptive certificate loop unless `--certificate` is explicitly supplied.
No command in this implementation run supplied that flag.  The seven pre-existing long-running
SU(3) processes were not stopped, restarted, signalled, or given modified input files.  The new
checker ran in separate, low-priority processes which exited after their smoke checks.

## 3. Parameterized exact backend

The implementation uses one `SectorSpec` abstraction with:

- a labelled three-face `Configuration`;
- the free residual label axes (`P,Q`, only `Q`, or none);
- exactly fixed label axes;
- the number of retained simplex coordinates; and
- an initial compact sector constructor.

The sparse-polynomial dimension is set per process/spec before reconstruction.  There is no dummy
coordinate: specializing `P=0` deletes the `P` axis, and specializing `P=Q=0` deletes both label
axes.  The public `gram_t`, retained original-side distributions, union construction, denominator
construction, rational logarithm bounds, and common-denominator control arithmetic are reused
unchanged.

### 3.1 Exact specialization

The public label-only Gram and side denominator polynomials are first constructed in variables
`(P,Q,coordinates)`.  A fixed label is then substituted term by term and its exponent axis is
deleted.  The resulting reduced polynomial is used as the denominator during interpolation, so a
face/slice is not represented by a full-dimensional box of zero width.

For each endpoint pattern the checker interpolates the cleared Gram numerator on its complete
degree grid.  It then compares the reconstructed ratio with the public direct formula at two
additional non-grid rational points.  Every retained side component is reconstructed and checked
the same way.  A mismatch raises immediately before compactification.

### 3.2 Compactification and initial sectors

Every remaining free label `X` is transformed exactly by

\[
 X={u\over1-u},\qquad
 \widetilde f=(1-u)^{d_X}f\!\left({u\over1-u}\right).
\]

The checker then converts numerator and denominator polynomials to exact rational Bernstein
controls and to the existing integer common-denominator representation.

Initial sectors are constructed only by exact midpoint de Casteljau splits:

- input low: six adjacent slabs covering `0<=a<=63/64`;
- input high: the single slab `63/64<=a<=1`;
- bent main: the right half `1/2<=a<=1`, equivalent to `P>=1`;
- bent Q-face: after exact `P=0` specialization, the right half `1/2<=b<=1`, equivalent to
  `Q>=1`;
- bent origin: after exact `P=Q=0` specialization, the full three-weight cube.

The low-sector coverage verifier checks the first endpoint, last endpoint, and every adjacency;
the other verifiers compare their exact rational bounds with the registered sector.

### 3.3 Exact search features

The opt-in full loop contains two speed features whose use does not alter proof semantics:

1. **Active-pattern pruning.**  On a box, pattern `e` is deleted if its exact upper bound is below
   the largest exact lower bound of another pattern.  The surviving pattern controls, not a
   controlwise mixed envelope, are passed to descendants.
2. **Exact trial-axis scoring.**  Every available axis is split by exact de Casteljau arithmetic;
   the axis certifying the most children and then maximizing the smaller child margin is selected.

These paths were syntax-checked and their constituent operations were exercised by smoke splits,
but a complete adaptive run was deliberately not started.

## 4. Implemented configurations

| CLI sector | retained original blocks | free dimension | endpoint patterns | Gram degrees | side degrees |
|---|---|---:|---:|---|---|
| `input-low` | `(-1,1),(1,0),(2,-2)` | 5 | 24 | `(12,12,2,2,2)` | `(5,5,1,1,1)` |
| `input-high` | `(-2,0),(1,-3),(1,0)` | 5 | 24 | `(12,12,2,2,2)` | `(4,4,1,1,1)` |
| `bent-main` | `(-1,1),(1,0)` | 4 | 72 | `(14,12,2,2)` | `(4,4,1,1)` |
| `bent-q-face` | `(-1,1),(1,0)` | 3 | 72 | `(12,2,2)` | `(4,1,1)` |
| `bent-origin` | `(-1,-2),(-1,1),(1,0)` | 3 | 36 | `(2,2,2)` | `(1,1,1)` |

The dimension and degree tuples in this table were produced by completed exact reconstruction,
not copied from the route proposal.

## 5. Smoke verification results

All five sectors completed full endpoint reconstruction and their two extra rational identity
tests.  `rational_range_common` successfully evaluated every initial box, which also checks that
no negative denominator control or unmatched projective zero was encountered there.

| sector | initial boxes | exact compact bounds | initial active patterns | initial `t_upper` range |
|---|---:|---|---|---|
| `input-low` | 6 | `[0,1/2]`, `[1/2,3/4]`, ..., `[31/32,63/64]` on `a` | 24/24 | `0.813361`--`0.846644` |
| `input-high` | 1 | `[63/64,1]` on `a` | 24/24 | `0.812925` |
| `bent-main` | 1 | `[1/2,1]` on `a` | 72/72 | `0.882806` |
| `bent-q-face` | 1 | `P=0`, `[1/2,1]` on `b` | 72/72 | `0.874939` |
| `bent-origin` | 1 | `P=Q=0`, `[0,1]^3` weights | 36/36 | `0.913158` |

One exact midpoint split was also performed for each sector command.  Both children in every
smoke split passed denominator/range evaluation.  The coarse initial boxes and their first
children generally had negative entropy margins.  This is expected and is **not** a route
counterexample: the Bernstein/entropy enclosures are intentionally coarse before adaptive
subdivision.

The initial boxes did not yet prune branches.  Active-pattern pruning is expected to become useful
only after weight and label localization; the smoke run was not extended to discover a favorable
depth.

## 6. Commands run

From the repository root:

```text
python3 -m py_compile \
  holevo-extensive-violation/tools/certify_su3_reduced_sector_covers.py

PYTHONPATH=holevo-extensive-violation/tools nice -n 10 python3 \
  holevo-extensive-violation/tools/certify_su3_reduced_sector_covers.py \
  bent-origin --smoke-splits 1

PYTHONPATH=holevo-extensive-violation/tools nice -n 10 python3 \
  holevo-extensive-violation/tools/certify_su3_reduced_sector_covers.py \
  bent-q-face --smoke-splits 1

PYTHONPATH=holevo-extensive-violation/tools nice -n 10 python3 \
  holevo-extensive-violation/tools/certify_su3_reduced_sector_covers.py \
  bent-main --smoke-splits 1

PYTHONPATH=holevo-extensive-violation/tools nice -n 10 python3 \
  holevo-extensive-violation/tools/certify_su3_reduced_sector_covers.py \
  input-low --smoke-splits 1

PYTHONPATH=holevo-extensive-violation/tools nice -n 10 python3 \
  holevo-extensive-violation/tools/certify_su3_reduced_sector_covers.py \
  input-high --smoke-splits 1
```

No `--certificate` invocation was made.

## 7. Limitations and next exact step

This implementation establishes that all five proposed reduced rational problems can be exactly
reconstructed, compactified, restricted to the intended initial sectors, bounded, and split.  It
does not establish that adaptive subdivision terminates with positive margins.

The 4D and 5D full reconstructions take several minutes because the current public approach calls
the complete exact `gram_t` formula independently on every branch/grid point.  Before production
runs, it would be useful to add a reviewed durable cache keyed by checker hash/configuration, or to
interpolate shared endpoint unary/pair potentials once.  No cache was written in this smoke run.

The next evidence-producing action is one bounded production run per sector with terminal output
captured under `artifacts/`.  Only after all three bent pieces or both input pieces complete should
their sector-cover arguments be assembled and reviewed.  Until then, this tool and record remain
implementation evidence, not a Bell no-gap certificate.
