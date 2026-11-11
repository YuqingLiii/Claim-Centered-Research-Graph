# Direct-360 and proof policy

Every SAT outer schedule receives both complete direct sectors without a repair prefilter. Each formula contains 360 primary selection variables from the full 1,884-member pool, exact `sum(select)≤10`, all syndrome parity rows, and a logical-nonzero disjunction. Pool, residual-pattern, check-count, and order-family restrictions are absent.

SAT is accepted only after parsing a complete assignment, checking every DIMACS clause, reconstructing selected columns, and replaying both canonical and physical 144-bit supports as zero-syndrome and nontrivial. All 24 sector queries satisfy this standard.

A direct UNSAT would be accepted only with the full candidate formula, retained DRAT and LRAT proofs, independent checker acceptance, and deterministic corrupt/truncated controls that are rejected. No candidate returned UNSAT, so no Gross proof file exists and repair was not entered. The fixtures under `controls/round74_proof_checker/` test the checker pipeline only.

UNKNOWN and timeout have no mathematical conclusion. Outer UNSAT would likewise require an equivalent proof-producing encoding and independent accepted proof before any exhaustion claim. No outer was UNSAT.
