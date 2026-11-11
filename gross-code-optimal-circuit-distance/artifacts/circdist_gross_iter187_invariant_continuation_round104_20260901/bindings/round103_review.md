# Exact independent review of the Gross global-closure Round-102 package (Round 103)

**Review date:** 2026-09-01  
**Package:** `circdist/artifacts/circdist_gross_global_closure_round102_20260901`  
**Review mode:** one fresh reviewer, strict serial execution, no subagents, no contact with the proposer or any prior worker/reviewer  
**Canonical action taken:** none; the scheduler, protocols, canonical Gross node, prior review, and sealed package were read-only  
**Verdict:** **CLEAR-PROPOSER-LEVEL-CONTINUATION**

## 1. Verdict and exact scope

The package is sealed correctly and its corrected scientific result is sound at its declared scope. I independently reconstructed the frozen Gross geometry, the complete order-72 translation action, the inherited and new formulas, all six direct-360 models, the full block and selector orbit closure, the corrected lex encoding, the complete corrected SAT assignment, the fresh iteration-187 frontier, compressed solver streams, process/failure records, and the replay interface. The corrected invariant quotient is equisatisfiable with the **full invariant base**, and only that base. Its SAT model and both eventual complete direct-sector SAT models replay physically. The 144 corrected translated selectors are sound and were added only after bilateral adjudication.

The first 330-selector quotient is scientifically retracted as a global quotient. I found a fresh complete model of its base formula whose only cut-free group translate is the identity, while the orbit's lexicographically least translate is `(1,5)` and hits 75 untranslated installed block cuts. Thus the orbit-representative argument fails exactly as feared. The old quotient and old base happen both to be SAT, but that coincidental truth-value agreement does not supply an equisatisfiability theorem or an orbit-complete quotient. No global coverage, UNSAT, exhaustion, or absence conclusion from the flawed quotient survives.

Its positive evidence is separable and safe: its complete SAT assignment, legal schedule, Xerr/Zerr direct assignments, physical effects, and all translated witness orbits were independently replayed without using the invalid quotient theorem. They justify exact source-schedule-valid selectors only. Full closure of those selectors does not import the flawed lex clauses into the corrected base.

The package has one real packaging/interface defect: the root has no conventional `replay.sh`. This caused the dispatcher’s recorded pre-launch `rc=127` and launched no science process. Neither the current schema nor the reviewed science requires that exact filename, and the sealed source entry is present and succeeds under the bound interpreter. I therefore rule the defect **nonblocking for proposer-level linking**, but it must remain disclosed and future packages should restore the conventional root entry.

Neither permitted root branch is proved:

* there is no explicit legal frozen Gross schedule with independently certified circuit distance 12; and
* there is no proof that every legal frozen Gross schedule has circuit distance at most 11.

Accordingly `CIRCDIST.gross` remains **CONJECTURED**, `gap-via-lift` remains **CONJECTURED**, and the exact residual remains

\[
D^*_{\mathrm{Gross}}\in\{11,12\}.
\]

This review licenses canonical installation of the reviewed Round-102 evidence and the fresh iteration-187 frontier, not a route or root promotion. A complete proposed replacement YAML is embedded in Section 18.

## 2. Authorization, immutable bindings, and identity separation

I first read the current `CIRCDIST.md`, `DAG_PROTOCOL.md`, `FILE_PROTOCOL.md`, proof-DAG schema/checker, evidence-closure tooling, current scheduler, canonical Gross node, and commissioned Round-101 review. The package is bound to the pre-proposer scheduler; the live scheduler has legitimately advanced to the Round-103 review authorization. I did not substitute one for the other.

| object | SHA-256 | bytes | LF | ruling |
|---|---|---:|---:|---|
| package-bound pre-proposer scheduler (`bindings/scheduler.yaml`) | `02cb4b7a02963451adf962dfc59fa3eb11ef8f71d7b2b2c49d89e6bc61e2c8f5` | 274,811 | 3,257 | exact dispatch binding |
| live scheduler at review authorization | `21bc418abd3cfaaaeac0a6d98b2f223963e9ad84c8210819659fb1564c1176c3` | 279,898 | 3,311 | later authorization state; not proposer input |
| package-bound and live canonical Gross node | `09290d2fb1d4f3c97e0ce503f9f5750a090df1b34b0114dcc9c6542733476dd4` | 92,199 | 992 | unchanged |
| commissioned Round-101 exact review | `8eb817e0af24df1d17af5cdd778cfa7180a1c6c60ca6c87d81ad3c5ad549ca88` | 159,949 | 1,684 | exact prior-review dependency |
| root `SHA256SUMS.txt` | `80e70f62075a852355029b765cbe7ebfa4f8156d25b6d9fa2ea1ddbb9e19b4f4` | 85,304 | 724 | exact |
| `PAYLOAD_SHA256SUMS.txt` | `d0f7c5257a779f63f7015409cafc19b18da2bb02b76f190c62e878059e82b5f9` | 85,215 | 723 | exact |
| `FILE_INVENTORY.jsonl` | `9c8b8db51cd170a13ff0cb20b90c3f1c0d401de23b468a70b3976914bdd4308c` | 117,727 | 722 | exact |
| `RESULT.json` | `391e951f401a409770c84291071fa0c00cc3e48cbe2cb847d9e1a661a038b57c` | 4,119 | 107 | exact |
| `REPORT.md` | `5fba916a5874eebcbfb972e6f22003918cad2d2942f107396204a91a4af511b8` | 13,701 | 250 | exact |

The scheduler’s Round-102 settlement describes a distinct dispatcher replay record (26,076 bytes / 461 LF, abbreviated SHA-256 `ee485e0d...b2e98`) and the pre-launch `rc=127`. I did not treat that scheduler statement as my replay. My fresh replay is separately identified in Section 16.

## 3. Seal, inventory, and physical filesystem reconstruction

I did not accept `check_manifests.py` as the seal proof. A separate streaming walker used `lstat`, rejected every non-regular entry and symlink, normalized every path relative to the package root, streamed SHA-256 in fixed chunks, counted raw bytes, and counted byte `0x0a` directly. It then performed set equality against each manifest rather than accepting a subtotal.

```text
physical := sorted(all descendants for which lstat says regular file)
assert no descendant is a symlink or another non-regular type
for path in physical:
    (digest, bytes, lf) := stream(path)
assert root-manifest rows match their named files exactly
assert payload-manifest rows match the payload domain exactly
assert inventory rows match the substantive domain exactly
assert every recorded (digest, bytes, lf) equals the streamed tuple
assert recomputed manifest bytes hash to the stated manifest identities
```

The result is exact:

| domain | files | bytes | LF |
|---|---:|---:|---:|
| physical package | 725 | 6,449,971,363 | 63,906,508 |
| substantive inventory | 722 | 6,449,683,117 | 63,904,339 |

Every root, payload, and inventory row resolved to the same physical file. There are no symlinks, missing rows, extra rows, path aliases, duplicate paths, stale substitutions, or post-seal byte changes. The three-file difference is exactly the manifest/inventory envelope. Rechecking the bound governance snapshots produced the identities in Section 2.

The five very large gzip members received a separate byte-stream audit described in Section 14. That audit also rules out a manifest-valid but non-round-tripping compressed substitution.

## 4. Independent reconstruction strategy

I wrote fresh standard Python auditors outside the package and did not import the proposer’s check modules for any independent conclusion. The auditors consumed the sealed JSON/JSONL/DIMACS/assignment data as inputs, rebuilt mathematical objects and encodings, and compared results to physical artifacts. Package replay was a later, separate reproducibility test.

The main independent passes were:

1. construct Gross checks, edges, overlaps, stabilizer rows, logical representatives, direct columns, and all translations from the frozen seeds;
2. regenerate each direct formula and check each complete assignment and physical mechanism;
3. normalize block/selector tuples, enumerate every parent-image pair, preserve first provenance, and test generator closure;
4. compile the three outer bases from their semantic sources while comparing every generated clause and assertion-map row;
5. rebuild all three lex suffixes, check all local truth tables, and replay complete outer models;
6. solve and replay a fresh adversarial model of the flawed base;
7. stream-decompress, hash, count, and deterministically recompress every retained compressed SAT/UNKNOWN stream; and
8. independently parse all process/failure/transition records before running the sealed replay.

These public algorithms and the exact counts below are the reproducible audit trail. Temporary implementations and outputs were review scratch and were removed after final identities were recorded.

## 5. Frozen Gross geometry and the complete group action

Let

\[
G=\mathbb Z_{12}\times\mathbb Z_6,\qquad |G|=72,
\]

with a group element encoded as `g = 6 i + j`. The frozen Gross seeds are

\[
A=\{(3,0),(0,1),(0,2)\},\qquad
B=\{(0,3),(1,0),(2,0)\}.
\]

For group addition modulo `(12,6)`, my reconstruction formed

\[
X_g=\{g+a:a\in A\}\cup\{72+g+b:b\in B\},
\]

\[
Z_g=\{g-b:b\in B\}\cup\{72+g-a:a\in A\}.
\]

There are 72 checks per sector, six qubits per check, 144 data qubits, 432 X edges, 432 Z edges, and 864 edges total. Among the `72 x 72 = 5,184` X/Z check pairs, 648 overlap in exactly two qubits and 4,536 are disjoint. No other overlap size occurs. The binary check matrices have

\[
\operatorname{rank}H_X=\operatorname{rank}H_Z=66,
\quad k=144-66-66=12.
\]

I expanded both frozen weight-12 seed files under all translations, removed stabilizer-span members by GF(2) elimination, and recovered exactly 1,884 logical representatives in each sector. Greedy quotient-basis construction produced 12 independent representatives per sector; the cross-pairing matrix has rank 12.

For `delta=(a,b)`, define

\[
\tau_\delta(6i+j)=6((i+a)\bmod 12)+((j+b)\bmod 6).
\]

On the two data sheets, `tau(q)=tau(q)` for `q<72` and `tau(q)=72+tau(q-72)` for `q>=72`. On an edge `(K,c,q)`,

\[
\tau_\delta(K,c,q)=(K,\tau_\delta(c),\tau_\delta(q)).
\]

The schedule action is the left relabeling

\[
(\delta S)(\tau_\delta(e))=S(e).
\]

The independent exhaustive counts are:

| property | cases checked |
|---|---:|
| edge bijections | 72 |
| identity action on edges | 864 |
| edge group composition `tau_d(tau_e(edge)) = tau_(d+e)(edge)` | 4,478,976 |
| check/qubit/incidence geometry | 20,736 |
| overlap transport | 46,656 |
| detector/stabilizer row transport | 10,368 |
| logical-coordinate transformations | 1,728 |
| direct-column equivariance | 51,840 |

The composition count is exactly `72 * 72 * 864`. The direct-column count is `72 translations * 2 sectors * 360 columns`. Translation preserves time bounds, edge uniqueness, same-check and same-data conflicts, the two-qubit overlap/MC relation, global interleaving, and extrema. It is therefore a bijection on legal schedules.

### 5.1 Direct columns and physical effects

For each sector and schedule, I sorted the six data qubits of every sector check by its six gate times. Direct columns comprise 144 data faults `D:q` and three residual faults `R:c:k` for each of 72 checks. The canonical residual positions are

```text
k=0: {0,1}
k=1: {3,4,5}
k=2: {4,5}
```

and the physical residual positions are respectively

```text
k=0: {2,3,4,5}
k=1: {3,4,5}
k=2: {4,5}.
```

Thus each sector has exactly `144 + 72*3 = 360` named columns and 216 distinct residual supports. I rebuilt canonical support, physical support, the 72-bit detector syndrome, downstream opposite-check `u` options, and the 12-bit logical action for every column. For each translation, name mapping is

```text
D:q   -> D:tau(q)
R:c:k -> R:tau(c):k.
```

Support and physical support translate on qubits, syndrome translates on detector rows, and logical action is transformed by an invertible 12-by-12 map. This proves that distinct-name weight, zero syndrome, and nontrivial logical class are preserved. All 144 translated witnesses for each of the exploratory and corrected witness pairs were also evaluated directly on their translated schedules: each sector has orbit size 72, every named weight is 10, every canonical and physical syndrome is zero, and every logical class is nonzero.

## 6. Mandatory iteration 184 and the atomic 328-to-330 transition

### 6.1 Outer formula

I rebuilt the iteration-184 semantic source from its frozen geometry and exact registry, then compiled it with independent deterministic variable allocation and gate clauses. The source and formula identities are:

| object | SHA-256 |
|---|---|
| source file | `5eb1607bebea7bfc44b693a4a3a9ae19f2ab5ae498407290863b34d6eb9b66b0` |
| semantic payload | `d601f297e8b2a1b7d6179d19452da8b0abca2e4f16d7404b6395a8254e949268` |
| selector state | `7296aa70690e01852519b78826b173af35998cec0e9c124c46ea30101dd0777d` |
| state file | `3b128ef192074a3bc0c163502e97eff99ab9d15c546381e98e1e178471552d7b` |
| CNF | `2b0030fd15b0ef8154e2dbc37508e03481f11d8c876c4fe59e6541cb3bfacd62` |

The formula has 19,210 semantic assertions, 415,793 variables, and 1,416,404 clauses. I compared every generated clause in order and every assertion-map row, not only the header or hash. The assertion counts are:

| family | assertions | root clauses |
|---|---:|---:|
| data distinctness | 144 | 2,160 |
| X-ancilla distinctness | 72 | 1,080 |
| Z-ancilla distinctness | 72 | 1,080 |
| MC equivalence | 648 | 1,296 |
| reviewed blocks | 14,484 | 14,484 |
| EFSSC exclusions | 328 | 328 |
| time nonnegative / upper bound | 864 / 864 | 0 / 864 |
| extrema inequality / attained | 1,728 / 4 | 1,728 / 4 |
| global interleaving | 2 | 2 |

The deterministic definitions comprise 225,902 AND, 97,705 OR, 80,343 XOR, 11,234 comparator, and 1,728 word-equality gates; there are 864 rank and 3,162 membership expressions.

The retained assignment has SHA-256 `cda3deebcee015ad123b6811bc016fab728482817825a2bf75b221c4d0cfa381`, assigns every variable exactly once, and satisfies all 1,416,404 clauses. The decoded raw schedule has SHA-256 `6cd28918760dce2d7e3b4c60e77c34a7a4628b86ced39e8917b280beffc21439`; its rank-compressed schedule has SHA-256 `5c13a6ef32fec263f6cdc5d10db1da30d6758a79f089194814fe99e360d55c23`, 123 used layers, and maximum time 122. Direct reconstruction found all 864 required edges exactly once, zero resource conflicts, zero MC violations, global interleaving, no installed block hit, and no installed selector hit.

### 6.2 Direct formula construction and all six accepted point models

For each 360-column sector, the independent encoder allocated selection variables `x[0..359]`, imposed 72 exact syndrome XOR-zero equations, formed 12 logical parity bits and required their disjunction, and used a sequential counter for `sum(x)<=10`. It imposed no candidate pool, residual-shape, contributing-check, fixed-basis, or within-check-order restriction. XOR gates used their full four-clause truth table. Every regenerated DIMACS file was byte-identical to the sealed formula; every assignment had the exact domain and satisfied every clause.

| candidate / sector | formula SHA-256 | vars / clauses | selected names | canonical / physical support weight | logical vector |
|---|---|---:|---|---:|---|
| iteration 184 Xerr | `40bcf7fc4e701d496c03d521324c5b7d88e094b5a350dbfb1f25468e1bea0b63` | 5,935 / 22,320 | `D:129 R:1:0 R:2:0 R:3:2 R:9:1 R:18:2 R:44:2 R:53:2 R:55:0 R:61:0` | 18 / 26 | `100000011111` |
| iteration 184 Zerr | `539289f9eccfd06d9c71e046fd62b2ec7140c09f5250f5761d9d5c55698b1f49` | 5,904 / 22,196 | `D:47 D:90 D:113 D:143 R:3:2 R:13:0 R:17:2 R:37:0 R:38:0 R:45:0` | 12 / 20 | `111110111111` |
| exploratory Xerr | `f6bd062bc61027faea3517888e4217e657b8d944691a514b28ca9540adb7937f` | 5,949 / 22,376 | `D:41 D:84 D:85 D:86 D:107 D:116 D:117 D:133 R:8:2 R:15:0` | 12 / 12 | `111100100000` |
| exploratory Zerr | `e1137a493717fcb05187c88439f3428a930183af111f9d90b8ce6a362427003e` | 5,931 / 22,304 | `D:17 D:49 D:50 D:67 D:107 D:113 D:119 D:122 R:24:2 R:39:0` | 12 / 14 | `110101001011` |
| corrected Xerr | `af4d1bddab1993402cd5b7118e4b9106416e14d06d09a61fb1f7d35ae4b92bb2` | 6,141 / 23,144 | `D:19 D:44 D:53 D:130 D:135 R:1:2 R:23:2 R:48:0 R:56:1 R:63:2` | 16 / 18 | `111001111100` |
| corrected Zerr | `0e44f84f95fdf9adf7c28aba6243b8cafc5056ba2fbb0279896a2b2c2ebc88a3` | 6,146 / 23,164 | `D:40 D:43 D:51 D:106 D:109 D:113 D:117 D:125 R:43:0 R:53:0` | 12 / 16 | `100111000000` |

All rows have exactly ten distinct names, empty canonical syndrome, empty physical syndrome, equal canonical/physical logical vector, and nontrivial canonical and physical action. The assignment file identities, in table order, are:

```text
4e4f46dfe603d55361732857b101b8f451f49584e413753249977e28526ce886
527d4ff72589c3aa21bfda3f8ef3467055ca4664f03204b4d9ab451ddd4f2c5e
232f203d7c72392be549543e32866bba9c931465587fb6f694ed6887f4be24d1
1aac96573ed8fd30a1760c1ec9629c5cc2e55273e5aa6ea5aa39bc056794e65b
bab70c8306258c2651627711ab396b86e38d83a8caeb5d0025d7c3b7b14e120d
dffb76553b8c13812b528b3bbfc9039086b9fa4fddf5e8f6473e0d8b3e06fde9
```

After both iteration-184 sectors had passed clause and physical replay, the transition added exactly selectors `r100-i184-Xerr` and `r100-i184-Zerr`. The independent transition audit establishes `328 -> pending 330 -> committed 330`, bilateral replay before the pending record, state file committed last, and no repair entry. No other selector or state field changed in that atomic transition.

## 7. Exact invariant orbit closure

### 7.1 Identity rules and algorithm

A block identity is the complete sorted tuple of edge-index pairs in its order atoms. A selector identity is

```text
(sector,
 sorted(data_support),
 sorted((check_index, sorted(residual_kinds_for_check))))
```

and its named list is reconstructed from that tuple. SHA-256 is a record label, never an equality oracle. My closure used insertion-ordered first occurrence:

```text
for parent_index, parent in enumerate(parents):
    orbit = empty exact-tuple set
    for delta in all 72 group elements in canonical order:
        key = normalize(translate(parent, delta))
        multiplicity[key] += 1
        orbit.add(key)
        if key unseen globally:
            first[key] = (parent_index, delta, inherited provenance)
for each output row in order:
    assert output tuple == next(first)
    assert output parent/delta/provenance == first tuple
for generator in {(1,0),(0,1)}:
    assert translate(key,generator) belongs to final exact set
```

The inverse-lifting soundness argument is exact. If a translated block or selector were unsound for a schedule in its translated source domain, apply `tau_-delta`. Schedule legality, order atoms, direct names, physical/canonical syndrome, named weight, and logical nontriviality are equivariant, so the inverse image would be a counterexample to the inherited source cut. Translation therefore preserves soundness at the source cut’s exact scope; it does not broaden that scope.

### 7.2 Blocks

The input has 14,484 block records but 14,477 unique normalized semantics; seven records are duplicate extras. All records remain parents because provenance and multiplicity are historical facts.

| quantity | exact value |
|---|---:|
| parent-element images | 1,042,848 |
| unique output semantics | 517,140 |
| collisions | 525,708 |
| parent orbits of size 36 | 90 |
| parent orbits of size 72 | 14,394 |
| output provenance rows replayed | 517,140 |
| two-generator invariance cases | 1,034,280 |

First-contribution family counts are 1,440 unary, 900 round-62, 500,868 generalized, and 13,932 dynamic, summing to 517,140. The complete image-multiplicity histogram is:

| multiplicity | output tuples |
|---:|---:|
| 1 | 300,024 |
| 2 | 113,148 |
| 3 | 55,368 |
| 4 | 24,048 |
| 5 | 10,728 |
| 6 | 4,896 |
| 7 | 3,168 |
| 8 | 1,728 |
| 9 | 504 |
| 10 | 720 |
| 11 | 360 |
| 12 | 144 |
| 13 | 72 |
| 14 | 72 |
| 15 | 144 |
| 16 | 180 |
| 17 | 288 |
| 20 | 72 |
| 22 | 36 |
| 72 | 1,440 |

Both weighted sums check: the row count is 517,140 and the multiplicity-weighted sum is 1,042,848.

### 7.3 Selectors through corrected iteration 186

The initial 330-selector registry closes to 23,724 unique selector semantics. The exploratory pair contributes two free orbits, 144 distinct parents, so the parent registry has 474 rows. Enumerating `474*72=34,128` images yields:

| quantity | exact value |
|---|---:|
| unique selectors | 23,868 |
| collisions | 10,260 |
| Xerr / Zerr split | 12,492 / 11,376 |
| parent orbits of size 36 / 72 | 1 / 473 |
| provenance rows replayed | 23,868 |
| two-generator invariance cases | 47,736 |

The selector multiplicity histogram is `1 -> 23,688`, `2 -> 36`, and `72 -> 144`; its weighted sum is 34,128. Every stored selector has distinct reconstructed names, named weight at most 10, exact semantic hash, first-parent identity, translation delta, and inverse-lift provenance.

The iter186 identities are:

| object | SHA-256 |
|---|---|
| source file | `a381709cb972a0ba693269bd47020dd02e32a3f7685b09d2d052c7d06c39504f` |
| semantic payload | `9129c5794edf809e8caeee788caa04204ad70a220b55859434a367f75ae0694e` |
| state file | `679220d47b2b2d04ccdd57a729008aeb5d983ae943835bd003bffa1134b14991` |
| selector state | `751ee9d6c59656d29dbfe99cd9b33539224eece3dc02c5b9b05142ab3b61ea50` |

### 7.4 Corrected witness addition and iteration 187

The corrected Xerr and Zerr witnesses each have a free orbit of 72. Their 144 translated selector tuples are mutually distinct and disjoint from the 23,868-set: 144 parent-images, 144 fresh semantics, zero collisions. All 144 translated schedules and mechanisms pass legality, distinct-name weight 10, both zero syndromes, and nontrivial logical action. Adding them gives exactly 24,012 selectors, split 12,564 Xerr / 11,448 Zerr, and remains invariant under both generators (48,024 generator cases).

The largest independent closure pass recorded a peak resident count of 7,322,042,368 bytes. Counters used exact Python integers; all image, collision, variable, and clause totals were also checked against signed 64-bit bounds. No hash table key was a digest, so collision safety is semantic. The package compilers stream clauses and never enumerate schedule assignments.

## 8. Scientific retraction and adversarial counter-scenario

Let `B_185` be the first outer base with 330 selectors and the untranslated 14,484 block registry. Its exact CNF has 416,062 variables, 1,417,374 clauses, and SHA-256 `ddd40740b42854b74de7d64e3899f017a58a56223b3fa560d15845a9f7cae6c9`. Let `L` be the conjunction of the 71 translation lex leaders.

I independently launched a fresh CaDiCaL solve of `B_185`, outside the proposer ledger. It returned `rc=10/SAT` in about 3.42 seconds with empty stderr. I parsed exactly 416,062 assignment literals, checked the exact variable domain, and satisfied all 1,417,374 clauses. The decoded legal raw schedule has SHA-256 `50e84c565d1ff4191a3fa48c22f0d4509ec072645540cb791e7acc3c33e8f148`; rank compression gives SHA-256 `1b68d1beb7c2205d7def84e5f1560340523d095be60ae348d27b58523f3df513`, 144 layers.

I then enumerated all 72 translated raw schedules and evaluated every original block and selector directly:

* exactly one translate survives `B_185`, the identity `(0,0)`;
* the orbit’s lexicographically least raw vector occurs at `(1,5)`;
* that least translate has raw schedule SHA-256 `01ced0f703ea1bf21c6c9a07d963f7514eaa85bbfd16ab4373a2635340c51087`;
* it hits 75 installed block cuts and zero selectors; and
* its first hit in registry order is `r69-Xerr-2-8-19`.

Therefore this base orbit contains no member satisfying both the original base and all lex leaders: its only base survivor is not least, and its least member is not a base model. The failed proof step is

\[
B_{185}(S)\Longrightarrow B_{185}(\delta S),
\]

which is false because the registry was not invariant. This is a concrete refutation of the orbit-canonicalization claim. It does not assert that `B_185 ∧ L` is UNSAT; the package’s different exploratory assignment proves it SAT. It establishes that the quotient has no licensed orbit-wise coverage or UNSAT lifting theorem.

I also checked the three package schedules against the old registry over all translations:

| orbit | old-base-surviving translates / 72 | least-translate old cut hits |
|---|---:|---:|
| iteration-184 schedule after its two cuts | 0 | 159 blocks / 0 selectors |
| exploratory schedule | 1 | 0 / 0 |
| corrected schedule | 72 | 0 / 0 |

The exploratory quotient encoding itself is internally exact: its raw quotient SHA-256 is `496ca65f5e9a6b6c24fc1050123f1f0850ecbbfb2219fb09e9606ec7055800d6` (physical compressed-bit artifact SHA-256 `c0af79e4110f54a2388502a201973833c7c470ef15db9cbce302cecc10602871`), with 1,029,502 variables and 6,324,965 clauses. Its complete assignment satisfies all clauses; its decoded schedule has raw SHA-256 `5b4f340bb40e25d84d49db2f19df2a172632b316b7e8e39e97ba3ac910d8915e`, compressed SHA-256 `2c8ce90954f7439947a6988d5a536533a44aeb6c3eda1ff5627a029790c8e958`, 548 layers, orbit size 72, and stabilizer size 1. Those are point facts, not coverage facts.

Positive evidence is uncontaminated for three reasons. First, clause satisfaction and schedule legality do not use invariance. Second, direct mechanisms were independently rebuilt from the frozen schedule and full 360-column dictionaries. Third, the group action itself transports each legal schedule and witness, and selector soundness follows by inverse translation. The corrected base was rebuilt from the closed source and exact-compared clause by clause; it contains no flawed lex suffix.

## 9. Corrected invariant bases and independent outer compilation

The same independent compiler reconstructed the corrected iteration-186 base and fresh iteration-187 base. All DIMACS clauses and assertion-map rows matched byte for byte.

| base | blocks / selectors | assertions | variables | clauses | CNF SHA-256 |
|---|---:|---:|---:|---:|---|
| iteration 184 | 14,484 / 328 | 19,210 | 415,793 | 1,416,404 | `2b0030fd15b0ef8154e2dbc37508e03481f11d8c876c4fe59e6541cb3bfacd62` |
| corrected invariant iteration 186 | 517,140 / 23,868 | 545,406 | 1,834,360 | 6,867,095 | `00a5f305166aded035442f689f2d8bd13d52622a258733e18342cb7ca3608dd9` |
| fresh invariant iteration 187 | 517,140 / 24,012 | 545,550 | 1,838,894 | 6,882,039 | `7f66b46643b6b10cce57358e4e66f7e95cdc1bfe52ee14f77884c56ddd5d5eab` |

For iteration 186, gate totals are 922,035 AND, 232,153 OR, 665,443 XOR, 11,234 comparators, and 1,728 word equalities. For iteration 187 they are 925,080 AND, 232,444 OR, 666,641 XOR, 11,234 comparators, and 1,728 word equalities. Both have 864 rank expressions and 6,048 membership expressions. The 144-selector delta accounts for the exact assertion, gate, variable, and clause changes. The compiler audit peaked at 4,681,433,088 resident bytes; all final identifiers and counts are far below signed 32-bit variable and signed 64-bit clause limits.

## 10. Lex quotient: exact encoding and equisatisfiability theorem

Let `v(S)` contain 8,640 bits: ten time bits for each of 864 frozen edges, with edges in frozen order and each time word ordered most-significant bit through least-significant bit. For each nonidentity `delta`, require

\[
v(S)\leq_{\mathrm{lex}} v(\delta S).
\]

For bits `x_i`, translated bits `y_i`, and suffix result `s=le_{i+1}`, the recurrence is

\[
le_i=(\neg x_i\land y_i)\lor((x_i=y_i)\land s),
\quad le_{8640}=\mathsf{true}.
\]

Its compressed truth table is:

| `x_i` | `y_i` | `le_i` |
|---:|---:|---|
| 0 | 0 | `s` |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 1 | `s` |

For each recurrence variable, eight clauses block the eight of 16 `(x,y,s,out)` valuations with the wrong output. I checked all 16 valuations, not only satisfying rows. Reverse induction from the constant terminal value proves a unique auxiliary extension for every primary schedule assignment.

There are `71*864=61,344` edge-map cases and `71*8,640=613,440` new recurrence variables. The exact suffix is `613,440*8=4,907,520` definition clauses plus 71 root unit clauses, totaling 4,907,591. Each base is an exact physical prefix of its quotient.

| quotient | base vars / clauses | final vars / clauses | quotient SHA-256 |
|---|---:|---:|---|
| retracted iteration 185 | 416,062 / 1,417,374 | 1,029,502 / 6,324,965 | raw `496ca65f5e9a6b6c24fc1050123f1f0850ecbbfb2219fb09e9606ec7055800d6`; compressed-bit file `c0af79e4110f54a2388502a201973833c7c470ef15db9cbce302cecc10602871` |
| corrected iteration 186 | 1,834,360 / 6,867,095 | 2,447,800 / 11,774,686 | `f6dec16c6ee19ee1a041d3eb78786171558f54805c3038ce9c311c62b82d7c13` |
| fresh iteration 187 | 1,838,894 / 6,882,039 | 2,452,334 / 11,789,630 | `e415b4c2c5b4923a47348a06ea9ebb06bbc85cea2c9c32bd3a9b25a1ce198234` |

For a full invariant base `F`, let the finite group act on its models. Every orbit of schedule vectors has a unique least vector. Invariance supplies a model at that vector; all 71 leaders hold; and the recurrence has one extension. Conversely, quotient projection is a base model because the base is a prefix. Hence

\[
F\text{ SAT}\iff F\land L\text{ SAT}.
\]

If a schedule has stabilizer `H`, several group elements may attain the minimum, but they produce the same vector. Thus the quotient selects one schedule vector per orbit, not necessarily one group element. This proof applies to iterations 186 and 187. It does **not** apply to the incomplete iteration-185 base, as Section 8 demonstrates.

## 11. Corrected quotient SAT model and direct retries

The corrected quotient assignment has SHA-256 `6571dbf1329722c1f052487ed070d200ff8826e200ea38eba330ca4cbb66030b`. It assigns all 2,447,800 variables and satisfies all 11,774,686 clauses. I separately checked all 8,640 primary time bits, all 613,440 recurrence values, and all 71 roots. The schedule is lexicographically least in a 72-vector orbit with stabilizer `{(0,0)}`. Its raw and compressed hashes are respectively

```text
2f6baa78a695e810929454e0f2375e740b25af5b75ebb527975eb28f4c878e62
f6a806a1b90535d497da63b154960f9ebf172c6c740356470cdeda56866bd5cf
```

It uses 483 layers, has all 864 edges, zero conflicts, zero MC violations, global interleaving, and no invariant block or selector hit. Corrupt assignment, truncated assignment, reversed comparator direction, and missing-root controls all fail as expected.

The default proof-mode direct queries reached their internal bound and returned `rc=0/UNKNOWN`:

| sector | unchanged CNF | UNKNOWN elapsed | retry elapsed / result |
|---|---|---:|---:|
| Xerr | `af4d1bddab1993402cd5b7118e4b9106416e14d06d09a61fb1f7d35ae4b92bb2` | 890.049392 s | 1,353.690736 s / `rc=10 SAT` |
| Zerr | `0e44f84f95fdf9adf7c28aba6243b8cafc5056ba2fbb0279896a2b2c2ebc88a3` | 890.056241 s | 53.452524 s / `rc=10 SAT` |

The UNKNOWN files contain incomplete derived/deleted-clause prefixes and no empty clause. They are non-certificates and establish no absence. The retry changed CaDiCaL heuristics/profile and binary-proof setting only; both attempts used the identical physical CNF path and hash. The eventual complete assignments are the corrected rows in Section 6.2 and satisfy every clause. Both physical replays pass. Because both sectors are SAT, repair remained forbidden. Only after both had been adjudicated were their two 72-element selector orbits staged; the fresh state was committed last without repair or partial installation.

## 12. Fresh, invariant, genuinely unstarted iteration 187

The iteration-187 state is not a renamed solver disposition. The source and state contain `started: false` and `stop: null`; the process ledger has zero iteration-187 solver processes; and no solver log, assignment, proof, model, stop reason, or disposition artifact exists in the iteration-187 base or quotient directories. Formula compilation and independent encoding checks are preparation, not a solve.

| item | exact value |
|---|---|
| blocks / selectors | 517,140 / 24,012 |
| source file SHA-256 | `d7a1f6bf63b328627362a70518f5beb77d3b4b32241ccaaab83d6d5d5c122124` |
| semantic payload SHA-256 | `88c726321144b782ce7fb72d8b1ed0d361473ab6587bb7f3ba8ec6cd0079dfa3` |
| state file SHA-256 | `b7fa430f67bdcb8fdb034c8e42174ee219d0d77ecdbe57f99576de1518de9bea` |
| selector-state SHA-256 | `7667fc8230b67224b1895180764680c5000dcef34b3c67352f904e5998e8879b` |
| base | 545,550 assertions; 1,838,894 variables; 6,882,039 clauses; `7f66b46643b6b10cce57358e4e66f7e95cdc1bfe52ee14f77884c56ddd5d5eab` |
| quotient | 2,452,334 variables; 11,789,630 clauses; `e415b4c2c5b4923a47348a06ea9ebb06bbc85cea2c9c32bd3a9b25a1ce198234` |

No solver disposition is inherited from iteration 186. The next valid action is to solve this quotient with proof output enabled from launch, then follow the bilateral SAT/direct or proof-checked UNSAT rules stated in Section 17.

## 13. Failures F001--F013 and accepted-evidence separation

I matched all thirteen ledger items to physical process records and outputs. Failed attempts are historical controls, never positive evidence.

| ID | independently confirmed failure | accepted correction / evidence ruling |
|---|---|---|
| F001 | iteration-184 replay under base Python could not import `z3`, rc 1 | bound vendored interpreter replay rc 0 |
| F002 | malformed shell quoting produced `SyntaxError`, rc 1 | corrected quoting bound Z3 5.1.0 and smoke test passed |
| F003 | asserted all 14,484 block records were semantically unique | corrected full-tuple accounting finds 14,477 semantics and seven duplicate extras |
| F004 | quotient checker lacked package `PYTHONPATH`, rc 1 | bound invocation rc 0 |
| F005 | control passed compressed quotient bits where raw bits were required | corrected raw path and all positive/negative controls passed |
| F006 | deleting the final DRAT line left a complete proof and returned rc 0, so it was not a valid truncation | half-byte DRAT truncation rc 1; corrupt DRAT, corrupt LRAT, and truncated LRAT rc 1; valid DRAT/LRAT rc 0 |
| F007 | lex leaders were appended to a non-invariant registry | global claim retracted; concrete fresh counter-scenario in Section 8; full closure and new quotient |
| F008 | builder coerced historical `source_iteration: "pre-124"` to integer, rc 1 | provenance tag preserved verbatim; corrected closure passed |
| F009 | Xerr bounded run returned UNKNOWN with 6,101,477,668-byte prefix | unchanged-CNF retry SAT; prefix retained as non-certificate |
| F010 | Zerr bounded run returned UNKNOWN with 6,379,134,538-byte prefix | unchanged-CNF retry SAT; prefix retained as non-certificate |
| F011 | iteration-187 source schema lacked required `-finite-source-v1` suffix | corrected source compiled and exact-checked; still unstarted |
| F012 | replay proof control asked for nonexistent `php6_5.fresh.drat` | corrected to retained proof filename and reran all children from the beginning |
| F013 | cleanup correctly found an empty package-local `scratch/` directory | directory removed by a recorded child; corrected cleanup passed |

The F006 ruling is especially important: a negative control must destroy proof completeness, not merely alter the container. The valid fixture establishes only the DRAT-to-LRAT tool chain. No Gross query returned UNSAT, so no Gross absence certificate exists.

The finite-source suffix and proof filename corrections change interface/schema references, not scientific formulas. The historical `pre-124` correction prevents provenance loss. The raw-versus-compressed correction prevents comparing different representations. None of F001--F006, F008, F011--F013 supplies scientific evidence; F009/F010 are explicitly incomplete non-certificates; F007 removes evidence rather than adding it.

## 14. Deterministic compressed-stream audit

For each gzip member I streamed decompression, computed the raw SHA-256/byte/LF/empty-clause counts, then independently recompressed the raw bytes with gzip level 9, `mtime=0`, and an empty stored filename. The recompressed member was byte-identical to the sealed member. This checks decompression completeness, raw identity, metadata determinism, and round trip for all five streams.

| stream | disposition | raw SHA-256 | raw bytes / LF | gzip SHA-256 | gzip bytes |
|---|---|---|---:|---|---:|
| corrected outer | SAT-side output, not UNSAT proof | `767b8ffae943d78de8313581648ab91e42249a9bac4eb268b852b06f5edee2bb` | 4,040,043,400 / 46,706,741 | `43e72fbf6ee8021d7808f414b71937365243fae4e2a90f9b7db0a9fb82339788` | 562,533,276 |
| Xerr default | UNKNOWN incomplete prefix | `a4c50c63e01fe6bbed082749561a3606de18c306db1f4c1cfcb6f4ef474e8c45` | 6,101,477,668 / 21,263,055 | `a55e33c50b49d7c6bc013f4a0ea4cc27556f2be0e6d1d6c35cf4e220b4f0d5fe` | 1,306,002,160 |
| Zerr default | UNKNOWN incomplete prefix | `3fceb8415b9c68437d3239d77bbc19262a070e904182556d1122ebff576c32fa` | 6,379,134,538 / 23,410,479 | `8bb3ea8978d18afe6eb5b0c57b7ffd9e29f3edaa20b3e4f6b89a18b39fbe7f08` | 1,266,246,198 |
| Xerr retry | SAT-side output, not UNSAT proof | `02e37d5517b2f5addeeb9e6999cd2475f5be89e96ffd0266fd6bbb0c3028947e` | 3,862,573,115 / 26,088,755 | `b7bbe9b082528b23477d70db20737a06582e9b7ff77da8e8642b22887ced4626` | 1,131,390,338 |
| Zerr retry | SAT-side output, not UNSAT proof | `9e012699c4e406733e0d6f6473590ef7f1a1f29dfac19047c98af2690d5ac949` | 274,032,152 / 2,139,634 | `292bb39d30922ad0158392870986ab0413711b8f106727e2fe71393d205f26ee` | 82,313,061 |

Totals are 20,657,260,873 raw bytes, 119,608,664 raw LF, and 4,348,485,033 gzip bytes. Every raw stream has zero empty-clause line. The two UNKNOWN prefixes remain incomplete even though they are large; size and deterministic preservation do not turn a prefix into a certificate.

## 15. Processes, transitions, proof controls, and repository gates

The retained ledger has 106 wrapper records: return-code distribution `0:82`, `1:13`, `10:9`, `20:2`. There are 105 PID-bearing records plus the disclosed bootstrap composite; two synchronous bootstrap child descriptions have `child_pid:null`. Every PID-bearing child is reaped, detached count is zero, wrapper-timeout count is zero, and record-to-file matching is 106/106.

The eleven science solver intervals, in ledger order, are:

```text
outer_iter184_cadical_proof
direct_iter184_Xerr_cadical_proof
direct_iter184_Zerr_cadical_proof
translation_quotient_iter185_cadical_proof
quotient_iter185_direct_Xerr_cadical_proof
quotient_iter185_direct_Zerr_cadical_proof
solve_iter186_full_invariant_quotient_cadical_proof
iter186_full_invariant_quotient_direct_Xerr_cadical_proof
iter186_full_invariant_quotient_direct_Zerr_cadical_proof
iter186_full_invariant_quotient_direct_Xerr_cadical_unsat_profile
iter186_full_invariant_quotient_direct_Zerr_cadical_unsat_profile
```

Their closed intervals are strictly nonoverlapping; the minimum adjacent gap is 6.176575422286987 seconds. No solver survived. Iteration 187 has zero solver records. Final package cleanup reports no package/system temporary survivor and no raw corrected large-stream survivor.

Proof controls accept the valid pigeonhole DRAT, convert it to LRAT, and accept LRAT (`rc=0,0`). Corrupt DRAT, corrected half-byte-truncated DRAT, corrupt LRAT, and truncated LRAT are rejected (`rc=1`). The earlier final-line deletion’s `rc=0` is retained as F006, not misreported as rejection. These controls establish the tool path only.

The package’s final repository wrapper has 11 strict-serial checks. Ten ordinary gates return zero. Evidence closure returns its expected proposer-stage rc 1 with 688 unique unlinked-path diagnostics, all under this single sealed package. This is expected because the proposer was forbidden to edit canonical state. It is not evidence closure after installation. The proposed replacement in Section 18 links both the package and this completed review; I validate that replacement separately in Section 18.

## 16. Fresh sealed replay and interface ruling

### 16.1 Entry-point defect and governance overlay

The package root lacks `replay.sh`. A conventional dispatcher invocation therefore failed before launch with `rc=127`; no package science process ran. This is a real interface defect, not a scientific failure and not evidence against the package result.

The required source entry is sealed at `source/replay_round102.py`. A first direct invocation from the current repository correctly stopped at its first `live_governance` child because the live scheduler hash is the later review-authorization identity rather than the pre-proposer identity. That behavior proves the governance guard is active. It is not a failed replay of the historical package.

For the historical replay, I made a disposable repository overlay. All 725 package files were hardlinked from the sealed package and checked byte-identical. Only the twelve governance inputs named by `bindings/LIVE_GOVERNANCE.json` were restored from the package’s bound originals. No science/source/result file was changed. The exact command was:

```text
/private/tmp/circdist-r72-dispatcher-venv/bin/python \
  source/replay_round102.py \
  --root <disposable-overlay>/circdist/artifacts/circdist_gross_global_closure_round102_20260901 \
  --output /private/tmp/round103_sealed_replay_record.json
```

The interpreter SHA-256 is `bdea59019a38eb6600cc9e71e984a97fedadc406448431281e7657030f54987e`.

### 16.2 Result

My replay record has SHA-256 `21eb862683d6297cd224ed7988d6a48fd0db6c438648ecb5bfc46f1e7b421fd9`, 26,055 bytes / 461 LF. Top-level stdout is one PASS JSON line, SHA-256 `69d58db56517eed9d271c1a5ac2cbe253721798ec44f29ac4d9727059b8e4b99`, 64 bytes / 1 LF. Top-level stderr is empty, SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

All 13 children returned rc 0, were reaped, ran strictly serially, had empty captured stderr, and were neither detached nor timed out:

```text
live_governance
full_translation_closure
fresh_iter187_orbit_frontier
fresh_iter187_encoding
corrected_translation_quotient
fresh_iter187_translation_quotient
corrected_sat_orbit_controls
corrected_assignment
corrected_outer_sat_replay
iteration184_direct_physical_replay
exploratory_quotient_direct_physical_replay
corrected_quotient_direct_physical_replay
proof_controls
```

The replay reports exactly 13/13 PASS, all children reaped, detached count zero. I inspected every child record and stderr field rather than accepting only the final line. The overlay and replay scratch record were removed after identities were incorporated into this review.

### 16.3 Interface decision

Absent root `replay.sh` is a packaging/interface defect because it violates the dispatcher’s conventional invocation and produced an observable `rc=127`. It does **not** block proposer-level linking here because:

1. the sealed source entry is explicit and immutable;
2. the dispatch authorization names that entry specifically;
3. the bound interpreter and full command are known;
4. a fresh historical-governance replay passes all 13 children with full process closure; and
5. the proof-DAG schema and evidence semantics do not require the literal filename `replay.sh`.

No wrapper was fabricated inside the sealed package. The proposed frontier records the explicit invocation and defect.

## 17. Root accounting, limitations, and exact residual

The new theorem is a finite symmetry theorem over the exact frozen Gross scheduling model and exact installed cuts. It proves action equivariance, registry invariance after closure, and a correct canonical quotient. It does not prove that the installed exclusions are complete for every possible low-weight direct mechanism unless each underlying cut theorem supplies that scope. The inherited fixed-basis span and mixed-sector results retain the Round-101 limits: fixed bases, fixed schedules, installed-mask quotient, and fixed direct domains do not become global through translation.

The corrected quotient is SAT, and both complete unrestricted direct sectors are SAT. Therefore there is no quotient UNSAT theorem to lift, no direct absence, no repair entry, no schedule with certified circuit distance 12, and no universal distance-11 ceiling. The fresh frontier is iteration 187.

The exact next action is:

1. solve the sealed iteration-187 quotient with proof output enabled from launch;
2. for SAT, retain and check the complete assignment and legal schedule, rebuild both full 360-column direct sectors, treat UNKNOWN as no disposition, and add only bilateral, physically replayed, source-schedule-valid selector orbits atomically;
3. for UNSAT, retain complete DRAT, independently accept it, generate and independently accept LRAT, run valid/corrupt/truncated controls, and state only the exact theorem induced by the sound invariant installed exclusions; and
4. enter repair only after both direct sectors are independently proved absent.

Even an iteration-187 quotient UNSAT result is not automatically the requested root theorem without the exact reviewed link from all installed exclusions to the complete frozen direct-mechanism domain. The root and route stay CONJECTURED, with `D*_Gross in {11,12}`.

## 18. Canonical-installation license and complete replacement

The verdict licenses proposer-level canonical installation. The block below is one complete byte-for-byte replacement for `circdist/proof-dag/nodes/CIRCDIST.gross.yaml`. It preserves the prior claim, both routes and all route fields, both CONJECTURED levels, every prior evidence item, the non-Gross frontier task, and all 21 prior events. It adds only the reviewed Round-102 run/review evidence, explicit retraction and positive-evidence scope, all F001--F013 and interface limitations, the exact fresh iteration-187 residual, and one append-only Round-103 review event. It contains no ellipses or patch notation.

The intended replacement identity is reported immediately after the block and in the final handoff. Validation extracts the bytes strictly between the fences, compares them byte-for-byte to the intended replacement, loads them with the duplicate-key loader, compares every prior route and event structurally to the current canonical node, and runs the proof-DAG/schema, duplicate-YAML, evidence-closure, and whitespace gates on a disposable overlay. The live canonical node is not edited.

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
    is licensed; CIRCDIST.gross and gap-via-lift remain CONJECTURED with D*_Gross in {11,12}.'
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
    task: 'Continue only from the independently reviewed sealed fresh/unstarted iteration 187 full-invariant state. The exact
      translation-closed registry contains 517,140 unique sound block semantics (1,440 unary, 900 round-62, 500,868 generalized,
      and 13,932 dynamic) and 24,012 invariant exact EFSSC selectors (12,564 Xerr and 11,448 Zerr). Bind source-file sha256:d7a1f6bf63b328627362a70518f5beb77d3b4b32241ccaaab83d6d5d5c122124,
      semantic-source sha256:88c726321144b782ce7fb72d8b1ed0d361473ab6587bb7f3ba8ec6cd0079dfa3, state-file sha256:b7fa430f67bdcb8fdb034c8e42174ee219d0d77ecdbe57f99576de1518de9bea,
      and selector-state sha256:7667fc8230b67224b1895180764680c5000dcef34b3c67352f904e5998e8879b before use. Its deterministic
      base formula has 545,550 source assertions, 1,838,894 variables, 6,882,039 clauses and CNF sha256:7f66b46643b6b10cce57358e4e66f7e95cdc1bfe52ee14f77884c56ddd5d5eab.
      The 71-root lex quotient adds exactly 613,440 unique-definition variables and 4,907,591 clauses, yielding 2,452,334
      variables, 11,789,630 clauses and CNF sha256:e415b4c2c5b4923a47348a06ea9ebb06bbc85cea2c9c32bd3a9b25a1ce198234. It is
      equisatisfiable with this full invariant base only; it has not been launched, and no solver/model/DRAT/LRAT disposition
      is inherited. Do not use or globalize the retracted first 330-selector quotient: the non-translation-closed registry
      admits a legal base model whose lex-minimal translate hits 75 untranslated installed cuts. Its SAT schedule, its complete
      Xerr/Zerr direct mechanisms, and their separately physically replayed 144 translations remain positive source-schedule-valid
      selector evidence only. The corrected iteration-186 quotient is SAT and both corrected complete unrestricted direct-360
      queries are SAT; their source-schedule-valid 144-selector orbit is the final atomic addition already represented in
      iteration 187, and repair was not entered. Solve the iteration-187 quotient with proof output enabled from launch. For
      SAT, retain the complete assignment, verify every DIMACS clause and frozen legal schedule condition, rebuild both complete
      unrestricted 360-column sectors, and add only independently physically replayed source-schedule-valid selector orbits
      after bilateral adjudication. UNKNOWN prefixes are incomplete non-certificates and change no state. For UNSAT, retain
      a complete DRAT proof, independently accept it, generate LRAT, independently accept LRAT, and state only the exact theorem
      supplied by the invariant installed exclusions; valid/corrupt/truncated controls remain mandatory. Enter repair only
      after both direct sectors have independently checked absence. Preserve the frozen S_Gross geometry, strict solver serialization,
      MC0, terminal residual semantics, both CSS sectors, full 72-element action, exact tuple identity rather than hash identity,
      integer/memory-safe streaming, atomic state-last transitions, and every earlier exclusion against morphing, Circ-Preserve
      substitutions, alternate conflict models, exploratory pair clauses, retroactive or schedule-globalized cuts, stale compressor
      provenance, mixed-sector XOR, support-weight substitution, and fixed-basis/full-span globalization. Invoke the package
      replay through the bound interpreter and source/replay_round102.py because the sealed root lacks conventional replay.sh;
      record that interface defect rather than inventing an entry point. Keep CIRCDIST.gross and gap-via-lift CONJECTURED
      and D*_Gross in {11,12}; this reviewed continuation supplies no Gross UNSAT, absence, exhaustion, distance-12 witness,
      universal distance-11 ceiling, D* narrowing, route promotion, or root promotion.'
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
```
<!-- END COMPLETE CIRCDIST.gross.yaml REPLACEMENT -->

The complete replacement above is SHA-256
`dd367bf93e59e10588a824d4f530a0b07c3707d43886004bb3ddb754f0ff7d91`, 99,195 bytes / 1,080 LF.
Exact fence extraction is byte-identical to that replacement. On a disposable canonical overlay it produced zero schema
errors, zero warnings, zero preservation errors, and preserved the claim, both routes, all 21 old events, `task-003`, and
both CONJECTURED levels exactly. Eight strict-serial overlay gates returned rc 0: proof-DAG `circdist`, proof-DAG `all`,
circdist migration, release contracts, DAG contracts, Lean DAG self-test, duplicate-YAML scan, and circdist evidence
closure. The duplicate-key loader and scanner found no duplicate key; evidence closure found 170 structured paths and zero
unlinked evidence after the package and this review were linked. `git diff --check` on the sole review edit also passed.
The disposable validation overlay, replay overlay, replay record, audit scripts/results, decompression material, probe files,
and all other Round-103 scratch were removed after final measurement; the final task process sweep found no survivor.
