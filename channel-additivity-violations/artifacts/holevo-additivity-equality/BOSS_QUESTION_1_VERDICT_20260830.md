# Boss question 1: does the Holevo additivity equality hold?

Date: 2026-08-30

## Frozen question

For finite-dimensional quantum channels `N,M`, is

\[
 \chi(N\otimes M)=\chi(N)+\chi(M)
\]

always true? Equivalently at the universal-statement level, can entangled codewords across channel
uses ever improve unassisted classical communication?

This is a **classical-capacity question for quantum channels**. It is not the quantum capacity
`Q` or private capacity `P`. Entanglement appears because the encodings across several quantum
channel uses may be entangled.

## Current verdict

No. Universal additivity is false. The source-bound logic is:

1. Hastings gives a finite-dimensional minimum-output-von-Neumann-entropy counterexample.
2. Shor's explicit Weyl-labelled extension transfers that pair defect exactly to a Holevo pair
   defect, while changing the channels. His universal equivalence gives the same existential
   conclusion but is no longer needed as the load-bearing step.
3. The Fukuda--Wolf classical-flag direct sum converts a pair violation into one finite channel
   `T` satisfying `chi(T tensor T)>2chi(T)`.
4. Therefore `C(T)>chi(T)` for that fixed channel.

This does not say every channel violates additivity. Entanglement-breaking channels are a strongly
additive class.

## Claim-library status

The exact chain has now passed hash-bound independent review. Canonical nodes
`HAEQ.hastings-moe-counterexample`, `HAEQ.weyl-extension-moe-preservation`,
`HAEQ.direct-moe-to-holevo-transfer`, `HAEQ.pair-to-self-reduction`,
`HAEQ.fixed-channel-regularization`, and the root `HAEQ.goal` are `PROVED` at their scoped claims.
This completion concerns universal one-shot Holevo additivity and its fixed-channel regularization
consequence only; it does not identify the original Hastings random channel as the final Holevo
witness.
