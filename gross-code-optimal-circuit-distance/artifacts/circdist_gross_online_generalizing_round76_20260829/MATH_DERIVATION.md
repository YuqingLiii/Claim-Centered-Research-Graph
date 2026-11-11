# Mathematical derivation and exact finite certificates

This document exposes the definitions, equations, encodings, selector maps, finite catalogs, DP construction, state transitions, controls, and scope limits needed to audit the result. It does not claim to expose private hidden chain-of-thought.

## 1. Gross incidence and schedule space

Let `G=Z_12 x Z_6`, with `g(i,j)=6i+j`, and

```text
A={(3,0),(0,1),(0,2)},  B={(0,3),(1,0),(2,0)}.
```

For each `g in G`, the X and Z check supports are

`X_g=(g+A) union (72+g+B)` and `Z_g=(g-B) union (72+g-A)`.

There are 72 checks of each type, each weight six, 144 data qubits, 864 uniquely named CNOT edges, and 648 X/Z check pairs of overlap two. The replayer reconstructs `rank(H_X)=rank(H_Z)=66`, commutation, and `k=144-66-66=12`.

A schedule assigns an integer time `t(e) in {0,...,863}` to each edge. The outer formula enforces: all six edges of every check are distinct; all six incident edges of every data qubit are distinct; each overlap pair has the same X-before-Z comparison on both shared qubits; and neither all-X-before-all-Z nor all-Z-before-all-X holds. Relabeling used times in increasing order preserves every equality/order predicate, so post-solve idle compression is lossless.

The exact outer assertion base has 4,398 assertions before installed sound blocks. At iteration `r`, it appends 1,440 reviewed unary blocks, 20 round-62 blocks, every term in the current generalized library, and every current dynamic exact block. Every next solve consumes exactly the state installed by the previous completed transaction.

## 2. Canonical residuals and physical hooks

For an earliest-first order `o=(q0,...,q5)`, the three canonical residual supports and physical suffix supports are

```text
R0={q0,q1},       P0={q2,q3,q4,q5},
R1={q3,q4,q5},    P1={q3,q4,q5},
R2={q4,q5},       P2={q4,q5}.
```

For kind zero, `P0 xor R0` is the complete stabilizer row; kinds one and two are identical. Hence canonical and physical contributions have identical detector syndrome and identical 12-bit logical quotient.

## 3. Complete unrestricted direct formula

Each sector has exactly 360 primary selection variables: 144 singleton data columns plus `72*3=216` residual elementary-fault columns. The reviewed 1,884-word logical pool is not the primary domain.

For primary variables `x_j`, `j=0,...,359`, the query is

`sum_j x_j <= 10`,

`xor_{j : detector bit b of c_j = 1} x_j = 0` for all 72 detector bits, and

`OR_{r=0}^{11} xor_{j : <c_j,L_r>=1} x_j = 1`.

Tseitin chains encode parity and a prefix sequential counter encodes cardinality. There is no pool, hook-count, residual-pattern, logical-weight, or within-check-order-family restriction. Every solver log supplies every variable `1..n` exactly once. The checker evaluates every DIMACS clause, maps selected variables to column records, reconstructs canonical and physical supports, and requires zero syndrome, equal nonzero logical quotient, stabilizer nonmembership, and at most ten faults.

All 48 candidate-sector formulas return SAT and pass this replay. Therefore none licenses direct absence or repair.

## 4. Candidate-exact sound blocks

For a selected residual support `S` in check row `Q`, the preserving atoms are all cross-boundary comparisons `S<O` for prefix kind zero or `O<S` for suffix kinds one/two, where `O=Q\S`. Singleton columns add no schedule atom. If all atoms hold, every selected column and hence its nontrivial zero-syndrome XOR is unchanged. Negating their conjunction is a sound outer exclusion. All 48 source blocks remain installed even when generalized terms cover their source schedules.

## 5. Complete local-order catalogs

For every participating `(sector,check)`, the package materializes all `6!=720` permutations. Every record contains: order ID and qubits; all three canonical residual and physical suffix supports; their exact 84-bit signature (72 syndrome + 12 logical bits); and, where applicable, a constructive unary completion. The checker verifies canonical=physical signature identity for every option. Round 76 contains 271 catalogs and 195120 order records.

## 6. Exact positive pair relations and selectors

For checks `a,b` and local order IDs `i,j`, define

`T_ab(i,j)=U_a(i) OR U_b(j) OR E_ab(i,j)`.

`U` carries an explicit unary selector. `E` is the exact union of stored positive two-hook configurations, each with explicit residual kinds, supports, singleton completion, fault count at most ten, zero syndrome, and nonzero quotient. Every one of the 720 rows is stored as a 720-bit integer, with separate explicit-good-good rows.

A retained pair antecedent induces masks `A,B` and is sound exactly when for every `i in A`, `B subseteq T_ab(i,*)`. Its selector is deterministic: choose the `a` unary witness if available; else the `b` unary witness; else the first stored explicit pair configuration covering `(i,j)`. The replay reconstructs both 144-bit canonical and physical supports for every retained tuple, verifies signature equality and nontriviality, and hashes the complete tuple stream. Exactly 2,637,648 retained pair tuples were literally visited.

Positive-finder misses and zero cells say only that this conservative positive library supplied no selector; they do not prove physical absence.

## 7. Exact multi-check GF(2) universal proof

For a retained fixed-selector mechanism, each constrained check `c` has an allowed local-order mask `A_c`. Every allowed order is materialized with its canonical and physical local contributions and their identical signature `sigma_c(o)`. Let `d` be the signature of fixed singleton data faults. The exact joint DP is

`S_0={d}`,

`S_r={s xor sigma_{c_r}(o) : s in S_{r-1}, o in A_{c_r}}`.

Induction is exact: every transition appends a real allowed local order, and every real allowed prefix has its predecessor and last transition. Merging equal GF(2) signatures loses no acceptance information because terminal validity depends only on the signature. The package records every signature class, allowed-order intersection, layer state count, sorted-state hash, and terminal set. Every terminal has zero syndrome and nonzero logical quotient. Canonical=physical signature identity lifts the conclusion to both supports.

The fixed selector uses the same recorded singleton set and same selected residual kinds for every tuple. Fault count is constant. The domain size is exactly `product_c |A_c|`; the two retained domains total 55,037,740,032 tuples. Stored sample tuples illustrate the construction but carry no universal burden.

## 8. Transaction and semantic state safety

The process order is:

```text
fresh outer build/solve
-> independent outer replay
-> complete Xerr solve
-> complete Zerr solve
-> complete clause/canonical/physical replay
-> append both candidate-exact blocks
-> exact catalogs, relations, raw candidates and deletion controls
-> tentative semantic classification in memory
-> exhaustive retained pair replay / multi universal proof
-> finalized dedup ledger and atomic generalized/registry writes
-> next fresh outer process.
```

No tentative semantic decision mutates installed state. `classification/iteration_state_chain.json` supplies exact before/after hashes for all 24 transitions.

## 9. Deletion controls and limits

Forward and reverse atom deletion is tested against the candidate positive pair relation or fixed-selector DP. A retained atom has an explicit exposed countertuple when removed. This proves only minimality of that named candidate relation/selector. It does not prove that the installed union loses coverage, that no different selector works, global physical-mechanism minimality, or absence.

The 15,874 exploratory round-63 pair clauses are never installed. Weight-12/14 misses, positive-library misses, zero pair cells, and countertuples have zero absence weight. Only checked direct absence in both sectors could license the arbitrary-round repair stage; only a checked repair result could classify that candidate; only proved outer exhaustion could support a universal interleaved ceiling. None occurs here.

## 10. Exact result boundary

The 24 candidates add 48 exact blocks and 303 generalized terms. The unstarted iteration-78 state is `G=5,743`, `D=156`, registry `72`, total `7,359`. There are no candidate-specific Gross UNSAT proofs and no outer proof. Thus `D*_Gross` remains in `{11,12}`; the package is material checked progress, not closure.
