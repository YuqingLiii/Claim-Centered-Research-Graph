# Gross global-closure proposal, Round 102

## Verdict

**MATERIAL-CHECKED-GLOBAL-PROGRESS-NOT-CLOSED.** Neither permitted Gross root
branch is proved.  No legal distance-12 witness was certified, and no proof was
obtained that every legal frozen schedule has circuit distance at most 11.
Accordingly `CIRCDIST.gross` and `gap-via-lift` remain **CONJECTURED**, and the
only justified distance statement remains

\[
D^*_{\mathrm{Gross}}\in\{11,12\}.
\]

The new root-level result is an exact, independently checked
\(\mathbb Z_{12}\times\mathbb Z_6\) action, full invariant closure of the
installed blocks and selectors, and an equisatisfiable lex-leader quotient.
The corrected quotient is SAT, and both complete unrestricted direct-360
queries on its schedule are SAT.  Those outcomes prevent a closure claim.

## Protected inputs

The scheduler, canonical Gross node, commissioned Round-101 review, protocols,
schema, and repository gate tools were snapshotted and treated read-only.  The
three dispatch identities are:

| input | SHA-256 | bytes | LF |
|---|---|---:|---:|
| `operations/circdist/SCHEDULER.yaml` | `02cb4b7a02963451adf962dfc59fa3eb11ef8f71d7b2b2c49d89e6bc61e2c8f5` | 274,811 | 3,257 |
| `circdist/proof-dag/nodes/CIRCDIST.gross.yaml` | `09290d2fb1d4f3c97e0ce503f9f5750a090df1b34b0114dcc9c6542733476dd4` | 92,199 | 992 |
| Round-101 exact review | `8eb817e0af24df1d17af5cdd778cfa7180a1c6c60ca6c87d81ad3c5ad549ca88` | 159,949 | 1,684 |

`bindings/LIVE_GOVERNANCE.json` binds twelve protected files.  Both the
preseal replay and repository gates rechecked their live bytes against the
snapshots.

## Mandatory iteration 184

Iteration 184 was the first scientific solve.  It bound exactly 14,484
reviewed order predicates, 328 exact selectors, selector-state SHA-256
`7296aa70690e01852519b78826b173af35998cec0e9c124c46ea30101dd0777d`,
state SHA-256
`3b128ef192074a3bc0c163502e97eff99ab9d15c546381e98e1e178471552d7b`,
source SHA-256
`5eb1607bebea7bfc44b693a4a3a9ae19f2ab5ae498407290863b34d6eb9b66b0`,
semantic source SHA-256
`d601f297e8b2a1b7d6179d19452da8b0abca2e4f16d7404b6395a8254e949268`,
and CNF SHA-256
`2b0030fd15b0ef8154e2dbc37508e03481f11d8c876c4fe59e6541cb3bfacd62`.
The formula has 19,210 source assertions, 415,793 variables, and 1,416,404
clauses.  Proof output was enabled on every solver command from launch.

The outer query returned SAT (PID 41074, rc 10, 3.195227 seconds).  Its complete
assignment satisfies every clause.  Frozen replay found a legal 864-edge
schedule with 123 used layers, maximum time 122, no reviewed-block hit, no
installed-selector hit, and compressed schedule SHA-256
`5c13a6ef32fec263f6cdc5d10db1da30d6758a79f089194814fe99e360d55c23`.

Both complete unrestricted direct-360 formulas returned SAT:

| sector | formula SHA-256 | vars / clauses | named mechanism | canonical / physical weight | logical vector | block atoms |
|---|---|---:|---|---:|---|---:|
| Xerr | `40bcf7fc4e701d496c03d521324c5b7d88e094b5a350dbfb1f25468e1bea0b63` | 5,935 / 22,320 | `D:129 R:1:0 R:2:0 R:3:2 R:9:1 R:18:2 R:44:2 R:53:2 R:55:0 R:61:0` | 18 / 26 | `100000011111` | 73 |
| Zerr | `539289f9eccfd06d9c71e046fd62b2ec7140c09f5250f5761d9d5c55698b1f49` | 5,904 / 22,196 | `D:47 D:90 D:113 D:143 R:3:2 R:13:0 R:17:2 R:37:0 R:38:0 R:45:0` | 12 / 20 | `111110111111` | 48 |

Each mechanism has ten distinct named faults, zero canonical and physical
detector syndrome, and the displayed nonzero canonical/physical logical
vector.  The assignments satisfy every DIMACS clause.  Only after both sectors
were adjudicated, the two exact source-schedule-valid selectors were staged
and atomically installed in the package-local iteration-185 frontier.  Repair
was forbidden and was not entered.  `ITERATION184_DISPOSITION.md` records the
full supports, commands, streams, and transition identities.

## Exact root-level mechanism

The package proves four linked statements.  Complete definitions, equations,
proofs, algorithms, and check counts are in `GLOBAL_TRANSLATION_THEOREM.md`.

1. The maps induced by modular translation on the 12-by-6 check torus and two
   data sheets form a 72-element group action by edge, check, qubit, detector,
   logical-row, and direct-column bijections.
2. Legal schedules and named direct mechanisms are equivariant.  Translation
   preserves distinct-name weight, zero syndrome, and nonzero logical effect.
3. Exact orbit closure makes the installed outer registry invariant.  Identity
   and collision decisions use full normalized tuples; SHA-256 values are
   checked labels rather than identity oracles.
4. The 71 exact lex leaders choose the unique minimum schedule vector in every
   finite orbit.  Their recurrence has a unique definitional extension, so the
   quotient is equisatisfiable with the invariant base and every representative
   lifts to all legal schedules in its orbit.

The independent action checker covered 72 edge bijections, 864 identity edge
cases, 4,478,976 edge-composition cases, 20,736 geometry/incidence cases,
46,656 overlap cases, 10,368 detector-row permutations, 51,840 direct-column
equivariance cases, and 144 translated direct witnesses.

### Invariant registry closure

The corrected closure started from 14,484 block records (14,477 distinct
semantics because seven historical records duplicate existing semantics) and
474 selectors.

| object | parent-translation pairs | unique output | collisions | orbit histogram |
|---|---:|---:|---:|---|
| blocks | 1,042,848 | 517,140 | 525,708 | 90 parents of size 36; 14,394 of size 72 |
| selectors | 34,128 | 23,868 | 10,260 | one parent of size 36; 473 of size 72 |

The unique blocks comprise 1,440 unary, 900 round-62, 500,868 generalized,
and 13,932 dynamic semantics.  Selectors comprise 12,492 Xerr and 11,376 Zerr.
The independent checker proved exact expected/observed set equality, replayed
all 541,008 provenance records, and checked generator invariance in 1,034,280
block plus 47,736 selector cases.

The invariant base source has SHA-256
`a381709cb972a0ba693269bd47020dd02e32a3f7685b09d2d052c7d06c39504f`
and semantic SHA-256
`9129c5794edf809e8caeee788caa04204ad70a220b55859434a367f75ae0694e`.
Its exact CNF has SHA-256
`00a5f305166aded035442f689f2d8bd13d52622a258733e18342cb7ca3608dd9`,
545,406 assertions, 1,834,360 variables, and 6,867,095 clauses.

### Corrected quotient and SAT model

The quotient adds exactly 613,440 recurrence variables, 4,907,520 definition
clauses, and 71 roots.  Its SHA-256 is
`f6dec16c6ee19ee1a041d3eb78786171558f54805c3038ce9c311c62b82d7c13`,
with 2,447,800 variables and 11,774,686 clauses.  The independent checker
reconstructed all 4,907,591 appended clauses, verified the base prefix, all 16
local truth-table cases, unique extension, signed-integer bounds, and streaming
memory use.

CaDiCaL PID 42419 returned SAT (rc 10) in 854.453879 seconds.  The retained
assignment contains all 2,447,800 variables and satisfies all 11,774,686
clauses.  Orbit controls independently rechecked every clause, all 8,640
primary time bits, 613,440 recurrence values, all 71 roots, a free orbit of 72
distinct schedule vectors, and lex minimality.  Corrupt, truncated, reversed
direction, and missing-root controls were rejected.  Frozen replay produced a
legal 483-layer schedule with SHA-256
`f6a806a1b90535d497da63b154960f9ebf172c6c740356470cdeda56866bd5cf`
and no invariant block or selector hit.

The earlier 330-selector quotient was discovered to be non-invariant.  Its
global quotient claim was retracted immediately and is not used.  Its schedule
and physically replayed direct mechanisms remain legal point evidence only.

## Corrected candidate direct adjudication

Both exact direct formulas use all 360 named columns, exact
`sum(select) <= 10`, all 72 syndrome rows, all 12 logical rows, and no pool,
residual-pattern, check-count, or within-check-order restriction.

| sector | CNF SHA-256 | vars / clauses | default proof-mode attempt | unchanged-CNF retry |
|---|---|---:|---|---|
| Xerr | `af4d1bddab1993402cd5b7118e4b9106416e14d06d09a61fb1f7d35ae4b92bb2` | 6,141 / 23,144 | PID 42760, rc 0/UNKNOWN, 890.049392 s | PID 43428, rc 10/SAT, 1,353.690736 s |
| Zerr | `0e44f84f95fdf9adf7c28aba6243b8cafc5056ba2fbb0279896a2b2c2ebc88a3` | 6,146 / 23,164 | PID 43068, rc 0/UNKNOWN, 890.056241 s | PID 43871, rc 10/SAT, 53.452524 s |

The UNKNOWN outputs are incomplete time-bounded prefixes and support no
absence statement.  The retries used the unchanged formulas, `--unsat` mode,
disabled binary proof format, and proof output from launch.  Complete SAT
assignments passed all clauses and physical replay:

| sector | named-weight-10 mechanism | canonical / physical weight | physical logical vector | exact block atoms |
|---|---|---:|---|---:|
| Xerr | `D:19 D:44 D:53 D:130 D:135 R:1:2 R:23:2 R:48:0 R:56:1 R:63:2` | 16 / 18 | `111001111100` | 41 |
| Zerr | `D:40 D:43 D:51 D:106 D:109 D:113 D:117 D:125 R:43:0 R:53:0` | 12 / 16 | `100111000000` | 16 |

Both canonical and physical syndromes are zero.  Both mechanisms are
nontrivial.  Because both direct queries are SAT, repair remains forbidden and
the corrected candidate is not a distance-12 witness.

## Fresh unstarted frontier

After both corrected direct sectors were SAT and replayed, the two mechanisms
were translated through all 72 group elements.  All 144 source schedules are
legal; all 144 translated selectors have ten distinct names, zero syndrome,
and nontrivial logical effect.  Each parent has orbit size 72 and there are zero
selector collisions.  Adding them yields 24,012 selectors while retaining all
517,140 invariant blocks.

Iteration 187 is sealed **unstarted**:

| item | identity / count |
|---|---|
| source SHA-256 | `d7a1f6bf63b328627362a70518f5beb77d3b4b32241ccaaab83d6d5d5c122124` |
| semantic SHA-256 | `88c726321144b782ce7fb72d8b1ed0d361473ab6587bb7f3ba8ec6cd0079dfa3` |
| state SHA-256 | `b7fa430f67bdcb8fdb034c8e42174ee219d0d77ecdbe57f99576de1518de9bea` |
| selector-state SHA-256 | `7667fc8230b67224b1895180764680c5000dcef34b3c67352f904e5998e8879b` |
| base CNF | `7f66b46643b6b10cce57358e4e66f7e95cdc1bfe52ee14f77884c56ddd5d5eab`; 1,838,894 vars / 6,882,039 clauses |
| lex quotient | `e415b4c2c5b4923a47348a06ea9ebb06bbc85cea2c9c32bd3a9b25a1ce198234`; 2,452,334 vars / 11,789,630 clauses |

The base independent audit reconstructed all 545,550 source assertions, 1,830,214 definitions,
all variables, and all clauses, including five negative controls.  The quotient
audit reconstructed all 4,907,591 appended clauses and rechecked the complete
group action.  No solver was launched on either fresh formula.

## Proofs, controls, streams, and replay

No Round-102 root query returned UNSAT.  Therefore this package contains no
Gross absence certificate and makes no absence claim.  SAT-side and UNKNOWN
solver streams were retained losslessly with explicit dispositions.  Each raw
stream was deterministically gzipped in fixed-size chunks, fully decompressed,
rehash/recount checked, and only then was the raw file removed.

The proof tool chain was tested on a finite pigeonhole fixture.  Valid DRAT was
accepted, converted to LRAT, and the LRAT was independently accepted.  Corrupt
and half-truncated DRAT and corrupt/truncated LRAT were rejected.  These are
tool-chain controls only.

The final preseal replay ran 13 children serially.  It regenerated iteration
187 byte-for-byte, rechecked invariant closure and both quotient encodings,
revalidated the complete corrected SAT model, replayed the iteration-184,
exploratory, and corrected direct candidates physically, and reran proof
controls.  Every child returned 0, was reaped, and was not detached.

The final read-only repository gate wrapper ran 11 serial children.  Proof-DAG
checks for `circdist` and `all`, migration, release and DAG contracts, Lean DAG
self-test, duplicate-YAML scan, `git diff --check`, and live-governance checks
all returned 0.  Evidence closure returned its expected proposer-stage rc 1;
the independent parser found 688 unique diagnostics, all under this sole new
unlinked package.  The wrapper therefore reports PASS without treating those
diagnostics as canonical evidence closure.

The retained process ledger contains 106 wrapper records and eleven science
solver intervals.  Every PID-bearing child is reaped, no retained child is
detached, no wrapper timed out, and no solver intervals overlap.  The final
process census found zero matching live science processes.  The corrected
cleanup audit found zero package/system scratch survivors and zero raw
corrected solver streams.

## Failures and corrections

`FAILURE_LEDGER.md` retains thirteen failures/corrections.  The scientifically
material correction was the discovery that the first quotient registry was
not invariant.  The corrected experiment closes every block and selector orbit
before adding lex leaders.  Other failures were environment/path/schema/control
or time-bounded solver attempts; no failed attempt is used as positive evidence.

## Exact residual

The smallest honest residual is the fresh, invariant, unstarted iteration-187
quotient.  Solving it with proof output from launch will either produce another
canonical candidate or a checkable UNSAT certificate for the fully installed
orbit-closed exclusions.  Even a quotient UNSAT result must be stated with the
exact theorem supplied by the sound installed exclusions; fixed-basis span,
fixed-schedule, sampled, heuristic, candidate-only, and mixed-sector results do
not close the root.

No canonical YAML, scheduler, protocol, or review was modified.  The proposed
canonical change is recorded separately and deliberately preserves both
CONJECTURED statuses and the bound `D*_Gross in {11,12}`.
