# Claude Opus 5 candidate hash-binding review record

Date: 2026-09-07

Reviewer: Claude Desktop, Opus 5. The UI was configured to Effort Max with Fast mode off.

Independence: the reviewer received the frozen V6 archive, treated its claims, evidence and prior
verdicts as untrusted, extracted it to a fresh temporary directory and reconstructed the candidate
arguments. This file is a project-local record of that completed audit, not a new review run.

Audited archive SHA-256:
`8028a2139b05d976e475b3936e2f5b4421548a39363684213922a231cdfc690d`.

## Findings

### Finding CO5-HCP-01

The exact `HCPREV.algebraic-witness-existence/density-and-semidecision` implication was checked at
candidate strength. The reviewer accepted the MOE existence premise, algebraic density,
effective sphere-net bounds, directed algebraic entropy intervals and dovetailed termination
argument, while retaining the no-resource-bound and no-practical-witness caveats.

Reviewed implication hash:
`sha256:0dcb693741d9f9cd389213ea1335a447b5c620b7665d8e38c72422d2a7c62ca3`.

Verdict: PASS at `CONJECTURED` candidate strength; no promotion.

### Finding CO5-HCP-02

The exact `HCPREV.algebraic-witness-existence` claim was checked at candidate strength. The
reviewer accepted computable deterministic existence with eventual termination, but not a usable
dimension, denominator, certificate-size or runtime bound and not a compact printed witness.

Reviewed claim hash:
`sha256:3743cbce35e1083e2f4417fa3ecd1aeefd5b0f3e2cafae55ffe14660e4a56a62`.

Verdict: PASS at `CONJECTURED` candidate strength; no promotion.

## Boundary

The earlier `ALGEBRAIC_WITNESS_EXISTENCE_INDEPENDENT_REVIEW_20260831.md` remains the immutable
record that blocked the superseded pre-repair wording. It is preserved through the node's events,
but it is not used as active support for the repaired hashes.
