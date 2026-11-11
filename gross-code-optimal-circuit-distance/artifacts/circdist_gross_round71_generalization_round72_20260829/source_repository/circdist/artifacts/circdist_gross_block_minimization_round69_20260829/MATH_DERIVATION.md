# Mathematical derivation and soundness argument

## 1. Frozen objects

The frozen Gross instance has 144 data qubits, 72 X checks, and 72 Z checks. Every check has weight six. Each data qubit is incident to three X-check edges and three Z-check edges, hence the scheduling graph contains

\[
72\cdot 6 + 72\cdot 6 = 864
\]

named CNOT edges. Each nonempty X/Z check overlap has size two; the frozen incidence tables contain 648 such overlaps. The MC constraint for overlap `(a,b,{q0,q1})` is

\[
[t(Z,b,q_0)<t(X,a,q_0)] = [t(Z,b,q_1)<t(X,a,q_1)].
\]

Each ancilla's six incident edge times are distinct, each data qubit's six incident edge times are distinct, all times are nonnegative and bounded by 863 before idle compression, and the schedule must not put all X edges strictly before all Z edges or vice versa.

For either error sector, the frozen direct model contains 360 columns:

- 144 data singleton columns `D:q`;
- three residual columns for each of 72 same-sector checks, for 216 residual columns.

For a local order `o=(o0,…,o5)`, the canonical residual position sets are

\[
P_0=(0,1),\qquad P_1=(3,4,5),\qquad P_2=(4,5),
\]

and the physical suffix position sets are

\[
\widehat P_0=(2,3,4,5),\qquad \widehat P_1=(3,4,5),\qquad \widehat P_2=(4,5).
\]

Only kind 0 differs between canonical and physical support. Their symmetric difference is the full weight-six check stabilizer, so opposite-check syndrome and logical quotient agree. The verifier checks that equality for every local order and every kind.

## 2. Why weights 12 and 14 suffice for one/two-residual mechanisms

A selected direct mechanism of at most ten columns with two residual columns has at most eight data singleton columns. Each canonical residual has support size at most three. Therefore the canonical net support has weight at most

\[
3+3+8=14.
\]

A nontrivial zero-syndrome support in the frozen sector has weight at least 12. It also has even weight: summing all opposite-sector parity checks counts every data coordinate three times, so the total support parity is zero. Thus a nontrivial net support of weight at most 14 must have weight 12 or 14.

Let residual supports be `r1,r2` and let `V` be a zero-syndrome nontrivial logical support. The required singleton set is fixed:

\[
D=V\triangle r_1\triangle r_2,
\]

and the direct fault count is

\[
2+|D|.
\]

The mechanism is retained exactly when this count is at most ten and the physical suffix replacement has the same zero syndrome and nonzero logical quotient. For a one-residual mechanism the corresponding count is `1+|V△r|`; the inherited round-63 unary clauses cover the qualifying cases. In the participating catalogs, precisely 360 of 720 orders per check have the kind-1 three-suffix contained in a frozen weight-12 logical support, yielding `1+(12-3)=10` faults.

For weight 12, all 1,884 members of the appropriate frozen logical pool are checked. For weight 14, a ten-fault completion requires two disjoint size-three residuals and eight singletons. The individual incremental queries checked 1,800 Xerr and 925 Zerr residual unions. Fifteen Xerr and six Zerr queries produced raw weight-14 completions. Only these 21 SAT completions are load-bearing.

The remaining 2,704 solver returns were UNSAT observations without independently checked DRAT/LRAT proofs. They are recorded but never used to establish absence or soundness.

## 3. Local-order catalog

For each sector/check pair used by a round-68 mechanism, all 720 permutations of the check's six fixed qubits are generated. Each catalog row records:

1. the ordered six qubits;
2. canonical and physical support for residual kinds 0, 1, and 2;
3. the opposite-check syndrome of each canonical support;
4. its logical quotient against the twelve frozen logical duals;
5. the unary-good/unary-bad classification;
6. for a unary-bad order, the weight-12 logical support and nine singleton columns completing the residual to a ten-fault mechanism.

There are 23 such catalogs and 16,560 order records. The independent verifier regenerates each permutation from the fixed row, recomputes all supports, syndromes, quotients, and unary mechanisms, and obtains exactly 360 unary-good and 360 unary-bad orders in every catalog.

## 4. Factorized pair relation

The twelve source blocks use 30 unique unordered pairs of participating checks. A pair `(a,b)` has a 720×720 relation. A cell `(oa,ob)` is in the conservative certified relation if one of the following holds:

- `oa` has an inherited unary mechanism;
- `ob` has an inherited unary mechanism;
- some residual kind/support from `oa` and some residual kind/support from `ob` matches an explicit positive configuration in the pair ledger.

The third case has an explicit tuple

\[
(k_a,r_a,k_b,r_b,V,D)
\]

with `r_a△r_b△D=V`, direct fault count at most ten, zero opposite syndrome, nontrivial logical quotient, and physical suffix replay equal in syndrome and quotient. The verifier assigns a concrete configuration index to each certified good-good cell. It assigns 1,197,120 witnesses and seals the deterministic selector stream with SHA-256

```text
bf023520379991fa597fba786d0505ccd71c85bd1f89f957298cefbbc65cdaed
```

This is an explicit reconstruction rule, not candidate agreement: given a covered pair of order IDs, scan the listed residual options in kind order and select the first matching positive configuration. The configuration contains `V`, all singleton columns, logical parities, and source (`weight12_pool` or `weight14_direct`), enough to rebuild the physical mechanism from the frozen model.

The primary Xerr source involves six checks, whose naive Cartesian space is `720^6`; primary Zerr involves four checks, with `720^4`. Soundness of each emitted clause depends on one unary catalog or one pair relation, so the exact positive region factors over 30 matrices of 518,400 cells. No sample substitutes for an unvisited Cartesian tuple.

## 5. Comparison-term representation

For a check `a`, a comparison atom is `t(edge_a(q)) < t(edge_a(r))`. A conjunction of atoms defines a subset `A` of the 720 local orders; a second conjunction defines `B` for check `b`. The conjunction is licensed only if

\[
A\times B \subseteq R_{a,b},
\]

where `R_{a,b}` is the conservative certified relation above. The outer block is the negation of that conjunction.

Starting from each explicit residual configuration, atoms that are unnecessary for the rectangle inclusion are deleted in forward and reverse orders. Duplicate terms are merged. Terms that cover no unary-good × unary-good cell are discarded. The retained representation contains 4,740 terms:

| atoms | terms |
|---:|---:|
| 4 | 8 |
| 6 | 52 |
| 7 | 1,088 |
| 8 | 1,416 |
| 9 | 1,092 |
| 10 | 920 |
| 11 | 104 |
| 12 | 60 |

The mean is 8.4768 atoms and the median is 8. Every generalized term is shorter than the 16-atom continuation source blocks; the mean antecedent is 47.0% shorter than 16 atoms. This is not a total-CNF reduction: twelve exact source blocks become 4,740 sound region clauses. The gain is coverage and shorter local antecedents, not fewer clauses.

For every atom of every term, deleting that atom exposes a concrete pair of local order IDs satisfying all remaining atoms but lying outside the retained positive relation. There are 40,180 such controls. They prove deletion-minimality with respect to this library. Because the negative side lacks proof-logged global classification, they do not prove that an exposed tuple has no different mechanism.

## 6. Physical replay

For every positive configuration, the verifier constructs canonical net support

\[
V=r_a\triangle r_b\triangle D
\]

and physical net support

\[
\widehat V=\widehat r_a\triangle\widehat r_b\triangle D.
\]

It checks both opposite syndromes are zero; `V` is not in the same-sector stabilizer span; at least one logical parity is one; and canonical and physical logical-parity vectors agree. This yields 3,368 direct physical replays before any outer candidate is considered.

For each CEGAR SAT assignment, replay is stricter: all selected columns are reconstructed from that candidate's actual local orders; every selected physical suffix is matched to its ordered edge list and times; all DIMACS clauses are evaluated under the complete assignment; canonical and physical nets are recomputed; zero syndrome and nontrivial quotient are rechecked; and the exact comparison block is derived from the selected columns.

## 7. Soundness theorem used by the outer model

For a retained term `T`, every schedule satisfying all comparisons in `T` induces a local-order tuple in its rectangle. Rectangle inclusion supplies an inherited unary witness or an explicit two-residual witness. All direct columns in that witness depend only on those local orders, and the physical replay proves zero syndrome and nontrivial logical quotient with at most ten faults. Therefore any schedule satisfying `T` has a direct-360 mechanism and cannot be a distance-at-least-11 candidate. Adding `¬T` to the outer model is sound.

This theorem uses only positive witnesses. Negative weight-14 outcomes, deletion-control exposed tuples, candidate agreement, and positive-only solver failure are absent from its premises.
