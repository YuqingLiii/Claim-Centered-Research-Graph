# Package manifest and evidence map

## Structural records

- `README.md`: claim summary, replay entry point, and boundary.
- `RESULT.json`: machine-readable result.
- `VERDICT.txt`: single authorized verdict.
- `MATH_DERIVATION.md`: positive soundness mathematics.
- `LOCAL_ORDER_CLASSIFICATION.md`: 12-block / 30-pair classification ledger.
- `DIRECT360_AND_PROOF_POLICY.md`: complete direct formula and proof gates.
- `CEGAR_LEDGER.md`: six exact continuation iterations.
- `ATTACK_LEDGER.md`: negative controls and unresolved attacks.
- `PROCESS_LEDGER.md`: FIX-2 accounting.
- `REVIEW_LICENSE.txt`: promotion boundary.
- `DISPATCHER_LICENSE.md`: exact iteration-6 restart.
- `COMMANDS.txt`: commands and limits.
- `FINAL_AUDIT.txt`: final seal, inventory, process scan, and cleanup.

## Classification payload

- `classification/local_order_catalog.json.gz`: 23 catalogs ×720 orders.
- `classification/pair_classification.json.gz`: 30 relations, configurations, row bitsets, terms, and controls.
- `classification/block_factorization.json`: mapping from all 12 round-68 blocks to pair factors.
- `classification/PAIR_SUMMARY.csv`: compact pair index.
- `classification/EXAMPLE_DELETION_CONTROL.json`: standalone control.
- `classification/Xerr_w14_individual.json`, `Zerr_w14_individual.json`: all individual query results.
- `classification/*_w14_needed*.txt`: exact assumption inputs.
- generator and verifier logs/run JSON.

## CEGAR payload

- `cegar/summary.json`: six-iteration summary.
- `cegar/dynamic_blocks.json`: restart state with 12 exact blocks.
- `cegar/PROCESS_TIMES.json`: exact wall/exit/timeout ledger.
- `cegar/sat_trace_disposition.json`: hashes and non-bearing disposition for SAT traces.
- `cegar/iter0` through `iter5`: candidate JSON, outer SMT-LIB, outer result, full X/Z direct formula family, solver assignment logs, and physical verification.

Large per-iteration files are deterministic gzip members. Their original hashes appear in `COMPRESSED_INVENTORY.json`.

## Frozen sources and inputs

- `src/round63_src/`: exact frozen model, outer, and pattern code inherited through round 68.
- `src/round68_build.py`, `round68_verify.py`: direct formula and raw replay implementation.
- `src/inputs/w12X.txt`, `w12Z.txt`: both 1,884-member logical pools.
- `src/global_single_clauses.json`: round-63 summary.
- `src/round62_cegar20.json`: 20 inherited raw blocks.
- `inputs/round68/`: primary and five-continuation raw mechanisms.
- `src/original/`: byte-preserved round-69 working scripts.
- `src/build_cegar_candidate.py`, `replay_direct_candidate.py`, `append_dynamic_blocks.py`: portable sealed continuation tools.

## Bindings and preflight

- `SOURCE_BINDINGS.json`: 50 bindings / 526 files plus five offline governing snapshots.
- `bindings/snapshots/`: protocol, definition, Gross node, and scheduler snapshots.
- `preflight/inherited_all_file_read_audit.json`: every byte of rounds 62, 63, and 68 audited.
- `preflight/preflight_*`: fresh inherited verifier logs and run JSON.
- `preflight/preseal_package_verification.*`: full pre-write independent replay.
- `preflight/PRESEAL_AUDITOR_DEBUG.json`: pre-seal verifier defects found and fixed.
- `preflight/repository_baseline.json`: package-excluding repository baseline.

## Tooling and controls

- `tooling/`: pinned CaDiCaL, drat-trim, lrat-check, source archives, and build records.
- `controls/proof_checker/`: valid and deliberately truncated proofs plus fresh logs/run JSON.
- `requirements.txt`: exact Python packages.
- `verify.py`: independent full verifier.

## Seals

- `COMPRESSED_INVENTORY.json`: compressed and original hashes.
- `PAYLOAD_SHA256SUMS.txt`: payload freeze before final audit records.
- `SHA256SUMS.txt`: all package files other than itself.
