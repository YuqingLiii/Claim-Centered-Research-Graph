---
id: "ADDGAP.fixed-r-diagonal-gate"
node_file: "channel-capacity/additivity-gap/proof-dag/nodes/ADDGAP.fixed-r-diagonal-gate.md"
aliases: ["P2b"]
kind: LEAF
role: proof
status: OPEN
status_source: "fixed-factor-count literature gate opened 2026-08-29"
disposition: null
parents: ["ADDGAP.matched-independent-tensors"]
children: []
related: ["ADDGAP.montanaro-gate"]
---

# ADDGAP.fixed-r-diagonal-gate — dimension-first independent-product additivity

## Claim

Determine whether a published random-channel theorem proves the following strong statement for
every fixed positive integer `s`: for independent channels `N_1,...,N_s` in a `p=1` Hastings/BCN
ensemble,

`Smin(N_1 tensor ... tensor N_s)=sum_i Smin(N_i)+o(1)`

with probability tending to one as an auxiliary dimension tends to infinity, while simultaneously
each matched pair `(N_i,conjugate(N_i))` has a common positive asymptotic gap.

## Role in DAG

Second stop/go gate for matched-independent amplification. Unlike the Montanaro route, it takes the
large-dimension limit separately for each fixed number of factors and then uses a diagonal sequence.

## Current status

OPEN. Collins--Fukuda--Nechita and related Weingarten papers have been identified as candidates, but
their exact optimisation and quantifiers have not yet been checked.

## Dependencies

BCN's positive matched conjugate/Bell gap and a theorem controlling the **global** minimum output
entropy of a fixed product of independent random channels.

## Work record

- 2026-08-29 — registered before literature verification. The diagonalisation avoids a false
  uniformity requirement: for each fixed `s`, choose the environment/output dimensions large enough
  that all desired events intersect with positive probability, then select one tuple.

## Evidence

Candidate pointers only: Collins--Fukuda--Nechita product-random-channel work cited in Fukuda 2014
and Montanaro 2013.

## Adversarial reviews

None yet.

## Open obligations

- Verify whether the cited papers optimise over all inputs or only evaluate specified Bell/product
  inputs.
- Verify independent-versus-conjugate sampling and the order of limits.
- If the theorem exists, write the finite-intersection/diagonal selection proof with explicit errors.

## Status history

- 2026-08-29 — created OPEN before source verification.

