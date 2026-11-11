# Round92 delta package guide

This is the single sealed proposer delta for Phase-A weight-9 synthesis and the strict-serial
Round92 continuation through iterations 124–135.

The package intentionally depends on the already reviewed repository package
`circdist/artifacts/circdist_gross_proof_outer_round90_20260830`.  `INPUT_BINDINGS.json`
binds both Round90 manifest files by SHA-256.  Replay validates the entire Round90 manifest
closure before using its semantic vendor tree, compilers, or proof tools; any drift fails.

Key directories:

- `synthesis/` and `preouter/`: complete finite synthesis proof object, atomic install,
  strict-expansion CNF/model/replay, and process record.
- `formulas/iter124` through `formulas/iter136`: complete semantic sources, compressed CNFs,
  assertion maps, circuit definitions, metadata, and encoding checks.
- `iterations/iter124` through `iterations/iter135`: complete outer models/logs/replays,
  both unrestricted direct formulas and dictionaries, solver logs, mechanisms, physical
  replays, and atomic transition records.
- `continuation/final_state.json`: fresh, unstarted iteration-136 state.
- `controls/`: actual-formula SAT-trace rejection controls and proof-tool fixture controls.
- `source/`: exact generators and replay checkers used by this package.
- `verification/`: preseal replay, repository validators, protected hashes, FIX-2 closure,
  and final validation summaries.

`PAYLOAD_SHA256SUMS.txt` covers every file except itself and `SHA256SUMS.txt`.
`SHA256SUMS.txt` covers every file except itself and includes the payload manifest.
`FILE_INVENTORY.jsonl` records path, SHA-256, bytes, and LF count for every pre-manifest
payload file.  Run `./replay.sh`; success prints `ROUND92_PACKAGE_REPLAY_PASS`.

