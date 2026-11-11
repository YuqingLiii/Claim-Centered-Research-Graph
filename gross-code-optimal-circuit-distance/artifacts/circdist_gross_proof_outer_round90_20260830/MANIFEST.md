# Round90 package manifest guide

## Purpose

This is the single sealed proposer package for the strict-serial Round90 continuation from iteration 112 through iteration 123. It is self-contained for formula reconstruction, complete SAT-model replay, direct-360 reconstruction, physical mechanism replay, exact EFSSC state reconstruction, proof-checker controls, and protected-input verification.

## Directory map

- `bindings/`: current canonical snapshots, frozen protocols, Round88 seals/report/state, and the initial proof-DAG snapshot.
- `formulas/iter112` … `iter124`: semantic sources, compressed DIMACS, assertion maps, circuit traces, metadata, and independent encoding checks.
- `iterations/iter112` … `iter123`: complete outer assignments/logs/candidates/replays; both direct formulas, dictionaries, solver logs, physical replays; atomic records.
- `continuation/final_state.json`: fresh/unstarted iteration-124 selector state.
- `data/sat_drat_trace_disposition.json`: complete hash/size/line disposition for all 36 SAT-side streams.
- `controls/`: actual-Gross SAT-stream rejection records and valid/corrupt/truncated DRAT/LRAT fixtures.
- `source/`: exact compiler, independent checkers, deterministic direct builder, transition writer, and replay helpers.
- `vendor/round80/`: frozen Gross semantic model and code/logical inputs.
- `tooling/`: exact arm64 macOS CaDiCaL/DRAT/LRAT binaries.
- `verification/`: durable replay and repository-validation records.

## Seal construction

`PAYLOAD_SHA256SUMS.txt` lists every package file except itself and `SHA256SUMS.txt`, sorted by POSIX relative path. `SHA256SUMS.txt` lists every package file except itself and therefore includes the payload manifest. The root seal is the SHA-256 of `SHA256SUMS.txt`; the payload seal is the SHA-256 of `PAYLOAD_SHA256SUMS.txt`.

`FILE_INVENTORY.jsonl` gives each file's path, SHA-256, byte count, and LF count. The inventory is itself sealed by both manifests. The two manifest files cannot both recursively include their own hashes; this two-level convention is the same deterministic closure used by the preceding sealed packages.

## Replay

Use the recorded interpreter or set `CIRCDIST_PYTHON` to a Python environment containing Z3 5.1.0 and PySAT 1.9.dev15:

```sh
CIRCDIST_PYTHON=/private/tmp/circdist-r72-dispatcher-venv/bin/python ./replay.sh
```

Successful completion prints `ROUND90_PACKAGE_REPLAY_PASS`. The replay never solves iteration 124 and never launches a new Gross SAT search.

## Evidentiary boundary

The package proves checked positive continuation through twelve candidates and a fresh exact state. It does not prove Gross UNSAT, direct absence, repair absence, outer exhaustion, `D*_Gross=11`, or `D*_Gross=12`.
