# CIRCDIST Gross exact outer/direct continuation — Round96 proposer report

## Exact verdict

**MATERIAL-CHECKED-PROGRESS-NOT-CLOSED.** This package is proposer evidence, not an independently reviewed theorem. All twelve exact outer queries at iterations 148–159 were SAT, and both complete unrestricted direct-360 CSS-sector queries were SAT for every outer model. No outer or direct UNSAT occurred, so no actual Gross DRAT/LRAT certificate exists and neither frozen branch closes. The canonical Gross node and root route remain **CONJECTURED** and the frozen claim remains **D*_Gross in {11,12}**.

The positive mechanisms close only their twelve concrete source schedules. They are not a universal cover and do not narrow {11,12}.

## Commissioned binding and reconstruction

The following inputs were checked byte-for-byte before the first solve and copied into `bindings/`:

- scheduler `3c8965b3cc30f6ebcdc5f051073f2c0eb0dc39d537cd9f3f171633d6eac7bab1`;
- Gross node `f84492190a1dad3b5d69bf38a9a62d3212f0c3844ee3338dc96517fbb0671135`;
- Round95 review `b6a23911b5f9974454a4f4291eaa09e30308547925aa71972d5199e3715c9450`;
- reviewed Round94 root and payload seals `1e0a4af8591aa63ccccd1b2516c630eccb11a73fb9dea2e0ff1e0d32ed82ac1c` and `c39ef3552e461dd7513812b8296901e72369dfacbf6e71ae758b5bb58ed94c54`.

All 1,570 Round94 root rows and 1,569 payload rows were independently rehashed before use. Iteration 148 was verified fresh/unstarted with 14,484 inherited order predicates and 256 exact EFSSC selectors. Its state, selector-state, source-file, source-semantic, and CNF digests are respectively `1902599acc47eb5d354692759b2d09d6ff1cfcd5e013f2b907cc310376ee6e81`, `9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f`, `0db20ed8ca0b120cda91eb7a94be25094adb9b77a2cacdd322e330a720d58b5f`, `2fd4a1982e1f6389804f7eee1120706f9d26c9e6a23acc05e2a15e036a67c032`, and `397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4`. The exact formula has 19,138 assertions, 409,157 variables, and 1,385,059 clauses.

Fresh deterministic compilation was byte-identical to the reviewed decompressed CNF, assertion map, and circuit trace; metadata agreed after excluding runtime-only timing. The independent encoding checker partitioned every clause once, reconstructed every source root, and proved every non-primary variable uniquely defined. See `reconstruction/correspondence.json` and `reconstruction/fresh.encoding_check.json`.

## Exact semantics checked

For a sector-specific set of named elementary fault locations F, the checker separately computes:

`N(F) = symmetric difference of named locations`, `C(F) = XOR of canonical column supports`, and `P(F) = XOR of physical suffix supports`.

A direct SAT witness is accepted only when `1 <= |N(F)| <= 10`, the complete DIMACS assignment satisfies every clause, the frozen schedule is legal, both detector syndromes vanish, both logical actions are nonzero, and canonical and physical logical parities agree. Named fault weight is never replaced by `|C(F)|` or `|P(F)|`. Every direct formula contains all 360 primary fault-selection variables and excludes pool, residual-pattern, check-count, and within-check-order restrictions.

## Exact order-4 synthesis census

Before blind continuation, the package exhaustively enumerated the reviewed post-i136 state137 same-sector order-4 domain. The exact split was independently verified as 125 Xerr selectors and 109 Zerr selectors. Therefore

`C(125,4) = 9,691,375`, `C(109,4) = 5,563,251`, total `15,254,626` unordered distinct quadruples.

The streaming MITM enumerator assigns every quadruple its unique sorted indices `a<b<c<d`, keeps exactly all left pairs `a<b<c`, and combines them only with `c<d`. Observed counts equal both binomial closed forms. It samples nothing.

| sector | full quadruples | named-weight <=10 | unique results | inherited results | novel eligible | canonical syndrome zero | physical syndrome zero | novel retained |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Xerr | 9,691,375 | 32,456 | 32,456 | 0 | 32,456 | 0 | 0 | 0 |
| Zerr | 5,563,251 | 1,304 | 1,304 | 106 | 1,198 | 1 | 1 | 0 |

All eligible exact-name multiplicities were one. Xerr canonical/physical support weights range 2–70/2–72; Zerr ranges 2–74/2–74. Complete support-weight histograms, location-weight histograms, checksums, and logical histograms are retained in `synthesis/order4_gf2_closure.json`. Xerr has no syndrome-zero logical action. Zerr has one conservative valid occurrence with logical action `100110100011`, but its exact named result is inherited; 106 eligible results are inherited in all and no novel predicate survives. Hence **zero selectors were appended from synthesis**.

The census explicitly separates zero named, canonical, and physical support (all zero counts); canonical and physical syndrome; canonical and physical logical triviality; sector; named-set multiplicity; inherited semantic dedup; overlapping pair decompositions; schedule-local validity; and support-weight substitution. Cross-sector XOR is excluded by a retained counterexample. See `SYNTHESIS_PROOF.md`.

## Strict-serial candidate campaign

Weights below are `named/canonical-support/physical-support`. Every syndrome is empty; every shown 12-bit physical logical action is nonzero and equals its canonical action.

| iter | selectors | outer | Xerr | X weights | X logical | Zerr | Z weights | Z logical |
|---:|---:|---|---|---|---|---|---|---|
| 148 | 256 | SAT 5.639071 | SAT 33.494364 | 10/20/22 | `001100000010` | SAT 7.899342 | 9/18/18 | `111110000000` |
| 149 | 258 | SAT 5.057482 | SAT 123.740184 | 10/12/14 | `100111100100` | SAT 22.762779 | 10/14/14 | `001010000000` |
| 150 | 260 | SAT 5.140995 | SAT 9.380263 | 10/18/18 | `000001010000` | SAT 0.022044 | 10/12/16 | `000001000000` |
| 151 | 262 | SAT 6.372336 | SAT 49.026051 | 10/18/14 | `101100000001` | SAT 16.986186 | 10/12/12 | `101001001111` |
| 152 | 264 | SAT 4.132022 | SAT 269.561427 | 10/12/16 | `111100100000` | SAT 7.132050 | 9/16/20 | `000111001011` |
| 153 | 266 | SAT 4.926043 | SAT 48.274864 | 10/16/20 | `000010000110` | SAT 28.221138 | 10/12/18 | `010001000000` |
| 154 | 268 | SAT 4.222385 | SAT 64.901174 | 10/14/18 | `010001110000` | SAT 43.811855 | 10/18/24 | `110011110101` |
| 155 | 270 | SAT 5.802846 | SAT 69.528052 | 10/14/14 | `011001000000` | SAT 27.556769 | 10/12/14 | `011010100100` |
| 156 | 272 | SAT 4.852203 | SAT 332.702697 | 10/14/14 | `100011000100` | SAT 26.966783 | 10/16/14 | `101000000000` |
| 157 | 274 | SAT 3.593457 | SAT 32.962800 | 10/14/18 | `010100001010` | SAT 40.610950 | 10/16/22 | `100000000000` |
| 158 | 276 | SAT 4.251230 | SAT 42.937736 | 10/16/14 | `010101000000` | SAT 32.993615 | 10/16/20 | `101011100001` |
| 159 | 278 | SAT 4.022281 | SAT 39.962030 | 10/16/18 | `001100000010` | SAT 36.085928 | 10/14/12 | `110010000000` |

Totals: 12 complete outer SAT assignments, 24 complete direct SAT assignments, zero UNSAT, zero unknown, zero timeout, zero repair entry. Solver intervals are pairwise non-overlapping. Each iteration appended exactly its two concrete schedule-valid selectors only after both sectors replayed, then atomically promoted a fresh next state.

SAT proof production was enabled on all 36 solver calls. Each SAT-side stream was fully read and summarized by SHA-256, byte count, LF count, and empty-clause count, then deleted because it is not an UNSAT certificate. All 36 summaries report zero empty-clause lines. Fixture controls establish tooling behavior only: valid DRAT and generated LRAT were accepted; corrupt and truncated DRAT and LRAT were rejected.

## Fresh frontier

Iteration 160 is sealed fresh/unstarted with 280 selectors, selector-state `ad3cf364dd9224c14ffb55046ba3dc8eb80035b1eaf997f1d7a5691297ad62a3`, state file `bb26ce4fc03ae9616a6a325438c3f4c82568a15c4fe133e074959b894e358194`, source file `8b754b649744a83eae6c80e64230f9782909b48e5613dcfd6c3c321d98b2dd66`, semantic source `bb19e724c66eb6f3df8830a205ba29a297f5795d42d3fe066fa3b873800789ed`, and CNF `aa18d2857ed5a7aefacd33bf4fbd42fded914393e123a87f00e84e4920e39d59`. Its formula has 19,162 assertions, 411,526 variables, and 1,396,722 clauses. There is no inherited solver, model, proof, or disposition for iteration 160.

## Branch accounting and limitations

The D*=11 branch is not closed because no checked outer UNSAT proves a universal selector cover. The D*=12 branch is not closed because no outer schedule had checked absence in both unrestricted direct sectors, so repair and a distance-12 certificate were never entered. The order-4 no-go applies only to the declared 15,254,626 post-i136, same-sector, four-distinct-selector domain; it says nothing about higher closure order, cross-sector constructions, selectors outside state137, or a universal Gross cover.

The package preserved frozen S_Gross, MC0, terminal residual semantics, both CSS sectors, strict serialization, and all canonical exclusions. It did not use morphing, Circ-Preserve substitution, an alternate conflict model, exploratory pair clauses, retroactive cuts, stale compressor provenance, mixed-sector XOR, support-weight substitution, or schedule-globalized dynamic predicates.

## Reproducibility and repository discipline

The bound interpreter is `/private/tmp/circdist-r72-dispatcher-venv/bin/python` with executable SHA-256 `bdea59019a38eb6600cc9e71e984a97fedadc406448431281e7657030f54987e`, Python `3.9.6 (default, May 22 2026, 11:13:45) `, z3 `5.1.0`, and pysat `1.9.dev15`. Native tool hashes are in `ENVIRONMENT.json`. Full replay rebuilds and checks all 13 exact outer formulas, all 12 candidate chains, all 24 direct formulas, the order-4 census, result/process crosschecks, protected bindings, and proof controls. Repository validators and FIX-2 results are recorded under `verification/` after installation. No canonical file was edited; no commit or push was made.
