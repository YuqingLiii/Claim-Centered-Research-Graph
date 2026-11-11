# FIX-2 process ledger

## Scope declaration

- Worker sessions: one, this round-68 worker.
- Sub-agents or delegated workers: none.
- Worker pools: none.
- Detached/background/nohup/daemon/cron jobs: none.
- Solver/checker calls: all foreground and explicitly time limited.
- Repository compute tools: read-only except for creation of this one package directory at final handoff.
- System-wide installation: none.
- External scratch root: `/tmp/circdist_gross_direct360_proof_round68_20260829/`; deleted at finalization.

## Foreground process classes

| stage | processes | concurrency | limit/termination | durable output |
|---|---|---|---|---|
| read-only preflight | `rg`, `find`, `cat`, `sed`, `shasum`, Python/YAML inspection, `git status`, `ps` | serial/batched reads | all exited | source/seal/binding logs |
| dependency environment | `python3 -m venv`; venv `pip install` pinned requirements | serial | exited 0 | requirements only; venv remains scratch until cleanup |
| source acquisition | two foreground `git clone --depth 1` calls, CaDiCaL tag `rel-1.9.5`, drat-trim HEAD | serial | exited 0 | exact source archives and commit/tree hashes |
| initial tool builds | CaDiCaL `./configure && make -j1`; drat-trim `make -j1` | both `make` jobs were individually `-j1`; the two independent builds were awaited in one foreground orchestration call | both exited 0; no job survived | binaries/source hashes |
| solver tests | CaDiCaL `make test` twice, second run retained | serial | exited 0 | `tooling/cadical_make_test.log` |
| inherited replay | round62 verifier; round63 manifest; round63 static/full-static verifier | serial | exited; stale live-bind failure retained separately | preflight logs |
| candidate/DIMACS build | three Python invocations: two assertion-stopped development attempts, one completed build | serial | first two exited by assertion; final exited 0 | candidate, SMT2, clauses, DIMACS, dictionaries |
| initial direct runs | CaDiCaL Xerr then Zerr using the first build | serial | `-t 600`; both exit 10 SAT | superseded after exact included-binary replay |
| exact retained direct runs | included CaDiCaL binary, Xerr then Zerr | serial | `-t 600`; both exit 10 SAT | solver logs, run records, compressed SAT traces |
| raw replay | Python clause evaluator/algebra verifier | serial | exited 0 | `verification.json` |
| C1 attempted control | CaDiCaL PID 83918 | one foreground solver | internal `-t 120`; explicitly SIGINT-terminated at 61.43 real s, exit 130; parent shell reaped | non-verdict log/run record; 693,145,600-byte trace deleted |
| proof positive control | CaDiCaL on PHP(6,5) | serial | `-t 60`, exit 20 UNSAT | CNF, DRAT, log |
| proof check | drat-trim, then lrat-check | serial | drat `-t 60`; LRAT checker enclosed by Python 60-second timeout; exit 0 | check logs, LRAT |
| proof corruptions | drat-trim and lrat-check on altered proofs | serial | 60-second limits; strong truncations exit 1; weak deletion exits 0 | all logs and corrupt objects |
| encoding controls | PySAT/CaDiCaL wrapper over 128 cardinality assignments and 8 XOR rows | serial | exited 0 | control JSON |
| independent SAT control | PySAT Glucose42 on complete primary Zerr CNF | serial | Python subprocess enclosing timeout 60 s; exit 0 SAT | full model and raw replay |
| CEGAR continuation | one Python/Z3 process, five sequential outer solves | serial | each outer solve has 120-second Z3 timeout; all SAT | five raw schedules, ten mechanisms/blocks |
| package verifier | Python verifier plus sequential drat-trim/lrat-check children | serial | checker children limited to 60 s | verification replay log |
| final manifest replay environment | temporary external Python venv and pinned `pip install -r requirements.txt`; package verifier plus sequential checker children | serial | verifier enclosed by a 180-second timeout; checker children limited to 60 s; venv deleted after replay | final audit |

The one foreground orchestration call that built the two unrelated source trees concurrently did not launch solver work, mathematical search, a worker pool, or detached compute. Every mathematical and verdict-bearing solve/check was strict serial.

## Termination state

The finalizer records the post-cleanup scratch existence check, process scan, package inventory, and repository delta in `FINAL_AUDIT.txt`. No process is handed off.
