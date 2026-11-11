# Round-54 author command, process, and FIX-2 ledger

## Authority and write boundary

Role: fresh strict-serial proof-certificate author for `CIRCDIST.sat.instances`; proposer only. No canonical assessment or route/node edit was authorized or made.

The only durable path created by this author is:

```text
circdist/artifacts/circdist_sat_instances_proof_certificates_20260826/
```

All temporary scripts and prototype data used `/tmp/circdist_sat_instances_cert_r54/`. They were not imported by the final verifier and were deleted before sealing. No network request, plugin, background command, detached command, scheduler mutation, or subagent was used.

The surrounding recovered repository checkout was already broadly untracked/dirty at entry, so a global clean-index assertion would be false and uninformative. Write-boundary enforcement instead used explicit absolute output paths, source hashes recorded in `source_audit.json`, a final source-hash comparison, and an inventory of the one new package directory. All canonical nodes, reviews, operations files, protocols, tools, generated views, old logs, and migration records were read-only.

## Environment

```text
Date: 2026-08-26
Host OS: Darwin 25.6.0 arm64
Python: 3.9.6
Shell used for orchestration: zsh/sh
Network: unused
External Python dependencies in final verifier: none
```

## Read-only source audit

The author read, in strict serial order, the repository protocols, frozen problem/rescope definitions, current instances/window/transfer/root nodes, the full instances dossier and independent review, the instances-window edge review, the downstream rebind review, the self-contained window proof/review, the transfer proof/end-to-end review, the exact-text/bridge reviews, every load-bearing proposer/reviewer program identified by those records, and the Stim cross-validation package.

Representative read/search commands were:

```sh
sed -n '<range>p' DAG_PROTOCOL.md
sed -n '<range>p' FILE_PROTOCOL.md
sed -n '<range>p' circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md
sed -n '<range>p' circdist/artifacts/definitions/SAT_RESCOPE_20260822.md
sed -n '<range>p' circdist/proof-dag/nodes/CIRCDIST.sat.{instances,window,transfer}.yaml
sed -n '<range>p' circdist/artifacts/circdist_sat_instances_20260823.md
sed -n '<range>p' circdist/reviews/circdist_sat_instances_review_20260823.md
sed -n '<range>p' circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md
sed -n '<range>p' circdist/reviews/circdist_sat_window_downstream_scope_rebind_review_20260826.md
rg -n '<definition/function/claim>' <the files above and archived source programs>
find circdist/artifacts/logs_circdist_sat_instances_20260823 -type f
find circdist/artifacts/logs_circdist_sat_instances_review_20260823 -type f
find circdist/artifacts/logs_circdist_stim_crossval_20260823 -type f
```

The exact inspected-file digests are in `source_audit.json`. The archived manifest checks were equivalent to:

```sh
(cd circdist/artifacts/logs_circdist_sat_instances_20260823 && shasum -a 256 -c SHA256SUMS.txt)
(cd circdist/artifacts/logs_circdist_sat_instances_review_20260823 && shasum -a 256 -c SHA256SUMS.txt)
(cd circdist/artifacts/logs_circdist_stim_crossval_20260823 && shasum -a 256 -c SHA256SUMS.txt)
```

Results: 247/247, 29/29, and 17/17 entries verified respectively. These results were treated as provenance, not proof.

## Authoring and proof-object construction

1. A temporary standard-library GF(2)/Clifford prototype reconstructed all three codes and schedules.
2. It generated every projected elementary fault, compared forward and backward signatures, and ran exhaustive meet-in-the-middle lower tests for all 28 cells.
3. It searched only for explicit upper witnesses of already-excluded weights, enforcing distinct occupied physical locations.
4. The durable `model.py` was then written inside the package, and JSON objects were generated from it by a temporary author script.
5. `verify.py` was written independently of the JSON generation control flow. It reconstructs all formulas and reruns every load-bearing computation.
6. `WITNESS_INDEX.md` was rendered from the immutable witness objects for human audit.

Principal authoring commands:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B -m py_compile circdist/artifacts/circdist_sat_instances_proof_certificates_20260826/model.py
PYTHONDONTWRITEBYTECODE=1 python3 -B /tmp/circdist_sat_instances_cert_r54/generate.py
PYTHONDONTWRITEBYTECODE=1 python3 -B /tmp/circdist_sat_instances_cert_r54/witness_index.py
python3 -B circdist/artifacts/circdist_sat_instances_proof_certificates_20260826/verify.py
```

The temporary generator used PyYAML only to read and serialize the exact current canonical claim/route strings. The final verifier does not use PyYAML: it checks those serialized strings against hard-coded lengths and hashes with the standard library.

## Corrected attempts and rejected routes

All corrections were made before the sealed final run. None is hidden as a successful certificate.

1. **Python-version portability.** The first scratch prototype used `int.bit_count`, absent in the available Python 3.9 runtime. It was replaced by exact `bin(x).count("1")`. No result object from the failed run survived.
2. **Sector display tag.** An early scratch serializer labeled the retained component backward. The propagation itself was correct, but the public label was wrong. It was corrected to Z-memory keeps X and X-memory keeps Z, then all effects were regenerated. No mislabeled object survived.
3. **Class-D measurement bound.** An early scratch assertion asked whether the flagged supermodel found a goal through weight 4 for an exclusion that only needs weights through 3. It was corrected to certify `>=4`, with an independent explicit weight-4 flagged upper. No overstrong exclusion survived.
4. **Surface effect-class erratum.** Reconstruction produced 77, not 78, one-round nonzero signatures. Inspection confirmed the old dossier's own corrected table and current caveat say 77. The package uses 77 and never imports the stale phrase.
5. **BB no-hook upper.** The first supplied BB logical basis vector is valid but need not be minimum weight. Using it as a bare upper failed the asserted weight-4 target. `bare_logical_witness` was changed to exhaust the exact kernel modulo the stabilizer span and choose the lexicographically first minimum static logical. It then replayed at weight 4 in both sectors. The failed nonminimal witness was discarded.
6. **Opaque-solver route rejected.** Old MILP, Stim, and min-plus logs were inspected but never converted into proofs. Solver termination and archived verdicts do not enter acceptance.
7. **Temporal-boundary overclaim rejected.** The certificate includes every ideal boundary equation but does not infer global absence of temporal-boundary mechanisms. The route's exact scoped caveat is preserved.

## Final proof verification

Exact command, run from the package directory:

```sh
python3 -B verify.py
```

Captured in `verifier_output.txt`. Result:

```text
5/5 scope hashes
3/3 exact instances; 268 gates
10,296 full physical assignments; 2,382 retained generators
28/28 distance cells; 78 lower exact-weight exclusions
30,060 forward/backward fault-pair equalities
354 restricted subset tests; 28 flagged-measurement supermodel tests
102 full-symplectic upper replays
14/14 aggregate first-d cells
4/4 negative controls rejected
VERIFIER RESULT: PASS
```

## Read-only repository validation

The exact commands and outputs are captured in `repository_validation.txt`:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B tools/proof_dag_check.py --problem circdist
PYTHONDONTWRITEBYTECODE=1 python3 -B tools/proof_dag_check.py --problem all
PYTHONDONTWRITEBYTECODE=1 python3 -B tools/evidence_closure_check.py --problem circdist
PYTHONDONTWRITEBYTECODE=1 python3 -B tools/evidence_closure_check.py --problem all
PYTHONDONTWRITEBYTECODE=1 python3 -B tools/check_circdist_migration.py
git diff --check
git status --short -- circdist/artifacts/circdist_sat_instances_proof_certificates_20260826
```

Structural DAG checks pass for circdist and all projects. Migration preservation passes. `git diff --check` passes. Evidence-closure checks report this new author package as unlinked. That is the expected pre-review state: the author is forbidden to edit a canonical evidence list, and linking is a dispatcher action after independent review. The closure failure is recorded, not suppressed or misreported as a pass.

## FIX-2 process accounting and cleanup

All computational commands were foreground commands with bounded waits. No shell `&`, `nohup`, detached session, job scheduler, persistent terminal, or child agent was launched. Every command returned an exit status before the next dependent mutation.

Final cleanup/audit commands:

```sh
rm -rf /tmp/circdist_sat_instances_cert_r54
ps -axo pid,ppid,state,command | rg 'circdist_sat_instances_cert_r54|circdist_sat_instances_proof_certificates_20260826/(verify|model)\.py'
find circdist/artifacts/circdist_sat_instances_proof_certificates_20260826 -maxdepth 1 -type f -print | LC_ALL=C sort
```

Surviving-process declaration: after cleanup, there were **zero author-launched verifier, generator, prototype, solver, Stim, MILP, or background processes**. A process search may momentarily show only the search command itself; it is not a survivor. Scratch declaration: `/tmp/circdist_sat_instances_cert_r54` does not exist at seal time.

## Manifest rule

After every other package file reached final bytes, the manifest was generated once by:

```sh
cd circdist/artifacts/circdist_sat_instances_proof_certificates_20260826
find . -type f ! -name SHA256SUMS -print | LC_ALL=C sort | while IFS= read -r f; do shasum -a 256 "$f"; done > SHA256SUMS
shasum -a 256 -c SHA256SUMS
```

The manifest deliberately excludes itself and covers every other regular file. No file was edited after the successful manifest check.
