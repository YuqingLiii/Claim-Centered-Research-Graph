---
id: "ADDGAP.beyond-one-bit"
node_file: "channel-capacity/additivity-gap/proof-dag/nodes/ADDGAP.beyond-one-bit.md"
aliases: ["P4"]
kind: LEAF
role: proof
status: OPEN
status_source: "brainstorm registration 2026-08-29"
disposition: PARKED
parents: ["ADDGAP.goal"]
children: []
related: ["ADDGAP.explicit-witness", "ADDGAP.pair-to-self"]
---

# ADDGAP.beyond-one-bit — search for a finite p=1 defect above one bit

## Claim

Find and certify a finite-dimensional von-Neumann (`p=1`) additivity defect strictly exceeding one
bit, or establish a new upper bound obstructing such a witness in a specified ensemble.

## Role in DAG

Record-improvement route. It addresses “how large are known examples?” but does not by itself imply
an unbounded or extensive violation.

## Current status

OPEN / PARKED. The audited literature supports defects arbitrarily close to one bit from below, not
a verified `>1`-bit or unbounded finite-dimensional `p=1` family.

## Dependencies

A pre-specified channel ensemble and a global entropy certificate.

## Work record

- 2026-08-29 — registered and PARKED; activate only with a principled ansatz or a theorem reducing
  the global optimisation to finitely many parameters.

## Evidence

`../../notes/chatgpt-four-rounds/round-3-audit.md` and `round-4-audit.md`.

## Adversarial reviews

None yet.

## Open obligations

Identify a bounded search family with rigorous lower/upper certificates.

## Status history

- 2026-08-29 — created OPEN / PARKED.

