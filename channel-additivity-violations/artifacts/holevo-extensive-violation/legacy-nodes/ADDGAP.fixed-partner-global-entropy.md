---
id: "ADDGAP.fixed-partner-global-entropy"
node_file: "channel-capacity/additivity-gap/proof-dag/nodes/ADDGAP.fixed-partner-global-entropy.md"
aliases: ["P2c1"]
kind: LEAF
role: proof
status: OPEN
status_source: "round-5 audit found an exact deterministic reformulation but no proof or counterexample 2026-08-29"
disposition: null
parents: ["ADDGAP.hierarchical-strong-additivity"]
children: []
related: ["ADDGAP.fixed-r-diagonal-gate", "ADDGAP.growing-level-rate"]
---

# ADDGAP.fixed-partner-global-entropy — fixed subspace times random subspace

## Claim

Fix a finite-dimensional Stinespring subspace `U subset C^q tensor C^m`, and let
`W_n subset C^k tensor C^n` be a Haar random subspace of dimension asymptotic to `tkn`, with fixed
`k,t`. Determine whether, with probability tending to one (or almost surely),

`Emin(U tensor W_n) >= Emin(U)+Emin(W_n)-epsilon_n(U)`,

where `epsilon_n(U)->0` and `Emin` is minimum bipartite von Neumann entanglement over unit vectors
of the subspace. Equivalently, for the corresponding fixed channel `Xi` and random channel
`Phi_n`, determine fixed-partner asymptotic additivity of global minimum output entropy.

## Role in DAG

This is the smallest isolated lemma needed to make the hierarchical absolute gap unbounded. It
removes the induction bookkeeping and asks only a two-factor, fixed-reference random-subspace
question. A separate quantitative child is needed for full-size extensivity.

## Current status

OPEN. Existing output-set convergence proves that the optimization has a deterministic limiting
convex body, but does not identify its minimum entropy. Existing fixed/well-behaved-input spectral
results do not optimize over the channel-dependent input vector. Round 5 sharpened the unknown to
the deterministic FCEA support-function inequality and found neither a proof nor a fixed-partner
counterexample.

## Dependencies

Strong convergence/output-set convergence for random Stinespring subspaces, plus a new entropy or
majorization inequality for the resulting matrix-valued/free-compression limit.

## Strategy blueprint

Write a general vector of `U tensor W_n` as a finite Schmidt sum across the fixed input factor. Its
reduced output has the form

`rho_QK=sum_{a,b} Xi(|a><b|) tensor Phi_n(|v_a><v_b|)`.

Because the fixed Schmidt rank is bounded, a matrix-coefficient strong-convergence theorem can
capture the limiting set uniformly over all channel-dependent choices of the vectors `v_a`; this
is what Theorem 8.1 of arXiv:1311.7571 supplies at the level of an unidentified output set. The new
step must prove that the minimum of von Neumann entropy over that limiting set is attained on a
rank-one Schmidt choice, or otherwise establish the displayed additive lower bound. A successful
majorization statement would imply the entropy bound. Conversely, a limiting entangled point with
entropy below the product minimum by a fixed amount would refute the claim and terminate the
hierarchical route.

Simple marginal entropy bounds are insufficient: both marginals have entropy at least their
one-channel minima, but their mutual information can lower the joint entropy. An epsilon-net alone
is also insufficient unless paired with a tail bound strong enough for the full channel-dependent
optimization and with a deterministic inequality identifying the limiting minimum.

## Work record

- 2026-08-29 — registered before a direct proof/counterexample attempt and before commissioning a
  fifth focused external research round.
- 2026-08-29 — round 5 derived deterministic convergence of the defect and the equivalent FCEA
  support-function inequality, but did not determine its value. It also showed that this gate alone
  controls absolute-unbounded rather than full-size extensive amplification.

## Evidence

Source-supported convergence and proposer-side reductions are audited in
`../../notes/chatgpt-four-rounds/round-5-audit.md`. Negative scope evidence for the weaker
convergence theorem is archived in `../../notes/HIERARCHICAL_STRONG_ADDITIVITY_GATE_2026-08-29.md`.

## Adversarial reviews

None yet.

## Open obligations

- Express the exact operator-valued/free-probability limiting support function for `U tensor W_n`.
- Prove product minimization/majorization or produce a fixed `U` with a strict limiting defect.
- Keep `U` fixed as `n->infinity`; a co-varying conjugate subspace is not a counterexample.
- State the probability mode and order of limits.
- If this lemma passes, compose it only to the absolute-unbounded conclusion unless
  `ADDGAP.growing-level-rate` also passes.

## Status history

- 2026-08-29 — created OPEN before proof/counterexample search.
- 2026-08-29 — retained OPEN after round 5; exact FCEA reformulation recorded.

