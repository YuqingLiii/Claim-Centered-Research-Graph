# Attacks and negative controls

The package checks complete assignments, every DIMACS clause, first-selected-primary flips, first-fault removal, schedule collisions, assignment truncation, all raw canonical/physical selectors, all retained pair tuples, exact multi DP products, zero-domain rejection, state-chain hashes, source/live bindings, manifest coverage, deterministic gzip dual hashes, and fresh valid/corrupt/truncated proof controls.

Counts: 24 assignment flips rejected, 24 fault removals rejected, 12 schedule collisions rejected, one assignment truncation rejected, 47,714 atom deletion controls, two valid proof accepts, two corrupt rejects and two truncated rejects.

Prohibited inference counters are all zero: zero truth cells, zero domains, completion misses, positive finder misses, solver negatives and deletion countertuples are never used as absence.
