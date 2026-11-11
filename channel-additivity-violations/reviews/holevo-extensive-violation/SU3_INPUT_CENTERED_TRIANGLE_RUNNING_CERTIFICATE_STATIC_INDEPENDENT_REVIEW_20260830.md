# Independent static review: running input-centered triangle SU(3) certificate

Date: 2026-08-30

Reviewer: Codex independent review agent `/root/su3_shorter_route`.

## Independence and scope

This is a static pre-review of the still-running process for route
`fixed-four-original-side-cover` of
`HEXT.su3-input-centered-triangular-three-face-bell-no-go`. I did not author the driver, did not
start or interact with session 71901 / PID 85955, did not consume its output pipe, and did not run
the reconstruction or certificate. I performed only read-only source inspection and small exact
enumerations of the registered configuration. I did not edit canonical YAML or any reviewed
source. This report is the only project file created by the review.

At the last check, PID 85955 was still running. Accordingly this report does **not** review a
completed transcript and does **not** authorize promotion. More importantly, the live process has
a separate source-provenance defect described below: three files in its recursive local import
closure have current filesystem modification times after the process launch. The current source
can be reviewed statically, but its hashes cannot retrospectively bind the already-running Python
process.

## Exact scope, statement bindings, and present verdict

I read `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full. Their reviewed SHA-256 hashes are:

| protocol | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |

The exact statement bindings reviewed are:

| object | exact statement hash | present assessment |
|---|---|---|
| `HEXT.su3-three-face-cluster-classification` claim | `sha256:d9e686c2b1a4146bd9bcb20efd0f60a15a513a6d53e92f8ea5559cfd9e9778cf` | premise currently `PROVED` |
| `HEXT.su3-fixed-original-side-endpoint-lemma` claim | `sha256:7435a8e46d009acbe7dabce7c520d1cbbbb45f7943c7b98cdbeef7065ff71398` | premise currently `PROVED` |
| `fixed-four-original-side-cover` implication | `sha256:901549c889c941f1e9e623495d96be7006fc8a3d7f47ff655a5791ce159f1692` | static design **PASS**, execution/provenance **PENDING** |
| `HEXT.su3-input-centered-triangular-three-face-bell-no-go` claim | `sha256:cb12bc058227ac0a1b806383f5f642a1538fc16218de2b1788d254edfcc2aa2e` | **do not promote** |

The target node file had SHA-256
`3dd929445fc403c59f513b8e2bd40b59ca1a159545a76f9329fd4551befbd47e` at review time.
This review covers only the fixed-four route for the labelled input-centered cluster. It does not
revive the separately `REFUTED` fixed-three route, adjudicate the alternative label-sector route,
transfer by an unlisted symmetry, or infer an aggregate triangular/three-face theorem.

The present verdict is:

1. The mathematical and exact-computation design in the **current checked-in source** passes this
   static audit.
2. The live execution is unfinished, so it cannot yet discharge the route.
3. Even if it terminates with exit status zero, it is not promotion-grade unless its launch-time
   source closure is recovered and bound. Current file hashes alone are insufficient because the
   process predates three current source versions.

## Reviewed proposer-side material

| material | SHA-256 | role in this review |
|---|---|---|
| `artifacts/SU3_INPUT_CENTERED_TRIANGLE_FIXED_THREE_COVER_FAILURE_20260830.md` | `f5701aac62325bf1fde0d7de65e4bb92cf252ba0b7eff61d242a95a49f8a1359` | exact obstruction to the retired three-side cover and motivation for four legal original-side outputs |
| `artifacts/SU3_INPUT_CENTERED_TRIANGLE_FOUR_SIDE_ASYMPTOTIC_SCAN_RUN_20260830.txt` | `7228c94d98ced447542a7b7d83ff3bd098755d8eca0a084b6cca26ea5d350ebc` | numerical asymptotic scan only; not an exact certificate |
| `artifacts/SU3_REMAINING_ORIENTATION_PARALLEL_ANALYSIS_20260830.md` | `5be48b654de6330ff43cde26a2c8050f5c278f8eb4afb1204b98869aa4e64b84` | alternative reduced-sector analysis; not the live route |
| `artifacts/SU3_REDUCED_CERTIFIER_IMPLEMENTATION_20260830.md` | `98bc1ac34c5b633bc90cdaabba4d34ec528cf414f7db9abd340cf56b2b4f6702` | alternative checker implementation; not the live route |

The asymptotic scan's approximately 0.234819-bit sampled minimum is useful route-selection
evidence only. It neither covers compact boundaries nor substitutes for exact Bernstein leaf
acceptance.

## Live process status and the launch-source provenance defect

At 2026-08-30 21:55 EDT, the process information was:

| field | observed value |
|---|---|
| PID / requested session | `85955` / `71901` |
| launch time | `Sun Aug 30 07:24:57 2026` EDT |
| elapsed time | approximately 14 h 30 min |
| state | running (`Rs`) |
| command | `/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python holevo-extensive-violation/tools/certify_su3_input_centered_triangle_sixdim.py` |
| working directory | repository root |
| standard input | `/dev/null` |
| standard output/error | pipes owned by the Codex execution service |

I deliberately did not poll or write to session 71901: doing so could consume or alter the shared
terminal record. No completed exact-certificate transcript was present in the repository.

An independent AST traversal of local imports from the current driver found exactly these seven
project files:

| current local Python import closure | current SHA-256 | filesystem mtime relative to launch |
|---|---|---|
| `tools/certify_su3_input_centered_triangle_sixdim.py` | `3c34647bebec2dc3a17c54eeeecce4da45b23e8544cba76d19794e7688bf00a0` | 2026-08-30 11:53:34 EDT — **after launch** |
| `tools/certify_su3_triangular_three_face_clusters.py` | `37b481a43c6f646a541ed9e0b87f9ac744e9c565ff1f6df1f75da0b3adbb6573` | 2026-08-30 11:53:21 EDT — **after launch** |
| `tools/certify_su3_adjacent_elementary_faces.py` | `68634062aca3293f3f2b483c4e05b441de8d9ba1ae16bf301f5c83c9e4797383` | 2026-08-30 04:47:48 EDT — before launch |
| `tools/certify_su3_all_elementary_cycles.py` | `4109cdfc63242e637f843280edc17aa9be126b0d1e824b9b25689048db264fa2` | 2026-08-30 04:18:41 EDT — before launch |
| `tools/certify_su3_highest_edge_adjacent_faces.py` | `09a37c01c9afd6d480227c9a7be9e9d3ff5b2461e542adef995df850e62fbc49` | 2026-08-30 05:12:25 EDT — before launch |
| `tools/scan_su3_adjacent_elementary_faces.py` | `fbe6a888f447d120f4c5f1cefe8304bec3665c78a8525b3c2bbf4497c955e0cd` | 2026-08-30 04:42:01 EDT — before launch |
| `tools/su3_common_den_controls.py` | `39f0e98fac092a101c3d8eeeeac939c7683af1851d09a1a6f8d8c85e97f8584c` | 2026-08-30 11:52:47 EDT — **after launch** |

The scan module's `numpy` imports are lazy inside scan-only functions and are not invoked by the
certificate path. Otherwise, the executed path uses the Python standard library and the local
files in this closure.

Python loads these modules into memory near process startup. Consequently, the process is using
the pre-11:52/11:53 contents of the three emphasized files, not necessarily the current contents
whose hashes appear in this table. I found no immutable launch manifest, prelaunch source bundle,
or second copy of the old driver in the repository or broader Codex workspace. Without such a
record, the current closure table must **not** be copied into a terminal transcript as though it
were the closure executed by PID 85955.

This is a blocking provenance issue, not evidence that the launch-time implementation was wrong.
It can be cured only by a trustworthy launch-time snapshot/hash record, or by recovering the
exact launch source and independently reviewing it (or an exact, reviewable equivalence/diff to
the audited source). A terminal success line and current-source hashes, by themselves, do not cure
it.

## Static findings for the current checked-in source

### FINDING-SU3-ICT-RUN-01 — configuration and all 12 correlated endpoints are complete

**Applies to:** route implication
`sha256:901549c889c941f1e9e623495d96be7006fc8a3d7f47ff655a5791ce159f1692`.

**Stable source locators:** `certify_su3_input_centered_triangle_sixdim.py`, object `CONFIG`;
`certify_su3_triangular_three_face_clusters.py`, functions `build_union`, `minimum_base`,
`endpoint_patterns`, and `all_weights`.

The current driver fixes cluster
`((-2,1),(-1,-1),(0,0))` and retains the four binary input offsets
`(-2,0),(-1,1),(1,0),(2,-2)`. Independent exact enumeration gives:

| input offset | ordered branch set | treatment |
|---|---|---|
| `(-2,0)` | `c,m` | retained binary |
| `(-1,-2)` | `c,m` | eliminated |
| `(-1,1)` | `h,m` | retained binary |
| `(0,-1)` | `h,c,m` | eliminated |
| `(1,-3)` | `h,c` | eliminated |
| `(1,0)` | `h,m` | retained binary |
| `(2,-2)` | `h,c` | retained binary |

Thus the three eliminated simplex degrees are exactly `2,3,2`. Their Cartesian product contains
exactly 12 distinct correlated endpoints, from `(0,0,0)` through `(1,2,1)` in registered order.
The complete endpoint tuple is passed into the full Gram calculation; diagonal and cross terms
are not optimized independently.

The minimum base shift is `(2,3)`. The shifted environment offsets are
`(0,4),(1,2),(2,0),(2,3),(3,1),(4,2)`, and the shifted input offsets are
`(0,3),(1,1),(1,4),(2,2),(3,0),(3,3),(4,1)`. All labels are nonnegative already at residual
`P=Q=0`, and every listed branch is valid there. The compact variables therefore cover the whole
finite integer-label domain claimed (indeed the rational calculation covers a stronger continuous
residual-label domain).

**Verdict:** static PASS for the current source; no missing endpoint or invalid smallest-label
branch.

### FINDING-SU3-ICT-RUN-02 — all four side outputs retain the original-channel quantifier

**Applies to:** the same implication and the already-`PROVED` fixed-original-side endpoint lemma.

**Stable source locators:** `certify_su3_triangular_three_face_clusters.py`, functions
`retained_side_distributions`, `reconstruct_side_numerators`, and
`correlated_side_entropy_upper`.

The side reconstruction is performed once, outside the 12-pattern loop. Its inputs are the
configuration, union, labels, and four retained binary weights; it has no eliminated endpoint
argument. Hence the candidate outputs are outputs of the original channel rather than of an
endpoint replacement. Their ordered types are `c/m`, `h/m`, `h/m`, and `h/c`, with current
q-constants `(3,4,3,1)`.

At the all-zero label/weight boundary, independent exact evaluation gives the four normalized,
nonnegative triples

`(1/2,1/2,0)`, `(1/3,2/3,0)`, `(1/5,4/5,0)`, and `(1/8,7/24,7/12)`.

An additional rational interior evaluation was also normalized and nonnegative. The two `h/m`
outputs use binary entropy. The `h/c` output uses the exact chain decomposition

`H(p0,p1,p2) = h(p0) + (p1+p2) h(p1/(p1+p2))`,

with its conditional label ratio bounded in the conservative direction. The `c/m` output uses
componentwise directed ternary bounds. Taking the minimum of four separately valid entropy upper
bounds remains an upper bound on the minimum entropy of these four legal outputs.

**Verdict:** static PASS; the original-side quantifier is retained exactly.

### FINDING-SU3-ICT-RUN-03 — common denominators and tensor reconstruction degrees are sufficient

**Stable source locators:** `certify_su3_triangular_three_face_clusters.py`, functions
`gram_denominator`, `reconstruct_gram_numerator`, `side_denominator`, and
`reconstruct_side_numerators`; driver reconstruction constants and loops.

The driver deliberately sets the imported six-variable Gram backend to `NVAR=6`; the polynomial
helpers read that module global dynamically. The triangular helper operations used on this path do
not silently truncate to their own five-variable default.

For the registered input-centered union, the exact Gram common denominator has degree
`(12,12,0,0,0,0)` and is strictly positive at every finite `P,Q>=0`. The four retained binary
weights enter diagonal terms quadratically and cross terms separately affinely, so reconstruction
degree `(12,12,2,2,2,2)` is sufficient. Each of the 12 patterns is interpolated on
`13*13*3^4 = 13,689` exact rational grid points and checked at two additional rational points.

The side common denominator has exact degree `(7,6,0,0,0,0)`. Side rows are separately affine in
the four retained weights, so degree `(7,6,1,1,1,1)` is sufficient. Its tensor interpolation uses
`8*7*2^4 = 896` exact rational grid points and an extra rational verification point. The common
denominators clear the environment/input dimension factors; no finite-domain zero or higher label
degree is hidden by the interpolation ansatz.

All reconstruction arithmetic is `fractions.Fraction`. The checks in the running program are
valuable only when their terminal output is bound to the actual launch source; the degree argument
above is an independent static argument for the current source.

**Verdict:** static PASS for exact degree sufficiency and finite-domain denominator positivity.

### FINDING-SU3-ICT-RUN-04 — exact compactification and common-denominator Bernstein controls cover boundaries

**Stable source locators:** `certify_su3_highest_edge_adjacent_faces.py`, functions `compactify`
and `bernstein_coefficients`; `su3_common_den_controls.py`, functions
`rational_range_common` and `split_common_controls`; shared `certify` backend.

The substitutions `P=a/(1-a)` and `Q=b/(1-b)` multiply numerator and denominator by the same
homogenizing powers: `(1-a)^12(1-b)^12` for the Gram ratios and
`(1-a)^7(1-b)^6` for side ratios. The rational functions are unchanged on every finite label;
the closed faces `a=1` or `b=1` bound all limiting approaches. The theorem itself needs only finite
integer labels, while the closed projective faces ensure that no approach to infinity is omitted.

With nonnegative denominator Bernstein controls, each rational value is a convex combination of
matched numerator/denominator control ratios. The backend compares those ratios by exact integer
cross multiplication. A negative denominator control raises; an unmatched zero denominator also
raises. Dyadic de Casteljau subdivision is exact and preserves matched common-denominator
controls.

The stack begins with the full closed six-cube and only accepts boxes whose final margin is
strictly positive. Each failed box is bisected in one coordinate, with depth cap six in every
coordinate. If every coordinate is exhausted without a certificate, the code raises an assertion,
so exit zero after stack exhaustion would cover all label faces, all four weight boundaries, and
the interior. Shared boundaries of dyadic children are harmless.

**Verdict:** static PASS; no compact face or interpolation boundary is omitted by the current
algorithm.

### FINDING-SU3-ICT-RUN-05 — logarithm and entropy directions imply the target strict inequality

**Stable source locators:** `certify_su3_all_elementary_cycles.py`, functions
`reduced_log_bounds`, `log_bounds`, `entropy_bounds`, and `isotropic_probabilities`;
`certify_su3_adjacent_elementary_faces.py`, function `component_entropy_upper`; shared backend
entropy functions and leaf acceptance test.

Power-of-two reduction makes `z=(x-1)/(x+1)` nonnegative. The 24-term odd `atanh` partial series
is a logarithm lower bound and its explicit positive geometric tail supplies the upper bound.
Restoring a negative power of two uses reversed endpoints for the negative multiple of `ln 2`, as
required. The resulting entropy intervals are directed.

The isotropic Bell entropy is decreasing in its Gram parameter, so the Bell lower bound is
evaluated at the certified `t_upper`. Binary entropy intervals account for the maximum at `1/2`.
The componentwise ternary bound uses the correct monotonicity split around `1/e`, the rigorous
rational comparison `1/e < 3/8`, and an upper enclosure of `ln 3`. For the actual `h/c` retained
block, the chain conditional bound uses q-constant one and its correct label monotonicity.

The exact leaf test is

`bell_lower - 2 * side_upper > 0`

as a `Fraction`. It therefore has the right direction for the strict Bell-input no-gap inequality
required by the endpoint lemma. The later display via `float(...):.12e` is only an approximate
human-readable rendering and must not be cited as a directed exact lower bound.

**Verdict:** static PASS for all logarithm, entropy, endpoint, minimum, and inequality directions.

### FINDING-SU3-ICT-RUN-06 — completion is fail-closed, but has not occurred

Every unresolved box is divided into exactly two children. If the final transcript reports `L`
certified leaves after stack exhaustion, the complete binary-tree accounting must give `L-1`
internal boxes and `2L-1` total processed boxes. For any recorded progress line immediately after
a box pop, the implementation's stack/certificate accounting gives a corresponding binary-tree
consistency check. An unresolved depth-six box raises rather than being silently discarded.

The final leaf count, smallest-margin rendering, and success sentence are printed only after the
stack is empty. Thus a captured exit-zero terminal record containing those final lines is necessary
execution evidence. It is not presently available. A process merely remaining alive or reaching a
large progress count proves nothing about uncovered boxes.

**Verdict:** completion criterion statically PASS; live execution **PENDING**.

## Required terminal dossier after the process ends

A final independent reviewer should require all of the following, without substituting current
source metadata for launch metadata:

1. The exact command, repository working directory, interpreter path and version, session/PID,
   launch/end timestamps, and exit status.
2. The uninterrupted captured output, including configuration identity, all 12 Gram
   reconstruction lines with degree `(12,12,2,2,2,2)`, the four side groups with degree
   `(7,6,1,1,1,1)`, useful progress checkpoints, the final certified-leaf count, the smallest
   recorded dyadic box, the success line, and absence of a depth-limit assertion or traceback.
3. Binary-tree consistency: for final leaf count `L`, total processed boxes `2L-1` (or enough
   recorded progress/accounting data to verify the equivalent invariant).
4. Exact positivity semantics. The proof fact is that every accepted margin is a positive
   `Fraction`; the printed float is not directed. Prefer recording the exact numerator and
   denominator of the minimum retained margin, or a separately proved directed rational lower
   bound, in addition to the approximate decimal.
5. A **launch-time** complete recursive local import closure and hashes for the seven files, with a
   source snapshot or other immutable evidence. Because three current files postdate launch, a
   post-run hash of the working tree is not sufficient. If a prelaunch bundle is recovered, audit
   that bundle directly; if an equivalence/diff is proposed, record and independently review it.
6. SHA-256 hashes of the immutable completed transcript and final proposer artifact, and exact
   linkage from the route to those records.
7. Confirmation that every premise remains `PROVED` at the exact hashes above and that the route
   and claim statement hashes have not changed. Do not infer an aggregate claim.

If items 1–7 are complete and the recovered launch source passes independent code review, the
already-`PROVED` premises allow a later reviewer to adjudicate the route and atomic claim for
promotion. Until then, both must remain below `PROVED`.

## Final adjudication

| component | verdict |
|---|---|
| current checked-in four-side configuration and 12 endpoint enumeration | **PASS (static)** |
| original-side quantifier and four legal retained outputs | **PASS (static)** |
| reconstruction degrees and common denominators | **PASS (static)** |
| compactification, exact Bernstein subdivision, and boundary coverage | **PASS (static)** |
| directed logarithm/entropy bounds and strict Fraction acceptance | **PASS (static)** |
| live execution completion | **PENDING** |
| live execution source binding | **BLOCKED by missing launch-time source provenance** |
| route promotion | **DO NOT PROMOTE** |
| atomic node promotion | **DO NOT PROMOTE** |

The blocker is deliberately narrow: it does not refute the route, and it does not undermine the
static validity of the current source. It prevents the still-running process from being treated as
an exact certificate of that audited source until launch-time provenance is supplied.
