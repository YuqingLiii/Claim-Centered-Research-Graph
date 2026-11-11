# Process ledger

`PROCESS_LEDGER.json` contains every accepted foreground subprocess record from the 12 iterations and all cross-registry development dispositions. There are 96 accepted subprocess records, no accepted timeout or signal, and no detached load-bearing process. Each iteration is serial: fresh outer build, independent outer replay, X direct solver, Z direct solver, direct replay, candidate-exact pending append, online pending generalization, cross-registry pending synthesis, then validated four-state commit.

Development memory incidents, failed assertions, the v6 rollback, and proof-control corrections are not omitted. Raw stdout/time logs are retained under `development/`. Absolute staging paths in historical argv records identify the actual run; package verification uses package-relative live paths.
