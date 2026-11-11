# CIRCDIST Gross Round 94 exact review — Round 95

## Verdict

**CLEAR-PROPOSER-LEVEL-CONTINUATION**

The sealed Round-94 package is accepted only as exact proposer-level continuation evidence. It licenses reuse of the 24 new exact EFSSC selectors and continuation from the fresh, unstarted iteration-148 state recorded below. It does **not** promote `CIRCDIST.gross` or `gap-via-lift`, narrow `D*_Gross`, prove a Gross or direct-query UNSAT result, license repair, establish exhaustion, or close either residual branch. `CIRCDIST.gross` and `gap-via-lift` remain `CONJECTURED`, and `D*_Gross` remains `{11,12}`.

This review was a fresh, strict-serial audit. I did not contact the proposer or any earlier worker/reviewer, did not use a sub-agent, did not edit the package, scheduler, canonical node, protocols, prior reviews, or prior packages, and did not commit or push. The only licensed repository write is this review. The complete replacement YAML at the end is a dispatchable proposal, not an installation performed by this reviewer.

## 1. Commission, bindings, and audit method

The commissioned live identities were independently read before use:

| object | observed SHA-256 |
|---|---|
| `operations/circdist/SCHEDULER.yaml` | `5a794463e956fc2bad257976a18d2872240788ed23a23f576564727ef113e90b` |
| `circdist/proof-dag/nodes/CIRCDIST.gross.yaml` | `c3b03597c496ace59bb84f5d4e4cfb1540b98e193dcba9f67adb0abd657bc3f3` |
| Round-93 review | `76a07f9d73fda5ced83818361eed24cd83b4ed7fc5a11c13b0fc027df4feb65d` |

The package snapshot of the scheduler is `4da1d0f15ddcdb7542cc69507661231807dad97edf684d578d5010c13b9b2383`, while its node and Round-93 snapshots equal the two live hashes above. This is a versioned input boundary, not a hidden mismatch: a line-by-line diff shows that the live scheduler advanced only to settle Round 94 and authorize this Round-95 review, including its budget, hold, ranked action, and round-log entry. The package correctly preserves the scheduler that existed when its computation began; the current commission correctly binds the later live scheduler. I replayed protected package checks against a disposable repository holding that historical snapshot and ran canonical replacement gates against a separate overlay holding the current scheduler.

The main checker was `/private/tmp/circdist-r95-cleanroom.py`, SHA-256 `6ac7a29f7b367aebcdcb626b36bf7ab2d4e36c8b1f01f98e5ce7ef46fa941836`, 42,975 bytes and 514 LF. It imports only the Python standard library and imports no package module. Its successful result was `/private/tmp/circdist-r95-cleanroom-result.json`, SHA-256 `61555a8e22a86b1312494cf65dffb47fdb820d0fa2dc61e8ef40a17448ab862a`. The exact run was:

```sh
cd <repo>
/private/tmp/circdist-r72-dispatcher-venv/bin/python /private/tmp/circdist-r95-cleanroom.py
# R95_CLEANROOM_ALL_PASS 13 12 24 125.125
```

The checker independently parses the files, DIMACS, assignments, semantic JSON, GF(2) supports, schedules, and ledgers. It does not call `replay.sh`. I later ran the sealed replay as a separate corroborating check. The full checker is reproduced in Appendix A so every construction below is public and executable.

## 2. Package census, manifests, seals, and protected identity

A recursive regular-file walk gives exactly:

| property | value |
|---|---:|
| files | 1,571 |
| bytes | 314,978,755 |
| LF bytes | 3,966,756 |
| root manifest rows | 1,570 |
| payload manifest rows | 1,569 |
| inventory rows | 1,568 |

All three row sets are sorted, unique, use normalized relative paths, and exhaust precisely their intended file sets. I streamed every listed file and recomputed every SHA-256. Every inventory byte and LF count also matches. The accepted identities are:

| object | SHA-256 |
|---|---|
| `SHA256SUMS.txt` / final root seal | `1e0a4af8591aa63ccccd1b2516c630eccb11a73fb9dea2e0ff1e0d32ed82ac1c` |
| `PAYLOAD_SHA256SUMS.txt` / final payload seal | `c39ef3552e461dd7513812b8296901e72369dfacbf6e71ae758b5bb58ed94c54` |
| `FILE_INVENTORY.jsonl` | `6d7efec34aeae4af05d269ec59a9dda4662d8da927c3c200515a3bbbbf1bc05a` |
| `REPORT.md` | `83a2db0af31ef3c87c0f67dcc88051f6bb95100b3d567f86c611c9921ee58419` |
| `RESULT.json` | `0a291feb16e04935558462bf61fd2f6833a85d6d81d11802c49d4391529ff047` |

The protected pre-install and post-install snapshots are byte-identical over exactly 227 files. Their common snapshot SHA-256 is `fe2f598511dfa2d0967f0cea3f705f8c7cc8867b2de176b70b6648af97b6daec`; `protected_tree_compare.json` reports both inventory equality and unchanged canonical/protected paths. The package made no canonical scientific-state change.

The first sealed attempt has different root/payload identities, `476dbea3f8fd2b785508cd2f9330f1ff94568549a5a3d0fecf690dbaebce7150` and `aa97afb5bf5292146da5f1166f05e57e1737f10671ac7d3f3db374e748d0f93b`. They occur only in the disclosed failure record with `first_seal_status: SUPERSEDED`; they are not the root or payload manifests at the package root. They cannot be mistaken for the accepted final seal.

## 3. Inherited iteration 136 was fresh and unstarted

Round-92's root and payload seals recompute as `4e255084bdab13ad0b9c295a9fe7cf2aea8231c4a56db656964f0695ddc6c982` and `fbc881f0dc54744cb3cfd0c4497571592f8597326ce98362eb42a032ed289090`. Round-94 `state/iter136_state.json` is byte-identical to Round-92 `continuation/final_state.json`; all six Round-94 iteration-136 formula files are byte-identical to their Round-92 counterparts.

The inherited state has `next_iteration=136`, `started=false`, `stop=null`, exactly 232 selectors, selector-state SHA-256 `1692d905120d2dcf51b949ce4a70ed4b8f1b270c2d07a1ddbf5813d20d80fa81`, and state-file SHA-256 `58781b46cc177df046ec334420046e1ccc8a23517f21fe4491e6412741ced57c`. Canonical serialization of each selector's mechanism ID, sector, selected names, data support, group kinds, and selector semantic hash reproduces that state hash.

A full Round-92 path census containing `iter136` finds only the six formula inputs (`source`, CNF, assertion map, circuit trace, metadata, encoding check). There is no inherited iteration directory, solver log, assignment, model, proof, status, or disposition. Thus iteration 136 was genuinely fresh/unstarted rather than a cleared copy of an earlier solve.

Its source and encoding are exactly:

- source file `a71fb5e708eeebf365dda0661b79652b264bc0eb87308626383a5ca389cfc5d8`;
- semantic source `a561515801904b458d34ebccea5aa364420f9a0a012e36e721f48fcbe9be4ebe`;
- 19,114 assertions, 406,656 variables, 1,372,232 clauses;
- CNF `289acad6be1068d63369511e9c95b0b1df146471bf05a1e4128758508612b64e`.

## 4. Independent reconstruction of all 13 outer encodings

For each iteration 136--148 I decompressed and parsed source, metadata, assertion map, circuit trace, and DIMACS independently. The semantic source hash is `SHA256(canonical JSON(source minus semantic_payload_sha256))`; every source and metadata binding matches. The exact 14,484 inherited block vector is unchanged: 1,440 unary, 20 round-62, 12,820 generalized, and 204 dynamic predicates. Every later selector list has the preceding list as an exact prefix.

I reconstructed each circuit-definition clause directly from the trace:

- constant true: `(v)`;
- `v <-> (a and b)`: `(-v,a)`, `(-v,b)`, `(v,-a,-b)`;
- `v <-> (a or b)`: `(v,-a)`, `(v,-b)`, `(-v,a,b)`;
- `v <-> (a xor b)`: `(-a,-b,-v)`, `(a,b,-v)`, `(a,-b,v)`, `(-a,b,v)`;
- rank membership: all 32 truth-table rows for the five pairwise comparisons of a qubit against the other five check qubits, with the output sign determined by whether the comparison popcount belongs to the declared position set.

The 10-bit little-endian comparison recurrence was independently checked on all `1024*1024 = 1,048,576` input pairs. Across the 6,157 distinct rank domains in the thirteen formulas, all `6!` local orders and all six qubits were checked, totaling 26,598,240 rank-membership cases.

I rebuilt every root assertion in source order: unsigned time nonnegativity, `<864`, X-ancilla distinctness, Z-ancilla distinctness, data-qubit conflict distinctness, the 648 two-qubit MC equivalences, extrema inequalities and attainment, both global-interleaving clauses, every inherited block, and every EFSSC exclusion. The zero-clause unsigned nonnegativity assertions are still mapped. Definition-clause IDs and root-clause IDs are disjoint and together equal exactly `1..number_of_clauses`; primary and definition variables are disjoint and together equal exactly `1..number_of_variables`. No clause, variable, assertion, or family is unaccounted for.

The thirteen-formula aggregate is 248,638 assertions, 5,302,455 variables, 17,922,578 clauses, 5,189,615 definition records, and 298,246 root clauses. The actual aggregate clause-family vector is:

```text
constant 13
def:and 8,713,809
def:or 3,791,586
def:rank_membership 1,182,144
def:xor 3,936,780
root:block:dynamic 2,652
root:block:generalized 166,660
root:block:round62 260
root:block:unary 18,720
root:distinct 56,160
root:efssc 3,172
root:extrema_attained 52
root:extrema_inequality 22,464
root:global_interleaving 26
root:mc 16,848
root:time_upper_bound 11,232
```

The total is exactly 17,922,578. The tables below give every formula, map, trace, source, schedule, direct formula, mechanism, selector, and state identity.
### Formula identities

| iter | sel | assertions | vars | clauses | CNF SHA-256 | source file / semantic SHA-256 | assertion-map / trace SHA-256 |
|---:|---:|---:|---:|---:|---|---|---|
| 136 | 232 | 19,114 | 406,656 | 1,372,232 | `289acad6be1068d63369511e9c95b0b1df146471bf05a1e4128758508612b64e` | `a71fb5e708eeebf365dda0661b79652b264bc0eb87308626383a5ca389cfc5d8` / `a561515801904b458d34ebccea5aa364420f9a0a012e36e721f48fcbe9be4ebe` | `d4e60ffc4f503bbd4845c5a933f21bfe93038ecfbdad48eb3b3556c8e7337601` / `707c5ebc42cf9d35dde99eaffd6207ea5de7a1cdea04f51d29676241380054f0` |
| 137 | 234 | 19,116 | 406,852 | 1,373,457 | `2f7f7be5cc67822aa30ca9ac8021c79afcb8e15ea4f9724dcc1d3c974ede88e4` | `0207760f863b90c715399b887b78123ba0382364e242b58031e7599868a9f452` / `dd16f5db19b6e2cdc6d75446d1029f02f07aa18628f12f6d426e2edfcd658514` | `fdf0e1a1964a55d2b8ccecb9e307d8149ef8e25eb4a524a8cff3511220da0611` / `5d657bb4843eed8c26ad021e4792f79a855193ed8babecebf731961ea365efeb` |
| 138 | 236 | 19,118 | 406,936 | 1,373,752 | `cf400af11b86f067718ba75a5bdb29e1d5fcde3730a0ef8cd99d6b2b95903fa1` | `1f4420e517f9bff2d55673eba0110853269e46a30b50b160c549744b9a70662f` / `ceb3beed624e626dbec068db0179c5625a58650911baf53c139b7e9964e0688b` | `44af050d41c8f3c55d0a40353c113b9c21020c639306c7b28c2356ba260dc0f3` / `d92707a910b697b6adfee7d03936d89c90c4ce501d5281f7664ef686ccbaadd8` |
| 139 | 238 | 19,120 | 407,121 | 1,374,932 | `3a82af909f27caa97d68463ada22814a537f6ece3fe3117bf1eb2298ec3eba24` | `fb12a5a01b196dda5254825a9f695fc98ab5c4056818c0da73c534cc7bad186a` / `c7f498068e16934517768285ab3a1e1def79482b769fec899c67134b32d50026` | `ac9e3358a61cd81710f129b6fa803dfff3ad1efa8ead47f5bb20e3ad376c37ee` / `1229873da389d97b55612ced47783dc1af7c2caf67037ad24ed355fe8dd055f4` |
| 140 | 240 | 19,122 | 407,424 | 1,376,557 | `d908f326aa36be550e7d501e1b5af8f736d3eec3aa4dbe0c22f54d398c20909a` | `788012b63fa6e10561ac21933d35ccaddca07b8387fbb08c7998976e059ac9c8` / `a8cb55aa10f19100abca67b82b229c14daa21a5f91e6a634f3747c1fcfe44c9f` | `7085fc81669396cc8a8260d8144e4074b34118716d0a84c6ac229ff04bd6eacc` / `65403b51951b2de3a535c4a45b94d5b3c938fc92480365697edcc8aa9fd98408` |
| 141 | 242 | 19,124 | 407,727 | 1,378,010 | `1347bcadd5c17d26fe021ce4a3293eb14ed9e57344474e10a9885618ba72cc7d` | `4767ba65d950cbc3e99a08b1cc6952d02cf94f339fdab9fe7b2c2968a175a285` / `6f03f6d9a3b14027a910e6e7633546eb55b051d070f45e1a6f8579fafaefb9ea` | `083616d39f656d68c07cced50cbdd2ffa5c9cef16f2717da1d9d176feb36826a` / `fc03d48157e9c3dbad827110d489a010c37043cd5b9f1a47cddeb213a1c4be28` |
| 142 | 244 | 19,126 | 407,904 | 1,378,649 | `9865bfe874f93d3be38fc8a82aae5ad00cfaf66c671246c3c75d150810ac73d4` | `a2310babfcc205c98b92f79151ab309311b2545fd17b54e1d401cc74b306bd18` / `635cf5fde3f940260852bf6bd5d1ea9135892589b96c511c65b7d4f17d3a87e3` | `ec88a28dc667f84aa4eb51d3cadaebe335690c931c518a6f3ae2745b4448700c` / `3ffb50a2b386f7c4e5568eaebf065ed98681cdb3ea76c91f744aeee63c50ce15` |
| 143 | 246 | 19,128 | 408,150 | 1,380,050 | `5781637f051643e254e7edd248dca276be33654e8da62127470fec1565bab9ed` | `51f03261eefef47a61dbc1a48d0deca91c5afb92931496859220194c4bca18b5` / `ed041895a0992fa1bdc8b0d76d908cc595098f8142d7efabe0c6d17938d4ba15` | `e14446678632c0380c24c44fb40f59e9793ee2b848aae5f20aa8f871304eccd8` / `cea55de78e29db588a5b1197c980719d284bac5d6e999fa86fab4b7613df6e80` |
| 144 | 248 | 19,130 | 408,330 | 1,380,858 | `8351cc28eb27874b4b174411a1bf66d4e9b81bcb1069f6b33ed4c27a2e8a72f5` | `e14222b07df79854336d6fb94bf0051e3d45836d8e59e1060e613f9ab5d3a5fb` / `3a1e08e3a578a36ae36446b0924af04c462dc33b1fa0134e271798d3e86ee405` | `0643962c90e7dd226b31e32d504f8b5b0c3ef11f9f93d66952c8cefc2b42e006` / `1787de025786846083d6be1cfac02abdd6b94399b8ff7bddcc348d9863b6a129` |
| 145 | 250 | 19,132 | 408,499 | 1,381,815 | `022bfb72723c6f6fc483189e76512a131931931332cdc2202a1a1bbe674b1415` | `57d4e62aeeb989859cd9f6998b230cf087c8750c794bc9478fdc35901cf4c424` / `de40e7a4b19fc6a3c0339f27f982cbdbce17e9ea8e973d7f98b289b031afe012` | `67092350eb3ff84e7be8bf55fcf0eadee66ea02d3923b6580e93c1680da772a3` / `2a97ffbde29610487ed48b33f75e15732245c829b82b0afcd2ae10cdbd6fedca` |
| 146 | 252 | 19,134 | 408,743 | 1,383,041 | `0363aace88f4e1589b652df293d28d451e6546ae4711d751385eb4233aa8a3c3` | `b7d33bd44a41913d490f9668d9213cbdb10add1a496af79eede452ec48df473c` / `5d553a53c63a060a2f3f2271da95b91bf9caf3aa0f1322b1cd3613b925917654` | `cb9332328b41ceea7871a9e052e0eb52d5c8a000325518f1f0bd6d1aa77803b2` / `9fac06834faaf6e04b6425fe062c1a46ccf0872317848b335e3d80b6117f38bf` |
| 147 | 254 | 19,136 | 408,956 | 1,384,166 | `30d73f37d48d5f99760b113912e0f851a3f35997df561cf631a0a18a15e28e7a` | `c1e70f8cf2a4593de911a37cdfd6700cd4176916ddc1ab0e194797d04505666f` / `fe5a95ff149ce08fd1cd483556e917c73d7015725879b2226033c430dede78b5` | `716470f7e486fd6d664fceef7d8ac988f71c2b29ae83351c4acdd7e9120a00b3` / `9f93d12c2cfe478cde1a559c673fb0798cb419826d02bace3dc3855849b17b5c` |
| 148 | 256 | 19,138 | 409,157 | 1,385,059 | `397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4` | `0db20ed8ca0b120cda91eb7a94be25094adb9b77a2cacdd322e330a720d58b5f` / `2fd4a1982e1f6389804f7eee1120706f9d26c9e6a23acc05e2a15e036a67c032` | `894a977dd56bc2bfb158b6e95dcfb6691802f5ff15d2aba2410f2b7971627a1a` / `97f9ec35ff3cf539dc432a6b345fc18cb92a1c786256e869fa5066146b61316a` |

### Per-formula clause-family census

Every row also has the fixed root-family vector `block unary=1,440; round62=20; generalized=12,820; dynamic=204; distinct=4,320; extrema inequality=1,728; extrema attained=4; global interleaving=2; MC=1,296; time upper bound=864`, totaling 22,698 fixed root clauses. `efssc` is the selector count.

| iter | constant | def AND | def OR | def rank | def XOR | EFSSC roots | total clauses |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 136 | 1 | 669,189 | 291,456 | 88,704 | 299,952 | 232 | 1,372,232 |
| 137 | 1 | 669,363 | 291,477 | 89,280 | 300,404 | 234 | 1,373,457 |
| 138 | 1 | 669,474 | 291,495 | 89,280 | 300,568 | 236 | 1,373,752 |
| 139 | 1 | 669,636 | 291,531 | 89,856 | 300,972 | 238 | 1,374,932 |
| 140 | 1 | 669,858 | 291,588 | 90,432 | 301,740 | 240 | 1,376,557 |
| 141 | 1 | 670,110 | 291,627 | 90,816 | 302,516 | 242 | 1,378,010 |
| 142 | 1 | 670,299 | 291,651 | 90,816 | 302,940 | 244 | 1,378,649 |
| 143 | 1 | 670,506 | 291,711 | 91,392 | 303,496 | 246 | 1,380,050 |
| 144 | 1 | 670,728 | 291,735 | 91,584 | 303,864 | 248 | 1,380,858 |
| 145 | 1 | 670,866 | 291,768 | 91,968 | 304,264 | 250 | 1,381,815 |
| 146 | 1 | 671,088 | 291,810 | 92,352 | 304,840 | 252 | 1,383,041 |
| 147 | 1 | 671,250 | 291,843 | 92,736 | 305,384 | 254 | 1,384,166 |
| 148 | 1 | 671,442 | 291,894 | 92,928 | 305,840 | 256 | 1,385,059 |

### Outer assignments and decoded schedules

| iter | complete variables | clauses checked | raw / compressed legal schedule SHA-256 | used layers | inherited selector validities |
|---:|---:|---:|---|---:|---:|
| 136 | 406,656 | 1,372,232 | `e4b8a3501705c99f75dd92f7c76b3ad1fc9cc55bb3e557ac998808164f4a1112` / `45051af0b08e6647d50c6fb0535894173016fd013279e7a0eaee8b2e69ee2e44` | 142 | 0 |
| 137 | 406,852 | 1,373,457 | `1d64678fae94ca113bfe675a81234c937b4d3cd53daee944c251612e8a0aa453` / `2994ed9fb7a1b839406337785fa6308e2d63c131ed9ffc4ab1e096dfd79081b0` | 124 | 0 |
| 138 | 406,936 | 1,373,752 | `e437ba6563a3f92d19b3dfc98f0fae0a9a7ae7d4f597e2a20a60157382ab17cd` / `fad8da6b3374bf8ba09c8ceda898d9170007af652f2f9645b0428e1c7532d1d6` | 117 | 0 |
| 139 | 407,121 | 1,374,932 | `8cc5382766ee910c3c5aa21def6899ce995aceffd0f57d45c99d8b507773f36b` / `fa6d566acadf7b30754fcc3a46bdc9634cad798958e190d5237266117acf33ff` | 103 | 0 |
| 140 | 407,424 | 1,376,557 | `c09fb84ddd7c42258a1f04e65b45e5514ea9e1aafd69dbbbecdd4a0a37b5d947` / `f24644303abf6cbd90de152129cbcff7caf711c0e72f6392ad0914d4b004d98c` | 89 | 0 |
| 141 | 407,727 | 1,378,010 | `8b04c41fcf79ade3f5897469714b21572de90bdd29233f71f191763d62e87181` / `2ecbd9e3cbf4dca49ad5e59796cc61facf18544957834391d8a8335fbdb94706` | 114 | 0 |
| 142 | 407,904 | 1,378,649 | `3450e02acfc636cc0da0014d9b6418e0f3bb4eee3130d6bff12f87add5edc660` / `9a837b9d8a87ac31ec0f95c838f63418e8622dca59078181f751ce7efb617696` | 116 | 0 |
| 143 | 408,150 | 1,380,050 | `e6b68e99608a8df0a4c05a62070c17db98c6eb779ad4c72751ce73c10d2b0ba9` / `2297593ce829e9beb252eecf72487030c699b0977e7225eebf5602caa58ea35f` | 128 | 0 |
| 144 | 408,330 | 1,380,858 | `7739bbaf95e674672397c37a4333e79133e63a414d4bb2ae5253e1509170f9cf` / `8599312f8af25596faf18bee0314224743edd79e3e5f39a25e73160d1b70ae45` | 135 | 0 |
| 145 | 408,499 | 1,381,815 | `d8ba106e321cd26c7b00a110a07b9702481bda285cff9c56dcf9b20cfe8ae198` / `8f9a77d1cb186f81643dd58475ea429631c143a9d0a8a1f821b207fc0d5b5766` | 116 | 0 |
| 146 | 408,743 | 1,383,041 | `045c4fb4743bdad50382d604064effb9908421bf4638562ae12916f098ed40e8` / `8a799f25585ff2c8f5e39ed4c47cee29af60a4cbed8ddeb47bba04fbd7127d1f` | 110 | 0 |
| 147 | 408,956 | 1,384,166 | `88b9059a27deaa4500b97d01c28596ef3d3f598a69cc1893fd5bce61afb37b53` / `b74dbc4d796acb3c12cb99465770781971875834127faed9fcbb947f3de77d1b` | 461 | 0 |

### Direct-360 formulas, assignments, mechanisms, and selectors

`cw` and `pw` are the canonical and physical net-support weights after GF(2) cancellation; neither replaces the named elementary-fault weight `w`. `L` is the 12-bit nonzero logical-parity vector. All syndrome supports are empty.

| iter | sector | vars / clauses | formula SHA-256 | w / cw / pw | L | selector semantic SHA-256 | exact selected names |
|---:|---|---:|---|---:|---|---|---|
| 136 | Xerr | 6,000 / 22,580 | `0c34e3e48d27404aa8db19d37695edc77c5f62b93d9cfd756e4f542b212956e6` | 10 / 12 / 18 | `111011000000` | `5065670eab6c0297b265fe48dbb180ff58fe8efc694c1436e6bff5f807da44ea` | `D:38,D:109,R:25:0,R:26:2,R:28:0,R:35:1,R:35:2,R:39:1,R:41:0,R:45:2` |
| 136 | Zerr | 5,903 / 22,192 | `c48539ba44709376e028689adccfce0b2d2a144d81955cba1b5ed3e907c0f5e5` | 10 / 14 / 18 | `100110100011` | `566b367ad2b12d622ee90fbe24d17fc408bb129635c2930ea75e43cc9d8efa95` | `D:45,D:98,D:104,D:110,D:115,D:119,D:121,R:4:0,R:30:0,R:35:1` |
| 137 | Xerr | 5,991 / 22,544 | `a500fd17741f7302e906a33ca0204b7d17a8c9905952118975915e00e275a9ee` | 10 / 14 / 14 | `100100000110` | `ac92b12dfec3a49555330da7de8677f3235a74be2b5f3f0455c5fa90fde06f87` | `D:35,D:41,D:84,D:85,D:86,D:87,D:88,R:14:1,R:20:0,R:23:2` |
| 137 | Zerr | 5,919 / 22,256 | `d6647d7f6982e4e3bc53b716e96f53597287f304fa348a10ae850cfaa4d97961` | 10 / 12 / 12 | `101011000000` | `faaff7c19770fc89d588ac518ea7776cc0b24793794b829b73f7c7b539144c4b` | `D:66,D:67,D:69,D:73,D:133,D:135,D:139,D:143,R:0:0,R:2:0` |
| 138 | Xerr | 5,897 / 22,168 | `0cb4c871ea8cad13fcddb7104095c06a8d6abd9535d0f6a4bb206764ffcd3f34` | 9 / 16 / 22 | `011100100000` | `916254480c0d0a2f568e649065ec35ce666eadcc577209816b79979dbb26a3db` | `D:54,D:95,R:12:2,R:20:2,R:35:1,R:45:0,R:59:2,R:68:1,R:69:0` |
| 138 | Zerr | 5,926 / 22,284 | `4e28baf8850d291bf421bae04b86ff962a559357a9fc91777ed95a5b19fb2a31` | 10 / 12 / 12 | `101000110010` | `958648610013aa2ae044304a2e0ee7ed86da9da8404b5b6b5696912c88d916d6` | `D:0,D:22,D:29,D:46,D:48,D:56,D:89,D:98,R:51:0,R:59:0` |
| 139 | Xerr | 5,946 / 22,364 | `56c34495f4db806bbbaf9f6466c59107548a306e597b2c3d049af46148af76db` | 10 / 16 / 20 | `101010000010` | `f1dc56cd0d1ab51f0fd1f9ca0a317e5c518a509d9488cfa18b9c37dc8930fec7` | `R:48:0,R:54:1,R:56:0,R:58:1,R:59:0,R:59:2,R:60:0,R:62:2,R:68:0,R:68:2` |
| 139 | Zerr | 5,954 / 22,396 | `7028bc90c5a13ff8c2a1271e0b48d6abb961130508e9e0cadbf3445e0bc1dbbd` | 10 / 16 / 18 | `010110000000` | `078facdb96fe6c68a72a80323f7c0a35d4041da244566740b0713e37f8fdbde8` | `D:88,D:89,D:99,R:20:2,R:22:2,R:26:2,R:28:1,R:33:1,R:34:1,R:37:0` |
| 140 | Xerr | 5,948 / 22,372 | `c851c9302d79978288700615a3d0e851e335af06f98e6fe7bcb71fca1e735f04` | 10 / 22 / 26 | `000000011001` | `0aadbb4fd35105d5fbb54796ac18ed92f70a96009e1320e0aea64d70a3d7e599` | `R:9:1,R:19:1,R:32:0,R:45:1,R:55:1,R:64:0,R:65:0,R:67:0,R:67:1,R:68:1` |
| 140 | Zerr | 5,924 / 22,276 | `a5aecbb26919b9a146c441f6e84e109ea338eee7234ce71bfa1c0e006779c484` | 10 / 20 / 20 | `010001000000` | `1679fa99e2e5d117f83751b9dbfb3b5a35c6e2d8b18da12a6358803aa85bb71e` | `D:68,D:134,R:39:0,R:49:2,R:56:2,R:61:1,R:64:0,R:66:0,R:66:2,R:70:1` |
| 141 | Xerr | 5,970 / 22,460 | `4fef1a7bdf679a50c27df1e59d10c8a349eb2fa480a6eb904b9df6d692886c2d` | 10 / 12 / 14 | `110010000000` | `dd57604f432332f3e645aee40711dd26e40a39504d57cea8714f718a552e1d47` | `D:38,D:53,D:62,D:114,D:115,D:137,D:138,R:4:0,R:35:0,R:37:1` |
| 141 | Zerr | 5,932 / 22,308 | `c0d5e58e28835ca0405a8c6c9fecaf435f26e6d64fb9ca6f55734df799e131f7` | 10 / 18 / 20 | `010010010100` | `f214490d52eed91c44c7bb8b41d485bf17c342fd41a5eab83e5b792532f2a84a` | `D:61,D:72,D:98,R:22:1,R:33:2,R:39:1,R:53:2,R:64:0,R:70:1,R:71:0` |
| 142 | Xerr | 5,979 / 22,496 | `b3fc4ba2e3b8fa9f1dfc21a4dd04f9711b98a47059553087b2df3a2bffebeb4f` | 10 / 12 / 16 | `001010000001` | `efe303bdfdd2b104117ed7135d2c7cdbae29135f1ab8fb35903fd3c6fd702fc8` | `D:126,D:130,R:53:0,R:55:0,R:58:2,R:62:0,R:64:1,R:64:2,R:66:1,R:66:2` |
| 142 | Zerr | 5,869 / 22,056 | `ac7c00760410ad967f1ae852df045866347593818fd71915dfcc207e45959fd0` | 10 / 14 / 16 | `001010000000` | `7f68f4289f6b25836e7aa424d7a04f65747e40098ee3ccecd0b712180073b747` | `D:128,D:134,R:2:0,R:2:1,R:54:1,R:54:2,R:61:2,R:67:2,R:69:0,R:70:0` |
| 143 | Xerr | 5,966 / 22,444 | `89a7beacb392e4bfd8fe7aaeb2c2ab01e7b2387787af9bcad6a93dc1a4c2b985` | 10 / 12 / 18 | `101100000001` | `9b3d9096a0cf360609a6d8d7f2ce337d35fd1c31a17182ac56c9af7eda426d0b` | `D:55,D:61,D:136,R:49:0,R:51:1,R:51:2,R:53:0,R:55:0,R:56:2,R:61:0` |
| 143 | Zerr | 5,897 / 22,168 | `609000c3f7c9d700b85e8fd1b6e03d329dfd531685215831091e4ceb28c9db21` | 10 / 16 / 16 | `000000110111` | `0cd62825e3c9b02c89f4efbc265c3c54549c644079d20fc5cd307f5b61aa2292` | `D:36,D:52,D:96,D:135,R:6:2,R:19:1,R:35:1,R:55:1,R:64:2,R:71:1` |
| 144 | Xerr | 5,999 / 22,576 | `63850c462e31cdb6ea8cce06b76b39db78a04bde78aab5b29da6c12c944c3f4c` | 10 / 12 / 16 | `110110001111` | `8e0bd0ec633645a73393d027e5f7e12486343e02400c30ecef2b73de00c250c8` | `D:8,D:61,D:62,D:135,R:1:2,R:2:1,R:65:0,R:67:0,R:68:1,R:69:2` |
| 144 | Zerr | 5,937 / 22,328 | `cb01c0aa4222ae8ea1cad16432fe0526036db19fb466213440f042c80a276822` | 10 / 12 / 12 | `100111010110` | `30f4b04c8c70ae1c62b5ed0dfcb3ab09e44f31aad4427af4d0a1ea8ba12abe3f` | `D:3,D:4,D:19,D:37,D:59,D:96,D:104,D:111,R:33:2,R:47:2` |
| 145 | Xerr | 5,941 / 22,344 | `cef53221649d2a6b9cf2eb5bf383d63a994cb34e4e13f56a42437b97824ce5e4` | 10 / 18 / 24 | `110011100100` | `d92ccd70e10b17003e48afac0aabf2ded837dcc8270b15f7f479a6a8bbcae2e5` | `D:77,D:132,R:16:1,R:47:0,R:51:0,R:54:1,R:56:1,R:57:0,R:60:1,R:64:0` |
| 145 | Zerr | 5,923 / 22,272 | `c658ddb038cc22330e96ae7f1730e9e682a925906ce37cb02424575c06497709` | 10 / 16 / 24 | `100101000000` | `64d319b0630ee229b34c4dd2140f432e05abae895abfbc87f01414e967b6006f` | `D:107,D:116,D:120,D:126,R:38:1,R:44:0,R:54:1,R:59:0,R:69:0,R:70:0` |
| 146 | Xerr | 5,972 / 22,468 | `4ef7d4549be52f7fdea353b7f029a8147fc6341ebab1eb909fa18acdafcb70d1` | 10 / 14 / 14 | `110111100100` | `98e817e57f572b27f3e5efa6abc862f361a78c7b0a83c49f8f4c7d840a79d5e1` | `D:51,D:54,D:57,D:63,D:69,D:109,D:131,R:1:1,R:15:2,R:24:2` |
| 146 | Zerr | 5,883 / 22,112 | `d17c8d84d74f445605e6cf9d6e366d931674b3e4ac61309a16f02e9c4bef8436` | 10 / 16 / 18 | `111100000000` | `d60495d55dcca115bc9c1a0fa3fb65a231abdea91f59307806c2da041824d0e6` | `D:16,D:60,D:133,D:141,R:0:1,R:7:0,R:10:2,R:13:0,R:20:1,R:21:0` |
| 147 | Xerr | 5,942 / 22,348 | `3e260cdbb39a9e1148ae833992def8e5239fa60a9eb4a20d45b8c7da3a7e538a` | 10 / 12 / 14 | `001010010000` | `5720621bcb3db7ca92587d07648f279092432eae73e444bebc155dce38fc2782` | `D:47,D:74,D:98,D:138,D:139,R:4:2,R:13:1,R:45:0,R:61:2,R:69:2` |
| 147 | Zerr | 5,934 / 22,316 | `15be04fd9bd0b6dea1a533b8e1a8664f9f370a62c9d758c7786b34032c313c93` | 10 / 14 / 16 | `011111110100` | `c7976f40fd749ca26719759885e1556e55ebda48d175005e870259a7afdb6764` | `D:94,D:114,D:120,D:123,R:8:2,R:15:2,R:38:0,R:49:2,R:55:2,R:71:0` |

### Atomic state/source frontier

| iteration | selectors | selector-state SHA-256 | state-file SHA-256 | source file / semantic SHA-256 | CNF SHA-256 |
|---:|---:|---|---|---|---|
| 136 | 232 | `1692d905120d2dcf51b949ce4a70ed4b8f1b270c2d07a1ddbf5813d20d80fa81` | `58781b46cc177df046ec334420046e1ccc8a23517f21fe4491e6412741ced57c` | `a71fb5e708eeebf365dda0661b79652b264bc0eb87308626383a5ca389cfc5d8` / `a561515801904b458d34ebccea5aa364420f9a0a012e36e721f48fcbe9be4ebe` | `289acad6be1068d63369511e9c95b0b1df146471bf05a1e4128758508612b64e` |
| 137 | 234 | `47792a8f8e757482604723abb0e08916f49b252f4ba07deae03cf4295159d0b6` | `ba670045a69722f9625d04d3f07d62e207db38f15e9323f8c32d89194bb585cd` | `0207760f863b90c715399b887b78123ba0382364e242b58031e7599868a9f452` / `dd16f5db19b6e2cdc6d75446d1029f02f07aa18628f12f6d426e2edfcd658514` | `2f7f7be5cc67822aa30ca9ac8021c79afcb8e15ea4f9724dcc1d3c974ede88e4` |
| 138 | 236 | `b97343946f563b80504e93b287424b29005eb2a71e56b0bf9370790ff79a0f97` | `d523ecf0ff9808b74f460a1ab31d46370fb2274b2cd1a5b1bcf21affa424fcc3` | `1f4420e517f9bff2d55673eba0110853269e46a30b50b160c549744b9a70662f` / `ceb3beed624e626dbec068db0179c5625a58650911baf53c139b7e9964e0688b` | `cf400af11b86f067718ba75a5bdb29e1d5fcde3730a0ef8cd99d6b2b95903fa1` |
| 139 | 238 | `c30cf810e923d41b39c4cb48334e68d1a3ae86983162a63bc70bd2a9d429a615` | `49d19908b0cf0a8fd4dc177cb515b7758798605812b61a3aa3c1c858905fd1e4` | `fb12a5a01b196dda5254825a9f695fc98ab5c4056818c0da73c534cc7bad186a` / `c7f498068e16934517768285ab3a1e1def79482b769fec899c67134b32d50026` | `3a82af909f27caa97d68463ada22814a537f6ece3fe3117bf1eb2298ec3eba24` |
| 140 | 240 | `4156821c4ce9d3a72b66d89bc5795d41db4af8d76b5ccb183a3a2216d59de59f` | `daac489dfaa80c22a304a0e3fa93c4a3017496cdf0dbd208985b05b8a44fc057` | `788012b63fa6e10561ac21933d35ccaddca07b8387fbb08c7998976e059ac9c8` / `a8cb55aa10f19100abca67b82b229c14daa21a5f91e6a634f3747c1fcfe44c9f` | `d908f326aa36be550e7d501e1b5af8f736d3eec3aa4dbe0c22f54d398c20909a` |
| 141 | 242 | `93ab0860bc05a05de7fbdb3dd21a854109f8f2a29ed937c84d578ebe079b2943` | `526181371b98ad24d08fae7c697a2c6f7f1438e9b9031bef5671adf08e21a1a4` | `4767ba65d950cbc3e99a08b1cc6952d02cf94f339fdab9fe7b2c2968a175a285` / `6f03f6d9a3b14027a910e6e7633546eb55b051d070f45e1a6f8579fafaefb9ea` | `1347bcadd5c17d26fe021ce4a3293eb14ed9e57344474e10a9885618ba72cc7d` |
| 142 | 244 | `8db1cb9823a3d3132ad87465aba84f7e3047d57fef9df4c6c31dc743e07caa84` | `b7a5f00c79156643bac89d8904515153d0e3be73cc31ab2bc7801421c0f9f1d0` | `a2310babfcc205c98b92f79151ab309311b2545fd17b54e1d401cc74b306bd18` / `635cf5fde3f940260852bf6bd5d1ea9135892589b96c511c65b7d4f17d3a87e3` | `9865bfe874f93d3be38fc8a82aae5ad00cfaf66c671246c3c75d150810ac73d4` |
| 143 | 246 | `3af337f77f89486bc25366be313607201dc10f048bcac9c5e87355a6ec8afae7` | `694b1db617d86ef4f068c969ca1eec7c982bc35f691be7a7045044281a3f95aa` | `51f03261eefef47a61dbc1a48d0deca91c5afb92931496859220194c4bca18b5` / `ed041895a0992fa1bdc8b0d76d908cc595098f8142d7efabe0c6d17938d4ba15` | `5781637f051643e254e7edd248dca276be33654e8da62127470fec1565bab9ed` |
| 144 | 248 | `15181d24541ff60571cf91577ffa8c85b48d749726e2511438187fac8135a64b` | `7a189eabfe5ef7a35bfa13c5ccf777ed137f6c6ae61309c7506d2bde81026296` | `e14222b07df79854336d6fb94bf0051e3d45836d8e59e1060e613f9ab5d3a5fb` / `3a1e08e3a578a36ae36446b0924af04c462dc33b1fa0134e271798d3e86ee405` | `8351cc28eb27874b4b174411a1bf66d4e9b81bcb1069f6b33ed4c27a2e8a72f5` |
| 145 | 250 | `ab0d6c7a41f876f39e6f94a59c15197a62015e355b7c7e6b173c3850dcbf45bf` | `e5f46b9f2d65e87b122e9224ae9a7d8d4ad11fd71c499c063c7036c7953cf78c` | `57d4e62aeeb989859cd9f6998b230cf087c8750c794bc9478fdc35901cf4c424` / `de40e7a4b19fc6a3c0339f27f982cbdbce17e9ea8e973d7f98b289b031afe012` | `022bfb72723c6f6fc483189e76512a131931931332cdc2202a1a1bbe674b1415` |
| 146 | 252 | `631514478c9ef90c3881ea85fe4e1764043c71c8a16ec2e499e4686b9ea5bc21` | `5035128cf81b9f31edcbf8fa68ec3841d524cdcd9d94b4434f0d64cd23658130` | `b7d33bd44a41913d490f9668d9213cbdb10add1a496af79eede452ec48df473c` / `5d553a53c63a060a2f3f2271da95b91bf9caf3aa0f1322b1cd3613b925917654` | `0363aace88f4e1589b652df293d28d451e6546ae4711d751385eb4233aa8a3c3` |
| 147 | 254 | `0e58e098f6d251179ed857cf644c36f349a70e45d6b42c3a6d37ab72932dd607` | `9d7a7ea0eda8d35673551ec72d1137d08539162c77ce307e3c70cd2f519ab608` | `c1e70f8cf2a4593de911a37cdfd6700cd4176916ddc1ab0e194797d04505666f` / `fe5a95ff149ce08fd1cd483556e917c73d7015725879b2226033c430dede78b5` | `30d73f37d48d5f99760b113912e0f851a3f35997df561cf631a0a18a15e28e7a` |
| 148 | 256 | `9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f` | `1902599acc47eb5d354692759b2d09d6ff1cfcd5e013f2b907cc310376ee6e81` | `0db20ed8ca0b120cda91eb7a94be25094adb9b77a2cacdd322e330a720d58b5f` / `2fd4a1982e1f6389804f7eee1120706f9d26c9e6a23acc05e2a15e036a67c032` | `397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4` |

## 5. Complete outer assignments and legal frozen schedules

For iterations 136--147, each stored assignment gives exactly one truth value for every DIMACS variable, with no omission or duplicate. The two independently retained outer assignments at each iteration decode to the same truth map. I evaluated every literal of all 16,537,519 outer clauses; every clause is satisfied.

I decoded each 10-bit edge time and each extrema word without package code. If `t(e)` is a raw time, deterministic compression is

`c(e) = |{u in used raw times : u < t(e)}|`.

For every candidate this equals the packaged compressed schedule byte-for-byte. The twelve compressed hashes are distinct. Each schedule contains exactly the 864 required named edges, uses nonnegative integer layers with no gaps after compression, has no ancilla/time or data/time collision, satisfies all 648 MC equivalences, and is globally X/Z interleaved. Each misses every inherited order block and makes every prior EFSSC invalid, as the outer formula requires.

The outer formula is existential. These twelve SAT assignments establish only twelve legal candidates outside the then-current finite cover. They do not establish a universal schedule, an absence result, or either value of `D*_Gross`.

## 6. Independent reconstruction and physical replay of all 24 direct formulas

For each candidate and sector I rebuilt the 360 columns from the source geometry: 144 named data singletons `D:q` and `72*3=216` named hook residuals `R:c:k`. The frozen canonical residual-position sets are `{0,1}`, `{3,4,5}`, and `{4,5}`; the corresponding physical ordered suffixes are `{2,3,4,5}`, `{3,4,5}`, and `{4,5}`. I derived the 72 detector rows, 12 logical duals, stabilizer spans, within-check orders, data-check orders, canonical supports, physical suffix supports, and schedule-dependent `u` options.

For primary selection bits `x_j`, every rebuilt direct formula is exactly:

1. 72 parity equations `xor_j(H[b,j] and x_j)=0`;
2. 12 linked logical-parity outputs `l_r=xor_j(<column_j,L_r> and x_j)` and the clause `l_0 or ... or l_11`;
3. an exact sequential-counter encoding of `sum_j x_j <= 10`.

No pool, residual-pattern, check-count, or within-check-order-family restriction occurs. My generated DIMACS, clause JSONL, variable dictionary, column dictionary, body hash, and summary are byte-for-byte equal to the stored artifacts for all 24 formulas. Their aggregate is 142,552 variables and 536,128 clauses. Every complete assignment satisfies every clause. As negative controls, flipping one selected primary bit violates the complete formula, and deleting the first selected name loses the required zero-syndrome/nontrivial condition.

For every selected residual I rebuilt the exact ordered hook suffix from the candidate's physical times. GF(2)-summing all elementary physical faults gives zero detector syndrome, nonzero logical action, and the same 12 logical parities as the canonical representative. Every named location is distinct, schedule legality is unchanged, and the exact named-location count is the direct weight. The weight histogram is `{9: 1, 10: 23}`: iteration-138 Xerr is the sole weight-9 mechanism, with exact names

`D:54,D:95,R:12:2,R:20:2,R:35:1,R:45:0,R:59:2,R:68:1,R:69:0`.

All other Xerr mechanisms and every Zerr mechanism have weight 10. Canonical or physical net-support Hamming weight can be larger because supports cancel and hook representatives differ; it is not the direct-query weight. SAT-side trace streams derive no empty clause and are not refutation certificates. The proof is the complete assignment plus clause and physical replay, and it proves existence only.

## 7. Exact EFSSC soundness and atomic 232-to-256 lineage

For selector `s`, sector `S`, check `c`, and qubit `q`, I reconstructed the exact rank-membership bit

`m[s,c,q](t) = 1 iff rank_t(q within c) belongs to symmetric_difference(residual_positions[k] for k in group_kinds[s,c])`.

Let `sigma[S,q]` be the frozen 84-bit detector/logical signature and `d_s` the XOR of the declared data-support signatures. The symbolic effect is

`E_s(t) = d_s xor xor_(c,q with m=1) sigma[S,q]`.

The selector-valid predicate is exactly “bits 0--71 of `E_s(t)` are zero and at least one of bits 72--83 is one.” The appended outer root is its negation. I reconstructed this circuit from trace gates for every old and new selector and proved its valid literal equals the trace literal. This establishes soundness on the complete frozen `S_Gross` outer domain: the predicate excludes exactly schedules on which that same named mechanism has zero syndrome and nonzero logical action. It does not globalize the mechanism beyond the frozen geometry, sectors, terminal convention, or legal-schedule constraints.

At every source candidate the direct mechanism makes the predicate true. The 24 IDs are exactly `r94-i136-Xerr`, `r94-i136-Zerr`, ..., `r94-i147-Xerr`, `r94-i147-Zerr`; their normalized `(sector, selected_names, data_support, group_kinds)` objects give the selector hashes in the direct table. All 256 final semantic hashes are distinct.

For each transition I independently constructed the two new full selector records, checked exact prefix append, and recomputed the new selector-state hash. The next source is the preceding compact selector prefix plus precisely those two records. Each `pending_intent.json` is `PENDING`; each `atomic_commit.json` is `COMMITTED`; their payloads are identical and bind the new selector IDs, count, state hash/file, source semantic/file, next CNF, and iteration record. `state_promoted_last=true`, every output exists, and the iteration record says state mutation was atomic and repair was not entered. There are exactly twelve transitions, no canceled transition, no failed output in state, no retroactive cut, no duplicate ID or predicate, and no repair output.

## 8. Exact order-3 same-sector GF(2) investigation

The investigation occurs after the iteration-136 transition, at state 137: 234 selectors split exactly into 125 Xerr and 109 Zerr. The declared domain is every unordered triple of distinct selectors within one sector:

`C(125,3) = 317,750`, `C(109,3) = 209,934`, total `527,684`.

My independent `itertools.combinations` loop visited exactly that many triples. For fault-name sets `A,B,C`, it formed the exact named-location result `A symmetric_difference B symmetric_difference C`; no support quotient or sector conversion was used. The complete weight histogram is:

```text
0:1, 5:1, 6:3, 7:34, 8:127, 9:457, 10:3610,
11:5618, 12:47372, 13:12, 14:43, 15:22, 16:205,
17:89, 18:727, 19:331, 20:2094, 21:1180, 22:7536,
23:4460, 24:26479, 25:11124, 26:76490, 27:18834,
28:145729, 29:18420, 30:156686.
```

Thus exactly `1+3+34+127+457+3610 = 4,232` results have named-location weight 1--10; no result has weight 1--4. All 4,232 are novel relative to the 234-state and unique with multiplicity one. The canonical digest of the sorted rows `(sector, exact selected_names, multiplicity)` is `d59f5641c32d7092ba7b7e042e04df6f8c953ab8ed3ee344d294788db1ed66f9`.

I replayed all 4,232 exact name sets through the complete frozen iteration-136 sector model. Every result has nonzero detector syndrome; the miss histogram is exactly `{nonzero_syndrome: 4232}` and zero has trivial/nontrivial ambiguity. The canonical digest of sorted `(sector, exact selected_names, syndrome, logical_parities, nontrivial)` replay rows is `41e09ff51a3a7b10f1b904bd11d7ea58cd640816b9b023cd519db306cad70784`. Zero selector is retained. Removing only the nondeterministic `seconds` field from the packaged synthesis object gives semantic SHA-256 `558a9fcdd88e527fb5a4c49b3e6c268793f6644188f512b5d0af25a971ea1b45`.

The adversarial controls are concrete:

- Cross-sector ambiguity uses the same 19 names `D:102,D:103,D:119,D:125,D:137,D:59,R:35:0,R:45:1,R:48:1,R:55:1,R:55:2,R:57:2,R:60:0,R:62:0,R:67:1,R:68:0,R:68:2,R:69:0,R:7:2`. In Xerr it has net weight 22 and syndrome `{2,4,5,9,10,19,20,25,26,31,36,42,43,54,56,59,61,62,63,64,66,68,69,70}`; in Zerr it has net weight 26 and syndrome `{8,9,11,15,19,21,22,25,30,34,35,36,38,39,40,44,45,47,52,55,63,64,65,66}`. There is no sector-independent XOR effect.
- The first overweight result, `iter42-Xerr xor iter43-Xerr xor iter44-Xerr`, has exact named weight 28 and is rejected before retention. Its names are `D:102,D:103,D:115,D:119,D:125,D:137,D:36,D:42,D:43,D:48,D:52,D:59,D:75,R:22:2,R:26:2,R:35:0,R:36:2,R:37:2,R:43:0,R:44:2,R:45:1,R:48:1,R:48:2,R:51:1,R:62:0,R:70:0,R:70:2,R:7:2`.
- `iter42-Xerr` with names `D:59,D:102,D:103,D:119,D:125,D:137,R:7:2,R:35:0,R:45:1,R:48:1` is valid on its source schedule, but on iteration 136 its syndrome is `{0,14,15,20,21,31,36,42,43,59,61,62,65,69}`. Dynamic validity cannot be schedule-globalized.
- The iteration-136 Xerr mechanism has ten named locations but canonical net-support weight 12. Named fault weight cannot be replaced by net support weight.

This is a complete finite no-go only for order-3, distinct, same-sector combinations of the 234 selectors at that exact frontier, tested for retention on the frozen iteration-136 schedule. It says nothing about mixed sectors, repeated/formally canceled inputs, order 4 or higher, arbitrary mechanisms outside the selector span, other schedules, global exhaustion, direct absence, or either value of `D*_Gross`.

## 9. Fresh iteration 148

The final state has exactly 256 selectors, selector-state SHA-256 `9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f`, state-file SHA-256 `1902599acc47eb5d354692759b2d09d6ff1cfcd5e013f2b907cc310376ee6e81`, `next_iteration=148`, `started=false`, and `stop=null`.

Its source file is `0db20ed8ca0b120cda91eb7a94be25094adb9b77a2cacdd322e330a720d58b5f`; semantic source is `2fd4a1982e1f6389804f7eee1120706f9d26c9e6a23acc05e2a15e036a67c032`. The independently reconstructed formula has 19,138 assertions, 409,157 variables, 1,385,059 clauses, and CNF SHA-256 `397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4`.

There is no `iterations/iter148` directory, no `transitions/iter148*`, and no solver, model, proof, assignment, status, or disposition artifact in the iteration-148 formula directory. It is checked and genuinely unsolved.

## 10. Environment, tooling, and proof controls

The bound interpreter path is a symlink chain

```text
/private/tmp/circdist-r72-dispatcher-venv/bin/python -> python3
python3 -> /Library/Developer/CommandLineTools/usr/bin/python3
```

Running through the venv path gives Python 3.9.6, z3 5.1.0, pysat 1.9.dev15, macOS 26.6.2, arm64. The executable-target SHA-256 is `bdea59019a38eb6600cc9e71e984a97fedadc406448431281e7657030f54987e`. `/usr/bin/python3 -c 'import z3,pysat'` exits 1 with `ModuleNotFoundError: No module named 'z3'`; preserving the venv path is therefore necessary.

| packaged tool | bytes | SHA-256 | observation |
|---|---:|---|---|
| CaDiCaL | 967,144 | `fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9` | Mach-O arm64; version 1.9.5 |
| drat-trim | 70,120 | `f58f63b0f76945d4c4c9ff6e87afaf870f579e67c0f7cca589492df8fc7ebd47` | Mach-O arm64 |
| lrat-check | 36,552 | `bd7eb8052623525814a0a37502b47f05375d9d9dfaf96ddc2fcd858958517cea` | Mach-O arm64 |

The package is not hermetic or cross-platform: the external venv is not copied, and all three packaged native tools require arm64 macOS. Reproduction on another host requires compatible exact APIs/binaries or a freshly validated port.

I independently ran the proof controls. Fixture CNF `b8d28f511bbc3bc5d67e0fcda748b6ad85d5e543c64bc91d09f34ecb10805efd` and DRAT `b6c2e560bb08c84d583ca94799951a21c8cae5de35d6d04d77bc4842e9c18ecd` are accepted; generated LRAT `cf32dfff36b24ba36c3504765f29ecf3d7a8abaa59956ade4d24a4062caa6431` is accepted. Corrupt and truncated DRAT and LRAT controls each exit 1 and are rejected. The six subprocesses are synchronous and reaped. These are fixture-only polarity/conversion controls. No actual Round-94 Gross query is UNSAT and no Gross DRAT/LRAT proof exists.

## 11. Failure ledger, repair boundary, and FIX-2 process closure

All six disclosed incident classes are present and correctly scoped:

1. The first logged-runner creation uses unsupported `Path.write_text(newline=...)` under Python 3.9, exits 1 before a durable runner is written, and is followed by a successful corrected creation. The bootstrap TSV records both the shell wrapper and Python child as reaped.
2. `prepare_reconstruction` first exits 1 only when writing the absent `science/reconstruction` directory. The retry creates it, exits 0, and emits the exact binding/source result.
3. The first iteration-136 Xerr assignment checker exits 1 with `ValueError: I/O operation on closed file`. Its corrected retry reopens the CNF, exits 0, assigns all 6,000 variables, and satisfies all 22,580 clauses.
4. The broad-removal compression probe is recorded as rejected before tool execution. It has no OS child and no filesystem mutation. This particular rejection is necessarily supported by the sealed human/tool ledger rather than an OS record; the process census contains no unexplained child.
5. The preliminary metadata generator uses `Path.resolve()` on the venv path, reaches the base Python without z3/pysat, and exits 1 at the dependency probe. The corrected generator uses the absolute venv path, exits 0, and emits final metadata. No failed-run result or scientific state entered the package.
6. The first sealed replay uses the superseded seals above. It passes both manifests, 13 formula replays, 12 outer iterations, all 24 direct rebuilds/assignments/physical replays, all 12 transitions, and both synthesis controls, then exits 1 only at the tail independent audit because it expects two retained rc1 records after incident 5 makes the exact count three. The assertion is corrected, no science or state byte changes, the package is resealed, and a full final replay succeeds.

The 217 bounded package process records have return-code census `0:178`, normal CaDiCaL SAT `10:36`, and disclosed/repaired `1:3`. The three rc1 names are exactly `direct_iter136_Xerr_assignment_check`, `prepare_reconstruction`, and `round94_make_package_metadata_preliminary`. Every record says reaped, not detached, not timed out. The 36 science solver intervals (12 outer and 24 direct) are strictly nonoverlapping. There are no unknowns, timeouts, UNSAT-checker failures, atomic rollback failures, repair entries, background jobs, or unreported structured-process failures.

FIX-2 records 217 bounded records, 36 science solvers, 6 synchronous proof-control children, 10 synchronous repository-validator children, and a 117-child successful preseal replay. Both Round-94 scratch roots are removed; the replay-temp glob is empty; the process scan finds zero matches; the only retained dependency is the explicitly handed-off interpreter. Protected identity remains exact.

As a separate review check I ran:

```sh
CIRCDIST_PYTHON=/private/tmp/circdist-r72-dispatcher-venv/bin/python \
ROUND94_REPOSITORY=/private/tmp/circdist-r95-replay-repo \
ROUND94_REPLAY_RECORD=/private/tmp/circdist-r95-package-replay.json \
./circdist/artifacts/circdist_gross_proof_outer_round94_20260830/replay.sh
```

The disposable repository held the historically bound scheduler/node/review and a link to the reviewed Round-92 package. Output was `MANIFESTS_PASS` and `ROUND94_PACKAGE_REPLAY_PASS 117`. The replay record, SHA-256 `9874934f6eb3765c97a8e05f4318a7c7495cf597cbb62e2f8eadc4def020d7a7`, has 117/117 return codes zero, `all_children_reaped=true`, and `detached_processes=0`. This corroborates rather than replaces the clean-room derivations.

Reviewer-side process disclosure: both full clean-room runs were single foreground Python processes with no subprocess; both passed. The proof-control driver reaped six children, sealed replay reaped 117, and the final clone-overlay driver reaped the clone child plus ten validator children. Two early scratch-only YAML-builder attempts exited 1 on reviewer guard assertions (a line-offset assertion, then a mistaken route-level key); both were reaped and wrote no repository file. Two scratch review-QA attempts also exited 1 and were reaped: the first used an overly broad placeholder-word sentinel, while the second correctly caught one trailing space in the scratch proposed YAML. One attempted final rerun on the older hardlink overlay reached prior-state and CIRCDIST rc0, then its all-project child exited 1 because unrelated concurrent repository edits had changed shared hardlinked node inodes while their newly added files were absent from that old directory snapshot. That child and driver were reaped; the live all-project gate immediately returned 0, so the stale overlay was discarded. The byte was removed, the node hash above was recomputed, and a fresh isolated APFS clone overlay passed every gate on the corrected bytes. Every inspection/generation command was foreground and returned. No reviewer background or detached job was started.

## 12. Evidence-closure census

Before linking, the live checker exits 1 with exactly 1,570 nonblank lines. Every line is unique and has the exact form `ERROR: circdist: unlinked evidence: <path>`; every path lies under the sole Round-94 package. There is no duplicate, non-package path, or other diagnostic.

The package's earlier retained log has exactly 1,537 unique package-local diagnostics. Set subtraction gives exactly 33 added paths and zero removed paths. The delta is fully explained:

- 3 final indexes: `FILE_INVENTORY.jsonl`, `PAYLOAD_SHA256SUMS.txt`, `SHA256SUMS.txt`;
- 12 process/stream files for final package installation, final metadata, postinstall protected snapshot, and repository validators;
- 2 final scripts: `source/final_preseal_checks.py`, `source/fix2_cleanup.py`;
- 5 final/failure records: audit recheck, closure interpretation, first-sealed failure, final preseal checks, FIX-2 closure;
- 11 validator/final-summary files: evidence-closure run/stdout/stderr, parser run/stdout/stderr, repository-validator summary, validator-driver run/stdout/stderr, and validation summary.

The exact 33-path list was compared as a set, not inferred from counts. The final 1,570 count governs; the stale 1,537 wording is pre-final and must not be reused as final closure evidence.

## 13. Licensed YAML delta and disposable linked overlay

The proposed complete node is 74,438 bytes, 849 LF, SHA-256 `f84492190a1dad3b5d69bf38a9a62d3212f0c3844ee3338dc96517fbb0671135`. A structural guard parses old and new YAML, erases only four licensed locations in the new object, and requires total equality:

- append Round-95 continuation wording to `assessment.summary`;
- append exactly two evidence rows, 64 to 66, with all 64 old rows identical and in order;
- replace only `frontier.dstar-residual.task` with the reviewed iteration-148 frontier;
- append exactly one review event, 17 to 18, with all 17 old events identical and in order.

The claim, caveats, assessment level, both routes and their levels, all old evidence, and all old events are unchanged. `assessment.level` and `routes.gap-via-lift.assessment.level` both remain `CONJECTURED`.

A first disposable hardlink overlay passed all ten gates on the semantically identical proposal. Because unrelated concurrent workspace edits can propagate through shared hardlink inodes, the final exact-byte run used `/bin/cp -cR` to create the isolated APFS copy-on-write overlay `/private/tmp/circdist-r95-final-overlay`. I replaced only its node with the corrected proposed bytes and installed the complete review at its licensed path. The clone child and ten gates ran serially with bytecode writes disabled; every child was reaped and returned 0:

| gate | result |
|---|---:|
| prior nodes/routes/events retained against Round-94 `bindings/initial_proof_dag` | 0 |
| proof DAG, `--problem circdist` | 0 |
| proof DAG, `--problem all` | 0 |
| evidence closure, `--problem circdist` | 0 |
| CIRCDIST migration | 0 |
| release contracts | 0 |
| DAG contracts | 0 |
| Lean DAG selftest | 0 |
| duplicate-YAML scan | 0 |
| `git diff --check` | 0 |

Observed details: prior state retained; CIRCDIST has 16 valid node files; the all-project gate validates all ten current project registries; evidence closure reports `162 structured paths; all evidence project-local and linked`; migration preserves 16 nodes, 143 original events, and 728 byte-identical copies; release contracts pass 14/14; DAG contracts pass 24/24; Lean selftest passes 23/23 assertions; duplicate scan covers 890 files and 23,364 mappings with zero duplicates. The overlay is disposable and no canonical node was installed by this reviewer.

## 14. Epistemic scope

What this review licenses is precise: 12 further positive outer candidates, 24 positive unrestricted direct mechanisms, 24 sound exact finite-domain EFSSC exclusions, an exact atomic frontier at 256 selectors, and a complete negative result for the declared order-3 same-sector synthesis domain on iteration 136. The new continuation may start only from the exact fresh iteration-148 state and formula recorded above.

What it does not license is equally precise. There is no actual Gross UNSAT, no direct-sector absence, no repair entry, no outer exhaustion, no distance-12 schedule, no universal distance-11 ceiling, no proof that higher-order or arbitrary synthesis is exhausted, and no closure theorem. Positive SAT assignments and SAT traces prove existence, not absence. The fixture proof controls do not turn any Gross query into UNSAT. Therefore the root, route, and interval remain unchanged.

## Appendix A — complete non-importing clean-room checker

```python
#!/usr/bin/env python3
"""Round95 clean-room audit. Standard library only; imports no package code."""
from pathlib import Path, PurePosixPath
from collections import Counter, defaultdict
from itertools import combinations, permutations
import gzip, hashlib, json, math, os, sys, time, gc

REPO=Path('<repo>')
R=REPO/'circdist/artifacts/circdist_gross_proof_outer_round94_20260830'
R92=REPO/'circdist/artifacts/circdist_gross_proof_outer_round92_20260830'
OUT=Path('/private/tmp/circdist-r95-cleanroom-result.json')
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
assert len(files)==1571
assert sum(p.stat().st_size for p in files)==314_978_755
assert sum(p.read_bytes().count(b'\n') for p in files)==3_966_756

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
assert len(inv)==1568 and [x['path'] for x in inv]==sorted(x['path'] for x in inv)
assert len({x['path'] for x in inv})==len(inv)
assert {x['path'] for x in inv}==actual-{'FILE_INVENTORY.jsonl','SHA256SUMS.txt','PAYLOAD_SHA256SUMS.txt'}
for x in inv:
 b=(R/x['path']).read_bytes(); assert (len(b),b.count(b'\n'),sha_bytes(b))==(x['bytes'],x['lines'],x['sha256'])
seals={'files':len(files),'bytes':sum(p.stat().st_size for p in files),'lf':sum(p.read_bytes().count(b'\n') for p in files),
 'root':sha_file(R/'SHA256SUMS.txt'),'payload':sha_file(R/'PAYLOAD_SHA256SUMS.txt'),'inventory':sha_file(R/'FILE_INVENTORY.jsonl'),
 'report':sha_file(R/'REPORT.md'),'result':sha_file(R/'RESULT.json')}
assert seals=={'files':1571,'bytes':314978755,'lf':3966756,'root':'1e0a4af8591aa63ccccd1b2516c630eccb11a73fb9dea2e0ff1e0d32ed82ac1c','payload':'c39ef3552e461dd7513812b8296901e72369dfacbf6e71ae758b5bb58ed94c54','inventory':'6d7efec34aeae4af05d269ec59a9dda4662d8da927c3c200515a3bbbbf1bc05a','report':'83a2db0af31ef3c87c0f67dcc88051f6bb95100b3d567f86c611c9921ee58419','result':'0a291feb16e04935558462bf61fd2f6833a85d6d81d11802c49d4391529ff047'}
print('R95_CLEANROOM_MANIFEST_PASS',json.dumps(seals,sort_keys=True),flush=True)

# Exact live and inherited bindings.
live={'scheduler':sha_file(REPO/'operations/circdist/SCHEDULER.yaml'),'node':sha_file(REPO/'circdist/proof-dag/nodes/CIRCDIST.gross.yaml'),'review93':sha_file(REPO/'circdist/reviews/circdist_gross_proof_outer_weight9_exact_review_round93_20260830.md')}
assert live=={'scheduler':'5a794463e956fc2bad257976a18d2872240788ed23a23f576564727ef113e90b','node':'c3b03597c496ace59bb84f5d4e4cfb1540b98e193dcba9f67adb0abd657bc3f3','review93':'76a07f9d73fda5ced83818361eed24cd83b4ed7fc5a11c13b0fc027df4feb65d'}
# Snapshot hashes; scheduler is deliberately its historical package input.
assert sha_file(R/'bindings/operations__circdist__SCHEDULER.yaml')=='4da1d0f15ddcdb7542cc69507661231807dad97edf684d578d5010c13b9b2383'
assert sha_file(R/'bindings/circdist__proof-dag__nodes__CIRCDIST.gross.yaml')==live['node']
assert sha_file(R/'bindings/circdist__reviews__circdist_gross_proof_outer_weight9_exact_review_round93_20260830.md')==live['review93']
# Round92 manifests and inherited exact bytes.
assert sha_file(R92/'SHA256SUMS.txt')=='4e255084bdab13ad0b9c295a9fe7cf2aea8231c4a56db656964f0695ddc6c982'
assert sha_file(R92/'PAYLOAD_SHA256SUMS.txt')=='fbc881f0dc54744cb3cfd0c4497571592f8597326ce98362eb42a032ed289090'
for a,b in [(R/'state/iter136_state.json',R92/'continuation/final_state.json'),(R/'formulas/iter136/source.json.gz',R92/'formulas/iter136/source.json.gz'),(R/'formulas/iter136/outer.cnf.gz',R92/'formulas/iter136/outer.cnf.gz'),(R/'formulas/iter136/assertion_map.jsonl.gz',R92/'formulas/iter136/assertion_map.jsonl.gz'),(R/'formulas/iter136/circuit_trace.json.gz',R92/'formulas/iter136/circuit_trace.json.gz'),(R/'formulas/iter136/metadata.json',R92/'formulas/iter136/metadata.json'),(R/'formulas/iter136/encoding_check.json',R92/'formulas/iter136/encoding_check.json')]: assert a.read_bytes()==b.read_bytes()
state136=load(R/'state/iter136_state.json')
assert state136['next_iteration']==136 and state136['started'] is False and state136['stop'] is None and state136['selector_count']==len(state136['selectors'])==232
state_keys=('mechanism_id','sector','selected_names','data_support','group_kinds','selector_semantic_sha256')
assert objsha([{k:s.get(k) for k in state_keys} for s in state136['selectors']])==state136['selector_state_sha256']=='1692d905120d2dcf51b949ce4a70ed4b8f1b270c2d07a1ddbf5813d20d80fa81'
assert sha_file(R/'state/iter136_state.json')=='58781b46cc177df046ec334420046e1ccc8a23517f21fe4491e6412741ced57c'
iter136paths=[p.relative_to(R92).as_posix() for p in R92.rglob('*') if p.is_file() and 'iter136' in p.as_posix()]
assert sorted(iter136paths)==sorted([f'formulas/iter136/{x}' for x in ['assertion_map.jsonl.gz','circuit_trace.json.gz','encoding_check.json','metadata.json','outer.cnf.gz','source.json.gz']])
print('R95_CLEANROOM_BINDINGS_PASS',json.dumps(live,sort_keys=True),flush=True)

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
for i in range(136,149):
 s,m,o=check_formula(i);sources[i]=s;metas[i]=m;formula.append(o);print('R95_CLEANROOM_FORMULA_PASS',i,o['vars'],o['clauses'],o['cnf'],flush=True)
# Sources have exact selector prefixes and frozen base.
base=sources[136]
for i in range(137,149):
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

outer=[];direct=[];schedules=set();states={136:state136};new_selectors={}
for i in range(136,148):
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
  ns={'mechanism_id':f'r94-i{i}-{label}','source_iteration':i,'sector':label,'fault_count':len(sel),'selected_names':names,'data_support':data,'group_kinds':groups,'source_schedule_sha256':cand['compressed_schedule_sha256'],'source_times':comp,'canonical_support':bits(can),'physical_support':bits(phys),'source_atoms':atoms,'source_atom_count':len(atoms),'origin':f'round94_proof_outer_iteration{i}_direct360','source_symbolic_validity':'True','selector_semantic_sha256':selhash}
  constructed.append(ns)
  direct.append({'i':i,'sector':label,'vars':len(E.vars),'clauses':len(E.cls),'formula':sha_bytes(dimacs),'weight':len(sel),'names':names,'canonical_weight':bin(can).count("1"),'physical_weight':bin(phys).count("1"),'syndrome':[],'logical':pp,'selector':selhash})
 assert [x['mechanism_id'] for x in constructed]==[f'r94-i{i}-Xerr',f'r94-i{i}-Zerr'];new_selectors[i]=constructed
 # Exact state transition and source compact append.
 prev=states[i];nxt=load(R/f'state/iter{i+1}_state.json');states[i+1]=nxt
 assert nxt['selectors']==prev['selectors']+constructed and nxt['selector_count']==len(nxt['selectors'])==prev['selector_count']+2 and nxt['next_iteration']==i+1 and nxt['started'] is False and nxt['stop'] is None
 sh=objsha([{k:s.get(k) for k in state_keys} for s in nxt['selectors']]);assert sh==nxt['selector_state_sha256'] and len({s['selector_semantic_sha256'] for s in nxt['selectors']})==len(nxt['selectors'])
 compact_keys=('mechanism_id','source_iteration','sector','fault_count','selected_names','data_support','group_kinds','source_schedule_sha256','origin','selector_semantic_sha256')
 assert sources[i+1]['selectors']==sources[i]['selectors']+[{k:s[k] for k in compact_keys} for s in constructed]
 rec=load(I/'record.json');assert rec['new_selectors']==[x['mechanism_id'] for x in constructed] and rec['state_after_sha256']==sh and rec['source_selector_state_sha256']==prev['selector_state_sha256'] and rec['state_mutated_atomically'] is True and rec['repair_entered'] is False
 payload={'cnf_sha256':metas[i+1]['cnf_sha256'],'new_selector_ids':[x['mechanism_id'] for x in constructed],'record_file_sha256':sha_file(I/'record.json'),'selector_count':nxt['selector_count'],'selector_state_sha256':sh,'source_file_sha256':sha_file(R/f'formulas/iter{i+1}/source.json.gz'),'source_semantic_sha256':sources[i+1]['semantic_payload_sha256'],'state_file_sha256':sha_file(R/f'state/iter{i+1}_state.json')}
 pend=load(R/f'transitions/iter{i}_to{i+1}/pending_intent.json');com=load(R/f'transitions/iter{i}_to{i+1}/atomic_commit.json');assert pend['payload']==com['payload']==payload and pend['status']=='PENDING' and com['status']=='COMMITTED' and pend['state_promoted_last'] is True and com['state_promoted_last'] is True and com['all_outputs_present'] is True
 print('R95_CLEANROOM_ITERATION_PASS',i,'outer',nv,nc,'direct',[(x['sector'],x['weight']) for x in direct[-2:]],flush=True)

# Fresh iteration148 is genuinely unstarted/unsolved.
s148=states[148];assert sha_file(R/'state/iter148_state.json')=='1902599acc47eb5d354692759b2d09d6ff1cfcd5e013f2b907cc310376ee6e81' and s148['selector_count']==256 and s148['selector_state_sha256']=='9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f' and s148['next_iteration']==148 and s148['started'] is False and s148['stop'] is None
assert not (R/'iterations/iter148').exists() and not any(R.glob('transitions/iter148*'))
for term in ('solver','model','proof','assignment','status','disposition'):
 assert not any(term in p.name.lower() for p in (R/'formulas/iter148').iterdir())
assert formula[-1]['source_file']=='0db20ed8ca0b120cda91eb7a94be25094adb9b77a2cacdd322e330a720d58b5f' and formula[-1]['source_semantic']=='2fd4a1982e1f6389804f7eee1120706f9d26c9e6a23acc05e2a15e036a67c032' and formula[-1]['cnf']=='397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4' and (formula[-1]['assertions'],formula[-1]['vars'],formula[-1]['clauses'])==(19138,409157,1385059)

# Exact same-sector order-3 enumeration, independent implementation.
sel=states[137]['selectors'];assert len(sel)==234
by={'Xerr':[],'Zerr':[]}
for x in sel:
 sem={k:x.get(k) for k in ('sector','selected_names','data_support','group_kinds')};assert objsha(sem)==x['selector_semantic_sha256'];by[x['sector']].append((x,frozenset(x['selected_names'])))
assert {k:len(v) for k,v in by.items()}=={'Xerr':125,'Zerr':109}
expected=math.comb(125,3)+math.comb(109,3);seen=0;hist=Counter();eligible=novmult=0;novel={};existing={(x['sector'],tuple(sorted(x['selected_names']))) for x in sel};over=None
for sector in ('Xerr','Zerr'):
 for (sa,A),(sb,B),(sc,C) in combinations(by[sector],3):
  seen+=1;S=A^B^C;w=len(S);hist[w]+=1
  if w>10 and over is None:over={'sector':sector,'input_ids':[sa['mechanism_id'],sb['mechanism_id'],sc['mechanism_id']],'exact_symmetric_difference_weight':w,'selected_names':sorted(S)}
  if not 1<=w<=10:continue
  eligible+=1;key=(sector,tuple(sorted(S)))
  if key in existing:continue
  novmult+=1;novel.setdefault(key,0);novel[key]+=1
assert seen==expected==527684 and eligible==novmult==len(novel)==4232 and all(v==1 for v in novel.values())
sec136={s:Sector(sources[136],s,load(R/'iterations/iter136/outer/candidate.json')['compressed_times']) for s in ('Xerr','Zerr')};miss=Counter();syndrome_rows=[]
novel_rows=[{'sector':sector,'selected_names':list(names),'multiplicity':novel[(sector,names)]} for sector,names in sorted(novel)]
for (sector,names),mult in sorted(novel.items()):
 v=sec136[sector].verify_names(list(names));assert not v['ok']
 syndrome_rows.append({'sector':sector,'selected_names':list(names),'syndrome':v['syndrome'],'logical_parities':v['logical_parities'],'nontrivial':v['nontrivial']})
 miss['nonzero_syndrome' if v['syndrome'] else 'logical_trivial' if not v['nontrivial'] else 'other']+=1
assert miss=={'nonzero_syndrome':4232}
triple=load(R/'synthesis/triple_gf2_closure.json');assert triple['finite_domain']['unordered_distinct_triples_enumerated']==seen and triple['finite_domain']['sector_counts']=={'Xerr':125,'Zerr':109} and {int(k):v for k,v in triple['counts']['result_weight_histogram_all_triples'].items()}==dict(hist) and triple['counts']['unique_novel_eligible_results']==4232 and triple['counts']['exact_candidate_valid_results_retained']==0 and triple['retained_terms']==[] and triple['rejected_relaxation_counterexamples']['overweight_result']==over
z=dict(triple);z.pop('seconds');assert objsha(z)=='558a9fcdd88e527fb5a4c49b3e6c268793f6644188f512b5d0af25a971ea1b45'
# Cross-sector and schedule-local controls.
cross=triple['rejected_relaxation_counterexamples']['cross_sector_xor'];names=cross['symmetric_difference_names'];assert sec136['Xerr'].verify_names(names,360)==cross['Xerr_effect'] and sec136['Zerr'].verify_names(names,360)==cross['Zerr_effect'] and cross['Xerr_effect']!=cross['Zerr_effect']
relax=load(R/'synthesis/relaxation_controls.json');sc=relax['schedule_globalization_counterexample'];ss=next(x for x in state136['selectors'] if x['mechanism_id']==sc['selector_id']);srcsec=Sector(sources[136],ss['sector'],ss['source_times']);assert srcsec.verify_names(ss['selected_names'])==sc['source_schedule_verification'] and sec136[ss['sector']].verify_names(ss['selected_names'])==sc['iteration136_schedule_verification'] and sc['source_schedule_verification']['ok'] and not sc['iteration136_schedule_verification']['ok']
fw=relax['fault_weight_quotient_counterexample'];assert fw['fault_location_weight']==10 and fw['net_data_support_weight']==12
tripleout={'sector_counts':{k:len(v) for k,v in by.items()},'domain':seen,'histogram':dict(sorted(hist.items())),'eligible':eligible,'unique':len(novel),'misses':dict(miss),'retained':0,'semantic':objsha(z),'novel_rows_sha256':objsha(novel_rows),'syndrome_replay_rows_sha256':objsha(syndrome_rows)}
print('R95_CLEANROOM_TRIPLE_PASS',json.dumps(tripleout,sort_keys=True),flush=True)

# Process ledger, strict serialization, incidents, protected identity, stale seal separation.
proc=load(R/'PROCESS_LEDGER.json');records=proc['records'];assert len(records)==217 and proc['bounded_foreground_records']==217 and proc['science_solver_children']==36 and proc['outer_solver_children']==12 and proc['direct_solver_children']==24 and proc['all_children_reaped'] and proc['survivors']==proc['timeouts']==proc['background_processes']==proc['detached_processes']==0
assert all(x['reaped'] and not x['detached'] and not x['timed_out'] for x in records)
solvers=sorted([x for x in records if x['returncode']==10 and 'cadical_proof' in x['name']],key=lambda x:x['started_unix']);assert len(solvers)==36 and all(a['ended_unix']<=b['started_unix'] for a,b in zip(solvers,solvers[1:]))
fails=[(x['name'],x['returncode']) for x in records if x['returncode'] not in (0,10)];assert fails==[('direct_iter136_Xerr_assignment_check',1),('prepare_reconstruction',1),('round94_make_package_metadata_preliminary',1)]
boot=(R/'logs/bootstrap-processes.tsv').read_text();assert 'failed logged-runner creation' in boot and 'TypeError before durable runner write' in boot
first=load(R/'verification/failures/first_sealed_replay_stale_failure_count.json');assert first['first_seal_status']=='SUPERSEDED' and first['first_seal_root_sha256']=='476dbea3f8fd2b785508cd2f9330f1ff94568549a5a3d0fecf690dbaebce7150' and first['first_seal_payload_sha256']=='aa97afb5bf5292146da5f1166f05e57e1737f10671ac7d3f3db374e748d0f93b' and first['formula_replays_passed']==13 and first['iteration_replays_passed']==12 and first['synthesis_controls_passed'] and not first['scientific_mismatch'] and first['repair_or_scientific_state_changed'] is False and first['first_seal_root_sha256']!=seals['root'] and first['first_seal_payload_sha256']!=seals['payload']
pre=load(R/'verification/protected_tree_preinstall.json');post=load(R/'verification/protected_tree_postinstall.json');cmp=load(R/'verification/protected_tree_compare.json');assert pre==post and cmp['file_count']==227 and cmp['canonical_and_protected_paths_unchanged'] and cmp['byte_hash_inventory_equal']
fix=load(R/'verification/fix2_closure.json');assert fix['status']=='PASS' and fix['all_task_children_reaped'] and fix['survivors']==fix['detached_processes']==fix['os_background_processes_started']==0 and fix['task_process_matches']==[] and fix['replay_temp_glob_matches']==[] and fix['science_solver_children']==36 and fix['bounded_records_in_package']==217
processout={'bounded':217,'science':36,'outer':12,'direct':24,'failures':fails,'strict_nonoverlap':True,'superseded_root':first['first_seal_root_sha256'],'final_root':seals['root'],'survivors':0}
print('R95_CLEANROOM_PROCESS_PASS',json.dumps(processout,sort_keys=True),flush=True)

result={'status':'PASS','seconds':round(time.time()-T0,3),'seals':seals,'live':live,'formulas':formula,'outer':outer,'direct':direct,'triple':tripleout,'process':processout,'fresh':formula[-1]}
OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print('R95_CLEANROOM_ALL_PASS',len(formula),len(outer),len(direct),round(time.time()-T0,3),flush=True)
```

## Appendix B — exact auxiliary commands and structural guard

```sh
# Live prelink closure census
/usr/bin/python3 tools/evidence_closure_check.py --problem circdist \
  > /private/tmp/r95-evidence-prelink.txt

# Proof controls (output record retained in scratch for the review)
/private/tmp/circdist-r72-dispatcher-venv/bin/python \
  circdist/artifacts/circdist_gross_proof_outer_round94_20260830/source/check_proof_controls.py \
  --root circdist/artifacts/circdist_gross_proof_outer_round94_20260830 \
  --output /private/tmp/circdist-r95-proof-controls.json

# Linked-overlay gates, run serially from /private/tmp/circdist-r95-overlay
/usr/bin/python3 tools/proof_dag_check.py --problem circdist \
  --previous-state /private/tmp/circdist-r95-overlay/circdist/artifacts/circdist_gross_proof_outer_round94_20260830/bindings/initial_proof_dag
/usr/bin/python3 tools/proof_dag_check.py --problem circdist
/usr/bin/python3 tools/proof_dag_check.py --problem all
/usr/bin/python3 tools/evidence_closure_check.py --problem circdist
/usr/bin/python3 tools/check_circdist_migration.py
/usr/bin/python3 tools/test_release_contracts.py
/usr/bin/python3 tools/test_dag_contracts.py
/usr/bin/python3 tools/lean_dag_check.py --selftest
/usr/bin/python3 circdist/artifacts/circdist_gross_proof_outer_round94_20260830/source/duplicate_yaml_scan.py \
  --root /private/tmp/circdist-r95-overlay \
  --output /private/tmp/circdist-r95-overlay-results/duplicate_yaml.result.json
git diff --check
```

The core parsed-object guard was:

```python
old = yaml.safe_load(open(live_node))
new = yaml.safe_load(open(proposed_node))
assert new['assessment']['level'] == 'CONJECTURED'
assert new['routes']['gap-via-lift']['assessment']['level'] == 'CONJECTURED'
assert new['assessment']['basis']['evidence'][:-2] == old['assessment']['basis']['evidence']
assert list(new['events'])[:-1] == list(old['events'])
assert len(new['assessment']['basis']['evidence']) == len(old['assessment']['basis']['evidence']) + 2
assert len(new['events']) == len(old['events']) + 1
probe = copy.deepcopy(new)
probe['assessment']['summary'] = old['assessment']['summary']
probe['assessment']['basis']['evidence'] = old['assessment']['basis']['evidence']
probe['frontier']['dstar-residual']['task'] = old['frontier']['dstar-residual']['task']
probe['events'] = old['events']
assert probe == old
```

## Appendix C — sole complete licensed replacement for `CIRCDIST.gross.yaml`

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
    CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}. Round 95''s fresh independent exact review clears the sealed Round-94 package for proposer-level continuation only: iterations 136--147 add 24 exact EFSSC selectors after twelve legal outer SAT schedules and twenty-four unrestricted direct-sector SAT/physical replays; the complete same-sector order-3 GF(2) search retains zero terms; and the fresh frontier is unstarted iteration 148 with 256 selectors and checked-unsolved CNF sha256:397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4. No Gross UNSAT, direct absence, repair, exhaustion, D* narrowing, route promotion, or root promotion is licensed; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
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
    task: 'Continue only from the independently reviewed sealed fresh/unstarted iteration 148 state. The inherited sound order-block
      library remains exactly 14,484 predicates (1,440 unary, 20 round-62, 12,820 generalized, and 204 dynamic), and the exact
      fixed-selector frontier is 256 EFSSCs: the reviewed 232-selector Round-93 frontier plus the 24 exact candidate-domain
      selectors from iterations 136--147. Bind selector-state sha256:9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f,
      state-file sha256:1902599acc47eb5d354692759b2d09d6ff1cfcd5e013f2b907cc310376ee6e81, iteration-148 semantic-source
      sha256:2fd4a1982e1f6389804f7eee1120706f9d26c9e6a23acc05e2a15e036a67c032, and source-file sha256:0db20ed8ca0b120cda91eb7a94be25094adb9b77a2cacdd322e330a720d58b5f
      before use. Its deterministic 10-bit compressed finite-outer formula has 19,138 source assertions, 409,157 variables,
      1,385,059 clauses and CNF sha256:397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4; it was checked but deliberately
      not solved, and no iteration-148 solver/model/DRAT/LRAT disposition is inherited. The complete same-sector order-3 GF(2)
      search at the post-iteration-136 234-selector frontier retained zero terms after replaying all 4,232 novel weight-at-most-10
      outputs, but this licenses a no-go only for that exact finite domain and frozen iteration-136 schedule; it does not cover
      mixed sectors, order 4 or higher, arbitrary mechanisms, or global exhaustion. For a SAT result, retain the complete assignment,
      replay every DIMACS clause and frozen schedule condition, then rebuild and adjudicate both complete unrestricted direct-360
      sectors; a positive mechanism kills only that concrete candidate domain and proves no absence, and only exact source-schedule-valid
      EFSSC selectors may be added atomically. For an UNSAT result, retain a complete DRAT proof, independently accept it, generate
      LRAT, and independently accept the LRAT with valid/corrupt/truncated controls. Enter repair only after both direct sectors
      have independently checked absence. Preserve frozen S_Gross, strict serialization, MC0, terminal residual semantics,
      both CSS sectors, and every existing exclusion against morphing, Circ-Preserve substitutions, alternate conflict models,
      exploratory pair clauses, retroactive cuts, stale compressor provenance, mixed-sector XOR, support-weight substitution,
      and schedule-globalized dynamic predicates. Keep CIRCDIST.gross and gap-via-lift CONJECTURED and D*_Gross in {11,12};
      this reviewed continuation supplies no Gross UNSAT, absence, exhaustion, distance-12 witness, universal distance-11 ceiling,
      route promotion, or root promotion.'
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
```
