---
id: "ADDGAP.noise-flag-damping"
node_file: "channel-capacity/additivity-gap/proof-dag/nodes/ADDGAP.noise-flag-damping.md"
aliases: ["P7"]
kind: LEAF
role: proof
status: OPEN
status_source: "brainstorm registration 2026-08-29"
disposition: PARKED
parents: ["ADDGAP.goal"]
children: []
related: ["ADDGAP.ef-flag-amplification"]
---

# ADDGAP.noise-flag-damping — suppress same-side defects with wrappers

## Claim

Wrap a known nonadditive channel pair with erasure/noise and classical flags so the desired matched
cross advantage decays more slowly than all same-side tensor correlations, allowing repeated blocks
to accumulate a net linear defect.

## Role in DAG

Engineering route aimed directly at the leakage terms obstructing naive tensor-power amplification.

## Current status

OPEN / PARKED. No wrapper inequality separating the decay rates has been established.

## Dependencies

Exact formulas or sharp continuity bounds for the wrapper's one-shot and product Holevo/minimum-
output-entropy quantities.

## Work record

- 2026-08-29 — registered and PARKED. Activation requires a two-rate inequality, not numerical
  evidence from a few tensor powers.

## Evidence

None yet.

## Adversarial reviews

None yet.

## Open obligations

Specify one wrapper and derive the cross-versus-self decay comparison symbolically.

## Status history

- 2026-08-29 — created OPEN / PARKED.

