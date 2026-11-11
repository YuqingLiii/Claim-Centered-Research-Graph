# Finite compression and exact CNF equivalence

## Frozen schedule universe

Let `E` be the 864 named Gross CNOT interactions and let a schedule be a map `t:E -> Z_{>=0}`. The frozen base predicate requires:

1. every named edge occurs exactly once;
2. the six edges of each of 72 X ancillas, 72 Z ancillas, and 144 data qubits have pairwise-distinct times;
3. for each of the 648 X/Z check overlaps, the two shared-qubit comparisons agree (MC0);
4. the X and Z families are globally interleaved: neither `xmax<zmin` nor `zmax<xmin`;
5. none of 14,484 exact reviewed block antecedents holds;
6. none of the exact EFSSC validity predicates in the current prefix holds.

All predicates depend on edge times only through equality, strict order, exact minima/maxima, and within-check ranks derived from strict order. No circuit morphing, alternate conflict relation, new generator, added ancilla, or changed terminal residual is present.

## Rank-compression theorem

**Theorem.** The unbounded frozen outer formula is satisfiable if and only if its restriction to edge times in `{0,...,863}` is satisfiable.

**Proof.** Let a legal schedule use distinct time values

`v_0 < v_1 < ... < v_(k-1)`.

There are 864 edges, so `1<=k<=864`. Define `rho(v_i)=i` and `t'(e)=rho(t(e))`. Then `t'(e)` lies in `0..863`. Because `rho` is strictly increasing and injective on the used values, for every edge pair `e,f`:

- `t(e)=t(f)` iff `t'(e)=t'(f)`;
- `t(e)<t(f)` iff `t'(e)<t'(f)`;
- `t(e)>t(f)` iff `t'(e)>t'(f)`.

Endpoint distinctness and conflicts are therefore preserved and reflected. Each MC0 equation equates two strict-comparison truth values, so it is preserved. Minima and maxima map to the ranks of their attaining values, preserving both non-separation inequalities. Every reviewed block is a conjunction of strict precedence atoms and is preserved. Within each six-edge check, the ordered qubit list is unchanged, so each residual rank membership, every detector parity, every logical parity, and every EFSSC validity predicate is unchanged. Thus `t` satisfies the outer predicate exactly when `t'` does.

Conversely, a satisfying schedule already bounded by `0..863` is itself an allowed unbounded schedule. This proves both directions. ∎

Idle layers are removed by the same rank map. The SAT model checker re-ranks every decoded ten-bit model and verifies every relation actually used by blocks, MC0, and EFSSCs.

## Ten-bit representation

Each of 864 edge times and the four words `xmin,xmax,zmin,zmax` is an unsigned ten-bit little-endian word. Ten bits represent `0..1023`; a complete unsigned comparator root enforces `time<864` for each edge.

The circuit compiler gives every Boolean auxiliary a single complete biconditional definition. For literals `a,b` and output `y`:

- `y <-> (a AND b)` is encoded by `(-y OR a)`, `(-y OR b)`, `(y OR -a OR -b)`;
- `y <-> (a OR b)` is encoded by `(y OR -a)`, `(y OR -b)`, `(-y OR a OR b)`;
- `y <-> (a XOR b)` is encoded by the four clauses excluding the unequal truth rows;
- equality is the conjunction of bitwise XNOR values;
- unsigned less-than is a most-significant-prefix recurrence over the ten bits.

Because every definition is biconditional and acyclic, each primary-word assignment has a unique extension to all auxiliary variables. Therefore adding the root unit clauses is equisatisfiable with the source Boolean formula, not merely one-directionally implied by it.

## Source root families and exact count

The base contributes 18,882 **source assertions** before EFSSCs:

- 864 unsigned-nonnegativity assertions, realized by the ten-bit representation and requiring no root clause;
- 864 exact upper-bound assertions `time<864`, one root clause each;
- 288 endpoint-distinctness assertions: 72 X ancillas, 72 Z ancillas, and 144 data qubits. Each expands to `C(6,2)=15` pair roots, for 4,320 root clauses;
- 648 MC0 equivalence assertions. Each expands to two implication roots, for 1,296 root clauses;
- 1,728 extrema-inequality assertions and four attained-equality assertions;
- two global-interleaving assertions;
- 14,484 block-exclusion assertions.

Thus iteration `i` with `s` selectors has `18,882+s` source assertions. Iteration 112 has `18,882+140=19,022`; iteration 124 has `18,882+164=19,046`. At iteration 112 these assertions expand to 22,838 root clauses before the auxiliary-definition clauses; the corresponding count at iteration 124 is 22,862.

For each EFSSC, five comparisons per participating check determine a rank. A 32-row truth table binds membership in the symmetric difference of residual position sets. The selected data and residual qubit signatures are XORed in `F_2^84`; low 72 bits are detector parities and high twelve are logical parities. The root forces the negation of `detectors_zero AND logical_nonzero`. Repeated selected residual kinds are combined by symmetric difference, never set union or integer addition.

The assertion map binds each source assertion to its exact root clause identifiers. The circuit trace records every auxiliary, comparator, equality, rank predicate, and selector-valid literal.

## Independent clause checker

`source/check_outer_encoding.py` is distinct from the compiler. It:

- recomputes semantic source and formula hashes;
- reconstructs the full biconditional clause family of every definition;
- reconstructs every root from the semantic source and assertion map;
- partitions every DIMACS clause exactly once between definitions and roots;
- checks that every nonprimary variable has exactly one definition;
- exhaustively tests all `2^20=1,048,576` pairs of ten-bit inputs for comparator direction;
- exhaustively checks every emitted rank-membership truth-table row against all local orders and qubit signatures;
- rejects first-clause mutation, clause truncation, semantic-source mutation, reversed comparison, and value 864.

All thirteen formulas pass.

## Formula inventory

| iter | selectors | assertions | variables | clauses | memberships | ranks | CNF SHA-256 | disposition |
|---:|---:|---:|---:|---:|---:|---:|---|---|
| 112 | 140 | 19,022 | 398,488 | 1,330,104 | 2,322 | 852 | `a8b917845427a0f746e72200a9a58eb5fac86d5e3c845eeaae69082038c86594` | SAT; complete model replayed |
| 113 | 142 | 19,024 | 398,835 | 1,332,075 | 2,346 | 852 | `5ef9cebd1452c83e0141d8e2071e5ca3438c32ec00edbdf9a59b572811d04567` | SAT; complete model replayed |
| 114 | 144 | 19,026 | 399,047 | 1,333,354 | 2,364 | 852 | `2f7c654737cdd6705fe8f4b1ff42ccd5ac5284bca5405b2d358a0163b705ec34` | SAT; complete model replayed |
| 115 | 146 | 19,028 | 399,332 | 1,335,074 | 2,388 | 852 | `7f6ebb4cb00f41e115ecb5c3ea902c902ebc7b0cf44f6922c71fc24101505004` | SAT; complete model replayed |
| 116 | 148 | 19,030 | 399,493 | 1,336,170 | 2,406 | 852 | `07f4fea846f08a9f5fadeff08eaa96cb50f700fa9321d323ba9708837aaec7f5` | SAT; complete model replayed |
| 117 | 150 | 19,032 | 399,631 | 1,337,002 | 2,418 | 852 | `e4ceca8d60ec2e48d6e85a0753425e6b98939e4335f8a1b31faf28020409ccc4` | SAT; complete model replayed |
| 118 | 152 | 19,034 | 399,854 | 1,338,496 | 2,442 | 852 | `6f625d5663c72691e19ed4360ab39b6da40a3e380382e0444d52a846e6942cec` | SAT; complete model replayed |
| 119 | 154 | 19,036 | 400,034 | 1,339,320 | 2,448 | 852 | `66f8762c2f2bb9a34ca8c262410b26a309b949f327bb98c66e1fe4cdce81ebce` | SAT; complete model replayed |
| 120 | 156 | 19,038 | 400,185 | 1,340,038 | 2,454 | 852 | `372e2798bc2ebac30bc15c7840a000ebb18bbace8cd4ef773d2443e508259507` | SAT; complete model replayed |
| 121 | 158 | 19,040 | 400,401 | 1,341,333 | 2,472 | 852 | `3ff94530aa80001f45b33314a41b8aaba00b0367e29bd638177ac80d99c79cff` | SAT; complete model replayed |
| 122 | 160 | 19,042 | 400,572 | 1,342,461 | 2,490 | 852 | `54945ef5b924dc0f7afbd62644deefc72470022b7da8a3a9ed411da63a0f0df1` | SAT; complete model replayed |
| 123 | 162 | 19,044 | 400,846 | 1,344,143 | 2,514 | 852 | `c22f42e48da3aaeb2556f2979f88566c7a2721649460a1159cd77dd87df0a39c` | SAT; complete model replayed |
| 124 | 164 | 19,046 | 401,040 | 1,345,190 | 2,526 | 858 | `2dd07d33ff0b29c1f06a7452c3b1c7ca9b6df950e819046f8a712dacb0dd7e5a` | checked; deliberately unsolved |

All rows have 11,234 cached comparisons and 1,728 word equalities. Rank-expression count is 852 through iteration 123 and 858 at iteration 124 because the last selector pair introduces previously unseen participating checks. Membership expressions grow from 2,322 to 2,526. The independent rank/order/qubit case count grows from 1,671,840 to 1,818,720.

## Logical interpretation of SAT and UNSAT

For a fixed selector prefix `P`, a satisfying assignment denotes exactly one bounded legal schedule together with the unique auxiliary extension. Decompression gives a legal schedule in the original unbounded universe by the theorem above. The twelve accepted SAT models were checked both at DIMACS level and in two semantic implementations.

An UNSAT refutation of one prefix formula would quantify over **all** frozen schedules and state that every legal schedule satisfies at least one installed sound block or exact EFSSC. No such UNSAT result occurred in Round 90. In particular, SAT-side proof output is not an UNSAT certificate and is never used as one.
