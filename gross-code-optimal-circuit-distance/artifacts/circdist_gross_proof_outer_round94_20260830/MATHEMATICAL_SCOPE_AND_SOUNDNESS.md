# Mathematical scope and soundness

## Frozen universe

Let `S_Gross` be exactly the legal schedule universe bound by `CIRCDIST.gross`, the scheduler snapshot, and the iteration-136 semantic source. A point `t` assigns the 864 X/Z check-data interactions to bounded integer times. The formula preserves all conflict constraints, all 648 measurement-compatibility overlaps, MC0, the licensed global interleaving, within-check orders, whole-check relationships, compressed idle-layer convention, and terminal residual semantics. No morphing code, Circ-Preserve substitution, alternative conflict graph, stale compressor, retroactive cut, or exploratory pair clause is admitted.

The 14,484 inherited predicates are fixed: 1,440 unary, 20 round-62, 12,820 generalized, and 204 dynamic. An EFSSC selector names a concrete same-sector set of distinct elementary fault locations with weight at most 10. Its validity is recomputed from the schedule's exact within-check ranks.

## Outer equivalence

For prefix `P`, define

`F_P(t) = Legal_Gross(t) ∧ inherited_miss(t) ∧ ∧_{p∈P} ¬Valid_p(t)`.

The packaged compiler encodes `exists t F_P(t)` with 10-bit primary time words and uniquely defining Tseitin gates. The source roots, clause partition, primary/defined variable partition, comparator truth tables, rank-membership domains, and negative controls are independently reconstructed for every iteration. Thus CNF SAT is equivalent to the existence of a bounded legal schedule outside the installed exclusion union; CNF UNSAT, if accompanied by an accepted proof, would establish universal coverage by those exact predicates.

All twelve Round94 outer formulas are SAT, so no universal coverage theorem is available.

## Complete direct sectors

For fixed legal `t` and CSS sector `s`, the direct formula ranges over all 360 named elementary columns. If `y_j` selects column `j`, it enforces distinct Boolean locations, `1 <= sum_j y_j <= 10`, detector parity `H_s(t)y=0`, and at least one nonzero logical parity in `L_s(t)y`. Its exclusions list is explicit: no pool restriction, residual-pattern restriction, check-count restriction, or within-check order-family restriction.

A SAT assignment is replayed twice. Canonical replay computes the exact GF(2) column sum. Physical replay expands each residual hook to its suffix in the candidate's physical within-check order. A retained mechanism must have exact named-location weight, zero canonical and physical syndrome, nonzero logical action, and equal canonical/physical logical parities.

All 24 direct sectors are SAT and pass these checks. Therefore every Round94 candidate is killed positively. Direct SAT cannot prove absence. Direct UNSAT would require an accepted retained proof before it could license repair; no such branch occurred.

## Conservative CEGAR transition

For mechanism `m` on source schedule `t`, the dynamic selector antecedent is the conjunction of exact strict order atoms that preserve every selected residual suffix. If a later schedule satisfies this antecedent, it has the same named canonical and physical mechanism. Negating that antecedent therefore removes only schedules already killed by `m`.

Round94 appends the Xerr and Zerr selectors only after both complete formulas, assignments, and physical replays pass. The pending state contains the next source, formula, record, and state hash. Formula compilation and independent encoding checking finish before the state file is atomically promoted last. Later selectors are never applied retroactively.

## Exact order-3 GF(2) theorem

Within one fixed sector, each named location is a GF(2) column. For three selector location sets `A,B,C`, linearity gives

`effect(A) + effect(B) + effect(C) = effect(A Δ B Δ C)`.

Repeated location names cancel because `v+v=0`. This identity is sound only within one fixed sector map. If the symmetric difference contains 1--10 distinct valid names and exact schedule replay returns detector zero and logical nonzero, the result is an ordinary conservative EFSSC.

At the 234-selector frontier there are 125 Xerr and 109 Zerr selectors. `itertools.combinations` visits every unordered distinct same-sector triple, and the observed count equals

`C(125,3)+C(109,3)=527,684`.

Exactly 4,232 triples have a novel exact symmetric difference of weight 1--10; each is unique in this run. Exact iteration-136 replay gives nonzero syndrome for all 4,232, hence zero retained selectors. The conclusion covers exactly this finite order-3 domain. It says nothing about higher closure orders, arbitrary mechanisms, or other schedules.

## Branch consequences

The known achievable floor is 11 and the proved cap is 12. The two exact canonical closure routes are:

1. Universal no-go: establish every legal schedule has `d_circ<=11`, which with the floor yields `D*_Gross=11`.
2. Explicit witness: exhibit a legal schedule with a complete certificate `d_circ=12`, yielding `D*_Gross=12`.

An accepted outer UNSAT over a sound effective-≤10 cover would advance the universal route. A candidate with accepted direct UNSAT in both sectors would license the subsequent repair analysis needed for a distance-12 witness. Neither antecedent occurred. Consequently this package leaves `D*_Gross in {11,12}` and both canonical nodes conjectured.
