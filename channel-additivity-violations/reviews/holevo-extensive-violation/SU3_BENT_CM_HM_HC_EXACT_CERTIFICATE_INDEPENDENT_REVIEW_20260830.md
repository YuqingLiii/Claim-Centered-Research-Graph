# Independent adversarial review: bent c/m, h/m, h/c SU(3) exact certificate

Date: 2026-08-30

Reviewer: Codex independent review agent `/root/su3_shorter_route`.

## Independence declaration

I did not author the reviewed driver or common certificate backend and did not participate in the
10,783-leaf certificate run. I reviewed the completed atomic dossier in a separate pass. Although I
have worked elsewhere in the same broad SU(3) campaign, this review uses no conclusion from those
other orientations. I did not edit any canonical YAML, reviewed source, proof artifact, or run
record. This report is the only project file created by this review.

## Exact scope and verdict

This review covers only route `fixed-three-original-side-cover` of
`HEXT.su3-bent-cm-hm-hc-three-face-bell-no-go` and the resulting atomic node claim, with the two
listed premises taken at their current independently reviewed `PROVED` levels.

The route implication and atomic claim **PASS** and merit `PROVED` at the exact statement hashes
below. The certificate covers the one labelled bent cluster
`((-1,-1),(0,-3),(0,0))`; it supplies no symmetry transfer to another orientation and no aggregate
three-face or chain conclusion.

Two nonblocking presentation defects remain. The shared backend hard-codes `triangular` in its
last line even though every configuration-bearing line and the driver bind this run to
`bent-cm-hm-hc-fixed-three`. Also, the displayed minimum-margin decimal is produced by ordinary
floating-point formatting. The exact certificate fact is that the internally retained
`Fraction` margin is positive on every accepted leaf; the full displayed decimal should not be
treated as a directed rational lower bound. Neither defect enters the proof test or its control
flow.

## Protocol and exact statement bindings

I read `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full. Their reviewed SHA-256 hashes are:

| protocol | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |

Repository-normalized exact statement hashes are:

| object | exact statement hash | reviewed status/verdict |
|---|---|---|
| `HEXT.su3-three-face-cluster-classification` claim | `sha256:d9e686c2b1a4146bd9bcb20efd0f60a15a513a6d53e92f8ea5559cfd9e9778cf` | premise currently `PROVED` |
| `HEXT.su3-fixed-original-side-endpoint-lemma` claim | `sha256:7435a8e46d009acbe7dabce7c520d1cbbbb45f7943c7b98cdbeef7065ff71398` | premise currently `PROVED` |
| `fixed-three-original-side-cover` implication | `sha256:b5ac9a5546b0875a789ab68e0a476a3c5268586d7d1570c487ae2ab7e897781e` | **PASS; promote to `PROVED`** |
| `HEXT.su3-bent-cm-hm-hc-three-face-bell-no-go` claim | `sha256:e6d06850459364cdb1d58096c0af7ceafe867c3d102f9a9f31453cb73b017c7f` | **PASS; promote to `PROVED` after route linkage** |

Raw node hashes at review time are:

| node file | SHA-256 |
|---|---|
| `HEXT.su3-three-face-cluster-classification.yaml` | `c193d98053bd31f6a8a4eaace0289b669de66b5aa5c2f2e9dce040b32dfa4aa2` |
| `HEXT.su3-fixed-original-side-endpoint-lemma.yaml` | `d327927af5079476df26f926c1cf6e3bfd45251695472736d615f7c28948069c` |
| `HEXT.su3-bent-cm-hm-hc-three-face-bell-no-go.yaml` | `68f5ea551f1d0351eedd71b674283e986cde883aafc08417900c2e9cc780fda6` |

The atomic proof artifact and transcript reviewed here have hashes:

| input | SHA-256 |
|---|---|
| `artifacts/SU3_BENT_CM_HM_HC_THREE_FACE_BELL_NO_GO_20260830.md` | `752f4aac665f9c8b2faf4a416964af962697569b14df562832b1fbb6fd4ebaf0` |
| `artifacts/SU3_BENT_CM_HM_HC_THREE_FACE_CERTIFICATE_20260830.txt` | `5b4b15bbbd2e0ceac65cd8ce177b862a8426f5801ce798109c01ef6f6f9ba475` |

The transcript records the command, terminal output, exit status zero, complete local closure,
and the hard-coded terminal-label note. I independently parsed the recursive imports and obtained
exactly the same seven files. Every recorded digest matches the current source:

| complete local Python import closure | SHA-256 |
|---|---|
| `tools/certify_su3_bent_chain_cm_hm_hc_cover.py` | `fc749995fde3b0c4f38dd1d0019d3d36cc8832933a1502060c2069a99ebe864e` |
| `tools/certify_su3_triangular_three_face_clusters.py` | `37b481a43c6f646a541ed9e0b87f9ac744e9c565ff1f6df1f75da0b3adbb6573` |
| `tools/certify_su3_adjacent_elementary_faces.py` | `68634062aca3293f3f2b483c4e05b441de8d9ba1ae16bf301f5c83c9e4797383` |
| `tools/certify_su3_all_elementary_cycles.py` | `4109cdfc63242e637f843280edc17aa9be126b0d1e824b9b25689048db264fa2` |
| `tools/certify_su3_highest_edge_adjacent_faces.py` | `09a37c01c9afd6d480227c9a7be9e9d3ff5b2461e542adef995df850e62fbc49` |
| `tools/scan_su3_adjacent_elementary_faces.py` | `fbe6a888f447d120f4c5f1cefe8304bec3665c78a8525b3c2bbf4497c955e0cd` |
| `tools/su3_common_den_controls.py` | `39f0e98fac092a101c3d8eeeeac939c7683af1851d09a1a6f8d8c85e97f8584c` |

The executed certificate path uses only these local files and Python standard-library modules.
The imported scan module contains lazy `numpy` imports inside scan-only functions, but none of
those functions is called while importing or running this certificate. Executing the recorded
driver path places its `tools/` directory first for the bare local module names, so the closure
also matches runtime resolution.

## Findings

### FINDING-SU3-CMHMHC-01 — configuration, labels, and 36 correlated endpoints are exact

**Applies to:** route implication
`sha256:b5ac9a5546b0875a789ab68e0a476a3c5268586d7d1570c487ae2ab7e897781e`.

**Stable source locator:** `certify_su3_bent_chain_cm_hm_hc_cover.py`, object `CONFIG`;
`certify_su3_triangular_three_face_clusters.py`, functions `build_union`, `minimum_base`,
`endpoint_patterns`, and `all_weights`.

The driver fixes the exact cluster and retained offsets written in the claim. Independent exact
enumeration reconstructs this input table:

| input offset | ordered branch set | treatment |
|---|---|---|
| `(-1,-2)` | `c,m` | retained binary |
| `(0,-4)` | `c,m` | eliminated |
| `(0,-1)` | `h,c,m` | eliminated |
| `(1,-3)` | `h,c,m` | eliminated |
| `(1,0)` | `h,m` | retained binary |
| `(2,-5)` | `h,c` | eliminated |
| `(2,-2)` | `h,c` | retained binary |

Thus the four eliminated simplex degrees are exactly `2,3,3,2`, whose product is 36. The code
forms the full Cartesian product once and passes each complete pattern into the full Gram formula;
it never maximizes diagonal and cross terms separately. All 36 tuples are distinct, ranging from
`(0,0,0,0)` through `(1,2,2,1)` in the registered ordering.

The minimum base shift is `(1,5)`. After that shift the seven environment offsets are
`(0,4),(1,2),(1,5),(2,0),(2,3),(3,1),(3,4)` and the seven input offsets are
`(0,3),(1,1),(1,4),(2,2),(2,5),(3,0),(3,3)`. Hence every registered representation and every
registered branch is valid for all residual `P,Q>=0`, including the smallest-label boundary.
The two compact variables cover every finite residual integer label, and in fact the code proves
the stronger continuous-label rational inequality.

**Verdict:** PASS; no missing endpoint, invalid boundary branch, or unproved orientation symmetry.

### FINDING-SU3-CMHMHC-02 — side outputs remain outputs of the original channel

**Applies to:** the same route implication and the applicability of the already-`PROVED`
fixed-original-side endpoint lemma.

**Stable source locator:** `certify_su3_triangular_three_face_clusters.py`, functions
`retained_side_distributions`, `reconstruct_side_numerators`, and
`correlated_side_entropy_upper`.

The side reconstruction takes only `(config, union, P, Q, coordinates)`; it has no endpoint-pattern
argument. It is performed once, outside the 36-pattern reconstruction, from the three original
binary weights. The resulting branch types are exactly `c/m`, `h/m`, and `h/c` in the table above.
Direct exact checks at label and weight boundaries and at interior rational points produced three
nonnegative triples, each summing identically to one.

For `h/m`, the output is binary and the code bounds its binary entropy. For `h/c`, the exact chain
rule is

`H(p0,p1,p2) = h(p0) + (p1+p2) h(p1/(p1+p2))`.

The conditional ratio is `1/(s+2)`, independent of the retained mixture weight; its compact upper
bound is evaluated at the correct lower label endpoint. The `c/m` distribution uses componentwise
directed entropy bounds. Each registered side quantity is therefore an upper bound on the entropy
of a legal output of the original channel, not an endpoint replacement. Taking the minimum of the
three separate upper bounds remains an upper bound on the minimum of their exact entropies.

**Verdict:** PASS; the dangerous endpoint-side quantifier reversal does not occur.

### FINDING-SU3-CMHMHC-03 — exact reconstruction and common denominators are sufficient

**Applies to:** the route implication.

**Stable source locator:** `certify_su3_triangular_three_face_clusters.py`, functions
`gram_denominator`, `reconstruct_gram_numerator`, `side_denominator`, and
`reconstruct_side_numerators`.

The Gram denominator is eight times the total input dimension times all distinct linear factors
from the seven environment dimensions. Every factor is strictly positive for finite `P,Q>=0`.
It clears both the diagonal barycentric reciprocals and all shared-environment terms. Its exact
degree is `(12,14,0,0,0)`. Diagonal weights are quadratic and cross-block weights are separately
affine, so `(12,14,2,2,2)` bounds every cleared Gram numerator. The side denominator has exact
degree `(6,5,0,0,0)` and clears every `h/m/c` row used by the retained blocks; side weights are
affine, giving `(6,5,1,1,1)`.

All interpolation and verification arithmetic is `fractions.Fraction`. Each of the 36 Gram
interpolants is checked by the run at two non-grid rational points; the side reconstruction is
checked at another. As an independent finite check, I fully reconstructed endpoint pattern
`(0,2,2,1)`, obtained actual degree `(12,14,2,2,2)`, and verified it at two additional rational
points, one on the label/weight boundary. I also independently reconstructed all three side
groups and verified them at two additional points. Twelve further deterministic rational samples
checked all 36 direct Gram branches in `[0,1]` and all side triples normalized and nonnegative.

**Verdict:** PASS; the chosen tensor degrees do not omit a higher-degree remainder, and the common
denominators have no finite-domain zero.

### FINDING-SU3-CMHMHC-04 — compactification and subdivision miss no finite label or weight boundary

**Applies to:** the route implication.

**Stable source locator:** `certify_su3_highest_edge_adjacent_faces.py`, functions `compactify`
and `bernstein_coefficients`; `su3_common_den_controls.py`, functions
`rational_range_common` and `split_common_controls`; shared backend function `certify`.

For `P=a/(1-a)` and `Q=b/(1-b)`, `compactify` multiplies numerator and denominator by the same
positive powers `(1-a)^12(1-b)^14` for Gram functions and `(1-a)^6(1-b)^5` for side functions.
Hence the ratio is unchanged for all finite labels. The closed projective faces are used to bound
all limiting approaches; the claim itself needs only `a,b<1`. Projective zero denominator controls
are accepted only when the matched numerator control is also zero.

With nonnegative denominator controls, a rational value is a convex combination of matched
numerator/denominator control ratios. `rational_range_common` compares those ratios by exact
integer cross multiplication. `split_common_controls` is exact dyadic de Casteljau subdivision
with a shared power-of-two denominator. I reran `test_su3_common_den_controls.py`; it returned
`common-denominator Bernstein controls exactly match Fraction backend`. I also independently
checked that the initial compact Gram and side denominator control tensors are nonnegative.

The stack begins with the full closed five-cube. A failed box is split in one axis, and no axis may
exceed depth seven. If all axes are exhausted without a positive certificate the code raises an
assertion, so an exit-zero exhausted stack covers every finite label, every three-weight boundary,
and every interior point. Boundary overlap between dyadic children is harmless.

**Verdict:** PASS; no sampled-only inference or omitted compact face.

### FINDING-SU3-CMHMHC-05 — logarithm and entropy directions prove the desired strict inequality

**Applies to:** the route implication.

**Stable source locator:** `certify_su3_all_elementary_cycles.py`, functions
`reduced_log_bounds`, `log_bounds`, `entropy_bounds`, and `isotropic_probabilities`;
`certify_su3_adjacent_elementary_faces.py`, function `component_entropy_upper`; shared backend
functions `binary_interval_entropy_upper`, `correlated_side_entropy_upper`, and `certify`.

After powers-of-two reduction, every logarithm series has nonnegative
`z=(x-1)/(x+1)`. The 24-term odd `atanh` series is a lower bound and the explicit geometric tail
is an upper bound. Restoring a negative power of two reverses the `ln 2` endpoints exactly as the
code implements. I checked 60 deterministic positive rationals against 100-digit decimal
logarithms; all lay inside the rational intervals.

`entropy_bounds` consequently gives directed lower and upper entropy bounds. The isotropic Bell
entropy decreases with `t`, so evaluating its lower enclosure at the exact Bernstein `t_upper` is
conservative. Binary entropy uses its maximum at `1/2`. The componentwise ternary bound uses
monotonicity outside an interval containing `1/e` and the rigorous rational global bound
`1/e<3/8`; it is further capped by an upper enclosure of `ln 3`. The acceptance test is exactly

`bell_lower - 2 * side_upper > 0`

as a `Fraction`. It therefore proves the strict Bell-input no-gap inequality required by the
endpoint lemma.

**Verdict:** PASS; every logarithm, entropy, maximum, and minimum has the correct direction.

### FINDING-SU3-CMHMHC-06 — the 10,783-leaf transcript and source bindings are coherent

**Applies to:** the route implication and atomic node claim.

**Stable source locator:** `SU3_BENT_CM_HM_HC_THREE_FACE_CERTIFICATE_20260830.txt`, complete file;
shared backend function `certify`.

The transcript records the exact driver command, configuration-specific prefixes, 36 reconstructed
Gram branches of degrees `(12,14,2,2,2)`, three side groups of degrees `(6,5,1,1,1)`, 10,783
certified leaves, a positive displayed margin, and exit status zero. Since every nonaccepted box
has exactly two children, an exhausted binary tree with 10,783 accepted leaves contains 10,782
internal boxes and 21,565 total processed boxes. The recorded smallest box is dyadic and within the
per-axis depth-seven policy.

The post-run provenance section contains the complete seven-file local closure, and my independent
AST traversal found neither an omitted local import nor a hash mismatch. The command and wrapper
fix the configuration; the first four terminal lines repeat its unique name. The hard-coded
`triangular` last sentence executes only after stack exhaustion and has no arithmetic role.

The displayed `4.648873074005e-07` is obtained from
`float(smallest_margin):.12e`. It is strong evidence for scale but is not itself printed with
directed rounding. What the exact control flow establishes—and all that the theorem needs—is that
every one of the 10,783 leaf margins passed the exact rational `> 0` test.

**Verdict:** PASS with the two disclosed, nonblocking presentation defects.

## Safe reproduction and review checks performed

I performed these checks without editing canonical materials or repeating the long adaptive run:

- recursively parsed and hash-verified the complete seven-file local import closure;
- reconstructed the exact union, minimum label shift, all incidences, and all 36 endpoint tuples;
- reran the phase-incidence and cross-coefficient positivity audits successfully;
- reran `test_su3_common_den_controls.py` successfully;
- fully reconstructed one Gram endpoint and every retained side polynomial, with extra exact
  rational identity checks outside the built-in interpolation checks;
- checked all 36 direct Gram functions at 12 deterministic rational samples and checked the three
  retained side triples for normalization and nonnegativity; and
- independently audited compactification, dyadic subdivision, logarithm tails, entropy
  monotonicity, and binary-tree accounting.

I did not repeat the 10,783-leaf adaptive run. The promotion recommendation relies on the amended,
hash-bound exit-zero transcript for that finite exhaustive portion, together with the independent
static audit and exact finite reconstructions above.

## Promotion verdict and exact scope

At the exact hashes recorded in this report:

1. the two route premises are already `PROVED` and match their reviewed claims;
2. promote route `fixed-three-original-side-cover` of
   `HEXT.su3-bent-cm-hm-hc-three-face-bell-no-go` to `PROVED`; and
3. after linking this review finding to that route, promote the atomic node claim to `PROVED`.

Do not infer or promote any aggregate chain, all-three-face, general covariant, multiplicity-space,
noncovariant, or non-Bell-input claim from this review.
