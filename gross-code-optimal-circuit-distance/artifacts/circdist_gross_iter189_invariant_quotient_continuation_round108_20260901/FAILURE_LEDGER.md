# Round108 failure ledger

This ledger was frozen before payload sealing. There were **zero scientific failures or UNKNOWN outcomes**. Every solver produced a complete SAT result, every required assignment and physical replay passed, both direct sectors were fully adjudicated, and the fresh frontier checks passed.

## F108-001 — orchestration visibility gaps

During long wrapped stages, the interactive exec transport twice stopped exposing the live session even though the recorded foreground child continued. No replacement computation was overlapped. Retained PID records, completion outputs and later censuses establish that the children exited and were reaped. Disposition: interface-only; no scientific artifact was accepted from an unknown process state.

## F108-002 — pre-execution adaptation defects

Static inspection and `py_compile` caught stale iteration/source-label and assertion-count references while adapting the continuation scripts. The affected drafts were never launched and produced no scientific output. Disposition: corrected before execution; the executed scripts and replay use iteration 189 as input and iteration 190 as the fresh output.

## F108-003 — first frontier-advance launch failed

`verification/logs/process/advance_iter190_full_invariant_frontier.json` records PID 7336, return code 1, 6.575234 seconds, attached, no timeout and reaped. The vendored Z3 directory was not on `PYTHONPATH`; failure occurred before frontier output. Stdout/stderr are retained. The corrected strictly serial retry set `PYTHONPATH=python/site-packages`; PID 7356 returned 0 and was independently replayed. Disposition: fully disclosed execution failure; no output from the failed launch was used.

## F108-004 — proof-control PID fields initially incomplete

The first proof-control wrapper (PID 8220) verified tool behavior but its six nested tool invocations lacked child-PID and reap fields in the JSON result. Before freezing, the control driver was changed to foreground `Popen` calls with exact intervals, timeout/reap/detach fields and expected return codes. The corrected parent PID 9190 and child PIDs 9191–9196 are retained; all six were reaped. A second complete 18-step preseal replay exercised the corrected code. Disposition: FIX-2 metadata defect corrected without changing scientific conclusions.

## Superseded verification runs

The first full preseal replay passed but preceded the F108-004 metadata enhancement. It remains in the process log as a superseded passing run. The final preseal replay is the binding used by `RESULT.json` and the report. Raw SAT search streams were deleted only after deterministic gzip roundtrip checks; descriptors retain raw hashes, byte and LF counts. No raw proof object required for a certificate was deleted because all three results were SAT.

## Scope of process accounting

All solvers, science checkers, replay children, proof-control children, repository-gate children, sealers and final censuses use attached foreground processes with retained PID/interval/outcome records. Read-only inspection and Codex transport orchestration outside those wrappers are not scientific computations and are disclosed here rather than represented as solver evidence. No background or detached compute was used. Final post-root verification records are external by design so that the sealed package is not mutated.
