CONTINUATION-ADVANCED-NOT-PROVED

# CIRCDIST.gross proof-producing outer continuation — Round 88

Date: 2026-08-30  
Scope: frozen `S_Gross` only  
Canonical claim SHA-256: `fc22f602b9bfd9e38fa69d7fc1d00b973c7a634e6c400662eaccd38c8ec0f180`

## Verdict and exact consequence

This proposer does **not** prove `D*_Gross=11` or `D*_Gross=12`.  The exact residual remains

`D*_Gross in {11,12}`.

The new result is a proof-producing finite outer engine and three sound strict-serial continuation steps.  Iterations 109, 110, and 111 each produced a complete SAT schedule.  Both unrestricted direct-360 sectors were SAT at weight 10 for each schedule.  Every assignment and physical mechanism was independently replayed before two exact EFSSC selectors were installed atomically.  The final continuation is fresh/unstarted iteration 112 with 140 selectors.  Its complete outer CNF is built and independently checked but deliberately unsolved.

No Gross outer UNSAT/exhaustion, no direct-sector absence, no arbitrary-round repair, no completion-gap certificate, and no distance-12 schedule is claimed.

## Input authorization and binding

The exact Round88 authorization in `operations/circdist/SCHEDULER.yaml` was read before work.  The protected inputs remained byte-identical through sealing:

| input | bytes | SHA-256 |
|---|---:|---|
| scheduler | 213,858 | `fb1c4003bb0da9426e49eff2e2d30a5af437e7be923ee765b20998fdad49081b` |
| canonical Gross node | 57,967 | `f42dd0333a8faea3858cefcd859c0343ab33aedf2a6a1e663f2fa1625701288e` |
| Round87 exact review | 87,783 | `c37912c5446819ed74e1636049d313c72601dd6a8b1543db01b6b22b51a2f25c` |
| Round86 root seal | 14,011 | `94322390a648262e8cc035f8e843617f134fe2d29ff36191720b646c021c89ff` |
| Round86 payload seal | 13,922 | `443b84ce18c568bdd6b88c4737d03b222b518897eecab787ffa1cc43718f182b` |

Round80/Round81 inputs and frozen problem/protocol/tool files are transitively and directly inventoried in `INPUT_BINDINGS.json`.  `verification/protected_hashes_final.json` recomputes every one of those initial hashes and reports PASS.  Canonical edits: **none**.

## Exact start state

The independently reviewed Round86 continuation was verified as fresh/unstarted iteration 109:

- `started: false`, with no iteration-109 record;
- 14,484 sound order exclusions: 1,440 unary, 20 Round62, 12,820 generalized, 204 dynamic;
- 134 exact EFSSC selectors: 120 Round80 plus 14 Round86;
- selector-state SHA-256 `9be75eba643ac167d5c51497ca8e5cd23eb1656f803a49cbd8e7f1285b004113`;
- compiler outer: 19,016 assertions, SHA-256 `94d404da1777ef108a2a508dc55ca0f3fda68bc489482a00337d9acb7317ac4d`;
- independent-printer normalized AST: 19,016/19,016 structurally equal, SHA-256 `6ac624f2acb35a6311034829970b4d2993fcdf208080898a8e1dbeff1dcb3c7d`.

The sealed Round86 replay returned 0 and rebuilt this state and formula independently.

## Finite compression theorem

A legal schedule assigns times to 864 named edges.  Sort the distinct used values and replace each time by its zero-based rank.  This maps every schedule to times `0..k-1`, where `k<=864`, hence the safe bound is exactly `0..863`.

The map preserves and reflects equality and strict order for every edge pair.  Consequently it preserves all ancilla/data conflicts, all MC0 comparison equivalences, extrema and global interleaving, every reviewed order block, every within-check rank, every residual-position membership, and all EFSSC detector/logical parities.  Conversely every bounded satisfying assignment is already an unbounded legal schedule.  The two outer problems are therefore equisatisfiable.

The public derivation and every clause family are specified in `COMPRESSION_AND_ENCODING_PROOF.md`.

## Total finite encoding

Each edge time and each of four extrema is a ten-bit unsigned word; roots enforce every edge time `<864`.  The compiler uses complete biconditional Tseitin definitions, producing a unique extension of each primary assignment.  It encodes the complete frozen formula: endpoint serialization, MC0, extrema, global interleaving, all 14,484 reviewed exclusions, and every exact EFSSC.

| iter | selectors | assertions | variables | clauses | CNF SHA-256 | disposition |
|---:|---:|---:|---:|---:|---|---|
| 109 | 134 | 19,016 | 397,902 | 1,326,596 | `536c348ede8409ca5d691091213acbada828934a6be641da0fd3a80a62c9292f` | SAT/replayed |
| 110 | 136 | 19,018 | 398,070 | 1,327,548 | `932c4b0f31bb010950bc9999269983c79bba4c3941b883031ca3c14693f8946d` | SAT/replayed |
| 111 | 138 | 19,020 | 398,235 | 1,328,487 | `f0255ef2232c572ae6cc0aa3a50ec76a7b5bef4a13fbc42ad1f342ecf6e5a8f0` | SAT/replayed |
| 112 | 140 | 19,022 | 398,488 | 1,330,104 | `a8b917845427a0f746e72200a9a58eb5fac86d5e3c845eeaae69082038c86594` | checked, unsolved |

The assertion map covers all source assertions and binds every root clause.  The circuit trace covers every auxiliary definition.  The independent checker partitions every DIMACS clause exactly once, reconstructs every source root, accounts for every variable, exhaustively checks all 1,048,576 ten-bit comparator input pairs, and checks 1,637,280 through 1,671,840 rank/order/qubit cases per formula.  Mutation, truncation, reversed-comparator, semantic-source, and value-864 controls are rejected.  All four checks report PASS.

`replay.sh` recompiles all four formulas byte-for-byte, then reruns these independent checks.

## SAT candidates and complete direct adjudication

CaDiCaL 1.9.5 returned SAT for the three outer CNFs.  Complete assignments satisfy every DIMACS clause, decode all 864 edge times, replay all frozen schedule predicates, and hit zero reviewed blocks and zero preceding EFSSCs.

| iter | outer seconds | schedule SHA-256 | layers | Xerr direct result | Zerr direct result |
|---:|---:|---|---:|---|---|
| 109 | 3.916632 | `773832f5d01143a26a41b03481c2c6a21524590191c76e8a4d80af208a6b2efe` | 129 | SAT, W=10, 5,966 vars / 22,444 clauses, block 16 | SAT, W=10, 5,934 vars / 22,316 clauses, block 50 |
| 110 | 4.336352 | `3e51e30e33a32697af935908eaa368409366dcd4bb334c2290b85a2c7ac47d46` | 136 | SAT, W=10, 5,980 / 22,500, block 16 | SAT, W=10, 5,946 / 22,364, block 63 |
| 111 | 6.534544 | `4d6db429ad2759d87b6e4291885581c860df901186bf5eebbb0ab077a7ede0d2` | 384 | SAT, W=10, 5,935 / 22,320, block 25 | SAT, W=10, 5,968 / 22,452, block 80 |

Each direct query is the complete unrestricted direct-360 `W<=10` formula for its sector.  Its solver log contains a complete assignment.  Independent replay checks every clause, reconstructs the canonical and physical fault, confirms weight 10, empty physical syndrome, physical nontriviality, and canonical/physical parity equality.  Because both sectors are SAT in every iteration, the frozen repair gate remains closed.

SAT-side DRAT traces have no empty-clause line and are neither SAT certificates nor UNSAT proofs.  Their hashes/sizes are disclosed in `data/sat_drat_trace_disposition.json`; complete CNFs, assignments, and semantic replays are sealed.  No solver-trust absence conclusion is made.

## Atomic continuation

For each candidate, both direct replays completed before state mutation.  The two source-exact EFSSC selectors were installed together; later selectors were never applied retroactively.  Three commits add:

- `r88-i109-Xerr`, `r88-i109-Zerr`;
- `r88-i110-Xerr`, `r88-i110-Zerr`;
- `r88-i111-Xerr`, `r88-i111-Zerr`.

The final state is:

- next iteration 112;
- `started: false` and no `iterations/iter112` solve directory;
- 140 selectors total;
- selector-state SHA-256 `a0364547f846fd68ace7cdba85d89c0f8e6326145243fb0fea7ff543420994cb`;
- checked unsolved iter112 CNF SHA-256 `a8b917845427a0f746e72200a9a58eb5fac86d5e3c845eeaae69082038c86594`.

`source/check_continuation.py` independently reconstructs every transition and returns PASS.

## Proof-chain controls

A fresh pigeonhole control validates the UNSAT tool chain without attributing that result to Gross:

- valid DRAT accepted;
- LRAT generated, SHA-256 `cf32dfff36b24ba36c3504765f29ecf3d7a8abaa59956ade4d24a4062caa6431`;
- generated LRAT accepted independently;
- corrupt and truncated DRAT rejected;
- corrupt and truncated LRAT rejected.

These are checker controls only.  No Gross formula returned UNSAT.

## Failures and exclusions from evidence

`FAILURE_LEDGER.md` preserves all ten development and packaging incidents.  Most consequential was an initial 1,326,595-clause iter109 serialization missing the pinned-true unit; the independent checker rejected it, it was never solver-run, and it is absent from the accepted formula set.  Other incidents were extractor/schema/key compatibility or packaging syntax failures stopped before evidence acceptance.  No OOM occurred.

## Process accounting and cleanup

Nine bounded foreground solver processes ran: three outer and six direct.  Every exact command, PID, parent PID, timeout, log, runtime, and final status is in `PROCESS_LEDGER.json`; all returned SAT code 10 and were reaped.  No detached or OS-background process was started.  The package and Round86 validation replays ran in Codex foreground sessions and both returned 0; their durable logs are under `verification/`.  Science scratch `/tmp/circdist_round88_outer` was removed.  The final pre-seal survivor scan found zero matching processes.

## Repository validation

| check | result | exit |
|---|---|---:|
| Round88 deterministic pre-seal replay | `ROUND88_PACKAGE_REPLAY_PASS` | 0 |
| sealed Round86 replay | `ROUND86_PACKAGE_REPLAY_PASS` | 0 |
| proof-DAG schema, circdist | 16 nodes valid | 0 |
| previous-state retention | prior nodes/routes/events retained | 0 |
| migration | 16 nodes, 143 events, 728 copies | 0 |
| release contracts | 14/14 | 0 |
| DAG contracts | 24/24 | 0 |
| Lean selftest | 23/23 | 0 |
| duplicate YAML keys | 758 files, 19,378 mappings, zero duplicates | 0 |
| `git diff --check` | clean | 0 |
| evidence closure | 231 unlinked paths, all inside this new package | 1, expected proposer-stage |

The evidence-closure result is not reported as clean.  Canonical edits were forbidden, so the checker correctly identifies this new proposer package as unlinked.  `verification/evidence_closure_interpretation.json` verifies that every reported error has that one prefix and that there are no unexpected closure failures.  Independent review and authorized canonical linkage are still required.

## Replay

From repository root:

`CIRCDIST_PYTHON=/private/tmp/circdist-r72-dispatcher-venv/bin/python ./circdist/artifacts/circdist_gross_proof_outer_round88_20260830/replay.sh`

The replay verifies both manifests, protected hashes, deterministic compilation, independent component equivalence, all SAT assignments, all direct physical mechanisms, the atomic final state, proof controls, and absence of an iter112 solve directory.

## Remaining work

Begin only from sealed fresh iteration 112.  Run the checked CNF with complete assignment replay if SAT or a complete accepted DRAT-to-LRAT proof chain if UNSAT.  A SAT schedule must again receive both unrestricted direct-360 adjudications.  Repair remains forbidden until both sectors are independently proof-UNSAT.  The residual `{11,12}` must remain unchanged unless the exact root route is completed.

`PROPOSED_CANONICAL_DELTA.md` is text only and requires independent review.  This proposer made no canonical, scheduler, generated-view, review, commit, or push change.
