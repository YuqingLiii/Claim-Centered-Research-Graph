# Term library, deduplication and dominance

Every source candidate retains its two exact outer blocks. Generalized terms are additional conservative blocks with a physical witness for every covered local-order tuple.

For each batch, `raw_term_candidates.json` precedes `semantic_dedup_ledger.json`. The ledger exposes the exact normalized finite region and one of: duplicate old, duplicate new, dominated old, covered by the full evolving union, or retained. Installed predecessors are preserved. The batch is validated against the full state it consumed, not against a sample or only the named seed mechanisms. Pair unions are exact rowwise 720-bit unions; online multi membership is decided by an exact complement CSP over local membership classes.

Deletion witnesses address a different question. Removing one atom may expose a tuple outside the named positive relation or fixed selector, but another installed term may cover it. Therefore deletion controls do not prove installed-union minimality, global minimality, necessity, or absence.
