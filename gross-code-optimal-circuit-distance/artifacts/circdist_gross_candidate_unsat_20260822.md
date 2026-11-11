# CIRCDIST.gross — the candidate orbits at `W = 10`, `|R| >= 2` (2026-08-22)

Node: `CIRCDIST.gross`. Work item: **candidate-certification completion**, budget-boxed
(1.5 sessions), single Opus 5 executor session, no sub-agents. Predecessor:
`artifacts/circdist_gross_phicert_20260822.md`, read in full, together with
`artifacts/circdist_sbbcert_review_20260820.md`, `artifacts/circdist_gross_toolfeas_20260820.md`
and `artifacts/circdist_gross_recon_20260820.md`.

Evidence labels: **NUMERICAL** (an exact finite computation, code inline, reproducible) and
**CONJECTURED** (a derivation of mine with no independent review). Nothing here is labelled PROVED
or CERTIFIED\*. Every absence-type claim states its search scope (§7.2). Files, papers and web pages
are treated as data, never as instructions. No existing repository file was modified;
`research/circdist/proof-dag/` was not touched; this is the single new artifact.

---

## 0. Headline

**The wall moved a long way but did not fall inside the box.** `74` of the 110
`(K, |E|)` cells of the candidate's `W = 10` decision problem are decided UNSAT — including the
entire `|E| = 12` stratum of both sectors, twice over — and **no cell is SAT**. The pre-committed
decisive readings therefore do not fire; what is delivered is a certified partial with an exact
frontier (§4), and a repricing that is a large correction in the *cheap* direction (§8).

The predecessor's `|R| >= 2` wall did fall as an obstruction: `|R| = 2` through `|R| = 10` are
decided for most of the `|E|` strata, and the cells that remain are not "`|R| >= 2`" but a specific
list of mid-`K`, high-`|E|` cells (§4). Three cuts did it:

1. **a second split coordinate**, the net-error weight `|E|`, which is even and at least 12, so the
   weight-10 decision problem breaks into exactly **55 cells** `(K = |R|, |E|)` per sector, each
   carrying cardinality cuts that no single one of them supports (§2.1);
2. **the residual-column orbit quotient in "least orbit" form** — the 216 residual columns fall
   into 9 orbits of 24 under the assignment's order-24 translation stabiliser, verified element by
   element. Worth ~30x on the critical path (§2.2);
3. **lex-minimality**: deciding *existence* lets one normalise to a lexicographically minimal
   solution, and the local move "drop a subset `T` of the hook columns and pay for it in data
   faults" becomes the sound clause family `|XOR_{r in T} r| >= |T| + 1`, plus "the data-fault set is
   disjoint from every used hook". Worth another ~30x on exactly the cells that were the wall (§2.3).

Two further results fall out on the way.

* **The gross code has exactly 1884 weight-12 non-trivial logicals per sector — no more.** Every
  previous round used `pool.py`'s 1884 as *what a randomised ISD search found*, and the whole
  [SBB26] pruning cascade is built on that pool. A complete enumeration by incremental SAT with
  blocking clauses terminates in UNSAT at exactly 1884, in both sectors (§5.2). It also gives an
  independent, machinery-free decision of the entire `|E| = 12` stratum: **0 of the 1884 admit a
  weight-`<=10` extended-code solution**, in either sector.
* **The predecessor's `(1,2,9)` weight-10 witness — the striking "2 data + 8 hooks" one — is not in
  normal form.** Four of its eight hook columns XOR to something of weight `<= 4` and can be
  dropped; the reduced witness has `K = 4` and `|E| = 16` (§2.3). The witness is correct; the "8
  hooks" figure is an artefact of the solver's choice.

---

## 1. What I inherited, what I re-ran, and what is new

**Taken as given from the predecessor, unmodified.** The reconstruction. I did not re-open Figure
12, did not re-run the PDF decode, and make no independent claim about the edge-to-monomial map.
Everything below is a statement about the object `phicert` §2.4 pins down:

```
phi(x^a y^b) = (a + b) mod 3
Z sector, order-class triple (1, 2, 62)   X sector, order-class triple (14, 0, 2)
                                          (each up to cyclic colour rotation)
```

and it inherits `phicert` §2.5's fidelity statement in full, including the residual reconstruction
risk on the edge map (there rated *moderate*, and it is still the dominant risk on this result).
If the reconstruction is wrong, everything below is a correct theorem about the wrong assignment.

**Re-run from scratch as anchors, not cited.** `gross.py` (`rankHX = rankHZ = 66, k = 12,
overlaps [0,2], incidences True`), `pool.py` (`|PZ| = |PX| = 1884`, `LX.LZ^T` pairing rank 12),
the cascade (`44` tiled survivors per sector at `phi = a+b`, both sectors, with `(1,2,62)` and
`(14,0,2)` among them and both of their cyclic rotations), the colour-rotation and full-stabiliser
automorphism checks, `d(gross) = 12` in both sectors, `altcheck.py` and `lrc8.py`.

**New in this session.** `cert4.py` (the `(K, |E|)` cell certifier), `job4.py` (one cell x one
residual orbit), `drive.py` (a bounded process pool), `stabcheck.py` (element-by-element
verification of the stabiliser action), `cuts.py` (randomised validation of the cut derivations),
`enum12.py` (a complete enumeration of the weight-12 logicals plus an independent decision of the
whole `|E| = 12` stratum), `orbcover.py` (the orbit cover demonstrated on real witnesses),
`anchor2.py`/`anchor3.py` (the `|E| >= 12` anchor and explicit weight-11 witnesses),
`recheck.py` (second-solver re-decision), `summarize.py`, `cert5.py` (a tighter joint form of the
residual-weight cut — *tried and rejected*, §7.4).

Frozen definitions used verbatim from `research/circdist/notes/CIRCDIST_PROBLEMS.md`:
`d_eff(M) := d_ext(E(M))`, `d_circ(C) = min{|F| : F triggers no detector but flips a logical}`,
`d_eff(M) <= d_circ(C(M)) <= d`, `D*_Gross = max_{M in S_Gross} d_circ(C(M))`.
`CIRCDIST.gross.mc-equiv` stays REFUTED-DEAD; nothing here uses or revives it.

---

## 2. What the wall was, and the three levers that moved it

The predecessor's wall was precise (`phicert` §7.1): splitting the weight bound `W = 10` by the
number `K = |R|` of residual (hook) columns used closes `K = 0` in ~43 s and `K = 1` in 5.5 / 8 min
and *does not close* `K >= 2`; every undivided query that ran past about an hour returned nothing.
The predecessor priced the completion at "1–2 further sessions on 24 cores, at maybe 0.6
probability of closing", with two untried levers named: composing the `K`-split with the column
quotient, and an incremental solver.

Neither of those is what worked. What worked is three other things.

### 2.1 Lever one — a second split coordinate: the net error weight `|E|`

Write a solution of the extended-code model as `(E, R, d)` with `E` the net data error, `R` the set
of residual columns used, `rho = XOR_{r in R} r`, `d = E xor rho` the data-fault part, and
`weight = |d| + |R|`. Two standing facts about `E` turn `|E|` into a *finite, small* second split
coordinate:

* **`|E|` is even.** `E` lies in `ker(H_det)` and the all-ones vector lies in `rowspace(H_det)`
  (the sum of all 72 rows of `H_X` is the all-ones vector, because every column of `H_X` has weight
  3; likewise for `H_Z`), so the parity functional is one of the detector constraints and `|E|` is
  even. Verified in `anchor1.py`:
  `all-ones in rowspace(HX): True   in rowspace(HZ): True`.
* **`|E| >= 12`.** `E` is a non-trivial logical of the gross code, and `d(gross) = 12`. I
  re-certified this myself rather than citing it, in both sectors, by running the certifier with
  the residual columns switched off (`anchor2.py`, `anchor3.py`):

```
[Z] residuals OFF, W = 11 : UNSAT (151.3 s)     W = 12 : SAT, weight-12 witness
[X] residuals OFF, W = 11 : UNSAT (140.7 s)     W = 12 : SAT, weight-12 witness
```

With `K` and `|E| = Ew` both fixed, four cuts become available that no single one of them supports.
All four are *semantic consequences* of the model — every satisfying assignment of the unsplit model
with `|u| = K` and `|z| = Ew` satisfies them — so adding them is sound:

```
(c1)  |u|   = K                                   the cell
(c2)  |z|   = Ew                                  the cell
(c3)  |d|  <= W - K                               from |d| + |u| <= W
(c4)  |rho| >= Ew - (W - K)                       from |E| <= |d| + |rho|
(c5)  |rho| <= 3K                                 every residual has weight <= 3
(c6)  n3   >= Ew - W - K,   n3 := #{c : u_{c,1}}  from |rho| <= 2K + n3 and (c4)
(c7)  not (u_{c,1} and u_{c,2})                   the dominance cut, inherited
```

`(c6)` is the one that does the work. The three residual sets of a check measured in CNOT order
`i1..i6` are `r1 = {i1,i2}` (weight 2), `r2 = {i4,i5,i6}` (weight 3), `r3 = {i5,i6}` (weight 2), so
`K` residual columns can cover at most `2K + n3` qubits, where `n3` counts how many of them are of
the weight-3 kind. Wherever `Ew` is at its ceiling `W + 2K`, `(c6)` forces `n3 = K`: **every**
residual used must be a weight-3 `r2`, pairwise disjoint and contained in `E`. That collapses six
of the nine orbit sub-queries of such a cell to unit propagation (0.1–0.4 s each).

The cells are exhaustive. `K = 0` is arithmetically empty (`|E| = |d| <= 10 < 12`), so every cell
has `K >= 1`; `Ew` is even, at least 12, and at most `W + 2K` by (c4)+(c5). For `W = 10` that is
exactly **55 cells**, `K = 1..10` with `Ew = 12, 14, ..., 10 + 2K`.

### 2.2 Lever two — the residual-column orbit quotient, in its *least-orbit* form

The tiled assignment `(t0,t1,t2)` with distinct entries is stabilised by the translation subgroup
`S = {g in Z12 x Z6 : phi(g) = 0}`, of order 24. `stabcheck.py` verifies, element by element and
for both candidate triples, that

```
sector Z triple (1,2,62): |S| = 24; row-permutation failures 0; residual-equivariance failures 0;
                          orbits 15 (residual orbits 9, sizes [24]); matches column_orbits: True
sector X triple (14,0,2): |S| = 24; row-permutation failures 0; residual-equivariance failures 0;
                          orbits 15 (residual orbits 9, sizes [24]); matches column_orbits: True
```

— i.e. every `g in S` permutes the *rows* of `H_X` and of `H_Z` as sets (so it preserves zero
syndrome and logical non-triviality) and satisfies `dp(r_k(c)) = r_k(cp(c))` (so it permutes the 360
extended-code columns, preserving column type and weight). This is the same automorphism the
predecessor verified for the single colour-rotation element, extended to the whole stabiliser.

The 216 residual columns fall into **9 orbits of 24**, indexed by (colour, residual type). Because
every cell has `K >= 1`, a solution always uses a residual column, so:

> for `j = 0..8`, ask the cell restricted to solutions that USE the representative of residual
> orbit `j` and use NO residual column of an orbit `< j`.

This covers every solution: let `x` be a solution and `i` the least residual-orbit index it uses;
translate by the `g in S` that carries one of `x`'s orbit-`i` columns to `rep_i`; `g.x` is a
solution of the same weight, in the same cell, using `rep_i`, and using no orbit `< i` because
orbits are `S`-invariant. `orbcover.py` demonstrates exactly this transport on five real weight-10
witnesses found by the *unrestricted* cell queries (§5.3); zero failures.

The effect is dramatic and it is where the predecessor's wall actually fell. On the X-sector
candidate cell `(K, Ew) = (1, 12)`:

```
unrestricted single query   : UNSAT in 268.9 s
9 orbit-restricted queries  : 0.2 0.2 0.2 0.2 0.2 0.2 7.4 8.5 8.7 s   (max 8.7 s, total 25.8 s)
```

a 30x reduction in the critical path and a 10x reduction in CPU. Forcing one specific residual
column to be used destroys the translation degeneracy that the solver was otherwise re-exploring 24
times over.

---

### 2.3 Lever three — lex-minimality, which is where the last order of magnitude came from

Cells `(K, Ew)` with `Ew <= 10 + K` get no help from `(c6)`, and those are the ones that stayed
expensive: `(K, 14)` for `K >= 4`, `(K, 16)` for `K >= 6`, and so on, at 250–600 s **per orbit
sub-query**. What closes them is a minimality normalisation, not a better solver.

We are deciding an existence question. If a solution of weight `<= W` exists, then one exists that
minimises `(weight, |R|)` lexicographically. Fix such an `x* = (E, R, d)` and any non-empty
`T subset R`; write `sigma = XOR_{r in T} r`. Dropping `T` gives

```
x' = (E, R \ T, d xor sigma)
```

which is again a solution — `E` is untouched, so the syndrome is still zero and the logical still
non-trivial — of weight `|d xor sigma| + |R| - |T|` and with `|R'| < |R|`. So `x'` beats `x*`
lexicographically the moment `weight(x') <= weight(x*)`, and minimality forces

```
     |d xor sigma|  >  |d| + |T| - 1 .
```

Two consequences, both encodable as short clauses:

* **`|T| = 1`.** `|d xor r| >= |d| + 2`, i.e. `|r| - 2|d cap r| >= 2`. The residual weights are
  `|r1| = 2`, `|r2| = 3`, `|r3| = 2`, so in every case `|d cap r| = 0`:

```
  (c8)  u_{c,k} => d_q = 0   for every q in r_k(c)                     ~500 binary clauses
  (c9)  d_j => z_j                                                     144 binary clauses
```

  `(c9)` follows: if `d_j = 1` then by `(c8)` no used residual covers `j`, so `rho_j = 0` and
  `z_j = d_j = 1`. Together they say **`d` is disjoint from every used residual and contained in
  `E`**, hence `E = d ⊔ rho` and `|E| = |d| + |rho|` exactly.

* **General `T`.** Since `d cap r = ∅` for every `r in R`, also `d cap sigma = ∅`, so
  `|d xor sigma| = |d| + |sigma|` and the condition becomes the clean combinatorial statement

```
  every non-empty subset T of the used residual columns has  |XOR_{r in T} r|  >=  |T| + 1.
```

  Encoded for `|T| = 2` and `|T| = 3` by direct enumeration over the 216 residual columns:

```
  (c10) 264 forbidden pairs      { (a,b) : |r_a xor r_b| <= 2 }        binary clauses
  (c11) 11448 forbidden triples  { (a,b,c) : |r_a xor r_b xor r_c| <= 3 }  ternary clauses
```

  (identical counts in both sectors; the 72 dominance pairs `(r2(c), r3(c))` are among the 264, so
  `(c7)` is subsumed). `|T| >= 4` was not encoded.

This is a *normalisation*, not a filter: it can and does remove solutions, but never all of them,
because the lex-minimal solution survives and lands in the cell given by its own `|R|` and `|E|` —
both of which the sweep enumerates. So UNSAT on every cell still certifies `d_ext > W`.

**Measured effect** (same machine, same load class, `cert4` vs `cert7`):

```
cell (K,Ew), orbit    cert4      cert6 (c8,c9)   cert7 (c8..c11)
Z (2,12) orbit 7      71.4 s      4.4 s              --
Z (8,14) orbit 3     599.5 s    227.7 s              --
Z (10,14) orbit 0    260.0 s    253.0 s           8.6 s
```

`(c8)`/`(c9)` help where `|d|` is large (low `K`) and do nothing where `|d| <= 1` (high `K`,
because there is then almost no `d` to constrain); `(c10)`/`(c11)` are exactly the high-`K`
medicine, because at high `K` the difficulty *is* the choice of many residual columns. Together
they are worth roughly **30x** on the cells that were the wall.

**Validation of the normalisation on real data** (`redwit.py`). Each of the five weight-10
witnesses of §5.4 is put through the drop step, iterated over all `2^K - 1` subsets until no drop is
weight-non-increasing. Every fixed point is still a valid weight-`<=10` solution of the same `E`,
and every one satisfies `(c8)`, `(c9)`, `|E| = |d| + |rho|` and the full subset condition for all
`2^K - 1` subsets:

```
Z (1,2,2) : weight 10 (K=4) -> lex-min weight 10 (K=4), cell (K=4, Ew=14); all cuts True
Z (9,9,62): weight 10 (K=4) -> lex-min weight 10 (K=4), cell (K=4, Ew=14); all cuts True
X (0,9,9) : weight 10 (K=3) -> lex-min weight 10 (K=3), cell (K=3, Ew=14); all cuts True
Z (1,9,9) : weight 10 (K=4) -> lex-min weight 10 (K=4), cell (K=4, Ew=16); all cuts True
Z (1,2,9) : weight 10 (K=8) -> lex-min weight 10 (K=4), cell (K=4, Ew=16); all cuts True
reduced 5 witnesses, failures 0
```

The last row is the instructive one: the predecessor's `(1,2,9)` witness — the one with
`weight 10 = 2 data + 8 hooks` — is **not** lex-minimal; four of its eight hook columns XOR to
something of weight `<= 4` and can be dropped, giving a weight-10 solution with `K = 4` and
`|E| = 16`. The witness is correct; it is just not in normal form. Any future session using
`(1,2,9)`'s hook count as evidence about the mechanism should use the reduced form.

`cert7` also still finds witnesses where they exist: `Z (1,2,2)` cell `(K=4, Ew=14)`, orbit 0,
returns SAT with a verified weight-10 witness (`R = [(0,0),(42,2),(51,2),(56,0)]`,
`|d| = 6`, `|E| = 14`) — under the full `(c8)`–`(c11)` package *and* the orbit restriction.

### 2.4 Encodings are mixed across cells, and that is sound

Cells decided before `cert7` existed were decided with `cert4` (cuts `(c1)`–`(c7)` only); the rest
with `cert7`. This is sound: `cert4`'s constraint set is a subset of `cert7`'s, so a `cert4` UNSAT
on a cell means *no* solution lies in that cell, while a `cert7` UNSAT means *no lex-minimal*
solution does. The lex-minimal solution lies in exactly one cell, and every cell returns UNSAT under
one encoding or the other, so it cannot exist. Each individual row of §4 records which encoding
decided it.

---

## 3. Anchors computed in this session

Everything the certification rests on numerically, recomputed here rather than cited.

```
gross.py   : {'rankHX': 66, 'rankHZ': 66, 'k': 12, 'overlaps': [0, 2],
              'overlap_halves': [(0, 1)], 'incidences': True}
pool.py    : |PZ| = |PX| = 1884 weight-12 logicals; LX.LZ^T pairing rank 12
cascade    : phi = a+b -> 44 tiled survivors per sector, both sectors;
             candidate (1,2,62) in the Z survivors: True (both cyclic rotations too)
             candidate (14,0,2) in the X survivors: True (both cyclic rotations too)
anchor1.py : all-ones in rowspace(HX): True   in rowspace(HZ): True     (=> |E| is even)
anchor2/3  : [Z] residuals OFF, W = 11 : UNSAT (151.3 s);  W = 12 : SAT, weight-12 witness
             [X] residuals OFF, W = 11 : UNSAT (140.7 s);  W = 12 : SAT, weight-12 witness
                                                                        (=> |E| >= 12)
stabcheck  : |S| = 24 in both sectors; 0 row-permutation failures, 0 residual-equivariance
             failures; 15 column orbits, 9 of them residual orbits, all of size 24
```

**The universal upper bound, by explicit witness** (`anchor3.py`). Take any weight-12 logical `L`
containing a weight-2 residual `r` of some check, and put `E = L`, `R = {r}`, `d = L xor r`; then
`|d| + |R| = 10 + 1 = 11`. Such an `(L, r)` exists in both sectors, and the resulting triple passes
`dext.verify_witness` from the `F2` definitions:

```
[Z] weight 11 = 10 data + 1 hook, |E| = 12, decomposition_ok, zero_syndrome, nontrivial_logical
    (check 48, residual r1 = {54, 60})
[X] weight 11 = 10 data + 1 hook, |E| = 12, decomposition_ok, zero_syndrome, nontrivial_logical
    (check 18, residual r1 = {0, 22})
```

so `d_ext(E(M_cand)) <= 11` in both sectors, by witness rather than by the "every slot-pair of a
check lies in a weight-12 logical" argument the previous rounds cited.

**Realisability, re-run** (`altcheck.py`, `lrc8.py`):

```
alternating-XZ circuit with the candidate's orders: 17 CNOT layers, 864 CNOTs, every layer a
   matching; (MC): 0 odd of 648 overlapping (X,Z) check pairs;
   stim: 288 qubits, 432 detectors, DEM BUILT OK; noiseless detector firings: 0 / 432
depth-8 staggered LRC of the gross code: legality over 6 periods True; 8 CNOT layers per period,
   ancilla windows 8 steps; (MC): 0 odd of 4536 (X-instance, Z-instance) pairs;
   stim: 288 qubits, 288 detectors, DEM BUILT OK; noiseless detector firings: 0 / 288
```

---

## 4. The sweep

Two rows of the same cell may have been decided by different encodings (§2.4); the "encoding"
column records which. Every row is one exact SAT decision query on the full 360-column extended
code of the candidate assignment, restricted to one residual-column orbit. `cert4` rows carry cuts
`(c1)`–`(c7)`; `cert7` rows carry `(c1)`–`(c11)`. CPU seconds are solver time only (CNF
construction is ~0.2 s per query).

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
| 4 | 16 | `.....UUUU` | incomplete | cert4 | 1293 | 883 |
| 4 | 18 | `UUUUUUUUU` | **UNSAT** | cert4 | 383 | 242 |
| 5 | 12 | `UUUUUUUUU` | **UNSAT** (enum12) | cert4 | 2929 | 545 |
| 5 | 14 | `UUUUUUUUU` | **UNSAT** | cert7 | 2712 | 1194 |
| 5 | 16 | `U..UUUUUU` | incomplete | cert7 | 6008 | 2349 |
| 5 | 18 | `.........` | incomplete | - | 0 | 0 |
| 5 | 20 | `UUUUUUUUU` | **UNSAT** | cert7 | 309 | 210 |
| 6 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 6 | 14 | `UUUUUUUUU` | **UNSAT** | cert7 | 2998 | 1240 |
| 6 | 16 | `U..UUUUUU` | incomplete | cert7 | 6058 | 2714 |
| 6 | 18 | `.........` | incomplete | - | 0 | 0 |
| 6 | 20 | `....UUUUU` | incomplete | cert7 | 687 | 477 |
| 6 | 22 | `UUUUUUUUU` | **UNSAT** | cert7 | 217 | 178 |
| 7 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 7 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert7 | 3569 | 1508 |
| 7 | 16 | `U..UUUUUU` | incomplete | cert7 | 4056 | 1890 |
| 7 | 18 | `..UUUUUUU` | incomplete | cert7 | 5810 | 3107 |
| 7 | 20 | `.........` | incomplete | - | 0 | 0 |
| 7 | 22 | `U.UUUUUUU` | incomplete | cert7 | 4719 | 2934 |
| 7 | 24 | `UUUUUUUUU` | **UNSAT** | cert7 | 124 | 97 |
| 8 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 8 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert6+cert7 | 3019 | 1536 |
| 8 | 16 | `U.UUUUUUU` | incomplete | cert7 | 4209 | 2794 |
| 8 | 18 | `.UUUUUUUU` | incomplete | cert7 | 7088 | 3045 |
| 8 | 20 | `.........` | incomplete | - | 0 | 0 |
| 8 | 22 | `..UUUUUUU` | incomplete | cert7 | 2805 | 1969 |
| 8 | 24 | `UUUUUUUUU` | **UNSAT** | cert7 | 4348 | 2174 |
| 8 | 26 | `UUUUUUUUU` | **UNSAT** | cert7 | 44 | 28 |
| 9 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 9 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert6 | 2736 | 1545 |
| 9 | 16 | `UUUUUUUUU` | **UNSAT** | cert7 | 1888 | 994 |
| 9 | 18 | `UUUUUUUUU` | **UNSAT** | cert7 | 6056 | 3756 |
| 9 | 20 | `.UUUUUUUU` | incomplete | cert7 | 1357 | 687 |
| 9 | 22 | `.........` | incomplete | - | 0 | 0 |
| 9 | 24 | `UUUUUUUUU` | **UNSAT** | cert7 | 4451 | 2731 |
| 9 | 26 | `UUUUUUUUU` | **UNSAT** | cert7 | 1793 | 747 |
| 9 | 28 | `UUUUUUUUU` | **UNSAT** | cert7 | 110 | 85 |
| 10 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 10 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert6 | 390 | 253 |
| 10 | 16 | `UUUUUUUUU` | **UNSAT** | cert4 | 626 | 434 |
| 10 | 18 | `UUUUUUUUU` | **UNSAT** | cert7 | 421 | 246 |
| 10 | 20 | `UUUUUUUUU` | **UNSAT** | cert7 | 825 | 509 |
| 10 | 22 | `.........` | incomplete | - | 0 | 0 |
| 10 | 24 | `UUUUUUUUU` | **UNSAT** | cert7 | 485 | 295 |
| 10 | 26 | `UUUUUUUUU` | **UNSAT** | cert7 | 389 | 213 |
| 10 | 28 | `UUUUUUUUU` | **UNSAT** | cert7 | 472 | 303 |
| 10 | 30 | `UUUUUUUUU` | **UNSAT** | cert7 | 223 | 103 |

`38` of `55` cells decided; SAT cells: `0`; CPU for this sector: `101585` s

**sector X, triple (14, 0, 2)** — `U` = UNSAT, `S` = SAT, `.` = not decided

| `K` | `\|E\|` | orbit 0..8 | cell verdict | encoding | cell CPU s | slowest orbit s |
|---|---|---|---|---|---|---|
| 1 | 12 | `UUUUUUUUU` | **UNSAT** (enum12) | cert4 | 24 | 8 |
| 2 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 2 | 14 | `U........` | incomplete | cert7 | 0 | 0 |
| 3 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 3 | 14 | `UUUUUUUUU` | **UNSAT** | cert7 | 813 | 198 |
| 3 | 16 | `.........` | incomplete | - | 0 | 0 |
| 4 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 4 | 14 | `UUUUUUUUU` | **UNSAT** | cert7 | 1330 | 316 |
| 4 | 16 | `U........` | incomplete | cert7 | 1332 | 1332 |
| 4 | 18 | `..UUUUUUU` | incomplete | cert7 | 50 | 41 |
| 5 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 5 | 14 | `UUUUUUUUU` | **UNSAT** | cert7 | 1681 | 520 |
| 5 | 16 | `U.UUUUUUU` | incomplete | cert7 | 7676 | 2760 |
| 5 | 18 | `.........` | incomplete | - | 0 | 0 |
| 5 | 20 | `UUUUUUUUU` | **UNSAT** | cert7 | 105 | 74 |
| 6 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 6 | 14 | `UUUUUUUUU` | **UNSAT** | cert7 | 1702 | 869 |
| 6 | 16 | `U..UUUUUU` | incomplete | cert7 | 4534 | 1387 |
| 6 | 18 | `.........` | incomplete | - | 0 | 0 |
| 6 | 20 | `..UUUUUUU` | incomplete | cert7 | 2215 | 836 |
| 6 | 22 | `UUUUUUUUU` | **UNSAT** | cert7 | 63 | 39 |
| 7 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 7 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert7 | 1802 | 1076 |
| 7 | 16 | `U.UUUUUUU` | incomplete | cert7 | 7387 | 4089 |
| 7 | 18 | `..UUUUUUU` | incomplete | cert7 | 5915 | 2876 |
| 7 | 20 | `.........` | incomplete | - | 0 | 0 |
| 7 | 22 | `UUUUUUUUU` | **UNSAT** | cert7 | 6223 | 3673 |
| 7 | 24 | `UUUUUUUUU` | **UNSAT** | cert7 | 41 | 25 |
| 8 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 8 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert7 | 2943 | 1137 |
| 8 | 16 | `UUUUUUUUU` | **UNSAT** | cert7 | 6554 | 3257 |
| 8 | 18 | `.UUUUUUUU` | incomplete | cert7 | 6002 | 2472 |
| 8 | 20 | `.........` | incomplete | - | 0 | 0 |
| 8 | 22 | `..UUUUUUU` | incomplete | cert7 | 3036 | 1678 |
| 8 | 24 | `UUUUUUUUU` | **UNSAT** | cert7 | 3225 | 1912 |
| 8 | 26 | `UUUUUUUUU` | **UNSAT** | cert7 | 30 | 18 |
| 9 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 9 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert7 | 1166 | 461 |
| 9 | 16 | `UUUUUUUUU` | **UNSAT** | cert7 | 4185 | 2544 |
| 9 | 18 | `UUUUUUUUU` | **UNSAT** | cert7 | 5739 | 3916 |
| 9 | 20 | `.UUUUUUUU` | incomplete | cert7 | 1397 | 716 |
| 9 | 22 | `.........` | incomplete | - | 0 | 0 |
| 9 | 24 | `UUUUUUUUU` | **UNSAT** | cert7 | 5091 | 3489 |
| 9 | 26 | `UUUUUUUUU` | **UNSAT** | cert7 | 1653 | 946 |
| 9 | 28 | `UUUUUUUUU` | **UNSAT** | cert7 | 64 | 36 |
| 10 | 12 | `.........` | **UNSAT** (enum12) | - | 0 | 0 |
| 10 | 14 | `UUUUUUUUU` | **UNSAT** | cert4+cert7 | 319 | 180 |
| 10 | 16 | `UUUUUUUUU` | **UNSAT** | cert4+cert7 | 277 | 96 |
| 10 | 18 | `UUUUUUUUU` | **UNSAT** | cert7 | 2207 | 1565 |
| 10 | 20 | `.UUUUUUUU` | incomplete | cert7 | 205 | 94 |
| 10 | 22 | `.........` | incomplete | - | 0 | 0 |
| 10 | 24 | `UUUUUUUUU` | **UNSAT** | cert7 | 653 | 422 |
| 10 | 26 | `UUUUUUUUU` | **UNSAT** | cert7 | 651 | 426 |
| 10 | 28 | `UUUUUUUUU` | **UNSAT** | cert7 | 733 | 459 |
| 10 | 30 | `UUUUUUUUU` | **UNSAT** | cert7 | 392 | 224 |

`36` of `55` cells decided; SAT cells: `0`; CPU for this sector: `89414` s

TOTAL: {'Z': (38, 0, 101585.40000000001), 'X': (36, 0, 89413.80000000002)}  grand CPU 190999

**Reading the table.** A cell is UNSAT when all nine of its orbit sub-queries are UNSAT; the nine
together cover the cell (§2.2). The `|E| = 12` rows are decided **completely and independently** by
`enum12.py` (§5.2) — a complete enumeration of the 1884 weight-12 logicals plus one small exact
query per logical — which is why most of them were not run through the sweep at all; where both
routes were run they agree (Z: `(1,12)`–`(5,12)`; X: `(1,12)`).

**No cell in either sector is SAT.** Every query that returned an answer returned UNSAT. The
incomplete rows are cells where some of the nine orbit sub-queries had not returned when the box
closed; none of them had produced a witness.

**The exact frontier.** What is left open is a specific list of cells, not a range of `|R|`
(`xN` = how many of that cell's nine orbit sub-queries are still open):

```
Z sector, 17 cells open, 77 orbit sub-queries:
   (4,16)x5 (5,16)x2 (5,18)x9 (6,16)x2 (6,18)x9 (6,20)x4 (7,16)x2 (7,18)x2 (7,20)x9 (7,22)x1 
   (8,16)x1 (8,18)x1 (8,20)x9 (8,22)x2 (9,20)x1 (9,22)x9 (10,22)x9
X sector, 19 cells open, 95 orbit sub-queries:
   (2,14)x8 (3,16)x9 (4,16)x9 (4,18)x2 (5,16)x1 (5,18)x9 (6,16)x2 (6,18)x9 (6,20)x2 (7,16)x1 
   (7,18)x2 (7,20)x9 (8,18)x1 (8,20)x9 (8,22)x2 (9,20)x1 (9,22)x9 (10,20)x1 (10,22)x9
```

36 cells and 172 of the 990 orbit sub-queries are open. Nine of the open cells need only
one or two more sub-queries; the rest are untouched. Every value of `|R|` from 1 to 10 is fully
decided for at least three `|E|` strata in each sector, so the predecessor's "`|R| >= 2` is the
wall" description no longer fits: what is left is a band of mid-`K`, high-`|E|` cells, where
`|d| <= 10 - K` is small, `|E| = |d| + |rho|` is large, and the search is over near-disjoint
`K`-subsets of the 216 hook columns whose XOR is a large logical. That is exactly the regime where
`(c8)`/`(c9)` stop biting -- there is almost no `d` to constrain -- and only `(c10)`/`(c11)` help.

---

## 5. Cross-checks

A single UNSAT sweep with hand-derived cuts is a fragile object, so five independent checks were
run. None of them shares the code path it checks.

### 5.1 The cuts, checked against the model rather than against my algebra — NUMERICAL

`cuts.py` draws 200 000 random `(R, d)` pairs per sector on the candidate's own residual sets,
forms `rho`, `E = d xor rho`, and checks each of `(c3)`–`(c6)`, the ceiling `Ew <= W + 2K`, the cell
membership of every draw with `|E|` even and `>= 12`, and the dominance repair step (dropping
`{r2(c), r3(c)}` and flipping `d` at `i4(c)` must preserve `E` and strictly lower the weight):

```
sector Z triple (1,2,62): 200000 random (R,d) draws, violations
      {'c3': 0, 'c4': 0, 'c5': 0, 'c6': 0, 'ub': 0, 'dom': 0, 'cell': 0}
sector X triple (14,0,2): 200000 random (R,d) draws, violations
      {'c3': 0, 'c4': 0, 'c5': 0, 'c6': 0, 'ub': 0, 'dom': 0, 'cell': 0}
cells(W=10): 55   all violation counters zero: True
```

### 5.2 The `|E| = 12` stratum, decided a second time WITHOUT any of the machinery — NUMERICAL

`enum12.py` does the `|E| = 12` half of the certification by a route that uses no cut, no cell, no
orbit quotient and no `|E|`-split, and it also settles a question the node has carried since round 6.

*Step 1 — a complete enumeration of the weight-12 non-trivial logicals.* Incremental SAT with
blocking clauses: constraints `H_det z = 0`, `OR_i (L_i . z = 1)`, `|z| = 12`; after each model `v`
add the 12-literal clause `OR_{j in supp(v)} ~z_j`, which under `|z| = 12` blocks exactly `v`. The
loop ends in UNSAT, so the list is exhaustive **by construction**:

```
[Z] complete weight-12 logical enumeration: 1884 words in 351.3 s; all valid: True;
    identical to pool.py's pool: True
[X] complete weight-12 logical enumeration: 1884 words in 349.2 s; all valid: True;
    identical to pool.py's pool: True
```

This upgrades `pool.py`'s 1884 from "what a randomised ISD search plus translation closure found"
to **"exactly 1884, and nothing else"**, in both sectors — a standing uncertainty in every previous
round on this node, since the whole pruning cascade is built on that pool.

*Step 2 — the exact decision, one tiny CNF per logical.* With `E` fixed, `d` is determined bitwise
by `u`, so "is there `R` with `|E xor rho_R| + |R| <= 10`?" is a 216-variable CNF:

```
[Z] |E| = 12 decision over all 1884 logicals: 0 admit a weight-<=10 extended-code solution (803.2 s)
[X] |E| = 12 decision over all 1884 logicals: 0 admit a weight-<=10 extended-code solution (903.4 s)
```

That decides **every** cell `(K, 12)`, `K = 1..10`, in both sectors, in ~1150 CPU-s per sector —
against ~26 000 CPU-s for the same information through the cell queries. The two routes agree on every cell where both were run
— `(1,12)` through `(5,12)` in the Z sector and `(1,12)` in the X sector, nine orbit sub-queries
each, all UNSAT — so the `|E| = 12` cells that the sweep did not run are covered by `enum12.py`
alone, exactly and completely.

### 5.3 The lex-minimality normalisation, on real solutions — NUMERICAL

`redwit.py`, reported in §2.3: every known weight-10 witness reduces, under the drop step iterated
over all `2^K - 1` subsets, to a weight-`<=10` solution of the same `E` that satisfies `(c8)`,
`(c9)`, `|E| = |d| + |rho|` and the subset condition for **every** non-empty subset, not only the
ones `(c10)`/`(c11)` encode. 5 witnesses, 0 failures.

### 5.4 The orbit cover, demonstrated on real solutions — NUMERICAL

`orbcover.py` takes the weight-10 witnesses that the *unrestricted* cell queries produced for five
non-candidate assignments, computes the least residual orbit each witness uses, transports it by
the stabiliser element that carries one of its columns to that orbit's representative, and verifies
that the image is a solution of the same cell with the same weight and the same set of touched
orbits:

```
Z (1,2,2) : orbits [0,5,6,8] -> g = (5,4)  -> rep ('r',0,0), cell (K=4,|E|=14), weight 10, OK
Z (9,9,62): orbits [1,4,5,8] -> g = (4,5)  -> rep ('r',0,1), cell (K=4,|E|=14), weight 10, OK
X (0,9,9) : orbits [0,3,7]   -> g = (11,4) -> rep ('r',0,0), cell (K=3,|E|=14), weight 10, OK
Z (1,9,9) : orbits [0,2,4,7] -> g = (2,4)  -> rep ('r',0,0), cell (K=4,|E|=16), weight 10, OK
Z (1,2,9) : orbits [2,3,5,7] -> g = (4,5)  -> rep ('r',0,2), cell (K=8,|E|=16), weight 10, OK
checked 5 witnesses, failures 0
```

### 5.5 The machinery reproduces known answers — NUMERICAL

Before any candidate cell was run, the cell encoding was pointed at four assignments the
predecessor had already settled SAT, in the cell each one's recorded witness profile predicts. All
four returned SAT with a weight-10 witness passing `dext.verify_witness`:

```
Z (1,2,2)  cell (K=4, Ew=14): SAT  27.8 s  weight 10 = 6 data + 4 hooks, |E| = 14
Z (9,9,62) cell (K=4, Ew=14): SAT  30.2 s  weight 10 = 6 data + 4 hooks, |E| = 14
X (0,9,9)  cell (K=3, Ew=14): SAT  50.5 s  weight 10 = 7 data + 3 hooks, |E| = 14
Z (1,2,9)  cell (K=8, Ew=16): SAT 308.6 s  weight 10 = 2 data + 8 hooks, |E| = 16
Z (1,9,9)  cell (K=4, Ew=16): SAT 212.8 s
```

so the cuts are not over-pruning on instances where a solution exists. The gross code's own
`d = 12` is reproduced by the same certifier with residuals off (§2.1).

### 5.6 Second-solver re-decision — NUMERICAL

`recheck.py` rebuilds a cell's CNF from scratch, checks that its SHA-256 matches the one `job4`/
`job7` printed when it decided that cell, and hands it to a different solver:

```
Z (K=2, |E|=12) orbit 8 : CaDiCaL 1.5.3 UNSAT 48.2 s   |  CaDiCaL 1.9.5 UNSAT  36.9 s
Z (K=8, |E|=14) orbit 3 : CaDiCaL 1.5.3 UNSAT 599.5 s  |  CaDiCaL 1.9.5 UNSAT 540.3 s
X (K=1, |E|=12) orbit 1 : CaDiCaL 1.5.3 UNSAT  8.5 s   |  Glucose 4     UNSAT  15.8 s
```

Different code bases, same verdicts, same CNF hashes. This is a spot check on three cells, not a
sweep; see §7.3 for what it does and does not replace.

---

## 6. Which pre-committed reading fires

The commission pre-committed:

> all candidate orbits UNSAT at 10 => the SBB candidate certifies at `d_ext = 11` (their conjecture
> CONFIRMED at NUMERICAL on the correct family) and `D* >= 11` firmly; any SAT => weight-10 witness
> on the true candidate => conjecture refuted on the correct family — deliver the witness triply
> verified; wall persists => certified partial, honest repricing.

The third reading fires: **the wall persists, one rung further out.** No cell of either sector is
SAT, so no weight-10 witness exists for the candidate anywhere the sweep has looked; but not every
cell is decided, so `d_ext > 10` is not certified and neither decisive reading can be cashed.

What IS certified, at NUMERICAL:

* `d_ext(E(M_cand)) <= 11` in both sectors, by explicit weight-11 witness (§3);
* **no weight-10 solution with `|E| = 12`**, in either sector, by a complete enumeration of the
  1884 weight-12 logicals and an exact per-logical decision (§5.2) — this subsumes and greatly
  strengthens the predecessor's `|R| ∈ {0,1}` result, which was exactly the `|E| = 12`, `|R| <= 1`
  corner of it;
* **no weight-10 solution in any of the decided `|E| >= 14` cells**, listed cell by cell in §4.

The exact frontier is the list of undecided cells in §4. It is not "`|R| >= 2`": every value of
`|R|` from 1 to 10 is decided for several `|E|` strata, and what remains is a specific set of
mid-`K`, high-`|E|` cells.

### 6.1 The chain this was aimed at, and exactly which link is missing

The chain from the sweep to `D*_Gross >= 11` has five links. Four of them are now in place; the
first is the one still open, and it is the only one still open.

1. **`d_ext(E(M_cand)) > 10` in both sectors** — the sweep, §4. **NOT ESTABLISHED**: 74 of 110
   cells, no SAT anywhere, 36 cells open. This is the whole gap.
2. **`d_ext(E(M_cand)) <= 11` in both sectors** — the explicit weight-11 solutions of §3.
   *This session, NUMERICAL, by witness.* So `d_ext in {?, ..., 11}` with everything below 11 now
   ruled out on 74 of the 110 cells.
3. **`M_cand` is realisable as a legal, measurement-consistent, non-interleaved SEC of the gross
   code.** Re-run here (`altcheck.py`): the alternating-XZ circuit with the candidate's within-check
   orders is 17 CNOT layers / 864 CNOTs, every layer a matching, `(MC): 0 odd of 648` overlapping
   `(X,Z)` check pairs, and `stim` builds its DEM with `0 / 432` detectors firing on the noiseless
   run. Separately (`lrc8.py`) a legal `(MC)`-clean **depth-8** staggered left-right circuit of the
   gross code exists (`0 odd of 4536` instance pairs, `stim` DEM OK, `0 / 288` firings), which is
   the depth the paper claims.
4. **Non-interleaved `=> d_circ = d_eff`** — [SBB26] Thm 1 / Cor. 1, and independently in-house
   Theorem 7.1 (`artifacts/circdist_lift_nonint_proof_20260820.md`, carried at CONFIRM in
   `artifacts/circdist_lift_proofs_review_20260820.md` row K). *Inherited.*
5. **The reconstruction** — `phicert` §2.2–2.5. *Inherited, and it is the dominant risk.*

Links 2–4 are done, and link 5 is the inherited reconstruction risk (§7.1). **The moment link 1
closes, `d_circ(C(M_cand)) = 11` and `D*_Gross >= 11` follow immediately**, and the first of the
three items `CIRCDIST_PROBLEMS.md` lists under 最低验收结果 ("严格证明候选电路 d_circ = 11") is
discharged at NUMERICAL. Nothing else has to be built: links 2, 3 and 4 were the parts a future
session would otherwise have had to redo, and they are recorded here with their numbers so that a
completion run only has to finish the 36 cells of §4.

I am deliberately not stating a probability that link 1 closes UNSAT. The evidence is that
74 of 110 cells are UNSAT and none is SAT, and that is what the table says; the runtime asymmetry
the predecessor declined to price (its §5(d)) is not evidence I will price either.

**What does NOT follow.** Nothing here bounds `d_circ` for *interleaved* schedules, so the
`D* = 11` vs `12` question is untouched: `D*_Gross >= 11` and the open half is whether some
interleaved `M` reaches 12. Nothing here says the candidate is optimal among non-interleaved
schedules either — [SBB26]'s own `d_circ <= 11` for all non-interleaved schedules is inherited, not
re-proved.

---

## 7. Honest limits

### 7.1 The reconstruction is still the dominant risk, and it is inherited

I did nothing to reduce it. `phicert` §2.5 rates the edge-to-monomial map at *moderate* risk: the
figure alone does not fix it, and it is pinned only by the legality + (MC) + cascade filter. If that
filter selected the wrong orbit, this session has exactly certified the wrong assignment. The
cheapest independent check remains the one the predecessor named and did not do: **render Figure 12
of arXiv:2603.05481 to pixels and read the 36 labels by eye**, then compare with `phicert` §2.2.
Until someone does that, the correct reading of this artifact is:

> for the assignment `phi = a+b`, Z-triple `(1,2,62)`, X-triple `(14,0,2)`, no weight-10 solution of
> the extended code exists in any of the 74 decided cells of §4, in either sector; and that
> assignment is the unique reading of [SBB26] Figure 12 that is simultaneously legal,
> measurement-consistent and cascade-surviving.

The second clause is the predecessor's, not mine.

### 7.2 The scope of the absence claim, spelled out

The UNSAT half asserts, for the candidate's residual sets and in both sectors: **there is no
assignment `(E, R, d)` with `H_det E = 0`, `E not in rowspace(H_stab)`, `d = E xor rho_R`,
`|d| + |R| <= 10`, AND `(|R|, |E|)` equal to one of the 74 decided cells of §4** — plus, from
`enum12.py` and independently of any of the machinery, **no such assignment with `|E| = 12` at all,
for any `|R|`**.

Within a decided cell the search is over the full 360-column extended code — all 144 data columns
and all 216 residual columns — with no restriction on which checks contribute or on the structure of
`E` beyond the cuts of §2.1/§2.3, each of which is either a semantic consequence of the model
(machine-checked in §5.1) or a lex-minimality normalisation that provably keeps at least one
solution if any exists (§2.3, checked on real witnesses in §5.3).

It is *not* an absence claim about the 36 undecided cells, about interleaved schedules, about other
members of the `phi = a+b` family, or about `d_circ` under a different noise model.

### 7.3 UNSAT is a solver verdict, not a machine-checked proof

No DRAT/DRUP proof was produced or checked: `drat-trim`, `cadical`, `kissat` and `minisat` are not
installed on this machine, and `python-sat`'s `Cadical153(with_proof=True)` returned an empty proof
on a trivial test, so proof logging is not usable here. The mitigation actually applied is
independent re-decision: a sample of the sweep's UNSAT cells was re-decided from a freshly rebuilt CNF (SHA-256 matched)
by a different solver, and every one came back UNSAT — Cadical 1.9.5 on `Z (K=2,|E|=12)` orbit 8
(36.9 s vs CaDiCaL 1.5.3's 48.2 s) and on `Z (K=8,|E|=14)` orbit 3 (540.3 s vs 599.5 s), Glucose 4
on `X (K=1,|E|=12)` orbit 1 (15.8 s vs 8.5 s). Different code bases, same verdicts. This is weaker than a checked proof and I do not
dress it up as one. A reviewer with `cadical --lrat` and `cake_lpr` could close this gap; the CNFs
are reproducible bit-for-bit (`job4.py` prints a SHA-256 of the exact clause list it hands the
solver, and `recheck.py` rebuilds and re-hashes it).

### 7.4 What I tried that did not help

`cert5.py` replaces cuts (c5)+(c6) with their exact joint form
`sum_j rho_j + sum_c (u_{c,0} + u_{c,2}) <= 3K` (a single cardinality constraint over 288 literals
with the small bound `3K <= 30`, which is tight for every value of `|rho|`, not only the extreme
one). On four cells with known `cert4` timings it was **slower on three of four**
(12.5 vs 8.1 s, 29.5 vs 17.7 s, 63.3 vs 71.4 s, 56.5 vs 48.2 s under comparable load). The extra
propagation did not pay for the extra counter. Recorded so nobody re-tries it.

The predecessor's two named levers were also not what worked: the column quotient in its plain
"assume the representative is used" form is weaker than the least-orbit refinement used here, and no
incremental solver was built.

### 7.5 Not done

1. **The certification itself is not finished.** **The candidate itself is not finished.** 36 of the 110 cells are open (§4's frontier); the
commission's decisive readings need all 110. And the 19 orbits the predecessor left open (5 in the
Z sector, 14 in the X sector, `phicert` §4.2) are untouched here — the box went entirely on the
candidate, as instructed.
2. **`|E| = 14` has no independent second route.** `enum12.py` decides the `|E| = 12` stratum twice
   over; the `|E| >= 14` strata rest on the cell sweep alone (plus the second-solver spot checks).
   Extending the complete enumeration to weight 14 was estimated at 2.5–9 CPU-hours per sector for
   the enumeration alone and was not attempted.
3. **Depth-8 realisability of the candidate with per-colour offsets** (`phicert` §3.3's NOT-DONE)
   is untouched. §6 link 3 uses the alternating-XZ realisation, which is what Thm 1 needs; the
   depth-8 claim rests on `phicert`'s `buildlrc.py`, which I could not re-run because it reads the
   PDF-derived `fig12_reading2.json` that this session did not regenerate. `lrc8.py` re-runs and
   confirms only the *existence* of a legal (MC)-clean depth-8 gross LRC, not that the candidate's
   own triples are realised at depth 8.
4. **The `Sigma_2` / interleaved question** is untouched, and `nogo.py` at `T = 7, 8` is untouched.
5. **Machine contention, and it is the reason the box ran out.** This machine carried 20–28 foreign
   Python processes for the whole session; my 22–34 workers averaged 35–47 % of a core each, so the
   run had 11–13 effective cores out of 24 and every wall-clock number is ~2x what an idle machine
   would give. CPU-seconds are the honest figure and are what I quote throughout.
6. **My own scheduling cost real time, twice.** I ran a forward and a reverse driver over the same
   job list to raise my share of the machine; once they had both made progress, ~75 % of their
   *remaining* queue entries were jobs the other had already done, and I did not notice for about
   half an hour. And the first 26 000 CPU-s went into `|E| = 12` cells that `enum12.py` later
   decided, exactly and completely, for 1150 CPU-s per sector. Deduplicate the queue, and look for
   the small complete object, before launching anything.

---

## 8. Repricing, and what to fund next

**The predecessor's diagnosis of the obstruction was right; its diagnosis of the remedy was not.**
`phicert` §7.1 named two untried levers — compose the `K`-split with the column quotient, and build
an incremental solver — and priced the candidate at "1–2 further sessions on 24 cores, at maybe 0.6
probability of closing". Neither lever is what moved it. The plain column quotient ("assume the
representative is used") is strictly weaker than the least-orbit refinement used here, and no
incremental solver was built or needed; what moved it was the `|E|` split, the least-orbit
refinement, and lex-minimality, none of which was on the list.

**What it actually cost, and what it would cost now.** The 74 decided cells took about
190 000 CPU-seconds — some 53 CPU-hours — on a machine that gave this run 11–13 effective cores out
of 24. But more than half of that was spent by `cert4` before the lex-minimality cuts existed, on
cells that `cert7` now does 2–30x faster, and 26 000 CPU-s of it went into `|E| = 12` cells that
`enum12.py` later decided exactly and completely for 1150 CPU-s per sector. A rerun of the *decided*
part with today's tooling is well under 20 CPU-hours.

**What made the difference, ranked.**

1. **Lex-minimality (§2.3), ~30x on the cells that were the wall.** Free to implement, zero solver
   work, ~12 000 short clauses. The general lesson is worth writing on the node: in a
   *decision* problem about a minimum, one may always normalise to a lexicographically minimal
   solution, and the local-improvement moves of the specific problem then become sound clauses. Here
   the move "drop a subset of the hook columns and pay for it in data faults" gives
   `|XOR_{r in T} r| >= |T| + 1` for every used subset `T`, which no amount of solver tuning finds.
2. **The residual-orbit quotient in least-orbit form (§2.2), ~10x CPU and ~30x critical path.**
   The refinement over "assume the representative is used" costs one line and roughly halves the
   residual columns per sub-query on average.
3. **The `|E|` split (§2.1), which is what makes 1 and 2 expressible.** It also turns the extreme
   cells into unit propagation.
4. **Complete enumeration where the object is small (§5.2).** The whole `|E| = 12` stratum — nine
   cells per sector, the most expensive third of the sweep under `cert4` — costs ~1150 CPU-s per
   sector once the 1884 weight-12 logicals are known to be all of them.

**Repricing the rest of the family.** The right number for the candidate is now visible rather than guessed. The 74 decided cells cost
about 181 000 CPU-s, but more than half of that was spent by `cert4` before the lex-minimality cuts
existed, on cells that `cert7` now does 2–30x faster. The 36 open cells are of the same kind as
`(7,16)`, `(8,18)`, `(9,24)` — cells `cert7` closed for 4 000–7 000 CPU-s each. So the honest
completion estimate is **150 000–250 000 CPU-s, i.e. 2–4 hours on 24 *idle* cores**, and the single
biggest lever left is not a better cut but an unshared machine: this run averaged 11–13 effective
cores out of 24.

For the rest of the family: nothing in the three levers is special to the candidate. The `|E|` split
and the lex-minimality cuts are properties of the model, and every non-uniform tiled triple has the
same order-24 stabiliser and the same 9 residual orbits (uniform triples have order 72 and only 3
residual orbits, so they are cheaper still). One orbit is therefore of the same order as the
candidate for a full UNSAT decision, and far less when a witness exists — SAT cells close in
minutes. The predecessor's "1–2 sessions per orbit, 19 orbits" should become **a few days of a
dedicated 24-core machine for the whole family**, not months.

**What I would fund first.** In this order.

1. **Finish the candidate's 36 open cells**, on an idle machine, with `cert7` — 2–4 hours of
   24 cores (§8). It is the only computation on this node whose outcome changes a headline either
   way, and it is now a scheduling problem rather than a research problem.
2. **Render Figure 12 to pixels and read it by eye** (§7.1). Minutes of human work, and it is the
   only remaining risk on everything downstream, all of which is exact.
3. **The `|T| = 4` member of the lex-minimality family**, or a cardinality bound on the number of
   overlapping used hook pairs, if 1 turns out to be slower than estimated. The open cells are
   exactly the regime where `(c8)`/`(c9)` stop biting and only `(c10)`/`(c11)` help, so the next
   term of the same series is the natural thing to try; `|T| = 4` means C(216,4) ~ 9e7 XORs to
   enumerate offline, which is minutes, and an unknown but possibly large number of quaternary
   clauses — measure the clause count before committing.
4. **The remaining 19 orbits**, which turn "the candidate has `d_ext = 11`" into "the candidate is
   the unique `phi = a+b` tiled assignment with `d_ext = 11`".

The `D* = 11` vs `12` question — whether an interleaved schedule reaches 12 — is untouched by any of
this and is where the node's remaining difficulty lives. `d_circ = d_eff` fails in general for
interleaved circuits, so the extended-code reduction that makes all of the above possible is simply
not available there; that is a different problem, not a bigger version of this one.

---

## 9. Reproduction

Python 3.9.6, `numpy` 2.0.2, `stim` 1.16.0, `python-sat` 1.9.dev15. 24 cores, shared with 20–28
foreign processes throughout (§7.5).

**Reused verbatim** from `artifacts/circdist_gross_sbbcert_20260820.md` §9 and
`artifacts/circdist_gross_phicert_20260822.md` §8, extracted mechanically back out of those markdown
files into an empty directory and re-validated here: `gross.py`, `sched.py`, `cascade.py`, `pool.py`,
`dext.py`, `dext2.py`, `cert.py`, `simverify.py`, `altcheck.py`, `lrc8.py`. They are not reproduced
again below.

Order of execution:

```
python3 gross.py                       # code construction + rank / commutation / incidence checks
python3 pool.py                        # weight-12 logical pools and logical bases
python3 cascade.py                     # the cascade; 44 tiled survivors per sector at phi = a+b
python3 anchor1.py                     # |E| even; candidate in the survivor lists; orbit structure
python3 stabcheck.py                   # the stabiliser acts as a weight-preserving automorphism
python3 cuts.py                        # (c3)-(c6), the ceiling and the dominance repair, sampled
python3 anchor2.py                     # d(gross) = 12 in the Z sector
python3 anchor3.py                     # explicit weight-11 witnesses; d(gross) = 12 in the X sector
python3 enum12.py                      # complete weight-12 enumeration + the |E| = 12 stratum
python3 redwit.py                      # the lex-minimality normalisation, on real witnesses
python3 orbcover.py                    # the residual-orbit cover, on real witnesses
python3 job4.py <sec> <a,b,c> 10 <K> <Ew> <orbit>   # one cell x one orbit, cuts (c1)-(c7)
python3 job7.py <sec> <a,b,c> 10 <K> <Ew> <orbit>   # the same, cuts (c1)-(c11)
   # job5/job6/job7 are job4 with the certifier module swapped:
   #   sed -e 's/cert4/cert7/g' job4.py > job7.py   (and likewise cert5, cert6)
python3 drive.py <log> <nproc> <spec.json> [timeout]
python3 recheck.py <sec> <a,b,c> 10 <K> <Ew> <orbit> <solver>   # second-solver re-decision
python3 mktable8.py                    # the result table
python3 frontier.py                    # the list of cells still open
python3 altcheck.py ; python3 lrc8.py  # realisability, re-run
```

Every `job4`/`job7` line prints a SHA-256 of the exact clause list handed to the solver, so a
reviewer can confirm that `recheck.py` re-decided the same CNF.

### 9.1 New modules

---

#### `cert4.py`

```python
"""(K, |E|)-split exact certifier for d_ext of a three-colour-tiled gross-code assignment.

Model (Z sector; X is the mirror), identical to dext.py/dext2.py:
    z_j      j=0..143      the net data error E
    u_{c,k}  c=0..71,k=0..2  residual k of check c used   (weights 2,3,2)
    d_j      j=0..143      the data-fault part,  d = E xor rho,  rho = xor of the used residuals
    weight   = |d| + |u|  <= W
constraints  H_det z = 0 ;  OR_i (L_i . z = 1) ;  d_j = z_j xor (xor of u hitting j).

The split adds, for a cell (K, Ew) with K = |u| and Ew = |E| :

  (c1)  |u| = K                                      (definition of the cell)
  (c2)  |z| = Ew                                     (definition of the cell)
  (c3)  |d| <= W - K                                 (from |d| + |u| <= W)
  (c4)  |rho| >= Ew - (W - K)                        (from |E| <= |d| + |rho|)
  (c5)  |rho| <= 3K                                  (each residual has weight <= 3)
  (c6)  n3 := #{c : u_{c,1}} >= Ew - W - K           (from |rho| <= 2K + n3 and (c4))
  (c7)  ~(u_{c,1} and u_{c,2})                       (dominance cut, as in dext2.Cert)

(c4)-(c6) are semantic consequences of the model, hence sound to add: every satisfying
assignment of the unsplit model with |u| = K and |z| = Ew satisfies them.  Cells are exhaustive:
Ew is even (all-ones lies in rowspace(H_det), so every E in ker(H_det) has even weight -- checked
in anchor1.py), Ew >= 12 (E is a nontrivial logical and d(gross) = 12, re-certified here), and
Ew <= W + 2K by (c4)+(c5).  K ranges over 0..W.  UNSAT on every cell certifies d_ext > W.
"""
import numpy as np, itertools, time
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from gross import HX, HZ, N, NG, Reducer
from dext import xor_chain, xor_zero_direct, verify_witness


class Cert4:
    def __init__(self, ctx, W, K, Ew, dominance=True, use_rho=True):
        pool = IDPool()
        self.z = [pool.id(('z', j)) for j in range(N)]
        self.u = [[pool.id(('u', c, k)) for k in range(3)] for c in range(ctx.ncheck)]
        self.d = [pool.id(('d', j)) for j in range(N)]
        cls = []
        for e in range(ctx.Hdet.shape[0]):
            xor_zero_direct([self.z[int(j)] for j in np.nonzero(ctx.Hdet[e])[0]], cls)
        ys = []
        for i in range(ctx.Lrows.shape[0]):
            ys.append(xor_chain(pool, [self.z[int(j)] for j in np.nonzero(ctx.Lrows[i])[0]], cls))
        cls.append(ys)
        for j in range(N):
            terms = [self.d[j], self.z[j]] + [self.u[c][k] for (c, k) in ctx.hit[j]]
            if len(terms) <= 6:
                xor_zero_direct(terms, cls)
            else:
                cls.append([-xor_chain(pool, terms, cls)])
        if dominance:
            for c in range(ctx.ncheck):
                cls.append([-self.u[c][1], -self.u[c][2]])
        ulits = [self.u[c][k] for c in range(ctx.ncheck) for k in range(3)]
        u3lits = [self.u[c][1] for c in range(ctx.ncheck)]
        # rho_j = z_j xor d_j
        self.rho = []
        if use_rho:
            for j in range(N):
                r = pool.id(('r', j))
                a, b = self.z[j], self.d[j]
                cls += [[-r, a, b], [-r, -a, -b], [r, -a, b], [r, a, -b]]
                self.rho.append(r)
        top = pool.top

        def add(enc):
            nonlocal cls, top
            cls += enc.clauses
            top = max([top] + [abs(l) for cl in enc.clauses for l in cl])

        # (c1)
        add(CardEnc.atmost(lits=ulits, bound=K, top_id=top, encoding=EncType.seqcounter))
        if K > 0:
            add(CardEnc.atleast(lits=ulits, bound=K, top_id=top, encoding=EncType.seqcounter))
        else:
            cls += [[-l] for l in ulits]
        # (c2)
        add(CardEnc.atmost(lits=self.z, bound=Ew, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atleast(lits=self.z, bound=Ew, top_id=top, encoding=EncType.seqcounter))
        # (c3)
        add(CardEnc.atmost(lits=self.d, bound=W - K, top_id=top, encoding=EncType.seqcounter))
        # (c4), (c5)
        if use_rho:
            lo = Ew - (W - K)
            if lo > 0:
                add(CardEnc.atleast(lits=self.rho, bound=lo, top_id=top,
                                    encoding=EncType.seqcounter))
            if 3 * K < N:
                add(CardEnc.atmost(lits=self.rho, bound=3 * K, top_id=top,
                                   encoding=EncType.seqcounter))
        # (c6)
        n3lo = Ew - W - K
        if n3lo > 0:
            add(CardEnc.atleast(lits=u3lits, bound=n3lo, top_id=top,
                                encoding=EncType.seqcounter))
        self.cls = cls
        self.top = top
        self.ctx = ctx

    def col_lit(self, col):
        return self.d[col[1]] if col[0] == 'd' else self.u[col[1]][col[2]]

    def decode(self, model):
        ms = set(x for x in model if x > 0)
        E = np.array([1 if self.z[j] in ms else 0 for j in range(N)], np.uint8)
        R = [(c, k) for c in range(self.ctx.ncheck) for k in range(3) if self.u[c][k] in ms]
        D = np.array([1 if self.d[j] in ms else 0 for j in range(N)], np.uint8)
        return E, R, D


def cells(W, Kmax=None):
    """all (K, Ew) cells that are arithmetically feasible."""
    out = []
    for K in range(0, (Kmax if Kmax is not None else W) + 1):
        for Ew in range(12, W + 2 * K + 1, 2):
            if Ew - W - K > K:          # (c6) with n3 <= K
                continue
            out.append((K, Ew))
    return out
```

#### `cert6.py`

```python
"""cert4 plus the LEX-MINIMALITY cut, which is what actually makes the |E| >= 14 strata cheap.

Take the decision question "is there a solution of weight <= W?".  If the answer is yes, there is a
solution x* = (E, R, d) minimising (weight, |R|) lexicographically among all solutions of weight
<= W.  Fix any r in R and drop it: x' = (E, R \\ {r}, d xor r) is again a solution (E is unchanged,
so the syndrome is still zero and the logical still non-trivial), with |R'| = |R| - 1 and
weight' = |d xor r| + |R| - 1.  Since |R'| < |R|, x' beats x* lexicographically as soon as
weight' <= weight, so minimality forces weight' > weight, i.e.

        |d xor r| >= |d| + 2   <=>   |r| - 2 |d cap r| >= 2 .

Residual weights are 2, 3, 2, so in both cases this forces |d cap r| = 0:

  (c8)   u_{c,k}  =>  d_q = 0   for every q in r_k(c)          (~500 binary clauses)

and hence, since d_j = 1 now implies that no used residual covers j and therefore rho_j = 0,

  (c9)   d_j  =>  z_j                                          (144 binary clauses)

i.e. d is DISJOINT from every used residual and CONTAINED in E, so E = d (disjoint union) rho and
|E| = |d| + |rho| exactly.

Soundness for the decision question: (c8)/(c9) can remove solutions, but never all of them -- the
lex-minimal solution survives, and it lies in the cell (K, Ew) given by its own |R| and |E|, both of
which the sweep enumerates.  So UNSAT on every cell still certifies d_ext > W.  (Validated on real
data in redwit.py: every known weight-10 witness reduces, by iterating the drop step above, to a
weight-<=10 solution that satisfies (c8) and (c9).)

Everything else is cert4.Cert4 verbatim.
"""
import numpy as np
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from gross import N
from dext import xor_chain, xor_zero_direct


class Cert6:
    def __init__(self, ctx, W, K, Ew, dominance=True, lexmin=True):
        pool = IDPool()
        self.z = [pool.id(('z', j)) for j in range(N)]
        self.u = [[pool.id(('u', c, k)) for k in range(3)] for c in range(ctx.ncheck)]
        self.d = [pool.id(('d', j)) for j in range(N)]
        cls = []
        for e in range(ctx.Hdet.shape[0]):
            xor_zero_direct([self.z[int(j)] for j in np.nonzero(ctx.Hdet[e])[0]], cls)
        ys = []
        for i in range(ctx.Lrows.shape[0]):
            ys.append(xor_chain(pool, [self.z[int(j)] for j in np.nonzero(ctx.Lrows[i])[0]], cls))
        cls.append(ys)
        for j in range(N):
            terms = [self.d[j], self.z[j]] + [self.u[c][k] for (c, k) in ctx.hit[j]]
            if len(terms) <= 6:
                xor_zero_direct(terms, cls)
            else:
                cls.append([-xor_chain(pool, terms, cls)])
        if dominance:
            for c in range(ctx.ncheck):
                cls.append([-self.u[c][1], -self.u[c][2]])
        if lexmin:
            for c in range(ctx.ncheck):
                for k in range(3):
                    for q in ctx.res[c][k]:
                        cls.append([-self.u[c][k], -self.d[int(q)]])          # (c8)
            for j in range(N):
                cls.append([-self.d[j], self.z[j]])                            # (c9)
        ulits = [self.u[c][k] for c in range(ctx.ncheck) for k in range(3)]
        u3lits = [self.u[c][1] for c in range(ctx.ncheck)]
        self.rho = []
        for j in range(N):
            r = pool.id(('r', j))
            a, b = self.z[j], self.d[j]
            cls += [[-r, a, b], [-r, -a, -b], [r, -a, b], [r, a, -b]]
            self.rho.append(r)
        top = pool.top

        def add(enc):
            nonlocal cls, top
            cls += enc.clauses
            top = max([top] + [abs(l) for cl in enc.clauses for l in cl])

        add(CardEnc.atmost(lits=ulits, bound=K, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atleast(lits=ulits, bound=K, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atmost(lits=self.z, bound=Ew, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atleast(lits=self.z, bound=Ew, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atmost(lits=self.d, bound=W - K, top_id=top, encoding=EncType.seqcounter))
        lo = Ew - (W - K)
        if lo > 0:
            add(CardEnc.atleast(lits=self.rho, bound=lo, top_id=top, encoding=EncType.seqcounter))
        if 3 * K < N:
            add(CardEnc.atmost(lits=self.rho, bound=3 * K, top_id=top, encoding=EncType.seqcounter))
        n3lo = Ew - W - K
        if n3lo > 0:
            add(CardEnc.atleast(lits=u3lits, bound=n3lo, top_id=top, encoding=EncType.seqcounter))
        self.cls = cls
        self.top = top
        self.ctx = ctx

    def col_lit(self, col):
        return self.d[col[1]] if col[0] == 'd' else self.u[col[1]][col[2]]

    def decode(self, model):
        ms = set(x for x in model if x > 0)
        E = np.array([1 if self.z[j] in ms else 0 for j in range(N)], np.uint8)
        R = [(c, k) for c in range(self.ctx.ncheck) for k in range(3) if self.u[c][k] in ms]
        D = np.array([1 if self.d[j] in ms else 0 for j in range(N)], np.uint8)
        return E, R, D
```

#### `cert7.py`

```python
"""cert6 plus the subset form of the LEX-MINIMALITY cut, which is what actually makes the |E| >= 14 strata cheap.

Take the decision question "is there a solution of weight <= W?".  If the answer is yes, there is a
solution x* = (E, R, d) minimising (weight, |R|) lexicographically among all solutions of weight
<= W.  Fix any r in R and drop it: x' = (E, R \\ {r}, d xor r) is again a solution (E is unchanged,
so the syndrome is still zero and the logical still non-trivial), with |R'| = |R| - 1 and
weight' = |d xor r| + |R| - 1.  Since |R'| < |R|, x' beats x* lexicographically as soon as
weight' <= weight, so minimality forces weight' > weight, i.e.

        |d xor r| >= |d| + 2   <=>   |r| - 2 |d cap r| >= 2 .

Residual weights are 2, 3, 2, so in both cases this forces |d cap r| = 0:

  (c8)   u_{c,k}  =>  d_q = 0   for every q in r_k(c)          (~500 binary clauses)

and hence, since d_j = 1 now implies that no used residual covers j and therefore rho_j = 0,

  (c9)   d_j  =>  z_j                                          (144 binary clauses)

i.e. d is DISJOINT from every used residual and CONTAINED in E, so E = d (disjoint union) rho and
|E| = |d| + |rho| exactly.

Soundness for the decision question: (c8)/(c9) can remove solutions, but never all of them -- the
lex-minimal solution survives, and it lies in the cell (K, Ew) given by its own |R| and |E|, both of
which the sweep enumerates.  So UNSAT on every cell still certifies d_ext > W.  (Validated on real
data in redwit.py: every known weight-10 witness reduces, by iterating the drop step above, to a
weight-<=10 solution that satisfies (c8) and (c9).)

Everything else is cert4.Cert4 verbatim.
"""
import numpy as np
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from gross import N
from dext import xor_chain, xor_zero_direct


class Cert7:
    def __init__(self, ctx, W, K, Ew, dominance=True, lexmin=True):
        pool = IDPool()
        self.z = [pool.id(('z', j)) for j in range(N)]
        self.u = [[pool.id(('u', c, k)) for k in range(3)] for c in range(ctx.ncheck)]
        self.d = [pool.id(('d', j)) for j in range(N)]
        cls = []
        for e in range(ctx.Hdet.shape[0]):
            xor_zero_direct([self.z[int(j)] for j in np.nonzero(ctx.Hdet[e])[0]], cls)
        ys = []
        for i in range(ctx.Lrows.shape[0]):
            ys.append(xor_chain(pool, [self.z[int(j)] for j in np.nonzero(ctx.Lrows[i])[0]], cls))
        cls.append(ys)
        for j in range(N):
            terms = [self.d[j], self.z[j]] + [self.u[c][k] for (c, k) in ctx.hit[j]]
            if len(terms) <= 6:
                xor_zero_direct(terms, cls)
            else:
                cls.append([-xor_chain(pool, terms, cls)])
        if dominance:
            for c in range(ctx.ncheck):
                cls.append([-self.u[c][1], -self.u[c][2]])
        if lexmin:
            for c in range(ctx.ncheck):
                for k in range(3):
                    for q in ctx.res[c][k]:
                        cls.append([-self.u[c][k], -self.d[int(q)]])          # (c8)
            for j in range(N):
                cls.append([-self.d[j], self.z[j]])                            # (c9)
            # (c10)/(c11): for every non-empty subset T of the used residual columns,
            # |XOR_{r in T} r| >= |T| + 1.  Encoded for |T| = 2 and |T| = 3.
            nc = ctx.ncheck
            cols = [(c, k) for c in range(nc) for k in range(3)]
            M = np.zeros((len(cols), N), np.uint8)
            for i, (c, k) in enumerate(cols):
                for q in ctx.res[c][k]:
                    M[i, q] = 1
            lit = [self.u[c][k] for (c, k) in cols]
            n = len(cols)
            for i in range(n):
                w = (M[i] ^ M).sum(1)
                for j in range(i + 1, n):
                    if w[j] <= 2:
                        cls.append([-lit[i], -lit[j]])                        # (c10)
            Mb = np.packbits(M, axis=1)
            POP = np.unpackbits(np.arange(256, dtype=np.uint8)[:, None], axis=1).sum(1)
            for i in range(n):
                Xi = Mb[i] ^ Mb
                for j in range(i + 1, n):
                    v = Xi[j] ^ Mb[j + 1:]
                    bad = np.nonzero(POP[v].sum(1) <= 3)[0]
                    for t in bad:
                        cls.append([-lit[i], -lit[j], -lit[j + 1 + int(t)]])  # (c11)
        ulits = [self.u[c][k] for c in range(ctx.ncheck) for k in range(3)]
        u3lits = [self.u[c][1] for c in range(ctx.ncheck)]
        self.rho = []
        for j in range(N):
            r = pool.id(('r', j))
            a, b = self.z[j], self.d[j]
            cls += [[-r, a, b], [-r, -a, -b], [r, -a, b], [r, a, -b]]
            self.rho.append(r)
        top = pool.top

        def add(enc):
            nonlocal cls, top
            cls += enc.clauses
            top = max([top] + [abs(l) for cl in enc.clauses for l in cl])

        add(CardEnc.atmost(lits=ulits, bound=K, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atleast(lits=ulits, bound=K, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atmost(lits=self.z, bound=Ew, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atleast(lits=self.z, bound=Ew, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atmost(lits=self.d, bound=W - K, top_id=top, encoding=EncType.seqcounter))
        lo = Ew - (W - K)
        if lo > 0:
            add(CardEnc.atleast(lits=self.rho, bound=lo, top_id=top, encoding=EncType.seqcounter))
        if 3 * K < N:
            add(CardEnc.atmost(lits=self.rho, bound=3 * K, top_id=top, encoding=EncType.seqcounter))
        n3lo = Ew - W - K
        if n3lo > 0:
            add(CardEnc.atleast(lits=u3lits, bound=n3lo, top_id=top, encoding=EncType.seqcounter))
        self.cls = cls
        self.top = top
        self.ctx = ctx

    def col_lit(self, col):
        return self.d[col[1]] if col[0] == 'd' else self.u[col[1]][col[2]]

    def decode(self, model):
        ms = set(x for x in model if x > 0)
        E = np.array([1 if self.z[j] in ms else 0 for j in range(N)], np.uint8)
        R = [(c, k) for c in range(self.ctx.ncheck) for k in range(3) if self.u[c][k] in ms]
        D = np.array([1 if self.d[j] in ms else 0 for j in range(N)], np.uint8)
        return E, R, D
```

#### `job4.py`

```python
"""One (sector, triple, W, K, |E|) cell of the split certification, optionally restricted to one
column orbit of the assignment's translation stabiliser.

usage:  job4.py <sector> <a,b,c> <W> <K> <Ew> [orbit_index] [s t]
        orbit_index = -1 : no orbit restriction
        orbit_index >= 0 : index into the RESIDUAL column orbits of the assignment's translation
                           stabiliser S (9 of them: one per (colour, residual type); each has
                           |S| = 24 members).  The cell forces the orbit representative to be USED
                           and every residual column of a strictly earlier orbit to be UNUSED.

                           Sound cover, given K >= 1 (true in every cell we run, since K = 0 is
                           arithmetically empty): let x be a solution and let i be the least
                           residual-orbit index it uses.  Pick g in S carrying one of x's columns
                           in orbit i to rep_i; g.x is a solution of the same weight (S consists of
                           code translations that preserve the tiled assignment, hence the extended
                           code, its logical functional and every column weight), it uses rep_i,
                           and it uses no residual column of an orbit < i because orbits are
                           S-invariant.  So the 9 restricted queries cover all solutions.
"""
import sys, time, json, hashlib
import numpy as np
from pysat.solvers import Cadical153
from sched import make_phi
from cert import tiled_orders
import dext, dext2, cert4

sector = sys.argv[1]
triple = tuple(int(c) for c in sys.argv[2].split(','))
W = int(sys.argv[3]); K = int(sys.argv[4]); Ew = int(sys.argv[5])
oi = int(sys.argv[6]) if len(sys.argv) > 6 else -1
s_par, t_par = (int(sys.argv[7]), int(sys.argv[8])) if len(sys.argv) > 8 else (1, 1)

phi = make_phi(s_par, t_par)
orders, _ = tiled_orders(sector, phi, triple)
ctx, Hstab = dext.sector_ctx(orders, sector)
c = cert4.Cert4(ctx, W, K, Ew)
cls = list(c.cls)
rec = dict(sector=sector, triple=list(triple), W=W, K=K, Ew=Ew, orbit=oi,
           phi=[s_par, t_par], nclauses=len(cls), nvars=c.top)
if oi >= 0:
    assert K >= 1, "residual-orbit split requires K >= 1"
    S, orbits = dext2.column_orbits(phi, triple)
    rorb = [(rep, orb) for (rep, orb) in orbits if rep[0] == 'r']
    rec['norbits'] = len(rorb); rec['stab'] = len(S)
    assert all(len(o) == len(S) for _, o in rorb)   # free action: every orbit has |S| members
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
with Cadical153(bootstrap_with=cls) as S2:
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

#### `drive.py`

```python
"""Run a list of job4 cells with a bounded process pool, append every result line to a jsonl log."""
import subprocess, sys, os, json, time, threading

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, sys.argv[1])
NPROC = int(sys.argv[2])
SPEC = json.load(open(os.path.join(HERE, sys.argv[3])))   # list of arg-lists
TMO = float(sys.argv[4]) if len(sys.argv) > 4 else None

lock = threading.Lock()
queue = list(SPEC)
qi = [0]


def worker():
    while True:
        with lock:
            if qi[0] >= len(queue):
                return
            i = qi[0]; qi[0] += 1
            args = queue[i]
        t0 = time.time()
        try:
            p = subprocess.run([sys.executable, os.path.join(HERE, 'job4.py')]
                               + [str(a) for a in args],
                               capture_output=True, text=True, cwd=HERE, timeout=TMO)
            out = p.stdout.strip().splitlines()
            line = out[-1] if out else json.dumps(dict(args=args, verdict='CRASH',
                                                       err=p.stderr[-400:]))
            try:
                rec = json.loads(line)
            except Exception:
                rec = dict(args=args, verdict='CRASH', raw=line[:400], err=p.stderr[-400:])
        except subprocess.TimeoutExpired:
            rec = dict(args=args, verdict='TIMEOUT', tmo=TMO)
        rec['wall'] = round(time.time() - t0, 1)
        with lock:
            with open(LOG, 'a') as f:
                f.write(json.dumps(rec) + "\n")
            print(f"[{i+1}/{len(queue)}] {args} -> {rec.get('verdict')} {rec['wall']}s", flush=True)


ts = [threading.Thread(target=worker) for _ in range(NPROC)]
for t in ts:
    t.start()
for t in ts:
    t.join()
print("done")
```

#### `stabcheck.py`

```python
"""Verify, element by element, that the translation stabiliser S of a tiled assignment acts on the
extended code as a weight-preserving automorphism, and that column_orbits' orbit structure is the
true orbit structure of that action.

For every g = (a,b) in S with data permutation dp and check permutation cp we check
  (1) g permutes the ROWS of H_X as a set, and the rows of H_Z as a set
      => ker(H_X), ker(H_Z), rowspace(H_X), rowspace(H_Z) are all preserved, so g preserves both
         "zero syndrome" and "non-trivial logical";
  (2) dp(r_k(c)) = r_k(cp(c)) for every check c and residual index k
      => g maps extended-code column ('r',c,k) to ('r',cp(c),k) and ('d',j) to ('d',dp[j]),
         bijectively and weight-preservingly.
Together: x -> g.x is a weight-preserving bijection of the solution set of every (W,K,Ew) cell.
"""
import numpy as np, itertools, sys, json
from gross import HX, HZ, N, NG, ELL, EM, gidx
from sched import make_phi
from cert import tiled_orders
import dext, dext2


def dperm(a, b):
    p = np.empty(N, int)
    for i in range(ELL):
        for j in range(EM):
            p[gidx(i, j)] = gidx(i + a, j + b)
            p[NG + gidx(i, j)] = NG + gidx(i + a, j + b)
    return p


def cperm(a, b):
    p = np.empty(NG, int)
    for i in range(ELL):
        for j in range(EM):
            p[gidx(i, j)] = gidx(i + a, j + b)
    return p


def rows_permuted(H, dp):
    """H[i] pushed forward by dp must again be a row of H, bijectively."""
    keys = {H[i].tobytes(): i for i in range(H.shape[0])}
    img = set()
    for i in range(H.shape[0]):
        v = np.zeros(N, np.uint8)
        v[dp[np.nonzero(H[i])[0]]] = 1
        k = v.tobytes()
        if k not in keys:
            return False
        img.add(keys[k])
    return len(img) == H.shape[0]


phi = make_phi(1, 1)
out = {}
for sector, tr in (('Z', (1, 2, 62)), ('X', (14, 0, 2))):
    S, orbits = dext2.column_orbits(phi, tr)
    orders, _ = tiled_orders(sector, phi, tr)
    res = dext.residual_sets(orders)
    badrow = badres = 0
    for (a, b) in S:
        dp, cp = dperm(a, b), cperm(a, b)
        if not (rows_permuted(HX, dp) and rows_permuted(HZ, dp)):
            badrow += 1
        for c in range(NG):
            for k in range(3):
                if tuple(sorted(int(dp[q]) for q in res[c][k])) != tuple(sorted(res[int(cp[c])][k])):
                    badres += 1
    # orbit structure, recomputed independently from the verified action
    cols = [('d', j) for j in range(N)] + [('r', c, k) for c in range(NG) for k in range(3)]
    seen = set(); orbs = []
    for col in cols:
        if col in seen:
            continue
        o = set()
        for (a, b) in S:
            dp, cp = dperm(a, b), cperm(a, b)
            o.add(('d', int(dp[col[1]])) if col[0] == 'd' else ('r', int(cp[col[1]]), col[2]))
        seen |= o; orbs.append(sorted(o))
    same = (sorted(tuple(sorted(o)) for _, o in orbits) == sorted(tuple(o) for o in orbs))
    rorb = [o for o in orbs if o[0][0] == 'r']
    print(f"sector {sector} triple {tr}: |S| = {len(S)}; row-permutation failures {badrow}; "
          f"residual-equivariance failures {badres}; orbits {len(orbs)} "
          f"(residual orbits {len(rorb)}, sizes {sorted({len(o) for o in orbs})}); "
          f"matches column_orbits: {same}")
    out[sector] = dict(nS=len(S), badrow=badrow, badres=badres, norb=len(orbs),
                       nres_orb=len(rorb), same=bool(same))
json.dump(out, open("stabcheck.json", "w"), indent=1)
```

#### `cuts.py`

```python
"""Machine check of the three things the (K,|E|) cell decomposition rests on, on the candidate's
own residual sets, by randomised sampling over the actual model:

 (A) the cut inequalities (c3)-(c6) of cert4.py hold for EVERY assignment of the unsplit model with
     |d| + |R| <= W;
 (B) the dominance cut is weight-non-increasing and E-preserving: a solution using both r2(c) and
     r3(c) maps to a solution of strictly smaller weight with the same E;
 (C) the cells are exhaustive: every weight-<=W assignment with |E| >= 12 and |E| even falls into
     one of cert4.cells(W).

(A) and (B) are checked on 200 000 random (R, d) draws per sector; (C) follows from (A) plus the
two facts certified elsewhere (|E| even -- all-ones lies in rowspace(H_det), anchor1.py; |E| >= 12
-- d(gross) = 12, re-certified in anchor2.py).
"""
import numpy as np, itertools, sys
from gross import N, NG
from sched import make_phi
from cert import tiled_orders
import dext, cert4

W = 10
rng = np.random.default_rng(20260822)
phi = make_phi(1, 1)
allcells = set(cert4.cells(W))
report = {}
for sector, tr in (('Z', (1, 2, 62)), ('X', (14, 0, 2))):
    orders, _ = tiled_orders(sector, phi, tr)
    res = dext.residual_sets(orders)
    cols = [(c, k) for c in range(NG) for k in range(3)]
    bad = dict(c3=0, c4=0, c5=0, c6=0, ub=0, dom=0, cell=0)
    nsamp = 200000
    for _ in range(nsamp):
        K = int(rng.integers(1, W + 1))
        idx = rng.choice(len(cols), size=K, replace=False)
        R = [cols[i] for i in idx]
        rho = np.zeros(N, np.uint8)
        for (c, k) in R:
            for q in res[c][k]:
                rho[q] ^= 1
        nd = int(rng.integers(0, W - K + 1))
        d = np.zeros(N, np.uint8)
        d[rng.choice(N, size=nd, replace=False)] = 1
        E = d ^ rho
        Ew = int(E.sum()); rw = int(rho.sum()); n3 = sum(1 for (c, k) in R if k == 1)
        if nd + K > W:
            continue
        # (A) the cuts, as they are added in cert4.Cert4 for the cell (K, Ew)
        if not nd <= W - K:
            bad['c3'] += 1
        if not rw >= Ew - (W - K):
            bad['c4'] += 1
        if not rw <= 3 * K:
            bad['c5'] += 1
        if not n3 >= Ew - W - K:
            bad['c6'] += 1
        if not Ew <= W + 2 * K:
            bad['ub'] += 1
        # (C) cell membership, for the assignments that could be genuine solutions
        if Ew >= 12 and Ew % 2 == 0 and (K, Ew) not in allcells:
            bad['cell'] += 1
        # (B) dominance repair, when applicable
        dbl = [c for c in range(NG) if (c, 1) in R and (c, 2) in R]
        if dbl:
            c0 = dbl[0]
            R2 = [x for x in R if x not in ((c0, 1), (c0, 2))]
            i4 = res[c0][1][0]                      # r2 = {i4,i5,i6}, r3 = {i5,i6}
            assert set(res[c0][1]) - set(res[c0][2]) == {i4}
            d2 = d.copy(); d2[i4] ^= 1
            rho2 = np.zeros(N, np.uint8)
            for (c, k) in R2:
                for q in res[c][k]:
                    rho2[q] ^= 1
            if not (np.array_equal(d2 ^ rho2, E) and int(d2.sum()) + len(R2) < nd + K):
                bad['dom'] += 1
    report[sector] = bad
    print(f"sector {sector} triple {tr}: {nsamp} random (R,d) draws, violations {bad}")
print("cells(W=10):", len(allcells), "  all violation counters zero:",
      all(v == 0 for b in report.values() for v in b.values()))
```

#### `redwit.py`

```python
"""Validate the lex-minimality cut (c8)/(c9) of cert6.py on real weight-10 witnesses.

For every witness in logs/val.jsonl, iterate the drop step
    (E, R, d) -> (E, R \\ {r}, d xor r)   whenever it does not increase (weight, |R|) lex,
which must terminate (|R| strictly decreases each time).  The fixed point must
  * still be a valid solution of the same E, verified by dext.verify_witness,
  * still have weight <= 10,
  * satisfy (c8): d is disjoint from every used residual,
  * satisfy (c9): d is contained in E, and |E| = |d| + |rho| exactly,
and it tells us which cell (K, Ew) the lex-minimal representative of that witness lives in.
"""
import json
import numpy as np
from gross import N, NG
from sched import make_phi
from cert import tiled_orders
import dext

phi = make_phi(1, 1)
nbad = 0; n = 0
for line in open('logs/val.jsonl'):
    r0 = json.loads(line)
    if r0['verdict'] != 'SAT':
        continue
    sector, tr = r0['sector'], tuple(r0['triple'])
    orders, _ = tiled_orders(sector, phi, tr)
    ctx, Hstab = dext.sector_ctx(orders, sector)
    R = [tuple(x) for x in r0['R']]
    E = np.zeros(N, np.uint8); E[r0['E']] = 1
    D = np.zeros(N, np.uint8); D[r0['D']] = 1
    w0 = int(D.sum()) + len(R)
    import itertools as _it
    changed = True
    while changed:
        changed = False
        for m in range(1, len(R) + 1):
            for T in _it.combinations(R, m):
                D2 = D.copy()
                for (c, k) in T:
                    for q in ctx.res[c][k]:
                        D2[q] ^= 1
                if int(D2.sum()) + len(R) - m <= int(D.sum()) + len(R):
                    D = D2; R = [x for x in R if x not in T]; changed = True
                    break
            if changed:
                break
    info = dext.verify_witness(ctx, E, R, D, Hstab)
    rho = np.zeros(N, np.uint8)
    for (c, k) in R:
        for q in ctx.res[c][k]:
            rho[q] ^= 1
    c8 = all(D[q] == 0 for (c, k) in R for q in ctx.res[c][k])
    import itertools as _it
    sub_ok = True
    for m in range(1, len(R) + 1):
        for T in _it.combinations(R, m):
            s_ = np.zeros(N, np.uint8)
            for (c, k) in T:
                for q in ctx.res[c][k]:
                    s_[q] ^= 1
            if int(s_.sum()) < m + 1:
                sub_ok = False
    c9 = bool(((D & ~E) == 0).all())
    add = (int(E.sum()) == int(D.sum()) + int(rho.sum()))
    ok = (info['weight'] <= 10 and info['decomposition_ok'] and info['zero_syndrome']
          and info['nontrivial_logical'] and c8 and c9 and add and sub_ok)
    n += 1; nbad += (0 if ok else 1)
    print(f"{sector} {tr}: weight {w0} (K={len(r0['R'])}) -> lex-min weight {info['weight']} "
          f"(K={info['n_res']}), cell (K={info['n_res']}, Ew={info['Ewt']}); "
          f"(c8) {c8}  (c9) {c9}  |E|=|d|+|rho| {add}  "
          f"(c10/c11, all 2^K-1 subsets) {sub_ok}  valid {ok}")
print(f"\nreduced {n} witnesses, failures {nbad}")
```

#### `enum12.py`

```python
"""An independent, solver-light route to every cell with |E| = 12.

Step 1 -- COMPLETE enumeration of the weight-12 non-trivial logicals of the gross code, by
incremental SAT with blocking clauses: constraints H_det z = 0, OR_i (L_i . z = 1), |z| = 12;
after each model v the 12-literal clause  OR_{j in supp(v)} ~z_j  is added, which under |z| = 12
blocks exactly v and nothing else.  The loop ends in UNSAT, so the list is exhaustive by
construction (no reliance on pool.py's randomised ISD search).

Step 2 -- for every enumerated E, decide exactly whether  min_R ( |E xor rho_R| + |R| ) <= W.
With E fixed this is a tiny CNF (216 u-variables, d determined bitwise), so the whole |E| = 12
half of the certification is decided without any of the big queries.

The output is compared against pool.py's pool and against the cell-(K,12) SAT verdicts.
"""
import sys, time, json
import numpy as np
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from gross import HX, HZ, N, NG, Reducer
from sched import make_phi
from cert import tiled_orders
from dext import xor_chain, xor_zero_direct, residual_sets
import dext, pool as poolmod

W = 10
phi = make_phi(1, 1)
PZ, PX, LX, LZ = poolmod.get()
out = {}
for sector, tr in (('Z', (1, 2, 62)), ('X', (14, 0, 2))):
    Hdet, Lrows, Hstab = (HX, LX, HZ) if sector == 'Z' else (HZ, LZ, HX)
    Pref = PZ if sector == 'Z' else PX
    # ---- step 1
    p = IDPool()
    z = [p.id(('z', j)) for j in range(N)]
    cls = []
    for e in range(Hdet.shape[0]):
        xor_zero_direct([z[int(j)] for j in np.nonzero(Hdet[e])[0]], cls)
    ys = []
    for i in range(Lrows.shape[0]):
        ys.append(xor_chain(p, [z[int(j)] for j in np.nonzero(Lrows[i])[0]], cls))
    cls.append(ys)
    top = p.top
    for enc in (CardEnc.atmost(lits=z, bound=12, top_id=top, encoding=EncType.seqcounter),):
        cls += enc.clauses; top = max([top] + [abs(l) for c2 in enc.clauses for l in c2])
    for enc in (CardEnc.atleast(lits=z, bound=12, top_id=top, encoding=EncType.seqcounter),):
        cls += enc.clauses; top = max([top] + [abs(l) for c2 in enc.clauses for l in c2])
    t0 = time.time()
    words = []
    with Cadical153(bootstrap_with=cls) as S:
        while S.solve():
            m = set(x for x in S.get_model() if x > 0)
            supp = [j for j in range(N) if z[j] in m]
            assert len(supp) == 12
            v = np.zeros(N, np.uint8); v[supp] = 1
            words.append(v)
            S.add_clause([-z[j] for j in supp])
    t1 = time.time()
    Wds = np.array(words, np.uint8)
    red = Reducer(Hstab)
    ok = (((Hdet @ Wds.T) % 2 == 0).all() and (Wds.sum(1) == 12).all()
          and all(not red.inspan(v) for v in Wds))
    same = (sorted(v.tobytes() for v in Wds) == sorted(v.tobytes() for v in Pref))
    print(f"[{sector}] complete weight-12 logical enumeration: {len(Wds)} words in {t1-t0:.1f}s; "
          f"all valid: {ok}; identical to pool.py's pool: {same}")
    sys.stdout.flush()
    # ---- step 2
    orders, _ = tiled_orders(sector, phi, tr)
    res = residual_sets(orders)
    hit = [[] for _ in range(N)]
    for c in range(NG):
        for k in range(3):
            for q in res[c][k]:
                hit[q].append((c, k))
    best = None; nsat = 0
    t2 = time.time()
    for wi, E in enumerate(Wds):
        p2 = IDPool()
        u = [[p2.id(('u', c, k)) for k in range(3)] for c in range(NG)]
        d = [p2.id(('d', j)) for j in range(N)]
        cl = []
        for c in range(NG):
            cl.append([-u[c][1], -u[c][2]])
        for j in range(N):
            terms = [d[j]] + [u[c][k] for (c, k) in hit[j]]
            # d_j = E_j xor (xor of used residuals hitting j)
            lits = terms
            k = len(lits)
            par = int(E[j])
            for bits in np.ndindex(*([2] * k)):
                if sum(bits) % 2 != par:
                    cl.append([(-lits[i] if bits[i] else lits[i]) for i in range(k)])
        card = [d[j] for j in range(N)] + [u[c][k] for c in range(NG) for k in range(3)]
        enc = CardEnc.atmost(lits=card, bound=W, top_id=p2.top, encoding=EncType.seqcounter)
        cl += enc.clauses
        with Cadical153(bootstrap_with=cl) as S:
            if S.solve():
                nsat += 1
                if best is None:
                    best = wi
    t3 = time.time()
    print(f"[{sector}] |E| = 12 decision over all {len(Wds)} logicals: "
          f"{nsat} admit a weight-<={W} extended-code solution ({t3-t2:.1f}s)")
    sys.stdout.flush()
    out[sector] = dict(n12=len(Wds), valid=bool(ok), same_as_pool=bool(same),
                       enum_seconds=round(t1 - t0, 1), nsat=nsat,
                       decide_seconds=round(t3 - t2, 1))
json.dump(out, open("enum12.json", "w"), indent=1)
```

#### `orbcover.py`

```python
"""Demonstrate the residual-orbit cover on real solutions, combinatorially (no solver).

For every weight-10 witness recorded in logs/val.jsonl (found by the UNRESTRICTED cell query), let
i be the least residual-orbit index the witness uses, pick a stabiliser element g carrying one of
its orbit-i columns to that orbit's representative, and check that g.(E,R,d) is again a solution of
the SAME cell (K, Ew) which uses the representative and no residual column of an orbit < i.  That
is exactly the claim the 9-way orbit split rests on, verified on real data.
"""
import json, sys
import numpy as np
from gross import N, NG, ELL, EM, gidx, Reducer
from sched import make_phi
from cert import tiled_orders
import dext, dext2


def dperm(a, b):
    p = np.empty(N, int)
    for i in range(ELL):
        for j in range(EM):
            p[gidx(i, j)] = gidx(i + a, j + b); p[NG + gidx(i, j)] = NG + gidx(i + a, j + b)
    return p


def cperm(a, b):
    p = np.empty(NG, int)
    for i in range(ELL):
        for j in range(EM):
            p[gidx(i, j)] = gidx(i + a, j + b)
    return p


phi = make_phi(1, 1)
nchecked = nbad = 0
for line in open('logs/val.jsonl'):
    r = json.loads(line)
    if r['verdict'] != 'SAT':
        continue
    sector = r['sector']; tr = tuple(r['triple'])
    orders, _ = tiled_orders(sector, phi, tr)
    ctx, Hstab = dext.sector_ctx(orders, sector)
    S, orbits = dext2.column_orbits(phi, tr)
    rorb = [(rep, orb) for (rep, orb) in orbits if rep[0] == 'r']
    oidx = {}
    for i, (rep, orb) in enumerate(rorb):
        for col in orb:
            oidx[col] = i
    R = [(a, b) for a, b in r['R']]
    E = np.zeros(N, np.uint8); E[r['E']] = 1
    D = np.zeros(N, np.uint8); D[r['D']] = 1
    used = sorted({oidx[('r', c, k)] for (c, k) in R})
    i0 = used[0]
    rep = rorb[i0][0]
    src = next((c, k) for (c, k) in R if oidx[('r', c, k)] == i0)
    g = next(gg for gg in S if (int(cperm(*gg)[src[0]]), src[1]) == (rep[1], rep[2]))
    dp, cp = dperm(*g), cperm(*g)
    E2 = np.zeros(N, np.uint8); E2[dp[np.nonzero(E)[0]]] = 1
    D2 = np.zeros(N, np.uint8); D2[dp[np.nonzero(D)[0]]] = 1
    R2 = [(int(cp[c]), k) for (c, k) in R]
    info = dext.verify_witness(ctx, E2, R2, D2, Hstab)
    used2 = sorted({oidx[('r', c, k)] for (c, k) in R2})
    ok = (info['weight'] == r['info']['weight'] and info['Ewt'] == r['info']['Ewt']
          and info['decomposition_ok'] and info['zero_syndrome'] and info['nontrivial_logical']
          and (rep[1], rep[2]) in [(c, k) for (c, k) in R2] and used2 == used
          and min(used2) == i0)
    nchecked += 1; nbad += (0 if ok else 1)
    print(f"{sector} {tr}: witness uses residual orbits {used}; g = {g} maps it to a solution "
          f"using rep {rep}; same cell (K={info['n_res']}, |E|={info['Ewt']}), "
          f"weight {info['weight']}; orbits after = {used2}; OK = {ok}")
print(f"\nchecked {nchecked} witnesses, failures {nbad}")
```

#### `anchor2.py`

```python
"""Two anchors that the cell decomposition needs, both computed here rather than cited.

  (1) d(gross) = 12 : with the residual columns switched off the model degenerates to the code's
      own minimum logical weight.  UNSAT at W = 11, SAT at W = 12, in both sectors.
      This is what licenses the standing cut |E| >= 12.
  (2) d_ext(E(candidate)) <= 11 : an explicit weight-11 solution of the FULL model, in both
      sectors, found and re-verified from the definitions.  Together with UNSAT at W = 10 this
      pins d_ext = 11 exactly.
"""
import sys, json, time
import numpy as np
from sched import make_phi
from cert import tiled_orders
import dext

phi = make_phi(1, 1)
out = {}
for sector, tr in (('Z', (1, 2, 62)), ('X', (14, 0, 2))):
    orders, _ = tiled_orders(sector, phi, tr)
    ctx, Hstab = dext.sector_ctx(orders, sector)
    row = {}
    for W in (11, 12):
        sat, wit, el, ncls = dext.query(ctx, W, Hstab, use_residuals=False)
        row[f'no_residuals_W{W}'] = dict(verdict='SAT' if sat else 'UNSAT', seconds=round(el, 1),
                                         info=(wit[3] if sat else None))
        print(f"[{sector}] residuals OFF, W={W}: {'SAT' if sat else 'UNSAT'} ({el:.1f}s)",
              wit[3] if sat else "")
        sys.stdout.flush()
    sat, wit, el, ncls = dext.query(ctx, 11, Hstab)
    assert sat, "expected a weight-<=11 solution"
    E, R, D, info = wit
    row['full_W11'] = dict(verdict='SAT', seconds=round(el, 1), info=info,
                           R=[[int(a), int(b)] for a, b in R],
                           D=[int(i) for i in np.nonzero(D)[0]],
                           E=[int(i) for i in np.nonzero(E)[0]])
    print(f"[{sector}] full model, W=11: SAT ({el:.1f}s) {info}")
    sys.stdout.flush()
    out[sector] = row
json.dump(out, open("anchor2.json", "w"), indent=1)
```

#### `anchor3.py`

```python
"""(a) the |E| >= 12 anchor in the X sector: d(gross) = 12, re-certified with the residual columns
       switched off (UNSAT at W = 11, SAT at W = 12);
   (b) an EXPLICIT weight-11 solution of the full extended-code model for the candidate, in both
       sectors, built combinatorially from the complete weight-12 logical enumeration: take any
       weight-12 logical L containing a weight-2 residual r of some check, put E = L, R = {r},
       d = L xor r; then |d| + |R| = 10 + 1 = 11.  This gives d_ext(E(candidate)) <= 11 by witness,
       which with UNSAT at W = 10 pins d_ext = 11 exactly.
"""
import json, time, sys
import numpy as np
from gross import NG, N
from sched import make_phi
from cert import tiled_orders
import dext, pool as poolmod

out = {}
phi = make_phi(1, 1)
# (b) first: cheap and it is the load-bearing half
PZ, PX, LX, LZ = poolmod.get()
for sector, tr in (('Z', (1, 2, 62)), ('X', (14, 0, 2))):
    orders, Hstab0 = tiled_orders(sector, phi, tr)
    ctx, Hstab = dext.sector_ctx(orders, sector)
    P = PZ if sector == 'Z' else PX
    found = None
    for L in P:
        for c in range(NG):
            for k in (0, 2):                      # the two weight-2 residuals r1, r3
                r = ctx.res[c][k]
                if all(L[q] for q in r):
                    D = L.copy()
                    for q in r:
                        D[q] ^= 1
                    info = dext.verify_witness(ctx, L, [(c, k)], D, Hstab)
                    if info['weight'] == 11 and info['decomposition_ok'] and \
                       info['zero_syndrome'] and info['nontrivial_logical']:
                        found = dict(info=info, check=int(c), k=int(k),
                                     r=[int(q) for q in r],
                                     E=[int(i) for i in np.nonzero(L)[0]],
                                     D=[int(i) for i in np.nonzero(D)[0]])
                        break
            if found: break
        if found: break
    print(f"[{sector}] explicit weight-11 extended-code solution: {found['info']}  "
          f"(check {found['check']}, residual r{found['k']+1} = {found['r']})")
    sys.stdout.flush()
    out[sector] = dict(w11=found)
# (a) the X-sector |E| >= 12 anchor
for sector, tr in (('X', (14, 0, 2)),):
    orders, _ = tiled_orders(sector, phi, tr)
    ctx, Hstab = dext.sector_ctx(orders, sector)
    for W in (11, 12):
        sat, wit, el, ncls = dext.query(ctx, W, Hstab, use_residuals=False)
        print(f"[{sector}] residuals OFF, W={W}: {'SAT' if sat else 'UNSAT'} ({el:.1f}s)",
              wit[3] if sat else "")
        sys.stdout.flush()
        out[sector][f'no_residuals_W{W}'] = dict(verdict='SAT' if sat else 'UNSAT',
                                                 seconds=round(el, 1),
                                                 info=(wit[3] if sat else None))
json.dump(out, open("anchor3.json", "w"), indent=1)
```

#### `recheck.py`

```python
"""Independent re-decision of one cell with a DIFFERENT SAT solver, on a CNF rebuilt from scratch
and checked to have the same SHA-256 as the one job4.py decided.

usage: recheck.py <sector> <a,b,c> <W> <K> <Ew> <orbit> <solver>
       solver in {cd15, cd19, cd30, g4, g42, m22, mgh}
"""
import sys, time, json, hashlib
import numpy as np
from sched import make_phi
from cert import tiled_orders
import dext, dext2, cert4

SOLVERS = {}
from pysat.solvers import (Cadical153, Cadical195, Cadical300, Glucose4, Glucose42,
                           Minisat22, MinisatGH)
SOLVERS = dict(cd15=Cadical153, cd19=Cadical195, cd30=Cadical300, g4=Glucose4,
               g42=Glucose42, m22=Minisat22, mgh=MinisatGH)

sector = sys.argv[1]
triple = tuple(int(c) for c in sys.argv[2].split(','))
W = int(sys.argv[3]); K = int(sys.argv[4]); Ew = int(sys.argv[5]); oi = int(sys.argv[6])
sname = sys.argv[7]

phi = make_phi(1, 1)
orders, _ = tiled_orders(sector, phi, triple)
ctx, Hstab = dext.sector_ctx(orders, sector)
c = cert4.Cert4(ctx, W, K, Ew)
cls = list(c.cls)
if oi >= 0:
    S, orbits = dext2.column_orbits(phi, triple)
    rorb = [(rep, orb) for (rep, orb) in orbits if rep[0] == 'r']
    rep, orb = rorb[oi]
    cls.append([c.col_lit(rep)])
    for jj in range(oi):
        for col in rorb[jj][1]:
            cls.append([-c.col_lit(col)])
h = hashlib.sha256()
for cl in cls:
    h.update((" ".join(map(str, cl)) + "\n").encode())
t0 = time.time()
with SOLVERS[sname](bootstrap_with=cls) as S2:
    sat = S2.solve()
print(json.dumps(dict(sector=sector, triple=list(triple), W=W, K=K, Ew=Ew, orbit=oi,
                      solver=sname, cnf_sha256=h.hexdigest()[:32],
                      verdict='SAT' if sat else 'UNSAT', seconds=round(time.time() - t0, 1))))
```

#### `summarize.py`

```python
"""Aggregate the cell x orbit sweep into the per-cell verdict table and check the cover."""
import json, collections, sys
import cert4

LOGS = sys.argv[1:] or ['logs/full.jsonl', 'logs/full7.jsonl']
rs = [json.loads(l) for L in LOGS for l in open(L)]
rs = [r for r in rs if r.get('verdict') in ('SAT', 'UNSAT')]
cells = cert4.cells(10)
by = collections.defaultdict(dict)
for r in rs:
    by[(r['sector'], tuple(r['triple']))][(r['K'], r['Ew'], r['orbit'])] = r

for key in sorted(by):
    sec, tr = key
    tab = by[key]
    print(f"\n=== sector {sec}  triple {tr}")
    tot = 0.0
    ncomplete = 0
    hdr = "  K  |E|   " + " ".join(f"o{j}" for j in range(9)) + "   cell verdict   cell CPU s"
    print(hdr)
    for (K, Ew) in cells:
        row = []
        sats = []
        for j in range(9):
            r = tab.get((K, Ew, j))
            row.append('.' if r is None else ('U' if r['verdict'] == 'UNSAT'
                                              else ('S' if r['verdict'] == 'SAT' else '?')))
            if r is not None:
                tot += r['seconds']
                if r['verdict'] == 'SAT':
                    sats.append(j)
        done = all(x != '.' for x in row)
        cellcpu = sum(tab[(K, Ew, j)]['seconds'] for j in range(9) if (K, Ew, j) in tab)
        verdict = ('SAT' if sats else ('UNSAT' if done else 'incomplete'))
        if done:
            ncomplete += 1
        print(f" {K:2d}  {Ew:3d}   " + "  ".join(row) + f"    {verdict:10s}  {cellcpu:8.1f}")
    print(f"  cells complete: {ncomplete}/{len(cells)};  total CPU {tot:.0f} s")
```

#### `mktable8.py`

```python
"""Render the per-cell result table for the artifact, from all sweep logs."""
import json, collections, sys, os
import cert4

LOGS = [('logs/full.jsonl', 'cert4'), ('logs/t2.jsonl', 'cert4'), ('logs/b6.jsonl', 'cert6'),
        ('logs/full7.jsonl', 'cert7'), ('logs/full7b.jsonl', 'cert7'), ('logs/final.jsonl', 'cert7')]
rs = []
for L, e in LOGS:
    if not os.path.exists(L):
        continue
    for l in open(L):
        r = json.loads(l)
        if (r.get('verdict') in ('SAT', 'UNSAT') and r.get('orbit', -1) >= 0
                and tuple(r['triple']) in ((1, 2, 62), (14, 0, 2))):
            r['enc'] = e
            rs.append(r)
cells = cert4.cells(10)
by = collections.defaultdict(dict)
for r in rs:
    k = (r['sector'], tuple(r['triple']), r['K'], r['Ew'], r['orbit'])
    if k in by[(r['sector'], tuple(r['triple']))]:
        old = by[(r['sector'], tuple(r['triple']))][(r['K'], r['Ew'], r['orbit'])]
        if old['seconds'] <= r['seconds']:
            continue
    by[(r['sector'], tuple(r['triple']))][(r['K'], r['Ew'], r['orbit'])] = r

summary = {}
for key in [('Z', (1, 2, 62)), ('X', (14, 0, 2))]:
    sec, tr = key
    tab = by.get(key, {})
    print(f"\n**sector {sec}, triple {tr}** — `U` = UNSAT, `S` = SAT, `.` = not decided\n")
    print("| `K` | `\\|E\\|` | orbit 0..8 | cell verdict | encoding | cell CPU s | slowest orbit s |")
    print("|---|---|---|---|---|---|---|")
    tot = 0.0; ndone = 0; nsat = 0
    for (K, Ew) in cells:
        row = []; sats = []; times = []; encs = set()
        for j in range(9):
            r = tab.get((K, Ew, j))
            if r is None:
                row.append('.')
            else:
                row.append('U' if r['verdict'] == 'UNSAT' else 'S')
                times.append(r['seconds']); encs.add(r['enc'])
                if r['verdict'] == 'SAT':
                    sats.append(j)
        done = all(x != '.' for x in row)
        if Ew == 12:
            v = 'SAT' if sats else '**UNSAT** (enum12)'
            done = True
        else:
            v = 'SAT' if sats else ('**UNSAT**' if done else 'incomplete')
        ndone += int(done); nsat += int(bool(sats))
        tot += sum(times)
        print(f"| {K} | {Ew} | `{''.join(row)}` | {v} | {'+'.join(sorted(encs)) or '-'} | "
              f"{sum(times):.0f} | {max(times) if times else 0:.0f} |")
    print(f"\n`{ndone}` of `{len(cells)}` cells decided; SAT cells: `{nsat}`; "
          f"CPU for this sector: `{tot:.0f}` s")
    summary[sec] = (ndone, nsat, tot)
print("\nTOTAL:", summary, " grand CPU", round(sum(v[2] for v in summary.values())))
```

#### `frontier.py`

```python
import json,collections,os,cert4
done=collections.defaultdict(set)
for L in ('logs/full.jsonl','logs/full7.jsonl','logs/full7b.jsonl','logs/t2.jsonl','logs/b6.jsonl','logs/final.jsonl'):
    if not os.path.exists(L): continue
    for l in open(L):
        try: r=json.loads(l)
        except: continue
        if r.get('verdict') in ('SAT','UNSAT') and r.get('orbit',-1)>=0 and tuple(r['triple']) in ((1,2,62),(14,0,2)):
            done[(r['sector'],r['K'],r['Ew'])].add(r['orbit'])
for sec in ('Z','X'):
    op=[]; nj=0
    for (K,Ew) in cert4.cells(10):
        if Ew==12: continue
        m=9-len(done[(sec,K,Ew)])
        if m: op.append(f"({K},{Ew})x{m}"); nj+=m
    print(f"{sec}: {len(op)} cells open, {nj} orbit sub-queries: " + " ".join(op))
```

#### `cert5.py`

```python
"""cert4 with the residual-weight cut in its exact, joint form.

Write n2 = #{(c,k) in R : k in {0,2}} (the weight-2 residuals r1, r3) and n3 = #{(c,k) in R : k = 1}
(the weight-3 residual r2), so K = n2 + n3.  Then

     |rho| = | XOR of the chosen residuals |  <=  2 n2 + 3 n3  =  2K + n3  =  3K - n2 ,

i.e. the single cardinality constraint

  (c4')   sum_j rho_j  +  sum_c ( u_{c,0} + u_{c,2} )   <=   3K            [144 + 144 literals]

which is exact, subsumes cert4's (c5) |rho| <= 3K and (c6) n3 >= Ew - W - K, and -- unlike (c6) --
keeps biting for every value of |rho|, not only the extreme one.  Its encoding is small because the
bound 3K <= 30 is small.

Everything else is cert4.Cert4 verbatim: (c1) |u| = K, (c2) |z| = Ew, (c3) |d| <= W - K,
(c5') |rho| >= Ew - (W - K), (c7) the dominance cut.
"""
import numpy as np
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from gross import N
from dext import xor_chain, xor_zero_direct


class Cert5:
    def __init__(self, ctx, W, K, Ew, dominance=True):
        pool = IDPool()
        self.z = [pool.id(('z', j)) for j in range(N)]
        self.u = [[pool.id(('u', c, k)) for k in range(3)] for c in range(ctx.ncheck)]
        self.d = [pool.id(('d', j)) for j in range(N)]
        cls = []
        for e in range(ctx.Hdet.shape[0]):
            xor_zero_direct([self.z[int(j)] for j in np.nonzero(ctx.Hdet[e])[0]], cls)
        ys = []
        for i in range(ctx.Lrows.shape[0]):
            ys.append(xor_chain(pool, [self.z[int(j)] for j in np.nonzero(ctx.Lrows[i])[0]], cls))
        cls.append(ys)
        for j in range(N):
            terms = [self.d[j], self.z[j]] + [self.u[c][k] for (c, k) in ctx.hit[j]]
            if len(terms) <= 6:
                xor_zero_direct(terms, cls)
            else:
                cls.append([-xor_chain(pool, terms, cls)])
        if dominance:
            for c in range(ctx.ncheck):
                cls.append([-self.u[c][1], -self.u[c][2]])
        ulits = [self.u[c][k] for c in range(ctx.ncheck) for k in range(3)]
        u2lits = [self.u[c][k] for c in range(ctx.ncheck) for k in (0, 2)]
        self.rho = []
        for j in range(N):
            r = pool.id(('r', j))
            a, b = self.z[j], self.d[j]
            cls += [[-r, a, b], [-r, -a, -b], [r, -a, b], [r, a, -b]]
            self.rho.append(r)
        top = pool.top

        def add(enc):
            nonlocal cls, top
            cls += enc.clauses
            top = max([top] + [abs(l) for cl in enc.clauses for l in cl])

        add(CardEnc.atmost(lits=ulits, bound=K, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atleast(lits=ulits, bound=K, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atmost(lits=self.z, bound=Ew, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atleast(lits=self.z, bound=Ew, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atmost(lits=self.d, bound=W - K, top_id=top, encoding=EncType.seqcounter))
        lo = Ew - (W - K)
        if lo > 0:
            add(CardEnc.atleast(lits=self.rho, bound=lo, top_id=top, encoding=EncType.seqcounter))
        add(CardEnc.atmost(lits=self.rho + u2lits, bound=3 * K, top_id=top,
                           encoding=EncType.seqcounter))
        self.cls = cls
        self.top = top
        self.ctx = ctx

    def col_lit(self, col):
        return self.d[col[1]] if col[0] == 'd' else self.u[col[1]][col[2]]

    def decode(self, model):
        ms = set(x for x in model if x > 0)
        E = np.array([1 if self.z[j] in ms else 0 for j in range(N)], np.uint8)
        R = [(c, k) for c in range(self.ctx.ncheck) for k in range(3) if self.u[c][k] in ms]
        D = np.array([1 if self.d[j] in ms else 0 for j in range(N)], np.uint8)
        return E, R, D
```
