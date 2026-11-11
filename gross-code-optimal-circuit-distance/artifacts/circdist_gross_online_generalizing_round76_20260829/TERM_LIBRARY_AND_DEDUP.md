# Term library and semantic deduplication

A generalized term is a sector plus a finite conjunction of within-check order atoms. For each constrained check, the atoms determine an exact subset of its 720 local orders. Its semantic key is the sector together with those exact 720-bit masks; omitted checks have the all-720 mask.

Terms are equal exactly when all masks agree. A sound term `U` dominates `V` exactly when `region(V) subseteq region(U)`. Every comparison uses the full installed library of 5,440 inherited terms plus terms retained earlier in round 76. Installed predecessor terms are never removed. Candidate-exact blocks are preserved independently of generalized coverage.

Aggregate disposition: 420 raw; 0 duplicate-old; 71 duplicate-new; 0 dominated-old; 46 dominated-new; 303 retained.

Tentative classification occurs only in memory after raw candidate soundness is established. The public dedup ledger and generalized/registry state are written only after every retained pair tuple has been literally replayed or every retained multi domain has passed its factorized universal proof.

Deletion controls prove only atom minimality relative to the candidate positive relation or fixed selector. They do not prove installed-union minimality, global physical-mechanism minimality, or absence. A countertuple may already be covered by another installed term.
