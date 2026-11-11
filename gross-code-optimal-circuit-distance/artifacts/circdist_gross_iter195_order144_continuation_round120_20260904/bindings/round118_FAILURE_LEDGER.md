# Failure ledger — Round 118

Every row below is a retained false start. No failed run contributes positive evidence.

| ID | process tag / interface event | rc | failure | correction and final disposition |
|---|---|---:|---|---|
| F118-001 | `audit-iter194-order144-orbit-controls` | 1 | The inherited order-72 checker required 71 trace rows; the reviewed quotient has 143. | Adapted only the group enumeration/root expectations to the reviewed order-144 construction; the full all-clause/orbit checker passed. |
| F118-002 | `adapt-order144-orbit-auditor` | 1 | The copied source retained sealed mode 0444. | Changed permissions on the scratch copy only, then applied and hashed the adaptation. No sealed input changed. |
| F118-003 | `audit-iter194-css-duality-and-registry-gap` | 1 | The iter193 auditor asserted its old block/selector counts. | Used the reviewed iter194 auditor with exact 814,392/50,832 counts; it passed. |
| F118-004 | `read-new-orbit-summary` | 1 | A non-scientific display probe called `len()` on an integer summary field. | Corrected the display-only query; scientific orbit evidence was unaffected. |
| F118-005 | `check-iter195-translation-registry` | 1 | The first frontier draft used a novel `full-order144-closure` schema label rejected by the established checker. | Restored the established `full-translation-closure` label, regenerated the entire source/state/audit, and reran translation/CSS/base/quotient checks successfully. The rejected draft is not the retained frontier. |
| F118-006 | `recover-advance-command` | 1 | A display query searched for a nonexistent tag. | Located the command by executable path; no scientific output changed. |
| F118-007 | `check-iter195-order144-quotient` | 1 | The gzip build trace was initially named with a `.json` suffix, so the checker treated compressed bytes as UTF-8. | Renamed the unchanged bytes to `.json.gz`; the full quotient check passed. Final package uses `trace.json.gz`. |
| F118-008 | `run-iter195-unstarted-audit` | 1 | The first auditor required a `solver_invocations` state key not present in the established frontier schema. | Audited `started=false`, the complete process ledger, and the artifact tree; final result is zero solver invocations and zero solver/model/assignment/proof artifacts. |
| F118-009 | early interface inspection | n/a | A few initial read-only shell/interface operations and scratch-directory setup preceded the inner child ledger. | Disclosed in `ADMIN_INTERFACE_OPERATIONS.json`; no solver, checker, formula mutation, or durable evidence write occurred there. All scientific subprocesses are ledgered and serialized. |
| F118-010 | `write-round118-package-docs` | 1 | The first documentation writer referenced nonexistent quotient-metadata key `nonidentity_elements`. | Used the established keys `symmetry_nonidentity_roots` and `symmetry_group_order`, reran the writer, then independently validated `RESULT.json`. No scientific evidence changed. |
| F118-011 | `sync-final-session-logs` | 0 | This administrative copy accidentally used scratch lock pathname `scienced.lock` instead of the canonical `science.lock`. No other child was active, so serialization was not violated, but the empty lock file was copied into the session-log snapshot. | Removed the stray package lock file, reran final log synchronization under `science.lock`, and retained this disclosure. No science or evidence content changed. |

Expected solver rc=10 for SAT is not a failure. No child was killed, detached, or left unreaped. The repair/gap branch was not attempted because its required antecedent was false.
