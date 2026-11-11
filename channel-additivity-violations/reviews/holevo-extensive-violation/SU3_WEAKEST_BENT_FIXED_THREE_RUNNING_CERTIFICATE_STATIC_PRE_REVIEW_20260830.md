# Independent static pre-review: weakest-bent fixed-three SU(3) certificate

Date: 2026-08-30

Reviewer: independent Codex review context `/root/su3_weakest_static_review`.

Status: **STATIC PRE-REVIEW ONLY — RUN IN PROGRESS — FRESH RERUN REQUIRED — NO PROMOTION AUTHORIZED**.

## Independence, scope, and noninterference

I did not author the weakest-bent certificate driver, its shared exact core, the target node, or
the existing numerical evidence. I read `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full and
performed a static adversarial review while the already-running process remained active. I did
not poll or write to unified terminal session `78883`, consume that session's output, signal or
otherwise interfere with PID `90693`, or edit canonical YAML.

This review covers only the atomic orientation
`HEXT.su3-bent-hc-hm-hm-three-face-bell-no-go` and its route
`fixed-three-original-side-cover`. It checks the current checked-in configuration/orientation,
label and weight coverage, endpoint enumeration, retained-original-side quantifier, exact
reconstruction degree bounds, compactification, common-denominator Bernstein subdivision,
directed entropy enclosures, and fail-closed terminal logic. It also checks whether the live
execution can be bound to the source now under review.

This review does not adjudicate the alternative `integer-sector-two-side-cover`, infer any other
bent or straight orientation, or promote the aggregate bent-chain conjunction. This report is the
only project file created by the review.

## Provisional verdict

The mathematical and exact-computation design in the **current checked-in source passes this
static audit**:

- the driver fixes exactly the registered bent cluster `((-3,0),(-2,1),(0,0))`;
- the retained original-side blocks are, in input order, `h/c`, `h/m`, and `h/m`;
- the other four blocks have simplex degrees `2,3,3,2`, hence exactly 36 correlated endpoint
  patterns;
- residual labels `P,Q>=0` cover every allowed translation from minimum base `(3,2)`;
- exact rational reconstruction uses sufficient tensor degrees `(14,12,2,2,2)` for the Gram
  functions and `(5,6,1,1,1)` for the retained-side distributions;
- the compact closed five-cube, its projective label faces, and all binary-weight boundaries are
  covered by exact common-denominator Bernstein controls; and
- every unresolved depth-seven box raises instead of being silently discarded.

However, the live run is not promotion-grade even if it later exits zero. PID `90693` launched at
`2026-08-30 09:20:15 -0400`, while the current shared triangular-cluster core was modified at
`11:53:21` and the current common-denominator backend at `11:52:47`. Python loaded its module code
near process startup, so the current hashes cannot identify the code executing in the live
process. The actual launch-time closure was not preserved in a reviewed immutable manifest.

This is a narrow evidence/provenance blocker, not a counterexample and not a defect in the current
mathematics. The live output may be retained as historical diagnostic evidence, but a **fresh run
from a source closure hashed and preserved before launch is mandatory before promotion**. Until
that fresh run completes and receives final independent review, the route and atomic node must
remain at most `NUMERICAL`.

## Exact statement and protocol bindings

The reviewed protocol hashes are:

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |

The repository-normalized exact statement hashes are:

| object | exact statement hash | present level / verdict |
|---|---|---|
| target claim | `sha256:00681fc2009f8475b2db7abf3490667716967fa2f1566b344aa2b04f44bb0212` | `NUMERICAL`; static PASS, no promotion |
| route `fixed-three-original-side-cover` implication | `sha256:3c459980bcd30c05ab77b6701b2bdfa73e5babe32b386fb2bea02faf2baee1ac` | `NUMERICAL`; static PASS, execution/provenance blocked |
| `HEXT.su3-three-face-cluster-classification` premise | `sha256:d9e686c2b1a4146bd9bcb20efd0f60a15a513a6d53e92f8ea5559cfd9e9778cf` | `PROVED` |
| `HEXT.su3-fixed-original-side-endpoint-lemma` premise | `sha256:7435a8e46d009acbe7dabce7c520d1cbbbb45f7943c7b98cdbeef7065ff71398` | `PROVED` |

Raw canonical-node hashes at review time were:

| node file | SHA-256 |
|---|---|
| target node YAML | `baeaa2d1ff7eca6c85b6307be633e0abfe4ebaef76b247dcdf077abe0e7fe257` |
| classification premise YAML | `c193d98053bd31f6a8a4eaace0289b669de66b5aa5c2f2e9dce040b32dfa4aa2` |
| fixed-original-side premise YAML | `d327927af5079476df26f926c1cf6e3bfd45251695472736d615f7c28948069c` |

## Existing proposer-side evidence inspected

| object | SHA-256 | scope |
|---|---|---|
| `artifacts/SU3_CHAIN_THREE_FACE_SCAN_20260830.md` | `95bd5a495f79cc18e3119177f6dbf9e288242329ac44b58c3e6de8e10e7e6b70` | finite route selection only |
| `artifacts/SU3_CHAIN_THREE_FACE_FIXED_THREE_STRESS_RUN_20260830.txt` | `4f48a84e747c3b4e7257d05d6a93fcdc3b3ccb5738ea168ab8d5aa6b282c0ed4` | finite large-label pressure only |
| `artifacts/SU3_THREE_FACE_CLUSTER_CLASSIFICATION_20260830.md` | `177ab70fa562b403419f534a5271c812382d03317e48d0e63c034a6c8baccc45` | classification premise |
| `artifacts/SU3_FIXED_ORIGINAL_SIDE_ENDPOINT_LEMMA_20260830.md` | `8f2f791e929688047bddb7af5f7d95c69a687eeae38ed52fd9df9cf6262d238f` | endpoint/original-side premise |

The stress record's approximately `0.093037809961`-bit minimum is useful falsification pressure,
but it neither covers continuous weights nor the compactified label boundary.

## Current-source import closure and live-run provenance

An independent AST traversal of recursive project-local imports from the current driver found
exactly the following seven files. This is the closure of the **current source**, not a recovered
closure of the already-running process.

| current local source | SHA-256 | mtime (`-0400`) relative to live launch |
|---|---|---|
| `tools/certify_su3_weakest_bent_three_face_cluster.py` | `056111454454f3c759ff35a2ea62875d65049b175166192f35bcfd636a21c251` | `2026-08-30 09:20:12` — before launch |
| `tools/certify_su3_triangular_three_face_clusters.py` | `37b481a43c6f646a541ed9e0b87f9ac744e9c565ff1f6df1f75da0b3adbb6573` | `2026-08-30 11:53:21` — **after launch** |
| `tools/certify_su3_adjacent_elementary_faces.py` | `68634062aca3293f3f2b483c4e05b441de8d9ba1ae16bf301f5c83c9e4797383` | `2026-08-30 04:47:48` — before launch |
| `tools/certify_su3_all_elementary_cycles.py` | `4109cdfc63242e637f843280edc17aa9be126b0d1e824b9b25689048db264fa2` | `2026-08-30 04:18:41` — before launch |
| `tools/certify_su3_highest_edge_adjacent_faces.py` | `09a37c01c9afd6d480227c9a7be9e9d3ff5b2461e542adef995df850e62fbc49` | `2026-08-30 05:12:25` — before launch |
| `tools/scan_su3_adjacent_elementary_faces.py` | `fbe6a888f447d120f4c5f1cefe8304bec3665c78a8525b3c2bbf4497c955e0cd` | `2026-08-30 04:42:01` — before launch |
| `tools/su3_common_den_controls.py` | `39f0e98fac092a101c3d8eeeeac939c7683af1851d09a1a6f8d8c85e97f8584c` | `2026-08-30 11:52:47` — **after launch** |

The certificate path otherwise uses only Python standard-library modules. The scan helper's
`numpy` import is lazy inside scan-only functions and is not executed by this certificate route.

At `2026-08-30 22:34 -0400`, read-only process inspection reported:

| field | observed value |
|---|---|
| requested unified session | `78883` (not read or polled here) |
| PID | `90693` |
| launch time | `Sun Aug 30 09:20:15 2026 -0400` |
| elapsed time | approximately 13 h 14 min |
| state / CPU | running (`Rs+`) / approximately 98% CPU |
| working directory | repository root |
| command | `/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python holevo-extensive-violation/tools/certify_su3_weakest_bent_three_face_cluster.py` |

The two post-launch modifications are promotion-blocking. In particular, the current core imports
and executes `su3_common_den_controls.py`, but the pre-11:52 launch-time core may have had a
different backend or import graph. Post-run hashing of the current working tree cannot repair that
uncertainty. The only clean repair for this route is a fresh run whose complete source closure is
preserved and hashed before launch.

## Static findings for the current checked-in source

### FINDING-SU3-WB-STATIC-01 — PASS: configuration, label domain, and all 36 endpoints match the atomic node

**Applies to:** route implication
`sha256:3c459980bcd30c05ab77b6701b2bdfa73e5babe32b386fb2bea02faf2baee1ac`
and target claim
`sha256:00681fc2009f8475b2db7abf3490667716967fa2f1566b344aa2b04f44bb0212`.

**Stable source locators:** `certify_su3_weakest_bent_three_face_cluster.py`, object `CONFIG`;
`certify_su3_triangular_three_face_clusters.py`, functions `build_union`, `minimum_base`,
`endpoint_patterns`, and `all_weights`.

The driver fixes configuration name `weakest-bent-fixed-three`, cluster
`((-3,0),(-2,1),(0,0))`, retained offsets `(-1,-2)`, `(-1,1)`, and `(1,0)`, all binary, and
expected endpoint count 36. Independent exact enumeration gives:

| input offset | ordered branch set | treatment |
|---|---|---|
| `(-3,-1)` | `c,m` | eliminated |
| `(-2,0)` | `h,c,m` | eliminated |
| `(-1,-2)` | `h,c` | retained binary |
| `(-1,1)` | `h,m` | retained binary |
| `(0,-1)` | `h,c,m` | eliminated |
| `(1,0)` | `h,m` | retained binary |
| `(2,-2)` | `h,c` | eliminated |

The four eliminated degrees are `2,3,3,2`, so their Cartesian product contains exactly 36
correlated patterns, from `(0,0,0,0)` through `(1,2,2,1)`. The endpoint generator inserts every
chosen vertex into one complete Gram expression; it does not maximize diagonal or cross terms
separately. The three retained binary coordinates cover their complete closed intervals.

The minimum translation is `(3,2)`. Above residual `P,Q>=0`, the shifted input offsets are
`(0,1),(1,2),(2,0),(2,3),(3,1),(4,2),(5,0)`, and the shifted environment offsets are
`(0,2),(1,0),(1,3),(2,1),(3,2),(4,0),(5,1)`. Every registered branch remains valid on the
smallest-label boundary. Hence residual nonnegative integer labels cover exactly all allowed
translations; the rational checker actually handles the stronger continuous domain `P,Q>=0`.

**Verdict:** static PASS; no omitted endpoint, invalid boundary branch, orientation substitution,
or unproved symmetry quotient.

### FINDING-SU3-WB-STATIC-02 — PASS: all three retained spectra are original-channel outputs

**Applies to:** the route implication above and the already-`PROVED`
fixed-original-side endpoint lemma.

**Stable source locators:** `certify_su3_triangular_three_face_clusters.py`, functions
`side_rows`, `retained_side_distributions`, `reconstruct_side_numerators`, and
`correlated_side_entropy_upper`.

The side distributions are reconstructed once from the three continuously varying retained
weights; they do not depend on the eliminated endpoint pattern. Thus they are outputs of the
original channel, not outputs of a replacement endpoint channel. Their branch types, shifted
input offsets, and `Q` constants are:

| retained input | type | shifted input offset | `Q` constant |
|---|---|---|---|
| `(-1,-2)` | `h/c` | `(2,0)` | `0` |
| `(-1,1)` | `h/m` | `(2,3)` | `3` |
| `(1,0)` | `h/m` | `(4,2)` | `2` |

At the smallest label and the all-zero retained coordinates, the exact side triples are

`(1/5,2/5,2/5)`, `(1/4,3/4,0)`, and `(1/6,5/6,0)`.

They are normalized and nonnegative. An additional independent rational interior evaluation also
gave three normalized nonnegative triples.

For either `h/m` block the third component vanishes, so the binary entropy enclosure is correct.
For the `h/c` block, if `q0` is the first component, then

`H(q)=h(q0)+(1-q0) h(1/(s+2))`.

Here `s=Q` and `1/(s+2)<=1/2`. Under `Q=b/(1-b)`, the code's
`compact_q_tail_parameter_upper` evaluates the largest conditional binary entropy at the lower
compact `b` endpoint. It separately upper-bounds `h(q0)` and the nonnegative tail mass. Taking
the minimum of the three separate entropy upper bounds remains an upper bound on the minimum
entropy of the three legal original-channel outputs.

**Verdict:** static PASS; there is no endpoint-channel/original-channel quantifier reversal.

### FINDING-SU3-WB-STATIC-03 — PASS: exact rational reconstruction degrees and denominator coverage are sufficient

**Stable source locators:** `certify_su3_triangular_three_face_clusters.py`, functions
`gram_denominator`, `reconstruct_gram_numerator`, `side_denominator`, and
`reconstruct_side_numerators`; `certify_su3_highest_edge_adjacent_faces.py`, exact sparse
polynomial helpers.

All reconstruction arithmetic uses `fractions.Fraction`. For this union:

- the Gram common denominator has exact degrees `(14,12,0,0,0)`;
- each retained binary weight enters the diagonal part quadratically and each cross term at most
  affinely, so `(14,12,2,2,2)` is a sufficient tensor degree;
- each of the 36 Gram interpolants is reconstructed on
  `15*13*3*3*3 = 5,265` exact grid points and checked at two additional rational points;
- the retained-side common denominator has exact degrees `(5,6,0,0,0)`;
- each side distribution is affine in its retained weight, so `(5,6,1,1,1)` is sufficient; and
- the side reconstruction uses `6*7*2*2*2 = 336` exact grid points and another exact rational
  check.

The Gram denominator includes the total input dimension and the linear representation-dimension
factors for every environment block. The side denominator includes every `r+2`, `s+2`, and
`r+s+3` factor needed by the three retained rows. All are strictly positive at finite residual
`P,Q>=0`. The a priori rational degree argument, rather than the extra interpolation samples
alone, rules out a hidden higher-degree remainder.

**Verdict:** static PASS for exact reconstruction and finite-domain denominator positivity.

### FINDING-SU3-WB-STATIC-04 — PASS: compactification and common-denominator Bernstein subdivision cover the full domain

**Stable source locators:** `certify_su3_highest_edge_adjacent_faces.py`, functions `compactify`
and `bernstein_coefficients`; `su3_common_den_controls.py`, functions
`rational_range_common` and `split_common_controls`; shared `certify` backend.

The substitutions `P=a/(1-a)` and `Q=b/(1-b)` multiply numerator and denominator by the same
homogenizing factors of label degrees `(14,12)` for Gram ratios and `(5,6)` for side ratios. They
leave the rational functions unchanged on every finite label. Closing to `a=1` or `b=1` controls
all approaches to infinite labels.

With nonnegative denominator Bernstein controls, each rational value is a convex combination of
matched numerator/denominator control ratios. The range routine compares these ratios by exact
integer cross multiplication, rejects a negative denominator control, rejects an unmatched
numerator at a projective zero, and rejects an identically zero denominator box. Its clipping to
the physical interval `[0,1]` is licensed here because the Gram parameter and side probabilities
are physical quantities already known to lie in that interval. Exact dyadic de Casteljau
subdivision preserves the matched common-denominator representation. A fresh short run of
`test_su3_common_den_controls.py` returned
`common-denominator Bernstein controls exactly match Fraction backend`.

The adaptive stack begins with the whole closed five-cube. Shared dyadic boundaries are retained
by both children and therefore cannot create a gap.

**Verdict:** static PASS; no finite label, projective label face, weight boundary, or interior box
is omitted by the current algorithm.

### FINDING-SU3-WB-STATIC-05 — PASS: logarithm and entropy enclosures have the required directions

**Stable source locators:** `certify_su3_all_elementary_cycles.py`, functions
`reduced_log_bounds`, `log_bounds`, `entropy_bounds`, and `isotropic_probabilities`;
`certify_su3_adjacent_elementary_faces.py`, function `component_entropy_upper`; shared backend
function `correlated_side_entropy_upper` and its leaf-acceptance block.

The logarithm enclosure uses 24 positive terms of the odd `atanh` expansion and an explicit
positive remainder. Power-of-two reduction restores interval endpoints in the correct order for
both positive and negative exponents. Entropy lower bounds use logarithm upper endpoints, and
entropy upper bounds use logarithm lower endpoints.

The isotropic Bell entropy decreases for `0<=t<1`, so its lower enclosure is evaluated at the
maximum of the 36 certified Gram upper bounds. Binary entropy accounts for its maximum at `1/2`.
The `h/c` chain-rule bound uses the correct `Q` monotonicity, including the boundary case with
`Q` constant zero. The exact leaf test is

`bell_lower - 2 * side_upper > 0`

as a `Fraction`. Thus the current source proves the strict Bell-input no-gap inequality required
by the endpoint lemma whenever the adaptive cover terminates normally. The later decimal display
of the smallest margin is only a human-readable approximation and is not used by the proof.

**Verdict:** static PASS for all logarithm, entropy, endpoint, maximum, minimum, and strictness
directions.

### FINDING-SU3-WB-STATIC-06 — PASS: terminal logic is fail-closed, but live completion is pending

**Stable source locator:** `certify_su3_triangular_three_face_clusters.py`, adaptive loop in
`certify`.

Every box failing the exact positive-margin test is split into exactly two children unless all
five coordinates have reached depth seven. An unresolved terminal box raises an assertion. Final
leaf count, smallest-margin display, and the configuration-prefixed Bell-no-go sentence are
printed only after the stack is empty.

If a completed run has `L` accepted leaves, the full binary tree has `L-1` internal boxes and
`2L-1` processed boxes. At a progress line printed just after popping a box, the implementation's
state must satisfy

`pending = processed - 1 - 2*certified`.

These give useful consistency checks for a future captured transcript. But no completed
transcript or exit status was available to this review, and merely remaining alive at high CPU
does not establish that every box will certify.

**Verdict:** current completion criterion static PASS; live execution **PENDING**.

### FINDING-SU3-WB-STATIC-07 — BLOCKER: the live process is not source-bound and must be rerun

**Applies to:** both the route implication and target node claim at the hashes above.

**Stable locator:** process launch metadata and the current-source closure table in this report.

The live Python process predates two files on its current recursive import path by more than two
hours. The actual in-memory core was loaded near startup and may differ materially from the
current exact common-denominator implementation. No immutable prelaunch bundle, source manifest,
or independently reviewable old closure was found in the target dossier.

A normal exit and the current file hashes therefore cannot be combined into a valid certificate
record. Saving the live output later is still useful, but it must be labelled an unbound
historical computation. The repair is a fresh run from a prehashed, preserved closure; appending
current hashes to the old transcript is not a repair.

**Severity:** promotion-blocking provenance defect; no mathematical refutation.

## Mandatory fresh-run dossier

Before a final reviewer may recommend promotion, the fresh run record must contain all of the
following:

1. A complete recursive local source bundle or immutable manifest created **before launch**, with
   SHA-256 hashes for the exact driver and every imported project-local file.
2. Exact command, repository working directory, interpreter path and version, session/PID,
   launch/end timestamps, and recorded exit status.
3. Uninterrupted terminal output containing the configuration identity, the line
   `weakest-bent-fixed-three: endpoint Gram branches reconstructed: 36; degrees=(14, 12, 2, 2, 2)`,
   the line
   `weakest-bent-fixed-three: retained side distributions reconstructed: 3; degrees=(5, 6, 1, 1, 1)`,
   progress checkpoints, final accepted-leaf count, smallest dyadic box, final success sentence,
   and no assertion or traceback.
4. Binary-tree accounting consistent with the accepted-leaf count. Prefer instrumenting the
   fresh source to print the final processed count explicitly.
5. Confirmation that every accepted leaf used exact positive `Fraction` comparison. Prefer also
   printing the exact numerator and denominator of the smallest retained margin; a
   nondirectionally rounded float alone is not an exact lower bound.
6. SHA-256 hashes of the completed transcript and final proposer artifact, with exact node/route
   linkage under the file and DAG protocols.
7. Confirmation that the two route premises remain `PROVED` at the hashes recorded above and that
   the target claim and route implication statements have not drifted.
8. A final independent adversarial review of the preserved source, complete transcript, exact
   statement bindings, and assembled two-premise route. No aggregate orientation claim may be
   inferred automatically.

## Final adjudication

| component | verdict |
|---|---|
| current configuration and exact orientation | **PASS (static)** |
| 36 correlated endpoints and full label/weight coverage | **PASS (static)** |
| retained `h/c`, `h/m`, `h/m` original-side outputs | **PASS (static)** |
| rational reconstruction degrees and denominator coverage | **PASS (static)** |
| compactification, common-denominator Bernstein subdivision, and boundaries | **PASS (static)** |
| directed logarithm/entropy bounds and strict exact acceptance | **PASS (static)** |
| live execution completion | **PENDING** |
| live execution source binding | **FAILED for promotion; post-launch source changes** |
| required repair | **fresh prehashed source-bound exit-zero rerun** |
| route promotion | **DO NOT PROMOTE** |
| atomic node promotion | **DO NOT PROMOTE** |

The blocker is scoped narrowly. It neither refutes the fixed-three route nor weakens the current
static argument; it only prevents the already-running process from serving as a certificate for
the source reviewed here.
