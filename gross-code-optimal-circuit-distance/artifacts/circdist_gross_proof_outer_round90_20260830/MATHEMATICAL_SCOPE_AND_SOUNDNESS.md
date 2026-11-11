# Mathematical scope, soundness, and distance convention

## Frozen objects

The code is the fixed Gross CSS code `[[144,12,12]]` with the frozen 72 X checks and 72 Z checks, each of weight six. A schedule assigns one execution time to each of the 864 named CNOTs. It lies in `S_Gross` exactly when each interaction occurs once, each ancilla/data endpoint is serial, all 648 MC0 relations hold, empty layers are compressed, and the X/Z families satisfy the frozen global-interleaving requirement. The package excludes flags, cat states, generator changes, endpoint morphing, alternative conflict graphs, and Circ-Preserve substitutions.

There are two CSS error sectors. `Xerr` hooks are produced by X-check CNOT orders and tested against Z detectors; `Zerr` hooks are produced by Z-check CNOT orders and tested against X detectors. Every result is required in both sectors; evidence from one is never silently transferred to the other.

## Distance definitions and the off-by-one boundary

The frozen problem defines

`d_eff(M) := d_ext(E(M))`

from terminal residual/hook columns, and

`d_circ(C) := min { |F| : F triggers no detector and flips a nontrivial logical }`

for the full spacetime detector circuit. Under the fixed memory experiment, elementary-fault weight, and ideal final-readout boundary,

`d_eff(M) <= d_circ(C(M)) <= d = 12`.

The optimization target is

`D*_Gross := max_(M in S_Gross) d_circ(C(M))`.

The certified achievable floor already in the canonical node and the code-distance ceiling reduce the root residual to `{11,12}`. Round 90 does not alter either bound.

A terminal effective witness of weight `w<=10` establishes `d_eff(M)<=w`. Because the frozen inequality points from `d_eff` **up** to `d_circ`, it does not by itself establish `d_circ(C(M))<=w`. Full circuit closure may require additional faults, and proving a ceiling of eleven requires the licensed arbitrary-round repair/completion argument. Round 90 never enters that argument because every direct query is SAT, not absent. This is the precise reason there is no off-by-one promotion from a direct weight-10 or weight-9 witness.

## Direct-360 universe

Fix a schedule and a sector. Let `H_opp` be the 72 opposite-sector detector rows, `S_same` the same-sector stabilizer span, and `lambda_0,...,lambda_11` a logical-dual basis. The 360 exact columns are:

- data singleton `D:q`, one for each `q in {0,...,143}`;
- residual `R:c:k`, one for each check `c in {0,...,71}` and kind `k in {0,1,2}`.

For the six qubits in a check's earliest-to-latest order `o=(q_0,...,q_5)`, canonical residual supports are

`R_0={q_0,q_1}`, `R_1={q_3,q_4,q_5}`, `R_2={q_4,q_5}`.

For a selected column set `J`, define its canonical net support

`e(J) = XOR_(j in J) support(j)`.

The complete direct query is

`exists J subseteq {0,...,359}: |J|<=10 AND H_opp e(J)=0 AND (exists r) <e(J),lambda_r>=1`.

The twelve logical parities form a complete quotient coordinate system modulo `S_same`, so the last disjunction is equivalent to `e(J)` being nontrivial modulo the stabilizer span after zero syndrome. The CNF contains a primary variable for every column, full XOR equivalences for 72 detector rows and twelve logical rows, one nonzero-logical disjunction, and an exact prefix-threshold encoding of `sum x_j<=10`. No candidate pool, residual family, check count, or local-order pattern is omitted.

**Direct SAT theorem.** A satisfying direct CNF assignment exists if and only if the fixed schedule has a named terminal effective logical using at most ten distinct elementary columns in that sector.

**Proof.** In the forward direction, take the true primary variables. The detector XOR unit clauses give zero syndrome; the logical-output equivalences and disjunction give a nonzero logical coordinate; the prefix recurrence gives at most ten selected columns. In the reverse direction, set precisely the witness's primary variables. Each biconditional XOR chain has its unique parity extension, the nonzero logical disjunction is true, and the exact cardinality recurrence has its unique satisfying extension. ∎

All 24 Round90 formulas are SAT and all assignments satisfy every clause.

## Canonical-to-physical replay theorem

The actual physical suffix supports for the three residual kinds are

`P_0={q_2,q_3,q_4,q_5}`, `P_1={q_3,q_4,q_5}`, `P_2={q_4,q_5}`.

For kinds 1 and 2, `P_k=R_k`. For kind 0,

`P_0 XOR R_0 = {q_0,q_1,q_2,q_3,q_4,q_5}`,

which is the full generating stabilizer row for check `c`. For any selected set, replacing each canonical residual by its physical suffix therefore changes the aggregate data operator by a sum of stabilizers. The opposite detector syndrome and all logical-dual parities are invariant. Data singletons are identical physically and canonically.

The physical replay sorts the six named CNOTs by their recorded times, constructs every physical suffix, XORs them with all selected data singletons, recomputes the 72-bit syndrome, tests stabilizer membership, and recomputes all twelve logical parities. For every Round90 mechanism, syndrome is empty, the logical class is nontrivial, and physical/canonical parities agree.

This theorem establishes faithful terminal-residual semantics. It does not claim an arbitrary-round spacetime closure of the same weight.

## Order-block and EFSSC soundness

Each inherited order block is a finite conjunction `B_j(t)` of strict comparisons. Its reviewed soundness theorem supplies a concrete terminal effective mechanism whenever `B_j(t)` holds. Excluding `B_j` therefore removes only schedules already killed by that mechanism on the licensed search route.

An EFSSC fixes named direct columns rather than one comparison cube. Its exact validity predicate `V_s(t)` recomputes the selector's entire detector/logical signature from the within-check ranks at schedule `t`. The theorem proved in `EFSSC_SOUNDNESS_AND_ATOMICITY.md` is

`V_s(t) <-> (the same named selection s is a terminal effective logical of weight <=10 on t)`.

Thus `NOT V_s(t)` is domain-wide sound. It never asserts absence of any unselected mechanism.

## Exact quantified content of the outer formula

For selector prefix `P`, the formula is

`exists t in S_Gross: [for all j, NOT B_j(t)] AND [for all s in P, NOT V_s(t)]`.

SAT supplies one legal schedule outside the installed killed domains. UNSAT would supply, after a valid formula refutation and the soundness theorem for every installed predicate, the universal statement

`for all t in S_Gross: (exists j, B_j(t)) OR (exists s in P, V_s(t))`.

That would be a universal terminal-effective cover by the installed mechanisms. Round 90 has no such refutation. Moreover, this package makes no independent new claim that terminal-effective cover alone is a full `d_circ<=11` proof; any root promotion would also have to discharge the completion/repair implication under the frozen convention and combine it with the certified floor.

## Round90 implication

The actual disposition is existential in every iteration: twelve legal schedules survived the then-current prefix, and each was subsequently shown to have positive mechanisms in both direct sectors. This certifies twelve sound CEGAR transitions and 24 exact new selector domains. It does not quantify over the schedules that remain after iteration 123. Therefore the correct theorem-level verdict is `MATERIAL-CHECKED-PROGRESS-NOT-CLOSED`, with `D*_Gross in {11,12}` unchanged.
