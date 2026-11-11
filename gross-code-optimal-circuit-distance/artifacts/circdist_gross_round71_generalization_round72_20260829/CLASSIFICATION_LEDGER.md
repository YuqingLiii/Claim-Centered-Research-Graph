# Classification truth-relation ledger

The load-bearing machine objects are under `classification/`:

| Object | Content |
|---|---|
| `formula_raw_replay_bindings.json.gz` | 48 CNF, solver-log, assignment, candidate, selected-column, and sealed-mechanism hashes plus independent clause result |
| `mechanisms.json.gz` | independently reconstructed source schedules, selectors, data support, check/kind multiplicities, canonical/physical support, logical parity, and retained cover IDs |
| `local_order_catalog.json.gz` | 113 complete 720-order catalogs with residuals, physical suffixes, signatures, and unary witnesses |
| `multi_check_relations.json.gz` | 48 exact signature-DP relations, per-order contributions, minimized terms, and exposed-tuple controls |
| `pair_relations.json.gz` | all 607 factorized 720x720 positive relations, 300 explicit configurations, raw selectors, and 600 extracted candidates |
| `retained_terms.json.gz` | 566 installed terms with selectors, tuple counts, masks, and every deletion control |
| `dedup_ledger.json.gz` | every duplicate/dominance disposition and pair-domain coverage difference |
| `summary.json.gz` | exact headline counts and explicit conservative claim scope |

The generator `src/generalize_round71.py` recreates every object deterministically from `source_repository/`. It performs the full 48 assignment replays before catalog construction, enumerates 81,360 local order records, materializes all 607 truth relations, uses exact signature DP for all multi-check couplings, checks every term's constructive witness rule, minimizes atoms, computes semantic deduplication/dominance, and asserts retained coverage for every source mechanism.

The pair relation contains 93,888 explicit good-good positive cells before rectangles. Zeros are merely “not proved by this positive library.” The three mechanisms without a positive selected-pair completion are carried by exact selected-mechanism relations and their existing exact blocks, not forced into a pair rectangle.
