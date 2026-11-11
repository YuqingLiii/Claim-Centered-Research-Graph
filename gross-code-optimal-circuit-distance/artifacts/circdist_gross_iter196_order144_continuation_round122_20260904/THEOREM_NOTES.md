# Round122 theorem and scope notes

## Exact quotient consequence

Let `B196` be the reviewed 3,130,306-variable / 11,477,997-clause base CNF and `Q196` its stabilizer-safe order-144 quotient. The reviewed checker proves `SAT(Q196) iff SAT(B196)` by a byte-exact base prefix and 143 non-strict lex leaders over the complete generalized-dihedral orbit. The observed complete model therefore licenses only `SAT(B196)` plus the independently decoded schedule semantics.

## Direct mechanism criterion

For each error sector, the direct formula contains all 360 physical fault columns. It asserts Hamming weight at most 10, all 72 syndrome parities zero, and a disjunction that at least one of 12 logical pairings is one. A satisfying assignment is independently checked against every clause and reconstructed from all physical columns. Its zero syndrome and nonzero logical pairing prove the net operator is outside the canonical and physical stabilizer spaces.

## Generalized-dihedral closure

Write `q=6i+j`. Translation is `T_(a,b)(q)=6((i+a) mod 12)+((j+b) mod 6)` in each 72-qubit half. The CSS involution swaps sectors and sends coordinates to their negatives. Direct enumeration verifies `D^2=I` and `D T_delta D=T_-delta`. Orbit-stabilizer gives sizes 36,72,36,72: the Xerr mechanism and its dual have stabilizer `{(0,0),(6,0)}`; the Zerr mechanism and its dual are free. Every one of the 288 group-element replays is legal and preserves weight, zero syndrome, and nonstabilizer action; exactly 216 distinct selector keys are installed once.

## Scientific boundary

The candidate is killed. This is material proposer progress, but it is not a distance-12 witness, a universal distance-at-most-11 theorem, root closure, exhaustion, or interval narrowing. `CIRCDIST.gross` and `gap-via-lift` remain CONJECTURED and `D*_Gross` remains `{11,12}`.
