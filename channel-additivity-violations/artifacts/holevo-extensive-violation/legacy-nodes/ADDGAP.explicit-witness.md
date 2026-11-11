---
id: "ADDGAP.explicit-witness"
node_file: "channel-capacity/additivity-gap/proof-dag/nodes/ADDGAP.explicit-witness.md"
aliases: ["P3"]
kind: LEAF
role: proof
status: OPEN
status_source: "brainstorm registration 2026-08-29"
disposition: PARKED
parents: ["ADDGAP.goal"]
children: []
related: ["ADDGAP.beyond-one-bit"]
---

# ADDGAP.explicit-witness — derandomise a finite p=1 witness

## Claim

Construct a fully explicit finite-dimensional `p=1` channel pair with a rigorously certified
positive minimum-output-entropy/Holevo additivity defect and enough algebraic structure to support
an amplification argument.

## Role in DAG

Derandomisation route; registered because explicitness and existence were separate questions in the
boss's prompt.

## Current status

OPEN / PARKED. Published random-existence and near-one-bit results answer existence without giving
the tensor-stable explicit structure this route needs.

## Dependencies

An exact channel parametrisation and certifiable global lower bounds on the separate minimum output
entropies.

## Work record

- 2026-08-29 — registered and PARKED pending a structural invariant from an active route; blind
  high-dimensional optimisation has no global certificate and is not commissioned.

## Evidence

Literature audit in `../../notes/chatgpt-four-rounds/`.

## Adversarial reviews

None yet.

## Open obligations

Specify a bounded explicit ansatz and a global certification method before activation.

## Status history

- 2026-08-29 — created OPEN / PARKED.

