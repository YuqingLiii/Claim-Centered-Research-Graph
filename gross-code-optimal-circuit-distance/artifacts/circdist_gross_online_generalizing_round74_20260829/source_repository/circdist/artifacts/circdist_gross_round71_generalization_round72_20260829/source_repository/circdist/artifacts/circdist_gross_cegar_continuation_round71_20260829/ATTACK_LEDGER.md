# Attack and limitation ledger

- **Restricted direct search:** excluded. Every sealed formula says `complete_query=true`, has 360 primaries, and lists all four forbidden restrictions as excluded.
- **One-sector short circuit:** excluded. Xerr and Zerr both ran for all 24 candidates before state mutation.
- **Unverified assignment:** excluded. All variables and clauses are replayed; physical support, syndrome, and logical quotient are recomputed.
- **Illegal outer model:** excluded candidate-by-candidate by exact SMT reconstruction, fixed-model SAT, 864-edge/648-MC audit, conflict checks, compression, and interleaving.
- **Exploratory pair clauses installed:** excluded; every candidate records zero and the verifier reconstructs only 1,440+20+4,740+dynamic blocks.
- **Negative observations used as proof:** excluded. The 2,704 inherited negative weight-14 observations are never loaded into the outer model or an absence inference.
- **Generalization from repeated weights:** rejected. Similar fault weights do not prove a tuple rectangle; this batch adds zero generalized clauses.
- **Sector absence:** unavailable because all 48 formulas are SAT.
- **Repair:** unavailable because no candidate has two accepted sector-absence proofs.
- **Outer exhaustion:** unavailable because all 24 outer queries are SAT.
- **Root value:** not closed; `D*_Gross` remains in `{11,12}`.
