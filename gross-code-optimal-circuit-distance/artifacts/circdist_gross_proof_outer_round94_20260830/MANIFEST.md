# Package map

- `REPORT.md`: public result, exact hashes, campaign table, branch accounting, and reproduction command.
- `RESULT.json`: machine-checkable scientific verdict.
- `INPUT_BINDINGS.json`, `bindings/`, `reconstruction/`: protected inputs and fresh iteration-136 source/CNF correspondence.
- `formulas/iter136..iter148/`: every exact source, CNF, assertion map, trace, metadata, and independent encoding check. Plain CNFs/maps are deterministically gzip-compressed.
- `iterations/iter136..iter147/`: complete outer assignments/schedules, both direct formulas and assignments, canonical/physical replays, SAT-stream dispositions, and transition records.
- `state/`, `transitions/`: all selector prefixes and atomic pending/commit evidence through fresh iteration 148.
- `synthesis/`, `SYNTHESIS_PROOF.md`: exact order-3 domain, coverage, misses, and relaxation counterexamples.
- `controls/`, `tooling/`: valid/corrupt/truncated DRAT/LRAT fixtures and native arm64 macOS tools.
- `vendor/round80/`: frozen Gross geometry, canonical/physical model, and direct replay implementation.
- `logs/`, `PROCESS_LEDGER.json`, `FAILURE_LEDGER.md`, `FIX-2.md`: complete retained processes, stdout/stderr/wrapper records, incidents, and closure.
- `source/`, `replay.sh`: deterministic reconstruction and all cross-checkers.
- `verification/`: independent audit, synthesis regeneration, replay, repository validators, protected-input scan, and FIX-2 evidence.
- `FILE_INVENTORY.jsonl`, `PAYLOAD_SHA256SUMS.txt`, `SHA256SUMS.txt`: exact byte/LF inventory and two-level seals.
