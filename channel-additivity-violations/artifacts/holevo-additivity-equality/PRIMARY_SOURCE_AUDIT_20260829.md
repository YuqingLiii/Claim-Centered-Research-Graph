# Primary-source audit: universal Holevo additivity

Date: 2026-08-29

Scope: bind the three external inputs in `HAEQ.goal` to primary papers and keep their quantifiers
separate. This is a proposer-side source audit, not an independent completion review.

## Source ledger

| Source | Local file | SHA-256 | Relevant location |
|---|---|---|---|
| M. B. Hastings, *Superadditivity of communication capacity using entangled inputs*, arXiv:0809.3972v4 | `primary-sources/hastings-0809.3972.pdf` | `b303560e5794e9b12b7c7f4145b4cd7958a6dd8ab83b61eb7947befca3348b98` | Main text, Theorem 1, PDF p. 2 |
| P. W. Shor, *Equivalence of Additivity Questions in Quantum Information Theory*, arXiv:quant-ph/0305035 | `primary-sources/shor-quant-ph-0305035.pdf` | `300a97664fe8d05531230cd6f3a812b23e2c2cbf22c429436e50442993f415d6` | Theorem 1, PDF pp. 5-6; regularized Holevo formula, PDF p. 3 |
| M. Fukuda and M. M. Wolf, *Simplifying additivity problems using direct sum constructions*, arXiv:0704.1092v2 | `primary-sources/fukuda-wolf-0704.1092.pdf` | `1a8890f8484d450894545190d306efd67b57ee7f646fc45be1e4a26fe6b653b7` | Proposition 1(4), statement on PDF p. 1 and proof on PDF p. 2; Proposition 2(2) and proof, PDF p. 3 |

Online records: <https://arxiv.org/abs/0809.3972>,
<https://arxiv.org/abs/quant-ph/0305035>, and <https://arxiv.org/abs/0704.1092>.

## Hastings quantifiers

Hastings fixes sufficiently large finite integers `D` and then sufficiently large finite `N`.
With nonzero probability, the random-unitary channel `E` and its complex conjugate `Ebar` obey

`S_min(E tensor Ebar) < S_min(E) + S_min(Ebar) = 2 S_min(E)`.

Therefore a deterministic finite-dimensional pair exists. The theorem does **not** say that every
large channel is a counterexample, and it does not supply the same channel as the later Holevo
witness obtained through Shor's global equivalence.

The paper also remarks that a same-channel minimum-output-entropy example can be obtained using
orthogonal rather than unitary matrices, or by adding a classical switch. The present root route
does not need that stronger same-channel MOE observation.

## Shor quantifiers

Shor's Theorem 1 concerns four universal finite-dimensional assertions:

1. minimum-output von Neumann entropy additivity for every channel pair;
2. Holevo quantity additivity for every channel pair;
3. entanglement-of-formation additivity for every state pair; and
4. strong superadditivity of entanglement of formation for every quadripartite state.

They are logically equivalent as universal propositions. Taking the contrapositive after the
Hastings theorem proves existence of at least one finite-dimensional Holevo-nonadditive pair.
This implication is existential: Shor's reductions may change spaces and do not identify that
Holevo pair with Hastings' displayed random pair.

Shor Section 9 supplies a stronger direct route for the implication needed here. After padding the
two outputs to a common dimension and adjoining classical Weyl labels, the extended one-channel
and product Holevo quantities equal the maximal output entropy minus the corresponding MOE.
Subtracting these identities preserves the numerical pair defect exactly. The local specialization
is written in `DIRECT_MOE_TO_HOLEVO_TRANSFER_20260830.md`.

## Fukuda-Wolf quantifiers

For a finite direct sum `T = direct_sum_i T_i`, Proposition 1(4) proves, with base-2 logarithms,

`chi(T) = log_2(sum_i 2^{chi(T_i)})`.

Proposition 2(2) states that Holevo additivity for every arbitrary pair is equivalent to Holevo
self-additivity for every equal pair. The proof expands `(T_1 direct_sum T_2) tensor 2` into four
flagged blocks. The strict existential version needed here follows from the same identity and is
written without an appeal to contradiction in `PAIR_TO_SELF_PROOF_20260829.md`.

## Resulting logic

The strongest local chain is now

`Hastings MOE pair failure`
`=> an exactly equal Holevo pair defect` by Shor's Weyl-labelled extension
`=> some same-channel two-copy Holevo failure` by the direct-sum calculation
`=> C(T) > chi(T)` by the regularized capacity formula.

The older universal-contrapositive chain remains logically valid but is no longer load-bearing.

No step establishes that Hastings' original random channel itself has nonadditive `chi`, and no
step concerns quantum capacity `Q` or private capacity `P`.

## Review status

The exact paper pages and hashes are now bound. Remaining completion gate: an independent reviewer
must check the frozen claim statements, the direct Weyl specialization and the two elementary
regularization/direct-sum derivations against these three files.
