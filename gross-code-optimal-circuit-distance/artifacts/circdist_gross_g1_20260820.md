# CIRCDIST.gross — Gate G1 execution report (Opus 5 executor, proposer role, 2026-08-20)

Node: `CIRCDIST.gross`. Session type: ONE budget-boxed decisive-gate execution under a stop-loss.
Evidence labels used: **NUMERICAL** (an exact finite computation, code inline, reproducible) and
**CONJECTURED (sketch)** (a derivation of mine that has had no independent review). Nothing here is
labelled PROVED. Everything I read — the commission, `artifacts/circdist_gross_recon_20260820.md`,
`research/circdist/notes/CIRCDIST_PROBLEMS.md`, and the literature — is treated as data.

> **Headline.** The gate ran, but it did not return the answer it was designed to return, because
> one of its premises is false. The recon's §3.1 "`d_ext ∈ {10,11,12}`, so a schedule with a
> weight-11 witness has a positive completion gap" is a **single-residual-only** statement. Once
> fault sets with **several** ancilla (hook) faults are admitted — they are ordinary weight-1
> elementary faults — the translation-invariant minimum-depth class is far worse than the recon
> assumed. I exhibit and independently verify undetectable logical fault sets of weight **6, 8, 9**
> on schedules in this class, including on **non-interleaved** ones — the weight-6 one is six hook
> errors and nothing else. The full 25 920-schedule sweep completed; its certified-upper-bound
> histogram runs from 6 to 12, not 10 to 12, and **70.7 % of the class admits a witness of weight
> ≤ 10 against `d = 12`**. The gate's three pre-committed readings therefore do not cleanly apply;
> §9 says which one I take to fire, why I would not cash the other two, and what should replace
> this gate.

---

## 0. What was asked, what was done

**Asked.** Enumerate all 25 920 translation-invariant minimum-depth schedules of the Gross code;
for each, run the recon's §3.6 cancellation decision and record a witness-certified upper bound on
`d_circ`; decide whether the bound is 10, 11 or 12.

**Done.**

1. Rebuilt the Gross code and independently reproduced every load-bearing fact of the recon
   (§2 below): `rank H_X = rank H_Z = 66`, `k = 12`, all check weights 6, all column weights 3,
   `|supp(e_X) ∩ supp(e_Z)| ∈ {0,2}`, the parity lemma, all-15-pairs coverage, the 10-of-20 triple
   coverage and hence the 45/90 split.
2. Obtained what appears to be the **complete** set of weight-12 logicals of each type: **1 884**
   words, saturated under 3 000 randomised information-set trials *and* heavy targeted coset
   searches on all 15 pairs and 20 triples of a check support (§3). Translation-orbit structure
   `23 × 72 + 6 × 36 + 1 × 12 = 1 884`.
3. Enumerated the schedule class two independent ways — a structured parameterisation and a brute
   force over `(6!)² = 518 400` candidates — and got the identical set of **25 920**
   (2 592 non-interleaved, 23 328 interleaved), each verified legal on the explicit 864-edge Tanner
   graph (§4).
4. Re-derived the last-round detector error model from scratch, classified the elementary Z-sector
   fault columns, and proved (sketch) that the two "mixed" CNOT faults collapse onto columns
   already in the list (§5).
5. Ran the recon's §3.6 family (**exactly one** ancilla fault) exhaustively over all 25 920
   schedules — 10 seconds — giving the histogram `{10: 3 852, 11: 20 460, 12: 1 608}` (§6).
6. **Discovered that this family is not the binding one**, built an independent Pauli-frame circuit
   simulator to adjudicate, and confirmed multi-residual witnesses of weight 6/8/9/10 (§7).
7. Ran the enlarged family over **all 25 920 schedules** (979 s, complete — no partial sweep was
   needed) and report the histogram, the comparison against the timing-free relaxation, and the
   extremal schedules (§8):

   | certified upper bound on `d_circ` | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
   |---|---|---|---|---|---|---|---|
   | schedules | 360 | 0 | 6 408 | 2 324 | 9 232 | 6 068 | 1 528 |

8. Verified one witness per weight class, in both CSS sectors, end-to-end against the independent
   simulator; all pass (§7).

**Not done** (stop-loss, stated honestly): no lower-bound certification of any kind. Every number in
§6–§8 is an **upper** bound obtained by exhibiting a witness. No claim of the form `d_circ = w`
appears anywhere in this report.

---

## 1. Fixed setup

Gross code `Q = [[144,12,12]]`, bivariate bicycle, `ℓ = 12`, `m = 6`, `G = Z_12 × Z_6` of order 72,

```
A = x³ + y + y² ,   B = y³ + x + x² ,   H_X = [A | B] ,   H_Z = [Bᵀ | Aᵀ] .
```

Data qubits: left half `0..71` (a free `G`-set), right half `72..143`. Checks: 72 X, 72 Z.

`gross.py` (inlined in §11) builds these with exact `uint8` mod-2 arithmetic and the RREF /
nullspace routines used everywhere below. Verification output:

```
{'rankHX': 66, 'rankHZ': 66, 'k': 12, 'overlaps': [0, 2]}
```

**Monomial-labelled Tanner incidences** (derived, then asserted against the explicit matrices for
all 72 checks and all 144 qubits in `tanner.verify()`):

| | left data | right data |
|---|---|---|
| X-check `g` touches | `g − A_i`, `A = {x³, y, y²}` | `g − B_i`, `B = {y³, x, x²}` |
| Z-check `g` touches | `g + B_i` | `g + A_i` |

---

## 2. Independent reproduction of the recon's groundwork — NUMERICAL

I re-derived rather than reused each of these.

**2.1 Parity lemma.** Every column of `H_X` has weight 3, so the sum of all 72 rows is the all-ones
vector, hence `1 ∈ rowspace(H_X)` and every `v ∈ ker(H_X)` has even weight. Same for `H_Z`.
Verified: `all-ones in rowspace(HX): True | in rowspace(HZ): True`.

**2.2 A sharper structural fact the recon did not state.** For a weight-12 logical `L` and any
check `c`, `|L + c| = 12 − 2|L ∩ c| + 6 ≥ 12` (minimum distance), so

> **`|L ∩ supp(c)| ≤ 3` for every weight-12 logical `L` and every check `c`.**

Confirmed exactly on the complete pool: the intersection histogram with a fixed Z-check is
`{0: 1191, 1: 496, 2: 145, 3: 52}` — never 4, 5 or 6. This is what caps the "gain" of any single
residual at 2 (§7) and is the reason the class bottoms out at 6 rather than lower.

**2.3 Pair and triple coverage.** With the complete weight-12 pool:

```
Z  pairs covered: 15/15   triples covered: 10/20   complement-closed: True
X  pairs covered: 15/15   triples covered: 10/20   complement-closed: True
   -> 5 of the 10 balanced 3|3 splits are covered  =>  45 of the 90 residual sets give <= 10
```

This reproduces the recon §3.2/§3.3 and [SBB26 Prop. 4]'s two published numbers exactly, and the
check supports agree with the recon's (`[3,6,12,73,74,90]` for Z, `[4,5,54,75,132,138]` for X).

---

## 3. The weight-12 logical pool — NUMERICAL, saturated

`pool.py` + `saturate.py`. Randomised information-set decoding over `ker(H_X)` (dim 78) harvesting
words of weight ≤ 12 from single rows, pairs and triples of a systematic generator, closed under the
72 translations; then a targeted coset search that *prescribes* the 1s on each of the 15 pairs and
20 triples of a check support and runs 250 further ISD trials per subset.

```
[Z-log] G-closed pool size after [250,500,...,3000] ISD trials:
    [1884, 1884, 1884, 1884, 1884, 1884, 1884, 1884, 1884, 1884, 1884, 1884]
[Z-log] after heavy targeted coset search on all 15 pairs + 20 triples of one check: 1884 -> 1884
[Z-log] 1884 words; translation-orbit size histogram: {72: 23, 36: 6, 12: 1}
[X-log] ... identical numbers ...
```

The pool is flat from the very first 250 trials and does not move under the targeted searches. I
therefore treat it as the complete set of weight-12 logicals — label **NUMERICAL (saturated
search; completeness not certified)**. Note that upper-bound witnesses are one-sided, so pool
incompleteness could only make my bounds *larger*, never invalid.

---

## 4. The schedule class — NUMERICAL, enumerated twice

At minimum depth the Tanner graph of `H_XZ` is 6-regular bipartite (864 edges), so `χ' = 6` by
König; six CNOT layers, depth 8 with prep+measure. Every check and every data qubit therefore uses
**each** of the layers `1..6` exactly once, which pins the CNOT order of every check to its layer
order — a fact I use constantly below.

A translation-invariant schedule assigns one layer to each of the 12 edge orbits. Writing
`P = σ(X-edges to left data)`, the four constraints (X-check, Z-check, left-qubit, right-qubit)
force `σ(X→right) = Pᶜ`, `σ(Z→left) = Pᶜ`, `σ(Z→right) = P`. So a schedule is exactly

```
(P, α, β, γ, δ)   |P| = 3 ;  α: A-monos ↪ P ;  β: B-monos ↪ Pᶜ ;  γ: B-monos ↪ Pᶜ ;  δ: A-monos ↪ P
```

Count `20 · 6⁴ = 25 920`. Cross-checked by brute force over all `(6!)² = 518 400` pairs of
X-/Z-check orderings:

```
brute-force count over (6!)^2 = 518400 candidate pairs: 25920
distinct (P,alpha,beta,gamma,delta) tuples: 25920
matches structured enumeration: True
```

Non-interleaved (LRC-like) ⟺ `P ∈ {{1,2,3},{4,5,6}}` ⟹ **2 592**; interleaved **23 328**.
40 random members were verified legal directly on the 864-edge graph. All three counts agree with
the recon §3.5.

---

## 5. Fault model, exactly as covered — CONJECTURED (sketch) for the reduction, NUMERICAL for the columns

CSS separation: a CNOT circuit maps the X-sector and the Z-sector into themselves, and X-check
detectors are sensitive only to Z-type faults. So a minimum-weight undetectable logical may be taken
purely Z-type (project any witness onto its Z-parts). I treat the two sectors independently and take
the minimum.

**Z-sector, last round `R`, ideal final data readout, earlier rounds fault-free.** Let `E` be the net
data Z error at readout and `f_e` the flip of X-check `e`'s round-`R` outcome. Then

```
D_e^(R)     = f_e ,
D_e^(final) = (H_X E)_e + f_e ,
```

so *no detector fires* ⟺ `E ∈ ker(H_X)` **and** `f = 0`; the fault set is logical ⟺
`E ∉ rowspace(H_Z)`.

**The elementary Z-sector fault columns of one round** (each of circuit weight 1):

* **(i) data fault** — Z on data `q` born after CNOT layer `j`. It flips `m_e` for every X-check `e ∋ q`
  with `layer(e,q) > j`. Since `q` has exactly 3 X-CNOTs, only the four *suffixes* of that ordered
  triple are realisable, so there are 4 distinct columns per qubit.
* **(ii) residual (hook) fault** — Z on a Z-check ancilla `c` between layers `l−1` and `l`. It is
  invisible to `c`'s own Z-basis measurement and deposits Z on `S_l(c) = {i_l,…,i_6}`, each qubit at
  the instant of its own Z-CNOT.
* **(iii) measurement fault** — Z on an X-check ancilla `e` (prep, idle, measurement, or the `ZI`
  component of one of its CNOTs). It flips `m_e` only.

*The two mixed CNOT faults collapse.* A `ZZ` fault on a (Z-check, data) CNOT at layer `j` puts Z on
the ancilla and on `i_j`; propagating, the ancilla error deposits Z on `i_{j+1}…i_6` and the total
data error is `{i_j} ∪ S_{j+1} = S_j` with exactly the birth times of column (ii) at position `j` —
the same column. A `ZZ` fault on an (X-check `e`, data `q`) CNOT gives a measurement fault on `e`
plus a data fault on `q` born *after* `e`; since "`q` alive at `e`" and "`e` measurement-flipped"
contribute identically to `f_e`, this equals column (i) with `q` born *just before* `e` — again the
same column. **Hence (i)–(iii) exhaust the sector.** (CONJECTURED (sketch).)

**Confining faults to the last round is WLOG for minimum weight.** Detectors are *differences* of
consecutive rounds, so a persistent data error fires each of its X-checks exactly once, split
between the round of birth and the next; moving the birth to the start of round `R` removes the
earlier-round events and preserves the round-`R` ones. I did not turn this into a full proof; the
sweep's scope statement (§7) records it as a restriction.

**Cost accounting.** Because measurement faults can flip any single detector at cost 1, for a fixed
choice of ancilla faults `A` and data faults `Q`,

> **weight = |A| + |Q| + wt(f)** ,  `f` = the residual detector pattern after `A` and `Q`.

**The key reduction (this is the recon's §3.6, re-derived and put in a usable form).** For a qubit
`q` carrying an error, let `θ_q ∈ {0,1,2,3}` be the number of `q`'s X-CNOTs that fire *before* the
error is born. Since `q`'s three X-checks are ordered by layer, "alive at the rank-`r` X-check" ⟺
`r > θ_q`, so `q`'s contribution to `f` is the top-`(3−θ_q)` suffix of its X-check triple. Then

```
f = Σ_{q}  mask(q, θ_q) ,     mask(q,θ) = XOR of q's X-checks of rank ≥ θ ,
θ_q free in {0,1,2,3} for a data fault ;  θ_q forced by the schedule for a hook-deposited qubit.
```

For a **left** data qubit the three X-CNOT layers are exactly `P` and the three Z-CNOT layers exactly
`Pᶜ` (and mirrored on the right). Consequently the rank of an X-check at a qubit depends only on the
*monomial*, i.e. only on the rank-permutations `ᾱ, β̄ ∈ S₃`; and the forced `θ` of a hook-deposited
qubit depends only on which **slot** of the residual check it occupies. That is what makes a
25 920-schedule sweep tractable.

---

## 6. The recon's family (exactly one hook fault), exhaustively — NUMERICAL

`engine.py` + `sweep.py`. Within this family the arithmetic is rigid. With `L` a weight-12 logical
and `S = S_l(c)`, the data faults are `Q = L Δ S` and

```
weight = 1 + |L Δ S| + wt(f) ,   |L Δ S| = 12 + |S| − 2|L ∩ S| ≥ 6 + |S|  (since |L ∩ c| ≤ 3)
```

so the minimum achievable is **10**, at `|S| = 3`, `L ∩ c = S`, `wt(f) = 0` — the unique route to 10.
Weight 11 arises three ways: `|S| = 2` with `S ⊆ L`; `|S| = 4` with `|L ∩ S| = 3`; or `|S| = 3` with
one measurement fault.

Implementation: for each of the `6 × 6 = 36` rank-permutation pairs and each pool logical meeting the
residual check in ≥ 2 points (197 of 1 884), a meet-in-the-middle over the free `θ`'s decides
`min wt(f) ∈ {0,1}` for every assignment of the forced `θ`'s; the 25 920 schedules are then table
lookups. Total runtime **10 s**.

```
overall histogram  : {10: 3852, 11: 20460, 12: 1608}
Z-sector histogram : {10: 2340, 11: 21588, 12: 1992}
X-sector histogram : {10: 2340, 11: 21588, 12: 1992}
interleaved (23328): {10: 3852, 11: 17868, 12: 1608}
non-interleaved(2592): {11: 2592}
```

**This is a correct set of upper bounds, and it is the number the gate asked for.** It is also
*misleading*, and the next section says why: every one of the 2 592 non-interleaved schedules is
listed at 11 here, yet all of them provably admit a weight-10 witness — outside this family.

---

## 7. The anomaly, and the verdict — NUMERICAL

**How it surfaced.** [SBB26 Prop. 5] (recon A5) states that a uniformly tiled circuit has
`d_circ ≤ 10`, and the recon carried this over as "all 25 920 have `d_ext ≤ 10`". My single-residual
sweep contradicted that for the non-interleaved members. Tracing it: for `P = {1,2,3}` the residual
check's CNOT order puts all three *right* neighbours first and all three *left* neighbours last, so
the weight-3 residual is always the pure-half split `(0,1,2)` or `(3,4,5)` — and the pure-half splits
are exactly two of the **ten uncovered** triples. So no single hook fault can reach 10 there. The
`≤ 10` must come from somewhere else.

**Where it comes from.** Nothing forbids *several* hook faults. Each is an ordinary weight-1 fault.
If pairwise-disjoint residuals `r_1,…,r_k` all sit inside a common logical `L`, then

```
weight before detectors = k + (12 − Σ|r_i|) = 12 − gain ,   gain := Σ (|r_i| − 1) ,
```

and since `|L ∩ c| ≤ 3` each residual contributes gain ≤ 2. A timing-free packing search (`relax.py`)
found `gain` up to **6**, i.e. skeletons of base weight **6**.

**This looked like a formula bug, so I adjudicated it with an independent simulator.** `sim.py`
takes a schedule, materialises the literal 864-CNOT circuit as a list of `(layer, control, target)`
gates, checks that each of the 288 qubits is used exactly once per layer, and propagates Pauli
frames through it — `z[c] ^= z[t]` for the Z-sector, `x[t] ^= x[c]` for the X-sector — reading the
detector flips off the ancilla frames. It shares **no code** with the analytic engine: no masks, no
ranks, no suffix formula.

**Verdict: not a formula bug. The low-base skeletons are real; what saves the distance is `wt(f)`,
and it does not save it as much as the recon's framework assumed.** The first check was the LRC
schedule `(P={1,2,3}, α=(1,2,3), β=(4,5,6), γ=(4,5,6), δ=(1,2,3))`, where the maximum gain is only 2,
base weight 10 — and the simulator confirms `wt(f) = 0`, i.e. a genuine **weight-10** undetectable
logical, exactly reproducing A5. But on other schedules gains of 3, 4 and 6 occur, and the detector
cancellation does *not* always cost enough to bring them back up.

**A fully verified weight-8 witness on a NON-INTERLEAVED schedule.**

```
schedule: P = {1,2,3},  α = (1,2,3),  β = (4,5,6),  γ = (6,4,5),  δ = (2,1,3)
fault set (Z-sector, 8 elementary faults, all in the last round):
   Z on the ancilla of Z-checks  4, 20, 37, 59, each between CNOT layers 4 and 5   (4 faults)
   Z on data qubits  78, 102, 117, 141, born after the last CNOT layer             (4 faults)
   no measurement faults
independent simulator:
   {'nfaults': 8, 'silent_round': True, 'silent_final': True,
    'E_in_kernel': True, 'nontrivial': True, 'Ewt': 12}
```

Every round-`R` X-check detector is silent, every final-readout detector is silent, and the residual
data error is a weight-12 **nontrivial** Z logical. So `d_circ ≤ 8` for that schedule.

**One witness per weight class, both sectors, all independently verified** (`batch_verify.py`):

```
class  8: sector Z  |A|=4 |Q|=4  wt(f)=0  -> nfaults 8  silent True/True  nontrivial True  |E|=12  PASS
class  9: sector X  |A|=3 |Q|=6  wt(f)=0  -> nfaults 9  silent True/True  nontrivial True  |E|=12  PASS
class 10: sector Z  |A|=2 |Q|=8  wt(f)=0  -> nfaults 10 silent True/True  nontrivial True  |E|=16  PASS
class 11: sector Z  |A|=1 |Q|=10 wt(f)=0  -> nfaults 11 silent True/True  nontrivial True  |E|=12  PASS
class 12: trivial witness (12 data faults born after the last layer) -> PASS in both sectors
```

**Consistency with the literature.** There is *no* contradiction. [SBB26] Prop. 4 (`≤ 11`,
non-interleaved) and Prop. 5 (`≤ 10`, uniform tiling) are **upper** bounds; `≤ 8` refines them. Their
conjectured distance-11 circuit is *three-colour tiled*, hence **not** translation-invariant and
**not** a member of this class, so nothing here bears on it. What is refuted is only the recon's
§3.1 claim that `d_ext ∈ {10,11,12}` for this code — that claim is true of single-residual
configurations and false in general.

---

## 8. The full sweep — NUMERICAL

### 8.1 Scope of the witness family `W` (stated so the "no smaller witness" language is auditable)

A fault set is in `W` iff, in one CSS sector:

* all faults lie in the final syndrome-extraction round;
* it contains an arbitrary set `A` of residual-check ancilla faults, at any positions `l ∈ {1..6}`;
* data faults with free birth times;
* **at most 2** measurement faults (`CAP = 2`);
* the net data error lies in the coset `L + ⟨checks used with a prefix representative⟩`, with `L`
  running over the complete weight-12 logical pool;
* the residual packings are enumerated by DFS keeping at most 25 packings per gain level per
  (logical orbit, residual structure) and at most 20 000 DFS nodes.

Everything the sweep reports is a **witness**, so every number is a rigorous upper bound on
`d_circ`. The two truncations (`CAP = 2`, packing caps) and the restriction to weight-12 logical
cosets can only make the reported bound **too large**, never too small.

### 8.2 Translation quotient, and its independent validation

The code and every schedule in the class are invariant under `G = Z_12 × Z_6` (order 72) — verified
directly on the explicit Tanner graph, by checking for 25 random schedules, all 72 translations and
three base checks that the whole `(side, monomial, layer)` profile is translation-invariant. Hence
the net logical `L` may be restricted to **one representative of each of the 30 `G`-orbits**.

Validated empirically as the commission requires: for 12 random schedules the sweep was rerun with
`L` ranging over the **full 1 884** logicals instead of the 30 orbit representatives.

```
check 1 (schedule is G-invariant on the explicit Tanner graph): True
reps: quotient 30  full 1884
   ... 12 schedules ... quotient 11/8/8/8/11/12/8/10/11/9/11/10  full-pool identical ...
mismatches: 0
```

### 8.3 Result

Full sweep: **25 920 / 25 920 schedules, 979 s**, `CAP = 2`, 30 logical orbit representatives.

**Histogram of witness-certified upper bounds on `d_circ` over the whole class**

| certified upper bound | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|
| **all 25 920** | 360 | 0 | 6 408 | 2 324 | 9 232 | 6 068 | 1 528 |
| interleaved (23 328) | 360 | 0 | 4 968 | 2 324 | 8 368 | 5 780 | 1 528 |
| non-interleaved (2 592) | 0 | 0 | 1 440 | 0 | 864 | 288 | 0 |

Z-sector taken alone: `{6: 240, 8: 3876, 9: 1760, 10: 8824, 11: 9352, 12: 1868}`. (The X-sector pass
is seeded with the Z-sector bound as its incumbent, so the "X" column of `analyze.py` is the running
minimum over both sectors, i.e. the overall row above, not a standalone X-sector histogram. The
class is closed under the code's ZX duality, so I expect the standalone X histogram to equal the Z
one; I did not spend the 16 min to confirm it.)

**Comparison with the timing-free relaxation.** Let `r(s) = 12 − max gain` be the best weight
reachable by the same residual packings *ignoring all detectors* (an upper bound on `d_ext`), and
`c(s)` the circuit-level certified bound. Within the family `W`, `c(s) − r(s)` is the amount the
detector timing costs — the family-level completion gap.

```
relaxation r(s) : {6: 15488, 7: 1504, 8: 6592, 9: 1248, 10: 1024, 11: 64}
blocking c - r  : {0: 4032, 1: 1568, 2: 5560, 3: 4124, 4: 5744, 5: 4012, 6: 880}

joint (r, c):
        c=6      c=8      c=9      c=10     c=11     c=12
 r=6    360      2896     2100     5296     3956     880
 r=7    0        696      72       552      128      56
 r=8    0        2816     144      2080     1232     320
 r=9    0        0        8        520      480      240
 r=10   0        0        0        784      208      32
 r=11   0        0        0        0        64       0
```

So the timing **does** obstruct: only 4 032 of 25 920 schedules (15.6 %) let the cheapest
timing-free skeleton close, and for 880 schedules it costs 6. That is the completion-gap mechanism
operating at scale — but see §9 for why this is *not* a demonstration that `d_circ > d_eff`.

**Extremes.**

*Worst schedule (lowest bound, 6; 360 schedules).* `P = {1,3,5}`, `α = (1,3,5)`, `β = (2,4,6)`,
`γ = (2,6,4)`, `δ = (5,1,3)`. The Z-sector witness needs **no data faults at all**:

```
6 elementary faults, all Z on Z-check ancillas between CNOT layers 2 and 3:
    checks 1, 15, 29, 37, 51, 65        (l = 3, i.e. residual S_3 on each)
independent simulator:
    {'nfaults': 6, 'silent_round': True, 'silent_final': True,
     'E_in_kernel': True, 'nontrivial': True, 'Ewt': 24}
```

Six hook errors, nothing else, and they compose into an undetectable weight-24 nontrivial logical
with every detector silent. `d_circ ≤ 6` — half the code distance.

*Best schedules (highest bound, 12; 1 528 schedules, all interleaved).* e.g. `P = {1,2,5}`,
`α = (1,2,5)`, `β = (3,6,4)`, `γ = (3,6,4)`, `δ = (1,2,5)`. For these, `W` contains no witness below
the trivial one: 12 data faults born after the last CNOT layer, which has `f = 0` because no X-check
CNOT fires afterwards, and net error a weight-12 logical (verified in both sectors). These 1 528 are
the only candidates in the class for `d_circ = 12`, and §9 says how little that means.

*Best non-interleaved schedules (bound 11; 288 of 2 592).* No non-interleaved schedule in the class
reaches 12 within `W`.

---

## 9. Which pre-committed reading fires

The gate's three readings were:

> (a) ALL schedules give ≤ 10 ⟹ `D* = 11` strong prior for this subclass, and the Gross code is a
> bad hunting ground for `CIRCDIST.lift`'s strict-inequality example at weight 11+.
> (b) ANY schedule gives exactly 11 ⟹ the completion-gap mechanism is constructive at scale.
> (c) ANY schedule gives 12 ⟹ report it and say what remains to certify `d_circ = 12`.

**Literally, (b) and (c) both fire:** 6 068 schedules certify at 11 and 1 528 at 12. **I do not think
either should be cashed, and I recommend the dispatcher record reading (a) in its *second* half
only.** Reasons, in order of force:

1. **The trigger clause is "certified no weight-≤10 witness *by your method's scope*", and my scope
   is now known to be loose in exactly this direction.** The narrower single-residual family (§6)
   certified all 2 592 non-interleaved schedules at 11; the enlarged family `W` then found weight-8
   witnesses for 1 440 of them and weight-10 for 864 more. The same thing can happen again: `W` caps
   measurement faults at 2, restricts the net error to weight-12 logical cosets, truncates packing
   enumeration, and uses one round. A "12" here is far more likely to be a scope artifact than a
   distance-12 schedule.

2. **The premise the gate was built on is false.** The gate discriminated by comparing the circuit
   bound against "`d_ext ≤ 10`, guaranteed for this class by A5". `d_ext` for this class is not ≤ 10
   in any useful sense — the timing-free relaxation reaches **6** for 15 488 of the 25 920 schedules.
   So "bound = 11" no longer implies `g ≥ 1`; it implies nothing at all without a lower bound on
   `d_circ`, which this session did not attempt and which the stop-loss forbade.

3. **The substantive finding is a negative one about the subclass, and it is robust** (it rests only
   on exhibited, simulator-verified witnesses, which cannot be wrong in the unsafe direction):

   > **The translation-invariant minimum-depth schedules of the Gross code are a bad subclass.**
   > 70.7 % of them (18 324 / 25 920) admit an undetectable logical fault set of weight ≤ 10,
   > 35.1 % (9 092) of weight ≤ 9, 26.1 % (6 768) of weight ≤ 8, and 360 of weight 6 — with `d = 12`. Uniform tiling is not merely
   > "`≤ 10`" as [SBB26 Prop. 5] states; it is often far worse, and the mechanism is *composition of
   > several hook errors*, which the residual-set formalism prices correctly only when one hook is
   > used.

4. **For `CIRCDIST.lift`**: the second half of reading (a) is confirmed, and more strongly than
   anticipated. This subclass is a bad hunting ground for the wanted strict-inequality example, not
   because the gap is always zero but because the *absolute* distances are so low that a
   demonstration of `d_circ > d_eff` here would be uninteresting. The `c − r` table is, however,
   direct quantitative evidence that the timing obstruction is real and generic: only 15.6 % of
   schedules let the cheapest timing-free mechanism close. If `CIRCDIST.lift` wants a testbed for the
   voltage/monodromy obstruction, this table is the right object; the Gross code is simply the wrong
   place to want a *large* `d_circ`.

5. **For `CIRCDIST.gross` itself, the node's route table should be re-priced.**
   * Route 3 (`symmetric-subclass-exhaustion`) is **discharged as a distance question and should be
     closed**: the optimum over the translation-invariant minimum-depth class is certainly ≤ 12 and
     the class is dominated by schedules an order of magnitude worse. It cannot contain a
     `d_circ = 12` witness that survives a real lower-bound check, and it was never going to
     discriminate `D* = 11` vs `12`. Its residual value is the `c − r` table above.
   * Route 2 (`gap-forcing-no-go`) gets **harder**, not easier: any no-go must now also handle
     multi-hook composition, which the recon's §3.6 machinery does not price.
   * Route 1 (`candidate-circuit-exact-certification`) rises in relative value, because it is the
     only route that touches a circuit anybody believes is good, and because §7 shows the candidate
     (three-colour tiled, *not* translation-invariant) is genuinely outside everything measured here.
   * **New and cheap:** apply exactly this multi-hook packing search to the *three-colour-periodic*
     class (index-3 subgroup, 36 edge orbits) and to the SBB candidate itself once its schedule is
     recovered. If multi-hook composition also bites there, the published `d_circ = 11` conjecture is
     in doubt and that is a high-value finding; if it does not, we learn what the three-colouring is
     buying. I would run this before anything else on the node.

**What would remain to certify `d_circ = 12` for one of the 1 528 top schedules** (asked for
explicitly by reading (c)): (i) enumerate weight-14 and weight-16 logical cosets, not just weight-12;
(ii) lift the measurement-fault cap from 2 to unbounded; (iii) remove the packing-enumeration
truncation; (iv) drop the one-round restriction, or prove the reduction of §5 properly; (v) then, and
only then, an exact minimum-distance certification on the full circuit-level detector error model
(≈ 1 500 columns per round per sector before multi-round expansion) showing no undetectable logical
of weight ≤ 11 — the expensive computation [Webster–Jacob–Higgott] warn about. Steps (i)–(iv) are
mechanical and would take one session; step (v) is the real cost and I would not fund it for this
subclass given (3).

---

## 10. Corrections to the round-1 recon

1. **§3.1 is wrong as stated.** "`d_ext ∈ {10,11,12}` for this code, and 11 can only ever be produced
   by a weight-2 residual inside a weight-12 logical" holds only for configurations using a *single*
   residual. Several disjoint residuals inside one weight-12 logical reduce the count to `12 − gain`
   with `gain` observed up to 6. The parity lemma itself (§3.1's first half) is correct and I use it.
2. **§3.5's rider "By A5 all of these have `d_ext ≤ 10`" is the right conclusion for the wrong
   reason.** A5's `≤ 10` cannot come from a single residual for the non-interleaved members of this
   class — their weight-3 residual is always a pure-half split, which is one of the ten *uncovered*
   triples. It comes from two disjoint weight-2 residuals.
3. **§3.6's syndrome formula is correct** where it applies, and I re-derived it independently; my
   `θ`-and-rank form is equivalent. But its consequence list understates the adversary: the "at most
   six X-checks with ten nested 4-way choices" picture assumes one hook fault.
4. **New structural fact worth recording:** `|L ∩ supp(c)| ≤ 3` for every weight-12 logical and every
   check. This is a one-line consequence of `d = 12` and it is what caps a single residual's gain at
   2, hence what stops this class from being even worse than 6.
5. **A5's "uniform tiling" is exactly this class**, and the recon's reading of it as a `d_ext`
   statement is fine; but `d_ext` for this class is *much* smaller than 10, so A5 is far from tight.
6. The recon's §3.2/§3.3/§3.5 numbers (15/15 pairs, 10/20 triples, 45/90, 25 920/23 328/2 592) all
   reproduce exactly. So do [SBB26]'s two published numbers.

---

## 11. Reproduction

Python 3.9 + numpy only. Files below are the complete pipeline; total runtime ≈ 20 min, of which
the final sweep is ≈ 18 min. Save each block under the given name in one directory and run in order:

```
python3 gross.py        # code + rank/commutation checks
python3 saturate.py     # weight-12 logical pools (writes poolZ.npy, poolX.npy)
python3 tanner.py       # incidence verification + 25920 schedule enumeration
python3 sweep.py        # single-residual family, all 25920 schedules  (10 s)
python3 relax.py        # timing-free multi-residual relaxation
python3 probe2.py       # the anomaly probe
python3 verify_orbit.py # translation-quotient validation
python3 full.py         # the full sweep (writes full.pkl)
python3 batch_verify.py full.pkl   # independent simulator verification, one witness per class
python3 analyze.py full.pkl        # histograms and tables
```

**Reproduction was validated end-to-end**: the fourteen files below were extracted *back out of this
markdown file* into an empty directory and re-run. `gross.py`, `tanner.py` and `saturate.py`
reproduce their quoted output exactly; `sweep.py` reproduces `{10: 3852, 11: 20460, 12: 1608}`
exactly; and `batch_verify.py` re-verified one witness per weight class 6/8/9/10/11/12 against the
independent simulator, all PASS.


### `gross.py`

```python
"""Gross code [[144,12,12]] construction + F2 linear algebra. Exact, numpy uint8 only."""
import numpy as np, itertools

ELL, EM = 12, 6
NG = ELL * EM          # 72 group elements
N = 2 * NG             # 144 data qubits (left half 0..71, right half 72..143)

def gidx(i, j):
    return (i % ELL) * EM + (j % EM)

def mono(a, b):
    """matrix of multiplication by x^a y^b : P[g+s, g] = 1."""
    P = np.zeros((NG, NG), np.uint8)
    for i in range(ELL):
        for j in range(EM):
            P[gidx(i + a, j + b), gidx(i, j)] = 1
    return P

# A = x^3 + y + y^2 ; B = y^3 + x + x^2
A_MONOS = [(3, 0), (0, 1), (0, 2)]      # "A1,A2,A3"
B_MONOS = [(0, 3), (1, 0), (2, 0)]      # "B1,B2,B3"
A = sum(mono(*m) for m in A_MONOS) % 2
B = sum(mono(*m) for m in B_MONOS) % 2
HX = np.concatenate([A, B], 1).astype(np.uint8)
HZ = np.concatenate([A.T * 0 + B.T, A.T], 1).astype(np.uint8)
HZ = np.concatenate([B.T, A.T], 1).astype(np.uint8)


def rref(Mat):
    Mat = Mat.copy() % 2
    rows, cols = Mat.shape
    piv = []
    r = 0
    for c in range(cols):
        pr = None
        for rr in range(r, rows):
            if Mat[rr, c]:
                pr = rr
                break
        if pr is None:
            continue
        if pr != r:
            Mat[[r, pr]] = Mat[[pr, r]]
        sel = (Mat[:, c] == 1)
        sel[r] = False
        Mat[sel] ^= Mat[r]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return Mat[:r], piv


def nullspace(Mat):
    R, piv = rref(Mat)
    cols = Mat.shape[1]
    pset = set(piv)
    free = [c for c in range(cols) if c not in pset]
    basis = []
    for f in free:
        v = np.zeros(cols, np.uint8)
        v[f] = 1
        for r, p in enumerate(piv):
            if R[r, f]:
                v[p] = 1
        basis.append(v)
    return np.array(basis, np.uint8)


class Reducer:
    """reduce a vector modulo the row space of a matrix (returns 0 iff in row space)."""
    def __init__(self, Mat):
        self.R, self.piv = rref(Mat)

    def red(self, v):
        w = v.copy() % 2
        for r, p in enumerate(self.piv):
            if w[p]:
                w ^= self.R[r]
        return w

    def inspan(self, v):
        return not self.red(v).any()


# ---- translation action on data qubits (code automorphism group G, order 72) ----
def tperm(a, b):
    """permutation p with  (g v)[q] = v[p[q]] ; i.e. new[gidx(i+a,j+b)] = old[gidx(i,j)]."""
    p = np.empty(N, int)
    for i in range(ELL):
        for j in range(EM):
            p[gidx(i + a, j + b)] = gidx(i, j)
            p[NG + gidx(i + a, j + b)] = NG + gidx(i, j)
    return p

TRANS = [tperm(a, b) for a in range(ELL) for b in range(EM)]


def sanity():
    assert ((HX @ HZ.T) % 2 == 0).all()
    assert set(HX.sum(1)) == {6} and set(HZ.sum(1)) == {6}
    assert set(HX.sum(0)) == {3} and set(HZ.sum(0)) == {3}
    rx = len(rref(HX)[1]); rz = len(rref(HZ)[1])
    k = N - rx - rz
    ov = set()
    for i in range(HX.shape[0]):
        for j in range(HZ.shape[0]):
            ov.add(int((HX[i] & HZ[j]).sum()))
    return dict(rankHX=rx, rankHZ=rz, k=k, overlaps=sorted(ov))


if __name__ == "__main__":
    print(sanity())
```

### `tanner.py`

```python
"""Explicit monomial-labelled Tanner incidences + the 25920 translation-invariant min-depth
schedules.  Every incidence claim is asserted against the explicit HX/HZ matrices."""
import numpy as np, itertools
from gross import HX, HZ, N, NG, ELL, EM, gidx, A_MONOS, B_MONOS

def gsum(g, m):
    i, j = divmod(g, EM)
    return gidx(i + m[0], j + m[1])

# ---- incidences, derived and then verified against HX / HZ ----------------------------------
# X-check g : left data  g - A_i   (monomial A_i)  ;  right data  NG + (g - B_i)
# Z-check g : left data  g + B_i                   ;  right data  NG + (g + A_i)
def xcheck_nb(g):
    out = []
    for i, m in enumerate(A_MONOS):
        out.append((gsum(g, (-m[0], -m[1])), 'L', i))
    for i, m in enumerate(B_MONOS):
        out.append((NG + gsum(g, (-m[0], -m[1])), 'R', i))
    return out

def zcheck_nb(g):
    out = []
    for i, m in enumerate(B_MONOS):
        out.append((gsum(g, m), 'L', i))
    for i, m in enumerate(A_MONOS):
        out.append((NG + gsum(g, m), 'R', i))
    return out

# data -> checks
def xchecks_of(q):
    """X-checks touching data qubit q, as (check, monomial index)."""
    if q < NG:
        return [(gsum(q, m), i) for i, m in enumerate(A_MONOS)]
    g = q - NG
    return [(gsum(g, m), i) for i, m in enumerate(B_MONOS)]

def zchecks_of(q):
    if q < NG:
        return [(gsum(q, (-m[0], -m[1])), i) for i, m in enumerate(B_MONOS)]
    g = q - NG
    return [(gsum(g, (-m[0], -m[1])), i) for i, m in enumerate(A_MONOS)]

def verify():
    for g in range(NG):
        assert sorted(q for q, _, _ in xcheck_nb(g)) == sorted(int(i) for i in np.nonzero(HX[g])[0]), g
        assert sorted(q for q, _, _ in zcheck_nb(g)) == sorted(int(i) for i in np.nonzero(HZ[g])[0]), g
    for q in range(N):
        assert sorted(c for c, _ in xchecks_of(q)) == sorted(int(i) for i in np.nonzero(HX[:, q])[0]), q
        assert sorted(c for c, _ in zchecks_of(q)) == sorted(int(i) for i in np.nonzero(HZ[:, q])[0]), q
    # cross-check that the (check, monomial) labels agree in both directions
    for g in range(NG):
        for q, side, i in xcheck_nb(g):
            assert (g, i) in xchecks_of(q)
        for q, side, i in zcheck_nb(g):
            assert (g, i) in zchecks_of(q)
    return True

# ---- schedules -------------------------------------------------------------------------------
# A translation-invariant minimum-depth schedule = one CNOT layer in {1..6} per edge orbit.
#   alpha : A-monomials -> P        (X-check  -> left  data)
#   beta  : B-monomials -> Pbar     (X-check  -> right data)
#   gamma : B-monomials -> Pbar     (Z-check  -> left  data)
#   delta : A-monomials -> P        (Z-check  -> right data)
# with P a 3-subset of {1..6} and Pbar its complement.
PSETS = [frozenset(s) for s in itertools.combinations(range(1, 7), 3)]

def all_schedules():
    for P in PSETS:
        Pb = frozenset(range(1, 7)) - P
        Ps, Pbs = sorted(P), sorted(Pb)
        for al in itertools.permutations(Ps):
            for be in itertools.permutations(Pbs):
                for ga in itertools.permutations(Pbs):
                    for de in itertools.permutations(Ps):
                        yield (P, al, be, ga, de)

def schedule_layers(sched):
    """returns dicts layerX[(check,side,i)] and layerZ[...] -> layer"""
    P, al, be, ga, de = sched
    lx = {('L', i): al[i] for i in range(3)}
    lx.update({('R', i): be[i] for i in range(3)})
    lz = {('L', i): ga[i] for i in range(3)}
    lz.update({('R', i): de[i] for i in range(3)})
    return lx, lz

def is_legal(sched):
    """brute verification on the explicit graph: every check and every data qubit uses 6 distinct layers."""
    lx, lz = schedule_layers(sched)
    for g in range(NG):
        assert sorted(lx[(s, i)] for _, s, i in xcheck_nb(g)) == [1, 2, 3, 4, 5, 6]
        assert sorted(lz[(s, i)] for _, s, i in zcheck_nb(g)) == [1, 2, 3, 4, 5, 6]
    for q in range(N):
        side = 'L' if q < NG else 'R'
        ls = [lx[(side, i)] for _, i in xchecks_of(q)] + [lz[(side, i)] for _, i in zchecks_of(q)]
        assert sorted(ls) == [1, 2, 3, 4, 5, 6], (q, ls)
    return True

def is_interleaved(sched):
    """LRC-like / non-interleaved <=> P = {1,2,3} or {4,5,6} (X and Z blocks separated on each half)."""
    P = sched[0]
    return not (P == frozenset({1, 2, 3}) or P == frozenset({4, 5, 6}))

if __name__ == "__main__":
    print("incidences verified:", verify())
    scheds = list(all_schedules())
    print("schedule count:", len(scheds))
    print("interleaved:", sum(1 for s in scheds if is_interleaved(s)),
          " non-interleaved:", sum(1 for s in scheds if not is_interleaved(s)))
    import random
    random.seed(0)
    for s in random.sample(scheds, 40):
        assert is_legal(s)
    print("40 random schedules verified legal on the full 864-edge Tanner graph")
```

### `pool.py`

```python
"""Collect weight-12 logical operators (both types), closed under the 72 translations.

Z-logicals: ker(HX) \\ rowspace(HZ).   X-logicals: ker(HZ) \\ rowspace(HX).
Search = randomised information-set decoding + translation closure + saturation monitoring.
Upper-bound witnesses only need membership, so a pool is one-sided-safe; we additionally run
targeted coset searches (prescribed 1s on a check support) to make the pool complete *where it
matters*, and report saturation statistics.
"""
import numpy as np, itertools, sys, time
from gross import HX, HZ, N, NG, rref, nullspace, Reducer, TRANS

rngmaster = np.random.default_rng(20260820)


def isd_collect(Gbasis, wmax, trials, found, rng, combo=3):
    """random information sets on the linear code spanned by Gbasis; harvest words of wt<=wmax."""
    nc = Gbasis.shape[1]
    for _ in range(trials):
        perm = rng.permutation(nc)
        R, _ = rref(Gbasis[:, perm])
        inv = np.empty(nc, int); inv[perm] = np.arange(nc)
        rows = R[:, inv]
        wts = rows.sum(1)
        for i in np.nonzero(wts <= wmax)[0]:
            found.setdefault(rows[i].tobytes(), rows[i])
        light = np.argsort(wts)[:40]
        for a, b in itertools.combinations(light, 2):
            v = rows[a] ^ rows[b]
            if v.sum() <= wmax:
                found.setdefault(v.tobytes(), v)
        if combo >= 3:
            light3 = np.argsort(wts)[:22]
            for a, b, c in itertools.combinations(light3, 3):
                v = rows[a] ^ rows[b] ^ rows[c]
                if v.sum() <= wmax:
                    found.setdefault(v.tobytes(), v)
    return found


def isd_coset(Gbasis, v0, wmax, trials, found, rng):
    """harvest words of wt<=wmax in the affine space v0 + span(Gbasis)."""
    nc = Gbasis.shape[1]
    for _ in range(trials):
        perm = rng.permutation(nc)
        R, piv = rref(Gbasis[:, perm])
        inv = np.empty(nc, int); inv[perm] = np.arange(nc)
        rows = R[:, inv]
        pivcols = np.array([inv[p] for p in piv])
        # reduce v0 against pivots
        w = v0.copy()
        for r, p in enumerate(pivcols):
            if w[p]:
                w ^= rows[r]
        if w.sum() <= wmax:
            found.setdefault(w.tobytes(), w)
        wts = rows.sum(1)
        light = np.argsort(wts)[:60]
        for a in light:
            v = w ^ rows[a]
            if v.sum() <= wmax:
                found.setdefault(v.tobytes(), v)
        for a, b in itertools.combinations(light[:35], 2):
            v = w ^ rows[a] ^ rows[b]
            if v.sum() <= wmax:
                found.setdefault(v.tobytes(), v)
    return found


def close_translations(words):
    d = {}
    for v in words:
        for p in TRANS:
            u = v[p]
            d[u.tobytes()] = u
    return d


def build(Hdet, Hstab, tag, trials=120, seed=1):
    """Hdet: the parity checks the logical must satisfy.  Hstab: stabilizers to quotient by."""
    rng = np.random.default_rng(seed)
    Ker = nullspace(Hdet)
    red = Reducer(Hstab)
    found = {}
    t0 = time.time()
    isd_collect(Ker, 12, trials, found, rng)
    words = [v for v in found.values() if v.sum() == 12 and not red.inspan(v)]
    pool = close_translations(words)
    print(f"[{tag}] plain ISD: raw {len(found)}  wt12-logical {len(words)}  after G-closure {len(pool)}  ({time.time()-t0:.1f}s)")

    # targeted coset searches: prescribe the 1s on subsets of one check support
    supp = sorted(int(i) for i in np.nonzero(Hstab[0])[0])
    for size in (2, 3):
        for T in itertools.combinations(supp, size):
            # affine space {v in ker(Hdet) : v|_T = 1}
            sub = np.array([v for v in Ker])
            # basis of {v : v|_T = 0} plus a particular solution
            Tm = sub[:, list(T)]
            Rt, pivt = rref(Tm.T.copy())  # not used; do it directly
            # solve: find combination with v|_T = all ones
            # gaussian elimination on the |T| x dim system
            dim = sub.shape[0]
            Msys = np.concatenate([Tm.T, np.ones((size, 1), np.uint8)], 1)  # size x (dim+1)
            Rs, ps = rref(Msys)
            if any(p == dim for p in ps):
                continue  # inconsistent (cannot happen here)
            x = np.zeros(dim, np.uint8)
            for r, p in enumerate(ps):
                x[p] = Rs[r, dim]
            v0 = (x @ sub) % 2
            assert all(v0[t] == 1 for t in T)
            # basis of the zero-on-T subspace
            Z = nullspace(Tm.T.copy())          # coefficient vectors c with (c@sub)|_T = 0
            Gb = (Z @ sub) % 2
            Gb, _ = rref(Gb)
            isd_coset(Gb, v0, 12, 25, found, rng)
    words = [v for v in found.values() if v.sum() == 12 and not red.inspan(v)]
    pool2 = close_translations(words)
    print(f"[{tag}] + targeted cosets: wt12-logical {len(words)}  after G-closure {len(pool2)}  ({time.time()-t0:.1f}s)")
    return np.array(list(pool2.values()), np.uint8)


if __name__ == "__main__":
    tr = int(sys.argv[1]) if len(sys.argv) > 1 else 120
    W = build(HX, HZ, "Z-logicals", trials=tr, seed=7)
    X = build(HZ, HX, "X-logicals", trials=tr, seed=11)
    np.save("poolZ.npy", W); np.save("poolX.npy", X)
    # verification
    assert ((HX @ W.T) % 2 == 0).all() and (W.sum(1) == 12).all()
    rz = Reducer(HZ); assert all(not rz.inspan(v) for v in W)
    assert ((HZ @ X.T) % 2 == 0).all() and (X.sum(1) == 12).all()
    rx = Reducer(HX); assert all(not rx.inspan(v) for v in X)
    print("pool sizes:", W.shape[0], X.shape[0])
```

### `saturate.py`

```python
"""Saturation evidence for the weight-12 logical pools + independent structural cross-checks."""
import numpy as np, itertools, time
from gross import HX, HZ, N, NG, rref, nullspace, Reducer, TRANS
from pool import isd_collect, isd_coset, close_translations

def saturation(Hdet, Hstab, tag, seed):
    rng = np.random.default_rng(seed)
    Ker = nullspace(Hdet); red = Reducer(Hstab)
    found = {}; hist = []
    for stage in range(12):
        isd_collect(Ker, 12, 250, found, rng)
        words = [v for v in found.values() if v.sum() == 12 and not red.inspan(v)]
        hist.append(len(close_translations(words)))
    print(f"[{tag}] G-closed pool size after {[250*(i+1) for i in range(12)]} ISD trials:")
    print("   ", hist)
    pool = close_translations(words)
    P = np.array(list(pool.values()), np.uint8)

    # targeted heavy coset search on every 2- and 3-subset of one check support
    supp = sorted(int(i) for i in np.nonzero(Hstab[0])[0])
    before = len(pool)
    Kerm = Ker
    for size in (2, 3):
        for T in itertools.combinations(supp, size):
            Tm = Kerm[:, list(T)]
            dim = Kerm.shape[0]
            Msys = np.concatenate([Tm.T, np.ones((size, 1), np.uint8)], 1)
            Rs, ps = rref(Msys)
            x = np.zeros(dim, np.uint8)
            for r, p in enumerate(ps):
                x[p] = Rs[r, dim]
            v0 = (x @ Kerm) % 2
            Zc = nullspace(Tm.T.copy()); Gb = (Zc @ Kerm) % 2; Gb, _ = rref(Gb)
            isd_coset(Gb, v0, 12, 250, found, rng)
    words = [v for v in found.values() if v.sum() == 12 and not red.inspan(v)]
    pool = close_translations(words)
    print(f"[{tag}] after heavy targeted coset search on all 15 pairs + 20 triples of one check:"
          f" {before} -> {len(pool)}")

    # orbit structure under the 72 translations
    P = np.array(list(pool.values()), np.uint8)
    keys = set(pool.keys()); seen = set(); orb = []
    for k, v in pool.items():
        if k in seen: continue
        o = set()
        for p in TRANS:
            u = v[p]; o.add(u.tobytes())
        seen |= o; orb.append(len(o))
    from collections import Counter
    print(f"[{tag}] {len(P)} words; translation-orbit size histogram: {dict(Counter(orb))}")
    return P

if __name__ == "__main__":
    t0 = time.time()
    W = saturation(HX, HZ, "Z-log", 101)
    X = saturation(HZ, HX, "X-log", 202)
    np.save("poolZ.npy", W); np.save("poolX.npy", X)
    print("elapsed", time.time() - t0)
```

### `engine.py`

```python
"""Cancellation engine.

FAULT MODEL COVERED (one sector at a time; the two sectors are independent for CSS circuits):
  Z-sector = Z-type faults, X-check detectors, Z-check ancilla residuals, Z logicals.
  Columns of the last-round Z-sector detector error model (each of circuit weight 1):
    (i)   data fault: Z on data qubit q born after CNOT layer j  (j = 0..6)
    (ii)  residual fault: Z on Z-check ancilla c between layers l-1 and l  -> Z on suffix S_l(c)
    (iii) measurement fault: Z on X-check ancilla e (prep / idle / meas / CNOT ZI) -> flips m_e
  A CNOT ZZ fault on an (X-check, data) gate equals column (i) with j = layer-1 (proved in the
  report); a CNOT ZZ fault on a (data, Z-check) gate equals column (ii). So (i)-(iii) exhaust
  the elementary Z-sector fault locations of one round.

  Detector condition: with all faults in the last round R and net data error E,
    D_e^(R) = f_e ,   D_e^(final) = (H_X E)_e + f_e ,
  so "no detector fires" <=> E in ker(H_X) and f = 0, where
    f_e = sum over data qubits q of  1[ q carries Z when e's CNOT to q fires ]  (mod 2)
         + 1[ e has a measurement fault ].

SEARCH SCOPE OF THIS MODULE: fault sets with EXACTLY ONE residual fault (|A| = 1), any number
of data faults, any number of measurement faults, and net data error E equal to a weight-12
logical.  Section |A|>=2 and |E| >= 14 are handled separately in extra.py.
"""
import numpy as np, itertools
from gross import HX, HZ, N, NG, Reducer
from tanner import xcheck_nb, zcheck_nb, xchecks_of, zchecks_of

PERM3 = list(itertools.permutations(range(3)))   # 6 rank-permutations per side


class Sector:
    """resnb: 6 (qubit, side, monoidx) slots of the residual check, slots 0-2 left, 3-5 right.
       detof: q -> [(detector check, monoidx)] (3 entries)."""

    def __init__(self, name, pool, resnb, detof):
        self.name = name
        self.pool = pool
        self.resnb = resnb
        self.resq = [q for q, _, _ in resnb]
        self.detof = {q: detof(q) for q in range(N)}
        # group pool logicals by their intersection pattern with the residual check support
        self.byR = {}
        for L in pool:
            supp = np.nonzero(L)[0]
            R = tuple(k for k in range(6) if L[self.resq[k]])
            if len(R) < 2:
                continue
            self.byR.setdefault(R, []).append(tuple(int(x) for x in supp))
        self.maxR = max(len(R) for R in self.byR)

    # -------- per (piL, piR) precomputation --------------------------------------------
    def _masks(self, Lsupp, piL, piR, extra=()):
        """bit indexing over detector checks touching L (plus the qubits in `extra`);
           returns (nbits, {q: [mask(q,theta) for theta in 0..3]})"""
        qs = list(Lsupp) + list(extra)
        checks = sorted({c for q in qs for c, _ in self.detof[q]})
        bidx = {c: i for i, c in enumerate(checks)}
        masks = {}
        for q in qs:
            pi = piL if q < NG else piR
            rk = {}
            for c, mi in self.detof[q]:
                rk[pi[mi]] = bidx[c]      # rank (0,1,2) -> bit
            m = [0, 0, 0, 0]
            for th in range(4):
                v = 0
                for r in range(th, 3):
                    v ^= 1 << rk[r]
                m[th] = v
            masks[q] = m
        return len(checks), masks

    @staticmethod
    def _mitm(Rq, freeq, masks, nbits, want1):
        """Rq: qubits with fixed theta (the residual-check ones).  freeq: qubits with free theta.
        Returns feas0[tau], feas1[tau] arrays over tau in 4^len(Rq) (row-major, Rq order)."""
        r = len(Rq)
        nfree = len(freeq)
        half = freeq[nfree // 2:]
        first = freeq[:nfree // 2]
        # part2 = `half`
        v2 = np.zeros(1, np.int64)
        for q in half:
            v2 = (v2[:, None] ^ np.array(masks[q], np.int64)[None, :]).ravel()
        present = np.zeros(1 << nbits, bool)
        present[v2] = True
        # part1 free portion
        v1 = np.zeros(1, np.int64)
        for q in first:
            v1 = (v1[:, None] ^ np.array(masks[q], np.int64)[None, :]).ravel()
        # fixed portion: all tau
        vt = np.zeros(1, np.int64)
        for q in Rq:
            vt = (vt[:, None] ^ np.array(masks[q], np.int64)[None, :]).ravel()
        vals = vt[:, None] ^ v1[None, :]                      # (4^r, 4^nfree1)
        feas0 = present[vals].any(1)
        if want1:
            bits = (1 << np.arange(nbits, dtype=np.int64))
            feas1 = feas0 | present[vals[:, :, None] ^ bits[None, None, :]].any((1, 2))
        else:
            feas1 = feas0
        return feas0, feas1

    def build_tables(self, want1=True, verbose=False):
        """T0[(piLi,piRi)][R][tau] : min wt(f)=0 achievable ; T1 : min wt(f)<=1."""
        self.T0 = {}
        self.T1 = {}
        for ai, piL in enumerate(PERM3):
            for bi, piR in enumerate(PERM3):
                t0 = {}
                t1 = {}
                for R, Ls in self.byR.items():
                    r = len(R)
                    acc0 = np.zeros(4 ** r, bool)
                    acc1 = np.zeros(4 ** r, bool)
                    Rq = [self.resq[k] for k in R]
                    for Lsupp in Ls:
                        freeq = [q for q in Lsupp if q not in Rq]
                        nb, masks = self._masks(Lsupp, piL, piR)
                        f0, f1 = self._mitm(Rq, freeq, masks, nb, want1)
                        acc0 |= f0
                        acc1 |= f1
                    t0[R] = acc0
                    t1[R] = acc1
                self.T0[(ai, bi)] = t0
                self.T1[(ai, bi)] = t1
            if verbose:
                print(f"   [{self.name}] piL {ai+1}/6 done")
        # derived: pair tables (2-subsets), OR-ing over the free third coordinate
        self.P0 = {}
        for key, t0 in self.T0.items():
            p = {}
            for R, arr in t0.items():
                r = len(R)
                a = arr.reshape((4,) * r)
                for sub in itertools.combinations(range(r), 2):
                    axes = tuple(i for i in range(r) if i not in sub)
                    red = a.any(axis=axes) if axes else a
                    slots = tuple(R[i] for i in sub)
                    p[slots] = p.get(slots, np.zeros((4, 4), bool)) | red
            self.P0[key] = p
        return self
```

### `sweep.py`

```python
"""Full sweep over the 25920 translation-invariant minimum-depth schedules."""
import numpy as np, itertools, time, pickle, sys
from collections import Counter
from gross import HX, HZ, N, NG
from tanner import (xcheck_nb, zcheck_nb, xchecks_of, zchecks_of, all_schedules,
                    is_interleaved)
from engine import Sector, PERM3

PIDX = {p: i for i, p in enumerate(PERM3)}


def rankperm(layers, ordered):
    """layers: tuple of 3 layers assigned to monomial indices 0,1,2 ; ordered: sorted layer set."""
    return tuple(ordered.index(layers[i]) for i in range(3))


def sector_data(sched, which):
    """returns (piLi, piRi, reslayer[6], theta[6]) for the chosen sector."""
    P, al, be, ga, de = sched
    Ps = sorted(P); Pbs = sorted(set(range(1, 7)) - P)
    if which == 'Z':
        # detectors = X-checks : left data det-layers = Ps (alpha) ; right = Pbs (beta)
        piL = rankperm(al, Ps); piR = rankperm(be, Pbs)
        detL, detR = Ps, Pbs
        res = list(ga) + list(de)          # slots 0-2 left (B-monos), 3-5 right (A-monos)
    else:
        # detectors = Z-checks : left data det-layers = Pbs (gamma) ; right = Ps (delta)
        piL = rankperm(ga, Pbs); piR = rankperm(de, Ps)
        detL, detR = Pbs, Ps
        res = list(al) + list(be)          # slots 0-2 left (A-monos), 3-5 right (B-monos)
    theta = []
    for k in range(6):
        dl = detL if k < 3 else detR
        theta.append(sum(1 for l in dl if l < res[k]))
    return PIDX[piL], PIDX[piR], res, theta


def tau_index(slots, theta):
    t = 0
    for k in slots:
        t = t * 4 + theta[k]
    return t


def bound_for(sec, sched, which):
    ai, bi, res, theta = sector_data(sched, which)
    key = (ai, bi)
    order = sorted(range(6), key=lambda k: res[k])   # slot at CNOT position 1..6
    S5 = tuple(sorted(order[4:]))     # residual fault before layer 5 -> |S| = 2
    S4 = tuple(sorted(order[3:]))     # |S| = 3
    t0 = sec.T0[key]; t1 = sec.T1[key]; p0 = sec.P0[key]
    if S4 in t0 and t0[S4][tau_index(S4, theta)]:
        return 10, ('l=4', S4, tuple(theta[k] for k in S4))
    if S5 in p0:
        a, b = S5
        if p0[S5][theta[a], theta[b]]:
            return 11, ('l=5', S5, tuple(theta[k] for k in S5))
    if S4 in t1 and t1[S4][tau_index(S4, theta)]:
        return 11, ('l=4+meas', S4, tuple(theta[k] for k in S4))
    return 12, None


def main():
    poolZ = np.load('poolZ.npy'); poolX = np.load('poolX.npy')
    t0 = time.time()
    secZ = Sector('Z', poolZ, zcheck_nb(0), xchecks_of).build_tables()
    print(f"Z tables built ({time.time()-t0:.1f}s)")
    secX = Sector('X', poolX, xcheck_nb(0), zchecks_of).build_tables()
    print(f"X tables built ({time.time()-t0:.1f}s)")

    hist = Counter(); histZ = Counter(); histX = Counter()
    hist_int = Counter(); hist_non = Counter()
    best = {}
    rows = []
    for sched in all_schedules():
        bz, wz = bound_for(secZ, sched, 'Z')
        bx, wx = bound_for(secX, sched, 'X')
        b = min(bz, bx)
        hist[b] += 1; histZ[bz] += 1; histX[bx] += 1
        (hist_int if is_interleaved(sched) else hist_non)[b] += 1
        if b >= 11:
            rows.append((sched, bz, bx, wz, wx))
    print("elapsed", time.time() - t0)
    print("overall histogram  :", dict(sorted(hist.items())))
    print("Z-sector histogram :", dict(sorted(histZ.items())))
    print("X-sector histogram :", dict(sorted(histX.items())))
    print("interleaved (23328):", dict(sorted(hist_int.items())))
    print("non-interleaved(2592):", dict(sorted(hist_non.items())))
    print("schedules with bound >= 11:", len(rows))
    with open('sweep.pkl', 'wb') as f:
        pickle.dump(dict(hist=hist, histZ=histZ, histX=histX, hist_int=hist_int,
                         hist_non=hist_non, rows=rows), f)


if __name__ == "__main__":
    main()
```

### `relax.py`

```python
"""Timing-free relaxation:  how much can several residual faults buy, ignoring detectors?

For a weight-12 logical L, a set of pairwise-disjoint residuals r_i (each r_i a residual of some
check, r_i subset of L) realises the net error L with  |A| + |Q| = #r_i + (12 - sum|r_i|)
= 12 - gain,  gain := sum (|r_i| - 1).  Any circuit fault set of this shape has weight >= 12-gain.
So max_L gain tells us how deep the multi-residual family can possibly reach.

A schedule enters only through its "residual structure": the ordered slot partition
 (i1 i2 | i3 | i4 | i5 i6) of the 6 slots of the residual check.  There are 15*4*3 = 180 of them.
"""
import numpy as np, itertools, pickle, sys
from collections import Counter
from gross import HX, HZ, N, NG
from tanner import zcheck_nb, xcheck_nb


def check_patterns(pool, nbfn):
    """for each L: list of (check, frozenset slots, dict slot->qubit) with |L cap c| >= 2"""
    out = []
    for L in pool:
        ent = []
        for g in range(NG):
            nb = nbfn(g)
            slots = [k for k in range(6) if L[nb[k][0]]]
            if len(slots) >= 2:
                ent.append((g, frozenset(slots), {k: nb[k][0] for k in slots}))
        out.append(ent)
    return out


def structures():
    """(Pair1, Pair2, Triple1, Triple2) as frozensets of slots, keyed by (o0o1, o2, o4o5)."""
    S = {}
    for p1 in itertools.combinations(range(6), 2):
        rest = [k for k in range(6) if k not in p1]
        for o2 in rest:
            rest2 = [k for k in rest if k != o2]
            for p2 in itertools.combinations(rest2, 2):
                o3 = [k for k in rest2 if k not in p2][0]
                key = (p1, o2, p2)
                S[key] = (frozenset(p1), frozenset(p2),
                          frozenset(p1) | {o2}, frozenset(p2) | {o3})
    return S


def maxgain(items):
    """items: list of (qubit frozenset, gain). max total gain over pairwise-disjoint choices."""
    items = sorted(items, key=lambda t: -t[1])
    best = 0
    n = len(items)

    def rec(i, used, g):
        nonlocal best
        if g > best:
            best = g
        if i >= n:
            return
        # optimistic bound
        if g + sum(it[1] for it in items[i:]) <= best:
            return
        for j in range(i, n):
            q, gg = items[j]
            if not (q & used):
                rec(j + 1, used | q, g + gg)
    rec(0, frozenset(), 0)
    return best


def run(tag, pool, nbfn):
    pats = check_patterns(pool, nbfn)
    S = structures()
    res = {}
    for key, (P1, P2, T1, T2) in S.items():
        best = 0
        arg = None
        for Li, ent in enumerate(pats):
            items = []
            for g, slots, qmap in ent:
                if slots == T1 or slots == T2:
                    items.append((frozenset(qmap[k] for k in slots), 2))
                if P1 <= slots:
                    items.append((frozenset(qmap[k] for k in P1), 1))
                if P2 <= slots:
                    items.append((frozenset(qmap[k] for k in P2), 1))
            g = maxgain(items)
            if g > best:
                best, arg = g, Li
        res[key] = (best, arg)
    h = Counter(v[0] for v in res.values())
    print(f"[{tag}] max gain over all weight-12 logicals, per residual structure (180): {dict(sorted(h.items()))}")
    print(f"[{tag}] => timing-free relaxation weight 12-gain: "
          f"{dict(sorted(Counter(12 - v[0] for v in res.values()).items()))}")
    return res


if __name__ == "__main__":
    rz = run('Z', np.load('poolZ.npy'), zcheck_nb)
    rx = run('X', np.load('poolX.npy'), xcheck_nb)
    with open('relax.pkl', 'wb') as f:
        pickle.dump({'Z': rz, 'X': rx}, f)
```

### `sim.py`

```python
"""INDEPENDENT circuit simulator: builds the last-round Z-sector detector error model by
literally propagating Pauli-Z frames through the CNOT schedule.  No use of the analytic
suffix/rank formula -- this is the cross-check for engine.py.

Qubit indexing: data 0..143 ; X-ancillas 144..215 (X-check g -> 144+g) ; Z-ancillas 216..287.
Z-frame propagation through CNOT(control c, target t):  z[c] ^= z[t]   (z[t] unchanged).
Measurement of an X-ancilla (X basis) is flipped by its z at measurement time.
Measurement of a Z-ancilla (Z basis) is insensitive to z.
"""
import numpy as np, itertools
from gross import HX, HZ, N, NG
from tanner import xcheck_nb, zcheck_nb, schedule_layers

NQ = N + 2 * NG
XA = lambda g: N + g
ZA = lambda g: N + NG + g


def gate_list(sched):
    """[(layer, control, target)] for the 864 CNOTs."""
    lx, lz = schedule_layers(sched)
    G = []
    for g in range(NG):
        for q, side, i in xcheck_nb(g):
            G.append((lx[(side, i)], XA(g), q))       # X-check ancilla controls data
        for q, side, i in zcheck_nb(g):
            G.append((lz[(side, i)], q, ZA(g)))       # data controls Z-check ancilla
    G.sort(key=lambda t: t[0])
    return G


def check_legal(G):
    from collections import defaultdict
    per = defaultdict(list)
    for t, c, tg in G:
        per[t] += [c, tg]
    assert set(per) == {1, 2, 3, 4, 5, 6}
    for t, qs in per.items():
        assert len(qs) == len(set(qs)) == 288, (t, len(qs), len(set(qs)))
    return True


def propagate(G, injections):
    """injections: list of (layer_after, qubit) meaning a Z fault appears on `qubit`
    immediately after CNOT layer `layer_after` (0 = before layer 1).
    Returns (E on data, m_flip on X-ancillas)."""
    z = np.zeros(NQ, np.uint8)
    mflip = np.zeros(NG, np.uint8)
    inj = {}
    for la, q in injections:
        inj.setdefault(la, []).append(q)
    for q in inj.get(0, []):
        z[q] ^= 1
    for layer in range(1, 7):
        for (t, c, tg) in G:
            if t != layer:
                continue
            z[c] ^= z[tg]
        for q in inj.get(layer, []):
            z[q] ^= 1
    # X-ancilla measurement outcomes flip by their accumulated z
    for g in range(NG):
        mflip[g] = z[XA(g)]
    return z[:N].copy(), mflip


def propagate_x(G, injections):
    """X-frame version.  CNOT(c,t): x[t] ^= x[c].  X on data reaches Z-check ancillas and flips
    their Z-basis outcome; X on an X-check ancilla spreads to its not-yet-touched data qubits."""
    x = np.zeros(NQ, np.uint8)
    mflip = np.zeros(NG, np.uint8)
    inj = {}
    for la, q in injections:
        inj.setdefault(la, []).append(q)
    for q in inj.get(0, []):
        x[q] ^= 1
    for layer in range(1, 7):
        for (t, c, tg) in G:
            if t != layer:
                continue
            x[tg] ^= x[c]
        for q in inj.get(layer, []):
            x[q] ^= 1
    for g in range(NG):
        mflip[g] = x[ZA(g)]
    return x[:N].copy(), mflip


def prop(G, injections, which):
    return propagate(G, injections) if which == 'Z' else propagate_x(G, injections)


def dem_columns(sched):
    """all elementary weight-1 Z-sector fault mechanisms of the last round."""
    G = gate_list(sched)
    cols = []
    for q in range(N):                      # data faults, born after layer j
        for j in range(7):
            E, f = propagate(G, [(j, q)])
            cols.append((('data', q, j), E, f))
    for g in range(NG):                     # Z-check ancilla faults, before layer l
        for l in range(1, 8):
            E, f = propagate(G, [(l - 1, ZA(g))])
            cols.append((('zanc', g, l), E, f))
    for g in range(NG):                     # X-check ancilla / measurement faults
        E, f = propagate(G, [(0, XA(g))])
        cols.append((('meas', g), E, f))
    return cols


def evaluate(sched, injections):
    """returns (E, f, detectors_all_zero, is_nontrivial_logical)"""
    from gross import Reducer
    G = gate_list(sched)
    E, f = propagate(G, injections)
    s = (HX @ E) % 2
    ok = (not f.any()) and (not s.any())
    rz = Reducer(HZ)
    logi = ok and not rz.inspan(E)
    return E, f, ok, logi
```

### `probe2.py`

```python
"""Anomaly check: do PREFIX residual columns really give gain up to 6 (=> weight-6 fault sets)?
Every candidate is built as an explicit circuit fault set and verified with sim.py, which
propagates Pauli-Z frames through the literal 864-CNOT schedule.
"""
import numpy as np, itertools, sys
from collections import Counter
from gross import HX, HZ, N, NG, Reducer
from tanner import zcheck_nb, xcheck_nb, all_schedules
import sim

RZ = Reducer(HZ); RX = Reducer(HX)


def sector(sched, which):
    P, al, be, ga, de = sched
    res = (list(ga) + list(de)) if which == 'Z' else (list(al) + list(be))
    order = sorted(range(6), key=lambda k: res[k])   # order[j] = slot of i_{j+1}
    nbfn = zcheck_nb if which == 'Z' else xcheck_nb
    anc = sim.ZA if which == 'Z' else sim.XA
    return res, order, nbfn, anc


def items_for(sched, which, L):
    """residual columns usable inside L.  (check, l, r-vector-as-qubitset, gain)
       l is the ancilla-fault position; r is the CHOSEN representative (prefix or suffix)."""
    res, order, nbfn, anc = sector(sched, which)
    pre2 = order[:2]; pre3 = order[:3]; suf2 = order[4:]; suf3 = order[3:]
    out = []
    for g in range(NG):
        nb = nbfn(g)
        for slots, l, gain in ((pre2, 3, 1), (suf2, 5, 1), (pre3, 4, 2), (suf3, 4, 2)):
            qs = [nb[k][0] for k in slots]
            if all(L[q] for q in qs):
                out.append((g, l, frozenset(qs), gain))
    return out


def packings(items, want_gain=None, limit=400):
    items = sorted(items, key=lambda t: -t[3])
    n = len(items); best = [0, []]
    def rec(i, used, g, ch, ancused):
        if g > best[0]:
            best[0] = g; best[1] = [list(ch)]
        elif g == best[0] and g > 0 and len(best[1]) < limit:
            best[1].append(list(ch))
        if i >= n: return
        if g + sum(it[3] for it in items[i:]) < best[0]: return
        for j in range(i, n):
            gg, l, r, ga = items[j]
            if r & used: continue
            if (gg, l) in ancused: continue      # a fault location can be used only once
            ch.append(items[j]); rec(j + 1, used | r, g + ga, ch, ancused | {(gg, l)}); ch.pop()
    rec(0, frozenset(), 0, [], frozenset())
    return best


def build_faultset(sched, which, L, packing):
    """returns (A, Q, E) with E the net data error; weight before measurement faults = |A|+|Q|."""
    res, order, nbfn, anc = sector(sched, which)
    G = sim.gate_list(sched)
    A = sorted({(g, l) for (g, l, r, ga) in packing})
    inj = [(l - 1, anc(g)) for (g, l) in A]
    EA, fA = sim.propagate(G, inj)
    cov = frozenset().union(*[r for (_, _, r, _) in packing]) if packing else frozenset()
    Q = np.zeros(N, np.uint8)
    for q in np.nonzero(L)[0]:
        if q not in cov:
            Q[q] = 1
    E = (EA ^ Q) % 2
    return A, [int(q) for q in np.nonzero(Q)[0]], E


def min_wtf(sched, which, A, Q, cap=2):
    """exact min wt(f) over the free birth times of the Q data faults (MITM)."""
    G = sim.gate_list(sched)
    anc = sim.ZA if which == 'Z' else sim.XA
    _, f0 = sim.propagate(G, [(l - 1, anc(g)) for (g, l) in A])
    def pk(f): return int.from_bytes(np.packbits(f).tobytes(), 'big')
    opts = []
    for q in Q:
        seen = {}
        for j in range(7):
            E, f = sim.propagate(G, [(j, q)])
            seen[pk(f)] = 1
        opts.append(list(seen))
    h = len(opts) // 2
    def acc(ol):
        cur = {0}
        for o in ol:
            cur = {c ^ v for c in cur for v in o}
        return cur
    Aset = acc(opts[:h]); Bset = acc(opts[h:]); tgt = pk(f0)
    for a in Aset:
        if (a ^ tgt) in Bset: return 0
    if cap >= 1:
        bits = [1 << i for i in range(NG)]
        for a in Aset:
            v = a ^ tgt
            for b in bits:
                if (v ^ b) in Bset: return 1
    return 99


def analyse(sched, which, pool, tag):
    best = (99, None)
    gains = []
    for Li, L in enumerate(pool):
        it = items_for(sched, which, L)
        g, pks = packings(it)
        gains.append(g)
    print(f"  [{tag}] max prefix+suffix gain over 1884 logicals: {dict(sorted(Counter(gains).items()))}")
    order = np.argsort(gains)[::-1]
    results = Counter()
    for Li in order[:120]:
        L = pool[Li]
        g, pks = packings(items_for(sched, which, L))
        for pk_ in pks[:40]:
            A, Q, E = build_faultset(sched, which, L, pk_)
            # verify E is a nontrivial logical of the right type
            Hd, Rst = (HX, RZ) if which == 'Z' else (HZ, RX)
            if ((Hd @ E) % 2).any() or Rst.inspan(E):
                results['E not a nontrivial logical'] += 1
                continue
            base = len(A) + len(Q)
            w = min_wtf(sched, which, A, Q)
            tot = base + w if w < 99 else base + 2
            results[(base, 'exact' if w < 99 else '>=')] += 1
            if tot < best[0]:
                best = (tot, (Li, A, Q, w, base))
    print(f"  [{tag}] (base weight, wt(f) status) histogram over top packings: {dict(results)}")
    print(f"  [{tag}] best total found: {best[0]}")
    return best


if __name__ == "__main__":
    poolZ = np.load('poolZ.npy'); poolX = np.load('poolX.npy')
    scheds = list(all_schedules())
    tests = [("non-interleaved P={1,2,3}", next(s for s in scheds if s[0] == frozenset({1, 2, 3}))),
             ("interleaved P={1,3,5}", next(s for s in scheds if s[0] == frozenset({1, 3, 5}))),
             ("interleaved P={2,4,6}", next(s for s in scheds if s[0] == frozenset({2, 4, 6})))]
    for name, s in tests:
        print(f"\n=== {name}  {s}")
        analyse(s, 'Z', poolZ, 'Z')
```

### `full.py`

```python
"""Full-family sweep: multi-residual skeletons + free data-fault timings + measurement faults.

Witness family  W  (this is the SCOPE statement for the report):
  * one CSS sector at a time (Z-sector: Z faults / X-check detectors / Z-check ancilla residuals);
  * an arbitrary set A of residual-check ancilla faults, each at any position l in {1..6};
  * data faults with free birth times (7 positions, 4 distinct detector signatures);
  * measurement faults on detector ancillas, at most `CAP` of them;
  * net data error E in the coset  L + <checks used with a prefix representative>, L running over
    the complete saturated pool of weight-12 logicals;
  * all faults in the final syndrome-extraction round.
Weight = |A| + |Q| + wt(f).  Everything reported is a WITNESS => upper bound on d_circ.

Translation compression: code + schedule are invariant under G = Z_12 x Z_6 (order 72), so L may
be restricted to one representative of each of the 30 G-orbits of weight-12 logicals.
"""
import numpy as np, itertools, pickle, sys, time
from collections import Counter, defaultdict
from gross import HX, HZ, N, NG, TRANS
from tanner import zcheck_nb, xcheck_nb, xchecks_of, zchecks_of, all_schedules, is_interleaved

CAP = 2                # max number of measurement faults searched
MAXPACK_PER_GAIN = 25  # packings kept per gain level per (rep, structure)


def orbit_reps(pool):
    seen, reps = set(), []
    for v in pool:
        if v.tobytes() in seen:
            continue
        seen |= {v[p].tobytes() for p in TRANS}
        reps.append(v)
    return reps


def structures():
    S = {}
    for p1 in itertools.combinations(range(6), 2):
        rest = [k for k in range(6) if k not in p1]
        for o2 in rest:
            r2 = [k for k in rest if k != o2]
            for p2 in itertools.combinations(r2, 2):
                o3 = [k for k in r2 if k not in p2][0]
                S[(p1, o2, p2)] = dict(pre2=frozenset(p1), suf2=frozenset(p2),
                                       pre3=frozenset(p1) | {o2}, suf3=frozenset(p2) | {o3})
    return S


def minwt(f0, opts, nbits, cap):
    """min wt(f0 XOR sum of one option per group), returned only if <= cap, else None."""
    h = max(1, len(opts) // 2)
    def acc(ol):
        cur = np.zeros(1, np.int64)
        for o in ol:
            cur = np.unique((cur[:, None] ^ np.array(o, np.int64)[None, :]).ravel())
        return cur
    Aa = acc(opts[:h]); Bb = np.sort(acc(opts[h:]))
    va = np.unique(Aa ^ np.int64(f0))
    def hit(v):
        i = np.searchsorted(Bb, v)
        np.clip(i, 0, len(Bb) - 1, out=i)
        return bool((Bb[i] == v).any())
    if hit(va):
        return 0
    if cap >= 1:
        for i in range(nbits):
            if hit(va ^ np.int64(1 << i)):
                return 1
    if cap >= 2:
        for i in range(nbits):
            vi = va ^ np.int64(1 << i)
            for j in range(i + 1, nbits):
                if hit(vi ^ np.int64(1 << j)):
                    return 2
    return None


class SectorFull:
    def __init__(self, name, pool, nbfn, detof):
        self.name = name
        self.reps = orbit_reps(pool)
        self.nb = [nbfn(g) for g in range(NG)]
        self.detof = [detof(q) for q in range(N)]
        self.structs = structures()
        self.repslots = []
        for L in self.reps:
            d = {}
            for g in range(NG):
                sl = frozenset(k for k in range(6) if L[self.nb[g][k][0]])
                if len(sl) >= 2:
                    d[g] = sl
            self.repslots.append(d)
        self.Lq = [[int(q) for q in np.nonzero(L)[0]] for L in self.reps]
        self.pcache = {}
        self.mcache = {}

    def packings(self, ri, skey):
        key = (ri, skey)
        if key in self.pcache:
            return self.pcache[key]
        st = self.structs[skey]
        items = []
        for g, sl in self.repslots[ri].items():
            for tag, l, gain in (('pre2', 3, 1), ('suf2', 5, 1), ('pre3', 4, 2), ('suf3', 4, 2)):
                if st[tag] <= sl:
                    items.append((g, l, frozenset(self.nb[g][k][0] for k in st[tag]), gain))
        items.sort(key=lambda t: -t[3])
        bygain = defaultdict(list)
        n = len(items)
        cnt = [0]
        def rec(i, used, g, ch, anc):
            if ch and len(bygain[g]) < MAXPACK_PER_GAIN:
                bygain[g].append(list(ch))
            cnt[0] += 1
            if i >= n or cnt[0] > 20000:
                return
            for j in range(i, n):
                gg, l, r, ga = items[j]
                if (r & used) or (gg, l) in anc:
                    continue
                ch.append(items[j])
                rec(j + 1, used | r, g + ga, ch, anc | {(gg, l)})
                ch.pop()
        rec(0, frozenset(), 0, [], frozenset())
        out = []
        for g in sorted(bygain, reverse=True):
            for p in bygain[g]:
                out.append((g, p))
        self.pcache[key] = out
        return out

    def masks_for(self, piL, piR):
        key = (piL, piR)
        if key in self.mcache:
            return self.mcache[key]
        M = {}
        for q in range(N):
            pi = piL if q < NG else piR
            rowsc = [None] * 3
            for c, mi in self.detof[q]:
                rowsc[pi[mi]] = c
            M[q] = rowsc          # rank -> detector check
        self.mcache[key] = M
        return M

    def eval_schedule(self, order, theta, piL, piR, best=12):
        skey = (tuple(sorted(order[:2])), order[2], tuple(sorted(order[4:])))
        Sl = {l: [order[j] for j in range(l - 1, 6)] for l in range(1, 7)}
        Mk = self.masks_for(piL, piR)
        wit = None
        for ri in range(len(self.reps)):
            for gain, pack in self.packings(ri, skey):
                base = 12 - gain
                if base >= best:
                    break
                A = sorted({(g, l) for (g, l, r, ga) in pack})
                fixed = [(self.nb[g][k][0], theta[k]) for (g, l) in A for k in Sl[l]]
                covered = frozenset().union(*[r for (_, _, r, _) in pack])
                freeq = [q for q in self.Lq[ri] if q not in covered]
                assert len(A) + len(freeq) == base
                bits = {}
                def bit(c):
                    if c not in bits:
                        bits[c] = len(bits)
                    return bits[c]
                def mask(q, th):
                    v = 0
                    for r in range(th, 3):
                        v ^= 1 << bit(Mk[q][r])
                    return v
                f0 = 0
                for q, th in fixed:
                    f0 ^= mask(q, th)
                opts = [[mask(q, th) for th in range(4)] for q in freeq]
                w = minwt(f0, opts, len(bits), min(CAP, best - base - 1))
                if w is not None and base + w < best:
                    best = base + w
                    wit = dict(rep=ri, A=A, free=freeq, wtf=w, base=base)
                    if best <= 7:
                        return best, wit
        return best, wit


def sched_sector(sched, which):
    P, al, be, ga, de = sched
    Ps = sorted(P); Pbs = sorted(set(range(1, 7)) - P)
    if which == 'Z':
        piL = tuple(Ps.index(al[i]) for i in range(3)); piR = tuple(Pbs.index(be[i]) for i in range(3))
        detL, detR, res = Ps, Pbs, list(ga) + list(de)
    else:
        piL = tuple(Pbs.index(ga[i]) for i in range(3)); piR = tuple(Ps.index(de[i]) for i in range(3))
        detL, detR, res = Pbs, Ps, list(al) + list(be)
    order = sorted(range(6), key=lambda k: res[k])
    theta = [sum(1 for l in (detL if k < 3 else detR) if l < res[k]) for k in range(6)]
    return order, theta, piL, piR


def main(limit=None, out='full.pkl'):
    poolZ = np.load('poolZ.npy'); poolX = np.load('poolX.npy')
    secZ = SectorFull('Z', poolZ, zcheck_nb, xchecks_of)
    secX = SectorFull('X', poolX, xcheck_nb, zchecks_of)
    print("orbit representatives:", len(secZ.reps), len(secX.reps))
    scheds = list(all_schedules())
    if limit:
        rng = np.random.default_rng(5); scheds = [scheds[i] for i in rng.choice(len(scheds), limit, replace=False)]
    hist = Counter(); hist_i = Counter(); hist_n = Counter()
    recs = []
    t0 = time.time()
    for n, s in enumerate(scheds):
        oz, tz, pLz, pRz = sched_sector(s, 'Z')
        bz, wz = secZ.eval_schedule(oz, tz, pLz, pRz)
        ox, tx, pLx, pRx = sched_sector(s, 'X')
        bx, wx = secX.eval_schedule(ox, tx, pLx, pRx, best=bz)
        b = min(bz, bx)
        hist[b] += 1
        (hist_i if is_interleaved(s) else hist_n)[b] += 1
        recs.append((s, bz, bx))
        if n % 500 == 499:
            print(f"  {n+1}/{len(scheds)}  {time.time()-t0:.0f}s  hist={dict(sorted(hist.items()))}", flush=True)
    print("TOTAL", time.time() - t0, "s")
    print("overall :", dict(sorted(hist.items())))
    print("interleaved :", dict(sorted(hist_i.items())))
    print("non-interleaved :", dict(sorted(hist_n.items())))
    with open(out, 'wb') as f:
        pickle.dump(dict(hist=hist, hist_i=hist_i, hist_n=hist_n, recs=recs), f)


if __name__ == "__main__":
    main(limit=int(sys.argv[1]) if len(sys.argv) > 1 else None,
         out=sys.argv[2] if len(sys.argv) > 2 else 'full.pkl')
```

### `verify.py`

```python
"""End-to-end verification of a witness with the INDEPENDENT simulator sim.py.

Rebuilds the explicit list of elementary circuit faults, propagates Pauli-Z frames through the
literal 864-CNOT schedule, and checks: (1) every detector of the last round and of the ideal final
readout is silent; (2) the residual data error is a nontrivial logical; (3) the fault count.
"""
import numpy as np, itertools, sys
from gross import HX, HZ, N, NG, Reducer
from tanner import zcheck_nb, xcheck_nb, xchecks_of, zchecks_of, all_schedules
import sim
from full import SectorFull, sched_sector, orbit_reps

RZ = Reducer(HZ); RX = Reducer(HX)


def reconstruct(sec, which, sched, order, theta, piL, piR, ri, A, freeq, target_w):
    """find birth layers for the free data faults realising wt(f) = target_w."""
    G = sim.gate_list(sched)
    anc = sim.ZA if which == 'Z' else sim.XA
    _, f0 = sim.prop(G, [(l - 1, anc(g)) for (g, l) in A], which)
    # per free qubit: birth layer -> f-vector (use the simulator, not the analytic mask)
    cand = []
    for q in freeq:
        d = {}
        for j in range(7):
            E, f = sim.prop(G, [(j, q)], which)
            assert E.sum() == 1 and E[q] == 1
            d.setdefault(f.tobytes(), j)
        cand.append([(j, np.frombuffer(k, np.uint8).copy()) for k, j in d.items()])
    h = max(1, len(cand) // 2)
    def acc(cl):
        cur = {(): np.zeros(NG, np.uint8)}
        for idx, o in enumerate(cl):
            nxt = {}
            for k, v in cur.items():
                for (j, f) in o:
                    nxt[k + (j,)] = v ^ f
            cur = nxt
        return cur
    Aa = acc(cand[:h]); Bb = acc(cand[h:])
    Bmap = {}
    for k, v in Bb.items():
        Bmap.setdefault(v.tobytes(), k)
    for ka, va in Aa.items():
        need = (va ^ f0)
        for extra in extras(target_w):
            key = (need ^ extra).tobytes()
            if key in Bmap:
                return list(ka) + list(Bmap[key]), np.nonzero(extra)[0].tolist()
    return None, None


def extras(w):
    z = np.zeros(NG, np.uint8)
    if w == 0:
        yield z; return
    for combo in itertools.combinations(range(NG), w):
        e = z.copy()
        for c in combo:
            e[c] = 1
        yield e


def verify(sched, which, sec, ri, A, freeq, wtf):
    order, theta, piL, piR = sched_sector(sched, which)
    births, meas = reconstruct(sec, which, sched, order, theta, piL, piR, ri, A, freeq, wtf)
    if births is None:
        return None
    anc = sim.ZA if which == 'Z' else sim.XA
    danc = sim.XA if which == 'Z' else sim.ZA
    inj = [(l - 1, anc(g)) for (g, l) in A]
    inj += [(j, q) for j, q in zip(births, freeq)]
    inj += [(0, danc(e)) for e in meas]
    G = sim.gate_list(sched)
    E, f = sim.prop(G, inj, which)
    Hd, Rst = (HX, RZ) if which == 'Z' else (HZ, RX)
    if which == 'X':
        # for the X sector the "mflip" returned by propagate is the X-ancilla one; recompute
        pass
    s = (Hd @ E) % 2
    return dict(nfaults=len(inj), silent_round=not f.any(), silent_final=not (s ^ f).any(),
                E_in_kernel=not s.any(), nontrivial=not Rst.inspan(E), Ewt=int(E.sum()),
                injections=inj)


if __name__ == "__main__":
    import pickle
    poolZ = np.load('poolZ.npy'); poolX = np.load('poolX.npy')
    secZ = SectorFull('Z', poolZ, zcheck_nb, xchecks_of)
    d = pickle.load(open(sys.argv[1], 'rb'))
    scheds = [r[0] for r in d['recs']]
    bz = [r[1] for r in d['recs']]
    # take the lowest Z-sector bound in the sample
    i = int(np.argmin(bz))
    s = scheds[i]
    print("schedule:", s, " Z-sector bound:", bz[i])
    order, theta, piL, piR = sched_sector(s, 'Z')
    b, wit = secZ.eval_schedule(order, theta, piL, piR)
    print("witness skeleton:", b, {k: v for k, v in wit.items() if k != 'free'}, "free:", wit['free'])
    r = verify(s, 'Z', secZ, wit['rep'], wit['A'], wit['free'], wit['wtf'])
    print("VERIFICATION:", {k: v for k, v in r.items() if k != 'injections'} if r else "reconstruction failed")
```

### `verify_orbit.py`

```python
"""Independent check of the translation quotient.

Claim used by the sweep: because the code AND every translation-invariant schedule are invariant
under G = Z_12 x Z_6 (order 72), letting the net logical L range over 30 orbit representatives
gives the same minimum as letting it range over all 1884 weight-12 logicals.

Check 1 (structural): for every g in G and every schedule in the class, g maps the schedule's
CNOT-layer function to itself.
Check 2 (empirical): evaluate a sample of schedules with reps = all 1884 logicals and compare.
"""
import numpy as np, itertools, sys, time
from gross import HX, HZ, N, NG, TRANS, gidx, ELL, EM
from tanner import (zcheck_nb, xcheck_nb, xchecks_of, zchecks_of, all_schedules,
                    schedule_layers)
from full import SectorFull, sched_sector
import numpy.random as npr


def check_translation_invariance(nsched=25):
    """the layer of a CNOT depends only on its (side, monomial-index) orbit, so translating a
    check translates its whole CNOT-time profile.  Verified directly on the explicit graph."""
    rng = npr.default_rng(0)
    scheds = list(all_schedules())
    for s in [scheds[i] for i in rng.choice(len(scheds), nsched, replace=False)]:
        lx, lz = schedule_layers(s)
        for a in range(ELL):
            for b in range(EM):
                for g in (0, 5, 37):
                    gg = gidx(a + g // EM, b + g % EM)
                    prof1 = sorted((side, i, lx[(side, i)]) for _, side, i in xcheck_nb(g))
                    prof2 = sorted((side, i, lx[(side, i)]) for _, side, i in xcheck_nb(gg))
                    assert prof1 == prof2
                    p1 = sorted((side, i, lz[(side, i)]) for _, side, i in zcheck_nb(g))
                    p2 = sorted((side, i, lz[(side, i)]) for _, side, i in zcheck_nb(gg))
                    assert p1 == p2
    return True


def full_pool_sector(pool, nbfn, detof):
    s = SectorFull('full', pool, nbfn, detof)
    s.reps = [v for v in pool]
    s.repslots = []
    for L in s.reps:
        d = {}
        for g in range(NG):
            sl = frozenset(k for k in range(6) if L[s.nb[g][k][0]])
            if len(sl) >= 2:
                d[g] = sl
        s.repslots.append(d)
    s.Lq = [[int(q) for q in np.nonzero(L)[0]] for L in s.reps]
    s.pcache = {}
    return s


if __name__ == "__main__":
    print("check 1 (schedule is G-invariant on the explicit Tanner graph):",
          check_translation_invariance())
    poolZ = np.load('poolZ.npy')
    quot = SectorFull('Z', poolZ, zcheck_nb, xchecks_of)
    full = full_pool_sector(poolZ, zcheck_nb, xchecks_of)
    print("reps: quotient", len(quot.reps), " full", len(full.reps))
    rng = npr.default_rng(3)
    scheds = list(all_schedules())
    idx = rng.choice(len(scheds), int(sys.argv[1]) if len(sys.argv) > 1 else 12, replace=False)
    t0 = time.time(); bad = 0
    for i in idx:
        s = scheds[i]
        o, th, pL, pR = sched_sector(s, 'Z')
        b1, _ = quot.eval_schedule(o, th, pL, pR)
        b2, _ = full.eval_schedule(o, th, pL, pR)
        flag = "OK" if b1 == b2 else "MISMATCH"
        if b1 != b2: bad += 1
        print(f"  {s[0]} a{s[1]} b{s[2]} g{s[3]} d{s[4]}: quotient {b1}  full-pool {b2}  {flag}")
    print(f"mismatches: {bad}   ({time.time()-t0:.0f}s)")
```

### `batch_verify.py`

```python
"""Verify, with the independent simulator, one witness for each certified weight class,
in both sectors, plus the trivial weight-12 witness."""
import numpy as np, pickle, sys, itertools
from collections import Counter, defaultdict
from gross import HX, HZ, N, NG, Reducer
from tanner import zcheck_nb, xcheck_nb, xchecks_of, zchecks_of, all_schedules
import sim
from full import SectorFull, sched_sector
from verify import verify

RZ = Reducer(HZ); RX = Reducer(HX)


def trivial12(sched, which, pool):
    """12 data faults born after the last CNOT layer: f = 0, E = L."""
    G = sim.gate_list(sched)
    L = pool[0]
    inj = [(6, int(q)) for q in np.nonzero(L)[0]]
    E, f = sim.prop(G, inj, which)
    Hd, Rst = (HX, RZ) if which == 'Z' else (HZ, RX)
    s = (Hd @ E) % 2
    return dict(nfaults=len(inj), silent_round=not f.any(), silent_final=not (s ^ f).any(),
                nontrivial=not Rst.inspan(E), Ewt=int(E.sum()))


if __name__ == "__main__":
    poolZ = np.load('poolZ.npy'); poolX = np.load('poolX.npy')
    secZ = SectorFull('Z', poolZ, zcheck_nb, xchecks_of)
    secX = SectorFull('X', poolX, xcheck_nb, zchecks_of)
    d = pickle.load(open(sys.argv[1], 'rb'))
    byclass = defaultdict(list)
    for (s, bz, bx) in d['recs']:
        byclass[min(bz, bx)].append((s, bz, bx))
    print("classes present:", {k: len(v) for k, v in sorted(byclass.items())})
    for w in sorted(byclass):
        s, bz, bx = byclass[w][0]
        which = 'Z' if bz <= bx else 'X'
        sec = secZ if which == 'Z' else secX
        o, th, pL, pR = sched_sector(s, which)
        b, wit = sec.eval_schedule(o, th, pL, pR)
        if wit is None:
            print(f"  class {w}: no sub-12 witness; trivial weight-12 witness ->",
                  trivial12(s, which, poolZ if which == 'Z' else poolX)); continue
        r = verify(s, which, sec, wit['rep'], wit['A'], wit['free'], wit['wtf'])
        ok = r and r['silent_round'] and r['silent_final'] and r['nontrivial'] and r['nfaults'] == w
        print(f"  class {w}: sector {which}  |A|={len(wit['A'])} |Q|={len(wit['free'])}"
              f" wt(f)={wit['wtf']}  ->  simulator: {r if r is None else {k: r[k] for k in ('nfaults','silent_round','silent_final','nontrivial','Ewt')}}"
              f"   {'PASS' if ok else 'FAIL'}")
    s = byclass[max(byclass)][0][0]
    print("  trivial weight-12 witness (Z):", trivial12(s, 'Z', poolZ))
    print("  trivial weight-12 witness (X):", trivial12(s, 'X', poolX))
```

### `analyze.py`

```python
"""Analysis of the full sweep: histograms, timing-free relaxation comparison, best schedules."""
import numpy as np, pickle, itertools, sys
from collections import Counter, defaultdict
from gross import HX, HZ, NG
from tanner import zcheck_nb, xcheck_nb, xchecks_of, zchecks_of, is_interleaved
from full import SectorFull, sched_sector, orbit_reps

poolZ = np.load('poolZ.npy'); poolX = np.load('poolX.npy')
secZ = SectorFull('Z', poolZ, zcheck_nb, xchecks_of)
secX = SectorFull('X', poolX, xcheck_nb, zchecks_of)


def relax_value(sec, order):
    """12 - max gain over the 30 orbit reps: the timing-free (extended-code style) value."""
    skey = (tuple(sorted(order[:2])), order[2], tuple(sorted(order[4:])))
    best = 0
    for ri in range(len(sec.reps)):
        p = sec.packings(ri, skey)
        if p:
            best = max(best, p[0][0])
    return 12 - best


d = pickle.load(open(sys.argv[1] if len(sys.argv) > 1 else 'full.pkl', 'rb'))
recs = d['recs']
print("schedules evaluated:", len(recs))
print("overall certified upper bound histogram :", dict(sorted(d['hist'].items())))
print("  interleaved      :", dict(sorted(d['hist_i'].items())))
print("  non-interleaved  :", dict(sorted(d['hist_n'].items())))
print("Z-sector           :", dict(sorted(Counter(r[1] for r in recs).items())))
print("X-sector           :", dict(sorted(Counter(r[2] for r in recs).items())))

# timing-free relaxation vs circuit-level bound
joint = Counter(); block = Counter(); relhist = Counter()
byP = defaultdict(Counter)
for (s, bz, bx) in recs:
    oz, _, _, _ = sched_sector(s, 'Z'); ox, _, _, _ = sched_sector(s, 'X')
    rz = relax_value(secZ, oz); rx = relax_value(secX, ox)
    r = min(rz, rx); c = min(bz, bx)
    joint[(r, c)] += 1; block[c - r] += 1; relhist[r] += 1
    byP[len(s[0] & {1, 2, 3})][c] += 1
print("\ntiming-free relaxation value (upper bound on d_ext) histogram:", dict(sorted(relhist.items())))
print("blocking  c - r  (how much the detector timing costs) :", dict(sorted(block.items())))
print("\njoint (relaxation r, circuit bound c) table:")
rs = sorted({k[0] for k in joint}); cs = sorted({k[1] for k in joint})
print("      " + "".join(f"c={c:<7}" for c in cs))
for r in rs:
    print(f" r={r:<3}" + "".join(f"{joint.get((r,c),0):<9}" for c in cs))

best = max(min(r[1], r[2]) for r in recs)
top = [r for r in recs if min(r[1], r[2]) == best]
print(f"\nmaximum certified upper bound over the class: {best}   attained by {len(top)} schedules")
for s, bz, bx in top[:5]:
    print("   P=", sorted(s[0]), "alpha", s[1], "beta", s[2], "gamma", s[3], "delta", s[4],
          " Zbound", bz, " Xbound", bx, " interleaved" if is_interleaved(s) else " NON-interleaved")
lo = min(min(r[1], r[2]) for r in recs)
bot = [r for r in recs if min(r[1], r[2]) == lo]
print(f"minimum certified upper bound over the class: {lo}   attained by {len(bot)} schedules")
for s, bz, bx in bot[:3]:
    print("   P=", sorted(s[0]), "alpha", s[1], "beta", s[2], "gamma", s[3], "delta", s[4],
          " Zbound", bz, " Xbound", bx, " interleaved" if is_interleaved(s) else " NON-interleaved")
```


---

## 12. Honest limits of this session

1. **No lower bounds anywhere.** Every entry of every histogram is an upper bound witnessed by an
   explicit, simulator-verified fault set. A schedule reported at 11 or 12 is a schedule for which
   *my family `W` contains no smaller witness*; it is **not** a schedule shown to have
   `d_circ ≥ 11`. Given that `W` missed the true value by 1–3 for the non-interleaved schedules in
   §6, I expect the 11 and 12 entries in §8.3 to be soft.
2. **Scope of `W`** — §8.1. In particular: at most 2 measurement faults; net error restricted to
   weight-12 logical cosets (weight-14 logicals are *not* enumerated, and they matter: a weight-4
   suffix inside a weight-14 logical also gives 11); last round only; packing enumeration truncated.
3. **Pool completeness is saturated, not certified.** The 1 884 count is stable but unproved.
4. The reduction "last round is WLOG" and the CNOT-fault collapse of §5 are derivations of mine that
   have had no independent review — CONJECTURED (sketch). Both are used only to argue that my column
   list is *complete*; if either is wrong, my bounds remain valid upper bounds, and only the
   "nothing smaller in `W`" language weakens.
5. I did not recover the SBB candidate circuit, did not read the Shaw–Terhal morphing paper, and did
   not attempt Route 1. The `P`/`D` re-estimates in §9 are scheduling judgements, not measurements.
