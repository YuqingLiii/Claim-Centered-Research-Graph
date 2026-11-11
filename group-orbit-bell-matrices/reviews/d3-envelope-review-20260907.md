# Independent review of the D3 envelope and linear-proposal counterexample

Date: 2026-09-07. Reviewer: Codex agent `/root/orbit_root_prior_art`,
same-model agent review. Reviewed root:
`/private/tmp/grothorb-classical-20260907-R0Shtu`.

Verdict: **PASS** for the exact finite method, the stated D3 envelope,
and route `exact-envelope`. **FAIL** for the universal linear-shift claim:
its exact counterexample is verified. No mathematical defect requiring
repair was found in the scoped D3 argument or implementation.

## Independence, scope, and limitations

The reviewer did not author the D3 enumerator, certificate, dossier, or
registered D3 statements. Earlier in this same agent context, the reviewer
performed the separate root-family literature check and authored
`classical-root-literature-20260907.md`. The parent also supplied the
candidate D3 formula before this review. Accordingly, this is a separate
author/reviewer assignment, **not a fresh-context review**. The reviewer's
own literature note is excluded from the review and is not evidence for
any verdict below.

The reviewer read the current three node YAML files, the complete dossier,
the full JSON certificate, the author checker source, and the author run
record. Both repository protocols had already been read completely.
The exact author checker was replayed with assertions enabled. A second
implementation was then written and run: it imports neither author code
nor the JSON certificate, constructs roots and signs differently, and
uses only integer endpoint tests and fixed bilinear witnesses.

Both implementations use Python 3.9.6 in the shared environment. Agreement
does not remove common model, interpreter, or hardware failure modes.
This is exact finite computation plus a human-readable mathematical
argument, not proof-assistant formalization, a cross-model review, or a
novelty assessment. No author artifact or node was edited by this reviewer.
The conclusions concern only `r=3`, `A=WW^T/8`, all 12 full roots,
independent Alice/Bob signs, and the stated closed parameter interval.

## Materials and reproducibility

Paths below are relative to `grothendieck-group-orbit/`.

| Frozen input | SHA-256 |
|---|---|
| `proof-dag/nodes/GROTHORB.d3-envelope-method.yaml` | `586f0088e9c755b8da958667b1798f5b5781a5dfedf1439a39c33e31f524ffef` |
| `proof-dag/nodes/GROTHORB.d3-shift-envelope.yaml` | `b6ae358b6f21e2a9b2a2993b441db9ca30256f6f09d5d54ce98aef834fe1ed96` |
| `proof-dag/nodes/GROTHORB.shift-linear-candidate.yaml` | `9601f9b7dae807bd9cd3343f19c95975ea3710e3ecb95e0369c5c59701538dc1` |
| `artifacts/d3-classical-envelope-20260907.md` | `6ad6e414f575b27881c193181375d4134ec84cf234a5a8aa4dfacf3958072c57` |
| `artifacts/d3-classical-envelope-certificate-20260907.json` | `f3461a1682c90bc52bc13a1b3a54f2e000d1b30b3ae7cd910d28bc4d912c4c12` |
| `tools/check_d3_classical_envelope.py` | `a31c7a9e8fb903d2ca608a2ce03ece4105e57120966c88253f4641e7a174898b` |
| `artifacts/d3-classical-envelope-exact-check-20260907.txt` | `b5d62d13c20457b86a92264b05b73422b82c75b0e4174e64f355e10e2bece575` |

Reviewer-created evidence:

- [Independent integer checker](../artifacts/d3-envelope-review-endpoints-20260907.py),
  SHA-256 `e01974a1678631c98b3f4117b82ab4dc0527fecd76203cefb4bdd64d51abcbf1`.
- [Fresh replay commands and exact output](../artifacts/d3-envelope-review-rerun-20260907.txt),
  runs R1 and R2, including input digests and statement-hashing convention.

Both runs exited 0. R1 recomputed the entire certificate and matched full
JSON object equality. R2 exhausted 4096 distinct Bob signs and checked
all of them separately at `lambda=0,1/4,1/2`; maxima were `10,7,6`.
The six mathematical inputs above were hashed again after execution and
were unchanged. The author run record was checked as provenance, not used
instead of the reviewer's fresh replay.

## F1. Exact enumeration method claim — PASS

Target: `GROTHORB.d3-envelope-method`, node claim.

`reviewed_hash: sha256:05cef7880b04166520d3a3ec4e6130492c7d64ff3057a987dc5529b1bd32dd8a`

The exact parsed `claim.strip()` reviewed is:

> For A_3 the 12 by 12 full D_3 root projection, exhaustive enumeration of all Bob sign vectors t and the rational upper envelope of sum_i |(A_3 t)_i-lambda*t_i| computes beta_cl(A_3-lambda I) exactly for every lambda in [0,1/2], with a matching Alice sign vector on each affine piece.

For fixed `t`, Alice maximizes each coordinate independently, giving the
sum of absolute values, with either sign valid at zero. The author code
includes all `2^12` Bob vectors without quotienting. Its matrix is the
full-root Gram divided by 8, not the half-root Gram or a shifted variant
with another normalization. Independent construction checked all 12 roots,
their antipodes, `W^T W=8I`, and `A^2=A` using integers.

All possible row zeros in the domain are collected before linearizing.
Each row has at most one zero because `t_i` is nonzero. On each resulting
open base interval, each `f_t` is affine and extends continuously to the
endpoints. Exact coefficients, line multiplicities, all pairwise crossings,
and endpoint dominance checks therefore cover the continuum, including
ties. The retained witness signs are checked directly. `Fraction` is used
throughout the author's mathematics; R1 ran with optimization flag 0.
Evidence: dossier D3-1--D3-2, checker `compute()`, replay R1.

## F2. D3 piecewise envelope claim — PASS

Target: `GROTHORB.d3-shift-envelope`, node claim.

`reviewed_hash: sha256:260cf713d4cd254ef432bf6fa2130718be433b157e0186f6f5cc386973b105d5`

The exact parsed `claim.strip()` reviewed is:

> For the 12 by 12 full D_3 root projection A_3=WW^T/8, beta_cl(A_3-lambda I)=10-12*lambda for 0<=lambda<=1/4, and beta_cl(A_3-lambda I)=8-4*lambda for 1/4<=lambda<=1/2.

R2 provides a shorter, algorithmically different upper-bound argument.
Let `M=8A` and write an endpoint as `lambda=p/8`, where `p=0,2,4`.
For every one of the 4096 signs `t`, R2 verifies
`sum_i |(Mt)_i-p*t_i| <= 80,56,48`, respectively. For fixed `t`,
`f_t(lambda)` is convex. Its values inside either interval lie below the
chord joining its endpoint values, which lies below the proposed affine
line because both endpoint bounds hold. Hence the inequalities hold for
every real parameter in both closed intervals; these are not grid-based
inferences about a possibly nonconvex objective.

The two fixed witness pairs in dossier D3-3 were reindexed into R2's
different root order. Direct integer bilinear evaluation yielded
`8s^TAt=80, s^Tt=12` and `8s^TAt=64, s^Tt=4`, respectively.
They attain `10-12lambda` and `8-4lambda` on the required intervals.
The two formulas agree at `lambda=1/4`, where both give 7; endpoints
`lambda=0` and `lambda=1/2` give 10 and 6. Upper and lower bounds match.
No all-r formula or quantum/vector-optimum theorem is used.
Evidence: dossier D3-3, replay R1, independent run R2.

## F3. Exact-envelope route implication — PASS

Target: `GROTHORB.d3-shift-envelope`, route `exact-envelope`.
Listed premise: `GROTHORB.d3-envelope-method`.

`reviewed_hash: sha256:d32e8679073f1f96fb3eeca4f9ce966656f5c75eb74e835f152adcecb98a81cf`

The exact parsed `implication.strip()` reviewed is:

> Exhausting all 4096 Bob sign vectors with exact rational row breakpoints and affine-line crossings leaves these two upper-envelope pieces, each attained by an explicit Alice and Bob sign pair.

The completed run realizes the registered method rather than merely
assuming its output. R1 verifies row breakpoints `0,1/4,1/2`, 18 and 17
distinct lines, total multiplicity 4096 on each interval, all 21 interior
pairwise crossings, and 23 elementary cells. The endpoint dominance
inequalities bound every enumerated line on its entire cell. Full JSON
equality includes the merged pieces and concrete witnesses, and all
original absolute-value functions are rechecked at merged boundaries.
F1 establishes the method's exactness; the frozen computation and witnesses
then imply exactly the F2 claim. R2 independently confirms the mathematical
conclusion without any crossing or line-merging implementation. There is
no unregistered all-r premise or reliance on the refuted linear proposal.
Evidence: certificate `base_intervals`, `pieces`, `endpoint_checks`;
checker `compute()`; replays R1--R2.

## F4. Universal linear-shift claim — FAIL; exact refutation PASS

Target: `GROTHORB.shift-linear-candidate`, node claim.

`reviewed_hash: sha256:8f149d1b408a8f98ed180b5d0dc1a260d437dc81c46dc91ef77fd58c5b64c269`

The exact parsed `claim.strip()` reviewed is:

> For every r>=3 and 0<=lambda<=1/2, the full D_r root projection A_r=WW^T/[4(r-1)], n=2r(r-1), satisfies beta_cl(A_r-lambda I)=2r(2r-1)/3-n*lambda.

Take `r=3`, `lambda=1/2`, and the second fixed witness pair in D3-3.
Direct full bilinear evaluation in R2 gives
`s^T(A-(1/2)I)t=(64-4*4)/8=6`. The claim predicts
`2*3*(2*3-1)/3-12/2=4`. Since the classical maximum is at least this
valid sign-pair value, `6>4` refutes the universal equality. This argument
needs no correctness assumption about the computed upper envelope.
The witness uses the stated full root matrix and an allowed boundary point.

The refutation applies to the whole-interval universal assertion only.
It does not refute the unshifted value, the first D3 interval, another
specified smaller domain, or a new candidate for larger ranks. The failed
proposal and its adverse evidence should remain in the research record.
Evidence: dossier D3-4, certificate `linear_proposal_counterexample`,
independent run R2's direct `48/8>32/8` check.

## Closeout

Each `reviewed_hash` above is SHA-256 of the UTF-8 encoding of the exact
parsed YAML `claim.strip()` or route `implication.strip()`, not the file
digest or rendered quote. PyYAML 6.0.3 supplied parsing only; it was not
used by either mathematical checker. Input digests and literal statements
make the review scope inspectable. A changed statement needs renewed
review even if this filename remains linked.

The report supports the scoped mathematical verdicts above. Protocol
promotion, graph regeneration, and canonical integration remain the
coordinator's responsibility. This report and the reviewer-created rerun
artifacts are frozen at completion; no novelty or literature-note verdict
is included.
