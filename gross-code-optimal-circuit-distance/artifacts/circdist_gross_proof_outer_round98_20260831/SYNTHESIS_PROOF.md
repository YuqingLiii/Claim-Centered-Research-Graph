# Round98 exact same-sector order-5 synthesis proof

Domain: five distinct selectors from the reviewed post-iteration-136 same-sector bases: X has 125 rows and Z has 109. Every tuple has exactly one increasing representation `a<b<c<d<e`; five nested increasing loops enumerate all and only these tuples. Counts are `C(125,5)=234,531,275`, `C(109,5)=116,828,271`, total `351,359,546`.

For every tuple the enumerator XORs named, canonical-support, physical-support, canonical-syndrome, physical-syndrome, canonical-logical and physical-logical bit vectors. Histograms independently sum to the closed-form domain sizes. Eligible named weight 1--10 results are stored by their full 384-bit name mask and exact five witnesses. The independent validator replays all 40,153 unique eligible results against the frozen model; maximum multiplicity is one. X and Z both have zero canonical-syndrome-zero eligible results, hence zero conservative valid occurrences and zero retained selectors.

This is a finite no-go only for five distinct same-sector selector XORs on the bound schedule/base. Exact data and histograms are in `synthesis/order5_gf2_closure.json`; the independent replay is `verification/dispatcher_order5_validation.json`.
