# Direct-360 completeness and proof policy

## Formula contents

Each candidate/sector formula is rebuilt from the frozen 360 columns tied to that candidate's 864-edge schedule. It contains:

- 360 primary selection variables;
- exact XOR constraints for all 72 opposite-check syndrome rows;
- exact XOR constraints for all 12 logical parity outputs;
- one disjunction requiring a nonzero logical quotient;
- an exact prefix-threshold recurrence encoding `sum(selection) ≤ 10`;
- no logical-pool restriction;
- no residual-pattern restriction;
- no check-count restriction;
- no within-check order-family restriction.

The formula summaries name these families and set `complete_query: true`. The full package verifier freshly rebuilds each formula and requires byte equality for CNF, clause dictionary, column dictionary, variable dictionary, and summary.

## SAT policy

A solver exit code 10 is not accepted on status text alone. `round68_verify.verify_one` parses the complete assignment, checks every DIMACS clause, derives all selected primary columns, and replays both canonical and physical mechanisms. The retained negative controls flip the first selected primary variable and remove the first selected fault; both perturbations must fail the relevant check.

A DRAT stream written during a SAT run is not a proof. The twelve SAT traces in this round were excluded after their hashes and byte counts were recorded in `cegar/sat_trace_disposition.json`. The retained formula and full assignment are sufficient for independent SAT checking and physical replay.

## UNSAT/absence policy

A direct-sector absence verdict would require all of the following for that exact candidate and sector:

1. the complete candidate-specific DIMACS described above;
2. a foreground proof-logging SAT run within an explicit hard limit;
3. an UNSAT solver result;
4. independent acceptance of the DRAT proof;
5. conversion to LRAT and independent LRAT acceptance;
6. hashes binding candidate, schedule, columns, DIMACS, proof, and checker binaries.

UNKNOWN, timeout, incomplete positive finder, missing proof, or rejected proof is no verdict. In round 69 no candidate sector was UNSAT, so candidate-specific absence proofs number zero.

## Repair gate

Arbitrary-round repair may begin only after independently checked absence in both Xerr and Zerr for the same candidate. All six candidates were SAT in both sectors. The gate therefore remained closed in every iteration.

## Checker controls

Fresh controls were run with the pinned binaries:

| checker | positive | corrupted/truncated |
|---|---|---|
| DRAT (`drat-trim`) | accepted, exit 0, `VERIFIED` | rejected, exit 1, `NOT VERIFIED` |
| LRAT (`lrat-check`) | accepted, exit 0, `VERIFIED` | rejected, exit 1, `NOT VERIFIED` |

The control CNF, proofs, logs, run JSON, binaries, source archives, and build records are sealed under `controls/proof_checker/` and `tooling/`. The full verifier reruns all four controls.
