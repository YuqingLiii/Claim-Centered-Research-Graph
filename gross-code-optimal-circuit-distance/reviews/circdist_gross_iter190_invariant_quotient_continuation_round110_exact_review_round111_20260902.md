# CIRCDIST.gross Round111 fresh independent exact review of the sealed Round110 iteration-190 continuation

**Date:** 2026-09-02

**Reviewer role:** sole fresh independent Round111 reviewer

**Reviewed package:** `circdist/artifacts/circdist_gross_iter190_invariant_quotient_continuation_round110_20260902`

**Verdict:** **CLEAR-PROPOSER-LEVEL-CONTINUATION**

## 1. Verdict and licensed scope

The sealed Round110 package is independently supported at proposer level. The reviewed iteration-190 full-invariant 71-root quotient is **SAT**: the retained complete assignment assigns each of 2,464,197 variables exactly once and satisfies every one of 11,827,887 clauses. Its decoded 864-edge frozen schedule is legal, MC-valid, globally X/Z-interleaved, and uses exactly 477 layers. Both complete unrestricted direct-360 queries are **SAT**. Independent formula reconstruction and exact canonical and physical replay establish a named-weight-10, zero-syndrome, nonstabilizer mechanism in Xerr and another in Zerr. Therefore this particular schedule is not a distance-12 witness and the package correctly did not enter repair.

The two mechanism stabilizers are trivial under the exact `Z_12 x Z_6` action, so each contributes a complete free 72-element selector orbit. All 144 additions are collision-free. The registry lineage is exactly `24,444 -> 24,588`; all 517,140 block semantics and all 24,588 selectors remain invariant. The exact continuation is fresh, checked, and unstarted iteration 191.

This licenses reuse of the reviewed evidence and strict continuation only. Root branch A, a certified legal distance-12 schedule, remains **not proved**. Root branch B, a universal distance-at-most-11 theorem, remains **not proved**. No accepted Gross DRAT/LRAT proof exists. `CIRCDIST.gross` and `gap-via-lift` remain `CONJECTURED`; the smallest honest residual remains exactly `D*_Gross in {11,12}`. I license no root or route promotion, interval narrowing, absence theorem, exhaustion theorem, repair entry, or inheritance beyond the frozen model.

I had no contact with the Round110 proposer, spawned no subagents, launched no iteration-191 SAT solve, made no commit or push, and modified no canonical node, scheduler, protocol, prior review, or sealed package. Reasoning is exposed below as definitions, reconstruction algorithms, counts, witness objects, hashes, controls, counterchecks, and explicit limitations rather than hidden chain-of-thought.

## 2. Live governance and exact bindings

I read the handoff at `research/circdist/notes/HANDOFF_20260823.md`, the scheduler, canonical Gross node, Round109 review, and package-local bindings before scientific work.

| object | independently observed SHA-256 | bytes | LF | disposition |
|---|---:|---:|---:|---|
| `operations/circdist/SCHEDULER.yaml` | `e64f830999e4a172cbb2275a8010446a2f9e24c31ef40f95766d424d09bbc9b5` | 312,309 | — | Round111 authorized/pending at 136/137; sole winner binding matches |
| canonical `CIRCDIST.gross.yaml` | `7302da9e4726bd2c62a9e335d75d6a9098780888ed91a87a66d503b5938f607b` | 121,740 | 1,278 | exact predecessor; root and route `CONJECTURED` |
| Round109 review | `0d31152bc03ca8066a7ffeaf885730b51ff2c55a3634819fc68d9fcbcd26dd82` | 156,134 | 1,519 | exact prior-review binding |
| package `REPORT.md` | `12b051a765520280a22748dc515ae6edc5f0a6260b0b6fb93b52b14bdacf11c4` | 7,952 | 63 | exact |
| package `RESULT.json` | `dd3c469cf4a7c1ffb09184ba6ced480b4fe11a16342f13d1bd7e5e112aace228` | 17,117 | 530 | exact |
| package `PROCESS_FIX2_LEDGER.json` | `342ec4a56e16f46e944ae9d83858f104585a1a80843f7124b1f35d307b7e807a` | 74,903 | 1,516 | exact |
| package `FAILURE_LEDGER.md` | `a8e3fbcd3e45504f5c0633fe3e77666b11178d61837453a6a548f3ee155263a7` | 6,333 | 41 | exact |
| package `FRESH_FRONTIER.json` | `a55ddf91f745f2ac27311aad80b0259ba5d622ae785624126b111bb4eaa80a12` | 1,817 | 50 | exact |
| package `INPUT_BINDINGS.json` | `bf1a2ed1d5b93e146aaf21cc411137de4ab9a78ed22d6143ccb0415a886f3f91` | 8,508 | 171 | exact |

The package-local scheduler binding is the proposer-start state, SHA-256 `beefafeee1608dda1eadfe0e82b920f7148bd2dfc12e93c52c6b48ff69e74aed`; later scheduler-only settlement and Round111 authorization explain the live scheduler difference. The package canonical binding and `PROPOSED_CIRCDIST.gross.yaml` are each byte-identical to the live predecessor, SHA-256 `7302…607b`. Thus the proposer did not preinstall a canonical conclusion.

The dispatcher replay at `/private/tmp/circdist-round110-independent-replay-root-20260902T0351.json`, SHA-256 `e5909e742f713924669cfaa84447f83c1d885afc43ee2f7f81f474ae2e32f2a0`, 54,417 bytes / 899 LF, and seal verification SHA-256 `4adca3bd0b6c8404b3f713d54a1df44de92ba4ad9ec81811ae3cc657a32a89da` were treated only as corroboration.

## 3. Seal, exclusions, inventory, and immutability attack

I walked the installed package without following links and independently hashed every regular file. The package has exactly 480 regular files, 43 directories, 523 filesystem entries, zero symlinks, zero other objects, and zero entries with any write bit. Modes are exactly 304 entries at `0444` and 219 entries at `0555`. Physical regular-file bytes total 4,078,354,588.

| sealed index | SHA-256 | bytes | rows | independently recomputed membership |
|---|---:|---:|---:|---|
| `SHA256SUMS.txt` | `8ce014a0bc1b4273cec02e2af7d9da54691290dd35a82d7c3bfe6c522a031bc5` | 50,835 | 479 | every physical file except this self-referential root manifest |
| `PAYLOAD_SHA256SUMS.txt` | `d36ab5ff07b8f3214f7d4ba1cbf0bcee679fc336ecfa0a099a06f1e1f37b617a` | 50,659 | 477 | exact payload set |
| `FILE_INVENTORY.jsonl` | `fd655231af824f63c814c6a001a42998cf44a07e31e898607432d3820f7e9938` | 72,383 | 478 | every physical file except inventory itself and root manifest |

The inventory-row byte sum is exactly 4,078,231,370, the commissioned substantive-byte count. The payload-row byte sum is 4,078,180,711; root-manifest-row byte sum is 4,078,303,753. Manifest paths are unique, normalized safe relative paths. The payload excludes exactly `FILE_INVENTORY.jsonl`, `PAYLOAD_SHA256SUMS.txt`, and `SHA256SUMS.txt`. The root manifest covers the first two and excludes only itself, so there is no final-root coverage gap.

Before the clean replay I recorded SHA-256, size, LF count, device, inode, mode, uid, gid, link count, `mtime_ns`, `ctime_ns`, and flags for every one of 523 entries. After replay I repeated the full walk. All 480 content identities and all 523 metadata records are exactly equal; there are no missing, extra, or type-changed paths. Both manifests and the inventory retain the hashes and counts above. This detects content substitution, link replacement, and metadata-only replacement around replay. The package root seal remained immutable.

## 4. Fresh installed `replay.sh` execution

I executed the installed root `replay.sh` from the package directory under a clean environment: `PATH=/usr/bin:/bin:/usr/sbin:/sbin`, `LANG=LC_ALL=C.UTF-8`, `PYTHONDONTWRITEBYTECODE=1`, and an external private `TMPDIR`. Wrapper PID 17731 launched foreground replay PID 17734. It returned 0 after 356.188232 seconds, emitted empty stderr, and was reaped without timeout or detachment. Stdout SHA-256 is `56e6bbdcfa42716a0594ad5ded429771e4f32eefe313a33340b4b128c52c27b8`.

The replay result SHA-256 is `1f284c4b3b27c1c507f88e958192f155c1c71063e94a1de6f65f11e25eeef0db`, 54,842 bytes / 899 LF. Its 19 direct children, in recorded order, are PIDs 17738, 17739, 17745, 17750, 17757, 17766, 17771, 17774, 17775, 17776, 17777, 17778, 17779, 17782, 17818, 17842, 17846, 17848, and 17855. Every child returned 0; every interval has exact PID, PPID, argv, cwd, clean environment, start/end, return code, stdout/stderr bytes and hashes; all were foreground, strictly nonoverlapping, reaped, and neither timed out nor detached. The replay reports iteration 191 fresh/unstarted, root not closed, canonical `CONJECTURED`, residual `[11,12]`, and no package mutation.

The fresh replay is corroboration. Sections 5–10 describe an independent standard-library reconstruction that imports no sealed scientific checker.

## 5. Frozen geometry and exact group action

Let `L=12`, `M=6`, group `G=Z_12 x Z_6` of order 72, and `N=144`. Decode a check coordinate `g` by `divmod(g,6)` and define

`add(g,(a,b)) = ((i+a) mod 12)*6 + ((j+b) mod 6)`.

Translate data qubits by `tq(q,d)=add(q,d)` for `q<72` and `72+add(q-72,d)` otherwise. Translate both endpoints of every `sector:check:qubit` edge. Using the frozen offsets `A=((3,0),(0,1),(0,2))` and `B=((0,3),(1,0),(2,0))`, I rebuilt

`X_g = {add(g,a):a in A} union {72+add(g,b):b in B}`

and

`Z_g = {add(g,-b):b in B} union {72+add(g,-a):a in A}`.

Independent results: 72 X checks and 72 Z checks, all weight 6; ranks 66 and 66; 144 data-incidence lists; 864 distinct required edges; 648 size-two X/Z overlaps; and all 5,184 X/Z commutators zero. Every group element permutes checks, qubits, incidences, overlaps, and edges. I checked all `72*72*864 = 4,478,976` edge composition cases, not a generator sample.

## 6. Iteration-190 source, base, quotient, lex controls, and complete SAT assignment

The exact reviewed source is iteration 190 with 517,140 unique block semantics and 24,444 unique selectors:

| object | SHA-256 / exact count |
|---|---|
| source gzip | `5231e7f5b4cd2a74390a5d137b9927276ce73829dc599ddc064ab8f2c94a2d2e` |
| canonical semantic payload | `76881a021258e6fda565ecfe0ad61c1fe0e6f6a97a418ea806c6d3193b692c00` |
| base CNF | `e3ec0d0b146fc4ade428052d1a14737ffade9974dfc37dd79fa8411841d45fc8`; 1,850,757 variables; 6,920,296 clauses; 545,982 assertions |
| quotient CNF | `12f2fe58f4bfcaff19d543cdb60411f1659e86c8b4f16f599a2d1679aeeca767`; 2,464,197 variables; 11,827,887 clauses; 546,053 assertions |
| retained complete assignment | `975dbb72397674377b2ef7a5c81156701b04e0667d6ac744e0238ebd9f7e2429`; exactly 2,464,197 variables |
| alternate serialization | `8a1f06b58914930b2ba3480392f25f8070aacf9cccca617f41f94f1e279f9a4f`; semantically identical complete assignment |

I parsed source, dictionaries, assertion maps, and both DIMACS files directly. The quotient begins with the exact complete base clause stream. It orders 864 edges with ten comparison bits per edge, hence 8,640 lex positions. For each of 71 nonidentity roots, the recurrence is

`r_i = (not x_i and y_i) or ((x_i == y_i) and r_{i+1})`.

I regenerated its eight defining clauses per position and the unit root, and checked the Boolean truth relation exhaustively. Each root adds exactly 8,640 unique-definition variables and 69,121 clauses. Therefore the extension adds `71*8,640 = 613,440` variables and `71*(8*8,640+1) = 4,907,591` clauses, giving the exact totals above. All generated variable identifiers, roots, and clauses match line by line.

All 72 orbit vectors are distinct; the assignment’s identity vector is strictly lexicographically smaller than each of its 71 nonidentity translates. More generally, invariance of the complete installed base means every finite base-model orbit contains a lex-minimal representative satisfying all 71 roots, while every quotient model satisfies the unchanged base prefix. This proves equisatisfiability for this full invariant base. It does not license reuse with a noninvariant or differently bound base.

The retained assignment parser required every variable 1 through 2,464,197 exactly once, rejected duplicates/out-of-range variables, and evaluated every literal of every clause. All 11,827,887 clauses are satisfied. Classification: **SAT**, not UNSAT and not UNKNOWN.

## 7. Decoded legal frozen schedule

The assignment decodes exactly one time for every one of the 864 frozen edges. Times use every integer from 0 through 476, so the schedule has exactly 477 layers. For each layer I keyed both ancilla `(sector,check)` and data `(D,q)` resources and found zero conflicts. Every required edge occurs once and no foreign edge occurs. All 648 shared X/Z pairs satisfy the frozen MC orientation; MC violations are zero. Seventy-five shared pairs are pair-interleaved, 321 check pairs are whole-check interleaved, and the schedule is globally X/Z-interleaved. Schedule semantic SHA-256 is `843f3a156476027bce38d9bdd97a7d9bdc496d9d3e4d0acfcedb0f6014210d58`.

This is a certified legal schedule object, not a certified circuit-distance-12 witness. The direct attacks below kill that stronger claim.

## 8. Independent complete unrestricted direct-360 attacks

For each sector I independently regenerated all 144 data columns and 216 residual columns, detector equations, logical equations, stabilizer rows, exact variable dictionaries, exact clause ledgers, and full DIMACS. I evaluated every assignment clause. Canonical and physical supports were XOR-reduced; detector syndrome was recomputed; all 12 logical pairings were recomputed; canonical and physical supports were tested against the exact GF(2) stabilizer row span.

| sector | variables | clauses | exact CNF SHA-256 | assignment SHA-256 | selected named faults |
|---|---:|---:|---:|---:|---|
| Xerr | 6,130 | 23,100 | `8bbe080ff3e6eadf65f7da0180daa686386237f4b64a23f05e9fe41dd932ff67` | `9cca8da6aa23024ab343fe8c591f339f75e52297be3610c4b94c8910d4376d67` | `D:14,D:29,D:35,D:78,D:88,D:103,D:120,R:5:1,R:26:0,R:67:2` |
| Zerr | 6,088 | 22,932 | `ddec622ceef752c73696c327a09c50768a331a9ff78e7fbcd5d1445afe8c0006` | `f13cf3e68cbf8278a7b29dd94bce8c537182e77603d16596ecbe72ed628bf8e1` | `D:0,D:65,D:75,D:131,D:133,D:137,D:138,D:140,R:2:0,R:7:2` |

**Xerr witness.** Canonical support is `[1,14,29,35,69,74,78,79,88,89,101,103,104,120]`; exact physical support is `[1,14,27,28,29,35,44,69,74,78,79,88,89,103,110,120]`; logical vector is `[1,1,0,0,0,0,0,0,1,1,1,0]`.

**Zerr witness.** Canonical support is `[0,1,5,65,67,72,75,131,133,137,138,140]`; exact physical support is `[0,1,62,65,67,68,73,75,128,131,133,137,138,140]`; logical vector is `[0,0,1,1,0,1,0,0,0,0,0,0]`.

Both assignments are complete and satisfy every direct clause. Both witnesses have named fault weight 10, empty detector syndrome, nonzero logical action, and canonical and physical supports outside stabilizer span. Classification for each direct query: **SAT**. These exact physical mechanisms kill only this candidate. They are positive counterexamples, not universal absence proofs.

## 9. Free selector orbits, exact lineage, and invariance

For every `d in Z_12 x Z_6`, I translated the complete schedule, names, checks, canonical supports, physical supports, and selector tuple. Both parent stabilizers have size 1, so orbit-stabilizer gives exactly 72 distinct images per parent. I replayed all 72 translated schedules and all 144 translated physical mechanisms. Every image remains legal, named-weight 10, zero-syndrome, and nonstabilizer.

Normalized tuple comparison gives zero collision with the 24,444-entry prefix, zero cross-orbit collision, and zero within-orbit collision. The exact lineage is `24,444 + 72 + 72 = 24,588`.

I canonicalized every one of 517,140 block keys, found all unique, and evaluated the candidate against every block antecedent: zero hits. Generator closure over `(1,0)` and `(0,1)` covers exactly 1,034,280 block cases. All 24,588 selector keys are unique; both generator images of each selector exist, for exactly 49,176 selector cases. Thus the full block and selector registries are invariant, and the 71-root quotient premise remains satisfied.

## 10. Exact fresh/unstarted iteration-191 frontier

I independently reconstructed the iteration-191 source and state by preserving the full iteration-190 block registry and appending only the authoritative 144-selector orbit suffix. Canonical JSON serialization plus deterministic gzip (`level=9`, empty filename, `mtime=0`) is byte-identical.

| frontier object | exact identity / state |
|---|---|
| source gzip | `0b0ac7e6daa69d8d3ab1b98b7228c43690a5406c52defe57e46027b185984a47` |
| semantic source | `02da1bcb87a45637afa8434a8dfa4e4c8092489ace7f5a7fd1ba3266f9615532` |
| state JSON | `6059554d307e7c503bd1792dd77718a205346f5dce243e719ae057f402cf6c9f` |
| selector state | `41bb458a1b9a31aba7d70f063165221a9ae9c989421682320826dbc5d166f9e6` |
| base CNF | `d1e68e88eb4c22ffda58d3a1c73cb7dbf6082690c594e8c538f8cc70c432e223`; 1,853,886 variables; 6,929,888 clauses; 546,126 assertions |
| quotient CNF | `30ce7d14d96349e61d7105255cddc8899b8927ce728dfd147b641c75c97fe10f`; 2,467,326 variables; 11,837,479 clauses; 546,197 assertions |

Every quotient clause was regenerated from the independently verified base and the same 71-root construction. The base directory contains exactly `assertion_map.jsonl`, `definitions.json.gz`, `encoding_check.json`, `metadata.json`, and `outer.cnf`. The quotient directory contains exactly `independent_check.json`, `metadata.json`, `outer.cnf`, `translation_roots.jsonl`, and `translation_trace.json.gz`. There is no solver log, assignment, model, DRAT, LRAT, or other proof artifact. State is `next_iteration=191`, `started=false`, `stop=null`; solver-artifact count is zero. I did not launch an iteration-191 solve. Classification: **UNSTARTED/UNSOLVED**, not SAT, UNSAT, or UNKNOWN.

## 11. Lossless SAT-trace compression and proof controls

I streamed each gzip, computed raw hash/counts, recompressed with gzip level 9, empty filename and `mtime=0`, compared the regenerated gzip byte for byte, and deleted each temporary before starting the next. The three runs were strictly sequential.

| trace | raw SHA-256 | raw bytes | raw LF | gzip SHA-256 | gzip bytes |
|---|---:|---:|---:|---:|---:|
| iter190 quotient | `d32a1edccc4a69c1eab658d5c0abd18b48292af7ad497f0adf80788a1f0a24cf` | 4,216,215,280 | 48,777,352 | `efd0a3707a5277743270529e1b64e41780b5c12653dcd28e83fa74cd9816e6ba` | 593,845,688 |
| Xerr | `faf74f84c9aeae2fe6cb33404aed693d932205c936e408911382b2e9eed33c8e` | 3,409,244,299 | 26,192,664 | `d91190c9f2bb1919ce356f1fb92e4f0d786ccd3702959183169cd3a2a05271e1` | 982,280,100 |
| Zerr | `755f15c0aef317e8a5d5dea08fa99636c3538cbe9188b98a4bc74dcaadefeb79` | 2,818,069,226 | 21,948,404 | `fda010fe294bf581e4441d18d21dfcc4cd6da8c1163dd909ffb5a82424e71aa9` | 830,585,295 |

Totals are 10,443,528,805 raw bytes, 96,918,420 LF, and 2,406,711,083 gzip bytes. All three regenerated gzip streams are byte-identical; all temporaries were removed. None contains an empty-clause line. They are complete **SAT search traces**, not accepted UNSAT certificates, and receive zero proof credit.

Fresh proof-control parent PID 18324 launched PIDs 18325–18330 strictly serially. The known-valid DRAT was accepted and generated LRAT SHA-256 `cf32dfff36b24ba36c3504765f29ecf3d7a8abaa59956ade4d24a4062caa6431`; that LRAT was accepted. Corrupt DRAT, truncated DRAT, corrupt LRAT, and truncated LRAT were all rejected. Exact return codes are `[0,0,1,1,1,1]`, minimum adjacent gap is 0.000052929 seconds, and all six children were foreground, reaped, nonoverlapping, not timed out, and not detached. The generated LRAT temporary was removed. Fixture CNF SHA-256 is `b8d28f511bbc3bc5d67e0fcda748b6ad85d5e543c64bc91d09f34ecb10805efd`; valid DRAT SHA-256 is `b6c2e560bb08c84d583ca94799951a21c8cae5de35d6d04d77bc4842e9c18ecd`. These are checker controls only and prove nothing about Gross.

## 12. Retained process reconciliation

The aggregate `PROCESS_FIX2_LEDGER.json` covers exactly 40 preinstall `logs/process/*.json` rows: 35 return 0, two return 1, and three SAT solvers return 10. Every row has a unique PID, complete interval/environment/stream hashes, `reaped=true`, no detachment or timeout, and strict nonoverlap; minimum adjacent gap is 7.127506 seconds.

The physical sealed package also retains failure-process copies. `F110-008/process.json` duplicates PID 16007 already in the aggregate; F110-002 PID 14772, F110-007 PID 15660, and F110-010 PID 16761 are three additional unique retained records. Therefore the exact physical union is **43 unique retained children**, not 40: 35 rc0, five rc1, and three rc10. All 43 remain strictly nonoverlapping and reaped. The package’s “40” is accurate for its stated preinstall aggregate scope but would undercount by three if misread as the physical union; this review records that scope correction.

The scientific solvers are PID 14419 (quotient), PID 14843 (Xerr), and PID 15147 (Zerr), each rc10/SAT, proof output enabled from start, no UNKNOWN, strictly serial with minimum adjacent gap 47.838523 seconds. Stored preseal replay has 19 rc0 children; stored proof controls have six children with `[0,0,1,1,1,1]`; stored repository gates have nine rc0 children. All are attached/reaped with no overlap, timeout, or detachment.

At final cleanup I repeated an exact package-basename/tool-name process census and found zero surviving relevant children. No review-launched process survived.

## 13. Failure ledger and adversarial disposition

| failure | independent disposition | load-bearing? |
|---|---|---|
| F110-001 | duplicate literal `--` was treated as executable; failure occurred before child/science launch; corrected run starts from scratch | no |
| F110-002 | PID 14772 rc1 because vendored Z3 was absent from clean `PYTHONPATH`; partial duplicate assignment is quarantined; complete retry plus independent all-variable/all-clause check supersedes it | no |
| F110-003 | copied checker retained sealed read-only mode; corrected in scratch before execution | no |
| F110-004 | corrective orchestration command rejected before execution; no scientific child/output | no |
| F110-005 | broad relabel replacement cascaded; rejected by assertions and rebuilt before execution | no |
| F110-006 | broad forbidden-label grep falsely matched the required Round108 input path; replaced with field-specific check | no |
| F110-007 | PID 15660 rc1 because iter191 quotient checker lacked vendored Z3; clean complete retry and independent every-clause reconstruction supersede it | no |
| F110-008 | PID 16007 rc1 ran the iteration-189 registry checker on iteration 190; output quarantined; correct checker and independent registry audit pass | no |
| F110-009 | PID 16618 rc1 because process pattern `work` matched generic macOS paths; PID 16637 exact-pattern retry rc0 strictly later | no |
| F110-010 | PID 16761 rc1/EACCES because the sealed scratch directory root was `0555`; destination was absent and repository received zero bytes. Corrected same-device atomic rename temporarily changed only scratch-root owner-write, restored destination `0555`, and produced the exact sealed destination. The successful-install record was external and is not retained; current exact destination, independent seal checks, and pre/post/fresh replays corroborate recovery | no scientific effect; retained-record gap disclosed |
| F110-011 | postseal external census used `root.parent.name`, yielding generic substring `artifacts` and a false positive. The proposer’s exact-basename rerun was external and later deleted. No retained record exists; this review does not reconstruct the missing historical record | non-load-bearing external-unretained disclosure gap |
| F110-012 | final external audit incorrectly required whole-repository `git diff` to be empty despite preexisting dirty state. Under the no-new-audit-file closeout instruction, no retained record exists | non-load-bearing external-unretained disclosure gap |

F110-011 and F110-012 occurred after the immutable root seal and postseal replay and never entered the sealed package. Their absence prevents claiming a complete retained proposer closeout record, but neither changes any sealed scientific object, SAT classification, manifest identity, replay result, or independently reconstructed conclusion. They do not block proposer-level continuation. They would block a stronger claim that every postseal administrative action has a retained in-package record.

## 14. Reviewer command/correction disclosure

All substantive review children were foreground and serialized. The following reviewer defects were corrected without changing any repository file or sealed byte:

- **H111-001, PID 18062, rc1:** the first standard-library science harness lexically sorted `data_incidence` string keys, while the source’s authoritative order is numeric. This was a reviewer-ordering error. I corrected only the iteration order and reran the complete audit from the beginning as PID 18101, rc0. The successful result SHA-256 is `bbbe4aab20ed8e8d83431a2b5c5531b05ca4752aebe0ebe6c7f6287c6c5c77a3`.
- **H111-002:** the first process-audit draft looked for an obsolete absolute scratch stream path after atomic installation. I rebound it to the sealed basename plus exact hash. No scientific result depended on the missing path.
- **H111-003:** an intermediate process-audit draft double-counted retained failure copies against the 40-row aggregate. The final audit deduplicates by PID and distinguishes the 40-row scoped aggregate from the 43-record physical union.
- **H111-004:** an intermediate process-audit draft guessed solver name literals. I bound the exact record names and checked rc10, SAT token, proof-at-start, no UNKNOWN, and nonoverlap directly.
- **H111-005:** a read-only canonical introspection snippet treated the `routes` mapping as a list and failed after printing data. I corrected the schema access; no file was written.
- **H111-006:** the first overlay-copy shell request was policy-rejected before execution because it contained an `rm -rf` form. It created no child and changed no path. I used a new destination and a Python hardlink copy.
- **H111-007, PID 18852, rc1:** the first candidate-extraction gate omitted the YAML’s final LF while comparing character slices. I added that one LF to the extracted comparison and reran the entire required gate set.
- **H111-008, PID 19017, rc1:** an optional all-project evidence-closure probe found preexisting unlinked `grothendieck-d4` draft artifacts. This was outside the commissioned Circdist closure gate and predates the overlay delta. The scoped Circdist evidence closure passes; all-project DAG validation separately passes.

Trace roundtrip PID 18182 returned 0 after 551.806704 seconds; proof-control wrapper and all six nested children returned the expected codes. No failed command output was used as evidence. Scratch-only scripts and JSON records are deleted after the final artifact and gate identities are recorded.

## 15. Limitations and exact claim labels

- Iteration-190 quotient: **SAT**, proved by a complete assignment satisfying every clause.
- Xerr direct-360: **SAT**, with a proved physical zero-syndrome nonstabilizer mechanism for this schedule.
- Zerr direct-360: **SAT**, with a proved physical zero-syndrome nonstabilizer mechanism for this schedule.
- Iteration 191: **UNSTARTED/UNSOLVED**; no solver was launched.
- SAT streams: lossless **traces**, not UNSAT proofs.
- Root branch A: **not proved**.
- Root branch B: **not proved**.
- `CIRCDIST.gross`: **CONJECTURED**.
- `gap-via-lift`: **CONJECTURED**.
- Exact residual: **`D*_Gross in {11,12}`**.
- Package: **installed and sealed**; candidate canonical below is **reviewer-proposed**, not installed by this review.
- F110-011/F110-012: **external-unretained disclosure gaps**, not reconstructed historical evidence.

## 16. Disposable-overlay validation and repository hygiene

The final disposable overlay gate run is recorded outside the repository as SHA-256 `504e098b998a25676662b16ca7a3bf459f9cd3b046cedbe6a01237c7298624f1`, 15,462 bytes / 304 LF. Its ten foreground children are strictly serial and reaped; every required gate returned 0:

| gate | exact result |
|---|---|
| extraction, unique-key YAML, and preservation | PASS; one marker pair; extracted bytes exact; zero duplicate keys; predecessor object exact after licensed-delta removal |
| Circdist DAG | PASS; 16 node files |
| all-project DAG | PASS; 500 node files |
| migration | PASS; 16 nodes, 143 original events, 728 byte-identical copies |
| release contracts | PASS; 14/14 |
| DAG contracts | PASS; 24/24 |
| Lean selftest | PASS; 23/23 assertions |
| repository duplicate-YAML scan | PASS; 988 YAML files, 30,105 mappings, zero duplicates |
| Circdist evidence closure | PASS; 178 structured paths, all project-local and linked |
| `git diff --check` | PASS |

The duplicate-scan result is SHA-256 `b6bffc429d77bb7e03b7b7014c2b5ad4b51ed661c4205f4cbf296e5e28573c90`, 126 bytes / 7 LF.

The overlay candidate preserves every predecessor object exactly after removing only the licensed append delta: one root-assessment suffix, two evidence entries (80 to 82), one `gap-via-lift` assessment suffix, the `dstar-residual.task` replacement, and one event (25 to 26). Both levels remain `CONJECTURED`; no old evidence/event is reordered or changed. Untouched source bytes remain byte-for-byte identical because the candidate was made by bounded textual insertions and one bounded frontier scalar replacement.

The live repository began on `main` at HEAD `e40a7ac40972ad5186018797efa390a8e3f784f0` with substantial preexisting dirty state. Final comparison is against the exact start snapshot, not against an incorrect all-clean premise. Relative to that snapshot, this review creates exactly one durable path: this Markdown file. The canonical replacement below is not installed by the reviewer.

## 17. Unique licensed replacement

There is exactly one licensed replacement in this review. Its extracted YAML is 127,667 bytes, SHA-256 `7cc45da6ae90deb2f44aee40fa28a17c5f0a74a36970f4cef795d6ae317883d4`. Marker counts are exactly one begin and one end. The Markdown file’s own final hash and size cannot be embedded non-self-referentially; they are reported externally after the immutable write. No second candidate is licensed.

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
    gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.
    The fresh Round-111 independent exact review clears the sealed Round-110 iteration-190 invariant-quotient
    continuation package for proposer-level continuation only. The complete 2,464,197-variable assignment satisfies all
    11,827,887 quotient clauses and decodes a legal globally interleaved 477-layer schedule; both independently rebuilt
    unrestricted direct-360 sectors are SAT and physically replay to zero-syndrome nonstabilizers. Their free 72-element
    orbits add exactly 144 collision-free selectors while preserving all 517,140 invariant block semantics. The exact
    fresh/unstarted iteration-191 frontier has 24,588 selectors, base
    sha256:d1e68e88eb4c22ffda58d3a1c73cb7dbf6082690c594e8c538f8cc70c432e223 and quotient
    sha256:30ce7d14d96349e61d7105255cddc8899b8927ce728dfd147b641c75c97fe10f. All three solver streams are SAT traces,
    not UNSAT proofs. No Gross UNSAT, direct absence, repair, exhaustion, distance-12 witness, universal distance-11
    ceiling, D* narrowing, route promotion, or root promotion is licensed; CIRCDIST.gross and gap-via-lift remain
    CONJECTURED with D*_Gross in {11,12}.'
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
    - path: circdist/artifacts/circdist_gross_iter190_invariant_quotient_continuation_round110_20260902
      kind: run
      note: Sealed Round-110 exact iteration-190 full-invariant continuation package independently cleared at proposer level by
        the fresh Round-111 review. Package identities are root SHA256SUMS sha256:8ce014a0bc1b4273cec02e2af7d9da54691290dd35a82d7c3bfe6c522a031bc5,
        payload sha256:d36ab5ff07b8f3214f7d4ba1cbf0bcee679fc336ecfa0a099a06f1e1f37b617a, and inventory sha256:fd655231af824f63c814c6a001a42998cf44a07e31e898607432d3820f7e9938.
        The iteration-190 quotient is SAT with a complete assignment and legal 477-layer schedule; complete unrestricted Xerr
        and Zerr formulas are SAT and physically replay to nonstabilizer mechanisms. Their two free translation orbits add exactly
        144 collision-free selectors, yielding fresh/unstarted iteration 191 with 517,140 blocks, 24,588 selectors, base sha256:d1e68e88eb4c22ffda58d3a1c73cb7dbf6082690c594e8c538f8cc70c432e223,
        and quotient sha256:30ce7d14d96349e61d7105255cddc8899b8927ce728dfd147b641c75c97fe10f. All solver streams are SAT traces.
        No absence, repair, exhaustion, distance narrowing, route change, or level change follows.
    - path: circdist/reviews/circdist_gross_iter190_invariant_quotient_continuation_round110_exact_review_round111_20260902.md
      kind: review
      note: Fresh independent Round-111 exact review. It verifies every root and payload manifest and inventory row, proves zero
        content or metadata change around a fresh clean 19-child strict-serial root replay, independently reconstructs the Z_12
        x Z_6 action, all iteration-190 source/base/quotient clauses and complete assignment, the legal schedule, both direct
        CNFs and physical mechanisms, the free selector orbits and invariant registries, and exact fresh/unstarted iteration 191.
        It losslessly roundtrips all three deterministic-gzip SAT traces, reruns proof controls, reconciles retained processes
        and F110-001--F110-010, discloses F110-011/F110-012 as postseal external-unretained non-load-bearing gaps, and passes
        the disposable-overlay gates. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION; evidence/frontier reuse only. CIRCDIST.gross
        and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.
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
        CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.
        The fresh Round-111 independent exact review clears the sealed Round-110 iteration-190 continuation at proposer
        level only. The quotient and both unrestricted direct sectors are SAT; the legal 477-layer candidate is killed
        in Xerr and Zerr by physically replayed zero-syndrome nonstabilizers. The two free translation orbits add 144
        collision-free selectors and yield fresh/unstarted iteration 191 with 517,140 blocks, 24,588 selectors, base
        sha256:d1e68e88eb4c22ffda58d3a1c73cb7dbf6082690c594e8c538f8cc70c432e223, and quotient
        sha256:30ce7d14d96349e61d7105255cddc8899b8927ce728dfd147b641c75c97fe10f. There is no Gross UNSAT, absence,
        exhaustion, distance-12 witness, universal distance-11 ceiling, D* narrowing, route promotion, or root
        promotion; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
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
    task: Continue only from the independently reviewed sealed fresh/unstarted iteration 191 full-invariant state. The exact
      translation-closed registry contains 517,140 unique sound block semantics and 24,588 invariant exact EFSSC
      selectors. Bind source-file sha256:0b0ac7e6daa69d8d3ab1b98b7228c43690a5406c52defe57e46027b185984a47,
      semantic-source sha256:02da1bcb87a45637afa8434a8dfa4e4c8092489ace7f5a7fd1ba3266f9615532, state-file
      sha256:6059554d307e7c503bd1792dd77718a205346f5dce243e719ae057f402cf6c9f, and selector-state
      sha256:41bb458a1b9a31aba7d70f063165221a9ae9c989421682320826dbc5d166f9e6 before use. Its deterministic base formula
      has 546,126 source assertions, 1,853,886 variables, 6,929,888 clauses and CNF
      sha256:d1e68e88eb4c22ffda58d3a1c73cb7dbf6082690c594e8c538f8cc70c432e223. The 71-root lex quotient adds exactly
      613,440 unique-definition variables and 4,907,591 clauses, yielding 2,467,326 variables, 11,837,479 clauses,
      546,197 assertions and CNF sha256:30ce7d14d96349e61d7105255cddc8899b8927ce728dfd147b641c75c97fe10f. It is
      equisatisfiable with this full invariant base only. It has not been launched; its base formula directory contains
      exactly assertion_map.jsonl, definitions.json.gz, encoding_check.json, metadata.json and outer.cnf, and its
      quotient directory contains exactly independent_check.json, metadata.json, outer.cnf, translation_roots.jsonl and
      translation_trace.json.gz, with no solver log, model, assignment, DRAT, LRAT or other proof artifact. The
      iteration-190 quotient is SAT and its exact schedule is killed in both complete unrestricted direct sectors by
      independently checked named-weight-10 physical mechanisms. Their two collision-free free 72-element selector
      orbits are the final atomic addition already represented in iteration 191. Repair was not entered because both
      direct sectors are SAT. Solve the iteration-191 quotient proof-first with proof output enabled from byte zero and
      strict serialization. For SAT, retain the complete assignment, verify every DIMACS clause and frozen
      legal-schedule condition, rebuild both complete unrestricted 360-column sectors, and add only independently
      physically replayed full selector orbits after bilateral adjudication. For UNSAT, retain a complete DRAT proof,
      independently accept it, generate LRAT, independently accept LRAT, and invoke only the theorem licensed by the
      invariant installed exclusions. UNKNOWN or SAT proof-side streams are non-certificates. Enter repair only after
      both complete direct sectors independently check UNSAT. Preserve the frozen S_Gross geometry, strict solver
      serialization, MC0, terminal residual semantics, both CSS sectors, the full 72-element action, exact tuple
      identity, integer- and memory-safe streaming, atomic state-last transitions, and every earlier exclusion. Use the
      sealed conventional replay.sh interface. Keep CIRCDIST.gross and gap-via-lift CONJECTURED and D*_Gross in {11,12};
      this reviewed continuation supplies no Gross UNSAT, absence, exhaustion, distance-12 witness, universal
      distance-11 ceiling, D* narrowing, route promotion, or root promotion.
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
  gross-iter190-invariant-continuation-round111-review-2026-09-02:
    date: '2026-09-02'
    type: review-completed
    summary: 'Fresh independent Round-111 review clears the sealed Round-110 iteration-190 full-invariant continuation package
      at proposer level and licenses continuation only from fresh/unstarted iteration 191: 517,140 invariant block semantics,
      24,588 invariant selectors, selector-state sha256:41bb458a1b9a31aba7d70f063165221a9ae9c989421682320826dbc5d166f9e6, checked-unstarted
      base CNF sha256:d1e68e88eb4c22ffda58d3a1c73cb7dbf6082690c594e8c538f8cc70c432e223 (546,126 assertions; 1,853,886 variables;
      6,929,888 clauses), and checked-unstarted 71-root quotient sha256:30ce7d14d96349e61d7105255cddc8899b8927ce728dfd147b641c75c97fe10f
      (546,197 assertions; 2,467,326 variables; 11,837,479 clauses). The iteration-190 quotient and both complete unrestricted
      direct sectors are SAT; the legal 477-layer candidate has named-weight-10 Xerr and Zerr physical mechanisms and is not
      a distance-12 witness. Both free 72-element selector orbits are collision-free and the full registry remains invariant.
      All three solver streams are SAT traces. F110-001--F110-010 and retained process records are adjudicated; F110-011/F110-012
      are disclosed as postseal external-unretained non-load-bearing gaps. No Gross UNSAT, direct absence, repair, exhaustion,
      distance-12 witness, universal distance-11 ceiling, D* narrowing, route change, or level change is licensed; CIRCDIST.gross
      and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
    sources:
    - path: circdist/artifacts/circdist_gross_iter190_invariant_quotient_continuation_round110_20260902
      kind: run
    - path: circdist/reviews/circdist_gross_iter190_invariant_quotient_continuation_round110_exact_review_round111_20260902.md
      kind: review
```
<!-- END COMPLETE CIRCDIST.gross.yaml REPLACEMENT -->
