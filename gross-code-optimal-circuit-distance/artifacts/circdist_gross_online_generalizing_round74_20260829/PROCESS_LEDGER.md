# Foreground process ledger

`PROCESS_LEDGER.json` contains 84 successful load-bearing records in strict time order: 12 outer builds, 12 independent outer replays, 24 CaDiCaL direct runs, 12 direct raw replays, 12 exact-block appends, and 12 online generalizations. The 24 solver records exit 10 (SAT); the other 60 exit 0. None timed out, received SIGTERM/SIGKILL, detached, or overlapped the next load-bearing stage.

Three corrected attempts from iteration 42 are retained separately: one replay schema assertion exited 1; two online-generalization authoring attempts were deliberately terminated with exit -15 before generalized/registry installation. Their exact reasons and state-mutation invariants are recorded in `FIX-2.md` and the iteration42 outcome. They are not silently omitted from the history.
