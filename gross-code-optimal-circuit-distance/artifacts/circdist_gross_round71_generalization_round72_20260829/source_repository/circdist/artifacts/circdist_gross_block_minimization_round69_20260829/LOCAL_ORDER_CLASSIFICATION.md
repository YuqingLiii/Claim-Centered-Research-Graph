# Exact local-order classification ledger

The word **exact** in this file applies to enumeration of all 720 local orders and to the positive witness relation represented by the sealed configurations and row bitsets. It does not promote the unproved negative weight-14 solver observations to absence facts.

## Twelve source mechanisms

| source block | sector | participating checks | unique pair references | round-68 atoms |
|---|---:|---|---:|---:|
| `primary-Xerr` | Xerr | 32, 33, 34, 41, 44, 46 | 15 | 53 |
| `primary-Zerr` | Zerr | 6, 8, 9, 11 | 6 | 32 |
| `continuation-0-Xerr` | Xerr | 2, 11 | 1 | 16 |
| `continuation-0-Zerr` | Zerr | 4, 14 | 1 | 16 |
| `continuation-1-Xerr` | Xerr | 10, 17 | 1 | 16 |
| `continuation-1-Zerr` | Zerr | 19, 21 | 1 | 16 |
| `continuation-2-Xerr` | Xerr | 11, 17 | 1 | 16 |
| `continuation-2-Zerr` | Zerr | 15, 23 | 1 | 16 |
| `continuation-3-Xerr` | Xerr | 2, 8 | 1 | 16 |
| `continuation-3-Zerr` | Zerr | 15, 23 | 1 | 16 |
| `continuation-4-Xerr` | Xerr | 7, 8 | 1 | 16 |
| `continuation-4-Zerr` | Zerr | 15, 18 | 1 | 16 |

The two primary mechanisms contribute 15 Xerr and 6 Zerr pair relations. Ten continuation blocks contribute ten pair references, one of which repeats the Zerr `(15,23)` relation. After deduplication there are 30 unique sector/pair relations. The twelve source antecedents contain 245 atoms in total. They are preserved through `inputs/round68/verification.json`, `inputs/round68/cegar_continuation5.json`, and the source binding to the complete round-68 package.

## Thirty pair relations

| # | sector | checks | positive residual configs | certified good-good cells | terms | atom histogram |
|---:|---|---:|---:|---:|---:|---|
| 1 | Xerr | 2,8 | 64 | 32,768 | 88 | `{"10":16,"11":4,"12":4,"8":48,"9":16}` |
| 2 | Xerr | 2,11 | 52 | 17,344 | 72 | `{"10":4,"11":8,"8":36,"9":24}` |
| 3 | Xerr | 7,8 | 88 | 35,456 | 128 | `{"10":24,"7":20,"8":52,"9":32}` |
| 4 | Xerr | 10,17 | 276 | 96,896 | 436 | `{"10":72,"7":92,"8":124,"9":148}` |
| 5 | Xerr | 11,17 | 64 | 32,768 | 84 | `{"10":16,"11":4,"8":48,"9":16}` |
| 6 | Xerr | 32,33 | 88 | 35,456 | 132 | `{"10":24,"7":12,"8":52,"9":44}` |
| 7 | Xerr | 32,34 | 148 | 52,928 | 184 | `{"10":36,"12":4,"7":16,"8":76,"9":52}` |
| 8 | Xerr | 32,41 | 52 | 17,344 | 92 | `{"10":20,"11":8,"12":4,"8":36,"9":24}` |
| 9 | Xerr | 32,44 | 20 | 10,752 | 40 | `{"10":12,"11":16,"12":4,"8":4,"9":4}` |
| 10 | Xerr | 32,46 | 64 | 20,160 | 96 | `{"10":28,"11":8,"12":4,"8":48,"9":8}` |
| 11 | Xerr | 33,34 | 88 | 35,456 | 132 | `{"10":24,"7":12,"8":52,"9":44}` |
| 12 | Xerr | 33,41 | 356 | 95,360 | 414 | `{"4":4,"6":26,"7":308,"8":76}` |
| 13 | Xerr | 33,44 | 44 | 20,544 | 64 | `{"10":24,"12":4,"7":12,"8":8,"9":16}` |
| 14 | Xerr | 33,46 | 60 | 25,024 | 92 | `{"10":16,"11":12,"12":4,"7":16,"8":8,"9":36}` |
| 15 | Xerr | 34,41 | 276 | 96,896 | 436 | `{"10":80,"7":100,"8":104,"9":152}` |
| 16 | Xerr | 34,44 | 68 | 19,264 | 80 | `{"10":16,"7":28,"8":24,"9":12}` |
| 17 | Xerr | 34,46 | 20 | 10,752 | 40 | `{"10":12,"11":16,"12":4,"8":4,"9":4}` |
| 18 | Xerr | 41,44 | 52 | 17,344 | 92 | `{"10":20,"11":8,"12":4,"8":36,"9":24}` |
| 19 | Xerr | 41,46 | 52 | 22,976 | 80 | `{"10":28,"11":4,"7":12,"8":8,"9":28}` |
| 20 | Xerr | 44,46 | 148 | 52,928 | 184 | `{"10":36,"12":4,"7":16,"8":76,"9":52}` |
| 21 | Zerr | 4,14 | 68 | 19,264 | 104 | `{"10":24,"7":24,"8":28,"9":28}` |
| 22 | Zerr | 6,8 | 148 | 52,928 | 196 | `{"10":48,"12":4,"7":12,"8":76,"9":56}` |
| 23 | Zerr | 6,9 | 96 | 43,520 | 152 | `{"10":72,"11":8,"8":32,"9":40}` |
| 24 | Zerr | 6,11 | 88 | 35,456 | 144 | `{"10":44,"12":4,"7":20,"8":36,"9":40}` |
| 25 | Zerr | 8,9 | 88 | 35,456 | 140 | `{"10":40,"12":4,"7":12,"8":40,"9":44}` |
| 26 | Zerr | 8,11 | 96 | 43,520 | 148 | `{"10":72,"8":32,"9":44}` |
| 27 | Zerr | 9,11 | 148 | 52,928 | 184 | `{"10":48,"12":4,"7":16,"8":76,"9":40}` |
| 28 | Zerr | 15,18 | 52 | 17,344 | 80 | `{"10":16,"11":8,"8":32,"9":24}` |
| 29 | Zerr | 15,23 | 356 | 95,360 | 442 | `{"4":4,"6":26,"7":344,"8":68}` |
| 30 | Zerr | 19,21 | 148 | 52,928 | 184 | `{"10":48,"12":4,"7":16,"8":76,"9":40}` |

Totals: 3,368 explicit configurations, 1,197,120 certified good-good cells, 4,740 terms, and 40,180 deletion controls. `classification/PAIR_SUMMARY.csv` gives the same index in machine-friendly form.

## Representation fields

`classification/local_order_catalog.json.gz` stores 23 entries. Each entry contains the fixed check row, all 720 orders, the three canonical/physical suffix options, opposite-check syndrome, logical quotient, and unary witness when present.

`classification/pair_classification.json.gz` stores for each pair:

- `positive_residual_configurations`: the complete retained positive configurations, including residual kinds/supports, logical support, singleton columns, fault weight, logical parity, source, and comparison atoms;
- `truth_rows_hex`: 720 row bitsets for the conservative certified relation (the historical field name is retained; it must not be read as a proved global negative truth table);
- `new_good_good_rows_hex`: the subset requiring a two-residual positive configuration;
- `deletion_minimal_terms`: comparison antecedents, coverage sizes, source configuration, and one exposed tuple per removed atom;
- counts and histograms independently checked by `verify.py`.

## Exact tuple reconstruction

For each good-good cell set in `new_good_good_rows_hex`, `verify.py` searches the two local option triples in fixed kind order and finds a key in `positive_residual_configurations`. It then replays the named logical support and singletons. The selector covers all 1,197,120 such cells and is hashed in `MATH_DERIVATION.md`. Unary cells use the cataloged inherited one-residual witness.

## Deletion and overgeneralization controls

Every term has one control for each atom. The control gives the removed atom plus exact `a` and `b` order IDs and six-qubit orders. The verifier checks that the exposed tuple satisfies every remaining atom and is outside the conservative certified relation. `classification/EXAMPLE_DELETION_CONTROL.json` is a small standalone example.

These controls reject unlicensed weakening of an antecedent. They do not establish that an exposed tuple is globally good: an unenumerated mechanism could exist. A reviewer may use them for library-relative deletion-minimality only.

## Original-block preservation versus generalized library

No source block was silently rewritten in place. The round-68 mechanisms remain bound as inputs. The new CEGAR outer model installs the 4,740 positive-witness terms atop the 1,460 inherited constraints and does not additionally install the twelve source blocks. The factor ledger records which pair relations arise from each source. If a reviewer rejects any pair representation, the corresponding terms must be removed; the exact round-68 block may be restored only from its raw-replayed source evidence.
