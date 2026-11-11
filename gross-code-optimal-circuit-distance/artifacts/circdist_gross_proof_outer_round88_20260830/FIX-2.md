# FIX-2 process ledger

All verdict-bearing jobs ran in the foreground through `source/run_bounded.py`.  The wrapper recorded runner PID, parent PID, child PID, exact argv, stdout/stderr paths, wall bound, start/end time, return code, timeout status, and wall time.  On timeout it sends TERM, waits up to ten seconds, sends KILL if needed, and always waits to reap the child.

Nine long processes were started: three outer CaDiCaL calls and six unrestricted direct-360 CaDiCaL calls.  Every process returned SAT with code 10 before its bound and was reaped.  The outer bounds were 900 seconds; direct bounds were 620 seconds around a solver `-t 600` limit.  Observed outer runtimes were 3.916632, 4.336352, and 6.534544 seconds.  Direct runtimes were 122.184040, 49.359826, 90.957324, 40.480697, 21.134692, and 29.374692 seconds.

No OS-level background or detached process was started.  `PROCESS_LEDGER.json` contains every exact command and PID.  Named process records and solver logs are retained under `logs/` and `iterations/`.  There is no pending handoff.  Final survivor scan output is under `verification/`.

The SAT invocations requested DRAT output, but such traces do not end in an empty clause and are not proof objects.  Their sizes, hashes, line counts, and zero empty-clause-line counts are preserved in `data/sat_drat_trace_disposition.json`; the large scratch traces are intentionally excluded.  Complete SAT CNFs, assignments, solver logs, and semantic replays are retained instead.
