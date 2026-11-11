---
id: "ADDGAP.goal"
node_file: "channel-capacity/additivity-gap/proof-dag/nodes/ADDGAP.goal.md"
aliases: ["G"]
kind: GOAL
role: proof
status: OPEN
status_source: "problem-scaffold-2026-07-28"
disposition: null
parents: []
children: ["ADDGAP.pair-to-self", "ADDGAP.matched-independent-tensors", "ADDGAP.explicit-witness", "ADDGAP.beyond-one-bit", "ADDGAP.holographic-toy", "ADDGAP.ef-flag-amplification", "ADDGAP.noise-flag-damping"]
related: ["ADDGAP.montanaro-gate"]
---

# ADDGAP.goal — Size of the Hastings additivity gap

## Claim

Determine sup Delta = S_min(N1) + S_min(N2) - S_min(N1 tensor N2); in particular decide whether extensive violations (qubit-linear dimensions, Delta(n) >= C n) exist. **[OPEN]**

## Role in DAG

Problem GOAL; the lead-flagged frontier problem of the classical-additivity branch.

## Current status

OPEN. Hastings 2009 gives Delta > 0; the 18-year record stays below log 2. Extensive form and dichotomy: Hayden–Penington — extensive violations exist XOR an almost-basis of disentangled black-hole microstates exists (see `../../../literature/papers/hayden-penington-2020-black-hole-additivity/`). Frontier class: per the capability-boundary stop-loss, no open-ended proving; only pre-gated bounded probes.

## Dependencies

None recorded yet beyond the shared field literature in `../../../literature/` (catalog + per-paper pages; see `../../README.md`).

## Strategy blueprints

The following children were registered before verification, as required by rule 8. Each is an
OR-route toward the extensive-violation part of the goal; none presently licenses a completion
tier.

1. `ADDGAP.pair-to-self`: first obtain an extensive defect for a possibly unequal pair of channels,
   balance their one-shot Holevo quantities by a classical side channel, and take a flagged direct
   sum. The direct-sum identity should lose only the universal additive constant `log2(9/4)`, so a
   linear pair defect would compose into a linear same-channel defect.
2. `ADDGAP.matched-independent-tensors`: take many independently sampled Hastings-type channels and
   their matched conjugate partners. Product Bell witnesses add the desired cross defects; a
   sufficiently strong single-side near-additivity theorem would make the two leakage terms
   sublinear, leaving a linear total defect.
3. `ADDGAP.explicit-witness`: derandomise a finite `p=1` Hastings/BCN witness and then look for a
   tensor-stable algebraic pattern. This would replace high-probability existence by a checkable
   finite family before amplification.
4. `ADDGAP.beyond-one-bit`: search directly for a finite-dimensional `p=1` pair defect exceeding one
   bit. Such a witness would sharpen the record and may cross the constant-loss gate in reductions,
   but by itself would not prove an unbounded gap.
5. `ADDGAP.holographic-toy`: turn the Hayden--Penington black-hole dichotomy into a finite tensor-
   network or random-code channel family whose entropy inequalities are explicit enough to certify.
6. `ADDGAP.ef-flag-amplification`: translate the problem through the entanglement-of-formation /
   constrained-Holevo equivalence and search for a flagged state construction with additive defect.
7. `ADDGAP.noise-flag-damping`: wrap a known nonadditive pair with erasure/noise and classical flags
   so unwanted same-side correlations are damped faster than the matched cross advantage.

## Work record

- 2026-07-28 — node registered at problem-scaffold creation (rule 8); no work commissioned yet.
- 2026-08-29 — seven candidate routes registered before verification (rule 8b); active bounded
  probes are `ADDGAP.pair-to-self` and `ADDGAP.matched-independent-tensors`. The other five are
  PARKED pending a positive gate from the active probes or a new quantitative invariant.

## Evidence

None yet.

## Adversarial reviews

None yet.

## Open obligations

- Decide whether the Montanaro weak-multiplicativity estimate is strong and uniform enough for the
  leakage bound required by `ADDGAP.matched-independent-tensors`.
- Put the constant-loss formula in `ADDGAP.pair-to-self` through an independent rule-6/7 review
  before using it as a theorem.

## Status history

- 2026-07-28 — created OPEN (problem scaffold, lead directive; carried over from the same-day field-level scaffold).

