# Proposed canonical delta — review required

This proposer did not edit canonical YAML. The following is a human-readable proposal for a future independent reviewer/dispatcher; it is not an instruction to apply automatically.

## Proposed evidence event

Link the sealed Round90 package only after a fresh independent review reproduces its manifests and full replay. The event should record:

- twelve exact outer SAT schedules, iterations 112–123;
- 24 exact direct-360 SAT mechanisms, physically replayed in both sectors;
- 24 atomically installed EFSSCs;
- fresh/unstarted iteration 124 with 164 selectors;
- selector-state SHA-256 `854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3`;
- semantic source SHA-256 `d155a897b8771a9821ef4ef14041bb910e7bbb6aaaad7f6cf08b6db1de0f397e`;
- CNF SHA-256 `2dd07d33ff0b29c1f06a7452c3b1c7ca9b6df950e819046f8a712dacb0dd7e5a`, checked and deliberately unsolved.

## Status discipline

Keep `CIRCDIST.gross` and `gap-via-lift` at `CONJECTURED`. Keep `D*_Gross in {11,12}`. Do not record direct UNSAT, arbitrary-round repair, exhaustion, distance-12 construction, universal distance-11 ceiling, route promotion, or root promotion.

A suitable reviewer verdict, if all checks pass, would be a continuation-only proposer clearance. Any canonical edit must be made by the authorized dispatcher after independent review, not by this package author.
