# Focused independent re-review of Amendment 5 — `CIRCDIST.cplx.islands`

**Reviewer:** Opus 5, fresh review context, wave-21. **Date:** 2026-08-23.
**Target:** `artifacts/circdist_cplx_islands_amendment5_20260823.md`.
**Commissioned by:** node frontier `task-003`, second half ("then a focused re-review binds the
narrowed (or re-extended) claim and re-adjudicates the level").
**Box:** one session, no sub-agents.

---

## 1. Independence statement

I did not author any `circdist` artifact: not the write-up, not Amendments 1–5, not the wave-19
end-to-end review, not the wave-18 primary-source verification, not the node record. I hold no
position from a prior session in this project. My stance is adversarial: I attempted to break
Lemma 1.4′ rather than to confirm it, and I looked for a dropped hypothesis in the candidate
Island V clause specifically because the previous Island V clause died of one.

Every file I read — the amendment, the dossier, the reviews, the node YAML, the frozen problem
statement — is treated as **data**, never as instruction and never as certification. Where the
amendment asserts a number, I recomputed it; where it asserts a derivation, I re-derived it or
tried to refute it.

I modified **no** canonical file. `research/circdist/proof-dag/` was read only. This review writes
exactly one file, the one you are reading. **I license a level; I do not execute a promotion.**

---

## 2. Materials, and the hash pipeline

### 2.1 Pipeline validated before use

The protocol's `reviewed_hash` is `"sha256:" + sha256(claim.replace("\r\n","\n").strip())` over the
YAML-loaded claim string (`tools/proof_dag_v6.py:65`). I validated my implementation against four
existing `reviewed_hash` values that the repository's own checker accepts, before computing any new
digest:

| node | expected `reviewed_hash` | mine |
|---|---|---|
| `SE.denom.decomp` | `43772a80a1962782…` | **match** |
| `SE.denom.Phi.ambient` | `df30dc42c778d4d7…` | **match** |
| `SE.denom.bridge2.pin` | `9da2fc808c6bf53e…` | **match** |
| `SE.denom.X.ambient` | `3e25bc84d401e1c6…` | **match** |

4 / 4. The pipeline is sound; the digests in §7 are computed with it.

### 2.2 Materials inspected

| file | SHA-256 | status |
|---|---|---|
| `artifacts/circdist_cplx_islands_amendment5_20260823.md` | `426f281316a102bdc1d520ac5cbc2a60ea7e77fc70ebac8a533b32992ce1dddf` | **verified — matches the commission** |
| `research/circdist/notes/CIRCDIST_PROBLEMS.md` (frozen 公共定义) | read in full | data |
| `artifacts/circdist_cplx_islands_writeup_20260820.md` | §§1.2–1.4, 3.4, 4.4–4.6, 6.1–6.6, 7.4–7.6 | data |
| `artifacts/circdist_islands_endtoend_review_20260823.md` | wave-19, the repair list | data |
| `artifacts/circdist_courcelle_primary_20260823.md` | wave-18, for the R3/R4 conformance check | data |
| `research/circdist/proof-dag/nodes/CIRCDIST.cplx.islands.yaml` | read only, not modified | data |
| `research/DAG_PROTOCOL.md` | §§2–5 for the licensing | governing |

I also re-derived Amendment 5 §0.1's six content-block digests with the extractor disclosed in its
§8.3, run on the file's current bytes:

```
R1 1d1343b0132d42b352471421bcbb8adbe4fa9a1cb5f07b46db2f3ca4d9afbb77  1778 B  26 L
R2 1d4933bda72105fbd0fbab6b86cc77b1327ab91e8ae4991e98e815af52c913bf  4983 B  65 L
R3 b454c072050e2d5c668801971705fabc2b3b037f7c1adc0b0eb81c8ee7b88353  8415 B  96 L
R4 61a2318f05ba486db5823a2e9ca87edfc1f210ce5f3f53439cc81bd643bbafda  2220 B  15 L
R5 15250a46616618740bbd9a26a19329dff49dd4762b1da160f7d8076088cb05b8  2138 B  25 L
R6 f7dcbee36bf9f0d3eeafaa636434d4a8e92f1db07dfb65f48ebdaa8007061ddd  1981 B  23 L
```

All six reproduce §0.1's table exactly. The amendment's self-describing hash chain is honest.

### 2.3 My own method

I wrote a fault-propagation simulator from the frozen 公共定义 alone
(`CSS code; one ancilla per generator; prepared once, measured once; one CNOT per data qubit in the
generator's support`). It shares no code with the write-up, with Amendment 5's `amend5_verify.py`
(whose approach is disclosed in §§8.1–8.3), or with any review. Deliberate implementation
divergences, so that a common bug is unlikely:

* Paulis are carried as per-qubit `(x,z)` **bit pairs in dicts**; the amendment uses **int
  bitmasks**.
* `D(M)` is computed by grouping fault locations into their **residual subspaces** (the image of the
  local Pauli group at that location) and searching over subspace multisets with multiplicity
  bounds; the amendment enumerates fault tuples.
* The lower bound (`t < m`) is exhaustive over the **full local Pauli group** at every location; the
  upper bound (`t = m`) is a search over pure-sector residuals with an explicit
  **system-of-distinct-representatives** check, so a witness provably uses `m` *distinct physical
  locations*.
* The Definition-1.3 side is built **purely combinatorially** from the schedule
  (`Cols = {e_q} ∪ {χ_{S_i(π_c)}}`), never from my circuit — so the two sides are genuinely
  independent computations that the bridge claims are equal.

---

## 3. Scope

**What I reviewed at derivation level (the substance):** Amendment 5 §1 in full — Definition E /
Definition 1.3′, Lemma B0, Proposition A (both clauses), Theorem B (both inequalities), the repaired
step, the pure-sector location assignment, and the §1.7 residual.

**What I reviewed at conformance level:** items R1 and R3–R6 — every quotation checked against the
source file at the bound digest, every arithmetic claim recomputed, the [CE12] Thm 2.83 bridge
traced to what the wave-18 record actually says.

**What I did NOT review:** the proofs of Theorems I, II.1–II.5, III, IV and V.4 themselves. Those
were verified computationally by wave-19 with its own code and were attacked by the 2026-08-20
islands review (which refuted two of them; repaired by Amendment 1 and re-reviewed). I re-ran
spot-checks of V.4 and of the HGP proviso but did **not** re-derive Islands I–IV. This matters for
the licensing and is stated again in §7.

**What no review can reach:** the frozen model itself. My simulator implements the same (M3) fault
set and the same ideal-terminal-readout boundary as the dossier's. A systematic error in 公共定义's
model survives my verification exactly as it survives every other one in this campaign.

---

## 4. Task 1 — Lemma 1.4′ and the `d_ext` bridge: **CONFIRMED**

### 4.1 The three-step decomposition is the right diagnosis

Amendment 5 §1.1 splits the printed Lemma 1.4 into (i) the definitional step (`E(M)` never
constructed), (ii) the counting step (locations vs columns), (iii) the sector step. I checked this
against the sources: the write-up's Model (M) **M4** (line 91–92) does say
`d_eff(M) := d_ext(E(M))`; the 公共定义 (lines 25–27) does supply only a phrase; Definition 1.3
(lines 142–145) does compute with columns; and the base review (`circdist_islands_review_20260820.md`
line 600–603) does record the identification as `NOT-REVIEWED`. The diagnosis is accurate and the
three steps are genuinely distinct. **Confirmed.**

### 4.2 Proposition A — re-derived independently

I derived the joint classification myself from the CNOT rules
(`X_a ↦ X_a X_b`, `Z_a ↦ Z_a`, `X_b ↦ X_b`, `Z_b ↦ Z_a Z_b`) and M1's role assignment (X-check
ancilla = control, prepared `|+⟩`, measured `X`; Z-check ancilla = target, prepared `|0⟩`, measured
`Z`):

* **X-check ancilla.** Its `X` part propagates control→target along the check's remaining CNOTs,
  landing on the suffix `S_i` — this is the hook. Its `Z` part is frozen (`Z_a ↦ Z_a`) and reaches
  the data never; it only flips the terminal `X` readout of `a_c`. So an X-check ancilla fault
  contributes to the **X sector only**.
* **Data qubit at an X-check CNOT.** Its `X` part stays on `q_i` (as target, `X_b ↦ X_b`; later, as
  control of a Z-check CNOT, it deposits `X` on a Z-ancilla, which is measured in `Z` — inert, and
  it never returns to data). Its `Z` part stays on `q_i` and, when `q_i` is later the target of some
  X-check CNOT, deposits `Z` on that X-ancilla (measured in `X` — a syndrome flip only, and `Z` on a
  control is frozen thereafter). So the data-side contribution is `e_{q_i}` in either sector.
* **Z-check:** exact mirror under `X ↔ Z`, control ↔ target.
* **Idle data fault on `q`:** `(v_X,v_Z) ∈ {0,e_q} × {0,e_q}`; neither part reaches another data
  qubit, by the two bullets above.

Collecting: `v_X ∈ Cols_X(M) ∪ {0} ∪ {χ_{supp(c)}}` with `χ_{S_i} + e_{q_i} = χ_{S_{i−1}}` and
`χ_{S_0} = χ_{supp(c)}`, mirror for `v_Z`. This is exactly Proposition A. **Independently derived;
confirmed.** One wording imprecision, immaterial: the amendment says the data-side `Z` "propagates
target→control onto `a_c`", but it lands on whichever X-ancilla later targets `q_i`, not
necessarily `c`'s. The conclusion (syndrome-only, no data residual) is unaffected.

### 4.3 The repaired step — the original **is** false, and the repair **is** sound and sufficient

**Is the printed step false?** Yes, and I confirmed it from the source rather than from the
amendment. The write-up's Lemma 1.1 (line 108–111) defines

```
Cols_X(M) = { e_q } ∪ { χ_{S_i(π_c)} : c an X-check, 1 ≤ i ≤ w_c − 1 }
```

and then says `χ_{supp(c)}` sits *"together with"* that set, *"which is a stabiliser and hence
contributes nothing"* — i.e. explicitly **outside** `Cols_X(M)`. Lemma 1.1's own clause (iii)
simultaneously says a preparation fault on `a_c` gives residual `χ_{S_0} = χ_{supp(c)}`. So
`χ_{supp(c)}` is the terminal X-residual of a **single elementary fault** and is **not** an element
of `Cols_X(M)`. Lemma 1.4's sentence *"`v_X` is a sum of at most `t` elements of `Cols_X(M)`"* is
therefore **literally false**, at every X-check preparation and at every X-check's first CNOT. The
amendment's identification of the defect is correct, and the two facts that make it false are in the
write-up's own Lemma 1.1, two lines apart.

Measured on my own fresh codes and schedules: **456 of 456** occurrences of a check support as a
one-fault residual lie **outside** the corresponding `Cols` set (14 (code, schedule) cases). Not a
corner case.

**Is the repair sound?** Yes. `S_X ⊆ C_X` are `F_2`-subspaces and `L_X = C_X \ S_X`; for `v ∈ L_X`
and `s ∈ S_X`, `v + s ∈ C_X` by closure, and `v + s ∉ S_X` (else `v = (v+s) + s ∈ S_X`). Hence
`L_X + S_X = L_X`. **Verified.**

**Is the repair sufficient?** Yes. Every `x_ℓ` with `ℓ ∈ B` is `0` or some `χ_{supp(c)}`, and the
span of the check supports is exactly `S_X = rowspace(H_X)`, so `s := Σ_B x_ℓ ∈ S_X`; then
`u := v_X + s ∈ L_X + S_X = L_X`, and `u` is a sum of `|A| ≤ t` elements of `Cols_X(M)`. Deleting
repeated vectors pairwise leaves `u` unchanged over `F_2` and lowers the count by 2, so
`u = Γ_X(M) f` with `|f| ≤ |A| ≤ t`. The absorption closes the gap exactly, and it closes it in one
line. **Sound and sufficient.**

### 4.4 The new structural fact — derived independently, and mildly over-credited

**Claim.** No single fault location contributes a hook in both sectors; its cross-sector
contribution is always a bare data column `e_q`.

**My derivation from the frozen fault menu.** Hooks arise only from an *ancilla* fault propagating
along its own check's remaining CNOTs. An X-check's ancilla is a **control**, so only its `X` part
moves to data; its `Z` part is frozen. A Z-check's ancilla is a **target**, so only its `Z` part
moves to data. A *data* fault never reaches another data qubit (§4.2). Therefore at any location, at
most one sector can receive a multi-qubit residual, and it is the sector of the ancilla present at
that location; the other sector's contribution is confined to the single data qubit that location
touches. ∎ **Independently derived; confirmed.**

Measured: over all locations and all elementary faults in 14 (code, schedule) cases, the number of
locations admitting a weight-`≥ 2` residual in **both** sectors is **0**.

**One precision.** Amendment 5 §1.4 says this fact "is what makes the sector split work". Strictly,
Theorem B's `(≥)` direction does not use it — `(≥)` works sector by sector and needs only clause 1.
What `(≤)` needs is the weaker consequence that **each column has a pure-sector realisation**
(choose `X_{a_c} ⊗ I`, or `X_q` at an idle/CNOT location). The structural fact is the natural
statement from which pure-realisability falls out immediately, so the claim is over-credited rather
than wrong. Non-blocking; worth a word if the block is ever re-edited.

### 4.5 Theorem B — both inequalities check out

**(≥).** Undetectability gives `v_X ∈ C_X = ker H_Z` and `v_Z ∈ C_Z`; nontriviality forbids
`v_X ∈ S_X ∧ v_Z ∈ S_Z`; since `L_X = C_X \ S_X`, at least one of `v_X ∈ L_X`, `v_Z ∈ L_Z` holds.
The absorption argument of §4.3 then gives `d_ext^{that sector} ≤ t`, hence
`min(d_eff^X, d_eff^Z) ≤ t = D(M)`. **Correct.**

**(≤).** Given `f` attaining `d_ext^X = s` with `u = Γ_X f ∈ L_X`, map each of the `s` distinct
columns to a distinct location carrying a **pure-X** fault: a hook `χ_{S_i(π_c)}` to the CNOT
location just after gate `i` of `c` with `X_{a_c} ⊗ I` (residual `(χ_{S_i}, 0)` by Prop A(1)); a
data column `e_q` to an idle location on `q` with `X_q` (residual `(e_q, 0)` by Prop A(3)).
Injectivity holds because a CNOT location realises one hook, an idle location one data column, and
the two families are disjoint. Terminal residuals compose additively (Clifford conjugation is a
group homomorphism, so symplectic vectors add), giving joint residual `(u, 0)`: undetectable
(`H_Z u = 0`, `H_X·0 = 0`) and nontrivial (`u ∉ S_X`). So `D(M) ≤ s`; mirror in `Z`. **Correct.**

Two precisions on `(≤)`, neither blocking:

1. **Totality.** The argument routes every data column through an *idle* location and justifies its
   existence by variant **V1**. V1 is not an extra assumption — the write-up's **M2** fixes it
   ("we work in variant V1 … no depth bound"), so the argument is in-model. But it is weaker than
   needed: for any `q` in the support of *some* check, the pure data-side fault `I ⊗ X_q` at that
   check's CNOT on `q` already gives residual `(e_q, 0)`, with no idle location and no appeal to V1.
   Only a qubit in **no** check's support needs V1. Recording this would make `(≤)` robust to a
   depth bound, which matters because the ambient Eff-Preserve input admits an optional depth bound
   `T` (公共定义, 课题三).
2. **Edge case.** The contradiction "every check would have support `{q}`, so `H_X H_Z^T ≠ 0`" needs
   `m_X, m_Z ≥ 1`. The amendment states this parenthetically; it is not stated as a standing
   hypothesis anywhere in Model (M). Degenerate and immaterial, but it is an unstated hypothesis.

**Lemma B0 / step (a)** is straightforward and correct: Definition 1.3's multiset minimum is attained
with pairwise distinct vectors (Lemma 1.5), and such a multiset is exactly a `0/1` vector `f` with
`Σ F = Γ_X f`, `|F| = |f|`.

### 4.6 Independent computational verification — 104 fresh triples, 0 disagreements

My simulator, on codes chosen to include ones Amendment 5 did **not** test:

```
PART 1 -- fresh codes, blockwise and gate-level-INTERLEAVED schedules
codes: HAM [[15,7,3]] (Hamming-Steane, weight-8 checks)      -- fresh
       HAM + dependent X-check (rank-deficient H_X)          -- fresh, DEPENDENT GENERATORS
       [[6,2,2]] C6 ; [[6,4,2]] ; weight-8/4 [[8,4,1]]       -- fresh
       toric 2x2 (8 edges; BOTH generator sets dependent)    -- fresh, DEPENDENT GENERATORS
       Steane + dependent X-check                            -- fresh, DEPENDENT GENERATORS
       Shor + dependent Z-check                              -- fresh, DEPENDENT GENERATORS
       4 random CSS with n in [11,13]                        -- fresh (Amdt 5 used n in [7,10])
(code, schedule, interleaving) triples tested : 72      DISAGREEMENTS : 0

PART 1b -- instances where the bridge BITES (min = 3, and sectors that differ)
codes: HGP(rep4,rep3) n=18 (k=1, d_X=3, d_Z=4)               -- fresh, largest tested anywhere
       HGP(rep3,rep3) alt ; G_neq3 ; G_neq3 + Z-check (0,2,11)
(code, schedule, interleaving) triples : 32   with min = 3 : 16   DISAGREEMENTS : 0

TOTAL : 104 triples, 0 disagreements.
```

Every triple compares four independently computed numbers and requires all four to agree:
`D(M)` (my circuit, location count) `=` `min(d_eff^X, d_eff^Z)` (Definition 1.3, combinatorial) `=`
`d_ext` with the check supports **added** as columns `=` the single-joint-matrix reading (§5).

The test is not vacuous: `D(M)` takes the values 1, 2, 3 across the sweep, the two sectors disagree
on many triples (e.g. `G_neq3`: `effX = 3`, `effZ = 1`, `D = 1`; `HGP(rep4,rep3)`: `effX = 3`,
`effZ = 4`, `D = 3`), and 16 triples sit at the biting value `min = 3` where both inequalities are
tight. Gate-level interleaved schedules agree with blockwise ones on every triple, which is Lemma 1.2
re-verified on the circuit.

```
PART 2 -- Proposition A and the new structural fact, from MY circuit
(code, schedule) cases                                      : 14
Proposition A clause-1 violations                           : 0
locations with a weight>=2 residual in BOTH sectors          : 0   <- the new structural fact
check supports chi_supp(c) occurring as a ONE-fault residual : 456
   ... of which OUTSIDE the corresponding Cols set           : 456 <- the false step, quantified
```

**Verdict on Task 1: Lemma 1.4′ is CONFIRMED.** The derivation is correct as written, the identified
defect is real, the repair is sound and sufficient, the new structural fact is true and correctly
derived, and Theorem B holds in the stated universal form — every CSS code, every schedule, no
promise. I could not break it. The three precisions in §§4.2, 4.4 and 4.5 are non-blocking.

---

## 5. Task 2 — the bounded residual: **NON-ISSUE, no LEAD ratification needed**

Amendment 5 §1.7 leaves one thing underived: that **Definition E is the `E(M)` 公共定义 intends**,
and recommends registering it as a model-fact assumption in the T-G3 mould. Its own scope note
bounds the exposure to readings that reject **(i)** counting elementary-fault *locations* or **(ii)**
the terminal-residual harm criterion.

**My adjudication: (i) and (ii) are not free choices. The frozen text pins both.** Chapter and verse,
from `research/circdist/notes/CIRCDIST_PROBLEMS.md`:

* **(ii) is fixed verbatim.** 公共定义 line 27: the extended code is built from *"全部 terminal
  residual/hook errors"* — all terminal residual/hook errors. 课题二 line 97–98 spells the same
  boundary out: `G_eff` is *"忽略中间时间 detector、只保留 terminal residual effects 后得到的
  effective graph"* — ignore intermediate-time detectors, retain only terminal residual effects.
  That **is** criterion (ii).
* **(i) is fixed by the surrounding inequality chain.** Line 31 defines
  `d_circ(C) = min{ |F| : F 不触发任何 detector,但翻转非平凡逻辑量 }`, and **M3** fixes
  *"`|F|` counts fault locations"*. Line 35 then asserts `d_eff(M) ≤ d_circ(C(M)) ≤ d`, and line 37
  asserts `非交错电路已知满足 d_circ = d_eff`. A quantity that is `≤` a location count for every
  circuit and **equal** to it on a whole class of circuits is a location count. That **is**
  criterion (i).
* **The competing reading is excluded by the frozen text itself.** One could try to read
  `d_ext(E(M))` as the minimum *Hamming weight* of a nontrivial logical of the extended code. That
  reading returns `d(Q)` for every schedule, so `d_eff` would not depend on `M` at all — flatly
  contradicting 公共定义's own line 35 (`d_eff(M) ≤ d_circ(C(M))`, with `d_circ` schedule-dependent)
  and the entire premise of 课题三. Excluded.

So the amendment's residual is discharged **from the frozen text**, not from a reviewer's taste. I
then tested the two remaining reasonable constructions computationally, and both coincide:

* **(α) the most literal reading** — put *all* one-fault terminal residuals in `Γ_X`, i.e. add the
  check supports `χ_{supp(c)}` that Definition 1.3′ omits. Provable in one line
  (`L_X + S_X = L_X` again, in both directions) and **verified on all 32 biting triples: identical**.
* **(β) one joint matrix over both sectors** rather than the minimum of two sector distances —
  **verified on all 32 biting triples: identical** (this is Theorem B's content).

**Decision: this is not a definitional pin, it is a non-issue, and it does not need a LEAD
ratification.** It does not gate `PROVED`. I nonetheless **endorse the amendment's hygiene
recommendation** — register Definition 1.3′ as a node-level `model-fact` assumption — on the
separate ground of §2's "keep every load-bearing input machine-visible": the bridge currently carries
every clause while being invisible to the machine-checkable record. That is bookkeeping, not a
caveat, and the assumption's `statement` should say the reading is *pinned by 公共定义 lines 25–37*,
not merely *chosen*.

---

## 6. Task 3 — conformance sweep of items 2–6

### 6.1 Item 2 (R1), the corrected Island V clause: **DEFECT — a dropped hypothesis, again**

The three quotations in §2.1 are **exact**. I checked each against the write-up at the bound digest:
Theorem V.4 (lines 1180–1182), the §6.1 promise (lines 1056–1060), the §6.6 first scope bullet
(lines 1300–1301) — all verbatim, no elision, no paraphrase. The clause correctly restores `d_X ≥ 4`,
correctly refuses the words "unconditional YES" and "Eff-Preserve", correctly confines itself to the
X sector, and correctly points at Proposition 2.1 for composition. The `k = 0` branch is harmless
(`Log = 0` makes `d_eff^X = ∞ ≥ 3` vacuously), so writing `k ≤ 1` rather than `k = 1` is safe.

**But Theorem V.4's own statement contains a fifth qualifier that the clause drops.** V.4 reads:

> Under the promise of §6.1, if `k ≤ 1` then **every choice-free instance** is a YES …

Amendment 5 quotes that sentence verbatim in §2.1 — and then, three lines later, audits it as
*"Four hypotheses, then, not two: `d(Q) = 3` with `k ≥ 1` (ambient), X-check weight `≤ 4`,
**`d_X ≥ 4`**, and `k ≤ 1`."* **"Choice-free" is not in that list, is not adjudicated anywhere in the
amendment, and does not appear in the candidate clause.**

Worse: **"choice-free" is defined nowhere.** `grep` over `artifacts/` and `research/circdist/` returns
exactly two occurrences in the entire repository — V.4's statement, and Amendment 5's verbatim quote
of it. The word has never been given a meaning.

Its evident meaning is *"no restriction on which local orders are allowed"*: V.4's proof needs to
pick, per weight-4 check, an option with `β = 0` and *"any of its 8 realising orders"*. If the
instance restricts the admissible orders, that pick may be unavailable. And restricted-order
instances are **squarely inside this node's claim** — the Island IV clause is literally *"`d = 3`
with **two allowed orders per check**"*, and 公共定义 课题三 lists *"允许的 CNOT
interaction/conflict graph"* among the inputs of Eff-Preserve.

**I built the witness.** Take the amendment's own cited instance, `G_{≠3} + Z`-check `(0,2,11)` —
`n = 12`, `k = 1`, `d_X = 4`, `d_Z = 3`, `d(Q) = 3`, all five X-checks of weight 4, satisfying §6.1
**verbatim**. Unrestricted, it is a YES: V.4's printed schedule measures `d_eff^X = 3`, and random
search reaches 4. Now allow **two local orders per X-check**:

```
X-check (0,1,2,3)   allowed: (3,1,0,2) , (1,3,2,0)
X-check (4,5,6,7)   allowed: (5,7,4,6) , (7,5,6,4)
X-check (1,4,8,10)  allowed: (8,4,10,1) , (1,4,10,8)
X-check (0,6,8,11)  allowed: (8,11,0,6) , (6,8,11,0)
X-check (3,7,9,10)  allowed: (9,10,3,7) , (10,7,3,9)

d_eff^X over ALL 2^5 = 32 allowed schedules : {2}   (max 2 < 3)   [recomputed twice, two routines]
```

On an instance meeting §6.1 verbatim with `k = 1`, **no allowed schedule reaches `d_eff^X ≥ 3`**. So
the candidate clause's *"a schedule with `d_eff^X >= 3` always exists"* is **false** on the
restricted-order reading that this node's own Island IV clause invites.

This is the **same failure mode** that killed the previous Island V clause four days ago: a hypothesis
of Theorem V.4 dropped when the theorem was compressed into claim prose. The amendment's §2.1 was an
explicit hypothesis audit of V.4 and it missed one of V.4's own words.

**Required repair if the clause is ever installed:** carry the qualifier — e.g. *"…and, when every
local order is admissible (V.4's 'choice-free' instances), the X-sector at `d = 3` under…"* — and
give "choice-free" a definition in the dossier, since it currently has none. **Until then the clause
must not be added to the claim.**

### 6.2 Item 3 (R3), write-up §4.4: **CONFORMANT**, with the Thm 2.83 question answered

I checked the R3 block line by line against the wave-18 primary-source file. Every finding it
imports is faithfully transmitted: Prop 5.13 is indeed recorded there as an **MS₁ inexpressibility**
result of opposite polarity (wave-18 §5: *"Proposition 5.13 asserts no such thing; it contains no
incidence structure, no tree-width, and no algorithm"*); [Cou90] Def (3.2) does carry set variables
*"of sort `v` or `e`"* and Prop (4.14)(1) does carry the linear-time form, so both halves the
write-up outsourced are indeed already in the 1990 paper; [ALS91] is correctly demoted; Thm 6.4(1) is
quoted verbatim as wave-18 quotes it, including *"fixed-parameter linear with respect to
`(twd(G), φ)`"*.

**On [CE12] Theorem 2.83 specifically — the item I was asked to check.** The wave-18 record does
**not** quote 2.83's statement. Its only mention is descriptive, inside its account of 6.4(1):

> its proof invokes Theorem 1.25 for the decomposition and Theorem 2.83 to convert it into an HR term

So 2.83 is recorded as performing the **tree-decomposition → HR-term** conversion, which is exactly
the direction the bridge needs. **Amendment 5's registration is faithful to its source and correctly
hedged** — it says in terms that *"this dossier has not read Theorem 2.83's statement itself, so the
bridge carries one step of indirection and is not primary-verified here"*. That is the right label.

Two precisions. (a) The amendment states the bridge as an **iff** (*"HR expression of width `≤ m` iff
tree-width `≤ m − 1`"*); only the `⟸` direction is what 2.83 is recorded as supplying and only `⟸`
is needed. Registering the biconditional claims marginally more than the source supports. (b) Both
are **immaterial**, for the reason the block itself gives and I confirm: Island III takes the [CE12]
6.4(1) route, which is already stated in `twd(G)`, so it never invokes the bridge. The "one closed
chain, not two" correction is right, and it is a *demotion* of the record's own earlier claim — the
amendment argues against its own project's interest here, which is a good sign.

### 6.3 Item 4 (R6), the N3 instance: **CONFORMANT, and every number reproduces**

Rebuilt `G_{≠3}` from the gadget document's printed parity checks with my own code:

```
G_neq3 : n=12 k=2 d_X=4 d_Z=3 d(Q)=3   X-check weights [4,4,4,4,4]
section 6.1 verbatim (d(Q)=3, k>=1, X-weight<=4, d_X>=4) : True
weight-3 Z-logicals : 8 -> (0,1,8) (0,2,11) (1,3,10) (2,3,9) (4,6,8) (4,7,10) (5,6,11) (5,7,9)
augmentations with k = 1 meeting 6.1 verbatim : 8 / 8
cited instance G_neq3+Z(0,2,11) : n=12 k=1 d_X=4 d_Z=3 d(Q)=3
d_eff^X of Theorem V.4's printed schedule, from Definition 1.3 : 3   (V.4 asserts >= 3)
Z-sector search : best d_eff^Z = 3 ;  full-circuit D(M) = 3 = sector min  => YES
```

The list of eight weight-3 Z-logicals is **identical**, element for element, to the amendment's. The
promise is witnessed verbatim; edit 11 is genuinely discharged, not relabelled. Note that this also
re-confirms the bridge on the cited instance from two directions at once.

### 6.4 Item 5 (R5), HGP hypothesis vs conclusion: **CONFORMANT** (my census underpowered)

The distinction is correct and important: a census of `d(Q) ≠ min(μ_X, μ_Z)` counts instances where
**Theorem II.4's hypothesis** fails, not instances where its **conclusion** fails. The R5 block's
part (b) — that Lemma II.5's hypothesis (four kernel-dimension comparisons) is poly-time checkable
while Theorem II.4's (a distance condition) is not — is right and is the correct discharge of
islands-review edit 9. The node's claim clause *"so constant YES under the non-degeneracy proviso"*
names the proviso as a condition and is **unaffected**; R5 is caveat-level precision, as the block
says.

My own census, own distribution: **150** random HGP instances with `k ≥ 1`; **1** hypothesis failure
(0.7 %); **0** conclusion failures. The qualitative point reproduces. **I flag honestly that with a
single hypothesis-failing instance my census is underpowered** and corroborates the amendment's
`13/400` only weakly; the published rates (2.3 %, 3.4 %, 3.3 %) are all above mine and all come from
different distributions. The load-bearing number — conclusion failures — is 0 in all four censuses.

### 6.5 Item 6 (R4), the C1 draft residue: **CONFORMANT**

The R4 row and note record all three surviving residues correctly: [ALS91] never read (immaterial),
the [CE12] numbering being the **April 2011 authors' draft**'s rather than the print edition's, and
the HR-width bridge's one step of indirection. The striking of *"and its optimization extension"* as
over-registration is correct — `Φ_{t,w,d}` is a plain Boolean CMS₂ sentence. §6.2 row 4 correctly
notes that the **node's** `assumptions.courcelle-c1.statement` still needs these two additions and
that the amendment did not apply them (it modified no canonical file). That obligation is live and I
carry it into the caveat set.

---

## 7. Task 4 — verdict, claim recommendation, and level licensing

### 7.1 Verdict on Amendment 5

**CLEAR on item 1 (the substance) and on items 3–6. FURTHER-REPAIR on item 2 (R1) only.**

The one item that matters most — Lemma 1.4′ — is correct, and I confirmed it by independent
derivation and by an independent simulator on 104 fresh triples with zero disagreements. Blocker 2's
"derived" half was discharged by the amendment; its "**reviewed**" half is discharged **by this
review**. The R1 defect is real but is confined to a *candidate* that the amendment explicitly did
not install, so it damages nothing that is currently in the claim.

### 7.2 The two claim candidates, with digests

Hash pipeline validated in §2.1.

**(a) The current narrowed four-island claim**, unchanged, as it stands in the node file today:

```
sha256:2e786e9625b0223f52c70cb2b6521cfe9125ccf8d57834df37446211e1256346
```

**(b) The five-clause claim**, constructed as instructed — the current claim with the amendment's
corrected ASCII clause appended with corrected grammar (the list's "and" moved to the new final
item). The exact string I hashed, in full:

> Nontrivial restricted classes of Eff-Preserve are in P (or FPT) with proven correctness — including factorising instances (no inter-check coupling; self-certifying), HGP codes (every schedule preserves d_eff >= min(mu_X, mu_Z), so constant YES under the non-degeneracy proviso), bounded-treewidth Tanner graphs (CMSO2/Courcelle FPT), d = 3 with two allowed orders per check (2-SAT, no check-weight bound), and the X-sector at d = 3 under k <= 1, X-check weight <= 4 and d_X >= 4 (Theorem V.4: a schedule with d_eff^X >= 3 always exists and is found in linear time -- an X-sector guarantee only, not by itself an Eff-Preserve verdict; the Z-sector must be settled separately).

```
sha256:c192a4ca0376053f0357c62e781bd8869c6614932e0ca2f509ad289001d9ec1d
```

**Recommendation: install (a). Do NOT install (b).** By §6.1, (b) contains a clause that is false on
restricted-order instances, and this node's own Island IV clause puts restricted-order instances
inside the claim's world. The amendment itself offers the minimal alternative — *"leave the claim at
four islands and record Theorem V.4 in the caveat set instead"* — and calls it defensible. It is
more than defensible; on the present evidence it is the only safe option. Amendment 5's `(b)` may be
revisited once "choice-free" is defined in the dossier and carried into the clause.

### 7.3 Licensed level for claim (a): **CERTIFIED\***

Not `FURTHER-REPAIR`: nothing blocking survives in the four-island claim. Blocker 2 is discharged in
both halves. The V-clause refutation is already absorbed by the narrowing. Items 3–6 are conformant.

Not `PROVED`, on three named grounds:

1. **No independent adversarial review has yet passed on the assembled four-island argument.**
   §5 requires, for completion-level promotion, "a locatable independent adversarial review of the
   **assembled argument**". Mine is *focused*: Amendment 5 §1 at derivation level plus items 2–6 at
   conformance level. I did **not** re-derive the proofs of Theorems I, II.1–II.5, III and IV. The
   only review that did attack the assembly — wave-19 — returned FURTHER-REPAIR and is bound to a
   retired claim hash. This is the honest structural bar, and it is one focused session away.
2. **The load-bearing external locator is draft-only.** C1's operative citation, [CE12]
   Theorem 6.4(1), is verified against the **April 2011 authors' pre-publication draft**, not the
   published edition; the series designation "EMA 138" and the pagination remain secondary-source
   data, and numbering may shift between draft and print. That is an unresolved verification residue
   sitting on a load-bearing input — precisely what the star is for.
3. **The node's own `assumptions.courcelle-c1` block is not yet conformant** with the amendment: the
   2011-draft provenance sentence and the "one closed chain, not two" softening (with the HR-width
   bridge named) are still owed, per R4 §6.2 row 4. A completion label should not stand over an
   assumption block that the governing amendment has already corrected.

### 7.4 Exact caveat set for claim (a) at CERTIFIED\*

1. **Frozen-model exposure (systemic, permanent).** Model (M3)'s elementary-fault menu and the
   ideal-terminal-readout boundary are fixed by 公共定义 and cannot be tested from inside. Every
   verification in this campaign — the dossier's, Amendment 5's, wave-19's and **mine** — implements
   the same M3. Lemma 1.4′ removes a derivation gap *inside* the model, not the model's exposure.
2. **C1 locator provenance.** [CE12] Thm 6.4(1) / Thm 5.68(2) / Def 5.17 are draft-edition locators;
   print numbering unverified. [ALS91] never read (not load-bearing, discharged twice by fully-read
   texts). [CE12] Thm 2.83's statement not read — one step of indirection on the HR-width bridge,
   which the route actually taken does not use.
3. **Island III remains conditional on C1 by construction** (Theorem III is stated "modulo the pinned
   external theorem of §4.4"); C1 is registered as an external-theorem assumption and is now
   primary-verified in substance.
4. **The dossier files are unamended.** Amendments 1–5 are append-only; the write-up on disk still
   contains the false Lemma 1.4 step and the withdrawn §4.4 pin. The claim rests on the **amended
   reading** (Amdt 5 ▷ 4 ▷ 3 ▷ 2 ▷ 1 ▷ base), which is the campaign's stated governance order.
5. **Theorem V.4 is out of the claim, and out for two reasons now**: §6.6 forbids reading it as an
   Eff-Preserve verdict, and its "choice-free" qualifier is undefined and load-bearing (§6.1 above,
   with witness). Island V's general case remains open (`task-004`).
6. **Definition 1.3′ is not yet registered** as a node-level `model-fact` assumption. I adjudicate
   the underlying question as a non-issue (§5), so this is hygiene, not conditionality — but the
   bridge carries every clause while being invisible to the machine-checkable record.
7. **My HGP census is underpowered** (1 hypothesis-failing instance); R5's substance rests on the
   amendment's and wave-19's larger censuses, not on mine.

### 7.5 Which links belong in `basis`, and which in `evidence`

The checker enforces that **every** entry in `assessment.basis.reviews` carries
`reviewed_hash == claim_hash(current claim)` once the level is a completion level
(`tools/proof_dag_v6.py:341–355`, `COMPLETION_LEVELS = {"CERTIFIED*", "PROVED"}`). Therefore:

* **`basis.reviews`** — **this review only**, bound to
  `sha256:2e786e9625b0223f52c70cb2b6521cfe9125ccf8d57834df37446211e1256346`, with a `scope` field
  stating what it actually checked (Amendment 5 §1 at derivation level with an independent
  simulator; items 2–6 at conformance level; Islands I–IV's own proofs **not** re-derived).
* **`basis.runs`** — the wave-19 end-to-end review's run record **stays** (it is the own-code
  verification of Islands I–IV that makes the narrowed claim more than a sketch), plus, if wanted, a
  run entry for this review's 104-triple bridge verification.
* **`basis.evidence`** — wave-19's review file, the wave-18 primary-source file, Amendments 2 and 4,
  and **Amendment 5** (which is currently linked only from an event and belongs in evidence, since
  the claim now rests on its §1).

Prior hash-bound reviews (amendments-4 item 3, old hash `b4325b44…`) must **stay out of
`basis.reviews`** — they are bound to the retired claim.

### 7.6 Frontier consequences

* `task-003` — the amendment half is done; the re-review half is done by this file. **Close it**, and
  open in its place a task for the **assembled-argument** review named in §7.3 ground 1, which is the
  remaining gate to `PROVED`.
* **New task** — repair R1 before any future re-extension: define "choice-free" in the dossier and
  carry it into any Island V clause. The witness in §6.1 is the acceptance test.
* **New task (hygiene)** — apply R4's two additions to `assumptions.courcelle-c1`, and register
  Definition 1.3′ as a `model-fact` assumption per §5.
* `task-004` (Island V general case) — untouched.

---

## 8. Limitations of this review

1. I re-derived Amendment 5 §1 and checked items 2–6. **I did not re-derive Islands I–IV.** My
   licensing explicitly accounts for this (§7.3 ground 1).
2. My simulator implements the same (M3) fault menu as the dossier's. It is independent **code**, not
   an independent **model**. A systematic modelling error is invisible to it.
3. `D(M)` and `d_eff^sector` are exact for values 1 and 2 and capped at 3; on the `d(Q) = 3` codes I
   exhibit `min = 3` witnesses with a system-of-distinct-representatives check, so the comparison is
   exact there. Values `> 3` were not resolved (reported as `>3`) and no triple required them.
4. My upper-bound search at `t = m` uses pure-sector residuals. That is sufficient for an upper bound
   (a witness is a witness) but means I did not enumerate mixed-sector witnesses at `t = m`; the
   lower-bound sweep at `t < m`, which is where the theorem could break, **is** exhaustive over the
   full local Pauli group.
5. I read no primary Courcelle text. §6.2 consumes the wave-18 verification as data, exactly as
   Amendment 5 does; I checked transmission fidelity, not the underlying scholarship.
6. The "choice-free" reading in §6.1 is my inference from V.4's proof (it needs *"any of its 8
   realising orders"*), since the term is defined nowhere. If the author intends something else, the
   witness still stands as a demonstration that *some* qualifier is needed; only its name would
   change.

---

## 9. Surprises worth the lead's attention

1. **The amendment's own hypothesis audit dropped a hypothesis.** §2.1 quotes Theorem V.4 verbatim —
   "every **choice-free** instance" — and then, three lines later, enumerates "four hypotheses, then,
   not two" without it. This is the eighth self-correction of the campaign and, more pointedly, it is
   *the same failure mode, on the same theorem, four days later*: the wave-19 refutation killed the
   old Island V clause for dropping `d_X ≥ 4`; the replacement drops "choice-free". Compressing a
   theorem into claim prose is where this project loses hypotheses, and doing it carefully once is
   evidently not enough.
2. **A term that has never been defined has been load-bearing since 2026-08-20.** "Choice-free"
   occurs exactly twice in the repository, both times inside the same sentence of Theorem V.4 and its
   quotation. Six review layers read past it.
3. **The §1.7 residual is smaller than the amendment thinks, and the frozen text is what shrinks
   it.** The amendment treats "is Definition E the intended `E(M)`?" as a lead-ratification item. But
   公共定义's own lines 31–37 — `d_circ` counting `|F|`, `d_eff ≤ d_circ`, and `d_circ = d_eff` for
   non-interleaved circuits — already force both conditions the scope note isolates. The author had
   the discharge in hand and under-claimed it. Under-claiming is the right direction to err, but the
   node should record the stronger, correct position.
4. **The bridge is more robust than either its (≥) or (≤) proof suggests.** Adding the check supports
   as extra columns, and merging both sectors into one matrix, both return the same number — verified
   on every biting instance. The quantity is stable under all four constructions I could think of,
   which is unusual and is the real reason the definitional worry evaporates.
5. **The one place the amendment argues against its own interest is the one place it is strongest.**
   R3 demotes "two disjoint chains" to one, demotes [ALS91], and flags its own Thm 2.83 indirection.
   That section needed no defending and got the most careful hedging in the file.
