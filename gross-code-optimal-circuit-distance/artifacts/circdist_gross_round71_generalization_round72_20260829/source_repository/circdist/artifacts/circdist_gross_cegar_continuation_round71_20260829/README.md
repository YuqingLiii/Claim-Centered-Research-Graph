# Gross exact CEGAR continuation — round 71

Date: 2026-08-29  
Verdict: **MATERIAL-CHECKED-PROGRESS-NOT-CLOSED**

This sealed proposer package continues the exact Gross-code CEGAR search from the only round-70-licensed boundary. It does not modify a canonical node, scheduler, protocol, generated view, review, or earlier artifact. It supplies checked positive-witness progress and an exact restart state; it supplies no absence or root-closing result.

## Bound start

- round-69 root seal: `aad4434050b1b64d3907b990e8279a2b25b2b4e29abcebf585fb885f3dbab647`; 249/249 entries passed.
- round-69 clean full verifier: PASS, including 3,368 raw mechanisms, 4,740 generalized terms, and all inherited six CEGAR candidates.
- round-70 review: `b2fe38fd6adb1ef974624a49b84b7a61620a5c97a531155aac01fc39dbfbaabe`.
- exact start: iteration 6 with `1,440 + 20 + 4,740 + 12 = 6,212` blocks.
- exploratory round-63 pair clauses installed: **0**.

## Batch result

Iterations 6 through 29 are 24 complete dual-sector candidates. Every outer query was SAT and every recorded schedule passed an independent complete legality/formula replay. Both complete direct-360 sectors were then generated and queried unconditionally. All 48 sector formulas were SAT; all complete assignments satisfied every DIMACS clause and replayed as physical zero-syndrome nontrivial mechanisms of weight at most ten.

The batch adds 48 candidate-exact sound blocks. No new generalized block was installed: recurring fault-weight statistics did not by themselves supply a raw-mechanism-backed tuple rectangle. No sector was UNSAT, so no candidate-specific DRAT/LRAT absence proof exists and arbitrary-round repair was never entered. No outer exhaustion certificate exists. Therefore `D*_Gross` remains in `{11,12}`.

The exact frozen frontier is iteration 30 with 60 dynamic blocks and `1,440 + 20 + 4,740 + 60 = 6,260` total blocks.

## Main audit objects

| path | role |
|---|---|
| `RESULT.json` | machine-readable claim boundary |
| `MATH_DERIVATION.md` | public formulas and soundness derivation |
| `ITERATION_LEDGER.md` | all 24 candidate/sector outcomes |
| `cegar/summary.json` | exact counts, hashes, timings, and selected mechanisms |
| `cegar/iter*/` | SMT, schedule/model dictionaries, direct formulas, assignments, raw witnesses, independent replays, and run JSON |
| `cegar/dynamic_blocks.json` | exact 60-block restart state |
| `PROCESS_LEDGER.json` | all 144 candidate process records plus preflight |
| `controls/negative_controls.json` | 48 assignment flips, 48 fault removals, 24 schedule corruptions, and one truncated assignment |
| `controls/round71_proof_checker/` | fresh valid/corrupted DRAT and LRAT checker controls |
| `SOURCE_BINDINGS.json` | hashes and offline snapshots of every frozen source |
| `COMPRESSED_INVENTORY.json` | compressed and original hashes for 410 deterministic gzip files |
| `RESTART_LICENSE.md` | exact iteration-30 continuation gate |
| `verify.py` | full self-contained replay |
| `SHA256SUMS.txt` | package seal, excluding itself |

## Clean replay

```bash
python3 -m venv /tmp/circdist-r71-verify-venv
/tmp/circdist-r71-verify-venv/bin/pip install -r requirements.txt
PYTHONDONTWRITEBYTECODE=1 /tmp/circdist-r71-verify-venv/bin/python verify.py
```

Add `--repo-root /absolute/path/to/Claim-Centered-Research-Graph` to compare live sources with the sealed snapshots. The default full replay checks the package seal and compression, source-copy bindings, proof-checker controls, all outer formulas/schedules, all 48 direct CNF reconstructions, every complete assignment, every raw mechanism, all dynamic-block links, and all negative controls.

## Stop loss

The run stopped at the first legal boundary after the commissioned minimum of 24 candidates. The uncompressed candidate workspace was 306 MiB; another iteration would add two full formulas, assignments, dictionaries, and replay objects. This finite batch boundary limits disk and clean-replay growth while preserving an exact restart. It is not evidence of search exhaustion.
