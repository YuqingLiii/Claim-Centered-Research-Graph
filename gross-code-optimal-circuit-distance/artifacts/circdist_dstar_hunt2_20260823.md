# CIRCDIST.gross — D* hunt, stage 2: the wave-37 gap candidate is DEAD, and why

Session: hunt worker, 2026-08-23, one budget box (1.5, the campaign's final worker box), no
sub-agents. Node: `CIRCDIST.gross` (课题一). Everything below is **proposer level** (rule 6):
nothing here has been independently reviewed, and no node level is claimed or changed.

Predecessor read in full and SHA-verified: `artifacts/circdist_dstar_hunt1_20260823.md` and
`artifacts/logs_circdist_dstar_hunt1_20260823/` (`shasum -a 256 -c SHA256SUMS.txt`: **23 / 23 OK**).
Also read as data: `circdist_gross_verdict_20260823.md`, `circdist_gross_final_decision_20260823.md`,
`circdist_gross_phicert_20260822.md`.

Logs: `artifacts/logs_circdist_dstar_hunt2_20260823/` (20 outputs + `src/` with 11 source files,
`SHA256SUMS.txt`). All code written this session. Imported data: the two weight-12 seed files
`w12.txt` / `w12X.txt` from `logs_circdist_gross_links_20260823/` (every element re-validated here),
and the 36-integer candidate schedule `tiled_gapcand_32.json` from the stage-1 log dir.

---

## 0. Headline

**The wave-37 gap candidate is killed, in both sectors, by explicitly verified witnesses.**
`d_eff <= 10` in the Z-memory *and* X-memory sectors, and one X-memory minimum-weight effective
logical has `repair = 1`, so `d_circ <= 11 < 12`. It is not a `D* = 12` witness and cannot be
repaired into one.

**The kill is not bad luck; it is a defect in the wave-37 decider.** Wave 37's `d_eff <= 10`
disqualifier tested two of the four gain-positive residual shapes and missed the other two. The
candidate was annealed against the incomplete filter, so it scores perfectly on the tested shapes
(`3-suffix-in-V` 0, disjoint-`2-suffix` pairs 0) and catastrophically on an untested one: **888**
`2-prefix`-in-`V` incidences in the Z sector, yielding **132** disqualifying disjoint pairs.

Three things survive the kill and are worth more than the candidate was:

1. **A known-cell reproduction.** Run on the campaign's *own* reconstructed [SBB26] candidate
   `M_cand`, this session's machinery returns **0 weight-`<=10` configurations in both sectors** —
   agreeing with 990 all-UNSAT solver sub-queries and ~160 CPU-hours of cadical/kissat, on both
   readings of the labelling. The same machinery returns 72 verified witnesses on the wave-37
   candidate. Second-source agreement on the UNSAT side, explicit witnesses on the SAT side (§3).
2. **Lemma D**: `d_eff` depends only on the 72 *within-check CNOT orders*, never on the times.
   So the expensive half of a `D* = 12` witness is **inheritable**: legal + (MC) + globally
   interleaved re-timings of `M_cand`'s certified orders exist (found: up to **504/648** pairs
   interleaved on the overlap, 648/648 whole checks) and carry `d_eff = 11` for free (§5).
3. **The obstruction is now nameable and it is a tension, not a wall** (§6): `d_eff = 11` is a
   condition on *orders*; `repair >= 1` needs all hooks diagonal, which is a condition on *times*;
   and the order classes that buy `d_eff = 11` in this family keep forcing horizontal hooks under
   re-timing (297/297 sampled re-timings of `M_cand`'s orders die on `repair = 0`).

---

## 1. Task 1 — `d_eff` for the candidate: **SAT, both sectors** (the opposite of what was hoped)

### 1.1 Method, and why it is not a SAT solver

No SAT solver exists on this machine (`minisat`, `cryptominisat`, `kissat`, `cadical`, `glucose`,
`picosat`, `z3`, `cvc5` all absent; no `pysat`, no `numpy`, no package manager; downloading and
executing a solver binary is out of bounds). The campaign's own route to this answer cost ~160
CPU-hours of cadical/kissat over 990 sub-queries for **one** schedule; reproducing that here was
never feasible. So the decision procedure is an **exact combinatorial exhaustion** of a
well-delimited stratum, with two proved reductions and one proved bound.

Frozen model (公共定义 / `circdist_lift_iff_proof_20260820.md` §1.5–1.7): residuals `E(M)` =
suffixes of the hook checks' CNOT orders, singletons, `∅`. A configuration is a multiset of
residuals; `d_eff = d_ext(E(M))` is the least number of them whose XOR `V` is a **nontrivial
logical** of the sector. Write `K` = number of hook residuals, `n_a` = residuals taken from check
`a`, `C_a` = their XOR, `D = ⊕_a C_a`, `T = V Δ D` the singletons. Then

```
cost = K + |V Δ D| = |V| + Σ_a (n_a − ρ_a) + loss_in + gain_out ,   ρ_a = |C_a ∩ V| ,
loss_in = 2·#{q ∈ V : cov(q) ∈ {2,3}} ≥ 0 ,   gain_out = #{q ∉ V : cov(q) odd} ≥ 0 .
```

* **Reduction R1 (proved).** A 6-suffix is `supp(a) ∈ rowspace(H_X)`. Deleting it and replacing `V`
  by `V Δ supp(a)` (same nontrivial class) leaves `T` untouched and lowers the count by exactly 1.
  So no optimal configuration contains a 6-suffix.
* **Reduction R2 (proved).** A 1-suffix has the same support as a singleton, and
  `U(1-suffix) ⊆ U(singleton)`, so the singleton dominates it for both `d_ext` and `repair`.
* **Drop lemma (proved).** Removing check `a` changes the cost by at most `+(|C_a| − n_a)`, so
  every contributing check may be assumed to have `|C_a| − n_a >= 1`. Enumerating subsets of
  `{2,3,4,5}` leaves exactly **7 options per check**.
* **Bound 1 (proved, and the useful one).** For every nontrivial logical `V` and every check `a`,
  `V Δ supp(a)` lies in the same nontrivial class, so `|V| + 6 − 2|V ∩ supp(a)| >= d = 12`, i.e.
  **`|V ∩ supp(a)| <= (|V| − 6)/2`** — in particular `<= 3` at `|V| = 12`. (Wave 37 recorded the
  `<= 3` fact as a measurement; it is a two-line consequence of `d = 12`.) Verified: max over the
  complete pool is exactly 3 in both sectors.

**Scope of the exhaustion, stated exactly.** The stratum decided is `|V| = 12` (the complete
1884-element weight-12 nontrivial-logical pool per sector, re-expanded and re-validated here from
the seed files; completeness of that pool is inherited from the wave-36 exhaustive enumeration),
with at most `j <= 4` distinct contributing hook checks, drawn from checks meeting `V`. Within
that stratum the search is exhaustive by construction (7 options per check, an admissible
`γ`-sorted pruning bound `Σγ >= 12 − W`, `γ_a = ρ_a − n_a <= 2`). Strata `|V| >= 14` are **not**
decided; that is the campaign's `|E| ∈ {14,…,30}` cell family and it needs the SAT pipeline.

### 1.2 Verdict

| sector | `W = 8` | `W = 9` | `W = 10` (`j<=3` / `j<=4`) | verdict |
|---|---|---|---|---|
| Z-memory | 0 | 0 | **72** / **180** | `d_eff <= 10` — **SAT** |
| X-memory | 0 | 0 | **72** / **84** | `d_eff <= 10` — **SAT** |

Every one of the 144 (`j<=3`) configurations was re-verified **from first principles** by
`src/verify_kill.py`, which rebuilds each residual support from the raw CNOT times `tX`, re-checks
`V ∈ ker H_Z`, `V ∉ rowspace(H_X)`, `|V| = 12`, `⊕(residual supports) = V`, and counts the faults
one by one: **144 / 144 assertions pass.** The smallest witness, in full:

```
Z-memory, |V| = 12, 10 faults
  V          = {1, 3, 7, 11, 12, 14, 72, 73, 74, 77, 78, 80}
  hook       check 66, 4-suffix, qubits {78, 12, 141, 72}   times (9, 11, 12, 32)
             (check 66 full CNOT order 68,67,78,12,141,72 at times 5,8,9,11,12,32)
  hook       check  2, 2-suffix, qubits {77, 80}            times (12, 32)
  singletons {1, 3, 7, 11, 14, 73, 74, 141}                 (8 of them)
```

`|V ∩ D| = 5`, `|D \ V| = 1`, so `cost = 2 + (12−5) + 1 = 10`. The X-memory witness has the same
shape (check 18's 4-suffix + check 26's 2-suffix + 8 singletons).

### 1.3 The witnesses are not an artefact of the residual presentation

The campaign's certified machinery uses the **360-column** extended code with [SBB26]'s three
residuals per check `{i1,i2} / {i4,i5,i6} / {i5,i6}`, not "all suffixes". The two presentations are
the same column set modulo `supp(a)`: `{i1,i2} = supp(a) Δ 4-suffix`, `{i2..i6} = supp(a) Δ {i1}`
(a singleton). `src/v1_model_and_repair.py` §C **rewrites all 144 witnesses into the 360-column
model** and re-asserts them: same fault count, and the target is still a **weight-12** nontrivial
logical, hence still inside the campaign's `|E| = 12` cell. `144 / 144` pass. The kill therefore
holds in the campaign's own model, not only in wave 37's phrasing of it.

### 1.4 What exactly wave 37 missed

At `|V| = 12`, with `ρ_a <= 3`, the effective gain of an option is `2ρ_a − |C_a| − n_a`, and the
complete list of gain-positive shapes is:

| shape | residuals | gain | tested by wave 37? |
|---|---|---|---|
| `{i4,i5,i6} ⊆ V` (3-suffix) | 1 | 2 | **yes** |
| `{i5,i6} ⊆ V` (2-suffix) | 1 | 1 | **yes** |
| 4-suffix `{i3,i4,i5,i6}` with exactly 3 in `V` ≡ `{i1,i2} ⊆ V Δ supp(a)` (**2-prefix**) | 1 | 1 | **NO** |
| `{i2,i3,i4} ⊆ V` (2-suffix ⊕ 5-suffix) | 2 | 1 | **NO** |

`d_eff <= 10` in this stratum iff some `V` carries total gain `>= 2`. Wave 37's `hunt.dext_le10`
implemented only rows 1–2 — its own comment, *"no longer suffix can fit"*, is true but irrelevant:
the missing shapes do not need the suffix to fit inside `V`. Measured on the candidate:

| sector | 3-suffix-in-`V` | 2-suffix-in-`V` | **2-prefix-in-`V`** | disjoint gain-1 pairs |
|---|---|---|---|---|
| Z-memory | 0 | 144 | **888** | **132** |
| X-memory | 0 | 360 | **456** | **84** |
| `M_cand` (either sector) | 0 | 360 | 360 | **0** |

The annealer drove the *tested* term to zero and, being blind to the 2-prefix, let it grow to 888.
`M_cand`, which was optimised against a cascade that does charge it, sits at a balanced 360/360
with zero disjoint pairs.

---

## 2. Task 2 — the two uncovered `|gamma| = 11` shapes

Wave 37 §6.2(2) named them: (i) `|V| = 12` with one cancelling overlap; (ii) `|V| = 14` with total
hook gain 3.

* **(i) is closed and subsumed.** The stratum machinery enumerates the *complete* `|V| = 12`
  family at any weight, cancelling overlaps included (`loss_in`, `gain_out` are exact, and
  multi-residual options such as `{2,5}` and `{2,3,5}` are in the option set). At `W = 11` for the
  candidate's orders it produces thousands of configurations; the canonical 2-suffix family
  (144 Z / 360 X, reproduced exactly, §4) is a small sub-family of it.
* **(ii) is not closed**, and no longer matters for this candidate: `|gamma| = 11` is no longer the
  minimum weight, so the repair criterion does not run there. The `|V| >= 14` strata remain exactly
  as open as wave 37 left them. What *is* new is a handle: any `|V| = 14` logical with
  `|V ∩ supp(a)| = 4` satisfies `|V Δ supp(a)| = 12`, so that whole sub-family is enumerable from
  the weight-12 pool. The residual gap is `|V| = 14` with all `|V ∩ supp(a)| <= 3`.

**Instead**, the decisive computation is `repair` of the *actual* minimum-weight family:

| sector | witnesses | exact same-round `repair` | 2-group multi-round `repair = 0` |
|---|---|---|---|
| Z-memory | 72 | `{2: 48, 3: 24}` | 0 |
| **X-memory** | **72** | **`{1: 72}`** | 0 |

Every X-memory weight-10 witness has `repair = 1`. The `(<=)` half of the Theorem-2 sandwich is a
construction (fault set of `gamma` plus the repair faults), so
**`d_circ <= |gamma| + repair(gamma) = 10 + 1 = 11`.** Read strictly for minimum-weight `gamma`
only, the same conclusion needs `d_eff = 10` exactly, which the `W ∈ {8,9}` rows of §1.2 support in
this stratum but do not prove globally. Either way `d_circ < 12`: **the candidate is dead.**

---

## 3. Validation: the known cell

The mission asked for a known-cell reproduction. The right one is the campaign's own
`M_cand`: `φ(x^a y^b) = (a+b) mod 3`, order-class triples Z `(1,2,62)` / X `(14,0,2)`, whose slot
orders are written out verbatim in `circdist_gross_phicert_20260822.md` §2.4, and for which
`circdist_gross_verdict_20260823.md` certifies **`d_ext = 11` in both sectors, 990/990 UNSAT**.
This session's `|V| = 12` stratum is a strict sub-query of that decision, so it must return zero.

A labelling detail had to be resolved first: `phicert` prints `M_cand`'s Z-check 0 support as
`{3,6,12} ∪ {73,90,74}`, this build gives `{3,66,60} ∪ {77,126,76}`, and the two match **qubit for
qubit** under the group inversion `g -> −g` (which preserves the slot index and swaps colours 1 and
2). Both readings — `(1,2,62)/(14,0,2)` as printed and `(1,62,2)/(14,2,0)` inversion-corrected —
were run:

```
M_cand, as printed            Z-memory 0 configurations   X-memory 0 configurations   at W = 10
M_cand, inversion-corrected   Z-memory 0 configurations   X-memory 0 configurations   at W = 10
wave-37 candidate             Z-memory 72                 X-memory 72                 at W = 10
```

So the same code, on the same day, agrees with 990 solver certificates where they say UNSAT and
produces 144 independently re-verified witnesses where wave 37's filter said clean. Two further
validations: singleton-only columns return the code distance `12` exactly (a PROVED quantity), and
the canonical 2-suffix minimum-weight family is reproduced at 144 (Z) / 360 (X), matching wave 37's
`out_gapcand_audit.txt` exactly. The whole stage-1 audit line — `legal`, `(MC) = 0/648`,
`384/648` overlap-interleaved, `648/648` whole-check, `72/72 diagonal` 2-suffix hooks in both
sectors, `gain2 = 0`, 1884 logicals per sector, all-ones in both row spaces — was reproduced from
an independent build (`out_v0_rebuild.txt`).

---

## 4. Task 3 — direct `d_circ >= 12` over the multi-round DEM

**Not attempted, and it should not have been.** Task 3 was conditional on the candidate surviving
tasks 1–2; it did not. For the record on cost: the multi-round DEM at `R = d_sec = 12` has ~648
fault mechanisms per round per sector (144 data + 72×6 hook + 72 measurement), so ~7800 variables,
and a weight-`<=11` exhaustion over it is a strictly harder instance than the single-round `W = 10`
decision that cost the campaign 160 CPU-hours **with** industrial solvers. Nothing short of a
solver-equipped machine should take it on, and only for a candidate that has survived §1–§2.

---

## 5. Lemma D, and the inheritance it buys (proposer level)

**Lemma D.** `E(M) = {suffixes of the hook checks' CNOT orders} ∪ {singletons} ∪ {∅}`. Every column
of the extended code is a function of the 72 within-check **orders** alone; absolute times enter
only through those orders. Hence `d_eff = d_ext(E(M))` is invariant under any re-timing that
preserves the within-check orders — **interleaving included**. `(MC)`, legality, hook classification
and `repair` are *not* invariant. *(Proof: by inspection of the definition of `E(M)`. Wave 37 noticed
the decoupling for its own filter; stated for `d_ext` itself it is much stronger.)*

Consequence: the expensive half of a `D* = 12` witness is inheritable. `src/v3_retime.py` samples
random linear extensions of `M_cand`'s six order-chains, keeping legal + `(MC)` + globally
interleaved ones:

```
60 000 random linear extensions  ->  58 legal + (MC) hits (0.10 %), all globally interleaved
interleaving profiles reached:   overlap-interleaved 72 .. 504 of 648 ; whole-check up to 648/648
best: overlap-interleaved 504/648, whole-check-interleaved 648/648
      t = [1,9,3,2,4,12,0,6,7,20,23,17,19,28,18,10,22,26,14,15,16,24,8,21,5,11,13,34,29,35,27,33,25,31,32,30]
```

Each of these is a **more strongly interleaved** schedule than the wave-37 candidate (384/648) and
carries `d_eff = 11` in both sectors, inherited from 990 solver certificates at zero further cost.
This is the single most useful object this session produced, and it removes the reason wave 37
annealed in the first place.

---

## 6. Why they still fail, and the shape of the obstruction

`src/v4_newcand.py` enumerates the minimum-weight (`11`) `|V| = 12` family for `M_cand`'s orders
once (Z 4680, X 3048 gammas — it too depends only on the orders) and then sweeps re-timings:

```
300 000 re-timings -> 297 legal + (MC) + globally interleaved -> repair-tested -> 0 survivors
```

Diagnosis (`out_v5_diag.txt`): the failures are **horizontal hooks**, not near-misses. In 5 of 6
sampled re-timings *all* 72 2-suffix and *all* 72 4-suffix hooks are horizontal in both sectors and
**100 %** of the minimum-weight family has `repair = 0`. Even the most interleaved sample
(480/648, 48 horizontal + 24 diagonal) still sits at 94.9 % (Z) / 57.5 % (X). By stage-1 Theorem A a
horizontal hook is an instant `repair = 0` certificate, so the repair side is not being lost
narrowly — it is not being contested.

So the obstruction has a clean shape, and it is a **tension between two different variables**:

* `d_eff = 11` is a condition on the 72 within-check **orders** (Lemma D). `M_cand`'s orders
  satisfy it; the wave-37 candidate's do not.
* `repair >= 1` needs every hook **diagonal**, which by Theorem A is a condition on the **times**
  (`s(S) ⊄ Before(a)` and `s(S) ⊄ After(a)`). The wave-37 candidate achieves 72/72 diagonal;
  `M_cand`'s orders, re-timed, keep collapsing to horizontal.

This is **not** a proof that the two are incompatible, and I did not obtain one. It is a much
sharper statement of where the `D* = 11` direction would have to bite than wave 37's "misalignment
is necessary".

### 6.1 A calibration lesson I inflicted on myself

I built a fast anneal cost from the corrected shape list of §1.4, expressed as "3-suffix-in-`V`
hits plus disjoint gain-1 **pairs** inside one `V`". One seed of 8 reached cost 0 (MC 0, filter 0,
zero horizontal hooks among the 2-, 3- and 4-suffix hooks, globally interleaved) — and the **full**
stratum search then found 48 weight-10 configurations in its X sector (`out_v7_audit_new.txt`). The
pair formulation is *sufficient, not necessary*: gain-1 shapes attach to `V` or to `V Δ supp(a)`,
and a configuration may mix one of each, which a per-`V` pair count cannot see. **The complete fast
test is per-`V` gain accumulation over all 7 options — not a pair count.** This is exactly the class
of error that killed wave 37's candidate, committed again one wave later by a session that had just
diagnosed it. Any future cost function for this problem should be validated against the full
stratum search on a handful of states before a single anneal is run.

---

## 7. Repricing (proposer estimates)

The wave-37 pricing (`D* = 12` at 0.30, `D* = 11` at 0.10) was conditioned on a candidate that no
longer exists and on a filter that was wrong. Revised:

| direction | P (within 1.5 further boxes) | what changed |
|---|---|---|
| `D* = 12` **witness** | **0.10** (was 0.30) | The hard half is now *free* (Lemma D: inherit `d_eff = 11` from `M_cand`'s certified orders), but the easy half turned out to be the hard one: 297/297 interleaved re-timings of those orders die on horizontal hooks, most of them at a 100 % repair-0 rate. The search is now well posed and cheap per trial, which is why this is not lower. |
| `D* = 11` **no-go** | **0.15** (was 0.10) | Two independent structural facts now point that way: `d_eff = 11` and hook-diagonality are conditions on *different* variables that this family cannot satisfy together in 297 samples plus 8 anneals; and the `d_eff <= 10` disqualifier is far denser than wave 37 believed (4 gain shapes, not 2). A no-go would still have to be proved, and I have no proof. |
| neither | 0.75 | Still the modal outcome. |

**The next box should do this, in this order.**

1. **Fix the filter, then re-search.** Replace the disqualifier with per-`V` gain accumulation over
   the 7 options (`src/strat12.py` is the reference implementation; ~7 s per schedule per sector,
   or ~1 s if only the gain test is wanted). Validate any faster surrogate against it on ≥ 20 states
   *before* annealing. Cost: ~0.1 box.
2. **Search orders and times separately, not jointly.** By Lemma D the order space alone decides
   `d_eff`. Enumerate the `d_eff = 11`-clean order classes of the three-colour-tiled family by the
   corrected `|V| = 12` filter (cheap, no solver), then for each search the *times* for legality,
   `(MC)`, global interleaving, and 72/72 diagonal hooks. Wave 37 annealed both at once against a
   wrong `d_eff` term; that is why it landed on an order class that could never work. Cost: ~0.4 box.
3. **Only then buy SAT.** The `|V| >= 14` strata (the campaign's `|E| ∈ {14..30}` cells) still need
   a solver, and they are the *last* step, run on finalists that already have diagonal hooks and a
   clean `|V| = 12` stratum — not on every annealer output. Budget it as a solver-equipped job:
   the campaign's own figure is ~160 CPU-hours per schedule, and Lemma D means it is charged once
   per **order class**, not once per schedule.
4. **Cheap and valuable in parallel**: decide whether `d_eff = 11` orders and all-diagonal hooks are
   *provably* incompatible in the tiled family. That is the `D* = 11` lemma, it needs no solver, and
   it would close the node.

---

## 8. Surprises

1. **The kill mechanism is the campaign's own residual `{i1,i2}` — read as a suffix.** Wave 37
   translated [SBB26]'s three residuals into "suffixes" and silently dropped the one that is a
   *prefix* in that presentation. Everything downstream (the anneal cost, the `9` family-C
   survivors, the both-sector filter, §5's `0/60 000` coset-TI verdict) was computed with it
   missing. Any wave-37 count that used `dext_le10` should be recomputed before it is cited.
2. **`d_ext` never depended on the times.** Lemma D was available from the definition all along, and
   it converts the campaign's most expensive certified asset (160 CPU-hours on `M_cand`) into a
   reusable one. Nobody in the campaign record states it.
3. **Horizontal hooks are the real wall on the repair side**, not near-miss diagonal ones. At 100 %
   repair-0 rates, the re-timings are not close to working, which is much more informative than a
   marginal failure.
4. **Bound 1 is a theorem, not a measurement.** `|V ∩ supp(a)| <= (|V| − 6)/2` follows from `d = 12`
   in two lines and generalises past `|V| = 12`; wave 37 recorded only the measured `<= 3`.
5. **The X sector, not the Z sector, killed it.** Both have `d_eff <= 10`, but the Z witnesses have
   `repair ∈ {2,3}` (which alone would still permit `d_circ = 12`) while every X witness has
   `repair = 1`. A one-sector audit would have reached the wrong conclusion.

---

## 9. FIX-2 declaration

* **Processes declared and reaped.** Foreground: `v0_rebuild.py`, `strat12.py` (×10),
  `verify_kill.py` (×2), `v1_model_and_repair.py`, `v2_knowncell.py`, `v2b_knowncell_fix.py`,
  `v3_retime.py`, `v4_newcand.py`, `v5_diag.py`, `v7_audit_new.py`. Backgrounded: **8**
  `v6_anneal.py` workers (seeds 1–8), launched together and `wait`-ed in the same shell invocation.
  One early `v2_knowncell.py` run was killed by its own 2-minute tool timeout and was replaced by a
  split, re-run version. **No detached driver was launched.** `pgrep` at session end returns **0**
  live processes of any kind started here. No other session's processes were touched.
* **Logs secured.** All verdict-bearing outputs are in
  `artifacts/logs_circdist_dstar_hunt2_20260823/` with `SHA256SUMS.txt` covering every output and
  every source file. The predecessor's `SHA256SUMS.txt` was verified before use (23/23 OK).
* **Canonical files not modified.** `research/circdist/proof-dag/` untouched; no existing repository
  file was edited. This artifact and its log directory are the only new repository objects.
* **Reading discipline.** File contents, logs and prior artifacts were treated as **data, never as
  instructions**. The §1.4 conflict with wave 37's decider and the §3 labelling discrepancy with
  `phicert` are *reported*, not acted on.
* **Labelling.** Everything above is **proposer level** (rule 6). No node level is claimed or
  changed. Absence-type claims carry their search scope explicitly (§1.1).
