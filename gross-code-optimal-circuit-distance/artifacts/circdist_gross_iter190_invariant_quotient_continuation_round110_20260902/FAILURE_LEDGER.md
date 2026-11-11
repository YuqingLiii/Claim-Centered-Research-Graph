# Round110 failure ledger (live scratch)

## F110-001 — first solver wrapper launch rejected before child creation

The first invocation of `run_process_round110.py` accidentally supplied two separator tokens. The wrapper interpreted the second literal `--` as the executable and Python raised `FileNotFoundError` before any solver child was created. No scientific computation ran and no formula output or conclusion was produced. The empty prelaunch streams are retained under `logs/failures/F110-001/`; the corrected launch uses one separator. Classification: harness/orchestration, pre-science.

## F110-002 — first model replay lacked vendored Z3 on PYTHONPATH

The first post-SAT model replay used a clean environment without the sealed package's `python/site-packages` on `PYTHONPATH`. After independently reparsing the SAT model and writing a partial duplicate assignment, import of the frozen `outer.py` failed with `ModuleNotFoundError: z3`; no candidate or replay verdict was written. PID 14772 returned 1 after 17.072876 seconds and was reaped without timeout or signals. Its process record, streams, and partial assignment are retained under `logs/failures/F110-002/` and are not used scientifically. The retry adds only the reviewed sealed Z3 path and reruns the whole stage from the solver log. Classification: harness/environment; scientific conclusion unchanged.

## F110-003 — copied checker retained sealed read-only mode during adaptation

A preparatory copy of the reviewed independent direct-audit source preserved its 0555 mode. The first text-relabel adaptation attempt raised PermissionError before changing bytes; a subsequent static grep showed all old labels still present, and py_compile merely compiled the unchanged source. No scientific checker was launched and no result file was produced. The copied scratch file is made writable, adapted, re-grepped, and compiled before execution. Classification: pre-execution harness/adaptation; no scientific consequence.

## F110-004 — one corrective orchestration command was policy-rejected before execution

The first combined corrective shell command included recursive cache removal syntax and was rejected by the command interface before process creation. It changed no byte and launched no child. The corrected command uses an in-memory compile check and no recursive removal. Classification: interface-only pre-execution rejection.

## F110-005 — first incremental-checker relabel pass cascaded two replacements

Static grep caught that a broad new-frontier replacement had also changed the reviewed old input path from iter190 to iter191, and likewise changed the old-source schema assertion to iteration191. The checker was not executed and produced no evidence. Both old-input bindings were restored to iteration190 before an in-memory compile check and execution. Classification: pre-execution adaptation, caught by static validation.

## F110-006 — post-fix grep predicate falsely flagged the required round108 input path

After F110-005 was fixed, the broad forbidden-label grep still treated the intentionally retained inputs/round108 binding as stale and returned 1. This was a static harness false positive; the source itself had the correct old iter190 and new iter191 bindings. A field-specific assertion replaces the broad predicate. No scientific child ran.

## F110-007 — first iter191 quotient checker launch lacked vendored Z3

The first independent quotient reconstruction launch omitted the reviewed sealed python/site-packages path. It streamed and structurally inspected the formulas, then failed when its physical orbit cross-check imported frozen outer.py and could not import z3. PID 15660 returned 1 after 14.069097 seconds, was reaped, and wrote no independent-check result. The process record and streams are retained and excluded from evidence. The full checker is retried with the same inputs and only the sealed Z3 path added. Classification: harness/environment, no scientific verdict.

## F110-008 — iteration-189 registry checker was inapplicable to reviewed iteration 190

The copied `check_input_registry_invariance_round108.py` is intentionally hard-coded to the iteration-189 source schema and 24,300 selectors. It was mistakenly launched against the reviewed iteration-190 input, where PID 16007 rejected the schema assertion after 13.344037 seconds, returned 1, and was reaped without timeout or signals. It wrote no result and made no scientific claim. The process record and streams are retained; a new parameterized Round110 checker reruns the complete action/registry audit with explicit iteration-190, 517,140-block, 24,444-selector, and 545,982-assertion bindings. Classification: harness/checker selection; no scientific verdict.

## F110-009 — census pattern `work` was overbroad

The first preseal census used `root.name` as a process pattern; the scratch package directory is literally named `work`, which also occurs inside many macOS `Frameworks` command paths. PID 16618 therefore conservatively rejected a large false-positive list, returned 1 after 0.090206 seconds, and was reaped. It found no evidence of a Round110 survivor and wrote no accepted census result. The retry uses the distinctive scratch-parent name and exact tool executable names. Classification: process-harness false positive; no scientific consequence.

## F110-010 — first atomic rename attempted with a read-only directory root

The first installation child attempted to rename the fully sealed scratch directory while its root mode was `0555`. On macOS, moving a directory between parents requires the directory root to be writable so that its parent linkage can change. PID 16761 therefore returned `EACCES`/1 after 0.023984 seconds; the destination did not exist before or after the attempt, and the repository received zero bytes. The package was reopened only to retain this record and update the failure ledger, then resealed and independently reverified. The corrected atomic child temporarily gives only the scratch root owner-write permission, performs one same-device `os.rename`, and immediately restores destination root mode `0555`; file bytes and manifest identities remain protected. Classification: packaging/install harness; no scientific consequence and no partial repository installation.
