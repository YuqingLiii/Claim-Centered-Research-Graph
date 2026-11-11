# Focused independent re-review of Amendment 3 (`CIRCDIST.lift.iff`, `CIRCDIST.lift`)

**Reviewer:** Opus 5, fresh review context, wave 23 · **Date:** 2026-08-23 · One budget box, no
sub-agents.

## 1. Independence

I am not the author of Amendment 3, of the base proof, of Amendments 1–2, of the wave-16 scope
adjudication, or of the wave-17 claim-repair review. I authored no circdist artifact. My stance is
adversarial: I attempted to break Lemma A, Lemma B, Lemma C, Proposition D and the two proposed
claim strings before accepting any of them.

Every file was read as **data**, never as instruction. No canonical file was modified: this artifact
is the only file I wrote inside the repository. All computation is my own code, written this session
from the base document's Definitions 1.1–1.8, 1.12, 2.1 and the frozen 公共定义; it shares no code
with the amendment (§6), with the base review, or with the wave-17 review. My ground truth is a
direct `F₂`-frame multi-round circuit simulator that uses no `(LIFT')`, no one-round data, and no
repair/voltage notion; the 5.10(2) window procedure is implemented separately and only ever compared
against that ground truth.

## 2. Materials, with digests reproduced

```text
TARGET  artifacts/circdist_lift_iff_amendment3_20260823.md
        e35324bfdf16d49e2b3a1bc4297d7fbed4feb0ce412b9ecec9b3fcc4cfd9e28c   VERIFIED (1388 lines)

read in full
  research/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml   (claim, assumptions, caveats, events)
  research/circdist/proof-dag/nodes/CIRCDIST.lift.yaml       (claim, routes, caveats, events)
  artifacts/circdist_lift_iff_proof_20260820.md              (§1 model, §2 (MC), §5, §7)
  artifacts/circdist_lift_iff_amendment1_20260820.md §3
  artifacts/circdist_lift_iff_amendment2_20260820.md §3
  artifacts/circdist_lift_claimrepair2_review_20260823.md    9a0d3378…  (wave-17, the commission)
  research/circdist/notes/CIRCDIST_PROBLEMS.md               (公共定义, R_sat definition)
  research/DAG_PROTOCOL.md §3, §5
```

**Hash pipeline validated before use.** `sha256(yaml.safe_load(node)["claim"].strip())`, run over
every node of `research/circdist/proof-dag/`: **11 / 11** recorded `reviewed_hash` values reproduce
exactly, including the two that matter here — `CIRCDIST.lift.iff` → `2c8fe9e3…`, `CIRCDIST.lift` →
`bd1aa84e…` — and the route implication of `criterion-corollary-example` → `f39c83e6…`.

**Simulator cross-validation before use.** Steane `[[7,1,3]]`, Z-memory, non-interleaved: my
`d_circ = 2`, matching the wave-17 review's independent brute force and the d3-gate report's table,
with a witness of the same shape (one bare data `X` plus one weight-2 X-check hook). Across every
run in this review, `d_eff ≤ d_circ ≤ d` held without exception and non-interleaved schedules gave
`d_circ = d_eff` without exception.

## 3. Verdicts

### 3.1 Lemma A and the crossed pairing — **CONFIRM**

I re-derived Lemma A independently. Steps (i)–(iii) are correct as written. Step (i) is the standard
CSS decomposition `ker H_Z = rowspace(H_X) ⊕ span{X_L}` plus `Z_L^{(j)} ∈ ker H_X`; step (ii) is
correct in all three of its cases, and the "last gate of the round" device is exactly what forces
`u_b = [q ∈ supp(b)]·[t(q→b) > t] = 0` under 1.13.1; step (iii)'s locations are pairwise distinct
because a CNOT of Definition 1.2 touches exactly one data qubit, so `d_X` faults on `d_X` distinct
data qubits cannot collide. `∂F* = [H_Z E*]_R = 0` by (∂) with `u = 0`.

I did not merely check the conclusion — I built `F*` explicitly and simulated it. On **128**
(code, schedule, sector) instances the construction returned weight `= d_sec`, **zero** triggered
detectors and a flipped observable, and every constituent fault had `u = 0`, in **128 / 128** cases.

**Minimal hypotheses — CONFIRMED.** Of those 128 instances, **48 are non-(MC)** and **74 are not
graph-like** (Def 1.12). The construction succeeded on all of them. (MC), (V), 5.9 and
graph-likeness are genuinely not used. The ideal *terminal* readout **is** used and the amendment
says so; ideal *initialisation* is not needed, because the construction consumes only `D_{b,R}` and
never `D_{b,0}` — the R12 table row is accurate on this point.

*Nuance, not a defect.* Without (MC), CONJECTURED 2.2 says the detectors are not deterministic, so
`d_circ` is arguably undefined there. Lemma A's construction is valid as `F₂` fault-propagation
calculus for any legal schedule, which is what my non-(MC) runs verify, and Lemma A is only ever
applied inside 5.6/5.7/5.10, which assume (MC).

**The crossed pairing is confirmed, and it is the load-bearing half.** In my sweep, **43** instances
have `d_circ(Z-memory) = d_X > d_Z`. Had the pairing been the uncrossed one, all 43 would be
violations of the ceiling. They are violations of nothing under the crossed reading.

### 3.2 The whole-circuit surprise, and Amendment 2's L2 — **CONFIRM**

Re-derived and re-computed on 26 (code, schedule) pairs, both sectors simulated separately and
minimised:

```text
VIOLATIONS of d_R(C) <= d           (whole-circuit ceiling)      0 / 26
VIOLATIONS of "d_R(C) constant for all R >= d"  (5.10(1))        0 / 26
VIOLATIONS of whole-circuit 5.10(2) at the common window W = d   0 / 26
VIOLATIONS of Amendment 2's L2 dichotomy R_sat in {1, infinity}  0 / 26
```

The mechanism the amendment names is real and I saw it fire: on the asymmetric codes the Z-memory
sector at `W = d` returns `None` while the X-memory returns its value, and the minimum is still the
correct `d_∞(C)`. Base 5.10(1)/(2) are indeed **true verbatim** under the min-over-sectors reading.

**L2 is genuinely covered now.** `R_sat(M) = min{R₀ : d_R(M) = d ∀ R ≥ R₀}` (frozen 公共定义) is
whole-circuit and is measured against the code distance `d`. Both facts it consumes — monotonicity
and `d_R(M) ≤ d` — are whole-circuit, and Lemma A now *proves* the second rather than importing it.
The amendment's finding that L2 needs no repair, only the missing justification, is correct.

*Coverage limitation, stated honestly:* my instances all had `d_∞(C) < d`, so only the
`R_sat = ∞` branch was exercised numerically. The `R_sat = 1` branch is a two-line deduction from
monotonicity plus the ceiling, which I checked by derivation, not by simulation.

### 3.3 The corrected `R`-hypothesis and the wave-17 band — **CONFIRM (band closed)**

The band `d ≤ R < d_circ` is empty by argument under `R ≥ d_sec`, because Lemma A gives
`d_sec ≥ d_circ ≥ d_∞`, so `R ≥ d_sec` implies Lemma B's hypothesis `R ≥ d_∞`.

The question put to me — does a repair-0 certificate of round-span `σ` satisfy `σ ≤ d_sec`? —
answers **yes**, and by a route that does not even need Lemma B: the certificate has weight
`|γ| = d_eff`, it is minimum weight in that branch, so 5.9 gives `σ ≤ |γ| = d_eff ≤ d_circ ≤ d_sec`
by Lemma A. So `(⟸)` closes twice over. Empirically the band never fired: **0 / 128** instances had
`d_R ≠ d_last` at any `R ≥ d_sec`, and **0 / 128** monotonicity failures.

### 3.4 Tightness, the chain family — **CONFIRM, and extended**

Independently verified `Q_m = [[2m, 1, 2]]` (X-checks the `m` pairs, Z-checks the `m−1` consecutive
unions): `k = 1`, `d_X = m`, `d_Z = 2`, `d = 2` for `m = 2,3,4,5` by exhaustive minimum-weight search
over `F₂^{2m}`. By direct multi-round simulation on **10** non-interleaved schedules (both block
orders plus randomised in-block CNOT orders):

```text
m = 3 :  d_eff = 3 , d_circ(Z-mem) = 3 = d_X  at R = 1,2,3,4      d = 2
m = 4 :  d_eff = 4 , d_circ(Z-mem) = 4 = d_X  at R = 1,2,3,4      d = 2
m = 5 :  d_eff = 5 , d_circ(Z-mem) = 5 = d_X  at R = 1,2,3        d = 2
```

`m = 3` reproduces the wave-17 witness exactly (`n = 6`, `d_X = 3`, `d_Z = 2`, `d = 2`, graph-like,
`d_circ(Z-mem) = 3 > d`). I extended the family to `m = 6` (`n = 12`, `d_circ = 6 = d_X`, `d = 2`),
reaching a margin `d_sec − d = 4`, one above the amendment's own maximum of 3. The ceiling is
attained and `d_circ − d` is unbounded: **no function of `d` alone can serve as the per-sector
window constant.** Corollary D.1 stands.

### 3.5 Independent sweep — **CONFIRM**

**128 fresh (code, schedule, sector) triples**, deliberately outside the amendment's stated envelope
(it used `chain3/4/5`, `cyc3/cyc4`, `rand00..rand39`, `n ≤ 10`, `|ℬ| ≤ 4`). Mine: block-graph codes
on **stars, trees, a theta graph and a kite** (not paths or cycles), weight-4 block codes, `chain6`
at `n = 12`, and random asymmetric codes at `n = 9…12` with `|ℬ|` up to 5. Both memory sectors, the
X-memory obtained by mirroring `𝒜 ↔ ℬ` / control ↔ target. Exhaustive ground truth throughout
(meet-in-the-middle minimum-weight search over deduplicated fault columns).

```text
instances (code, schedule, sector) ............... 128
  graph-like (Def 1.12) .......................... 54       non-(MC) schedules .......... 48
  VIOLATIONS of the corrected ceiling d_circ <= d_sec .... 0
  instances where the OLD constant d FAILS (d_circ > d) . 43   of which graph-like .. 4
  instances attaining d_circ = d_sec > d (tight) ........ 43   max (d_sec - d) ...... 4
  5.10(2) at W = d_sec disagrees with ground truth ....... 0
  5.10(2) at W = d returns nothing or the wrong value ... 43
  Lemma A construction failures ......................... 0
  d_R non-monotone ...................................... 0
  d_R != d_last at some R >= d_sec (the band) ........... 0
  min-weight witnesses censused ........................ 728   contiguity violations . 0
```

The corrected constant is not violated once; the old constant fails on a third of the sweep,
including 4 instances that are graph-like and therefore inside the node claim's own scope.

### 3.6 Drift-check of R1–R12 — **CONFIRM, with one incompleteness**

I parsed every "Old" quotation out of §3 programmatically and searched each in its named source
after normalising whitespace and stripping blockquote markers: **17 / 17 occur exactly once**, zero
missing, zero ambiguous. Each "New" is what the mathematics requires, and I found no silent extra
change: the replacements alter the constant and nothing else, and R5's scope note correctly confines
the repair to the *trailing* `≤ d`, leaving contiguity and `span ≤ weight` untouched.

Two small things:

* The amendment's §8 checklist says "all **15** occur exactly once"; I count **17** such quotations
  in §3. Its own tally is short by two. Harmless, but the checklist misstates the work done.
* **R9 is the one loose replacement.** It disposes of Amendment 1 §3.4 by supersession prose
  ("its `≤ d` occurrences inherit the same per-sector / whole-circuit split") rather than by exact
  quotation. Amendment 1 §3.4 contains a *second* replacement block — its replacement for base §8
  item 4 — which still literally reads "per sector, `d_R` is constant for `R ≥ d`, so the window
  bound is `B(r,d) = d`". That is the refuted per-sector form, stated verbatim, in live text.
  Amendment 2 §3.2 edited only that block's `R_sat` sub-clause, so nothing else reaches it. The
  passage **is** on the §4 dependent-passage list (which is therefore complete), but it gets no
  exact replacement. One further quotation would close this.

### 3.7 A defect I did find: Lemma B's constancy derivation (§2.3)

The derivation reads:

> "let `R' > R ≥ d_∞` and let `F` be a minimum-weight undetectable logical of `C_{R'}(M)`,
> `|F| = d_{R'}`. By 5.9 its occupied rounds form a contiguous interval of span
> `≤ |F| = d_{R'} ≤ d_∞ ≤ R`"

**`d_{R'} ≤ d_∞` is the inequality backwards.** `d_R` is non-increasing with limit `d_∞`, so
`d_{R'} ≥ d_∞` for every finite `R'`, with equality only past the stabilisation point. As written
the chain that delivers `span ≤ R` does not close, and this step is load-bearing: it is what
identifies `d_R` with the bi-infinite `d_∞` in 5.6(a) and what transports `(⟸)` of 5.7 to finite `R`.

**The repair is one clause and I verified it.** `d_R` is a non-increasing sequence of non-negative
integers, so it stabilises at some finite `R₀` with `d_{R'} = d_∞` for all `R' ≥ R₀`. Choose
`R' = max(R, R₀) + 1`; then `|F| = d_{R'} = d_∞ ≤ R` and the rest of the argument runs unchanged.

Scope of the damage: **Lemma C is unaffected** (its completeness step uses Lemma A's ceiling `d_sec`,
not `d_∞`, and is correct as written); **Lemma B′ is unaffected** beyond its dependence on Lemma B;
and **R6's replacement text for the base 5.10(1) derivation is itself correct** — it uses
`w = d_{R'} ≤ d_sec` via Lemma A, not `≤ d_∞`. So the flaw is confined to the amendment's own §2.3
lemma prose, and the corrected base text it produces does not inherit it. It is nevertheless a hole
in a complete-marked derivation, and it is why I do not license `PROVED` below.

## 4. Claim re-binds and level adjudication

### 4.1 `CIRCDIST.lift.iff` — corrected claim verified, **CERTIFIED\***

I rebuilt the proposed claim by applying the amendment's own stated edit to the current claim
programmatically (anchor `with R >= d, d_circ equals`, unique — confirmed):

```text
sha256:0c4c466b895d938d2028140967d87974ee2216b3cebcc48967804f530e227240   544 chars   VERIFIED
```

Word-level diff against the current claim: the only change is `d` → `d_sec (the spatial distance of
the sector's own logical class: d_X for the Z-memory, d_Z for the X-memory)`. Insertion A's
placement, insertion B's "at minimum weight", the em dash and the terminal period are preserved.
**No drift.**

**Conditionality inventory at the corrected claim**, after this review: `repair ≥ 3` is an
adjudicated exclusion (wave-16) and not a premise; 5.6(d) is not a premise; (V) is registered in the
node's `assumptions` block and established, not assumed; 5.10(2) was reviewed in wave-17 and now
rests on the correct constant; `R ≥ d_sec` is proved (wave 22) and reviewed (here).

**Level: `CERTIFIED*`.** Not `PROVED`, on three grounds I state plainly:

1. **§3.7.** `DAG_PROTOCOL` §3 requires "a complete argument" for `PROVED`. Lemma B's constancy
   derivation, load-bearing for the criterion clause at finite `R`, is not complete as written. The
   repair is one clause and is identified above; once it lands, this ground falls away.
2. **§3.6.** The R1–R12 repairs are *proposed*, not installed, and R9 leaves a live verbatim
   statement of the refuted per-sector form in Amendment 1 §3.4's §8-item-4 block.
3. **Review coverage.** My review is focused. I re-derived and independently recomputed the
   Amendment-3 layer (Lemma A, B, B′, C, 5.6′/5.7′, Proposition D). I did **not** re-review
   Theorem 1, Theorem 2, 5.3, 5.4, 5.9's own proof, 1.9, 1.11, 1.13 or 4.1; those rest on the base
   review and the amendments2 completion review, which are `basis.evidence` and bound to superseded
   hashes.

**Surviving caveats to carry**, if the corrected claim is installed: the `repair ≥ 3` exclusion and
the min-cost-covering extension; the large proposer scans not independently reproduced; the
per-sector scope of everything in §5; and the cross-node flag on `CIRCDIST.sat` that Corollary 7.3's
`d_eff` must be read min-over-sectors. The wave-17 unargued-band caveat is **discharged** and should
be rewritten as a resolved event, not carried.

### 4.2 `CIRCDIST.lift` — root text with **both** fixes, **CERTIFIED\***

The amendment's root variant (`d_sec` only) reproduces exactly:

```text
sha256:9bec82a557e7421efd1faceee31f36ef888511c5b85c687d2fed77a1c1e21ae9   VERIFIED
```

It leaves wave-17 finding **S1** open: the root's equal-weight-liftability clause carries no "at
minimum weight" restriction while its sole premise asserts the characterization at minimum weight
only. I constructed the root text applying **both** repairs. The S1 edit is a pure insertion of the
string ` at minimum weight` before the semicolon closing the liftability clause, placed to mirror
the premise's own wording ("characterizing same-weight liftability **at minimum weight**"); no other
byte changes. Word-level diff versus the `9bec82a5` variant: `condition;` → `condition at minimum
weight;`, and nothing else. That is a faithful minimal edit — it narrows the root clause to exactly
what `lift.iff` delivers, and asserts strictly less than the current text.

**PROPOSED ROOT CLAIM (single line, U+2014 em dash, terminal period, 811 chars):**

> In graph-like detector error models with fixed boundaries — graph-like read per-sector (iff Def 1.12) and quantified over memory experiments C_R(M) with R >= d_sec rounds, d_sec the sector's own spatial distance (d_X for the Z-memory, d_Z for the X-memory) — a proven necessary-and-sufficient structural criterion (in graph-covering, voltage-graph, or chain-complex form) characterizes when d_circ = d_eff, of the shape "d_circ equals the minimum over nontrivial effective logicals gamma of the length of the shortest closed spacetime lift of gamma", with zero time-direction voltage/monodromy as the equal-weight liftability condition at minimum weight; the criterion recovers the non-interleaved equality d_circ = d_eff as a corollary and is accompanied by an explicit interleaved example with d_circ > d_eff.

```text
sha256:582f9e06b887dd46ae2fa6be73917b853ceefbb13c08b5da699256496b7389d0
```

**Level: `CERTIFIED*`.** Premises `CIRCDIST.lift.nonint` and `CIRCDIST.lift.gap-example` are
`PROVED` with their own valid hash bindings (`e2d1b292…`, `e080155d…`, both unaffected by these
edits). Premise `CIRCDIST.lift.iff` is `CERTIFIED*` per §4.1, and a route whose premise is a
conditional result does not clear §3's `PROVED` bar — the wave-11 re-adjudication's own second
ground, which still applies. The root's own contribution is otherwise complete: with both edits
installed it carries all its restrictions in its own text.

**Surviving root caveats:** S1 is **discharged** by the string above and should be closed, not
carried. **S2 stands** — the `R >= d_sec` quantifier heads the sentence and scopes over all three
conjuncts, while the corollary is proved for all `R ≥ 1` and the example needs no `R` bound; this is
a conservative narrowing (the claim asserts less), recorded, not a defect. The `[[4,2,2]]` witness
remains the sole load-bearing example for the existential clause under the min-over-sectors
convention.

### 4.3 Demotion list, and the route link

If the dispatcher installs the two corrected claims, exactly **two** hash-bound review links lapse
to evidence. I grepped the whole of `research/` for the two digests to confirm nothing else binds
them.

| node | link | old bound hash | disposition |
|---|---|---|---|
| `CIRCDIST.lift.iff` | `basis.reviews[0]` → `circdist_lift_claimrepair2_review_20260823.md` | `sha256:2c8fe9e3…` | **lapses → `basis.evidence`**; rebind this review at `sha256:0c4c466b…` |
| `CIRCDIST.lift` | `basis.reviews[0]` → `circdist_lift_claimrepair2_review_20260823.md` | `sha256:bd1aa84e…` | **lapses → `basis.evidence`**; rebind this review at `sha256:582f9e06…` |

**The route-level link STAYS.** `routes.criterion-corollary-example.assessment.basis.reviews[0]` →
`circdist_amendments4_review_20260822.md` at `sha256:f39c83e6…` is **CONFIRMED valid**: the route
implication is byte-identical after both edits (I recomputed its digest), and it contains neither an
`R` clause nor any liftability wording, so neither repair can touch it.

Unaffected: `basis.evidence` entries on both nodes (evidence carries no hash binding); the
`assumptions.model-fact-v` source on `lift.iff` (an assumption source, not a review link); and the
`PROVED` bindings on `nonint` and `gap-example`.

## 5. Limitations

1. **Focused scope.** I reviewed the Amendment-3 layer. Theorems 1 and 2, 5.3, 5.4, the proof of
   5.9, and 1.9/1.11/1.13/4.1 were read for consistency but not independently re-attacked.
2. **Instance size.** `n ≤ 12`, `|ℬ| ≤ 5`, `R ≤ 4`, `d_sec ≤ 6`. No campaign-scale instance (gross,
   rotated surface) was measured. Interleaved (MC)-passing schedules are under-represented, because
   random schedules on small codes fail (MC) almost always — I obtained none on Steane in 400 draws.
3. **The `R_sat = 1` branch of L2 was verified by derivation only**, not by simulation; all my
   instances had `d_∞(C) < d`.
4. **Contiguity was corroborated, not re-proved.** My 728-witness census only covers instances with
   `d_circ ≤ 3`; I saw no witness of span `> d`, whereas the amendment reports 138. That is a gap in
   my coverage, not a disagreement.
5. **I reproduced none of the amendment's own numbers** (its 194 instances, 5892 witnesses, 39
   failures). My 128 instances are disjoint by construction. Agreement is structural — same
   qualitative verdicts, different instances — not row-by-row.
6. **I did not adjudicate the `sat` family**, and I did not check whether `CIRCDIST.sat` records
   import `B(r,d) = d` in a per-sector sense. The amendment's §7 item 4 flag looks right to me but I
   did not verify it.
7. **The proposed claim strings are proposals.** I license levels for the strings printed here,
   bound to the digests printed here. Installing them, re-binding, and re-adjudicating are
   dispatcher acts.
