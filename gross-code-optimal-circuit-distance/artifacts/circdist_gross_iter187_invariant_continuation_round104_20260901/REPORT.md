# CIRCDIST Gross Round104 exact iteration-187 continuation

## Verdict

**MATERIAL-CHECKED-CONTINUATION-NOT-CLOSED.** The exact iteration-187
full-invariant lex quotient is SAT. Its decoded schedule is legal, but both
complete unrestricted direct sectors are SAT with independently replayed
weight-10 nontrivial undetected mechanisms. The candidate is not a distance-12
circuit. Both 72-element selector orbits were added with zero collisions, the
entire block/selector registry remains invariant, and an exact checked,
unstarted iteration-188 quotient is frozen.

The root did not close. `CIRCDIST.gross` and `gap-via-lift` remain
`CONJECTURED`, with

\[
D^*_{\mathrm{Gross}}\in\{11,12\}.
\]

## Immutable inputs

| input | SHA-256 | disposition |
|---|---|---|
| `operations/circdist/SCHEDULER.yaml` | `d9bcb7affe40ed12a479785f5a102673108b4322fe0d20a1cf6da4483069c31f` | Round104 pending, budget 129/130 |
| canonical Gross node | `dd367bf93e59e10588a824d4f530a0b07c3707d43886004bb3ddb754f0ff7d91` | read-only |
| Round103 exact review | `a7e027b228d785fae5280b33ab95f7999bb4e9b3e001cd30a5816444637db48e` | read-only |
| Round102 root `SHA256SUMS.txt` | `80e70f62075a852355029b765cbe7ebfa4f8156d25b6d9fa2ea1ddbb9e19b4f4` | all 724 rows rehashed |
| iteration-187 base CNF | `7f66b46643b6b10cce57358e4e66f7e95cdc1bfe52ee14f77884c56ddd5d5eab` | 1,838,894 variables; 6,882,039 clauses |
| iteration-187 quotient CNF | `e415b4c2c5b4923a47348a06ea9ebb06bbc85cea2c9c32bd3a9b25a1ce198234` | 2,452,334 variables; 11,789,630 clauses |

The starting quotient directory contained exactly `independent_check.json`,
`metadata.json`, `outer.cnf`, `translation_roots.jsonl`, and
`translation_trace.json.gz`. There was no solver log, assignment, candidate,
proof stream, or replay file. The bound state said iteration 187, `started:
false`, 517,140 blocks, and 24,012 selectors. `INPUT_BINDINGS.json` records
sizes, line counts, tool hashes, and the complete file-set check.

## Strict-serial protocol

Every scientific child ran in the foreground through
`source/run_process_round104.py`, which records the child PID, exact argv,
working directory, selected environment, UTC and Unix timestamps, user/system
time, peak RSS, timeout signals, return code, and reaping state. The three
solver intervals were disjoint:

| query | PID | start UTC | wall seconds | return | result |
|---|---:|---|---:|---:|---|
| iteration-187 quotient | 47626 | 2026-09-01 09:00:56 | 787.220342 | 10 | SAT |
| complete Xerr direct | 48003 | 2026-09-01 09:17:10 | 1192.822605 | 10 | SAT |
| complete Zerr direct | 48379 | 2026-09-01 09:37:13 | 163.354507 | 10 | SAT |

CaDiCaL 1.9.5 was invoked with proof output enabled from byte zero and
`--no-binary`. The outer limit was 21,600 seconds; each direct limit was 7,200
seconds. None timed out. Empty stderr files and full commands are retained.

## Iteration-187 quotient SAT

The complete assignment has SHA-256
`d75cb2a1aa9bab3f0fd7dd87f127273d0462861e21f565e497abe449e1e5092c`.
The independent assignment checker assigned every one of 2,452,334 variables
exactly once and evaluated all 11,789,630 clauses successfully.

The separate quotient/orbit checker then:

* re-evaluated all 11,789,630 clauses;
* linked 8,640 primary time bits to the decoded raw schedule;
* recomputed all 613,440 lex recurrence values and all 71 roots;
* enumerated the full 72-image schedule orbit;
* found 72 distinct images and stabilizer size one;
* proved the retained model is the lexicographically least image;
* rejected a constant-bit mutation, a truncated assignment, reversed lex
  direction, and omission of the sole root needed by the second orbit vector.

The candidate’s raw schedule SHA-256 is
`fd6c434105478de84ace78520b6b542e626e205f9722cdbafcd32437a2ea312e`.
After strictly increasing rank compression its SHA-256 is
`ef15e4e8dc53d6d14303238d3a32db6a5d73a4ba3cbd4c28a8f1576debc7dadd`.

## Frozen schedule replay

The frozen replay reconstructed all 864 required interaction edges. Times use
exactly layers 0 through 450. Resource conflicts and measurement-circuit
violations are empty. The schedule globally interleaves X and Z operations.

| invariant | value |
|---|---:|
| edges | 864 |
| used layers | 451 |
| minimum / maximum time | 0 / 450 |
| X/Z overlaps | 648 |
| overlap-interleaved pairs | 85 |
| whole-check interleaved pairs | 323 |
| reviewed-block hits | 0 |
| symbolic selector hits | 0 |
| named frozen selector hits | 0 |
| rank-compression order pairs checked | 5,616 |

The initial frozen replay failed only because the system Python lacked `z3`.
After binding the exact vendored runtime with `PYTHONPATH`, the corrected replay
passed. Both attempts are retained and classified in `FAILURE_LEDGER.md`.

## Complete direct adjudication

Each sector formula contains all 360 primary fault columns, a provably complete
`sum(select) <= 10` recurrence, 72 zero-syndrome parity equations, 12 logical
parity equations, and a nonzero-logical disjunction. There is no fixed basis,
pool restriction, residual-pattern restriction, check-count restriction, or
within-check order-family restriction.

| sector | variables | clauses | CNF SHA-256 | assignment SHA-256 |
|---|---:|---:|---|---|
| Xerr | 6,114 | 23,036 | `032757d174845b1311280f15a06bc6af09ee816fe359fefae650cae1174442ea` | `c28d4d2fbe29dac79057c1030b62bdb55975098b93f4f6f45a17133dfa402163` |
| Zerr | 6,084 | 22,916 | `fd430c2d8fad7fe7b9db5e1528e127dbe7e575440bba80d92bd93fa405b54d55` | `de2f4c3e1429317000bda3d7febfe52c123d7bf9e5e18ebd7ec8b81d879fb8f1` |

The new standard-library audit imported none of the frozen model modules. It
reconstructed the (12\times6) incidence geometry, all 720 columns, all
syndrome/logical rows, every physical hook suffix, stabilizer ranks 66/66,
normalizer ranks 78/78, and logical pairing rank 12. It also parsed and checked
all 45,952 direct clauses and both complete assignments.

### Xerr mechanism

The selected named faults are

```text
D:35 D:41 D:84 D:107 D:109 D:110 D:126 R:2:2 R:11:1 R:16:0
```

The canonical net support is

```text
3 7 20 35 41 80 84 85 94 95 107 109 110 126
```

and the physical net support is

```text
3 7 12 17 20 34 35 41 80 84 95 100 107 109 110 126
```

Both have empty syndrome, lie outside the X-stabilizer span, and have logical
parities

```text
0 1 0 0 1 1 0 1 1 1 0 0
```

The difference between canonical and physical support is a sum of check
stabilizers, explaining equality of the logical parity vector.

### Zerr mechanism

The selected named faults are

```text
D:5 D:7 D:29 D:45 D:46 D:55 D:69 D:121 R:3:0 R:10:0
```

The canonical net support is

```text
5 7 29 45 46 55 69 70 73 81 121 129
```

and the physical net support is

```text
0 4 5 29 45 46 55 63 74 80 121 136
```

Both have empty syndrome, lie outside the Z-stabilizer span, and have logical
parities

```text
0 0 1 1 1 0 0 1 1 0 0 1
```

Thus the outer candidate fails the distance-12 test in both sectors. No repair
was entered: the mandate permits repair only after independently checked UNSAT
in both complete sectors.

## SAT trace retention and proof controls

CaDiCaL’s proof-side outputs are meaningful only on UNSAT. Because all queries
were SAT, they are classified as trace streams and carry no certificate claim.
Each was deterministically gzip-compressed only after a full decompression
round trip matched raw SHA-256, byte count, line count, and empty-clause count.

| stream | raw bytes | raw SHA-256 | gzip bytes | gzip SHA-256 |
|---|---:|---|---:|---|
| outer | 3,992,309,439 | `c3482603435ca7eb860579473a0efca28ba340b9aa3589249a65db0f00661a11` | 575,477,336 | `7fc1c602d02a3f587265e4c69119983f9cdd81fb97d2f8ac613be334b6041450` |
| Xerr | 3,741,975,525 | `d4d923be34db28f07435f1a1356133dc9e224123b8cdf07c8ab6ed4b4e5defe5` | 1,067,315,248 | `e63d4336952911bc375ad00c1d477e9043e5dbfd04c6b64ad7c90e1d47d94f35` |
| Zerr | 812,987,852 | `bb7235adf460367dba1f10373eb140a5ce9c81b986cdb60adfabb9599368170d` | 245,939,748 | `379c9fae52785e19138dfb54d2f5da5a2117aeb298cbe0205d41cbfa1588f2a0` |

All three streams contain zero empty-clause records. Independently, the retained
proof-tool fixture showed that `drat-trim` accepted a valid DRAT and generated
LRAT, `lrat-check` accepted the generated LRAT, and both tools rejected corrupt
and truncated inputs. These controls establish tool behavior only.

## Sound full-orbit continuation

For each parent mechanism and each (delta\in\mathbb Z_{12}\times\mathbb
Z_6), Round104 translated the source schedule, data support, and local
check/kind names; replayed schedule legality; rebuilt the complete sector; and
rechecked weight, syndrome, and nonstabilizer status. The two parent orbits each
have size 72. No translated selector collided with the existing 24,012 or with
the other parent orbit.

The update is prefix-preserving:

\[
24{,}012+72+72=24{,}156.
\]

Blocks remain exactly 517,140. The independent checker tested all 1,034,280
block and 48,312 selector generator images. `GLOBAL_TRANSLATION_THEOREM.md`
gives the formal equivariance and quotient proof.

## Fresh iteration-188 frontier

The base source/state and both encodings passed independent reconstruction.
The state has `started: false`, `stop: null`, and no solver artifact exists in
the quotient directory.

| artifact | variables | clauses | SHA-256 |
|---|---:|---:|---|
| invariant base | 1,841,756 | 6,890,981 | `051dbece97d9cd94a69de7bff644dbb31b35076d0c43558b5408d9f3cc86b257` |
| lex quotient | 2,455,196 | 11,798,572 | `29b16602aa5cdf0e4207271cb50045454ea0aba9254396d732414459a4029215` |

Additional bindings are:

* source file SHA-256:
  `bb6605e47b541fccd8c33a4b8f3ae56e1ac298ab4be591fbc4c388dc102e0647`;
* source semantic SHA-256:
  `026c4cdde428436ec24768d4436b593547319e21b69981fdac6c5decb4527370`;
* state SHA-256:
  `ac4140e37f855fe37c1403c645e08d600d7ab70a6aee725f707b74a9721a30cd`;
* selector-state SHA-256:
  `90999b94525d7e4d23c7e62d4caf057a061baa461c56941057043b0ba3e22e99`.

The exact quotient checker reconstructed the 6,890,981-clause base prefix and
all 4,907,591 appended clauses. It proved unique definitional extension,
checked all 16 recurrence truth-table cases, and verified signed integer limits.

## Reproduction

`replay.sh` is the conventional entry point. With an explicit output path:

```sh
./replay.sh /tmp/circdist-round104-replay.json
```

Without an argument it writes a uniquely PID-named JSON record under `$TMPDIR`
or `/tmp`. The source-level entry is `source/replay_round104.py`. The replay
uses a sanitized environment, creates all generated comparison artifacts in a
temporary directory, launches children strictly serially, and records every
child PID, command, timing, status, stdout, stderr, and reaping state. The
retained pre-seal run passed 13 children in 253.437258 seconds.

## Repository and process validation

The repository suite passed live governance, problem and all-project DAG
checks, CIRCDIST migration, release contracts, DAG contracts, Lean DAG
self-test, the duplicate-key scan, and `git diff --check`. Evidence closure’s
raw return was 1, as required before review: all 344 unique diagnostics were
under this single uninstalled package.

The PID ledger covers 31 wrapper records, 13 replay children, 10 repository
validator children, and the nested proof controls. The three solver intervals
do not overlap. There were no wrapper timeouts or detached processes. The final
`ps` census found no live science process and no replay temporary directory.

## Smallest honest residual

Solve the exact fresh iteration-188 quotient proof-first. On SAT, repeat the
complete physical Xerr/Zerr adjudication and add only sound full 72-element
selector orbits. On UNSAT, retain and independently validate DRAT/LRAT and check
every theorem-chain link before claiming the universal distance-11 ceiling.
Neither UNKNOWN nor timeout can receive root credit.
