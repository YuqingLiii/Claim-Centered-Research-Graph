# Process ledger guide

`PROCESS_LEDGER.json` contains all 72 candidate process records with exact argv, PID/process group, start/end, wall time, hard limit, exit code, timeout flag, and signal flags. Records are ordered and asserted nonoverlapping. The ledger also states the corrected reader/generalizer attempts. Individual wrapper records and logs remain under `cegar/iter30` through `cegar/iter41`.

Counts: 48 exit-0 Python stages, 24 exit-10 CaDiCaL SAT stages, zero timeout, zero signal, zero interruption, zero detached process. The slowest direct call is iteration 41 Xerr at 103.007196125 seconds.
