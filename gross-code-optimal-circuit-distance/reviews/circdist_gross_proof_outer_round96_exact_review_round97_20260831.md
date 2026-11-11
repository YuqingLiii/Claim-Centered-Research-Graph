# CIRCDIST Gross Round 96 exact review — Round 97

## Verdict

**CLEAR-PROPOSER-LEVEL-CONTINUATION**

The sealed Round-96 package is sound for linking and reuse only as exact proposer-level continuation evidence. It licenses the 24 concrete EFSSC selectors obtained from the twelve checked schedules and continuation from the fresh, unstarted iteration-160 state. It does **not** license a theorem promotion, a route promotion, a repair, an exhaustion claim, or any narrowing of the frozen residual. `CIRCDIST.gross` and its `gap-via-lift` completion route remain `CONJECTURED`; `D*_Gross` remains exactly `{11,12}`.

All twelve outer queries at iterations 148--159 are SAT. Both unrestricted direct-360 CSS-sector queries are SAT for every one of those schedules. Positive SAT mechanisms exclude only those twelve concrete schedules from the current finite outer search. They are not a universal cover. The exhaustive same-sector order-4 computation retains no novel selector, but that no-go has only the exact finite scope proved in Section 9.

This was a fresh, strict-serial review. I did not contact the proposer or any earlier worker, use a sub-agent, delegate, edit the sealed package, edit the scheduler or canonical node, commit, or push. The repository was already broadly dirty before this task. The only repository write made by this reviewer is this review. Appendix C is a dispatchable complete replacement document; this reviewer did not install it.

## 1. Commission, version boundary, and independent method

The commissioned live identities were read independently:

| object | observed SHA-256 |
|---|---|
| `operations/circdist/SCHEDULER.yaml` | `c09e15bfef6b0c58e6fd8c024603d38e3323ee00bebcbc5ee8f8dcf273c83556` |
| `circdist/proof-dag/nodes/CIRCDIST.gross.yaml` | `f84492190a1dad3b5d69bf38a9a62d3212f0c3844ee3338dc96517fbb0671135` |
| Round-95 review | `b6a23911b5f9974454a4f4291eaa09e30308547925aa71972d5199e3715c9450` |

The package-bound node and Round-95 review equal the live objects byte-for-byte. The package-bound scheduler is the historical SHA-256 `3c8965b3cc30f6ebcdc5f051073f2c0eb0dc39d537cd9f3f171633d6eac7bab1`. A line-level comparison showed that the live scheduler advanced only to settle Round 96 and authorize Round 97, with corresponding budget/ranking/log changes. This is the expected version boundary. Protected replay therefore belongs against a disposable repository containing the bound historical scheduler; replacement-node gates belong against a separate overlay containing the commissioned live scheduler.

The primary independent checker is reproduced in Appendix A. It is standard-library-only and imports no package module. Its identity is:

| property | value |
|---|---:|
| path during review | `/private/tmp/circdist-r97-review-20260831/r97_cleanroom.py` |
| SHA-256 | `ab470229c20f73a0eef2818497bc60f0beed1c82bc74e529c4d043677d3d77af` |
| bytes | 53,328 |
| LF | 626 |
| successful result SHA-256 | `c8cfb09a07829cdcef20eb9cf81157f7131569b084c85bde1450dc768040550f` |
| successful stdout SHA-256 | `a822d4dfeb8fc3484fd783a69c883a18b0e68c1c73eaa988c26d8feb0a510eb2` |
| final wall time | 122.419 s |

The exact final command and terminal disposition were:

```sh
cd <repo>
/usr/bin/python3 /private/tmp/circdist-r97-review-20260831/r97_cleanroom.py   > /private/tmp/circdist-r97-review-20260831/cleanroom-final.stdout   2> /private/tmp/circdist-r97-review-20260831/cleanroom-final.stderr
# rc=0; stderr empty
# R97_CLEANROOM_ALL_PASS 13 12 24 122.419
```

The checker parses bytes, JSON/JSONL/gzip, DIMACS, complete assignments, formula traces, frozen geometry, schedules, state files, transition intents, process ledgers, and exact GF(2) supports. It independently recreates both encoders. It does not call `replay.sh`; sealed replay is a separate corroborating check.

## 2. Package census, seals, inventories, and inherited identity

A recursive regular-file walk, independent of every manifest, gives:

| property | observed |
|---|---:|
| physical files | 1,589 |
| total bytes | 336,522,684 |
| total LF bytes | 4,592,093 |
| root-manifest rows | 1,588 |
| payload-manifest rows | 1,587 |
| inventory rows | 1,586 |

Every row set is sorted and unique, every path is normalized and relative, and the sets exhaust exactly their intended domains. The root manifest equals all files except itself; the payload manifest additionally excludes the root manifest; the inventory additionally excludes both manifests and itself. I streamed every listed file, recomputed every SHA-256, and checked every inventory byte and LF count.

| object | observed SHA-256 |
|---|---|
| `SHA256SUMS.txt` | `d992087072835e2651834aceb3012f8afd20442b2886673b45254e95e861a361` |
| `PAYLOAD_SHA256SUMS.txt` | `9cf210a8dd392a57700a61b640ced0deda5d212173f88293083759f67cb77121` |
| `FILE_INVENTORY.jsonl` | `f472a22f81197aa78d401caa77e85011549898491fbc3f174cd1bc562b62939b` |
| `REPORT.md` | `e0c3ff15d41f9d3c494a501bafd78b5a1c1a3b5d072061b7b7bcefd073ebc4fe` |
| `RESULT.json` | `cb395187a01c30f560e94f1310044a5a248cd67d44d65cd252fe2552fbba6434` |

The protected pre-install and post-install snapshots are byte-identical over exactly 231 files. Their common snapshot SHA-256 is `39b1b2565237d67972d98b18364f481f1928d3f9def622bc2e3fb0aa8eb78ca7`; all protected and canonical paths are unchanged.

The inherited Round-94 root and payload seals recompute as `1e0a4af8591aa63ccccd1b2516c630eccb11a73fb9dea2e0ff1e0d32ed82ac1c` and `c39ef3552e461dd7513812b8296901e72369dfacbf6e71ae758b5bb58ed94c54`. Round-96 iteration-148 state plus all six formula artifacts are byte-identical to Round 94's reviewed fresh frontier. The inherited state is `next_iteration=148`, `started=false`, `stop=null`, has 256 selectors, selector-state `9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f`, and state-file SHA-256 `1902599acc47eb5d354692759b2d09d6ff1cfcd5e013f2b907cc310376ee6e81`.

A full Round-94 path scan for `iter148` returns only the six formula files, two bounded compile/check process records, their stdout/stderr logs, four wrapper logs, and the state file. There is no inherited iteration directory, assignment, solver disposition, model, or proof. Iteration 148 was truly fresh and unstarted before this campaign.

## 3. Exact outer source-to-CNF reconstruction

For every iteration 148--160 I independently decompressed and parsed source, metadata, assertion map, circuit trace, and DIMACS. The semantic source identity is

`SHA256(canonical_JSON(source with semantic_payload_sha256 removed))`.

Every stored semantic hash, source-file hash, CNF hash, assertion-map hash, and trace hash agrees. Selector lists are exact prefixes across successive sources. The inherited order vector is unchanged in all thirteen formulas: 1,440 unary predicates, 20 Round-62 predicates, 12,820 generalized predicates, and 204 dynamic predicates, totaling 14,484.

I independently emitted each definition family:

* constant true: `(v)`;
* `v <-> (a and b)`: `(-v,a)`, `(-v,b)`, `(v,-a,-b)`;
* `v <-> (a or b)`: `(v,-a)`, `(v,-b)`, `(-v,a,b)`;
* `v <-> (a xor b)`: `(-a,-b,-v)`, `(a,b,-v)`, `(a,-b,v)`, `(-a,b,v)`;
* rank membership: all 32 truth-table rows over the five pairwise comparisons of one check qubit against the other five, with output polarity selected by membership of the comparison popcount in the declared position set.

The 10-bit little-endian comparator recurrence was checked on all `1024 * 1024 = 1,048,576` value pairs. Across the thirteen formulas there are 6,410 formula-local rank-membership domains; checking all `6!` local orders and six qubits gives exactly 27,691,200 rank cases.

I then independently reconstructed every source root in source order: unsigned time nonnegativity (zero clauses but retained assertion records), `<864`, X-ancilla and Z-ancilla distinctness, data-conflict distinctness, 648 two-qubit MC equivalences, extrema inequalities and attainment, both global-interleaving roots, all 14,484 blocks, and all EFSSC exclusions. Primary and definition variables partition `1..nvars`; every non-primary variable has one defining trace record. Definition and root clause IDs are disjoint and together partition `1..nclauses`. No assertion, clause, variable, or family is unaccounted for.

The aggregate over all thirteen formulas is 248,950 source assertions, 5,334,819 variables, 18,083,210 clauses, 5,221,979 definition records, 298,558 root clauses, and 27,691,200 local-order rank cases. The aggregate clause-family vector is:

```text
constant                         13
def:and                   8,742,699
def:or                    3,797,616
def:rank_membership       1,230,720
def:xor                   4,013,604
root:block:dynamic            2,652
root:block:generalized      166,660
root:block:round62              260
root:block:unary             18,720
root:distinct                56,160
root:efssc                    3,484
root:extrema_attained            52
root:extrema_inequality      22,464
root:global_interleaving         26
root:mc                      16,848
root:time_upper_bound        11,232
TOTAL                    18,083,210
```

### Formula identities

| iter | selectors | assertions | variables | clauses | CNF SHA-256 | source file / semantic SHA-256 | map / trace SHA-256 |
|---:|---:|---:|---:|---:|---|---|---|
| 148 | 256 | 19,138 | 409,157 | 1,385,059 | `397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4` | `0db20ed8ca0b120cda91eb7a94be25094adb9b77a2cacdd322e330a720d58b5f` / `2fd4a1982e1f6389804f7eee1120706f9d26c9e6a23acc05e2a15e036a67c032` | `894a977dd56bc2bfb158b6e95dcfb6691802f5ff15d2aba2410f2b7971627a1a` / `97f9ec35ff3cf539dc432a6b345fc18cb92a1c786256e869fa5066146b61316a` |
| 149 | 258 | 19,140 | 409,417 | 1,386,178 | `6516f9ea030c0447f37c05526c514ea22813adaf184aef1a4a0695b451cdba5c` | `28bb711319acf512bb7d1bd2e23f50c0c6251f77f50c25b00009cf6b859c94dd` / `179285be0408bc7a7470ce25bd770f09f0f8c3487b5be8b0373f43ac712c6cd3` | `e0f671bf92a08a5e0fd79187fee319317dfafca661a56773ca6a3aa17750ceba` / `3f47d4f98078d2de821da993d82d04dfe3820ae5331ca29c8db10bb00c868ec3` |
| 150 | 260 | 19,142 | 409,582 | 1,387,284 | `a92ab9bac8d2051eb919eb8ac43024ad080fb4f5214c89a4dbebffeba91218b1` | `902bc3051d0adaa76a75933ec8d1f093364eff46960f2a90b13f8b3f962b7869` / `d88da266ad026e7ebcf0c90b2eaf25da665175930117c8746e8f17b64838b6ef` | `0907fdc6285dea4361cd8e86e43c1d06496c536b86b4361285afb7ec53d6ba14` / `07d4dd8cc1e3aa2860f685f30ea18df875e9ba766c4c631db0ef08d973058b2f` |
| 151 | 262 | 19,144 | 409,741 | 1,388,193 | `16a416e57d4aa1ec65f3c1a007a1814256d311544de5a963a4320680dbd01973` | `3e90319a22e43f04b105c207c25d822466c8db85f32f0273acbfcf9e06e2612d` / `29a4d9f5f82622c2c54e359505190e24f23f6cb319dc2222a367b4b6434c5750` | `d211d82f1225e8abb89b4a384b6b0a8c093bb513e6eb9ff58602a316ce9de400` / `72e001a9bf519018842377f2cd33edb06b37616e04886020d98b80a127e4ccb6` |
| 152 | 264 | 19,146 | 409,912 | 1,388,984 | `9e9e1f5378d1dcf3fb5aea90810505f39bc30f641640f397775bf1142db16ceb` | `19aebadd29bf7a457daec2dccf5dace107bf0272c3bd6c4c2bf8fbbcfe5ae2c9` / `06fd4a2e86b312286072f9a6c34c15998a2e891e8606571af27948cbf6e5c9cb` | `eae8249825b6f75554caa1e61aaf75a0bb0ea5ba8c8ad657ca6850fc7c7bc39f` / `520114abdb1a92ec9d1732f250395dff52468bd750c47c420df54cb146b407e9` |
| 153 | 266 | 19,148 | 410,160 | 1,390,235 | `59caf619014d6e9cbd4e11943962d6dea9ebd0ea2fb966f179431f5d0fd5f7c8` | `c497b4bfd1a197e4c37a9ab7fbafd9bd0b42d6ea79f8b1a5d2ec6ae66c06bd1c` / `2de22091d14cab507d942efa350f8fceb433103fe1a7004bcbae8ce80623ef06` | `f5b338ee00c0d51768fa7600304c543d7a9c422ab9772bc39547b1c70a8bab17` / `e71f8a9e3f73ba6e05e6fa8e5b5a0b8f68021771b80249cdd43ee08728c53194` |
| 154 | 268 | 19,150 | 410,410 | 1,391,319 | `1bae4b34433f063cb4c08924cc2b888856ec6581d990a90d50dc947ff6ae61ea` | `bfcb6312500d22945de7ee8ad94f7f40c9e300e05cb0df9fa450d4ae876b4ad1` / `1a99780977864ad871ba4cf729c217a7a5c4d4e276d31cbe6c89e8837031c311` | `eef4c2e6a3e8270e977ca291fc7c3101ccab68cfe524bdf4fcdf18de1ed9ba53` / `af904c9f8a112c5168420ea51fbbd53b3b2b1e379b0ca28825eab974f90d1a09` |
| 155 | 270 | 19,152 | 410,681 | 1,392,486 | `a1dbe9c0929cf8af6c8c5cbfe20c99f75df10326b426a7b4fb98ffd71602a6fb` | `700031f5e9b60955a933b377e48f5ce013a5c0e3eeec0c03a6d503f8b4ef11e4` / `7adf7ad6548d70d198a68385e334614202313a9da3dfc616bdde6a29b37200d3` | `d19854362a576156ba42e2bce7616d0826c64a12977cc3c54bf6395baceb5337` / `9eeb58b5c735d18401bb066ec2e2900fe1bc80fc4ced433b79a4e68764729fd0` |
| 156 | 272 | 19,154 | 410,760 | 1,392,766 | `f6fa21a5766d77a593b337726b6f1c1bfad9776de9cf9a7128dff1d4845c7f06` | `d184e93e8c9ee8547a1af454f305710bab786cd79d8d1d218d84cb7924cdc180` / `66555ce65def77e638429ea1cc11c8fc39a0a071a020aaaa107bb1737acdcbd5` | `e359cd67fb73286674816b4b86529ece2a5e6f2d3206662f3c46b6bb1f0e6d56` / `cbd7f1c3c2192484f92cac01f8d3c2ea183dd68a4a4322a2e0464a333ef1896a` |
| 157 | 274 | 19,156 | 410,916 | 1,393,495 | `0465ce59476310349dae8837111bfa900e7c3fa4050f95c832f2f7b346186e26` | `14fa670cd0f4d78be84e25ace60f0a3d91b81d5dfadc2b7ce673b8f2cb31e5a4` / `735bd14e04488be53b96c77d9b16de12b33d830c4ef8c92b6e324e6482361f81` | `f7efbb66ac29b319acd82d2b06d417bd3b6994da9f6bd1d281eaf52ebb12a92d` / `b730c78b7992a171b89df5b2ea0a7b4db33acf2bdd3c7416b9421d5667c52c4b` |
| 158 | 276 | 19,158 | 411,201 | 1,394,882 | `455bacd787401a45555abb88a1a020986b5443b7f6b29f5e2c1d03499c0c3023` | `5fa642ddadb9f2ce1068e02fafb7ebc46a8c8f9198de89d01526ba42660da26a` / `6620c7dafb54502b3668037106c42c6e99f436d3390b9566a2d1d3ee07ae49b2` | `7a5367bc13b6b8683799d43af33370cdcb410237aaa75bf7c1e4eed1de79e987` / `828b5178ef86eca3115a27410582499a493b8edc47359e703a4fbd87076d3647` |
| 159 | 278 | 19,160 | 411,356 | 1,395,607 | `00cae899873f157ddacc3126ec891987929d6430abcddcefac77debb542e3c98` | `fd2f46f713ee97992bb9f48236175b1dd05aa25ac3da232b45babe85b9fb3d2f` / `a5f4afa22bc8fa56e8558fd003853f7a5e39ba54433602fb976fe6eb68ac8827` | `ba04fb2f3ea3dd10a5ed546e6788473498d2b06792ad356b2cd6f7f7179d7e8f` / `dcb560b572f208762311746f19b4999081b877b01467c46b477b21d6b7ee374f` |
| 160 | 280 | 19,162 | 411,526 | 1,396,722 | `aa18d2857ed5a7aefacd33bf4fbd42fded914393e123a87f00e84e4920e39d59` | `8b754b649744a83eae6c80e64230f9782909b48e5613dcfd6c3c321d98b2dd66` / `bb19e724c66eb6f3df8830a205ba29a297f5795d42d3fe066fa3b873800789ed` | `bb03077f1052d9fadc3254f239e8873dd9fe07198c8035e18947822cea9a4d12` / `5a6992f6b2e93e78ed97efea3cc0fb8eb6ce9446f59ab4f8d70fe44cd12b8aa8` |

### Per-formula clause-family census

Every row also carries the fixed root families: unary 1,440; Round-62 20; generalized 12,820; dynamic 204; distinctness 4,320; extrema inequality 1,728; extrema attainment 4; global interleaving 2; MC 1,296; time upper bound 864. These fixed roots total 22,698 clauses; `EFSSC` is the current selector count.

| iter | const | AND | OR | rank | XOR | EFSSC | total |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 148 | 1 | 671,442 | 291,894 | 92,928 | 305,840 | 256 | 1,385,059 |
| 149 | 1 | 671,670 | 291,939 | 93,120 | 306,492 | 258 | 1,386,178 |
| 150 | 1 | 671,820 | 291,969 | 93,696 | 306,840 | 260 | 1,387,284 |
| 151 | 1 | 671,973 | 292,011 | 94,080 | 307,168 | 262 | 1,388,193 |
| 152 | 1 | 672,132 | 292,041 | 94,272 | 307,576 | 264 | 1,388,984 |
| 153 | 1 | 672,333 | 292,077 | 94,656 | 308,204 | 266 | 1,390,235 |
| 154 | 1 | 672,540 | 292,128 | 94,848 | 308,836 | 268 | 1,391,319 |
| 155 | 1 | 672,741 | 292,188 | 95,040 | 309,548 | 270 | 1,392,486 |
| 156 | 1 | 672,846 | 292,197 | 95,040 | 309,712 | 272 | 1,392,766 |
| 157 | 1 | 672,990 | 292,248 | 95,232 | 310,052 | 274 | 1,393,495 |
| 158 | 1 | 673,233 | 292,278 | 95,616 | 310,780 | 276 | 1,394,882 |
| 159 | 1 | 673,398 | 292,308 | 95,808 | 311,116 | 278 | 1,395,607 |
| 160 | 1 | 673,581 | 292,338 | 96,384 | 311,440 | 280 | 1,396,722 |

The package also performed a fresh deterministic recompilation of inherited iteration 148. CNF, assertion map, and circuit trace are byte-identical; metadata and encoding-check objects agree after excluding runtime-only seconds. The independent reconstruction additionally exercised first-clause mutation, truncation, comparator direction, time-864, and semantic-source mutation negative controls; each was rejected.

## 4. Twelve complete outer SAT assignments and frozen schedules

For each iteration 148--159, both retained assignment files decode to the same complete truth map: exactly one signed literal for every DIMACS variable, no omission, duplicate, or out-of-range variable. I evaluated all 16,686,488 outer clauses across the twelve assignments; every clause is satisfied.

Each 10-bit time word and extrema word was decoded without package code. If `t(e)` is a raw edge time, compression was independently defined by

`c(e) = |{u in used raw times : u < t(e)}|`.

The result equals every stored compressed schedule byte-for-byte. All twelve compressed hashes are distinct. Each schedule contains exactly 864 required named edges, uses nonnegative contiguous compressed layers, has no ancilla/time or data/time collision, satisfies every one of the 648 MC equivalences, and is globally X/Z interleaved. Every prior EFSSC-validity count is zero, as required by the outer exclusions.

The SHA values in `assignment files` are hashes of the stored gzip containers, in package order `assignment.dimacs.gz / assignment.independent.dimacs.gz`.

| iter | vars / clauses | assignment files SHA-256 | raw / compressed schedule SHA-256 | layers | overlap / whole interleavings | prior valid |
|---:|---:|---|---|---:|---:|---:|
| 148 | 409,157 / 1,385,059 | `ed38c0169180bb33b8276c557f5cfae7e638b21534ea24931676ca37c749fe8a` / `b6519db06d846f114d455a793fd5ec48df0637f92305cc86b00d54a982ec4be4` | `a11db70e227c4407a5306d5c89dc7f3622e9e1d7228d2feb3734939bafe3a018` / `1334982cca90f94a1e8a26235f2f7cab3aa3ec749c76e3bb4797a6c2294ca5a9` | 135 | 160 / 553 | 0 |
| 149 | 409,417 / 1,386,178 | `fa683ceec2e896cc395db590d447ee90086416458ed0333898c1f7a7b7dc9c8e` / `7c7d9cf262f636446bc21f45a26688891b84107c3729aa76d4d997604fa66997` | `3f22ae15a6b81279c50ced70e712100ec8842633405bdcca0567a15171626ebd` / `e32da3de9e7fb0c1ac30c7cc7e7ef0881cb21f4a2b5f7164dfbce56d1bad73e1` | 134 | 177 / 501 | 0 |
| 150 | 409,582 / 1,387,284 | `8000700bb23a2df9b7f96a35a895ed6c270a60c88a017a6790a77ac4c4b068b3` / `5d4f1e218fbbb823e0fc184d68f41f53cdfb331a5146d8c45f5510680e4d4a92` | `c85e3fae30c1d1eff154a0af4f95d7bb858a7a7e0dd9a7f0a5689aba0299c580` / `3e66cf8e79b50fea206090127fee77ff9eda84cb33722a25272fc46ebea08285` | 124 | 215 / 556 | 0 |
| 151 | 409,741 / 1,388,193 | `f43febc38ab7f22aa581c8dbd3893321cca8c5a4c7410465df4001984ff5467f` / `063aed43db804426fab8a1996a20d45b3dccf3ab130bb46c66b3e69fad394904` | `2e958b95a01e80a11cdf494ad39d229c9fb07d71be25ffbe879c5b01fe3b7687` / `37b62c5c84d6ceb567e437ea314dd36f93e229c03a70fdfcb2ff319a8262e1bc` | 73 | 124 / 498 | 0 |
| 152 | 409,912 / 1,388,984 | `316ac3128f4f8ee2f329598405ec5aa352b74f492bbbd4b953cee851af9e7f8f` / `2b8f81cc82bedb45157f2d5d8dab25fd3ce682633549604a3b536d44bdaa4e2c` | `9005b816dba6cf5204adfd7cb006bc40958f34537695bd311a706fc8a764eb8b` / `9d97671d8fd5f1b28f700de1b740883f6632cb3342135834ecddc121c9f7b33b` | 457 | 153 / 457 | 0 |
| 153 | 410,160 / 1,390,235 | `0fda013540737f97ab93fd81dea544e4f68428bf7b3a9db9dff65430fa3ad059` / `e22248bfc7b299354b162032a6df45ba45179585ee1360c69e8317177e837b3b` | `0a69bf6abf9781d114eaa0165996b7fd389ca8d1e5583b8c3b3dea785a9b5439` / `107e2f70debc8a2d8d1c2609dd9a6d08e96293badf52d425170b980d181877e9` | 135 | 162 / 508 | 0 |
| 154 | 410,410 / 1,391,319 | `948fee1f10114611b8513835d9ce678497e13fb7a41ecdf82cc89dadca20df3d` / `67b5405e9edaf596888c499e10563850e3b4bd4aa92303d381d0c49095839486` | `fd3c6254717c0b3734975140f662225c74ccb11ea8f05a14f7ee392b021a3371` / `efc0d3b624ba0e6c3b387cb97d6aa686c57cacc81470b156ad8487335b62372a` | 106 | 173 / 555 | 0 |
| 155 | 410,681 / 1,392,486 | `c88cca99732988c2c49d5fb170467145254fc2158f19c090ad556080c088f1c1` / `08f65d278372ae291642b96013eff4be756cd2e5fc797d5c48363f8dcf63f3e6` | `1754bfff552e889738fc10a92e7e297036081cbbf29ad5f5a72a024800b928a0` / `e300595c91479ec60b1d8920fcc6af294215b9d8b4c02f5720aae6e29c029412` | 96 | 128 / 492 | 0 |
| 156 | 410,760 / 1,392,766 | `fdf9c6dfcb068cfa5b094918b8caa9d3477c8333aa3a343fc3a872b37d51c813` / `4918e2b9ef359c66701f3f35a70af7d99d33055193bfba1c457b840506cdfc80` | `79e2fcea63c8de8057d13cdf42cafff92668c8f6b88de9913b07d8d1f25eeb9e` / `90b8c442094b67775e1d16b897cc3d5cfe8ba3ec8371422ee22e36d31c010472` | 106 | 198 / 568 | 0 |
| 157 | 410,916 / 1,393,495 | `c5918358c6bb7e18cba6d8bd1583958edcc77ee22635fff62c39e34f07b57273` / `a958949a3395cd8564981c2023e5602eefe11c414d709a75009a8f683c446cce` | `c680b44a5532dff6139fb529f8c735e96bbce9063e46c60c73a6041486add580` / `0e48652870b060e4dc9cb38c211bdf82c39f603d5b4b8cae3abdf67298a41679` | 120 | 186 / 548 | 0 |
| 158 | 411,201 / 1,394,882 | `03c04340eb500976f8f1bd3406e93053873d13030b3d1d1e56a447a7df951cd3` / `79d1f04b6ff4ec3f899882285a427c6bc152664ea87675fab5afc15ac326f556` | `7db9ee1aca1c9687745b312aaecb3c61c3be24f1a143d3a4537ae4a0145a9d8b` / `c8b6b430f2b31bb532ae8cfd37ba77eed2087244bd2d8dc93956712de2683528` | 127 | 174 / 532 | 0 |
| 159 | 411,356 / 1,395,607 | `f781ce224778dbaf39a34c056df2a323c6dbbd85c5ea20ed4266433f4b018392` / `bf84b33752f06c04848aa9f26b58e6d0fc2ccbe19e6d444b774dc6ccd5f9dbe8` | `8cfd57b498d1c8dc5328b0ad83ea43777333981d47405b86085812e8e9823abd` / `7118916dca99de714f42714c1bfcda8536447e8989ed533dcea7c795ce1275d9` | 131 | 183 / 535 | 0 |

These formulas are existential. Twelve satisfying schedules establish twelve counterexamples to the then-current selector cover; they do not prove a universal schedule, an absence theorem, or either exact value in `{11,12}`.

## 5. Twenty-four unrestricted direct-360 SAT adjudications

For a sector-specific set `F` of distinct named elementary fault locations, I separately compute:

* `N(F)`, the symmetric difference/set of named locations, whose size is the direct fault weight;
* `C(F)`, the XOR of canonical representative supports;
* `P(F)`, the XOR of physical schedule-ordered hook suffixes.

The direct query is accepted only if `1 <= |N(F)| <= 10`, its complete DIMACS assignment satisfies every clause, its frozen schedule remains legal, both detector syndromes vanish, the canonical and physical logical actions are equal and nonzero, and the resulting support is outside the stabilizer span. `|C(F)|` and `|P(F)|` are reported separately and never substituted for named-location weight.

For each sector and schedule I rebuilt all 360 columns: 144 data singletons `D:q` and `72*3=216` residuals `R:c:k`. Canonical residual positions are `{0,1}`, `{3,4,5}`, `{4,5}`; physical hook suffix positions are `{2,3,4,5}`, `{3,4,5}`, `{4,5}` in the schedule-derived within-check order. Each independently rebuilt formula has:

1. 360 unrestricted primary selection variables;
2. 72 syndrome parity equations fixed to zero;
3. 12 linked logical-parity outputs and one nonzero disjunction;
4. an exact prefix-threshold sequential counter for `sum(x_j) <= 10`.

No pool, residual-pattern, check-count, or within-check-order-family restriction occurs. The independently generated DIMACS bytes, variables, columns, clause JSONL, body hash, and summary match the stored artifacts for every sector. Aggregate direct size is 142,556 variables and 536,144 clauses. Every complete assignment satisfies every clause. Flipping one selected primary literal violates the complete formula; removing the first selected name loses the required zero-syndrome/nontrivial condition.

In the table, `w/cw/pw` means named/canonical-support/physical-support weight, `L` is the little-endian 12-bit logical vector, and the syndrome column is empty in both canonical and physical replay. `selector` is the canonical SHA-256 of `(sector, selected_names, data_support, group_kinds)`.

| iter | sector | vars / clauses | formula SHA-256 | assignment / mechanism SHA-256 | w/cw/pw | syndrome | L | selector SHA-256 | exact selected names |
|---:|---|---:|---|---|---:|---|---|---|---|
| 148 | Xerr | 6,003 / 22,592 | `0ce943051678026bc5d3f1845dea05b26f0ac805f729a74007d2e5922af6dea0` | `b617a352e640c95976c8378d827a38e2371341a6f91ebdfec4b9cd4b6c734c60` / `716d37779d90accee8493fe43aa1d46fe80f98ea6167b1ecc32b6c2727999ae0` | 10/20/22 | `[] / []` | `001100000010` | `7bf4a4b59c900dd441b0a86aa4754e578bf984d6705d0ccfdf5674137c39012d` | `D:130,D:136,R:44:0,R:55:2,R:59:2,R:63:0,R:63:1,R:65:1,R:68:0,R:71:0` |
| 148 | Zerr | 5,893 / 22,152 | `1db69a26dd18cd301d2de036e71aa21dce41f35a46c45b2a8b547f2e120e9e3d` | `84a5faca126358ff9db860b515caab29a6bbc9d292c4602d3c57596ccc1fcca3` / `85d722324db152b1f807a8c9f93a2d1db43b80f618da753b91e2f6634c672c36` | 9/18/18 | `[] / []` | `111110000000` | `c3e0197744514042e8e94bde06bf1f62308cfb1d8085d2b7641506d0cadce4af` | `D:117,R:51:1,R:53:0,R:56:2,R:57:1,R:58:0,R:58:2,R:60:2,R:65:1` |
| 149 | Xerr | 5,984 / 22,516 | `dceb6da4a51f27b7a0df23d4a82216930e4f7db69f6bf0601ffe7e623e3e58d0` | `a2aa719d0bf82a5d6a703078b613b21e3006aa35f0c7791b14a8556edfe2e839` / `79fafb995fe74de9f47d86e0a41d0daa3d1e5ee100391ebf71b59b18619f370e` | 10/12/14 | `[] / []` | `100111100100` | `8b548991a1b3351e662326f91d8fad731a16ed926f05aaeb8262a2c55e781773` | `D:55,D:64,D:67,D:70,D:72,D:73,D:95,R:5:0,R:6:1,R:28:2` |
| 149 | Zerr | 5,917 / 22,248 | `f64cc341b968fb859fdfb67201bc71466c35099160997871d1957f4a54af10b8` | `62ff54d23fb0573349200b23eb5e80890df36a0375ee9f8d3395e75860eeb366` / `e053f48a066c7d06e20120bf3b5e1e68a41edf391c28087b52cd2cb3afa61234` | 10/14/14 | `[] / []` | `001010000000` | `66162697d66f05893cd9b7a4907f8951a43cae58226b2a8d8b55b86b1bb3e050` | `D:19,D:25,D:98,R:31:1,R:31:2,R:33:0,R:38:2,R:40:0,R:42:0,R:42:2` |
| 150 | Xerr | 5,962 / 22,428 | `8994075688b4c3e3ab10314050ba60494554aaa609f890249c89a22b1bfbd7b6` | `6c39b6a5f22be93f97e7b9ff2d507718ded97f7e7cd9104041cdc63f1c7ddf0e` / `954f40712b9324b3f7fa05ae716ea66b33eb7e65aac63944556c4d0be822fdcb` | 10/18/18 | `[] / []` | `000001010000` | `d1f69ad1197b30ec9943201c2f362257f7061d8ec493ca4cae26e7972249ab5a` | `D:123,D:131,R:0:0,R:15:0,R:15:1,R:23:0,R:23:2,R:24:0,R:53:0,R:62:1` |
| 150 | Zerr | 5,900 / 22,180 | `dcaf1e42c0135ddafb67f96b7782cd801ac2c4c18cb1456e752e1642d5bd2df8` | `8e8161a8b7f2448e62ae44f53985194a586473a50c29ae1b0cf524e147bca2e0` / `9f06fc52c34e4fcc3c04340cb46c153f28a7a5bfe7afec3928be8d3ad2a670e4` | 10/12/16 | `[] / []` | `000001000000` | `ce9414a721ebf9c41303afc1a8bf9c80212e931dbfb80b4950e0ba46895581b9` | `D:70,D:71,D:133,D:136,D:137,D:139,D:142,D:143,R:8:0,R:70:0` |
| 151 | Xerr | 5,921 / 22,264 | `96923645f179f788334ef265f71a6793f3320c4a257e0631bcde4f400476d384` | `10f1ea7471202826989406dced0f767e3c03fe162d9abbf674c3731db560d51f` / `bc7773513f3a80126c909a922826598fc8a45acf24274febf9ac99174cf80bbf` | 10/18/14 | `[] / []` | `101100000001` | `c2059873e7eb9f031ea129315317e70f78992a5014a4ef44e15df473f7b5dd18` | `D:137,R:45:2,R:49:0,R:49:2,R:54:0,R:55:0,R:55:2,R:56:1,R:65:2,R:69:0` |
| 151 | Zerr | 5,904 / 22,196 | `5d3a697212f7299e9ee124882ed04eac502fa93b0b7491c170332d29be2dc8db` | `28b752432737cafbfd9970b9915e6f5b91399adf95671390714454a73a19df65` / `fa0c115514e199404b8f2cdfe9a741cbdb4bf36725c1bf1ef2760dc745d54ccd` | 10/12/12 | `[] / []` | `101001001111` | `72f4b52aec5ee693d3d50db81dbded4c3bb8cd004ad23b8c56ac266ca2ac7eaa` | `D:1,D:8,D:16,D:32,D:48,D:49,D:83,D:84,R:4:2,R:6:2` |
| 152 | Xerr | 5,997 / 22,568 | `6ead8e0dd1aa829ed75e7c128a433d92a6aaedbcd2656cfdb3fbd92b6ceeb3a8` | `36d58d3bd2f614172cecd16ed65ab2c02137640dd2980c8fed56789d9d8dd0b4` / `acae4e5fedee0e10fb59e21ebb17731c543db34f14dc7adae8cf961aed365422` | 10/12/16 | `[] / []` | `111100100000` | `cb3dc77f198405063e4cc6798398400d564fc77326c58468a9206054a47a59d3` | `D:81,D:97,D:122,D:128,D:129,R:44:2,R:51:0,R:52:0,R:59:2,R:68:1` |
| 152 | Zerr | 5,915 / 22,240 | `bd7f5f70d86dbffc217c77d4f6a01636f4051100b683b193c440c56a5d101818` | `57f74762f0168c826ea6c3a020ac88f4ddcfd0b3777db8b2283b5e07379a4b13` / `2e97f6a82f3e31c2b31ecbf558063e6e72319ab8c9e8fa42a6e6c853a390f0df` | 9/16/20 | `[] / []` | `000111001011` | `1bd7821e14064a9ff2252c6e8ed902d5749bf2a623632b4180588e9328cd0f8d` | `R:24:2,R:29:0,R:37:0,R:37:1,R:38:0,R:44:1,R:50:0,R:51:0,R:70:2` |
| 153 | Xerr | 5,945 / 22,360 | `71df1f7627a86c6513dde7b8871d1bf20f371e670ff2decacca573e525edb694` | `1cadc80053a70e97afee86415f7a49cc0d44e2bc8e188361c2e1c34d74c72044` / `6ef36c0b91949f5e5976ed9604aca96c0011908d1641666ff4b22f39dd7019f5` | 10/16/20 | `[] / []` | `000010000110` | `63c55d16a48a59a85825f972ab595f4dea80d901056e01cf76c29b16de6ffc68` | `D:135,R:48:2,R:49:2,R:55:0,R:61:0,R:63:2,R:64:2,R:65:2,R:68:2,R:70:1` |
| 153 | Zerr | 5,912 / 22,228 | `7d2fdd1febe811b0da984a3aaff3d6999703dd4002288c557adfe864efbdd123` | `9cb28f9850e86dbb86c845ee21a985ea2d240712c4d15dd8ce226c525208ca6d` / `f26b817dcb386dcfd436bc53be8f6027b87fbd1214a04227c40ba4d4da000d17` | 10/12/18 | `[] / []` | `010001000000` | `b062f957344798bd9c281bc74fa83e8fecea9933780ce0caacfa1c36d34025cb` | `D:25,D:29,D:31,D:91,D:104,D:105,R:19:0,R:24:0,R:28:0,R:30:2` |
| 154 | Xerr | 5,960 / 22,420 | `854d2753c871ba0443cb88f8d00f686cc269680d6447d4e695e1946e6b884040` | `c545f715b13791d9bb34351b471d173408f8fa02d2e9aab5cb2a2783cbd19584` / `38db1f0e85e44bed95e7bab406bf0e50df4ce3fc0149109167644393cd97053d` | 10/14/18 | `[] / []` | `010001110000` | `d11faffc89450c06a0abf098c2b22d3178fb28cc1460adc8e90e05cf0c010ccf` | `D:70,D:72,D:74,D:80,D:97,R:3:2,R:12:1,R:44:0,R:60:2,R:67:0` |
| 154 | Zerr | 5,884 / 22,116 | `f5bbf11818c5b0579c87803580acd7f4a5431e72dc11f3cde40604d766b2dbf1` | `28f311e106b7eb90e31ac6944d78dda6c5a86e22bcbc2a0247707eb272e980df` / `e7cf86f52d79bfa2ddc44490c86a2906537e54604a62ad72b0b82e041c5dc33c` | 10/18/24 | `[] / []` | `110011110101` | `45b36090e1bb127d0d97b3cc03e6ef8a10e3b048d4181c9436517a6d1c0a0448` | `D:67,R:5:2,R:21:2,R:52:2,R:53:0,R:61:2,R:62:2,R:68:2,R:69:0,R:70:1` |
| 155 | Xerr | 5,973 / 22,472 | `91e4b6a2443136c14e06e57ba3ab9ae3dc3a41f460b98fc79b50b3b76e7df222` | `1f95601cfdc9cc847d4a302d98abd7c74c4170be87c4d342ab6d249522d08d6e` / `9a6b89c6abca7c89221dd746c2242355bff3314d45e915bb777faa88809ca1d7` | 10/14/14 | `[] / []` | `011001000000` | `a18b2d6d265c5c8c514f1f7658a2ba0014c494b062140cb827156933f09bbb19` | `D:63,D:105,D:115,D:116,D:122,D:132,D:139,R:5:1,R:22:2,R:30:0` |
| 155 | Zerr | 5,900 / 22,180 | `18f82b9cc48313f69880ebddbed1b8c3a8a2fe9f5074dc17c2ee7acb3c4453e7` | `0f9cdbcded3f3e5c93c3238f1d3bebac75eb8d42d892dcb654ad36000c9758c6` / `0f77747d14a57d774360b66821647e0010a52bc12a543360dfc82876100b3d08` | 10/12/14 | `[] / []` | `011010100100` | `9b6e6a6a7a6a1a88ee2835168af6b6c135d0c18e67845feb3237ed07602b4f84` | `D:2,D:40,D:41,D:58,D:92,D:98,D:104,D:113,R:15:0,R:24:2` |
| 156 | Xerr | 5,932 / 22,308 | `eecc981d80ab9bf39b14346d3618df66fcddea20d253ef3c7016153f9c73656a` | `ada2deee8e480ea127f13ef21abafd6192bb84d10e403d5c36578458a710d228` / `ccb958726026ae8433e6cf5b98cc8fab2ae8678c1b3299110f0455ce3311f8b9` | 10/14/14 | `[] / []` | `100011000100` | `8fc11f3a9b1ce9de1b370efe51d08a503ae546636088a2927a9eaa65cb410452` | `D:48,D:98,D:107,D:114,D:122,D:123,D:139,R:15:1,R:19:2,R:24:2` |
| 156 | Zerr | 5,937 / 22,328 | `db3cd937a78c04a82ce02cca72567e5083aa1e861aab0fda7db907ffd691bb6f` | `0879703354f71e2d74c57727d7daebd5738619254e5d462f99eee0bb3e772e60` / `ca787af50c23a952783e0113d6456a1662ffb8a413d25a4fd03683611006a565` | 10/16/14 | `[] / []` | `101000000000` | `5b141c9d1546e4e277d69a15475678be50e328108ac7d5b2922d9b1f83d8bd6f` | `D:132,D:136,D:138,D:141,D:142,R:0:1,R:1:1,R:2:0,R:2:2,R:67:1` |
| 157 | Xerr | 5,992 / 22,548 | `1cf27a5c5a8319e52e52f906f4f133d14ad0a99b22207bce0d006161935fb93d` | `a8cf066cadbafbff4599bea78e81998e94d1a49824ac3a4a7d9e343a50b3762f` / `8e907993015b768184fa51a7c41a343cd1d360a039067426a9126d6fb9e02938` | 10/14/18 | `[] / []` | `010100001010` | `6f46efdf55ab4ac7b0f5433b9315b68b74d4db48b3358fe3f1934210c982bcfc` | `R:33:2,R:34:1,R:42:1,R:42:2,R:44:0,R:45:2,R:50:0,R:52:2,R:56:2,R:57:2` |
| 157 | Zerr | 5,974 / 22,476 | `097ff8dd33792a96a70ac7fb0f7c92b68354ca02fdaac350cdedd32aa893be7d` | `6c1fddccfd93f1c711bf30c13f35407e937854d8de6f474b0fcb782c35f1d9fb` / `fa422dc1d2d65271d6d2aa4ed6d6a117396908178314e3ff5cfe4d83cb1a5201` | 10/16/22 | `[] / []` | `100000000000` | `9f1b81a30d9dfd6d579f2ed97dbad8b61836ce1cc04a4bd38c960b8d01493bc5` | `R:43:0,R:44:0,R:50:0,R:52:1,R:56:0,R:59:0,R:59:2,R:61:0,R:66:0,R:66:1` |
| 158 | Xerr | 6,023 / 22,672 | `43792684446b41c1fdcf578cdccb46317ce51058b7f334e002a52f3b0930f990` | `7a370f3d9c6bb94b93382df6d408fe539d5f332b58de1c47daa1367ae6bf0f09` / `c93a1384b2b7f88c8b2d23f0f1461ca98b0a32644c426516afdc7497e0d040f7` | 10/16/14 | `[] / []` | `010101000000` | `d0389ef2ff27841b3daf2bf7ad35c4b9016b1edca1f688399849c736c11a53ac` | `D:94,D:117,D:120,D:125,D:142,R:17:2,R:18:0,R:18:2,R:26:2,R:33:1` |
| 158 | Zerr | 5,903 / 22,192 | `789fff44effbeac5845178a171484fdb62c6764069e967737c8b0e979c0e51b6` | `8a615f34e3a9c83313319cfa5000f1739f806b17fb949bc547556c639f8bad8b` / `5716317fd3ccfc6c4244367709790d712743e543aadf4357724dba59254e0bea` | 10/16/20 | `[] / []` | `101011100001` | `0091d1b1d08cff3986549ad31449adc177f3718cdedff32dbefe7d4148bd9867` | `D:22,D:28,D:29,D:30,D:129,R:19:0,R:34:1,R:58:2,R:60:0,R:65:0` |
| 159 | Xerr | 5,940 / 22,340 | `d25160e550afe759d53437eeea136e3950180f4ab685a1ceb355915caa1ccb43` | `f726d612ed37fa1e7fc23570dcb2e9599ae18606f6a8d025af1818579d1f7192` / `bb6fa33a82b3615329ce2e7f01c776f5ea504dd3bf846303d952f28751621edf` | 10/16/18 | `[] / []` | `001100000010` | `e0d91360c0daea464018ebf4546767b90a438ea67f9069e96f6ea186a7da4181` | `D:60,D:63,D:137,R:4:0,R:4:2,R:48:0,R:55:0,R:61:0,R:61:1,R:68:0` |
| 159 | Zerr | 5,885 / 22,120 | `c3e3e238fcb8907367610f3db51f4cccc3ecd89bb963cdc511219f7e011702cd` | `ffbc451ed3b86ce5054c41ce2b40a1dccca4581273d93a486dfe131084824a55` / `d5f9634020231d84b457378cf2f67bc57aa9027b9836ad76d98f63d5a78d7500` | 10/14/12 | `[] / []` | `110010000000` | `9e185a8ffbb293d8f0c774398ac8dcdfa745cba2446678fd75bd30eec1269986` | `D:39,D:97,D:99,D:106,D:108,R:37:0,R:39:2,R:40:0,R:40:1,R:50:2` |

All twelve Xerr mechanisms have named weight 10. Zerr at iterations 148 and 152 has named weight 9; every other Zerr mechanism has named weight 10. There is no weight-8-or-less event. Both parities are nonzero for all 24 witnesses, and canonical and physical logical vectors agree. The 24 positive witnesses prove only existence on their named source schedules.

All 36 SAT solver calls had proof output enabled. Every stream was completely read and summarized with SHA-256, bytes, LF, and empty-clause count, then deleted because a SAT-side stream is not an UNSAT certificate. All 36 have zero empty-clause lines and 36 distinct hashes. The proof of each positive result is the complete assignment plus exact clause and physical replay, not a refutation certificate.

## 6. EFSSC semantics and exact atomic lineage 256 -> 280

For selector `s`, sector `S`, check `c`, and qubit `q`, the reconstructed rank-membership bit is

`m[s,c,q](t) = 1 iff rank_t(q within c) lies in XOR(residual_positions[k] for k in group_kinds[s,c])`.

Let `sigma[S,q]` be the frozen 84-bit detector/logical signature and let `d_s` be the XOR of declared data-support signatures. Then

`E_s(t) = d_s XOR XOR_{c,q : m[s,c,q](t)=1} sigma[S,q]`.

The selector-valid literal is exactly “detector bits 0--71 of `E_s(t)` are all zero and at least one logical bit 72--83 is one.” The appended outer root is its negation. I reconstructed that Boolean circuit for every inherited and new selector and checked it against the trace. This proves the cut sound on the complete frozen `S_Gross` outer domain. It does not make a schedule-specific physical representative valid on a different schedule or geometry.

For each transition `i -> i+1`, the next selector array is exactly the previous array followed by `[r96-i-Xerr, r96-i-Zerr]`. The source compact array is the same ordered append restricted to the declared compact keys. Pending intent and atomic commit carry byte-equivalent payload objects; both say state promoted last; the commit says every output is present. Every record says `repair_entered=false`. All final selector semantic hashes are distinct, so there is no collision, omission, unordered append, silent repair, or reuse of rejected output.

| state iteration | selectors | selector-state SHA-256 | state-file SHA-256 | source file / semantic SHA-256 | CNF SHA-256 |
|---:|---:|---|---|---|---|
| 148 | 256 | `9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f` | `1902599acc47eb5d354692759b2d09d6ff1cfcd5e013f2b907cc310376ee6e81` | `0db20ed8ca0b120cda91eb7a94be25094adb9b77a2cacdd322e330a720d58b5f` / `2fd4a1982e1f6389804f7eee1120706f9d26c9e6a23acc05e2a15e036a67c032` | `397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4` |
| 149 | 258 | `74bf041d7a029a8ef3802cc751848dd9f91a2cf8061e8a193ba2260defe6e66c` | `f2c9da37373cb956bb800827c4d7c94a08f7c60a6bb4d226dde0db0cbd7d5ede` | `28bb711319acf512bb7d1bd2e23f50c0c6251f77f50c25b00009cf6b859c94dd` / `179285be0408bc7a7470ce25bd770f09f0f8c3487b5be8b0373f43ac712c6cd3` | `6516f9ea030c0447f37c05526c514ea22813adaf184aef1a4a0695b451cdba5c` |
| 150 | 260 | `ac0699fb7e2d129fe5259ac0fc8c1a8528b126fa4209d75d829c0c1cdaf4cb88` | `079739f7a6f1e9674b4e7b5f50efcd88933e8e330ea50db47388ce42b7a1ac7f` | `902bc3051d0adaa76a75933ec8d1f093364eff46960f2a90b13f8b3f962b7869` / `d88da266ad026e7ebcf0c90b2eaf25da665175930117c8746e8f17b64838b6ef` | `a92ab9bac8d2051eb919eb8ac43024ad080fb4f5214c89a4dbebffeba91218b1` |
| 151 | 262 | `0130aa25e3cef5ea8ee45010955248e83298fee34dcf19a811edfdb0607e1044` | `ef74570e87a12201ba21ec0db9104ecce03756ba430da68bd3c98670dab547ad` | `3e90319a22e43f04b105c207c25d822466c8db85f32f0273acbfcf9e06e2612d` / `29a4d9f5f82622c2c54e359505190e24f23f6cb319dc2222a367b4b6434c5750` | `16a416e57d4aa1ec65f3c1a007a1814256d311544de5a963a4320680dbd01973` |
| 152 | 264 | `f5548affa2a1a7460f399067dd0796c2873d0d85aeb12d88790c325220bd2ea0` | `81e101c21a5deb8713ee291978d98f8b3274414eb1d9e2e33527bc3519f11a52` | `19aebadd29bf7a457daec2dccf5dace107bf0272c3bd6c4c2bf8fbbcfe5ae2c9` / `06fd4a2e86b312286072f9a6c34c15998a2e891e8606571af27948cbf6e5c9cb` | `9e9e1f5378d1dcf3fb5aea90810505f39bc30f641640f397775bf1142db16ceb` |
| 153 | 266 | `543afe1f2346a9fa3c0d1946a09dc4e66f4ecfb5c7da08b95420db44076c1ebf` | `3d7a19fa29ddf1a831813d917fec6fa66f4a637a477c3929543fa93898ad6973` | `c497b4bfd1a197e4c37a9ab7fbafd9bd0b42d6ea79f8b1a5d2ec6ae66c06bd1c` / `2de22091d14cab507d942efa350f8fceb433103fe1a7004bcbae8ce80623ef06` | `59caf619014d6e9cbd4e11943962d6dea9ebd0ea2fb966f179431f5d0fd5f7c8` |
| 154 | 268 | `3f144c28666a394df8c2ca54b5614648d6dd75eba4cfa81d74760dc6d527430f` | `3e4980aabe1d023e7739bb986c1a55b658299c9b2b90e20f5c0a66ef3d3f7eda` | `bfcb6312500d22945de7ee8ad94f7f40c9e300e05cb0df9fa450d4ae876b4ad1` / `1a99780977864ad871ba4cf729c217a7a5c4d4e276d31cbe6c89e8837031c311` | `1bae4b34433f063cb4c08924cc2b888856ec6581d990a90d50dc947ff6ae61ea` |
| 155 | 270 | `fe49161cbc43006540b4ef04032b345705a124b47f55569e6b53722180999308` | `148c4f545b574733d4aba69667788f8db920b2662d835219e49faa4592414b37` | `700031f5e9b60955a933b377e48f5ce013a5c0e3eeec0c03a6d503f8b4ef11e4` / `7adf7ad6548d70d198a68385e334614202313a9da3dfc616bdde6a29b37200d3` | `a1dbe9c0929cf8af6c8c5cbfe20c99f75df10326b426a7b4fb98ffd71602a6fb` |
| 156 | 272 | `7004c3bbf2932b81ba056e54e6ad475cb0ce0217ce1841f6ffb61b474711a977` | `4d8a55d7012c222fdb483915bf7385b5c11e4ed95f71fc7c993c1e0ecb50e856` | `d184e93e8c9ee8547a1af454f305710bab786cd79d8d1d218d84cb7924cdc180` / `66555ce65def77e638429ea1cc11c8fc39a0a071a020aaaa107bb1737acdcbd5` | `f6fa21a5766d77a593b337726b6f1c1bfad9776de9cf9a7128dff1d4845c7f06` |
| 157 | 274 | `dca60e10329912f52268af403c44122b99712c068ff09315ab166e1db9e3b417` | `bde4937d9aaaad01e35f9add06fcb4b79706bfb6fe437ce5b947bee9d6a8cdbf` | `14fa670cd0f4d78be84e25ace60f0a3d91b81d5dfadc2b7ce673b8f2cb31e5a4` / `735bd14e04488be53b96c77d9b16de12b33d830c4ef8c92b6e324e6482361f81` | `0465ce59476310349dae8837111bfa900e7c3fa4050f95c832f2f7b346186e26` |
| 158 | 276 | `d2d25eea43b346574ec54f0cff535aa86c286040b4e0319e82a63931a2608fb2` | `3c70a7de7927ecbfbc835f77c7aebfa34f3ddf25a4ff24d74e13c96468ab9589` | `5fa642ddadb9f2ce1068e02fafb7ebc46a8c8f9198de89d01526ba42660da26a` / `6620c7dafb54502b3668037106c42c6e99f436d3390b9566a2d1d3ee07ae49b2` | `455bacd787401a45555abb88a1a020986b5443b7f6b29f5e2c1d03499c0c3023` |
| 159 | 278 | `d45635739fe0c9cea1cf4c3cd8d55ccf48ac445602cfd27c31c135af2c62d7e5` | `1cca8290cd39fffe1a5cbdff62d0a95b0200e4b6c2e99a7a2e0876d309f8e462` | `fd2f46f713ee97992bb9f48236175b1dd05aa25ac3da232b45babe85b9fb3d2f` / `a5f4afa22bc8fa56e8558fd003853f7a5e39ba54433602fb976fe6eb68ac8827` | `00cae899873f157ddacc3126ec891987929d6430abcddcefac77debb542e3c98` |
| 160 | 280 | `ad3cf364dd9224c14ffb55046ba3dc8eb80035b1eaf997f1d7a5691297ad62a3` | `bb26ce4fc03ae9616a6a325438c3f4c82568a15c4fe133e074959b894e358194` | `8b754b649744a83eae6c80e64230f9782909b48e5613dcfd6c3c321d98b2dd66` / `bb19e724c66eb6f3df8830a205ba29a297f5795d42d3fe066fa3b873800789ed` | `aa18d2857ed5a7aefacd33bf4fbd42fded914393e123a87f00e84e4920e39d59` |

The retained IDs are therefore exactly the inherited 256-prefix followed by

`r96-i148-Xerr,r96-i148-Zerr,...,r96-i159-Xerr,r96-i159-Zerr`

in increasing iteration and Xerr-before-Zerr order. The final count is 280.

## 7. Fresh, checked, unstarted iteration 160

The final state is `next_iteration=160`, `started=false`, `stop=null`. A package-wide path scan containing `iter160` finds exactly these 17 files and no others:

```text
formulas/iter160/assertion_map.jsonl.gz
formulas/iter160/circuit_trace.json.gz
formulas/iter160/encoding_check.json
formulas/iter160/metadata.json
formulas/iter160/outer.cnf.gz
formulas/iter160/source.json.gz
logs/process/iter160_pending_compile.json
logs/process/iter160_pending_encoding_check.json
logs/stderr/iter160_pending_compile.log
logs/stderr/iter160_pending_encoding_check.log
logs/stdout/iter160_pending_compile.log
logs/stdout/iter160_pending_encoding_check.log
logs/wrapper/iter160_pending_compile.stderr.log
logs/wrapper/iter160_pending_compile.stdout.log
logs/wrapper/iter160_pending_encoding_check.stderr.log
logs/wrapper/iter160_pending_encoding_check.stdout.log
state/iter160_state.json
```

There is no `iterations/iter160`, no transition starting at 160, and no iteration-160 assignment, model, proof, solver status, or disposition. Its exact bindings are:

| property | value |
|---|---|
| selectors | 280 |
| selector semantic/state SHA-256 | `ad3cf364dd9224c14ffb55046ba3dc8eb80035b1eaf997f1d7a5691297ad62a3` |
| state file SHA-256 | `bb26ce4fc03ae9616a6a325438c3f4c82568a15c4fe133e074959b894e358194` |
| source file SHA-256 | `8b754b649744a83eae6c80e64230f9782909b48e5613dcfd6c3c321d98b2dd66` |
| source semantic SHA-256 | `bb19e724c66eb6f3df8830a205ba29a297f5795d42d3fe066fa3b873800789ed` |
| assertion map SHA-256 | `bb03077f1052d9fadc3254f239e8873dd9fe07198c8035e18947822cea9a4d12` |
| circuit trace SHA-256 | `5a6992f6b2e93e78ed97efea3cc0fb8eb6ce9446f59ab4f8d70fe44cd12b8aa8` |
| assertions / variables / clauses | 19,162 / 411,526 / 1,396,722 |
| CNF SHA-256 | `aa18d2857ed5a7aefacd33bf4fbd42fded914393e123a87f00e84e4920e39d59` |

This is a checked-unsolved continuation frontier, not an absence result.

## 8. Exact order-4 input binding

The synthesis input `synthesis/inputs/iter137_state.json`, SHA-256 `ba670045a69722f9625d04d3f07d62e207db38f15e9323f8c32d89194bb585cd`, is byte-identical to the reviewed Round-94 `state/iter137_state.json`. It contains 234 selectors and selector-state `47792a8f8e757482604723abb0e08916f49b252f4ba07deae03cf4295159d0b6`. The source schedule inputs are also byte-identical to the reviewed Round-94 iteration-136 candidate and direct verification:

| input | SHA-256 |
|---|---|
| `iter136_candidate.json` | `9596d1456ea66c086c06b4b7b4aaf4e442da9943644ae9839d113f10d937a640` |
| `iter136_direct_verification.json` | `f206cb75b7af6cbf2c5421f58c9ebc0c1c0b51d7e44eb3f1c5713a47987a485e` |
| compressed source schedule | `45051af0b08e6647d50c6fb0535894173016fd013279e7a0eaee8b2e69ee2e44` |

Rebuilding every selector's normalized semantic object and source effect gives exactly 125 Xerr rows and 109 Zerr rows. There is no input mutation or hidden later-state substitution.

## 9. Exact same-sector order-4 GF(2) census

For sector size `n`, the independent enumerator streams strict indices `a<b<c<d`. Immediately before processing `c`, the left-pair list contains exactly all `(a,b)` with `a<b<c`, obtained by adding `(a,c-1)`. It combines each left pair only with `(c,d)` for `c<d`. Thus every unordered distinct quadruple appears once and sampling is impossible.

The closed forms are

`C(125,4) = 9,691,375`, `C(109,4) = 5,563,251`, total `15,254,626`.

As an independent multiplicity control, all unordered pair-pair decompositions split into overlapping, noncanonical-disjoint, and retained canonical-disjoint terms:

| sector | all `C(C(n,2),2)` | overlap `3*C(n,3)` | other pairings `2*C(n,4)` | retained `C(n,4)` |
|---|---:|---:|---:|---:|
| Xerr | 30,027,375 | 953,250 | 19,382,750 | 9,691,375 |
| Zerr | 17,319,555 | 629,802 | 11,126,502 | 5,563,251 |

The three right columns sum exactly to the first in each row. This catches overlap, duplicate-pairing, and ordering errors independently of the streaming counter.

For each quadruple the checker XORs the 360-bit named-location mask, canonical support, physical support, detector syndromes, and logical actions of the four rows. It records full named/canonical/physical weight histograms, triviality and zero-support counters, logical histograms, and a rolling 256-bit checksum. It then replays every unique named result with weight 1--10 through an independent sector verifier and compares the fully normalized object to `synthesis/order4_gf2_closure.json` byte-for-byte at JSON-object level. Appendix E reproduces that exact stored census.

| sector | domain | eligible occurrences | unique eligible | inherited | novel | canonical syndrome-zero | physical syndrome-zero | conservative valid | retained novel | max eligible multiplicity | checksum mod 2^256 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Xerr | 9,691,375 | 32,456 | 32,456 | 0 | 32,456 | 0 | 0 | 0 | 0 | 1 | `7995964f26ce16be693f5c459427c10855bd904cade6bd8279b47c2a75f7576c` |
| Zerr | 5,563,251 | 1,304 | 1,304 | 106 | 1,198 | 1 | 1 | 1 | 0 | 1 | `a7b44ab8479c13e64304bb8e4a023e9b17c38b570eabcdf8f3ebdff284c3862e` |

Every eligible named result has multiplicity one. Zero named-location, zero canonical-support, and zero physical-support counts are all zero. The sole conservative valid occurrence is at zero-based Zerr row indices `[5,79,95,108]`, with logical vector `100110100011`; its exact named result is already inherited as selector `r94-i136-Zerr`. Hence it creates no novel predicate, and the retained selector list is empty.

Three adversarial scope controls also replay exactly:

* **Sector separation.** The stored common name set has different Xerr and Zerr effects, so cross-sector XOR is not licensed.
* **Schedule locality.** A selector valid on its source schedule is invalid on the iteration-136 schedule, so schedule-specific physical validity is not globalized.
* **Weight separation.** The retained witness has named/canonical/physical weights `10/12/18`, refuting substitution of either net-support weight for named fault count.

The proved no-go covers exactly same-sector XORs of four **distinct** selectors from the post-i136/state137 bases on the declared frozen source schedule, under the conservative canonical-plus-physical agreement test. It does not cover mixed sectors, repeated selectors, order 5 or higher, another schedule/frontier, arbitrary physical mechanisms, or a universal schedule cover. Schedule-validity predicates are conservative: a term is retained only when both canonical and physical replays have zero syndrome, equal nonzero logical action, and legal source atoms. Failure to retain cannot be promoted to a global impossibility theorem.

## 10. Proof controls, environment, and process closure

The bound environment is macOS arm64, Python 3.9.6, z3 5.1.0, pysat 1.9.dev15, with no network use. The external interpreter is bound by SHA-256 `bdea59019a38eb6600cc9e71e984a97fedadc406448431281e7657030f54987e`; system Python lacks z3, which is disclosed rather than silently substituted. Native tools are:

| tool | bytes | SHA-256 |
|---|---:|---|
| CaDiCaL 1.9.5 | 967,144 | `fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9` |
| drat-trim | 70,120 | `f58f63b0f76945d4c4c9ff6e87afaf870f579e67c0f7cca589492df8fc7ebd47` |
| lrat-check | 36,552 | `bd7eb8052623525814a0a37502b47f05375d9d9dfaf96ddc2fcd858958517cea` |

I directly reran the six proof-tool controls. Valid DRAT returned 0 and generated LRAT SHA-256 `cf32dfff36b24ba36c3504765f29ecf3d7a8abaa59956ade4d24a4062caa6431`; generated LRAT returned 0. Corrupt DRAT, truncated DRAT, corrupt LRAT, and truncated LRAT each returned 1. These are only tooling fixtures. There is no Gross/direct UNSAT result and no candidate-specific DRAT or LRAT certificate.

The package process ledger has exactly 204 bounded foreground records, including 12 outer and 24 direct science solver children. The 36 solver intervals are pairwise non-overlapping in ledger time. Every child is reaped; timeouts, background processes, detached processes, and survivors are all zero. The 36 science calls return SAT code 10. The only non-0/non-10 records are the two disclosed order-4 implementation attempts described next.

FIX-2 independently records that the exact Round-96 scratch root was removed after the complete package was installed, the 116 preseal-replay children were reaped, and process scanning found no Round-96 survivor. The retained external interpreter is explicitly handed off as a bound dependency, not mislabeled as package scratch.

## 11. Complete failure and interruption disclosure

No failure below changes a scientific disposition or contributes an accepted result.

1. **Rejected bootstrap.** An initial setup command combined removal and creation. The safety layer rejected it before process creation; the filesystem was unchanged. Setup proceeded only after an absence assertion.
2. **Lexical-order negative control, rc=1, 2.904381 s.** The first order-4 script wrongly asserted `selected_names == sorted(selected_names)`. Reviewed selectors preserve direct-column order; GF(2) requires uniqueness, not lexical order. The assertion failed before any accepted census or state mutation.
3. **Python 3.9 compatibility, rc=1, 3.056889 s.** The corrected script used `int.bit_count`, unavailable in the bound Python 3.9. It was replaced with the already frozen popcount semantics. The complete repair-2 run then returned 0 in 60.963179 s wrapper / 60.838360 s census.
4. **Packaging-time GPT capacity interruption.** This was orchestration-only after the foreground 116-child preseal replay had already completed and recorded rc=0. It started no OS process, affected no science process or disk evidence, and triggered no repeat of solving or order-4 enumeration.
5. **Reviewer live-repository replay attempt, rc=1 at child 1.** I initially pointed sealed replay at the later live repository. `check_protected.py` correctly rejected live scheduler `c09e...3556` against historical binding `3c89...bab1`. The child was reaped. I then used a read-only disposable historical overlay. This is a reviewer setup boundary, not a package defect.
6. **Reviewer clean-room compatibility correction, rc=1 after formula/SAT checks.** My first independent order-4 loop also used `int.bit_count` and failed under Python 3.9 with `AttributeError`. I replaced it with `bin(v).count("1")`, reran successfully, then strengthened the checker with exact inherited-byte and scope-control assertions and reran successfully again. The final code and final run are the ones published here.

The proposer did not conceal any package failure. The review adds its own two scratch incidents explicitly. None produced an UNSAT claim, selector append, repair entry, or altered package byte.

## 12. Independent sealed replay

I created a disposable repository containing the exact package-bound protected inputs, including historical scheduler `3c8965...bab1`, then ran:

```sh
ROUND96_REPLAY_RECORD=/private/tmp/circdist-r97-review-20260831/sealed-replay-record-historical.json ROUND96_REPOSITORY=/private/tmp/circdist-r97-review-20260831/historical-overlay <repo>/circdist/artifacts/circdist_gross_proof_outer_round96_20260831/replay.sh
```

The result is 116/116 serial children PASS, all reaped, no detached process, empty stderr, no failure object, and total wall time 413.992748 s. The independent record is SHA-256 `935f0b92317cbefe04359fed767f2a309b4c25e78f3554e7a68ac9b338b93391`, 231,280 bytes and 2,793 LF. Its stdout is SHA-256 `80c1d38c993b45df8aa3b47c495f1d0b8eb45d0c92ea400fe993977e0641bc35`, 12,817 bytes and 144 LF. Exact stdout is in Appendix B. This replay corroborates, but does not replace, the independent encoder, assignment, state, and GF(2) reconstruction above.

## 13. Exact prelink evidence-closure set

Against the commissioned live repository before this review existed, the exact command was:

```sh
cd <repo>
/usr/bin/python3 tools/evidence_closure_check.py --problem circdist
# rc=1
```

It emitted exactly 1,588 unique diagnostics. Every diagnostic is `unlinked evidence` under the single Round-96 package prefix; there is no diagnostic elsewhere. The exact set equals every one of the package's 1,589 regular files except `bindings/initial_proof_dag/circdist/proof-dag/README.md`, which the checker deliberately exempts. Thus this is a set identity, not merely a count.

The sorted newline-terminated path set is 177,851 bytes with SHA-256 `b07043cabeada208f75c4115588c02c7c5bfdb531996f81f95172cd6418af7ad`. The raw 1,588-line diagnostic stream is 235,019 bytes with SHA-256 `eeab0722de6c52084f8ffb325d0623a0ef9ab6cfcec0393fe3d22bee37b1f503`. Appendix D publishes all 1,588 paths in exact sorted order.

The package's `verification/evidence_closure_interpretation.json` records 1,563 errors. That file is a disclosed pre-final snapshot. Its exact path set is a subset of the final set, with no extra path; the following 25 final-package paths are the exact set difference:

```text
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/FILE_INVENTORY.jsonl
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/PAYLOAD_SHA256SUMS.txt
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/SHA256SUMS.txt
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/round96_make_package_metadata_postinstall.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/round96_make_package_metadata_postinstall.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/evidence_closure_interpretation.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/final_preseal_checks.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/fix2_cleanup.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/fix2_cleanup.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/fix2_cleanup.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/fix2_closure.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/orchestration_events.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/evidence_closure.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/evidence_closure.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/evidence_closure.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/evidence_closure_parser.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/evidence_closure_parser.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/evidence_closure_parser.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators_driver.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/round96_make_package_metadata_postinstall.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/validation_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/write_final_reports.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/write_final_reports.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/write_final_reports.stdout.log
```

The 1,563 count is therefore not the final package census. The final commissioned assertion is 1,588 and is independently established here from the final tree. Linking the package directory as one evidence entry removes the entire exact set; it does not bless any additional path.

## 14. Complete replacement YAML and disposable-overlay validation

I formed Appendix C by preserving the complete live node and making only four append-only/frontier bookkeeping edits:

1. append one Round-97 summary paragraph;
2. append the Round-96 package and this review as two evidence entries (the review omits its own hash to avoid circularity);
3. replace only the current D-star frontier bookkeeping with the exact fresh iteration-160 facts and honest scope;
4. append one `gross-proof-outer-round97-review-2026-08-31` review event.

The proposed node is SHA-256 `912721a2fc92419ace54c78c092dee2d545b2a03262a4c1f22a16444c93435bd`, 79,555 bytes and 893 LF. A parsed-object structural guard reports old/new evidence counts 66/68 and event counts 18/19. After restoring `assessment.summary`, `assessment.basis.evidence`, the one replaced frontier object, and the top-level `events` array, the proposed parsed object is exactly equal to the live parsed object. Claims, claim hashes, levels, routes, children, formalization, all previous evidence, all previous frontier entries, and the full prior event history are retained. Both root and route levels remain `CONJECTURED`; the residual remains `{11,12}`.

I placed that exact node and a review-path placeholder into a disposable complete repository overlay based on the commissioned live tree. Nine sequential children all returned 0 and were reaped:

| gate | exact result |
|---|---|
| previous-state retention | `circdist: prior nodes, routes, and events retained`; 16 structurally valid nodes |
| proof DAG, circdist | 16 structurally valid nodes |
| proof DAG, all projects | `se=85, ksum=144, circdist=16, holevo-additivity-equality=8, holevo-counterexample-prevalence=19, holevo-extensive-violation=147, werner-holevo-capacity-threshold=20, grothendieck-d4=41, grothendieck-e8=9, grothendieck-group-orbit=11` |
| evidence closure | `circdist: evidence closure OK, 164 structured paths; all evidence project-local and linked` |
| migration | `Migration preservation OK: 16 nodes, 143 original events, 728 byte-identical copies` |
| release contracts | 14/14 tests OK |
| DAG contracts | 24/24 tests OK |
| Lean checker selftest | `SELFTEST: 23/23 assertions passed` |
| duplicate scan | PASS; 934 files, 24,868 mappings, `duplicates=[]` |

The exact 9-child structured record is SHA-256 `76469ed481d4c70116f6f41b04914d659d5d04cffaf3519de512ec3417837139`, 42,135 bytes and 130 LF, and is reproduced in Appendix B. Live `git diff --check` returned 0 with empty stdout/stderr. `git diff --no-index --check` between live and proposed nodes returned 1 solely because files differ, with empty stdout/stderr, so there are no whitespace diagnostics.

Appendix C is the single complete replacement YAML. Extracting the bytes between its one `yaml` fence and closing fence must produce exactly the SHA-256/byte/LF triple above; this is the installation artifact licensed by the verdict.

## 15. Branch accounting and epistemic limit

The `D*=11` branch remains open because no checked outer UNSAT establishes a universal finite selector cover. The `D*=12` branch remains open because no candidate had checked direct absence in both unrestricted sectors; repair and an explicit distance-12 certificate were never entered. Twelve positive continuations and a finite order-4 no-go narrow neither branch.

Accordingly, this review licenses only: link the sealed package and review, append the 24 exact selectors already represented by the fresh state, record the reviewed iteration-160 frontier, and continue strict-serial search. Any theorem-level use still requires independently checked branch-closing proof evidence.

## Appendix A — complete independent clean-room checker

The following is the exact final successful checker, SHA-256 `ab470229c20f73a0eef2818497bc60f0beed1c82bc74e529c4d043677d3d77af`.

```python
#!/usr/bin/env python3
"""Round97 clean-room audit. Standard library only; imports no package code."""
from pathlib import Path, PurePosixPath
from collections import Counter, defaultdict
from itertools import combinations, permutations
import gzip, hashlib, json, math, os, sys, time, gc

REPO=Path('<repo>')
R=REPO/'circdist/artifacts/circdist_gross_proof_outer_round96_20260831'
R94=REPO/'circdist/artifacts/circdist_gross_proof_outer_round94_20260830'
OUT=Path('/private/tmp/circdist-r97-review-20260831/cleanroom-result.json')
T0=time.time()

def sha_bytes(b): return hashlib.sha256(b).hexdigest()
def sha_file(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''): h.update(b)
 return h.hexdigest()
def canon(o): return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def objsha(o): return sha_bytes(canon(o))
def raw(p):
 p=Path(p); b=p.read_bytes()
 return gzip.decompress(b) if p.suffix=='.gz' else b
def load(p): return json.loads(raw(p))
def load_jsonl(p): return [json.loads(x) for x in raw(p).splitlines() if x]
def bits(v): return [i for i in range(v.bit_length()) if (v>>i)&1]
def mask(qs):
 v=0
 for q in qs: v|=1<<int(q)
 return v
def parity(v): return bin(v).count("1")&1
def popcount(v): return bin(v).count("1")

def parse_dimacs_bytes(b, keep=True):
 nvars=nclauses=None; clauses=[] if keep else None; seen=0
 for line in b.splitlines():
  if not line or line.startswith(b'c'): continue
  if line.startswith(b'p '):
   _,fmt,nv,nc=line.split(); assert fmt==b'cnf'; nvars=int(nv);nclauses=int(nc);continue
  vals=tuple(map(int,line.split())); assert vals and vals[-1]==0 and 0 not in vals[:-1]
  cl=vals[:-1]; seen+=1
  assert all(0<abs(x)<=nvars for x in cl)
  if keep: clauses.append(cl)
 assert nvars is not None and seen==nclauses
 return nvars,nclauses,clauses

def parse_assignment_bytes(b,nvars):
 vals=[]; status=None
 for line in b.splitlines():
  if line.startswith(b's '): status=line[2:].decode()
  if line.startswith(b'v '): vals.extend(int(x) for x in line[2:].split() if int(x))
 assert len(vals)==nvars and {abs(x) for x in vals}==set(range(1,nvars+1))
 return [False]+[None]*nvars, vals, status

def assignment_map(b,nvars):
 a,vals,status=parse_assignment_bytes(b,nvars)
 for x in vals: a[abs(x)]=x>0
 return a,vals,status

def check_clauses(clauses,a):
 failed=[]
 for j,c in enumerate(clauses,1):
  if not any(a[abs(x)]==(x>0) for x in c): failed.append(j)
 return failed

# Package census and seal rules.
files=sorted((p for p in R.rglob('*') if p.is_file()),key=lambda p:p.relative_to(R).as_posix())
assert len(files)==1589
assert sum(p.stat().st_size for p in files)==336_522_684
assert sum(p.read_bytes().count(b'\n') for p in files)==4_592_093

def parse_manifest(name):
 rows=[]
 for line in (R/name).read_text().splitlines():
  h,sep,rel=line.partition('  '); assert sep and len(h)==64
  q=PurePosixPath(rel); assert not q.is_absolute() and '..' not in q.parts and '.' not in q.parts and q.as_posix()==rel
  rows.append((rel,h)); assert sha_file(R/rel)==h
 assert rows==sorted(rows) and len(rows)==len({x[0] for x in rows})
 return rows
rootrows=parse_manifest('SHA256SUMS.txt'); payloadrows=parse_manifest('PAYLOAD_SHA256SUMS.txt')
actual={p.relative_to(R).as_posix() for p in files}
assert {x[0] for x in rootrows}==actual-{'SHA256SUMS.txt'}
assert {x[0] for x in payloadrows}==actual-{'SHA256SUMS.txt','PAYLOAD_SHA256SUMS.txt'}
inv=load_jsonl(R/'FILE_INVENTORY.jsonl')
assert len(rootrows)==1588 and len(payloadrows)==1587
assert len(inv)==1586 and [x['path'] for x in inv]==sorted(x['path'] for x in inv)
assert len({x['path'] for x in inv})==len(inv)
assert {x['path'] for x in inv}==actual-{'FILE_INVENTORY.jsonl','SHA256SUMS.txt','PAYLOAD_SHA256SUMS.txt'}
for x in inv:
 b=(R/x['path']).read_bytes(); assert (len(b),b.count(b'\n'),sha_bytes(b))==(x['bytes'],x['lines'],x['sha256'])
seals={'files':len(files),'bytes':sum(p.stat().st_size for p in files),'lf':sum(p.read_bytes().count(b'\n') for p in files),
 'root':sha_file(R/'SHA256SUMS.txt'),'payload':sha_file(R/'PAYLOAD_SHA256SUMS.txt'),'inventory':sha_file(R/'FILE_INVENTORY.jsonl'),
 'report':sha_file(R/'REPORT.md'),'result':sha_file(R/'RESULT.json')}
assert seals=={'files':1589,'bytes':336522684,'lf':4592093,'root':'d992087072835e2651834aceb3012f8afd20442b2886673b45254e95e861a361','payload':'9cf210a8dd392a57700a61b640ced0deda5d212173f88293083759f67cb77121','inventory':'f472a22f81197aa78d401caa77e85011549898491fbc3f174cd1bc562b62939b','report':'e0c3ff15d41f9d3c494a501bafd78b5a1c1a3b5d072061b7b7bcefd073ebc4fe','result':'cb395187a01c30f560e94f1310044a5a248cd67d44d65cd252fe2552fbba6434'}
print('R97_CLEANROOM_MANIFEST_PASS',json.dumps(seals,sort_keys=True),flush=True)

# Exact live and inherited bindings.
live={'scheduler':sha_file(REPO/'operations/circdist/SCHEDULER.yaml'),'node':sha_file(REPO/'circdist/proof-dag/nodes/CIRCDIST.gross.yaml'),'review95':sha_file(REPO/'circdist/reviews/circdist_gross_proof_outer_round94_exact_review_round95_20260830.md')}
assert live=={'scheduler':'c09e15bfef6b0c58e6fd8c024603d38e3323ee00bebcbc5ee8f8dcf273c83556','node':'f84492190a1dad3b5d69bf38a9a62d3212f0c3844ee3338dc96517fbb0671135','review95':'b6a23911b5f9974454a4f4291eaa09e30308547925aa71972d5199e3715c9450'}
# Snapshot hashes; scheduler is deliberately its historical package input.
assert sha_file(R/'bindings/operations__circdist__SCHEDULER.yaml')=='3c8965b3cc30f6ebcdc5f051073f2c0eb0dc39d537cd9f3f171633d6eac7bab1'
assert sha_file(R/'bindings/circdist__proof-dag__nodes__CIRCDIST.gross.yaml')==live['node']
assert sha_file(R/'bindings/circdist__reviews__circdist_gross_proof_outer_round94_exact_review_round95_20260830.md')==live['review95']
# Reviewed Round94 manifests and inherited iteration-148 bytes.
assert sha_file(R94/'SHA256SUMS.txt')=='1e0a4af8591aa63ccccd1b2516c630eccb11a73fb9dea2e0ff1e0d32ed82ac1c'
assert sha_file(R94/'PAYLOAD_SHA256SUMS.txt')=='c39ef3552e461dd7513812b8296901e72369dfacbf6e71ae758b5bb58ed94c54'
for a,b in [(R/'state/iter148_state.json',R94/'state/iter148_state.json')]+[(R/f'formulas/iter148/{n}',R94/f'formulas/iter148/{n}') for n in ('source.json.gz','outer.cnf.gz','assertion_map.jsonl.gz','circuit_trace.json.gz','metadata.json','encoding_check.json')]: assert a.read_bytes()==b.read_bytes()
state148=load(R/'state/iter148_state.json')
assert state148['next_iteration']==148 and state148['started'] is False and state148['stop'] is None and state148['selector_count']==len(state148['selectors'])==256
state_keys=('mechanism_id','sector','selected_names','data_support','group_kinds','selector_semantic_sha256')
assert objsha([{k:s.get(k) for k in state_keys} for s in state148['selectors']])==state148['selector_state_sha256']=='9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f'
assert sha_file(R/'state/iter148_state.json')=='1902599acc47eb5d354692759b2d09d6ff1cfcd5e013f2b907cc310376ee6e81'
# Round94 contains only formula artifacts for its then-fresh iteration 148.
iter148paths=[p.relative_to(R94).as_posix() for p in R94.rglob('*') if p.is_file() and 'iter148' in p.as_posix()]
assert sorted(iter148paths)==sorted([f'formulas/iter148/{x}' for x in ['assertion_map.jsonl.gz','circuit_trace.json.gz','encoding_check.json','metadata.json','outer.cnf.gz','source.json.gz']]+['logs/process/iter148_pending_compile.json','logs/process/iter148_pending_encoding_check.json','logs/stderr/iter148_pending_compile.log','logs/stderr/iter148_pending_encoding_check.log','logs/stdout/iter148_pending_compile.log','logs/stdout/iter148_pending_encoding_check.log','logs/wrapper/iter148_pending_compile.stderr.log','logs/wrapper/iter148_pending_compile.stdout.log','logs/wrapper/iter148_pending_encoding_check.stderr.log','logs/wrapper/iter148_pending_encoding_check.stdout.log','state/iter148_state.json'])
print('R97_CLEANROOM_BINDINGS_PASS',json.dumps(live,sort_keys=True),flush=True)

# GF(2) and frozen schedule/direct model, derived only from semantic source JSON.
def rref(rows,n=144):
 rows=[int(x) for x in rows if x]; piv=[]; r=0
 for c in range(n-1,-1,-1):
  p=next((k for k in range(r,len(rows)) if (rows[k]>>c)&1),None)
  if p is None: continue
  rows[r],rows[p]=rows[p],rows[r]
  for k in range(len(rows)):
   if k!=r and ((rows[k]>>c)&1): rows[k]^=rows[r]
  piv.append(c);r+=1
  if r==len(rows):break
 return rows[:r],piv
def inspan(v,rows,n=144):
 rr,piv=rref(rows,n)
 for w,c in zip(rr,piv):
  if (v>>c)&1:v^=w
 return v==0

class Sector:
 RES=((0,1),(3,4,5),(4,5)); PHYS=((2,3,4,5),(3,4,5),(4,5))
 def __init__(self,source,label,times):
  self.label=label;self.times=times; d=source['sector_definitions'][label]
  self.checks=d['checks'];self.kind=d['edge_kind']; self.detrows=[int(x) for x in d['detector_rows']];self.logical=[int(x) for x in d['logical_duals']]
  other=source['z_checks'] if label=='Xerr' else source['x_checks']; self.stabilizers=[mask(x) for x in (source['x_checks'] if label=='Xerr' else source['z_checks'])]
  self.det_of=[[] for _ in range(144)]
  for b,row in enumerate(other):
   for q in row:self.det_of[q].append(b)
  self.dkind='Z' if label=='Xerr' else 'X'
  self.orders=[sorted(row,key=lambda q,a=a:times[f'{self.kind}:{a}:{q}']) for a,row in enumerate(self.checks)]
  self.qorders=[sorted(self.det_of[q],key=lambda b,q=q:times[f'{self.dkind}:{b}:{q}']) for q in range(144)]
  self.columns=[]
  for q in range(144):
   s=1<<q; u=[0];v=0
   for b in reversed(self.qorders[q]):v|=1<<b;u.append(v)
   self.columns.append(self.col(len(self.columns),f'D:{q}',s,s,tuple(u),'data',None,None))
  for a,o in enumerate(self.orders):
   for k,pos in enumerate(self.RES):
    rep=mask(o[p] for p in pos);phys=mask(o[p] for p in self.PHYS[k]);u=0
    for q in bits(phys):
     for b in self.det_of[q]:
      if times[f'{self.dkind}:{b}:{q}']>times[f'{self.kind}:{a}:{q}']:u^=1<<b
    assert self.syndrome(rep)==self.syndrome(phys)
    self.columns.append(self.col(len(self.columns),f'R:{a}:{k}',rep,phys,(u,),'residual',a,k))
  assert len(self.columns)==360 and len({c['support'] for c in self.columns[144:]})==216
  self.byname={c['name']:c for c in self.columns}
 def syndrome(self,s):return sum((parity(s&r)<<i) for i,r in enumerate(self.detrows))
 def col(self,index,name,support,physical,u,kind,check,k): return {'index':index,'name':name,'support':support,'physical':physical,'syndrome':self.syndrome(support),'u':u,'kind':kind,'check':check,'k':k}
 def verify_names(self,names,W=10):
  if len(names)!=len(set(names)) or any(x not in self.byname for x in names):return {'ok':False}
  sel=[self.byname[x]['index'] for x in names];net=0
  for j in sel:net^=self.columns[j]['support']
  syn=self.syndrome(net); pars=[parity(net&x) for x in self.logical]; non=not inspan(net,self.stabilizers)
  return {'ok':len(sel)<=W and syn==0 and non,'weight':len(sel),'selected':sel,'selected_names':names,'net_support':bits(net),'net_weight':bin(net).count("1"),'syndrome':bits(syn),'nontrivial':non,'logical_parities':pars}
 def atoms(self,selected):
  out=set()
  for j in selected:
   c=self.columns[j]
   if c['kind']=='data':continue
   o=self.orders[c['check']]; S=set(bits(c['support']));O=set(o)-S
   if c['k']==0:
    for q in sorted(S):
     for r in sorted(O):out.add((f'{self.kind}:{c["check"]}:{q}','<',f'{self.kind}:{c["check"]}:{r}'))
   else:
    for q in sorted(O):
     for r in sorted(S):out.add((f'{self.kind}:{c["check"]}:{q}','<',f'{self.kind}:{c["check"]}:{r}'))
  assert out
  return [list(x) for x in sorted(out)]

def schedule_audit(source,times):
 edges=set(source['edges']);errors=[]
 if set(times)!=edges:errors.append({'edge_set_mismatch':{'missing':sorted(edges-set(times))[:10],'extra':sorted(set(times)-edges)[:10]}})
 if any(type(x) is not int or x<0 for x in times.values()):errors.append('times_not_nonnegative_integers')
 conflicts=[]; seen={}
 for e,t in times.items():
  kind,a,q=e.split(':');nodes=((kind,int(a)),('D',int(q)))
  for node in nodes:
   z=(node,t)
   if z in seen:conflicts.append([seen[z],e,t])
   seen[z]=e
 used=sorted(set(times.values()))
 if used!=list(range(len(used))):errors.append({'idle_compression':{'used_min':min(used) if used else None,'used_max':max(used) if used else None,'used_count':len(used)}})
 mc=[];pair=whole=0
 for o in source['overlaps']:
  a=o['x_check'];b=o['z_check'];sh=o['qubits'];vals=[times[f'Z:{b}:{q}']<times[f'X:{a}:{q}'] for q in sh]
  if vals[0]!=vals[1]:mc.append([a,b,sh,vals])
  xt=[times[f'X:{a}:{q}'] for q in sh];zt=[times[f'Z:{b}:{q}'] for q in sh]
  if not(max(xt)<min(zt) or max(zt)<min(xt)):pair+=1
  xt=[times[f'X:{a}:{q}'] for q in source['x_checks'][a]];zt=[times[f'Z:{b}:{q}'] for q in source['z_checks'][b]]
  if not(max(xt)<min(zt) or max(zt)<min(xt)):whole+=1
 xs=[times[e] for e in edges if e.startswith('X:')];zs=[times[e] for e in edges if e.startswith('Z:')]
 return {'ok':not errors and not conflicts and not mc,'errors':errors,'edge_count':len(times),'conflicts':conflicts,'used_layers':len(used),'min_time':min(used),'max_time':max(used),'mc_violations':mc,'overlaps':len(source['overlaps']),'global_interleaved':not(max(xs)<min(zs) or max(zs)<min(xs)),'overlap_interleaved_pairs':pair,'whole_check_interleaved_pairs':whole}

# Independent trace/CNF/source checker.
def check_formula(i):
 F=R/f'formulas/iter{i}';source=load(F/'source.json.gz');m=load(F/'metadata.json');tr=load(F/'circuit_trace.json.gz');rows=load_jsonl(F/'assertion_map.jsonl.gz')
 given=source['semantic_payload_sha256'];tmp=dict(source);tmp.pop('semantic_payload_sha256');assert objsha(tmp)==given
 assert m['source_semantic_payload_sha256']==given and m['source_file_sha256']==sha_file(F/'source.json.gz')
 cnfb=raw(F/'outer.cnf.gz'); assert sha_bytes(cnfb)==m['cnf_sha256']; nv,nc,clauses=parse_dimacs_bytes(cnfb,True);assert (nv,nc)==(m['variables'],m['clauses'])
 assert sha_bytes(raw(F/'assertion_map.jsonl.gz'))==m['assertion_map_sha256'] and sha_file(F/'circuit_trace.json.gz')==m['definitions_sha256']
 assert len(rows)==m['assertions']==source['expected']['assertions'] and [x['assertion_index'] for x in rows]==list(range(len(rows)))
 T=tr['constant_variable'];defs=tr['definitions'];assert T==1 and [x['var'] for x in defs]==sorted(x['var'] for x in defs) and len({x['var'] for x in defs})==len(defs)
 used=set(); opcounts=Counter(); defvars=set()
 for d in defs:
  v=d['var'];ids=d['clause_ids'];op=d['op'];inp=d['inputs'];defvars.add(v);opcounts[op]+=len(ids)
  assert not (used&set(ids));used.update(ids)
  got=[clauses[x-1] for x in ids]
  if op=='constant_true':exp=[(v,)]
  elif op=='and':a,b=inp;exp=[(-v,a),(-v,b),(v,-a,-b)]
  elif op=='or':a,b=inp;exp=[(v,-a),(v,-b),(-v,a,b)]
  elif op=='xor':a,b=inp;exp=[(-a,-b,-v),(a,b,-v),(a,-b,v),(-a,b,v)]
  elif op=='rank_membership':
   pos=set(d['positions']);exp=[]
   for mk in range(32):
    mismatch=tuple((-x if (mk>>j)&1 else x) for j,x in enumerate(inp));exp.append(mismatch+((v if bin(mk).count("1") in pos else -v),))
  else:raise AssertionError(op)
  assert got==exp,(i,v,op)
 rootids=set()
 for row in rows:
  ids=row['root_clause_ids'];assert row['root_clauses']==[list(clauses[x-1]) for x in ids];assert not(rootids&set(ids));rootids.update(ids)
 assert not used&rootids and used|rootids==set(range(1,nc+1))
 primary={x for vs in m['time_bit_variables'].values() for x in vs}|{x for vs in m['extrema_bit_variables'].values() for x in vs}
 assert primary|defvars==set(range(1,nv+1)) and not primary&defvars
 # Trace maps and exact roots from source.
 lt={(a,b):v for a,b,v in tr['lt_relations']};eq={tuple(sorted((a,b))):v for a,b,v in tr['eq_relations']};mem={(s,c,tuple(p),q):v for s,c,p,q,v in tr['member_relations']}
 assert len(lt)==len(tr['lt_relations'])==m['comparison_count'];assert len(eq)==len(tr['eq_relations'])==m['word_equality_count'];assert len(mem)==len(tr['member_relations'])==m['membership_expressions']
 ri=0
 def take(fam,sid,css):
  nonlocal ri
  z=rows[ri];ri+=1;assert (z['family'],z['source_id'],z['root_clauses'])==(fam,sid,css)
 for e in source['edges']:
  take('time_nonnegative',e,[]);take('time_upper_bound',e,[[lt['time:'+e,'constant:864']]])
 def distinct(fam,sid,es):
  css=[]
  for a in range(6):
   for b in range(a+1,6):css.append([lt['time:'+es[a],'time:'+es[b]],lt['time:'+es[b],'time:'+es[a]]])
  take(fam,sid,css)
 for a,row in enumerate(source['x_checks']):distinct('x_ancilla_distinct',f'Xcheck:{a}',[f'X:{a}:{q}' for q in row])
 for a,row in enumerate(source['z_checks']):distinct('z_ancilla_distinct',f'Zcheck:{a}',[f'Z:{a}:{q}' for q in row])
 for q,row in enumerate(source['data_incidence']):distinct('data_distinct',f'data:{q}',row)
 for o in source['overlaps']:
  a=o['x_check'];b=o['z_check'];q0,q1=o['qubits'];l0=lt['time:'+f'Z:{b}:{q0}','time:'+f'X:{a}:{q0}'];l1=lt['time:'+f'Z:{b}:{q1}','time:'+f'X:{a}:{q1}'];take('mc_equivalence',f'overlap:{a}:{b}',[[-l0,l1],[l0,-l1]])
 xs=[e for e in source['edges'] if e.startswith('X:')];zs=[e for e in source['edges'] if e.startswith('Z:')]
 for label,es,mode in [('xmin',xs,'min'),('xmax',xs,'max'),('zmin',zs,'min'),('zmax',zs,'max')]:
  for e in es:
   lit=-lt['time:'+e,'extrema:'+label] if mode=='min' else -lt['extrema:'+label,'time:'+e];take('extrema_inequality',f'{label}:{e}',[[lit]])
  take('extrema_attained',label,[[eq[tuple(sorted(('extrema:'+label,'time:'+e)))] for e in es]])
 take('global_interleaving','not_all_X_before_Z',[[-lt['extrema:xmax','extrema:zmin']]])
 take('global_interleaving','not_all_Z_before_X',[[-lt['extrema:zmax','extrema:xmin']]])
 bc=Counter()
 for b in source['blocks']:
  bc[b['family']]+=1;take('reviewed_block',b['source_id'],[[-lt['time:'+x,'time:'+y] for x,y in b['atoms']]])
 assert dict(bc)==source['expected']['block_family_counts']==m['block_family_counts']
 # Reconstruct selector circuit from gate relations.
 gate={}
 for d in defs:
  if d['op'] in ('and','or','xor'):gate[(d['op'],tuple(sorted(d['inputs'])))]=d['var']
 def and2(a,b):
  if a==T:return b
  if b==T:return a
  if a==-T or b==-T:return -T
  if a==b:return a
  if a==-b:return -T
  return gate['and',tuple(sorted((a,b)))]
 def or2(a,b):
  if a==-T:return b
  if b==-T:return a
  if a==T or b==T:return T
  if a==b:return a
  if a==-b:return T
  return gate['or',tuple(sorted((a,b)))]
 def xor2(a,b):
  if a==-T:return b
  if b==-T:return a
  if a==T:return -b
  if b==T:return -a
  if a==b:return -T
  if a==-b:return T
  return gate['xor',tuple(sorted((a,b)))]
 def many(fn,vals,start):
  r=start
  for x in vals:r=fn(r,x)
  return r
 res=[set(x) for x in source['residual_positions']]
 domains=set();sourcekeys=set()
 for si,s in enumerate(source['selectors']):
  sd=source['sector_definitions'][s['sector']];qs=[int(x) for x in sd['qubit_signatures']];ds=0
  for q in s['data_support']:ds^=qs[q]
  terms=[[] for _ in range(84)]
  for cs,kinds in sorted(s['group_kinds'].items(),key=lambda x:int(x[0])):
   p=set()
   for k in kinds:p.symmetric_difference_update(res[int(k)])
   pos=tuple(sorted(p));c=int(cs);domains.add((s['sector'],c,pos))
   for q in sd['checks'][c]:
    sourcekeys.add((s['sector'],c,pos,q));mv=mem[(s['sector'],c,pos,q)];sig=qs[q]
    for bit in range(84):
     if (sig>>bit)&1:terms[bit].append(mv)
  bv=[many(xor2,terms[k],T if ((ds>>k)&1) else -T) for k in range(84)]
  valid=and2(many(and2,[-x for x in bv[:72]],T),many(or2,bv[72:],-T));assert valid==tr['selector_valid_literals'][si]
  take('efssc_exclusion',s['mechanism_id'],[[-valid]])
 assert ri==len(rows) and sourcekeys==set(mem)
 # Rank truth-table clauses imply exact position membership; independently census domains.
 cases=0
 for sec,c,pos in domains:
  row=source['sector_definitions'][sec]['checks'][c]
  for order in permutations(row):
   rank={q:j for j,q in enumerate(order)}
   for q in row:assert (rank[q] in pos)==(sum(rank[x]<rank[q] for x in row if x!=q) in pos);cases+=1
 assert cases==load(F/'encoding_check.json')['rank_membership_local_order_qubit_cases']
 # Family census from actual partition.
 fam=Counter();fam['constant']=opcounts['constant_true'];fam['def:and']=opcounts['and'];fam['def:or']=opcounts['or'];fam['def:xor']=opcounts['xor'];fam['def:rank_membership']=opcounts['rank_membership']
 rootmap={'time_upper_bound':'root:time_upper_bound','x_ancilla_distinct':'root:distinct','z_ancilla_distinct':'root:distinct','data_distinct':'root:distinct','mc_equivalence':'root:mc','extrema_inequality':'root:extrema_inequality','extrema_attained':'root:extrema_attained','global_interleaving':'root:global_interleaving','efssc_exclusion':'root:efssc'}
 for z in rows:
  if z['family']=='reviewed_block': key='root:block:'+z['block_family']
  else:key=rootmap.get(z['family'])
  if key:fam[key]+=len(z['root_clause_ids'])
 assert dict(fam)==m['clause_family_counts']
 out={'i':i,'selectors':len(source['selectors']),'assertions':len(rows),'vars':nv,'clauses':nc,'cnf':m['cnf_sha256'],'source_file':m['source_file_sha256'],'source_semantic':given,'map':m['assertion_map_sha256'],'trace':m['definitions_sha256'],'definitions':len(defs),'root_clauses':len(rootids),'rank_domains':len(domains),'rank_cases':cases}
 del clauses,defs,tr,rows;gc.collect();return source,m,out

formula=[]; sources={}; metas={}
# Exhaust the generic little-endian comparator recurrence independently once.
cc=0
for x in range(1024):
 xb=[bool((x>>j)&1) for j in range(10)]
 for y in range(1024):
  yb=[bool((y>>j)&1) for j in range(10)];z=False
  for a,b in zip(xb,yb):z=((not a and b) or ((a==b) and z))
  assert z==(x<y);cc+=1
assert cc==1_048_576
for i in range(148,161):
 s,m,o=check_formula(i);sources[i]=s;metas[i]=m;formula.append(o);print('R97_CLEANROOM_FORMULA_PASS',i,o['vars'],o['clauses'],o['cnf'],flush=True)
# Sources have exact selector prefixes and frozen base.
base=sources[148]
for i in range(149,161):
 for k in ('blocks','data_incidence','edges','frozen_semantics','overlaps','residual_positions','sector_definitions','x_checks','z_checks'):assert sources[i][k]==base[k]
 assert sources[i]['selectors'][:len(sources[i-1]['selectors'])]==sources[i-1]['selectors']

# Direct CNF encoder independently recreated.
class Encoder:
 def __init__(self):self.vars=[];self.by={};self.cls=[]
 def var(self,name,role,context):
  if name in self.by:return self.by[name]
  v=len(self.vars)+1;self.by[name]=v;self.vars.append({'id':v,'name':name,'role':role,'context':context});return v
 def add(self,lits,rule,context):self.cls.append({'id':len(self.cls)+1,'lits':list(lits),'rule':rule,'context':context})
 def xorlink(self,a,b,y,c):
  for z in ([-y,a,b],[-y,-a,-b],[y,-a,b],[y,a,-b]):self.add(z,'xor2_equivalence',c)
 def xorvalue(self,lits,prefix,ctx):
  assert lits;acc=lits[0]
  for st,x in enumerate(lits[1:],1):
   y=self.var(f'{prefix}.xor_aux.{st}','xor_auxiliary',{**ctx,'step':st,'left':acc,'right':x});self.xorlink(acc,x,y,{**ctx,'step':st,'output':y});acc=y
  return acc
 def xorconstraint(self,lits,p,pre,ctx):
  if not lits:
   if p:self.add([],'empty_xor_contradiction',ctx)
   return
  a=self.xorvalue(lits,pre,ctx);self.add([a if p else -a],'xor_terminal_value',{**ctx,'parity':p})
 def atmost(self,x,k):
  n=len(x);s={}
  for i in range(1,n+1):
   for j in range(1,k+1):s[i,j]=self.var(f'card.s.{i}.{j}','cardinality_auxiliary',{'counter':'prefix_at_least','prefix_length':i,'threshold':j})
  self.add([-s[1,1],x[0]],'card_base_equivalence',{'i':1,'j':1});self.add([s[1,1],-x[0]],'card_base_equivalence',{'i':1,'j':1})
  for j in range(2,k+1):self.add([-s[1,j]],'card_impossible_base',{'i':1,'j':j})
  for i in range(2,n+1):
   xi=x[i-1];y=s[i,1];a=s[i-1,1]
   self.add([-y,a,xi],'card_or_equivalence',{'i':i,'j':1});self.add([-a,y],'card_or_equivalence',{'i':i,'j':1});self.add([-xi,y],'card_or_equivalence',{'i':i,'j':1})
   for j in range(2,k+1):
    y=s[i,j];a=s[i-1,j];b=s[i-1,j-1];c={'i':i,'j':j}
    self.add([-y,a,b],'card_recurrence_equivalence',c);self.add([-y,a,xi],'card_recurrence_equivalence',c);self.add([-a,y],'card_recurrence_equivalence',c);self.add([-b,-xi,y],'card_recurrence_equivalence',c)
   self.add([-s[i-1,k],-xi],'card_atmost_overflow_forbidden',{'i':i,'bound':k})

def direct_expected(sec,candsha):
 E=Encoder();x=[E.var(f'select[{c["index"]}]','direct_column_selection',{'column_index':c['index'],'column_name':c['name']}) for c in sec.columns];assert x==list(range(1,361))
 synrows=[]
 for b in range(72):
  lits=[x[c['index']] for c in sec.columns if (c['syndrome']>>b)&1];synrows.append({'row':b,'literals':lits,'column_indices':[v-1 for v in lits]});E.xorconstraint(lits,0,f'syndrome[{b}]',{'family':'detector_syndrome','row':b})
 logrows=[];lvars=[]
 for r,l in enumerate(sec.logical):
  lits=[x[c['index']] for c in sec.columns if parity(c['support']&l)];lv=E.var(f'logical_parity[{r}]','logical_parity_output',{'logical_dual_index':r,'logical_dual_support':bits(l)});acc=E.xorvalue(lits,f'logical[{r}]',{'family':'logical_parity','logical_dual_index':r});E.add([-lv,acc],'logical_output_equivalence',{'logical_dual_index':r});E.add([lv,-acc],'logical_output_equivalence',{'logical_dual_index':r});lvars.append(lv);logrows.append({'row':r,'logical_dual_support':bits(l),'logical_dual_mask_hex':hex(l),'literals':lits,'column_indices':[v-1 for v in lits],'output_var':lv})
 E.add(lvars,'logical_nonzero_disjunction',{'logical_outputs':lvars});E.atmost(x,10)
 lines=[f'c CIRCDIST Gross direct-360 {sec.label} W<=10',f'c candidate_sha256 {candsha}','c variables 1..360 select the exact columns listed in the companion column dictionary',f'p cnf {len(E.vars)} {len(E.cls)}']+[' '.join(map(str,c['lits']))+' 0' for c in E.cls];dimacs=('\n'.join(lines)+'\n').encode();body=''.join(' '.join(map(str,c['lits']))+' 0\n' for c in E.cls).encode()
 return E,dimacs,synrows,logrows,sha_bytes(body)

def columns_public(sec,candsha,synrows,logrows):
 cols=[]
 for c in sec.columns:
  cols.append({'index':c['index'],'primary_var':c['index']+1,'name':c['name'],'kind':c['kind'],'check':c['check'],'residual_kind':c['k'],'support':bits(c['support']),'support_mask_hex':hex(c['support']),'physical_support':bits(c['physical']),'syndrome':bits(c['syndrome']),'syndrome_mask_hex':hex(c['syndrome']),'u_options':[{'bits':bits(u),'mask_hex':hex(u)} for u in c['u']]})
 return {'schema':'circdist-gross-direct360-column-dictionary-v1','sector':sec.label,'candidate_sha256':candsha,'column_count':360,'columns':cols,'detector_rows':[{'row':i,'support':bits(v),'mask_hex':hex(v)} for i,v in enumerate(sec.detrows)],'stabilizer_rows':[{'row':i,'support':bits(v),'mask_hex':hex(v)} for i,v in enumerate(sec.stabilizers)],'logical_duals':[{'row':i,'support':bits(v),'mask_hex':hex(v)} for i,v in enumerate(sec.logical)],'syndrome_equations':synrows,'logical_equations':logrows}

outer=[];direct=[];schedules=set();states={148:state148};new_selectors={}
for i in range(148,160):
 I=R/f'iterations/iter{i}';src=sources[i];meta=metas[i];cand=load(I/'outer/candidate.json');replay=load(I/'outer/replay.json')
 cnfb=raw(R/f'formulas/iter{i}/outer.cnf.gz');nv,nc,clauses=parse_dimacs_bytes(cnfb,True)
 a1,v1,st1=assignment_map(raw(I/'outer/assignment.dimacs.gz'),nv);a2,v2,st2=assignment_map(raw(I/'outer/assignment.independent.dimacs.gz'),nv);assert a1==a2 and st1=='SATISFIABLE' and st2 is None
 assert not check_clauses(clauses,a1) and replay['dimacs_clauses_checked']==nc and replay['complete_assignment_variables']==nv
 times={e:sum((1<<b) for b,var in enumerate(meta['time_bit_variables'][e]) if a1[var]) for e in src['edges']};assert times==cand['raw_times']
 ext={k:sum((1<<b) for b,var in enumerate(meta['extrema_bit_variables'][k]) if a1[var]) for k in meta['extrema_bit_variables']};assert ext==cand['raw_extrema']
 rankmap={t:j for j,t in enumerate(sorted(set(times.values())))};comp={e:rankmap[t] for e,t in times.items()};assert comp==cand['compressed_times'];assert objsha(times)==cand['raw_schedule_sha256'];assert objsha(comp)==cand['compressed_schedule_sha256'];assert len(rankmap)==cand['raw_used_layers']==cand['compressed_layers']
 aud=schedule_audit(src,comp);assert aud==cand['frozen_audit'] and aud['ok'] and aud['global_interleaved']
 assert all(not all(comp[x]<comp[y] for x,y in b['atoms']) for b in src['blocks'])
 secs={s:Sector(src,s,comp) for s in ('Xerr','Zerr')};valid=[s['mechanism_id'] for s in src['selectors'] if secs[s['sector']].verify_names(s['selected_names'])['ok']];assert not valid
 assert cand['compressed_schedule_sha256'] not in schedules;schedules.add(cand['compressed_schedule_sha256'])
 outer.append({'i':i,'vars':nv,'clauses':nc,'cnf':meta['cnf_sha256'],'schedule':cand['compressed_schedule_sha256'],'raw_layers':len(rankmap),'prior_valid':len(valid)})
 del clauses,a1,a2;gc.collect()
 dv=load(I/'direct/direct_verification.json');assert dv['schedule_audit']==aud and dv['candidate_sha256']==cand['compressed_schedule_sha256'] and dv['repair_gate']['entered'] is False
 constructed=[]
 for label in ('Xerr','Zerr'):
  sec=secs[label];D=I/'direct/direct360';E,dimacs,synrows,logrows,bodysha=direct_expected(sec,cand['compressed_schedule_sha256']);stored=raw(D/f'{label}.cnf.gz');assert stored==dimacs
  assert load_jsonl(D/f'{label}.clauses.jsonl.gz')==E.cls
  vard=load(D/f'{label}.variables.json.gz');assert vard=={'schema':'circdist-gross-direct360-variable-dictionary-v1','sector':label,'candidate_sha256':cand['compressed_schedule_sha256'],'variable_count':len(E.vars),'variables':E.vars}
  assert load(D/f'{label}.columns.json.gz')==columns_public(sec,cand['compressed_schedule_sha256'],synrows,logrows)
  summ=load(D/f'{label}.summary.json');assert summ['dimacs_sha256']==sha_bytes(dimacs) and summ['formula_body_sha256']==bodysha and summ['variables']==len(E.vars) and summ['clauses']==len(E.cls) and summ['complete_query'] is True and summ['excluded_restrictions']==['no pool restriction','no residual-pattern restriction','no check-count restriction','no within-check order family restriction']
  aa,vv,st=assignment_map(raw(I/f'direct/solver/{label}.assignment.dimacs'),len(E.vars));assert st is None and not check_clauses([tuple(x['lits']) for x in E.cls],aa)
  sel=[j for j in range(360) if aa[j+1]];mech=dv['sectors'][label]['mechanism'];names=[sec.columns[j]['name'] for j in sel];ev=sec.verify_names(names);assert ev['ok'] and ev['weight']==len(sel) and ev==mech['canonical_replay']
  can=phys=0
  faults=[]
  for j in sel:
   c=sec.columns[j];can^=c['support'];phys^=c['physical']
   if c['kind']=='data':faults.append({'column_index':j,'column_name':c['name'],'elementary_fault':'data_singleton','data_support':[int(c['name'].split(':')[1])],'schedule_dependency':'none'})
   else:
    o=sec.orders[c['check']];edges=[f'{sec.kind}:{c["check"]}:{q}' for q in o];faults.append({'column_index':j,'column_name':c['name'],'elementary_fault':'ancilla_hook_suffix','check':c['check'],'residual_kind':c['k'],'canonical_representative_support':bits(c['support']),'physical_suffix_positions_zero_based':list(Sector.PHYS[c['k']]),'physical_suffix_support':bits(c['physical']),'within_check_order_qubits':o,'within_check_order_edges':edges,'within_check_times':[comp[e] for e in edges]})
  ps=sec.syndrome(phys);pp=[parity(phys&l) for l in sec.logical];cp=[parity(can&l) for l in sec.logical];assert ps==0 and not inspan(phys,sec.stabilizers) and pp==cp and any(pp)
  atoms=sec.atoms(sel);assert all(comp[a]<comp[b] for a,op,b in atoms)
  assert mech['fault_count']==len(sel) and mech['selected_indices']==sel and mech['selected_names']==names and mech['physical_net_support']==bits(phys) and mech['physical_net_weight']==bin(phys).count("1") and mech['physical_syndrome']==[] and mech['physical_nontrivial'] is True and mech['physical_logical_parities']==pp and mech['canonical_physical_parities_equal'] is True and mech['faults']==faults and mech['sound_outer_block']['atoms']==atoms and mech['sound_outer_block']['atom_count']==len(atoms)
  # Complete formula negative witnesses: one selected primary flip violates clauses; removing first loses zero syndrome.
  af=list(aa);af[sel[0]+1]=False;assert check_clauses([tuple(x['lits']) for x in E.cls],af);assert not sec.verify_names(names[1:])['ok']
  data=sorted(int(n.split(':')[1]) for n in names if n.startswith('D:'));groups=defaultdict(list)
  for n in names:
   if n.startswith('R:'):_,c,k=n.split(':');groups[c].append(int(k))
  groups={k:sorted(v) for k,v in sorted(groups.items(),key=lambda z:int(z[0]))}
  sem={'sector':label,'selected_names':names,'data_support':data,'group_kinds':groups};selhash=objsha(sem)
  ns={'mechanism_id':f'r96-i{i}-{label}','source_iteration':i,'sector':label,'fault_count':len(sel),'selected_names':names,'data_support':data,'group_kinds':groups,'source_schedule_sha256':cand['compressed_schedule_sha256'],'source_times':comp,'canonical_support':bits(can),'physical_support':bits(phys),'source_atoms':atoms,'source_atom_count':len(atoms),'origin':f'round96_proof_outer_iteration{i}_direct360','source_symbolic_validity':'True','selector_semantic_sha256':selhash}
  constructed.append(ns)
  direct.append({'i':i,'sector':label,'vars':len(E.vars),'clauses':len(E.cls),'formula':sha_bytes(dimacs),'weight':len(sel),'names':names,'canonical_weight':bin(can).count("1"),'physical_weight':bin(phys).count("1"),'syndrome':[],'logical':pp,'selector':selhash})
 assert [x['mechanism_id'] for x in constructed]==[f'r96-i{i}-Xerr',f'r96-i{i}-Zerr'];new_selectors[i]=constructed
 # Exact state transition and source compact append.
 prev=states[i];nxt=load(R/f'state/iter{i+1}_state.json');states[i+1]=nxt
 assert nxt['selectors']==prev['selectors']+constructed and nxt['selector_count']==len(nxt['selectors'])==prev['selector_count']+2 and nxt['next_iteration']==i+1 and nxt['started'] is False and nxt['stop'] is None
 sh=objsha([{k:s.get(k) for k in state_keys} for s in nxt['selectors']]);assert sh==nxt['selector_state_sha256'] and len({s['selector_semantic_sha256'] for s in nxt['selectors']})==len(nxt['selectors'])
 compact_keys=('mechanism_id','source_iteration','sector','fault_count','selected_names','data_support','group_kinds','source_schedule_sha256','origin','selector_semantic_sha256')
 assert sources[i+1]['selectors']==sources[i]['selectors']+[{k:s[k] for k in compact_keys} for s in constructed]
 rec=load(I/'record.json');assert rec['new_selectors']==[x['mechanism_id'] for x in constructed] and rec['state_after_sha256']==sh and rec['source_selector_state_sha256']==prev['selector_state_sha256'] and rec['state_mutated_atomically'] is True and rec['repair_entered'] is False
 payload={'cnf_sha256':metas[i+1]['cnf_sha256'],'new_selector_ids':[x['mechanism_id'] for x in constructed],'record_file_sha256':sha_file(I/'record.json'),'selector_count':nxt['selector_count'],'selector_state_sha256':sh,'source_file_sha256':sha_file(R/f'formulas/iter{i+1}/source.json.gz'),'source_semantic_sha256':sources[i+1]['semantic_payload_sha256'],'state_file_sha256':sha_file(R/f'state/iter{i+1}_state.json')}
 pend=load(R/f'transitions/iter{i}_to{i+1}/pending_intent.json');com=load(R/f'transitions/iter{i}_to{i+1}/atomic_commit.json');assert pend['payload']==com['payload']==payload and pend['status']=='PENDING' and com['status']=='COMMITTED' and pend['state_promoted_last'] is True and com['state_promoted_last'] is True and com['all_outputs_present'] is True
 print('R97_CLEANROOM_ITERATION_PASS',i,'outer',nv,nc,'direct',[(x['sector'],x['weight']) for x in direct[-2:]],flush=True)

# Fresh iteration160 is genuinely unstarted/unsolved.
s160=states[160];assert sha_file(R/'state/iter160_state.json')=='bb26ce4fc03ae9616a6a325438c3f4c82568a15c4fe133e074959b894e358194' and s160['selector_count']==280 and s160['selector_state_sha256']=='ad3cf364dd9224c14ffb55046ba3dc8eb80035b1eaf997f1d7a5691297ad62a3' and s160['next_iteration']==160 and s160['started'] is False and s160['stop'] is None
assert not (R/'iterations/iter160').exists() and not any(R.glob('transitions/iter160*'))
for term in ('solver','model','proof','assignment','status','disposition'):
 assert not any(term in p.name.lower() for p in (R/'formulas/iter160').iterdir())
iter160paths=sorted(p.relative_to(R).as_posix() for p in R.rglob('*') if p.is_file() and 'iter160' in p.as_posix())
assert iter160paths==sorted([f'formulas/iter160/{x}' for x in ('assertion_map.jsonl.gz','circuit_trace.json.gz','encoding_check.json','metadata.json','outer.cnf.gz','source.json.gz')]+['logs/process/iter160_pending_compile.json','logs/process/iter160_pending_encoding_check.json','logs/stderr/iter160_pending_compile.log','logs/stderr/iter160_pending_encoding_check.log','logs/stdout/iter160_pending_compile.log','logs/stdout/iter160_pending_encoding_check.log','logs/wrapper/iter160_pending_compile.stderr.log','logs/wrapper/iter160_pending_compile.stdout.log','logs/wrapper/iter160_pending_encoding_check.stderr.log','logs/wrapper/iter160_pending_encoding_check.stdout.log','state/iter160_state.json'])
assert formula[-1]['source_file']=='8b754b649744a83eae6c80e64230f9782909b48e5613dcfd6c3c321d98b2dd66' and formula[-1]['source_semantic']=='bb19e724c66eb6f3df8830a205ba29a297f5795d42d3fe066fa3b873800789ed' and formula[-1]['cnf']=='aa18d2857ed5a7aefacd33bf4fbd42fded914393e123a87f00e84e4920e39d59' and (formula[-1]['assertions'],formula[-1]['vars'],formula[-1]['clauses'])==(19162,411526,1396722)

# Exact same-sector order-4 enumeration, independent implementation.
synth_state=load(R/'synthesis/inputs/iter137_state.json')
assert sha_file(R/'synthesis/inputs/iter137_state.json')=='ba670045a69722f9625d04d3f07d62e207db38f15e9323f8c32d89194bb585cd'
assert (R/'synthesis/inputs/iter137_state.json').read_bytes()==(R94/'state/iter137_state.json').read_bytes()
assert synth_state['next_iteration']==137 and synth_state['started'] is False and synth_state['stop'] is None
assert synth_state['selector_count']==len(synth_state['selectors'])==234
assert objsha([{k:x.get(k) for k in state_keys} for x in synth_state['selectors']])==synth_state['selector_state_sha256']=='47792a8f8e757482604723abb0e08916f49b252f4ba07deae03cf4295159d0b6'
synth_cand=load(R/'synthesis/inputs/iter136_candidate.json')
synth_direct=load(R/'synthesis/inputs/iter136_direct_verification.json')
assert sha_file(R/'synthesis/inputs/iter136_candidate.json')=='9596d1456ea66c086c06b4b7b4aaf4e442da9943644ae9839d113f10d937a640'
assert sha_file(R/'synthesis/inputs/iter136_direct_verification.json')=='f206cb75b7af6cbf2c5421f58c9ebc0c1c0b51d7e44eb3f1c5713a47987a485e'
assert (R/'synthesis/inputs/iter136_candidate.json').read_bytes()==(R94/'iterations/iter136/outer/candidate.json').read_bytes()
assert (R/'synthesis/inputs/iter136_direct_verification.json').read_bytes()==(R94/'iterations/iter136/direct/direct_verification.json').read_bytes()
synth_source=load(R94/'formulas/iter136/source.json.gz')
for k in ('blocks','data_incidence','edges','frozen_semantics','overlaps','residual_positions','sector_definitions','x_checks','z_checks'):assert synth_source[k]==base[k]
synth_times={k:int(v) for k,v in synth_cand['compressed_times'].items()}
assert objsha(synth_times)==synth_cand['compressed_schedule_sha256']=='45051af0b08e6647d50c6fb0535894173016fd013279e7a0eaee8b2e69ee2e44'
assert schedule_audit(base,synth_times)==synth_cand['frozen_audit'] and synth_cand['frozen_audit']['ok']
synth_sectors={x:Sector(base,x,synth_times) for x in ('Xerr','Zerr')}
name_universe=sorted(synth_sectors['Xerr'].byname)
assert len(name_universe)==360 and set(name_universe)==set(synth_sectors['Zerr'].byname)
name_bit={x:i for i,x in enumerate(name_universe)}
def bitstr(v,n=12):return ''.join(str((v>>i)&1) for i in range(n))
def effect(sec,names):
 can=phys=0
 for name in names:
  c=sec.byname[name];can^=c['support'];phys^=c['physical']
 cs=sec.syndrome(can);ps=sec.syndrome(phys)
 cl=sum(parity(can&d)<<i for i,d in enumerate(sec.logical));pl=sum(parity(phys&d)<<i for i,d in enumerate(sec.logical))
 return can,phys,cs,ps,cl,pl
by={'Xerr':[],'Zerr':[]}
for gi,x in enumerate(synth_state['selectors']):
 sem={k:x.get(k) for k in ('sector','selected_names','data_support','group_kinds')};assert objsha(sem)==x['selector_semantic_sha256']
 assert len(x['selected_names'])==len(set(x['selected_names']))
 nm=sum(1<<name_bit[n] for n in x['selected_names']);ef=effect(synth_sectors[x['sector']],x['selected_names'])
 by[x['sector']].append((gi,x,nm,*ef))
assert {k:len(v) for k,v in by.items()}=={'Xerr':125,'Zerr':109}
expected4={'Xerr':math.comb(125,4),'Zerr':math.comb(109,4)}
assert expected4=={'Xerr':9691375,'Zerr':5563251} and sum(expected4.values())==15254626
stored4=load(R/'synthesis/order4_gf2_closure.json');sector4={};valid_occurrences=[]
for label in ('Xerr','Zerr'):
 rows=by[label];n=len(rows);existing={r[2] for r in rows};seen=0;checksum=0;mod=(1<<256)-1
 wh=Counter();ch=Counter();ph=Counter();lh=Counter();eligible={};left=[]
 zl=zc=zp=cs0=ps0=cl0=pl0=cvn=pvn=con=0
 for c in range(2,n-1):
  b=c-1;rb=rows[b]
  for a in range(b):
   ra=rows[a];left.append((a,b,ra[2]^rb[2],ra[3]^rb[3],ra[4]^rb[4],ra[5]^rb[5],ra[6]^rb[6],ra[7]^rb[7],ra[8]^rb[8]))
  rc=rows[c]
  for d in range(c+1,n):
   rd=rows[d];rn=rc[2]^rd[2];rcan=rc[3]^rd[3];rphys=rc[4]^rd[4];rcs=rc[5]^rd[5];rps=rc[6]^rd[6];rcl=rc[7]^rd[7];rpl=rc[8]^rd[8]
   for a,b,ln,lcan,lphys,lcs,lps,lcl,lpl in left:
    seen+=1;nm=ln^rn;can=lcan^rcan;phys=lphys^rphys;cs=lcs^rcs;ps=lps^rps;cl=lcl^rcl;pl=lpl^rpl
    w=popcount(nm);cw=popcount(can);pw=popcount(phys);wh[w]+=1;ch[cw]+=1;ph[pw]+=1
    zl+=w==0;zc+=can==0;zp+=phys==0;cs0+=cs==0;ps0+=ps==0;cl0+=cl==0;pl0+=pl==0
    cv=1<=w<=10 and cs==0 and cl!=0;pv=1<=w<=10 and ps==0 and pl!=0;good=cv and pv and cl==pl
    cvn+=cv;pvn+=pv;con+=good
    if good:lh[bitstr(cl)]+=1;valid_occurrences.append((label,nm,cl,(a,b,c,d)))
    checksum=(checksum+nm+(can<<1)+(phys<<2)+(a+1)*3+(b+1)*5+(c+1)*7+(d+1)*11)&mod
    if 1<=w<=10:
     z=eligible.get(nm);effects=(can,phys,cs,ps,cl,pl)
     if z is None:eligible[nm]=[1,(a,b,c,d),effects,cv,pv,good]
     else:assert z[2:]==[effects,cv,pv,good];z[0]+=1
 assert seen==expected4[label] and len(left)==math.comb(n-2,2)
 mult=Counter();maxm=0;maxnm=None;inherited=novel=replayed=retained=0;miss=Counter()
 for nm,z in sorted(eligible.items()):
  mult[z[0]]+=1
  if z[0]>maxm:maxm=z[0];maxnm=nm
  names=[name_universe[j] for j in bits(nm)];can,phys,cs,ps,cl,pl=effect(synth_sectors[label],names);assert z[2]==(can,phys,cs,ps,cl,pl)
  rep=synth_sectors[label].verify_names(names);replayed+=1
  assert rep['weight']==len(names) and rep['net_support']==bits(can) and rep['syndrome']==bits(cs) and rep['logical_parities']==[(cl>>j)&1 for j in range(12)] and rep['ok']==z[3]
  if nm in existing:inherited+=1;continue
  novel+=1
  if z[5]:retained+=1
  elif cs:miss['canonical_nonzero_syndrome']+=1
  elif not cl:miss['canonical_logical_trivial']+=1
  elif ps:miss['physical_nonzero_syndrome']+=1
  elif not pl:miss['physical_logical_trivial']+=1
  elif cl!=pl:miss['canonical_physical_logical_mismatch']+=1
  else:miss['other']+=1
 got={'selector_count':n,'unordered_pairs':math.comb(n,2),'unordered_distinct_quadruples_expected':expected4[label],
      'unordered_distinct_quadruples_enumerated':seen,'canonical_left_pairs_final':len(left),
      'all_pair_pair_decompositions':math.comb(math.comb(n,2),2),'overlapping_pair_decompositions_excluded':3*math.comb(n,3),
      'noncanonical_disjoint_pairings_excluded':2*math.comb(n,4),'canonical_disjoint_pairing_retained':math.comb(n,4),
      'location_weight_histogram':dict(sorted(wh.items())),'canonical_support_weight_histogram':dict(sorted(ch.items())),
      'physical_support_weight_histogram':dict(sorted(ph.items())),'zero_location_results':zl,'zero_canonical_support_results':zc,
      'zero_physical_support_results':zp,'canonical_syndrome_zero_results':cs0,'physical_syndrome_zero_results':ps0,
      'canonical_logical_trivial_results':cl0,'physical_logical_trivial_results':pl0,'canonical_source_valid_quadruples':cvn,
      'physical_source_valid_quadruples':pvn,'conservative_source_valid_quadruples':con,
      'conservative_logical_action_histogram':dict(sorted(lh.items())),'eligible_weight_1_to_10_with_multiplicity':sum(wh[w] for w in range(1,11)),
      'unique_eligible_named_results':len(eligible),'unique_eligible_replayed':replayed,'unique_existing_predicate_results':inherited,
      'unique_novel_eligible_results':novel,'unique_novel_conservative_source_valid_retained':retained,'unique_novel_source_valid_counter':retained,
      'novel_miss_reasons':dict(sorted(miss.items())),'multiplicity_histogram_for_unique_eligible_results':dict(sorted(mult.items())),
      'maximum_result_multiplicity':maxm,'maximum_multiplicity_witness_names':[name_universe[j] for j in bits(maxnm)],
      'enumeration_checksum_mod_2_256':f'{checksum:064x}','retained_terms':[]}
 # JSON object keys are strings after serialization; normalize integer-keyed histograms.
 normalized=json.loads(json.dumps(got,sort_keys=True));assert normalized==stored4['sector_results'][label]
 sector4[label]={'domain':seen,'eligible':len(eligible),'inherited':inherited,'novel':novel,'valid_occurrences':con,'retained':retained,'checksum':got['enumeration_checksum_mod_2_256']}
 print('R97_CLEANROOM_ORDER4_SECTOR_PASS',label,json.dumps(sector4[label],sort_keys=True),flush=True)
assert valid_occurrences and len(valid_occurrences)==1
vl,vnm,vlog,vidx=valid_occurrences[0]
assert vl=='Zerr' and bitstr(vlog)=='100110100011' and vnm in {r[2] for r in by['Zerr']}
valid_inherited_ids=[r[1]['mechanism_id'] for r in by['Zerr'] if r[2]==vnm]
assert len(valid_inherited_ids)==1
assert sector4['Xerr']=={'domain':9691375,'eligible':32456,'inherited':0,'novel':32456,'valid_occurrences':0,'retained':0,'checksum':'7995964f26ce16be693f5c459427c10855bd904cade6bd8279b47c2a75f7576c'}
assert sector4['Zerr']=={'domain':5563251,'eligible':1304,'inherited':106,'novel':1198,'valid_occurrences':1,'retained':0,'checksum':'a7b44ab8479c13e64304bb8e4a023e9b17c38b570eabcdf8f3ebdff284c3862e'}
assert stored4['finite_domain']['unordered_distinct_quadruples_enumerated']==15254626 and stored4['retained_term_count']==0 and stored4['retained_terms']==[]
# Independently replay the three scope controls recorded with the census.
cross=stored4['audits']['cross_sector_ambiguity'];names=cross['selected_names'];xe=effect(synth_sectors['Xerr'],names);ze=effect(synth_sectors['Zerr'],names)
def public_effect(e):
 can,phys,cs,ps,cl,pl=e;return {'canonical_support':bits(can),'physical_support':bits(phys),'syndrome':bits(cs),'physical_syndrome':bits(ps),'logical':bitstr(cl),'physical_logical':bitstr(pl)}
assert public_effect(xe)==cross['Xerr'] and public_effect(ze)==cross['Zerr'] and xe!=ze
glob=stored4['audits']['schedule_globalization'];ss=next(x for x in synth_state['selectors'] if x['mechanism_id']==glob['selector_id'])
source_v=Sector(base,ss['sector'],ss['source_times']).verify_names(ss['selected_names']);current_v=synth_sectors[ss['sector']].verify_names(ss['selected_names'])
assert source_v==glob['source_verification'] and current_v==glob['iteration136_verification'] and source_v['ok'] and not current_v['ok']
ww=stored4['audits']['support_weight_substitution'];wm=synth_direct['sectors'][ww['sector']]['mechanism']
assert ww['selected_names']==wm['selected_names'] and (ww['named_location_weight'],ww['canonical_support_weight'],ww['physical_support_weight'])==(10,12,18)
order4out={'sector_counts':{k:len(v) for k,v in by.items()},'domain':15254626,'sectors':sector4,'sole_valid':{'sector':vl,'logical':bitstr(vlog),'inherited':True,'inherited_ids':valid_inherited_ids,'indices':list(vidx)},'scope_controls':{'cross_sector':True,'schedule_local':True,'weight_distinct':True}}
print('R97_CLEANROOM_ORDER4_PASS',json.dumps(order4out,sort_keys=True),flush=True)

# Process ledger, strict serialization, disclosed incidents, protected identity.
proc=load(R/'PROCESS_LEDGER.json');records=proc['records']
assert len(records)==proc['bounded_foreground_records']==204 and proc['science_solver_children']==36 and proc['outer_solver_children']==12 and proc['direct_solver_children']==24
assert proc['all_children_reaped'] and proc['survivors']==proc['timeouts']==proc['background_processes']==proc['detached_processes']==0
assert all(x['reaped'] and not x['detached'] and not x['timed_out'] for x in records)
solvers=sorted([x for x in records if x['returncode']==10 and 'cadical_proof' in x['name']],key=lambda x:x['started_unix'])
assert len(solvers)==36 and all(a['ended_unix']<=b['started_unix'] for a,b in zip(solvers,solvers[1:]))
fails=[(x['name'],x['returncode']) for x in records if x['returncode'] not in (0,10)]
assert fails==[('order4_exact_synthesis',1),('order4_exact_synthesis_repair1',1)]
assert proc['corrected_failure_records']==[{'name':'order4_exact_synthesis','path':'logs/process/order4_exact_synthesis.json','returncode':1},{'name':'order4_exact_synthesis_repair1','path':'logs/process/order4_exact_synthesis_repair1.json','returncode':1}]
boot=(R/'logs/bootstrap-processes.tsv').read_text();assert 'failed_bootstrap' in boot and 'REJECTED' in boot and 'before process creation' in boot
err1=(R/'logs/stderr/order4_exact_synthesis.log').read_text();err2=(R/'logs/stderr/order4_exact_synthesis_repair1.log').read_text()
assert 'selected == sorted(selected)' in err1 and 'AssertionError' in err1 and "no attribute 'bit_count'" in err2 and 'AttributeError' in err2
orch=load(R/'verification/orchestration_events.json');assert orch['status']=='DISCLOSED' and len(orch['events'])==1
ev=orch['events'][0];assert ev['kind']=='transient_model_capacity_interruption' and not ev['os_process_started'] and not ev['science_process_affected'] and not ev['disk_evidence_affected'] and not ev['candidate_science_repeated'] and not ev['order4_census_repeated']
# Every SAT-side proof stream was fully summarized, contained no empty clause, and was deleted as a non-certificate.
streams=[]
for i in range(148,160):
 for rel in [f'iterations/iter{i}/outer/sat_trace_summary.json',f'iterations/iter{i}/direct/solver/Xerr.sat_trace_summary.json',f'iterations/iter{i}/direct/solver/Zerr.sat_trace_summary.json']:
  z=load(R/rel);assert z['solver_status']=='SATISFIABLE' and z['proof_output_enabled'] and z['empty_clause_lines']==0 and z['physical_lines_iterated']==z['lf_count'] and z['trace_absent_after_deletion'] and not z['full_trace_retained'] and z['certificate_disposition']=='not an UNSAT certificate';streams.append((z['bytes'],z['lf_count'],z['trace_sha256']))
assert len(streams)==36 and len({x[2] for x in streams})==36
pre=load(R/'verification/protected_tree_preinstall.json');post=load(R/'verification/protected_tree_postinstall.json');cmp=load(R/'verification/protected_tree_compare.json')
assert pre==post and pre['file_count']==cmp['file_count']==231 and cmp['canonical_and_protected_paths_unchanged'] and cmp['rows_equal'] and cmp['preinstall_sha256']==cmp['postinstall_sha256']=='39b1b2565237d67972d98b18364f481f1928d3f9def622bc2e3fb0aa8eb78ca7'
fix=load(R/'verification/fix2_closure.json');assert fix['status']=='PASS' and fix['all_task_children_reaped'] and fix['survivors']==fix['detached_processes']==fix['os_background_processes_started']==0 and fix['task_process_matches']==[] and fix['replay_temp_glob_matches']==[] and fix['science_solver_children']==36 and fix['bounded_records_in_package']==204 and fix['preseal_replay']=={'all_reaped':True,'children':116}
env=load(R/'ENVIRONMENT.json');assert env['python_executable_sha256']=='bdea59019a38eb6600cc9e71e984a97fedadc406448431281e7657030f54987e' and env['z3']=='5.1.0' and env['pysat']=='1.9.dev15' and env['network_used'] is False
for name,want in {'cadical-1.9.5-arm64-macos':'fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9','drat-trim-arm64-macos':'f58f63b0f76945d4c4c9ff6e87afaf870f579e67c0f7cca589492df8fc7ebd47','lrat-check-arm64-macos':'bd7eb8052623525814a0a37502b47f05375d9d9dfaf96ddc2fcd858958517cea'}.items():assert sha_file(R/'tooling'/name)==want==env['tooling'][name]['sha256']
res=load(R/'RESULT.json');assert res['D_star_Gross']==[11,12] and res['status']=='PASS' and res['verdict']=='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED' and res['completed_candidate_count']==12 and res['outer_sat_count']==12 and res['direct_sat_count']==24 and res['canonical_edits'] is False and res['commit'] is False
assert res['fresh_state']=={'assertions':19162,'clauses':1396722,'cnf_sha256':'aa18d2857ed5a7aefacd33bf4fbd42fded914393e123a87f00e84e4920e39d59','next_iteration':160,'selector_count':280,'selector_state_sha256':'ad3cf364dd9224c14ffb55046ba3dc8eb80035b1eaf997f1d7a5691297ad62a3','source_file_sha256':'8b754b649744a83eae6c80e64230f9782909b48e5613dcfd6c3c321d98b2dd66','source_semantic_sha256':'bb19e724c66eb6f3df8830a205ba29a297f5795d42d3fe066fa3b873800789ed','started':False,'state_file_sha256':'bb26ce4fc03ae9616a6a325438c3f4c82568a15c4fe133e074959b894e358194','variables':411526}
processout={'bounded':204,'science':36,'outer':12,'direct':24,'failures':fails,'strict_nonoverlap':True,'protected_files':231,'sat_streams':36,'survivors':0,'orchestration_non_os':1}
print('R97_CLEANROOM_PROCESS_PASS',json.dumps(processout,sort_keys=True),flush=True)

result={'status':'PASS','seconds':round(time.time()-T0,3),'seals':seals,'live':live,'formulas':formula,'outer':outer,'direct':direct,'order4':order4out,'process':processout,'fresh':formula[-1]}
OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print('R97_CLEANROOM_ALL_PASS',len(formula),len(outer),len(direct),round(time.time()-T0,3),flush=True)
```
## Appendix B — exact replay and overlay records

### B.1 Historical-overlay sealed replay stdout

```text
ROUND96_DEPENDENCIES_PASS 5.1.0 1.9.dev15
MANIFESTS_PASS 1589 d992087072835e2651834aceb3012f8afd20442b2886673b45254e95e861a361 9cf210a8dd392a57700a61b640ced0deda5d212173f88293083759f67cb77121
{"expected_returncode": 0, "name": "protected_bindings", "returncode": 0, "wall_seconds": 0.337566}
{"expected_returncode": 0, "name": "compile_iter148", "returncode": 0, "wall_seconds": 4.184968}
{"expected_returncode": 0, "name": "encoding_iter148", "returncode": 0, "wall_seconds": 7.662126}
FORMULA_REPLAY_PASS 148
{"expected_returncode": 0, "name": "compile_iter149", "returncode": 0, "wall_seconds": 4.228326}
{"expected_returncode": 0, "name": "encoding_iter149", "returncode": 0, "wall_seconds": 7.58274}
FORMULA_REPLAY_PASS 149
{"expected_returncode": 0, "name": "compile_iter150", "returncode": 0, "wall_seconds": 4.24402}
{"expected_returncode": 0, "name": "encoding_iter150", "returncode": 0, "wall_seconds": 7.810573}
FORMULA_REPLAY_PASS 150
{"expected_returncode": 0, "name": "compile_iter151", "returncode": 0, "wall_seconds": 4.291596}
{"expected_returncode": 0, "name": "encoding_iter151", "returncode": 0, "wall_seconds": 7.783946}
FORMULA_REPLAY_PASS 151
{"expected_returncode": 0, "name": "compile_iter152", "returncode": 0, "wall_seconds": 4.323188}
{"expected_returncode": 0, "name": "encoding_iter152", "returncode": 0, "wall_seconds": 7.673245}
FORMULA_REPLAY_PASS 152
{"expected_returncode": 0, "name": "compile_iter153", "returncode": 0, "wall_seconds": 4.230222}
{"expected_returncode": 0, "name": "encoding_iter153", "returncode": 0, "wall_seconds": 7.905847}
FORMULA_REPLAY_PASS 153
{"expected_returncode": 0, "name": "compile_iter154", "returncode": 0, "wall_seconds": 4.236518}
{"expected_returncode": 0, "name": "encoding_iter154", "returncode": 0, "wall_seconds": 7.781015}
FORMULA_REPLAY_PASS 154
{"expected_returncode": 0, "name": "compile_iter155", "returncode": 0, "wall_seconds": 4.266962}
{"expected_returncode": 0, "name": "encoding_iter155", "returncode": 0, "wall_seconds": 7.862684}
FORMULA_REPLAY_PASS 155
{"expected_returncode": 0, "name": "compile_iter156", "returncode": 0, "wall_seconds": 4.284241}
{"expected_returncode": 0, "name": "encoding_iter156", "returncode": 0, "wall_seconds": 7.906659}
FORMULA_REPLAY_PASS 156
{"expected_returncode": 0, "name": "compile_iter157", "returncode": 0, "wall_seconds": 4.270098}
{"expected_returncode": 0, "name": "encoding_iter157", "returncode": 0, "wall_seconds": 8.189687}
FORMULA_REPLAY_PASS 157
{"expected_returncode": 0, "name": "compile_iter158", "returncode": 0, "wall_seconds": 4.325198}
{"expected_returncode": 0, "name": "encoding_iter158", "returncode": 0, "wall_seconds": 7.959599}
FORMULA_REPLAY_PASS 158
{"expected_returncode": 0, "name": "compile_iter159", "returncode": 0, "wall_seconds": 4.30233}
{"expected_returncode": 0, "name": "encoding_iter159", "returncode": 0, "wall_seconds": 8.135567}
FORMULA_REPLAY_PASS 159
{"expected_returncode": 0, "name": "compile_iter160", "returncode": 0, "wall_seconds": 4.317083}
{"expected_returncode": 0, "name": "encoding_iter160", "returncode": 0, "wall_seconds": 8.054105}
FORMULA_REPLAY_PASS 160
{"expected_returncode": 0, "name": "outer_replay_iter148", "returncode": 0, "wall_seconds": 4.299288}
{"expected_returncode": 0, "name": "outer_assignment_iter148", "returncode": 0, "wall_seconds": 1.53184}
{"expected_returncode": 0, "name": "direct_build_iter148", "returncode": 0, "wall_seconds": 2.968347}
{"expected_returncode": 0, "name": "direct_assignment_iter148_Xerr", "returncode": 0, "wall_seconds": 0.045033}
{"expected_returncode": 0, "name": "direct_assignment_iter148_Zerr", "returncode": 0, "wall_seconds": 0.043586}
{"expected_returncode": 0, "name": "direct_replay_iter148", "returncode": 0, "wall_seconds": 2.874566}
{"expected_returncode": 0, "name": "transition_iter148", "returncode": 0, "wall_seconds": 3.389359}
CANDIDATE_REPLAY_PASS 148
{"expected_returncode": 0, "name": "outer_replay_iter149", "returncode": 0, "wall_seconds": 4.045315}
{"expected_returncode": 0, "name": "outer_assignment_iter149", "returncode": 0, "wall_seconds": 1.549169}
{"expected_returncode": 0, "name": "direct_build_iter149", "returncode": 0, "wall_seconds": 2.968857}
{"expected_returncode": 0, "name": "direct_assignment_iter149_Xerr", "returncode": 0, "wall_seconds": 0.045677}
{"expected_returncode": 0, "name": "direct_assignment_iter149_Zerr", "returncode": 0, "wall_seconds": 0.045013}
{"expected_returncode": 0, "name": "direct_replay_iter149", "returncode": 0, "wall_seconds": 2.865149}
{"expected_returncode": 0, "name": "transition_iter149", "returncode": 0, "wall_seconds": 3.356993}
CANDIDATE_REPLAY_PASS 149
{"expected_returncode": 0, "name": "outer_replay_iter150", "returncode": 0, "wall_seconds": 3.982871}
{"expected_returncode": 0, "name": "outer_assignment_iter150", "returncode": 0, "wall_seconds": 1.535084}
{"expected_returncode": 0, "name": "direct_build_iter150", "returncode": 0, "wall_seconds": 2.992617}
{"expected_returncode": 0, "name": "direct_assignment_iter150_Xerr", "returncode": 0, "wall_seconds": 0.04587}
{"expected_returncode": 0, "name": "direct_assignment_iter150_Zerr", "returncode": 0, "wall_seconds": 0.045692}
{"expected_returncode": 0, "name": "direct_replay_iter150", "returncode": 0, "wall_seconds": 2.881272}
{"expected_returncode": 0, "name": "transition_iter150", "returncode": 0, "wall_seconds": 3.477782}
CANDIDATE_REPLAY_PASS 150
{"expected_returncode": 0, "name": "outer_replay_iter151", "returncode": 0, "wall_seconds": 3.983844}
{"expected_returncode": 0, "name": "outer_assignment_iter151", "returncode": 0, "wall_seconds": 1.513406}
{"expected_returncode": 0, "name": "direct_build_iter151", "returncode": 0, "wall_seconds": 2.795763}
{"expected_returncode": 0, "name": "direct_assignment_iter151_Xerr", "returncode": 0, "wall_seconds": 0.045222}
{"expected_returncode": 0, "name": "direct_assignment_iter151_Zerr", "returncode": 0, "wall_seconds": 0.048273}
{"expected_returncode": 0, "name": "direct_replay_iter151", "returncode": 0, "wall_seconds": 2.812545}
{"expected_returncode": 0, "name": "transition_iter151", "returncode": 0, "wall_seconds": 3.387075}
CANDIDATE_REPLAY_PASS 151
{"expected_returncode": 0, "name": "outer_replay_iter152", "returncode": 0, "wall_seconds": 3.914397}
{"expected_returncode": 0, "name": "outer_assignment_iter152", "returncode": 0, "wall_seconds": 1.503565}
{"expected_returncode": 0, "name": "direct_build_iter152", "returncode": 0, "wall_seconds": 2.947846}
{"expected_returncode": 0, "name": "direct_assignment_iter152_Xerr", "returncode": 0, "wall_seconds": 0.045863}
{"expected_returncode": 0, "name": "direct_assignment_iter152_Zerr", "returncode": 0, "wall_seconds": 0.044822}
{"expected_returncode": 0, "name": "direct_replay_iter152", "returncode": 0, "wall_seconds": 2.841645}
{"expected_returncode": 0, "name": "transition_iter152", "returncode": 0, "wall_seconds": 3.402727}
CANDIDATE_REPLAY_PASS 152
{"expected_returncode": 0, "name": "outer_replay_iter153", "returncode": 0, "wall_seconds": 3.917452}
{"expected_returncode": 0, "name": "outer_assignment_iter153", "returncode": 0, "wall_seconds": 1.538774}
{"expected_returncode": 0, "name": "direct_build_iter153", "returncode": 0, "wall_seconds": 3.02745}
{"expected_returncode": 0, "name": "direct_assignment_iter153_Xerr", "returncode": 0, "wall_seconds": 0.045615}
{"expected_returncode": 0, "name": "direct_assignment_iter153_Zerr", "returncode": 0, "wall_seconds": 0.044971}
{"expected_returncode": 0, "name": "direct_replay_iter153", "returncode": 0, "wall_seconds": 2.942173}
{"expected_returncode": 0, "name": "transition_iter153", "returncode": 0, "wall_seconds": 3.420337}
CANDIDATE_REPLAY_PASS 153
{"expected_returncode": 0, "name": "outer_replay_iter154", "returncode": 0, "wall_seconds": 3.914683}
{"expected_returncode": 0, "name": "outer_assignment_iter154", "returncode": 0, "wall_seconds": 1.502757}
{"expected_returncode": 0, "name": "direct_build_iter154", "returncode": 0, "wall_seconds": 2.905225}
{"expected_returncode": 0, "name": "direct_assignment_iter154_Xerr", "returncode": 0, "wall_seconds": 0.045812}
{"expected_returncode": 0, "name": "direct_assignment_iter154_Zerr", "returncode": 0, "wall_seconds": 0.045061}
{"expected_returncode": 0, "name": "direct_replay_iter154", "returncode": 0, "wall_seconds": 2.843905}
{"expected_returncode": 0, "name": "transition_iter154", "returncode": 0, "wall_seconds": 3.381956}
CANDIDATE_REPLAY_PASS 154
{"expected_returncode": 0, "name": "outer_replay_iter155", "returncode": 0, "wall_seconds": 4.043646}
{"expected_returncode": 0, "name": "outer_assignment_iter155", "returncode": 0, "wall_seconds": 1.551551}
{"expected_returncode": 0, "name": "direct_build_iter155", "returncode": 0, "wall_seconds": 2.958537}
{"expected_returncode": 0, "name": "direct_assignment_iter155_Xerr", "returncode": 0, "wall_seconds": 0.045522}
{"expected_returncode": 0, "name": "direct_assignment_iter155_Zerr", "returncode": 0, "wall_seconds": 0.04515}
{"expected_returncode": 0, "name": "direct_replay_iter155", "returncode": 0, "wall_seconds": 2.740335}
{"expected_returncode": 0, "name": "transition_iter155", "returncode": 0, "wall_seconds": 3.416236}
CANDIDATE_REPLAY_PASS 155
{"expected_returncode": 0, "name": "outer_replay_iter156", "returncode": 0, "wall_seconds": 3.929266}
{"expected_returncode": 0, "name": "outer_assignment_iter156", "returncode": 0, "wall_seconds": 1.53012}
{"expected_returncode": 0, "name": "direct_build_iter156", "returncode": 0, "wall_seconds": 2.93014}
{"expected_returncode": 0, "name": "direct_assignment_iter156_Xerr", "returncode": 0, "wall_seconds": 0.045556}
{"expected_returncode": 0, "name": "direct_assignment_iter156_Zerr", "returncode": 0, "wall_seconds": 0.045334}
{"expected_returncode": 0, "name": "direct_replay_iter156", "returncode": 0, "wall_seconds": 2.695523}
{"expected_returncode": 0, "name": "transition_iter156", "returncode": 0, "wall_seconds": 3.411705}
CANDIDATE_REPLAY_PASS 156
{"expected_returncode": 0, "name": "outer_replay_iter157", "returncode": 0, "wall_seconds": 4.037531}
{"expected_returncode": 0, "name": "outer_assignment_iter157", "returncode": 0, "wall_seconds": 1.527212}
{"expected_returncode": 0, "name": "direct_build_iter157", "returncode": 0, "wall_seconds": 2.973664}
{"expected_returncode": 0, "name": "direct_assignment_iter157_Xerr", "returncode": 0, "wall_seconds": 0.045128}
{"expected_returncode": 0, "name": "direct_assignment_iter157_Zerr", "returncode": 0, "wall_seconds": 0.045169}
{"expected_returncode": 0, "name": "direct_replay_iter157", "returncode": 0, "wall_seconds": 2.830849}
{"expected_returncode": 0, "name": "transition_iter157", "returncode": 0, "wall_seconds": 3.318214}
CANDIDATE_REPLAY_PASS 157
{"expected_returncode": 0, "name": "outer_replay_iter158", "returncode": 0, "wall_seconds": 3.966885}
{"expected_returncode": 0, "name": "outer_assignment_iter158", "returncode": 0, "wall_seconds": 1.534344}
{"expected_returncode": 0, "name": "direct_build_iter158", "returncode": 0, "wall_seconds": 2.953545}
{"expected_returncode": 0, "name": "direct_assignment_iter158_Xerr", "returncode": 0, "wall_seconds": 0.04694}
{"expected_returncode": 0, "name": "direct_assignment_iter158_Zerr", "returncode": 0, "wall_seconds": 0.0446}
{"expected_returncode": 0, "name": "direct_replay_iter158", "returncode": 0, "wall_seconds": 2.862317}
{"expected_returncode": 0, "name": "transition_iter158", "returncode": 0, "wall_seconds": 3.497196}
CANDIDATE_REPLAY_PASS 158
{"expected_returncode": 0, "name": "outer_replay_iter159", "returncode": 0, "wall_seconds": 3.96015}
{"expected_returncode": 0, "name": "outer_assignment_iter159", "returncode": 0, "wall_seconds": 1.512416}
{"expected_returncode": 0, "name": "direct_build_iter159", "returncode": 0, "wall_seconds": 2.886788}
{"expected_returncode": 0, "name": "direct_assignment_iter159_Xerr", "returncode": 0, "wall_seconds": 0.045165}
{"expected_returncode": 0, "name": "direct_assignment_iter159_Zerr", "returncode": 0, "wall_seconds": 0.044673}
{"expected_returncode": 0, "name": "direct_replay_iter159", "returncode": 0, "wall_seconds": 2.813927}
{"expected_returncode": 0, "name": "transition_iter159", "returncode": 0, "wall_seconds": 3.439423}
CANDIDATE_REPLAY_PASS 159
{"expected_returncode": 0, "name": "order4_synthesis", "returncode": 0, "wall_seconds": 51.565554}
{"expected_returncode": 0, "name": "independent_campaign_audit", "returncode": 0, "wall_seconds": 24.858977}
{"expected_returncode": 0, "name": "result_crosscheck", "returncode": 0, "wall_seconds": 0.520215}
{"expected_returncode": 0, "name": "process_crosscheck", "returncode": 0, "wall_seconds": 0.021788}
{"expected_returncode": 0, "name": "proof_controls", "returncode": 0, "wall_seconds": 0.092445}
ROUND96_PACKAGE_REPLAY_PASS 116
```
### B.2 Disposable linked-overlay gate record

```json
{
  "all_children_reaped": true,
  "child_count": 9,
  "rows": [
    {
      "command": [
        "/usr/bin/python3",
        "tools/proof_dag_check.py",
        "--problem",
        "circdist",
        "--previous-state",
        "/private/tmp/circdist-r97-review-20260831/linked-overlay/circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag"
      ],
      "name": "previous_state",
      "reaped": true,
      "returncode": 0,
      "stderr": "",
      "stdout": "circdist: prior nodes, routes, and events retained\ncircdist: 16 node files structurally valid\n",
      "wall_seconds": 0.454734
    },
    {
      "command": [
        "/usr/bin/python3",
        "tools/proof_dag_check.py",
        "--problem",
        "circdist"
      ],
      "name": "proof_dag_circdist",
      "reaped": true,
      "returncode": 0,
      "stderr": "",
      "stdout": "circdist: 16 node files structurally valid\n",
      "wall_seconds": 0.19224
    },
    {
      "command": [
        "/usr/bin/python3",
        "tools/proof_dag_check.py",
        "--problem",
        "all"
      ],
      "name": "proof_dag_all",
      "reaped": true,
      "returncode": 0,
      "stderr": "",
      "stdout": "se: 85 node files structurally valid\nksum: 144 node files structurally valid\ncircdist: 16 node files structurally valid\nholevo-additivity-equality: 8 node files structurally valid\nholevo-counterexample-prevalence: 19 node files structurally valid\nholevo-extensive-violation: 147 node files structurally valid\nwerner-holevo-capacity-threshold: 20 node files structurally valid\ngrothendieck-d4: 41 node files structurally valid\ngrothendieck-e8: 9 node files structurally valid\ngrothendieck-group-orbit: 11 node files structurally valid\n",
      "wall_seconds": 1.730373
    },
    {
      "command": [
        "/usr/bin/python3",
        "tools/evidence_closure_check.py",
        "--problem",
        "circdist"
      ],
      "name": "evidence_closure",
      "reaped": true,
      "returncode": 0,
      "stderr": "",
      "stdout": "circdist: evidence closure OK, 164 structured paths; all evidence project-local and linked\n",
      "wall_seconds": 0.422252
    },
    {
      "command": [
        "/usr/bin/python3",
        "tools/check_circdist_migration.py"
      ],
      "name": "circdist_migration",
      "reaped": true,
      "returncode": 0,
      "stderr": "",
      "stdout": "Migration preservation OK: 16 nodes, 143 original events, 728 byte-identical copies\n",
      "wall_seconds": 0.701232
    },
    {
      "command": [
        "/usr/bin/python3",
        "tools/test_release_contracts.py"
      ],
      "name": "release_contracts",
      "reaped": true,
      "returncode": 0,
      "stderr": "..............\n----------------------------------------------------------------------\nRan 14 tests in 0.100s\n\nOK\n",
      "stdout": "",
      "wall_seconds": 0.147307
    },
    {
      "command": [
        "/usr/bin/python3",
        "tools/test_dag_contracts.py"
      ],
      "name": "dag_contracts",
      "reaped": true,
      "returncode": 0,
      "stderr": "........................\n----------------------------------------------------------------------\nRan 24 tests in 0.262s\n\nOK\n",
      "stdout": "",
      "wall_seconds": 0.307984
    },
    {
      "command": [
        "/usr/bin/python3",
        "tools/lean_dag_check.py",
        "--selftest"
      ],
      "name": "lean_selftest",
      "reaped": true,
      "returncode": 0,
      "stderr": "",
      "stdout": "=== selftest fixture: clean ===\n\ncoverage (evaluations actually performed):\n  1            : 2\n  2            : 4\n  3            : 2\n  4            : 1\n  6            : 2\n  7a           : 2\n  7b           : 1\n  lean-none    : 0\n  mechanized   : 2\n  nodes        : 2\n  schema:legacy-md : 1\n\nsummary: 0 FAIL, 0 WARN, 0 INFO\nassertion: clean fixture must produce no FAIL and exit 0 -> PASS\n\n=== selftest fixture: major2_unbacked_state ===\nFAIL [7a] FIX.parent: state asserts `composition-checked` but `composition` is null -- UNBACKED (the R11 MAJOR-2 class)\n\ncoverage (evaluations actually performed):\n  1            : 2\n  2            : 4\n  3            : 2\n  6            : 2\n  7a           : 2\n  7b           : 1\n  lean-none    : 0\n  mechanized   : 2\n  nodes        : 2\n  schema:legacy-md : 1\n\nsummary: 1 FAIL, 0 WARN, 0 INFO\nassertion: `state: composition-checked` with no composition theorem must FAIL (MAJOR-2 class) -> PASS\n\n=== selftest fixture: stale_hash ===\nFAIL [3] FIX.parent: node `claim_hash` d338fb05375bfa553ad6340bc04c20388b2b9d048f42fd3a69d53d985d31b702 != recomputed 1ae15fc3b2a1cce99f3dc0907a3f87031ad3fc1220b186d17fcf5fb15dca56c3\nFAIL [3] FIX.parent: docstring digest d338fb05375bfa553ad6340bc04c20388b2b9d048f42fd3a69d53d985d31b702 != recomputed 1ae15fc3b2a1cce99f3dc0907a3f87031ad3fc1220b186d17fcf5fb15dca56c3\nWARN [3b] FIX.parent: docstring frozen Claim body differs from the node's canonical claim (hash line may be stale-but-intact)\n\ncoverage (evaluations actually performed):\n  1            : 2\n  2            : 4\n  3            : 2\n  4            : 1\n  6            : 2\n  7a           : 2\n  7b           : 1\n  lean-none    : 0\n  mechanized   : 2\n  nodes        : 2\n  schema:legacy-md : 1\n\nsummary: 2 FAIL, 1 WARN, 0 INFO\nassertion: edited Claim body with a stale hash must FAIL -> PASS\n\n=== selftest fixture: import_mismatch ===\nWARN [4] FIX.parent: composition theorem text does not mention child `FIX.child` (TEXTUAL APPROXIMATION: a sound check needs elaboration)\nFAIL [6] FIX.parent: node-module imports [] != children ['FIX.child'] (UNDECLARED children not imported: ['FIX.child (mechanized)']) -- DAG_PROTOCOL \u00a71 lets a premise arrive as a child, a cited interface or an explicit relative hypothesis, but every such arrival must be NAMED in formalization.lean.rel as `premise-not-imported: <child> - <mechanism>` / `import-not-child: <module> - <mechanism>`\n\ncoverage (evaluations actually performed):\n  1            : 2\n  2            : 4\n  3            : 2\n  4            : 1\n  6            : 2\n  7a           : 2\n  7b           : 1\n  lean-none    : 0\n  mechanized   : 2\n  nodes        : 2\n  schema:legacy-md : 1\n\nsummary: 1 FAIL, 1 WARN, 0 INFO\nassertion: import not matching `children` must FAIL -> PASS\n\n=== selftest fixture: v6_clean ===\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=2, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 0 of 2 nodes carry no `formalization.lean` block.\n\ncoverage (evaluations actually performed):\n  1            : 2\n  2            : 4\n  3            : 2\n  4            : 1\n  6            : 2\n  7a           : 2\n  7b           : 1\n  7c           : 1\n  lean-none    : 0\n  mechanized   : 2\n  nodes        : 2\n  schema:v6    : 1\n\nsummary: 0 FAIL, 0 WARN, 2 INFO\nassertion: clean SCHEMA-V6 fixture must produce no FAIL and exit 0 -> PASS\n\n=== selftest fixture: v6_major2_unbacked_state ===\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=2, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 0 of 2 nodes carry no `formalization.lean` block.\nFAIL [7a] FIX.parent: state asserts `composition-checked` but `composition` is null -- UNBACKED (the R11 MAJOR-2 class)\n\ncoverage (evaluations actually performed):\n  1            : 2\n  2            : 4\n  3            : 2\n  6            : 2\n  7a           : 2\n  7b           : 1\n  7c           : 1\n  lean-none    : 0\n  mechanized   : 2\n  nodes        : 2\n  schema:v6    : 1\n\nsummary: 1 FAIL, 0 WARN, 2 INFO\nassertion: v6: `state: composition-checked` with `theorems:` absent must FAIL -> PASS\n\n=== selftest fixture: v6_stale_hash ===\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=2, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 0 of 2 nodes carry no `formalization.lean` block.\nFAIL [3] FIX.parent: node `claim_hash` 3aef117d2f1c62068c74577701e7ff9514e7852dcf25b011ff70ca46c36543a8 != recomputed 1a7187e1e4bceabb225d8efd3ccc87d8edaf23fc101acd375da9c2289436fa28\nFAIL [3] FIX.parent: docstring digest 3aef117d2f1c62068c74577701e7ff9514e7852dcf25b011ff70ca46c36543a8 != recomputed 1a7187e1e4bceabb225d8efd3ccc87d8edaf23fc101acd375da9c2289436fa28 [node declares `sync_state: current` (a claim about the QUOTED TEXT and the DIGESTS only -- never about whether the Lean `Claim : Prop` expresses the node claim) -- \u00a77 requires the formal statement, imports, proof and hash to be synchronized, so this FAIL is that open gate]\nWARN [3b] FIX.parent: docstring frozen Claim body differs from the node's canonical claim (hash line may be stale-but-intact)\n\ncoverage (evaluations actually performed):\n  1            : 2\n  2            : 4\n  3            : 2\n  4            : 1\n  6            : 2\n  7a           : 2\n  7b           : 1\n  7c           : 1\n  lean-none    : 0\n  mechanized   : 2\n  nodes        : 2\n  schema:v6    : 1\n\nsummary: 2 FAIL, 1 WARN, 2 INFO\nassertion: v6: edited claim with an intact claim_hash must FAIL -> PASS\n\n=== selftest fixture: v6_import_mismatch ===\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=1, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 1 of 2 nodes carry no `formalization.lean` block.\nWARN [4] FIX.parent: composition theorem text does not mention child `FIX.child` (TEXTUAL APPROXIMATION: a sound check needs elaboration)\nFAIL [6] FIX.parent: node-module imports [] != children ['FIX.child'] (UNDECLARED children not imported: ['FIX.child (no formal mirror)']) -- DAG_PROTOCOL \u00a71 lets a premise arrive as a child, a cited interface or an explicit relative hypothesis, but every such arrival must be NAMED in formalization.lean.rel as `premise-not-imported: <child> - <mechanism>` / `import-not-child: <module> - <mechanism>`\n\ncoverage (evaluations actually performed):\n  1            : 1\n  2            : 2\n  3            : 1\n  4            : 1\n  6            : 1\n  7a           : 1\n  7b           : 1\n  7c           : 1\n  lean-none    : 1\n  mechanized   : 1\n  nodes        : 2\n  schema:v6    : 1\n\nsummary: 1 FAIL, 1 WARN, 2 INFO\nassertion: v6: import not matching the route premises must FAIL -> PASS\n\n=== selftest fixture: v6_import_mismatch_declared ===\nINFO [rel] nodes: this tool checks that a declared `Cited.<field>` EXISTS, never that it is RELEVANT: a plausible but FALSE mechanism naming a real field passes. Judging the truth of a declared mechanism is a STANDING REVIEW OBLIGATION (DAG_PROTOCOL \u00a76.2/\u00a76.4), discharged for the 26 SE declarations by artifacts/se_task006_review_20260817.md \u00a7V3 and UNDISCHARGED for any declaration added since. 1 declaration(s) parsed in this run.\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=1, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 1 of 2 nodes carry no `formalization.lean` block.\nWARN [4] FIX.parent: composition theorem text does not mention child `FIX.child` (TEXTUAL APPROXIMATION: a sound check needs elaboration)\nINFO [6] FIX.parent: imports [] != children ['FIX.child'], and EVERY difference is declared in lean.rel: FIX.child <- enters as the cited interface field `Cited.fixture_field`, which the fixture Interface declares\n\ncoverage (evaluations actually performed):\n  1            : 1\n  2            : 2\n  3            : 1\n  4            : 1\n  6            : 1\n  7a           : 1\n  7b           : 1\n  7c           : 1\n  lean-none    : 1\n  mechanized   : 1\n  nodes        : 2\n  rel          : 1\n  schema:v6    : 1\n\nsummary: 0 FAIL, 1 WARN, 4 INFO\nassertion: v6: the SAME import mismatch, DECLARED per-premise in lean.rel, must NOT FAIL -> PASS\n\n=== selftest fixture: v6_import_mismatch_blanket ===\nFAIL [rel] FIX.parent: declaration `premise-not-imported: FIX.child` carries no substantive mechanism (needs >= 24 non-space characters, has 8; needs >= 4 words, has 1; names no `backticked identifier`, dotted node id, or ruling/deviation reference) -- it must name HOW the premise arrives / WHY the route is unrendered, in terms a reviewer can check\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=1, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 1 of 2 nodes carry no `formalization.lean` block.\nWARN [4] FIX.parent: composition theorem text does not mention child `FIX.child` (TEXTUAL APPROXIMATION: a sound check needs elaboration)\nFAIL [6] FIX.parent: node-module imports [] != children ['FIX.child'] (UNDECLARED children not imported: ['FIX.child (no formal mirror)']) -- DAG_PROTOCOL \u00a71 lets a premise arrive as a child, a cited interface or an explicit relative hypothesis, but every such arrival must be NAMED in formalization.lean.rel as `premise-not-imported: <child> - <mechanism>` / `import-not-child: <module> - <mechanism>`\n\ncoverage (evaluations actually performed):\n  1            : 1\n  2            : 2\n  3            : 1\n  4            : 1\n  6            : 1\n  7a           : 1\n  7b           : 1\n  7c           : 1\n  lean-none    : 1\n  mechanized   : 1\n  nodes        : 2\n  rel          : 1\n  schema:v6    : 1\n\nsummary: 2 FAIL, 1 WARN, 2 INFO\nassertion: v6: a declaration with no substantive mechanism must FAIL (no rubber stamps) -> PASS\n\n=== selftest fixture: v6_import_mismatch_bogus_field ===\nINFO [rel] nodes: this tool checks that a declared `Cited.<field>` EXISTS, never that it is RELEVANT: a plausible but FALSE mechanism naming a real field passes. Judging the truth of a declared mechanism is a STANDING REVIEW OBLIGATION (DAG_PROTOCOL \u00a76.2/\u00a76.4), discharged for the 26 SE declarations by artifacts/se_task006_review_20260817.md \u00a7V3 and UNDISCHARGED for any declaration added since. 1 declaration(s) parsed in this run.\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=1, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 1 of 2 nodes carry no `formalization.lean` block.\nWARN [4] FIX.parent: composition theorem text does not mention child `FIX.child` (TEXTUAL APPROXIMATION: a sound check needs elaboration)\nINFO [6] FIX.parent: imports [] != children ['FIX.child'], and EVERY difference is declared in lean.rel: FIX.child <- enters as the cited field `Cited.no_such_field`, which does not exist anywhere\nFAIL [6] FIX.parent: declaration names the cited field `Cited.no_such_field`, which does NOT exist in FIX.Interface -- the declared mechanism cannot be the real one\n\ncoverage (evaluations actually performed):\n  1            : 1\n  2            : 2\n  3            : 1\n  4            : 1\n  6            : 1\n  7a           : 1\n  7b           : 1\n  7c           : 1\n  lean-none    : 1\n  mechanized   : 1\n  nodes        : 2\n  rel          : 1\n  schema:v6    : 1\n\nsummary: 1 FAIL, 1 WARN, 4 INFO\nassertion: v6: a declaration naming a `Cited.<field>` absent from Interface.lean must FAIL -> PASS\n\n=== selftest fixture: v6_false_import_declaration ===\nINFO [rel] nodes: this tool checks that a declared `Cited.<field>` EXISTS, never that it is RELEVANT: a plausible but FALSE mechanism naming a real field passes. Judging the truth of a declared mechanism is a STANDING REVIEW OBLIGATION (DAG_PROTOCOL \u00a76.2/\u00a76.4), discharged for the 26 SE declarations by artifacts/se_task006_review_20260817.md \u00a7V3 and UNDISCHARGED for any declaration added since. 1 declaration(s) parsed in this run.\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=2, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 0 of 2 nodes carry no `formalization.lean` block.\nFAIL [6] FIX.parent: lean.rel declares premise `FIX.child` not imported, but the module DOES import it -- the declaration is false\n\ncoverage (evaluations actually performed):\n  1            : 2\n  2            : 4\n  3            : 2\n  4            : 1\n  6            : 2\n  7a           : 2\n  7b           : 1\n  7c           : 1\n  lean-none    : 0\n  mechanized   : 2\n  nodes        : 2\n  rel          : 1\n  schema:v6    : 1\n\nsummary: 1 FAIL, 0 WARN, 3 INFO\nassertion: v6: declaring a premise not-imported while the module DOES import it must FAIL -> PASS\n\n=== selftest fixture: v6_route_undeclared ===\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=2, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 0 of 2 nodes carry no `formalization.lean` block.\nFAIL [5] FIX.parent: composition_via_* suffixes ['only'] != live routes ['alt', 'only']; UNDECLARED unrendered route(s) ['alt'] -- each needs either a rendered theorem or an explicit `route-not-formalized: <route> - <reason>` entry in formalization.lean.rel\n\ncoverage (evaluations actually performed):\n  1            : 2\n  2            : 4\n  3            : 2\n  5            : 1\n  6            : 2\n  7a           : 2\n  7b           : 1\n  7c           : 1\n  lean-none    : 0\n  mechanized   : 2\n  nodes        : 2\n  schema:v6    : 1\n\nsummary: 1 FAIL, 0 WARN, 2 INFO\nassertion: v6: an unrendered ENABLED route with no declaration must FAIL -> PASS\n\n=== selftest fixture: v6_route_declared ===\nINFO [rel] nodes: this tool checks that a declared `Cited.<field>` EXISTS, never that it is RELEVANT: a plausible but FALSE mechanism naming a real field passes. Judging the truth of a declared mechanism is a STANDING REVIEW OBLIGATION (DAG_PROTOCOL \u00a76.2/\u00a76.4), discharged for the 26 SE declarations by artifacts/se_task006_review_20260817.md \u00a7V3 and UNDISCHARGED for any declaration added since. 1 declaration(s) parsed in this run.\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=2, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 0 of 2 nodes carry no `formalization.lean` block.\nINFO [5] FIX.parent: unrendered route(s) ['alt'], each DECLARED not-formalized in lean.rel: alt: the route carries no `proof:` key on the node, so rendering a `composition_via_*` theorem would invent content. Ruling R5 / deviation D6.\n\ncoverage (evaluations actually performed):\n  1            : 2\n  2            : 4\n  3            : 2\n  5            : 1\n  6            : 2\n  7a           : 2\n  7b           : 1\n  7c           : 1\n  lean-none    : 0\n  mechanized   : 2\n  nodes        : 2\n  rel          : 1\n  schema:v6    : 1\n\nsummary: 0 FAIL, 0 WARN, 4 INFO\nassertion: v6: the SAME unrendered route, DECLARED in lean.rel, must NOT FAIL -> PASS\n\n=== selftest fixture: v6_route_false_declaration ===\nINFO [rel] nodes: this tool checks that a declared `Cited.<field>` EXISTS, never that it is RELEVANT: a plausible but FALSE mechanism naming a real field passes. Judging the truth of a declared mechanism is a STANDING REVIEW OBLIGATION (DAG_PROTOCOL \u00a76.2/\u00a76.4), discharged for the 26 SE declarations by artifacts/se_task006_review_20260817.md \u00a7V3 and UNDISCHARGED for any declaration added since. 1 declaration(s) parsed in this run.\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=2, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 0 of 2 nodes carry no `formalization.lean` block.\nFAIL [5] FIX.parent: composition_via_* suffixes ['only'] != live routes ['alt', 'only']; UNDECLARED unrendered route(s) ['alt'] -- each needs either a rendered theorem or an explicit `route-not-formalized: <route> - <reason>` entry in formalization.lean.rel\nFAIL [5] FIX.parent: lean.rel declares route `only` not-formalized, but `composition_via_only` EXISTS in the module -- the declaration is false\n\ncoverage (evaluations actually performed):\n  1            : 2\n  2            : 4\n  3            : 2\n  5            : 1\n  6            : 2\n  7a           : 2\n  7b           : 1\n  7c           : 1\n  lean-none    : 0\n  mechanized   : 2\n  nodes        : 2\n  rel          : 1\n  schema:v6    : 1\n\nsummary: 2 FAIL, 0 WARN, 3 INFO\nassertion: v6: declaring a route not-formalized while its theorem EXISTS must FAIL -> PASS\n\n=== selftest fixture: v6_route_disabled ===\nINFO [rel] nodes: this tool checks that a declared `Cited.<field>` EXISTS, never that it is RELEVANT: a plausible but FALSE mechanism naming a real field passes. Judging the truth of a declared mechanism is a STANDING REVIEW OBLIGATION (DAG_PROTOCOL \u00a76.2/\u00a76.4), discharged for the 26 SE declarations by artifacts/se_task006_review_20260817.md \u00a7V3 and UNDISCHARGED for any declaration added since. 1 declaration(s) parsed in this run.\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=2, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 1 of 3 nodes carry no `formalization.lean` block.\nINFO [5] FIX.parent: route(s) DISABLED per \u00a74 and therefore not required to carry a `composition_via_*` theorem: alt (premise FIX.dead is REFUTED)\nINFO [6] FIX.parent: lean.rel retains the non-import declaration for disabled-route premise `FIX.dead`; it is historical metadata and is not required by the live composition\n\ncoverage (evaluations actually performed):\n  1            : 2\n  2            : 4\n  3            : 2\n  5            : 1\n  6            : 2\n  7a           : 2\n  7b           : 1\n  7c           : 1\n  lean-none    : 1\n  mechanized   : 2\n  nodes        : 3\n  rel          : 1\n  schema:v6    : 1\n\nsummary: 0 FAIL, 0 WARN, 5 INFO\nassertion: v6: a route disabled by a REFUTED premise (\u00a74) needs no theorem and no declaration -> PASS\n\n=== selftest fixture: v6_import_mismatch_junk ===\nFAIL [rel] FIX.parent: declaration `premise-not-imported: FIX.child` carries no substantive mechanism (needs >= 4 words, has 1; names no `backticked identifier`, dotted node id, or ruling/deviation reference) -- it must name HOW the premise arrives / WHY the route is unrendered, in terms a reviewer can check\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=1, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 1 of 2 nodes carry no `formalization.lean` block.\nWARN [4] FIX.parent: composition theorem text does not mention child `FIX.child` (TEXTUAL APPROXIMATION: a sound check needs elaboration)\nFAIL [6] FIX.parent: node-module imports [] != children ['FIX.child'] (UNDECLARED children not imported: ['FIX.child (no formal mirror)']) -- DAG_PROTOCOL \u00a71 lets a premise arrive as a child, a cited interface or an explicit relative hypothesis, but every such arrival must be NAMED in formalization.lean.rel as `premise-not-imported: <child> - <mechanism>` / `import-not-child: <module> - <mechanism>`\n\ncoverage (evaluations actually performed):\n  1            : 1\n  2            : 2\n  3            : 1\n  4            : 1\n  6            : 1\n  7a           : 1\n  7b           : 1\n  7c           : 1\n  lean-none    : 1\n  mechanized   : 1\n  nodes        : 2\n  rel          : 1\n  schema:v6    : 1\n\nsummary: 2 FAIL, 1 WARN, 2 INFO\nassertion: F1: a 26-character mechanism with no words and no anchor must FAIL (the pure length gate is gone) -> PASS\n\n=== selftest fixture: v6_relevance_notice ===\nINFO [rel] nodes: this tool checks that a declared `Cited.<field>` EXISTS, never that it is RELEVANT: a plausible but FALSE mechanism naming a real field passes. Judging the truth of a declared mechanism is a STANDING REVIEW OBLIGATION (DAG_PROTOCOL \u00a76.2/\u00a76.4), discharged for the 26 SE declarations by artifacts/se_task006_review_20260817.md \u00a7V3 and UNDISCHARGED for any declaration added since. 1 declaration(s) parsed in this run.\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=1, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 1 of 2 nodes carry no `formalization.lean` block.\nWARN [4] FIX.parent: composition theorem text does not mention child `FIX.child` (TEXTUAL APPROXIMATION: a sound check needs elaboration)\nINFO [6] FIX.parent: imports [] != children ['FIX.child'], and EVERY difference is declared in lean.rel: FIX.child <- enters as the cited interface field `Cited.fixture_field`, which the fixture Interface declares\n\ncoverage (evaluations actually performed):\n  1            : 1\n  2            : 2\n  3            : 1\n  4            : 1\n  6            : 1\n  7a           : 1\n  7b           : 1\n  7c           : 1\n  lean-none    : 1\n  mechanized   : 1\n  nodes        : 2\n  rel          : 1\n  schema:v6    : 1\n\nsummary: 0 FAIL, 1 WARN, 4 INFO\nassertion: F2: relevance is undecidable here, so a run carrying declarations must PRINT the residual risk and the docstring must keep the disclosure -> PASS\n\n=== selftest fixture: v6_import_not_child_mechanized ===\nINFO [rel] nodes: this tool checks that a declared `Cited.<field>` EXISTS, never that it is RELEVANT: a plausible but FALSE mechanism naming a real field passes. Judging the truth of a declared mechanism is a STANDING REVIEW OBLIGATION (DAG_PROTOCOL \u00a76.2/\u00a76.4), discharged for the 26 SE declarations by artifacts/se_task006_review_20260817.md \u00a7V3 and UNDISCHARGED for any declaration added since. 1 declaration(s) parsed in this run.\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=3, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 0 of 3 nodes carry no `formalization.lean` block.\nFAIL [6] FIX.child: node-module imports [] != children ['FIX.grand'] (UNDECLARED children not imported: ['FIX.grand (mechanized)']) -- DAG_PROTOCOL \u00a71 lets a premise arrive as a child, a cited interface or an explicit relative hypothesis, but every such arrival must be NAMED in formalization.lean.rel as `premise-not-imported: <child> - <mechanism>` / `import-not-child: <module> - <mechanism>`\nINFO [6] FIX.parent: imports ['FIX.child', 'FIX.grand'] != children ['FIX.child'], and EVERY difference is declared in lean.rel: FIX.grand (non-child import) <- GRANDCHILD reached by skipping the intermediate node `FIX.child`; `FIX.grand.Claim` is consumed directly as a parameter of `composition`. Ruling R3 / deviation D2.\nFAIL [6] FIX.parent: declared non-child import `FIX.grand` is a DAG descendant of `FIX.parent`, but it is reached ACROSS the MECHANIZED intermediate node(s) ['FIX.child'], which do carry a `formalization` block -- the licence for a non-child import is that the skipped nodes have NO module to import (skipped: ['FIX.child'])\nWARN [7c] FIX.child: node level PROVED exceeds min(route down=OPEN, FIX.grand=PROVED) on its best live route and NO assessment caveat names the shortfall\n\ncoverage (evaluations actually performed):\n  1            : 3\n  2            : 6\n  3            : 3\n  4            : 1\n  6            : 3\n  7a           : 3\n  7b           : 1\n  7c           : 2\n  lean-none    : 0\n  mechanized   : 3\n  nodes        : 3\n  rel          : 1\n  schema:v6    : 1\n\nsummary: 2 FAIL, 1 WARN, 4 INFO\nassertion: F3: a non-child import reached ACROSS a MECHANIZED intermediate must FAIL -> PASS\n\n=== selftest fixture: v6_import_not_child_unmechanized ===\nINFO [rel] nodes: this tool checks that a declared `Cited.<field>` EXISTS, never that it is RELEVANT: a plausible but FALSE mechanism naming a real field passes. Judging the truth of a declared mechanism is a STANDING REVIEW OBLIGATION (DAG_PROTOCOL \u00a76.2/\u00a76.4), discharged for the 26 SE declarations by artifacts/se_task006_review_20260817.md \u00a7V3 and UNDISCHARGED for any declaration added since. 2 declaration(s) parsed in this run.\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=2, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 1 of 3 nodes carry no `formalization.lean` block.\nWARN [4] FIX.parent: composition theorem text does not mention child `FIX.child` (TEXTUAL APPROXIMATION: a sound check needs elaboration)\nINFO [6] FIX.parent: imports ['FIX.grand'] != children ['FIX.child'], and EVERY difference is declared in lean.rel: FIX.child <- the node carries no `formalization` block, so no module for it exists to import; the obligation lives on the grandchild `FIX.grand`. Ruling R3. | FIX.grand (non-child import) <- GRANDCHILD reached by skipping the intermediate node `FIX.child`; `FIX.grand.Claim` is consumed directly as a parameter of `composition`. Ruling R3 / deviation D2.\nWARN [7c] FIX.child: node level PROVED exceeds min(route down=OPEN, FIX.grand=PROVED) on its best live route and NO assessment caveat names the shortfall\n\ncoverage (evaluations actually performed):\n  1            : 2\n  2            : 4\n  3            : 2\n  4            : 1\n  6            : 2\n  7a           : 2\n  7b           : 1\n  7c           : 2\n  lean-none    : 1\n  mechanized   : 2\n  nodes        : 3\n  rel          : 2\n  schema:v6    : 1\n\nsummary: 0 FAIL, 2 WARN, 4 INFO\nassertion: F3 control: the SAME non-child import across an UNMECHANIZED intermediate is still licensed and must NOT FAIL -> PASS\n\n=== selftest fixture: v6_premise_not_imported_mechanized ===\nINFO [rel] nodes: this tool checks that a declared `Cited.<field>` EXISTS, never that it is RELEVANT: a plausible but FALSE mechanism naming a real field passes. Judging the truth of a declared mechanism is a STANDING REVIEW OBLIGATION (DAG_PROTOCOL \u00a76.2/\u00a76.4), discharged for the 26 SE declarations by artifacts/se_task006_review_20260817.md \u00a7V3 and UNDISCHARGED for any declaration added since. 1 declaration(s) parsed in this run.\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=2, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 0 of 2 nodes carry no `formalization.lean` block.\nWARN [4] FIX.parent: composition theorem text does not mention child `FIX.child` (TEXTUAL APPROXIMATION: a sound check needs elaboration)\nINFO [6] FIX.parent: imports [] != children ['FIX.child'], and EVERY difference is declared in lean.rel: FIX.child <- enters as the cited interface field `Cited.fixture_field`, which the fixture Interface declares\nFAIL [6] FIX.parent: lean.rel declares premise `FIX.child` not imported, but `FIX.child` CARRIES A `formalization` BLOCK (module `FIX.child`) -- a module for it demonstrably exists, so the composition must import it rather than route it around the DAG\n\ncoverage (evaluations actually performed):\n  1            : 2\n  2            : 4\n  3            : 2\n  4            : 1\n  6            : 2\n  7a           : 2\n  7b           : 1\n  7c           : 1\n  lean-none    : 0\n  mechanized   : 2\n  nodes        : 2\n  rel          : 1\n  schema:v6    : 1\n\nsummary: 1 FAIL, 1 WARN, 4 INFO\nassertion: F4: declaring a premise not-imported while it CARRIES a formalization block must FAIL -> PASS\n\n=== selftest fixture: doc_refuted_silences_check5 ===\ndocumentation regression; sentinel '* F5 A `REFUTED` WRITE LEGITIMATELY SILENCES CHECK 5.' FOUND in the module docstring\nassertion: F5: the docstring must keep naming the \u00a74 REFUTED-route exemption as a legitimate silencer of check 5 -> PASS\n\n=== selftest fixture: v6_sync_state_notice ===\nINFO [3] nodes: `sync_state: current` asserts ONLY that the module quotes the current claim text and that the digests agree (checks 3/3b). It does NOT assert that the Lean `Claim : Prop` expresses the node claim: a module may quote its claim perfectly and still render a deliberately weaker SHADOW of it. That correspondence is a review act this tool cannot perform; read each module header and the node's own caveats. current=2, stale=0.\nINFO [0] nodes: schema v6 has no `lean: none` + reason field: absence of a formal mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL \u00a71/\u00a77), so the \u00a77.4 per-node silence check is NOT PORTABLE and is not run. 0 of 2 nodes carry no `formalization.lean` block.\n\ncoverage (evaluations actually performed):\n  1            : 2\n  2            : 4\n  3            : 2\n  4            : 1\n  6            : 2\n  7a           : 2\n  7b           : 1\n  7c           : 1\n  lean-none    : 0\n  mechanized   : 2\n  nodes        : 2\n  schema:v6    : 1\n\nsummary: 0 FAIL, 0 WARN, 2 INFO\nassertion: F6: every run reporting `sync_state` must say it is about quoted TEXT and DIGESTS only, in the output and in the docstring -> PASS\n\nSELFTEST: 23/23 assertions passed\n",
      "wall_seconds": 0.130521
    },
    {
      "command": [
        "/usr/bin/python3",
        "/private/tmp/circdist-r97-review-20260831/linked-overlay/circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/duplicate_yaml_scan.py",
        "--root",
        "/private/tmp/circdist-r97-review-20260831/linked-overlay",
        "--output",
        "/private/tmp/circdist-r97-review-20260831/overlay-gates/duplicate.result.json"
      ],
      "name": "duplicate_yaml",
      "reaped": true,
      "returncode": 0,
      "stderr": "",
      "stdout": "{\"duplicates\": [], \"files\": 934, \"mappings\": 24868, \"schema\": \"round88-duplicate-yaml-scan-v1\", \"status\": \"PASS\"}\n",
      "wall_seconds": 6.810391
    }
  ],
  "status": "PASS"
}
```
### B.3 Independent proof-fixture rerun summary

The rerun used the package-native binaries and package fixtures with a reviewer-owned generated LRAT path. This is the exact return-code and output-hash summary.

```text
independent return codes:
valid_drat=0
valid_lrat=0
corrupt_drat=1
truncated_drat=1
corrupt_lrat=1
truncated_lrat=1

independent output SHA-256 values:
9382d64004c352284f604fb3bcc8b8abf400f668124a9db89213e01b5beb062b  corrupt-drat.out
581f3b3f55a33a4547681025f12a9bc29f030cb747490c96d448519ffca4f4d7  corrupt-lrat.out
2d5252c56aec92233bd7476b38b9f3d83b565835f75c5dc912504f7b9f69a907  truncated-drat.out
ec5553864144a099068519043983a9fa1272d0bf1c246a663a9fe3e6b0f55094  truncated-lrat.out
54f024fae61b40172176ab9bf3c76a856030aa18b8e58049ee83fb316317bd52  valid-drat.out
54b78d5976475e8834663f5cc7cc530ff2338fd46f3d678f0feac39315512c1c  valid-lrat.out

independent generated LRAT:
cf32dfff36b24ba36c3504765f29ecf3d7a8abaa59956ade4d24a4062caa6431  generated.lrat

All six independent stderr files were empty.
```
### B.4 Sealed package proof-control record

```json
{
  "corrupt_drat_rejected": true,
  "corrupt_lrat_rejected": true,
  "fixture_cnf_sha256": "b8d28f511bbc3bc5d67e0fcda748b6ad85d5e543c64bc91d09f34ecb10805efd",
  "generated_lrat_accepted": true,
  "generated_lrat_sha256": "cf32dfff36b24ba36c3504765f29ecf3d7a8abaa59956ade4d24a4062caa6431",
  "runs": [
    {
      "command": [
        "/private/tmp/circdist-r96-work-20260831/tooling/drat-trim-arm64-macos",
        "/private/tmp/circdist-r96-work-20260831/controls/proof_checker/php6_5.cnf",
        "/private/tmp/circdist-r96-work-20260831/controls/proof_checker/php6_5.fresh.drat",
        "-t",
        "170",
        "-L",
        "<tmpdir>/T/circdist-r88-proof-control.xataontc/generated.lrat"
      ],
      "name": "valid_drat_generate_lrat",
      "returncode": 0,
      "stderr": "",
      "stdout": "\nc parsing input formula with 30 variables and 141 clauses\n\nc finished parsing\n\nc detected empty clause; start verification via backward checking\n\nc 87 of 141 clauses in core                            \n\nc 135 of 165 lemmas in core using 1985 resolution steps\n\nc 0 RAT lemmas in core; 0 redundant literals in core lemmas\n\ns VERIFIED\n\nc verification time: 0.024 seconds\n",
      "wall_seconds": 0.286214
    },
    {
      "command": [
        "/private/tmp/circdist-r96-work-20260831/tooling/lrat-check-arm64-macos",
        "/private/tmp/circdist-r96-work-20260831/controls/proof_checker/php6_5.cnf",
        "<tmpdir>/T/circdist-r88-proof-control.xataontc/generated.lrat"
      ],
      "name": "valid_generated_lrat",
      "returncode": 0,
      "stderr": "",
      "stdout": "c parsed a formula with 30 variables and 141 clauses\nc VERIFIED\nc allocated 1024 634 300\nc Added clauses = 276.  Deleted clauses = 251.  Max live clauses = 141\nc verification time = 0.00 secs\n",
      "wall_seconds": 0.11871
    },
    {
      "command": [
        "/private/tmp/circdist-r96-work-20260831/tooling/drat-trim-arm64-macos",
        "/private/tmp/circdist-r96-work-20260831/controls/proof_checker/php6_5.cnf",
        "/private/tmp/circdist-r96-work-20260831/controls/proof_checker/php6_5.corrupt.drat",
        "-t",
        "170"
      ],
      "name": "corrupt_drat",
      "returncode": 1,
      "stderr": "",
      "stdout": "\nc turning on binary mode checking\n\nc parsing input formula with 30 variables and 141 clauses\n\nc WARNING: wrong binary prefix, stop reading proof\n\nc finished parsing\n\nc ERROR: no conflict\n\ns NOT VERIFIED\n\nc verification time: 0.022 seconds\n",
      "wall_seconds": 0.025811
    },
    {
      "command": [
        "/private/tmp/circdist-r96-work-20260831/tooling/drat-trim-arm64-macos",
        "/private/tmp/circdist-r96-work-20260831/controls/proof_checker/php6_5.cnf",
        "/private/tmp/circdist-r96-work-20260831/controls/proof_checker/php6_5.truncated.drat",
        "-t",
        "170"
      ],
      "name": "truncated_drat",
      "returncode": 1,
      "stderr": "",
      "stdout": "\nc parsing input formula with 30 variables and 141 clauses\n\nc finished parsing\n\nc ERROR: no conflict\n\ns NOT VERIFIED\n\nc verification time: 0.019 seconds\n",
      "wall_seconds": 0.02267
    },
    {
      "command": [
        "/private/tmp/circdist-r96-work-20260831/tooling/lrat-check-arm64-macos",
        "/private/tmp/circdist-r96-work-20260831/controls/proof_checker/php6_5.cnf",
        "/private/tmp/circdist-r96-work-20260831/controls/proof_checker/php6_5.corrupt.lrat"
      ],
      "name": "corrupt_lrat",
      "returncode": 1,
      "stderr": "",
      "stdout": "c parsed a formula with 30 variables and 141 clauses\nc WARNING: Verification incomplete. Last line checked = 0\nc NOT VERIFIED\nc allocated 1024 634 300\nc Added clauses = 141.  Deleted clauses = 0.  Max live clauses = 141\nc verification time = 0.00 secs\n",
      "wall_seconds": 0.005273
    },
    {
      "command": [
        "/private/tmp/circdist-r96-work-20260831/tooling/lrat-check-arm64-macos",
        "/private/tmp/circdist-r96-work-20260831/controls/proof_checker/php6_5.cnf",
        "/private/tmp/circdist-r96-work-20260831/controls/proof_checker/php6_5.truncated.lrat"
      ],
      "name": "truncated_lrat",
      "returncode": 1,
      "stderr": "",
      "stdout": "c parsed a formula with 30 variables and 141 clauses\nc WARNING: Verification incomplete. Last line checked = 147\nc NOT VERIFIED\nc allocated 1024 634 300\nc Added clauses = 147.  Deleted clauses = 59.  Max live clauses = 141\nc verification time = 0.00 secs\n",
      "wall_seconds": 0.005264
    }
  ],
  "schema": "circdist-round88-proof-controls-v1",
  "scope": "tool-chain controls only; no Gross UNSAT occurred",
  "status": "PASS",
  "truncated_drat_rejected": true,
  "truncated_lrat_rejected": true,
  "valid_drat_accepted": true,
  "valid_drat_sha256": "b6c2e560bb08c84d583ca94799951a21c8cae5de35d6d04d77bc4842e9c18ecd"
}
```
## Appendix C — sole complete licensed replacement for `CIRCDIST.gross.yaml`

Extract exactly the bytes in this single YAML fence, including its final LF. No other replacement document is licensed by this review.

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
    CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}. Round 95''s fresh independent exact review clears the sealed Round-94 package for proposer-level continuation only: iterations 136--147 add 24 exact EFSSC selectors after twelve legal outer SAT schedules and twenty-four unrestricted direct-sector SAT/physical replays; the complete same-sector order-3 GF(2) search retains zero terms; and the fresh frontier is unstarted iteration 148 with 256 selectors and checked-unsolved CNF sha256:397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4. No Gross UNSAT, direct absence, repair, exhaustion, D* narrowing, route promotion, or root promotion is licensed; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}. Round 97''s fresh independent exact review clears the sealed Round-96 package for proposer-level continuation only: iterations 148--159 add 24 exact EFSSC selectors after twelve legal outer SAT schedules and twenty-four unrestricted direct-sector SAT/physical replays; the complete same-sector order-4 GF(2) search covers 15,254,626 distinct quadruples and retains zero novel terms; and the fresh frontier is unstarted iteration 160 with 280 selectors and checked-unsolved CNF sha256:aa18d2857ed5a7aefacd33bf4fbd42fded914393e123a87f00e84e4920e39d59. No Gross UNSAT, direct absence, repair, exhaustion, D* narrowing, route promotion, or root promotion is licensed; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
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
    task: 'Continue only from the independently reviewed sealed fresh/unstarted iteration 160 state. The inherited sound order-block
      library remains exactly 14,484 predicates (1,440 unary, 20 round-62, 12,820 generalized, and 204 dynamic), and the exact
      fixed-selector frontier is 280 EFSSCs: the reviewed 256-selector Round-95 frontier plus the 24 exact candidate-domain
      selectors from iterations 148--159. Bind selector-state sha256:ad3cf364dd9224c14ffb55046ba3dc8eb80035b1eaf997f1d7a5691297ad62a3,
      state-file sha256:bb26ce4fc03ae9616a6a325438c3f4c82568a15c4fe133e074959b894e358194, iteration-160 semantic-source
      sha256:bb19e724c66eb6f3df8830a205ba29a297f5795d42d3fe066fa3b873800789ed, and source-file sha256:8b754b649744a83eae6c80e64230f9782909b48e5613dcfd6c3c321d98b2dd66
      before use. Its deterministic 10-bit compressed finite-outer formula has 19,162 source assertions, 411,526 variables,
      1,396,722 clauses and CNF sha256:aa18d2857ed5a7aefacd33bf4fbd42fded914393e123a87f00e84e4920e39d59; it was checked but deliberately
      not solved, and no iteration-160 solver/model/DRAT/LRAT disposition is inherited. The complete same-sector order-4 GF(2)
      search at the post-iteration-136 234-selector frontier retained zero novel terms after exhaustively visiting C(125,4)+C(109,4)=15,254,626
      distinct quadruples. Its only conservative syndrome-zero valid occurrence is a Zerr result with logical action 100110100011
      whose exact named predicate was already inherited. This licenses a no-go only for that exact same-sector, four-distinct-selector
      finite domain and frozen iteration-136 schedule; it does not cover mixed sectors, order 5 or higher, arbitrary mechanisms,
      other frontiers, or global exhaustion. For a SAT result, retain the complete assignment, replay every DIMACS clause and
      frozen schedule condition, then rebuild and adjudicate both complete unrestricted direct-360 sectors; a positive mechanism
      kills only that concrete candidate domain and proves no absence, and only exact source-schedule-valid EFSSC selectors
      may be added atomically. For an UNSAT result, retain a complete DRAT proof, independently accept it, generate LRAT, and
      independently accept the LRAT with valid/corrupt/truncated controls. Enter repair only after both direct sectors have
      independently checked absence. Preserve frozen S_Gross, strict serialization, MC0, terminal residual semantics, both
      CSS sectors, and every existing exclusion against morphing, Circ-Preserve substitutions, alternate conflict models,
      exploratory pair clauses, retroactive cuts, stale compressor provenance, mixed-sector XOR, support-weight substitution,
      and schedule-globalized dynamic predicates. Keep CIRCDIST.gross and gap-via-lift CONJECTURED and D*_Gross in {11,12};
      this reviewed continuation supplies no Gross UNSAT, absence, exhaustion, distance-12 witness, universal distance-11 ceiling,
      route promotion, or root promotion.'
    kind: task
    since: '2026-08-31'
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
```
## Appendix D — exact final prelink evidence-closure set

This is the complete sorted 1,588-path set, one repository-relative path per line. Its newline-terminated byte stream is 177,851 bytes, SHA-256 `b07043cabeada208f75c4115588c02c7c5bfdb531996f81f95172cd6418af7ad`.

```text
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/ENVIRONMENT.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/EVIDENCE_HASHES.md
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/FAILURE_LEDGER.md
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/FILE_INVENTORY.jsonl
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/FIX-2.md
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/INPUT_BINDINGS.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/MANIFEST.md
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/MATHEMATICAL_SCOPE_AND_SOUNDNESS.md
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/PAYLOAD_SHA256SUMS.txt
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/PROCESS_LEDGER.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/PROPOSED_CANONICAL_DELTA.md
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/REPORT.md
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/RESULT.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/SHA256SUMS.txt
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/SYNTHESIS_PROOF.md
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/DAG_PROTOCOL.md
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/FILE_PROTOCOL.md
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/circdist__artifacts__circdist_gross_proof_outer_round94_20260830__PAYLOAD_SHA256SUMS.txt
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/circdist__artifacts__circdist_gross_proof_outer_round94_20260830__SHA256SUMS.txt
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/circdist__artifacts__definitions__CIRCDIST_PROBLEMS.md
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/circdist__proof-dag__nodes__CIRCDIST.gross.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/circdist__reviews__circdist_gross_proof_outer_round94_exact_review_round95_20260830.md
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/GRAPH.mmd
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/NODE_INDEX.md
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/PROJECT.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/nodes/CIRCDIST.cplx.fixed-d.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/nodes/CIRCDIST.cplx.islands.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/nodes/CIRCDIST.cplx.sigma2.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/nodes/CIRCDIST.cplx.upper.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/nodes/CIRCDIST.cplx.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/nodes/CIRCDIST.gross.dext-cap.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/nodes/CIRCDIST.gross.mc-equiv.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/nodes/CIRCDIST.lift.gap-example.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/nodes/CIRCDIST.lift.nonint.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/nodes/CIRCDIST.lift.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/nodes/CIRCDIST.sat.instances.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/nodes/CIRCDIST.sat.window.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/initial_proof_dag/circdist/proof-dag/nodes/CIRCDIST.sat.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/bindings/operations__circdist__SCHEDULER.yaml
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/campaign/current.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/campaign/driver_process_149_150.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/campaign/driver_process_151_153.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/campaign/driver_process_154_156.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/campaign/driver_process_157_159.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/campaign/manual_process_148.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/campaign/progress.jsonl
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/campaign/summary_148_148.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/campaign/summary_149_150.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/campaign/summary_151_153.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/campaign/summary_154_156.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/campaign/summary_157_159.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/controls/proof_checker/php6_5.cnf
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/controls/proof_checker/php6_5.corrupt.drat
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/controls/proof_checker/php6_5.corrupt.lrat
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/controls/proof_checker/php6_5.fresh.drat
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/controls/proof_checker/php6_5.fresh.lrat
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/controls/proof_checker/php6_5.truncated.drat
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/controls/proof_checker/php6_5.truncated.lrat
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/controls/proof_fixture_controls.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/data/campaign_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/data/vendor_inventory.jsonl
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter148/assertion_map.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter148/circuit_trace.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter148/encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter148/metadata.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter148/outer.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter148/source.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter149/assertion_map.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter149/circuit_trace.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter149/encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter149/metadata.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter149/outer.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter149/source.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter150/assertion_map.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter150/circuit_trace.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter150/encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter150/metadata.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter150/outer.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter150/source.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter151/assertion_map.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter151/circuit_trace.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter151/encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter151/metadata.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter151/outer.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter151/source.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter152/assertion_map.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter152/circuit_trace.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter152/encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter152/metadata.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter152/outer.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter152/source.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter153/assertion_map.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter153/circuit_trace.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter153/encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter153/metadata.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter153/outer.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter153/source.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter154/assertion_map.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter154/circuit_trace.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter154/encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter154/metadata.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter154/outer.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter154/source.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter155/assertion_map.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter155/circuit_trace.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter155/encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter155/metadata.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter155/outer.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter155/source.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter156/assertion_map.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter156/circuit_trace.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter156/encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter156/metadata.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter156/outer.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter156/source.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter157/assertion_map.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter157/circuit_trace.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter157/encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter157/metadata.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter157/outer.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter157/source.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter158/assertion_map.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter158/circuit_trace.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter158/encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter158/metadata.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter158/outer.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter158/source.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter159/assertion_map.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter159/circuit_trace.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter159/encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter159/metadata.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter159/outer.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter159/source.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter160/assertion_map.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter160/circuit_trace.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter160/encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter160/metadata.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter160/outer.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/formulas/iter160/source.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/build_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/direct360/Xerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/direct360/Xerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/direct360/Xerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/direct360/Xerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/direct360/Xerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/direct360/Zerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/direct360/Zerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/direct360/Zerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/direct360/Zerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/direct360/Zerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/direct_verification.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/solver/Xerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/solver/Xerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/solver/Xerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/solver/Xerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/solver/Xerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/solver/Zerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/solver/Zerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/solver/Zerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/solver/Zerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/direct/solver/Zerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/outer/assignment.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/outer/assignment.independent.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/outer/assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/outer/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/outer/replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/outer/sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/outer/solver.log.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/outer/solver.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter148/record.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/build_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/direct360/Xerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/direct360/Xerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/direct360/Xerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/direct360/Xerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/direct360/Xerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/direct360/Zerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/direct360/Zerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/direct360/Zerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/direct360/Zerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/direct360/Zerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/direct_verification.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/solver/Xerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/solver/Xerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/solver/Xerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/solver/Xerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/solver/Xerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/solver/Zerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/solver/Zerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/solver/Zerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/solver/Zerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/direct/solver/Zerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/outer/assignment.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/outer/assignment.independent.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/outer/assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/outer/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/outer/replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/outer/sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/outer/solver.log.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/outer/solver.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter149/record.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/build_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/direct360/Xerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/direct360/Xerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/direct360/Xerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/direct360/Xerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/direct360/Xerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/direct360/Zerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/direct360/Zerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/direct360/Zerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/direct360/Zerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/direct360/Zerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/direct_verification.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/solver/Xerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/solver/Xerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/solver/Xerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/solver/Xerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/solver/Xerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/solver/Zerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/solver/Zerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/solver/Zerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/solver/Zerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/direct/solver/Zerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/outer/assignment.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/outer/assignment.independent.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/outer/assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/outer/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/outer/replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/outer/sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/outer/solver.log.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/outer/solver.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter150/record.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/build_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/direct360/Xerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/direct360/Xerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/direct360/Xerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/direct360/Xerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/direct360/Xerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/direct360/Zerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/direct360/Zerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/direct360/Zerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/direct360/Zerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/direct360/Zerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/direct_verification.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/solver/Xerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/solver/Xerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/solver/Xerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/solver/Xerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/solver/Xerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/solver/Zerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/solver/Zerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/solver/Zerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/solver/Zerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/direct/solver/Zerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/outer/assignment.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/outer/assignment.independent.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/outer/assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/outer/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/outer/replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/outer/sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/outer/solver.log.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/outer/solver.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter151/record.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/build_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/direct360/Xerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/direct360/Xerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/direct360/Xerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/direct360/Xerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/direct360/Xerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/direct360/Zerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/direct360/Zerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/direct360/Zerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/direct360/Zerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/direct360/Zerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/direct_verification.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/solver/Xerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/solver/Xerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/solver/Xerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/solver/Xerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/solver/Xerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/solver/Zerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/solver/Zerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/solver/Zerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/solver/Zerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/direct/solver/Zerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/outer/assignment.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/outer/assignment.independent.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/outer/assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/outer/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/outer/replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/outer/sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/outer/solver.log.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/outer/solver.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter152/record.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/build_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/direct360/Xerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/direct360/Xerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/direct360/Xerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/direct360/Xerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/direct360/Xerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/direct360/Zerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/direct360/Zerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/direct360/Zerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/direct360/Zerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/direct360/Zerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/direct_verification.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/solver/Xerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/solver/Xerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/solver/Xerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/solver/Xerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/solver/Xerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/solver/Zerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/solver/Zerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/solver/Zerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/solver/Zerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/direct/solver/Zerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/outer/assignment.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/outer/assignment.independent.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/outer/assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/outer/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/outer/replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/outer/sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/outer/solver.log.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/outer/solver.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter153/record.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/build_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/direct360/Xerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/direct360/Xerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/direct360/Xerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/direct360/Xerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/direct360/Xerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/direct360/Zerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/direct360/Zerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/direct360/Zerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/direct360/Zerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/direct360/Zerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/direct_verification.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/solver/Xerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/solver/Xerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/solver/Xerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/solver/Xerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/solver/Xerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/solver/Zerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/solver/Zerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/solver/Zerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/solver/Zerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/direct/solver/Zerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/outer/assignment.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/outer/assignment.independent.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/outer/assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/outer/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/outer/replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/outer/sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/outer/solver.log.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/outer/solver.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter154/record.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/build_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/direct360/Xerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/direct360/Xerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/direct360/Xerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/direct360/Xerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/direct360/Xerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/direct360/Zerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/direct360/Zerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/direct360/Zerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/direct360/Zerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/direct360/Zerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/direct_verification.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/solver/Xerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/solver/Xerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/solver/Xerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/solver/Xerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/solver/Xerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/solver/Zerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/solver/Zerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/solver/Zerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/solver/Zerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/direct/solver/Zerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/outer/assignment.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/outer/assignment.independent.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/outer/assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/outer/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/outer/replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/outer/sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/outer/solver.log.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/outer/solver.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter155/record.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/build_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/direct360/Xerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/direct360/Xerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/direct360/Xerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/direct360/Xerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/direct360/Xerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/direct360/Zerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/direct360/Zerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/direct360/Zerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/direct360/Zerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/direct360/Zerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/direct_verification.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/solver/Xerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/solver/Xerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/solver/Xerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/solver/Xerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/solver/Xerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/solver/Zerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/solver/Zerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/solver/Zerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/solver/Zerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/direct/solver/Zerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/outer/assignment.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/outer/assignment.independent.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/outer/assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/outer/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/outer/replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/outer/sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/outer/solver.log.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/outer/solver.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter156/record.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/build_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/direct360/Xerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/direct360/Xerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/direct360/Xerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/direct360/Xerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/direct360/Xerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/direct360/Zerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/direct360/Zerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/direct360/Zerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/direct360/Zerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/direct360/Zerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/direct_verification.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/solver/Xerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/solver/Xerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/solver/Xerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/solver/Xerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/solver/Xerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/solver/Zerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/solver/Zerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/solver/Zerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/solver/Zerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/direct/solver/Zerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/outer/assignment.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/outer/assignment.independent.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/outer/assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/outer/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/outer/replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/outer/sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/outer/solver.log.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/outer/solver.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter157/record.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/build_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/direct360/Xerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/direct360/Xerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/direct360/Xerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/direct360/Xerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/direct360/Xerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/direct360/Zerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/direct360/Zerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/direct360/Zerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/direct360/Zerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/direct360/Zerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/direct_verification.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/solver/Xerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/solver/Xerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/solver/Xerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/solver/Xerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/solver/Xerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/solver/Zerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/solver/Zerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/solver/Zerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/solver/Zerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/direct/solver/Zerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/outer/assignment.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/outer/assignment.independent.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/outer/assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/outer/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/outer/replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/outer/sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/outer/solver.log.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/outer/solver.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter158/record.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/build_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/direct360/Xerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/direct360/Xerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/direct360/Xerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/direct360/Xerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/direct360/Xerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/direct360/Zerr.clauses.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/direct360/Zerr.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/direct360/Zerr.columns.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/direct360/Zerr.summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/direct360/Zerr.variables.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/direct_verification.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/solver/Xerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/solver/Xerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/solver/Xerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/solver/Xerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/solver/Xerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/solver/Zerr.assignment.dimacs
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/solver/Zerr.assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/solver/Zerr.sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/solver/Zerr.solver.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/direct/solver/Zerr.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/outer/assignment.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/outer/assignment.independent.dimacs.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/outer/assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/outer/candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/outer/replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/outer/sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/outer/solver.log.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/outer/solver.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/iterations/iter159/record.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/bootstrap-processes.tsv
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter148_Xerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter148_Xerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter148_Xerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter148_Zerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter148_Zerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter148_Zerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter148_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter148_replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter149_Xerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter149_Xerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter149_Xerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter149_Zerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter149_Zerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter149_Zerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter149_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter149_replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter150_Xerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter150_Xerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter150_Xerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter150_Zerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter150_Zerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter150_Zerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter150_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter150_replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter151_Xerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter151_Xerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter151_Xerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter151_Zerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter151_Zerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter151_Zerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter151_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter151_replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter152_Xerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter152_Xerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter152_Xerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter152_Zerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter152_Zerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter152_Zerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter152_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter152_replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter153_Xerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter153_Xerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter153_Xerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter153_Zerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter153_Zerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter153_Zerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter153_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter153_replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter154_Xerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter154_Xerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter154_Xerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter154_Zerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter154_Zerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter154_Zerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter154_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter154_replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter155_Xerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter155_Xerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter155_Xerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter155_Zerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter155_Zerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter155_Zerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter155_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter155_replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter156_Xerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter156_Xerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter156_Xerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter156_Zerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter156_Zerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter156_Zerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter156_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter156_replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter157_Xerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter157_Xerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter157_Xerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter157_Zerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter157_Zerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter157_Zerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter157_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter157_replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter158_Xerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter158_Xerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter158_Xerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter158_Zerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter158_Zerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter158_Zerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter158_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter158_replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter159_Xerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter159_Xerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter159_Xerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter159_Zerr_assignment_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter159_Zerr_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter159_Zerr_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter159_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/direct_iter159_replay.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/initial_binding_and_frontier.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter148_atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter148_correspondence.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter148_encoding_recheck.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter148_pending_transition_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter148_recompile.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter149_atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter149_pending_compile.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter149_pending_encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter149_pending_transition_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter150_atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter150_pending_compile.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter150_pending_encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter150_pending_transition_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter151_atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter151_pending_compile.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter151_pending_encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter151_pending_transition_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter152_atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter152_pending_compile.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter152_pending_encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter152_pending_transition_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter153_atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter153_pending_compile.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter153_pending_encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter153_pending_transition_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter154_atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter154_pending_compile.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter154_pending_encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter154_pending_transition_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter155_atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter155_pending_compile.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter155_pending_encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter155_pending_transition_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter156_atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter156_pending_compile.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter156_pending_encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter156_pending_transition_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter157_atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter157_pending_compile.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter157_pending_encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter157_pending_transition_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter158_atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter158_pending_compile.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter158_pending_encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter158_pending_transition_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter159_atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter159_pending_compile.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter159_pending_encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter159_pending_transition_build.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter160_pending_compile.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/iter160_pending_encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/order4_exact_synthesis.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/order4_exact_synthesis_repair1.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/order4_exact_synthesis_repair2.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter148_assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter148_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter148_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter148_verify_sat.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter149_assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter149_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter149_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter149_verify_sat.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter150_assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter150_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter150_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter150_verify_sat.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter151_assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter151_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter151_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter151_verify_sat.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter152_assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter152_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter152_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter152_verify_sat.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter153_assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter153_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter153_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter153_verify_sat.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter154_assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter154_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter154_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter154_verify_sat.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter155_assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter155_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter155_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter155_verify_sat.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter156_assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter156_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter156_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter156_verify_sat.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter157_assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter157_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter157_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter157_verify_sat.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter158_assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter158_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter158_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter158_verify_sat.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter159_assignment_independent_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter159_cadical_proof.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter159_sat_trace_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/outer_iter159_verify_sat.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/record_iter148_campaign.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/round96_deterministic_compression.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/round96_independent_campaign_audit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/round96_independent_campaign_audit_after_compression.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/process/round96_proof_fixture_controls.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter148_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter148_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter148_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter148_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter148_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter148_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter149_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter149_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter149_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter149_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter149_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter149_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter150_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter150_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter150_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter150_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter150_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter150_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter151_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter151_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter151_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter151_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter151_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter151_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter152_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter152_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter152_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter152_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter152_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter152_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter153_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter153_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter153_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter153_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter153_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter153_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter154_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter154_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter154_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter154_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter154_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter154_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter155_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter155_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter155_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter155_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter155_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter155_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter156_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter156_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter156_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter156_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter156_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter156_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter157_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter157_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter157_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter157_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter157_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter157_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter158_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter158_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter158_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter158_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter158_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter158_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter159_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter159_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter159_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter159_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter159_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/direct_iter159_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/initial_binding_and_frontier.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter148_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter148_correspondence.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter148_encoding_recheck.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter148_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter148_recompile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter149_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter149_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter149_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter149_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter150_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter150_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter150_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter150_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter151_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter151_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter151_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter151_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter152_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter152_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter152_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter152_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter153_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter153_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter153_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter153_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter154_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter154_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter154_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter154_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter155_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter155_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter155_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter155_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter156_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter156_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter156_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter156_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter157_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter157_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter157_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter157_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter158_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter158_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter158_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter158_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter159_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter159_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter159_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter159_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter160_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/iter160_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/order4_exact_synthesis.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/order4_exact_synthesis_repair1.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/order4_exact_synthesis_repair2.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter148_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter148_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter148_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter149_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter149_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter149_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter150_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter150_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter150_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter151_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter151_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter151_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter152_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter152_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter152_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter153_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter153_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter153_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter154_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter154_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter154_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter155_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter155_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter155_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter156_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter156_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter156_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter157_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter157_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter157_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter158_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter158_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter158_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter159_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter159_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/outer_iter159_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/record_iter148_campaign.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/round96_deterministic_compression.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/round96_independent_campaign_audit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/round96_independent_campaign_audit_after_compression.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/round96_make_package_metadata.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/round96_make_package_metadata_postinstall.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/round96_proof_fixture_controls.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stderr/round96_write_reports.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter148_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter148_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter148_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter148_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter148_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter148_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter149_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter149_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter149_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter149_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter149_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter149_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter150_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter150_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter150_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter150_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter150_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter150_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter151_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter151_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter151_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter151_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter151_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter151_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter152_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter152_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter152_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter152_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter152_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter152_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter153_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter153_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter153_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter153_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter153_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter153_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter154_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter154_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter154_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter154_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter154_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter154_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter155_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter155_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter155_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter155_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter155_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter155_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter156_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter156_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter156_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter156_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter156_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter156_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter157_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter157_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter157_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter157_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter157_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter157_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter158_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter158_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter158_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter158_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter158_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter158_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter159_Xerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter159_Xerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter159_Zerr_assignment_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter159_Zerr_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter159_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/direct_iter159_replay.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/initial_binding_and_frontier.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter148_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter148_correspondence.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter148_encoding_recheck.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter148_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter148_recompile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter149_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter149_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter149_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter149_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter150_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter150_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter150_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter150_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter151_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter151_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter151_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter151_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter152_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter152_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter152_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter152_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter153_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter153_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter153_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter153_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter154_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter154_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter154_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter154_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter155_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter155_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter155_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter155_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter156_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter156_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter156_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter156_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter157_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter157_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter157_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter157_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter158_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter158_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter158_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter158_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter159_atomic_commit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter159_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter159_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter159_pending_transition_build.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter160_pending_compile.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/iter160_pending_encoding_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/order4_exact_synthesis.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/order4_exact_synthesis_repair1.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/order4_exact_synthesis_repair2.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter148_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter148_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter148_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter149_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter149_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter149_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter150_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter150_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter150_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter151_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter151_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter151_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter152_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter152_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter152_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter153_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter153_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter153_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter154_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter154_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter154_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter155_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter155_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter155_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter156_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter156_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter156_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter157_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter157_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter157_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter158_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter158_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter158_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter159_assignment_independent_check.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter159_sat_trace_summary.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/outer_iter159_verify_sat.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/record_iter148_campaign.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/round96_deterministic_compression.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/round96_independent_campaign_audit.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/round96_independent_campaign_audit_after_compression.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/round96_make_package_metadata.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/round96_make_package_metadata_postinstall.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/round96_proof_fixture_controls.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/stdout/round96_write_reports.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter149_Xerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter149_Xerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter149_Xerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter149_Xerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter149_Xerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter149_Xerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter149_Zerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter149_Zerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter149_Zerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter149_Zerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter149_Zerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter149_Zerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter149_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter149_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter149_replay.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter149_replay.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter150_Xerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter150_Xerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter150_Xerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter150_Xerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter150_Xerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter150_Xerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter150_Zerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter150_Zerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter150_Zerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter150_Zerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter150_Zerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter150_Zerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter150_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter150_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter150_replay.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter150_replay.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter151_Xerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter151_Xerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter151_Xerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter151_Xerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter151_Xerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter151_Xerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter151_Zerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter151_Zerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter151_Zerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter151_Zerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter151_Zerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter151_Zerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter151_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter151_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter151_replay.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter151_replay.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter152_Xerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter152_Xerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter152_Xerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter152_Xerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter152_Xerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter152_Xerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter152_Zerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter152_Zerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter152_Zerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter152_Zerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter152_Zerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter152_Zerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter152_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter152_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter152_replay.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter152_replay.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter153_Xerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter153_Xerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter153_Xerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter153_Xerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter153_Xerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter153_Xerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter153_Zerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter153_Zerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter153_Zerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter153_Zerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter153_Zerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter153_Zerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter153_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter153_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter153_replay.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter153_replay.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter154_Xerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter154_Xerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter154_Xerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter154_Xerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter154_Xerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter154_Xerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter154_Zerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter154_Zerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter154_Zerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter154_Zerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter154_Zerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter154_Zerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter154_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter154_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter154_replay.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter154_replay.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter155_Xerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter155_Xerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter155_Xerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter155_Xerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter155_Xerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter155_Xerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter155_Zerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter155_Zerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter155_Zerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter155_Zerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter155_Zerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter155_Zerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter155_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter155_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter155_replay.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter155_replay.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter156_Xerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter156_Xerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter156_Xerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter156_Xerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter156_Xerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter156_Xerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter156_Zerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter156_Zerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter156_Zerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter156_Zerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter156_Zerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter156_Zerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter156_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter156_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter156_replay.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter156_replay.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter157_Xerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter157_Xerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter157_Xerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter157_Xerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter157_Xerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter157_Xerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter157_Zerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter157_Zerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter157_Zerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter157_Zerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter157_Zerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter157_Zerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter157_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter157_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter157_replay.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter157_replay.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter158_Xerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter158_Xerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter158_Xerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter158_Xerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter158_Xerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter158_Xerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter158_Zerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter158_Zerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter158_Zerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter158_Zerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter158_Zerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter158_Zerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter158_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter158_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter158_replay.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter158_replay.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter159_Xerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter159_Xerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter159_Xerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter159_Xerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter159_Xerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter159_Xerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter159_Zerr_assignment_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter159_Zerr_assignment_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter159_Zerr_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter159_Zerr_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter159_Zerr_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter159_Zerr_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter159_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter159_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter159_replay.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/direct_iter159_replay.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter149_atomic_commit.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter149_atomic_commit.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter149_pending_transition_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter149_pending_transition_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter150_atomic_commit.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter150_atomic_commit.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter150_pending_compile.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter150_pending_compile.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter150_pending_encoding_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter150_pending_encoding_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter150_pending_transition_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter150_pending_transition_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter151_atomic_commit.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter151_atomic_commit.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter151_pending_compile.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter151_pending_compile.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter151_pending_encoding_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter151_pending_encoding_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter151_pending_transition_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter151_pending_transition_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter152_atomic_commit.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter152_atomic_commit.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter152_pending_compile.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter152_pending_compile.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter152_pending_encoding_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter152_pending_encoding_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter152_pending_transition_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter152_pending_transition_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter153_atomic_commit.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter153_atomic_commit.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter153_pending_compile.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter153_pending_compile.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter153_pending_encoding_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter153_pending_encoding_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter153_pending_transition_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter153_pending_transition_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter154_atomic_commit.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter154_atomic_commit.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter154_pending_compile.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter154_pending_compile.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter154_pending_encoding_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter154_pending_encoding_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter154_pending_transition_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter154_pending_transition_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter155_atomic_commit.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter155_atomic_commit.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter155_pending_compile.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter155_pending_compile.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter155_pending_encoding_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter155_pending_encoding_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter155_pending_transition_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter155_pending_transition_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter156_atomic_commit.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter156_atomic_commit.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter156_pending_compile.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter156_pending_compile.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter156_pending_encoding_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter156_pending_encoding_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter156_pending_transition_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter156_pending_transition_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter157_atomic_commit.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter157_atomic_commit.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter157_pending_compile.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter157_pending_compile.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter157_pending_encoding_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter157_pending_encoding_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter157_pending_transition_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter157_pending_transition_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter158_atomic_commit.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter158_atomic_commit.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter158_pending_compile.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter158_pending_compile.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter158_pending_encoding_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter158_pending_encoding_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter158_pending_transition_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter158_pending_transition_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter159_atomic_commit.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter159_atomic_commit.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter159_pending_compile.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter159_pending_compile.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter159_pending_encoding_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter159_pending_encoding_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter159_pending_transition_build.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter159_pending_transition_build.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter160_pending_compile.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter160_pending_compile.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter160_pending_encoding_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/iter160_pending_encoding_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter149_assignment_independent_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter149_assignment_independent_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter149_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter149_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter149_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter149_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter149_verify_sat.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter149_verify_sat.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter150_assignment_independent_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter150_assignment_independent_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter150_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter150_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter150_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter150_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter150_verify_sat.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter150_verify_sat.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter151_assignment_independent_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter151_assignment_independent_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter151_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter151_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter151_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter151_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter151_verify_sat.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter151_verify_sat.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter152_assignment_independent_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter152_assignment_independent_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter152_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter152_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter152_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter152_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter152_verify_sat.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter152_verify_sat.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter153_assignment_independent_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter153_assignment_independent_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter153_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter153_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter153_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter153_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter153_verify_sat.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter153_verify_sat.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter154_assignment_independent_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter154_assignment_independent_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter154_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter154_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter154_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter154_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter154_verify_sat.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter154_verify_sat.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter155_assignment_independent_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter155_assignment_independent_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter155_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter155_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter155_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter155_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter155_verify_sat.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter155_verify_sat.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter156_assignment_independent_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter156_assignment_independent_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter156_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter156_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter156_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter156_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter156_verify_sat.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter156_verify_sat.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter157_assignment_independent_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter157_assignment_independent_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter157_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter157_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter157_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter157_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter157_verify_sat.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter157_verify_sat.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter158_assignment_independent_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter158_assignment_independent_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter158_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter158_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter158_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter158_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter158_verify_sat.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter158_verify_sat.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter159_assignment_independent_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter159_assignment_independent_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter159_cadical_proof.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter159_cadical_proof.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter159_sat_trace_summary.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter159_sat_trace_summary.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter159_verify_sat.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/logs/wrapper/outer_iter159_verify_sat.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/reconstruction/correspondence.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/reconstruction/fresh.assertion_map.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/reconstruction/fresh.circuit_trace.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/reconstruction/fresh.encoding_check.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/reconstruction/fresh.metadata.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/reconstruction/fresh.outer.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/reconstruction/input_bindings.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/reconstruction/stored.assertion_map.jsonl.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/reconstruction/stored.outer.cnf.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/replay.sh
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/advance_round96.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/atomic_promote_round96.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/audit_round96.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/build_direct_from_candidate.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/check_evidence_closure_expected.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/check_iter148_correspondence.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/check_manifests.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/check_outer_encoding.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/check_process_ledger.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/check_proof_controls.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/check_protected.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/check_result.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/compare_json.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/compile_outer_cnf.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/deterministic_compress.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/duplicate_yaml_scan.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/extract_and_check_assignment.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/final_preseal_checks.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/fix2_cleanup.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/make_package_metadata.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/order4_gf2_closure.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/prepare_round96.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/protected_tree_snapshot.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/record_iter148_campaign.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/replay_package.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/run_bounded.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/run_logged.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/run_repository_validators.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/run_round96_campaign.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/seal_package.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/summarize_sat_trace.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/verify_actual_unsat.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/verify_outer_sat_model.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/source/write_round96_reports.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/state/iter148_state.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/state/iter149_state.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/state/iter150_state.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/state/iter151_state.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/state/iter152_state.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/state/iter153_state.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/state/iter154_state.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/state/iter155_state.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/state/iter156_state.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/state/iter157_state.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/state/iter158_state.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/state/iter159_state.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/state/iter160_state.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/synthesis/inputs/iter136_candidate.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/synthesis/inputs/iter136_direct_verification.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/synthesis/inputs/iter137_state.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/synthesis/order4_gf2_closure.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/tooling/cadical-1.9.5-arm64-macos
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/tooling/drat-trim-arm64-macos
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/tooling/lrat-check-arm64-macos
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter148_to149/atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter148_to149/pending_intent.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter149_to150/atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter149_to150/pending_intent.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter150_to151/atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter150_to151/pending_intent.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter151_to152/atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter151_to152/pending_intent.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter152_to153/atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter152_to153/pending_intent.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter153_to154/atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter153_to154/pending_intent.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter154_to155/atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter154_to155/pending_intent.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter155_to156/atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter155_to156/pending_intent.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter156_to157/atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter156_to157/pending_intent.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter157_to158/atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter157_to158/pending_intent.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter158_to159/atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter158_to159/pending_intent.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter159_to160/atomic_commit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/transitions/iter159_to160/pending_intent.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/vendor/round80/restart/dynamic_blocks_iteration102.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/vendor/round80/restart/full_raw_mechanisms_iteration102.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/vendor/round80/restart/installed_generalized_terms_iteration102.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/vendor/round80/restart/online_mechanism_registry_iteration102.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/vendor/round80/restart/restart_state.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/vendor/round80/src/global_single_clauses.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/vendor/round80/src/inputs/w12X.txt
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/vendor/round80/src/inputs/w12Z.txt
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/vendor/round80/src/replay_direct_candidate.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/vendor/round80/src/round62_cegar20.json.gz
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/vendor/round80/src/round63_src/model.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/vendor/round80/src/round63_src/outer.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/vendor/round80/src/round63_src/pattern.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/vendor/round80/src/round68_build.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/vendor/round80/src/round68_verify.py
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/compression.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/evidence_closure_interpretation.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/final_preseal_checks.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/fix2_cleanup.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/fix2_cleanup.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/fix2_cleanup.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/fix2_closure.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/independent_campaign_audit.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/install_copy.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/orchestration_events.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/preseal_replay.children.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/preseal_replay.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/preseal_replay.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/preseal_replay.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/protected_tree_compare.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/protected_tree_postinstall.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/protected_tree_preinstall.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/pruning.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/circdist_migration.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/circdist_migration.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/circdist_migration.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/dag_contracts.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/dag_contracts.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/dag_contracts.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/duplicate_yaml.result.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/duplicate_yaml.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/duplicate_yaml.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/duplicate_yaml.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/evidence_closure.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/evidence_closure.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/evidence_closure.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/evidence_closure_parser.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/evidence_closure_parser.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/evidence_closure_parser.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/git_diff_check.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/git_diff_check.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/git_diff_check.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/lean_dag_selftest.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/lean_dag_selftest.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/lean_dag_selftest.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/proof_dag_circdist.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/proof_dag_circdist.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/proof_dag_circdist.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/proof_dag_previous_state.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/proof_dag_previous_state.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/proof_dag_previous_state.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/release_contracts.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/release_contracts.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/release_contracts.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators/summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators_driver.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators_driver.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/repository_validators_driver.stdout.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/round96_make_package_metadata.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/round96_make_package_metadata_postinstall.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/round96_write_reports.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/validation_summary.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/write_final_reports.run.json
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/write_final_reports.stderr.log
circdist/artifacts/circdist_gross_proof_outer_round96_20260831/verification/write_final_reports.stdout.log
```
## Appendix E — exact stored order-4 census independently reproduced

The normalized JSON object below was matched in full by Appendix A, including every histogram, miss reason, multiplicity control, checksum, and scope audit. File SHA-256 is `7a0cc557f3b0cc07d1e7c692e36a225f48d79dcdf73ee69d28c9c1246125b583`.

```json
{
  "audits": {
    "cross_sector_ambiguity": {
      "Xerr": {
        "canonical_support": [
          3,
          8,
          9,
          13,
          30,
          47,
          49,
          57,
          62,
          75,
          80,
          102,
          103,
          114,
          123,
          125,
          126,
          132,
          135,
          137,
          140,
          142
        ],
        "logical": "011100000100",
        "physical_logical": "011100000100",
        "physical_support": [
          3,
          6,
          9,
          13,
          14,
          15,
          31,
          47,
          49,
          53,
          57,
          61,
          63,
          64,
          69,
          71,
          72,
          81,
          102,
          103,
          104,
          113,
          114,
          119,
          123,
          125,
          126,
          132,
          142,
          143
        ],
        "physical_syndrome": [
          2,
          4,
          5,
          9,
          10,
          19,
          20,
          25,
          26,
          31,
          36,
          42,
          43,
          54,
          56,
          59,
          61,
          62,
          63,
          64,
          66,
          68,
          69,
          70
        ],
        "syndrome": [
          2,
          4,
          5,
          9,
          10,
          19,
          20,
          25,
          26,
          31,
          36,
          42,
          43,
          54,
          56,
          59,
          61,
          62,
          63,
          64,
          66,
          68,
          69,
          70
        ]
      },
      "Zerr": {
        "canonical_support": [
          10,
          29,
          36,
          45,
          51,
          56,
          57,
          58,
          59,
          61,
          62,
          66,
          67,
          99,
          102,
          103,
          106,
          114,
          115,
          119,
          121,
          124,
          125,
          127,
          132,
          139
        ],
        "logical": "110001101000",
        "physical_logical": "110001101000",
        "physical_support": [
          10,
          23,
          32,
          36,
          45,
          48,
          50,
          51,
          54,
          56,
          58,
          59,
          61,
          65,
          67,
          71,
          89,
          99,
          102,
          103,
          105,
          115,
          116,
          119,
          121,
          122,
          123,
          124,
          125,
          127,
          133,
          136,
          137,
          138,
          139,
          140
        ],
        "physical_syndrome": [
          8,
          9,
          11,
          15,
          19,
          21,
          22,
          25,
          30,
          34,
          35,
          36,
          38,
          39,
          40,
          44,
          45,
          47,
          52,
          55,
          63,
          64,
          65,
          66
        ],
        "syndrome": [
          8,
          9,
          11,
          15,
          19,
          21,
          22,
          25,
          30,
          34,
          35,
          36,
          38,
          39,
          40,
          44,
          45,
          47,
          52,
          55,
          63,
          64,
          65,
          66
        ]
      },
      "conclusion": "mixed-sector XOR has no sector-independent effect and is excluded",
      "selected_names": [
        "D:102",
        "D:103",
        "D:119",
        "D:125",
        "D:137",
        "D:59",
        "R:35:0",
        "R:45:1",
        "R:48:1",
        "R:55:1",
        "R:55:2",
        "R:57:2",
        "R:60:0",
        "R:62:0",
        "R:67:1",
        "R:68:0",
        "R:68:2",
        "R:69:0",
        "R:7:2"
      ],
      "x_input_id": "iter42-Xerr",
      "z_input_id": "iter42-Zerr"
    },
    "multiplicity": "all eligible exact-name result multiplicities counted; one semantic predicate retained per novel result",
    "overlapping_pair_decompositions": {
      "per_sector_counts_match_closed_forms": true,
      "policy": "only canonical disjoint split is enumerated"
    },
    "schedule_globalization": {
      "conclusion": "validity is schedule-local; retained terms remain dynamic exact EFSSC predicates",
      "iteration136_verification": {
        "logical_parities": [
          0,
          0,
          0,
          1,
          1,
          0,
          1,
          0,
          1,
          0,
          0,
          0
        ],
        "net_support": [
          8,
          9,
          30,
          47,
          49,
          59,
          102,
          103,
          114,
          123,
          125,
          126,
          132,
          137
        ],
        "net_weight": 14,
        "nontrivial": true,
        "ok": false,
        "selected": [
          59,
          102,
          103,
          119,
          125,
          137,
          167,
          249,
          280,
          289
        ],
        "selected_names": [
          "D:59",
          "D:102",
          "D:103",
          "D:119",
          "D:125",
          "D:137",
          "R:7:2",
          "R:35:0",
          "R:45:1",
          "R:48:1"
        ],
        "syndrome": [
          0,
          14,
          15,
          20,
          21,
          31,
          36,
          42,
          43,
          59,
          61,
          62,
          65,
          69
        ],
        "weight": 10
      },
      "sector": "Xerr",
      "selected_names": [
        "D:59",
        "D:102",
        "D:103",
        "D:119",
        "D:125",
        "D:137",
        "R:7:2",
        "R:35:0",
        "R:45:1",
        "R:48:1"
      ],
      "selector_id": "iter42-Xerr",
      "source_schedule_sha256": "141d7ae068f4342dfb24fd7e37ca08cf2169966cb51d5119218cd70c4dd240b8",
      "source_verification": {
        "logical_parities": [
          0,
          0,
          0,
          1,
          1,
          0,
          1,
          0,
          0,
          1,
          1,
          0
        ],
        "net_support": [
          25,
          30,
          46,
          50,
          59,
          63,
          82,
          102,
          103,
          113,
          119,
          123,
          125,
          129,
          132,
          137
        ],
        "net_weight": 16,
        "nontrivial": true,
        "ok": true,
        "selected": [
          59,
          102,
          103,
          119,
          125,
          137,
          167,
          249,
          280,
          289
        ],
        "selected_names": [
          "D:59",
          "D:102",
          "D:103",
          "D:119",
          "D:125",
          "D:137",
          "R:7:2",
          "R:35:0",
          "R:45:1",
          "R:48:1"
        ],
        "syndrome": [],
        "weight": 10
      }
    },
    "semantic_predicate_dedup": "sector plus exact selected names/data/group fields; all hashes collision-free against 234 inherited selectors and each retained term",
    "support_weight_substitution": {
      "canonical_support_weight": 12,
      "conclusion": "neither canonical nor physical net-support weight may replace named elementary-fault weight",
      "named_location_weight": 10,
      "physical_support_weight": 18,
      "sector": "Xerr",
      "selected_names": [
        "D:38",
        "D:109",
        "R:25:0",
        "R:26:2",
        "R:28:0",
        "R:35:1",
        "R:35:2",
        "R:39:1",
        "R:41:0",
        "R:45:2"
      ]
    },
    "zero_support_and_logical_trivial": "tracked independently for all enumerated quadruples and replayed for every unique weight<=10 result"
  },
  "finite_domain": {
    "coverage_proof": [
      "Every domain member has unique sorted indices a<b<c<d.",
      "The streaming left bucket before c contains exactly every pair a<b<c.",
      "Pairing each bucket row with each c<d emits that quadruple once.",
      "The observed per-sector counts equal C(125,4) and C(109,4); cross-sector and repeated-index tuples are outside the declared domain."
    ],
    "no_sampling": true,
    "sector_counts": {
      "Xerr": 125,
      "Zerr": 109
    },
    "sector_expected": {
      "Xerr": 9691375,
      "Zerr": 5563251
    },
    "selector_count": 234,
    "unordered_distinct_quadruples_enumerated": 15254626,
    "unordered_distinct_quadruples_expected": 15254626,
    "weight_cap_for_candidate_predicates": 10
  },
  "inputs": {
    "candidate_file_sha256": "9596d1456ea66c086c06b4b7b4aaf4e442da9943644ae9839d113f10d937a640",
    "candidate_schedule_sha256": "45051af0b08e6647d50c6fb0535894173016fd013279e7a0eaee8b2e69ee2e44",
    "direct_file_sha256": "f206cb75b7af6cbf2c5421f58c9ebc0c1c0b51d7e44eb3f1c5713a47987a485e",
    "selector_state_sha256": "47792a8f8e757482604723abb0e08916f49b252f4ba07deae03cf4295159d0b6",
    "state_file_sha256": "ba670045a69722f9625d04d3f07d62e207db38f15e9323f8c32d89194bb585cd"
  },
  "retained_term_count": 0,
  "retained_terms": [],
  "schema": "circdist-round96-exact-order4-same-sector-gf2-closure-v1",
  "seconds": 60.83836,
  "sector_results": {
    "Xerr": {
      "all_pair_pair_decompositions": 30027375,
      "canonical_disjoint_pairing_retained": 9691375,
      "canonical_left_pairs_final": 7503,
      "canonical_logical_trivial_results": 3176,
      "canonical_source_valid_quadruples": 0,
      "canonical_support_weight_histogram": {
        "2": 6,
        "4": 488,
        "6": 7954,
        "8": 23482,
        "10": 11,
        "12": 119,
        "14": 1104,
        "16": 6204,
        "18": 23282,
        "20": 67300,
        "22": 157539,
        "24": 287822,
        "26": 416000,
        "28": 499669,
        "30": 515488,
        "32": 538855,
        "34": 597384,
        "36": 721163,
        "38": 867499,
        "40": 977233,
        "42": 1002690,
        "44": 924514,
        "46": 756053,
        "48": 548463,
        "50": 355300,
        "52": 206118,
        "54": 107607,
        "56": 49980,
        "58": 20940,
        "60": 7685,
        "62": 2440,
        "64": 770,
        "66": 183,
        "68": 25,
        "70": 5
      },
      "canonical_syndrome_zero_results": 0,
      "conservative_logical_action_histogram": {},
      "conservative_source_valid_quadruples": 0,
      "eligible_weight_1_to_10_with_multiplicity": 32456,
      "enumeration_checksum_mod_2_256": "7995964f26ce16be693f5c459427c10855bd904cade6bd8279b47c2a75f7576c",
      "location_weight_histogram": {
        "3": 4060,
        "4": 27405,
        "8": 1,
        "9": 62,
        "10": 928,
        "11": 47,
        "12": 591,
        "13": 409,
        "14": 4684,
        "15": 3203,
        "16": 29767,
        "17": 21593,
        "18": 157484,
        "19": 83707,
        "20": 600667,
        "21": 184489,
        "22": 1368990,
        "23": 302,
        "24": 6199,
        "25": 1671,
        "26": 24030,
        "27": 6795,
        "28": 73346,
        "29": 22801,
        "30": 201730,
        "31": 70501,
        "32": 522125,
        "33": 154424,
        "34": 1112377,
        "35": 236402,
        "36": 1757411,
        "37": 241136,
        "38": 1745328,
        "39": 120802,
        "40": 905908
      },
      "maximum_multiplicity_witness_names": [
        "R:0:0",
        "R:0:2",
        "R:38:0"
      ],
      "maximum_result_multiplicity": 1,
      "multiplicity_histogram_for_unique_eligible_results": {
        "1": 32456
      },
      "noncanonical_disjoint_pairings_excluded": 19382750,
      "novel_miss_reasons": {
        "canonical_nonzero_syndrome": 32456
      },
      "overlapping_pair_decompositions_excluded": 953250,
      "physical_logical_trivial_results": 3176,
      "physical_source_valid_quadruples": 0,
      "physical_support_weight_histogram": {
        "2": 7,
        "4": 454,
        "6": 2763,
        "8": 6759,
        "10": 9439,
        "12": 8264,
        "14": 4864,
        "16": 5559,
        "18": 16909,
        "20": 44375,
        "22": 97660,
        "24": 178640,
        "26": 278713,
        "28": 378227,
        "30": 469570,
        "32": 545238,
        "34": 608771,
        "36": 681512,
        "38": 772592,
        "40": 864771,
        "42": 921530,
        "44": 917987,
        "46": 840338,
        "48": 705042,
        "50": 533564,
        "52": 363385,
        "54": 220109,
        "56": 119135,
        "58": 57679,
        "60": 24545,
        "62": 8968,
        "64": 3000,
        "66": 812,
        "68": 151,
        "70": 37,
        "72": 6
      },
      "physical_syndrome_zero_results": 0,
      "retained_terms": [],
      "selector_count": 125,
      "unique_eligible_named_results": 32456,
      "unique_eligible_replayed": 32456,
      "unique_existing_predicate_results": 0,
      "unique_novel_conservative_source_valid_retained": 0,
      "unique_novel_eligible_results": 32456,
      "unique_novel_source_valid_counter": 0,
      "unordered_distinct_quadruples_enumerated": 9691375,
      "unordered_distinct_quadruples_expected": 9691375,
      "unordered_pairs": 7750,
      "zero_canonical_support_results": 0,
      "zero_location_results": 0,
      "zero_physical_support_results": 0
    },
    "Zerr": {
      "all_pair_pair_decompositions": 17319555,
      "canonical_disjoint_pairing_retained": 5563251,
      "canonical_left_pairs_final": 5671,
      "canonical_logical_trivial_results": 7397,
      "canonical_source_valid_quadruples": 1,
      "canonical_support_weight_histogram": {
        "2": 1,
        "4": 57,
        "6": 450,
        "8": 585,
        "10": 63,
        "12": 399,
        "14": 1214,
        "16": 3427,
        "18": 8047,
        "20": 17118,
        "22": 36851,
        "24": 67574,
        "26": 107089,
        "28": 144615,
        "30": 189768,
        "32": 260876,
        "34": 369173,
        "36": 509543,
        "38": 647701,
        "40": 735087,
        "42": 733142,
        "44": 637183,
        "46": 479199,
        "48": 310107,
        "50": 171355,
        "52": 81035,
        "54": 33749,
        "56": 12360,
        "58": 3885,
        "60": 1146,
        "62": 330,
        "64": 91,
        "66": 21,
        "68": 6,
        "70": 3,
        "74": 1
      },
      "canonical_syndrome_zero_results": 1,
      "conservative_logical_action_histogram": {
        "100110100011": 1
      },
      "conservative_source_valid_quadruples": 1,
      "eligible_weight_1_to_10_with_multiplicity": 1304,
      "enumeration_checksum_mod_2_256": "a7b44ab8479c13e64304bb8e4a023e9b17c38b570eabcdf8f3ebdff284c3862e",
      "location_weight_histogram": {
        "3": 286,
        "4": 715,
        "7": 15,
        "8": 92,
        "9": 18,
        "10": 178,
        "11": 150,
        "12": 434,
        "13": 338,
        "14": 1116,
        "15": 2219,
        "16": 6025,
        "17": 8465,
        "18": 26120,
        "19": 26651,
        "20": 98292,
        "21": 58993,
        "22": 216163,
        "23": 2576,
        "24": 7864,
        "25": 6525,
        "26": 21274,
        "27": 18498,
        "28": 56091,
        "29": 47753,
        "30": 152139,
        "31": 104596,
        "32": 364315,
        "33": 192411,
        "34": 725370,
        "35": 255106,
        "36": 1087862,
        "37": 226443,
        "38": 1141612,
        "39": 112123,
        "40": 594423
      },
      "maximum_multiplicity_witness_names": [
        "D:13",
        "D:14",
        "D:15",
        "D:71",
        "D:72",
        "D:74",
        "D:79",
        "R:11:1",
        "R:12:0",
        "R:15:0"
      ],
      "maximum_result_multiplicity": 1,
      "multiplicity_histogram_for_unique_eligible_results": {
        "1": 1304
      },
      "noncanonical_disjoint_pairings_excluded": 11126502,
      "novel_miss_reasons": {
        "canonical_nonzero_syndrome": 1198
      },
      "overlapping_pair_decompositions_excluded": 629802,
      "physical_logical_trivial_results": 7397,
      "physical_source_valid_quadruples": 1,
      "physical_support_weight_histogram": {
        "2": 2,
        "4": 38,
        "6": 116,
        "8": 251,
        "10": 322,
        "12": 359,
        "14": 480,
        "16": 1081,
        "18": 2676,
        "20": 6064,
        "22": 12936,
        "24": 26069,
        "26": 48301,
        "28": 79745,
        "30": 116278,
        "32": 160263,
        "34": 220921,
        "36": 303068,
        "38": 405879,
        "40": 514724,
        "42": 602110,
        "44": 645105,
        "46": 634097,
        "48": 562209,
        "50": 452553,
        "52": 326092,
        "54": 212628,
        "56": 123067,
        "58": 62141,
        "60": 27836,
        "62": 10579,
        "64": 3650,
        "66": 1200,
        "68": 315,
        "70": 72,
        "72": 17,
        "74": 7
      },
      "physical_syndrome_zero_results": 1,
      "retained_terms": [],
      "selector_count": 109,
      "unique_eligible_named_results": 1304,
      "unique_eligible_replayed": 1304,
      "unique_existing_predicate_results": 106,
      "unique_novel_conservative_source_valid_retained": 0,
      "unique_novel_eligible_results": 1198,
      "unique_novel_source_valid_counter": 0,
      "unordered_distinct_quadruples_enumerated": 5563251,
      "unordered_distinct_quadruples_expected": 5563251,
      "unordered_pairs": 5886,
      "zero_canonical_support_results": 0,
      "zero_location_results": 0,
      "zero_physical_support_results": 0
    }
  },
  "soundness_theorem": {
    "does_not_prove": "No-go counts outside retained positives do not exhaust arbitrary mechanisms, mixed-sector combinations, repeated-selector algebra, closure orders other than four, or schedules other than the tested source; no D* branch closes.",
    "statement": "Within one fixed CSS sector and one frozen schedule, each named location is a GF(2) column. The sum of four selector name sets is their exact symmetric difference. Replaying that distinct-name set proves its actual named weight, canonical and physical support, detector syndrome and logical action. A novel result is retained only when weight is 1..10, both syndromes vanish, both logical actions are equal and nonzero, and its dynamic outer antecedent holds on the source schedule."
  },
  "status": "PASS",
  "strategy": "exact streaming meet-in-the-middle over canonical disjoint pair split (a,b)|(c,d) with a<b<c<d"
}
```
