# k-Sum composition-layer independent review — 2026-07-30

**Reviewer:** fresh Opus instance, commissioned as the rule-6 independent checker for the
2026-07-30 composition/edge-typing layer of the k-Sum proof DAG.
**Scope:** the ten inputs named in the commission (composition blocks on `KSUM.A1`, `KSUM.A2`,
`KSUM.B2`, `KSUM.B4`; route maps on `KSUM.goal`, `KSUM.B1`, `KSUM.B3`, `KSUM.B4b`; the three edge
re-typings `A1e`/`A1f`/`U1`; the `KSUM.B4b.L2.FILT` → `KSUM.B4b.L2.M1` edge-typing question), plus
the two structural debts and the `KSUM.B1` Claim rewrite.
**Artifact:** this file only. No node, index, Mermaid, Lean, or build was touched (per commission
Step 4); applying the verdicts and syncing the views is the lead's duty.

---

## 0. PRE-ACTION REPORT

- **Entry node / statuses as read from disk (2026-07-30):** `KSUM.goal` — **OPEN**, kind GOAL,
  `children: [KSUM.B1, KSUM.B2, KSUM.B3, KSUM.B4]`. Internal layer under review:
  `KSUM.A1` **CONJECTURED**, `KSUM.A2` **CONJECTURED**, `KSUM.B1` **OPEN**, `KSUM.B2` **OPEN**,
  `KSUM.B3` **OPEN**, `KSUM.B4` **OPEN**, `KSUM.B4b` **OPEN**, `KSUM.k3.donor` **OPEN·PARKED**,
  `KSUM.L32` **NUMERICAL**, `KSUM.LEAN` **OPEN**, `KSUM.B4b.L2.FILT` **CONJECTURED·pending-review**,
  `KSUM.B4b.L2.M1` **PROVED**.
- **Role:** reviewer. **Independence statement:** I did not author any of the reviewed material —
  not the composition blocks, not the edge re-typings, not the proposed route-kills, not the Lean
  modules, not the manuscript. I was given no desired outcome and no indication of which verdict
  the lead expects; the commission states explicitly that confirmation and rejection are equally
  acceptable. My only inputs were the on-disk files and the protocols.
- **Highest status my evidence can license (§2 ladder):** as the independent checker I may license
  **PROVED** on a composition claim whose proof I verified, **REFUTED** on a route entry whose kill
  I verified, and **CERTIFIED\*** where my review is single/partial-scope. The *write* is the
  lead's; this artifact is the citation.
- **Gates / deliverables (one line each):** (a) per-composition verdict with a 7c
  worksheet written before reading the lead's block; (b) per-route-kill verdict; (c) per-edge-typing
  verdict; (d) the three adjudications (A1d duplication, `gcd(k,q)=1` prose repair, A2b dual status);
  (e) the two structural debts; (f) a rule-7-complete audit (7a–7g); (g) one artifact, no repo edits.
- **Conflicts between commission text and disk — TWO, both reported rather than silently resolved:**
  1. The commission says "`KSUM.k3.donor`, `KSUM.L32`, and `KSUM.LEAN` still have **NO composition
     blocks**". **Disk contradicts this.** All three carry `composition:` blocks written in the
     2026-07-30 pass: `KSUM.k3.donor.yaml:12-32` (a three-entry route map), `KSUM.L32.yaml:12-19` (a
     one-entry route map), `KSUM.LEAN.yaml:12-17` (an AND composition claim with an inline scope-check
     proof). What is actually missing is a *route proof* (`proof: "none"`) on three of those five
     entries. I answer the debt under the disk reading in §7.
  2. The commission describes `KSUM.B4b.L2.FILT` as possibly needing to become "a status-propagating
     CHILD of `KSUM.B4b.L2.M1`, retroactively adding a composition obligation to a PROVED node". The
     disk shows that M1's archived independent review (`ksum/artifacts/ksum_L2p2_review.md:74-83`,
     `:95-106`) **already re-derived and finitely verified the filtration bridge**, which changes the
     adjudication materially (§5.5). I flag it because the commission's framing presupposes the step
     is unreviewed.

---

## 1. VERDICT TABLE

| # | Item | Verdict |
|---|---|---|
| 1 | `KSUM.A1` composition `A1a ∧ A1b ∧ A1c ⇒ A1d` | **CONFIRMED-WITH-REPAIRS** (R-A1-1 … R-A1-4) |
| 2 | `KSUM.A2` composition `A2a ∧ A2b ⇒ A2` | **CONFIRMED-WITH-REPAIRS** (R-A2-1 … R-A2-3) |
| 3 | `KSUM.goal` route `B1 → G` (proposed kill) | **KILL CONFIRMED** (scoped; two mandatory repairs) |
| 4 | `KSUM.goal` route `B3 → G` (proposed kill) | **KILL CONFIRMED** (scoped to the registered routes) |
| 5 | `KSUM.B3` route `L32 → B3` kill | **KILL CONFIRMED** |
| 6 | `KSUM.B3` route `L33 → B3` kill | **KILL CONFIRMED** |
| 7 | `KSUM.B2` composition `A2 ∧ k3.donor ⇒ B2` | **CONFIRMED-WITH-REPAIRS** (R-B2-1 … R-B2-3; one is a genuine missing premise) |
| 8 | `KSUM.B4` composition `B4a ∧ B4b ⇒ B4` | **CONFIRMED-WITH-REPAIRS** (R-B4-1, R-B4-2) |
| 9 | `KSUM.B4b` route map (L1/L2/L3) | **CONFIRMED** (routes correctly recorded as unwritten) |
| 10 | `KSUM.B1` route map (L11/L12 moot; A1-route defect) | **CONFIRMED** |
| 11 | Re-typing `A1e` children → related | **ENDORSE** (with a sync defect to fix) |
| 12 | Re-typing `A1f` children → related | **ENDORSE** (with the same sync defect) |
| 13 | Re-typing `U1` children → related | **ENDORSE** |
| 14 | `goal → B4` edge type QUESTIONED | **ENDORSE the re-typing to `related`** |
| 15 | `FILT → M1` edge-typing | **ENDORSE `related`** (do NOT make it a child) + raise FILT to CERTIFIED\* |
| 16 | Adjudication: `A1` / `A1d` duplication | **KEEP BOTH**, with `A1`'s Claim rewritten (ruling in §6.1) |
| 17 | Adjudication: `gcd(k,q)=1` prose repair | **SCOPED REMOVAL**, not deletion (ruling in §6.2) |
| 18 | Adjudication: `A2b` dual-status split | **SPLIT ENDORSED** (ruling in §6.3) |
| 19 | `KSUM.k3.donor` route map (exists on disk) | **CONFIRMED-WITH-REPAIRS** (§7.1) |
| 20 | `KSUM.L32` route map (exists on disk) | **ENDORSE the re-typing it proposes** (§7.2) |
| 21 | `KSUM.LEAN` composition (exists on disk) | **REJECTED — the claim is false as written** (§7.3) |

### THE ONE COMPOSITION CLAIM THAT IS WRONG (commission Step 4: put this at the very top)

**`KSUM.LEAN`'s composition claim is false as written, and its inline proof is the false part.**
The block (`ksum/proof-dag/nodes/KSUM.LEAN.yaml:12-17`) says T1 ∧ T2 ∧ T3 ∧ statement-fidelity
imply the parent, that the composition "is definitional", and that *"the only content is that the
SCOPE of the union of T1/T2/T3 equals the paper's in-scope theorem list, checked against the LaTeX
table of theorems"*, with the inline proof asserting that census: *"T1 covers `sec:prelim` facts +
the k=2 chain + `thm:oabarrier`; T2 covers `prop:rosmanis`(1) + `thm:kfloor` lemmas; T3 covers the
`sec:proof-search` obstruction group; `thm:k2-upper` excluded as algorithmic — matches the paper's
theorem census."*

That census does not match. The parent's own scope predicate is "every theorem that is **not** an
imported citation and **not** a quantum-algorithmic construction". Enumerating the manuscript's
theorem-like environments against the three tiers, the following are in scope by that predicate and
are covered by **no** child:

- `lem:embed`, `prop:embed`, `lem:embed-allt`, `rem:k3embed` (the whole `k`-collision embedding,
  `ssec:embed` + `app:embed`) — T2 is scoped to `prop:rosmanis`(1) and the `thm:kfloor` lemmas;
- `prop:kclaw-fillers` and `prop:kclaw-coloring` (`ssec:kclaw-lb`) — the paper's own first
  above-`√n` bounds for `k`-partite `k`-collision;
- `prop:rosmanis` **(2) and (3)** — the census explicitly names only clause (1);
- `lem:factorial-filtration` and `prop:joint-lp` — exactly the two labels the T3 audit reported as
  having no node at all (finding F-T1), now registered as `KSUM.B4b.L2.FILT` and
  `KSUM.B4b.L2.JOINTLP`;
- `rem:torsion` (a proved statement, not a gloss).

So `T1 ∧ T2 ∧ T3 ∧ fidelity` does **not** imply `KSUM.LEAN.Claim`; the implication fails on scope,
not on any child's quality. Nothing propagates today (the node is OPEN and non-propagating to
`KSUM.goal`), so **no status is currently wrong** — but if the fidelity gate closes and the three
tiers land, this block as written would discharge a parent that its children do not cover. Repair in
§7.3. *Second, smaller census defect in the same block:* the 2026-07-30 `KSUM/` DAG-mirroring layer
(17 modules, including the `A1`/`A2`/`B2`/`B4` composition theorems under review here) is not a
child of `KSUM.LEAN` and appears nowhere in the AND, so the audit's own composition tier is outside
the node that is supposed to account for the audit.

**Everything else in the layer is correct-but-incomplete rather than wrong.** The two findings
closest to the "wrong" line are (i) `KSUM.A1`'s composition consuming an all-targets equivalence
that `lem:transl-cover` does not prove (§3.1, R-A1-3) — the composition claim survives because the
manuscript's own argument avoids it, but the premise as attributed to child `A1c` is strictly
stronger than the child, and is FALSE at small `q`; (ii) `KSUM.B4`'s mechanized sandwich being
**vacuous** because its `B4bClaim` is unsatisfiable at `q ∈ {1,2}` (§3.4, R-B4-1). Also relevant:
three of the reviewed nodes' frozen Claims (`KSUM.goal`, `KSUM.B1`, `KSUM.k3.donor`) are **not
propositions**, which makes two route verdicts scope-dependent rather than absolute (§4.1).

---

## 2. RULE-7c WORKSHEETS — written BEFORE reading the lead's composition blocks

Method actually followed, in order: (a) read the *children's* frozen Claims from the child node
files and the manuscript lemmas they cite (`sec:prelim` facts (i)/(ii), `thm:abi`, `thm:tani`,
`lem:encode`, `cor:threshold`, `thm:kfloor`, `lem:core`, `prop:core-even`, `lem:core-odd`,
`lem:transl-cover`, `rem:window-tight`, `lem:embed`, `prop:embed`, `lem:embed-allt`,
`rem:k3embed`, `rem:kclaw-composition`, `prob:donor`, `rem:crossover`,
`lem:factorial-filtration`, `thm:pair-tensor`); (b) wrote the premise lists and composition
arguments below, using `Read` with explicit line ranges on the parent files so that only their
`## Claim` sections were visible and their `composition:` front matter and `## Composition proof` /
`## Route proofs` sections were NOT; (c) only then read the parent files and the Lean modules in
full; (d) diffed. This section is the (b) artifact, unedited after step (c).

### 2.1 Worksheet A1 — what `A1a ∧ A1b ∧ A1c ⇒ A1d` would need

*Children's frozen Claims as read:* A1a = "freeze k−2 coords: CONSTANT `C₀=⌊q/(k−1)⌋` (as authored)
OR positive CORE summing to `t` (kills all `d≥1` bad patterns)"; A1b = "EVEN 2n-coord k=2 claw
encoding on live part (no unpaired live coord)"; A1c = "target coverage: window family +
translation identity `kSum_t(x)=kSum_{t+ka}(x+a·1)`, all `t` via gcd argument, no parity cond.";
conclusion A1d = the two-clause `Ω_k(√N q^{1/6})` / `Ω_k(N^{2/3})` floor over
`q₀(k)=2k²+2k−5 ≤ q ≤ C_kN`, all `t`, all large `N`.

**My premise list (P1–P8):**

- **P1 (even-parity identity).** For `k≥3`, `K≥2`, `U=kK+1`, `q ≥ (k−1)(kK+1)`, `t ∈ W_even =
  [(k−2)U, q−U]`, and `N=(k−2)+2m`: the frozen-core+live-block string satisfies
  `kSum_{Z_q,t,N}(x(f,g)) = Claw_{m→K}(f,g)` pointwise. (= A1a ∧ A1b on the even branch;
  manuscript `prop:core-even`.)
- **P2 (odd-parity identity).** Same with the **parked coordinate** `v=t+(k−1)K+1` on the shorter
  window `W_odd = [(k−2)(kK+1), q−2(k−1)K−2]`, `N=(k−2)+2m+1`. (Manuscript `lem:core-odd`.)
  *Flag written at (b)-time:* the parked coordinate appears in **no child's frozen Claim** — A1a
  freezes the core, A1b encodes the live block, A1c covers targets. Unless A1a's "core" is read to
  include it, the odd branch needs an explicit premise.
- **P3 (target coverage).** Translation identity `kSum_{q,t,N}(x)=kSum_{q,t+ka,N}(x+a·1)` plus
  "window length `≥ k ≥ gcd(k,q)` ⇒ every coset `t+kZ_q` meets the window". (= A1c;
  `lem:transl-cover`.) **No coprimality hypothesis is needed or used.**
- **P4 (query-model transfer).** (i) restriction to a subdomain does not increase `Q`;
  (ii) per-coordinate relabeling costs a factor ≤ 2, with the alphabet allowed to vary by position;
  **(iii) a third principle, in neither (i) nor (ii): coordinates frozen to constants may be
  dropped — the encoder changes the input LENGTH (`N` vs `2m`), which (i) does not cover.** Both
  the `k−2` core and the parked coordinate need (iii).
- **P5 (donor).** `thm:abi` `Q(Claw_{n→κ})=Ω(√n κ^{1/6})` for `2≤κ<n`, extended by `thm:tani` to
  `2≤κ≤2n−1`.
- **P6 (parameter bookkeeping, glue not hypothesis).** `K:=⌊(q−2k+1)/(k²−2)⌋`;
  `K≥2 ⟺ q ≥ q₀(k)`; `K = Θ_k(q)`; `K ≤ 2m−1` for all large `N` once `q ≤ C_kN`;
  `m=⌊(N−(k−2))/2⌋=Θ_k(N)`; plateau branch `K=m−1`, `q ≥ c_kN` with e.g. `c_k=k²`.
- **P7 (both parities of `N−(k−2)`).** A1d quantifies over all large `N`, so both P1 and P2 are
  required; P2 carries the *stronger* modulus condition, which is why `thm:kfloor` states
  `q ≥ (k²−2)K+2k−1`.
- **P8 (uniformity).** Constants depend on `k` only, not on `t`, `N`, `q`; the boundedly many
  factor-2 losses (one relabeling in the encoding, two in the translation `Θ`) are absorbed in `Ω_k`.

**My one-paragraph composition argument.** Fix `k≥3`, `N` large, `t∈Z_q` arbitrary,
`q₀(k) ≤ q ≤ C_kN`. Put `K=⌊(q−2k+1)/(k²−2)⌋` and `m=⌊(N−(k−2))/2⌋`. By P6, `K≥2`. By P3 choose `a`
with `t+ka` in the window matching the parity of `N−(k−2)`, and pay a factor `Θ(1)` (P4(ii) applied
in both directions). By P1/P2 the restriction of `kSum_{Z_q,t+ka,N}` to the encoder's image equals
`Claw_{m→K}` read through a per-coordinate map that is a bijection on the `2m` live coordinates and
constant on the `k−2` core and the parked coordinate. Apply P4(i) (restriction), P4(iii) (drop the
frozen coordinates), P4(ii) (re-encode the live alphabet): `Q(kSum_{Z_q,t,N}) = Ω(Q(Claw_{m→K}))`.
By P6, `2 ≤ K ≤ 2m−1`, so P5 applies and gives `Ω(√m K^{1/6}) = Ω_k(√N q^{1/6})`. For the plateau
take `K=m−1<m` (ABI's own range) whenever `q ≥ c_kN`, giving `Ω_k(N^{2/3})`. ∎

**Arithmetic I verified myself, from scratch, at (b)-time** (recorded here because it is what makes
P6 a computation rather than an assumption):

- `K≥2 ⟺ q−2k+1 ≥ 2(k²−2) ⟺ q ≥ 2k²+2k−5 = q₀(k)`. ✓ (So A1d's floor is exactly "the core
  construction admits `K≥2`", not an extra assumption.)
- `K = Θ_k(q)`: upper `K ≤ q/(k²−2)`; lower, writing `q=q₀+s`, `K ≥ 1+s/(k²−2)` and `K≥2`, whence
  `K ≥ q/q₀(k)` in both the `q≤2q₀` and `q>2q₀` cases. ✓
- The sharper two-sided form **`q ≤ 2k²·K`** holds for every `k≥3` once `K≥2`: at the largest `q`
  compatible with a given `K`, namely `q=(k²−2)(K+1)+2k−2`, the inequality reduces to
  `K ≥ (k²+2k−4)/(k²+2)`, and `(k²+2k−4)/(k²+2) < 2 ⟺ 0 < k²−2k+8`, always true. ✓
- Odd-branch modulus dominates the even one: `[(k²−2)K+2k−1] − (k−1)(kK+1) = (k−2)K+k > 0` for
  `k≥3`. ✓ So `thm:kfloor`'s single stated condition covers `prop:core-even` too.
- Claw range: `K ≤ q/(k²−2) ≤ C_kN/(k²−2)` and `2m−1 ≈ N`, so any `C_k ≤ (k²−2)/2` works for large
  `N`; plateau needs `q ≥ (k²−2)(m−1)+2k−1`, so `c_k=k²` works, and **`C_k=c_k=(k²−2)/2` makes the
  two clauses contiguous** — the theorem as stated does not claim contiguity, and with an
  independently chosen small `C_k` and `c_k=k²` a window `(C_kN, c_kN)` is left unclaimed. Not an
  error; worth one sentence (MINOR-A1-a).

**Premises that are NOT in any child and must be declared explicitly:** P4(i), P4(ii), P4(iii)
[= Lean finding F1], P5 (ABI/Tani), and — unless A1a is widened — P2's parked coordinate.
**Premise that is NOT needed:** `gcd(k,q)=1`.

### 2.2 Worksheet A2 — what `A2a ∧ A2b ⇒ A2` would need

*Children:* A2a = the payload/tag formulas `u_j=ω^{j−1}`, `u_k=−(ω^{k−1}−1)/(ω−1)`,
`w_j=V(2k+1)^{j−1}`, modulus `q=(P+1)(M+1)` (Lean note: rendered as **completeness**);
A2b = "all wrong block-multisets excluded (balanced base-`ω`) + 62,140 exhaustive checks"
(Lean note: rendered as **soundness**). *Parent:* "exact query-free reduction k-partite
k-collision → k-Sum, `q=Θ_k(R^{k−1})`".

**My premise list (Q1–Q6):**

- **Q1 completeness** (A2a): good pattern `μ=(1,…,1)` sums to `0` iff the `k` payloads coincide.
- **Q2 soundness** (A2b): every wrong pattern `μ≠(1,…,1)` is at cyclic distance `≥1` from `0`;
  needs `1≤|m(ν)|≤M` (balanced base-`(2k+1)` uniqueness), `|pay|≤P`, and `q=(P+1)(M+1)=VM+P+1`.
- **Q3 exactness ⇒ pointwise identity** `kSum_{Z_q,0,kn}(enc(g)) = Coll_{k,n→R}(g)` for every `g`.
- **Q4 "query-free"** must resolve to a definition: the encoder is *per position* —
  position `i` of block `j` ↦ `w_j + u_j g_j(i)` — so one query to the encoded string is answered
  by one query to `g`; this is exactly fact (ii) (factor ≤2), plus the fact that `n` and `kn`
  positions correspond bijectively (no length change here, so P4(iii) is NOT needed for A2).
- **Q5 parameter clause** `q=(P+1)(M+1)=Θ_k(R^{k−1})`, `N=kn`: needs
  `P=k(R−1)(ω^{k−1}−1)/(ω−1)=Θ_k(R^{k−1})` with `ω=2R−1`, and `M=((2k+1)^{k−1}−1)/2` a **constant
  in `R`** for fixed `k`. Both are read off A2a's data — but note A2a's *frozen Claim prints
  neither the definition of `P` nor of `M`*, only `q=(P+1)(M+1)`.
- **Q6 all targets** — *only if* A2's claim is meant for every `t`: then `gcd(k,q)=1` is needed
  (multiplication by `k` must be a bijection of `Z_q`), and it is a **theorem** from A2a's data:
  `k∣P` (immediate, `P` carries the factor `k`) gives `P+1≡1 (mod p)` for every `p∣k`; and
  `2(M+1)=(2k+1)^{k−1}+1` gives `M+1≡1 (mod p)` for odd `p∣k` (since `2k+1≡1`, numerator `≡2`, and
  `2` is invertible) and `M+1` odd when `2∣k` (since `2k+1≡1 mod 4` ⇒ numerator `≡2 mod 4`).

**My composition argument.** Q1 ∧ Q2 give Q3 pointwise on the encoded subdomain; Q4 turns Q3 into
`Q(kSum_{Z_q,0,kn}) = Ω(Q(Coll_{k,n→R}))` via facts (i)+(ii); Q5 supplies the modulus asymptotics
that make the statement about `q`; Q6, if all targets are claimed, is supplied by `lem:embed-allt`
and is FORCED by the construction rather than assumed. ∎

**Scope flags written at (b)-time.** (α) The `Θ_k(R^{k−1})` clause is a statement about **one
constructed modulus per `R`**, not about an interval of moduli; (β) `rem:k3embed`'s tighter `k=3`
recipe at `q ≥ 21R²−8` is a *different* construction, where coprimality with 3 is a genuine
hypothesis, not automatic — so any "`gcd(k,q)=1` is forced" statement must be scoped to
`q=(P+1)(M+1)`; (γ) A2b's "62,140 exhaustive checks" is NUMERICAL corroboration and cannot be part
of a proposition quantified over all instances.

### 2.3 Worksheet B2 — what `A2 ∧ k3.donor ⇒ B2` would need

*Children:* A2 (above); `k3.donor` = "k-Sum CONSEQUENCE: needs a WALK-OPTIMAL small-range `k≥3`
k-collision detection LB — no tight donor found; partial floors L2e/f do not suffice".

**Type flag written at (b)-time:** `k3.donor`'s frozen Claim is **not a proposition** — it is a
statement of need. As an AND input it must be read as the proposition
`∃c ≥ (k−1)/(2(k+1)): Q(Coll_{k,n→R}) = Ω(√n R^c)` uniformly for `R` up to `n^{Θ(1)}`.

**My premise list (R1–R6):**

- **R1** A2's exact reduction, at the constructed family `q=q_k(R)=(P+1)(M+1)`, `N=kn`.
- **R2** the donor: `Q(Coll_{k,n→R}) = Ω(√n R^c)`, **valid uniformly over the `R`-range that the
  conclusion's `q`-range needs** (the L2fC lesson: a donor living only at `R=Ω(n²)` forces
  `q=Ω_k(N^{2(k−1)})`, outside the useful window).
- **R3** transfer arithmetic: `R=Θ_k(q^{1/(k−1)})`, `N=kn` ⇒ `√n R^c = Θ_k(√N q^{c/(k−1)})`.
- **R4** facts (i)/(ii) (already inside A2).
- **R5 novelty side condition:** the transported bound must EXCEED the standing envelope
  `max{thm:kfloor, BS}`; without it the composition is valid but dominated (`rem:kclaw-composition`
  proves exactly that for the available `c=1/6`). Correct placement: on the `goal → B2` route, not
  on B2 itself.
- **R6 construction-family / padding premise** *(my own; flagged at (b)-time as the one most likely
  to be missing)*: `q` ranges over the discrete set `{q_k(R)}` and `N` over multiples of `k`. A
  conclusion of the form "for all `q` in a window and all `N`" needs a padding lemma in `N` and an
  interpolation/monotonicity argument in `q`. The manuscript's own footnote to
  `rem:kclaw-composition` says this explicitly ("a family-only statement, with no padding to
  arbitrary `N` and no interpolation to moduli between construction points").

### 2.4 Worksheet B4 — what `B4a ∧ B4b ⇒ B4` would need

*Children:* B4a = `Q(2Sum_{Z_q,t,N}) = O_ε(N^{1/2+ε} q^{1/4})`; B4b = "close the remaining
`q^{1/6}`-vs-`q^{1/4}` window through any registered lower-bound route".

**My premise list (S1–S5):**

- **S1** an upper bound `U(N,q)` — B4a.
- **S2** a lower bound `L(N,q)` — B4b's (unwritten) output.
- **S3 two-parameter matching:** `L` and `U` must agree in the exponents of **both** `N` and `q`
  at the **same** `(N,q)`; agreement on one slice (fixed `q`, or `q=Θ(N)`) closes nothing.
- **S4 ε-tolerance:** B4a carries `N^{1/2+ε}` for every `ε>0`, so "closed" can only mean matching
  up to `N^{o(1)}`; the composition claim must say so or it is unsatisfiable.
- **S5 same problem family** *(my own)*: B4a is stated for cyclic `Z_q`, every `q≥2`, every `t`,
  after fixed-point preprocessing; the registered lower-bound routes (M1 and the L2 group) are
  stated for **odd `q`, `N ≥ q`**, all `t`. A sandwich is only a sandwich where the two scopes
  coincide, so B4's composition must carry the intersection `(G=Z_q, q odd, N≥q)` or explicitly
  widen one side.

### 2.5 Worksheet — the four `goal` routes

Goal's frozen Claim: "reduce alphabet requirement in BS `Ω(N^{k/(k+1)})` for fixed `k≥3`; find
`Q(N,k,q)` between `q=O(1)` (Grover `√N`) and `q≥n^k` (BS tight)". **This is not a proposition**
(rule 7g), and the two readings give different route verdicts:
**(A)** "prove `Ω(N^{k/(k+1)})` at alphabet size far below `n^k`"; **(B)** "determine `Q(N,k,q)` in
the middle range". I record both and rule under (A), the reading every route entry presupposes.

- **`B1 → G`.** What a *kill* needs, in my own terms: not "the currently proved floor `2/3` is
  below `k/(k+1)`" (that only says the route has not yet reached the target), but a **ceiling**:
  every bound obtainable by this route is `≤ O(N^{2/3})`. That ceiling is available and is
  donor-intrinsic — `Q(Claw_{m→K}) = O(m^{2/3})` for every range `K`
  (Ambainis element-distinctness / Childs–Eisenberg, cited in the manuscript for `cor:threshold`),
  and `m ≤ N/2`. So *any* reduction whose live block carries a 2-wise (pair) problem on at most `N`
  coordinates is capped at `O(N^{2/3})`, and `2/3 < k/(k+1)` for every `k≥3`. **A kill that omits
  the donor-ceiling citation proves the wrong thing** (rule 3: "a route whose current output falls
  short is not refuted; a route whose ceiling falls short is").
- **`B2 → G`.** Conditional on the donor; correctly CONJECTURED if and only if the route entry
  carries R2, R5, R6 above.
- **`B3 → G`.** A kill needs: (a) every registered B3 sub-route is dead or non-asymptotic, and
  (b) the standing constraint that finite exact `Adv±` values at reachable `n` cannot license an
  asymptotic exponent (G11). (b) is a constraint on *inference from those runs*, not a theorem that
  no direct method exists, so the kill can only be scoped to the **registered** routes L31/L32/L33.
- **`B4 → G`.** B4 is about `k=2` (`q^{1/6}` vs `q^{1/4}`); the goal is `k≥3`. There is no
  reduction from the `k=2` window to the `k≥3` target on disk. As an edge type, "children" asserts
  status propagation that nothing supports.

### 2.6 Worksheet — `B3`'s internal routes and `B4b`'s

- **`L31 → B3`**: child REFUTED·DEAD ⇒ route moot by §1 ("a REFUTED child kills that route").
- **`L32 → B3`**, **`L33 → B3`**: both children are NUMERICAL exact-value computations at small
  `(N,q)`. Under G11 no exponent claim follows, so no route to a `k≥3` asymptotic lower bound
  exists *through these runs*; and both are `k=2`-only, which is a second, independent scope kill
  relative to a `k≥3` goal.
- **`B4b`'s L1/L2/L3**: all three are unfinished constructions; L2's PROVED components (M1, M2, T4,
  VBUD, ORIENT, G1–G3, BANDMULT, L2P3) are *obstructions and tools*, i.e. they constrain the
  witness rather than build it, so they cannot be assembled into a route proof. The honest route
  status is "route proof unwritten" for all three, not "route refuted".

---

## 3. PER-ITEM DETAIL — THE FOUR AND-COMPOSITIONS

### 3.1 `KSUM.A1` — `A1a ∧ A1b ∧ A1c ⇒ A1d` — **CONFIRMED-WITH-REPAIRS**

**Diff of my worksheet (§2.1) against the lead's block.** The frozen composition claim is a faithful
restatement of `A1d`, and the four-step proof is the manuscript's argument. Agreements: the four
declared `rel` premises are exactly my P4(i), P4(ii), P4(iii) and P5 — including the
coordinate-freezing principle, which I derived independently at (b)-time before reading the block or
the Lean, and which the lead reached from the prose side and the Lean audit reached from the
formalization side. **Three independent derivations of the same missing premise; I flag the
coincidence per 7c and confirm the premise is real.** I also confirm the lead's/Lean's finding that
`gcd(k,q)=1` is NOT needed here: `lem:transl-cover`'s covering runs off the window length
`≥ k ≥ gcd(k,q)`, which I re-derived from the appendix before reading the claim.

Differences, all repairs rather than refutations:

- **R-A1-1 (premise not supplied by any child — the parked coordinate).** The composition needs both
  parities of `N−(k−2)`; the odd branch is `lem:core-odd`'s parked coordinate `v = t+(k−1)K+1`,
  which appears in **no child's frozen Claim** (`A1a` says "freeze k−2 coords"). The Lean rendering
  silently widens `A1a.Claim` to core size `m ∈ {k−2, k−1}` (`KSUM/A1a.lean:82-97`) and the node's
  work record concedes the prose "mentioned only in passing". This is the standing failure mode
  "smuggled hypothesis": the composition consumes a statement strictly stronger than the child it is
  attributed to. It is bookkeeping, not mathematics — `lem:core-odd` is in the manuscript and `A1f`
  records that R3 independently re-audited it — but it must be fixed by widening `A1a`'s frozen
  Claim to "a frozen core of `k−2` coordinates, plus the parked coordinate when `N−(k−2)` is odd",
  or by adding the odd branch as an explicit `rel` entry citing `lem:core-odd`.
- **R-A1-2 (missing hypothesis of the cited donor).** The prose step 4 imports the ABI/Tani bound
  without stating the claw range condition `2 ≤ K ≤ 2m−1`. That condition is where the ceiling
  `q ≤ C_kN` comes from and is not optional — without it `thm:tani` does not apply. The Lean proof
  *does* carry it (`hκ2n : κ < 2 * n`, `KSUM/A1.lean:182`, derived from `q ≤ N` with `C_k = 1`), so
  this is a prose-only defect; add one clause.
- **R-A1-3 (the significant one: an over-strong premise attributed to `A1c`).** Step 3 lifts a bound
  proved at *one* target to *every* target. That step needs `Q(kSum_{t₀}) ≤ C·Q(kSum_t)` for the
  construction's target `t₀` and arbitrary `t` — and the Lean makes it explicit as
  `KSUM.A1c.Claim` = "for every pair of targets `t₀, t`, `Q(kSum_{t₀}) ≤ C·Q(kSum_t)`"
  (`KSUM/A1c.lean:89-92`). **`lem:transl-cover` does not prove that.** Translation relates only
  targets in the same coset `t + kZ_q`; the covering half says every coset *meets the window*. For
  `gcd(k,q) > 1` different cosets are not related by any argument on disk, and the all-pairs form is
  outright **false** at `k=3, q=3` (where `kSum_{Z_3,0,N}` is constant for `N ≥ 7` while
  `kSum_{Z_3,1,N}` is not — the same witness the reorg report uses for F-R8, there read only as a
  non-vacuity remark). The manuscript's own proof of `thm:kfloor` avoids this: it picks, *for each
  `t`*, an `a` with `t+ka` in the window and applies `prop:core-even` **at that target**, which is
  legitimate because `prop:core-even` holds for *every* `t ∈ W_even`. **Repair (available and
  costless):** state `A1a` for *every* window target rather than for an existential `t₀`, and state
  `A1c` as the coset-covering statement ("for every `t` there is a window target `t′ ∈ t+kZ_q` with
  `Q(kSum_t) ≥ Q(kSum_{t′})/C`"). The composition then closes with the same four steps and no
  over-strong premise. Until repaired, `A1c`'s PROVED label does not cover the statement the
  composition consumes (rule 7d).
- **R-A1-4 (notation, rule 7e "undefined terms").** Step 4 writes `n` and `κ` — the `k=2` symbols —
  for the `k≥3` objects `m = ⌊(N−(k−2))/2⌋` and `K = ⌊(q−2k+1)/(k²−2)⌋`, and asserts "`n = Θ(N)`
  and `κ = Θ(q)`" without defining either in this setting. Rename to `m`, `K` and state the choice
  of `K` and the two-sided estimate.

**Arithmetic verified independently (7f: I verified the mathematics, and separately the statement
correspondence of the Lean; I did NOT rebuild — no `lake` was run, per Step 4).** `K ≥ 2 ⟺ q ≥ q₀(k)`;
`K ≥ q/q₀(k)`; `q ≤ 2k²K` for every `k ≥ 3` once `K ≥ 2` (reduces to `0 < k²−2k+8`); the odd-case
modulus dominates the even one by `(k−2)K + k > 0`; `C_k = 1`, `c_k = 1/2` are admissible and, being
`c_k < C_k`, make the two clauses of `A1d` **overlap**, so the exhibited constants close the
coverage question the prose statement leaves open. The Lean `A1d.Claim` (`KSUM/A1d.lean:61-67`) is a
faithful and slightly stronger (explicit-constant) rendering of the frozen prose, with `A, B, C_k,
c_k, N₀` depending on `k` only — I checked the quantifier order term by term.

**Regime coverage (7b).** `k = 3`: the core degenerates to the single coordinate `c₁ = t` and
`prop:core-even`'s second bad-pattern bullet is empty — checked, the argument survives. Large `k`:
`q₀(k) ~ 2k²` and `C_k = 1` keep the window nonempty for `N ≥ N₀(k) = 40k+40`. `q` odd and `q` even:
the `k≥3` construction imposes no parity condition, correctly. `m ∈ {k−2, k−1}`: covered by the Lean
decomposition `N = 2n + m`, uncovered by the prose (R-A1-1). Boundary `q = q₀(k)`: `K = 2` exactly,
and `2 ≤ K ≤ 2m−1` still holds — checked.

**Verdict: CONFIRMED-WITH-REPAIRS (R-A1-1 … R-A1-4).** With R-A1-1 and R-A1-3 applied, the
composition claim is proved and I license **PROVED** on `KSUM.A1`'s composition, hence
`status(A1) = min(PROVED, A1a, A1b, A1c, A1d) = PROVED`. Without them, `A1` stays CONJECTURED,
because as written the composition rests on a premise (`A1c` all-pairs) that its child does not
carry.

### 3.2 `KSUM.A2` — `A2a ∧ A2b ⇒ A2` — **CONFIRMED-WITH-REPAIRS**

**Diff against my worksheet (§2.2).** My Q1–Q5 map one-to-one onto the block's steps 1–5, including
the observation that the AND is genuine (completeness and soundness are the two directions of one
iff). My Q6 is the `gcd` question, which the block raises and the Lean settles. No disagreement on
the mathematics.

- **R-A2-1 (scope of the `Θ_k` clause — the one place the claim is weaker than it reads).** "`q =
  Θ_k(R^{k−1})`" is a statement about the constructed modulus **for each `R`**, uniformly in `R` for
  fixed `k`. The Lean renders it per-`EmbedData` instance (`∃ cq, R^{k−1} ≤ q ≤ cq·R^{k−1}`,
  `KSUM/A2.lean:186`) and honestly names this as a gap. The prose composition should say the same in
  one clause: the reduction produces one modulus per `R`, and the uniformity of `c_P` and `M` in `R`
  is a property of `lem:embed`'s formulas, which `A2a`'s frozen Claim does not print (it gives
  `q=(P+1)(M+1)` but neither `P = k(R−1)(ω^{k−1}−1)/(ω−1)` nor `M = ((2k+1)^{k−1}−1)/2`).
  Consequence for citation: the two arithmetic facts the coprimality theorem consumes (`k ∣ P`,
  `2(M+1) = (2k+1)^{k−1}+1`) are read off `lem:embed`'s parameter display, not off `A2a`'s Claim, so
  the composition must cite that display explicitly.
- **R-A2-2 (query-freeness must resolve to a definition, 7g).** The block's step 4 defines it
  operationally ("one query to the `kSum` instance is answered by one query to the `k`-collision
  instance") — good — but the term "query-free" appears in `A2`'s frozen Claim without that gloss.
  Either put the gloss in the Claim or define the term once. Note also that, unlike `A1`, `A2` needs
  **no** freezing principle: the encoder is length-preserving (`kn ↦ kn`), so only facts (i)/(ii)
  are used. I checked this against `KSUM/A2.lean:206-214` and confirm `QueryModel.freeze` does not
  appear in the A2 chain.
- **R-A2-3 (non-vacuity, §7.10(5)).** `A2.Claim` is `∀ D : EmbedData, …`, and no `EmbedData`
  instance exists anywhere in the development — so the mechanized composition is vacuous if the
  structure is uninhabited. It is inhabited (e.g. `k=3, n=1, R=2, P=12, Mv=24, cP=3`, an injective
  `enc` into `ZMod 325`: `k∣P` ✓, `2·25 = 7²+1` ✓, `R^{k−1}=4 ≤ 12 ≤ 3·4` ✓), so this is a gap in
  the *evidence*, not in the claim. `KSUM.A1` states its analogous gap explicitly; `KSUM.A2` does
  not. Recommend a `demoEmbed : EmbedData` witness, mirroring `demoModel`.

**Regime coverage (7b).** `k` odd vs `k` even: the coprimality argument branches exactly there
(odd prime `p ∣ k` uses invertibility of 2; `2 ∣ k` uses the mod-4 step) and both branches are
present in the Lean (`KSUM/A2.lean:121-150`), which runs them through `d = gcd(k, M+1) ∣ 2` plus
`d ≠ 2` rather than prime-by-prime. I re-derived both branches from the appendix before reading the
Lean; they agree. `R = 2` boundary: `ω = 3`, `P = k·(3^{k−1}−1)/2`, all fields still satisfied.
`k = 3`: `M = 24`, `M+1 = 25 ≡ 1 (mod 3)`, `P = 6R(R−1) ≡ 0 (mod 3)` — checked, and the
`SelfTest` negative control at `KSUM/SelfTest.lean:179` (`gcd(3, 3·25) = 3`) correctly shows the
statement fails without `k ∣ P`.

**Verdict: CONFIRMED-WITH-REPAIRS (R-A2-1 … R-A2-3).** The composition claim is correct and its
proof valid. With R-A2-1 and the `rel` repair of §6.2 applied I license **PROVED** on `KSUM.A2`'s
composition, hence `status(A2) = PROVED`. (R-A2-3 is an evidence gap on the Lean corroboration, not
a defect of the prose composition, and does not block the promotion.)

### 3.3 `KSUM.B2` — `A2 ∧ k3.donor ⇒ B2` — **CONFIRMED-WITH-REPAIRS**

**Diff against my worksheet (§2.3).** R1–R4 match the block. R5 (novelty) is present and correctly
identified as the premise "that is not bookkeeping", with the L2fC lesson attached — my worksheet
reached the same conclusion independently, including the placement question; I flag the coincidence
per 7c. The `rel` entry is well drafted. **R6 is missing**, and one type defect is new:

- **R-B2-1 (missing premise — the construction family, and the padding it needs).** The block says
  "the `kSum` bound is then `Ω(L(m,R))` with `N = km`", which is a statement about *one* `(N,q)` per
  `(m,R)`: `q` ranges over the discrete set `{q_k(R) = (P+1)(M+1)}` and `N` over multiples of `k`.
  Any reading of B2's output as "a lower bound on a `q`-window, for all `N`" needs a padding lemma
  in `N` and an interpolation/monotonicity argument in `q`, neither of which is on disk. The
  manuscript already states this restriction in the footnote to `rem:kclaw-composition` ("a
  family-only statement, with no padding to arbitrary `N` and no interpolation to moduli between
  construction points"), and the Lean `Claim` is honestly per-`EmbedData`, so this is a prose
  omission in a place where it matters: the goal-level route asks for a bound on a *range* of `q`.
  Promote it to a second `rel` entry.
- **R-B2-2 (type defect in the mechanized donor hypothesis).** `DonorClaim` (`KSUM/B2.lean:75-76`)
  quantifies `∀ k n R, 3 ≤ k → … → L n R ≤ Q(Coll k n R)`, i.e. a *single* bound function `L`,
  independent of `k`, valid for **every** `k ≥ 3` simultaneously. A donor for one fixed `k` — which
  is what `prob:donor` and `k3.donor` are about — does not instantiate it. As an antecedent this is
  the safe direction (it makes the mechanized `Claim` weaker), but it means the machine-checked
  transport does not cover the intended use. Index `L` by `k`, or fix `k` outside.
- **R-B2-3 (the child's Claim is not a proposition).** `k3.donor`'s frozen Claim is a statement of
  need ("needs a WALK-OPTIMAL … LB — no tight donor found"), so `A2 ∧ k3.donor ⇒ B2` has no truth
  value until it is replaced by the proposition it stands for. The composition block itself supplies
  the right one in its own words ("a walk-optimal small-range `k ≥ 3` `k`-collision detection lower
  bound"); freeze it as `∃ c ≥ (k−1)/(2(k+1)) : Q(Coll_{k,n→R}) = Ω(√n·R^c)` uniformly for
  `R = Θ(n)` — the threshold is the manuscript's own transfer calculus. Also define "walk-optimal"
  in the same place (7g): it resolves to `Q(Coll_{k,n→Θ(n)}) = Θ(n^{k/(k+1)})`, i.e. Tani's walk is
  optimal, per `prob:donor`.

**Regime coverage (7b).** The dangerous regime is exactly the one the `rel` names: donors valid only
at large `R`. I re-checked L2fC's arithmetic: `R = Ω(n²)` with `q = Θ_k(R^{k−1})` gives
`q = Ω_k(n^{2(k−1)}) = Ω_k(N^{2(k−1)})`, above `N^{k−1}`, where BS is already tight — correct, and
correctly cited. Small-`R` boundary `R = 2`: the transport is valid but the induced `q` is `O_k(1)`,
where the conclusion is empty; worth one clause.

**Verdict: CONFIRMED-WITH-REPAIRS (R-B2-1 … R-B2-3).** No status changes: `B2` stays **OPEN**
(`min(composition, A2, k3.donor)` with `k3.donor` OPEN). The composition *claim* may be promoted to
CERTIFIED\* once R-B2-1/R-B2-3 are applied — I decline PROVED on it because R-B2-3 means the claim
is not yet a proposition, and a proposition is a precondition for a completion tier.

### 3.4 `KSUM.B4` — `B4a ∧ B4b ⇒ B4` — **CONFIRMED-WITH-REPAIRS**

**Diff against my worksheet (§2.4).** S1–S4 coincide with the block almost word for word (the
two-parameter point and the `ε`-clause). **I flag this coincidence explicitly per 7c** — it is the
one place in this review where my independent list and the lead's are notationally the same, and the
reason is that both are forced by `B4a`'s shape. My S5 (same problem family) is absent, and checking
it at the boundary produced the finding below.

- **R-B4-1 (the mechanized sandwich is VACUOUS — 7b/§7.10(5)).** `B4bClaim` (`KSUM/B4.lean:66-69`)
  asserts `c·N^{1/2}·q^{1/4} ≤ Q(2Sum_{Z_q,t,N})` for **every** `q` with `NeZero q` and every `t`.
  At `q = 2, t = 0, N ≥ 3` the function is constant: values lie in `{0,1}`, pigeonhole gives `i ≠ j`
  with `x_i = x_j`, and `x_i + x_j = 2x_i = 0` in `Z_2`, so `2Sum ≡ true` and `Q = 0` in any
  faithful model, while the claim demands `c·√N·2^{1/4} > 0`. (`q = 1` fails likewise for `N ≥ 2`.)
  **So `B4bClaim` is not merely unmet — it is unsatisfiable, and the machine-checked composition is
  vacuous in the intended interpretation.** The node's own gloss, "`B4bClaim` is an unmet
  hypothesis, which is exactly the state of the node", is therefore inaccurate. The prose
  composition claim inherits the defect by not stating a `q`-range at all. **Repair:** restrict both
  the claim and `B4bClaim` to the non-degenerate window in which the exponent question lives — at
  minimum `q ≥ 5`, and per S5 the intersection of the two sides' scopes, `G = Z_q` with `q` odd and
  `N ≥ q`, since every registered `B4b` route (`M1` and the `L2` group) is stated for odd `q` with
  `N ≥ q` while `B4a` holds for all `q`. A sandwich between differently-scoped sides is not a
  sandwich.
- **R-B4-2 (define "matching"/"closed", 7g).** The block explains both terms well in prose; the
  frozen composition claim should carry the definition it argues for: "closed" = the two exponents
  agree in `N` and in `q` at the same `(N,q,t)`, up to `N^{o(1)}`.

**Regime coverage (7b), both `cor:threshold` cases.** Case 1 (`q ≥ N−1`) and Case 2
(`cN ≤ q < N−1`) both land inside `B4`'s window and both are covered by `B4a`; I independently
re-checked the T1 finding F6 while doing so and confirm it — in Case 2, `κ = ⌊(q−1)/2⌋ ≤ (N−3)/2 <
⌊N/2⌋ = n`, which is ABI's own range, so `thm:tani` is not needed there (`thm:main-odd` genuinely
does need it for `2n−1 < q ≤ 4n−1`). That is a manuscript strengthening, already on the T1 list.

**Verdict: CONFIRMED-WITH-REPAIRS (R-B4-1, R-B4-2).** No status changes: `B4` stays **OPEN**. With
R-B4-1 applied the composition claim may go to CERTIFIED\*; I decline PROVED while the mechanized
form is vacuous, because a vacuous corroboration is exactly what rule 7 tells a reviewer not to
launder into a completion tier.

---

## 4. PER-ITEM DETAIL — ROUTE MAPS AND THE PROPOSED KILLS

### 4.1 The claim-shape problem (7g), stated once because it conditions three verdicts

`KSUM.goal`, `KSUM.B1` and `KSUM.k3.donor` all have frozen Claims that are **not propositions**
(a target description, a strategy description, and a statement of need). The lead identified the
first two and correctly declined to invent them in Lean; I add `k3.donor`, which is load-bearing as
an AND input to `B2`. Consequence for this review: a route kill is a claim that *no* proof of
`B → GOAL` exists, and its truth depends on which proposition `GOAL` names. I rule under the reading
the route entries themselves presuppose — **(A) "prove `Ω(N^{k/(k+1)})` for fixed `k ≥ 3` at
alphabet size far below the Belovs–Špalek requirement"** — and I state the dependence in each
verdict rather than hiding it. If the lead ever freezes reading (B) ("determine `Q(N,k,q)` on the
whole middle range"), **both kills must be withdrawn**, since under (B) a floor is a partial answer
and finite exact values are evidence, not failure.

### 4.2 `goal.B1` — proposed kill — **KILL CONFIRMED (scoped; two mandatory repairs)**

*My own (b)-time analysis, before reading the entry:* a kill needs a **ceiling** on the route, not a
comparison of the currently proved value.

The entry argues: "B1's best output is the floor `Ω_k(√N q^{1/6})`, i.e. `Ω_k(N^{2/3})` at
`q = Θ(N)`, and `2/3 < k/(k+1)` for every `k ≥ 3` — the gap is intrinsic to the donor exponent
`1/6`, not the encoding." The arithmetic is right (`2/3 < k/(k+1) ⟺ 2 < k`), and "intrinsic to the
donor" is the right *idea*, but as printed the argument evaluates the bound at one point instead of
bounding the route. **Repairs required before REFUTED is written:**

- **K-B1-1 (cite the ceiling).** Add either (a) the range cap — the live block has
  `m = ⌊(N−(k−2))/2⌋ ≤ N/2` positions and `thm:abi`/`thm:tani` need `K ≤ 2m−1`, so
  `√m·K^{1/6} = O(N^{2/3})` for every admissible `(m,K)`; or, stronger and cleaner, (b) the donor's
  own upper bound `Q(Claw_{n→κ}) = O(n^{2/3})` for every range `κ`
  (Ambainis / Childs–Eisenberg — the manuscript already cites both for `cor:threshold`). With (b),
  **no** reduction whose live block carries a 2-wise problem on at most `N` coordinates can exceed
  `O(N^{2/3})`, which is what "intrinsic to the donor" means and what makes the route dead rather
  than unfinished (rule 3).
- **K-B1-2 (scope the verdict).** REFUTED applies to the **route entry** `B1 → GOAL` under reading
  (A), with disposition **DEAD** and the reason "donor-intrinsic ceiling `O(N^{2/3})` <
  `N^{k/(k+1)}` for all `k ≥ 3`". `KSUM.B1` itself stays **OPEN** and its floor stands — the entry
  already says this, correctly.

**7d — the `A1e` question the commission asks me to adjudicate.** The kill leans on `A1e`, a node at
**OPEN**. That is admissible here, but not as written. The content actually borrowed from `A1e` is
(i) a decidable arithmetic inequality and (ii) a value read off `A1d`, which is PROVED with an
archived independent review covering exactly that statement (`ksum/artifacts/ksum_rev2_review.md`). So
the borrowed content is covered at the granularity now used — but the kill should cite `A1d` +
the inequality directly rather than an OPEN node's label, and after K-B1-1 the ceiling (not `A1e`)
is what carries the kill. Separately, `A1e`'s **OPEN** status is itself a mis-typing: it is a
corollary of a PROVED node plus arithmetic, not an open obligation. Recommend `role: outcome`,
status **PROVED** (or CERTIFIED\* if the lead prefers), which also discharges rule 8d for it.

### 4.3 `goal.B3` — proposed kill — **KILL CONFIRMED (scoped to the registered routes)**

*My own (b)-time analysis:* the kill needs (a) every registered sub-route dead or non-asymptotic and
(b) the constraint that finite exact values cannot license a uniform exponent.

Both hold. `L31` is REFUTED·DEAD; `L32`/`L33` are exact `Adv±` computations at reachable `(n,q)`;
G11 forbids the exponent inference, and `L32a`'s own reviewed text records the exponent as
numerically undecidable, with `KSUM_STAGE0_VERDICT.md:61` making the quantitative case (a
G11-compliant 2× separation needs `n ≈ 256` at `q = 3`, where the matrix has `~3^n` columns). I add
a **second, independent** ground the entry does not use: `L32` and `L33` are `k = 2` solvers, while
GOAL is `k ≥ 3` — so even an unlimited-`n` solver of that kind would be answering a different
question. Two independent grounds is what makes this kill safe.

**Repairs required:** **K-B3-1** — G11 is a term of art (7g) that currently resolves only in prose
(`ksum/notes/KSUM_STAGE0_VERDICT.md:61,71` and the prover prompt). Two route kills now lean
on it; register it as a constraint (a clause on `KSUM.C0`, whose role is exactly "constraints that
prune ALL branches", or its own node) and cite that. **K-B3-2** — scope the verdict: REFUTED·DEAD on
the route entries `L32 → B3`, `L33 → B3` and `B3 → GOAL` **as registered** (finite exact
computation), explicitly *not* a kill of adversary-method approaches in general, which live under
`B4b.L1/L2/L3` and stay OPEN. Without K-B3-2 this reads as killing the adversary method, which the
disk does not support.

### 4.4 `KSUM.B3`'s internal route map — **KILLS CONFIRMED (L32, L33); L31 moot — CONFIRMED**

Same argument one level down, same two repairs. `L31`'s entry is correctly marked moot (child
REFUTED·DEAD ⇒ `min(child, route)` REFUTED regardless), which is the right application of §1. One
consistency note: with all three routes dead or moot, `B3`'s own status becomes REFUTED at the route
level while the node's NUMERICAL children keep their value. Record it as **REFUTED · PARKED**, not
DEAD — the three *route entries* are DEAD (the G11 obstruction admits no repair for a finite
computation), but the node stands for a class, and a route that is not a finite computation could be
registered under it later; per rule 4 the PARKED revival condition should be written down: *"an
adversary-value route that is analytic and uniform in `n` (a closed-form or asymptotic bound on
`Adv±`), rather than exact values at reachable `(n,q)`, and stated for `k ≥ 3`."* `L32`/`L33` are
untouched, and the recomputation must not walk further up: `GOAL` is an OR, so its `max` is
unaffected.

### 4.5 `KSUM.B4b`'s route map (L1/L2/L3) — **CONFIRMED**, with one factual correction

The three entries correctly record that **no route proof exists** for any of L1/L2/L3, and correctly
decline to mark them refuted. The `rel` on the L2 entry (the surviving candidate needs `≥3` active
pairs and must be non-product) is the right shape for an unresolved hypothesis. The observation that
PROVED obstruction children must not propagate to an OR parent whose claim is "close the window" is
correct and is the best-argued point in the route layer.

- **K-B4b-1 (factual correction).** The entry says L2's proved components "M1, M2, T4, VBUD, ORIENT,
  G1, G2, G3 — are all **obstruction** results". **M1 is not an obstruction**: `NODE_INDEX.md:19`
  types it `tool`, its claim is a positive construction (an `ℓ1 = 1` invariant measure annihilating
  every query polynomial of degree `< q−1`), and the manuscript calls `thm:pair-tensor` "an
  annihilation tool, not a cap-violating complexity statement". Two further PROVED components are
  also tools and are omitted from the list: `L2P3` and `BANDMULT` (`NODE_INDEX.md:20-21`). The
  correct reason the route is unwritten is sharper than "they are all obstructions": the tools
  supply **pure high degree** but not **correlation** — M1's tensor has correlation exactly
  `2^{1−r}`, below the `2/3` threshold the polynomial method needs — and the obstructions rule out
  the constructions that would have supplied correlation. Stated that way the entry says something
  true about all ten components and explains the frontier.

### 4.6 `KSUM.B1`'s internal route map — **CONFIRMED**

`L11`/`L12` moot (children REFUTED·DEAD). The `A1 → B1` entry correctly identifies that the blocker
is a defect in `B1`'s own Claim rather than mathematics; "X realizes strategy S has no truth value
until S is written as a claim" is exactly right and is the same defect as `KSUM.goal`'s and
`k3.donor`'s. Recommended rewrite in §7.4.

---

## 5. EDGE RE-TYPINGS

### 5.1 `A1e` `children → related` — **ENDORSE**

`A1e` is a caveat about what `A1` fails to reach; nothing in `A1`'s composition consumes it, and I
confirm by inspection of all four steps that no step uses it. Its work is at the `B1 → GOAL` route
entry, where it is now cited. The re-typing also removes a real anomaly (an AND node at PROVED with
an OPEN child), and the lead correctly declines to let that rescue the status. **Defect to fix in
the same diff:** `KSUM.A1e.yaml`'s front matter now reads `parents: []` / `related: [KSUM.A1,
KSUM.goal]`, but its prose "Dependencies" section still says "Parents: [KSUM.A1]" and "Related: none
recorded" (`KSUM.A1e.yaml:36-38`). The Mermaid is already correct (`A1 -.-> A1e`,
`KSUM_PROOF_DAG.md:1070`). Same defect on `A1f` (`KSUM.A1f.yaml:38-39`).

### 5.2 `A1f` `children → related` — **ENDORSE**

`A1f` is a certification record (a completed independent audit), not a mathematical input; it is
the *evidence* for other nodes' statuses. Under §1 it belongs in `related`. Note the substantive
sentence it carries — "Donor (ABI/Tani) still on trust" — is now also an explicit `rel` entry on
`A1`'s composition, so nothing is lost by the re-typing. Same prose-sync defect as §5.1.

### 5.3 `B4b.U1` `children → related` — **ENDORSE**

`U1` is a CERTIFIED\* *outcome*: a conditional certificate that a family of **upper-bound**
constructions cannot succeed within the `F_SC^charge` cost model. It is an obstruction, and its own
review already states it "does not close the global `q^{1/6}`-versus-`q^{1/4}` window". As an
OR-child of `B4b` it would have been a route that cannot discharge the parent's claim. Re-typing is
correct, and here the node file, the Mermaid (`B4b -.-> B4bU1`, `KSUM_PROOF_DAG.md:832`) and the
front matter agree — no sync defect. This also resolves the "known legacy ambiguity" recorded at
`NODE_INDEX.md:171-175`.

### 5.4 `goal → B4` edge type QUESTIONED — **ENDORSE re-typing to `related`**

GOAL is stated for fixed `k ≥ 3`; `B4` is the `k = 2` exponent window. There is no route proof
`k=2 ⇒ k≥3` on disk, none has been attempted, and none is plausible: the `k = 2` results rest on the
involution structure that `sec:k3` opens by saying is "gone" for `k ≥ 3`, and `KSUM.C0`(ii) records
that `k ≥ 3` alphabet symmetry is only `diag(Aff)⋊S_n`. A `children` edge asserts status
propagation that nothing supports. **Re-type to `related`.** Consequences the lead must apply in the
same diff: GOAL's `children` becomes `[B1, B2, B3]`; `B4`'s `parents` becomes `[]`; the root's `max`
is unaffected (it was `OPEN` on every route); and the Mermaid edge `G --> B4` becomes dotted. This
does not demote `B4` or `B4a` — it says the delivered `k=2` results are not a route to the `k≥3`
goal, which is what the manuscript already says.

### 5.5 `KSUM.B4b.L2.FILT → KSUM.B4b.L2.M1` — **ENDORSE `related`; do NOT make it a child** — and raise FILT

This is the adjudication the commission frames as "should it become a status-propagating CHILD of a
PROVED node?". The disk changes the question.

**The mathematics.** M1's claim ("annihilates every query polynomial of degree below `q−1`") does
genuinely consume the filtration: `thm:pair-tensor`'s proof ends "*Lemma `lem:factorial-filtration`
gives the query-polynomial statement*". Without it, M1 is a theorem about falling-factorial
occupancy rows, not about query polynomials — exactly as `KSUM.B4b.L2.FILT.yaml:28-30` says.

**The epistemics (rule 7d, applied to the review that would be leaned on).** M1's archived
independent review — `ksum/artifacts/ksum_L2p2_review.md`, a fresh hostile reviewer who "authored none of
the target work; no wanted verdict" — **re-derived the filtration bridge itself** (lines 74-83: the
`S_N`-averaged one-hot monomial is `∏_a (n_a)_{α_a}/(N)_m`; repeated same-position variables reduce
by idempotence; incompatible symbols vanish; hence the factorial rows span all query-polynomial
restrictions below the degree "without loss; no compressed-label polynomial degree is substituted")
**and finitely verified it against raw one-hot rows** (lines 95-106: 1,526 raw one-hot rows at
`(5,5,0)` and 22 at `(7,3,0)`, every residual exactly zero in `Fraction` arithmetic). So the
archived review's scope **does** cover the use M1 makes of FILT, at the granularity now in question.

**Ruling.** Keep the edge `related`. Making FILT a status-propagating child would recompute
`status(M1) = min(composition, FILT) = CONJECTURED`, demoting a node whose proof *of this very step*
is independently reviewed — a status regression unsupported by any evidence, and a violation of
rule 3's "do not over-kill" in its structural form. Instead: (a) record FILT on `M1` as a **cited
internal interface**, naming the review lines above, so the premise is not "hidden in prose" (§1's
actual requirement — it demands a child, a cited interface, *or* an explicit relative hypothesis,
and an interface is available here); and (b) **raise `KSUM.B4b.L2.FILT` from CONJECTURED to
CERTIFIED\***, citing `ksum/artifacts/ksum_L2p2_review.md:74-83,95-106`, with the caveat: *"reviewed as a
step inside the phase-2 M1 review, at the `S_N`-invariant odd-`q` pair-tensor use; the manuscript's
general statement (arbitrary `S_N`-invariant `μ`, arbitrary `α`, both directions of the iff) was
re-derived there but not itemized as its own claim; not mechanized — this is the gap behind
`thm:pair-tensor`'s NARROWER Lean verdict."* That is the honest tier: single review, partial scope,
which is exactly what CERTIFIED\* means. The recorded rule-8b breach (late registration) stands as
history and is not backdated.

---

## 6. THE THREE ADJUDICATIONS

### 6.1 `A1d` restates `A1` — **KEEP BOTH NODES; rewrite `A1`'s Claim; do not collapse**

Three reasons. (i) Stable ids are permanent references (structure protocol §3) and both ids are cited
across the manuscript, the Mermaid, the index and four Lean modules; collapsing would break cites for
no mathematical gain. (ii) The duplication is not vacuous — `A1d` is a *reviewed leaf* carrying the
2026-07-19 statement correction and its own review, while `A1` is the *composition obligation*; those
are different objects with different evidence, and the protocol explicitly wants the composition to
be separately reviewable. (iii) The right fix is to remove the *appearance* of duplication by making
`A1`'s Claim say what an AND node's claim should say. **Recommended `A1` Claim:** *"The frozen-core
reduction composes: `A1a` (core), `A1b` (live claw encoding) and `A1c` (target coverage), together
with `sec:prelim` facts (i)/(ii), the coordinate-freezing principle and the ABI/Tani claw bound,
yield `A1d`."* Then `A1d` stays the theorem, `A1` states the composition, and `KSUM/A1.lean`'s
`Claim := KSUM.A1d.Claim` can stay as the conclusion-mirror with a one-line note. **Do not** keep
`A1d` in `children` *and* as the conclusion without saying so: the composition claim reads
`A1a ∧ A1b ∧ A1c ⇒ A1d`, so `A1d` is the consequent, and listing it among the AND inputs is what
makes the arrangement look circular. Recommended: move `A1d` from `children` to a new explicit field
(or keep it in `children` with the node text stating it is the conclusion — the current text does
say this, which is why I rule this a presentation defect and not a circularity).

### 6.2 `gcd(k,q)=1` prose repair — **SCOPED REMOVAL from `rel`, not deletion**

**Is `KSUM.A2.coprime_k_q`'s derivation faithful to `lem:embed-allt`? YES.** I checked it line by
line against the appendix (7f: statement *and* proof correspondence verified by reading; the build
was not re-run — Step 4 forbids it, and `KSUM.LEAN.statement-fidelity` is the node that owns build
verification). `coprime_k_succ_of_dvd` is the paper's first sentence, done through `gcd ∣ P` and
`gcd ∣ P+1` instead of prime-by-prime — strictly cleaner, same content. `coprime_k_MvSucc` runs the
paper's two cases through `d = gcd(k, M+1)`: `d ∣ k ⇒ 2k+1 ≡ 1 (mod d) ⇒ (2k+1)^{k−1} ≡ 1 ⇒ d ∣
(2k+1)^{k−1}−1`, and `d ∣ M+1 ⇒ d ∣ 2(M+1) = (2k+1)^{k−1}+1`, so `d ∣ 2`; then `d = 2` forces `2 ∣ k`,
whence `2k+1 ≡ 1 (mod 4)`, `4 ∣ (2k+1)^{k−1}−1` and `4 ∣ 2(M+1)`, giving `4 ∣ 2` — contradiction.
That is the paper's odd-prime case and mod-4 case, merged. Both hypotheses (`k ∣ P`,
`2(M+1) = (2k+1)^{k−1}+1`) are properties of `lem:embed`'s formulas, so the fact is **forced by the
construction**, not assumed.

**Ruling.** Remove `gcd(k,q)=1` from `KSUM.A2`'s `composition.rel` and replace it — do not simply
delete the line — with: *"`gcd(k,q)=1` is not a hypothesis: for the constructed modulus
`q=(P+1)(M+1)` it is a theorem (`lem:embed-allt`; machine-checked as `KSUM.A2.coprime_k_q` from
`k ∣ P` and `2(M+1)=(2k+1)^{k−1}+1`, both read off `lem:embed`'s parameter display), and it was
already independently verified on 2026-07-19 (`KSUM.A2a.yaml:53-55`, `ksum/artifacts/ksum_rev2_review.md`).
It enters `A2`'s Claim as the all-targets clause."* **Two scope conditions, both mandatory:**
(a) the removal is valid **only** for the general recipe's modulus family `q = (P+1)(M+1)`; for the
`k = 3` tighter recipe of `rem:k3embed` at `q ≥ 21R²−8`, coprimality with 3 is a genuine hypothesis
("or at any larger modulus `q` with `gcd(3,q)=1`; without that coprimality condition the displayed
tags prove only the target-`0` statement") and must remain stated there; (b) the fact is consumed
**only** by `A2`'s own all-targets clause — `KSUM.B2`'s composition discards it
(`KSUM/B2.lean:108` obtains the transport at target `0` and drops the all-targets conjunct), so no
downstream node depends on it. Recording (b) prevents a later reader from thinking B2 inherits an
all-targets guarantee it does not use.

### 6.3 `A2b` dual-status split — **SPLIT ENDORSED**, in the form the Lean already uses

`A2b`'s Claim carries "[PROVED + NUMERICAL]", and §2 gives a node one status. Recommendation:
`A2b` keeps status **PROVED** for the general balanced-base-`ω` exclusion of every wrong block
multiset — that is the argument the reduction consumes and it is what `KSUM/A2b.lean`'s `Claim`
renders — and the 62,140 exhaustive checks move into the Evidence section as **NUMERICAL**
corroboration with their command/log/SHA provenance, explicitly *not* part of the Claim. This is
what the Lean module already did (`KSUM.A2b.yaml:54-60`), so the prose is the only thing out of sync.
Do **not** create a second node: the checks are evidence for one claim, not a separate claim (rule 8b
registers *ideas*, not evidence files). Same treatment is owed on `A1a`'s "[both variants
F1-verified]" and `A1f`'s embedded audit narrative, though those are less acute.

---

## 7. THE TWO STRUCTURAL DEBTS, AND THE `B1` CLAIM REWRITE

**Reported conflict, repeated here because it changes the shape of the answer:** the commission says
`KSUM.k3.donor`, `KSUM.L32` and `KSUM.LEAN` have **no** composition blocks. All three have one on
disk. What is missing is a route *proof* on three of the five entries (`proof: "none"`). I therefore
answer both readings: what each block should say, and what is wrong with what is there.

### 7.1 `KSUM.k3.donor` (OR, three route entries) — **CONFIRMED-WITH-REPAIRS**

One sentence per route, as the block should read:

- **`zhang-tani → k3.donor`:** *"The Zhang/Tani-composable donors imply `k3.donor`"* — **and this is
  a kill, not an open route**: the reviewed donor-cap `L2d` gives `c ≤ min{1/2, (k−1)/(2θ(k+1))}`,
  which at `R = Θ(n)` is below the walk-optimal exponent the parent's claim requires, so the entry
  should be presented for rule-6 confirmation as `REFUTED·PARKED` (parked, not dead: it revives if a
  stronger composition is found — which is what the current `reason` already says in words) rather
  than sitting at OPEN with a kill argument in a `reason` field. I do **not** confirm this kill in
  this review: it was not in my commissioned scope, `L2d`'s cap involves a `θ` whose definition I
  did not audit, and rule 2 forbids me from killing on a reading rather than a check.
- **`dream → k3.donor`:** *"A walk-optimal small-range `k`-collision lower bound implies `k3.donor`;
  the route proof is the identity, since the dream donor **is** the parent's claim specialized to an
  explicit construction — so the whole content of this route is the existence of the donor, which is
  `prob:donor`."* The current entry says this and is correct.
- **`L2c → k3.donor`:** *"Moot: the child is REFUTED·DEAD (large-alphabet-only `q ≥ Ω(n²)`,
  non-range-symmetric), so `min(child, route)` is REFUTED regardless."* Correct as written.

**Precondition for all three (R-B2-3):** `k3.donor`'s own Claim must first become a proposition —
`∃c ≥ (k−1)/(2(k+1)) : Q(Coll_{k,n→R}) = Ω(√n·R^c)` for `R = Θ(n)`, fixed `k ≥ 3` — with
"walk-optimal" defined as `Q(Coll_{k,n→Θ(n)}) = Θ(n^{k/(k+1)})` per `prob:donor`. Until then no
route proof into it can be stated.

### 7.2 `KSUM.L32` (OR, one route entry) — **ENDORSE the re-typing it proposes**

The single entry says the `L32 → L32a` edge is mis-typed: `L32a` ("exponent numerically undecidable
at reachable `n`") is an **outcome of `L32`'s runs**, not an input to `L32`. I confirm — the child's
own Claim describes what `L32`'s solver produced. What the block should say, in one sentence:
*"`L32` has no status-propagating children; its NUMERICAL status rests on its own runs, and `L32a`
is the outcome of those runs, recorded as `related`."* **Apply the re-typing**, and then re-kind
`L32` from `OR` to `LEAF` — an OR node with no children cannot have a route, and the `kind` field
should not advertise one. This also discharges the "known legacy ambiguity" at `NODE_INDEX.md:170`
("`L32` is NUMERICAL while its drawn child `L32a` is OPEN"), which was recorded there precisely
because it could not be resolved without this adjudication.

### 7.3 `KSUM.LEAN` (AND, one composition claim) — **REJECTED; repair required**

The defect is stated at the top of this review: the inline scope-census is false, so the composition
claim `T1 ∧ T2 ∧ T3 ∧ fidelity ⇒ LEAN` does not hold. What the block should say, in one sentence:
*"`T1 ∧ T2 ∧ T3 ∧ statement-fidelity ⇒ KSUM.LEAN`, where the conjunction is definitional and the
**only** mathematical content is the scope identity `targets(T1) ∪ targets(T2) ∪ targets(T3) = {paper
theorems that are neither imported citations nor quantum-algorithmic constructions}`, to be
discharged by an itemized census table (LaTeX label → tier → module → state) that does not yet exist
on disk."* Concretely the lead has three options, and should pick one explicitly rather than leave
the census implicit: (a) **write the census and add the missing tiers/nodes** for `lem:embed`
+`prop:embed`+`lem:embed-allt`+`rem:k3embed`, `prop:kclaw-fillers`, `prop:kclaw-coloring`,
`prop:rosmanis`(2)(3), `rem:torsion`, plus `FILT` and `JOINTLP`; (b) **narrow the parent's Claim**
to the theorems the three tiers actually target, and say so in the Claim rather than in a census
nobody can check; or (c) add a fifth child covering the remainder. Additionally, register the
2026-07-30 `KSUM/` DAG-mirroring layer somewhere in this AND — at present the composition tier under
review here is not accounted for by the node that is supposed to account for the audit.

### 7.4 The `KSUM.B1` Claim rewrite, in one sentence

*"For every fixed `k ≥ 3` there is a frozen-coordinate reduction — a core of `k−2` coordinates (plus
one parked coordinate when `N−(k−2)` is odd) together with the `k=2` claw encoding on the `2m` live
coordinates — such that `Q(kSum_{Z_q,t,N}) = Ω(Q(Claw_{m→K}))` for every target `t`, every
`K ≥ 2` and every `q ≥ (k²−2)K+2k−1`."* (That is a proposition, it is exactly what `A1` delivers, and
it makes the route entry `A1 ⇒ B1` statable — indeed near-trivial, which is the honest state of that
edge. The same treatment turns `KSUM.goal`'s Claim into reading (A) and `k3.donor`'s into §7.1's
proposition; all three are the lead's mathematical decision, not an executor's or a reviewer's.)

---

## 8. RULE-7 COMPLIANCE RECORD

- **7a — type/quantifier audit per composition.** Done per item: A1 (§3.1: quantifier order of
  `A1d.Claim` checked term by term — `∀k ∃C_k,c_k,A,B,N₀ ∀N,q,t`, with all constants depending on
  `k` only; the `k−2 ≤ m ≤ k−1` widening of `A1a`; the all-pairs quantifier in `A1c.Claim`); A2
  (§3.2: `∀ EmbedData`, the per-instance modulus conjunct, the branch structure of the coprimality
  proof); B2 (§3.3: `DonorClaim`'s `∀k` binding the single `L`); B4 (§3.4: both bounds under one
  shared `∀(N,q,t)` — correct — and the unrestricted `q` that makes it vacuous). Every premise was
  traced to a child, a cited interface, or an explicit `rel`; the ones that were in prose only are
  R-A1-1, R-A1-2, R-B2-1, R-B4-1.
- **7b — regime coverage.** `k=3` vs large `k` (§3.1); `q` odd vs even (§3.1 for `k≥3`, §3.2 for the
  `2∣k` branch); `m ∈ {k−2,k−1}` (§3.1, R-A1-1); both `cor:threshold` cases (§3.4, including an
  independent re-check of finding F6); boundary `q = q₀(k)`, `R = 2`, and `q ∈ {1,2}` — the last of
  which produced the vacuity finding R-B4-1.
- **7c — anchoring ban.** §2 was written from the children's frozen Claims and the manuscript only,
  using line-ranged reads that excluded every parent's `composition:` front matter and
  `## Composition proof` / `## Route proofs` section, and was not edited afterwards. Two notational
  coincidences with the lead's lists are flagged where they occur (§3.4 for B4's two-parameter/`ε`
  clauses; §3.1/§3.3 for the freezing principle and the novelty condition).
- **7d — no frozen-input immunity.** Three archived reviews were re-opened for scope, not
  re-reviewed: `ksum/artifacts/ksum_rev2_review.md` (does it cover `A1d`'s statement as used in the B1
  kill? yes — §4.2); `ksum/artifacts/ksum_L2p2_review.md` (does it cover the filtration bridge at the
  granularity M1 now needs? yes, with the exact lines — §5.5); `A1e`'s OPEN status against its
  load-bearing use (§4.2 — admissible, but the kill must cite `A1d` + arithmetic, and after the
  required ceiling repair `A1e` is no longer load-bearing).
- **7e — standing failure-mode list.** Dropped normalization: checked the factor-2 accounting in A1
  (encoding + two translations, absorbed in `Ω_k`) and A2 (single relabeling). Type/dimension
  mismatch: R-A1-4 (`n,κ` vs `m,K`). Undefined terms: 7g below. Quantifier drift: R-A1-3, R-B2-2.
  Smuggled hypotheses: R-A1-1, R-A1-3 — both in the direction that makes a composition assume more
  than its child gives. Numerics validating values while the derivation is broken: A2b's 62,140
  checks and A1a's F1 sweeps are corroboration only and are so labelled (§6.3).
- **7f — value-vs-formula / statement correspondence.** Where I cite Lean, I verified **statement
  correspondence by reading the source** (`A1a`, `A1c`, `A1d`, `A1`, `A2a`, `A2`, `B2`, `B4`, `B4a`,
  `Interface`, `Support/Freeze`, `Support/Embed`, `goal`) and, for `coprime_k_q`, the **proof** as
  well. **I did NOT reproduce the build**: no `lake` was run (Step 4 forbids it), so every claim here
  about "machine-checked" is a claim about what the source says, taken together with the
  lead-recorded exit-0 build; reproducing the build and running `#print axioms` belongs to
  `KSUM.LEAN.statement-fidelity` and remains owed. Where I state mathematics (the `K`-arithmetic of
  §3.1, the `q ∈ {1,2}` degeneracy of §3.4, `2/3 < k/(k+1)`, the F6 range check), I derived it
  myself; no verification script was run and none is claimed.
- **7g — terms of art.** Resolved: "exact reduction" (§3.2 step 3, = the pointwise iff);
  "query-free" (§3.2, = one simulated query per query, fact (ii)); "matching"/"closed" (§3.4, up to
  `N^{o(1)}` in both parameters); "hard class" (resolves on `KSUM.B4b.L2`'s reviewed phase-5 scope).
  **Unresolved and flagged:** "walk-optimal" (used in `B2`'s and `k3.donor`'s claims; resolves only
  via `prob:donor`, and must be written down — §7.1); "G11" (carries two route kills; resolves only
  in prose — K-B3-1); "GOAL", "B1", "k3.donor" as propositions (§4.1); "block label" in
  `thm:block-obstruction` (already on the T3 list as F-T9, repeated here because `B4b`'s route map
  leans on the obstruction group).

---

## 9. SUMMARY — WHAT CHANGES WHEN THESE VERDICTS ARE APPLIED

The layer is in much better shape than its own demotions suggest: the two central composition claims
(`A1`, `A2`) are correct, their proofs are valid, and both are one bookkeeping repair away from
restoring PROVED. The single wrong claim is in a block the commission did not think existed —
`KSUM.LEAN`'s scope census — and it is caught before it could discharge anything. Applying this
review: **`KSUM.A1` composition CONJECTURED → PROVED** (after R-A1-1 and R-A1-3, which are edits to
`A1a`'s and `A1c`'s frozen Claims, not new mathematics), **hence `KSUM.A1` CONJECTURED → PROVED**;
**`KSUM.A2` composition CONJECTURED → PROVED** (after R-A2-1 and the §6.2 `rel` repair), **hence
`KSUM.A2` CONJECTURED → PROVED**; **`KSUM.goal`'s `B1` route entry OPEN → REFUTED·DEAD** (after
K-B1-1's ceiling citation, under goal-reading (A)); **`KSUM.goal`'s `B3` route entry, and
`KSUM.B3`'s `L32`/`L33` route entries, OPEN → REFUTED·DEAD** (after K-B3-1/K-B3-2), which makes
**`KSUM.B3` OPEN → REFUTED·PARKED** (with the written revival condition of §4.4) while `L32`/`L33`
keep their NUMERICAL values;
**`KSUM.goal` `children` loses `B4`** (re-typed `related`), so `B4`'s `parents` becomes empty;
**`KSUM.B4b.L2.FILT` CONJECTURED → CERTIFIED\*** with the scope caveat of §5.5, and its edge to `M1`
stays `related` so **`M1` keeps PROVED**; **`KSUM.L32` re-kinded OR → LEAF** with `L32a` re-typed
`related`; **`KSUM.A1e` re-typed `role: outcome`, OPEN → PROVED**; and **`KSUM.LEAN`'s composition
status CONJECTURED → REFUTED** until its census is repaired or its Claim narrowed. `KSUM.B2` and
`KSUM.B4` compositions may go to **CERTIFIED\*** but not PROVED (§3.3, §3.4). **The root stays
OPEN**, and after these changes it is OPEN on exactly one live route — `B2`, blocked on the single
named donor — with two routes refuted, one re-typed away, and no endpoint moved.

---

## 10. RECEIPT (to be completed by the lead, rule 8c)

- Review completed and archived: 2026-07-30, this file.
- Read by the lead on: 2026-07-30 (same session, rule 8c); verdicts applied on: 2026-07-30 —
  A2→PROVED (+R-A2-1, §6.2); A1 stays CONJECTURED with R-A1-2/R-A1-4 applied and R-A1-1/R-A1-3
  queued behind the in-flight T2 executor (which owns A1a/A1c; it was messaged mid-flight not to
  prove the refuted all-pairs A1c.Claim); goal.B1/goal.B3/B3.L32/B3.L33 routes REFUTED·DEAD with
  K-B1-1/K-B3-1/K-B3-2 applied; B3 REFUTED·PARKED with the §4.4 revival condition; G11 registered
  (CERTIFIED*, K-B3-1); FILT→CERTIFIED* with the §5.5 caveat + M1 interface note; A1e→PROVED
  outcome; A1e/A1f prose-deps synced; L32 re-kinded LEAF with L32a related; B2/B4 compositions
  →CERTIFIED* with caveats (B4's mechanized vacuity R-B4-1 flagged, Lean fix queued); B4b K-B4b-1
  correction applied; B1 Claim rewritten per §7.4; KSUM.LEAN composition REFUTED per §7.3 with
  Claim narrowed (lead option (b)). Deferred behind T2 (shared files / lake build): goal→B4
  re-typing, B4.lean q-range fix, R-A1-1/R-A1-3 claim repairs + A1 composition re-close, the
  "Most recent change" header block. Views synced same-day: node files + NODE_INDEX + Mermaid +
  outline; validator 141 nodes OK.
- Files this review says must change when applied: `KSUM.A1.yaml`, `KSUM.A1a.yaml`, `KSUM.A1c.yaml`,
  `KSUM.A1e.yaml`, `KSUM.A1f.yaml`, `KSUM.A2.yaml`, `KSUM.A2b.yaml`, `KSUM.B1.yaml`, `KSUM.B2.yaml`,
  `KSUM.B3.yaml`, `KSUM.B4.yaml`, `KSUM.B4b.yaml`, `KSUM.goal.yaml`, `KSUM.k3.donor.yaml`, `KSUM.L32.yaml`,
  `KSUM.L32a.yaml`, `KSUM.LEAN.yaml`, `KSUM.B4b.L2.FILT.yaml`, `KSUM.B4b.L2.M1.yaml`, plus the four Lean
  modules named in R-A1-1/R-A1-3/R-B2-2/R-B4-1 and the manuscript repairs already on the T1/T3 lists.
- Nothing in this review was written to any of those files by me: this artifact is the only file I
  created or modified, and no `lake` build, validator, or `git` command was run.

---

`COMPOSITION REVIEW: A1 CONFIRMED-WITH-REPAIRS | A2 CONFIRMED-WITH-REPAIRS | goal.B1-kill KILL CONFIRMED (scoped, 2 repairs) | goal.B3-kill KILL CONFIRMED (scoped) | B3.L32/L33-kills KILL CONFIRMED / KILL CONFIRMED | B2 CONFIRMED-WITH-REPAIRS | B4 CONFIRMED-WITH-REPAIRS (mechanized form VACUOUS) | B4b-routes CONFIRMED (one factual correction: M1 is a tool, not an obstruction) | retypings A1e ENDORSE / A1f ENDORSE / U1 ENDORSE / B4-edge ENDORSE (re-type to related) / FILT ENDORSE related + raise to CERTIFIED* | A1d-dup KEEP BOTH, rewrite A1's Claim | gcd-repair SCOPED REMOVAL from rel (derivation faithful; scope: q=(P+1)(M+1) only) | PLUS ONE WRONG CLAIM FOUND: KSUM.LEAN's composition scope-census is false — REJECTED | statuses to change on apply: A1 composition→PROVED, A1→PROVED, A2 composition→PROVED, A2→PROVED, goal.B1 route→REFUTED·DEAD, goal.B3 route→REFUTED·DEAD, B3.L32/L33 routes→REFUTED·DEAD, B3→REFUTED·PARKED, goal→B4 edge children→related, B4 parents→[], FILT→CERTIFIED*, A1e→PROVED (role: outcome), L32 kind OR→LEAF + L32a→related, KSUM.LEAN composition→REFUTED (until census repaired); B2/B4 compositions eligible for CERTIFIED* only; root stays OPEN`
