# Round100 package manifest

This is the sole Round100 Gross proposer package. The deterministic file inventory is `FILE_INVENTORY.jsonl`; the two SHA-256 seal levels are `PAYLOAD_SHA256SUMS.txt` and `SHA256SUMS.txt`.

- `bindings/`: exact dispatch copies, full initial proof-DAG snapshot, and verified Round98 seal/replay evidence.
- `formulas/`, `state/`, `iterations/`, `transitions/`: exact iterations 172–184 frontier and 172–183 SAT/direct/atomic-transition evidence.
- `synthesis/order6/`: exact six-distinct MITM outputs and independent validation.
- `synthesis/span/`: two retained DRATs, accepted LRATs, negative controls, CNFs, and direct-Z3 validation.
- `source/`, `vendor/`, `tooling/`: package-only reconstruction, validation, solver, and proof tools.
- `verification/`: independent audits, repository gates, full preseal replay, compression controls, and FIX-2 closure.
- `FAILURE_LEDGER.*`, `PROCESS_LEDGER.json`: every known rejected attempt and retained PID-bearing process evidence.
- `REPORT.md`, `RESULT.json`, `SYNTHESIS_PROOF.md`, `MATHEMATICAL_SCOPE_AND_SOUNDNESS.md`: verdict, exact derivations, theorem scope, and limitations.

Replay with a Python environment providing Z3 5.1.0:

```sh
PYTHON=/private/tmp/circdist-r72-dispatcher-venv/bin/python ./replay.sh /private/tmp/round100-replay.json
```

The sealed replay is read-only with respect to this package; its record is written to the supplied external path.
