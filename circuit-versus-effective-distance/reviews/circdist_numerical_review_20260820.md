# CIRCDIST — independent numerical review, 2026-08-20

**Reviewer:** fresh Opus 5 session, independent-reviewer role. One budget-boxed session, no
sub-agents.

## Independence statement

I authored **none** of the reviewed artifacts (`artifacts/circdist_lift_recon_20260820.md`,
`artifacts/circdist_lift_d3gate_20260820.md`, `artifacts/circdist_gross_g1_20260820.md`,
`artifacts/circdist_gross_recon_20260820.md`) and none of the reviewed proof-DAG nodes. I was
given **no desired verdict** — my instructions were to try to refute each claim, and a claim
survives only where my own from-scratch computation failed to break it. I reused **no proposer
code**: every number below comes from code I wrote in this session (reproduced in §7), in two
independent implementations (a hand-written F₂ symplectic propagator and my own `stim` circuit
generator, `stim` 1.16.0, numpy 2.0.2, Python 3.9.6). I did not modify any file other than this
one, and I did not touch `research/circdist/proof-dag/`.

## Verdict table

| # | item | verdict |
|---|---|---|
| 1 | `[[4,2,2]]` (MC) constraint, repaired witnesses, retracted depth-5 circuit | **CONFIRM** (one definitional discrepancy, §1.4) |
| 2 | Steane `[[7,1,3]]` interleaved depth-8 witness, `d_eff = 2 → d_circ = 3` | **CONFIRM** |
| 3a | Gross weight-6 six-hook fault set, as a *fault set* | **CONFIRM** (value reproduced exactly) |
| 3b | Gross weight-6 witness *for the named translation-invariant schedule*, as a circuit-distance statement | **REFUTE** — that schedule, and all 25 920 in the class, have **non-deterministic detectors** (§3.3) |
| 3c | the multi-hook mechanism / refutation of the `d_ext ∈ {10,11,12}` clause | **CONFIRM after repair** — I rebuilt it on an (MC)-valid schedule (§3.4) |
| 3d | surviving universal claim `d_ext(E(M)) ≤ 11` | **CONFIRM** |
| 4a | G1 histogram spot-check, buckets 6 / 8 / 12 | **CONFIRM** as fault sets; inherits the §3.3 break |
| 4b | `d_circ = min_γ(|γ| + repair(γ))` agreement, 4 schedules × 2 sectors | **CONFIRM** (8/8) |

**One break was found**, in item 3. It is stated in full in §3.3 and it is repairable (§3.4).

## 0. Type audit and definitions used (rule 7a, 7g)

Every term resolves to `research/circdist/notes/CIRCDIST_PROBLEMS.md` (公共定义) or to a definition
I state here.

* **Circuit.** CSS code, one ancilla per stabiliser generator, prepared once and measured once per
  round. X-check ancilla: prep `|+⟩`, **control** of `CNOT(anc → q)` for each `q ∈ supp`, measured
  in X. Z-check ancilla: prep `|0⟩`, **target** of `CNOT(q → anc)`, measured in Z. A *schedule*
  assigns a time slot to every CNOT; no qubit is in two two-qubit gates at one slot.
* **Memory experiment (公共定义 "标准 memory experiment ... 理想最终读出边界").** Z-memory: ideal
  `|0⟩^n` data init, `R` identical rounds, ideal transversal Z readout. X-memory: dual. Detectors
  (primary = the check type stabilising the initial state): `D_{g,0} = m_{g,0}`;
  `D_{g,r} = m_{g,r} + m_{g,r-1}` for `r ≥ 1`; terminal `D_g = m_{g,R-1} + ⊕_{q∈supp(g)} readout(q)`.
  Dual-type checks carry only the difference detectors `r ≥ 1`. Observable = readout parity on the
  logical support.
* **Elementary fault, `|F|`.** One of: a Pauli on an ancilla right after prep; one of the 15
  non-identity two-qubit Paulis right after a CNOT; a Pauli on any idle qubit at any slot; a
  classical flip of one recorded ancilla outcome. Each has weight 1. Data init and final readout
  are ideal (公共定义).
* **`d_circ(C) = min{|F| : F fires no detector but flips a non-trivial logical}`** — 公共定义 verbatim.
* **`d_eff(M) := d_ext(E(M))`** — 公共定义. `E(M)` = the set of terminal residual data errors of
  single faults over **one** round; `d_ext` = the minimum **number of residuals** whose product has
  trivial syndrome and non-trivial logical action.
* **(MC), my own statement (see §1.1):** for every X-check `a` and Z-check `b`,
  `#{q ∈ supp(a) ∩ supp(b) : t(a→q) < t(q→b)}` is even.

**Sectors.** Every `d_eff`/`d_circ` number below is per-memory-experiment and I report **both**
sectors everywhere (rule 7b). For the Gross code the "Z-sector" of the G1 artifact = Z-type faults,
X-check detectors = my **X-memory** experiment.

**Supports and dimensions.** `[[4,2,2]]`: data 0–3, X-anc = qubit 4, Z-anc = qubit 5;
`S_X = S_Z = {0,1,2,3}`; `Z_L = Z₀Z₂`, `X_L = X₀X₁`. Steane `[[7,1,3]]`: data 0–6, X-anc 7–9,
Z-anc 10–12; `X`- and `Z`-checks both `{3,4,5,6},{1,2,5,6},{0,2,4,6}`; `Z_L = Z₀Z₁Z₂`,
`X_L = X₀X₁X₂`. Gross: data 0–143 (left half 0–71 a free `G = Z₁₂ × Z₆`-set, right half 72–143),
X-anc 144–215, Z-anc 216–287; group element `g = 6i + j`, `i ∈ Z₁₂`, `j ∈ Z₆`.

## 1. Item 1 — `[[4,2,2]]`

### 1.1 The measurement-consistency constraint, derived before reading the proposer's derivation

**Anchoring disclosure (rule 7c).** I read the node YAML `CIRCDIST.lift.gap-example.yaml` first, and
its `assessment.summary` states the constraint in one line. So I had seen the *statement* (in the
proposer's notation) before deriving. I had **not** read the derivation. I wrote my derivation to a
timestamped scratch file *before* opening
`artifacts/circdist_lift_d3gate_20260820.md`. My derivation coincides with §2 of that artifact
notationally as well as mathematically — **I flag this coincidence rather than claim independence
of notation.** The mathematics below is mine.

Conjugation rules: `CNOT_{c,t}` sends `X_c ↦ X_c X_t`, `X_t ↦ X_t`, `Z_c ↦ Z_c`, `Z_t ↦ Z_c Z_t`.

*Z-ancilla side.* Back-propagate `Z_b` through one round. Crossing `CNOT(q→b)` (b is target) gives
`Z_b ↦ Z_q Z_b`, so `Z_q` enters at time `t(q→b)`. Once `Z_q` is present, crossing an **earlier**
`CNOT(a→q)` (q is target) gives `Z_q ↦ Z_a Z_q`. So at the start of the round the observable is

```
    Z_b(prep) · ∏_{q ∈ supp(b)} Z_q · ∏_a Z_a^{c_Z(a,b)} ,
    c_Z(a,b) = #{ q ∈ supp(a) ∩ supp(b) : t(a→q) < t(q→b) } .
```

`Z_b(prep) = +1`; `∏ Z_q` is the Z-stabiliser and back-propagates cleanly through **earlier
rounds**, because there the full count `|supp(a) ∩ supp(b)|` appears and it is even by CSS
commutation, so all earlier-round `Z_a` cancel. But `Z_a` for an X-ancilla freshly prepared in
`|+⟩` is uniformly random and never recorded (`a` is measured in X), and it is *fresh each round*,
so it does not cancel in `m_b(r) + m_b(r-1)` either. Hence **`c_Z(a,b)` must be even for every
pair**, and this is necessary as well as sufficient for the standard per-check detectors.

*X-ancilla side.* Dually, `X_a` picks up `X_b` once for each shared `q` with `t(q→b) < t(a→q)`;
`X_b` on a fresh `|0⟩` is random. So `c_X(a,b) = #{q : t(q→b) < t(a→q)}` must be even.

*Equivalence.* `c_X(a,b) + c_Z(a,b) = |supp(a) ∩ supp(b)|`, even by CSS commutation. So the two
forms are the same condition — **one condition per (X-check, Z-check) pair.** The node's stated
form is the X-ancilla one; mine is the Z-ancilla one; they are equivalent. Non-interleaved
schedules satisfy it trivially (all counts 0 or `|overlap|`).

**Independent validation against `stim`.** Over **every** legal `[[4,2,2]]` schedule of depth 5, 6
and 7 with the fixed within-check orders (524 schedules), my predicate agrees with
`stim.Circuit.detector_error_model()` succeeding/raising, in **both** memory sectors:

```
(MC) predicate vs stim determinism, depth 5-7 [[4,2,2]]: agree 524  disagree 0
   breakdown (mine, stimZ, stimX): {(False, False, False): 319, (True, True, True): 205}
```

**Verdict 1(a): CONFIRM.** The constraint is correct as a characterisation of deterministic
detectors under the standard per-check detector convention, and the two published phrasings are
equivalent. *This is a VALUE verification plus an independently derived proof; I did not audit the
proposer's printed derivation line by line, but I re-derived the same statement and it is correct.*

### 1.2 The repaired witnesses (3 of 176)

Schedule space: X order `a = [0,1,2,3]`, Z order `b = [2,0,1,3]` fixed; each check's four CNOTs get
strictly increasing slots; `t(a→q) ≠ t(q→b)` for each data qubit; depth = 1 + max slot.
Reproducing the proposer's denominators exactly:

```
depth 5: MC-consistent 2    d_circ hist {1: 2}
depth 6: MC-consistent 27   d_circ hist {1: 27}
depth 7: MC-consistent 176  d_circ hist {1: 173, 2: 3}
depth 8: MC-consistent 769  d_circ hist {1: 743, 2: 26}
```

(2 / 27 / 176 / 769 and 173+3 / 743+26 all match the artifact's §7 table.) The three depth-7
witnesses I find are

| xslot | zslot | interleaved | `d_eff` (Z-mem) | `d_circ` (Z-mem, R = 2,3,4,5) | `d_eff` (X-mem) | `d_circ` (X-mem) |
|---|---|---|---|---|---|---|
| `[0,3,4,5]` | `[0,1,2,6]` | yes | 1 | **2,2,2,2** | 1 | **2,2,2,2** |
| `[2,3,4,5]` | `[0,1,4,6]` | yes | 1 | **2,2,2,2** | 1 | 1,1,1,1 |
| `[2,3,4,5]` | `[0,1,5,6]` | yes | 1 | **2,2,2,2** | 1 | 1,1,1,1 |

The first is exactly the explicit witness printed in §7 of the d3-gate artifact. All 176 are
interleaved (4 + 4 slots cannot separate inside 7 layers), so "3 of the 176 … interleaved" is
correct. Residual set in every case
`{0},{1},{2},{3},{2,3},{1,2,3},{0,1,2,3}` with the weight-1 effective logical `{2,3}` → `d_eff = 1`.

**Non-interleaved partners with identical within-check orders** (X block `t0..t3`, Z block `t4..t7`,
and the mirror): `d_eff = 1`, identical residual set, `d_circ = 1` at `R = 2,3,4,5`, both sectors,
`stim` DEM builds. Weight-1 certificate `('cnot', round 0, step 1, gate 0, 'XI')` — an X on the
X-ancilla after its second CNOT.

`stim` cross-check of the first witness, my own circuit build, all four `R`:

```
witness R=2..5, faults {X on Z-ancilla at prep} + {X on X-ancilla after step 3}:
   detectors fired = 0, observable = 1     (all four R)
brute force over every single-location Pauli fault, R=3, Z-memory:
   witness circuit                : 0 weight-1 undetectable logicals
   non-interleaved partner        : 6 weight-1 undetectable logicals
```

**Verdict 1(b): CONFIRM** (VALUE — independent construction agrees, in two implementations).

**Bonus finding.** The first witness lifts **both** sectors (`d_circ = 2` in X-memory too), which is
stronger than the artifact's §9 limitation 6 ("tracks the `Z₀Z₂` observable only") records.

### 1.3 The retracted depth-5 circuit

X order `q₀q₁q₂q₃` at `t1..t4`, Z order `q₂q₀q₁q₃` at `t2..t5`:

```
MC counts (c_Z, c_X, |overlap|) = (3, 1, 4)   ->  ODD, (MC) violated
   q0: t(a->q)=1 t(q->b)=3 ;  q1: 2,4 ;  q2: 3,2 ;  q3: 4,5
stim, R=2 and R=3, Z-memory:  "The circuit contains non-deterministic detectors."
```

My `c_Z = 3` and the artifact's `c_X = 1` are both odd and sum to `|overlap| = 4`, as my derivation
predicts. **Verdict 1(c): CONFIRM** — the retraction was correct.

### 1.4 Discrepancy found: the schedule space admits empty time layers

The denominators 2 / 27 / 176 / 769 are reproduced **only** if a "depth-`D`" schedule is allowed to
leave some of the `D` layers empty (the constraint used is `max slot = D − 1`, not "all `D` layers
occupied"). The 公共定义 says 「无意义的空闲层应当压缩掉」. With empty layers excluded, my counts are:

| depth | MC-consistent, empty layers allowed (proposer) | MC-consistent, no empty layer (公共定义) |
|---|---|---|
| 5 | 2 | 2 |
| 6 | 27 | 17 |
| 7 | **176** | **44** |
| 8 | 769 | 34 |

All **3** depth-7 witnesses have no empty layer, so the witnesses themselves are unaffected and the
claim survives verbatim except for the denominator. At depth 8 only **5** of the 26 witnesses have
no empty layer. Recommendation: state the schedule-space convention explicitly wherever a fraction
("3 of the 176", "26 of the 769") is cashed, or recompute under the compressed-layer convention.
This is a **presentation/scope** defect, not a numerical error.

## 2. Item 2 — Steane `[[7,1,3]]`

Code re-verified independently: all X/Z checks commute, logicals commute with the checks and
anticommute with each other, minimum non-trivial logical weight = 3 by exhaustive support search,
in both sectors.

`M_IL` (the artifact's §5.2 schedule, depth 8) is legal and (MC)-consistent — my per-pair counts:

```
(cZ, cX, |overlap|) over the nine (X-check, Z-check) pairs:
 (0,0) (2,2,4)  (0,1) (2,0,2)  (0,2) (2,0,2)
 (1,0) (0,2,2)  (1,1) (2,2,4)  (1,2) (0,2,2)
 (2,0) (2,0,2)  (2,1) (2,0,2)  (2,2) (2,2,4)     -> all even, valid
```

**`M_NI` is my own construction**, not the artifact's: same within-check orders, X block greedily
packed into `t0..t4`, Z block into `t5..t9`, depth 10, legal, (MC)-consistent, non-interleaved.

| schedule | sector | `d_eff` | `d_circ`, `R = 2,3,4,5` | DEM columns / detectors, `R = 2..5` | `stim` |
|---|---|---|---|---|---|
| `M_IL` | **Z-memory** | 2 | **3, 3, 3, 3** | 149/12, 285/18, 421/24, 557/30 | deterministic |
| `M_IL` | X-memory | 2 | 2, 2, 2, 2 | 148/12, 285/18, 422/24, 559/30 | deterministic |
| `M_NI` (mine) | Z-memory | 2 | **2, 2, 2, 2** | 149/12, 281/18, 413/24, 545/30 | deterministic |
| `M_NI` (mine) | X-memory | 2 | 2, 2, 2, 2 | 146/12, 278/18, 410/24, 542/30 | deterministic |

The Z-memory column counts **149 / 285 / 421 / 557** and detector counts **12 / 18 / 24 / 30** match
the artifact's §5.2 table exactly. The residual sets are identical between `M_IL` and `M_NI` in both
sectors, and are exactly the printed set
`{0}…{6}, {0,6}, {2,6}, {4,5}, {0,2,6}, {2,5,6}, {3,4,5}, {0,2,4,6}, {1,2,5,6}, {3,4,5,6}` for the
Z sector. `d_eff = 2` from `{2} ⊕ {4,5}` (Z-mem) and `{0} ⊕ {5,6}` (X-mem).

The `d_circ = 3` determination is exact: my enumeration finds **no** weight-≤2 undetectable logical
and exhibits a weight-3 one, and `d_circ ≤ d = 3` always. A weight-3 certificate at `R = 3`:
`('prep', round 0, Z-ancilla 10, 'X')`, `('cnot', 0, step 0, gate 3, 'XX')`, `('cnot', 0, step 1,
gate 0, 'XI')`.

**Regime completeness (7b).** The X-memory sector of `M_IL` gives `d_circ = 2`, so
`min(d_circ^Z, d_circ^X) = 2` for that circuit. The node claim is explicitly per-sector ("R = 2..5,
Z memory sector") and is therefore correctly stated; the artifact's §5.2 honest-scope note is
accurate.

**Cross-validation of my two implementations.** Every single-qubit Pauli fault at every
(round, step, pre/post) location, detector mask **and** observable bit compared between my F₂
propagator and my `stim` build:

```
Steane M_IL: Z-mem 1872/1872 agree, X-mem 1872/1872 agree
Steane M_NI: Z-mem 2340/2340 agree, X-mem 2340/2340 agree
[[4,2,2]] witness: Z-mem 756/756, X-mem 756/756      (9 936 columns, 0 disagreements)
```

**Verdict item 2: CONFIRM** (VALUE — independent enumeration at weight ≤ 3 agrees, in two
implementations, with an independently built non-interleaved partner).

## 3. Item 3 — Gross code `[[144,12,12]]`

### 3.1 The code, rebuilt from scratch

`G = Z₁₂ × Z₆`, `g = 6i + j`; `A = {x³, y, y²}`, `B = {y³, x, x²}`; incidences as in the G1
artifact's table (X-check `g`: left `g − A_i`, right `72 + (g − B_i)`; Z-check `g`: left `g + B_i`,
right `72 + (g + A_i)`). My verification:

```
HX HZ^T == 0 : True
rank HX = 66   rank HZ = 66   k = 144 - 66 - 66 = 12
row weights: {6}     column weights: {3}
X/Z check overlap histogram over all 72x72 pairs: {0: 4536, 2: 648}   (max overlap 2)
all-ones in rowspace(HX): True   in rowspace(HZ): True
randomised ISD over ker(HX) and ker(HZ): minimum non-stabiliser weight found = 12 (both sectors)
```

All of these match the G1 artifact's §1/§2.1 output.

### 3.2 The weight-6 fault set — value confirmed exactly

Schedule `P = {1,3,5}`, `α = (1,3,5)`, `β = (2,4,6)`, `γ = (2,6,4)`, `δ = (5,1,3)`; legality checked
directly on the literal 864-CNOT circuit (each of the 288 qubits in exactly one gate in each of the
6 layers; the CNOT set of every one of the 144 checks equals its `H_X`/`H_Z` support).

Fault set: Z on the ancilla of Z-checks `1, 15, 29, 37, 51, 65`, each born between CNOT layers 2 and
3 (so it deposits on the suffix `S₃`). Full multi-round X-memory simulation with my own propagator:

```
R=1: |F|=6  detectors=144  fired=0  |E|=24  E in ker(HX)=True  E in rowspace(HZ)=False -> logical
R=2: |F|=6  detectors=216  fired=0  |E|=24  ...  -> nontrivial logical
R=3: |F|=6  detectors=288  fired=0  |E|=24  ...  -> nontrivial logical
R=4: |F|=6  detectors=360  fired=0  |E|=24  ...  -> nontrivial logical
per-detector breakdown at R=3: round-0 0, round-1 0, round-2 (fault round) 0, terminal 0
supp(E) = [5,7,13,21,27,35,41,43,49,57,63,71,75,83,89,91,97,105,111,119,125,127,133,141]
        = the disjoint union of the six S_3, all 24 distinct
controls: dropping one fault -> 8 detectors fire; shifting to boundary 4 -> 18 fire
```

Stabiliser-equivalence check (rule 7e): "non-trivial logical" is `E ∈ ker(H_X) \ rowspace(H_Z)`,
tested by RREF membership, not by an observable heuristic. **Every claimed number reproduces: 6
faults, silent round detectors, silent final detectors, `|E| = 24`, non-trivial.**

**Verdict 3a: CONFIRM** (VALUE — my own simulator, my own code build, exact agreement).

### 3.3 THE BREAK — the named schedule is not a valid syndrome-extraction circuit

Applying the **same** (MC) constraint that the sibling node `CIRCDIST.lift` established on the same
day, to the same class of circuits:

```
(MC)-violating (X-check, Z-check) pairs, out of the 648 overlapping pairs:
  bucket-6   P={1,3,5} a=(1,3,5) b=(2,4,6) g=(2,6,4) d=(5,1,3) :  360 / 648   INVALID
  bucket-8   P={1,2,3} a=(1,2,3) b=(4,5,6) g=(6,4,5) d=(2,1,3) :  648 / 648   INVALID
  bucket-12  P={1,2,5} a=(1,2,5) b=(3,6,4) g=(3,6,4) d=(1,2,5) :  648 / 648   INVALID
  LRC        P={1,2,3} a=(1,2,3) b=(4,5,6) g=(4,5,6) d=(1,2,3) :  648 / 648   INVALID

exhaustive over the whole class:  0 of 25 920 TI minimum-depth schedules satisfy (MC).
```

**Proof (mine), not merely numerics.** For an overlapping pair (X-check `g`, Z-check `h`), the
shared qubits are those with `g − h = A_i + B_j` (a **left** qubit) and `g − h = A_{j'} + B_{i'}`
(a **right** qubit); since the overlap is 2 and the two counts are equal, the representation is
unique and `(j', i') = (i, j)`. The left qubit is touched by `g` at layer `α_i` and by `h` at layer
`γ_j`; the right qubit at `β_j` and `δ_i`. So the (MC) count for that pair is

```
    [ α_i < γ_j ] + [ β_j < δ_i ] .
```

Summing over all nine `(i,j)` and using `image(α) = image(δ) = P`, `image(β) = image(γ) = P̄`:

```
    Σ_{i,j} [α_i < γ_j] + Σ_{i,j} [β_j < δ_i]
      = |{(p,q) ∈ P × P̄ : p < q}| + |{(q,p) ∈ P̄ × P : q < p}|
      = |P × P̄| = 9 ,   which is ODD.
```

Nine parities summing to an odd number cannot all be even. **Hence no translation-invariant
minimum-depth Gross schedule satisfies (MC).** (The identity was checked for all 20 choices of `P`;
the per-pair predicate was validated against the literal 72 × 72 computation on 12 random
schedules, 0 mismatches.)

**Independent confirmation with `stim`**, my own circuit build, `R = 2`, both memory sectors:

```
bucket-6 / bucket-8 / bucket-12 / LRC, X-memory and Z-memory : stim REFUSES,
   "The circuit contains non-deterministic detectors."         (8/8)
10 further random TI schedules : 10/10 refused.

Direct sampling (200 noiseless shots, no detectors involved):
  bucket-6 TI : m_e(1) XOR m_e(0) is NOT constant for 72/72 X-checks;
                the round-0 X-check outcome is not constant for 72/72 checks.
```

**Positive control** — the same detector definitions on a genuinely non-interleaved Gross schedule
(all X-CNOTs in layers 1–6, all Z-CNOTs in layers 7–12, depth 12, legal):

```
(MC)-violating pairs: 0 ;  stim: DEM BUILT in both sectors ;
m_e(1) XOR m_e(0) constant for 72/72 checks ; round-0 outcome constant for 72/72.
```

So the refusal is a property of the circuits, not of my detector bookkeeping.

**Consequence.** Every circuit-level number in the G1 sweep is computed on circuits whose detectors
are non-deterministic — the *exact* failure mode for which the sibling session retracted the depth-5
`[[4,2,2]]` witness the same day, and which that artifact's own §2 warns about: "Any future session
computing circuit distance for interleaved schedules must impose (MC) or its numbers are
meaningless." Specifically invalidated as circuit-distance statements:

* the histogram `6/8/9/10/11/12 = 360/6408/2324/9232/6068/1528`;
* "70.7 % of translation-invariant minimum-depth schedules admit a weight-≤10 witness, 26.1 % ≤ 8"
  (node `assessment.summary`);
* "only 15.6 % of TI schedules let the cheapest timing-free skeleton close" and the `(r, c)` joint
  table;
* "1 528 schedules certify at 12 … the only candidates in the class for `d_circ = 12`";
* the §7 "fully verified weight-8 witness on a **non-interleaved** schedule".

**Verdict 3b: REFUTE**, as a statement about `d_circ` for a legal syndrome-extraction circuit.

**Secondary terminology defect.** "Non-interleaved (LRC-like) ⟺ `P ∈ {{1,2,3},{4,5,6}}`" is a
misnomer. In the whole TI minimum-depth class, `σ(X→left) = P` forces `σ(X→right) = P̄`,
`σ(Z→left) = P̄`, `σ(Z→right) = P`, so X-check and Z-check CNOTs coexist in **every one of the six
layers** for every member. No member is non-interleaved in the sense used by the lift artifact
(X block, then Z block). Since a weight-6 check needs six slots of its own, a genuinely
non-interleaved Gross schedule needs depth ≥ 12, and none exists in the minimum-depth class.

### 3.4 The repair — the multi-hook mechanism survives on a valid circuit

The break is about the *schedule*, not about the *mechanism*. Because `E(M)` depends only on the
within-check CNOT orders, I rebuilt the witness on an (MC)-valid schedule: same within-check orders
as the bucket-6 schedule, X block at layers 1–6 (`α = (1,3,5)`, `β = (2,4,6)`), Z block at layers
7–12 (`γ = (8,12,10)`, `δ = (11,7,9)`), depth 12, no empty layer, legal.

```
legal: True ;  (MC)-violating pairs: 0 ;  stim: DEM BUILT in BOTH sectors
within-check X and Z orders identical to the TI bucket-6 schedule for all 144 checks: True
same six hook faults (now born between the 2nd and 3rd Z-CNOT, i.e. at layer 9):
  R=2: |F|=6 detectors=216 fired=0 |E|=24 ker=True stabiliser=False -> undetectable logical
  R=3: |F|=6 detectors=288 fired=0 |E|=24 ...                        -> undetectable logical
  R=4: |F|=6 detectors=360 fired=0 |E|=24 ...                        -> undetectable logical
net error identical to the TI witness: True
```

And the `d_ext` reading needs no detectors at all: the six residuals

```
S_3(1)  = {75,13,91,7}      S_3(15) = {89,27,105,21}    S_3(29) = {97,41,119,35}
S_3(37) = {111,49,127,43}   S_3(51) = {125,63,141,57}   S_3(65) = {133,5,83,71}
```

are six distinct elements of `E(M)`, their product has weight 24, zero X-syndrome, and is not a
stabiliser. So `d_ext(E(M)) ≤ 6 < 10` for a **valid** schedule.

**Verdict 3c: CONFIRM after repair.** The multi-hook mechanism is real, the cap `|L ∩ supp(c)| ≤ 3`
is confirmed on the pool (histogram `{0: 1191, 1: 496, 2: 145, 3: 52}` against a fixed Z-check —
never 4, 5 or 6), and the refutation of the dropped `d_ext ∈ {10,11,12}` clause stands. What must
change is the *named witness schedule*: the node currently cites an invalid circuit. It also follows
that some **legal, valid, non-interleaved** Gross schedules have `d_circ ≤ 6` — far below the
published `≤ 11` upper bounds, with which this is consistent (those are upper bounds, and the
conjectured distance-11 circuit is three-colour tiled and outside this family).

### 3.5 The surviving universal claim `d_ext(E(M)) ≤ 11`

My own randomised ISD over `ker(H_X)` / `ker(H_Z)`, closed under the 72 translations (verified to be
code automorphisms by the incidence relabelling `g ↦ g + t`):

```
[Z] raw ISD hits <=12: 1493, min weight found 12, weight-12: 1493, after translations: 1884
[X] raw ISD hits <=12: 1544, min weight found 12, weight-12: 1544, after translations: 1884
```

The pool size **1884 per sector** matches the recon and G1 independently. Six random
(sector, check, pair) choices, each yielding an explicit weight-12 logical containing the pair,
verified to have weight exactly 12, zero syndrome, and to be outside the stabiliser row space:

| sector | check | support | pair | witness `L` |
|---|---|---|---|---|
| Z | 41 | `[38,47,53,108,109,131]` | `(47,108)` | `[7,24,25,47,62,63,96,105,108,111,117,123]` |
| Z | 6 | `[9,12,18,79,80,96]` | `(9,80)` | `[0,1,2,3,7,9,74,76,78,80,85,87]` |
| Z | 12 | `[15,18,24,85,86,102]` | `(24,86)` | `[2,16,24,38,52,60,72,86,100,108,122,136]` |
| X | 7 | `[6,11,61,73,82,139]` | `(11,82)` | `[0,2,6,7,8,11,68,70,74,76,78,82]` |
| X | 4 | `[2,3,58,73,136,142]` | `(2,73)` | `[0,1,2,3,9,10,63,67,69,73,80,141]` |
| X | 53 | `[35,51,52,113,119,122]` | `(35,51)` | `[3,35,44,51,59,68,90,112,119,136,138,143]` |

Full coverage on one check of each type: **15/15 pairs covered**, both sectors.

The argument, restated in my own words: for **any** schedule `M` and any Z-check `c` with CNOT order
`i₁…i₆`, a single Z fault on `c`'s ancilla between its 4th and 5th CNOT deposits Z on exactly
`{i₅, i₆} ⊆ supp(c)`, so `{i₅,i₆} ∈ E(M)`; all 15 pairs of `supp(c)` lie in some weight-12 logical
`L`; `E(M)` also contains every singleton; so `{i₅,i₆}` together with the 10 singletons of
`L \ {i₅,i₆}` is an extended-code codeword of **11 residuals** with zero syndrome and non-trivial
logical action. Dual for X-checks. Hence `d_ext(E(M)) ≤ 11` for every legal `M`, interleaved or not.

Note this argument is a `d_ext` statement and needs **no** detector determinism, so it is untouched
by §3.3. **Verdict 3d: CONFIRM** (VALUE, plus a line-by-line check of the printed argument, which
is sound).

## 4. Item 4 — spot-checks

### 4a. Three G1 histogram buckets, verified end-to-end with my own simulator

| bucket | schedule | fault set | my result |
|---|---|---|---|
| **6** | `P={1,3,5}, α=(1,3,5), β=(2,4,6), γ=(2,6,4), δ=(5,1,3)` | 6 hooks at boundary 3 | 288 detectors, 0 fired, `\|E\|=24`, non-trivial logical ✔ |
| **8** | `P={1,2,3}, α=(1,2,3), β=(4,5,6), γ=(6,4,5), δ=(2,1,3)` | 4 hooks at boundary 5 on Z-checks 4,20,37,59 + Z on data 78,102,117,141 after layer 6 | 288 detectors, 0 fired, `\|E\|=12`, non-trivial logical ✔ |
| **12** | `P={1,2,5}, α=(1,2,5), β=(3,6,4), γ=(3,6,4), δ=(1,2,5)` | 12 data faults born after layer 6 on the weight-12 logical `[0,1,2,3,4,5,18,21,90,93,96,99]` | 288 detectors, 0 fired, `\|E\|=12`, non-trivial logical ✔ |

Controls: the same 12 data faults born *before* layer 6 fire 8 detectors; the bucket-6 six-hook set
transplanted onto the bucket-12 schedule fires 36. All three claimed witness weights are correct
**as fault sets**. They inherit the §3.3 break as circuit-distance statements. I did **not**
re-enumerate the absence side ("no smaller witness in `W`") for the bucket-12 schedule — that is
**NOT-REVIEWED**.

### 4b. The `d_circ = min_γ(|γ| + repair(γ))` formula

I derived the repair cost independently before checking. A weight-1 fault in round `r` flips that
round's primary outcomes by `u` and leaves residual `E` with syndrome `s`, which then flips every
later round; with `D_g(r') = m_g(r') + m_g(r'-1)` this gives `D(r) = u`, `D(r+1) = u + s`, nothing
after — i.e. the chain `x^r(u(1+x) + s x)`. For `γ` with `Σ s_i = 0`, `B = Σ s_i x^{r_i} = (1+x)C`,
total `= (1+x)(A + xC)` with `A = Σ u_i x^{r_i}`; a measurement flip adds one monomial to `A` at
cost 1, so `repair(γ) = min wt(A + xC)`. For `|γ| = 1` with `s = 0`: `|u₁|`. For `|γ| = 2` with
`s₁ = s₂ = s` and round gap `k`: `k=0 → |u₁ ⊕ u₂|`, `k=1 → |u₁| + |u₂ ⊕ s|` (and mirror),
`k≥2 → |u₁| + (k−1)|s| + |u₂ ⊕ s|`. This matches §6.1 of the artifact; I flag the coincidence.
`U(E)` is read off my one-round fault enumeration; **no multi-round circuit is built** by the
predictor.

| schedule | sector | `d_eff` | predicted `min_γ ℓ(γ)` | exhaustive `d_circ` (R=3) | agree | minimising `γ` |
|---|---|---|---|---|---|---|
| Steane `M_IL` (d8) | Z | 2 | **3** | **3** | ✔ | `{X₃} ⊕ hook{2,6}`, repair 1 |
| Steane `M_IL` | X | 2 | 2 | 2 | ✔ | `{X₀} ⊕ hook{5,6}`, repair 0 |
| Steane `M_NI` (d10, mine) | Z | 2 | 2 | 2 | ✔ | `{X₂} ⊕ hook{4,5}`, repair 0 |
| Steane `M_NI` | X | 2 | 2 | 2 | ✔ | `{X₀} ⊕ hook{5,6}`, repair 0 |
| `[[4,2,2]]` IL witness (d7) | Z | 1 | 2 | 2 | ✔ | `hook{2,3}`, repair 1 |
| `[[4,2,2]]` IL witness | X | 1 | 2 | 2 | ✔ | `hook{1,3}`, repair 1 |
| `[[4,2,2]]` NI partner (d8) | Z | 1 | 1 | 1 | ✔ | `hook{2,3}`, repair 0 |
| `[[4,2,2]]` NI partner | X | 1 | 1 | 1 | ✔ | `hook{1,3}`, repair 0 |

**8 / 8 agreement**, including the sign of the gap. The Steane `M_IL` Z-memory minimiser is exactly
the artifact's §6.2 row. **Verdict 4b: CONFIRM** (VALUE; the bulk 5129/5129 agreement figure was
**NOT-REVIEWED** — I checked 4 schedules × 2 sectors, not the full families).

## 5. Standing failure modes checked (rule 7e)

* **Time-index off-by-one.** Hook residuals were cross-checked two ways: analytically (suffix of the
  check's CNOT order) and by forward propagation. For the Gross witness the union of the six
  analytic `S₃` sets equals `supp(E)` from the simulator exactly. Controls that shift the fault by
  one layer boundary fire detectors (18 for the Gross witness), so the boundary is not slack.
* **X/Z sector swaps.** Every claim is computed in **both** memory sectors and reported separately;
  the Gross `d_ext ≤ 11` argument is checked for both check types.
* **Parity conventions.** The (MC) count was computed in both directions (`c_X`, `c_Z`) and their
  sum verified equal to `|overlap|` in every printed case.
* **Silently accepting invalid circuits.** This is exactly the break in §3.3 — found by applying the
  lift node's own validity predicate, then confirmed by `stim`'s DEM refusal *and* by direct
  sampling of the noiseless circuit, with a passing positive control.
* **Stabiliser-equivalence errors.** "Non-trivial logical" is always `E ∈ ker(H_det) \
  rowspace(H_stab)` via RREF membership, never an observable heuristic.
* **Single-implementation risk.** 9 936 DEM columns compared between my F₂ propagator and my `stim`
  build, 0 disagreements.

## 6. What is NOT reviewed

* The rotated `d = 3` surface-code arm of the d3-gate artifact (§4) — **NOT-REVIEWED**.
* The bulk agreement figure 5129/5129 (§6.3) beyond the 4 schedules of §4b — **NOT-REVIEWED**.
* Conjectures 3.1 / 3.2 (overlap-4 / containment) and their tables — **NOT-REVIEWED**.
* Completeness of the weight-12 logical pool (upper-bound witnesses are one-sided, so this cannot
  invalidate `d_ext ≤ 11`) — **NOT-REVIEWED**, and the G1 artifact already labels it as such.
* The absence side of the G1 sweep ("no smaller witness in `W`") for any bucket — **NOT-REVIEWED**.
* Whether the Gross code's minimum distance really is 12 — I verified `k = 12` and that randomised
  ISD finds nothing below weight 12, which is evidence, not proof.
* `CIRCDIST.cplx` and `CIRCDIST.sat` — out of scope.

## 7. Code

All of the above is reproducible from the following. Nothing here is derived from proposer code.
`rev.py` / `stimgen.py` / `xval.py` cover items 1, 2 and 4b; `gross_rev.py` and the `item3*` /
`item4a` scripts cover item 3 and 4a.

### `rev.py`

```python
"""Independent reviewer's F2 stabilizer-circuit fault propagator.

Written from scratch for the 2026-08-20 review. No proposer code reused.

Conventions (mine):
  qubit indices 0..n-1  = data
                n..     = ancillas, one per check, in the order checks are listed
  Pauli error state = (x, z) as python ints (bitmasks over all N qubits)
  CNOT(c,t) forward propagation of an error:  x_t ^= x_c ;  z_c ^= z_t
  X-check ancilla: prep |+>, is CONTROL of CNOT(anc -> q), measured in X
                   -> its recorded outcome is flipped by a Z error on the ancilla
  Z-check ancilla: prep |0>, is TARGET of CNOT(q -> anc), measured in Z
                   -> its recorded outcome is flipped by an X error on the ancilla
"""
import itertools
from functools import lru_cache


# ---------------------------------------------------------------- code container
class Code:
    def __init__(self, n, xchecks, zchecks, zl, xl):
        self.n = n
        self.xchecks = [sorted(s) for s in xchecks]   # supports (data indices)
        self.zchecks = [sorted(s) for s in zchecks]
        self.zl = sorted(zl)   # Z logical support
        self.xl = sorted(xl)   # X logical support
        self.mx = len(xchecks)
        self.mz = len(zchecks)
        self.N = n + self.mx + self.mz

    def xanc(self, i):
        return self.n + i

    def zanc(self, j):
        return self.n + self.mx + j

    def check_valid(self):
        """all X/Z checks commute; logicals commute with checks, anticommute w/ each other"""
        ok = True
        for a in self.xchecks:
            for b in self.zchecks:
                if len(set(a) & set(b)) % 2:
                    ok = False
        for a in self.xchecks:
            if len(set(a) & set(self.zl)) % 2:
                ok = False
        for b in self.zchecks:
            if len(set(b) & set(self.xl)) % 2:
                ok = False
        if len(set(self.xl) & set(self.zl)) % 2 == 0:
            ok = False
        return ok


# ---------------------------------------------------------------- schedule
class Schedule:
    """
    xorder[i]  : list of data qubits, the order X-check i touches them
    xslot[i]   : list of time slots (strictly increasing), same length
    zorder[j], zslot[j] : same for Z-check j (data qubit is the CONTROL)
    """
    def __init__(self, code, xorder, xslot, zorder, zslot):
        self.code = code
        self.xorder, self.xslot = xorder, xslot
        self.zorder, self.zslot = zorder, zslot
        self.depth = 1 + max([t for s in xslot for t in s] + [t for s in zslot for t in s])
        # build per-step gate list: (control, target, tag)
        steps = [[] for _ in range(self.depth)]
        for i, (o, s) in enumerate(zip(xorder, xslot)):
            for q, t in zip(o, s):
                steps[t].append((code.xanc(i), q, ('X', i, q)))
        for j, (o, s) in enumerate(zip(zorder, zslot)):
            for q, t in zip(o, s):
                steps[t].append((q, code.zanc(j), ('Z', j, q)))
        self.steps = steps

    def is_legal(self):
        for t, gs in enumerate(self.steps):
            used = set()
            for c, tg, _ in gs:
                if c in used or tg in used:
                    return False
                used.add(c)
                used.add(tg)
        for t, gs in enumerate(self.steps):
            if not gs:
                return False   # no empty (compressible) layers
        # within-check slots strictly increasing
        for s in self.xslot + self.zslot:
            if any(s[k] >= s[k + 1] for k in range(len(s) - 1)):
                return False
        return True

    def t_xq(self, i, q):
        return self.xslot[i][self.xorder[i].index(q)]

    def t_qz(self, j, q):
        return self.zslot[j][self.zorder[j].index(q)]

    def mc_counts(self):
        """my (MC) predicate, derived independently: for every (X-check a, Z-check b),
           #{q in supp(a)&supp(b) : t(a->q) < t(q->b)}  must be EVEN.
           (equivalently the complementary count, since |supp(a)&supp(b)| is even)"""
        out = {}
        for i, a in enumerate(self.code.xchecks):
            for j, b in enumerate(self.code.zchecks):
                sh = sorted(set(a) & set(b))
                cZ = sum(1 for q in sh if self.t_xq(i, q) < self.t_qz(j, q))
                cX = sum(1 for q in sh if self.t_qz(j, q) < self.t_xq(i, q))
                out[(i, j)] = (cZ, cX, len(sh))
        return out

    def is_mc(self):
        return all(c[0] % 2 == 0 for c in self.mc_counts().values())

    def is_interleaved(self):
        xt = [t for s in self.xslot for t in s]
        zt = [t for s in self.zslot for t in s]
        return not (max(xt) < min(zt) or max(zt) < min(xt))


# ---------------------------------------------------------------- propagation
def popcount_mask(v, support):
    return sum((v >> q) & 1 for q in support) % 2


class Sim:
    """Forward F2 propagation of a single elementary fault through R rounds."""

    def __init__(self, sched, R, sector):
        self.s = sched
        self.c = sched.code
        self.R = R
        self.sector = sector    # 'Z' = Z-memory (|0>^n init, Z readout), 'X' = X-memory

    # -- one full run given a fault (round r0, kind, ...) ------------------
    def run(self, fault):
        c, s = self.c, self.s
        x = z = 0
        meas = {}                       # (kind,idx,round) -> recorded bit
        kind = fault[0]
        for r in range(self.R):
            # ancilla prep: errors reset
            for i in range(c.mx):
                b = c.xanc(i)
                x &= ~(1 << b); z &= ~(1 << b)
            for j in range(c.mz):
                b = c.zanc(j)
                x &= ~(1 << b); z &= ~(1 << b)
            if kind == 'prep' and fault[1] == r:
                _, _, q, p = fault
                if p in 'XY': x ^= 1 << q
                if p in 'ZY': z ^= 1 << q
            for t in range(s.depth):
                # idle faults happen at the START of step t on qubits not in a gate
                if kind == 'idle' and fault[1] == r and fault[2] == t:
                    _, _, _, q, p = fault
                    if p in 'XY': x ^= 1 << q
                    if p in 'ZY': z ^= 1 << q
                # generic single-qubit fault, 'pre' = before the step's gates
                if kind == 'sq' and fault[1] == r and fault[2] == t and fault[3] == 'pre':
                    q, p = fault[4], fault[5]
                    if p in 'XY': x ^= 1 << q
                    if p in 'ZY': z ^= 1 << q
                for gi, (cc, tt, tag) in enumerate(s.steps[t]):
                    # propagate through the CNOT
                    if (x >> cc) & 1: x ^= 1 << tt
                    if (z >> tt) & 1: z ^= 1 << cc
                    if kind == 'cnot' and fault[1] == r and fault[2] == t and fault[3] == gi:
                        p = fault[4]           # 2-char string, on (control, target)
                        if p[0] in 'XY': x ^= 1 << cc
                        if p[0] in 'ZY': z ^= 1 << cc
                        if p[1] in 'XY': x ^= 1 << tt
                        if p[1] in 'ZY': z ^= 1 << tt
                if kind == 'sq' and fault[1] == r and fault[2] == t and fault[3] == 'post':
                    q, p = fault[4], fault[5]
                    if p in 'XY': x ^= 1 << q
                    if p in 'ZY': z ^= 1 << q
            # measurements
            for i in range(c.mx):
                b = c.xanc(i)
                meas[('X', i, r)] = (z >> b) & 1      # X-basis meas flipped by Z error
            for j in range(c.mz):
                b = c.zanc(j)
                meas[('Z', j, r)] = (x >> b) & 1      # Z-basis meas flipped by X error
            if kind == 'meas' and fault[1] == r:
                meas[fault[2]] ^= 1
        return x, z, meas

    # -- detector / observable extraction ---------------------------------
    def columns(self, fault):
        c = self.c
        x, z, meas = self.run(fault)
        det = []
        if self.sector == 'Z':
            prim, dual, err = 'Z', 'X', x
            primchecks, dualchecks = c.zchecks, c.xchecks
            obs_supp = c.zl
        else:
            prim, dual, err = 'X', 'Z', z
            primchecks, dualchecks = c.xchecks, c.zchecks
            obs_supp = c.xl
        for g in range(len(primchecks)):
            det.append(meas[(prim, g, 0)])
            for r in range(1, self.R):
                det.append(meas[(prim, g, r)] ^ meas[(prim, g, r - 1)])
            det.append(meas[(prim, g, self.R - 1)] ^ popcount_mask(err, primchecks[g]))
        for g in range(len(dualchecks)):
            for r in range(1, self.R):
                det.append(meas[(dual, g, r)] ^ meas[(dual, g, r - 1)])
        mask = 0
        for k, b in enumerate(det):
            if b:
                mask |= 1 << k
        obs = popcount_mask(err, obs_supp)
        return mask, obs, len(det)

    # -- enumerate all elementary faults ----------------------------------
    def fault_list(self):
        c, s = self.c, self.s
        F = []
        for r in range(self.R):
            for i in range(c.mx):
                for p in 'XYZ':
                    F.append(('prep', r, c.xanc(i), p))
            for j in range(c.mz):
                for p in 'XYZ':
                    F.append(('prep', r, c.zanc(j), p))
            for t in range(s.depth):
                busy = set()
                for cc, tt, _ in s.steps[t]:
                    busy.add(cc); busy.add(tt)
                for gi in range(len(s.steps[t])):
                    for p in ['II', 'IX', 'IY', 'IZ', 'XI', 'XX', 'XY', 'XZ',
                              'YI', 'YX', 'YY', 'YZ', 'ZI', 'ZX', 'ZY', 'ZZ'][1:]:
                        F.append(('cnot', r, t, gi, p))
                for q in range(c.N):
                    if q not in busy:
                        for p in 'XYZ':
                            F.append(('idle', r, t, q, p))
            for i in range(c.mx):
                F.append(('meas', r, ('X', i, r)))
            for j in range(c.mz):
                F.append(('meas', r, ('Z', j, r)))
        return F

    def dem(self):
        cols = {}
        ndet = None
        for f in self.fault_list():
            m, o, nd = self.columns(f)
            ndet = nd
            if m == 0 and o == 0:
                continue
            cols.setdefault((m, o), f)
        return cols, ndet


def d_circ(sched, R, sector, maxw=3):
    sim = Sim(sched, R, sector)
    cols, ndet = sim.dem()
    items = list(cols.items())
    # weight 1
    for (m, o), f in items:
        if m == 0 and o == 1:
            return 1, [f], len(items), ndet
    # weight 2
    by_mask = {}
    for (m, o), f in items:
        by_mask.setdefault(m, {}).setdefault(o, f)
    for m, d in by_mask.items():
        if 0 in d and 1 in d:
            return 2, [d[0], d[1]], len(items), ndet
    if maxw < 3:
        return None, None, len(items), ndet
    # weight 3: meet in the middle
    pair = {}
    for i in range(len(items)):
        (m1, o1), f1 = items[i]
        for j in range(i + 1, len(items)):
            (m2, o2), f2 = items[j]
            pair.setdefault(m1 ^ m2, []).append((o1 ^ o2, f1, f2))
    for (m, o), f in items:
        if m in pair:
            for (oo, f1, f2) in pair[m]:
                if oo ^ o == 1 and f1 != f and f2 != f:
                    return 3, [f, f1, f2], len(items), ndet
    return None, None, len(items), ndet


# ---------------------------------------------------------------- d_eff
def residual_set(sched, sector):
    """terminal residual data errors of single faults over ONE round"""
    sim = Sim(sched, 1, sector)
    c = sched.code
    out = set()
    for f in sim.fault_list():
        x, z, meas = sim.run(f)
        err = x if sector == 'Z' else z
        sup = frozenset(q for q in range(c.n) if (err >> q) & 1)
        if sup:
            out.add(sup)
    return out


def d_ext(code, residuals, sector, maxk=4):
    """min number of residuals whose product has trivial syndrome + nontrivial logical"""
    if sector == 'Z':
        checks, obs = code.zchecks, code.zl     # X errors: detected by Z checks, flip Z_L
    else:
        checks, obs = code.xchecks, code.xl
    R = sorted(residuals, key=lambda s: (len(s), sorted(s)))
    def sig(s):
        sy = 0
        for gi, g in enumerate(checks):
            if len(s & set(g)) % 2:
                sy |= 1 << gi
        return sy, len(s & set(obs)) % 2
    sigs = [sig(s) for s in R]
    for k in range(1, maxk + 1):
        for comb in itertools.combinations(range(len(R)), k):
            sy = 0; ob = 0
            for i in comb:
                sy ^= sigs[i][0]; ob ^= sigs[i][1]
            if sy == 0 and ob == 1:
                return k, [sorted(R[i]) for i in comb]
    return None, None
```

### `stimgen.py`

```python
"""Independent stim circuit builder (my own; not the proposer's stimgen.py)."""
import stim


def build(code, sched, R, sector='Z', faults=()):
    """faults: list of ('pauli', step_round, step_t, 'before'|'after', qubit, 'X'/'Y'/'Z')
                     or ('meas', round, ('X'|'Z', idx))  -> classical flip
       inserted with probability 1."""
    c, s = code, sched
    C = stim.Circuit()
    n = c.n
    xa = [c.xanc(i) for i in range(c.mx)]
    za = [c.zanc(j) for j in range(c.mz)]
    if sector == 'Z':
        C.append('R', list(range(n)))
    else:
        C.append('RX', list(range(n)))
    mi = 0                                   # measurement counter
    recs = {}
    for r in range(R):
        C.append('RX', xa)
        C.append('R', za)
        C.append('TICK')
        for t in range(s.depth):
            for f in faults:
                if f[0] == 'pauli' and f[1] == r and f[2] == t and f[3] == 'pre':
                    C.append(f'{f[5]}_ERROR', [f[4]], 1.0)
            targs = []
            for (cc, tt, tag) in s.steps[t]:
                targs += [cc, tt]
            if targs:
                C.append('CX', targs)
            # inserted faults, applied AFTER the gates of step t
            for f in faults:
                if f[0] == 'pauli' and f[1] == r and f[2] == t and f[3] == 'post':
                    C.append(f'{f[5]}_ERROR', [f[4]], 1.0)
            C.append('TICK')
        for i in range(c.mx):
            C.append('MX', [xa[i]]); recs[('X', i, r)] = mi; mi += 1
        for j in range(c.mz):
            C.append('M', [za[j]]); recs[('Z', j, r)] = mi; mi += 1
        for f in faults:
            if f[0] == 'meas' and f[1] == r:
                # emulate a classical readout flip by flipping the qubit right before meas:
                # not possible post hoc; handled by caller using a pre-measurement error.
                raise NotImplementedError
    if sector == 'Z':
        C.append('M', list(range(n)))
    else:
        C.append('MX', list(range(n)))
    for q in range(n):
        recs[('data', q)] = mi; mi += 1
    total = mi

    def rec(key):
        return stim.target_rec(recs[key] - total)

    prim = 'Z' if sector == 'Z' else 'X'
    dual = 'X' if sector == 'Z' else 'Z'
    primchecks = c.zchecks if sector == 'Z' else c.xchecks
    dualchecks = c.xchecks if sector == 'Z' else c.zchecks
    obs = c.zl if sector == 'Z' else c.xl
    for g in range(len(primchecks)):
        C.append('DETECTOR', [rec((prim, g, 0))])
        for r in range(1, R):
            C.append('DETECTOR', [rec((prim, g, r)), rec((prim, g, r - 1))])
        C.append('DETECTOR', [rec((prim, g, R - 1))] + [rec(('data', q)) for q in primchecks[g]])
    for g in range(len(dualchecks)):
        for r in range(1, R):
            C.append('DETECTOR', [rec((dual, g, r)), rec((dual, g, r - 1))])
    C.append('OBSERVABLE_INCLUDE', [rec(('data', q)) for q in obs], 0)
    return C


def deterministic(code, sched, R, sector='Z'):
    try:
        build(code, sched, R, sector).detector_error_model()
        return True
    except ValueError:
        return False
```

### `xval.py`

```python
"""Column-by-column cross-validation: my F2 propagator vs my stim circuit build."""
import sys
sys.path.insert(0, '/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from rev import Code, Schedule, Sim
from stimgen import build


def xval(code, sched, R, sector, verbose=True):
    sim = Sim(sched, R, sector)
    agree = dis = 0
    bad = []
    for r in range(R):
        for t in range(sched.depth):
            for where in ('pre', 'post'):
                for q in range(code.N):
                    for P in 'XYZ':
                        f = ('sq', r, t, where, q, P)
                        m, o, nd = sim.columns(f)
                        mine = ([(m >> k) & 1 for k in range(nd)], o)
                        ckt = build(code, sched, R, sector,
                                    faults=[('pauli', r, t, where, q, P)])
                        det, obs = ckt.compile_detector_sampler().sample(
                            1, separate_observables=True)
                        theirs = ([int(b) for b in det[0]], int(obs[0][0]))
                        if mine == theirs:
                            agree += 1
                        else:
                            dis += 1
                            bad.append((f, mine, theirs))
    if verbose:
        print(f'  {sector}-memory R={R}: agree {agree}  disagree {dis}')
        for b in bad[:3]:
            print('    MISMATCH', b)
    return agree, dis
```

### `gross_rev.py`

```python
"""Independent reviewer's Gross-code build + literal circuit simulator.
Written from scratch; no proposer code reused."""
import numpy as np
import itertools, random

L, M = 12, 6
NG = L * M          # 72
N = 2 * NG          # 144 data qubits

# group element  g = i*M + j,  i in Z_12, j in Z_6.  x = (+1,0), y = (0,+1)
def gadd(g, mono):
    i, j = divmod(g, M)
    di, dj = mono
    return ((i + di) % L) * M + (j + dj) % M

def gsub(g, mono):
    i, j = divmod(g, M)
    di, dj = mono
    return ((i - di) % L) * M + (j - dj) % M

Amon = [(3, 0), (0, 1), (0, 2)]     # x^3, y, y^2
Bmon = [(0, 3), (1, 0), (2, 0)]     # y^3, x, x^2

# --- incidences exactly as the proposer's table states them -----------------
# X-check g : left data  g - A_i ;  right data  NG + (g - B_i)
# Z-check g : left data  g + B_i ;  right data  NG + (g + A_i)
def xcheck_support(g):
    return [gsub(g, a) for a in Amon] + [NG + gsub(g, b) for b in Bmon]

def zcheck_support(g):
    return [gadd(g, b) for b in Bmon] + [NG + gadd(g, a) for a in Amon]

HX = np.zeros((NG, N), dtype=np.uint8)
HZ = np.zeros((NG, N), dtype=np.uint8)
for g in range(NG):
    for q in xcheck_support(g):
        HX[g, q] ^= 1
    for q in zcheck_support(g):
        HZ[g, q] ^= 1


# ---------------------------------------------------------------- F2 linalg
def rref(Min):
    A = Min.copy() % 2
    rows, cols = A.shape
    piv = []
    r = 0
    for c in range(cols):
        p = None
        for rr in range(r, rows):
            if A[rr, c]:
                p = rr; break
        if p is None:
            continue
        A[[r, p]] = A[[p, r]]
        for rr in range(rows):
            if rr != r and A[rr, c]:
                A[rr] ^= A[r]
        piv.append(c); r += 1
        if r == rows:
            break
    return A[:r], piv

def rank(Min):
    return rref(Min)[0].shape[0]

def in_rowspace(Rref, piv, v):
    w = v.copy() % 2
    for r, c in enumerate(piv):
        if w[c]:
            w ^= Rref[r]
    return not w.any()

def nullspace(Min):
    """basis of {v : Min v = 0} over F2"""
    R, piv = rref(Min)
    cols = Min.shape[1]
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        v = np.zeros(cols, dtype=np.uint8)
        v[f] = 1
        for r, c in enumerate(piv):
            if R[r, f]:
                v[c] = 1
        basis.append(v)
    return np.array(basis, dtype=np.uint8) if basis else np.zeros((0, cols), np.uint8)


# ---------------------------------------------------------------- schedule
class TISchedule:
    """(P, alpha, beta, gamma, delta):  alpha/delta: A-monomial index -> layer in P
                                        beta/gamma : B-monomial index -> layer in Pbar"""
    def __init__(self, P, alpha, beta, gamma, delta):
        self.P = set(P)
        self.Pbar = set(range(1, 7)) - self.P
        self.alpha, self.beta, self.gamma, self.delta = alpha, beta, gamma, delta
        assert set(alpha) == self.P and set(delta) == self.P, 'alpha,delta must land in P'
        assert set(beta) == self.Pbar and set(gamma) == self.Pbar, 'beta,gamma must land in Pbar'
        self.build()

    def build(self):
        # qubit indices in the simulator: 0..143 data, 144..215 X-anc, 216..287 Z-anc
        self.NQ = N + 2 * NG
        self.xanc = lambda g: N + g
        self.zanc = lambda g: N + NG + g
        layers = {l: [] for l in range(1, 7)}
        for g in range(NG):
            for i, a in enumerate(Amon):                     # X-check -> left
                layers[self.alpha[i]].append((self.xanc(g), gsub(g, a)))
            for i, b in enumerate(Bmon):                     # X-check -> right
                layers[self.beta[i]].append((self.xanc(g), NG + gsub(g, b)))
            for i, b in enumerate(Bmon):                     # Z-check -> left
                layers[self.gamma[i]].append((gadd(g, b), self.zanc(g)))
            for i, a in enumerate(Amon):                     # Z-check -> right
                layers[self.delta[i]].append((NG + gadd(g, a), self.zanc(g)))
        self.layers = layers

    def legality(self):
        bad = []
        for l in range(1, 7):
            used = {}
            for c, t in self.layers[l]:
                for q in (c, t):
                    used[q] = used.get(q, 0) + 1
            if any(v != 1 for v in used.values()) or len(used) != self.NQ:
                bad.append((l, len(used), max(used.values())))
        return bad

    def z_cnot_order(self, g):
        """ordered list of the data qubits Z-check g touches, layer 1..6"""
        out = [None] * 7
        for i, b in enumerate(Bmon):
            out[self.gamma[i]] = gadd(g, b)
        for i, a in enumerate(Amon):
            out[self.delta[i]] = NG + gadd(g, a)
        return out[1:]

    def x_cnot_order(self, g):
        out = [None] * 7
        for i, a in enumerate(Amon):
            out[self.alpha[i]] = gsub(g, a)
        for i, b in enumerate(Bmon):
            out[self.beta[i]] = NG + gsub(g, b)
        return out[1:]


# ---------------------------------------------------------------- Z-sector simulator
def simulate_z(sched, R, faults):
    """faults: list of ('zanc', round, check g, layer_boundary l)  meaning a Z error on the
       Z-check-g ancilla born between CNOT layers l-1 and l (so it acts from layer l onward);
       or ('data', round, qubit, l) = Z on data qubit born just before layer l  (l=7 => after all);
       or ('meas', round, X-check g) = flip of X-check g's outcome.
       Returns detector list + final data error."""
    z = np.zeros(sched.NQ, dtype=np.uint8)
    mX = {}
    for r in range(R):
        z[N:] = 0                                    # ancillas prepared fresh
        for l in range(1, 7):
            for f in faults:
                if f[0] == 'zanc' and f[1] == r and f[3] == l:
                    z[sched.zanc(f[2])] ^= 1
                if f[0] == 'data' and f[1] == r and f[3] == l:
                    z[f[2]] ^= 1
            snap = z.copy()
            for c, t in sched.layers[l]:
                z[c] ^= snap[t]                       # CNOT(c,t): z_c ^= z_t
        for f in faults:
            if f[0] == 'data' and f[1] == r and f[3] == 7:
                z[f[2]] ^= 1
        for g in range(NG):
            mX[(g, r)] = int(z[sched.xanc(g)])
        for f in faults:
            if f[0] == 'meas' and f[1] == r:
                mX[(f[2], r)] ^= 1
    E = z[:N].copy()
    det = []
    for g in range(NG):
        det.append(mX[(g, 0)])
        for r in range(1, R):
            det.append(mX[(g, r)] ^ mX[(g, r - 1)])
        det.append(mX[(g, R - 1)] ^ int((HX[g] & E).sum() % 2))
    return np.array(det, dtype=np.uint8), E
```

### `item1_full.py`

```python
import itertools, sys
sys.path.insert(0, '/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from rev import Code, Schedule, d_circ, residual_set, d_ext

C = Code(4, [[0, 1, 2, 3]], [[0, 1, 2, 3]], zl=[0, 2], xl=[0, 1])
XO = [0, 1, 2, 3]; ZO = [2, 0, 1, 3]

def build(xs, zs):
    s = Schedule.__new__(Schedule)
    s.code = C; s.xorder = [XO]; s.xslot = [list(xs)]
    s.zorder = [ZO]; s.zslot = [list(zs)]
    s.depth = 1 + max(max(xs), max(zs))
    steps = [[] for _ in range(s.depth)]
    for q, t in zip(XO, xs):
        steps[t].append((C.xanc(0), q, ('X', 0, q)))
    for q, t in zip(ZO, zs):
        steps[t].append((q, C.zanc(0), ('Z', 0, q)))
    s.steps = steps
    return s

def enum(depth):
    out = []
    for xs in itertools.combinations(range(depth), 4):
        for zs in itertools.combinations(range(depth), 4):
            if any(xs[XO.index(q)] == zs[ZO.index(q)] for q in range(4)):
                continue
            if max(max(xs), max(zs)) != depth - 1:
                continue
            out.append(build(xs, zs))
    return out

for depth in (5, 6, 7, 8):
    sch = [s for s in enum(depth) if s.is_mc()]
    hist = {}
    wits = []
    for s in sch:
        dc, cert, ncol, ndet = d_circ(s, 3, 'Z', maxw=3)
        hist[dc] = hist.get(dc, 0) + 1
        if dc and dc >= 2:
            wits.append(s)
    print(f'depth {depth}: MC-consistent {len(sch)}  d_circ hist {hist}')
    if depth in (7, 8):
        for s in wits:
            nonempty = all(st for st in s.steps)
            print('   witness xslot', s.xslot[0], 'zslot', s.zslot[0],
                  'interleaved', s.is_interleaved(), 'no-empty-layer', nonempty)

# --- non-interleaved partners with the SAME within-check orders --------------
print()
print('=== non-interleaved partners, same orders ===')
for name, xs, zs in [('X block then Z block', (0,1,2,3), (4,5,6,7)),
                     ('Z block then X block', (4,5,6,7), (0,1,2,3))]:
    s = build(xs, zs)
    print(name, 'MC:', s.is_mc(), 'interleaved:', s.is_interleaved())
    for R in (2,3,4,5):
        dc, cert, ncol, ndet = d_circ(s, R, 'Z', maxw=3)
        print(f'   R={R}: d_circ={dc}  cols={ncol} dets={ndet} cert={cert}')
    E = residual_set(s, 'Z'); de, ec = d_ext(C, E, 'Z')
    print('   d_eff =', de, ec, ' residuals', sorted([sorted(e) for e in E], key=lambda a:(len(a),a)))

# --- stability of the 3 witnesses over R = 2..5, both sectors ---------------
print()
print('=== the 3 depth-7 witnesses, R=2..5, both memory sectors ===')
for xs, zs in [((0,3,4,5),(0,1,2,6)), ((2,3,4,5),(0,1,4,6)), ((2,3,4,5),(0,1,5,6))]:
    s = build(xs, zs)
    line = [f'x={list(xs)} z={list(zs)}']
    for sector in ('Z', 'X'):
        E = residual_set(s, sector); de, _ = d_ext(C, E, sector)
        ds = []
        for R in (2,3,4,5):
            dc, _, _, _ = d_circ(s, R, sector, maxw=3)
            ds.append(dc)
        line.append(f'{sector}-mem: d_eff={de} d_circ={ds}')
    print('  ' + ' | '.join(line))

# --- the RETRACTED depth-5 circuit ------------------------------------------
print()
print('=== retracted recon depth-5 circuit: X order q0q1q2q3 @ t1..t4, Z order q2q0q1q3 @ t2..t5 ===')
s = build((1,2,3,4), (2,3,4,5))   # slots as printed (shifted to 0-index below too)
print('  MC counts (cZ,cX,|overlap|):', s.mc_counts(), ' -> MC holds?', s.is_mc())
for q in range(4):
    print(f'   q{q}: t(a->q)={s.xslot[0][XO.index(q)]}  t(q->b)={s.zslot[0][ZO.index(q)]}',
          ' t(q->b)<t(a->q):', s.zslot[0][ZO.index(q)] < s.xslot[0][XO.index(q)])
```

### `item1_stim.py`

```python
import itertools, sys
sys.path.insert(0, '/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from rev import Code, Schedule, d_circ
from stimgen import build, deterministic
import stim

C = Code(4, [[0,1,2,3]], [[0,1,2,3]], zl=[0,2], xl=[0,1])
XO=[0,1,2,3]; ZO=[2,0,1,3]

def mk(xs, zs):
    return Schedule(C, [XO], [list(xs)], [ZO], [list(zs)])

# ---- (A) my (MC) predicate vs stim determinism, over ALL depth<=7 legal schedules ----
agree = dis = 0
tab = {}
for depth in (5,6,7):
    for xs in itertools.combinations(range(depth), 4):
        for zs in itertools.combinations(range(depth), 4):
            if any(xs[XO.index(q)] == zs[ZO.index(q)] for q in range(4)): continue
            if max(max(xs),max(zs)) != depth-1: continue
            s = mk(xs, zs)
            mine = s.is_mc()
            got_z = deterministic(C, s, 3, 'Z')
            got_x = deterministic(C, s, 3, 'X')
            if mine == got_z == got_x: agree += 1
            else:
                dis += 1
                if dis < 6: print('DISAGREE', xs, zs, mine, got_z, got_x)
            tab[(mine, got_z, got_x)] = tab.get((mine,got_z,got_x),0)+1
print(f'(MC) predicate vs stim determinism, depth 5-7 [[4,2,2]]: agree {agree}  disagree {dis}')
print('   breakdown (mine, stimZ, stimX):', tab)

# ---- (B) the retracted depth-5 circuit in stim ----
print()
s_bad = mk((1,2,3,4), (2,3,4,5))
for R in (2,3):
    try:
        build(C, s_bad, R, 'Z').detector_error_model()
        print(f'  retracted depth-5, R={R}: stim DEM BUILT (deterministic)  <-- unexpected')
    except ValueError as e:
        print(f'  retracted depth-5, R={R}: stim REFUSES ->', str(e).splitlines()[0][:80])

# ---- (C) the repaired witness: explicit weight-2 fault, stim, R=2..5 ----
print()
s_w = mk((0,3,4,5), (0,1,2,6))
print('witness x=[0,3,4,5] z=[0,1,2,6]  MC =', s_w.is_mc())
for R in (2,3,4,5):
    ok = deterministic(C, s_w, R, 'Z')
    print(f'  R={R}: stim DEM builds = {ok}')
# my propagator's weight-2 certificate at R=3 was
#   ('prep',0, qubit 5 = Z-ancilla, 'X') and ('cnot',0,step 3,gate 0,'XI')
# translate to stim: X on the Z-ancilla (qubit 5) right at round-0 start,
#   plus X on the control of the gate at step 3.
print('  step-by-step gates:', [(t,[(g[0],g[1]) for g in s_w.steps[t]]) for t in range(s_w.depth)])

def check_fault_set(sched, R, sector, faults, label):
    ckt = build(C, sched, R, sector, faults=faults)
    det, obsv = ckt.compile_detector_sampler().sample(1, separate_observables=True)
    print(f'  {label}: detectors fired = {int(det.sum())}, observable = {int(obsv[0][0])}')
    return det.sum() == 0 and bool(obsv[0][0])

print()
print('=== explicit weight-2 witness, verified in stim (independent circuit build) ===')
# fault A: X on the Z-check ancilla (qubit 5) at prep, i.e. before step 0 of round 0
# fault B: X on the X-check ancilla (qubit 4) right after its gate at step 3
for R in (2,3,4,5):
    faults = [('pauli', 0, 0, 'pre', 5, 'X'), ('pauli', 0, 3, 'post', 4, 'X')]
    ok = check_fault_set(s_w, R, 'Z', faults, f'witness R={R} weight-2 fault set')
    print('      -> undetectable nontrivial logical:', ok)

print()
print('=== weight-1 witness on the NON-INTERLEAVED partner (X block t0-3, Z block t4-7) ===')
s_ni = mk((0,1,2,3), (4,5,6,7))
print('  MC =', s_ni.is_mc(), ' interleaved =', s_ni.is_interleaved())
for R in (2,3,4,5):
    print('  stim DEM builds:', deterministic(C, s_ni, R, 'Z'))
    ok = check_fault_set(s_ni, R, 'Z', [('pauli', 0, 1, 'post', 4, 'X')], f'NI R={R} weight-1 fault')
    print('      -> undetectable nontrivial logical:', ok)

print()
print('=== is there a weight-1 undetectable logical in the WITNESS circuit?  (stim, brute force) ===')
# enumerate every single-location Pauli fault in the stim model and test it
def brute_w1(sched, R, sector):
    found = []
    locs = []
    for r in range(R):
        for t in range(sched.depth):
            for q in range(C.N):
                for P in 'XYZ':
                    locs.append(('pauli', r, t, 'pre', q, P))
                    locs.append(('pauli', r, t, 'post', q, P))
    for f in locs:
        ckt = build(C, sched, R, sector, faults=[f])
        det, obsv = ckt.compile_detector_sampler().sample(1, separate_observables=True)
        if det.sum() == 0 and obsv[0][0]:
            found.append(f)
    return found
print('  witness circuit R=3, Z-mem, weight-1 undetectable logicals found:',
      len(brute_w1(s_w, 3, 'Z')))
print('  non-interleaved partner R=3, Z-mem, weight-1 undetectable logicals found:',
      len(brute_w1(s_ni, 3, 'Z')))
```

### `item2_steane.py`

```python
import sys, itertools
sys.path.insert(0, '/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from rev import Code, Schedule, d_circ, residual_set, d_ext
from stimgen import build, deterministic

CH = [[3,4,5,6],[1,2,5,6],[0,2,4,6]]
S = Code(7, CH, CH, zl=[0,1,2], xl=[0,1,2])
print('Steane code valid:', S.check_valid())

# independent check that min logical weight is 3
def min_logical_weight(code, sector):
    checks = code.zchecks if sector=='Z' else code.xchecks
    obs = code.zl if sector=='Z' else code.xl
    best = None
    for w in range(1, code.n+1):
        for sup in itertools.combinations(range(code.n), w):
            s = set(sup)
            if all(len(s & set(g)) % 2 == 0 for g in checks) and len(s & set(obs)) % 2 == 1:
                return w, sorted(s)
    return None
print('min weight nontrivial logical (Z sector):', min_logical_weight(S,'Z'))
print('min weight nontrivial logical (X sector):', min_logical_weight(S,'X'))

# ---------------- the interleaved witness M_IL (as printed in the artifact) --------
XO = [[6,3,5,4],[1,5,6,2],[4,2,6,0]]
XT = [[0,1,2,3],[4,5,6,7],[0,1,2,7]]
ZO = [[3,4,6,5],[2,1,5,6],[2,4,6,0]]
ZT = [[0,1,3,4],[2,3,6,7],[0,4,5,6]]
M_IL = Schedule(S, XO, XT, ZO, ZT)
print()
print('M_IL depth', M_IL.depth, 'legal', M_IL.is_legal(), 'MC', M_IL.is_mc(),
      'interleaved', M_IL.is_interleaved())
print('  MC counts (cZ,cX,|overlap|) per (X,Z) pair:')
for k,v in sorted(M_IL.mc_counts().items()): print('   ', k, v)
print('  gates by step:')
for t,g in enumerate(M_IL.steps):
    print('   t%d:'%t, [('X%d->q%d'%(tag[1]+1,tag[2]) if tag[0]=='X' else 'q%d->Z%d'%(tag[2],tag[1]+1)) for _,_,tag in g])

# ---------------- my own non-interleaved partner, SAME within-check orders --------
XT_NI = [[0,1,2,3],[0,1,2,3],[0,1,3,4]]
ZT_NI = [[5,6,7,8],[5,6,7,9],[6,7,8,9]]
M_NI = Schedule(S, XO, XT_NI, ZO, ZT_NI)
print()
print('M_NI (mine) depth', M_NI.depth, 'legal', M_NI.is_legal(), 'MC', M_NI.is_mc(),
      'interleaved', M_NI.is_interleaved())

def report(name, sched):
    print()
    print('===', name, '===')
    for sector in ('Z','X'):
        E = residual_set(sched, sector)
        de, ec = d_ext(S, E, sector)
        Es = sorted([sorted(e) for e in E], key=lambda a:(len(a),a))
        print(f'  [{sector}-memory]  d_eff = {de}   (witness residuals {ec})')
        print(f'     residual set ({len(Es)}): {Es}')
        for R in (2,3,4,5):
            dc, cert, ncol, ndet = d_circ(sched, R, sector, maxw=3)
            det_ok = deterministic(S, sched, R, sector)
            print(f'     R={R}: d_circ = {dc}   cols={ncol} detectors={ndet}  stim-deterministic={det_ok}')
            if R == 3:
                print(f'        certificate: {cert}')

report('M_IL (interleaved, depth 8)', M_IL)
report('M_NI (non-interleaved, depth 10, mine)', M_NI)
```

### `item3_gross.py`

```python
import sys, numpy as np
sys.path.insert(0, '/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from gross_rev import *

print('=== A. the code ===')
print('  HX HZ^T == 0 :', not ((HX @ HZ.T) % 2).any())
print('  rank HX =', rank(HX), ' rank HZ =', rank(HZ), ' k =', N - rank(HX) - rank(HZ))
print('  row weights HX:', sorted(set(HX.sum(1))), ' HZ:', sorted(set(HZ.sum(1))))
print('  col weights HX:', sorted(set(HX.sum(0))), ' HZ:', sorted(set(HZ.sum(0))))
ov = {}
for g in range(NG):
    for h in range(NG):
        o = int((HX[g] & HZ[h]).sum())
        ov[o] = ov.get(o, 0) + 1
print('  X/Z check overlap histogram:', ov)
allone = np.ones(N, dtype=np.uint8)
RX, pX = rref(HX); RZ, pZ = rref(HZ)
print('  all-ones in rowspace(HX):', in_rowspace(RX, pX, allone),
      ' in rowspace(HZ):', in_rowspace(RZ, pZ, allone))

print()
print('=== B. the named schedule ===')
S = TISchedule(P={1,3,5}, alpha=(1,3,5), beta=(2,4,6), gamma=(2,6,4), delta=(5,1,3))
bad = S.legality()
print('  legality (each of 288 qubits in exactly one gate per layer):', 'OK' if not bad else bad)
print('  total CNOTs:', sum(len(v) for v in S.layers.values()))
print('  Z-check 1 CNOT order (layers 1..6):', S.z_cnot_order(1))
print('  X-check 0 CNOT order (layers 1..6):', S.x_cnot_order(0))
# cross-check the circuit against HX/HZ
ok = True
for g in range(NG):
    if sorted(S.z_cnot_order(g)) != sorted(np.flatnonzero(HZ[g]).tolist()): ok = False
    if sorted(S.x_cnot_order(g)) != sorted(np.flatnonzero(HX[g]).tolist()): ok = False
print('  circuit CNOT sets match HX/HZ supports for all 72+72 checks:', ok)

print()
print('=== C. the claimed weight-6 witness ===')
CHECKS = [1, 15, 29, 37, 51, 65]
for R in (1, 2, 3, 4):
    faults = [('zanc', R - 1, c, 3) for c in CHECKS]     # born between layers 2 and 3
    det, E = simulate_z(S, R, faults)
    ndet = len(det)
    # split detectors: last-round comparison detectors vs terminal detectors
    ker = not ((HX @ E) % 2).any()
    triv = in_rowspace(RZ, pZ, E)
    print(f'  R={R}: nfaults={len(faults)}  detectors={ndet}  fired={int(det.sum())}'
          f'  |E|={int(E.sum())}  E in ker(HX)={ker}  E in rowspace(HZ)={triv}'
          f'  -> nontrivial logical={ker and not triv}')

R = 3
faults = [('zanc', R - 1, c, 3) for c in CHECKS]
det, E = simulate_z(S, R, faults)
supp = np.flatnonzero(E).tolist()
print('  support of E (24 qubits):', supp)
print('  deposited residual S_3 per check:')
for c in CHECKS:
    o = S.z_cnot_order(c)
    print(f'    Z-check {c}: order {o}  ->  S_3 = {o[2:]}')
dep = sorted([q for c in CHECKS for q in S.z_cnot_order(c)[2:]])
print('  union of the six S_3 (with multiplicity):', len(dep), ' distinct:', len(set(dep)))
print('  equals supp(E):', sorted(set(dep)) == supp)

print()
print('  --- per-detector breakdown (R=3) ---')
# recompute detector groups explicitly
mXflips = []
z = np.zeros(S.NQ, dtype=np.uint8)
for c in CHECKS:
    pass
det2, E2 = simulate_z(S, 3, faults)
per = det2.reshape(NG, 4)   # [round0, round1, round2, terminal] per X-check
print('   round-0 detectors fired :', int(per[:,0].sum()))
print('   round-1 detectors fired :', int(per[:,1].sum()))
print('   round-2 (fault round) fired :', int(per[:,2].sum()), '  <- this is wt(f)')
print('   terminal detectors fired :', int(per[:,3].sum()))

print()
print('  --- control: perturb the witness, detectors should light up ---')
for drop in (0, 1):
    f2 = [('zanc', 2, c, 3) for c in CHECKS[:5]] if drop == 0 else \
         [('zanc', 2, c, 4) for c in CHECKS]
    d2, e2 = simulate_z(S, 3, f2)
    lbl = 'drop one fault (5 hooks)' if drop == 0 else 'shift all to layer boundary 4'
    print(f'   {lbl}: detectors fired {int(d2.sum())}, |E|={int(e2.sum())},'
          f' in ker(HX)={not ((HX@e2)%2).any()}')
```

### `item3b_pairs.py`

```python
import sys, numpy as np, random, itertools
sys.path.insert(0, '/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from gross_rev import *

random.seed(20260820); np.random.seed(20260820)
RX, pX = rref(HX); RZ, pZ = rref(HZ)

def isd_pool(Hdet, Rstab, pstab, trials=400, wmax=12):
    """harvest weight<=wmax words of ker(Hdet) that are NOT in rowspace(Rstab)"""
    K = nullspace(Hdet)
    found = set()
    cols = K.shape[1]
    for _ in range(trials):
        perm = np.random.permutation(cols)
        A = K[:, perm].copy()
        Rr, piv = rref(A)
        back = np.zeros((Rr.shape[0], cols), dtype=np.uint8)
        back[:, perm] = Rr
        rows = [back[i] for i in range(back.shape[0])]
        cand = list(rows)
        for i in range(len(rows)):
            for j in range(i + 1, len(rows)):
                cand.append(rows[i] ^ rows[j])
        for v in cand:
            w = int(v.sum())
            if 0 < w <= wmax and not in_rowspace(Rstab, pstab, v):
                found.add(tuple(np.flatnonzero(v).tolist()))
    return found

def translate(sup, t):
    out = []
    for q in sup:
        if q < NG: out.append(gadd(q, t))
        else:      out.append(NG + gadd(q - NG, t))
    return tuple(sorted(out))

TRANS = [(i, j) for i in range(L) for j in range(M)]

print('=== harvesting weight-12 logicals ===')
for sector, Hdet, Rstab, pstab, label in [('Z', HX, RZ, pZ, 'Z-logicals (ker HX \\ rowspace HZ)'),
                                          ('X', HZ, RX, pX, 'X-logicals (ker HZ \\ rowspace HX)')]:
    pool = isd_pool(Hdet, Rstab, pstab, trials=300)
    wmin = min(len(p) for p in pool) if pool else None
    pool12 = {p for p in pool if len(p) == 12}
    closed = set()
    for p in pool12:
        for t in TRANS:
            closed.add(translate(p, t))
    print(f'  [{sector}] raw ISD hits <=12: {len(pool)}  min weight found: {wmin}'
          f'  weight-12: {len(pool12)}  after 72 translations: {len(closed)}')
    globals()[f'POOL_{sector}'] = closed

print()
print('=== every 2-subset of a check support lies in a weight-12 logical? ===')
random.seed(7)
def verify_pair(sector, checkidx, pairidx):
    if sector == 'Z':
        sup = sorted(np.flatnonzero(HZ[checkidx]).tolist()); pool = POOL_Z; Hdet = HX; Rst, pst = RZ, pZ
    else:
        sup = sorted(np.flatnonzero(HX[checkidx]).tolist()); pool = POOL_X; Hdet = HZ; Rst, pst = RX, pX
    q1, q2 = sup[pairidx[0]], sup[pairidx[1]]
    hits = [Lg for Lg in pool if q1 in Lg and q2 in Lg]
    if not hits:
        return sup, (q1, q2), None, 0
    Lg = min(hits)
    v = np.zeros(N, dtype=np.uint8); v[list(Lg)] = 1
    assert int(v.sum()) == 12
    assert not ((Hdet @ v) % 2).any(), 'syndrome not zero!'
    assert not in_rowspace(Rst, pst, v), 'stabiliser, not a logical!'
    return sup, (q1, q2), Lg, len(hits)

# 3 random (sector, check, pair) choices  + full 15/15 coverage on one check of each type
choices = [('Z', random.randrange(72), tuple(sorted(random.sample(range(6), 2)))) for _ in range(3)]
choices += [('X', random.randrange(72), tuple(sorted(random.sample(range(6), 2)))) for _ in range(3)]
for sector, ci, pi in choices:
    sup, pair, Lg, nh = verify_pair(sector, ci, pi)
    print(f'  [{sector}] check {ci} support {sup}  pair (slots {pi}) = {pair}')
    if Lg is None:
        print('     *** NO weight-12 logical in pool contains this pair ***')
    else:
        print(f'     witness L (wt 12, zero syndrome, non-stabiliser) = {list(Lg)}   ({nh} witnesses in pool)')
        rest = [q for q in Lg if q not in pair]
        print(f'     extended-code codeword: residual {{{pair[0]},{pair[1]}}} + {len(rest)} singletons'
              f' = {1+len(rest)} residuals  ->  d_ext <= {1+len(rest)}')

print()
print('=== full 15/15 pair coverage, one check of each type ===')
for sector in ('Z', 'X'):
    ci = 0
    cov = 0
    for pi in itertools.combinations(range(6), 2):
        _, _, Lg, _ = verify_pair(sector, ci, pi)
        cov += (Lg is not None)
    print(f'  [{sector}] check {ci}: {cov}/15 pairs covered by a weight-12 logical')

print()
print('=== the argument, made explicit ===')
print('  For ANY schedule M and ANY Z-check c with CNOT order i1..i6, a single Z fault on c\'s')
print('  ancilla between the 4th and 5th CNOT deposits Z on exactly {i5,i6} c supp(c).')
print('  Since all 15 pairs of supp(c) sit in some weight-12 Z-logical L, E(M) contains')
print('  {i5,i6} and all 144 singletons, so {i5,i6} + 10 singletons is a weight-11 extended')
print('  codeword with zero syndrome and nontrivial logical action  =>  d_ext(E(M)) <= 11.')
```

### `item3c_mc.py`

```python
"""Cross-node check: do the Gross TI minimum-depth schedules satisfy the (MC) validity
constraint that CIRCDIST.lift's d3 gate established?  (rule 7e: silently accepting
invalid circuits)"""
import sys, itertools, numpy as np
sys.path.insert(0, '/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from gross_rev import *

def mc_report(S, verbose=False):
    tX = {}      # (xcheck g, qubit) -> layer
    tZ = {}
    for g in range(NG):
        for l, q in enumerate(S.x_cnot_order(g), start=1):
            tX[(g, q)] = l
        for l, q in enumerate(S.z_cnot_order(g), start=1):
            tZ[(g, q)] = l
    supX = [set(np.flatnonzero(HX[g]).tolist()) for g in range(NG)]
    supZ = [set(np.flatnonzero(HZ[h]).tolist()) for h in range(NG)]
    bad = 0; tot = 0
    examples = []
    for g in range(NG):
        for h in range(NG):
            sh = supX[g] & supZ[h]
            if not sh:
                continue
            tot += 1
            c = sum(1 for q in sh if tX[(g, q)] < tZ[(h, q)])
            if c % 2:
                bad += 1
                if len(examples) < 3:
                    examples.append((g, h, sorted(sh),
                                     [(q, tX[(g,q)], tZ[(h,q)]) for q in sorted(sh)]))
    return bad, tot, examples

named = {
 'bucket-6  P={1,3,5} a=(1,3,5) b=(2,4,6) g=(2,6,4) d=(5,1,3)':
     TISchedule({1,3,5},(1,3,5),(2,4,6),(2,6,4),(5,1,3)),
 'bucket-8  P={1,2,3} a=(1,2,3) b=(4,5,6) g=(6,4,5) d=(2,1,3)':
     TISchedule({1,2,3},(1,2,3),(4,5,6),(6,4,5),(2,1,3)),
 'bucket-12 P={1,2,5} a=(1,2,5) b=(3,6,4) g=(3,6,4) d=(1,2,5)':
     TISchedule({1,2,5},(1,2,5),(3,6,4),(3,6,4),(1,2,5)),
 'LRC       P={1,2,3} a=(1,2,3) b=(4,5,6) g=(4,5,6) d=(1,2,3)':
     TISchedule({1,2,3},(1,2,3),(4,5,6),(4,5,6),(1,2,3)),
}
print('=== (MC) on the named Gross TI schedules ===')
for name, S in named.items():
    bad, tot, ex = mc_report(S)
    print(f'  {name}\n     odd (X,Z) pairs: {bad} of {tot} overlapping pairs   -> MC valid: {bad==0}')
    for e in ex:
        print(f'       e.g. X-check {e[0]} / Z-check {e[1]}, shared {e[2]}, (q, t(a->q), t(q->b)) = {e[3]}')

print()
print('=== (MC) over the whole 25920-schedule TI class ===')
nvalid = 0; ntot = 0
valid_by_P = {}
for P in itertools.combinations(range(1, 7), 3):
    Pb = tuple(sorted(set(range(1,7)) - set(P)))
    for alpha in itertools.permutations(P):
        for beta in itertools.permutations(Pb):
            for gamma in itertools.permutations(Pb):
                for delta in itertools.permutations(P):
                    ntot += 1
    break   # count structure only
print('  (structure) 20 * 6^4 =', 20 * 6**4)

# MC depends only on (P, alpha, beta, gamma, delta); evaluate on a reduced predicate.
# Overlap of X-check g and Z-check h is 2 whenever nonempty; the two shared qubits are
#   left  q = g - A_i = h + B_j    and   right q = g - B_i' = h + A_j'
# with g-h = A_i + B_j  and  g-h = B_i' + A_j'.  MC requires the two orderings to agree.
def mc_valid_fast(P, alpha, beta, gamma, delta):
    # layer of X-check at its left  data via monomial A_i : alpha[i]
    # layer of X-check at its right data via monomial B_i : beta[i]
    # layer of Z-check at its left  data via monomial B_j : gamma[j]
    # layer of Z-check at its right data via monomial A_j : delta[j]
    for i in range(3):
        for j in range(3):
            # difference d = A_i + B_j  labels one left-shared qubit;
            # the SAME d is realised on the right by  B_i' + A_j'  with A_j'+B_i' = d,
            # i.e. i' = i? no: right sharing needs g-h = B_i' + A_j' = A_j' + B_i',
            # so (j', i') = (i, j).  Left pair uses (alpha[i], gamma[j]);
            # right pair uses (beta[j], delta[i]).
            c = (alpha[i] < gamma[j]) + (beta[j] < delta[i])
            if c % 2:
                return False
    return True

cnt = 0; tot = 0
for P in itertools.combinations(range(1, 7), 3):
    Pb = tuple(sorted(set(range(1,7)) - set(P)))
    for alpha in itertools.permutations(P):
        for beta in itertools.permutations(Pb):
            for gamma in itertools.permutations(Pb):
                for delta in itertools.permutations(P):
                    tot += 1
                    if mc_valid_fast(P, alpha, beta, gamma, delta):
                        cnt += 1
print(f'  fast predicate: {cnt} of {tot} TI minimum-depth schedules satisfy (MC)')

# validate the fast predicate against the literal one on 12 random schedules
import random
random.seed(3)
print('  validating fast predicate against literal 72x72 computation on 12 random schedules:')
mis = 0
for _ in range(12):
    P = tuple(sorted(random.sample(range(1,7), 3)))
    Pb = tuple(sorted(set(range(1,7)) - set(P)))
    alpha = tuple(random.sample(P,3)); delta = tuple(random.sample(P,3))
    beta = tuple(random.sample(Pb,3)); gamma = tuple(random.sample(Pb,3))
    S = TISchedule(set(P), alpha, beta, gamma, delta)
    bad, tot2, _ = mc_report(S)
    fast = mc_valid_fast(P, alpha, beta, gamma, delta)
    if (bad == 0) != fast:
        mis += 1
        print('    MISMATCH', P, alpha, beta, gamma, delta, bad, fast)
print(f'    mismatches: {mis}/12')
```

### `item3d_stim.py`

```python
"""Decisive independent test: does stim accept the Gross TI minimum-depth circuits as having
deterministic detectors?"""
import sys, itertools, random, numpy as np, stim
sys.path.insert(0, '/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from gross_rev import *

def gross_stim(S, R, sector='X'):
    """sector='X' : X-memory (|+> init, MX readout) -- the one the G1 Z-fault analysis uses."""
    C = stim.Circuit()
    data = list(range(N))
    xa = [S.xanc(g) for g in range(NG)]
    za = [S.zanc(g) for g in range(NG)]
    C.append('RX' if sector == 'X' else 'R', data)
    mi = 0; recs = {}
    for r in range(R):
        C.append('RX', xa); C.append('R', za)
        for l in range(1, 7):
            t = []
            for c, tg in S.layers[l]:
                t += [c, tg]
            C.append('CX', t); C.append('TICK')
        for g in range(NG):
            C.append('MX', [xa[g]]); recs[('X', g, r)] = mi; mi += 1
        for g in range(NG):
            C.append('M', [za[g]]); recs[('Z', g, r)] = mi; mi += 1
    C.append('MX' if sector == 'X' else 'M', data)
    for q in range(N):
        recs[('d', q)] = mi; mi += 1
    tot = mi
    rec = lambda k: stim.target_rec(recs[k] - tot)
    prim, dual = ('X', 'Z') if sector == 'X' else ('Z', 'X')
    H = HX if sector == 'X' else HZ
    for g in range(NG):
        C.append('DETECTOR', [rec((prim, g, 0))])
        for r in range(1, R):
            C.append('DETECTOR', [rec((prim, g, r)), rec((prim, g, r - 1))])
        C.append('DETECTOR', [rec((prim, g, R - 1))] +
                 [rec(('d', q)) for q in np.flatnonzero(H[g])])
    for g in range(NG):
        for r in range(1, R):
            C.append('DETECTOR', [rec((dual, g, r)), rec((dual, g, r - 1))])
    return C

named = {
 'bucket-6   P={1,3,5} a=(1,3,5) b=(2,4,6) g=(2,6,4) d=(5,1,3)': ({1,3,5},(1,3,5),(2,4,6),(2,6,4),(5,1,3)),
 'bucket-8   P={1,2,3} a=(1,2,3) b=(4,5,6) g=(6,4,5) d=(2,1,3)': ({1,2,3},(1,2,3),(4,5,6),(6,4,5),(2,1,3)),
 'bucket-12  P={1,2,5} a=(1,2,5) b=(3,6,4) g=(3,6,4) d=(1,2,5)': ({1,2,5},(1,2,5),(3,6,4),(3,6,4),(1,2,5)),
 'LRC        P={1,2,3} a=(1,2,3) b=(4,5,6) g=(4,5,6) d=(1,2,3)': ({1,2,3},(1,2,3),(4,5,6),(4,5,6),(1,2,3)),
}
print('=== stim determinism test, Gross TI minimum-depth schedules, R = 2 ===')
for name, args in named.items():
    S = TISchedule(*args)
    for sector in ('X', 'Z'):
        try:
            gross_stim(S, 2, sector).detector_error_model()
            verdict = 'DEM BUILT (deterministic)'
        except ValueError as e:
            verdict = 'stim REFUSES: ' + str(e).splitlines()[0][:60]
        print(f'  {name}  [{sector}-memory]: {verdict}')

print()
print('=== 10 random TI schedules ===')
random.seed(11)
nbad = 0
for _ in range(10):
    P = tuple(sorted(random.sample(range(1, 7), 3)))
    Pb = tuple(sorted(set(range(1, 7)) - set(P)))
    S = TISchedule(set(P), tuple(random.sample(P, 3)), tuple(random.sample(Pb, 3)),
                   tuple(random.sample(Pb, 3)), tuple(random.sample(P, 3)))
    try:
        gross_stim(S, 2, 'X').detector_error_model(); ok = True
    except ValueError:
        ok = False
    nbad += (not ok)
print(f'  {nbad}/10 refused by stim (non-deterministic detectors)')

print()
print('=== the parity obstruction, stated and checked ===')
print('  For an overlapping (X-check g, Z-check h) pair the two shared qubits are exactly one')
print('  LEFT qubit (X-side monomial A_i, Z-side monomial B_j) and one RIGHT qubit (X-side B_j,')
print('  Z-side A_i) -- same index pair (i,j).  So the (MC) count for that pair is')
print('      [alpha_i < gamma_j] + [beta_j < delta_i].')
print('  Summing over all 9 (i,j):  sum = |{(p,q) in P x Pbar : p<q}| + |{(q,p) : q<p}| = 9, ODD.')
print('  So the 9 per-pair parities cannot all be even  =>  NO TI minimum-depth Gross schedule')
print('  satisfies (MC).  Numerically verified: 0 of 25920.')
for P in itertools.combinations(range(1,7),3):
    Pb = sorted(set(range(1,7))-set(P))
    c = sum(1 for p in P for q in Pb if p<q)
    assert c + (9-c) == 9
print('  (identity |{p<q}| + |{q<p}| = 9 checked for all 20 choices of P)')
```

### `item3e_control.py`

```python
"""Positive control: a genuinely NON-INTERLEAVED Gross schedule (all X-CNOTs in layers 1..6,
all Z-CNOTs in layers 7..12) must be deterministic under the SAME detector definitions."""
import sys, numpy as np, stim
sys.path.insert(0, '/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from gross_rev import *


class GenSchedule:
    """arbitrary layer assignment: alpha (X->left, A-monos), beta (X->right, B-monos),
       gamma (Z->left, B-monos), delta (Z->right, A-monos); layers 1..D"""
    def __init__(self, alpha, beta, gamma, delta):
        self.alpha, self.beta, self.gamma, self.delta = alpha, beta, gamma, delta
        self.D = max(list(alpha) + list(beta) + list(gamma) + list(delta))
        self.NQ = N + 2 * NG
        self.xanc = lambda g: N + g
        self.zanc = lambda g: N + NG + g
        layers = {l: [] for l in range(1, self.D + 1)}
        for g in range(NG):
            for i, a in enumerate(Amon):
                layers[alpha[i]].append((self.xanc(g), gsub(g, a)))
            for i, b in enumerate(Bmon):
                layers[beta[i]].append((self.xanc(g), NG + gsub(g, b)))
            for i, b in enumerate(Bmon):
                layers[gamma[i]].append((gadd(g, b), self.zanc(g)))
            for i, a in enumerate(Amon):
                layers[delta[i]].append((NG + gadd(g, a), self.zanc(g)))
        self.layers = layers

    def legal(self):
        for l in range(1, self.D + 1):
            used = set()
            for c, t in self.layers[l]:
                if c in used or t in used:
                    return False, l
                used.add(c); used.add(t)
        return True, None

    def x_order(self, g):
        o = {}
        for i, a in enumerate(Amon): o[self.alpha[i]] = gsub(g, a)
        for i, b in enumerate(Bmon): o[self.beta[i]] = NG + gsub(g, b)
        return [o[k] for k in sorted(o)]

    def z_order(self, g):
        o = {}
        for i, b in enumerate(Bmon): o[self.gamma[i]] = gadd(g, b)
        for i, a in enumerate(Amon): o[self.delta[i]] = NG + gadd(g, a)
        return [o[k] for k in sorted(o)]

    def mc_bad(self):
        tX = {}; tZ = {}
        for g in range(NG):
            for i, a in enumerate(Amon): tX[(g, gsub(g, a))] = self.alpha[i]
            for i, b in enumerate(Bmon): tX[(g, NG + gsub(g, b))] = self.beta[i]
            for i, b in enumerate(Bmon): tZ[(g, gadd(g, b))] = self.gamma[i]
            for i, a in enumerate(Amon): tZ[(g, NG + gadd(g, a))] = self.delta[i]
        supX = [set(np.flatnonzero(HX[g]).tolist()) for g in range(NG)]
        supZ = [set(np.flatnonzero(HZ[h]).tolist()) for h in range(NG)]
        bad = 0
        for g in range(NG):
            for h in range(NG):
                sh = supX[g] & supZ[h]
                if sh and sum(1 for q in sh if tX[(g, q)] < tZ[(h, q)]) % 2:
                    bad += 1
        return bad


def gross_stim(S, R, sector='X'):
    C = stim.Circuit(); data = list(range(N))
    xa = [S.xanc(g) for g in range(NG)]; za = [S.zanc(g) for g in range(NG)]
    C.append('RX' if sector == 'X' else 'R', data)
    mi = 0; recs = {}
    for r in range(R):
        C.append('RX', xa); C.append('R', za)
        for l in range(1, S.D + 1):
            t = []
            for c, tg in S.layers[l]:
                t += [c, tg]
            if t: C.append('CX', t)
            C.append('TICK')
        for g in range(NG):
            C.append('MX', [xa[g]]); recs[('X', g, r)] = mi; mi += 1
        for g in range(NG):
            C.append('M', [za[g]]); recs[('Z', g, r)] = mi; mi += 1
    C.append('MX' if sector == 'X' else 'M', data)
    for q in range(N): recs[('d', q)] = mi; mi += 1
    tot = mi; rec = lambda k: stim.target_rec(recs[k] - tot)
    prim, dual = ('X', 'Z') if sector == 'X' else ('Z', 'X')
    H = HX if sector == 'X' else HZ
    for g in range(NG):
        C.append('DETECTOR', [rec((prim, g, 0))])
        for r in range(1, R):
            C.append('DETECTOR', [rec((prim, g, r)), rec((prim, g, r - 1))])
        C.append('DETECTOR', [rec((prim, g, R - 1))] + [rec(('d', q)) for q in np.flatnonzero(H[g])])
    for g in range(NG):
        for r in range(1, R):
            C.append('DETECTOR', [rec((dual, g, r)), rec((dual, g, r - 1))])
    return C


print('=== POSITIVE CONTROL: fully non-interleaved depth-12 Gross schedule ===')
NI = GenSchedule(alpha=(1,2,3), beta=(4,5,6), gamma=(7,8,9), delta=(10,11,12))
print('  legal:', NI.legal(), ' depth:', NI.D)
print('  (MC)-violating (X,Z) pairs:', NI.mc_bad())
for sector in ('X', 'Z'):
    try:
        dem = gross_stim(NI, 2, sector).detector_error_model()
        print(f'  [{sector}-memory] stim: DEM BUILT (deterministic detectors)  <-- control passes')
    except ValueError as e:
        print(f'  [{sector}-memory] stim REFUSES: {str(e).splitlines()[0][:70]}')

print()
print('=== direct sampling test: are individual X-check outcomes random? ===')
S6 = GenSchedule(alpha=(1,3,5), beta=(2,4,6), gamma=(2,6,4), delta=(5,1,3))
print('  bucket-6 schedule legal:', S6.legal(), ' MC-violating pairs:', S6.mc_bad())
for name, S in [('bucket-6 TI (interleaved)', S6), ('non-interleaved depth-12 control', NI)]:
    C = stim.Circuit(); data = list(range(N))
    xa = [S.xanc(g) for g in range(NG)]; za = [S.zanc(g) for g in range(NG)]
    C.append('RX', data)
    for r in range(2):
        C.append('RX', xa); C.append('R', za)
        for l in range(1, S.D + 1):
            t = []
            for c, tg in S.layers[l]: t += [c, tg]
            if t: C.append('CX', t)
        C.append('MX', xa); C.append('M', za)
    m = C.compile_sampler().sample(200)          # 200 shots, 4*72 measurements
    m = m.reshape(200, 4, NG)
    diff = m[:, 2, :] ^ m[:, 0, :]               # X-check round1 XOR round0
    varying = int((diff.std(axis=0) > 0).sum())
    print(f'  {name}: X-check difference m_e(1)^m_e(0) NOT constant for {varying}/72 checks')
    r0 = m[:, 0, :]
    print(f'     round-0 X-check outcome not constant for {int((r0.std(axis=0)>0).sum())}/72 checks')
```

### `item3f_repair.py`

```python
"""Can the multi-hook weight-6 mechanism be REPAIRED onto an (MC)-VALID Gross schedule?
Same within-check CNOT orders as the bucket-6 TI schedule, but X block in layers 1..6 and
Z block in layers 7..12 (genuinely non-interleaved, hence automatically (MC)-consistent)."""
import sys, numpy as np, stim
sys.path.insert(0, '/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from gross_rev import *
from item3e_control import GenSchedule, gross_stim

RX, pX = rref(HX); RZ, pZ = rref(HZ)

def simulate_gen(S, R, faults):
    z = np.zeros(S.NQ, dtype=np.uint8); mX = {}
    for r in range(R):
        z[N:] = 0
        for l in range(1, S.D + 1):
            for f in faults:
                if f[0] == 'zanc' and f[1] == r and f[3] == l: z[S.zanc(f[2])] ^= 1
                if f[0] == 'data' and f[1] == r and f[3] == l: z[f[2]] ^= 1
            snap = z.copy()
            for c, t in S.layers[l]:
                z[c] ^= snap[t]
        for f in faults:
            if f[0] == 'data' and f[1] == r and f[3] == S.D + 1: z[f[2]] ^= 1
        for g in range(NG): mX[(g, r)] = int(z[S.xanc(g)])
    E = z[:N].copy()
    det = []
    for g in range(NG):
        det.append(mX[(g, 0)])
        for r in range(1, R): det.append(mX[(g, r)] ^ mX[(g, r - 1)])
        det.append(mX[(g, R - 1)] ^ int((HX[g] & E).sum() % 2))
    return np.array(det, np.uint8), E

# bucket-6 TI orders:  X = A0(1) B0(2) A1(3) B1(4) A2(5) B2(6)
#                      Z = A1(1) B0(2) A2(3) B2(4) A0(5) B1(6)
# non-interleaved version, SAME orders, X at 1..6 and Z at 7..12:
NIrep = GenSchedule(alpha=(1, 3, 5), beta=(2, 4, 6),
                    gamma=(8, 12, 10), delta=(11, 7, 9))
print('=== repaired schedule (same within-check orders, non-interleaved, depth 12) ===')
print('  legal:', NIrep.legal(), '  depth:', NIrep.D)
print('  (MC)-violating (X,Z) pairs:', NIrep.mc_bad())
for sector in ('X', 'Z'):
    try:
        gross_stim(NIrep, 2, sector).detector_error_model()
        print(f'  [{sector}-memory] stim: DEM BUILT -> VALID syndrome-extraction circuit')
    except ValueError as e:
        print(f'  [{sector}-memory] stim REFUSES: {str(e).splitlines()[0][:60]}')

CHECKS = [1, 15, 29, 37, 51, 65]
S6 = TISchedule({1,3,5}, (1,3,5), (2,4,6), (2,6,4), (5,1,3))
print()
print('  within-check Z orders identical to the TI bucket-6 schedule?')
same = all(S6.z_cnot_order(g) == NIrep.z_order(g) for g in range(NG)) and \
       all(S6.x_cnot_order(g) == NIrep.x_order(g) for g in range(NG))
print('   ', same)
for c in CHECKS[:2]:
    print(f'    Z-check {c}: TI order {S6.z_cnot_order(c)}  |  repaired order {NIrep.z_order(c)}')

print()
print('=== the same 6 hook faults on the REPAIRED (valid) schedule ===')
# hook after the 2nd Z-CNOT of each check: in the repaired schedule that is after layer 8,
# i.e. born at layer 9 -> deposits on the last four Z-CNOT targets = the same S_3.
for R in (2, 3, 4):
    faults = [('zanc', R - 1, c, 9) for c in CHECKS]
    det, E = simulate_gen(NIrep, R, faults)
    ker = not ((HX @ E) % 2).any(); triv = in_rowspace(RZ, pZ, E)
    print(f'  R={R}: |F|=6  detectors={len(det)}  fired={int(det.sum())}  |E|={int(E.sum())}'
          f'  ker={ker}  stabiliser={triv}  -> undetectable nontrivial logical={ker and not triv and det.sum()==0}')

det, E = simulate_gen(NIrep, 3, [('zanc', 2, c, 9) for c in CHECKS])
det6, E6 = simulate_z(S6, 3, [('zanc', 2, c, 3) for c in CHECKS])
print('  net error identical to the TI witness:', bool((E == E6).all()), ' |E| =', int(E.sum()))

print()
print('=== d_ext reading (needs no detectors at all) ===')
print('  The six residuals S_3(c), c in', CHECKS, ', are six distinct elements of E(M):')
tot = np.zeros(N, np.uint8)
for c in CHECKS:
    s3 = NIrep.z_order(c)[2:]
    v = np.zeros(N, np.uint8); v[s3] = 1
    tot ^= v
    print(f'    S_3({c}) = {s3}  (weight {len(s3)})')
print('  product weight', int(tot.sum()), ' zero X-syndrome:', not ((HX@tot)%2).any(),
      ' non-stabiliser:', not in_rowspace(RZ, pZ, tot))
print('  => d_ext(E(M)) <= 6 for this VALID schedule, refuting "d_ext in {10,11,12}" outright.')
```

### `item4a_hist.py`

```python
import sys, numpy as np, itertools, random
sys.path.insert(0, '/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from gross_rev import *
RX, pX = rref(HX); RZ, pZ = rref(HZ)

def verdict(S, faults, R=3, label=''):
    det, E = simulate_z(S, R, faults)
    per = det.reshape(NG, R + 1)
    ker = not ((HX @ E) % 2).any()
    triv = in_rowspace(RZ, pZ, E)
    print(f'  {label}')
    print(f'     |F|={len(faults)}  detectors={len(det)}  fired={int(det.sum())}'
          f'  (rounds {[int(per[:,i].sum()) for i in range(R)]}, terminal {int(per[:,R].sum())})')
    print(f'     |E|={int(E.sum())}  E in ker(HX)={ker}  E in rowspace(HZ)={triv}'
          f'  -> undetectable nontrivial logical = {ker and not triv and det.sum()==0}')
    return ker and not triv and det.sum() == 0

print('=== bucket 6: worst schedule P={1,3,5} a=(1,3,5) b=(2,4,6) g=(2,6,4) d=(5,1,3) ===')
S6 = TISchedule({1,3,5}, (1,3,5), (2,4,6), (2,6,4), (5,1,3))
print('  legality:', 'OK' if not S6.legality() else S6.legality())
verdict(S6, [('zanc', 2, c, 3) for c in [1,15,29,37,51,65]], label='6 hook faults, layer boundary 3')

print()
print('=== bucket 8: NON-INTERLEAVED P={1,2,3} a=(1,2,3) b=(4,5,6) g=(6,4,5) d=(2,1,3) ===')
S8 = TISchedule({1,2,3}, (1,2,3), (4,5,6), (6,4,5), (2,1,3))
print('  legality:', 'OK' if not S8.legality() else S8.legality())
print('  non-interleaved? P == {1,2,3} so all X-CNOTs in layers 1-3 to LEFT data and 4-6 to RIGHT;')
print('    X-check layers:', sorted(set((1,2,3))|set((4,5,6))), ' Z-check layers:', sorted(set((6,4,5))|set((2,1,3))))
f8 = [('zanc', 2, c, 5) for c in [4, 20, 37, 59]] + \
     [('data', 2, q, 7) for q in [78, 102, 117, 141]]
for c in [4,20,37,59]:
    print(f'    Z-check {c} order {S8.z_cnot_order(c)}  S_5 = {S8.z_cnot_order(c)[4:]}')
verdict(S8, f8, label='4 hook faults (boundary 5) + 4 late data faults')

print()
print('=== bucket 12: best schedule P={1,2,5} a=(1,2,5) b=(3,6,4) g=(3,6,4) d=(1,2,5) ===')
S12 = TISchedule({1,2,5}, (1,2,5), (3,6,4), (3,6,4), (1,2,5))
print('  legality:', 'OK' if not S12.legality() else S12.legality())
# trivial witness: 12 data faults born after the last CNOT layer, on a weight-12 logical
def isd_pool(Hdet, Rstab, pstab, trials=120, wmax=12):
    K = nullspace(Hdet); found = set(); cols = K.shape[1]
    np.random.seed(1)
    for _ in range(trials):
        perm = np.random.permutation(cols)
        Rr, piv = rref(K[:, perm].copy())
        back = np.zeros((Rr.shape[0], cols), dtype=np.uint8); back[:, perm] = Rr
        rows = [back[i] for i in range(back.shape[0])]
        for v in rows + [rows[i] ^ rows[j] for i in range(len(rows)) for j in range(i+1, len(rows))]:
            w = int(v.sum())
            if 0 < w <= wmax and not in_rowspace(Rstab, pstab, v):
                found.add(tuple(np.flatnonzero(v).tolist()))
    return found
Lg = sorted(isd_pool(HX, RZ, pZ))[0]
print('  weight-12 Z-logical used:', list(Lg))
verdict(S12, [('data', 2, q, 7) for q in Lg], label='12 data faults born after layer 6')
print('  (control) same 12 faults born BEFORE layer 6:')
verdict(S12, [('data', 2, q, 6) for q in Lg], label='12 data faults born before layer 6')

print()
print('=== does the weight-6 fault class also work on the bucket-12 schedule? (sanity) ===')
best = None
for c0 in range(3):
    f = [('zanc', 2, c, 3) for c in [1,15,29,37,51,65]]
    det, E = simulate_z(S12, 3, f)
    print(f'   same 6-hook set on S12: detectors fired {int(det.sum())} -> not a witness there')
    break
```

### `item4b_formula.py`

```python
"""My own derivation + check of the one-round repair-cost predictor.

Derivation (mine).  A weight-1 fault in round r flips the primary-check outcomes of THAT round
by u, and leaves a terminal residual E with syndrome s = H_prim E.  The residual persists, so it
flips every later round's outcome by s.  With D_g(r') = m_g(r') + m_g(r'-1):
    D(r) = u ,  D(r+1) = u + s ,  D(r'>r+1) = 0 , terminal = 0
i.e. detector chain  x^r ( u(1+x) + s x ).  For gamma = {e_1..e_w} with sum s_i = 0 and
sum lambda_i = 1, put B(x) = sum s_i x^{r_i}; B(1) = 0 so B = (1+x)C.  Total chain
= (1+x)(A + xC), A = sum u_i x^{r_i}.  A measurement-flip fault costs 1 and adds one monomial
to A.  So repair(gamma) = min over round assignments of wt(A + xC).
  w=1, s=0:            repair = |u_1|
  w=2, s_1=s_2=s, gap k: k=0 -> |u1 ^ u2| ; k=1 -> |u1| + |u2 ^ s| (or mirror);
                         k>=2 -> |u1| + (k-1)|s| + |u2 ^ s|  (never better when s != 0;
                         when s = 0 it degenerates to the k=0 case).
"""
import sys, itertools
sys.path.insert(0, '/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from rev import Code, Schedule, Sim, d_circ, residual_set, d_ext

def bits(v):
    return bin(v).count('1')

def one_round_data(code, sched, sector):
    """residual E -> set of achievable u (as bitmasks over the primary checks)"""
    sim = Sim(sched, 1, sector)
    prim = 'Z' if sector == 'Z' else 'X'
    primchecks = code.zchecks if sector == 'Z' else code.xchecks
    obs = code.zl if sector == 'Z' else code.xl
    U = {}
    for f in sim.fault_list():
        x, z, meas = sim.run(f)
        err = x if sector == 'Z' else z
        E = frozenset(q for q in range(code.n) if (err >> q) & 1)
        u = 0
        for g in range(len(primchecks)):
            if meas[(prim, g, 0)]:
                u |= 1 << g
        U.setdefault(E, set()).add(u)
    def syn(E):
        s = 0
        for g, ch in enumerate(primchecks):
            if len(E & set(ch)) % 2:
                s |= 1 << g
        return s
    def lam(E):
        return len(E & set(obs)) % 2
    return U, syn, lam

def predict(code, sched, sector):
    U, syn, lam = one_round_data(code, sched, sector)
    Es = [E for E in U if E]
    best = None; bestg = None
    for E in Es:                                   # |gamma| = 1
        if syn(E) == 0 and lam(E) == 1:
            r = min(bits(u) for u in U[E])
            if best is None or 1 + r < best:
                best, bestg = 1 + r, (sorted(E), r)
    for E1, E2 in itertools.combinations(Es, 2):   # |gamma| = 2
        if syn(E1) != syn(E2):
            continue
        if (lam(E1) ^ lam(E2)) != 1:
            continue
        s = syn(E1)
        r = min(min(bits(u1 ^ u2),
                    bits(u1) + bits(u2 ^ s),
                    bits(u2) + bits(u1 ^ s))
                for u1 in U[E1] for u2 in U[E2])
        if best is None or 2 + r < best:
            best, bestg = 2 + r, (sorted(E1), sorted(E2), r)
    return best, bestg

CH = [[3,4,5,6],[1,2,5,6],[0,2,4,6]]
St = Code(7, CH, CH, zl=[0,1,2], xl=[0,1,2])
M_IL = Schedule(St, [[6,3,5,4],[1,5,6,2],[4,2,6,0]], [[0,1,2,3],[4,5,6,7],[0,1,2,7]],
                    [[3,4,6,5],[2,1,5,6],[2,4,6,0]], [[0,1,3,4],[2,3,6,7],[0,4,5,6]])
M_NI = Schedule(St, [[6,3,5,4],[1,5,6,2],[4,2,6,0]], [[0,1,2,3],[0,1,2,3],[0,1,3,4]],
                    [[3,4,6,5],[2,1,5,6],[2,4,6,0]], [[5,6,7,8],[5,6,7,9],[6,7,8,9]])
C4 = Code(4, [[0,1,2,3]], [[0,1,2,3]], zl=[0,2], xl=[0,1])
W_IL = Schedule(C4, [[0,1,2,3]], [[0,3,4,5]], [[2,0,1,3]], [[0,1,2,6]])
W_NI = Schedule(C4, [[0,1,2,3]], [[0,1,2,3]], [[2,0,1,3]], [[4,5,6,7]])

print(f'{"schedule":34s} {"sector":8s} {"d_eff":6s} {"pred min l":11s} {"exhaustive d_circ":18s} agree')
for name, code, sch in [('Steane M_IL (interleaved, d8)', St, M_IL),
                        ('Steane M_NI (non-IL, d10)', St, M_NI),
                        ('[[4,2,2]] IL witness (d7)', C4, W_IL),
                        ('[[4,2,2]] NI partner (d8)', C4, W_NI)]:
    for sector in ('Z', 'X'):
        E = residual_set(sch, sector)
        de, _ = d_ext(code, E, sector)
        p, g = predict(code, sch, sector)
        dc, cert, _, _ = d_circ(sch, 3, sector, maxw=3)
        print(f'{name:34s} {sector:8s} {de:<6d} {str(p):11s} {str(dc):18s} {p == dc}')
        print(f'{"":34s}   minimising gamma: {g}')
```
