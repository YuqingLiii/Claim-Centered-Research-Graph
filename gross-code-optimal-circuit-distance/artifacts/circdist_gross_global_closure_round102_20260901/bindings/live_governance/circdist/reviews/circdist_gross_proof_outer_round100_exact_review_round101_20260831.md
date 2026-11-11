# Round 101 exact independent review of the Gross proof-outer Round 100 package

## Review identity and verdict

This is the one-shot fresh independent review commissioned for
`circdist/artifacts/circdist_gross_proof_outer_round100_20260831`. The review began under the
2026-08-31 dispatch and completed after the local date rolled to 2026-09-01; the bound package and
requested `20260831` review identity are unchanged. I did not contact the proposer or any prior
worker. I treated the canonical proof DAG, scheduler, protocol files, and sealed package as
read-only. I imported no sealed-package Python module into the principal outer/direct or full-span
reconstruction; the independent order-six checker reused only the already independently rebuilt
Gross geometry functions. All reviewer scratch was ephemeral and is required to be absent at
finalization.

**Verdict: `CLEAR-PROPOSER-LEVEL-CONTINUATION`.** The sealed Round 100 package is safe to link and
reuse only with the exact scope and documentation correction in this review. It licenses a strict
continuation from the fresh, checked, unstarted, unsolved iteration-184 frontier. It does **not**
license a root or route promotion, a narrowed interval, a direct-sector absence result, repair
entry, outer exhaustion, a universal distance-11 ceiling, or a distance-12 witness.

The canonical conclusions therefore remain:

* `CIRCDIST.gross`: **CONJECTURED**;
* `gap-via-lift`: **CONJECTURED**; and
* \(D^*_{\mathrm{Gross}}\in\{11,12\}\).

I found one definite public-documentation defect. `SYNTHESIS_PROOF.md` says that every X and Z
canonical, physical, and combined triple-key group has size one. X does. Z does not: each of the
three Z histograms is exactly `size 1: 209,304 groups; size 2: 315 groups`. Every Z doubleton is
nonseparated, so no doubleton can be the lower-three/upper-three split of a sorted six-set. The
retained count is still exactly zero. This is non-load-bearing for the science, but the all-singleton
sentence must not be cited. The replacement YAML below records the correction explicitly.

## Frozen definitions used by this review

I rebuilt the Gross CSS geometry from the frozen coordinate construction rather than accepting
derived package tables. Let \(L=12\), \(M=6\), \(G=72\), and \(N=144\), with
\(g(i,j)=(i\bmod 12)6+(j\bmod 6)\). For each \(g\in\{0,\ldots,71\}\), I used

\[
A=((3,0),(0,1),(0,2)),\qquad B=((0,3),(1,0),(2,0)),
\]

and reconstructed the six-qubit X and Z checks exactly as the frozen source specifies. This gives
72 checks per sector, 864 distinct CNOT edges, and 648 nonempty X/Z overlaps, each of size two. The
1884 weight-12 logical representatives per sector were rebuilt from translated seed words; the
stabilizer ranks, 12-element logical bases, and the 12-by-12 cross-sector pairing rank all checked.

For a fixed schedule and sector, the complete direct name universe is

\[
\{D:q:0\le q<144\}\cup\{R:a:k:0\le a<72,\ 0\le k<3\},
\]

so it has 360 names. A data name has its one-qubit canonical/physical support and all allowed
detector suffix options. A residual name uses canonical residual positions
`(0,1)`, `(3,4,5)`, `(4,5)` and raw physical suffix positions `(2,3,4,5)`, `(3,4,5)`, `(4,5)` in
the schedule-sorted six-CNOT check. “Named weight” means the number of selected names, not the
weight of the propagated support. Canonical and physical effects were separately XORed, separately
syndrome-checked, and compared in the fixed 12-bit logical basis.

For mixed CSS mechanisms, the common-name convention counts a name occurring in both components
once, as a Y-type location: the mixed named weight is \(|N_X\cup N_Z|\).

## Immutable input and seal audit

### Exact dispatch bindings

The package is bound to the dispatched scheduler bytes, not the later live scheduler. Independent
stored/content hashing of every row in `INPUT_BINDINGS.json` found 69/69 exact rows and reproduced
the immutable-input tree
`4b82108c67f0288460de64fdf48a43efbdb0a07d4cb1bf5de735d93d253446ab`. The initial proof-DAG
snapshot contains 20/20 exact files and reproduces tree
`dec18588cbaf9b8e5de93f1b5198c5bfecedcec9d2c39509416673bffbdbaf62`.

The protected identities are:

| Object | SHA-256 | bytes | LF | finding |
|---|---|---:|---:|---|
| dispatched `operations/circdist/SCHEDULER.yaml` copy | `a4ecdb895bb62b1537cf012f3dd4385d3e45f63380e95896f3bece409c43abe4` | 265,091 | 3,167 | exact commissioned dispatch |
| live scheduler at review | `6383f777bdb9acb2f1bae64424de5198547154a384820527aec810a83456afc9` | 270,021 | 3,218 | intentionally later Round-101 authorization; never substituted for dispatch |
| live and bound `CIRCDIST.gross.yaml` | `43abf1f383f44a4aee98c71da17af6fddca8b526d76cf135cd16c89a9aaae14c` | 85,062 | 938 | byte-identical pre-review state |
| live and bound `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` | 15,377 | 283 | byte-identical |
| live and bound `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` | 8,523 | 166 | byte-identical |
| live and bound Round-99 review | `28ed0201da7cfc87aba7ce2ec2ad53afbb3d363b7bc66ab802f9feea6bc1d060` | 583,650 | 5,810 | byte-identical prior decision |

The licensed iteration-172 starting point also reproduces exactly: selector count 304; selector
state `a5c64ae41f474844ecd3ac41829331f54d419a81573e4f0e11528db0b49e25d1`; state file
`9fd675be9712a28dd625fba7cce95f75a8a3b9bdf7edc3f398bfa8b13844d2be`; source file
`99faca59521b675844d0c10eb12afcfe925f474d3eac9d5cac56e11537397b08`; semantic source
`cfa261df8b148622c80248d398df20f1ff5a4cf3f04eb76a31b2795185cc6412`; and CNF
`f86b8db36af1df3877ca1d9dbafb171b6173ddc8b6c2f045a808dd6c71f98342`, with 19,186
assertions, 413,646 variables, and 1,406,245 clauses. The prior Round-98 seal root/payload/inventory
are respectively `f64feb1b424b4aff938a1b5a0c1f9a799179e41f4ec99295c5c67376fad9142f`,
`2df276eb26dc569f830d0c95ac76aa5ed322bc9fcb525637a96196d66394e6ec`, and
`35f77eacac06bb114f897b16e61b2a03b00f961cc8448e258d2210e65273f45c`; its 56-child sealed
replay status is PASS.

### Two-level manifests and physical inventory

I walked the sealed tree myself, rejected symlinks, hashed stored bytes, counted physical bytes and
LFs, and separately checked the root manifest, payload manifest, and inventory rows. There are
exactly 1,696 physical files, 351,189,415 bytes, and 5,332,240 LF. Every listed hash is correct and
all expected paths are unique.

| Object | SHA-256 | bytes | LF / rows |
|---|---|---:|---:|
| `SHA256SUMS.txt` | `37d542fd5ec88370351efdba043506ee0d2b581f458dd5b6d882249260a63e49` | 194,516 | 1,695 |
| `PAYLOAD_SHA256SUMS.txt` | `c35ee5e5944f40b76320de1bdeafca9830315046e8fb5e3e90b74dc81f502c19` | 194,427 | 1,694 |
| `FILE_INVENTORY.jsonl` | `fc9def57f4bea09822271895ac9a76a56092b39d4db42a4de6695996b3a2465b` | 269,407 | 1,693 |
| `RESULT.json` | `997a3a8f89b7f2d8d5f4f577dde3e6272b0e3fb790ffe9e36aaef86702e48498` | 35,252 | 1,084 |
| `REPORT.md` | `a6ae44aacc8f48366feb4adfe345956128a63daedcdb9ca558b27b23fca55e2b` | 4,037 | 39 |

The preseal count was 1,692 files / 350,530,811 bytes / 5,327,150 LF; the four later physical
entries are the normal final two-level seal/inventory additions. No stale live file was used to
fill a package binding.

## Independent outer-formula and direct-query audit

### Method

For each iteration 172 through 184 I recomputed the semantic-source digest after removing only its
self-hash field; rebuilt the geometry, sector rows, block and selector predicates; and reconstructed
every clause from `circuit_trace.json.gz` and every root clause from
`assertion_map.jsonl.gz`. I did not compare only aggregate counts. Each expected clause was placed at
its declared one-based clause ID and hashed from its complete signed literal sequence. I then
streamed the actual DIMACS in order and required equality for every clause.

The trace encodings checked were exact equivalences:

* `and`: \(y\leftrightarrow(a\land b)\), three clauses;
* `or`: \(y\leftrightarrow(a\lor b)\), three clauses;
* `xor`: \(y\leftrightarrow(a\oplus b)\), four clauses;
* `constant_true`: the unit clause \(y\); and
* rank membership: all 32 five-input valuations, with output polarity selected by the declared
  accepted-rank set.

This accounts for all 18,343,494 outer clauses across the thirteen formulas, including the unsolved
iteration-184 formula. For iterations 172--183, I parsed both retained complete assignments,
required exactly one value for every variable, required the two parsed value maps to agree, and
evaluated every clause under both maps. The differently wrapped DIMACS text is not claimed to be
byte-identical; the complete variable assignments are identical.

For each decoded outer model I rebuilt the 864 raw edge times and extrema, compressed by sorted
distinct time rank, and required exact equality to the retained candidate. Independently checked
conditions were: exactly the frozen edge set; nonnegative integer times; no check or data-qubit
conflict at a time; compressed layers contiguous; zero measurement-consistency violations on all
648 two-edge overlaps; global X/Z interleaving; zero hits on all 14,484 inherited order blocks; and
zero survivors among all then-installed selectors. The twelve schedule hashes are distinct.

For every Xerr and Zerr direct query I regenerated the complete 360-column dictionary, variable
dictionary, clause JSONL, DIMACS body, and summary. Selection variables are exactly 1..360. Detector
parities use XOR equivalences and a false terminal; the 12 logical outputs are exact parity outputs
with one nonzero disjunction; and the named-cardinality encoding is a complete at-most-10 prefix
counter. This reconstructed all 535,520 direct clauses byte-for-byte. Every retained direct
assignment is complete and satisfies every clause.

For physical replay, if \(J\) is the selected-name set, I recomputed

\[
C(J)=\bigoplus_{j\in J}C_j,\qquad P(J)=\bigoplus_{j\in J}P_j,
\]

directly from the frozen schedule and suffix rule. For all 24 mechanisms, both detector syndromes
are zero, canonical and physical 12-bit logical actions are equal and nonzero, neither support is in
the sector stabilizer span, and the retained supports/names match. These are 24 distinct mechanisms
on 12 distinct schedules.

### Thirteen formula/source/map tuples

| iter | selectors | selector state | state file | source file (stored) | semantic source | assertion map | circuit trace | assertions / vars / clauses | CNF (content) |
|---:|---:|---|---|---|---|---|---|---:|---|
| 172 | 304 | `a5c64ae41f474844ecd3ac41829331f54d419a81573e4f0e11528db0b49e25d1` | `9fd675be9712a28dd625fba7cce95f75a8a3b9bdf7edc3f398bfa8b13844d2be` | `99faca59521b675844d0c10eb12afcfe925f474d3eac9d5cac56e11537397b08` | `cfa261df8b148622c80248d398df20f1ff5a4cf3f04eb76a31b2795185cc6412` | `0e4c1dff0802376d495429ee629d15c60cc1552fd8e983759b137f29cbd4e851` | `a5ffa7d2eb47261e743f070fcd987ce0af24de64d4bf1db163ecf2fe94fee83f` | 19,186 / 413,646 / 1,406,245 | `f86b8db36af1df3877ca1d9dbafb171b6173ddc8b6c2f045a808dd6c71f98342` |
| 173 | 306 | `45cefeb847e0b57e1c1e393c63b72183036ad12b9d7492e0301f11f37b20f3c4` | `6db9c127d089667a6440b641cb3329310eeeff799dd3e3e70b7413c926502bf6` | `834ab9883121ad7083ff19fb96db10af97984af2c6b843ebefc83a40eada566f` | `315ab6dab68915822597c52a8fd0a9d1ce9e44d6c04e29189076a5e7c4e35dbf` | `c53f7f675b55c73d8890d3ae9e9fced6051eb63cc2dbaa011653d3256efa1435` | `5fd48ffaae3032dd7b156f1dfb630ad9923e0c91fca44e33a2617a3c7385b6fc` | 19,188 / 413,697 / 1,406,420 | `901195aa6fe738f45a55a1699b844bdae6492206e8bf7186d172cc6617473878` |
| 174 | 308 | `d8017e1ba54a3b231a281c304b19435d501dab8207f110af8f1783ebb093b585` | `79fa9c5d4ed63db04881274174a19610d56aa33dbc141d333c6368858cd020d6` | `4930d124e1916176c766515878eddc627c7e027640613bc78328306ce8344a64` | `2e798bcfa694c50f514ed410493fde2d5e83adea858a8e4665153b4c0769ff2a` | `1b454d6f95e07ccd88867bdd71c7a58da15a90ffcdf151b01e9c9c663b485b32` | `f87da211535f85ac9a3588a7d94613253e463f8dea9805d068094edda2cca5f4` | 19,190 / 413,945 / 1,407,673 | `3132e8d56680973c0c4feacf8623bed4c2cc14a23da5190cac0fb8e1965d58ea` |
| 175 | 310 | `93d3fdf433e1273136a34c6127c037947a49842613f280691eb08a3b421398bd` | `f482cf5400069a3f713b577ae9a1d666165ac32799679e4abb83e4b0dd953888` | `908613956ce66fbc528fffc37529de244ba87e094d2d3fac9c2fbd6d6b08c4ff` | `d01328922a56aa2d8c6adf93a728e6ffb964082c07f52a1bfa227d25eb72dc03` | `d1ecb3fb684b221e1a88b14ea69a836ef0f8425e2a509f7b5ae71a89d5f2108d` | `83deb29330261fc914a2645fa03e385577c41764ea529cd21626641a31605d0e` | 19,192 / 414,035 / 1,407,987 | `ab8a4eb18f1bb2d649bb6d132efd4cbb32da7dcb235e3ad29900799f1d92a9df` |
| 176 | 312 | `f5172be432d80c13390fc261c90eda59c9adf8439e06249d5e9df31b7c9b7abb` | `087b31f441a7f910f49d19380fa2b3e989e7914fb04ba9cb350bd34646af9cfa` | `97ebb046b934f0b5705674888bcbcc220eb858034986b9ed0c6d201ee61581bd` | `0e3f9d6a68e550d8f147a9c45fe4884015405e0eb0ec6989dcd85cfa2229f096` | `21ed101aa81afd310dec6b280b07889d3460350638402aa322467f6c359c1db7` | `b9c5223a514f6dd0d42b2addabcaadc45bc8322b963b8d485206077a8b00d315` | 19,194 / 414,201 / 1,408,749 | `f1d954e3e89beaa2aea1584d125388f769bed6d775d945365ea22a1bd3a09130` |
| 177 | 314 | `f3479e3321fb80021353c16a6060470e835a60bf56b45fcd8a10c472a71416dc` | `5a10e3611f5d927b0733805c2cd19f7c2e367d2c5f96637f29cf33c02bd000dd` | `4aa6f965c533b8894eff3e8aa38708e159251f71e2c9402db3ad2a2ccff0dcd7` | `53d72b4295b4b91573736ce75821239096decd870a1bd12fc9edc0b4fa77c5ac` | `37454e4ccf1c75ab45be3ff9feefda90503b4821076f6a921f3c7d8f812ab420` | `b02a3171e7e112f5b3ddd972120756561e718dd2eddd2d14d663c7f884088bf6` | 19,196 / 414,393 / 1,409,615 | `1884a54f54aa8e688f4d1975dbd8d93923a172b97ca25089685d314a51bf5d41` |
| 178 | 316 | `10e3bd3b219618634704cecacafe81daaf5bfd967bf0d370d38011bde6654975` | `8b0fd21b1c83ee7ce13b0f48f2114d8d43df168a72adc7015f810609548a56ef` | `4b2c78035858b60cb2f1e78c9a093f6f3d20c0b878c33bce871cfe03b18a9ac0` | `c8584ab911b915fe905cffab6ef47f2380181133cf9739a00a2b5c6ff3979643` | `47aa83c91ac7b0a6ea4f9a137b4475bb70ace9fe589aad533d2c5aa4c3ebf703` | `7b1725e7e00e440475410685a40c7b664b631751b02376d47eecacd6b128f0bb` | 19,198 / 414,581 / 1,410,637 | `f89fb3e91ce6b7c9ffcf6397cd6ad9ab656626e0aad8f3caa34318782d02cc79` |
| 179 | 318 | `2e1d8cc563e1a97fced13df395429ccc1b94af6e222025f6bee5193de9d3797a` | `51ff749069cef3199c18dba13ca9f804a4f01b9f02cefc575826dbe063d10bb0` | `3b9e1f0aef65ef16cae91eaa2503dcd497a9db22ff425965266cbf0ecced93ae` | `9d0d1bcba0639c661a9b91d98a095ddfebba77cf5e75901aa4da3945ab78d9f7` | `197fca78ecb4b3b4cad18dd82e4174aea0cec2c0cdf5d4d0df9914eec9d0830f` | `1a6933783b1a90d0ede02513b1af96c83303c3c49e9c6a4966d1b17511a69593` | 19,200 / 414,850 / 1,411,964 | `6ce9694264656a00c1f88b54b28b469a273ca7a0c658f949f7d51aa2fae837a8` |
| 180 | 320 | `38f0d11bc0cc8ce391b2321e8ff959b31753bcbb439edfda22a003f17456acaf` | `abf177bea1690e1cbd5cd54dacc6132f3b7c254fe9cc2807f21c051a980b5c3a` | `d548c4f6d08d07fd239ff6fd2c2984859fc23b1640ef5caf17dcf2fdd7124f9f` | `e52e8e059fea280fdb2f02e661cad6712ae594686a159f3f0840eeb09d5fba30` | `526b85387479725f11065f33e5c13375698f1682be9a62c66dabb46e24f8d20d` | `76255a030b399e8a6b447b97e587c21c25cf5830b6302589466249c4a99fece6` | 19,202 / 415,041 / 1,412,833 | `c9f59fd026c9b372d81b6ff7a82e172f2a46d42d6fc1de8e79427d63cba17919` |
| 181 | 322 | `04f9c656d03bf5a671d70149b83f9d82314156207b1e756ad229766810976dc3` | `9bba3918c4b07b214ac3c34bc3150da303042289c6b8d2e2e3c7f9f017c67ddd` | `42d0abf6fe72e92c96daf13d1765cb56fd7c9612baf82719b3f026cf6211c5cb` | `31c397bb1c3233c9b8e7e892c5dde3ebd3b389556b97953288b0c279d0c68dc7` | `b1ac1474e20059b4abc3126f34dec48e0254e1a093faa0620ce2ce9eb82ac89f` | `b2193c9d8ebc3df74a31f6aa148cb3bd68b27b807bf203db56ceb19675d1e55e` | 19,204 / 415,301 / 1,414,118 | `014c05cd6cade4fbdced2078b827575f8f4d87cfe6aa51a653dde81716f70ed5` |
| 182 | 324 | `91a01ad658980814c3c250a251e879727f0c2aa3222f222e0ac5a15814316d62` | `9720b098c5608ccb48ac43bb45b629848e798c2e8029f50dc8005ba39746332f` | `e80261c0b552916155b2dd59c2cae3b91f18b8141de44eb5205c72c00c3dccfe` | `ab7f43da858394296f4af5a22b0ff70979ef3d0782356cc9c5851a23f84c0c87` | `1fb9e1ae6fbdc363adb6a8b6e762d8ac1c94be2d07e4532e6379697c37fcd119` | `9af2ce66ab12049ffdc94dd569b4e385ea27430fd4b67b5495d4ce7f173c2460` | 19,206 / 415,472 / 1,414,905 | `ccbccab56ba829a93a149723ec2dd63d3650e4fd51435378f437848cc08cacc6` |
| 183 | 326 | `be7c8f7ecae6fa913fb94fc6d0e2875e1803f1ed38c0a9192add31904e370cb3` | `2c7600de5ce6e561402ab8b130da43b07526efc49451f59fe6261992dda25894` | `081b18d1c37abddc0ab147c274812aa7fcf03c62bddb58a62582968841c04b70` | `4d60f8c878aa2ce50954b9cc9669a6f2f23b3e1dedb00d360d73365f64205fd7` | `057cd52de9096dc1aad4d077a9ada9b2fb259bff1043bd02c028d6ee552ee04f` | `38dd317c644b0c4fcad696bd915cc8ff9ca8394bb2f47f179866af480524c2a2` | 19,208 / 415,712 / 1,415,944 | `0704953638a975f48b40b70ed4e6ffd21f7e3e00960b08ddca9f4b81b7a86d8e` |
| 184 | 328 | `7296aa70690e01852519b78826b173af35998cec0e9c124c46ea30101dd0777d` | `3b128ef192074a3bc0c163502e97eff99ab9d15c546381e98e1e178471552d7b` | `5eb1607bebea7bfc44b693a4a3a9ae19f2ab5ae498407290863b34d6eb9b66b0` | `d601f297e8b2a1b7d6179d19452da8b0abca2e4f16d7404b6395a8254e949268` | `4d3367d47442ebbe0be483bb5fb9f79b974b6ce8af66e2030bf97a077757edc6` | `f1d797ca7cd570eb232c07c22ec8928307ab8a7a16a4d37b9e71701ee065f3fe` | 19,210 / 415,793 / 1,416,404 | `2b0030fd15b0ef8154e2dbc37508e03481f11d8c876c4fe59e6541cb3bfacd62` |

The `assertion map` and `circuit trace` hashes in this table are hashes of the exact decoded content
or stored trace identity specified by each metadata record, matching its binding convention. The
counts sum to the all-clause total above.

### Twelve outer assignments and schedules

| iter | solver assignment stored/content SHA-256 | independent assignment stored/content SHA-256 | parsed values identical | raw/compressed schedule SHA-256 | interleaved overlap/whole-check pairs |
|---:|---|---|---|---|---:|
| 172 | `4ce20dd4f2fd2a5f684e252ed78a618dc81ca1243008cb68221e864bfa2da6ef` / `3e19dec26f60f1ca1b29f3a5a320b9212b0390e908861d16a93972389105f233` | `16d942986cc81d702828e52a2280885c729b774aef9bdb6722f1f54b3a01da22` / `c6f12d66643cda8609fad2f87cd07753d5b122ea33a8cb6add18d3cc28d35893` | yes, all 413,646 values | `b15efb009a9aa5d4e44d9b4ad684536b768a09a03c9a78b8fefe0ba2e428b637` / `e43ae8ecd69b8411944f985195dc29b8cc10295fe875f9ba4cd3c0f2d7e529e0` | 37/202 |
| 173 | `9321d077312d96471b0c1f84475a5fb0b9675272a655119beae146f61e6b4a8f` / `aa09b86d328644ffb0ace2593efb74133d847c952e6ffe1c7bb917694fecc574` | `b8dfe3c6b35191ce9ddadc235f1fbc78b1a671c2f4090c92cf01751dacc6f8a6` / `d55ba8ff7dd8ee5a60399c331c6bc611214dad2c77d66cc075ca3dde873c4e76` | yes, all 413,697 values | `e412213d08355b63fe878e3dfa2f2c7ae56377084b7b54e18b7a710de9038a99` / `42b8942e6ee9332f4091563398f2af4a2eb0b83015f0d86cf7b306db3b573979` | 179/525 |
| 174 | `c1fddc798a79256c7c3e94853b514ad21b450269aafa0c9a30265e0db9e806fd` / `757d1cce1af883b10e85d5d211ce65673663a5aaf8519d293b24cc2f29dfed25` | `9a238c8937070c84af7882c423e0d2a14f09e5390d0b937acb3fd41c6a4e29b7` / `7cebff6a0a28e598d5a765086387c379659eadc17a4bcdcd4b15beda626cc9e4` | yes, all 413,945 values | `f2c49f5f64cffb931e0f9508501d543e292874889d4fc71b7eefd5aa555eb934` / `257fa5e7cace1cf7c5e14e3c9fe8767ef60fefb5e9ab19baebcfde8afaa06158` | 179/542 |
| 175 | `1032c3a1c7accb76256677690b14526ba1ad601179f82bad366b7351a718743f` / `87d8e77b66c7505e72a2736a3793827a4494c9e9ced3334d890c121cd3b46f2d` | `699f2f2206ba051ffe0c73b43463fdab0f2652e06d0df55fe9f1800314830f2e` / `ead9eb2b4dfb98e8fbf14a7a5c5cff7b32483fe5eff2d64fa4c6fba279e899e0` | yes, all 414,035 values | `4c0e0f848cee48b0d005a747b8db5212921bdfcf156d05cb1dcb1feeba9b4b81` / `a262ed3b2f9d2df3e2eb381539a6ecf483261dd129b59892f1702ae72c14b844` | 252/619 |
| 176 | `bb323aa412697bfde56e2cfa377adeeda18677537057302221e584059c3b1d27` / `e727919da33e32204b88353c1045332cf51de605e42e2eb89699816f5d032612` | `ad3516fa4198ac75bbf5614ac91d5c1bca972a58b4196e20a3da47ce7b765f92` / `bbd2a568a3f4d03567a9f7076875a3a5d9a5dbf189f7fca6c425b160a10134ba` | yes, all 414,201 values | `b953e8efd9210dd812988641c42bb7ab1845471491c7ed6e56c0f54549411518` / `d5c9f82aa82f0aeda403eb1079e9e1f0fd86c56a4a4d71f16390cbf79f4b02a0` | 188/550 |
| 177 | `a58051fc061c6fb51f8d16946ff1b09dcb9895972a9e2ebdee90d3209e046070` / `2dda74e76c42c1959e65fa804c40dde0284e987bf5cf6d364a221943e432a991` | `294171e3d3e4df6e711cd01f89cffe9e607a3aa2adea542fbc564590e81b6998` / `2c5f8b6d37d0849bd05d70549d41c471e5e31a4f7a732c0c01626bf2fdd81c30` | yes, all 414,393 values | `45387b7305f78b6241ae5d4178d86eecffc25c300531a4b3ad4ab9d61ea7e386` / `5cd394269f40155767be7837aa379032a8905a1d1636a5c7458e84740b336fe7` | 118/424 |
| 178 | `42e05bbb3131c50fee6970a95707f0dbf3bfd41685a8e7653906ed6a287053c4` / `0122eef1d5ed485385c16fcff3cbd470cccebe637606fe98de30385978b2cfa7` | `8b9d8175bdb95063cf530d696ac529ac7ff6f52df673ac3a65acc4f2101f115b` / `06c8d7b37679b6ef7526c9e7d652b02c09dc1bcee4830854d9fdcb69bf3cc4dc` | yes, all 414,581 values | `3113f426f65db2b3e9ff764f2513ed4e905aaf3df8b854af39ae6f39584be64b` / `10f1bd9b95802d41fc415c6902aafd4d4aee24d1c77693ce3d1da5b103c38602` | 177/508 |
| 179 | `83f999a128ca2804d74aef46a887f9c76cda5e4f47d08d254413ecbc2cfe6cec` / `e6aaf2f9b4ec8eefcee794c8705cde14f860c9c6db2b141112c5109322d491f9` | `b58e2f7fb8380c7d716e1549f1a64214dbc55bc989da3b20d5e5ba04ecb21e3e` / `adc92f5b865634779460a5fc41dc711e0fc2a897cdea0fdf61c4a3a267d7d67a` | yes, all 414,850 values | `5e4671b96f8c6028e169a6946e6fee5d88a14ec0c8a202f8707377a21fadff87` / `6e72a3258b57ed970096b6f7f3b3e2377efca2eee3d68161b06dd8598fd60195` | 184/525 |
| 180 | `b6e0aa2344e04e4699409808e47e0f3250ec91280d393010cc2ce8dbf916a024` / `a957c0a03f4cae5a25762dada3952d3bb023c83b45ddbe627e8377b5226bd3ac` | `8a45a67280e82e3c93f355e8ba0cb80069cd70229f4b5743e140966a7e94694c` / `2a0cace22bbb03c54015991421ef266b1eb053336ca3f524f8e07d56cc30e0dc` | yes, all 415,041 values | `8a7cf1d5ebce32c0b231cd2ce7d2d5c1c199530fbeb8593f89901099e59eddf4` / `5fbb4a30b3b9c0aff87fe464ef65ca7017f11ecdbc09f0577905117c16349374` | 175/571 |
| 181 | `2b3b254cd46bd7923741bcd0cd3786f08868c03d44cd8825e4ed1abb10abc2eb` / `fdfce2a05c52235e805de6b69e2f261aeca34f3e0f5ef7f327a1c543fc180698` | `a0bf333c0ba4cff3896c1f83ca6bf710b192498d9228223d871e1a35fdfbd225` / `5f81c03bf67a50ad230116c2c25a5013ad4fef547c9e4d356932c0da02f71c3a` | yes, all 415,301 values | `33acf5de39aee12d883187212854fda0430bba45662050814cc6cf533de561f8` / `f7fd789dc5bf357a3cb4c76d69b0f0bd62efb71474d9027da74f731c3b0ed72c` | 167/504 |
| 182 | `2dd16eec8aa64ae5c846119e247576e34f05654d8b64f7d612b6b11f8d42b404` / `d656254ced8aa1fc7017886922c81057cd62367ee00393d1c7218b077f8e9038` | `8084bc073660d75d8e23c217242d2e4365eee747cd735ea619faf588f6219978` / `f1de01d0d21915b22161f544e6fda49b987aebcf4374ec1750a319cabc001d63` | yes, all 415,472 values | `3e1768ea4bc6a5247c81acc85d841788dae3f6a04d5f24589a16d90e0fe336f6` / `f5a15b667e345654aff1c0f8972b203edfdd86a5e5aa3843a18ce21054f03aa6` | 236/579 |
| 183 | `335acdb82229f81679aa47fa48f25e2950de6afa12cbc45691b8148337fc09e0` / `a4418ff2c18c6e5786d032fd48d5c5071950f936b36b8cd83af73a43a4aadd39` | `86153d154b0ce75ab714a41b435ba438a34b1e547bff6ffd13dbe44c07dd6279` / `6eb5467f612b10180a321d0c9d5c8556c2ce7490c12a97676feb9ccd7040220d` | yes, all 415,712 values | `d53379f53b00e1a5451cfacfc6ae84aa9a939df123ceec3de13e770d320a097e` / `3877d8855ead414cb5a25f7c8541b723c2888e864f6567a7900c6a27b16a44fd` | 200/522 |

All twelve decoded schedules use 360 compressed layers, have all 864 edges exactly once, have zero
conflicts and zero MC violations, and avoid every installed block/selector. The final column reports
two independent interleaving diagnostics, not acceptance criteria substituted for the complete
schedule audit.

### Twenty-four direct assignments and frozen physical replays

| iter/sector | CNF SHA-256 | vars / clauses | assignment stored/content SHA-256 | weight; selected names | canonical support | physical support | logical parity |
|---|---|---:|---|---|---|---|---|
| 172/Xerr | `57447647ff29ba18c4e3ec7120b73ea5a224f90c462d4442c03f842ebeceb594` | 5,943 / 22,352 | `ee956a4634e65666d25552e8bff2f5da17dc243a8b1bb0d8194171b863fe5283` / `eeafb930769edd484289d3f4e66c2528eab1207ee3fca6951665842580e812da` | 10; D:28, D:54, D:80, D:96, D:104, D:111, D:112, D:136, R:35:0, R:51:2 | 28,30,53,54,69,80,96,104,111,112,129,136 | 28,31,54,69,80,96,111,112,113,119,129,136 | `101000110000` |
| 172/Zerr | `b1462cda24b3e612f9b2aeb34e9441aa1548b2502c536c34a9710f204bf9a447` | 5,973 / 22,472 | `af6622b3ecfb348484ed950f694cd78adec4e17a39d4d23c0bc98f10622530c8` / `b658828bd4fbe22bd68aca6ae18848f8c7a05bc03463bc4ba2d131d6b4c765db` | 10; D:14, D:38, D:39, D:63, D:74, D:90, D:98, D:113, R:13:2, R:43:2 | 7,14,31,38,39,63,74,89,90,98,113,114 | 7,14,31,38,39,63,74,89,90,98,113,114 | `111110111111` |
| 173/Xerr | `364032c6fdf30d29d02963ed09eef444d97e852387584bd1a454c7769bed4366` | 6,000 / 22,580 | `a589e9f59d90e9be0d68b7f5630e4b76b34e8dcd9737dc6ef52cd3ae7dd59cf8` / `63b1f067d509cf113556b8cbe3e0e11759aced0ae846cf983944a555aa863624` | 10; D:26, D:33, D:109, D:134, R:0:2, R:5:1, R:5:2, R:7:0, R:24:0, R:56:1 | 9,18,26,33,42,57,58,78,83,85,102,109,134,140 | 8,18,33,57,58,78,82,83,91,99,108,109,134,140 | `110001110000` |
| 173/Zerr | `53fb58a033db90972674c50be6bc54cd8d648df908794206270ef5fc92b972ba` | 5,931 / 22,304 | `91c5127a610543c2cb87cc4b5cd05ca7d3377c15c3e3fca013e1acb0cc668542` / `e58e0f4ed9abf20aaf747b7f014b48d76b18e5547825bb0e2258b290b8c1f247` | 10; D:130, R:58:2, R:62:0, R:62:1, R:64:1, R:67:2, R:68:2, R:69:0, R:69:1, R:70:2 | 50,52,55,56,57,58,62,63,64,65,116,118,121,123,128,130,133,135 | 52,55,58,62,64,66,118,121,128,130,132,135,139,140 | `001010000000` |
| 174/Xerr | `31fea0cf5c09b3633a82d9b1bc434a397f428699907bf583aaa12e2ec7eeeab5` | 5,942 / 22,348 | `c0dd0bc20d7135a2548bb46d242b621a34101d087d6b26cdba55ab2ea0882290` / `541529d283c4815831fa25f38e3b5ea2939176b6ff4a4afc2a76b136ca350d1e` | 10; D:9, D:49, D:56, D:85, D:107, D:123, D:131, D:132, R:0:2, R:55:0 | 9,49,56,75,84,85,107,123,130,131,132,139 | 1,9,49,57,75,84,85,107,123,131,132,133 | `100000000000` |
| 174/Zerr | `11febba288d2c77f008b3729b7e12632481984d728696210b00975eabd62509b` | 5,897 / 22,168 | `a57ce82d1cf7fc45fdfd2c959665e19b9a18b5fb8a7cde195bdb8a7c42e8daaa` / `c857b415f4e8989e25c81b3b8e2661393054a66a5d40926b620b1e6b539ba074` | 10; D:14, D:22, D:23, D:24, D:46, D:62, D:98, R:3:2, R:12:2, R:20:1 | 0,8,15,22,23,24,46,62,63,91,98,138 | 0,8,15,22,23,24,46,62,63,91,98,138 | `000110101000` |
| 175/Xerr | `170cbdecc53d8ef48836ac58d5cac1f6ab807377da2c97d647eae9a1ab830951` | 5,938 / 22,332 | `aa42a905b38c8b0336f2f91d1e2158ca6f42ab87ac3b81b8da6339317c37d57f` / `9a47997aed30ed5dd36190ee546f68d1870db13ffab0e0e405d793bfabe2fc64` | 10; D:27, D:36, D:83, D:130, R:0:1, R:8:2, R:16:0, R:16:1, R:24:0, R:35:2 | 2,9,12,17,26,27,30,34,36,75,78,83,94,100,102,108,113,130 | 2,9,25,27,30,36,42,75,78,83,85,99,113,130 | `101111101000` |
| 175/Zerr | `2ba299bad9c04466f2902c461a0cf5ff45a20d84864185ac43e7afe434c913e1` | 5,918 / 22,252 | `7a82c34b73c720ff36a0fefa918a57d33c89df3f7557428a3817970608a3d181` / `cf2eec8b3684f14e0d8a5ec68f2ae2b9a748c8661b84ec2756a63eab08cb6a14` | 7; D:102, R:35:0, R:37:0, R:38:0, R:41:1, R:42:2, R:44:2 | 29,30,32,35,40,95,96,98,102,106,108,113 | 23,25,26,30,31,32,35,41,89,91,92,95,96,98,102,105,108,109 | `010011000000` |
| 176/Xerr | `1388e08a53afcca32bfced4bf63850c702cfefe0d0b48653a8248dd4e9da14fe` | 5,979 / 22,496 | `8d3cb25b25947871bb323bce22f71e783042269073b736a1254848fd06c8450b` / `1753eecb316ff60e4395c378dd64aef246afb0f3ba249053e09d1897740d23b5` | 10; D:1, D:75, D:81, D:83, D:106, D:131, R:6:1, R:7:0, R:24:0, R:31:1 | 1,8,33,75,82,83,84,91,99,108,109,131 | 1,9,26,33,42,75,83,84,85,102,109,131 | `110001110000` |
| 176/Zerr | `d33443915e2042cbc6530c168a085d613454ae961f7ee0c697f00ebe847dd4c4` | 5,910 / 22,220 | `2246bbe53f116d03f2aa42fca65abd6cccc53f94a0a05c116d6e8871ac1f7706` / `fe5b00d05b6bd85b4e35bcdfe063ff10ea0dea3c16e0a4f29b75ba1774beecb6` | 10; R:50:2, R:55:0, R:58:0, R:65:2, R:66:0, R:66:1, R:68:0, R:69:2, R:71:1, R:71:2 | 56,57,59,60,69,122,123,125,126,128,129,131,142,143 | 43,46,49,52,54,55,57,58,59,62,71,109,112,120,123,125,138,139 | `101110000000` |
| 177/Xerr | `22e3b858a806a606972db01caabd5c00961fce3f3c583c644b545a83f13db40b` | 5,932 / 22,308 | `26a06d4b034e6dc6427f24e5f86e9ed67c038d869b7515a3de75a82150be148c` / `7e780616fa0ea7d8563535ae2ae8b35837e4615043b77ca0e1556efff459bb9a` | 10; D:34, D:43, D:67, D:77, D:83, D:110, D:125, R:8:1, R:18:2, R:57:2 | 9,26,34,43,67,77,83,92,93,102,110,125,126,141 | 9,26,34,43,67,77,83,92,93,102,110,125,126,141 | `000001010000` |
| 177/Zerr | `65b9cb34abe864d8a87a8e13c9698fefee8aaa98a99a608ab4f3b81349e82775` | 5,879 / 22,096 | `becd26a182e88055a9fd0687390ec7ced28a6c41832da846ad40694e5f34e041` / `480e52ac4336b7da8267c51b4a38e3af6a4b14bd72fc4f230a1e330aa024c3e2` | 10; D:114, R:50:2, R:53:2, R:54:0, R:56:1, R:59:2, R:62:1, R:62:2, R:66:1, R:67:0 | 38,42,44,47,50,54,55,104,108,113,114,116,120,123,127,129 | 38,44,47,48,50,54,57,61,70,104,113,114,116,120,121,123,127,129,130,131,138,143 | `010010000000` |
| 178/Xerr | `c4007e530c5f1cb67dc2809ec45f044a2891b16a68d1544e3a66c172cf52259e` | 5,900 / 22,180 | `cda610863dba398edc28b2ea312443a5dc3dd3f1f54b876cc73ab43984c7ad29` / `75526bb3b1bf7b3818cef0088d77be174b286ff16a7e7f91b83a0d9f4fa3517c` | 10; D:55, D:66, D:126, D:132, R:43:2, R:46:2, R:47:2, R:50:0, R:50:2, R:55:2 | 42,43,55,57,61,66,68,116,125,126,127,128,132,134 | 42,43,51,52,55,57,61,66,116,126,127,132 | `000101001000` |
| 178/Zerr | `060aa015786992b40333fd94b431b76fc9692e631a48f915e9b6b6ea353b8bfc` | 5,913 / 22,232 | `2949e236b861b5c09d8f50e5adb92d41e6fde9ad00150fabd8f8352bc010d7f0` / `fedadeb3bcb230b5cb9ed086b4087d420eba7964ec0e0eac37548bca31d5185b` | 10; R:4:0, R:14:2, R:20:2, R:27:1, R:33:1, R:37:0, R:46:0, R:51:0, R:51:1, R:54:1 | 1,2,8,14,15,21,30,39,40,42,45,74,81,85,98,100,103,105,108,113,121,122,130,131 | 2,8,14,15,21,25,30,31,34,40,42,43,48,64,70,75,81,85,91,98,103,116,117,131 | `110101111100` |
| 179/Xerr | `3b97a319012934c6320af8a73d129ca08bb4205bff9549fcec53a051176e179b` | 5,914 / 22,236 | `ed7b2913b184f109203fe4755a2dac084b2593b7404a6aff6aa8e3a225e4952e` / `0b5e1f05a747c4bf87ed4fea7b46812ad20253727da43271450d140db1101b4c` | 10; D:70, D:132, R:57:0, R:57:2, R:58:1, R:62:2, R:64:1, R:65:0, R:68:0, R:71:2 | 3,8,10,17,58,59,61,65,69,70,74,76,77,83,126,132,136,137,141,142 | 8,10,11,14,17,60,65,76,80,83,132,134,135,136,137,142 | `000010000110` |
| 179/Zerr | `107d2d11f3943cc39eb6452a5b3eeaa901a96ec034c108d7ebe21399d01059f3` | 5,921 / 22,264 | `710eb0effa93bd6ab23501304943a83ee8824eccfcf76c2af9962791e0b67010` / `7e2000be3d6ede90d09f711baead855eb61cf51756b5b10def77846f6b4f4180` | 10; D:59, D:66, D:76, D:125, D:132, D:138, D:141, R:1:0, R:5:1, R:64:0 | 59,61,66,67,71,125,127,131,132,134,138,141 | 4,52,58,59,61,66,71,72,77,118,125,131,132,135,138,141 | `010011000000` |
| 180/Xerr | `18db4978c3491c7158a0d54ef9d18e434b110d78fb2c4c8cf6c60e74f3b53157` | 5,979 / 22,496 | `b2abbe8514d091eeff15b475d606278052b979593f1e52d08178625e86d3509a` / `b441f9000929026cda03e34493f1e0bb42909149c94fe79ed0b91646985389cc` | 10; D:140, D:141, R:1:0, R:53:0, R:55:0, R:55:2, R:62:0, R:64:0, R:68:0, R:68:2 | 3,8,10,14,56,57,70,71,76,80,130,133,140,141,142,143 | 1,2,19,48,49,60,63,64,65,69,76,79,85,122,131,133,139,141 | `111111000101` |
| 180/Zerr | `12375cdfd73ed049437fb955e789959986c1d091e0ea29d23598530424d92782` | 5,948 / 22,372 | `052713b6833ca2267a8a61041141e2ed897da2c0472e6d640070d1481398c159` / `d54da0c5603f5591281357b9f9f7a58eb8f9eda90fad4256046c7018596f2ba1` | 10; R:21:2, R:52:0, R:53:0, R:58:1, R:61:1, R:64:1, R:67:0, R:67:1, R:68:2, R:69:2 | 18,41,46,52,57,62,64,70,71,75,106,115,118,121,129,134,137,138,139,143 | 18,40,47,49,50,52,55,57,61,62,64,71,75,107,115,118,122,124,129,134,137,139 | `110110110101` |
| 181/Xerr | `2793fe93ca362943b403d8964f5e0bb6d31cd391dfce2431ac6e83eab781b041` | 5,928 / 22,292 | `4f2d8953be12d0668c8006ca382b3aefee9cf3ede920c4d79008f03f928a2976` / `7d48ff2a9c6e5971ec75879640d2499bd4832cefb29ed760ada02be3a4984fcf` | 10; D:126, R:14:2, R:15:1, R:24:0, R:31:2, R:32:0, R:46:1, R:46:2, R:55:1, R:71:0 | 1,25,33,50,56,66,83,99,107,108,109,126,130,139 | 1,17,26,34,42,56,67,77,102,109,110,116,126,130,139,140 | `010001110000` |
| 181/Zerr | `3b2315c062eabd44926711b087440de079f444fd42a0ef63df9dcf5c7e34b8c0` | 5,910 / 22,220 | `24ec26644a693009350f672325f532cf21e21b8e9b841f23f6ef11682ea3de95` / `3a839fe13083fcfe932af7632488d6badd5d08e63f19bfb5aef2a129089e2d87` | 10; D:68, D:69, D:134, D:135, D:137, D:140, D:141, D:143, R:6:2, R:68:0 | 66,68,69,71,132,134,135,137,138,140,141,143 | 56,62,66,68,69,122,132,134,135,137,139,140,141,143 | `000010000000` |
| 182/Xerr | `80747e006d230c72b2e410c46308c113e9aa13e4d3ccca5393ce69c81d7f0585` | 5,957 / 22,408 | `4936dbec77c0b4723932c8478aa6c468db7b6939cca1b6b8d800dc8057220622` / `7162a762310419cc7e406a0a5746490f2da5bad221c618eaf0ec6c528c844b9a` | 10; D:68, D:96, D:138, D:143, R:3:2, R:10:1, R:13:0, R:44:0, R:64:0, R:64:1 | 6,10,21,60,62,65,68,76,79,87,96,97,119,133,138,143 | 6,14,15,21,31,45,46,68,79,87,88,91,96,122,128,138,142,143 | `010001110000` |
| 182/Zerr | `7a24b1f75d4da8c9ce227f8cc37e9254b298d265604f1d9affcd1eea10412e63` | 5,932 / 22,308 | `87cf80b342c7ed558daa5edf91b22bb96726c5b82fb166b3a4b5ce4f5ad828a7` / `8b6f0c63a8d518bc5be9b592712f02fb6781fb533adbfa845f57f67abff39243` | 10; D:119, R:24:0, R:33:2, R:37:0, R:39:0, R:40:2, R:43:0, R:44:1, R:45:2, R:48:2 | 25,31,32,34,36,91,98,100,102,104,109,110 | 12,18,31,32,33,34,37,40,46,78,93,97,98,101,102,104,108,113,114,119 | `010101000000` |
| 183/Xerr | `a94fcb047788bb859fb325ab8a571ede20bab3fdb9db5a300bef07d6e7032573` | 5,923 / 22,272 | `9c3896af53628de1ada1cba0311bf2b0f83f65a6c72bee4249024ed85d5c3875` / `d8e451117fa6cdf17a7d3110cf99856d56c03b1fd3109a4fdcd449839947f7df` | 10; D:49, D:58, D:64, D:70, D:88, D:104, D:121, D:122, R:3:2, R:60:2 | 4,49,58,61,64,70,87,88,104,121,122,138 | 4,49,58,61,64,70,87,88,104,121,122,138 | `100101000101` |
| 183/Zerr | `8b74d31a8473519a80848b5a08b9196df8fc1ed9a85d9f734136350ff195769c` | 5,933 / 22,312 | `c5af6f31484af3e8c02ee607596f8f0efe5d54cf7f40a0113a43d7b6ad2f519c` / `4bc863d8b582355b83be31924ce5899c1cfeb14cf7c18d11c532319d64ffa9fa` | 10; D:5, D:7, D:15, D:31, D:48, D:53, D:63, D:129, R:11:0, R:12:2 | 0,5,7,15,31,48,53,63,81,89,129,137 | 0,7,8,15,31,48,53,63,71,82,89,129 | `010010001011` |

The table exposes every selected name and both reconstructed support sets. Its logical bit strings
use the retained logical-dual order. The Xerr/Zerr order follows the package sector convention; no
bit reversal or sector swap was used. All 24 assignment files were parsed over their full variable
ranges and all 535,520 clauses were evaluated.

### Atomic 304-to-328 selector lineage

At each transition I required: the old selector list is an exact prefix; the two appended rows are
the just-replayed Xerr and Zerr mechanisms; each selector semantic hash recomputes from sector,
selected names, data support, and group kinds; the iteration record is exactly the last state
iteration; pending and committed payloads agree; `state_promoted_last` is true; and all payload
state/source/formula/record hashes match the target files.

| close→next | selectors | new IDs | selector state | state file | source file | semantic source | CNF | record | commit file SHA-256 |
|---|---:|---|---|---|---|---|---|---|---|
| 172→173 | 306 | `r100-i172-Xerr`, `r100-i172-Zerr` | `45cefeb847e0b57e1c1e393c63b72183036ad12b9d7492e0301f11f37b20f3c4` | `6db9c127d089667a6440b641cb3329310eeeff799dd3e3e70b7413c926502bf6` | `834ab9883121ad7083ff19fb96db10af97984af2c6b843ebefc83a40eada566f` | `315ab6dab68915822597c52a8fd0a9d1ce9e44d6c04e29189076a5e7c4e35dbf` | `901195aa6fe738f45a55a1699b844bdae6492206e8bf7186d172cc6617473878` | `45cef7c736e223accc95c5dbe7d452bac0edfd7d54a982f36fd2d160d120af38` | `05b29a2b562381094307ef57581bb42d2116e79b3ff6763bc340208758361b8c` |
| 173→174 | 308 | `r100-i173-Xerr`, `r100-i173-Zerr` | `d8017e1ba54a3b231a281c304b19435d501dab8207f110af8f1783ebb093b585` | `79fa9c5d4ed63db04881274174a19610d56aa33dbc141d333c6368858cd020d6` | `4930d124e1916176c766515878eddc627c7e027640613bc78328306ce8344a64` | `2e798bcfa694c50f514ed410493fde2d5e83adea858a8e4665153b4c0769ff2a` | `3132e8d56680973c0c4feacf8623bed4c2cc14a23da5190cac0fb8e1965d58ea` | `eea792dc4ffd51e291a1010a95ce5d74e68d50d302b727d1176c50521a5747fe` | `a49d587132485b82f8e9118b9f32da5fc63b6f57fc95b5cf9eddbdadd8182f29` |
| 174→175 | 310 | `r100-i174-Xerr`, `r100-i174-Zerr` | `93d3fdf433e1273136a34c6127c037947a49842613f280691eb08a3b421398bd` | `f482cf5400069a3f713b577ae9a1d666165ac32799679e4abb83e4b0dd953888` | `908613956ce66fbc528fffc37529de244ba87e094d2d3fac9c2fbd6d6b08c4ff` | `d01328922a56aa2d8c6adf93a728e6ffb964082c07f52a1bfa227d25eb72dc03` | `ab8a4eb18f1bb2d649bb6d132efd4cbb32da7dcb235e3ad29900799f1d92a9df` | `3fd471b4896c8a85eeb7f6f38cd1aa16962d2c89654bc88541bdc6e44ba72432` | `6cfb0141e72618e2c857241acabd6ed8665e8d55d2467b866622d5f21e3bc9d3` |
| 175→176 | 312 | `r100-i175-Xerr`, `r100-i175-Zerr` | `f5172be432d80c13390fc261c90eda59c9adf8439e06249d5e9df31b7c9b7abb` | `087b31f441a7f910f49d19380fa2b3e989e7914fb04ba9cb350bd34646af9cfa` | `97ebb046b934f0b5705674888bcbcc220eb858034986b9ed0c6d201ee61581bd` | `0e3f9d6a68e550d8f147a9c45fe4884015405e0eb0ec6989dcd85cfa2229f096` | `f1d954e3e89beaa2aea1584d125388f769bed6d775d945365ea22a1bd3a09130` | `05a67311c5e3db9a38289e7a4654912ae08e05fe378da9ace2bb485417d53dd6` | `960e5d8c7dfac8f0a4690fc16f9ee13296edb7c002d7882f68f33dbec011edf8` |
| 176→177 | 314 | `r100-i176-Xerr`, `r100-i176-Zerr` | `f3479e3321fb80021353c16a6060470e835a60bf56b45fcd8a10c472a71416dc` | `5a10e3611f5d927b0733805c2cd19f7c2e367d2c5f96637f29cf33c02bd000dd` | `4aa6f965c533b8894eff3e8aa38708e159251f71e2c9402db3ad2a2ccff0dcd7` | `53d72b4295b4b91573736ce75821239096decd870a1bd12fc9edc0b4fa77c5ac` | `1884a54f54aa8e688f4d1975dbd8d93923a172b97ca25089685d314a51bf5d41` | `79fa37353f5eacd98f44eb7d8c1dd4d21fb7beb48b86ee68df9208e7dbe9aca9` | `1cf640491d396d7a05bcdc8662436b393e30f3f75427b428361934d560ae86f2` |
| 177→178 | 316 | `r100-i177-Xerr`, `r100-i177-Zerr` | `10e3bd3b219618634704cecacafe81daaf5bfd967bf0d370d38011bde6654975` | `8b0fd21b1c83ee7ce13b0f48f2114d8d43df168a72adc7015f810609548a56ef` | `4b2c78035858b60cb2f1e78c9a093f6f3d20c0b878c33bce871cfe03b18a9ac0` | `c8584ab911b915fe905cffab6ef47f2380181133cf9739a00a2b5c6ff3979643` | `f89fb3e91ce6b7c9ffcf6397cd6ad9ab656626e0aad8f3caa34318782d02cc79` | `1646a998a4d8b9ca2f78e8f40723be54af702dbc748da08081b4df288de9629b` | `93e9432f6e89f8f535844066d3d7af4c8b263b2e8c0aea32179853c7f3d92d8a` |
| 178→179 | 318 | `r100-i178-Xerr`, `r100-i178-Zerr` | `2e1d8cc563e1a97fced13df395429ccc1b94af6e222025f6bee5193de9d3797a` | `51ff749069cef3199c18dba13ca9f804a4f01b9f02cefc575826dbe063d10bb0` | `3b9e1f0aef65ef16cae91eaa2503dcd497a9db22ff425965266cbf0ecced93ae` | `9d0d1bcba0639c661a9b91d98a095ddfebba77cf5e75901aa4da3945ab78d9f7` | `6ce9694264656a00c1f88b54b28b469a273ca7a0c658f949f7d51aa2fae837a8` | `eff470fd47d3143ff6ded43f791745b6b94824317a6883d0c7b37c36ef590e6e` | `aa6d76cd3a8acc66121f63d566d56be22af0bc1d968dcc3d52de59c93398d6f1` |
| 179→180 | 320 | `r100-i179-Xerr`, `r100-i179-Zerr` | `38f0d11bc0cc8ce391b2321e8ff959b31753bcbb439edfda22a003f17456acaf` | `abf177bea1690e1cbd5cd54dacc6132f3b7c254fe9cc2807f21c051a980b5c3a` | `d548c4f6d08d07fd239ff6fd2c2984859fc23b1640ef5caf17dcf2fdd7124f9f` | `e52e8e059fea280fdb2f02e661cad6712ae594686a159f3f0840eeb09d5fba30` | `c9f59fd026c9b372d81b6ff7a82e172f2a46d42d6fc1de8e79427d63cba17919` | `09b1993db8a4b77e115424a90ac28f9ae18b64f98de7ad2ba66a735014f75f0c` | `7ee49db22769d41a279143840e9e6b6bebf217ce79fb5a1359b5c1066035c8eb` |
| 180→181 | 322 | `r100-i180-Xerr`, `r100-i180-Zerr` | `04f9c656d03bf5a671d70149b83f9d82314156207b1e756ad229766810976dc3` | `9bba3918c4b07b214ac3c34bc3150da303042289c6b8d2e2e3c7f9f017c67ddd` | `42d0abf6fe72e92c96daf13d1765cb56fd7c9612baf82719b3f026cf6211c5cb` | `31c397bb1c3233c9b8e7e892c5dde3ebd3b389556b97953288b0c279d0c68dc7` | `014c05cd6cade4fbdced2078b827575f8f4d87cfe6aa51a653dde81716f70ed5` | `338e5ea0bf118fe73c128e30504a01c00022304f6188283d8e9bcbbb53fcbd9f` | `5e60bba1a5b0e4b1f243cd08d69e221dc3e819b58ae9023c6e213a8e72315a87` |
| 181→182 | 324 | `r100-i181-Xerr`, `r100-i181-Zerr` | `91a01ad658980814c3c250a251e879727f0c2aa3222f222e0ac5a15814316d62` | `9720b098c5608ccb48ac43bb45b629848e798c2e8029f50dc8005ba39746332f` | `e80261c0b552916155b2dd59c2cae3b91f18b8141de44eb5205c72c00c3dccfe` | `ab7f43da858394296f4af5a22b0ff70979ef3d0782356cc9c5851a23f84c0c87` | `ccbccab56ba829a93a149723ec2dd63d3650e4fd51435378f437848cc08cacc6` | `9c2c70bce6e82c4ea4f007345f8b2cf23af32482d2a06fa570d08e4fc446d059` | `b22e787a9b723832ea5eba1ed63e14840ccd34ce3b96ec107e865125bb957763` |
| 182→183 | 326 | `r100-i182-Xerr`, `r100-i182-Zerr` | `be7c8f7ecae6fa913fb94fc6d0e2875e1803f1ed38c0a9192add31904e370cb3` | `2c7600de5ce6e561402ab8b130da43b07526efc49451f59fe6261992dda25894` | `081b18d1c37abddc0ab147c274812aa7fcf03c62bddb58a62582968841c04b70` | `4d60f8c878aa2ce50954b9cc9669a6f2f23b3e1dedb00d360d73365f64205fd7` | `0704953638a975f48b40b70ed4e6ffd21f7e3e00960b08ddca9f4b81b7a86d8e` | `a65a51d70feafd3ff77993f4fe7c424933b646dfdf328e0101a77f422e197555` | `9863b94760f580e99aee865d42ead4a3651b2bb1f6cfe364464ad7bfcc792b02` |
| 183→184 | 328 | `r100-i183-Xerr`, `r100-i183-Zerr` | `7296aa70690e01852519b78826b173af35998cec0e9c124c46ea30101dd0777d` | `3b128ef192074a3bc0c163502e97eff99ab9d15c546381e98e1e178471552d7b` | `5eb1607bebea7bfc44b693a4a3a9ae19f2ab5ae498407290863b34d6eb9b66b0` | `d601f297e8b2a1b7d6179d19452da8b0abca2e4f16d7404b6395a8254e949268` | `2b0030fd15b0ef8154e2dbc37508e03481f11d8c876c4fe59e6541cb3bfacd62` | `3a6e5d05e867b7d6136eddb7c35249396d417943f965b093c056a8a7b6fe4181` | `8d23958515e4636e97283cf6745ca99cf6baf68c76be74b395de8f0ec746be83` |

This proves the exact lineage `304,306,...,328`; it does not make any candidate-exact selector
schedule-global.

### Iteration 184 freshness

Iteration 184 is genuinely fresh, checked, unstarted, and unsolved:

* selector count 328 and selector state
  `7296aa70690e01852519b78826b173af35998cec0e9c124c46ea30101dd0777d`;
* state file `3b128ef192074a3bc0c163502e97eff99ab9d15c546381e98e1e178471552d7b`;
* source file `5eb1607bebea7bfc44b693a4a3a9ae19f2ab5ae498407290863b34d6eb9b66b0`;
* semantic source `d601f297e8b2a1b7d6179d19452da8b0abca2e4f16d7404b6395a8254e949268`;
* CNF `2b0030fd15b0ef8154e2dbc37508e03481f11d8c876c4fe59e6541cb3bfacd62`;
* 19,210 assertions, 415,793 variables, and 1,416,404 clauses; and
* state fields `next_iteration=184`, `started=false`, `stop=null`, status PASS, with 184 absent from
  completed iterations.

The only iteration-184 objects are the state, formula directory, and two compile/encoding-check
process records with their logs. There is no `iterations/iter184`, solver assignment, proof, model,
solver disposition, or `iter184_to185` transition.

## Exact same-sector order-six theorem

### Bound basis and row reconstruction

The synthesis theorem is not about the iteration-184 basis. It is bound to the post-iteration-136
state and schedule:

| Bound object | SHA-256 / value |
|---|---|
| iteration-137 state | `ba670045a69722f9625d04d3f07d62e207db38f15e9323f8c32d89194bb585cd` |
| selector state / count | `47792a8f8e757482604723abb0e08916f49b252f4ba07deae03cf4295159d0b6` / 234 |
| iteration-136 candidate | `9596d1456ea66c086c06b4b7b4aaf4e442da9943644ae9839d113f10d937a640` |
| compressed schedule | `45051af0b08e6647d50c6fb0535894173016fd013279e7a0eaee8b2e69ee2e44` |
| direct verification | `f206cb75b7af6cbf2c5421f58c9ebc0c1c0b51d7e44eb3f1c5713a47987a485e` |
| 360-name universe | `3bd9ab41d8bb293292d3e04215a552c8e01b277c780d3b1a2a863373862f0234` |
| X rows / IDs | `2a04ab2d0ccb6574434954b3ca122836e751782fac94fe9c1d0f30360f77e8ff` / `bffc923fdd2aec62fde20525403eb4ce5b3bd0952d3c9a62c39711bfb8da72c` |
| Z rows / IDs | `26dce46a0779a6d2950cf1f9410704ddd6865bbe9af0e081c11f8d635d13fea1` / `58315549e50c3eb78cee7ed210a9dafcd72d60f48e1377fcfa63e07399b6af5c` |

I regenerated all 234 fixed-schedule rows and required byte-for-byte equality to the explicit
little-endian 19-word row files. There are exactly 125 Xerr rows and 109 Zerr rows. A row carries a
360-bit name mask, canonical and physical supports, two 72-bit syndromes, and two 12-bit logical
actions. No checksum or hash participates in membership decisions.

### Coverage and uniqueness derivation

For row \(j\), set \(v_j=(s^c_j,s^p_j)\in\mathbb F_2^{144}\). Enumerate every triple
\(a<b<c\) and key it by the complete pair

\[
K(a,b,c)=v_a\oplus v_b\oplus v_c.
\]

Every sorted six-set \(i_0<i_1<i_2<i_3<i_4<i_5\) has exactly one canonical split
\(L=(i_0,i_1,i_2)\), \(U=(i_3,i_4,i_5)\), with `max(L)<min(U)`. In characteristic two,

\[
v_{i_0}\oplus\cdots\oplus v_{i_5}=0\quad\Longleftrightarrow\quad K(L)=K(U).
\]

Thus scanning every equal-key group and accepting every pair satisfying the strict separation
condition is complete, sound, and unique. I independently exhaustively compared this MITM map with
literal `C(n,6)` sets for every small universe `n=6,...,12`; the counts were exactly
`1,7,28,84,210,462,924`. This is a proof of the reduction, not a sampled check.

Independent pseudocode was:

```text
T = []
for (a,b,c) in combinations(range(n),3):
    T.append((canonical_syndrome_xor, physical_syndrome_xor, a,b,c, full_effects))
sort T by the complete syndrome key
for each maximal equal-key group G:
    for L,U in G x G with max(L) < min(U):
        emit the unique sorted six-set and reconstruct every full effect
```

### Counts, collisions, multiplicities, and zero result

\[
\binom{125}{6}=4,690,625,500,\qquad
\binom{109}{6}=2,025,023,364,
\]

so the exact combined domain is 6,715,648,864. The X triple count is 317,750 and the Z triple count
is 209,934.

| Sector | triple-key histogram (canonical = physical = combined) | separated equal-key pairs | eligible occurrences / unique results | triple checksum mod \(2^{256}\) |
|---|---|---:|---:|---|
| Xerr | `1:317,750` | 0 | 0 / 0 | `c030453f472dc14de03249734a8ea38d0b9bfbaba48441bcd1383d579b0ff978` |
| Zerr | `1:209,304; 2:315` | 0 | 0 / 0 | `aa95d9754426a758eb47a8ff7e82e8debd69abcdbb6a91556b720d84c7981300` |

Representative Z doubletons are `(0,5,79)` with `(0,95,108)`, and `(0,5,95)` with
`(0,79,108)`. They overlap at index 0 and therefore fail strict separation. I tested every pair in
all 315 doubletons; all are nonseparated. X has no zero triple key. Z has exactly one zero triple,
`[5,79,95]`; it is the all-effect-zero kernel vector also found below, occupies a singleton key
group, and cannot pair with a distinct triple. The canonical-only, physical-only, and combined
separated-pair counts are all zero. Therefore the
24-byte eligible files contain the correct zero count and both hash to
`6fd4de01a7468bd5168151f88e13ac082db3505ce8163d0edd17231c7e65707e`. Eligible occurrence,
unique eligible, conservative-valid occurrence, conservative-valid unique, and maximum
multiplicity are all exactly zero. Nothing was sampled or probabilistically deduplicated.

### Integer, memory, and runtime checks

The domain counts and all relevant binomials fit unsigned 64-bit integers; checksum accumulation is
explicitly modulo \(2^{256}\). Complete keys are four 64-bit limbs with unused high bits checked
zero; membership uses full key equality. The C++ triple row is 152 bytes. Nominal triple-table
storage is 48,298,000 bytes for X and 31,909,968 for Z. Retained macOS peak RSS is respectively
51,347,456 and 34,553,856 bytes, consistent with the nominal arrays plus process overhead. Retained
science runtimes are 0.160842 s and 0.074303 s. My independent Python reconstruction of all rows,
545,126 triples, all groups, collisions, checksums, and empty output streams took 2.759 s in the
review process. The fast proposer runtime is credible and no impossible streaming claim is needed:
the MITM closes billions of six-sets through the proved unique split.

The theorem covers only six distinct indices within one of these two exact bases on this exact
schedule. It does not cover mixed sectors, outside-basis mechanisms, another schedule, or a later
frontier. Repeated GF(2) indices cancel algebraically, but that fact does not convert this specific
six-distinct statement into an all-orders theorem; the separate span query supplies the latter only
inside the same fixed spans.

## High-risk fixed-basis full-span audit

### Exact quantified semantics

I regenerated both span CNFs from the independently reconstructed row files, without calling the
package builder. For sector rows \(r_j\) and unrestricted coefficients
\(c_j\in\mathbb F_2\), every output is a full linear image:

\[
n_b=\bigoplus_j c_j n_{j,b},\quad
s^c_b=\bigoplus_j c_j s^c_{j,b},\quad
s^p_b=\bigoplus_j c_j s^p_{j,b},
\]

with analogous 12-bit \(\ell^c,\ell^p\). The complete coefficient spaces are \(2^{125}\) and
\(2^{109}\); there is no cardinality bound on the coefficients. The CNF asserts exactly:

1. all 360 name bits equal their coefficient XORs;
2. all 72 canonical and 72 physical syndrome bits are false;
3. all 12 bits of \(\ell^c\oplus\ell^p\) are false;
4. `OR(n[0..359])`, excluding the empty named result;
5. `OR(ell_c[0..11])`, requiring a nontrivial logical action;
6. named weight at most 10; and
7. for each installed same-sector full named mask \(m\), the 360-literal clause
   \(\bigvee_b(n_b\ne m_b)\).

The last clause has literal `n_b` when `m_b=0` and `not n_b` when `m_b=1`; I explicitly checked
this polarity and all 125 X / 109 Z masks. There are no schedule-choice or source-validity
variables. That is not a missing predicate: every row effect was freshly evaluated in the fixed
iteration-136 schedule over the complete allowed 360-name universe, and every coefficient vector
therefore denotes exactly one combination in that fixed row span. The absence claim is consequently
for every combination in that exact span and for no vector outside it. It is not a universal
frozen-family schedule theorem.

The at-most-10 recurrence is an equivalence, not a one-way counter:

\[
A_{i,1}=A_{i-1,1}\lor n_i,
\qquad
A_{i,j}=A_{i-1,j}\lor(A_{i-1,j-1}\land n_i),
\]

with exact boundaries and final `not A[360,11]`. I exhausted all truth assignments for the binary
XOR/AND/OR gates (8 joint gate cases) and all prefix-cardinality cases through `n=12`, totaling
544,766 recurrence evaluations. This catches the principal wrong-inequality and one-way-encoding
risks.

### Byte-exact formulas, ranks, and solver checks

| Sector | rows / coefficient space | name rank / nullity | combined-syndrome rank | variables / clauses | CNF SHA-256 | result |
|---|---:|---:|---:|---:|---|---|
| Xerr | 125 / \(2^{125}\) | 125 / 0 | 65 | 12,949 / 43,827 | `c689883518b2abbf28aadbc9f13025d032f6f1e792e469b7a584517cfc4f48e5` | UNSAT |
| Zerr | 109 / \(2^{109}\) | 108 / 1 | 65 | 12,089 / 40,443 | `ce2113182676ab6063006a60d0fb4a6fc60447056ea2449b351eb6e9024c01b9` | UNSAT |

Every variable was allocated in the deterministic expected order and every clause/family was
regenerated. The emitted DIMACS bytes, counts, and hashes are exact. A separate direct-semantics
Z3 5.1.0 model, using Boolean XOR expressions and integer name-weight rather than CNF auxiliaries,
returned UNSAT for both complete coefficient domains.

Z has the expected one-dimensional name kernel. Coefficients `[5,79,95]` produce zero names, zero
canonical support, zero physical support, both syndromes zero, and both logical actions zero. This
is a coefficient/result collision, not a theorem failure: every output gate depends on the result,
and the nonempty/logical roots exclude the zero result. X has no name kernel.

Controls establish nonvacuity and correct quotient behavior:

* Remove novelty only: X is SAT with coefficient `[124]`, named weight 10, logical `0x37`, and an
  installed full mask; Z is SAT with coefficients `[5,79,95,108]`, named weight 10, logical `0xc59`,
  and an installed full mask.
* Remove novelty, name-nonzero, and logical-nonzero and force every coefficient false: both sectors
  are SAT at the exact zero result. This specifically tests the nonempty roots.
* Raising the name bound to 11 remained UNSAT in both sectors. I treat this only as a diagnostic
  mutation, not as added canonical scope.

Thus accepted UNSAT means precisely:

> For every coefficient vector in the exact fixed sector basis, if its full named result has weight
> 1..10, its canonical and physical syndromes are zero, and its canonical/physical logical actions
> agree and are nonzero, then its full named mask is one of the installed same-sector masks.

It does not mean that no valid combinations exist; the no-novelty controls exhibit them. It does
not cover an arbitrary 360-bit direct vector outside the row span, another basis, another schedule,
or the whole frozen Gross schedule family.

### DRAT, LRAT, and negative controls

I decompressed fresh copies of the formulas/proofs into reviewer scratch and invoked the packaged
checkers directly, strictly serially. Six valid objects were accepted: X and Z DRAT/LRAT plus a
fresh PHP(6,5) fixture DRAT/LRAT. Twelve negative controls were rejected: truncated and corrupt
DRAT/LRAT for X, Z, and the fixture. All 18 processes were reaped, none detached, and every captured
stderr was empty.

| Sector | DRAT SHA-256 / bytes | LRAT SHA-256 / bytes | valid outputs | negative outputs |
|---|---|---|---|---|
| Xerr | `b14ece4b00c0c0ade83e8477fc2b6b97a230cb8622c928b4d5bd3d616d34ebb8` / 6,086,647 | `88cde84e0153be278136e17c5f2c733b134b20ec8b8142318da657566d4eb2b1` / 10,226,266 | DRAT `s VERIFIED`; LRAT `c VERIFIED` | truncated/corrupt DRAT and LRAT each return 1 / NOT VERIFIED |
| Zerr | `718512fdfc7e3c4695e0ac866f27fbfba95dad848d6c5131a1e013a2870bb58e` / 4,495,132 | `14502bc70ab7f0ced69f90ec8504ef555c3cb8a18b1f0e548576b71c7b7dfd7c` / 11,714,693 | DRAT `s VERIFIED`; LRAT `c VERIFIED` | truncated/corrupt DRAT and LRAT each return 1 / NOT VERIFIED |

The fixture has 30 variables and 141 clauses and shows the tools accept a separate known UNSAT
instance while rejecting its corruptions. There is no proof/formula hash mismatch, truncation
acceptance, reversed literal polarity, omitted nonempty root, or stale-basis substitution.

## Mixed-sector component reduction

The package theorem is correct at its declared scope. Let a fixed-schedule CSS mechanism have
components \((N_X,N_Z)\) and total named weight \(|N_X\cup N_Z|\le10\). CSS linearity gives separate
syndromes \((s_X,s_Z)\) and an ordered logical pair \((\ell_X,\ell_Z)\). If the mixed mechanism is
undetected, then `s_X=s_Z=0`. If the logical pair is nonzero, at least one component, say S, has
`ell_S != 0`. Finally,

\[
|N_S|\le |N_X\cup N_Z|\le10.
\]

So a low-weight undetected nontrivial mixed direct mechanism always contains a same-sector
low-weight undetected nontrivial direct mechanism on the same fixed schedule. X/Z overlap can reduce
the union relative to the sum, but it cannot make the union smaller than either component. There is
therefore no lower effective mechanism created solely by cross-sector composition under this named
weight convention.

What it covers: the common 360-name universe, CSS decomposition, fixed schedule, and complete direct
weight-10 component queries. If both component direct queries are checked UNSAT, mixed direct
absence follows for that schedule. What it does not cover: another schedule; an outside-name or
non-CSS/correlated fault model; another weight convention; weight above 10; or the assertion that
the fixed X/Z selector bases span all direct mechanisms. The Round100 direct queries are SAT, so the
theorem's absence antecedent is false for all twelve new candidates. A fixed-basis span theorem
cannot silently become universal frozen-family closure through this reduction.

## Process, proof-stream, and failure audit

### Retained process census

I parsed all retained process JSON independently and cross-checked PIDs, parents, commands, return
codes, timestamps, reaping, timeout/TERM/KILL fields, and the final process scan.

* 211 retained PID records are present. FIX-2 correctly records 210 before the cleanup wrapper and
  211 after it.
* The immutable science census is exactly 204 records. It excludes the later
  `independent_campaign_audit` and `round100_*` packaging/replay records.
* Science return codes are `0:165`, `1:1`, `10:36`, `20:2`, matching success, the disclosed failed
  validator, and CaDiCaL SAT/UNSAT conventions.
* All 38 retained CaDiCaL solver intervals are strictly nonoverlapping. No timeout, detached child,
  or survivor is hidden by a second concurrent interval.
* The 36 SAT proof streams (12 outer plus 24 direct) were correctly classified as non-certificates,
  summarized by hashes/bytes/LF/first/last/empty-clause counts, and deleted. They total
  6,035,040,945 bytes and 65,763,297 LF. All 36 paths are absent. The complete assignments and
  independent clause/physical replays remain, so no absence claim depends on a deleted SAT stream.
* The preseal full replay is PASS with 126 direct plus 18 nested children. FIX-2 reports zero
  survivors, zero detached processes, original Round100 scratch absent, and no replay temp left.

### All twelve proposer failure records

| ID | rejected/failed attempt | correction and audited effect |
|---|---|---|
| F001 | guessed `formulas/iter172/source.json` rather than `.json.gz` | used the manifest-bound gzip path; no solver/model ran |
| F002 | Z3 `Xor` called positionally with more than three arguments | binary XOR fold; the exception occurred before `solver.check()`, so the failed run yielded no theorem |
| F003 | inspection helper requested one line past source length | bounded the read; inspection only |
| F004 | generated audit draft contained a placeholder source hash | rejected before execution and replaced with commissioned hash |
| F005 | first compressor draft had malformed f-string | `py_compile` failed before any compression; corrected build compressed 222 streams with round trips |
| F006 | first preseal replay resolved the dispatcher venv symlink to base/system Python | 28 children passed; child 29 physical replay lacked z3 and returned 1; fixed by preserving `absolute()` interpreter path; incomplete run supports no package verdict |
| F007 | next replay hard-coded the immutable 204-process science count after later packaging logs existed | 122 direct children and 12 nested children passed; direct child 123 failed the scope count; science and packaging records were separated; incomplete run supports no package verdict |
| F008 | mixed-sector toy control used unavailable `int.bit_count` under system Python | changed to `bin(value).count("1")`; all 256 controls reran PASS |
| F009 | `validate_span.py --help` under system Python lacked z3 | actual validation used the bound z3 environment; help probe produced no result |
| F010 | invoked `order6_mitm` without arguments for usage | expected usage exit; theorem runs used complete arguments |
| F011 | patch request attempted delete-and-add on one path | host rejected before mutation; corrected draft later compiled |
| F012 | first sealed-replay launch text included `rm -rf` | host policy rejected before an OS process; fresh unique directory/no deletion then produced the retained 145-child PASS |

The F006 and F007 failure directories preserve the failed replay records byte-for-byte. They are
distinct from the three Round98 post-science model-capacity interruptions, which occurred in the
prior package workflow and are not Round100 failures. This distinction is correctly retained.

### Reviewer-side corrections during reconstruction

For completeness, my own discarded audit assumptions are recorded here; none changed package
science. An initial inventory helper read a nonexistent `lf` key instead of the inventory's `lines`
key and reported false count mismatches; the corrected pass recomputed physical LF counts directly.
The first outer checker assumed detector rows were support lists rather than decimal bitmask strings,
assumed a legacy `source_iteration` field existed in every state row, and required a SAT status line
in the independently formatted assignment; those format assumptions were corrected before the
final full pass. A first table-generation pass mistook the package's “assignment values identical”
flag for gzip/content byte identity; the final table reports separate hashes and parsed-value
identity. In the order-six checker I first compared the combined-candidate checksum to a pair-count
checksum field and looked for `wall_seconds` rather than `seconds`; both were corrected to the
documented definitions. The first zero-control span query allowed an arbitrary model; the final
control additionally forced every coefficient false. These corrections are why the review reports
final exact checks rather than relying on one script invocation.

## Environment, repository gates, and evidence closure

The sealed environment reports macOS 26.6.2 arm64, system Python 3.9.6, Z3 5.1.0, packaged CaDiCaL
1.9.5, `drat-trim`, and `lrat-check`. Key executable identities independently hashed as:

| Tool | SHA-256 | bytes |
|---|---|---:|
| CaDiCaL 1.9.5 | `fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9` | 967,144 |
| `drat-trim` | `f58f63b0f76945d4c4c9ff6e87afaf870f579e67c0f7cca589492df8fc7ebd47` | 70,120 |
| `lrat-check` | `bd7eb8052623525814a0a37502b47f05375d9d9dfaf96ddc2fcd858958517cea` | 36,552 |
| order-six MITM | `e09855a34bfd35c8bcefeac1156b178a7151ae740d02a2969e2a6802e75c63d9` | 95,608 |

I reran the current repository checks strictly serially. Results were: proof DAG `circdist` PASS;
proof DAG against the bound previous state PASS; proof DAG `all` PASS; migration PASS; 14 release
contract tests PASS; 24 DAG contract tests PASS; Lean DAG selftest PASS; duplicate YAML scan PASS;
and `git diff --check` PASS. Test-suite progress is normally printed on stderr; both suites returned
zero and ended `OK`.

Before this review is linked, evidence closure must fail because the new sealed directory is
intentionally unlinked. The current final-package scan returned 1 with 1,695 unique diagnostics,
all and only under `circdist/artifacts/circdist_gross_proof_outer_round100_20260831/`; stderr was
empty. The retained preseal interpretation has 1,658 because it preceded the final seal metadata.
Neither count is treated as a repository defect. The replacement YAML links the package directory
and this review, and the disposable-overlay closure check described below passes.

Representative reproduction commands, with no canonical mutation, were:

```sh
cd <repo>
/usr/bin/python3 tools/proof_dag_check.py --problem circdist
/usr/bin/python3 tools/proof_dag_check.py --problem circdist \
  --previous-state circdist/artifacts/circdist_gross_proof_outer_round100_20260831/bindings/initial_proof_dag
/usr/bin/python3 tools/proof_dag_check.py --problem all
/usr/bin/python3 tools/check_circdist_migration.py
/usr/bin/python3 tools/test_release_contracts.py
/usr/bin/python3 tools/test_dag_contracts.py
/usr/bin/python3 tools/lean_dag_check.py --selftest
git diff --check
/usr/bin/python3 tools/evidence_closure_check.py --problem circdist  # expected 1 before linking

PYTHON=/private/tmp/circdist-r72-dispatcher-venv/bin/python \
  circdist/artifacts/circdist_gross_proof_outer_round100_20260831/replay.sh \
  /private/tmp/FRESH_REVIEW_DIRECTORY/record.json
```

The independent algorithms used ordinary integer/GF(2) operations, streamed gzip/DIMACS parsing,
explicit truth-table controls, and packaged checker invocations. They did not call the proposer
campaign driver or accept its summary as a substitute for reconstruction.

## Fresh sealed replay

I created a new unique `/private/tmp/circdist-r101-sealed-replay.*` directory and ran `replay.sh`
with the exact bound interpreter `/private/tmp/circdist-r72-dispatcher-venv/bin/python`. The replay
completed PASS in 391.241810 s.

* direct children: 127;
* nested children: 18, in three six-child groups (`span_proof_controls_Xerr`,
  `span_proof_controls_Zerr`, `proof_fixture_controls`);
* total known children: 145;
* strict serial: true;
* all children reaped: true;
* detached processes: 0;
* every direct child captured stderr: empty;
* wrapper stderr: 0 bytes, SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
* all 127 direct PIDs unique and parented to the replay PID; and
* post-completion `ps` rows for all recorded child/replay PIDs: zero.

The record is SHA-256
`4f3ef4614e72e4730138cf87389eea202e67b634053c746646aeb9273e714757`, 264,113 bytes / 3,659 LF.
Replay stdout is SHA-256
`821458cbee6cfc47527e7c23b81e5287e05574bff0ad96a40e4887514c15ded6`, 16,388 bytes / 153 LF,
and ends exactly `ROUND100_PACKAGE_REPLAY_PASS 127 18`. I inspected all child records rather than
accepting only that terminal line. Reviewer replay and proof-materialization scratch were removed
before finalization.

## Claim accounting and remaining mathematical gap

The 12 new outer SAT schedules and their 24 direct SAT mechanisms are positive counterexample-style
continuation evidence. Each appended EFSSC excludes only the exact source candidate domain for which
its schedule predicate is sound. None is a schedule-global absence fact.

The order-six theorem is an exact finite no-go on six distinct rows in each fixed sector basis. The
span theorem is stronger in order but narrower in ambient space: it closes every GF(2) combination
in those fixed bases only after existing full named masks are permitted/quotiented. The mixed-sector
theorem reduces a fixed-schedule complete-direct mixed witness to a component; it cannot fill the
outside-span or other-schedule gaps. Taken together, these results still do not establish the full
frozen root claim.

The remaining mathematical gap is unchanged: either produce an explicit legal frozen Gross
schedule with independently certified circuit distance 12, or prove every legal frozen Gross
schedule has circuit distance at most 11. Within the current CEGAR route, the next authorized step
may solve the exact checked iteration-184 outer formula, then must rebuild both complete unrestricted
direct sectors. Repair may begin only after both direct sectors are independently proof-checked
UNSAT. A universal conclusion would additionally need coverage beyond the fixed post-iteration-136
selector spans and beyond the finite candidates visited so far.

## Canonical-installation license and replacement validation

Because the verdict licenses canonical installation at proposer level, the fenced block below is
one complete replacement for `circdist/proof-dag/nodes/CIRCDIST.gross.yaml`. It preserves the prior
claim, status, routes, route assessments, evidence, and every prior event. It adds only reviewed
Round100 evidence and scope, the corrected iteration-184 frontier/failure provenance, and one
append-only Round101 review event. It contains no ellipsis or patch notation.

The extracted YAML was compared byte-for-byte with the intended replacement; loaded with the
duplicate-key loader; checked for exact preservation of every prior route and event; validated on a
disposable proof-DAG overlay; checked by the duplicate-YAML scanner; and run through project-local
evidence closure with the package and completed review linked. The canonical live file itself was
not edited.

<!-- replacement identity is reported in the reviewer's final handoff; placing a self-hash inside
this file would be circular because the replacement is embedded in this review. -->

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
    CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}. Round 95''s fresh independent exact review clears the sealed Round-94 package for proposer-level continuation only: iterations 136--147 add 24 exact EFSSC selectors after twelve legal outer SAT schedules and twenty-four unrestricted direct-sector SAT/physical replays; the complete same-sector order-3 GF(2) search retains zero terms; and the fresh frontier is unstarted iteration 148 with 256 selectors and checked-unsolved CNF sha256:397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4. No Gross UNSAT, direct absence, repair, exhaustion, D* narrowing, route promotion, or root promotion is licensed; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}. Round 97''s fresh independent exact review clears the sealed Round-96 package for proposer-level continuation only: iterations 148--159 add 24 exact EFSSC selectors after twelve legal outer SAT schedules and twenty-four unrestricted direct-sector SAT/physical replays; the complete same-sector order-4 GF(2) search covers 15,254,626 distinct quadruples and retains zero novel terms; and the fresh frontier is unstarted iteration 160 with 280 selectors and checked-unsolved CNF sha256:aa18d2857ed5a7aefacd33bf4fbd42fded914393e123a87f00e84e4920e39d59. No Gross UNSAT, direct absence, repair, exhaustion, D* narrowing, route promotion, or root promotion is licensed; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}. Round 99''s fresh independent exact review clears the sealed Round-98 package for proposer-level continuation only: iterations 160--171 add 24 exact EFSSC selectors after twelve legal outer SAT schedules and twenty-four unrestricted direct-sector SAT/physical replays; the complete same-sector order-5 GF(2) search covers C(125,5)+C(109,5)=351,359,546 distinct quintuples, reconstructs 40,153 unique named-weight-1..10 results, finds zero canonical-syndrome-zero results in either sector, and retains zero selectors; and the fresh frontier is unstarted iteration 172 with 304 selectors and checked-unsolved CNF sha256:f86b8db36af1df3877ca1d9dbafb171b6173ddc8b6c2f045a808dd6c71f98342. No Gross UNSAT, direct absence, repair, exhaustion, D* narrowing, route promotion, or root promotion is licensed; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}. The fresh Round-101 independent exact review clears the sealed Round-100 package for proposer-level continuation only: iterations 172--183 add 24 exact EFSSC selectors after twelve legal outer SAT schedules and twenty-four unrestricted direct-sector SAT/physical replays; the complete same-sector order-6 search covers C(125,6)+C(109,6)=6,715,648,864 six-sets and retains zero selectors; and exact all-orders fixed-basis span queries are UNSAT in both sectors after quotienting installed named masks. The valid mixed-sector component reduction remains fixed-schedule direct-domain reasoning, not global closure. The review corrects one non-load-bearing sentence: the Z triple-key histogram has 209,304 singleton groups and 315 doubletons, all nonseparated, rather than all singleton groups. The fresh frontier is unstarted iteration 184 with 328 selectors and checked-unsolved CNF sha256:2b0030fd15b0ef8154e2dbc37508e03481f11d8c876c4fe59e6541cb3bfacd62. No Gross UNSAT, direct absence, repair, exhaustion, D* narrowing, route promotion, or root promotion is licensed; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
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
      note: 'Sealed Round-94 proof-producing finite-outer continuation package independently cleared at proposer level in
        Round 95; final root seal sha256:1e0a4af8591aa63ccccd1b2516c630eccb11a73fb9dea2e0ff1e0d32ed82ac1c and payload seal sha256:c39ef3552e461dd7513812b8296901e72369dfacbf6e71ae758b5bb58ed94c54.
        Iterations 136--147 are twelve complete legal outer SAT schedules; all twenty-four unrestricted direct-360 sectors
        are SAT and physically replayed, with iteration-138 Xerr at weight 9 and the other twenty-three mechanisms at weight
        10. Twenty-four exact EFSSC selectors were appended atomically. The complete same-sector order-3 GF(2) search covers
        C(125,3)+C(109,3)=527,684 triples, finds 4,232 novel unique outputs of named-location weight at most 10, rejects every
        one by nonzero frozen-schedule syndrome, and retains zero terms. The exact fresh/unstarted frontier is iteration 148
        with 14,484 inherited order blocks, 256 selectors, selector-state sha256:9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f,
        and independently checked but unsolved 409,157-variable/1,385,059-clause CNF sha256:397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4.
        The superseded first seals are non-final. Positive SAT mechanisms, SAT traces, and the finite order-3 no-go prove no
        Gross absence, repair, exhaustion, D* narrowing, route promotion, or root promotion.'
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
      note: 'Sealed Round-96 proof-producing finite-outer and exact same-sector order-4 continuation package independently
        cleared at proposer level in Round 97; final root seal sha256:d992087072835e2651834aceb3012f8afd20442b2886673b45254e95e861a361
        and payload seal sha256:9cf210a8dd392a57700a61b640ced0deda5d212173f88293083759f67cb77121. Iterations 148--159
        are twelve complete legal outer SAT schedules; all twenty-four unrestricted direct-360 sectors are SAT and physically
        replayed, with iteration-148 and iteration-152 Xerr/Zerr named weights 10/9 and every other sector weight 10. Twenty-four
        exact EFSSC selectors were appended atomically. The exact same-sector order-4 GF(2) search covers C(125,4)+C(109,4)=15,254,626
        distinct quadruples. Its sole conservative syndrome-zero result is Zerr logical action 100110100011 and is already
        inherited, so zero novel selectors are retained. The exact fresh/unstarted frontier is iteration 160 with 14,484 inherited
        order blocks, 280 selectors, selector-state sha256:ad3cf364dd9224c14ffb55046ba3dc8eb80035b1eaf997f1d7a5691297ad62a3,
        and independently checked but unsolved 411,526-variable/1,396,722-clause CNF sha256:aa18d2857ed5a7aefacd33bf4fbd42fded914393e123a87f00e84e4920e39d59.
        Positive SAT mechanisms, SAT streams, and the finite order-4 no-go prove no Gross absence, repair, exhaustion, D* narrowing,
        route promotion, or root promotion.'
    - path: circdist/reviews/circdist_gross_proof_outer_round96_exact_review_round97_20260831.md
      kind: review
      note: Fresh independent Round-97 exact review. A non-importing standard-library checker reconstructs all thirteen outer
        semantic sources/CNFs/maps/traces, satisfies every clause of the twelve complete outer assignments, decodes twelve
        distinct legal frozen schedules, rebuilds all twenty-four unrestricted direct-360 formulas and physical mechanisms,
        proves the exact EFSSC semantics and atomic 256--258--...--280 lineage, and exhausts the 15,254,626-quadruple same-sector
        order-4 domain with exact multiplicity and conservative schedule-validity checks. It also verifies the fresh unsolved
        iteration-160 frontier, manifests, environment, proof fixtures, all disclosed incident classes, exact final 1,588-path
        prelink closure, protected state, process closure, and the complete replacement on a disposable overlay. Verdict
        CLEAR-PROPOSER-LEVEL-CONTINUATION; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.
    - path: circdist/artifacts/circdist_gross_proof_outer_round98_20260831
      kind: run
      note: 'Sealed Round-98 proof-producing finite-outer and exact same-sector order-5 continuation package independently
        cleared at proposer level in Round 99; final root seal sha256:f64feb1b424b4aff938a1b5a0c1f9a799179e41f4ec99295c5c67376fad9142f
        and payload seal sha256:2df276eb26dc569f830d0c95ac76aa5ed322bc9fcb525637a96196d66394e6ec. Iterations 160--171
        are twelve complete legal outer SAT schedules; all twenty-four unrestricted direct-360 sectors are SAT and physically
        replayed, with iteration-161 Xerr at named weight 9 and every other sector at named weight 10. Twenty-four exact EFSSC
        selectors were appended atomically. The exact same-sector order-5 GF(2) search covers C(125,5)+C(109,5)=351,359,546
        distinct quintuples, reconstructs 38,382 Xerr plus 1,771 Zerr unique named-weight-1..10 results, finds zero canonical-syndrome-zero
        results in both sectors, and retains zero selectors. The exact fresh/unstarted frontier is iteration 172 with 14,484 inherited
        order blocks, 304 selectors, selector-state sha256:a5c64ae41f474844ecd3ac41829331f54d419a81573e4f0e11528db0b49e25d1,
        and independently checked but unsolved 413,646-variable/1,406,245-clause CNF sha256:f86b8db36af1df3877ca1d9dbafb171b6173ddc8b6c2f045a808dd6c71f98342.
        Positive SAT mechanisms, SAT streams, and the finite order-5 no-go prove no Gross absence, repair, exhaustion, D* narrowing,
        route promotion, or root promotion.'
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
        theorem covers C(125,6)+C(109,6)=6,715,648,864 six-distinct sets and retains zero selectors. The exact all-orders span
        CNFs are UNSAT only over the fixed post-iteration-136 Xerr/Zerr bases and fixed schedule after excluding installed full
        named masks; they say nothing about arbitrary mechanisms outside those spans. The review corrects SYNTHESIS_PROOF.md:
        Z has 315 size-two triple-key groups, all nonseparated, not an all-singleton histogram. Failures F001--F012 are retained;
        F006 is the first incomplete replay under base Python without z3 and F007 is the incomplete replay whose hard-coded
        204-record census included later packaging records. Neither supports a package verdict, and neither is a Round-98 capacity
        interruption. The exact fresh/unstarted frontier is iteration 184 with 328 selectors and checked-unsolved CNF sha256:2b0030fd15b0ef8154e2dbc37508e03481f11d8c876c4fe59e6541cb3bfacd62.
        Positive SAT mechanisms and the scoped synthesis no-go results prove no Gross absence, repair, exhaustion, D* narrowing,
        route promotion, or root promotion.'
    - path: circdist/reviews/circdist_gross_proof_outer_round100_exact_review_round101_20260831.md
      kind: review
      note: 'Fresh independent Round-101 exact review. It binds the package to the exact dispatched scheduler and prior canonical
        state; reconstructs every iteration-172--184 source/map/trace/CNF tuple, every clause of the twelve outer and twenty-four
        direct SAT assignments, every frozen physical replay, and the atomic 304--328 selector lineage; proves the exact order-6
        MITM coverage and collision logic; regenerates both full-span CNFs and checks Z3, DRAT, LRAT, valid controls, and every
        corrupt/truncated negative control; proves the mixed-sector reduction at its actual fixed direct scope; checks manifests,
        all twelve failures, the 211/204 process censuses, 38 nonoverlapping solver intervals, proof-stream deletion, FIX-2,
        repository gates, and a fresh 127+18-child sealed replay. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION with the Z triple-key
        documentation correction; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
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
    task: 'Continue only from the independently reviewed sealed fresh/unstarted iteration 184 state. The inherited sound order-block
      library remains exactly 14,484 predicates (1,440 unary, 20 round-62, 12,820 generalized, and 204 dynamic), and the exact
      fixed-selector frontier is 328 EFSSCs: the reviewed 304-selector Round-99 frontier plus the 24 exact candidate-domain
      selectors from iterations 172--183. Bind selector-state sha256:7296aa70690e01852519b78826b173af35998cec0e9c124c46ea30101dd0777d,
      state-file sha256:3b128ef192074a3bc0c163502e97eff99ab9d15c546381e98e1e178471552d7b, iteration-184 semantic-source
      sha256:d601f297e8b2a1b7d6179d19452da8b0abca2e4f16d7404b6395a8254e949268, and source-file sha256:5eb1607bebea7bfc44b693a4a3a9ae19f2ab5ae498407290863b34d6eb9b66b0
      before use. Its deterministic 10-bit compressed finite-outer formula has 19,210 source assertions, 415,793 variables,
      1,416,404 clauses and CNF sha256:2b0030fd15b0ef8154e2dbc37508e03481f11d8c876c4fe59e6541cb3bfacd62; it was checked but deliberately
      not solved, and no iteration-184 solver/model/DRAT/LRAT disposition is inherited. The complete same-sector order-6 search
      at the post-iteration-136 fixed bases exhaustively covers C(125,6)+C(109,6)=4,690,625,500+2,025,023,364=6,715,648,864
      six-distinct sets via the unique sorted lower-three/upper-three split. X has 317,750 singleton triple-key groups. Z has
      209,304 singleton groups and 315 doubletons, but every doubleton is nonseparated, so neither sector has an eligible equal-key
      split and zero selectors are retained. The stronger span CNFs quantify all 2^125 Xerr and 2^109 Zerr coefficient vectors
      over those exact bases, construct the full 360-bit named result, require named weight 1..10, both frozen-schedule syndromes
      zero, equal nonzero canonical/physical logical action, and inequality to each installed full named mask; both are proof-checked
      UNSAT (X CNF sha256:c689883518b2abbf28aadbc9f13025d032f6f1e792e469b7a584517cfc4f48e5; Z CNF sha256:ce2113182676ab6063006a60d0fb4a6fc60447056ea2449b351eb6e9024c01b9).
      These are fixed-basis, fixed-schedule theorems, not closure over arbitrary named mechanisms, other schedules/frontiers,
      bases, or frozen-family schedules; installed-mask quotienting also means they do not assert absence of all combinations.
      The mixed-sector component theorem says only that a fixed-schedule CSS mixed direct mechanism of total named weight at
      most 10 contains a same-sector undetected nontrivial component within that bound; it does not globalize either synthesis
      theorem, and the Round-100 direct queries are SAT. For a new outer SAT result, retain the complete assignment, replay every
      DIMACS clause and frozen schedule condition, then rebuild and adjudicate both complete unrestricted direct-360 sectors;
      a positive mechanism kills only that concrete candidate domain and proves no absence, and only exact source-schedule-valid
      EFSSC selectors may be added atomically. For an UNSAT result, retain a complete DRAT proof, independently accept it, generate
      LRAT, and independently accept the LRAT with valid/corrupt/truncated controls. Enter repair only after both direct sectors
      have independently checked absence. Preserve frozen S_Gross, strict serialization, MC0, terminal residual semantics, both
      CSS sectors, and every existing exclusion against morphing, Circ-Preserve substitutions, alternate conflict models, exploratory
      pair clauses, retroactive cuts, stale compressor provenance, mixed-sector XOR, support-weight substitution, schedule-globalized
      dynamic predicates, and fixed-basis/full-span globalization. Keep CIRCDIST.gross and gap-via-lift CONJECTURED and D*_Gross
      in {11,12}; this reviewed continuation supplies no Gross UNSAT, absence, exhaustion, distance-12 witness, universal distance-11
      ceiling, route promotion, or root promotion.'
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
      256 exact EFSSC selectors, selector-state sha256:9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f,
      and checked-unsolved CNF sha256:397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4 (409,157 variables;
      1,385,059 clauses; 19,138 source assertions). Iterations 136--147 and all twenty-four unrestricted direct sectors are
      SAT; their physically replayed mechanisms, including iteration-138 Xerr at weight 9, license only twenty-four candidate-domain
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
      280 exact EFSSC selectors, selector-state sha256:ad3cf364dd9224c14ffb55046ba3dc8eb80035b1eaf997f1d7a5691297ad62a3,
      and checked-unsolved CNF sha256:aa18d2857ed5a7aefacd33bf4fbd42fded914393e123a87f00e84e4920e39d59 (411,526 variables;
      1,396,722 clauses; 19,162 source assertions). Iterations 148--159 and all twenty-four unrestricted direct sectors are
      SAT; their physically replayed mechanisms, including iteration-148 and iteration-152 Zerr at weight 9, license only
      twenty-four candidate-domain cuts. The exhaustive 15,254,626-quadruple investigation retains zero novel terms and proves
      a no-go only on its exact declared same-sector order-4 domain. No Gross UNSAT, direct absence, repair, exhaustion, D*
      narrowing, route change, or level change is licensed; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross
      in {11,12}.'
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
      304 exact EFSSC selectors, selector-state sha256:a5c64ae41f474844ecd3ac41829331f54d419a81573e4f0e11528db0b49e25d1,
      and checked-unsolved CNF sha256:f86b8db36af1df3877ca1d9dbafb171b6173ddc8b6c2f045a808dd6c71f98342 (413,646 variables;
      1,406,245 clauses; 19,186 source assertions). Iterations 160--171 and all twenty-four unrestricted direct sectors are
      SAT; their physically replayed mechanisms, including iteration-161 Xerr at weight 9, license only twenty-four candidate-domain
      cuts. The exhaustive 351,359,546-quintuple investigation reconstructs 40,153 unique eligible named-weight-1..10 results,
      finds zero canonical-syndrome-zero results in either sector, retains zero selectors, and proves a no-go only on its exact
      declared same-sector order-5 domain. No Gross UNSAT, direct absence, repair, exhaustion, D* narrowing, route change, or
      level change is licensed; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
    sources:
    - path: circdist/artifacts/circdist_gross_proof_outer_round98_20260831
      kind: run
    - path: circdist/reviews/circdist_gross_proof_outer_round98_exact_review_round99_20260831.md
      kind: review
  gross-proof-outer-round101-review-2026-09-01:
    date: '2026-09-01'
    type: review-completed
    summary: 'Fresh independent Round-101 review clears the sealed Round-100 finite-outer, exact same-sector order-6, and fixed-basis
      full-span package at proposer level and licenses continuation only from fresh/unstarted iteration 184: 14,484 inherited
      order blocks, 328 exact EFSSC selectors, selector-state sha256:7296aa70690e01852519b78826b173af35998cec0e9c124c46ea30101dd0777d,
      and checked-unsolved CNF sha256:2b0030fd15b0ef8154e2dbc37508e03481f11d8c876c4fe59e6541cb3bfacd62 (415,793 variables;
      1,416,404 clauses; 19,210 source assertions). Iterations 172--183 and all twenty-four unrestricted direct sectors are SAT;
      their physically replayed mechanisms license only twenty-four candidate-domain cuts. Exact order-6 coverage retains zero
      selectors. The X/Z all-orders span UNSAT results cover only the exact fixed bases, installed-mask quotient and post-iteration-136
      schedule; the mixed-sector theorem is only a fixed-direct-domain component reduction. A non-load-bearing synthesis sentence
      is corrected: Z has 315 nonseparated doubleton triple-key groups, not an all-singleton histogram. All F001--F012 records,
      211 retained PID records, the immutable 204-record science census, 38 strictly nonoverlapping solver intervals, deletion
      of 36 SAT non-certificate streams, FIX-2, and a fresh strict-serial 127-direct plus 18-nested sealed replay pass review.
      No Gross UNSAT, direct absence, repair, exhaustion, D* narrowing, route change, or level change is licensed; CIRCDIST.gross
      and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
    sources:
    - path: circdist/artifacts/circdist_gross_proof_outer_round100_20260831
      kind: run
    - path: circdist/reviews/circdist_gross_proof_outer_round100_exact_review_round101_20260831.md
      kind: review
```
