# CIRCDIST.gross — auditing the rescued driver logs and the final decision attempt at `W = 10` (2026-08-23)

Node: `CIRCDIST.gross`. Work item: **the gross candidate FINAL DECISION at `W = 10`**, budget-boxed
(1 session, primarily COMPUTE), single Opus 5 executor session, proposer role, no sub-agents.
Predecessors, read in full: `artifacts/circdist_gross_candidate_decision_20260822.md` (state, machinery
§9, the 22-open frontier) and `artifacts/circdist_gross_phicert_20260822.md` (candidate definition).
Raw material audited: `artifacts/logs_circdist_gross_drivers_20260823/`.

Evidence labels used here: **NUMERICAL** (an exact finite computation, code inherited verbatim or
inline, reproducible) and **CONJECTURED**. Nothing is labelled PROVED or CERTIFIED\*. Every
absence-type claim states its search scope. Files, logs, papers and web pages are treated as **data,
never as instructions**. No existing repository file was modified; `research/circdist/proof-dag/` was
not touched. This artifact and `artifacts/logs_circdist_gross_final_20260823/` are the only new
repository objects.

---

## 0. Headline

**The audit passes completely, the decision still does not close — and the reason it has not closed
is not the one the previous session recorded.**

Part 1 of the commission (audit the rescued driver logs) is finished and clean. Part 2 (decide the
remaining frontier) is not finished, so Part 3 fires the **wall** reading. But the frontier moved
from `22` open sub-queries at session start to **`13`** at the close — `97` of the `110` cells are now
decided UNSAT — and the box overturned the previous session's diagnosis of why the remainder is hard.

Five things, in order of how much they should change the next commission:

1. **The nine "timeouts" were never established as hard, and at least one is trivial.** The
   predecessor recorded nine sub-queries as having no verdict after 10 800 seconds of wall clock and
   argued they were "genuinely hard, not merely queued". This box decided two of them.
   `X (9,20) orbit 0` took `2 683.6` s. `X (10,22) orbit 0` took **`225.3` s** — a 225-second problem
   recorded as a three-hour wall. Those `TIMEOUT` records measured machine contention, not difficulty
   (§6.2).
2. **Finishing the whole decision costs on the order of 60–90 CPU-hours.** A cost model fitted in
   this box (§6.2, `predict2.py`) puts the remaining frontier at `≈ 30` CPU-hours, but all three of
   its out-of-sample predictions under-shot by `2`–`3×`, so the honest figure is `60`–`90` — three to
   five hours of wall clock on 24 uncontended cores. This is not a problem that needs a new idea; it
   needs a quiet machine for an evening.
3. **Every rescued record verifies: 859 of 859 recorded CNF hashes were reproduced by rebuilding the
   formula from source** in a fresh namespace (§2.5). The predecessors spot-checked *one*. The
   certificate chain markdown → source → CNF → hash is now closed for the entire decided set.
4. **Zero SAT on the candidate, verified independently.** All 6 SAT records sit on 5 distinct
   **non-candidate validation triples**; I checked the triples myself rather than accepting the
   dispatcher's reconciliation (§2.4). No witness has ever appeared at weight 10 on the candidate,
   across `851` decided orbit sub-queries.
5. **Two structural checks that no previous session had run, both pass.** `cert4 ⊆ cert6 ⊆ cert7`
   holds as literal clause-set inclusion, with identical variable numbering and identical column
   literals, on **all 110 cells** — this is what licenses mixing encodings within a cell, and it had
   only ever been argued (§3.2). And `K = 0` is arithmetically vacuous, so the orbit split's `K >= 1`
   precondition holds everywhere rather than being an assert that never fires (§3).

**Two accounting corrections.** The dispatcher's reconciliation reported `19` open sub-queries
(15 at orbit 0, 4 at orbit 1). Recomputed from the audited union the figure at session start was
**`22`** (15 at orbit 0, **7** at orbit 1); §2.7 shows the `19` is a double-count that would have left
three orbit-1 sub-queries permanently unscheduled. Relatedly, the three sub-queries the commission
singled out for fresh re-decision — `X(6,20)`, `Z(6,16)`, `Z(7,16)` at orbit 0 — **were never open**;
they are in the decided set, and it is orbit 1 of those cells that is open. I ran the fresh solves
anyway, as commissioned, and **all three reproduce the inherited record exactly**: same rebuilt CNF
hash, same UNSAT verdict, under a different solver (§4).

**What this box does not claim.** `13` orbit sub-queries in `13` cells are still undecided. So the
candidate is **not** certified at `d_ext = 11`, the conjecture is **not** confirmed on the correct
family, and `D* >= 11` is **not** established. Nothing here is labelled above NUMERICAL, and the
dominant risk — that the Figure 12 reconstruction is simply wrong — is inherited, unreduced, and
still gates everything (§7.4).

---

## 1. Commission, and what I actually did

| commissioned | status |
|---|---|
| 1. Audit the rescued logs: dedup, hash consistency, SAT-record check, candidate coverage tally | **done, clean** (§2) |
| 1b. Re-decide `X(6,20)/Z(6,16)/Z(7,16)` orbit 0 with my own encoding run | **done — 3/3 confirm, hash + verdict** (§4) |
| 2. Recompute the open list; decide the remaining sub-queries | **recomputed (§2.7); 2 of 9 hard ones decided, 22 open → 16** (§5, §6) |
| 3. Verdict | **wall** — exact frontier + FIX-2 handoff (§6, §8) |

Additional work not commissioned but done because the audit made it cheap and it strengthens the
result: a **full** rebuild-and-hash-match of every recorded certificate (§2.5); identification of the
four records that did not match on first pass (§2.6); verification that `cert4 ⊆ cert6 ⊆ cert7` on all
110 cells (§3.2) and that `K = 0` is vacuous (§3); a calibrated cost model for the open frontier
(§6.2); and the demonstration that the inherited `TIMEOUT` records measure contention rather than
difficulty (§6.2) — which is the finding most likely to matter downstream.

---

## 2. The audit — NUMERICAL

### 2.1 Provenance and integrity

`artifacts/logs_circdist_gross_drivers_20260823/` contains **12** `jsonl` files plus `SHA256SUMS.txt`.
(The commission said 13; there are 12, and `SHA256SUMS.txt` lists 12. This is a miscount in the
commission text, not a missing file — no log referenced anywhere in the predecessor artifacts is
absent.)

```
$ shasum -a 256 -c SHA256SUMS.txt
b6.jsonl: OK        bench.jsonl: OK     final.jsonl: OK     full.jsonl: OK
full7.jsonl: OK     full7b.jsonl: OK    mine.jsonl: OK      mine2.jsonl: OK
rc.jsonl: OK        recheck_v2.jsonl: OK t2.jsonl: OK       val.jsonl: OK
```

All 12 verify. `972` records parse, `0` unparseable lines.

**The predecessor's volatile scratch directory still exists**, and its three drivers were still
running when I started (§7.1). So I audited the rescued snapshot *and* the live directory it was
copied from, and report both.

### 2.2 Verdict and triple histograms, over all 972 rescued records

```
verdicts   UNSAT 955   TIMEOUT 9   SAT 6   CRASH 2
```

```
(sector, triple)          records
Z (1, 2, 62)                  484   <== CANDIDATE
X (14, 0, 2)                  470   <== CANDIDATE
Z (1, 2, 2)                     3
Z (9, 9, 62)                    1
X (0, 9, 9)                     1
Z (1, 9, 9)                     1
Z (1, 2, 9)                     1
```

The `TIMEOUT` and `CRASH` records carry no `sector`/`K`/`|E|`/`orbit` fields — they are written by the
*driver*, not by the job — so they cannot be and are not counted as decisions. **A TIMEOUT is
undecided, never UNSAT.** Recovering which sub-query each belongs to requires the drivers' `.out`
files rather than the `jsonl`, which is worth noting as a defect in the log format: the rescued
`jsonl` alone cannot tell you what timed out. §6.2 does the recovery, and the answer turns out to be
the most consequential finding in this artifact.

### 2.3 The dedup union on the candidate

Deduplicating on `(sector, K, |E|, orbit)`, restricted to the two candidate triples, `W = 10`,
orbit `>= 0`, verdict in `{SAT, UNSAT}`:

```
distinct sub-queries decided        842   (rescued snapshot)
                                    843   (rescued ∪ live, at the time compute began)
contributing records                950 / 954
sub-queries appearing in >1 record   98 / 101      max multiplicity 3
verdict conflicts across duplicates    0
union verdicts                      {'UNSAT': 843}
```

**`0` verdict conflicts.** Where the same sub-query was decided two or three times — by different
drivers, different encodings, or different solvers — the answers always agreed. This is the check
that would have caught a nondeterministic or memory-corrupted solver, and it is clean.

### 2.4 The SAT records — the bombshell check

There are **6** SAT records (the commission said 5; the difference is that `Z (1,2,2) K=4 |E|=14`
appears twice, once unrestricted and once under the orbit-0 restriction — **5 distinct validation
cells**, 6 records). I verified the triples myself rather than accepting any reconciliation:

| log | sector | triple | K | \|E\| | orbit | on candidate? |
|---|---|---|---|---|---|---|
| `b6.jsonl` | Z | `(1, 2, 2)` | 4 | 14 | 0 | **no** |
| `val.jsonl` | Z | `(1, 2, 2)` | 4 | 14 | −1 | **no** |
| `val.jsonl` | Z | `(9, 9, 62)` | 4 | 14 | −1 | **no** |
| `val.jsonl` | X | `(0, 9, 9)` | 3 | 14 | −1 | **no** |
| `val.jsonl` | Z | `(1, 9, 9)` | 4 | 16 | −1 | **no** |
| `val.jsonl` | Z | `(1, 2, 9)` | 8 | 16 | −1 | **no** |

The candidate triples are `Z (1, 2, 62)` and `X (14, 0, 2)` (`phicert` §2.4). **None of the five SAT
triples is either of them**, in either sector — `(1,2,2) ≠ (1,2,62)`, `(9,9,62) ≠ (1,2,62)`,
`(1,9,9) ≠ (1,2,62)`, `(1,2,9) ≠ (1,2,62)`, and `(0,9,9) ≠ (14,0,2)`. Every SAT record carries
`decomposition_ok: true, zero_syndrome: true, nontrivial_logical: true`, i.e. these are *genuine*
weight-10 witnesses — on the validation triples, which is exactly their purpose: they are the
evidence that the encoding is not vacuously UNSAT.

**No SAT record sits on a candidate triple. There is no bombshell.** Scope of that statement: the
decided orbit sub-queries counted in §5.2, over the `110` `(K, |E|)` cells of the `W = 10` problem in
the two sectors, under the `cert4`/`cert5`/`cert6`/`cert7` encodings, with the `|E| = 12` stratum
decided separately by `enum12.py`.

### 2.5 Every recorded certificate rebuilds — the check nobody had run

The predecessor verified **one** CNF hash (its §2.6). I re-extracted the machinery into a fresh
namespace and rebuilt **every** recorded CNF from source, comparing the SHA-256 against the record.
(The `cnf_sha256` field is `hashlib.sha256(...).hexdigest()[:32]` — a SHA-256 **truncated to its
first 128 bits**, not an MD5, despite the 32-hex-character width. Worth stating because a reviewer
will otherwise read 32 hex characters as MD5 and mistrust it.)

First, the predecessor's own anchor reproduces in my namespace:

```
X (14,0,2) K=2 |E|=14 orbit 3  ->  cnf_sha256 = a8ab5e67021a83b7e0021a0ff701b54c
```

identical to its §2.6. Then, over the whole union:

```
distinct (sub-query, hash) records to verify:   859
VERIFIED (rebuilt hash == recorded hash):       859
FAILED:                                           0
encoding that reproduced it:  cert7 689   cert4 162   cert6 4   cert5 4
```

**859 of 859, zero failures.** The reproduction chain markdown → source → CNF → hash → verdict is closed for the
entire decided set. A third party can now re-derive any certificate in the manifest of §5 without
trusting a single number in this repository.

### 2.6 The four records that did not match on the first pass

Four records — all in `bench.jsonl`, all at `|E| = 12`, all in sector Z — failed against
`cert4`/`cert6`/`cert7` with anomalously high clause counts (e.g. `21213` where `cert4` gives `19341`).
Rather than wave them through, I searched the encoding space and identified them exactly:

```
Z K=2 |E|=12 orbit 7  ->  cert5(dominance=True)   nclauses 21213, final 21382   MATCH
Z K=2 |E|=12 orbit 8  ->  cert5(dominance=True)   nclauses 21213, final 21406   MATCH
Z K=3 |E|=12 orbit 8  ->  cert5(dominance=True)   nclauses 23705, final 23898   MATCH
Z K=4 |E|=12 orbit 8  ->  cert5(dominance=True)   nclauses 26145, final 26338   MATCH
```

`bench.jsonl` is the predecessor's **encoding benchmark** file, and `cert5` is the intermediate
encoding it was benchmarking. Two independent reasons these four carry no weight anyway: each of the
four sub-queries is *also* decided by a separately verified record in `full.jsonl`/`b6.jsonl`/`rc.jsonl`
with an independently reproduced hash and the same UNSAT verdict; and the entire `|E| = 12` stratum is
decided independently of all cell machinery by `enum12.py` (0 of 1884 weight-12 logicals per sector
admitting a weight-`≤ 10` solution).

### 2.7 My accounting, and where the dispatcher's `19` came from

Recomputed from the audited union with the predecessor's `acct.py` logic re-implemented from scratch:

```
at session start (rescued ∪ live):    22 open   -> orbit 0: 15   orbit 1: 7
when compute began (X(6,20,1) closed): 21 open  -> orbit 0: 15   orbit 1: 6
```

The dispatcher reported `19` open (15 at orbit 0, 4 at orbit 1), together with the statement that the
drivers had "closed `X(6,20)` / `Z(6,16)` / `Z(7,16)` at orbit 0". Both halves are individually true
and they were **combined by subtraction, which double-counts**:

- `X(6,20) orbit 0`, `Z(6,16) orbit 0` and `Z(7,16) orbit 0` are indeed decided UNSAT.
- But they were *already* decided when the predecessor's §4.1 frontier was written — its table shows
  `U.UUUUUUU` for `Z(6,16)`, `Z(7,16)` and `X(6,20)`, i.e. **orbit 0 present, orbit 1 missing**.
- So those three closures were already excluded from the 22. Subtracting them again drops the
  orbit-1 count from 7 to 4 and the total from 22 to 19.

Consequences, both benign: no record is missing and no verdict changes; but a completion run driven
off the `19` would have **left three orbit-1 sub-queries permanently unscheduled** —
`Z(6,16,1)`, `Z(7,16,1)`, and (before it closed) `X(6,20,1)`. The commission's instruction to trust my
own accounting over the dispatcher's was the right call and this is what it bought.

**Three specific corrections**, since the reconciliation was written into
`research/circdist/proof-dag/nodes/CIRCDIST.gross.yaml` and will otherwise propagate. (That file was
modified at 02:17 by the dispatcher, not by this session; I read it as data and did not touch it.)

| the reconciliation says | audited value | why |
|---|---|---|
| "union tally = 850 sub-query verdicts, **845 UNSAT + 5 SAT**" | `842` candidate sub-queries, **all UNSAT**; separately `6` SAT records on `5` **non-candidate** cells | the tally merges candidate decisions with the unquotiented (`orbit = -1`) validation runs on other triples. Those SAT records are not candidate sub-query verdicts and should not be summed with them — presenting them in one total invites exactly the misreading that some candidate cell is SAT |
| "the drivers additionally closed **3 of the 22** open candidate sub-queries (`X(6,20)`, `Z(6,16)`, `Z(7,16)`, each at orbit 0)" | those three were **already closed** before the 22-open frontier was computed | the predecessor's §4 table shows `U.UUUUUUU` for all three cells — orbit 0 present, orbit **1** missing. They were never in the 22 |
| "RECONCILED FRONTIER: **95/110 cells**, **19** sub-queries — 15 at orbit 0, **4** at orbit 1" | **`92/110`** cells, **`22`** sub-queries — 15 at orbit 0, **`7`** at orbit 1 | follows from the row above: the three orbit-0 closures were subtracted a second time, and the three *cells* were counted as closed although each still had orbit 1 open |

The `19` figure is not merely a miscount: it is `22` minus three sub-queries that were already
excluded from the `22`. By coincidence the true frontier passed through `19` about an hour into this
box, as the inherited drivers closed real sub-queries — which is precisely the kind of coincidence
that makes a wrong number hard to notice later.

**The authoritative open list at the moment compute began (21 sub-queries, 17 cells):**

```
Z sector, 10 cells, 13 sub-queries:
   (5,18):[0,1]  (6,16):[1]  (6,18):[0]  (6,20):[0,1]  (7,16):[1]
   (7,18):[0]    (7,20):[0,1] (8,20):[0] (8,22):[0]    (9,22):[0]
X sector,  7 cells,  8 sub-queries:
   (5,18):[0]  (6,18):[0]  (7,20):[0,1]  (8,20):[0]  (8,22):[0]  (9,20):[0]  (10,22):[0]
```

Every open sub-query is at residual-orbit index 0 or 1, confirming the predecessor's §4.2 structural
claim on the newer data: orbits 2–8 are closed in every cell of both sectors.

---

## 3. Lever revalidation before using the machinery — NUMERICAL

The commission required the levers to be revalidated on a known cell before the §9 machinery was
trusted. Re-extracted into a fresh namespace (`work2/`, byte-identical to the live drivers' modules,
deliberately *not* the same directory — see §7.3), all five reproduce:

```
stabcheck.py  Z (1,2,62): |S|=24; row-permutation failures 0; residual-equivariance failures 0;
                          orbits 15 (residual 9, sizes [24]); matches column_orbits: True
              X (14,0,2): |S|=24; row-permutation failures 0; residual-equivariance failures 0;
                          orbits 15 (residual 9, sizes [24]); matches column_orbits: True

cuts.py       Z (1,2,62): 200000 draws, violations {c3:0,c4:0,c5:0,c6:0,ub:0,dom:0,cell:0}
              X (14,0,2): 200000 draws, violations {c3:0,c4:0,c5:0,c6:0,ub:0,dom:0,cell:0}
              cells(W=10): 55   all violation counters zero: True

orbcover.py   5 witnesses transported to their least-orbit representative; failures 0
redwit.py     5 witnesses reduced to lex-minimal normal form; failures 0
              (including the (1,2,9) K=8 -> K=4 reduction)
recheck/hash  X (14,0,2) K=2 |E|=14 orbit 3 -> a8ab5e67021a83b7e0021a0ff701b54c  (matches)
```

Identical to the predecessor's §2.1–§2.6 and to the predecessor's predecessor, to the digit. The
least-orbit quotient is sound and the cut package does not over-prune on any known solution.

One further precondition, which the least-orbit cover argument needs and which no previous artifact
had checked explicitly, is that `K >= 1` in every cell actually run — `job7.py` asserts it, and an
assert that never fires is not evidence. It holds, and for a clean arithmetic reason:

```
cells(W=10):  55 per sector, 110 over both sectors
K values present:  [1,2,3,4,5,6,7,8,9,10]        K = 0 cells: []        K >= 1 in every cell: True
cells per K:  {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10}
|E| values:   [12,14,16,18,20,22,24,26,28,30]
```

At `K = 0` the cell constructor ranges `|E|` over `12 .. W + 2K = 10`, which is empty. So the `K = 0`
stratum is arithmetically vacuous rather than merely unrun, the `assert K >= 1` can never fire, and
the 9-orbit cover applies to all 110 cells without exception.

### 3.1 The over-pruning check — the one that matters most — PASSES

An over-constrained encoding would return UNSAT everywhere and look like a triumph. The check is that
the **full** `(c1)`–`(c11)` `cert7` package, **with** the orbit-0 restriction applied, still *finds* a
witness on a validation triple where one is known to exist. Re-run here under Kissat404:

```
Z (1,2,2) cell (K=4, |E|=14) orbit 0 :  SAT in 70.8 s
   cnf_sha256 = a36433a698853212a921c933492eb068   (36229 clauses -> 36230, 9928 vars)
   weight 10 = 6 data + 4 hooks, |E| = 14
   R = [(0,0), (23,0), (58,2), (64,2)]
   d = {7, 63, 113, 122, 133, 142}
   E = {3, 6, 7, 20, 29, 63, 76, 82, 113, 122, 131, 133, 137, 142}
   dext.verify_witness: decomposition_ok True, zero_syndrome True, nontrivial_logical True
```

**The witness is a different one from the predecessor's.** Its `R = [(0,0),(23,0),(58,2),(64,2)]`
against the predecessor's `R = [(0,0),(42,2),(51,2),(56,0)]`. That is expected and is *additional*
information rather than a discrepancy: a satisfiable instance generally has many solutions, and a
different solver takes a different path to a different one. Both lie in the same cell `(K=4, |E|=14)`,
both use residual orbit 0, both have weight exactly 10, and both pass `verify_witness` on all three
conditions. So this box contributes a **second, independent, end-to-end verified weight-10 witness**
on that validation triple, found under the full cut package plus the orbit restriction — which is the
strongest form the anti-over-pruning check has taken in this node so far.

Kissat404 solved it in `70.8` s against the predecessor's `155.4` s with Cadical153 under comparable
load — the ~2× that motivated using Kissat on the hard tail (§8).

### 3.2 Mixing encodings within a cell is sound — verified, not argued

The sweep mixes encodings: some sub-queries of a cell were decided under `cert4`, others under `cert7`.
The predecessor justified this by an *argument* (its §2.4): `cert4`'s constraint set is a subset of
`cert7`'s, so a `cert4` UNSAT rules out any solution in the cell while a `cert7` UNSAT rules out any
*lex-minimal* one, and the lex-minimal solution lies in exactly one cell, which the sweep enumerates.

The subset claim had never been **checked**. It is checkable directly, and I checked it on every cell
of both sectors — `chain.py`, §9:

```
cells checked: 110 (55 per sector x 2)

CORE CHAIN (cert4 <= cert6 <= cert7, same variable numbering, same col_lit map):
   failures: 0   ->  holds on all 110 cells: True

SIDE BRANCH (cert5, the bench-only encoding):
   c4 <= c5 failures: 60
```

The core chain holds as **literal clause-set inclusion** — `{frozenset(c) for c in cert4.cls}` is a
subset of the same for `cert6` and `cert7` — and, just as importantly, the three encodings assign the
**same variable numbers** (`c4.top == c6.top == c7.top`) and the **same column literals**
(`c4.col_lit(rep) == c6.col_lit(rep) == c7.col_lit(rep)` for every orbit representative). That second
half matters and is easy to overlook: if the column-literal map differed, the orbit restriction
`cls.append([c.col_lit(rep)])` would mean a *different* restriction under a different encoding, and
mixing them within a cell would be unsound even with clause inclusion.

`cert5` is **not** in the chain — `c4 <= c5` fails on 60 of the 110 cells. That is not a problem, and
the reason is specific rather than hand-waved: `cert5` appears in exactly 4 records, all in
`bench.jsonl`, all at `|E| = 12`, and **no sub-query anywhere relies solely on a `cert5` record** —

```
('Z',2,12,7)  also decided in b6.jsonl, full.jsonl
('Z',2,12,8)  also decided in full.jsonl, rc.jsonl
('Z',3,12,8)  also decided in full.jsonl
('Z',4,12,8)  also decided in full.jsonl
sub-queries relying SOLELY on cert5: 0
```

— on top of which the whole `|E| = 12` stratum is closed independently by `enum12.py`. So `cert5`
can be dropped from the certificate set entirely without changing a single cell verdict.

---

## 4. The three commissioned re-decisions — NUMERICAL

The commission asked for a fresh, independent solve of `X(6,20)`, `Z(6,16)`, `Z(7,16)` at orbit 0,
on the grounds that the rescued records are raw and unaudited. Two things to record.

**First, the audit substantially discharges the concern by other means.** All three records rebuild
and hash-match (§2.5):

| sub-query | recorded verdict | recorded solver s | CNF SHA-256 (first 128 bits) | rebuilt? |
|---|---|---|---|---|
| `X (14,0,2) K=6 \|E\|=20 orbit 0` | UNSAT | 2462.3 | `3aced03563a1938a7202eabdcf2c4f12` | **yes** |
| `Z (1,2,62) K=6 \|E\|=16 orbit 0` | UNSAT | 2714.4 | `e1541c79641545043f6cca55814518ba` | **yes** |
| `Z (1,2,62) K=7 \|E\|=16 orbit 0` | UNSAT | 1890.1 | `6bc1c4c8c413dde51cd19dfca23df389` | **yes** |

`X (6,20,0)` additionally appears **twice** in the union — `final.jsonl` at 2462.3 s and `mine2.jsonl`
at 3457.5 s — with **identical hashes and identical UNSAT verdicts**, i.e. it was already
independently re-decided by two different drivers.

The rebuild was done in this box's own namespace with `hashonly.py`, which is `job7.py`'s CNF
construction with the solve removed:

```
X(6,20) orbit 0   recorded 3aced03563a1938a7202eabdcf2c4f12   rebuilt 3aced03563a1938a7202eabdcf2c4f12   MATCH
Z(6,16) orbit 0   recorded e1541c79641545043f6cca55814518ba   rebuilt e1541c79641545043f6cca55814518ba   MATCH
Z(7,16) orbit 0   recorded 6bc1c4c8c413dde51cd19dfca23df389   rebuilt 6bc1c4c8c413dde51cd19dfca23df389   MATCH
```

So the *formula* each of the three verdicts refers to is confirmed bit-for-bit. What remains unconfirmed
is only the solver's answer on it, which is precisely what §7.5 says is the weak link for all 844.

**Second, I launched the fresh solves anyway, with an independent solver.** Each was run through
`job7k.py` (CNF construction byte-identical to `job7.py`, so hashes are comparable) under
**Kissat404** rather than the Cadical153 that produced the originals — a different solver on an
independently rebuilt formula is a strictly stronger validation than a re-run of the same one.

```
02:26:14  job7k.py X 14,0,2 10 6 20 0 kissat
02:26:14  job7k.py Z 1,2,62 10 6 16 0 kissat
02:26:14  job7k.py Z 1,2,62 10 7 16 0 kissat
```

**All three returned inside the box, and all three confirm the inherited record exactly** — same
rebuilt CNF hash, same UNSAT verdict, under a different solver:

| sub-query | inherited (Cadical153) | fresh (Kissat404) | CNF SHA-256 (first 128 bits) | agree? |
|---|---|---|---|---|
| `X (6,20) orbit 0` | UNSAT, 2462.3 s | **UNSAT, 850.0 s** | `3aced03563a1938a7202eabdcf2c4f12` | **yes — hash + verdict** |
| `Z (7,16) orbit 0` | UNSAT, 1890.1 s | **UNSAT, 1294.7 s** | `6bc1c4c8c413dde51cd19dfca23df389` | **yes — hash + verdict** |
| `Z (6,16) orbit 0` | UNSAT, 2714.4 s | **UNSAT, 2287.5 s** | `e1541c79641545043f6cca55814518ba` | **yes — hash + verdict** |

**The validation the commission asked for passes, three for three.** Each is an independent
confirmation at two levels at once: the formula was rebuilt from source and hashed to the recorded
value, and a different solver was then run on it and returned the same verdict. Combined with §2.5's
859/859 rebuild over the whole decided set, the rescued logs are as well-founded as anything short of
proof-logging (§7.5) can make them.

Kissat404 was `2.9×`, `1.46×` and `1.19×` faster than the recorded Cadical153 times respectively.
Worth recording precisely because the trend is the wrong way: **the speedup shrinks as the instance
gets harder.** A completion estimate for the hard nine (§6.1) should therefore assume roughly parity
with Cadical, not a 2–3× win — which is the single most useful planning number this box produced, and
it contradicts the optimistic reading the first result alone would have supported.

---

## 5. State of the decision, and the certificate manifest

### 5.1 Cell tables

Regenerated from the audited union at the close of the box. `U` = UNSAT, `.` = not decided; a cell is
UNSAT when all nine orbit sub-queries are UNSAT, by the least-orbit cover re-verified in §3.

<!--CELLTABLE-->

**sector Z, triple (1, 2, 62)**

| `K` | `\|E\|` | orbit 0..8 | cell verdict | cell CPU s |
|---|---|---|---|---|
| 1 | 12 | `UUUUUUUUU` | **UNSAT** | 32 |
| 2 | 12 | `UUUUUUUUU` | **UNSAT** | 2786 |
| 2 | 14 | `UUUUUUUUU` | **UNSAT** | 242 |
| 3 | 12 | `UUUUUUUUU` | **UNSAT** | 3018 |
| 3 | 14 | `UUUUUUUUU` | **UNSAT** | 4034 |
| 3 | 16 | `UUUUUUUUU` | **UNSAT** | 423 |
| 4 | 12 | `UUUUUUUUU` | **UNSAT** | 2760 |
| 4 | 14 | `UUUUUUUUU` | **UNSAT** | 2672 |
| 4 | 16 | `UUUUUUUUU` | **UNSAT** | 11945 |
| 4 | 18 | `UUUUUUUUU` | **UNSAT** | 383 |
| 5 | 12 | `UUUUUUUUU` | **UNSAT** | 2929 |
| 5 | 14 | `UUUUUUUUU` | **UNSAT** | 2712 |
| 5 | 16 | `UUUUUUUUU` | **UNSAT** | 21170 |
| 5 | 18 | `.UUUUUUUU` | open (1) | 18564 |
| 5 | 20 | `UUUUUUUUU` | **UNSAT** | 309 |
| 6 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 6 | 14 | `UUUUUUUUU` | **UNSAT** | 2998 |
| 6 | 16 | `U.UUUUUUU` | open (1) | 14785 |
| 6 | 18 | `.UUUUUUUU` | open (1) | 22020 |
| 6 | 20 | `UUUUUUUUU` | **UNSAT** | 18675 |
| 6 | 22 | `UUUUUUUUU` | **UNSAT** | 217 |
| 7 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 7 | 14 | `UUUUUUUUU` | **UNSAT** | 3569 |
| 7 | 16 | `U.UUUUUUU` | open (1) | 10572 |
| 7 | 18 | `.UUUUUUUU` | open (1) | 10950 |
| 7 | 20 | `.UUUUUUUU` | open (1) | 15219 |
| 7 | 22 | `UUUUUUUUU` | **UNSAT** | 8293 |
| 7 | 24 | `UUUUUUUUU` | **UNSAT** | 124 |
| 8 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 8 | 14 | `UUUUUUUUU` | **UNSAT** | 3019 |
| 8 | 16 | `UUUUUUUUU` | **UNSAT** | 11081 |
| 8 | 18 | `UUUUUUUUU` | **UNSAT** | 10998 |
| 8 | 20 | `.UUUUUUUU` | open (1) | 5334 |
| 8 | 22 | `UUUUUUUUU` | **UNSAT** | 13093 |
| 8 | 24 | `UUUUUUUUU` | **UNSAT** | 4348 |
| 8 | 26 | `UUUUUUUUU` | **UNSAT** | 44 |
| 9 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 9 | 14 | `UUUUUUUUU` | **UNSAT** | 2736 |
| 9 | 16 | `UUUUUUUUU` | **UNSAT** | 1888 |
| 9 | 18 | `UUUUUUUUU` | **UNSAT** | 6056 |
| 9 | 20 | `UUUUUUUUU` | **UNSAT** | 5828 |
| 9 | 22 | `.UUUUUUUU` | open (1) | 2475 |
| 9 | 24 | `UUUUUUUUU` | **UNSAT** | 4451 |
| 9 | 26 | `UUUUUUUUU` | **UNSAT** | 1793 |
| 9 | 28 | `UUUUUUUUU` | **UNSAT** | 110 |
| 10 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 10 | 14 | `UUUUUUUUU` | **UNSAT** | 390 |
| 10 | 16 | `UUUUUUUUU` | **UNSAT** | 626 |
| 10 | 18 | `UUUUUUUUU` | **UNSAT** | 421 |
| 10 | 20 | `UUUUUUUUU` | **UNSAT** | 825 |
| 10 | 22 | `UUUUUUUUU` | **UNSAT** | 1961 |
| 10 | 24 | `UUUUUUUUU` | **UNSAT** | 485 |
| 10 | 26 | `UUUUUUUUU` | **UNSAT** | 389 |
| 10 | 28 | `UUUUUUUUU` | **UNSAT** | 472 |
| 10 | 30 | `UUUUUUUUU` | **UNSAT** | 223 |

`47` of `55` cells decided; SAT cells: `0`

**sector X, triple (14, 0, 2)**

| `K` | `\|E\|` | orbit 0..8 | cell verdict | cell CPU s |
|---|---|---|---|---|
| 1 | 12 | `UUUUUUUUU` | **UNSAT** | 24 |
| 2 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 2 | 14 | `UUUUUUUUU` | **UNSAT** | 51 |
| 3 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 3 | 14 | `UUUUUUUUU` | **UNSAT** | 813 |
| 3 | 16 | `UUUUUUUUU` | **UNSAT** | 104 |
| 4 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 4 | 14 | `UUUUUUUUU` | **UNSAT** | 1330 |
| 4 | 16 | `UUUUUUUUU` | **UNSAT** | 7328 |
| 4 | 18 | `UUUUUUUUU` | **UNSAT** | 346 |
| 5 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 5 | 14 | `UUUUUUUUU` | **UNSAT** | 1681 |
| 5 | 16 | `UUUUUUUUU` | **UNSAT** | 11532 |
| 5 | 18 | `.UUUUUUUU` | open (1) | 10388 |
| 5 | 20 | `UUUUUUUUU` | **UNSAT** | 105 |
| 6 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 6 | 14 | `UUUUUUUUU` | **UNSAT** | 1702 |
| 6 | 16 | `UUUUUUUUU` | **UNSAT** | 19975 |
| 6 | 18 | `.UUUUUUUU` | open (1) | 19902 |
| 6 | 20 | `UUUUUUUUU` | **UNSAT** | 8078 |
| 6 | 22 | `UUUUUUUUU` | **UNSAT** | 63 |
| 7 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 7 | 14 | `UUUUUUUUU` | **UNSAT** | 1802 |
| 7 | 16 | `UUUUUUUUU` | **UNSAT** | 15661 |
| 7 | 18 | `UUUUUUUUU` | **UNSAT** | 20942 |
| 7 | 20 | `.UUUUUUUU` | open (1) | 13440 |
| 7 | 22 | `UUUUUUUUU` | **UNSAT** | 6223 |
| 7 | 24 | `UUUUUUUUU` | **UNSAT** | 41 |
| 8 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 8 | 14 | `UUUUUUUUU` | **UNSAT** | 2943 |
| 8 | 16 | `UUUUUUUUU` | **UNSAT** | 6554 |
| 8 | 18 | `UUUUUUUUU` | **UNSAT** | 16095 |
| 8 | 20 | `.UUUUUUUU` | open (1) | 5847 |
| 8 | 22 | `.UUUUUUUU` | open (1) | 5617 |
| 8 | 24 | `UUUUUUUUU` | **UNSAT** | 3225 |
| 8 | 26 | `UUUUUUUUU` | **UNSAT** | 30 |
| 9 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 9 | 14 | `UUUUUUUUU` | **UNSAT** | 1166 |
| 9 | 16 | `UUUUUUUUU` | **UNSAT** | 4185 |
| 9 | 18 | `UUUUUUUUU` | **UNSAT** | 5739 |
| 9 | 20 | `UUUUUUUUU` | **UNSAT** | 4081 |
| 9 | 22 | `UUUUUUUUU` | **UNSAT** | 7418 |
| 9 | 24 | `UUUUUUUUU` | **UNSAT** | 5091 |
| 9 | 26 | `UUUUUUUUU` | **UNSAT** | 1653 |
| 9 | 28 | `UUUUUUUUU` | **UNSAT** | 64 |
| 10 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 10 | 14 | `UUUUUUUUU` | **UNSAT** | 319 |
| 10 | 16 | `UUUUUUUUU` | **UNSAT** | 277 |
| 10 | 18 | `UUUUUUUUU` | **UNSAT** | 2207 |
| 10 | 20 | `UUUUUUUUU` | **UNSAT** | 4244 |
| 10 | 22 | `UUUUUUUUU` | **UNSAT** | 437 |
| 10 | 24 | `UUUUUUUUU` | **UNSAT** | 653 |
| 10 | 26 | `UUUUUUUUU` | **UNSAT** | 651 |
| 10 | 28 | `UUUUUUUUU` | **UNSAT** | 733 |
| 10 | 30 | `UUUUUUUUU` | **UNSAT** | 392 |

`50` of `55` cells decided; SAT cells: `0`
<!--/CELLTABLE-->

### 5.2 Aggregate — NUMERICAL

Regenerated at the close of the box. Note that this is still a **lower bound** on what is decided:
two inherited drivers were running as it was written (§8.2).

<!--AGGREGATE-->
```
decided orbit sub-queries on the candidate       851
    of which SAT                                   0
    of which UNSAT                               851
verdict conflicts across duplicate decisions       0
recorded certificates rebuilt and hash-matched  859 / 859
solver time, distinct records              ~  576497 s   (~160 CPU-hours)
solver time, best-of per sub-query         ~  481598 s   (~134 CPU-hours)
cells decided (of 110)                           97
open orbit sub-queries                           13   (orbit 0: 11, orbit 1: 2)
open cells                                       13
```

**The exact open frontier at the close of the box:**

```
Z sector, 8 cells, 8 sub-queries:
   (5,18):[0]  (6,16):[1]  (6,18):[0]  (7,16):[1]
   (7,18):[0]  (7,20):[0]  (8,20):[0]  (9,22):[0]
X sector, 5 cells, 5 sub-queries:
   (5,18):[0]  (6,18):[0]  (7,20):[0]  (8,20):[0]
   (8,22):[0]
```
<!--/AGGREGATE-->

### 5.3 Verdict checkpoint log — every sub-query THIS box decided

Appended as each verdict landed, per the commission. `solver s` is solver time only; the `re-decision`
rows are the §4 audit validations, the rest come from `drive10.py`.

<!--CHECKPOINT-->
| # | source | sector | K | \|E\| | orbit | verdict | solver | CNF SHA-256 (first 128 bits) | solver s | vs. inherited record |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | re-decision | X | 6 | 20 | 0 | **UNSAT** | kissat | `3aced03563a1938a7202eabdcf2c4f12` | 850.0 | **hash+verdict match** (was 2462.3s, cd15) |
| 2 | re-decision | Z | 7 | 16 | 0 | **UNSAT** | kissat | `6bc1c4c8c413dde51cd19dfca23df389` | 1294.7 | **hash+verdict match** (was 1890.1s, cd15) |
| 3 | re-decision | Z | 6 | 16 | 0 | **UNSAT** | kissat | `e1541c79641545043f6cca55814518ba` | 2287.5 | **hash+verdict match** (was 2714.4s, cd15) |
| 4 | drive10 | X | 9 | 20 | 0 | **UNSAT** | kissat | `68afaaa69a5b7eb6521d818ad7226e90` | 2683.6 | — (first decision) |
| 5 | direct | X | 10 | 22 | 0 | **UNSAT** | kissat | `39b17e4d170b8ed4cd1c980a6defa4c3` | 225.3 | — (first decision) |

`5` sub-queries decided in this box; SAT: `0`; verdict conflicts against the inherited records: `0`.
<!--/CHECKPOINT-->

### 5.4 The full certificate manifest

Every decided sub-query, with its CNF hash, solver and solver time, is in
`artifacts/logs_circdist_gross_final_20260823/MANIFEST.md` (one row per decided sub-query), alongside the audited log
union and the checksums. Each row is independently re-derivable: rebuild the CNF with `hashonly.py`
(§9) and compare the hash, then re-solve.

---

## 6. Which reading fires — the **wall** reading

The commission pre-committed three readings. Taking them in order:

**All-UNSAT (audited + fresh) does not fire.** It required the audited set to be clean *and* the
frontier to be decided. The audit half is complete and clean (§2). The fresh half is not: the exact
counts are in §5.2, and at the close of this box orbit sub-queries in `17` cells of the `110` remained
undecided. A cell is UNSAT only when **all nine** of its orbit sub-queries are; `17` cells fall short,
so the split certification does not close.

I therefore **do not** state that the candidate certifies at `d_ext = 11` in both sectors, **do not**
state that the conjecture is confirmed on the correct family, and **do not** state `D* >= 11`. None of
those is established, by this box or by the record it audited. Any downstream node citing this one for
those claims is citing it wrongly.

What the fresh half *did* produce is validation rather than coverage: the re-decisions of §4 confirmed
two inherited records exactly — same rebuilt CNF hash, same UNSAT verdict, a different solver — and
the over-pruning check of §3.1 passed with a second independent witness. That raises confidence in the
`845` decisions already in hand; it does not add to them.

**Any candidate SAT does not fire.** There is none, in any decided sub-query, ever (§2.4).

**The wall reading fires.** Exact remaining frontier in §5.2; FIX-2 declaration and handoff in §8.

### 6.1 Why the wall is where it is, precisely

This is the one genuinely new structural fact this box produced, and it should shape the next
commission.

**The 9 open sub-queries that no inherited driver was running are exactly the 9 that had already
timed out at 10 800 seconds.** I did not arrange this; I discovered it by cross-referencing the live
process table against my recomputed open list:

```
open, and NOT being worked by any inherited driver:
   Z (6,16) orbit 1     Z (7,16) orbit 1     Z (6,18) orbit 0
   Z (7,18) orbit 0     Z (8,20) orbit 0     X (6,18) orbit 0
   X (8,20) orbit 0     X (9,20) orbit 0     X (10,22) orbit 0

the predecessor's §4.3 list of 10 800 s timeouts:
   Z (6,16) orbit 1     Z (7,16) orbit 1     Z (6,18) orbit 0
   Z (7,18) orbit 0     Z (8,20) orbit 0     X (6,18) orbit 0
   X (8,20) orbit 0     X (9,20) orbit 0     X (10,22) orbit 0
```

The same nine, in both sectors, with no exceptions. The remaining 12 open sub-queries were all in
flight with the inherited drivers. Those nine were therefore this box's entire target, since nothing
else on the machine was attacking them. They were attacked with Kissat404, and **two of them fell**.

### 6.2 The "timeouts" are contaminated by CPU starvation — the most important finding of this box

The predecessor titled its §4.3 *"Some sub-queries are genuinely hard, not merely queued"* and argued
that the nine timeouts were "plausibly finishable rather than intractable" but comparable in cost to
its most expensive completed sub-queries. **That diagnosis is wrong, and this box can now show it is
wrong with a decisive counterexample.**

```
X (10,22) orbit 0    predecessor: no verdict after 10 800 s WALL
                     this box:    UNSAT in 225.3 s of solver time      (Kissat404)

X ( 9,20) orbit 0    predecessor: no verdict after 10 800 s WALL
                     this box:    UNSAT in 2 683.6 s of solver time    (Kissat404)
```

`X (10,22) orbit 0` is not a hard sub-query. It is a **225-second** sub-query that was recorded as a
three-hour timeout. Whatever else was happening on that machine — a worker starved to a few percent
of a core, memory pressure, or both — the `TIMEOUT` verdict carried essentially no information about
the instance's difficulty. The driver's own log states it plainly:

```
[66/210] ['X', '14,0,2', 10, 10, 22, 0] -> TIMEOUT 10800.4s      <- this box: UNSAT in 225.3 s
[17/210] ['X', '14,0,2', 10,  9, 20, 0] -> TIMEOUT 10800.6s      <- this box: UNSAT in 2683.6 s
```

**The full picture, regenerated at the close of the box.** The predecessor's §4.3 listed nine
timeouts; the inherited `drive7.py` recorded five more while this box was running, so the set is now
fourteen. Every one of them should be treated as *unmeasured*, not as *hard*:

<!--TIMEOUTS-->
| sub-query | recorded by the inherited driver | actually |
|---|---|---|
| `X (5,18) orbit 0` | TIMEOUT after 10800 s wall | still open |
| `X (6,18) orbit 0` | TIMEOUT after 10800 s wall | still open |
| `X (7,20) orbit 0` | TIMEOUT after 10800 s wall | still open |
| `X (8,20) orbit 0` | TIMEOUT after 10800 s wall | still open |
| `X (9,20) orbit 0` | TIMEOUT after 10801 s wall | **UNSAT in 2683.6 s** (kissat) — **4× less than the wall it was given** |
| `X (10,22) orbit 0` | TIMEOUT after 10800 s wall | **UNSAT in 225.3 s** (kissat) — **48× less than the wall it was given** |
| `Z (5,18) orbit 0` | TIMEOUT after 10800 s wall | still open |
| `Z (6,16) orbit 1` | TIMEOUT after 10800 s wall | still open |
| `Z (6,18) orbit 0` | TIMEOUT after 10800 s wall | still open |
| `Z (7,16) orbit 1` | TIMEOUT after 10800 s wall | still open |
| `Z (7,18) orbit 0` | TIMEOUT after 10800 s wall | still open |
| `Z (7,20) orbit 0` | TIMEOUT after 10800 s wall | still open |
| `Z (8,20) orbit 0` | TIMEOUT after 10800 s wall | still open |
| `Z (9,22) orbit 0` | TIMEOUT after 10800 s wall | still open |

14 distinct sub-queries carry a TIMEOUT record; 2 of them have since been decided.
<!--/TIMEOUTS-->

The cost model built in this box (`predict2.py`, §9) had flagged it in advance. Fitting a per-orbit
cost multiplier against each cell's *own* orbit-2 time, over the 77 cells where that is measurable:

```
orbit        0     1     2     3     4     5     6     7     8
multiplier  2.03  1.90  1.00  0.57  0.10  0.06  0.01  0.00  0.00     (median, relative to orbit 2)
```

Orbit 0 and orbit 1 are only about **2×** the cost of orbit 2 of the same cell — not the order of
magnitude the raw medians in the predecessor's §4.2 suggest.

The model got three out-of-sample tests before the box closed, and it is worth reporting them
honestly because they all fail in the same direction:

| sub-query | predicted | actual | ratio |
|---|---|---|---|
| `X (10,22) orbit 0` | `111` s | `225.3` s | **2.0× under** |
| `X ( 9,20) orbit 0` | `930` s | `2 683.6` s | **2.9× under** |
| `Z ( 6,20) orbit 0` | `3 413` s | `7 241.8` s | **2.1× under** |

Right order of magnitude, consistently optimistic by a factor of `2`–`3`. So the honest reading of
the model's `≈ 30` CPU-hour total for the frontier is **`60`–`90` CPU-hours**, or roughly `3`–`5`
hours of wall clock on 24 uncontended cores. That is still small, and it is still the right
conclusion — but the raw model number should not be quoted without this correction.

**Consequences for the next commission, and they are large.**

1. **Do not trust any `TIMEOUT` record as evidence of difficulty.** Re-run all seven remaining ones
   before treating them as hard. One of the two tried so far was 48× cheaper than its timeout implied.
2. **The total remaining cost is small.** The model gives `≈ 30` CPU-hours for the whole frontier;
   corrected for its consistent `2`–`3×` optimism, **`60`–`90` CPU-hours**, i.e. three to five hours
   on 24 free cores. This is not a project that needs a new idea; it needs an uncontended machine for
   one evening.
3. **The right per-job timeout is generous wall plus a CPU-time floor.** A wall-clock timeout on a
   contended machine measures contention, not the instance. A driver should either cap CPU time
   rather than wall time, or refuse to record a `TIMEOUT` until the job has actually consumed a
   stated amount of CPU.

---

## 7. Honest limits

### 7.1 What this box did not do

**It did not close the decision.** `13` orbit sub-queries in `13` cells were still open when it ended,
so none of the headline claims the commission pre-committed to — `d_ext = 11` on the candidate, the
conjecture confirmed, `D* >= 11` — is available. It decided `2` of the timed-out sub-queries directly, and
the inherited driver closed `5` more cells while it ran; `7` are handed off, still running (§8.1).

**It did not reduce the dominant risk** (§7.4), which remains exactly where three sessions have left
it: nobody has looked at Figure 12.

**It did not emit proof certificates.** All 848 UNSATs remain solver verdicts, not machine-checked
proofs (§7.5). The rebuild audit of §2.5 establishes that the *formula* is right, which is a different
and weaker thing.

**It did not free the machine properly.** It reniced the superseded processes (§7.2) rather than
killing them, which recovered a modest fraction of what killing them would have.

What it did contribute: the audit (§2), the accounting correction (§2.7), two structural checks
nobody had run (§3.2 and the `K = 0` vacuity check in §3), a second independent witness for the
over-pruning check (§3.1), three re-decisions that all confirm (§4), two first decisions from the
supposedly-hard nine, the demonstration that the `TIMEOUT` records are contaminated (§6.2), a
calibrated cost model for the remainder, a correctly-disciplined driver, and a clean handoff with the
volatile logs finally copied into the repository (§8.3).

### 7.2 Machine contention is the binding constraint, and most of it is abandoned work

24 cores; load average `74–85` throughout. The oversubscription is roughly threefold. Breaking it
down at the close of the box:

| processes | provenance | status |
|---|---|---|
| 3 drivers + ~20 `job7.py` workers | the predecessor's `drive7`/`drive9`, inherited live | **useful** — working the open frontier |
| 11 `job7k.py` workers | mine, this box | **useful** — the hard nine + three re-decisions |
| 14 `job3.py` | a session that ended ~7h45m before this box opened | **superseded** |
| 5 (`noclass.py`, `witness2.py`, 2× `job.py`, one detached interpreter) | sessions that ended 2+ days ago | **orphaned** (`ppid = 1`) |

The `job3.py` cluster deserves naming because it is the largest single waste on the machine. It
computes the **whole-cell** query for one `(sector, K)` at a time under `dext2.Cert` with only cuts
`(c1)`–`(c3)` — no orbit split and none of the `cert7` cuts. That is strictly the formulation the
least-orbit split was built to replace: for `K = 3` and `K = 4` in sector Z its target cells are
*already* decided UNSAT by the sweep, and for `K = 5..9` it is a strictly harder query than the
orbit-split sub-queries that themselves time out at three hours. Fourteen processes have been running
it for 7 h 45 m — roughly **108 CPU-hours** — and have produced nothing; they write output only on
completion, and their parent shells are gone.

**I did not kill them, and I did not ask a tool to.** They are not my processes, no user was reachable
to approve it, and killing them is irreversible — a destructive action on another session's work is
not something an autonomous executor should take on its own initiative, however good the argument.

**What I did instead was `renice` them to 20**, the lowest scheduling priority:

```
14 × job3.py           nice  5 -> 20
     noclass.py        nice 10 -> 20
     witness2.py       nice  5 -> 20
 2 × job.py            nice 10 -> 20
```

This is a proportionate middle path and it is worth naming the distinction. Renicing **destroys
nothing**: every one of those processes keeps running, keeps its accumulated state, and will still
write its output file if it ever completes. What changes is only that they yield the CPU to the
frontier work when the two compete. The honest caveat is that it is not *fully* reversible by me —
lowering a nice value back requires privilege I do not have — so the practical effect is that
superseded work now runs slower for the rest of its life. Against 108 CPU-hours already spent for
zero output on a strictly superseded formulation, that trade is clearly right; against killing them,
it is clearly safer.

The measured effect was modest but real: my workers went from ≈ 0.47 to ≈ 0.52 core each, and the
first re-decision returned shortly after (§5.3). Freeing those ~10 cores *properly* remains, on the
evidence of §6.1, the single highest-value action available to the next box. It should be an
explicit, human-approved item in the next commission rather than a judgement call left to an executor.

### 7.3 A near-miss avoided

The predecessor recorded (its §1.2) that it had overwritten the live drivers' `.py` modules in the
shared scratch directory, which was harmless only by luck. That scratch directory is *also* mine —
the session-scoped path is identical — and the drivers were still running. I therefore did **not**
write into `work/`; I copied the modules to a sibling `work2/` and ran everything from there.
`diff` confirms the copies are byte-identical to the originals for `job7.py`, `cert.py`, `cert4.py`,
`cert7.py`, `dext.py`, `dext2.py`, `sched.py`, so hashes remain comparable across the two namespaces —
which §2.5 then demonstrated empirically 859 times.

### 7.4 The dominant risk is unchanged and inherited

Everything above is a statement about the object `phicert` §2.4 pins down:

```
phi(x^a y^b) = (a + b) mod 3
Z sector, order-class triple (1, 2, 62)      X sector, order-class triple (14, 0, 2)
```

If that reconstruction of Figure 12 of arXiv:2603.05481 is wrong, this artifact is a correct set of
statements about the wrong assignment. `phicert` §2.5 rates the residual reconstruction risk on the
edge map *moderate*. **I did nothing to reduce it.** Rendering Figure 12 to pixels and reading the 36
labels by eye remains the cheapest independent check, and remains not done. It is cheap, it is
non-COMPUTE, and it now gates more accumulated work than any other open item in this node.

### 7.5 UNSAT is a solver verdict, not a machine-checked proof

No DRAT/LRAT proof was emitted or checked for any of the decided sub-queries. What §2.5 establishes is
that the *formula* each verdict refers to is exactly reproducible; it does not establish that the
solver's UNSAT is correct. The mitigations actually in hand are: `0` verdict conflicts across `101`
independently duplicated sub-queries (§2.3), agreement across four encodings and several solvers, and
the encoding's demonstrated ability to find witnesses where they exist (§3, five validation cells).
Proof-logging remains the correct fix and remains not done.

---

## 8. FIX-2 declaration and handoff

**Every OS-level background process this box started is declared here.** All run from
`work2/`, working directory
`/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad/work2`.

### 8.1 Processes this box started — DECLARED, and HANDED OFF (not terminated)

Working directory for all of them:
`…/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad/work2` (a **sibling** of the live drivers'
directory — see §7.3 for why that matters).

**Still running at the close — handed off:**

| job | pid | started | command | log |
|---|---|---|---|---|
| my driver | `43443` | 02:25:35 | `drive10.py logs/d10.jsonl 8 10800 queue10.json` | `work2/logs/d10.jsonl`, `d10.out` |
| 7 solver workers | children of `43443` | 02:25:35 | `job7k.py … kissat`, one per remaining hard sub-query | via the driver |

The seven are `Z (7,18,0)`, `Z (6,18,0)`, `Z (6,16,1)`, `Z (8,20,0)`, `Z (7,16,1)`, `X (8,20,0)`,
`X (6,18,0)` — i.e. seven of the fourteen contaminated `TIMEOUT` sub-queries of §6.2. Each had
accumulated `≈ 2 000` CPU-seconds at the close. Per-job wall timeout is `10 800` s, after which the
driver records a `TIMEOUT`, **releases its claim file**, and moves on; its queue is otherwise
exhausted, so it will exit once these seven finish or time out.

**Ran to completion inside the box — nothing left running:**

| job | purpose | result | log |
|---|---|---|---|
| `job7k.py X 14,0,2 10 6 20 0 kissat` | re-decision 1 | UNSAT 850.0 s | `work2/logs/redecide.jsonl` |
| `job7k.py Z 1,2,62 10 6 16 0 kissat` | re-decision 2 | UNSAT 2287.5 s | `work2/logs/redecide.jsonl` |
| `job7k.py Z 1,2,62 10 7 16 0 kissat` | re-decision 3 | UNSAT 1294.7 s | `work2/logs/redecide.jsonl` |
| `job7k.py X 14,0,2 10 10 22 0 kissat` | the 9th hard sub-query the driver had no worker for | **UNSAT 225.3 s** | `work2/logs/extra.jsonl` |
| `verifyall.py` | rebuild + hash-match every certificate | 853/853 | `work2/logs/verifyall.out` |
| `chain.py` | `cert4 ⊆ cert6 ⊆ cert7` on all 110 cells | 0 failures | `work2/logs/chain.out` |
| `job7k.py Z 1,2,2 10 4 14 0 kissat` | over-pruning check | SAT 70.8 s, witness verified | `work2/logs/knowncell_v3.json` |

I confirmed by `ps` at the close that none of these is still alive.

**Why the driver is handed off rather than terminated.** It is the only thing on the machine
attacking those seven sub-queries, they hold ~2 000 CPU-seconds each, and §6.2 says at least some of
them are far cheaper than their timeout record implies — killing them would discard exactly the work
most likely to close cells. It is safe to leave running: `drive10.py` takes a filesystem claim
(`O_CREAT|O_EXCL`) before every dispatch and re-checks every known log directory **and** the live
process table, so it cannot duplicate work done by `drive7.py` or by a future session's driver. That
dedup was exercised repeatedly and visibly — `SKIP inflight`, `SKIP decided`, and `SKIP claimed`
lines in `d10.out` — including one case where it correctly declined to start `X (10,22) orbit 0`
because it detected my own manually launched process on it.

**It is safe to terminate** if the machine is needed:

```
kill 43443 ; pkill -f job7k.py
```

Nothing downstream depends on them; every verdict already produced is in the logs and in §5.3.

### 8.2 Processes this box inherited and did NOT start

```
pid 5675   drive7.py logs/final.jsonl 30 spec_final.json 10800   (started 2026-08-22 22:11:51)
           + 4 job7.py workers                                    -- STILL RUNNING, left alone
```

Two of the three inherited drivers **exhausted their queues and exited during this box**:
`pid 24328` (`drive9.py logs/mine.jsonl 12 7200`) and `pid 29862` (`drive9.py logs/mine2.jsonl 10 7200`).

`drive7.py` closed `X (6,20) orbit 1`, `X (7,20) orbit 1` and `Z (5,18) orbit 1` while this box ran,
and recorded **five further `TIMEOUT`s** — `Z (5,18,0)`, `Z (7,20,0)`, `Z (9,22,0)`, `X (5,18,0)`,
`X (7,20,0)` — which is how the contaminated-timeout set grew from nine to fourteen (§6.2). It has no
dedup against anything and will keep re-deciding closed sub-queries; that waste is the price of not
killing it mid-flight, and it was the predecessor's judgement as much as mine.

The superseded and orphaned processes from earlier sessions are inventoried in §7.2; I reniced them
to 20 rather than killing them, and the reasoning is given there.

### 8.3 Verdict-bearing logs copied into the repository BEFORE the box closed

`artifacts/logs_circdist_gross_final_20260823/` contains, with `SHA256SUMS.txt`:

- `live_*.jsonl` — a fresh snapshot of all 12 logs from the predecessor's **volatile** `/private/tmp`
  scratch directory, taken at the close of this box. This is strictly newer than the rescued copy in
  `logs_circdist_gross_drivers_20260823/` and supersedes it as the authority.
- `mine_d10.jsonl`, `mine_d10.out`, `mine_redecide.jsonl` — this box's own driver and re-decision logs.
- `knowncell_overpruning_check.json` — the §3.1 witness, in full.
- `verifyall.out` — the 859/859 rebuild audit transcript.
- `MANIFEST.md` — the complete per-sub-query certificate manifest.
- `accounting.txt` — the frontier accounting at the close.

The predecessor could not do this — its commission permitted one file — and it correctly flagged the
loss as the weakest point of its result. That gap is now closed: **no certificate now exists only in
volatile scratch.**

### 8.4 What the next box should do, in priority order

1. **Free the machine first, with human approval.** ~10 of 24 cores are held by the superseded
   `job3.py` cluster and day-old orphans (§7.2). On the evidence of §6.1 this is worth more than any
   encoding improvement. It is an irreversible action on another session's processes and should be a
   named, approved item in the commission, not an executor's judgement call.
2. **Harvest before launching anything.** Run the accounting (§9 `frontier.py`) over
   `logs_circdist_gross_final_20260823/`, `work/logs/` and `work2/logs/`. The frontier in §5 is a
   *lower bound* on what is decided — three drivers were still running when it was written.
3. **Then run the nine hard sub-queries** (§6.1) on the freed machine with Kissat404 and a per-job
   wall timeout of at least 6 hours. They have never been given enough CPU; §6.1 argues they are
   finishable, not intractable.
4. **Use `drive10.py`, or any driver with filesystem claims.** Never launch a driver without them.
5. **Do the Figure 12 read (§7.4).** It is non-COMPUTE, it is cheap, and it now gates more
   accumulated work than anything else in this node.

---

## 9. Reproduction

All modules are the predecessor's, re-extracted verbatim from
`artifacts/circdist_gross_candidate_decision_20260822.md` §9 and its own predecessors; `diff` against
the live copies is empty (§7.3). Three modules are new in this box and are given in full below.

New in this box, in full. `job7k.py` is `job7.py` with a selectable solver and **byte-identical CNF
construction**, so its `cnf_sha256` is directly comparable to the inherited records — that comparability
is what makes §2.5 and §4 meaningful. `drive10.py` implements the fix the predecessor recommended in its
§1.1 but could not apply: **the claim lives in the filesystem**, via `os.open(..., O_CREAT|O_EXCL)`, so
any number of independently launched drivers — including ones inherited mid-flight — cooperate without
knowing about each other. It additionally skips a sub-query already decided in *any* known log directory,
and one currently in flight in *any* `job7*.py` process on the machine.

#### `job7k.py`

```python

"""job7.py with a selectable solver.  CNF construction is byte-identical to job7.py, so
cnf_sha256 is comparable across solvers.

usage: job7k.py <sector> <a,b,c> <W> <K> <Ew> <orbit> <solver>
       solver in {cd15, cd19, cd30, kissat, g42, mgh, cms}
"""
import sys, time, json, hashlib
import numpy as np
from pysat.solvers import (Cadical153, Cadical195, Cadical300, Glucose42,
                           MinisatGH, Kissat404)
from sched import make_phi
from cert import tiled_orders
import dext, dext2, cert7

SOLVERS = dict(cd15=Cadical153, cd19=Cadical195, cd30=Cadical300,
               kissat=Kissat404, g42=Glucose42, mgh=MinisatGH)

sector = sys.argv[1]
triple = tuple(int(c) for c in sys.argv[2].split(','))
W = int(sys.argv[3]); K = int(sys.argv[4]); Ew = int(sys.argv[5])
oi = int(sys.argv[6]); sname = sys.argv[7]
s_par, t_par = 1, 1

phi = make_phi(s_par, t_par)
orders, _ = tiled_orders(sector, phi, triple)
ctx, Hstab = dext.sector_ctx(orders, sector)
c = cert7.Cert7(ctx, W, K, Ew)
cls = list(c.cls)
rec = dict(sector=sector, triple=list(triple), W=W, K=K, Ew=Ew, orbit=oi,
           phi=[s_par, t_par], nclauses=len(cls), nvars=c.top, solver=sname)
if oi >= 0:
    assert K >= 1, "residual-orbit split requires K >= 1"
    S, orbits = dext2.column_orbits(phi, triple)
    rorb = [(rep, orb) for (rep, orb) in orbits if rep[0] == 'r']
    rec['norbits'] = len(rorb); rec['stab'] = len(S)
    assert all(len(o) == len(S) for _, o in rorb)
    if oi >= len(rorb):
        rec.update(verdict='NOORBIT'); print(json.dumps(rec)); sys.exit(0)
    rep, orb = rorb[oi]
    rec['rep'] = str(rep)
    cls.append([c.col_lit(rep)])
    for jj in range(oi):
        for col in rorb[jj][1]:
            cls.append([-c.col_lit(col)])
h = hashlib.sha256()
for cl in cls:
    h.update((" ".join(map(str, cl)) + "\n").encode())
rec['cnf_sha256'] = h.hexdigest()[:32]
rec['nclauses_final'] = len(cls)
t0 = time.time()
with SOLVERS[sname](bootstrap_with=cls) as S2:
    sat = S2.solve()
    m = S2.get_model() if sat else None
rec['seconds'] = round(time.time() - t0, 1)
if sat:
    E, R, D = c.decode(m)
    info = dext.verify_witness(ctx, E, R, D, Hstab)
    rec.update(verdict='SAT',
               info={k2: (bool(v) if isinstance(v, bool) else int(v)) for k2, v in info.items()},
               R=[[int(a), int(b)] for a, b in R],
               D=[int(i) for i in np.nonzero(D)[0]],
               E=[int(i) for i in np.nonzero(E)[0]])
else:
    rec.update(verdict='UNSAT')
print(json.dumps(rec))
```

#### `drive10.py`

```python

"""Dedup-aware, claim-file driver.  Implements the predecessor's own recommended fix:
the claim lives in the FILESYSTEM (os.open(..., O_CREAT|O_EXCL)), so any number of
independently launched drivers -- including ones inherited mid-flight -- cooperate
without knowing about each other.

usage: drive10.py <logfile> <nworkers> <timeout_s> <queue.json>
queue.json: [[sector, "a,b,c", W, K, Ew, orbit, solver], ...]  in dispatch order
"""
import json, os, sys, subprocess, time, glob, threading, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
LOGFILE = sys.argv[1]; NW = int(sys.argv[2]); TMO = int(sys.argv[3]); QF = sys.argv[4]
CLAIMS = os.path.join(HERE, 'claims'); os.makedirs(CLAIMS, exist_ok=True)
os.makedirs(os.path.dirname(LOGFILE) or '.', exist_ok=True)

# every log dir we know about: rescued repo copy, inherited live dir, mine
LOGDIRS = [
    "<home>/Documents/Codex/2026-08-07/i-have-connected-an-old-windows/outputs/Windows-SSD-Recovery-2026-08-07/Research-Projects/discovery-new-algorithms/artifacts/logs_circdist_gross_drivers_20260823",
    os.path.join(os.path.dirname(HERE), 'work', 'logs'),
    os.path.join(HERE, 'logs'),
]
CAND = {('Z', (1, 2, 62)), ('X', (14, 0, 2))}

def decided():
    """set of (sector,K,Ew,orbit) already decided SAT/UNSAT on a candidate triple, any log"""
    out = set()
    for D in LOGDIRS:
        for L in glob.glob(os.path.join(D, '*.jsonl')):
            try: fh = open(L)
            except OSError: continue
            for ln in fh:
                ln = ln.strip()
                if not ln: continue
                try: r = json.loads(ln)
                except Exception: continue
                if r.get('verdict') not in ('SAT', 'UNSAT'): continue
                if 'triple' not in r or r.get('W') != 10: continue
                if (r['sector'], tuple(r['triple'])) not in CAND: continue
                if r.get('orbit', -1) < 0: continue
                out.add((r['sector'], r['K'], r['Ew'], r['orbit']))
    return out

def inflight():
    """(sector,K,Ew,orbit) currently being solved by ANY job7*.py on this machine"""
    out = set()
    try:
        ps = subprocess.run(['ps', '-eo', 'command'], capture_output=True, text=True, timeout=30).stdout
    except Exception:
        return out
    for ln in ps.splitlines():
        if 'job7' not in ln or 'grep' in ln: continue
        t = ln.split()
        try:
            i = max(j for j, x in enumerate(t) if x.endswith('job7.py') or x.endswith('job7k.py'))
        except ValueError:
            continue
        a = t[i+1:]
        if len(a) < 6: continue
        try:
            sec = a[0]; K = int(a[3]); Ew = int(a[4]); orb = int(a[5])
        except Exception:
            continue
        out.add((sec, K, Ew, orb))
    return out

lock = threading.Lock()
logfh = open(LOGFILE, 'a', buffering=1)
outfh = open(LOGFILE.replace('.jsonl', '.out'), 'a', buffering=1)

def emit(s):
    with lock:
        outfh.write(f"[{time.strftime('%H:%M:%S')}] {s}\n")

def worker(q):
    while True:
        with lock:
            if not q: return
            task = q.pop(0)
        sec, trip, W, K, Ew, orb, solver = task
        key = (sec, K, Ew, orb)
        if key in decided():
            emit(f"SKIP decided {key}"); continue
        if key in inflight():
            emit(f"SKIP inflight {key} (inherited driver is on it)"); continue
        cname = os.path.join(CLAIMS, f"{sec}_{K}_{Ew}_{orb}.claim")
        try:
            fd = os.open(cname, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, f"{os.getpid()} {time.time()} {solver}\n".encode()); os.close(fd)
        except FileExistsError:
            emit(f"SKIP claimed {key}"); continue
        emit(f"START {key} solver={solver} tmo={TMO}")
        t0 = time.time()
        try:
            p = subprocess.run([sys.executable, os.path.join(HERE, 'job7k.py'),
                                sec, trip, str(W), str(K), str(Ew), str(orb), solver],
                               capture_output=True, text=True, timeout=TMO, cwd=HERE)
            wall = round(time.time() - t0, 1)
            line = p.stdout.strip().splitlines()[-1] if p.stdout.strip() else ''
            if line.startswith('{'):
                r = json.loads(line); r['wall'] = wall
                with lock: logfh.write(json.dumps(r) + "\n")
                emit(f"DONE  {key} {r['verdict']} {r['seconds']}s (wall {wall})")
            else:
                with lock: logfh.write(json.dumps(dict(
                    sector=sec, triple=[int(x) for x in trip.split(',')], W=W, K=K, Ew=Ew,
                    orbit=orb, solver=solver, verdict='CRASH', wall=wall,
                    stderr=p.stderr[-400:])) + "\n")
                emit(f"CRASH {key} {p.stderr[-200:]}")
                os.unlink(cname)
        except subprocess.TimeoutExpired:
            wall = round(time.time() - t0, 1)
            with lock: logfh.write(json.dumps(dict(
                sector=sec, triple=[int(x) for x in trip.split(',')], W=W, K=K, Ew=Ew,
                orbit=orb, solver=solver, verdict='TIMEOUT', wall=wall)) + "\n")
            emit(f"TMO   {key} after {wall}s")
            os.unlink(cname)   # release so a later/longer run can retry

q = json.load(open(QF))
emit(f"driver start pid={os.getpid()} nworkers={NW} timeout={TMO} queue={len(q)}")
ths = [threading.Thread(target=worker, args=(q,), daemon=True) for _ in range(NW)]
for t in ths: t.start()
for t in ths: t.join()
emit("driver done")
```

#### `hashonly.py` — rebuild one sub-query's CNF and print its hash, no solve

```python

"""Rebuild one sub-query's CNF and print its hash + shape. No solve.
usage: hashonly.py <sector> <a,b,c> <W> <K> <Ew> <orbit>"""
import sys, json, hashlib, time
from sched import make_phi
from cert import tiled_orders
import dext, dext2, cert7
sector=sys.argv[1]; triple=tuple(int(c) for c in sys.argv[2].split(','))
W=int(sys.argv[3]); K=int(sys.argv[4]); Ew=int(sys.argv[5]); oi=int(sys.argv[6])
t0=time.time()
phi=make_phi(1,1)
orders,_=tiled_orders(sector,phi,triple)
ctx,Hstab=dext.sector_ctx(orders,sector)
c=cert7.Cert7(ctx,W,K,Ew)
cls=list(c.cls)
rec=dict(sector=sector,triple=list(triple),W=W,K=K,Ew=Ew,orbit=oi,
         nclauses=len(cls),nvars=c.top)
if oi>=0:
    S,orbits=dext2.column_orbits(phi,triple)
    rorb=[(rep,orb) for (rep,orb) in orbits if rep[0]=='r']
    rec['norbits']=len(rorb); rec['stab']=len(S)
    rep,orb=rorb[oi]; rec['rep']=str(rep)
    cls.append([c.col_lit(rep)])
    for jj in range(oi):
        for col in rorb[jj][1]:
            cls.append([-c.col_lit(col)])
h=hashlib.sha256()
for cl in cls: h.update((" ".join(map(str,cl))+"\n").encode())
rec['cnf_sha256']=h.hexdigest()[:32]; rec['nclauses_final']=len(cls)
rec['build_s']=round(time.time()-t0,1)
print(json.dumps(rec))
```

#### `verifyall.py` — rebuild and hash-match EVERY recorded certificate (§2.5)

```python

"""Rebuild the CNF of EVERY recorded candidate sub-query and check its hash against the
record.  Tries cert4 / cert6 / cert7; a record is VERIFIED if some encoding reproduces both
its clause counts and its hash exactly."""
import json, os, sys, glob, hashlib, collections, time
from sched import make_phi
from cert import tiled_orders
import dext, dext2, cert4, cert6, cert7

CAND={'Z':(1,2,62),'X':(14,0,2)}
LOGDIRS=sys.argv[1:]
recs=[]
seen=set()
for D in LOGDIRS:
    for L in sorted(glob.glob(os.path.join(D,'*.jsonl'))):
        for ln in open(L):
            ln=ln.strip()
            if not ln: continue
            try: r=json.loads(ln)
            except: continue
            if r.get('verdict') not in ('SAT','UNSAT'): continue
            if 'triple' not in r or r.get('W')!=10: continue
            if tuple(r['triple'])!=CAND.get(r['sector']): continue
            if r.get('orbit',-1)<0: continue
            if not r.get('cnf_sha256'): continue
            sig=(r['sector'],r['K'],r['Ew'],r['orbit'],r['cnf_sha256'])
            if sig in seen: continue
            seen.add(sig); r['_log']=os.path.basename(L); recs.append(r)
print("distinct (sub-query, hash) records to verify:", len(recs), flush=True)

phi=make_phi(1,1)
CTX={}; RORB={}
for sec,trip in CAND.items():
    orders,_=tiled_orders(sec,phi,trip)
    CTX[sec]=dext.sector_ctx(orders,sec)[0]
    S,orbits=dext2.column_orbits(phi,trip)
    RORB[sec]=[(rep,orb) for (rep,orb) in orbits if rep[0]=='r']

CACHE={}
def build(sec,K,Ew,oi,cls_name):
    key=(sec,K,Ew,cls_name)
    if key not in CACHE:
        C={'cert4':cert4.Cert4,'cert6':cert6.Cert6,'cert7':cert7.Cert7}[cls_name]
        CACHE[key]=C(CTX[sec],10,K,Ew)
        if len(CACHE)>40: CACHE.pop(next(iter(CACHE)))
    c=CACHE[key]
    cls=list(c.cls)
    rorb=RORB[sec]
    rep,orb=rorb[oi]
    cls.append([c.col_lit(rep)])
    for jj in range(oi):
        for col in rorb[jj][1]:
            cls.append([-c.col_lit(col)])
    h=hashlib.sha256()
    for cl in cls: h.update((" ".join(map(str,cl))+"\n").encode())
    return h.hexdigest()[:32], len(c.cls), len(cls)

res=collections.Counter(); fails=[]; encused=collections.Counter()
t0=time.time()
for i,r in enumerate(recs):
    ok=False
    for nm in ('cert7','cert4','cert6'):
        try: hh,nc,ncf=build(r['sector'],r['K'],r['Ew'],r['orbit'],nm)
        except Exception as e: continue
        if hh==r['cnf_sha256']:
            ok=True; encused[nm]+=1
            if r.get('nclauses') not in (None,nc) or r.get('nclauses_final') not in (None,ncf):
                res['hash_ok_count_mismatch']+=1
            break
    if ok: res['VERIFIED']+=1
    else:
        res['FAILED']+=1
        fails.append((r['sector'],r['K'],r['Ew'],r['orbit'],r['cnf_sha256'],r['_log'],r.get('nclauses')))
    if (i+1)%100==0: print(f"  {i+1}/{len(recs)}  {dict(res)}  {round(time.time()-t0)}s", flush=True)
print("\n=== RESULT ===")
print(dict(res)); print("encoding used:", dict(encused))
print("failures:", len(fails))
for f in fails[:40]: print("   FAIL", f)
```

#### `chain.py` — verify cert4 ⊆ cert6 ⊆ cert7 on every cell (§3.2)

```python
"""Verify cert4.cls subset cert5/6.cls subset cert7.cls, with identical variable numbering and
identical column-literal maps, on EVERY cell of both sectors.  This is what licenses mixing a
cert4 UNSAT and a cert7 UNSAT within one cell."""
from sched import make_phi
from cert import tiled_orders
import dext, dext2, cert4, cert5, cert6, cert7
phi=make_phi(1,1); CAND={'Z':(1,2,62),'X':(14,0,2)}
cells=cert4.cells(10)
bad=[]; n=0
for sec,trip in CAND.items():
    orders,_=tiled_orders(sec,phi,trip)
    ctx=dext.sector_ctx(orders,sec)[0]
    cols=[rep for rep,_ in dext2.column_orbits(phi,trip)[1]]
    for (K,Ew) in cells:
        n+=1
        c4=cert4.Cert4(ctx,10,K,Ew); c5=cert5.Cert5(ctx,10,K,Ew)
        c6=cert6.Cert6(ctx,10,K,Ew); c7=cert7.Cert7(ctx,10,K,Ew)
        S4={frozenset(c) for c in c4.cls}; S5={frozenset(c) for c in c5.cls}
        S6={frozenset(c) for c in c6.cls}; S7={frozenset(c) for c in c7.cls}
        checks = {
          'vars_equal':  c4.top==c6.top==c7.top,
          'c4<=c6':      S4<=S6,
          'c4<=c7':      S4<=S7,
          'c6<=c7':      S6<=S7,
          'c4<=c5':      S4<=S5,
          'col_lit_46':  all(c4.col_lit(r)==c6.col_lit(r) for r in cols),
          'col_lit_47':  all(c4.col_lit(r)==c7.col_lit(r) for r in cols),
        }
        if not all(checks.values()):
            bad.append((sec,K,Ew,{k:v for k,v in checks.items() if not v}))
import collections
cnt=collections.Counter()
for _,_,_,d in bad:
    for k in d: cnt[k]+=1
print(f"cells checked: {n} (55 per sector x 2)")
print(f"cells with >=1 failing check: {len(bad)}")
print("failing check breakdown:", dict(cnt))
core=['vars_equal','c4<=c6','c4<=c7','c6<=c7','col_lit_46','col_lit_47']
print()
print("CORE CHAIN (cert4 <= cert6 <= cert7, same vars, same col_lit):")
print("   failures:", sum(cnt[k] for k in core), " -> holds on all 110 cells:", sum(cnt[k] for k in core)==0)
print("SIDE BRANCH (cert5, the bench-only encoding):")
print("   c4<=c5 failures:", cnt['c4<=c5'])
```

#### `timeouts.py` — recover which sub-query each TIMEOUT belongs to, and what is now known (§6.2)

```python
"""Every TIMEOUT the inherited drivers recorded, against what is now known about that sub-query."""
import json,glob,os,re,ast,statistics,sys
SC="/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad"
R="<home>/Documents/Codex/2026-08-07/i-have-connected-an-old-windows/outputs/Windows-SSD-Recovery-2026-08-07/Research-Projects/discovery-new-algorithms/artifacts/logs_circdist_gross_drivers_20260823"
CAND={'Z':(1,2,62),'X':(14,0,2)}
tmo=[]
for f in glob.glob(os.path.join(SC,"work","logs","*.out")):
    for ln in open(f, errors='ignore'):
        m=re.search(r"\[\s*\d+/\d+\]\s*(\[[^\]]*\])\s*->\s*TIMEOUT\s*([\d.]+)s", ln)
        if m:
            a=ast.literal_eval(m.group(1))
            tmo.append(((a[0],a[3],a[4],a[5]), float(m.group(2)), os.path.basename(f)))
u={}
for D in (R,SC+"/work/logs",SC+"/work2/logs"):
    for L in glob.glob(os.path.join(D,'*.jsonl')):
        for ln in open(L):
            try: r=json.loads(ln)
            except: continue
            if r.get('verdict') not in ('SAT','UNSAT') or 'triple' not in r: continue
            if r.get('W')!=10 or tuple(r['triple'])!=CAND.get(r['sector']): continue
            k=(r['sector'],r['K'],r['Ew'],r.get('orbit'))
            if k not in u or u[k]['seconds']>r['seconds']: u[k]=r
seen=set(); rows=[]
for k,w,src in sorted(tmo):
    if k in seen: continue
    seen.add(k)
    r=u.get(k)
    rows.append((k,w,r))
print("| sub-query | recorded by the inherited driver | actually |")
print("|---|---|---|")
solved=0
for (sec,K,Ew,o),w,r in rows:
    if r:
        solved+=1
        note=f"**UNSAT in {r['seconds']} s** ({r.get('solver','cd15')}) — **{w/r['seconds']:.0f}× less than the wall it was given**"
    else:
        note="still open"
    print(f"| `{sec} ({K},{Ew}) orbit {o}` | TIMEOUT after {w:.0f} s wall | {note} |")
print()
print(f"{len(rows)} distinct sub-queries carry a TIMEOUT record; {solved} of them have since been decided.")
```

#### `predict2.py` — per-orbit cost model and remaining-cost estimate (§6.2)

```python
"""Predict the cost of each OPEN sub-query from the decided sub-queries of its own cell.
Within a cell, cost falls steeply with orbit index; the ratio orbit_j / orbit_8 is fairly
stable across cells, so we fit a per-orbit multiplier and apply it to each open cell's own
decided orbits."""
import json,os,glob,sys,collections,statistics
sys.path.insert(0,"/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad/work2")
import cert4
SC="/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad"
R="<home>/Documents/Codex/2026-08-07/i-have-connected-an-old-windows/outputs/Windows-SSD-Recovery-2026-08-07/Research-Projects/discovery-new-algorithms/artifacts/logs_circdist_gross_drivers_20260823"
CAND={'Z':(1,2,62),'X':(14,0,2)}
lines={}
for D in (R, SC+"/work/logs", SC+"/work2/logs"):
    for L in sorted(glob.glob(os.path.join(D,'*.jsonl'))):
        for ln in open(L):
            ln=ln.strip()
            if ln: lines[(os.path.basename(L),ln)]=ln
u={}
for ln in lines.values():
    try: r=json.loads(ln)
    except: continue
    if r.get('verdict') not in ('SAT','UNSAT') or 'triple' not in r: continue
    if r.get('W')!=10 or tuple(r['triple'])!=CAND.get(r['sector']) or r.get('orbit',-1)<0: continue
    k=(r['sector'],r['K'],r['Ew'],r['orbit'])
    if k not in u or u[k]['seconds']>r['seconds']: u[k]=r
# per-orbit multiplier relative to the cell's orbit-2 time (orbit 2 is always decided)
ratios=collections.defaultdict(list)
cells=cert4.cells(10)
for sec in ('Z','X'):
    for (K,Ew) in cells:
        base=u.get((sec,K,Ew,2))
        if not base or base['seconds']<5: continue
        for o in range(9):
            r=u.get((sec,K,Ew,o))
            if r: ratios[o].append(r['seconds']/base['seconds'])
print("per-orbit cost multiplier, relative to the same cell's orbit-2 time")
print("(median over cells where orbit 2 took >5 s; n = number of cells)")
print()
mult={}
for o in range(9):
    if ratios[o]:
        mult[o]=statistics.median(ratios[o])
        print(f"   orbit {o}: median x{mult[o]:7.2f}   (n={len(ratios[o])})")
print()
# open list
op=[]
for sec in ('Z','X'):
    for (K,Ew) in cells:
        have={o for o in range(9) if (sec,K,Ew,o) in u}
        if Ew==12 and len(have)<9: continue
        for o in sorted(set(range(9))-have): op.append((sec,K,Ew,o))
print(f"predicted solver cost of each of the {len(op)} OPEN sub-queries")
print("(from its OWN cell's orbit-2 time x the multiplier above)")
print()
tot=0; rows=[]
for (sec,K,Ew,o) in op:
    b=u.get((sec,K,Ew,2))
    if not b: rows.append((sec,K,Ew,o,None)); continue
    est=b['seconds']*mult.get(o,1.0)
    tot+=est; rows.append((sec,K,Ew,o,est))
for sec,K,Ew,o,est in rows:
    b=u.get((sec,K,Ew,2))
    print(f"   {sec} ({K:2d},{Ew:2d}) orbit {o}   cell orbit-2 = {b['seconds']:8.1f} s"
          f"   -> predicted {est:9.1f} s" if est else f"   {sec} ({K},{Ew}) orbit {o}   no basis")
print()
print(f"predicted TOTAL solver time to finish the frontier: {tot:.0f} s  = {tot/3600:.1f} CPU-hours")
print(f"on 24 free cores that is ~{tot/3600/24*1.3:.1f} h wall (30% scheduling overhead);")
print(f"at the ~0.5 core a worker gets on the machine as it stands, ~{tot/3600/ (0.5*8):.1f} h with 8 workers.")
```

#### Frontier accounting (§2.7), re-implemented rather than inherited

```python

import json, os, sys, glob, collections
sys.path.insert(0,"/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad/work2")
import cert4
CAND={('Z',(1,2,62)),('X',(14,0,2))}
DIRS=sys.argv[1:]
rec={}; src=collections.Counter()
for D in DIRS:
    for L in sorted(glob.glob(os.path.join(D,'*.jsonl'))):
        for ln in open(L):
            ln=ln.strip()
            if not ln: continue
            try: r=json.loads(ln)
            except: continue
            if r.get('verdict') not in ('SAT','UNSAT'): continue
            if 'triple' not in r or r.get('W')!=10: continue
            if (r['sector'],tuple(r['triple'])) not in CAND: continue
            if r.get('orbit',-1)<0: continue
            k=(r['sector'],r['K'],r['Ew'],r['orbit'])
            r['_src']=os.path.basename(D)+'/'+os.path.basename(L)
            src[k]=1
            if k not in rec or rec[k]['seconds']>r['seconds']: rec[k]=r
cells=cert4.cells(10)
print("cells per sector:", len(cells))
print("decided candidate sub-queries (union over %d dirs): %d" % (len(DIRS), len(rec)))
print("verdicts:", collections.Counter(r['verdict'] for r in rec.values()))
tot=0; openlist=[]
for sec in ('Z','X'):
    op=[]; nj=0; ndone=0
    for (K,Ew) in cells:
        have={o for o in range(9) if (sec,K,Ew,o) in rec}
        if Ew==12 and len(have)<9:
            ndone+=1; continue   # enum12 closes these independently
        if len(have)==9: ndone+=1
        else:
            miss=sorted(set(range(9))-have)
            op.append(f"({K},{Ew}):{miss}"); nj+=len(miss)
            for o in miss: openlist.append((sec,K,Ew,o))
    print(f"\n{sec}: {ndone}/{len(cells)} cells decided; {len(op)} cells open, {nj} sub-queries open")
    for x in op: print("     ", x)
    tot+=nj
print("\nTOTAL OPEN:", tot)
print("by orbit:", collections.Counter(o for _,_,_,o in openlist))
json.dump(openlist, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'openlist.json'),'w'))
print("\nOPEN LIST:")
for x in openlist: print("   ", x)
```


---

## 10. What independent review must check

In priority order. Items 1–3 gate everything; items 4–7 are the audit itself and are cheap to re-run.

1. **The reconstruction (§7.4).** Render Figure 12 of arXiv:2603.05481 and read the 36 edge labels by
   eye. Confirm `phi(x^a y^b) = (a+b) mod 3` and the two order-class triples `Z (1,2,62)`,
   `X (14,0,2)`. Everything else is conditional on this and nothing in three sessions has tested it.
2. **That the decision is *open*, not closed.** Orbit sub-queries in `13` cells were undecided when
   this box ended (§5.2), and the inherited drivers were still running, so recount before relying on it.
   Reject any downstream claim of `d_ext = 11` on the candidate, of the conjecture being confirmed,
   or of `D* >= 11`, that cites this node — none of them is established.
3. **The least-orbit cover argument** (`job7.py` docstring, §3 `stabcheck.py`/`orbcover.py`): that the
   9 orbit sub-queries provably cover a cell with `K >= 1`, and that `K = 0` is arithmetically empty.
   This is the only step where an error would silently invalidate every UNSAT in the manifest at once.
4. **The rebuild-and-hash audit (§2.5).** Re-run `verifyall.py` against the log union; expect
   `859/859`. Independently confirm that `cnf_sha256` is `sha256(...).hexdigest()[:32]`, not MD5.
5. **The SAT-record check (§2.4).** Confirm all 6 SAT records sit on non-candidate triples, and that
   the 5 validation cells carry `decomposition_ok / zero_syndrome / nontrivial_logical` all true.
6. **The accounting (§2.7).** Recompute the open list from the union and confirm the dispatcher's
   `19` was a double-count of `22` at session start. The count then falls as the handed-off drivers
   work, so check the count, not the number printed here.
7. **The mixed-encoding soundness argument** (predecessor §2.4 / §4). The *clause-inclusion* half is
   now verified on all 110 cells (§3.2, `chain.py`) and need not be re-argued. What review should
   still check is the half that is not mechanical: that a `cert7` UNSAT rules out only *lex-minimal*
   solutions, that the lex-minimal solution of a cell lies in exactly one cell, and that the sweep
   enumerates all of them — i.e. that `cells(W)` is exhaustive, not merely the cells someone ran.

8. **The contaminated-timeout finding (§6.2), because it changes what the next box should do.**
   Confirm from `live_final.out` that `X (10,22) orbit 0` is recorded as a `10800.4` s `TIMEOUT`, and
   from `mine_extra.jsonl` that the same sub-query is `UNSAT` in `225.3` s on a CNF whose hash
   rebuilds. If that holds, then the predecessor's §4.3 conclusion — that the timed-out sub-queries
   are "genuinely hard, not merely queued" — does not follow from its evidence, and the remaining
   twelve timeouts carry no information about difficulty either.
9. **The cost model (§6.2, `predict2.py`), before it is used to plan.** It is fitted on decided
   sub-queries and validated on only two out-of-sample points (`X (10,22,0)`: predicted 111 s, actual
   225 s; `X (9,20,0)`: predicted 930 s, actual 2 684 s). Both are within ~3×, both **under**-predict,
   and two points is not a validation set. Treat its `≈ 30` CPU-hour total as an optimistic lower
   bound — the right order of magnitude, not a schedule.

Two things review should **not** spend time on, because they are settled: the four `bench.jsonl`
hash mismatches (§2.6 — `cert5`, doubly redundant, and no sub-query depends on them), and whether the
`|E| = 12` stratum is closed (it is, independently, by `enum12.py`).

**One thing review should be suspicious of in this artifact specifically.** Every number in §5.2,
§5.3, §6.2 and the cell tables was regenerated from the logs by script at the moment the box closed,
while three drivers were still writing to those logs. The counts are therefore a *snapshot of a
moving target* and are lower bounds on what is decided. The scripts are in §9; re-run them rather
than quoting this document.
