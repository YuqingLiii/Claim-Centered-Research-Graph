# Direct-360 and proof policy

Every candidate carries two independently generated complete formulas with 360 primary columns, 1,884 bound logical-pool members, and exact `sum(select)<=10`. The only accepted SAT evidence is a complete assignment that satisfies every clause and passes canonical plus physical replay.

UNSAT would be accepted only with a retained complete formula, solver proof, independently accepted DRAT and LRAT checks (or an equally strong independently checkable object), and valid/corrupted/truncated checker controls. No sector in this package returned UNSAT, so there are no candidate absence proofs. The small proof files under `controls/` test tools and cannot be used as Gross evidence.

UNKNOWN, timeout, a solver's printed UNSAT string, positive-only search, the round-69 2,704 negative weight-14 observations, and deletion controls cannot establish absence. Repair requires accepted absence in both sectors of the same candidate.
