# CIRCDIST Gross block minimization and continued direct-360 CEGAR — round 69

Date: 2026-08-29  
Frozen problem: Gross bivariate bicycle code, direct-360 column model, `D*_Gross ∈ {11,12}`  
Package verdict: **MATERIAL-CHECKED-PROGRESS-NOT-CLOSED**

This is a sealed evidence package, not a canonical promotion. It does not edit the Gross node, scheduler, route, protocols, generated views, reviews, or any earlier artifact. A fresh independent exact review is required before any result from this directory is used canonically.

## What was established

Round 69 independently replayed the seals and verifiers from rounds 62, 63, and 68, reconstructed all twelve round-68 raw mechanisms, and enumerated all `6! = 720` local orders of every participating weight-six check. There are 23 sector/check catalogs and 30 unique cross-check pair relations. The factorization evaluates 30 × 720² = 15,552,000 pair-order cells, avoiding the infeasible `720^6` and `720^4` products of the two primary mechanisms.

The retained, load-bearing positive library contains:

- 3,368 explicit one/two-residual mechanisms of fault weight at most ten;
- 3,347 mechanisms completed by a frozen weight-12 logical-pool member;
- 21 mechanisms completed by a raw SAT weight-14 logical support;
- 4,740 deletion-minimal comparison antecedents, each with 4–12 atoms;
- 1,197,120 certified good-good pair-order cells;
- an explicit reconstructible witness selection for every one of those cells;
- 40,180 atom-deletion controls exposing a tuple outside the retained positive library.

Every retained antecedent is sound: every order tuple satisfying it retains either an inherited unary mechanism or one of the explicit two-residual mechanisms. The full verifier recomputes all local supports, opposite-check syndromes, logical quotients, physical suffix supports, singleton completions, zero syndromes, nontrivial logical status, and the mapping from every covered tuple to a positive configuration.

The 2,704 negative weight-14 solver outcomes are deliberately **non-load-bearing observations**. They have no candidate-specific DRAT/LRAT proofs and support no absence claim. The deletion controls are minimality controls relative to the conservative positive library; they are not claims that the exposed tuple has no other mechanism. This distinction is enforced in `verify.py`, `ATTACK_LEDGER.md`, and `REVIEW_LICENSE.txt`.

## Continued CEGAR

The exact outer model installed only:

- 1,440 globally proved round-63 unary clauses;
- 20 raw-replayed round-62 blocks;
- 4,740 round-69 generalized sound blocks;
- the raw-replayed dynamic blocks from earlier round-69 iterations.

The exploratory 15,874 round-63 pair-pattern clauses were installed zero times.

Six complete outer iterations, 0 through 5, were run. Each candidate used all 864 named CNOT edges, all 648 MC overlap constraints, and the global interleaving condition. Each outer solve was SAT. For every candidate, both complete direct-360 formulas were generated independently: Xerr and Zerr, 360 primary selection variables each, both 1,884-member logical pools bound, no pool/residual/check-count/order-family restriction, and exact `sum(select) ≤ 10` cardinality. All twelve formulas were SAT. Their complete assignments satisfy every DIMACS clause and replay as physical zero-syndrome nontrivial mechanisms.

The six iterations produced twelve new exact sound blocks, six per sector. No direct sector was UNSAT, so no candidate-specific absence proof exists and arbitrary-round repair was never entered. The continuation stop was set after six fully closed dual-sector candidates. The exact restart point is iteration 6 with 6,212 installed blocks and `cegar/dynamic_blocks.json` unchanged from the sealed frontier.

## Why the verdict is not root-closing

No complete outer exhaustion was obtained, so `D*=11` is not proved. No candidate passed independently checked direct absence in both sectors, so repair was never permitted; no raw-verifiable schedule plus repair certificate exists for `D*=12`. The rigorous interval therefore remains:

```text
D*_Gross ∈ {11,12}
```

## Independent replay

Create a clean Python 3.9 environment and install the exact dependencies:

```bash
python3 -m venv /tmp/circdist-r69-review-venv
/tmp/circdist-r69-review-venv/bin/pip install -r requirements.txt
```

Run the full sealed replay from this directory:

```bash
/tmp/circdist-r69-review-venv/bin/python verify.py
```

To include live repository binding checks:

```bash
/tmp/circdist-r69-review-venv/bin/python verify.py \
  --repo-root /absolute/path/to/Claim-Centered-Research-Graph
```

The full replay performs the 15.55-million-cell classification, explicit tuple-witness selection, all 3,368 physical replays, six fresh-process outer SMT byte reconstructions, twelve fresh direct-CNF reconstructions, all SAT-assignment and raw-mechanism replays, and fresh positive/corrupted DRAT and LRAT controls. The sealed pre-write replay took 121.67 seconds on the recorded host. `--quick` checks seals, compression, bindings, preflight records, and checker controls but intentionally skips the mathematical/computational replay and is not sufficient for promotion.

## Main files

| Path | Purpose |
|---|---|
| `RESULT.json` | Machine-readable claim boundary and counts |
| `MATH_DERIVATION.md` | Local-order and direct-model derivation |
| `LOCAL_ORDER_CLASSIFICATION.md` | All 12 blocks, 30 pair relations, representation, coverage, and controls |
| `classification/local_order_catalog.json.gz` | All 16,560 local order records and three suffix choices per order |
| `classification/pair_classification.json.gz` | Positive configurations, row bitsets, 4,740 terms, and 40,180 controls |
| `classification/PAIR_SUMMARY.csv` | Compact 30-relation index |
| `classification/EXAMPLE_DELETION_CONTROL.json` | Concrete licensed negative control |
| `cegar/summary.json` | Six-iteration outer/direct ledger |
| `cegar/dynamic_blocks.json` | Twelve new raw-replayed exact blocks and restart state |
| `cegar/iter*/` | Candidate, outer SMT, complete X/Z formulas, solver logs, and raw replay |
| `DIRECT360_AND_PROOF_POLICY.md` | Completeness boundary, proof requirements, and SAT trace treatment |
| `ATTACK_LEDGER.md` | Negative controls, rejected inferences, and remaining attacks |
| `PROCESS_LEDGER.md` | Every material process, interruption, limit, and final scan |
| `SOURCE_BINDINGS.json` | Current hashes for 50 evidence bindings / 526 bound files |
| `COMPRESSED_INVENTORY.json` | Exact original hashes and sizes for 110 deterministic gzip members |
| `PAYLOAD_SHA256SUMS.txt` | Payload freeze |
| `SHA256SUMS.txt` | Full package seal, excluding itself |
| `DISPATCHER_LICENSE.md` | Exact iteration-6 continuation procedure |
| `REVIEW_LICENSE.txt` | What an independent reviewer may and may not promote |
| `VERDICT.txt` | The single authorized verdict |

## Compression and inspectability

Large JSON, CNF, SMT-LIB, and solver logs are deterministically gzip-compressed with `mtime=0`. `COMPRESSED_INVENTORY.json` records the uncompressed byte count and SHA-256 as well as the compressed hash. `verify.py` checks both layers and rebuilds the formulas from source instead of trusting decompressed candidates.

CaDiCaL can emit a DRAT stream during a SAT run, but such a stream is not an UNSAT certificate. Those twelve redundant SAT traces totaled 811,176,127 bytes. They were not sealed. `cegar/sat_trace_disposition.json` records their individual hashes, sizes, and non-bearing status. The complete DIMACS formulas, variable/column/clause dictionaries, full SAT assignments, solver run records, and raw physical mechanisms are all retained.

## Claim boundary

This package licenses use of the 4,740 generalized blocks and twelve dynamic blocks only after the independent verifier passes. It licenses no inference from the 2,704 negative solver observations, no absence inference from a positive-only routine, no repair entry, no outer exhaustion, no exact value for `D*_Gross`, and no canonical edit. See `REVIEW_LICENSE.txt` for the precise boundary.
