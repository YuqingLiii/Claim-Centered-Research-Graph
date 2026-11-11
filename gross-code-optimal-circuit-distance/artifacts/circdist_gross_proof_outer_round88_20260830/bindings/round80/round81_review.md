# Round-81 exact review of the Round-80 Gross whole-registry package

Date: 2026-08-30  
Reviewer role: fresh independent mathematical reviewer  
Reviewed package: `circdist/artifacts/circdist_gross_whole_registry_round80_20260830/`  
Accepted external root-manifest seal: `e086a828391361620eabfbd31b544606f7817826af546fb8779a500f95ec0426`

## Verdict and exact license

**CLEAR-PROPOSER-LEVEL-CONTINUATION**, subject only to the narrow delta stated below. I found no load-bearing mathematical, state-chain, process, or packaging discrepancy in the sealed Round-80 proposer package.

This review licenses a later canonical evidence/frontier link to this exact sealed package and this review, with continuation only from the exact fresh, unstarted iteration-102 state:

- 1,440 inherited unary blocks;
- 20 Round-62 blocks;
- `G=12,820` installed generalized blocks;
- `D=204` candidate-exact dynamic blocks;
- mechanism registry/raw count `120/120`;
- total installed sound blocks `14,484`;
- semantic SHA-256 values: dynamic `62cabe5f2925fc0caadd340848ea439219c13dc3d397c67762f852d36b6560e2`, generalized `4547a39d560358ce24c1615f5db99f17735c717a2b10d67ad2cfac515731acf3`, registry `b9816477e347ed095e26fd4a521be8a951e92e1b3aa66c668cd2fa315d652604`, raw mechanisms `fff897136200a97d12ae1756ca07a8aadd10e80cf11e4cce8e7ba30f8e428600`.

It does **not** decide `D*_Gross`, prove absence, license repair, promote the Gross claim, close any route, change the exact claim or routes, edit a protocol or scheduler, or assign mathematical meaning to a miss, zero domain, deletion countertuple, SAT trace, or packaging-budget exclusion. The reviewed result remains `MATERIAL-CHECKED-PROGRESS-NOT-CLOSED`; `D*_Gross` remains in `{11,12}`.

## Independence, scope, and reproducibility

I did not contact or use the Round-80 author and did not inherit a conclusion from a proposer checker. I first made fresh, non-importing checkers in a disposable directory outside the repository. Those checkers read package data but imported no package Python module. I independently rebuilt geometry, GF(2) signatures, catalogs, relations, selectors, semantic classifications, schedules, direct CNFs, assignments, state transitions, controls, and manifests. Only after all independent gates passed did I invoke the proposer full verifier as corroboration. I used no sub-agent.

The review was read-only except for this single review file. In particular, I did not edit any package object, proof-DAG node, scheduler, protocol, generated view, or existing review. The scratch path was `/tmp/cgr_round81_exact_review.MLQC0w` and was deleted after the final hashes and process checks. The repository was already broadly dirty/untracked. I took a pathname/size/mtime/mode baseline of 12,237 files and a NUL-delimited `git status --porcelain=v1 -z` baseline before review, preserved concurrent work, and never reverted it.

The principal commands were of the following exact form, with `P` the sealed package, `R` the repository, and `S=/tmp/cgr_round81_exact_review.MLQC0w`:

```text
python3 -m venv "$S/venv"
"$S/venv/bin/pip" install z3-solver==4.13.3.0 psutil==7.0.0
"$S/venv/bin/python" "$S/check_manifests.py" "$P" "$S/manifest_check.json"
"$S/venv/bin/python" "$S/check_sources.py" "$P" "$R" "$S/source_check.json"
"$S/venv/bin/python" "$S/check_math_core.py" "$P" "$S/math_core_result.json"
/usr/bin/time -l "$S/venv/bin/python" "$S/check_multi8.py" "$P" "$S/multi8_result.json"
/usr/bin/time -l "$S/venv/bin/python" "$S/check_cegar_direct.py" "$P" "$S/cegar_direct_result.json"
/usr/bin/time -l "$S/venv/bin/python" "$S/check_cegar_literal.py" "$P" "$S/cegar_literal_result.json"
/usr/bin/time -l "$S/venv/bin/python" "$S/check_cegar_classification.py" "$P" "$S/cegar_classification_result.json"
/usr/bin/time -l "$S/venv/bin/python" "$S/check_negative_controls.py" "$P" "$S/negative_controls_result.json"
/usr/bin/time -l "$S/venv/bin/python" "$S/check_proof_controls.py" "$P" "$S/fresh_controls"
/usr/bin/time -l "$S/venv/bin/python" "$S/check_incidents_process_packaging.py" "$P" "$S/incidents_process_packaging_result.json"
/usr/bin/time -l "$S/venv/bin/python" "$S/check_repository_inventory.py" "$P" "$R" "$S/repository_inventory_result.json"
```

Checker source SHA-256 values were:

| checker | SHA-256 | independent wall / max RSS |
|---|---|---:|
| `check_manifests.py` | `ec10264c4eca54a872638300c33da8750d9d03ab31fd700c4ff9825d17bc7b96` | 5.251 s / not sampled |
| `check_sources.py` | `340e8f2583c0ac7eedd147c314e2c24f98344583670fe2bf390a85021eb8e3cc` | ordinary hash scan |
| `check_math_core.py` | `41565409ca45f9d844e8d3205ca389cc6a362d7e4e43efcb416444882d8b7124` | 169.862 s / not sampled |
| `check_multi8.py` | `30a118f250d26d6753481d2da3b585b20e8717ea8d1dc6bf7561a9b3648d2376` | 4,071.08 s / 3,901,079,552 B |
| `check_cegar_direct.py` | `47c1e0e4f0183c124dd8ecf7653cd8439038dc7bfa7bc74a5143836e07fdee7c` | 57.50 s / 2,758,361,088 B |
| `check_cegar_literal.py` | `323ebf0fc345c5a500c1f49eee70535b0775980bba1c47562917c1a57953c7a2` | 307.80 s / 3,345,874,944 B |
| `check_cegar_classification.py` | `f1d93377ec514ebbd3e101a209c84df0ef21d39138e6318e2dc6eba494bc52b3` | 15.58 s / 2,558,263,296 B |
| `check_negative_controls.py` | `12be4098ab2e175c51bd34729898d11f83e4befe60e07ca7945d423f7ad0738e` | 38.58 s / 10,354,835,456 B |
| `check_proof_controls.py` | `a35197e704643ef5352bd3dcb9fb4293f5133fdc21399bb8bfed7b923929444f` | 0.31 s / 47,382,528 B |
| `check_incidents_process_packaging.py` | `f6d93ce7bc34326ba810091b198ad9a31651ddf6f6dafe91f8539817c2dd7ebf` | 7.94 s / 627,343,360 B |
| `check_repository_inventory.py` | `24e4cb51b15709dabc0cb92ff47e9872d3514441142f5b740c364f72e16d0bbf` | 1.94 s / ordinary scan |

The 10.35 GB peak of the deletion-control checker is high but the process completed normally; I report it rather than conceal it. The core checker had three reviewer-side assertion bugs during development: a local-name shadow, reversed dominator orientation, and an overly strict deletion-witness identity requirement. I corrected those only in disposable reviewer code and reran from the start. They exposed no package defect and changed no package data.

## Seal, inventory, gzip, and source authority

I parsed both manifests independently, rejected absolute paths, `.`/`..`, duplicate rows, unsorted rows, malformed hashes and sizes, and recomputed every file hash from package-root-relative bytes. The root manifest excludes exactly itself and includes the payload manifest; the payload manifest excludes exactly both manifests. Reconstructed set equations and row order were exact.

Results:

- physical package: 1,221 files, 303,862,955 bytes;
- root manifest: 1,220 rows, 138,803 bytes, SHA-256 `e086a828391361620eabfbd31b544606f7817826af546fb8779a500f95ec0426`;
- payload manifest: 1,219 rows, 138,714 bytes, SHA-256 `8f71dc39916cdab9d57ff2add15e5130631600b2789d7da0bd5626afdfdc202d`;
- bytes named by root rows: 303,724,152;
- mismatched, missing, extra, duplicate, unsafe, or incorrectly self-included rows: zero.

For every `.gz` row I parsed the header/trailer, required deterministic header fields `FLG=0`, `mtime=0`, `OS=255`, streamed decompression, checked CRC/ISIZE where applicable, and recomputed compressed and uncompressed SHA-256 independently. All 942 objects passed. They represent 10,108,629,063 uncompressed bytes and 294,398,854 compressed bytes. My ordered combined compressed/uncompressed stream digest was `9508a895c5f42834d11c58a206bbb6ed756cfdf7b23161c2788148c172283f0a`; dual-hash mismatches were zero.

The licensed source is exactly the fresh, unstarted iteration-90 state reviewed in Rounds 78/79:

- base `1,440+20=1,460`, generalized `10,595`, dynamic `180`, registry/raw `96/96`, total `12,235`;
- dynamic `30227f09a28c318ea392ae0473cc7644c294ea02aac6007d30eaddd1884ee348`;
- generalized `ba4e37e48c856f8966fd86540daab423468c551289856517aacc35cc1403c8f3`;
- registry `6663a3a3036199de684255c622690ebf00e02b7e5fd0249af6bbafcfece42cdd`;
- raw `6746258d7e045c211596ec264a1bcf9a748357e6b7a8f76008e532e189179f1f`.

I independently matched the accepted Round-78 root seal `db82c387493285e56eeddcef6e7bafc3e48954c4034e6ec2fc699cea1699c987`, its 1,138-row payload, and the fresh Round-79 review: 39,463 bytes / `e90dc1a23c5c1740267c0ed21920ef4b4af05dab1aecd5eeef934c2a25d2a17a`. The exact Round-77 compressor is 2,760 bytes / `d4abdf75b066d8a2507d5c010f96c1c1760f36c6d1d242048fb45c5928cb8dde`. No defective/rejected Round-78 seal and no stale compressor row appears in the source closure.

`SOURCE_BINDINGS.json` has five live-binding assertions but four unique live objects because the prior review is deliberately checked through two bindings. I treat this as transparent assertion accounting, not five distinct files. All five assertions matched. During review the scheduler legitimately advanced from the sealed snapshot `d0cdd2a6f6a67a49f3250c781ea82a97e0b32b02eda7c2ce43568a8e3212a35b` (185,510 bytes) to the later Round-80/81 scheduler `38686099c543e63bf2da69751f9e99ae9b9499b0d26d4c09760aec7dc9608448` (189,680 bytes). That disclosed later control-plane drift did not alter any licensed source object.

## Independent geometry and raw-mechanism reconstruction

I rebuilt the `12 x 6` torus indexing, all 864 encoded edges, the 72 X and 72 Z check rows, and all 648 MC overlaps from the lattice formulas rather than package helper functions. GF(2) elimination rebuilt stabilizer row spaces and twelve logical representatives in each sector. For a support vector `v`, my signature was the concatenation

```text
sigma_X(v) = (<v,H_Z[0]>,...,<v,H_Z[71]>,<v,L_Z[0]>,...,<v,L_Z[11]>)
sigma_Z(v) = (<v,H_X[0]>,...,<v,H_X[71]>,<v,L_X[0]>,...,<v,L_X[11]>)
```

with all inner products in GF(2). A mechanism is positive only when the first 72 syndrome bits vanish and at least one of the final 12 logical bits is nonzero. I independently translated the seed supports across all `12*6` lattice offsets, removed the stabilizer span, and rebuilt canonical and physical support signatures. Useful geometry stream digests were X/Z check rows `dbd300d1b6727374b6d6a2f068af7891243dbc76b261a93d3c7c70137f337bdb` / `b5cc6e91d5159515082ccaff33a2293fe2b8107f665c943b99c0341ba5036205`, X/Z pools `48778b0e1ec5df722305b2f8a8eade3750a4d5480dfb595149b8844a1a162c8a` / `a3f568f88a1702e2d02b30f29a1363bc820bfaaf8e7a05ea87d7b05ba068e147`, and X/Z bases `66aa5130e41c3794c06e1ec15918f09aefd80b020eae47448d46a4a8236a0aa4` / `b700b2b585a13a723294fef150be81e760a45f467ea60dcda97ba850cde2ea4d`.

All 96 raw mechanisms were canonical and physically replayable, split 48 Xerr / 48 Zerr. Every stored canonical and physical residual sequence produced the same signature, zero syndrome, nonzero logical component, and permitted fault weight. Replay stream SHA-256: `6dbee55bdf73a534c400deec42dfd332a098e8d208cea9883ae3f205903fb9a6`.

## Complete leaf catalogs and pair reconstruction

For each participating check I enumerated all `6!=720` permutations lexicographically and rebuilt every strict-order mask from the order itself. The result is exactly 138 complete catalogs / 99,360 records and 459 distinct residual options. Catalog and option streams were respectively `ead0c3b4e236f3d4e9554f459a12aa24bdf00390ae26068156952ede40e362ed` and `11d5547174a2ca34d01686dfbc18f706207eca7d7f8a5f6250eba850320009c5`.

For each distinct-check option pair I recomputed the canonical and physical XOR supports and their signatures. There were 51,855 completion attempts, 3,169 positive configurations, and 1,557 exact pair relations; the attempt stream was `1528e85e23f792efa591a27231e9da8e938ecccea1bbcb221ab6587ca2a9a56c`. For checks `a,b` the exact positive set was reconstructed as

```text
R_ab = (U_a x Omega_b) union (Omega_a x U_b)
       union union_r (A_r x B_r),        |Omega_c|=720.
```

I materialized each of the 720 row masks, counted their union, and also retained first-hit raw selectors. The complete set contains 606,704,944 positive truth cells; 1,343,344 cells are explicitly represented by positive option rectangles. Ordered truth-row stream SHA-256: `8d4979b858fc192b6cf160f371178096bd8f9654a3a5222535ff0ffad9c07661`.

### The 6,338 versus 6,346 reconciliation gate

This apparent discrepancy was an explicit blocking gate. It is now closed by an exact list/set reconciliation:

- the 3,169 positive two-check configurations generate two deterministic rectangle directions each, hence `3,169*2=6,338` ordinary pair terms;
- the package then appends exactly eight terms from two eligible shared-check two-selector pairs, four deterministic minimization directions per pair;
- `raw_term_candidates == flatten(pair_relations.generated_terms) ++ flatten(multi_selector_search.generated_terms)` byte-for-byte;
- therefore the classification raw count is `6,338+8=6,346`.

This is a staged-definition distinction, not a missing raw enumeration. I rebuilt semantic normalized keys and replayed the evolving installed union without trusting the ledger. Exact classification was `duplicate_old=5,923`, `duplicate_new=64`, `dominated_old=28`, `covered_by_full_evolving_union=331`, `retained=0`; classification stream `95085547bbd3c75ad002ad914e3d4c1f68183899058b2078fd9dfa76a2cde96f`. The installed state hashes before and after this pair stage are identical.

For the eight shared-check terms, I independently computed each check-domain mask and a joint GF(2) dynamic program. On shared checks the DP state is `(s1,s2)`; on checks exclusive to selector one/two it is `s1` or `s2`. For every shared state I counted completions in which selector one is valid, otherwise selector two is valid, and required the double-invalid count to be zero:

```text
Nbad = sum_s Nshared(s) * N1_invalid(s1) * N2_invalid(s2) = 0.
N1choice + N2choice + Nbad = product_c |M_c|.
```

I reran forward and reverse atom deletion minimization from selector-one, selector-two, and union seeds as applicable, checked the exact eight emitted terms, and replayed every stored relaxed-box deletion witness against both physical selectors. The complete direction-duplicated products and terminal counts were:

| selectors / seed | direction | atoms | product | selector-one choices | selector-two choices | shared states | exclusive states |
|---|---|---:|---:|---:|---:|---:|---:|
| iter48/iter67 / selector1 | forward | 16 | 320,979,616,137,216,000,000 | 320,979,616,137,216,000,000 | 0 | 36 | 1 / 11,390,625 |
| iter48/iter67 / selector1 | reverse | 16 | 320,979,616,137,216,000,000 | 320,979,616,137,216,000,000 | 0 | 36 | 1 / 11,390,625 |
| iter48/iter67 / selector2 | forward | 64 | 782,757,789,696 | 0 | 782,757,789,696 | 36 | 1 / 1 |
| iter48/iter67 / selector2 | reverse | 64 | 782,757,789,696 | 0 | 782,757,789,696 | 36 | 1 / 1 |
| iter50/iter70 / selector1 | forward | 66 | 278,628,139,008 | 278,628,139,008 | 0 | 3 | 1 / 1 |
| iter50/iter70 / selector1 | reverse | 66 | 278,628,139,008 | 278,628,139,008 | 0 | 3 | 1 / 1 |
| iter50/iter70 / selector2 | forward | 16 | 320,979,616,137,216,000,000 | 0 | 320,979,616,137,216,000,000 | 24 | 900,000 / 1 |
| iter50/iter70 / selector2 | reverse | 16 | 320,979,616,137,216,000,000 | 0 | 320,979,616,137,216,000,000 | 24 | 900,000 / 1 |

Every double-invalid terminal count is zero. The eight direction-duplicated products sum to 1,283,918,466,671,635,857,408; DP stream SHA-256 is `22d8db681e79d891c36dddb06d5d9246156d81b4ce0614b3af55468ffe5b7fd6`. Runtime was 4,069.813 s internally / 4,071.08 s externally, maximum RSS 3,901,079,552 B, zero swaps and zero signals. This independently closes the eight-item reconciliation subgate.

## Exact whole-registry star synthesis

I did not infer stars from summary counts. I reconstructed every candidate box from strict atoms and 720-bit local masks. Across 27,142 seed attempts I obtained 457 sound synergistic raw candidates, 2,461 zero-domain rejections, zero unsound accepted candidates, and 48,905 non-synergistic minimization directions. The ordered raw stream hash was `2ea173041f1596036eacfc25ac326531e424a1607aafaa701804f95a5cde6ca9`.

For a star center `c`, leaf `l`, candidate local domains `M`, and exact pair relation `R_cl`, I computed

```text
G_l = {o_c in M_c : for every o_l in M_l, (o_c,o_l) in R_cl}.
P_l = M_c intersect G_l minus union_{k before l} G_k.
```

The `P_l` masks were rebuilt in fixed priority and required to be pairwise disjoint with union exactly `M_c`. Every retained star had at least two nonempty leaf partitions and no single universal leaf. At each `(o_c,o_l)` cell I selected the first raw witness in the recorded deterministic priority, then independently reconstructed its canonical support, physical support, equal signature, zero syndrome, nontrivial logical action, and fault bound. Other leaves are free, so a partition cell represents

```text
|P_l| * |M_l| * product_{k != l}|M_k|
```

complete tuples. The sum over leaves had to equal `product_j |M_j|` exactly.

I actually replayed all 304,704 literal raw-selector center/leaf cells and evaluated the complete factorized products totaling 35,294,400 tuples. Selector stream SHA-256: `1e40db7913e344ca03804c151cd7397fb3600dbf16795c545b339484ef51dd39`. I also rebuilt all 292 star deletion controls in the scope they claim; each exposes only the named relaxed star test and was never used as global absence evidence.

Semantic classification used sector plus all exact local-domain masks, never atom spelling. It produced `dominated_old=77`; the remaining 380 were unique and nondominated; 54 were already covered by the full evolving installed union; exactly 24 were retained strict expansions; and 302 sound candidates were deterministically excluded by the packaging budget. The arithmetic `77+380=457` and `54+24+302=380` closes. The 302 exclusions remain positive sound terms and carry no absence inference.

For each of the 24 retained terms, I independently asked Z3 for an assignment in the term's product box and outside every member of the entire then-installed evolving union. All 24 were SAT. For the 54 covered terms, the analogous outside-union formula was UNSAT. I then expanded every retained witness to all 144 local checks and, at every X and Z check, verified every one of the 144 local-order assignments: 3,456 check assignments total. Thus the union grows strictly 24 times. Re-serializing the post-whole library yielded the full SHA-256 `b71eb0509a99016a1718aa2f03ba19193c9b88ef359b47898c3d3517127e9a5f`, taking `G` from 10,595 to 10,619.

## Iterations 90 through 101: exact CEGAR

### Outer schedules

For each iteration I reconstructed the SMT instance independently from the exact committed state, not from a solver log. The instance names all 864 edges, checks all 648 MC overlap constraints, local legality, and the encoded global interleaving/parallel-layer conditions. Each stored complete schedule satisfies every asserted clause. All twelve formulas are SAT. Across them I directly evaluated 158,899 installed-block antecedents as false on the candidates, consistent with legal outer counterexamples and not with closure.

The schedules are complete legal schedules in the package's encoded model; I do not broaden “complete” into an unrestricted serial permutation. No iteration returned UNSAT, UNKNOWN, or timeout.

### Complete unrestricted direct sectors

For each outer schedule and each of Xerr/Zerr I rebuilt the unrestricted direct-360 formula from first principles: 72 checks, 144 singleton data columns, 216 elementary residual columns, 360 primary choices, and fault bound `W=10`, with no pool, residual-pattern, check-count, or within-check order-family restriction. I rebuilt all 24 DIMACS files byte-for-byte. All 24 stored assignments are complete and SAT. I evaluated all 536,608 clauses, then replayed all 24 canonical and physical mechanisms for equal signatures, zero syndrome, nontrivial logical action, and permitted weight. As adversarial controls I flipped one assignment literal in each sector and removed one selected physical fault; all 24+24 corruptions were rejected.

The most constrained proof-output attempt is iteration 90 Xerr. Its SAT trace is 248,948,763 bytes / SHA-256 `420634d8d7bcbe9184e3a16a04915a5cbb6f2f5ea248360f9d407af7d18e48c9`; deterministic gzip is 52,158,184 bytes / `2d56fff5acc0b8f2f9a95c3812d1b6b97d70ff88320880c21d02738222cff1a4`. It accompanies SAT and is not a DRAT/LRAT absence certificate. Candidate Gross UNSAT proofs are zero.

### Per-iteration reconstruction and atomic state order

I matched each `before`, pending output, commit journal, `after`, and next iteration `before` semantic object. Online synthesis and all exhaustive checks precede its installation; cross-registry synthesis and all exhaustive checks precede its installation; the two candidate-exact blocks and two raw/registry mechanisms are staged only after direct replay. The journal writes temporary files on the same filesystem, fsyncs as recorded, and uses `os.replace`; only a complete four-object state is published. All twelve commits are atomic and every next process consumes the exact prior commit.

| iter | G before -> after | layers | online + | cross + | exact + | X vars/clauses | Z vars/clauses |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 90 | 10,619 -> 10,806 | 160 | 7 | 180 | 2 | 5,934 / 22,316 | 5,932 / 22,308 |
| 91 | 10,806 -> 11,049 | 155 | 14 | 229 | 2 | 5,914 / 22,236 | 5,931 / 22,304 |
| 92 | 11,049 -> 11,242 | 143 | 3 | 190 | 2 | 5,947 / 22,368 | 5,961 / 22,424 |
| 93 | 11,242 -> 11,371 | 180 | 3 | 126 | 2 | 5,963 / 22,432 | 5,977 / 22,488 |
| 94 | 11,371 -> 11,548 | 164 | 13 | 164 | 2 | 5,962 / 22,428 | 5,965 / 22,440 |
| 95 | 11,548 -> 11,621 | 173 | 2 | 71 | 2 | 5,967 / 22,448 | 5,972 / 22,468 |
| 96 | 11,621 -> 11,833 | 175 | 11 | 201 | 2 | 5,948 / 22,372 | 5,970 / 22,460 |
| 97 | 11,833 -> 11,958 | 183 | 10 | 115 | 2 | 5,938 / 22,332 | 5,960 / 22,420 |
| 98 | 11,958 -> 12,157 | 156 | 5 | 194 | 2 | 5,953 / 22,392 | 5,955 / 22,400 |
| 99 | 12,157 -> 12,321 | 175 | 5 | 159 | 2 | 5,951 / 22,384 | 5,913 / 22,232 |
| 100 | 12,321 -> 12,562 | 168 | 12 | 229 | 2 | 5,911 / 22,224 | 5,919 / 22,256 |
| 101 | 12,562 -> 12,820 | 157 | 9 | 249 | 2 | 5,921 / 22,264 | 5,908 / 22,212 |

Totals independently sum to online `+94`, cross `+2,107`, candidate-exact `+24`, registry/raw `+24`. The candidate-exact increment is included in each G transition only according to the package's four-state accounting: `G` receives online+cross, while the exact blocks increment `D`. Final `G=12,820`, `D=204`, registry/raw `120/120` and total `1,460+12,820+204=14,484`.

### Complete online/cross domains and classification

I regenerated every participating 720-order catalog, residual option, positive completion, exact relation, raw selector, and zero-domain decision for all twelve online and cross stages. I actually visited all 20,820,216 literal selector cells. Separately I used exact count DPs over complete local domains, not sampling, and obtained 55,037,740,032 factorized tuples: 55,037,657,088 from the iteration-93 multi term and 82,944 from iteration 101. Every stored product, terminal-state digest, and selector stream matched.

I independently normalized every semantic key, rebuilt duplicate-old/new, dominance, evolving full-union coverage, and reverse-deletion decisions. Online: 160 raw, 94 retained. Cross: 93,200 raw, 2,107 retained. Per-iteration classification totals were:

| iter | online raw/retained | cross raw | dup-old | dup-new | dom-old | covered-union | cross retained |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 90 | 14 / 7 | 6,578 | 5,874 | 120 | 28 | 376 | 180 |
| 91 | 24 / 14 | 6,884 | 6,083 | 135 | 28 | 409 | 229 |
| 92 | 10 / 3 | 7,116 | 6,342 | 123 | 28 | 433 | 190 |
| 93 | 6 / 3 | 7,262 | 6,549 | 112 | 28 | 447 | 126 |
| 94 | 18 / 13 | 7,470 | 6,663 | 132 | 28 | 483 | 164 |
| 95 | 8 / 2 | 7,578 | 6,859 | 127 | 29 | 492 | 71 |
| 96 | 16 / 11 | 7,834 | 6,955 | 141 | 29 | 508 | 201 |
| 97 | 14 / 10 | 7,984 | 7,205 | 115 | 29 | 520 | 115 |
| 98 | 12 / 5 | 8,244 | 7,316 | 153 | 29 | 552 | 194 |
| 99 | 10 / 5 | 8,448 | 7,548 | 147 | 29 | 565 | 159 |
| 100 | 16 / 12 | 8,740 | 7,684 | 197 | 29 | 601 | 229 |
| 101 | 12 / 9 | 9,062 | 7,929 | 203 | 27 | 654 | 249 |

The online ledger additionally contains duplicate-new, dominated-new, and two covered-union candidates exactly as recorded; its row sums and evolving-install order also matched. I rebuilt 886 online pair deletion controls, 83 online multi controls, 20,163 cross controls, and the 292 whole-star controls, 21,424 in all. Each witness is in the precise relaxed candidate/relation box stated and defeats only that local deletion. All deletion-scope wording is narrow and none is used as an absence theorem.

## Frozen iteration-102 restart

The four final objects parse and reserialize to the exact hashes licensed at the beginning of this review. Counts are `G=12,820`, `D=204`, registry/raw `120/120`, total 14,484. The package contains no `cegar/iter102` work directory, process record, candidate, pending journal, or formula. The state-chain next iteration field is 102, every iteration-101 commit is complete, and no iteration-102 process appears in the process ledger. Iteration 102 was never started.

## Proof controls, rejected negatives, and absence policy

I generated a fresh pigeonhole PHP(6,5) CNF in reviewer scratch and used the sealed CaDiCaL, DRAT-trim, and LRAT checker binaries through their documented interfaces. Exact controls:

- fresh UNSAT generation: one, solver exit 20;
- valid DRAT acceptance and valid LRAT acceptance: two;
- independently corrupted DRAT and LRAT rejection: two;
- independently truncated DRAT and LRAT rejection: two;
- Gross candidate UNSAT proofs: zero.

Fresh fixture hashes were CNF `a48f6b21861b28eb862aeb78e70c4c0510fbe3770800742a07e4b9f92bc73a56`, DRAT `b6c2e560bb08c84d583ca94799951a21c8cae5de35d6d04d77bc4842e9c18ecd`, and LRAT `cf32dfff36b24ba36c3504765f29ecf3d7a8abaa59956ade4d24a4062caa6431`. I also applied all twelve schedule-collision controls and rejected a truncated direct assignment. These controls validate checker pathways. They do not convert any SAT trace or finite positive library into absence.

No accepted process returned UNSAT, UNKNOWN, or timeout; no accepted absence proof exists; no repair or branch-closure state exists. This is why a clean audit still cannot narrow `{11,12}`.

## Process, rollback, and FIX-2 audit

I parsed all 96 accepted process records and twelve driver records, verified timestamps/order, command/argument hashes, working directories, exit meanings, output hashes, and parent/child relationships. Accepted exit histogram is 72 processes with exit 0 and 24 CaDiCaL SAT processes with exit 10. There are no accepted signals, timeouts, overlapping iteration drivers, or survivors. Each stage was tentative until its exhaustive check and atomic commit.

All ten disclosed FIX-2 incidents are present and exactly bounded:

1. Whole synthesis v1: missing handling for a non-raw catalog mask; exit 1 after 7.562914750 s, RSS 1,953,562,624 B; no state mutation.
2. v2: Python 3.9 lacks `int.bit_count`; exit 1 after 7.590646792 s, RSS 1,968,340,992 B; no state mutation.
3. v3: exact quadratic column scan manually SIGTERM'd, exit -15 after 238.798085542 s, RSS 1,968,406,528 B; no mutation. The replacement uses bitsets over the same domain.
4. v4: schema-only staged experiment required synergy too early and retained zero. Its temporary `G=10,595` hash `4f8d510b7f4d510d5f8a46de7d91e88c9687089fd9238ba7930e501813e40862` was rejected and rolled back exactly to `ba4e37e48c856f8966fd86540daab423468c551289856517aacc35cc1403c8f3` before any outer run.
5. v5: reached raw 457, dominated 77, covered 54, strict 24, budget 302, then replay hit the Python 3.9 popcount site; exit 1 after 199.931826458 s, RSS 1,986,281,472 B; no installed mutation.
6. v6: accepted after portable popcount, seed-timing, and bitset-dominance corrections; 398.520581917 s, RSS 1,986,330,624 B; 24 exact strict expansions.
7. Iteration-90 v1: fresh candidate built, but independent replay rejected `.gz` versus missing plain copied Round-62 input; exit 1 after 28.604085833 s, RSS 662,192,128 B. The clean restart consumed the unchanged four-object state and reproduced exact outer SMT SHA `a67a6c3e48bd3ff9adf99ec7f0fa66240bed00b7233092e70c4b46d58ac2cd1e` and schedule SHA `88d3eb6ba8c2a2b6ac0a04660c44c405927ee598128c5458de25f4a64db0c555`.
8. Verifier v1: a removed `main()` call produced exit 0 and a zero-byte log. It is explicitly rejected; accepted verifier runs require parsed `status=PASS`.
9. Verifier v2: corrected a nonexistent live Gross path to `circdist/proof-dag/nodes/CIRCDIST.gross.yaml`. The commissioned dispatcher snapshot remained 51,391 bytes / `7e49c500c7102c7df933bb406aa88dae75c47594b9f7b956e8786c9b6278b48a`; only binding metadata changed.
10. Repository audit v1: tried to read a compressed preinventory as plain; exit 1 before scan or mutation. The accepted version transparently decompresses the exact same input.

I found no additional package-disclosed synthesis/process incident beyond these ten. A separate post-seal environment incident is correctly kept outside FIX-2: `/usr/bin/python3 verify.py --quick ...` fails immediately because system Python lacks `z3` (`ModuleNotFoundError`, exit 1, about 0.04 s, max RSS 18,415,616 B). I reproduced that rejection. It is not accepted verification. The venv-backed official quick/full runs below are the accepted corroboration.

## Verification and release controls

The sealed logs independently parse as PASS with internal walls:

- precompression quick 0.672801750 s;
- postcompression quick 7.980552125 s;
- preinstall full 862.580498750 s, reported max RSS 3,338,452,992 B;
- postcopy quick 8.266785667 s (external `/usr/bin/time` rounds to 8.321 s), five live binding assertions;
- postcopy full 847.330643 s, reported max RSS 3,338,665,984 B, mismatch zero.

The release-gate record and contemporaneous scheduler record state that a sealed hidden-path quick PASS (8.243 s) preceded the atomic rename, and the official-path quick PASS (8.321 s) followed it without package mutation. Because post-seal mutation is forbidden, those external actions are necessarily recorded outside the root payload; I checked their resulting conditions independently by relocating an exact sealed copy to a reviewer-hidden scratch path, running quick there, and rerunning quick at the official path. The relocated run returned structured PASS with five live-binding assertions in 9.078 s internally / 9.15 s externally, max RSS 2,379,972,608 B. The official-path rerun returned structured PASS with the same five assertions in 8.474 s internally / 8.53 s externally, max RSS 2,380,152,832 B. The root/payload hashes remained exact before and after.

Only after every independent mathematical gate passed, I ran the proposer full verifier as corroboration:

```text
/usr/bin/time -l "$S/venv/bin/python" "$P/verify.py" --full --repo-root "$R"
```

My first full invocation used the independent-checker environment's Z3 4.13.3 rather than the package's frozen Z3 5.1.0. It correctly rejected the iteration-90 SMT2 byte stream after 25.42 s: the version-dependent serialization hash was `150115086948e7310918637ecf63647a486a1f7ebbc680446f34d63c523d6b27` instead of stored `a67a6c3e48bd3ff9adf99ec7f0fa66240bed00b7233092e70c4b46d58ac2cd1e`. I preserved this reviewer-environment failure, created a second disposable venv from the exact `requirements.freeze.txt` (Python 3.9.6, Z3 5.1.0, NumPy 2.0.2, python-sat 1.9.dev15, psutil 7.0.0, six 1.17.0), and restarted full verification from the beginning.

The exact-freeze run returned structured PASS, internal wall 874.302 s / external real 874.38 s, maximum RSS 3,088,121,856 B, zero swaps and zero signals. It freshly passed all twelve outer rebuilds, 24 direct formulas/assignments, 120 canonical/physical raw mechanisms, 20,820,216 literal and 55,037,740,032 factorized online/cross tuples, and the complete whole-registry rebuild (138 catalogs, 1,557 relations, 606,704,944 truth cells, 304,704 literal cells, 35,294,400 factorized tuples, 24 strict witnesses). This corroborating PASS was not used to construct the independent counts above. The initial wrong-version rejection is a disclosed reviewer incident, not a package FIX-2 incident or mathematical discrepancy.

## Repository-excluding inventory and concurrent drift

I rebuilt the sealed repository-excluding inventories. Before proposer work there were 10,958 files / digest `f013dc072fd4ba87cecbca2cf034659e77d2ee221d6e663e2ba65f5bf5be4663`; preinstall 11,010 / `296288a6fabb12228ab1a1f59616127a77e52288b7fc52703f40032c0caf1405`; postcopy 11,016 / `a0acf42b811cfcdd629a4c0ed0611542635a87ed8eeee97af1d87efe934e633b`. Before-to-preinstall was 52 additions, seven changes, zero removals; before-to-postcopy 58 additions, seven changes, zero removals. All were disclosed unrelated concurrent drift.

At my first fresh scan, excluding this package, the repository had 11,031 files, 708,693,602 bytes, digest `065da0d513e64e25b1edd7f99991376627f5464be5c5860d2797cd6cdab19196`: fifteen additions and thirteen changes relative to the sealed postcopy inventory, no removals. Twelve of the changes and all fifteen additions were concurrent `holevo-extensive-violation` work (artifacts, proof-DAG nodes/index/graph, tools and README); the thirteenth change was the authorized later scheduler append. I preserved every one.

Of 23 protected bindings, 22 remained byte-exact; the sole difference was the allowed scheduler drift described above. The last pre-write repository-excluding snapshot had 11,034 files / 708,726,338 bytes / digest `7e36a7c91ede7c02bef166acbf8c8572da41e959cd18f5a64647ac6ddeaf5fd2`, or 18 additions, 13 changes, and zero removals versus sealed postcopy. Relative to my task-start metadata baseline, all 18 additions and twelve content/metadata changes were concurrent Holevo work; the scheduler already had its later authorized bytes at task start. After writing, the sole reviewer-authored delta was this review file, with no reviewer modification or removal of any baseline path. Package manifests still hashed to the accepted two seals. Reviewer scratch/venv/staging were deleted, and a final task-specific process scan found zero survivors.

## Discrepancy ledger and final scope

No load-bearing discrepancy remains.

The audit did resolve four accounting/provenance points explicitly:

1. `6,338` is the complete ordinary pair-rectangle stream; `6,346` is that stream plus eight exact two-selector terms. This gate is closed by exact concatenation and independent DP, not waived.
2. Five live-binding assertions refer to four unique objects because the review is asserted through two bindings. Every assertion is correct.
3. Later scheduler updates are control-plane drift and do not mutate the licensed iteration-90 source.
4. Historical hidden/official quick wall values are external post-seal release records; independent relocated/official reruns corroborate the immutable end state rather than pretending to recreate historical timing.

The reviewer-side scratch assertion corrections and high-memory deletion-control run are disclosed above; neither is package evidence or an inherited conclusion.

**FIX-2 determination:** satisfied. All ten development incidents and every rollback boundary are disclosed and non-load-bearing; accepted v6 and all twelve atomic iteration commits begin from exact clean states. The separate system-Python missing-z3 rejection is also disclosed and followed only by accepted venv-backed verification.

**Licensed delta:** link only this exact package, this exact review, and the exact fresh unstarted iteration-102 state as positive frontier evidence. **No inheritance:** stale/rejected seals, stale compressor rows, pending states, negative misses, SAT traces, budget exclusions, and reviewer scratch are forbidden continuation inputs.
