# Public mathematical derivation

## 1. Schedule domain

There are 864 named CNOT-edge time variables. A valid schedule is a permutation with all reviewed causal inequalities and 648 multi-check constraints. Every candidate stores all times and passes the schedule audit. An outer block is a conjunction of local order atoms; the scheduler asserts the negation of each installed conjunction.

## 2. Unrestricted direct-360 formula

For each sector there are exactly 360 primary columns: 144 data singletons and 72×3 residual elementary fault columns. For check row `r_c` and within-check permutation `π`, residual kind `k` has canonical support `u_{c,k}(π)` at the reviewed residual positions and physical suffix/prefix support `p_{c,k}(π)`. A Boolean selector is created for every primary column, with only the exact cardinality bound `Σx_j≤10`, all 72 syndrome parity equations, and a disjunction that one of 12 logical quotient parities is nonzero. The formula excludes pool, residual-pattern, check-count, and order-family restrictions.

Every SAT assignment is complete on all DIMACS variables and every clause is evaluated. Selected columns map back to names, then to canonical and physical supports. Both must have zero detector syndrome, the same nonzero logical quotient, and at most ten faults. A nonzero quotient proves stabilizer nonmembership.

## 3. Local order catalogs

Each participating weight-six check has all `6!=720` permutations. Every record contains the six qubits, all three canonical residual supports, corresponding physical supports, their detector/logical signatures, and any constructive unary witness. Canonical and physical option signatures are checked equal for all records. An atom `q<r` becomes the exact 720-bit mask of orders where `q` precedes `r`; a term is the intersection of its atom masks.

## 4. Exact pair relations and rectangles

For checks `a,b`, the exact positive truth relation is a 720×720 Boolean matrix. Unary witnesses cover a whole partner row or column. Each explicit configuration contributes a Cartesian product of two option masks. A retained term has masks `A,B` derived from its atoms and is sound only if `A×B⊆T`. Its physical construction is replayed literally for every `(i,j)∈A×B`, using the published selector priority and completion.

## 5. Multi-check GF(2) proof

For a fixed selected mechanism, each allowed order at check `c` has canonical and physical local contributions with identical signature `σ_c(o)`. With data constant `σ_0`, the exact reachable multiplicities are

`N_0(σ_0)=1`, and `N_{t+1}(z)=Σ_o N_t(z⊕σ_{c_t}(o))`.

Orders with the same signature are aggregated with their exact multiplicity. Every allowed record, every signature class, every transition, layer hash, terminal multiplicity and Cartesian product is stored. Soundness requires total multiplicity positive, invalid terminal multiplicity zero, and every terminal signature to have zero syndrome and nonzero quotient. The physical selector is the named fixed mechanism with its exact data and residual-kind mapping. This proves every tuple in a large product without sampling.

The cross-registry two-selector pilot uses shared/exclusive signature classes and meet-in-the-middle terminal products with explicit selector-choice multiplicities. No such term survived the accepted batches; this says nothing about all possible higher-dimensional constructions.

## 6. Exact semantic classification

A term is normalized by sector, ordered check list and exact 720-bit masks. Exact duplicates have identical normalized regions. `U` dominates `V` precisely when every normalized local mask/product of `V` is contained in `U`. Pair-domain union coverage is counted row by row over all 720×720 cells. Tentative classifications remain in memory; raw soundness and retained exhaustive validation finish before ledgers and installed states are finalized.

## 7. Scope

All conclusions are positive constructive soundness. Sampling, solver negatives, zero cells, positive misses and deletion countertuples never imply absence. No candidate-specific Gross UNSAT proof exists here, so no repair or branch closure is licensed.
