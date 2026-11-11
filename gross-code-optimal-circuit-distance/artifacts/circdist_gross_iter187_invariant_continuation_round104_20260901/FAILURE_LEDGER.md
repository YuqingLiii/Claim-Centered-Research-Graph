# Round104 failure and scope ledger

## Scientific disposition

No solver timed out, returned UNKNOWN, was killed, or suffered an OOM. All
three exact queries returned SAT (`10`) and all complete assignments passed.
The three proof-output streams contain no empty-clause record and are retained
as SAT traces only; they are not DRAT or LRAT certificates.

No distance-12 claim, absence claim, exhaustion claim, universal ceiling,
repair, or root promotion is made. Repair was forbidden because both complete
unrestricted direct sectors were SAT.

## Recorded failures and corrections

| ID | failure | scientific reach | correction and retained evidence |
|---|---|---|---|
| F104-001 | The initial Round102-manifest wrapper command pointed at a nonexistent relative runner path. | No scientific child launched. | The absolute-path rerun checked the complete 724-row Round102 root manifest and passed; `logs/process/verify_round102_root_manifest.json`. |
| F104-002 | The first frozen SAT replay lacked vendored `z3` on `PYTHONPATH` and exited 1. | Clause/model construction had not failed; this was an import error. | The exact sealed Python runtime was copied, the corrected PID-recorded replay passed, and both records are retained as `replay_iter187_quotient_sat_frozen*.json`. |
| F104-003 | A first version of the new independent checker used `int.bit_count()`, unavailable in the host Python 3.9. | It stopped during geometry reconstruction before opening either direct CNF. | Replaced with a portable population count. The overwritten record was recovered transparently from the captured wrapper transcript under `logs/recovered/`. |
| F104-004 | A log-renaming helper raised `TypeError` before preserving F104-003 in place. | No scientific process launched. | The exact PID/times/status/traceback were reconstructed as provenance, explicitly marked recovered rather than original. |
| F104-005 | The portable direct checker initially assumed stabilizer ranks 60/60 instead of the correct 66/66. | It stopped at the independent algebra check before reading the direct CNFs. | The reaped failure is `logs/process/independent_iter187_direct_stdlib_audit_failed_rank_assumption.json`; the corrected checker proves ranks 66/66, normalizer ranks 78/78, and logical pairing rank 12. |
| F104-006 | The first pre-seal replay compared the volatile bind-time `cwd` field. | All immutable binding hashes had passed; replay stopped before later checks. | The comparison now excludes only `created_utc` and `environment.cwd`; the failed and successful PID records are both retained. |
| F104-007 | A live-governance smoke check searched for `status: CONJECTURED`, while the canonical schema uses `level: CONJECTURED`. | Unlogged smoke check only; canonical bytes were already hash-bound. | Corrected key; the full logged ten-child repository suite passed. |
| F104-008 | Early compact inspection commands used two wrong shorthand paths and one wrong JSON key. | Reporting/inspection only; no evidence mutation or scientific inference. | Subsequent exact-path binding and schema-aware inspection passed. |
| F104-009 | One attempted cleanup command was rejected by the shell safety layer before process creation. | No process launched and no file changed. | A safe fixed `/tmp` comparison file was used. |

`logs/recovered/orchestration_failure_notes.json` discloses the unwrapped
inspection/orchestration events. The authoritative PID ledger covers every
solver, scientific verifier, replay child, repository validator, and final
census child.

## Scope limitations

1. SAT of a lex quotient proves only existence of a representative satisfying
   the installed invariant formula.
2. The two direct SAT mechanisms disqualify this candidate as a distance-12
   witness; they do not prove a global distance-11 ceiling by themselves.
3. Adding sound selector orbits removes schedules retaining those exact
   mechanisms. It does not prove that the fresh frontier is UNSAT.
4. Proof-tool controls validate the tools and rejection paths, not the SAT
   trace streams.
5. The iteration-188 quotient is checked and unstarted. No conclusion is drawn
   from an unrun formula.

