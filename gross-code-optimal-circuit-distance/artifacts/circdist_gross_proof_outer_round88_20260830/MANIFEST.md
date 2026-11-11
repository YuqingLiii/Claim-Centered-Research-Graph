# Package map

- `REPORT.md`: verdict, public derivation summary, logical consequences, validation, and residual.
- `RESULT.json`: machine-readable outcome and fresh iter112 frontier.
- `COMPRESSION_AND_ENCODING_PROOF.md`: formal bounded-time lemma, full CNF semantics, model maps, checker, controls, and formula inventory.
- `continuation/final_state.json`: atomic fresh/unstarted iter112 state with 140 selectors.
- `formulas/iter109` through `formulas/iter112`: semantic sources, compressed complete CNFs, assertion maps, circuit traces, metadata, and independent checks.
- `iterations/iter109` through `iterations/iter111`: complete outer assignments/models/replays, both unrestricted direct-360 CNFs/logs/replays, and atomic records.
- `source/`: deterministic compiler, independent encoding checker, SAT/model replay, direct/final-state replay helpers, manifest/protected checks, and bounded runner.
- `controls/proof_checker/`: valid/corrupt/truncated DRAT and LRAT controls and durable logs.
- `bindings/`: exact canonical snapshots, Round80/Round81 and Round86/Round87 bindings, and initial proof-DAG snapshot.
- `PROCESS_LEDGER.json`, `FIX-2.md`, and `FAILURE_LEDGER.md`: process and failure accounting.
- `verification/`: replay, protected-input, previous-state, schema, migration, contract, Lean, evidence-closure, duplicate-key, diff, cleanup, and survivor records.
- `PROPOSED_CANONICAL_DELTA.md`: review-only proposed evidence/frontier text; no canonical edit.
- `FILE_INVENTORY.jsonl`: per-file bytes, lines, and SHA-256, excluding itself and the two recursive seal manifests.
- `PAYLOAD_SHA256SUMS.txt`: every payload file except both seal manifests.
- `SHA256SUMS.txt`: root manifest containing every file except itself, including the payload manifest.
