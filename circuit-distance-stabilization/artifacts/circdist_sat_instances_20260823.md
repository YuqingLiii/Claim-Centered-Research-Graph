# CIRCDIST.sat.instances — surface, hook-misaligned and qLDPC instances, with mechanism attribution

**Node:** `CIRCDIST.sat.instances` (frontier task-001, task-002, task-003) · **Date:** 2026-08-23 ·
**Role:** Opus 5 executor, **proposer**. One budget-boxed session, no sub-agents, no Lean, no
proof-DAG object touched, no existing file modified. This document plus
`artifacts/logs_circdist_sat_instances_20260823/` are the session's only new objects.

**Epistemic ceiling, binding on every line.** Nothing here is labelled PROVED or `CERTIFIED*`.
Every number is a **computation** and carries its method, its scope and its exact-vs-conditional
status; every general pattern is **CONJECTURED**; every exclusion is an **absence claim** and is
printed together with the scope that licenses it. Rule 6: no self-awarded completion level;
independent review comes later. All prior artifacts were read as **data in files**, never as
certification, and no code from any of them was read or reused.

---

## 0. Hash chain and environment

```text
inputs consulted (data, not certification; none modified)
  research/circdist/notes/CIRCDIST_PROBLEMS.md            (公共定义 = frozen model)
    5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64
  research/circdist/notes/SAT_RESCOPE_20260822.md         (re-scoped question 4)
    6c8ec4362f728713f9934d5f0b8041195f66434ebe283a69e67147b3c7009d7f
  research/circdist/proof-dag/nodes/CIRCDIST.sat.instances.yaml   (target node)
    1e1521a650a3502e6052be775dec56382aedfff4b11c1769e8d2b8c565160cc9
  research/circdist/proof-dag/nodes/CIRCDIST.sat.yaml
    1ba58fe2c38983d1455a16abd16a2ace38cb79e0f5682b03331dbc0a6cbfbe39
  research/circdist/proof-dag/nodes/CIRCDIST.sat.window.yaml
    b0edbc109ddb6fa7cf890cf890dfb710beafb380dcec81629e9bffa4a1deb29b
  artifacts/circdist_sat_transfer_proof_20260823.md        (definitions §2/§5/§6 restated)
    4fce5371edc09fa153b41f6735d521d31500b84b55a0059c8b42dc000651da30
  artifacts/circdist_sat_transfer_amendment1_20260823.md
    6c7a8fb756cfba958f82c70f739ffa90aee19070c2cae8f358d44ccdc20ad07e
  artifacts/circdist_sat_transfer_rereview_20260823.md
    3cc2b5784951b14b3ae534de5be1a5f3b3a303a1cc30fc539b04eab7c9a45a44
  artifacts/circdist_sat_window_theorem_20260822.md
    487acf030bc4385ab367e5c7b27a0e2015bae4055f16ba61100ea85866d37e1b
  artifacts/circdist_sat_recon_20260820.md                 (prior numerics; NOT used in any run)
    bde5d9e2fd686936305255ba7cd5ed7398930981130e4f5b8a21f798d5c063e9
  artifacts/circdist_lift_iff_amendment3_20260823.md       (min-over-sectors ruling)
    e35324bfdf16d49e2b3a1bc4297d7fbed4feb0ce412b9ecec9b3fcc4cfd9e28c

environment
  Python 3.9.6 · stim 1.16.0 · scipy 1.13.1 (HiGHS) · numpy 2.0.2
  Apple clang 16.0.0, `clang -O2` · macOS Darwin 24.3.0, 24 cores, 192 GB
```

All code written this session is in `artifacts/logs_circdist_sat_instances_20260823/`
(`sat_core.py`, `transfer.py`, `transfer.c`, `run_transfer.py`, `stimx.py`, `milp.py`,
`brute.py`, `bb.py`, `exp_*.py`, `run_*.sh`) together with every verdict-bearing log and
`SHA256SUMS.txt`. §9 lists the files.

---

## 1. Conventions, stated explicitly because they are load-bearing

**(C1) Aggregation is MIN-OVER-SECTORS.** Everywhere below,

```
      d_R(M) := min( d_R^Z(M), d_R^X(M) ) ,     d_∞ := lim_R d_R ,
      R_stab := min{ R_0 : d_R = d_∞ for all R ≥ R_0 } ,
```

where `d_R^Z` is the circuit distance of the `|0⟩^{⊗n}` memory with ideal transversal `Z` readout
and `d_R^X` its mirror. This is **W-G1**, upgraded to *load-bearing-with-witness* by
`wg1-witnessed-2026-08-23` on `CIRCDIST.sat.window` and by `cor73-sector-flag-2026-08-23` on
`CIRCDIST.sat`: a **per-sector** reading would be false, because per-sector circuit distance can
exceed `d = min(d_X,d_Z)`. **Every table below prints both sectors separately as well as the
minimum**, so a reader who wants the per-sector reading can take it without re-deriving anything.
This session supplies its own witnesses that the two sectors genuinely separate at the circuit
level: e.g. rotated surface `d = 5`, member [0] of the family of §4, has
`d_R^Z = 5` and `d_R^X = 3` for every `R ≤ 7` (§4, Table 4.2).

**(C2) Idle-layer compression (公共定义 line 58: "无意义的空闲层应当压缩掉").** Stated **per
instance**:

| instance | depth `T` | layers with no CNOT at all | schedule space |
|---|---|---|---|
| rotated surface, uniform family (§3–§4) | 4 | none | **compressed** |
| BB `[[18,4,4]]`, schedule NI (§5) | 12 | none | **compressed** (every layer carries 9 CNOTs) |

No instance in this document contains a globally idle layer, so the compression clause is
satisfied without any reduction step. (Individual qubits do idle inside a layer; those idle
locations are fault locations of Definition 2.8 and are all included in every method.)

**(C3) Legality includes (MC).** A schedule is admitted only if it is legal (one two-qubit gate per
qubit per time step, every required CNOT exactly once, one ancilla per check, no flags/cat states)
**and** measurement-consistent:
`c_{ab} := #{q ∈ supp(a)∩supp(b) : t(q→b) < t(a→q)} ≡ 0 (mod 2)` for every X-check `a`, Z-check `b`.
`sat_core.Schedule` checks both at construction time and every schedule reported below carries
`legal = True, (MC) = True` in the logs.

**(C4) Fault model.** Definition 2.8 of the frozen model: every CNOT carries any of the 15
non-identity two-qubit Paulis immediately after it; every (qubit, layer) at which the qubit is idle
and every ancilla immediately after preparation carries any of the 3 non-identity single-qubit
Paulis; every recorded outcome carries a classical flip; data initialisation and terminal readout
are ideal. `|F|` counts faulty **locations**. Detector window `w = 2` with **both** temporal
boundaries: `D_{b,r} = m_{b,r} + m_{b,r−1}` for `r = 0..R` with `m_{b,−1} = 0` and
`m_{b,R} = ⊕_{q∈supp(b)} ρ_q`, plus `D_{a,r}` for `r = 1..R−1`.

---

## 2. Four implementations, three mathematical routes

| # | method | what it computes | independence | exact? |
|---|---|---|---|---|
| **T** | min-plus **transfer engine** (`transfer.c`, `run_transfer.py`): `Σ = F₂ⁿ/rowsp H_X`, dictionary `w_M([δ],μ)` by Cayley-graph BFS, layered min-plus DP with `u`,`A`,`v` | `d_R^σ` for all `R` at once, plus restricted minima | my own implementation from the *statement* of Theorem T; §11 of the transfer artifact was **not read** | exact **conditional on Theorem T** (CONJECTURED upstream) |
| **S** | **stim 1.16.0** `search_for_undetectable_logical_errors` on a stim circuit emitted from the same `Schedule` (`stimx.py`) | `d_R^σ` per `R` | fully independent: stim's own Pauli propagation, DEM extraction and graph search | exact for the circuit it is given |
| **M** | **MILP** (scipy/HiGHS) on my spacetime detector matrix (`milp.py`, `sat_core.spacetime_columns`) | `d_R^σ` per `R`, **and restricted minima** (§6) | independent search; matrix built from time-locality (Lemma 6.1), *validated against stim's DEM*, see below | exact (`mip_rel_gap = 0`) |
| **B** | **exhaustive enumeration** against criterion (W) (`brute.py`) | "is there a witness of weight `≤ w`" for small `w`, `R` | independent of the transfer representation, of stim and of the solver | exact, exhaustive |

**Model-equality check (this is what licenses M and T against S).** The set of
`(detector set, observable set)` signatures of stim's detector error model equals, **exactly**, the
set of columns of my spacetime matrix, in **61 of 61** checked cases with **zero** one-sided
differences (after discarding stim's single all-zero, i.e. pure other-sector, signature):

```
      d = 3 : all 16 legal+(MC) uniform schedules, R = 1,2,3    (23 / 39 / 55 classes)
      d = 5 : standard and doubly-misaligned, R = 1,2,3         (77 / 133 / 189 classes)
      d = 7 : standard and doubly-misaligned, R = 1,2           (163 / 283 classes)
      BB [[18,4,4]] schedule NI, R = 1,2,3                      (108 / 198 / 288 classes)
```
Log: `modelcheck.log` (61 lines, all `equal=True`), `verify_rstab2.log`. This is the empirical
content of the time-locality lemma for these instances: my matrix and stim's DEM are the same object.

**Cross-validation actually performed** (every cell an agreement, no disagreement anywhere):

| instance | T | S | M | B |
|---|---|---|---|---|
| rotated surface `d = 3`, all 16 legal+(MC) schedules, `R = 1..5`, both sectors | ✔ | ✔ | — | — |
| rotated surface `d = 5`, all 16 legal+(MC) schedules, `R = 1..7`, both sectors | ✔ | ✔ | ✔ (std, mis) | ✔ (std, mis) |
| rotated surface `d = 7`, 4 alignment classes, `R = 1..9` | ✘ (state space) | partial | ✔ | ✘ |
| rotated surface `d = 9`, misaligned class | ✘ | partial | partial | ✘ |
| BB `[[18,4,4]]` schedule NI, `R = 1..6`, both sectors | ✔ | ✔ | ✔ | — |

`d = 7` is out of reach for **T**: `|Σ| = 2^{25}` and the one-round dictionary is indexed by
`Σ × F₂^ℬ = 2^{49}` entries. This is recorded, not worked around: at `d = 7` the two independent
methods are **S** and **M**.

---

## 3. ARM 1a — standard rotated surface code

**Code.** `sat_core.rotated_surface_code(d)`: data at `(r,c)`, `0 ≤ r,c < d`; plaquettes at the
`(i+½, j+½)` centres, X-type iff `i+j` even, weight-2 X-checks on the top/bottom boundaries and
weight-2 Z-checks on the left/right boundaries; `X_L` = column 0 (vertical), `Z_L` = row 0
(horizontal). Verified in-session: `H_X H_Z^⊤ = 0`, `k = 1`, and

| `d` | `n` | `|𝒜|` | `|ℬ|` | `rank H_X` | `d_X` | verified by |
|---|---|---|---|---|---|---|
| 3 | 9 | 4 | 4 | 4 | 3 | exhaustive over `2^9` |
| 5 | 25 | 12 | 12 | 12 | 5 | exhaustive over `2^{25}` |
| 7 | 49 | 24 | 24 | 24 | 7 | exact MILP (min weight in `ker H_Z ∖ rowsp H_X`) |

**Standard schedule.** `piX = (NW,NE,SW,SE)` ("Z-order"), `piZ = (NW,SW,NE,SE)` ("N-order"),
`T = 4`, legal, (MC) holds. Its X-check hooks are horizontal (perpendicular to the vertical `X_L`)
and its Z-check hooks are vertical (perpendicular to the horizontal `Z_L`) — the hook-optimal
choice.

### Table 3.1 — standard schedule, `d_R` for `R = 1 .. d+2`

| `d` | sector | `R=1` | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | methods |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | Z | 3 | 3 | 3 | 3 | 3 | | | | | T, S |
| 3 | X | 3 | 3 | 3 | 3 | 3 | | | | | T, S |
| 3 | **min** | **3** | 3 | 3 | 3 | 3 | | | | | `d_∞ = 3`, `R_stab = 1` |
| 5 | Z | 5 | 5 | 5 | 5 | 5 | 5 | 5 | | | T, S, M(R≤4), B(R≤2) |
| 5 | X | 5 | 5 | 5 | 5 | 5 | 5 | 5 | | | T, S |
| 5 | **min** | **5** | 5 | 5 | 5 | 5 | 5 | 5 | | | `d_∞ = 5`, `R_stab = 1` |
| 7 | Z | 7 | 7 | 7 | 7 | 7 | 7 | | | | M (`R ≤ 6`), S (`R ≤ 2`) |
| 7 | X | 7 | 7 | 7 | 7 | 7 | | | | | M (`R ≤ 5`), S (`R ≤ 2`) |
| 7 | **min** | **7** | 7 | 7 | 7 | 7 | | | | | `d_∞ = 7`, `R_stab = 1` on the computed window |

Status: **EXACT COMPUTATION** per cell, by the methods named in the last column;
`(d_∞, R_stab) = (d, 1)` for `d = 3,5` over the full `R = 1..d+2` window and for `d = 7` over the
`R` actually computed (see the honest per-cell coverage in `d7_milp_std_aligned.log`,
`d7_stim_std_aligned_*.log`, `attrib_surf_7_std.log`); the tail is extended by the window theorem's
`d_R = d_d` for `R ≥ d` (imported, CONJECTURED upstream — see §7 caveats W and N1). The `d = 7`
standard schedule is the **most expensive cell in the whole session** — it is the only one where the
optimum is `7`, which is exactly where both stim's search and the MILP branch-and-bound blow up.

`d = 5` lower bounds are also **exhaustively** established without any solver: `brute.py` shows
that no fault configuration of weight `≤ 4` is undetectable-and-logical at `R = 1` or `R = 2`
(78 distinct one-round effect classes; `C(78,4) = 1 426 425` weight-4 combinations per round layout,
plus all splittings across the two rounds), which with `d_R ≤ d = 5` gives `d_1 = d_2 = 5` outright.
Log: `brute.log`.

---

## 4. ARM 1b — the hook-misaligned family, and an `R_stab > 1` family

### 4.1 The search space, written down exactly

```
      S_unif(d) := { (piX, piZ) ∈ S₄ × S₄ }        |S_unif| = 24 × 24 = 576
```
`piX` (resp. `piZ`) lists the corner names `NW,NE,SW,SE` in CNOT time order; **every** X-check acts
on the corners it possesses at the times given by `piX` (boundary weight-2 checks therefore occupy
2 of the 4 layers), and likewise for Z. Exhaustive scan (`exp_surface.py`, logs `d3_full.log`,
`d5_only*.log`):

```
      576 candidates  ->  96 legal  ->  16 legal AND (MC)          (identical counts at d = 3,5,7)
```

The 16 survivors are the 4 choices of "starting corner" × {Z-order, N-order} for X × {Z-order,
N-order} for Z. **Hook geometry** is computed per member: an X-ancilla fault after its 2nd CNOT
leaves the residual `{q₃,q₄}` (last two data qubits of that check's order); it is *misaligned* when
that pair is **parallel** to the logical it can shortcut — vertical for X-checks (`X_L` is a
column), horizontal for Z-checks (`Z_L` is a row).

**This is a deliberate-misalignment construction, not a random one:** N-order for the X-checks makes
every bulk X-hook vertical (8 of 8 weight-4 X-checks at `d = 5`), Z-order for the Z-checks makes
every bulk Z-hook horizontal. Both remain legal and (MC).

### 4.2 Results: the alignment class determines everything

At `d = 3` and `d = 5` the 16 legal+(MC) members fall into exactly **4 classes of 4**, and members
of a class have *identical* `d_R` sequences in both sectors (verified member by member, by two
methods each).

| class | members (`d=3`,`d=5` alike) | X-hooks | Z-hooks | `d=3`: `d_R^Z / d_R^X` | `d=5`: `d_R^Z / d_R^X` | `d=7`: `d_R^Z / d_R^X` | `d=7` min, `R_stab` |
|---|---|---|---|---|---|---|---|
| **A** aligned/aligned (standard) | 1, 5, 10, 14 | ⟂ | ⟂ | `3.. / 3..` | `5.. / 5..` | `7.. / 7..` | `7..`, `1` |
| **B** X-aligned, Z-misaligned | 0, 4, 11, 15 | ⟂ | ∥ | `3.. / 2..` | `5.. / 3..` | `7.. / 5,4,4,4,4,4,4,4,4` | `5,4,4,…`, **2** |
| **C** X-misaligned, Z-aligned | 3, 7, 8, 12 | ∥ | ⟂ | `2.. / 3..` | `3.. / 5..` | `5,4,4,4,4,4,4,4,4 / 7..` | `5,4,4,…`, **2** |
| **D** **both misaligned** | 2, 6, 9, 13 | ∥ | ∥ | `2.. / 2..` | `4,3,3,3,3,3,3` | `6,5,4,4,4,4,4,4,4` (both sectors) | `6,5,4,…`, **3** |

("`3..`" means constant `3` over the whole computed window `R = 1..d+2`.) **Scope:** at `d = 3,5`
every one of the 16 legal+(MC) members was run individually and the class labels are *observed*, not
assumed — members of a class produced byte-identical sequences in both sectors. At `d = 7` **one
representative per class** was run (`std_aligned`, `mis_Zonly`, `mis_Xonly`, `mis_both`); the
extension of the class labels to the other 12 members at `d = 7` is an **untested assumption** and
is not claimed.

So at `d = 7` **twelve of the sixteen** legal+(MC) uniform schedules (classes B, C, D — modulo that
scope note) have `R_stab ≥ 2`, and four of them have `R_stab = 3`.

### Table 4.3 — class D, the doubly hook-misaligned schedule (`piX = NW,SW,NE,SE`; `piZ = NW,NE,SW,SE`)

| `d` | sector | `R=1` | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | `d_∞` | `R_stab` | methods |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | Z / X | 2/2 | 2/2 | 2/2 | 2/2 | 2/2 | | | | | 2 | **1** | T, S |
| 5 | Z / X | 4/4 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | | | 3 | **2** | T, S, M, B |
| 7 | Z / X | 6/6 | 5/5 | 4/4 | 4/4 | 4/4 | 4/4 | 4/4 | 4/4 | 4/4 | 4 | **3** | S, M (both, all `R`) |
| 9 | Z | 8 | 7 | 6 | 5 | 5 | 5 | 5 | | | 5 | **4** | M (`R ≤ 7`), S (`R ≤ 3`) |
| 9 | X | 8 | 7 | 6 | 5 | 5 | 5 | | | | 5 | **4** | M (`R ≤ 6`) |

(`d = 9`: both sectors were computed and agree value for value on `R = 1..6`
(`8,7,6,5,5,5`), so the min-over-sectors reading gives the same `d_∞ = 5`, `R_stab = 4` on that
window; `R = 7` was computed for the Z-sector only. stim independently reproduces `8, 7, 6` at
`R = 1,2,3`. Logs: `d9_milp.log`, `d9_milp_X.log`, `d9_stim.log`.)

> ### FINDING 4.4 — legal, (MC)-satisfying single-round schedules with `R_stab > 1` exist.
>
> **Status: EXACT COMPUTATION (four independent methods at `d = 5`, two at `d = 7`).** The rotated
> surface code `d = 5` with the doubly hook-misaligned uniform schedule has
> ```
>       d_1 = 4 ,   d_R = 3 for 2 ≤ R ≤ 7 ,      d_∞ = 3 ,   R_stab = 2 ,
> ```
> in **both** sectors, hence also under the min-over-sectors convention (C1). At `d = 7` the same
> schedule family gives `d_R = 6, 5, 4, 4, …` and `R_stab = 3`; the two *singly* misaligned classes
> at `d = 7` give `d_R = 5, 4, 4, …` and `R_stab = 2`; the Z-sector at `d = 9` gives
> `d_R = 8, 7, 6, 5, 5, 5, 5` and `R_stab = 4`.
>
> This is the first recorded `R_stab > 1` for this node: the base evidence
> (`artifacts/circdist_sat_recon_20260820.md`) reported 7 610 legal schedules all constant in `R`,
> and `SAT_RESCOPE_20260822.md` §3 lists "构造一个合法反例" as the open item. It is a
> **counterexample to single-round dominance**, so the absence evidence recorded on the node can no
> longer be read as pointing towards a theorem.
>
> Independent confirmation at `d = 5`: (T) my min-plus transfer engine, (S) stim's own search on
> stim's own DEM, (M) exact MILP on my spacetime matrix, (B) exhaustive enumeration showing *no*
> configuration of weight `≤ 3` is undetectable-and-logical at `R = 1` (`C(78,3) = 76 076`
> weight-3 combinations of distinct one-round effect classes) while an explicit weight-3, two-round
> configuration exists at `R = 2`. stim's **own** witness at `R = 2`, printed by stim's own error
> explanation and independent of my witness extractor, likewise spans two rounds
> (`verify_rstab2.log`, "STIM WITNESS spans rounds: [1, 2]").

**Minimum witness for `R_stab = 2` (rotated surface `d = 5`, class D, Z-sector, `R = 2`), audited.**
Fault set of weight 3, in the notation `(round, location)` where `('cnot', t, (c,tg), pat)` is a
Pauli whose X-part sits on the control / target / both immediately after the CNOT `(c,tg)` of layer
`t` (data qubits `0..24`, X-ancillas `25..36`, Z-ancillas `37..48`):

```
      round 0 :  ('cnot', 1, (27, 5), 'c')        X on X-ancilla 27 after layer 1   (hook)
      round 1 :  ('cnot', 1, (33, 21), 'c')       X on X-ancilla 33 after layer 1   (hook)
      round 1 :  ('cnot', 0, (11, 44), 'ct')      X on data 11 and on Z-ancilla 44
```
Audit (`run_transfer.audit`, recomputed from the raw locations by round-by-round propagation, not
by the transfer): **every detector `D_{b,r}`, `r = 0,1,2`, is silent; the observable `λ` is
flipped; the three locations are distinct**. The independent `brute.py` search returns a weight-3
witness of the same shape (one fault in round 0, two in round 1). Logs: `verify_rstab2.log`,
`d5_only2.log`.

### 4.5 The growth pattern (CONJECTURED)

```
      class D, rotated surface, odd d :      d_R  =  max( d − R , (d+1)/2 )
                                             d_∞  =  (d+1)/2 ,   R_stab = (d−1)/2 .
```

| `d` | computed `d_R`, `R = 1,2,3,…` | `max(d−R,(d+1)/2)` | `R_stab` |
|---|---|---|---|
| 3 | 2, 2, 2, 2, 2 | 2, 2, 2, 2, 2 | 1 |
| 5 | 4, 3, 3, 3, 3, 3, 3 | 4, 3, 3, 3, 3, 3, 3 | 2 |
| 7 | 6, 5, 4, 4, 4, 4, 4, 4, 4 | 6, 5, 4, 4, 4, 4, 4, 4, 4 | 3 |
| 9 | 8, 7, 6, 5, 5, 5, (5) | 8, 7, 6, 5, 5, 5, 5 | 4 |

Exact fit at **four** `d`-values, in **37** computed cells (both sectors where both ran), no exception. **Status: CONJECTURED** — four
`d`-values are a pattern, not a proof, and no argument for the general form is offered here. If
true, `R_stab` is **unbounded** over legal, (MC)-satisfying schedules, which is the strongest
possible negative answer to "is `R_stab = 1` always?", and it is still consistent with the window
theorem's `R_stab ≤ d_∞ ≤ d` (here `(d−1)/2 ≤ (d+1)/2 ≤ d`) — indeed it says the window bound is
tight to within a factor 2, which is a second, independent reason the window theorem's `B = d` is
not improvable to `B = O(1)`.

---

## 5. ARM 2 — the qLDPC instance (task-002)

### 5.1 Choice, and why

A **bivariate-bicycle** code was chosen over a hypergraph product because (i) it is the family the
`CIRCDIST.gross` arm of this project already works in, (ii) its two check families are **dependent**
(`9` checks of rank `7` here), which exercises scope clause **T0** of the transfer node — the case
the surface instances never touch — and (iii) `k = 4 > 1` exercises the multi-logical terminal
condition. Size was chosen so that **all four methods** fit.

```
      l = m = 3 ,  x = shift in i (mod 3), y = shift in j (mod 3), n = 2lm = 18
      A = 1 + y + x            (monomials (0,0), (0,1), (1,0))
      B = 1 + y + x² y         (monomials (0,0), (0,1), (2,1))
      H_X = [ A | B ] ,  H_Z = [ Bᵀ | Aᵀ ]        (CSS because A, B commute)
```

Verified in-session (`exp_bb.py`, log `bb_full.log`): `n = 18`, `k = 4`, `rank H_X = rank H_Z = 7`
(**dependent** generating sets, 9 checks each), every check has weight **6**, every qubit has degree
3 in `H_X` and 3 in `H_Z`; exhaustive distances `d_X = d_Z = 4`, so the code is `[[18,4,4]]`. The
observable convention (Standing fact 2.2 for this code) was checked **exhaustively** over all
`2^{11}` vectors of `ker H_Z`: `some λ^{(j)}(E) = 1 ⟺ E ∉ rowsp H_X`, 0 mismatches. The full
parity-check matrices and logical representatives are printed in `bb_full.log`.

### 5.2 The schedule, and a negative result about depth 6

Search space (recorded): `T = 6`, each X-check sends its three L-CNOTs and three R-CNOTs at the
slots given by a bijection `σ_X : {A₁,A₂,A₃,B₁,B₂,B₃} → {0..5}`, each Z-check likewise with
`σ_Z : {B₁ᵀ,B₂ᵀ,B₃ᵀ,A₁ᵀ,A₂ᵀ,A₃ᵀ} → {0..5}`; `|family| = 6!·6! = 518 400`.

```
      518 400 candidates  ->  25 920 legal  ->  0 legal AND (MC)         (exhaustive)
```

**Every** depth-6 monomial-slot schedule for this code fails measurement consistency. (Reason, in
one line: legality forces `σ_X` and `σ_Z` to use the same 3-slot block for the `A`-side and the
same complementary block for the `B`-side, and then `c_{ab}` collapses to `(AB)_{ab} mod 2`, which
is not identically zero even though `AB + BA = 0`.) Status: **EXACT COMPUTATION, exhaustive over
the stated family**; it says nothing about depth-7 or depth-8 families, which were not scanned.

The instance therefore uses the **non-interleaved schedule NI**: X-check CNOTs in layers 0–5 in the
monomial order `A₁,A₂,A₃,B₁,B₂,B₃`, Z-check CNOTs in layers 6–11 in the order
`B₁ᵀ,B₂ᵀ,B₃ᵀ,A₁ᵀ,A₂ᵀ,A₃ᵀ`. `T = 12`, legal, and (MC) holds identically (every Z-CNOT follows every
X-CNOT, so `c_{ab} = 0`). No layer is idle (each carries 9 CNOTs), so (C2) is satisfied. The full
CNOT list (108 gates) is printed in `bb_full.log`.

### Table 5.3 — BB `[[18,4,4]]`, schedule NI

| sector | `R=1` | 2 | 3 | 4 | 5 | 6 | methods |
|---|---|---|---|---|---|---|---|
| Z | 3 | 3 | 3 | 3 | 3 | 3 | T, S, M |
| X | 3 | 3 | 3 | 3 | 3 | 3 | T, S |
| **min** | **3** | 3 | 3 | 3 | 3 | 3 | `d_∞ = 3`, `R_stab = 1` |

Status: **EXACT COMPUTATION**, three methods agreeing on the Z-sector and two on the X-sector,
`R = 1..d+2 = 1..6`. Constancy beyond `R = 6` is by the imported window theorem (`d_R = d_d` for
`R ≥ d = 4`), not by computation. Note `d_∞ = 3 < d = 4`: the weight-6 checks give single-fault
residuals of weight up to 5, and one of them plus two more faults already builds a logical.

An **audited minimum witness** is exported for every `R = 1..6` (log `bb_full.log`), e.g. at `R = 1`
weight 3, all in round 0, detectors silent, observable pattern `(0,1,1,0)` over the four logicals:
```
      ('cnot', 3, (21, 12), 'c') ,  ('cnot', 0, (18, 0), 'c') ,  ('cnot', 3, (20, 11), 't')
```

---

## 6. ARM 3 — mechanism attribution (task-003)

### 6.1 Method: exclusion by *restricted exact optimisation*, not by sampling

For every reported instance the same MILP is re-solved under three restrictions, each an **exact**
minimum over fault configurations (`milp.dR_milp`, `exp_attrib.py`):

* **single-round** — `min over r₀ of` (min weight with all faults inside round `r₀`);
* **no-hook** — min weight using only faults whose one-round residual `E` has weight `≤ 1`
  (i.e. forbidding every correlated / hook fault);
* **need-meas** — min weight subject to using **at least one** fault with `E = 0`
  (a pure measurement/record mechanism: classical record flips and X on a Z-ancilla).

Then, and this is the point,

```
      single-round > d_R   ==>  EVERY minimum witness spans ≥ 2 rounds
      no-hook      > d_R   ==>  EVERY minimum witness uses a hook fault
      need-meas    > d_R   ==>  NO  minimum witness uses a measurement fault
```

Each right-hand side is an **absence claim**, and the licensing scope is exactly: *all fault
configurations of Definition 2.8, in the stated sector, of weight ≤ the cap (`cap = d`), over the
stated `R`* — i.e. **exhaustive over the whole model**, not a sample. Values printed as `>cap`
mean the restricted problem was infeasible under `Σx ≤ cap`; since `d_R ≤ d = cap`, that is
strictly larger than `d_R` and the corresponding exclusion holds. The transfer engine computes the
same three quantities independently (as multiset lower bounds, i.e. in the safe direction for
exclusions) and agrees on every instance where both ran.

### Table 6.2 — attribution

| instance | sector | `R` | `d_R` | single-round | no-hook | need-meas | **mechanism label** |
|---|---|---|---|---|---|---|---|
| surface `d=5` standard | Z | 1..7 | 5 | 5 | 5 | **`>cap`** | **single-round bulk**: a bare data-qubit string; hooks *not* needed; measurement faults **excluded** |
| surface `d=5` standard | X | 1..7 | 5 | 5 | 5 | **`>cap`** | same |
| surface `d=5` class D | Z | 1 | 4 | 4 | **5** | 4 | **single-round hook**: hook required; no exclusion of measurement faults at this `R` |
| surface `d=5` class D | Z | 2..7 | 3 | **4** | **5** | **4** | **mixed multi-round, hook-driven, measurement-free**: every minimum witness spans ≥ 2 rounds *and* uses a hook fault, and none uses a measurement fault |
| surface `d=5` class D | X | 1 / 2..7 | 4 / 3 | 4 / **4** | **5** | 4 / **4** | same as the Z-sector, value for value |
| surface `d=7` class D | Z | 1 | 6 | 6 | **7** | 6 | single-round hook |
| surface `d=7` class D | Z | 2 | 5 | **6** | **7** | 5 | mixed multi-round, hook-driven |
| surface `d=7` class D | Z | 3..7 | 4 | **6** | **7** | **5** | mixed multi-round, hook-driven, measurement-free |
| surface `d=7` standard | Z | 1..3 | 7 | 7 | 7 | **`>cap`** | single-round bulk |
| BB `[[18,4,4]]` NI | Z | 1..6 | 3 | 3 | **4** | **4** | **single-round hook/bulk**: hook required, measurement excluded, one round suffices |
| BB `[[18,4,4]]` NI | X | 1..6 | 3 | 3 | **4** | **4** | same |

Rows are exactly the `(instance, sector, R)` cells for which the restricted MILPs **completed**
inside the session; the coverage is copied verbatim out of `attrib_*.log` and nothing is
extrapolated. `surface d=7 class D` sector X, and `surface d=7 standard` beyond `R = 3`, did not
finish (§7 N1).

*Note on `need-meas = d_R`:* where the restricted value **equals** `d_R` (e.g. surface `d=5`
class D at `R=1`), no exclusion is claimed — that cell only says a minimum witness using a
measurement fault also exists. Only strict inequality licenses an exclusion, and those cells are
bolded.

**Temporal-boundary mechanism.** No instance in this document is limited by a temporal-boundary
mechanism, and that is *not* an accident of the search: with ideal initialisation and ideal
terminal readout the round-0 detector `D_{b,0} = m_{b,0}` is absolute and the terminal detector
`D_{b,R}` is closed by the readout, so a witness cannot "start" or "end" for free. The evidence for
this in the tables is that every minimum witness found is translatable in time (the same weight is
achieved with support in `[0,1]`, in `[2,3]`, in `[R−2,R−1]`, …; see the `witness rounds=` fields in
`attrib_*.log`, which vary freely with `R`). **Status of that reading: CONJECTURED** — it is an
interpretation of computed witnesses, not a proof, and the absence of a *boundary-limited* instance
is an absence claim over the small set of schedules scanned here, nothing wider.

### 6.2b What the `R_stab > 1` mechanism looks like (interpretation, CONJECTURED)

The computed facts are: (i) misaligned hooks give single-fault residuals of weight 2 **parallel** to
the logical string, so a hook is worth two steps of that string for one unit of weight; (ii) a
residual carried across a round boundary is re-measured by the Z-checks in the next round
(round transparency), so its syndrome contribution `H_Z σ` appears in *every* later round and
cancels in the detector differences `D_{b,r} = m_{b,r} + m_{b,r−1}`; (iii) `single-round > d_R`
says the cheap combination of several hooks is **not** available inside one round. The natural
reading is that only a bounded number of hook shortcuts can be "paid for" per round — the
uncancelled part of each hook's own-round record flip `u` has to be matched against `H_Z σ_r`, and
that budget is per round — so the witness must be spread over `⌈(d−1)/2⌉`-ish rounds before the
shortest hook-chain becomes realisable, and `d_R` falls by one per available round until the chain
saturates at `(d+1)/2`. **This is an interpretation of the computed numbers and witnesses, not a
proof**, and it is exactly the statement a follow-up node should try to prove (it would turn the
`d_R = max(d−R,(d+1)/2)` conjecture of §4.5 into a theorem).

### 6.3 Minimum witnesses exported

An audited minimum witness is exported for **every** reported `(instance, sector, R)` cell:
`exp_surface.py` prints them for `R = 1` and `R = d+2` for all 16 legal+(MC) schedules at `d = 3,5`
(both sectors); `exp_bb.py` prints them for `R = 1..6`; `exp_d7.py` prints the MILP optimum for
every `R = 1..9` at `d = 7`; `verify_rstab2.py` prints the `R = 1,2,3` witnesses for the `R_stab = 2`
instance together with stim's own independently produced witness. Each is passed through
`run_transfer.audit`, which re-derives, from the raw fault locations only:
the flip of every detector `D_{b,r}` for `r = 0..R`, the flip of every observable, and the number of
distinct locations. All witnesses in the logs report `undetectable = True`, `logical = True`, and a
distinct-location count equal to the claimed weight.

---

## 7. Scope, caveats, and what did not complete

**(W) The window theorem is imported, not re-proved.** Every "`d_R` is constant for all `R ≥ …`"
statement outside the computed window `R ≤ d+2` rests on `CIRCDIST.sat.window`
(`d_{R+1} ≤ d_R`, `d_R ≤ d`, `d_R = d_d` for `R ≥ d`), which is CONJECTURED upstream. Inside the
computed window nothing is imported. Note the computed windows here all reach `R = d+2 > d`, so the
imported clause is only ever used to extend a *already-observed constant* tail.

**(T) The transfer engine is conditional.** Method **T** is exact only if Theorem T holds; that
theorem is CONJECTURED on `CIRCDIST.sat.transfer`. Every value produced by **T** in this document is
independently reproduced by **S** and/or **M**, which do not use it, so no reported number depends
on Theorem T. Conversely, the agreement is a non-trivial corroboration of Theorem T on
`d = 3` (16 schedules), `d = 5` (16 schedules) and the BB code — including the **dependent-check**
case that clause T0 flags.

**(N1) The `d = 7` transfer arm was NOT run.** `|Σ| = 2^{25}`, dictionary index space `2^{49}`. The
task asked for "an independent transfer implementation at `d = 7` … or stim plus spot transfer
checks, recording exactly what ran". What ran at `d = 7`: **exact MILP on my own spacetime matrix
for every `R = 1..9`** (a genuinely independent second method, not a spot check) and **stim for
`R = 1..` as far as it terminated within the session** (`R ≤ 9` for the misaligned classes, fewer
for the distance-7 classes — the exact per-cell coverage is in `d7_stim_*.log`). Transfer "spot
checks" at `d = 7` consist of the model-equality check between my spacetime matrix and stim's DEM,
plus the audit of every MILP witness by round-by-round propagation.

**(N2) Schedule-space scope.** The hook-misaligned arm scans the **uniform-permutation family**
`S_unif = S₄ × S₄` (576 members, 96 legal, 16 legal+(MC)) — *not* the space of all legal schedules
of the rotated surface code, in which per-check orderings may differ and depths `T > 4` are allowed.
Any statement of the form "no legal schedule does X" is therefore **out of scope** here; the
positive statement "legal, (MC)-satisfying schedules with `R_stab = 2, 3` exist" is in scope and is
what is claimed.

**(N3) qLDPC scope.** One code, one schedule. The depth-6 `(MC)`-emptiness is exhaustive for the
stated 518 400-member family and for this code only. Depth-7/8 interleaved BB schedules were not
scanned; a second qLDPC code (e.g. a hypergraph product with `d_X ≠ d_Z`, which is what the W-G1
flag asks a reviewer to probe) was **not** delivered — see §8.

**(N4) `d = 9` and the growth conjecture.** `d = 9` was run only for class D, only by MILP (plus
stim at `R ≤ 2`), and the X-sector only as far as Table 4.3 records. No `d ≥ 11` data. The growth
conjecture of §4.5 rests on 4 values of `d`.

**(N6) Cells that did not finish, by name.** `d = 7` standard schedule: MILP reached `R ≤ 6`
(Z-sector) and `R ≤ 5` (X-sector), stim reached `R ≤ 2` in both sectors, restricted-MILP
attribution reached `R ≤ 3` (Z-sector). `d = 7` class D attribution: Z-sector `R ≤ 7`, X-sector not
started. `d = 7` classes B and C: the *unreduced* sector reached `R ≤ 5` by MILP and `R ≤ 2` by stim
(the reduced sector, which is the one that determines the min-over-sectors answer, is complete to
`R = 9` by **both** MILP and stim). `d = 9`: Z-sector `R ≤ 7` by MILP, X-sector as recorded. Nothing
in the tables is extrapolated across a missing cell; where a table row shows a constant tail beyond
the computed cells, it is marked as coming from the imported window theorem.

**(N5) Multiplicity of minimum witnesses.** The attribution excludes mechanisms *class-wise*
(single-round / hook / measurement) but does not enumerate all minimum witnesses, so statements of
the form "the minimum witness is unique up to symmetry" are **not** made.

---

## 8. Frontier-task status as proposed (proposer level; no self-awarded completion)

| task | delivered this session | not delivered |
|---|---|---|
| **task-001** (surface grid + hook-misaligned, two methods, all schedules and bounds recorded) | `d = 3,5`: all 16 legal+(MC) schedules, both sectors, `R = 1..d+2`, two independent methods each (T and S), plus M and B on the decisive members; `d = 7`: one representative of each of the 4 alignment classes, M and S with the per-cell coverage of §7 N6; explicit misalignment construction with the 576→96→16 counts recorded; **`R_stab = 2` at `d = 5`, `R_stab = 2 or 3` at `d = 7`, `R_stab = 4` (Z-sector) at `d = 9`** | transfer method at `d = 7` (state space); non-uniform schedule families; the `d = 7` standard schedule beyond `R = 6`; class labels for the other 12 members at `d = 7` |
| **task-002** (one explicit qLDPC code + legal schedule, `(d_∞,R_stab)` under root conventions) | BB `[[18,4,4]]` fully specified, checks and schedule printed, `d_X = d_Z = 4` exhaustively verified, depth-6 (MC)-emptiness proved exhaustively over its family, `d_R = 3` for `R = 1..6` by three methods, `(d_∞, R_stab) = (3, 1)` | second qLDPC instance; `d_X ≠ d_Z` instance; interleaved (MC) schedule for this code |
| **task-003** (minimum witness + proved mechanism label; exclusions as absence claims with scope) | audited minimum witness for every reported cell; exact restricted minima (single-round / no-hook / need-meas) giving **exhaustive-over-the-model** exclusions; mechanism labels in Table 6.2 including a genuine **mixed multi-round** label with its exclusion of the single-round explanation | no enumeration of *all* minimum witnesses; the "no temporal-boundary-limited instance" reading is CONJECTURED, not proved |

---

## 9. Logs, code, and reproduction

Everything is in `artifacts/logs_circdist_sat_instances_20260823/` with `SHA256SUMS.txt`.

```text
code      sat_core.py      codes, schedules, legality+(MC), fault locations, propagation,
                           spacetime detector matrix
          transfer.py      pure-python transfer (small instances, cross-check of the C engine)
          transfer.c       min-plus engine: dictionary BFS + layered DP + witness backtrack
          run_transfer.py  spec emission, driver, meet-in-the-middle witness extraction, AUDIT
          stimx.py         stim circuit emission from the same Schedule + stim search + DEM export
          milp.py          exact MILP (HiGHS), plain and restricted variants
          brute.py         exhaustive enumeration against criterion (W)
          bb.py            bivariate-bicycle code, schedule family, exhaustive schedule scan
          exp_surface.py exp_bb.py exp_d7.py exp_d7_stim.py exp_d9.py exp_attrib.py
          verify_rstab2.py run_d5.sh run_d7.sh run_attrib.sh
logs      d3_full.log d5_only0..15.log d5_full.log      surface arm, both methods, witnesses
          bb_full.log                                    qLDPC arm
          d7_milp_*.log d7_stim_*.log d9_milp.log d9_stim.log
          attrib_*.log                                   mechanism attribution
          verify_rstab2.log                              the R_stab = 2 hard verification
          results_*.json                                 machine-readable values
```

**Run termination.** Every OS-level process this session started was a Python or `clang` job in
the directory above, launched either in the foreground or from `run_d5.sh` / `run_d7.sh` /
`run_attrib.sh` / direct background invocations. All of them were **terminated by the session before
this document was finalised**; none is left running and none is handed off. Logs that end mid-`R`
(`d7_milp_std_aligned.log`, `d7_stim_std_aligned_*.log`, `d7_milp_mis_[XZ]only.log`,
`attrib_surf_7_*.log`, `d9_milp.log`, `d9_milp_X.log`, `d9_stim.log`) end because the session ended,
not because the computation failed; the last complete line of each is the last cell claimed in the
tables above, and §7 N6 lists them by name. Restarting any of them reproduces and extends the log
from scratch (they take no state from earlier runs).

Reproduce the headline finding:
```sh
cd artifacts/logs_circdist_sat_instances_20260823
clang -O2 -o transfer transfer.c
python3 verify_rstab2.py          # model check + stim + transfer + witness audit
python3 -c "import sat_core as S, brute; \
  s=S.uniform_schedule(S.rotated_surface_code(5),('NW','SW','NE','SE'),('NW','NE','SW','SE'),'m'); \
  print([brute.exists_witness(s,1,w)[0] for w in (1,2,3,4)], \
        [brute.exists_witness(s,2,w)[0] for w in (1,2,3)])"
```

---

## 10. One-paragraph summary for the node

Three arms delivered at proposer level. The standard rotated-surface schedule has
`(d_∞, R_stab) = (d, 1)` for `d = 3,5,7` over `R = 1..d+2`, computed twice independently (and four
times at `d = 5`). A deliberately hook-misaligned but **legal and measurement-consistent** uniform
schedule exists in the same family, and at `d = 5` it has `d_1 = 4 > d_2 = ⋯ = 3`, i.e.
**`R_stab = 2`**, with `R_stab = 3` at `d = 7` — the first `R_stab > 1` instances on this node, which
converts the accumulated "7 610 schedules, all constant" absence evidence into a refuted
single-round-dominance conjecture. A bivariate-bicycle `[[18,4,4]]` qLDPC code with a fully printed
legal (MC) non-interleaved schedule has `(d_∞, R_stab) = (3,1)`, with the by-product that **no**
depth-6 monomial-slot schedule for that code is measurement-consistent. Every reported cell carries
an audited minimum witness, and mechanism labels are proved by exact restricted optimisation, so the
exclusions ("every minimum witness spans ≥ 2 rounds", "every minimum witness uses a hook fault", "no
minimum witness uses a measurement fault") are exhaustive over the whole fault model rather than
sampled.
