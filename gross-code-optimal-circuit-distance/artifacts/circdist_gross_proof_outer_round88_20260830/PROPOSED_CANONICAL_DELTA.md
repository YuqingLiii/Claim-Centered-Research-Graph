# Proposed canonical evidence/frontier delta

Text proposal only.  This package does not edit the canonical Gross node, scheduler, generated views, or reviews.

## Evidence proposal

Add reviewed evidence pointing to `circdist/artifacts/circdist_gross_proof_outer_round88_20260830/` with proposer verdict `CONTINUATION-ADVANCED-NOT-PROVED`.

Record that Round88 proved a finite order-preserving compression to times `0..863`, compiled the full frozen outer formula to independently checked CNF, and processed iterations 109 through 111.  Each outer formula was SAT and each candidate had SAT weight-10 unrestricted direct-360 mechanisms in both Xerr and Zerr.  All six mechanisms were independently assignment/physical replayed and installed atomically as exact EFSSC selectors.

## Frontier proposal

Replace only the continuation pointer after independent review with:

- next iteration: 112;
- `started: false`;
- inherited reviewed order exclusions: 14,484 = 1,440 unary + 20 Round62 + 12,820 generalized + 204 dynamic;
- exact selectors: 140 = 120 Round80 + 14 Round86 + 6 Round88;
- selector-state SHA-256: `a0364547f846fd68ace7cdba85d89c0f8e6326145243fb0fea7ff543420994cb`;
- independently checked unsolved iter112 outer CNF: 398,488 variables, 1,330,104 clauses, 19,022 assertions, SHA-256 `a8b917845427a0f746e72200a9a58eb5fac86d5e3c845eeaae69082038c86594`.

Keep `frontier.dstar-residual` exactly `{11,12}`.  No outer exhaustion, direct absence, repair result, or distance-12 schedule has been proved.
