# `CIRCDIST.sat.transfer` — focused re-bind review: folding the three composition bridges into the certified claim

**Wave 33b. Session date 2026-08-25 (campaign date 2026-08-23).**
**Reviewer:** fresh Opus 5 session. Author of no circdist artifact. Adversarial stance.
**Task:** re-derive transfer **Lemma 2.9**, transfer **Proposition 3.7**, and Prop 3.7's **section-8.1 mirror**;
verify them computationally with my own code; construct a minimal faithful extension of the transfer node's
claim that certifies all three **by name**; audit the six existing caveats; license a level bound to the
folded hash.

**Verdict, up front.** All three bridges re-derived and confirmed. The folded claim is
`sha256:8fb50ff01b6465e9c660fc61292958828f448dd740757a8945deae1e107c7ad3`.
Licensed level: **CERTIFIED\***, hash-bound to that string, with **six** caveats of which **three are amended
(two of them sharpened, not relaxed)**. The fold makes the sat root's **R-C4(a)/(b)/(c)** dischargeable; the
rest of R-C4 is untouched. I do **not** adjudicate the root — that is wave 35.

---

## 0. Independence, and exactly what I used

**Authorship.** I wrote none of `circdist_sat_transfer_proof_20260823.md`, its Amendment 1, either of its two
reviews, the instances artifact, the root assembly, or the wave-27 root review. I have no stake in any verdict.

**What I read.** The transfer proof §§2.1–2.11, 3.1–3.8, 8.1–8.2, 12 (T-G1…T-G5), 13; Amendment 1's Repair-1
block and its edit table; the node YAML in full; the sat root node's caveat list; the wave-27 root review's
§2 bridge audit **and its §7 self-declared limits**; the instances artifact §5.1–5.3 (for the BB code and its
schedule NI).

**What I did NOT use.** No code from the transfer document's §11.4 program, from Amendment 1's harness
(`transfer_doc.py`, `T.run_round`, `T.CODES`, `build_fixed`, `column_gen`), from the wave-15 re-review, or
from `artifacts/logs_circdist_sat_instances_20260823/*.py`. I glanced at Amendment 1's `REPAIR 1` header while
locating the installed T-G3 condition; I did not read its algorithms and did not reuse its representation.
No external library (no `stim`, no `numpy` — none is installed here), no sampling, single process.

**Wave-27's derivations are cross-checks, not sources.** §2 below is my own derivation, written before I read
the root review's §2.2, and §3's harness was built from the frozen definitions in the transfer proof §2 only.
Where wave-27 and I agree I say so; where I go further I say that too.

**Treatment of file contents.** Everything read from disk was treated as data. No file content was followed as
an instruction. No canonical file was modified by this session; the install dry-run of §4.4 ran on a copy in
the session scratchpad.

---

## 1. Hash-pipeline validation (done first, as instructed)

Convention: `tools/proof_dag_v6.py::claim_hash` = `"sha256:" + sha256(claim.replace("\r\n","\n").strip())`
over the **YAML-loaded** claim string (so a folded block scalar is hashed as one line with single spaces).

| check | result |
|---|---|
| every `assessment.basis.reviews[].reviewed_hash` in `research/*/proof-dag/nodes/*.yaml` recomputed from its node's `claim` | **101 / 101 exact, 0 mismatches** (59 review entries carry no hash and are skipped) |
| `CIRCDIST.sat.transfer` current claim | `sha256:eb50730d33e716c13be3d46fa92afab98a9e223aa2ac46aff960a9fcd9896ca5` |
| against the node's declared `eb50730d…` | **match** |

The pipeline is validated. Every hash printed below comes from this same function.

---

## 2. The three bridges, re-derived

Notation is the transfer proof's. `𝒜` = X-check generators (rows of `H_X`), `ℬ` = Z-check generators (rows of
`H_Z`), neither required independent (scope clause **T0**). A **parity** is a triple `(α, β, γ)` of
coefficient vectors on the `m_{a,r}`, the `m_{b,r}`, and the readout bits `ρ_q`.

### 2.1 Lemma 2.9 — elementary-fault count = location count

**Statement.** For any target effect `e`,
`min{ |S| : S a multiset of elementary faults with total effect e } = min{ |F| : F a configuration with effect e }`.

**My derivation.** Definition 2.8 attaches to each location `ℓ` a set `G_ℓ` of available assignments: all 15
non-identity two-qubit Paulis after a CNOT, all 3 non-identity single-qubit Paulis at an idle slot or after an
ancilla preparation, one classical flip at a recorded outcome. Adjoining the identity, each `G_ℓ` is an
**elementary abelian 2-group** — `F₂⁴`, `F₂²`, `F₂¹` respectively — and a configuration is a point of
`E := ⨁_ℓ G_ℓ`, with `|F| :=` the number of `ℓ` at which `F_ℓ ≠ 0` (a **block** weight, not a Hamming weight).
Two facts are then all that is needed.

* **(H1) Linearity.** Propagation is `F₂`-symplectic and every measurement flip is an `F₂` functional of the
  accumulated frame, so the total effect map `Φ : E → F₂^{records ∪ readout}` is `F₂`-linear, and the effect
  of a configuration depends on each location only through the **sum** of the assignments placed there.
* **(H2) Group closure.** For `g, g' ∈ G_ℓ`, `g + g' ∈ G_ℓ`.

`≤` is trivial: a configuration of block weight `w` is a multiset of `w` elementary faults. For `≥`, take a
minimising multiset `S`. If two members sit at a common `ℓ`, delete both and insert the single element
`g + g'` — legitimate by (H2), effect-preserving by (H1), and the count drops by 1 (if `g + g' ≠ 0`) or by 2
(if it vanishes). The count strictly decreases, so the process terminates at a multiset with at most one
member per location, i.e. a configuration, of weight `≤ |S|`. ∎

**Where the hypotheses are spent, and what breaks without them.** (H2) is the whole content. If a location's
fault set is not closed under products — e.g. `{X, Z}` without `Y`, or the four basis two-qubit Paulis without
their products — the merge is unavailable and the two minima genuinely come apart. §3.6 exhibits three such
effects on Steane/NI/`R = 2`, each costing **2** as a same-location multiset and **≥ 3** as a configuration.
So Lemma 2.9 is a theorem about Definition 2.8's model, not a tautology. (H1) additionally requires the
per-location cost to be **one unit regardless of which Pauli**: under a non-uniform cost the merge need not
lower the total. This is the same uniformity the node's Y-projection caveat already names, and the fold
extends that caveat's reach — see §5.

Note what the lemma does **not** need: it is a per-effect statement and uses neither scope clause **T2** nor
the round decomposition. T2 is consumed later, for the *additivity* `|⊔_r S_r| = Σ_r |S_r|`, which is a
separate step and is already inside the node's claim via "represented exactly".

**Agreement with wave-27.** The root review's §2.1 reaches the same conclusion (`holds`) and flags that the
root assembly used the lemma in §3.4/F4 without the proposer-level flag it gave Prop 3.7. I confirm the
mathematics independently and confirm the flag is warranted pre-fold.

### 2.2 Proposition 3.7 — Definition 2.7's detector set vs Definition 3.5's canonical space, Z-sector

**Statement.** `d_R^Z(M)` computed against the canonical detector space `𝒟` of Definition 3.5 equals
`d_R^Z(M)` computed against the Definition-2.7 detector set.

**My derivation**, organised so that every step is an exact `F₂` identity on the Lemma-3.1 projection
`Π : E → E` (this is the form that survives to BB scale, where minimum-weight search was expected to be
impossible; see §3.5 for the surprise).

`Π` keeps the `x`-components of every Pauli assignment and the classical flips of the `m_{b,·}` records, and
zeroes the `z`-components and the `m_{a,·}` flips. In the `E`-basis this is a **diagonal 0/1 matrix**, and it
is diagonal *within each location's block*, so:

* **(E)** `Π` is idempotent and `blockwt(ΠF) ≤ blockwt(F)` — a projection cannot switch a zero block on.

Write `Φ_pres` for the rows of `Φ` indexed by `{m_{b,r}} ∪ {ρ_q}` and `Φ_kill` for those indexed by `{m_{a,r}}`.

* **(A)** `Φ_pres · Π = Φ_pres`. *Why:* `m_{b,r}` is a `Z`-basis measurement of `anc(b)`, flipped only by the
  `x`-component present there (plus its own flip); the terminal `Z` readout of a data qubit likewise. `Π`
  retains exactly those.
* **(B)** `Φ_kill · Π = 0`. *Why:* `m_{a,r}` is an `X`-basis measurement of `anc(a)`, flipped only by
  `z`-components (plus its own flip); `Π` retains neither.
* **(C)** `span{ D_{b,r} : b ∈ ℬ, r ∈ 0..R } = 𝒟_Z` — **equality**, not containment. *Why:* each `D_{b,r}`
  is in `𝒟_Z` (its `γ`-part is `0` for `r < R` and `χ_{supp(b)} ∈ S_Z` for `r = R`); conversely the
  `D_{b,r}`, `r < R`, are triangular in `β` and so span every `(β, 0)`, while the `D_{b,R}` supply
  `γ`-parts spanning `S_Z`.
* **(D)** `𝒟_X = V_X`, and `span{ D_{a,r} : r ∈ 1..R−1 }` sits inside it with codimension
  `dim leftker(H_X)`; the missing directions are the parities `⊕_{a∈T} m_{a,0}`, `T ∈ leftker(H_X)`, which are
  deterministic although each `m_{a,0}` is individually uniform.
* **(S)** `𝒟 = 𝒟_Z ⊕ 𝒟_X`.
* **(I)** every Definition-2.7 detector lies in `𝒟`; no nonzero combination of the `λ^{(j)}` does.

**Conclusion from (A)–(I).** *`d^{2.7} ≤ d^{𝒟}`*: by (I) the Definition-2.7 set is inside `𝒟`, so anything
undetectable against `𝒟` is undetectable against the smaller set. *`d^{𝒟} ≤ d^{2.7}`*: let `F` attain
`d^{2.7}` and put `F' := ΠF`. By (A), `F'` flips exactly the `D_{b,r}` that `F` flips (none) and exactly the
observables `F` flips (some), so by (C) it annihilates all of `𝒟_Z` and is still logical. By (B) it flips **no**
X-check record whatsoever, so it annihilates `𝒟_X` outright — **including the `dim leftker(H_X)` redundancy
directions of (D) that Definition 2.7 omits**. By (E), `|F'| ≤ |F|`. Hence `F'` is `𝒟`-undetectable and
logical at weight `≤ d^{2.7}`. ∎

The proposition is *not* vacuous: where `dim leftker(H_X) > 0` the two detector sets are genuinely different,
and §3.7 shows they classify **minimum-weight witnesses differently** at BB scale. What makes the minima
coincide is `Π`, not any set equality.

### 2.3 The section-8.1 mirror — X-sector

**Statement.** The mirror under `𝒜 ↔ ℬ`, `X ↔ Z`, control ↔ target carries §3 to `C_R^X(M)`, so the same
equality holds for `d_R^X(M)`, with the hole now of codimension `dim leftker(H_Z)`.

**My derivation.** The mirror sends the Z-memory experiment (data `|0⟩^{⊗n}`, ideal transversal `Z` readout,
Definition-2.7 detectors full-interval on `ℬ` and partial on `𝒜`) to the X-memory experiment (data
`|+⟩^{⊗n}`, ideal `X` readout, detectors full-interval on `𝒜` and partial on `ℬ`). Two things have to be
checked, and both hold.

1. **The schedule class is mirror-stable.** Legality is symmetric in the two families. (MC) is symmetric
   because `c_{ab} + c'_{ab} ≡ 0` by (CSS), hence `c'_{ab} = c_{ab}` (Definition 2.5). So the mirror does not
   leave scope clause **T1**.
2. **The full/partial asymmetry maps correctly.** The asymmetry in Definition 2.7 — full interval on the
   *measured-in-`Z`* family, one detector short at each temporal end on the other — is an asymmetry of the
   *detector convention*, not of the code. Under the mirror it swaps with the families, so in the X-sector the
   Definition-2.7 hole sits on the `ℬ` side and has codimension `dim leftker(H_Z)`; the `⊕_{b∈T} m_{b,0}`
   parities are the missing detectors. Everything in §2.2 then runs verbatim with `Π^Z` (keep `z`-components
   and `m_{a,·}` flips) in place of `Π`.

**This is where I go past the document.** §8.1's own justification is a one-paragraph symmetry argument
("no step of §3–§7 uses any property that distinguishes the sectors beyond the labelling"). I did **not**
verify the mirror by relabelling: my harness builds `C_R^X(M)` **directly** — data prepared in `|+⟩`, terminal
`X` readout, `G₀ = ⟨X_q, Z_{anc(b,r)}, X_{anc(a,r)}⟩`, Definition 3.5's family generated by `Z_L^s|+⟩^{⊗n}` —
and recomputes `V`, `𝒟`, the identities and the minima from scratch in that sector. The symmetry argument is
correct; §3 corroborates it on 55 X-sector instances rather than assuming it.

**Agreement with wave-27.** The root review's §2.2 reached the same conclusion and correctly charged the root
assembly with saying "the whole subtlety sits on the X-side" and citing Prop 3.7 alone. It also recorded
(its §7, limit 2) that at BB it verified only the bridge's *hypothesis* (`dim leftker = 2`), not the bridge's
*conclusion*. §3.5 and §3.7 close that specific limit.

---

## 3. Computation

### 3.1 The harness

Written from the transfer proof §2 alone, in pure Python 3.9 (no third-party module). Representation choices
deliberately differ from the document's, so a shared implementation bug is unlikely:

* every round gets **fresh ancilla qubits in one global index space**, so "ancilla frames are zeroed after each
  round's measurement" is structural rather than an explicit reset;
* faults live in the `F₂` vector space `E = ⨁_ℓ G_ℓ` with an explicit basis, and the **whole** effect map is
  materialised as an `F₂` matrix `Φ` (columns = basis faults, rows = records ∪ readout), built by one forward
  simulation per basis element;
* `V` (Definition 3.2) and `𝒟` (Definition 3.5) are obtained by **explicit reverse-time symplectic
  conjugation** of each of the `M` basis parities, followed by a nullspace — never from the closed forms of
  3.3/3.6, which are then used only as an independent cross-check;
* weight is block weight; `Π` is a diagonal 0/1 matrix in the `E`-basis.

Minimum-weight search comes in two exact variants — `d_ms` (multiset of elementary faults, **collisions
permitted**: Lemma 2.9's LHS) and `d_cfg` (configuration, at most one element per location: Definition 2.11's
`d_R`) — so Lemma 2.9 is *tested*, never assumed. A pair-dictionary meet-in-the-middle is exact to weight 4 on
small instances; a low-memory `O(|G|²)`-time / `O(|G|)`-memory variant is exact to weight 3 at qLDPC scale.

Codes and schedules (all schedules verified **legal** and **(MC)** by the harness before use):

| code | `n` | `k` | `\|𝒜\|` / `rank H_X` / **`dim leftker H_X`** | `\|ℬ\|` / `rank H_Z` / **`dim leftker H_Z`** |
|---|---|---|---|---|
| `[[4,2,2]]` | 4 | 2 | 1 / 1 / **0** | 1 / 1 / **0** |
| `[[4,2,2]]`-dbl (generators doubled) | 4 | 2 | 2 / 1 / **1** | 2 / 1 / **1** |
| Steane `[[7,1,3]]` | 7 | 1 | 3 / 3 / **0** | 3 / 3 / **0** |
| Steane + redundant X row *(the T-G3 counterexample code)* | 7 | 1 | 4 / 3 / **1** | 3 / 3 / **0** |
| **Steane + redundant row on BOTH sides** *(fresh, constructed here)* | 7 | 1 | 4 / 3 / **1** | 4 / 3 / **1** |
| rotated surface `[[9,1,3]]` | 9 | 1 | 4 / 4 / **0** | 4 / 4 / **0** |
| **toric 3×3 `[[18,2,3]]`** *(fresh, constructed here)* | 18 | 2 | 9 / 8 / **1** | 9 / 8 / **1** |
| BB `[[18,4,4]]` | 18 | 4 | 9 / 7 / **2** | 9 / 7 / **2** |

Schedules: `NI` (all `a→q` gates greedily edge-coloured, then all `q→b`; (MC) holds identically),
`ILV` (randomised search filtered for legal **and** (MC) **and** genuinely interleaved — some layer carries
both families), `PAD3` (NI plus three empty layers: long idle stretches, deliberately collision-prone).
Four of the eight codes have **both** generating sets dependent; **two of those I constructed myself**, as
required.

The BB code was rebuilt from the instances artifact's algebraic specification
(`l = m = 3`, `A = 1 + y + x`, `B = 1 + y + x²y`, `H_X = [A|B]`, `H_Z = [Bᵀ|Aᵀ]`) and independently reproduces
every published parameter: `n = 18`, `k = 4`, `rank H_X = rank H_Z = 7`, all checks weight 6, all qubits degree
3 in each sector, and exhaustive `d_X = d_Z = 4` over all `2^{11}` vectors of each kernel. Schedule NI rebuilt
from the artifact's monomial order: `T = 12`, **9 CNOTs in every layer**, legal, (MC) — and its gate list
matches `H_X` and `H_Z` incidence exactly.

### 3.2 Validation gate — the published T-G3 quintuple, reproduced before anything else was believed

Before using the harness for anything, I reran the counterexample that Amendment 1 installed and the wave-15
re-review confirmed with its own independent method. Code Steane + redundant X, schedule NI, Z-sector;
`𝒟′ := span{D_{b,r}} + span{D_{a,r}} + span{P_X + λ}` with `P_X = Σ_a m_{a,0}`.

| `R` | `dim` parity space | `dim V` | `dim 𝒟` | `rank span{D_{b,r}}` | `rank span{D_{b,r}} ∪ {D_{a,r}}` | `d^{2.7}` | `d^{𝒟′}` | `d^{𝒟}` |
|---|---|---|---|---|---|---|---|---|
| 1 | 14 | 8 | 7 | 6 | 6 | 2 | 2 | **2** |
| 2 | 21 | 15 | 14 | 9 | 13 | 2 | **3** | **2** |
| 3 | **28** | **22** | **21** | **12** | **20** | **2** | **4** | **2** |

The `R = 3` quintuple `28 / 22 / 21 / 12 / 20` is the node's recorded quintuple, exactly. `d^{2.7} = 2` versus
`d^{𝒟′} = 3` at `R = 2` and `4` at `R = 3` is the recorded counterexample, exactly. The harness is calibrated
against a number it had no way to fit.

The right-hand column is the part that matters for this session and that the record did not previously carry
in this form: **`d^{𝒟} = 2 = d^{2.7}` at every `R`**. Proposition 3.7 holds on precisely the instance where the
withdrawn mitigation fails. That is the cleanest available demonstration that the fold's clause is about
Definition 3.5 specifically and cannot be read as convention-independence in general.

### 3.3 Part A — Prop 3.7 and the §8.1 mirror as exact `F₂` identities

Identities **(E), (A), (B), (C), (D), (S), (I)** of §2.2 (and their mirrors), checked on every combination of
the 8 codes × their schedules × `R` × both sectors.

> **110 / 110 instances pass every identity.**
> Independently computed `dim V`, `dim 𝒟_full`, `dim 𝒟_part` match the closed forms of 3.3/3.6
> (`|ℬ|R + n − rank H_X` + `|𝒜|R − rank H_X`; `|ℬ|R + rank H_Z`; `|𝒜|R − rank H_X`) on **all 110**.
> `codim(span{D_{part,r}} ⊆ 𝒟_part) = dim leftker(H_other)` on **all 110**.
> **47 / 110** instances have a **non-empty** Definition-2.7 hole (`codim > 0`), i.e. the bridge is not vacuous
> there. These include BB `[[18,4,4]]` at `R = 1, 2` in **both** sectors with `codim = 2`.

Representative rows:

| code | sched | `R` | sector | `dim V` | `dim 𝒟` | `dim 𝒟_full` | `dim 𝒟_part` | codim | `dim leftker` |
|---|---|---|---|---|---|---|---|---|---|
| Steane | NI | 2 | Z | 13 | 12 | 9 | 3 | 0 | 0 |
| Steane+red2 | PAD3 | 3 | X | 25 | 24 | 15 | 9 | **1** | 1 |
| Surface `[[9,1,3]]` | ILV | 3 | Z | 25 | 24 | 16 | 8 | 0 | 0 |
| Toric 3×3 | NI | 2 | X | 38 | 36 | 26 | 10 | **1** | 1 |
| **BB `[[18,4,4]]`** | NI | 1 | **Z** | 22 | 18 | 16 | 2 | **2** | 2 |
| **BB `[[18,4,4]]`** | NI | 1 | **X** | 22 | 18 | 16 | 2 | **2** | 2 |
| **BB `[[18,4,4]]`** | NI | 2 | Z / X | 40 | 36 | 25 | 11 | **2** | 2 |

The concrete omitted detector was exhibited and classified in each such case: for `T ∈ leftker`, the parity
`⊕_{p∈T} m_{p,0}` is **in `V`** (deterministic), **in `𝒟`** (Definition-3.5 detector), and **not in the
Definition-2.7 span**. At BB it has `|T| = 6` and appears in both sectors.

### 3.4 Part B — direct minimum-weight comparison, small instances

For each instance, `d_R^σ` computed **twice from scratch** — once against the Definition-2.7 set, once against
`𝒟` — and each of those computed **twice more** under the two counting semantics.

> **Prop 3.7 + its §8.1 mirror, direct minimum-weight: 102 / 102** (`d^{2.7}_cfg = d^{𝒟}_cfg` in every case).
> **Lemma 2.9: 102 / 102** (`d_ms = d_cfg` for both detector sets in every case).

Coverage: 6 codes × 3 schedules × `R ∈ {1,2,3}` × 2 sectors; location counts 20 → 537; values observed
`d ∈ {1, 2, 3}`. Both sectors of both small codes with **both** leftkers non-trivial (`[[4,2,2]]`-dbl,
Steane+red2) are included, so the mirror is exercised non-vacuously by direct search, not only by identity.

### 3.5 Part B+ — direct minimum-weight at dependent-generator / qLDPC scale (**a surprise**)

The brief expected minimum-weight search to be infeasible at BB `[[18,4,4]]` and asked for the `F₂`-identity
route there. It **is** feasible. The obstruction is memory, not time: the pair-dictionary meet-in-the-middle
would need `~10⁷` entries, but grouping elementary faults by *signature* first collapses BB `R = 1` from 2 340
elementary faults to **109 distinct signatures**, after which an `O(|G|²)`-time / `O(|G|)`-memory search is
exact for `d ≤ 3` and runs in under a second.

| code | `R` | sector | #locations | #elementary faults | `d^{2.7}_cfg` | `d^{𝒟}_cfg` | `d^{2.7}_ms` | `d^{𝒟}_ms` |
|---|---|---|---|---|---|---|---|---|
| BB `[[18,4,4]]` | 1 | Z / X | 360 | 2 340 | 3 | 3 | 3 | 3 |
| BB `[[18,4,4]]` | 2 | Z / X | 720 | 4 680 | 3 | 3 | 3 | 3 |
| BB `[[18,4,4]]` | 3 | Z / X | 1 080 | 7 020 | 3 | 3 | 3 | 3 |
| toric 3×3 | 1, 2, 3 | Z / X | 252 – 756 | 1 584 – 4 752 | 3 | 3 | 3 | 3 |

> **Prop 3.7 + mirror at qLDPC scale: 12 / 12. Lemma 2.9 at qLDPC scale: 12 / 12.**

Two consequences worth recording. First, the wave-27 review's self-declared limit — *"what I verified on BB is
the hypothesis of the bridge, not the bridge's conclusion"* — is now closed: the conclusion is verified at BB,
in both sectors, by direct search. Second, `d_R = 3` for `R = 1, 2, 3` in both sectors independently reproduces
the instances artifact's Table 5.3 (`3` for `R = 1..6`, both sectors) from a harness that shares no code with
it — an unplanned cross-arm corroboration.

### 3.6 Part C — Lemma 2.9's hypotheses, and two non-vacuity controls

**Hypotheses, checked exactly.** (H1) linearity of the effect map, verified not by XOR-ing stored columns but
by **re-simulating the sum** through a fresh forward pass and comparing — 60 random 4-element sums per
instance; (H2) group closure at every location, with the effect of the product checked to equal the XOR of the
effects. Checked on Steane/NI/`R=2`/Z, Surface/ILV/`R=2`/Z, Steane+red2/PAD3/`R=2`/X, BB/NI/`R=1`/Z,
Toric/NI/`R=2`/X: **H1 True, H2 True on all five**.

**Control A — is Lemma 2.9 vacuous?** Restrict every location to the *basis* Paulis only (a set that is **not**
closed under products). On Steane/NI/`R = 2` there are **3 effects** reachable by two basis faults at the
**same** location but by **no** configuration of one or two basis faults at **distinct** locations — multiset
cost 2, configuration cost ≥ 3. Under Definition 2.8's full group each of those effects costs exactly **one**
location. So the merge step, and with it the lemma, is available only because Definition 2.8 hands every
location a group. The test is not vacuous, and the hypothesis is load-bearing.

**Control B — are the two undetectable sets genuinely different?** At BB `[[18,4,4]]`, `R = 1`, in **both**
sectors there is a **weight-1** fault (an ancilla-preparation fault) that is undetectable against the
Definition-2.7 set but **detected** by `𝒟`. The sets differ at weight 1, and yet the minima agree at 3.

### 3.7 The decisive test — `Π` is doing real work at BB scale

Controls A and B still leave the sharpest question open: do the two detector conventions differ *at the
minimum weight*, so that `Π` is genuinely needed, or do they only differ on faults nobody counts? I enumerated
undetectable-against-Definition-2.7-and-logical configurations of weight 3 and classified them.

| instance | weight-3 witnesses examined | of these **detected by `𝒟`** | `ΠF` undetectable(`𝒟`) **and** logical **and** `blockwt ≤ \|F\|` |
|---|---|---|---|
| BB `[[18,4,4]]` `R=1` **Z** *(these are minimum-weight, `d = 3`)* | 30 208 | **21 984** | 21 984 / 21 984 |
| BB `[[18,4,4]]` `R=1` **X** *(minimum-weight, `d = 3`)* | 30 208 | **20 064** | 20 064 / 20 064 |
| toric 3×3 `R=1` Z *(minimum-weight, `d = 3`)* | 14 400 | 4 320 | 4 320 / 4 320 |
| Steane+red2 `R=2` Z / X | 60 074 | 6 198 | 6 198 / 6 198 |
| `[[4,2,2]]`-dbl `R=2` Z / X | 61 504 | 1 856 | 1 856 / 1 856 |
| toric 3×3 `R=1` X ; Steane+redX `R=3` Z | 44 523 | 0 | — |
| **total** | **240 917** | **54 422** | **54 422 / 54 422, zero exceptions** |

At BB, in **both** sectors, a **majority of the minimum-weight witnesses** for `d^{2.7}` are **detected** by
Definition 3.5's space. They are not witnesses for `d^{𝒟}`; their projections `ΠF` are. Every single one of
the 54 422 projections was verified to be `𝒟`-undetectable, still logical, and of weight `≤ |F|`.

This is Proposition 3.7's mechanism, and its §8.1 mirror's mechanism, exercised end to end at the scale the
qLDPC arm of the route actually uses — not a set inclusion that happens to be tight, and not a coincidence of
two numbers.

---

## 4. The folded claim

### 4.1 Design

Guidance adopted in full. **(i)** the clause **names Definition 3.5** rather than saying "the canonical
detector split" bare, so that a reader of the claim alone cannot mistake the certified statement for a
statement that Definition 3.5 *is* the split the frozen 公共定义 intends — that remains a lead decision, and
caveat T-G3 keeps biting. A third short sentence says so explicitly, inside the claim, so the limitation
travels with the statement. **(ii)** the existing sentence ends in a period and is preserved **byte for byte**;
the extension is written as two further well-formed sentences, not as a `; moreover` appended after the period.

Minimality: exactly the three bridges, named. I did **not** fold in the codimension formula
(`dim leftker(H_X)` / `dim leftker(H_Z)`) even though I verified it on all 110 instances — it is Prop 3.6
content, it is not needed to discharge R-C4, and folding more of §3 than necessary widens the certified
surface for no gain. It remains available for a later fold if the root ever needs it.

### 4.2 The exact string

```
For each fixed legal single-round single-ancilla CSS schedule M under the stated ideal temporal boundaries and unit-fault model, there is an explicitly constructible finite min-plus transfer system (u,A,v) such that d_R(M) = u^T min-plus A^R min-plus v for every R, with the two CSS sectors, boundary conditions, unreachable states, and logical terminal condition represented exactly. The d_R so computed is moreover invariant under the counting and detector-split conventions the surrounding route composes across: by Lemma 2.9 it is the same whether a witness is counted by its number of elementary faults, collisions permitted, or by its number of faulty locations; and in each CSS sector separately it is the same whether detectors are taken to be the Definition-2.7 set or the canonical detector space of Definition 3.5, this being Proposition 3.7 in the Z-sector and its mirror under section 8.1 in the X-sector. Definition 3.5 is named here as a specific space; that it is the detector/observable split the frozen 公共定义 intends is a lead decision recorded in the caveats, not a result proved here.
```

1 103 characters, one line as YAML loads it.

### 4.3 Hashes

| | |
|---|---|
| current claim | `sha256:eb50730d33e716c13be3d46fa92afab98a9e223aa2ac46aff960a9fcd9896ca5` |
| **folded claim (LICENSED)** | **`sha256:8fb50ff01b6465e9c660fc61292958828f448dd740757a8945deae1e107c7ad3`** |

### 4.4 Install notes for the dispatcher (one edit; dry-run already passed)

1. **The YAML scalar style must change.** The current `claim:` is a *plain* multi-line scalar. The folded text
   contains `": "` (in "…composes across: by Lemma 2.9…"), which a plain scalar **cannot** carry — I verified
   the failure: `yaml.ScannerError: mapping values are not allowed here`. Use a **`>-` block scalar** (verified
   round-trip: loads to the exact string above, hashes to `8fb50ff0…`) or a double-quoted scalar (also
   verified). Suggested block form:

   ```yaml
   claim: >-
     For each fixed legal single-round single-ancilla CSS schedule M under the stated ideal
     temporal boundaries and unit-fault model, there is an explicitly constructible finite min-plus
     transfer system (u,A,v) such that d_R(M) = u^T min-plus A^R min-plus v for every R, with the
     two CSS sectors, boundary conditions, unreachable states, and logical terminal condition
     represented exactly. The d_R so computed is moreover invariant under the counting and
     detector-split conventions the surrounding route composes across: by Lemma 2.9 it is the same
     whether a witness is counted by its number of elementary faults, collisions permitted, or by
     its number of faulty locations; and in each CSS sector separately it is the same whether
     detectors are taken to be the Definition-2.7 set or the canonical detector space of Definition
     3.5, this being Proposition 3.7 in the Z-sector and its mirror under section 8.1 in the
     X-sector. Definition 3.5 is named here as a specific space; that it is the detector/observable
     split the frozen 公共定义 intends is a lead decision recorded in the caveats, not a result proved
     here.
   ```

   Re-wrapping is safe provided every continuation line carries the **same** two-space indent (a more-indented
   line would make `>-` preserve a newline and change the hash). Verify with `claim_hash` after the edit.

2. **`reviewed_hash` must be re-bound on *every* review entry**, since `proof_dag_v6` requires all of them to
   equal the current claim hash. Set them to `sha256:8fb50ff0…`.

3. **Honesty about what each review covered.** The wave-15 re-review
   (`circdist_sat_transfer_rereview_20260823.md`) cleared the *pre-fold* sentence and did not see the folded
   clause; after re-binding it must not read as though it did. Amend its `scope` to end with, e.g.:
   *"…clears promotion at CERTIFIED\* with the stated caveat set; this review adjudicated the pre-fold claim
   (sha256:eb50730d…) and is re-bound by the wave-33b bridge fold, which it did not review."* Then add this
   artifact as a second review entry with the scope proposed in §6.3. Multi-review basis lists with per-review
   scope lines are already the repo's convention (`CIRCDIST.sat.window`, `CIRCDIST.lift.iff`,
   `CIRCDIST.cplx.islands`).

4. **Add a `claim-revised` event** recording the fold, its motivation (root caveat R-C4 a/b/c), and this
   artifact as source.

5. **Dry run performed.** A scratch copy of `tools/ research/ artifacts/ provenance/` with the folded claim and
   the re-bound hash installed gives `python3 tools/proof_dag_check.py --problem circdist` →
   `circdist: 16 node files structurally valid / Proof-DAG validation OK: 16 nodes`, identical to the
   pre-edit baseline. No canonical file was touched by this session.

---

## 5. Caveat audit

The node carries six caveats. All six **survive**. Three need amending; two of those are **sharpened**, and
the sharpening is deliberate.

### C1 — T-G3, closed by decision. **SURVIVES, SHARPENED.**

The adjudication the 33a preflight anticipated is correct, but for a more specific reason than "the claim now
asserts equivalence with Definition 3.5's space by name". The mathematics of the folded clause does **not**
depend on the lead decision: Proposition 3.7 and its mirror are theorems about a well-posed, named space, and I
re-derived and recomputed both without reference to whether that space is the intended one. What the fold
changes is the **misreading surface**. Pre-fold, the claim said nothing about detector conventions, so T-G3 was
a caveat about the document's internals. Post-fold, the claim contains the words *"invariant under the …
detector-split conventions"*, and a downstream consumer reading the claim alone could take that for
convention-independence in general. **It is not.** The invariance is proved for the ordered pair
(Definition 2.7, Definition 3.5) and **fails** for other admissible splits — my own recomputation of the
withdrawn mitigation's `𝒟′` gives `d^{2.7} = 2` against `d^{𝒟′} = 3` at `R = 2` and `4` at `R = 3` on
Steane + redundant X (§3.2). So T-G3 must now guard the *claim*, not only the document, and its wording should
carry that counterexample. Proposed replacement:

> `T-G3 is closed BY DECISION, not derivation: the lead ratified Definition 3.5 (verbatim "批准 Definition 3.5,
> 缓解条款不批") as the intended reading of the frozen 公共定义; the mitigation clause was REFUTED by explicit
> counterexample and withdrawn; the installed safe condition is span{D_{b,r}} within D-prime within D
> (re-verified independently at its tightest endpoint on 3 codes). The 2026-08-23 bridge fold makes this caveat
> bite on the CLAIM and not only on the document: the claim now names Definition 3.5, and its certified
> invariance holds for the ordered pair (Definition 2.7, Definition 3.5) ONLY - it is NOT convention
> independence in general, and fails for other admissible splits, e.g. D-prime = span{D_{b,r}} +
> span{D_{a,r}} + span{P_X + lambda} on Steane+redundant-X, where d^2.7 = 2 while d^D-prime = 3 at R = 2 and 4
> at R = 3 (dimension quintuple 28/22/21/12/20, recomputed independently by the wave-33b re-bind review, which
> also confirmed d^D = d^2.7 = 2 at every R on that same instance).`

### C2 — T-G1/G2/G4/G5 open minors. **SURVIVES, unchanged text; one dependency worth knowing.**

The folded clause depends on **T-G1** (the imported Definition-2.8 fault taxonomy, and T3's per-sector-then-
monotone-aggregate convention) and on **nothing else** in this group. It does not touch **T-G2** (state-space
minimality), **T-G4** (computability of `A`), or **T-G5** (availability of the two weight-1 mechanisms). The
T-G1 dependency is real and sharp: control A shows that a different fault taxonomy at the same locations would
break Lemma 2.9 outright. No text change needed, but the record should note the dependency; I put it in the
amended C3 rather than duplicating a caveat.

### C3 — Y-projection needs the uniform unit-cost model. **SURVIVES, SHARPENED (scope widened).**

Pre-fold this guarded Lemma 3.1's Y-splitting. Post-fold it also guards the newly certified Lemma-2.9 clause,
for two reasons I established directly: the merge is weight-**reducing** only under one-unit-per-location
costing, and it is **available** only because Definition 2.8 gives every location a full Pauli group. Proposed
replacement:

> `The Y-projection step needs the uniform unit-cost Pauli fault model (公共定义); a non-uniform cost model
> would reopen it. The 2026-08-23 bridge fold extends this dependency to the newly certified Lemma-2.9 clause:
> the collision merge lowers the count only under one-unit-per-location costing, and it is available at all
> only because Definition 2.8 gives every location a full Pauli GROUP (T-G1, imported not re-derived). Under a
> non-group per-location fault set the two counts come apart - witnessed on Steane/NI/R=2 by 3 explicit
> effects of multiset cost 2 and configuration cost >= 3, each of which costs exactly 1 location under
> Definition 2.8.`

### C4 — evidence scope ≠ statement scope. **SURVIVES; relieved for the folded clause only.**

The main clause is unaffected: Theorem T is still stated for arbitrary legal single-round single-ancilla CSS
schedules while the document's evidence is `d = 3, k = 1, R ≤ 3`. For the **three folded bridges** the evidence
base is now materially wider and independent. Proposed addition to the existing text:

> `... the general case rests on the reviewed derivations. For the three bridges folded into the claim on
> 2026-08-23 the evidence is wider and independent: 110 mechanism-route instances (exact F2 identities) and
> 114 direct minimum-weight instances over 8 codes and 3 schedule families, R <= 3, both sectors, including 4
> codes with BOTH generating sets dependent (2 of them constructed by the reviewer) and BB [[18,4,4]] at
> k = 4 - where the minimum-weight conclusion, not merely the hypothesis, was verified in both sectors.`

### C5 — superseded §11.4 program digest. **SURVIVES, unchanged.**

Document hygiene, safe direction. It does not touch this session: my harness shares no code with the §11.4
program, so a defect there cannot propagate into these results.

### C6 — external assumption A1 (BCOQ Thm 3.112). **SURVIVES, unchanged.**

Worth recording for the root's benefit: the folded clause is **A1-free**. Lemma 2.9, Proposition 3.7 and the
§8.1 mirror are all finite-`R` statements and consume no eventual-periodicity input.

### 5.7 Effect on the sat root's R-C4 — **dischargeable, in part, and only in part**

R-C4 currently reads (root node, caveat index 3): *"…THREE composition steps rest on numbered results NOT in
any premise's claim text (proposer-level): transfer Prop 3.7 …, its §8.1 mirror …, and transfer Lemma 2.9 …"*

After the fold **all three are in the transfer node's certified claim text, by name**, hash-bound. The
proposer-level flag on (a), (b) and (c) is therefore **dischargeable** at wave 35, and the root may compose the
three steps as certified premise content rather than as document-internal results.

**What is not discharged, and must not be read as discharged:** R-C4's *first* clause — *"the detector/observable
split is fixed BY DECISION (Definition 3.5, lead-ratified; corrected condition span{D_{b,r}} within D-prime
within D; W-G3 not carried; S3-prime load-bearing)"* — is untouched, and per §5.1 it now applies to the claim
text itself. My recommendation to wave 35, offered as input and not as an adjudication: **R-C4 should not be
deleted; it should be narrowed to its by-decision clause and re-worded to carry the `𝒟′` counterexample**, so
that the residual caveat is exactly the residual risk. I do not adjudicate the root.

---

## 6. Verdict

### 6.1 Level

**CERTIFIED\***, bound to `sha256:8fb50ff01b6465e9c660fc61292958828f448dd740757a8945deae1e107c7ad3`.

The folded claim is **strictly stronger** than the current one, and everything newly asserted was re-derived
here and confirmed computationally by an independent harness at 110 + 114 instances with zero exceptions.
That is more than enough to carry the extension at the node's existing level.

**Why not PROVED**, honestly, against the existing caveat set:

* **The detector/observable split is fixed by a decision, not a derivation.** A circuit distance is exactly as
  well-defined as the split it is measured against, and the split this claim now names is ratified, not proved
  to be the frozen 公共定义's intent. My own `𝒟′` recomputation shows the value genuinely moves when the split
  moves. That alone is disqualifying for PROVED.
* **Statement scope still exceeds evidence scope for the main clause.** Theorem T quantifies over all legal
  single-round single-ancilla CSS schedules at any depth for any CSS code; the general case rests on reviewed
  derivations. My work widened the evidence for the three bridges, not for Theorem T's core.
* **The model is imported, not re-derived** (T-G1) — a single-point-of-failure the route already records as
  R-C1.
* **A1 is cited as published**, not re-derived here or anywhere in this route.

None of these is a defect I found; all four are already on the node, and all four survive the fold. PROVED
would require closing at least the first, which is a lead-level definitional question, not a mathematical one.

### 6.2 Caveat set to install (six)

Positions 1, 3 and 4 replaced with the amended text of §5.1, §5.3, §5.4. Positions 2, 5, 6 unchanged.

### 6.3 Proposed `basis.reviews` entry for this artifact

```yaml
- path: artifacts/circdist_transfer_bridgefold_20260823.md
  kind: review
  scope: >-
    Focused independent re-bind review (wave 33b, fresh session, author of no circdist artifact)
    folding three composition bridges into the certified claim. All three re-derived by the reviewer
    before comparison with wave-27, then verified with a harness sharing no code with the document,
    its amendment, or either prior review: Prop 3.7 and its section-8.1 mirror as exact F2 identities
    on the Lemma-3.1 projection (110/110 instances, 8 codes, 3 schedule families, R <= 3, both
    sectors, dims matching the 3.3/3.6 closed forms, Def-2.7 hole non-empty in 47), by direct
    minimum-weight search (114/114 including BB [[18,4,4]] in BOTH sectors at R = 1,2,3 - the
    conclusion, not merely the hypothesis wave 27 could reach), and at the mechanism level (54,422 of
    240,917 weight-3 undetectable-and-logical configurations are DETECTED by the Definition-3.5
    space, and Pi repairs all 54,422). Lemma 2.9 verified as d_ms = d_cfg on the same 114 instances,
    with its two hypotheses checked exactly and a non-group control showing the group-closure
    hypothesis is load-bearing. Harness calibrated first against the published T-G3 quintuple
    (28/22/21/12/20; d^2.7 = 2 vs d^D-prime = 3 at R=2, 4 at R=3), reproduced exactly, and it further
    establishes d^D = d^2.7 = 2 there. Licenses CERTIFIED* (not PROVED) for the folded claim with the
    six-caveat set, T-G3 and the unit-cost caveat SHARPENED. This review adjudicated the folded claim
    (sha256:8fb50ff0...); it did not re-adjudicate Theorem T's core, which rests on the earlier chain.
  locator: Section 6
  reviewed_hash: sha256:8fb50ff01b6465e9c660fc61292958828f448dd740757a8945deae1e107c7ad3
```

---

## 7. Limitations of this session, stated plainly

1. **I did not re-adjudicate Theorem T's core.** Sufficiency of `Σ`, the fault dictionary, the two
   correspondence directions, `u`/`v`, the min-plus assembly and the spectrum are as the wave-7 proof, wave-13
   review, Amendment 1 and the wave-15 re-review left them. My clearance covers the folded extension and the
   re-binding; the rest of the claim carries its existing basis.
2. **Minimum-weight search is exact only in the range searched** — to weight 4 on small instances
   (pair-dictionary) and to weight 3 at qLDPC scale (signature search). Every value observed was `≤ 3`, so no
   result depends on the cap; but a hypothetical instance with `d_R ≥ 5` was not searched.
3. **The §3.7 mechanism sweep is a capped enumeration** (~30 000 witnesses per instance, in signature order),
   not an exhaustive one. It is an existence-and-repair statement over a large sample, not a census. Parts A
   and B are exhaustive in their own terms and carry the argument; §3.7 is what makes the mechanism visible.
4. **I did not verify the frozen 公共定义 itself.** Like every premise in this route I read the model as the
   transfer document states it. If §2 misreads the frozen model, everything here inherits the misreading —
   root caveat R-C1, which the fold does not touch and cannot.
5. **Schedule scope.** Three schedule families per small code (`NI`, a randomly found legal + (MC) interleaved
   one, and a padded collision-prone one); the BB instance uses the published NI schedule only, since depth-6
   is exhaustively (MC)-empty for that code and no interleaved BB schedule is on record.
6. **The harness lives in this session's scratchpad and is ephemeral.** §3.1 specifies it completely enough to
   be re-implemented — codes by their check matrices, schedules by their construction rule, identities by their
   statements, both search semantics by their definitions — and the BB code and schedule NI were rebuilt from
   the instances artifact's own algebraic specification, so every number above is reproducible from published
   inputs. Frontier task-002 (reproducible packaging) remains open on the node and is not discharged by this
   session.

---

## 8. Summary table

| item | result |
|---|---|
| hash pipeline validated | 101/101 existing `reviewed_hash` values reproduced |
| current claim hash confirmed | `eb50730d…` ✓ |
| harness calibration (published T-G3 quintuple) | `28/22/21/12/20`, `2 / 3 / 4` — exact |
| Lemma 2.9 re-derived | ✔ , hypotheses (H1) (H2) isolated and checked |
| Prop 3.7 re-derived | ✔ , as identities (E)(A)(B)(C)(D)(S)(I) on `Π` |
| §8.1 mirror re-derived | ✔ , and verified by direct X-sector construction, not relabelling |
| Part A — exact `F₂` identities | **110 / 110**; closed forms match 110/110; hole non-empty in 47 |
| Part B — direct min-weight, small | **102 / 102** (Prop 3.7 + mirror) and **102 / 102** (Lemma 2.9) |
| Part B+ — direct min-weight, qLDPC scale | **12 / 12** and **12 / 12**; BB `d_R = 3` reproduces Table 5.3 |
| mechanism sweep | 54 422 / 54 422 `𝒟`-detected witnesses repaired by `Π` |
| non-vacuity controls | both bite (3 non-group divergences; weight-1 set difference at BB) |
| **folded claim hash** | **`sha256:8fb50ff01b6465e9c660fc61292958828f448dd740757a8945deae1e107c7ad3`** |
| **licensed level** | **CERTIFIED\***, 6 caveats (C1, C3, C4 amended; C1 and C3 sharpened) |
| root R-C4 | (a)(b)(c) dischargeable; by-decision clause untouched; root not adjudicated |
| checker dry-run | `Proof-DAG validation OK: 16 nodes` |
