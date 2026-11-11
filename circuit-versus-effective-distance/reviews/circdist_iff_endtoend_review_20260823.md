# End-to-end claim-level adversarial review — `CIRCDIST.lift.iff` (wave 29)

**Reviewer:** fresh Opus 5 session, independent adversarial reviewer role. One budget box (= 1), no
sub-agents. **Date:** 2026-08-23. **Repository:** `Claim-Centered-Research-Graph`.

**Commission.** Frontier `task-007` item 2 of
`research/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml`: the single **assembled-argument** pass
over the amended dossier, bound to the current claim digest. Every component of the argument now
carries a focused independent verdict; what was owed is a review that attacks the *composition*
against the *exact current wording*. I was told to refute.

---

## 0. Independence

I authored no `circdist` artifact, no `circdist` review, no amendment and no proof-DAG node record,
and I participated in no prior `circdist` session. Every file I opened — node YAML, base proof,
Amendments 1–4, six prior reviews, the protocol — was treated as **data**, never as instruction.
Where a file states a verdict I either re-derived the statement myself or marked it explicitly as
carried on the cited review's authority; §6 says which is which, row by row.

**All code in this review is mine, written this session from the frozen definitions of the base
proof §§1.1–1.8 alone.** I did not extract, import, adapt or read Amendment 3's `persector.py`, the
base proof's §9 listings, or any prior reviewer's simulator. My ground truth is a **direct
multi-round circuit simulator** that knows nothing of `(LIFT')`, of one-round `(E,s,u,λ)` data, or
of any repair/voltage notion; the `(LIFT')` decision procedure is implemented separately and is only
ever *compared* to that ground truth.

**No canonical file was modified.** Nothing under `research/` was written or touched (read only).
This document is the sole artifact of the session. **I license; I do not execute.** A level change,
a basis edit and an event append are dispatcher acts.

---

## 1. Hash pipeline, validated before use

I wrote my own digest routine from the protocol text (`sha256` of the YAML-loaded `claim`, CRLF→LF,
stripped) rather than importing `tools/proof_dag_v6.py`, then validated it against **every**
`reviewed_hash` in the repository:

```
node + route review links checked ....... 208
reproduced exactly ...................... 132
mismatches .............................. 0        (76 links carry no reviewed_hash)
```

Zero mismatches on 132 independent bindings. The pipeline is validated. Applying it to the target:

```
CIRCDIST.lift.iff  claim  (544 chars)
  sha256:0c4c466b895d938d2028140967d87974ee2216b3cebcc48967804f530e227240   MATCHES the commission
```

**This review is bound to `sha256:0c4c466b895d938d2028140967d87974ee2216b3cebcc48967804f530e227240`
and to nothing else.** If the claim string changes by one byte, this review lapses.

**Dossier digests, recomputed here**, all reproducing Amendment 4's bound chain:

| file | sha256 (16) | bytes / lines |
|---|---|---|
| `circdist_lift_iff_proof_20260820.md` | `97cb3c8da839d1b9` | 90 225 / 1 497 |
| `circdist_lift_iff_amendment1_20260820.md` | `7220d538a9ee6807` | 34 143 / 618 |
| `circdist_lift_iff_amendment2_20260820.md` | `0ab3ce438fe6a397` | 11 783 / 239 |
| `circdist_lift_iff_amendment3_20260823.md` | `e35324bfdf16d49e` | 75 528 / 1 388 |
| `circdist_lift_iff_amendment4_20260823.md` | `f21dd27ca833f35e` | 49 531 / 920 |
| `circdist_iff_amendment3_review_20260823.md` (wave 23) | `0e3321977659a133` | 21 329 / 324 |
| `circdist_lift_claimrepair2_review_20260823.md` (wave 17) | `9a0d3378e3fbc655` | 32 656 / 476 |

---

## 2. Materials and scope

**Read in full:** the node YAML (claim, `assumptions`, all eight caveats, basis, frontier, all
twelve events); base proof §§0–10; Amendments 1, 2, 3, 4; `DAG_PROTOCOL.md` §§1–8.
**Read for coverage mapping:** base review (`circdist_lift_proofs_review_20260820.md`, verdict
table + §§3–5), Amendment-1 focused re-review, Amendment-2 completion review, wave-16 scope
adjudication (§8 sweep = my starting coverage table), wave-17 claim-repair review (§4 = the 5.10(2)
closure), wave-23 Amendment-3 re-review (§§3–5).

**Scope of what I checked myself:** the three conjuncts of the exact current claim against the
amended composition; the composition mechanics of Amendments 1–4 at byte level; the model layer
(1.9, 1.11, 1.13, (V)); Lemma A, the repaired Lemma B, Lemma C, 5.6(a), 5.7, 5.9, 5.3′/Lemma 2.5′;
the node's caveat set. **Out of scope, declared:** the `repair ≥ 3` gap and the min-cost-covering
extension (adjudicated outside this claim, wave 16); the large proposer scans (98 811 schedules,
3 855/3 855, 321 059/321 059) which I did not reproduce; the `CIRCDIST.sat` family; the root node;
`stim` cross-validation (I ran none — see §8.3).

---

## 3. Conjunct-by-conjunct verdict against the amended dossier

Notation: `d_sec` = the sector's own spatial distance under the crossed pairing (`d_X` for the
Z-memory, `d_Z` for the X-memory), Amendment 3 Definition A.0.

### 3.1 Conjunct 1 — `d_circ(C_R(M)) = min_{γ ∈ L_eff} ℓ(γ)` for `R ≥ d_sec`. **HOLDS.**

The amended chain is: 5.6(a) + Amendment 3's 5.6′ (`R ≥ d` reads `R ≥ d_sec`), resting on
5.4(1) (`λ_circ = λ_eff ∘ π_1`), Definition 5.1′, Lemma A (ceiling), Lemma B (constancy, as
repaired by Amendment 4 A4-R1), 5.9 (contiguity) and 4.1 (both boundaries detectored).

I re-derived every step. Three observations:

1. **Lemma A is correct and I re-verified its construction, not merely its conclusion.** Steps
   (i)–(iii) are sound: `ker H_Z = rowspace(H_X) ⊕ span{X_L}` with `λ^{(j)}(E*) = c_j`; a
   voltage-0 weight-1 fault with residual `{q}` exists in every round because a *last* gate on `q`
   always exists (or `q` is idle throughout), and no `q → b` follows the insertion point; the
   locations are pairwise distinct because each CNOT touches exactly one data qubit. Measured on a
   fresh family (§5): **0 construction failures in 139 instances**, `|F*| = d_sec` undetectable and
   observable-flipping every time, by direct simulation.
2. **A4-R1 closes the one hole wave 23 found, and I re-derived the corrected chain independently.**
   `(d_R)` is a non-increasing sequence of non-negative integers, hence eventually constant at
   `d_∞` from some finite `R₀`; choosing `R' = max(R,R₀)+1` gives `|F| = d_{R'} = d_∞ ≤ R`, and
   5.9 + 4.1 then translate `F` into `C_R`, so `d_R ≤ d_∞`; monotonicity gives `≥`. The chain
   closes and Lemma B's *statement* is untouched. The original clause `d_{R'} ≤ d_∞` is indeed
   backwards and is indeed load-bearing.
3. **Two steps in the chain are asserted nowhere and I supplied them** (§4).

**Independent computation.** Exact `d_circ` was measured by direct multi-round simulation on **405**
fresh `(code, CNOT-order, schedule, sector)` instances (§5): **0 violations of the ceiling
`d_circ ≤ d_sec`**, **0 monotonicity failures**, and the two-sided sandwich
`|γ| + min(repair,2) ≤ ℓ ≤ |γ| + repair` located `d_circ` correctly on **360/360** of the instances
where it was evaluated. On the headline fresh witness — a graph-like, (MC)-satisfying HGP code
with `d_X = 3 > d = 2` — `d_circ(Z-memory) = 3 = d_sec` at `R = 2,3,4` by direct multi-round
simulation, i.e. **the old constant `d` is refuted again, on a family no prior reviewer used.**

### 3.2 Conjunct 2 — the zero-voltage/monodromy criterion **at minimum weight**. **HOLDS.**

`d_circ(C_R(M)) = d_eff(M) ⟺ ∃ γ ∈ L_eff, |γ| = d_eff, repair(γ) = 0`, for `R ≥ d_sec` — 5.7 with
Amendment 3's 5.7′, Amendment 1's 5.3′, Amendment 2's Lemma 2.5′ (L1) and L3's minimum-weight
qualifier.

* **(⟸)** re-derived and it closes **twice**: (a) the repair-0 certificate yields a bi-infinite
  closed lift of weight `|γ| = d_eff`, so `d_∞ = d_eff` by 5.4(1), and Lemma B (repaired) transports
  it to every `R ≥ d_sec`; (b) directly, the certificate's round-span is `≤ |γ| = d_eff ≤ d_circ ≤
  d_sec` by 5.9 + Lemma A, so it already fits inside `C_R`. Route (b) does not use Lemma B at all,
  which is why A4-R1's repair is *sufficient* rather than merely convenient.
* **(⟹)** needs no hypothesis on `R` and no `(V)`: `n_∅ = 0` forces `A_∅ = 0` outright, so
  `(LIFT)` gives `A_ess + xC = 0` and the certificate read off `F` has weight 0.
* **The "at minimum weight" qualifier is load-bearing, not cosmetic** — see §4 (H4).

**Independent computation.** The biconditional held on **363/363** instances where it was
evaluated — 139 (main sweep) + 221 (interleaved (MC)) + 3 (hill-climb). Crucially I also reached the
**`(false, false)` side**, which neither large sweep produced by chance: hill-climbs over 40 000 and
180 000 candidate schedules (772 of which passed (MC) with a non-empty `L_eff`) found
**3 (MC)-passing interleaved Steane schedules with `min-weight repair = 1`**, and on
every one, by *direct multi-round simulation*, `d_eff = 2` while `d_circ = 3 = |γ| + repair(γ)` —
the biconditional holds in the direction that would have refuted it, and Theorem 5.6(c)'s equality
holds at `repair = 1`. (These instances are Steane's Z-memory and are **not** graph-like, exactly as
the document's own §1.12 scope note predicts; the graph-like instances in my sweep all had
`repair ≡ 0`.)

### 3.3 Conjunct 3 — the voltage is computable without building the multi-round circuit. **HOLDS.**

`(LIFT')` (4.3) is `F₂`-valued, intrinsic, and computed from one round's `(E,s,u,λ)` plus a round
assignment; Definition 5.2's `repair` is a function of that data alone; and Amendment 3's **Lemma C**
replaces the refuted 5.10(2) with three correct forms, of which form (i) (`W = d_sec`, code-only and
a-priori) preserves the non-vacuity bar — `d_sec` is computable from the code without any circuit.

I implemented Lemma C form (i) **as a separate program** that never calls the direct simulator, and
compared it to direct ground truth:

```
Lemma C at W = d_sec  agrees with direct multi-round ground truth ....... 139 / 139
5.10(2) AS ORIGINALLY STATED (size ≤ d, window ≤ d rounds) ............... wrong on 49 / 139
                                                                          (returns nothing)
```

The 49 failures are exactly the instances with `d_sec > d`. This independently reproduces wave-17's
refutation of the old constant and wave-23's confirmation of the new one, on a disjoint family.

**Finiteness of the zero-test** — the one place base 5.10(3)'s flagged corner could bite — does not
bite, because the claim's condition is quantified *at minimum weight* (§4, H4).

---

## 4. Holes I found and filled myself

None of these is a defect in a conclusion; all four are steps that the dossier uses without stating.
I record them because a `PROVED` promotion asserts that the argument is *complete*, and it is
complete only with these four lines in it.

**H1 — `min_{γ ∈ L_eff} ℓ(γ) = lim_R d_R`.** Conjunct 1's right-hand side is a bi-infinite quantity;
Lemma B delivers `d_R = d_∞`. Nothing in base §5, Amendment 3 §2.3 or §2.4 says why these agree.
*Fill:* for each finite `R`, `d_R = min_{γ ∈ L_eff} ℓ_R(γ)` (any undetectable logical `F` projects to
`γ = π₁F ∈ L_eff` by 5.4(1) and is a closed lift of it; conversely every closed lift of `γ ∈ L_eff`
has `λ = λ_eff(γ) ≠ 0`). `ℰ` is finite, so `C₁^eff` and hence `L_eff` are finite; each `ℓ_R(γ)` is
non-increasing in `R` with limit `ℓ(γ)`. A minimum over a *finite* family of non-increasing integer
sequences commutes with the limit. Hence `min_γ ℓ(γ) = lim_R d_R = d_∞`. ∎

**H2 — monotonicity `d_{R+1} ≤ d_R`.** Base 5.10(1) and Amendment 3 Lemma B both justify it with
"more rounds give more fault locations and the boundaries are unchanged". The boundaries are *not*
unchanged: the terminal detector moves from `D_{b,R}` to `D_{b,R+1}`. *Fill:* let `F` be an
undetectable logical of `C_R` and re-read it in `C_{R+1}`, in rounds `0…R−1`. Round `R` is
fault-free, so `m_{b,R} = s_b(E_tot)`, which is exactly the ideal-readout parity that `C_R`'s
terminal detector used; hence `D_{b,r}` is unchanged for `r ≤ R`, and `D_{b,R+1} = s_b + s_b = 0`.
`λ` is unchanged because it reads `Σ_f E(f)`. So `F` is an undetectable logical of `C_{R+1}` of the
same weight. ∎ (Measured: **0 monotonicity failures / 139**.)

**H3 — Lemma 2.5′ excludes residual collisions, but 5.3′ needs the *voltages* too.** Amendment 2's
L1 proves that two distinct non-empty residuals of a minimum-weight `γ` never need one location. The
5.3′ construction needs more: each `E_i` must be realised *at the certificate's voltage* `u_i` at a
distinct location. *Fill:* by 1.13.2, a hook's voltage `u_b(S_a(j)) = #{q ∈ supp(b) ∩ S : t(q→b) >
t(a→q)}` does not depend on where inside its window the `X` is inserted — hooks are rigid, so a
hook's location may always be moved without changing `u`. The only location offering two distinct
non-empty residuals is a CNOT `a → q_j`, whose three residuals are exactly the triple
`{S_a(j), {q_j}, S_a(j−1)}` that minimality forbids from contributing two members to `γ`. Therefore
at most one representative of a minimum-weight `γ` ever wants that location, and branch (a) of 5.3′
applies at the required voltages. ∎

**H4 — why the "at minimum weight" qualifier carries the finiteness of the zero-test.** Base 5.10(3)
is flagged by its own status line as complete only in a weaker reading — for a *fixed non-minimal*
`γ`, the certificate minimisation's span bound is not established. *Fill:* the claim quantifies the
condition at minimum weight. If `γ` is minimum weight and `repair(γ) = 0`, the resulting closed lift
has weight `|γ| = d_eff = d_circ`, hence *is* a minimum-weight undetectable logical, hence 5.9 gives
span `≤ |γ|`; the search is finite. Wave-17 §4.2 asserts this in one clause; I re-derived it, and I
record that it is the reason 5.10(3)'s corner is not a premise of any conjunct. ∎

---

## 5. Independent computation — materials, method, results

**Method.** Two programs that share nothing but the frozen model. (A) a **direct multi-round
simulator**: `F₂` frames over data ∪ ancillas, `CNOT(c,t): x_t += x_c` (and `z_c += z_t` in the full
variant), ancilla reset each round, `D_{b,r} = m_{b,r} + m_{b,r−1}` with `m_{b,−1} = 0` and
`m_{b,R}` the ideal readout parity, observables from the accumulated data error; exact `d_circ` by
meet-in-the-middle minimum-weight search over **fault configurations** (one Pauli per location,
Definition 5.1′, with a system-of-distinct-representatives test enforcing distinct locations).
(B) a **one-round program**: extracts `(E, s, u, λ)` per elementary fault by a *single*-round
simulation, then decides `d_circ` from `(LIFT')` alone inside a window `W`, and computes
`repair(γ)` from Definition 5.2. (B) never calls (A).

**Calibration on a campaign instance.** Steane `[[7,1,3]]`, list-scheduled non-interleaved:
`d_circ = 2` at `R = 2,3` by (A), and `2` by (B) — reproducing the d3-gate table, iff §9.4 and
wave-17's independent reproduction under a third independently written detector layer.

**Fresh families, chosen to be disjoint from every prior sweep.** Prior reviewers used `chain_m`
(`Q_m`), `cyc3/cyc4`, `rand00–39`, block-graph codes on stars/trees/theta/kite, weight-4 block
codes, random asymmetric `n = 9…12`, and the campaign codes (Steane, rotated surface, `[[4,2,2]]`,
gross). **I used hypergraph-product codes** `HGP(H₁,H₂)` built from small classical codes, **and
rectangular Shor codes** `a × b`. Neither family appears anywhere in the circdist record. Headline
instance: `HGP(pair, rep3)` = `[[8,1,·]]`, `𝒜 = {036, 1467, 257}`, `ℬ = {016, 127, 346, 457}`,
`k = 1`, `d_X = 3`, `d_Z = 2`, `d = 2` — with a CNOT order under which the Z-memory sector is
**graph-like** (Def. 1.12: **0 violations / 163 elementary faults**) and (MC) holds, so it lies
squarely inside the node claim's own scope, in both non-interleaved orders and in a genuinely
interleaved (MC)-passing schedule.

**Main sweep** — 139 `(code, CNOT-order, schedule, sector)` instances, all (MC), both sectors
(X-memory via the `𝒜 ↔ ℬ` mirror), exhaustive ground truth at `R = 2,3,4`:

```
instances ................................................. 139     graph-like ............. 113
asymmetric (d_sec != d) ................................... 68
VIOLATIONS of the ceiling d_circ <= d_sec .................. 0
Lemma A construction failures (|F*| = d_sec, undetectable) . 0
instances where the OLD constant d fails (d_circ > d) ...... 49
d_R non-monotone in R ..................................... 0
model fact (V) violations ................................. 0 / 139
conjunct-1 sandwich locates d_circ ........................ 139 / 139
conjunct-2 biconditional .................................. 139 / 139
Lemma C at W = d_sec vs direct ground truth ............... 139 / 139 agree
5.10(2) as originally stated (W = d) ...................... wrong on 49
```

**Further instances.** (i) **42** HGP/rect-Shor instances, both non-interleaved orders, both
sectors, exact `d_circ`: 29 graph-like, **0 ceiling violations**, **14** further old-constant
failures, Lemma C at `W = d_sec` agrees **42/42**. (ii) **221** interleaved (MC) instances, exact
`d_circ`: **0 ceiling violations**, biconditional **221/221**, sandwich **221/221**. (iii) **70**
random-time-slot interleaved (MC) instances and **1 530** Steane offset-family (MC) schedules, used
for the `repair` census only (every one had a minimum-weight `γ` with `repair = 0`, which is why the
hill-climb of §3.2 was needed). Grand total with exact `d_circ` measured: **405**, ceiling
violations **0**.

**The `(false,false)` side of conjunct 2**, reached by hill-climb (3 instances, Steane interleaved,
(MC), not graph-like):

```
steane/IL/s43363053   d_eff = 2   min-weight repair = 1   d_circ (direct) = 3   biconditional HOLDS
steane/RND/s95861351  d_eff = 2   min-weight repair = 1   d_circ (direct) = 3   biconditional HOLDS
steane/RND/s3469477   d_eff = 2   min-weight repair = 1   d_circ (direct) = 3   biconditional HOLDS
```

and on all three `d_circ = |γ| + repair(γ)` exactly — Theorem 5.6(c) at `repair = 1`.

**Model layer, re-derived from my own simulator** (124 (MC) instances, five codes):

```
1.13 residual inventory (E empty / singleton / X-check suffix) ....  18 126 checked, 0 violations
(V)  U(empty) subset {0} u {e_b} .................................    5 932 checked, 0 violations
1.11 time locality   d(f,r) = [u]_r + [u+s]_{r+1} ................   54 378 checked, 0 violations
1.9  sector decoupling, FULL symplectic (x,z) simulator, all 15
     two-qubit Paulis + both detector families + both meas-flip
     types: Z-check detectors and observables depend only on the
     x-part, X-check detectors only on the z-part ................   35 292 checked, 0 violations
```

`(V)` and 1.9 are the two inputs the node's `assumptions` block and §7.3 call load-bearing; both are
now re-derived independently of the base review's 440/440.

---

## 6. Coverage table — every load-bearing input, and who established it

"**RE-DERIVED HERE**" means I reproduced the argument and/or measured it myself this session.

| load-bearing input | prior independent verdict (object unchanged since) | this review |
|---|---|---|
| (MC) ⟺ deterministic detectors (2.2) | base review verdict **B** CONFIRM [V][D], re-derived pre-reading | implemented and enforced on every instance |
| 1.9 sector decoupling | base review §4.7 CONFIRM (full two-sector search) | **RE-DERIVED HERE**, 35 292 full-Pauli checks |
| 1.11 time locality (∂) | base review (used throughout) | **RE-DERIVED HERE**, 54 378 checks |
| 1.13 residual inventory `ℰ` | base review §4.2, 1 994/1 994 | **RE-DERIVED HERE**, 18 126 checks |
| model fact **(V)** | base review §4.2, structural + 440/440 | **RE-DERIVED HERE**, 5 932 checks |
| 4.1 no temporal-boundary correction | base review verdict **J** CONFIRM [D][N] | corroborated: (LIFT')-only and direct pipelines agree 139/139 |
| 4.2 / 4.3 (LIFT), (LIFT′) | base review §§4.3–4.4, re-derived line by line | **RE-DERIVED HERE** as a separate program |
| 5.4(1) `λ_circ = λ_eff ∘ π₁` (systole hazard) | base review §4.3 item 1 — "Correct" | re-derived; used in H1 |
| 5.4(2)(3)(4) weight accounting | base review verdict **E** CONFIRM [D][N] | carried; its consequence (the sandwich) measured 139/139 |
| Def 5.1′ per-location weight | base review verdict **M** CONFIRM | implemented exactly (SDR test) |
| 5.3′ branch (a) at min weight (Amd 2 L1) | Amendment-2 completion review — CLEAN-PASS | **RE-DERIVED HERE**, plus hole **H3** filled |
| 5.6(a) | base review **E**/**G** neighbourhood; amendments2 assembled | **RE-DERIVED HERE**, plus hole **H1** filled |
| 5.7 the biconditional | base review verdict **G** CONFIRM [D][N], 282/282; wave-17 reproduced both sides | **RE-DERIVED HERE**; 430 instances + 3 on the `(false,false)` side |
| 5.9 contiguity, `span ≤ weight` | base review verdict **H** CONFIRM [V][D][N], 203 186/203 186 | re-derived; used in H2/H4 |
| Lemma A (`d_circ ≤ d_sec`), crossed pairing | wave-23 §3.1 CONFIRM, 128/128 | **RE-DERIVED HERE**; construction verified 139/139 |
| Lemma B (constancy) **as repaired by A4-R1** | wave-23 §3.7 found the defect and verified the repair | **RE-DERIVED HERE** step by step; A4-R1 verified at source; hole **H2** filled |
| Lemma B′ (whole-circuit `d`) | wave-23 §3.2 CONFIRM | carried; consistency with A4-R2's new block checked |
| Lemma C (replaces 5.10(2)) | wave-17 §4.4 CONFIRM-WITH-REQUIRED-REPAIR (mechanism); wave-23 CONFIRM (constant) | **RE-DERIVED HERE**; 139/139 at `W = d_sec`, old constant wrong on 49 |
| 5.6′/5.7′ (`R ≥ d_sec`) | wave-23 §3.3 CONFIRM, band closed twice | **RE-DERIVED HERE**, both closure routes |
| Prop. D tightness (`d_circ − d` unbounded) | wave-23 §3.4 CONFIRM, extended to `m = 6` | not re-verified — **carried**; not a premise of any conjunct |
| 5.10(3) finiteness corner | base review §5 item 4: "not used by (a)–(d)" | **RE-DERIVED HERE** why it is not a premise (H4) |

Nothing on this table is now resting on an unreviewed step.

---

## 7. Composition audit — do Amendments 1–4 apply cleanly, in order?

**7.1 Quotation mechanics, checked at byte level.** I normalised blockquote markers and whitespace
and searched every `Old` quotation in its named source:

```
Amendment 3 section 3 "Old" quotations ......... 17 found, 17 locatable, each exactly once
Amendment 4 A4-R1 Old in Amendment 3 ........... exactly 1 occurrence   (516 chars)
Amendment 4 A4-R2 Old in Amendment 1 ........... exactly 1 occurrence   (525 chars)
Amendment 4 A4-R3 Old in Amendment 3 ........... exactly 1 occurrence   (132 chars)
```

My independent census is **17**, confirming wave-23 and confirming that A4-R3's 15→17 correction is
right. The composition is therefore *unambiguous*: each edit has one and only one target.

**7.2 The A4-R2 absorption is sound — and it repairs a defect nobody had named.** Amendment 2 §3.2
instructs an edit to Amendment 1 §3.4's `R_sat` sub-clause and quotes its target in **ASCII
transliteration** (`R_sat(M) <= d` iff `d_infty(M) = d`), whereas Amendment 1's bytes are Unicode
(`R_sat(M) ≤ d` **iff** `d_∞(M) = d`). I measured it: **Amendment 2 §3.2's `Old` string occurs 0
times in Amendment 1.** As a byte-exact edit instruction it was *never executable*, from the day it
landed. A4-R2 resolves this correctly and in the only sound way: its `Old` is Amendment 1's **actual
bytes** (verified unique), and its `New` **carries** the `R_sat(M) = 1` form, so L2's content
survives by absorption rather than by an instruction that could not fire. I verified the new block
carries **both** constants on their correct readings — `d_sec` per sector, `d` whole-circuit for the
`R_sat` dichotomy — and confirm Amendment 4's point that a blanket `d → d_sec` would have broken the
dichotomy. Consequence for ordering: the composition must be read as *edits against the frozen
originals*, with Amendment 2 §3.2 a no-op discharged by A4-R2. Read that way, **Amendments 1–4
compose cleanly and in order, with no contradiction between amended passages.**

**7.3 No refuted text left standing.** Searching for the refuted per-sector form "per sector, `d_R`
is constant for `R ≥ d`": **1 live occurrence** (Amendment 1 §3.4 — exactly the block A4-R2
replaces), **0 elsewhere** in the base proof or Amendments 2/3 (Amendment 4's three hits are inside
its own quotation and discussion of it). Amendment 4's dependent-passage claim is exact.

**7.4 The §7.1 status table, as amended by R12, matches reality.** I checked each row against the
derivation it summarises. The Lemma A row's inputs ((CSS), legality, ideal *terminal* readout, no
(MC), no graph-likeness, no (V)) are exactly what Lemma A's proof uses — I confirmed by re-deriving
it. Two notes, neither a defect: the table has **no column for 1.9**, which Lemma A does use (for
"no X-check detector fires"); and the `(V) ✓` mark on the "5.6(a)/5.7" row is **conservative** —
neither 5.6(a) nor 5.7 actually needs (V) (in (⟹), `n_∅ = 0` forces `A_∅ = 0` outright; in (⟸) with
`repair = 0` no measurement flips are added). Over-attributing an established model fact is the safe
direction, so I flag it as an accuracy note, not a repair.

---

## 8. Caveat audit — what survives a `PROVED` promotion, and what must go

### 8.1 The wave-23 deciding caveat is **DISCHARGEABLE**. Verified at source.

Caveat 1 names two Amendment-3 defects plus a quotation-count erratum, and states that PROVED
additionally needs a claim-level end-to-end pass. All four items are now closed:

| item | status |
|---|---|
| (a) Lemma B §2.3 inequality backwards | **discharged** — A4-R1; `Old` unique, `New` correct, chain re-derived by me (§3.1, H2) |
| (b) R9's stale §8-item-4 block | **discharged** — A4-R2; `Old` unique, `New` carries both constants, absorption sound, no other live occurrence (§7.2, §7.3) |
| (c) 15 vs 17 quotation count | **discharged** — A4-R3; my independent census says 17 |
| (d) "PROVED needs a claim-level end-to-end pass" | **discharged by this document** |

Caveat 1 must be **retired to an event**, not carried.

### 8.2 Caveats that survive as honest scope notes (all of them)

* **Per-sector scope.** Survives verbatim; it is also now *in the claim*, via `d_sec`.
* **`repair ≥ 3` exclusion** (adjudicated wave 16). Survives verbatim. I re-checked the adjudication
  against the wording: conjunct 1 is 5.6(a) with no repair term; conjunct 2's (⟹) needs no repair
  hypothesis and its (⟸) uses only `min(repair,2) ≥ 1`; conjunct 3's voltage is Definition 5.2 data
  with Lemma C repair-free. The exclusion is a boundary of the claim, not a conditionality inside it.
* **The `d_X ≠ d_Z` sweep record.** Survives, and should be updated: it is now **triply** swept —
  194 (wave 22) + 128 (wave 23) + **405 (this review, on two families no prior sweep touched)**,
  with **0** ceiling violations in all three and the old constant failing on **63** of mine
  (49 + 14).
* **Large proposer scans not independently reproduced.** Survives verbatim; I reproduced none of
  them either. They are corroboration, not premises, so they do not obstruct `PROVED`.
* **5.6(d) unreviewed but not a premise.** Survives; re-confirmed — no conjunct cites 5.6(d).
* **Certification is for the exact current claim.** Survives; strengthened by the hash binding here.
* **Model fact (V) registered in `assumptions`.** Survives as a pointer, now with a second
  independent establishment (§5). Protocol §2 permits a node-level `assumptions` block on a
  route-free direct-proof node, so the registration is well-formed.

### 8.3 Caveats that must be **added**

1. **Shared model design is not independence.** Base review §5 item 2 says this of itself; it is
   equally true of me. My simulator re-implements Definition 1.8's *design* — which locations exist
   and which Paulis are available — so a systematic mismatch between the frozen 公共定义 and a real
   compiler (`stim`) would survive all three independent implementations. **I ran no `stim`
   cross-check.** This should be a standing caveat on the node; it is a limitation of the whole
   campaign, not a defect of this argument.
2. **The dossier is a five-file append-only composition, not a consolidated document.** The
   argument that this review certifies is base + A1 + A2 + A3 + A4 read as edits against the frozen
   originals, with Amendment 2 §3.2 a discharged no-op. That composition is byte-verified here, but
   no single readable document states the proved theorem. Recommended (non-blocking): a
   consolidation pass.

### 8.4 Two defects in the canonical record — dispatcher-executable, no new mathematics

**D1 (must fix at promotion).** `assessment.summary` still asserts the **refuted** per-sector form:
"the CONTIGUITY THEOREM (min-weight undetectable logicals occupy contiguous rounds with span <=
weight <= **d**)". Amendment 3 §4 flagged this as dependent-passage item 2 and no wave has executed
it. It must read `span <= weight <= d_sec` per sector. In the same sentence, "together with
monotonicity and `d_R<=d`, Amendment 2 gives the exact `R_sat` dichotomy" is correct **only** under
the whole-circuit reading (Lemma B′) and must say so. A node whose summary asserts a refuted
statement cannot carry `PROVED`.

**D2 (must fix at promotion).** `basis.evidence` is incomplete: the live dossier is base + A1 + A2 +
A3 + A4, but evidence links only the base proof and Amendment 3. **Amendments 1, 2 and 4** are
linked nowhere in the basis (A4 appears only inside an event summary), and so are the **wave-16
scope adjudication** and the **Amendment-1 focused re-review**. Under protocol §5 item 4 an auditor
starting at this node cannot reconstruct the argument. All five must be added to `basis.evidence`.

---

## 9. Verdict

> ### **PROVED-QUALIFIES**, conditional on the two mechanical record repairs D1 and D2.

Under `DAG_PROTOCOL.md` §3, `PROVED` requires *"a complete argument and all load-bearing inputs
passed independent adversarial review."*

* **Complete argument:** yes, for the exact claim at
  `sha256:0c4c466b895d938d2028140967d87974ee2216b3cebcc48967804f530e227240`. All three conjuncts
  hold as worded against the amended composition (§3). The four unstated steps H1–H4 are filled in
  §4 and are now part of the record. Wave-23's ground 1 (Lemma B) and ground 2 (R9's live refuted
  text) are discharged by Amendment 4, verified at source here.
* **All load-bearing inputs independently reviewed:** yes (§6). Wave-23's ground 3 was the absence
  of an assembled-argument reviewer; this document is that reviewer, and it re-derives or re-measures
  every row rather than inheriting it.
* **Amendment 4 was unreviewed:** it is reviewed here — all three repairs verified at source,
  including its self-flagged DEVIATION, which I judge **correctly handled**: A4-R1 is a derivation
  repair with no numerical consequence, and reporting the 148 clean instances as if they
  discriminated would have been the dishonest move.

I found **no defect that refutes any conjunct** and **no defect requiring new mathematics**. D1 and
D2 are canonical-record repairs a dispatcher executes in minutes; they are pre-conditions of the
promotion, not blockers of the argument. If the dispatcher declines to execute them, the correct
level is **STAYS-CERTIFIED\*** with D1 as the deciding conditionality (a summary asserting a refuted
statement).

**Surviving caveat set for the promoted node** (7 items): per-sector scope; the `repair ≥ 3`
exclusion and its min-cost-covering extension; the triple `d_X ≠ d_Z` sweep record; large proposer
scans not independently reproduced; 5.6(d) unreviewed and not a premise; model fact (V) registered
in `assumptions`; **plus the two new ones of §8.3** — shared model design is not independence (no
`stim` cross-check anywhere in the campaign), and the dossier is a five-file append-only composition.
Caveat 1 (the wave-23 deciding conditionality) is **retired** to an event.

**Basis restructuring I license.**

| action | object |
|---|---|
| **add** `basis.reviews` | this document, `kind: review`, `reviewed_hash: sha256:0c4c466b…`, scope = assembled-argument end-to-end pass over base + Amendments 1–4 |
| **keep** `basis.reviews` | `circdist_iff_amendment3_review_20260823.md` at `sha256:0c4c466b…` — still valid and still hash-bound |
| **add** `basis.evidence` | `circdist_lift_iff_amendment1_20260820.md`, `…amendment2_20260820.md`, `…amendment4_20260823.md`, `circdist_iff_scope_adjudication_20260823.md`, `circdist_amendments_review_20260820.md` |
| **no demotions** | nothing currently linked lapses; the two demotions wave-23 prescribed were executed at the `d_sec` re-bind |
| **frontier** | `task-007` **discharged in full** (item 1 by Amendment 4, item 2 by this review); `task-006` and `task-003` unchanged |

I promote nothing. The dispatcher executes.

---

## 10. Limitations — what I did not do

1. **Instance size.** `n ≤ 12`, `|ℬ| ≤ 6`, `R ≤ 4`, exhaustive `d_circ` search capped at weight 4.
   No campaign-scale instance (gross `[[144,12,12]]`, rotated surface at scale) was measured. My
   `d_sec` margins reach `d_sec − d = 2`; wave 23 reached 4.
2. **The `repair ≥ 3` regime was never entered** — by anyone, in this campaign. It is excluded from
   the claim, and nothing here changes that.
3. **`(false,false)`-side coverage is thin: 3 instances**, all Steane, all non-graph-like. My
   graph-like instances all had `repair ≡ 0`, so the biconditional's refuting direction is exercised
   *inside the claim's graph-like scope* only through prior work (base review 282/282, wave-17's
   `M_IL`/`M_NI` pair), not through mine.
4. **No `stim` cross-validation** (§8.3 item 1). My independence is of *implementation*, not of
   *model design*.
5. **Proposition D (tightness) and the `CIRCDIST.sat` cross-node flag were not re-verified**; I
   carry wave-23 on both. Neither is a premise of any conjunct.
6. **I did not re-verify Amendment 3's R1–R12 `New` texts against the mathematics** one by one;
   wave-23 did that, and I verified only that the 17 `Old` anchors are unique and locatable.
7. **I did not review the root node** `CIRCDIST.lift`, its folded claim, or its blockers S1/S2.
8. **This review is itself unreviewed.** It is one session's work, and §4's four fills are mine
   alone — they have had no adversary.
