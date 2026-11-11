# Classical denominators and shifted duplication: research checkpoint

Date: 2026-09-07. This is a navigation summary; the claims and evidence
levels are owned by the linked canonical YAML nodes, not this prose.

## STATE

The project has moved from the vector spectral optimum to exact classical
denominators and to a normalization issue that matters when composing
group-orbit constructions. These results do not solve a Grothendieck
constant, the general classical optimization problem, or a new-record problem.

For the full signed D_r roots W and A_r=WW^T/[4(r-1)], the classical-value
chain now has a complete author proof, exact finite replays, and separate
author-independent adversarial reviews:

- [GROTHORB.root-classical](../proof-dag/nodes/GROTHORB.root-classical.yaml):
  beta_cl(A_r)=2r(2r-1)/3 for every r>=3. The proof is global, via the
  root support function, not extrapolated from finite-r checks.
- [GROTHORB.root-classical-equality](../proof-dag/nodes/GROTHORB.root-classical-equality.yaml):
  every optimal ordered sign pair is diagonal and has Weyl-chamber signs;
  there are exactly 2^(r-1)r! pairs, with no global-sign quotient.
- [GROTHORB.root-small-shift](../proof-dag/nodes/GROTHORB.root-small-shift.yaml):
  the same pair remains optimal for
  0<=lambda<=1/[4r(r-1)^2], giving beta_cl(A_r-lambda I)=2r(2r-1)/3-2r(r-1)lambda.
  This is only a sufficient interval, not the maximal interval.

The full D3 parameter calculation is separately auditable:

- [GROTHORB.d3-envelope-method](../proof-dag/nodes/GROTHORB.d3-envelope-method.yaml)
  records complete 4096-sign exact enumeration, row kinks, line crossings,
  and endpoint coverage. A reviewer wrote an independent integer endpoint
  checker; convexity supplies the continuum upper bound between endpoints.
- [GROTHORB.d3-shift-envelope](../proof-dag/nodes/GROTHORB.d3-shift-envelope.yaml)
  gives 10-12lambda on [0,1/4] and 8-4lambda on [1/4,1/2], with explicit
  fixed sign pairs attaining both lines.
- [GROTHORB.shift-linear-candidate](../proof-dag/nodes/GROTHORB.shift-linear-candidate.yaml)
  retains the failed whole-interval extrapolation. At r=3, lambda=1/2,
  an explicit pair scores 6 rather than its predicted 4. This precise
  failure does not refute any smaller-domain theorem or the main research
  program.

The duplication comparison explains why full roots and half roots must be
kept distinct after a diagonal modification:

- [GROTHORB.antipodal-shift-comparison](../proof-dag/nodes/GROTHORB.antipodal-shift-comparison.yaml)
  gives the exact ternary-sign optimization for arbitrary real square C.
  For D(C)=(1/2)[C,-C;-C,C], beta_cl(D(C)-lambda I)>=2beta_cl(C-lambda I),
  with equality at lambda=0. Positive-lambda equality is not asserted.
- [GROTHORB.d3-half-shift-value](../proof-dag/nodes/GROTHORB.d3-half-shift-value.yaml)
  proves beta_cl(UU^T/4-I_6/3)=3 for the six positive D3 roots.
  Its upper certificate has three hand-checkable signed-edge cases;
  all 64 Bob signs and all 4096 ordered pairs were also replayed exactly.
- [GROTHORB.shift-duplication-gap](../proof-dag/nodes/GROTHORB.shift-duplication-gap.yaml)
  compares the correctly reordered matrices at lambda=1/3:
  full-root beta is 20/3, whereas twice the half-root beta is 6.

The reviews distinguish exact finite proof, all-parameter algebra,
failed conjectures, and open work. They disclose author/reviewer separation
within a shared model family, lack of a fresh context in this round, and
the absence of proof-assistant formalization. They are not independent
human or cross-model certification.

## PRIOR-ART

[classical-root-literature-20260907.md](classical-root-literature-20260907.md)
checks primary-source locators and normalization. The unshifted D_r
family/classical value and diagonal-shift construction have prior-art
counterparts; these are not presented as novel discoveries.
The explicit elementary certificates serve as verified interfaces.
No originality claim for the other consequences has passed a novelty review.

The half-root unit Gram convention P=UU^T/2 differs from our projection
C=P/(r-1). The literature shift mu corresponds to lambda=mu/(r-1).
After duplication a further symmetric-block term appears; ignoring it
would incorrectly identify distinct classical optimization problems.

## REPLAY

Run from the repository root with Python assertions enabled:

    PYTHONDONTWRITEBYTECODE=1 python3 grothendieck-group-orbit/tools/check_root_classical_value.py
    PYTHONDONTWRITEBYTECODE=1 python3 grothendieck-group-orbit/tools/check_root_classical_equality.py
    PYTHONDONTWRITEBYTECODE=1 python3 grothendieck-group-orbit/tools/check_d3_classical_envelope.py --check grothendieck-group-orbit/artifacts/d3-classical-envelope-certificate-20260907.json
    PYTHONDONTWRITEBYTECODE=1 python3 grothendieck-group-orbit/tools/check_d3_envelope_review.py
    PYTHONDONTWRITEBYTECODE=1 python3 grothendieck-group-orbit/tools/check_d3_half_shift_value.py
    PYTHONDONTWRITEBYTECODE=1 python3 grothendieck-group-orbit/tools/check_shift_duplication_gap_review.py
    PYTHONDONTWRITEBYTECODE=1 python3 grothendieck-group-orbit/tools/check_weighted_isotropic_optimum.py
    PYTHONDONTWRITEBYTECODE=1 python3 grothendieck-group-orbit/tools/check_minimum_settings_isotropic.py
    PYTHONDONTWRITEBYTECODE=1 python3 grothendieck-group-orbit/tools/check_clifford_generators.py

The reviewer first froze its endpoint-checker source at
artifacts/d3-envelope-review-endpoints-20260907.py. That immutable audit
input remains at its original reviewed path; the byte-identical runnable
copy now resides in tools/check_d3_envelope_review.py under FILE_PROTOCOL.
The immutable review report was not silently rewritten to conceal placement.
The node links the project-specific runnable checker and the frozen review.

All universal conclusions require the linked proofs and reviews, not just
these replay exit codes. Structural validation likewise is not a truth test.

## NEXT

[GROTHORB.rch-reduction](../proof-dag/nodes/GROTHORB.rch-reduction.yaml)
now has a complete reviewed orthogonal R/C/H multiplicity and PSD reduction.
Its repaired claim explicitly fixes finite permutation setting actions;
the [preserved model diagnostic](rch-model-clarification-20260907.md) shows
why arbitrary orthogonal setting actions do not suffice. Original affine
balance constraints remain in force after block reduction. This is the
invariant subset, not every extremizer or the unrestricted minimum-rank
problem. The real-Schur input is registered explicitly.

The pre-existing physical-realization interface
[GROTHORB.measurements](../proof-dag/nodes/GROTHORB.measurements.yaml)
has now passed its separate all-rank review and exact small-rank replay.
A rank-s feasible weight gives the explicit maximally entangled/Clifford
construction in local dimension 2^floor(s/2); this is an achievable
dimension, not a proof that no smaller physical realization exists.
The standard construction is retained as setup rather than a novel result.

The weighted continuation,
[GROTHORB.weighted-isotropic-optimum](../proof-dag/nodes/GROTHORB.weighted-isotropic-optimum.yaml),
moves beyond a single transitive orbit: positive weighted isotropic unit
frames on possibly different-sized sides give vector optimum S*T/r.
The complete claim passed its author-independent correctness review.
The separate source check identifies the weighted upper
certificate as a standard diagonal SDP consequence; the unweighted two-frame
formula is already explicit in Pal--Vertesi.

[GROTHORB.minimum-settings-isotropic](../proof-dag/nodes/GROTHORB.minimum-settings-isotropic.yaml)
certifies the framework-scoped setting count r(r+1)/2+1 with a coordinate/
coordinate-difference construction. The independent literature check found
the same count and directions in Gribling--de Laat--Laurent, with an earlier
equivalent Bell family and its classical formula in Vertesi--Pal (2009).
This is retained as a reproduced interface, not a new construction or an
unsolved classical-value problem. See
[weighted-orbit-literature-20260907.md](weighted-orbit-literature-20260907.md)
for exact source locators and normalization, together with its separately
preserved [bibliographic correction and conditioning comparison](weighted-orbit-literature-correction-20260907.md).

The quantitative continuation is
[GROTHORB.minimal-setting-conditioning](../proof-dag/nodes/GROTHORB.minimal-setting-conditioning.yaml):
an upper bound for the smallest eigenvalue of the traceless quadratic-
measurement frame operator at the minimal setting budget. Its complete
rank/trace proof passed a separate author-independent review. The bound
must not be conflated with a sharp attainable constant, an operational
noise guarantee, or a completed novelty assessment.

The associated reviewed equality statement is
[GROTHORB.minimal-conditioning-equality](../proof-dag/nodes/GROTHORB.minimal-conditioning-equality.yaml):
characterizing attainment through one equiangular tight side, unbiased cross
overlaps, and a lower bound for the opposite centered frame operator.
The exact iff passed its separate author-independent review. An
attainment criterion alone does not prove that such frames exist in every
dimension, or identify the optimal value when attainment is impossible.
The [four-source comparison](minimal-conditioning-equality-literature-20260907.md)
documents known ETF/unbiased-frame structure and the distinct asymmetric
scope. Failure to find the exact complete iff in that bounded search does
not certify originality.

The all-dimensional classical continuation is now reviewed as
[GROTHORB.psd-antipodal-linear-window](../proof-dag/nodes/GROTHORB.psd-antipodal-linear-window.yaml)
and [GROTHORB.root-extended-shift-window](../proof-dag/nodes/GROTHORB.root-extended-shift-window.yaml).
The first supplies a four-term nonnegative gap certificate, valid for
every real symmetric PSD C, including singular inputs and closed endpoints:

    beta_cl(D(C)-lambda I_(2N)) = 2 beta_cl(C)-2N lambda,
    0 <= lambda <= (1/2) min_i C_ii.

The separately reviewed root assembly therefore gives, for every r>=3,

    beta_cl(A_r-lambda I_n) = 2r(2r-1)/3-n lambda,
    n=2r(r-1),  0 <= lambda <= 1/[2(r-1)].

This widens the earlier sufficient interval by the factor 2r(r-1).
The separately reviewed
[GROTHORB.root-shift-window-maximality](../proof-dag/nodes/GROTHORB.root-shift-window-maximality.yaml)
now proves that this closed interval is exact among lambda>=0: a concrete
ordered sign pair exceeds the affine value by
4(lambda-1/[2(r-1)]) at every parameter beyond the endpoint. It does not
compute the full post-window envelope.

The reviewed
[GROTHORB.psd-antipodal-interior-equality](../proof-dag/nodes/GROTHORB.psd-antipodal-interior-equality.yaml)
also classifies every ordered optimizer in the strict interior: it must be
a=b=(z,-z), with z maximizing z^T C z. This classification deliberately
excludes lambda=0, the upper endpoint, and zero-diagonal inputs.
The [exact claim and route audit](../reviews/psd-antipodal-window-review-20260907.md)
is separate from the [bounded prior-art comparison](psd-antipodal-window-literature-20260907.md).
The latter did not locate the same interval theorem in its accessible
sources; the original Fishburn--Reeds full text was not accessible. This
is not an originality certificate or a new Grothendieck record.

Other precise remaining questions are the full post-window envelope,
the upper-endpoint and zero-diagonal equality classifications, and useful
rectangular or multi-orbit families with an independently certified classical
denominator. The R/C/H and measurement interfaces have passed their scoped
reviews; the wreath question and all broader unresolved scopes remain
preserved. Do not revive unrelated H4/E8 campaigns from this checkpoint.
