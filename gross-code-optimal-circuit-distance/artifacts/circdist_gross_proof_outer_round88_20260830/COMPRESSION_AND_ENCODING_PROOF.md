# Finite compression and exact CNF equivalence

## Frozen schedule universe

Let `E` be the 864 named Gross CNOT edges.  A schedule is a map `t:E -> Z` in the frozen `S_Gross` semantics.  The formula constrains all edge times to be nonnegative; it depends on those times only through equality, strict order, and extrema defined by equality/order.  This includes the 72 X-check and 72 Z-check six-edge serializations, the 144 data-qubit six-edge serializations, MC0, global interleaving, all 14,484 reviewed order exclusions, and the rank tests used by every EFSSC.

No circuit morphing, alternate conflict model, new check generator, flag, cat state, or changed terminal-residual convention is present in this package.

## Compression lemma

For any legal schedule `t`, list its distinct used values in increasing order

`v_0 < v_1 < ... < v_(k-1)`.

Define `rho(v_i)=i` and `t'(e)=rho(t(e))`.  Since there are 864 edges, `1 <= k <= 864`, hence every compressed time lies in the exact safe interval `0..863`.

For every pair of edges `e,f`:

- `t(e)=t(f)` iff `t'(e)=t'(f)`;
- `t(e)<t(f)` iff `t'(e)<t'(f)`;
- `t(e)>t(f)` iff `t'(e)>t'(f)`.

The proof is immediate because `rho` is injective and strictly increasing on the finite set of used times.  Every strict serialization and reviewed block is a Boolean combination of these pair relations, so its truth is unchanged.  Each MC0 constraint compares the same two strict-order bits before and after compression.  Minima and maxima map to their ranks, so both global-interleaving inequalities are unchanged.  Within-check order positions are unchanged; therefore every residual-position membership, 72 detector parities, 12 logical parities, and EFSSC validity bit is unchanged.  The frozen terminal residual convention consequently remains unchanged.

Thus every unbounded legal schedule has a bounded representative in `0..863` satisfying exactly the same outer formula.  Conversely, a bounded assignment satisfying that formula is already a legal schedule in the original unbounded universe.  Inclusion supplies this reverse direction.  Therefore the unbounded and bounded outer formulas are equisatisfiable, and a bounded model maps directly to a frozen schedule.

## Boolean representation

Each of the 864 edge times is a ten-bit unsigned little-endian word.  Ten bits can express `0..1023`; an exact comparator root enforces `t<864` for every edge.  Four additional ten-bit words represent `xmin`, `xmax`, `zmin`, and `zmax`.

The compiler emits a Tseitin CNF with a unique definitional extension of every primary-word assignment.  `and`, `or`, and `xor` gates use their full biconditional clause sets.  Word equality is a conjunction of bitwise XNORs.  Unsigned less-than is the standard most-significant-prefix recurrence, implemented over little-endian inputs by iterating from low to high while updating the prefix result.  Every cached relation is bound in the circuit trace.

The source-root families are:

1. 864 unsigned nonnegativity assertions, implicit in the representation, and 864 explicit `t<864` roots.
2. 288 six-way `Distinct` assertions expanded to 4,320 pair clauses: 72 X ancillas, 72 Z ancillas, and 144 data qubits.  Each pair clause is `(a<b) or (b<a)`.
3. 648 MC0 equivalences, each encoded by the two clauses for equality of the two relevant comparison bits, for 1,296 roots.
4. Four exact extrema: 1,728 bound roots plus four attained-equality disjunctions.  The two global-interleaving roots enforce `xmax>=zmin` and `zmax>=xmin`.
5. The exact reviewed exclusions: 1,440 unary, 20 Round62, 12,820 generalized, and 204 dynamic blocks.  Each root is the disjunction negating every strict-order atom of its source block.
6. One root per EFSSC.  For each fixed weight-10 mechanism, five within-check comparisons determine a rank.  A 32-row truth table defines membership in the selector's symmetric-difference residual-position set.  Those membership bits reconstruct all 84 parity coordinates.  The excluded validity expression is `detectors_zero AND logical_nonzero`, with a root unit clause forcing its negation.  Tuple sums are never treated as union sizes.

The assertion map records every source assertion and all of its root clause identifiers.  The circuit trace records every auxiliary definition, comparator, equality, rank membership, and selector-valid literal.

## Independent checker

`source/check_outer_encoding.py` does not invoke the compiler.  It:

- recomputes the semantic source hash and all formula-file hashes;
- reconstructs every definition's complete biconditional clause family;
- reconstructs every source root from the source object and assertion map;
- partitions every DIMACS clause exactly once between definitions and roots;
- proves that every nonprimary variable has exactly one definition;
- exhaustively checks all `2^20 = 1,048,576` pairs of ten-bit inputs for comparator direction;
- exhaustively checks every emitted rank-membership truth-table case against the frozen within-check order and qubit interpretation;
- rejects a first-clause mutation, truncation, a semantic-source mutation, reversed comparator direction, and the out-of-bound value 864.

Iteration 109 checks 1,637,280 rank/order/qubit cases; iterations 110, 111, and 112 check 1,645,920, 1,654,560, and 1,671,840 cases respectively.  All four checks pass.

## Formula inventory

| iteration | selectors | assertions | variables | clauses | CNF SHA-256 |
|---:|---:|---:|---:|---:|---|
| 109 | 134 | 19,016 | 397,902 | 1,326,596 | `536c348ede8409ca5d691091213acbada828934a6be641da0fd3a80a62c9292f` |
| 110 | 136 | 19,018 | 398,070 | 1,327,548 | `932c4b0f31bb010950bc9999269983c79bba4c3941b883031ca3c14693f8946d` |
| 111 | 138 | 19,020 | 398,235 | 1,328,487 | `f0255ef2232c572ae6cc0aa3a50ec76a7b5bef4a13fbc42ad1f342ecf6e5a8f0` |
| 112 | 140 | 19,022 | 398,488 | 1,330,104 | `a8b917845427a0f746e72200a9a58eb5fac86d5e3c845eeaae69082038c86594` |

Every row has 11,234 distinct cached comparisons, 1,728 word equalities, and 852 rank expressions.  Membership-expression counts are 2,274, 2,286, 2,298, and 2,322.  Iteration 112 is a fresh, independently checked formula and was not submitted to a SAT solver.

## Logical scope of SAT and UNSAT evidence

The three accepted outer results are SAT.  Their complete DIMACS assignments are clause-replayed and decoded to all 864 times, then independently audited in the frozen model.  A SAT solver trace is not an UNSAT certificate and is not used as one.

The package also validates the DRAT-to-LRAT tool chain on a separate pigeonhole control: valid DRAT is accepted, generated LRAT is accepted, and corrupt/truncated DRAT and LRAT are rejected.  This is only a checker control.  It proves no Gross absence statement because no Gross formula in this package returned UNSAT.
