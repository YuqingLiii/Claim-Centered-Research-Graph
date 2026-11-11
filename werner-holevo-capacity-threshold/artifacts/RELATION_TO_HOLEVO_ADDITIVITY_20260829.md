# Why WHGAP is not a Holevo-additivity subproblem

Date: 2026-08-29

## Different operational quantities

The first three projects study classical communication over a quantum channel:

- one-shot Holevo quantity `chi(N)`;
- unassisted classical capacity `C(N)=lim_n chi(N^n)/n`;
- minimum output entropy `S_min`, connected to universal Holevo additivity by Shor's theorem.

WHGAP instead studies:

- coherent information and quantum capacity `Q`;
- private information and private classical capacity `P`;
- degradability, antidegradability and receiver-versus-environment comparison orders.

Entangled inputs appear in both subjects because both require optimization over tensor powers, but
that shared mechanism does not make one problem a special case of the other.

## No direct implication

Shor's additivity equivalence concerns universal statements about `S_min`, `chi`, and entanglement
of formation. It does not include quantum capacity or private capacity. Conversely, an
antidegradability or complete-less-noisy certificate giving `Q=P=0` does not imply `chi=0`,
`C=chi`, or Holevo additivity.

For example, an erasure channel can be antidegradable and have zero quantum/private capacity in
its high-erasure regime while still transmitting nonzero unassisted classical information whenever
the erasure probability is below one. Thus “cannot transmit qubits” is not “cannot transmit
classical bits,” and neither is “the one-shot classical formula is additive.”

## Exact project relationship

The relationship is organizational rather than a reduction:

`tensor-power regularization / entangled inputs`

branches into

1. `chi, C, S_min` additivity and size of classical-capacity advantages; and
2. `Q, P`, coherent/private information and zero-capacity thresholds.

WHGAP is therefore a parallel quantum-channel regularization project. It is not one of the Holevo
equality, prevalence, or extensive-gap subproblems, and none of those three currently closes the
remaining WHGAP strip `[2/5,1/2)`.
