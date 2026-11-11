CLEAR-PROPOSER-LEVEL-CONTINUATION

# Round 87 independent exact review of the sealed CIRCDIST.gross EFSSC package

## Licensed consequence

The sealed Round-86 package is clean for **proposer-level continuation only**. This review licenses one canonical evidence/frontier bookkeeping replacement, reproduced byte-for-byte below, and a fresh process beginning at iteration 109. It does not license a root or route promotion, a distance-12 witness, a universal distance-11 ceiling, an UNSAT/exhaustion claim, inheritance, or any narrowing of `D*_Gross in {11,12}`. `CIRCDIST.gross` and its live `gap-via-lift` route remain `CONJECTURED`. The preserved final formula was not solved.

The review was authorized by scheduler Round 87. The live scheduler was 210,740 bytes at `sha256:74d7dd33d8f38741a509c0abf4228b198ee59dd8b807b0600102ac959a0f9872`; the read-only live node was 55,666 bytes at `sha256:a8ab9d9c5b98840d90dbd76f2edf8943ad4e6c1fba2e037456c675f425dfa2d0`. No canonical YAML, scheduler, prior review, package, generated index, or protocol was edited in this session.

## Seals, inventory, and input binding

The package contains **138 files** totaling **58,856,346 bytes** and **1,565,092 LF bytes**. There are **20 descendant directories**; the report's 21 counts the package root as a directory. The root manifest has 137 rows and the payload manifest 136 rows. `FILE_INVENTORY.jsonl` has 135 pre-seal payload rows and intentionally omits itself and both subsequently written manifests. There are no symlinks.

- `SHA256(SHA256SUMS.txt)` = `94322390a648262e8cc035f8e843617f134fe2d29ff36191720b646c021c89ff`.
- `SHA256(PAYLOAD_SHA256SUMS.txt)` = `443b84ce18c568bdd6b88c4737d03b222b518897eecab787ffa1cc43718f182b`.
- `REPORT.md` = 21,588 bytes, `sha256:86bd003012c274d22632996f6e1c8804f6b8193b0c7535660057b594dd1bba03`.
- Bound Round-80 package = 1,221 files / 303,862,955 bytes; all 1,220 root rows and 1,219 payload rows independently rehashed; seals `e086a828391361620eabfbd31b544606f7817826af546fb8779a500f95ec0426` and `8f71dc39916cdab9d57ff2add15e5130631600b2789d7da0bd5626afdfdc202d`.
- Bound Round-81 review = 35,936 bytes / `sha256:e0d6ad5b54768195516239f4d0a262135025a630ecd6292d91cb694baa51597e`; packaged copy byte-identical.
- All 23 bound current inputs matched their sealed hashes except the scheduler alone, whose change from the Round-86 input hash to the exact Round-87 authorization hash above is expected dispatcher state. The frozen node, problem statement, DAG/FILE protocols, closeout, Round-80 manifests/model/data, and Round-81 review matched exactly.

Fresh package replay used Python 3.9.6, Z3 5.1.0 and PySAT 1.9.dev15. PID 99244 exited 0 after 62.817598 s and ended with `ROUND86_PACKAGE_REPLAY_PASS`; every one of the 137 root-manifest rows printed `OK`.

## EFSSC theorem, rederived

Fix one sector and a named selector. Data faults contribute singleton masks. A residual `R:c:k` contributes the within-check positions `P0={0,1}`, `P1={3,4,5}`, or `P2={4,5}`. Multiple residuals on check `c` add over GF(2), so their net position set is the symmetric difference `Q_c=△_k P_k`. For qubit `q`, define `rank_c(q)=Σ_{r≠q}[t(c,r)<t(c,q)]`. Strict ancilla serialization makes the six times distinct, hence the ranks are a bijection onto `{0,…,5}` and there is no tie branch. Therefore `[rank_c(q)∈Q_c]` is exactly the coefficient of `q` in the canonical residual aggregate.

Let `σ(q)` concatenate 72 detector parities and 12 logical-dual parities. Linearity gives each compiled bit as the XOR of the data signature and the membership-selected qubit signatures. Thus the first 72 compiled bits are all zero iff the aggregate has zero terminal syndrome. The last twelve are not all zero iff its logical-dual signature is nonzero. The reviewer rebuilt the Gross matrices and obtained `rank(HX)=rank(HZ)=66`, `rank(HZ∪LZ)=rank(HX∪LX)=78`, full 12-by-12 logical pairing rank 12, and `k=144−66−66=12`. The rank-66 stabilizer space lies in the kernel of the 78 detector-plus-dual rows; equal dimensions make it the entire kernel. Consequently, inside zero syndrome, nonzero logical-dual signature is equivalent in both directions to a nonstabilizer logical class. This proves the advertised iff, not just its easy direction.

For kind 0 the canonical `{0,1}` mask differs from the physical `{2,3,4,5}` suffix by the full weight-6 check stabilizer. Kinds 1 and 2 are physically identical to their canonical suffixes. XORing several selected residuals therefore changes canonical to physical support only by stabilizer rows; syndrome and all logical parities agree. The reviewer checked this separately on all fourteen mechanisms. This is terminal-residual/direct-360 reasoning only.

## Reviewer-authored reconstruction

A standard-library-only reviewer program, importing no Round-86 code, rebuilt the 144-qubit Gross checks, rank-66 CSS spaces, 1,884 weight-12 static logicals per sector, quotient bases, all 864 edge names, 648 overlaps, the 14,484 inherited blocks, all selectors, schedules and mechanisms. Its final run (PID 99694) exited 0 in 7.418182 s with `R87_REVIEWER_INDEPENDENT_AUDIT_PASS`. It checked 134/134 source truth assignments and exact selector semantic hashes. The first 120 were rebound field-for-field to the sorted Round-80 raw ledger.

The 14,484 blocks were independently reconstructed as 720 X unary + 720 Z unary + 20 Round-62 + 12,820 generalized + 204 dynamic. Every unary check exhaustively caught all 360 bad orders and zero of 360 good orders. Every one of the seven new schedules hit zero old blocks and zero EFSSCs preceding its iteration. Later cuts were never used retroactively.

### Fourteen new selectors and exact domains

| selector | sec | data support | residual groups | selected names | valid tuples | source cube | factor |
|---|---:|---|---|---|---:|---:|---:|
| `iter102-Xerr` | Xerr | `[2, 49, 78, 103, 123, 124, 125]` | `{'25': [1], '63': [0], '71': [0]}` | `['D:2', 'D:49', 'D:78', 'D:103', 'D:123', 'D:124', 'D:125', 'R:25:1', 'R:63:0', 'R:71:0']` | 165,888 | 82,944 | 2 |
| `iter102-Zerr` | Zerr | `[1, 23, 24, 47, 57, 84, 122, 131]` | `{'45': [2], '52': [0]}` | `['D:1', 'D:23', 'D:24', 'D:47', 'D:57', 'D:84', 'D:122', 'D:131', 'R:45:2', 'R:52:0']` | 2,304 | 2,304 | 1 |
| `r86-i103-Xerr` | Xerr | `[50, 57, 66, 85, 107, 126, 131, 133]` | `{'0': [0], '63': [2]}` | `['D:50', 'D:57', 'D:66', 'D:85', 'D:107', 'D:126', 'D:131', 'D:133', 'R:0:0', 'R:63:2']` | 2,304 | 2,304 | 1 |
| `r86-i103-Zerr` | Zerr | `[42, 45, 46, 47, 105, 107, 116, 118]` | `{'36': [0], '38': [2]}` | `['D:42', 'D:45', 'D:46', 'D:47', 'D:105', 'D:107', 'D:116', 'D:118', 'R:36:0', 'R:38:2']` | 2,304 | 2,304 | 1 |
| `r86-i104-Xerr` | Xerr | `[33, 39, 73, 113, 128, 129]` | `{'12': [0], '22': [2], '26': [0], '27': [0]}` | `['D:33', 'D:39', 'D:73', 'D:113', 'D:128', 'D:129', 'R:12:0', 'R:22:2', 'R:26:0', 'R:27:0']` | 5,308,416 | 5,308,416 | 1 |
| `r86-i104-Zerr` | Zerr | `[13, 14, 15, 71, 72, 74, 79]` | `{'11': [1], '12': [0], '15': [0]}` | `['D:13', 'D:14', 'D:15', 'D:71', 'D:72', 'D:74', 'D:79', 'R:11:1', 'R:12:0', 'R:15:0']` | 165,888 | 82,944 | 2 |
| `r86-i105-Xerr` | Xerr | `[61, 116, 127]` | `{'47': [0, 2], '48': [0, 2], '50': [1], '54': [0], '56': [2]}` | `['D:61', 'D:116', 'D:127', 'R:47:0', 'R:47:2', 'R:48:0', 'R:48:2', 'R:50:1', 'R:54:0', 'R:56:2']` | 764,411,904 | 5,308,416 | 144 |
| `r86-i105-Zerr` | Zerr | `[33, 98, 108, 110, 116]` | `{'34': [2], '43': [1], '44': [2], '45': [2], '52': [2]}` | `['D:33', 'D:98', 'D:108', 'D:110', 'D:116', 'R:34:2', 'R:43:1', 'R:44:2', 'R:45:2', 'R:52:2']` | 382,205,952 | 191,102,976 | 2 |
| `r86-i106-Xerr` | Xerr | `[]` | `{'0': [1], '13': [1], '15': [1], '28': [0], '35': [2], '45': [0, 1], '5': [1], '8': [0], '9': [1]}` | `['R:0:1', 'R:5:1', 'R:8:0', 'R:9:1', 'R:13:1', 'R:15:1', 'R:28:0', 'R:35:2', 'R:45:0', 'R:45:1']` | 25,678,369,290,977,280 | 80,244,904,034,304 | 320 |
| `r86-i106-Zerr` | Zerr | `[9, 52, 94, 100, 103, 141]` | `{'16': [2], '20': [0], '8': [0], '9': [2]}` | `['D:9', 'D:52', 'D:94', 'D:100', 'D:103', 'D:141', 'R:8:0', 'R:9:2', 'R:16:2', 'R:20:0']` | 5,308,416 | 5,308,416 | 1 |
| `r86-i107-Xerr` | Xerr | `[49, 54]` | `{'23': [1], '48': [0], '58': [0], '61': [1], '63': [0], '66': [1], '67': [1], '70': [2]}` | `['D:49', 'D:54', 'R:23:1', 'R:48:0', 'R:58:0', 'R:61:1', 'R:63:0', 'R:66:1', 'R:67:1', 'R:70:2']` | 285,315,214,344,192 | 8,916,100,448,256 | 32 |
| `r86-i107-Zerr` | Zerr | `[47, 104]` | `{'27': [0], '4': [2], '43': [2], '56': [1], '59': [1, 2], '62': [1], '66': [1]}` | `['D:47', 'D:104', 'R:4:2', 'R:27:0', 'R:43:2', 'R:56:1', 'R:59:1', 'R:59:2', 'R:62:1', 'R:66:1']` | 4,953,389,137,920 | 61,917,364,224 | 80 |
| `r86-i108-Xerr` | Xerr | `[64, 68, 134]` | `{'55': [2], '57': [1, 2], '60': [2], '63': [2], '70': [0, 2]}` | `['D:64', 'D:68', 'D:134', 'R:55:2', 'R:57:1', 'R:57:2', 'R:60:2', 'R:63:2', 'R:70:0', 'R:70:2']` | 637,009,920 | 10,616,832 | 60 |
| `r86-i108-Zerr` | Zerr | `[11, 93, 122]` | `{'12': [0], '28': [2], '44': [0], '48': [1], '58': [0], '64': [2], '68': [2]}` | `['D:11', 'D:93', 'D:122', 'R:12:0', 'R:28:2', 'R:44:0', 'R:48:1', 'R:58:0', 'R:64:2', 'R:68:2']` | 880,602,513,408 | 440,301,256,704 | 2 |

For each participating check the reviewer enumerated all `6! = 720` orders and independently computed the exact 84-bit signature multiplicity. A meet-in-the-middle XOR join split the checks, bucketed the right half by its 72-bit syndrome, and for each left state subtracted exactly the unique right 12-bit logical signature that would make the total logical signature zero. All arithmetic was integral. Every source cube had zero invalid tuples. Exact totals are 25,969,520,291,556,096 valid tuples and 89,663,440,921,344 source-cube tuples, with nine strict expansions, five equal cases and maximum factor 320. These are sums of multiplicities on fourteen different local Cartesian spaces, not a union cardinality. As a concrete overlap control, each of the seven source schedules satisfies both same-schedule selectors: fourteen selector incidences but seven unique schedules.

### Seven schedules and fourteen direct mechanisms

| iter | schedule SHA-256 | layers | MC/conflicts | old hits | prior EFSSC survivors | X canonical/physical net wt | Z canonical/physical net wt |
|---:|---|---:|---|---:|---:|---:|---:|
| 102 | `e52aa6f1aceb1fde6d39e06f124b738dd574eb83e0066d498e6788593d414ed2` | 344 | 0 / 0 | 0 | 0 | 12/16 | 12/12 |
| 103 | `57c38511202175a99afc77c28275c101f0c16ff22cb47b7f67bc3c26384d720c` | 278 | 0 / 0 | 0 | 0 | 12/12 | 12/14 |
| 104 | `2fb5bff2497e52a64f2b75b291b33d2637863511afaa6863522110818733a7ec` | 331 | 0 / 0 | 0 | 0 | 12/18 | 14/16 |
| 105 | `d1985dae0ad8fb4c31cf742a936712ccbc88e65930a5f371cb5e53ec8a07dffa` | 308 | 0 / 0 | 0 | 0 | 12/16 | 12/12 |
| 106 | `4f9580e59fd193254f26c33c96c747a58393b53f2f2d01bed60e39904c46cc3e` | 233 | 0 / 0 | 0 | 0 | 20/24 | 14/18 |
| 107 | `679cf3c5a5cf1b739894a28a622ada6866de0fbdf3168cf8461f9f75116ebe09` | 278 | 0 / 0 | 0 | 0 | 18/18 | 14/16 |
| 108 | `423dc6a174e31353d7a37d34a45465d2a9bbb4dae82c6e3544410e06a2f4d191` | 279 | 0 / 0 | 0 | 0 | 14/12 | 16/20 |

Each schedule has exactly the frozen 864 named edges, compressed nonnegative integer times, strict data and ancilla serialization, zero MC0 violations over 648 overlaps, and global X/Z interleaving. Each stored mechanism names ten distinct columns in the full 360-column universe (144 data plus 216 residual), has zero canonical syndrome, nonzero logical class, zero physical syndrome, physical nontriviality, and identical canonical/physical logical parity. The stored selected indices, names, supports, order atoms and positive replays were rebuilt. Positive SAT mechanisms reject only those candidates and say nothing about absence.

For sealed seed iteration 102, the reviewer parsed every DIMACS clause, every complete solver assignment, the variable dictionaries and clause JSONL ledgers. Xerr: 5,966 variables, 22,444 clauses, `sha256:ff345e6e7cb8679f6d9f54936f07e9de2e17a8bb18e15ac3539060540680401c`; Zerr: 5,927 variables, 22,288 clauses, `sha256:f76a9cd441902f8f3af95fc5e61210121eae9ee976bc7b8e0672665a06b35553`. Both assignments set all variables, satisfy every clause, and select exactly ten primary columns. Both summaries say `complete_query:true` and explicitly exclude pool, residual-pattern, check-count, and within-check-family restrictions. The six later records do not seal raw CNFs; their positive mechanisms were instead rebuilt directly from the full 360-column semantics, which is sufficient to validate the asserted SAT witnesses but would not support an absence claim.

## Atomic state and formula

| transition | selectors before→after | prefix hashes verified | solved formula assertions | direct disposition |
|---|---:|---|---:|---|
| 103 | 122→124 | `534b0f9a2372086f7260cf39bc48da6dc5f232e4c51373fce054f158c3a5ac21` → `316c1b99d98cdba5f7ab32275659741c71c16e08c0aa020cd7dbf6fefcc96797` | 19,004 | X/Z SAT; no repair |
| 104 | 124→126 | `316c1b99d98cdba5f7ab32275659741c71c16e08c0aa020cd7dbf6fefcc96797` → `fbc0a547eb1d61063be2179423e01c8abbb2b1df239cb8343e4cbe7d3b7fe989` | 19,006 | X/Z SAT; no repair |
| 105 | 126→128 | `fbc0a547eb1d61063be2179423e01c8abbb2b1df239cb8343e4cbe7d3b7fe989` → `e68360697730a0f4ed3b9c2b340f31c4567aa18389927bbff3870c64913835e6` | 19,008 | X/Z SAT; no repair |
| 106 | 128→130 | `e68360697730a0f4ed3b9c2b340f31c4567aa18389927bbff3870c64913835e6` → `7c6d6cacda9af3d5324a329360c11dc591239f0f804f0994fee32884cb164d69` | 19,010 | X/Z SAT; no repair |
| 107 | 130→132 | `7c6d6cacda9af3d5324a329360c11dc591239f0f804f0994fee32884cb164d69` → `6786748b97a21108683068711352190d0fc105c8913c6c1c87249bc419c9429c` | 19,012 | X/Z SAT; no repair |
| 108 | 132→134 | `6786748b97a21108683068711352190d0fc105c8913c6c1c87249bc419c9429c` → `9be75eba643ac167d5c51497ca8e5cd23eb1656f803a49cbd8e7f1285b004113` | 19,014 | X/Z SAT; no repair |

The checkpoint selectors are exactly equal to final-state selectors; completed iterations are exactly 103–108; selector count is 134; selector-state hash is `9be75eba643ac167d5c51497ca8e5cd23eb1656f803a49cbd8e7f1285b004113`; next iteration is 109; `started:false`; stop is null. Base legality plus 14,484 blocks gives 18,882 assertions, and adding 134 EFSSCs gives 19,016. The final formula is `sha256:94d404da1777ef108a2a508dc55ca0f3fda68bc489482a00337d9acb7317ac4d`. It was intentionally not solved after installing the last pair.

A separate reviewer-owned rebuild imported frozen Round-80 model/outer code but no Round-86 compiler. It made no solver call, rebuilt 852 rank and 2,274 membership expressions, parsed 19,016 assertions on each side, and found 0 unequal corresponding ASTs. Its normalized AST hash is `6ac624f2acb35a6311034829970b4d2993fcdf208080898a8e1dbeff1dcb3c7d`. The sealed compiler raw hash is `94d404da1777ef108a2a508dc55ca0f3fda68bc489482a00337d9acb7317ac4d`; the proposer fresh-printer hash is `95562d673d6ea31fd6f47d1be6cb4b60b45ff9fbe7079e574c0b2d8c80ac159b`; the reviewer printer produced a third raw hash `9ff1cc3274f1ed5d4780fb08b93cec9744345bd3fe46b05f2a1f9ada1dbd4216` (13,484,667 bytes). All parse to the same ordered assertion vector, so the differences are printer serialization only. Negating the last reviewer assertion makes it structurally unequal and changes the serialization hash, a negative control.

## Adversarial controls and scope

- Changing `R:25:1` to `R:25:0` in `iter102-Xerr` changes the semantic hash to `9bd63ee441ae57ad1346e8a46207ff62c16b64feae06ece467357d4721608106` and makes source validity false.
- Colliding `X:0:1` and `X:0:2` produces one endpoint conflict and is rejected.
- Replacing the last selected fault name by a duplicate is rejected before mechanism use.
- The per-selector-sum-as-union reading fails dimensionally and concretely (14 incidences on 7 source schedules); the package expressly disclaims it.
- Scope stayed at frozen `S_Gross`: fixed Gross code/checks/edges, strict endpoint serialization, MC0, terminal residuals, both CSS sectors, positive static-distance premise and global interleaving. No morphing, Circ-Preserve, alternate conflict graph, or conflict-model leakage appeared.

## Disclosed development failures

The package preserves, and does not cite as successes: (1) the seed compiler Z3-5.1 variadic-Xor API rejection before solving/state write; (2) PID 97169 full-DP census terminated and reaped after 140.7 s at 14,361,591,808-byte maximum RSS / 49,598,090,208-byte peak footprint before selector 9, with no accepted aggregate; and (3) the raw-SMT byte-hash checker rejection. The successful binary-XOR compiler, exact MITM census (all fourteen), and exact parsed/normalized-AST comparison replace those paths. No partial failed output entered state.

Reviewer development also stopped twice on overstrong reviewer assertions (assuming all inherited selectors had exact rather than at-most weight 10; then expecting an exception rather than a structured duplicate rejection). PIDs 99642 and 99654 exited 1; the assertions were narrowed without changing package data. Final reviewer runs PIDs 99671 and 99694 passed. Two unit-test invocations from the repository root failed only because those test modules require the `tools` script directory on `sys.path`; direct-script reruns then passed 14/14 and 24/24. These are invocation/authoring failures, not evidence.

## Evidence closure and disposable installation

Before any hypothetical link, `tools/evidence_closure_check.py --problem circdist` exited 1 with exactly **138** distinct errors. Their path set is exactly equal to all 138 files beneath `circdist/artifacts/circdist_gross_efssc_round86_20260830`; there were no missing links, nonlocal paths, or unrelated unlinked files. This is the expected sealed-but-unlinked class.

A hard-linked disposable repository overlay replaced only the Gross node copy and added a review-path placeholder. Results: proof-DAG structure 16/16, evidence closure clean with 154 structured paths, migration 16 nodes / 143 original events / 728 byte-identical copies, release contracts 14/14, DAG contracts 24/24, Lean selftest 23/23, and duplicate-key scan 735 YAML files / zero errors. `git diff --check` on the live repository exited 0. The live working tree already contains extensive unrelated historical/untracked state; this review added only the one review file.

## FIX-2 process accounting

All load-bearing jobs were foreground and strict serial. No network was used, no background job was handed off, and no SAT solver was launched by the reviewer. The following supervisor entries include every reviewer-declared foreground job, including failed development/invocation attempts:

| id | PID | seconds | exit | final | command | log |
|---|---:|---:|---:|---|---|---|
| `initial_scan` | 99064 | 0.142631 | 0 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/initial_scan.py` | `/tmp/circdist_round87_20260830/initial_scan.log` |
| `read_targets` | 99080 | 0.048818 | 0 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/read_targets.py` | `/tmp/circdist_round87_20260830/read_targets.log` |
| `extract_scheduler` | 99102 | 0.044837 | 0 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/extract_scheduler.py` | `/tmp/circdist_round87_20260830/extract_scheduler.log` |
| `scheduler_round87_only` | 99206 | 0.048557 | 0 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/scheduler_round87_only.py` | `/tmp/circdist_round87_20260830/scheduler_round87_only.log` |
| `package_core_print` | 99232 | 0.024234 | 0 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/package_core_print.py` | `/tmp/circdist_round87_20260830/package_core_print.log` |
| `package_replay` | 99244 | 62.817598 | 0 | exited | `/usr/bin/env CIRCDIST_PYTHON=/private/tmp/circdist-r72-dispatcher-venv/bin/python ./replay.sh` | `/tmp/circdist_round87_20260830/package_replay.log` |
| `read_verification_short` | 99287 | 0.02479 | 0 | exited | `/usr/bin/python3 -c from pathlib import Path; p=Path('verification/evidence_closure.stdout.log'); print(p.read_text()); print(Path('verification/previous_state.stdout.log').read_text()); print(Path('verification/proof_dag_circdist.stdout.log').read_text()); print(Path('verification/migration.stdout.log').read_text())` | `/tmp/circdist_round87_20260830/read_verification_short.log` |
| `schema_inspect` | 99304 | 0.209341 | 0 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/schema_inspect.py` | `/tmp/circdist_round87_20260830/schema_inspect.log` |
| `print_code_segments` | 99331 | 0.048791 | 0 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/print_code_segments.py` | `/tmp/circdist_round87_20260830/print_code_segments.log` |
| `print_state_replay` | 99361 | 0.024344 | 0 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/print_state_replay.py` | `/tmp/circdist_round87_20260830/print_state_replay.log` |
| `print_round68_build` | 99389 | 0.042892 | 0 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/print_round68_build.py` | `/tmp/circdist_round87_20260830/print_round68_build.log` |
| `print_rebuild` | 99499 | 0.048908 | 0 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/print_rebuild.py` | `/tmp/circdist_round87_20260830/print_rebuild.log` |
| `independent_audit` | 99642 | 3.224158 | 1 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/independent_audit.py` | `/tmp/circdist_round87_20260830/independent_audit.log` |
| `independent_audit_v2` | 99654 | 7.123268 | 1 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/independent_audit.py` | `/tmp/circdist_round87_20260830/independent_audit_v2.log` |
| `independent_audit_v3` | 99671 | 6.832024 | 0 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/independent_audit.py` | `/tmp/circdist_round87_20260830/independent_audit_v3.log` |
| `independent_audit_v4` | 99694 | 7.418182 | 0 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/independent_audit.py` | `/tmp/circdist_round87_20260830/independent_audit_v4.log` |
| `inventory_audit` | 99718 | 0.1484 | 1 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/inventory_audit.py` | `/tmp/circdist_round87_20260830/inventory_audit.log` |
| `inventory_audit_v2` | 99759 | 0.150368 | 1 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/inventory_audit.py` | `/tmp/circdist_round87_20260830/inventory_audit_v2.log` |
| `inventory_rows_probe` | 99840 | 0.04569 | 0 | exited | `/usr/bin/python3 -c from pathlib import Path;import json;p=Path('circdist/artifacts/circdist_gross_efssc_round86_20260830/FILE_INVENTORY.jsonl');r=[json.loads(x) for x in p.read_text().splitlines()];print(len(r));print(r[0]);print(r[-1])` | `/tmp/circdist_round87_20260830/inventory_rows_probe.log` |
| `inventory_audit_v3` | 99871 | 0.625874 | 0 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/inventory_audit.py` | `/tmp/circdist_round87_20260830/inventory_audit_v3.log` |
| `reviewer_formula_rebuild` | 99909 | 22.057394 | 0 | exited | `/private/tmp/circdist-r72-dispatcher-venv/bin/python /tmp/circdist_round87_20260830/reviewer_formula_rebuild.py` | `/tmp/circdist_round87_20260830/reviewer_formula_rebuild.log` |
| `read_validation_commands` | 99924 | 0.024609 | 0 | exited | `/usr/bin/python3 -c from pathlib import Path;p=Path('circdist/artifacts/circdist_gross_efssc_round86_20260830/verification'); for n in ['evidence_closure.stderr_time.log','dag_contracts.stderr_time.log','release_contracts.stderr_time.log','lean_selftest.stderr_time.log','migration.stderr_time.log','previous_state.stderr_time.log','proof_dag_circdist.stderr_time.log','git_diff_check.stderr_time.log']:  print('===',n);print((p/n).read_text())` | `/tmp/circdist_round87_20260830/read_validation_commands.log` |
| `read_build_log` | 99943 | 0.048719 | 0 | exited | `/usr/bin/python3 -c from pathlib import Path;print(Path('circdist/artifacts/circdist_gross_efssc_round86_20260830/logs/build.log').read_text())` | `/tmp/circdist_round87_20260830/read_build_log.log` |
| `inspect_validator_cli` | 99961 | 0.045953 | 0 | exited | `/usr/bin/python3 -c from pathlib import Path; for f in ['tools/evidence_closure_check.py','tools/proof_dag_check.py','tools/check_circdist_migration.py','tools/lean_dag_check.py','tools/test_release_contracts.py','tools/test_dag_contracts.py']:  print('===',f);print('\n'.join(Path(f).read_text().splitlines()[-45:]))` | `/tmp/circdist_round87_20260830/inspect_validator_cli.log` |
| `evidence_closure_prelink` | 99983 | 0.506625 | 1 | exited | `/usr/bin/python3 tools/evidence_closure_check.py --problem circdist` | `/tmp/circdist_round87_20260830/evidence_closure_prelink.log` |
| `count_evidence_failures` | 109 | 0.048304 | 0 | exited | `/usr/bin/python3 -c from pathlib import Path;root=Path('<repo>');pkg=root/'circdist/artifacts/circdist_gross_efssc_round86_20260830';L=Path('/tmp/circdist_round87_20260830/evidence_closure_prelink.log').read_text().splitlines();pref='ERROR: circdist: unlinked evidence: ';x=[line[len(pref):] for line in L if line.startswith(pref)];expected={str(p.relative_to(root)) for p in pkg.rglob('*') if p.is_file()};print(len(x),len(set(x)),len(expected),set(x)==expected);print('other_error_lines', [l for l in L if l.startswith('ERROR:') and not l.startswith(pref)])` | `/tmp/circdist_round87_20260830/count_evidence_failures.log` |
| `inspect_node_structure` | 128 | 0.090404 | 0 | exited | `/usr/bin/python3 -c from pathlib import Path;import yaml,json;p=Path('circdist/proof-dag/nodes/CIRCDIST.gross.yaml');x=yaml.safe_load(p.read_text()); print('top',list(x));print('assessment',list(x['assessment']));print('basis',list(x['assessment']['basis']));print('evidence_count',len(x['assessment']['basis']['evidence']));print('evidence_tail',json.dumps(x['assessment']['basis']['evidence'][-8:],indent=2));print('frontier',json.dumps(x.get('frontier'),indent=2));print('routes',json.dumps(x.get('routes'),indent=2));print('events_count',len(x['events']));print('events_tail',json.dumps(list(x['events'].items())[-10:],indent=2))` | `/tmp/circdist_round87_20260830/inspect_node_structure.log` |
| `build_candidate_overlay` | 174 | 4.498607 | 0 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/build_candidate_overlay.py` | `/tmp/circdist_round87_20260830/build_candidate_overlay.log` |
| `overlay_proof_dag` | 477 | 0.261868 | 0 | exited | `/usr/bin/python3 tools/proof_dag_check.py --problem circdist` | `/tmp/circdist_round87_20260830/overlay_proof_dag.log` |
| `overlay_evidence_closure` | 480 | 0.390524 | 0 | exited | `/usr/bin/python3 tools/evidence_closure_check.py --problem circdist` | `/tmp/circdist_round87_20260830/overlay_evidence_closure.log` |
| `overlay_migration` | 481 | 0.858495 | 0 | exited | `/usr/bin/python3 tools/check_circdist_migration.py` | `/tmp/circdist_round87_20260830/overlay_migration.log` |
| `overlay_release_contracts` | 482 | 0.090341 | 1 | exited | `/usr/bin/python3 -m unittest tools.test_release_contracts` | `/tmp/circdist_round87_20260830/overlay_release_contracts.log` |
| `overlay_dag_contracts` | 483 | 0.048128 | 1 | exited | `/usr/bin/python3 -m unittest tools.test_dag_contracts` | `/tmp/circdist_round87_20260830/overlay_dag_contracts.log` |
| `overlay_lean_selftest` | 487 | 0.150373 | 0 | exited | `/usr/bin/python3 tools/lean_dag_check.py --selftest` | `/tmp/circdist_round87_20260830/overlay_lean_selftest.log` |
| `overlay_release_contracts_v2` | 493 | 0.210736 | 0 | exited | `/usr/bin/python3 tools/test_release_contracts.py` | `/tmp/circdist_round87_20260830/overlay_release_contracts_v2.log` |
| `overlay_dag_contracts_v2` | 496 | 0.382822 | 0 | exited | `/usr/bin/python3 tools/test_dag_contracts.py` | `/tmp/circdist_round87_20260830/overlay_dag_contracts_v2.log` |
| `overlay_duplicate_yaml_scan` | 556 | 4.616792 | 0 | exited | `/usr/bin/python3 /tmp/circdist_round87_20260830/duplicate_yaml_scan.py` | `/tmp/circdist_round87_20260830/overlay_duplicate_yaml_scan.log` |

Supervisor PID 99057 was the only review process alive at serialization. Finalization requires and performs its explicit quit/reap immediately after artifact hashing; the final response must not issue unless `R87_SUPERVISOR_DONE` is observed. Package-local replay children were synchronous descendants of PID 99244 and all exited before that parent; the survivor scan found no EFSSC compiler, replay, analyzer, CaDiCaL, or overlay-validation child.

## Sole licensed canonical replacement

Replace `circdist/proof-dag/nodes/CIRCDIST.gross.yaml` byte-for-byte with the following UTF-8/LF document, including its terminal LF. It is **57,967 bytes** at **`sha256:f42dd0333a8faea3858cefcd859c0343ab33aedf2a6a1e663f2fa1625701288e`**. The parsed root claim is unchanged (claim-string `sha256:fc22f602b9bfd9e38fa69d7fc1d00b973c7a634e6c400662eaccd38c8ec0f180`), all 56 prior root evidence items and 12 prior events are preserved, two structured evidence items and two events are added, the route mapping is byte-semantically unchanged, and both root and live route remain `CONJECTURED`.

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
    task: Continue only in a fresh outer process from the independently reviewed sealed Round-86 state at fresh/unstarted
      iteration 109. The inherited order-block library remains exactly 14,484 predicates (1,440 unary, 20 round-62, 12,820
      generalized, 204 dynamic), and the exact fixed-selector frontier is 134 EFSSCs (120 reviewed Round-80 selectors plus
      fourteen Round-86 selectors from iterations 102--108). Bind selector-state sha256:9be75eba643ac167d5c51497ca8e5cd23eb1656f803a49cbd8e7f1285b004113
      and the preserved 19,016-assertion formula sha256:94d404da1777ef108a2a508dc55ca0f3fda68bc489482a00337d9acb7317ac4d before
      use. The final formula was intentionally not solved. For every SAT candidate, rebuild both complete unrestricted direct-360
      sectors, clause-check any sealed complete assignment, and raw-replay canonical and physical mechanisms before an atomic
      transition. Install only selectors valid on that source schedule, and exclude only their exact EFSSC validity domains.
      Tentative synthesis remains in memory until exhaustive retained validation passes; later cuts may not be used retroactively.
      A positive mechanism kills only its candidate and proves no absence. No UNSAT, exhaustion, distance-12 witness, or universal
      distance-11 ceiling is inherited from Round 86. Retain direct absence only after a candidate-specific proof-producing
      run, independent DRAT acceptance, generated LRAT and independent LRAT acceptance with valid/corrupt/truncated controls;
      enter repair only after both sectors have checked absence. Keep frozen S_Gross, strict serialization, MC0, terminal
      residual semantics, both CSS sectors, and the existing prohibition on morphing, Circ-Preserve substitutions, alternate
      conflict models, the 15,874 exploratory round-63 pair clauses, and stale compressor provenance.
    kind: task
    since: '2026-08-28'
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
```

## Final limitation

This review clears only the exact sealed package and the licensed continuation state. Iteration 109 remains fresh/unstarted. A later SAT candidate still needs complete two-sector certification; an outer UNSAT result still needs an accepted proof object or independent exhaustive certificate. No canonical root status can change merely because continuation is cleared.

The review file cannot contain its own ordinary SHA-256 without changing the bytes being hashed. Its exact post-write byte count and SHA-256 are therefore computed after serialization and reported with delivery; the complete licensed node SHA above is non-self-referential and fixed inside this artifact.
