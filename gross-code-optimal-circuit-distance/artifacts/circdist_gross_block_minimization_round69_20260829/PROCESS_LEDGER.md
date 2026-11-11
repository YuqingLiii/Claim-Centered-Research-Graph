# FIX-2 process ledger

## Execution policy

Every round-69 computation was run in the foreground and serially. No worker pool, detached command, background shell job, `nohup`, scheduler, or daemon was used. Each potentially long solver/replay had an internal and/or external hard timeout. Solver result `UNKNOWN`, timeout, interruption, or missing proof was never converted to SAT or UNSAT.

A clean virtual environment at `/tmp/circdist_round69_work_20260829_a/venv` used Python 3.9.6 and the four pinned packages in `requirements.txt`. No system-wide package was installed. The already sealed round-68 ARM64 macOS binaries were reused; round 69 compiled no solver or proof checker. Their source archives and prior build records are copied into `tooling/`.

## Material completed processes

| phase | command/process | limit | result |
|---|---|---:|---|
| round-62 preflight | clean-venv Python `verify.py` | 180 s external | PASS, 3.272 s |
| round-63 preflight | clean-venv Python `verify.py --full-static` | 300 s external | PASS, 10.644 s |
| round-68 live-binding preflight | clean-venv Python `verify.py --repo-root …` | 300 s external | exit 1, expected post-seal drift at Gross node and scheduler only, 19.303 s |
| round-68 sealed preflight | clean-venv Python `verify.py` | 300 s external | PASS, 18.673 s |
| W14 Xerr individual incremental query | PySAT CaDiCaL 1.9.5, 1,800 assumptions | 300 s external | all decided, 15 SAT, 1,785 solver-UNSAT observations, 253.163 s internal |
| W14 Zerr individual incremental query | PySAT CaDiCaL 1.9.5, 925 assumptions | 240 s external | all decided, 6 SAT, 919 solver-UNSAT observations, 104.086 s internal |
| classification generator | Python exhaustive 23×720 catalogs and 30×720² factors | foreground | completed; 4,740 terms |
| independent generalized verifier | Python physical and matrix replay | 300 s external | PASS, 35.586 s |
| CEGAR outer iterations 0–5 | six clean Python/Z3 processes | 120 s Z3 / 180 s external each | all SAT; build walls 14.10–14.66 s |
| direct X/Z iterations 0–5 | twelve pinned CaDiCaL processes | 600 s internal / 660 s external each | all exit 10 SAT; no timeout |
| raw candidate replay | six clean Python processes | foreground | all PASS; exact walls in `cegar/PROCESS_TIMES.json` |
| proof checker controls | 2× DRAT, 2× LRAT | 60 s internal / 70 s external | valid accepted, truncated rejected |
| pre-seal package verifier | clean Python, full scope | 360 s external | PASS, 121.718 s external |

The twelve direct solver wall times and all exact argv arrays are in the per-iteration compressed `*.run.json.gz` files and `cegar/PROCESS_TIMES.json`.

## Interrupted or failed exploratory processes

These processes produced no verdict and supplied no retained negative fact:

1. A naive exploratory classifier (`explore.py`) exceeded its tool yield. PID 88854 was explicitly terminated and a subsequent process scan found no survivor.
2. Two selector-based weight-14 prototypes were manually interrupted. They were replaced by the time-bounded individual incremental queries. Neither interruption was called UNSAT.
3. A direct-replay invocation under system Python failed at import because `z3` was not installed globally. It produced no replay object and was rerun in the clean pinned environment.
4. The staging assembler failed twice on a Python `str / str` path-construction error and then completed. No repository path existed during these failures.
5. Three pre-seal verifier development runs rejected tuple/list normalization or same-process Z3 SMT identifier differences. `preflight/PRESEAL_AUDITOR_DEBUG.json` records the exact causes and fixes. The final full replay passed. No mathematical data changed in those fixes.

## SAT trace disposition

CaDiCaL was initially given a DRAT output path for every direct query so an unexpected UNSAT result would have a foreground proof trace. All twelve results were SAT. Their streams are not UNSAT certificates and carry no verdict. `cegar/sat_trace_disposition.json` records 811,176,127 bytes of such streams by hash. They were omitted from the sealed payload; complete formulas, assignments, dictionaries, run logs, and physical replays remain.

## Scratch and termination

All scratch was confined to `/tmp/circdist_round69_work_20260829_a`, `/tmp/circdist_round69_package_stage_20260829`, and short-lived verifier/checker temporary directories created with `TemporaryDirectory`. The final procedure copies one sealed directory into the repository, performs an external replay, scans the repository and process table, and deletes all scratch trees. The final outcome of those actions is recorded in `FINAL_AUDIT.txt` and `REPOSITORY_FINAL_INVENTORY.json`.
