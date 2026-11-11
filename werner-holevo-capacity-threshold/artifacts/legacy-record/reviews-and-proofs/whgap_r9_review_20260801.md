# WHGAP R9 — independent rule-7 review of the P15-A package

Reviewer: fresh Opus 5 instance, 2026-08-01. Commission: Track R9 of
`channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_LEAN4_R9_M6_20260801.md`,
executing the R9 section of
`channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_P15A_P16A_20260730.md`.
Node: `WHGAP.pure-anchor-order` (P15). Rule-7 embeds: §1–§3 of
`channel-capacity/werner-holevo-gap/notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md`.

**VERDICT: FINDINGS (menu option B).** Two MAJOR, five minor. The A1 identity and the
G-A0 / G-A+ verdicts at x = 2/5 are independently confirmed and are licensable at the
scope the note itself states; §A3.3 states a false "proved" criterion; §A4.3 and §5
report a strip null that the note's own A4 data contradicts.

---

## PRE-ACTION REPORT

- **Target node:** `WHGAP.pure-anchor-order`, status **OPEN**, `disposition: null`
  (front matter of `channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.pure-anchor-order.md`).
- **Role:** REVIEWER. **Independence statement:** I did not author P15-A, any P15/P12/R8
  material, or any tool under `tools/whgap_p15a_*.py`; I was given no desired outcome, and
  the commission presents its licensing menu as alternatives.
- **Highest status my evidence could license (§2 ladder):** my own runs are NUMERICAL
  (proposer tier). As an independent reviewer completing an archived review I may open the
  completion tier for the reviewed work; the *writer* of any node status is the decision
  layer (single-writer deviation binding on me — I edit no node, no NODE_INDEX, no DAG).
- **Gates/deliverables of my commission (one line each):** re-derive the decomposition
  identity by my own route; re-find/re-verify the x = 2/5 violating pair with my own
  optimizer and my own I_c code at ≥ 40 digits; audit the G-A0 verdict and the G-A+
  non-trigger; audit A3 for the over-claim R8 MAJOR-3 flagged; audit A4's strip statements
  and the G-Acal calibration gate; report
  `{verdict, summary, majors, minors, report_path}`; budget ≤ 90 min.
- **Conflicts between commission text and disk protocols:** one, non-mathematical. The
  P15-A/P16-A commission names the R9 report `artifacts/whgap_r9_review_20260730.md`; the
  2026-08-01 commission that dispatched me names `artifacts/whgap_r9_review_20260801.md`.
  I follow the later (dispatching) commission and record the discrepancy here rather than
  resolving it silently. No protocol conflict otherwise.
- **Anchoring-ban compliance (7c), with a disclosed exposure.** I derived Proposition A1
  from scratch and ran my own 200-restart optimizer at x = 2/5 to completion **before**
  opening `notes/WHGAP_P15A_STRICTNESS_20260730.md` or any `tools/whgap_p15a_*.py`.
  **Disclosed exposure:** the mandatory pre-task reload requires reading the node file,
  which already displays `G = -0.1224208841` and `min spec Λ(σ*) = 2.95e-2` from R8. I
  could not avoid that and did not use it: my optimizer was seeded only from
  `numpy.random.default_rng(2500)` and the value was reproduced from 200 independent
  random starts, 191 of which returned a negative value.

---

## 0. Package integrity

`sha256sum -c artifacts/logs_whgap_p15a_20260730/SHA256SUMS_posthoc_decision_layer.txt`
→ **24/24 OK** (14 logs/JSON + the note + 9 scripts). The reviewed package is byte-identical
to what the decision layer hashed post-hoc. Per my commission I treat the missing
run-time manifest as a recorded closeout defect, not as fresh suspicion — but see minor m4:
the note *asserts* a manifest that does not exist.

---

## 1. A1 — the decomposition identity. **CONFIRMED (own derivation + own numerics).**

### 1.1 My own derivation (written before reading §A1)

For any channel Λ with complement Λ^c and any pure decomposition σ = Σ_u p_u P_{ψ_u},

    Σ_u p_u D(Λ(P_u) ‖ Λ(σ)) = −Σ_u p_u S(Λ(P_u)) − Tr[(Σ_u p_u Λ(P_u)) log Λ(σ)]
                              = −Σ_u p_u S(Λ(P_u)) + S(Λ(σ))  =  χ_B ,

and identically χ_E on the E side, so Σ_u p_u G(ψ_u, σ) = χ_E − χ_B. For a *pure* input,
Λ(P_ψ) and Λ^c(P_ψ) are the two marginals of the pure vector V|ψ⟩, hence isospectral, so
S(Λ(P_u)) = S(Λ^c(P_u)) and the ensemble-entropy terms cancel:

    Σ_u p_u G(ψ_u, σ) = S(Λ^c(σ)) − S(Λ(σ)) = − I_c(σ).

Finiteness: p_u Λ(P_u) ≤ Λ(σ) gives supp Λ(P_u) ⊆ supp Λ(σ) automatically on both sides,
so no faithfulness hypothesis is needed. **This is the same statement, the same support
analysis, and structurally the same two-step route as §A1.2.** Per 7c I flag the
coincidence explicitly: the route is essentially forced (isospectrality is the only place
the purity of the ψ_u can enter), so notational agreement here is not evidence of
independence beyond the fact that I wrote it first.

### 1.2 My own verification

- `tools/whgap_r9_a1.py` (log `artifacts/logs_whgap_p15a_20260730/r9_a1.log`,
  `r9_a1.json`): float layer, x ∈ {1/4, 2/5, 9/20, 11/20, 4/5}, 3 random σ each, **four
  different decompositions per σ** (eigen-ensemble + 4-, 5-, 7-element isometry ensembles),
  plus two rank-2 σ. Worst residual |Σ p_u G + I_c| = **1.83e-15**. Independent sanity
  legs all PASS: Kraus sum = closed form (1.1e-16), trace preservation, pure-input
  isospectrality (4.2e-16), I_c(P_ψ) = 0 (4.4e-16).
- `tools/whgap_r9_a1mp.py` (log `r9_a1mp.log`, `r9_a1mp.json`): **60 dps**, σ built *from*
  an exact-to-working-precision 3-term pure ensemble at x ∈ {1/4, 2/5, 11/20}, then
  re-decomposed into 4-, 5- and 8-term ensembles by an mp isometry. All four ensembles
  give **the same** Σ p_u G to 30 printed digits, matching −I_c; worst residual **6.6e-61**.

**Value-vs-formula (7f).** My numerics verify VALUES; the general claim is carried by the
derivation in §1.1, which I performed myself. My code computes G and I_c from their
definitions and never from the identity, so the agreement is an independent-construction
check, not a self-consistency check.

**Audit of the note's own verification legs.** §A1.4's symbolic leg (L1) is sound: I read
`tools/whgap_p15a_a1.py` and confirm ψ is a *fully generic* unnormalised complex vector
`a_i + i b_i` (not a special state), the chart is genuinely radical-free
(`Tr[(Λ^c(P))^k] = Tr[(N D²)^k]` with `D² = diag(u,v,v,v)`), and the Newton argument is
valid: power sums k = 1,2,3 plus `det Λ^c(P) = 0` pin the 4×4 spectrum to the 3×3 spectrum
padded by a zero (k = 4 is redundant but harmless). Homogeneity makes the unnormalised
check equivalent to the normalised one. The recorded negative control (the sub-normalised
ensemble that passes at x = 2/5 and fails at 11/20) is a genuinely useful catch and the
note is right to keep it.

**Type audit (7a).** P: 3×3 Hermitian rank-1; Λ(P): 3×3; Λ^c(P): 4×4 padded with
Λ^c(Y)_{ab} = Tr(K_a Y K_b^†); Kraus real so K^† = K^T (I used `.conj().T` throughout and
never relied on realness); D(·‖·) between a 3×3 pair and a 4×4 pair respectively — the two
terms of G live in *different* dimensions, which is exactly why the isospectrality step,
not a dimension-matching step, is what makes the cancellation work. I re-derived
Λ^c from the Kraus list myself; the padded-4-dim convention and the (1−x), x/2 weights
agree with R5 §1.

**Licensing opinion (A1):** the Proposition is correct as stated, including the
"no faithfulness needed" clause and the decomposition-independence. It is a genuine proof,
independently re-derived and independently corroborated symbolically and at 60 dps.

---

## 2. A2 / G-Acal / G-A0 / G-A+ — **CONFIRMED at the note's stated scope.**

### 2.1 G-Acal (hard calibration, x = 11/20) — **PASS, independently.**

`tools/whgap_r9_search.py gacal` (log `r9_gacal.log`, `r9_gacal.json`):
**400** random (ψ,σ) samples give `min G = +7.303e-2` and `max I_c = −3.980e-2`; **60**
Nelder-Mead restarts over the joint 15-real-parameter chart give `min G = −3.60e-14` at
`⟨ψ|σ|ψ⟩ = 1.000000` — i.e. the only "negative" is the known stall into the corner
σ → P_ψ where G → 0⁺. No violation; I_c ≤ 0 everywhere. Gate verdict **PASS**, matching
the note. (This calibration is stronger than it looks: 11/20 < 4/7, so Λ_{11/20} is *not*
antidegradable and P_b2 there rests on the PROVED cRE domination, not on DPI.)

### 2.2 The x = 2/5 violating pair — **found independently, values agree to 7–12 digits.**

`tools/whgap_r9_search.py x25` (log `r9_x25.log`, `r9_x25.json`): 200 random restarts, my
own G/I_c implementation, my own parametrisation, seeded only by RNG. Result:
**191 of 200 restarts returned G < −1e-7**; best `G = −0.122420884165` (float64).
Refinement at 60 dps (`tools/whgap_r9_refine.py`, log `r9_refine.log`):

| quantity | R9 (this review) | P15-A note §A2.1/§A2.3 |
|---|---|---|
| `G(ψ*,σ*)` @60 dps | `−0.12242088416530087145567930160` | `−0.12242088416530682817159722598` |
| `min spec Λ(σ*)` | `0.0295155952801729200` | `0.0295156122465005253` |
| `min spec Λ^c(σ*)` | `0.0215076905121455979` | `0.0215077025834745161` |
| `spec σ*` | `[0.87374440, 0.12625560, 6.5e-17]` | `[0.87374434, 0.12625567, 4.6e-18]` |
| `⟨ψ*|Π_ker|ψ*⟩` | `0.99621` | `0.99612` |
| `I_c(σ*)` (nats) | `−0.023524164056474115045` | `−0.023524168363883401132` |

Agreement to 7–8 significant digits on every quantity (12 on G), exactly as expected for
two float64 minimisers of the same function. **The datum is real, reproducible from
scratch, and is not a support artifact** (both output spectra bounded away from 0 by
~2e-2). The decomposition D_E = 2.3558499227, D_B = 2.4782708069 shows the violation is a
genuine competition between two large finite relative entropies, not a near-singular
blow-up.

### 2.3 ψ* ∉ range(σ*) and the full-rank refinement (§A2.2 / §A2.2b) — **CONFIRMED, and
I close a gap in the note's argument.**

I independently reproduce that the global minimiser is degenerate: σ* is rank 2
(third eigenvalue 6.5e-17) with ψ* 99.6% in ker σ*, so (ψ*,σ*) cannot occur in any pure
decomposition of σ* and Proposition A1 does not constrain it. §A2.2 is correct.

§A2.2b's sharper claim — that the violation survives with σ full rank, where A1 *does*
bind — is also correct, but **the note never evaluates I_c at those full-rank σ**; it
infers −I_c(σ) > 0 from the global numerical claim "max I_c = 0 at x = 2/5, attained only
at pure states". That is a bounded search doing load-bearing work where a one-line direct
computation suffices. I did the direct computation
(`tools/whgap_r9_fullrank.py`, log `r9_fullrank.log`, `r9_fullrank.json`), with my own
optimizer and a hard floor on min spec σ:

| x | floor | my `min G` | note's `min G` | my `I_c(σ)` @50 dps | `−I_c(σ)` |
|---|---|---|---|---|---|
| 2/5 | 0.01 | `−0.1034053611` | `−0.1034396332` | `−0.02882988528` | `+0.0288` |
| 2/5 | 0.05 | `−0.0770663819` | `−0.0770709944` | `−0.02773646239` | `+0.0277` |

So at x = 2/5 there is an explicit **full-rank** σ (spec `[0.050, 0.474, 0.476]`) with
`G(ψ,σ) = −7.7e-2 < 0` while `Σ_u p_u G(ψ_u,σ) = −I_c(σ) = +2.77e-2 > 0`. The average is
positive and one term is negative, verified *at that σ* rather than inferred. **§A2.2b's
conclusion stands and is now value-verified; the restricted order `P_b2^rng` is indeed
dead at x = 2/5.**

### 2.4 G-A+ non-trigger — **CONFIRMED.**

My own I_c maximisation at x = 2/5 (`r9_refine.log`): 150 restarts seeded near σ* give
`max I_c = 1.58e-12`, 150 unconstrained restarts give `max I_c = 1.67e-12`; in both cases
the argmax collapses to a pure state (spec `[≈1, 5e-13, 1e-15]`) where I_c ≡ 0 identically,
and the 60-dps re-evaluation at those argmaxima returns `−1.42e-12` and `−1.33e-12`, i.e.
numerical zero from below. No rank-unambiguous state with I_c > 1e-8 was found.
**G-A+ NOT triggered; G-A0 holds.** The note's §A2.4 table (max 7.77e-16 over
x ∈ {2/5 … 0.55}) is consistent with mine.

### 2.5 Audit of §A2.5's licensing statement — **accurate, and I endorse its non-claims.**

I independently reached the same conclusion the note reaches before reading it: a single
pair with G < 0 and I_c(σ*) < 0 does **not** establish "P_b2 ⊋ {Q^{(1)}=0} as classes of
channels at x = 2/5", because that needs `Q^{(1)}(Λ_{2/5}) = 0`, which is precisely the
OPEN onset question (the PROVED Q > 0 covers only the *open* interval (0,2/5), and the
ε log ε mechanism has d₁ = (1−x)(2−5x)/(2−x) = 0 exactly at x = 2/5, so it says nothing
there). §A2.5 non-claim 1 states this explicitly and correctly; non-claim 2 preserves R8
MAJOR 3 intact; non-claim 4 correctly warns that the 60-dps strings are exact evaluations
of a float64 state, so only ~8 leading digits are properties of the minimiser.
**A3's/A2.5's strictness claim does not repeat the R8 MAJOR-3 over-claim.** This is the
strongest part of the note.

**Quantifier hygiene (7g).** "Strictness", "pointwise", "range-restricted", "support
artifact", "rank-unambiguous" all resolve to definitions in the note or the commission.
One term does not: §A3.3's "spread" (see MAJOR 1).

---

## 3. MAJOR findings

### MAJOR 1 — §A3.3's "strictness CRITERION (proved)" is **false as stated**, and the note's own §A3.4 data is a counterexample to it.

§A3.3 asserts: with δ = −I_c(σ₀) ≥ 0 and Σ_u p_u G(ψ_u,σ₀) = δ,

> "Hence min_u G(ψ_u,σ₀) ≤ δ. **In particular, if δ is smaller than the spread of the
> values {G(ψ_u,σ₀)}, then some G(ψ_u,σ₀) < 0 and P_b2 FAILS while Q^{(1)} = 0 holds**".

`min ≤ average` is correct. The "in particular" is a non-sequitur. Counterexample:
two terms, p = (1/2,1/2), G = (0, 2δ) with δ > 0. Average = δ; spread = 2δ > δ; yet
min G = 0, not negative. (Under the alternative reading spread = max − average, take three
equal-weight terms G = (0,0,3δ): max − average = 2δ > δ, min = 0.) The failure is
structural: a lower bound on the *average* plus a bound on the *range* never forces a
negative element.

The note's **own** probe falsifies it and does not retract it. `p15a_a3.log` records
p = (0.08167, 0.91833), G = (0.8352991, 0.01256111), δ = 7.975e-2: spread = 0.823 ≫ δ,
yet min G = +0.0126 > 0. §A3.4 observes exactly this and explains it away —
"the criterion gives only min_u G ≤ δ" — without withdrawing the sufficient condition
stated two paragraphs earlier as **proved**. A reader of §A3.3 in isolation (and the note
recommends registering "the A3.3 strictness criterion" as a node-worthy general statement,
§5) takes away a false proposition.

**Correct replacement, which is what the identity actually gives:** if all G_u ≥ 0 then
p_v G_v ≤ Σ_u p_u G_u = δ for every v; contrapositively, **if p_v G(ψ_v,σ₀) > δ for some v,
then some term is negative.** (On the note's own data p₀G₀ = 0.0682 < δ = 0.0798, so the
correct criterion also does not fire — consistent with the observed null.) The label
"(proved)" must be removed from §A3.3 as written, and the criterion must not be registered
as a node in its current form.

Scope: this does **not** touch A1, A2, G-Acal, G-A0 or G-A+. It is contained in §A3.3/§A3.4
and in the §5 recommendation list.

### MAJOR 2 — §A4.3 and §5 report a strip bounded null that the note's **own A4 data contradicts**: P_b2 is violated at x = 41/100, inside the strip.

§A4.2 fixes the tested points as x ∈ {2/5, 41/100, 9/20, 49/100}. §A4.3 then states:

> "**`inf G = 0` on the strip points tested, approached degenerately; no negative value
> found.**"

and §5 obligation 2 repeats "the bounded null stands". `artifacts/logs_whgap_p15a_20260730/p15a_a4.log`
and `p15a_a4.json` — the note's own archived outputs — say otherwise:

| x | note's own `inf G` (210 restarts) | frac. of restarts < −1e-9 |
|---|---|---|
| 2/5 | **−1.224209e-01** | 0.995 |
| **41/100** | **−6.803397e-02** | **0.971** |
| 9/20 | +5.84e-09 (purity 1.000, stall) | 0.000 |
| 49/100 | +6.07e-09 (purity 1.000, stall) | 0.000 |

Two of the four tested points return large negative minima in 97–99.5% of restarts. The
sentence is false for both, and the omission is not cosmetic: **x = 41/100 = 0.41 lies
strictly inside the open strip [2/5, 1/2)**, so this is a violation of P_b2 at a strip
point — the single most consequential datum A4 produced, and it appears nowhere in the
note's prose, summary table, or §5 obligation mapping.

I confirm it independently. `tools/whgap_r9_fullrank.py` (log `r9_fullrank.log`), my own
optimizer and my own G/I_c, at **x = 41/100 with σ constrained FULL RANK**:

| floor on min spec σ | `min G` (mine) | `I_c(σ)` @50 dps (mine) | spec σ |
|---|---|---|---|
| 0.01 | `−0.06309995098` | `−0.04372853400` | `[0.010, 0.494, 0.496]` |
| 0.05 | `−0.04496932855` | `−0.03975653569` | `[0.050, 0.470, 0.480]` |

So at x = 0.41 there is an explicit interior, full-rank σ (smallest eigenvalue 0.05, both
output states manifestly non-singular) and a pure ψ ∈ range(σ) with G = −4.50e-2 < 0 while
−I_c(σ) = +3.98e-2 > 0. This is the same decomposition-visible mechanism as at 2/5 and it
is **not** a support artifact, **not** a corner stall, and **not** measure-zero: it is found
from generic random restarts.

**Consequences the note should have drawn (and the node record needs):**
1. **P_b2 is numerically DEAD at x = 41/100**, i.e. on part of the strip. Obligation 2 of
   `WHGAP.pure-anchor-order` is therefore not "weakened, not advanced" — it is partly
   answered in the negative.
2. The interesting quantity is no longer "does P_b2 hold on the strip" but **where in
   (0.41, 0.45) P_b2 dies** — a new, sharp, cheap question the note's own data poses and
   does not state.
3. §A4.3's methodological correction ("the violation lives on a measure-zero stratum that
   generic restarts do not sample, so the null is weak evidence") is **wrong on its own
   premise** at 2/5 and 41/100 — generic restarts sample it 97–99.5% of the time — while
   remaining a reasonable caution for 9/20 and 49/100, where the nulls are real
   (I have not yet completed my own unconstrained re-scan at those two points; see
   "Residual" below).

I read this as a reporting/derivation defect, not data fabrication: the runs are honest and
archived, the prose summarising them is not. But under rule 1 the prose is what a node
would cite, and it would have propagated a false null.

---

## 4. minor findings

- **m1 — §A2.2b's "−I_c(σ) > 0" is inferred, not computed.** The full-rank argument leans
  on the global bounded-search claim "max I_c = 0 at x = 2/5, attained only at pure states"
  where a direct evaluation of I_c at the exhibited σ costs one line. I supplied it (§2.3
  above): the conclusion survives, but as written the note routes a value-level claim
  through a search-level claim unnecessarily.
- **m2 — §A4.1 rhetorical overstatement.** "the violating σ has spectrum [0.478, 0.473,
  0.05] — as far from a pure state as a qutrit state gets" is not right (that would be
  [1/3,1/3,1/3]); and the spectrum quoted is the σ produced under an *imposed* floor of
  0.05, not a free minimiser. Harmless to the argument, but it is the kind of framing that
  later gets quoted as a fact.
- **m3 — §A2.4's negative maxima are printed as if meaningful.** Entries like
  `max I_c = −1.161293e-13` are numerical zeros of a maximisation whose true value is 0
  (attained at pure states); presenting a *negative* maximum without saying that the
  optimizer simply failed to reach the exact-zero pure stratum invites misreading. The note
  does say this in the following paragraph; the table should carry it.
- **m4 — the Reproduction section cites a manifest that does not exist.** "Script and log
  SHA-256 in `artifacts/logs_whgap_p15a_20260730/SHA256SUMS_E-P15A.txt` (LF), **verified
  with `sha256sum -c`**" — that file is not on disk; only the decision layer's post-hoc
  `SHA256SUMS_posthoc_decision_layer.txt` exists. The node already records the closeout
  defect, so the *gap* is known; what is not recorded is that the note affirmatively claims
  a verification that never happened. The claim should be struck or corrected in the record
  rather than left standing (rule 1). Integrity itself is fine: I verified all 24 post-hoc
  hashes OK.
- **m5 — orphaned reproduction commands.** `p15a_a2.json` and `p15a_a3.json` do not exist
  (both runs were terminated early, as the note discloses for a2 and a3). The Reproduction
  block lists the commands without noting that two of them do not run to completion as
  archived; a reproducer following it will not obtain the a2/a3 JSON.

---

## 5. Rule-7 checklist (how this review discharged it)

- **7a type audit** — done, §1.2: dimensions of P, Λ(P), Λ^c(P), the padded 4×4 convention,
  the K^† = K^T question, and the *different-dimension* structure of G's two terms.
- **7b c ≥ 2 identity gates** — A1 checked at five distinct rational x in float and three at
  60 dps, with 3-, 4-, 5-, 7- and 8-element decompositions of the *same* σ, plus rank-2 σ;
  the note's own symbolic leg re-read and its Newton step re-derived.
- **7c anchoring ban** — own derivation and own 200-restart optimizer completed before
  opening the note or any P15-A script; notational coincidence with §A1.2 flagged in §1.1;
  unavoidable node-file exposure disclosed in the PRE-ACTION REPORT.
- **7d frozen-input scope** — I relied only on P2/P4 (Q = P = 0 on [1/2,1]), P3+R5d
  (Q > 0 PROVED on the *open* (0,2/5)), R5c/R6 (weight operator d₁), and R5 §1 conventions.
  I did **not** treat R8's numbers, the onset conjecture, or any pending-review claim as
  established — in particular MAJOR 2's consequence rests on my own runs, not on P15-A's.
- **7e standing failure modes (R5 §2), item by item** — (1) no sympy `.H` on real symbolics
  in my code; I re-derived Λ^c from Kraus numerically/at mp, never symbolically with
  radicals. (2) pinned interpreter `C:<home>/cpython3119/python.exe` throughout.
  (3) complement convention re-derived from §1 and cross-checked against the closed form
  (max deviation 1.1e-16 at four x). (4) `.conj().T` everywhere; realness never assumed.
  (5) no `sorted()` on symbolic eigenvalues (no symbolic layer in my scripts).
  (6) LF used for all outputs. (7) degeneracy: explicit thresholds (1e-13 float,
  10^{-(dps−8)} in mpmath), every "zero" eigenvalue printed with its cluster; the rank-2 σ*
  handled by support projection rather than by inversion. (8) ε log ε: not used
  analytically by me; I note the ε log ε mechanism's d₁ vanishes exactly at 2/5, which is
  why 2/5 is not covered by the PROVED Q > 0. (9) anchoring — see 7c.
- **7f value-vs-formula** — A1: FORMULA carried by my §1.1 derivation, VALUES by my
  independent-construction numerics (code evaluates G, I_c from definitions, never from the
  identity). A2/G-A0/G-A+/G-Acal/A4: **VALUES only**, at specific float64 states; nothing
  here is a formula-level or exact-arithmetic result, and no σ was rationalised (correctly:
  chart-aware rationalisation was owed only on a G-A+ hit).
- **7g quantifier hygiene** — all terms resolve except §A3.3's "spread" (MAJOR 1).

---

## 6. Licensing opinion (what the decision layer may write, and what it may not)

**Licensable, at the tier stated:**

- **A1 (Proposition, §A1.1–A1.2): PROVED.** Independently re-derived, symbolically and
  numerically corroborated at 60 dps across decompositions; the no-faithfulness clause and
  the decomposition-independence are correct. Consequence `P_b2 ⟹ Q^{(1)} = 0`: **PROVED**.
- **G-Acal: PASS**, independently reproduced (400 samples + 60 restarts, no violation).
- **G-A0 at x = 2/5: licensed exactly as §A2.5 states it** — NUMERICAL / CERTIFIED\* at the
  value level: an explicit pair with `G < 0` and `I_c(σ*) < 0`, plus (§A2.2b, now
  value-verified by me) an explicit **full-rank** σ with `G ≤ −7.7e-2` and
  `−I_c(σ) = +2.77e-2 > 0`, so the P_b2 condition is strictly stronger than the
  `Q^{(1)}`-condition **at that σ**. `P_b2^rng` is dead at 2/5.
- **G-A+ NOT triggered**, independently confirmed; the onset conjecture
  `WHGAP.onset-two-fifths` survives this falsification attempt, at bounded-search strength
  only.
- **§A2.5's five non-claims**: endorsed verbatim. In particular channel-level strictness at
  x = 2/5 remains **conditional on the OPEN onset question** and must be written that way.

**NOT licensable:**

- **§A3.3's criterion** in its "in particular" form (MAJOR 1). The only proved content is
  `min_u G ≤ δ`, plus the correct contrapositive `p_v G_v > δ ⟹ some term < 0`. Do not
  register the criterion as a node in the note's wording.
- **§A4.3's / §5's strip null** (MAJOR 2). The correct record is: **P_b2 is numerically
  VIOLATED at x = 2/5 and at x = 41/100** (both with full-rank σ; 97–99.5% of generic
  restarts negative), and the bounded null holds only at x = 9/20 and x = 49/100. Obligation
  2 should be rewritten accordingly, and the new frontier question registered: *where in
  (0.41, 0.45) does P_b2 die?*
- Anything about tensorization (obligation 3) — untouched, as the note says.

---

## 7. Independent strip re-scan — completed; MAJOR 2 fully confirmed at all four points

`tools/whgap_r9_search.py strip` (log `artifacts/logs_whgap_p15a_20260730/r9_strip.log`,
`r9_strip.json`): my own optimizer, my own G, 200 unconstrained random restarts per point,
no seeding from any P15-A output.

| x | my `inf G` (200 restarts) | ⟨ψ|σ|ψ⟩ at min | my restarts < −1e-7 | note's A4 `inf G` |
|---|---|---|---|---|
| 2/5 | **−0.122420884165** | 0.00339 | **191/200** | −1.224209e-01 |
| **41/100** | **−0.0680339730197** | 0.00406 | **168/200** | **−6.803397e-02** |
| 9/20 | −3.56e-14 (corner stall, σ→P_ψ) | 1.000000 | 0/200 | +5.84e-09 |
| 49/100 | −4.80e-14 (corner stall, σ→P_ψ) | 1.000000 | 0/200 | +6.07e-09 |

My x = 41/100 minimum agrees with the note's own archived A4 value to **9 significant
digits**, from an independent optimizer and an independent implementation. The nulls at
9/20 and 49/100 are also independently reproduced: the only "negative" values there are
~1e-14 stalls into the degenerate corner where G → 0⁺, exactly as R8 minor m1 described.

So the corrected A4 record — now established by *my* runs, not only by the note's — is:
**P_b2 is violated at x = 2/5 and at x = 41/100, and survives a 200-restart bounded search
at x = 9/20 and x = 49/100.** Nothing in my plan is left incomplete.

## 8. Artifacts produced by this review

Scripts: `tools/whgap_r9_core.py`, `tools/whgap_r9_a1.py`, `tools/whgap_r9_a1mp.py`,
`tools/whgap_r9_search.py`, `tools/whgap_r9_refine.py`, `tools/whgap_r9_fullrank.py`.
Logs/JSON (all `r9_`-prefixed, additive, in `artifacts/logs_whgap_p15a_20260730/`):
`r9_a1.log/.json`, `r9_a1mp.log/.json`, `r9_gacal.log/.json`, `r9_x25.log/.json`,
`r9_refine.log/.json`, `r9_fullrank.log/.json`, `r9_strip.log/.json`.
Manifest: `artifacts/logs_whgap_p15a_20260730/SHA256SUMS_R9.txt` (LF, 21 entries — the six
scripts, the fourteen logs/JSON, and this report), written and verified with
`sha256sum -c` (21/21 OK). Interpreter `C:<home>/cpython3119/python.exe`
(numpy 1.26.4, scipy 1.14.1, mpmath 1.3.0, sympy 1.13.1).

Reproduction, from the repository root:

```
python -u tools/whgap_r9_a1.py       | tee artifacts/logs_whgap_p15a_20260730/r9_a1.log
python -u tools/whgap_r9_a1mp.py     | tee artifacts/logs_whgap_p15a_20260730/r9_a1mp.log
python -u tools/whgap_r9_search.py gacal | tee artifacts/logs_whgap_p15a_20260730/r9_gacal.log
python -u tools/whgap_r9_search.py x25   | tee artifacts/logs_whgap_p15a_20260730/r9_x25.log
python -u tools/whgap_r9_refine.py   | tee artifacts/logs_whgap_p15a_20260730/r9_refine.log
python -u tools/whgap_r9_fullrank.py | tee artifacts/logs_whgap_p15a_20260730/r9_fullrank.log
python -u tools/whgap_r9_search.py strip > artifacts/logs_whgap_p15a_20260730/r9_strip.log
```

(`r9_refine.py` consumes `r9_x25.json`, so run `x25` before it. Total wall time ~75 min.)

