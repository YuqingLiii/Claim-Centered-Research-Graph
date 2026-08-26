# External primitives used by KSUM.B4a

These entries identify the external guarantees used in Section 3 of
[`ksum_B4_upper_note_v2.md`](ksum_B4_upper_note_v2.md). They do not attribute the
whole recursive algorithm or its worst-case cap to the cited papers.

## Search and counting

Gilles Brassard, Peter Hoyer, Michele Mosca, and Alain Tapp,
*Quantum Amplitude Amplification and Estimation*, arXiv:quant-ph/0005055v1
(2000; published 2002): [source](https://arxiv.org/abs/quant-ph/0005055v1).
Section 2 supplies amplitude amplification and search. Sections 4 and Appendix A,
Theorems 12, 13, and 15, supply amplitude estimation and approximate counting.
For a Boolean oracle on s positions with b>0 marked items, Theorem 15 gives
relative-error estimation with constant success probability and expected
O(epsilon^-1 sqrt(s/b)) queries; at b=0 it returns zero using O(sqrt(s)) queries.
The fixed budget, failure handling, amplification, and use inside the recursive
2-Sum algorithm are local adaptations, not additional guarantees of Theorem 15.

## Minimum finding

Christoph Durr and Peter Hoyer, *A Quantum Algorithm for Finding the Minimum*,
arXiv:quant-ph/9607014v2 (1996):
[source](https://arxiv.org/abs/quant-ph/9607014v2).
The algorithm finds a minimum of an s-item oracle table in O(sqrt(s)) queries
with bounded error; repetition improves success probability. Applying it to
the earliest marked position in a fixed prefix is a local reduction. Verification,
the no-marked-item outcome, and a worst-case truncation rule remain obligations
of the B4a proof, not claims that the source proves the full recursive algorithm.

## Coherent composition model fact

Input-independent reversible computation, stored-value comparisons, and their
inverses carry no input-query cost. For unitary operators U_i and V_i with
||U_i-V_i|| <= eta_i on the relevant full spaces, a telescoping expansion and
unitary norm invariance give

    ||U_M ... U_1 - V_M ... V_1|| <= sum_i eta_i.

Thus M coherent oracle replacements of operator error at most delta/M contribute
at most delta total operator error. Establishing that bound for the amplified
compute-copy-uncompute implementation, including its workspace, remains part
of the local proof. A scalar success probability alone does not supply it.

## Subset-finding base

The separate [Childs--Eisenberg source record](reference_childs_eisenberg_2005_subset_finding.md)
identifies the range-independent O(s^(2/3)) two-item subset-finding guarantee.
The predicate here enforces distinct indices and checks their sum using stored
values, so marking needs no additional input queries.
