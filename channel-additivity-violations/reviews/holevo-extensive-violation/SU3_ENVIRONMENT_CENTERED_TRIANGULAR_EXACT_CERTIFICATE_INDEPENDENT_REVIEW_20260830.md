# Independent adversarial review: environment-centered triangular SU(3) certificate

Date: 2026-08-30

Reviewer: independent Codex review context `/root/q2_probability_review`.

## Independence declaration

I did not author the environment-centered certificate, its checker, its prose artifact, or its
canonical node. I received those materials only for read-only adversarial review. I did not modify
any proposer source, proposer artifact, canonical node, route, assessment, event, or generated
view. This immutable report is the only project file created by the audit.

## 1. Scope and overall verdict

This review covers only:

- route `fixed-binary-ternary-original-side-cover` of
  `HEXT.su3-environment-centered-triangular-three-face-bell-no-go`; and
- the resulting atomic environment-centered triangular claim.

The mathematical design of the **current** checker passes static review, and the two listed
premises are independently `PROVED` at their unchanged exact interfaces. The archived execution,
however, **FAILS the source-provenance gate**. Its five-line transcript contains no command,
working directory, interpreter, start/end time, process or session identifier, exit status,
prelaunch source manifest, post-run source hashes, or import-closure record. More decisively, the
current driver and common-denominator backend were modified more than three hours after the
transcript was created. Current source therefore cannot be substituted for the unknown source
bytes used by the historical execution.

Accordingly the route implication and atomic claim are **BLOCKED from promotion**. Both must
remain `CONJECTURED` until a fresh source-bound run (or an equivalently strong recovery of the exact
historical source and execution metadata) completes and receives an execution amendment review.

This review does not authorize the aggregate triangular parent, any sibling orientation, a
non-Bell input result, or the Question 3 root.

## 2. Protocol and exact statement bindings

`DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` were read in full. Their hashes were:

- `DAG_PROTOCOL.md`: `sha256:d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095`;
- `FILE_PROTOCOL.md`: `sha256:d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595`.

Repository-normalized exact statement hashes are:

| object | exact hash | verdict |
|---|---|---|
| `fixed-binary-ternary-original-side-cover` implication | `sha256:782c8fe291601d1afe46d47c133b6a5c32f17d3d69c6da678d38df60c4e095f4` | static design PASS; execution/provenance BLOCK |
| atomic environment-centered triangular claim | `sha256:dcbaba81a7479ab6a98860ef46bde5486fc6aef6c1249c4b1f53347ca75c4582` | do not promote |

The already completed premise interfaces are:

| premise | exact claim hash | status at review |
|---|---|---|
| `HEXT.su3-three-face-cluster-classification` | `sha256:d9e686c2b1a4146bd9bcb20efd0f60a15a513a6d53e92f8ea5559cfd9e9778cf` | `PROVED` |
| `HEXT.su3-fixed-original-side-endpoint-lemma` | `sha256:7435a8e46d009acbe7dabce7c520d1cbbbb45f7943c7b98cdbeef7065ff71398` | `PROVED` |

The target materials reviewed had these hashes:

| file | SHA-256 |
|---|---|
| `proof-dag/nodes/HEXT.su3-environment-centered-triangular-three-face-bell-no-go.yaml` | `72d5d100678c29e9c9b9e63ca62fe664c011e46c5428a3aca4631890ce589c7e` |
| `artifacts/SU3_ENVIRONMENT_CENTERED_TRIANGLE_BELL_NO_GO_20260830.md` | `b9c4a00edb1a3f27fb024feb81f513b8dd8ce949a57a7565c4d43811ac556de0` |
| `artifacts/SU3_ENVIRONMENT_CENTERED_TRIANGLE_CERTIFICATE_20260830.txt` | `bc9a2b31d1ad8c495f0c04ca884ffc355de7ce076e8e871347ee0b22b1a00d1b` |

## 3. Finding ECT-IR-01 — current configuration and 36-endpoint reduction statically PASS

**Applies to:** route implication
`sha256:782c8fe291601d1afe46d47c133b6a5c32f17d3d69c6da678d38df60c4e095f4`.

**Stable current-source locators:** `certify_su3_triangular_three_face_clusters.py`, object
`CONFIGURATIONS` and functions `build_union`, `endpoint_patterns`, `retained_weights`, and
`all_weights`.

The current checker contains exactly one configuration:

- name `environment-centered`;
- cluster `((-2,1),(-1,2),(0,0))`;
- retained binary block `(0,2)`;
- retained ternary block `(1,0)`; and
- expected endpoint count 36.

I independently rebuilt its labelled union. It has seven environment vertices, six input
vertices, and 15 distinct incidence edges. The six input blocks are:

| input offset | ordered branch set | treatment |
|---|---|---|
| `(-2,0)` | `c,m` | eliminated |
| `(-1,1)` | `h,c,m` | eliminated |
| `(0,-1)` | `h,c,m` | eliminated |
| `(0,2)` | `h,m` | retained binary |
| `(1,0)` | `h,c,m` | retained ternary |
| `(2,-2)` | `h,c` | eliminated |

The four eliminated block sizes are `2,3,3,2`, so their full correlated Cartesian endpoint set
has exactly `2*3*3*2=36` members, from `(0,0,0,0)` through `(1,2,2,1)`. No factor is omitted or
duplicated. The retained binary parameter spans its whole segment. The ternary stick map

`(x,y) -> (x,(1-x)y,(1-x)(1-y))`

surjects onto the full probability simplex, including its boundary. These three retained weight
coordinates plus two compactified label residuals give exactly the five-dimensional domain named
by the route. The minimum translation is `(2,2)`, which makes every shifted input and environment
label nonnegative at residual `P=Q=0`.

The `PROVED` fixed-original-side endpoint lemma supplies the separate-convexity and phase reduction
from arbitrary eliminated weights to these 36 correlated endpoints while keeping the two listed
side outputs attached to the original channel.

**Verdict:** static PASS for the current source and exact route orientation. This finding does not
bind the archived execution to this source.

## 4. Finding ECT-IR-02 — current exact reconstruction and directed inequalities statically PASS

**Applies to:** the same route implication.

**Stable current-source locators:** `certify_su3_triangular_three_face_clusters.py`, functions
`gram_denominator`, `reconstruct_gram_numerator`, `side_denominator`,
`reconstruct_side_numerators`, `correlated_side_entropy_upper`, and `certify`;
`certify_su3_highest_edge_adjacent_faces.py`, functions `tensor_interpolate`, `compactify`, and
`bernstein_coefficients`; `su3_common_den_controls.py`, functions `rational_range_common` and
`split_common_controls`; `certify_su3_all_elementary_cycles.py`, functions
`reduced_log_bounds`, `log_bounds`, `entropy_bounds`, and `isotropic_probabilities`.

The current source uses `fractions.Fraction` or exact integers throughout the certificate-critical
formulas, interpolation, compactification, Bernstein conversion, common-denominator range
comparison, de Casteljau splitting, logarithm intervals, entropy intervals, and leaf acceptance.
I independently recomputed:

- Gram common-denominator label degrees `(12,12)` and reconstruction degrees
  `(12,12,2,2,2)`;
- side common-denominator label degrees `(4,4)` and reconstruction degrees
  `(4,4,1,1,1)`;
- 36 Gram endpoint patterns; and
- two retained original-side distribution groups.

Every Gram interpolant is checked at two additional rational points, and every side interpolant is
checked at a separate rational point. Compactification is an exact common homogenization under
`P=a/(1-a)` and `Q=b/(1-b)`. The common-denominator backend compares ratios using exact integer
cross multiplication, rejects negative denominator controls and unmatched projective zeros, and
halves Bernstein controls exactly.

The 24-term odd `atanh` series gives a lower logarithm endpoint and an explicit positive tail gives
the upper endpoint. Power-of-two restoration reverses the `ln 2` endpoints when the exponent is
negative. Entropy lower/upper directions therefore match their use: the Bell entropy receives a
lower bound at the upper Gram parameter, each legal side entropy receives an upper bound, and a
leaf is accepted only by the exact rational test

`bell_lower - 2*side_upper > 0`.

The adaptive stack begins with the full closed five-cube. In the current source, any unresolved box
at maximum depth raises `AssertionError("uncertified box",...)`; final count, margin, and Bell-no-go
lines occur only after the stack is empty. Thus a source-bound exit-zero execution of this exact
source would prove full coverage rather than sampling.

**Verdict:** static PASS for the current implementation. This is not a verdict on the historical
run, whose executed source is unknown.

## 5. Finding ECT-IR-03 — the historical transcript is not source-bound and BLOCKS completion

**Applies to:** both exact target hashes in section 2.

The complete archived transcript is only five lines. It reports:

- 36 Gram branches and degrees `(12,12,2,2,2)`;
- two retained side distributions and degrees `(4,4,1,1,1)`;
- 2,263 certified boxes;
- a displayed margin `1.915664030824e-04` and one dyadic box; and
- the final Bell-no-go sentence.

It does **not** record the invoked command, working directory, interpreter or version, environment,
launch/end times, PID/session, exit status, stderr, progress checkpoints, source-tree snapshot,
source hashes, import closure, configuration values, or post-completion drift check. Its
`environment-centered` prefix is only a name; without source binding it does not prove which
cluster or implementation produced the lines.

Filesystem metadata makes retrospective substitution especially invalid:

| object | filesystem mtime (America/New_York) |
|---|---|
| archived transcript | 2026-08-30 08:41:04 -0400 |
| current `su3_common_den_controls.py` | 2026-08-30 11:52:47 -0400 |
| current `certify_su3_triangular_three_face_clusters.py` | 2026-08-30 11:53:21 -0400 |

The current driver hash is
`sha256:37b481a43c6f646a541ed9e0b87f9ac744e9c565ff1f6df1f75da0b3adbb6573`, and the current
common-denominator backend hash is
`sha256:39f0e98fac092a101c3d8eeeeac939c7683af1851d09a1a6f8d8c85e97f8584c`.
Both files postdate the transcript. The historical Python process, if it ran at or before the
transcript time, necessarily used earlier in-memory bytes or an unrecorded copy. No archived
launch-source tree or prelaunch hash manifest was found. Inspecting current files cannot establish
the contents or behavior of those earlier bytes.

The five terminal-looking lines are mutually compatible with the current fail-closed loop, but
compatibility is not provenance. In particular:

- `2,263` is only an assertion in the transcript; no exit status or complete tree record establishes
  normal termination or absence of uncertified maximum-depth boxes;
- the current source's final print sites cannot be used to interpret an unbound historical source;
  and
- a present-day reproduction command in the prose artifact does not identify the command that
  created the historical file.

**Verdict:** BLOCK. Neither the route implication nor atomic claim may be promoted on this dossier.

## 6. Finding ECT-IR-04 — the displayed decimal is not a directed exact lower bound

The current source stores every accepted margin as an exact `Fraction`, but prints

`float(smallest_margin):.12e`.

That formatting is a nearest floating rendering. It does not prove the literal inequality

`smallest_margin > 1.915664030824e-04`

written in the prose artifact. If a source-bound run of the current source exits normally, the
exact comparison `margin>0` proves strict positivity, which is sufficient for the route and node
statements because neither contains a quantitative threshold. It does not by itself license the
last digit of the displayed decimal as a directed lower endpoint.

A fresh dossier should print the exact smallest `Fraction` (numerator and denominator), or a
rational decimal floor constructed and checked below it. Until then the decimal must be described
only as “displayed as approximately ...”, not as an exact certified `>` threshold.

**Verdict:** nonfatal to the qualitative claim after a valid fresh run, but the current prose's
quantitative sentence is unsupported as written.

## 7. Exact repair gate and promotion boundary

The existing `CONJECTURED` assessments are appropriate and must not change on this review. A fresh
execution amendment may authorize promotion only if it verifies all of the following:

1. a prelaunch immutable source snapshot and SHA-256 manifest for the full recursive local import
   closure, captured before process creation;
2. exact command, working directory, interpreter path/version, configuration, launch/end time,
   PID/session or equivalent run identifier, and merged stdout/stderr;
3. unchanged snapshot hashes and a recorded working-tree drift check after completion;
4. child exit status 0 and the required terminal tokens;
5. actual configuration `((-2,1),(-1,2),(0,0))`, retained `(0,2)` binary and `(1,0)` ternary;
6. exactly 36 endpoint branches with degrees `(12,12,2,2,2)` and two retained side distributions
   with degrees `(4,4,1,1,1)`;
7. complete adaptive-tree accounting, terminal leaf count, zero pending boxes, and no
   `uncertified box` exception;
8. the exact positive smallest `Fraction`, or a separately verified directed rational lower
   decimal; and
9. a transcript hash bound to the unchanged route and claim hashes in section 2.

The independently reviewed source-bound runner in this project is suitable for a fresh run, but
its existence does not retroactively cure this legacy transcript.

Even after that gate passes, the only eligible order is route
`fixed-binary-ternary-original-side-cover` first and then the atomic node, after reconfirming both
premises remain `PROVED`. No aggregate triangular parent, sibling orientation, non-Bell claim, or
Question 3 root is authorized by this review.

## 8. Independent checks performed and limitations

Without changing proposer material, I:

- read both repository protocols in full;
- recomputed the exact target and premise statement hashes;
- verified the two premise levels and their hash-bound independent-review links;
- rebuilt the labelled union, six input incidence sets, retained/eliminated partition, 36-pattern
  product, minimum shift, and five-variable dimension;
- recomputed both denominator degree tuples from the current exact source;
- traversed the current six-file local import closure and hashed every member;
- audited exact interpolation, compactification, Bernstein/common-denominator arithmetic,
  directed logarithm/entropy bounds, and fail-closed adaptive logic;
- compared transcript and source filesystem chronology; and
- treated the printed decimal only as an approximate rendering, not a directed exact bound.

I did not rerun the long adaptive certificate. More importantly, no rerun of current source can
retroactively identify the unknown historical source; it must be archived as a new dated run and
reviewed on its own source-bound dossier.

Only public artifacts, source, exact calculations, and repository metadata were used. Hidden or
private chain of thought was neither requested nor used as evidence.
