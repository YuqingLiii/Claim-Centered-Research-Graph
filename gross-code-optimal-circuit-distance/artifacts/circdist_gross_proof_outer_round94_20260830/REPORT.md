# CircDist Gross Round94 proposer report

## Exact verdict

`MATERIAL-CHECKED-PROGRESS-NOT-CLOSED`.

Round94 establishes twelve further exact, strictly serial CEGAR transitions from the independently reviewed fresh iteration-136 frontier. Every outer query was SAT. Both complete unrestricted direct-360 CSS-sector queries were SAT for every outer candidate, and all 24 direct assignments passed clause checking plus canonical and physical mechanism replay. No actual query was UNSAT, no repair query was licensed, and no absence theorem was obtained.

Therefore `CIRCDIST.gross` and `gap-via-lift` remain `CONJECTURED`, and the only licensed residual is

`D*_Gross in {11,12}`.

This package is proposer evidence. It edits no canonical node, scheduler, review, protocol, prior package, or tool; it creates no commit and performs no push.

## Reviewed starting point and reconstruction

Round94 binds the corrected Round93 frontier exactly. The independently verified state-file hash ends in `ccc8a`; the disclosed `ccc4a` commission spelling is not used.

| object | exact value |
|---|---|
| scheduler SHA-256 | `4da1d0f15ddcdb7542cc69507661231807dad97edf684d578d5010c13b9b2383` |
| Gross node SHA-256 | `c3b03597c496ace59bb84f5d4e4cfb1540b98e193dcba9f67adb0abd657bc3f3` |
| Round93 review SHA-256 | `76a07f9d73fda5ced83818361eed24cd83b4ed7fc5a11c13b0fc027df4feb65d` |
| Round92 root / payload seals | `4e255084bdab13ad0b9c295a9fe7cf2aea8231c4a56db656964f0695ddc6c982` / `fbc881f0dc54744cb3cfd0c4497571592f8597326ce98362eb42a032ed289090` |
| initial state file | `58781b46cc177df046ec334420046e1ccc8a23517f21fe4491e6412741ced57c` |
| initial selector semantic state | `1692d905120d2dcf51b949ce4a70ed4b8f1b270c2d07a1ddbf5813d20d80fa81` |
| iteration-136 source file / semantic | `a71fb5e708eeebf365dda0661b79652b264bc0eb87308626383a5ca389cfc5d8` / `a561515801904b458d34ebccea5aa364420f9a0a012e36e721f48fcbe9be4ebe` |
| iteration-136 CNF | 19,114 assertions; 406,656 variables; 1,372,232 clauses; `289acad6be1068d63369511e9c95b0b1df146471bf05a1e4128758508612b64e` |

The source contains exactly 14,484 inherited order predicates: 1,440 unary, 20 round-62, 12,820 generalized, and 204 dynamic. It begins with 232 exact EFSSC selectors: reviewed 164, reviewed Round92 pre-outer 44, and 24 selectors from iterations 124--135.

Before solving, Round94 independently recompiled the source to CNF, assertion map, and circuit-definition trace. The CNF, map, and trace were byte-identical; metadata agreed after removing only compilation time; the independent encoding checker reconstructed every root and uniquely defined variable. `reconstruction/correspondence.json` records this source/CNF correspondence. The commissioned iteration had no model, proof, solver status, or inherited disposition.

## Exact query semantics

For selector prefix `P`, the finite outer formula is

`exists t in S_Gross: inherited_blocks_miss(t) and every p in P is invalid on t`.

The frozen universe has 864 interaction times, all 648 MC overlaps, MC0, the licensed global interleaving, strict schedule serialization, fixed terminal residual conventions, both CSS sectors, and all canonical exclusions. The 10-bit Tseitin CNF is an exact projection: every legal bounded schedule extends uniquely through the definitional variables, and every CNF model projects to such a schedule.

For a fixed candidate schedule and sector, the complete direct-360 formula ranges over every one of the 360 named elementary fault locations. It imposes exact weight at most 10, zero detector syndrome, and nonzero logical action. It has no pool, residual-pattern, check-count, or within-check-order-family restriction. A direct SAT assignment is a positive mechanism only. The mechanism's ordered hook suffixes are replayed against the physical schedule, and zero physical syndrome, nonzero physical logical action, canonical/physical parity equality, and exact named-location weight are checked.

A positive mechanism creates one dynamic EFSSC whose antecedent is the exact conjunction of source-schedule order atoms. Its exclusion is conservative: any schedule retaining those atoms retains that named mechanism. It kills only that concrete outer candidate domain and proves no global absence. Both sectors are fully adjudicated before the two selectors are appended, and the state is promoted last through a checked pending commit.

## Iteration-136 solve boundary

The first proof-enabled CaDiCaL invocation returned SAT (`10`). Two complete DIMACS decodings independently satisfied all 1,372,232 clauses and mapped to the same legal frozen schedule. The direct sectors were then built without restriction.

- Xerr: SAT, exact weight 10: `D:38,D:109,R:25:0,R:26:2,R:28:0,R:35:1,R:35:2,R:39:1,R:41:0,R:45:2`.
- Zerr: SAT, exact weight 10: `D:45,D:98,D:104,D:110,D:115,D:119,D:121,R:4:0,R:30:0,R:35:1`.

Both complete assignments satisfied every direct clause and passed canonical and physical replay. This licensed exactly `r94-i136-Xerr` and `r94-i136-Zerr`, installed by the checked 136→137 atomic transition.

## New exact higher-order investigation

Before blind repetition, Round94 investigated exact order-3 same-sector GF(2) closure at the 234-selector post-iteration-136 frontier. See `SYNTHESIS_PROOF.md` and `synthesis/triple_gf2_closure.json`.

The finite domain is every unordered three-element subset within each sector:

`C(125,3) + C(109,3) = 527,684`.

Every triple was enumerated exactly once. Its named-location set was the exact symmetric difference. Of the full domain, 4,232 triples produced a novel result with exact named-location weight 1--10. All 4,232 unique results were replayed on the frozen iteration-136 schedule; every one had nonzero detector syndrome, so zero selectors were retained. This is a checked no-go only for the declared order-3 domain. It does not cover order 4 or higher, arbitrary mechanisms, mixed sectors, or global exhaustion.

Exact counterexamples reject three tempting relaxations:

1. Cross-sector XOR lacks a sector-independent column effect.
2. A source-valid selector can be invalid on iteration 136, so dynamic predicate validity cannot be globalized.
3. Named fault count can differ from net data-support weight, so support weight cannot replace the direct weight.

No heuristic, sampled, overweight, mixed-sector, or schedule-globalized predicate entered the state.

## Strict serial campaign

Every outer solver ran with textual proof production enabled. Each SAT assignment was checked before either direct sector was started. Xerr and Zerr were run one after the other; both were replayed before a pending transition was built; the next source/CNF was compiled and independently checked before the state became visible. The independent audit proves that the 36 solver child intervals do not overlap.

| iteration | outer | Xerr | Zerr | transition |
|---:|---|---:|---:|---|
| 136 | SAT | 10 | 10 | 232→234 |
| 137 | SAT | 10 | 10 | 234→236 |
| 138 | SAT | 9 | 10 | 236→238 |
| 139 | SAT | 10 | 10 | 238→240 |
| 140 | SAT | 10 | 10 | 240→242 |
| 141 | SAT | 10 | 10 | 242→244 |
| 142 | SAT | 10 | 10 | 244→246 |
| 143 | SAT | 10 | 10 | 246→248 |
| 144 | SAT | 10 | 10 | 248→250 |
| 145 | SAT | 10 | 10 | 250→252 |
| 146 | SAT | 10 | 10 | 252→254 |
| 147 | SAT | 10 | 10 | 254→256 |

The iteration-138 Xerr weight-9 mechanism is positive evidence about that candidate, not an absence proof and not a reason to narrow `D*_Gross`.

## Proof-output disposition

There are 36 actual proof-enabled SAT invocations: 12 outer and 24 direct. Each SAT-side stream was fully iterated, hashed, byte-counted, LF-counted, and checked to contain no empty-clause line. Because these are SAT runs, the streams are not refutation certificates. They were deleted only after the complete assignments, formulas, legal schedules, and physical mechanisms were independently checked. Their exact disposition records remain beside each query.

No actual Gross DRAT or LRAT proof exists because no actual query returned UNSAT. The packaged proof fixture accepts a valid DRAT, generates and accepts LRAT, and rejects corrupt and truncated DRAT and LRAT. Those controls demonstrate the toolchain only.

## Branch accounting

The canonical Gross claim says `D*_Gross=12` requires an explicit legal interleaved schedule with certified `d_circ=12`, while `D*_Gross=11` requires a proof that every legal schedule has `d_circ<=11`, together with the already certified achievable floor 11.

- The `D*=11` branch did not close: no proof-checked outer UNSAT established a universal cover by effective weight-≤10 mechanisms.
- The `D*=12` branch did not close: no outer candidate had checked direct absence in both CSS sectors, so repair analysis was never licensed and no schedule obtained a `d_circ=12` certificate.
- Twelve SAT/direct-SAT transitions show only that the current finite selector union did not yet cover each encountered schedule and that each schedule had concrete low-weight mechanisms.

No solver text is used to infer `D*`; every scientific statement above is tied to a formula, assignment, replay, or finite enumeration.

## Fresh frontier

The checked continuation frontier is deliberately unstarted iteration 148:

| field | exact value |
|---|---|
| selectors | 256 |
| selector semantic state | `9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f` |
| state file | `1902599acc47eb5d354692759b2d09d6ff1cfcd5e013f2b907cc310376ee6e81` |
| source file | `0db20ed8ca0b120cda91eb7a94be25094adb9b77a2cacdd322e330a720d58b5f` |
| source semantic | `2fd4a1982e1f6389804f7eee1120706f9d26c9e6a23acc05e2a15e036a67c032` |
| exact CNF | 19,138 assertions; 409,157 variables; 1,385,059 clauses |
| CNF SHA-256 | `397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4` |
| solver/model/proof disposition | absent |

There is no `iterations/iter148` directory and no pending state.

## Reproduction

The package contains the frozen physical-model vendor, deterministic compiler and encoding checker, direct builder and physical replay code, native arm64 macOS CaDiCaL/DRAT/LRAT tools, every formula and assignment, and the complete state chain. The external interpreter remains necessary and is explicitly bound in `ENVIRONMENT.json`:

`/private/tmp/circdist-r72-dispatcher-venv/bin/python`

with Python 3.9.6, z3 5.1.0, and pysat 1.9.dev15. Run:

```sh
CIRCDIST_PYTHON=/private/tmp/circdist-r72-dispatcher-venv/bin/python ./replay.sh
```

Replay checks the package manifests when present, live protected bindings, all Round92 manifest rows, all thirteen source/CNF correspondences, all twelve outer assignments and schedules, all twenty-four rebuilt direct formulas and assignments, every physical replay, every atomic state transition, the exact triple domain and controls, the result/process ledgers, and proof-tool controls.

## Limitations

Round94 gives checked computational progress, not a theorem closing the quantified schedule universe. The triple result is a finite-domain no-go, not a global closure invariant. Positive mechanisms establish no absence. SAT-side traces establish no refutation. The recorded Python venv is an explicit portability dependency. Independent review is required before any canonical link or promotion.
