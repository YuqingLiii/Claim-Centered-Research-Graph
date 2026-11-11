# Exact order-3 same-sector GF(2) synthesis proof

## Domain

The input is the checked post-iteration-136 state with 234 exact selectors: 125 Xerr and 109 Zerr. The search domain is every unordered set of three distinct selectors in one sector. It is not sampled and has no heuristic cutoff:

`C(125,3)+C(109,3)=317,750+209,934=527,684`.

The generator uses `itertools.combinations(rows,3)` separately in Xerr and Zerr. It asserts that the observed enumeration count equals this binomial census.

## Exact construction

Each selector is rebound to its semantic hash over sector, selected names, data support, and grouped residual kinds. For input location sets `A,B,C`, the candidate is their exact name-level symmetric difference `A Δ B Δ C`. This is the unique location set representing the three GF(2) column sums because duplicate names cancel pairwise.

Candidates with zero names or more than 10 names are outside the ordinary EFSSC weight domain. Existing selectors are removed semantically. Every remaining result is replayed with the frozen direct model; retention requires distinct valid names, exact weight ≤10, detector syndrome zero, and nontrivial logical parity. There is no sampled predicate and no cap on the number retained.

## Census and result

- full exact domain: 527,684 triples;
- novel results of exact weight 1--10: 4,232;
- unique novel eligible results: 4,232;
- exact replays with detector zero and logical nonzero: 0;
- misses by nonzero detector syndrome: 4,232;
- selectors installed: 0.

The runtime-independent semantic result hash is `558a9fcdd88e527fb5a4c49b3e6c268793f6644188f512b5d0af25a971ea1b45`. A fresh replay matched the stored object after removing only the measured `seconds` field.

## Rejected relaxations

- **Mixed sectors:** one explicit X/Z pair has different sector effects for the same name-level construction. There is no sector-independent XOR semantics.
- **Schedule globalization:** selector `iter42-Xerr` is exact and valid on its source schedule but has nonzero syndrome on iteration 136. Validity must remain a schedule-dependent EFSSC predicate.
- **Support as weight:** the iteration-136 Xerr mechanism has 10 named fault locations but canonical net-support weight 12. Direct weight counts named locations, not the post-cancellation data support.
- **Overweight triples:** an explicit enumerated triple has symmetric-difference weight above 10 and is rejected rather than projected, truncated, or quotiented.

## Licensed conclusion

This is a finite checked no-go for order-3 same-sector closure of the 234-selector frontier on iteration 136. It retains no term and proves no schedule absence, universal invariant, selector-union exhaustion, or `D*` branch.
