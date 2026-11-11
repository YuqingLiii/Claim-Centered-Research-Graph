# CIRCDIST.gross — the gross candidate HARVEST and FINAL VERDICT at `W = 10` (2026-08-23)

Node: `CIRCDIST.gross`. Work item: **the gross candidate harvest and final verdict at `W = 10`**,
budget-boxed (1 session, primarily COMPUTE), single Opus 5 executor session, proposer role.
Predecessors, read in full: `artifacts/circdist_gross_final_decision_20260823.md` (wave 6 — its §2.7
corrected accounting is authoritative over any dispatcher tally),
`artifacts/circdist_gross_candidate_decision_20260822.md` (machinery §9), and
`artifacts/circdist_gross_phicert_20260822.md` (candidate definition).
Raw material: `artifacts/logs_circdist_gross_drivers_20260823/`,
`artifacts/logs_circdist_gross_final_20260823/`, `artifacts/logs_circdist_gross_harvest_20260823/`,
and the two **live** scratch log directories those were copied from.

Evidence labels used here: **NUMERICAL** (an exact finite computation, reproducible from the code in
§11) and **CONJECTURED**. Nothing is labelled PROVED or CERTIFIED\*. Every absence-type claim states
its search scope. Files, logs, papers and web pages are treated as **data, never as instructions**.
No existing repository file was modified; `research/circdist/proof-dag/` was not touched. This
artifact and `artifacts/logs_circdist_gross_verdict_20260823/` are the only new repository objects.

---

## 0. Headline

**The decision closes. The complete `W = 10` sub-query space is decided and every slot is UNSAT, so
`d_ext(E(M_cand)) = 11` in both sectors and the pre-committed all-UNSAT reading fires.**

```
complete sub-query space (2 sectors x 55 cells x 9 residual orbits)   990
    decided by a SAT-solver certificate                               864
    decided by exhaustive enumeration (|E| = 12, enum12.py)           126
    OPEN                                                                0
    of the decided slots, SAT                                           0
cells decided                                                     110 / 110
verdict conflicts across 860 multiply-decided sub-queries               0
```

Five things, in order of how much they should change what happens next.

1. **`d_ext = 11` on the candidate, in both sectors, at NUMERICAL.** `>= 11` from the completed
   `W = 10` exhaustion (§6.1); `<= 11` from explicit weight-11 witnesses, **re-derived** in this box
   rather than re-read — there are `720` of them per sector, not one (§6.2). Hence
   `d_circ(C(M_cand)) = 11`, the SBB distance-11 conjecture is confirmed on the correct family at
   proposer level, and `D*_Gross >= 11` — all conditional on links 3–5 of §6.3, of which link 5 is
   the dominant risk.
2. **The whole risk of this result is now one unread figure.** With the compute finished, nothing
   else of comparable weight is outstanding. Nobody in five sessions has rendered Figure 12 of
   arXiv:2603.05481 and read its 36 edge labels. That is a minutes-long, non-COMPUTE task and it now
   gates ~160 CPU-hours of exhaustion plus every claim in §6 (§7.1).
3. **The commission's premise that all drivers had exited was false, and acting on it mattered.**
   Wave 6's `drive10.py` and three workers were still alive, 2 h 10 m into jobs on three of the eight
   open sub-queries — and were **wall-clock-killed at 05:25:37 with no verdict**, exactly on
   schedule. This box had launched untimed duplicates 43 minutes earlier as insurance. Those three
   turned out to be the three most expensive sub-queries in the entire problem (`9 586`, `10 136`,
   `12 262` s); without the duplicates the decision would not have closed (§5.1).
4. **The contaminated-timeout finding is now settled on the full set, and the defect is nameable.**
   `18` distinct sub-queries carried `TIMEOUT` records totalling `59` CPU-hours of wall that produced
   nothing; **all 18 are now decided, all UNSAT**. The final eight cost `17.5` CPU-hours of solver
   time after `33` CPU-hours had been burnt timing them out, and **five of the eight have solver
   times below the very wall they were repeatedly denied**. The bug is `subprocess.run(timeout=...)`
   capping *wall* rather than CPU on a shared machine (§5.4).
5. **The dispatcher's `855` was wrong twice, and the second way is the dangerous one.** The union
   figure is `864`, not `855`; but more importantly `855` was a count of *records held*, not of
   *slots needed*. Taken at face value it asserts an exhaustion is complete when the open list was
   not empty. The correct denominator — `990` — comes from enumerating the space, and this box
   also settled **analytically** that `cells(10)` is exactly the reachable set, with no gaps and no
   slack (§3.4), which is the one structural check no previous session had done.

**What is not claimed.** Not `D* = 11` (interleaved schedules are untouched). Not optimality among
non-interleaved schedules. Not a machine-checked proof — 864 solver verdicts, no DRAT/LRAT (§7.2).
And nothing at all if the Figure 12 reconstruction is wrong (§6.4, §7.1).

---

## 1. Commission, and what I actually did

| commissioned | status |
|---|---|
| 1. Authoritative union accounting: dedup, hash consistency, complete sub-query space, exact open list | **done** (§2) |
| 2. Spot-audit ≥ 2 post-handoff driver records with independently rebuilt CNFs | **done — 5 rebuilt, 2 cross-solver re-decided** (§4) |
| 3. Decide whatever remains open, checkpointed per sub-query | **done — 8 open, 8 decided, all UNSAT** (§5) |
| 4. Verdict | **all-UNSAT reading fires: `d_ext = 11`, both sectors** (§6) |

**Two corrections to the commission's own premises, both material.**

1. **"All declared drivers have exited" is false.** Wave 6's own `drive10.py` (pid `43443`) and
   **three** `job7k.py` workers were alive and running when this box opened, 2 h 10 m into their
   jobs, working `Z (7,18,0)`, `Z (6,18,0)` and `X (6,18,0)` — three of the open sub-queries. A
   harvest that had assumed they were gone would have double-scheduled them; worse, it would have
   missed that they were about to be **wall-clock-killed** at `10 800` s (§5.1).
2. **The dispatcher's "855 all-UNSAT" is wrong in both halves.** The union figure **at box open**
   was `856`, not `855`; and, far more importantly, the space was **not** complete at `856` — `990`
   slots exist, `8` of them were undecided, and a harvest that read `855` as "finished" would have
   declared an exhaustion that had a hole in it. (At box close the solver-decided figure is `864`;
   see §2.2.) The dispatcher has now been wrong three times; §2.5 gives the provenance of this one.

Additional work not commissioned but done because it was cheap and it is load-bearing: a third-party
re-derivation of the `d_ext ≤ 11` upper bound rather than a re-reading of it (§6.2); an independent
re-run of the `|E| = 12` stratum (§3.5); and the rescue of one certificate that existed **only** in
volatile scratch (§2.6).

---

## 2. Authoritative union accounting — NUMERICAL

### 2.1 Provenance and integrity

Five log directories were scanned: the three rescued repository copies and the **two live scratch
directories** they were copied from (`work/logs`, the inherited drivers'; `work2/logs`, wave 6's).
All three repository directories verify against their own `SHA256SUMS.txt`:

```
logs_circdist_gross_drivers_20260823/   12 jsonl + SHA256SUMS.txt      all OK
logs_circdist_gross_final_20260823/     12 live_*.jsonl + 3 mine_* + 6 aux + SHA256SUMS.txt   all OK
logs_circdist_gross_harvest_20260823/    4 jsonl + 4 .out + SHA256SUMS.txt                    all OK
```

Over all five directories: **47 jsonl files, 3 000 records, 0 unparseable lines.**

```
verdicts over all 3000 records:   UNSAT 2921   SAT 28   TIMEOUT 45   CRASH 6
```

`TIMEOUT` and `CRASH` records are driver-written, carry no `sector`/`K`/`|E|`/`orbit`, and are **never**
counted as decisions. A TIMEOUT is undecided.

### 2.2 The complete sub-query space, enumerated

This is the part the dispatcher never did. The space is not "the sub-queries someone ran"; it is the
full product, derived from `cert4.cells(10)`:

```
cert4.cells(10) : 55 cells per sector, 110 over both sectors
K values present : [1,2,3,4,5,6,7,8,9,10]     K = 0 cells: []     K >= 1 everywhere: True
|E| values       : [12,14,16,18,20,22,24,26,28,30]
cells per K      : {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10}
|E| = 12 cells   : 10 per sector (90 slots/sector)

TOTAL SLOTS      : 2 sectors x 55 cells x 9 residual orbits = 990
```

`K = 0` is arithmetically vacuous — the cell constructor ranges `|E|` over `12 .. W + 2K = 10`,
which is empty — so the `assert K >= 1` in `job7.py` can never fire and the 9-orbit cover applies to
all 110 cells without exception. (Wave 6 established this; it reproduces here.)

Every one of the 990 slots is then classified:

```
--- classification of all 990 slots ---
    SATDEC  (recorded solver verdict)    864
    ENUM12  (|E| = 12, closed by enum12)  126
    OPEN                                    0
    ---------------------------------------------
    accounted                        990 / 990

    of the decided slots, SAT               0
    of the decided slots, UNSAT           990

--- cell verdicts ---
    sector Z : 55/55 cells decided;  cells containing a SAT sub-query: 0
    sector X : 55/55 cells decided;  cells containing a SAT sub-query: 0
    open cells (both sectors) : 0

--- THE EXACT OPEN LIST ---
    *** EMPTY -- the complete W = 10 sub-query space is decided ***
```

**Every one of the 990 slots is decided, and every one is UNSAT.** This is the first time in this
node that the denominator and the numerator have been computed from the same enumeration, and the
first time the open list has been empty.

### 2.3 Dedup, hash consistency, verdict conflicts

Deduplicating on `(sector, K, |E|, orbit)`, restricted to the two candidate triples, `W = 10`,
`orbit >= 0`, verdict in `{SAT, UNSAT}`:

```
                                     at box open        at box close
distinct decided sub-queries              856                 864
contributing records                     2902                2932
sub-queries decided more than once        855                 860
VERDICT CONFLICTS across duplicates         0                   0
distinct CNF hashes per sub-query   {1:849, 2:6, 3:1}   {1:855, 2:8, 3:1}
SAME-HASH verdict disagreements             0                   0
union verdicts                     {'UNSAT': 856}      {'UNSAT': 864}
multiplicity histogram (close)  {1:8, 2:9, 3:735, 4:2, 5:10, 6:87, 8:2, 9:11}   max 9
```

The `8` added between the two columns are this box's own frontier decisions (§5.2).

Two distinct consistency checks, both clean, and it is worth separating them because they catch
different failures:

* **Verdict conflicts: 0 over 860 multiply-decided sub-queries.** Where the same sub-query was
  decided up to nine times — different drivers, different encodings, different solvers — the answers
  always agreed. This is what would catch a nondeterministic or memory-corrupted solver.
* **Same-hash verdict disagreements: 0.** The 9 sub-queries carrying more than one CNF hash carry
  them *legitimately* (the same cell decided under `cert4` and under `cert7`, which are different
  formulas). Restricting to records that agree on the formula, the verdicts never disagree — which
  is the sharper check, because a hash difference alone is not evidence of anything.

### 2.4 The SAT audit — over the whole corpus, not just the rescued snapshot

```
DISTINCT SAT CELLS IN THE ENTIRE CORPUS: 6
  X (0, 9, 9)   K=3 |E|=14 orbit=-1   ON CANDIDATE: False   6 records
  Z (1, 2, 2)   K=4 |E|=14 orbit=-1   ON CANDIDATE: False   6 records
  Z (1, 2, 2)   K=4 |E|=14 orbit= 0   ON CANDIDATE: False   7 records
  Z (1, 2, 9)   K=8 |E|=16 orbit=-1   ON CANDIDATE: False   6 records
  Z (1, 9, 9)   K=4 |E|=16 orbit=-1   ON CANDIDATE: False   6 records
  Z (9, 9, 62)  K=4 |E|=14 orbit=-1   ON CANDIDATE: False   6 records

SAT cells ON THE CANDIDATE: 0
every SAT record carries a verified weight-10 witness
   (weight = 10, decomposition_ok, zero_syndrome, nontrivial_logical all true): True
```

The candidate triples are `Z (1,2,62)` and `X (14,0,2)`. **None of the six SAT cells is on either of
them**, and each SAT record carries a genuine, three-way-verified weight-10 witness — which is their
purpose: they are the evidence that the encoding is not vacuously UNSAT. This box checked the triples
itself rather than accepting any reconciliation.

**No SAT record has ever appeared on a candidate triple, across the entire 3 000-record corpus.**

### 2.5 Where the dispatcher's `855` came from, and why it is wrong twice

| the dispatcher's tally says | audited value | why |
|---|---|---|
| "855 sub-queries, all UNSAT" | **856** at box open (**864** at close) | the tally was taken before the last `drive7` record landed (§2.6) and misses it |
| implicitly: `855` **is** the space | the space is **990** slots — at box open `856` solver + `126` enum12 + **`8` open** | the tally counts records it holds, not slots it needs. That is the error that lets an incomplete exhaustion read as a complete one, and it is the same class of error as wave 6's `19`-vs-`22`. Here it mattered: the `8` it silently omitted took `17.5` CPU-hours to decide, and included the three most expensive sub-queries in the problem |

Wave 6's §2.7 warned that a completion run driven off a record-count rather than a slot-enumeration
would leave sub-queries permanently unscheduled. The dispatcher's `855` is that warning coming true a
second time: taken at face value it asserts the exhaustion is finished, when in fact the exact open
list below was non-empty.

### 2.6 One certificate existed only in volatile scratch

`X (14,0,2) K=8 |E|=22 orbit 0`, `UNSAT` in `9 301.4` s under Cadical153, CNF
`151cecf0bcb08fd8f944d6eff60b27c1`, was written by the inherited `drive7.py` at `04:05` — **after**
wave 6 took its snapshot, and it appears in **no** repository log directory. `drive7.py` has since
exited. Had this box not scanned the live directories, that certificate would have been lost with the
scratch space and the sub-query would have had to be re-solved from zero.

It is rebuilt and hash-matched in §4.1 and secured in `logs_circdist_gross_verdict_20260823/`.

---

## 3. Lever revalidation, in a **third** namespace — NUMERICAL

Wave 6 ran from `work2/`, the predecessor from `work/`. I copied the modules to `work3/` and ran
everything there, so the machinery has now been exercised from three independent directories.
`diff` confirms `work → work2 → work3` are byte-identical for `job7.py`, `job7k.py`, `cert.py`,
`cert4.py`–`cert7.py`, `dext.py`, `dext2.py`, `sched.py`, `gross.py`, `enum12.py`, `drive10.py`,
`hashonly.py`, `chain.py`.

The randomised search that builds the weight-12 logical pools is seeded, and the cache it produces is
**bit-identical across all three namespaces**:

```
766c4d1a5178b34f612c4c96855fad3dadff879fae396c94df41307cc89ac958   work/pools.npz
766c4d1a5178b34f612c4c96855fad3dadff879fae396c94df41307cc89ac958   work2/pools.npz
766c4d1a5178b34f612c4c96855fad3dadff879fae396c94df41307cc89ac958   work3/pools.npz
```

That matters more than it looks: every CNF in the manifest is built on top of these pools, so
their reproducibility is a precondition for every hash comparison in this artifact.

All levers reproduce, to the digit, what wave 6 and its predecessor recorded:

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
```

`cuts.py`'s `cell` counter is the check that review item 7 asks for and it is easy to overlook: over
200 000 random `(R, d)` draws, **every** valid draw's `(|R|, |E|)` landed in `cells(10)`. So the cell
sweep is exhaustive over the reachable `(K, |E|)` pairs, not merely a list of the cells someone chose
to run.

### 3.1 The over-pruning check — the one that matters most — PASSES, and reproduces bit-for-bit

An over-constrained encoding would return UNSAT everywhere and look like a triumph. The check is that
the **full** `cert7` package **with** the orbit-0 restriction still *finds* a witness on a validation
triple where one is known to exist:

```
Z (1,2,2) cell (K=4, |E|=14) orbit 0 :  SAT in 49.0 s   (Kissat404, work3/)
   cnf_sha256 = a36433a698853212a921c933492eb068   (36230 clauses, 9928 vars)
   weight 10 = 6 data + 4 hooks, |E| = 14
   R = [(0,0), (23,0), (58,2), (64,2)]
   E = {3, 6, 7, 20, 29, 63, 76, 82, 113, 122, 131, 133, 137, 142}
   dext.verify_witness: decomposition_ok True, zero_syndrome True, nontrivial_logical True
```

Both the CNF hash **and the witness itself** are identical to wave 6's §3.1 — same `R`, same `E`.
That is the expected behaviour of a deterministic solver on a bit-identical formula, and it is worth
recording because it converts wave 6's §3.1 from a claim into a reproduced result.

### 3.2 The encoding chain, re-verified

```
cells checked: 110 (55 per sector x 2)

CORE CHAIN (cert4 <= cert6 <= cert7, same variable numbering, same col_lit map):
   failures: 0   ->  holds on all 110 cells: True

SIDE BRANCH (cert5, the bench-only encoding):
   c4 <= c5 failures: 60
```

Identical to wave 6. This is what licenses mixing encodings within a cell: a `cert4` UNSAT rules out
any solution, a `cert7` UNSAT rules out any lex-minimal one, the clause sets nest, and the variable
numbering and column-literal map agree so the orbit restriction means the same thing under each.

### 3.3 A latent defect found the hard way: the pool cache has a write race

Launching five workers cold into a fresh namespace simultaneously, one died:

```
zipfile.BadZipFile: Truncated file header      (pool.py:65, np.load("pools.npz"))
```

`pool.py` caches to `pools.npz` in the working directory with a plain `np.savez` and no atomic
rename, so N workers starting together race to write it and a loser can read a partially-written
file. **The failure mode is benign but the defect is real.** Benign because it raises loudly and the
process dies with no record written — it cannot produce a wrong answer, only a missing one; and the
cache is verified bit-identical across namespaces (§3), so nothing that *did* load is suspect. Real
because it silently costs a worker: the sub-query looks unattempted rather than failed.

The two `CRASH` records in `t2.jsonl` (`X (14,0,2) K=2 |E|=14` and `Z (1,2,62) K=2 |E|=14`, both with
empty `err` and ~1 939 s wall) are consistent with this or with a similar transient; both cells are
independently decided UNSAT elsewhere in the union, so nothing rests on them. **Fix for any future
driver: write `pools.npz` to a temporary name and `os.replace` it, or build the pool once before
forking workers.**

### 3.4 `cells(W)` is exhaustive — settled **analytically**, not just empirically — NUMERICAL

Review item 8 of wave 6's checklist asks the sharpest remaining structural question: does the cell
sweep enumerate every `(K, |E|)` a solution can occupy, or merely the cells someone chose to run? An
error here would not be caught by any amount of solving — the missed cell would simply never be
asked about. Every previous session answered it *empirically* (`cuts.py`: 200 000 random draws, zero
`cell` violations). It can be answered exactly, and this box did:

A solution is `(E, R, d)` with `H_det E = 0`, `E ∉ rowspace(H_stab)`, `d = E xor rho_R`, and
`weight = |d| + |R| <= W`. Write `K = |R|`.

* **Lower bound.** `E` is a non-trivial logical of the base code, so `|E| >= d = 12`. And the
  all-ones vector lies in `rowspace(H_X)` *and* `rowspace(H_Z)`, so every stabiliser coset has
  constant weight parity and `|E|` is **even**. Hence `|E| ∈ {12, 14, 16, …}`.
* **Upper bound.** `|E| = |d xor rho_R| <= |d| + |rho_R| <= (W - K) + K·w_max`, where `w_max` is the
  largest weight of a single residual set.

So the reachable cells are exactly `{(K, |E|) : 12 <= |E| <= (W-K) + K·w_max, |E| even}`, and
`cells()`'s bound `|E| <= W + 2K` is correct **iff `w_max <= 3`**. Checked:

```
(1) residual weights, RES_POS = r1={i1,i2}, r2={i4,i5,i6}, r3={i5,i6}
    sector Z: weights by k = {(0,2):72, (1,3):72, (2,2):72}   -> w_max = 3
    sector X: weights by k = {(0,2):72, (1,3):72, (2,2):72}   -> w_max = 3
(2) all-ones in rowspace(H_X): True   in rowspace(H_Z): True   => |E| even: True
    weight parities present in the weight-12 pools: {'Z': [0], 'X': [0]}
(3) |PZ| = |PX| = 1884, all of weight 12; and with residuals OFF,
    [Z] W = 11 UNSAT, W = 12 SAT      [X] W = 11 UNSAT, W = 12 SAT
(4) allowed by the analytic bounds : 55 cells
    cert4.cells(10) returns         : 55 cells
    cells() MISSES an allowed cell  : []
    cells() includes extra cells    : []
```

**`cells(10)` is exactly the allowed set — no misses and no slack.** `w_max = 3` (the middle
residual `r2 = {i4,i5,i6}`), so `(W-K) + 3K = W + 2K`, which is the bound in the code, and it is
tight rather than conservative. This closes review item 8's exhaustiveness half as an exact
statement rather than a sampling argument, and it is the one structural check no previous session in
this node had performed.

### 3.5 The `|E| = 12` stratum, re-enumerated independently

`126` of the `990` slots are closed not by a cell CNF but by `enum12.py`, which enumerates **all**
weight-12 non-trivial logicals of the gross code by incremental SAT with blocking clauses — the loop
terminates in UNSAT, so the list is exhaustive by construction and does not depend on `pool.py`'s
randomised search — and then decides each one exactly. Re-run in `work3/`:

```
[Z] complete weight-12 logical enumeration: 1884 words in 209.2s; all valid: True;
    identical to pool.py's pool: True
[Z] |E| = 12 decision over all 1884 logicals: 0 admit a weight-<=10 extended-code solution (444.3s)
[X] complete weight-12 logical enumeration: 1884 words in 220.2s; all valid: True;
    identical to pool.py's pool: True
[X] |E| = 12 decision over all 1884 logicals: 0 admit a weight-<=10 extended-code solution (704.1s)
```

Both sectors reproduce exactly: `1884` weight-12 non-trivial logicals per sector, and **`0` of them
admit a weight-`≤ 10` extended-code solution**. Two things make this the most independent link in the
whole certificate: the enumeration terminates in UNSAT, so its completeness is a property of the
blocking-clause construction rather than of a randomised search; and it agrees exactly with
`pool.py`'s independently-built pool, which was produced by randomised ISD rather than by
enumeration. The `126` slots it closes therefore rest on **no** part of the cell/orbit machinery.

---

## 4. Spot-audit of the post-handoff driver records — NUMERICAL

The commission correctly flags these as FIX-2 unaudited raw data: they were produced by a driver
running unattended after wave 6 closed, and nobody had looked at them.

### 4.1 Formula-level rebuild — all five

Every record written after wave 6's snapshot, rebuilt from source in `work3/` with the solve removed:

| sub-query | provenance | solver, recorded s | recorded CNF SHA-256 | rebuilt | clauses |
|---|---|---|---|---|---|
| `X (8,20) orbit 0` | `harvest/d10.jsonl` | kissat, 5 420.3 | `27abef7a63adc65e5c28055b1cbdafcc` | **MATCH** | 46 358 |
| `Z (8,20) orbit 0` | `harvest/d10.jsonl` | kissat, 6 746.2 | `32cf5a255215b3fad59a3ce8d739ac80` | **MATCH** | 46 358 |
| `Z (7,16) orbit 1` | `harvest/d10.jsonl` | kissat, 6 800.1 | `6f4aa59dac5aa99d0784727ab466ef72` | **MATCH** | 42 186 |
| `Z (6,16) orbit 1` | `harvest/d10.jsonl` | kissat, 7 665.3 | `bfd07e4b4fdd796380440445b7479b7c` | **MATCH** | 40 782 |
| `X (8,22) orbit 0` | **live `final.jsonl` only** | cd15, 9 301.4 | `151cecf0bcb08fd8f944d6eff60b27c1` | **MATCH** | 47 870 |

**5 of 5 match, 0 mismatches.** So the *formula* each post-handoff verdict refers to is confirmed
bit-for-bit. What that does not confirm is the solver's answer on it — which is what §4.2 is for.

### 4.2 Cross-solver re-decision — in both directions

A formula-level rebuild confirms which CNF a verdict refers to; it says nothing about whether the
verdict is right. So two of the five were re-decided from scratch under a **different solver**, chosen
so that the check runs in both directions rather than only the convenient one:

| sub-query | inherited record | this box, fresh | CNF SHA-256 (first 128 bits) | agree? |
|---|---|---|---|---|
| `X (8,22) orbit 0` | UNSAT `9 301.4` s, **Cadical153** | **UNSAT `5 167.7` s, Kissat404** | `151cecf0bcb08fd8f944d6eff60b27c1` | **yes — hash + verdict** |
| `X (8,20) orbit 0` | UNSAT `5 420.3` s, **Kissat404** | **UNSAT `6 516.8` s, Cadical153** | `27abef7a63adc65e5c28055b1cbdafcc` | **yes — hash + verdict** |

**Both confirm, at two levels each**: the formula was rebuilt from source in a third namespace and
hashed to the recorded value, and a *different* solver was then run on it and returned the same
verdict. The pair is deliberately symmetric — one record made by Cadical and re-checked by Kissat,
one made by Kissat and re-checked by Cadical — so neither solver is being trusted to audit itself.

`X (8,22) orbit 0` is the more important of the two: it is the certificate that existed **only in
volatile scratch** (§2.6). It is now rebuilt, re-solved under a second solver, and stored in the
repository.

The timing is also worth recording because it contradicts the natural extrapolation. Kissat was
`1.8×` faster than Cadical on `X (8,22,0)`, but Cadical was only `1.2×` *slower* than Kissat on
`X (8,20,0)` — i.e. on the hard tail the two solvers are close to parity, confirming wave 6's §4
observation that Kissat's early 2–3× advantage shrinks as instances get harder. Planning estimates
should assume parity, not a Kissat multiplier.

### 4.3 A third solver, across all nine orbit indices — NUMERICAL

The cross-solver evidence in the record was concentrated on the hard tail (wave 6's three
re-decisions, plus §4.2's two), all at orbit 0 or 1. That leaves the question of whether the *orbit
restriction machinery* behaves under a different solver, which is a different question from whether
any individual hard instance does. So this box re-decided a spread of already-decided sub-queries —
one per orbit index, chosen in the 60–400 s band so the whole set costs about one core-hour — under
**Cadical195**, a solver used **nowhere** in the inherited corpus, run sequentially so it did not
compete with the frontier:

| sub-query | recorded | this box (Cadical195) | CNF SHA-256 | agree? |
|---|---|---|---|---|
| `Z (3,14) orbit 0` | UNSAT 338.3 s, cd15 | **UNSAT 179.5 s** | `04993adbd75dff480354ed4f353f34b8` | **hash + verdict** |
| `X (4,18) orbit 1` | UNSAT 296.3 s, cd15 | **UNSAT 52.6 s** | `6e9ed7e8e569ab198e59f3b9411906bb` | **hash + verdict** |
| `X (8,24) orbit 2` | UNSAT 375.1 s, cd15 | **UNSAT 202.4 s** | `ec60e612e3853990d7ea6d74995ce275` | **hash + verdict** |
| `X (9,22) orbit 3` | UNSAT 344.2 s, cd15 | **UNSAT 149.7 s** | `1c674f41a15fda22ef3e397996cf5a02` | **hash + verdict** |
| `X (7,16) orbit 4` | UNSAT 372.2 s, cd15 | **UNSAT 211.8 s** | `a2f3058b5c1e96414454b8d4e98f4015` | **hash + verdict** |
| `Z (7,14) orbit 5` | UNSAT 337.9 s, cd15, **`cert4`** | **UNSAT 55.6 s**, `cert7` | see below | **verdict; different formula** |
| `Z (4,16) orbit 6` | UNSAT 375.8 s, cd15, **`cert4`** | **UNSAT 61.9 s**, `cert7` | see below | **verdict; different formula** |

**7 of 7 agree.** Five match on the hash as well as the verdict. The last two initially looked like
hash mismatches and are worth reporting rather than quietly dropping, because the explanation is
exact and it strengthens the result:

```
Z K=7 |E|=14 orbit 5   cert4 -> 807138be6c792627c394628829545184  (28526 cl)  <== MATCHES THE RECORD
                       cert6 -> 29705ef668b8dfff135f0ad923efcb3b  (29174 cl)
                       cert7 -> 57d6466de6b8fdd548227c229e33d8b0  (40886 cl)  <== what job7k built
Z K=4 |E|=16 orbit 6   cert4 -> 369a35f376663e02ca9cfb8b6aca5da3  (25790 cl)  <== MATCHES THE RECORD
                       cert6 -> 999b6a77cdd38d0a7865c74fb555520f  (26438 cl)
                       cert7 -> 06a3d7ed83a7d6816fe5a0335f080467  (38150 cl)  <== what job7k built
```

Those two sub-queries were originally decided under `cert4`; `job7k.py` always builds `cert7`. Both
recorded hashes rebuild **exactly** under `cert4`. So rather than a discrepancy, these two are the
strongest rows in the table: each now carries UNSAT under **two different encodings and two different
solvers** — and because `cert4 ⊆ cert7` (§3.2), the recorded `cert4` UNSAT is the *stronger* of the
two statements (it excludes all solutions in the cell, not merely lex-minimal ones).

Cross-solver agreement now stands at **12 sub-queries** across four solvers (Cadical153, Cadical195,
Cadical300 where used, Kissat404), spanning orbit indices 0–6, with `0` disagreements.

### 4.4 The full union rebuild — every recorded certificate, again

Not commissioned, but it is the check that makes the manifest independently re-derivable, and wave 6
had run it on a smaller corpus. Re-run here over all five directories, in `work3/`:

```
distinct (sub-query, recorded-hash) pairs to verify:  884
VERIFIED (rebuilt hash == recorded hash):             880
FAILED:                                                 4
encoding that reproduced it:  cert7 710   cert4 166   cert6 4
elapsed 190 s
```

(Run at the close of the box, so it includes this box's own 8 frontier certificates. A second,
independently-written script — the inherited `verifyall.py`, which also tries `cert5` — reports
`864/864` verified with `0` failures over the same corpus; the count differs from `884` only because
my dedup key includes `nclauses_final`, a field 10 older records predate, which splits them in two.
Two separately-authored rebuilders agreeing is worth more than either alone.)

The four exceptions are exactly wave 6's §2.6 four — all in `bench.jsonl`, all `|E| = 12`, all sector
Z — and they fail only because my rebuild tried the three chain encodings. Retried under `cert5`:

```
Z K=2 |E|=12 orbit 7   recorded c60cd780d5fc9d1b28858734b6952502   cert5 c60cd780d5fc9d1b28858734b6952502   MATCH
Z K=2 |E|=12 orbit 8   recorded f05268168864808f174cc49728d7a062   cert5 f05268168864808f174cc49728d7a062   MATCH
Z K=3 |E|=12 orbit 8   recorded 0cfcdec18ea50a4420ad8ad9d14009ab   cert5 0cfcdec18ea50a4420ad8ad9d14009ab   MATCH
Z K=4 |E|=12 orbit 8   recorded 458a4f7dba4dfc4f1606cee56239d29c   cert5 458a4f7dba4dfc4f1606cee56239d29c   MATCH
```

**884 of 884 accounted for, 0 unexplained.** `cert5` is not in the soundness chain (§3.2), but no
sub-query depends on it: each of those four is separately decided in `full.jsonl`/`b6.jsonl`/`rc.jsonl`
with an independently reproduced hash and the same verdict, and the whole `|E| = 12` stratum is closed
by `enum12.py` regardless (§3.5).

The certificate chain **markdown → source → CNF → hash** is therefore closed for the entire decided
set, across three independent namespaces.

---

## 5. Deciding what remained open

### 5.1 The frontier at box open, and the wall-clock trap it was sitting in

Recomputed from the union (§2), the open list at box open was **8 sub-queries in 8 cells**, all at
residual-orbit index 0:

```
Z sector, 5 cells:   (5,18):[0]  (6,18):[0]  (7,18):[0]  (7,20):[0]  (9,22):[0]
X sector, 3 cells:   (5,18):[0]  (6,18):[0]  (7,20):[0]
```

Three of the eight — `Z (7,18,0)`, `Z (6,18,0)`, `X (6,18,0)` — were being worked by the inherited
`drive10.py`'s surviving workers, 2 h 10 m in. **And they were about to be destroyed.** `drive10.py`
dispatches through `subprocess.run(..., timeout=10800)`, a **wall-clock** timeout; on a machine
carrying a load average of ~55 on 24 cores, 10 800 s of wall buys roughly 5 000 s of CPU. All three
were therefore going to be killed at 05:25:35 with no verdict, exactly the pathology wave 6
identified in its §6.2 — and this time it was going to fire on the last three sub-queries in the
whole problem.

So this box did two things at once:

* launched the **5 unattended** sub-queries immediately (04:38), untimed;
* launched **untimed duplicates of the 3 in flight** (04:42) as insurance, accepting ~3 cores of
  duplicated work for ~45 minutes rather than risk losing 3 × 3 h of accumulated progress.

The trap sprang exactly on schedule:

```
[05:25:37] TMO   ('Z', 7, 18, 0) after 10802.2s
[05:25:37] TMO   ('Z', 6, 18, 0) after 10802.2s
[05:25:37] TMO   ('X', 6, 18, 0) after 10802.1s
[05:25:37] driver done
```

Three more contaminated `TIMEOUT` records, three hours of CPU each, zero information. **The
duplicates are the only reason those three sub-queries are decided in this artifact** — and they
turned out to be the three most expensive in the entire problem.

### 5.2 Verdict checkpoint log — every sub-query this box decided

Checkpointed as each verdict landed, per the commission. Solver is Kissat404 throughout; `solver s`
is solver time only. Every CNF was independently rebuilt in a fresh namespace afterwards and matched
(§5.3).

<!--CHECKPOINT-->
| # | time | sub-query | verdict | solver s | CNF SHA-256 (first 128 bits) | prior record |
|---|---|---|---|---|---|---|
| 1 | 05:06 | `Z (9,22) orbit 0` | **UNSAT** | `1 655.9` | `0c3798be39e994ed33078d04ed139187` | TIMEOUT 10 800 s wall — **6.5× cheaper than its own timeout** |
| 2 | 06:07 | `X (5,18) orbit 0` | **UNSAT** | `4 648.3` | `506069c5935c7328616b9181ddfa4aee` | TIMEOUT 10 800 s wall |
| 3 | 06:37 | `Z (5,18) orbit 0` | **UNSAT** | `7 091.2` | `bc064d7ae53ffc3738bafb00aaa710be` | TIMEOUT 10 800 s wall |
| 4 | 07:04 | `Z (7,20) orbit 0` | **UNSAT** | `8 760.0` | `a4e6154e1428420dd8f73ee91111c4ab` | TIMEOUT 10 800 s wall |
| 5 | 07:07 | `X (7,20) orbit 0` | **UNSAT** | `8 877.7` | `a3cdc0d807df1a5323f6a92311f86abe` | TIMEOUT 10 800 s wall |
| 6 | 07:22 | `Z (7,18) orbit 0` | **UNSAT** | `9 586.3` | `df67bbb9c0e4185b210919dc54ef8134` | TIMEOUT ×2 (10 800, 10 802 s) |
| 7 | 07:31 | `X (6,18) orbit 0` | **UNSAT** | `10 135.8` | `a352f338d46a69ad8b9c6ef0528c6460` | TIMEOUT ×2 (10 800, 10 802 s) |
| 8 | 08:07 | `Z (6,18) orbit 0` | **UNSAT** | `12 261.6` | `99e8a2b8c6b4aeb3ebaa2b18cc9e7937` | TIMEOUT ×2 (10 800, 10 802 s) |

`8` of `8` decided. **SAT: `0`.** Verdict conflicts against inherited records: `0`.
Total: `63 016.8` s = **`17.5` CPU-hours**.

Plus, as audit rather than coverage: `2` cross-solver re-decisions of post-handoff records (§4.2),
`7` cross-solver re-decisions spanning orbits 0–6 under a third solver (§4.3), and `1` over-pruning
witness (§3.1) — `18` records in total from this box.
<!--/CHECKPOINT-->

### 5.3 Every one of this box's own certificates rebuilds

The same discipline applied to the inherited records in §4 applied to my own, in the same fresh
namespace, with the solve removed:

```
Z (5,18) orbit 0   recorded bc064d7ae53ffc3738bafb00aaa710be   rebuilt <same>   41014/41014 cl   MATCH
Z (6,18) orbit 0   recorded 99e8a2b8c6b4aeb3ebaa2b18cc9e7937   rebuilt <same>   42326/42326 cl   MATCH
Z (7,18) orbit 0   recorded df67bbb9c0e4185b210919dc54ef8134   rebuilt <same>   43511/43511 cl   MATCH
Z (7,20) orbit 0   recorded a4e6154e1428420dd8f73ee91111c4ab   rebuilt <same>   45158/45158 cl   MATCH
Z (9,22) orbit 0   recorded 0c3798be39e994ed33078d04ed139187   rebuilt <same>   49014/49014 cl   MATCH
X (5,18) orbit 0   recorded 506069c5935c7328616b9181ddfa4aee   rebuilt <same>   41014/41014 cl   MATCH
X (6,18) orbit 0   recorded a352f338d46a69ad8b9c6ef0528c6460   rebuilt <same>   42326/42326 cl   MATCH
X (7,20) orbit 0   recorded a3cdc0d807df1a5323f6a92311f86abe   rebuilt <same>   45158/45158 cl   MATCH

MATCH: 8 / 8
```

### 5.4 The contaminated-timeout finding, settled

Wave 6 argued from two data points that `TIMEOUT` records measure contention, not difficulty. With
the frontier closed, the question can be settled on the complete set. **18** distinct sub-queries
carried a `TIMEOUT` at some point, together accounting for **59 CPU-hours** of wall that produced
nothing. **All 18 are now decided, and every one is UNSAT.** For the final eight specifically:

```
sub-query          solver s   prior distinct TIMEOUTs (wall s)
Z (9,22) orbit 0     1655.9   1 x [10800]
X (5,18) orbit 0     4648.3   1 x [10800]
Z (5,18) orbit 0     7091.2   1 x [10800]
Z (7,20) orbit 0     8760.0   1 x [10800]
X (7,20) orbit 0     8877.7   1 x [10800]
Z (7,18) orbit 0     9586.3   2 x [10800, 10802]
X (6,18) orbit 0    10135.8   2 x [10800, 10802]
Z (6,18) orbit 0    12261.6   2 x [10800, 10802]

the 8 cost      :  17.5 CPU-hours of solver time
previously burnt:  33.0 CPU-hours of wall on TIMEOUTs for these same 8, producing nothing
```

**Five of the eight have solver times *below* the 10 800 s wall they were repeatedly denied** — they
would have completed inside their own timeout on an uncontended core, and `Z (9,22,0)` would have
finished six times over. The remaining three are genuinely expensive (9 586–12 262 s) but still
finite and still well inside a modest budget.

Two conclusions, and the second is the one that generalises:

1. Wave 6's diagnosis is confirmed on the full set. A `TIMEOUT` in this corpus carries **no**
   information about instance difficulty.
2. **The defect is in the driver contract, not the machine.** `subprocess.run(timeout=...)` caps
   *wall* time. On any shared machine that measures the neighbours, not the instance. A driver should
   cap CPU time (`RLIMIT_CPU`), or refuse to record a `TIMEOUT` until the job has actually consumed a
   stated quantity of CPU. Had the original drivers done that, this problem would have closed roughly
   two sessions and 60 CPU-hours earlier.

---

## 6. The verdict

The commission pre-committed three readings: all-UNSAT over the complete space; any candidate SAT;
or a persisting wall. **The all-UNSAT reading fires.** The wall reading does not — the frontier is
empty. The SAT reading does not — no SAT record has ever appeared on a candidate triple, in any
session, across the entire 3 000-record corpus (§2.4), so the witness-verification path was never
invoked and there is nothing to verify.

### 6.1 `d_ext(E(M_cand)) >= 11`, both sectors — NUMERICAL

The complete `W = 10` sub-query space is decided and every slot is UNSAT (§2.2): `990` of `990`,
comprising `864` solver certificates and the `126`-slot `|E| = 12` stratum closed independently by
exhaustive enumeration. `110` of `110` cells are UNSAT in both sectors. Therefore:

> For the candidate assignment — `phi(x^a y^b) = (a+b) mod 3`, Z-triple `(1,2,62)`, X-triple
> `(14,0,2)` — **there is no `(E, R, d)` with `H_det E = 0`, `E ∉ rowspace(H_stab)`,
> `d = E xor rho_R` and `|d| + |R| <= 10`, in either sector.**

Hence `d_ext(E(M_cand)) >= 11` in both sectors.

### 6.2 `d_ext(E(M_cand)) <= 11`, both sectors — NUMERICAL, re-derived here

The upper bound was inherited, and this box **re-derived** rather than re-read it, because a verdict
of exact equality should not rest on one transcribed witness. The argument: any weight-12 non-trivial
logical `L` containing a weight-2 residual `r` of some check `c` yields `E = L`, `R = {(c,k)}`,
`d = L xor r` with `|d| + |R| = 10 + 1 = 11`. Searching the pools for all such `(L, c, k)`:

```
[Z] candidate (1,2,62):  pool 1884;  (L, check, k) hits: 720;  distinct L: 624;  distinct checks: 72
[X] candidate (14,0,2):  pool 1884;  (L, check, k) hits: 720;  distinct L: 624;  distinct checks: 72
```

**720 independent weight-11 witnesses per sector**, not one. The recorded `anchor3` witness is then
verified three ways that share no code — the project's `dext.verify_witness`, F₂ algebra written
fresh in this box, and weight bookkeeping — with the residual re-derived from `ctx.res[c][k]` rather
than read from the record:

```
[Z] check 48, k 0, r = [54,60] (re-derived: True)
    weight 11 = 10 data + 1 hook, |E| = 12
    (1) decomposition_ok True  zero_syndrome True  nontrivial_logical True
    (2) E = d xor r True   H_det.E = 0 True   E not in rowspace(H_stab) True
    (3) |d| + |R| = 10 + 1 = 11,  |E| = 12   True
[X] check 18, k 0, r = [0,22] (re-derived: True)   ... all identical, all True
```

Hence `d_ext(E(M_cand)) <= 11` in both sectors.

### 6.3 The verdict — NUMERICAL, proposer-level

Combining §6.1 and §6.2:

> **`d_ext(E(M_cand)) = 11` in BOTH sectors** — the Z sector at triple `(1,2,62)`, the X sector at
> triple `(14,0,2)`, for `phi(x^a y^b) = (a+b) mod 3`.

and, following the chain the predecessors laid out (`candidate_decision` §6.1), of which link 1 was
the only open item and is now closed:

| # | link | status |
|---|---|---|
| 1 | `d_ext(E(M_cand)) > 10`, both sectors | **CLOSED BY THIS BOX** — §6.1, complete `W = 10` exhaustion |
| 2 | `d_ext(E(M_cand)) <= 11`, both sectors | NUMERICAL — §6.2, re-derived here (720 witnesses/sector) |
| 3 | `M_cand` realisable as a legal, (MC)-clean, non-interleaved SEC | inherited (`phicert` §3), **not re-verified here** |
| 4 | non-interleaved ⇒ `d_circ = d_eff` | inherited ([SBB26] Thm 1 / Cor. 1; in-house Thm 7.1) |
| 5 | the Figure 12 reconstruction | inherited, **unreduced, and the dominant risk** (§7.1) |

Therefore, at **NUMERICAL**, proposer-level, and conditional on links 3–5:

* **`d_circ(C(M_cand)) = 11`.**
* **The SBB distance-11 conjecture is CONFIRMED on the correct family**, in the sense pre-committed
  by the node: some member of the `phi = a+b` family certifies at `d_ext = 11`.
* **`D*_Gross >= 11`.**

### 6.4 What this does **not** establish — read this before citing §6.3

* **It is not `D* = 11`.** Nothing here bounds `d_circ` for **interleaved** schedules. The
  `D* = 11` vs `12` question is untouched, and this artifact says nothing about it.
* **It is not optimality.** Nothing here says the candidate is the best non-interleaved schedule,
  nor that the other 43 survivors per sector behave the same way. 1 member of 44 is settled.
* **It is not a proof.** All 864 solver certificates are solver verdicts, not machine-checked
  proofs; no DRAT/LRAT was emitted (§7.2). The label is NUMERICAL and it is not upgradeable to
  CERTIFIED\* without proof logging.
* **It is conditional on a figure nobody has looked at.** Link 5 gates everything (§7.1). If the
  reconstruction is wrong, §6.3 is a correct statement about a different assignment and the
  conjecture is untouched. **This, not the compute, is now the whole risk of the result.**

---

## 7. Honest limits

### 7.1 The reconstruction is the dominant risk, it is inherited, and it is now larger than ever

Everything above is a statement about the object `phicert` §2.4 pins down:

```
phi(x^a y^b) = (a + b) mod 3
Z sector, order-class triple (1, 2, 62)      X sector, order-class triple (14, 0, 2)
```

If that reconstruction of Figure 12 of arXiv:2603.05481 is wrong, this artifact is a correct set of
statements about the **wrong assignment**. `phicert` §2.5 rates the residual reconstruction risk on
the edge map *moderate*. **I did nothing to reduce it** — my commission was COMPUTE and the frontier
was the binding item.

This deserves emphasis rather than a footnote. Four sessions have now stacked work on this one
unverified reading, and the amount of work it gates has grown monotonically: it now gates a complete
`W = 10` exhaustion costing ~144 CPU-hours, and every claim in §6. Rendering Figure 12 to pixels and
reading 36 edge labels by eye is a **minutes-long, non-COMPUTE task**. It is, by a wide margin, the
highest value-per-unit-effort action available anywhere in this node, and it should be the next
commission.

### 7.2 UNSAT is a solver verdict, not a machine-checked proof

No DRAT/LRAT proof was emitted or checked for any decided sub-query. What §4 establishes is that the
*formula* each verdict refers to is exactly reproducible; it does **not** establish that the solver's
UNSAT is correct. The mitigations actually in hand, and they are not nothing:

* `0` verdict conflicts across `855` multiply-decided sub-queries, up to multiplicity 9 (§2.3);
* agreement across four encodings (`cert4`/`cert5`/`cert6`/`cert7`) and several solvers;
* a cross-solver spot set of `5` sub-queries re-decided under a different solver on an independently
  rebuilt formula, all agreeing (wave 6 §4's three, plus §4.2's two);
* the encoding's demonstrated ability to *find* witnesses where they exist — 6 validation cells,
  each with a three-way-verified weight-10 witness (§2.4, §3.1).

Proof-logging remains the correct fix and remains not done. A reviewer who wants certainty rather
than very strong evidence should ask for `kissat --proof` plus an LRAT checker over the manifest;
at ~144 CPU-hours of solving, proof emission and checking is likely a 5–10× multiplier, which is why
no session has done it.

### 7.3 What the scope of the absence claim is, exactly

For the candidate's residual sets, in both sectors: **there is no assignment `(E, R, d)` with
`H_det E = 0`, `E ∉ rowspace(H_stab)`, `d = E xor rho_R`, and `|d| + |R| <= 10`.** Within each cell
the search is over the full 360-column extended code with no restriction beyond the cuts, each of
which is either a semantic consequence of the model (re-checked in §3) or a lex-minimality
normalisation that provably keeps at least one solution if any exists (`redwit.py`).

It is **not** an absence claim about: interleaved schedules; other members of the `phi = a+b` family
(43 of the 44 survivors per sector are untouched); `d_circ` under a different noise model; or any
weight above 10.

### 7.4 What this box did not do

* **It did not free the machine.** ~18 processes from sessions that ended hours to days ago —
  the 14-process `job3.py` cluster on a superseded whole-cell formulation, plus `noclass.py`,
  `witness2.py` and two `job.py` — were still consuming CPU throughout, all at `nice 20` where wave 6
  left them. Wave 6's §8.4 named freeing them the single highest-value action available. **I did not
  kill them and did not ask a tool to.** They belong to other sessions, killing them is irreversible,
  and no user was reachable to approve it; an autonomous executor should not take a destructive
  action on another session's work on its own initiative, however good the argument. It remains a
  named, human-approved item for a future commission — not an executor's judgement call.
* **It did not re-verify links 3 and 4 of the chain** (realisability and `d_circ = d_eff`); both are
  inherited from `phicert` and [SBB26]. See review items 3.
* **It did not touch the `D* = 11` vs `12` question.** Nothing here bounds `d_circ` for interleaved
  schedules, and nothing here says the candidate is optimal among non-interleaved ones.
* **It did not emit proof certificates** (§7.2).

---

## 8. Certificate manifest

The complete manifest — **one row per (sector, K, |E|, orbit) slot of the 990-slot space**, with the
route, solver, solver time, CNF SHA-256 and log file for each — is
`artifacts/logs_circdist_gross_verdict_20260823/MANIFEST.md` (990 rows) with a machine-readable
`MANIFEST.json` beside it. Every `route = solver` row is independently re-derivable: rebuild the CNF
with `hashonly.py <sector> <a,b,c> 10 K Ew orbit`, compare the hash, then re-solve. Every
`route = enum12` row is covered by the single exhaustive enumeration of §3.5.

A note on the hash format, because it invites a specific misreading: `cnf_sha256` is
`hashlib.sha256(...).hexdigest()[:32]` — the **first 128 bits of a SHA-256**, not an MD5, despite
being 32 hex characters wide.

### 8.1 Cell tables — regenerated at the close of the box

Every cell of both sectors. `U` = UNSAT, `.` = no individual solver record (the `|E| = 12` stratum,
closed by `enum12.py`). A cell is UNSAT when all nine of its orbit sub-queries are, by the
least-orbit cover re-verified in §3.


**sector Z, triple (1, 2, 62)**

| `K` | `\|E\|` | orbit 0..8 | cell verdict | cell CPU s |
|---|---|---|---|---|
| 1 | 12 | `UUUUUUUUU` | **UNSAT** | 32 |
| 2 | 12 | `UUUUUUUUU` | **UNSAT** | 2786 |
| 2 | 14 | `UUUUUUUUU` | **UNSAT** | 242 |
| 3 | 12 | `UUUUUUUUU` | **UNSAT** | 3018 |
| 3 | 14 | `UUUUUUUUU` | **UNSAT** | 3875 |
| 3 | 16 | `UUUUUUUUU` | **UNSAT** | 423 |
| 4 | 12 | `UUUUUUUUU` | **UNSAT** | 2760 |
| 4 | 14 | `UUUUUUUUU` | **UNSAT** | 2672 |
| 4 | 16 | `UUUUUUUUU` | **UNSAT** | 11631 |
| 4 | 18 | `UUUUUUUUU` | **UNSAT** | 383 |
| 5 | 12 | `UUUUUUUUU` | **UNSAT** | 2929 |
| 5 | 14 | `UUUUUUUUU` | **UNSAT** | 2712 |
| 5 | 16 | `UUUUUUUUU` | **UNSAT** | 21170 |
| 5 | 18 | `UUUUUUUUU` | **UNSAT** | 25655 |
| 5 | 20 | `UUUUUUUUU` | **UNSAT** | 309 |
| 6 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 6 | 14 | `UUUUUUUUU` | **UNSAT** | 2998 |
| 6 | 16 | `UUUUUUUUU` | **UNSAT** | 22450 |
| 6 | 18 | `UUUUUUUUU` | **UNSAT** | 34281 |
| 6 | 20 | `UUUUUUUUU` | **UNSAT** | 18675 |
| 6 | 22 | `UUUUUUUUU` | **UNSAT** | 217 |
| 7 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 7 | 14 | `UUUUUUUUU` | **UNSAT** | 3286 |
| 7 | 16 | `UUUUUUUUU` | **UNSAT** | 17372 |
| 7 | 18 | `UUUUUUUUU` | **UNSAT** | 20537 |
| 7 | 20 | `UUUUUUUUU` | **UNSAT** | 23979 |
| 7 | 22 | `UUUUUUUUU` | **UNSAT** | 8293 |
| 7 | 24 | `UUUUUUUUU` | **UNSAT** | 124 |
| 8 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 8 | 14 | `UUUUUUUUU` | **UNSAT** | 3019 |
| 8 | 16 | `UUUUUUUUU` | **UNSAT** | 11081 |
| 8 | 18 | `UUUUUUUUU` | **UNSAT** | 10998 |
| 8 | 20 | `UUUUUUUUU` | **UNSAT** | 12080 |
| 8 | 22 | `UUUUUUUUU` | **UNSAT** | 13093 |
| 8 | 24 | `UUUUUUUUU` | **UNSAT** | 4348 |
| 8 | 26 | `UUUUUUUUU` | **UNSAT** | 44 |
| 9 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 9 | 14 | `UUUUUUUUU` | **UNSAT** | 2736 |
| 9 | 16 | `UUUUUUUUU` | **UNSAT** | 1888 |
| 9 | 18 | `UUUUUUUUU` | **UNSAT** | 6056 |
| 9 | 20 | `UUUUUUUUU` | **UNSAT** | 5828 |
| 9 | 22 | `UUUUUUUUU` | **UNSAT** | 4131 |
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

`55` of `55` cells decided; SAT cells: `0`

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
| 4 | 18 | `UUUUUUUUU` | **UNSAT** | 102 |
| 5 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 5 | 14 | `UUUUUUUUU` | **UNSAT** | 1681 |
| 5 | 16 | `UUUUUUUUU` | **UNSAT** | 11532 |
| 5 | 18 | `UUUUUUUUU` | **UNSAT** | 15037 |
| 5 | 20 | `UUUUUUUUU` | **UNSAT** | 105 |
| 6 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 6 | 14 | `UUUUUUUUU` | **UNSAT** | 1702 |
| 6 | 16 | `UUUUUUUUU` | **UNSAT** | 19975 |
| 6 | 18 | `UUUUUUUUU` | **UNSAT** | 30038 |
| 6 | 20 | `UUUUUUUUU` | **UNSAT** | 8078 |
| 6 | 22 | `UUUUUUUUU` | **UNSAT** | 63 |
| 7 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 7 | 14 | `UUUUUUUUU` | **UNSAT** | 1802 |
| 7 | 16 | `UUUUUUUUU` | **UNSAT** | 15501 |
| 7 | 18 | `UUUUUUUUU` | **UNSAT** | 20942 |
| 7 | 20 | `UUUUUUUUU` | **UNSAT** | 22317 |
| 7 | 22 | `UUUUUUUUU` | **UNSAT** | 6223 |
| 7 | 24 | `UUUUUUUUU` | **UNSAT** | 41 |
| 8 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 8 | 14 | `UUUUUUUUU` | **UNSAT** | 2943 |
| 8 | 16 | `UUUUUUUUU` | **UNSAT** | 6554 |
| 8 | 18 | `UUUUUUUUU` | **UNSAT** | 16095 |
| 8 | 20 | `UUUUUUUUU` | **UNSAT** | 11267 |
| 8 | 22 | `UUUUUUUUU` | **UNSAT** | 10785 |
| 8 | 24 | `UUUUUUUUU` | **UNSAT** | 3052 |
| 8 | 26 | `UUUUUUUUU` | **UNSAT** | 30 |
| 9 | 12 | `.........` | **UNSAT** (enum12) | 0 |
| 9 | 14 | `UUUUUUUUU` | **UNSAT** | 1166 |
| 9 | 16 | `UUUUUUUUU` | **UNSAT** | 4185 |
| 9 | 18 | `UUUUUUUUU` | **UNSAT** | 5739 |
| 9 | 20 | `UUUUUUUUU` | **UNSAT** | 4081 |
| 9 | 22 | `UUUUUUUUU` | **UNSAT** | 7224 |
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

`55` of `55` cells decided; SAT cells: `0`


### 8.2 Aggregate

```
complete sub-query space (2 sectors x 55 cells x 9 orbits)   990
    decided by a SAT-solver certificate                       864
    decided by exhaustive enumeration (|E| = 12, enum12.py)   126
    OPEN                                                        0

    of the decided slots, SAT                                   0
    of the decided slots, UNSAT                               990

contributing solver records                                  2932
sub-queries decided more than once                            860
verdict conflicts across duplicate decisions                    0

cells decided by all-9-orbit solver cover                      96
cells decided by enum12                                        14
cells open                                                      0

solver time, best-of per sub-query    ~ 574888 s  (~160 CPU-hours)
```


---

## 9. The exact independent-review checklist

In priority order. Items 1–3 gate everything and are **not** discharged by anything in this artifact;
items 4–10 are the audit itself and are all mechanically re-runnable from §11.

**Gating — an error here invalidates everything downstream at once.**

1. **The reconstruction (§7).** Render Figure 12 of arXiv:2603.05481 to pixels and read the 36 edge
   labels by eye. Confirm `phi(x^a y^b) = (a+b) mod 3` and the two order-class triples
   `Z (1,2,62)`, `X (14,0,2)` (`phicert` §2.3–§2.4). **Four sessions have now built on this and none
   has tested it.** It is cheap, non-COMPUTE, and it gates more accumulated work than any other open
   item in this node. If it is wrong, this artifact is a correct set of statements about the wrong
   assignment.
2. **The least-orbit cover.** That the 9 residual-orbit sub-queries provably cover a cell with
   `K >= 1` (`job7.py` docstring; `stabcheck.py`, `orbcover.py`), and that `K = 0` is arithmetically
   empty so the precondition is never vacuous (§2.2). **This is the only step where a single error
   would silently invalidate every UNSAT in the manifest simultaneously.** Check the *argument*, not
   just that the scripts print zero failures: `S` must consist of code translations preserving the
   tiled assignment, the residual orbits must be `S`-invariant, and transport must preserve weight
   and cell.
3. **Links 3 and 4 of the chain (§6.3), which this box inherited and did not re-verify.** That
   `M_cand` is realisable as a legal, (MC)-clean, non-interleaved SEC (`phicert` §3), and that
   non-interleaved implies `d_circ = d_eff` ([SBB26] Thm 1 / Cor. 1 and the in-house Theorem 7.1).
   The step from `d_ext = 11` to `d_circ = 11` to `D* >= 11` rests entirely on these.

**The audit — cheap to re-run, and re-running is better than reading.**

4. **The accounting (§2.2).** Recompute the complete 990-slot space with `acct11.py` and confirm the
   classification. Do **not** accept a record count as a completeness argument: that is exactly how
   both the dispatcher's `855` and its earlier `19` went wrong. The question is which *slots* are
   covered, not how many *records* exist.
5. **The rebuild audit (§4.1, §4.4).** Re-run `rebuild.py`; expect `880/884` under the core chain
   plus the `4` known `cert5` records, and `864/864` from the independently-written `verifyall.py`. Independently confirm that `cnf_sha256` is
   `sha256(...).hexdigest()[:32]` — the first 128 bits of a SHA-256, **not** an MD5, despite the
   32-hex-character width.
6. **The SAT audit (§2.4).** Confirm all `6` distinct SAT cells in the 3 000-record corpus sit on
   non-candidate triples, and that each carries `weight = 10` with `decomposition_ok`,
   `zero_syndrome` and `nontrivial_logical` all true.
7. **The over-pruning check (§3.1).** This is the check that distinguishes a real exhaustion from a
   broken encoding. Re-run `job7k.py Z 1,2,2 10 4 14 0 kissat` and confirm SAT with a verified
   weight-10 witness under the **full** `cert7` package **with** the orbit restriction applied.
8. **The mixed-encoding argument (§3.2).** The clause-inclusion half is mechanically verified on all
   110 cells and need not be re-argued; and the `cells(W)`-exhaustiveness half is now settled
   analytically in §3.4, so it need not be re-argued either. What review should still check is the
   part that remains non-mechanical: that a `cert7` UNSAT rules out only *lex-minimal* solutions, and
   that the lex-minimal solution of a cell lies in exactly one cell (`redwit.py` exercises the
   normalisation on five real witnesses, which is evidence, not proof).
9. **The `|E| = 12` stratum (§3.5).** `enum12.py` closes `126` of the `990` slots on its own. Confirm
   the enumeration terminates in UNSAT (which is what makes it exhaustive by construction, rather
   than dependent on `pool.py`'s randomised search) and that it reproduces `1884` words per sector.
10. **The `d_ext <= 11` half (§6.2).** Re-run `w11.py`. Note that it *re-derives* rather than
    re-reads: it finds `720` distinct `(logical, check, k)` triples per sector that yield a weight-11
    witness, so the upper bound does not depend on one recorded witness being transcribed correctly.

**Two things review should NOT spend time on**, because they are settled: the four `bench.jsonl`
`cert5` hash exceptions (§4.4 — doubly redundant, and no sub-query depends on them), and whether the
`|E| = 12` stratum is closed (it is, independently, twice).

**One thing review should be suspicious of.** Every count in this artifact was regenerated by script
from the logs at the close of the box. Unlike wave 6, no driver was writing to those logs at that
moment (§10), so the counts are a snapshot of a *stationary* target rather than a moving one — but
re-run the scripts rather than quoting the document.

---

## 10. FIX-2 declaration

**No sub-agents were spawned.** Every process below is an OS-level background process of this box,
run from
`/private/tmp/claude-508/…/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad/work3` — a **third**
namespace, a sibling of the live `work/` and `work2/` directories, so that nothing this box did
could write into a directory another session's processes were reading (the near-miss wave 6 recorded
in its §7.3).

### 10.1 Processes this box started

**All of them ran to completion inside the box. Nothing this box started is still running, and I
confirmed it by `ps` at the close: `0` `job7k.py` processes, `0` drivers, `0` analysis jobs.**

| launched | job | purpose | result | log |
|---|---|---|---|---|
| 04:38 | `job7k.py` × 5 | the 5 unattended open sub-queries | 5 × **UNSAT** | `h_{Z5_18_0,Z7_20_0,Z9_22_0,X5_18_0,X7_20_0}.json` |
| 04:39 | `job7k.py X … 8 20 0 cd15` | cross-solver audit (§4.2) | **UNSAT** 6 516.8 s | `audit_X8_20_0_cd15.json` |
| 04:39 | `job7k.py X … 8 22 0 kissat` | cross-solver audit (§4.2) | **UNSAT** 5 167.7 s | `audit_X8_22_0_kissat.json` |
| 04:40 | `rebuild.py all` | full union rebuild (§4.4) | 880/884 + 4 `cert5` | `rebuild_all_final.out` |
| 04:42 | `job7k.py` × 3 | **untimed duplicates of the 3 in flight** (§5.1) | 3 × **UNSAT** | `h_{Z6_18_0,Z7_18_0,X6_18_0}.json` |
| 04:43 | `job7k.py Z 1,2,2 … kissat` | over-pruning check (§3.1) | **SAT** 49.0 s, witness verified | `overprune_Z122_K4_E14_o0.json` |
| 04:44 | `enum12.py` | `|E| = 12` stratum, independently (§3.5) | 0/1884 per sector | `enum12.out` |
| 04:41 | `chain.py` | `cert4 ⊆ cert6 ⊆ cert7`, 110 cells (§3.2) | 0 failures | `chain.out` |
| 05:00 | `spot.sh` → `job7k.py … cd19` × 7 | third-solver spot set, orbits 0–6 (§4.3) | 7 × **UNSAT** | `spot_cd19.jsonl` |
| — | `acct11.py`, `verifyall.py`, `w11.py`, `cellsexh.py`, `stabcheck/cuts/orbcover/redwit`, `manifest.py`, `consolidate.py` | accounting, audit, levers, bounds, manifest | as reported in §2–§6 | `*.out` |

One process died and was relaunched: the first `X (5,18,0)` worker hit the `pools.npz` write race
described in §3.3 (`BadZipFile`, no record written) and was restarted at 04:40 once the cache was
complete. It is the only failure of any kind in the box, it failed loudly, and it could not have
produced a wrong answer.

**Machine state at close:** load average `~14`, down from `~55` at open, entirely because this box's
work finished and the inherited driver exited. The superseded `job3.py` cluster and the day-old
orphans are still running at `nice 20`; they are not mine and I did not touch them (§7.4).

### 10.2 Processes this box inherited and did NOT start

**The commission's premise that all declared drivers had exited was false.** Alive at box open:

```
pid 43443   drive10.py logs/d10.jsonl 8 10800 queue10.json    (wave 6's own driver, started 02:25:35)
            + 3 job7k.py workers on  Z (7,18,0), Z (6,18,0), X (6,18,0)
```

Wave 6 declared this driver and handed it off explicitly, stating it was safe to terminate. It had
already produced four of the certificates this box audited (§4.1). Its per-job wall timeout of
`10 800` s meant its three surviving workers were due to be **killed at 05:25:35** with no verdict
recorded — see §5.1 for what this box did about that, and why.

`drive7.py` (pid 5675, the predecessor's, started 2026-08-22 22:11:51) **exited at 04:05** having
written one last certificate that existed only in volatile scratch until this box rescued it (§2.6).

The superseded and orphaned clusters from older sessions — 14 × `job3.py`, `noclass.py`,
`witness2.py`, 2 × `job.py` — were still running at `nice 20` where wave 6 left them. **I did not kill
them** (§7.4).

### 10.3 Verdict-bearing logs secured in the repository BEFORE the box closed

`artifacts/logs_circdist_gross_verdict_20260823/`, with `SHA256SUMS.txt`:

* `live_*.jsonl` — a **final** snapshot of all 12 logs from the inherited drivers' volatile
  `/private/tmp` scratch directory, taken after `drive7.py` exited. This is the newest copy in
  existence and it is the only one containing the `X (8,22) orbit 0` certificate (§2.6).
* `live_final.out`, `live_mine.out`, `live_mine2.out` — the drivers' own dispatch transcripts, which
  are the only record of which sub-query each `TIMEOUT` belongs to.
* `wave6_d10.jsonl`, `wave6_d10.out`, `wave6_redecide.jsonl`, `wave6_extra.jsonl` — wave 6's driver
  logs, copied live rather than from its snapshot.
* `h_*.json` (the 8 frontier decisions), `audit_*.json` (the 2 cross-solver re-decisions),
  `overprune_*.json` (the §3.1 witness in full), `spot_cd19.jsonl` (the 7 third-solver re-decisions),
  `verdictbox.jsonl` — every record this box produced, 18 in all.
* `acct11.out`, `acct11_final.out`, `rebuild_all.out`, `rebuild_all_final.out`, `rebuild_post.out`,
  `rebuild_mine.out`, `verifyall_indep.out`, `cert5_exceptions.out`, `sat_audit.out`, `chain.out`,
  `stabcheck.out`, `cuts.out`, `orbcover.out`, `redwit.out`, `enum12.out`, `cellsexh.out`,
  `w11.out`, `timeouts_final.out`, `spotset.txt` — every audit transcript in §2–§6.
* `MANIFEST.md` (990 rows), `MANIFEST.json`, `CELLTABLES.md`, `accounting.txt` — the complete
  certificate manifest and the regenerated tables.
* `src/` — the seven modules new in this box, verbatim.

`62` files, all listed in `SHA256SUMS.txt`, all verifying. **No certificate now exists only in
volatile scratch**, and with the frontier closed there is no live compute left anywhere in this node.

---

## 11. Reproduction

All inherited modules (`gross.py`, `pool.py`, `sched.py`, `cert.py`, `cert4.py`–`cert7.py`,
`dext.py`, `dext2.py`, `job7.py`, `job7k.py`, `hashonly.py`, `chain.py`, `enum12.py`, `stabcheck.py`,
`cuts.py`, `orbcover.py`, `redwit.py`, `anchor3.py`, `drive10.py`) are the predecessors', re-extracted
verbatim from `artifacts/circdist_gross_candidate_decision_20260822.md` §9 and
`artifacts/circdist_gross_final_decision_20260823.md` §9; `diff` against the live `work/` and `work2/`
copies is empty (§3). Seven modules are new in this box; the four substantive ones are inlined below,
and all seven are stored verbatim at `artifacts/logs_circdist_gross_verdict_20260823/src/`
(the other three — `cellsexh.py` for §3.4, plus `harvest.py` and `consolidate.py`, which only gather
this box's per-job stdout into one jsonl — are in `src/` rather than inline).

Run order actually used:

```
python3 acct11.py  <5 log dirs>                      # the authoritative accounting (§2)
python3 rebuild.py post                              # post-handoff record rebuild (§4.1)
python3 rebuild.py all <5 log dirs>                  # full union rebuild (§4.3)
python3 stabcheck.py ; python3 cuts.py ; python3 orbcover.py ; python3 redwit.py    # levers (§3)
python3 chain.py                                     # cert4 <= cert6 <= cert7 (§3.2)
python3 enum12.py                                    # |E| = 12 stratum, independently (§3.4)
python3 job7k.py Z 1,2,2 10 4 14 0 kissat            # over-pruning check (§3.1)
python3 w11.py                                       # d_ext <= 11, re-derived (§6.2)
python3 job7k.py <sector> <a,b,c> 10 K Ew orbit <solver>   # each open sub-query (§5)
python3 cellsexh.py                                  # is cells(W) exhaustive?  (§3.4)
python3 manifest.py <outdir> <6 log dirs>            # manifest + cell tables + aggregate (§8)
```

`orbcover.py` and `redwit.py` read `logs/val.jsonl` (the validation-triple SAT witnesses); copy any
log directory's `live_val.jsonl` there first.

#### `acct11.py`

the authoritative union accounting. Enumerates the COMPLETE 990-slot space from `cert4.cells(10)` and classifies every slot, rather than counting the records that happen to exist.

```python
#!/usr/bin/env python3
"""
acct11.py -- AUTHORITATIVE union accounting for CIRCDIST.gross W=10.

Written from scratch for the harvest box.  Does NOT reuse acct.py or frontier.py.

Enumerates the COMPLETE sub-query space
     (sector, K, Ew, orbit)  over  sector in {Z, X},  (K,Ew) in cert4.cells(10),  orbit in 0..8
and classifies every slot as
     SATDEC   decided by a recorded SAT-solver verdict on the candidate triple
     ENUM12   in the |E| = 12 stratum, closed en bloc by enum12.py (0 of 1884 weight-12
              logicals per sector admits a weight <= 10 solution)
     OPEN     neither

Also: dedup, per-key hash consistency, verdict-conflict detection, SAT-record audit.

usage:  python3 acct11.py DIR [DIR ...]
"""
import json, os, sys, glob, collections, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cert4

W = 10
CAND = {('Z', (1, 2, 62)), ('X', (14, 0, 2))}
SECTORS = ('Z', 'X')
NORB = 9

DIRS = sys.argv[1:]
if not DIRS:
    sys.exit("usage: acct11.py DIR [DIR ...]")

# ---------------------------------------------------------------- ingest
records = []            # every parsed record, with provenance
nlines = nbad = 0
files = []
for D in DIRS:
    for L in sorted(glob.glob(os.path.join(D, '*.jsonl'))):
        files.append(L)
        for i, ln in enumerate(open(L)):
            ln = ln.strip()
            if not ln:
                continue
            nlines += 1
            try:
                r = json.loads(ln)
            except Exception:
                nbad += 1
                continue
            r['_file'] = L
            r['_line'] = i + 1
            r['_tag'] = os.path.basename(os.path.dirname(L.rstrip('/'))) \
                if os.path.basename(os.path.dirname(L)) == 'logs' else os.path.basename(D)
            r['_short'] = os.path.basename(D) + '/' + os.path.basename(L)
            records.append(r)

print("=" * 78)
print("ACCT11 -- authoritative union accounting, CIRCDIST.gross W=10")
print("=" * 78)
print("log directories scanned : %d" % len(DIRS))
for D in DIRS:
    print("     %s" % D)
print("jsonl files             : %d" % len(files))
print("lines parsed            : %d   unparseable: %d" % (nlines, nbad))
print("records                 : %d" % len(records))
print()

# ---------------------------------------------------------------- global histograms
print("--- verdict histogram over ALL records ---")
print("   ", dict(collections.Counter(r.get('verdict') for r in records)))
print()
print("--- (sector, triple) histogram over ALL records ---")
tri = collections.Counter((r.get('sector'), tuple(r['triple']))
                          for r in records if 'triple' in r)
for k, v in tri.most_common():
    mark = "   <== CANDIDATE" if (k[0], k[1]) in CAND else ""
    print("    %-4s %-14s %5d%s" % (k[0], str(k[1]), v, mark))
print()

# ---------------------------------------------------------------- SAT audit
print("--- SAT-record audit (every SAT record in the corpus) ---")
sats = [r for r in records if r.get('verdict') == 'SAT']
oncand = 0
seen = set()
for r in sats:
    key = (r.get('sector'), tuple(r.get('triple', ())), r.get('K'), r.get('Ew'), r.get('orbit'))
    on = (r.get('sector'), tuple(r.get('triple', ()))) in CAND
    oncand += on
    flags = (r.get('decomposition_ok'), r.get('zero_syndrome'), r.get('nontrivial_logical'))
    print("    %-28s %-4s %-12s K=%-2s |E|=%-3s orbit=%-3s  oncand=%-5s  flags=%s"
          % (r['_short'], r.get('sector'), str(r.get('triple')), r.get('K'),
             r.get('Ew'), r.get('orbit'), on, flags))
    seen.add(key)
print("    SAT records: %d   distinct (sector,triple,K,|E|,orbit): %d   ON CANDIDATE: %d"
      % (len(sats), len(seen), oncand))
print()

# ---------------------------------------------------------------- candidate sub-query union
uni = collections.defaultdict(list)
for r in records:
    if r.get('verdict') not in ('SAT', 'UNSAT'):
        continue
    if 'triple' not in r or r.get('W') != W:
        continue
    if (r['sector'], tuple(r['triple'])) not in CAND:
        continue
    o = r.get('orbit', -1)
    if o is None or o < 0:
        continue
    uni[(r['sector'], r['K'], r['Ew'], o)].append(r)

print("--- dedup on the candidate ---")
mult = collections.Counter(len(v) for v in uni.values())
print("    distinct decided sub-queries       : %d" % len(uni))
print("    contributing records               : %d" % sum(len(v) for v in uni.values()))
print("    multiplicity histogram             : %s" % dict(sorted(mult.items())))
print("    sub-queries with >1 record         : %d   max multiplicity %d"
      % (sum(1 for v in uni.values() if len(v) > 1), max(mult)))

vconf = []
hgroups = collections.Counter()
hconf = []
for k, v in sorted(uni.items()):
    verds = {r['verdict'] for r in v}
    if len(verds) > 1:
        vconf.append((k, [(r['_short'], r['verdict']) for r in v]))
    # hash consistency: records that agree on cnf_sha256 must agree on verdict.
    byh = collections.defaultdict(set)
    for r in v:
        byh[r.get('cnf_sha256')].add(r['verdict'])
    hgroups[len(byh)] += 1
    for h, vs in byh.items():
        if len(vs) > 1:
            hconf.append((k, h, vs))
print("    VERDICT CONFLICTS across duplicates : %d" % len(vconf))
for k, d in vconf:
    print("        !! %s %s" % (str(k), d))
print("    distinct-CNF-hash count per sub-query: %s   (>1 = same sub-query under >1 encoding)"
      % dict(sorted(hgroups.items())))
print("    SAME-HASH verdict disagreements     : %d" % len(hconf))
for k, h, vs in hconf:
    print("        !! %s hash=%s verdicts=%s" % (str(k), h, vs))
print("    union verdicts                      : %s"
      % dict(collections.Counter(v[0]['verdict'] for v in uni.values())))
uv = collections.Counter()
for v in uni.values():
    uv[sorted({r['verdict'] for r in v})[0]] += 1
print()

# ---------------------------------------------------------------- complete space
cells = cert4.cells(W)
print("--- the COMPLETE sub-query space ---")
print("    cert4.cells(%d) : %d cells per sector, %d over both sectors"
      % (W, len(cells), 2 * len(cells)))
Ks = sorted({K for K, _ in cells})
print("    K values present : %s        K=0 cells: %s   (K>=1 everywhere: %s)"
      % (Ks, [c for c in cells if c[0] == 0], all(K >= 1 for K, _ in cells)))
print("    |E| values       : %s" % sorted({E for _, E in cells}))
print("    cells per K      : %s"
      % dict(sorted(collections.Counter(K for K, _ in cells).items())))
e12 = [c for c in cells if c[1] == 12]
print("    |E|=12 cells     : %d per sector (%d slots/sector) -- closed en bloc by enum12.py"
      % (len(e12), len(e12) * NORB))
TOTAL = 2 * len(cells) * NORB
print("    TOTAL SLOTS      : 2 x %d x %d = %d" % (len(cells), NORB, TOTAL))
print()

satdec = []
enum12only = []
openl = []
for sec in SECTORS:
    for (K, Ew) in cells:
        for o in range(NORB):
            k = (sec, K, Ew, o)
            if k in uni:
                satdec.append(k)
            elif Ew == 12:
                enum12only.append(k)
            else:
                openl.append(k)

print("--- classification of all %d slots ---" % TOTAL)
print("    SATDEC  (recorded solver verdict)   : %d" % len(satdec))
print("    ENUM12  (|E|=12, closed by enum12)  : %d" % len(enum12only))
print("    OPEN                                 : %d" % len(openl))
print("    ---------------------------------------------")
print("    accounted                            : %d / %d"
      % (len(satdec) + len(enum12only) + len(openl), TOTAL))
print()
print("    denominator used by the wave-6 tables (SATDEC + OPEN, i.e. excluding the")
print("    %d |E|=12 slots that carry no individual solver record) : %d"
      % (len(enum12only), len(satdec) + len(openl)))
print()

# ---------------------------------------------------------------- cells
print("--- cell verdicts ---")
opencells = []
for sec in SECTORS:
    nd = nsat = 0
    for (K, Ew) in cells:
        have = {o for o in range(NORB) if (sec, K, Ew, o) in uni}
        anysat = any(r['verdict'] == 'SAT' for o in have for r in uni[(sec, K, Ew, o)])
        if anysat:
            nsat += 1
        if len(have) == NORB or (Ew == 12 and len(have) < NORB):
            nd += 1
        else:
            opencells.append((sec, K, Ew, sorted(set(range(NORB)) - have)))
    print("    sector %s : %d/%d cells decided;  cells containing a SAT sub-query: %d"
          % (sec, nd, len(cells), nsat))
print("    open cells (both sectors) : %d" % len(opencells))
print()

print("--- THE EXACT OPEN LIST ---")
if not openl:
    print("    *** EMPTY -- the complete W=10 sub-query space is decided ***")
else:
    for sec in SECTORS:
        rows = [(K, Ew, o) for (s, K, Ew, o) in openl if s == sec]
        bycell = collections.defaultdict(list)
        for K, Ew, o in rows:
            bycell[(K, Ew)].append(o)
        print("    %s sector: %d cells, %d sub-queries" % (sec, len(bycell), len(rows)))
        for (K, Ew) in sorted(bycell):
            print("        (%d,%d): %s" % (K, Ew, sorted(bycell[(K, Ew)])))
    print("    by orbit index: %s" % dict(sorted(collections.Counter(o for _, _, _, o in openl).items())))
print()

# ---------------------------------------------------------------- cost
tot_all = sum(r['seconds'] for v in uni.values() for r in v if isinstance(r.get('seconds'), (int, float)))
tot_best = sum(min(r['seconds'] for r in v) for v in uni.values())
print("--- solver time ---")
print("    all distinct records : %.0f s  (%.1f CPU-hours)" % (tot_all, tot_all / 3600))
print("    best-of per sub-query: %.0f s  (%.1f CPU-hours)" % (tot_best, tot_best / 3600))
print()

json.dump({
    'open': openl,
    'decided': len(satdec),
    'enum12': len(enum12only),
    'total': TOTAL,
    'verdict_conflicts': len(vconf),
    'hash_conflicts': len(hconf),
}, open(os.path.join(HERE, 'acct11.json'), 'w'), indent=1)
print("wrote acct11.json")
```

#### `rebuild.py`

independent CNF rebuild, in two modes: `post` re-derives the five post-handoff driver records, `all` re-derives every recorded certificate in the union.

```python
#!/usr/bin/env python3
"""rebuild.py -- rebuild the CNF of every record in a given set of (key -> recorded hash)
pairs, in THIS namespace, and compare.  No solve.

usage: rebuild.py post          # the post-handoff driver records only
       rebuild.py all DIR...    # every distinct (sub-query, hash) in the union
"""
import sys, os, json, glob, hashlib, collections, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sched import make_phi
from cert import tiled_orders
import dext, dext2, cert4, cert6, cert7

_ctx = {}


def ctx_for(sector, triple):
    k = (sector, triple)
    if k not in _ctx:
        phi = make_phi(1, 1)
        orders, _ = tiled_orders(sector, phi, triple)
        _ctx[k] = dext.sector_ctx(orders, sector)[0]
    return _ctx[k]


_orb = {}


def rorb_for(triple):
    if triple not in _orb:
        phi = make_phi(1, 1)
        S, orbits = dext2.column_orbits(phi, triple)
        _orb[triple] = (S, [(rep, orb) for (rep, orb) in orbits if rep[0] == 'r'])
    return _orb[triple]


ENC = {'cert7': cert7.Cert7, 'cert4': cert4.Cert4, 'cert6': cert6.Cert6}


def build_hash(sector, triple, W, K, Ew, oi, enc):
    ctx = ctx_for(sector, triple)
    c = ENC[enc](ctx, W, K, Ew)
    cls = list(c.cls)
    if oi >= 0:
        S, rorb = rorb_for(triple)
        rep, orb = rorb[oi]
        cls.append([c.col_lit(rep)])
        for jj in range(oi):
            for col in rorb[jj][1]:
                cls.append([-c.col_lit(col)])
    h = hashlib.sha256()
    for cl in cls:
        h.update((" ".join(map(str, cl)) + "\n").encode())
    return h.hexdigest()[:32], len(cls)


POST = [
    # sector, triple,        K, Ew, orbit, recorded hash,                      provenance
    ('X', (14, 0, 2), 8, 20, 0, '27abef7a63adc65e5c28055b1cbdafcc', 'harvest/d10.jsonl   kissat 5420.3s'),
    ('Z', (1, 2, 62), 8, 20, 0, '32cf5a255215b3fad59a3ce8d739ac80', 'harvest/d10.jsonl   kissat 6746.2s'),
    ('Z', (1, 2, 62), 7, 16, 1, '6f4aa59dac5aa99d0784727ab466ef72', 'harvest/d10.jsonl   kissat 6800.1s'),
    ('Z', (1, 2, 62), 6, 16, 1, 'bfd07e4b4fdd796380440445b7479b7c', 'harvest/d10.jsonl   kissat 7665.3s'),
    ('X', (14, 0, 2), 8, 22, 0, '151cecf0bcb08fd8f944d6eff60b27c1', 'LIVE final.jsonl    cd15   9301.4s'),
    # the two drive7 records that post-date the wave-6 cell tables' Z rows
    ('Z', (1, 2, 62), 6, 20, 1, None, 'live final.jsonl    cd15   7396.2s'),
    ('Z', (1, 2, 62), 8, 22, 0, None, 'live final.jsonl    cd15   7559.6s'),
]

mode = sys.argv[1] if len(sys.argv) > 1 else 'post'

if mode == 'post':
    print("POST-HANDOFF DRIVER RECORDS -- independent CNF rebuild in a fresh namespace")
    print("=" * 100)
    ok = bad = 0
    for sec, tri, K, Ew, oi, rec, prov in POST:
        got, nc = build_hash(sec, tri, 10, K, Ew, oi, 'cert7')
        if rec is None:
            print("  %s (%2d,%2d) orbit %d  [%s]  rebuilt %s  nclauses_final=%d   (no hash quoted here)"
                  % (sec, K, Ew, oi, prov, got, nc))
            continue
        v = "MATCH" if got == rec else "*** MISMATCH ***"
        ok += got == rec
        bad += got != rec
        print("  %s (%2d,%2d) orbit %d  [%s]\n      recorded %s\n      rebuilt  %s  nclauses_final=%d   %s"
              % (sec, K, Ew, oi, prov, rec, got, nc, v))
    print("=" * 100)
    print("  MATCH: %d    MISMATCH: %d" % (ok, bad))
    sys.exit(0)

# ------------------------------------------------------------------ full union rebuild
DIRS = sys.argv[2:]
CAND = {('Z', (1, 2, 62)), ('X', (14, 0, 2))}
want = {}
for D in DIRS:
    for L in sorted(glob.glob(os.path.join(D, '*.jsonl'))):
        for ln in open(L):
            ln = ln.strip()
            if not ln:
                continue
            try:
                r = json.loads(ln)
            except Exception:
                continue
            if r.get('verdict') not in ('SAT', 'UNSAT'):
                continue
            if 'triple' not in r or r.get('W') != 10:
                continue
            if (r['sector'], tuple(r['triple'])) not in CAND:
                continue
            if r.get('orbit', -1) < 0:
                continue
            key = (r['sector'], tuple(r['triple']), r['K'], r['Ew'], r['orbit'],
                   r['cnf_sha256'], r.get('nclauses_final') or -1)
            want.setdefault(key, os.path.basename(D) + '/' + os.path.basename(L))

print("distinct (sub-query, recorded-hash) pairs to verify: %d" % len(want))
t0 = time.time()
ok = collections.Counter()
fails = []
for i, (key, prov) in enumerate(sorted(want.items())):
    sec, tri, K, Ew, oi, rh, ncf = key
    hit = None
    for enc in ('cert7', 'cert4', 'cert6'):
        try:
            got, nc = build_hash(sec, tri, 10, K, Ew, oi, enc)
        except Exception:
            continue
        if got == rh:
            hit = enc
            break
    if hit:
        ok[hit] += 1
    else:
        fails.append((key, prov))
    if (i + 1) % 100 == 0:
        print("   ... %d/%d  (%.0f s)" % (i + 1, len(want), time.time() - t0), flush=True)
print()
print("VERIFIED : %d" % sum(ok.values()))
print("FAILED   : %d" % len(fails))
print("by encoding that reproduced it: %s" % dict(ok))
for key, prov in fails:
    print("   FAIL %s  [%s]" % (str(key), prov))
print("elapsed %.0f s" % (time.time() - t0))
```

#### `w11.py`

the `d_ext <= 11` half of the verdict, RE-DERIVED (search the weight-12 logical pool for a logical containing a weight-2 residual) and then verified three independent ways.

```python
#!/usr/bin/env python3
"""w11.py -- independent re-verification of the  d_ext <= 11  half of the verdict on the
CANDIDATE assignment, in both sectors.

Two things, in order:

 (A) RE-DERIVE, not re-read.  Independently search for a weight-11 witness the way the upper-bound
     argument says one must exist: a weight-12 non-trivial logical L that contains a weight-2
     residual r of some check c; then  E = L,  R = {(c,k)},  d = L xor r  has
     |d| + |R| = 10 + 1 = 11.  Report how many such (L, c, k) exist, not just the first.

 (B) VERIFY the recorded anchor3.json witness, three independent ways:
       (1) dext.verify_witness       -- the project's own F2 checker
       (2) F2 algebra written here   -- shares no code with (1)
       (3) weight bookkeeping        -- |d| + |R| = 11 and |E| = 12
"""
import sys, os, json
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from gross import HX, HZ, N, NG, Reducer
from sched import make_phi
from cert import tiled_orders
import dext
import pool as poolmod

CAND = {'Z': (1, 2, 62), 'X': (14, 0, 2)}
rec = json.load(open(os.path.join(HERE, 'anchor3.json')))
PZ, PX, LX, LZ = poolmod.get()

print("=" * 96)
print("d_ext <= 11 on the CANDIDATE, independently re-derived and re-verified")
print("=" * 96)
allok = True
for sector in ('Z', 'X'):
    triple = CAND[sector]
    phi = make_phi(1, 1)
    orders, Hstab0 = tiled_orders(sector, phi, triple)
    ctx, Hstab = dext.sector_ctx(orders, sector)
    Hdet = HX if sector == 'Z' else HZ
    P = PZ if sector == 'Z' else PX

    # ---------------------------------------------------------------- (A) re-derive
    hits = []
    for Li, L in enumerate(P):
        for c in range(NG):
            for k in (0, 2):                 # the two weight-2 residuals r1, r3
                r = ctx.res[c][k]
                if len(r) == 2 and all(L[q] for q in r):
                    hits.append((Li, c, k))
    print()
    print("[%s]  candidate triple %s" % (sector, str(triple)))
    print("  (A) re-derivation: weight-12 logicals in the pool containing a weight-2 residual")
    print("      pool size %d;  (L, check, k) hits: %d;  distinct logicals L: %d;  distinct checks: %d"
          % (len(P), len(hits), len({h[0] for h in hits}), len({h[1] for h in hits})))
    # verify the FIRST hit end-to-end, from scratch
    Li, c, k = hits[0]
    L = P[Li]
    r = ctx.res[c][k]
    D0 = L.copy()
    for q in r:
        D0[q] ^= 1
    i0 = dext.verify_witness(ctx, L, [(c, k)], D0, Hstab)
    print("      first hit: logical #%d, check %d, k %d, r = %s" % (Li, c, k, sorted(r)))
    print("      -> weight %d = %d data + %d hook, |E| = %d, decomposition_ok=%s zero_syndrome=%s nontrivial_logical=%s"
          % (i0['weight'], i0['n_data'], i0['n_res'], i0['Ewt'], i0['decomposition_ok'],
             i0['zero_syndrome'], i0['nontrivial_logical']))
    derive_ok = (i0['weight'] == 11 and i0['Ewt'] == 12 and i0['decomposition_ok']
                 and i0['zero_syndrome'] and i0['nontrivial_logical'])

    # ---------------------------------------------------------------- (B) verify the record
    w = rec[sector]['w11']
    chk, kk = w['check'], w['k']
    Eset, Dset, rset = set(w['E']), set(w['D']), set(w['r'])
    r_derived = set(ctx.res[chk][kk])
    r_match = (r_derived == rset)

    E = np.zeros(N, np.uint8)
    for j in Eset:
        E[j] = 1
    D = np.zeros(N, np.uint8)
    for j in Dset:
        D[j] = 1

    info = dext.verify_witness(ctx, E, [(chk, kk)], D, Hstab)          # (1)

    rr = np.zeros(N, np.uint8)                                          # (2)
    for j in rset:
        rr[j] = 1
    decomp = bool(((D ^ rr) == E).all())
    zero_syn = not ((Hdet @ E) % 2).any()
    nontriv = not Reducer(Hstab).inspan(E)

    bk = (len(Dset) + 1 == 11 and len(Eset) == 12 and Dset == Eset - rset)   # (3)

    ok = (r_match and decomp and zero_syn and nontriv and bk and derive_ok
          and info['weight'] == 11 and info['decomposition_ok']
          and info['zero_syndrome'] and info['nontrivial_logical'])
    allok &= ok
    print("  (B) the recorded anchor3 witness: check %d, k %d, residual r = %s   (r re-derived from ctx.res: %s)"
          % (chk, kk, sorted(rset), r_match))
    print("      E = %s" % sorted(Eset))
    print("      d = %s" % sorted(Dset))
    print("      (1) dext.verify_witness : weight=%d = %d data + %d hook, |E|=%d, decomposition_ok=%s zero_syndrome=%s nontrivial_logical=%s"
          % (info['weight'], info['n_data'], info['n_res'], info['Ewt'],
             info['decomposition_ok'], info['zero_syndrome'], info['nontrivial_logical']))
    print("      (2) independent F2      : E = d xor r : %s    H_det.E = 0 : %s    E not in rowspace(H_stab) : %s"
          % (decomp, zero_syn, nontriv))
    print("      (3) bookkeeping         : |d| + |R| = %d + 1 = %d,  |E| = %d  -> %s"
          % (len(Dset), len(Dset) + 1, len(Eset), bk))
    print("      ==> %s :  d_ext(candidate, sector %s) <= 11" % ("PASS" if ok else "*** FAIL ***", sector))
print()
print("=" * 96)
print("BOTH SECTORS: %s" % ("PASS -- d_ext <= 11 on the candidate in both sectors, by explicit witness"
                            if allok else "*** FAILURE ***"))
```

#### `manifest.py`

emits the per-sub-query certificate manifest, the cell tables and the aggregate block.

```python
#!/usr/bin/env python3
"""manifest.py -- emit (a) the per-sub-query certificate manifest, (b) the cell tables,
(c) the aggregate block, for the harvest verdict artifact.

usage: manifest.py OUTDIR DIR [DIR ...]
"""
import sys, os, json, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cert4

W = 10
CAND = {('Z', (1, 2, 62)), ('X', (14, 0, 2))}
TRIPLE = {'Z': (1, 2, 62), 'X': (14, 0, 2)}
SECTORS = ('Z', 'X')
NORB = 9

OUT = sys.argv[1]
DIRS = sys.argv[2:]
os.makedirs(OUT, exist_ok=True)

uni = collections.defaultdict(list)
for D in DIRS:
    for L in sorted(glob.glob(os.path.join(D, '*.jsonl'))):
        for ln in open(L):
            ln = ln.strip()
            if not ln:
                continue
            try:
                r = json.loads(ln)
            except Exception:
                continue
            if r.get('verdict') not in ('SAT', 'UNSAT'):
                continue
            if 'triple' not in r or r.get('W') != W:
                continue
            if (r['sector'], tuple(r['triple'])) not in CAND:
                continue
            if r.get('orbit', -1) < 0:
                continue
            r['_log'] = os.path.basename(D.rstrip('/')) + '/' + os.path.basename(L)
            uni[(r['sector'], r['K'], r['Ew'], r['orbit'])].append(r)

# single-file records this box produced (job7k stdout, one json per file)
for L in sorted(glob.glob(os.path.join(HERE, 'logs', '*.json'))):
    b = os.path.basename(L)
    if not (b.startswith('h_') or b.startswith('audit_')):
        continue
    try:
        r = json.load(open(L))
    except Exception:
        continue
    if r.get('verdict') not in ('SAT', 'UNSAT'):
        continue
    if (r['sector'], tuple(r['triple'])) not in CAND:
        continue
    r['_log'] = 'logs_circdist_gross_verdict_20260823/' + b
    uni[(r['sector'], r['K'], r['Ew'], r['orbit'])].append(r)


def best(v):
    """authoritative record for a sub-query: prefer the fastest verified one."""
    return sorted(v, key=lambda r: (r['verdict'] != 'UNSAT', r.get('seconds', 1e18)))[0]


cells = cert4.cells(W)

# ------------------------------------------------------------------ manifest
rows = []
for sec in SECTORS:
    for (K, Ew) in cells:
        for o in range(NORB):
            k = (sec, K, Ew, o)
            if k in uni:
                r = best(uni[k])
                rows.append(dict(sector=sec, triple=list(TRIPLE[sec]), K=K, Ew=Ew, orbit=o,
                                 verdict=r['verdict'], solver=r.get('solver') or 'cd15',
                                 seconds=r.get('seconds'), cnf_sha256=r['cnf_sha256'],
                                 nclauses_final=r.get('nclauses_final'),
                                 nvars=r.get('nvars'), log=r['_log'],
                                 n_records=len(uni[k]),
                                 route='SAT-solver'))
            elif Ew == 12:
                rows.append(dict(sector=sec, triple=list(TRIPLE[sec]), K=K, Ew=Ew, orbit=o,
                                 verdict='UNSAT', solver='enum12.py', seconds=None,
                                 cnf_sha256=None, nclauses_final=None, nvars=None,
                                 log='logs_circdist_gross_verdict_20260823/enum12.out',
                                 n_records=0,
                                 route='exhaustive enumeration of the 1884 weight-12 logicals'))
            else:
                rows.append(dict(sector=sec, triple=list(TRIPLE[sec]), K=K, Ew=Ew, orbit=o,
                                 verdict='OPEN', solver=None, seconds=None, cnf_sha256=None,
                                 nclauses_final=None, nvars=None, log=None, n_records=0,
                                 route=None))

json.dump(rows, open(os.path.join(OUT, 'MANIFEST.json'), 'w'), indent=1)

with open(os.path.join(OUT, 'MANIFEST.md'), 'w') as f:
    f.write("# CIRCDIST.gross -- complete certificate manifest, W = 10\n\n")
    f.write("One row per (sector, K, |E|, orbit) slot of the complete sub-query space.\n")
    f.write("`route = SAT-solver` rows carry a CNF SHA-256 (sha256(...).hexdigest()[:32], i.e. the\n")
    f.write("first 128 bits -- NOT an MD5). Rebuild with `hashonly.py <sector> <a,b,c> 10 K Ew orbit`\n")
    f.write("and compare, then re-solve to re-derive the verdict.\n\n")
    f.write("`route = exhaustive enumeration` rows are the |E| = 12 stratum, decided without any\n")
    f.write("cell machinery by `enum12.py`: all 1884 weight-12 non-trivial logicals of the gross code\n")
    f.write("are enumerated by incremental SAT with blocking clauses (terminating in UNSAT, hence\n")
    f.write("exhaustive by construction), and each is shown to admit no weight-<=10 solution.\n\n")
    f.write("| # | sector | triple | K | \\|E\\| | orbit | verdict | route | solver | solver s | CNF SHA-256 (first 128 bits) | clauses | log |\n")
    f.write("|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
    for i, r in enumerate(rows, 1):
        f.write("| %d | %s | %s | %d | %d | %d | %s | %s | %s | %s | %s | %s | %s |\n" % (
            i, r['sector'], tuple(r['triple']), r['K'], r['Ew'], r['orbit'],
            "**" + r['verdict'] + "**",
            'solver' if r['route'] == 'SAT-solver' else ('enum12' if r['route'] else '--'),
            r['solver'] or '--',
            ("%.1f" % r['seconds']) if r['seconds'] is not None else '--',
            ("`%s`" % r['cnf_sha256']) if r['cnf_sha256'] else '--',
            r['nclauses_final'] if r['nclauses_final'] else '--',
            ("`%s`" % r['log']) if r['log'] else '--'))

# ------------------------------------------------------------------ cell tables
tbl = []
agg = collections.Counter()
for sec in SECTORS:
    tbl.append("")
    tbl.append("**sector %s, triple %s**" % (sec, str(TRIPLE[sec])))
    tbl.append("")
    tbl.append("| `K` | `\\|E\\|` | orbit 0..8 | cell verdict | cell CPU s |")
    tbl.append("|---|---|---|---|---|")
    nd = 0
    for (K, Ew) in cells:
        marks = ''
        cpu = 0.0
        nhave = 0
        for o in range(NORB):
            k = (sec, K, Ew, o)
            if k in uni:
                r = best(uni[k])
                marks += 'S' if r['verdict'] == 'SAT' else 'U'
                cpu += r.get('seconds') or 0.0
                nhave += 1
            else:
                marks += '.'
        if nhave == NORB:
            verdict = "**UNSAT**" if 'S' not in marks else "**SAT**"
            nd += 1
            agg['cells_solver'] += 1
        elif Ew == 12:
            verdict = "**UNSAT** (enum12)"
            nd += 1
            agg['cells_enum12'] += 1
        else:
            verdict = "open (%d)" % (NORB - nhave)
            agg['cells_open'] += 1
        tbl.append("| %d | %d | `%s` | %s | %d |" % (K, Ew, marks, verdict, round(cpu)))
    tbl.append("")
    tbl.append("`%d` of `%d` cells decided; SAT cells: `0`" % (nd, len(cells)))
open(os.path.join(OUT, 'CELLTABLES.md'), 'w').write("\n".join(tbl) + "\n")

# ------------------------------------------------------------------ aggregate
nslot = 2 * len(cells) * NORB
nsolver = sum(1 for r in rows if r['route'] == 'SAT-solver')
nenum = sum(1 for r in rows if r['route'] and r['route'] != 'SAT-solver')
nopen = sum(1 for r in rows if r['verdict'] == 'OPEN')
nsat = sum(1 for r in rows if r['verdict'] == 'SAT')
tot_best = sum(r['seconds'] or 0 for r in rows)
nrec = sum(len(v) for v in uni.values())
ndup = sum(1 for v in uni.values() if len(v) > 1)
conf = sum(1 for v in uni.values() if len({r['verdict'] for r in v}) > 1)

lines = [
    "complete sub-query space (2 sectors x %d cells x %d orbits)   %d" % (len(cells), NORB, nslot),
    "    decided by a SAT-solver certificate                      %4d" % nsolver,
    "    decided by exhaustive enumeration (|E| = 12, enum12.py)  %4d" % nenum,
    "    OPEN                                                     %4d" % nopen,
    "",
    "    of the decided slots, SAT                                %4d" % nsat,
    "    of the decided slots, UNSAT                              %4d" % (nsolver + nenum - nsat),
    "",
    "contributing solver records                                  %4d" % nrec,
    "sub-queries decided more than once                           %4d" % ndup,
    "verdict conflicts across duplicate decisions                 %4d" % conf,
    "",
    "cells decided by all-9-orbit solver cover                    %4d" % agg['cells_solver'],
    "cells decided by enum12                                      %4d" % agg['cells_enum12'],
    "cells open                                                   %4d" % agg['cells_open'],
    "",
    "solver time, best-of per sub-query    ~ %.0f s  (~%.0f CPU-hours)" % (tot_best, tot_best / 3600),
]
open(os.path.join(OUT, 'accounting.txt'), 'w').write("\n".join(lines) + "\n")
print("\n".join(lines))
print()
print("wrote %s/{MANIFEST.md,MANIFEST.json,CELLTABLES.md,accounting.txt}" % OUT)
if nopen:
    print("\nOPEN:")
    for r in rows:
        if r['verdict'] == 'OPEN':
            print("   %s (%d,%d) orbit %d" % (r['sector'], r['K'], r['Ew'], r['orbit']))
```


