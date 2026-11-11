# FIX-2 exhaustive disposition

All 72 material CEGAR processes are individually sealed in `PROCESS_LEDGER.json` and in per-iteration run records: 12 outer builds, 12 independent outer replays, 24 direct solver calls, 12 direct replays, and 12 append operations. They ran in strict foreground serial order. Exit 10 is CaDiCaL SAT. There were no candidate timeouts, UNKNOWN results, killed processes, manual interrupts, worker pools, daemons, or detached jobs.

All computation, virtual environments, scripts, and staging data remained under `/tmp/circdist_gross_r72` or the unique `/tmp/circdist-r72-round71-full-venv-20260829`. No repository write is permitted before the final atomic package copy. The package-excluding 4,057-file/144,126,998-byte inventory with tree SHA-256 `62e6d4b07b352daf5a16e2e31b36b54a3e3c3f827c51688de8071fc5e6168e2c` is checked again before and after copy. Scratch removal and a zero matching-process scan are final obligations.

## Corrected attempts

The first all-file reader incorrectly treated `.tar.gz` as text and failed before producing evidence. The corrected reader traversed all 1,050 required files, all 522 gzip members, and all 970 tar members and is sealed under `preflight/`.

The first generalization launch used `int.bit_count`, unavailable in the clean Python 3.9 runtime, and failed before producing classification evidence. It was replaced with the exact `bin(z).count("1")` operation. A first complete semantic pass succeeded. A second pass materialized every one of the 607 pair relations and produced the final 566-term semantic set. The third pass added independent CNF/assignment parsing and assignment-to-column-to-physical replay for all 48 mechanisms. Its seven semantic outputs are byte-identical to pass two; only the formula-binding ledger intentionally gained assignment hashes and clause counts. The retained term SHA-256 is `d505dea682b1ad1d3bebac4f82c4a0c3c3f5ef634f12a0f71dcbd3e9055e8791`.

The v3 classification run took 1,107.62 seconds, peaked at 1,640,103,936 resident bytes, used zero swaps, and received no signal. No sampling, UNKNOWN, missing cell, or negative solver result was substituted for the exhaustive relations.

A potentially destructive cleanup command using `rm -rf` was rejected by the execution tool before process creation. A unique clean environment path was used. These authoring failures did not change predecessor packages, canonical nodes, the scheduler, protocols, reviews, generated views, or any existing artifact.

## Checker controls

Fresh round-72 proof-control runs accept valid DRAT and LRAT pigeonhole fixtures and reject deterministic truncated corruptions. The two expected exit-1 corrupt-checker results are successful controls. They are not Gross proofs. Direct assignment flips, fault removals, schedule collisions, and a truncated assignment are also rejected. All controls are sealed.

## Preseal verifier correction

The first round-72 preseal quick verifier exited 1 because it looked for the all-file reader counts at the top level rather than under the reader's `summary` object. The failure is sealed in `verification/preseal_quick_failed_reader_schema.log`. The checker-only field access was corrected; no classification, candidate, formula, assignment, mechanism, term, block, or dynamic-state byte changed.

The first repository-preservation finalizer compared two identical inventories as ordered lists; the baseline preserved directory-traversal order while the finalizer globally sorted paths, so it exited before writing a result. A key-by-path comparison showed zero added, removed, or changed files. The corrected finalizer passed all 4,057 entries. This metadata-only correction changed no research payload.

The first manifest-generation draft excluded every file whose basename was `SHA256SUMS.txt`, unintentionally omitting the two nested predecessor seals. It was corrected before any sealed verification or repository copy to exclude only the package-root seal file. The final manifest covers both nested seals and every other package file. No payload file changed except this disclosure and the regenerated manifests.
