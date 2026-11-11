# Gross exact online-generalizing CEGAR — round 74

Date: 2026-08-29  
Verdict: **MATERIAL-CHECKED-PROGRESS-NOT-CLOSED**

This sealed proposer package continues the frozen Gross-code search from the exact round-73 license. It performs twelve complete online iterations, 42 through 53. It modifies no canonical node, scheduler, protocol, generated view, review, or predecessor artifact. It supplies positive, checked progress and an exact restart frontier; it does not prove physical absence, outer exhaustion, or the root claim.

## Bound start

- round-72 root seal: `bc2bf8bdc2da199e348b0471ef4f0367e52e1a7e5eefe1294adb51ab25a4f7f6`;
- round-73 review: `92e2b6306f7181b2c61fa02b3eba0624a74864f19045e6e72b208754115224d3`;
- clean full round-72 replay: PASS in 1,326.432405 seconds;
- iteration 42: `1,440 + 20 + 4,740 + 566 + 84 = 6,850` installed blocks;
- merged reviewed generalized library: 5,306 terms;
- exploratory round-63 pair clauses installed: **0**.

## Result

All twelve fresh outer queries are SAT. Every schedule has all 864 named CNOT edges, 648 measurement-collision checks, one edge once, one gate per qubit-time, compressed idle layers, and global X/Z interleaving. Each stored SMT formula and fixed schedule passed an independent replay.

Both unrestricted direct-360 sectors were generated unconditionally for every schedule. All 24 formulas are SAT. Every complete assignment satisfies every DIMACS clause and reconstructs a canonical and physical zero-syndrome, nontrivial mechanism with at most ten elementary faults. The run adds 24 candidate-exact blocks.

Each pair of SAT mechanisms was generalized before the next outer. Across the twelve online passes, 188 raw candidates classify as 31 duplicate-new, 23 dominated-new, zero duplicate-old, zero dominated-old, and 134 retained. The final merged generalized library has 5,440 terms. All 1,137,096 retained pair tuples were instantiated and replayed literally. The one retained multi-check term covers 2,985,984 tuples through a symbolic universal proof over all materialized local-order signature classes and the exact joint GF(2) DP; it is not a sample-based claim.

The frozen next frontier is iteration 54 with 108 exact dynamic blocks and

```text
1,440 + 20 + 5,440 + 108 = 7,008 blocks.
```

No sector was UNSAT, so there is no candidate-specific DRAT/LRAT absence proof and repair was never licensed. No outer UNSAT proof exists. `D*_Gross` therefore remains in `{11,12}`.

## Audit map

| path | role |
|---|---|
| `RESULT.json` | machine-readable claim boundary and exact restart hashes |
| `MATH_DERIVATION.md` | definitions, formulas, DP exactness, factorized universal proof, and soundness limits |
| `ITERATION_LEDGER.md` | all twelve online transactions |
| `CLASSIFICATION_LEDGER.md` | catalog/pair/multi/term/dedup counts |
| `cegar/iter*/` | outer formulas, schedules, direct CNFs, assignments, witnesses, online generalization objects, and run ledgers |
| `classification/round74_retained_terms.json.gz` | all 134 retained terms and 1,372 deletion controls |
| `classification/installed_generalized_terms.json` | exact 5,440-term iteration-54 library |
| `cegar/dynamic_blocks.json` | exact 108-block dynamic state |
| `controls/negative_controls.json` | assignment, fault, schedule, truncation, and deletion controls |
| `controls/round74_proof_checker/` | valid and corrupted DRAT/LRAT checker controls; not Gross proofs |
| `SOURCE_BINDINGS.json` | frozen/live inputs, seals, reviews, and nested round-72 source package |
| `COMPRESSED_INVENTORY.json` | deterministic gzip compressed/uncompressed byte hashes |
| `PROCESS_LEDGER.json` | 84 load-bearing foreground runs and three corrected attempts |
| `RESTART_LICENSE.md` | exact iteration-54 continuation boundary |
| `verify.py` | quick and full self-contained replay |
| `SHA256SUMS.txt` | package-root external seal, excluding itself |

## Verification

```bash
python3 -m venv /tmp/circdist-r74-review-venv
/tmp/circdist-r74-review-venv/bin/pip install -r requirements.txt
PYTHONDONTWRITEBYTECODE=1 /tmp/circdist-r74-review-venv/bin/python verify.py --full
```

Use `--repo-root /absolute/path/to/Claim-Centered-Research-Graph` to compare the ten frozen source bindings with live files. `--quick` checks seals, compression, all stored ledgers, catalog signatures, tuple certificates, negative controls, and exact state chains without rerunning the expensive generators. Default execution is full.

The verifier is a proposer-supplied reproducibility tool. A **fresh independent exact review is required** before any canonical installation or restart license is exercised.
