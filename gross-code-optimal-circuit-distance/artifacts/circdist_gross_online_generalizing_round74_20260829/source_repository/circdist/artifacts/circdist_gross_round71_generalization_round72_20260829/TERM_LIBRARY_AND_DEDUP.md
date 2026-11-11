# Term library, controls, and semantic difference

The round-69 library is preserved verbatim at `classification/round69_pair_classification.json.gz`. The installed round-72 additions are the 566 entries in `classification/retained_terms.json.gz`.

Every term records its exact local-order mask(s), covered tuple count, a constructive mechanism selector, and one exposed tuple for every atom deletion. Pair terms partition their covered cells into `a_unary`, `b_unary_after_a_good`, and `explicit_pair_after_both_good`; the counts are asserted to sum to the rectangle size. Multi-check terms store the fixed selected names, data support, selected kinds per check, permitted masks, and exact reachable-signature count.

The dedup ledger uses finite semantic masks, not text equality. It records 85 internal duplicates and 45 new terms dominated by other new terms. No new term duplicates or is dominated by a reviewed old term, and no old term is removed. The 272 pair-domain difference rows report 4,018,600 cells in the retained new pair unions not covered by the old union on the same two-check domain. This is library-relative coverage, not a count of globally new physical failures, because old or new terms involving additional checks do not define unconditional two-check cells.
