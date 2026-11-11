# SU(3) stale-source run stop record

Date: 2026-08-30

Status: operational provenance record; not a mathematical certificate and not a counterexample.

## Reason for stopping

Independent static reviews established that two long-running exact-certificate processes had
loaded shared Python sources before those sources were later modified. Their launch-time import
closures were not preserved. Consequently, neither process could support a canonical promotion
even if it later exited zero.

The affected processes were:

| target | unified session | PID | promotion blocker |
|---|---:|---:|---|
| input-centered triangular four-side cover | `71901` | `85955` | three current imports postdated launch |
| weakest-bent fixed-three cover | `78883` | `90693` | shared triangular core and common-denominator backend postdated launch |

The exact source tables and static mathematical verdicts are in
`SU3_INPUT_CENTERED_TRIANGLE_RUNNING_CERTIFICATE_STATIC_INDEPENDENT_REVIEW_20260830.md` and
`SU3_WEAKEST_BENT_FIXED_THREE_RUNNING_CERTIFICATE_STATIC_PRE_REVIEW_20260830.md`.

## Action and observed termination

After the blockers were confirmed, both unified sessions received one interrupt character. Each
process terminated with `KeyboardInterrupt` while performing exact `fractions.Fraction`
comparisons in the adaptive rational-range calculation. A subsequent process-table check found
neither PID alive.

No source file was modified to force termination, no result was interpreted as a certificate,
and no route was refuted. The completed static reviews remain valid for the current checked-in
checker design. Promotion now requires a fresh run whose full project-local import closure is
hashed and preserved before launch, followed by an exit-zero transcript and final independent
review.

