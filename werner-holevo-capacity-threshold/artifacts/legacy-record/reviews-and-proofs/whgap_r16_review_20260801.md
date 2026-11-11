# WHGAP R16 — independent rule-7 review of the P15-B package (death point + tensorization)

Reviewer: R16, a FRESH Opus 5 instance, 2026-08-01. Commission:
`channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_R16_20260801.md` (frozen).
Reviewed work: `notes/WHGAP_P15B_DEATHPOINT_20260801.md`, `artifacts/logs_whgap_p15b_20260801/`,
`tools/whgap_p15b_*.py`.

**Independence statement.** I did not author P15-B, P15-A, R8 or R9. I was given no desired
outcome: the commission states explicitly that LICENSE and FINDINGS are equally acceptable, and
I formed the verdict only after running my own instrument. My scripts (`tools/whgap_r16_*.py`)
were written from the CLAIM alone; `tools/whgap_p15b_core.py` was opened only AFTER my own
derivation, my own code, and the run `r16_item12.log` were complete and on disk (rule 7c).

---

## PRE-ACTION REPORT

- **Target node / status as read from disk:** `WHGAP.pure-anchor-order` (alias P15) —
  **`status: OPEN`, `disposition: null`**
  (`channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.pure-anchor-order.md` front matter
  lines 2–14; row `P15` of `proof-dag/NODE_INDEX.md` line 127; DAG outline line 345).
- **My ROLE:** REVIEWER. **Independence:** see statement above.
- **Highest status my evidence could license (§2 ladder):** as a fresh independent reviewer
  completing an archived rule-7 review, my report can open the **completion gate** — i.e. it can
  license the decision layer to write **CERTIFIED\*** (or **PROVED** for the items where I
  independently re-derived a formula-level identity) on the reviewed *content*. I write no status
  myself: rule 6 reserves the write to the checker/decision layer with the review cited, and the
  commission forbids me any node/index/DAG edit. Everything of P15-B's own authorship stays
  NUMERICAL `pending-review:` until that write happens.
- **Gates / deliverables of my commission, one line each:** (1) re-derive the quadratic-form
  reduction by my own route with a type audit; (2) derive `G*(x)` symbolically AND at ≥50 dps and
  re-solve `x_d`; (3) re-verify both bracket endpoints with my own optimizer plus my own power
  reasoning; (4) spot-check ≥3 of the 7 certificates with support/rank status; (5) verify the
  `W₂` additivity identity and the 41/100 2-copy calibration + superadditivity with my own 2-copy
  code; (6) null-scope honesty audit; (7) no-Q-consequence audit; (8) value-vs-formula statements;
  then the licensing menu. Deliverables: this report, `tools/whgap_r16_*.py`, `r16_*` logs added
  to `artifacts/logs_whgap_p15b_20260801/` with my own `SHA256SUMS_r16.txt`.
- **Conflicts between commission text and the disk protocols:** **none.** One observation, not a
  conflict: the commission's single-writer restriction (no node/index/DAG edits) suspends my
  §5/§6 DAG write duties; the atomic-update obligation therefore falls to the decision layer, and
  this report contains everything needed for it.
- **One disk sync-drift noticed while reloading (decision layer's to fix, not mine):** the DAG
  file's nested outline still reads *"`WHGAP.pure-anchor-order` … P15-A commission on disk, not
  executed — agent died on session limit"* (`notes/WERNER-HOLEVO-GAP_PROOF_DAG.md` lines 345–347)
  while the same file's header (lines 3–7) records P15-B as landed. Recorded as minor **m6**.

---

## 0. Verdict

**(A) — P15-B is LICENSED AS RECORDED.** The bracket, the exact-form candidate (as candidate),
and the tensorization bounded null all stand at NUMERICAL with accurate scope wording.
**0 MAJOR, 6 minors.** Every load-bearing claim I tested reproduced under an instrument I built
myself, and two claims are STRONGER than recorded — see §9 (reviewer upgrades U1–U3).

| item | reviewer outcome |
|---|---|
| 1. quadratic-form reduction | **CONFIRMED, and re-derived independently.** Formula-level, not merely value-level. Scope caveat supplied (rank-1 σ). |
| 2. `G*(x)` and `x_d` | **CONFIRMED.** Symbolic residual exactly `0`; 60-dps definitional agreement `3.1e-61`; `x_d` reproduced to 40 digits by two root-finders. Wording ("exact on-stratum, candidate globally") is accurate. |
| 3. bracket endpoints | **CONFIRMED and TIGHTENED.** My own optimizer reproduces the 687/1600 violation and the 43/100 null (0/350); my scan narrows the death point to `[0.42966287, 0.4297]`, width `3.7e-6`. Detection-power claim does NOT outrun the instrument. |
| 4. certificates | **5 of 7 spot-checked, all CONFIRMED** at 60 dps with an independent 4-term route; support/rank status verified, no boundary artifact. |
| 5. tensorization | `W₂(σ₁⊗σ₂) = W(σ₁)⊗1 + 1⊗W(σ₂)` **PROVED by my own route** and gate-checked (`6.2e-15`); the product-σ ⟺ 1-copy consequence is correct; superadditivity at 41/100 **independently reproduced** (my own descent reaches `−0.136390603`, marginally deeper than recorded). |
| 6. null-scope honesty | **CLEAN.** The 2-copy null is presented as exactly what it is; the un-run F2 caveat survives into the note, the node, and the DAG header. |
| 7. no-Q-consequence | **CLEAN.** No sentence in the note or in any log derives a Q-statement from P_b2 data. |
| 8. value-vs-formula | stated per headline number in §8; the one FORMULA-level claim (`G*`) is the one I re-derived rather than re-ran. |

---

## 1. Item 1 — the quadratic-form reduction, re-derived by my own route (anchoring ban honored)

**My derivation, written before opening any P15-B code.** With `Λ_x(X) = (1−x)X + (x/2)(Tr X·1 − Xᵀ)`
and Kraus set `K₀ = √(1−x)·1`, `K_k = √(x/2)·L_k`, `(L_k)_{ij} = ε_{ijk}`:

1. `Σ_k L_k X L_k† = δ_{ab}Tr X − (Xᵀ)_{ab}` by `Σ_k ε_{ack}ε_{bdk} = δ_{ab}δ_{cd} − δ_{ad}δ_{cb}`,
   so the Kraus set reproduces `Λ_x` with **|E| = 4**.
2. `Λ(P_ψ)` and `Λ^c(P_ψ)` are the two marginals of the pure vector `Vψ` ⟹ isospectral ⟹
   `Tr Λ(P_ψ) log Λ(P_ψ) = Tr Λ^c(P_ψ) log Λ^c(P_ψ)`. **The two entropy terms of `G` cancel.**
   This step uses purity of the FIRST argument only; `σ` is unrestricted — exactly the class P_b2.
3. Therefore `G(ψ,σ) = Tr[Λ(P_ψ) log Λ(σ)] − Tr[Λ^c(P_ψ) log Λ^c(σ)] = ⟨ψ|W(σ)|ψ⟩` with
   `W(σ) = Λ†(log Λ(σ)) − (Λ^c)†(log Λ^c(σ))`.
4. I computed both adjoints myself: `Λ† = Λ` (the map is **self-adjoint**, and unital since
   `Λ(1)=1`), and `(Λ^c)†(M) = Σ_{jk} M_{jk} K_j† K_k`, which is unital because `Σ_j K_j†K_j = 1`.
5. `W(σ)` is Hermitian, so `min_{pure ψ} G(ψ,σ) = λ_min(W(σ))`, attained at the lowest eigenvector.

**7c coincidence flag (mandatory).** My derivation coincides notationally with the note's §2.1 —
same symbol `W(σ)`, same displayed formula. I flag this as required. It is a genuine coincidence,
not anchoring: the derivation and `tools/whgap_r16_core.py` were finished and the gate run
`r16_item12.log` was written to disk before `tools/whgap_p15b_core.py` was opened. The coincidence
is unsurprising — the reduction has essentially one natural route.

**Type audit (7a), per display.**

| object | domain → codomain | dimensions (n copies) |
|---|---|---|
| `Λ_x` | `M_{3^n}(ℂ) → M_{3^n}(ℂ)` | 3ⁿ×3ⁿ; unital, TP, self-adjoint |
| `Λ^c` | `M_{3^n}(ℂ) → M_{4^n}(ℂ)` | 3ⁿ×3ⁿ → 4ⁿ×4ⁿ (the two relative entropies live in DIFFERENT dimensions — the cancellation is isospectrality, not dimension matching) |
| `Λ†`, `(Λ^c)†` | back to `M_{3^n}` | both **unital** (adjoints of TP maps) — this is what §5.1 consumes |
| `W(σ)` | — | `3ⁿ×3ⁿ` Hermitian |
| `P_ψ` | — | `3ⁿ×3ⁿ`, rank 1 |

**Gates (c ≥ 2 on the load-bearing identity), log `r16_item12.log`:**

| gate | worst residual |
|---|---|
| Kraus completeness + `Σ K X K† = Λ(X)`, 6 x-values × 3 randoms | `3.5e-16` |
| `⟨Y,ΛX⟩ = ⟨ΛY,X⟩` (self-adjointness) | `1.3e-15` |
| `⟨M,Λ^c X⟩ = ⟨(Λ^c)†M, X⟩` | `1.1e-15` |
| pure-input isospectrality (spec, incl. the extra 0) | `4.4e-16` |
| **`G_def` (4-term, four eigendecompositions, isospectrality NOT used) vs `⟨ψ|W|ψ⟩`**, 48 random (ψ,σ) at 6 x-values, σ ranks 2 and 3 | `8.3e-16` |
| **same identity at mpmath dps 60**, 12 pairs at x ∈ {41/100, 43/100, 687/1600} | **`6.6e-61`** |
| `G_def(eigvec_min, σ) = λ_min(W)` and 400 random pure ψ never beat `λ_min` | `7.1e-16` |

**Scope limit I add (the standing exact-zero-mode failure mode).** `W(σ)` requires
`Λ(σ) > 0` **and** `Λ^c(σ) > 0`. For `x ∈ (0,1)` a rank-1 `σ = P_φ` makes `Λ^c(σ)` singular
(rank 3 < 4), so `W` is **undefined** there. This is not a gap: I checked directly
(`G1f`, x = 0.43) that `D(Λ^c(P_ψ)‖Λ^c(P_φ)) = +∞` for `φ ≠ ψ` (kernel mismatch) while the
B-side term is finite, so `G = +∞ ≥ 0` and **rank-1 σ can never violate P_b2**. Hence
`inf over all σ of λ_min(W(σ))` over `rank σ ≥ 2` is the complete question, and the reduction is
scope-complete for P_b2. The note does not state this explicitly; it is implicit in its support
floor. Recorded as minor **m1** (an addition, not a defect).

**Verdict on item 1: CONFIRMED at FORMULA level.** Nothing downstream inherits a defect.

---

## 2. Item 2 — the stratum value `G*(x)` and the root `x_d`

**Own derivation (symbolic route).** Take `ψ = e₁` (legitimate: `Λ_x` is `O(3)`-covariant, since
`(OXOᵀ)ᵀ = OXᵀOᵀ`), `σ = (1 − P_ψ)/2 = diag(0,½,½)`. All four outputs are diagonal:

```
Λ(P)   = diag(1−x, x/2, x/2)        Λ(σ)   = diag(x/2, (2−x)/4, (2−x)/4)
Λ^c(P) = diag(1−x, 0, x/2, x/2)     Λ^c(σ) = diag(1−x, x/2, x/4, x/4)
```

`supp Λ^c(P) ⊆ supp Λ^c(σ)`, so `D_E = 2·(x/2)ln 2 = x ln 2` and
`D_B = (1−x)ln(2(1−x)/x) + x ln(2x/(2−x))`, giving

> `G*(x) = (1−2x) ln x + x ln(2−x) − (1−x) ln(1−x) − (1−x) ln 2`.

I built the same four matrices in sympy from the **Kraus definition** (not by hand-copying) and
formed the difference: **`G*_sympy − claimed formula = 0` exactly** (`r16_item12.log`).

**c ≥ 2 gate — the ≥50-dps numeric route (definitional, NOT the formula):** mpmath dps 60,
4-term definitional `G` at the exact pair, six x-values `{0.3, 0.41, 0.4296, 0.43, 0.47, 0.499}`:
worst `|G_def − G*| = 3.1e-61`. Third gate: four **random real** ψ with `σ = (1−P_ψ)/2` at
x = 43/100 reproduce `G*` to `2.4e-17` (the O(3)-covariance the derivation used). Control: a
**complex** ψ with the same construction gives `0.0599 ≠ G*(0.43) = 0.00112` — so "ψ real" in the
note's stratum definition is load-bearing and correctly stated.

**The root, two independent routes.**

```
x_d (mpmath findroot on MY G*)          = 0.4296628745658923241200561989373791075714
x_d (findroot on the sympy-lambdified   = 0.4296628745658923241200561989373791075714
     CLAIMED form)                        difference 0.0 at 40 digits
G*'(x_d) = 3.32621288542 > 0   (simple, transversal)     687/1600 < x_d < 43/100: TRUE
```

This matches the note's 50-digit string `0.42966287456589232412005619893737910757142031486046`
on every digit I computed.

**Wording audit ("EXACT only on-stratum, CANDIDATE globally").** Accurate, and I checked the
distinction is real: at x = 0.47 and 0.499 the real ψ is **no longer** the argmin of
`W(σ_orth)` (`λ_min = 0.1045` vs `G* = 0.1237` at 0.47), while at every x ≤ 0.43 tested the real
ψ **is** the argmin to 60 dps. So `G*` equals `min_ψ G(ψ,σ_orth)` near `x_d` but not globally in
x — precisely the "on-stratum" scoping the note uses. The "5-point global-optimality check" count
is right (0.415, 0.420, 0.425 in §4.1 plus 0.4295, 0.4296 in §4.3); the §6.3 cross-reference
sends the reader to §4.3 alone, whose table has three rows. Bookkeeping only — minor **m2**.

---

## 3. Item 3 — bracket endpoints with my own optimizer, and the power audit

My instrument (`tools/whgap_r16_item3.py`): minimize `λ_min(W(σ))` over `σ = AA†/Tr`,
`A ∈ ℂ^{3×r}`, r ∈ {2,3}; L-BFGS-B, **220 restarts** per point (100 rank-2 random + 100 rank-3
random + 20 orthocomplement-stratum seeds); no support floor (rank-1 σ simply diverges).
The reduction licenses this: the anchor is solved exactly, so every null covers ALL pure anchors.

**(a) x = 687/1600 = 0.429375 — violation independently re-found.**

```
own optimizer      min λ_min(W) = -9.580821873350e-04   hit rate 66/220
definitional 4-term G at (argmin ψ, σ)  = -9.580821873356e-04
σ spectrum = [~0, 0.5, 0.5] (rank 2)    min spec Λ(σ) = 2.146875e-01
dps-60 sharpening at the SAME σ         = -0.000958082187334920740038279170897090500393782425
```

Agrees with the executor's certificate `-0.000958082187335739…` to 12 significant digits (the
residual difference is float64-input level, see m4).

**(b) x = 43/100 — null independently reproduced.** `0/350` restarts negative;
`min = −1.78e-15` at a σ that is numerically pure (`spec ≈ [0, 4e-15, 1]`), i.e. the same σ→P_ψ
corner the note documents; a dps-50 recheck at that σ returns `+8.4e-16`. **No violation found.**

**Detection-power reasoning — mine, then the audit of theirs.** I calibrated my OWN protocol on
the violating side, and the essential question is whether the basin collapses as `x ↑ x_d`:

| x | my min `λ_min(W)` | my hit rate |
|---|---|---|
| 0.42 | −3.276525805e-02 | 52/90 = 0.58 |
| 0.4285 | −3.876950922e-03 | 29/90 = 0.32 |
| 0.429375 | −9.580821873e-04 | 24/90 = 0.27 |
| 0.4296 | −2.091604277e-04 | 18–21/90 ≈ 0.20 |
| **0.42966287** (4.6e-9 below `x_d`) | **−1.518711350e-08** | **15/90 = 0.17** |
| 0.4297 / 0.4298 / 0.43 / 0.431 | +3.6e-15 / +3.6e-15 / +5.3e-15 / +1.7e-15 | **0/90** each |

The basin fraction does **not** collapse: it decays gently from 0.58 to 0.17 and is still 0.17
at 4.6 nano-units below the death point. With `p ≥ 0.167` sustained to the death point, my
`0/350` at 43/100 misses a violation of comparable basin volume with probability
`(1−0.167)^350 ≈ 1.6e-28`.

**Audit of the executor's §3.2 argument: it does NOT outrun the instrument.** Their claim (hit
rates 0.85 → 0.34 where violations exist; `N = 200`; `(1−p)^N`; `p = 0.34 ⇒ 1e-35`; `p = 0.015`
still caught 95%) is arithmetically correct — `(1−0.015)^200 = 0.049` — and, decisively, its weak
link (extrapolating `p` from points *far* below `x_d` to the endpoint) is the thing I tested
directly and independently confirmed. Both their §3.2 last sentence and their §6.2 correctly
restrict the statement to basin volume in the chart, not to non-existence. **No power over-claim.**

**Reviewer's tightened bracket (upgrade U2, §9).** My scan brackets the death point in
`[0.42966287, 0.4297]`, **width 3.7e-6** (vs the recorded `6.25e-4`), and the global minimum
equals `G*(x)` to 5 significant digits at every violating point including the one 4.6e-9 below
`x_d` (`−1.5187e-8` measured vs `G*'(x_d)·(x−x_d) = −1.5187e-8`). This is a materially stronger
global-optimality corroboration than the recorded 5 points.

---

## 4. Item 4 — certificate hygiene (5 of 7 spot-checked)

Recomputed with my own 4-term definitional route at dps 60 from the recorded `(ψ, params)`
(`r16_item45.log`):

| x | recorded G | my recomputation | diff | σ rank | min spec Λ(σ) | min spec Λ^c(σ) | ⟨ψ\|σ\|ψ⟩ |
|---|---|---|---|---|---|---|---|
| 41/100 | −0.06803397301969790… | −0.0680339730196979… | 4e-17 | 2 | 0.1615350515 | 0.0906500551 | 4.06e-3 |
| 21/50 | −0.03276525804502643… | −0.0327652580450264… | 6.2e-18 | 2 | 0.21 | 0.104999998 | 8.2e-17 |
| 17/40 | −0.01565454265639577… | −0.0156545426563958… | 6.7e-18 | 2 | 0.2125 | 0.106249999 | 1.5e-16 |
| 171/400 | −0.00722527997304624… | −0.0072252799730462… | 5.8e-18 | 2 | 0.21375 | 0.106874996 | 1.6e-15 |
| 687/1600 | −0.00095808218733574… | −0.0009580821873357… | 2.7e-18 | 2 | 0.2146875 | 0.107343747 | 2.3e-16 |

All five are **negative**, all five reproduce, and none is a support/boundary artifact: the σ's
are rank-2 (smallest eigenvalue at float64 noise, `~1e-17`), but their **outputs** are bounded
away from singular by `~1e-1` on both sides. The standing exact-zero-mode trap is therefore
screened, and screened for the right reason (it is the OUTPUT spectra that matter, not `rank σ`).

**Interior full-rank claims — verified, with a structural observation.** At 41/100 (`f`=0.03 and
0.15) and 17/40 (`f`=0.03) I reproduce the recorded floored minima to all printed digits
(`−6.3102503072e-02`, `−4.5110645498e-02`, `−1.2118199551e-02`; min spec σ = 0.010, 0.050, 0.010;
rank 3). **New observation:** every one of these values equals, to all printed digits, my direct
evaluation of `λ_min(W)` at the **f-smoothed orthocomplement state** `(1−f)(1−P_ψ)/2 + f·1/3`
(`r16_item2b.log`). So the "interior full-rank violator" is not an independent structure — it is
the stratum state pushed inside. That strengthens rather than weakens the note's picture.

**minor m3 (mechanism mislabel, conclusion unaffected).** §3.5 reading 3 says the null rows of
that table are "genuine **interior** minima (no corner stall, fidelity < 1)". They are not
corner-free: at 687/1600, 43/100 and 9/20 the reported `min spec Λ(σ) = 1.00e-02 = f/3` and
`min spec Λ^c(σ) = 4.29e-03 ≈ f·x/3` are exactly the signature of the **σ → pure, τ = 0 corner
regularized by the floor** — the same corner as §3.3, not a new interior structure. The
CONCLUSION drawn from those rows ("no interior full-rank violator near `x_d`") is nonetheless
sound and I confirm it independently: the floored stratum state itself gives
`+2.20e-3` at 687/1600 and `+4.23e-3` at 43/100 (`r16_item2b.log`), positive as claimed.

**minor m4 (digit hygiene).** The 46-digit certificate strings are exact evaluations at a float64
pair whose recorded `ψ` has `‖ψ‖ = 1 + O(1e-16)`. Since `G` is a quadratic form in `ψ`, the
printed digits beyond ~15 are convention-dependent at the `1e-16` relative level (my
recomputations differ from the recorded strings at exactly that size). The **sign** — the entire
content of a violation certificate — is untouched, and the note's own §3.4 caveat already says
only ~8 digits are properties of the minimiser. Worth one clause: "…at the recorded pair, under
unit normalization of ψ".

---

## 5. Item 5 — tensorization structure and the 41/100 calibration

**My own proof of the structural fact.** `Λ_2 = Λ⊗Λ` has Kraus set `{K_a⊗K_b}`, so
`Λ_2^c = Λ^c⊗Λ^c` (up to the isometric freedom in E, under which relative entropies are
invariant). For a product `σ₁⊗σ₂`, `log(A⊗B) = log A⊗1 + 1⊗log B`, and **both** adjoints are
unital (`Λ(1)=1`; `Σ_j K_j†K_j = 1`), so every cross term collapses to an identity:

> `W₂(σ₁⊗σ₂) = W(σ₁)⊗1 + 1⊗W(σ₂)`, hence
> `λ_min(W₂(σ₁⊗σ₂)) = λ_min(W(σ₁)) + λ_min(W(σ₂))`, attained at a **product** anchor.

Unitality is the load-bearing hypothesis and the note names it correctly. Gates with my own
independent 2-copy code (16 Kraus operators, 9×9/16×16): `Λ_2 = Λ⊗Λ` and the 2-copy adjoint
identity to `4.4e-15`; the additivity identity itself to **`6.2e-15`** over 3 x-values × 12
product states of mixed ranks (2⊗3, 3⊗3, 3⊗2).

**Consequence, audited:** "2-copy P_b2 restricted to product σ ⟺ 1-copy P_b2" is correct, and
the stronger reading the note draws — *any* 2-copy violation requires a **correlated** σ, and
entangling the anchor alone can never help — follows because the anchor minimisation is exact.
This is the sharpest structural statement in the package and it is right.

**2-copy calibration and superadditivity at x = 41/100 (my own code):**

```
recorded  min G₂                       = -0.13639057367592
R16 λ_min(W₂) at the SAME σ            = -0.13639057367591   (diff 5.2e-15)
R16 own 1-copy min G₁                  = -0.06803397301044  ->  2·min G₁ = -0.13606794602088
R16 cross-check λ_min(W₂(σ*⊗σ*))       = -0.13606794602089   (T1 identity, 1e-14)
R16 OWN 2-copy descent (6 starts)      = -0.136390603102
superadditive gap  min G₂ − 2 min G₁   = -3.23e-04           (strictly negative)
```

**Superadditivity CONFIRMED independently.** My own descent, seeded at the product optimum and
run with my own code, reaches `−0.136390603`, i.e. `2.9e-8` **deeper** than the recorded
`−0.136390574` — so the recorded minimum is very slightly under-converged, which makes the
recorded gap conservative rather than optimistic. The recorded σ has rank 5 on the 9×9 side, with
`‖σ − marg⊗marg‖ = 0.041`: genuinely correlated. The note's framing — a statement about the
DEPTH of an already-existing violation, **not** a non-tensorization of the property — is exactly
right. minor **m5**: report the recorded 2-copy minimum as `≤ −0.1363905737` (a bound), not an
equality, given the 24-restart budget the note itself flags.

---

## 6. Item 6 — null-scope honesty audit

**CLEAN, in both directions (no over-claim, no under-claim).**

- The 2-copy null is presented as exactly what it is: §5.4 states the budget (80 restarts at 0.46
  and 0.48, **32** at 0.43, split across three start families; 162 real parameters; chart;
  support floor), and §6.5 says in terms that "80 (resp. 32) restarts in 162 real dimensions
  cannot exclude a violation on a small or lower-dimensional stratum".
- The un-run **F2** boundary-restricted 2-copy search is flagged in the note (§6.5, §8), survives
  into the node's Work record ("…was NOT run (batch 1 of ≤ 2)"), and is carried as the
  highest-value follow-up in the node's Open obligations. It survives into every summary sentence
  I could find. The DAG header calls the result a "bounded null", not a tensorization result.
- The 1-copy `+1e-11` rows are labelled corner stalls rather than minima (the R8-m1/R9 lesson
  correctly internalized); the 2-copy `+9.5e-10 / +4.6e-10 / +2.9e-9` rows likewise, with the
  interior runs supplied as the substantive content.
- **Under-claim check:** §7's "`P_b2` … holds (bounded null) from 0.43 upward" compresses
  "no violation found in a bounded search" into "holds"; the parenthetical repairs it in the same
  breath and the node repeats the qualified form. Not a finding, but the node wording the decision
  layer adopts should keep the qualifier attached.

## 7. Item 7 — no-Q-consequence audit (R8 MAJOR-3)

**CLEAN.** I grepped the note and every log for `Q(`, `Q = 0`, `Q^(1)`, `onset`, `qpositive`.
Findings: one line (§6.6) *disclaiming* a Q-consequence in exactly R8's adopted wording
(`P_b2 ⟹ Q^(1) = 0`, never the converse, so the violations "say nothing about `Q(Λ_x)` on
`[2/5, x_d)`"); one line (§7) confirming nothing bears on `WHGAP.onset-two-fifths` or
`WHGAP.qpositive-onset`; and two lines describing "the P15 **route** to `Q = 0` … survives",
which is a statement about the viability of a route (P_b2 + tensorization ⟹ Q = 0), not a
derivation of a Q-statement from P_b2 data. **No log contains any Q-statement at all.**

One quantifier nit, minor **m6b** folded into m6: §2.3's negative control says "x = 1/5
(Q > 0 PROVED, so P_b2 must fail)". Strictly, `Q > 0` alone does not force `Q^(1) > 0` and hence
does not force `¬P_b2`; what does is that the R5d witness on `(0,2/5)` is **single-letter**
(`I_c > 0` at n = 1). The control is valid; the one-line justification is a step short.

## 8. Item 8 — value-vs-formula statements (7f)

| headline number | VALUE or FORMULA | reviewer status |
|---|---|---|
| `G*(x)` closed form | **FORMULA** | **Re-derived independently by me** (sympy, residual exactly 0) — this is a formula-level verification, not a re-run of the executor's check. Corroborated by an independent 60-dps *definitional* construction (`3.1e-61`). Both exist and agree. |
| `x_d = 0.42966287456589232412…` | **FORMULA-evaluated** (root of `G*`) | Reproduced to 40 digits by two independent root-finders on two independently produced expressions; transversal (`G*' = 3.326`). Agrees digit-for-digit with the recorded 50-digit string. |
| bracket endpoint `687/1600` violation | **VALUE** | Reproduced by my own optimizer and by an exact-rational evaluation; both routes exist and agree to 12 digits. |
| bracket endpoint `43/100` null | **VALUE** (a search outcome) | Reproduced (0/350). Not a formula and must never be read as one. |
| the 7 certificate `G` values | **VALUES** from an independent construction | 5 of 7 recomputed with my 4-term route; agreement to float64-input precision (m4). Independent-construction agreement corroborates the numbers; it does not verify any printed derivation, because there is none to verify here. |
| `W₂` additivity | **FORMULA** | Proved by my own route AND gate-checked as a matrix identity (`6.2e-15`). Both. |
| superadditive gap `−3.2e-4` | **VALUE** | Reproduced at the recorded σ and by my own independent descent. |

**Standing failure-mode list (7e), all screened:** *double-precision locators vs mpmath
certificates* — correct discipline (float64 locates, 60 dps certifies at the located pair), with
m4 as the only residue; *exact-zero-mode / support degeneracy near boundaries* — screened at every
certificate (output spectra `~1e-1`), plus my rank-1 analysis in §1; *optimizer stalls read as
minima* — the note labels them, with the m3 exception; *power claims outrunning the instrument* —
tested head-on in §3 and independently confirmed. Frozen-input scopes (7d): I leaned only on the
node's frozen definitions of `G`/`P_b2` and on P2/P4/R5b for the `x ≥ 1/2` control (PROVED tier,
in scope); the new load-bearing input — the reduction — I did not import at all, I derived it.
Quantifier hygiene (7g): "P_b2", "stratum", "corner stall", "bounded null", "interior" (= min
spec σ ≥ f/3) and "death point" all resolve in the note or on the node.

---

## 9. Reviewer upgrades (offered under licensing menu A)

- **U1 — the stratum identity is reviewer-verified at FORMULA level.** `G*(x) = (1−2x)ln x +
  x ln(2−x) − (1−x)ln(1−x) − (1−x)ln 2` is exact for the pair (ψ real, σ = (1−P_ψ)/2) at every
  x ∈ (0,1). I re-derived it symbolically by my own route; sympy residual is exactly `0`. Under
  rule 6 this is licensable above NUMERICAL by the decision layer as a **reviewer-verified
  identity** (with the O(3)-covariance step, which I also checked, as its only ingredient).
- **U2 — the violation side of the bracket is ANALYTIC, not a 7-point sample.** Because the
  exhibited pair is a legitimate P_b2 pair with an exactly known value, `G*(x) < 0` **is** a
  violation. On a 50-dps grid `x = k/4000, k = 1…1999`, `G*` is negative at all 1718 points below
  `x_d` (max `−5.4e-4`) and positive at all 281 above, with `G*' > 0` throughout the strip
  (`3.735` at 2/5, `3.326` at `x_d`, `2.470` at 0.499); `G* → −∞` as `x → 0⁺` and
  `G*(1/2) = +0.2027` (`r16_item2b.log`). So **P_b2 fails at EVERY x < x_d**, not merely at the
  seven certified points — a statement needing only an elementary monotonicity lemma for `G*` to
  be a theorem. The note under-claims here. Recommended node wording: *"P_b2 is violated at every
  x < x_d by the exhibited orthocomplement pair (exact closed-form value); the death point
  itself is a candidate pending stratum-minimality (F1)."*
- **U3 — a strictly better certificate at the bracket endpoint.** At the exact rational inputs
  `ψ = e₁`, `σ = diag(0,½,½)`, `x = 687/1600`:
  `G = −0.000958082187335938228207335155849733193025442636` (dps 60), and the same value is
  `λ_min(W(σ))`. Every printed digit here is a property of an **exactly specified** pair, which
  the float64-located certificates cannot claim (m4). The decision layer may prefer this as the
  citable endpoint certificate.
- **U4 — the tightened bracket** `[0.42966287, 0.4297]` (width `3.7e-6`) with the global minimum
  tracking `G*` to 5 digits at 4.6e-9 below `x_d` (§3). This makes "the stratum is globally
  optimal in a neighbourhood of `x_d`" a much better supported NUMERICAL statement, and it is
  still NUMERICAL: F1 remains the proof obligation.

## 10. Minors (itemized)

- **m1.** State the domain of `W` explicitly (`rank σ ≥ 2`; rank-1 σ gives `G = +∞`, so the
  reduction is scope-complete for P_b2). One sentence; currently only implicit in the support floor.
- **m2.** §6.3's "five points (§4.3)" points at a three-row table; the five points are 0.415,
  0.420, 0.425 (§4.1) + 0.4295, 0.4296 (§4.3). Cross-reference only.
- **m3.** §3.5 reading 3 calls the floored null rows "genuine interior minima (no corner stall)";
  their printed `min spec Λ(σ) = f/3` shows they ARE the σ→pure τ = 0 corner, regularized by the
  floor. The conclusion drawn from them survives (I verified the floored stratum state is positive
  at 687/1600 and 43/100); only the mechanism sentence needs correcting.
- **m4.** The 46-digit certificate strings depend on the unit-normalization convention for the
  recorded `ψ` beyond ~15 digits; add that clause. The sign is unaffected.
- **m5.** Report the 41/100 2-copy minimum as a bound `≤ −0.1363905737`: my own descent reaches
  `−0.1363906031`, so the 24-restart value is slightly under-converged (conservative direction).
- **m6.** Disk-view drift for the decision layer (not the executor's doing): the DAG nested
  outline (`notes/WERNER-HOLEVO-GAP_PROOF_DAG.md` lines 345–347) still describes P15 as
  "P15-A commission on disk, not executed", contradicting the same file's header. Also folded in:
  §2.3's "Q > 0 PROVED, so P_b2 must fail" needs the word *single-letter* to be a valid inference.

## 11. Provenance

Reviewer scripts: `tools/whgap_r16_core.py`, `whgap_r16_item12.py`, `whgap_r16_item3.py`,
`whgap_r16_item45.py`, `whgap_r16_item2b.py`. Reviewer logs (additive; no executor artifact was
modified or overwritten): `artifacts/logs_whgap_p15b_20260801/r16_item12.{log,json}`,
`r16_item3.{log,json}`, `r16_item45.{log,json}`, `r16_item2b.{log,json}`, hashed in
`artifacts/logs_whgap_p15b_20260801/SHA256SUMS_r16.txt` (LF, separate from the executor ledger).
Interpreter: CPython 3.11.9, numpy 1.26.4, scipy 1.14.1, mpmath 1.3.0, sympy 1.13.1; local
compute only; no credentials in any artifact. I also verified the executor's own ledger:
`sha256sum -c SHA256SUMS.txt` from the log directory returns **19/19 OK**, matching the node's
claim (the node's "LF manifest, 19/19 verified" is accurate — cf. R9 m4, where a manifest claim
was struck for never having happened; this one did happen and I re-ran it).

**Final line.** Verdict **(A) licensed as recorded**, 0 MAJOR, 6 minors, with upgrades U1–U4
offered. I wrote no node, index or DAG file, and made no commit.

