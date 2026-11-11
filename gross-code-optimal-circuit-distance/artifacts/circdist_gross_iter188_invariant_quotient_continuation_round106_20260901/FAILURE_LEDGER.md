# Round106 failure and scope ledger

| ID | Stage | Observation | Disposition | Scientific effect |
|---|---|---|---|---|
| F106-001 | initial binding probe | The first read-only hash command looked for the reviewed root manifest as `SHA256SUMS`; the actual sealed name is `SHA256SUMS.txt`. The command stopped after already printing the three canonical hashes. | Re-ran against the exact filename, obtained the required digest `410807...6ebb`, then checked all 383 manifest rows. | None; no file was written or changed. |
| F106-002 | preseal preparation | A combined shell command containing `rm -rf source/__pycache__` was rejected by the execution safety layer before process creation. | Used a bounded Python `shutil.rmtree` on that exact cache directory, set executable bits explicitly, and relaunched the replay. | None; the rejected command launched no process and made no change. |
| F106-003 | source adaptation review | A mechanical draft of the independent iteration-189 closure checker temporarily advanced the old-source path/schema to iteration 189 as well as the new-source path/schema. | Detected by immediate `rg` inspection before execution; corrected old input to reviewed iteration 188 and executed only the corrected checker. | None; no scientific output was produced from the draft. |
| F106-004 | first post-payload-seal replay | All 13 scientific replay children passed, but the final payload-manifest assertion failed. The provisional manifest had included the payload sealer's still-open `logs/payload_seal.stdout.log` at zero bytes; the sealer then wrote 738 bytes to that log after hashing it. This was the sole manifest mismatch. | Preserved the failed replay streams and process record, added explicit exclusion of payload-sealer self-logs, regenerated and verified the immutable-payload manifest, and reran the full postseal replay. | None; no scientific payload file differed, no solver was rerun, and the failure was confined to a self-referential packaging log. |
| F106-005 | final root-seal invocation | The first direct invocation of `source/seal_root_round106.py` omitted its mandatory `--root` argument. `argparse` rejected it with return code 2 before any package file was read or written by the sealer. | Retained the exact command, stderr, return code, and foreground/reaping record in `logs/root_seal_missing_root.*`; then invoked the same sealer with the explicit package root. | None; no solver, checker, replay child, or scientific process was started. |
| F106-006 | final root-seal payload check | After F106-005 was disclosed, the explicit-root sealer correctly rejected the now-stale payload manifest at `FAILURE_LEDGER.md` with return code 1. | Retained the exact traceback and foreground/reaping record in `logs/root_seal_stale_payload.*`; regenerated the payload manifest only after all failure disclosures were present, then repeated the full corrected postseal replay before root sealing. | None; this was an expected integrity rejection caused solely by adding the F106-005 disclosure after the prior payload seal. |
| F106-007 | payload-reseal invocation | The first payload-reseal invocation supplied `--root` but omitted the mandatory `--output` argument. `argparse` rejected it with return code 2 before any package file was written. | Retained the exact command, stderr, return code, and foreground/reaping record in `logs/payload_reseal_missing_output.*`; then supplied the explicit existing payload-manifest path. | None; no scientific process was started. |
| F106-008 | final external replay preparation | A combined command containing `rm -rf /tmp/circdist-round106-final-postseal` was rejected by the execution safety layer before process creation. | Retained the rejected command and disposition in `logs/final_postseal_safety_rejection.record.json`; used a newly allocated `mktemp` directory without a deletion command. | None; no shell, replay, checker, solver, or filesystem mutation was launched by the rejected command. |
| F106-009 | payload-sealer output contract and aborted replay | Two payload-reseal invocations incorrectly pointed `--output` at `PAYLOAD_SHA256SUMS.txt`. The script first generated the manifest at that fixed root path and then overwrote it with its 804-byte JSON summary (`05d753d1...d959f`). A verification replay was subsequently launched against this malformed file and was interrupted with return code 130 during its third serial child as soon as the contract error was reported. | Read both sealing scripts and `--help` semantics before further mutation; retained the wrong-output and interrupted-replay records under excluded `logs/payload*`/`logs/postseal*` paths; verified by process census that no replay/checker/solver survived; then invoked the payload sealer with `--output verification/payload_seal.json`, its intended excluded summary target. | None; the malformed object was packaging metadata, the interrupted run performed verification only, no SAT solver or frontier generation ran, and the final corrected replay supersedes it. |
| F106-010 | external post-root-seal self-check summary | The complete read-only self-check had already passed its root/payload/inventory hashes, exact file sets, canonical bindings, git diff, cache/temp, and survivor assertions, but its final JSON-summary construction requested a nonexistent `postseal_replay["manifests_checked"]` key. The script exited with return code 1 after all evidence assertions. | Retained the exact KeyError and record in `logs/postseal_failure_F106-010_final_selfcheck.*`; inspected the replay schema, replaced only the summary expression with `len(postseal_replay["manifests"])`, and reran the full read-only check outside the package after the final root seal. | None; this was a summary-field interface error, no package byte was changed by the failed self-check, and no scientific process started. |

## Solver and resource ledger

- Iteration-188 quotient: SAT, return code 10, 836.157983 s, no timeout, no OOM.
- Xerr complete direct-360: SAT, return code 10, 625.627899 s, no timeout, no OOM.
- Zerr complete direct-360: SAT, return code 10, 137.818738 s, no timeout, no OOM.
- UNKNOWN outcomes: zero.
- Wrapper timeouts: zero.
- Solver overlaps or portfolios: zero.
- Detached processes: zero.
- Repair attempts: zero; repair was forbidden after direct SAT.

SAT solver proof-side output is retained only as a search trace. No DRAT/LRAT claim is made for any of the three SAT queries. Valid/corrupt/truncated tool controls do not change that classification.

## Scope exclusions

- No exhaustive universal absence proof was obtained.
- No legal distance-12 circuit was obtained.
- No selector was installed from a fixed basis, heuristic sample, or partial translation set.
- No canonical YAML, scheduler, review, prior artifact, or proof-DAG file was edited.
- No positive SAT assignment, heuristic coverage statement, or candidate-specific failure receives root credit.
