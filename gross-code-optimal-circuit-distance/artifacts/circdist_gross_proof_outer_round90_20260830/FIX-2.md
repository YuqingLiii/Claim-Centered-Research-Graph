# FIX-2 process and scratch closure

## Process model

Round 90 used bounded foreground subprocesses only. No detached child, shell background job, daemon, or OS-level handoff was started.

Science process count: 36 = 12 outer CaDiCaL + 24 direct CaDiCaL. Every command enabled proof output with `--no-binary`, had a 900-second wrapper timeout and an internal 890-second limit, returned SAT code 10, timed out false, and was explicitly waited/reaped. Exact PIDs, parent PIDs, runner PIDs, commands, start/end times, logs, and statuses are in `PROCESS_LEDGER.json` and `logs/*.process.json`.

Actual-Gross trace controls used three further bounded foreground `drat-trim` children. Each returned the expected rejection code 1, timed out false, and was waited/reaped. Fresh package replay uses only deterministic compilers, model verifiers, direct formula builders, DRAT/LRAT fixture checkers, and repository validators; it launches no new Gross SAT search.

## Timeout harvest rule

The wrapper rule was: send TERM at the wall limit, wait at most ten seconds, send KILL if needed, then wait/reap and record the final status. No timeout occurred, so no TERM or KILL was needed.

## Handoffs

`handoffs: []`. No process ownership was transferred. The proposer retains responsibility for all children through final replay and cleanup.

## Scratch ownership and final disposition

Task-owned scratch paths:

- `/tmp/circdist_round90_iter112`: science formulas, full SAT-side proof streams, and temporary transition states;
- `/tmp/circdist_round90_package_build`: pre-install package construction;
- replay `mktemp` directories matching `/tmp/circdist-r90-replay.*`.

The only durable output is the single installed package `circdist/artifacts/circdist_gross_proof_outer_round90_20260830`. The science and build scratch paths were deleted with Python `shutil.rmtree` after pre-seal replay; replay directories were removed by the replay trap. `verification/fix2_closure.json` confirms those paths and the accidental wrong-workspace path are absent. The survivor scan covers `circdist_round90`, `cadical`, `drat-trim`, and `lrat-check`. Any scan command itself is distinguished from a task process.

## Closure requirements

Final response is permitted only after all of the following are true:

1. package manifests and installed replay pass;
2. protected scheduler/node/review/Round88 seal hashes still match;
3. repository validators have recorded dispositions;
4. evidence closure fails only for the expected new unlinked Round90 package;
5. all task scratch is absent;
6. no task solver/checker/replay process survives;
7. no commit and no push occurred.
