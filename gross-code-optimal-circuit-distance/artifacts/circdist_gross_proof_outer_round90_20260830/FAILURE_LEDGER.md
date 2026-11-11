# Failure ledger

No failed artifact contributes to the verdict. Accepted evidence is only the formula/model/replay/state set sealed by the package manifests.

## F-01 — inherited Round88 protected checker expected an older canonical node

- Stage: initial binding audit.
- Action: the complete Round88 root/payload manifests were independently checked successfully. Its package-local `check_protected.py` was also invoked against the live repository.
- Failure: that old checker expected the pre-Round89 `CIRCDIST.gross.yaml` hash, while the canonical node had lawfully advanced in Round89.
- Effect: nonzero checker exit due solely to the stale protected-hash expectation; no science formula was built or solved from this failure.
- Resolution: Round90 independently bound the current scheduler, node, Round89 review, Round88 root seal, and Round88 payload seal in `INPUT_BINDINGS.json`. Package-local `source/check_protected.py` checks those current bindings.
- Evidentiary status: excluded.

## F-02 — destructive shell cleanup command rejected before execution

- Stage: scratch preparation.
- Action: an attempted shell command included recursive removal syntax for a `/tmp` path.
- Failure: the command was rejected by the execution policy before it ran.
- Effect: no filesystem change and no science state mutation.
- Resolution: all scratch cleanup uses `pathlib`/`shutil.rmtree` on exact task-owned paths.
- Evidentiary status: excluded.

## F-03 — transition writer initially required weight exactly ten

- Stage: iteration 115 transition, after outer SAT and both direct solves, before state write.
- Action: the first transition-writer version asserted every positive direct mechanism had `fault_count==10`.
- Failure: iteration 115 Zerr is a valid complete `W<=10` solution of weight 9, so the assertion stopped the writer.
- Effect: the process terminated before writing the next state, record, or source. The candidate, direct formula, assignment, and physical replay remained valid. No partial selector update occurred.
- Resolution: the exact logical contract was corrected to `1<=fault_count<=10`. Iteration 115 was replayed from its unchanged prefix and committed only after both sectors passed. The same contract correctly accepted iteration 119 Xerr at weight 9.
- Evidentiary status: failed writer run excluded; corrected source and complete atomic replay are sealed.

## F-04 — result cross-check initially misread a list field

- Stage: package consistency checker development.
- Action: the first `check_result.py` version compared `RESULT.iterations[*].new_selectors` with integer `2`.
- Failure: the durable result schema stores the exact two-element mechanism-ID list, so the checker assertion stopped.
- Effect: no formula, model, replay, or state changed.
- Resolution: require exact equality with `record.new_selectors` and separately require list length two. The corrected checker passed for all twelve iterations and is part of full replay.
- Evidentiary status: failed checker attempt excluded; record in `verification/failures/package_crosscheck_schema_mismatch.json`.

## F-05 — validator helper was first written in the unrelated initial workspace

- Stage: repository-validator packaging.
- Action: a relative patch target resolved under the session's unrelated initial workspace rather than the mandated `Claim-Centered-Research-Graph` repository.
- Failure: the subsequent invocation in the mandated repository returned code 2 because the helper was absent there.
- Effect: only one helper source file was created outside the target repository; it never ran. No science or canonical file changed.
- Resolution: the stray file and empty Round90 directory were removed and their absence checked; the helper was written explicitly under the single authorized package.
- Evidentiary status: excluded; record in `verification/failures/wrong_workspace_helper.json`.

## F-06 — duplicate-YAML scan first used an interpreter without PyYAML

- Stage: first repository-validator pass.
- Action: the validator wrapper selected the recorded Z3/PySAT venv for the duplicate-key helper.
- Failure: that venv lacks PyYAML, so import failed with code 1 before scanning.
- Effect: no YAML verdict was produced and that first validator set was not accepted.
- Resolution: rerun with `/usr/bin/python3`, the repository validator environment. It scanned 777 YAML/YML files and 20,291 mappings, found zero duplicate keys, and the complete validator set passed.
- Evidentiary status: failed tool attempt excluded; record in `verification/failures/duplicate_yaml_wrong_interpreter.json`.

## Absences from the failure set

There was no solver timeout, UNKNOWN, OOM, verifier rejection, DIMACS clause failure, semantic schedule failure, direct physical-replay failure, state-hash collision, or accepted-proof failure. All 36 science solver children returned SAT code 10 and were reaped. The three actual-trace checker failures are deliberate negative controls, not development failures: `drat-trim` correctly rejected a SAT-side stream and its corrupt/truncated variants.

