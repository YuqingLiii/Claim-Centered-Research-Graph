# Failure ledger — Round 116

Every failed or corrected attempt is retained. No failure is converted into scientific credit.

## F116-001 — handoff path mismatch

The dispatch abbreviated the handoff as `circdist/notes/HANDOFF_20260823.md`; the installed file is `research/circdist/notes/HANDOFF_20260823.md`. The first read failed at the abbreviated path. The exact installed file was then read and hash-bound.

## F116-002 — `rg` absent from the clean administrative PATH

The first clean-environment protocol locator invoked `rg`, which was absent from `/usr/bin:/bin:/usr/sbin:/sbin`. Because it appeared in a diagnostic shell pipeline, the shell returned 0 despite the command-not-found text. The command was rerun using the exact bundled `rg` path. No scientific check used the failed locator.

## F116-003 — stale direct-builder reporting constant

The reviewed Round114 direct builder hard-coded `existing_blocks_avoided: 14484`, a stale reporting value unrelated to its generated direct formula. Before building either direct query, the adapted Round116 copy introduced required `--source-block-count 814068` and reported that value. The formulas themselves remained complete unrestricted direct-360 queries. The original and adapted source are both retained.

## F116-004 — free-only selector orbit auditor rejected a nonfree orbit

The inherited Round112 audit assumed 72 distinct selector keys and failed with `assert tk not in orbit_keys` on Xerr after discovering a real stabilizer. Its process exited 1 and its stderr is retained. No exclusion was accepted from that run. A new nonfree-aware auditor recomputed all 72 translated schedules and mechanisms, found orbit size 36 with stabilizer deltas `(0,0)` and `(0,3)`, checked orbit-stabilizer exactly, and passed.

## F116-005 — provisional iter194 schema string incompatible with legacy checker

The first provisional iter194 source used a descriptive new schema label. The inherited registry checker exited 1 solely at its exact schema assertion. That provisional source was never solved, sealed, or used for a claim. The source assembler was corrected to the conventional iteration schema, the entire deterministic source was rebuilt, and translation closure, CSS closure, base compilation, base encoding, and order-144 quotient checks were rerun on the final hashes.

## F116-006 — stale canonical task prose

`frontier.dstar-residual.task` in the canonical Gross YAML still names iteration 192. The installed Round115 evidence/event, exact Round115 review, scheduler authorization, and sealed reviewed Round114 package all bind the fresh unstarted iteration-193 frontier. Lead independently confirmed this is a bookkeeping defect, not scientific ambiguity. This proposer used the exact reviewed iter193 files and did not edit canonical bytes.

## F116-007 — early interface operations lack child-PID capture

Initial read-only file discovery/hash reads and patch creation occurred through the execution interface before the session wrapper was installed. Those were administrative/interface operations, not scientific solver or checker children; exact PIDs are unavailable. Every scientific solver/checker/build/audit after the wrapper was installed has STARTED and REAPED rows with argv, environment, PID, timestamps, return code, and stream paths. This limitation is disclosed rather than retroactively invented.

## F116-008 — provisional Markdown transport markers

The first unsealed document-generation pass retained leading `+` transport markers from the patch representation in multiline Markdown literals. The malformed provisional documents were never sealed or installed. The generator was corrected to remove only line-leading transport markers and the complete document set was regenerated and revalidated before replay.

## F116-009 — failed scratch-source correction command

An attempted shell-quoted Python one-liner to add F116-008 was split by shell metacharacters and exited 1 without modifying the generator. Its exact malformed argv and stderr are retained. The correction was then applied directly to the scratch source, and document generation was rerun from the unchanged scientific evidence.

## F116-010 — source resynchronization met read-only staging files

The first source-resynchronization command attempted to overwrite executable staging copies already mode 0555 and exited 1 at `check_sealed_package_round116.py`. No file content was partially changed. The retry temporarily restored owner write permission within the unsealed staging tree, copied every source byte, restored mode 0555, and then reran package validation.

## F116-011 — cleanup command rejected before execution

An administrative tool call attempted to recreate a documentation snapshot directory using `rm -rf`; host safety rejected the command before any OS process was created or any path changed. A fresh uniquely named snapshot directory was used instead. This was a packaging-interface failure only.

## F116-012 — malformed snapshot copy destination

The first administrative snapshot copy supplied two source operands and `/dev/null`, so `cp` rejected `/dev/null` as a non-directory. It copied nothing. The two exact files were then copied with separate destination paths before final document generation.
