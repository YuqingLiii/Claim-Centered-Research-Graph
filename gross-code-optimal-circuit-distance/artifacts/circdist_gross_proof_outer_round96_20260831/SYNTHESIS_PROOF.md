# Exact order-4 same-sector GF(2) synthesis proof

## Domain

Input is the independently reviewed, fresh post-i136 state137: 234 exact dynamic selectors split into 125 Xerr and 109 Zerr selectors. Only four distinct selectors from one sector are admitted. Thus the domain is exactly

`Q = {(a,b,c,d): 0 <= a < b < c < d < n}`, with `|Q| = C(n,4)`.

For Xerr this is 9,691,375; for Zerr it is 5,563,251; total 15,254,626. Repeated indices and mixed-sector tuples are outside this stated domain.

## Coverage and uniqueness

At each `c` from 2 through `n-2`, the algorithm first appends every pair `(a,c-1)` with `a<c-1`. Induction gives a left-pair list containing exactly all `(a,b)` with `a<b<c`. It then combines every such pair with every `(c,d)`, `c<d`. Every emitted tuple satisfies `a<b<c<d`. Conversely, any sorted quadruple appears when the loop reaches its unique third index `c`. Therefore every domain element appears exactly once.

The observed canonical counts equal the closed forms. Pair-pair enumeration would contain 30,027,375/17,319,555 X/Z decompositions. The code excludes 953,250/629,802 overlapping X/Z decompositions and 19,382,750/11,126,502 alternative disjoint pairings, retaining the unique canonical split.

## Effect algebra

Each selector is represented independently by a named-location bitset, canonical support bitset, physical support bitset, canonical/physical syndrome bitsets, and canonical/physical 12-bit logical actions. A quadruple effect is component-wise XOR. Named locations are symmetric-differenced before the fault-weight cap. Candidate retention requires named weight 1–10, both syndromes zero, both logical actions nonzero, equal canonical/physical actions, source-schedule validity, and a novel semantic predicate.

## Exact results

| quantity | Xerr | Zerr |
|---|---:|---:|
| domain | 9,691,375 | 5,563,251 |
| named weight <=10, multiplicity | 32,456 | 1,304 |
| unique eligible names | 32,456 | 1,304 |
| maximum multiplicity | 1 | 1 |
| zero named/canonical/physical support | 0/0/0 | 0/0/0 |
| canonical syndrome zero | 0 | 1 |
| physical syndrome zero | 0 | 1 |
| canonical logical trivial | 3,176 | 7,397 |
| physical logical trivial | 3,176 | 7,397 |
| inherited eligible names | 0 | 106 |
| novel eligible names | 32,456 | 1,198 |
| novel retained | 0 | 0 |

The one Zerr conservative valid occurrence has logical action `100110100011` and an inherited exact named predicate. Hence it cannot add a selector. All 33,654 novel eligible exact-name results fail conservatively: 32,456 Xerr and 1,198 Zerr have nonzero canonical syndrome. No sampling or probabilistic inference is used.

## Required audits

- Zero named support, canonical support, and physical support are counted separately.
- Logical triviality is counted independently from detector syndrome.
- Sector identity is never erased; a concrete mixed-sector ambiguity witness is retained.
- Every eligible exact name set is replayed; multiplicity is counted independently from semantic dedup.
- Dynamic predicates remain tied to their source schedule. A retained selector that is valid on its source schedule and invalid on iteration136 demonstrates why globalization is unsound.
- Named elementary-fault weight, canonical net-support weight, and physical net-support weight are distinct; the retained counterexample is 10/12/18.

## Scope

This is an exact no-go only for four distinct same-sector selectors in the frozen post-i136 state137. It neither proves Gross distance nor excludes higher closure order, other frontiers, or any cross-sector construction. The executable source, full histograms, counts, checksums, inputs, and replay output are retained.
