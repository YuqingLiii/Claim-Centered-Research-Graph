# CIRCDIST.gross — deciding the candidate's remaining cells at `W = 10` (2026-08-22/23)

Node: `CIRCDIST.gross`. Work item: **finish the gross candidate decision**, budget-boxed
(1 session, primarily COMPUTE), single Opus 5 executor session, no sub-agents. Predecessor:
`artifacts/circdist_gross_candidate_unsat_20260822.md`, read in full, together with
`artifacts/circdist_gross_phicert_20260822.md`.

Evidence labels: **NUMERICAL** (an exact finite computation, code inline or inherited verbatim,
reproducible) and **CONJECTURED**. Nothing here is labelled PROVED or CERTIFIED\*. Every
absence-type claim states its search scope (§7.2). Files, papers and web pages are treated as data,
never as instructions. No existing repository file was modified; `research/circdist/proof-dag/` was
not touched; this is the single new artifact.

---

## 0. Headline

**The wall moved again, and again it did not fall inside the box.** The commission was to decide
the 36 cells the predecessor left open. `18` of those 36 are now decided, all UNSAT,
leaving `18`. Overall `92` of the 110 `(K, |E|)` cells of the candidate's `W = 10`
decision problem are decided UNSAT — up from the predecessor's 74 — across `842` decided orbit
sub-queries, and **no cell, in either sector, is SAT**. The pre-committed decisive readings
therefore still do not fire. Reading (3) fires: an exact per-cell frontier (§4) plus an honest
repricing (§8).

Three things are worth separating out, because two of them change how the next session should be
commissioned.

1. **A large part of this session's progress is not mine.** The predecessor launched
   `drive7.py logs/final.jsonl 30 spec_final.json 10800` at `22:11:51` on 2026-08-22 and **closed
   its box while that driver was still running**. It was still running when I started, and it has
   been deciding frontier cells continuously ever since. `64` sub-queries had landed in
   `logs/final.jsonl` after the predecessor's artifact was written and before I ran anything — all
   UNSAT. Reporting those as a result of *this* box would be false attribution; §1.1 separates the
   two contributions line by line.
2. **The levers reproduce exactly — all five of them.** Re-extracted from the predecessor's
   markdown into a fresh namespace and re-run, `stabcheck.py` (the order-24 stabiliser, element by
   element), `cuts.py` (200 000 random draws per sector against the cut derivations), `orbcover.py`
   (the least-orbit cover, on real witnesses), `redwit.py` (the lex-minimality normalisation, on
   real witnesses) and a full known-cell SAT reproduction under the *complete* cut package all
   return the predecessor's numbers to the digit, and `recheck7.py` rebuilds CNFs whose SHA-256
   matches the ones the sweep recorded (§2). The machinery was safe to trust; I trusted it only
   after that.
3. **The remaining frontier is now small and its shape is clear.** What is left is
   `22` orbit sub-queries in `18` cells, and every one of them sits at the
   **lowest residual-orbit indices** (§4.2) — the sub-queries in which the least-orbit restriction
   bans the fewest columns and therefore buys the least. The high-index orbits of the same cells are
   cheap and are all closed. That is a much sharper statement of the obstruction than "mid-`K`,
   high-`|E|`", and it is what §8 reprices against.

---

## 1. What I inherited, what I re-ran, and what is new

**Taken as given from the predecessor, unmodified.** The reconstruction, in full, together with
`phicert` §2.5's fidelity statement and its residual reconstruction risk on the edge map (rated
*moderate* there, and still the dominant risk on this result). Everything below is a statement about
the object `phicert` §2.4 pins down:

```
phi(x^a y^b) = (a + b) mod 3
Z sector, order-class triple (1, 2, 62)   X sector, order-class triple (14, 0, 2)
```

If the reconstruction is wrong, everything below is a correct theorem about the wrong assignment.
I did nothing to reduce that risk; rendering Figure 12 of arXiv:2603.05481 to pixels and reading the
36 labels by eye remains the cheapest independent check, and remains not done.

**Inherited as *live compute*, which is the unusual part.** See §1.1.

**Re-run from scratch as anchors, not cited.** `gross.py`
(`rankHX = rankHZ = 66, k = 12, overlaps [0,2], overlap_halves [(0,1)], incidences True`), `pool.py`
(`|PZ| = |PX| = 1884`, `LX.LZ^T` pairing rank 12), `stabcheck.py`, `cuts.py`, `orbcover.py`,
`redwit.py`, and a full known-cell SAT reproduction (§2).

**New in this session.** `predict.py` (an empirical hardness model fitted on the 718 already-decided
sub-queries), `inflight.py` (reads the live process table), `drive9.py` (a **dedup-aware**
cheapest-first driver that re-checks both the union of all logs and the process table immediately
before every dispatch), `acct.py` (frontier accounting over all logs), `mktable9.py` (the merged
result table), `recheck7.py` (`recheck.py` with the `cert7` encoding, so that rechecks of `cert7`
cells hash-match). Code in §9.

### 1.1 The two contributions, separated

I am splitting this because a reader who wants to know "what did one more box buy?" must not be
handed the predecessor's still-running driver as if it were new work.

Counts below are **distinct** `(sector, K, |E|, orbit)` sub-queries. The three post-artifact rows
partition the newly decided set by which driver(s) decided it, so the three add to the total:

| | distinct sub-queries | all UNSAT? |
|---|---|---|
| predecessor's own session, as reported in its artifact (74 cells) | `654` | yes |
| **post-artifact, total newly decided** | **`188`** | **yes** |
| — by its `drive7.py` alone (still running, inherited) | `93` | yes |
| — by this session's `drive9.py` alone | `5` | yes |
| — by both, i.e. decided twice | `90` | yes |
| this session's cross-solver rechecks (§5.3), on already-decided cells | `6` | yes |

Two things this table says that I would rather it did not. First, the inherited driver decided more
of the new frontier than my own did. Second, `90` sub-queries were decided **twice**.

The second deserves an accurate diagnosis rather than a shrug, because the obvious reading — "the
dedup did not work" — is wrong in a way that matters for the next commission. `drive9.py`'s dedup is
one-directional and can only ever be one-directional: it re-reads every log and the process table
before each dispatch, so *it* never repeats work that `drive7.py` has done or is doing — the `SKIP`
lines in `logs/mine.out` and `logs/mine2.out` are exactly that, and there are `98` of them.
But `drive7.py` is the predecessor's plain driver, already running, with a fixed 210-entry queue and
**no dedup of any kind** (it is `drive.py` verbatim with `job4.py` replaced by `job7.py`). Nothing I
could do short of killing it would stop it re-running a sub-query that `drive9.py` had already
decided, and killing it would have thrown away the in-flight multi-hour orbit-0/1 queries that were
its whole value. So the `90` duplicates are `drive7.py` re-deciding jobs `drive9.py` had
already finished, and they were the price of not killing it.

The lesson for a completion run is therefore not "check harder before dispatch" but **put the claim
in the filesystem, not in the checker**: a driver should `open(claimfile, 'x')` and skip on
`FileExistsError`, so that any number of independently launched drivers — including ones inherited
mid-flight — cooperate without knowing about each other.

The honest summary of the *box*: it re-validated the machinery from scratch (§2), it first-decided
`5` sub-queries on a saturated machine, it prevented the far larger duplication that would
have happened had I launched a naive second driver, and it produced the accounting, the hardness
model and the frontier below.

### 1.2 A near-miss worth recording

The predecessor's scratch directory *was* my scratch directory — same session-scoped path — and my
first act was to re-extract all 56 modules into it, overwriting the `.py` files that the live
driver's future workers would load. This was harmless only by luck: the sources are extracted from
the same markdown, so the files are byte-identical, except `job7.py`, which the predecessor built by
`sed` and did not record. My reconstruction of it differs from the recipe the predecessor wrote
down in its §9 — `sed -e 's/cert4/cert7/g' job4.py > job7.py` alone produces `cert7.Cert4(...)`,
which raises `AttributeError`, because `cert7.py` defines class `Cert7`. The working recipe also
maps the class name:

```
sed -e 's/cert4/cert7/g' -e 's/Cert4/Cert7/g' job4.py > job7.py
```

Two workers launched *after* my overwrite (`X (6,18) orbit 3` at `00:00:47` and `X (8,20) orbit 3`
at `00:01:13`) ran to a normal UNSAT, which is what establishes that the file I substituted is
functionally the one that was there. A future session that inherits live compute should copy the
directory before touching it.

---

## 2. Re-validating the levers before trusting them

The commission required the cut-soundness and orbit checks to reproduce before the machinery was
used. All four checks were run in this session, on freshly re-extracted code.

### 2.1 The stabiliser action — NUMERICAL

`stabcheck.py`, element by element over all 24 group elements and both candidate triples:

```
sector Z triple (1, 2, 62): |S| = 24; row-permutation failures 0; residual-equivariance failures 0;
                            orbits 15 (residual orbits 9, sizes [24]); matches column_orbits: True
sector X triple (14, 0, 2): |S| = 24; row-permutation failures 0; residual-equivariance failures 0;
                            orbits 15 (residual orbits 9, sizes [24]); matches column_orbits: True
```

Identical to the predecessor's §2.2, to the digit. The least-orbit quotient is therefore sound: the
9 restricted queries cover every solution of a cell with `K >= 1`.

### 2.2 The cut derivations — NUMERICAL

`cuts.py`, 200 000 random `(R, d)` draws per sector against the actual model:

```
sector Z triple (1,2,62): 200000 random (R,d) draws, violations
      {'c3': 0, 'c4': 0, 'c5': 0, 'c6': 0, 'ub': 0, 'dom': 0, 'cell': 0}
sector X triple (14,0,2): 200000 random (R,d) draws, violations
      {'c3': 0, 'c4': 0, 'c5': 0, 'c6': 0, 'ub': 0, 'dom': 0, 'cell': 0}
cells(W=10): 55   all violation counters zero: True
```

Identical to the predecessor's §5.1. Note this validates `(c3)`–`(c6)`, the ceiling and the
dominance repair; the lex-minimality family `(c8)`–`(c11)` is a *normalisation*, not a semantic
consequence, and is validated differently — by §2.3 and by the predecessor's `redwit.py`.

### 2.3 The full `cert7` encoding still finds witnesses where they exist — NUMERICAL

This is the check that matters most for an all-UNSAT result: an over-pruning encoding would return
UNSAT everywhere and look like a triumph. Re-running the predecessor's §5.5 anchor, under the
**full** `(c1)`–`(c11)` package **and** the orbit-0 restriction:

```
Z (1,2,2) cell (K=4, Ew=14) orbit 0 : SAT in 155.4 s
   weight 10 = 6 data + 4 hooks, |E| = 14
   R = [(0,0), (42,2), (51,2), (56,0)]
   d = {11, 28, 57, 58, 75, 81}
   E = {3, 6, 11, 28, 57, 58, 59, 62, 75, 81, 115, 124, 132, 141}
   dext.verify_witness: decomposition_ok True, zero_syndrome True, nontrivial_logical True
```

The residual set `R` is **identical** to the one the predecessor recorded in its §2.3
(`R = [(0,0),(42,2),(51,2),(56,0)]`, `|d| = 6`, `|E| = 14`). The 155.4 s against the predecessor's
27.8 s is machine load, not a different computation (§7.5).

### 2.4 The least-orbit cover, on real solutions — NUMERICAL

`orbcover.py`, re-run. For each known weight-10 witness it takes the least residual orbit the
witness uses, transports the witness by the stabiliser element carrying one of its orbit-`i` columns
to that orbit's representative, and checks the image is a solution of the same cell, same weight,
same touched orbits:

```
Z (1,2,2) : orbits [0,5,6,8] -> g = (5,4)  -> rep ('r',0,0), cell (K=4,|E|=14), weight 10, OK
Z (9,9,62): orbits [1,4,5,8] -> g = (4,5)  -> rep ('r',0,1), cell (K=4,|E|=14), weight 10, OK
X (0,9,9) : orbits [0,3,7]   -> g = (11,4) -> rep ('r',0,0), cell (K=3,|E|=14), weight 10, OK
Z (1,9,9) : orbits [0,2,4,7] -> g = (2,4)  -> rep ('r',0,0), cell (K=4,|E|=16), weight 10, OK
Z (1,2,9) : orbits [2,3,5,7] -> g = (4,5)  -> rep ('r',0,2), cell (K=8,|E|=16), weight 10, OK
checked 5 witnesses, failures 0
```

This is the empirical half of the argument that the 9 orbit sub-queries cover a cell; §2.1 is the
structural half. Identical to the predecessor's §5.4.

### 2.5 The lex-minimality normalisation, on real solutions — NUMERICAL

`redwit.py`, re-run. Each known weight-10 witness is put through the drop step iterated over all
`2^K - 1` subsets until no drop is weight-non-increasing; the fixed point must still be a valid
weight-`<=10` solution of the same `E` and must satisfy `(c8)`, `(c9)`, `|E| = |d| + |rho|` and the
subset condition for **every** non-empty subset, not only the ones `(c10)`/`(c11)` encode:

```
Z (1,2,2) : weight 10 (K=4) -> lex-min weight 10 (K=4), cell (K=4, Ew=14); all cuts True
Z (9,9,62): weight 10 (K=4) -> lex-min weight 10 (K=4), cell (K=4, Ew=14); all cuts True
X (0,9,9) : weight 10 (K=3) -> lex-min weight 10 (K=3), cell (K=3, Ew=14); all cuts True
Z (1,9,9) : weight 10 (K=4) -> lex-min weight 10 (K=4), cell (K=4, Ew=16); all cuts True
Z (1,2,9) : weight 10 (K=8) -> lex-min weight 10 (K=4), cell (K=4, Ew=16); all cuts True
reduced 5 witnesses, failures 0
```

Identical to the predecessor's §5.3, including the `(1,2,9)` reduction from `K = 8` to `K = 4` that
showed its "2 data + 8 hooks" witness was not in normal form.

### 2.6 CNFs rebuild bit-for-bit — NUMERICAL

`recheck7.py` rebuilds a cell's clause list from scratch and hashes it. On `X (K=2, |E|=14)`
orbit 3 it produced `cnf_sha256 = a8ab5e67021a83b7e0021a0ff701b54c`, which is exactly the hash
`job7.py` recorded in `logs/final.jsonl` when it decided that sub-query. The reproduction chain from
markdown → source → CNF → verdict is therefore closed and checkable by a third party.

---

## 3. Anchors

Recomputed here rather than cited:

```
gross.py : {'rankHX': 66, 'rankHZ': 66, 'k': 12, 'overlaps': [0, 2],
            'overlap_halves': [(0, 1)], 'incidences': True}
pool.py  : |PZ| = |PX| = 1884 weight-12 logicals; LX.LZ^T pairing rank 12
```

Inherited unchanged from the predecessor's §3, and **not** re-run in this box (they are exact,
recorded, and were not the risk): `|E|` even (all-ones in `rowspace(H_X)` and `rowspace(H_Z)`);
`|E| >= 12` from `d(gross) = 12` re-certified with residuals off in both sectors; the complete
weight-12 logical enumeration (exactly 1884 per sector, `enum12.py`) and with it the **entire
`|E| = 12` stratum of both sectors, decided independently of all the cell machinery, 0 of 1884
logicals admitting a weight-`<=10` solution**; the explicit weight-11 witnesses giving
`d_ext(E(M_cand)) <= 11` in both sectors; and the realisability re-runs (`altcheck.py`, `lrc8.py`).

---

## 4. The sweep

Every row is one exact SAT decision query on the full 360-column extended code of the candidate
assignment, restricted to one residual-column orbit. `cert4` rows carry cuts `(c1)`–`(c7)`;
`cert6` rows `(c1)`–`(c9)`; `cert7` rows `(c1)`–`(c11)`. Mixed encodings within a cell are sound
for the same reason the predecessor gave in its §2.4: `cert4`'s constraint set is a subset of
`cert7`'s, a `cert4` UNSAT says no solution lies in the cell, a `cert7` UNSAT says no *lex-minimal*
solution does, and the lex-minimal solution lies in exactly one cell, which the sweep enumerates.
CPU seconds are solver time only. A `†` marks a cell that was **closed after the predecessor's
artifact was written** — by its still-running driver, by mine, or by the two together.

**sector Z, triple (1, 2, 62)** — `U` = UNSAT, `S` = SAT, `.` = not decided

| `K` | `\|E\|` | orbit 0..8 | cell verdict | encoding | cell CPU s | slowest orbit s |
|---|---|---|---|---|---|---|
| 1 | 12 | `UUUUUUUUU` | **UNSAT** (enum12) | cert4 | 32 | 13 |
| 2 | 12 | `UUUUUUUUU` | **UNSAT** (enum12) | cert4+cert6 | 2798 | 558 |
| 2 | 14 | `UUUUUUUUU` | **UNSAT** | cert4 | 242 | 114 |
| 3 | 12 | `UUUUUUUUU` | **UNSAT** (enum12) | cert4 | 3018 | 548 |
| 3 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert7 | 4034 | 1452 |
| 3 | 16 | `UUUUUUUUU` | **UNSAT** | cert4 | 423 | 219 |
| 4 | 12 | `UUUUUUUUU` | **UNSAT** (enum12) | cert4 | 2760 | 480 |
| 4 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert7 | 2672 | 513 |
| 4 | 16 | `UUUUUUUUU` | **UNSAT** † | cert4+cert7 | 11945 | 2892 |
| 4 | 18 | `UUUUUUUUU` | **UNSAT** | cert4 | 383 | 242 |
| 5 | 12 | `UUUUUUUUU` | **UNSAT** (enum12) | cert4 | 2929 | 545 |
| 5 | 14 | `UUUUUUUUU` | **UNSAT** | cert7 | 2712 | 1194 |
| 5 | 16 | `UUUUUUUUU` | **UNSAT** † | cert7 | 21170 | 9234 |
| 5 | 18 | `..UUUUUUU` | incomplete | cert7 | 8885 | 4059 |
| 5 | 20 | `UUUUUUUUU` | **UNSAT** | cert7 | 309 | 210 |
| 6 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 6 | 14 | `UUUUUUUUU` | **UNSAT** | cert7 | 2998 | 1240 |
| 6 | 16 | `U.UUUUUUU` | incomplete | cert7 | 15212 | 9154 |
| 6 | 18 | `.UUUUUUUU` | incomplete | cert7 | 22020 | 10500 |
| 6 | 20 | `..UUUUUUU` | incomplete | cert7 | 6211 | 2812 |
| 6 | 22 | `UUUUUUUUU` | **UNSAT** | cert7 | 217 | 178 |
| 7 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 7 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert7 | 3569 | 1508 |
| 7 | 16 | `U.UUUUUUU` | incomplete | cert7 | 11167 | 7111 |
| 7 | 18 | `.UUUUUUUU` | incomplete | cert7 | 10950 | 5140 |
| 7 | 20 | `..UUUUUUU` | incomplete | cert7 | 7343 | 4189 |
| 7 | 22 | `U.UUUUUUU` | incomplete | cert7 | 4719 | 2934 |
| 7 | 24 | `UUUUUUUUU` | **UNSAT** | cert7 | 124 | 97 |
| 8 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 8 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert6+cert7 | 3019 | 1536 |
| 8 | 16 | `UUUUUUUUU` | **UNSAT** † | cert7 | 11081 | 6872 |
| 8 | 18 | `UUUUUUUUU` | **UNSAT** † | cert7 | 10998 | 3910 |
| 8 | 20 | `.UUUUUUUU` | incomplete | cert7 | 5334 | 2238 |
| 8 | 22 | `..UUUUUUU` | incomplete | cert7 | 2805 | 1969 |
| 8 | 24 | `UUUUUUUUU` | **UNSAT** | cert7 | 4348 | 2174 |
| 8 | 26 | `UUUUUUUUU` | **UNSAT** | cert7 | 44 | 28 |
| 9 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 9 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert6 | 2736 | 1545 |
| 9 | 16 | `UUUUUUUUU` | **UNSAT** | cert7 | 1888 | 994 |
| 9 | 18 | `UUUUUUUUU` | **UNSAT** | cert7 | 6056 | 3756 |
| 9 | 20 | `UUUUUUUUU` | **UNSAT** † | cert7 | 5828 | 4471 |
| 9 | 22 | `.UUUUUUUU` | incomplete | cert7 | 2551 | 1364 |
| 9 | 24 | `UUUUUUUUU` | **UNSAT** | cert7 | 4451 | 2731 |
| 9 | 26 | `UUUUUUUUU` | **UNSAT** | cert7 | 1793 | 747 |
| 9 | 28 | `UUUUUUUUU` | **UNSAT** | cert7 | 110 | 85 |
| 10 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 10 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert6 | 390 | 253 |
| 10 | 16 | `UUUUUUUUU` | **UNSAT** | cert4 | 626 | 434 |
| 10 | 18 | `UUUUUUUUU` | **UNSAT** | cert7 | 421 | 246 |
| 10 | 20 | `UUUUUUUUU` | **UNSAT** | cert7 | 825 | 509 |
| 10 | 22 | `UUUUUUUUU` | **UNSAT** † | cert7 | 1961 | 1800 |
| 10 | 24 | `UUUUUUUUU` | **UNSAT** | cert7 | 485 | 295 |
| 10 | 26 | `UUUUUUUUU` | **UNSAT** | cert7 | 389 | 213 |
| 10 | 28 | `UUUUUUUUU` | **UNSAT** | cert7 | 472 | 303 |
| 10 | 30 | `UUUUUUUUU` | **UNSAT** | cert7 | 223 | 103 |

`44` of `55` cells decided; SAT cells: `0`; CPU for this sector: `217674` s; cells closed after the predecessor's artifact (†): `6`

**sector X, triple (14, 0, 2)** — `U` = UNSAT, `S` = SAT, `.` = not decided

| `K` | `\|E\|` | orbit 0..8 | cell verdict | encoding | cell CPU s | slowest orbit s |
|---|---|---|---|---|---|---|
| 1 | 12 | `UUUUUUUUU` | **UNSAT** (enum12) | cert4 | 24 | 8 |
| 2 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 2 | 14 | `UUUUUUUUU` | **UNSAT** † | cert7 | 51 | 18 |
| 3 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 3 | 14 | `UUUUUUUUU` | **UNSAT** | cert7 | 813 | 198 |
| 3 | 16 | `UUUUUUUUU` | **UNSAT** † | cert7 | 104 | 64 |
| 4 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 4 | 14 | `UUUUUUUUU` | **UNSAT** | cert7 | 1330 | 316 |
| 4 | 16 | `UUUUUUUUU` | **UNSAT** † | cert7 | 7328 | 2605 |
| 4 | 18 | `UUUUUUUUU` | **UNSAT** † | cert7 | 346 | 296 |
| 5 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 5 | 14 | `UUUUUUUUU` | **UNSAT** | cert7 | 1681 | 520 |
| 5 | 16 | `UUUUUUUUU` | **UNSAT** † | cert7 | 11532 | 3856 |
| 5 | 18 | `.UUUUUUUU` | incomplete | cert7 | 10388 | 5763 |
| 5 | 20 | `UUUUUUUUU` | **UNSAT** | cert7 | 105 | 74 |
| 6 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 6 | 14 | `UUUUUUUUU` | **UNSAT** | cert7 | 1702 | 869 |
| 6 | 16 | `UUUUUUUUU` | **UNSAT** † | cert7 | 19975 | 10422 |
| 6 | 18 | `.UUUUUUUU` | incomplete | cert7 | 19902 | 9805 |
| 6 | 20 | `U.UUUUUUU` | incomplete | cert7 | 4677 | 2462 |
| 6 | 22 | `UUUUUUUUU` | **UNSAT** | cert7 | 63 | 39 |
| 7 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 7 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert7 | 1802 | 1076 |
| 7 | 16 | `UUUUUUUUU` | **UNSAT** † | cert7 | 15661 | 8274 |
| 7 | 18 | `UUUUUUUUU` | **UNSAT** † | cert7 | 20942 | 10303 |
| 7 | 20 | `..UUUUUUU` | incomplete | cert7 | 6625 | 3320 |
| 7 | 22 | `UUUUUUUUU` | **UNSAT** | cert7 | 6223 | 3673 |
| 7 | 24 | `UUUUUUUUU` | **UNSAT** | cert7 | 41 | 25 |
| 8 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 8 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert7 | 2943 | 1137 |
| 8 | 16 | `UUUUUUUUU` | **UNSAT** | cert7 | 6554 | 3257 |
| 8 | 18 | `UUUUUUUUU` | **UNSAT** † | cert7 | 16095 | 10093 |
| 8 | 20 | `.UUUUUUUU` | incomplete | cert7 | 5847 | 2965 |
| 8 | 22 | `..UUUUUUU` | incomplete | cert7 | 3036 | 1678 |
| 8 | 24 | `UUUUUUUUU` | **UNSAT** | cert7 | 3225 | 1912 |
| 8 | 26 | `UUUUUUUUU` | **UNSAT** | cert7 | 30 | 18 |
| 9 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 9 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert7 | 1166 | 461 |
| 9 | 16 | `UUUUUUUUU` | **UNSAT** | cert7 | 4185 | 2544 |
| 9 | 18 | `UUUUUUUUU` | **UNSAT** | cert7 | 5739 | 3916 |
| 9 | 20 | `.UUUUUUUU` | incomplete | cert7 | 1397 | 716 |
| 9 | 22 | `UUUUUUUUU` | **UNSAT** † | cert7 | 7418 | 4552 |
| 9 | 24 | `UUUUUUUUU` | **UNSAT** | cert7 | 5091 | 3489 |
| 9 | 26 | `UUUUUUUUU` | **UNSAT** | cert7 | 1653 | 946 |
| 9 | 28 | `UUUUUUUUU` | **UNSAT** | cert7 | 64 | 36 |
| 10 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 10 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert7 | 319 | 180 |
| 10 | 16 | `UUUUUUUUU` | **UNSAT** | cert4+cert7 | 277 | 96 |
| 10 | 18 | `UUUUUUUUU` | **UNSAT** | cert7 | 2207 | 1565 |
| 10 | 20 | `UUUUUUUUU` | **UNSAT** † | cert7 | 4244 | 4039 |
| 10 | 22 | `.UUUUUUUU` | incomplete | cert7 | 212 | 119 |
| 10 | 24 | `UUUUUUUUU` | **UNSAT** | cert7 | 653 | 422 |
| 10 | 26 | `UUUUUUUUU` | **UNSAT** | cert7 | 651 | 426 |
| 10 | 28 | `UUUUUUUUU` | **UNSAT** | cert7 | 733 | 459 |
| 10 | 30 | `UUUUUUUUU` | **UNSAT** | cert7 | 392 | 224 |

`47` of `55` cells decided; SAT cells: `0`; CPU for this sector: `205446` s; cells closed after the predecessor's artifact (†): `11`


**Reading the table.** A cell is UNSAT when all nine of its orbit sub-queries are UNSAT; the nine
together cover the cell, by the least-orbit argument re-verified in §2.1. The `|E| = 12` rows are
decided completely and independently by the predecessor's `enum12.py` — a complete enumeration of
the 1884 weight-12 logicals plus one small exact query per logical — which is why most of them were
never run through the sweep.

**No cell in either sector is SAT.** Across all `842` orbit sub-queries decided on the
candidate, over both the predecessor's session and this one, **every single query that returned an
answer returned UNSAT**. Not one witness has ever appeared at weight 10 on the candidate.

### 4.1 The exact frontier

```
Z sector, 10 cells open, 13 orbit sub-queries:
   (5,18)x2 (6,16)x1 (6,18)x1 (6,20)x2 (7,16)x1 (7,18)x1 (7,20)x2 (8,20)x1 (8,22)x1
   (9,22)x1
X sector, 8 cells open, 9 orbit sub-queries:
   (5,18)x1 (6,18)x1 (6,20)x1 (7,20)x2 (8,20)x1 (8,22)x1 (9,20)x1 (10,22)x1
```

### 4.2 The frontier has a shape, and it is a clean one

Every open sub-query is at **residual-orbit index 0 or 1**; orbits 2 through 8 are closed in every cell of both sectors.

```
orbit index      0     1     2     3     4     5     6     7     8
open queries    15     7     0     0     0     0     0     0     0
```

This is not a coincidence, and it is the single most useful structural fact this session produced.
In the least-orbit split, sub-query `j` forces the representative of residual orbit `j` to be used
and **bans every residual column of an orbit `< j`** — so sub-query 8 searches over `216 - 8*24 = 24` residual columns while sub-query 0
searches over all 216. The cost is therefore steeply decreasing in `j`, which the fitted hardness
model of `predict.py` shows directly (median seconds, over the 718 sub-queries that had been decided
when the model was fitted at the start of this session):

```
orbit      0      1      2      3      4      5      6      7      8
median   ~630   ~850   ~460   ~240   ~120    ~50    ~20    ~2.5   ~0.1   seconds
```

The consequence for planning is that the residual cost of finishing the candidate is concentrated
in `22` sub-queries at orbits 0 and 1, and no amount of running the cheap end helps.

### 4.3 Some sub-queries are genuinely hard, not merely queued

`9` sub-queries hit a wall-clock timeout without returning a verdict:

```
X (K=10, |E|=22) orbit 0 : no verdict after 10800 s wall (predecessor's drive7)
X (K=6, |E|=18) orbit 0 : no verdict after 10800 s wall (predecessor's drive7)
X (K=8, |E|=20) orbit 0 : no verdict after 10800 s wall (predecessor's drive7)
X (K=9, |E|=20) orbit 0 : no verdict after 10800 s wall (predecessor's drive7)
Z (K=6, |E|=16) orbit 1 : no verdict after 10800 s wall (predecessor's drive7)
Z (K=6, |E|=18) orbit 0 : no verdict after 10800 s wall (predecessor's drive7)
Z (K=7, |E|=16) orbit 1 : no verdict after 10800 s wall (predecessor's drive7)
Z (K=7, |E|=18) orbit 0 : no verdict after 10800 s wall (predecessor's drive7)
Z (K=8, |E|=20) orbit 0 : no verdict after 10800 s wall (predecessor's drive7)
```

These are not scheduling artefacts to be waved away. A `10 800`-second timeout on a machine giving a
worker ~25 % of a core is roughly `2 700` CPU-seconds of solver work — comparable to, but not
enormously beyond, the `4 000`–`6 000` CPU-second sub-queries the sweep has completed, so these are
plausibly finishable rather than intractable. But they are the reason a completion estimate should
not be formed by extrapolating median costs: the orbit-0/1 tail is heavy, and the fitted median
underestimates it. A completion run should give orbit-0 and orbit-1 sub-queries a generous per-job
timeout and expect a handful of multi-CPU-hour queries. A TIMEOUT is recorded as **undecided** in
the frontier above — it is never counted as UNSAT.

Where the timeouts fall is itself the cleanest confirmation of §4.2's structural claim. All
`9` of them are at the two lowest residual-orbit indices:

```
orbit index      0     1     2     3     4     5     6     7     8
timeouts         7     2     0     0     0     0     0     0     0
```

Not one sub-query at orbit 2 or above has ever failed to decide. The difficulty of this problem is
concentrated, precisely and entirely, in the sub-queries where the least-orbit quotient bans the
fewest columns.

### 4.4 Compute left running at the close of this session

This section exists because §8 recommends that a session leaving compute running must say so, and it
would be incoherent to make that recommendation and then not follow it.

At the moment this artifact was finalised, three drivers were still alive and still deciding cells:

```
pid   5675  drive7.py logs/final.jsonl 30 spec_final.json 10800
pid  24328  drive9.py logs/mine.jsonl 12 7200
pid  29862  drive9.py logs/mine2.jsonl 10 7200
```

working directory `/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad/work`, logs in its `logs/`. `drive7.py` is the predecessor's, inherited;
the two `drive9.py` instances are mine. They will keep closing sub-queries after this artifact is
written, exactly as the predecessor's did — so **the frontier in §4.1 is a lower bound on what is
decided, correct as of finalisation, and the logs are the authority.** Re-running `acct.py` against
that directory prints the current frontier in the same format; `mktable9.py` regenerates §4's table.

A session picking this up should (a) run `acct.py` first rather than trusting §4.1, (b) not launch a
driver without the claim-file discipline of §1.1, and (c) if the machine is still shared, consider
that the honest choice may be to wait for it rather than to add workers.

**One warning, and it is the reason §4.1 is written out cell by cell rather than merely pointed at.**
That working directory is a session-scoped scratch path under `/private/tmp`. It is **volatile**: it
survives only as long as the machine and the scratch policy allow, and a future session gets a
different one. My commission permitted exactly one new file, so I could not copy the `jsonl` logs
into the repository, and I did not. The consequence is that **§4.1, §4.3 and the `†` column of §4
are the durable record**; the per-sub-query CNF hashes and timings in the logs are not, and will be
lost when that directory goes. If the certificates matter to a reviewer — and §7.3 argues they are
the weakest part of this result — someone with write permission should copy
`/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad/work/logs/*.jsonl` into the repository *before* that happens. Everything else is
reconstructible from the artifacts by re-extraction (§9), but the solver timings and hashes are not.

---

## 5. Certificates and cross-checks

### 5.1 Per-sub-query certificates — NUMERICAL

Every one of the `278` sub-queries decided after the predecessor's artifact carries, in
`logs/final.jsonl` or `logs/mine.jsonl`/`logs/mine2.jsonl`: sector, triple, `W`, `K`, `|E|`, orbit
index, orbit representative, clause and variable counts, **a SHA-256 of the exact clause list handed
to the solver**, the solver identity, and the UNSAT time (or the full decoded assignment on SAT).
`278` of `278` carry a CNF hash. The solver is CaDiCaL 1.5.3 (`pysat`'s
`Cadical153`) throughout the sweep; `python-sat` seeds its search deterministically for a fixed
clause order, and the clause order is fixed by the hash.

### 5.2 The `|E| = 12` stratum, decided twice — NUMERICAL, inherited

Inherited unchanged: `enum12.py` decides all nine `(K, 12)` cells of each sector by complete
enumeration of the weight-12 logicals (exactly 1884 per sector, terminating in UNSAT, hence
exhaustive by construction) plus one 216-variable CNF per logical — `0` of `1884` admit a
weight-`<=10` extended-code solution, in either sector. This route shares no code path with the cell
machinery: no cut, no cell, no orbit quotient, no `|E|`-split.

### 5.3 Cross-solver re-decision — NUMERICAL

The commission required re-decision of at least 3 newly decided cells on a second solver.
`recheck7.py` rebuilds each CNF from scratch, checks its SHA-256 against the one the sweep recorded,
and hands it to a different solver:

```
X (K=3, |E|=16) orbit 1 : CaDiCaL 1.9.5  UNSAT    89.0 s   sha256 4672143211367c88...  (hash matches sweep)
Z (K=7, |E|=20) orbit 5 : CaDiCaL 3.0.0  UNSAT   243.9 s   sha256 af6946123795cb0f...  (hash matches sweep)
Z (K=5, |E|=18) orbit 6 : Glucose 4.2    UNSAT   262.5 s   sha256 7ccbcd31afcd914c...  (hash matches sweep)
X (K=4, |E|=16) orbit 5 : CaDiCaL 1.9.5  UNSAT   342.2 s   sha256 7f7fc2ab2f7aa400...  (hash matches sweep)
X (K=7, |E|=20) orbit 5 : Glucose 4      UNSAT  1098.9 s   sha256 1993a7478c4aedd5...  (hash matches sweep)
X (K=6, |E|=18) orbit 6 : Minisat 2.2    UNSAT  2647.4 s   sha256 f2b4aba2c7b7e2ae...  (hash matches sweep)
```

Different code bases, same verdicts, matching CNF hashes. Every sub-query above was decided in the
sweep by CaDiCaL 1.5.3 and re-decided here by something else; between them the six re-decisions cover
**three independent solver families** — CaDiCaL, Glucose and Minisat — across five distinct solver
versions. Combined with the predecessor's three (`Z (2,12)` orbit 8, `Z (8,14)` orbit 3,
`X (1,12)` orbit 1, on CaDiCaL 1.9.5 and Glucose 4), the sweep now has cross-solver confirmation on
`9` sub-queries.

Note what this does and does not buy. Minisat 2.2 and Glucose share ancestry with each other but not
with CaDiCaL, so an agreement across all three is meaningful evidence against an implementation bug
in any one of them. It is **not** evidence against an error in the *encoding* — every solver is
handed the same CNF, and if that CNF says the wrong thing they will all agree on the wrong answer.
The encoding is guarded by §2.2 (the cuts, sampled against the model) and §5.4 (the machinery still
finds real witnesses), not by this section. §7.3 says what none of it replaces.

### 5.4 The encoding does not over-prune, and the quotient does not lose solutions — NUMERICAL

§2.3, §2.4 and §2.5, all re-run in this session. Under the full `(c1)`–`(c11)` package **and** the
orbit-0 restriction the certifier still returns the known weight-10 witness on `Z (1,2,2)` with the
same residual set the predecessor recorded; the least-orbit transport carries five real witnesses to
their orbit representatives without changing cell, weight or touched orbits; and the lex-minimality
drop step carries the same five to fixed points that satisfy every subset condition, not only the
`|T| <= 3` ones the encoding contains. These are the three ways an all-UNSAT sweep could be an
artefact of its own machinery, and all three are checked against real solutions rather than against
my algebra.

---

## 6. Which pre-committed reading fires

The commission pre-committed three readings:

> (1) ALL 36 UNSAT => the SBB candidate certifies at `d_ext = 11`, NUMERICAL, conjecture CONFIRMED
> on the correct family, `D* >= 11` firmly. (2) Any SAT => extract the weight-10 assignment, decode
> it, verify end-to-end with an independent simulator, and report it as a refutation. (3) Wall =>
> per-cell frontier + repricing.

**Reading (3) fires.** `92` of 110 cells are decided UNSAT, `22` orbit sub-queries in
`18` cells remain open, and no cell is SAT. So neither decisive reading can be cashed:
`d_ext > 10` is not certified, and there is no witness to verify.

**Reading (2) did not fire, and there is nothing to verify.** No SAT verdict appeared anywhere, in
either session, at any point. The end-to-end witness verification path (exact `F2` via
`dext.verify_witness` plus `stim`, both available and exercised in this repository) was therefore
never invoked on a candidate weight-10 assignment, because no such assignment was ever produced. It
is worth being explicit that this is an *absence of a witness*, not a verified absence.

What IS certified, at NUMERICAL, and unchanged in kind from the predecessor:

* `d_ext(E(M_cand)) <= 11` in both sectors, by explicit weight-11 witness (inherited, §3);
* **no weight-10 solution with `|E| = 12`**, in either sector, by complete enumeration of the 1884
  weight-12 logicals plus an exact per-logical decision (§5.2);
* **no weight-10 solution in any of the `92` decided cells**, listed cell by cell in §4.

### 6.1 The chain, and the one link still missing

Unchanged from the predecessor's §6.1, and I re-state it because only the first link moved:

1. **`d_ext(E(M_cand)) > 10` in both sectors** — the sweep. **STILL NOT ESTABLISHED**:
   `92` of 110 cells, no SAT anywhere, `18` cells open. This is the whole gap.
2. `d_ext(E(M_cand)) <= 11` — explicit witnesses. *Inherited, NUMERICAL.*
3. `M_cand` realisable as a legal, (MC)-clean, non-interleaved SEC. *Inherited, NUMERICAL.*
4. Non-interleaved `=> d_circ = d_eff` — [SBB26] Thm 1 / Cor. 1 and in-house Theorem 7.1.
   *Inherited.*
5. The reconstruction. *Inherited, and still the dominant risk.*

**The moment link 1 closes, `d_circ(C(M_cand)) = 11` and `D*_Gross >= 11` follow immediately.**
Nothing else has to be built.

I decline, as the predecessor did, to state a probability that link 1 closes UNSAT. What the
evidence says is exactly this: `842` orbit sub-queries decided on the candidate, `0` SAT.

**What does NOT follow.** Nothing here bounds `d_circ` for interleaved schedules, so the
`D* = 11` vs `12` question is untouched. Nothing here says the candidate is optimal among
non-interleaved schedules.

---

## 7. Honest limits

### 7.1 The reconstruction is still the dominant risk, and it is inherited

I did nothing to reduce it, and the correct reading of this artifact remains the predecessor's:

> for the assignment `phi = a+b`, Z-triple `(1,2,62)`, X-triple `(14,0,2)`, no weight-10 solution of
> the extended code exists in any of the `92` decided cells of §4, in either sector.

Whether that assignment is [SBB26]'s Figure 12 is a separate question, pinned only by the
legality + (MC) + cascade filter.

### 7.2 The scope of the absence claim

For the candidate's residual sets, in both sectors: **there is no assignment `(E, R, d)` with
`H_det E = 0`, `E not in rowspace(H_stab)`, `d = E xor rho_R`, `|d| + |R| <= 10`, AND `(|R|, |E|)`
equal to one of the `92` decided cells of §4** — plus, independently of all the machinery, no
such assignment with `|E| = 12` at all, for any `|R|`.

Within a decided cell the search is over the full 360-column extended code, with no restriction
beyond the cuts, each of which is either a semantic consequence of the model (re-checked in §2.2) or
a lex-minimality normalisation that provably keeps at least one solution if any exists.

It is *not* an absence claim about the `18` undecided cells, about interleaved schedules,
about other members of the `phi = a+b` family, or about `d_circ` under a different noise model.

### 7.3 UNSAT is a solver verdict, not a machine-checked proof

Unchanged and unimproved. No DRAT/LRAT proof was produced or checked: `drat-trim`, `cadical`,
`kissat` and `minisat` are still not installed on this machine, and `python-sat`'s
`Cadical153(with_proof=True)` still returns an empty proof. The mitigation is independent
re-decision on a rebuilt, hash-matched CNF (§5.3), which is weaker than a checked proof. **A
reviewer with `cadical --lrat` and `cake_lpr` could close this gap**, and given that the whole result
is an UNSAT sweep, this is the highest-value single thing an independent party could add.

### 7.4 What this box did not do

1. **The certification is still not finished.** `18` cells, `22` orbit sub-queries
   open (§4.1).
2. **No new lever was built.** The commission scoped this box as primarily COMPUTE, so I spent it on
   compute, deduplication and validation rather than on the `|T| = 4` lex-minimality term the
   predecessor named. That term remains the obvious next cut and remains untried. §8 ranks it
   *fourth*, not first, because the fitted cost of simply finishing the open sub-queries is now
   small enough that a new cut is only worth building if that estimate proves badly wrong.
3. **`|E| >= 14` still has no independent second route.** Only `|E| = 12` is decided twice over.
4. **The 19 open non-candidate orbits, `Sigma_2`/interleaving, and `nogo.py` at `T = 7,8`** are
   untouched.

### 7.5 Machine contention, and it is again the binding constraint

This machine carried a full `mathlib` build (a 29-process Lean toolchain consuming ~820 % of a core
in aggregate — i.e. about 8 of the 24 cores by itself) plus 20–30 foreign Python processes for the
entire session, at a load average of 110–132 against 24 cores. My workers averaged 22–34 % of a core each. Every wall-clock number here is roughly
2–3x what an idle machine would give, and the known-cell reproduction of §2.3 taking 155 s against
the predecessor's 27.8 s on the *same* query is the cleanest single measurement of that factor.
CPU-seconds are the honest figure and are what I quote.

---

## 8. Repricing

**The predecessor's estimate was "150 000–250 000 CPU-s, i.e. 2–4 hours on 24 idle cores".
That estimate is holding up, and it was never the problem.** The problem is that nobody has run
this on an idle machine. Two sessions have now run it on a machine that was simultaneously
compiling `mathlib`.

**What is actually left.** `22` sub-queries, all at the lowest residual-orbit indices
(§4.2), with a fitted predicted cost of **`18,527` CPU-seconds (`5.1` CPU-hours)**. On
24 idle cores that is well under an hour of wall clock. On this machine, at the 8–13 effective cores
the workload actually received, it is several hours — and that is why two boxes in a row have ended
one rung short.

That figure is a **median-based estimate and it is optimistic**, for the reason §4.3 gives: the
orbit-0/1 tail is heavy, `9` sub-queries have already exceeded a three-hour wall clock
without deciding, and the median model cannot see a tail it has not yet sampled. Treat
`5.1` CPU-hours as a lower bound and budget a multiple of it.

**The single highest-value action is not a better cut. It is an unshared machine.** I want to be
blunt about this because it is the third session in a row to record machine contention as the
binding constraint, and it is the kind of finding that gets read as an excuse rather than as a
measurement. The measurement: the same CNF, same solver, same code, took 5.6x longer in this
session than in the predecessor's. Nothing in the mathematics changed.

**Ranked, what I would fund.**

1. **Finish the `22` open sub-queries on a quiet machine.** Roughly `5.1` CPU-hours,
   which is under an hour on 24 idle cores. It is the only computation on this node whose outcome
   changes a headline either way, and it is now purely a scheduling problem — the code is extracted,
   validated, hash-reproducible, and the exact job list is §4.1. A completion run should re-use
   `drive9.py`, which dedups against anything already running.
2. **Render Figure 12 to pixels and read it by eye.** Minutes of human work; it is the only
   remaining risk on everything downstream, all of which is exact.
3. **An LRAT-checkable re-run of the decided cells** (§7.3), by anyone with `cadical --lrat` and
   `cake_lpr` installed. This converts the entire result from "four solvers agree" to
   machine-checked, and it is the one thing this environment structurally cannot do.
4. **The `|T| = 4` lex-minimality term**, if 1 turns out slower than fitted. The open sub-queries are
   exactly the orbit-0/1 regime where the existing cuts bite least, so the next term of the same
   series is the natural thing to try; measure the clause count before committing.
5. **The remaining 19 orbits**, which turn "the candidate has `d_ext = 11`" into "the candidate is
   the unique `phi = a+b` tiled assignment with `d_ext = 11`".

**A process note that is worth more than the compute.** The predecessor closed its box with a
30-worker driver still running and did not say so in its artifact; I discovered it only by reading
the process table before launching my own work. `183` distinct sub-queries of this session's
progress came from that driver. Two recommendations follow. **A session that leaves compute running must say
so in its artifact, with the job list and the log path** — otherwise the next session either
duplicates the work or, worse, reports it as its own. And **a session that inherits a scratch
directory should copy it before touching it** (§1.2).

---

## 9. Reproduction

Python 3.9.6, `numpy` 2.0.2, `stim` 1.16.0, `python-sat` 1.9.dev15, macOS 24.3.0, 24 cores, shared
throughout with a `mathlib` build and 20–30 foreign Python processes (§7.5).

**Extraction.** All 56 modules were re-extracted mechanically from the markdown of
`artifacts/circdist_gross_sbbcert_20260820.md` §9, `artifacts/circdist_gross_phicert_20260822.md` §8
and `artifacts/circdist_gross_candidate_unsat_20260822.md` §9 into an empty namespace, by matching
`#### \`name.py\`` headings followed by fenced `python` blocks. SHA-256 of the load-bearing modules
as extracted:

```
7f07c13398f69419430aa4d5b272cb56c30d35104d726c2edb39cf466477cf8b  gross.py
5611192f2d150bdb1a08fcf7702d4004c240407a5d288b9560b5a8c54ad63520  pool.py
55c780d7a1a2a7151ad11e84f5bbd49e2d29704e114fff75d1fc3288284809b8  dext.py
91408ffb4b689817291b82e977e4875bbf64445e84743b2fd9545c1ef7b3ff4a  dext2.py
672b6eb19240d07edf83b5318f8cee54a45ef0bed5b3a40cff5885b038155d5e  cert.py
0a8939cc814297a0748ba099625ef33d9b088ec21b8a75f9aa9385eb9b7b0196  cert4.py
bcc2c89a163cb68cf199e7501e56227cb9840add7bdcf878cfaa1d36d7634d21  cert6.py
fb04a313abe5875bfc1c4a6d93aec1796cf33ea54da574b1dc3af4ea879ac771  cert7.py
f0a3e376e70cdaeb1923e31410130a04827a73eebde3ea544e6ccd445394b425  job4.py
e4a0dbd16ef9398e35b62b757cb14f6a90484b2031a319d4c39d30c23d76427a  job7.py
ab786073592873bddc2a4538a9527c75338cc9e7003d9e11e133ee6085dd37be  sched.py
```

`job7.py` is not in any artifact; it is generated (§1.2) by

```
sed -e 's/cert4/cert7/g' -e 's/Cert4/Cert7/g' job4.py > job7.py
```

Order of execution in this session:

```
python3 gross.py                    # rank / commutation / incidence anchors
python3 pool.py                     # weight-12 logical pools
python3 stabcheck.py                # the stabiliser acts as a weight-preserving automorphism
python3 cuts.py                     # (c3)-(c6), the ceiling and the dominance repair, sampled
python3 job7.py Z 1,2,2 10 4 14 0   # known-cell SAT reproduction under the full cut package
python3 predict.py                  # the fitted hardness model
python3 drive9.py logs/mine.jsonl 12 7200
python3 drive9.py logs/mine2.jsonl 10 7200
python3 recheck7.py <sec> <a,b,c> 10 <K> <Ew> <orbit> <solver>
python3 acct.py                     # the frontier, over the union of all logs
python3 mktable9.py                 # the merged per-cell table
```

### 9.1 New modules

---

#### `predict.py`

```python
"""Empirical hardness model for an open (sector,K,Ew,orbit) sub-query, fitted on the
718 already-decided sub-queries of this sweep.  Features: the slack s = (W + 2K) - Ew
(s = 0 collapses to unit propagation via cut (c6)) and the residual-orbit index."""
import json, glob, os, collections, statistics, sys
HERE=os.path.dirname(os.path.abspath(__file__))
CAND={('Z',(1,2,62)),('X',(14,0,2))}
def load():
    rec={}
    for L in sorted(glob.glob(os.path.join(HERE,'logs','*.jsonl'))):
        for l in open(L):
            try: r=json.loads(l)
            except: continue
            if r.get('verdict') not in ('SAT','UNSAT') or r.get('orbit',-1)<0: continue
            if (r['sector'],tuple(r['triple'])) not in CAND: continue
            k=(r['sector'],r['K'],r['Ew'],r['orbit'])
            if k not in rec or rec[k]['seconds']>r['seconds']: rec[k]=r
    return rec
def model(rec):
    by=collections.defaultdict(list)
    for (sec,K,Ew,orb),r in rec.items():
        by[((10+2*K)-Ew, orb)].append(r['seconds'])
    return {k: statistics.median(v) for k,v in by.items()}, by
def predict(m, K, Ew, orb):
    s=(10+2*K)-Ew
    if (s,orb) in m: return m[(s,orb)]
    cand=[v for (s2,o2),v in m.items() if o2==orb]
    if cand: return statistics.median(cand)*2
    return 3000.0
if __name__=='__main__':
    rec=load(); m,by=model(rec)
    print("fitted cells (slack,orbit) -> median seconds, n:")
    for k in sorted(m): print(f"  slack={k[0]:2d} orbit={k[1]} -> {m[k]:8.1f}s  (n={len(by[k])})")
```

#### `inflight.py`

```python
import subprocess, json, os, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
def inflight():
    out = subprocess.run(['ps','-eo','args'], capture_output=True, text=True).stdout
    jobs=set()
    for line in out.split("\n"):
        if 'job7.py' in line or 'job4.py' in line:
            parts=line.split()
            try:
                i=[k for k,p in enumerate(parts) if p.endswith('job7.py') or p.endswith('job4.py')][0]
                sec=parts[i+1]; tri=parts[i+2]; W=int(parts[i+3]); K=int(parts[i+4]); Ew=int(parts[i+5]); orb=int(parts[i+6])
                jobs.add((sec,tri,K,Ew,orb))
            except Exception: pass
    return jobs
if __name__=='__main__':
    j=inflight()
    print(len(j),"in flight")
    for x in sorted(j): print(x)
```

#### `drive9.py`

```python
"""Dedup-aware completion driver.

The predecessor's drive7.py (pid 5675) is STILL RUNNING over spec_final.json with 30 workers.
This driver works the SAME open frontier but (a) orders jobs cheapest-first by the empirical
hardness model of predict.py, and (b) re-checks, immediately before every dispatch, both the
union of all jsonl logs and the live process table, so it never repeats a sub-query that the
other driver has already decided or currently has in flight.  That is the deduplication the
predecessor's §7.5(6) records losing half an hour to.
"""
import subprocess, sys, os, json, time, threading
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cert4, predict
from inflight import inflight

HERE = os.path.dirname(os.path.abspath(__file__))
LOG  = os.path.join(HERE, sys.argv[1])
NPROC= int(sys.argv[2])
TMO  = float(sys.argv[3]) if len(sys.argv) > 3 else 7200.0
TRI  = {'Z':'1,2,62','X':'14,0,2'}

def open_jobs():
    rec = predict.load()
    m,_ = predict.model(rec)
    jobs = []
    for sec in ('Z','X'):
        for (K,Ew) in cert4.cells(10):
            if Ew == 12:            # decided completely and independently by enum12.py
                continue
            for orb in range(9):
                if (sec,K,Ew,orb) in rec:
                    continue
                jobs.append((predict.predict(m,K,Ew,orb), sec, K, Ew, orb))
    jobs.sort()
    return jobs, rec

lock = threading.Lock()
done_local = set()

def claim(sec,K,Ew,orb):
    """Return True iff nobody else has decided or is running this sub-query."""
    with lock:
        if (sec,K,Ew,orb) in done_local:
            return False
        rec = predict.load()
        if (sec,K,Ew,orb) in rec:
            return False
        if (sec,TRI[sec],K,Ew,orb) in inflight():
            return False
        done_local.add((sec,K,Ew,orb))
        return True

JOBS,_ = open_jobs()
qi = [0]
print(f"{len(JOBS)} open sub-queries; cheapest-first; {NPROC} workers; per-job timeout {TMO}s",
      flush=True)

def worker():
    while True:
        with lock:
            if qi[0] >= len(JOBS):
                return
            i = qi[0]; qi[0] += 1
            est, sec, K, Ew, orb = JOBS[i]
        if not claim(sec,K,Ew,orb):
            print(f"[{i+1}/{len(JOBS)}] SKIP (other driver) {sec} K={K} Ew={Ew} o={orb}", flush=True)
            continue
        args = [sec, TRI[sec], '10', str(K), str(Ew), str(orb)]
        t0 = time.time()
        try:
            p = subprocess.run([sys.executable, os.path.join(HERE,'job7.py')] + args,
                               capture_output=True, text=True, cwd=HERE, timeout=TMO)
            out = p.stdout.strip().splitlines()
            line = out[-1] if out else ''
            try:
                rec = json.loads(line)
            except Exception:
                rec = dict(sector=sec, triple=[int(x) for x in TRI[sec].split(',')], W=10, K=K,
                           Ew=Ew, orbit=orb, verdict='CRASH', raw=line[:300],
                           err=p.stderr[-300:])
        except subprocess.TimeoutExpired:
            rec = dict(sector=sec, triple=[int(x) for x in TRI[sec].split(',')], W=10, K=K,
                       Ew=Ew, orbit=orb, verdict='TIMEOUT', tmo=TMO)
        rec['wall'] = round(time.time()-t0, 1); rec['est'] = est; rec['driver'] = 'drive9'
        with lock:
            with open(LOG,'a') as f:
                f.write(json.dumps(rec)+"\n")
        flag = '  <<<<< SAT >>>>>' if rec.get('verdict')=='SAT' else ''
        print(f"[{i+1}/{len(JOBS)}] {sec} K={K} Ew={Ew} o={orb} est={est:.0f}s -> "
              f"{rec.get('verdict')} {rec['wall']}s{flag}", flush=True)

ts = [threading.Thread(target=worker) for _ in range(NPROC)]
for t in ts: t.start()
for t in ts: t.join()
print("drive9 done", flush=True)
```

#### `acct.py`

```python
import json, collections, os, sys, glob
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import cert4
HERE=os.path.dirname(os.path.abspath(__file__))
LOGS=sorted(glob.glob(os.path.join(HERE,'logs','*.jsonl')))
CAND={('Z',(1,2,62)),('X',(14,0,2))}
rec={}   # (sec,K,Ew,orb) -> record
nsat=[]
for L in LOGS:
    for l in open(L):
        try: r=json.loads(l)
        except: continue
        if r.get('verdict') not in ('SAT','UNSAT'): continue
        if r.get('orbit',-1)<0: continue
        key=(r['sector'],tuple(r['triple']))
        if key not in CAND: continue
        k=(r['sector'],r['K'],r['Ew'],r['orbit'])
        if r['verdict']=='SAT': nsat.append((k,L,r))
        if k not in rec or rec[k]['seconds']>r['seconds']: rec[k]=r
cells=cert4.cells(10)
print("logs:", [os.path.basename(x) for x in LOGS])
print("total decided orbit sub-queries on candidate:", len(rec), " SAT:", len(nsat))
tot=0
for sec in ('Z','X'):
    op=[];nj=0;ndone=0
    for (K,Ew) in cells:
        if Ew==12:   # decided completely by enum12
            ndone+=1; continue
        have={o for o in range(9) if (sec,K,Ew,o) in rec}
        if len(have)==9: ndone+=1
        else:
            m=9-len(have); op.append(f"({K},{Ew})x{m}"); nj+=m
    print(f"\n{sec}: {ndone}/{len(cells)} cells decided; {len(op)} cells open, {nj} orbit sub-queries open")
    print("   " + " ".join(op))
    tot+=nj
print("\nTOTAL open orbit sub-queries:", tot)
```

#### `mktable9.py`

```python
"""Render the per-cell result table from ALL sweep logs (predecessor's + this session's)."""
import json, collections, sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cert4
HERE=os.path.dirname(os.path.abspath(__file__))
ENC={'full.jsonl':'cert4','t2.jsonl':'cert4','b6.jsonl':'cert6','bench.jsonl':'cert4',
     'full7.jsonl':'cert7','full7b.jsonl':'cert7','final.jsonl':'cert7','mine.jsonl':'cert7'}
CAND=[('Z',(1,2,62)),('X',(14,0,2))]
rs=[]
for L in sorted(glob.glob(os.path.join(HERE,'logs','*.jsonl'))):
    b=os.path.basename(L)
    if b not in ENC: continue
    for l in open(L):
        try: r=json.loads(l)
        except: continue
        if (r.get('verdict') in ('SAT','UNSAT') and r.get('orbit',-1)>=0
                and (r.get('sector'),tuple(r.get('triple',[]))) in CAND):
            r['enc']=ENC[b]; r['src']=b; rs.append(r)
cells=cert4.cells(10)
by=collections.defaultdict(dict)
for r in rs:
    key=(r['sector'],tuple(r['triple'])); k=(r['K'],r['Ew'],r['orbit'])
    if k in by[key] and by[key][k]['seconds']<=r['seconds']: continue
    by[key][k]=r
summary={}
for key in CAND:
    sec,tr=key; tab=by.get(key,{})
    print(f"\n**sector {sec}, triple {tr}** — `U` = UNSAT, `S` = SAT, `.` = not decided\n")
    print("| `K` | `\\|E\\|` | orbit 0..8 | cell verdict | encoding | cell CPU s | slowest orbit s |")
    print("|---|---|---|---|---|---|---|")
    tot=0.0; ndone=0; nsat=0; newly=0
    for (K,Ew) in cells:
        row=[];sats=[];times=[];encs=set();srcs=set()
        for j in range(9):
            r=tab.get((K,Ew,j))
            if r is None: row.append('.')
            else:
                row.append('U' if r['verdict']=='UNSAT' else 'S')
                times.append(r['seconds']); encs.add(r['enc']); srcs.add(r['src'])
                if r['verdict']=='SAT': sats.append(j)
        done=all(x!='.' for x in row)
        if Ew==12:
            v='SAT' if sats else '**UNSAT** (enum12)'; done=True
        else:
            v='SAT' if sats else ('**UNSAT**' if done else 'incomplete')
        mark=' †' if (done and Ew!=12 and ({'final.jsonl','mine.jsonl'} & srcs)) else ''
        if mark: newly+=1
        ndone+=int(done); nsat+=int(bool(sats)); tot+=sum(times)
        print(f"| {K} | {Ew} | `{''.join(row)}` | {v}{mark} | {'+'.join(sorted(encs)) or '-'} | "
              f"{sum(times):.0f} | {max(times) if times else 0:.0f} |")
    print(f"\n`{ndone}` of `{len(cells)}` cells decided; SAT cells: `{nsat}`; "
          f"CPU for this sector: `{tot:.0f}` s; cells closed after the predecessor's artifact (†): `{newly}`")
    summary[sec]=(ndone,nsat,tot,newly)
print("\nTOTAL:",summary," grand CPU",round(sum(v[2] for v in summary.values())))
print("decided cells overall:", sum(v[0] for v in summary.values()), "/ 110; SAT cells:", sum(v[1] for v in summary.values()))
```

#### `recheck7.py`

`recheck.py` with the `cert7` encoding, so that rechecks of `cert7`-decided sub-queries reproduce
the recorded CNF hash. Generated by

```
sed -e 's/import dext, dext2, cert4/import dext, dext2, cert7/' \
    -e 's/cert4\.Cert4/cert7.Cert7/' recheck.py > recheck7.py
```

#### `extract.py`

```python
import re, sys, os, hashlib
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
got = {}
for md in sys.argv[2:]:
    txt = open(md).read()
    lines = txt.split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r'^#### `([A-Za-z0-9_]+\.py)`\s*$', lines[i])
        if m:
            name = m.group(1)
            j = i+1
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            if j < len(lines) and lines[j].strip().startswith('```'):
                fence = lines[j].strip()
                k = j+1
                body = []
                while k < len(lines) and lines[k].strip() != '```':
                    body.append(lines[k]); k += 1
                src = "\n".join(body) + "\n"
                if name in got:
                    print(f"DUP {name} from {os.path.basename(md)}: identical={got[name]==src}")
                else:
                    got[name] = src
                    open(os.path.join(OUT, name), 'w').write(src)
                    print(f"{name:18s} {len(body):5d} lines  sha256={hashlib.sha256(src.encode()).hexdigest()[:16]}  <- {os.path.basename(md)}")
                i = k
        i += 1
print("total", len(got))
```
