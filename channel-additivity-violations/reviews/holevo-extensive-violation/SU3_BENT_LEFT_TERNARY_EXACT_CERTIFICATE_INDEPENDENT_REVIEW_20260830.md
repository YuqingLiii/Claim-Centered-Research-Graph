# Independent adversarial review: bent-left ternary SU(3) exact certificate and route premises

Date: 2026-08-30

Reviewer: Codex independent review agent `/root/weyl_majorization_audit`.

## Independence declaration

I did not participate in the proposer-side derivation, implementation, long certificate run, or
the subsequent provenance repair. I received the completed materials only for adversarial review.
I reconstructed the combinatorial enumeration, endpoint argument, configuration mapping, and
certificate logic independently from the submitted artifacts and source. I did not edit any
canonical YAML node, proof artifact, checker, or run record. This file is the only project file I
created.

## Scope and verdict

This review covers exactly:

1. `HEXT.su3-three-face-cluster-classification`;
2. `HEXT.su3-fixed-original-side-endpoint-lemma`;
3. route `fixed-three-original-side-cover` of
   `HEXT.su3-bent-left-ternary-three-face-bell-no-go`; and
4. the resulting atomic bent-left node claim.

All four reviewed statements **PASS**. The two premise nodes, the route implication, and the
atomic bent-left node merit `PROVED` at the exact hashes recorded below. This recommendation does
not cover any other straight, bent, or triangular orientation, and it does not close any aggregate
parent conjunction.

The disclosed final-line text `input-centered triangular SU(3) face cluster is Bell-no-go` is a
presentation defect: it is hard-coded in the shared core. It is not a mathematical or provenance
defect because the command-line dispatch, immutable configuration, progress prefix, endpoint
count, and complete source closure all bind the run to `bent-left-ternary-fixed-three`.

## Protocol and immutable inputs

I read `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full before reviewing the mathematical
materials. Their reviewed file hashes were respectively:

- `DAG_PROTOCOL.md`:
  `sha256:d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095`;
- `FILE_PROTOCOL.md`:
  `sha256:d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595`.

The repository-normalized exact statement hashes are:

| reviewed object | exact statement hash | recommendation |
|---|---|---|
| `HEXT.su3-three-face-cluster-classification` claim | `sha256:d9e686c2b1a4146bd9bcb20efd0f60a15a513a6d53e92f8ea5559cfd9e9778cf` | `PROVED` |
| `HEXT.su3-fixed-original-side-endpoint-lemma` claim | `sha256:7435a8e46d009acbe7dabce7c520d1cbbbb45f7943c7b98cdbeef7065ff71398` | `PROVED` |
| `fixed-three-original-side-cover` implication | `sha256:4381806219e3e9a9b89a8dd8df03cb734633368f2401e7e90247124a9ef0e4ec` | `PROVED` |
| `HEXT.su3-bent-left-ternary-three-face-bell-no-go` claim | `sha256:5ea45de9d9071b8e221d6cf1199d62747c263e3ed046b548741bf3cf85ec3d7f` | `PROVED` |

The raw node-file hashes at review time were:

| node file | SHA-256 |
|---|---|
| `HEXT.su3-three-face-cluster-classification.yaml` | `fdc86389f60f75e97d132c094518de10f83f2b6b4b78d8e8ed10656d9ef015fe` |
| `HEXT.su3-fixed-original-side-endpoint-lemma.yaml` | `f2bec2ef75ca78fd9618e182e69bf6923c330bde86c74ad2321bcde1c95fad6c` |
| `HEXT.su3-bent-left-ternary-three-face-bell-no-go.yaml` | `13a60d26bfb7803cff7c88a056d4fd4b5489d9b6ce734cce43b882b5f6f0427a` |

I inspected the following premise materials:

| input | SHA-256 |
|---|---|
| `artifacts/SU3_THREE_FACE_CLUSTER_CLASSIFICATION_20260830.md` | `177ab70fa562b403419f534a5271c812382d03317e48d0e63c034a6c8baccc45` |
| `artifacts/SU3_THREE_FACE_CLUSTER_CLASSIFICATION_RUN_20260830.txt` | `cf31d9c6d9c6dcf275f1f6dabca9af068d010c514c980546c793e2f248ee5451` |
| `tools/classify_su3_three_face_clusters.py` | `d1066284966c8b13a0cd7f10a4a33a299b883b554166555e59158d7ba421a2ab` |
| `artifacts/SU3_FIXED_ORIGINAL_SIDE_ENDPOINT_LEMMA_20260830.md` | `8f2f791e929688047bddb7af5f7d95c69a687eeae38ed52fd9df9cf6262d238f` |
| `tools/audit_su3_three_face_phase_independence.py` | `3820ff42bb67b88847337ba8b69e5dfa10b1ba9e14ce0b6c4e4b74dc5bdef96d` |
| `artifacts/SU3_THREE_FACE_PHASE_INDEPENDENCE_RUN_20260830.txt` | `16e8282cdaf17cc9ef24c5180b37b520204043da66ef83312ffd13ff7c492e8c` |
| `tools/audit_su3_cross_coefficient_positivity.py` | `d114c53bc62c61197c03b400f5230e1542c5be039b53e37fcf0f47b85ac08846` |
| `artifacts/SU3_CROSS_COEFFICIENT_POSITIVITY_RUN_20260830.txt` | `851b9646c2bd94c04665f7967f46cb07dab8b71bf256bd284dcb2e4bbab22c8f` |

I inspected the bent-left certificate and run record at these hashes:

| input | SHA-256 |
|---|---|
| `artifacts/SU3_BENT_LEFT_TERNARY_EXACT_CERTIFICATE_20260830.md` | `2bb863483e6c8a6652fa53cbe7a0c3a34633fc426ccd7ded6f15550bd91fde18` |
| `artifacts/SU3_BENT_LEFT_TERNARY_EXACT_RUN_20260830.txt` | `f4b81bcdac67833b9411d47c6adfc93e6f6d1ba63f5072bbda80adca652fca52` |

The run record lists the complete eight-file local Python import closure. I independently parsed
the imports and obtained exactly the same closure. Every recorded hash matches the current file:

| local source | SHA-256 |
|---|---|
| `tools/certify_su3_adjacent_elementary_faces.py` | `68634062aca3293f3f2b483c4e05b441de8d9ba1ae16bf301f5c83c9e4797383` |
| `tools/certify_su3_all_elementary_cycles.py` | `4109cdfc63242e637f843280edc17aa9be126b0d1e824b9b25689048db264fa2` |
| `tools/certify_su3_chain_three_face_sixdim_covers.py` | `25751612b38aea64f527ebb56d09c38245074f0edc5806067ad2ed52323be9ac` |
| `tools/certify_su3_highest_edge_adjacent_faces.py` | `09a37c01c9afd6d480227c9a7be9e9d3ff5b2461e542adef995df850e62fbc49` |
| `tools/certify_su3_input_centered_triangle_sixdim.py` | `3c34647bebec2dc3a17c54eeeecce4da45b23e8544cba76d19794e7688bf00a0` |
| `tools/certify_su3_triangular_three_face_clusters.py` | `37b481a43c6f646a541ed9e0b87f9ac744e9c565ff1f6df1f75da0b3adbb6573` |
| `tools/scan_su3_adjacent_elementary_faces.py` | `fbe6a888f447d120f4c5f1cefe8304bec3665c78a8525b3c2bbf4497c955e0cd` |
| `tools/su3_common_den_controls.py` | `39f0e98fac092a101c3d8eeeeac939c7683af1851d09a1a6f8d8c85e97f8584c` |

## Findings

### FINDING-SU3-C3-01 — the 11-class enumeration is exhaustive

**Applies to:** `HEXT.su3-three-face-cluster-classification`, claim hash
`sha256:d9e686c2b1a4146bd9bcb20efd0f60a15a513a6d53e92f8ea5559cfd9e9778cf`.

**Stable source locator:** `SU3_THREE_FACE_CLUSTER_CLASSIFICATION_20260830.md`, paragraph beginning
“Enumerate every connected three-element subset”; `classify_su3_three_face_clusters.py`, functions
`translate_normal_form`, `shape`, and `all_clusters`.

The neighbor differences are exactly
`±(1,1), ±(1,-2), ±(2,-1)`. A connected graph on three vertices has diameter at most two, so after
translating any one member to the origin all members lie in the two-step ball. Conversely every
enumerated three-set is tested for connectivity. Taking the lexicographic minimum over the three
translations which put a member at the origin is exactly a translation quotient; it invokes no
rotation, Weyl action, or conjugation.

I wrote a separate in-memory enumeration over a substantially larger ambient lattice, with an
independent canonicalizer and shape test. It again returned exactly 11 classes, partitioned as
three straight chains, six non-triangular bent chains, and two triangles. Thus neither the
two-step restriction nor the normal form loses or identifies an orientation.

**Verdict:** PASS; no defect.

### FINDING-SU3-C3-02 — the labelled incidence signatures and phase premise match

**Applies to:** the same classification claim and to the applicability premise of the endpoint
lemma.

**Stable source locator:** `SU3_THREE_FACE_CLUSTER_CLASSIFICATION_20260830.md`, paragraph beginning
“Every chain union”; `classify_su3_three_face_clusters.py`, function `union_signature`;
`SU3_THREE_FACE_PHASE_INDEPENDENCE_RUN_20260830.txt`, terminal summary.

I independently reconstructed the six labelled `h/m/c` edges of every face before deduplication.
All nine chains have `I/E/edges = 7/7/16` and degree multisets
`[2,2,2,2,2,3,3]` on both sides. The two triangles have respectively `7/6/15` and `6/7/15`, with
the stated swapped degree multisets. For each of the 11 unions, every distinct input pair shares
at most one environment. Fresh reruns of both proposer checkers reproduced their archived output.

**Verdict:** PASS; the classification node merits `PROVED`.

### FINDING-SU3-ENDPOINT-01 — phases and nonnegativity are controlled

**Applies to:** `HEXT.su3-fixed-original-side-endpoint-lemma`, claim hash
`sha256:7435a8e46d009acbe7dabce7c520d1cbbbb45f7943c7b98cdbeef7065ff71398`.

**Stable source locator:** `SU3_FIXED_ORIGINAL_SIDE_ENDPOINT_LEMMA_20260830.md`, proof paragraphs
beginning “Because two distinct inputs” and “Each diagonal block”;
`audit_su3_cross_coefficient_positivity.py`, function `positive_numerator`.

When a distinct input pair shares at most one environment, its off-diagonal Gram entry contains
one edge-amplitude product, so taking its squared modulus removes the arbitrary relative phase.
There is no second shared-environment amplitude with which it could interfere. Each diagonal term
is the nonnegative chi-square expression

`(sum_b lambda_b^2 / c_b - 1)/8`,

where both `lambda` and the barycentric `c` sum to one. Shared-environment terms are squared
Hilbert--Schmidt overlaps. The denominator-cleared audit is algebraically consistent with the
registered branch formula: if `E` is the environment dimension and `d_o` is the omitted branch,

`8 E C_ab = 24 E^2 - 17 E d_o + 3 d_o^2 - 3 d_a^2 + E d_a - 3 d_b^2 + E d_b`.

Expansion in the valid highest-weight coordinates has only positive monomial coefficients for
all three branch pairs; the fresh exact run reproduced 17, 17, and 13 positive monomials with
smallest coefficient `3/2`. Boundary cases where a branch dimension vanishes follow by the same
polynomial identity.

**Verdict:** PASS; no hidden phase or sign assumption remains.

### FINDING-SU3-ENDPOINT-02 — separate convexity gives the correlated endpoint maximum

**Applies to:** the endpoint lemma claim above.

**Stable source locator:** `SU3_FIXED_ORIGINAL_SIDE_ENDPOINT_LEMMA_20260830.md`, proof paragraph
beginning “For one eliminated block”.

With all other block weights fixed, the dependence on one eliminated simplex vector is a positive
diagonal quadratic form from its chi-square term plus affine shared-environment terms. It is
therefore convex on that simplex. A convex function on a finite simplex is bounded by its maximum
over vertices. Repeating this argument one block at a time proves

`t(lambda) <= max_e t_e`.

Joint convexity is neither asserted nor needed. Bilinear cross-block terms are affine in the one
block currently being eliminated, and each iteration evaluates the full Gram expression. Hence
the final comparison uses one correlated endpoint pattern, not separately maximized summands.
An independent exact rational smoke test with all seven blocks continuously weighted also obeyed
the resulting 24-endpoint domination.

**Verdict:** PASS; no endpoint-correlation gap.

### FINDING-SU3-ENDPOINT-03 — Bell monotonicity and the side-output quantifiers are correct

**Applies to:** the endpoint lemma claim above.

**Stable source locator:** `SU3_FIXED_ORIGINAL_SIDE_ENDPOINT_LEMMA_20260830.md`, proof paragraphs
beginning “The endpoint certificate supplies” and “For each retained block”, plus
“Quantifier warning”.

For the qutrit isotropic spectrum,

`B'(t)=-(8/9) log((1+8t)/(1-t)) <= 0` on `0<=t<1`.

Thus `t(lambda)<=T<1` implies `B(t(lambda))>=B(T)`. For every retained block, the registered
block-highest input is a legal input of the original channel with its original retained weights,
so `S_min(Phi)<=H(q_r(lambda_r))`. Therefore
`S_min(Phi)<=min_r H(q_r)`. The proof never substitutes endpoint-channel side outputs, and the
order of the maximum over Gram endpoints and minimum over legal original outputs is not reversed.
The strict certified inequality consequently implies the strict Bell-input no-gap inequality for
all eliminated weights and phases.

**Verdict:** PASS; the endpoint lemma merits `PROVED`.

### FINDING-SU3-BENT-01 — configuration and label coverage are exact

**Applies to:** route `fixed-three-original-side-cover`, implication hash
`sha256:4381806219e3e9a9b89a8dd8df03cb734633368f2401e7e90247124a9ef0e4ec`, and the atomic bent-left
claim hash `sha256:5ea45de9d9071b8e221d6cf1199d62747c263e3ed046b548741bf3cf85ec3d7f`.

**Stable source locator:** `certify_su3_chain_three_face_sixdim_covers.py`, configuration
`CONFIGURATIONS["bent-left-ternary"]`; `certify_su3_triangular_three_face_clusters.py`, functions
`build_union`, `minimum_base`, `endpoint_patterns`, and `retained_weights`.

The command argument `bent-left-ternary` dispatches to the exact cluster
`((-3,3),(-2,1),(0,0))`. The independently reconstructed input blocks are:

| input offset | branches | treatment |
|---|---|---|
| `(-3,2)` | `c,m` | eliminated |
| `(-2,0)` | `c,m` | eliminated |
| `(-2,3)` | `h,m` | retained binary |
| `(-1,1)` | `h,c,m` | retained ternary |
| `(0,-1)` | `h,c,m` | eliminated |
| `(1,0)` | `h,m` | retained binary |
| `(2,-2)` | `h,c` | eliminated |

The eliminated degrees are `2,2,3,2`, yielding exactly 24 correlated endpoint patterns. The
retained stick-breaking coordinates cover both binary simplices and the full ternary simplex,
including their boundaries. The minimum label translation is `(3,2)`, so `P,Q>=0` covers every
allowed translation and keeps every registered branch valid. Compactification
`a=P/(1+P)`, `b=Q/(1+Q)` covers all finite labels with `[0,1)^2`; certifying its closed cube also
controls all limits at infinity.

**Verdict:** PASS; the nickname does not conceal an orientation or boundary substitution.

### FINDING-SU3-BENT-02 — exact reconstruction degrees and checks are sufficient

**Applies to:** the route implication and atomic claim above.

**Stable source locator:** `certify_su3_input_centered_triangle_sixdim.py`, functions
`gram_denominator`, `reconstruct_gram_numerator`, `side_denominator`, and
`reconstruct_side_numerators`.

All reconstruction arithmetic uses `fractions.Fraction`. The Gram common denominator has label
degrees `(12,12)` and includes the total input dimension and every linear factor from all relevant
environment dimensions. A retained weight occurs quadratically at most, so tensor degrees
`(12,12,2,2,2,2)` are sufficient. The side denominator has label degrees `(5,5)` and the side
distributions are affine in each stick coordinate, so `(5,5,1,1,1,1)` is sufficient. The exact
interpolation grids contain respectively 13,689 and 576 points. Every one of the 24 Gram
interpolants is checked at two independent rational points; the side reconstruction is checked at
another rational point. The degree argument, rather than the spot checks alone, proves that no
higher-degree remainder is omitted.

Direct exact evaluations at several independent rational points, including label and weight
boundaries, produced 24 physical Gram parameters and normalized nonnegative retained-side
distributions.

**Verdict:** PASS; no interpolation or denominator gap.

### FINDING-SU3-BENT-03 — Bernstein compactification and subdivision cover the full domain

**Applies to:** the route implication and atomic claim above.

**Stable source locator:** `certify_su3_input_centered_triangle_sixdim.py`, functions `compactify`
and `main`; `su3_common_den_controls.py`, functions `rational_range_common` and
`split_common_controls`.

The compactification multiplies numerator and denominator by common projective degrees and
expands `P=a/(1-a)`, `Q=b/(1-b)` exactly. In a common tensor Bernstein basis with nonnegative
denominator controls, the rational value is a convex combination of matched coefficient ratios.
The code compares those ratios by integer cross multiplication, rejects negative denominator
controls, and rejects an unmatched numerator at a zero denominator control. Exact de Casteljau
halving preserves the represented polynomials. A fresh run of
`test_su3_common_den_controls.py` returned
`common-denominator Bernstein controls exactly match Fraction backend`.

The adaptive stack begins with the entire closed six-cube. A box is discarded only after an exact
positive entropy margin; otherwise it is bisected, and exhausting depth six on an uncertified box
raises an assertion. Therefore an exit-zero terminal run certifies a disjoint recursive cover of
the complete domain, including all finite labels and all simplex boundaries.

**Verdict:** PASS; no uncovered box or projective boundary is inferred from sampling.

### FINDING-SU3-BENT-04 — entropy enclosures are directed rigorously

**Applies to:** the route implication and atomic claim above.

**Stable source locator:** `certify_su3_all_elementary_cycles.py`, functions
`reduced_log_bounds`, `log_bounds`, `entropy_bounds`, and `isotropic_probabilities`;
`certify_su3_input_centered_triangle_sixdim.py`, function `retained_side_entropy_upper` and the
acceptance block in `main`.

The logarithm enclosure uses a 24-term `atanh` series with an explicit positive tail. Powers of
two are restored with the correct endpoint direction for both positive and negative exponents.
The Bell lower bound is evaluated at the certified `t_upper`, which is valid because `B` is
decreasing. Binary retained outputs use the exact location of the binary-entropy maximum. For a
ternary output, each `-p log p` component is bounded using its monotonic regions and the rigorous
global bound `1/e<3/8`, with a further cap by an upper enclosure of `log 3`. Taking the minimum of
the separate retained-side upper bounds is still an upper bound on the minimum retained-side
entropy. Box acceptance is the exact comparison `Fraction margin > 0`; floating point is used
only to render the already positive margin.

**Verdict:** PASS; all inequality directions match the desired lower-minus-upper certificate.

### FINDING-SU3-BENT-05 — terminal statistics and source bindings are coherent

**Applies to:** the route implication and atomic claim above.

**Stable source locator:** `SU3_BENT_LEFT_TERNARY_EXACT_RUN_20260830.txt`, sections “Recorded
progress checkpoints”, “Final terminal output”, and “Complete local Python import closure”.

The run exited zero after certifying 21,058 leaves. A full binary subdivision tree with that many
leaves has 21,057 internal boxes and 42,115 processed boxes. The recorded checkpoint values obey
the stack identity printed immediately after each pop,
`pending = processed - 1 - 2*certified`: they give respectively 5, 7, and 3. Thus the checkpoints,
leaf count, and normal termination are internally consistent. The smallest displayed lower margin
is strictly positive, `> 6.340626717749e-08`, and its six intervals are exact dyadic boxes allowed
by the depth-six policy.

The run record now binds every local imported source, states that all recorded mtimes predate
launch, and records the executed command and configuration-specific progress prefix. I independently
reconstructed the eight-file import closure and verified every hash. The hard-coded final sentence
is inconsistent with the configuration name but is executed only after the stack empties; it has
no control-flow or arithmetic role.

**Verdict:** PASS with one nonblocking presentation defect already disclosed in the source
artifact.

## Reproduction and independent checks

I performed these safe checks without modifying canonical materials:

- reran `classify_su3_three_face_clusters.py` and reproduced all 11 classes and signatures;
- independently enumerated the translation classes in a larger ambient lattice and reproduced
  `3/6/2`;
- reran the phase-incidence and cross-coefficient exact audits;
- independently reconstructed every union signature and the maximum shared-environment count;
- parsed the local Python import graph and reproduced the recorded eight-file closure;
- reran `test_su3_common_den_controls.py` successfully;
- directly evaluated all 24 endpoint Gram functions and all retained-side distributions at
  several exact rational points;
- tested the separate-convex endpoint domination on an independently assembled seven-block
  rational mixture; and
- checked the terminal binary-tree accounting and dyadic bounds.

I did not repeat the approximately 8 hour 20 minute full adaptive run. I began an independent
launch but stopped it during the first expensive reconstruction stage before it emitted a
certificate checkpoint; that interruption is not a failed certificate. The completed review
therefore relies on the immutable exit-zero run record at the recorded source hashes, reinforced
by full static proof-path inspection and the finite exact reruns above.

## Final promotion instructions

At the exact statement hashes in this report:

1. promote `HEXT.su3-three-face-cluster-classification` to `PROVED`;
2. promote `HEXT.su3-fixed-original-side-endpoint-lemma` to `PROVED`;
3. promote route `fixed-three-original-side-cover` of
   `HEXT.su3-bent-left-ternary-three-face-bell-no-go` to `PROVED`; and
4. after those premise and route promotions are linked, promote the atomic bent-left node to
   `PROVED`.

Do not use this review to promote another orientation or an aggregate SU(3) parent node. No
remaining mathematical defect was found within the reviewed scope.
