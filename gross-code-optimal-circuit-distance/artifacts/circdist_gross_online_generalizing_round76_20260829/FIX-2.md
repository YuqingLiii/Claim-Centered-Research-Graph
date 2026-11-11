# FIX-2 incident and process disclosure

All computation was foreground and serial. No detached solver, driver, verifier, or generalizer was launched or handed off.

## Corrected/nonzero attempt

The first round-74 `verify.py --quick --repo-root ...` call returned exit 1 at `operations/circdist/SCHEDULER.yaml`. This is the expected live scheduler drift already described by the round-75 review, not a seal or mathematical-input failure. The exact log and run record are retained under `preflight/`. It was followed by a successful sealed offline quick verification and an explicit independent binding of the exact reviewed iteration-54 state. No candidate or installed state existed yet, so the failed read-only check mutated nothing.

## Successful candidate processes

All 168 load-bearing child runs are in `PROCESS_LEDGER.json`. They are serial; 120 exit zero and 48 CaDiCaL runs exit ten. Timeout and signal counts are zero. Exact per-stage logs and run records survive under each iteration.

## Proof-control expected failures

The corrupted/truncated DRAT and LRAT controls exit one with `NOT VERIFIED` by design. They are recorded as successful negative controls, not computation incidents or Gross proof objects.

## Cleanup contract

Before final response, all solver/generalizer/verifier processes, the temporary venv, scratch package, and pointer are removed after atomic installation and post-copy verification. The package records the final process and residue scans.

## Verification-stage distinction

The 3,416.156687416-second uncompressed FULL is explicitly development/precompression and is not accepted as the release gate. After deterministic gzip, the release process runs a separate accepted preseal FULL over the final dual-hash inventory. After atomic installation it runs a separate sealed FULL with live bindings, followed by sealed quick. External accepted/sealed stdout is not inserted into the tree it certifies.

## Compressed-tree quick correction

The first compressed-tree `verify.py --quick --allow-unsealed` call exited one before any mathematical replay because `verify_bindings()` directly opened `src/round62_cegar20.json`, which deterministic compression had replaced with `src/round62_cegar20.json.gz`. The package data and dual-hash inventory were intact. The verifier was corrected to use its transparent `data()` reader for engine bindings, its explicit self-binding in `SOURCE_BINDINGS.json` was refreshed, and the compressed quick was rerun. This was a staging-only verifier-path correction before accepted preseal FULL, seal creation, or repository installation; it mutated no CEGAR state and has no mathematical disposition.
