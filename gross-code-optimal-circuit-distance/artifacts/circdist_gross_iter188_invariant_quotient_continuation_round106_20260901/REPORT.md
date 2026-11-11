# Round106 Gross iteration-188 full-invariant quotient continuation

**Date:** 2026-09-01  
**Verdict:** `MATERIAL-CHECKED-CONTINUATION-NOT-CLOSED`  
**Canonical status:** unchanged: `CIRCDIST.gross = CONJECTURED`, `gap-via-lift = CONJECTURED`, and `D*_Gross in {11,12}`.

## 1. Exact dispatch and immutable bindings

This package starts only from the independently reviewed, fresh, unstarted iteration-188 full-invariant quotient. The live canonical files were treated as read-only. Their SHA-256 bindings are:

| Object | SHA-256 |
|---|---|
| `operations/circdist/SCHEDULER.yaml` | `89767aecd57e32608cc75010c26a5d415af3330964c42e572aefed86796c259b` |
| `circdist/proof-dag/nodes/CIRCDIST.gross.yaml` | `3fe41bc65891f94f65be55931c40f37cf3bbb3c5bdb7cca9cfa70a73489526ae` |
| Round105 exact review | `01d14be78fc75362c16340b4ba32df783a645084a819fc18a96f432d9a45e932` |
| reviewed Round104 root `SHA256SUMS.txt` | `410807a787005a0fb5ebb1753f8b75712c798d9a15e9101f1265d0be25206ebb` |

The package independently checked all 383 rows in the reviewed root manifest before solving. The reviewed frontier was exactly:

| Formula | Assertions | Variables | Clauses | SHA-256 |
|---|---:|---:|---:|---|
| iteration-188 invariant base | 545,694 | 1,841,756 | 6,890,981 | `051dbece97d9cd94a69de7bff644dbb31b35076d0c43558b5408d9f3cc86b257` |
| iteration-188 71-root quotient | 545,765 | 2,455,196 | 11,798,572 | `29b16602aa5cdf0e4207271cb50045454ea0aba9254396d732414459a4029215` |

The state had 517,140 invariant order blocks and 24,156 invariant selectors. Its group was `Z_12 x Z_6`, order 72, with 71 nonidentity lex leaders. `state.json` had `next_iteration = 188`, `started = false`, and `stop = null`. The quotient directory contained only `independent_check.json`, `metadata.json`, `outer.cnf`, `translation_roots.jsonl`, and `translation_trace.json.gz`. The base formula directory contained only `assertion_map.jsonl`, `definitions.json.gz`, `encoding_check.json`, `metadata.json`, and `outer.cnf`. A recursive filename census found no solver, model, assignment, proof, DRAT, or LRAT artifact in either bound frontier.

## 2. Independent reconstruction before solving

The standard-library input audit rehashed the canonical bindings, all reviewed-manifest rows, every copied frontier file, both DIMACS headers and every zero-terminated clause. A separate source-to-CNF checker reconstructed all 6,890,981 base clauses from:

- 1,833,076 acyclic, uniquely defined Boolean records;
- 545,694 source assertions and 549,510 root clauses;
- 11,234 ten-bit comparisons and all 1,048,576 comparison truth-pairs;
- 1,008 rank-membership domains and 4,354,560 local-order/qubit cases;
- all 517,140 block roots and all 24,156 selector roots.

Every variable was primary or uniquely defined, every clause ID was assigned once, and all source roots were reconstructed. Negative controls rejected a source mutation, a first-clause mutation, a truncated CNF, an out-of-bound time, and a reversed comparator.

The quotient checker then proved that its first 6,890,981 clauses were byte-for-byte the checked base and independently rebuilt the entire 4,907,591-clause suffix. It checked 613,440 unique recurrence variables, 71 roots, 4,478,976 group-composition edge cases, 51,840 direct-column equivariance cases, 10,368 stabilizer/detector row-permutation cases, 72 translated schedules, and 144 translated direct witnesses.

## 3. Quotient definition and finite theorem

Let `G = Z_12 x Z_6`. The action sends a check index `(i,j)` to `(i+a mod 12, j+b mod 6)` and acts on both 72-qubit halves in the same way. It therefore permutes all 864 schedule edges. Let `v(S)` be the 8,640-bit vector obtained from the ten-bit times of those edges in fixed order.

For every nonidentity `delta in G`, the quotient adds `v(S) <=lex v(delta.S)`. For a bit pair `(x,y)` and already-computed equal-prefix/suffix condition `z`, the recurrence is

`R(x,y,z) = ((not x) and y) or ((x == y) and z)`.

The checker exhausted all 16 assignments to `(x,y,z,R)` and reconstructed the eight CNF clauses for every recurrence step. The recurrence is functional, so every base assignment has a unique quotient-variable extension. Because every finite orbit has a lexicographically least vector, the quotient is equisatisfiable with the invariant base. Ties are harmless: group elements in the stabilizer produce the same schedule vector.

This theorem is used only at its checked scope. It would be invalid to globalize a selector registry not closed under all translations. Full generator closure is checked below before the theorem is reused for iteration 189.

## 4. Proof-first iteration-188 solve

Exactly one foreground CaDiCaL 1.9.5 process ran:

`cadical-1.9.5-arm64-macos -t 21600 --no-binary outer.cnf outer.drat`

It returned SAT, competition exit code 10, after 836.157983 seconds. Peak recorded `ru_maxrss` was 7,438,614,528 bytes. The process remained attached to the wrapper, did not time out, and was reaped before any next process started.

The complete assignment assigns all 2,455,196 variables exactly once and satisfies all 11,798,572 clauses. The retained assignment SHA-256 is `9a65121507b563eb42e47970a48e5cd9cd4902a1ffd260e975d7b2c68fed0bb0`; the solver log SHA-256 is `127e514439282f88678ece035484d301390fa71ab673a06edfe1878570b56c1f`.

Unique definitional replay reconstructed the base projection and the schedule. The compressed schedule SHA-256 is `e9daddcf1b38ecf505adeeb0da0a54ddff70ea0aac17c2c72ff81b54dda5f72a`. It has all 864 required edges, 511 used layers numbered 0 through 510, zero qubit/check conflicts, all 648 X/Z overlaps, zero MC violations, and global X/Z interleaving. No retained block or selector is violated.

SAT is positive evidence only. It does not prove the absence of a low-weight mechanism and does not prove either root branch.

## 5. Complete unrestricted direct-360 adjudication

For each CSS sector, the direct formula has one primary selection variable for each of 360 physical fault columns: 144 data singletons and 216 schedule-dependent residual hook columns. It contains the full weight-at-most-10 constraint, all 72 detector parity equations, and the complete logical-nontriviality condition. The builder and independent checker explicitly excluded every pool, residual-pattern, check-count, or within-check-order restriction.

The two formulas were solved strictly serially, each with proof output enabled from launch:

| Sector | Variables | Clauses | CNF SHA-256 | Solver result | Wall seconds |
|---|---:|---:|---|---|---:|
| Xerr | 6,115 | 23,040 | `62d7d207fc09c79b91425cc6612cfe3c825c4e8a8d06ecc6cf032080f47ce45b` | SAT / exit 10 | 625.627899 |
| Zerr | 6,111 | 23,024 | `f5c075d3ca0e49579e5380360404430d129ef2fc0cda1a4d5590c32eb4c289d1` | SAT / exit 10 | 137.818738 |

Every direct assignment variable and clause was checked. A nonimporting standard-library verifier independently rebuilt the `12 x 6` geometry, both rank-66 stabilizer spaces, twelve logical duals per sector, all 720 columns, both CNFs, the selected canonical sums, the physical hook suffixes, syndromes, logical parities, and stabilizer-membership tests. Flipping one selected primary variable makes clauses fail in each sector, providing assignment negative controls.

### Xerr mechanism

Selected faults:

`D:0, D:47, D:91, D:92, D:99, D:116, R:5:1, R:14:0, R:39:1, R:55:0`.

The canonical support is `{1,16,23,32,40,47,57,91,92,99,116,123,130,133}`. The physical support is `{15,23,40,47,56,89,91,98,99,116,123,139}`. Both syndromes are zero, both supports are outside the X-stabilizer row span, and their logical parity vector is `(0,0,1,0,1,1,0,0,0,0,0,0)`.

### Zerr mechanism

Selected faults:

`D:10, D:17, D:58, D:65, D:103, D:134, R:15:2, R:23:1, R:32:0, R:48:1`.

The canonical support is `{10,12,17,20,26,35,36,58,65,77,93,102,103,125,134,141}`. The physical support is `{10,12,17,36,58,65,77,86,93,125,134,141}`. Both syndromes are zero, both supports are outside the Z-stabilizer row span, and their logical parity vector is `(1,0,1,0,0,0,1,1,0,0,1,0)`.

Thus the candidate fails the distance-12 test independently in both sectors. Repair is forbidden because repair may be entered only after both complete sectors are independently certified UNSAT.

## 6. Sound full-orbit continuation

Each checked mechanism defines a selector whose antecedent is the conjunction of the within-check strict comparisons fixing exactly the residual columns used by that mechanism. On any schedule satisfying that antecedent, the same named distinct faults have weight 10, zero detector syndrome, and a nontrivial physical logical class. Negating the antecedent is therefore a sound exclusion of that schedule cell.

The continuation algorithm was:

```text
for delta in Z_12 x Z_6:
    translate all 864 schedule edges
    audit the complete translated legal schedule
    for sector in {Xerr, Zerr}:
        translate all ten selected fault names
        reconstruct the translated 360-column sector
        replay weight, syndrome, physical suffix, and logical class
        normalize the selector key and deduplicate by exact tuple
after insertion:
    check every block and selector under generators (1,0) and (0,1)
```

Both parent stabilizers are trivial at selector-key level: each orbit has size 72. The two orbits are disjoint from each other and from all 24,156 inherited selectors. Exactly 144 selectors were added, with zero tuple collisions and zero semantic-hash collisions. The result has 24,300 selectors.

The independent closure audit checked all 1,034,280 block/generator cases and all 48,600 selector/generator cases. Since `(1,0)` and `(0,1)` generate `G`, these checks prove closure under every translation. It also independently replayed all 72 translated schedules and all 144 translated physical mechanisms. No non-invariant registry was globalized.

## 7. Fresh iteration-189 frontier

The new source has SHA-256 `b3bdfbe8924490da1e20230ff856515d13173966bc4170c6078b7aab9e36558b` and semantic payload SHA-256 `e8b17eac5c55f1b1c32fb84972dcc2c52ce259c99a65200c8ed7bc046c811eb4`. Its state has SHA-256 `8bb97ba8ff7590f178aaff29f51da8ab6953b1fae90bcf6952546d31f59c6f97`; its selector-state SHA-256 is `8e4db1fbf08e24b81995a6ac1b25f791480edebd06e560442e2ca49a5ad5cefa`.

| Formula | Assertions | Variables | Clauses | SHA-256 |
|---|---:|---:|---:|---|
| iteration-189 invariant base | 545,838 | 1,847,301 | 6,909,336 | `f5ccbe6aa4c0a0df5940cd979809003182416900e76a6cc6e3755e493cc6b178` |
| iteration-189 71-root quotient | 545,909 | 2,460,741 | 11,816,927 | `3ece12a1ea0ee6502982fecfcaf75debae985ea2ddff93ea3b875552c0714df7` |

The source-to-base checker independently reconstructed all 6,909,336 clauses. The quotient checker proved the exact 6,909,336-clause prefix and regenerated all 4,907,591 quotient clauses. The state is `next_iteration = 189`, `started = false`, `stop = null`. Both exact frontier allowlists pass, and no solver/model/assignment/proof artifact appears in the frontier trees.

The smallest honest residual is: solve this exact iteration-189 quotient proof-first; if SAT, repeat full model, geometry, Xerr and Zerr adjudication and add only complete sound translation orbits; if UNSAT, retain and independently check the full DRAT/LRAT theorem chain.

## 8. SAT trace disposition and proof controls

All three CaDiCaL proof-side streams began at solver launch, but every solver returned SAT. They are traces, not DRAT/LRAT certificates. Deterministic streaming gzip preserved 7,045,413,283 raw bytes as 1,480,740,495 gzip bytes. An independent decompression scan reproduced every raw hash, byte count, line count, and found zero lines whose complete stripped content was `0`.

| Query | Raw bytes | Raw LF | Raw SHA-256 | Gzip SHA-256 |
|---|---:|---:|---|---|
| quotient | 3,966,058,553 | 47,028,532 | `75ed605aad0a3de44b03f384975a9aabf3f37365f6f38a0a69cd2dd013d83989` | `ffb63e8efceef58782c2ffe8b52f5b0efadb9912829ccb4aad917c449808b176` |
| Xerr | 2,397,205,129 | 16,425,108 | `7945b2bb52210a7f73b04842667aad90a6faa03e07a0ff8b976eb5e5582975d7` | `89f7c588bc3f6c5bf72657b2076f87723af4b5d08b5742ad46a2faa363e42475` |
| Zerr | 682,149,601 | 4,552,225 | `e7f537d13c366c10f41541546313f0bcc4e20c58bd0a13aff97d5a5f288c8198` | `d85147b6cea468f78e8e33463a3e50d99b798446ffb0a9cb0908d9e33e42a38b` |

Tool controls independently accepted a valid pigeonhole DRAT, converted it to LRAT, and accepted that LRAT. Corrupt DRAT, truncated DRAT, corrupt LRAT, and truncated LRAT each returned rejection. These controls establish tool behavior only; they supply no Gross UNSAT proof.

## 9. Process, replay, failures, and scope

All three solver intervals are disjoint and have return code 10. All solver/verifier/replay children are attached, recorded, and reaped. No solver timeout, wrapper timeout, OOM, UNKNOWN, detached job, portfolio, or repair run occurred. The root `replay.sh` invokes `source/replay_round106.py` and rechecks bindings, assignment, model, direct formulas, physical mechanisms, orbit construction, full registry closure, base/source bijection, quotient reconstruction, SAT traces, and proof controls in a clean environment. The preseal replay passed 13/13 serial children.

The complete incident record is in `FAILURE_LEDGER.md`. Two development-interface incidents had no scientific effect: an initial manifest filename probe used `SHA256SUMS` instead of `SHA256SUMS.txt`, and one combined shell preparation was rejected before launch because it contained `rm -rf`. Both were corrected with bounded operations and no protected or evidence-bearing file was lost.

No theorem in this package proves `D*_Gross = 11` or `D*_Gross = 12`. The SAT quotient and two low-weight mechanisms prove only that this candidate is not a distance-12 witness and justify the sound invariant continuation. The universal frozen-family ceiling remains unproved because the exact quotient is SAT, not UNSAT. The explicit construction branch remains unproved because the candidate fails both sectors. Therefore the exact root residual remains `{11,12}`.
