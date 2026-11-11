# CIRCDIST — stim cross-validation of the frozen model against a real compiler

Fresh Opus 5 cross-validation reviewer, adversarial stance, one budget-boxed session
(box = 1, no sub-agents). Commissioned to attack the standing campaign caveat:

> "shared model design is not independence — every implementation re-implements the frozen
> 公共定义 fault inventory (Def 1.8/2.8: which locations exist, which Paulis are available) and
> the ideal-terminal-readout boundary; a systematic mismatch between the frozen model and a real
> compiler would survive every check in the chain; NO stim cross-check exists anywhere."

**Headline: the frozen model survives contact with stim on every load-bearing instance tested
(5/5 targets MATCH, 0 MISMATCH), and the two most plausible forms of the feared systematic
mismatch are shown to be provably inert.** One campaign-level *bookkeeping* defect was found —
the caveat is literally false on one of the three nodes that carries it.

Logs: `artifacts/logs_circdist_stim_crossval_20260823/` (17 files, `SHA256SUMS.txt`).

---

## 0. FIX-2 process declaration

| item | declaration |
|---|---|
| processes launched | **all foreground, all exited before this report.** One `python3 -m venv`; one `pip install stim==1.16.0`; eight foreground `python3` script runs. |
| background / detached processes | **none.** No `&`, no `run_in_background`, no daemons, no servers. |
| stray-process check | `ps -eo pid,ppid,etime,command | grep -i "stimvenv\|xval\|t1_422\|t2_steane\|t3\|t4_transfer"` → **NONE** (run after the last script, before writing this file; recorded in this session's transcript). |
| verdict-bearing logs | secured under `artifacts/logs_circdist_stim_crossval_20260823/` with `SHA256SUMS.txt`. |
| canonical files modified | **none.** No node YAML, no `CIRCDIST_PROBLEMS.md`, no prior artifact was edited. This file and the logs directory are the only writes. |
| environment note | stim was **not present** in this environment; it was installed with `pip install stim==1.16.0` into a throwaway venv under the session scratchpad (`.../scratchpad/stimvenv`), **not** into the user's system Python and **not** into the repo. The repo's own prior session had already established `pip install stim` as project practice (`circdist_lift_d3gate_20260820.md` §9.5). Flagging it because installing a package is a network fetch, not a pure-compute step. |

---

## 1. Independence — what is and is not independent here

Honest accounting, because this is the whole point of the exercise.

**Independent of the campaign's implementations:**

1. **The fault space is stim's, not mine and not the campaign's.** I do not enumerate faults. I
   place stim noise channels and call `Circuit.detector_error_model()`; stim's own Pauli
   propagation and DEM extraction decide which faults exist and what each one does. Every number
   below is read off a stim DEM.
2. **Two distance extractors, of different provenance.** (a) my own exact GF(2)
   minimum-weight search over the DEM columns (weight 1 / 2 / 3 by meet-in-the-middle / 4 by
   pair-sum collision); (b) stim's own `search_for_undetectable_logical_errors`, C++,
   written by someone with no connection to this campaign. **They agreed on every single cell
   computed in this session — 0 disagreements.**
3. **The (MC) predicate was re-derived from scratch** (`xval.mc_violations`) from the physical
   argument (a Z-check's recorded bit is deterministic only if the back-propagation count is
   even), then tested against stim's determinism oracle: of 176 [[4,2,2]] schedules my predicate
   passed, stim refused **0**; of the 400 it rejected in the surface family, the class-D member
   under my first (wrong) layout was refused by stim exactly where my predicate said it would be.
4. **The rotated-surface layout was not taken on trust.** My first reconstruction disagreed with
   the record (24 legal, 0 (MC), against the published 96 → 16). Rather than adopt the campaign's
   code, I enumerated the 64 candidate layout conventions and asked which reproduces the
   published funnel. **Exactly one does** (§5), and it is the geometrically canonical
   half-plaquette reading. The published funnel acted as a fingerprint; the fit is
   over-determined (96 *and* 16, at d = 3 *and* d = 5, plus code distance = d).
5. **Codes are re-derived and re-validated** — CSS commutation, logical algebra, and exact code
   distance by coset search — not imported.

**NOT independent (the residual, and it is the caveat's actual core):**

6. **I read the frozen model before implementing it**, including §10.6 `stimgen.py`, the prior
   session's stim generator. My generator is a fresh file but it is not a *blind*
   re-implementation; where the frozen text is ambiguous I may have resolved the ambiguity the
   same way they did. This is the honest limit of a single-session cross-check.
7. **The translation 公共定义 → stim channels is itself a modelling choice** (§2). It is
   documented in full precisely so that a future mismatch can be localised to it. §6 attacks it
   directly.
8. **`d_eff` is imported, not recomputed** (Target 5 only). I compute `d_circ`; the `d_eff`
   values it is compared against come from the campaign records.

---

## 2. The translation convention, stated exactly

This is the load-bearing modelling decision. Frozen inventory (公共定义 lines 14–41, as restated
in `circdist_lift_d3gate_20260820.md` §1.3) on the left, stim on the right.

| 公共定义 fault location | Paulis | stim channel |
|---|---|---|
| ancilla, immediately after preparation | `X`,`Y`,`Z` | `DEPOLARIZE1(p)` on all ancillas after `RX`/`R` |
| immediately after a CNOT | 15 non-identity 2-qubit Paulis | `DEPOLARIZE2(p)` on each CX pair |
| any qubit (data or ancilla) idle at a time step | `X`,`Y`,`Z` | `DEPOLARIZE1(p)` on that step's idle set |
| recorded ancilla measurement outcome | classical flip | `MX(p)` / `M(p)` |
| data initialisation | **none** (ideal boundary) | noiseless `R` / `RX` on data |
| terminal transversal readout | **none** (ideal boundary) | noiseless `M` / `MX` on data |

`DEPOLARIZE1` gives exactly `{X,Y,Z}` and `DEPOLARIZE2` exactly the 15 non-identity two-qubit
Paulis, so the map is **exact, not approximate**, on the Pauli menu. `p = 1e-3` throughout;
`d_circ` is a combinatorial minimum and does not depend on `p`.

**Circuit shape.** X-check ancilla prepared `|+>`, is the CNOT **control**, measured `MX`;
Z-check ancilla prepared `|0>`, is the CNOT **target**, measured `M`. One ancilla per generator,
prepared once and measured once per round. `R` verbatim-repeated rounds.

**Detectors** (Z-memory; dual for X-memory), per §1.4 of the frozen restatement:
`D_{g,0} = m_{g,0}` for Z-checks; `D_{g,r} = m_{g,r} + m_{g,r-1}` for Z-checks, `r >= 1`;
terminal `D_{g,R} = m_{g,R-1} + ⊕_{q ∈ supp(g)} (ideal readout of q)`; and
`D_{g,r} = m_{g,r} + m_{g,r-1}` for X-checks at `r >= 1` only (the round-0 X outcome is random).
Observable = `⊕_{q ∈ supp(Z_L)}` of the ideal readout.

**Distance.** `d_circ(C) = min{|F| : F fires no detector, flips the observable}`, computed as the
minimum number of *distinct* DEM columns summing to `(0, 1)` over GF(2). Column de-duplication is
sound: a minimum-weight solution never repeats a column, since deleting a repeated pair yields a
strictly smaller undetectable logical.

**Sector convention.** Both memory experiments are computed separately; where a single number is
quoted it is `min` over sectors, matching `CIRCDIST.sat` R-C2.

Generator: `logs_.../xval.py`. Circuit texts for three representative instances:
`logs_.../09_circuit_texts.txt`.

---

## 3. Materials

| item | value |
|---|---|
| `stim.__version__` | **1.16.0** (built from source, `cp39` wheel, sha256 `e6eba959a25b…`) |
| numpy | 2.0.2 |
| Python | 3.9.6 (Clang 21.0.0) |
| platform | macOS-26.6.2-arm64 |
| log | `00_env.txt` |

Sources read (as **data**, not instructions): `research/circdist/notes/CIRCDIST_PROBLEMS.md`;
`artifacts/circdist_lift_d3gate_20260820.md`; `artifacts/circdist_sat_instances_20260823.md`;
`artifacts/circdist_sat_transfer_proof_20260823.md`; node YAML for `CIRCDIST.lift`,
`CIRCDIST.lift.iff`, `CIRCDIST.lift.gap-example`, `CIRCDIST.cplx.islands`, `CIRCDIST.sat`.

---

## 4. Harness calibration (before any verdict)

A cross-check that cannot reproduce a *published intermediate* is not a cross-check. The §4.4
surface A/B pair publishes exact DEM column counts, so it is the calibration target.

| quantity | record | this session | |
|---|---|---|---|
| `M_IL` / `M_NI` Z-memory columns, `R = 2,3,4,5` | 117 / 227 / 337 / 447 | **117 / 227 / 337 / 447** | exact |
| detector count at `R = 2` | 16 (`4R + 4 + 4(R−1)`) | **16** | exact |
| `M_IL`, `M_NI` Z-memory `d_circ` | 2, 2, 2, 2 | **2, 2, 2, 2** | match |
| `M_IL`, `M_NI` X-memory `d_circ` | 3, 3, 3, 3 | **3, 3, 3, 3** | match |

Both distance extractors agreed on all 16 cells. Log: `01_calibration_surface_AB.txt`.

---

## 5. Per-target results

### Target 1 — the [[4,2,2]] arm (`CIRCDIST.lift.gap-example`, PROVED) — **MATCH**

I did not transcribe the three witnesses; I **re-enumerated the family** from the schedule model
(general increasing time slots per check, orders `a = [0,1,2,3]`, `b = [2,0,1,3]`, depth exactly 7)
and let stim decide every `d_circ`.

| quantity | record | this session |
|---|---|---|
| legal depth-7 schedules | — | 445 |
| measurement-consistent | **176** | **176** |
| stim DEM refusals among those 176 | 0 implied | **0** |
| with `d_circ^Z = 2` | **3** | **3** |
| of those, gapping **both** sectors | **1** ("witness 1") | **1** |
| witness 1 slots | `a = [0,3,4,5]`, `b = [0,1,2,6]` | **identical**, and the full t-table reproduces §7 line for line |
| witness `d_circ`, `R = 2,3,4,5` | 2, 2, 2, 2 | **2, 2, 2, 2** (both extractors) |
| non-interleaved partners | `d_circ = 1` | **1, 1, 1, 1**, both sectors, both block orders |

`(d_Z, d_X)` histogram over the family: `{(1,1): 23, (1,2): 150, (2,1): 2, (2,2): 1}`. The node
caveat "witness 1 gaps BOTH sectors, witnesses 2–3 gap Z-memory only" is **independently
confirmed** — witnesses 2 and 3 return `d_X = 1`. Log: `02_target1_422.txt`.

### Target 2 — the Steane instance — **MATCH**

| schedule | sector | record `d_circ`, `R = 2..5` | this session | record columns | this session |
|---|---|---|---|---|---|
| `M_IL` (depth 8, interleaved) | Z | **3, 3, 3, 3** | **3, 3, 3, 3** | 149/285/421/557 | **149/285/421/557** |
| `M_IL` | X | 2, 2, 2, 2 | **2, 2, 2, 2** | — | 148/285/422/559 |
| `M_NI` (non-interleaved) | Z | 2, 2, 2, 2 | **2, 2, 2, 2** | — | 150/284/418/552 |
| `M_NI` | X | 2, 2, 2, 2 | **2, 2, 2, 2** | — | 144/276/408/540 |

Detector counts 12/18/24/30 reproduced exactly. The `d_eff = 2 → d_circ = 3` lift, and the A/B
contrast that isolates interleaving as its sole cause, both stand under stim.

*Scope note:* my `M_NI` is a depth-11 greedy block partner, not the record's depth-10 one — same
code, same within-check orders, non-interleaved, but not byte-identical. The A/B contrast is
reproduced; the specific depth-10 circuit is not. Log: `03_target2_steane.txt`.

### Target 3 — the `R_stab > 1` headline cell (`CIRCDIST.sat.instances`, CERTIFIED*) — **MATCH**

The discovery cell. Rotated surface `d = 5`, class D (`piX = NW,SW,NE,SE`; `piZ = NW,NE,SW,SE`).

My first reconstruction **failed** (24 legal / 0 (MC) against the published 96 / 16) because I
had the boundary weight-2 corner labels wrong. Rather than copy the campaign's code, I enumerated
64 layout conventions (interior parity × 4 boundary corner-readings × which sector owns
top/bottom) under three constraints — valid CSS code, code distance = `d`, funnel = 96 → 16 at
**both** `d = 3` and `d = 5`. **Exactly one convention survives**: interior parity 0 = Z,
X on top/bottom, and a weight-2 boundary check read as *half a virtual plaquette lying outside
the array* (top-boundary qubits are its SOUTH corners, bottom its NORTH, left its EAST, right its
WEST). This is the geometrically canonical reading, and the record's layout is thereby
**independently pinned, not assumed**.

| quantity | record | this session |
|---|---|---|
| funnel, `d = 3` and `d = 5` | 576 → 96 → 16 | **576 → 96 → 16** (both) |
| class D in the legal+(MC) set | yes | **yes** |
| `d = 5` weight-4 X-hooks | 8 of 8 vertical | **8 of 8 vertical** |
| `d = 5` weight-4 Z-hooks | horizontal | **8 of 8 horizontal** |
| **`d = 5` class D, `d_1`** | **4** | **4** (Z **4**, X **4**) |
| **`d = 5` class D, `d_2`** | **3** | **3** (Z **3**, X **3**) |
| min-over-sectors | `d_1 = 4`, `d_2 = 3`, `R_stab = 2` | **`d_1 = 4`, `d_2 = 3`, `R_stab = 2`** |
| `d = 3` class D | 2 at every `R` (`R_stab = 1`) | **2, 2, 2** |

**`R_stab > 1` is confirmed by stim, in both sectors, at the cell the campaign calls the
discovery.** Columns 77 (`R = 1`) / 421 (`R = 2`); both extractors agreed.
Logs: `06_target3_layout_search.txt`, `07_target3_headline_d5_classD.txt`
(and `05_..._FIRST_ATTEMPT_wrong_layout_superseded.txt`, retained deliberately).

### Target 4 — the transfer `d = 3` table (`CIRCDIST.sat.transfer`) — **MATCH**

| instance | record Z `d_R` (R=1,2,3) | this session | record X | this session |
|---|---|---|---|---|
| `surface913/ilv0` | [3,3,3] | **[3,3,3]** | [2,2,2] | **[2,2,2]** |
| `surface913/ilv1` | [2,2,2] | **[2,2,2]** | [3,3,3] | **[3,3,3]** |
| `surface913/blkX` | [3,3,3] | **[3,3,3]** | [2,2,2] | **[2,2,2]** |
| `surface913/blkZ` | [3,3,3] | **[3,3,3]** | [2,2,2] | **[2,2,2]** |

24/24 values, 0 disagreements.

**Bonus, unrequested:** I ran **all 16** legal+(MC) members at `d = 3` *and* `d = 5`, which tests
the record's structural claim (Table 4.2) that they fall into 4 classes of 4 with identical `d_R`
sequences. They do — class sizes `[4,4,4,4]` at both `d`, and at `d = 5` the four signatures are
`Z[5,5]/X[5,5]`, `Z[5,5]/X[3,3]`, `Z[3,3]/X[5,5]`, `Z[4,3]/X[4,3]`, i.e. **the whole of Table 4.2's
`d = 5` column, classes A/B/C/D, reproduced under stim**, not just class D.
Log: `08_target4_transfer_and_target5.txt`.

### Target 5 — LIFT' repair-0 spot check — **MATCH**

Non-interleaved schedules are the repair-0 case, where the criterion (and 公共定义's
"非交错电路已知满足 `d_circ = d_eff`") predicts equality.

| instance (non-interleaved) | sector | `d_eff` (imported) | stim `d_circ`, `R = 1..4` | |
|---|---|---|---|---|
| Steane `M_NI` | Z / X | 2 / 2 | **[2,2,2,2] / [2,2,2,2]** | match |
| surface `blkX` | Z / X | 3 / 2 | **[3,3,3,3] / [2,2,2,2]** | match |
| `[[4,2,2]]` block | Z / X | 1 / 1 | **[1,1,1,1] / [1,1,1,1]** | match |

Weakest target of the five: `d_eff` is imported rather than recomputed, so this confirms
`d_circ = imported d_eff`, not `d_circ = independently-computed d_eff`.

---

## 6. The adversarial probe — is the feared systematic mismatch real?

Reproducing the campaign's numbers under *their* modelling choices does not by itself refute the
caveat, which is about the choices themselves. So I perturbed the translation in the two most
plausible directions a real compiler diverges, and re-derived everything.

* **Convention B ("compiler")** — identical circuit, but data qubits *also* idle-depolarize during
  the ancilla **reset** layer and the ancilla **measurement** layer. These are locations a real
  compiler unquestionably has, and which the frozen model's "any time step in which it is not in a
  gate" arguably omits (it counts idle slots only *within* the schedule).
* **Convention C ("noisy readout")** — frozen model plus a **noisy terminal readout**, deliberately
  breaking the stated ideal boundary. A control.

Instruction counts are blind here because stim *fuses* adjacent identical channels, so I counted
noise **targets** and derived the elementary-fault totals:

| instance | convention | elementary faults | **distinct DEM columns** | `d_circ` |
|---|---|---|---|---|
| Steane `M_IL`, Z, `R=2` | frozen | 1104 | **149** | 3 |
| | compiler | **1188** (+84) | **149** | **3** |
| | noisy readout | **1111** (+7) | **149** | **3** |
| surface `d=5` class D, Z, `R=2` | frozen | 2808 | **421** | 3 |
| | compiler | **3108** (+300) | **421** | **3** |
| | noisy readout | **2833** (+25) | **421** | **3** |

Also run on `[[4,2,2]]` witness 1 and Steane `M_NI`, both sectors, `R = 2,3`, and on the `d = 5`
discovery cell at `R = 1` and `2` — **every value unchanged**.

**This is the substantive finding.** Adding 300 genuine elementary faults produces **zero** new
DEM columns. The added locations are *redundant*, not missing: a data idle error during the reset
or measurement layer is already realised by an existing column, and a terminal readout flip on
qubit `q` is exactly the column of a pre-readout `X` on `q`, which the frozen inventory already
contains. So for these instances:

1. the frozen fault inventory is **column-complete** with respect to the reset/measure idle
   locations it appears to omit; and
2. **the ideal-terminal-readout boundary is not load-bearing for `d_circ`** — the very boundary
   the caveat names as a risk cannot move these numbers.

Log: `04_probe_integrity.txt`.

---

## 7. Defect found: the caveat is literally false on one node

Adversarial duty, reported whether or not it was asked for.

`CIRCDIST.lift.yaml` line 33 carries:

> "Shared model design is not independence (standing campaign limitation): **no stim cross-check
> exists anywhere in this subtree.**"

But `CIRCDIST.lift.gap-example.yaml` — **a child in exactly that subtree** — records at line 71
`"stim 1.16.0 cross-validation"` as the scope of its run evidence, and at line 121 that the
wave-11 re-adjudication rested on "the reviewer's own propagator + **own stim build, 9936 DEM
columns, 0 disagreements**". `circdist_sat_instances_20260823.md` line 109 likewise lists
**stim 1.16.0** `search_for_undetectable_logical_errors` as method **S**, one of four.

So the parent's caveat contradicts its own child's evidence register. The sibling caveats on
`CIRCDIST.lift.iff` ("...in this **node's verification chain**") and `CIRCDIST.cplx.islands`
("...in this **node's history**") are **node-scoped and were accurate as written**; only the
`CIRCDIST.lift` subtree-scoped one over-reached. This is a bookkeeping defect, not a
mathematical one — but it is the kind that makes a caveat set untrustworthy, and it was found
before a single circuit was built.

---

## 8. Verdict table

| # | target | node | verdict | numbers |
|---|---|---|---|---|
| 0 | harness calibration (§4.4 A/B) | — | **MATCH** | columns 117/227/337/447 exact; `d` 2/3 |
| 1 | `[[4,2,2]]` three depth-7 witnesses + partners | `CIRCDIST.lift.gap-example` | **MATCH** | 176 (MC); 3 with `d_circ=2`; 1 both-sector; `d_circ = 2` at `R=2..5`; partners `1` |
| 2 | Steane depth-8 lift | `CIRCDIST.lift.gap-example` | **MATCH** | `M_IL` Z `3,3,3,3` (149/285/421/557 cols); X `2`; `M_NI` `2` |
| 3 | `d=5` class-D `R_stab>1` cell | `CIRCDIST.sat.instances` | **MATCH** | `d_1 = 4`, `d_2 = 3`, both sectors; `R_stab = 2`; funnel 96→16 |
| 4 | transfer `d=3` table | `CIRCDIST.sat.transfer` | **MATCH** | 24/24 values; plus all-16 class structure `[4,4,4,4]` at `d=3,5` |
| 5 | LIFT' repair-0 spot check | `CIRCDIST.lift.iff` | **MATCH** | `d_circ = d_eff` on 6 sector-instances |
| — | translation-perturbation probe | all | **NO MISMATCH FOUND** | +300 faults → +0 columns → `d` unchanged |
| — | caveat bookkeeping | `CIRCDIST.lift` | **DEFECT** | subtree caveat contradicts child's stim record |

**5/5 targets MATCH. 0 MISMATCH. 0 disagreements between the two distance extractors across every
cell computed this session.**

---

## 9. Overall adjudication of the shared-model caveat

**The frozen model survives contact with a real compiler on the load-bearing instances.** stim —
which knows nothing about 公共定义 — was handed the circuits and produced the campaign's numbers,
every one of them, including the discovery cell. Moreover the caveat's two named risk surfaces
(the fault inventory's location set, and the ideal-terminal-readout boundary) were perturbed
directly and shown to be **inert**: the perturbations add hundreds of real faults and zero DEM
columns.

The caveat should therefore be **DOWNGRADED, not deleted**. What remains genuinely untested:

* the **whole `CIRCDIST.gross` arm** (`[[144,12,12]]`) — nothing here touches it;
* `CIRCDIST.cplx` **gadget/reduction** constructions, which are complexity-theoretic and were not
  circuit-built at all;
* `d >= 7` and `d = 9` cells (`R_stab = 3, 4`), the qLDPC `[[18,4,4]]` instance, and all `R > 5`;
* the **general lift criterion at `repair >= 2`** — Target 5 is repair-0 only;
* the deeper reading of the caveat: I read the frozen model before implementing it (§1.6), so a
  *shared misreading of the frozen text itself* remains possible in principle. What is now excluded
  is a mismatch between the frozen model **as the campaign implements it** and **stim's own fault
  semantics**.

### Licensed amendments — the dispatcher executes; I only license

**(A) `CIRCDIST.lift.yaml`, caveat at line 33 — LICENSED TO REPLACE (this one is also a factual
correction, not merely a downgrade):**

> 'Shared model design is not independence (standing campaign limitation): every independent
> implementation re-implements the frozen 公共定义 fault inventory, so a shared misreading of the
> frozen text would survive all of them. SPOT-VALIDATED AGAINST STIM 1.16.0
> (artifacts/circdist_stim_crossval_20260823.md, 2026-08-25): the [[4,2,2]] arm (176 (MC)
> schedules re-enumerated, 3 gap witnesses, 1 both-sector, d_circ = 2 at R = 2..5, partners 1)
> and the Steane arm (M_IL Z-memory d_circ = 3 at R = 2..5, 149/285/421/557 DEM columns exact;
> M_NI 2) reproduce under stim with 0 disagreements between two independent distance extractors;
> perturbing the fault inventory (data idle at the reset/measure layers, +84 to +300 elementary
> faults) and breaking the ideal-readout boundary (noisy terminal readout) changed 0 DEM columns
> and 0 distances. Systematic-mismatch risk is bounded to untested regions (gross arm, d >= 7,
> repair >= 2). The prior wording "no stim cross-check exists anywhere in this subtree" was
> FACTUALLY WRONG — CIRCDIST.lift.gap-example already recorded stim 1.16.0 cross-validation
> (its lines 71 and 121).'

**(B) `CIRCDIST.lift.iff.yaml`, caveat at lines 33–37 — LICENSED TO AMEND** (the node-scoped
claim was accurate; only the last clause changes):

> replace "— NO stim cross-check exists anywhere in this node's verification chain." with
> "— a stim cross-check now exists but is NARROW: artifacts/circdist_stim_crossval_20260823.md
> (stim 1.16.0) confirms d_circ = d_eff on six repair-0 (non-interleaved) sector-instances across
> [[4,2,2]], Steane and rotated surface, and separately shows the frozen inventory to be DEM-column-
> complete against reset/measure idle locations and against a noisy terminal readout. This is a
> REPAIR-0 SPOT CHECK ONLY: the criterion at repair >= 1 (the node's own load-bearing regime) has
> NO stim cross-check, and d_eff there was imported rather than recomputed."

**(C) `CIRCDIST.cplx.islands.yaml`, caveat at lines 62–66 — LICENSED TO AMEND ONLY the final
sentence**, and deliberately *weakly*, because nothing in this session built a cplx gadget:

> replace "NO stim cross-check exists anywhere in this node's history." with
> "NO stim cross-check exists anywhere in this node's history. The 2026-08-25 stim cross-validation
> (artifacts/circdist_stim_crossval_20260823.md) validated the SHARED 公共定义 fault menu and (M4)
> terminal boundary against stim 1.16.0 on the lift and sat arms — including a direct demonstration
> that the (M4) ideal-readout boundary is not load-bearing for d_circ — but built NO island gadget
> and NO reduction instance, so this node's own constructions remain stim-untouched."

**(D) `CIRCDIST.sat.yaml`, R-C1 (lines 18–20) — LICENSED TO APPEND** (do not weaken the
single-point-of-failure statement; it is correct):

> append: "PARTIALLY MITIGATED 2026-08-25 (artifacts/circdist_stim_crossval_20260823.md): stim
> 1.16.0 independently reproduces the headline R_stab > 1 cell (rotated surface d = 5, class D:
> d_1 = 4, d_2 = 3, both sectors, min-over-sectors R_stab = 2), the full transfer d = 3 table
> (24/24 values), and the Table 4.2 class structure at d = 3 and d = 5 (four classes of four, all
> four d = 5 signatures). The layout was NOT taken on trust: the published 576 -> 96 -> 16 funnel
> uniquely pins the boundary convention among 64 candidates. Still single-point at d >= 7, d = 9,
> the qLDPC instance, and every R beyond the computed stim window."

I do **not** license any change to `CIRCDIST.gross` caveats, to `CIRCDIST.lift.nonint`, or to any
completion level. Nothing here promotes anything.

---

## 10. Limitations

1. **Five targets, one session.** Everything outside §5 is untested. Coverage is narrow by design
   (stop-loss per target); breadth was traded for exactness on the load-bearing cells.
2. **I read the frozen model, including the prior `stimgen.py`, before implementing** (§1.6). Not
   a blind re-implementation. A shared *misreading of the frozen text* is not excluded.
3. **The translation of §2 is itself a modelling choice.** Documented in full so a future
   mismatch can be localised to it; §6 tests its two most plausible failure modes, not all of them.
4. **`d_eff` imported** in Target 5; the LIFT' check is `d_circ` vs *recorded* `d_eff`.
5. **Steane `M_NI` is my depth-11 greedy partner, not the record's depth-10 circuit.** Same code,
   orders and non-interleaving; not byte-identical.
6. **`R <= 5` everywhere** (`R <= 2` at `d = 5`). Tail behaviour and the window theorem are
   untouched; `R_stab = 2` is confirmed by `d_1 != d_2` plus `d_2 = d_infinity` **imported**.
7. **No `d >= 7`, no `d = 9`, no `[[144,12,12]]`, no qLDPC, no cplx gadget.**
8. **stim's DEM is not an oracle either.** It shares the *concept* of a spacetime fault model
   with the campaign. What it does not share is this campaign's code, its authors, or its
   conventions — which is the sense of independence claimed here, and no more.
9. **`p = 1e-3` fixed**; distances are combinatorial and `p`-independent, but no
   error-rate sweep was run to confirm no channel degenerated at that value.

---

*No canonical file was modified by this session. All verdict-bearing output is under
`artifacts/logs_circdist_stim_crossval_20260823/` with `SHA256SUMS.txt`.*
