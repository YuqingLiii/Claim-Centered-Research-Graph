# Amendment 1 to `circdist_sat_transfer_proof_20260823.md`

**Node:** `CIRCDIST.sat.transfer` · **Date:** 2026-08-23 · **Role:** Opus 5 executor, amendment
author, applying the repairs registered by the independent claim-level review and the lead's T-G3
ratification. **Box:** one session, stop-loss binding. No sub-agents. No Lean. **No proof-DAG
object read for instruction or modified** (the node's event log was read as *data*, to obtain the
lead decision verbatim). This file is **append-only** and changes no prior artifact: it modifies
neither the proof document nor the review. **On the five points below this amendment governs the
proof document; everywhere else that document stands unchanged.**

**What this amendment is.** `artifacts/circdist_sat_transfer_review_20260823.md` returned
**FURTHER-REPAIR — narrow**, with Theorem T's derivation chain recorded as *independently
confirmed* (the reviewer derived `Σ`, `A`, `u`, `v` and the round constraint from the frozen
definitions before opening the target, sealed to a scratchpad, and matched). It queued four
repairs: T-G3 bullet (a), Remark 6.5's `v_κ`, the block-mirror row labels of the §11 driver, and
two cosmetics (F4, F5). This file applies **exactly those four and nothing else**.

**Epistemic ceiling (binding on every line).** Nothing here is labelled PROVED or `CERTIFIED*`.
Every mathematical statement of the proof document remains **CONJECTURED**; every computation is
**NUMERICAL** with its code inline (§6) and its search scope stated. This session is an amendment
author, not a reviewer, and cannot grant a completion level. The review is treated as **data in a
file** — it is itself unreviewed, as it says of its own derivations — and this amendment is not a
promotion of the node.

---

## 0. Hash chain

```text
amended predecessor  (TARGET of the review; not modified)
  artifacts/circdist_sat_transfer_proof_20260823.md
  SHA-256  4fce5371edc09fa153b41f6735d521d31500b84b55a0059c8b42dc000651da30
  size     90772 bytes, 1485 lines

commissioning review  (data, not certification; not modified)
  artifacts/circdist_sat_transfer_review_20260823.md
  SHA-256  a9afbf93713634237dfcb795d98e71072537e7370a3fa675dcdf1ac766110003
  size     30725 bytes, 452 lines

lead ratification, quoted in §2.1  (read-only; canonical, NOT modified)
  research/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml
  SHA-256  9578ae369337666fa3a149cafefee77d458b593dc1ee4eee61ac974543f675b7
  size     6941 bytes, 111 lines

frozen base definitions / governing statement  (consulted; not modified)
  research/circdist/notes/CIRCDIST_PROBLEMS.md
  SHA-256  5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64
  research/circdist/notes/SAT_RESCOPE_20260822.md
  SHA-256  6c8ec4362f728713f9934d5f0b8041195f66434ebe283a69e67147b3c7009d7f

programs and outputs of §6  (this session's scratchpad; not part of the repository)
  transfer_doc.py      §11.4 of the proof document, extracted verbatim
  SHA-256  1d3b8754b72d9dc77a8c16ecfab1c8b81f9dcfd5dd0a9abb2baf1b1a26e64c68
  transfer_fixed.py    transfer_doc.py with exactly the Repair-3 patch of §4.2 applied
  SHA-256  f3dfa1f9048984de557cacee3cd0c6d56f04f7ae8a6036a256e5807552d19ced
  amend.py             the verification harness of §6.1, written for this amendment
  SHA-256  9a3e7db73b6dffdd079c21c9abd06f900199752b18ee918dc311c3fc60128291
```

**Chain link, checked, not assumed.** The digest of `transfer_doc.py` — the §11.4 program as
extracted from the predecessor's own bytes — reproduces `1d3b8754…`, the digest the predecessor
declares for it in its §0. So the program amended in §4 *is* the program the document published and
hashed. The review's §0 digest for the target (`4fce5371…`) is likewise the digest recomputed here.

**One digest has moved since the predecessor was written, legitimately.** The predecessor's §0
records the node record at `bb3f8464…`; it now hashes to `9578ae36…` because the node has since
gained the `transfer-review-2026-08-23` and `tg3-lead-ratification-2026-08-23` events. Nothing in
the predecessor's derivations depends on the node record; this is bookkeeping, recorded so the
mismatch is not later read as tampering.

**This artifact's own digest** is computed over its final bytes after writing and is reported in
this session's return record; it cannot be embedded in the bytes it measures. Any consumer should
recompute it and bind it as the successor link of the chain above.

**If any hash above fails to reproduce, this amendment is void until re-derived against the changed
input.**

---

## 1. Repair index

| # | review id | where in the predecessor | action here | verified |
|---|---|---|---|---|
| 1 | **F1** | §12, T-G3 risk-reduction bullet (a) | the mitigation is **withdrawn** and replaced by the corrected safe condition `span{D_{b,r}} ⊆ 𝒟' ⊆ 𝒟`; Definition 3.5 / 3.6 / 3.7 are **ratified** by the lead and stand verbatim; T-G3's closing sentence and §13's residual list propagate | §6.2, block **REPAIR 1** (counterexample recomputed, with the rank facts that make it a genuine complement) |
| 2 | **F2** | §6, Remark 6.5 | the no-`D_{b,0}` family is `(A_κ, v_κ)` with a **`κ`-dependent** terminal vector, not `(A_κ, v)` | §6.2, block **REPAIR 2** (16 instances: as printed 0/16, corrected 16/16) |
| 3 | **F3** | §11.4 driver `build()` | mirror the **circuit** (swap control/target at the same time step, relabel the families), not the schedule **name**; six `blk*/X` row labels become honest | §6.2, block **REPAIR 3**, and §6.3 (6/6 mislabelled rows exhibited; repaired program re-run, output byte-identical) |
| 4 | **F4, F5** | Cor 9.2 / Thm T(e) / A1; Thm T(a) box / Rem 6.6 | irreducibility language restricted to one sector block; `w > 2` "is false" downgraded, and §3.6 credited with forcing `w = 2` | no computation touched (text-level) |

Repairs 1–3 change **no computed value anywhere in the document**: F1 and F2 are counterfactual
statements about models Theorem T does not use, and F3 is a labelling defect. The document's 48
transfer-vs-direct values, its 18 parity-space rows, and every step of §4–§9 are untouched.

---

## 2. Repair 1 — T-G3 bullet (a): the mitigation is withdrawn, the corrected condition installed

### 2.1 The lead ratification this repair executes

The node record `research/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml`, event
`tg3-lead-ratification-2026-08-23`, carries the decision **verbatim** (quoted here as data; the file
is canonical and was not modified):

> **LEAD DECISION (verbatim: "批准 Definition 3.5, 缓解条款不批"):** Definition 3.5 — detectors are
> the parity quantities whose value is deterministic regardless of the prepared logical basis
> state — is RATIFIED as the intended reading of the frozen 公共定义, together with 3.6/3.7 (the
> review confirmed Def 2.7's Z-detectors span its Z-half exactly, so no computed value changes).
> The MITIGATION ("any D between Def-2.7 and V leaves the theorem intact") is REJECTED, per the
> review's explicit counterexample (d = 2 vs 3/4 on Steane+redundant-X); the corrected safe
> condition is D-prime within D (the 3.5 space), as supplied by the reviewer. T-G3 is hereby closed
> definitionally; the pending transfer amendment must cite this ratification and install the
> corrected condition.

So the decision splits three ways, and this amendment executes all three: **ratify** Definition 3.5
(and 3.6, 3.7) as printed; **reject** the mitigation; **install** the reviewer's corrected
condition in its place.

### 2.2 What was wrong

**Quoted from the predecessor, §12, T-G3, the sentence beginning "Three things reduce the risk"
(lines 1430–1434 at the bound hash):**

> Three things reduce the risk and should be recorded with the sub-claim: (a) whatever `𝒟` is
> chosen, if it contains the Definition-2.7 set and is contained in `V`, then Proposition 3.7's
> argument goes through verbatim, because `F^X` annihilates *all* of `V_X` and all of `𝒟_Z`;
> (b) the split is forced on the Z-side by 3.6's dimension count; (c) it is confirmed numerically
> on 18 instances including a dependent generating set (11.2).

Bullet (a) is asserted, never proved, and it is **false**. The reasoning it rests on is sound as far
as it goes — `F^X` does annihilate `V_X` and `𝒟_Z`, hence all of `𝒟 = 𝒟_Z ⊕ V_X` — but it stops one
line early. By 3.6, `V = 𝒟_Z ⊕ span{λ^{(1)},…,λ^{(k)}} ⊕ V_X` is **strictly larger** than `𝒟`, so a
`𝒟'` with `𝒟' ⊆ V` may contain elements with a non-zero `λ`-component, and `F^X` — being logical —
flips those by construction. The correct hypothesis is `𝒟' ⊆ 𝒟`, not `𝒟' ⊆ V`.

The review exhibits this on the document's own dependent-generator instance, and §6.2 below
recomputes it. With `P_X := m_{a_0,0} + m_{a_1,0} + m_{a_2,0} + m_{a_3,0}` the round-0 redundancy
parity of `steane+redX` (which exists because the four X-checks sum to zero), put

```
𝒟' := span{D_{b,r}}  +  span{D_{a,r}}  +  span{ P_X + λ } .
```

`𝒟'` satisfies bullet (a)'s hypothesis — it contains the whole Definition-2.7 set and is contained
in `V` — and it satisfies the stronger, more charitable reading T-G3's own headline uses, namely
that a detector space is a **complement of the observables**: `rank 𝒟' = dim V − 1`,
`𝒟' + span{λ} = V`, `λ ∉ 𝒟'`. Yet, in the Z-memory,

```
R = 2 :  d_R against Definition 2.7 = 2      d_R against 𝒟' = 3
R = 3 :  d_R against Definition 2.7 = 2      d_R against 𝒟' = 4
```

The mechanism is exactly the one bullet (a) overlooks: the minimising `F^X` flips `P_X` by `0` but
flips `λ` by `1`, hence flips `P_X + λ`, hence is **detected** against `𝒟'`, and recovering a
witness costs extra faults. It bites precisely in the dependent-generator case that §3 was written
to handle and that scope clause T1 puts explicitly in scope.

### 2.3 The replacement (governing)

**Bullet (a) is retired.** In §12, T-G3, the sentence quoted in §2.2 is replaced verbatim by:

> Three things bear on the residual risk and should be recorded with the sub-claim.
> **(a) The corrected safe condition — containment in `𝒟`, not in `V`.** If `𝒟'` satisfies
> ```
>       span{ D_{b,r} : b ∈ ℬ, r ∈ {0,…,R} }  ⊆  𝒟'  ⊆  𝒟 ,
> ```
> i.e. `𝒟'` lies **inside** the canonical detector space of Definition 3.5, then `d_R^Z(M)`
> computed against `𝒟'` equals `d_R^Z(M)` computed against the Definition-2.7 set. *Derivation:*
> the projected witness `F^X` of 3.1 annihilates `𝒟_Z` — because the `D_{b,r}` span `𝒟_Z`
> **exactly** (3.6) and `F^X` flips none of them — and by 3.1(2) it flips no X-check record at all,
> so it annihilates `𝒟_X = V_X` and hence all of `𝒟 ⊇ 𝒟'`; that gives `d^{𝒟'} ≤ d^{2.7}`, while
> `𝒟' ⊇ span{D_{b,r}}` together with 3.1(2) gives the reverse. This is Proposition 3.7's argument,
> with its hypothesis stated correctly. **Containment in `V` is not sufficient**, and the earlier
> form of this bullet — "if it contains the Definition-2.7 set and is contained in `V`, then
> Proposition 3.7's argument goes through verbatim" — is **false**: on `steane+redX` in the
> Z-memory, `𝒟' := span{D_{b,r}} + span{D_{a,r}} + span{P_X + λ}` contains the Definition-2.7 set,
> lies in `V`, and is a genuine complement of `span{λ}` in `V` (`rank 𝒟' = dim V − 1`,
> `𝒟' + span{λ} = V`, `λ ∉ 𝒟'`), yet `d^{2.7} = 2` against `d^{𝒟'} = 3` at `R = 2` and `4` at
> `R = 3`. The minimiser flips `λ` and therefore flips `P_X + λ`.
> **(b)** The split is forced on the Z-side by 3.6's dimension count.
> **(c)** It is confirmed numerically on 18 instances including a dependent generating set (11.2).
>
> **Residual risk, restated honestly.** It is *larger* than the retired bullet suggested. A reader
> who prefers a different canonical split is **not** automatically covered: only splits inside `𝒟`
> are. The case for Definition 3.5 therefore has to be made on its merits — and is: the review
> ratifies it as well-posed and canonical (Definition 3.2 first restricts to the *deterministic*
> parities `V`, and 3.5 then selects those whose *value* is constant across the logical-basis
> family, so state-independent-but-random parities are excluded; the value shift
> `Σ_j s_j⟨ζ^{(0)}, χ_{X_L^{(j)}}⟩` is linear in the parity, so `𝒟` is the kernel of a linear map
> `V → Hom(F₂^k, F₂)` and a genuine subspace), and the lead has ratified it as the intended reading
> of the frozen 公共定义 (node event `tg3-lead-ratification-2026-08-23`, 2026-08-23).

### 2.4 Dependent passages

| where | before | after / reason |
|---|---|---|
| §12, T-G3, "Three things reduce the risk…" | quoted in §2.2 | **replaced**, §2.3 |
| §12, T-G3, closing: "**What is not established is that Definition 3.5 is the split the frozen 公共定义 intends.** This is precisely the hole the window theorem labelled W-G3 and its review answered with S3′; §3 answers it more sharply, but the answer rests on a definition a reviewer must ratify." | — | **replaced by:** "**This was the one thing not established when the document was written; it is now established by decision, not by derivation.** The independent review ratifies Definition 3.5 as well-posed and canonical, and the lead has ratified it as the intended reading of the frozen 公共定义 (node event `tg3-lead-ratification-2026-08-23`: 批准 Definition 3.5). **T-G3 is closed definitionally.** What survives as a caveat is the corrected condition of (a): a future document that adopts a different split must place it inside `𝒟`, and if it does not, `d_R` may change — as the `steane+redX` counterexample shows it can." |
| §12 preamble: "**T-G3 is the one this session considers the sharpest**, because it is the only one that could change the *value* of `d_R` rather than the *generality* of the statement." | — | **replaced by:** "T-G3 was the sharpest of these when the document was written, being the only one that could change the *value* of `d_R` rather than the *generality* of the statement; it was closed definitionally on 2026-08-23 by the lead ratification of Definition 3.5, and is retained below with its corrected safe condition because the ratification is a decision about the intended reading, not a theorem." |
| §13, final sentence: "What this document does **not** settle: whether `Σ` is minimal, whether the canonical detector/observable split introduced in §3 is the one 公共定义 intends, and any instance value at `d ≥ 5`." | — | **replaced by:** "What this document does **not** settle: whether `Σ` is minimal, and any instance value at `d ≥ 5`. (The third item as originally printed — whether the canonical detector/observable split introduced in §3 is the one 公共定义 intends — was settled on 2026-08-23 by lead ratification of Definition 3.5, i.e. by decision rather than by derivation; the split must lie inside that `𝒟`, and containment in `V` is not enough.)" |
| **Definition 3.5, CONJECTURED 3.6, CONJECTURED 3.7** (§3.3) | — | **unchanged, verbatim.** Ratified. The review confirms 3.5 well-posed, 3.6's Z-side equality and X-side codimension by its own back-propagation, and 3.7's derivation as printed. 3.7 quantifies over the canonical `𝒟` and the Definition-2.7 set — both inside `𝒟` — so the corrected condition does not touch it. |
| §3.3 preamble ("`d_circ` is a function of `(circuit, fault model, detector/observable split)`, and the split must be pinned down…") | — | **unchanged.** Still true, and now the pinning is ratified rather than proposed. |
| §10 danger table, row "S3′ span subtleties with dependent checks" | — | **unchanged.** It argues from 3.1(2) plus the *equality* in 3.6 — the correct route — and never invokes the retired bullet. |
| §7 (≥)-direction, "undetectable (against Definition 2.7's set, and by 3.7 against the canonical `𝒟`)" | — | **unchanged.** Consumes 3.7, not the retired bullet. |
| §1 Theorem T box, §2.6 import table | — | **unchanged.** Neither mentions the detector-space choice. |
| §11.2 / NUMERICAL 3.8 | — | **unchanged.** They measure `𝒟` as defined by 3.5, which is ratified. |

---

## 3. Repair 2 — Remark 6.5: the no-`D_{b,0}` family needs a `κ`-dependent `v`

### 3.1 What was wrong

**Quoted from the predecessor, §6, Remark 6.5 (lines 603–610 at the bound hash):**

> **Remark 6.5 (what each boundary buys, quantitatively).** Drop the round-0 detector (noisy or
> unknown initialisation). Then (W) becomes `u(S_r) = H_Z σ_r + κ` for an unconstrained constant
> `κ ∈ F₂^ℬ`, and the correct object is no longer a single `(u,A,v)` but the family
> `A_κ[σ,σ'] := w_M(σ'−σ, H_Z σ + κ)` with `d_R = min_κ ( u ⊙ A_κ^{⊙R} ⊙ v )` — equivalently a
> state space `Σ × F₂^ℬ` in which `κ` is carried as a constant component. Drop the terminal detector
> instead and `v` loses its first clause, becoming `v[σ] = 0` iff `σ ≠ [0]`, which is a *different*
> and generally smaller quantity. **Both boundaries are load-bearing, in different places**, and
> this is the precise form of the round-0/terminal asymmetry.

The `A_κ` half is right and the `v` half is wrong. Re-run the document's own Lemma 6.2 computation
with `D_{b,0}` deleted: the terminal detector reads

```
      D_{b,R} = (H_Z σ_R)_b + [ (H_Z σ_{R−1}) + u(S_{R−1}) ]_b = (H_Z σ_R)_b + κ_b ,
```

so the terminal condition is `H_Z σ_R = κ`, **not** `H_Z σ_R = 0`. And since `E_tot ∉ ker H_Z` in
general once `κ ≠ 0`, Lemma 6.3's shortcut ("logical iff `σ_R ≠ [0]`", which is valid only on
`ker H_Z`) is unavailable: the logical condition is `λ(σ_R) = 1`. Keeping `v` fixed forces `κ = 0`
and collapses the family, so the printed formula does not merely lose precision — it computes the
wrong number, in **16 of 16** instances tested (§6.2).

### 3.2 The replacement (governing)

**Remark 6.5's first two sentences are replaced verbatim by:**

> **Remark 6.5 (what each boundary buys, quantitatively).** Drop the round-0 detector (noisy or
> unknown initialisation). Then (W) becomes `u(S_r) = H_Z σ_r + κ` for an unconstrained constant
> `κ ∈ F₂^ℬ`, and the terminal detector reads
> `D_{b,R} = (H_Z σ_R)_b + [(H_Z σ_{R−1}) + u(S_{R−1})]_b = (H_Z σ_R)_b + κ_b`, so the terminal
> condition becomes `H_Z σ_R = κ`. Since `σ_R` then need not lie in `ker H_Z`, Lemma 6.3's form of
> the logical condition is unavailable and the condition is `λ(σ_R) = 1` — for `k = 1`,
> `λ(σ) = ⟨σ, χ_{Z_L}⟩`, which descends to `Σ` by 4.2. The correct object is therefore no longer a
> single `(u,A,v)` but the family **`(A_κ, v_κ)`**,
> ```
>       A_κ[σ,σ'] := w_M(σ'−σ, H_Z σ + κ) ,     v_κ[σ] := 0 if H_Z σ = κ and λ(σ) = 1, else +∞ ,
>       d_R = min_{κ ∈ F₂^ℬ} ( u ⊙ A_κ^{⊙R} ⊙ v_κ ) ,
> ```
> — equivalently a state space `Σ × F₂^ℬ` in which `κ` is carried as a constant component, the
> terminal test reading the `κ`-component. **`v` must move with `κ`:** holding `v` fixed at
> `v[σ] = 0 iff H_Z σ = 0 and σ ≠ [0]` forces `κ = 0`, collapses the family, and returns the wrong
> value (§11.6: wrong in 16 of 16 tested instances; the `κ`-dependent form right in 16 of 16). At
> `κ = 0` the two coincide, which is why nothing in Theorem T is affected. Drop the terminal
> detector instead and …

(the remainder of the remark, from "Drop the terminal detector instead", stands verbatim.)

**Derivation status.** The corrected `(A_κ, v_κ)` is **CONJECTURED**, derived in the two lines above
from the document's own Lemmas 6.1–6.3 with the `D_{b,0}` constraint removed, and **NUMERICALLY**
confirmed in §6.3 on 16 instances. Like the printed remark it is a statement about a
**counterfactual model** — Theorem T *has* the round-0 detector — and is load-bearing for nothing.

### 3.3 Dependent passages

| where | before | after / reason |
|---|---|---|
| §6, Remark 6.5, first two sentences | quoted in §3.1 | **replaced**, §3.2 |
| §6, Remark 6.5, remainder ("Drop the terminal detector instead…") | — | **unchanged.** The terminal-detector counterfactual is a separate and correct statement. |
| §6, "Derivation of the boundary vectors" box (the `r = 0` and `r = R` bullets) | — | **unchanged.** They describe the model *with* both boundaries, where `κ = 0`; the round-0 bullet's "it forces `u(S_0) = 0`" is exactly the statement whose removal produces the free `κ`. |
| §10 danger table, row "round-0 / terminal detector meaning shift": "…Each boundary is load-bearing in a *different* place, and Remark 6.5 states exactly what each one buys." | — | **unchanged in wording, and now true as written.** Before this repair the cited remark did not state what the round-0 boundary buys; after it, it does. |
| §1 Theorem T(c), §7, §9 | — | **unchanged.** No step of the theorem or of §9 uses the `κ`-family; the review records the same ("no line of §7 or §9 inherits the error"). |
| §11 (numerical section) | — | **one addition:** the check of §6.2 below is filed as **NUMERICAL 11.6** and its code is §6.1. No existing §11 value changes. |
| node event `transfer-proof-2026-08-23`, summary phrase "the boundary quantified (without D_{b,0} the object is a matrix FAMILY over F2^B)" | — | **not modified here** — the node record is canonical and read-only for this session. Flagged for the dispatcher: the phrase is right about the family and silent about `v`; if the summary is ever rewritten it should say `(A_κ, v_κ)`. |

---

## 4. Repair 3 — the block-schedule mirror in the §11.4 driver

### 4.1 What was wrong

**Quoted from the predecessor, §11.4 (the driver, lines 1265–1290 at the bound hash):**

```python
# ---------------------------------------------------------------- driver
def mirror(code):
    return dict(n=code['n'], A=code['B'], B=code['A'], ZL=code['XL'], XL=code['ZL'])

def build(codename, schedname, sector):
    c = CODES[codename]
    cc = c if sector == 'Z' else mirror(c)
    if schedname.startswith('blk'):
        steps = sched_blocks(cc['A'], cc['B'], schedname[3])
    else:
        piX, piZ = SCHEDS[schedname]
        if sector == 'X': piX, piZ = piZ, piX
        steps = sched_corners(piX, piZ) if sector == 'Z' else sched_corners_mirror(piX, piZ)
    return Inst(cc['n'], cc['A'], cc['B'], cc['ZL'], steps,
                '%s/%s/%s' % (codename, schedname, sector), XL=cc['XL'])

def sched_corners_mirror(piX, piZ):
    """same physical CNOTs, roles swapped: A<->B."""
    steps = [[] for _ in range(4)]
    for i, slots in SURF_SLOT_Z.items():
        for t, cn in enumerate(piX):
            if cn in slots: steps[t].append(('aq', i, slots[cn]))
    for j, slots in SURF_SLOT_X.items():
        for t, cn in enumerate(piZ):
            if cn in slots: steps[t].append(('qb', j, slots[cn]))
    return steps
```

Mirroring is conjugation by `H^{⊗all}`: `CNOT(c,t) → CNOT(t,c)` at the **same time step**, with the
two ancilla families exchanging roles. `sched_corners_mirror` does exactly that and the interleaved
rows are correct. The block branch does not: it re-derives the block order from `schedname[3]`
**after** `A ↔ B` have been swapped, so `sched_blocks(cc['A'], cc['B'], 'Z')` puts the *mirrored*
`B`-block — i.e. the original X-checks — first, which is the physical mirror of `blkX`, not of
`blkZ`. The two block rows are therefore exchanged, for each of the three codes: **six of the
sixteen rows of Table 11.3 carry transposed labels** (§6.4 exhibits all six).

**No printed value changes**, because `blkZ/X` and `blkX/X` coincide for all three codes, and the
*set* of sixteen instances is exactly the intended one — so the coverage claim of NUMERICAL 11.1
survives intact. What was wrong is what the row labels *denote*.

### 4.2 The replacement (governing)

**The quoted block of §11.4 is replaced verbatim by** (this is the whole patch; nothing else in the
program changes, and `sched_corners_mirror` is deleted because the general rule subsumes it):

```python
# ---------------------------------------------------------------- driver
def mirror(code):
    return dict(n=code['n'], A=code['B'], B=code['A'], ZL=code['XL'], XL=code['ZL'])

def mirror_steps(steps):
    """Conjugation by H on every qubit: the SAME time steps, control and target swapped,
    the two ancilla families relabelled.  ('aq', i, q) = CNOT(anc_a_i -> q) mirrors to
    CNOT(q -> anc_a_i), and anc_a_i is a Z-check ancilla of the mirrored code."""
    return [[(('qb', i, q) if k == 'aq' else ('aq', i, q)) for (k, i, q) in ops]
            for ops in steps]

def phys_steps(codename, schedname):
    """the physical schedule of the named instance, written in Z-memory roles."""
    c = CODES[codename]
    if schedname.startswith('blk'):
        return sched_blocks(c['A'], c['B'], schedname[3])
    piX, piZ = SCHEDS[schedname]
    return sched_corners(piX, piZ)

def build(codename, schedname, sector):
    c = CODES[codename]
    cc = c if sector == 'Z' else mirror(c)
    steps = phys_steps(codename, schedname)
    if sector == 'X': steps = mirror_steps(steps)      # mirror the CIRCUIT, not the name
    return Inst(cc['n'], cc['A'], cc['B'], cc['ZL'], steps,
                '%s/%s/%s' % (codename, schedname, sector), XL=cc['XL'])
```

The patched program is `transfer_fixed.py`, SHA-256 `f3dfa1f9…` (§0). It was run; its stdout is
reproduced in §6.3 and **differs from the predecessor's published §11.3 output in exactly one line —
the wall-clock `elapsed` line** (`5.1s` → `4.6s`). Verified by `diff`, shown in §6.3.

### 4.3 Dependent passages

| where | before | after / reason |
|---|---|---|
| §11.4, driver block | quoted in §4.1 | **replaced**, §4.2 |
| §11.3, "Output, verbatim" — the 16-row Table 11.3 and the 16-row structure table | — | **unchanged, byte for byte** (`diff` in §6.4), but the six `blk*/X` rows now *denote* the instances their labels name. Repair 3 changes the meaning of six labels, not one character of the table. |
| §0, digest of the verification program `transfer.py` = `1d3b8754…` | — | **superseded for the repaired program:** the text of §11.4 as amended hashes to `f3dfa1f9…`. The old digest remains correct for the predecessor's own bytes and is retained there as the pre-repair record; any re-run should bind `f3dfa1f9…`. |
| **NUMERICAL 11.1** ("16/16 (schedule, sector) instances … 48/48 values, 0 disagreements"; "all entries finite", "exactly 2 zero-cost self-loops") | — | **unchanged.** All 48 values reproduce under the repaired program, and the instance *set* is unchanged. |
| **NUMERICAL 11.2** and the parity-space table (§11.3, lower block) | — | **unchanged, and not affected at all:** the driver calls `build(cn, sn, 'Z')` there, and the Z-branch of `build()` never took the defective path. |
| §11's "Schedules" scope bullet ("two non-interleaved (Z-block-first, X-block-first …)") | — | **unchanged.** Both block schedules are present in both sectors either way. |
| §8 (CONJECTURED 8.1, the mirror of Definitions 2.6–2.11) | — | **unchanged.** The mathematical mirror was always stated correctly — "`𝒜 ↔ ℬ`, `X ↔ Z`, control ↔ target" is precisely the rule the repaired code now implements; the defect was in the driver only. |

---

## 5. Repair 4 — the two cosmetics

### 5.1 F4 — irreducibility is a per-block property

**Quoted from the predecessor, Corollary 9.2 (lines 724–729):**

> **Corollary 9.2 (spectrum).** All entries of `A` are finite (5.5), so `A` is irreducible; all
> weights are `≥ 0` and `A` has a zero-weight loop at `[0]`, so the min-plus eigenvalue is
> `λ_⊙(A) = 0`; the critical graph is exactly the set of `2^k` self-loops at `{σ : H_Z σ = 0}` (4.3),
> whose cyclicity is `1`. By the cyclicity theorem (ASSUMPTION A1 below), `A^{⊙(R+1)} = A^{⊙R}` for
> all `R` beyond some transient — `A^{⊙R}` is eventually **constant**, not merely eventually
> periodic. *The recon's "`2^{2k}` self-loops" is corrected to `2^k`.*

The assembled two-sector matrix of Theorem T(d) is `A = A^Z ⊕ A^X`, which is block-diagonal and
therefore **reducible**, while A1 is stated for irreducible matrices. The conclusion survives — each
block is irreducible with eigenvalue `0` and cyclicity `1`, so each block is eventually constant and
so is the direct sum — but the language should not stand in a text headed for certification.

**Governing correction.** In Corollary 9.2 the first clause becomes

> All entries of the **single-sector** matrix `A^Z` are finite (5.5), so `A^Z` is irreducible; …

and the final sentence of 9.2 gains

> The assembled two-sector matrix `A = A^Z ⊕ A^X` of T(d) is block-diagonal and hence **reducible**;
> A1 is applied to each block separately, and a direct sum of eventually-constant blocks is
> eventually constant, so T(e)'s conclusion holds for the assembled matrix as well.

In **Theorem T(e)** (§1) the sentence "Hence the min-plus eigenvalue of `A` is `0`, its critical
graph consists of exactly `2^k` self-loops (`2^k + 2^k` for the assembled two-sector system), and
its cyclicity is `1`" gains the parenthesis "(per sector block; the assembled `A = A^Z ⊕ A^X` is
block-diagonal, and the spectral statements are applied blockwise)". In **A1** the phrase "For
irreducible `A`" is retained as the statement of the imported theorem, and its *Load-bearing for*
line gains "…and it is applied to a single irreducible sector block, never to the assembled
block-diagonal matrix". A1 remains **declared non-load-bearing** (9.3–9.6 do not use it), which is
why this is cosmetic.

### 5.2 F5 — `w > 2`, and what actually forces `w = 2`

**Quoted from the predecessor, Theorem T(a) box (lines 74–76) and Remark 6.6 (lines 612–616):**

> **No measurement memory and no logical bookkeeping beyond this class is needed** (Lemma 6.4); the
> corresponding statement for a detector window `w > 2` is false and is out of scope (Remark 6.6).

> **Remark 6.6 (detector window `w > 2`).** If detectors spanned `w` consecutive rounds, (W) would
> couple `u(S_r)` to the previous `w−2` rounds' record flips, and Theorem T(a) would be **false** as
> stated: the state would have to be enlarged to `Σ × (F₂^ℬ)^{w−2}`. Definition 2.7 fixes `w = 2`,
> which is exactly why no measurement memory appears in `Σ`. The recon's §3.7 sketch of the `w > 2`
> case is consistent with this and is out of scope here.

Two defects, both presentational. "Is false" is asserted, not shown — what is shown is that the
*argument* breaks and the state would have to be enlarged. And crediting **Definition 2.7** with
fixing `w = 2` undersells the document: 2.7 is a *definition*, so it could in principle be replaced;
what actually forbids a canonical Z-side detector spanning more than two rounds is the **equality**
`𝒟_Z = span{D_{b,r}}` of 3.6, together with the model facts that ancilla frames are zeroed each
round and round location sets are disjoint (T2). The theorem is better supported than its own remark
claims.

**Governing correction.** In the **T(a) box**, "the corresponding statement for a detector window
`w > 2` is false and is out of scope (Remark 6.6)" becomes

> for a detector window `w > 2` the same statement **would require enlarging the state space to
> `Σ × (F₂^ℬ)^{w−2}`, and is out of scope** (Remark 6.6).

and **Remark 6.6** becomes

> **Remark 6.6 (detector window `w > 2`).** If detectors spanned `w` consecutive rounds, (W) would
> couple `u(S_r)` to the previous `w−2` rounds' record flips, and Theorem T(a)'s state space would
> no longer suffice: it would have to be enlarged to `Σ × (F₂^ℬ)^{w−2}`. This document does not
> claim that no smaller sufficient statistic exists in that regime; it claims only that the
> derivation of §6 does not deliver one, so `w > 2` is **out of scope**. Within scope, `w = 2` is
> not merely a stipulation of Definition 2.7: it is **forced**, by the model (ancilla frames zeroed
> each round, round location sets disjoint — T2) and, for the canonical detector space, by the
> **equality** `𝒟_Z = span{D_{b,r}}` of 3.6, which leaves no canonical Z-side detector spanning
> more than two rounds. That is why no measurement memory appears in `Σ`. The recon's §3.7 sketch of
> the `w > 2` case is consistent with this and is out of scope here.

**Dependent passages for §5.** §6 Lemma 6.1–6.4 and §7: **unchanged** (the `w = 2` fact they use is
Lemma 6.1, which is proved, not the remark). §9 Corollaries 9.3–9.6: **unchanged** (they do not use
A1). §10 danger table: **unchanged**. The review's independent test of Lemma 6.1 — 378,720 detector
predictions, 0 mismatches, across interleaved and dependent-generator instances — is recorded here
as **corroboration of the replacement wording**, and was not re-run in this session; it is the
review's number, not this amendment's.

---

## 6. Verification, with code and genuine stdout

**Method and its inherited limitation, stated first.** The simulation core used below is the
predecessor's **own** §11.4 program, extracted verbatim from the artifact's bytes (its SHA-256
reproduces the digest the document declares, §0) and imported as `transfer_doc`. That is deliberate
and it is also a limitation:

* it is *required* for Repair 3, which is a defect **in** that program — a fix has to be exhibited
  against the program it fixes;
* it is *appropriate* for Repair 2, whose two arms (direct multi-round simulation with `D_{b,0}`
  deleted; the min-plus family) are that program's own two arms with one constraint removed;
* but it means **these checks are not independent of the document's model design** in the way the
  reviewer's were. The reviewer wrote its own simulator from its own pre-read derivation and got the
  same numbers; that agreement, not this section, is the independent evidence. What this section
  establishes is that the repairs are correct *and reproduce the reviewer's reported values exactly*
  on the document's own machinery — which is what an amendment must show before installing them.

Everything below the import was written for this amendment. No `stim`, no external library, no
sampling; Python 3.9.6, single process, `nice -n 19`, under 8 s wall clock. **Background processes
started by this session: none** (the `job3.py` / `job7k.py` / `noclass.py` / `witness2.py` +
`kissat` workers on this machine belong to another work item and were not touched, inspected or
signalled).

### 6.1 The harness, verbatim

```python
"""Amendment 1 to circdist_sat_transfer_proof_20260823.md -- local verification of the
repairs queued by artifacts/circdist_sat_transfer_review_20260823.md.

The simulation core is the document's OWN section 11.4 program, extracted verbatim from the
artifact (its SHA-256 reproduces the digest declared in the document's section 0) and imported
here as `transfer_doc`.  That is deliberate: repair 3 is a defect IN that program, so the fix
has to be exhibited against the program itself, and repair 2 concerns a formula whose two
arms (direct simulation / min-plus) are that program's two arms.  Everything below the import
was written for this amendment.

REPAIR 3 (F3): the correct physical mirror.  Mirroring conjugates by H^{tensor all}: CNOT(c,t)
  -> CNOT(t,c) at the SAME time step, ancilla families swap roles.  build() instead re-derived
  the block order from schedname[3] after swapping A <-> B, which reverses the two blocks.
REPAIR 2 (F2): Remark 6.5's no-D_{b,0} matrix family, document formula vs the reviewer's
  corrected v_kappa, both against direct simulation with D_{b,0} deleted.
REPAIR 1 (T-G3(a)): the reviewer's counterexample D' on the dependent-generator code.

No stim, no external library, no sampling, single process.
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import transfer_doc as T           # the document's section 11.4 program, verbatim

INF = float('inf')

# ================================================================ REPAIR 3: physical mirror
def mirror_steps(steps):
    """Conjugation by H on every qubit: same time steps, control/target swapped, families
    relabelled.  ('aq', i, q) is CNOT(anc_a_i -> q); its mirror is CNOT(q -> anc_a_i), and in
    the mirrored code anc_a_i is a Z-check ancilla, i.e. the op ('qb', i, q)."""
    return [[(('qb', i, q) if k == 'aq' else ('aq', i, q)) for (k, i, q) in ops]
            for ops in steps]

def phys_steps(codename, schedname):
    """the physical schedule of the named instance, in Z-memory roles."""
    c = T.CODES[codename]
    if schedname.startswith('blk'):
        return T.sched_blocks(c['A'], c['B'], schedname[3])
    piX, piZ = T.SCHEDS[schedname]
    return T.sched_corners(piX, piZ)

def build_fixed(codename, schedname, sector):
    """section 11.4's build(), with the mirror taken on the CIRCUIT rather than on the name."""
    c = T.CODES[codename]
    cc = c if sector == 'Z' else T.mirror(c)
    steps = phys_steps(codename, schedname)
    if sector == 'X':
        steps = mirror_steps(steps)
    return T.Inst(cc['n'], cc['A'], cc['B'], cc['ZL'], steps,
                  '%s/%s/%s' % (codename, schedname, sector), XL=cc['XL'])

def norm(steps):
    return tuple(tuple(sorted(ops)) for ops in steps)

# ================================================================ generalised brute force
def column_gen(I, R, r_f, rf, drop_r0=False, extra=None):
    """Definition-2.7 detector vector + optional extra parity + observable, for one fault.
    drop_r0 deletes every D_{b,0} (Remark 6.5's counterfactual model).
    extra='PXlam' appends the parity (sum_a m_{a,0}) + lambda (the reviewer's D' generator)."""
    xf = zf = 0; recB = []; recA = []
    for r in range(R):
        xf, zf, mb, ma = T.run_round(I, xf, zf, rf if r == r_f else {})
        recB.append(mb); recA.append(ma)
    ro = [(xf >> q) & 1 for q in range(I.n)]
    bits = []
    for j in range(I.nb):
        for r in range(R + 1):
            if r == 0:
                if not drop_r0:
                    bits.append(recB[0][j])
            elif r < R:
                bits.append(recB[r][j] ^ recB[r-1][j])
            else:
                bits.append((sum(ro[q] for q in I.B[j]) % 2) ^ recB[R-1][j])
    for i in range(I.na):
        for r in range(1, R):
            bits.append(recA[r][i] ^ recA[r-1][i])
    obs = sum(ro[q] for q in I.ZL) % 2
    if extra == 'PXlam':
        bits.append((sum(recA[0][i] for i in range(I.na)) % 2) ^ obs)
    v = 0
    for b in bits:
        v = (v << 1) | b
    return (v << 1) | obs

def brute_dR_gen(I, R, cap=4, **kw):
    """min weight of an undetectable-and-logical fault set; meet-in-the-middle to weight cap."""
    fl = T.faults(I, xsector=False)
    cols = set()
    for r in range(R):
        for rf in fl:
            c = column_gen(I, R, r, rf, **kw)
            if c:
                cols.add(c)
    cols = sorted(cols)
    target = 1                                    # every detector 0, observable flipped
    lvl2 = {0: 0}
    for c in cols:
        if c not in lvl2 or lvl2[c] > 1:
            lvl2[c] = 1
    for i, a in enumerate(cols):
        for b in cols[i+1:]:
            s = a ^ b
            if s and (s not in lvl2 or lvl2[s] > 2):
                lvl2[s] = 2
    ans = cap + 1
    for s, w in lvl2.items():
        o = lvl2.get(s ^ target)
        if o is not None and w + o < ans:
            ans = w + o
    return ans if ans <= cap else None

# ================================================================ transfer arm, factored
def transfer_parts(I):
    """section 11.4's transfer arm, factored so that the constant kappa can be varied.
    dist[E | (mu << n)] = w_M(E, mu) on representatives; Sig = coset minima of F_2^n / S_X."""
    n, nb = I.n, I.nb
    cols = set()
    for rf in T.faults(I, xsector=True):
        xf, zf, mb, ma = T.run_round(I, 0, 0, rf)
        mu = 0
        for j in range(nb):
            mu |= mb[j] << j
        c = xf | (mu << n)
        if c:
            cols.add(c)
    cols = sorted(cols)
    from collections import deque
    size = 1 << (n + nb)
    dist = [-1] * size; dist[0] = 0; dq = deque([0])
    while dq:
        s = dq.popleft()
        for c in cols:
            t = s ^ c
            if dist[t] < 0:
                dist[t] = dist[s] + 1; dq.append(t)
    SX = {0}
    for row in [T.mask(a) for a in I.A]:
        SX |= {s ^ row for s in SX}
    SX = sorted(SX)
    canon = {}
    for E in range(1 << n):
        if E not in canon:
            cl = min(E ^ s for s in SX)
            for s in SX:
                canon[E ^ s] = cl
    Sig = sorted(set(canon.values()))
    def HZ(E):
        v = 0
        for j, b in enumerate(I.B):
            if bin(E & T.mask(b)).count('1') % 2:
                v |= 1 << j
        return v
    return Sig, dist, SX, HZ

def minplus(Sig, Amat, vvec, Rmax):
    """u = indicator([0]); return [u (min-plus) A^R (min-plus) v : R = 1..Rmax]."""
    N = len(Sig)
    vec = [0 if Sig[i] == 0 else INF for i in range(N)]
    out = []
    for _ in range(1, Rmax + 1):
        nv = [INF] * N
        for i in range(N):
            if vec[i] == INF:
                continue
            for j in range(N):
                t = vec[i] + Amat[i][j]
                if t < nv[j]:
                    nv[j] = t
        vec = nv
        out.append(min(vec[i] + vvec[i] for i in range(N)))
    return out

def rem65_family(I, Rmax, corrected):
    """Remark 6.5's family.  A_kappa[s,s'] = w_M(s'-s, H_Z s + kappa).
    document:  v [s] = 0 iff H_Z s = 0     and s != [0]      (kappa-INDEPENDENT)
    corrected: v_k[s] = 0 iff H_Z s = kappa and lambda(s) = 1 (kappa-DEPENDENT)"""
    Sig, dist, SX, HZ = transfer_parts(I)
    n, N = I.n, len(Sig)
    ZLm = T.mask(I.ZL)
    lam = lambda s: bin(s & ZLm).count('1') % 2
    best = [INF] * Rmax
    for kappa in range(1 << I.nb):
        Amat = [[INF] * N for _ in range(N)]
        for a, s in enumerate(Sig):
            mu = HZ(s) ^ kappa
            for b, sp in enumerate(Sig):
                m = INF
                for g in SX:
                    d = dist[(s ^ sp ^ g) | (mu << n)]
                    if 0 <= d < m:
                        m = d
                Amat[a][b] = m
        if corrected:
            vv = [0 if (HZ(s) == kappa and lam(s) == 1) else INF for s in Sig]
        else:
            vv = [0 if (HZ(s) == 0 and s != 0) else INF for s in Sig]
        vals = minplus(Sig, Amat, vv, Rmax)
        best = [min(best[i], vals[i]) for i in range(Rmax)]
    return best

# ================================================================ parity spaces (T-G3)
def spaces(I, R):
    """exact back-propagation; returns record list, the V- and D-obstruction tables."""
    n, na, nb, Tn = I.n, I.na, I.nb, I.T
    gates = []
    for r in range(R):
        for t in range(Tn):
            for (k, idx, q) in I.steps[t]:
                if k == 'aq': gates.append((n + r*(na+nb) + idx, q))
                else:         gates.append((q, n + r*(na+nb) + na + idx))
    recs = []
    for r in range(R):
        for i in range(na): recs.append(('a', i, r))
        for j in range(nb): recs.append(('b', j, r))
    for q in range(n): recs.append(('ro', q))
    XLm = T.mask(I.XL)
    oV, oD = [], []
    for key in recs:
        if key[0] == 'a':   x, z = 1 << (n + key[2]*(na+nb) + key[1]), 0
        elif key[0] == 'b': x, z = 0, 1 << (n + key[2]*(na+nb) + na + key[1])
        else:               x, z = 0, 1 << key[1]
        for (c, t) in reversed(gates):
            if (x >> c) & 1: x ^= 1 << t
            if (z >> t) & 1: z ^= 1 << c
        dm = (1 << n) - 1
        xd, zd, xa, za = x & dm, z & dm, x >> n, z >> n
        bad = 0; bit = 0
        for q in range(n): bad |= ((xd >> q) & 1) << bit; bit += 1
        for r in range(R):
            for i in range(na): bad |= ((za >> (r*(na+nb)+i)) & 1) << bit; bit += 1
            for j in range(nb): bad |= ((xa >> (r*(na+nb)+na+j)) & 1) << bit; bit += 1
        oV.append(bad)
        oD.append(bad | ((bin(zd & XLm).count('1') % 2) << bit))
    return recs, oV, oD

def rk(vs):
    return T.rank2(list(vs))

# ================================================================ driver
if __name__ == '__main__':
    t0 = time.time()
    good = T.find_interleaved()
    T.SCHEDS['ilv0'] = good[0]
    T.SCHEDS['ilv1'] = good[len(good)//2]
    CODENAMES = ('steane713', 'surface913', 'steane+redX')

    print('=' * 78)
    print('REPAIR 3 (F3) -- the block-schedule mirror in the section 11.4 driver')
    print('=' * 78)
    print('for each code: does the X-sector instance that build() constructs equal the')
    print('physical mirror of blkZ, or of blkX?')
    print()
    bad = 0
    for cn in CODENAMES:
        for sn in ('blkZ', 'blkX'):
            doc = norm(T.build(cn, sn, 'X').steps)
            mz  = norm(mirror_steps(phys_steps(cn, 'blkZ')))
            mx  = norm(mirror_steps(phys_steps(cn, 'blkX')))
            print('  %-12s %s X-sector: == mirror of blkZ? %-5s   == mirror of blkX? %s'
                  % (cn, sn, doc == mz, doc == mx))
            bad += (doc != norm(mirror_steps(phys_steps(cn, sn))))
    print()
    print('  block rows built by build() from the WRONG physical schedule: %d of 6' % bad)
    ok_i = all(norm(T.build('surface913', sn, 'X').steps)
               == norm(mirror_steps(phys_steps('surface913', sn))) for sn in ('ilv0', 'ilv1'))
    print('  interleaved rows already correct in build(): %s' % ok_i)

    print()
    print('=' * 78)
    print('REPAIR 3 -- Table 11.3 re-emitted with the mirror fixed (labels now honest)')
    print('=' * 78)
    jobs = [(cn, sn) for cn in CODENAMES for sn in ('blkZ', 'blkX')]
    jobs += [('surface913', 'ilv0'), ('surface913', 'ilv1')]
    print('%-30s %-3s %-16s %-16s %s' % ('instance', 'sec', 'brute d_R', 'transfer d_R', 'match'))
    allok = True
    for (cn, sn) in jobs:
        for sec in ('Z', 'X'):
            I = build_fixed(cn, sn, sec)
            assert I.mc
            tr, nsig, nzs, fin, _ = T.transfer(I, 3)
            br = [brute_dR_gen(I, R) for R in (1, 2, 3)]
            ok = (br == tr); allok &= ok
            print('%-30s %-3s %-16s %-16s %s'
                  % ('%s/%s' % (cn, sn), sec, str(br), str(tr), 'OK' if ok else 'MISMATCH'))
    print()
    print('  ALL transfer == brute, correctly-labelled instances : %s' % allok)

    print()
    print('=' * 78)
    print('REPAIR 2 (F2) -- Remark 6.5, the no-D_{b,0} family')
    print('=' * 78)
    print('truth  = direct simulation with every D_{b,0} deleted')
    print('doc    = min_kappa u (+) A_kappa^R (+) v      (v as printed in Remark 6.5)')
    print('corr   = min_kappa u (+) A_kappa^R (+) v_kappa,  v_kappa[s]=0 iff H_Z s = kappa, lam(s)=1')
    print()
    INST = [('steane713', 'blkZ'), ('surface913', 'blkZ'), ('steane+redX', 'blkZ'),
            ('surface913', 'ilv1')]
    print('%-26s %-32s %s' % ('instance', 'R=2', 'R=3'))
    ndoc = ncorr = ntot = 0
    for (cn, sn) in INST:
        for sec in ('Z', 'X'):
            I = build_fixed(cn, sn, sec)
            truth = [brute_dR_gen(I, R, drop_r0=True) for R in (2, 3)]
            doc   = rem65_family(I, 3, corrected=False)[1:]
            corr  = rem65_family(I, 3, corrected=True)[1:]
            cells = []
            for i in range(2):
                cells.append('truth %s  Rem6.5 %s  corrected %s'
                             % (truth[i], doc[i], corr[i]))
                ntot += 1
                ndoc += (doc[i] == truth[i]); ncorr += (corr[i] == truth[i])
            print('%-26s %-32s %s' % ('%s/%s/%s' % (cn, sn, sec), cells[0], cells[1]))
    print()
    print('  Remark 6.5 as printed agrees with the truth : %d of %d' % (ndoc, ntot))
    print('  reviewer-corrected v_kappa agrees           : %d of %d' % (ncorr, ntot))

    print()
    print('=' * 78)
    print("REPAIR 1 (T-G3(a)) -- the reviewer's counterexample D' on steane+redX")
    print('=' * 78)
    A4 = T.CODES['steane+redX']['A']
    x = 0
    for a in A4: x ^= T.mask(a)
    print('  XOR of the four X-checks of steane+redX = %d  (so P_X is deterministic)' % x)
    print()
    for R in (2, 3):
        I = build_fixed('steane+redX', 'blkZ', 'Z')
        recs, oV, oD = spaces(I, R)
        ri = {k: i for i, k in enumerate(recs)}
        def vec(ks):
            v = 0
            for k in ks: v ^= 1 << ri[k]
            return v
        def obs(c, table):
            v = 0
            for i in range(len(recs)):
                if (c >> i) & 1: v ^= table[i]
            return v
        Db = []
        for j in range(I.nb):
            for r in range(R + 1):
                if r == 0:  Db.append(vec([('b', j, 0)]))
                elif r < R: Db.append(vec([('b', j, r), ('b', j, r-1)]))
                else:       Db.append(vec([('ro', q) for q in I.B[j]] + [('b', j, R-1)]))
        Da  = [vec([('a', i, r), ('a', i, r-1)]) for i in range(I.na) for r in range(1, R)]
        lam = vec([('ro', q) for q in I.ZL])
        PX  = vec([('a', i, 0) for i in range(I.na)])
        Dp  = Db + Da + [PX ^ lam]
        dimV = len(recs) - rk(oV)
        dimD = len(recs) - rk(oD)
        print('  R=%d  #records %d   dim V %d   dim D (Def 3.5) %d' % (R, len(recs), dimV, dimD))
        print('        lambda in V: %-5s  lambda in D: %-5s   P_X in V: %-5s  P_X in D: %s'
              % (obs(lam, oV) == 0, obs(lam, oD) == 0, obs(PX, oV) == 0, obs(PX, oD) == 0))
        print("        rank D' = %d (= dim V - 1: %s)   rank D' u {lambda} = %d (= dim V: %s)"
              % (rk(Dp), rk(Dp) == dimV - 1, rk(Dp + [lam]), rk(Dp + [lam]) == dimV))
        print("        lambda not in D': %-5s   D' contains the Def-2.7 set: %-5s   D' inside V: %s"
              % (rk(Dp + [lam]) > rk(Dp), rk(Dp) == rk(Dp + Db + Da),
                 all(obs(c, oV) == 0 for c in Dp)))
        print("        rank span{D_b,r} = %d   rank span{D_b,r} u {D_a,r} = %d"
              % (rk(Db), rk(Db + Da)))
        d27 = brute_dR_gen(I, R)
        dDp = brute_dR_gen(I, R, extra='PXlam')
        print("        d_R against Def-2.7 = %s      d_R against D' = %s" % (d27, dDp))
    print()
    print('elapsed %.1fs' % (time.time() - t0))
```

### 6.2 Output, verbatim

```text
==============================================================================
REPAIR 3 (F3) -- the block-schedule mirror in the section 11.4 driver
==============================================================================
for each code: does the X-sector instance that build() constructs equal the
physical mirror of blkZ, or of blkX?

  steane713    blkZ X-sector: == mirror of blkZ? False   == mirror of blkX? True
  steane713    blkX X-sector: == mirror of blkZ? True    == mirror of blkX? False
  surface913   blkZ X-sector: == mirror of blkZ? False   == mirror of blkX? True
  surface913   blkX X-sector: == mirror of blkZ? True    == mirror of blkX? False
  steane+redX  blkZ X-sector: == mirror of blkZ? False   == mirror of blkX? True
  steane+redX  blkX X-sector: == mirror of blkZ? True    == mirror of blkX? False

  block rows built by build() from the WRONG physical schedule: 6 of 6
  interleaved rows already correct in build(): True

==============================================================================
REPAIR 3 -- Table 11.3 re-emitted with the mirror fixed (labels now honest)
==============================================================================
instance                       sec brute d_R        transfer d_R     match
steane713/blkZ                 Z   [2, 2, 2]        [2, 2, 2]        OK
steane713/blkZ                 X   [2, 2, 2]        [2, 2, 2]        OK
steane713/blkX                 Z   [2, 2, 2]        [2, 2, 2]        OK
steane713/blkX                 X   [2, 2, 2]        [2, 2, 2]        OK
surface913/blkZ                Z   [3, 3, 3]        [3, 3, 3]        OK
surface913/blkZ                X   [2, 2, 2]        [2, 2, 2]        OK
surface913/blkX                Z   [3, 3, 3]        [3, 3, 3]        OK
surface913/blkX                X   [2, 2, 2]        [2, 2, 2]        OK
steane+redX/blkZ               Z   [2, 2, 2]        [2, 2, 2]        OK
steane+redX/blkZ               X   [2, 2, 2]        [2, 2, 2]        OK
steane+redX/blkX               Z   [2, 2, 2]        [2, 2, 2]        OK
steane+redX/blkX               X   [2, 2, 2]        [2, 2, 2]        OK
surface913/ilv0                Z   [3, 3, 3]        [3, 3, 3]        OK
surface913/ilv0                X   [2, 2, 2]        [2, 2, 2]        OK
surface913/ilv1                Z   [2, 2, 2]        [2, 2, 2]        OK
surface913/ilv1                X   [3, 3, 3]        [3, 3, 3]        OK

  ALL transfer == brute, correctly-labelled instances : True

==============================================================================
REPAIR 2 (F2) -- Remark 6.5, the no-D_{b,0} family
==============================================================================
truth  = direct simulation with every D_{b,0} deleted
doc    = min_kappa u (+) A_kappa^R (+) v      (v as printed in Remark 6.5)
corr   = min_kappa u (+) A_kappa^R (+) v_kappa,  v_kappa[s]=0 iff H_Z s = kappa, lam(s)=1

instance                   R=2                              R=3
steane713/blkZ/Z           truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
steane713/blkZ/X           truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
surface913/blkZ/Z          truth 1  Rem6.5 3  corrected 1   truth 1  Rem6.5 3  corrected 1
surface913/blkZ/X          truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
steane+redX/blkZ/Z         truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
steane+redX/blkZ/X         truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
surface913/ilv1/Z          truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
surface913/ilv1/X          truth 1  Rem6.5 3  corrected 1   truth 1  Rem6.5 3  corrected 1

  Remark 6.5 as printed agrees with the truth : 0 of 16
  reviewer-corrected v_kappa agrees           : 16 of 16

==============================================================================
REPAIR 1 (T-G3(a)) -- the reviewer's counterexample D' on steane+redX
==============================================================================
  XOR of the four X-checks of steane+redX = 0  (so P_X is deterministic)

  R=2  #records 21   dim V 15   dim D (Def 3.5) 14
        lambda in V: True   lambda in D: False   P_X in V: True   P_X in D: True
        rank D' = 14 (= dim V - 1: True)   rank D' u {lambda} = 15 (= dim V: True)
        lambda not in D': True    D' contains the Def-2.7 set: True    D' inside V: True
        rank span{D_b,r} = 9   rank span{D_b,r} u {D_a,r} = 13
        d_R against Def-2.7 = 2      d_R against D' = 3
  R=3  #records 28   dim V 22   dim D (Def 3.5) 21
        lambda in V: True   lambda in D: False   P_X in V: True   P_X in D: True
        rank D' = 21 (= dim V - 1: True)   rank D' u {lambda} = 22 (= dim V: True)
        lambda not in D': True    D' contains the Def-2.7 set: True    D' inside V: True
        rank span{D_b,r} = 12   rank span{D_b,r} u {D_a,r} = 20
        d_R against Def-2.7 = 2      d_R against D' = 4

elapsed 7.7s
```

### 6.3 The repaired §11.4 program, re-run, and its `diff` against the published Table 11.3

The patched program `transfer_fixed.py` (§4.2) was run on its own; `out_doc113.txt` is the
predecessor's §11.3 output block extracted from the artifact's bytes, `out_fixed.txt` the repaired
program's stdout:

```text
$ diff out_doc113.txt out_fixed.txt
63c63
< elapsed 5.1s
---
> elapsed 4.6s
```

One line differs, and it is the wall clock. **Repair 3 changes no printed value and no printed
character of Table 11.3; it changes which physical instance six of the labels denote.**

### 6.4 Reading the output

* **Repair 3.** All six `blk*/X` instances that `build()` constructed are the mirror of the *other*
  block schedule (`False` / `True` in every row), and the two interleaved rows were already correct
  — exactly the review's F3, reproduced row for row. With the patch, all 16 correctly-labelled
  instances still satisfy transfer `=` brute force at `R = 1,2,3`: **48/48, 0 disagreements**.
* **Repair 2.** With every `D_{b,0}` deleted, the true `d_R` is `1` in all 16 tested cases (a single
  data-qubit `X` before round 0 is now undetectable, and logical). Remark 6.5 as printed returns
  `2` or `3` — it is pinned to `κ = 0`, i.e. it returns the value of the *unmodified* model —
  and is wrong in **16 of 16**; the `κ`-dependent `v_κ` returns `1` and is right in **16 of 16**.
  The per-instance values reproduce the review's table exactly (`2,2,3,2,2,2,2,3` for the printed
  formula, at both `R = 2` and `R = 3`).
* **Repair 1.** `P_X` is deterministic (the four X-checks of `steane+redX` XOR to `0`) and *is* a
  canonical detector (`P_X in D: True`), while `λ` is deterministic and is *not* (`lambda in D:
  False`) — Definition 3.5 behaving exactly as 3.6 says. `𝒟'` contains the Definition-2.7 set, lies
  in `V`, has rank `dim V − 1`, and `𝒟' + span{λ} = V` with `λ ∉ 𝒟'`: a genuine complement of the
  observables satisfying the retired bullet's hypothesis. And `d^{2.7} = 2` while `d^{𝒟'} = 3`
  (`R = 2`) and `4` (`R = 3`). At `R = 3` the ancillary dimensions `#records 28`, `dim V 22`,
  `dim 𝒟 21`, `rank span{D_{b,r}} 12`, `rank span{D_{b,r}} ∪ {D_{a,r}} 20` all reproduce the
  review's §4(4b)/§4(4c) numbers, and `dim 𝒟_Z = 12`, `dim 𝒟 − rank = 1 = dim leftker(H_X)` agree
  with the predecessor's own Table 11.3 parity block. The mitigation is refuted on the document's
  own instance, with the document's own machinery.

---

## 7. What this amendment does **not** change

1. **It promotes nothing.** `CIRCDIST.sat.transfer` stays as the dispatcher finds it,
   **CONJECTURED**. Rule 6 still requires an independent claim-level review before the node may
   carry a completion level; the review that commissioned these repairs withheld promotion pending
   exactly these items and is not a certification of this amendment. The review's own forward
   statement — "With F1–F3 repaired, I see no remaining obstacle in the mathematics to `CERTIFIED*`
   for the transfer arm" — is *its* judgement, recorded here as data; this session does not act on
   it, and a re-review is the dispatcher's call.
2. **It changes no mathematical content of §4–§9.** No step of the derivation chain is touched.
   The review found nothing in it to touch: "Nothing I found touches the derivation chain of
   Theorem T."
3. **The open minors stay open, verbatim.** **T-G1** (inherited model clauses: Definition 2.8's
   taxonomy, T2, T3 — imported, not re-derived), **T-G2** (minimality of `Σ` — OPEN, and
   value-neutral), **T-G4** (computability of `A`: exponential, with NP-hardness explicitly *not*
   claimed), **T-G5** (scope of finiteness: a model lacking both weight-1 mechanisms would break
   Corollary 9.2's irreducibility and the "no unreachable states" claim). None of the four is
   addressed, weakened or strengthened here. **T-G3** is the only sub-claim this amendment moves,
   and it moves by lead decision on the definitional question plus the corrected safe condition —
   not by new mathematics.
4. **The scope is unchanged and still excludes `d ≥ 5`, `k > 1`, genuine qLDPC instances, `R > 3`,
   and any claim about `R_stab ≥ 2`.** §11's "Not covered" bullet stands verbatim.
5. **The review's two optional recommendations are deliberately NOT folded in**, because they were
   not queued as repairs and this session's instruction is to apply exactly the queued repairs: the
   `[[4,2,2]]` `k = 2` instance (which would close the `k > 1` coverage hole precisely where the
   `2^k`-vs-`2^{2k}` correction and the `2^k − 1` count of finite `v` entries become discriminating)
   and the direct Lemma 6.1 test (378,720 predictions, 0 mismatches). Both are recorded here as
   **available, cheap, and unexecuted**, so a later session can pick them up without re-deriving
   them; the review's numbers for them are the review's, not this amendment's.
6. **It modifies no existing file.** Nothing under `research/circdist/proof-dag/` was written; the
   node record was read only to quote the lead decision. The proof document and the review are
   untouched — this amendment governs the predecessor on the five points above by being read
   alongside it, in the project's established append-only pattern. Files created by this session:
   this one.
7. **Deviations from the queued repairs: none.** All four repairs are installed with the reviewer's
   supplied content, and the lead's three-way decision (ratify 3.5/3.6/3.7; reject the mitigation;
   install `𝒟' ⊆ 𝒟`) is executed as written. Two things are recorded rather than silently absorbed,
   neither of which is a deviation from the queued content: the verification harness is not
   independent of the document's model design (§6 preamble), and the §0 digest of the verification
   program necessarily moves when the program is repaired (§4.3).
