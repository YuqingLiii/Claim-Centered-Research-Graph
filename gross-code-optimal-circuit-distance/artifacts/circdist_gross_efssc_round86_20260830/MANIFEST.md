# Package manifest

`REPORT.md` is the top-level scientific report and begins with the required verdict. This directory is the sole durable Round86 proposer package.

## Layout

- `continuation/`: exact final and checkpoint states, both iteration 109 unstarted.
- `data/`: seed candidate, complete seed direct-360 CNFs/dictionaries/assignments/replay, and the exact fourteen-selector domain census.
- `formulas/`: compiler final SMT-LIB, independent normalized-equivalent rebuild, and the seed formula.
- `iterations/`: complete atomic iteration records 103 through 108.
- `source/`: Round86 compiler, direct builder, exact census, and independent checkers.
- `vendor/round80/`: the minimal frozen reviewed model and restart inputs required for self-contained replay.
- `source_bindings/`: immutable copies of mandatory canonical documents and the reviewed package manifests.
- `verification/`: deterministic expected replay objects, canonical read-only inventory, protocol-gate logs, exit codes, and timings.
- `logs/`: accepted computation, solver, replay, environment, and process logs.
- `development/`: rejected attempts and exact FIX-2 diagnostics; none is accepted evidence.
- `FIX-2.md`, `PROCESS_LEDGER.json`: rollback and process accounting.
- `INPUT_BINDINGS.json`: origin hashes, sizes, counts, and network disposition.
- `FILE_INVENTORY.jsonl`: SHA-256, bytes, and line counts for every non-seal payload file present before the inventory was written.
- `replay.sh`: package-local deterministic replay.

## Seal convention

`PAYLOAD_SHA256SUMS.txt` lists every payload file except itself and `SHA256SUMS.txt`, in bytewise path order. `SHA256SUMS.txt` lists the same payload plus `PAYLOAD_SHA256SUMS.txt`; it excludes itself. The payload seal is the SHA-256 of `PAYLOAD_SHA256SUMS.txt`. The root seal is the SHA-256 of `SHA256SUMS.txt`. This is the inherited non-circular seal convention.
