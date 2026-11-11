# CIRCDIST.gross Round109 fresh independent exact review of the sealed Round108 iteration-189 continuation

**Date:** 2026-09-02

**Reviewer role:** sole fresh independent Round109 reviewer

**Reviewed package:** `circdist/artifacts/circdist_gross_iter189_invariant_quotient_continuation_round108_20260901`

**Verdict:** **CLEAR-PROPOSER-LEVEL-CONTINUATION**

## 1. Verdict and licensed scope

The sealed Round108 claim is independently supported at proposer level. The reviewed iteration-189 full-invariant quotient is SAT, its complete assignment satisfies every one of 11,816,927 clauses, and its decoded 864-edge schedule is legal and globally interleaved. Both unrestricted direct-360 sectors are SAT and contain independently replayed named-weight-10 zero-syndrome nonstabilizer physical mechanisms. The schedule is therefore not a distance-12 witness, and the repair branch was correctly not entered. The two complete free translation orbits add 144 collision-free selectors and produce an exact, fresh, unstarted iteration-190 frontier.

This is continuation evidence only. Neither exact root branch is complete: there is no legal schedule certified at circuit distance 12, and there is no complete UNSAT proof establishing the universal circuit-distance-at-most-11 branch. `CIRCDIST.gross` and `gap-via-lift` therefore remain `CONJECTURED`, and the literal residual remains `D*_Gross in {11,12}`. I license no root promotion, route promotion, interval narrowing, repair entry, absence theorem, exhaustion theorem, or inheritance beyond the frozen model.

I did not communicate with or rely on the Round108 proposer. No hidden chain-of-thought was requested or used. The audit record instead exposes definitions, algorithms, exact counts, hashes, clause evaluation, counterchecks, process records, failure corrections, and limitations. Iteration 190 was rebuilt compile-only and was **not solved**. No canonical file, scheduler file, prior review, or sealed-package byte was modified. No commit or push was performed.

## 2. Live bindings and governance

Before scientific work I read the repository instructions and protocols, including `README.md`, `CONTRIBUTING.md`, `DAG_PROTOCOL.md`, `FILE_PROTOCOL.md`, the Circdist project instructions, the live scheduler, the live canonical node, and the Round107 predecessor review.

| binding | independently observed SHA-256 | bytes | LF | result |
|---|---:|---:|---:|---|
| `operations/circdist/SCHEDULER.yaml` | `9b7e12cbf03053ce9cee4a713cadb6e96908a301f1e4d80119900e94eb0bcfdd` | 304,776 | 3,561 | exact live dispatch binding |
| `circdist/proof-dag/nodes/CIRCDIST.gross.yaml` | `8b805a806d5b704047f4ccca648c92efe11740d7c5b7825659eb1e6b7b5dc977` | 114,191 | 1,215 | exact live canonical binding |
| Round107 predecessor review | `eda1d894cde8a56fd7eac9188ed2bb73bef4ddd7842e2fcb091435cbd759c036` | 149,822 | 1,625 | exact dispatch binding |

The scheduler was at budget 134/135, Round109 exact review pending, with winner `CIRCDIST.gross@round108-exact-review` at score 0.95. The canonical root and `gap-via-lift` were both `CONJECTURED`; the exact residual was `{11,12}`. The package's `PROPOSED_CIRCDIST.gross.yaml` was deliberately byte-identical to the live canonical and proposed no installation. The append-only replacement at the end of this review is a reviewer-licensed evidence/frontier update, not a proposer-installed mutation.

Key sealed package identities also rehashed exactly: `REPORT.md` `d40c860e646b9654deded871d079d6c67ced35d619c767578dd1639c2d1f5576`; `RESULT.json` `6005740e39fbd83f15d5a65837e5d39d2fb75dd230bd0e1c0557d2764a6d0b17`; `PROCESS_FIX2_LEDGER.json` `cc3ab1a6c8532a0e3c9b6baa073a3c8c877b248231555da9ab0da7ef6e019c70`; `FAILURE_LEDGER.md` `ca240094a9e67ba477fecb88d7956957dcac429489149e3ee63be190a2aaea69`; `FRESH_FRONTIER.json` `69f719dbb27bd3fce72dc765be79ac1980e898cfa974c406d4e54eb590652ff5`; and `INPUT_BINDINGS.json` `919408be92d9f6cb4cadda6edb38d372445ce2d123e464bc221bb9162ad855ff`.

## 3. Seal, manifests, membership, and post-seal mutation attack

I traversed the package without following links and found exactly 444 regular files, 42 directories, zero symlinks, and zero other filesystem objects. The file modes were 293 at `0444` and 151 executable files at `0555`; all 42 directories were `0555`. No file or directory had any write bit. My first mode harness incorrectly demanded `0444` even for executable files; that reviewer error is disclosed in Section 14. The corrected predicate is “read-only, with execute bits permitted where sealed,” and it passes.

Every manifest row was parsed as a unique safe relative path. For every row I independently streamed the named file and recomputed SHA-256, byte count, and LF count; order, uniqueness, membership, and exact row counts all match:

| sealed index | SHA-256 | bytes | LF / rows | exact membership |
|---|---:|---:|---:|---|
| `SHA256SUMS.txt` | `6c7f94706744ec7e11dcae7616d56ac3cc816025c72c25d4dc7396f981666cc0` | 49,350 | 443 | all 444 physical files except the root manifest itself |
| `PAYLOAD_SHA256SUMS.txt` | `f8a998b19317a2a9d1ff77a8cf8e7d6cb9bf55c6f15962036dce88919a60e5e5` | 48,717 | 436 | exact payload membership |
| `FILE_INVENTORY.jsonl` | `e4b09cb611b0cdceb3296da881280fd3e9f2af76078d0178aaade14ae9b59004` | 69,304 | 442 | all physical files except itself and the root manifest |

The eight deliberate payload exclusions are `ENVIRONMENT.json`, `FILE_INVENTORY.jsonl`, `PAYLOAD_SHA256SUMS.txt`, `PROCESS_FIX2_LEDGER.json`, `RESULT.json`, `SHA256SUMS.txt`, `verification/final_process_census.json`, and `verification/postseal_replay.json`. Removing the root-manifest self-reference, each of the other seven is covered by the final root manifest. Thus the payload exclusions do not create a final-root coverage gap.

Before the fresh replay I recorded content and metadata for all 486 entries. After replay I repeated the full scan. There were zero missing or extra entries, zero new symlinks, and zero changes in file SHA-256, bytes, LF, device, inode, mode, uid, gid, `mtime_ns`, `ctime_ns`, link count, or flags. This attacks post-root-seal substitution more strongly than a manifest-only comparison: a replacement with identical content but a different inode or metadata would also have appeared. The stored process ledgers, zero-write modes, external replay records, root coverage, and this 486-entry before/after comparison agree. I found no post-root-seal mutation.

The independent post-seal dispatcher record remains `/private/tmp/circdist-round108-dispatcher-postseal-replay-final-20260902.json`, SHA-256 `cf9894aaa651a44975b33310947f469f9be2c993967803355407314982a5d806`, 37,771 bytes / 642 LF. The scheduler-gate record remains `/private/tmp/circdist-round109-scheduler-gates-20260902/summary.json`, SHA-256 `2346c46a8d7d827c799bdbba074eea22aaddf5c747abf84b4c3a01fca3629714`. Both external identities match dispatch.

## 4. Fresh sealed-root replay

I executed the sealed root `replay.sh` in a clean environment with all output outside the package. Wrapper PID 11700 launched replay PID 11702. It returned 0 in 348.484326 seconds with empty stderr and no timeout. The retained fresh record is `/private/tmp/circdist-round109-fresh-sealed-replay-20260902.json`, SHA-256 `48f1364752dbb2b3248b145421cfc1ae59dece7be1d88562037cb59de0d08f2b`, 37,803 bytes / 642 LF.

The 18 direct replay children, in exact order, were PIDs 11706, 11707, 11731, 11738, 11743, 11744, 11750, 11754, 11757, 11758, 11759, 11760, 11761, 11770, 11780, 11793, 11816, and 11823. They covered bindings, the iteration-189 base, registry, quotient, complete assignment, schedule, orbit controls, direct rebuild, Xerr and Zerr assignments, physical replay, an independent direct audit, iteration-190 orbit construction, registry, base and quotient, SAT traces, and proof controls. Every child returned 0, emitted a PASS JSON, had empty stderr, was reaped, and recorded `timed_out=false`, `term_sent=false`, `kill_sent=false`, and `detached=false`. All 17 adjacent gaps were positive; the minimum was 0.00024890899658203125 seconds. There were zero overlaps and no surviving child PID. Both manifests verified within replay.

This fresh replay is corroboration, not the scientific conclusion. Sections 5–11 describe the non-importing standard-library reconstruction.

## 5. Frozen geometry and exact group action

The independent auditor imported no sealed checker module. Its script SHA-256 is `845118f3cce15f2ceaf19b1dfe5de5536c765ec1a16dbf64a956f5edbc1ec8b9`. It represented supports as Python integers, computed GF(2) parity by popcount, used explicit Gaussian elimination for row rank and span membership, parsed JSON/gzip directly, and parsed DIMACS itself.

Let `L=12`, `M=6`, `G=72`, and `N=144`. A check coordinate `g` is decoded by `divmod(g,6)`. For delta `(a,b)`, the action is `add(g,delta)=((i+a) mod 12)*6+((j+b) mod 6)`. On data qubits it is `tq(q,delta)=add(q,delta)` for `q<72` and `72+add(q-72,delta)` otherwise. On an edge `kind:check:qubit`, both check and qubit are translated. Group addition is coordinatewise modulo `(12,6)`.

With `A=((3,0),(0,1),(0,2))` and `B=((0,3),(1,0),(2,0))`, the independent reconstruction used

- `X_g = { add(g,a): a in A } union { 72+add(g,b): b in B }`;
- `Z_g = { add(g,-b): b in B } union { 72+add(g,-a): a in A }`.

These reproduce all 72 X checks, 72 Z checks, 144 data-incidence lists, 864 distinct required CNOT edges, and 648 size-two X/Z overlaps byte-semantically. Both check matrices have rank 66 and commute pairwise. The exact action audit checked 72 edge permutations and the identity, then all `72*72*864 = 4,478,976` edge-composition cases. It also checked `72*(2*72+144) = 20,736` check/incidence cases, `72*648 = 46,656` overlap cases, and `72*144 = 10,368` row-permutation cases. No mismatch occurred.

## 6. Iteration-189 source, registry, base, quotient, and equisatisfiability

The reviewed input is genuinely fresh before launch: iteration 189, `started=false`, `stop=null`, 517,140 blocks, and 24,300 selectors. The source gzip SHA-256 is `b3bdfbe8924490da1e20230ff856515d13173966bc4170c6078b7aab9e36558b`; its canonical semantic payload SHA-256 is `e8b17eac5c55f1b1c32fb84972dcc2c52ce259c99a65200c8ed7bc046c811eb4`. The state file SHA-256 is `8bb97ba8ff7590f178aaff29f51da8ab6953b1fae90bcf6952546d31f59c6f97`; selector-state SHA-256 is `8e4db1fbf08e24b81995a6ac1b25f791480edebd06e560442e2ca49a5ad5cefa`.

For each selector I reconstructed the tuple `(sector, sorted data support, sorted (check, residual-kinds))`, rebuilt its selected names and semantic digest, enforced fault count at most 10 and uniqueness, and checked closure under generators `(1,0)` and `(0,1)`: 48,600 input-registry generator cases. For each block I canonicalized its atom pairs, checked unique semantic digest and source id, evaluated its cut directly on the candidate schedule, and checked both generator images. All 517,140 cuts reject the candidate relation as intended; all 1,034,280 block-generator cases pass. The candidate satisfies zero prior selector mechanisms, so it is not stale-blocked.

The base CNF has 1,847,301 variables, 6,909,336 clauses, and 545,838 assertions, SHA-256 `f5ccbe6aa4c0a0df5940cd979809003182416900e76a6cc6e3755e493cc6b178`. I compared its entire clause stream with the prefix of the quotient CNF: all 6,909,336 lines are byte-identical.

The quotient orders 864 edges and ten time bits per edge, hence 8,640 comparison bits. For each of the 71 nonidentity deltas it defines the suffix-lex recurrence `r=(not x and y) or ((x==y) and suffix)`. I exhaustively checked its 16 Boolean input/output cases. Each bit has exactly eight defining clauses; each root has 8,640 new variables and `8*8,640+1 = 69,121` clauses, including its unit root. Therefore the extension adds exactly `71*8,640 = 613,440` variables and `71*69,121 = 4,907,591` clauses. The total is 2,460,741 variables and 11,816,927 clauses, SHA-256 `3ece12a1ea0ee6502982fecfcaf75debae985ea2ddff93ea3b875552c0714df7`.

The 72 translated candidate vectors are distinct, and the identity vector is strictly smaller than each of the 71 nonidentity translates. More generally, because the full installed registry is invariant under the finite group, every base-model orbit contains a lexicographically minimal representative; that representative satisfies all quotient roots. Conversely every quotient model satisfies the unchanged base prefix. This proves base/quotient equisatisfiability for this full invariant base, and only for this bound base.

I parsed the retained complete assignment, required exactly one value for every variable 1 through 2,460,741, and evaluated every literal in every clause. The retained assignment file is SHA-256 `c992d5938b3b2531bd559ca085e723061f43479ece3510f94eef27a14768a498`; every one of 11,816,927 clauses is satisfied. The different `1c30…` value appearing in an alternative serialization binding is not the retained file hash; my initial confusion is a disclosed reviewer-harness error, while the semantic all-variable/all-clause result is unchanged.

## 7. Schedule legality and frozen controls

The candidate schedule semantic SHA-256 is `0c1fc8bfede56c24fd3e5b10bbcb03b215aefc271dd3471d2c34cfdd7626fcba`. Its map contains exactly the 864 frozen edges, integer times, and the contiguous layer set 0 through 447: 448 layers. For each layer I keyed both the ancilla node `(sector,check)` and data node `(D,q)` and found no duplicate occupation. For every one of the 648 size-two X/Z overlaps, the two shared-qubit orientations agree, which is the frozen MC condition. The exact counts are 125 pair-interleaved overlaps, 409 whole-check-interleaved overlaps, and global X/Z interleaving true. No conflict, MC violation, or frozen-cut violation was found.

The lex controls above establish 71 strict roots and 72 unique orbit vectors. The recurrence was checked independently from its truth function and exact clause sequence, not inferred from stored metadata.

## 8. Independent unrestricted direct-360 reconstruction

For each sector I regenerated 144 data columns and 216 residual columns. Data-column detector options are the reverse-time suffixes of incident detector checks. Residual positions are `{0,1}`, `{3,4,5}`, and `{4,5}`; their physical positions are `{2,3,4,5}`, `{3,4,5}`, and `{4,5}`. I rebuilt detector equations, logical equations, stabilizer rows, CNF clauses, clause ledgers, and the complete assignments from the frozen source and schedule. Canonical and physical supports were reduced by XOR. I recomputed zero detector syndrome, all 12 logical pairings, and GF(2) stabilizer-row membership for both canonical and physical supports.

| sector | variables | clauses | direct CNF SHA-256 | assignment SHA-256 | selected named faults |
|---|---:|---:|---:|---:|---|
| Xerr | 6,102 | 22,988 | `3a103f690d095b80f18a0499ba022d3dc2c8311c49629c431709a2746707bfbf` | `52601f873e94d5532690713cf84505059a9cb5dbd9444098107ccbd453ad6dc1` | `D:48,D:60,D:63,D:66,D:89,D:105,D:138,D:143,R:4:2,R:55:0` |
| Zerr | 6,100 | 22,980 | `576c1646bdb37eb8c14ca5029e29d763bfd8aac019fd20b351684e116a261b0f` | `f5b1b6479bf0fbbda7142f3b7577a8b2fa28b77129de9c0a1c220fbd80bf409e` | `D:48,D:90,D:93,D:96,D:105,D:131,R:4:1,R:5:0,R:7:1,R:14:0` |

Xerr selected indices are `[48,60,63,66,89,105,138,143,158,309]`. Its canonical support is `[0,48,57,60,63,66,88,89,105,138,139,143]`; physical support is `[0,1,48,56,60,63,66,88,89,105,130,133,138,143]`; logical parities are `[1,0,0,1,1,1,0,0,0,0,1,0]`.

Zerr selected indices are `[48,90,93,96,105,131,157,159,166,186]`. Its canonical support is `[48,64,65,67,78,84,90,93,96,105,130,131,133,140]`; physical support is `[8,17,48,64,67,71,75,76,78,85,90,93,96,105,130,133]`; logical parities are `[1,0,0,1,0,1,0,0,1,0,1,0]`.

Both canonical and physical supports have zero syndrome, identical nonzero logical action, and are outside the appropriate stabilizer span. Thus both SAT assignments select real nonstabilizer mechanisms in the frozen physical semantics. They kill this candidate and prohibit repair. They do not prove a universal bound.

## 9. Atomic selector orbits and iteration-190 reconstruction

For each parent mechanism and every delta in `Z_12 x Z_6`, I translated names, schedule, canonical support, physical support, checks, and selector identity. I reran all 72 translated schedules and all 144 translated physical mechanisms. Each parent orbit has size 72, the two orbits are disjoint, and neither intersects the 24,300-selector prefix. The exact lineage is 24,300 to 24,444 selectors with zero collisions. The suffix uses the authoritative delta-major, sector-interleaved record order.

The post-extension countercheck at `/private/tmp/circdist-round109-iter190-registry-countercheck-20260902.json`, SHA-256 `ce1194c0df949077bcd8ffe0a709c6c054449569edb66f068391a07fd116d48c`, 428 bytes / 17 LF, directly checks exact prefix-object equality, the two 72-element suffix orbits, and both generator images of all 24,444 selectors: exactly **48,888 selector-generator cases**. The iteration-190 blocks are object-equal to iteration 189, so the independently established 1,034,280 block-generator cases transport exactly. This also confirms the required 517,140 blocks, 1,034,280 block cases, 48,888 selector cases, 72 schedule replays, and 144 physical mechanisms in one lineage.

I reconstructed the source JSON, extended only the licensed fields and selector suffix, canonicalized its semantic payload, serialized sorted indented JSON with one LF, and compressed with deterministic gzip level 9 and `mtime=0`. It is byte-identical to the sealed iteration-190 source. I independently serialized the state and obtained byte identity. Exact identities are:

| artifact | SHA-256 | state/count |
|---|---:|---|
| source gzip | `5231e7f5b4cd2a74390a5d137b9927276ce73829dc599ddc064ab8f2c94a2d2e` | byte-identical |
| semantic source payload | `76881a021258e6fda565ecfe0ad61c1fe0e6f6a97a418ea806c6d3193b692c00` | byte-identical semantics |
| state JSON | `af31130cbb6f0f80d2b37b3ba27d1b1d86fa5b18a80c1e02aa3de02504863be4` | `next_iteration=190`, `started=false`, `stop=null` |
| selector state | `02b71bfed57c070359b77d69514397a021734aec7563057c02eeff29f4b6cdbd` | 24,444 selectors |
| base CNF | `e3ec0d0b146fc4ade428052d1a14737ffade9974dfc37dd79fa8411841d45fc8` | 1,850,757 variables; 6,920,296 clauses; 545,982 assertions |
| quotient CNF | `12f2fe58f4bfcaff19d543cdb60411f1659e86c8b4f16f599a2d1679aeeca767` | 2,464,197 variables; 11,827,887 clauses; 546,053 assertions |

I then ran the deterministic builders compile-only against my independently rebuilt source. Six deterministic outputs are byte-identical: base `outer.cnf` 185,961,625 bytes / 6,920,297 LF; `assertion_map.jsonl` 188,586,041 bytes / 545,982 LF; `definitions.json.gz` 33,219,810 bytes; quotient `outer.cnf` 331,930,384 bytes / 11,827,888 LF; roots 35,582 bytes / 71 LF; and trace 6,825 bytes / 26 LF. Only the explicitly nondeterministic `compile_seconds` metadata field differs.

The exact 13-file frontier allowlist is source, state, orbit audit; five base-formula files (`assertion_map.jsonl`, `definitions.json.gz`, `encoding_check.json`, `metadata.json`, `outer.cnf`); and five quotient files (`independent_check.json`, `metadata.json`, `outer.cnf`, `translation_roots.jsonl`, `translation_trace.json.gz`). There is no solver log, model, assignment, DRAT, LRAT, or other solver artifact. I did not solve iteration 190.

## 10. SAT trace roundtrips and proof controls

I independently decompressed, hashed, counted, deterministically recompressed, and compared each complete SAT search stream byte for byte. The implementation used 8 MiB chunks, gzip level 9, empty filename, and `mtime=0`; it never materialized a raw file. Each rebuilt gzip was deleted before moving to the next stream.

| stream | raw SHA-256 | raw bytes | raw LF | gzip SHA-256 | gzip bytes | empty-clause lines |
|---|---:|---:|---:|---:|---:|---:|
| quotient | `04dad78f1631bf5526e2a36ad0d1cf1411e4d3ba49a9d0082d8384bcffb5c5ef` | 3,023,479,844 | 37,347,718 | `4ecf47c758af926eea99d17d423c81764b950568f9dd9162094c132fc5b31441` | 402,994,314 | 0 |
| Xerr | `1b3cead6431f9fb5d044351b6a4ed4ec4d92a9df3266f3afc9bdfe072e519e95` | 1,542,579,103 | 10,784,906 | `2cc84b350eaa8bcce4225a7867438a6c2e81587c2488f2cd079f90947249a61c` | 460,322,411 | 0 |
| Zerr | `bc0b5564e7d9ed7e1bd609c60f629f1e0196662ebcb4ce4299baf3558b0cdc3a` | 828,784,097 | 5,997,071 | `92c1e35b5262f9ca686c66748705e43770f3ddd3b1a9a9d1b5fdb00f7d9eadf4` | 250,369,001 | 0 |

Totals are 5,394,843,044 raw bytes, 54,129,695 LF, and 1,113,685,726 gzip bytes. All regenerated gzip files were byte-identical and removed; all three raw package paths remain absent. These are SAT search traces, not DRAT/LRAT UNSAT certificates, and carry zero Gross UNSAT credit.

Fresh proof-control parent PID 12586 launched PIDs 12587–12592 strictly serially. Valid DRAT generated LRAT and was accepted; the generated LRAT was accepted; corrupt DRAT, truncated DRAT, corrupt LRAT, and truncated LRAT were rejected with expected return codes `[0,0,1,1,1,1]`. All six were reaped with no timeout, TERM, KILL, detachment, or survivor; the minimum adjacent gap was 0.00006198883056640625 seconds, and the temporary generated LRAT was removed. Fixture CNF SHA-256 is `b8d28f511bbc3bc5d67e0fcda748b6ad85d5e543c64bc91d09f34ecb10805efd`, valid DRAT is `b6c2e560bb08c84d583ca94799951a21c8cae5de35d6d04d77bc4842e9c18ecd`, and generated LRAT is `cf32dfff36b24ba36c3504765f29ecf3d7a8abaa59956ade4d24a4062caa6431`. Stored parent 9190 and nested PIDs 9191–9196 independently reconcile to the same behavior. These are checker-fixture controls only; no Gross UNSAT occurred.

## 11. Package process ledger, failures, and cleanup

I reconciled every one of the 37 retained top-level package process JSONs against `PROCESS_FIX2_LEDGER.json`. All child PIDs are unique. Return-code distribution is 33 at 0, one disclosed execution failure at 1, and three SAT solver exits at 10. Every record is attached, reaped, not timed out, and has no TERM/KILL. The top-level intervals are strictly nonoverlapping with minimum gap 4.795646905899048 seconds.

The three solver intervals are PID 6378 for 484.950212 seconds, PID 6568 for 393.323492 seconds, and PID 6712 for 261.00184 seconds. Each launched proof output from the start, returned SAT exit 10, and contains `SATISFIABLE` with no `UNKNOWN`. Their adjacent gaps are 118.20069098472595 and 13.795459032058716 seconds. There are no solver overlaps.

Adversarial disposition of the four package failures:

- **F108-001:** historical exec-transport visibility gaps cannot be recreated. The retained child intervals, later completion outputs, strict nonoverlap, reaping fields, and pre-payload/final censuses agree; no overlapping replacement computation appears.
- **F108-002:** unlaunched draft history is not externally observable. I independently verified the executed source semantics and correct iteration-189 input/iteration-190 output labels. No draft artifact is in the sealed inventory.
- **F108-003:** PID 7336 returned 1, attached and reaped, because vendored Z3 was absent from `PYTHONPATH`. The traceback fails at the line-161 import; the first output-directory creation is line 255, so the failure precedes frontier output. Corrected retry PID 7356 set the bound Python path and returned 0 strictly later. My independent byte-identical rebuild confirms no failed output was used.
- **F108-004:** initial proof-control parent PID 8220 lacked nested PID/reap fields. Fixed parent PID 9190 records PIDs 9191–9196 with complete intervals and outcomes. The fresh Round109 control run independently reproduces all six outcomes.

The pre-payload and final package censuses both report zero matching live science processes, zero detached processes, zero replay temporaries, and reaped `ps` children. Cleanup verifies three raw SAT streams removed after gzip roundtrip, no forbidden fresh-frontier artifacts, and no Python caches. The conventional root replay interface exists and passed. I found no undisclosed scientific failure, stale binding, schema/iteration mislabel, manifest gap, mutable package artifact, solver `UNKNOWN`, timeout, detached process, or post-seal write.

## 12. Reviewer process discipline and correction ledger

Through the last pre-draft inspection, the one-shot audit log contains 77 completed foreground command children and 77 wrapper starts; the separately PID-bearing nested sets comprise 18 fresh-replay children, six fresh proof-control children, and 11 overlay-gate children. The initial persistent runner PID 11505 is separately recorded as an infrastructure failure. Later durable installation, extraction, census, and cleanup are bound by the final external audit record reported with this review. All scientific/checker work ran serially; no review command timed out or detached.

The following are reviewer-harness defects, not package defects. Every failed scientific-harness retry left the package untouched, and the final necessary semantic gate was retained and passed.

| id | PID | stage | exact cause | correction |
|---|---:|---|---|---|
| H109-001 | 11505 | persistent runner startup | PTY/IPC request echoed but no command child was ever spawned | SIGINT, reaped exit 1; replaced by one-shot foreground run_one wrapper |
| H109-002 | 11653 | seal mode audit | reviewer incorrectly required mode 0444 for executable package files | accepted read-only 0444 and executable read-only 0555; full corrected audit passed |
| H109-003 | 12147 | independent scientific harness | system Python lacks int.bit_count | portable bin(x).count implementation |
| H109-004 | 12161 | independent scientific harness | reviewer confused alternative complete assignment serialization hash 1c30... with retained assignment file | bound retained c992d593... and retained every all-variable/every-clause semantic check |
| H109-005 | 12179 | independent scientific harness | reviewer DIMACS parser assumed header preceded comment lines | skip comments, then require exact header |
| H109-006 | 12204 | independent scientific harness | translated selector mechanism names were compared before canonical sorting | canonical sort after action |
| H109-007 | 12223 | independent scientific harness | reviewer generated iter190 suffix as all X then all Z | authoritative delta-major sector-interleaved order |
| H109-008 | 12285 | independent scientific harness | reviewer allowlist omitted orbit_audit.json, encoding_check.json and independent_check.json | exact 13-file authoritative allowlist |
| H109-009 | 12409 | iter190 byte comparison | reviewer named quotient nondeterministic timing field build_seconds | authoritative compile_seconds; all six deterministic artifacts were already byte-identical |
| H109-010 | 12656 | process audit harness | reviewer assumed solver record carried expected_returncode | retained observed rc10/SAT/proof-launch/UNKNOWN checks |
| H109-011 | 12661 | process audit harness | reviewer guessed wrong literal for frontier output-directory creation | verified actual line-255 mkdir follows failing line-161 import |
| H109-012 | 12670 | process audit harness | reviewer counted every F108 identifier mention rather than ledger headings | required each F108-001--F108-004 heading exactly once |
| H109-013 | 12719 | canonical introspection | reviewer queried nonexistent top-level evidence instead of assessment.basis.evidence | used authoritative nested schema |
| H109-014 | 12788 | overlay build | clean environment stripped PyYAML import path | reran deterministic builder in verified inherited Python environment |
| H109-015 | unexposed | 19a wrapper invocation | reviewer passed plain argv where run_one requires one base64 JSON argument; wrapper failed before logging or spawning a command child | all subsequent calls used encoded request |
| H109-016 | unexposed | run_one source inspection | one read-only /bin/cat was invoked directly before wrapper interface was known; exec supervisor did not expose its PID | all subsequent OS commands used the logged one-shot wrapper |

The malformed 19a wrapper invocation failed before spawning a command child. One direct read-only `/bin/cat` of `run_one.py` occurred before its base64 interface was known; the exec supervisor did not expose that inspection PID. Both are disclosed rather than presented as scientific evidence. JavaScript-side base64 helper errors spawned no OS process.

## 13. Independent audit records

The frozen core record is `/private/tmp/circdist-round109-exact-review-core-audit-20260902.json`, SHA-256 `29d6653b8d5f09b4ea803fc1cfd669d3e18e3d35aab85b68dd27c162f98c775a`, 518,404 bytes / 6,553 LF. It embeds the completed process snapshot, commands, PIDs, timing, outputs, failures, and selected audit-record hashes. The fresh replay and iteration-190 registry countercheck are retained separately as identified above.

| scratch audit record frozen into the core | SHA-256 | bytes | LF |
|---|---:|---:|---:|
| `04b_corrected_seal_mode_audit.json` | `3bf0c7b81fe8add3dbb940998b9a7a572a67a71841c218dd04049e78d73a2d54` | 6,961 | 175 |
| `09_replay_structural_independent_audit.json` | `198826ecb9c140198eec0b9242a8865d7e60f1e4ebef1ae64b72e05431317c6f` | 8,145 | 195 |
| `10_post_replay_immutability_audit.json` | `044cfffff7cb662539a6c23e4f0d84f218c79eeef3ce61b0fa110bac42832891` | 194 | 10 |
| `17_independent_stdlib_scientific_audit.json` | `da2928b6aab11e963b5200d9a2693a8eebdb2720d5522cdb4da756767b961e3a` | 5,797 | 253 |
| `18f_corrected_byte_rebuild_comparison.json` | `bddf83e43fb04079d277bbaef0c4491ec51567461c284d9d80ba744f6ac08484` | 2,073 | 69 |
| `19_independent_trace_roundtrip.json` | `1d087ba37943bfa5d97c44ae004c57a88f016941c8ae0dd2f3f728e3b970a445` | 2,996 | 72 |
| `20_nested_proof_audit.json` | `a6ed5f27db07db9a7ad4bb136002db64cfd526d5deee9e4d9cebf5468b048083` | 1,791 | 86 |
| `21_independent_process_failure_audit.json` | `232b480a7c56d6700341ea5d6f2622f12ce6c39a9d6c7e1035791649cff2e51a` | 5,481 | 179 |
| `22_overlay_gates.json` | `eebcf7f4f4f8a365f370588902c348e248f77d8fbb57aef2608518f9b8a4bbf7` | 15,894 | 453 |

Scratch scripts and generated artifacts are disposable. Only the explicitly cited external audit records are retained after cleanup.

## 14. Disposable overlay gates

The candidate YAML was installed only into a disposable hardlink overlay after unlinking the canonical target hardlink. `.git` was excluded. The live canonical was never opened for writing. A unique-key loader and explicit reversal proof establish that the only loaded changes are: appended root assessment text; two appended root evidence items; appended `gap-via-lift` assessment text; replacement of `frontier.dstar-residual.task`; and one appended event. Resetting those five licensed edits gives exact loaded equality with the live canonical. Root evidence moves 78 to 80; events move 24 to 25. Both old prefixes are exact.

All 11 gate children PIDs 13016–13026 ran strictly serially under PID 13015, with minimum adjacent gap 0.00025177001953125 seconds. All were reaped; no timeout, TERM, KILL, detachment, or survivor occurred.

| gate | exact result |
|---|---|
| previous-state structural preservation | PASS; all unlicensed loaded structure equal; both `CONJECTURED`; residual `[11,12]` |
| proof DAG, Circdist | rc 0; 16 node files structurally valid |
| proof DAG, all | rc 0; 500 node files across ten projects structurally valid |
| Circdist migration | rc 0; 16 nodes, 143 original events, 728 byte-identical copies |
| release contracts | rc 0; 14/14 tests |
| DAG contracts | rc 0; 24/24 tests |
| Lean DAG selftest | rc 0; 23/23 assertions; internal failing fixtures behaved as expected |
| evidence closure | rc 0; 176 structured paths, all project-local and linked |
| duplicate-YAML scan | rc 0; 985 files, 29,469 mappings, zero duplicates |
| live `git diff --check` | rc 0; empty stdout/stderr before the sole review write |
| candidate no-index whitespace | expected rc 1 for content difference; empty stdout/stderr, hence no whitespace diagnostic |

The exact replacement YAML is SHA-256 `7302da9e4726bd2c62a9e335d75d6a9098780888ed91a87a66d503b5938f607b`, 121,740 bytes / 1,278 LF. Final review extraction will require exactly one marker pair, exactly one YAML fence, unique mapping keys, and byte identity with this candidate.

## 15. Limitations and branch discipline

This audit proves the exact claims above inside the frozen `S_Gross` geometry, conflict/MC semantics, translation-closed registry, CNF encodings, and unrestricted direct-360 semantics. It does not globalize a SAT mechanism into a universal theorem. Historical transport visibility and unlaunched draft history are bounded by the limitations stated under F108-001 and F108-002. The Lean selftest validates its checker contract, not the Gross mathematics. SAT trace bytes validate retention and reproducibility, not UNSAT. No iteration-190 solver was launched.

Accordingly, root branch A remains incomplete because the reviewed schedule is killed in both sectors. Root branch B remains incomplete because all three actual Gross searches are SAT and there is no Gross DRAT/LRAT. The exact residual remains to solve the fresh iteration-190 quotient proof-first, retaining a complete proof or model and repeating bilateral unrestricted direct adjudication if SAT.

## 16. Complete replacement `CIRCDIST.gross.yaml`

The bytes between the unique fence delimiters are the complete intended replacement. They append only the reviewed Round108 run/review evidence, the corresponding assessment text, the fresh iteration-190 frontier task, and the Round109 review event.

<!-- BEGIN COMPLETE CIRCDIST.gross.yaml REPLACEMENT -->
```yaml
id: CIRCDIST.gross
role: outcome
aliases:
- GROSS-DSTAR
claim: For the Gross code [[144,12,12]] with single-ancilla CNOT syndrome extraction (interleaving of X- and Z-check CNOTs
  allowed; each required CNOT exactly once; one two-qubit gate per qubit per time step; no flag ancillas, cat states, or generating-set
  changes; idle layers compressed), the optimum D*_Gross = max over legal schedules M of d_circ(C(M)) is determined with proof,
  as either an explicit interleaved schedule with certified d_circ = 12, or a proof that every legal schedule satisfies d_circ
  <= 11; and the published conjectured distance-11 circuit has a certified d_circ = 11.
assessment:
  level: CONJECTURED
  caveats:
  - Do not cite SBB26 Appendix H.2 as proving circuit distance 12 for the original Gross code. Shaw-Terhal Table I reports
    only tilde d_circ <= 12 for a different end-cycle “second gross” code; equality of n=144 and k=12 (or of the 288-qubit
    total hardware count) is not code identity or S_Gross membership.
  summary: 'The optimal circuit-distance question remains CONJECTURED, with D* in {11,12} unresolved. The universal d_ext
    <= 11 cap is PROVED; the candidate-certification route is CERTIFIED*. The latest completion-gap candidate was killed by
    the missed two-prefix shape. The three recorded no-go classes and search machinery are scoped by-products, not a universal
    proof of D*=11. A fresh primary-source scope audit closes the Shaw-Terhal morphing lead negatively: its distance-12-labeled
    endpoint is a different weight-9 [[144,12,12]] “second gross” code with alternating code frames, outside frozen S_Gross,
    and Table I gives only a BP-OSD circuit-distance upper bound <=12. It supplies neither a legal distance-12 witness nor
    a universal <=11 no-go. Round 61''s proposer-level clean-room audit refutes two further completion screens: absence of
    all four individually gain-positive shapes does not exclude cancelling multi-check weight-10 mechanisms, and even a clean
    |V|=12 / at-most-four-check stratum with diagonal short hooks does not exclude repair-zero minimum mechanisms. It also
    finds that hunt2''s j<=4 recursion did not enforce distinct contributing checks; the earlier candidate kill survives because
    its 144 decisive witnesses were separately rebuilt from raw schedules. These are filter no-go results, not a universal
    theorem, so D* remains in {11,12}. Round 62 installs a proposer-level unrestricted 864-edge/648-MC CEGAR package with
    direct-360 effective and arbitrary-round repair adversaries plus raw replay. Its first 20 exact outer schedules are all
    legal, MC-valid and interleaved, and all are killed in Xerr by verified weight-10 mechanisms; 20 sound order-region blocks
    and all 190 prior-block exclusions replay. This is quantitative search progress only: no effective-layer UNSAT, repair-layer
    UNSAT or outer exhaustion was obtained. Round 63 adds a proposer-level library of 1,440 globally valid deletion-minimal
    five-atom single-residual order clauses, exhaustively replayed over 103,680 local-order cases with 7,200 atom-deletion
    controls. A separate ten-step experiment generated 15,874 witness-checked pair-pattern clauses but did not retain the
    raw ledgers needed for absence use. No checked DRUP/DRAT/LRAT proof exists, so the exact residual is unchanged. Round
    68 emits complete direct-360 DIMACS for one unrestricted clause-saturated candidate, but both sectors are SAT and raw
    replay to weight-10 Xerr and weight-8 Zerr mechanisms. Five continuation candidates are likewise killed in both sectors.
    Twelve new sound blocks are retained, for 1,472 total; no direct absence, repair entry or outer exhaustion exists, so
    D* remains in {11,12}. Round 70''s fresh exact review clears the round-69 positive-witness block library as proposer-level
    evidence and licenses strict continuation at outer iteration 6 with 6,212 installed sound blocks. It licenses no absence,
    repair, outer exhaustion, D* narrowing, route change or level change. Round 71 continues through iterations 6--29: all
    24 outer candidates and all 48 complete direct sectors are SAT and raw-replayed, adding 48 candidate-exact blocks. The
    next reviewed-by-dispatcher frontier is iteration 30 with 6,260 blocks; no absence, repair, exhaustion or D* narrowing
    exists. Round 73''s fresh exact review clears the round-72 566-term conservative positive library and iterations 30--41
    as proposer-level evidence. The exact continuation frontier is iteration 42 with 6,850 installed blocks; no absence, repair,
    exhaustion, D* narrowing, route change or level change is licensed. Round 75''s fresh independent exact review clears
    the sealed round-74 online generalization package as proposer-level evidence. Iterations 42--53 add 134 sound generalized
    terms and 24 candidate-exact blocks after twelve legal outer SAT schedules and twenty-four complete direct-sector SAT/raw
    replays. The exact fresh-process continuation is iteration 54 with 7,008 installed blocks: 1,440 unary, 20 round-62, 4,740
    round-69 generalized, 566 round-72 generalized, 134 round-74 generalized and 108 dynamic exact. The review literally replays
    all 1,137,096 retained pair tuples and validates the factorized exhaustive proof for 2,985,984 retained multi tuples.
    Deletion controls establish only candidate-relation or fixed-selector atom minimality, not installed-union or global physical-mechanism
    minimality. No absence, repair, exhaustion, D* narrowing, route change or level change is licensed. Round 77''s fresh
    independent exact review clears the sealed round-76 package as proposer-level evidence. Iterations 54--77 add 303 sound
    generalized terms and 48 candidate-exact blocks after twenty-four legal outer SAT schedules and forty-eight complete direct-sector
    SAT/raw replays. The exact fresh-process continuation is unstarted iteration 78 with G=5,743 generalized, D=156 dynamic
    exact, registry=72 and 7,359 installed blocks. The review literally replays all 2,637,648 retained pair tuples and validates
    two factorized exhaustive multi-domain proofs totaling 55,037,740,032 tuples. It corrects one non-load-bearing provenance
    row: the final sealed compressor is 2,760 bytes with SHA-256 d4abdf75b066d8a2507d5c010f96c1c1760f36c6d1d242048fb45c5928cb8dde;
    the stale pre-adaptation row must not be cited as final inventory. Deletion controls still license only candidate-relation
    or fixed-selector atom minimality. No absence, repair, exhaustion, D* narrowing, route change or level change is licensed.
    Round 79''s fresh independent exact review clears the sealed round-78 cross-registry package as proposer-level evidence.
    Before iterations 78--89, synthesis across all 72 reviewed mechanisms retains 2,826 sound cross-registry terms; the twelve
    legal outer schedules and twenty-four complete direct sectors are all SAT and raw-replayed, adding 24 candidate-exact
    blocks, 62 online terms and 1,964 further cross-registry terms. The review''s non-importing checker actually visits all
    43,834,872 literal selector tuples and validates four factorized exhaustive domains totaling 15,485,313,024 tuples, including
    classification, dominance, union and zero-domain checks. The exact fresh-process continuation is unstarted iteration 90
    with G=10,595 generalized, D=180 dynamic exact, registry/raw=96 and 12,235 installed blocks. One non-load-bearing wording
    correction applies: the derivation''s word "permutation" denotes the encoded legal schedule with allowed parallel layers,
    not a strict total order. No absence, repair, exhaustion, D* narrowing, route change or level change is licensed. Round
    81''s fresh independent exact review clears the sealed round-80 whole-registry package as proposer-level evidence. Its
    exact star synthesis retains 24 strict installed-union expansions, with all 304,704 literal raw-selector pair cells replayed
    and 35,294,400 factorized tuples checked. Iterations 90--101 contain twelve legal outer SAT schedules and twenty-four
    complete direct-sector SAT/raw replays, adding 94 online terms, 2,107 cross-registry terms and 24 candidate-exact blocks.
    The review independently visits all 20,820,216 online/cross literal tuples and validates 55,037,740,032 factorized tuples,
    plus the eight reconstructed multi-selector terms and their exact GF(2) domains. The exact fresh-process continuation
    is unstarted iteration 102 with G=12,820 generalized, D=204 dynamic exact, registry/raw=120 and 14,484 installed blocks.
    No direct query is UNSAT and no accepted absence proof exists, so no repair, exhaustion, D* narrowing, route change or
    level change is licensed. Round 93''s fresh independent exact review clears the sealed Round-92 weight-9 synthesis and
    finite-outer continuation package for proposer-level continuation only. Exact Phase-A enumeration retains 44 new ordinary
    EFSSCs and zero relaxed cubes, with an explicit strict-union expansion witness; iterations 124--135 are twelve legal outer
    SAT schedules with all twenty-four complete unrestricted direct-360 sectors SAT and physically replayed, including weight-9
    mechanisms at iteration 124 Zerr and iteration 133 Xerr. The atomic frontier is fresh/unstarted iteration 136 with the
    same 14,484 inherited order blocks, 232 exact EFSSC selectors, selector-state sha256:1692d905120d2dcf51b949ce4a70ed4b8f1b270c2d07a1ddbf5813d20d80fa81,
    and a checked but unsolved 406,656-variable/1,372,232-clause CNF sha256:289acad6be1068d63369511e9c95b0b1df146471bf05a1e4128758508612b64e.
    The review licenses no Gross UNSAT, direct absence, repair, exhaustion, D* narrowing, route promotion, or root promotion;
    CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}. Round 95''s fresh independent exact review
    clears the sealed Round-94 package for proposer-level continuation only: iterations 136--147 add 24 exact EFSSC selectors
    after twelve legal outer SAT schedules and twenty-four unrestricted direct-sector SAT/physical replays; the complete same-sector
    order-3 GF(2) search retains zero terms; and the fresh frontier is unstarted iteration 148 with 256 selectors and checked-unsolved
    CNF sha256:397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4. No Gross UNSAT, direct absence, repair, exhaustion,
    D* narrowing, route promotion, or root promotion is licensed; CIRCDIST.gross and gap-via-lift remain CONJECTURED with
    D*_Gross in {11,12}. Round 97''s fresh independent exact review clears the sealed Round-96 package for proposer-level
    continuation only: iterations 148--159 add 24 exact EFSSC selectors after twelve legal outer SAT schedules and twenty-four
    unrestricted direct-sector SAT/physical replays; the complete same-sector order-4 GF(2) search covers 15,254,626 distinct
    quadruples and retains zero novel terms; and the fresh frontier is unstarted iteration 160 with 280 selectors and checked-unsolved
    CNF sha256:aa18d2857ed5a7aefacd33bf4fbd42fded914393e123a87f00e84e4920e39d59. No Gross UNSAT, direct absence, repair, exhaustion,
    D* narrowing, route promotion, or root promotion is licensed; CIRCDIST.gross and gap-via-lift remain CONJECTURED with
    D*_Gross in {11,12}. Round 99''s fresh independent exact review clears the sealed Round-98 package for proposer-level
    continuation only: iterations 160--171 add 24 exact EFSSC selectors after twelve legal outer SAT schedules and twenty-four
    unrestricted direct-sector SAT/physical replays; the complete same-sector order-5 GF(2) search covers C(125,5)+C(109,5)=351,359,546
    distinct quintuples, reconstructs 40,153 unique named-weight-1..10 results, finds zero canonical-syndrome-zero results
    in either sector, and retains zero selectors; and the fresh frontier is unstarted iteration 172 with 304 selectors and
    checked-unsolved CNF sha256:f86b8db36af1df3877ca1d9dbafb171b6173ddc8b6c2f045a808dd6c71f98342. No Gross UNSAT, direct absence,
    repair, exhaustion, D* narrowing, route promotion, or root promotion is licensed; CIRCDIST.gross and gap-via-lift remain
    CONJECTURED with D*_Gross in {11,12}. The fresh Round-101 independent exact review clears the sealed Round-100 package
    for proposer-level continuation only: iterations 172--183 add 24 exact EFSSC selectors after twelve legal outer SAT schedules
    and twenty-four unrestricted direct-sector SAT/physical replays; the complete same-sector order-6 search covers C(125,6)+C(109,6)=6,715,648,864
    six-sets and retains zero selectors; and exact all-orders fixed-basis span queries are UNSAT in both sectors after quotienting
    installed named masks. The valid mixed-sector component reduction remains fixed-schedule direct-domain reasoning, not
    global closure. The review corrects one non-load-bearing sentence: the Z triple-key histogram has 209,304 singleton groups
    and 315 doubletons, all nonseparated, rather than all singleton groups. The fresh frontier is unstarted iteration 184
    with 328 selectors and checked-unsolved CNF sha256:2b0030fd15b0ef8154e2dbc37508e03481f11d8c876c4fe59e6541cb3bfacd62. No
    Gross UNSAT, direct absence, repair, exhaustion, D* narrowing, route promotion, or root promotion is licensed; CIRCDIST.gross
    and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}. The fresh Round-103 independent exact review clears the
    sealed Round-102 global-translation package for proposer-level continuation only. It reconstructs the full Z_12 x Z_6
    action, all 517,140 invariant block semantics, the 23,868-selector corrected iteration-186 invariant base, the exact 71-root
    lex quotient and its SAT assignment, all six complete unrestricted direct-360 formulas and physical witnesses, and the
    fresh iteration-187 frontier with 24,012 selectors. The review proves that the first 330-selector lex quotient was unsound
    as a global quotient because its cut registry was not translation closed: a legal base model has a lex-minimal translate
    that hits 75 untranslated installed cuts. Every global conclusion from that flawed quotient is retracted. Its SAT schedule,
    direct witnesses, and their separately replayed translation orbits remain valid positive evidence. The corrected quotient
    is equisatisfiable only with the full invariant base and is SAT; both corrected direct sectors are SAT, so no absence
    or repair result exists. Failures F001--F013 and two bounded UNKNOWN direct prefixes are retained as non-evidence. The
    package lacks a conventional root replay.sh, a real interface defect; the explicit bound-venv source/replay_round102.py
    entry nevertheless passes 13/13 children under the package-bound historical governance overlay. The exact fresh unstarted
    frontier is iteration 187 with 517,140 invariant blocks, 24,012 invariant selectors, base CNF sha256:7f66b46643b6b10cce57358e4e66f7e95cdc1bfe52ee14f77884c56ddd5d5eab
    and quotient CNF sha256:e415b4c2c5b4923a47348a06ea9ebb06bbc85cea2c9c32bd3a9b25a1ce198234. No Gross UNSAT, direct absence,
    repair, exhaustion, distance-12 witness, universal distance-11 ceiling, D* narrowing, route promotion, or root promotion
    is licensed; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}. The fresh Round-105 independent
    exact review clears the sealed Round-104 iteration-187 invariant-continuation package for proposer-level continuation
    only. The exact iteration-187 71-root quotient is SAT with a complete 2,452,334-variable assignment satisfying all 11,789,630
    clauses; its decoded schedule is legal, globally interleaved, and rank-compresses to 451 layers with sha256:ef15e4e8dc53d6d14303238d3a32db6a5d73a4ba3cbd4c28a8f1576debc7dadd.
    Both complete unrestricted direct-360 queries are SAT: Xerr sha256:032757d174845b1311280f15a06bc6af09ee816fe359fefae650cae1174442ea
    and Zerr sha256:fd430c2d8fad7fe7b9db5e1528e127dbe7e575440bba80d92bd93fa405b54d55 each have a physically replayed weight-10
    zero-syndrome nonstabilizer mechanism, so this candidate is not a distance-12 witness and repair is forbidden. The two
    complete 72-element selector orbits add 144 collision-free selectors, preserve all 517,140 invariant block semantics,
    and produce a fresh unstarted iteration-188 frontier with 24,156 invariant selectors. Its base CNF sha256:051dbece97d9cd94a69de7bff644dbb31b35076d0c43558b5408d9f3cc86b257
    has 1,841,756 variables and 6,890,981 clauses; its exact quotient sha256:29b16602aa5cdf0e4207271cb50045454ea0aba9254396d732414459a4029215
    has 2,455,196 variables and 11,798,572 clauses and has never been started. No UNSAT, absence, exhaustion, distance-12
    witness, repair, universal distance-11 ceiling, D* narrowing, route promotion, or root promotion is licensed; CIRCDIST.gross
    and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}. The fresh Round-107 independent exact review clears the
    sealed Round-106 iteration-188 invariant-quotient continuation package for proposer-level continuation only. The mandatory
    2,455,196-variable, 11,798,572-clause iteration-188 quotient sha256:29b16602aa5cdf0e4207271cb50045454ea0aba9254396d732414459a4029215
    is SAT under a complete assignment independently checked exactly once per variable and against every clause. Its decoded
    frozen schedule is legal, globally interleaved, and compresses to 511 layers with gzip sha256:e9daddcf1b38ecf505adeeb0da0a54ddff70ea0aac17c2c72ff81b54dda5f72a.
    Both complete unrestricted direct-360 sectors are SAT at named weight 10; independent formula reconstruction, clause evaluation,
    detector replay, logical pairing, and row-space tests establish zero-syndrome nonstabilizer physical mechanisms, so this
    candidate is not a distance-12 witness and repair is forbidden. Their two free 72-element selector orbits add exactly
    144 collision-free selectors to the invariant registry. The exact fresh unstarted iteration-189 frontier has 517,140 invariant
    blocks and 24,300 invariant selectors; base sha256:f5ccbe6aa4c0a0df5940cd979809003182416900e76a6cc6e3755e493cc6b178 has
    1,847,301 variables and 6,909,336 clauses, and quotient sha256:3ece12a1ea0ee6502982fecfcaf75debae985ea2ddff93ea3b875552c0714df7
    has 2,460,741 variables and 11,816,927 clauses. All three solver streams are SAT traces, never UNSAT certificates. Failures
    F106-001--F106-014 are retained and adjudicated; corrected final seals and fresh post-seal replay fully supersede their
    failed or stale intermediates without erasing them. No Gross UNSAT, direct absence, repair, exhaustion, distance-12 witness,
    universal distance-11 ceiling, D* narrowing, route promotion, or root promotion is licensed; CIRCDIST.gross and gap-via-lift
    remain CONJECTURED with D*_Gross in {11,12}. The fresh Round-109 independent exact review clears the sealed Round-108
    iteration-189 invariant-quotient continuation package for proposer-level continuation only. The mandatory 2,460,741-variable,
    11,816,927-clause quotient is SAT under a complete assignment satisfying every clause; its decoded frozen schedule is
    legal, globally interleaved, and compresses to 448 layers. Both independently rebuilt complete unrestricted direct-360
    sectors are SAT at named weight 10 and physically replay to zero-syndrome nonstabilizer mechanisms, so the candidate is
    not a distance-12 witness and repair is forbidden. The two free 72-element selector orbits add exactly 144 collision-free
    selectors while preserving all 517,140 invariant block semantics. The exact fresh unstarted iteration-190 frontier has
    24,444 selectors, source sha256:5231e7f5b4cd2a74390a5d137b9927276ce73829dc599ddc064ab8f2c94a2d2e, semantic sha256:76881a021258e6fda565ecfe0ad61c1fe0e6f6a97a418ea806c6d3193b692c00,
    base sha256:e3ec0d0b146fc4ade428052d1a14737ffade9974dfc37dd79fa8411841d45fc8 and quotient sha256:12f2fe58f4bfcaff19d543cdb60411f1659e86c8b4f16f599a2d1679aeeca767.
    All three solver streams are SAT traces, not UNSAT certificates. No Gross UNSAT, direct absence, repair, exhaustion, distance-12
    witness, universal distance-11 ceiling, D* narrowing, route promotion, or root promotion is licensed; CIRCDIST.gross and
    gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
  basis:
    routes:
    - candidate-certification
    evidence:
    - path: circdist/artifacts/circdist_gross_whole_registry_round80_20260830
      kind: run
      note: Sealed round-80 proposer package cleared by the fresh round-81 exact review. Whole-registry star synthesis retains
        24 strict installed-union expansions over 304,704 literal raw-selector pair cells and 35,294,400 factorized tuples.
        Iterations 90--101 contain twelve legal outer SAT schedules and twenty-four complete direct-sector SAT/raw replays,
        adding 94 online terms, 2,107 cross-registry terms and 24 candidate-exact blocks. The exact fresh-process restart
        is unstarted iteration 102 with G=12,820, D=204, registry/raw=120 and 14,484 installed blocks. The accepted root seal
        is sha256:e086a828391361620eabfbd31b544606f7817826af546fb8779a500f95ec0426. Positive SAT mechanisms, misses, zero
        domains and deletion controls remain non-absence evidence.
    - path: circdist/reviews/circdist_gross_round80_whole_registry_exact_review_20260830.md
      kind: review
      note: Fresh independent round-81 review with non-importing clean-room checkers. It reconstructs 96 source raw mechanisms,
        138 complete catalogs, all pair and star classifications, twelve outer formulas, twenty-four direct CNFs/assignments
        and 120 final raw mechanisms. It actually visits 304,704 whole-star and 20,820,216 online/cross literal cells; validates
        35,294,400 whole-star and 55,037,740,032 online/cross factorized tuples; and independently closes the eight multi-selector
        GF(2) terms, atomic state chain and exact iteration-102 semantic hashes. All ten FIX-2 incidents and rollback boundaries
        pass audit. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION; claim, routes, D* interval and level remain unchanged. Review
        sha256:e0d6ad5b54768195516239f4d0a262135025a630ecd6292d91cb694baa51597e.
    - path: circdist/artifacts/circdist_gross_cross_registry_round78_20260829
      kind: run
      note: Sealed round-78 proposer package cleared by the fresh round-79 exact review. Cross-registry synthesis over all
        72 reviewed mechanisms retains 2,826 terms before the outer loop; iterations 78--89 contain twelve legal outer SAT
        schedules and twenty-four complete direct-sector SAT/raw replays, adding 24 candidate-exact blocks, 62 online terms
        and 1,964 further cross-registry terms. The exact fresh-process restart is unstarted iteration 90 with G=10,595, D=180,
        registry/raw=96 and 12,235 installed blocks. The accepted root seal is sha256:db82c387493285e56eeddcef6e7bafc3e48954c4034e6ec2fc699cea1699c987;
        both earlier defective seals remain forbidden. Positive SAT mechanisms and deletion controls remain non-absence evidence.
    - path: circdist/reviews/circdist_gross_round78_cross_registry_exact_review_20260830.md
      kind: review
      note: Fresh independent round-79 review with non-importing clean-room checkers. It reconstructs all twelve outer formulas
        and twenty-four direct CNFs/assignments plus 96 raw mechanisms, actually visits all 43,834,872 literal selector tuples
        and validates four factorized exhaustive domains totaling 15,485,313,024 tuples. It verifies classification, dominance,
        union, zero-domain handling, atomic state commits and the exact iteration-90 state and semantic hashes. All v1--v7
        failures, proof-control incident, rejected seals and rollback boundaries pass audit. It records only a non-load-bearing
        use of "permutation" for a schedule allowing parallel layers. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION; claim, routes,
        D* interval and level remain unchanged. Review sha256:e90dc1a23c5c1740267c0ed21920ef4b4af05dab1aecd5eeef934c2a25d2a17a.
    - path: circdist/artifacts/circdist_gross_online_generalizing_round76_20260829
      kind: run
      note: Sealed round-76 proposer package cleared by the fresh round-77 exact review. Iterations 54--77 contain twenty-four
        legal outer SAT schedules and forty-eight complete direct-sector SAT/raw replays. Online generalization produces 420
        candidates and retains 303 sound terms after exact semantic filtering; forty-eight candidate-exact blocks freeze a
        fresh-process restart at iteration 78 with 7,359 installed blocks. The final compressor binding is the 2,760-byte
        sealed file, not the stale pre-adaptation provenance row. Positive misses, zero cells and deletion countertuples remain
        non-absence evidence.
    - path: circdist/reviews/circdist_gross_round76_online_generalizing_exact_review_20260829.md
      kind: review
      note: Fresh independent round-77 review with non-importing clean-room checkers. It reconstructs all twenty-four outer
        formulas and forty-eight direct CNFs/assignments/raw mechanisms, literally replays 2,637,648 retained pair tuples,
        validates two factorized exhaustive multi proofs totaling 55,037,740,032 tuples and the exact state chain G=5,743,
        D=156, registry=72, total=7,359. It records one non-load-bearing compressor provenance correction and limits deletion
        minimality to the candidate relation or fixed selector. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION; claim, routes,
        D* interval and level remain unchanged.
    - path: circdist/artifacts/circdist_gross_online_generalizing_round74_20260829
      kind: run
      note: Sealed round-74 proposer package cleared by the fresh round-75 exact review. Iterations 42--53 contain twelve
        legal outer SAT schedules and twenty-four complete direct-sector SAT/raw replays. Online generalization produces 188
        candidates and retains 134 sound terms after exact semantic filtering; twenty-four candidate-exact blocks freeze a
        fresh-process restart at iteration 54 with 7,008 installed blocks. Positive misses, zero cells and deletion countertuples
        remain non-absence evidence.
    - path: circdist/reviews/circdist_gross_round74_online_generalizing_exact_review_20260829.md
      kind: review
      note: Fresh independent round-75 review with non-importing clean-room checkers. It reconstructs all twelve outer formulas
        and twenty-four direct CNFs/assignments/raw mechanisms, literally replays 1,137,096 retained pair tuples, validates
        the factorized exhaustive 2,985,984-tuple multi proof and exact state chain G=5,440, D=108, total=7,008. It records
        two non-load-bearing documentation corrections and limits deletion minimality to the candidate relation or fixed selector.
        Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION; claim, routes, D* interval and level remain unchanged.
    - path: circdist/artifacts/circdist_gross_round71_generalization_round72_20260829
      kind: run
      note: Sealed round-72 proposer package cleared by the fresh round-73 exact review. It reconstructs all 48 round-71 mechanisms,
        113 local-order catalogs, 607 conservative pair relations and 48 multi-check GF(2) relations, retaining 566 new sound
        generalized terms after exact deduplication/dominance. Iterations 30--41 are twelve further dual-sector SAT/raw-replayed
        candidates. The package licenses continuation at iteration 42 / 6,850 blocks but no absence, repair, exhaustion, D*
        or level claim.
    - path: circdist/reviews/circdist_gross_round72_generalization_exact_review_20260829.md
      kind: review
      note: Fresh independent round-73 review with a non-importing 863-line clean-room checker. It validates 314,668,800 pair
        cells, 32,031,216 retained physical-selector tuples, all 48 source assignments, semantic deduplication from 696 candidates
        to 566 retained terms, twelve outer schedules and twenty-four complete direct SAT/raw replays; verdict CLEAR-PROPOSER-LEVEL-CONTINUATION,
        with claim, routes, D* interval and level unchanged.
    - path: circdist/artifacts/circdist_gross_cegar_continuation_round71_20260829
      kind: run
      note: Sealed round-71 proposer package independently replayed by the dispatcher. Iterations 6--29 contain 24 legal 864-edge/648-MC
        outer schedules; both complete unrestricted direct-360 sectors are SAT for every candidate, and all 48 assignments
        pass every DIMACS clause and raw physical replay. The 48 new exact blocks license strict continuation at iteration
        30 / 6,260 blocks but no absence, repair, exhaustion, D* or level claim.
    - path: circdist/artifacts/circdist_gross_block_minimization_round69_20260829
      kind: run
      note: Sealed round-69 proposer package cleared for positive-witness use by the fresh round-70 exact review. It contains
        4,740 conservative generalized sound blocks backed by 3,368 raw physical mechanisms and 1,197,120 explicit tuple witnesses,
        plus twelve raw-replayed dynamic blocks from six complete dual-sector SAT CEGAR candidates. The 2,704 negative weight-14
        solver observations are non-load-bearing. The package licenses continuation at iteration 6 / 6,212 blocks but no absence,
        repair, exhaustion, D* or level claim.
    - path: circdist/reviews/circdist_gross_block_minimization_exact_review_20260829.md
      kind: review
      note: Fresh independent round-70 review with a non-importing 478-line clean-room checker. It exhaustively validates
        all 15,552,000 pair cells, 56,539,296 antecedent-tuple incidences, 3,368 raw mechanisms, six outer schedules, twelve
        rebuilt direct-360 formulas and every SAT/raw replay; verdict CLEAR-PROPOSER-LEVEL-CONTINUATION, with claim, routes,
        D* interval and level unchanged.
    - path: circdist/artifacts/circdist_gross_direct360_proof_round68_20260829
      kind: run
      note: Sealed round-68 direct-360 package. Dispatcher independently verified the 101-entry manifest, 49 live bindings
        expanding to 424 files, full 864-edge/648-MC model, both 1884-word pools, complete DIMACS and raw SAT assignments,
        twelve new mechanisms/blocks, and DRAT/LRAT positive and corruption controls. Both primary sectors are SAT, so it
        licenses no absence or level claim.
    - path: circdist/artifacts/circdist_gross_pattern_cegar_round63_20260828
      kind: run
      note: Sealed round-63 proposer package. The independently replayed load-bearing output is a 1,440-clause single-residual
        order library with exhaustive 6! local-order soundness checks and atom-deletion controls. The 15,874-clause two-residual
        CEGAR output is explicitly exploratory because raw ledgers/exclusion replay were not retained. It contains zero checked
        proof objects and licenses no absence or level claim.
    - path: circdist/artifacts/circdist_gross_cegar_round62_20260828
      kind: run
      note: Sealed round-62 proposer package containing the unrestricted outer schedule model, direct-360 effective adversary,
        arbitrary-round repair adversary, raw replay validators, 20 sound CEGAR blocks, named/negative controls and SHA manifest.
        All 20 schedules are killed by positive Xerr witnesses; no absence-side UNSAT or outer exhaustion is claimed. Dispatcher
        independently replayed verify.py in a clean dependency environment before linking the directory.
    - path: circdist/artifacts/circdist_dstar_hunt3_20260828.md
      kind: run
      note: Round-61 proposer-level clean-room four-shape and bounded-stratum audit. Two explicit legal interleaved schedules
        refute those filters as sufficient closure criteria; the report also identifies a distinct-check defect in the old
        j<=4 recursion while preserving the raw-verified candidate kill. No exact D* branch closes, no solver UNSAT verdict
        is claimed, and the residual remains {11,12}.
    - path: circdist/artifacts/circdist_gross_morphing_scope_ruling_20260826.md
      kind: text
      note: Fresh primary-source Shaw-Terhal scope audit; the distance-12-labeled morphing endpoint is a different weight-9
        [[144,12,12]] “second gross” code derived from a [[288,12,18]] mid-cycle code; Table I reports only BP-OSD d_circ
        <= 12. The construction is outside frozen S_Gross, closes frontier task-002 negatively, and leaves D*_Gross in {11,12}.
    - path: circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.gross.yaml
      kind: text
      note: Immutable pre-migration record, including every original event, former summary and frontier; historical evidence,
        not an additional completion review.
    - path: circdist/artifacts/history/legacy_DAG_PROTOCOL.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_verdict_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/logs_circdist_gross_verdict_20260823/SHA256SUMS.txt
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_final_decision_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/logs_circdist_gross_final_20260823/SHA256SUMS.txt
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_candidate_decision_20260822.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/logs_circdist_gross_drivers_20260823/SHA256SUMS.txt
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_candidate_unsat_20260822.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_phicert_20260822.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/reviews/circdist_sbbcert_review_20260820.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_sbbcert_20260820.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_lift_iff_proof_20260820.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/reviews/circdist_numerical_review_20260820.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_lift_d3gate_20260820.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_g1_20260820.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_toolfeas_20260820.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_recon_20260820.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/reviews/circdist_gross_verdict_review_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/reviews/circdist_gross_links_review_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_dstar_hunt1_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_dstar_hunt2_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/logs_circdist_dstar_hunt1_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
    - path: circdist/artifacts/logs_circdist_dstar_hunt2_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
    - path: circdist/artifacts/logs_circdist_gross_drivers_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
    - path: circdist/artifacts/logs_circdist_gross_final_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
    - path: circdist/artifacts/logs_circdist_gross_harvest_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
    - path: circdist/artifacts/logs_circdist_gross_links_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
    - path: circdist/artifacts/logs_circdist_gross_verdict_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
    - path: circdist/artifacts/logs_circdist_gross_verdictreview_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
    - path: circdist/artifacts/circdist_campaign4_closeout_20260823.md
      kind: text
      note: Preserved campaign context; not used as a new mathematical premise or completion review.
    - path: circdist/artifacts/history/legacy_FILE_PROTOCOL.md
      kind: text
      note: Preserved campaign context; not used as a new mathematical premise or completion review.
    - path: circdist/artifacts/history/notes/CAMPAIGN4_KICKOFF_20260822.md
      kind: text
      note: Preserved campaign context; not used as a new mathematical premise or completion review.
    - path: circdist/artifacts/history/notes/CAMPAIGN_CLOSEOUT_20260820.md
      kind: text
      note: Preserved campaign context; not used as a new mathematical premise or completion review.
    - path: circdist/artifacts/history/notes/HANDOFF_20260820.md
      kind: text
      note: Preserved campaign context; not used as a new mathematical premise or completion review.
    - path: circdist/artifacts/history/notes/HANDOFF_20260823.md
      kind: text
      note: Preserved campaign context; not used as a new mathematical premise or completion review.
    - path: circdist/artifacts/history/PATH_MAP.json
      kind: text
      note: Mechanical relocation map for immutable historical report references; not mathematical evidence.
    - path: circdist/artifacts/circdist_gross_efssc_round86_20260830
      kind: run
      note: Sealed Round-86 EFSSC proposer package, independently cleared at proposer level in Round 87; root seal sha256:94322390a648262e8cc035f8e843617f134fe2d29ff36191720b646c021c89ff.
        No distance-12 witness, universal distance-11 ceiling, UNSAT/exhaustion result, route promotion, or root promotion
        is inferred.
    - path: circdist/reviews/circdist_gross_efssc_exact_review_round87_20260830.md
      kind: review
      note: Fresh strict-serial Round-87 independent exact review licensing proposer-level continuation from iteration 109
        only, with CIRCDIST.gross and gap-via-lift remaining CONJECTURED and D*_Gross in {11,12}.
    - path: circdist/artifacts/circdist_gross_proof_outer_round88_20260830
      kind: run
      note: 'Sealed Round-88 proof-producing finite-outer continuation package independently cleared at proposer level in
        Round 89; root seal sha256:c4061caff46b632b5c4beb7b6eb33281f3520d07c4dfaaa6eb7c6a33883c7e20 and payload seal sha256:d2de2f014954070f20bbba0e55caf49aed93b26986a63fab77955a75f62c8157.
        Iterations 109--111 are complete outer SAT schedules with all six unrestricted direct-360 sectors SAT at weight 10
        and physically replayed, adding six exact EFSSC selectors atomically. The exact fresh/unstarted frontier is iteration
        112 with 14,484 inherited order blocks, 140 selectors, selector-state sha256:a0364547f846fd68ace7cdba85d89c0f8e6326145243fb0fea7ff543420994cb,
        and an independently checked but unsolved 398,488-variable/1,330,104-clause CNF sha256:a8b917845427a0f746e72200a9a58eb5fac86d5e3c845eeaae69082038c86594.
        This is positive continuation evidence only: no Gross UNSAT, direct absence, repair entry, outer exhaustion, D* narrowing,
        route promotion, or root promotion is licensed.'
    - path: circdist/reviews/circdist_gross_proof_outer_exact_review_round89_20260830.md
      kind: review
      note: Fresh independent Round-89 exact review. It re-derives the 864-event rank-compression theorem, reconstructs all
        19,016/19,018/19,020/19,022 source roots and 14,484 inherited order blocks, exhaustively audits all four deterministic
        Tseitin CNFs/source maps and complete iter109--111 SAT assignments, physically replays all six unrestricted direct-360
        weight-10 mechanisms, verifies exact EFSSC soundness and the atomic 134--136--138--140 selector chain, and confirms
        iteration 112 is fresh, checked, and unsolved. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION; CIRCDIST.gross and its live
        gap route remain CONJECTURED with D*_Gross in {11,12}.
    - path: circdist/artifacts/circdist_gross_proof_outer_round90_20260830
      kind: run
      note: 'Sealed Round-90 proof-producing finite-outer continuation package independently cleared at proposer level in
        Round 91; root seal sha256:41ac5ad7f28895f09aae29a256d91aec241298ec7bfe0d1dec2e14709fa00ca7 and payload seal sha256:545efe756a51190aaa8877e1d0d9fa1100da48aa213811b75a62a1f6a9b6c4d4.
        Iterations 112--123 are twelve complete outer SAT schedules; all twenty-four unrestricted direct-360 sectors are SAT
        and physically replayed, with iteration-115 Zerr and iteration-119 Xerr at weight 9 and the other twenty-two at weight
        10. Twenty-four exact EFSSC selectors were appended atomically. The exact fresh/unstarted frontier is iteration 124
        with 14,484 inherited order blocks, 164 selectors, selector-state sha256:854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3,
        and an independently checked but unsolved 401,040-variable/1,345,190-clause CNF sha256:2dd07d33ff0b29c1f06a7452c3b1c7ca9b6df950e819046f8a712dacb0dd7e5a.
        This is positive continuation evidence only: no Gross UNSAT, direct absence, repair entry, outer exhaustion, D* narrowing,
        route promotion, or root promotion is licensed.'
    - path: circdist/reviews/circdist_gross_proof_outer_exact_review_round91_20260830.md
      kind: review
      note: Fresh independent Round-91 exact review. Non-importing checkers reconstruct all thirteen semantic sources and
        finite CNFs, satisfy every clause of the twelve complete outer assignments, re-audit every frozen legal-schedule condition,
        rebuild all twenty-four unrestricted direct-360 formulas from Gross geometry, and physically replay all mechanisms,
        including the two weight-9 cases. It proves the EFSSC iff semantics over each complete local-order domain, verifies
        the atomic 140--142--...--164 chain, and confirms iteration 124 is fresh, checked, and unsolved. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION;
        CIRCDIST.gross and its live gap route remain CONJECTURED with D*_Gross in {11,12}.
    - path: circdist/artifacts/circdist_gross_proof_outer_round92_20260830
      kind: run
      note: Sealed Round-92 proposer package cleared at proposer level by the fresh Round-93 exact review; root seal sha256:4e255084bdab13ad0b9c295a9fe7cf2aea8231c4a56db656964f0695ddc6c982
        and payload seal sha256:fbc881f0dc54744cb3cfd0c4497571592f8597326ce98362eb42a032ed289090. Exact weight-9 slack synthesis
        retains 44 ordinary EFSSCs and zero relaxed cubes, and its strict-union witness is old164=false/new44=true. Iterations
        124--135 are twelve complete outer SAT schedules with twenty-four complete unrestricted direct-360 SAT/physical replays;
        twenty-four exact selectors are appended atomically after the pre-outer 44. The fresh unstarted frontier is iteration
        136 with 14,484 inherited order blocks, 232 selectors, selector-state sha256:1692d905120d2dcf51b949ce4a70ed4b8f1b270c2d07a1ddbf5813d20d80fa81
        and checked-unsolved CNF sha256:289acad6be1068d63369511e9c95b0b1df146471bf05a1e4128758508612b64e. SAT traces and synthesis
        misses are non-absence evidence; no repair, exhaustion, D* narrowing, route promotion, or root promotion is licensed.
    - path: circdist/reviews/circdist_gross_proof_outer_weight9_exact_review_round93_20260830.md
      kind: review
      note: Fresh independent Round-93 exact review. Clean-room standard-library checkers reconstruct both Round-90 weight-9
        bases, every finite Phase-A domain and retained predicate, the strict-expansion witness, all thirteen outer sources/CNFs/maps,
        all twelve complete outer assignments/legal schedules, all twenty-four direct-360 formulas and physical mechanisms,
        and the exact 164->208->232 atomic selector lineage. It independently checks proof fixtures, SAT-trace negative controls,
        process closure, input bindings, manifests, and repository gates, and confirms iteration 136 is fresh, checked, and
        unsolved. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross
        in {11,12}.
    - path: circdist/artifacts/circdist_gross_proof_outer_round94_20260830
      kind: run
      note: Sealed Round-94 proof-producing finite-outer continuation package independently cleared at proposer level in Round
        95; final root seal sha256:1e0a4af8591aa63ccccd1b2516c630eccb11a73fb9dea2e0ff1e0d32ed82ac1c and payload seal sha256:c39ef3552e461dd7513812b8296901e72369dfacbf6e71ae758b5bb58ed94c54.
        Iterations 136--147 are twelve complete legal outer SAT schedules; all twenty-four unrestricted direct-360 sectors
        are SAT and physically replayed, with iteration-138 Xerr at weight 9 and the other twenty-three mechanisms at weight
        10. Twenty-four exact EFSSC selectors were appended atomically. The complete same-sector order-3 GF(2) search covers
        C(125,3)+C(109,3)=527,684 triples, finds 4,232 novel unique outputs of named-location weight at most 10, rejects every
        one by nonzero frozen-schedule syndrome, and retains zero terms. The exact fresh/unstarted frontier is iteration 148
        with 14,484 inherited order blocks, 256 selectors, selector-state sha256:9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f,
        and independently checked but unsolved 409,157-variable/1,385,059-clause CNF sha256:397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4.
        The superseded first seals are non-final. Positive SAT mechanisms, SAT traces, and the finite order-3 no-go prove
        no Gross absence, repair, exhaustion, D* narrowing, route promotion, or root promotion.
    - path: circdist/reviews/circdist_gross_proof_outer_round94_exact_review_round95_20260830.md
      kind: review
      note: Fresh independent Round-95 exact review. A non-importing standard-library checker reconstructs all thirteen outer
        semantic sources/CNFs/maps/traces, satisfies all 16,537,519 clauses of the twelve complete outer assignments, decodes
        twelve distinct legal frozen schedules, rebuilds all twenty-four unrestricted direct-360 formulas and physical mechanisms,
        proves the exact EFSSC domains and atomic 232--234--...--256 lineage, exhausts the 527,684-triple same-sector order-3
        domain and replays all 4,232 novel weight-at-most-10 outputs. It also checks the fresh unsolved iteration-148 frontier,
        manifests, environment, proof fixtures, all six disclosed incident classes, exact final 1,570-path prelink closure,
        protected state, process closure, and the complete replacement on a disposable overlay. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION;
        CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.
    - path: circdist/artifacts/circdist_gross_proof_outer_round96_20260831
      kind: run
      note: Sealed Round-96 proof-producing finite-outer and exact same-sector order-4 continuation package independently
        cleared at proposer level in Round 97; final root seal sha256:d992087072835e2651834aceb3012f8afd20442b2886673b45254e95e861a361
        and payload seal sha256:9cf210a8dd392a57700a61b640ced0deda5d212173f88293083759f67cb77121. Iterations 148--159 are
        twelve complete legal outer SAT schedules; all twenty-four unrestricted direct-360 sectors are SAT and physically
        replayed, with iteration-148 and iteration-152 Xerr/Zerr named weights 10/9 and every other sector weight 10. Twenty-four
        exact EFSSC selectors were appended atomically. The exact same-sector order-4 GF(2) search covers C(125,4)+C(109,4)=15,254,626
        distinct quadruples. Its sole conservative syndrome-zero result is Zerr logical action 100110100011 and is already
        inherited, so zero novel selectors are retained. The exact fresh/unstarted frontier is iteration 160 with 14,484 inherited
        order blocks, 280 selectors, selector-state sha256:ad3cf364dd9224c14ffb55046ba3dc8eb80035b1eaf997f1d7a5691297ad62a3,
        and independently checked but unsolved 411,526-variable/1,396,722-clause CNF sha256:aa18d2857ed5a7aefacd33bf4fbd42fded914393e123a87f00e84e4920e39d59.
        Positive SAT mechanisms, SAT streams, and the finite order-4 no-go prove no Gross absence, repair, exhaustion, D*
        narrowing, route promotion, or root promotion.
    - path: circdist/reviews/circdist_gross_proof_outer_round96_exact_review_round97_20260831.md
      kind: review
      note: Fresh independent Round-97 exact review. A non-importing standard-library checker reconstructs all thirteen outer
        semantic sources/CNFs/maps/traces, satisfies every clause of the twelve complete outer assignments, decodes twelve
        distinct legal frozen schedules, rebuilds all twenty-four unrestricted direct-360 formulas and physical mechanisms,
        proves the exact EFSSC semantics and atomic 256--258--...--280 lineage, and exhausts the 15,254,626-quadruple same-sector
        order-4 domain with exact multiplicity and conservative schedule-validity checks. It also verifies the fresh unsolved
        iteration-160 frontier, manifests, environment, proof fixtures, all disclosed incident classes, exact final 1,588-path
        prelink closure, protected state, process closure, and the complete replacement on a disposable overlay. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION;
        CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.
    - path: circdist/artifacts/circdist_gross_proof_outer_round98_20260831
      kind: run
      note: Sealed Round-98 proof-producing finite-outer and exact same-sector order-5 continuation package independently
        cleared at proposer level in Round 99; final root seal sha256:f64feb1b424b4aff938a1b5a0c1f9a799179e41f4ec99295c5c67376fad9142f
        and payload seal sha256:2df276eb26dc569f830d0c95ac76aa5ed322bc9fcb525637a96196d66394e6ec. Iterations 160--171 are
        twelve complete legal outer SAT schedules; all twenty-four unrestricted direct-360 sectors are SAT and physically
        replayed, with iteration-161 Xerr at named weight 9 and every other sector at named weight 10. Twenty-four exact EFSSC
        selectors were appended atomically. The exact same-sector order-5 GF(2) search covers C(125,5)+C(109,5)=351,359,546
        distinct quintuples, reconstructs 38,382 Xerr plus 1,771 Zerr unique named-weight-1..10 results, finds zero canonical-syndrome-zero
        results in both sectors, and retains zero selectors. The exact fresh/unstarted frontier is iteration 172 with 14,484
        inherited order blocks, 304 selectors, selector-state sha256:a5c64ae41f474844ecd3ac41829331f54d419a81573e4f0e11528db0b49e25d1,
        and independently checked but unsolved 413,646-variable/1,406,245-clause CNF sha256:f86b8db36af1df3877ca1d9dbafb171b6173ddc8b6c2f045a808dd6c71f98342.
        Positive SAT mechanisms, SAT streams, and the finite order-5 no-go prove no Gross absence, repair, exhaustion, D*
        narrowing, route promotion, or root promotion.
    - path: circdist/reviews/circdist_gross_proof_outer_round98_exact_review_round99_20260831.md
      kind: review
      note: Fresh independent Round-99 exact review. A non-importing standard-library checker reconstructs all thirteen outer
        semantic sources/CNFs/maps/traces, satisfies all 16,805,239 clauses of the twelve complete outer assignments, decodes
        twelve distinct legal frozen schedules, rebuilds all twenty-four unrestricted direct-360 formulas and physical mechanisms,
        proves exact EFSSC semantics and the atomic 280--282--...--304 lineage, and confirms fresh iteration 172. A separately
        compiled independent C++ enumerator uses lexicographic next-combination traversal, explicit little-endian I/O, 64-bit
        counters with 128-bit binomial arithmetic, and an ordered full-six-word key map without hashing; it exhausts all 351,359,546
        distinct same-sector quintuples and produces byte-identical eligible outputs before all 40,153 unique low-named-weight
        results are independently replayed. The review also verifies both manifests, the reviewed Round-96 dependency, process/FIX-2
        closure, proof controls, all rejected failures and packaging interruptions, exact prelink closure semantics, protected
        state, repository gates, and the complete replacement on a disposable overlay. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION;
        CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.
    - path: circdist/artifacts/circdist_gross_proof_outer_round100_20260831
      kind: run
      note: 'Sealed Round-100 finite-outer, exact same-sector order-6, and fixed-basis full-span package independently cleared
        at proposer level by the fresh Round-101 exact review. Its two-level identities are SHA256SUMS sha256:37d542fd5ec88370351efdba043506ee0d2b581f458dd5b6d882249260a63e49,
        payload sha256:c35ee5e5944f40b76320de1bdeafca9830315046e8fb5e3e90b74dc81f502c19, and inventory sha256:fc9def57f4bea09822271895ac9a76a56092b39d4db42a4de6695996b3a2465b.
        Iterations 172--183 are twelve complete legal outer SAT schedules; all twenty-four unrestricted direct-360 sectors
        are SAT and physically replayed, and twenty-four exact selectors were appended atomically. The exact same-sector order-6
        theorem covers C(125,6)+C(109,6)=6,715,648,864 six-distinct sets and retains zero selectors. The exact all-orders
        span CNFs are UNSAT only over the fixed post-iteration-136 Xerr/Zerr bases and fixed schedule after excluding installed
        full named masks; they say nothing about arbitrary mechanisms outside those spans. The review corrects SYNTHESIS_PROOF.md:
        Z has 315 size-two triple-key groups, all nonseparated, not an all-singleton histogram. Failures F001--F012 are retained;
        F006 is the first incomplete replay under base Python without z3 and F007 is the incomplete replay whose hard-coded
        204-record census included later packaging records. Neither supports a package verdict, and neither is a Round-98
        capacity interruption. The exact fresh/unstarted frontier is iteration 184 with 328 selectors and checked-unsolved
        CNF sha256:2b0030fd15b0ef8154e2dbc37508e03481f11d8c876c4fe59e6541cb3bfacd62. Positive SAT mechanisms and the scoped
        synthesis no-go results prove no Gross absence, repair, exhaustion, D* narrowing, route promotion, or root promotion.'
    - path: circdist/reviews/circdist_gross_proof_outer_round100_exact_review_round101_20260831.md
      kind: review
      note: Fresh independent Round-101 exact review. It binds the package to the exact dispatched scheduler and prior canonical
        state; reconstructs every iteration-172--184 source/map/trace/CNF tuple, every clause of the twelve outer and twenty-four
        direct SAT assignments, every frozen physical replay, and the atomic 304--328 selector lineage; proves the exact order-6
        MITM coverage and collision logic; regenerates both full-span CNFs and checks Z3, DRAT, LRAT, valid controls, and
        every corrupt/truncated negative control; proves the mixed-sector reduction at its actual fixed direct scope; checks
        manifests, all twelve failures, the 211/204 process censuses, 38 nonoverlapping solver intervals, proof-stream deletion,
        FIX-2, repository gates, and a fresh 127+18-child sealed replay. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION with the
        Z triple-key documentation correction; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.
    - path: circdist/artifacts/circdist_gross_global_closure_round102_20260901
      kind: run
      note: 'Sealed Round-102 global-translation and orbit-closure package independently cleared at proposer level by the
        fresh Round-103 exact review. Its identities are root SHA256SUMS sha256:80e70f62075a852355029b765cbe7ebfa4f8156d25b6d9fa2ea1ddbb9e19b4f4,
        payload sha256:d0f7c5257a779f63f7015409cafc19b18da2bb02b76f190c62e878059e82b5f9, and inventory sha256:9c8b8db51cd170a13ff0cb20b90c3f1c0d401de23b468a70b3976914bdd4308c.
        The exact Z_12 x Z_6 action closes 14,484 inherited block records (14,477 unique semantics) to 517,140 invariant semantics
        and closes 474 positive-evidence selectors to 23,868 invariant selectors. The corrected iteration-186 base CNF sha256:00a5f305166aded035442f689f2d8bd13d52622a258733e18342cb7ca3608dd9
        has 1,834,360 variables and 6,867,095 clauses; its exact 71-root quotient sha256:f6dec16c6ee19ee1a041d3eb78786171558f54805c3038ce9c311c62b82d7c13
        has 2,447,800 variables and 11,774,686 clauses and is SAT. Both complete unrestricted direct-360 sectors are SAT and
        their 144 translated selectors are sound, yielding fresh unstarted iteration 187 with 517,140 blocks, 24,012 selectors,
        base sha256:7f66b46643b6b10cce57358e4e66f7e95cdc1bfe52ee14f77884c56ddd5d5eab and quotient sha256:e415b4c2c5b4923a47348a06ea9ebb06bbc85cea2c9c32bd3a9b25a1ce198234.
        The initial incomplete-registry quotient is scientifically retracted: its lex-minimal translate may hit an untranslated
        installed cut, so it licenses no global quotient conclusion. Its independently replayed SAT schedule/direct orbits
        are positive evidence only. F001--F013, bounded UNKNOWN prefixes, and the absent conventional root replay.sh interface
        are retained. No root branch, absence, repair, exhaustion, distance narrowing, or status promotion follows.'
    - path: circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md
      kind: review
      note: Fresh independent Round-103 exact review. It binds the sealed package to the dispatched scheduler and prior canonical
        state; recomputes every manifest row and physical count; reconstructs the frozen Gross geometry, all 72 translations,
        group law, detector/logical/direct actions, all 1,416,404 iteration-184 clauses, all six direct formulas and models,
        exact block/selector orbit closure with collisions and stabilizers, both corrected base and quotient CNFs, the 11,774,686-clause
        SAT assignment, and fresh unstarted iteration 187. It supplies a concrete legal-model counterexample to the first
        non-invariant quotient, retracts every global inference from it while preserving independently replayed positive evidence,
        audits all five deterministic compressed streams, thirteen failures, 106 process records, eleven nonoverlapping solver
        intervals, repository/proof controls, and a fresh strict-serial 13-child source-entry replay. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION;
        the missing root replay.sh is a nonblocking packaging/interface defect; CIRCDIST.gross and gap-via-lift remain CONJECTURED
        with D*_Gross in {11,12}.
    - path: circdist/artifacts/circdist_gross_iter187_invariant_continuation_round104_20260901
      kind: run
      note: Sealed Round-104 exact iteration-187 continuation package cleared at proposer level by the fresh Round-105 review.
        Package identities are root SHA256SUMS sha256:410807a787005a0fb5ebb1753f8b75712c798d9a15e9101f1265d0be25206ebb, payload
        sha256:e80b85386ae928307ac56ef5cc7c5c8fc5be31768656cefe66b6d903b1abcb33 and inventory sha256:570ea025da23de1802cb9f9f45dfd5f8d4ddf881d567aa3679ef86a119983906.
        The iteration-187 invariant quotient is SAT; the legal 451-layer model is killed by complete unrestricted Xerr and
        Zerr weight-10 physical mechanisms. Their two full translation orbits add 144 exact selectors without collisions and
        preserve the invariant registry. The exact fresh unstarted iteration-188 state has 517,140 blocks, 24,156 selectors,
        selector-state sha256:90999b94525d7e4d23c7e62d4caf057a061baa461c56941057043b0ba3e22e99, base sha256:051dbece97d9cd94a69de7bff644dbb31b35076d0c43558b5408d9f3cc86b257
        and quotient sha256:29b16602aa5cdf0e4207271cb50045454ea0aba9254396d732414459a4029215. All three solver outcomes are
        SAT; proof-side streams are traces, not UNSAT certificates. No absence, repair, exhaustion, distance narrowing, route
        change or level change follows.
    - path: circdist/reviews/circdist_gross_iter187_invariant_continuation_round104_exact_review_round105_20260901.md
      kind: review
      note: Fresh independent Round-105 exact review. It binds all governance and seal identities; rehashes every manifest
        and inventory row; runs the conventional root replay.sh in a clean environment with 14/14 strict-serial children;
        and independently reconstructs the Z_12 x Z_6 geometry, all 11,789,630 iteration-187 quotient clauses and complete
        assignment, lex leaders, legal schedule, both direct CNFs and physical mechanisms, exact 72-element selector orbits,
        all 1,034,280 block and 48,312 selector generator cases, the fresh iteration-188 source/base/quotient bijections,
        three 8.55-GB SAT trace roundtrips, proof controls, nine disclosed failures, 31 retained PID records and repository
        gates. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION; evidence/frontier reuse only. CIRCDIST.gross and gap-via-lift remain
        CONJECTURED with D*_Gross in {11,12}.
    - path: circdist/artifacts/circdist_gross_iter188_invariant_quotient_continuation_round106_20260901
      kind: run
      note: Sealed Round-106 exact iteration-188 invariant-quotient continuation package independently cleared at proposer
        level by the fresh Round-107 exact review. Package identities are root SHA256SUMS sha256:0b9cc6d4074e8397062219ec8d079afbcf0388e14912ab925b5d66ac00c61c9d,
        payload sha256:232e81354fa4d9a579256a231274467ce92d26a2fd6f47182c03fd8c84a927c6 and inventory sha256:dfc282893f20a5dde928415c2a0d690741ec29e7a977f32c7ee9f939f0cf6cd3;
        it is bound to canonical predecessor sha256:3fe41bc65891f94f65be55931c40f37cf3bbb3c5bdb7cca9cfa70a73489526ae and prior
        review sha256:01d14be78fc75362c16340b4ba32df783a645084a819fc18a96f432d9a45e932. The iteration-188 full-invariant quotient
        is SAT and decodes a legal 511-layer schedule; complete unrestricted Xerr and Zerr direct formulas are SAT at named
        weight 10 and physically replay to nonstabilizer mechanisms. Their two full free translation orbits add 144 collision-free
        exact selectors, yielding fresh unstarted iteration 189 with 517,140 blocks, 24,300 selectors, base sha256:f5ccbe6aa4c0a0df5940cd979809003182416900e76a6cc6e3755e493cc6b178
        and quotient sha256:3ece12a1ea0ee6502982fecfcaf75debae985ea2ddff93ea3b875552c0714df7. All solver streams are SAT traces.
        No absence, repair, exhaustion, distance narrowing, route change, or level change follows.
    - path: circdist/reviews/circdist_gross_iter188_invariant_continuation_round106_exact_review_round107_20260901.md
      kind: review
      note: Fresh independent Round-107 exact review. It rehashes every root and payload manifest and inventory row, proves
        a fresh clean replay leaves every sealed byte and metadata field unchanged, reconstructs the invariant iteration-188
        source/base/quotient bijections and every quotient clause, verifies the complete SAT assignment and legal 511-layer
        schedule, rebuilds both unrestricted direct formulas and physical mechanisms, proves the exact free Z_12 x Z_6 action
        and both collision-free 72-element selector orbits, reconstructs fresh unstarted iteration 189, streams all three
        gzip traces, audits proof controls and all 37 process records, adjudicates F106-001--F106-014, and passes all candidate
        repository gates on a disposable overlay. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION; evidence/frontier reuse only.
        CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.
    - path: circdist/artifacts/circdist_gross_iter189_invariant_quotient_continuation_round108_20260901
      kind: run
      note: Sealed Round-108 exact iteration-189 invariant-quotient continuation package independently cleared at proposer
        level by the fresh Round-109 exact review. Package identities are root SHA256SUMS sha256:6c7f94706744ec7e11dcae7616d56ac3cc816025c72c25d4dc7396f981666cc0,
        payload sha256:f8a998b19317a2a9d1ff77a8cf8e7d6cb9bf55c6f15962036dce88919a60e5e5 and inventory sha256:e4b09cb611b0cdceb3296da881280fd3e9f2af76078d0178aaade14ae9b59004;
        it is bound to canonical predecessor sha256:8b805a806d5b704047f4ccca648c92efe11740d7c5b7825659eb1e6b7b5dc977 and prior
        review sha256:eda1d894cde8a56fd7eac9188ed2bb73bef4ddd7842e2fcb091435cbd759c036. The iteration-189 full-invariant quotient
        is SAT with a complete assignment and legal 448-layer schedule; complete unrestricted Xerr and Zerr formulas are SAT
        at named weight 10 and physically replay to nonstabilizer mechanisms. Their two full free translation orbits add 144
        collision-free exact selectors, yielding fresh unstarted iteration 190 with 517,140 blocks, 24,444 selectors, base
        sha256:e3ec0d0b146fc4ade428052d1a14737ffade9974dfc37dd79fa8411841d45fc8 and quotient sha256:12f2fe58f4bfcaff19d543cdb60411f1659e86c8b4f16f599a2d1679aeeca767.
        All solver streams are SAT traces. No absence, repair, exhaustion, distance narrowing, route change, or level change
        follows.
    - path: circdist/reviews/circdist_gross_iter189_invariant_continuation_round108_exact_review_round109_20260902.md
      kind: review
      note: Fresh independent Round-109 exact review. It binds live governance and all seal identities; recomputes every one
        of 443 root-manifest, 436 payload-manifest and 442 inventory rows; proves zero package content or metadata change
        around a fresh clean 18-child strict-serial root replay; independently reconstructs the Z_12 x Z_6 action, 4,478,976
        edge compositions, all iteration-189 source/base/quotient semantics, every quotient clause and complete assignment,
        legal schedule, both direct CNFs and physical mechanisms, exact free selector orbits and generator cases, and byte-identical
        fresh unstarted iteration 190 source/base/quotient artifacts; roundtrips all 5,394,843,044 raw bytes of the three
        deterministic-gzip SAT traces; rechecks valid/corrupt/truncated proof controls and nested PIDs; audits F108-001--F108-004,
        all 37 retained process records, three solver intervals, cleanup/censuses, and the repository overlay gates. Verdict
        CLEAR-PROPOSER-LEVEL-CONTINUATION; evidence/frontier reuse only. CIRCDIST.gross and gap-via-lift remain CONJECTURED
        with D*_Gross in {11,12}.
routes:
  candidate-certification:
    premises:
    - CIRCDIST.gross.dext-cap
    assumptions:
      sbb-thm1:
        kind: external-theorem
        statement: 'SBB Thm 1 (arXiv:2603.05481, Theorem 1): d_circ of the candidate circuit equals the minimum distance of
          the associated extended code (two 360-column codes, one per sector) — the reduction this route''s entire certification
          rides on. PROOF VERIFIED 2026-08-23 (wave 36, artifacts/circdist_gross_links_review_20260823.md): re-derived against
          the frozen model, scoped to claim (11), R = E, NON-INTERLEAVED schedules, no 公共定义 mismatch; two published-proof
          defects found and closed (double Prop-2-for-Prop-3 mis-citation — typo, the needed statement is proved in the paper;
          the partition-by-idling step false as drawn for an LRC, closed by an order-preserving re-timing argument, 0/144
          qubits without a consistent order). UNUSABLE for interleaved schedules (only the paper''s claim (12) applies there).
          PDF on disk at <home>/Documents/ChatGPT/circcert/papers/.'
        source:
          note: arXiv:2603.05481 Theorem 1; local PDF under <home>/Documents/ChatGPT/circcert/papers/ (outside this
            repository).
    implication: Via SBB26 Thm 1 the statement d_circ = 11 for the candidate circuit reduces to an exact minimum-distance
      certification on a 360-column extended code (not a circuit-level DEM search); combined with the universal d_ext cap
      this certifies the first half of the claim and pins the achievable floor at 11.
    proof:
      sketch: Finite exact computation with a distance certificate; risk is solver scaling and recovering the actual published
        schedule. Recon P 0.60, D 2 sessions.
      sources:
      - path: circdist/artifacts/circdist_gross_recon_20260820.md
        kind: text
      - path: circdist/artifacts/circdist_gross_sbbcert_20260820.md
        kind: text
    assessment:
      level: CERTIFIED*
      caveats:
      - UNSAT verdicts are solver-grade certificates, not LRAT-checked (no DRAT toolchain on this machine).
      - 'Reconstruction, not authorship: the candidate schedule is the phicert reading of SBB Figure 12 (pixel-verified wave
        13; legality-filter uniqueness re-derived wave 36 over a LARGER space — 72 readings, one object), not a circuit published
        as machine-readable data by the authors.'
      - 'The shared colour-map constraint is LOAD-BEARING for uniqueness: with independent per-panel colour maps the reading
        space grows to 528 with 12 extra pairings (wave-36 finding); the frozen reading keeps the shared map, as the paper''s
        construction implies.'
      - SBB Thm 1 is VERIFIED (wave 36) scoped to claim (11), R = E, NON-INTERLEAVED schedules — it is unusable for interleaved
        schedules (only claim (12) applies there); the candidate is non-interleaved, so the route is unaffected, but no interleaved
        conclusion may cite it.
      - The implication text says "a 360-column extended code"; it is TWO 360-column codes, one per CSS sector (wave-36 precision
        note; rewording would rebind the implication hash and is left to a future fold).
      - 'Carried from wave 13: the verdict artifact''s cross-checking overstatement stands corrected (114 truly multiply-decided,
        not 860; 1026 records, not 3000; max 3 real decisions per sub-query); Figure-12 fill-convention conflict recorded
        and harmless.'
      summary: 'Promoted NUMERICAL -> CERTIFIED* 2026-08-23 (wave 36, artifacts/circdist_gross_links_review_20260823.md):
        the two inherited proposer-grade links are CLOSED — link 3 (phicert legality filter) CONFIRMED STRENGTHENED with the
        reviewer''s own EXHAUSTIVE weight-12 pool (meet-in-the-middle C, 1884/sector — the artifacts'' heuristic ISD pool
        shown exactly complete) and uniqueness re-derived over all 720 edge-maps per panel at t = 6,7,8 (72 readings, ONE
        object, pairing invariant, phi forced to a + b, no second reading; phicert §2.5''s "moderate" sublattice flag retires);
        link 4 (encoding fidelity) CONFIRMED as an exact reformulation of Def 2/3 (360 columns identical, 216/216 residual
        columns, 60/60 + 60/60 witness round-trips both sectors, 5/5 recorded CNF hashes rebuilt, W = 11 UNSAT / W = 12 SAT
        control); and SBB Thm 1''s PROOF IS VERIFIED against the frozen model (scoped: claim (11), R = E, non-interleaved;
        no 公共定义 mismatch) with two published-proof defects found and closed — a double Prop-2-for-Prop-3 mis-citation (needed
        statement proved in the paper), and the partition-by-idling step false as drawn for an LRC, closed by the reviewer''s
        own re-timing argument (0/144 qubits lack a consistent order). Verdict clauses (d) d_circ = 11 and (f) D* >= 11 are
        thereby lifted from PARTIAL. HISTORY: promoted CONJECTURED -> NUMERICAL 2026-08-23 by the wave-13 adversarial review
        (990/990 UNSAT reproduced; Figure-12 pixel-verified; d_ext = 11 both sectors).'
      basis:
        reviews:
        - path: circdist/reviews/circdist_gross_links_review_20260823.md
          kind: review
          scope: Wave-36 closure of the two inherited links (exhaustive-pool legality-filter uniqueness; encoding-fidelity
            round-trips and CNF hash rebuilds) plus verification of the SBB Thm 1 proof against the frozen model with two
            published-proof defects closed; licenses the route at CERTIFIED*.
          locator: Section 5
          reviewed_hash: sha256:4f40673227208c58d21650b3d685670019f5460b44ee52c0440b22293eec1598
        - path: circdist/reviews/circdist_gross_verdict_review_20260823.md
          kind: review
          scope: Independent adversarial review of the final compute verdict — analytic 990-slot completeness re-derived,
            orbit partition + equivariance closed, slot bookkeeping recomputed from SHA256-verified logs, 3+ adversarial spot
            re-decisions with a different solver, 50/50 witness re-verification, Figure-12 pixel verification at 900 dpi,
            inherited-links audit, per-clause verdicts with an honest downgrade of the verdict artifact's cross-checking claim.
          locator: Per-clause verdicts
          reviewed_hash: sha256:4f40673227208c58d21650b3d685670019f5460b44ee52c0440b22293eec1598
        runs:
        - path: circdist/artifacts/circdist_gross_sbbcert_20260820.md
          kind: run
          scope: Full certification sweep of the group-tiled representative class of the SBB candidate on the 360-column extended
            code, both sectors, symmetry-quotiented SAT decision queries; 10/10 eliminated-assignment witnesses audited end-to-end.
          result: d_ext <= 10 for all 8 survivors (hence all group-tiled assignments); d_ext(R) = 11 exactly for every <=
            2-check subset; gross code d = 12 reproduced as method validation; no 6-layer gross SEC is measurement-consistent
            (exact SAT, 55 s).
        evidence:
        - path: circdist/reviews/circdist_sbbcert_review_20260820.md
          kind: text
  gap-via-lift:
    premises:
    - CIRCDIST.gross.dext-cap
    - CIRCDIST.lift.iff
    implication: Given the universal d_ext <= 11 cap, D* = 12 holds iff some interleaved schedule has completion gap >= 1
      at weight 12; the closed-lift criterion turns this into a voltage/monodromy condition checkable per witness family,
      deciding the second half of the claim in either direction.
    proof:
      sketch: Cross-root import; inherits CIRCDIST.lift risk. Recon P 0.20, D 5 (about 2 sessions shared with the lift subtree).
      sources:
      - path: circdist/artifacts/circdist_gross_recon_20260820.md
        kind: text
    assessment:
      level: CONJECTURED
      summary: 'STAGE-2 VERDICT (wave 38): THE CANDIDATE IS DEAD IN BOTH SECTORS — d_eff <= 10, not 11 (Z: 72 configs at j
        <= 3, 180 at j <= 4; X: 72/84; zero at weights 8-9; all 144 witnesses re-verified from raw CNOT times and re-derived
        inside the campaign''s 360-column model), killed by the FOURTH gain-positive residual shape (the 2-prefix {i1,i2},
        = 4-suffix mod stabiliser) which wave 37''s d_eff filter missed (it tested 2 of 4 shapes); decisively, every X-memory
        weight-10 witness has exact repair = 1, so d_circ <= 11 for the candidate regardless. REPRICING: P(D* = 12) 0.30 ->
        0.10; P(D* = 11) 0.10 -> 0.15 — three no-go walls now stand at proposer level (check-serial class repair-0 PROVED;
        fully-TI cannot hold d_eff = 11 both sectors; all 297 interleaved re-timings of M_cand die on horizontal hooks, 100
        percent repair-0). NEW LEMMA D (proposer): d_eff depends only on within-check orders, so M_cand''s certification TRANSFERS
        to its interleaved re-timings (up to 504/648 interleaved) for free. D* remains OPEN in {11, 12}, evidence direction
        tilted toward 11. STAGE-1 HISTORY (candidate since killed): a 3-colour-tiled annealed schedule — legal, 0/648 MC violations,
        384/648 pairs interleaved, 72/72 hooks diagonal 0 vertical both sectors, no weight-<=10 configs — has repair-0 on
        0/144 (Z) and 0/360 (X) canonical minimum-weight gamma (same-round and 2-group multi-round), the exact gap signature
        the PROVED criterion demands. Schedule recorded in the hunt artifact. BINDING REMAINING CHECK (stage 2): SAT-certify
        d_eff = 11 for this schedule in both sectors and close the two uncovered |gamma| = 11 shapes (weight-13 provably empty
        — all gross logicals have even weight). Stage-1 no-go by-products: the whole CHECK-SERIAL (global-potential) class
        is PROVED repair-0 (226/226 + 170/170, with the two-line u(S) argument) so cannot gap; no fully-TI schedule keeps
        d_eff = 11 in both sectors (353/400 and 357/400 die on d_eff <= 10) — the binding constraint for a gap witness is
        keeping d_eff UP, not making repair positive. Stage-2 pricing: P(D* = 12 witness) 0.30, P(D* = 11 no-go) 0.10. The
        fresh Round-105 independent exact review clears the sealed Round-104 iteration-187 invariant-continuation package
        for proposer-level continuation only. The exact iteration-187 71-root quotient is SAT with a complete 2,452,334-variable
        assignment satisfying all 11,789,630 clauses; its decoded schedule is legal, globally interleaved, and rank-compresses
        to 451 layers with sha256:ef15e4e8dc53d6d14303238d3a32db6a5d73a4ba3cbd4c28a8f1576debc7dadd. Both complete unrestricted
        direct-360 queries are SAT: Xerr sha256:032757d174845b1311280f15a06bc6af09ee816fe359fefae650cae1174442ea and Zerr
        sha256:fd430c2d8fad7fe7b9db5e1528e127dbe7e575440bba80d92bd93fa405b54d55 each have a physically replayed weight-10
        zero-syndrome nonstabilizer mechanism, so this candidate is not a distance-12 witness and repair is forbidden. The
        two complete 72-element selector orbits add 144 collision-free selectors, preserve all 517,140 invariant block semantics,
        and produce a fresh unstarted iteration-188 frontier with 24,156 invariant selectors. Its base CNF sha256:051dbece97d9cd94a69de7bff644dbb31b35076d0c43558b5408d9f3cc86b257
        has 1,841,756 variables and 6,890,981 clauses; its exact quotient sha256:29b16602aa5cdf0e4207271cb50045454ea0aba9254396d732414459a4029215
        has 2,455,196 variables and 11,798,572 clauses and has never been started. No UNSAT, absence, exhaustion, distance-12
        witness, repair, universal distance-11 ceiling, D* narrowing, route promotion, or root promotion is licensed; CIRCDIST.gross
        and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}. The fresh Round-107 independent exact review clears
        the sealed Round-106 iteration-188 invariant-quotient continuation package for proposer-level continuation only. Its
        complete quotient assignment satisfies all 11,798,572 clauses and decodes a legal globally interleaved 511-layer schedule,
        but both independently rebuilt unrestricted direct-360 sectors contain named-weight-10 zero-syndrome nonstabilizer
        physical mechanisms. Thus this candidate is killed, repair is forbidden, and its two collision-free free 72-element
        selector orbits supply positive evidence only. The exact fresh/unstarted iteration-189 frontier has 517,140 blocks
        and 24,300 selectors, source sha256:b3bdfbe8924490da1e20230ff856515d13173966bc4170c6078b7aab9e36558b, semantic sha256:e8b17eac5c55f1b1c32fb84972dcc2c52ce259c99a65200c8ed7bc046c811eb4,
        base sha256:f5ccbe6aa4c0a0df5940cd979809003182416900e76a6cc6e3755e493cc6b178, and quotient sha256:3ece12a1ea0ee6502982fecfcaf75debae985ea2ddff93ea3b875552c0714df7.
        There is no Gross UNSAT, absence, exhaustion, distance-12 witness, universal distance-11 ceiling, D* narrowing, route
        promotion, or root promotion; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}. The fresh
        Round-109 independent exact review clears the sealed Round-108 iteration-189 invariant-quotient continuation package
        for proposer-level continuation only. Its complete quotient assignment satisfies all 11,816,927 clauses and decodes
        a legal globally interleaved 448-layer schedule, but both independently rebuilt complete unrestricted direct-360 sectors
        contain named-weight-10 zero-syndrome nonstabilizer physical mechanisms. Thus this candidate is killed, repair is
        forbidden, and its two collision-free free 72-element selector orbits supply positive evidence only. The exact fresh/unstarted
        iteration-190 frontier has 517,140 blocks and 24,444 selectors, source sha256:5231e7f5b4cd2a74390a5d137b9927276ce73829dc599ddc064ab8f2c94a2d2e,
        semantic sha256:76881a021258e6fda565ecfe0ad61c1fe0e6f6a97a418ea806c6d3193b692c00, base sha256:e3ec0d0b146fc4ade428052d1a14737ffade9974dfc37dd79fa8411841d45fc8,
        and quotient sha256:12f2fe58f4bfcaff19d543cdb60411f1659e86c8b4f16f599a2d1679aeeca767. There is no Gross UNSAT, absence,
        exhaustion, distance-12 witness, universal distance-11 ceiling, D* narrowing, route promotion, or root promotion;
        CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
      basis:
        runs:
        - path: circdist/artifacts/circdist_dstar_hunt2_20260823.md
          kind: run
          scope: 'Stage-2 certification attempt (logs: artifacts/logs_circdist_dstar_hunt2_20260823/, 45 SHA-summed entries;
            predecessor logs re-verified 23/23): no SAT solver on the machine, so an exact combinatorial exhaustion of the
            |V| = 12 stratum (complete 1884-logical pool per sector, j <= 4 contributing checks) on three proved reductions
            plus Bound 1; second-source validation — the same code returns 0 configurations for the published candidate M_cand
            (agreeing with its 990 all-UNSAT solver sub-queries) on both labelling readings, d = 12 on singleton-only columns,
            144/360 canonical family reproduction.'
          result: Candidate d_eff <= 10 both sectors (144 witnesses, 144/144 assertion checks); every X-memory weight-10 witness
            has exact repair = 1 hence candidate d_circ <= 11; 297/297 interleaved re-timings of M_cand repair-0 via horizontal
            hooks; Lemma D (d_eff order-only dependence) established at proposer level.
        - path: circdist/artifacts/circdist_dstar_hunt1_20260823.md
          kind: run
          scope: 'Stage-1 hunt (logs: artifacts/logs_circdist_dstar_hunt1_20260823/, 23 SHA-summed entries): LIFT-prime/repair
            decider built from scratch and validated on ground truth (Steane 21/21 criterion + 21/21 sandwich agreements vs
            brute-force multi-round DEM; independently reproduces the known Steane gap, 1/68 random schedules); gross rebuilt
            (overlaps {0:4536, 2:648}, k = 12, 1884 logicals/sector, 1080/1080 pair coverage); four families swept.'
          result: 'Non-interleaved 4/4 repair-0; check-serial 60 schedules repair-0 PROVED class-wide; TI legal+MC 400 sampled
            (1.15 percent acceptance), 0 gap survivors in both sectors; coset-TI 0/60000 pass MC; 3-colour-tiled annealed:
            ONE candidate with zero repair-0 canonical gamma in both sectors.'
frontier:
  task-003:
    task: 'Remaining after wave 36 closed links 3/4 and verified SBB Thm 1: (c) optionally LRAT-check a certificate sample
      (the sole remaining verification-depth item on the route); and fold the two-codes-one-per-sector precision into the
      implication text when next re-binding it.'
    kind: task
    since: '2026-08-20'
  dstar-residual:
    task: Continue only from the independently reviewed sealed fresh/unstarted iteration 190 full-invariant state. The exact
      translation-closed registry contains 517,140 unique sound block semantics (1,440 unary, 900 round-62, 500,868 generalized,
      and 13,932 dynamic) and 24,444 invariant exact EFSSC selectors (12,780 Xerr and 11,664 Zerr). Bind source-file sha256:5231e7f5b4cd2a74390a5d137b9927276ce73829dc599ddc064ab8f2c94a2d2e,
      semantic-source sha256:76881a021258e6fda565ecfe0ad61c1fe0e6f6a97a418ea806c6d3193b692c00, state-file sha256:af31130cbb6f0f80d2b37b3ba27d1b1d86fa5b18a80c1e02aa3de02504863be4,
      and selector-state sha256:02b71bfed57c070359b77d69514397a021734aec7563057c02eeff29f4b6cdbd before use. Its deterministic
      base formula has 545,982 source assertions, 1,850,757 variables, 6,920,296 clauses and CNF sha256:e3ec0d0b146fc4ade428052d1a14737ffade9974dfc37dd79fa8411841d45fc8.
      The 71-root lex quotient adds exactly 613,440 unique-definition variables and 4,907,591 clauses, yielding 2,464,197
      variables, 11,827,887 clauses, 546,053 assertions and CNF sha256:12f2fe58f4bfcaff19d543cdb60411f1659e86c8b4f16f599a2d1679aeeca767.
      It is equisatisfiable with this full invariant base only. It has not been launched; its base formula directory contains
      exactly assertion_map.jsonl, definitions.json.gz, encoding_check.json, metadata.json and outer.cnf, and its quotient
      directory contains exactly independent_check.json, metadata.json, outer.cnf, translation_roots.jsonl and translation_trace.json.gz,
      with no solver log, model, assignment, DRAT, LRAT or other proof artifact. The iteration-189 quotient is SAT and its
      exact schedule is killed in both complete unrestricted direct sectors by independently checked named-weight-10 physical
      mechanisms. Their two collision-free free 72-element selector orbits are the final atomic addition already represented
      in iteration 190. Repair was not entered because both direct sectors are SAT. Solve the iteration-190 quotient proof-first
      with proof output enabled from byte zero and strict serialization. For SAT, retain the complete assignment, verify every
      DIMACS clause and frozen legal-schedule condition, rebuild both complete unrestricted 360-column sectors, and add only
      independently physically replayed full selector orbits after bilateral adjudication. For UNSAT, retain a complete DRAT
      proof, independently accept it, generate LRAT, independently accept LRAT, and invoke only the theorem licensed by the
      invariant installed exclusions. UNKNOWN or SAT proof-side streams are non-certificates. Enter repair only after both
      complete direct sectors independently check UNSAT. Preserve the frozen S_Gross geometry, strict solver serialization,
      MC0, terminal residual semantics, both CSS sectors, the full 72-element action, exact tuple identity, integer- and memory-safe
      streaming, atomic state-last transitions, and every earlier exclusion against morphing, Circ-Preserve substitutions,
      alternate conflict models, exploratory pair clauses, retroactive or schedule-globalized cuts, stale compressor provenance,
      mixed-sector XOR, support-weight substitution, and fixed-basis/full-span globalization. Use the sealed conventional
      replay.sh interface. Keep CIRCDIST.gross and gap-via-lift CONJECTURED and D*_Gross in {11,12}; this reviewed continuation
      supplies no Gross UNSAT, absence, exhaustion, distance-12 witness, universal distance-11 ceiling, D* narrowing, route
      promotion, or root promotion.
    kind: task
    since: '2026-09-01'
events:
  gross-whole-registry-round81-review-2026-08-30:
    date: '2026-08-30'
    type: review-completed
    summary: Fresh independent exact review cleared the sealed round-80 whole-registry package as proposer-level evidence
      and licensed strict fresh-process continuation from unstarted iteration 102 with 14,484 blocks. Non-importing clean-room
      checkers rebuilt 96 source raw mechanisms, 138 complete catalogs, exact pair/star synthesis and classification, twelve
      legal outer SAT schedules, twenty-four complete direct SAT/raw replays and 120 final raw mechanisms. They actually visited
      304,704 whole-star and 20,820,216 online/cross literal cells; validated 35,294,400 whole-star and 55,037,740,032 online/cross
      factorized tuples; and independently closed the eight multi-selector GF(2) terms, atomic commits and the state chain
      G=12,820, D=204, registry/raw=120. All ten FIX-2 incidents and rollback boundaries pass audit. No absence, repair, exhaustion,
      D* narrowing, route change or level change is licensed. Gross remains CONJECTURED with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_whole_registry_round80_20260830
      kind: run
    - path: circdist/reviews/circdist_gross_round80_whole_registry_exact_review_20260830.md
      kind: review
  gross-cross-registry-round79-review-2026-08-30:
    date: '2026-08-30'
    type: review-completed
    summary: Fresh independent exact review cleared the sealed round-78 cross-registry package as proposer-level evidence
      and licensed strict fresh-process continuation from unstarted iteration 90 with 12,235 blocks. Non-importing clean-room
      checkers rebuilt twelve legal outer SAT schedules, twenty-four complete direct SAT/raw replays and 96 raw mechanisms;
      actually visited all 43,834,872 literal selector tuples; validated four factorized exhaustive domains totaling 15,485,313,024
      tuples; and verified classification, dominance, union, zero-domain handling, atomic commits and the state chain G=10,595,
      D=180, registry/raw=96. All synthesis v1--v7 failures, rollback boundaries, proof controls and both rejected seals pass
      audit. One non-load-bearing wording correction limits "permutation" to the encoded legal schedule with allowed parallel
      layers. No absence, repair, exhaustion, D* narrowing, route change or level change is licensed. Gross remains CONJECTURED
      with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_cross_registry_round78_20260829
      kind: run
    - path: circdist/reviews/circdist_gross_round78_cross_registry_exact_review_20260830.md
      kind: review
  gross-online-generalization-round77-review-2026-08-29:
    date: '2026-08-29'
    type: review-completed
    summary: Fresh independent exact review cleared the sealed round-76 positive online-generalization package as proposer-level
      evidence and licensed strict fresh-process continuation from unstarted iteration 78 with 7,359 blocks. Non-importing
      clean-room checkers rebuilt twenty-four legal outer SAT schedules, forty-eight complete direct SAT/raw replays, exact
      classification from 420 candidates to 303 retained terms, every one of 2,637,648 retained pair tuples, two factorized
      exhaustive proofs totaling 55,037,740,032 multi tuples and the state chain G=5,743, D=156, registry=72. One stale pre-adaptation
      compressor provenance row is corrected at review level; final sealed binding is 2,760 bytes / sha256:d4abdf75b066d8a2507d5c010f96c1c1760f36c6d1d242048fb45c5928cb8dde.
      Deletion minimality is limited to candidate relations or fixed selectors. No absence, repair, exhaustion, D* narrowing,
      route change or level change is licensed. Gross remains CONJECTURED with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_online_generalizing_round76_20260829
      kind: run
    - path: circdist/reviews/circdist_gross_round76_online_generalizing_exact_review_20260829.md
      kind: review
  gross-online-generalization-round75-review-2026-08-29:
    date: '2026-08-29'
    type: review-completed
    summary: Fresh independent exact review cleared the sealed round-74 positive online-generalization package as proposer-level
      evidence and licensed strict fresh-process continuation from iteration 54 with 7,008 blocks. Non-importing clean-room
      checkers rebuilt twelve legal outer SAT schedules, twenty-four complete direct SAT/raw replays, exact classification
      from 188 candidates to 134 retained terms, every one of 1,137,096 retained pair tuples, the factorized exhaustive proof
      for 2,985,984 retained multi tuples and the state chain G=5,440, D=108. Two documentation imprecisions are corrected
      at review level, and deletion minimality is limited to candidate relations or fixed selectors. No absence, repair, exhaustion,
      D* narrowing, route change or level change is licensed. Gross remains CONJECTURED with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_online_generalizing_round74_20260829
      kind: run
    - path: circdist/reviews/circdist_gross_round74_online_generalizing_exact_review_20260829.md
      kind: review
  gross-round72-generalization-round73-review-2026-08-29:
    date: '2026-08-29'
    type: review-completed
    summary: Fresh independent exact review cleared the sealed round-72 positive-witness generalization package as proposer-level
      evidence and licensed strict continuation from iteration 42 with 6,850 blocks. A non-importing clean-room checker validated
      314,668,800 pair cells, 32,031,216 retained physical-selector tuples, all 48 source assignments, exact semantic deduplication
      from 696 candidates to 566 retained terms, twelve legal outer schedules and twenty-four complete direct SAT/raw replays.
      Zero truth cells and failed positive completions remain non-load-bearing; no absence, repair, exhaustion, D* narrowing,
      route change or level change is licensed. Gross remains CONJECTURED with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_round71_generalization_round72_20260829
      kind: run
    - path: circdist/reviews/circdist_gross_round72_generalization_exact_review_20260829.md
      kind: review
  gross-cegar-continuation-round71-2026-08-29:
    date: '2026-08-29'
    type: repair-applied
    summary: Linked the sealed round-71 exact CEGAR continuation after dispatcher manifest and full verifier replay, without
      a level change. Iterations 6--29 give 24 legal outer schedules and 48 complete direct-sector SAT assignments, all clause-checked
      and raw-replayed, yielding 48 candidate-exact sound blocks. No sector is UNSAT, no repair is entered and no outer exhaustion
      exists. The exact restart is iteration 30 with 6,260 installed blocks. Gross remains CONJECTURED with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_cegar_continuation_round71_20260829
      kind: run
  gross-block-minimization-round70-review-2026-08-29:
    date: '2026-08-29'
    type: review-completed
    summary: Fresh independent exact review cleared the sealed round-69 positive-witness library as proposer-level evidence
      and licensed strict continuation from iteration 6 with 6,212 blocks. A non-importing clean-room checker validated all
      15,552,000 pair cells, 4,740 sound antecedents over 56,539,296 covered incidences, 3,368 raw mechanisms, six legal outer
      schedules and twelve complete direct-360 SAT/raw replays. The 2,704 negative weight-14 observations remain non-load-bearing;
      no absence, repair, outer exhaustion, D* narrowing, route change or level change is licensed. Gross remains CONJECTURED
      with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_block_minimization_round69_20260829
      kind: run
    - path: circdist/reviews/circdist_gross_block_minimization_exact_review_20260829.md
      kind: review
  gross-direct360-round68-2026-08-29:
    date: '2026-08-29'
    type: repair-applied
    summary: Linked the sealed round-68 complete direct-360 package after dispatcher manifest and full verifier replay, without
      a level change. One unrestricted clause-saturated candidate has SAT direct queries in both sectors and raw-verified
      weight-10 Xerr and weight-8 Zerr mechanisms; five further exact candidates are also killed in both sectors. Twelve new
      sound exact blocks raise the retained total to 1,472. The independent DRAT/LRAT toolchain accepts valid controls and
      rejects truncated proofs, but no candidate-specific UNSAT, repair result or outer exhaustion exists. Gross remains CONJECTURED
      with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_direct360_proof_round68_20260829
      kind: run
  gross-pattern-cegar-round63-2026-08-28:
    date: '2026-08-28'
    type: repair-applied
    summary: Linked the sealed round-63 pattern-CEGAR package after dispatcher replay, without a level change. The package
      proves 1,440 globally valid five-atom single-residual order clauses by exhaustive local-order checks and deletion controls.
      Its 15,874 pair-pattern clauses remain exploratory due to retention gaps, and it contains zero checked proof objects.
      Gross remains CONJECTURED with D*_Gross in {11,12}; the frontier now requires a proof-logged and independently checked
      direct-360 sector UNSAT on one exact outer candidate.
    sources:
    - path: circdist/artifacts/circdist_gross_pattern_cegar_round63_20260828
      kind: run
  gross-integrated-cegar-round62-2026-08-28:
    date: '2026-08-28'
    type: repair-applied
    summary: Linked the sealed round-62 integrated CEGAR package after independent manifest and replay verification, without
      a level change. The exact outer model produced 20 legal MC-valid interleaved schedules; each is killed by a raw-verified
      Xerr weight-10 mechanism, yielding 20 sound order-region blocks. No UNSAT or outer exhaustion exists, so Gross remains
      CONJECTURED with D*_Gross in {11,12}; the frontier now targets proof-producing residual-support-pattern clauses and
      an incremental checked backend.
    sources:
    - path: circdist/artifacts/circdist_gross_cegar_round62_20260828
      kind: run
  gross-dstar-hunt3-screen-repair-2026-08-28:
    date: '2026-08-28'
    type: repair-applied
    summary: Round-61 proposer audit linked without a level change. It refutes the four-positive-shape and bounded-|V|=12/at-most-four-check
      screens by explicit legal interleaved counterexamples, records the hunt2 distinct-check recursion defect, preserves
      the earlier candidate kill through separately raw-verified witnesses, and replaces the stale filter-based frontier with
      the exact integrated CEGAR residual. Gross remains CONJECTURED with D*_Gross in {11,12}; every new theorem in the report
      remains proposer-level.
    sources:
    - path: circdist/artifacts/circdist_dstar_hunt3_20260828.md
      kind: run
  gross-morphing-scope-ruling-2026-08-26:
    date: '2026-08-26'
    type: repair-applied
    summary: Fresh primary-source audit corrected the prior second-hand morphing gloss. Shaw-Terhal's original Gross [[144,12,12]]
      is only a mid-cycle input whose end-cycle code is [[72,12,6]]; their distance-12 endpoint is a different weight-9 [[144,12,12]]
      “second gross” code derived from [[288,12,18]], and its reported morphing circuit distance is only the BP-OSD upper
      bound <=12. The construction is outside frozen S_Gross. Frontier task-002 closes negative; the root stays CONJECTURED
      with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_morphing_scope_ruling_20260826.md
      kind: text
  gross-efssc-round87-review-2026-08-30:
    date: '2026-08-30'
    type: review-completed
    summary: Fresh independent Round-87 review cleared the sealed Round-86 exact fixed-selector semantic-cut package for proposer-level
      continuation only. It independently rederived the EFSSC iff theorem and canonical/physical stabilizer equivalence; checked
      134 source truths, fourteen selector domains (nine strict expansions, five equal, maximum factor 320), seven legal MC0
      globally interleaved schedules, fourteen unrestricted weight-10 mechanisms, atomic transitions, exact iteration-109
      state, and 0/19,016 structural formula differences. No UNSAT, exhaustion, distance-12 witness, universal distance-11
      ceiling, route change, inheritance, or level change is licensed. CIRCDIST.gross and gap-via-lift remain CONJECTURED
      with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_efssc_round86_20260830
      kind: run
    - path: circdist/reviews/circdist_gross_efssc_exact_review_round87_20260830.md
      kind: review
  gross-efssc-frontier-iteration109-2026-08-30:
    date: '2026-08-30'
    type: repair-applied
    summary: 'Canonical frontier bookkeeping synchronized to the reviewed fresh/unstarted iteration 109 state: 14,484 inherited
      sound order blocks, 134 EFSSC selectors, selector-state sha256:9be75eba643ac167d5c51497ca8e5cd23eb1656f803a49cbd8e7f1285b004113
      and preserved unsolved 19,016-assertion formula sha256:94d404da1777ef108a2a508dc55ca0f3fda68bc489482a00337d9acb7317ac4d.
      This records continuation state only and leaves root/route status and D* residual unchanged.'
    sources:
    - path: circdist/artifacts/circdist_gross_efssc_round86_20260830
      kind: run
    - path: circdist/reviews/circdist_gross_efssc_exact_review_round87_20260830.md
      kind: review
  gross-proof-outer-round89-review-2026-08-30:
    date: '2026-08-30'
    type: review-completed
    summary: 'Fresh independent Round-89 review clears the sealed Round-88 finite-outer package at proposer level and licenses
      continuation only from fresh/unstarted iteration 112: 14,484 inherited order blocks, 140 exact EFSSC selectors, selector-state
      sha256:a0364547f846fd68ace7cdba85d89c0f8e6326145243fb0fea7ff543420994cb, and checked-unsolved CNF sha256:a8b917845427a0f746e72200a9a58eb5fac86d5e3c845eeaae69082038c86594
      (398,488 variables; 1,330,104 clauses; 19,022 source assertions). Iterations 109--111 and all six unrestricted direct
      sectors are SAT; their exact physical mechanisms license only six candidate-domain cuts. No Gross UNSAT, direct absence,
      repair, exhaustion, D* narrowing, route change or level change is licensed; CIRCDIST.gross remains CONJECTURED with
      D*_Gross in {11,12}.'
    sources:
    - path: circdist/artifacts/circdist_gross_proof_outer_round88_20260830
      kind: run
    - path: circdist/reviews/circdist_gross_proof_outer_exact_review_round89_20260830.md
      kind: review
  gross-proof-outer-round91-review-2026-08-30:
    date: '2026-08-30'
    type: review-completed
    summary: 'Fresh independent Round-91 review clears the sealed Round-90 finite-outer package at proposer level and licenses
      continuation only from fresh/unstarted iteration 124: 14,484 inherited order blocks, 164 exact EFSSC selectors, selector-state
      sha256:854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3, and checked-unsolved CNF sha256:2dd07d33ff0b29c1f06a7452c3b1c7ca9b6df950e819046f8a712dacb0dd7e5a
      (401,040 variables; 1,345,190 clauses; 19,046 source assertions). Iterations 112--123 and all twenty-four unrestricted
      direct sectors are SAT; their exact physical mechanisms, including two weight-9 cases, license only twenty-four candidate-domain
      cuts. No Gross UNSAT, direct absence, repair, exhaustion, D* narrowing, route change, or level change is licensed; CIRCDIST.gross
      remains CONJECTURED with D*_Gross in {11,12}.'
    sources:
    - path: circdist/artifacts/circdist_gross_proof_outer_round90_20260830
      kind: run
    - path: circdist/reviews/circdist_gross_proof_outer_exact_review_round91_20260830.md
      kind: review
  gross-proof-outer-round93-review-2026-08-30:
    date: '2026-08-30'
    type: review-completed
    summary: 'Fresh independent Round-93 review clears the sealed Round-92 weight-9 synthesis and finite-outer package at
      proposer level and licenses continuation only from fresh/unstarted iteration 136: 14,484 inherited order blocks, 232
      exact EFSSC selectors, selector-state sha256:1692d905120d2dcf51b949ce4a70ed4b8f1b270c2d07a1ddbf5813d20d80fa81, and checked-unsolved
      CNF sha256:289acad6be1068d63369511e9c95b0b1df146471bf05a1e4128758508612b64e (406,656 variables; 1,372,232 clauses; 19,114
      source assertions). Phase A adds 44 exact ordinary selectors and zero relaxed cubes; iterations 124--135 and all twenty-four
      direct sectors are SAT, with two weight-9 mechanisms. No Gross UNSAT, direct absence, repair, exhaustion, D* narrowing,
      route change, or level change is licensed; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
    sources:
    - path: circdist/artifacts/circdist_gross_proof_outer_round92_20260830
      kind: run
    - path: circdist/reviews/circdist_gross_proof_outer_weight9_exact_review_round93_20260830.md
      kind: review
  gross-proof-outer-round95-review-2026-08-30:
    date: '2026-08-30'
    type: review-completed
    summary: 'Fresh independent Round-95 review clears the sealed Round-94 finite-outer and same-sector order-3 GF(2) package
      at proposer level and licenses continuation only from fresh/unstarted iteration 148: 14,484 inherited order blocks,
      256 exact EFSSC selectors, selector-state sha256:9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f, and
      checked-unsolved CNF sha256:397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4 (409,157 variables; 1,385,059
      clauses; 19,138 source assertions). Iterations 136--147 and all twenty-four unrestricted direct sectors are SAT; their
      physically replayed mechanisms, including iteration-138 Xerr at weight 9, license only twenty-four candidate-domain
      cuts. The exhaustive 527,684-triple investigation retains zero terms and proves a no-go only on its exact declared domain.
      No Gross UNSAT, direct absence, repair, exhaustion, D* narrowing, route change, or level change is licensed; CIRCDIST.gross
      and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
    sources:
    - path: circdist/artifacts/circdist_gross_proof_outer_round94_20260830
      kind: run
    - path: circdist/reviews/circdist_gross_proof_outer_round94_exact_review_round95_20260830.md
      kind: review
  gross-proof-outer-round97-review-2026-08-31:
    date: '2026-08-31'
    type: review-completed
    summary: 'Fresh independent Round-97 review clears the sealed Round-96 finite-outer and same-sector order-4 GF(2) package
      at proposer level and licenses continuation only from fresh/unstarted iteration 160: 14,484 inherited order blocks,
      280 exact EFSSC selectors, selector-state sha256:ad3cf364dd9224c14ffb55046ba3dc8eb80035b1eaf997f1d7a5691297ad62a3, and
      checked-unsolved CNF sha256:aa18d2857ed5a7aefacd33bf4fbd42fded914393e123a87f00e84e4920e39d59 (411,526 variables; 1,396,722
      clauses; 19,162 source assertions). Iterations 148--159 and all twenty-four unrestricted direct sectors are SAT; their
      physically replayed mechanisms, including iteration-148 and iteration-152 Zerr at weight 9, license only twenty-four
      candidate-domain cuts. The exhaustive 15,254,626-quadruple investigation retains zero novel terms and proves a no-go
      only on its exact declared same-sector order-4 domain. No Gross UNSAT, direct absence, repair, exhaustion, D* narrowing,
      route change, or level change is licensed; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
    sources:
    - path: circdist/artifacts/circdist_gross_proof_outer_round96_20260831
      kind: run
    - path: circdist/reviews/circdist_gross_proof_outer_round96_exact_review_round97_20260831.md
      kind: review
  gross-proof-outer-round99-review-2026-08-31:
    date: '2026-08-31'
    type: review-completed
    summary: 'Fresh independent Round-99 review clears the sealed Round-98 finite-outer and same-sector order-5 GF(2) package
      at proposer level and licenses continuation only from fresh/unstarted iteration 172: 14,484 inherited order blocks,
      304 exact EFSSC selectors, selector-state sha256:a5c64ae41f474844ecd3ac41829331f54d419a81573e4f0e11528db0b49e25d1, and
      checked-unsolved CNF sha256:f86b8db36af1df3877ca1d9dbafb171b6173ddc8b6c2f045a808dd6c71f98342 (413,646 variables; 1,406,245
      clauses; 19,186 source assertions). Iterations 160--171 and all twenty-four unrestricted direct sectors are SAT; their
      physically replayed mechanisms, including iteration-161 Xerr at weight 9, license only twenty-four candidate-domain
      cuts. The exhaustive 351,359,546-quintuple investigation reconstructs 40,153 unique eligible named-weight-1..10 results,
      finds zero canonical-syndrome-zero results in either sector, retains zero selectors, and proves a no-go only on its
      exact declared same-sector order-5 domain. No Gross UNSAT, direct absence, repair, exhaustion, D* narrowing, route change,
      or level change is licensed; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
    sources:
    - path: circdist/artifacts/circdist_gross_proof_outer_round98_20260831
      kind: run
    - path: circdist/reviews/circdist_gross_proof_outer_round98_exact_review_round99_20260831.md
      kind: review
  gross-proof-outer-round101-review-2026-09-01:
    date: '2026-09-01'
    type: review-completed
    summary: 'Fresh independent Round-101 review clears the sealed Round-100 finite-outer, exact same-sector order-6, and
      fixed-basis full-span package at proposer level and licenses continuation only from fresh/unstarted iteration 184: 14,484
      inherited order blocks, 328 exact EFSSC selectors, selector-state sha256:7296aa70690e01852519b78826b173af35998cec0e9c124c46ea30101dd0777d,
      and checked-unsolved CNF sha256:2b0030fd15b0ef8154e2dbc37508e03481f11d8c876c4fe59e6541cb3bfacd62 (415,793 variables;
      1,416,404 clauses; 19,210 source assertions). Iterations 172--183 and all twenty-four unrestricted direct sectors are
      SAT; their physically replayed mechanisms license only twenty-four candidate-domain cuts. Exact order-6 coverage retains
      zero selectors. The X/Z all-orders span UNSAT results cover only the exact fixed bases, installed-mask quotient and
      post-iteration-136 schedule; the mixed-sector theorem is only a fixed-direct-domain component reduction. A non-load-bearing
      synthesis sentence is corrected: Z has 315 nonseparated doubleton triple-key groups, not an all-singleton histogram.
      All F001--F012 records, 211 retained PID records, the immutable 204-record science census, 38 strictly nonoverlapping
      solver intervals, deletion of 36 SAT non-certificate streams, FIX-2, and a fresh strict-serial 127-direct plus 18-nested
      sealed replay pass review. No Gross UNSAT, direct absence, repair, exhaustion, D* narrowing, route change, or level
      change is licensed; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
    sources:
    - path: circdist/artifacts/circdist_gross_proof_outer_round100_20260831
      kind: run
    - path: circdist/reviews/circdist_gross_proof_outer_round100_exact_review_round101_20260831.md
      kind: review
  gross-global-closure-round103-review-2026-09-01:
    date: '2026-09-01'
    type: review-completed
    summary: 'Fresh independent Round-103 review clears the sealed Round-102 global-translation package at proposer level
      and licenses continuation only from fresh/unstarted iteration 187: 517,140 invariant block semantics, 24,012 invariant
      exact selectors, selector-state sha256:7667fc8230b67224b1895180764680c5000dcef34b3c67352f904e5998e8879b, checked-unsolved
      base CNF sha256:7f66b46643b6b10cce57358e4e66f7e95cdc1bfe52ee14f77884c56ddd5d5eab (545,550 assertions; 1,838,894 variables;
      6,882,039 clauses), and checked-unsolved 71-root quotient sha256:e415b4c2c5b4923a47348a06ea9ebb06bbc85cea2c9c32bd3a9b25a1ce198234
      (2,452,334 variables; 11,789,630 clauses). The exact Z_12 x Z_6 action, orbit closure and corrected quotient are sound;
      the corrected iteration-186 quotient and both complete direct sectors are SAT. The first quotient over a non-invariant
      registry is retracted as global evidence, with a concrete lex-translate/cut counterexample; only its independently replayed
      SAT schedule and direct translation orbits survive as positive evidence. All F001--F013 records, two bounded UNKNOWN
      non-certificates, compressed streams, process/proof/repository controls, and a fresh strict-serial 13-child source-entry
      replay pass review. The missing root replay.sh is a real nonblocking packaging/interface defect. No Gross UNSAT, direct
      absence, repair, exhaustion, D* narrowing, route change, or level change is licensed; CIRCDIST.gross and gap-via-lift
      remain CONJECTURED with D*_Gross in {11,12}.'
    sources:
    - path: circdist/artifacts/circdist_gross_global_closure_round102_20260901
      kind: run
    - path: circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md
      kind: review
  gross-iter187-invariant-continuation-round105-review-2026-09-01:
    date: '2026-09-01'
    type: review-completed
    summary: 'Fresh independent Round-105 review clears the sealed Round-104 iteration-187 invariant-continuation package
      at proposer level and licenses continuation only from fresh/unstarted iteration 188: 517,140 invariant block semantics,
      24,156 invariant exact selectors, selector-state sha256:90999b94525d7e4d23c7e62d4caf057a061baa461c56941057043b0ba3e22e99,
      checked-unstarted base CNF sha256:051dbece97d9cd94a69de7bff644dbb31b35076d0c43558b5408d9f3cc86b257 (545,694 assertions;
      1,841,756 variables; 6,890,981 clauses), and checked-unstarted 71-root quotient sha256:29b16602aa5cdf0e4207271cb50045454ea0aba9254396d732414459a4029215
      (2,455,196 variables; 11,798,572 clauses). The iteration-187 quotient and both complete unrestricted direct sectors
      are SAT; the legal candidate has weight-10 Xerr and Zerr physical mechanisms and is not a distance-12 witness. Both
      72-element selector orbits are collision-free and the full registry remains invariant. All three SAT streams are non-certificate
      traces. All nine disclosed failures, 31 PID records, three nonoverlapping solver intervals, proof controls, and a fresh
      strict-serial 14-child replay pass review. No Gross UNSAT, direct absence, repair, exhaustion, distance-12 witness,
      universal distance-11 ceiling, D* narrowing, route change, or level change is licensed; CIRCDIST.gross and gap-via-lift
      remain CONJECTURED with D*_Gross in {11,12}.'
    sources:
    - path: circdist/artifacts/circdist_gross_iter187_invariant_continuation_round104_20260901
      kind: run
    - path: circdist/reviews/circdist_gross_iter187_invariant_continuation_round104_exact_review_round105_20260901.md
      kind: review
  gross-iter188-invariant-continuation-round107-review-2026-09-01:
    date: '2026-09-01'
    type: review-completed
    summary: 'Fresh independent Round-107 review clears the sealed Round-106 iteration-188 full-invariant continuation package
      at proposer level and licenses continuation only from fresh/unstarted iteration 189: 517,140 invariant block semantics,
      24,300 invariant exact selectors, selector-state sha256:8e4db1fbf08e24b81995a6ac1b25f791480edebd06e560442e2ca49a5ad5cefa,
      checked-unstarted base CNF sha256:f5ccbe6aa4c0a0df5940cd979809003182416900e76a6cc6e3755e493cc6b178 (545,838 assertions;
      1,847,301 variables; 6,909,336 clauses), and checked-unstarted 71-root quotient sha256:3ece12a1ea0ee6502982fecfcaf75debae985ea2ddff93ea3b875552c0714df7
      (2,460,741 variables; 11,816,927 clauses). The iteration-188 quotient and both complete unrestricted direct sectors
      are SAT; the legal candidate has named-weight-10 Xerr and Zerr physical mechanisms and is not a distance-12 witness.
      Both free 72-element selector orbits are collision-free and the full registry remains invariant. All three solver streams
      are SAT traces. All fourteen disclosed failure classes, 37 PID records, three nonoverlapping solver intervals, proof
      controls, and a fresh strict-serial 13-child sealed replay pass review. No Gross UNSAT, direct absence, repair, exhaustion,
      distance-12 witness, universal distance-11 ceiling, D* narrowing, route change, or level change is licensed; CIRCDIST.gross
      and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
    sources:
    - path: circdist/artifacts/circdist_gross_iter188_invariant_quotient_continuation_round106_20260901
      kind: run
    - path: circdist/reviews/circdist_gross_iter188_invariant_continuation_round106_exact_review_round107_20260901.md
      kind: review
  gross-iter189-invariant-continuation-round109-review-2026-09-02:
    date: '2026-09-02'
    type: review-completed
    summary: 'Fresh independent Round-109 review clears the sealed Round-108 iteration-189 full-invariant continuation package
      at proposer level and licenses continuation only from fresh/unstarted iteration 190: 517,140 invariant block semantics,
      24,444 invariant exact selectors, selector-state sha256:02b71bfed57c070359b77d69514397a021734aec7563057c02eeff29f4b6cdbd,
      checked-unstarted base CNF sha256:e3ec0d0b146fc4ade428052d1a14737ffade9974dfc37dd79fa8411841d45fc8 (545,982 assertions;
      1,850,757 variables; 6,920,296 clauses), and checked-unstarted 71-root quotient sha256:12f2fe58f4bfcaff19d543cdb60411f1659e86c8b4f16f599a2d1679aeeca767
      (546,053 assertions; 2,464,197 variables; 11,827,887 clauses). The iteration-189 quotient and both complete unrestricted
      direct sectors are SAT; the legal candidate has named-weight-10 Xerr and Zerr physical mechanisms and is not a distance-12
      witness. Both free 72-element selector orbits are collision-free and the full registry remains invariant. All three
      solver streams are SAT traces. All four disclosed failure classes, 37 PID records, three nonoverlapping solver intervals,
      proof controls, and a fresh strict-serial 18-child sealed replay pass review. No Gross UNSAT, direct absence, repair,
      exhaustion, distance-12 witness, universal distance-11 ceiling, D* narrowing, route change, or level change is licensed;
      CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
    sources:
    - path: circdist/artifacts/circdist_gross_iter189_invariant_quotient_continuation_round108_20260901
      kind: run
    - path: circdist/reviews/circdist_gross_iter189_invariant_continuation_round108_exact_review_round109_20260902.md
      kind: review
```
<!-- END COMPLETE CIRCDIST.gross.yaml REPLACEMENT -->

## 17. Durable boundary

This review is the sole permitted repository write. It is assembled and checked in scratch, then moved once to `circdist/reviews/circdist_gross_iter189_invariant_continuation_round108_exact_review_round109_20260902.md`. The live scheduler, canonical node, predecessor review, and sealed package are rehashed after installation. Final unique extraction, whitespace checks, zero-survivor census, durable-file count, review SHA-256/bytes/LF, cleanup, and no-commit/no-push state are recorded externally and reported to the dispatcher.
