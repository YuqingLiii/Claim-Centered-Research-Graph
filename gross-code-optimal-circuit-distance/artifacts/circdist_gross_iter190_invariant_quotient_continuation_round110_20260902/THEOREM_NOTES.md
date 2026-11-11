# Round110 public theorem derivation

## Definitions

Let `G = Z_12 x Z_6`, so `|G|=72`. Let `E` be the frozen ordered set of 864 interaction edges. A bounded schedule is `S in [0,1023]^E`, and `v(S)` is its ordered 8,640-bit time vector. `Legal_190(S)` denotes the conjunction represented by the reviewed iteration-190 source: geometry and edge completeness, time bounds, conflict freedom, MC constraints, overlap and whole-check interleaving, global interleaving, 517,140 reviewed block exclusions, and 24,444 named mechanism selectors.

Let `B_190` be the base CNF and

`Q_190 = B_190 AND product_{g in G, g != e} [v(S) <=_lex v(g.S)]`.

The retained hashes are `sha256(B_190)=e3ec0d0b146fc4ade428052d1a14737ffade9974dfc37dd79fa8411841d45fc8` and `sha256(Q_190)=12f2fe58f4bfcaff19d543cdb60411f1659e86c8b4f16f599a2d1679aeeca767`.

## Proposition 1 — source/base correspondence

The streaming compiler checker independently reconstructs every source assertion, definition, and DIMACS clause. Counts agree at 545,982 assertion roots, 1,850,757 variables, and 6,920,296 clauses; assertion-map and definition hashes agree. Thus a `B_190` model projects to exactly one bounded schedule satisfying `Legal_190`, and every such schedule has the encoded auxiliary extension.

## Proposition 2 — full registry soundness and invariance

The action checker reconstructs 72 edge bijections, 864 identity cases, and 4,478,976 composition cases `g.(h.e)=(g+h).e`. The two generators preserve all 517,140 unique block tuples (1,034,280 cases) and all 24,444 unique selector tuples (48,888 cases). Since `(1,0)` and `(0,1)` generate `G`, the whole registry is `G`-invariant. Selector semantic hashes, named-fault uniqueness, weight at most 10, and exact source/state hashes all agree.

## Proposition 3 — quotient equisatisfiability

Every finite orbit `{g.S:g in G}` has a lexicographically least schedule vector. Registry invariance from Proposition 2 preserves `Legal_190` under translation. Translating a base model to any minimizer therefore yields a base model satisfying all 71 lex leaders and hence a quotient model. Conversely, deleting the lex recurrence variables and roots from any quotient model gives a base model. The recurrence truth table has a unique extension. Therefore `SAT(B_190) iff SAT(Q_190)`, including stabilizer ties.

## Proposition 4 — checked quotient model

The retained assignment covers exactly variables `1..2,464,197`; streaming evaluation checks all 11,827,887 clauses and finds none false. Physical reconstruction gives 864 edges, 477 used layers, zero conflicts/errors/MC violations, and all frozen interleaving predicates. All 71 root recurrences and 613,440 recurrence values agree. Hence `Q_190` and `B_190` are SAT, excluding branch B at iteration 190.

## Proposition 5 — explicit candidate-killing mechanisms

For each sector the unrestricted direct formula reconstructs all 360 primary columns and encodes `sum(select)<=10`, zero 72-row detector syndrome, and nonzero 12-row logical parity. Complete satisfying assignments select:

- Xerr: `D:14 D:29 D:35 D:78 D:88 D:103 D:120 R:5:1 R:26:0 R:67:2`;
- Zerr: `D:0 D:65 D:75 D:131 D:133 D:137 D:138 D:140 R:2:0 R:7:2`.

The Xerr canonical/physical supports are `[1, 14, 29, 35, 69, 74, 78, 79, 88, 89, 101, 103, 104, 120]` and `[1, 14, 27, 28, 29, 35, 44, 69, 74, 78, 79, 88, 89, 103, 110, 120]`; the Zerr supports are `[0, 1, 5, 65, 67, 72, 75, 131, 133, 137, 138, 140]` and `[0, 1, 62, 65, 67, 68, 73, 75, 128, 131, 133, 137, 138, 140]`. Independent reconstruction gives empty syndrome and nonzero logical vector in both canonical and physical semantics, and row reduction proves neither support is in the stabilizer span. Thus the candidate has a legal adverse mechanism of named weight 10 in each sector. It is not a distance-12 witness, so branch A does not close.

## Proposition 6 — complete free-orbit exclusion update

For each parent mechanism, exact translation finds trivial stabilizer. Orbit-stabilizer gives `|G.m|=72`. All 144 normalized tuples are distinct from the old 24,444 selectors and from one another. Translation replay preserves schedule legality, fault-name cardinality, syndrome zero, logical nontriviality, and physical nonstabilizer status. Adding both whole orbits therefore yields exactly 24,588 selectors and preserves `G`-invariance.

## Proposition 7 — fresh iteration-191 formula

The updated source has SHA-256 `0b0ac7e6daa69d8d3ab1b98b7228c43690a5406c52defe57e46027b185984a47`. Its source/base bijection checker accepts base SHA-256 `d1e68e88eb4c22ffda58d3a1c73cb7dbf6082690c594e8c538f8cc70c432e223` with 1,853,886 variables and 6,929,888 clauses. Its action/quotient checker reconstructs the exact base prefix, 613,440 added variables, 4,907,520 definition clauses, 71 root clauses, unique recurrence extension, and finite-orbit equisatisfiability for quotient SHA-256 `30ce7d14d96349e61d7105255cddc8899b8927ce728dfd147b641c75c97fe10f`. Its state is fresh/unstarted and contains no solve artifact.

## Licensed conclusion

The propositions establish a material continuation, not root closure. Branch A is false for this candidate; branch B is unavailable because `Q_190` is SAT. Therefore the canonical statements remain exactly

`CIRCDIST.gross = CONJECTURED`, `gap-via-lift = CONJECTURED`, `D*_Gross in {11,12}`.

No inference depends on private reasoning. The package exposes definitions, checked objects, algorithms, counts, hashes, counterexamples, and replay programs needed to audit each public step.
