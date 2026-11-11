# Foreground process ledger

`PROCESS_LEDGER.json` contains 168 load-bearing records in strict time order: 24 outer builds, 24 independent outer replays, 48 CaDiCaL direct runs, 24 direct raw replays, 24 exact-block appends, and 24 online generalizations. The 48 solver records exit 10 (SAT); the other 120 exit 0. None timed out, received SIGTERM/SIGKILL, detached, or overlapped the next load-bearing stage.

The sole nonzero author attempt was a read-only source-package quick check with live bindings. It exited 1 on the scheduler snapshot because the live scheduler had expected post-round-74/75 drift. No research state was touched. The sealed package was then verified without the stale live comparison, and the reviewed iteration-54 states were separately rebound to their exact hashes.
