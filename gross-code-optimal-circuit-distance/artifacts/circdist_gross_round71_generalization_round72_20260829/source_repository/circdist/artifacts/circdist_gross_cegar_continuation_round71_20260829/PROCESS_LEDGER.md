# Process and FIX-2 ledger

The computation was strictly serial and foreground. Each child had its own process group; the wrapper waited in the foreground and would send SIGTERM followed after five seconds by SIGKILL. `PROCESS_LEDGER.json` preserves the 144 candidate process records with argv, PID, process group, UTC times, wall time, exit code, timeout limit, and signal flags.

- 24 outer build/solve processes; all exit 0.
- 24 independent outer replay processes; all exit 0.
- 48 CaDiCaL processes; all exit 10 (SAT).
- 24 direct replay processes; all exit 0.
- 24 dynamic append processes; all exit 0.
- timeout count: 0.
- SIGTERM count: 0.
- SIGKILL count: 0.
- manual interruption count: 0.
- detached/background process count: 0.

The slowest direct query was iter29 Xerr at 47.344877 seconds. The internal/external limits were 600/660 seconds. Fresh package controls add four serial checker processes: valid DRAT and LRAT exit 0; corrupted/truncated DRAT and LRAT exit 1 as required.

Preflight also records the 249-entry round-69 seal check, clean full verifier, all-file/gzip/tar read, dependency installation, and round-70 hash binding. One non-bearing development diagnostic initially used the wrong glob for solver run records and printed an empty slowest list; a corrected query immediately replaced it. It exited 0, changed no state, and was never evidence.

Final inventory, process scan, and scratch cleanup are performed after the package seal; their results are reported in `FINAL_AUDIT.txt`.

## Verification construction ledger

Four preseal development outcomes are retained: one missing-`.gz` quick-check failure, its corrected PASS, one stateful-Z3 full-check failure plus localization rerun, and the fresh-process repair PASS. The final design starts a new Python process for each exact SMT byte reconstruction, matching the computation protocol. See `verification/` and `PROCESS_LEDGER.json`; none of these checker-development runs altered evidence objects.
