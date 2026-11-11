# CIRCDIST.lift — the d = 3 gate (Opus 5 executor, proposer role)

**Date:** 2026-08-20 · **Node:** `CIRCDIST.lift` · **Frontier item:** the `d = 3` gap instance
proposed in `artifacts/circdist_lift_recon_20260820.md` §6.
**Session type:** one budget-boxed executor session under stop-loss. No sub-agents.
**Epistemic ceiling for this document: nothing here is labelled PROVED.** Every computational
result is **NUMERICAL** (exhaustive `F₂` enumeration, two independent implementations);
every structural statement is **CONJECTURED** with an explicit combinatorial derivation whose
gaps are named.

---

## 0. Executive summary

**Which pre-committed reading fired: (c) mixed — but the axis of the mixture is not the one
the recon anticipated.** The gate does not split by interleaving pattern within a fixed code;
it splits by **code geometry**, and the deciding invariant is
`|supp(X-check) ∩ supp(Z-check)|`.

1. **Rotated `d = 3` surface code → reading (b).** With hook-damaged within-check orders
   (`d_eff = 2`), **`d_circ = 2` for every legal, measurement-consistent schedule**, interleaved
   or not. Exhaustive: **26 570** schedules at depths 6, 7, 8 (23 902 at depth 8 alone, of which
   48 non-interleaved), all `d_circ = 2`, `R = 3`; the A/B pair re-checked at `R = 2,3,4,5`.
   The obstruction is characterised in §3 and holds for **all 2 304 within-check order choices**
   (exhaustive, §4.3).
2. **Steane `[[7,1,3]]` → reading (a), and within Steane also (c).** An explicit
   measurement-consistent **interleaved** depth-8 schedule has `d_eff = 2` and **`d_circ = 3`** —
   the completion gap fully repairs the hook damage — while the **non-interleaved schedule with
   identical within-check CNOT orders** has `d_circ = 2 = d_eff`. Stable for `R = 2,3,4,5`;
   reproduced exactly by `stim 1.16.0`. `g(C) = 1`. Holding code, within-check orders and depth
   fixed, **2 of the 16 measurement-consistent depth-8 schedules reach 3 and 14 stay at 2** — so
   the interleaving pattern alone decides, and §6 predicts which from one round of data.
3. **The load-bearing correction of this session: a validity constraint the round-1 recon
   missed.** An interleaved single-ancilla CSS schedule is a syndrome-extraction circuit **only
   if** for every X-check `a` and Z-check `b`,
   `#{ q ∈ supp(a) ∩ supp(b) : t(q→b) < t(a→q) }` is **even** (§2). Schedules violating it have
   non-deterministic detectors — `stim` refuses to build a detector error model for them. My
   first (unconstrained) scan produced spurious `d_circ = 3` results from exactly such circuits.
   **The round-1 recon's `[[4,2,2]]` interleaved circuit violates this constraint** (§7).
4. **But the recon's claim survives, repaired.** Among measurement-**consistent** `[[4,2,2]]`
   schedules with the recon's within-check orders, 3 of 176 at depth 7 and 26 of 769 at depth 8
   have `d_circ = 2 > d_eff = 1`. An explicit valid witness is given in §7, `stim`-confirmed for
   `R = 2..5`. So the recon's mechanism is real; only its circuit was not.
5. **The criterion the node is looking for, in its sharpest form found this session
   (CONJECTURED, §3).** A hook left by a fault on X-check ancilla `a` can carry non-zero
   *timelike voltage* on Z-check `b` **only if `|supp(a) ∩ supp(b)| ≥ 4`**. Overlap `≤ 2`
   forces `u ⊆ s` — every hook is a horizontal (spacelike) edge, the completion gap vanishes,
   and `d_circ = d_eff` for **every** schedule. This is why the surface code gives (b) and
   Steane (whose `X_i`/`Z_i` share their full weight-4 support) gives (a).
6. **Formula check.** The conjectured `d_circ = min_γ (|γ| + repair(γ))`, with `repair` computed
   from **one round only** via the group-ring criterion, **agreed with exhaustive weight-≤3
   enumeration on 5 129 of 5 129 schedules** across three codes (§6.3). Both sides are tabulated
   explicitly for four named schedules (Steane IL/NI, surface IL/NI) plus the `[[4,2,2]]` witness
   in §6.2. `repair = 1` occurs exactly where `d_circ > d_eff` and `repair = 0` exactly where
   `d_circ = d_eff`; no disagreement of any kind was observed.
7. **Cross-node consequence for `CIRCDIST.gross` (§8).** The gross code's X/Z check pairs
   overlap in **at most 2** qubits (exact computation: histogram `{0: 4536, 2: 648}`). Under the
   §3 criterion, **no hook in any measurement-consistent gross-code schedule can carry timelike
   voltage.** This is evidence *against* the existence of a distance-12 interleaved gross
   circuit, i.e. toward `D*_Gross = 11`. It is a lead, not a proof: §3 constrains single hooks,
   while the gross question concerns weight-11 effective logicals.

---

## 1. Model, stated precisely

Everything below uses exactly this model; deviations are the main reproducibility risk and are
flagged in §9.

### 1.1 Codes

| code | data | ancillas | checks | `Z_L` | `X_L` | `d` |
|---|---|---|---|---|---|---|
| rotated `[[9,1,3]]` surface | 9 (3×3 grid) | 8 | `X: {1,2,4,5},{3,4,6,7},{0,1},{7,8}` ; `Z: {0,1,3,4},{4,5,7,8},{2,5},{3,6}` | `Z₀Z₁Z₂` | `X₀X₃X₆` | 3 |
| Steane `[[7,1,3]]` | 7 | 6 | `X` and `Z` both `{3,4,5,6},{1,2,5,6},{0,2,4,6}` | `Z₀Z₁Z₂` | `X₀X₁X₂` | 3 |
| `[[4,2,2]]` (recon re-check) | 4 | 2 | `X: {0,1,2,3}` ; `Z: {0,1,2,3}` | `Z₀Z₂` | `X₀X₁` | 2 |

Grid indexing for the surface code:

```
0 1 2
3 4 5
6 7 8
```

Both `d = 3` codes were verified in code: all X/Z checks commute, the logicals commute with all
checks and anticommute with each other, and the minimum-weight non-trivial logical is 3 by
exhaustive search over supports.

### 1.2 Circuit

Single ancilla per stabilizer generator, prepared once and measured once per round. X-check
ancilla: prepared `|+⟩`, **control** of every CNOT to its data qubits, measured in X. Z-check
ancilla: prepared `|0⟩`, **target** of every CNOT from its data qubits, measured in Z. A
*schedule* `M` assigns a time step to each CNOT such that no qubit is in two two-qubit gates at
the same step (*legality*), and additionally satisfies the measurement-consistency constraint of
§2.

Memory experiment `C_R(M)`: **ideal** data initialisation (`|0⟩^n` for the Z-memory, `|+⟩^n` for
the X-memory), `R` identical rounds of `M`, **ideal** transversal final data readout.

### 1.3 Elementary fault model (the enumeration set)

`|F|` = number of elementary faults. One elementary fault is one of:

| location | fault | count per round |
|---|---|---|
| ancilla, immediately after preparation | `X`, `Y`, or `Z` | `3 × #checks` |
| immediately after a CNOT | one of the 15 non-identity two-qubit Paulis on (control, target) | `15 × #CNOTs` |
| any qubit (data **or** ancilla) at any time step in which it is not in a gate | `X`, `Y`, or `Z` | `3 ×` #idle slots |
| a recorded ancilla measurement outcome | classical bit flip | `#checks` |

Ancillas are idle-eligible at every step of the round (they are prepared at the start and
measured at the end of every round). Data initialisation and final readout carry no faults
(ideal boundary), per the 公共定义.

This is the "hook propagation" model: a fault's effect is obtained by forward `F₂` symplectic
propagation, `CNOT(c,t): x_t ← x_t + x_c, z_c ← z_c + z_t`, with ancilla error zeroed after each
round's measurement (reset).

### 1.4 Detectors and observable

Write `m_{g,r}` for the recorded outcome of check `g` in round `r` (`r = 0..R-1`). For a
**Z-memory** experiment:

- `D_{g,0} = m_{g,0}` for every Z-check `g` (deterministic, data in `|0⟩`);
- `D_{g,r} = m_{g,r} + m_{g,r-1}` for every Z-check `g`, `r ≥ 1`;
- terminal `D_{g,R} = m_{g,R-1} + ⊕_{q ∈ supp(g)} (ideal readout of q)` for every Z-check `g`;
- `D_{g,r} = m_{g,r} + m_{g,r-1}` for every X-check `g`, `r ≥ 1` (the round-0 X outcome is
  random, so it carries no detector, and there is no terminal X detector in a Z-basis readout).

Observable: `⊕_{q ∈ supp(Z_L)}` (ideal readout of `q`). Dual for the X-memory. Detector counts:
`4R + 4 + 4(R−1)` for the surface code (16 at `R = 2`), `3R + 3 + 3(R−1)` for Steane (12 at
`R = 2`) — matching the reported column tables.

`d_circ(C) = min{ |F| : F flips no detector and flips the observable }`. Both memory experiments
are computed separately and reported separately; the circuit's distance is the minimum of the
two, and §5.2 notes where they differ.

### 1.5 `d_eff`

`d_eff(M) = d_ext(E(M))`: `E(M)` is the set of terminal residual data errors of single faults
(computed by running one round with each single fault and reading off the data error at the end
of the round), and `d_ext` is the minimum **number of residuals** whose product has trivial
syndrome and non-trivial logical action. Verified numerically to depend only on the within-check
CNOT orders — the residual sets of every A/B pair below are printed and are identical.

### 1.6 Exhaustive search

Every fault is reduced to a DEM column `(detector bitmask, observable bit)`; identical columns
are de-duplicated (a minimum-weight solution never repeats a column, since deleting a repeated
pair yields a smaller undetectable logical). Then:

- weight 1: a column with empty detector set and observable 1;
- weight 2: two columns with equal detector masks and different observable bits;
- weight 3: meet-in-the-middle — hash all pairwise detector-mask sums, then look up each single
  column's mask.

Since `d_circ ≤ d = 3` always, finding no weight-≤2 solution and one weight-3 solution pins
`d_circ = 3` exactly.

---

## 2. The measurement-consistency constraint (the correction that drove the session)

**CONJECTURED 2.1 (validity of an interleaved single-ancilla CSS schedule).**
A schedule `M` yields deterministic detectors — i.e. is a syndrome-extraction circuit at all —
**iff** for every X-check `a` and every Z-check `b`,

```
    #{ q ∈ supp(a) ∩ supp(b) : t(q→b) < t(a→q) }   is even.                       (MC)
```

*Derivation.* Back-propagate the X-basis measurement of `a` through one round, processing gates
in reverse time order. `CNOT(a→q)` sends `X_a ↦ X_a X_q`; a subsequent (earlier-in-time)
`CNOT(q→b)` sends `X_q ↦ X_q X_b`. So `MX(a)`, expressed at the start of the round, is
`X_a · ∏_{q ∈ supp(a)} X_q · ∏_b X_b^{c_{ab}}` with
`c_{ab} = #{q ∈ supp(a)∩supp(b) : t(q→b) < t(a→q)} mod 2`. The Z-ancilla `b` starts every round
in `|0⟩`, which is **not** an `X_b` eigenstate, so a surviving `X_b` factor makes the X-check
outcome random relative to the data. Dually, `M(b)` picks up `Z_a` once for each shared `q` with
the opposite ordering; since `|supp(a)∩supp(b)|` is even (CSS commutation), the two conditions
coincide. ∎(sketch)

**Non-interleaved schedules satisfy (MC) automatically** (all counts are 0), which is one reason
the phenomenon has no analogue there.

**NUMERICAL 2.2 (validity predicate vs `stim`).** The predicate (MC) was compared against
`stim.Circuit.detector_error_model()` — which raises `ValueError: The circuit contains
non-deterministic detectors` exactly when the circuit is invalid — on 56 surface-code schedules
at depth 5 across three Z-order families: **56 agreements, 0 disagreements.** Every schedule used
anywhere else in this report additionally had its `stim` DEM built successfully, which re-checks
(MC) on each.

**Why this matters, concretely.** My first scan enumerated only *legal* schedules and found
"`d_circ = 3`" for 20/20 depth-5 and 289/289 depth-6 surface-code schedules under one order
choice. **Every one of those was an invalid circuit.** After imposing (MC), 0 of those 20 and 0
of those 289 remain, and the surviving schedules all give `d_circ = 2`. Any future session
computing circuit distance for interleaved schedules must impose (MC) or its numbers are
meaningless.

---

## 3. The hook-voltage criterion (the structural result)

Fix an X-check ancilla `a` with CNOT order `q₁,…,q_w`. A fault putting `X` on `a` between its
`j`-th and `(j+1)`-th CNOT leaves the *hook* residual `S = {q_{j+1},…,q_w}` (the suffix), with
prefix `P = {q₁,…,q_j}`. For a Z-check `b`, with `c_q = [t(q→b) > t(a→q)]`:

```
    s_b(S) = |supp(b) ∩ S|  mod 2                    (terminal syndrome)
    u_b(S) = Σ_{q ∈ supp(b) ∩ S} c_q  mod 2          (this-round outcome flips)
```

In the recon's edge taxonomy the fault is *horizontal* iff `u ∈ {0, s}` (voltage 0) and carries
timelike voltage otherwise. Adding `s_b` to `u_b` and applying (MC) to the pair `(a,b)`:

```
    u_b(S) + s_b(S)  =  #{ q ∈ supp(b) ∩ P : t(q→b) < t(a→q) }   mod 2.           (*)
```

**CONJECTURED 3.1 (overlap-4 necessary condition).** In a measurement-consistent schedule, a
hook of X-check `a` carries non-zero voltage on Z-check `b` — i.e. `u_b = 1` while `s_b = 0` —
only if `|supp(a) ∩ supp(b)| ≥ 4`.

*Derivation.* `s_b = 0` with `u_b = 1` forces `supp(b) ∩ S ≠ ∅` and `|supp(b) ∩ S|` even, hence
`|supp(b) ∩ S| ≥ 2`. And `u_b + s_b = 1` with (*) forces `supp(b) ∩ P ≠ ∅`, hence
`|supp(b) ∩ P| ≥ 1`. So `|supp(a) ∩ supp(b)| ≥ 3`, and by CSS commutation it is even, so `≥ 4`. ∎

**CONJECTURED 3.2 (containment lemma).** If every X/Z check pair of the code overlaps in at most
2 qubits, then in every measurement-consistent schedule every suffix residual satisfies
`u ⊆ s` (componentwise `u_b ≤ s_b`). *Same case analysis:* `|supp(b)∩S| ∈ {0,1,2}`; for 0 and 2
(MC) gives `u_b = 0 = s_b`; for 1, `s_b = 1` and `u_b` is unconstrained but `≤ 1`. ∎

Bare data errors always satisfy `u ⊆ s` (for every `b ∋ q`, `s_b = 1`).

**NUMERICAL 3.3 (containment lemma, verified).** Over all `(residual, achievable u)` pairs of all
single faults, in measurement-consistent schedules:

| code | schedule family | schedules | `(E, u)` pairs | `u ⊆ s` holds | violations |
|---|---|---|---|---|---|
| rotated surface | general slots, depth 6 | 3 000 (capped) | 87 000 | 87 000 | **0** |
| Steane (order set A) | general slots, depth 8 | 2 152 (exhaustive) | 60 256 | 60 256 | **0** |
| `[[4,2,2]]` | general slots, depth 7 | 176 (exhaustive) | 1 936 | 1 933 | **3** |

The 3 `[[4,2,2]]` violations are exactly the 3 schedules with `d_circ > d_eff`, and the violating
object is exactly the recon's mechanism: residual `E = {2,3}` with `s = 0`, `u = 1` — a pure
**vertical** edge with voltage 1. The correspondence *"containment fails ⟺ the gap opens"* held
on every case examined.

---

## 4. Arm 1 — rotated `d = 3` surface code: reading (b)

### 4.1 Hook damage

Within-check orders (fixed for the whole arm):

```
XA = [2,5,1,4]   XB = [3,4,6,7]   XC = [0,1]   XD = [7,8]
ZA = [0,3,1,4]   ZB = [4,7,5,8]   ZC = [2,5]   ZD = [3,6]
```

`XA`'s order ends in `1,4`, so a single `X` fault on the `XA` ancilla after its second CNOT
leaves the weight-2 hook `X₁X₄`. Since `X₁X₄X₈` is a weight-3 logical, `{X₁X₄}` together with the
single-qubit residual `{X₈}` is a **weight-2 effective logical**:

```
residual set (X sector, identical for every schedule with these orders):
  {0} {1} {2} {3} {4} {5} {6} {7} {8} {0,1} {1,4} {6,7} {7,8}
  {1,4,5} {4,6,7} {1,2,4,5} {3,4,6,7}
d_eff = 2      witness residuals  {1,4} and {8}
```

### 4.2 Exhaustive scan over all measurement-consistent schedules

Schedule model for this scan: each check's `j`-th CNOT at `start_c + j` (consecutive steps),
`start_c` free — the full offset family, filtered by legality and (MC). Z-memory, `R = 3`,
exhaustive weight-≤3.

| depth | legal | measurement-consistent | `d_circ = 2` | `d_circ = 3` |
|---|---|---|---|---|
| 4 | 0 | 0 | – | – |
| 5 | 36 | 0 | – | – |
| 6 | 474 | 96 (all interleaved) | **96** | 0 |
| 7 | 6 282 | 2 572 (all interleaved) | **2 572** | 0 |
| 8 | 48 848 | 23 902 (23 854 interleaved + 48 non-interleaved) | **23 902** | 0 |

**26 570 measurement-consistent schedules, every one with `d_circ = 2 = d_eff`.** The 48
non-interleaved ones also give 2, as Strikis et al. Cor. 1 requires (a consistency check on the
whole pipeline).

### 4.3 Why — and that it is not an artefact of these orders

Exhaustive over **all 2 304 within-check X-order choices** (`4!·4!·2!·2!`), enumerating every
weight-2 effective logical of the resulting residual set:

- `d_eff = 2` for **1 280** order sets, `d_eff = 3` for 1 024;
- weight-2 effective logicals occur in two shapes only: `(|E|,|F|) = (1,2)` — 3 072 instances —
  and `(2,3)` — 384 instances;
- **every one of the 3 456 weight-2 effective logicals has `|s| = 1`** (a single Z-check).

**CONJECTURED 4.1.** For the rotated `d = 3` surface code, `d_circ = d_eff` for every legal,
measurement-consistent schedule and every within-check order choice.
*Derivation.* All X/Z overlaps are `≤ 2` (computed: `{0, 2}`), so Conj. 3.2 gives `u ⊆ s` for
both members of any weight-2 effective logical `γ = {E,F}` with `s(E) = s(F) = s`. By the
exhaustive order scan `|s| = 1`, so `u_E, u_F ∈ {0, s}`. If `u_E = u_F`, placing both faults in
the same round closes the lift at weight 2. If `u_E ≠ u_F`, one is `0` and the other is `s`, and
placing the `u = 0` fault in round `r` and the `u = s` fault in round `r+1` closes it at weight 2
(§6.1, `k = 1`). Either way `repair(γ) = 0` and `d_circ = |γ| = d_eff`. ∎(sketch; the gap is that
the argument covers weight-2 effective logicals of the *residual* kinds enumerated, which is what
decides `d_circ ∈ {2,3}` here, not a general statement for all codes.)

### 4.4 A/B pair (surface), `R = 2..5`, `stim`-confirmed

Both schedules use the §4.1 within-check orders and therefore have identical residual sets.

`M_IL` (interleaved, depth 8), starts `XA,XB,XC,XD @0,0,0,0 ; ZA@2 ZB@4 ZC@1 ZD@2`:

```
 t0 : XA:a→q2  XB:a→q3  XC:a→q0  XD:a→q7
 t1 : XA:a→q5  XB:a→q4  XC:a→q1  XD:a→q8  ZC:q2→a
 t2 : XA:a→q1  XB:a→q6  ZA:q0→a  ZC:q5→a  ZD:q3→a
 t3 : XA:a→q4  XB:a→q7  ZA:q3→a  ZD:q6→a
 t4 : ZA:q1→a  ZB:q4→a
 t5 : ZA:q4→a  ZB:q7→a
 t6 : ZB:q5→a
 t7 : ZB:q8→a
```

`M_NI` (non-interleaved, depth 8): X block `t0..t3`, Z block `t4..t7`.

| schedule | sector | `d_eff` | `d_circ`, `R = 2,3,4,5` | `stim` |
|---|---|---|---|---|
| `M_IL` | Z-memory | 2 | **2, 2, 2, 2** | agrees (117/227/337/447 columns) |
| `M_IL` | X-memory | 3 | 3, 3, 3, 3 | agrees |
| `M_NI` | Z-memory | 2 | **2, 2, 2, 2** | agrees (117/227/337/447 columns) |
| `M_NI` | X-memory | 3 | 3, 3, 3, 3 | agrees |

Hook voltages present in either schedule: **none** (as Conj. 3.2 predicts). Weight-2 witness
(both schedules): `('cnot', round 0, step 0, gate 3, 'IX')` and
`('cnot', round 0, step 1, gate 0, 'XI')` — a bare data `X` and the `XA` hook.

---

## 5. Arm 2 — Steane `[[7,1,3]]`: reading (a)

### 5.1 Why Steane is the right fallback

Steane's `X_i` and `Z_i` have **identical** weight-4 supports, so `|supp(X_i) ∩ supp(Z_i)| = 4`
(overlap histogram `{2, 4}`) — the regime Conj. 3.1 says is necessary for voltage. Also, the
Hamming/Fano structure makes **every** pair of qubits lie in a unique weight-3 logical, so
**every** within-check order is hook-damaged: `d_eff = 2` for every Steane schedule. There is no
hook-safe ordering to compare against, which makes the interleaving the only variable.

### 5.2 The witness

Orders and time slots (depth 8, legal, measurement-consistent, interleaved):

```
X1 = [6,3,5,4] @ t 0,1,2,3        Z1 = [3,4,6,5] @ t 0,1,3,4
X2 = [1,5,6,2] @ t 4,5,6,7        Z2 = [2,1,5,6] @ t 2,3,6,7
X3 = [4,2,6,0] @ t 0,1,2,7        Z3 = [2,4,6,0] @ t 0,4,5,6
```

```
 t0 : X1:a→q6  X3:a→q4  Z1:q3→a  Z3:q2→a
 t1 : X1:a→q3  X3:a→q2  Z1:q4→a
 t2 : X1:a→q5  X3:a→q6  Z2:q2→a
 t3 : X1:a→q4  Z1:q6→a  Z2:q1→a
 t4 : X2:a→q1  Z1:q5→a  Z3:q4→a
 t5 : X2:a→q5  Z3:q6→a
 t6 : X2:a→q6  Z2:q5→a  Z3:q0→a
 t7 : X2:a→q2  X3:a→q0  Z2:q6→a
```

Residual set (Z-memory), identical to the non-interleaved partner's:
`{0}…{6}, {0,6}, {2,6}, {4,5}, {0,2,6}, {2,5,6}, {3,4,5}, {0,2,4,6}, {1,2,5,6}, {3,4,5,6}` —
`d_eff = 2`.

| `R` | `d_circ` (own propagator) | DEM columns / detectors | `stim` |
|---|---|---|---|
| 2 | **3** | 149 / 12 | `d = 3`, 149 / 12 |
| 3 | **3** | 285 / 18 | `d = 3`, 285 / 18 |
| 4 | **3** | 421 / 24 | `d = 3`, 421 / 24 |
| 5 | **3** | 557 / 30 | `d = 3`, 557 / 30 |

Weight-3 witness at `R = 3`: `('prep','Z1',0,'X')`, `('cnot',0,0,3,'XX')`, `('cnot',0,1,0,'XI')`.

**Hook voltages present — one per X-check:** `(X1, hook {5,4}, Z1)`, `(X2, hook {6,2}, Z2)`,
`(X3, hook {6,0}, Z3)`, each with `u_b = 1`, `s_b = 0`. That is three genuine vertical edges,
and they are exactly what blocks all three weight-2 effective logicals.

**Honest scope note.** In the **X-memory** sector this same circuit has `d_eff = 2` and
`d_circ = 2`: the interleaving repairs the X-sector hooks but not the Z-sector ones. So
`min(d_circ^Z, d_circ^X) = 2` for this circuit. The lift `d_eff = 2 → d_circ = 3` is a
**per-sector** statement, exactly and exhaustively established for the Z-memory experiment. A
schedule lifting both sectors simultaneously was searched for; see §5.4.

### 5.3 The non-interleaved A/B partner

Same within-check orders, X block `t0..t4`, Z block `t5..t9` (depth 10, measurement-consistent,
non-interleaved). Residual sets identical to `M_IL` in both sectors (Consequence 2.1 of the
recon, verified again).

| schedule | sector | `d_eff` | `d_circ`, `R = 2,3,4,5` | hook voltages | `g(C)` |
|---|---|---|---|---|---|
| `M_IL` (interleaved, depth 8) | Z-memory | 2 | **3, 3, 3, 3** | 3 | **1** |
| `M_NI` (non-interleaved, depth 10) | Z-memory | 2 | **2, 2, 2, 2** | none | 0 |
| `M_IL` | X-memory | 2 | 2, 2, 2, 2 | – | 0 |
| `M_NI` | X-memory | 2 | 2, 2, 2, 2 | – | 0 |

`stim` agrees on all 16 entries. `M_NI`'s weight-2 witness at `R = 3`:
`('cnot',0,1,0,'XI')` (the `X1` hook) and `('idle',0,0,2,'X')` (bare `X₂`).

**This is the `d = 3` gap instance the gate asked for**, with an A/B pair that isolates
interleaving as the sole cause: identical code, identical within-check CNOT orders, identical
residual set, identical `d_eff`; only the interleaving pattern differs, and `d_circ` moves from 2
to 3.

### 5.4 Density of the effect

Three measurements of how common the lift is:

- **With the §5.2 within-check orders, at depth 8, exhaustively: 2 of the 16 measurement-consistent
  schedules give `d_circ = 3`; the other 14 give 2.** Code, orders and depth are held fixed, so
  this isolates the interleaving pattern as the only variable — the sharpest form of "mixed".
- Under a *different* Steane order set at depth 8, all 2 152 measurement-consistent schedules have
  zero hook voltage and `d_circ = 2`; at depth 9, 1 499 of 60 000 carry hook voltage, and of the
  40 of those examined exhaustively all still had `d_circ = 2` — voltage on *one* hook is not
  enough, because the other two weight-2 effective logicals still close.
- A randomised sweep over order sets and depth-8/9 schedules found predicted `d_circ = 3` in
  **2 of 4 531** screened schedules, both confirmed by exhaustive enumeration.

So the effect is **rare but robust**: it needs non-zero voltage on *all three* weight-2 effective
logicals simultaneously — a conjunction of three parity conditions, each of which is individually
easy to satisfy.

---

## 6. The conjectured formula, both sides

### 6.1 The repair cost, computed from one round only

Group-ring bookkeeping (recon §3.4). For a fault `i` placed in round `r_i`, the detector chain is
`x^{r_i}( u_i(1+x) + s_i x )`. For an effective logical `γ = {e₁,…,e_w}` (`Σ s_i = 0`,
`Σ λ_i = 1`) with a round assignment, put `B(x) = Σ_i s_i x^{r_i}`; `B(1) = 0`, so
`B = (1+x)C(x)` with `C` unique (`F₂[x,x⁻¹]` is a domain). The total chain is
`(1+x)(A(x) + xC(x))` with `A(x) = Σ_i u_i x^{r_i}`. A measurement-flip fault on check `g` in
round `r` has `s = 0`, `u = {g}` and adds one monomial to `A` at cost 1. Hence

```
    repair(γ)  =  min over round assignments and weight-1 representatives of
                  wt( A(x) + x·C(x) )   as a set of (check, round) pairs
    ℓ(γ)       =  |γ| + repair(γ)
    d_circ    ?=  min_γ ℓ(γ)                                 [the conjectured formula]
```

For `w = 2` with `s₁ = s₂ = s` and round gap `k`:

```
    k = 0 :  |u₁ ⊕ u₂|
    k = 1 :  |u₁| + |u₂ ⊕ s|          (and the mirror)
    k ≥ 2 :  |u₁| + (k−1)|s| + |u₂ ⊕ s|      — never better when s ≠ 0
```

so only `k ∈ {0,1}` can be optimal. `U(E)`, the set of `u` vectors achievable at weight 1 for a
given residual `E`, is read off from the one-round fault enumeration. **No multi-round circuit is
built anywhere in this computation** — this is the node's "不需要构造完整多轮电路的等号判定算法"
in the weight-2 case.

### 6.2 Both sides, for four named schedules

| schedule | `γ` | `|γ|` | `s` | `repair(γ)` | route | `ℓ(γ)` | `min_γ ℓ` | exhaustive `d_circ` |
|---|---|---|---|---|---|---|---|---|
| **Steane `M_IL`** | `{X₃, hook{2,6}}` | 2 | `(1,0,0)` | 1 | same-round | 3 | | |
| | `{X₂, hook{4,5}}` | 2 | `(0,1,1)` | 1 | same-round | 3 | | |
| | `{X₅, hook{0,6}}` | 2 | `(1,1,0)` | 1 | same-round | 3 | **3** | **3** ✓ |
| **Steane `M_NI`** | `{X₂, hook{4,5}}` | 2 | `(0,1,1)` | 0 | same-round | 2 | | |
| | `{X₃, hook{2,6}}` | 2 | `(1,0,0)` | 0 | same-round | 2 | | |
| | `{X₅, hook{0,6}}` | 2 | `(1,1,0)` | 0 | same-round | 2 | **2** | **2** ✓ |
| **surface `M_IL`** | `{X₇, hook{1,4}}` | 2 | `(0,1,0,0)` | 0 | same-round | 2 | | |
| | `{X₈, hook{1,4}}` | 2 | `(0,1,0,0)` | 0 | same-round | 2 | **2** | **2** ✓ |
| **surface `M_NI`** | `{X₇, hook{1,4}}` | 2 | `(0,1,0,0)` | 0 | same-round | 2 | | |
| | `{X₈, hook{1,4}}` | 2 | `(0,1,0,0)` | 0 | same-round | 2 | **2** | **2** ✓ |
| **`[[4,2,2]]` valid IL** | `{hook{2,3}}` | 1 | `(0)` | 1 | vertical repair | 2 | **2** | **2** ✓ |

**Agreement is exact in every row**, including the sign of the gap: `repair = 1` exactly where
`d_circ > d_eff`, `repair = 0` exactly where `d_circ = d_eff`.

### 6.3 Bulk agreement test

Predictor (one round only) vs exhaustive weight-≤3 enumeration (`R = 3`, Z-memory), over every
measurement-consistent schedule in each family:

| family | schedules | `(predicted, exact)` |
|---|---|---|
| surface, offset family, depth 6 | 96 | `(2,2): 96` |
| surface, offset family, depth 7 | 2 572 | `(2,2): 2 572` |
| Steane, general slots, depth 8, order set A | 1 500 (capped) | `(2,2): 1 500` |
| Steane, general slots, depth 8, **witness order set** | 16 (exhaustive) | `(2,2): 14`, **`(3,3): 2`** |
| `[[4,2,2]]`, general slots, depth 7 | 176 (exhaustive) | `(1,1): 173`, **`(2,2): 3`** |
| `[[4,2,2]]`, general slots, depth 8 | 769 (exhaustive) | `(1,1): 743`, **`(2,2): 26`** |
| **total** | **5 129** | **agreement 5 129 / 5 129 = 1.0000** |

Two further exhaustive agreement runs done earlier in the session and consistent with the above:
Steane order set A at depth 8 (all 2 152 schedules) → `(2,2)` on all 2 152; and the same
`[[4,2,2]]` depth-7 family → 176/176.

Note the fourth row: with the §5.2 witness's within-check orders there are exactly **16**
measurement-consistent depth-8 schedules, and exactly **2** of them reach `d_circ = 3`. That is
the sharpest available statement of "mixed by interleaving pattern" — with the code, the
within-check orders and the depth all held fixed, the interleaving pattern alone moves `d_circ`
between 2 and 3, and the one-round voltage data predicts which.

---

## 7. Correction to the round-1 recon's `[[4,2,2]]` result

**The recon's interleaved circuit (`artifacts/circdist_lift_recon_20260820.md` §4.1) is not a
valid syndrome-extraction circuit.** With X order `q₀,q₁,q₂,q₃` at `t1..t4` and Z order
`q₂,q₀,q₁,q₃` at `t2..t5`, the pair `(a,b)` has
`#{q : t(q→b) < t(a→q)} = 1` — odd, violating (MC). `stim` reports non-deterministic detectors
for `R = 2` and `R = 3`. The recon's own numbers (`d_eff = 1`, `d_circ = 2`) are reproduced by my
propagator, which — like the recon's — does not check determinism; the detectors it uses are not
deterministic, so the number is not a circuit distance.

**The claim survives, with a different witness.** Enumerating measurement-consistent `[[4,2,2]]`
schedules with the same within-check orders (`a = [0,1,2,3]`, `b = [2,0,1,3]`):

| depth | consistent schedules | `d_circ = 1` | `d_circ = 2` |
|---|---|---|---|
| 5 | 2 | 2 | 0 |
| 6 | 27 | 27 | 0 |
| 7 | 176 | 173 | **3** |
| 8 | 769 | 743 | **26** |

Explicit valid witness (depth 7, interleaved, measurement-consistent, `stim`-confirmed
`d_circ = 2` for `R = 2,3,4,5`), slots `a = [0,3,4,5]`, `b = [0,1,2,6]`:

```
 t0 : a:anc→q0   b:q2→anc
 t1 :            b:q0→anc
 t2 :            b:q1→anc
 t3 : a:anc→q1
 t4 : a:anc→q2
 t5 : a:anc→q3
 t6 :            b:q3→anc
```

(MC) check for the single pair `(a,b)`: `supp(a) ∩ supp(b) = {0,1,2,3}`, and
`t(q→b) < t(a→q)` holds for `q = 0` (1 < 0? no), `q = 1` (2 < 3 yes), `q = 2` (0 < 4 yes),
`q = 3` (6 < 5? no) — count 2, even. Valid.

Its residual `{2,3}` has `s = 0`, `λ = 1` (a weight-1 effective logical, `d_eff = 1`) and its
**unique** achievable `u = 1`: a pure vertical edge of voltage 1. `repair = 1`, `ℓ = 2`, and
`d_circ = 2` exactly. This is the recon's `d_circ = |γ| + repair` picture realised in a valid
circuit, and it is the smallest instance found.

**Consequence for the node record.** The recon's acceptance-clause discharge ("至少一个交错严格
不等号例子") **still holds**, but the citable witness must be replaced — either by the `[[4,2,2]]`
circuit above or, better, by the `d = 3` Steane pair of §5, which is non-degenerate.

---

## 8. Cross-node implication for `CIRCDIST.gross`

Exact computation of the gross code `[[144,12,12]]` (bivariate bicycle, `ℓ = 12`, `m = 6`,
`A = x³ + y + y²`, `B = y³ + x + x²`, `H_X = [A|B]`, `H_Z = [Bᵀ|Aᵀ]`; row weights all 6,
`H_X H_Zᵀ = 0` verified):

```
|supp(X-check) ∩ supp(Z-check)| histogram over all 72 × 72 pairs :  {0: 4536, 2: 648}
maximum overlap : 2
```

**Every X/Z check pair of the gross code overlaps in at most 2 qubits.** Under Conj. 3.1, **no
hook in any measurement-consistent gross-code schedule can carry timelike voltage**; by Conj. 3.2
every hook is horizontal, exactly as in the rotated surface code.

This is evidence *against* the existence of a distance-12 interleaved gross circuit — i.e.
toward `D*_Gross = 11` — and it inverts the recon's §8.5 reading, which treated `CIRCDIST.lift`
as the mechanism by which the gross code *could* reach 12.

**It is a lead, not a claim.** §3 constrains the voltage of a *single hook*. The gross question
concerns weight-11 effective logicals, where (i) a low-weight mechanism can combine many faults
whose individual `u`s are horizontal but whose *sum* is not matched by the available
representatives (the `|s| = 1` step of Conj. 4.1 has no analogue at weight 11), and (ii) my
weight-2 case analysis of `repair` does not extend to `w = 11` without the finite-window
argument. Recommended: register this as a premise of a new route on `CIRCDIST.gross`, not as a
result.

---

## 9. Honest limitations

1. **Nothing is proved.** Conj. 2.1, 3.1, 3.2, 4.1 have short combinatorial derivations that I
   believe, but they have had no independent review and the boundary rounds (`r = 0`, terminal)
   are handled only by the exhaustive enumeration, not by the derivations.
2. **`d_eff` and `d_circ` are per-sector.** All headline numbers are for one memory experiment.
   The Steane witness lifts the Z-memory sector only (§5.2). A both-sector witness is a small
   open item; the search for one is reported in §5.4 and is not resolved.
3. **The schedule model in §4.2 is the offset family** (each check's CNOTs on consecutive
   steps). The Steane arm uses the fully general model (arbitrary increasing time slots per
   check, §10.3), so the surface-code "reading (b)" statement is exhaustive over the offset
   family and over all within-check orders, but not over all general-slot schedules. Conj. 4.1
   covers the general case; the enumeration does not.
4. **`repair(γ)` was analysed exactly only for `|γ| = 2`** (and `|γ| = 1` for `[[4,2,2]]`). The
   `k ≥ 2` round-gap case is dismissed by an inequality that holds for `s ≠ 0`; for `s = 0` the
   criterion degenerates to `u₁ = u₂` in the same round, which is what the code implements.
5. **Two implementations, one author.** The hand-written `F₂` propagator and the `stim` circuit
   generator are independent in their propagation and detector bookkeeping, and they agreed on
   every DEM column count and every distance reported here — but the fault-location set and the
   detector *definitions* are the same design in both, so a systematic modelling error would not
   be caught. The `stim` install (`pip install stim`, version 1.16.0) is new in this environment;
   the recon's §8.6 tooling note is now out of date.
6. **The `[[4,2,2]]` re-check tracks the `Z₀Z₂` observable only** (the one the recon's hook
   flips), not both logical qubits.

---

## 10. Code

All results are reproducible from the following. Python 3.9, `numpy` (only for §8), `stim`
1.16.0 (only for the cross-check).

### 10.1 `circdist.py` — code, schedules, propagation, DEM, distance, `d_eff`

```python
from itertools import combinations, permutations, product

PAULI1 = ['X', 'Y', 'Z']
PAULI2 = [a + b for a in 'IXYZ' for b in 'IXYZ'][1:]      # 15 non-identity 2-qubit Paulis


def pxz(p):
    return (1 if p in 'XY' else 0, 1 if p in 'YZ' else 0)


class Code:
    def __init__(self, n, xchecks, zchecks, zl, xl, name=""):
        self.n = n; self.name = name
        self.xchecks = xchecks; self.zchecks = zchecks
        self.xnames = list(xchecks); self.znames = list(zchecks)
        self.names = self.xnames + self.znames
        self.anc = {c: n + i for i, c in enumerate(self.names)}
        self.nq = n + len(self.names)
        self.zl = zl; self.xl = xl
        for a, s in xchecks.items():
            for b, t in zchecks.items():
                assert len(set(s) & set(t)) % 2 == 0, (a, b)
        assert len(set(zl) & set(xl)) % 2 == 1
        for b, t in zchecks.items():
            assert len(set(t) & set(xl)) % 2 == 0
        for a, s in xchecks.items():
            assert len(set(s) & set(zl)) % 2 == 0

    def syn(self, supp, basis):
        ch = self.zchecks if basis == 'Z' else self.xchecks
        nm = self.znames if basis == 'Z' else self.xnames
        return tuple(len(set(supp) & set(ch[c])) % 2 for c in nm)

    def log(self, supp, basis):
        L = self.zl if basis == 'Z' else self.xl
        return len(set(supp) & set(L)) % 2

    def distance(self, basis, maxw=5):
        for w in range(1, maxw + 1):
            for c in combinations(range(self.n), w):
                if all(v == 0 for v in self.syn(c, basis)) and self.log(c, basis):
                    return w, c
        return None, None


def build_steps(code, orders, times):
    T = max(max(v) for v in times.values()) + 1
    steps = [[] for _ in range(T)]
    for c, qs in orders.items():
        a = code.anc[c]
        for j, q in enumerate(qs):
            t = times[c][j]
            if c in code.xchecks:
                steps[t].append(('CX', a, q, c))      # X-check ancilla is the control
            else:
                steps[t].append(('CX', q, a, c))      # Z-check ancilla is the target
    return steps


def legal(steps):
    for st in steps:
        used = set()
        for (_, c, t, _) in st:
            if c in used or t in used:
                return False
            used.add(c); used.add(t)
    return True


def qtime(orders, times, c):
    return {q: times[c][i] for i, q in enumerate(orders[c])}


def consistency_violations(code, orders, times):
    """(MC): for every X-check a and Z-check b,
       #{q in supp(a)&supp(b) : t(q->b) < t(a->q)} must be even."""
    bad = []
    for an in code.xnames:
        ta = qtime(orders, times, an)
        for bn in code.znames:
            tb = qtime(orders, times, bn)
            I = [q for q in ta if q in tb]
            if not I:
                continue
            if sum(1 for q in I if tb[q] < ta[q]) % 2:
                bad.append((an, bn, len(I)))
    return bad


def is_consistent(code, orders, times):
    return not consistency_violations(code, orders, times)


def is_interleaved(code, times):
    xt = [t for c in code.xnames for t in times[c]]
    zt = [t for c in code.znames for t in times[c]]
    return not (max(xt) < min(zt) or max(zt) < min(xt))


def enumerate_schedules(code, orders, Tmax, need_consistent=True):
    """offset family: check c's j-th CNOT at start_c + j"""
    ranges = [range(0, Tmax - len(orders[c]) + 1) for c in code.names]
    for combo in product(*ranges):
        times = {c: [combo[i] + j for j in range(len(orders[c]))]
                 for i, c in enumerate(code.names)}
        if need_consistent and not is_consistent(code, orders, times):
            continue
        steps = build_steps(code, orders, times)
        if len(steps) != Tmax:
            continue
        if legal(steps):
            yield times, steps


class Sim:
    """forward F2 Pauli-frame propagation through the R-round memory circuit"""
    def __init__(self, code, steps, R):
        self.code = code; self.steps = steps; self.R = R; self.T = len(steps)
        self.busy = []
        for st in steps:
            s = set()
            for (_, c, t, _) in st:
                s.add(c); s.add(t)
            self.busy.append(s)

    def run(self, fault):
        code = self.code
        x = [0] * code.nq; z = [0] * code.nq; m = {}
        for r in range(self.R):
            if fault is not None and fault[0] == 'prep' and fault[2] == r:
                a = code.anc[fault[1]]; px, pz = pxz(fault[3]); x[a] ^= px; z[a] ^= pz
            for t in range(self.T):
                for gi, (_, c, tg, _) in enumerate(self.steps[t]):
                    x[tg] ^= x[c]; z[c] ^= z[tg]
                    if (fault is not None and fault[0] == 'cnot'
                            and fault[1] == r and fault[2] == t and fault[3] == gi):
                        p2 = fault[4]
                        if p2[0] != 'I':
                            a1, b1 = pxz(p2[0]); x[c] ^= a1; z[c] ^= b1
                        if p2[1] != 'I':
                            a2, b2 = pxz(p2[1]); x[tg] ^= a2; z[tg] ^= b2
                if (fault is not None and fault[0] == 'idle'
                        and fault[1] == r and fault[2] == t):
                    q = fault[3]; px, pz = pxz(fault[4]); x[q] ^= px; z[q] ^= pz
            for nme in code.xnames:                       # MX: flipped by a Z error
                a = code.anc[nme]; m[(nme, r)] = z[a]; x[a] = 0; z[a] = 0
            for nme in code.znames:                       # M : flipped by an X error
                a = code.anc[nme]; m[(nme, r)] = x[a]; x[a] = 0; z[a] = 0
        if fault is not None and fault[0] == 'meas':
            m[(fault[1], fault[2])] ^= 1
        return m, x[:code.n], z[:code.n]

    def locations(self):
        code = self.code; locs = []
        for r in range(self.R):
            for nme in code.names:
                for p in PAULI1:
                    locs.append(('prep', nme, r, p))
                locs.append(('meas', nme, r))
            for t in range(self.T):
                for gi in range(len(self.steps[t])):
                    for p2 in PAULI2:
                        locs.append(('cnot', r, t, gi, p2))
                for q in range(code.nq):
                    if q not in self.busy[t]:
                        for p in PAULI1:
                            locs.append(('idle', r, t, q, p))
        return locs


def detector_defs(code, R, basis):
    dets = []
    det_checks = code.znames if basis == 'Z' else code.xnames
    oth = code.xnames if basis == 'Z' else code.znames
    for nme in det_checks:
        for r in range(R):
            dets.append(('cmp', nme, r))
        dets.append(('term', nme, R - 1))
    for nme in oth:
        for r in range(1, R):
            dets.append(('cmp', nme, r))
    return dets


def build_dem(code, steps, R, basis):
    sim = Sim(code, steps, R); dets = detector_defs(code, R, basis)
    ch = code.zchecks if basis == 'Z' else code.xchecks
    L = code.zl if basis == 'Z' else code.xl
    cols = {}
    for loc in sim.locations():
        m, fx, fz = sim.run(loc)
        err = fx if basis == 'Z' else fz
        bits = 0
        for i, d in enumerate(dets):
            nme, r = d[1], d[2]; v = m[(nme, r)]
            if d[0] == 'cmp':
                if r >= 1:
                    v ^= m[(nme, r - 1)]
            else:
                v ^= sum(err[q] for q in ch[nme]) % 2
            if v:
                bits |= (1 << i)
        obs = sum(err[q] for q in L) % 2
        if bits == 0 and obs == 0:
            continue
        cols.setdefault((bits, obs), loc)
    return cols, dets, sim


def circuit_distance(cols, maxw=3):
    """exhaustive weight<=3 search; returns (d, witness) with d=4 meaning '>3'"""
    items = list(cols.items())
    for (bits, obs), loc in items:
        if bits == 0 and obs:
            return 1, [loc]
    bybits = {}
    for (bits, obs), loc in items:
        bybits.setdefault(bits, {})[obs] = loc
    for bits, d in bybits.items():
        if 0 in d and 1 in d:
            return 2, [d[0], d[1]]
    keys = list(bybits.items()); pairsum = {}
    for i in range(len(keys)):
        b1, d1 = keys[i]
        for j in range(i + 1, len(keys)):
            b2, d2 = keys[j]
            tgt = pairsum.setdefault(b1 ^ b2, {})
            for o1, l1 in d1.items():
                for o2, l2 in d2.items():
                    tgt.setdefault(o1 ^ o2, (l1, l2))
    for bits, d in bybits.items():
        if bits in pairsum:
            for o, loc in d.items():
                for o2, pl in pairsum[bits].items():
                    if o ^ o2:
                        return 3, [loc, pl[0], pl[1]]
    return 4, None


def residual_set(code, steps, basis):
    sim = Sim(code, steps, 1); res = set()
    for loc in sim.locations():
        m, fx, fz = sim.run(loc)
        err = fx if basis == 'Z' else fz
        res.add(frozenset(q for q in range(code.n) if err[q]))
    return res


def d_ext(code, res, basis, maxw=4):
    lst = [r for r in res if r]
    nz = len(code.znames) if basis == 'Z' else len(code.xnames)
    for w in range(1, maxw + 1):
        for combo in combinations(lst, w):
            s = [0] * nz; l = 0
            for r in combo:
                ss = code.syn(r, basis)
                for i in range(nz):
                    s[i] ^= ss[i]
                l ^= code.log(r, basis)
            if all(v == 0 for v in s) and l:
                return w, combo
    return maxw + 1, None


def fault_data(code, steps, basis):
    """one-round (residual support, s, u, lambda) for every single fault"""
    sim = Sim(code, steps, 1)
    nm = code.znames if basis == 'Z' else code.xnames
    out = []
    for loc in sim.locations():
        m, fx, fz = sim.run(loc)
        err = fx if basis == 'Z' else fz
        supp = frozenset(q for q in range(code.n) if err[q])
        out.append((loc, supp, code.syn(supp, basis),
                    tuple(m[(c, 0)] for c in nm), code.log(supp, basis)))
    return out
```

### 10.2 `codes.py`

```python
from circdist import Code

SURF = Code(9,
    {'XA': [1, 2, 4, 5], 'XB': [3, 4, 6, 7], 'XC': [0, 1], 'XD': [7, 8]},
    {'ZA': [0, 1, 3, 4], 'ZB': [4, 5, 7, 8], 'ZC': [2, 5], 'ZD': [3, 6]},
    zl=[0, 1, 2], xl=[0, 3, 6], name="rotated [[9,1,3]] surface")

H = {'1': [3, 4, 5, 6], '2': [1, 2, 5, 6], '3': [0, 2, 4, 6]}
STEANE = Code(7,
    {'X1': H['1'], 'X2': H['2'], 'X3': H['3']},
    {'Z1': H['1'], 'Z2': H['2'], 'Z3': H['3']},
    zl=[0, 1, 2], xl=[0, 1, 2], name="Steane [[7,1,3]]")

D422 = Code(4, {'a': [0, 1, 2, 3]}, {'b': [0, 1, 2, 3]},
            zl=[0, 2], xl=[0, 1], name="[[4,2,2]]")
```

### 10.3 `gensched.py` — general schedule search (arbitrary time slots per check)

```python
from itertools import combinations
from circdist import build_steps


def _pair_ok(code, orders, times, a, b):
    ta = {q: times[a][i] for i, q in enumerate(orders[a])}
    tb = {q: times[b][i] for i, q in enumerate(orders[b])}
    I = [q for q in ta if q in tb]
    return (not I) or sum(1 for q in I if tb[q] < ta[q]) % 2 == 0


def search(code, orders, T, limit=200000, cap=None):
    """every legal, measurement-consistent schedule of exact depth T"""
    names = code.names
    W = {c: len(orders[c]) for c in names}
    out = []; occupied = [set() for _ in range(T)]; times = {}; nodes = [0]

    def rec(k):
        if cap is not None and len(out) >= cap:
            return
        nodes[0] += 1
        if nodes[0] > limit:
            return
        if k == len(names):
            if max(max(v) for v in times.values()) != T - 1:
                return
            out.append(({c: list(v) for c, v in times.items()},
                        build_steps(code, orders, times)))
            return
        c = names[k]; a = code.anc[c]; qs = orders[c]
        for slots in combinations(range(T), W[c]):
            if any(a in occupied[t] or qs[i] in occupied[t] for i, t in enumerate(slots)):
                continue
            times[c] = list(slots)
            if c in code.xchecks:
                good = all(_pair_ok(code, orders, times, c, b)
                           for b in code.znames if b in times)
            else:
                good = all(_pair_ok(code, orders, times, aa, c)
                           for aa in code.xnames if aa in times)
            if good:
                for i, t in enumerate(slots):
                    occupied[t].add(a); occupied[t].add(qs[i])
                rec(k + 1)
                for i, t in enumerate(slots):
                    occupied[t].discard(a); occupied[t].discard(qs[i])
            del times[c]
            if cap is not None and len(out) >= cap:
                return
    rec(0)
    return out, nodes[0]
```

### 10.4 `voltage.py` — the repair cost, from one round only

```python
from circdist import fault_data


def wt(v):
    return sum(v)


def xor(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def residual_profiles(code, steps, basis):
    prof = {}
    for (loc, supp, s, u, lam) in fault_data(code, steps, basis):
        p = prof.setdefault(supp, {'s': s, 'lam': lam, 'U': {}})
        assert p['s'] == s and p['lam'] == lam
        p['U'].setdefault(u, loc)
    return prof


def weight2_logicals(code, prof):
    out = []; keys = [k for k in prof if k]
    zero = tuple([0] * len(prof[keys[0]]['s']))
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = keys[i], keys[j]
            if xor(prof[a]['s'], prof[b]['s']) == zero and (prof[a]['lam'] ^ prof[b]['lam']):
                out.append((a, b))
    return out


def repair2(prof, a, b):
    s = prof[a]['s']; best = None
    for ua, la in prof[a]['U'].items():
        for ub, lb in prof[b]['U'].items():
            for c, tag in ((wt(xor(ua, ub)), 'same-round'),
                           (wt(ua) + wt(xor(ub, s)), 'adjacent(a,b)'),
                           (wt(ub) + wt(xor(ua, s)), 'adjacent(b,a)')):
                if best is None or c < best[0]:
                    best = (c, tag, ua, ub, la, lb)
    return best


def predict(code, steps, basis, dmax=3):
    prof = residual_profiles(code, steps, basis)
    detail = []; best = dmax
    for (a, b) in weight2_logicals(code, prof):
        r = repair2(prof, a, b); detail.append((a, b, r))
        best = min(best, 2 + r[0])
    for k, p in prof.items():                       # weight-1 effective logicals
        if k and all(v == 0 for v in p['s']) and p['lam']:
            best = min(best, 1 + min(wt(u) for u in p['U']))
    return best, detail, prof
```

### 10.5 `hook_voltage.py` — the §3 diagnostic

```python
def hook_voltages(code, orders, times):
    """hooks with u_b = 1 while s_b = 0 : genuine timelike voltage"""
    out = []
    T = {c: {q: times[c][i] for i, q in enumerate(orders[c])} for c in code.names}
    for a in code.xnames:
        oa = orders[a]
        for j in range(1, len(oa)):
            S = oa[j:]
            for b in code.znames:
                inter = [q for q in S if q in set(orders[b])]
                if not inter:
                    continue
                u = sum(1 for q in inter if T[b][q] > T[a][q]) % 2
                s = len(inter) % 2
                if u and not s:
                    out.append((a, tuple(S), b, u, s))
    return out
```

### 10.6 `stimgen.py` — the independent cross-check

```python
import stim


def stim_circuit(code, steps, R, basis, p=1e-3):
    T = len(steps)
    xanc = [code.anc[c] for c in code.xnames]
    zanc = [code.anc[c] for c in code.znames]
    busy = []
    for st in steps:
        s = set()
        for (_, c, t, _) in st:
            s.add(c); s.add(t)
        busy.append(s)
    allq = list(range(code.nq)); data = list(range(code.n))
    c = stim.Circuit()
    c.append("R" if basis == 'Z' else "RX", data)
    det_checks = code.znames if basis == 'Z' else code.xnames
    oth = code.xnames if basis == 'Z' else code.znames
    nmeas = 0; recs = {}
    for r in range(R):
        c.append("RX", xanc); c.append("R", zanc)
        c.append("DEPOLARIZE1", xanc + zanc, p)
        for t in range(T):
            targ = []
            for (_, ctl, tgt, _) in steps[t]:
                targ += [ctl, tgt]
            if targ:
                c.append("CX", targ); c.append("DEPOLARIZE2", targ, p)
            idle = [q for q in allq if q not in busy[t]]
            if idle:
                c.append("DEPOLARIZE1", idle, p)
        c.append("MX", xanc, p)
        for i, n in enumerate(code.xnames):
            recs[(n, r)] = nmeas + i
        nmeas += len(xanc)
        c.append("M", zanc, p)
        for i, n in enumerate(code.znames):
            recs[(n, r)] = nmeas + i
        nmeas += len(zanc)
        for n in det_checks:
            if r == 0:
                c.append("DETECTOR", [stim.target_rec(recs[(n, 0)] - nmeas)])
            else:
                c.append("DETECTOR", [stim.target_rec(recs[(n, r)] - nmeas),
                                      stim.target_rec(recs[(n, r - 1)] - nmeas)])
        for n in oth:
            if r >= 1:
                c.append("DETECTOR", [stim.target_rec(recs[(n, r)] - nmeas),
                                      stim.target_rec(recs[(n, r - 1)] - nmeas)])
    c.append("M" if basis == 'Z' else "MX", data)
    for i, q in enumerate(data):
        recs[('d', q)] = nmeas + i
    nmeas += code.n
    ch = code.zchecks if basis == 'Z' else code.xchecks
    for n in det_checks:
        tg = [stim.target_rec(recs[(n, R - 1)] - nmeas)]
        for q in ch[n]:
            tg.append(stim.target_rec(recs[('d', q)] - nmeas))
        c.append("DETECTOR", tg)
    obs = code.zl if basis == 'Z' else code.xl
    c.append("OBSERVABLE_INCLUDE",
             [stim.target_rec(recs[('d', q)] - nmeas) for q in obs], 0)
    return c


def stim_dem_columns(circ):
    """raises ValueError on non-deterministic detectors -- the (MC) oracle"""
    dem = circ.detector_error_model(decompose_errors=False,
                                    approximate_disjoint_errors=True)
    cols = {}
    for inst in dem.flattened():
        if inst.type != 'error':
            continue
        bits = 0; obs = 0
        for t in inst.targets_copy():
            if t.is_relative_detector_id():
                bits ^= (1 << t.val)
            elif t.is_logical_observable_id():
                obs ^= 1
        if bits or obs:
            cols[(bits, obs)] = True
    return cols, dem.num_detectors
```

---

## 11. What this changes for the node

- The recon's **route R5** (`minimal-interleaved-gap-example`) is now discharged at `d = 3` with a
  non-degenerate logical and a `stim`-checked A/B pair (§5) — but its `[[4,2,2]]` premise `P5.1`
  must be replaced (§7).
- The recon's **route R6** (`gap-formula-and-decision-algorithm`) is repriced **up**: the
  one-round repair-cost formula reproduced the exhaustive answer on every schedule tested, and
  §6.1 gives a concrete decision procedure at `|γ| = 2` that never builds `C_R(M)`. `P6.2` (the
  matching lower bound) remains the hard part, but it is now supported by a large numerical
  agreement rather than a single instance.
- A **new premise for every route**: (MC). It belongs in the definition of "legal schedule" for
  this node and for `CIRCDIST.gross` and `CIRCDIST.cplx` (where it changes the search space of
  the complexity question, possibly substantially).
- The **most promising new object** is Conj. 3.1: an overlap-4 necessary condition for hook
  voltage, which converts the node's iff from a statement about interleaving patterns into a
  statement about the code's Tanner-level geometry. Proving 3.1 and finding the matching
  sufficient condition looks cheaper than the general lift criterion, and it is what decides the
  gross-code question (§8).
