CONTINUATION-ADVANCED-NOT-PROVED

# CIRCDIST.gross Round 86: exact fixed-selector semantic cuts

## Verdict and canonical consequence

Round 86 does **not** decide the frozen root residual. It constructs, proves sound, independently replays, and installs in a sealed continuation state a new exact no-good mechanism called an **exact fixed-selector semantic cut** (EFSSC). Seven new legal, measurement-correct, globally interleaved schedules were generated from the independently reviewed iteration-102 frontier. Every schedule has an unrestricted direct-360 effective fault of weight 10 in **both** CSS sectors. Therefore none is a distance-12 witness. The final EFSSC formula was deliberately not solved after the seventh transition, so there is no exhaustive ceiling certificate.

The mathematical disposition is unchanged:

- inherited certified candidate: distance 11;
- inherited universal upper bound: 12;
- remaining exact residual: `D* in {11,12}`;
- root status: `CONJECTURED`;
- canonical edits by this proposer: **none**.

A later independent reviewer must assess this package before any canonical frontier link is added. No level change is proposed.

## Authorization, scope, and exclusions

The Round-86 scheduler authorization and the frozen `CIRCDIST.gross` node were read before any scientific action. This package stays inside the frozen class `S_Gross`: the 144-qubit Gross CSS code, its 72 X and 72 Z weight-6 checks, the fixed 864 named data-ancilla CNOT edges, one occurrence of every edge, strict serialization at every data and ancilla endpoint, the frozen measurement-correctness predicate, positive static-distance premise, terminal-residual convention, and both CSS sectors. It does not use a morphing circuit, a different conflict graph, or Circ-Preserve as a substitute.

No network was used. The scheduler, node YAML, proof-DAG generated files, prior packages, and prior reviews were read only. `verification/CANONICAL_READ_ONLY_INVENTORY.json` inventories 23 canonical/protocol files and confirms the four predeclared protected hashes are unchanged.

## Exact input binding

The complete machine-readable binding is `INPUT_BINDINGS.json`. The load-bearing reviewed Round80 package is `circdist/artifacts/circdist_gross_whole_registry_round80_20260830`:

| Object | Exact value |
|---|---:|
| Physical files | 1,221 |
| Physical bytes | 303,862,955 |
| Root manifest SHA-256 | `e086a828391361620eabfbd31b544606f7817826af546fb8779a500f95ec0426` |
| Payload manifest SHA-256 | `8f71dc39916cdab9d57ff2add15e5130631600b2789d7da0bd5626afdfdc202d` |
| Root manifest rows verified | 1,220 / 1,220 |
| Payload manifest rows verified | 1,219 / 1,219 |
| Round81 review SHA-256 | `e0d6ad5b54768195516239f4d0a262135025a630ecd6292d91cb694baa51597e` |
| Scheduler SHA-256 | `8834d2077f89f334b5cd9ec9d36e2223a02c7af6a530e23eddfdabc0b48ba2af` |
| Frozen node SHA-256 | `a8ab9d9c5b98840d90dbd76f2edf8943ad4e6c1fba2e037456c675f425dfa2d0` |

The reviewed restart was independently decoded from the vendored gzip inputs and hashed as canonical JSON:

| State component | Count | Semantic SHA-256 |
|---|---:|---|
| Generalized terms | 12,820 | `4547a39d560358ce24c1615f5db99f17735c717a2b10d67ad2cfac515731acf3` |
| Dynamic blocks | 204 | `62cabe5f2925fc0caadd340848ea439219c13dc3d397c67762f852d36b6560e2` |
| Raw mechanisms | 120 | `fff897136200a97d12ae1756ca07a8aadd10e80cf11e4cce8e7ba30f8e428600` |
| Registry mechanisms | 120 | `b9816477e347ed095e26fd4a521be8a951e92e1b3aa66c668cd2fa315d652604` |
| Installed reviewed block predicates | 14,484 | derived as 1,440 + 20 + 12,820 + 204 |

`cegar/iter102` was absent, so iteration 102 was unstarted before scratch work. The prior sealed directory was never mutated.

## New mechanism: EFSSC

### Definitions

Fix a direct-360 selected fault set `s` in one sector. Its named columns consist of data singletons `D:q` and residual columns `R:c:k`. For check `c`, let `K_c` be the multiset of selected residual kinds. The canonical residual position sets are

- `P_0 = {0,1}`,
- `P_1 = {3,4,5}`,
- `P_2 = {4,5}`.

All positions are zero based in the earliest-to-latest within-check order. Because supports add over GF(2), the positions retained by all residual columns on check `c` are their symmetric difference

`Q_c = symmetric_difference_{k in K_c} P_k`.

For qubit `q` in check `c`, define its exact symbolic rank

`rank_c(q) = sum_{r in check(c), r != q} [t(c,r) < t(c,q)]`.

Strict serialization makes the six times distinct. Hence `rank_c(q)` is exactly the position of `q` in the within-check order, with no tie case. Define

`m_cq = OR_{p in Q_c} (rank_c(q) = p)`.

Let `sigma(q)` be the 84-bit signature of qubit `q`: first its 72 detector parities, then its 12 parities against the fixed logical-dual basis. Let `sigma_D` be the XOR signature of the selected data singletons. For bit `i`, the selected fixed mechanism has symbolic signature

`b_i(t) = sigma_D[i] XOR XOR_{c,q: sigma(q)[i]=1} m_cq(t)`.

Its exact validity predicate is

`V_s(t) = (AND_{i=0}^{71} NOT b_i(t)) AND (OR_{i=72}^{83} b_i(t))`.

The EFSSC installed in the outer solver is `NOT V_s(t)`.

### Soundness lemma

**Lemma.** For every legal frozen schedule `t`, `V_s(t)` is true if and only if the fixed named direct-360 selection `s` has zero detector syndrome and nonzero logical class on `t`.

**Proof.** Strict serialization makes `rank_c` a bijection from the six qubits to positions 0 through 5. Thus `m_cq` is true exactly for qubits in the symmetric-difference residual support `Q_c`. XOR linearity makes the aggregate selected support equal the data-singleton mask XOR all such qubit masks. The 84 signature coordinates are linear parity functionals, so each `b_i` is exactly the corresponding parity of that support. The first conjunction is therefore equivalent to zero syndrome, and the final disjunction is equivalent to at least one nonzero logical-dual parity. The frozen logical-dual basis has rank 12 modulo stabilizers, checked by the vendored model. Hence the latter is equivalent to a nontrivial logical class. This proves both directions. QED.

For residual kind 0, the direct-360 canonical representative uses positions `{0,1}` while the physical elementary suffix uses `{2,3,4,5}`. Their XOR is the full weight-6 check stabilizer. Kinds 1 and 2 use the physical suffix directly. Therefore replacing every canonical residual by its physical elementary support changes the aggregate only by stabilizer rows. Detector syndromes and logical parities are identical. The independent state replay verifies this equality for all fourteen new mechanisms.

### Why this differs from the reviewed library

The reviewed generalized blocks are conjunction/product regions: a sufficient set of strict precedence atoms preserves a concrete fault. EFSSC retains the full Boolean rank/parity relation for one fixed selector. It can represent a union of many disconnected within-check order regions, including cross-check cancellations, without forcing a single precedence cube.

For every new selector, the exact analyzer enumerates all `6! = 720` orders on each participating check. It maps each order to its exact 84-bit local signature. A meet-in-the-middle integer proof splits the checks into two groups. For every left signature, zero syndrome fixes the required right 72-bit syndrome bucket; from that bucket the proof subtracts exactly the one 12-bit right logical signature that would make the final logical component zero. No sampling or floating arithmetic is used.

The old source atom cube is checked separately by restricting each local order list before the same join. All fourteen cubes have zero invalid tuples, proving cube containment. Nine EFSSCs strictly contain their corresponding cube; five equal it on their participating-check order product.

| Selector | Sector | Checks | Full local-order product | EFSSC-valid tuples | Source-cube tuples | Factor |
|---|---:|---:|---:|---:|---:|---:|
| `iter102-Xerr` | X | 3 | 373,248,000 | 165,888 | 82,944 | 2 |
| `iter102-Zerr` | Z | 2 | 518,400 | 2,304 | 2,304 | 1 |
| `r86-i103-Xerr` | X | 2 | 518,400 | 2,304 | 2,304 | 1 |
| `r86-i103-Zerr` | Z | 2 | 518,400 | 2,304 | 2,304 | 1 |
| `r86-i104-Xerr` | X | 4 | 268,738,560,000 | 5,308,416 | 5,308,416 | 1 |
| `r86-i104-Zerr` | Z | 3 | 373,248,000 | 165,888 | 82,944 | 2 |
| `r86-i105-Xerr` | X | 5 | 193,491,763,200,000 | 764,411,904 | 5,308,416 | 144 |
| `r86-i105-Zerr` | Z | 5 | 193,491,763,200,000 | 382,205,952 | 191,102,976 | 2 |
| `r86-i106-Xerr` | X | 9 | 51,998,697,814,228,992,000,000,000 | 25,678,369,290,977,280 | 80,244,904,034,304 | 320 |
| `r86-i106-Zerr` | Z | 4 | 268,738,560,000 | 5,308,416 | 5,308,416 | 1 |
| `r86-i107-Xerr` | X | 8 | 72,220,413,630,873,600,000,000 | 285,315,214,344,192 | 8,916,100,448,256 | 32 |
| `r86-i107-Zerr` | Z | 7 | 100,306,130,042,880,000,000 | 4,953,389,137,920 | 61,917,364,224 | 80 |
| `r86-i108-Xerr` | X | 5 | 193,491,763,200,000 | 637,009,920 | 10,616,832 | 60 |
| `r86-i108-Zerr` | Z | 7 | 100,306,130,042,880,000,000 | 880,602,513,408 | 440,301,256,704 | 2 |

The sum across selector domains is 25,969,520,291,556,096 valid tuples versus 89,663,440,921,344 source-cube tuples. These sums are per-selector multiplicities, **not** a union cardinality; no disjointness is asserted.

Each iteration source schedule falsifies all 14,484 reviewed antecedents and every EFSSC installed before that iteration, while both newly selected mechanisms are valid there. Thus each pair adds a certified schedule point outside the previous cumulative library. Because both members of a pair hold on the same source schedule, this statement does not claim that the second member necessarily adds another point after the first is installed.

## Strict-serial experiment

### Seed iteration 102

The compiler placed all 120 reviewed raw selectors into exact EFSSC form and solved the resulting legal outer formula.

- compile: 18.162 s;
- solve: 196.557 s, `SAT`;
- total external wall: 215.22 s;
- maximum RSS: 700,907,520 bytes;
- 846 rank expressions, 2,154 membership expressions, 19,002 assertions;
- formula SHA-256: `4f11fc7312338d548bb4677a43a226498123495dd69e0a02cb37be067890a29d`;
- schedule SHA-256: `e52aa6f1aceb1fde6d39e06f124b738dd574eb83e0066d498e6788593d414ed2`;
- schedule audit: 864 edges, zero conflicts, zero MC violations, global interleaving, 344 compressed layers;
- reviewed block hits: 0 / 14,484;
- reviewed fixed-selector survivors: 0 / 120.

Complete unrestricted direct-360 CNFs were then generated. They impose no pool, residual-pattern, check-count, or within-check-family restriction.

| Sector | Vars | Clauses | DIMACS SHA-256 | CaDiCaL result | Exact selected weight |
|---|---:|---:|---|---|---:|
| Xerr | 5,966 | 22,444 | `ff345e6e7cb8679f6d9f54936f07e9de2e17a8bb18e15ac3539060540680401c` | SAT, exit 10, 23.41 s | 10 |
| Zerr | 5,927 | 22,288 | `f76a9cd441902f8f3af95fc5e61210121eae9ee976bc7b8e0672665a06b35553` | SAT, exit 10, 2.35 s | 10 |

The package contains each DIMACS file, variable/column dictionary, clause ledger, full assignment log, and a checker that verifies every clause and then replays canonical and physical mechanisms.

### Iterations 103 through 108

The transition was atomic: solve an outer formula; check schedule legality, MC, global interleaving, old-block avoidance, and all prior EFSSC avoidance; run unrestricted direct-360 in both sectors; replay both positive mechanisms; compile and source-evaluate both new exact domains; only then install the pair and write the next unstarted state. Any non-SAT direct result would have stopped with no absence inference. All twelve incremental direct queries returned SAT.

| Iteration | Outer status/time | Schedule SHA-256 | Prior survivors | X/Z source-cube atoms | Direct result |
|---:|---|---|---:|---:|---|
| 103 | SAT / 235.316 s | `57c38511202175a99afc77c28275c101f0c16ff22cb47b7f67bc3c26384d720c` | 0 | 16 / 16 | both SAT, weight 10 |
| 104 | SAT / 102.983 s | `2fb5bff2497e52a64f2b75b291b33d2637863511afaa6863522110818733a7ec` | 0 | 32 / 25 | both SAT, weight 10 |
| 105 | SAT / 32.317 s | `d1985dae0ad8fb4c31cf742a936712ccbc88e65930a5f371cb5e53ec8a07dffa` | 0 | 49 / 41 | both SAT, weight 10 |
| 106 | SAT / 69.163 s | `4f9580e59fd193254f26c33c96c747a58393b53f2f2d01bed60e39904c46cc3e` | 0 | 80 / 32 | both SAT, weight 10 |
| 107 | SAT / 57.124 s | `679cf3c5a5cf1b739894a28a622ada6866de0fbdf3168cf8461f9f75116ebe09` | 0 | 68 / 62 | both SAT, weight 10 |
| 108 | SAT / 75.071 s | `423dc6a174e31353d7a37d34a45465d2a9bbb4dae82c6e3544410e06a2f4d191` | 0 | 47 / 57 | both SAT, weight 10 |

All seven new schedules avoid all reviewed blocks. Each has independently replayed weight-10 effective logical mechanisms in both sectors, including zero canonical syndrome, nonzero canonical logical parity, zero physical syndrome, nontrivial physical logical class, and exact canonical/physical logical-parity equality. Repair was correctly not entered because both direct queries were SAT on every candidate.

## Independent controls

`source/rebuild_final_formula.py` does not import either Round86 compiler. It reconstructs the reviewed outer constraints and EFSSC equations from the vendored frozen model and final selector catalog.

- reviewed blocks reconstructed: 14,484;
- selectors reconstructed: 134;
- source selector truth evaluations: 134 / 134 true;
- new local domains exhausted: 62;
- local rank-membership evaluations: 267,840 = 62 x 720 x 6;
- ranks/memberships/assertions: 852 / 2,274 / 19,016;
- compiler formula raw SHA-256: `94d404da1777ef108a2a508dc55ca0f3fda68bc489482a00337d9acb7317ac4d`;
- fresh-printer raw SHA-256: `95562d673d6ea31fd6f47d1be6cb4b60b45ff9fbe7079e574c0b2d8c80ac159b`;
- parsed assertions: 19,016 on each side;
- structurally unequal corresponding assertions: 0;
- normalized AST SHA-256 on each side: `6ac624f2acb35a6311034829970b4d2993fcdf208080898a8e1dbeff1dcb3c7d`;
- solver check invoked by this checker: false.

The different raw SMT-LIB hashes are a disclosed printer-only difference: nested `let` abbreviations versus an expanded `or`. The exact parsed identity rules out a semantic or state mismatch. A negative control changes one residual kind and changes the selector semantic hash from `0570cc4a303b30f1d8636b770f577ef9a929798eb65cdb378ff86482d2bf3083` to `fdbb58119e465f33ed279cf0eeb391edd1fcccf1707258af87821150d67c04b4`.

`source/independent_state_replay.py` separately reconstructs all 14,484 reviewed blocks, binds all 120 reviewed selectors to the raw ledger, audits seven schedules, tests every schedule against all reviewed blocks and all selectors preceding it, and rebuilds all fourteen direct positive mechanisms from names. It reports PASS. Its negative controls force a same-check time collision and a duplicate fault name; both are rejected.

`source/analyze_all_new_selector_domains.py` regenerates the complete fourteen-selector integer census byte for byte. `vendor/round80/src/replay_direct_candidate.py` regenerates the seed direct DIMACS verification byte for byte. `replay.sh` runs all four independent paths and ends with `ROUND86_PACKAGE_REPLAY_PASS`.

## What this proves and does not prove

This package proves, at proposer level pending independent review:

1. EFSSC is an exact sound exclusion predicate for a declared fixed selector on all legal schedules in the frozen class.
2. The fourteen stored new selectors are valid on their declared source schedules in both sectors.
3. Seven legal MC0 schedules outside their then-current reviewed/EFSSC frontier each have an exact effective fault of weight 10 in both sectors.
4. Nine of the fourteen semantic domains strictly contain their corresponding source atom cube, by exact order-product counts.
5. The continuation state chain is atomic and ends at iteration 109 unstarted.

It does **not** prove:

- a distance-12 schedule;
- that every schedule has effective distance at most 11 or at most 10;
- exhaustion of the final outer formula;
- disjointness of selector domains or a union coverage fraction;
- an UNSAT statement of any kind;
- canonical promotion.

Positive SAT mechanisms reject candidates but cannot establish a universal ceiling. Conversely, an outer SAT schedule that merely avoids the current finite library would not establish distance 12; it must survive complete both-sector distance certification. The final formula is preserved as a continuation object and is intentionally unchecked after the last pair was installed.

## Fresh unstarted continuation

`continuation/final_state.json` and `continuation/checkpoint_state.json` agree exactly:

| Field | Value |
|---|---:|
| Next iteration | 109 |
| `started` | false |
| Reviewed generalized/dynamic blocks | 12,820 / 204 |
| Reviewed registry/raw mechanisms | 120 / 120 |
| Reviewed installed block predicates | 14,484 |
| Inherited reviewed EFSSCs | 120 |
| Round86 seed EFSSCs | 2 |
| Round86 incremental EFSSCs | 12 |
| Total EFSSCs | 134 |
| Final outer assertions | 19,016 |
| Selector-state SHA-256 | `9be75eba643ac167d5c51497ca8e5cd23eb1656f803a49cbd8e7f1285b004113` |
| Final compiler formula SHA-256 | `94d404da1777ef108a2a508dc55ca0f3fda68bc489482a00337d9acb7317ac4d` |
| Stop reason | null |

The next exact action, if separately authorized, is an outer check of the preserved iteration-109 formula with a checkable disposition. A SAT result must receive full both-sector certification. An UNSAT result is not a ceiling proof without an accepted proof object or independent exhaustive certificate for the full encoding.

## Reproduction environment and commands

Accepted environment:

- macOS 26.6.2 arm64, Darwin 25.6.0;
- Python 3.9.6;
- Z3 Python 5.1.0;
- PySAT 1.9.dev15;
- NumPy 2.0.2;
- six 1.17.0;
- CaDiCaL 1.9.5, commit `146207318796f094dcded87349a64f0c6927309e`;
- Git 2.50.1;
- `shasum` 6.02.

From this package directory:

```sh
CIRCDIST_PYTHON=/private/tmp/circdist-r72-dispatcher-venv/bin/python ./replay.sh
```

The replay requires Python with the listed Z3 and PySAT modules. It creates a session temporary directory, verifies the seal when manifests are present, regenerates all deterministic checker outputs, byte-compares them with sealed expected outputs, and deletes the temporary directory. It does not solve the final outer formula.

Direct component commands are encoded in the scripts and logs. The formula/state regeneration commands are:

```sh
$CIRCDIST_PYTHON source/independent_state_replay.py --root . --output /tmp/state.json
$CIRCDIST_PYTHON source/analyze_all_new_selector_domains.py \
  --package vendor/round80 --state continuation/final_state.json \
  --seed-direct data/seed_iter102/direct_verification.json --output /tmp/domains.json
$CIRCDIST_PYTHON source/rebuild_final_formula.py --root . \
  --compiler-smt2 formulas/final_outer.smt2 \
  --output-smt2 /tmp/rebuilt.smt2 --output-summary /tmp/formula.json
```

## Protocol validation

All commands were read only with respect to canonical state.

| Check | Result | Exit |
|---|---|---:|
| Package-local full replay | `ROUND86_PACKAGE_REPLAY_PASS` | 0 |
| `tools/test_dag_contracts.py` | 24 / 24 tests | 0 |
| `tools/proof_dag_check.py --problem circdist` | 16 node files structurally valid | 0 |
| `tools/evidence_closure_check.py --problem circdist` | 152 structured paths, closed | 0 |
| `tools/check_circdist_migration.py` | 16 nodes / 143 events / 728 copies | 0 |
| `proof_dag_check --previous-state ...` | nodes, routes, events retained | 0 |
| `tools/test_release_contracts.py` | 14 / 14 tests | 0 |
| `tools/lean_dag_check.py --selftest` | 23 / 23 assertions | 0 |
| `git diff --check` | clean | 0 |

Exact stdout, stderr, timing, and exit files are under `verification/` and `logs/`.

## FIX-2 and rollback accounting

`FIX-2.md` and `PROCESS_LEDGER.json` disclose all process incidents: the initial Z3 arity rejection, a full-DP domain census stopped at 14.36 GB RSS and replaced by an exact 79.6 MB meet-in-the-middle proof, and an over-strong raw-SMT byte comparison replaced only after exact AST identity was demonstrated. No rejected result mutated a continuation or canonical state. PID 97169 was explicitly terminated and reaped. No detached process is handed off.

## Proposed canonical evidence text only

A later independent reviewer may consider the following text; this proposer makes no YAML edit:

> Candidate evidence link: `circdist/artifacts/circdist_gross_efssc_round86_20260830/REPORT.md`. Round86 introduces exact fixed-selector semantic cuts, independently replays seven new legal schedules and fourteen both-sector weight-10 positive mechanisms, and freezes iteration 109 unstarted with 14,484 reviewed blocks plus 134 semantic cuts. Nine of fourteen new cuts strictly strengthen their source precedence cubes. No distance-12 witness or universal distance-11 ceiling is proved. Keep `CIRCDIST.gross` CONJECTURED with residual `D* in {11,12}` pending independent review.

## Seal and durable inventory

- Durable package path: `circdist/artifacts/circdist_gross_efssc_round86_20260830`
- Payload seal definition: SHA-256 of `PAYLOAD_SHA256SUMS.txt`; exact post-seal value is reported with delivery.
- Root seal definition: SHA-256 of `SHA256SUMS.txt`; exact post-seal value is reported with delivery.
- Per-file SHA-256 values: `PAYLOAD_SHA256SUMS.txt` and `SHA256SUMS.txt`.
- Per-file byte/line counts: `FILE_INVENTORY.jsonl` (all non-seal payload files; the inventory and seal files are reported with delivery).
- Canonical edits: none
- Prior artifact edits: none
- Network: unused
- Final root verdict: `CONTINUATION-ADVANCED-NOT-PROVED`
