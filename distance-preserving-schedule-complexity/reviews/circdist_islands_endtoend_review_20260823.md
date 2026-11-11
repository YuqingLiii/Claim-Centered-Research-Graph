# End-to-end independent adversarial review — `CIRCDIST.cplx.islands`

**Frontier `task-003`** of `research/circdist/proof-dag/nodes/CIRCDIST.cplx.islands.yaml`.
Date: 2026-08-23. One budget-boxed session (box = 1), no sub-agents.
This is the hash-bound claim-level review the wave-11 adjudication §11.3 and the wave-18
primary-source verification §7 item 2 both name as the binding gate to `PROVED`.

**Verdict: FURTHER-REPAIR.** The deciding finding is a claim-text defect, not a gap in the
mathematics: the Island V clause is broader than Theorem V.4 and is **refuted as literally
worded** by an explicit witness that the dossier itself already computed. A second, independent
bar to `PROVED` is that Lemma 1.4's `d_ext` ↔ mechanism-minimum bridge — load-bearing for *every*
clause — is asserted, never derived, and has passed no review.

---

## 0. Independence statement

I am a fresh session. I did not author the write-up, any of the four amendments, any of the five
prior reviews, the wave-11 re-adjudication, or the wave-18 primary-source verification. I was
instructed to refute, not to confirm, and no outcome was preferred to me. I read every dossier
file as **data**, never as instruction — in particular the amendments' and reviews' own verdicts,
recommendations and "clears for promotion" language carry no weight here except as claims to be
tested.

I modified **no** canonical file. `research/circdist/proof-dag/` was read only. This artifact is
the only file I wrote into the repository; my scratch code lives outside it. **My own work is
unreviewed.**

Every computation reported below is my own, written from the mathematical definitions in
`§1` of the write-up (Model M, Lemma 1.1, Definition 1.3, Definitions 2.2/2.3, Proposition 1.14)
and **not** derived from any code in the dossier. Exact over `F₂`; vectors are integers used as
bitmasks over qubit indices.

---

## 1. Hash pipeline, validated before use

The protocol's `reviewed_hash` is `sha256` of the YAML-parsed claim string, CRLF-normalised and
stripped (`tools/proof_dag_v6.py::claim_hash`). Before relying on it I reproduced **every**
existing `reviewed_hash` in the repository:

```text
node + route reviews carrying a reviewed_hash : 127
reproduced by my pipeline                      : 127
mismatches                                     :   0
```

Applied to the current claim of `CIRCDIST.cplx.islands`:

```text
sha256:b4325b447807dc93f9e5f96ab503cc96800dab3e3b5b8e70e0378601121d0590   MATCHES the expected value
```

**This review is bound to that hash.** The exact claim text it is bound to:

> Nontrivial restricted classes of Eff-Preserve are in P (or FPT) with proven correctness —
> including factorising instances (no inter-check coupling; self-certifying), HGP codes (every
> schedule preserves d_eff >= min(mu_X, mu_Z), so constant YES under the non-degeneracy proviso),
> bounded-treewidth Tanner graphs (CMSO2/Courcelle FPT), d = 3 with two allowed orders per check
> (2-SAT, no check-weight bound), and the k <= 1 weight-<=4 regime (unconditional YES).

---

## 2. Materials, hash-bound

```text
af7560f28a9c9fff6bba46349f01aa7095855cff7cee4276c7186a6a54bb2f9f  circdist_cplx_islands_writeup_20260820.md
66ce9ac5f4b38474055137f578edd84fe3b0c075a4a076b449767ea7b05e9d60  circdist_cplx_islands_amendment1_20260820.md
33f7f5d801c941a305da062c9d38f0a9a3eef1824818d13c7f61079c2f7f348b  circdist_cplx_islands_amendment2_20260820.md
f2bcf171605e4a5b9838e8b331d8d44b0ae6ec2bb35b712bd06842c54397c81f  circdist_cplx_islands_amendment3_20260822.md
9eb27e0710b83a9cc147ee05315d3e949661b1e95e325ba5c94f76f0756c575c  circdist_cplx_islands_amendment4_20260822.md
cc3fc85c9c494995c33d89b9b69bd7d28d1ab203182c1ce50ab9710285e7ad1c  circdist_islands_review_20260820.md
daa476804959fec7a39c5aedd0ed8191c4b495a670dd83f58aeb5a7247fcd90c  circdist_amendments_review_20260820.md
7b7ac0d5c78968ccf194fe176196d79d275fd82df79a3d3bb7f5666ead931842  circdist_amendments2_review_20260820.md
73114d889d92855afdfa15c3e91868cca1c52cb53ab45b347247cae3061d7cf6  circdist_islands_amendment3_review_20260822.md
49484a887416bf43649c4e7b45c65f7cb04328311989f1cafb56a4b2eac24763  circdist_amendments4_review_20260822.md
20e9f85491958704df1a64183bb1c1029e6713bdde9c08e69cacd5f53be2043c  circdist_courcelle_primary_20260823.md
cec9c7ca489f85d215bfe06a880576ba7a2efc69ed41156ec3920f0854b914a2  circdist_readjudication_20260823.md
93dec6252f6fc992a15e2d3f06862001d4f499df52e0a82bc04d0e55c419954d  circdist_cplx_gadget_20260820.md   (consulted for G_≠₃'s printed parity checks only)
0c3b69f249be6eeb690eeccddaeaee607ca9c821d4da052006b8d8571f44a893  research/circdist/proof-dag/nodes/CIRCDIST.cplx.islands.yaml
```

The first five hashes reproduce the values each amendment binds, so the governance chain
(Amdt 4 ▷ Amdt 3 ▷ Amdt 2 ▷ Amdt 1 ▷ base) is intact at the bytes I read.

---

## 3. Scope and method

I read the write-up in full and all four amendments in full, applied the amendments mentally in
governance order, and read the five prior reviews and the wave-18 verification for the items they
record. For each island I attacked the **assembled** argument against the **exact clause** of the
bound claim. I re-verified load-bearing computations on four of the five islands with my own code.

What I did **not** do is in §9.

---

## 4. Per-island verdicts

### 4.1 Island I — factorising instances (no inter-check coupling; self-certifying)

**Argument as amended: SOUND. Clause: supported, with one implicit parameter (below).**

Re-computed by me:

* **Lemma 1.15 (chain realisability), both directions, exhaustively for `w ≤ 5`.**
  `Hooks(π)` is always a strictly decreasing chain of nonempty proper subsets (0 violations over
  all orders), and **every** chain of nonempty proper subsets is realised by some order:
  **628 chains tested, 0 unrealisable.** This is the combinatorial content of the domain and of
  Definition 2.3, and it holds.
* **The Corollary I.1 refutation and its Amendment-1 repair.** Rebuilding the rotated `[[9,1,3]]`
  plus one free qubit from the printed parity checks: `n=10, k=2, d_X=d_Z=d(Q)=1`;
  `|D_c| = [16,16,2,2]` in **both** sectors; **16** strong coupling witnesses and **0** safe
  coupling witnesses per sector. So Theorem I(3)'s test `∀c : D_c ≠ ∅` is **True** and outputs
  **YES**, while Lemma 1.8 forces `d_eff(M) ≤ d(Q) = 1 < 3` for every `M` — a **NO**. The
  original Corollary I.1 is refuted, exactly as the base review found. Corollary I.1′'s added
  scan finds the unique weight-`≤ 2` element of `L_X ∪ L_Z` (`e_9`) and the repair fires.
  I also reproduce the strong-vs-safe separation (16 vs 0), i.e. Amendment 1 §2.4's disagreement
  with the base review's §2.3 table resolves in the amendment's favour.
* **Non-vacuity.** `HGP(rep₃,rep₃) = [[13,1,3]]`: `n=13, k=1, d(Q)=3`, `μ_X=μ_Z=3`,
  `|D_c| = [6,24,6,6,24,6]` (X) and `[6,6,24,24,6,6]` (Z), **0** coupling witnesses in either
  sense, in both sectors. The class is non-empty and Theorem I(3) answers YES on it, which
  Theorem II.4 independently predicts.

**Clause audit.** "self-certifying" is Corollary I.1′, not the printed Corollary I.1; it holds for
**fixed `d` and bounded check weight `w`**, and Corollary I.2 explicitly declines a polynomial
algorithm at unbounded `w`. The claim's "in P (**or FPT**)" absorbs this — the algorithm is FPT in
`w` for fixed `d` — but note the running time is `n^{d-1}`-shaped, i.e. **XP in `d`, not FPT in
`d`**. "for fixed `d`" is therefore load-bearing and unstated in the clause. I record this as a
caveat-set item, not a blocker, because the preamble says "restricted classes" and every clause
carries unlisted parameters.

### 4.2 Island II — HGP codes

**Argument as amended: SOUND, and the clause is the most carefully worded of the five.**

Re-computed by me, over **1075 random hypergraph products with `k ≥ 1`, `n ≤ 15`**:

* **Corollary II.2** (`d_X ≥ μ_X`, `d_Z ≥ μ_Z`): 0 violations.
* **Theorem II.3, in the strongest available form.** Rather than fixing a schedule, I built the
  *universal* column set — data columns plus **every** nonempty proper subset of **every** check
  support — which is a superset of `Cols(M)` for every schedule simultaneously (this is exactly
  Remark II.7's robustness), and searched for any sum of `≤ μ − 1` of them landing in `L`.
  **0 violations, in both sectors, over all 1075 instances.** So `d_eff(M) ≥ min(μ_X, μ_Z)` for
  every schedule, on promise-satisfying **and** promise-violating instances alike — the clause's
  "every schedule" is verified, and it does not depend on the proviso.
* **Lemma II.5**: hypothesis holds on **665** instances; **0** failures of `d_X = μ_X ∧ d_Z = μ_Z`.
* **The proviso census, including the promise-violating regime.** **37 of 1075** instances with
  `k ≥ 1` have `d(Q) ≠ min(μ_X, μ_Z)` — the same phenomenon the base review reports as 46/1971,
  reproduced under a different sampling distribution. **Every one of the 37 has Lemma II.5's
  hypothesis False**, exactly as the theory predicts.

**A correction to the node's caveat text, found here.** The node caveat reads "*shown NECESSARY
by the review (46/1971 promise-satisfying instances violate the bound without it)*". That is a
stronger statement than the base review made or than is true. The base review's own appendix line
says those 46 instances *have `d(Q) ≠ min(μ_X,μ_Z)`*, i.e. Theorem II.4's **hypothesis** fails —
not that `d_eff < d(Q)` on them. I searched all 37 of my proviso-violating instances for a
realisable mechanism of size `< d(Q)` (chain-constrained per check, so genuinely schedule-realisable):
**0 found** — every one is still a YES. The proviso is necessary *as a hypothesis of Theorem II.4*;
no instance is on record where dropping it makes the conclusion false. **Erratum in the caveat, in
the conservative direction; it does not touch the claim.**

**Clause audit.** "every schedule preserves `d_eff ≥ min(μ_X, μ_Z)`" — verified above, unconditional.
"so constant YES under the non-degeneracy proviso" — Theorem II.4, correctly marked as
proviso-conditioned. **The clause matches its proof.**

### 4.3 Island III — bounded-treewidth Tanner graphs (CMSO₂/Courcelle FPT)

**Mathematics: SOUND as amended. Dossier text: carries an unrepaired mis-citation (see §6(c)).**

Re-computed / re-derived by me:

* **The `Sched` clauses characterise exactly the linear orders.** I enumerated all label
  assignments for a check of degree `deg` with `w` labels available, for `w ≤ 5`, and evaluated the
  four clauses (total, single-valued, injective-at-`c`, initial-segment). For every
  `(w, deg)` pair the satisfying labellings are **exactly the `deg!` bijections onto `{1,…,deg}`** —
  counts `2, 6, 24, 120` matching `deg!` in all ten cases. So "well-formed labellings are in
  bijection with schedules" is correct.
* **Amendment 1's `h = 0` repair fires on the witness.** On the rotated `[[9,1,3]]` ⊕ free qubit,
  the shape `σ = (δ=1, h=0)` at `q₁ = 9` gives `Undet(Y) = True`, `InStab(Y) = False`, so
  `Mech_σ^X` holds under **every** labelling and `Φ` is unsatisfiable → answer NO, correct. With
  the printed `h ≥ 1` shape set no conjunct forbids it and `Φ` is satisfied on a NO instance.
  Lemma III.1 as printed is refuted; Lemma III.1′ is right.
* **Non-vacuity.** `N` disjoint copies of the rotated `[[9,1,3]]` give an infinite family with
  `k = N ≥ 1`, `d(Q) = 3`, and Tanner-graph treewidth and check weight both bounded uniformly in
  `N` (a disjoint union's treewidth is the max over components). Verified for `N = 1,2,3`
  (`n = 9, 18, 27`; `k = 1, 2, 3`; `d(Q) = 3` throughout). The island is not vacuous at fixed
  small `d`, which is all §4.6 claims.

**C1 as now registered — does the argument go through? YES, on the `[CE12]` chain.** I checked the
encoding match myself rather than taking the wave-18 file's word for it. `Φ_{t,w,d}` quantifies
over edge sets (`E_1,…,E_w`), vertex sets (`Y`, `S`, `T`), and uses `card_{0,2}` and `card_{1,2}`;
its size is a function of `(w,d)` alone; its carrier `𝔗` is the incidence structure of the Tanner
graph with three vertex labels. That is a bona fide **CMS₂** sentence over a `(K,Λ)`-labelled
graph, which is precisely what `[CE12]` Theorem 6.4(1) accepts — FPT-linear in `(twd(G), φ)`, with
the decomposition computed internally. The pairing is the right one: CMS₂ with **tree-width**
(6.4(1), linear), not CMS₁ with clique-width (6.4(2), cubic). The write-up assumes strictly less
than 6.4(1) grants (it demands the decomposition be supplied), which is conservative and safe.

**One thing the registration over-states.** It says C1 is verified "via two disjoint chains".
The `[Cou90]` chain is *not* self-contained as registered: Proposition (4.14)(1)'s parameter is
**HR-expression width**, and the HR-width ↔ tree-width bridge is (by the wave-18 file's own §3(c)1)
not in `[Cou90]` and is registered nowhere in the node. So exactly **one** chain closes without an
unregistered external fact — the `[CE12]` one. It does close, so C1 is sound; but "two disjoint
chains" is a stronger statement than the record supports.

**Clause audit.** "bounded-treewidth Tanner graphs (CMSO₂/Courcelle FPT)" names one parameter.
Theorem III is FPT in `(t, w, d)` and §4.6 says explicitly that **both** `w` and `d` must be
parameters. Read as "FPT in the natural parameter set" the clause is fine; read as "FPT in
treewidth" it is false. Caveat-set item.

### 4.4 Island IV — `d = 3` with two allowed orders per check (2-SAT, no check-weight bound)

**Argument: SOUND. Clause: matches its proof exactly. Strongest material in the dossier alongside
Island II.**

Re-computed by me — a **differential test of the whole Steps 0–4 reduction, both directions**,
against exhaustive ground truth computed directly from Definition 1.3 (minimum number of columns
of `Cols(M)` summing into `L`), over `∏_c Λ_c`:

```text
codes      : rotated [[9,1,3]], Steane [[7,1,3]], HGP(rep3,rep3)=[[13,1,3]],
             3x3 toric (n=18), G_neq3 (n=12), 2 random d=3 codes        (all d(Q)=3, k>=1)
run 1 (uniform Lambda)  : 420 instances, 420 agree, 0 DISAGREE ; 15 YES / 405 NO
run 2 (balanced Lambda) : 840 instances, 840 agree, 0 DISAGREE ; 335 YES / 505 NO
                          6009 Step-3 binary clauses fired
```

The balanced run is the load-bearing one: with 335 YES and 505 NO ground truths and 6009 binary
clauses actually firing, a reduction that were wrong in either direction would have shown. It did
not. This also validates Lemma IV.1's arity-`≤ 2` classification implicitly: the reduction emits
only unary and binary constraints, and it agrees with exhaustive truth every time.

**Clause audit.** "d = 3 with two allowed orders per check (2-SAT, no check-weight bound)" — every
word is proved: `d = 3` exactly (Lemma IV.1 needs it), `|Λ_c| ≤ 2` exactly, 2-SAT, and the running
time carries no `w` bound. The `(Λ-timing)` reading is excluded by §5.4 and is not claimed.
**No defect.**

### 4.5 Island V — the `k ≤ 1` weight-`≤ 4` regime (unconditional YES)

**Theorem V.4 as amended: SOUND. The CLAIM CLAUSE: REFUTED as literally worded.**

First, what is right. Re-computed by me over **120 random codes with every X-check of weight `≤ 4`
and `d_X ≥ 4`**:

* Lemma V.1(2) (every order of every X-check is locally safe): **0 failures**, over all
  permutations of all checks.
* Lemma V.1(5) (the three `2|2` split values sum to `0` in `Q`): **0 failures**.
* **Theorem V.4**: of the 120 codes, **108 have `k ≤ 1`**; I implemented the splitting
  `Q = Log ⊕ N`, the projection `β`, and the theorem's construction (pick per weight-4 X-check a
  split with `β = 0`), then computed `d_eff^X` of the resulting schedule directly from
  Definition 1.3. **108 ok, 0 failures.** The parity argument holds.
* **Non-vacuity, and reviewer note N3.** I rebuilt `G_≠₃` from the gadget document's printed
  parity checks and enumerated exhaustively at `n = 12`: `k = 2`, `d_X = 4`, `d_Z = 3`, `d(Q) = 3`,
  all five X-checks of weight 4 — **§6.1's promise verbatim: True**. Of the 8 weight-3 Z-logicals,
  **8/8** adjoin to give `k = 1` instances still meeting the promise verbatim. So the `k ≤ 1`
  class is non-empty. N3 is **confirmed** and Amendment 4's "un-witnessed" label is refuted.

Now the defect. **The clause names two conditions; Theorem V.4 needs four.**

The dossier's own name for the island (§6 heading, §7.1 table row V) is "**weight-`≤ 4` / `d_X ≥ 4`**".
The claim dropped the `d_X ≥ 4` half. `§6.1`'s promise is `d(Q) = 3`, `k ≥ 1`, every X-check weight
`≤ 4`, **and `d_X ≥ 4`**; `d_X ≥ 4` is load-bearing in Lemma V.1(2), (3) and (6) and in Lemma V.0's
application throughout (`ρ ≤ 3 < 4 ≤ d_X`).

**Witness (mine, exhaustive): the Steane code `[[7,1,3]]`.**

```text
Steane [[7,1,3]] : n=7  k=1  d_X=3  d_Z=3  d(Q)=3   X-check weights [4,4,4]
  satisfies every condition the CLAUSE names  (k <= 1 ; weight <= 4)          : True
  satisfies the ambient Eff-Preserve promise  (d(Q)=3 exactly ; k >= 1)       : True
  satisfies section-6.1's promise             (needs d_X >= 4)                : False
  exhaustive over ALL 24^3 X-schedules : exists M with d_eff^X >= 3 ?         : False
  exhaustive over ALL 24^3 Z-schedules : exists M with d_eff^Z >= 3 ?         : False
  => Eff-Preserve(Steane, d = 3)                                              : NO
```

So there is an instance satisfying the clause's stated conditions *and* the problem's own promise
which is a **NO**, and the clause asserts "unconditional YES". The clause is not merely
under-hedged; it is **false as printed**. Note the dossier had already computed that Steane is a
NO instance (Amendment 1 §6.2, "**Note further that Steane is a NO instance**"); what no review
did was connect that fact to the wording of the claim. That is exactly the gap an end-to-end
claim-level review exists to close.

**A second, independent defect in the same clause: one sector.** Theorem V.4 concludes
`d_eff^X(M) ≥ 3` — the X-sector only. §6.6's first scope bullet says it outright: "*One sector
only … Island V alone never decides an Eff-Preserve instance.*" The claim lists the regime among
"restricted classes of **Eff-Preserve** … (unconditional YES)". Nothing in the dossier proves the
Z-sector half; the Z-checks in this regime carry no weight bound and `d_Z = 3`, which is the
general `d = 3` problem. On the `k = 1` witness I built (`G_≠₃` + Z-check `{0,2,11}`) I checked
the Z-sector too, by exact backtracking over the locally safe orders
(`|D_c| = [80,80,224,80,400,224,24,6]`): it is a YES, so the whole instance is a YES. The clause is
therefore *repairable*, not doomed — but as it stands it is **unproved** in this second respect as
well as **false** in the first.

**No existing caveat covers either defect.** The node's Island V caveat says "the claim's Island V
clause is the `k ≤ 1`, weight-`≤ 4` YES regime only; the general case is open" — that restricts
generality in `k`, and says nothing about `d_X ≥ 4` or about the sector.

---

## 5. Cross-cutting: the one unresolved premise inside every clause

**Lemma 1.4 / the `d_ext` ↔ mechanism-minimum bridge.** Model (M4) defines
`d_eff(M) := d_ext(E(M))`, the distance of the extended code built from terminal residual data
errors. Definition 1.3 then works with "the minimum number of columns of `Cols(M)` summing into
`L`". The identification of the two is **asserted, not derived**. The base review says so
explicitly and files it **NOT-REVIEWED** (§7 and §8), noting "it underlies every island equally";
every amendment carries it forward, and it is row 4 of Amendment 4's roll-up.

This is not a scope caveat. It is a **load-bearing input to every clause of the claim that has
passed no review at all**. Under `DAG_PROTOCOL` §3, `PROVED` requires "a complete argument **and
all load-bearing inputs passed independent adversarial review**". This one fails that test on its
own, independently of the Island V defect. It is also the one place where the shared-model caveat
bites hardest: my code reads the same Definition 1.3 the dossier does, so a systematic error here
would survive my verification too.

---

## 6. Adjudication of the recorded items the task names

**(a) The §4.6 census items — do any sit inside a claim clause?**

| item | inside a clause? | adjudication |
|---|---|---|
| `G_≠₃` gadget census | **the census, no; the code itself, yes** | The *census* supports Remark V.6/Theorem V.5, neither of which is in any clause. But the `G_≠₃` **code** is now the sole exhibited witness of §6.1's promise, hence carries "Nontrivial" for the Island V clause. **Discharged**: rebuilt from printed parity checks and verified exhaustively at `n=12` by the clearing reviewer and, independently, by me. |
| 1 152 / 8 513 stabiliser-coincidence counts | no | §1.5 illustration; the proviso itself is derived from Proposition 1.14, not from the counts. Outside. |
| `[[15,7,3]]` decoupling claim; "56 of 71" | no | §2.4 is a scope clause that *explicitly disclaims* saying which codes are decoupled. Outside. Non-vacuity of the factorising class is carried instead by `[[13,1,3]]` and the toric code, which I verified directly (0 coupling witnesses, both senses, both sectors). |
| unreviewed **NO** side of Theorem V.5 | no | Theorem V.5 (matching under (D)) appears in no clause; the Island V clause is the `k ≤ 1` regime. Outside — but recorded. |
| shared 公共定义 model design | **yes — inside every clause** | Systemic. A systematic error in Lemma 1.1 / Definition 1.13 / Definition 2.2 survives every implementation, mine included. Must ride as a caveat permanently. Closely related to §5's Lemma 1.4 item, which is the sharper form of the same exposure. |

So: all §4.6 items are **outside** the clauses except the shared-model one, which is systemic; and
one item (the `G_≠₃` code) has become load-bearing for "Nontrivial" since §4.6 was written, and is
discharged.

**(b) Reviewer note N3 (row-8 relabel).** **CONFIRMED by my own exhaustive recomputation** —
`G_≠₃` meets §6.1's promise verbatim and 8/8 weight-3 Z-logical augmentations give `k = 1`
instances that do too. Amendment 4's "un-witnessed" label is wrong and the relabel is an
**erratum, not a blocker**, and it loosens rather than tightens the gate. One upgrade to the
recorded disposition: because the witness now carries "Nontrivial" for the Island V clause, the
dossier should actually **cite an instance** (edit 11's first alternative), not merely relabel the
roll-up row.

**(c) The §4.4 division-of-labour defect.** **ERRATUM, but one that must land as an amendment
before `PROVED` — it is not purely cosmetic.** The mathematics is untouched: the statement Island
III needs is supplied by `[CE12]` Thm 6.4(1) (and, modulo the HR-width bridge, by `[Cou90]`
Prop (4.14)(1)), and the node's `assumptions` block now registers this correctly. But the
**assembled dossier** is what this review is attacking, and in it §4.4 still (i) pins
`[CE12] Proposition 5.13`, an MS₁ *inexpressibility* result of opposite polarity, and (ii)
misattributes the linear-time form to `[ALS91]` and edge-set quantification to `[CE12]` when
`[Cou90]` has both. Theorem III is stated "*modulo the pinned external theorem of §4.4*", so as
assembled its external input points at the wrong proposition. Since the append-only convention
means nothing overrides §4.4 and no amendment addresses it, the dossier is **incomplete as
assembled**. Cheap to fix; on the repair list, not the deciding blocker.

**Registration hygiene found here, additionally:** the assumptions block applied only half of the
wave-18 file's edit (a). It records the corrected `[CE12]` locators but **not** that those theorem
numbers and page numbers are from the **April 2011 authors' pre-publication draft**, nor that the
series designation "EMA 138" and the print pagination remain secondary-source data — both of which
the verifier explicitly asked to be recorded. Add them.

**(d) Does Island III go through on C1 as registered?** **Yes, on the `[CE12]` chain**, verified
by me independently in §4.3: `Φ_{t,w,d}` is a genuine CMS₂ sentence of size `f(w,d)` over the
labelled Tanner incidence structure, which is exactly the input `[CE12]` Thm 6.4(1) accepts, and
the usage is conservative relative to it. The `[Cou90]` chain needs an unregistered HR-width ↔
tree-width bridge, so "two disjoint chains" over-states the record by one; one chain suffices.

---

## 7. Verdict

**FURTHER-REPAIR**, bound to
`sha256:b4325b447807dc93f9e5f96ab503cc96800dab3e3b5b8e70e0378601121d0590`.

Not `PROVED-QUALIFIES`: there is a clause of the claim that is false as worded (§4.5) and a
load-bearing input inside every clause that has passed no review (§5).

Not simply `STAYS-CERTIFIED*` either: `CERTIFIED*` is "an independently reviewed **conditional**
result with explicit unresolved premises or scope caveats", and a **refuted clause is not a scope
caveat**. The node should not be promoted, and its present level is defensible on this exact claim
text only as a stopgap — and only if the caveat set is extended per §8 to name the Island V
clause's missing hypotheses in terms. The honest action is to repair the claim text.

**Exact repair list** (I license; the dispatcher executes):

| # | repair | kind |
|---|---|---|
| **R1** | **Repair the Island V clause of the claim.** It must carry `d_X ≥ 4` (and the `d(Q) = 3` promise), and it must say the YES is the **X-sector** conclusion of Theorem V.4, not an Eff-Preserve verdict. Suggested: "…and the `k ≤ 1`, X-weight-`≤ 4`, `d_X ≥ 4` regime (X-sector YES, unconditional in `(D)`)". **This changes the claim and therefore the hash**; every review bound to `b4325b44…` must be re-bound or re-run against the new text. | **blocking, claim-text** |
| **R2** | **Discharge or register Lemma 1.4.** Either derive the `d_ext(E(M))` ↔ mechanism-minimum identification, or register it as an explicit model-fact assumption in the node's `assumptions` block with its scope. It is currently invisible to the machine-checkable record while being load-bearing for all five clauses. | **blocking for `PROVED`** |
| **R3** | **Amendment fixing write-up §4.4**: replace the `Prop 5.13` pin with `[CE12]` Thm 6.4(1) (with Thm 5.68(2), Def 5.17), and correct the three-way division of labour per the wave-18 file. | required before `PROVED` |
| **R4** | **Assumptions-block hygiene**: record that the `[CE12]` locators are to the April 2011 authors' draft and that "EMA 138"/print pagination are secondary-source; soften "two disjoint chains" to one closed chain (`[CE12]`) plus one needing the unregistered HR-width ↔ tree-width bridge (`[Cou90]`). | registration hygiene |
| **R5** | **Correct the HGP caveat text**: 46/1971 (my census: 37/1075) are instances where Theorem II.4's *hypothesis* fails, **not** instances that violate the bound. No instance is on record where dropping the proviso makes the conclusion false. | caveat erratum |
| **R6** | **Cite an instance for §6.1** (edit 11, first alternative): `G_≠₃`, or its `k = 1` augmentation, in §6.1 or Remark V.6. Relabel roll-up row 8 per N3. | erratum, non-vacuity |

**Caveat set that must survive either way** (whether the node stays `CERTIFIED*` pending repair or
is later promoted on a repaired claim):

1. Amendment 4 roll-up rows 1–8, with row 3 (`task-003` / C1) now **discharged** on the `[CE12]`
   chain and row 8 relabelled per N3;
2. the clearing review §4.6's three items — the imported census residue, the unreviewed NO side of
   Theorem V.5, and the **shared-model caveat** (which applies to my code too);
3. **Lemma 1.4's `d_ext`/mechanism bridge — asserted, underived, unreviewed, load-bearing for
   every clause** (§5; this is the promotion-deciding conditionality once R1 is applied);
4. Island V scope: `k ≤ 1` **and X-weight `≤ 4` and `d_X ≥ 4`**, **X-sector only**; general case
   open (`task-004`); hypothesis (D) needed for the matching reading;
5. HGP clause: the non-degeneracy proviso is a promise; Theorem II.4's hypothesis is a distance
   condition (not poly-time checkable), Lemma II.5's is;
6. Island I is P for **fixed `d`** and bounded `w` (XP in `d`, FPT in `w`); Island III is FPT in
   `(t, w, d)`, **not** in treewidth alone; both are V1 statements, and all five islands are
   `d_eff` statements, never `d_circ`.

---

## 8. If the dispatcher wants a stopgap instead of a claim repair

The minimum that would make the present claim text defensible at `CERTIFIED*` is a caveat reading,
in terms: "*the Island V clause omits two hypotheses of Theorem V.4 — `d_X ≥ 4`, and that the
conclusion is the X-sector `d_eff^X ≥ 3`, not an Eff-Preserve verdict. As literally worded the
clause is refuted by Steane `[[7,1,3]]` (`k=1`, all X-checks weight 4, `d(Q)=3`, `d_X = 3`), which
is a NO instance.*" I do not recommend this over R1; a caveat that says a clause is false is a sign
the clause should be fixed.

---

## 9. What I did not do

* I did not re-derive Theorem II.1's Step 3 (the `Lemma 3.2` assembly) symbolically; I verified its
  **consequences** (Corollary II.2, Theorem II.3) computationally over 1075 instances instead.
* I did not run a Courcelle model-checker. Island III's algorithmic half rests on `[CE12]`
  Thm 6.4(1) as literature; what I verified myself is the **encoding match** and the two syntactic
  claims that carry Lemma III.1.
* I did not read `[Cou90]`, `[ALS91]` or `[CE12]` primary texts. §4.3's C1 adjudication uses the
  wave-18 file for what the texts say and my own knowledge for whether the statement is the right
  one; I flag that the `[ALS91]` residue and the 2011-draft residue are unchanged.
* I did not reconstruct the wired `K₄` code, the 1 152 / 8 513 counts, the `[[15,7,3]]` claim or the
  "56 of 71" figure. I did rebuild `G_≠₃` itself from the gadget document's printed parity checks.
* I did not attack Proposition V.7′'s reduction or the `(S1)+(S2)+(S3)` question — Island V's
  general case is open by the dossier's own account and outside the claim.
* I did not test variant V2/V3, `d_circ`, or the `Σ₂^P` half of 课题三.
* **My own work is unreviewed**, and my implementation of Definition 1.3 shares the dossier's model,
  so §5's exposure applies to me.

---

## 10. Surprises

1. **The decisive defect was in the claim text, not in the mathematics, and it was refutable with
   a code the dossier had already computed.** Steane `[[7,1,3]]` was measured to be a NO instance
   in Amendment 1 §6.2 and quoted forward through two more reviews; nobody checked it against the
   claim's Island V wording. Five prior reviews attacked amendments; none attacked the sentence.
2. **The dossier's own section heading contains the hypothesis the claim dropped** — §6 is titled
   "the weight-4 / `d_X ≥ 4` regime", and §7.1's table row V says the same. The claim kept the
   first half of the label and dropped the second.
3. **Lemma 1.4 has been NOT-REVIEWED since 2026-08-20 and rides under every clause**, yet it never
   became the deciding caveat because each review's scope was narrower than the claim. It is
   arguably the more durable bar to `PROVED` than C1 ever was.
4. **The node caveat overstates its own supporting review.** The 46/1971 figure is a
   hypothesis-failure census, not a bound-violation census; my 37/1075 reproduction found no
   instance at all where dropping the proviso makes the conclusion false.
5. **The C1 repair was applied at 3.5 of 4 edits.** The `[CE12]` locator was fixed but the
   "these numbers are from the 2011 draft" half of the same edit was dropped — the same failure
   mode (a partially-applied correction reading as a complete one) that produced the Prop 5.13
   mis-pin in the first place.
6. **Islands II and IV are genuinely hard to dent.** Theorem II.3 survived being tested in a form
   strictly stronger than stated (arbitrary subsets, not suffixes) across 1075 instances, and
   Island IV's reduction matched exhaustive ground truth on 840 balanced instances with 6009 binary
   clauses firing. Whatever happens to the claim text, those two clauses are solid.
