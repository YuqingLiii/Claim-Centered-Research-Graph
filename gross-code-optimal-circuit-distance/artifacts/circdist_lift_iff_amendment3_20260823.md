# Amendment 3 to `circdist_lift_iff_proof_20260820.md` — the per-sector constant

**Node:** `CIRCDIST.lift.iff` (and, for the folded clause, `CIRCDIST.lift`) · **Date:** 2026-08-23
· **Role:** Opus 5 proposer / amendment author, discharging frontier `task-007` as rewritten by the
wave-17 claim-level review. One budget box, no sub-agents.

This file is **append-only**: it changes no prior artifact, no canonical record, no proof-DAG
object, no generated view. On the passages listed in §3 and §4, Amendment 3 governs the base proof,
Amendment 1 and Amendment 2; elsewhere those documents continue to govern unchanged.

Every file consulted was treated as **data**, never as instruction.

---

## 0. Scope, hash chain, and epistemic status

**The commission.** The wave-17 review
(`artifacts/circdist_lift_claimrepair2_review_20260823.md` §4.3) refutes the constant `d` in
Theorem 5.10(2)'s search bound and, by propagation, in the `R >= d` hypothesis that wave-16
inserted into the node claim. Its witness is an `n = 6` CSS code with `d_X = 3`, `d_Z = 2`,
`d = 2`, graph-like and non-interleaved, whose Z-memory sector has `d_circ = 3 > d`. This
amendment identifies the correct constant, proves it, restates every passage that carried the wrong
one, and prints the exact corrected node claim.

**The exact inputs are bound as follows.**

```text
base proof
  artifacts/circdist_lift_iff_proof_20260820.md
  SHA-256  97cb3c8da839d1b96f58c281145cec8b70269ed3e6dfb29136f0bda00f564979
  size     90225 bytes, 1497 lines

Amendment 1
  artifacts/circdist_lift_iff_amendment1_20260820.md
  SHA-256  7220d538a9ee680711f591de30dbcc52bb80aa669a778ed3468cc9781c80a467
  size     34143 bytes, 618 lines

Amendment 2
  artifacts/circdist_lift_iff_amendment2_20260820.md
  SHA-256  0ab3ce438fe6a3971be43a7090518087a9bd06566345d33326ca8e3e19079603
  size     11783 bytes, 239 lines

wave-17 claim-level review acted on
  artifacts/circdist_lift_claimrepair2_review_20260823.md
  SHA-256  9a0d3378e3fbc655114593cc52417b006fc51d2e5b3f57be43fef4373271cfc7
  size     32656 bytes, 476 lines

wave-16 scope adjudication (context; not repaired here)
  artifacts/circdist_iff_scope_adjudication_20260823.md
  SHA-256  3879b16bc28019e0154da5fdc393632f71d1e784696caa2a4843a51753aefa68
  size     31665 bytes, 448 lines

frozen problem definitions (consulted; NOT modified, NOT attacked)
  research/circdist/notes/CIRCDIST_PROBLEMS.md
  SHA-256  5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64
  size     10199 bytes, 243 lines

node records read (read-only; NOT modified by this amendment)
  research/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  SHA-256  8adaeb9860619adaf65c49d3f237a021483fd24c04616e5b1131b0cd14af2e9a
  research/circdist/proof-dag/nodes/CIRCDIST.lift.yaml
  SHA-256  fa13e311d42098d4e817f047a571828550fe721be3e58010d2cf9a4e1ca8d88b

claim-hash pipeline, revalidated before use
  sha256( yaml.safe_load(node)["claim"].replace("\r\n","\n").strip().encode("utf-8") )
  CIRCDIST.lift.iff  ->  2c8fe9e3a670367c1c321149d76ae33f0df05fefe101c74c6b0f76406ace8926  (439 chars)
  CIRCDIST.lift      ->  bd1aa84ed25a14c4f0c731d7a8359b1ed14dce6f385223beadabb2f8d7b03b4c  (703 chars)
```

Both recomputed claim digests reproduce the wave-17 review's §3.1 and §3.2 values exactly, so the
pipeline is validated and neither claim has drifted since that review bound it.

If any bound hash fails to reproduce, this amendment is void until it is re-derived against the
changed input.

**Epistemic ceiling.** As in the base document, every mathematical statement here is labelled
**CONJECTURED** with an explicit *derivation status* line, and every computation is labelled
**NUMERICAL** with the code inline (§6). The derivations of §2 are complete at proposer level and
have **not** been independently reviewed. This amendment assigns no level to anything and licenses
no promotion.

---

## 1. Repair index

| item | target | action |
|---|---|---|
| **M1** | new | **Lemma A**, the per-sector spatial ceiling `d_circ(sector) <= d_sector`, proved from the model. This is the statement the whole-circuit fact `d_circ <= d` was wrongly transposed into. |
| **M2** | 5.9's trailing chain; 5.10(1)/(1′)/(1″); 5.10(2) | restate with the per-sector constant; add the whole-circuit readings, which are **true with `d`** and which explain how the error survived |
| **M3** | 5.6 preamble, 5.7 | replace `R >= d` by `R >= d_sec`, closing the unargued band `d <= R < d_circ` |
| **M4** | §0, §4.3, §7.2, §8, §10, §7.1 table | the same constant, propagated |
| **M5** | node claim `CIRCDIST.lift.iff` (and the folded clause of `CIRCDIST.lift`) | the exact corrected claim string, printed with its digest (§5). **A claim edit is a dispatcher act; this amendment proposes, it does not apply.** |

---

## 2. The correct constant, and its proof

### 2.1 Two spatial distances, and which sector each one bounds

The base document's Definition 1.1 fixes a CSS code `Q = [[n,k,d]]` by its X-checks `𝒜` and
Z-checks `ℬ`, and Definition 1.5 fixes the two memory sectors. It never names the two one-sided
spatial distances separately, and that omission is the whole defect. Name them.

> **Definition A.0 (per-sector spatial distances).** Write `H_X` for the `𝒜`-incidence matrix and
> `H_Z` for the `ℬ`-incidence matrix over `F₂`. Put
>
> ```
>    d_X  :=  min { |v| : v ∈ F₂^n , H_Z v = 0 , v ∉ rowspace(H_X) }      (X-type logicals)
>    d_Z  :=  min { |w| : w ∈ F₂^n , H_X w = 0 , w ∉ rowspace(H_Z) }      (Z-type logicals)
> ```
>
> so that `d = min(d_X, d_Z)` is the code distance of Definition 1.1. For a memory sector `S` put
>
> ```
>    d_sec(S)  :=  d_X   if  S = Z-memory  ,        d_sec(S)  :=  d_Z   if  S = X-memory .
> ```
>
> **The pairing is the crossed one**, and it is forced by Definition 1.5 together with 1.9: the
> Z-memory initialises in `|0⟩^n`, reads out in the Z basis, and carries the observables
> `λ^{(j)} = ⊕_{q ∈ supp(Z_L^{(j)})}`; by CONJECTURED 1.9 its `d_circ` is attained in the
> **X-sector**, i.e. the faults are `X` Paulis and Z-check outcome flips. So the object that
> corrupts a Z-memory is an *X-type* logical, and the spatial distance that governs it is `d_X`.
> The X-memory is the mirror image under `𝒜 ↔ ℬ`, `X ↔ Z`, control ↔ target, and is governed by
> `d_Z`.

Throughout §2, as throughout base §5, statements are for the **Z-memory sector**; the X-memory
statements are the mirror images, obtained by the substitution above, and §6.3 verifies them
computationally by running the same code on the mirrored instance.

### 2.2 Lemma A — the per-sector ceiling

> **CONJECTURED Lemma A (per-sector spatial ceiling).** Let `M` be any legal single-ancilla CSS
> schedule (measurement-consistent or not; graph-like or not) and let `C_R(M)` be the Z-memory
> experiment of Definition 1.5 with `R >= 1` rounds and the 公共定义's ideal boundaries. Then
>
> ```
>    d_circ( C_R(M) )   ≤   d_X                                                       (A)
> ```
>
> and, in the mirror, `d_circ` of the X-memory experiment is `≤ d_Z`. Consequently the
> min-over-sectors quantity of Definition 1.5 satisfies `d_circ(C(M)) ≤ min(d_X, d_Z) = d`, which is
> exactly the 公共定义's inequality `d_eff(M) <= d_circ(C(M)) <= d` — **and neither sector inherits
> the other sector's bound.**
>
> *Derivation.* Let `E*` be a minimum-weight X-type logical, `|E*| = d_X`, so `H_Z E* = 0` and
> `E* ∉ rowspace(H_X)`.
>
> *(i) `E*` flips an observable.* `ker H_Z` decomposes as `rowspace(H_X) ⊕ span{X_L^{(1)},…,X_L^{(k)}}`
> with the standard symplectic pairing `|X_L^{(i)} ∩ supp(Z_L^{(j)})| ≡ δ_{ij}`, and every element
> of `rowspace(H_X)` has even overlap with every `Z_L^{(j)}` (that is (CSS) applied to
> `Z_L^{(j)} ∈ ker H_X`). Writing `E* = Σ_i c_i X_L^{(i)} + σ` with `σ ∈ rowspace(H_X)` gives
> `λ^{(j)}(E*) = c_j`, and `E* ∉ rowspace(H_X)` forces some `c_j = 1`. So `λ(E*) ≠ 0`.
>
> *(ii) A weight-1 fault with residual `{q}` and voltage `0` exists in every round, for every `q`.*
> Fix a round and let `g` be the **last** gate of that round involving the data qubit `q`.
> - If `g = (a → q)`, `q` is the target; the elementary two-qubit fault `I ⊗ X` immediately after
>   `g` (Definition 1.8) leaves `X` on `q` and nothing else.
> - If `g = (q → b)`, `q` is the control; the elementary two-qubit fault `X ⊗ I` immediately after
>   `g` leaves `X` on `q`. The CNOT has already acted, so `anc(b)` is untouched.
> - If `q` lies in no gate of the round, it is idle at every step, and a single-qubit `X` on `q`
>   (Definition 1.8, "on any qubit at any step at which it is not in a gate") does it.
>
> In all three cases the fault is elementary, of weight 1, of the X-sector, has residual
> `E = {q}`, and by 1.13.1 has `u_b = [q ∈ supp(b)]·[t(q→b) > t] = 0` for every `b`, because no gate
> `q → b` of that round follows the insertion point. Note this argument uses **only** the existence
> of a last gate; it needs neither (MC) nor non-interleaving, and it is the schedule-independent
> version of the "bare data errors" step of 5.11's *Case Z-block first*.
>
> *(iii) The construction.* In round `R−1` place one such fault for each `q ∈ E*`; call the set
> `F*`, so `|F*| = |E*| = d_X` and the locations are pairwise distinct (distinct qubits). By (∂) of
> CONJECTURED 1.11 each contributes `[u]_{R−1} + [u+s]_R = [s({q})]_R`, since `u = 0`; summing,
>
> ```
>    ∂F*  =  [ Σ_{q ∈ E*} s({q}) ]_R  =  [ H_Z E* ]_R  =  0 .
> ```
>
> `F*` triggers no Z-check detector. It triggers no X-check detector either: it is an X-sector fault
> set, and by 1.9 the X-check detectors are functions of the Z-parts alone. And
> `λ(F*) = λ(E*) ≠ 0` by (i). So `F*` is an undetectable logical fault set of `C_R(M)` of weight
> `d_X`, giving `d_circ(C_R(M)) ≤ d_X`. ∎
>
> *Derivation status: complete.* Model inputs used: Definition 1.8's fault menu (specifically that
> `I⊗X` and `X⊗I` are available immediately after every CNOT), Definition 1.5's ideal terminal
> readout (so that the accumulated residual is what the observable sees, and `D_{b,R}` exists —
> Lemma 4.1), 1.9, 1.11, 1.13.1. **(V) is not used**, nor is 5.3, 5.4, 5.9 or graph-likeness.

> **Remark A.1 (exactly where the transposition fails).** The 公共定义 writes
> `d_eff(M) <= d_circ(C(M)) <= d` for the **circuit** `C(M)`, and Definition 1.5 defines
> `d_circ(C)` as the **min over the two memory sectors**. The chain of Lemma A shows why `d`
> appears there: `d = min(d_X,d_Z)` is exactly the min of the two per-sector ceilings. A single
> sector only ever sees *its own* ceiling. The whole of base §5 is per-sector ("All statements below
> are for the Z-memory"), so importing `d_circ ≤ d` into §5 imports the min of two numbers into a
> statement about one of them. It is sound precisely when `d_X = d_Z` — which is why every instance
> in the campaign's record (`[[4,2,2]]`, Steane, rotated surface, gross `[[144,12,12]]`) hid it, and
> why the wave-17 review's asymmetric witness was needed to expose it.

> **Remark A.2 (the ceiling is one-sided).** `d_circ(sector) ≤ d_sec` is a ceiling, never a value:
> `d_eff(M) ≤ d_circ ≤ d_sec` and both inequalities are routinely strict (§6.2 has instances with
> `d_X = 3`, `d_circ = 2`, and instances with `d_eff = 2 < d_circ = 3 = d_X`). What Lemma A supplies
> is an *a-priori, code-only, circuit-free* upper bound — which is what every window and
> saturation statement in §5 actually needs, and it is all they need.

### 2.3 The corrected saturation and window statements

> **CONJECTURED Lemma B (per-sector saturation; replaces the constant in 5.10(1)).** Fix a memory
> sector and write `d_R := d_circ(C_R(M))` for that sector, `d_∞ := lim_R d_R`. Then `d_R` is
> non-increasing in `R`, and
>
> ```
>    d_R  =  d_∞     for every  R ≥ d_∞ ;      and      d_∞  ≤  d_sec ,
> ```
>
> so in particular `d_R` is **constant for all `R ≥ d_sec`**, with limiting value `d_∞ = d_{R = d_sec}`.
>
> *Derivation.* Monotonicity: more rounds give strictly more fault locations and the boundaries are
> unchanged, so `d_{R+1} ≤ d_R`; hence the limit exists and `d_R ≥ d_∞` for every `R`. Ceiling:
> Lemma A gives `d_R ≤ d_sec` for every `R`, hence `d_∞ ≤ d_sec`. Constancy: let `R' > R ≥ d_∞` and
> let `F` be a minimum-weight undetectable logical of `C_{R'}(M)`, `|F| = d_{R'}`. By 5.9 its
> occupied rounds form a contiguous interval of span `≤ |F| = d_{R'} ≤ d_∞ ≤ R`; by Lemma 4.1 the
> detector index set is the full interval at both ends and the bulk is time-translation invariant,
> so `F` may be translated to start at round `0` and lands inside `C_R(M)`, whence `d_R ≤ d_{R'}`.
> With monotonicity, `d_R = d_{R'}`. ∎ *Derivation status: complete.* This is the base derivation of
> 5.10(1) with `d` replaced by `d_∞` where the argument actually uses the *weight* of the witness,
> and with Lemma A supplying the a-priori ceiling that makes the conclusion checkable.

> **CONJECTURED Lemma B′ (whole-circuit saturation — `d` is the right constant here).** Let
> `d_R(C) := d_circ(C_R(M)) = min` of the two sectors, per Definition 1.5, and `d_∞(C)` its limit.
> Then `d_R(C)` is non-increasing, `d_R(C) ≤ d` for every `R`, and
>
> ```
>    d_R(C)  =  d_∞(C)      for every  R ≥ d ,
> ```
>
> i.e. base 5.10(1)'s "constant for all `R ≥ d`" is **TRUE as written when `d_R` is read
> whole-circuit**.
>
> *Derivation.* `d_R(C) = min(d_R^{Z-mem}, d_R^{X-mem})` is a min of two non-increasing sequences,
> hence non-increasing, and `≤ d` by Lemma A. Let `S*` be a sector attaining
> `d_∞(C) = d_∞^{S*}`. For `R ≥ d ≥ d_∞(C) = d_∞^{S*}`, Lemma B gives `d_R^{S*} = d_∞^{S*}`, so
> `d_R(C) ≤ d_∞(C)`; monotonicity gives `≥`. ∎ *Derivation status: complete.*

> **CONJECTURED Lemma C (the corrected finite-window decision procedure; replaces 5.10(2)).** Fix a
> memory sector. `d_circ` of that sector is computable from the one-round data
> `{(E(f), s(f), u(f), λ(f)) : f ∈ 𝔽}` alone, by a search over fault multisets of size `≤ d_sec`
> distributed over `≤ d_sec` consecutive rounds. No multi-round circuit is constructed at any point.
> Three equivalent forms of the bound, in increasing order of practicality:
>
> ```
>    (i)   W = d_sec                       — code-only, a-priori, always sufficient ;
>    (ii)  W = any known upper bound on d_circ(sector) ;
>    (iii) run w = 1, 2, 3, … with window w and stop at the first hit — no a-priori bound
>          needed, terminates at w = d_circ(sector) .
> ```
>
> *Derivation.* **Soundness** (unchanged from the base derivation, and independently confirmed by
> the wave-17 review §4.2): any `F ⊆ 𝔽 × {0,…,K−1}` satisfying (LIFT') with `λ(F) ≠ 0` is a genuine
> undetectable logical of `C_R(M)` for `R ≥ K`, because (LIFT') ⟺ `∂F = 0` is 4.3 and the finite-`R`
> detector set is the full interval by 4.1. **Completeness**: a minimum-weight undetectable logical
> `F` has `|F| = d_circ ≤ d_sec` by Lemma A and round-span `≤ |F| ≤ d_sec` by 5.9, and translates to
> start at round `0` by 4.1; so it lies inside the window. Form (ii) is the same argument with
> `d_sec` replaced by `W`. Form (iii) needs no ceiling at all: the search at window `w` finds a
> witness iff `d_circ ≤ w` — "only if" is soundness, "if" is 5.9 plus translation — so the first
> hit occurs at `w = d_circ`. ∎ *Derivation status: complete.*
>
> **Whole-circuit corollary.** Running form (i) in *both* sectors with the common window `W = d` and
> taking the minimum returns `d_circ(C(M))` correctly: the sector attaining the min has a witness of
> weight `d_∞(C) ≤ d` and span `≤ d`, and the other sector can only return `None` or a value
> `≥ d_∞(C)`. So base 5.10(2) is also **true as written under the whole-circuit reading**; what is
> false is the per-sector reading, which is the reading base §5 declares and which the node claim
> uses.

### 2.4 The corrected `R`-hypothesis, and the band that is now closed

> **CONJECTURED 5.6′ / 5.7′ (the `R`-hypothesis).** In Theorem 5.6's preamble and in Theorem 5.7,
> `R ≥ d` must read `R ≥ d_sec`. With that reading both theorems hold as stated.
>
> *Derivation.* 5.6(a) asserts `d_circ(C_R(M)) = min_{γ ∈ L_eff} ℓ(γ)`, whose right-hand side is the
> bi-infinite quantity `d_∞`; the identification of `d_R` with `d_∞` is exactly Lemma B, which needs
> `R ≥ d_∞` and is guaranteed by `R ≥ d_sec`. Parts (b), (c), (d) are statements about `ℓ(γ)` and
> `repair(γ)` in the bi-infinite model and carry no `R` at all. For 5.7: (⟸) the repair-0 certificate
> yields a closed lift of weight `|γ| = d_eff` in the bi-infinite model (5.3), so `d_∞ = d_eff` by
> 5.4(1); Lemma B then transports it to every `R ≥ d_sec`. (⟹) is unchanged and needs no hypothesis
> on `R` beyond the existence of the witness it is handed. ∎ *Derivation status: complete.*

> **What this closes.** The wave-17 review's blocker **B2** is that the band `d ≤ R < d_circ` is
> inside the claim's quantifier and outside its argument. Under `R ≥ d_sec` the band is empty:
> `d_circ(sector) ≤ d_sec` by Lemma A, so `R ≥ d_sec` implies `R ≥ d_circ ≥ d_∞`, and Lemma B
> applies. The blocker **B3** (the claim's bare symbol `d` is undefined and the two readings differ)
> is closed by the same edit, which names the intended quantity in the claim text.

### 2.5 Tightness: the constant cannot be lowered, and the error is unbounded

> **CONJECTURED Proposition D (the chain family).** For `m ≥ 2` let `Q_m` be the `[[2m, 1, 2]]` CSS
> code with X-checks the `m` pairs `P_i = {2i, 2i+1}` and Z-checks the `m−1` consecutive unions
> `P_i ∪ P_{i+1}`. Then
>
> ```
>    d_X(Q_m) = m ,      d_Z(Q_m) = 2 ,      d = 2 ,      k = 1 ,
> ```
>
> and for every **non-interleaved** legal schedule `M` of `Q_m`, the Z-memory sector satisfies
>
> ```
>    d_circ( C_R(M) )  =  d_eff(M)  =  m  =  d_X   for all R ≥ 1 ,    while   d = 2 .
> ```
>
> Hence the ceiling of Lemma A is **attained**, and `d_circ(sector) − d = m − 2` is **unbounded**.
> `m = 3` is the wave-17 review's witness.
>
> *Derivation.* Write `σ_i(v) := |v ∩ P_i| mod 2`. `H_Z v = 0` says `σ_i + σ_{i+1} = 0` for all `i`,
> i.e. all `σ_i` are equal; `rowspace(H_X)` is exactly `{v : v|_{P_i} ∈ {00,11} ∀i} = {v : σ ≡ 0}`.
> So an X-type logical has `σ_i = 1` for every `i`, hence at least one qubit in each of the `m`
> pairs: `d_X = m`, attained by any transversal choice. Dually `ker H_X = {` unions of pairs `}`,
> whose indicator `t ∈ F₂^m` ranges over all of `F₂^m`, while `rowspace(H_Z)` is the even-weight
> subspace of `F₂^m`; so a Z-type logical is an odd union of pairs, minimally one pair:
> `d_Z = 2`. Next, `d_eff`: by 1.13 the realisable non-empty residuals are the singletons `{q}` and
> the suffixes of the X-check CNOT orders, i.e. `{q}` and the full pairs `P_i` (the X-checks have
> weight 2). `Σ_{E ∈ γ} E` must be an X-type logical, so it has `σ_i = 1` for every `i`; a full pair
> contributes `σ ≡ 0` and a singleton contributes `1` to exactly one `σ_i`; therefore `γ` contains at
> least one singleton per pair and `|γ| ≥ m`, with equality realised. So `d_eff = m`. Finally 5.11
> gives `repair ≡ 0` for non-interleaved `M`, hence `d_circ = d_eff = m` at every `R ≥ 1`. ∎
> *Derivation status: complete.* NUMERICAL corroboration at `m = 3, 4, 5` (both non-interleaved
> orders, plus (MC)-passing interleaved schedules at `m = 3`) is in §6.2, by direct multi-round
> simulation that uses none of 5.11, 5.9 or (LIFT').

> **Corollary D.1.** No function of `d` alone is a correct per-sector window constant, and `d_sec`
> cannot be replaced by anything smaller that depends only on the code: `d_sec` is attained on
> `Q_m` for every `m`. Both halves of 5.10(2) fail on `Q_m` for `m ≥ 3` — the *size* bound `≤ d = 2`
> admits no witness at all, and the *window* bound `≤ 2` rounds excludes witnesses of span 3
> (§6.1 exhibits them).

> **Remark D.2 (what is *not* tight).** `R ≥ d_sec` is sufficient, not necessary. The sharp
> sufficient condition is `R ≥ d_∞ = d_circ(sector)`, which is not available a priori; and on the
> chain family the true saturation index is `1`, far below `d_sec = m`. Across the whole §6.2 sweep
> (194 instances) not one instance had `d_R ≠ d_∞` at any `R ≥ 1` — consistent with the wave-17
> review's report that it "did not exhibit a failure of `R >= d`". The band was a **coverage gap in
> the argument, not a counterexample**, and Lemma A + Lemma B close it by argument rather than by
> hoping it is empty.

---

## 3. Exact replacements in the base proof

Each item quotes the original verbatim and gives the exact replacement. Nothing else in the quoted
neighbourhood changes.

*Quoting convention.* Every "Old" string below was checked programmatically to occur **exactly
once** in its source file (base proof, Amendment 1, or Amendment 2), modulo line-wrapping, which is
presentational; §8 records that check.

### R1 — §0, executive summary, item 1 (two clauses)

> **Old:** "A minimum-weight undetectable logical of `C_R(M)` occupies
> a **contiguous** block of rounds and its round-span is at most its weight, hence `≤ d`."

> **New:** "A minimum-weight undetectable logical of `C_R(M)` occupies
> a **contiguous** block of rounds and its round-span is at most its weight, hence `≤ d_sec`, the
> spatial distance of the sector's own logical class (`d_X` for the Z-memory, `d_Z` for the
> X-memory; Definition A.0 and Lemma A of Amendment 3). Under the min-over-sectors reading of
> Definition 1.5 the same chain ends at `≤ d`."

> **Old:** "gives `d_R(M) = d_∞(M)` for all `R ≥ d`, and makes `d_circ` computable from one round."

> **New:** "gives `d_R(M) = d_∞(M)` for all `R ≥ d_sec` per sector (equivalently for all `R ≥ d`
> when `d_R` is read whole-circuit; Amendment 3 Lemmas B and B′), and makes `d_circ` computable
> from one round."

### R2 — §4.3, non-tautology check, item (c)

> **Old:** "(c) the search space for `ℓ` is finite and `d`-bounded (§5.7)."

> **New:** "(c) the search space for `ℓ` is finite and `d_sec`-bounded (§5.7 as amended by
> Amendment 3 Lemma C; the bound may equivalently be taken to be any known upper bound on
> `d_circ`, or dispensed with by searching at increasing window `w = 1,2,3,…`)."

### R3 — §5.4, the preamble of CONJECTURED 5.6

> **Old:** "Fix a legal, measurement-consistent single-ancilla CSS schedule
> `M` and a memory sector. Then for `R` large enough (`R ≥ d` suffices, by §5.7):"

> **New:** "Fix a legal, measurement-consistent single-ancilla CSS schedule
> `M` and a memory sector. Then for `R` large enough (`R ≥ d_sec` suffices, by §5.7 as amended by
> Amendment 3 Lemmas A and B; `d_sec = d_X` for the Z-memory and `d_Z` for the X-memory, and
> `R ≥ d_circ` is the sharp condition):"

### R4 — §5.5, the hypothesis of CONJECTURED 5.7

> **Old:** "**CONJECTURED 5.7 (the criterion).** For every legal, measurement-consistent
> single-ancilla CSS schedule `M`, and `R ≥ d`,"

> **New:** "**CONJECTURED 5.7 (the criterion).** For every legal, measurement-consistent
> single-ancilla CSS schedule `M`, and every `R ≥ d_sec` (Definition A.0: `d_sec = d_X` for the
> Z-memory sector, `d_Z` for the X-memory sector),"

*Note.* The `(⟹)` direction needs no hypothesis on `R` at all; the hypothesis is used only by
`(⟸)`, through Lemma B. Amendment 3 §2.4 records the two directions separately.

### R5 — §5.7, the display of CONJECTURED 5.9

> **Old:**
> ```
>    round-span( F )  ≤  |F|  =  d_circ  ≤  d .
> ```

> **New:**
> ```
>    round-span( F )  ≤  |F|  =  d_circ  ≤  d_sec        (per sector, Amendment 3 Lemma A)
>                                        ≤  d           (only under the min-over-sectors reading)
> ```
> with the first two inequalities being the content of 5.9 itself and the third being Lemma A.

*Scope note that must accompany R5.* Only the trailing `≤ d` is repaired. **Contiguity and
`span ≤ weight` are untouched** and remain confirmed — base review verdict **H**
(203 186 / 203 186), the wave-17 review's independent 27 562 / 27 562, and this amendment's
5 892 / 5 892 (§6.2), on three disjoint code sets and three independently written simulators.

### R6 — §5.7, CONJECTURED 5.10(1) and its derivation

Base 5.10(1) was already retracted-and-replaced by Amendment 1 §3.4 as 5.10(1′) and then by
Amendment 2 §3.1 as 5.10(1″); the live text is 5.10(1″), repaired at R8 below. For the base
sentence itself:

> **Old:** "1. `d_R(M) := d_circ(C_R(M))` is non-increasing in `R` and **constant for all `R ≥ d`**;
> i.e. `R_sat(M) ≤ d` in the sense of `CIRCDIST.sat`, for this model."

> **New:** "1. `d_R(M) := d_circ(C_R(M))` is non-increasing in `R`; per sector it is **constant for
> all `R ≥ d_sec`**, and under the min-over-sectors reading of Definition 1.5 it is **constant for
> all `R ≥ d`** (Amendment 3 Lemmas B and B′). The clause `i.e. R_sat(M) ≤ d` remains withdrawn per
> Amendment 1 §3."

> **Old (derivation of (1)):** "More rounds give more fault locations, so `d_R` is non-increasing; a
> minimum-weight witness of weight `w ≤ d` has span `≤ w ≤ d` by 5.9 and the bulk is
> time-translation invariant with both temporal boundaries fully detectored (4.1), so it can be
> translated into any `C_{R'}` with `R' ≥ w`."

> **New:** "More rounds give more fault locations, so `d_R` is non-increasing; a minimum-weight
> witness of weight `w = d_{R'} ≤ d_sec` (Amendment 3 Lemma A) has span `≤ w ≤ d_sec` by 5.9 and
> the bulk is time-translation invariant with both temporal boundaries fully detectored (4.1), so
> it can be translated into any `C_{R'}` with `R' ≥ w`. The step `w ≤ d` used previously is a
> whole-circuit fact and is **not** available per sector."

### R7 — §5.7, CONJECTURED 5.10(2), and the cross-node note

> **Old:** "2. `d_circ` is computable from the one-round data
> `{(E(f), s(f), u(f), λ(f)) : f ∈ 𝔽}` alone, by a search over fault multisets of size `≤ d`
> distributed over `≤ d` consecutive rounds. No multi-round circuit is constructed at any point."

> **New:** "2. `d_circ` of a fixed memory sector is computable from the one-round data
> `{(E(f), s(f), u(f), λ(f)) : f ∈ 𝔽}` alone, by a search over fault multisets of size `≤ d_sec`
> distributed over `≤ d_sec` consecutive rounds, `d_sec` being that sector's own spatial distance
> (Definition A.0). Any known upper bound `W ≥ d_circ` may replace `d_sec`, and the bound may be
> dispensed with entirely by searching at increasing window `w = 1,2,3,…` and stopping at the first
> hit. Running the search in both sectors with the common window `W = d` and taking the minimum
> computes the min-over-sectors `d_circ(C(M))` correctly. No multi-round circuit is constructed at
> any point. (Amendment 3 Lemma C; the mechanism was independently re-derived and confirmed by
> `artifacts/circdist_lift_claimrepair2_review_20260823.md` §4.2/§4.4, whose verdict was
> CONFIRM-WITH-REQUIRED-REPAIR — this is that repair.)"

> **Old:** "5.10(1) is a `CIRCDIST.sat` result obtained for free here, with `B(r,d) = d`, but only
> inside this model"

> **New:** "5.10(1) is a `CIRCDIST.sat` result obtained for free here, with `B(r,d) = d_sec` per
> sector and `B(r,d) = d` for the min-over-sectors circuit distance, but only inside this model"

### R8 — Amendment 2 §3.1, CONJECTURED 5.10(1″)

> **Old:** "`d_R(M)` is non-increasing in `R` and constant for all `R >= d`, with
> `d_infty(M) = d_{R=d}(M)`. Moreover,
> ```text
> R_sat(M) = 1          if d_infty(M) = d,
> R_sat(M) = infinity   if d_infty(M) < d.
> ```
> In either case the dichotomy is decided by inspecting `R = 1,...,d`, and the finite-window bound
> remains `B(r,d) = d`."

> **New:** "**CONJECTURED 5.10(1‴).** `d_R(M)` is non-increasing in `R`. **Per sector** it is
> constant for all `R >= d_sec` with `d_infty = d_{R = d_sec}` and the finite-window bound is
> `B(r,d) = d_sec`. **Whole-circuit** — i.e. with `d_R(M) := d_circ(C_R(M))` the min over the two
> sectors, which is the reading the frozen `R_sat` definition uses — it is constant for all
> `R >= d`, with `d_infty(M) = d_{R=d}(M)` and `B(r,d) = d`, and
> ```text
> R_sat(M) = 1          if d_infty(M) = d,
> R_sat(M) = infinity   if d_infty(M) < d,
> ```
> the dichotomy being decided by inspecting `R = 1,...,d`."

> **Old (Reason for the sharpening):** "The 公共定义 gives `d_R(M) <= d` for every `R`, while 5.10
> gives that `d_R` is non-increasing."

> **New:** "The 公共定义's `d_R(M) <= d` is a **whole-circuit** statement — `d_circ(C)` is the min
> over the two memory sectors (Definition 1.5) — and Amendment 3 Lemma A proves it from the model,
> as `min(d_X, d_Z) = d`. Read whole-circuit, the ceiling and the monotonicity are exactly what the
> dichotomy below needs, and the L2 argument goes through unchanged. Read **per sector** the ceiling
> is `d_sec` and not `d`, and the per-sector clauses above are stated accordingly."

**L2 verdict.** Amendment 2's L2 dichotomy `R_sat ∈ {1, ∞}` **survives intact**, because `R_sat` is
defined in the 公共定义 against the whole-circuit `d_R(M)` and against the code distance `d`, and
both of the facts it consumes — `d_R(M) ≤ d` and monotonicity — are whole-circuit facts, now proved
(Lemma A, Lemma B′). The wave-17 review's §4.3 propagation note flagged L2 as *possibly* infected;
this amendment finds it is not, and supplies the missing justification rather than a repair.

### R9 — Amendment 1 §3.4 (5.10(1′)) and §3.6

Amendment 1's 5.10(1′) is superseded by R8's 5.10(1‴); its `≤ d` occurrences inherit the same
per-sector / whole-circuit split. In Amendment 1 §3.6:

> **Old:** "the finite-window fact (`span ≤ weight ≤ d`) is what those use, and it survives intact."

> **New:** "the finite-window fact (`span ≤ weight ≤ d_sec` per sector, `≤ d` whole-circuit) is what
> those use; contiguity and `span ≤ weight` survive intact, and only the trailing constant is
> corrected (Amendment 3 R5)."

> **Old:** "§8 item 2's "`P1.4` (finite window) is **discharged** by 5.9 with `B(r,d) = d`" is
> therefore also unaffected."

> **New:** "§8 item 2's "`P1.4` (finite window) is **discharged** by 5.9" is unaffected; the window
> constant reads `B(r,d) = d_sec` per sector and `B(r,d) = d` whole-circuit."

### R10 — §7.2, two occurrences inside the `repair ≥ 3` gap discussion

> **Old:** "Contiguity (5.9) bounds `r'' − r' ≤ d`, so the search is finite"

> **New:** "Contiguity (5.9) bounds `r'' − r' ≤ d_sec`, so the search is finite"

> **Old:** "Exhibiting (ESC) needs `repair(γ) ≥ 3` with `|γ| + 2 ≤ d`, hence `d ≥ d_eff + 2 ≥ 5` —
> outside every instance examined in this campaign."

> **New:** "Exhibiting (ESC) needs `repair(γ) ≥ 3` with `|γ| + 2 ≤ d_sec`, hence
> `d_sec ≥ d_eff + 2 ≥ 5` — outside every instance examined in this campaign. Note that the
> asymmetric codes of Amendment 3 §2.5 relax this: they reach `d_sec = 5` at `d = 2`, so an (ESC)
> hunt need no longer wait for a `[[n,k,5]]` code."

### R11 — §10, the one-paragraph statement for the node record

> **Old:** "a minimum-weight undetectable logical occupies at most `d` consecutive rounds"

> **New:** "a minimum-weight undetectable logical occupies at most `d_sec` consecutive rounds
> (`d_X` for the Z-memory sector, `d_Z` for the X-memory; at most `d` for the min-over-sectors
> circuit distance)"

### R12 — §7.1, the status table

Insert one row and annotate four, so that the table records where the new hypothesis enters. `𝒜/ℬ`
denotes that the statement needs the code's own check structure and Definition A.0.

| statement | (CSS) | legality | (MC) | ideal boundaries | graph-like | (V) | `d_sec` | derivation |
|---|---|---|---|---|---|---|---|---|
| **A per-sector ceiling `d_circ ≤ d_sec`** | ✓ | ✓ | — | ✓ **terminal readout** | — | — | defines it | **complete (Amd 3 §2.2)** |
| 5.6(c) **Theorem 2**, `repair ≤ 2` | — | — | — | ✓ | — | ✓ | — | **complete** |
| 5.6(a) / 5.7 **the iff** at finite `R` | — | — | — | ✓ | — | ✓ | **✓ (`R ≥ d_sec`)** | **complete (Amd 3 §2.4)** |
| 5.9 contiguity, `span ≤ weight` | — | — | — | ✓ | — | — | — | complete |
| 5.9's trailing `≤ d_sec` | ✓ | ✓ | — | ✓ | — | — | **✓** | complete (Amd 3 §2.2) |
| 5.10(1‴), 5.10(2) window | — | — | — | ✓ | — | — | **✓** | complete (Amd 3 §2.3) |

The row "(MC) is needed for Theorem 1 but **not** for Theorem 2" is unchanged. Lemma A likewise does
not need (MC): it needs only legality (to speak of a last gate) and (CSS) (for the observable
pairing). It does need the **ideal terminal readout**, which is where `H_Z E* = 0` becomes
undetectability rather than a live syndrome — with a non-ideal readout Lemma A fails together with
Lemma 4.1, exactly as §4.1's status line warns.

---

## 4. Dependent-passage list

**Repaired in this amendment (§3):** base §0 item 1 (×2), §4.3(c), §5.4 5.6 preamble, §5.5 5.7
hypothesis, §5.7 5.9 display, §5.7 5.10(1) + derivation, §5.7 5.10(2), §5.7 cross-node note, §7.1
table, §7.2 (×2), §10; Amendment 1 §3.4 and §3.6; Amendment 2 §3.1 (×2).

**Canonical records that carry the constant and are OUT OF SCOPE for a proposer** — listed for the
dispatcher, and **not** modified here (`research/circdist/proof-dag/` is read-only for this role):

1. `nodes/CIRCDIST.lift.iff.yaml`, `claim` — `R >= d`. Corrected string and digest in §5.
2. `nodes/CIRCDIST.lift.iff.yaml`, `assessment.summary` — "the CONTIGUITY THEOREM (min-weight
   undetectable logicals occupy contiguous rounds with span <= weight <= d)" and "together with
   monotonicity and d_R<=d, Amendment 2 gives the exact R_sat dichotomy". The first needs
   `<= d_sec`; the second is correct as written (whole-circuit) and should say so.
3. `nodes/CIRCDIST.lift.iff.yaml`, `assessment.caveats[0]` — the wave-17 BINDING caveat. Its
   refutation stands; its "Repair needs the correct per-sector constant — new mathematics,
   frontier task-007" is discharged by this amendment and should be rewritten to point here.
4. `nodes/CIRCDIST.lift.iff.yaml`, `frontier.task-007` — discharged; see §7 for what remains.
5. `nodes/CIRCDIST.lift.yaml`, `claim` — the folded clause "quantified over memory experiments
   C_R(M) with R >= d rounds". Corrected string and digest in §5.
6. `nodes/CIRCDIST.lift.yaml`, `assessment.caveats` — the wave-17 root caveat 3 ("`R >= d` itself
   is the wrong constant per sector; `R >= d_X` is what is argued"). The parenthetical `d_X` is
   right for the Z-memory and should be generalised to `d_sec`.
7. Any `CIRCDIST.sat` record importing `B(r,d) = d` or `R_sat ≤ d` from 5.10(1). The whole-circuit
   forms are correct (Lemma B′); the per-sector forms need `d_sec`. **This amendment does not
   adjudicate the `sat` family.** One live ambiguity is flagged in §7 item 4.

**Hash consequences.** Editing either claim moves its digest and, by `DAG_PROTOCOL` §5, lapses any
review bound to the old digest — here
`artifacts/circdist_lift_claimrepair2_review_20260823.md` at `sha256:2c8fe9e3…` (iff) and at
`sha256:bd1aa84e…` (root). The route implication of `routes.criterion-corollary-example`
(`sha256:f39c83e6…`) is **not** touched by the §5 edits; it contains no `R` clause.

---

## 5. The corrected claim strings

### 5.1 `CIRCDIST.lift.iff`

The edit is minimal and mechanical: in the current claim, the substring

```text
with R >= d, d_circ equals
```

(unique) is replaced by

```text
with R >= d_sec (the spatial distance of the sector's own logical class: d_X for the Z-memory, d_Z for the X-memory), d_circ equals
```

Nothing else changes — insertion A's placement, insertion B's "at minimum weight", the em dash, and
the terminal period are all preserved byte for byte.

**PROPOSED CLAIM (single line, U+2014 em dash, terminal period, 544 chars):**

> In graph-like detector error models with fixed boundaries, for memory experiments C_R(M) with R >= d_sec (the spatial distance of the sector's own logical class: d_X for the Z-memory, d_Z for the X-memory), d_circ equals the minimum over nontrivial effective logicals gamma of the length of the shortest closed spacetime lift of gamma, with an intrinsic zero-voltage/monodromy condition characterizing same-weight liftability at minimum weight — and the voltage is computable without constructing the full multi-round circuit (non-vacuity bar).

**Digest of the proposed claim:**
`sha256:0c4c466b895d938d2028140967d87974ee2216b3cebcc48967804f530e227240`

This single edit discharges wave-17 blockers **B2** (the unargued band) and **B3** (the undefined
bare `d`). Blocker **B1** — that 5.10(2) carried a required repair on an unrepaired document — is
discharged by §3 R7 landing the repair, per the repository's "repair before promotion" precedent.

*Uniform alternative, if the dispatcher prefers a sector-agnostic quantifier:* `R >= max(d_X, d_Z)`
is sufficient for both sectors simultaneously and needs no sector name; it is weaker (a larger `R`)
and loses the information that each sector saturates at its own constant.

### 5.2 `CIRCDIST.lift` (the folded root clause)

Replacement of the unique substring `memory experiments C_R(M) with R >= d rounds` by
`memory experiments C_R(M) with R >= d_sec rounds, d_sec the sector's own spatial distance (d_X for the Z-memory, d_Z for the X-memory)`:

> In graph-like detector error models with fixed boundaries — graph-like read per-sector (iff Def 1.12) and quantified over memory experiments C_R(M) with R >= d_sec rounds, d_sec the sector's own spatial distance (d_X for the Z-memory, d_Z for the X-memory) — a proven necessary-and-sufficient structural criterion (in graph-covering, voltage-graph, or chain-complex form) characterizes when d_circ = d_eff, of the shape "d_circ equals the minimum over nontrivial effective logicals gamma of the length of the shortest closed spacetime lift of gamma", with zero time-direction voltage/monodromy as the equal-weight liftability condition; the criterion recovers the non-interleaved equality d_circ = d_eff as a corollary and is accompanied by an explicit interleaved example with d_circ > d_eff.

**Digest:** `sha256:9bec82a557e7421efd1faceee31f36ef888511c5b85c687d2fed77a1c1e21ae9`

This is offered for completeness only. The root's own wave-17 blockers **S1** (no minimum-weight
qualifier at the root) and **S2** (the `R` clause scopes over all three conjuncts, weakening two
`PROVED` premises) are **untouched** by this amendment and remain open. Fixing S2 would in any case
move this string again, so the dispatcher may prefer to make both edits at once.

---

## 6. NUMERICAL verification — code and genuine output

**Independence of the computation.** All code below was written this session from the model
definitions (Definitions 1.1–1.8, 1.10, 1.12, 1.13, 1.16 and the 公共定义) and shares no code with
the proposer's §9, with the base review, or with the wave-17 review. The **ground-truth** path is a
direct `F₂`-frame multi-round simulator: it propagates `x` through the CNOTs, resets ancilla frames
each round, records `m_{b,r}`, forms `D_{b,r} = m_{b,r} + m_{b,r−1}` with `m_{b,−1} = 0` and
`m_{b,R}` the ideal readout parity, and reads the observable off the accumulated data error. It
uses **no** (LIFT'), **no** one-round data, and **no** repair/voltage notion. The one-round
5.10(2) procedure (`sec510`) is implemented separately, from `(E,s,u,λ)` plus (LIFT') only, and is
never used as ground truth — only compared against it.

`d_circ` is obtained by a shortest-path search over syndrome states with the deduplicated fault
columns. That is exact: a minimum-weight fault set never contains two faults with equal detector
columns, since deleting such a pair preserves both `∂F = 0` and `λ(F) ≠ 0` and lowers the weight.
By CONJECTURED 1.9 the search may be restricted to X-sector faults for the Z-memory; the X-memory
is handled by running the identical code on the **mirrored** instance (`𝒜 ↔ ℬ`, control ↔ target,
same time steps), whose legality and (MC) are preserved by §2.2 Step 1's `c'_{ab} = c_{ab}`.

Files (this session's scratch): `persector.py` (SHA-256
`6023bbbafbabec9d7dfc39ea9c75a2562a8a52f18220f2ed48d5671919d7d81c`), `run_witness.py`
(`a4274e6dadac7329f62bd77bcdbc0489bb68cfdd0057e91688a6476ad177f584`), `run_sweep.py`
(`4aa6247cf2e48240a3e68c6ad4a0c3237731af5f6969c6ca4145cf9103a7447b`).

### 6.0 The model code (`persector.py`)

```python
#!/usr/bin/env python3
"""
Per-sector circuit-distance ceiling: independent re-derivation and sweep.
Written from the model definitions of artifacts/circdist_lift_iff_proof_20260820.md
(Def 1.1-1.8, 1.12, 1.16) and the frozen CIRCDIST_PROBLEMS.md common definitions.
No use of (LIFT'), of one-round data, or of any repair/voltage notion in the
GROUND-TRUTH path: d_circ is obtained by direct multi-round frame simulation of the
memory experiment.  The one-round 5.10(2) procedure is implemented separately in
sec510(), from (E,s,u,lambda) + (LIFT') only, and is only ever COMPARED to the
ground truth.
Qubit ids: data 0..n-1 ; anc(a_i) = n+i ; anc(b_j) = n+nA+j.
"""
import itertools, random, sys
from collections import defaultdict

pc = lambda x: bin(x).count('1')

# ---------------------------------------------------------------- F2 linear algebra
def rref(rows):
    rows = [r for r in rows if r]
    piv, r = [], 0
    for c in range(64):
        p = None
        for i in range(r, len(rows)):
            if (rows[i] >> c) & 1:
                p = i; break
        if p is None: continue
        rows[r], rows[p] = rows[p], rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i] >> c) & 1): rows[i] ^= rows[r]
        piv.append(c); r += 1
    return rows[:r], piv

def reduce_vec(basis, piv, v):
    for row, c in zip(basis, piv):
        if (v >> c) & 1: v ^= row
    return v

def mask(sup):           # set of ints -> bitmask
    m = 0
    for q in sup: m |= 1 << q
    return m

# ---------------------------------------------------------------- code-level distances
def spatial_distances(n, A, B):
    """A = X-check supports, B = Z-check supports (lists of sets).
       d_X = min wt of v with H_Z v = 0, v not in rowspace(H_X)   (X-type logical)
       d_Z = min wt of w with H_X w = 0, w not in rowspace(H_Z)   (Z-type logical)"""
    HA = [mask(a) for a in A]; HB = [mask(b) for b in B]
    rA, pA = rref(list(HA)); rB, pB = rref(list(HB))
    k = n - len(rA) - len(rB)
    dX = dZ = None
    xlog = []; zlog = []
    for v in range(1, 1 << n):
        if all(pc(v & h) % 2 == 0 for h in HB) and reduce_vec(rA, pA, v) != 0:
            if dX is None or pc(v) < dX: dX = pc(v)
            xlog.append(v)
        if all(pc(v & h) % 2 == 0 for h in HA) and reduce_vec(rB, pB, v) != 0:
            if dZ is None or pc(v) < dZ: dZ = pc(v)
            zlog.append(v)
    ZL = min((v for v in zlog), key=lambda v: (pc(v), v)) if zlog else None
    XL = min((v for v in xlog), key=lambda v: (pc(v), v)) if xlog else None
    return dX, dZ, k, XL, ZL, rA, pA

# ---------------------------------------------------------------- schedules
def greedy(gate_list, busy, start=1):
    tm = {}
    for (c, t) in gate_list:
        s = start
        while c in busy[s] or t in busy[s]: s += 1
        busy[s].add(c); busy[s].add(t); tm[(c, t)] = s
    return tm

def make_schedule(n, A, B, kind, rng=None):
    nA = len(A)
    ancA = lambda i: n + i
    ancB = lambda j: n + nA + j
    gX = [(ancA(i), q) for i in range(len(A)) for q in sorted(A[i])]
    gZ = [(q, ancB(j)) for j in range(len(B)) for q in sorted(B[j])]
    busy = defaultdict(set)
    if kind == 'NI_Zfirst':
        tz = greedy(gZ, busy, 1); s = max(tz.values()) + 1
        tx = greedy(gX, busy, s)
    elif kind == 'NI_Xfirst':
        tx = greedy(gX, busy, 1); s = max(tx.values()) + 1
        tz = greedy(gZ, busy, s)
    elif kind == 'random':
        allg = gX + gZ; rng.shuffle(allg)
        tt = greedy(allg, busy, 1)
        tx = {g: tt[g] for g in gX}; tz = {g: tt[g] for g in gZ}
    gates = {}; gates.update(tx); gates.update(tz)
    return gates, tx, tz

def mc_ok(n, A, B, tx, tz):
    nA = len(A)
    ancA = lambda i: n + i
    ancB = lambda j: n + nA + j
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            c = 0
            for q in a & b:
                if tz[(q, ancB(j))] < tx[(ancA(i), q)]: c += 1
            if c % 2: return False
    return True

# ---------------------------------------------------------------- fault menu (X-sector)
def fault_menu(n, A, B, gates):
    """Elementary X-sector faults of ONE round, as injections '(step t, qubit set S)'
       meaning: the X-frame S is added immediately AFTER time step t (t=0 = after prep).
       Menu per Def 1.8: (i) the X-part of a 2-qubit Pauli immediately after a CNOT;
       (ii) a single-qubit X on a qubit idle at that step; (iii) an X on an ancilla
       immediately after preparation.  Classical outcome flips are handled separately."""
    nA = len(A); nq = n + nA + len(B)
    T = max(gates.values())
    at = defaultdict(list); busy = defaultdict(set)
    for (c, t), s in gates.items():
        at[s].append((c, t)); busy[s].add(c); busy[s].add(t)
    inj = []
    for s in range(1, T + 1):
        for (c, t) in at[s]:
            for S in ({c}, {t}, {c, t}): inj.append((s, frozenset(S), '2q'))
        for v in range(nq):
            if v not in busy[s]: inj.append((s, frozenset({v}), '1q'))
    for g in range(n, nq): inj.append((0, frozenset({g}), 'prep'))
    return inj, T

# ---------------------------------------------------------------- direct simulator
def simulate(n, A, B, gates, T, R, ZLmask, injections, flips):
    """injections: [(r, step, frozenset S)] ; flips: [(r, j)] classical flips of m_{b,r}.
       Returns (detector bitmask over B x {0..R}, observable bit)."""
    nA = len(A); nB = len(B); nq = n + nA + nB
    datamask = (1 << n) - 1
    at = defaultdict(list)
    for (c, t), s in gates.items(): at[s].append((c, t))
    byrt = defaultdict(list)
    for (r, s, S) in injections: byrt[(r, s)].append(S)
    frame = 0
    m = [[0] * nB for _ in range(R + 1)]
    for r in range(R):
        frame &= datamask                       # ancillas re-prepared
        for S in byrt.get((r, 0), []):
            for v in S: frame ^= 1 << v
        for s in range(1, T + 1):
            for (c, t) in at[s]:
                if (frame >> c) & 1: frame ^= 1 << t
            for S in byrt.get((r, s), []):
                for v in S: frame ^= 1 << v
        for j in range(nB): m[r][j] = (frame >> (n + nA + j)) & 1
    for (r, j) in flips: m[r][j] ^= 1
    E = frame & datamask
    for j in range(nB): m[R][j] = pc(E & mask(B[j])) % 2
    det = 0
    for j in range(nB):
        for r in range(R + 1):
            d = m[r][j] ^ (m[r - 1][j] if r > 0 else 0)
            if d: det |= 1 << (j * (R + 1) + r)
    return det, pc(E & ZLmask) % 2

def columns(n, A, B, gates, T, R, ZLmask, inj):
    """one column per (round, elementary fault), deduplicated by (detector, observable)"""
    cols = {}
    for r in range(R):
        for (s, S, kind) in inj:
            d, o = simulate(n, A, B, gates, T, R, ZLmask, [(r, s, S)], [])
            cols.setdefault((d, o), [0, (r, s, S, kind)])[0] += 1
        for j in range(len(B)):
            d, o = simulate(n, A, B, gates, T, R, ZLmask, [], [(r, j)])
            cols.setdefault((d, o), [0, (r, 'flip', j, 'cl')])[0] += 1
    return cols

# ---------------------------------------------------------------- min-weight search
def dcirc_bfs(cols, cap=8):
    """min weight of a subset of columns with XOR of detectors = 0 and obs = 1.
       Minimum-weight solutions never repeat a column vector (a repeated pair cancels
       and lowers the weight), so a shortest-path search over distinct column VECTORS
       is exact."""
    keys = list(cols.keys())
    cur = {(0, 0): 0}
    for w in range(1, cap + 1):
        nxt = {}
        for (d, o), _ in cur.items():
            for (cd, co) in keys:
                st = (d ^ cd, o ^ co)
                if st not in cur and st not in nxt: nxt[st] = w
        if (0, 1) in nxt: return w
        if not nxt: return None
        cur.update(nxt)
    return None

def round_class_columns(n, A, B, gates, T, R, ZLmask, inj):
    """One entry per (round r, one-round fault class); the class is the equivalence class
       of elementary faults with equal (s,u,lambda).  Distinct rounds are kept distinct
       even when their detector columns coincide, so that round-spans are honest."""
    nB = len(B)
    reps = {}
    for (s0, S, kind) in inj:
        d1, o1 = simulate(n, A, B, gates, T, 1, ZLmask, [(0, s0, S)], [])
        reps.setdefault((d1, o1), [0, (s0, S)])[0] += 1
    for j in range(nB):
        d1, o1 = simulate(n, A, B, gates, T, 1, ZLmask, [], [(0, j)])
        reps.setdefault((d1, o1), [0, ('flip', j)])[0] += 1
    out = []
    for (d1, o1), (mult, rep) in reps.items():
        if d1 == 0 and o1 == 0: continue          # the trivial class
        for r in range(R):
            if rep[0] == 'flip':
                d, o = simulate(n, A, B, gates, T, R, ZLmask, [], [(r, rep[1])])
            else:
                d, o = simulate(n, A, B, gates, T, R, ZLmask, [(r, rep[0], rep[1])], [])
            out.append((r, d, o, mult))
    return out

def census_minweight(rcols, w):
    """all weight-w subsets of DISTINCT (round, class) entries with XOR det = 0, obs = 1.
       A minimum-weight fault set never contains two entries with equal columns (they
       cancel), so this enumeration is exhaustive at w = d_circ."""
    out = []
    N = len(rcols)
    def rec(start, chosen, d, o):
        if len(chosen) == w:
            if d == 0 and o == 1: out.append(tuple(chosen))
            return
        if N - start < w - len(chosen): return
        for i in range(start, N):
            r, cd, co, mu = rcols[i]
            chosen.append(i); rec(i + 1, chosen, d ^ cd, o ^ co); chosen.pop()
    rec(0, [], 0, 0)
    return out

# ---------------------------------------------------------------- one-round data + 5.10(2)
def one_round_data(n, A, B, gates, T, ZLmask, inj):
    """(E, s, u, lambda) per Def 1.10, by simulating ONE round only."""
    nA = len(A); nB = len(B); nq = n + nA + nB
    datamask = (1 << n) - 1
    at = defaultdict(list)
    for (c, t), s in gates.items(): at[s].append((c, t))
    data = []
    for (s0, S, kind) in inj:
        frame = 0
        if s0 == 0:
            for v in S: frame ^= 1 << v
        for s in range(1, T + 1):
            for (c, t) in at[s]:
                if (frame >> c) & 1: frame ^= 1 << t
            if s == s0:
                for v in S: frame ^= 1 << v
        E = frame & datamask
        u = 0
        for j in range(nB):
            if (frame >> (n + nA + j)) & 1: u |= 1 << j
        sy = 0
        for j in range(nB):
            if pc(E & mask(B[j])) % 2: sy |= 1 << j
        data.append((E, sy, u, pc(E & ZLmask) % 2, kind))
    for j in range(nB):
        data.append((0, 0, 1 << j, 0, 'cl'))
    return data

def graph_like(data, nB):
    """Def 1.12: |u| + |u+s| <= 2 for every fault."""
    bad = 0
    for (E, s, u, lam, kind) in data:
        if pc(u) + pc(u ^ s) > 2: bad += 1
    return bad, len(data)

def sec510(data, nB, W):
    """Theorem 5.10(2) as a procedure: search over fault multisets of size <= W
       distributed over <= W consecutive rounds, deciding undetectability by (LIFT')
       from one-round data only.  Returns the min size found, or None."""
    cols = {}
    for r in range(W):
        for (E, s, u, lam, kind) in data:
            d = 0
            for j in range(nB):
                if (u >> j) & 1: d |= 1 << (j * (W + 1) + r)
                if ((u ^ s) >> j) & 1: d |= 1 << (j * (W + 1) + r + 1)
            cols[(d, lam)] = cols.get((d, lam), 0) + 1
    return dcirc_bfs(cols, cap=W)

# ---------------------------------------------------------------- mirror (X-memory sector)
def mirror_instance(n, A, B, tx, tz):
    """The X-memory sector of (A,B,M) is the Z-memory sector of the mirrored instance
       (A<->B, control<->target, same time steps).  Legality and (MC) are preserved
       (c'_{ab} = c_{ab} by (CSS), proof doc Sec 2.2 Step 1)."""
    A2, B2 = [set(b) for b in B], [set(a) for a in A]
    nA2 = len(A2)
    ancA2 = lambda i: n + i          # was anc(b_i)
    ancB2 = lambda j: n + nA2 + j    # was anc(a_j)
    tx2, tz2 = {}, {}
    for j, b in enumerate(B):        # old (q -> anc(b_j)) becomes new (anc(a'_j) -> q)
        for q in b: tx2[(ancA2(j), q)] = tz[(q, n + len(A) + j)]
    for i, a in enumerate(A):        # old (anc(a_i) -> q) becomes new (q -> anc(b'_i))
        for q in a: tz2[(q, ancB2(i))] = tx[(n + i, q)]
    gates2 = {}; gates2.update(tx2); gates2.update(tz2)
    return A2, B2, gates2, tx2, tz2

def deff(data, nB, cap=8):
    """d_eff(M) = min |gamma| over L_eff (Def 1.16), from the one-round residual classes."""
    cls = set()
    for (E, s, u, lam, kind) in data:
        if E != 0: cls.add((s, lam))
    cur = {(0, 0): 0}
    for w in range(1, cap + 1):
        nxt = {}
        for (s, l) in cur:
            for (cs, cl) in cls:
                st = (s ^ cs, l ^ cl)
                if st not in cur and st not in nxt: nxt[st] = w
        if (0, 1) in nxt: return w
        if not nxt: return None
        cur.update(nxt)
    return None
```

### 6.1 NUMERICAL A — the wave-17 witness, rebuilt and re-measured (`run_witness.py`)

```python
#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from persector import *

n = 6
A = [{0,1},{2,3},{4,5}]              # X-checks
B = [{0,1,2,3},{2,3,4,5}]            # Z-checks
dX, dZ, k, XL, ZL, rA, pA = spatial_distances(n, A, B)
print("code n=%d  X-checks %s  Z-checks %s" % (n, A, B))
print("k = %d   d_X = %d   d_Z = %d   d = min = %d" % (k, dX, dZ, min(dX,dZ)))
print("min-weight X-logical  :", bin(XL), "wt", pc(XL))
print("min-weight Z-logical Z_L:", bin(ZL), "wt", pc(ZL))

gates, tx, tz = make_schedule(n, A, B, 'NI_Zfirst')
print("schedule NI_Zfirst, (MC) ok:", mc_ok(n,A,B,tx,tz), " depth", max(gates.values()))
inj, T = fault_menu(n, A, B, gates)
data = one_round_data(n, A, B, gates, T, ZL, inj)
bad, tot = graph_like(data, len(B))
print("elementary X-sector faults enumerated (one round): %d ; Def 1.12 violations: %d"
      % (tot, bad))

import random
rng = random.Random(7); R = 4; ok = 0
for trial in range(200):
    fs = [(rng.randrange(R), *inj[rng.randrange(len(inj))][:2]) for _ in range(rng.randint(2,4))]
    fs = [(r, s, S) for (r, s, S) in fs]
    dtot, otot = simulate(n, A, B, gates, T, R, ZL, fs, [])
    dx = 0; ox = 0
    for f in fs:
        d1, o1 = simulate(n, A, B, gates, T, R, ZL, [f], [])
        dx ^= d1; ox ^= o1
    ok += (dtot == dx and otot == ox)
print("simulator F2-linearity self-test: %d/200 agreements" % ok)

print()
for R in (1,2,3,4):
    cols = columns(n, A, B, gates, T, R, ZL, inj)
    print("  R = %d :  distinct fault columns %4d   d_circ(Z-mem) = %s"
          % (R, len(cols), dcirc_bfs(cols, cap=6)))

resid = sorted(set((E, s, lam) for (E,s,u,lam,kind) in data if E != 0))
best = None
from itertools import combinations
for w in range(1, 6):
    found = False
    for combo in combinations(range(len(resid)), w):
        tot_s = 0; tot_l = 0
        for i in combo: tot_s ^= resid[i][1]; tot_l ^= resid[i][2]
        if tot_s == 0 and tot_l == 1:
            found = True; break
    if found: best = w; break
print("  d_eff (min |gamma| over L_eff) = %s   [%d distinct non-empty residual classes]"
      % (best, len(resid)))

print()
for W, lab in ((min(dX,dZ), "W = d   = %d  (5.10(2) as stated)" % min(dX,dZ)),
               (dX,          "W = d_X = %d  (per-sector constant)" % dX)):
    print("  %-38s -> %s" % (lab, sec510(data, len(B), W)))

R = 4
cols = columns(n, A, B, gates, T, R, ZL, inj)
w = dcirc_bfs(cols, cap=6)
rc = round_class_columns(n, A, B, gates, T, R, ZL, inj)
sols = census_minweight(rc, w)
spans = {}; loc_total = 0; contig = 0; spanloc = {}
for s in sols:
    rr = sorted(rc[i][0] for i in s)
    sp = rr[-1] - rr[0] + 1
    spans[sp] = spans.get(sp, 0) + 1
    mult = 1
    for i in s: mult *= rc[i][3]
    loc_total += mult; spanloc[sp] = spanloc.get(sp, 0) + mult
    if set(rr) == set(range(rr[0], rr[-1] + 1)): contig += 1
print("minimum-weight undetectable logicals at R = 4 (weight %d = d_X):" % w)
print("   (round,class)-level solutions : %d   contiguous: %d/%d   location-level: %d"
      % (len(sols), contig, len(sols), loc_total))
print("   round-span histogram (classes)   : %s" % dict(sorted(spans.items())))
print("   round-span histogram (locations) : %s" % dict(sorted(spanloc.items())))
print("   span > weight                    : %d   (5.9 holds)"
      % sum(c for sp, c in spans.items() if sp > w))
print("   span > d = 2, i.e. missed by the stated '<= d rounds' window : %d classes / %d locations"
      % (sum(c for sp, c in spans.items() if sp > 2), sum(c for sp, c in spanloc.items() if sp > 2)))

print()
Estar = XL
last = {}
for (c,t), s in gates.items():
    for v in (c,t):
        if v < n: last[v] = max(last.get(v,0), s)
faults = [(R-1, last[q], frozenset({q})) for q in range(n) if (Estar>>q)&1]
d_, o_ = simulate(n, A, B, gates, T, R, ZL, faults, [])
print("Lemma A construction: %d faults, one per qubit of the min-weight X-logical," % len(faults))
print("   each injected immediately after that qubit's LAST gate of round R-1:")
print("   detectors triggered = %d   observable flipped = %d" % (pc(d_), o_))
```

**Genuine output:**

```text
code n=6  X-checks [{0, 1}, {2, 3}, {4, 5}]  Z-checks [{0, 1, 2, 3}, {2, 3, 4, 5}]
k = 1   d_X = 3   d_Z = 2   d = min = 2
min-weight X-logical  : 0b10101 wt 3
min-weight Z-logical Z_L: 0b11 wt 2
schedule NI_Zfirst, (MC) ok: True  depth 6
elementary X-sector faults enumerated (one round): 87 ; Def 1.12 violations: 0
simulator F2-linearity self-test: 200/200 agreements

  R = 1 :  distinct fault columns   10   d_circ(Z-mem) = 3
  R = 2 :  distinct fault columns   16   d_circ(Z-mem) = 3
  R = 3 :  distinct fault columns   22   d_circ(Z-mem) = 3
  R = 4 :  distinct fault columns   28   d_circ(Z-mem) = 3
  d_eff (min |gamma| over L_eff) = 3   [9 distinct non-empty residual classes]

  W = d   = 2  (5.10(2) as stated)       -> None
  W = d_X = 3  (per-sector constant)     -> 3
minimum-weight undetectable logicals at R = 4 (weight 3 = d_X):
   (round,class)-level solutions : 38   contiguous: 38/38   location-level: 14556
   round-span histogram (classes)   : {1: 12, 2: 24, 3: 2}
   round-span histogram (locations) : {1: 5112, 2: 8352, 3: 1092}
   span > weight                    : 0   (5.9 holds)
   span > d = 2, i.e. missed by the stated '<= d rounds' window : 2 classes / 1092 locations

Lemma A construction: 3 faults, one per qubit of the min-weight X-logical,
   each injected immediately after that qubit's LAST gate of round R-1:
   detectors triggered = 0   observable flipped = 1
```

**Reading.** The witness reproduces on independently written code: `d_X = 3`, `d_Z = 2`, `d = 2`,
graph-like (0 / 87 violations of Definition 1.12), `d_circ(Z-mem) = 3 > d` at every `R = 1,…,4`,
5.10(2) at `W = d = 2` returns **nothing** while at `W = d_X = 3` it returns **3**, which is the
ground truth. Lemma A's explicit construction is verified directly: three weight-1 faults, one per
qubit of the minimum-weight X-logical, each placed after that qubit's last gate of the final round,
trigger **zero** detectors and flip the observable. Both halves of 5.10(2)'s stated bound fail here:
the size bound (`3 > 2`) and the window bound (2 of 38 solution classes, 1 092 of 14 556
locations, have span 3 > 2).

*Two accounting differences from the wave-17 review, both benign.* My one-round fault menu has 87
elementary faults where the review reports 91, and my location-level census gives 14 556 where the
review reports 27 562 — these are location-counting conventions (which idle slots and which
two-qubit Paulis are counted as distinct locations), not disagreements about the mathematics.
Everything structural agrees exactly: all witnesses contiguous, maximum span 3, span-3 witnesses
present, `d_circ = 3`.

### 6.2 NUMERICAL B — the sweep (`run_sweep.py`)

```python
#!/usr/bin/env python3
"""Sweep: per-sector ceiling d_circ(sector) <= d_sector on asymmetric (d_X != d_Z) CSS codes."""
import sys, os, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from persector import *

def chain(m):
    n = 2*m
    A = [{2*i, 2*i+1} for i in range(m)]
    B = [{2*i, 2*i+1, 2*i+2, 2*i+3} for i in range(m-1)]
    return n, A, B

def cyclic_chain(m):
    n = 2*m
    A = [{2*i, 2*i+1} for i in range(m)]
    B = [{2*i, 2*i+1, (2*i+2) % n, (2*i+3) % n} for i in range(m)]
    return n, A, B

def random_codes(rng, want, nmax=8):
    out = []; seen = set(); tries = 0
    while len(out) < want and tries < 200000:
        tries += 1
        n = rng.randint(5, nmax); rX = rng.randint(1, 3); A = []
        for _ in range(rX):
            w = rng.randint(2, min(4, n)); A.append(set(rng.sample(range(n), w)))
        HA = [mask(a) for a in A]; rA, pA = rref(list(HA))
        if len(rA) != rX: continue
        dual = [v for v in range(1, 1 << n) if all(pc(v & h) % 2 == 0 for h in HA)]
        if not dual: continue
        need = n - len(rA) - 1                      # want k = 1
        if need < 1: continue
        B = []
        for _ in range(min(need + rng.randint(0, 1), 4)):
            v = rng.choice(dual); B.append({q for q in range(n) if (v >> q) & 1})
        HB = [mask(b) for b in B]
        if len(rref(list(HB))[0]) != need: continue
        if any(len(b) < 2 or len(b) > 6 for b in B): continue
        dX, dZ, k, XL, ZL, _, _ = spatial_distances(n, A, B)
        if k != 1 or dX is None or dZ is None: continue
        if dX == dZ: continue
        if min(dX, dZ) < 2: continue
        if max(dX, dZ) > 5: continue
        key = (n, tuple(sorted(tuple(sorted(a)) for a in A)),
                  tuple(sorted(tuple(sorted(b)) for b in B)))
        if key in seen: continue
        seen.add(key); out.append(("rand%02d" % len(out), n, A, B))
    return out

def run_sector(tag, n, A, B, gates, tx, tz, Rmax, do_census=True):
    dX, dZ, k, XL, ZL, _, _ = spatial_distances(n, A, B)
    d = min(dX, dZ)
    inj, T = fault_menu(n, A, B, gates)
    data = one_round_data(n, A, B, gates, T, ZL, inj)
    bad, tot = graph_like(data, len(B))
    dR = []
    for R in range(1, Rmax + 1):
        cols = columns(n, A, B, gates, T, R, ZL, inj)
        dR.append(dcirc_bfs(cols, cap=dX + 1))
    dc = dR[-1]
    span_max = None; contig_ok = True; nsol = 0; nspan_gt_d = 0
    if do_census and dc is not None and dc <= 4:
        rc = round_class_columns(n, A, B, gates, T, Rmax, ZL, inj)
        sols = census_minweight(rc, dc); nsol = len(sols)
        for s in sols:
            rr = sorted(rc[i][0] for i in s); sp = rr[-1] - rr[0] + 1
            span_max = sp if span_max is None else max(span_max, sp)
            if set(rr) != set(range(rr[0], rr[-1] + 1)): contig_ok = False
            if sp > d: nspan_gt_d += 1
    de = deff(data, len(B), cap=dX + 1)
    p_dS = sec510(data, len(B), dX)          # 5.10(2) with the per-sector constant
    p_d  = sec510(data, len(B), d)           # 5.10(2) as stated
    return dict(tag=tag, n=n, nA=len(A), nB=len(B), dX=dX, dZ=dZ, d=d, dsec=dX,
                glike=(bad == 0), nf=tot, dR=dR, dcirc=dc, T=T, deff=de,
                span_max=span_max, contig=contig_ok, nsol=nsol, nspan_gt_d=nspan_gt_d,
                p_dS=p_dS, p_d=p_d)

def main():
    rng = random.Random(20260823)
    codes = []
    for m in (3, 4, 5):
        n, A, B = chain(m);        codes.append(("chain%d" % m, n, A, B))
    for m in (3, 4):
        n, A, B = cyclic_chain(m); codes.append(("cyc%d" % m, n, A, B))
    codes += random_codes(rng, 40)
    rows = []
    for (name, n, A, B) in codes:
        Rmax = 4 if n <= 8 else 3
        scheds = ['NI_Zfirst', 'NI_Xfirst'] + ['random'] * 60
        got = 0
        for kind in scheds:
            gates, tx, tz = make_schedule(n, A, B, kind, rng)
            if not mc_ok(n, A, B, tx, tz): continue
            if kind == 'random' and got >= 4: break
            rows.append(run_sector("%s/%s/Zmem" % (name, kind), n, A, B, gates, tx, tz, Rmax))
            A2, B2, g2, tx2, tz2 = mirror_instance(n, A, B, tx, tz)
            assert mc_ok(n, A2, B2, tx2, tz2)
            rows.append(run_sector("%s/%s/Xmem" % (name, kind), n, A2, B2, g2, tx2, tz2, Rmax))
            got += 1
    # ... printing of the per-instance table and of the summary block below ...
```

**Genuine output — the head of the table and the full summary block** (the middle of the 194-row
table is elided for length; the summary counts every row):

```text
instance                   dX dZ dsec  d GL deff dcirc d_R (R=1..)    span cont spd W=ds  W=d ok
------------------------------------------------------------------------------------------------
chain3/NI_Zfirst/Zmem       3  2    3  2  Y    3     3 3,3,3,3           3    Y   2    3 None OK
chain3/NI_Zfirst/Xmem       2  3    2  2  Y    1     1 1,1,1,1           1    Y   0    1    1 OK
chain3/NI_Xfirst/Zmem       3  2    3  2  Y    3     3 3,3,3,3           3    Y   2    3 None OK
chain3/NI_Xfirst/Xmem       2  3    2  2  Y    1     1 1,1,1,1           1    Y   0    1    1 OK
chain3/random/Zmem          3  2    3  2  Y    3     3 3,3,3,3           3    Y   4    3 None OK
chain3/random/Xmem          2  3    2  2  Y    1     1 1,1,1,1           1    Y   0    1    1 OK
chain3/random/Zmem          3  2    3  2  Y    3     3 3,3,3,3           3    Y   4    3 None OK
chain3/random/Xmem          2  3    2  2  Y    1     1 1,1,1,1           1    Y   0    1    1 OK
chain4/NI_Zfirst/Zmem       4  2    4  2  Y    4     4 4,4,4,4           4    Y  17    4 None OK
chain4/NI_Zfirst/Xmem       2  4    2  2  Y    1     1 1,1,1,1           1    Y   0    1    1 OK
chain4/NI_Xfirst/Zmem       4  2    4  2  Y    4     4 4,4,4,4           4    Y  17    4 None OK
chain4/NI_Xfirst/Xmem       2  4    2  2  Y    1     1 1,1,1,1           1    Y   0    1    1 OK
chain5/NI_Zfirst/Zmem       5  2    5  2  Y    5     5 5,5,5          None    Y   0    5 None OK
chain5/NI_Zfirst/Xmem       2  5    2  2  Y    1     1 1,1,1             1    Y   0    1    1 OK
chain5/NI_Xfirst/Zmem       5  2    5  2  Y    5     5 5,5,5          None    Y   0    5 None OK
chain5/NI_Xfirst/Xmem       2  5    2  2  Y    1     1 1,1,1             1    Y   0    1    1 OK
cyc3/NI_Zfirst/Zmem         3  2    3  2  Y    3     3 3,3,3,3           2    Y   0    3 None OK
cyc3/NI_Zfirst/Xmem         2  3    2  2  Y    1     1 1,1,1,1           1    Y   0    1    1 OK
cyc3/NI_Xfirst/Zmem         3  2    3  2  Y    3     3 3,3,3,3           2    Y   0    3 None OK
cyc3/NI_Xfirst/Xmem         2  3    2  2  Y    1     1 1,1,1,1           1    Y   0    1    1 OK
cyc4/NI_Zfirst/Zmem         4  2    4  2  Y    4     4 4,4,4,4           3    Y   4    4 None OK
cyc4/NI_Zfirst/Xmem         2  4    2  2  Y    1     1 1,1,1,1           1    Y   0    1    1 OK
cyc4/NI_Xfirst/Zmem         4  2    4  2  Y    4     4 4,4,4,4           3    Y   4    4 None OK
cyc4/NI_Xfirst/Xmem         2  4    2  2  Y    1     1 1,1,1,1           1    Y   0    1    1 OK
rand00/NI_Zfirst/Zmem       3  2    3  2  Y    2     2 2,2,2,2           2    Y   0    2    2 OK
rand00/NI_Zfirst/Xmem       2  3    2  2  n    2     2 2,2,2,2           2    Y   0    2    2 OK
   ... 166 further rows ...
rand21/NI_Zfirst/Zmem       3  2    3  2  n    3     3 3,3,3,3           3    Y   2    3 None OK
rand39/NI_Xfirst/Xmem       2  3    2  2  n    1     1 1,1,1,1           1    Y   0    1    1 OK

instances (code, schedule, sector) ............ 194
  graph-like (Def 1.12) ....................... 78
  VIOLATIONS of corrected ceiling d_circ <= d_sec  0
  VIOLATIONS of 5.9 (contiguity, span<=weight) .. 0
  instances where the OLD constant d FAILS ...... 39   (d_circ > d)
  instances attaining d_circ = d_sec > d (tight)  39
  5.10(2) with W = d_sec disagrees with truth ... 0
  5.10(2) with W = d returns nothing/wrong ...... 39
  min-weight witnesses censused ................. 5892
  of which span > d (excluded by the old window)  138
  d_R non-monotone (should be 0) ................ 0
  d_eff <= d_circ <= d_sec violated ............. 0
  instances with d_R != d_last for some R >= d .. 0   (the unargued band, empirically)
```

Post-analysis of the same table:

```text
rows parsed: 194
distinct codes: 45
distinct (code, schedule) pairs: 96
instances with d_circ > d: 39  of which graph-like: 13
max (d_sec - d) over failures: 3
max (d_circ - d) over failures: 3
whole-circuit checks (min over the two sectors) : 96  violations of d_circ(C) <= d : 0
instances where max span > d: 35
```

**Reading.**

* **The corrected ceiling holds everywhere.** 194 instances — 45 distinct codes, 96
  (code, schedule) pairs, every one with `d_X ≠ d_Z` and `min(d_X,d_Z) ≥ 2`, both memory sectors,
  non-interleaved (both block orders) and (MC)-passing interleaved schedules — and **zero**
  violations of `d_circ(sector) ≤ d_sec`, of `d_eff ≤ d_circ ≤ d_sec`, or of 5.9.
* **The old constant fails on 39 of them**, 13 of which are graph-like and therefore inside the
  node claim's own scope. On all 39, 5.10(2) at `W = d` returns nothing or the wrong value; on all
  194, 5.10(2) at `W = d_sec` returns exactly the directly simulated ground truth.
* **The corrected constant is attained on all 39** (`d_circ = d_sec > d`), and the margin reaches
  `d_sec − d = 3` inside this sweep; Proposition D makes it unbounded.
* **Contiguity is untouched.** 5 892 minimum-weight witnesses censused, 5 892 contiguous with
  `span ≤ weight`; 138 of them have span `> d`, i.e. are precisely the witnesses the stated
  "over `≤ d` consecutive rounds" window would have thrown away.
* **The whole-circuit inequality survives**: over the 96 (code, schedule) pairs, the min over the
  two sectors satisfies `d_circ(C) ≤ d` in every case, as Lemma A predicts.
* **The band is empty in practice but was still unargued.** No instance had `d_R ≠ d_∞` at any
  `R ≥ 1`, so no counterexample to the *old* claim exists in this sweep; the repair closes a
  coverage gap in the argument, exactly as the wave-17 review's limitation 4 anticipated.

### 6.3 What the sweep does **not** cover

* Only `k = 1` codes, so that the single observable `Z_L` is exact; for `k ≥ 2` the search must
  range over all `k` observables and the numbers here would need re-running.
* `n ≤ 10`, `|ℬ| ≤ 4`, `R ≤ 4`, and `d_sec ≤ 5` — small enough that the syndrome-state search is
  exhaustive.
* The census is run at `R = R_max` and skipped where `d_circ > 4` (the two `chain5` Z-memory rows
  report `span = None` for that reason); their ceiling, monotonicity and 5.10(2) checks did run.
* Interleaved schedules are under-represented, because random schedules on these small codes fail
  (MC) most of the time; `chain3` contributes two.
* No campaign instance (Steane, rotated surface, `[[4,2,2]]`, gross) is re-measured here — they all
  have `d_X = d_Z`, on which the old and new constants coincide, and the wave-17 review already
  reproduced the Steane numbers.

---

## 7. What this amendment does NOT do

1. **It does not repair the `repair ≥ 3` gap** (§7.2), which remains the base document's located
   gap and, per the wave-16 adjudication, outside the node claim.
2. **It does not touch the root node's blockers S1 and S2** — the missing minimum-weight qualifier
   at the root, and the `R` clause's over-wide scope. §5.2 is offered only so that both root edits
   can be made in one move.
3. **It applies no claim edit and assigns no level.** §5 prints strings and digests; installing
   them, re-binding reviews, and re-adjudicating are dispatcher acts.
4. **It does not adjudicate the `sat` family.** One live ambiguity is flagged for that node:
   Amendment 1 §3.5 reads sibling Corollary 7.3's `d_eff(M)` as a single quantity, but `d_eff` is a
   per-sector object (Definition 1.16 is built from one sector's residuals) while `R_sat` is
   whole-circuit. For asymmetric codes the two sectors have different `d_eff`, and Corollary 7.3's
   dichotomy needs `d_eff` read as the min over sectors. This does not affect anything in §2–§5.
5. **It does not reproduce any large proposer scan** (98 811 schedules, 3 855/3 855,
   321 059/321 059), nor the wave-17 review's 27 562 census at its own location-counting
   convention.
6. **It does not attack the 公共定义.** `d_eff(M) <= d_circ(C(M)) <= d` is read as a whole-circuit
   statement — the only reading its `d_circ(C)` supports — and Lemma A *proves* it rather than
   assuming it. The defect was always downstream, in the transposition.
7. **This amendment is unreviewed.** The derivations of §2 are proposer-level and complete as
   written; they have had no adversarial reading. `DAG_PROTOCOL` §3's bar for `PROVED` is
   independent adversarial review of a complete argument, and only the first half is supplied here.

**No promotion.** This append-only proposer amendment supplies checkable candidate repairs and a
proposed claim string only. It does not assign `PROVED`, `CERTIFIED`, `CERTIFIED-LEAN`, or any
other status to the base proof, to the amendments, to these repairs, or to either node.

## 8. Verification checklist

- [x] Reproduced the SHA-256 hashes and byte/line counts of the base proof, Amendment 1,
  Amendment 2, the wave-17 review, the scope adjudication, and the frozen 公共定义 before writing.
- [x] Revalidated the claim-hash pipeline against two independently recorded digests
  (`2c8fe9e3…`, `bd1aa84e…`) before proposing any new claim string.
- [x] Applied the §5 claim edits **programmatically** to the current claim text, asserting that each
  anchor occurs exactly once; the printed strings are the outputs of those substitutions, not
  retyped.
- [x] Checked every "Old" quotation of §3 programmatically against its source file: all 15 occur
  exactly once, modulo line-wrapping.
- [x] Checked Lemma A against Definitions 1.5, 1.8, 1.9, 1.11, 1.13.1 and Lemma 4.1; it uses no
  step whose scope is narrower than "legal single-ancilla CSS schedule with ideal boundaries".
- [x] Verified Lemma A's construction by direct simulation on the wave-17 witness (0 detectors, 1
  observable flip, weight `d_X`).
- [x] Verified the corrected ceiling, the corrected 5.10(2) window, contiguity, and monotonicity on
  194 (code, schedule, sector) instances with `d_X ≠ d_Z`, both sectors: 0 violations.
- [x] Confirmed that the whole-circuit readings of 5.10(1) and 5.10(2) are true with the constant
  `d`, and that Amendment 2's L2 dichotomy survives on that reading.
- [x] No existing file, proof-DAG object, scheduler file, generated view, or canonical record was
  modified; `research/` was read only.
