# CIRCDIST Gross round-72 generalization: fresh independent exact review (round 73)

Date: 2026-08-29  
Reviewer role: fresh, independent, exact, rebuttal-first reviewer  
Reviewed package: `circdist/artifacts/circdist_gross_round71_generalization_round72_20260829`  
Package seal file SHA-256: `bc2bf8bdc2da199e348b0471ef4f0367e52e1a7e5eefe1294adb51ab25a4f7f6`  
Final verdict: **CLEAR-PROPOSER-LEVEL-CONTINUATION**

## 1. Verdict and exact scope

I found no material defect in the round-72 positive-witness generalization or in its twelve new exact CEGAR iterations. I independently reconstructed the frozen Gross incidence, the 48 nested round-71 source mechanisms, all 113 participating local-order catalogs, all 607 conservative pair relations, all 48 selected-mechanism multi-check relations, the 696-candidate semantic ledger, every tuple covered by every retained term, and iterations 30--41. The load-bearing clean-room run passed without importing the proposer's `verify.py`, `generalize_round71.py`, `round63_src/model.py`, or any other proposer Python module.

This verdict licenses only the following dispatcher action:

1. link the sealed round-72 package and this review as **proposer-level** evidence;
2. make the minimum Gross-node summary, frontier, and event update needed to record that evidence;
3. continue the exact workflow in a fresh process at outer iteration **42** with exactly **6,850** installed blocks: 1,440 reviewed unary blocks + 20 round-62 blocks + 4,740 reviewed round-69 generalized blocks + 566 round-72 generalized blocks + 84 exact dynamic blocks; and
4. keep the 15,874 exploratory round-63 pair clauses at installed count zero.

It licenses **no** claim rewrite, route change, level change, repair entry, outer-exhaustion claim, physical-absence inference, or narrowing of `D*_Gross in {11,12}`. `CIRCDIST.gross` remains `CONJECTURED`.

### Findings ledger

| ID | Disposition | Finding |
|---|---|---|
| F1 | clean | The 1,492-file package is sealed by 1,491 checked entries; every physical file, every gzip member stream, and every regular tar member was read. |
| F2 | clean | Forty-eight source assignments satisfy all 1,072,768 source DIMACS clauses and replay through the independently rebuilt 360-column maps to valid physical mechanisms of fault weight at most ten. |
| F3 | clean | The 113 x 720 catalog, 607 pair relations, and 48 exact multi-check DPs reproduce the sealed objects exactly. The multi-check proof treats all participating checks jointly; it never assumes pair independence. |
| F4 | clean | The 696 new candidates classify as 85 duplicate-new, 45 dominated-new, zero duplicate-old, zero dominated-old, and 566 retained; the reviewed 4,740 old terms are preserved byte-for-byte. |
| F5 | clean | Every one of 32,031,216 retained tuples has an explicit raw physical selector: 5,074,416 pair tuples and 26,956,800 multi-check tuples. All 48 source mechanisms have a retained cover, and all 48 source exact blocks remain. |
| F6 | clean with mandatory limitation | Three explicit attacks show a zero conservative pair cell can coexist with a valid ten-fault multi-check physical mechanism. Positive-library misses and deletion controls cannot support absence. |
| F7 | clean | Iterations 30--41 have exact fresh-process outer formulas/models, 12 legal compressed globally interleaved schedules, and 24 independently rebuilt complete direct-360 SAT formulas/assignments/raw replays. |
| F8 | administrative drift, non-material | The requested author command with live `--repo-root` fails only because the scheduler advanced after sealing to settle round 72 and authorize this review. The other seven frozen bindings are byte-identical; offline author full verification passes. |

## 2. Independence, read boundary, and sealed inputs

I did not contact the round-72 author, create a sub-agent, import proposer code, edit the package, or use the author's verifier as an independent proof. All independent code, environments, logs, reconstructed formula text, and candidate installations were confined to `/tmp/circdist_r73_exact_review_20260829` and deleted after the final review copy. Path, byte-count, and digest records below make those ephemeral materials publicly bindable without retaining scratch state. The only permitted repository write is this review.

No `AGENTS.md` exists in or above the repository. I read `DAG_PROTOCOL.md`, `FILE_PROTOCOL.md`, the complete current scheduler, the frozen Gross problem statement, the Gross node, the sealed round-69 package, the round-70 review, the sealed round-71 package, and every physical file in round 72. The required live text bindings were:

| object | bytes / lines | SHA-256 |
|---|---:|---|
| `DAG_PROTOCOL.md` | 15,377 / 283 | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | 8,523 / 166 | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| current scheduler | 160,007 / 2,080 | `b183b1231826d7827caca507cf96d96c3688d14c533541cd022c0f98fcbdaf39` |
| frozen Gross problems | 10,199 / 243 | `5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64` |
| pre-review Gross node | 35,885 / 510 | `b62d580cd89f6bfa7c0d93112446f7aaf142bba7b2bd0d917134d230985964bf` |
| round-70 review | 36,570 / 792 | `b2fe38fd6adb1ef974624a49b84b7a61620a5c97a531155aac01fc39dbfbaabe` |

The independent streaming reader was 57 lines / 2,814 bytes, SHA-256 `bfedfef6ea9375478e7b08e5721a6f5c5639c2bb2ee90fcbd895c7e057db6c5b`. It hashed the path and content of every physical file, decompressed every `.gz`, and opened each gzip-compressed tar source archive to read every regular member. Results:

| package | physical files / bytes | gzip files / uncompressed bytes | tar archives / regular members / bytes | physical stream SHA-256 | gzip stream SHA-256 | tar stream SHA-256 |
|---|---:|---:|---:|---|---|---|
| round 69 | 250 / 19,557,352 | 112 / 193,419,638 | 2 / 472 / 10,469,303 | `e8c39fbff986fe9d01d69293df671609a28e98795c046ded62d73e09bc371625` | `c799bb03f61727640492eee5e035475af4214a36d6b46242fb5857ebf6eee5fe` | `d139f2c9b69b3f767e560402425aff9a381a0903eaac8a3a1fbb5973708fd66a` |
| round 71 | 794 / 35,756,404 | 414 / 386,906,559 | 2 / 472 / 10,469,303 | `9654cfad880b94f99114300c58b41165c30748c5217478389cfe13a96a0fdc64` | `850602b780f9d00c14a77589f1f72908cab02ac2c77cf5eb3b2db229ba009fcd` | `d139f2c9b69b3f767e560402425aff9a381a0903eaac8a3a1fbb5973708fd66a` |
| round 72 | 1,492 / 77,257,267 | 742 / 1,107,066,644 | 4 / 944 / 20,938,606 | `1391be1cfdd25c85745a7d135186f58372d8cd036fa0bd707379a0e00515428b` | `faa26521a46e4e737160c75a8febcc269d91b8f002ed3df57eb7847e33af4304` | `0a551ae4ef14300c29eb8966d0292772130d9e94260b9641066def57ce7d2a52` |

There were zero read, gzip, or tar errors. The detailed read ledger SHA-256 is `16e114a955395ba402e1b0be6dfffc6ee94de2029cfc67b740bb34e37772b528`.

The package contains 1,492 physical files: `SHA256SUMS.txt` plus 1,491 sealed paths. Its seal file has exact SHA-256 `bc2bf8bdc2da199e348b0471ef4f0367e52e1a7e5eefe1294adb51ab25a4f7f6`; `shasum -a 256 -c` returned zero with 1,491 `OK` lines. The check log has SHA-256 `f995a665cbc771a1c126176798d24c2276ac20cc983f4d3d1cddaeced46c57c4`.

## 3. Exact dependency environment and author verifier

The fresh Python 3.9.6 environment froze to:

```text
numpy==2.0.2
python-sat==1.9.dev15
six==1.17.0
z3-solver==5.1.0.0
```

The freeze SHA-256 is `e5ace88d19150ff07d84704ca6e9f4a4a070c2f588a6502e4ca0bfe99ebf6ee6`.

The exact requested author command, `verify.py --full --repo-root <live-root>`, ran in the foreground with a 2,400-second hard limit. It returned 1 after 1.383428 seconds, with no timeout or signal. The only assertion was the byte comparison for `operations/circdist/SCHEDULER.yaml`. An independent eight-binding comparison found seven exact matches and one scheduler drift:

- sealed scheduler: 156,423 bytes, SHA-256 `bc47e7d6fdea0da1215a9e20dabd567bec4e3256dbeca115dc1bffa2669c7c99`;
- live scheduler: 160,007 bytes, SHA-256 `b183b1231826d7827caca507cf96d96c3688d14c533541cd022c0f98fcbdaf39`;
- unified diff: 70 additions, 24 deletions. It settles round 72 and adds the round-73 authorization, budget, action, ranking, and round-log entry. It does not alter a mathematical input.

The binding-drift ledger SHA-256 is `a1c55022bb01b82c46288613f347f1636b21b07303d72928e0088f8d6f09873b`; the diff SHA-256 is `7ce4fcb139a230227b471d7941668a2ab5ba4e8b17fcc454a82ae1fbd2b6c17e`.

The author's self-contained `verify.py --full` then returned zero after 1,289.634159 seconds, with no timeout or signal. Its 267-line output SHA-256 is `bd54266550f619110ef2bfe813ea3a1e8e13d82b515c1dbf26fa06fde2e2fb2b`. I treat that only as a proposer self-consistency cross-check. Everything from Section 4 onward comes from the non-importing clean-room checker or direct external proof checkers.

## 4. Clean-room checker and frozen Gross reconstruction

The final checker is 863 lines / 64,853 bytes, SHA-256 `d9bfdb2652dd590efb6e4ef3fcef2529e3d6a4613a308672531a9bae84a70e34`. The load-bearing full run returned zero in 233.579914 seconds under a 3,600-second foreground process-group hard limit, with no timeout, SIGTERM, or SIGKILL. Its result/log is 16,530 bytes, SHA-256 `66e03ea258660b7f9a747eb815fd319e174b6afb205cd644f2772af06090e778`; its canonical content-before-self-hash is `69879e6f44811513cfe969fb9c858c14fe75fb0d636a7fa8200c969fc25ef97c`.

Let `G = Z_12 x Z_6`, indexed by `g(i,j)=6i+j`, with two 72-qubit halves. From the frozen polynomials

```text
A = {(3,0),(0,1),(0,2)},   B = {(0,3),(1,0),(2,0)},
```

the checker constructs

```text
X_g = {g+a : a in A} union {72+g+b : b in B},
Z_g = {g-b : b in B} union {72+g-a : a in A}.
```

This gives 72 X rows and 72 Z rows, every row of weight six; 864 distinct named CNOT edges; 648 X/Z row pairs with overlap two and 4,536 with overlap zero. Direct GF(2) elimination gives `rank(H_X)=rank(H_Z)=66`, all X/Z dot products zero, and `k=144-66-66=12`. The incidence hash is `7a4da6730b72a3fc74767cec949808d33ac451e4287c89db9f4c309b991f4102`.

The checker parses the frozen weight-12 seeds, translates each over all 72 group elements, removes stabilizer words, and verifies detector orthogonality and weight. Both exact pools have 1,884 words. Their canonical hashes are X `48778b0e1ec5df722305b2f8a8eade3750a4d5480dfb595149b8844a1a162c8a` and Z `a3f568f88a1702e2d02b30f29a1363bc820bfaaf8e7a05ea87d7b05ba068e147`. Incremental quotient-rank selection produces twelve logical representatives in each sector.

For a hook check with earliest-first local order `o=(q0,...,q5)`, the three canonical representatives and physical suffixes are

```text
R0(o)={q0,q1},       P0(o)={q2,q3,q4,q5},
R1(o)={q3,q4,q5},    P1(o)=R1(o),
R2(o)={q4,q5},       P2(o)=R2(o).
```

For kind zero, `P0 xor R0` is the full stabilizer row; for kinds one and two the representatives coincide. Therefore canonical and physical detector/logical signatures agree in all three cases. Together with 144 singleton data columns this reconstructs exactly 360 physical columns per sector. Primary DIMACS variables 1--360 map to these columns, never to auxiliary variables.

## 5. Forty-eight source formulas, assignments, and raw physical mechanisms

For each iteration 6--29 and each sector, the checker starts from the nested sealed round-71 candidate schedule, direct CNF, complete solver assignment, column dictionary, and raw witness. It does the following without invoking any proposer parser:

1. parse the DIMACS header and every clause, requiring the declared variable/clause counts and in-range literals;
2. parse one complete SAT assignment, requiring every variable `1..n` exactly once;
3. evaluate every clause under that assignment;
4. take only true variables among 1--360 and map each to its independently rebuilt physical column;
5. recompute local order from named schedule times and require the stored canonical and physical suffix supports to match the formulas above;
6. XOR all selected canonical supports and, separately, all physical supports;
7. require fault count at most ten, zero detector syndrome in both representations, equal nonzero twelve-bit logical parity, and non-membership in the corresponding stabilizer span; and
8. regenerate the order atoms, candidate/formula/assignment bindings, and mechanism hash, then compare every field with the sealed ledgers.

All 48 assignments pass all 1,072,768 clauses. Fault weights are forty at weight ten and eight at weight nine. Canonical net weights range from 12 to 20; physical net weights range from 12 to 22. The ordered mechanism-hash stream is `e16be4a915b52470acb95b485ff0c5db044de4cb38cd8ed3d9e871f16e5b6b99`.

The following table binds every source formula and mechanism. `C/P wt` is the independently recomputed canonical/physical XOR weight; `checks` counts distinct residual checks; `retained covers` is the number of retained antecedents true on that exact source order.

| mechanism | faults | C/P wt | checks | source atoms | retained covers | CNF vars/clauses | mechanism SHA-256 | CNF SHA-256 |
|---|---:|---:|---:|---:|---:|---:|---|---|
| iter6-Xerr | 10 | 18/12 | 7 | 60 | 14 | 5996/22564 | `8ff5b5c0ff24d9751b65b1b4fe499f0749cf61c4e7d7924f0ff7f9f84e64175d` | `e9cddd258743bd80a2d4a007d0198239dbc0ee51cf8f30778ea96f2ba960eb90` |
| iter6-Zerr | 10 | 14/16 | 7 | 63 | 36 | 5962/22428 | `e589e8098815be1f87d633094af4faea00605e93b425d9e48581e0f03c933aa7` | `bbbfb5e9ea20c3b0701d7aed62c8e1465e01a1f5deb173c626f2c7ea5727e91d` |
| iter7-Xerr | 9 | 16/16 | 7 | 62 | 35 | 6005/22600 | `fe5a809b938aaa481822b32ff8682964dcc11b48aba9fcbbe5628ff378ab3d69` | `29a690fe79bccf6bd0828255a4b13e421b61e441681827e4aa8a969f4e5f7f9e` |
| iter7-Zerr | 10 | 14/18 | 9 | 76 | 44 | 5960/22420 | `cb56cc4ea2810f6530e2dc9db8503b3f0e408e956b056aed23db49c19855c4ea` | `a30d397a4160a839d2772954f43819f6d01ce20df759b8775700f9fd7567ecc4` |
| iter8-Xerr | 10 | 14/14 | 3 | 25 | 2 | 5984/22516 | `b7915a64bb397e42e354f0daf551b2db40139a9e7dd43b2e1a829261f26e9a0f` | `795e1e29b381aa65e6c258d8ea195758d7c4a021771bf18d236e260f399d8167` |
| iter8-Zerr | 10 | 14/14 | 4 | 34 | 4 | 5961/22424 | `04c07c6906ae16ab91f3c4d8681eb1bc596e24b78a23393114ec9fc25c0ec3b4` | `d0f323040246a423bc5dd9d5f05363d377c9d3065e3b1cafeaa43fab578ce747` |
| iter9-Xerr | 10 | 16/20 | 7 | 57 | 11 | 5999/22576 | `582c69633c0c407bdb0359abfd0ddabee35163ff7caf7fece695f072fa6701bd` | `3ebec07026d424a961d9edb5f57cbfbdbfda7d324b189a85d57a3a2b2bb6fffd` |
| iter9-Zerr | 10 | 12/12 | 4 | 35 | 5 | 5961/22424 | `2f1727c1e1545ce467e492b87e51f709329c030f7109aa12636549bddc45076c` | `ef304762c237f6fda025c676f70d2b16bd89da21c8074a44c43382007cae0e02` |
| iter10-Xerr | 10 | 12/12 | 2 | 16 | 1 | 5998/22572 | `72ff01e7da1274285796e8e3210d938057e03d1f2a0dfb571e36b07cfa86e1c5` | `f464e4c77ef8ac6ede60a4246109f80c25993a565d1218e93c5539acde76510a` |
| iter10-Zerr | 10 | 20/16 | 7 | 66 | 34 | 5964/22436 | `40a88cca8af3d87668a3e89e50e1df84d82a799beedef97c37178ead626b2b36` | `30b0c6dbdf4fe0f99120fb8c61e8ce7faf37f703ea3e14607ea9228b050fff45` |
| iter11-Xerr | 10 | 16/20 | 5 | 46 | 1 | 5994/22556 | `3a747926e53794ce98657cb4e2318384a3c6091d5f0dc424354d8f7acec7e7c8` | `8b5b52d725f8f3a170a6957cd9ba32fd5c79bfc82abcbda97295c7cb00c88375` |
| iter11-Zerr | 10 | 16/16 | 5 | 41 | 8 | 5964/22436 | `ddf63e2f4c47658e0faabc81a4314bf660fdfce5b757d2db30254c62e1f549cf` | `c232a0209ed08cf98b4d62de4326714a345deda2ba58ac63169f06aed208d9bb` |
| iter12-Xerr | 10 | 16/12 | 9 | 76 | 34 | 6003/22592 | `fa4fa770f1e4d22ad4da8a818f091a062ccb38c5d841d60e835823edf4cfb10b` | `abdf1e5a193834277dcb89e7cb5ecd808f23c63ff90ee9dd0856f32398744a63` |
| iter12-Zerr | 10 | 14/14 | 6 | 48 | 24 | 5964/22436 | `7b1788474e127401ac76388f5372d5542037788f76305dc09e29c90a68d9fd44` | `82112b2c31f63121ae907d84619c66c4c531b762aab7758504da84fb7df7622f` |
| iter13-Xerr | 10 | 20/18 | 8 | 72 | 18 | 6001/22584 | `a5fbf65782097dd7bed2c9271b64303e67176bbeb04322574712e27d471f25ee` | `e60ffabb3a20fdf382c45696a396b9e96ad70d3f2479523f3849616e43f2fdd7` |
| iter13-Zerr | 10 | 12/12 | 6 | 53 | 6 | 5954/22396 | `696301848389a3f1adb73f308a3d17dc4cf97e0c8f332a12a9bbb7bb215b01b3` | `f32000806bffe33ee2f348042ce348a68a5e3543a8465b733075d8d488c33e5e` |
| iter14-Xerr | 9 | 16/20 | 9 | 72 | 28 | 5988/22532 | `40b5920f0c46d28f7fea74eea0ca953a6e349f9f03944ef3d84edecbab28d9f3` | `e24eed8ddc654a66202d123645a720d17053c22380c70cceb85c91ec50909c91` |
| iter14-Zerr | 9 | 14/16 | 5 | 40 | 14 | 5957/22408 | `e1e33d5cd13a51a78234c52300bde5b87102ba0bf9b3048a5592d778800e6b64` | `211f710bd45400ec663c8dbf669ce197015e7c9dd314ab792f23927bc7ee280a` |
| iter15-Xerr | 10 | 12/12 | 3 | 25 | 2 | 5931/22304 | `d14a28144f9a4459a75ca8f2b145d0ae9ecdc41cf7ba4a70dc725198fda5f93d` | `08d8cfdd3f4f4b9b2b9425bd74a586e131c93afabd571aaf22dce2a278e954f4` |
| iter15-Zerr | 10 | 12/20 | 9 | 76 | 22 | 5926/22284 | `679e3b978e3fd9aeb9a21fc3b9a2ac3b333c4889893780fec79708003aa452ac` | `2f4ab4424ae85989fdd4ef71d3f2851b7e1cfed2b9582cc3b080b0d93eeb796e` |
| iter16-Xerr | 10 | 18/14 | 6 | 53 | 4 | 5912/22228 | `fcaa320e9891087228ff1909ce6f3028e4dc35806af24094cfbc14d08dfbd537` | `d7ba4c9d998f605e844ceed501ed85bd55081527d2a66f523a198a15a66e9d58` |
| iter16-Zerr | 9 | 14/14 | 6 | 52 | 30 | 5906/22204 | `24b44bb113cd608787ebd6b1e39f87117f9fb9c53ba4200f0ea99a9ec07dd181` | `f02bd5a4ac4a3c7a52aa03230cc678f2b1e5bbca63e9e63e701e93061928ac3a` |
| iter17-Xerr | 10 | 14/14 | 4 | 34 | 1 | 5975/22480 | `f1605d8562cea607dbc5a2ef2a2b9f97d66884c7f95ad62918a777e1adf435e6` | `da042eca1811fd2ecb89b8b56ebb3eb84195e622cde35269e2e29a1c54241acf` |
| iter17-Zerr | 10 | 18/18 | 6 | 61 | 12 | 5915/22240 | `1814b34de362553c9c5306be926fc220169581b773d963f791c4dae2039e03a4` | `72bb0a86f587047b477ce8240e9ceea8dd6255c8338256214becc77c6dfa902c` |
| iter18-Xerr | 10 | 12/14 | 2 | 16 | 2 | 5974/22476 | `1ca88f054f4709f164fe94e41be9b90045e5aca57b676a6dd04e0734a918a65f` | `0c3588ee9fdc673575d31005a05ac7c26a997df3591ce089cf6964864f3be739` |
| iter18-Zerr | 9 | 12/16 | 5 | 42 | 6 | 5918/22252 | `d03b978f018c29881dfe3b936e63e04672811a43e94fc2594305f7f1440a3ce6` | `2f132e3c9ebfdbea609e68cb273159d94ad82a9e4ef5fa2e85b1c1e157c3864c` |
| iter19-Xerr | 10 | 14/14 | 3 | 25 | 1 | 5971/22464 | `5898eb87770a5241bf1d2c0f0d1ab998dc06ef24c27843338814918665fd9b90` | `f217fa3bc43df8e25b3abf9e79908de00c74d1c3fb06ee082e6564c6d35fe6b4` |
| iter19-Zerr | 10 | 20/16 | 7 | 66 | 36 | 5908/22212 | `f57f1a31970f8b196d879dcf72efdc1c94bbed56e847820c6682bd66b585dfa1` | `c12cd968e8283f349e51d77b22c3e202364883cbae6332748ff59346ed1b45e3` |
| iter20-Xerr | 10 | 12/18 | 8 | 64 | 26 | 5924/22276 | `697282edea5b7a32f524d5491df8189179b253fd383c577c8d478ffcb9b2fd35` | `1a6ca126c8597dcb0109908181c5967541801db6ed21414961556f40d31988ad` |
| iter20-Zerr | 10 | 12/14 | 2 | 16 | 2 | 5895/22160 | `20ac9eb5673d87ccd321fee09483afb144d45ef147ddb1f890d6c854b4467c66` | `eec7d9292dd241d1331b2ae5604c11835ffb19312cbe4e78228e1d67b42603cf` |
| iter21-Xerr | 10 | 20/12 | 8 | 70 | 37 | 5974/22476 | `4536dc910b35d83ca5bf19892dd85bb6b8f4f5ff0231d2069c485130b1df5b73` | `1a6b8abcc3caee8bc2b3ed88b0f75b7f025b363209c19842d9e77cbc3379283f` |
| iter21-Zerr | 10 | 12/16 | 2 | 16 | 4 | 5905/22200 | `a1d8c7ac12a95b5e50f7b02bbc3c09b8e979178c84511a60bc386a3d07a849f3` | `27b547c3d519b1bcba0d9c4e750a43532d0626fa353436afc61622831be6c694` |
| iter22-Xerr | 9 | 12/12 | 6 | 55 | 20 | 5958/22412 | `383e8ced40b4225fa494fe8b9b0bf3c4114d3655def784fcc1fcb3ca87ddf5d6` | `1fa0bc50c98d150736c645601089ae9d8448d42d765b6578cd1755cc29bd91ca` |
| iter22-Zerr | 10 | 18/22 | 8 | 72 | 22 | 5904/22196 | `1623ecc12cfd4e43044d92814a19bd528178fb821cdf313b0b56e38a48130dcb` | `662a265c9f301023f329ed3eb5579dcc6ccd7ab7472536e99b724d6461803904` |
| iter23-Xerr | 10 | 16/14 | 6 | 51 | 6 | 5908/22212 | `1410753ae7437c1cd225324a6c9b7f138a2adc2325bae5102308236607811370` | `74f28cb4edfcb4d8008fb28279b6a1e466c0dc0cba59554ef3cb8386a4d2ab19` |
| iter23-Zerr | 10 | 12/12 | 6 | 48 | 10 | 5904/22196 | `729b58d4690468a21045f53bc2dc972618dd949c82920e06d6d3a6039af3f28a` | `5919eebb4ed8dc63249f755c396c95969a1c314e83d42944053c83d2a82e3206` |
| iter24-Xerr | 10 | 14/12 | 4 | 35 | 5 | 5946/22364 | `568310d31dd6c9a27d8fe6a42e574fa39cf424c84fbd629fc05c076493161aab` | `23bd5150926a91ae765b19814df67bdda9eef72f27e798d805e6d2784673ac17` |
| iter24-Zerr | 10 | 12/14 | 2 | 16 | 2 | 5884/22116 | `0e97f1621162b07d2b517010ac80d0fed01974877660926998cad707bd882c77` | `8b93886c36a7dea7b2bab5c5749d62b7f64318afd36c4391e182877608c080e3` |
| iter25-Xerr | 10 | 18/16 | 7 | 66 | 17 | 5964/22436 | `e8f9bbd819fcf50cad316128d6bdef4fc3544ce8190d5e9dbb5657cceb8aecd7` | `47155e0f181a97ce7fe41893323920e2d48c8d161a14c6118a0686ce23ef8907` |
| iter25-Zerr | 10 | 18/16 | 7 | 68 | 34 | 5890/22140 | `4ee19658f6b9b3ff719bb02da5034787b5dc94a52baf715f037d9bf4d6c57956` | `625ea3c5316328b68b649b941e495a4a33798e237bd16e9e5eb0d639d7933bd6` |
| iter26-Xerr | 9 | 18/14 | 6 | 52 | 12 | 5899/22176 | `6fdfd20302f319307b033911065d3988cefe47bd88d73f7a97e760069fa6eda7` | `29f7e436bed3ae68792aa8781f267f19f18fd0cdad82e952b8e58227ccc75d94` |
| iter26-Zerr | 10 | 20/16 | 7 | 68 | 32 | 5859/22016 | `8c0ef0e237c4f0f28c2d0da90bb7ab94f033269a9bb5a383807b1494caf35d1b` | `4eabdd8a8a157cfbae70cfe5d582c3b09600034478c874e6dcbe14cdb297a198` |
| iter27-Xerr | 9 | 14/12 | 7 | 64 | 16 | 5982/22508 | `cc0ea12e6239816f78221aca2684bc11bc5706be7ab5bff603ea455351d3cf8f` | `293fd4a81c2edbc28ff29334f2fad97da9b68ad20d7fed9490a560794079a00f` |
| iter27-Zerr | 10 | 12/16 | 6 | 48 | 20 | 5880/22100 | `82a1a65b9f923c5d96b86bf65eeff7a654883ca497e5c529b14bddd860ffd1be` | `da72ffa72b9ac333aecb13a18f497187fc63d74cac51503fcc34ac5bd78df66d` |
| iter28-Xerr | 10 | 14/12 | 5 | 44 | 15 | 5911/22224 | `4c4d8023becbb556bbe970dd02f8a4373077f877389111b6e5d6007e5453cdef` | `13cd29ba11d11693bc494ad518a241ee43309cc3d292ef62ac856e8c54eb9905` |
| iter28-Zerr | 10 | 14/20 | 9 | 76 | 16 | 5861/22024 | `09b09db33000ea4fafd89584306e87f47516a87b0b08328576f3093ba4548a85` | `fc29bd179ad1fcd8c6a3bdfe1226ca203de46e26bf67b3575de85c6c00f56811` |
| iter29-Xerr | 10 | 16/22 | 5 | 41 | 2 | 5968/22452 | `cb8dbcbc55d8f4270dd37cd797ae4f223808b50341620d0ae7ac3ddc36f60317` | `7e7e460f81290d681c634e9ea1d0e0459b82ff22ffac320ff07f308c6205b793` |
| iter29-Zerr | 10 | 12/20 | 6 | 54 | 20 | 5865/22040 | `54621d5fe9058658ea39db2b1a2f4e3d6ffdd27caca5554f4653878410a251f9` | `faab67b674e51f2a3646ba79f0c9b587fd0ed551b6f3d289024674773fb144eb` |

## 6. The 113 x 720 catalog

The 48 mechanisms involve 113 distinct `(sector,check)` catalogs. For each, the checker enumerates all `6! = 720` permutations of the six physical qubits, yielding exactly 81,360 order records. Each record contains all three `(Rk,Pk)` supports and the exact 84-bit signature

```text
sigma(v) = syndrome_72(v) || logical_parity_12(v).
```

The low 72 bits are detector syndrome; the high 12 bits are pairings with a quotient basis. A signature is a valid logical signature exactly when the syndrome part is zero and the logical part is nonzero.

For the three-suffix `R1(o)`, the unary predicate is constructive: it is true only if a frozen weight-12 logical `V` contains `R1(o)`. Then `D=V xor R1(o)` has nine qubits and the explicit mechanism is one physical residual plus nine singleton data faults, of cost ten. The checker validates `R1(o) xor D=V`, physical/canonical signature equality, zero syndrome, nonzero logical quotient, and the stored pool index. Every catalog has exactly 360 unary-positive and 360 unary-negative orders, giving 40,680 constructive unary witnesses over the 113 catalogs.

The reconstructed catalog is field-for-field equal to the sealed catalog. Its canonical SHA-256 is `fd7a065cae35643846567acb3cb6ec806cfe9bd20e14a60b9072d0e2195f97de`.

## 7. Conservative pair relations and the weight-14 positive witness

The source mechanisms induce 607 distinct structural `(sector,a,b)` pairs. For catalogs `a,b`, define:

- `U_a(i)` and `U_b(j)` as the constructive unary predicates above;
- a positive configuration `r=(ka,Sa,kb,Sb,V,D)` by `Sa xor Sb xor D=V` and cost `2+|D| <= 10`; and
- `C_r(i,j)` as “order `i` realizes `(ka,Sa)` and order `j` realizes `(kb,Sb)`.”

The finite truth relation is

```text
T_ab(i,j) = U_a(i) OR U_b(j) OR exists r: C_r(i,j).
```

This is a positive constructive relation. It is not an absence oracle. The checker explicitly materializes all 720 truth rows for every pair, representing

```text
607 * 720 * 720 = 314,668,800
```

cells. There are 272 relations with at least one explicit positive pair configuration and 335 unary-only relations. The 300 distinct configurations consist of 299 weight-12 logical completions and one weight-14 completion. They cover 93,888 good-good cells before unary closure.

The weight-14 search is independently reconstructed, not taken from the proposer catalog. It forms `V xor h` for every weight-12 pool word `V` and stabilizer row `h`, keeps valid logical words of weight 14, and unions the previously reviewed positive round-69 weight-14 words and raw round-71 weight-14 words. This gives 9,438 Xerr and 9,435 Zerr words. The sole new positive weight-14 configuration is:

```text
sector Xerr, checks (51,57), kinds (1,1)
supports {53,120,135} and {3,58,141}
logical support {3,42,47,49,53,57,58,60,115,120,123,125,135,141}
singletons {42,47,49,57,60,115,123,125}
cost 2+8 = 10
source = weight12 pool index 566 xor X stabilizer check 57
source mechanism = iter16-Xerr
```

The checker reconstructs every positive configuration and truth row field-for-field. No failed weight-12 or weight-14 completion is used negatively.

### Pair factorization does not assume independence

A minimized pair term factors as a rectangle `A x B` only after the checker proves

```text
for every i in A and every j in B: T_ab(i,j)=1.
```

Each true cell already selects one explicit mechanism by the priority `a-unary`, `b-unary`, then first matching explicit pair configuration. Rectangular storage therefore compresses an exhaustively checked two-check relation; it does not combine marginal probabilities or infer that independently positive pairs can be glued. Mechanisms involving more than two checks are handled by the joint DP below.

## 8. Exact multi-check GF(2) DP and its equivalence proof

Fix one selected source mechanism with data singleton mask `D`, participating checks `C=(c1,...,cm)`, and selected residual kinds `K_c` at each check. For local order `o`, set

```text
g_c(o) = XOR over k in K_c of sigma(R_c,k(o)).
```

The checker also constructs every `P_c,k(o)` and proves locally that its signature equals the corresponding canonical signature. Hence the physical and canonical total signatures are both

```text
Sigma(o1,...,om) = sigma(D) xor g_c1(o1) xor ... xor g_cm(om).
```

An antecedent is a conjunction of within-check comparisons. Grouping its atoms by check gives a finite allowed-order domain `O_c`. The checker deliberately takes the full Cartesian product `O_c1 x ... x O_cm`. Any globally reachable schedule satisfying the antecedent maps into that product, so proving the full product safe is at least as strong as proving only the globally reachable subset safe.

The DP starts at

```text
S_0 = {sigma(D)}
S_r = {s xor g_cr(o) : s in S_(r-1), o in O_cr}.
```

**Exactness proof by induction.** For `r=0`, `S_0` is exactly the signature of the fixed data part. Assume `S_(r-1)` equals the signatures of all choices for the first `r-1` checks. Every DP transition appends one allowed order at check `cr`, so it produces a real `r`-check tuple. Conversely, every real `r`-check tuple has a first `r-1` prefix whose signature is in `S_(r-1)` by induction, and its last order appears in the transition, so its total is in `S_r`. Deduplicating equal 84-bit states loses no acceptance information because the acceptance predicate depends only on the final signature. Thus `S_m` is exactly the set of final signatures for the whole Cartesian domain.

The term is sound exactly when every state in `S_m` has zero syndrome and nonzero logical part. This test retains all cross-check XOR cancellations and correlations, including those involving three through nine checks. It is not a product of pair decisions and makes no pair-independence assumption.

The clean-room reconstruction gives 48 exact selected-mechanism relations, with 2--9 participating checks. Forward and reverse deletion minimization generate 96 candidates. For each retained multi term, the checker additionally enumerates every tuple, instantiates its canonical and physical 144-bit selector from the actual orders and selected kinds, confirms fixed fault cost at most ten, and binds `(mechanism id, order ids, canonical support, physical support, final signature)` into a stream. The 26,956,800-selector stream SHA-256 is `31b182982a2692f987662bbb6a507a66d3fc9905ca6746ac18c0a7849bdd5550`.

## 9. Minimization, semantic equality, dominance, and deduplication

Each pair seed and each multi source is minimized twice, once in forward atom order and once in reverse. An atom is removed only if the exact pair-rectangle test or exact multi DP remains sound.

For an antecedent `t`, let `M_t(c)` be its 720-bit allowed-order mask at check `c`; omitted checks have the all-orders mask. The semantic key is

```text
(sector, sorted nontrivial pairs (c,M_t(c))).
```

Two terms are duplicates exactly when these keys agree. Term `u` dominates term `v` exactly when they have the same sector and

```text
M_v(c) subseteq M_u(c) for every check c.
```

That inclusion means every tuple satisfying `v` also satisfies the already-sound, at-least-as-general antecedent `u`. It is checked by full 720-bit masks, not atom syntax.

The old library is reconstructed from the reviewed round-69 object and contains 4,740 terms. The nested copy is byte-for-byte equal to the sealed round-69 classification. Against it, the 600 pair candidates plus 96 multi candidates classify as:

| class | count |
|---|---:|
| new raw candidates | 696 |
| duplicate old | 0 |
| duplicate new | 85 |
| dominated old | 0 |
| dominated new | 45 |
| retained new | 566 |
| merged installed generalized | 5,306 |

The retained set contains 563 pair rectangles and three exact multi-check terms. Its canonical SHA-256 is `0aec51794845c461fe3dfd1685343c7aa66491f4c54e4db483a22ea28e38056b`.

## 10. Exhaustive retained-tuple replay and source coverage

For every tuple in every retained pair rectangle, the checker produces a physical mechanism:

- 4,170,564 tuples use the explicit `a` unary witness;
- 731,484 use the explicit `b` unary witness after `a` is unary-negative; and
- 172,368 both-good tuples use a matching explicit pair configuration whose canonical and physical XORs are independently checked.

That is 5,074,416 pair tuples. The three retained multi terms contribute another 26,956,800 explicit physical selectors:

| term | checks | allowed-order counts | tuple count | exact states / maximum layer states |
|---|---|---|---:|---:|
| `r72-generalized-0018` / `iter17-Xerr` | 3,26,44,60 | 48,36,36,48 | 2,985,984 | 1 / 1 |
| `r72-generalized-0040` / `iter19-Xerr` | 11,51,61 | 48,48,36 | 82,944 | 1 / 1 |
| `r72-generalized-0096` / `iter11-Xerr` | 30,40,44,46,51 | 48,36,36,48,8 | 23,887,872 | 1 / 1 |

The total is 32,031,216 tuple-to-physical-selector replays. The small state count in these three terms is a consequence of their atoms fixing each selected residual support's signature; it is not an assumption made by the DP.

Every one of the 48 source orders satisfies at least one retained term. Forty-five mechanisms have a retained pair-based positive generalization (and also their exact multi relation); `iter11-Xerr`, `iter17-Xerr`, and `iter19-Xerr` have no positive pair mechanism and are covered by the three retained exact multi terms. The 48 original candidate-exact blocks are preserved unchanged.

## 11. Rebuttal-first positive-only attacks

The decisive scope attack is constructive. In each of the three pair-library misses, I located a source pair whose exact source-order cell is zero in the conservative pair truth table while the full selected multi-check mechanism remains an explicit valid physical mechanism of cost ten:

| mechanism | zero pair / order ids | full selected physical support | nonzero logical parity indices |
|---|---|---|---|
| `iter11-Xerr` | checks 30,40 / ids 396,523 | 31,36,42,45,48,52,53,58,62,64,88,108,109,114,115,120,128,130,138,143 | 0,1,2,3,5,8,11 |
| `iter17-Xerr` | checks 3,26 / ids 91,396 | 21,27,37,44,45,52,61,72,96,97,101,110,121,128 | 0,5,7 |
| `iter19-Xerr` | checks 11,51 / ids 499,90 | 29,37,45,63,69,80,89,111,119,120,121,136,138,139 | 0,1,5,6,7 |

For example, `iter11-Xerr` selects `D:88,D:120,D:138,D:143,R:30:0,R:40:1,R:44:1,R:46:0,R:51:0,R:51:2`. Its pair `(30,40)` is zero at the listed orders, but the complete ten-fault physical XOR has zero syndrome and the displayed nonzero logical parity. This is a direct counterexample to “zero pair cell implies no physical mechanism.” The other two rows give the same attack with fewer participating checks.

The logical error behind all prohibited inferences is the same:

```text
no witness found in library L  does not imply  no witness exists in the full direct-360 space.
```

Therefore:

- a zero pair cell means only that neither catalog unary witness nor a listed explicit pair configuration proves that cell positive;
- a positive-finder miss means only that its finite constructive search did not find a completion;
- failure to find a weight-12 or weight-14 completion says nothing about other logical words or multi-check cancellations;
- a deletion countertuple proves the retained antecedent is minimal relative to its finite relation; and
- a direct SAT assignment, not a library lookup, remains the authority for existence. A direct UNSAT claim requires an independently accepted candidate-specific proof.

## 12. The 5,705 deletion controls

Every retained atom has a deletion control, for 5,705 controls total. For a pair rectangle, removing an atom exposes `(i,j)` with `T_ab(i,j)=0`; this proves only that the weaker rectangle is not certified by the conservative positive pair library. For a multi term, removing an atom exposes an allowed tuple whose selected mechanism has a bad final signature; this proves only that the weakened antecedent is not sound for that fixed selector. Neither countertuple establishes physical absence. The package and this review correctly label every control with that library-relative or selected-mechanism-relative scope.

## 13. Fresh-process outer formulas and models, iterations 30--41

Each outer iteration was reconstructed in a newly launched clean-room subprocess. The base model has 864 named integer edge-time variables in `[0,863]`; six-way `Distinct` constraints for every X check, Z check, and data qubit; all 648 measurement-consistency equivalences on size-two overlaps; and explicit global X/Z interleaving constraints. Every installed antecedent `a1 AND ... AND ak` contributes the blocking assertion `NOT a1 OR ... OR NOT ak`.

The base has 4,398 assertions. Iteration 30 installs 6,826 blocks and each completed dual-sector iteration adds two exact blocks, so iteration 41 starts with 6,848. The checker reconstructs all 1,440 unary terms, 20 round-62 blocks, 4,740 old generalized terms, 566 new generalized terms, and the exact dynamic prefix. It verifies each stored schedule has all 864 edges, all 648 MC constraints, no qubit/check collision, compressed used times `0..L-1`, global interleaving, and no installed antecedent left true.

Raw Z3 SMT2 bytes can differ because the printer numbers internal shared `$x...` DAG nodes according to Python expression sharing. To avoid confusing that serializer detail with formula equality, both the rebuilt and sealed texts were parsed by the same Z3 SMT-LIB parser. For every iteration, the ordered assertion sequence is equal element-by-element as canonical `sexpr()`, and both the rebuilt assertion set and the sealed assertion set accept the complete stored schedule when fixed. This is stronger than comparing a solver status alone.
| iter | blocks/assertions | layers | schedule SHA-256 | X vars/clauses/w | X DIMACS SHA-256 | Z vars/clauses/w | Z DIMACS SHA-256 |
|---:|---:|---:|---|---:|---|---:|---|
| 30 | 6826/11224 | 159 | `23c6b85b2c33e886d430ba59ea064b7b137f1b90d7bf8633ff46fd893131a68e` | 5983/22512/10 | `517c52d8a18930354543277119aec532dea175332ddad2c363388b2140ddface` | 5901/22184/10 | `9f5f5aa5b6a5de019345e8848629d1fdb10ec2a47d59dbdc1d383c79003a69ab` |
| 31 | 6828/11226 | 163 | `7cd759cb93fd3f1b0a1a2a5a0487f432c12f9cf00b8263862abba6e83193f6cf` | 5984/22516/10 | `d9369e6a81faae73f2e12f00c92a24fd74339c7eadf3be0d5adde249180af077` | 5904/22196/10 | `16c95b1eaa4cf2d179f63fb48154972d2ea5b231d1e5b534980e6214231d3ae4` |
| 32 | 6830/11228 | 142 | `79cb7a43363722b5fe7e3c977dfac59396b4bc17cddc6971e9f56b890e3bc28e` | 5939/22336/10 | `d76835baeca95ed2ab66b5461f0bfac9dc3b9fe39c4a7b6033e49ac609025dc6` | 5897/22168/10 | `39841a3f85e7941b78ccc774e422cc268c052979b908c2fdc1bff98bc36de8ce` |
| 33 | 6832/11230 | 141 | `2f52a7d44c821db6229f907fb6ec03d3f96f1afb5117f0d8cab7f85333f5ce54` | 5939/22336/10 | `a94fdaf571ef9f0085dc804d9dc947aefaff311b5aa54ab8510e6e820d49f5b5` | 5895/22160/10 | `461cd27cce14fe13b76bc2bc1b0d0fe5795c3ee0ef116c6dbd43588e907a59aa` |
| 34 | 6834/11232 | 152 | `9074090085e287580a7e3430b3b50452cea1b24e9187b45a25e524d3655bf7fb` | 5970/22460/10 | `781f3e3130391512b647d893d4c52b7cefd1495ce531ae1ffcac9d0409ad154e` | 5895/22160/10 | `41045b2fdaec7d1e3f2b543080fca5410b745f7213f5a2de722a4ec4821ba982` |
| 35 | 6836/11234 | 184 | `2ef491a93653e7e0d5024a67dfaee269c676828e933233109f1fd77c47190603` | 5908/22212/10 | `07920681cb1b878179e7877b52ea5536d8661bc83da03e1ac5bc3bc4a234760c` | 5879/22096/10 | `d8b90e182a11b1ad1e9eb8ecd82b5a7bd5ca7a3496ac59c9fdce619b1637e3a7` |
| 36 | 6838/11236 | 180 | `83e4904227d466dfeab6e957023711fe03bfdbc49f2b309289b006fbbbd63790` | 5899/22176/10 | `9da704f8b5aff40f4e7159c05ea57a638ceabe35dbece9a1da960e87e242207d` | 5881/22104/9 | `3f2f6b514a28568b0ddb113acf714282f1d9975c9c14682d1c7420e1af74f3c0` |
| 37 | 6840/11238 | 180 | `3b6513cc8d7ae6080f19993756de3d8a68a8ec62d0fd47f1cd3797e684a0c6bc` | 5900/22180/10 | `608607923768b06d601322d706b7419764c3206e9acbab749e9c4b93dd96b35f` | 5881/22104/10 | `2dcb40d33635af1108b7b0663f792aaabeba1001bfe97b511f1d628d5ce44296` |
| 38 | 6842/11240 | 151 | `6dd6d535c64160a6f84ddb91d7b2f3f8aed67451e220f8949a7edca8c369f141` | 5904/22196/10 | `6356ecfecca197e7ebb7465dc342485e94d4545c3808698de80131e6fab2e361` | 5893/22152/10 | `2c3c99381f476849df8f5f1fedcc969ec7b13d696fc603d4be23ef5d0ae81abf` |
| 39 | 6844/11242 | 165 | `fce5dd538b0954f47b3dda16a472ff10391e696476f4e981ea349090056e2a6f` | 5893/22152/10 | `a865fabce9303dfa51be68857f077d66699e57d7d102687dc7dbaf1c88ce02ff` | 5874/22076/10 | `d15a6ffaab91690522ff8d7a51f0e523ba210e90444ca8818803798a1f3e2316` |
| 40 | 6846/11244 | 150 | `c799b9399c8bc419f7d92556f3932168dfa13ab38d6c68e156a2feb9369202fb` | 5968/22452/10 | `190fd3391744b2baa1c548714c09169f81aee1f4c266231360c5ae4d1bf99f5a` | 5903/22192/10 | `5370200511d2d5fc802469b6b8526d44a139b3c23b5139941e61573ce17b6e44` |
| 41 | 6848/11246 | 143 | `28c123cce2a7579a3145b9224efb54ea4cff54745381f6290e55f772c3a1507e` | 5944/22356/10 | `7dba0b7738c5d956ff19494ba1c5c6cb0755c394849134356f1957c4f9bcfdce` | 5906/22204/10 | `295d10a6f392898446cc587d6fe7473d21d3c9b7de9bea673fb347bc3a7fe636` |

The ordered assertion hashes for iterations 30--41 are, respectively:

```text
a17a6f7f620acfb2d4c3f4125b35d2d53ef2e51728fcdcb1b72c91d00bca0774
88f4347f561fb9d2987217957442eaf269bac8168d7aeb4fcabd05d4250f5304
549adf0dea85ebbbf369e78c2503a44900f13745caed5e66a39a07a8ab55cd70
9d792c3850a422a892ed27b5eb20a3a3996f250bc0ad0bbdc7b6fca70cbddff4
094bf31a467b5772df0194b9c93effc683f1325a93001e49a3387c2a32cedcfe
c9ddf26619e22da898f3c68fbfeba31f62b96331cdb10737d01d5d4515050a66
9a03ff37ace79cca06d7ea65152e5ac1fb3d5242dad99d458aae0481b7ec9f49
c147276a46cfa5ccf569295f329c7bfde6d53fc3cf94245738885b882c815a99
6585f0c8c446b3a71ce0d8edf043a1bb77ebdb284be79872db548f0b5a4c797d
fdfdb0b082f368fe4e16c7201100e40b9e21e1b2991b6321054a4f585f173a2d
2cb0a48e4c598f15110b03026372c71d4a68fa1b154c577d831e523106a6b81c
5303ad67bb8af23d5326ba9e26e6323b7be247821f428092e6b078fa86b42d5a
```

## 14. Twenty-four complete direct-360 formulas

For each sector at each new iteration, the checker reconstructs the complete direct formula from the schedule and frozen incidence:

- variables 1--360 are the 144 singleton data columns followed by 216 residual columns;
- 72 exact XOR constraints set all detector syndrome rows to zero;
- twelve exact XOR outputs compute logical quotient parities, followed by one nonzero disjunction;
- an exact prefix-threshold recurrence enforces `sum(select[1..360]) <= 10`; and
- there is no pool, residual-pattern, check-count, or within-check-family restriction.

For every candidate, the bound Xerr and Zerr pool counts are both 1,884, their hashes equal the independently rebuilt complete pools from Section 4, and their twelve stored logical-basis representatives equal the independently selected quotient bases. These bindings are checked even though the direct query is stronger than pool membership: it accepts every zero-syndrome selector with nonzero quotient parity.

The rebuilt DIMACS bytes, variable dictionary, column dictionary, formula summary, and clause JSONL bytes match all 24 sealed formulas. All 24 complete assignments bind every formula variable exactly once and satisfy every clause. In total, 533,680 clauses and 141,940 assignment values were evaluated. Replaying the selected primary variables through actual physical suffixes gives twelve Xerr mechanisms of weight ten, eleven Zerr mechanisms of weight ten, and one Zerr mechanism of weight nine. Every physical XOR has zero syndrome and the same nonzero logical parity as its canonical XOR.

The ordered 24-formula hash-stream SHA-256 is `7221107e86ac9b00444317f4b1bc3cc01c1b4390d1299f6036b6d25ed6093be2`. The exact dynamic state starts at 60 inherited blocks, appends two independently reconstructed blocks per iteration, and ends byte-for-byte at 84. Every iteration outcome is outer SAT, Xerr SAT, Zerr SAT, accepted absence proofs zero, and repair not entered. The next state is iteration 42 / 6,850 blocks. Exploratory round-63 pair clauses installed: zero.

## 15. Negative and proof-checker controls

The clean-room direct checker reran these mutations rather than accepting recorded booleans:

| control | count | independent result |
|---|---:|---|
| flip one selected assignment variable | 24 | rejected by clauses; stored first failed clause and count reproduced |
| remove one selected primary fault | 24 | no longer a valid zero-syndrome nontrivial logical mechanism |
| collide one schedule edge time | 12 | legality audit rejects |
| truncate one full assignment | 1 | completeness check rejects: exactly one formula variable missing |

The independent proof binaries were then run directly in the foreground:

| proof control | exit | required marker / result |
|---|---:|---|
| valid DRAT on `php6_5.cnf` | 0 | `s VERIFIED` |
| DRAT truncated to ten lines | 1 | `s NOT VERIFIED`, `ERROR: no conflict` |
| LRAT generated fresh from valid DRAT | 0 | `c VERIFIED` |
| LRAT truncated to ten lines | 1 | `c NOT VERIFIED`, verification incomplete |

The freshly generated LRAT is byte-identical to the sealed round-72 LRAT, SHA-256 `0723e34b24bfa7b1b8432f1606f5ba9c43e325e1c8e9eab6195b45d3cedcfd0f`. These are toolchain controls only; round 72 contains no candidate-specific UNSAT proof.

## 16. Repository contracts and candidate installation

Before linking, the live repository passed:

| command | result |
|---|---|
| `proof_dag_check.py --problem circdist` | 16/16 node files structurally valid |
| `proof_dag_check.py --problem all` | 85 SE + 144 k-Sum + 16 circdist = 245/245 |
| `check_circdist_migration.py` | 16 nodes / 143 original events / 728 byte-identical copies |
| `test_release_contracts.py` | 14/14 |
| `test_dag_contracts.py` | 24/24 |
| `lean_dag_check.py --selftest` | 23/23 |
| strict duplicate-key YAML scan | 558 files / 558 documents, zero duplicate keys |

The baseline evidence-closure command correctly returned nonzero: it reported exactly 1,489 unlinked evidence files, and every one is inside the not-yet-linked round-72 directory. There was no other orphan or foreign path. Its output has SHA-256 `0ccff8ed7a826d7a5c76141d90656f687b509f396ebcb3fab9898314a8f84348`.
After this review was copied but before any dispatcher node update, the live closure command predictably reports 1,490 unlinked paths: those same 1,489 package files plus this one review, and nothing else. Its output SHA-256 is `3aee06d3a25aa76c79a5e6dd280d1ed805942689a8cfac03f5f0431af341b921`. The isolated candidate below closes all 1,490.

Candidate-install results are recorded below after testing an isolated `/tmp` copy. The candidate is constrained to add two evidence links, one summary paragraph, one frontier replacement, and one append-only event; claim text, routes, assessment level, caveats, historical events, and all other nodes remain unchanged.

The install script is 6,559 bytes, SHA-256 `a0e87e4ce8abd6441825689b23fa3fbb31694afae75a96ca2f708811df1044e3`. It parsed the old and candidate YAML and made text-local replacements only. Its semantic assertions returned `PASS`: the claim, role, routes, `CONJECTURED` level, caveats, and frontier key set are equal; all seven historical events are value-equal; exactly one append-only event and two evidence links are added. The node changes from 35,885 bytes / SHA-256 `b62d580cd89f6bfa7c0d93112446f7aaf142bba7b2bd0d917134d230985964bf` to 38,424 bytes / SHA-256 `a4cef1b1c3c4bfdd65406079b4303be224e42c6d01564fe697e6aa379a992b4b`. The result record SHA-256 is `e12678056e999c789da19bcd88a56a91263343722860cffa05f019479eb85a76`.

All candidate commands ran in the foreground and returned zero:

| candidate command | wall seconds | exact result |
|---|---:|---|
| minimal install and semantic assertions | 0.087841 | `PASS` |
| `proof_dag_check.py --problem circdist --write-generated` | 0.323212 | 16/16 structurally valid |
| `proof_dag_check.py --problem circdist --previous-state <live-root>` | 0.385384 | prior nodes, routes, and events retained; 16/16 valid |
| `proof_dag_check.py --problem all` | 1.043932 | 85 SE + 144 k-Sum + 16 circdist = 245/245 |
| `evidence_closure_check.py --problem circdist` | 0.206733 | closure OK; 140 structured paths, all local and linked |
| `check_circdist_migration.py` | 0.747432 | 16 nodes / 143 original events / 728 byte-identical copies |
| release contracts | 0.204009 | 14/14 |
| DAG contracts | 0.322112 | 24/24 |
| Lean selftest | 0.148494 | 23/23 |
| strict duplicate-key YAML scan | 2.950518 | 558 files / 558 documents / zero errors |

Regeneration touched the two generated-view timestamps but left both contents byte-identical: `NODE_INDEX.md` SHA-256 `08ec3a7a830bfb4dd779585eb3a9fa79a58d5d371cf05c884878a875627f304c` and `GRAPH.mmd` SHA-256 `c34c1a78663bfdebd1b1587a3aae3fb8627b2b9df7801fcba99a982582ead66e`. A recursive checksum comparison between candidate and live roots, excluding `.git`, the candidate Gross node, and this candidate review, found no other content difference. Thus the tested installation is both closure-clean and minimal.

## 17. Exact dispatcher license and prohibitions

With this clean result, the maximum license is:

```text
CLEAR-PROPOSER-LEVEL-CONTINUATION
link: circdist/artifacts/circdist_gross_round71_generalization_round72_20260829
link: circdist/reviews/circdist_gross_round72_generalization_exact_review_20260829.md
node update: minimal assessment.summary + frontier.dstar-residual + append-only event
restart: iteration 42
installed blocks: 6,850
claim: unchanged
routes: unchanged
assessment.level: CONJECTURED, unchanged
D*_Gross: {11,12}, unchanged
```

Continuation must remain strict: rebuild every outer candidate in a fresh process, independently replay it, generate both complete direct sectors unconditionally, accept an absence result only with a candidate-specific independently checked proof, and enter repair only after both sectors pass that standard.

The following inferences remain forbidden:

- positive library -> completeness of the direct-360 search;
- zero pair cell -> physical absence;
- no weight-12/weight-14 completion -> physical absence;
- deletion countertuple -> physical absence;
- timeout, UNKNOWN, or a positive-finder miss -> UNSAT;
- one or two direct-sector absence results -> repair without the required dual result;
- finite continued SAT iterations -> outer exhaustion;
- this proposer-level progress -> `D*=11`, `D*=12`, a route change, or a level change.

## 18. FIX-2 foreground execution and failure ledger

Every long-running command used a foreground wrapper that starts one process group, waits with a recorded hard limit, sends SIGTERM only on timeout, then SIGKILL only after a five-second grace. The two load-bearing full runs used 2,400 seconds (author) and 3,600 seconds (clean-room); the twelve clean-room outer children used 300-second foreground subprocess timeouts. No command timed out and no signal was sent. The final durable wrapper aggregation contains 47 records: 30 exit zero, 17 disclosed expected/construction exits one, zero timeouts, zero SIGTERMs, and zero SIGKILLs. Its SHA-256 is `50c4650fd2673848517bf7efe86ff92d7d6e23c02ea2ee5187853702b0482333`.

Substantive command ledger:

1. searched for and confirmed absence of `AGENTS.md`; enumerated all required files;
2. ran the independent all-file/gzip/tar reader over round 69, round 71, and round 72;
3. checked the 1,491-entry round-72 SHA-256 manifest;
4. created the Python 3.9.6 venv, installed the exact four-package dependency set, and froze it;
5. ran author `verify.py --full --repo-root` with a 2,400-second limit (expected administrative binding failure described in Section 3);
6. independently diffed all eight source bindings;
7. ran author self-contained `verify.py --full` with a 2,400-second limit (pass; cross-check only);
8. compiled and smoke-tested the clean-room checker, retaining every construction failure listed below;
9. ran full clean-room v1 (200.379010 seconds, pass), strengthened every multi tuple to instantiate and hash its physical support, then ran final full v2 (233.579914 seconds, pass);
10. ran valid/corrupt DRAT and LRAT controls with 60-second limits;
11. ran proof-DAG circdist/all, evidence closure, migration, release contracts, DAG contracts, Lean selftest, and strict duplicate-key scan with 300-second limits;
12. built and validated the isolated candidate installation, including generated views, previous-state retention, closure, migration, contracts, Lean, duplicate keys, and diff scope; and
13. bound a pre-write whole-repository content inventory and Git status, scanned for reviewer processes, copied only this review, proved the post-write inventory equal outside this permitted path, deleted the entire scratch tree, and performed a final process/residue scan.

All observed nonzero or construction failures are disclosed:

| stage | exit / wall | reason and resolution |
|---|---|---|
| author live full | 1 / 1.383428 s | scheduler advanced after seal; exact seven-equal/one-administrative-drift comparison performed; offline full passed |
| first `outer30` smoke | 1 / 0.148070 s | Python 3.9 lacks `int.bit_count`; replaced with `bin(x).count('1')` |
| one wrapper invocation | 2 / before child start | used summary-style `--seconds` instead of actual `--timeout --cwd --log`; rerun with wrapper's declared interface |
| second `outer30` smoke | 1 / 0.047988 s | omitted `R73_PKG`; explicit sealed absolute path bound thereafter |
| third/fourth `outer30` smoke | 1 / 11.341710 s and 1 / 11.276999 s | raw Z3 SMT2 differed; diagnostic proved internal `$x` DAG-sharing IDs/expansion only |
| fifth `outer30` smoke | 1 / 12.431367 s | compared builder AST with parser-normalized AST; normalized both texts through the same parser |
| sixth `outer30` smoke | 0 / 12.570620 s | 11,224 ordered parsed assertions equal; rebuilt and sealed fixed models SAT |
| first repository-validator batch | seven exits 1 / 0.02--0.05 s each | exact math venv intentionally lacked PyYAML; reran unchanged commands with system Python 3.9.6 / PyYAML 6.0.3; all expected contracts passed except expected unlinked closure |
| baseline evidence closure | 1 / 0.210001 s | expected 1,489 round-72 package files unlinked before review; no other path |
| post-review live evidence closure | 1 / 0.209961 s | expected 1,489 package files plus this unlinked review before dispatcher installation; no other path; isolated candidate closes all |
| candidate installer, first anchor check | 1 / fast foreground assertion | no write occurred; the sealed summary wraps after `through`, so the exact old-text anchor was corrected |
| candidate installer, second anchor check | 1 / 0.089774 s | no write occurred; `Round 71` begins mid-line after the prior sentence, so the anchor was restricted to that substring; the recorded third run passed |
| corrupt DRAT and LRAT | 1 / 0.023937 s and 1 / 0.011792 s | expected rejection controls |

A whole-repository pre-write content inventory excluded only this permitted review path and `.git`. It bound 5,549 regular-file/symlink entries and 221,387,849 regular-file bytes to stream SHA-256 `8f1c633f7e22baf1863d2f2ec078658df1472bb05c3314346f952bab9ba11baa`; the pre-write Git porcelain stream SHA-256 is `5eb993f9ebba30835cb2d832984cad85728788813889e5653e248deda3a77dfd`. The inventory script is SHA-256 `6e26500b64a0b62d37fa316e5236ebddde9d601d51a02f4ba7c8c81892370847`.

After the review copy, the same excluded-path inventory was byte-for-byte identical: 5,549 entries, 221,387,849 bytes, stream SHA-256 `8f1c633f7e22baf1863d2f2ec078658df1472bb05c3314346f952bab9ba11baa`, and inventory-file SHA-256 `efbba97fa3531e5b6201c77624a41c18aeb241489ba6ebf402ae8dfc402bc931`. The before/after Git porcelain streams are also byte-identical, SHA-256 `5eb993f9ebba30835cb2d832984cad85728788813889e5653e248deda3a77dfd`; Git collapses the existing untracked `circdist/` tree, so the full content inventory is the stronger path-level delta check. It proves that this review is the sole repository content addition. A process scan immediately before the copy found zero reviewer/verifier/clean-room/candidate processes; its output SHA-256 is `92c11d394cc22e373eac4f680853b3981e89cad9a5b916337673d53a61d2ae2a`. The final post-deletion residue and process result is reported with the dispatcher return.

The raw-byte SMT diagnostic was not weakened to a mere SAT comparison. Parsing both rebuilt and sealed text yields equal assertion counts, equal ordered assertion `sexpr()` sequences, and equal fixed-model acceptance in every iteration.

## 19. Final decision

The exact constructive evidence is clean, the attacks enforce its proper positive-only scope, and the new CEGAR state is fit for strict proposer-level continuation. No completion claim follows.

**CLEAR-PROPOSER-LEVEL-CONTINUATION**
