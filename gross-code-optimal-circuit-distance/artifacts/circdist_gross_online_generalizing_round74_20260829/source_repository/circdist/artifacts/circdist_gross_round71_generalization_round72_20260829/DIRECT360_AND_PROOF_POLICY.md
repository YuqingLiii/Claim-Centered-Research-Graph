# Direct-360 and proof policy

Every candidate carries both complete direct queries. Each has 360 primary fault variables, the complete 1,884-member logical pool binding, exact `sum(select)<=10`, 72 syndrome XOR rows, 12 logical parity rows, and a nonzero-logical disjunction. There is no pool, residual pattern, check count, or within-check order-family restriction.

SAT is accepted only from a complete assignment satisfying every DIMACS clause followed by deterministic canonical and physical replay. All 24 queries meet that rule.

UNSAT would require retaining complete DIMACS plus a proof-producing rerun, accepted DRAT/LRAT (or equivalent) with an independent checker, and corrupted/truncated rejection controls. No new sector is UNSAT. The pigeonhole files under `controls/proof_checker/` prove only that the checker accepts a valid fixture and rejects corrupt fixtures; they carry no Gross absence.

UNKNOWN, timeout, positive-finder miss, pair-table zero, the round-69 negative observations, and deletion controls are never absence. Repair needs independently accepted absence in both sectors of one candidate. Outer UNSAT would additionally require an equivalent proof-producing outer encoding and independently accepted proof before exhaustion.
