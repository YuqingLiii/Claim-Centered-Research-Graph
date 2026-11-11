# Complete direct-360 sectors and proof gate

For each SAT outer schedule, both sectors are rebuilt with the unrestricted primary domain: 72 checks, 144 singleton data columns, 216 elementary residual columns, 360 primary selection variables per sector, and W=10. There is no pool, residual-pattern, check-count, or within-check order-family restriction.

A SAT result is retained only with a complete DIMACS assignment, all-clause replay, canonical mechanism replay, physical mechanism replay, zero physical syndrome, nontrivial logical action and fault count at most 10. All 24 sector queries passed.

For every candidate, the branch with the greatest complete CNF clause count (then variable count and label) receives a candidate-specific direct-absence attempt. Iteration 90 enabled proof output even though the result was SAT, producing a 248,948,763-byte non-certificate trace; later SAT attempts omit such traces. Any UNSAT result would have required fresh DRAT generation, independent DRAT acceptance with LRAT emission, independent LRAT acceptance, and valid/corrupt/truncated controls before repair. No candidate returned UNSAT, so no absence was accepted and repair was never entered.

The PHP(6,5) toolchain control independently demonstrates one generated UNSAT proof, valid DRAT acceptance, generated LRAT acceptance, and rejection of two corrupt and two truncated proofs. These controls validate the checker path only; they are not Gross proofs.
