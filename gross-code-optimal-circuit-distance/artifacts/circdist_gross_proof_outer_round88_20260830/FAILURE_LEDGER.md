# Failure ledger

All incidents below were bounded foreground development failures.  None contributed verdict-bearing evidence, and no failed formula was submitted as an accepted formula.

| incident | disposition |
|---|---|
| Initial extractor addressed `source_iteration` although the reviewed state uses `iteration`. | Stopped with `KeyError`; extractor corrected and all bound start-state fields rechecked. |
| Initial normalized-AST lookup used a nonexistent key. | Stopped; exact reviewed field was used. |
| Development Python 3.9 lacks `int.bit_count`. | Stopped; replaced by `bin(mask).count("1")`, then exhaustive truth tests passed. |
| A loop variable shadowed the parsed argparse namespace. | Stopped before accepted output; variable renamed. |
| First serialized iter109 CNF omitted the pinned-true unit: 397,902 variables, 1,326,595 clauses, SHA-256 `30da99d6fb47966fb01bc8e2b26e89144dd54307bebcf07140cf03c74d038e13`. | Independent checker rejected the missing clause.  It was never solver-run and is not in the accepted formula set. |
| First generalized compiler rejected iter110 because iteration109 appeared in a schema assertion. | Stopped; schema check generalized to the exact iteration prefix/suffix. |
| First independent checker hard-coded 2,274 memberships. | Stopped on iter110; checker changed to source-bound counts and rerun on every accepted formula. |
| First package continuation audit compared a provenance schema field absent from compact source rows. | Stopped before PASS; comparison restricted to the exact semantic selector key set. |
| First continuation checker contained two formatting defects introduced while packaging. | Both were syntax failures before evidence acceptance; corrected, then the complete checker returned PASS. |
| First root-manifest generator filtered nested files by basename, incorrectly omitting bound nested manifests. | The independent manifest checker rejected the set equation.  No seal was accepted; generation was changed to package-relative root names and the checker then passed exactly. |

A disclosed Round86 14.36 GB failed DP path is inherited history only; this proposer neither reran nor relied on it.  No out-of-memory event occurred here.
