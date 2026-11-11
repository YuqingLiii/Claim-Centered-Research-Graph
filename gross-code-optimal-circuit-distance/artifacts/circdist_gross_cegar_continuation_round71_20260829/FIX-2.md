# FIX-2 exhaustive disposition

All material candidate processes are enumerated individually in `PROCESS_LEDGER.json`; none is omitted or aggregated away there. There were no timeouts, killed processes, manual interrupts, daemons, worker pools, or detached jobs. CaDiCaL exit 10 is the documented SAT result, not a failure. The two checker-control exit-1 results are required rejection outcomes.

The run made no repository write before the final atomic package copy. All candidate state, virtual environments, scripts, and staging data lived under `/tmp/circdist_gross_r71`. Package-excluding inventory is compared byte-for-byte at finalization. After the final copy, the scratch tree is removed and a final process scan is required to show no matching solver, verifier, builder, checker, or wrapper process.

## Verifier development failures retained

The first preseal quick run exited 1 because the checker referred to `round69_all_file_read.json` after deterministic compression had renamed it `.json.gz`. The corrected quick run passed. The first preseal full run and a diagnostic rerun exited 1 at iter7 because a fixed-model Z3 check in the same Python process changed AST creation/printing state for the next `to_smt2()` call. An isolated iter7 fresh process reproduced the sealed bytes exactly. The verifier was repaired to spawn one fresh outer-reconstruction process per candidate; the next full replay passed all 24 iterations in 332.04 seconds. All four logs, the localization hashes, and the successful isolated/final logs are sealed under `verification/`. No candidate, formula, assignment, block, or dynamic-state byte was changed by these checker-only failures.

## Clean-environment and tool-policy record

A command that would have removed a possibly existing clean-preseal virtual environment with `rm -rf` was rejected by the execution tool before process creation. No command ran and no file changed. A fresh unique path was used instead. That Python 3.9.6 environment installed the exact four pinned requirements and completed full replay with live repository bindings in 332.28 seconds, exit 0.

A combined process-scan diagnostic initially matched its own shell command line and failed its zero-match assertion. The corrected two-step snapshot/filter found zero actual matching processes. This was a scan-construction artifact, not a surviving process.
