# Fresh independent exact review of the sealed Round-78 Gross cross-registry package

Date: 2026-08-30  
Reviewer role: sole fresh Round-79 mathematical reviewer  
Accepted proposer package: `circdist/artifacts/circdist_gross_cross_registry_round78_20260829/`  
Accepted root-seal SHA-256: `db82c387493285e56eeddcef6e7bafc3e48954c4034e6ec2fc699cea1699c987`  
Accepted payload-manifest SHA-256: `1c9b1bf35b0adba900cf188c3bf6098ff8a19b2cf1729396e2ce7ef7f60f24fb`

## Verdict and exact license

**Verdict: CLEAR — PROPOSER-LEVEL CONTINUATION AND CANONICAL EVIDENCE LINKING AT THE FRESH ITERATION-90 RESTART ONLY.**

I found no load-bearing mathematical, state-transition, provenance, manifest, or process-ledger discrepancy in the accepted seal. Independent clean-room reconstruction passed for the Gross geometry, all twelve outer schedules, all twenty-four unrestricted direct-360 formulas and assignments, all ninety-six raw mechanisms, every retained generalized-term domain, all semantic classification and commit transitions, all `43,834,872` literal pair tuples, and the exact `15,485,313,024` multi-domain tuples.

The licensed canonical delta is deliberately narrow: a later canonical edit may link this accepted package and this review as positive evidence, release the held continuation, and identify the exact fresh unstarted iteration-90 state (`G=10,595`, `D=180`, registry/raw `=96`, total installed outer blocks `=12,235`). This review does **not** decide `D*_Gross`, prove an absence result, license a repair, promote `CIRCDIST.gross`, close a branch, change the exact-root claim, or alter its routes. `CIRCDIST.gross` remains `CONJECTURED`, and the previously recorded residual `D*_Gross in {11,12}` is unchanged.

There is no inheritance from either rejected seal, from any stale compressor row, from any failed or interrupted computation, or from an unreviewed proposer conclusion. In particular, the seals beginning `1f4c0e3d` and `9f703d88` remain **REJECTED_NOT_LICENSED** for every purpose.

## Review scope, independence, and method

I did not contact or rely on the Round-78 author, did not use subagents, and did not import any proposer Python module into the independent checkers. I treated package JSON, gzip members, SMT-LIB, DIMACS, assignments, manifests, and ledgers as data. Two disposable Python 3.12.13 programs were written outside the repository:

- `round79-cleanroom-core-v1` reconstructed the code geometry and linear algebra, parsed and evaluated SMT-LIB with its own S-expression evaluator, rebuilt direct CNFs with an independently written encoder, checked complete assignments and raw mechanisms, and followed every four-state commit. Script SHA-256 `e46f98939752640d3663076e243fd318165c13bda858c26b9cecba9408d3fce7`; result SHA-256 `d2c778222afbc16f8c051ed7ee3f3980b767a22a4dbdf02d2c54785d13853bb1`.
- `round79-cleanroom-synthesis-v1` rebuilt all `6!` catalogs, residual options, constructive completions, truth relations, minimized rectangles, semantic regions, union coverage, literal selector streams, and GF(2) multi-domain dynamic programs. Script SHA-256 `a9efc7a4b0bfb4bdd886a10535bc5aa0c715cd35e470005900de0d9661cc0a34`; result SHA-256 `719f1da05cf6c56f3823804d0638ef5e7108b5e703109907dc9ebf2f731b4a77`.

The scripts and their output were disposable audit scratch and were deleted after this review. The algorithms, equations, counts, controls, commands, hashes, and resource measurements needed to reproduce their conclusions are recorded below.

## Package identity, manifests, and deterministic compression

I walked the installed package from the filesystem rather than trusting the package summary. The physical inventory is exactly:

| Item | Independently observed |
|---|---:|
| Regular files | 1,140 |
| Directories below package root | 94 |
| File bytes | 198,806,153 |
| Root-manifest rows | 1,139 |
| Payload-manifest rows | 1,138 |
| Deterministic gzip members | 865 |
| Compressed gzip-member bytes | 194,694,272 |
| Uncompressed gzip-member bytes | 7,934,212,026 |

Every root and payload row was independently parsed; its path was required to be unique, package-root-relative, non-escaping, present, and byte-hash exact. The root row set equals every package file except the exact package-root path `SHA256SUMS.txt`. The payload row set equals every file except the two exact package-root paths `SHA256SUMS.txt` and `PAYLOAD_SHA256SUMS.txt`. Hashing the manifest bytes gave the two accepted hashes at the head of this review.

The embedded Round-76 source manifest has 1,349 rows and SHA-256 `e966770d8839eeeabbd672a4c4a647d1b92fb9a2955b6750834d7f6bda1cb87e`. Its expected set excludes only its own exact root `SHA256SUMS.txt`; it correctly retains `source_bindings/round74/SHA256SUMS.txt`. An exhaustive source search and a direct expected-set reconstruction found exactly three load-bearing manifest/self-exclusion sites in `verify.py`:

1. root seal: exclude exact `SHA256SUMS.txt`;
2. root payload: exclude exact `SHA256SUMS.txt` and `PAYLOAD_SHA256SUMS.txt`;
3. nested source seal: exclude exact nested-root `SHA256SUMS.txt`.

All three now compare package-root-relative exact paths. There is no remaining basename-only manifest exclusion. This repairs both earlier defect classes. The first rejected seal, `1f4c0e3dd75b3aaed8551be79be92191478fd0ecaaad6f860dcf859634d85f5b`, wrongly omitted a nested source manifest under a basename rule. The second, `9f703d88470629decbf8304fd5e723b2790bae4c6707842879e0ae3be487d7df`, repaired that site but retained stale basename exclusions in the root seal and payload expected sets. Neither is licensed by the accepted seal or by this review.

I streamed all 865 gzip members, checked gzip framing and deterministic metadata (`mtime=0`), recomputed compressed and uncompressed sizes and SHA-256 values, and matched every `COMPRESSED_INVENTORY.json` row. This pass took 3.594 s and 229,392,384 bytes maximum RSS. The final Round-77-adapted compressor is exactly 2,760 bytes with SHA-256 `d4abdf75b066d8a2507d5c010f96c1c1760f36c6d1d242048fb45c5928cb8dde`; the stale preadaptation row is not used as provenance.

## Reviewed input and present canonical context

The accepted input is the Round-76/77 reviewed continuation, not a reconstructed approximation. I matched the embedded prior package manifest and exact prior review:

| Binding | Bytes | SHA-256 |
|---|---:|---|
| Round-76 root manifest | 146,564 | `e966770d8839eeeabbd672a4c4a647d1b92fb9a2955b6750834d7f6bda1cb87e` |
| Round-76 exact review | 60,025 | `1105df9cda3c9afb7b152ebd0cd6e7f5aff82b2a2441c52635169d13eb2cea39` |
| Gross node at start | 46,978 | `c041e00bffd1444a25c06850e29496f88d0d5c75c0eb672a642d71368b4bc5a9` |
| Scheduler at start | 177,829 | `a919b15c284f87d7578b5a58099e9a7dc1e77a3e71d80cdb782f28b12977da0a` |
| `DAG_PROTOCOL.md` | 15,377 | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | 8,523 | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |

The four initial semantic hashes are independently reproduced as:

- dynamic: `656be42225ee1fb1f51426eb5544208a6d58df8ef6a015d981561b8048d57082`;
- generalized: `031794ebbcad05fc81e1f028a7e4833ced91779c44c888b98db73f4ebd20c3cd`;
- registry: `bafc7e4c7fb5ebdd5d090790a603b1dc8c956e2260d1047c9f4b825478b103a9`;
- raw mechanisms: `864e151dde3451a63a30ff960a02826f8d6a752fd3a4383cfe266caec890a3ce`.

The starting state is fresh and unstarted at iteration 78: 1,460 fixed base blocks, `G=5,743` generalized terms, `D=156` candidate-exact blocks, 72 registry records, and 72 raw mechanisms. Thus the installed outer-block total is `1,460+5,743+156=7,359`. The raw 72 split exactly into the 24 embedded Round-74 mechanisms and 48 Round-76 mechanisms, with identifiers, selectors, source candidates, canonical/physical signatures, and hashes matching their reviewed sources.

At review time the Gross node and both protocols still have their start hashes. The scheduler has allowed later drift to 181,669 bytes and SHA-256 `9d85c770e62860a00ae53cb9f97aaef7f8b1a620f9b4c60c32279ace777c974d`: the diff records Round-78 settlement, holds continuation pending this review, and authorizes Round 79. It does not pre-license iteration 90 or contradict the package. A present-tree `--quick --repo-root` verifier run therefore fails only the byte-equality assertion for `operations/circdist/SCHEDULER.yaml`; this is expected later scheduler drift, not a package failure or a mathematical mismatch.

## Independent Gross geometry and quotient reconstruction

I reconstructed the lattice from the published offsets rather than loading the proposer model. With `L=6`, `M=12`, `g(i,j)=(i mod 6)M+(j mod 12)`, the two 72-check families use

`A=((3,0),(0,1),(0,2))`, `B=((0,3),(1,0),(2,0))`

on two 72-qubit halves. The reconstruction gives:

| Quantity | Exact value |
|---|---:|
| Data qubits | 144 |
| X checks / Z checks | 72 / 72 |
| Weight of every check | 6 |
| Rank of X / Z check matrices over GF(2) | 66 / 66 |
| Encoded quotient dimension `144-66-66` | 12 |
| Named CNOT edges | 864 |
| Nonempty X/Z check overlaps | 648 |
| Size of every nonempty overlap | 2 |
| Expanded nonstabilizer weight-12 pool per sector | 1,884 |
| Independently selected logical-dual basis per sector | 12 |

For a support bit vector `v`, I computed detector syndrome and logical quotient directly as GF(2) dot products. The combined signature was

`sigma(v) = syndrome(v) | (logical(v) << 72)`.

A support is accepted as constructive positive evidence only when the low 72 syndrome bits are zero and the upper 12 logical bits are nonzero. RREF and span membership were implemented independently; all pool words have weight 12, zero detector syndrome, and lie outside the relevant stabilizer span.

## Outer formulas and twelve schedules

For each candidate I parsed the complete stored SMT-LIB into an independent S-expression tree and evaluated every assertion under the stored integer assignment. I also rebuilt the 1,440 global unary blocks, the 20 Round-62 blocks, all evolving generalized regions, and every candidate-exact block, and matched the asserted block count and formula hash.

A legal schedule assigns one nonnegative integer time to each of 864 named edges, uses a contiguous set of layers from zero, has six distinct times within every check, has distinct incident times at each data qubit, obeys every one of the 648 two-overlap MC orientation equalities, and interleaves the two sectors. Unrelated edges may share a layer. This last point matters for the wording issue discussed below.

| Iteration | Candidate SHA-256 | Outer SMT2 SHA-256 | Blocks before | Used layers | Result |
|---:|---|---|---:|---:|---|
| 78 | `d4aab1f9d774cf3fb4b06015b820a2904fa01c9b5d74177627f6d628855a1eb0` | `4db83c87ee08b658a7c84aa41ad3f5f18e9a3f46fff1429453b7499eef5b1074` | 10,185 | 153 | SAT |
| 79 | `703d3b779038d72c1e24d3420e9fe3ee1601449b7dc7b92f099d8edf1e154fde` | `8d43a62c2558179afddf53a41a59d257d7035f828c7bcf4a9a21d2414282e435` | 10,429 | 169 | SAT |
| 80 | `297152a96b495f8b1cbc78cb3acaa1a39fa23ddf7fb53025ac59734921965415` | `6a1bf4a4f82759a6baf6c527e5c93d901f25497b77e5461d5fc40cfda69a9eea` | 10,573 | 157 | SAT |
| 81 | `7babae322246c65d83d73177548b5080e7fa4c528e8ac0266abb5207fdd4ac11` | `6be2f09fd3ccdef0dfd5eec21213e51bfaaef64d7fef06ecdb60cd5176cbac9c` | 10,873 | 168 | SAT |
| 82 | `f618324e7bc70b3d2a4ea27f1372463fefc3ffb20280ebade113b2e3685112ef` | `a368cdd28381778646094ce4b4a88a8585e0e9b6905b0fc8a1da2e62653954bc` | 11,092 | 153 | SAT |
| 83 | `7e8801c2d6829a1ac63c377e0d4aee7ef03aeecdfee897c29ca86b39cc6c4353` | `d423f2caadb5c41587630cccf181433c4f9e731e85b516ef8e70a13564378478` | 11,207 | 175 | SAT |
| 84 | `8200d95e6eb291c0abb9240cff21d580890f182413eb9e917a879193297398a6` | `9c122c402a691c3828af38268b36dd8665f97f26b499bbbca5287e48dba1c551` | 11,365 | 144 | SAT |
| 85 | `cb17c7a6a2b546574e52063f8beb03e2ccd0c603cd8390059298159c1c9b0af1` | `d71d8ca9a9f4a7a6ead175df250e08bea86d47b0ba016fa63831e45818177a36` | 11,531 | 158 | SAT |
| 86 | `032fcd815a7d6003a31ec23ae3d569a5541fcf68da3588df86010d9ff2f97781` | `09ddd6bc077cbadc33d19d1c155fc39d180186c841b4ee28c7f1cf3ac42129d5` | 11,672 | 166 | SAT |
| 87 | `dbc63d9f67168beec5b9f995cb775c1b7c155f0bc3f4e3a9710d685a72e4c9af` | `b8b689d9f3ee832036d1aba3b091223ebb3456f1e7d0291892fddf4397a1a12c` | 11,766 | 160 | SAT |
| 88 | `8f4079713e99b829e9a9d7e046b147991fd32e7a5c637b1c8726fd01b4f49aa7` | `daf6b616754cf720921a0d2918bf11370a2d322da82491063cbe4337b346a1d1` | 11,960 | 162 | SAT |
| 89 | `54d1d0a4ddb819a5073d8815baa480b80534ab66536452523c2f3029ecf452e7` | `5504904573f797cf4a409881c86c85d01281a1847d2fc4305f449a94c2313710` | 12,057 | 153 | SAT |

All twelve schedules are legal and complete. There are exactly twelve SAT results and zero outer UNSAT, UNKNOWN, timeout, signal, repair, or exhaustion results. A schedule-collision mutation was rejected in every iteration.

## Independent direct-360 reconstruction

For either error sector, I reconstructed exactly 360 primary columns:

- 144 data-singleton columns;
- `72*3=216` residual elementary columns, one for each check and each of the three reviewed residual kinds.

For a candidate schedule, each residual column has a canonical support and a physical prefix/suffix support. I recomputed both and required equal detector/logical signature. The Boolean formula has selectors `x_0,...,x_359`, 72 exact zero-syndrome XOR equations, 12 logical parity outputs with one nonzero disjunction, and only the cardinality constraint `sum x_j <= 10`. I independently regenerated the prefix-threshold cardinality recurrence and XOR gates. There is no pool restriction, residual-pattern restriction, check-count restriction, or within-check order-family restriction. The weight-12/14 pools are constructive completion resources elsewhere, not restrictions on these formulas.

Every regenerated DIMACS file was byte-for-byte equal to the package. Every stored assignment named every DIMACS variable exactly once, satisfied every clause, and selected at most ten primary columns. I XORed selected canonical supports and selected physical supports independently; both had zero syndrome, the same nonzero logical quotient, and lay outside the stabilizer span. I then reconstructed each named raw mechanism from the selected column names, residual kinds, data mask, source orders, and source atoms.

| Iter. | Sector | Variables | Clauses | Regenerated DIMACS SHA-256 | Faults | Result |
|---:|---|---:|---:|---|---:|---|
| 78 | X | 5,944 | 22,356 | `ad140a3f08b3c9add69527868607e84e6056ab82923aac1f048a4993a01c267d` | 10 | SAT |
| 78 | Z | 5,914 | 22,236 | `d361e3d51abcc9d62df93e601ff17ad4afe6109d41bd1ca05b1b1cfa4926a330` | 10 | SAT |
| 79 | X | 5,928 | 22,292 | `0d2712e9b409908b713b262ca0770f05ff9360232d79d17fa3e74060d7c28c67` | 10 | SAT |
| 79 | Z | 5,913 | 22,232 | `0430662b0f5277968faa9d13faafdcb1ded2f0a3679e433e80905eb673d16983` | 10 | SAT |
| 80 | X | 5,911 | 22,224 | `e5725778945420b44caecaf63fa0aa33db90ab94c1e7dbeaf9ad0af7c07e825d` | 10 | SAT |
| 80 | Z | 5,908 | 22,212 | `5299df8f53a985d8e7cc8b433ed2853eae5c1b2d891520d2f1c9cebc1ab2b260` | 10 | SAT |
| 81 | X | 5,882 | 22,108 | `73024dd66f434e9fc8bdfa6f8d8e8db2c6253a7282963bf97eb491b138dd9f78` | 10 | SAT |
| 81 | Z | 5,929 | 22,296 | `4825ec2392c244015d8472eba9ace68fc6ea5afab271fb2c9478aa2928138680` | 9 | SAT |
| 82 | X | 5,949 | 22,376 | `d9d0bb81a750df571361ca357201bf5624a3ea1c04562bc5c60e306a06e4eb5f` | 10 | SAT |
| 82 | Z | 5,932 | 22,308 | `afd3feb7f5aeb7d0a35ba11a909fc617079f26af55424b128c98414bf73df6fb` | 10 | SAT |
| 83 | X | 5,905 | 22,200 | `0effde4e51d1a5f095791ede66cc6b074d8bc20ed9c658e2a3a545cf978f3a91` | 10 | SAT |
| 83 | Z | 5,910 | 22,220 | `974bf7cfe9307978745405b78b4af564a5c614b01f24122a25439aaa271047f2` | 10 | SAT |
| 84 | X | 5,927 | 22,288 | `93c14acb4e09c1b243d6867cd689fbf58ea26be82804d67894940831fddc19ea` | 10 | SAT |
| 84 | Z | 5,939 | 22,336 | `ab7f10dfc2fc9275be8dc2f879da9b7d28b38539fe2d7a16f3fb090e6d7a8776` | 10 | SAT |
| 85 | X | 5,939 | 22,336 | `cfdf3116df42c9a9d302d879d98b4d12cbf220deedf56c855ec48c5667e6d803` | 10 | SAT |
| 85 | Z | 5,918 | 22,252 | `42abdad7460a04562f05447c6243469c9daf0d7019bc63bc1bf7863a2a79a795` | 10 | SAT |
| 86 | X | 5,912 | 22,228 | `be8d6df3db3012d88d4353b9079bc50d054a7e4aaceacbf5746ff4c9cf98b735` | 10 | SAT |
| 86 | Z | 5,912 | 22,228 | `480db8f175ba20abb1cfefdf0a6c709b10bbc99e5b756e2057177990d9212965` | 10 | SAT |
| 87 | X | 5,908 | 22,212 | `903161780ad64a90357fee01fbf1245daea5b570d69a562d7470079cc94dc484` | 10 | SAT |
| 87 | Z | 5,912 | 22,228 | `66aa34d48c9208327140b0ba4cd7224bbacf9c292aac6020fba0305f9244ef3b` | 10 | SAT |
| 88 | X | 5,956 | 22,404 | `4ca7a23f723970649179713a02fa9c149ad292fa751bc8f9ecd97a0b35ea85bb` | 10 | SAT |
| 88 | Z | 5,942 | 22,348 | `424f7372e56215a6ff5a6d3c8b697187897acc3d62169173af26dbdf18b417bb` | 10 | SAT |
| 89 | X | 5,913 | 22,232 | `bb7d38d75de8bd8297eabe20e3f4feccd77a61c824c9a4af691bdb8b6375696c` | 9 | SAT |
| 89 | Z | 5,920 | 22,260 | `40f87573ce7bc2fc25f0ce76dbaf7566933768c7bb427809f779e93dc8bb6e27` | 10 | SAT |

This is exactly 24 unrestricted complete direct assignments and 24 physical mechanisms, all SAT. There is no direct UNSAT, UNKNOWN, timeout, partial assignment, or absence proof. As adversarial controls I flipped the first selected primary variable in every assignment, removed the first selected physical fault in every mechanism, and truncated one assignment. All 24 flips, all 24 removals, and the truncation were rejected by the appropriate formula or physical invariant.

## Clean-room cross-registry synthesis

### Catalogs, options, and constructive eligibility

For each participating sector/check I enumerated all `6!=720` orders directly. A catalog row records the six-qubit order and, for each of three residual kinds, its canonical support, physical support, and 84-bit detector/logical signature. I independently verified canonical/physical signature equality for every record. An order atom `q<r` was converted into the exact 720-bit mask of permutations in which `q` precedes `r`; a term domain is the intersection of its atom masks.

For a sector `s`, check `c`, residual kind `k`, and canonical support `u`, I rebuilt the option registry from the reviewed raw mechanisms. Two options are pair-eligible only in the same sector and on distinct checks. They may come from different source candidates. For residual XOR `r=u_a xor u_b`, a constructive completion must give an explicit data mask `d` such that `2+|d|<=10` and `sigma(r xor d)` has zero syndrome and nonzero quotient. Weight-12 pool words and the explicitly positive weight-14 set were searched as completion sources; they did not restrict the primary direct domain. Failed completion searches were given no negative meaning.

For checks `a,b`, I rebuilt the exact 720-by-720 positive relation rowwise as

`T(i,j) = U_a(i) OR U_b(j) OR OR_h (A_h(i) AND B_h(j))`,

where `U_a,U_b` are constructive unary-witness masks and each `A_h x B_h` comes from an explicit positive completion. A proposed rectangle `A x B` was accepted only if every bit of every row satisfied `A x B subset T`. Greedy atom deletion was independently repeated in the published direction; every retained atom's named deletion control exposed a tuple outside the named positive relation. Those controls prove only local atom minimality, never global necessity or absence.

The pre-outer reconstruction over all 72 reviewed mechanisms matched every intermediate count:

| Pre-78 quantity | Exact value |
|---|---:|
| Complete catalogs | 129 |
| Catalog order records | 92,880 |
| Distinct residual options | 349 |
| Eligible distinct-check option-pair attempts | 30,037 |
| Constructive positive configurations | 1,938 |
| Configurations joining different source candidates | 1,835 |
| Positive pair relations | 1,051 |
| Raw sound term candidates | 3,884 |
| Retained pair terms after exact classification | 2,826 |
| Literal selector tuples visited | 25,685,232 |
| Zero retained domains | 0 |

Only after those checks does generalized state change from `5,743` to `8,569`; dynamic, registry, and raw states remain at 156, 72, and 72. The transition journal and the first iteration-78 input hashes match this order exactly.

### Physical selector replay

For every retained pair tuple `(i,j)`, not a sample, I recomputed the deterministic selector priority: `a_unary`, then `b_unary`, then the first listed global explicit configuration. Unary selection returns its stored constructive logical word. Explicit selection returns canonical support `u_a(i) xor u_b(j) xor d` and physical support `p_a(i) xor p_b(j) xor d`. I checked fault count at most ten, equal canonical/physical signature, zero syndrome, and nonzero quotient for every tuple. Independently generated binary stream records matched the package stream SHA-256 values, samples, selector partitions, and histograms in every batch.

### Semantic equality, dominance, union, and mutation order

I normalized each term to `(sector, sorted checks, exact 720-bit mask per nontrivial check)`. Thus:

- semantic duplicate means equality of this normalized finite region;
- `U` dominates `V` exactly when `M_V(c) subset M_U(c)` for every check, taking an omitted mask as all 720 orders;
- a zero local mask or zero Cartesian/DP total is rejected before it can be sound, classified, retained, or installed;
- pair-domain full-union coverage is computed exactly row by row with 720-bit integers;
- online multi-domain full-union coverage is decided by an exact complement CSP over local membership classes, with memoized states, rather than sampling;
- installed predecessors and candidate-exact blocks are preserved.

I reproduced every classification label (`duplicate_old`, `duplicate_new`, `dominated_old`, `dominated_new`, `covered_by_full_evolving_union`, `retained`, or `rejected_zero_domain`), every cover-set hash, every exact covered-domain count, and the deterministic reverse-sweep order. Raw soundness and all retained-domain validations occur before the corresponding pending state is committed.

## Exhaustiveness: literal replay and exact multi-domain DP

The following table is from actual independent visits, not multiplication of ledger summaries. `Online factorized` is separate from the literal column.

| Batch | Online retained | Online literal visited | Online factorized | Cross retained | Cross literal visited |
|---|---:|---:|---:|---:|---:|
| pre-78 cross | — | — | — | 2,826 | 25,685,232 |
| 78 | 9 | 66,240 | 0 | 233 | 1,966,536 |
| 79 | 7 | 42,048 | 2,985,984 | 135 | 1,272,672 |
| 80 | 5 | 38,592 | 0 | 293 | 2,620,392 |
| 81 | 4 | 31,680 | 13,759,414,272 | 213 | 1,910,784 |
| 82 | 5 | 34,272 | 2,985,984 | 108 | 958,176 |
| 83 | 10 | 81,216 | 0 | 146 | 1,367,640 |
| 84 | 4 | 39,168 | 0 | 160 | 1,580,352 |
| 85 | 7 | 56,232 | 0 | 132 | 1,038,912 |
| 86 | 4 | 29,376 | 0 | 88 | 798,144 |
| 87 | 2 | 19,584 | 0 | 190 | 1,701,696 |
| 88 | 3 | 23,112 | 0 | 92 | 844,536 |
| 89 | 2 | 8,640 | 1,719,926,784 | 174 | 1,619,640 |
| **Totals** | **62** | **470,160** | **15,485,313,024** | **4,790 including pre** | **43,364,712** |

The actual visited literal total is

`43,364,712 cross + 470,160 online = 43,834,872`.

The independent literal pass completed in the synthesis checker; it did not use stream lengths as a proxy. It covered all retained pair tuples in all 25 synthesis batches (pre-outer, twelve online, and twelve post-cross), rebuilt the physical selector for each, and checked its stream record.

For a retained multi term with allowed order set `O_c` at each check, I independently grouped local contributions by exact signature and used the recurrence

`N_0(sigma_data)=1`,

`N_{t+1}(z)=sum_{o in O_c} N_t(z xor sigma_c(o))`.

The multiplicity of an order remains in the grouped transition. At every layer I matched the allowed mask, signature-class multiplicities, reachable-signature set hash, and total multiplicity. At termination I required the sum of multiplicities to equal the Cartesian product, every terminal syndrome to be zero, and every terminal logical quotient to be nonzero. The four products are:

| Retained multi term | Local order counts | Exact product |
|---|---|---:|
| iteration 79 X | `48*36*48*36` | 2,985,984 |
| iteration 81 X | `36*48*36*12*48*8*48` | 13,759,414,272 |
| iteration 82 X | `48*36*48*36` | 2,985,984 |
| iteration 89 Z | `48*36*48*12*48*36` | 1,719,926,784 |
| **Total** | — | **15,485,313,024** |

All four domains are nonempty. All local masks are nonempty. No invalid terminal multiplicity exists. The accepted cross-registry two-selector pilot retained no multi term; that bounded outcome is not a global higher-dimensional absence claim. Across all accepted batches I found zero installed zero-domain terms, zero union off-by-one errors, and zero semantic containment mismatches. I also independently checked all 47,714 atom-deletion controls while preserving their narrow interpretation.

The synthesis checker took 225.254 s internally (227.21 s under `/usr/bin/time -l`) and 2,772,123,648 bytes maximum RSS. It made 51,389 independently cached constructive pool-completion queries. No proposer module was imported.

## Per-iteration additions and atomic commit chain

The exact state arithmetic is:

| Iter. | Blocks before | Layers | X/Z faults | Online `+` | Cross `+` | G after | D after | Registry/raw after | Blocks after |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 78 | 10,185 | 153 | 10/10 | 9 | 233 | 8,811 | 158 | 74/74 | 10,429 |
| 79 | 10,429 | 169 | 10/10 | 7 | 135 | 8,953 | 160 | 76/76 | 10,573 |
| 80 | 10,573 | 157 | 10/10 | 5 | 293 | 9,251 | 162 | 78/78 | 10,873 |
| 81 | 10,873 | 168 | 10/9 | 4 | 213 | 9,468 | 164 | 80/80 | 11,092 |
| 82 | 11,092 | 153 | 10/10 | 5 | 108 | 9,581 | 166 | 82/82 | 11,207 |
| 83 | 11,207 | 175 | 10/10 | 10 | 146 | 9,737 | 168 | 84/84 | 11,365 |
| 84 | 11,365 | 144 | 10/10 | 4 | 160 | 9,901 | 170 | 86/86 | 11,531 |
| 85 | 11,531 | 158 | 10/10 | 7 | 132 | 10,040 | 172 | 88/88 | 11,672 |
| 86 | 11,672 | 166 | 10/10 | 4 | 88 | 10,132 | 174 | 90/90 | 11,766 |
| 87 | 11,766 | 160 | 10/10 | 2 | 190 | 10,324 | 176 | 92/92 | 11,960 |
| 88 | 11,960 | 162 | 10/10 | 3 | 92 | 10,419 | 178 | 94/94 | 12,057 |
| 89 | 12,057 | 153 | 9/10 | 2 | 174 | 10,595 | 180 | 96/96 | 12,235 |

The 24 SAT mechanisms add exactly 24 candidate-exact blocks. Online generalization adds `9+7+5+4+5+10+4+7+4+2+3+2=62` retained terms. Post-iteration cross-registry synthesis adds `233+135+293+213+108+146+160+132+88+190+92+174=1,964`. Together with pre-outer `2,826`, cross-registry retention is exactly `4,790`.

For every iteration I matched the before states to the prior complete commit; appended the two candidate-exact blocks only to pending dynamic state; checked online generalized/registry/raw pending outputs; checked post-cross generalized pending output; matched intent hashes to all four pending files; and matched complete-commit hashes to the next live state. No iteration consumes a half-committed bundle. All 96 accepted CEGAR process records are strictly serial: 72 have exit code 0 and the 24 SAT solver processes have exit code 10. Accepted computation has zero timeout, signal, UNKNOWN, or concurrent load-bearing process.

## Exact fresh iteration-90 restart

The final restart is unstarted: there is no iteration-90 candidate, outer model, direct query, or pending commit. I independently recomputed all four semantic hashes:

| State | Count | Semantic SHA-256 |
|---|---:|---|
| Dynamic candidate-exact blocks | 180 | `30227f09a28c318ea392ae0473cc7644c294ea02aac6007d30eaddd1884ee348` |
| Generalized terms | 10,595 | `ba4e37e48c856f8966fd86540daab423468c551289856517aacc35cc1403c8f3` |
| Mechanism registry | 96 | `6663a3a3036199de684255c622690ebf00e02b7e5fd0249af6bbafcfece42cdd` |
| Full raw mechanisms | 96 | `6746258d7e045c211596ec264a1bcf9a748357e6b7a8f76008e532e189179f1f` |

The installed count is `1,460+10,595+180=12,235`. A continuation must launch a fresh iteration-90 outer process over these exact four states and preserve the same unrestricted direct and atomic-commit rules.

## Proof-policy and fresh checker controls

There is no Gross UNSAT proof in this package. I nevertheless exercised the bundled proof pipeline on a fresh PHP(6,5) control:

1. CaDiCaL generated a 3,114-byte DRAT, SHA-256 `b6c2e560bb08c84d583ca94799951a21c8cae5de35d6d04d77bc4842e9c18ecd`, and exited 20 with `UNSATISFIABLE`.
2. `drat-trim` accepted it, emitted `VERIFIED`, and generated an 11,189-byte LRAT, SHA-256 `cf32dfff36b24ba36c3504765f29ecf3d7a8abaa59956ade4d24a4062caa6431`.
3. `lrat-check` independently accepted the LRAT.
4. Both checkers rejected a low-memory corrupt fixture and an independent ten-line truncation, each with nonzero exit status.

These controls test the binaries and rejection discipline only. They do not prove any Gross absence. A future repair still requires candidate-specific proof-producing formulas for both sectors, independent DRAT acceptance, LRAT generation and acceptance, negative controls, and exact state binding.

## FIX-2 incident and rollback audit

The incident ledger is internally consistent with preserved attempt records and the immutable accepted state:

| Attempt | Observed resource/result | Disposition checked |
|---|---|---|
| synthesis v1 | 508.46 s; max RSS 17,801,838,592; peak footprint 40,066,248,976 | naive full-vector DP interrupted; no state mutation |
| synthesis v2 | 292.84 s; max RSS 9,262,628,864; peak footprint 9,258,146,584 | terminal DP interrupted; no state mutation |
| synthesis v3 | 377.95 s; max RSS 20,533,542,912; peak footprint 35,033,834,240 | eight-pair MITM guard stop; no state mutation |
| synthesis v4 | 715.44 s; max RSS 1,073,250,304 | exact safe classification path, but repeated RREF replay interrupted; no state mutation |
| synthesis v5 | 149.72 s; max RSS 1,073,479,680 | assertion exposed candidate already covered by full evolving union; failed before mutation |
| synthesis v6 | 194.60 s; temporary `G=8,572`, semantic `e26c650f41a653774305a17871670a32cd7481115ffd589d74025ed9cc73aa7f` | three contradictory-atom multi terms had zero domains; staging rejected and rolled back before outer |
| synthesis v7 | 148.11 s; max RSS 2,111,930,368 | accepted: 3,884 raw, 2,826 retained, 25,685,232 literal tuples, zero retained domains, `G=8,569` |

For v6 I matched the rollback targets to all four reviewed iteration-78 start hashes, not merely the counts. Canonical files and source packages were untouched. The v7 rule rejects zero DP totals and zero local masks before minimizer seeding, classification, or mutation, and uses exact full-evolving-union coverage.

The first proof-control corrupt fixture prepended out-of-domain literal `999999999`; `drat-trim` attempted pathological allocation and reached approximately 17,571,790,848 bytes RSS. The process was terminated under the memory guard, and all four mathematical state hashes were rechecked unchanged. The attempted `RLIMIT_AS` replacement failed in `preexec_fn` before a checker child started. The accepted v3 control uses syntactically corrupt valid-scale and truncated fixtures with a 30-second hard subprocess limit. These incidents are honestly separated from mathematical evidence.

Two development verifier failures are also correctly nonmathematical: Python 3.9 lacked `int.bit_count()` in v1 after outer/direct checks, and v2 exposed the online `fault_weight_histogram` versus cross `fault_count_histogram` schema branch. Both occurred before any state mutation. The compatible implementation and branch-specific schema check are present in the accepted verifier.

I found no hidden state mutation behind any failed attempt. The accepted state begins only at synthesis v7, the v6 staging mutation is fully rolled back, and no failure, timeout, signal, or negative search is assigned mathematical meaning.

## Proposer verifier used only after independent checks

Only after both clean-room programs passed did I construct a disposable Python 3.9.6 environment with the exact freeze:

`numpy==2.0.2`, `python-sat==1.9.dev15`, `six==1.17.0`, `z3-solver==5.1.0.0`.

Fresh installed-package, no-live corroboration gave:

| Mode | Exit/status | Internal / real time | Max RSS | Output bytes | Output SHA-256 |
|---|---|---|---:|---:|---|
| `--full` | 0 / PASS | 419.740 / 420.11 s | 4,528,898,048 | 20,984 | `3b1e6dcee8973c859466bf0375de1aa6ae28788df7a3148cbf5de00e702a11cc` |
| `--quick` | 0 / PASS | 6.116 / 6.19 s | 4,528,832,512 | 2,278 | `e9fd425a229b27e4bfcc90adf84313e7db2d40bab99781dc8762a60984bca2be` |

The full result reports `MATERIAL-CHECKED-PROGRESS-NOT-CLOSED`, rebuilds all 12 outer and 24 direct instances, replays 96 raw mechanisms and all literal/factorized domains, and agrees with every independent total above.

The accepted ordinary post-copy original full/live result is externally reported as PASS with SHA-256 `bd0d5fe09d5c84ca4776e8c78ef35f4addb3b8669e18fe3e2f39eee95f2e548a` and 425.52 s. The accepted original quick/live result is externally reported as PASS with SHA-256 `1c361835146336b0a99476c4c9516b357c2ab86a2867af993a74d473a8f4f87c` and 6.27 s. By design those original output bytes remain outside the immutable package, so I cannot claim to have rehashed absent logs. I record the supplied hashes as original operator-run evidence and distinguish them from my fresh output hashes above.

The repaired preseal quick incident is separate: the verifier itself exited 0 and reported PASS with six live bindings; an external summary wrapper incorrectly expected two and exited 1. That parser error is not a verifier failure, is not either accepted post-copy result, and has no mathematical effect.

## Install tripwire, protected hashes, and concurrent drift

The package's preflight disclosure records a global inventory change before the final install baseline: `9,532` records / `446,347,640` bytes / SHA-256 `399dd30089ebd58e49e8abea6135506d6073e7a22e3b6e8a8c6e422827267acd` became `9,762` records / `506,423,497` bytes / SHA-256 `b0354c3b9af124c854b17765825646092f2e0792b5b22d7ff4a64a68eb03f26b`. The exact diff is 230 additions, 68 changes, and zero removals, all in disclosed unrelated grothendieck, holevo, werner-holevo, and `tmp` work. The authorized target was absent, and the six protected hashes matched the source bindings.

The accepted release protocol requires an immediate preinstall baseline, atomic target installation, exact before/after repository equality over the same set excluding the authorized target, and a target-only Git delta. The operator context records that those gates passed. Like the original post-copy verifier output, the two historical inventory byte streams are intentionally external and not sealed; I therefore do not claim to have rehashed unavailable historical bytes. I independently established the present stronger content facts that matter to this review: the sole installed target has the exact accepted seal and 1,140-file inventory; the Gross node, protocols, prior seal, and prior review have their protected hashes; and the only protected-path difference from the starting snapshot is the explicitly allowed later scheduler update described above.

At my own audit baseline the repository already had substantial unrelated work: 8,735 porcelain-v2 records (12 tracked-status records and 8,723 untracked records), 1,187,496 status bytes, SHA-256 `9e271af4b43cd256227299ef32a4563d4ef51d00df58ddfca4794c2952a4f435`. At sealing, status had 8,754 records, 1,189,256 bytes, SHA-256 `3b506df0cc98a874ff3025b83eb8df66d80b164ab623733d26ba80037116e909`. The set difference was exactly nineteen additions and zero removals: this one authorized review plus eighteen concurrent untracked records, all eighteen under `holevo-extensive-violation/`. No other CIRCDIST, protocol, scheduler, or package path drifted. I did not revert or modify that concurrent work.

## Observations and evidence boundaries

I found no load-bearing discrepancy. Three boundaries should remain explicit:

1. `MATH_DERIVATION.md` calls a valid schedule “a permutation.” The formulas and audits actually allow unrelated edges to share a layer, as the independently checked 144–175-layer schedules demonstrate. The operative constraints are consistently encoded and verified; this is a non-load-bearing prose imprecision, not a geometry or satisfiability error.
2. Original accepted post-copy logs and historical pre/post inventory streams are external by release design. Their supplied hashes/outcomes are not silently presented as independently rehashed sealed evidence. Fresh clean-room verification, current target sealing, and fresh proposer no-live runs independently establish the mathematical/package claims.
3. Positive SAT mechanisms and positive generalized regions cannot narrow `D*_Gross`. Zero truth cells, completion misses, zero domains, solver negatives, and deletion countertuples are not used as absence evidence anywhere in the accepted state or in this review.

## Reproduction record and resource use

Repository root:

`<repo>`

Independent interpreter:

`<home>/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3` (Python 3.12.13)

Core run:

```text
/usr/bin/time -l PYTHON3.12 /tmp/circdist-round79-exact-review-20260830-audit/core_audit.py
```

Result: PASS; internal wall 15.059 s, real 16.74 s, maximum RSS 643,448,832 bytes.

Synthesis and exhaustiveness run:

```text
/usr/bin/time -l PYTHON3.12 /tmp/circdist-round79-exact-review-20260830-audit/synthesis_audit.py
```

Result: PASS; internal wall 225.254 s, real 227.21 s, maximum RSS 2,772,123,648 bytes; literal tuples actually visited `43,834,872`; factorized tuples exactly proved `15,485,313,024`.

Proposer corroboration:

```text
/usr/bin/time -l SCRATCH_VENV/bin/python PACKAGE/verify.py --full
/usr/bin/time -l SCRATCH_VENV/bin/python PACKAGE/verify.py --quick
SCRATCH_VENV/bin/python PACKAGE/verify.py --quick --repo-root REPOSITORY
```

The first two passed. The third intentionally used the current live tree and failed only the later scheduler byte-binding assertion. Manifest and gzip streaming were separate independent passes. Fresh proof controls invoked the bundled CaDiCaL, `drat-trim`, and `lrat-check` directly with short hard limits.

Final hygiene used a fresh process table with the invoking process and its ancestors excluded. Both `/tmp/circdist-round79-exact-review-20260830-audit` and `/private/tmp/circdist_round78_cross_registry_20260829` were absent, and the scan found zero surviving process whose command referenced either task scratch, either independent checker, or the package verifier. Relative to the recorded baseline, this review is the only authorized durable file written by this task.

## Final disposition

The accepted seal is internally exact and mathematically sound as positive proposer-level progress. The exact continuation point is fresh iteration 90 over the four semantic hashes listed above. Canonical evidence linking and release of that continuation are licensed only when they cite both the accepted package seal and this review and preserve the current `CONJECTURED` level, the exact-root claim/routes, and the prohibition on absence inference.

No rejected seal, failed FIX-2 staging state, stale compressor row, external parser failure, or unreviewed conclusion is inherited.
