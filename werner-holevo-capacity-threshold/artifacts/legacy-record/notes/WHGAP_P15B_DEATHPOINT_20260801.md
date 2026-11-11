# WHGAP P15-B — where does the pure-anchor order P_b2 die, and does it tensorize?

Executor note, 2026-08-01. Commission
[WHGAP_COMMISSION_LEAN5_P15B_20260801.md](WHGAP_COMMISSION_LEAN5_P15B_20260801.md), Track P15B.
Node: `WHGAP.pure-anchor-order` (P15), obligations 2 and 3. Reviewer: not yet commissioned.

**Everything below is executor-authored and UNREVIEWED. Cap: NUMERICAL with
`pending-review:` (DAG_PROTOCOL §2, rule 6). Nothing here licenses a completion tier.**

---

## PRE-ACTION REPORT

- **Target node:** `WHGAP.pure-anchor-order` (alias P15). **Status as read from disk:**
  `OPEN`, `disposition: null`
  (`channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.pure-anchor-order.md` front
  matter lines 2–14; row `P15` of `proof-dag/NODE_INDEX.md` line 127).
- **Role:** EXECUTOR (Track P15B). I did not author P15-A, R8 or R9; I was given the R9
  baseline as frozen input, not as a desired outcome.
- **Highest status my planned evidence could license (§2 ladder):** **NUMERICAL** with a
  `pending-review:` marker, writable by me as proposer with command + raw log path + script
  SHA-256. Completion tiers (CERTIFIED\*/PROVED/REFUTED) may be written only by the decision
  layer after an archived, cited, rule-7-compliant independent review (rule 6). One item in
  §4 is a closed-form identity that I regard as a complete derivation by my own lights; it is
  written here as CONJECTURED/NUMERICAL and is flagged for the reviewer as the single item
  where a FORMULA-level (not value-level) check is owed.
- **Gates and deliverables of my commission, one line each:**
  - **G-P15B-1 (Phase 0, hard)** — with my own optimizer reproduce a `P_b2` violation at
    x = 41/100 and sharpen it with mpmath to ≥ 40 digits; failure ⇒ STOP the track.
  - **G-P15B-2 (Phase 1)** — coarse scan {0.415 … 0.445} at a restart count justified from
    the Phase-0 hit rate, then bisect to a bracket [x_viol, x_null] of width ≤ 5·10⁻³;
    deliver the bracket, every mpmath-sharpened violation certificate, and the min-G-vs-x
    curve.
  - **G-P15B-3 (Phase 2)** — 2-copy tensorization probe at ≥ 2 surviving-side points
    (Λ_x ⊗ Λ_x, pure anchors in the 9-dim input, σ over 9×9 states): a confirmed 2-copy
    violation where the 1-copy property holds ⇒ P_b2 does NOT tensorize; bounded null ⇒ the
    route survives, NUMERICAL only.
  - Deliverables: this note, `tools/whgap_p15b_*.py`, `artifacts/logs_whgap_p15b_20260801/`
    with an LF `SHA256SUMS.txt`. Single-writer deviation: **no node file, no `NODE_INDEX.md`,
    no `WERNER-HOLEVO-GAP_PROOF_DAG.md` edits**; no git commit or push.
- **Conflicts between commission text and disk protocols:** **none.** Three notes, none of
  them a conflict:
  1. the single-writer deviation suspends my DAG-protocol §5/§6 write duties (commissioned in
     writing, §"Standing rules"); the atomic-update obligation therefore falls to the decision
     layer and this note contains everything it needs;
  2. the commission's frozen-input summary is accurate against disk — I re-read the
     definitions from `notes/WHGAP_P15A_STRICTNESS_20260730.md` and
     `artifacts/whgap_r9_review_20260801.md` and found no mismatch (§1);
  3. the commission suggests probe points 0.46 and 0.48 for Phase 2; I ran those **and** the
     more informative point immediately above the death point (43/100). That is an extra
     point inside Phase 2, not a fourth phase.

---

## 0. Executive summary

| item | outcome |
|---|---|
| **G-P15B-1** (calibration at x = 41/100) | **PASS.** Own instrument, 170/200 restarts negative, `min G = −0.068033973020`, 60-dps certificate `−0.0680339730196980833689685022337685252422370345`. Agrees with R9's independent `−0.0680339730197` to every printed digit. |
| **G-P15B-2** (bracket) | **PASS.** `[x_viol, x_null] = [687/1600, 43/100] = [0.429375, 0.430000]`, **width 6.25·10⁻⁴** (commission required ≤ 5·10⁻³). Seven mpmath-sharpened violation certificates, one per violating grid/bisection point. |
| **new (Phase 1 by-product, the sharpest result here)** | Near the death point the global minimiser is EXACTLY the **orthocomplement pair** `ψ` real, `σ = (1 − P_ψ)/2`. On that stratum `G` has the closed form `G*(x) = (1−2x)ln x + x ln(2−x) − (1−x)ln(1−x) − (1−x)ln 2`, and **x_d = 0.42966287456589232412005619893737910757142031486046** (50 digits) is a simple transversal root, `G*'(x_d) = 3.3262…`. It sits inside the independently-obtained search bracket. |
| **G-P15B-3** (tensorization) | **PASS as a gate; verdict = BOUNDED NULL.** No 2-copy violation at x ∈ {43/100, 23/50, 12/25} (free and interior searches). So the P15 route to `Q = 0` on `(x_d, 1/2)` **survives** this first test — NUMERICAL only, with the budget stated in §5.4. |
| **structural theorem (Phase 2)** | `W_2(σ₁⊗σ₂) = W(σ₁)⊗1 + 1⊗W(σ₂)`, hence **2-copy P_b2 restricted to product σ ⟺ 1-copy P_b2**, with the optimal anchor a product vector. Any 2-copy violation therefore REQUIRES a correlated σ; entangling the anchor alone can never help. |
| **new finding (NUMERICAL, unexpected)** | At x = 41/100 the 2-copy minimum is **strictly superadditive**: `min G₂ = −0.13639057368 < 2 · min G₁ = −0.13606794604` (gap 3.2·10⁻⁴), attained at a slightly entangled anchor (Schmidt `[0.99992, 0.01304, 2.8e-5]`) and a correlated σ. The *functional* is non-additive; the *property* still tensorized at every point probed. |
| **support/rank hygiene** | The free minimisers sit on the rank-2 boundary (`σ` rank 2) but their OUTPUTS are far from singular (min spec Λ(σ*) = 0.16, Λ^c(σ*) = 0.09 at 41/100), so they are not support artifacts. Interior full-rank violators exist at 41/100 and 17/40 but **not** at 687/1600 or 43/100: as x → x_d the violation retreats to the boundary stratum. |

---

## 1. Definitions as read from disk (frozen inputs; nothing taken from the commission prose)

| object | definition | disk cite |
|---|---|---|
| channel family | `Λ_x(X) = (1−x) X + (x/2)(Tr(X)·1 − X^T)` on qutrits | `channel-capacity/werner-holevo-gap/README.md` line 3 |
| Kraus set | `K_0 = √(1−x)·1`, `K_{a+1} = √(x/2)·L_a` with `(L_a)_{jk} = ε_{ajk}` (4 operators) | verified against the closed form to 8.9e-16 (§2 gate 1); convention consistent with `notes/WHGAP_P15A_STRICTNESS_20260730.md` §"Standing failure modes" item 3 |
| complement | `Λ^c(Y)_{ab} = Tr(K_a Y K_b^†)`, padded 4-dim | `notes/WHGAP_P15A_STRICTNESS_20260730.md` line 622; `artifacts/whgap_r9_review_20260801.md` §1.2 (type audit) lines 110–116 |
| functional | `G(ψ,σ) = D(Λ^c(P_ψ) ‖ Λ^c(σ)) − D(Λ(P_ψ) ‖ Λ(σ))` | node `WHGAP.pure-anchor-order` lines 24–25 |
| property | `P_b2` = "`G(ψ,σ) ≥ 0` for all pure ψ and all states σ" | node lines 22–26 |
| decomposition identity | `Σ_u p_u G(ψ_u,σ) = −I_c(σ)` for every pure decomposition of σ | `notes/WHGAP_P15A_STRICTNESS_20260730.md` §A1.1; **PROVED-tier per R9 §6** (`artifacts/whgap_r9_review_20260801.md` lines 375–377) |
| frozen baseline | violations at x = 2/5 and x = 41/100; bounded null at 9/20 and 49/100; death point in (0.41, 0.45) | `artifacts/whgap_r9_review_20260801.md` §7 (lines 404–424) and §6 (lines 395–399) |
| calibration reference | R9's own strip re-scan: `inf G(41/100) = −0.0680339730197`, 168/200 restarts negative | `artifacts/whgap_r9_review_20260801.md` line 413 |

**Type audit (rule 7a, for my own displays).** `P_ψ`: 3×3 (9×9 at two copies) Hermitian rank 1;
`Λ(·)`: 3×3 → 3×3 (9×9 → 9×9); `Λ^c(·)`: 3×3 → 4×4 (9×9 → 16×16); the two relative entropies
in `G` therefore live in **different dimensions** — the cancellation in §2.1 is an
isospectrality statement, not a dimension-matching one. `Λ^†` and `(Λ^c)^†` map the output
spaces back to 3×3 (9×9) and are unital (`Σ_a K_a^† K_a = 1`), which is what §5.1 uses. At two
copies the complement of `Λ⊗Λ` is `Λ^c⊗Λ^c` under the product Stinespring isometry; relative
entropies are invariant under the isometric freedom in the choice of complement, so `G₂` is
well defined.

---

## 2. Instrument (my own; provenance recorded)

`tools/whgap_p15b_core.py`, written from the definitions above. I did not read or import any
`tools/whgap_p15a_*.py` or `tools/whgap_r9_*.py` code; the only P15-A/R9 inputs I used are the
*definitions* in the table above and the *reference values* used as calibration targets.

### 2.1 The reduction that makes this instrument sharper than its predecessors

For a pure input, `Λ(P_ψ)` and `Λ^c(P_ψ)` are the two marginals of a pure vector, hence
isospectral (P15-A §A1.2(ii); R9 §1.1). Therefore

```
G(ψ,σ) = Tr[Λ(P_ψ) log Λ(σ)] − Tr[Λ^c(P_ψ) log Λ^c(σ)] = ⟨ψ| W(σ) |ψ⟩,
W(σ) := Λ^†( log Λ(σ) ) − (Λ^c)^†( log Λ^c(σ) ),        (Λ^c)^†(Z) = Σ_{ab} Z_{ab} K_a^† K_b .
```

`G` is a **quadratic form in the anchor**, so

```
min over pure ψ of G(ψ,σ)  =  λ_min( W(σ) ),   attained at the lowest eigenvector.
```

Consequences: (i) the anchor is minimised EXACTLY, not searched — every reported null covers
*all* pure anchors at every σ visited, which a joint (ψ,σ) search does not; (ii) the search
space drops from 24 to 18 real parameters at one copy and from 180 to 162 at two copies;
(iii) at two copies "product and entangled anchor starts" become vacuous as a distinction —
the exact minimiser is returned and I report its Schmidt spectrum instead.
The hit rate at x = 41/100 rose from R9's 168/200 to my 170/200 at a much lower cost per
restart, and the *same* minimum value is returned.

### 2.2 Gates on the instrument (log `p15b_phase0.log`, §"instrument gates")

| gate | worst deviation over 7 values of x × 30 random instances |
|---|---|
| Kraus sum = closed form `Λ_x` | 8.882e-16 |
| adjoint identity `Tr[Z Λ^c(Y)] = Tr[(Λ^c)^†(Z) Y]` | 7.106e-15 |
| adjoint identity `Tr[Z Λ(Y)] = Tr[Λ^†(Z) Y]` | 7.324e-15 |
| pure-input isospectrality `spec Λ(P_ψ) = spec Λ^c(P_ψ) \ {0}` | 5.551e-16 |
| **c ≥ 2 identity gate**: reduced `⟨ψ|W(σ)|ψ⟩` vs the DEFINITIONAL four-term `G` (four independent eigendecompositions, isospectrality NOT used) | 9.992e-16 |

The definitional cross-check is re-run at **every** reported optimum (column `|G_def − G|` in
the logs; worst 4.8e-15 anywhere in this run), so no headline number rests on the reduction.

**Value-vs-formula (7f).** The instrument gates verify VALUES of an independent construction.
The one FORMULA-level claim in this note is `G*(x)` in §4, checked below both ways.

### 2.3 Negative controls (log `p15b_phase0.log`)

- **x = 11/20** (P_b2 must hold: cRE domination PROVED there, P2/P4 + R5b): 120 restarts,
  `min = +9.9968e-12`, **0 hits**. The minimiser runs into the σ → pure corner where
  `G → 0⁺` — the same degenerate stall R9 documented; the value is the barrier, not an
  interior minimum (see §3.3).
- **x = 1/5** (Q > 0 PROVED, so P_b2 must fail): `min = −11.3296`, hit rate 0.783. The
  pipeline does detect violations.

---

## 3. Phase 0 and Phase 1 — calibration and localization

### 3.1 GATE G-P15B-1 — **PASS** (log `p15b_phase0.log`, JSON `p15b_phase0.json`)

```
x = 41/100, 200 L-BFGS-B restarts, 18-parameter sigma chart
hit rate (G < -1e-7)  : 0.850  (170/200)
min G (float64)       : -0.068033973020
G definitional        : -0.068033973020        (|diff| = 8.33e-17)
spec sigma*           : [2.951944e-16, 4.421955e-01, 5.578045e-01]      (RANK 2)
min spec Lambda(s*)   : 1.615351036e-01     min spec Lambda^c(s*) : 9.065007284e-02
I_c(sigma*)           : -0.043235451160     (so -I_c > 0: the decomposition average is positive)
mpmath 60 dps         : G = -0.0680339730196980833689685022337685252422370345
R9 reference (disk)   : -0.0680339730197
```

Not a support artifact: both output states are bounded away from singular by ~1e-1. The gate
is passed at 46 printed digits, well past the required 40.

### 3.2 Restart count for the scan (detection-power reasoning, pre-registered)

At the calibration point the per-restart hit rate is `p = 0.85`. Across the whole scan the
measured hit rate degrades smoothly (0.85, 0.81, 0.64, 0.46 at 0.410 → 0.425, and 0.34–0.38 at
the three bisection points), never falling below 0.34 at any point where a violation exists.
With **N = 200** restarts, a violation whose basin has fraction `p` is missed with probability
`(1−p)^N`: `p = 0.34 ⇒ 10⁻³⁵`, and even `p = 0.015` (a basin 20× thinner than anything
observed) is caught with probability 95%. N = 200 is therefore the calibrated budget, and I
use it at every scan and bisection point. This is a statement about basin volume in my chart,
not a guarantee that no violation exists on a measure-zero stratum invisible to random starts
— see §6.

### 3.3 Coarse scan and bisection (log `p15b_phase1.log`, JSON `p15b_phase1.json`)

| x | min G (float64) | hits/200 | ⟨ψ|σ|ψ⟩ | spec σ at the minimum | verdict |
|---|---|---|---|---|---|
| 41/100 = 0.410 | −6.8033973020e-02 | 170 | 0.00406 | [0, 0.44220, 0.55780] | VIOLATION |
| 83/200 = 0.415 | −5.0215713000e-02 | 162 | 0.00000 | [0, 0.5, 0.5] | VIOLATION |
| 21/50 = 0.420 | −3.2765258045e-02 | 128 | 0.00000 | [0, 0.5, 0.5] | VIOLATION |
| 17/40 = 0.425 | −1.5654542656e-02 | 92 | 0.00000 | [0, 0.5, 0.5] | VIOLATION |
| 171/400 = 0.4275 | −7.2252799730e-03 | 68 | 0.00000 | [0, 0.5, 0.5] | VIOLATION |
| 343/800 = 0.42875 | −3.0419495390e-03 | 72 | 0.00000 | [0, 0.5, 0.5] | VIOLATION |
| 687/1600 = 0.429375 | −9.5808218734e-04 | 75 | 0.00000 | [0, 0.5, 0.5] | VIOLATION |
| 43/100 = 0.430 | +9.9980284536e-12 | 0 | 1.000000 | [0, 0, 1] | bounded null |
| 87/200 = 0.435 | +9.9978042160e-12 | 0 | 1.000000 | [0, 0, 1] | bounded null |
| 11/25 = 0.440 | +9.9983757970e-12 | 0 | 1.000000 | [0, 0, 1] | bounded null |
| 89/200 = 0.445 | +9.9978709460e-12 | 0 | 1.000000 | [0, 0, 1] | bounded null |
| 9/20 = 0.450 | +9.9970594533e-12 | 0 | 1.000000 | [0, 0, 1] | bounded null |

**Reading the null rows honestly.** The `+1e-11` entries are NOT interior minima: the
optimizer walks into the degenerate corner `σ → P_ψ` (fidelity 1.000000, `min spec Λ^c(σ)`
pinned at my 1e-11 support floor), where `G → 0⁺`. This is the R8-m1 / R9 stall, reproduced.
The honest statement at those points is **`inf G = 0`, approached degenerately, no negative
value found** — identical in kind to R9's `−3.56e-14` corner values at 9/20. §3.5 supplies the
interior minima that the corner value hides.

**GATE G-P15B-2 — PASS.**

```
bracket [x_viol, x_null] = [687/1600, 43/100] = [0.429375, 0.430000],  width 6.25e-4
```

(coarse bracket [17/40, 43/100] of width 5.0e-3, narrowed by 3 bisection steps).

### 3.4 Violation certificates (mpmath, 60 dps, at the exact float64 pair)

Every violating point carries a certificate: the float64 pair `(ψ, M)` is an exact binary
rational, promoted to mpmath and re-evaluated **definitionally** (four eigendecompositions of
the four output states, no use of the reduction) at 60 working digits.

| x | G at 60 dps |
|---|---|
| 41/100 | `-0.0680339730196979005877496555944154427235593376` |
| 83/200 | `-0.0502157129997620829265121635230430517506732074` |
| 21/50 | `-0.0327652580450264329684604236080204580017181748` |
| 17/40 | `-0.0156545426563957671652913815774111379064333` |
| 171/400 | `-0.00722527997304623863046315028078755595146056917` |
| 343/800 | `-0.00304194953896796971827893132065841180646057253` |
| **687/1600** | `-0.000958082187335739016576963432971724083214401877` |

Per R9 non-claim 4 (endorsed): these strings are exact evaluations *of a float64 state*, so
only the leading ~8 digits are properties of the minimiser; what the 60 digits certify is that
**the exhibited pair has `G < 0`**, which is all a violation certificate needs. The states are
in `p15b_phase1.json` (`certificates.<x>.r.psi` and `.params`).

### 3.5 Support / rank-degeneracy hygiene (log `p15b_fullrank.log`, JSON `p15b_fullrank.json`)

The free minimisers are rank-2 states. To exclude the exact-zero-mode trap (R5a) and to
reproduce R9's interior protocol, I re-ran with `σ = (1−f)·σ(M) + f·1/3`, so `min spec σ ≥ f/3`
by construction (60 restarts per cell, 60-dps certificate on each):

| x | floor f | min G | spec σ | −I_c(σ) | min spec Λ(σ) / Λ^c(σ) |
|---|---|---|---|---|---|
| 41/100 | 0.03 | **−6.3102503072e-02** | [0.0100, 0.4950, 0.4950] | +4.373e-02 | 2.09e-01 / 1.04e-01 |
| 41/100 | 0.15 | **−4.5110645498e-02** | [0.0500, 0.4750, 0.4750] | +3.979e-02 | 2.24e-01 / 1.08e-01 |
| 17/40 | 0.03 | **−1.2118199551e-02** | [0.0100, 0.4950, 0.4950] | +5.989e-02 | 2.16e-01 / 1.07e-01 |
| 17/40 | 0.15 | +7.7790649742e-04 | — | +5.725e-02 | 2.31e-01 / 1.12e-01 |
| 687/1600 | 0.03 | +2.1777046836e-03 | — | +9.274e-03 | 1.00e-02 / 4.29e-03 |
| 687/1600 | 0.15 | +1.1240976411e-02 | — | +2.853e-02 | 5.00e-02 / 2.15e-02 |
| 43/100 | 0.03 | +2.1899160552e-03 | — | +9.351e-03 | 1.00e-02 / 4.30e-03 |
| 43/100 | 0.15 | +1.1306510126e-02 | — | +2.882e-02 | 5.00e-02 / 2.15e-02 |
| 9/20 | 0.03 | +2.5691504487e-03 | — | +1.176e-02 | 1.00e-02 / 4.50e-03 |
| 9/20 | 0.15 | +1.3335014215e-02 | — | +3.772e-02 | 5.00e-02 / 2.25e-02 |

Three things to read off.

1. **Interior full-rank violators exist at 41/100 and at 17/40 = 0.425**, deep inside the state
   space, with `−I_c(σ) > 0` computed directly at that σ (not inferred): the decomposition
   average is positive while one term is negative — R9's decomposition-visible mechanism,
   now confirmed at a *strip* point up to 0.425.
2. **They do not exist near x_d.** At 687/1600 (a violating point!) and at 43/100 the floored
   minimum is already positive at `f = 0.03`. So as `x ↑ x_d` the violation retreats onto the
   rank-2 boundary stratum; at the death point it is a boundary phenomenon only.
3. The null rows are genuine **interior** minima (no corner stall, `fidelity < 1`), which is
   the missing content of the `+1e-11` rows of §3.3.

---

## 4. The death point in closed form (the sharpest result of this run)

### 4.1 The stratum

At x = 0.415, 0.420, 0.425 (and at 0.4295, 0.4296) the 200-restart global minimiser is, to
13 digits, **exactly**

```
psi real (tau = |psi^T psi| = 1),      sigma = ( 1 - P_psi ) / 2
```

— the maximally mixed state on the orthogonal complement of the anchor (`⟨ψ|σ|ψ⟩ = 0`,
`spec σ = [0, 1/2, 1/2]`, `‖σ − (1−P_ψ)/2‖ ≤ 2.4e-8`). Because `Λ_x` is O(3)-covariant we may
take `ψ = e_1`; then all four matrices are diagonal:

```
Lambda(P)     = diag(1-x, x/2, x/2)          Lambda(sigma)   = diag(x/2, (2-x)/4, (2-x)/4)
Lambda^c(P)   = diag(1-x, 0, x/2, x/2)       Lambda^c(sigma) = diag(1-x, x/2, x/4, x/4)
```

so `D_E = x·log 2` and `D_B = (1−x)log(2(1−x)/x) + x·log(2x/(2−x))`, giving

> **`G*(x) = (1−2x) log x + x log(2−x) − (1−x) log(1−x) − (1−x) log 2`**  (nats).

**Checks (log `p15b_stratum.log`).** Against the definitional four-term `G` built from the
generic Kraus code in float64: worst deviation **3.886e-16** over x ∈ {2/5, 41/100, 17/40,
43/100, 9/20, 11/20}. Against the diagonal definition evaluated at 60 dps: worst deviation
**7.78e-62**. This is a FORMULA-level identity in x (the only one in this note); the reviewer
should re-derive it independently rather than re-run my check.

### 4.2 The root

```
x_d = 0.42966287456589232412005619893737910757142031486046      (50 digits, mpmath findroot)
G*'(x_d) = 3.32621288542 > 0      (simple, transversal crossing)
G*(0.4296) = -2.0916e-4      G*(0.4297) = +1.2348e-4      G*(0.43) = +1.1206e-3
```

`x_d` lies strictly inside the independently obtained search bracket `[0.429375, 0.430000]` —
two different instruments, one exact-form and one stochastic, agreeing.

### 4.3 Is the stratum globally optimal? (bounded search, log `p15b_stratum.log`)

| x | global min (200 restarts) | `G*(x)` | difference | hits | τ(ψ) | ‖σ − (1−P_ψ)/2‖ |
|---|---|---|---|---|---|---|
| 859/2000 = 0.42950 | −5.419315541355e-04 | −5.419315541343e-04 | −1.3e-15 | 67 | 1.000000000 | 2.3e-08 |
| 537/1250 = 0.42960 | −2.091604276932e-04 | −2.091604276914e-04 | −1.9e-15 | 72 | 1.000000000 | 2.3e-08 |
| 2149/5000 = 0.42980 | +9.997443797e-12 (corner) | +4.559836123e-04 | — | **0** | — | — |

So immediately below `x_d` the global minimum **equals** the closed form to machine precision,
and immediately above it there is no violation. **Conditional on the stratum remaining globally
optimal in a neighbourhood of `x_d`** — a bounded-search statement, not a theorem — the death
point of `P_b2` for this family is exactly the root above.

**One honest wrinkle (unresolved, and it does not affect `x_d`).** At x = 41/100 the global
minimum is `2.37e-5` BELOW the stratum value (`−0.068033973` vs `G*(0.41) = −0.068010234`).
That minimiser has `τ(ψ) = 0.918` (a genuinely complex anchor), `⟨ψ|σ|ψ⟩ = 0.0041` and
`spec σ = [0, 0.4422, 0.5578]`. I probed the obvious one-parameter escape — unbalancing
`σ = diag(0, s, 1−s)` at real `ψ` — and found `s_opt = 1/2` at **every** x from 0.405 to 0.429
(`p15b_stratum.log`, last block), so the extra gain at 0.41 comes from the complex-anchor
direction, not from unbalancing. I did not chase that branch: it lies below 0.415, it only
makes `G` more negative, and every point at and above 0.415 is on the stratum to 13 digits.
A reviewer should treat "the stratum is globally optimal on [0.415, x_d]" as NUMERICAL.

---

## 5. Phase 2 — does P_b2 tensorize?

### 5.1 A structural fact that reshapes the question (gate S, log `p15b_phase2.log`)

`Λ^†` and `(Λ^c)^†` are unital, so for a **product** second argument

```
W_2(sigma_1 (x) sigma_2) = W(sigma_1) (x) 1 + 1 (x) W(sigma_2)
```

(checked numerically at 3 values of x × 5 random product states: worst deviation 3.776e-15).
Hence `min_ψ G₂(ψ, σ₁⊗σ₂) = min G₁(·,σ₁) + min G₁(·,σ₂)`, attained at a **product** anchor.

> **Consequence.** 2-copy `P_b2` restricted to product σ is *equivalent* to 1-copy `P_b2`.
> Entangling the anchor alone can never produce a 2-copy violation; **any** 2-copy violation
> requires a **correlated σ**. The tensorization question is therefore entirely a question
> about correlated second arguments — which is exactly where I directed the search.

(The same computation shows the additivity `G₂(ψ₁⊗ψ₂, σ₁⊗σ₂) = G₁ + G₁`, verified to 7.8e-16.)

### 5.2 2-copy calibration at x = 41/100 (where the 1-copy property fails)

```
min G_2 = -1.3639057368e-01     hits 23/24 restarts
2 x min G_1 = -1.3606794604e-01  (product doubling)      ->  CALIBRATION PASS
psi Schmidt spectrum   = [0.999915, 0.0130377, 0.0000278]   (slightly ENTANGLED)
||sigma - marg (x) marg|| = 0.0412                          (slightly CORRELATED)
```

The 2-copy instrument reproduces at least the embedded product violation, so it is calibrated.
**New (NUMERICAL):** it does strictly better — `min G₂ < 2·min G₁` by `3.23e-4`, i.e. the
violation depth is **superadditive**, achieved by correlating σ and slightly entangling the
anchor. The *functional* is therefore not additive. This is a statement about the depth of an
already-existing violation; it is **not** a non-tensorization of the *property*, which needs a
violation at a 1-copy-null x.

### 5.3 The probe on the surviving side (logs `p15b_phase2.log`, `p15b_phase2b.log`)

1-copy state of the probe points first (same instrument, 120 restarts): `min G = +1.0e-11`,
**0 hits** at both 23/50 = 0.46 and 12/25 = 0.48 — the property holds there (bounded null).

| x | search | restarts (product / generic / entangled) | min G₂ | hits | reading |
|---|---|---|---|---|---|
| 23/50 = 0.46 | free | 20 / 40 / 20 | +9.4992e-10 | 0/80 | corner stall (fid 1.000, `min spec Λ^c` at floor) |
| 12/25 = 0.48 | free | 20 / 40 / 20 | +4.6426e-10 | 0/80 | corner stall |
| **43/100 = 0.43** (just above `x_d`) | free | 8 / 16 / 8 | +2.9453e-09 | 0/32 | corner stall; restart quantiles (0,10,50,90) = (2.9e-9, 3.7e-8, 2.2e-6, 1.1e-3) |
| 43/100 | interior, `min spec σ ≥ 5.6e-3` | 8 / 16 / 8 | **+4.5919e-03** | 0/32 | genuine interior minimum, positive |
| 23/50 | interior, `min spec σ ≥ 5.6e-3` | 8 / 16 / 8 | **+5.7185e-03** | 0/32 | genuine interior minimum, positive |

At every optimum the definitional four-term `G₂` was recomputed (worst `|G_def − G|` = 3.1e-15).
The interior runs are what make this a real null rather than a barrier reading.

**GATE G-P15B-3: PASS** (a verdict at ≥ 2 surviving-side points; three delivered).
**Verdict: BOUNDED NULL — no 2-copy violation found where the 1-copy property holds.** So the
P15 route to `Q = 0` on `(x_d, 1/2)` **survives its first tensorization test**. This is
NUMERICAL evidence of survival, not evidence of tensorization: a null over 80 restarts in a
162-parameter search space is thin coverage, and I say so in §6.

### 5.4 Search budget and protocol of the null (mandatory statement)

Free searches: L-BFGS-B with an **analytic gradient** (envelope theorem + Fréchet derivative of
the matrix log; validated against central finite differences, worst relative deviation 1.6e-9),
`maxiter = 2000`, from 80 (0.46, 0.48) and 32 (0.43) random starts split across three start
families — product `M₁⊗M₂`, generic complex 9×9, and maximally-entangled-seeded. Anchors are
minimised exactly (§2.1), so the null covers **all** pure anchors — product and entangled — at
every σ visited. Interior searches: `σ = 0.95·σ(M) + 0.05·1/9`, 32 starts each. Chart:
`σ = MM^†/Tr`, 162 real parameters. Support floor 1e-11 on both outputs; any σ violating it is
rejected as invalid, which is what produces the σ → pure corner barrier.

---

## 6. Honest coverage statement

1. **Everything here is NUMERICAL and unreviewed** (`pending-review:`), except where it cites
   an already-reviewed disk result. The only FORMULA-level item is `G*(x)` (§4.1).
2. **The bracket is a bounded-search statement.** `x_viol = 687/1600` is certified (60-dps
   negative value at an exhibited pair). `x_null = 43/100` means only: 200 restarts of my
   optimizer found nothing negative, at a point where the calibrated basin fraction would have
   been ≥ 0.34 had a violation of the observed kind existed. It is not a proof that
   `P_b2` holds at 43/100.
3. **`x_d` is exact only for the orthocomplement stratum.** The identification of the stratum
   root with the true death point rests on the numerical global-optimality check at five points
   (§4.3) and would be upgraded by a proof that the stratum minimises `G` for x in a
   neighbourhood of `x_d` — see follow-up F1.
4. **The 41/100 off-stratum wrinkle is unresolved** (§4.3). It affects the shape of `min G(x)`
   below 0.415, not the death point.
5. **The 2-copy null is thin.** 80 (resp. 32) restarts in 162 real dimensions cannot exclude a
   violation on a small or lower-dimensional stratum. The 1-copy experience is a direct
   warning: the violation near `x_d` lives on the **rank-2 boundary** (§3.5), a measure-zero
   set that random full-rank starts reach only because the barrier pushes them there. I did
   not run a boundary-restricted 2-copy search (rank-deficient σ on the 9×9 side) — that is
   follow-up F2 and it is the single most likely place for a 2-copy violation to hide.
6. **No `Q`-consequence is claimed anywhere.** R8 MAJOR 3 stands: `P_b2 ⟹ Q^(1) = 0`, never
   the converse, so the violations recorded here say nothing about `Q(Λ_x)` on `[2/5, x_d)`.
   In particular this note does **not** touch `WHGAP.onset-two-fifths`.
7. **Superadditivity (§5.2) is one data point at one x**, from a 24-restart run. It should be
   re-measured before it is used for anything.
8. Compute: **local only** (`tools/pypinned.cmd` → `C:\Users\wtaph\pyrt311\python.exe`, numpy
   1.26.4, scipy 1.14.1, mpmath 1.3.0). The Mac Studio was NOT used — the analytic gradient
   made the 2-copy phase a 60-second local job. No credentials appear in any artifact.

### Standing failure modes screened (R5 §2)

1. no sympy `.H` / unresolved radicals — no symbolic layer in this run; the closed form of §4
   was derived by hand and checked numerically at 60 dps two independent ways.
2. pinned interpreter throughout (never WindowsApps python for the mathematics).
3. complement convention re-derived from the Kraus list and gate-checked against the closed
   form (8.9e-16).
4. `.conj().T` everywhere; realness of the Kraus operators never assumed.
5. no `sorted()` on symbolic eigenvalues (none exist here).
6. `SHA256SUMS.txt` written with LF and verified with `sha256sum -c`.
7. degeneracy bookkeeping: explicit support floor 1e-11 on both outputs, `min spec Λ(σ)` and
   `min spec Λ^c(σ)` printed at every optimum, rank of σ printed as its full spectrum; the
   corner-stall rows are labelled as such rather than reported as minima.
8. `ε log ε`: not used; nothing here is perturbative around a pure state.
9. anchoring: my optimizer and my `G` were written from the definitions and gate-checked
   before I compared any value with R9's; the comparison is a calibration target, and the
   commission (correctly) made reproducing it a hard gate.
10. **caught defect, recorded not silently repaired:** my first Phase-2b driver called
    L-BFGS-B without the analytic gradient on the 162-parameter problem (163 function
    evaluations per gradient); it was killed after ~6 minutes without producing output, the
    driver was switched to `jac=True`, and the same run then took 14.7 s. No result was
    computed by the discarded version, so nothing was replaced — only the runtime.

---

## 7. What this changes on `WHGAP.pure-anchor-order` (for the decision layer; I edit no node)

- **Obligation 2 ("does it hold on the strip") — largely answered, negatively, and sharply.**
  `P_b2` is violated at every x in `[2/5, 0.429375]` tested and holds (bounded null) from
  `0.43` upward. The candidate's surviving domain is `(x_d, 1/2)` with
  `x_d = 0.42966287456589232412005619893737910757142031486046` (exact-form root of
  `G*(x) = 0`, §4). The strip `[2/5, 1/2)` is therefore **split**: `P_b2` is dead on roughly
  its first 60%, alive on the rest.
- **Obligation 3 (tensorization) — first data, and the question is now structurally sharper.**
  `2`-copy `P_b2` with product σ ⟺ 1-copy `P_b2` (§5.1), so tensorization is entirely about
  correlated second arguments. At three surviving-side points a bounded 2-copy search found no
  violation: the route survives (NUMERICAL).
- **Suggested node wording** (decision layer's call): "P_b2 is numerically DEAD on
  [2/5, x_d) and alive on a bounded search for x ≥ 0.43, with x_d the root of an exact
  stratum equation; 2-copy tensorization survives a first bounded probe."
- Nothing here bears on `WHGAP.onset-two-fifths`, `WHGAP.qpositive-onset` or any Q-statement.

## 8. Follow-up proposals (registered here only; rule 8b write is the decision layer's)

- **F1 — prove the stratum is the minimiser.** Show that for x in a neighbourhood of `x_d`,
  `min_{ψ,σ} G = G*(x)` with the minimum at `(ψ real, σ = (1−P_ψ)/2)`. The pieces are
  encouraging: O(3)-covariance reduces `ψ` to `τ = |ψ^Tψ|`, and the numerics say the optimum
  is `τ = 1` with a balanced orthocomplement. This would make `x_d` an exact analytic
  threshold — a third exactly-known threshold on this family alongside `2/5` and `1/2`.
- **F2 — boundary-restricted 2-copy search.** Redo Phase 2 with σ constrained to low rank on
  the 9×9 side (rank 2–4), and with anchors in the kernel — the geometry that carries the
  1-copy violation near `x_d`. This is the cheapest test that could still overturn §5.3.
- **F3 — measure the superadditive gain as a function of x.** `min G₂(x) − 2 min G₁(x)` was
  `−3.2e-4` at 41/100. If that gap survives (relatively) as `x ↑ x_d`, a 2-copy violation
  above `x_d` becomes plausible and F2 knows where to look; if it collapses, the null firms up.
- **F4 — is `x_d` a `P_b2`-vs-`cRE` separation point?** P15-A §A3.1 puts
  antidegradable ⟹ cRE ⟹ `P_b2` ⟹ `Q^(1)=0`, and cRE's exact boundary is `1/2` (PROVED, R5b).
  A `P_b2` survivor on `(x_d, 1/2)` would separate `P_b2` from cRE strictly. The interval is
  now explicit and short, which makes this a concrete question rather than a slogan.
- **F5 — n = 3.** Only if F2 comes back null: the same reduction and gradient work at three
  copies (27-dim anchors, 729-parameter σ) and would cost minutes, not hours.

---

## Reproduction

Interpreter `tools/pypinned.cmd` (CPython 3.11.9: numpy 1.26.4, scipy 1.14.1, mpmath 1.3.0).
From the repository root:

```
tools/pypinned.cmd -u tools/whgap_p15b_phase0.py   > artifacts/logs_whgap_p15b_20260801/p15b_phase0.log
tools/pypinned.cmd -u tools/whgap_p15b_phase1.py 200 > artifacts/logs_whgap_p15b_20260801/p15b_phase1.log
tools/pypinned.cmd -u tools/whgap_p15b_stratum.py  > artifacts/logs_whgap_p15b_20260801/p15b_stratum.log
tools/pypinned.cmd -u tools/whgap_p15b_fullrank.py 41/100 17/40 687/1600 43/100 9/20 > artifacts/logs_whgap_p15b_20260801/p15b_fullrank.log
tools/pypinned.cmd -u tools/whgap_p15b_phase2.py   > artifacts/logs_whgap_p15b_20260801/p15b_phase2.log
tools/pypinned.cmd -u tools/whgap_p15b_phase2b.py  > artifacts/logs_whgap_p15b_20260801/p15b_phase2b.log
```

Script and log SHA-256 in `artifacts/logs_whgap_p15b_20260801/SHA256SUMS.txt` (LF, with a
convention header; this note is NOT in the ledger — it is a live co-edited file, R13 m8 rule).
Total wall time ≈ 27 minutes, single machine, no remote compute.

---

## R16 application (decision layer, 2026-08-01) — dated corrections per the review

R16 ([whgap_r16_review_20260801.md](../../../artifacts/whgap_r16_review_20260801.md)):
**LICENSE A, 0 MAJOR, 6 minors, 4 upgrades.** The minors are applied here append-only
(the body above is left as written; where a body sentence conflicts with this section,
THIS section governs):

- **m1 (domain of W):** the quadratic-form reduction is stated for σ with rank ≥ 2. For
  rank-1 σ, Λ^c(σ) is singular and G = +∞, so such σ can never witness a violation and
  the reduction is scope-complete for P_b2.
- **m2 (cross-reference):** §6.3's "five points (§4.3)" should read: the five
  stratum-optimality points are 0.415 / 0.420 / 0.425 (§4.1) + 0.4295 / 0.4296 (§4.3).
  The count is right; the pointer was wrong.
- **m3 (mechanism sentence):** §3.5 reading 3 called the floored null rows "genuine
  interior minima (no corner stall)". Their printed min spec Λ(σ) = floor/3 shows they
  ARE the σ→pure, τ=0 corner regularized by the floor. The CONCLUSION (no interior
  full-rank violator near x_d) survives — R16 independently confirms the floored stratum
  state (+2.20e-3 at 687/1600, +4.23e-3 at 43/100) — only the mechanism wording was wrong.
- **m4 (certificate normalization):** the 46-digit certificate strings are properties of
  the recorded pairs *under unit normalization of ψ* (recorded ‖ψ‖ = 1 + O(1e-16));
  beyond ~15 digits the digits depend on that convention. Signs unaffected.
- **m5 (2-copy minimum is a bound):** the 41/100 2-copy minimum is a BOUND
  min G₂ ≤ −0.1363905737, not an equality — R16's own descent reaches −0.1363906031
  (under-convergence in the conservative direction; the superadditive gap stands).
- **m6 fold-in (§2.3 wording):** "Q > 0 PROVED, so P_b2 must fail" is a valid inference
  only with the word **single-letter**: P_b2 ⟹ Q^{(1)} = 0, and the PROVED positivity on
  (0, 2/5) is single-letter (Q^{(1)} > 0 via the witness family), which is what
  contradicts P_b2 there. (The nested-outline half of m6 is fixed in the DAG doc itself.)

**Upgrades registered (R16-authored, reviewer-verified):**
- **U1:** G*(x) is verified at FORMULA level (independent symbolic derivation, residual
  exactly 0) — carried on the node as a reviewer-verified identity.
- **U2:** the violation side is ANALYTIC modulo a monotonicity lemma (G* < 0 at all 1718
  50-dps grid points below x_d, > 0 at all 281 above; G*′ > 0 throughout; G*(0⁺) = −∞;
  G*(1/2) = +0.2027). The lemma is now supplied by the decision layer:
  [WHGAP_P15B_MONOTONICITY_LEMMA_20260801.md](WHGAP_P15B_MONOTONICITY_LEMMA_20260801.md)
  (pending-review). Together: P_b2 fails at EVERY x < x_d, pending that single review.
- **U3:** exact rational endpoint certificate — ψ = e₁, σ = diag(0, 1/2, 1/2),
  x = 687/1600: G = −0.000958082187335938228207335155849733… (60 dps), every digit a
  property of an exactly specified pair.
- **U4:** tightened bracket **[0.42966287, 0.4297]** (width 3.7e-6), with the global
  minimum tracking G* to 5 digits at 4.6e-9 below x_d — materially stronger
  global-optimality corroboration than the body's 5 points (still NUMERICAL; F1 remains
  the proof obligation).

