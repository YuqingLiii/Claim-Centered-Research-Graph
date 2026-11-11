# Independent review: bent SU(3) `hm/hm/hc` three-face certificate

Date: 2026-08-30

Reviewer: Codex independent review agent `/root/weyl_majorization_audit`.

## Independence declaration

I did not participate in the proposer-side derivation, checker implementation, historical
certificate run, transcript recovery, or provenance amendment. I received the completed dossier
for adversarial review. I did not modify any canonical YAML node, proof artifact, checker, or run
record. This immutable review is the only project file I created for this task.

## Scope and headline verdict

This review covers only `HEXT.su3-bent-hm-hm-hc-three-face-bell-no-go` and its route
`fixed-three-original-side-cover`. I accepted its two premises at their existing `PROVED` levels
and did not re-review them here.

The mathematical configuration, 36-endpoint reduction, retained original-side spectra, exact
polynomial construction, compactification, Bernstein subdivision, and directed entropy bounds
**PASS static adversarial review**. However, the recorded 3,435-box execution is not bound to the
source bytes that actually ran. This is a **promotion-blocking provenance defect requiring
repair**, not a mathematical counterexample.

Accordingly, neither the route implication nor the node claim merits `PROVED` at the current
hashes. Both should remain `CONJECTURED` until either a fresh hash-bound exit-zero run completes or
the exact pre-optimization source snapshot used by the historical run is preserved and bound
credibly to that execution.

This review makes no inference about another bent orientation or any aggregate SU(3) node.

## Exact reviewed statements

The repository-normalized hashes are:

| reviewed object | exact hash | verdict |
|---|---|---|
| route `fixed-three-original-side-cover` implication | `sha256:2f84ea289d4d3a8dae619253822ff1cfb7ed0458b28f843eef8cbceddaf53481` | static implication PASS; remain `CONJECTURED` because the certificate execution is not source-bound |
| `HEXT.su3-bent-hm-hm-hc-three-face-bell-no-go` claim | `sha256:b9b116d1379ad530aa917636fe211c736131665b981dd47d4b241bf950bb66be` | no promotion; remain `CONJECTURED` |

The raw canonical node hash at review time was
`sha256:2ec66d13aa8e2f565a668cc2ea66bf8c8a09d4ed01f20ba09124f6a85d3ad193`.

The two accepted premise claims were already `PROVED` at:

- `HEXT.su3-three-face-cluster-classification`:
  `sha256:d9e686c2b1a4146bd9bcb20efd0f60a15a513a6d53e92f8ea5559cfd9e9778cf`;
- `HEXT.su3-fixed-original-side-endpoint-lemma`:
  `sha256:7435a8e46d009acbe7dabce7c520d1cbbbb45f7943c7b98cdbeef7065ff71398`.

## Inputs inspected

I read `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full. Their hashes were respectively
`sha256:d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` and
`sha256:d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595`.

| project input | SHA-256 at review time |
|---|---|
| `artifacts/SU3_CHAIN_THREE_FACE_SCAN_20260830.md` | `95bd5a495f79cc18e3119177f6dbf9e288242329ac44b58c3e6de8e10e7e6b70` |
| `artifacts/SU3_BENT_HM_HM_HC_THREE_FACE_BELL_NO_GO_20260830.md` | `b1735ad974732c3149d0477563e7576da42b0b714af8ae6e90f2e269dfa74aa5` |
| amended `artifacts/SU3_BENT_HM_HM_HC_THREE_FACE_CERTIFICATE_20260830.txt` | `9181efaf008654a33c976b8fd0b82ed59e029575d2d6949c6fd2723293b62807` |
| `tools/certify_su3_bent_chain_hm_hm_hc_cover.py` | `327043c8d8045dd8370dcbc1410ed491198883b76b43aa0793e5549c2da0d818` |
| `tools/certify_su3_triangular_three_face_clusters.py` | `37b481a43c6f646a541ed9e0b87f9ac744e9c565ff1f6df1f75da0b3adbb6573` |
| `tools/certify_su3_adjacent_elementary_faces.py` | `68634062aca3293f3f2b483c4e05b441de8d9ba1ae16bf301f5c83c9e4797383` |
| `tools/certify_su3_all_elementary_cycles.py` | `4109cdfc63242e637f843280edc17aa9be126b0d1e824b9b25689048db264fa2` |
| `tools/certify_su3_highest_edge_adjacent_faces.py` | `09a37c01c9afd6d480227c9a7be9e9d3ff5b2461e542adef995df850e62fbc49` |
| `tools/scan_su3_adjacent_elementary_faces.py` | `fbe6a888f447d120f4c5f1cefe8304bec3665c78a8525b3c2bbf4497c955e0cd` |
| `tools/su3_common_den_controls.py` | `39f0e98fac092a101c3d8eeeeac939c7683af1851d09a1a6f8d8c85e97f8584c` |

I independently parsed the current local import graph. It contains exactly the seven source files
listed above: the one-line driver, the shared triangular-cluster core, the adjacent-face helper,
the all-cycles formula/log helper, the highest-edge polynomial/Bernstein helper, the scan formula
helper imported by the adjacent-face module, and the common-denominator control backend.

## Findings

### FINDING-HMHC-01 — configuration mapping and all 36 endpoints are correct

**Applies to:** the route implication hash
`sha256:2f84ea289d4d3a8dae619253822ff1cfb7ed0458b28f843eef8cbceddaf53481`.

**Stable locator:** `certify_su3_bent_chain_hm_hm_hc_cover.py`, constant `CONFIG`;
`certify_su3_triangular_three_face_clusters.py`, functions `build_union`, `minimum_base`, and
`endpoint_patterns`.

The driver selects exactly the claimed bent face-base cluster
`((-3,0),(-1,-1),(0,0))`. Its reconstructed input incidence list is:

| input offset | labelled branches | treatment |
|---|---|---|
| `(-3,-1)` | `c,m` | eliminated |
| `(-2,0)` | `h,m` | retained binary |
| `(-1,-2)` | `h,c,m` | eliminated |
| `(0,-1)` | `h,c,m` | eliminated |
| `(1,-3)` | `h,c` | eliminated |
| `(1,0)` | `h,m` | retained binary |
| `(2,-2)` | `h,c` | retained binary |

Thus the four eliminated simplex degrees are `2,3,3,2`, whose product is exactly 36. The
endpoint generator is a Cartesian product over those four blocks and inserts all chosen vertices
into one complete Gram expression, so the branches are correlated endpoint patterns rather than
separately maximized summands. The three retained binary coordinates cover their complete closed
intervals.

The minimum admissible base translation is `(3,3)`. Therefore `P,Q>=0` covers all allowed integer
Dynkin labels and all incidence branches remain valid. Direct exact evaluations at several
rational label/weight points returned 36 parameters in `[0,1]` and normalized nonnegative side
distributions.

**Verdict:** PASS; no missing endpoint or orientation substitution.

### FINDING-HMHC-02 — the retained original-side spectra and entropy factorization are correct

**Applies to:** the route implication hash above.

**Stable locator:** `certify_su3_triangular_three_face_clusters.py`, functions `side_rows`,
`retained_side_distributions`, and `correlated_side_entropy_upper`.

For an input label `(r,s)`, the registered highest-input output rows are

- `h = (1,0,0)`;
- `m = (1/(r+2),(r+1)/(r+2),0)`; and
- `c = (1/(r+s+3),(r+s+2)/((s+2)(r+s+3)),
  (s+1)(r+s+2)/((s+2)(r+s+3)))`.

Each is nonnegative and sums to one. Mixing the appropriate rows with the three retained original
weights therefore gives legal outputs of the original channel, not outputs of the endpoint
replacement channels. The retained branch metadata align in input order as `hm`, `hm`, `hc`, with
shifted input labels `(1,3)`, `(4,3)`, and `(5,1)` above `(P,Q)`.

For either `hm` block the third probability vanishes, so the binary interval entropy bound is
exactly the required upper enclosure. For the `hc` block, writing `q_0` for the first probability
gives

`H(q)=h(q_0)+(1-q_0) h(1/(s+2))`.

Here `s>=1`, so `1/(s+2)<=1/3`; its binary entropy is maximized at the lower compact `Q` endpoint.
The code separately upper-bounds `h(q_0)`, the tail mass, and this conditional entropy, with all
factors nonnegative. Finally, the minimum of three per-output upper bounds is still an upper bound
on the minimum of the three legal output entropies, as required by the already-proved endpoint
lemma.

**Verdict:** PASS; the original-side quantifier and every entropy direction are correct.

### FINDING-HMHC-03 — exact interpolation and compact rational controls are sufficient

**Applies to:** the route implication hash above.

**Stable locator:** `certify_su3_triangular_three_face_clusters.py`, functions
`gram_denominator`, `reconstruct_gram_numerator`, `side_denominator`,
`reconstruct_side_numerators`, and `certify`; `certify_su3_highest_edge_adjacent_faces.py`,
functions `tensor_interpolate`, `compactify`, and `bernstein_coefficients`;
`su3_common_den_controls.py`, functions `rational_range_common` and `split_common_controls`.

The current checker uses `fractions.Fraction` throughout reconstruction. The common Gram
denominator has degrees `(14,12)` in `(P,Q)` and contains the total input-dimension denominator
and all environment-dimension factors needed by the diagonal and shared-environment formulas.
Each retained binary weight enters at degree at most two, so
`(14,12,2,2,2)` is a sufficient tensor degree. The interpolation grid has 5,265 points per
endpoint. Every one of the 36 reconstructed functions is checked at two additional rational
points.

The side denominator has label degrees `(6,5)`; every side probability is affine in its own
binary weight. Hence `(6,5,1,1,1)` and its 336-point grid are sufficient, and the reconstructed
side triples receive an additional exact rational check. These a priori degree bounds, rather
than the spot checks alone, rule out an unrepresented higher-degree remainder.

The compactification substitutes `P=a/(1-a)` and `Q=b/(1-b)` after multiplying numerator and
denominator by the same projective degrees. In a common tensor Bernstein basis with nonnegative
denominator controls, a rational function is a weighted average of matched numerator/denominator
control ratios. The range routine compares ratios by exact integer cross multiplication and
rejects negative denominator controls, unmatched projective zeros, and identically zero
denominators. Exact de Casteljau splitting preserves every represented polynomial. The independent
backend test reproduced exact equality with the per-control `Fraction` split and range routines.

**Verdict:** PASS for the current checker source.

### FINDING-HMHC-04 — directed logarithm and adaptive-cover logic are rigorous

**Applies to:** the route implication hash above.

**Stable locator:** `certify_su3_all_elementary_cycles.py`, functions `reduced_log_bounds`,
`log_bounds`, `entropy_bounds`, and `isotropic_probabilities`;
`certify_su3_triangular_three_face_clusters.py`, the adaptive loop in `certify`.

The logarithm interval uses 24 terms of the positive `atanh` expansion with an explicit positive
remainder. Rescaling by powers of two uses the correct lower/upper orientation for both signs of
the exponent. Entropy lower bounds use logarithm upper endpoints; entropy upper bounds use
logarithm lower endpoints.

The qutrit isotropic entropy is decreasing for `0<=t<1`, so evaluating its lower enclosure at the
maximum of the 36 certified `t` upper bounds is correct. The side term is an upper enclosure, and
acceptance occurs only when the exact `Fraction` value `bell_lower - 2*side_upper` is strictly
positive. Floating point is used only to render an already positive rational margin.

The adaptive stack begins with the complete closed five-cube. Every failed box is bisected exactly
unless all axes have reached depth seven, in which case the checker raises an assertion. Thus a
genuine exit-zero run would prove that every leaf was certified. The reported 3,435 leaves would
correspond to a full binary tree with 3,434 internal boxes and 6,869 processed boxes. The reported
smallest box has dyadic endpoints and lies comfortably inside the allowed depth budget. A direct
midpoint evaluation of that box gave a positive actual margin; this is only a smoke test, not a
replacement for the Bernstein certificate.

**Verdict:** PASS for the current checker source.

### FINDING-HMHC-05 — the historical transcript is not bound to the code that ran

**Applies to:** both the route implication and the node claim at their exact hashes above.

**Stable locator:** `SU3_BENT_HM_HM_HC_THREE_FACE_BELL_NO_GO_20260830.md`, “Reproduction”;
amended `SU3_BENT_HM_HM_HC_THREE_FACE_CERTIFICATE_20260830.txt`, blocks “Exit status” and
“Complete local Python import closure”.

The theorem artifact explicitly states that the completed historical process used “the original
per-control `Fraction` backend already loaded before the common-denominator optimization was
introduced.” The amended transcript instead lists hashes of the **current** common-denominator
core and includes `su3_common_den_controls.py` in a seven-file closure. The current core imports
and executes that module. Consequently, the appended seven-file list cannot be the local import
closure that the artifact says was loaded by the historical process.

The amendment states only that the current source mtimes predate “this transcript.” It does not
state or demonstrate that those mtimes predate process launch; indeed the artifact's loaded-before-
optimization explanation indicates that the on-disk optimized sources may have changed while the
old process was running. No launch time, historical PID/session, hash of the loaded pre-optimization
core, or preserved old source snapshot is supplied. The exit status was also appended
retrospectively, based on the project event rather than a contemporaneous shell-status record.

The five original output lines and same-day project event are consistent with a completed run, and
the hard-coded word “triangular” in the final line is only a disclosed presentation defect because
all progress prefixes identify `bent-hm-hm-hc-fixed-three`. But neither those facts nor the exact
backend-equivalence unit test identifies the source bytes used by the historical execution. The
unit test proves an arithmetic interface property of the current source; it cannot reconstruct an
unpreserved historical module or show that backend replacement was its only change.

**Severity:** promotion-blocking, repair required. It does not refute the mathematical claim.

**Required repair:** either:

1. run the current seven-file checker to completion and save a fresh record containing source
   hashes captured before launch, launch/exit metadata, complete output, and exit status; or
2. preserve the exact pre-optimization source closure with its hashes and provide a credible
   binding of that snapshot to the historical execution.

Until then, the current transcript is not sufficient evidence for `PROVED` under the repository's
source-locatable completion standard.

## Independent checks and limitations

I performed the following safe checks:

- independently reconstructed the seven input and seven environment blocks;
- verified the retained `hm/hm/hc` branch order and `2*3*3*2=36` endpoint count;
- computed the denominator degrees and interpolation-grid sizes directly;
- evaluated all 36 endpoint functions and all three original-side spectra at several exact
  rational points, including the smallest-label boundary;
- checked endpoint domination on an independently assembled all-continuous rational mixture;
- verified the `hc` conditional entropy factorization and monotonicity;
- reran `test_su3_common_den_controls.py` successfully; and
- parsed and hashed the current seven-file local import closure.

I also launched a fresh run of the current checker at 2026-08-30 21:22:29 EDT (PID 49514). After
more than ten minutes it remained in the first exact Gram-reconstruction stage and had emitted no
certificate output. I interrupted it cleanly. That interruption is neither a failed mathematical
run nor positive certificate evidence; it simply did not repair the provenance gap.

The existing 3,435-box computation was not repeated to completion. This review therefore passes
the current checker's mathematics but cannot independently authenticate the historical terminal
statistics against executed source bytes.

## Promotion instructions

At route implication hash
`sha256:2f84ea289d4d3a8dae619253822ff1cfb7ed0458b28f843eef8cbceddaf53481`
and node claim hash
`sha256:b9b116d1379ad530aa917636fe211c736131665b981dd47d4b241bf950bb66be`:

- do **not** promote the route;
- do **not** promote the node;
- keep both `CONJECTURED`; and
- register the source-bound fresh-run repair above as the remaining gate.

No aggregate conclusion is licensed by this review.
