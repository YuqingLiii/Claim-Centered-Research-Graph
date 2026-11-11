# Term library, semantic filtering, and coverage differences

A term is identified semantically by `(sector, constrained check → exact 720-bit order mask)`. Syntax and atom order do not determine equality. An absent check has the all-720 mask. `U` dominates `V` when every mask-domain tuple of `V` is contained in `U`; this implication is safe because both terms already have constructive soundness proofs.

The initial 5,306-term library is immutable. Round-74 terms are appended only. The comparison index is incremental: it normalizes the current installed library once and selects terms whose check domains can interact with the current mechanism. It does not rescan the reviewed 314,668,800 old pair cells on every iteration. Final full verification reruns the complete twelve-step state chain and compares every generated object byte-for-byte.

For two-check rectangles, prior union coverage is computed exactly over the finite 720×720 domain. This yields 1,098,444 pair tuples not covered by relevant predecessors. For a multi-check Cartesian domain, the package records the exact term total plus exact semantic duplicate/dominance decisions; it does not claim an expensive high-dimensional global union cardinality.

No predecessor is removed when a new term is stronger. The ledger records `candidate_dominates_installed_preserved`; it is empty here. The final 134 retained terms are linked to all 24 source mechanisms, while all source exact blocks remain installed independently.
