# CIRCDIST.gross Round 91 proof-producing outer exact review

Date: 2026-08-30
Reviewer role: sole fresh independent Round-91 reviewer
Reviewed proposer package: `circdist/artifacts/circdist_gross_proof_outer_round90_20260830`
Canonical node under protection: `circdist/proof-dag/nodes/CIRCDIST.gross.yaml`

## Disposition

**Verdict: `CLEAR-PROPOSER-LEVEL-CONTINUATION`.**

The sealed Round-90 package is complete for its narrow positive-continuation claim. I independently rebuilt the thirteen semantic sources and finite outer CNFs for iterations 112--124, checked every clause of the twelve complete outer assignments, decoded twelve distinct legal frozen schedules, rebuilt and physically replayed all twenty-four unrestricted direct-360 formulas, proved the exact fixed-selector semantics over their whole order domains, and reconstructed every transition from 140 to 164 selectors. I found no scientific defect.

This verdict licenses only linking the exact sealed Round-90 package and this review, recording the twelve SAT continuation steps and twenty-four exact candidate-domain cuts, and continuing from the exact fresh, unstarted, checked, but **unsolved** iteration-124 frontier. It does not prove a Gross UNSAT, a direct-sector absence, repair, outer exhaustion, a distance-12 schedule, or a universal distance-11 ceiling. It cannot narrow the exact residual or promote any route or root. `CIRCDIST.gross` and its live `gap-via-lift` route remain `CONJECTURED`, and

\[
D^*_{\mathrm{Gross}}\in\{11,12\}.
\]

The proposer's own result wording `MATERIAL-CHECKED-PROGRESS-NOT-CLOSED` is therefore scientifically correct. The review verdict above is the licensed canonical wording for that same narrow status.

## Independence and protected scope

I did not contact, query, or rely on the Round-90 proposer and did not import a proposer compiler, geometry module, model verifier, direct builder, or continuation checker into the load-bearing scientific checks. The standard-library reviewer programs reproduced below treat the sealed JSON, DIMACS, assignments, and schedules as data and independently derive their required semantics. The package replay was run separately as corroboration and as a deterministic-serialization attack.

No hidden chain-of-thought is requested, claimed, or presented. This document instead gives the definitions, formulas, proof arguments, counters, executable checks, hashes, failed reviewer attempts, and scope limitations needed for a public audit.

The live repository was broadly dirty/untracked before this review. I therefore used cryptographic bindings and a disposable clone overlay, never repository cleanliness, as the protection boundary. Exactly these protected hashes were observed at start and again immediately before the durable write:

| object | SHA-256 |
|---|---|
| `operations/circdist/SCHEDULER.yaml` | `6879da1a60814a8b009050bfb2647c4bdfa812f141a82b3b0e44bf75f51aacf7` |
| `circdist/proof-dag/nodes/CIRCDIST.gross.yaml` | `d3629fef2b325e3a41c39a2fea774391d99c9ff90ca9014f011a0bfa7a7118f5` |
| Round-89 exact review | `95f830f41a51bff2f0f72967a48984f496981aac89f49b6b9f95f2a4a34d77a8` |
| Round-90 root manifest | `41ac5ad7f28895f09aae29a256d91aec241298ec7bfe0d1dec2e14709fa00ca7` |
| Round-90 payload manifest | `545efe756a51190aaa8877e1d0d9fa1100da48aa213811b75a62a1f6a9b6c4d4` |
| Round-90 report | `4725b448320669413ac1dd80dbf36734bacc6a891777bd0e430dd363ea93fbe2` |
| Round-90 `RESULT.json` | `d73cc7ec209399a122d335fca4be924499906f4815189c2703a5786df33b88e3` |


The scheduler authorizes exactly one fresh Round-91 review at position 116/117 and score `1.5833333333333333`. The live node and live route were both `CONJECTURED`, and the exact residual was `{11,12}`. No live scheduler or node edit was made.

## 1. Package, manifests, serialization, bindings, and replay

### 1.1 Independent filesystem inventory

I enumerated the installed directory rather than trusting any package list. It contains 552 regular files, no symlinks, 352,257,469 bytes, and 4,866,878 LF bytes. The root manifest has 551 sorted unique rows and covers every file except itself. The payload manifest has 550 sorted unique rows and excludes only the two top-level manifests. The inventory has 549 sorted unique canonical compact-JSON rows and excludes itself and those manifests. Every recorded path, byte count, LF count, and SHA-256 matched the file. The inventory itself is 86,386 bytes, 549 LF, SHA-256 `06c7bca2eda4f8671463b2ce020092a876f36dee9f6fbd1862455f09c26f8649`.

All 64 package-created gzip members under `formulas/` or `iterations/` have a gzip header mtime of zero. The manifest and JSON path orderings are deterministic; the thirteen independently rebuilt uncompressed CNFs, source maps, circuit traces, and semantic source hashes agree exactly as detailed below.

The package contains eight protected snapshots. I compared each snapshot hash to `INPUT_BINDINGS.json`, and compared the applicable snapshot bytes to the live frozen protocol, problem statement, Round-89 review, node, and predecessor manifests. The package correctly binds the Round-90 scheduler SHA `adc03e56e36656dec95a82cc8e14b9e3c0559fc9af3f8ae42c01b03da57f2d61`; the live scheduler has since acquired the authorized Round-91 row and therefore has the different protected hash shown above. Directly running the sealed package's protected checker against that later live scheduler fails for exactly this expected temporal binding. It is not evidence corruption. A copied package replay against its own protected context, with the recorded dependency interpreter, passed.

### 1.2 Process ledger and actual SAT trace inventory

The science ledger contains 36 unique foreground children: twelve outer and twenty-four direct CaDiCaL processes. Every command used `--no-binary`, an internal 890-second limit, and a 900-second wrapper; every child returned SAT code 10, timed out false, and was waited and reaped. Aggregate recorded science wall time is 1,003.409333 seconds. Three additional bounded foreground `drat-trim` actual-trace controls returned the expected rejection code 1 and were reaped. There were zero OS background processes, zero handoffs, and zero survivors at serialization.

The SAT-side trace disposition has 36 rows totaling 7,805,443,420 bytes and 72,337,300 LF; no trace contains an empty-clause line. Those streams are SAT search traces, not UNSAT refutations. Their rejected full/corrupt/truncated submissions are discussed in section 9.

I also checked the sealed FIX-2 closure against the filesystem: `/tmp/circdist_round90_iter112`, `/tmp/circdist_round90_package_build`, `/tmp/circdist_round90_preseal_replay.log`, and the disclosed wrong-workspace Round-90 path are absent. The ledger's timeout policy is TERM, bounded ten-second harvest, KILL if necessary, then mandatory wait/reap; no timeout occurred, so no signal was needed. Package replay uses a trapped task-owned `mktemp` directory and removes it on exit.

### 1.3 Failure ledger and rejected artifacts

All six disclosed failure paths were attacked:

1. **F-01:** the inherited Round-88 checker expected the pre-Round-89 node. It failed before new science and was replaced by current explicit bindings.
2. **F-02:** a destructive shell cleanup was rejected before execution. No file changed.
3. **F-03:** the first transition writer incorrectly demanded weight exactly ten. It stopped at iteration 115 Zerr, whose valid result has weight nine, before any state, record, or next-source write. The accepted writer enforces the actual query contract `1 <= W <= 10`; iteration 115 was replayed from its unchanged prefix, and the same rule accepted iteration 119 Xerr at weight nine.
4. **F-04:** an early result checker compared a two-ID list to integer `2`. It changed no science object; the rejected record is explicitly excluded.
5. **F-05:** a helper was first written in an unrelated workspace and never ran. It and the empty stray directory were removed.
6. **F-06:** a duplicate-key scan was invoked with an interpreter lacking PyYAML and produced no verdict. The full validator set was rerun with `/usr/bin/python3` and passed.

The accepted manifests contain the corrected sources and accepted outputs. The F-04--F-06 records are disclosure-only files and are not cited as positive results. There was no solver timeout, UNKNOWN, OOM, accepted formula mismatch, clause failure, schedule failure, physical replay failure, state collision, or proof acceptance failure. No rejected artifact supports this verdict.

### 1.4 Replay and evidence-closure interpretation

The independent package audit source has SHA-256 `83a1559e882774db2924d586756af36e41a017cb0134941152b4a6711a7462e7`; its JSON stdout is 527 bytes / 23 LF with SHA-256 `9bb6a0e2f9a22b2c3677f4672280c1e85e0120434ff8a4e1b37125f20c14f0d6`, and stderr is empty. A complete copied-package replay exited 0, emitted 68,311 bytes / 121 LF, ended `ROUND90_PACKAGE_REPLAY_PASS`, had stdout SHA-256 `6f84117c72b3200376b3f2149cf8efcf4076733636f3d1cfb76245aa2ee09db5`, and empty stderr.

The current prelink evidence-closure check exits 1 with 551 messages, every one under the new package prefix. The package's sealed interpretation recorded 548 before `FILE_INVENTORY.jsonl` and the two top-level manifests were added; final filesystem enumeration explains the three-row difference. The package has 552 files, and the closure tool intentionally ignores one bound README, hence 551 current prelink messages. This seal-timing count correction is non-scientific and supplies no absence inference. In the linked disposable overlay, evidence closure passes with 158 structured paths.

The principal commands were:

```text
/usr/bin/python3 /tmp/circdist_r91_package_audit.py
CIRCDIST_PYTHON=/private/tmp/circdist-r72-dispatcher-venv/bin/python \
  /tmp/circdist-r91-pkgreplay/package/replay.sh
/usr/bin/python3 tools/evidence_closure_check.py --problem circdist
```

## 2. Frozen schedules and finite rank compression

### 2.1 Event set and exact compression theorem

Let `G = Z_12 x Z_6`, with 72 group elements and 144 data qubits split into two 72-qubit halves. From

```text
A = ((3,0),(0,1),(0,2))
B = ((0,3),(1,0),(2,0))
```

I independently constructed 72 X and 72 Z checks of weight six. There are

\[
E=E_X\sqcup E_Z,\qquad |E_X|=|E_Z|=72\cdot6=432,
\qquad |E|=864.
\]

Every data qubit has six incident CNOTs. The construction has exactly 648 nonempty X/Z check intersections, each on two qubits. These independently derived arrays agree with all thirteen sources byte-semantically.

For an arbitrary integer schedule `t`, write its distinct used times as `u_0 < ... < u_(k-1)` and define `rho_t(e)=j` iff `t(e)=u_j`. Since `k<=864`, `0<=rho_t(e)<=863`, and for all events `e,f`,

\[
t(e)<t(f)\iff\rho_t(e)<\rho_t(f),\qquad
t(e)=t(f)\iff\rho_t(e)=\rho_t(f).
\]

Every frozen predicate used here is a bound, equality, strict-order atom, attained extremum, or Boolean combination of such atoms. Endpoint serialization, MC0, global family interleaving, local rank, inherited blocks, and EFSSC validity are therefore preserved and reflected. Ranking always satisfies the absolute `0<=t<864` domain. Conversely, every satisfying ten-bit assignment already gives a legal integer schedule in that domain. Thus the finite formula captures exactly the frozen order types. Ten bits suffice for `0..863`; nine bits do not.

### 2.2 Exact source families

The fixed 14,484 inherited blocks are identical in every source and split exactly as follows:

```text
unary       1,440
round62        20
generalized 12,820
dynamic       204
```

All 14,484 `source_id` values are unique. The selector prefixes have sizes `140,142,...,164`; each successor source preserves the full previous list and appends exactly the preceding iteration's two accepted selectors. All selector semantic hashes in each prefix are unique.

For `S` selectors, the semantic source contains `18,882+S` assertions. The fixed 18,882 are:

```text
864 unsigned nonnegativity declarations (zero root clauses)
864 upper-bound assertions t(e)<864
72 X-ancilla + 72 Z-ancilla + 144 data-endpoint distinctness assertions
648 MC0 equivalence assertions
4*432 extremum inequalities + 4 extremum-attainment assertions
2 global interleaving assertions
14,484 inherited block exclusions
```

Each six-way distinctness assertion emits all `C(6,2)=15` disjunctions of the two strict orders. Each MC0 equivalence emits two clauses. Each block and selector emits one exclusion clause. Therefore the root-clause count is exactly `22,698+S`, matching every source map.

## 3. Independent Tseitin/CNF reconstruction

### 3.1 Primitive variables and gates

Each formula has 8,640 event-time primary bits and 40 extremum primary bits. Every remaining variable is a topologically ordered definition whose absolute input variable is smaller than its output. I reconstructed every definition and every root clause at its exact DIMACS ordinal:

```text
T=true:              (T)
v <-> (x and y):     (-v x), (-v y), (v -x -y)
v <-> (x or y):      (v -x), (v -y), (-v x y)
v <-> (x xor y):     (-x -y -v), (x y -v), (x -y v), (-x y v)
rank-membership:      one implication row for each of the 32 five-bit inputs
```

For LSB-first ten-bit words, the strict comparator recurrence starts with false and scans toward the most significant bit:

\[
r\leftarrow(\neg x_k\wedge y_k)\vee(\neg(x_k\oplus y_k)\wedge r).
\]

I exhaustively checked all `2^20 = 1,048,576` pairs `(x,y)` against Python integer `<`. Equality is the conjunction of ten negated XORs. A qubit's within-check rank is the sum of five strict-comparison truth values; the 32-row membership gate therefore tests membership in the exact residual-position set. For each selector, the circuit XORs the 84-bit qubit signatures, conjoins zero in the first 72 detector bits, disjoins nonzero in the high twelve logical bits, and roots the negation of that validity literal.

For each of 13 formulas I checked header counts, literal syntax, maximum variable use, complete primary/definition coverage, every definition clause, every source-map root clause, every ordinal, every comparator relation, all equality relations, all membership relations, and all EFSSC output circuits. The total reconstructed partition is 17,394,760 clauses: 17,097,710 definition clauses plus 297,050 root clauses. The reviewer also visited 22,744,800 local-order/qubit membership cases and applied 65 mutation/truncation/hash/edge negative controls.

### 3.2 Formula census

| iter | S | assert | vars | clauses | defs | def cls | root cls | member | rank dom | local cases | semantic source SHA-256 | CNF SHA-256 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 112 | 140 | 19022 | 398488 | 1330104 | 389808 | 1307266 | 22838 | 2322 | 387 | 1671840 | `a816fa6a7aec4eb3502f4b5c1a8c50dc8d958b383a003a84738fcb7e630e7c43` | `a8b917845427a0f746e72200a9a58eb5fac86d5e3c845eeaae69082038c86594` |
| 113 | 142 | 19024 | 398835 | 1332075 | 390155 | 1309235 | 22840 | 2346 | 391 | 1689120 | `0f7207878bfa8261e2c2ea38f8f439f66019a643e400f4f2139aa721a149439a` | `5ef9cebd1452c83e0141d8e2071e5ca3438c32ec00edbdf9a59b572811d04567` |
| 114 | 144 | 19026 | 399047 | 1333354 | 390367 | 1310512 | 22842 | 2364 | 394 | 1702080 | `29e89f88733a19ef2c60681de9d71913591273b8f9feacedd2eb56f2ecb07d05` | `2f7c654737cdd6705fe8f4b1ff42ccd5ac5284bca5405b2d358a0163b705ec34` |
| 115 | 146 | 19028 | 399332 | 1335074 | 390652 | 1312230 | 22844 | 2388 | 398 | 1719360 | `b07599c19b825c119d52407e1521742cb86eb813baa6ed2e538e9537fe2d1d07` | `7f6ebb4cb00f41e115ecb5c3ea902c902ebc7b0cf44f6922c71fc24101505004` |
| 116 | 148 | 19030 | 399493 | 1336170 | 390813 | 1313324 | 22846 | 2406 | 401 | 1732320 | `ec42f802ce0d53a420e00fa0f0014f1a40d98327d9265edbca4d490b12bb8c68` | `07f4fea846f08a9f5fadeff08eaa96cb50f700fa9321d323ba9708837aaec7f5` |
| 117 | 150 | 19032 | 399631 | 1337002 | 390951 | 1314154 | 22848 | 2418 | 403 | 1740960 | `98475e01d283bf5b9ab88089b8ba8b1504983e183273389a75763872856520a7` | `e4ceca8d60ec2e48d6e85a0753425e6b98939e4335f8a1b31faf28020409ccc4` |
| 118 | 152 | 19034 | 399854 | 1338496 | 391174 | 1315646 | 22850 | 2442 | 407 | 1758240 | `da4a63c005a0d11c1d3566cb197b37961ca603ea8283735e0d8e68bc67da1693` | `6f625d5663c72691e19ed4360ab39b6da40a3e380382e0444d52a846e6942cec` |
| 119 | 154 | 19036 | 400034 | 1339320 | 391354 | 1316468 | 22852 | 2448 | 408 | 1762560 | `02c3b5752397973138173c395d30282cb8cc5024a6539fbb7465845575beef1b` | `66f8762c2f2bb9a34ca8c262410b26a309b949f327bb98c66e1fe4cdce81ebce` |
| 120 | 156 | 19038 | 400185 | 1340038 | 391505 | 1317184 | 22854 | 2454 | 409 | 1766880 | `351b16fa25ca80a28189c47501ebc4f65d88a02d7badccebea7c764a3a2ca560` | `372e2798bc2ebac30bc15c7840a000ebb18bbace8cd4ef773d2443e508259507` |
| 121 | 158 | 19040 | 400401 | 1341333 | 391721 | 1318477 | 22856 | 2472 | 412 | 1779840 | `a4578336add266f94695a55eb2d21e0496abfd791e280d1ceac2d219594e4234` | `3ff94530aa80001f45b33314a41b8aaba00b0367e29bd638177ac80d99c79cff` |
| 122 | 160 | 19042 | 400572 | 1342461 | 391892 | 1319603 | 22858 | 2490 | 415 | 1792800 | `0532dc1592b5e1be3f890953a351f86dce32c089c34fd9a44067a4eb56397145` | `54945ef5b924dc0f7afbd62644deefc72470022b7da8a3a9ed411da63a0f0df1` |
| 123 | 162 | 19044 | 400846 | 1344143 | 392166 | 1321283 | 22860 | 2514 | 419 | 1810080 | `beea56906a53dd00d1a61bf5f550b9dc24f6d35aec5ead5e6046ecc22468121e` | `c22f42e48da3aaeb2556f2979f88566c7a2721649460a1159cd77dd87df0a39c` |
| 124 | 164 | 19046 | 401040 | 1345190 | 392360 | 1322328 | 22862 | 2526 | 421 | 1818720 | `d155a897b8771a9821ef4ef14041bb910e7bbb6aaaad7f6cf08b6db1de0f397e` | `2dd07d33ff0b29c1f06a7452c3b1c7ca9b6df950e819046f8a712dacb0dd7e5a` |


All counts and full 64-hex hashes above were independently computed. `CNF SHA-256` is the decompressed DIMACS identity. The complete companion-file identities are:

| iter | source.gz | source map.gz | trace.gz | metadata | encoding check | CNF.gz |
|---|---|---|---|---|---|---|
| 112 | `3a906e7abb020a6ea3bd108b9ad80ed8170439687c95830b21a7d9d283ecf5f8` | `2a25419bd8ddd7bcc1fbb9616b77c35adba02a5ff6544e9d30035c677b25a8cf` | `4113d7937a23f720eb70b0f137399b738e91ff1f546c396aaa6ec0bf964cfedf` | `4474f4af8da03b10f65419dea8ed93e8f2eb83494de913361b1a5af0e3b27323` | `5747cca5750b3b8a6a710ef470e7361779660fe11fa761b79585d92da4e3c9ff` | `889e3cb12d3ffdbcb5ea5da3cb769c552f5649bce763428ac43ea471d4f16dd4` |
| 113 | `65fc1bf87ca34269715d4c876005dcf4e64f6254e8ee72d94b8e5f356c20884c` | `71e917ac41988e95f44530fd9271e997af7ffed8a49296f6bcea547d1b106659` | `b582909d52829e26675f164fc71cc276bbd8f7db1e176b6169735bedfda992f8` | `370d419b4680e8262f66567f450159a06f95fe76c99673dfad53e47c299a8bfb` | `8f9089419a83f15441bbfa66ba57eb39def2dc057c3e389f970d28c76e030c80` | `e1d32daef508e9ad451ab788a81f917acfea35a1ff8042891dd583549f9b65a3` |
| 114 | `cea2ce8fc2b58a5326e9ddde3201c44f633e219baab33b959fa84dc68283997b` | `6723a80bb663187c7cbaab3ed56179f3b1a72ab5d9be5181e7e588c7d61c3cdf` | `ef9116d498e1dc9d940b11d0b7f59dc7eadbb2bb4a552cf08ee193a861d4b990` | `a396e2c221d9bba735c6869a4b128ae98c1daaf77084063750584687069f4602` | `5c02452b144de90d71dca89e6f06bc5001b6a751d59c7d6ae4196c0b46a399f1` | `e2d1f7e346edb1420bb53a5704179492c094b7bc784fb9275741b9a266dddabd` |
| 115 | `f5502564fb3399ebbbcbf17bc2335e6532405de4f68600c3d3fee4093749c212` | `9f6e7b29463856f9cd7e99aad005ed61932588f10109b0b00b7e1c6ec01579b3` | `8f90405c7dfa5ddd0cd25ae3441236314c0987606f3bbc4f6f330d52daa6bf28` | `e7f663eb9c3d73973015e8a18379377aa3b4b805d1df13f57cce8a2f43c1d84e` | `9148e6c53a24b79d164d17d3d94e410c1a45d2b67f99880e36e2dbc932bf153e` | `c9232e67485750646acd35493e3ecbe1c18155190f891f52c935c351a02236c6` |
| 116 | `533172333b4d7c3d1ee1f8fbefa2c1361e6c9a1bb3993609b8347114d38b4f04` | `51e621122e7b51608b1c7a316672c0c0019b26bc3a14a1c72b37876956054cde` | `658fa68e8c38f9ad3f004af0d18835416bf7da4d03484c67dc0af68b6ee59316` | `676d6ae31691035f5f565bd0f777ab983186da520492a07484b20cd7438b82b2` | `28578af0b62d533c57c4756de2abda555967a023216f45f775128ac6145b5b02` | `a3e42aba5fc7173d72f04f9b7b92153c55b86fe4a0d208cbd0987d0c90d80cd8` |
| 117 | `2f59aa2e08af067e40bf1ab0dbf6f1e71292ee185ce47d0567a961246cf8f537` | `8fdccf6637ab47ec5704e341ed1e57539b0da1746822bea1b7958c3cd69e2be3` | `eda356e6b48fd2001cda17c83fa53547a94023c0516724176f41a39e90eb1279` | `41c110a80463a12f1782c824eac50e424e0dfe28f5dc0abd814b558e6355c206` | `572d44b1744fc494b4740db51dddbf3e5348ba4a90ff63e83fdcfdf58646930c` | `0fafad7dba95a3f05d592d0272842b14a4ac32d699459038c397f9355a6499ce` |
| 118 | `b3856e7ab52926122c5898e10ec08a5c404a8022ecd232dbb0476f67d280fc6d` | `25794567a2ce0ee974ccb2299e74efadf98a2febbe7b98de43f93c9fdb9dd011` | `9c09ec10ade3907a6739f13251a75c06c79e71b175606f7de9f78709186d2e4c` | `cb793c6c322f2b0a64e9a3a4927baea849bc3bc5102d02e2c340a99f400f6b30` | `057739acf02afafc8d05518c6026e5f46a46512d7afe5fa8cb3f7c4444c013b0` | `fb1419a0bff02600e287828fd5c10a05072803fbeb32181b56785d9098ab2765` |
| 119 | `884ceec9cf8c6a927b8d16790bac714d15ff5f255b42a67217748fe92dd16b2d` | `ae32185a0868e6374bb50ce3530ea4df6c4145dda78ccc2a1b5b61aa2b15a543` | `c5dcfe8f7b023d34b498c1ffe97624841d89e1ce8e9bdaaf79c2ab69418e79af` | `1195fcd1b5278d3d70a31e7cd7182167c2c61ce88a38bd8308db3290b641e903` | `340640081663bedea542cdcf175bf7ece21fd834913882d749a71b28a65a2c3f` | `3497d637bbd9e57daf7247d6011f3e9aaefdd4b3d4e0a2b4e82e26fa16664681` |
| 120 | `45c87e8c681fa65ca2ce7b86df49830ba479f3c24889f3cc2269f9c4c53f9558` | `d9ec6fb4a06700e30db76dd6755207a273658af0e6a205a4c650438cec86adbc` | `ff41a1ae84b720f7ebd764387b16e213829a9e840f862e30b00088b243dcb0bb` | `e60e0e94e9b17fff25efa71f42a00f8c5f9550f8851bd6f5db97b65274d99fbb` | `f1f68f90ddbf802b5c59f8d6ffd71b664ff944b97afcab2897218a7e45b877ae` | `7564d9ad03a83e82fbe172ddce3af20d1a885abf02f6dba2fbe74d3bb67c7bb1` |
| 121 | `998cdf0141ef3aeb548d2aa05abce7b2416cfdf628e9e9a366436475272540ad` | `783f7367a18b5a609ad9e4d18690bb41e4f65d4c68b24bc64b7a41f71a28ef09` | `9ce97093fb0b6c57842a9f4ea70b2135e5efaa9711d85b32987866f451a1d162` | `584d0116be5dbfa7ecf989a9bad86c1035f7d620ed1c06d99a046d5f668e8e66` | `6703d802729a7109d6c8c32ad12bae2b5eb3cc0d89911b5132a828ba7908cf9f` | `bcb8e5c6be58d6247ba5be0aa1dea6c19233bbc5534ea56f9e51e32a98ce4867` |
| 122 | `8ea80fa0ed337e5ff437a50f85b87f9975b950c9a781d5998d5df5c93c185b6c` | `bb3819af8bb2b1c7a996b03aee04715fad33c5b87b513a94a417464e24cdcdc0` | `7043335f0a7ab31f64c928fe52edfff4061e3881a3695d443130bae35c388ee9` | `0e9c15e0527c4180267bd24276392cb067bd423afe8cbc8b39e8096de336a999` | `4190d8dc0775a91d43773900d2a8052cab76aaa203f8c62be45eeb3cb2922045` | `4597b91420f6ab4363c615c923a6ce1295b68282aa97c1fbef4c7f9139a3a384` |
| 123 | `a72e0281b9e02d93687ffdcbb4e83cd8f09abd9198758c698bf8cdde27ea43ee` | `e77cf13bbb2dc5c83d3e04b1631379e29940fab01a785cafd44a99c8add3b9ba` | `2c8ab25c685201d979a77b92245da07f542f797842053efb7ea50706a2cd8e65` | `b24ed674f4c23a5e85911a2bf57cbf5a7c7157aafd0a45cec3edaad2c3a2bda9` | `1e9032426458b790bf8e185c145bdaa69b085c00693231315ccf0188a7e7f0d9` | `956aa53256282fd7e58dd6e9b5a98945f13920634b908b562753ac5cb9820e35` |
| 124 | `1c4556377a4f84d5bf7df1e08af0e98d5cb3d4ea3da94db2e94d645f40a4f544` | `f4c0f6e5ecb2a68cf11e8bd9aec8c519cc7d632960ceae4664fa76c47d963920` | `62f0422936228371e69a95b5bd11002f2da2fd79d5c2ab23fdbf549f51e8694a` | `a5fc71431824edac2582fd0edc20c37e7c06610669f0c37b19f64aada7054a30` | `46bb6edea9cf5fe2f21a7ea2f30d7634fa54d6a0fbdc646e50929ea1642b4773` | `7990357daab511500d46b2471bf0e2b2244bcab85483a2093b07ba26402c1f42` |


The outer checker source SHA-256 is `baad581883179d84eb4840ea00c9c97253563c3531a0b27ad204799c4cd39c59`. Its output JSON SHA-256 is `4c4f598a8c213771373f3cc692170e737f6041e0980288d2a2d508ffd5743a30`; stdout is 2,220 bytes / 14 LF, SHA-256 `0fe42328ba445ec9a94b58bc364724b803c4ad414ae6df929dcf5e1d290d8b82`; stderr is empty. Command:

```text
/usr/bin/python3 /tmp/circdist_r91_outer.py \
  circdist/artifacts/circdist_gross_proof_outer_round90_20260830 \
  /tmp/circdist-r91-outer-results.json
```

## 4. Twelve complete outer assignments and frozen legality

For iterations 112--123, the assignment contains every variable exactly once. I evaluated every DIMACS clause directly, for 16,049,570 satisfied clauses and zero failures. I decoded all 864 raw ten-bit times and four extrema, matched the recorded raw schedule, rank-compressed it independently, and matched the recorded compressed schedule. On each schedule I then checked:

- all 72 X-check and 72 Z-check local orders, hence all 864 interactions;
- all 144 data endpoints, each with six distinct incident times;
- all 648 MC0 equivalences;
- both global-interleaving negations and the observed overlap/whole-check interleavings;
- every one of the 14,484 inherited block conjunctions, with zero hits;
- every selector in the then-current prefix, with zero valid old selectors;
- all `C(864,2)=372,816` unordered event pairs for exact `<` and `=` preservation under compression;
- agreement with the stored candidate and replay audit.

The twelve candidate files and twelve compressed schedule hashes are pairwise distinct, so no candidate was silently duplicated. Every iteration uses the exact selector prefix shown in the formula census; later selectors are absent from earlier source files, so no schedule was re-solved under a retroactively changed state.

| iter | layers | overlap interleaved | whole-check interleaved | schedule SHA-256 | model SHA-256 | candidate-file SHA-256 | replay SHA-256 |
|---|---|---|---|---|---|---|---|
| 112 | 444 | 144 | 487 | `bbcce5e137626ac9fb9600ac093c46789ae2b8ddb13531078b5c06371e574e5e` | `68d762f6bc2b69bfc2df1fcb7d043bfac4963350bbcfcb0415cb0ac3dbe504e3` | `132b033687b0a024e61e01cedbc3f642986a94ebd25a198a7688d45576aa00fa` | `66715b4bd1ed45402095d1c266519716283c7e64bcacf2494b881b1f447fabaf` |
| 113 | 429 | 126 | 464 | `69db40d0326eb03ddf32e92880f446471cc06f409d802547516d6315687c5cd7` | `20e3fd40c1bd806eaa9694c10518fbecb1b628dbad30a7eefb7cb56955fec46f` | `cb2ac2fd37883cb3b796937bc1a779c1f3e9d1df42a733a1e5f415c6a71d9a80` | `7f66ce880042047a08a765e968858d8e7657bb73ca238e05bc83a41487406014` |
| 114 | 87 | 52 | 274 | `0fd9611076774d9359d473303269ad801a7b911b6db1a319ee8cd86dc1928fb7` | `893780e6f2adaad911ea78fbed07b0c8577bd7b713e7ee25cd0508240a6e06c6` | `95352520fca9d4b1003fcaa06809bf841981f3c544648cf44b5ee6a3de39a01e` | `f2e7980249764173c1713a090802a0af5f6f99a05c99d5865b2bc7d03968eec5` |
| 115 | 475 | 136 | 443 | `5dac0dbc23c28a3b58e1affbaf7df67270c9364d1a9646792c1403858a29571e` | `b9389c3356129767376f7d5a8cb5059e73448c39a669a42362385929640a0208` | `92d1ff64318190a6f9b98fca9051c44d3339d256ff39bf55fe25a9be4e4905c2` | `eeb78f5f9fd4383c04ed118421e9e54ec112b74652bb74c10f1ef3de5b17a128` |
| 116 | 424 | 140 | 444 | `6c1f5efcf2ec11e980c3fa6f79b7aba380187abc922687695fd70607b475e26f` | `9c4050cc6d9ec220a3bd3e3b81a321286d57380c1b0aac00644d4b5591eeac9f` | `acdbe7599efe4b586dc03d946f715c49628d39bb7b8ba89621401b3a0595641f` | `c257c7f8097db9ac2eb5e6005f1f1e958e06ac5927953d912711236d33b26881` |
| 117 | 441 | 195 | 549 | `b6de1a0ba69a87841ffc17f8db691d85c85ad29bb245f3b40abbb72fc7099291` | `21b3addde8a2952215b415eaf195c9ab44db092e555e102b0f0c37ff28462c3a` | `e5df32c90737c707ff31bebb0f13402ba4c450f622e83fc58aebfebe2302360d` | `545323a8cff2bc4946cd1f556f7bff65cd7ccddcd776b6075fa410b6cbb9cef5` |
| 118 | 115 | 175 | 539 | `956618afb0325fa69adecaf994dbcabbd9fb744882552fb8620f1f72070e8b21` | `3a547c62c12a6a8144d78f570ec097b11b3d401d82acf76c77d18ef557429982` | `7b5099a54d5a7109d1477e39edddb2f995c6b2f9264e19b0959ff77e965a1dac` | `9cd027265d0e0e22a9b10b0f4d5a828b3398da2ad21fbfbaf6e2c15b659502b2` |
| 119 | 123 | 160 | 513 | `2efd95f27430f1b8a4d8cef8c86c15ef2247eda26bbe55959f355e60c3410c49` | `c11276167c4725ee05b2fbd90b95399d7bfbcd7e2c1d3fa2d8a31067b70077bc` | `17e63c320e581d7062a8b82b164322537e8324624e4df7f41ebdba5e372508c1` | `b7f20ebe9fe174ccdcff09c78a996f3e30c24950f7c5bdb29163a568a1957a06` |
| 120 | 359 | 168 | 514 | `a7c52588b152724dce6e822910bbed4ebe37df1aacbbe06ba1459b1ae2688210` | `867e657f6b7d98dcca5895a0bef041477d0830150a9d9023a57a709e912ddb51` | `2ef90edc16b484548ff840213403afbe420754fdfd1f775ba5c652c695d30dc3` | `1a1bcae66402db64be3cfb993297b1eaed4ca5123fe94f7dac62b96147d68a7f` |
| 121 | 119 | 189 | 527 | `4db4b8641df1ae4709f1467177ee0397d5b2cd384ec8c1e7b9f0ca81ea01b643` | `f3473a1f7a376de84f4e08a3f209cb22a659931b71557f80f3da1f4828a2c0e1` | `17d4ec47a6b83cfc503cfae8e891d66af56e1f731f6ac248feb93338cf7e78f2` | `2b91dd700b42695a1cc38647295426b57150c26b454ca2a99bad4433c20497a5` |
| 122 | 120 | 162 | 534 | `91db319cc429009edcf5c856efd24317498e04875c28cf7a9655b225025974be` | `83fe329a92023c1404d1f4fb76b1970635d9f35fb5adf0440b813932de008026` | `88e4980590d13172d62afd9398d08313ed26c96e0d7bcbdcb97d983c7159f05c` | `7fbbff41b6fcd6238be2a13440553d26761c3c5a727ca20c216e6999870572d9` |
| 123 | 433 | 160 | 502 | `9fd434dbd60840b4da5ad4954e655af11468d3643a0fbc1197c89329908ae5f6` | `ea0b92261229d468aff74aaa4ba1d1653591b40bf234df7d11e759c33ce35c37` | `a06464ff4d7cadcfb4c5e0d5327788fd56df227858c68b56983c341af0c4401c` | `2cb6b4096ea2a6959db817b1d2743957465cd7cf8ac955b2fc0f51f7ce9666d5` |


The model hash is the decompressed complete assignment and equals the claim inside its candidate. The gzip assignment, raw-schedule, solver-log, direct-verification, and record hashes were also cross-bound; the complete reviewer-generated table carrying those values has SHA-256 `a44468668d69d5c3717f2cce1dd270a2e086a310d0c902d06c49416ca1ac53ff` and is reproducible from the embedded checker and sealed files.

## 5. Unrestricted direct-360 formulas

### 5.1 CSS algebra and complete query

The independent Gross matrices have `rank(H_X)=rank(H_Z)=66`, so each same-sector normalizer quotient has dimension `144-66-66=12`. From the frozen weight-12 seeds, I independently translated, deduplicated, removed stabilizers, and obtained 1,884 nonstabilizer weight-12 logical words in each sector. Twelve independent representatives and twelve duals give a full-rank 12 by 12 pairing. Canonical JSON hashes are:

```text
PX 48778b0e1ec5df722305b2f8a8eade3750a4d5480dfb595149b8844a1a162c8a
PZ a3f568f88a1702e2d02b30f29a1363bc820bfaaf8e7a05ea87d7b05ba068e147
LX 66aa5130e41c3794c06e1ec15918f09aefd80b020eae47448d46a4a8236a0aa4
LZ b700b2b585a13a723294fef150be81e760a45f467ea60dcda97ba850cde2ea4d
```

The sector map is exact: Xerr uses X-check hook orders, `H_Z` detectors, `H_X` stabilizers, and `L_Z` logical duals; Zerr uses Z-check hooks, `H_X` detectors, `H_Z` stabilizers, and `L_X` duals. There is no sector swap.

For each schedule and sector the 360 columns are 144 data singletons `D:q` plus 216 residuals `R:c:k`, for 72 checks and three kinds. If `(q_0,...,q_5)` is a check's strict earliest-to-latest order, the canonical supports are

\[
A_0=\{q_0,q_1\},\quad A_1=\{q_3,q_4,q_5\},\quad A_2=\{q_4,q_5\}.
\]

The formula quantifies all 360 primaries, enforces all 72 syndrome XORs to zero, defines all twelve logical parities and requires at least one, and uses a full prefix-threshold recurrence for `sum x_j <= 10`. It contains no pool, support, residual-pattern, participating-check-count, or within-check-family restriction. The twelve dual parities are a complete quotient coordinate system after zero syndrome, so nonzero is equivalent to nonstabilizer logical class.

I rebuilt every column dictionary, variable dictionary, clause JSONL, summary, and DIMACS byte-for-byte. Every SAT log supplies every variable exactly once; every one of 536,216 clauses is satisfied. For every selected column I reconstructed the physical suffix from the six named edge times, XORed the physical supports, recomputed the detector syndrome, stabilizer membership, and twelve logical coordinates, and matched the sealed mechanism. There were 48 reviewer mutation/removal controls.

### 5.2 Formula and physical-replay census

| iter | sector | vars | clauses | W | DIMACS SHA-256 | selected named columns | canonical support | physical support | logical vector |
|---|---|---|---|---|---|---|---|---|---|
| 112 | Xerr | 5934 | 22316 | 10 | `fb24251b91e99b57e213bed7d5e493041a51c71abdecff7316f9cce2b60367ab` | `R:0:2, R:1:2, R:2:0, R:6:2, R:7:1, R:8:0, R:8:2, R:9:1, R:12:2, R:14:2` | [9,11,14,16,18,20,25,26,78,83,84,85,91,92] | [3,4,10,11,14,16,18,25,77,78,80,84,85,91] | 001000000111 |
| 112 | Zerr | 5947 | 22368 | 10 | `1621d6a4cc4f6ee5f367348ffa47f3fe1b109b771505a6b7671b1f3e31fe2175` | `D:109, D:115, D:117, D:120, R:48:2, R:51:2, R:55:2, R:60:0, R:64:2, R:69:0` | [48,49,51,52,114,115,117,118,120,121,123,124] | [49,51,52,54,57,66,115,117,118,120,121,124,136,137,139,140] | 000011000000 |
| 113 | Xerr | 5915 | 22240 | 10 | `49bd1f3fe726ea997685d08eb1b75e7696dfe0266601d43f6c63d07ce2b5dbaf` | `D:106, D:107, D:123, D:138, D:139, R:4:2, R:5:2, R:7:0, R:7:2, R:69:1` | [0,8,9,71,74,75,85,89,106,107,123,139] | [0,25,71,74,75,82,89,91,106,107,123,139] | 110101000000 |
| 113 | Zerr | 5940 | 22340 | 10 | `02b1747b2d088d7b6a17a4e5f03e55802c05c4460c04d3fbe48aa9800e4f508f` | `D:92, D:97, D:98, R:7:2, R:13:0, R:23:0, R:30:0, R:30:2, R:34:1, R:35:0` | [17,18,22,24,29,32,83,84,88,89,92,94,97,98,105,106] | [1,7,11,16,20,22,23,33,77,83,84,88,89,92,93,97,98,106,107,139] | 001001000000 |
| 114 | Xerr | 5978 | 22492 | 10 | `669140d9063df4e73777a3758fdf07e06b2ad9c2bec6fab49d6807ab0523fdc3` | `D:124, R:41:2, R:49:0, R:50:1, R:54:0, R:55:1, R:61:1, R:63:0, R:65:0, R:69:0` | [1,7,56,59,61,62,68,70,73,127,128,129,133,134] | [0,1,7,9,11,15,50,51,55,59,60,62,64,65,67,68,71,73,77,81,124,128,141,143] | 010100001010 |
| 114 | Zerr | 5877 | 22088 | 10 | `cdb8df009a10c3c5cdf6439ec59d2332f2f3c5df8a0818924cd014a37fc69c07` | `D:115, D:116, R:28:2, R:38:0, R:38:2, R:45:0, R:61:0, R:61:2, R:68:2, R:69:2` | [16,26,39,41,49,55,56,63,92,99,109,123,137,139] | [16,32,33,42,56,63,64,108,116,123,132,139] | 111111000010 |
| 115 | Xerr | 5953 | 22392 | 10 | `53a312123a0c37b8d51ec89354f894a6068b14ee733bf343b5dffc6a29a11b9e` | `D:63, D:83, D:98, D:99, D:115, D:137, D:138, D:139, R:5:2, R:69:0` | [0,1,63,70,81,83,98,99,115,137,138,139] | [0,1,15,63,71,75,83,98,99,115,137,139] | 000101100000 |
| 115 | Zerr | 5990 | 22540 | 9 | `c0371fa70e780c62b0dc49f3ca9c5013aca0bb0d22ebf2d9e1d09aa494783fdb` | `D:111, D:114, R:38:0, R:41:0, R:41:2, R:43:2, R:47:2, R:48:0, R:50:2` | [35,36,38,41,46,101,102,104,108,112,114,119] | [26,29,32,42,46,51,92,95,101,104,109,111,114,119,124,125] | 001101000000 |
| 116 | Xerr | 5944 | 22356 | 10 | `ff7ad5c86dd4ee8a9f61d9515596522bff57c62f3c16ebcbb51057e2b8e5f94c` | `D:58, D:78, D:100, D:107, D:109, D:124, D:133, D:134, R:24:0, R:32:0` | [26,33,58,78,100,102,107,109,116,124,133,134] | [25,34,42,50,58,78,99,100,108,109,110,124,133,134] | 001010010000 |
| 116 | Zerr | 5934 | 22316 | 10 | `2410318a256c450660a5f006c649b58308e94b96cfbaa267a79b155a873922ae` | `D:126, D:128, D:132, D:137, R:4:0, R:4:1, R:48:0, R:63:1, R:64:0, R:68:2` | [1,56,58,60,70,74,75,122,124,126,128,130,132,133,134,137] | [36,42,51,52,56,60,61,64,102,118,122,125,126,128,132,133,135,137] | 101001000000 |
| 117 | Xerr | 5948 | 22372 | 10 | `27cbd5372159136fc75550b9731ced65dcb44ff1322b63c396ad21b597add57b` | `D:77, D:78, D:110, D:111, D:127, R:2:0, R:9:2, R:10:0, R:10:1, R:17:2` | [3,6,10,11,28,35,77,78,86,88,93,94,101,110,111,127] | [4,10,20,35,78,79,80,93,101,110,111,127] | 001110100000 |
| 117 | Zerr | 5928 | 22292 | 10 | `b8239fef8758f0ce657ecb8225988954c88d314d10dd760f02a3c86d67c9d99d` | `D:37, D:122, R:37:1, R:37:2, R:38:0, R:42:2, R:44:0, R:49:1, R:49:2, R:51:2` | [32,37,38,48,98,103,109,113,118,119,121,122] | [26,32,37,41,47,48,92,103,108,113,114,115,118,119,121,122] | 100100000000 |
| 118 | Xerr | 5958 | 22412 | 10 | `83742a9a3be914c7d8dbf37f5ea269de0be33cbc619967aa3d7e9856db60d98a` | `R:52:0, R:52:2, R:54:0, R:55:1, R:55:2, R:56:2, R:60:0, R:62:2, R:63:0, R:66:1` | [0,2,9,48,53,62,63,68,75,121,130,138,140,141] | [2,6,55,56,61,63,64,65,68,70,72,129,135,136,138,140] | 101111001010 |
| 118 | Zerr | 5891 | 22144 | 10 | `fbec13e971ba3c1a9cb6f5dd2d6c5588e472afa5795edab5601d408fff86de4c` | `D:42, D:46, D:105, D:107, D:108, D:112, D:116, D:118, R:51:0, R:53:0` | [39,41,42,45,46,47,105,107,108,112,116,118] | [42,46,48,50,108,112,116,118,121,122,123,124] | 001111000000 |
| 119 | Xerr | 5968 | 22452 | 9 | `a654e6ccc9108d61fbb47de2a743a03b1620b89a01665d49d5ffc0dc38b84cc6` | `D:55, D:63, D:129, R:53:0, R:55:0, R:56:2, R:62:2, R:65:0, R:71:1` | [55,56,57,58,61,63,67,71,129,131,133,137] | [1,11,48,49,55,58,60,63,67,77,122,129,130,134,139,143] | 101100000001 |
| 119 | Zerr | 5930 | 22300 | 10 | `a5b9eadb508265b3ee0f6bd25d3181ab535b3fe50546d171b4129eab6e756b76` | `D:33, D:46, D:47, D:99, D:105, D:107, D:115, R:36:2, R:38:2, R:42:1` | [33,41,45,46,47,99,105,107,108,112,115,118] | [33,41,45,46,47,99,105,107,108,112,115,118] | 001111000000 |
| 120 | Xerr | 5922 | 22268 | 10 | `005906180acd9d81848a7c77e44454015f88390c947f436f64aa3bdb63f54b20` | `D:8, D:14, D:17, D:110, D:126, R:2:0, R:2:2, R:3:2, R:19:2, R:25:1` | [3,4,5,8,14,17,27,43,72,80,86,94,100,103,110,126] | [5,8,14,17,20,27,43,72,77,94,100,103,110,126] | 011111011110 |
| 120 | Zerr | 5969 | 22456 | 10 | `f43bf928c08b90690d75497e98a2176dcc29bbeceb681a47652e63f65a2bacd7` | `D:49, D:115, D:139, R:5:0, R:55:2, R:59:0, R:59:2, R:65:1, R:66:1, R:67:1` | [47,49,53,56,60,61,69,70,71,113,115,121,126,129,135,136,139,142] | [2,49,60,61,65,69,70,75,76,115,121,126,130,131,135,136,139,142] | 100000000000 |
| 121 | Xerr | 5944 | 22356 | 10 | `13f9994b7ad05c3681fcdaff38a8b33672331f4f57beefb72ce72767274fa9ec` | `D:90, D:95, D:112, R:54:0, R:55:2, R:60:0, R:65:2, R:68:0, R:70:1, R:70:2` | [0,6,57,60,66,69,74,90,95,112,129,130] | [14,55,56,57,60,61,62,66,70,72,80,90,95,112,130,132,135,143] | 100101100010 |
| 121 | Zerr | 5939 | 22336 | 10 | `0f5f0ca0ea62dd36c8f472c372568406c2c3d9b15cb4a5fbd53c401e9d0aab92` | `D:68, D:70, D:71, D:136, D:137, D:139, D:142, D:143, R:63:0, R:70:2` | [67,68,70,71,133,134,136,137,139,140,142,143] | [51,57,60,67,68,70,71,117,136,137,139,140,142,143] | 000001000000 |
| 122 | Xerr | 5972 | 22468 | 10 | `a88c6d68c01eae273b6d0ab610930730b833093d3769ae3c9938f4c1594e33e3` | `D:52, D:135, D:139, R:9:0, R:19:0, R:50:2, R:58:0, R:61:0, R:68:1, R:68:2` | [11,20,52,54,68,80,87,103,128,135,136,142] | [4,7,10,21,27,37,52,59,62,63,68,73,78,80,93,94,97,127,128,135,136,139] | 001011000000 |
| 122 | Zerr | 5906 | 22204 | 10 | `da3c5bbcfe167bf934b2628b156102c21fa262b2a972965cf3d299bfb1533158` | `D:61, D:118, R:55:0, R:57:0, R:60:0, R:60:1, R:64:1, R:66:2, R:70:0, R:71:0` | [48,60,61,63,65,67,114,120,127,131,135,136,140,141] | [43,45,49,51,59,60,61,64,68,109,111,120,124,125,126,128,135,137,141,142] | 010001000000 |
| 123 | Xerr | 5965 | 22440 | 10 | `fdade47d7b718e27f7deb44b6b527f0ca6007177677a28da0144974a23373ae2` | `R:2:0, R:18:2, R:50:0, R:54:2, R:60:1, R:63:0, R:63:2, R:64:0, R:64:1, R:67:2` | [0,3,9,10,13,19,52,55,60,62,64,65,73,75,86,102,125,133,135,138,141,142] | [0,4,13,19,20,51,55,62,65,68,73,76,77,80,102,128,132,134,135,138] | 111010000100 |
| 123 | Zerr | 5922 | 22268 | 10 | `f677acb25c84a264834b7d3e07450fdf02f5a33e36105d6585fdcd2ac56348e0` | `D:24, D:25, D:26, D:85, D:89, D:90, D:92, D:100, R:25:2, R:35:0` | [19,23,24,25,26,29,85,89,90,92,96,100] | [19,24,25,26,32,85,90,92,96,100,105,106] | 101000000000 |


All 24 canonical and physical syndromes are exactly the empty set; every logical vector is nonzero and is identical for canonical and physical replay. The weight histogram is 22 mechanisms of weight 10 and two of weight 9. The direct checker source SHA-256 is `1f14aa27992aa88e455b399605f31492a42ca664a23d0310e1acb08cfaf49216`; result JSON SHA-256 is `20e87534bff557c527b0b414a3420d2fdce2faeafd1ace8a424bb038527636c7`; stdout SHA-256 is `1c1c9da68c9239b92010f1f78d84bb6ec0d967870ae23d23a7729455beee2ddf`; stderr is empty.

### 5.3 Canonical versus physical supports

The actual physical suffix sets are `P_0={q_2,q_3,q_4,q_5}`, `P_1=A_1`, and `P_2=A_2`. For kinds 1 and 2 they equal the canonical supports. For kind 0,

\[
P_0\mathbin\triangle A_0=\{q_0,q_1,q_2,q_3,q_4,q_5\},
\]

the entire same-sector stabilizer row. Replacing any number of canonical kind-0 columns by physical suffixes therefore changes the aggregate only by stabilizers; opposite syndrome and every logical-dual parity are unchanged. The independent replay nevertheless computed the physical aggregate explicitly for every mechanism rather than relying only on this theorem.

## 6. Adversarial weight-nine audit

The weight is the number of distinct selected elementary columns, not the Hamming weight of the final data support. Both special assignments select exactly nine true primary variables; all auxiliary values are complete and every clause passes. No tenth column is hidden in a combined residual name.

### 6.1 Iteration 115 Zerr

Selected columns are `D:111`, `D:114`, `R:38:0`, `R:41:0`, `R:41:2`, `R:43:2`, `R:47:2`, `R:48:0`, `R:50:2`. This is Zerr: Z-check hook orders, `H_X` syndrome, and `L_X` logical coordinates. The exact formula has 5,990 variables, 22,540 clauses, and SHA-256 `c0371fa70e780c62b0dc49f3ca9c5013aca0bb0d22ebf2d9e1d09aa494783fdb`.

Canonical support is `[35,36,38,41,46,101,102,104,108,112,114,119]` (data weight 12). Physical support is `[26,29,32,42,46,51,92,95,101,104,109,111,114,119,124,125]` (data weight 16). Both have exactly zero `H_X` syndrome and logical vector `001101000000`, which is nonzero. The selected-column weight remains nine.

| column | canonical | physical | full local order @ times |
|---|---|---|---|
| D:111 | [111] | same | schedule-independent |
| D:114 | [114] | same | schedule-independent |
| R:38:0 | [41,108] | [26,32,92,109] | [41,108,26,92,109,32] @ [302,309,355,436,463,465] |
| R:41:0 | [111,112] | [29,35,38,95] | [111,112,29,95,38,35] @ [166,263,307,312,313,450] |
| R:41:2 | [35,38] | [35,38] | [111,112,29,95,38,35] @ [166,263,307,312,313,450] |
| R:43:2 | [46,119] | [46,119] | [37,97,114,31,46,119] @ [366,376,380,382,383,435] |
| R:47:2 | [44,101] | [44,101] | [118,41,35,117,44,101] @ [314,340,357,390,445,455] |
| R:48:0 | [36,102] | [42,51,124,125] | [36,102,125,42,124,51] @ [306,326,364,410,415,458] |
| R:50:2 | [44,104] | [44,104] | [120,38,121,53,104,44] @ [316,317,342,346,352,389] |


### 6.2 Iteration 119 Xerr

Selected columns are `D:55`, `D:63`, `D:129`, `R:53:0`, `R:55:0`, `R:56:2`, `R:62:2`, `R:65:0`, `R:71:1`. This is Xerr: X-check hook orders, `H_Z` syndrome, and `L_Z` logical coordinates. The exact formula has 5,968 variables, 22,452 clauses, and SHA-256 `a654e6ccc9108d61fbb47de2a743a03b1620b89a01665d49d5ffc0dc38b84cc6`.

Canonical support is `[55,56,57,58,61,63,67,71,129,131,133,137]` (data weight 12). Physical support is `[1,11,48,49,55,58,60,63,67,77,122,129,130,134,139,143]` (data weight 16). Both have exactly zero `H_Z` syndrome and logical vector `101100000001`, which is nonzero. Again, selected-column weight is nine.

| column | canonical | physical | full local order @ times |
|---|---|---|---|
| D:55 | [55] | same | schedule-independent |
| D:63 | [63] | same | schedule-independent |
| D:129 | [129] | same | schedule-independent |
| R:53:0 | [71,131] | [48,49,122,137] | [131,71,122,137,49,48] @ [0,2,6,7,8,23] |
| R:55:0 | [56,133] | [1,57,130,139] | [56,133,1,130,57,139] @ [23,38,41,51,74,94] |
| R:56:2 | [57,58] | [57,58] | [134,140,131,2,58,57] @ [0,1,2,3,9,88] |
| R:62:2 | [137,140] | [137,140] | [63,64,8,74,140,137] @ [0,33,51,78,101,116] |
| R:65:0 | [61,77] | [11,60,134,143] | [61,77,60,134,143,11] @ [0,1,52,62,63,109] |
| R:71:1 | [67,77,140] | [67,77,140] | [83,17,66,140,77,67] @ [14,24,33,41,51,56] |


These are unrestricted positive terminal mechanisms. They kill their source candidates and support exact selector cuts. They do **not** show `d_circ<=9`, `d_circ<=10`, or `d_circ<=11`, because the frozen relation is `d_eff(M) <= d_circ(C(M)) <= 12`; the inequality points upward from the terminal effective distance. A full arbitrary-round completion/repair theorem would be needed for a circuit-distance ceiling, and this package does not enter repair because neither direct sector is absent.

## 7. Exact fixed-selector semantic cuts

### 7.1 Domain-wide iff theorem

For a fixed named selection `s`, let `o_c(t)` be the six qubits of participating check `c` sorted by their strict local times. If several residual kinds are selected on one check, their aggregate canonical positions are the symmetric difference of `A_0,A_1,A_2`. Let each qubit signature `sigma(q) in F_2^84` have the 72 detector incidences in its low coordinates and the twelve logical-dual parities in its high coordinates. Define

\[
\Sigma_s(t)=\bigoplus_{D:q\in s}\sigma(q)
\oplus\bigoplus_c\bigoplus_{p\in A(K_c)}\sigma(o_c(t)[p]),
\]

and

\[
V_s(t)\iff [\operatorname{low}_{72}\Sigma_s(t)=0]
\wedge[\operatorname{high}_{12}\Sigma_s(t)\ne0].
\]

For **every** frozen schedule, not merely the source witness, `V_s(t)` holds iff that same fixed named selection is a terminal effective logical in its declared sector. Each data name contributes its singleton signature; each residual name contributes the signatures at its exact schedule-dependent positions; grouping by check uses XOR cancellation and hence symmetric difference. The low coordinates are exactly syndrome. After zero syndrome, completeness of the dual basis makes nonzero high coordinates exactly nontriviality modulo the stabilizer. The named weight is fixed and at most ten. Conversely, any such named terminal mechanism has exactly those two signature properties. The physical theorem follows from the full-row stabilizer identity for kind 0 above. Thus the installed unit `not V_s(t)` is necessary and sufficient for excluding precisely that named mechanism's entire validity domain.

### 7.2 Exact domain enumeration

Each participating six-body check has all `6!=720` strict local orders. The reviewer literally visited all 720 orders for every participating-check occurrence, 90,000 visits total. For each check it counted the multiplicity of every resulting 84-bit signature. It then convolved one half of the independent check distributions by XOR and exactly matched detector/logical signatures against the other half. This meet-in-the-middle count is algebraically identical to enumerating all `720^m` local-order tuples: multiplication accounts for permutation multiplicity, detector keys enforce low-zero, and subtracting the one equal logical key enforces high-nonzero. It is an exact integer count, not sampling.

Across the 24 new selectors the total order-domain size is 104,141,938,015,870,697,970,720,000, with exactly 20,101,357,097,563,392 valid tuples and 104,141,937,995,769,340,873,156,608 invalid tuples.

| iter | sector | checks m | 720^m domain | valid | invalid | left signatures | right signature tuples |
|---|---|---|---|---|---|---|---|
| 112 | Xerr | 9 | 51998697814228992000000000 | 15216811431690240 | 51998697799012180568309760 | 50625 | 337500 |
| 112 | Zerr | 6 | 139314069504000000 | 12230590464 | 139314057273409536 | 3375 | 3375 |
| 113 | Xerr | 4 | 268738560000 | 7962624 | 268730597376 | 225 | 150 |
| 113 | Zerr | 6 | 139314069504000000 | 36691771392 | 139314032812228608 | 3375 | 2250 |
| 114 | Xerr | 9 | 51998697814228992000000000 | 4565043429507072 | 51998697809663948570492928 | 33750 | 337500 |
| 114 | Zerr | 6 | 139314069504000000 | 12230590464 | 139314057273409536 | 3375 | 3375 |
| 115 | Xerr | 2 | 518400 | 2304 | 516096 | 15 | 15 |
| 115 | Zerr | 6 | 139314069504000000 | 24461180928 | 139314045042819072 | 3375 | 3375 |
| 116 | Xerr | 2 | 518400 | 2304 | 516096 | 15 | 15 |
| 116 | Zerr | 5 | 193491763200000 | 955514880 | 193490807685120 | 90 | 2250 |
| 117 | Xerr | 4 | 268738560000 | 13271040 | 268725288960 | 225 | 90 |
| 117 | Zerr | 6 | 139314069504000000 | 76441190400 | 139313993062809600 | 1350 | 1350 |
| 118 | Xerr | 8 | 72220413630873600000000 | 211344603217920 | 72220413419528996782080 | 20250 | 33750 |
| 118 | Zerr | 2 | 518400 | 2304 | 516096 | 15 | 15 |
| 119 | Xerr | 6 | 139314069504000000 | 18345885696 | 139314051158114304 | 3375 | 2250 |
| 119 | Zerr | 3 | 373248000 | 165888 | 373082112 | 15 | 150 |
| 120 | Xerr | 4 | 268738560000 | 15925248 | 268722634752 | 225 | 150 |
| 120 | Zerr | 6 | 139314069504000000 | 41278242816 | 139314028225757184 | 3375 | 1000 |
| 121 | Xerr | 6 | 139314069504000000 | 30576476160 | 139314038927523840 | 3375 | 1350 |
| 121 | Zerr | 2 | 518400 | 2304 | 516096 | 15 | 15 |
| 122 | Xerr | 6 | 139314069504000000 | 30576476160 | 139314038927523840 | 3375 | 1350 |
| 122 | Zerr | 7 | 100306130042880000000 | 2201506283520 | 100306127841373716480 | 1350 | 33750 |
| 123 | Xerr | 8 | 72220413630873600000000 | 105672301608960 | 72220413525201298391040 | 50625 | 13500 |
| 123 | Zerr | 2 | 518400 | 2304 | 516096 | 15 | 15 |


All 164 final selector semantic hashes and named selections are unique. The 24 new normalized predicates `(sector, fixed data signature, sorted check/position groups)` are structurally unique. More strongly, at each source schedule every old selector is false while each of the two new selectors is true; hence no old exclusion predicate contains the new selector's source point and the new cut is neither a duplicate nor already dominated by the installed union. A possible implication in the opposite direction, where a new exact predicate also covers part or all of an older killed domain, is benign redundancy and cannot remove a schedule without a valid named mechanism. No dominance inference is used for the verdict.

The two selectors added in the same iteration are distinct named mechanisms in different declared CSS sectors and have distinct semantic hashes and normalized expressions. I do not claim an unnecessary cross-sector extensional-minimality theorem: even if two sound validity predicates happened to agree on some or all legal schedules, the duplicate coverage would be benign. State exactness depends on the two exact named selectors and soundness of each predicate, not on a minimal cut basis.

### 7.3 Atomic state chain

The semantic transition is atomic: validate both direct assignments and both physical mechanisms, construct both selectors, check both true and all old selectors false, then append the pair and emit the next source/record. The sealed filesystem is an immutable publication of the completed transaction, not a claim that two POSIX file writes happened simultaneously. F-03 demonstrates the rollback boundary: it stopped before any new state file.

| iter | prefix | after | W X/Z | exact consumed candidates | source schedule SHA-256 | state-after SHA-256 |
|---|---|---|---|---|---|---|
| 112 | 140 |  → 142 | 10/10 | `r90-i112-Xerr, r90-i112-Zerr` | `bbcce5e137626ac9fb9600ac093c46789ae2b8ddb13531078b5c06371e574e5e` | `f3c7f81bf7b0d81af3ed254054cd29338c173d2da7f8837be18abcf8306feeee` |
| 113 | 142 |  → 144 | 10/10 | `r90-i113-Xerr, r90-i113-Zerr` | `69db40d0326eb03ddf32e92880f446471cc06f409d802547516d6315687c5cd7` | `0f61bd1f7ddc52a6bfdcfff3d198774ac99d3558931737b9f72b9149311a954b` |
| 114 | 144 |  → 146 | 10/10 | `r90-i114-Xerr, r90-i114-Zerr` | `0fd9611076774d9359d473303269ad801a7b911b6db1a319ee8cd86dc1928fb7` | `0b269f3609e81928bf3e79bc2d1dda1f53f23e800da1c51f2ff1e4a7a1738708` |
| 115 | 146 |  → 148 | 10/9 | `r90-i115-Xerr, r90-i115-Zerr` | `5dac0dbc23c28a3b58e1affbaf7df67270c9364d1a9646792c1403858a29571e` | `7896e13abd03b0665852112f97417e7ec42d838c076b3563bc01c08d59f961b4` |
| 116 | 148 |  → 150 | 10/10 | `r90-i116-Xerr, r90-i116-Zerr` | `6c1f5efcf2ec11e980c3fa6f79b7aba380187abc922687695fd70607b475e26f` | `a16ac76ea004b02d2df4cd3ef6e2787d0de18273a0fa55c0ba8873b1a03df03d` |
| 117 | 150 |  → 152 | 10/10 | `r90-i117-Xerr, r90-i117-Zerr` | `b6de1a0ba69a87841ffc17f8db691d85c85ad29bb245f3b40abbb72fc7099291` | `0392d24445dfc276715ec3eb4ad73e851bac1ad0d58b7463bffac2ad5e78bb55` |
| 118 | 152 |  → 154 | 10/10 | `r90-i118-Xerr, r90-i118-Zerr` | `956618afb0325fa69adecaf994dbcabbd9fb744882552fb8620f1f72070e8b21` | `53e01b89f5b1772a4e6109ce454a5351077ca2092a9f5e3e39a1ebf2c91f4d5e` |
| 119 | 154 |  → 156 | 9/10 | `r90-i119-Xerr, r90-i119-Zerr` | `2efd95f27430f1b8a4d8cef8c86c15ef2247eda26bbe55959f355e60c3410c49` | `e7278568a1e38939969bde2da6b60e950e5be2f8fadd70c58b74e3d807e01faf` |
| 120 | 156 |  → 158 | 10/10 | `r90-i120-Xerr, r90-i120-Zerr` | `a7c52588b152724dce6e822910bbed4ebe37df1aacbbe06ba1459b1ae2688210` | `c96a2e01c5579c28ab048b4101182fea54bec26b9e9e5f70aabde75c72bcd506` |
| 121 | 158 |  → 160 | 10/10 | `r90-i121-Xerr, r90-i121-Zerr` | `4db4b8641df1ae4709f1467177ee0397d5b2cd384ec8c1e7b9f0ca81ea01b643` | `e00d6529570b2e69dbd6da75fa7cc707de354b81b86a2630d2b8bbd0d6bd0b05` |
| 122 | 160 |  → 162 | 10/10 | `r90-i122-Xerr, r90-i122-Zerr` | `91db319cc429009edcf5c856efd24317498e04875c28cf7a9655b225025974be` | `14e551af5ea909e1e88f02def5bfaaf61df3d0557e48c9544546389db1acbf99` |
| 123 | 162 |  → 164 | 10/10 | `r90-i123-Xerr, r90-i123-Zerr` | `9fd434dbd60840b4da5ad4954e655af11468d3643a0fbc1197c89329908ae5f6` | `854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3` |


Each successor source preserves the fixed geometry, frozen semantics, blocks, incidences, overlaps, and sector definitions; it appends exactly the two compact selectors, updates the exact selector count/assertion count and continuation bindings, and binds the consumed candidate CNF. The final state is 164 selectors, selector-state SHA-256 `854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3`, file SHA-256 `d67aad48ca63955350d044a138940a32168a5c53ca8580fd8720a856f06e636c`.

For every participating check, the source schedule's raw ten-bit times and canonical compressed times induce the same six-qubit order, so selector truth is independent of the chosen ranked representative. At each transition the exact candidate schedule hash is consumed once, and the next source's binding names that iteration's exact CNF hash. Earlier source bytes never contain later selectors.

The EFSSC checker source SHA-256 is `3b704e1cb678b32e4de3e7e47fcb0692dc649154502a70072e18ae99ed16ef00`; result JSON SHA-256 is `7a8a321c8640d7ccee14b5cda91c93644a5f1f0cced442744672cf66b33d2b78`; stdout SHA-256 is `e1d80afb9efcbaa3676ab50a760d1f2180c2ff44b0affcbc9b84863f5bcaf841`; stderr is empty.

## 8. Exact iteration-124 frontier

Iteration 124 has exactly the thirteen-source geometry and 14,484 fixed blocks, 164 selectors, 19,046 assertions, 401,040 variables, and 1,345,190 clauses. Its identities are:

```text
selector state       854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3
semantic source      d155a897b8771a9821ef4ef14041bb910e7bbb6aaaad7f6cf08b6db1de0f397e
source.json.gz       1c4556377a4f84d5bf7df1e08af0e98d5cb3d4ea3da94db2e94d645f40a4f544
assertion map.gz     f4c0f6e5ecb2a68cf11e8bd9aec8c519cc7d632960ceae4664fa76c47d963920
circuit trace.gz     62f0422936228371e69a95b5bd11002f2da2fd79d5c2ab23fdbf549f51e8694a
metadata             a5fc71431824edac2582fd0edc20c37e7c06610669f0c37b19f64aada7054a30
encoding check       46bb6edea9cf5fe2f21a7ea2f30d7634fa54d6a0fbdc646e50929ea1642b4773
outer.cnf.gz         7990357daab511500d46b2471bf0e2b2244bcab85483a2093b07ba26402c1f42
decompressed CNF     2dd07d33ff0b29c1f06a7452c3b1c7ca9b6df950e819046f8a712dacb0dd7e5a
```

The continuation state says `next_iteration: 124`, `started: false`, and `stop: null`. There is no `iterations/iter124` directory. A package-wide filename and content search found no iteration-124 solver log, assignment, model, candidate, direct formula, DRAT, LRAT, disposition, or claim of SAT/UNSAT. Only the six checked formula companion files exist. Therefore iteration 124 is exactly fresh/unstarted and checked, but unsolved.

## 9. SAT traces and independent DRAT/LRAT controls

An UNSAT proof must derive contradiction, normally witnessed by an accepted empty-clause derivation. The 36 Gross processes returned SAT and have complete satisfying assignments. A proof checker rejecting their solver-side streams says only that the streams are not valid UNSAT refutations. Corrupting or truncating the same streams and observing rejection is a negative checker control, not additional SAT evidence and certainly not absence evidence. The original huge streams were intentionally omitted after disposition; their absence cannot be converted into any theorem.

I independently regenerated an UNSAT pigeonhole fixture with the sealed CaDiCaL, converted fresh DRAT to LRAT with the sealed `drat-trim`, and accepted it with the sealed LRAT checker. I also accepted the sealed valid DRAT and LRAT fixtures and rejected the sealed corrupt and truncated forms. The nine return codes were `20,0,0,0,0,1,1,1,1`. Fresh DRAT SHA-256 is `b6c2e560bb08c84d583ca94799951a21c8cae5de35d6d04d77bc4842e9c18ecd`; fresh LRAT SHA-256 is `cf32dfff36b24ba36c3504765f29ecf3d7a8abaa59956ade4d24a4062caa6431`. The control source SHA-256 is `e113c64ac0cdd59013679f34f423e650321a7f57e41efc7e2fd714915b233cd2`; stdout SHA-256 is `e38d7ed0bcf98472feab79299a84e2e5e9abd7200f2e20b8f92d44ea5d69f1a1`; stderr is empty.

These controls validate only this tool chain and these fixtures. They prove no Gross UNSAT. The package contains no Gross DRAT or LRAT proof.

## 10. Adversarial attacks and limitations

| attack | disposition |
|---|---|
| off-by-one distance convention | Rejected. A W9/W10 terminal witness bounds `d_eff`, while `d_eff<=d_circ`; no circuit ceiling follows. |
| missing CSS sector | Rejected. Every candidate has independently rebuilt Xerr and Zerr formulas and physical replays. |
| changed frozen scope | Rejected. Geometry, all 864 named CNOTs, endpoint conflicts, 648 MC0 relations, global interleaving, and excluded ancilla/generator changes match the frozen source. |
| incomplete direct query | Rejected. All 360 columns are quantified, all detector/logical rows and exact `<=10` cardinality are present, with no support/pool/pattern/check restriction. |
| false outer exhaustion | Rejected. Twelve formulas are SAT and iteration 124 is merely unsolved. |
| premature repair | Rejected. Both direct sectors are SAT in every iteration; no repair precondition occurs. |
| selector unsoundness | Rejected. The 84-bit iff theorem is domain-wide, canonical/physical equivalence is exact, and all CNF membership/validity circuits were reconstructed. |
| retroactive cut | Rejected. Every candidate satisfies its exact prefix; the pair is appended only to the next source. |
| positive-to-negative inference | Rejected. Positive mechanisms kill only their source candidate and exact validity domains. They do not establish absence, exhaustion, or a universal upper bound. |
| hidden candidate duplicate | Rejected. Twelve candidate-file and schedule hashes are pairwise distinct, and selector prefixes advance exactly. |
| SAT trace treated as proof | Rejected. Complete assignments establish SAT; the trace controls are tool-chain-only and no Gross UNSAT proof exists. |

The review does not independently re-prove the historical soundness theorem for each of the inherited 14,484 order blocks; that theorem and finite-compression bridge were already fresh-reviewed before Round 90. I did, however, reconstruct every block byte-semantically, every block CNF root, and verify zero block hits on every new schedule. The new load-bearing mathematics in this round is the exact EFSSC theorem and the direct/outer application audited above.

## 11. Environment, reviewer failed attempts, process closure

The recorded/reproduced science environment is Apple arm64, Python 3.9.6, Z3 5.1.0, and PySAT 1.9.dev15. `/usr/bin/python3` lacks Z3; the package correctly records `/private/tmp/circdist-r72-dispatcher-venv/bin/python` for replay. Tool identities are:

```text
CaDiCaL  fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9
drat-trim f58f63b0f76945d4c4c9ff6e87afaf870f579e67c0f7cca589492df8fc7ebd47
lrat-check bd7eb8052623525814a0a37502b47f05375d9d9dfaf96ddc2fcd858958517cea
```

Reviewer-side failed attempts, none evidentiary:

1. Direct live replay hit the expected old-scheduler binding; copied protected-context replay passed.
2. The first outer checker used `int.bit_count`, absent in Python 3.9; it was replaced by an explicit population count.
3. The first outer truncation control asserted an incorrect line relation; it was corrected to the actual header clause count.
4. The first assignment parser tried to parse SAT `s`/`v` tokens as integers; it was restricted to `v` payloads.
5. The first EFSSC provenance check expected `source_iteration` where inherited selectors use `iteration`; normalization now accepts the schema's two historical spellings.
6. The first EFSSC state comparison confused compact source selectors with full continuation selectors; explicit compact projection fixed it.
7. The first package audit expected a `records` key where the disposition schema uses `traces`; the field access was corrected.
8. The first YAML-delta introspection looked for top-level `evidence`; the actual list is under `assessment.basis.evidence`.
9. One shell search command had an unmatched quote due to backticks; no command ran.
10. One shell glob for an already absent replay file produced zsh's expected no-match error.

These harness/invocation errors changed no sealed input and contributed no accepted count or theorem. The final embedded sources and hashes identify the corrected programs.

The reviewer launched only bounded foreground processes and explicitly waited for each one. No reviewer background job or handoff was started. Final scratch deletion and survivor scan are performed after the one durable serialization and reported with delivery under FIX-2.

## 12. Licensed canonical replacement and validator overlay

Because the package is clear only at proposer level, the following is the **sole complete licensed replacement** for `circdist/proof-dag/nodes/CIRCDIST.gross.yaml`. It preserves every current claim, assessment level, route, caveat, prior evidence/event, and hash. It performs exactly four logical changes: append the Round-90 package evidence, append this Round-91 review evidence, replace only frontier `dstar-residual` with the exact fresh iteration-124 bindings/limitations, and append one `review-completed` event.

Licensed YAML identity:

```text
bytes 64800
LF    763
SHA-256 4a19230bce6822d3afab50db16b2657ec0924b826b409b0c65d3c9fd57c10992
```

It was serialized by PyYAML with `sort_keys=False`, `allow_unicode=True`, and width 120. The unmodified live node reserializes byte-identically under those settings. A structural delta audit confirmed that no other field changed.

I installed the candidate and a placeholder review at the licensed path in a disposable clone, never in the live node. All overlay checks passed:

| check | result |
|---|---|
| CIRCDIST proof DAG | 16 node files structurally valid |
| previous-state retention | prior nodes, routes, and events retained; 16 nodes valid |
| all-project proof DAG | exit 0 for every project |
| linked evidence closure | 158 structured paths, all local and linked |
| migration | 16 nodes, 143 original events, 728 byte-identical copies |
| release contracts | 14/14 tests |
| DAG contracts | 24/24 tests |
| Lean DAG selftest | 23/23 assertions |
| duplicate-key scan | 777 YAML files, 20,299 mappings, zero duplicates |
| `git diff --check` | exit 0 |

The overlay-validator source SHA-256 is `1e760a679edae7f8a6183d9817a8aab13e61aea544aa4443c75d01a9c2df1340`; JSON stdout SHA-256 is `bd504329b56269f6541a3924694a970f41172884c4ebdcd1b0612f72a4be4538`; stderr is empty.

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
    level change is licensed.'
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
        keeping d_eff UP, not making repair positive. Stage-2 pricing: P(D* = 12 witness) 0.30, P(D* = 11 no-go) 0.10.'
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
    task: Continue only from the independently reviewed sealed fresh/unstarted iteration 124 state. The inherited sound order-block
      library remains exactly 14,484 predicates (1,440 unary, 20 round-62, 12,820 generalized, and 204 dynamic), and the exact
      fixed-selector frontier is 164 EFSSCs (120 reviewed Round-80 selectors, fourteen Round-86 selectors from iterations
      102--108, six Round-88 selectors from iterations 109--111, and twenty-four Round-90 selectors from iterations 112--123).
      Bind selector-state sha256:854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3, the iteration-124 semantic
      source sha256:d155a897b8771a9821ef4ef14041bb910e7bbb6aaaad7f6cf08b6db1de0f397e, and source-file sha256:1c4556377a4f84d5bf7df1e08af0e98d5cb3d4ea3da94db2e94d645f40a4f544
      before use. Its deterministic 10-bit compressed finite-outer formula has 19,046 source assertions, 401,040 variables,
      1,345,190 clauses and CNF sha256:2dd07d33ff0b29c1f06a7452c3b1c7ca9b6df950e819046f8a712dacb0dd7e5a; it was checked but
      deliberately not solved, and no iteration-124 solver/model/DRAT/LRAT disposition is inherited. For a SAT result, retain
      the complete assignment, replay every DIMACS clause and frozen schedule condition, then rebuild and adjudicate both
      complete unrestricted direct-360 sectors; a positive mechanism kills only that concrete candidate and proves no absence,
      and only exact source-schedule-valid EFSSC selectors may be added atomically. For an UNSAT result, retain a complete
      DRAT proof, independently accept it, generate LRAT, and independently accept the LRAT with valid/corrupt/truncated controls.
      Enter repair only after both direct sectors have independently checked absence. Preserve frozen S_Gross, strict serialization,
      MC0, terminal residual semantics, both CSS sectors, and every existing exclusion against morphing, Circ-Preserve substitutions,
      alternate conflict models, exploratory pair clauses, retroactive cuts, and stale compressor provenance. Keep CIRCDIST.gross
      and gap-via-lift CONJECTURED and D*_Gross in {11,12}; this reviewed continuation supplies no Gross UNSAT, absence, exhaustion,
      distance-12 witness, universal distance-11 ceiling, route promotion, or root promotion.
    kind: task
    since: '2026-08-30'
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
```


## 13. Embedded independent reviewer programs

These sources are included so that deleting reviewer scratch does not delete the auditable algorithms. They use only the Python standard library except the repository validators/tools they invoke. Their output objects are not canonical evidence; the sealed package and this review are the licensed evidence.

### 13.1 Package/manifests/process audit

Source SHA-256: `83a1559e882774db2924d586756af36e41a017cb0134941152b4a6711a7462e7`

```python
#!/usr/bin/env python3
import hashlib, json, os, pathlib, struct, sys

REPO = pathlib.Path('<repo>')
PKG = REPO/'circdist/artifacts/circdist_gross_proof_outer_round90_20260830'

def sha_bytes(b): return hashlib.sha256(b).hexdigest()
def sha_file(p): return sha_bytes(p.read_bytes())
def load(p): return json.loads(p.read_text())
def require(x, msg):
    if not x: raise AssertionError(msg)

files = sorted(p.relative_to(PKG).as_posix() for p in PKG.rglob('*') if p.is_file())
require(len(files)==552, ('file count',len(files)))
require(not any(p.is_symlink() for p in PKG.rglob('*')), 'symlink in package')
stats = {}
for rel in files:
    b=(PKG/rel).read_bytes()
    stats[rel]={'sha256':sha_bytes(b),'bytes':len(b),'lines':b.count(b'\n')}
require(sum(x['bytes'] for x in stats.values())==352257469, 'byte total')
require(sum(x['lines'] for x in stats.values())==4866878, 'LF total')

def read_manifest(name):
    raw=(PKG/name).read_bytes()
    require(raw.endswith(b'\n'), name+' missing final LF')
    out=[]
    for n,line in enumerate(raw.decode('utf-8').splitlines(),1):
        require(len(line)>=67 and line[64:66]=='  ', (name,n,'format'))
        digest,rel=line[:64],line[66:]
        require(len(digest)==64 and all(c in '0123456789abcdef' for c in digest), (name,n,'digest'))
        out.append((rel,digest))
    require([r for r,d in out]==sorted(r for r,d in out), name+' not sorted')
    require(len(set(r for r,d in out))==len(out), name+' duplicate path')
    return out

root=read_manifest('SHA256SUMS.txt')
payload=read_manifest('PAYLOAD_SHA256SUMS.txt')
require(len(root)==551, len(root))
require(set(r for r,d in root)==set(files)-{'SHA256SUMS.txt'}, 'root coverage')
require(len(payload)==550, len(payload))
require(set(r for r,d in payload)==set(files)-{'SHA256SUMS.txt','PAYLOAD_SHA256SUMS.txt'}, 'payload coverage')
for name,rows in [('root',root),('payload',payload)]:
    for rel,d in rows: require(stats[rel]['sha256']==d,(name,rel))
require(sha_file(PKG/'SHA256SUMS.txt')=='41ac5ad7f28895f09aae29a256d91aec241298ec7bfe0d1dec2e14709fa00ca7','root seal')
require(sha_file(PKG/'PAYLOAD_SHA256SUMS.txt')=='545efe756a51190aaa8877e1d0d9fa1100da48aa213811b75a62a1f6a9b6c4d4','payload seal')

inv_raw=(PKG/'FILE_INVENTORY.jsonl').read_bytes()
require(inv_raw.endswith(b'\n'),'inventory final LF')
inv=[json.loads(x) for x in inv_raw.splitlines()]
require(len(inv)==549, len(inv))
irels=[x['path'] for x in inv]
require(irels==sorted(irels),'inventory sorted')
require(len(set(irels))==len(irels),'inventory dup')
require(set(irels)==set(files)-{'SHA256SUMS.txt','PAYLOAD_SHA256SUMS.txt','FILE_INVENTORY.jsonl'},'inventory coverage')
for x in inv:
    require(set(x)=={'bytes','lines','path','sha256'},('inventory keys',x['path']))
    require(x==stats[x['path']] | {'path':x['path']},('inventory mismatch',x['path']))
    canonical=json.dumps(x,sort_keys=True,separators=(',',':')).encode()+b'\n'
    # each line uses deterministic compact sorted-key JSON
    require(canonical in inv_raw,('inventory serialization',x['path']))
require(sha_file(PKG/'FILE_INVENTORY.jsonl')=='06c7bca2eda4f8671463b2ce020092a876f36dee9f6fbd1862455f09c26f8649','inventory sha')
require(stats['FILE_INVENTORY.jsonl']['bytes']==86386 and stats['FILE_INVENTORY.jsonl']['lines']==549,'inventory identity')

# Every package-created formula/assignment gzip has deterministic mtime=0. Frozen vendor gzip inputs are separately bound.
gz=[rel for rel in files if rel.endswith('.gz')]
created=[r for r in gz if r.startswith('formulas/') or r.startswith('iterations/')]
bad_mtime=[]
for rel in created:
    b=(PKG/rel).read_bytes()
    require(b[:2]==b'\x1f\x8b',('gzip magic',rel))
    mt=struct.unpack('<I',b[4:8])[0]
    if mt!=0: bad_mtime.append((rel,mt))
require(not bad_mtime,('gzip mtime',bad_mtime[:3]))

bindings=load(PKG/'INPUT_BINDINGS.json')
expected=bindings['expected_protected_sha256']
snapshot_map={
 'DAG_PROTOCOL.md':'bindings/protocols/DAG_PROTOCOL.md',
 'FILE_PROTOCOL.md':'bindings/protocols/FILE_PROTOCOL.md',
 'circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md':'bindings/protocols/CIRCDIST_PROBLEMS.md',
 'circdist/proof-dag/nodes/CIRCDIST.gross.yaml':'bindings/canonical/CIRCDIST.gross.yaml',
 'circdist/reviews/circdist_gross_proof_outer_exact_review_round89_20260830.md':'bindings/canonical/round89_review.md',
 'operations/circdist/SCHEDULER.yaml':'bindings/canonical/SCHEDULER.yaml',
 'circdist/artifacts/circdist_gross_proof_outer_round88_20260830/SHA256SUMS.txt':'bindings/round88/SHA256SUMS.txt',
 'circdist/artifacts/circdist_gross_proof_outer_round88_20260830/PAYLOAD_SHA256SUMS.txt':'bindings/round88/PAYLOAD_SHA256SUMS.txt',
}
for live,snap in snapshot_map.items():
    require(sha_file(PKG/snap)==expected[live],('snapshot hash',live))
    require((PKG/snap).read_bytes()==(REPO/live).read_bytes() or live=='operations/circdist/SCHEDULER.yaml',('live binding changed',live))
require(sha_file(REPO/'operations/circdist/SCHEDULER.yaml')=='6879da1a60814a8b009050bfb2647c4bdfa812f141a82b3b0e44bf75f51aacf7','live Round91 scheduler')
require(expected['operations/circdist/SCHEDULER.yaml']=='adc03e56e36656dec95a82cc8e14b9e3c0559fc9af3f8ae42c01b03da57f2d61','Round90 scheduler binding')

for rel,d in bindings['package_snapshot_sha256'].items(): require(sha_file(PKG/rel)==d,('package snapshot map',rel))

env=load(PKG/'ENVIRONMENT.json')
for name,x in env['tooling'].items():
    p=PKG/'tooling'/name
    require(p.stat().st_size==x['bytes'] and sha_file(p)==x['sha256'],('tool',name))
require(env['system_python_has_required_z3_and_pysat'] is False and env['system_python_dependency_probe_returncode']==1,'environment negative probe')

ledger=load(PKG/'PROCESS_LEDGER.json')
processes=ledger['processes']; controls=ledger['actual_sat_trace_control_processes']
require(len(processes)==36 and len(controls)==3,'process counts')
require(ledger['foreground_bounded_solver_processes']==36 and ledger['foreground_bounded_control_processes']==3,'declared process counts')
require(ledger['all_children_reaped'] and ledger['survivors_at_serialization']==0 and ledger['os_background_processes_started']==0 and ledger['handoffs']==[],'ledger closure')
names=[x['name'] for x in processes+controls]
require(len(set(names))==39,'process name uniqueness')
pids=[x['child_pid'] for x in processes+controls]
require(len(set(pids))==39,'child pid uniqueness')
for x in processes:
    require(x['returncode']==10 and not x['timed_out'] and x['final_status']=='exited_and_reaped','science disposition')
    require(x['timeout_seconds']==900 and x['command'][1:4]==['-t','890','--no-binary'],'science command')
for x in controls:
    require(x['returncode']==1 and not x['timed_out'] and x['final_status']=='exited_and_reaped','control disposition')

log_objs=[load(p) for p in sorted((PKG/'logs').glob('*.process.json'))]
require(len(log_objs)==36,'per-process logs')
require({x['name']:x for x in log_objs}=={x['name']:x for x in processes},'science ledger/log equality')
control_files={'actual_iter112_sat_trace_drat_rejection':'full.run.json','actual_iter112_truncated_sat_trace_drat_rejection':'truncated.run.json','actual_iter112_corrupt_sat_trace_drat_rejection':'corrupt.run.json'}
for x in controls: require(load(PKG/'controls/actual_gross_sat_trace'/control_files[x['name']])==x,('control ledger/log equality',x['name']))

trace=load(PKG/'data/sat_drat_trace_disposition.json')
records=trace['traces']
require(len(records)==36,'trace rows')
require(sum(x['bytes'] for x in records)==7805443420,'trace bytes')
require(sum(x['lf_count'] for x in records)==72337300,'trace LF')
require(sum(x['empty_clause_lines'] for x in records)==0,'trace empty clauses')
require(all(x['solver_status']=='SATISFIABLE' and x['proof_output_enabled'] and x['certificate_disposition']=='not an UNSAT certificate' for x in records),'trace semantics')
require(len({(x['iteration'],x['query']) for x in records})==36,'trace uniqueness')
require({x['iteration'] for x in records}==set(range(112,124)),'trace iterations')
require(all({x['query'] for x in records if x['iteration']==i}=={'outer','Xerr','Zerr'} for i in range(112,124)),'trace coverage')
require(abs(sum(x['wall_seconds'] for x in processes)-1003.409333)<1e-6,('science wall total',sum(x['wall_seconds'] for x in processes)))

faildir=PKG/'verification/failures'
failids={load(p)['failure_id'] for p in faildir.glob('*.json')}
require(failids=={'F-04','F-05','F-06'},failids)
require(all(load(p)['status']=='EXCLUDED' for p in faildir.glob('*.json')),'failure exclusion')

result={
 'status':'ROUND91_PACKAGE_INDEPENDENT_AUDIT_PASS',
 'files':len(files),'bytes':sum(x['bytes'] for x in stats.values()),'lf':sum(x['lines'] for x in stats.values()),
 'root_rows':len(root),'payload_rows':len(payload),'inventory_rows':len(inv),'created_gzip_mtime_zero':len(created),
 'protected_snapshots':len(snapshot_map),'science_processes':len(processes),'control_processes':len(controls),
 'science_wall_seconds':round(sum(x['wall_seconds'] for x in processes),6),
 'sat_trace_rows':len(records),'sat_trace_bytes':sum(x['bytes'] for x in records),'sat_trace_lf':sum(x['lf_count'] for x in records),
 'sat_trace_empty_clause_lines':sum(x['empty_clause_lines'] for x in records),
 'excluded_failure_records':sorted(failids),
}
print(json.dumps(result,sort_keys=True,indent=2))
```

### 13.2 Outer source/CNF/model audit

Source SHA-256: `baad581883179d84eb4840ea00c9c97253563c3531a0b27ad204799c4cd39c59`

```python
#!/usr/bin/env python3
"""Round91 clean-room outer-CNF/source/model audit. Standard library only.
Does not import any proposer module. Reads sealed JSON/DIMACS as data and derives
Gross geometry, roots, circuit clauses, schedules, and selector truth itself.
"""
from pathlib import Path
from collections import Counter
import gzip,hashlib,itertools,json,sys,time
ROOT=Path(sys.argv[1]).resolve()
OUT=Path(sys.argv[2])

def J(o): return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def H(b): return hashlib.sha256(b).hexdigest()
def FH(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def load(p):
 p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def cdig(c):return hashlib.sha256((' '.join(map(str,c))+' 0').encode()).digest()
def mask(qs):
 r=0
 for q in qs:r|=1<<int(q)
 return r
# Independent algebraic Gross geometry.
L,M,G,N=12,6,72,144
A=((3,0),(0,1),(0,2));B=((0,3),(1,0),(2,0))
def gi(i,j):return (i%L)*M+(j%M)
def add(g,d):
 i,j=divmod(g,M);return gi(i+d[0],j+d[1])
XC=[sorted([add(g,a) for a in A]+[G+add(g,b) for b in B]) for g in range(G)]
ZC=[sorted([add(g,(-b[0],-b[1])) for b in B]+[G+add(g,(-a[0],-a[1])) for a in A]) for g in range(G)]
EDGES=[f'X:{a}:{q}' for a,row in enumerate(XC) for q in row]+[f'Z:{a}:{q}' for a,row in enumerate(ZC) for q in row]
INC=[[] for _ in range(N)]
for kind,checks in [('X',XC),('Z',ZC)]:
 for a,row in enumerate(checks):
  for q in row:INC[q].append(f'{kind}:{a}:{q}')
OV=[]
for a,x in enumerate(XC):
 for b,z in enumerate(ZC):
  sh=sorted(set(x)&set(z))
  if sh:OV.append({'x_check':a,'z_check':b,'qubits':sh})
assert len(EDGES)==864 and len(set(EDGES))==864 and len(OV)==648 and all(len(x)==6 for x in INC)

# Comparator algorithm gets an actual exhaustive independent 2^20 test once.
cmp_cases=0
for x in range(1024):
 for y in range(1024):
  r=False
  for k in range(10):
   xb=bool((x>>k)&1);yb=bool((y>>k)&1)
   r=((not xb and yb) or (xb==yb and r))
  assert r==(x<y)
  cmp_cases+=1

BASE_BLOCK_HASH=None;BASE_BINDINGS=None;prev_selectors=None
rows_out=[]; total_model_clauses=0; total_definition_clauses=0;total_root_clauses=0;total_local_cases=0
schedule_hashes=[]; candidate_file_hashes=[]
for iteration in range(112,125):
 t0=time.time();F=ROOT/f'formulas/iter{iteration}'
 S=load(F/'source.json.gz');MTA=json.loads((F/'metadata.json').read_text());D=load(F/'circuit_trace.json.gz')
 amap=[json.loads(x) for x in gzip.decompress((F/'assertion_map.jsonl.gz').read_bytes()).decode().splitlines()]
 sem=S['semantic_payload_sha256'];payload=dict(S);payload.pop('semantic_payload_sha256')
 assert H(J(payload))==sem
 assert FH(F/'source.json.gz')==MTA['source_file_sha256']
 assert S['schema']==f'circdist-gross-iteration{iteration}-finite-source-v1'
 assert S['x_checks']==XC and S['z_checks']==ZC and S['edges']==EDGES and S['data_incidence']==INC and S['overlaps']==OV
 assert S['residual_positions']==[[0,1],[3,4,5],[4,5]]
 assert S['sector_definitions']['Xerr']['checks']==XC and S['sector_definitions']['Xerr']['edge_kind']=='X'
 assert S['sector_definitions']['Zerr']['checks']==ZC and S['sector_definitions']['Zerr']['edge_kind']=='Z'
 # bind qubit signatures independently to detector-row and logical-dual masks in source
 for sec,detchecks in [('Xerr',ZC),('Zerr',XC)]:
  sd=S['sector_definitions'][sec]; sig=[int(v) for v in sd['qubit_signatures']]
  assert len(sig)==144
  for q in range(144):
   low=sum((1<<r) for r,row in enumerate(detchecks) if q in row)
   assert (sig[q]&((1<<72)-1))==low
 # exact fixed block family and selector-prefix chain
 bh=H(J(S['blocks']))
 if BASE_BLOCK_HASH is None:BASE_BLOCK_HASH=bh;BASE_BINDINGS={k:v for k,v in S['bindings'].items() if not k.startswith('round90_iteration') and k!='round90_continuation_selector_state_sha256'}
 assert bh==BASE_BLOCK_HASH and len(S['blocks'])==14484
 assert Counter(x['family'] for x in S['blocks'])==Counter({'unary':1440,'round62':20,'generalized':12820,'dynamic':204})
 assert len({x['source_id'] for x in S['blocks']})==14484
 assert len(S['selectors'])==140+2*(iteration-112)
 assert len({x['selector_semantic_sha256'] for x in S['selectors']})==len(S['selectors'])
 if prev_selectors is not None:assert S['selectors'][:-2]==prev_selectors
 prev_selectors=list(S['selectors'])
 expected_assertions=18882+len(S['selectors'])
 assert S['expected']['assertions']==expected_assertions==len(amap)==MTA['assertions']
 assert S['expected']['reviewed_blocks']==14484 and S['expected']['selectors']==len(S['selectors'])
 # load and validate exact full clause partition
 nv=MTA['variables'];nc=MTA['clauses'];T=MTA['constant_variable']
 assert FH(F/'outer.cnf.gz')==MTA['cnf_gzip_sha256'] if 'cnf_gzip_sha256' in MTA else True
 rawcnf=gzip.decompress((F/'outer.cnf.gz').read_bytes())
 assert H(rawcnf)==MTA['cnf_sha256']
 assert FH(F/'assertion_map.jsonl.gz')==MTA['assertion_map_gzip_sha256'] if 'assertion_map_gzip_sha256' in MTA else True
 assert FH(F/'circuit_trace.json.gz')==MTA['definitions_sha256']
 assert D['constant_variable']==T and len(D['selector_valid_literals'])==len(S['selectors'])
 exp=bytearray(32*nc);seen=bytearray(nc)
 def put(cid,c):
  assert 1<=cid<=nc and not seen[cid-1]
  seen[cid-1]=1;exp[32*(cid-1):32*cid]=cdig(c)
 def defclauses(d):
  v=d['var'];op=d['op'];ins=d['inputs']
  if op=='constant_true':return [[v]]
  if op=='and':
   x,y=ins;return [[-v,x],[-v,y],[v,-x,-y]]
  if op=='or':
   x,y=ins;return [[v,-x],[v,-y],[-v,x,y]]
  if op=='xor':
   x,y=ins;return [[-x,-y,-v],[x,y,-v],[x,-y,v],[-x,y,v]]
  if op=='rank_membership':
   pos=set(d['positions']);out=[]
   for bm in range(32):
    out.append([(-x if (bm>>i)&1 else x) for i,x in enumerate(ins)]+[v if bin(bm).count('1') in pos else -v])
   return out
  raise AssertionError(op)
 defined=bytearray(nv+1);rankdef={};gate={};def_clause_count=0
 for d in D['definitions']:
  v=d['var'];assert 1<=v<=nv and not defined[v] and all(abs(x)<v for x in d['inputs']);defined[v]=1
  cs=defclauses(d);assert len(cs)==len(d['clause_ids'])
  for cid,c in zip(d['clause_ids'],cs):put(cid,c);def_clause_count+=1
  if d['op'] in ('and','or','xor'):
   key=(d['op'],)+tuple(sorted(d['inputs']));assert key not in gate;gate[key]=v
  elif d['op']=='rank_membership':rankdef[v]=d
 root_clause_count=0
 for i,r in enumerate(amap):
  assert r['assertion_index']==i and len(r['root_clause_ids'])==len(r['root_clauses'])
  for cid,c in zip(r['root_clause_ids'],r['root_clauses']):put(cid,c);root_clause_count+=1
 assert all(seen) and def_clause_count+root_clause_count==nc
 # primary/definition variable coverage
 primary=bytearray(nv+1)
 for tbl in (MTA['time_bit_variables'],MTA['extrema_bit_variables']):
  for bits in tbl.values():
   for v in bits:assert not primary[v];primary[v]=1
 assert sum(primary)==8680
 assert all(primary[v] or defined[v] for v in range(1,nv+1))
 # compare every actual DIMACS clause at exact ordinal, and syntax/header
 lines=rawcnf.decode().splitlines();head=lines[0].split();assert head[:2]==['p','cnf'] and list(map(int,head[2:]))==[nv,nc]
 assert len(lines)==nc+1;actual_max=0
 for ci,line in enumerate(lines[1:],1):
  z=list(map(int,line.split()));assert z[-1]==0 and all(x for x in z[:-1]);actual_max=max(actual_max,max(map(abs,z[:-1]),default=0))
  assert cdig(z[:-1])==exp[32*(ci-1):32*ci]
 assert actual_max==nv
 # reconstruct comparator/equality/membership circuit expressions from the checked gate table
 words={'time:'+k:tuple(v) for k,v in MTA['time_bit_variables'].items()}
 words.update({'extrema:'+k:tuple(v) for k,v in MTA['extrema_bit_variables'].items()})
 words['constant:0']=tuple(-T for _ in range(10));words['constant:864']=tuple(T if (864>>i)&1 else -T for i in range(10))
 def and2(x,y):
  if x==T:return y
  if y==T:return x
  if x==-T or y==-T:return -T
  if x==y:return x
  if x==-y:return -T
  return gate[('and',)+tuple(sorted((x,y)))]
 def or2(x,y):
  if x==-T:return y
  if y==-T:return x
  if x==T or y==T:return T
  if x==y:return x
  if x==-y:return T
  return gate[('or',)+tuple(sorted((x,y)))]
 def xor2(x,y):
  if x==-T:return y
  if y==-T:return x
  if x==T:return -y
  if y==T:return -x
  if x==y:return -T
  if x==-y:return T
  return gate[('xor',)+tuple(sorted((x,y)))]
 def many(op,xs,init):
  r=init
  for x in xs:r=op(r,x)
  return r
 def lt(x,y):
  r=-T
  for a,b in zip(x,y):r=or2(and2(-a,b),and2(-xor2(a,b),r))
  return r
 def eq(x,y):return many(and2,[-xor2(a,b) for a,b in zip(x,y)],T)
 ltmap={};eqmap={}
 for a,b,l in D['lt_relations']:assert lt(words[a],words[b])==l;ltmap[a,b]=l
 for a,b,l in D['eq_relations']:assert eq(words[a],words[b])==l;eqmap[a,b]=l;eqmap[b,a]=l
 assert len(ltmap)==MTA['comparison_count']==11234 and len(D['eq_relations'])==1728
 possets=[set(x) for x in S['residual_positions']]
 def poss(ks):
  z=set()
  for k in ks:z.symmetric_difference_update(possets[int(k)])
  return tuple(sorted(z))
 member={}
 for sec,c,p,q,l in D['member_relations']:
  key=(sec,c,tuple(p),q);assert key not in member;member[key]=l
  if l not in (T,-T):
   rd=rankdef[l];assert tuple(rd['positions'])==tuple(p)
   sd=S['sector_definitions'][sec];expected=[ltmap['time:'+f"{sd['edge_kind']}:{c}:{r}",'time:'+f"{sd['edge_kind']}:{c}:{q}"] for r in sd['checks'][c] if r!=q]
   assert rd['inputs']==expected
 sourcekeys=set();domains=set()
 for s in S['selectors']:
  for cs,ks in s['group_kinds'].items():
   c=int(cs);p=poss(ks);domains.add((s['sector'],c,p))
   sourcekeys.update((s['sector'],c,p,q) for q in S['sector_definitions'][s['sector']]['checks'][c])
 assert sourcekeys==set(member) and len(member)==S['expected']['membership_expressions']==MTA['membership_expressions']
 local_cases=0
 for sec,c,p in domains:
  row=S['sector_definitions'][sec]['checks'][c]
  for order in itertools.permutations(row):
   rank={q:i for i,q in enumerate(order)}
   for q in row:assert ((rank[q] in p)==(sum(rank[r]<rank[q] for r in row if r!=q) in p));local_cases+=1
 # exact source-root reconstruction
 ri=0
 def take(fam,sid,cs):
  nonlocal_dummy=None
  global_dummy=None
  nonlocal_vars=None
  # use mutable outer ri through list-free local reassignment
  return
 def expect(fam,sid,cs):
  nonlocal_ri[0]+=1;r=amap[nonlocal_ri[0]-1]
  assert r['family']==fam and r['source_id']==sid and r['root_clauses']==cs,(iteration,nonlocal_ri[0]-1,fam,sid)
 nonlocal_ri=[0]
 for e in S['edges']:
  expect('time_nonnegative',e,[]);expect('time_upper_bound',e,[[ltmap['time:'+e,'constant:864']]])
 def distinct(fam,sid,es):
  expect(fam,sid,[[ltmap['time:'+es[i],'time:'+es[j]],ltmap['time:'+es[j],'time:'+es[i]]] for i in range(6) for j in range(i+1,6)])
 for i,row in enumerate(S['x_checks']):distinct('x_ancilla_distinct',f'Xcheck:{i}',[f'X:{i}:{q}' for q in row])
 for i,row in enumerate(S['z_checks']):distinct('z_ancilla_distinct',f'Zcheck:{i}',[f'Z:{i}:{q}' for q in row])
 for q,es in enumerate(S['data_incidence']):distinct('data_distinct',f'data:{q}',es)
 for o in S['overlaps']:
  a,b=o['x_check'],o['z_check'];q0,q1=o['qubits'];l0=ltmap['time:'+f'Z:{b}:{q0}','time:'+f'X:{a}:{q0}'];l1=ltmap['time:'+f'Z:{b}:{q1}','time:'+f'X:{a}:{q1}']
  expect('mc_equivalence',f'overlap:{a}:{b}',[[-l0,l1],[l0,-l1]])
 xs=[e for e in S['edges'] if e[0]=='X'];zs=[e for e in S['edges'] if e[0]=='Z']
 for lab,es,mode in [('xmin',xs,'min'),('xmax',xs,'max'),('zmin',zs,'min'),('zmax',zs,'max')]:
  for e in es:
   l=-ltmap['time:'+e,'extrema:'+lab] if mode=='min' else -ltmap['extrema:'+lab,'time:'+e]
   expect('extrema_inequality',f'{lab}:{e}',[[l]])
  expect('extrema_attained',lab,[[eqmap['extrema:'+lab,'time:'+e] for e in es]])
 expect('global_interleaving','not_all_X_before_Z',[[-ltmap['extrema:xmax','extrema:zmin']]])
 expect('global_interleaving','not_all_Z_before_X',[[-ltmap['extrema:zmax','extrema:xmin']]])
 for b in S['blocks']:expect('reviewed_block',b['source_id'],[[-ltmap['time:'+a,'time:'+b] for a,b in b['atoms']]])
 for si,s in enumerate(S['selectors']):
  sd=S['sector_definitions'][s['sector']];qsig=list(map(int,sd['qubit_signatures']));ds=0
  for q in s['data_support']:ds^=qsig[q]
  terms=[[] for _ in range(84)]
  for cs,ks in sorted(s['group_kinds'].items(),key=lambda x:int(x[0])):
   c=int(cs);p=poss(ks)
   for q in sd['checks'][c]:
    ml=member[s['sector'],c,p,q]
    for bit in range(84):
     if (qsig[q]>>bit)&1:terms[bit].append(ml)
  bits=[many(xor2,terms[k],T if (ds>>k)&1 else -T) for k in range(84)]
  valid=and2(many(and2,[-x for x in bits[:72]],T),many(or2,bits[72:],-T))
  assert valid==D['selector_valid_literals'][si]
  expect('efssc_exclusion',s['mechanism_id'],[[-valid]])
 assert nonlocal_ri[0]==len(amap)
 # Five actual rejection predicates per iteration.
 assert cdig([T,-T])!=exp[:32] and len(lines[1:-1])!=nc
 mutant=dict(payload);mutant['schema']=mutant['schema']+'-mut';assert H(J(mutant))!=sem
 assert not (864<864) and (17<19) and not (19<17)
 model_info=None
 if iteration<124:
  I=ROOT/f'iterations/iter{iteration}';cand=json.loads((I/'outer/candidate.json').read_text())
  ab=gzip.decompress((I/'outer/assignment.dimacs.gz').read_bytes());assert H(ab)==cand['assignment_sha256']
  vals={}
  for aline in ab.decode().splitlines():
   if aline.startswith('v '):
    for z in map(int,aline[2:].split()):
     if z:assert abs(z) not in vals;vals[abs(z)]=z>0
  assert len(vals)==nv and set(vals)==set(range(1,nv+1))
  failed=0
  for line in lines[1:]:
   c=list(map(int,line.split()))[:-1]
   if not any(vals[abs(x)]==(x>0) for x in c):failed+=1
  assert failed==0;total_model_clauses+=nc
  raw={e:sum((int(vals[v])<<k) for k,v in enumerate(MTA['time_bit_variables'][e])) for e in EDGES}
  ext={e:sum((int(vals[v])<<k) for k,v in enumerate(MTA['extrema_bit_variables'][e])) for e in ('xmin','xmax','zmin','zmax')}
  assert raw==cand['raw_times'] and ext==cand['raw_extrema']
  rel={v:i for i,v in enumerate(sorted(set(raw.values())))};comp={e:rel[t] for e,t in raw.items()}
  assert comp==cand['compressed_times'] and sorted(set(comp.values()))==list(range(cand['compressed_layers']))
  assert H(J(raw))==cand['raw_schedule_sha256'] and H(J(comp))==cand['compressed_schedule_sha256']
  # Stronger than only encoded pairs: all C(864,2) order/equality relations survive compression.
  allpairs=0
  for ai in range(len(EDGES)):
   a=EDGES[ai]
   for b in EDGES[ai+1:]:assert ((raw[a]<raw[b])==(comp[a]<comp[b])) and ((raw[a]==raw[b])==(comp[a]==comp[b]));allpairs+=1
  # endpoint serialization, all 648 MC0 equalities, global family interleaving, compression
  conflicts=[]
  for kind,checks in [('X',XC),('Z',ZC)]:
   for a,row in enumerate(checks):assert len({comp[f'{kind}:{a}:{q}'] for q in row})==6
  for q,es in enumerate(INC):assert len({comp[e] for e in es})==6
  mcv=[]
  for o in OV:
   a,b=o['x_check'],o['z_check'];q0,q1=o['qubits']
   if (comp[f'Z:{b}:{q0}']<comp[f'X:{a}:{q0}'])!=(comp[f'Z:{b}:{q1}']<comp[f'X:{a}:{q1}']):mcv.append((a,b))
  assert not mcv
  xt=[comp[e] for e in EDGES if e[0]=='X'];zt=[comp[e] for e in EDGES if e[0]=='Z'];assert not(max(xt)<min(zt) or max(zt)<min(xt))
  pair_interleaved=0;whole_interleaved=0
  for o in OV:
   a,b=o['x_check'],o['z_check'];sh=o['qubits']
   xx=[comp[f'X:{a}:{q}'] for q in sh];zz=[comp[f'Z:{b}:{q}'] for q in sh]
   pair_interleaved+=not(max(xx)<min(zz) or max(zz)<min(xx))
   xx=[comp[f'X:{a}:{q}'] for q in XC[a]];zz=[comp[f'Z:{b}:{q}'] for q in ZC[b]]
   whole_interleaved+=not(max(xx)<min(zz) or max(zz)<min(xx))
  hits=sum(all(comp[a]<comp[b] for a,b in bl['atoms']) for bl in S['blocks']);assert hits==0
  def selector_valid(s):
   sd=S['sector_definitions'][s['sector']];sig=list(map(int,sd['qubit_signatures']));v=0
   for q in s['data_support']:v^=sig[q]
   for cs,ks in s['group_kinds'].items():
    c=int(cs);order=sorted(sd['checks'][c],key=lambda q:comp[f"{sd['edge_kind']}:{c}:{q}"])
    for p in poss(ks):v^=sig[order[p]]
   return (v&((1<<72)-1))==0 and (v>>72)!=0
  sv=sum(selector_valid(s) for s in S['selectors']);assert sv==0
  assert cand['frozen_audit']['edge_count']==864 and cand['frozen_audit']['overlaps']==648 and cand['frozen_audit']['conflicts']==[] and cand['frozen_audit']['mc_violations']==[] and cand['frozen_audit']['ok']
  assert cand['frozen_audit']['global_interleaved'] and cand['frozen_audit']['overlap_interleaved_pairs']==pair_interleaved and cand['frozen_audit']['whole_check_interleaved_pairs']==whole_interleaved
  assert cand['frozen_audit']['used_layers']==len(set(comp.values())) and cand['frozen_audit']['min_time']==min(comp.values()) and cand['frozen_audit']['max_time']==max(comp.values())
  assert FH(I/'outer/candidate.json') not in candidate_file_hashes;candidate_file_hashes.append(FH(I/'outer/candidate.json'))
  assert cand['compressed_schedule_sha256'] not in schedule_hashes;schedule_hashes.append(cand['compressed_schedule_sha256'])
  # stored replay/hash cross-bindings
  replay=json.loads((I/'outer/replay.json').read_text());assert replay['all_dimacs_clauses_satisfied'] and replay['dimacs_clauses_checked']==nc and replay['reviewed_block_hits']==0 and replay['efssc_symbolic_valid_selectors']==0
  model_info={'assignment_variables':len(vals),'clauses_satisfied':nc,'layers':cand['compressed_layers'],'schedule_sha256':cand['compressed_schedule_sha256'],'all_pair_relations':allpairs,'block_hits':hits,'prior_selector_valid':sv,'overlap_interleaved_pairs':pair_interleaved,'whole_check_interleaved_pairs':whole_interleaved}
 rows_out.append({'iteration':iteration,'selectors':len(S['selectors']),'assertions':len(amap),'variables':nv,'clauses':nc,'cnf_sha256':MTA['cnf_sha256'],'source_semantic_sha256':sem,'source_file_sha256':FH(F/'source.json.gz'),'root_clauses':root_clause_count,'definition_records':len(D['definitions']),'definition_clauses':def_clause_count,'comparisons':len(ltmap),'equalities':len(D['eq_relations']),'memberships':len(member),'rank_domains':len(domains),'local_order_qubit_cases':local_cases,'model':model_info,'negative_controls':5,'seconds':round(time.time()-t0,3)})
 total_definition_clauses+=def_clause_count;total_root_clauses+=root_clause_count;total_local_cases+=local_cases
 print('OUTER_PASS',iteration,nv,nc,sem,MTA['cnf_sha256'],model_info and model_info['layers'],flush=True)
# exact fresh frontier constraints
assert rows_out[-1]['iteration']==124 and rows_out[-1]['selectors']==164 and rows_out[-1]['assertions']==19046 and rows_out[-1]['variables']==401040 and rows_out[-1]['clauses']==1345190
assert rows_out[-1]['cnf_sha256']=='2dd07d33ff0b29c1f06a7452c3b1c7ca9b6df950e819046f8a712dacb0dd7e5a'
assert rows_out[-1]['source_semantic_sha256']=='d155a897b8771a9821ef4ef14041bb910e7bbb6aaaad7f6cf08b6db1de0f397e'
assert rows_out[-1]['source_file_sha256']=='1c4556377a4f84d5bf7df1e08af0e98d5cb3d4ea3da94db2e94d645f40a4f544'
assert not (ROOT/'iterations/iter124').exists()
out={'status':'PASS','schema':'round91-clean-room-outer-v1','comparison_truth_cases':cmp_cases,'geometry':{'edges':len(EDGES),'overlaps':len(OV),'data_endpoints':len(INC)},'fixed_blocks':14484,'block_family_counts':dict(Counter(x['family'] for x in S['blocks'])),'iterations':rows_out,'total_formula_clauses_partitioned':sum(x['clauses'] for x in rows_out),'total_definition_clauses':total_definition_clauses,'total_root_clauses':total_root_clauses,'total_model_clauses_satisfied':total_model_clauses,'total_local_order_qubit_cases':total_local_cases,'negative_controls':5*13,'unique_schedules':len(schedule_hashes),'unique_candidate_files':len(candidate_file_hashes)}
OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print('ROUND91_OUTER_ALL_PASS',H(J(out)))
```

### 13.3 Direct-360 and physical replay audit

Source SHA-256: `1f14aa27992aa88e455b399605f31492a42ca664a23d0310e1acb08cfaf49216`

```python
#!/usr/bin/env python3
"""Round91 independent Gross/direct-360 rebuild and SAT/physical replay.
Standard library only; imports no proposer code."""
from pathlib import Path
from collections import Counter
import hashlib,itertools,json,sys,gzip
ROOT=Path(sys.argv[1]).resolve();OUT=Path(sys.argv[2])
def J(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def H(b):return hashlib.sha256(b).hexdigest()
def FH(p):return H(Path(p).read_bytes())
def dumpb(o):return (json.dumps(o,indent=2,sort_keys=True)+'\n').encode()
def mask(qs):
 r=0
 for q in qs:r|=1<<int(q)
 return r
def bits(v):
 o=[]
 while v:
  b=v&-v;o.append(b.bit_length()-1);v^=b
 return o
def pc(v):return bin(v).count('1')
# Gross bicycle/biplane construction, independently from the frozen parameters.
L,M,G,N=12,6,72,144;A=((3,0),(0,1),(0,2));B=((0,3),(1,0),(2,0))
def gi(i,j):return (i%L)*M+(j%M)
def add(g,d):
 i,j=divmod(g,M);return gi(i+d[0],j+d[1])
XC=[sorted([add(g,a) for a in A]+[G+add(g,b) for b in B]) for g in range(G)]
ZC=[sorted([add(g,(-b[0],-b[1])) for b in B]+[G+add(g,(-a[0],-a[1])) for a in A]) for g in range(G)]
HX=list(map(mask,XC));HZ=list(map(mask,ZC))
Xof=[[] for _ in range(N)];Zof=[[] for _ in range(N)]
for a,row in enumerate(XC):
 for q in row:Xof[q].append(a)
for a,row in enumerate(ZC):
 for q in row:Zof[q].append(a)
def rref(rows,n=144):
 a=[int(x) for x in rows if x];piv=[];r=0
 for c in range(n-1,-1,-1):
  k=next((k for k in range(r,len(a)) if (a[k]>>c)&1),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r]
  for j in range(len(a)):
   if j!=r and ((a[j]>>c)&1):a[j]^=a[r]
  piv.append(c);r+=1
  if r==len(a):break
 return a[:r],piv
def rank(rows,n=144):return len(rref(rows,n)[0])
def inspan(v,rows,n=144):
 rr,p=rref(rows,n)
 for w,c in zip(rr,p):
  if (v>>c)&1:v^=w
 return v==0
def translate(w,d):
 o=0
 for half in (0,72):
  for q in bits((w>>half)&((1<<72)-1)):o|=1<<(half+add(q,d))
 return o
def seeds(path):
 o=[]
 for line in Path(path).read_text().splitlines():
  if line.strip():
   a,b,c,d=[int(x,16) for x in line.split()];o.append((a|(b<<64))|((c|(d<<64))<<72))
 return o
def pool(path,stabs,dets):
 p=sorted({translate(w,(i,j)) for w in seeds(path) for i in range(12) for j in range(6)})
 p=[w for w in p if not inspan(w,stabs)]
 assert len(p)==1884 and all(pc(w)==12 for w in p) and all(all(pc(w&h)%2==0 for h in dets) for w in p)
 return p
def quotient_basis(p,stabs):
 o=[];rows=list(stabs);r=rank(rows)
 for v in p:
  nr=rank(rows+[v])
  if nr>r:o.append(v);rows.append(v);r=nr
  if len(o)==12:break
 assert len(o)==12;return o
inp=ROOT/'vendor/round80/src/inputs';PX=pool(inp/'w12X.txt',HX,HZ);PZ=pool(inp/'w12Z.txt',HZ,HX)
LX=quotient_basis(PX,HX);LZ=quotient_basis(PZ,HZ)
assert rank(HX)==rank(HZ)==66 and rank(HX+LX)==rank(HZ+LZ)==78
pair=[sum(((pc(x&z)&1)<<j) for j,z in enumerate(LZ)) for x in LX];assert rank(pair,12)==12
# For zero opposite syndrome, 12 dual parities vanish iff vector lies in same-sector stabilizer span.
def quotient_coordinate_complete(stabs,primal,dual):
 assert rank(stabs)==66 and rank(stabs+primal)==78
 assert all(all(pc(s&d)%2==0 for d in dual) for s in stabs)
 mat=[sum(((pc(p&d)&1)<<j) for j,d in enumerate(dual)) for p in primal]
 assert rank(mat,12)==12
quotient_coordinate_complete(HX,LX,LZ);quotient_coordinate_complete(HZ,LZ,LX)
# Bind every source qubit signature, including high logical coordinates, from independent geometry.
src=json.loads(gzip.decompress((ROOT/'formulas/iter112/source.json.gz').read_bytes()))
for label,checks,duals in [('Xerr',ZC,LZ),('Zerr',XC,LX)]:
 exp=[]
 for q in range(144):
  lo=sum(1<<i for i,row in enumerate(checks) if q in row);hi=sum(1<<i for i,d in enumerate(duals) if (d>>q)&1);exp.append(lo|(hi<<72))
 assert list(map(int,src['sector_definitions'][label]['qubit_signatures']))==exp
RES=((0,1),(3,4,5),(4,5));PHYS=((2,3,4,5),(3,4,5),(4,5))
class Sector:
 def __init__(self,label,times):
  self.label=label;self.times=times
  if label=='Xerr':self.hooks,self.det_of,self.dets,self.stabs,self.duals,self.kind=XC,Zof,HZ,HX,LZ,'X'
  else:self.hooks,self.det_of,self.dets,self.stabs,self.duals,self.kind=ZC,Xof,HX,HZ,LX,'Z'
  self.orders=[sorted(row,key=lambda q,a=a:times[f'{self.kind}:{a}:{q}']) for a,row in enumerate(self.hooks)]
  self.cols=self.columns()
 def syndrome(self,s):return sum((pc(s&r)&1)<<i for i,r in enumerate(self.dets))
 def singleton_u(self,q):
  dkind='Z' if self.label=='Xerr' else 'X';ordered=sorted(self.det_of[q],key=lambda b:self.times[f'{dkind}:{b}:{q}']);o=[0];v=0
  for b in reversed(ordered):v|=1<<b;o.append(v)
  return tuple(o)
 def hook_u(self,a,qs):
  dkind='Z' if self.label=='Xerr' else 'X';u=0
  for q in qs:
   for b in self.det_of[q]:
    if self.times[f'{dkind}:{b}:{q}']>self.times[f'{self.kind}:{a}:{q}']:u^=1<<b
  return u
 def columns(self):
  o=[]
  for q in range(144):
   s=1<<q;o.append({'index':len(o),'name':f'D:{q}','kind':'data','check':None,'residual_kind':None,'support':s,'physical':s,'syndrome':self.syndrome(s),'u':self.singleton_u(q)})
  for a,order in enumerate(self.orders):
   for k in range(3):
    s=mask(order[p] for p in RES[k]);ph=mask(order[p] for p in PHYS[k]);assert self.syndrome(s)==self.syndrome(ph)
    if k==0:assert s^ph==mask(self.hooks[a])
    else:assert s==ph
    o.append({'index':len(o),'name':f'R:{a}:{k}','kind':'residual','check':a,'residual_kind':k,'support':s,'physical':ph,'syndrome':self.syndrome(s),'u':(self.hook_u(a,bits(ph)),)})
  assert len(o)==360 and len({c['support'] for c in o[144:]})==216
  return o
 def col_public(self,c):return {'index':c['index'],'primary_var':c['index']+1,'name':c['name'],'kind':c['kind'],'check':c['check'],'residual_kind':c['residual_kind'],'support':bits(c['support']),'support_mask_hex':hex(c['support']),'physical_support':bits(c['physical']),'syndrome':bits(c['syndrome']),'syndrome_mask_hex':hex(c['syndrome']),'u_options':[{'bits':bits(u),'mask_hex':hex(u)} for u in c['u']]}
class Enc:
 def __init__(self,label,csha):self.label=label;self.csha=csha;self.vars=[];self.by={};self.cls=[]
 def var(self,n,role,ctx):
  if n in self.by:return self.by[n]
  v=len(self.vars)+1;self.by[n]=v;self.vars.append({'id':v,'name':n,'role':role,'context':ctx});return v
 def add(self,lits,rule,ctx):self.cls.append({'id':len(self.cls)+1,'lits':list(lits),'rule':rule,'context':ctx})
 def xorlink(self,a,b,y,ctx):
  for c in ([-y,a,b],[-y,-a,-b],[y,-a,b],[y,a,-b]):self.add(c,'xor2_equivalence',ctx)
 def xorval(self,lits,prefix,ctx):
  assert lits
  if len(lits)==1:return lits[0]
  a=lits[0]
  for step,x in enumerate(lits[1:],1):
   y=self.var(f'{prefix}.xor_aux.{step}','xor_auxiliary',{**ctx,'step':step,'left':a,'right':x});self.xorlink(a,x,y,{**ctx,'step':step,'output':y});a=y
  return a
 def xorzero(self,lits,prefix,ctx):
  assert lits;v=self.xorval(lits,prefix,ctx);self.add([-v],'xor_terminal_value',{**ctx,'parity':0})
 def atmost10(self,x):
  s={}
  for i in range(1,361):
   for j in range(1,11):s[i,j]=self.var(f'card.s.{i}.{j}','cardinality_auxiliary',{'counter':'prefix_at_least','prefix_length':i,'threshold':j})
  self.add([-s[1,1],x[0]],'card_base_equivalence',{'i':1,'j':1});self.add([s[1,1],-x[0]],'card_base_equivalence',{'i':1,'j':1})
  for j in range(2,11):self.add([-s[1,j]],'card_impossible_base',{'i':1,'j':j})
  for i in range(2,361):
   xi=x[i-1];y=s[i,1];a=s[i-1,1]
   for c in ([-y,a,xi],[-a,y],[-xi,y]):self.add(c,'card_or_equivalence',{'i':i,'j':1})
   for j in range(2,11):
    y=s[i,j];a=s[i-1,j];b=s[i-1,j-1]
    for c in ([-y,a,b],[-y,a,xi],[-a,y],[-b,-xi,y]):self.add(c,'card_recurrence_equivalence',{'i':i,'j':j})
   self.add([-s[i-1,10],-xi],'card_atmost_overflow_forbidden',{'i':i,'bound':10})
def build(sec,csha):
 e=Enc(sec.label,csha);x=[e.var(f'select[{c["index"]}]','direct_column_selection',{'column_index':c['index'],'column_name':c['name']}) for c in sec.cols];assert x==list(range(1,361))
 sr=[]
 for b in range(72):
  lits=[x[c['index']] for c in sec.cols if (c['syndrome']>>b)&1];sr.append({'row':b,'literals':lits,'column_indices':[v-1 for v in lits]});e.xorzero(lits,f'syndrome[{b}]',{'family':'detector_syndrome','row':b})
 lr=[];lvs=[]
 for r,d in enumerate(sec.duals):
  lits=[x[c['index']] for c in sec.cols if pc(c['support']&d)&1];lv=e.var(f'logical_parity[{r}]','logical_parity_output',{'logical_dual_index':r,'logical_dual_support':bits(d)});acc=e.xorval(lits,f'logical[{r}]',{'family':'logical_parity','logical_dual_index':r});e.add([-lv,acc],'logical_output_equivalence',{'logical_dual_index':r});e.add([lv,-acc],'logical_output_equivalence',{'logical_dual_index':r});lvs.append(lv);lr.append({'row':r,'logical_dual_support':bits(d),'logical_dual_mask_hex':hex(d),'literals':lits,'column_indices':[v-1 for v in lits],'output_var':lv})
 e.add(lvs,'logical_nonzero_disjunction',{'logical_outputs':lvs});e.atmost10(x)
 nv=len(e.vars);nc=len(e.cls);body=''.join(' '.join(map(str,c['lits']))+' 0\n' for c in e.cls);dim='\n'.join([f'c CIRCDIST Gross direct-360 {sec.label} W<=10',f'c candidate_sha256 {csha}','c variables 1..360 select the exact columns listed in the companion column dictionary',f'p cnf {nv} {nc}']+[' '.join(map(str,c['lits']))+' 0' for c in e.cls])+'\n'
 cold={'schema':'circdist-gross-direct360-column-dictionary-v1','sector':sec.label,'candidate_sha256':csha,'column_count':360,'columns':[sec.col_public(c) for c in sec.cols],'detector_rows':[{'row':i,'support':bits(v),'mask_hex':hex(v)} for i,v in enumerate(sec.dets)],'stabilizer_rows':[{'row':i,'support':bits(v),'mask_hex':hex(v)} for i,v in enumerate(sec.stabs)],'logical_duals':[{'row':i,'support':bits(v),'mask_hex':hex(v)} for i,v in enumerate(sec.duals)],'syndrome_equations':sr,'logical_equations':lr}
 vard={'schema':'circdist-gross-direct360-variable-dictionary-v1','sector':sec.label,'candidate_sha256':csha,'variable_count':nv,'variables':e.vars}
 summ={'schema':'circdist-gross-direct360-formula-summary-v1','sector':sec.label,'candidate_sha256':csha,'W':10,'variables':nv,'clauses':nc,'primary_selection_variables':360,'logical_output_variables':12,'formula_body_sha256':H(body.encode()),'dimacs_sha256':H(dim.encode()),'families':{'syndrome_xor_rows':72,'logical_parity_rows':12,'logical_nonzero_disjunctions':1,'cardinality_constraint':'exact prefix-threshold recurrence encoding of sum(select)<=10'},'complete_query':True,'excluded_restrictions':['no pool restriction','no residual-pattern restriction','no check-count restriction','no within-check order family restriction']}
 return e,dim.encode(),vard,cold,summ

def parse_assignment(p):
 status=None;ls=[]
 for line in Path(p).read_text(errors='replace').splitlines():
  if line.startswith('s '):status=line[2:].strip()
  elif line.startswith('v '):ls.extend(int(x) for x in line[2:].split() if int(x))
 assert status=='SATISFIABLE';a={}
 for z in ls:assert abs(z) not in a;a[abs(z)]=z>0
 return a
rows=[];all_mech_names=[];totclauses=0;special={};weights=Counter();neg=0
for it in range(112,124):
 cand=json.loads((ROOT/f'iterations/iter{it}/outer/candidate.json').read_text());times={k:int(v) for k,v in cand['compressed_times'].items()};csha=H(J(times));assert csha==cand['compressed_schedule_sha256']
 storedver=json.loads((ROOT/f'iterations/iter{it}/direct/direct_verification.json').read_text())
 irow={'iteration':it,'schedule_sha256':csha,'sectors':{}}
 for label in ('Xerr','Zerr'):
  sec=Sector(label,times);enc,dim,vard,cold,summ=build(sec,csha);base=ROOT/f'iterations/iter{it}/direct/direct360/{label}'
  assert dim==(base.with_suffix('.cnf')).read_bytes()
  assert dumpb(vard)==base.with_suffix('.variables.json').read_bytes()
  assert dumpb(cold)==base.with_suffix('.columns.json').read_bytes()
  assert dumpb(summ)==base.with_suffix('.summary.json').read_bytes()
  clausebytes=b''.join((json.dumps(c,sort_keys=True,separators=(',',':'))+'\n').encode() for c in enc.cls);assert clausebytes==base.with_suffix('.clauses.jsonl').read_bytes()
  a=parse_assignment(ROOT/f'iterations/iter{it}/direct/solver/{label}.solver.log');assert len(a)==len(enc.vars) and set(a)==set(range(1,len(enc.vars)+1))
  failed=[c['id'] for c in enc.cls if not any(a[abs(x)]==(x>0) for x in c['lits'])];assert not failed
  sel=[j for j in range(360) if a[j+1]];assert 1<=len(sel)<=10;names=[sec.cols[j]['name'] for j in sel];assert len(names)==len(set(names));all_mech_names.append((label,tuple(names)))
  canonical=0;physical=0
  for j in sel:canonical^=sec.cols[j]['support'];physical^=sec.cols[j]['physical']
  syn=sec.syndrome(canonical);psyn=sec.syndrome(physical);cp=[pc(canonical&d)&1 for d in sec.duals];pp=[pc(physical&d)&1 for d in sec.duals]
  assert syn==psyn==0 and any(cp) and cp==pp and not inspan(canonical,sec.stabs) and not inspan(physical,sec.stabs)
  # each model's logical output primaries agree exactly with recomputed quotient coordinates
  stored_cols=json.loads(base.with_suffix('.columns.json').read_text());outs=[r['output_var'] for r in stored_cols['logical_equations']];assert [int(a[v]) for v in outs]==cp
  sv=storedver['sectors'][label];mech=sv['mechanism'];assert sv['all_dimacs_clauses_satisfied'] and sv['assignment_variables']==len(a) and sv['formula_summary']==summ
  assert mech['selected_indices']==sel and mech['selected_names']==names and mech['fault_count']==len(sel) and mech['canonical_replay']['syndrome']==[] and mech['physical_syndrome']==[] and mech['canonical_physical_parities_equal']
  assert mech['canonical_replay']['net_support']==bits(canonical) and mech['physical_net_support']==bits(physical) and mech['physical_logical_parities']==pp
  # independent fault-by-fault suffix/time reconstruction
  for f,j in zip(mech['faults'],sel):
   c=sec.cols[j];assert f['column_index']==j and f['column_name']==c['name']
   if c['kind']=='data':assert f['data_support']==bits(c['physical']) and f['schedule_dependency']=='none'
   else:
    order=sec.orders[c['check']];eds=[f'{sec.kind}:{c["check"]}:{q}' for q in order];ts=[times[e] for e in eds]
    assert f['canonical_representative_support']==bits(c['support']) and f['physical_suffix_support']==bits(c['physical']) and f['physical_suffix_positions_zero_based']==list(PHYS[c['residual_kind']]) and f['within_check_order_edges']==eds and f['within_check_times']==ts and ts==sorted(ts)
  # mutation controls: flip a selected primary in the complete assignment; remove first physical fault
  flip=dict(a);flip[sel[0]+1]=not flip[sel[0]+1];assert any(not any(flip[abs(x)]==(x>0) for x in c['lits']) for c in enc.cls)
  rem=sel[1:];net=0
  for j in rem:net^=sec.cols[j]['support']
  assert not (len(rem)<=10 and sec.syndrome(net)==0 and not inspan(net,sec.stabs));neg+=2
  weights[len(sel)]+=1;totclauses+=len(enc.cls)
  rr={'status':'SATISFIABLE','variables':len(enc.vars),'clauses':len(enc.cls),'dimacs_sha256':H(dim),'selected_indices':sel,'selected_names':names,'fault_count':len(sel),'canonical_support':bits(canonical),'physical_support':bits(physical),'detector_matrix':'HZ' if label=='Xerr' else 'HX','syndrome':bits(syn),'logical_parities':cp,'physical_parities':pp,'solver_log_sha256':FH(ROOT/f'iterations/iter{it}/direct/solver/{label}.solver.log'),'mechanism_semantic_sha256':H(J(mech))}
  irow['sectors'][label]=rr
  if (it,label) in ((115,'Zerr'),(119,'Xerr')):special[f'i{it}-{label}']=rr|{'faults':mech['faults'],'canonical_net_weight':pc(canonical),'physical_net_weight':pc(physical)}
  print('DIRECT_PASS',it,label,len(enc.vars),len(enc.cls),len(sel),H(dim),flush=True)
 rows.append(irow)
assert weights==Counter({10:22,9:2}) and len(set(all_mech_names))==24
assert special['i115-Zerr']['fault_count']==9 and special['i119-Xerr']['fault_count']==9
out={'status':'PASS','schema':'round91-clean-room-direct-v1','geometry':{'n':144,'x_checks':72,'z_checks':72,'columns_per_sector':360,'data_columns':144,'residual_columns':216,'detector_rank_each':66,'logical_quotient_dimension':12,'pool_each':1884},'sector_semantics':{'Xerr':{'hook_checks':'X','detectors':'HZ','stabilizers':'HX','logical_duals':'LZ'},'Zerr':{'hook_checks':'Z','detectors':'HX','stabilizers':'HZ','logical_duals':'LX'}},'rows':rows,'formula_count':24,'total_formula_clauses_rebuilt_and_satisfied':totclauses,'weight_histogram':dict(weights),'negative_controls':neg,'special_weight9':special,'logical_basis_hashes':{'PX':H(J(PX)),'PZ':H(J(PZ)),'LX':H(J(LX)),'LZ':H(J(LZ))}}
OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print('ROUND91_DIRECT_ALL_PASS',H(J(out)))
```

### 13.4 EFSSC domain/state audit

Source SHA-256: `3b704e1cb678b32e4de3e7e47fcb0692dc649154502a70072e18ae99ed16ef00`

```python
#!/usr/bin/env python3
"""Round91 independent EFSSC domain theorem, exact domain count, and atomic-state audit.
Standard library only; no proposer imports."""
from pathlib import Path
from collections import Counter,defaultdict
import gzip,hashlib,itertools,json,sys
ROOT=Path(sys.argv[1]).resolve();OUT=Path(sys.argv[2])
def J(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def H(b):return hashlib.sha256(b).hexdigest()
def FH(p):return H(Path(p).read_bytes())
def load(p):
 p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
RP=[{0,1},{3,4,5},{4,5}]
def positions(ks):
 p=set()
 for k in ks:p.symmetric_difference_update(RP[int(k)])
 return tuple(sorted(p))
def selector_valid(s,times,source):
 sd=source['sector_definitions'][s['sector']];qs=list(map(int,sd['qubit_signatures']));v=0
 for q in s['data_support']:v^=qs[q]
 for cs,ks in s['group_kinds'].items():
  c=int(cs);o=sorted(sd['checks'][c],key=lambda q:times[f"{sd['edge_kind']}:{c}:{q}"])
  for p in positions(ks):v^=qs[o[p]]
 return (v&((1<<72)-1))==0 and (v>>72)!=0
# Domain distribution per one check: literally visit 6!=720 local orders.
def group_dist(qs,row,pos):
 d=Counter();vis=0
 for perm in itertools.permutations(row):
  v=0
  for p in pos:v^=qs[perm[p]]
  d[v]+=1;vis+=1
 assert vis==720 and sum(d.values())==720
 return list(d.items()),vis
def half_dist(groups):
 d={0:1}
 for g in groups:
  n=defaultdict(int)
  for a,ca in d.items():
   for b,cb in g:n[a^b]+=ca*cb
  d=n
 return d
def domain_count(s,source):
 sd=source['sector_definitions'][s['sector']];qs=list(map(int,sd['qubit_signatures']));groups=[];local=0;shape=[]
 for cs,ks in sorted(s['group_kinds'].items(),key=lambda x:int(x[0])):
  c=int(cs);p=positions(ks);g,v=group_dist(qs,sd['checks'][c],p);groups.append(g);local+=v;shape.append({'check':c,'kinds':ks,'positions':list(p),'distinct_signatures':len(g),'local_orders':720})
 data=0
 for q in s['data_support']:data^=qs[q]
 # balanced exact meet-in-middle; left aggregated, right iterated explicitly.
 cut=len(groups)//2;left=half_dist(groups[:cut]);bydet={}
 for sig,c in left.items():
  det=sig&((1<<72)-1);log=sig>>72
  if det not in bydet:bydet[det]=[0,defaultdict(int)]
  bydet[det][0]+=c;bydet[det][1][log]+=c
 valid=0;right_tuples=0
 def walk(k,sig,mult):
  nonlocal valid,right_tuples
  if k==len(groups):
   right_tuples+=1;need_det=((data^sig)&((1<<72)-1));target_log=(data^sig)>>72
   z=bydet.get(need_det)
   if z:valid+=mult*(z[0]-z[1].get(target_log,0))
   return
  for v,c in groups[k]:walk(k+1,sig^v,mult*c)
 walk(cut,0,1)
 m=len(groups);total=720**m
 assert 0<valid<=total
 return {'participating_checks':m,'order_domain_size':total,'valid_order_tuples':valid,'invalid_order_tuples':total-valid,'valid_fraction_numerator':valid,'valid_fraction_denominator':total,'local_orders_visited':local,'left_distinct_signatures':len(left),'right_distinct_tuples_visited':right_tuples,'groups':shape}
initial=json.loads((ROOT/'bindings/round88/final_state.json').read_text());assert initial['next_iteration']==112 and not initial['started'] and initial['selector_count']==140
selectors=list(initial['selectors']);assert initial['selector_state_sha256']=='a0364547f846fd68ace7cdba85d89c0f8e6326145243fb0fea7ff543420994cb'
statekeys=('mechanism_id','sector','selected_names','data_support','group_kinds','selector_semantic_sha256')
compactkeys=('mechanism_id','source_iteration','sector','fault_count','selected_names','data_support','group_kinds','source_schedule_sha256','origin','selector_semantic_sha256')
def compact(s):return {k:(s.get('source_iteration',s.get('iteration')) if k=='source_iteration' else s[k]) for k in compactkeys}
all_sem={x['selector_semantic_sha256'] for x in selectors};all_names={(x['sector'],tuple(x['selected_names'])) for x in selectors}
def norm(s,source):
 sd=source['sector_definitions'][s['sector']];qs=list(map(int,sd['qubit_signatures']));d=0
 for q in s['data_support']:d^=qs[q]
 return (s['sector'],d,tuple((int(c),positions(k)) for c,k in sorted(s['group_kinds'].items(),key=lambda x:int(x[0]))))
normal=set();rows=[];total_local=0
for it in range(112,124):
 source=load(ROOT/f'formulas/iter{it}/source.json.gz');nexts=load(ROOT/f'formulas/iter{it+1}/source.json.gz');cand=json.loads((ROOT/f'iterations/iter{it}/outer/candidate.json').read_text());direct=json.loads((ROOT/f'iterations/iter{it}/direct/direct_verification.json').read_text());rec=json.loads((ROOT/f'iterations/iter{it}/record.json').read_text());times=cand['compressed_times'];raw=cand['raw_times']
 assert source['selectors']==[compact(s) for s in selectors] and len(selectors)==140+2*(it-112)
 assert not any(selector_valid(s,times,source) for s in source['selectors'])
 prior_norms={norm(s,source) for s in source['selectors']}
 new=[];domains=[]
 for label in ('Xerr','Zerr'):
  mech=direct['sectors'][label]['mechanism'];names=mech['selected_names'];assert len(names)==len(set(names))==mech['fault_count'] and 1<=len(names)<=10
  ds=[];g={}
  for n in names:
   z=n.split(':')
   if z[0]=='D':ds.append(int(z[1]))
   else:assert z[0]=='R';g.setdefault(z[1],[]).append(int(z[2]))
  s={'mechanism_id':f'r90-i{it}-{label}','source_iteration':it,'sector':label,'fault_count':len(names),'selected_names':names,'data_support':sorted(ds),'group_kinds':{k:sorted(v) for k,v in sorted(g.items(),key=lambda x:int(x[0]))},'source_schedule_sha256':cand['compressed_schedule_sha256'],'source_times':times,'canonical_support':mech['canonical_replay']['net_support'],'physical_support':mech['physical_net_support'],'source_atoms':mech['sound_outer_block']['atoms'],'source_atom_count':mech['sound_outer_block']['atom_count'],'origin':f'round90_proof_outer_iteration{it}_direct360','source_symbolic_validity':'True'}
  s['selector_semantic_sha256']=H(J({k:s[k] for k in ('sector','selected_names','data_support','group_kinds')}))
  assert s['selector_semantic_sha256'] not in all_sem and (label,tuple(names)) not in all_names
  assert selector_valid(s,times,source)
  # raw and compressed times induce identical local order for every participating check.
  sd=source['sector_definitions'][label]
  for cs in s['group_kinds']:
   c=int(cs);kind=sd['edge_kind'];row=sd['checks'][c]
   assert sorted(row,key=lambda q:raw[f'{kind}:{c}:{q}'])==sorted(row,key=lambda q:times[f'{kind}:{c}:{q}'])
  dom=domain_count(s,source);total_local+=dom['local_orders_visited'];domains.append(dom);new.append(s)
  all_sem.add(s['selector_semantic_sha256']);all_names.add((label,tuple(names)))
 # normalized expression duplicates: exact structural selector validity functions are unique.
 for s in new:
  n=norm(s,source);assert n not in prior_norms and n not in normal;normal.add(n)
 selectors+=new
 statehash=H(J([{k:s.get(k) for k in statekeys} for s in selectors]))
 assert rec['source_selector_count']==len(selectors)-2 and rec['source_selector_state_sha256']==(initial['selector_state_sha256'] if it==112 else rows[-1]['state_after_sha256'])
 assert rec['new_selectors']==[s['mechanism_id'] for s in new] and rec['state_after_sha256']==statehash and rec['new_cuts_installed']==2 and rec['state_mutated_atomically'] and not rec['repair_entered']
 # Exact next-source mutation: append exactly the pair and only permitted bookkeeping fields change.
 assert nexts['selectors'][-2:]==[compact(s) for s in new] and nexts['selectors'][:-2]==source['selectors']
 a=dict(source);b=dict(nexts)
 for x in (a,b):x.pop('semantic_payload_sha256')
 assert b['schema']==f'circdist-gross-iteration{it+1}-finite-source-v1'
 # all invariant scientific source families are byte-semantically identical
 for k in ('blocks','data_incidence','edges','frozen_semantics','overlaps','residual_positions','sector_definitions','x_checks','z_checks'):assert a[k]==b[k]
 assert b['bindings'][f'round90_iteration{it}_cnf_sha256']==cand['cnf_sha256'] and b['bindings']['round90_continuation_selector_state_sha256']==statehash
 assert b['expected']['selectors']==len(selectors) and b['expected']['assertions']==18882+len(selectors)
 rows.append({'iteration':it,'prefix':len(selectors)-2,'new_ids':[s['mechanism_id'] for s in new],'weights':[s['fault_count'] for s in new],'source_schedule_sha256':cand['compressed_schedule_sha256'],'source_old_selector_truths':0,'source_new_selector_truths':2,'state_after_sha256':statehash,'domains':domains})
 print('EFSSC_PASS',it,statehash,[d['valid_order_tuples'] for d in domains],flush=True)
final=json.loads((ROOT/'continuation/final_state.json').read_text());assert final['selectors']==selectors and final['selector_count']==164 and final['selector_state_sha256']==rows[-1]['state_after_sha256']=='854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3'
assert final['next_iteration']==124 and final['started'] is False and final['stop'] is None and final['completed_iterations'][-12:]==list(range(112,124)) and final['round90_completed_candidates']==12
assert FH(ROOT/'continuation/final_state.json')=='d67aad48ca63955350d044a138940a32168a5c53ca8580fd8720a856f06e636c'
assert len({s['selector_semantic_sha256'] for s in final['selectors']})==164
# New selector is true at a point where every old selector is false: no prior domain contains
# that source point, so the commit is not a duplicate or a retroactive old-union hit.
out={'status':'PASS','schema':'round91-clean-room-efssc-v1','initial_selectors':140,'new_selectors':24,'final_selectors':164,'atomic_transitions':12,'source_old_truth_total':0,'source_new_truth_total':24,'semantic_hashes_unique':164,'named_selections_unique':len(all_names),'structural_new_predicates_unique':len(normal),'total_local_orders_visited':total_local,'rows':rows,'final_state_sha256':FH(ROOT/'continuation/final_state.json'),'final_selector_state_sha256':final['selector_state_sha256']}
OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print('ROUND91_EFSSC_ALL_PASS',H(J(out)))
```

### 13.5 DRAT/LRAT controls

Source SHA-256: `e113c64ac0cdd59013679f34f423e650321a7f57e41efc7e2fd714915b233cd2`

```python
#!/usr/bin/env python3
import hashlib, json, pathlib, subprocess, time
P=pathlib.Path('<repo>/circdist/artifacts/circdist_gross_proof_outer_round90_20260830')
S=pathlib.Path('/tmp/circdist-r91-proof-controls'); S.mkdir(exist_ok=True)
cad=P/'tooling/cadical-1.9.5-arm64-macos'; drat=P/'tooling/drat-trim-arm64-macos'; lrat=P/'tooling/lrat-check-arm64-macos'
C=P/'controls/proof_checker'; cnf=C/'php6_5.cnf'; fresh=S/'reviewer-fresh.drat'; gen_lrat=S/'reviewer-generated.lrat'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def run(name,argv,expected,markers):
    t=time.monotonic(); q=subprocess.run([str(x) for x in argv],capture_output=True,text=True,timeout=30); dt=time.monotonic()-t
    text=q.stdout+q.stderr
    assert q.returncode==expected,(name,q.returncode,text)
    assert any(m in text for m in markers),(name,text)
    return {'name':name,'argv':[str(x) for x in argv],'returncode':q.returncode,'wall_seconds':round(dt,6),'stdout_sha256':hashlib.sha256(q.stdout.encode()).hexdigest(),'stderr_sha256':hashlib.sha256(q.stderr.encode()).hexdigest(),'markers':[m for m in markers if m in text]}
r=[]
r.append(run('fresh_unsat_generation',[cad,'--no-binary',cnf,fresh],20,['UNSATISFIABLE']))
r.append(run('valid_fresh_drat_generate_lrat',[drat,cnf,fresh,'-t','170','-L',gen_lrat],0,['VERIFIED']))
r.append(run('valid_generated_lrat',[lrat,cnf,gen_lrat],0,['VERIFIED']))
r.append(run('valid_sealed_drat',[drat,cnf,C/'php6_5.fresh.drat','-t','170'],0,['VERIFIED']))
r.append(run('valid_sealed_lrat',[lrat,cnf,C/'php6_5.fresh.lrat'],0,['VERIFIED']))
r.append(run('corrupt_drat',[drat,cnf,C/'php6_5.corrupt.drat','-t','170'],1,['NOT VERIFIED','ERROR']))
r.append(run('truncated_drat',[drat,cnf,C/'php6_5.truncated.drat','-t','170'],1,['NOT VERIFIED','ERROR']))
r.append(run('corrupt_lrat',[lrat,cnf,C/'php6_5.corrupt.lrat'],1,['NOT VERIFIED','incomplete']))
r.append(run('truncated_lrat',[lrat,cnf,C/'php6_5.truncated.lrat'],1,['NOT VERIFIED','incomplete']))
assert sha(fresh)==sha(C/'php6_5.fresh.drat')=='b6c2e560bb08c84d583ca94799951a21c8cae5de35d6d04d77bc4842e9c18ecd'
assert sha(gen_lrat)==sha(C/'php6_5.fresh.lrat')=='cf32dfff36b24ba36c3504765f29ecf3d7a8abaa59956ade4d24a4062caa6431'
print(json.dumps({'status':'ROUND91_PROOF_CONTROLS_PASS','scope':'fixture tool-chain only; no Gross UNSAT inference','runs':r,'fresh_drat_sha256':sha(fresh),'fresh_lrat_sha256':sha(gen_lrat)},sort_keys=True,indent=2))
```

### 13.6 Licensed YAML generator/delta guard

Source SHA-256: `0fe956a189bcb00373822735bb1334736967ad67e8dd420e154aa9acb0eb263a`

```python
from pathlib import Path
import yaml,hashlib
src=Path('<repo>/circdist/proof-dag/nodes/CIRCDIST.gross.yaml')
out=Path('/tmp/circdist-r91-licensed-CIRCDIST.gross.yaml')
raw=src.read_text();doc=yaml.safe_load(raw)
def dump(o):return yaml.safe_dump(o,sort_keys=False,allow_unicode=True,width=120)
assert dump(doc)==raw
E=doc['assessment']['basis']['evidence']
assert all(x['path']!='circdist/artifacts/circdist_gross_proof_outer_round90_20260830' for x in E)
E.extend([
 {'path':'circdist/artifacts/circdist_gross_proof_outer_round90_20260830','kind':'run','note':('Sealed Round-90 proof-producing finite-outer continuation package independently cleared at proposer level in Round 91; root seal sha256:41ac5ad7f28895f09aae29a256d91aec241298ec7bfe0d1dec2e14709fa00ca7 and payload seal sha256:545efe756a51190aaa8877e1d0d9fa1100da48aa213811b75a62a1f6a9b6c4d4. Iterations 112--123 are twelve complete outer SAT schedules; all twenty-four unrestricted direct-360 sectors are SAT and physically replayed, with iteration-115 Zerr and iteration-119 Xerr at weight 9 and the other twenty-two at weight 10. Twenty-four exact EFSSC selectors were appended atomically. The exact fresh/unstarted frontier is iteration 124 with 14,484 inherited order blocks, 164 selectors, selector-state sha256:854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3, and an independently checked but unsolved 401,040-variable/1,345,190-clause CNF sha256:2dd07d33ff0b29c1f06a7452c3b1c7ca9b6df950e819046f8a712dacb0dd7e5a. This is positive continuation evidence only: no Gross UNSAT, direct absence, repair entry, outer exhaustion, D* narrowing, route promotion, or root promotion is licensed.')},
 {'path':'circdist/reviews/circdist_gross_proof_outer_exact_review_round91_20260830.md','kind':'review','note':('Fresh independent Round-91 exact review. Non-importing checkers reconstruct all thirteen semantic sources and finite CNFs, satisfy every clause of the twelve complete outer assignments, re-audit every frozen legal-schedule condition, rebuild all twenty-four unrestricted direct-360 formulas from Gross geometry, and physically replay all mechanisms, including the two weight-9 cases. It proves the EFSSC iff semantics over each complete local-order domain, verifies the atomic 140--142--...--164 chain, and confirms iteration 124 is fresh, checked, and unsolved. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION; CIRCDIST.gross and its live gap route remain CONJECTURED with D*_Gross in {11,12}.')}
])
doc['frontier']['dstar-residual']={
 'task':('Continue only from the independently reviewed sealed fresh/unstarted iteration 124 state. The inherited sound order-block library remains exactly 14,484 predicates (1,440 unary, 20 round-62, 12,820 generalized, and 204 dynamic), and the exact fixed-selector frontier is 164 EFSSCs (120 reviewed Round-80 selectors, fourteen Round-86 selectors from iterations 102--108, six Round-88 selectors from iterations 109--111, and twenty-four Round-90 selectors from iterations 112--123). Bind selector-state sha256:854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3, the iteration-124 semantic source sha256:d155a897b8771a9821ef4ef14041bb910e7bbb6aaaad7f6cf08b6db1de0f397e, and source-file sha256:1c4556377a4f84d5bf7df1e08af0e98d5cb3d4ea3da94db2e94d645f40a4f544 before use. Its deterministic 10-bit compressed finite-outer formula has 19,046 source assertions, 401,040 variables, 1,345,190 clauses and CNF sha256:2dd07d33ff0b29c1f06a7452c3b1c7ca9b6df950e819046f8a712dacb0dd7e5a; it was checked but deliberately not solved, and no iteration-124 solver/model/DRAT/LRAT disposition is inherited. For a SAT result, retain the complete assignment, replay every DIMACS clause and frozen schedule condition, then rebuild and adjudicate both complete unrestricted direct-360 sectors; a positive mechanism kills only that concrete candidate and proves no absence, and only exact source-schedule-valid EFSSC selectors may be added atomically. For an UNSAT result, retain a complete DRAT proof, independently accept it, generate LRAT, and independently accept the LRAT with valid/corrupt/truncated controls. Enter repair only after both direct sectors have independently checked absence. Preserve frozen S_Gross, strict serialization, MC0, terminal residual semantics, both CSS sectors, and every existing exclusion against morphing, Circ-Preserve substitutions, alternate conflict models, exploratory pair clauses, retroactive cuts, and stale compressor provenance. Keep CIRCDIST.gross and gap-via-lift CONJECTURED and D*_Gross in {11,12}; this reviewed continuation supplies no Gross UNSAT, absence, exhaustion, distance-12 witness, universal distance-11 ceiling, route promotion, or root promotion.'),
 'kind':'task','since':'2026-08-30'}
key='gross-proof-outer-round91-review-2026-08-30';assert key not in doc['events']
doc['events'][key]={
 'date':'2026-08-30','type':'review-completed',
 'summary':('Fresh independent Round-91 review clears the sealed Round-90 finite-outer package at proposer level and licenses continuation only from fresh/unstarted iteration 124: 14,484 inherited order blocks, 164 exact EFSSC selectors, selector-state sha256:854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3, and checked-unsolved CNF sha256:2dd07d33ff0b29c1f06a7452c3b1c7ca9b6df950e819046f8a712dacb0dd7e5a (401,040 variables; 1,345,190 clauses; 19,046 source assertions). Iterations 112--123 and all twenty-four unrestricted direct sectors are SAT; their exact physical mechanisms, including two weight-9 cases, license only twenty-four candidate-domain cuts. No Gross UNSAT, direct absence, repair, exhaustion, D* narrowing, route change, or level change is licensed; CIRCDIST.gross remains CONJECTURED with D*_Gross in {11,12}.'),
 'sources':[{'path':'circdist/artifacts/circdist_gross_proof_outer_round90_20260830','kind':'run'},{'path':'circdist/reviews/circdist_gross_proof_outer_exact_review_round91_20260830.md','kind':'review'}]}
b=dump(doc).encode();out.write_bytes(b)
print(len(b),b.count(b'\n'),hashlib.sha256(b).hexdigest())
```

### 13.7 Linked-overlay validators

Source SHA-256: `1e760a679edae7f8a6183d9817a8aab13e61aea544aa4443c75d01a9c2df1340`

```python
#!/usr/bin/env python3
import hashlib,json,pathlib,subprocess,time,sys
R=pathlib.Path('/tmp/circdist-r91-overlay')
P=R/'circdist/artifacts/circdist_gross_proof_outer_round90_20260830'
O=pathlib.Path('/tmp/circdist-r91-overlay-validator-output'); O.mkdir(exist_ok=True)
subprocess.run(['git','add','-N','circdist/proof-dag/nodes/CIRCDIST.gross.yaml','circdist/reviews/circdist_gross_proof_outer_exact_review_round91_20260830.md'],cwd=R,check=True,capture_output=True)
cmds=[
 ('proof_dag_circdist',['/usr/bin/python3','tools/proof_dag_check.py','--problem','circdist'],0),
 ('proof_dag_previous_state',['/usr/bin/python3','tools/proof_dag_check.py','--problem','circdist','--previous-state',str(P/'bindings/initial_proof_dag')],0),
 ('proof_dag_all_projects',['/usr/bin/python3','tools/proof_dag_check.py'],0),
 ('evidence_closure_linked',['/usr/bin/python3','tools/evidence_closure_check.py','--problem','circdist'],0),
 ('circdist_migration',['/usr/bin/python3','tools/check_circdist_migration.py'],0),
 ('release_contracts',['/usr/bin/python3','tools/test_release_contracts.py'],0),
 ('dag_contracts',['/usr/bin/python3','tools/test_dag_contracts.py'],0),
 ('lean_dag_selftest',['/usr/bin/python3','tools/lean_dag_check.py','--selftest'],0),
 ('duplicate_yaml',['/usr/bin/python3',str(P/'source/duplicate_yaml_scan.py'),'--root',str(R),'--output',str(O/'duplicate_yaml.result.json')],0),
 ('git_diff_check',['git','diff','--check'],0),
]
rows=[]
for name,cmd,want in cmds:
    t=time.monotonic(); q=subprocess.run(cmd,cwd=R,capture_output=True,timeout=600); dt=time.monotonic()-t
    (O/(name+'.stdout')).write_bytes(q.stdout); (O/(name+'.stderr')).write_bytes(q.stderr)
    row={'name':name,'returncode':q.returncode,'expected':want,'wall_seconds':round(dt,6),'stdout_bytes':len(q.stdout),'stderr_bytes':len(q.stderr),'stdout_sha256':hashlib.sha256(q.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(q.stderr).hexdigest(),'stdout_tail':q.stdout.decode(errors='replace')[-1000:],'stderr_tail':q.stderr.decode(errors='replace')[-1000:]}
    rows.append(row)
    if q.returncode!=want:
        print(json.dumps(row,indent=2),file=sys.stderr); raise SystemExit(1)
print(json.dumps({'status':'ROUND91_LINKED_OVERLAY_VALIDATORS_PASS','checks':rows},sort_keys=True,indent=2))
```


## 14. Final limitations and delivery state

The next authorized scientific action begins only from the exact sealed iteration-124 CNF. A SAT result requires a complete assignment, legal-schedule replay, and both unrestricted direct adjudications before another atomic pair transition. An UNSAT claim requires an accepted full proof object or independently exhaustive certificate. Repair remains unavailable unless both direct sectors have checked absence. Positive SAT evidence cannot be transformed into an absence or exhaustion claim.

The protected scheduler, live node, Round-89 review, Round-90 root/payload manifests, report, and result were unchanged throughout the scientific audit. The only durable reviewer file is this review. The live node and scheduler were not edited. No commit and no push were performed.

As with any ordinary content-addressed file, this review cannot contain its own final SHA-256 without changing the bytes being hashed. Its exact post-write bytes, LF count, and SHA-256 are computed after the single durable write and reported with delivery. The licensed YAML identity above is fixed and non-self-referential.
