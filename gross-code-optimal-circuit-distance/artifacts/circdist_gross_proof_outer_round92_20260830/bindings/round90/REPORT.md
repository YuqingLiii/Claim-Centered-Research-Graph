MATERIAL-CHECKED-PROGRESS-NOT-CLOSED

# CIRCDIST.gross proof-producing outer continuation — Round 90

Date: 2026-08-30  
Scope: frozen `S_Gross` only  
Canonical claim SHA-256: `fc22f602b9bfd9e38fa69d7fc1d00b973c7a634e6c400662eaccd38c8ec0f180`

## Verdict and exact mathematical consequence

Round 90 does **not** prove `D*_Gross=11` and does **not** prove `D*_Gross=12`. The exact certified residual remains

`D*_Gross in {11,12}`.

The root `CIRCDIST.gross` and its live `gap-via-lift` route remain `CONJECTURED`. The material result is a strict-serial proof-producing continuation through twelve complete candidates, iterations 112–123. Every outer formula was SAT; every complete assignment satisfies every DIMACS clause and decodes to a legal, globally interleaved frozen schedule. Both complete unrestricted direct-360 sectors were SAT for every candidate. All 24 assignments were clause checked and physically replayed, yielding 22 weight-10 and two weight-9 terminal effective mechanisms. Each pair of exact fixed-selector semantic cuts (EFSSCs) was committed only after both direct replays passed.

The fresh continuation is iteration 124, `started:false`, with 164 selectors and no iteration-124 solver disposition. Its independently checked CNF has 19,046 assertions, 401,040 variables, 1,345,190 clauses, and SHA-256 `2dd07d33ff0b29c1f06a7452c3b1c7ca9b6df950e819046f8a712dacb0dd7e5a`.

No Gross outer UNSAT, direct-sector absence, LRAT/DRAT refutation of a Gross formula, arbitrary-round repair entry, outer exhaustion, distance-12 schedule, or universal distance-11 ceiling is claimed.

## Exact authorization and immutable bindings

Round 90 was authorized and pending in the scheduler at budget 115/116 and score `0.042669456318784105`. The following protected files were read before solving and remained read-only:

| input | bytes | LF lines | SHA-256 |
|---|---:|---:|---|
| `operations/circdist/SCHEDULER.yaml` | 222,063 | 2,737 | `adc03e56e36656dec95a82cc8e14b9e3c0559fc9af3f8ae42c01b03da57f2d61` |
| `circdist/proof-dag/nodes/CIRCDIST.gross.yaml` | 61,309 | 728 | `d3629fef2b325e3a41c39a2fea774391d99c9ff90ca9014f011a0bfa7a7118f5` |
| `circdist/reviews/circdist_gross_proof_outer_exact_review_round89_20260830.md` | 105,623 | 1,369 | `95f830f41a51bff2f0f72967a48984f496981aac89f49b6b9f95f2a4a34d77a8` |
| `circdist/artifacts/circdist_gross_proof_outer_round88_20260830/SHA256SUMS.txt` | 27,710 | 256 | `c4061caff46b632b5c4beb7b6eb33281f3520d07c4dfaaa6eb7c6a33883c7e20` |
| `circdist/artifacts/circdist_gross_proof_outer_round88_20260830/PAYLOAD_SHA256SUMS.txt` | 27,621 | 255 | `d2de2f014954070f20bbba0e55caf49aed93b26986a63fab77955a75f62c8157` |
| `DAG_PROTOCOL.md` | 15,377 | 283 | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | 8,523 | 166 | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| `circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md` | 10,199 | 243 | `5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64` |

The complete Round88 package was checked against its root seal `c4061caff46b632b5c4beb7b6eb33281f3520d07c4dfaaa6eb7c6a33883c7e20` and payload seal `d2de2f014954070f20bbba0e55caf49aed93b26986a63fab77955a75f62c8157`. The current Round89 review is bound at `95f830f41a51bff2f0f72967a48984f496981aac89f49b6b9f95f2a4a34d77a8`. `INPUT_BINDINGS.json` and package-local snapshots make every binding replayable. Canonical files were not edited.

## Exact starting state

The inherited state was fresh/unstarted iteration 112:

- 14,484 reviewed, exact, sound order blocks: 1,440 unary, 20 Round62, 12,820 generalized, and 204 dynamic;
- 140 EFSSCs: 120 reviewed Round80, 14 Round86, and 6 Round88;
- selector-state SHA-256 `a0364547f846fd68ace7cdba85d89c0f8e6326145243fb0fea7ff543420994cb`;
- semantic source SHA-256 `a816fa6a7aec4eb3502f4b5c1a8c50dc8d958b383a003a84738fcb7e630e7c43`;
- deterministic compressed CNF: 19,022 assertions, 398,488 variables, 1,330,104 clauses, SHA-256 `a8b917845427a0f746e72200a9a58eb5fac86d5e3c845eeaae69082038c86594`;
- inherited disposition: **UNSOLVED**. Round 90 did not import a model, proof, or solver result.

The mandatory first science action launched a fresh CaDiCaL process on that exact decompressed CNF with proof output enabled. It returned SAT in 3.508054 seconds. The resulting 398,488-variable assignment was retained and independently checked against all 1,330,104 clauses before any continuation state was changed.

## Exact finite outer formula

For a schedule `t`, the outer predicate is

`Outer_P(t) = Legal_MC0_Interleaved(t) AND (AND_j NOT Block_j(t)) AND (AND_s NOT EFSSC_s(t))`,

where `P` is the exact selector prefix used for that iteration. `Legal_MC0_Interleaved` binds all 864 named interactions, strict ancilla and data endpoint serialization, all 648 measurement-commutation overlap equalities, exact extrema, global X/Z whole-check interleaving, and idle-layer compression by rank. No endpoint, stabilizer generator, conflict relation, terminal residual, sector, or repair convention is changed.

The rank-compression theorem and the clause-level equivalence proof are in `COMPRESSION_AND_ENCODING_PROOF.md`. The EFSSC theorem and transition atomicity proof are in `EFSSC_SOUNDNESS_AND_ATOMICITY.md`. The exact distance convention and the boundary between terminal effective evidence and full circuit distance are in `MATHEMATICAL_SCOPE_AND_SOUNDNESS.md`.

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

Every formula was recompiled byte-for-byte from its semantic source. The independent checker partitions every clause exactly once between roots and complete biconditional Tseitin definitions, reconstructs all source roots, accounts for all variables, exhaustively checks `2^20 = 1,048,576` comparator inputs, and checks every emitted rank-membership local-order/qubit case. The checked case count rises from 1,671,840 at iteration 112 to 1,818,720 at iteration 124. Five controls per formula reject a first-clause mutation, truncation, semantic-source mutation, reversed comparator, and the forbidden time value 864.

## Twelve complete outer and 24 complete direct dispositions

| iter | outer seconds | schedule SHA-256 | layers | Xerr direct | Zerr direct | state after |
|---:|---:|---|---:|---|---|---|
| 112 | 3.508054 | `bbcce5e137626ac9fb9600ac093c46789ae2b8ddb13531078b5c06371e574e5e` | 444 | SAT, W=10, 5,934 vars / 22,316 clauses | SAT, W=10, 5,947 vars / 22,368 clauses | `f3c7f81bf7b0d81af3ed254054cd29338c173d2da7f8837be18abcf8306feeee` |
| 113 | 3.711217 | `69db40d0326eb03ddf32e92880f446471cc06f409d802547516d6315687c5cd7` | 429 | SAT, W=10, 5,915 vars / 22,240 clauses | SAT, W=10, 5,940 vars / 22,340 clauses | `0f61bd1f7ddc52a6bfdcfff3d198774ac99d3558931737b9f72b9149311a954b` |
| 114 | 4.056261 | `0fd9611076774d9359d473303269ad801a7b911b6db1a319ee8cd86dc1928fb7` | 87 | SAT, W=10, 5,978 vars / 22,492 clauses | SAT, W=10, 5,877 vars / 22,088 clauses | `0b269f3609e81928bf3e79bc2d1dda1f53f23e800da1c51f2ff1e4a7a1738708` |
| 115 | 3.794670 | `5dac0dbc23c28a3b58e1affbaf7df67270c9364d1a9646792c1403858a29571e` | 475 | SAT, W=10, 5,953 vars / 22,392 clauses | SAT, W=9, 5,990 vars / 22,540 clauses | `7896e13abd03b0665852112f97417e7ec42d838c076b3563bc01c08d59f961b4` |
| 116 | 6.510392 | `6c1f5efcf2ec11e980c3fa6f79b7aba380187abc922687695fd70607b475e26f` | 424 | SAT, W=10, 5,944 vars / 22,356 clauses | SAT, W=10, 5,934 vars / 22,316 clauses | `a16ac76ea004b02d2df4cd3ef6e2787d0de18273a0fa55c0ba8873b1a03df03d` |
| 117 | 6.345738 | `b6de1a0ba69a87841ffc17f8db691d85c85ad29bb245f3b40abbb72fc7099291` | 441 | SAT, W=10, 5,948 vars / 22,372 clauses | SAT, W=10, 5,928 vars / 22,292 clauses | `0392d24445dfc276715ec3eb4ad73e851bac1ad0d58b7463bffac2ad5e78bb55` |
| 118 | 4.285309 | `956618afb0325fa69adecaf994dbcabbd9fb744882552fb8620f1f72070e8b21` | 115 | SAT, W=10, 5,958 vars / 22,412 clauses | SAT, W=10, 5,891 vars / 22,144 clauses | `53e01b89f5b1772a4e6109ce454a5351077ca2092a9f5e3e39a1ebf2c91f4d5e` |
| 119 | 4.036587 | `2efd95f27430f1b8a4d8cef8c86c15ef2247eda26bbe55959f355e60c3410c49` | 123 | SAT, W=9, 5,968 vars / 22,452 clauses | SAT, W=10, 5,930 vars / 22,300 clauses | `e7278568a1e38939969bde2da6b60e950e5be2f8fadd70c58b74e3d807e01faf` |
| 120 | 5.249039 | `a7c52588b152724dce6e822910bbed4ebe37df1aacbbe06ba1459b1ae2688210` | 359 | SAT, W=10, 5,922 vars / 22,268 clauses | SAT, W=10, 5,969 vars / 22,456 clauses | `c96a2e01c5579c28ab048b4101182fea54bec26b9e9e5f70aabde75c72bcd506` |
| 121 | 3.983865 | `4db4b8641df1ae4709f1467177ee0397d5b2cd384ec8c1e7b9f0ca81ea01b643` | 119 | SAT, W=10, 5,944 vars / 22,356 clauses | SAT, W=10, 5,939 vars / 22,336 clauses | `e00d6529570b2e69dbd6da75fa7cc707de354b81b86a2630d2b8bbd0d6bd0b05` |
| 122 | 4.064522 | `91db319cc429009edcf5c856efd24317498e04875c28cf7a9655b225025974be` | 120 | SAT, W=10, 5,972 vars / 22,468 clauses | SAT, W=10, 5,906 vars / 22,204 clauses | `14e551af5ea909e1e88f02def5bfaaf61df3d0557e48c9544546389db1acbf99` |
| 123 | 3.610781 | `9fd434dbd60840b4da5ad4954e655af11468d3643a0fbc1197c89329908ae5f6` | 433 | SAT, W=10, 5,965 vars / 22,440 clauses | SAT, W=10, 5,922 vars / 22,268 clauses | `854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3` |

For every outer model, replay checked all 864 exact interactions, 648 MC overlap constraints, endpoint conflicts, local six-edge orders, MC0, global whole-check interleaving, all 14,484 order blocks, and every EFSSC in that iteration's prefix. All twelve schedules have zero conflicts, zero MC violations, zero reviewed-block hits, and zero valid prior selectors.

Each direct query contains all 360 named columns in one sector: 144 data singletons and 216 residual columns (72 checks times three residual kinds). It enforces all 72 detector XOR equations, twelve logical-parity equations, a nonzero-logical disjunction, and exact `sum(select)<=10`. It has no pool, residual-pattern, check-count, or within-check-family restriction. Each complete assignment was checked against every DIMACS clause, and its physical elementary faults were replayed from the six CNOT times of every selected check.

Iterations 115/Zerr and 119/Xerr produced weight 9; the other 22 mechanisms have weight 10. All have empty physical detector syndrome, nontrivial physical logical class, and equality of canonical and physical logical parities. Complete selections, supports, parities, fault-by-fault times, assignments, formulas, and semantic hashes are sealed under `iterations/`; `PHYSICAL_MECHANISM_INDEX.md` is the compact index.

## Why the positive mechanisms do not close the root

The frozen definitions state

`d_eff(M) = d_ext(E(M))`,

`d_circ(C) = min{ |F| : F triggers no detector and flips a nontrivial logical }`,

and, for the stated memory experiment and boundaries,

`d_eff(M) <= d_circ(C(M)) <= 12`.

A SAT direct-360 assignment is a terminal effective logical of weight at most 10. It proves that its source schedule is invalid as a surviving candidate on the currently licensed completion route, and it licenses only a sound fixed-selector exclusion. Because the direct-360 formula omits the arbitrary-round closure constraints of the full detector circuit, the terminal witness alone is not asserted to be a full spacetime fault of the same weight. It therefore proves neither `d_circ<=10` nor, by itself, `d_circ<=11`. Both direct sectors were SAT on all twelve candidates, so the protocol's repair gate was never entered.

## Exact physical replay

For each sector, the canonical residual representatives at within-check positions are

`R_0={0,1}, R_1={3,4,5}, R_2={4,5}`,

while the actual elementary ancilla-fault suffixes are

`P_0={2,3,4,5}, P_1={3,4,5}, P_2={4,5}`.

For kind 0, `R_0 XOR P_0` is the complete weight-6 stabilizer row. Kinds 1 and 2 coincide. Hence replacing all canonical residuals by physical suffixes changes the net data operator only by stabilizers; detector syndrome and logical coset are invariant. The replay independently recomputes every suffix from the schedule times and checks these invariants for all 24 mechanisms. This is terminal-residual/direct-360 reasoning only.

## Atomic continuation

For each iteration `i`, state mutation occurred only after: the exact prefix formula returned SAT; every outer clause and schedule condition passed; both unrestricted direct sectors returned SAT; both direct assignments and physical mechanisms passed; and the two new EFSSCs were re-evaluated on their source schedule. The transition then appended `r90-i-Xerr` and `r90-i-Zerr` together, emitted the fresh source for `i+1`, and left `started:false`. Later selectors were never applied retroactively to earlier candidates.

The exact chain is 140 → 142 → 144 → 146 → 148 → 150 → 152 → 154 → 156 → 158 → 160 → 162 → 164 selectors. `source/check_continuation.py` rederives the chain from the frozen model. `replay.sh` additionally reruns `source/advance_round90.py` twelve times from the sealed Round88 state and requires byte-identical records, byte-identical next semantic sources, and a byte-identical final state.

## Fresh frontier

- next iteration: 124;
- `started:false`; no `iterations/iter124` directory and no solver/model/proof disposition;
- order blocks: 14,484, unchanged;
- selectors: 164, including 24 new Round90 EFSSCs;
- selector-state SHA-256: `854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3`;
- semantic source SHA-256: `d155a897b8771a9821ef4ef14041bb910e7bbb6aaaad7f6cf08b6db1de0f397e`;
- source-file SHA-256: `1c4556377a4f84d5bf7df1e08af0e98d5cb3d4ea3da94db2e94d645f40a4f544`;
- CNF: 19,046 assertions / 401,040 variables / 1,345,190 clauses;
- CNF SHA-256: `2dd07d33ff0b29c1f06a7452c3b1c7ca9b6df950e819046f8a712dacb0dd7e5a`;
- disposition: independently encoding checked, deliberately unsolved.

## Proof production and controls

All 36 science solver invocations enabled textual proof output and returned SAT code 10. SAT-side proof streams are not refutations: all 36 contain zero empty-clause lines. Their complete hashes, byte counts, and LF counts are in `data/sat_drat_trace_disposition.json`; together they total 7,805,443,420 bytes and 72,337,300 LF lines. The non-certificate streams are intentionally not retained after their dispositions were hash-scanned.

The actual iteration-112 SAT-side stream, a truncated copy, and a corrupted copy were each submitted to `drat-trim` against the actual Gross CNF; all were rejected with code 1. That is a negative checker control only. There is no meaningful actual Gross LRAT conversion target because no Gross DRAT refutation exists.

The sealed pigeonhole fixture validates the tool chain: valid DRAT is accepted; LRAT is generated and accepted; corrupt/truncated DRAT and LRAT are rejected. Fixture LRAT SHA-256 is `cf32dfff36b24ba36c3504765f29ecf3d7a8abaa59956ade4d24a4062caa6431`. Fixture controls establish checker behavior, not a Gross absence fact.

## Environment and process accounting

The recorded dependency interpreter is `/private/tmp/circdist-r72-dispatcher-venv/bin/python` with Python 3.9.6, Z3 5.1.0, and PySAT 1.9.dev15. `/usr/bin/python3` lacks `z3` and is not an acceptable replay interpreter. The sealed CaDiCaL, DRAT, and LRAT binary hashes are in `ENVIRONMENT.json`; network access was unused.

Thirty-six bounded foreground solver children ran: twelve outer and 24 direct. Every child returned code 10, timed out false, and was waited/reaped. Three bounded actual-trace negative-control children returned the expected rejection code 1 and were reaped. Science solver wall time totals 1003.409333 seconds. No detached process, OS background job, or handoff was used. Exact commands, PIDs, parents, timeouts, logs, and statuses are in `PROCESS_LEDGER.json`.

## Replay and evidence layout

`replay.sh` performs the following without running a new Gross SAT search:

1. verifies root/payload manifests and protected canonical hashes;
2. recompiles iterations 112–124 byte-for-byte and reruns the independent encoding checker;
3. replays every outer assignment against every clause and frozen schedule predicate;
4. deterministically rebuilds all 24 direct formulas and dictionaries, clause-checks their stored assignments, and physically replays each mechanism;
5. reconstructs the full twelve-transition EFSSC state chain from the sealed Round88 frontier;
6. cross-checks `RESULT.json`, process records, actual-trace controls, and fresh DRAT/LRAT fixture controls.

`EVIDENCE_HASHES.md` indexes all load-bearing model/replay/formula hashes. `FAILURE_LEDGER.md` excludes every development incident from the verdict. `FIX-2.md` records termination and scratch disposition.

## Pre-seal replay, repository validation, and cleanup

The deterministic pre-seal replay returned `ROUND90_PACKAGE_REPLAY_PASS`. Its 120-line log SHA-256 is `90ddec927b76f07f383320c29dcded09f87751a083f4a4f28039bd11e8e49200` and is sealed under `verification/preseal_replay.log`.

| check | disposition | exit |
|---|---|---:|
| proof-DAG structure, circdist | 16 node files structurally valid | 0 |
| previous-state retention | prior nodes, routes, and events retained; 16 nodes valid | 0 |
| migration preservation | 16 nodes / 143 original events / 728 byte-identical copies | 0 |
| release contracts | 14/14 tests pass | 0 |
| DAG contracts | 24/24 tests pass | 0 |
| Lean DAG selftest | 23/23 assertions pass | 0 |
| duplicate YAML keys | 777 files / 20,291 mappings / zero duplicates | 0 |
| `git diff --check` | no whitespace error | 0 |
| evidence closure | expected new unlinked package only: 548 reported paths, all under the Round90 package prefix | 1 expected |

The first duplicate-YAML invocation used an interpreter without PyYAML and was excluded; the corrected complete validator run is the one summarized above. All six packaging/development incidents and their non-evidentiary status are in `FAILURE_LEDGER.md`.

Protected final hashes pass for all eight live repository inputs and eight package snapshots. `verification/fix2_closure.json` records absence of science scratch, build scratch, the external pre-seal log, the accidental wrong-workspace helper path, and every matching task process. Canonical YAML remains byte-identical.

## Limitations

This package supplies positive continuation evidence only. A library miss, zero selector domain, deletion countertuple, SAT trace, solver runtime, or twelve-candidate campaign is not exhaustion. No negative direct result occurred. No arbitrary-round repair formula was entered. No complete new theorem deciding `D*_Gross` is proposed. Fresh independent review is required before any continuation event or evidence link is added to canonical state.

Canonical YAML remains read-only. No commit and no push were performed.
