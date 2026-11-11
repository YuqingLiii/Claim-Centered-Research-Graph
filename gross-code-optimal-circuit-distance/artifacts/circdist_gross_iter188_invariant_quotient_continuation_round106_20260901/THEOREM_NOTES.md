# Public theorem notes and checked derivations

## Definitions

Let `E` be the 864 required CNOT edges in the frozen Gross syndrome-extraction geometry. A schedule is a function `t:E -> {0,...,1023}`. The base encoding requires each edge exactly once, prevents a data or check ancilla from participating in two gates at one time, enforces the MC orientation constraint on all 648 X/Z overlaps, attains all four extrema, and requires global X/Z interleaving. Its definitions are equivalences, so a primary schedule has at most one extension to the auxiliary variables.

For sector `sigma`, a direct column `c` carries a canonical data mask `p_c`, a physical suffix mask `p'_c`, a detector syndrome `h_c`, and detector-frame options `u_c`. A selected distinct-name set `A` is a physical failure when

1. `|A| <= 10`;
2. `xor_{c in A} h_c = 0`, after the encoded detector-frame choices;
3. `xor_{c in A} p_c` has a nonzero logical parity;
4. direct physical replay gives `xor_{c in A} p'_c` with the same logical parities and zero syndrome.

The complete direct formulas quantify all 360 columns and impose no pool, residual-pattern, check-count, or within-check-order restriction.

## Lemma 1: exact iteration-188 source/CNF correspondence

The retained source checker assigns every DIMACS clause ID exactly once, regenerates all 1,833,076 definition records, and reconstructs every source root. Every variable is either a primary schedule/extremum bit or the output of one unique acyclic definition. Therefore projection from a satisfying CNF assignment to the schedule variables is sound, and every satisfying source schedule has one definitional CNF extension.

## Lemma 2: translation quotient equisatisfiability

The concrete action of `G = Z_12 x Z_6` is a permutation of checks, qubits, 864 edges, overlap pairs, stabilizer rows, detector rows, logical classes, and all 360 direct columns in each sector. The full iteration-188 registry is closed under `G`.

For every schedule orbit, choose a least ten-bit edge-time vector. It satisfies all 71 nonidentity lex constraints. Conversely, every quotient model is a base model. The recurrence relation implementing each lex constraint is functional and its full four-variable truth table is checked. Hence the quotient and base are equisatisfiable, with a unique quotient-variable extension for each base assignment satisfying the lex roots.

## Theorem 3: concrete checked SAT candidate

The retained assignment satisfies all 11,798,572 clauses. Projection and physical replay yield a legal globally interleaved schedule with all 864 edges, 511 used layers, zero conflicts, and zero MC violations. This is a finite certificate for existence of one base/quotient model. It makes no universal distance statement.

## Theorem 4: both direct sectors refute this candidate as a distance-12 witness

The Xerr and Zerr complete formulas are SAT. Independent reconstruction checks every clause and yields ten distinct named faults in each sector. Canonical and physical masks have zero detector syndrome, equal nonzero logical parities, and are outside the appropriate stabilizer span. Therefore both sectors contain a physical failure of weight 10, so the candidate circuit has effective distance at most 10 under the checked direct model and cannot certify distance 12.

This theorem is candidate-specific. It does not prove a universal ceiling over every legal schedule.

## Lemma 5: selector soundness

For either parent mechanism, let `P(t)` be the conjunction of strict comparisons that fixes the within-check orders needed for its residual columns. Direct column semantics depend only on those orders. The checked named set remains a weight-10, zero-syndrome, nontrivial physical mechanism for every legal schedule satisfying `P`. Consequently `not P` is a sound selector clause.

For every `delta in G`, the translated schedule is legal, the translated selected names remain distinct, and the translated physical replay has the same weight, zero syndrome, and nontrivial class. Thus every translated selector is sound on its translated schedule cell.

## Lemma 6: exact orbit and invariant-registry accounting

The normalized selector key is `(sector, sorted data support, sorted (check,kinds) groups)`. Both parent keys have orbit size 72. Their 144 translates are pairwise new: zero existing-key collisions, zero cross-parent collisions, and zero semantic-hash collisions. The selector count increases from 24,156 to 24,300.

The independent checker verifies closure of all 517,140 blocks and 24,300 selectors under generators `(1,0)` and `(0,1)`. These generators span `G`, so the full iteration-189 registry is invariant under all 72 translations.

## Theorem 7: exact fresh iteration-189 continuation

The iteration-189 source is the iteration-188 source with exactly the 144 sound translated selectors appended; block semantics and all fixed geometry fields are unchanged. The source-to-base checker reconstructs all 6,909,336 clauses, and the quotient checker reconstructs its complete 4,907,591-clause suffix. The resulting quotient has 2,460,741 variables and 11,816,927 clauses and SHA-256 `3ece12a1ea0ee6502982fecfcaf75debae985ea2ddff93ea3b875552c0714df7`.

Its state is fresh and unstarted. Therefore it is a sound strict continuation frontier. No root branch follows from freshness or from positive SAT evidence.

## Root-credit corollary

The explicit distance-12 branch is not proved because the only new circuit candidate has a checked failure in each sector. The universal `D* <= 11` branch is not proved because the checked quotient is SAT and there is no Gross UNSAT certificate. Hence `CIRCDIST.gross` and `gap-via-lift` remain `CONJECTURED`, with the exact residual `D*_Gross in {11,12}`.

## Counterexample and control attempts

- First-clause mutation, CNF truncation, semantic-source mutation, comparator reversal, and out-of-bound time controls are rejected by the base checker.
- Flipping one selected direct primary variable makes each complete direct assignment fail clauses.
- Valid DRAT and generated LRAT controls are accepted; corrupt and truncated variants are rejected.
- Every SAT trace has zero complete empty-clause records and is expressly denied UNSAT-proof status.
- Registry globalization was attempted only after complete generator closure and all 144 translated physical replays passed.
