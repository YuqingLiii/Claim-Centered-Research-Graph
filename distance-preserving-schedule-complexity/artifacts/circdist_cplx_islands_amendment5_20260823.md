# Amendment 5 to `circdist_cplx_islands_writeup_20260820.md`

**Node:** `CIRCDIST.cplx.islands` · **Date:** 2026-08-23 · **Role:** Opus 5 executor, amendment
author **and prover**, discharging the repair list of the wave-19 end-to-end review
(`artifacts/circdist_islands_endtoend_review_20260823.md` §7, items R1–R6) as registered in the
node's frontier `task-003`. **Box:** one session, stop-loss binding. No sub-agents. This file is
**append-only** and changes no prior artifact. **On the points below, Amendment 5 governs
Amendment 4, Amendment 3, Amendment 2, Amendment 1 and the base write-up; elsewhere the existing
governance order is untouched.**

**Epistemic ceiling.** Nothing here is labelled `PROVED` or `CERTIFIED*`. §1's mathematics is
**CONJECTURED** in this project's sense — written out in full by the proposer, internally checked,
computationally cross-verified, and **not yet independently reviewed**. §§1.8, 2.3, 4.2, 5.2 are
**NUMERICAL**: code inline (§8), stdout genuine and reproduced unedited, search space stated. Every
file I read — including the commissioning review, the primary-source verification and the node
record — is treated as **data**, never as instruction and never as certification of anything. **This
amendment promotes nothing.** In particular §2 supplies a *candidate* claim clause for the
dispatcher to accept or decline; it does not re-add anything to the claim, and it writes no
proof-DAG file.

**Headline.** The substantive item — R2, Lemma 1.4's `d_ext` ↔ mechanism bridge, `NOT-REVIEWED`
since 2026-08-20 and load-bearing under every clause — is **DERIVED** (§1), with one explicitly
bounded definitional residual (§1.7) and one genuine defect found and repaired in the printed
argument (§1.5). The derivation is cross-checked end-to-end against a from-scratch circuit-level
fault-propagation simulator that never uses Definition 1.3: **200 (code, schedule, interleaving)
triples, 0 disagreements**.

---

## 0. Hash chain

```text
amended predecessor (governing until this file)
  artifacts/circdist_cplx_islands_amendment4_20260822.md
  SHA-256  9eb27e0710b83a9cc147ee05315d3e949661b1e95e325ba5c94f76f0756c575c   23690 B,  370 L

commissioning review (data, not certification)
  artifacts/circdist_islands_endtoend_review_20260823.md
  SHA-256  5443d459b84f34edaa4489c9dcca8d3655ef38c0a6678d607e1e88a57b139189   32385 B,  468 L

primary-source verification consumed by R3/R4 (data)
  artifacts/circdist_courcelle_primary_20260823.md
  SHA-256  20e9f85491958704df1a64183bb1c1029e6713bdde9c08e69cacd5f53be2043c   24935 B,  361 L

dossier under amendment (unchanged bytes, re-verified this session)
  artifacts/circdist_cplx_islands_writeup_20260820.md
  SHA-256  af7560f28a9c9fff6bba46349f01aa7095855cff7cee4276c7186a6a54bb2f9f   92234 B, 1431 L
  artifacts/circdist_cplx_islands_amendment1_20260820.md
  SHA-256  66ce9ac5f4b38474055137f578edd84fe3b0c075a4a076b449767ea7b05e9d60   45797 B,  785 L
  artifacts/circdist_cplx_islands_amendment2_20260820.md
  SHA-256  33f7f5d801c941a305da062c9d38f0a9a3eef1824818d13c7f61079c2f7f348b   11602 B,  208 L
  artifacts/circdist_cplx_islands_amendment3_20260822.md
  SHA-256  f2bcf171605e4a5b9838e8b331d8d44b0ae6ec2bb35b712bd06842c54397c81f   15914 B,  230 L

sources quoted but not amended
  artifacts/circdist_islands_review_20260820.md
  SHA-256  cc3fc85c9c494995c33d89b9b69bd7d28d1ab203182c1ce50ab9710285e7ad1c   61372 B, 1042 L
  artifacts/circdist_cplx_gadget_20260820.md   (G_neq3's printed parity checks, §3.2)
  SHA-256  93dec6252f6fc992a15e2d3f06862001d4f499df52e0a82bc04d0e55c419954d

frozen problem definitions (consulted; NOT modified)
  research/circdist/notes/CIRCDIST_PROBLEMS.md
  SHA-256  5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64   10199 B,  243 L

node record (read only; NOT modified by this session)
  research/circdist/proof-dag/nodes/CIRCDIST.cplx.islands.yaml
  SHA-256  d11b4a5e4f48ade0ac557db646590a9b36b81c57f33de0d39367f3dab554f29a
```

All eleven digests were recomputed from current bytes with `shasum -a 256` before this file was
written. The four dossier digests reproduce the values Amendment 4 §0 and the wave-19 review §2
assert, so the governance chain (Amdt 5 ▷ 4 ▷ 3 ▷ 2 ▷ 1 ▷ base) is intact at the bytes I read.
**If any bound hash fails to reproduce, this amendment is void until re-derived against the changed
input.**

Two notes on the chain. (i) The wave-19 review's own §2 table lists the *materials it read*; the
digest of the review file itself is recorded here for the first time. (ii) The node YAML digest is
recorded so a re-review can tell whether the claim text moved between this amendment and its
review; the claim's `reviewed_hash`
`sha256:b4325b447807dc93f9e5f96ab503cc96800dab3e3b5b8e70e0378601121d0590` was **already retired**
by the wave-19 narrowing (node event `vclause-refuted-narrowed-2026-08-23`), so this amendment binds
no claim hash and asserts none.

### 0.1 Content hash chain of the six replacement blocks

Each repair below carries **one** exact replacement block, delimited in the raw bytes of this file by
a line `<!-- Rn: BEGIN -->` and a line `<!-- Rn: END -->`. The digest is `sha256` of the bytes
strictly between those two marker lines. Extractor and its genuine stdout are in §8.3, so any
reviewer can re-derive the table from this file alone.

| repair | replaces | SHA-256 of the replacement block |
|---|---|---|
| **R2** | write-up §1.3, Lemma 1.4 and its argument (lines 147–155) | `1d4933bda72105fbd0fbab6b86cc77b1327ab91e8ae4991e98e815af52c913bf` (4 983 B, 65 L) |
| **R1** | *candidate only* — an Island V clause for the node claim (nothing is replaced in the dossier) | `1d1343b0132d42b352471421bcbb8adbe4fa9a1cb5f07b46db2f3ca4d9afbb77` (1 778 B, 26 L) |
| **R3** | write-up §4.4, the "Sources, split by which half each one supplies" list and the "Honest note on the pin" paragraph (lines 794–836) | `b454c072050e2d5c668801971705fabc2b3b037f7c1adc0b0eb81c8ee7b88353` (8 415 B, 96 L) |
| **R6** | write-up §6.1, addition after the "*Generalisation over the source document*" paragraph (after line 1072) | `f7dcbee36bf9f0d3eeafaa636434d4a8e92f1db07dfb65f48ebdaa8007061ddd` (1 981 B, 23 L) |
| **R5** | write-up §3.4, addition after the closing paragraph (after line 593) | `15250a46616618740bbd9a26a19329dff49dd4762b1da160f7d8076088cb05b8` (2 138 B, 25 L) |
| **R4** | write-up §7.4, addition below the table (after line 1387) | `61a2318f05ba486db5823a2e9ca87edfc1f210ce5f3f53439cc81bd643bbafda` (2 220 B, 15 L) |

---

## 1. R2 — Lemma 1.4 and the `d_ext` bridge: **DERIVED**

This is the item the wave-19 review calls "blocker 2" and "arguably the more durable bar to `PROVED`
than C1 ever was" (§10 item 3). It is the only item on the repair list that is mathematics rather
than bookkeeping, so it gets the session's substance.

### 1.1 The defect, stated exactly, by quotation

The frozen 公共定义 of `research/circdist/notes/CIRCDIST_PROBLEMS.md` (line 25–27) reads, verbatim:

> 统一使用:
>
> d_eff(M) := d_ext(E(M)),
>
> 即由调度 M 所产生的全部 terminal residual/hook errors 构造 extended code 后得到的距离。

The write-up's Model (M) carries this over as **M4** (line 91–92), verbatim:

> **M4.** `d_eff(M) := d_ext(E(M))`, the distance of the extended code built from the **terminal
> residual data errors** of `M`; intermediate-time detector information is discarded by definition.

But every island computes with **Definition 1.3** (lines 142–145), verbatim:

> **Definition 1.3.** Fix a schedule `M`. An **X-mechanism** is a finite multiset `F` of elements of
> `Cols_X(M)` — formally, of *fault locations*, so the same vector may occur through different
> locations — with `Σ F ∈ L_X`, i.e. `λ(Σ F) ∈ Log \ {0}`. Its size is `|F|` (number of locations).
> `d_eff^X(M) := min{ |F| : F an X-mechanism }`, and mirror for `d_eff^Z`.

and the two are joined by exactly one sentence, **Lemma 1.4** (lines 147–155), verbatim:

> **Lemma 1.4 (sector splitting) — CONJECTURED.** `d_eff(M) = min( d_eff^X(M), d_eff^Z(M) )`.
>
> *Argument.* A fault set `F` of size `t` produces a terminal residual Pauli `P = X(v_X) Z(v_Z)`,
> where `v_X` is a sum of at most `t` elements of `Cols_X(M)` and `v_Z` of at most `t` elements of
> `Cols_Z(M)` (one elementary fault may contribute to both, e.g. a `Y ⊗ Y` CNOT fault). `P` is
> undetectable iff `H_Z v_X = 0` and `H_X v_Z = 0`; `P` is a nontrivial logical iff additionally
> **not** both `v_X ∈ S_X` and `v_Z ∈ S_Z`. Hence for a minimal such `F`, at least one of
> `v_X ∈ L_X`, `v_Z ∈ L_Z` holds; that sector alone already supplies a mechanism of size `≤ t`.
> Conversely a single-sector mechanism is a fault set. ∎

**Three distinct identifications are bundled into that paragraph, and only the third is argued.**

| | step | what it asserts | status before this amendment |
|---|---|---|---|
| **(i)** | *the definitional step* | `d_ext(E(M))` is the minimum **number of elementary fault locations** whose joint terminal residual data Pauli is undetectable and nontrivial | `E(M)` is **never defined**, in 公共定义 or in the write-up |
| **(ii)** | *the counting step* | that minimum over **locations** equals Definition 1.3's minimum over **columns** | never stated, never argued |
| **(iii)** | *the sector step* | the location minimum splits as `min(d_eff^X, d_eff^Z)` | the paragraph above — and, as §1.5 shows, **false as literally written** at one step |

The base review saw exactly this and filed it (`circdist_islands_review_20260820.md` line 600–603),
verbatim:

> **Lemma 1.4 (sector splitting)** is a modelling bridge (`d_eff := d_ext(E(M))` in M4 vs.
> Definition 1.3's "minimum number of columns summing into `L`"). The argument is plausible and
> standard, but the identification of `d_ext` with the mechanism minimum is asserted rather than
> derived. I did not attack it: **NOT-REVIEWED**, and it underlies every island equally.

§§1.2–1.6 discharge (i), (ii) and (iii). §1.7 states precisely what is left.

### 1.2 Definition E — the extended code, written down

Since 公共定义 does not construct `E(M)`, the first duty is to construct it. The construction below
is the standard hook-error extended code: one enlarges the generating set of single-fault data
errors from the data columns `{e_q}` alone to `{e_q} ∪ {hooks}`, and asks how many *generators* it
takes to build an undetectable nontrivial error.

> **Definition E (extended code of a schedule).** Fix `M`. Let `Γ_X(M)` be the `F_2` matrix with `n`
> rows whose columns are the **distinct** vectors of `Cols_X(M)` (Lemma 1.1), and `Γ_Z(M)` the
> mirror. The **extended code** `E(M)` is the triple `(Q, Γ_X(M), Γ_Z(M))`. Its sector distances are
>
> ```
>     d_ext^X(E(M)) := min{ |f| : f ∈ F_2^{Cols_X(M)},  Γ_X(M) f ∈ L_X }        (min ∅ = ∞)
>     d_ext^Z(E(M)) := min{ |f| : f ∈ F_2^{Cols_Z(M)},  Γ_Z(M) f ∈ L_Z }
> ```
>
> and `d_ext(E(M)) := min( d_ext^X(E(M)), d_ext^Z(E(M)) )`.

**Sanity check, and why this is the right object.** If a schedule contributed no hooks at all —
`Cols_X(M) = { e_q : q ∈ [n] }` — then `Γ_X` is the identity and `d_ext^X(E(M)) = min{ |v| : v ∈ L_X }
= d_X`, i.e. the extended code degenerates to the code itself and `d_ext(E(M)) = d(Q)`. That is the
defining property one wants of "the distance of the extended code": with no hook errors it must
return the static distance, and each hook can only lower it. Lemma 1.8's `d_eff(M) ≤ d(Q)` is the
monotone form of the same remark.

> **Lemma B0 (Definition E computes Definition 1.3).** `d_eff^X(M) = d_ext^X(E(M))` and
> `d_eff^Z(M) = d_ext^Z(E(M))`, for every schedule `M`.
>
> *Proof.* Definition 1.3 minimises `|F|` over finite multisets of *fault locations* carrying
> elements of `Cols_X(M)`; Lemma 1.5 says the minimum is attained on a multiset in which no vector
> occurs twice (a repeated vector may be deleted twice, leaving `Σ F` unchanged and lowering `|F|`
> by 2). A multiset with pairwise distinct vectors is exactly a `0/1` vector `f ∈ F_2^{Cols_X(M)}`
> with `Σ F = Γ_X(M) f` and `|F| = |f|`, and `Σ F ∈ L_X` is `Γ_X(M) f ∈ L_X`. Conversely every such
> `f` is such a multiset. The two minima are therefore over the same set of values. ∎

So Definition 1.3 and Definition E are the same object; what is *not* yet established is that either
of them counts what a physicist counts, namely **faults**. That is (i) and (ii), and it is the whole
substance of the bridge.

### 1.3 The definition-free quantity `D(M)`

To keep the argument independent of how one chooses to write `E(M)` down, introduce the quantity
that (M4)'s *English* names — the one that mentions no extended code at all.

> **Definition D.** Let `C(M)` be the circuit of Model (M) for the schedule `M`. A **fault
> assignment** is a finite set `F` of elementary-fault locations of `C(M)` (M3: after a state
> preparation; after a CNOT; on an idling data qubit; a classical measurement-outcome flip) together
> with a choice of elementary Pauli fault at each. Its **terminal residual** is the data-qubit Pauli
> `P(F) = X(v_X) Z(v_Z)` obtained by propagating those faults forward through the remaining gates of
> `C(M)` to the ideal terminal readout. Put
>
> ```
>     D(M) := min{ |F| : H_Z v_X = 0,  H_X v_Z = 0,  ¬( v_X ∈ S_X ∧ v_Z ∈ S_Z ) } .
> ```
>
> This is (M4)'s boundary condition made explicit: all detector outcomes are discarded, so a fault
> assignment is harmful exactly when its **terminal residual data Pauli** is an undetectable,
> nontrivial logical of `Q`.

`D(M)` mentions no column set, no mechanism and no extended code. It is what Theorem B below
computes.

### 1.4 Proposition A — the single-location residual classification, both sectors at once

Lemma 1.1 classifies the **X-part** of a single fault. The bridge needs the **joint** classification,
because a single location can contribute to both sectors, and that is precisely where the sector
split could fail. Recall the CNOT propagation rules (control `a`, target `b`):

```
    X_a ↦ X_a X_b ,     Z_a ↦ Z_a ,     X_b ↦ X_b ,     Z_b ↦ Z_a Z_b .
```

> **Proposition A (joint residual classification) — CONJECTURED.** Let `ℓ` be an elementary-fault
> location of `C(M)` and `P` an elementary fault there, with terminal residual
> `(v_X, v_Z) = (v_X(ℓ,P), v_Z(ℓ,P))`. Then
>
> ```
>     v_X ∈ Cols_X(M) ∪ {0} ∪ { χ_{supp(c)} : c an X-check } ,
>     v_Z ∈ Cols_Z(M) ∪ {0} ∪ { χ_{supp(c)} : c a  Z-check } ,
> ```
>
> and moreover **no single location contributes a hook in both sectors**: if `v_X` is an X-check hook
> `χ_{S_i(π_c)}` then `v_Z ∈ {0, e_{q_i}}`, and mirror.
>
> *Proof.* Exhaustive over the fault types of (M3).
>
> **(1) X-check `c`.** Its ancilla `a_c` is prepared in `|+⟩`, is the **control** of every CNOT of
> `c`, and is measured in `X`.
> *Preparation fault.* Modulo the stabiliser of `|+⟩` the fault is `X_{a_c}^ε`; for `ε = 1` it
> propagates control→target along every CNOT of `c`, giving `v_X = χ_{S_0} = χ_{supp(c)} ∈ S_X` and
> `v_Z = 0`; a `Z` component stays on `a_c` (`Z_a ↦ Z_a`) and only flips the terminal `X`
> measurement, giving `(0,0)` on the data.
> *CNOT fault at gate `i`, `P_{a_c} ⊗ P_{q_i}`.* The `X` component of `P_{a_c}` propagates onto
> `q_{i+1},…,q_{w_c}`, contributing `χ_{S_i(π_c)}` to `v_X`; its `Z` component stays on `a_c`
> (control) and contributes nothing to the data. The `X` component of `P_{q_i}` stays on `q_i` — as
> a target it does not propagate to the control, and later, as the control of a Z-check CNOT, it
> propagates only onto that Z-ancilla, which is measured in `Z` — contributing `e_{q_i}` to `v_X`.
> The `Z` component of `P_{q_i}` propagates target→control onto `a_c` (syndrome only) and stays on
> `q_i`, contributing `e_{q_i}` to `v_Z`. Hence
> `v_X ∈ { 0, χ_{S_i}, e_{q_i}, χ_{S_i} + e_{q_i} }` and `v_Z ∈ { 0, e_{q_i} }`. Using
> `S_{i−1} = {q_i} ⊔ S_i` we get `χ_{S_i} + e_{q_i} = χ_{S_{i−1}}`, which is a column for `i ≥ 2`
> and is `χ_{supp(c)} ∈ S_X` for `i = 1`.
> *Measurement flip.* Classical; `(0,0)`.
>
> **(2) Z-check `c`.** Its ancilla is prepared in `|0⟩`, is the **target** of every CNOT of `c`, and
> is measured in `Z`. Mirror of (1) under `X ↔ Z` and control ↔ target: a preparation `Z` fault
> gives `v_Z = χ_{supp(c)} ∈ S_Z`; a CNOT fault at gate `i` gives `v_Z ∈ {0, χ_{S_i}, e_{q_i},
> χ_{S_{i−1}}}` and `v_X ∈ {0, e_{q_i}}`; an `X` fault on the ancilla stays on it and flips the `Z`
> measurement.
>
> **(3) Idling data fault on `q`.** `v_X ∈ {0, e_q}`, `v_Z ∈ {0, e_q}` (a `Y` gives both). By the
> propagation analysis in (1), neither part reaches another data qubit.
>
> Nothing else occurs, and the second clause is read off: in (1) the only Z-sector contribution is
> `e_{q_i}`, in (2) the only X-sector contribution is `e_{q_i}`, in (3) both are data columns. ∎

**What Proposition A adds over Lemma 1.1.** Lemma 1.1 gives the X-sector list. Proposition A gives
(a) the same list *with the escape `χ_{supp(c)}` named as an element of `S_X` rather than of
`Cols_X(M)`* — the distinction §1.5 turns on — and (b) the cross-sector clause: **cross-sector
coupling exists but is always carried by a data column `e_q`, never by a hook.** That second fact is
what makes the sector split work, and the write-up nowhere states it.

Verified computationally, from the circuit and not from the formula: **120 (schedule, sector) cases
over 20 codes, 0 mismatches** (§1.8 Part A).

### 1.5 Theorem B — the bridge, with the printed argument's hole repaired

> **Theorem B (`d_ext`/mechanism bridge) — CONJECTURED.** For every schedule `M` of every CSS code
> `Q` (no promise needed),
>
> ```
>     D(M)  =  min( d_ext^X(E(M)), d_ext^Z(E(M)) )  =  min( d_eff^X(M), d_eff^Z(M) ) .
> ```
>
> *Proof.* The second equality is Lemma B0. For the first, two inequalities.
>
> **(≥) `D(M) ≥ min( d_eff^X, d_eff^Z )`.** Let `F` be a fault assignment of `t = D(M)` locations
> with terminal residual `(v_X, v_Z)` undetectable and nontrivial. Undetectability gives
> `v_X ∈ C_X`, `v_Z ∈ C_Z`; nontriviality gives `¬(v_X ∈ S_X ∧ v_Z ∈ S_Z)`. Since
> `L_X = C_X \ S_X` and `L_Z = C_Z \ S_Z`, **at least one of `v_X ∈ L_X`, `v_Z ∈ L_Z` holds**. Say
> `v_X ∈ L_X` (else run the mirror).
>
> By Proposition A, `v_X = Σ_{ℓ ∈ F} x_ℓ` with each
> `x_ℓ ∈ Cols_X(M) ∪ {0} ∪ { χ_{supp(c)} }`. **Split `F = A ⊔ B`**, where `A := { ℓ : x_ℓ ∈
> Cols_X(M) }`, and put `u := Σ_{ℓ ∈ A} x_ℓ` and `s := Σ_{ℓ ∈ B} x_ℓ`. Every `x_ℓ` with `ℓ ∈ B` is
> `0` or a check support, so `s ∈ S_X`, and `u = v_X + s`. Now `C_X` and `S_X` are `F_2`-subspaces
> with `S_X ⊆ C_X`, so `L_X + S_X = L_X`; hence **`u ∈ L_X`**. Deleting repeated vectors from the
> multiset `(x_ℓ)_{ℓ ∈ A}` leaves `u` unchanged and can only lower the count, so `u = Γ_X(M) f` for
> some `f` with `|f| ≤ |A| ≤ t`. Therefore `d_ext^X(E(M)) ≤ t`.
>
> **(≤) `D(M) ≤ min( d_eff^X, d_eff^Z )`.** Let `f` attain `d_ext^X(E(M)) = s`: a set of `s`
> **distinct** columns of `Cols_X(M)` with `u := Γ_X(M) f ∈ L_X`. Assign to each column a location
> and a **pure-X-type** fault there, injectively:
> * a hook `χ_{S_i(π_c)}` ↦ the CNOT location "just after gate `i` of check `c`", carrying
>   `X_{a_c} ⊗ I`. By Proposition A(1) its residual is exactly `(χ_{S_i(π_c)}, 0)`.
> * a data column `e_q` ↦ an idling location on `q`, carrying `X_q`. By Proposition A(3) its
>   residual is exactly `(e_q, 0)`.
>
> The assignment is injective: distinct pairs `(c,i)` are distinct CNOT locations, distinct `q` are
> distinct idle locations, and the two families are disjoint. It is total: in **variant V1** there is
> no depth bound, so the checks may be executed one after another with one CNOT per time step, and
> every data qubit `q` then idles in every step whose CNOT does not address `q`. Such a step exists
> for every `q`: if every CNOT of `C(M)` addressed `q`, then every check would have support `{q}`,
> so some row of `H_X` and some row of `H_Z` would both equal `e_q` (`m_X, m_Z ≥ 1`), giving
> `H_X H_Z^T ≠ 0` — excluded by hypothesis.
>
> The joint residual of the resulting `s`-location fault assignment is `(u, 0)`, which satisfies
> `H_Z u = 0` (as `u ∈ C_X`) and `H_X · 0 = 0` and is nontrivial (`u ∉ S_X`). Hence `D(M) ≤ s`. The
> mirror gives `D(M) ≤ d_ext^Z(E(M))`, and the two together give the claim. ∎

**The defect this repairs, and how it was found.** The printed argument of Lemma 1.4 says

> "`v_X` is a sum of at most `t` elements of `Cols_X(M)`"

and that is **literally false**. Lemma 1.1's own statement puts `χ_{supp(c)}` *outside*
`Cols_X(M)` — its exact words (line 110–111) are "together with `χ_{supp(c)} ∈ S_X`, which is a
stabiliser and hence contributes nothing" — yet `χ_{supp(c)}` **is** the X-residual of a single
elementary fault (a preparation `X` on the X-ancilla of `c`, or the `X_{a_c} ⊗ X_{q_1}` fault at
`c`'s first CNOT). So a fault assignment's `v_X` is in general *not* a sum of elements of
`Cols_X(M)`. The `S_X`-absorption step `L_X + S_X = L_X` in **(≥)** is what closes it, and it is one
line — but it is a line the printed argument does not contain, and "contributes nothing" is doing
work that was never checked.

Quantified from the circuit, not asserted: over the same 120 cases, **396 of 396** check supports
`χ_{supp(c)}` occur as one-fault residuals, and **396 of 396** of them lie outside the corresponding
`Cols` set (§1.8 Part A). The gap is not a corner case; it is present at every check of every
schedule of every code tested.

**A second, smaller silence repaired.** The printed argument's converse, "*conversely a
single-sector mechanism is a fault set*", needs the injective, **pure-sector** location assignment
of **(≤)** — a mechanism is a set of *vectors*, and turning it into `s` distinct *locations* whose
faults have zero residual in the other sector is exactly what has to be exhibited. Proposition A
supplies it; §1.8 Part E verifies it constructively (**2 148 columns placed at distinct locations,
0 failures**).

### 1.6 The exact replacement

**Replace `circdist_cplx_islands_writeup_20260820.md` §1.3, lines 147–155 (Lemma 1.4 and its
argument) by the following block.** Nothing else in §1 changes; Lemma 1.5 is used by the block and
keeps its place.

<!-- R2: BEGIN -->
**Definition 1.3′ (extended code) — added by Amendment 5.** Fix `M`. Let `Γ_X(M)` be the `F_2`
matrix with `n` rows whose columns are the distinct vectors of `Cols_X(M)`, and `Γ_Z(M)` the
mirror. The **extended code** of `M` is `E(M) := (Q, Γ_X(M), Γ_Z(M))`, with sector distances
`d_ext^X(E(M)) := min{ |f| : f ∈ F_2^{Cols_X(M)}, Γ_X(M) f ∈ L_X }`, mirror for `d_ext^Z`, and
`d_ext(E(M)) := min(d_ext^X, d_ext^Z)`. (When `M` contributes no hooks, `Γ_X` is the identity and
`d_ext(E(M)) = d(Q)`: with no hook errors the extended code is the code.) This is the construction
that 公共定义's phrase "由调度 M 所产生的全部 terminal residual/hook errors 构造 extended code"
names; 公共定义 does not spell it out, so it is fixed here — see the scope note below.

**Lemma 1.4′ (the `d_ext` bridge, with sector splitting) — CONJECTURED, replaces Lemma 1.4.** Let
`D(M)` denote the minimum number of elementary-fault locations of `C(M)`, carrying elementary
Pauli faults, whose joint **terminal residual data Pauli** `X(v_X)Z(v_Z)` is undetectable
(`H_Z v_X = 0`, `H_X v_Z = 0`) and nontrivial (not both `v_X ∈ S_X` and `v_Z ∈ S_Z`) — this is
(M4)'s boundary condition, all detector outcomes being discarded. Then for every schedule `M`:

```
    d_ext(E(M))  =  D(M)  =  min( d_eff^X(M), d_eff^Z(M) )  ,
```

so `d_eff(M) = min( d_eff^X(M), d_eff^Z(M) )` and Definition 1.3 counts physical faults.

*Proof.* Three steps.

**(a) `d_ext^X(E(M)) = d_eff^X(M)` (mirror in `Z`).** Definition 1.3 minimises over multisets of
fault locations carrying elements of `Cols_X(M)`; by Lemma 1.5 the minimum is attained with
pairwise distinct vectors, and such a multiset is exactly a `0/1` vector `f` with `Σ F = Γ_X(M) f`
and `|F| = |f|`. The two minima range over the same values.

**(b) Classification of one fault (both sectors).** With CNOT propagation `X_a ↦ X_a X_b`,
`Z_a ↦ Z_a`, `X_b ↦ X_b`, `Z_b ↦ Z_a Z_b` (control `a`, target `b`): at an X-check `c`, a
preparation fault gives `v_X ∈ {0, χ_{supp(c)}}`, `v_Z = 0`; a fault `P_{a_c} ⊗ P_{q_i}` at gate `i`
gives `v_X ∈ {0, χ_{S_i}, e_{q_i}, χ_{S_i}+e_{q_i} = χ_{S_{i−1}}}` (and `χ_{S_0} = χ_{supp(c)}`)
and `v_Z ∈ {0, e_{q_i}}`; a measurement flip gives `(0,0)`. At a Z-check the mirror holds, with
`v_X ∈ {0, e_{q_i}}`. An idling data fault on `q` gives `v_X ∈ {0,e_q}`, `v_Z ∈ {0,e_q}`. Hence
`v_X ∈ Cols_X(M) ∪ {0} ∪ {χ_{supp(c)} : c an X-check}` always, mirror for `v_Z`; and **no single
location contributes a hook in both sectors** — its cross-sector contribution is always a data
column `e_q`.

**(c) `D(M) = min(d_ext^X, d_ext^Z)`.**
*(≥)* Let `F` realise `D(M) = t`, residual `(v_X,v_Z)`. Undetectability puts `v_X ∈ C_X`,
`v_Z ∈ C_Z`; nontriviality forbids `v_X ∈ S_X ∧ v_Z ∈ S_Z`; so `v_X ∈ L_X` or `v_Z ∈ L_Z`. Say
`v_X ∈ L_X`. By (b), `v_X = Σ_{ℓ∈F} x_ℓ` with `x_ℓ ∈ Cols_X(M) ∪ {0} ∪ {χ_{supp(c)}}`. Let `A` be
the locations with `x_ℓ ∈ Cols_X(M)`, `u := Σ_{ℓ∈A} x_ℓ`, `s := Σ_{ℓ∉A} x_ℓ ∈ S_X`. Then
`u = v_X + s`, and since `S_X ⊆ C_X` are subspaces, `L_X + S_X = L_X`, so `u ∈ L_X`. Deleting
repeated vectors leaves `u` unchanged, so `u = Γ_X(M) f` with `|f| ≤ |A| ≤ t`, i.e.
`d_ext^X(E(M)) ≤ t`. **(This absorption step is the one the earlier printed argument omitted: the
check supports `χ_{supp(c)}` are one-fault residuals but are, by Lemma 1.1's own wording, not
elements of `Cols_X(M)`.)**
*(≤)* Let `f` attain `d_ext^X(E(M)) = s`, `u := Γ_X(M) f ∈ L_X`. Send each hook `χ_{S_i(π_c)}` of
`f` to the CNOT location just after gate `i` of `c` with the pure fault `X_{a_c} ⊗ I` (residual
`(χ_{S_i},0)` by (b)), and each data column `e_q` of `f` to an idling location on `q` with the
fault `X_q` (residual `(e_q,0)`). Distinct columns get distinct locations, and in V1 every data
qubit has an idling location (no depth bound: run the checks one after another, one CNOT per step;
and no `q` is addressed by *every* CNOT, else every check would have support `{q}`, contradicting
`H_X H_Z^T = 0`).
The joint residual is `(u,0)`: undetectable and nontrivial. So `D(M) ≤ s`; mirror for `Z`. ∎

**Scope note (what is derived, and what is a reading).** 公共定义 fixes `d_eff(M) := d_ext(E(M))`
but never constructs `E(M)`. Lemma 1.4′ derives `D(M) = min(d_eff^X, d_eff^Z)`, and `D(M)` is
stated without reference to any extended code. Consequently **any** reading of `E(M)` that (i)
counts elementary-fault **locations** and (ii) calls a fault assignment harmful exactly when its
terminal residual data Pauli is undetectable and nontrivial returns `D(M)`, hence the same number.
The residual conditionality is confined to readings that abandon (i) or (ii) — e.g. one that counts
*generators of a location's residual group* rather than locations, or one that also uses detector
outcomes (which is `d_circ`, not `d_eff`; cf. Lemma 1.2 and node `CIRCDIST.lift`).
<!-- R2: END -->

### 1.7 The residual, stated precisely

**What is now derived.** Steps (i), (ii) and (iii) of the §1.1 table. In particular the two things
the record called asserted — "the identification of `d_ext` with the mechanism minimum" and the
sector split — are proved from Model (M) M1–M4, the CNOT propagation rules, and `F_2` linear
algebra, with no external input and no promise on the code.

**What is not derived, exactly.** One thing: that **Definition E is the `E(M)` 公共定义 intends**.
This is a definitional reading, not a theorem, because 公共定义 supplies a phrase and not a
construction. Its scope is bounded by the scope note in §1.6: any construction satisfying (i)
location-counting and (ii) the terminal-residual harm criterion agrees with `D(M)` on the nose, so
the residual bites only on readings that reject (i) or (ii). I know of no such reading in the
fault-tolerance literature, and the write-up uses none. **Recommended registration:** a one-line
model-fact assumption on the node — *"`E(M)` is the hook-error extended code of Definition 1.3′;
`d_ext` counts fault locations, and a fault assignment is harmful iff its terminal residual data
Pauli is undetectable and nontrivial (M4). Derived consequence: `d_ext(E(M)) = min(d_eff^X,
d_eff^Z)`, Lemma 1.4′."* — rather than the current situation, in which the bridge is invisible to
the machine-checkable record while carrying every clause.

**What this does *not* do.** It does not touch the *other* half of the shared-model exposure that
the wave-19 review §6(a) calls systemic: Lemma 1.1's own fault model (which elementary faults M3
admits, and that the ideal terminal readout is the right boundary) is a modelling choice frozen in
公共定义, and no amount of internal derivation can test it. My simulator implements the same M3.
That caveat must ride permanently; Lemma 1.4′ removes a *derivation* gap inside the model, not the
model's own exposure.

### 1.8 Local verification (NUMERICAL)

Full script in §8.1, full stdout in §8.2, both this session's. The circuit side is computed by
laying out `C(M)` operation by operation and pushing Pauli faults through it; **it never calls the
Definition-1.3 code path**, and the two implementations share only the `F_2` primitives. Test set:
20 codes — `[[4,2,2]]`, Steane `[[7,1,3]]`, rotated `[[9,1,3]]`, Shor `[[9,1,3]]`,
`HGP(rep₃,rep₃) = [[13,1,3]]`, `G_{≠3}` (`n = 12`), and 14 random CSS codes with `n ∈ [7,10]`,
`k ≥ 1`, `d ≥ 2`.

```text
PART A -- Proposition A: the single-location residual classification
codes: 20      (schedule, sector) cases: 120      mismatches: 0
check supports chi_supp(c) realised as a one-fault residual : 396
   ... of which NOT in Cols_X(M)/Cols_Z(M)                  : 396

PART B -- the bridge:  D(M) [circuit]   vs   min(d_eff^X, d_eff^Z) [Definition 1.3]
(code, schedule, interleaving) triples tested : 200
joint value D(M) beat both sectors            : 0
joint value D(M) exceeded the sector minimum  : 0
DISAGREEMENTS                                 : 0

PART C -- the capped value 3 is a true value: explicit 3-location witness
   (6/6 named codes: an explicit idle-fault assignment on a minimum-weight logical
    is undetectable and nontrivial, so the search's cap is attained)

PART D -- Lemma 1.2: D(M) does not move with the interleaving of the blocks
(code, schedule) pairs over 4 interleavings each : 40      D(M) moved: 0

PART E -- every column of Cols_X(M) is realised by a PURE-X-type elementary fault
          at a location of its own
(code, schedule, sector) cases: 120    columns placed at distinct locations: 2148    failures: 0
```

**How to read this.** Part B is the theorem itself, on 200 independent instances, with the two
one-sided failure modes counted separately and both zero: the joint fault model never beats the
sector minimum (which would refute (≥)) and never exceeds it (which would refute (≤)). The rows in
§8.2 show the test is not vacuous — `D(M)` takes the values 1, 2 and 3 across the sweep, and moves
with the schedule (e.g. rotated `[[9,1,3]]`: `2,2,2,3`; Shor: `1,2,3`), so agreement is agreement on
a moving target. Parts A and E are the two halves of the proof of Theorem B verified separately.
Part D is a free by-product: Lemma 1.2 (order-determinacy) verified on the circuit rather than
inferred from Lemma 1.1.

**Search-space statement.** `D(M)` and `d_eff^sector(M)` are both computed exactly for values `1`
and `2` and capped at `3`; Part C exhibits, for each named code, an explicit 3-location assignment
realising a logical, so on the `d(Q) = 3` codes the capped value `3` is the true value and the
comparison is exact. On the `d(Q) = 2` codes all values are `≤ 2` and exact. Fault types enumerated
per location: `2` generators (1-qubit) or `4` generators (2-qubit), i.e. the full local Pauli group,
not a sample.

### 1.9 Dependent passages of R2

Located by `grep -n "Lemma 1\.4"` over the dossier at the digests of §0; every occurrence is listed.

| # | file · line | text | disposition under R2 |
|---|---|---|---|
| 1 | `writeup` §1.3, 147–155 | Lemma 1.4 statement + argument | **replaced** by the R2 block (Definition 1.3′, Lemma 1.4′) |
| 2 | `writeup` §1.4, 195 | Prop 1.11: "*one per check, both sectors, on disjoint variable sets by Lemma 1.4*" | **now derived**, not assumed; read as Lemma 1.4′. No text change needed |
| 3 | `writeup` §1.4, 199 | Prop 1.11's proof: "*Immediate from Definition 1.3, Lemma 1.4, Lemma 1.5, …*" | read as Lemma 1.4′; no text change needed |
| 4 | `writeup` §2.1, 275–277 | Prop 2.1 (sector factorisation): "*By Lemma 1.4 and Proposition 1.11 the two sector CSPs have disjoint variable sets*" | read as Lemma 1.4′. **This is the passage Island V's clause leans on** (§2 below), so the upgrade matters there specifically |
| 5 | `amendment1` §8 item 7, 774 | "*Lemma 1.4's identification of `d_ext(E(M))` with the mechanism minimum is asserted, not …*" | **discharged** by §1.6, modulo the §1.7 definitional residual |
| 6 | `amendment2` §5, 202 | carries the item forward in a list | discharged, same |
| 7 | `amendment3` §5, 225 | carries the item forward in a list | discharged, same |
| 8 | `amendment4` §2.1, roll-up **row 4** | "*Lemma 1.4's `d_ext` / mechanism bridge — open*" | **row 4 → derived (Amdt 5 §1), with the §1.7 definitional residual registered as a model-fact assumption; no longer "open"** |
| 9 | node caveat "BLOCKER 2" | "*must be derived (or the dependence removed) and reviewed before any completion level*" | the "derived" half is done here; the "**reviewed**" half is **not** and remains the gate — this amendment is unreviewed |

Note the asymmetry in row 9 deliberately: `PROVED` needs the bridge *reviewed*, and a proposer
deriving his own bridge is not a review. The most this amendment can move is "asserted, underived"
→ "derived, unreviewed".

---

## 2. R1 — the corrected Island V clause: a candidate, from Theorem V.4's exact words

### 2.1 The three exact statements the clause must respect

**Theorem V.4**, verbatim (`writeup` lines 1180–1182):

> **Theorem V.4 (`k ≤ 1` forces YES) — CONJECTURED.** Under the promise of §6.1, if `k ≤ 1` then
> **every** choice-free instance is a YES: there is a schedule with `d_eff^X(M) ≥ 3`, and it is found
> in linear time.

**The promise of §6.1**, verbatim (lines 1056–1060):

> **Problem `Eff-Preserve≥^X[w ≤ 4, d_X ≥ 4]`.**
> *Input:* `H_X, H_Z` with `H_X H_Z^T = 0`; the integer `d = 3`.
> *Promise:* `d(Q) = 3` and `k ≥ 1`; **every X-check has weight `≤ 4`**; and `d_X ≥ 4`
> (hence `d_Z = 3`, since `d = min(d_X,d_Z) = 3`).
> *Question:* is there a tuple of local orders of the X-checks with `d_eff^X(M) ≥ 3`?

**§6.6's first scope bullet**, verbatim (lines 1300–1301):

> * **One sector only.** The hypotheses force `d_Z = 3`; the Z-sector is untouched and must be
>   settled separately (Proposition 2.1). Island V alone never decides an Eff-Preserve instance.

Four hypotheses, then, not two: `d(Q) = 3` with `k ≥ 1` (ambient), X-check weight `≤ 4`, **`d_X ≥ 4`**,
and `k ≤ 1`. And one conclusion, `d_eff^X(M) ≥ 3` — **an X-sector statement, not an Eff-Preserve
verdict**. Two further precisions worth carrying into the clause: (a) under §6.1's promise `k ≥ 1`,
"`k ≤ 1`" means `k = 1` exactly, and the `k = 0` branch of V.4's proof is vacuous there; (b) V.4's
X-sector YES combines with a separate Z-sector answer through **Proposition 2.1**, whose proof (§1.9
row 4) rests on Lemma 1.4 — now Lemma 1.4′.

### 2.2 The candidate clause

Offered for the dispatcher to accept, amend or decline. It is **not** re-added by this file.

<!-- R1: BEGIN -->
**Candidate Island V clause (Unicode form, for prose).**

> …and, in the `X`-sector only, the `k ≤ 1` regime at `d = 3` with every `X`-check of weight `≤ 4`
> and `d_X ≥ 4`, where a schedule with `d_eff^X(M) ≥ 3` always exists and is found in linear time
> (Theorem V.4) — an `X`-sector guarantee, **not** by itself an Eff-Preserve verdict: the `Z`-sector
> carries no weight bound and must be settled separately (Proposition 2.1, e.g. by Island I, III or
> IV).

**Candidate Island V clause (ASCII form, for the node `claim` field).**

> and the X-sector at d = 3 under k <= 1, X-check weight <= 4 and d_X >= 4 (Theorem V.4: a schedule
> with d_eff^X >= 3 always exists and is found in linear time -- an X-sector guarantee only, not by
> itself an Eff-Preserve verdict; the Z-sector must be settled separately)

**What the clause deliberately does not say.** (1) It does not say "unconditional YES" — the YES is
conditional on `d_X ≥ 4` and is one sector's. (2) It does not say "Eff-Preserve", because §6.6
forbids it. (3) It does not claim the general `k ≥ 2` case, which is open (`task-004`) and where the
`K₄` composite is a NO. (4) It does not claim Theorem V.5's matching reading, which needs
hypothesis (D). (5) It says `k ≤ 1` rather than `k = 1` to match Theorem V.4's own words, with the
note above that the ambient promise makes them the same.

**If the dispatcher prefers the minimal action**, the alternative is to leave the claim at four
islands and record Theorem V.4 in the caveat set instead. That is defensible: the clause above is a
one-sector sub-result, and a claim sentence about "restricted classes of **Eff-Preserve** in P" is
arguably not the place for it. What is **not** defensible is the deleted wording, for the reason
below.
<!-- R1: END -->

### 2.3 The refutation of the old wording, re-verified independently

I did not take the wave-19 review's Steane computation on trust; I recomputed it with my own code
(§8.1), enumerating **all** `24³ = 13 824` X-schedules and **all** `24³ = 13 824` Z-schedules
exhaustively — not a sample.

```text
PART F -- Steane [[7,1,3]]: exhaustive over ALL schedules, both sectors
n=7 k=1 d_X=3 d_Z=3 d(Q)=3   X-check weights [4, 4, 4]
conditions the DELETED clause named (k <= 1 ; X-weight <= 4) : True
ambient promise (d(Q) = 3 exactly ; k >= 1)                  : True
section 6.1 promise (adds d_X >= 4)                          : False
  sector X : 13824 schedules enumerated, max d_eff^X over all of them = 2
  sector Z : 13824 schedules enumerated, max d_eff^Z over all of them = 2
  => Eff-Preserve(Steane, d = 3) = NO
  corrected clause requires d_X >= 4; Steane has d_X = 3  =>  EXCLUDED: True
```

So: Steane satisfies every condition the **deleted** clause named and the ambient promise, and is a
**NO** — the deleted clause was false, not merely under-hedged. And the **candidate** clause excludes
it at the first hypothesis, `d_X ≥ 4` (Steane has `d_X = 3`). Note the exhaustive maxima are `2` in
*both* sectors, which is a stronger statement than "the X-sector fails": no schedule of Steane
preserves distance in either sector at `d = 3`.

Non-vacuity of the candidate clause is not left to chance either — §4 exhibits an explicit instance
satisfying all four hypotheses, and measures `d_eff^X = 3` on Theorem V.4's own constructed schedule.

### 2.4 Dependent passages of R1

| # | location | disposition |
|---|---|---|
| 1 | node `claim`, Island V clause | **deleted** by the wave-19 narrowing; the candidate above is offered for re-addition. **Re-adding changes the claim and therefore the claim hash**; every review bound to the narrowed text must be re-bound or re-run |
| 2 | `writeup` §6 heading, line 1048 ("*the weight-4 / `d_X ≥ 4` regime*") | already correct — it is the claim that had dropped the second half, not the dossier |
| 3 | `writeup` §7.1 table, row V ("*weight-`≤ 4` / `d_X ≥ 4`*") | already correct; unchanged |
| 4 | `writeup` §6.6 bullets 1 and 2 | already correct; they are the source of the clause's hedges. Unchanged |
| 5 | node caveat "Island V scope" | must now read `k ≤ 1` **and** X-weight `≤ 4` **and** `d_X ≥ 4`, **X-sector only** — as the wave-19 caveat list item 4 already states |
| 6 | `writeup` §2.1 Prop 2.1 | the composition rule the clause's hedge points at; its proof is upgraded by §1 (Lemma 1.4′) |

---

## 3. R3 — write-up §4.4: the division of labour, and the HR-width bridge

### 3.1 What is wrong, by quotation

`writeup` §4.4's source list pins three things, and the wave-18 primary-source verification
(`circdist_courcelle_primary_20260823.md`, digest in §0) found two of the three attributions wrong
and one locator pointing at a result of the opposite polarity. The three defective passages,
verbatim:

> * **[ALS91]** … This is the paper usually cited for the explicit **linear-time algorithmic form**
>   (given the decomposition) and for the extension of the logic with counting/evaluation.

> * **[CE12]** … Cited for the **MSO₂** half: quantification over edge sets is MSO₁ over the
>   incidence structure, and the bounded-treewidth theorem applies there
>   (*Proposition 5.13, p. 338* — theorem number taken from the secondary source above, **not**
>   verified against the book).

> **Honest note on the pin.** The *statement* above is standard and is what the island needs; what
> this session could not do inside the box is quote a theorem number from a primary text. …

The wave-18 file's findings, quoted as data: `[CE12]` **Proposition 5.13** is *"The following
properties are not MS-expressible: (1) Two sets `X` and `Y` have equal cardinality. …"* — an
**MS₁ inexpressibility** result, the book's *motivation* for edge-set quantification, not the
theorem; `[Cou90]` **already contains** both the linear-time algorithmic form (Proposition (4.14)(1))
and edge-set quantification (Definition (3.2), set variables of sort `e`); and `[ALS91]`'s full text
was unobtainable, so no theorem number in it is verified. Theorem III is stated "*modulo the pinned
external theorem of §4.4*" (line 840), so as assembled the dossier's external input points at the
wrong proposition. That is the defect.

### 3.2 The exact replacement

**Replace `circdist_cplx_islands_writeup_20260820.md` §4.4, lines 794–836 (the "Sources, split by
which half each one supplies" list and the "Honest note on the pin" paragraph) by the following
block.** The boxed *statement* at lines 787–792 is unchanged — the wave-18 verification found it
sound and found Island III's usage conservative relative to it.

<!-- R3: BEGIN -->
**Sources, split by which half each one supplies — corrected by Amendment 5 after primary-source
verification (`artifacts/circdist_courcelle_primary_20260823.md`).** The earlier split in this
section was wrong in two of its three places and pinned a locator of the opposite polarity; what
follows replaces it.

* **[CE12] — the load-bearing citation, and the one that closes.** B. Courcelle, J. Engelfriet,
  *"Graph Structure and Monadic Second-Order Logic: A Language-Theoretic Approach"*, Cambridge
  University Press, 2012 (series designation *Encyclopedia of Mathematics and its Applications* 138:
  secondary-source data, see the provenance note below). The statement Island III uses is
  **Theorem 6.4(1)** (draft p. 429), §6.1 "Fixed-parameter tractable algorithms for model-checking":
  *"For all finite sets `K` and `Λ` of vertex and edge labels, the model-checking problem
  `MC(JS[K,Λ][∅], CMS₂)` is fixed-parameter linear with respect to `(twd(G), φ)`, where `G` is the
  input graph and `φ` is the input sentence."* Supporting locators in the same book:
  **Theorem 5.68(2)** (draft p. 397, *"Every `CMS₂`-definable set of (labelled) `s`-graphs is
  effectively HR-recognizable"*) and **Definition 5.17** (draft p. 345, the incidence representation
  `⌈G⌉ = ⟨V_G ∪ E_G, in_G⟩`, which is this island's carrier `𝔗`). Theorem 6.4(1) is parameterized by
  `twd(G)` and **computes the decomposition internally**, so it grants strictly more than the boxed
  statement above demands; §4.5's two-case time bookkeeping and the separately cited Bodlaender
  results are, against 6.4(1), surplus rather than necessary.
  ~~*Proposition 5.13, p. 338*~~ — **withdrawn.** Proposition 5.13 states that certain properties
  are **not** MS-expressible (equicardinality, Hamiltonicity, perfect matching, nontrivial
  automorphism). It is an MS₁ **inexpressibility** result of the opposite polarity, the book's
  motivation for introducing edge-set quantification (§5.2.5 cross-references it for exactly that),
  and it contains no incidence structure, no tree-width and no algorithm. The mis-pin was
  page-self-consistent — 5.13 really does sit at pp. 337–338 — so only reading the statement caught
  it.
* **[Cou90] — the second, independent route; primary text read in full.** B. Courcelle, *"The
  Monadic Second-Order Logic of Graphs. I. Recognizable Sets of Finite Graphs"*, **Information and
  Computation 85, 12–75 (1990)** (header verbatim from the paper). It supplies **more** than this
  write-up originally credited it with:
  **Definition (3.2)** introduces the counting atoms `card_{n,p}(U)` and fixes "definable" to mean
  CMSO-definable — this is the `CMSO`-over-`MSO` half, which Island III genuinely needs for
  `InStab` (unbounded data-qubit degree); the same definition declares set variables *"of sort `v` or
  `e`"*, so **edge-set quantification is already here** and was wrongly outsourced to [CE12];
  **Theorem (4.4)**, *"Every definable subset of `FG(A)_k` is an effectively given recognizable set
  of graphs"*; and **Proposition (4.14)(1)**, which decides `φ ∈ CMS_{A,k,q}` in time `O(size(e))`
  for a given expression `e` — i.e. **the linear-time algorithmic form is already here too**, and was
  wrongly attributed to [ALS91]. Two hypotheses this write-up's paraphrase drops: [Cou90]'s objects
  are directed hyperedge-labelled hypergraphs with sources (`FG(A)_k`) — immaterial, `𝔗` is well
  inside that class — and its parameter is **HR-expression width, not tree-width** (see the bridge
  note below).
* **[ALS91] — demoted to corroborating, not load-bearing.** S. Arnborg, J. Lagergren, D. Seese,
  *"Easy Problems for Tree-Decomposable Graphs"*, *Journal of Algorithms* **12**(2) (1991) 308–340.
  Bibliographic data verified exactly against two independent indexes (DBLP `journals/jal/ArnborgLS91`
  and Semantic Scholar via publisher DOI `10.1016/0196-6774(91)90006-K`), **full text not obtained**
  (publisher paywall; `openAccessPdf: CLOSED`), **theorem numbers unverified**. Its role in the
  original split — the linear-time form — is discharged twice over by texts that *were* read in full
  ([Cou90] Prop (4.14)(1); [CE12] Thm 6.4(1)), and its counting/evaluation extension is not used by
  Island III at all. It is retained as a customary citation and carries no weight in Theorem III.
* **The HR-width ↔ tree-width bridge, registered explicitly.** [Cou90] never uses the words
  "tree-width" or "tree decomposition" (the sole occurrence in that paper is a bibliography entry),
  and Proposition (4.14)(1)'s input is an **HR expression** `e` of width `≤ m` over the
  source-labelled graph algebra, not a tree decomposition. The standard equivalence — *a graph has
  an HR expression of width `≤ m` iff its tree-width is `≤ m − 1`*, so that a width-`t` tree
  decomposition yields an expression of width `t+1` — is what converts Prop (4.14)(1) into the boxed
  statement. It is **not in [Cou90]**. It is available in [CE12], whose Theorem 6.4(1) obtains its
  decomposition via Theorem 1.25 and converts it into an HR term via **Theorem 2.83** (draft
  numbering; recorded by the wave-18 verification, which read the draft — *this dossier has not read
  Theorem 2.83's statement itself, so the bridge carries one step of indirection and is not
  primary-verified here*). Coverage of this island's usage: `𝔗` has tree-width `≤ t + 1` (§4.2), so
  the bridge is invoked at `m = t + 2`, well inside its range. **Island III does not depend on it**,
  because the route actually taken is [CE12] Theorem 6.4(1), which is already stated in terms of
  `twd(G)`.
* **Consequently: one closed chain, not two.** The [CE12] chain (Def 5.17 + Thm 5.68(2) +
  Thm 6.4(1)) closes with no unregistered external fact. The [Cou90] chain (Def (3.2) + Thm (4.4) +
  Prop (4.14)(1)) closes only *modulo* the HR-width bridge above. Earlier language describing the
  verification as "two disjoint chains" over-states the record by one; one chain suffices, and it
  closes.
* **Tree decomposition, if it must be computed:** H. L. Bodlaender, *SIAM J. Comput.* **25**(6)
  (1996) 1305–1317 (`2^{O(t³)} n`); or the `c^k n` 5-approximation, Bodlaender–Drange–Dregi–
  Fomin–Lokshtanov–M. Pilipczuk, *SIAM J. Comput.* **45**(2) (2016) 317–378. *Standard; not
  re-verified; redundant against [CE12] Thm 6.4(1) (§4.5's second time bound is kept only for
  readers who prefer the "decomposition supplied" formulation).*
* **The parameter dependence is unavoidably bad:** M. Frick, M. Grohe, *Ann. Pure Appl. Logic*
  **130**(1–3) (2004) 3–31. *Bibliographic data from a secondary source; supports a scope clause
  (§4.6), not a theorem.*

**Provenance note on the [CE12] locators — added by Amendment 5.** Every [CE12] theorem, definition
and page number in this dossier is read from the **April 2011 authors' pre-publication draft**
(`labri.fr/perso/courcell/Book/TheBook.pdf`, linked from the authors' book page), **not** from the
printed 2012 CUP edition. That draft's title page reads "to be published by Cambridge University
Press" and **does not carry a series designation**, so *"Encyclopedia of Mathematics and its
Applications 138"* and the printed pagination remain **secondary-source data**. Draft numbering is
plausibly stable — the draft's own p. 338 coincides with the page the withdrawn pin named — but **no
number here has been checked against the print edition, and page numbers may shift**. Cite these by
number-and-name (`Theorem 6.4(1)`, `Theorem 5.68(2)`, `Definition 5.17`, `Theorem 2.83`), not by
page.

**Honest note on the pin, replacing the earlier one.** The boxed statement above is now
primary-source verified: [Cou90] was read in full from the author's homepage (bibliographic header
verbatim, OCR text layer — prose and theorem numbers extract cleanly, mathematical symbols do not),
and the [CE12] draft was read in full. What remains open at the citation layer is exactly three
things, all recorded above: [ALS91]'s text (paywalled, immaterial), the print-edition numbering of
[CE12] (draft-only), and the statement of [CE12] Theorem 2.83 (needed by the [Cou90] route only,
which is not the route Theorem III takes). No mathematical defect was found in what this island
assumes, and the island's usage is *conservative* relative to what both texts grant.
<!-- R3: END -->

### 3.3 Dependent passages of R3

Located by `grep -n "§4\.4\|ALS91\|CE12\|Cou90\|Prop.* 5\.13"` over the dossier.

| # | file · line | text | disposition |
|---|---|---|---|
| 1 | `writeup` §4.4, 794–836 | the source split and the honest note | **replaced** by the R3 block |
| 2 | `writeup` §4.4, 787–792 | the boxed CMSO₂ statement | **unchanged** — verified sound; Island III assumes strictly less than [CE12] 6.4(1) grants |
| 3 | `writeup` §4, 658 | "*The recon (premise P6.3) flagged this island's **citation** as the one missing piece. §4.4 pins it.*" | still true; the pin is now correct and primary-verified |
| 4 | `writeup` §4.5, 840 | Theorem III "*— CONJECTURED (modulo the pinned external theorem of §4.4)*" | the modulus now points at [CE12] Thm 6.4(1); Theorem III's conditionality is **unchanged in kind**, discharged in substance |
| 5 | `writeup` §4.5, 848–849 | "*Apply the theorem of §4.4 to `𝔗` (whose treewidth is `≤ t + 1`)*" | unchanged; against 6.4(1) one may equally apply it to the Tanner graph with parameter `twd(G) ≤ t`, and `tw(Inc(G)) ≤ tw(G)+1` becomes surplus |
| 6 | `writeup` §4.6, 883 | "*§4.4 is the part that needs a citation check*" | **discharged** (wave-18 + this block) |
| 7 | `writeup` §7.3 item 4, 1366 | "*the Courcelle citation pinned (§4.4)*" | unchanged in force; the pin is corrected |
| 8 | `writeup` §7.4, row `C1`, 1377 | status column "*bibliographic data confirmed via secondary sources; primary texts not read; theorem numbers not verified*" | **superseded** — see R4 (§6) for the exact replacement row |
| 9 | `writeup` §7.5, 1404–1406 | "*The Courcelle pin has a residual … no theorem number was verified against a primary text.*" | **discharged** for [Cou90] and [CE12]; **stands** for [ALS91] |
| 10 | `writeup` §7.6 item 3, 1421 | "*Do the 15-minute primary-source checks … the Courcelle theorem number (§4.4) and A9*" | Courcelle half **done**; A9 half **still open** |
| 11 | node `assumptions.courcelle-c1` | already carries the corrected [CE12] locator and the [ALS91] demotion | needs the two additions of R4 (§6): the 2011-draft provenance, and the HR-width bridge / "one closed chain" softening |

---

## 4. R6 — §6.1's promise is witnessed: an instance is cited

Islands-review **edit 11** (quoted verbatim in Amendment 4 §2) asked to *"exhibit one code satisfying
the promise verbatim (weight-4 X-checks, `d_X ≥ 4`, `d_Z = 3`), or relax the stated promise"*.
Amendment 4 §2.1 row 8 recorded it **unsatisfied and "currently un-witnessed"**, on the strength of
an absence result (≈10⁶ random draws, no hit). The wave-19 review found a witness by rebuilding
`G_{≠3}`. I rebuilt it independently from the gadget document's printed parity checks and confirm
the finding; the absence evidence was simply looking in the wrong place.

### 4.1 The exact addition

**Add to `circdist_cplx_islands_writeup_20260820.md` §6.1, immediately after the "*Generalisation
over the source document*" paragraph (after line 1072), the following block.**

<!-- R6: BEGIN -->
**Witness — the promise is satisfiable verbatim (added by Amendment 5; NUMERICAL, recomputed this
session from the printed parity checks).** Take `G_{≠3}` of `circdist_cplx_gadget_20260820.md` §3.2:
`n = 12`, X-checks `(0,1,2,3)`, `(4,5,6,7)`, `(1,4,8,10)`, `(0,6,8,11)`, `(3,7,9,10)`; Z-checks
`(1,2,4,7,9)`, `(0,1,6,7,10)`, `(0,1,2,3,8,9)`, `(0,1,4,5,11)`, `(0,2,4,6,8,11)`,
`(4,5,6,7,10,11)`, `(8,9,10,11)`. Exhaustive enumeration gives `k = 2`, `d_X = 4`, `d_Z = 3`,
`d(Q) = 3`, all five X-checks of weight exactly 4 — **§6.1's promise, verbatim, except that `k = 2`**.

`G_{≠3}` has exactly **eight** weight-3 Z-logicals: `{0,1,8}`, `{0,2,11}`, `{1,3,10}`, `{2,3,9}`,
`{4,6,8}`, `{4,7,10}`, `{5,6,11}`, `{5,7,9}`. Adjoining any one of them as a further Z-check leaves
`H_X H_Z^T = 0` (it is in `ker H_X`), lowers `k` to `1`, and preserves `d_X = 4`, `d_Z = 3`,
`d(Q) = 3` and the weight-4 X-checks: **8 of 8 do**. So §6.1's promise is satisfiable verbatim, and
Theorem V.4's hypothesis `k ≤ 1` is non-vacuous inside it.

**The instance cited for the record** is `G_{≠3}` **+ Z-check** `{0,2,11}` — `n = 12`, `k = 1`,
`d_X = 4`, `d_Z = 3`, `d(Q) = 3`, five weight-4 X-checks. Running Theorem V.4's own construction on
it (splitting `Q = Log ⊕ N`, projection `β`, one `β = 0` option per weight-4 check) yields the
schedule `(0,3,1,2)`, `(4,5,6,7)`, `(1,4,8,10)`, `(0,11,6,8)`, `(3,9,7,10)`, whose `d_eff^X`
measured directly from Definition 1.3 is **3**, as V.4 asserts. The parity argument is visible in the
data: the three `2|2` splits of the five checks have `β`-patterns `[1,1,0]`, `[0,0,0]`, `[0,0,0]`,
`[1,1,0]`, `[1,0,1]` — every one has an even number of `1`s, hence a `0`, exactly as Lemma V.1(5)
forces. Pairing this X-schedule with a Z-schedule found by search (`d_eff^Z = 3`) makes the whole
instance a **YES** for Eff-Preserve at `d = 3`, so the `k ≤ 1` regime is not only non-empty but
contains genuine YES instances of the full problem.
<!-- R6: END -->

### 4.2 Local verification (NUMERICAL)

Own code (§8.1), rebuilt from the gadget document's printed parity checks; the distances are full
enumerations over `F_2^{12}`, not samples.

```text
PART G -- G_neq3 and its k = 1 augmentations against section 6.1 VERBATIM
G_neq3 : n=12 k=2 d_X=4 d_Z=3 d(Q)=3  X-check weights [4, 4, 4, 4, 4]
section 6.1 verbatim (d(Q)=3, k>=1, X-weight<=4, d_X>=4) : True
weight-3 Z-logicals : 8  ->  [(0,1,8),(0,2,11),(1,3,10),(2,3,9),(4,6,8),(4,7,10),(5,6,11),(5,7,9)]
   ... every one gives k=1 d_X=4 d_Z=3 d=3 ...
augmentations with k = 1 meeting 6.1 verbatim : 8 / 8

PART H -- Theorem V.4's construction on the cited instance; d_eff^X measured
G_neq3 + Z-check (0,2,11) : n=12 k=1 d_X=4 d_Z=3 d(Q)=3
dim Log = k = 1 ; a representative ell of weight 4 ; splitting coordinate 0
   check (0, 1, 2, 3)   beta of the three 2|2 splits = [1, 1, 0]  ->  order (0, 3, 1, 2)
   check (4, 5, 6, 7)   beta of the three 2|2 splits = [0, 0, 0]  ->  order (4, 5, 6, 7)
   check (1, 4, 8, 10)  beta of the three 2|2 splits = [0, 0, 0]  ->  order (1, 4, 8, 10)
   check (0, 6, 8, 11)  beta of the three 2|2 splits = [1, 1, 0]  ->  order (0, 11, 6, 8)
   check (3, 7, 9, 10)  beta of the three 2|2 splits = [1, 0, 1]  ->  order (3, 9, 7, 10)
d_eff^X of Theorem V.4's schedule, measured from Definition 1.3 : 3   (V.4 asserts >= 3)
Z-sector random search : best d_eff^Z = 3 after 94 draws
full-circuit D(M) on (V.4 X-schedule, searched Z-schedule) = 3 ; sector min = 3
=> Eff-Preserve(cited instance, d = 3) = YES
```

The last two lines are a free cross-check of §1: on this instance the circuit-level `D(M)` and the
Definition-1.3 sector minimum agree at `3`.

### 4.3 Dependent passages of R6

| # | location | disposition |
|---|---|---|
| 1 | `writeup` §6.1, after line 1072 | **addition** — the R6 block |
| 2 | `amendment4` §2, "*§6.1's promise is currently un-witnessed*" and the ≈10⁶-draw absence evidence | **superseded**: the promise **is** witnessed. The absence result is not contradicted — it was a random-sampling statement over an unstated distribution, and `G_{≠3}` was constructed, not sampled |
| 3 | `amendment4` §2.1 roll-up **row 8** (islands-review edit 11) | **discharged**, not merely relabelled: an instance is cited (edit 11's first alternative), so the promise need not be relaxed |
| 4 | islands review §9 item 11 | satisfied by the first alternative |
| 5 | node caveat, "*N3 erratum confirmed … dossier should cite an instance*" | **done** |
| 6 | `writeup` §6.4 "*Consistency check*" (the `K₄` instance, `k = 6`) | unchanged and still consistent: `k ≥ 2` is what admits NO instances, and the cited witness has `k = 1` |

---

## 5. R5 — HGP: hypothesis-failure is not conclusion-failure (and islands-review edit 9)

### 5.1 What is wrong

The node caveat had read that the non-degeneracy proviso was *"shown NECESSARY by the review
(46/1971 promise-satisfying instances violate the bound without it)"*. The islands review's own
sentence (line 285–287) is:

> **The proviso is genuinely necessary.** I attacked Theorem II.4's hypothesis by asking whether
> `d(Q) = min(μ_X, μ_Z)` is automatic under the `k ≥ 1` promise. **It is not**: 46 of 1971
> promise-satisfying instances have `d(Q) > min(μ_X,μ_Z)`.

That is a census of **hypothesis** failures — instances where Theorem II.4 may not be invoked. It is
**not** a census of instances where the **conclusion** `d_eff(M) = d(Q)` fails. The node caveat has
already been corrected by the wave-19 review; the **dossier** has not recorded the distinction at
all, and the same section is where islands-review **edit 9** (roll-up row 7, still unapplied) belongs.
Both are fixed by one addition.

### 5.2 The exact addition

**Add to `circdist_cplx_islands_writeup_20260820.md` §3.4, immediately after the closing paragraph
(after line 593), the following block.**

<!-- R5: BEGIN -->
**Two precisions about the proviso — added by Amendment 5.**

**(a) Hypothesis-failure is not conclusion-failure.** A census of the form "*`N` of `M`
promise-satisfying instances have `d(Q) ≠ min(μ_X, μ_Z)`*" counts instances where **Theorem II.4's
hypothesis fails**, i.e. where the theorem may not be invoked. It does **not** exhibit an instance
where the theorem's **conclusion** — that every schedule has `d_eff(M) = d(Q)` — is false, and no
such instance is on record anywhere in this dossier. (Recomputed for this amendment on 400 random
hypergraph products with `k ≥ 1`: **13** have `d(Q) ≠ min(μ_X, μ_Z)`, and on **0** of those 13 did
any of 200 random schedules per instance drop `d_eff` below `d(Q)`; an independent census reports
37 of 1075 and likewise 0.) Note also that by Corollary II.2 the inequality can only go one way:
`d(Q) ≥ min(μ_X, μ_Z)` always, so "`≠`" and "`>`" name the same set. The honest statement is: **the
proviso is necessary as a hypothesis of Theorem II.4 — the theorem's proof uses it and Corollary II.2
does not supply it — and it is not known to be necessary for the conclusion.** Nothing in §3 asserts
otherwise, and Theorem II.3's bound `d_eff(M) ≥ min(μ_X, μ_Z)` holds for **every** schedule with no
proviso at all.

**(b) Which hypothesis is testable (islands-review edit 9).** Theorem II.4's hypothesis
`d(Q) = min(μ_X, μ_Z)` is a **distance condition** and is not known to be poly-time checkable —
computing the minimum distance of a quantum code is NP-hard (ASSUMPTION A5), so this hypothesis is a
*promise*, not a test. Lemma II.5's hypothesis, by contrast, is `k_1 > 0 ⟺ k_2 > 0` and
`k_1^T > 0 ⟺ k_2^T > 0`, i.e. four kernel-dimension comparisons on the two seed matrices: **poly-time
checkable** in `O(n³)`. Consequently the **poly-time recognisable** constant-YES subclass of Island II
is the **Lemma II.5** one, not the Theorem II.4 one, and any statement that the HGP island is
"recognisable in polynomial time" must be read as being about Lemma II.5's class. Theorem II.4
remains the sharper statement about a larger class, granted the promise.
<!-- R5: END -->

### 5.3 Local verification (NUMERICAL)

```text
PART I -- HGP proviso census: hypothesis-failure is not conclusion-failure
random HGP instances with k >= 1 sampled     : 400
  Theorem II.4 hypothesis d(Q) = min(mu) HOLDS : 387
  Theorem II.4 hypothesis FAILS                : 13   (this is what a "46/1971"-style census counts)
  of those, an instance where some schedule drops d_eff below d(Q)
  (i.e. the CONCLUSION fails)                  : 0
  (200 random schedules per hypothesis-failing instance, both sectors,
   d_eff computed from Definition 1.3 and capped at 3)
```

Sampling distribution stated: `H_1, H_2` uniform `F_2` matrices with `1 ≤ m_i ≤ 3`, `2 ≤ n_i ≤ 4`,
retaining products with `n ≤ 16` and `k ≥ 1`; `μ_X = min(d(ker H_2), d(ker H_1^T))`,
`μ_Z = min(d(ker H_1), d(ker H_2^T))`; kernel distances by full enumeration. My rate (13/400 = 3.3 %)
sits between the two published ones (46/1971 = 2.3 %, 37/1075 = 3.4 %) — three different
distributions, same phenomenon, and the conclusion-failure count is `0` in all three.

### 5.4 Dependent passages of R5

| # | location | disposition |
|---|---|---|
| 1 | `writeup` §3.4, after line 593 | **addition** — the R5 block |
| 2 | `writeup` §3.4 closing paragraph ("*…in which case `d(Q)` can exceed `min(μ_X,μ_Z)` and Theorem II.4 must not be invoked*") | already correct; the addition sharpens it rather than correcting it |
| 3 | `writeup` §3.7 first scope bullet | unchanged; the addition is what the bullet's "not a formality" means precisely |
| 4 | `amendment4` §2.1 roll-up **row 7** (islands-review edit 9) | **discharged** by part (b) |
| 5 | islands review §9 item 9 | satisfied |
| 6 | node caveat "HGP caveat CORRECTED (wave-19)" | already correct; the dossier now matches it |
| 7 | node `claim`, HGP clause ("*so constant YES under the non-degeneracy proviso*") | **unchanged and correct** — it names the proviso as a condition. Part (b) is a caveat-level precision about *recognisability*, not a claim defect |

---

## 6. R4 — the C1 fourth-edit residue, in the dossier

The wave-19 review §6(c) records that the node's `assumptions` block applied "3.5 of 4" of the
wave-18 edits: the corrected `[CE12]` locators landed, the provenance half of the same edit did not.
§3.2's R3 block already carries the provenance note into the write-up. What remains is the dossier's
own external-results table.

### 6.1 The exact replacement

**Replace `circdist_cplx_islands_writeup_20260820.md` §7.4's `C1` row, and add the note below the
table (after line 1387), as follows.**

<!-- R4: BEGIN -->
| C1 | Courcelle's theorem, CMSO₂ form (§4.4) | **[CE12]** Courcelle–Engelfriet, CUP 2012, **Thm 6.4(1)** (+ Thm 5.68(2), Def 5.17); **[Cou90]** Courcelle, *Inform. and Comput.* **85** (1990) 12–75, **Def (3.2) + Thm (4.4) + Prop (4.14)(1)**; [ALS91] Arnborg–Lagergren–Seese, *J. Algorithms* **12**(2) (1991) 308–340 — corroborating only | **PRIMARY-VERIFIED** 2026-08-23 for [CE12] and [Cou90] (both read in full). **One closed chain, not two:** [CE12] Thm 6.4(1) is stated in `twd(G)` and closes; the [Cou90] route closes only modulo the HR-width ↔ tree-width bridge (§4.4), which [Cou90] does not contain. [ALS91]: bibliographic data verified against two indexes, **full text paywalled, theorem numbers unverified — not load-bearing**. **All [CE12] locators are to the April 2011 authors' draft, not the print edition**; "EMA 138" and print pagination remain secondary-source. Island III's usage is *conservative* relative to what both texts grant |

**Note on C1's provenance and scope — added by Amendment 5.** Three residues survive the
primary-source verification and are recorded rather than absorbed. (i) **[ALS91] was never read**;
it is retained as a customary citation and carries no weight — its obligation is discharged twice by
texts that were read. (ii) **The [CE12] numbering is the April 2011 authors' draft's.** The draft
does not carry the series designation, so "*Encyclopedia of Mathematics and its Applications* 138"
and the printed pagination are secondary-source data; page numbers may shift between draft and print,
so cite by number-and-name. (iii) **The HR-width ↔ tree-width bridge is a named dependency of the
[Cou90] route only**, is not in [Cou90], and its [CE12] locator (Theorem 2.83, draft numbering) was
recorded by the wave-18 verification rather than read by this dossier — one step of indirection,
flagged. Theorem III takes the [CE12] route and does not use it. Finally, the earlier registration's
phrase "**and its optimization extension**" was struck as over-registration: `Φ_{t,w,d}` is a plain
Boolean CMS₂ sentence, and the "counting" Island III needs is the modular cardinality predicates
`card_{r,p}` of [Cou90] Def (3.2), a different thing.
<!-- R4: END -->

### 6.2 Dependent passages of R4

| # | location | disposition |
|---|---|---|
| 1 | `writeup` §7.4 row `C1` | **replaced** by the R4 block's row |
| 2 | `writeup` §7.4, below the table (after line 1387) | **addition** — the R4 note |
| 3 | `writeup` §7.5 bullet "*The Courcelle pin has a residual*" | superseded by the R4 note (which is finer-grained) |
| 4 | node `assumptions.courcelle-c1.statement` | **needs two additions** the block above supplies verbatim: the 2011-draft provenance sentence, and the "one closed chain, not two" softening with the HR-width bridge named. The node is canonical and was not touched by this session; the dispatcher applies it |
| 5 | node caveat "*'two disjoint chains' overstated (Cou90's parameter is HR-width; the width-treewidth bridge is registered nowhere)*" | **the bridge is now registered** — in §4.4 (R3) and in §7.4 (R4). The caveat can be retired once the node text is updated |

---

## 7. Verification checklist, and what this amendment does not do

- [x] Recomputed the SHA-256 digest, byte count and line count of all eleven bound inputs of §0 from
      current bytes before writing this file; the four dossier digests reproduce the values
      Amendment 4 §0 and the wave-19 review §2 assert.
- [x] Quoted every passage being replaced verbatim from the file at its bound digest, with line
      numbers, before giving a replacement.
- [x] Supplied an **exact replacement block** for each of R2, R3, R5, R6, R4 and an exact
      **candidate** for R1, each delimited by markers so its content digest can be re-derived (§0.1,
      extractor in §8.3).
- [x] Gave a **per-repair dependent-passage list** located by `grep` over the whole dossier (§§1.9,
      2.4, 3.3, 4.3, 5.4, 6.2); no occurrence found by the greps is left unclassified.
- [x] Wrote every line of code in §8.1 for this amendment; it reuses **no** code from the dossier,
      from the wave-19 review, or from the gadget document. The stdout in §8.2 is that script's own,
      pasted unedited, from the run whose digests are recorded in §8.2's header.
- [x] Re-derived, rather than imported, every number quoted in §§2.3, 4.2, 5.3 — including the
      Steane refutation (exhaustive, both sectors) and `G_{≠3}`'s spectrum (full `F_2^{12}`
      enumeration from the gadget document's *printed* parity checks).
- [x] Modified **no** canonical file. `research/circdist/proof-dag/` was read only; no node, route,
      assessment or level was touched; no claim was re-added and no hash was bound to a claim.

**What this amendment does not do, stated plainly.**

1. **It does not review itself.** §1's derivation is proposer-side. The node's blocker 2 has two
   halves — *derived* and *reviewed* — and only the first is addressed here. A focused re-review that
   attacks Proposition A's case analysis and Theorem B's two inequalities is the remaining gate for
   that item.
2. **It does not promote the node** or recommend a level. The wave-19 review's licence is to the
   dispatcher, not to me.
3. **It does not re-add the Island V clause.** §2.2 is a candidate. Re-adding it changes the claim
   text and therefore the claim hash.
4. **It does not touch the open items**: the abstract `(S1)+(S2)+(S3)` question (roll-up row 1),
   Island V's general case (row 2, `task-004`), Definition 2.2's multiset→set passage (row 5), the
   imported `K₄` data and the unrecomputed census families (row 6), the unreviewed NO side of
   Theorem V.5, or A9. Rows 3, 4, 7 and 8 are the ones this file moves.
5. **It does not remove the shared-model caveat** (§1.7, last paragraph). My simulator implements the
   same (M3) fault set as the dossier; a systematic error in the *model* survives this verification
   exactly as it survives every other one in the campaign.
6. **It reads [Cou90], [ALS91] and [CE12] not at all.** §3 and §6 consume the wave-18 verification as
   data. What I contribute there is the division of labour, the bridge registration and the
   provenance hygiene — not a second primary reading.

**Roll-up delta.** Against Amendment 4 §2.1's eight rows: row 3 (C1 primary verification) →
discharged with the residues of §6 recorded; row 4 (Lemma 1.4 bridge) → **derived** here, review
outstanding; row 7 (edit 9) → discharged by §5; row 8 (edit 11) → discharged by §4 with an instance
cited. Rows 1, 2, 5, 6 stand untouched.

---

## 8. Appendix — the verification, in full

### 8.1 The script

Written for this amendment, run once; the digests below are of the exact bytes shown and of the
stdout in §8.2.

```text
sha256(amend5_verify.py) = 284c8b6a68027423d9eda83a61800068fe082cc47bad9b7597a7dd767cdf457b   707 lines
sha256(stdout)           = 94975bff125c0a3dfb259c87bd4016315f34c219cd9437069cf40edaf95a7a0a   153 lines
python 3.9.6 ; wall time 34.6 s ; no third-party dependencies
```

```python
"""Amendment 5 verification. Self-contained, exact over F_2, no dependencies.

The point of this file is that the CIRCUIT side is never computed from Definition 1.3.
It is computed by laying out the CNOT circuit of Model (M) op by op and pushing Pauli
faults through it with the symplectic rules   CNOT(c,t): x_t ^= x_c ,  z_c ^= z_t .
The Definition-1.3 side is computed independently from the combinatorial formula
Cols_X(M) = {e_q} u {chi_{S_i(pi_c)}}.  Parts A-E compare them.

Vectors are python ints used as bitmasks over qubit indices.
"""
import itertools
import random

# ------------------------------------------------------------------ F_2 linear algebra


def rref(vecs):
    basis, pivots = [], []
    for v in vecs:
        for b, p in zip(basis, pivots):
            if (v >> p) & 1:
                v ^= b
        if v:
            p = v.bit_length() - 1
            basis.append(v)
            pivots.append(p)
    return basis, pivots


def in_span(v, basis, pivots):
    for b, p in zip(basis, pivots):
        if (v >> p) & 1:
            v ^= b
    return v == 0


def par(a, b):
    return bin(a & b).count('1') & 1


def syndrome(v, rows):
    s = 0
    for i, r in enumerate(rows):
        if par(r, v):
            s |= 1 << i
    return s


class Code(object):
    def __init__(self, name, n, xchecks, zchecks):
        self.name, self.n = name, n
        self.xchecks = [tuple(sorted(c)) for c in xchecks]
        self.zchecks = [tuple(sorted(c)) for c in zchecks]
        self.HX = [sum(1 << q for q in c) for c in self.xchecks]
        self.HZ = [sum(1 << q for q in c) for c in self.zchecks]
        for a in self.HX:
            for b in self.HZ:
                assert not par(a, b), (name, 'H_X H_Z^T != 0')
        self.SXb, self.SXp = rref(self.HX)
        self.SZb, self.SZp = rref(self.HZ)
        self.k = n - len(self.SXb) - len(self.SZb)
        self.dX = self._dist(self.HZ, self.SXb, self.SXp)
        self.dZ = self._dist(self.HX, self.SZb, self.SZp)
        self.d = min(self.dX, self.dZ)

    def _dist(self, checks, sb, sp):
        for w in range(1, self.n + 1):
            for sup in itertools.combinations(range(self.n), w):
                v = sum(1 << q for q in sup)
                if all(not par(c, v) for c in checks) and not in_span(v, sb, sp):
                    return w
        return float('inf')

    def is_logical_X(self, v):
        return all(not par(c, v) for c in self.HZ) and not in_span(v, self.SXb, self.SXp)

    def is_logical_Z(self, v):
        return all(not par(c, v) for c in self.HX) and not in_span(v, self.SZb, self.SZp)


# ----------------------------------------------- the circuit of Model (M), laid out in time

def build_circuit(code, sched, interleave=None):
    """Qubits 0..n-1 data, then one ancilla per check.  Each check is a contiguous
    block; one CNOT per time step (variant V1: no depth bound), so every data qubit
    not involved in the current CNOT has an IDLE fault location in that step."""
    n = code.n
    keys = ([('X', i) for i in range(len(code.xchecks))]
            + [('Z', i) for i in range(len(code.zchecks))])
    if interleave is None:
        interleave = keys
    anc = dict((kk, n + j) for j, kk in enumerate(keys))
    ops = []
    for kk in interleave:
        sec, ci = kk
        a = anc[kk]
        ops.append(('PREP', a))
        for q in sched[kk]:
            ops.append(('CNOT', a, q) if sec == 'X' else ('CNOT', q, a))
            for qq in range(n):
                if qq != q:
                    ops.append(('IDLE', qq))
        ops.append(('MEAS', a))
    return ops, anc


def propagate(x, z, ops, start):
    for op in ops[start:]:
        if op[0] == 'CNOT':
            c, t = op[1], op[2]
            if (x >> c) & 1:
                x ^= 1 << t
            if (z >> t) & 1:
                z ^= 1 << c
    return x, z


def fault_locations(ops):
    """Every elementary-fault location of (M3), with its local Pauli generators:
    after each preparation (1 qubit), after each CNOT (2 qubits), on each idling
    data qubit (1 qubit); a measurement outcome flip has no data residual at all."""
    locs = []
    for i, op in enumerate(ops):
        if op[0] == 'PREP':
            a = op[1]
            locs.append((('prep', a), i + 1, [(1 << a, 0), (0, 1 << a)]))
        elif op[0] == 'CNOT':
            c, t = op[1], op[2]
            locs.append((('cnot', i), i + 1,
                         [(1 << c, 0), (0, 1 << c), (1 << t, 0), (0, 1 << t)]))
        elif op[0] == 'IDLE':
            q = op[1]
            locs.append((('idle', i, q), i + 1, [(1 << q, 0), (0, 1 << q)]))
        elif op[0] == 'MEAS':
            locs.append((('meas', op[1]), i + 1, []))
    return locs


def residual_group(code, ops, loc):
    """Image of one location's local Pauli group under 'propagate to the end and
    restrict to the data qubits' -- a subgroup of F_2^n x F_2^n."""
    _, at, gens = loc
    mask = (1 << code.n) - 1
    out = set([(0, 0)])
    for (gx, gz) in gens:
        x, z = propagate(gx, gz, ops, at)
        x &= mask
        z &= mask
        out |= set(((u ^ x, v ^ z) for (u, v) in out))
    return sorted(out)


# ------------------------------------------------------------------ the two sides

def circuit_side(code, ops):
    """D(M) := min number of fault LOCATIONS carrying elementary faults whose joint
    terminal residual data Pauli is undetectable and nontrivial.  Capped at 3."""
    locs = fault_locations(ops)
    items, xparts, zparts = [], set(), set()
    for li, loc in enumerate(locs):
        for (vx, vz) in residual_group(code, ops, loc):
            xparts.add(vx)
            zparts.add(vz)
            if (vx, vz) != (0, 0):
                items.append((vx, vz, li))

    def nontrivial(vx, vz):
        if any(par(c, vx) for c in code.HZ) or any(par(c, vz) for c in code.HX):
            return False
        return not (in_span(vx, code.SXb, code.SXp) and in_span(vz, code.SZb, code.SZp))

    for (vx, vz, li) in items:
        if nontrivial(vx, vz):
            return 1, xparts, zparts
    buckets = {}
    for it in items:
        buckets.setdefault((syndrome(it[0], code.HZ), syndrome(it[1], code.HX)), []).append(it)
    for lst in buckets.values():
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i][2] != lst[j][2] and nontrivial(lst[i][0] ^ lst[j][0],
                                                         lst[i][1] ^ lst[j][1]):
                    return 2, xparts, zparts
    return 3, xparts, zparts


def cols_sector(code, sched, sector):
    """Definition 1.3's column set, from the combinatorial formula ONLY."""
    cols = set(1 << q for q in range(code.n))
    checks = code.xchecks if sector == 'X' else code.zchecks
    for ci in range(len(checks)):
        order = sched[(sector, ci)]
        for i in range(1, len(order)):
            cols.add(sum(1 << q for q in order[i:]))
    cols.discard(0)
    return sorted(cols)


def def13_side(code, sched, sector):
    """d_eff^sector(M) by Definition 1.3, capped at 3."""
    cols = cols_sector(code, sched, sector)
    checks = code.HZ if sector == 'X' else code.HX
    sb, sp = (code.SXb, code.SXp) if sector == 'X' else (code.SZb, code.SZp)

    def isL(v):
        return v and all(not par(c, v) for c in checks) and not in_span(v, sb, sp)

    for v in cols:
        if isL(v):
            return 1
    buckets = {}
    for v in cols:
        buckets.setdefault(syndrome(v, checks), []).append(v)
    for lst in buckets.values():
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if isL(lst[i] ^ lst[j]):
                    return 2
    return 3


def random_sched(code, rng):
    s = {}
    for i, c in enumerate(code.xchecks):
        o = list(c)
        rng.shuffle(o)
        s[('X', i)] = tuple(o)
    for i, c in enumerate(code.zchecks):
        o = list(c)
        rng.shuffle(o)
        s[('Z', i)] = tuple(o)
    return s


# ------------------------------------------------------------------ test codes

def steane():
    r = [(3, 4, 5, 6), (1, 2, 5, 6), (0, 2, 4, 6)]
    return Code('Steane [[7,1,3]]', 7, r, r)


def shor():
    return Code('Shor [[9,1,3]]', 9, [(0, 1, 2, 3, 4, 5), (3, 4, 5, 6, 7, 8)],
                [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (7, 8)])


def c422():
    return Code('[[4,2,2]]', 4, [(0, 1, 2, 3)], [(0, 1, 2, 3)])


def rotated913():
    return Code('rotated [[9,1,3]]', 9, [(0, 1), (1, 2, 4, 5), (3, 4, 6, 7), (7, 8)],
                [(0, 1, 3, 4), (2, 5), (3, 6), (4, 5, 7, 8)])


def hgp_rep3():
    H, m, nn = [[1, 1, 0], [0, 1, 1]], 2, 3
    xs, zs = [], []
    for a in range(m):
        for j in range(nn):
            sup = [i * nn + j for i in range(nn) if H[a][i]]
            sup += [nn * nn + a * m + b for b in range(m) if H[b][j]]
            xs.append(tuple(sup))
    for i in range(nn):
        for b in range(m):
            sup = [i * nn + j for j in range(nn) if H[b][j]]
            sup += [nn * nn + a * m + b for a in range(m) if H[a][i]]
            zs.append(tuple(sup))
    return Code('HGP(rep3,rep3) [[13,1,3]]', nn * nn + m * m, xs, zs)


def gneq3():
    return Code('G_neq3 (n=12)', 12,
                [(0, 1, 2, 3), (4, 5, 6, 7), (1, 4, 8, 10), (0, 6, 8, 11), (3, 7, 9, 10)],
                [(1, 2, 4, 7, 9), (0, 1, 6, 7, 10), (0, 1, 2, 3, 8, 9), (0, 1, 4, 5, 11),
                 (0, 2, 4, 6, 8, 11), (4, 5, 6, 7, 10, 11), (8, 9, 10, 11)])


def random_css(rng, n, mx, mz, w):
    for _ in range(3000):
        xs = [tuple(sorted(rng.sample(range(n), w))) for _ in range(mx)]
        HX = [sum(1 << q for q in c) for c in xs]
        cand = []
        for wz in (3, 4):
            for sup in itertools.combinations(range(n), wz):
                v = sum(1 << q for q in sup)
                if all(not par(a, v) for a in HX):
                    cand.append(tuple(sup))
        if len(cand) < mz:
            continue
        c = Code('random n=%d' % n, n, xs, rng.sample(cand, mz))
        if c.k >= 1 and c.d >= 2:
            return c
    return None


# =================================================================== the runs
rng = random.Random(20260823)
CODES = [c422(), steane(), rotated913(), shor(), hgp_rep3(), gneq3()]
j = 0
while len([c for c in CODES if c.name.startswith('rand')]) < 14 and j < 400:
    j += 1
    c = random_css(rng, 7 + (j % 7), 3, 3, 4)
    if c:
        c.name = 'random#%02d n=%d' % (len([x for x in CODES if x.name.startswith('rand')]) + 1, c.n)
        CODES.append(c)

print('=' * 78)
print('PART A -- Proposition A: the single-location residual classification')
print('  claim: X-part of any one elementary fault lies in Cols_X(M) u {0} u {chi_supp(c)}')
print('=' * 78)
badA = totA = 0
stab_outside = stab_tot = 0
for code in CODES:
    for _ in range(3):
        sched = random_sched(code, rng)
        keys = list(sched.keys())
        rng.shuffle(keys)
        ops, anc = build_circuit(code, sched, keys)
        _, xp, zp = circuit_side(code, ops)
        colsX = set(cols_sector(code, sched, 'X'))
        colsZ = set(cols_sector(code, sched, 'Z'))
        predX = colsX | set([0]) | set(code.HX)
        predZ = colsZ | set([0]) | set(code.HZ)
        totA += 2
        if xp != predX:
            badA += 1
            print('   MISMATCH X', code.name, sorted(xp ^ predX))
        if zp != predZ:
            badA += 1
            print('   MISMATCH Z', code.name, sorted(zp ^ predZ))
        # is the printed Lemma-1.4 step "v_X is a sum of at most t elements of
        # Cols_X(M)" literally true?  Only if every chi_supp(c) already lies in Cols_X(M).
        for c in code.HX:
            stab_tot += 1
            if c not in colsX:
                stab_outside += 1
        for c in code.HZ:
            stab_tot += 1
            if c not in colsZ:
                stab_outside += 1
print('codes: %d      (schedule, sector) cases: %d      mismatches: %d' % (len(CODES), totA, badA))
print('check supports chi_supp(c) realised as a one-fault residual : %d' % stab_tot)
print('   ... of which NOT in Cols_X(M)/Cols_Z(M)                  : %d' % stab_outside)
print('   (so the printed Lemma 1.4 step "v_X is a sum of at most t elements of Cols_X(M)"')
print('    is literally false at those locations; the absorption step L + S = L repairs it)')

print()
print('=' * 78)
print('PART B -- the bridge:  D(M) [circuit]   vs   min(d_eff^X, d_eff^Z) [Definition 1.3]')
print('=' * 78)
print('%-26s %3s %3s %3s  %5s %5s %5s   %s' %
      ('code', 'n', 'k', 'd', 'D(M)', 'effX', 'effZ', 'verdict'))
bad = tot = 0
hist = {}
for code in CODES:
    seen = {}
    for _ in range(10):
        sched = random_sched(code, rng)
        keys = list(sched.keys())
        rng.shuffle(keys)
        ops, anc = build_circuit(code, sched, keys)
        D = circuit_side(code, ops)[0]
        ex, ez = def13_side(code, sched, 'X'), def13_side(code, sched, 'Z')
        tot += 1
        ok = (D == min(ex, ez))
        bad += (0 if ok else 1)
        hist[(D, min(ex, ez))] = hist.get((D, min(ex, ez)), 0) + 1
        seen[(D, ex, ez, ok)] = seen.get((D, ex, ez, ok), 0) + 1
    for (D, ex, ez, ok), cnt in sorted(seen.items()):
        print('%-26s %3d %3d %3d  %5d %5d %5d   %s  (x%d)' %
              (code.name, code.n, code.k, code.d, D, ex, ez,
               'AGREE' if ok else 'DISAGREE', cnt))
print('-' * 78)
print('(code, schedule, interleaving) triples tested : %d' % tot)
print('joint value D(M) beat both sectors            : %d'
      % sum(v for (a, b), v in hist.items() if a < b))
print('joint value D(M) exceeded the sector minimum  : %d'
      % sum(v for (a, b), v in hist.items() if a > b))
print('DISAGREEMENTS                                 : %d' % bad)

print()
print('=' * 78)
print('PART C -- the capped value 3 is a true value: explicit 3-location witness')
print('=' * 78)
for code in CODES[:6]:
    sched = random_sched(code, rng)
    ops, anc = build_circuit(code, sched)
    locs = fault_locations(ops)
    got = None
    for w in range(1, code.n + 1):
        for sup in itertools.combinations(range(code.n), w):
            v = sum(1 << q for q in sup)
            sec = 'X' if code.is_logical_X(v) else ('Z' if code.is_logical_Z(v) else None)
            if sec is None:
                continue
            tx = tz = 0
            used = set()
            for q in sup:
                for li, loc in enumerate(locs):
                    if loc[0][0] == 'idle' and loc[0][2] == q and li not in used:
                        grp = residual_group(code, ops, loc)
                        want = (1 << q, 0) if sec == 'X' else (0, 1 << q)
                        assert want in grp
                        tx ^= want[0]
                        tz ^= want[1]
                        used.add(li)
                        break
            ok = (all(not par(c, tx) for c in code.HZ) and all(not par(c, tz) for c in code.HX)
                  and not (in_span(tx, code.SXb, code.SXp) and in_span(tz, code.SZb, code.SZp)))
            got = (w, sec, len(used), ok)
            break
        if got:
            break
    print('%-26s d(Q)=%d : %d idle faults on a min-weight %s-logical -> undetectable nontrivial: %s'
          % (code.name, code.d, got[2], got[1], got[3]))

print()
print('=' * 78)
print('PART D -- Lemma 1.2: D(M) does not move with the interleaving of the blocks')
print('=' * 78)
bd = td = 0
for code in CODES:
    for _ in range(2):
        sched = random_sched(code, rng)
        keys = list(sched.keys())
        vals = set()
        for _ in range(4):
            p = keys[:]
            rng.shuffle(p)
            ops, anc = build_circuit(code, sched, p)
            vals.add(circuit_side(code, ops)[0])
        td += 1
        if len(vals) != 1:
            bd += 1
            print('   INTERLEAVING-DEPENDENT', code.name, vals)
print('(code, schedule) pairs over 4 interleavings each : %d      D(M) moved: %d' % (td, bd))

print()
print('=' * 78)
print('PART E -- the (<=) half constructively: every column of Cols_X(M) is realised')
print('  by a PURE-X-type elementary fault at a location of its own (injective map)')
print('=' * 78)
tot = bad = ncols = 0
for code in CODES:
    for _ in range(3):
        sched = random_sched(code, rng)
        keys = list(sched.keys())
        rng.shuffle(keys)
        ops, anc = build_circuit(code, sched, keys)
        locs = fault_locations(ops)
        mask = (1 << code.n) - 1
        for sector in ('X', 'Z'):
            checks = code.xchecks if sector == 'X' else code.zchecks
            used, okall, cnt = set(), True, 0
            for ci in range(len(checks)):
                order = sched[(sector, ci)]
                a = anc[(sector, ci)]
                cn = [oi for oi, op in enumerate(ops)
                      if op[0] == 'CNOT' and a in (op[1], op[2])]
                for i in range(1, len(order)):
                    col = sum(1 << q for q in order[i:])
                    oi = cn[i - 1]
                    gx, gz = ((1 << a, 0) if sector == 'X' else (0, 1 << a))
                    x, z = propagate(gx, gz, ops, oi + 1)
                    want = (col, 0) if sector == 'X' else (0, col)
                    if (x & mask, z & mask) != want or oi in used:
                        okall = False
                    used.add(oi)
                    cnt += 1
            for q in range(code.n):
                hit = False
                for loc in locs:
                    if loc[0][0] == 'idle' and loc[0][2] == q and (loc[1] - 1) not in used:
                        gx, gz = ((1 << q, 0) if sector == 'X' else (0, 1 << q))
                        x, z = propagate(gx, gz, ops, loc[1])
                        if (x & mask, z & mask) == ((1 << q, 0) if sector == 'X' else (0, 1 << q)):
                            used.add(loc[1] - 1)
                            hit = True
                            cnt += 1
                            break
                if not hit:
                    okall = False
            tot += 1
            ncols += cnt
            if not okall:
                bad += 1
                print('   FAIL', code.name, sector)
print('(code, schedule, sector) cases: %d    columns placed at distinct locations: %d    failures: %d'
      % (tot, ncols, bad))

print()
print('=' * 78)
print('PART F -- Steane [[7,1,3]]: exhaustive over ALL schedules, both sectors')
print('=' * 78)
S = steane()
print('n=%d k=%d d_X=%d d_Z=%d d(Q)=%d   X-check weights %s'
      % (S.n, S.k, S.dX, S.dZ, S.d, [len(c) for c in S.xchecks]))
print('conditions the DELETED clause named (k <= 1 ; X-weight <= 4) : %s'
      % (S.k <= 1 and max(len(c) for c in S.xchecks) <= 4))
print('ambient promise (d(Q) = 3 exactly ; k >= 1)                  : %s' % (S.d == 3 and S.k >= 1))
print('section 6.1 promise (adds d_X >= 4)                          : %s' % (S.dX >= 4))
res = {}
for sector in ('X', 'Z'):
    checks = S.xchecks if sector == 'X' else S.zchecks
    other, ochecks = (('Z', S.zchecks) if sector == 'X' else ('X', S.xchecks))
    mx = cnt = 0
    for combo in itertools.product(*[list(itertools.permutations(c)) for c in checks]):
        sched = dict(((sector, i), o) for i, o in enumerate(combo))
        for i, c in enumerate(ochecks):
            sched[(other, i)] = tuple(c)
        mx = max(mx, def13_side(S, sched, sector))
        cnt += 1
    res[sector] = (mx, cnt)
    print('  sector %s : %d schedules enumerated, max d_eff^%s over all of them = %d'
          % (sector, cnt, sector, mx))
yes = res['X'][0] >= 3 and res['Z'][0] >= 3
print('  => Eff-Preserve(Steane, d = 3) = %s' % ('YES' if yes else 'NO'))
print('  corrected clause requires d_X >= 4; Steane has d_X = %d  =>  EXCLUDED: %s'
      % (S.dX, S.dX < 4))

print()
print('=' * 78)
print('PART G -- G_neq3 and its k = 1 augmentations against section 6.1 VERBATIM')
print('=' * 78)
G = gneq3()
print('G_neq3 : n=%d k=%d d_X=%d d_Z=%d d(Q)=%d  X-check weights %s'
      % (G.n, G.k, G.dX, G.dZ, G.d, [len(c) for c in G.xchecks]))
print('section 6.1 verbatim (d(Q)=3, k>=1, X-weight<=4, d_X>=4) : %s'
      % (G.d == 3 and G.k >= 1 and max(len(c) for c in G.xchecks) <= 4 and G.dX >= 4))
w3 = [s for s in itertools.combinations(range(G.n), 3) if G.is_logical_Z(sum(1 << q for q in s))]
print('weight-3 Z-logicals : %d  ->  %s' % (len(w3), w3))
ok = 0
for sup in w3:
    A = Code('aug', G.n, G.xchecks, list(G.zchecks) + [sup])
    good = (A.k == 1 and A.d == 3 and max(len(c) for c in A.xchecks) <= 4 and A.dX >= 4)
    ok += 1 if good else 0
    print('   + Z-check %-12s k=%d d_X=%d d_Z=%d d=%d   6.1 verbatim: %s'
          % (str(sup), A.k, A.dX, A.dZ, A.d, good))
print('augmentations with k = 1 meeting 6.1 verbatim : %d / %d' % (ok, len(w3)))

print()
print('=' * 78)
print("PART H -- Theorem V.4's construction on the cited instance; d_eff^X measured")
print('=' * 78)
A = Code('G_neq3 + Z-check (0,2,11)', G.n, G.xchecks, list(G.zchecks) + [(0, 2, 11)])
print('%s : n=%d k=%d d_X=%d d_Z=%d d(Q)=%d' % (A.name, A.n, A.k, A.dX, A.dZ, A.d))
free = [i for i in range(A.n) if i not in set(A.SXp)]


def red(v):
    for b, p in zip(A.SXb, A.SXp):
        if (v >> p) & 1:
            v ^= b
    return v


def coords(v):
    r = red(v)
    return tuple((r >> i) & 1 for i in free)


ell = None
for w in range(1, A.n + 1):
    for sup in itertools.combinations(range(A.n), w):
        v = sum(1 << q for q in sup)
        if A.is_logical_X(v):
            ell = red(v)
            break
    if ell is not None:
        break
p = [i for i, b in enumerate(coords(ell)) if b][0]
print('dim Log = k = %d ; a representative ell of weight %d ; splitting coordinate %d'
      % (A.k, bin(ell).count('1'), p))
sched = {}
for ci, c in enumerate(A.xchecks):
    q1, rest = c[0], [q for q in c if q != c[0]]
    betas = [coords((1 << q1) | (1 << q))[p] for q in rest]
    pick = [q for q, b in zip(rest, betas) if b == 0]
    assert pick, 'V.4 parity argument FAILED on %s' % (c,)
    half = (q1, pick[0])
    sched[('X', ci)] = half + tuple(q for q in c if q not in half)
    print('   check %-14s beta of the three 2|2 splits = %s  ->  order %s'
          % (str(c), betas, str(sched[('X', ci)])))
for ci, c in enumerate(A.zchecks):
    sched[('Z', ci)] = tuple(c)
print("d_eff^X of Theorem V.4's schedule, measured from Definition 1.3 : %d   (V.4 asserts >= 3)"
      % def13_side(A, sched, 'X'))
r2 = random.Random(7)
bz, found, t = 0, None, 0
while bz < 3 and t < 200000:
    t += 1
    s2 = dict(sched)
    for ci, c in enumerate(A.zchecks):
        o = list(c)
        r2.shuffle(o)
        s2[('Z', ci)] = tuple(o)
    v = def13_side(A, s2, 'Z')
    if v > bz:
        bz, found = v, dict(s2)
print('Z-sector random search : best d_eff^Z = %d after %d draws' % (bz, t))
if bz >= 3:
    ops, anc = build_circuit(A, found)
    print('full-circuit D(M) on (V.4 X-schedule, searched Z-schedule) = %d ; sector min = %d'
          % (circuit_side(A, ops)[0], min(def13_side(A, found, 'X'), def13_side(A, found, 'Z'))))
    print('=> Eff-Preserve(cited instance, d = 3) = YES')


# ================================================= PART I (HGP proviso census)



def kerdist(rows, ncols):
    """min weight of a nonzero v with <row,v> = 0 for every row; inf if none."""
    for w in range(1, ncols + 1):
        for sup in itertools.combinations(range(ncols), w):
            v = sum(1 << q for q in sup)
            if all(bin(r & v).count('1') % 2 == 0 for r in rows):
                return w
    return float('inf')


def rowmasks(H):
    return [sum(1 << j for j, b in enumerate(r) if b) for r in H]


def transpose(H):
    return [[H[i][j] for i in range(len(H))] for j in range(len(H[0]))]


def hgp(H1, H2):
    m1, n1 = len(H1), len(H1[0])
    m2, n2 = len(H2), len(H2[0])
    # qubits: A = (j,b) in [n1]x[n2] -> j*n2+b ; B = (i,a) in [m1]x[m2] -> n1*n2 + i*m2 + a
    nA = n1 * n2
    N = nA + m1 * m2
    xs = []
    for i in range(m1):
        for b in range(n2):
            sup = [j * n2 + b for j in range(n1) if H1[i][j]]
            sup += [nA + i * m2 + a for a in range(m2) if H2[a][b]]
            if sup:
                xs.append(tuple(sorted(sup)))
    zs = []
    for j in range(n1):
        for a in range(m2):
            sup = [j * n2 + b for b in range(n2) if H2[a][b]]
            sup += [nA + i * m2 + a for i in range(m1) if H1[i][j]]
            if sup:
                zs.append(tuple(sorted(sup)))
    return N, xs, zs

rng = random.Random(11235)
tot = kok = hypfail = concfail = 0
examples = []
trials = 0
while tot < 400 and trials < 40000:
    trials += 1
    m1 = rng.randint(1, 3)
    n1 = rng.randint(2, 4)
    m2 = rng.randint(1, 3)
    n2 = rng.randint(2, 4)
    H1 = [[rng.randint(0, 1) for _ in range(n1)] for _ in range(m1)]
    H2 = [[rng.randint(0, 1) for _ in range(n2)] for _ in range(m2)]
    N, xs, zs = hgp(H1, H2)
    if N == 0 or N > 16 or not xs or not zs:
        continue
    try:
        C = Code('hgp', N, xs, zs)
    except AssertionError:
        continue
    if C.k < 1:
        continue
    tot += 1
    muX = min(kerdist(rowmasks(H2), n2), kerdist(rowmasks(transpose(H1)), m1))
    muZ = min(kerdist(rowmasks(H1), n1), kerdist(rowmasks(transpose(H2)), m2))
    mu = min(muX, muZ)
    if C.d == mu:
        kok += 1
        continue
    hypfail += 1
    # conclusion side: is there STILL a schedule with d_eff(M) = d(Q)?  and does EVERY
    # schedule have d_eff(M) = d(Q)?   (d(Q) is small here, so cap-3 arithmetic suffices)
    if C.d > 3:
        continue
    worst = 99
    for _ in range(200):
        s = random_sched(C, rng)
        v = min(def13_side(C, s, 'X'), def13_side(C, s, 'Z'))
        worst = min(worst, min(v, C.d))
    if worst < C.d:
        concfail += 1
        examples.append((N, C.k, C.d, muX, muZ, worst))

print('=' * 78)
print('PART I -- HGP proviso census: hypothesis-failure is not conclusion-failure')
print('=' * 78)
print('random HGP instances with k >= 1 sampled     : %d' % tot)
print('  Theorem II.4 hypothesis d(Q) = min(mu) HOLDS : %d' % kok)
print('  Theorem II.4 hypothesis FAILS                : %d   (this is what a "46/1971"-style' % hypfail)
print('                                                 census counts)')
print('  of those, an instance where some schedule drops d_eff below d(Q)')
print('  (i.e. the CONCLUSION fails)                  : %d' % concfail)
if examples:
    print('  examples:', examples[:5])
print('  (200 random schedules per hypothesis-failing instance, both sectors,')
print('   d_eff computed from Definition 1.3 and capped at 3)')
```

### 8.2 Its stdout, pasted unedited

```text
==============================================================================
PART A -- Proposition A: the single-location residual classification
  claim: X-part of any one elementary fault lies in Cols_X(M) u {0} u {chi_supp(c)}
==============================================================================
codes: 20      (schedule, sector) cases: 120      mismatches: 0
check supports chi_supp(c) realised as a one-fault residual : 396
   ... of which NOT in Cols_X(M)/Cols_Z(M)                  : 396
   (so the printed Lemma 1.4 step "v_X is a sum of at most t elements of Cols_X(M)"
    is literally false at those locations; the absorption step L + S = L repairs it)

==============================================================================
PART B -- the bridge:  D(M) [circuit]   vs   min(d_eff^X, d_eff^Z) [Definition 1.3]
==============================================================================
code                         n   k   d   D(M)  effX  effZ   verdict
[[4,2,2]]                    4   2   2      1     1     1   AGREE  (x10)
Steane [[7,1,3]]             7   1   3      2     2     2   AGREE  (x10)
rotated [[9,1,3]]            9   1   3      2     2     2   AGREE  (x2)
rotated [[9,1,3]]            9   1   3      2     2     3   AGREE  (x2)
rotated [[9,1,3]]            9   1   3      2     3     2   AGREE  (x5)
rotated [[9,1,3]]            9   1   3      3     3     3   AGREE  (x1)
Shor [[9,1,3]]               9   1   3      1     1     3   AGREE  (x1)
Shor [[9,1,3]]               9   1   3      2     2     3   AGREE  (x7)
Shor [[9,1,3]]               9   1   3      3     3     3   AGREE  (x2)
HGP(rep3,rep3) [[13,1,3]]   13   1   3      3     3     3   AGREE  (x10)
G_neq3 (n=12)               12   2   3      1     3     1   AGREE  (x2)
G_neq3 (n=12)               12   2   3      2     2     2   AGREE  (x3)
G_neq3 (n=12)               12   2   3      2     3     2   AGREE  (x5)
random#01 n=8                8   2   2      1     1     1   AGREE  (x1)
random#01 n=8                8   2   2      1     1     2   AGREE  (x5)
random#01 n=8                8   2   2      1     2     1   AGREE  (x3)
random#01 n=8                8   2   2      2     2     2   AGREE  (x1)
random#02 n=9                9   3   2      1     1     1   AGREE  (x3)
random#02 n=9                9   3   2      1     1     2   AGREE  (x4)
random#02 n=9                9   3   2      1     2     1   AGREE  (x3)
random#03 n=7                7   1   2      1     1     2   AGREE  (x2)
random#03 n=7                7   1   2      2     2     2   AGREE  (x5)
random#03 n=7                7   1   2      2     2     3   AGREE  (x3)
random#04 n=8                8   2   2      1     1     1   AGREE  (x1)
random#04 n=8                8   2   2      1     1     2   AGREE  (x2)
random#04 n=8                8   2   2      1     2     1   AGREE  (x1)
random#04 n=8                8   2   2      2     2     2   AGREE  (x6)
random#05 n=9                9   3   2      1     1     1   AGREE  (x2)
random#05 n=9                9   3   2      1     1     2   AGREE  (x2)
random#05 n=9                9   3   2      1     2     1   AGREE  (x4)
random#05 n=9                9   3   2      2     2     2   AGREE  (x2)
random#06 n=10              10   4   2      1     1     1   AGREE  (x6)
random#06 n=10              10   4   2      1     2     1   AGREE  (x2)
random#06 n=10              10   4   2      2     2     2   AGREE  (x2)
random#07 n=7                7   1   2      1     1     1   AGREE  (x1)
random#07 n=7                7   1   2      1     1     2   AGREE  (x3)
random#07 n=7                7   1   2      1     2     1   AGREE  (x2)
random#07 n=7                7   1   2      2     2     2   AGREE  (x4)
random#08 n=8                8   2   2      1     1     2   AGREE  (x3)
random#08 n=8                8   2   2      2     2     2   AGREE  (x7)
random#09 n=9                9   3   2      1     1     1   AGREE  (x1)
random#09 n=9                9   3   2      1     1     2   AGREE  (x3)
random#09 n=9                9   3   2      1     2     1   AGREE  (x1)
random#09 n=9                9   3   2      2     2     2   AGREE  (x5)
random#10 n=10              10   4   2      1     1     1   AGREE  (x7)
random#10 n=10              10   4   2      1     2     1   AGREE  (x2)
random#10 n=10              10   4   2      2     2     2   AGREE  (x1)
random#11 n=7                7   1   2      1     1     2   AGREE  (x1)
random#11 n=7                7   1   2      2     2     2   AGREE  (x9)
random#12 n=8                8   2   2      1     1     2   AGREE  (x4)
random#12 n=8                8   2   2      2     2     2   AGREE  (x6)
random#13 n=9                9   3   2      1     1     1   AGREE  (x2)
random#13 n=9                9   3   2      1     1     2   AGREE  (x2)
random#13 n=9                9   3   2      1     2     1   AGREE  (x3)
random#13 n=9                9   3   2      2     2     2   AGREE  (x3)
random#14 n=10              10   4   2      1     1     1   AGREE  (x4)
random#14 n=10              10   4   2      1     1     2   AGREE  (x1)
random#14 n=10              10   4   2      1     2     1   AGREE  (x4)
random#14 n=10              10   4   2      2     2     2   AGREE  (x1)
------------------------------------------------------------------------------
(code, schedule, interleaving) triples tested : 200
joint value D(M) beat both sectors            : 0
joint value D(M) exceeded the sector minimum  : 0
DISAGREEMENTS                                 : 0

==============================================================================
PART C -- the capped value 3 is a true value: explicit 3-location witness
==============================================================================
[[4,2,2]]                  d(Q)=2 : 2 idle faults on a min-weight X-logical -> undetectable nontrivial: True
Steane [[7,1,3]]           d(Q)=3 : 3 idle faults on a min-weight X-logical -> undetectable nontrivial: True
rotated [[9,1,3]]          d(Q)=3 : 3 idle faults on a min-weight Z-logical -> undetectable nontrivial: True
Shor [[9,1,3]]             d(Q)=3 : 3 idle faults on a min-weight X-logical -> undetectable nontrivial: True
HGP(rep3,rep3) [[13,1,3]]  d(Q)=3 : 3 idle faults on a min-weight X-logical -> undetectable nontrivial: True
G_neq3 (n=12)              d(Q)=3 : 3 idle faults on a min-weight Z-logical -> undetectable nontrivial: True

==============================================================================
PART D -- Lemma 1.2: D(M) does not move with the interleaving of the blocks
==============================================================================
(code, schedule) pairs over 4 interleavings each : 40      D(M) moved: 0

==============================================================================
PART E -- the (<=) half constructively: every column of Cols_X(M) is realised
  by a PURE-X-type elementary fault at a location of its own (injective map)
==============================================================================
(code, schedule, sector) cases: 120    columns placed at distinct locations: 2148    failures: 0

==============================================================================
PART F -- Steane [[7,1,3]]: exhaustive over ALL schedules, both sectors
==============================================================================
n=7 k=1 d_X=3 d_Z=3 d(Q)=3   X-check weights [4, 4, 4]
conditions the DELETED clause named (k <= 1 ; X-weight <= 4) : True
ambient promise (d(Q) = 3 exactly ; k >= 1)                  : True
section 6.1 promise (adds d_X >= 4)                          : False
  sector X : 13824 schedules enumerated, max d_eff^X over all of them = 2
  sector Z : 13824 schedules enumerated, max d_eff^Z over all of them = 2
  => Eff-Preserve(Steane, d = 3) = NO
  corrected clause requires d_X >= 4; Steane has d_X = 3  =>  EXCLUDED: True

==============================================================================
PART G -- G_neq3 and its k = 1 augmentations against section 6.1 VERBATIM
==============================================================================
G_neq3 : n=12 k=2 d_X=4 d_Z=3 d(Q)=3  X-check weights [4, 4, 4, 4, 4]
section 6.1 verbatim (d(Q)=3, k>=1, X-weight<=4, d_X>=4) : True
weight-3 Z-logicals : 8  ->  [(0, 1, 8), (0, 2, 11), (1, 3, 10), (2, 3, 9), (4, 6, 8), (4, 7, 10), (5, 6, 11), (5, 7, 9)]
   + Z-check (0, 1, 8)    k=1 d_X=4 d_Z=3 d=3   6.1 verbatim: True
   + Z-check (0, 2, 11)   k=1 d_X=4 d_Z=3 d=3   6.1 verbatim: True
   + Z-check (1, 3, 10)   k=1 d_X=4 d_Z=3 d=3   6.1 verbatim: True
   + Z-check (2, 3, 9)    k=1 d_X=4 d_Z=3 d=3   6.1 verbatim: True
   + Z-check (4, 6, 8)    k=1 d_X=4 d_Z=3 d=3   6.1 verbatim: True
   + Z-check (4, 7, 10)   k=1 d_X=4 d_Z=3 d=3   6.1 verbatim: True
   + Z-check (5, 6, 11)   k=1 d_X=4 d_Z=3 d=3   6.1 verbatim: True
   + Z-check (5, 7, 9)    k=1 d_X=4 d_Z=3 d=3   6.1 verbatim: True
augmentations with k = 1 meeting 6.1 verbatim : 8 / 8

==============================================================================
PART H -- Theorem V.4's construction on the cited instance; d_eff^X measured
==============================================================================
G_neq3 + Z-check (0,2,11) : n=12 k=1 d_X=4 d_Z=3 d(Q)=3
dim Log = k = 1 ; a representative ell of weight 4 ; splitting coordinate 0
   check (0, 1, 2, 3)   beta of the three 2|2 splits = [1, 1, 0]  ->  order (0, 3, 1, 2)
   check (4, 5, 6, 7)   beta of the three 2|2 splits = [0, 0, 0]  ->  order (4, 5, 6, 7)
   check (1, 4, 8, 10)  beta of the three 2|2 splits = [0, 0, 0]  ->  order (1, 4, 8, 10)
   check (0, 6, 8, 11)  beta of the three 2|2 splits = [1, 1, 0]  ->  order (0, 11, 6, 8)
   check (3, 7, 9, 10)  beta of the three 2|2 splits = [1, 0, 1]  ->  order (3, 9, 7, 10)
d_eff^X of Theorem V.4's schedule, measured from Definition 1.3 : 3   (V.4 asserts >= 3)
Z-sector random search : best d_eff^Z = 3 after 94 draws
full-circuit D(M) on (V.4 X-schedule, searched Z-schedule) = 3 ; sector min = 3
=> Eff-Preserve(cited instance, d = 3) = YES
==============================================================================
PART I -- HGP proviso census: hypothesis-failure is not conclusion-failure
==============================================================================
random HGP instances with k >= 1 sampled     : 400
  Theorem II.4 hypothesis d(Q) = min(mu) HOLDS : 387
  Theorem II.4 hypothesis FAILS                : 13   (this is what a "46/1971"-style
                                                 census counts)
  of those, an instance where some schedule drops d_eff below d(Q)
  (i.e. the CONCLUSION fails)                  : 0
  (200 random schedules per hypothesis-failing instance, both sectors,
   d_eff computed from Definition 1.3 and capped at 3)
```

### 8.3 The content-hash-chain extractor, and its output

The §0.1 table is re-derivable from this file alone. The extractor takes the amendment's own path.

```python
"""Content hash chain of Amendment 5's replacement blocks.

For each repair Rn, the block is the bytes of this file STRICTLY BETWEEN the line
'<!-- Rn: BEGIN -->' and the line '<!-- Rn: END -->' (marker lines excluded, the
newline that ends the BEGIN marker line excluded, the newline that ends the last
content line included).  Run it on the amendment itself.
"""
import hashlib
import sys

path = sys.argv[1] if len(sys.argv) > 1 else \
    'artifacts/circdist_cplx_islands_amendment5_20260823.md'
raw = open(path, 'rb').read()
print('file      :', path)
print('sha256    :', hashlib.sha256(raw).hexdigest())
print('bytes     :', len(raw), ' lines:', raw.count(b'\n'))
print()
for n in ('R1', 'R2', 'R3', 'R4', 'R5', 'R6'):
    b = ('<!-- %s: BEGIN -->\n' % n).encode()
    e = ('<!-- %s: END -->' % n).encode()
    i = raw.find(b)
    j = raw.find(e)
    if i < 0 or j < 0:
        print('%s  MARKER MISSING' % n)
        continue
    block = raw[i + len(b):j]
    print('%s  sha256 %s   %6d B  %4d lines'
          % (n, hashlib.sha256(block).hexdigest(), len(block), block.count(b'\n')))
```

Run against this file, the six block lines are:

```text
R1  sha256 1d1343b0132d42b352471421bcbb8adbe4fa9a1cb5f07b46db2f3ca4d9afbb77     1778 B    26 lines
R2  sha256 1d4933bda72105fbd0fbab6b86cc77b1327ab91e8ae4991e98e815af52c913bf     4983 B    65 lines
R3  sha256 b454c072050e2d5c668801971705fabc2b3b037f7c1adc0b0eb81c8ee7b88353     8415 B    96 lines
R4  sha256 61a2318f05ba486db5823a2e9ca87edfc1f210ce5f3f53439cc81bd643bbafda     2220 B    15 lines
R5  sha256 15250a46616618740bbd9a26a19329dff49dd4762b1da160f7d8076088cb05b8     2138 B    25 lines
R6  sha256 f7dcbee36bf9f0d3eeafaa636434d4a8e92f1db07dfb65f48ebdaa8007061ddd     1981 B    23 lines
```

The extractor's first three lines — the whole-file digest and its byte and line counts — are
**deliberately not reproduced here**: pasting them into this file changes them, so they are
self-referentially unstable, whereas the six block digests are invariant under any edit outside the
marker pairs (verified: they are unchanged across the two edits made to this file after the blocks
were written). A reviewer wanting the whole-file digest computes it directly with `shasum -a 256`.

---

## 9. Surprises worth the lead's attention

1. **Lemma 1.4's printed argument is not merely unproved; one of its steps is false as written.**
   "`v_X` is a sum of at most `t` elements of `Cols_X(M)`" fails at every X-check preparation and at
   every X-check's first CNOT, because Lemma 1.1 explicitly puts `χ_{supp(c)}` *outside* `Cols_X(M)`
   ("which is a stabiliser and hence contributes nothing") while it *is* the residual of a single
   elementary fault. Measured: **396 of 396** check supports occur as one-fault residuals and **396
   of 396** lie outside the corresponding column set. The repair is one line (`L_X + S_X = L_X`), and
   the conclusion is unaffected — but "contributes nothing" was doing unchecked work in the one
   lemma that carries every island, and five reviews read past it because they read it as a scope
   caveat rather than as a proof.
2. **The load-bearing fact about the sector split is one the write-up never states.** The split works
   because **no single fault location contributes a hook in both sectors** — an X-check CNOT's
   Z-side residual is always a bare data column `e_{q_i}`, never a Z-hook. The printed argument
   gestures at cross-sector coupling ("*e.g. a `Y ⊗ Y` CNOT fault*") without noticing that this is
   exactly the structure that makes the coupling harmless. Proposition A(second clause) is, to my
   reading, new to the dossier.
3. **The bridge is provable without the promise, and it is an equality with the *physical* count.**
   I expected to deliver a specialisation per island (the task's stop-loss branch). In fact `D(M) =
   min(d_eff^X, d_eff^Z)` holds for every CSS code and every schedule with no hypothesis at all, so
   no island needs a weaker form. The residual is definitional, not mathematical, and is bounded to
   readings of "extended code" that refuse to count fault locations.
4. **The un-witnessed §6.1 promise was witnessed by an object the dossier had built for another
   purpose.** `G_{≠3}` was constructed in the gadget document to realise the `≠₃` template; nobody
   checked it against §6.1's promise, and the ≈10⁶-draw absence search that made row 8 look
   frightening was sampling a distribution in which `d_X ≥ 4` with `d_Z = 3` is rare. Both the wave-19
   reviewer and I found the witness in minutes once we looked at the dossier's own codes instead of
   at random ones. **This is the second time in this campaign that an "absence" result was refuted by
   an object already in the repository** (Steane was the first).
5. **`[Cou90]` contains both halves the write-up outsourced.** The linear-time algorithmic form
   (Prop (4.14)(1)) attributed to `[ALS91]` and the edge-set quantification (Def (3.2), set
   variables of sort `e`) attributed to `[CE12]` are both in the 1990 paper. The citations were all
   real; the story about who supplies what was invented. That is a failure mode worth naming: a
   *plausible* division of labour reads as more scholarly than a correct one.
6. **The three-way count came out 2–1 the other way, too.** The verification that was supposed to
   confirm three citations ended up demoting one to corroborating, correcting one locator to a
   result of the opposite polarity, and *upgrading* the third beyond what the write-up claimed for
   it. None of the three attributions survived unchanged.
