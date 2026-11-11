# Round100 failure ledger

All 12 rejected or failed attempts known to this proposer are listed. Failed partial outputs support no scientific or package verdict.

## F001 — pre-science binding audit

**Attempt.** Read a guessed formulas/iter172/source.json path.

**Failure.** FileNotFoundError; the commissioned source is source.json.gz.

**Correction.** Used the manifest-bound gzip path and completed the prior-package manifest check.

**Effect.** None; no solver or model was run and partial output supports no verdict.

**Evidence.** `FAILURE_LEDGER.md`

## F002 — synthesis independent validation

**Attempt.** Initial direct-Z3 span validator used positional Xor with more than three arguments under z3 5.1.0.

**Failure.** API arity exception, return code 1, before solver.check().

**Correction.** Replaced it with an explicit binary left fold and reran both sectors to checked UNSAT.

**Effect.** The failed attempt produced no SAT/UNSAT result and supports no theorem.

**Evidence.** `failures/F002_span_validator_z3_api/`

## F003 — read-only source audit

**Attempt.** A line-extraction helper requested one line past the source length.

**Failure.** IndexError in an inspection-only loop.

**Correction.** Bounded the extraction to the actual line count.

**Effect.** None; no file mutation and no scientific process.

**Evidence.** `FAILURE_LEDGER.md`

## F004 — audit authoring

**Attempt.** A generated audit draft contained a placeholder source hash.

**Failure.** Manual pre-execution review rejected the draft.

**Correction.** Replaced the placeholder with the commissioned exact source binding before first execution.

**Effect.** None; rejected code never executed.

**Evidence.** `FAILURE_LEDGER.md`

## F005 — compression authoring

**Attempt.** First Round100 compressor draft had a malformed f-string.

**Failure.** py_compile SyntaxError before compression.

**Correction.** Corrected the delimiter, recompiled, then compressed all 222 streams with byte-roundtrip checks.

**Effect.** None; no evidence file was compressed by the failed draft.

**Evidence.** `FAILURE_LEDGER.md`

## F006 — preseal replay attempt 1

**Attempt.** Replay resolved the virtual-environment Python symlink to its base interpreter.

**Failure.** First physical replay could not import z3 after 28 successful binding/compression/formula children; replay child 29 returned 1.

**Correction.** Preserved the supplied interpreter path with absolute() rather than resolve().

**Effect.** All 13 formula replays passed; the incomplete run supports no package verdict.

**Evidence.** `failures/F006_replay_venv_resolution/`

## F007 — preseal replay attempt 2

**Attempt.** The immutable science audit counted later packaging process records.

**Failure.** Hard-coded 204 science-record assertion failed after 123 successful direct replay children and 12 proof grandchildren.

**Correction.** Explicitly separated the closed 204-record science census from later round100_* packaging records.

**Effect.** Every science and synthesis replay stage through the mixed-sector theorem passed; incomplete package run supports no final replay verdict.

**Evidence.** `failures/F007_replay_science_census_scope/`

## F008 — mixed-sector checker authoring

**Attempt.** Toy cardinality control used int.bit_count under the system Python.

**Failure.** AttributeError before the checker result.

**Correction.** Used bin(value).count("1") and reran all 256 controls to PASS.

**Effect.** None; proof statement and science artifacts were unchanged.

**Evidence.** `FAILURE_LEDGER.md`

## F009 — read-only CLI inspection

**Attempt.** Invoked validate_span.py --help with system Python lacking z3.

**Failure.** Import-time ModuleNotFoundError; no validation was requested or run.

**Correction.** Used the bound z3-capable environment for all actual span validations.

**Effect.** None; this was a help probe.

**Evidence.** `FAILURE_LEDGER.md`

## F010 — read-only binary inspection

**Attempt.** Invoked order6_mitm with no arguments to obtain its usage string.

**Failure.** Expected usage exit; no input was read.

**Correction.** All theorem runs supplied INPUT ELIGIBLE SUMMARY SECTOR.

**Effect.** None; this was a usage probe.

**Evidence.** `FAILURE_LEDGER.md`

## F011 — packaging edit

**Attempt.** An apply_patch request tried delete-and-add operations on one path.

**Failure.** Patch tool rejected the request without changing a file.

**Correction.** Wrote the draft, then compiled and corrected it before execution.

**Effect.** None; no OS science process and no artifact mutation from the rejected patch.

**Evidence.** `FAILURE_LEDGER.md`

## F012 — first sealed-replay launch

**Attempt.** The launch setup included an rm -rf cleanup of a proposed external replay directory.

**Failure.** The host command policy rejected the command before creating an OS process.

**Correction.** Used a fresh unique directory and no deletion command; the sealed replay then passed with 145 known children.

**Effect.** None; the rejected launch did not execute and did not touch the package or filesystem.

**Evidence.** `FAILURE_LEDGER.md`

## Prior-round disclosure

Round98 had three post-science model-capacity interruptions. They are disclosed here but are not inherited as Round100 failures.
