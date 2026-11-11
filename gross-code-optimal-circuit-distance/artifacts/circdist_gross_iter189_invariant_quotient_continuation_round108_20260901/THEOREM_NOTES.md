# Round108 theorem notes

## Objects

Let `G = Z_12 x Z_6`, `|G|=72`. Let `E` be the ordered 864-edge frozen interaction set. A bounded schedule is `S in [0,1023]^E`; `v(S)` is its fixed ordered ten-bit vector. The retained source defines `Legal(S)` through exact geometry, distinctness, MC, overlap, whole-check and global-interleaving predicates plus installed exclusion roots.

Let `B_189` be the iteration-189 base CNF and `Q_189` its quotient. Their checked dimensions and hashes are:

- `B_189`: `(1,847,301 variables, 6,909,336 clauses)`, SHA-256 `f5ccbe6aa4c0a0df5940cd979809003182416900e76a6cc6e3755e493cc6b178`;
- `Q_189`: `(2,460,741 variables, 11,816,927 clauses)`, SHA-256 `3ece12a1ea0ee6502982fecfcaf75debae985ea2ddff93ea3b875552c0714df7`.

`Q_189 = B_189 AND (AND_{g != e} v(S) <=_lex v(g.S))`, encoded by 71 lex roots and a uniquely determined definitional recurrence.

## Lemma 1 — source/base bijection

The independent source compiler audit streams every retained assertion and definition. It matches all 545,838 roots and all 6,909,336 clauses of `B_189`, including negative controls. Therefore projection of a CNF model to the primary schedule bits is a bounded legal source schedule satisfying exactly the installed exclusions, and every such source schedule has one auxiliary extension.

## Lemma 2 — action and registry invariance

For every `g,h in G`, the reconstructed edge map is a bijection and `g.(h.e)=(g+h).e`; 72 edge bijections, 4,478,976 composition cases and 864 identity cases pass. Geometry incidence, overlaps, detector rows, logical rows and all 720 direct columns are equivariant. All 517,140 blocks and 24,300 iteration-189 selectors are closed under the two generators and therefore under `G`.

## Lemma 3 — quotient/base equisatisfiability

For a base model `S`, the finite orbit `{g.S:g in G}` has at least one lexicographically least vector. Choose a minimizer `g0`; invariance from Lemma 2 gives `Base(g0.S)`. Minimality gives `v(g0.S)<=_lex v(h.g0.S)` for every nonidentity `h`, so `g0.S` extends uniquely to a quotient model. Conversely, deleting the lex extension from any quotient model leaves a base model. Thus `SAT(B_189) iff SAT(Q_189)`. Stabilizer ties do not alter the schedule vector and do not affect the implication.

## Lemma 4 — checked quotient model

The retained assignment assigns variables `1..2,460,741` exactly once. Streaming clause evaluation checks 11,816,927 terminated clauses and finds none false. The reconstructed schedule is legal: 864 edges, 448 used layers, bounds `[0,447]`, zero conflicts, zero MC violations, 648 overlap pairs, 125 overlap-interleaving pairs, 409 whole-check-interleaving pairs, and passing global interleaving. All 71 quotient roots hold; the orbit has 72 distinct vectors and trivial stabilizer.

Therefore `Q_189` and `B_189` are SAT. This immediately rules out entering branch B at iteration 189.

## Lemma 5 — complete direct SAT mechanisms

For each sector, the builder enumerates the unrestricted 144 data columns plus all retained hook columns for 360 total columns and encodes exactly ten selected names, zero detector syndrome and nonzero logical class. Complete assignments satisfy every clause:

- Xerr: 6,102 variables, 22,988 clauses; selected `D:48 D:60 D:63 D:66 D:89 D:105 D:138 D:143 R:4:2 R:55:0`;
- Zerr: 6,100 variables, 22,980 clauses; selected `D:48 D:90 D:93 D:96 D:105 D:131 R:4:1 R:5:0 R:7:1 R:14:0`.

Independent standard-library reconstruction yields empty canonical and physical syndromes and nonzero logical parity. Row-reduction places neither physical support in the stabilizer span. Thus each selected set is an explicit weight-10 adverse mechanism for this schedule.

Consequently the candidate's circuit distance is at most 10 under the complete direct mechanism semantics and it cannot be used for branch A. This candidate-specific conclusion does not change the campaign interval.

## Lemma 6 — atomic orbit cuts

For each parent mechanism `m`, exact translation replay finds `Stab_G(m)={e}`. Orbit-stabilizer gives `|G.m|=72`. Normalized semantic tuple comparison finds no duplicate against the old registry and no collision between the Xerr and Zerr orbits. Every translated mechanism remains named, weight 10, zero-syndrome and nonstabilizer on its translated legal schedule. Appending both full orbits therefore adds exactly 144 selectors and preserves invariance:

`24,300 + 72 + 72 = 24,444`.

No partial orbit is installed.

## Lemma 7 — fresh iteration-190 formula

The post-addition source has SHA-256 `5231e7f5b4cd2a74390a5d137b9927276ce73829dc599ddc064ab8f2c94a2d2e`; its full registry is invariant. The independently checked base has SHA-256 `e3ec0d0b146fc4ade428052d1a14737ffade9974dfc37dd79fa8411841d45fc8`. The quotient checker replays the 72-element action, preserves the exact base prefix, reconstructs all 4,907,591 appended clauses, and proves unique extension and finite-orbit equisatisfiability for quotient SHA-256 `12f2fe58f4bfcaff19d543cdb60411f1659e86c8b4f16f599a2d1679aeeca767`.

The exact file allowlists contain no solve output. Hence iteration 190 is fresh and unstarted.

## Root theorem status

Branch A requires an explicit legal candidate with both complete unrestricted direct sectors certified UNSAT and all circuit obligations independently replayed. Lemma 5 gives the opposite outcome for this candidate. Branch B requires certified UNSAT of the exact quotient plus the universal lifting composition. Lemma 4 gives SAT. Therefore neither branch is proved.

The licensed statement remains:

`CIRCDIST.gross = CONJECTURED`, `gap-via-lift = CONJECTURED`, `D*_Gross in {11,12}`.

The package proves only the material continuation: exact iteration-189 exclusion, exact full-orbit update, and exact fresh iteration-190 frontier. SAT proof-side streams are search traces; proof-tool controls are not Gross certificates.
