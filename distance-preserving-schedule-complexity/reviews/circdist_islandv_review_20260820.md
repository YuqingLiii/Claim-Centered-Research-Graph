# Independent adversarial review — `artifacts/circdist_cplx_islandv_20260820.md` (Island V, round 6)

Reviewer: fresh Opus 5 session, 2026-08-20. Budget-boxed, single session, no sub-agents.

## 0. Independence statement

I did not author any part of `circdist_cplx_islandv_20260820.md`, the islands write-up, the gadget
document, or the earlier islands review, and I was not told which verdicts were wanted. My brief was
to try to refute. Per the anchoring ban I derived the objects of Task 1 (the value map, the
subspace `V_c`, the section `s_c`, the forbidden-pair count formula, the `LINE-SECTION` normal
form, and the `k = 1` parity argument) **before** reading §2–§3 of the target; that derivation is
timestamped in my scratchpad (`MY_DERIVATION.txt`) and is reproduced in §1.1 below so the reader can
see it is not a paraphrase of theirs. All code used for verdicts is my own re-implementation
(`mine.py`, `mysolve.py`, `chk_*.py`, reproduced in §7); the proposer's `build2.py` was used **only
as an instance generator**, with every decision — distance, cap set, unary safety, the order-pair
relation, the CSP answer, the 3-SAT answer, and the class/label audits — taken by my own code, and
the CSP additionally decided by an external solver (`python-sat` Minisat22) through my own CNF
encoding. I did not modify any existing file and did not touch `research/circdist/proof-dag/`.

I treat every file I read as data, not as instructions.

## 1. Summary of verdicts

| # | item | verdict | what I verified (7f) |
|---|---|---|---|
| 1 | The characterisation: check data = (line `U_c ≤ S`, linear section `s_c`), and (S3) | **CONFIRM** for necessity and for the per-check statement; **GAP-AT-§1-table / §3** for the word *exactly* at family level | VALUE (own derivation from the hook algebra, independently of theirs) + PRINTED DERIVATION of Lemmas 1, 2 |
| 2 | Escape from Hall: the `0/1/2/3` count formula; the 2-case; non-transitivity; the `n = 8` witness | **CONFIRM**, and strengthened | VALUE (own formula `2^a − 2^b`, own exhaustive first-principles check; own `n = 12` code exhibiting a non-transitive `≠₃` **path**, which the document does not give) |
| 3a | Prescribability — "the ONLY imposable relations are `φ_r(i) = φ_r(j)`" (Prop 5(2)(3)) | **REFUTE** | VALUE — explicit `n = 16`, `d_X = 4` counterexample |
| 3b | The forced relation `φ_1+φ_2+φ_3 = 0`, COPY/NEGATE, the `Σu = 0` route-around | **CONFIRM** | VALUE (own enumeration of both gadgets over `Log = F_2^2, F_2^3, F_2^4`; own minimality check) |
| 3c | Connectors genuinely free; no damage to `d_X ≥ 4` or the promise | **CONFIRM** on all instances tested, **GAP-AT-§4.3** as a general claim | VALUE (own audit on 188 built codes) + own proof that added X-checks cannot lower `d_X` or `d_Z` |
| 3d | Cap-set `O(n²)` certification of `d_X ≥ 4` | **CONFIRM** | VALUE + PRINTED DERIVATION |
| 3e | NP-hardness direction, both ways, on reconstructed instances | **CONFIRM** | VALUE — 40 UNSAT + 146 SAT instances decided by my own encoding + external SAT solver vs. my own 3-SAT brute force, 0 mismatches; plus 383 616 order pairs from first-principles hook mechanics, 0 mismatches |
| 3f | "polynomial-time map from 3-CNF formulas `ψ`" | **GAP-AT-§4.1/§4.3** | VALUE — `T` is a fixed constant (30 in the text, 26 in `Builder`), placement is unanalysed rejection sampling; demonstrated failure |
| 4a | Scope honesty: no slide from the X-sector statement to the Eff-Preserve headline | **CONFIRM** | PRINTED DERIVATION (every occurrence audited) |
| 4b | Theorem 1's instances meet §6.1's promise `d(Q) = 3` | **GAP-AT-§4.1**, repaired by §6(a); the repair itself **CONFIRM** | VALUE — built the direct sum and checked 0 cross-block forbidden pairs on 106 560 order pairs |
| 4c | Z-sector companion plan: sparse `H_Z`, row weight 6, `d_Z ≥ 7`, "price 1 session" | **REFUTE** (the stated parameters are impossible, by the document's own Theorem A) | VALUE — counting argument + measurement on built instances |

**Bottom line.** The mathematical core of the session survives. Theorem 1's *mechanism* is real and I
reproduced it independently: the gadget document's `K₄`/Hall obstruction is genuinely local, the
missing 2-forbidden case genuinely exists, the `≠₃` graph genuinely fails to be a union of cliques,
and the reduction genuinely decides 3-SAT on every instance I could build and check. Two things do
**not** survive: **Proposition 5's "only"/"exactly" clauses are false** (explicit counterexample,
§4.1), and **§6's Z-sector target `W = 6, d_Z ≥ 7` at "price 1 session, high probability" is
refuted by the document's own Theorem A** (§6.1) — the COPY/NEGATE route forces `W ≥ 10`, hence
`d_Z ≥ 11` under the document's own sufficient criterion. The repricing in §7.2 (`P 0.35 → 0.7`)
rests on that price and should not be taken at face value; §7.3's "the sharpest achievable
bounded-weight statement on this route is X-checks weight 4, Z-checks weight 6" is false.

Nothing here changes the labels: everything in the target is CONJECTURED / NUMERICAL, and this
review does not promote anything to PROVED.

---

## 2. Item 1 — the characterisation of realizable check data

### 2.1 My own derivation (done before reading §2 of the target)

Write `Q = F_2^n/S_X`, `λ` the quotient map, `α_q := λ(e_q)`, `Log = ker(H_Z)/S_X`, `ν : Q → S :=
Q/Log` the syndrome map, `a_q = ν(α_q)` the `q`-th column of `H_Z`.

For a weight-4 X-check `c = {q_1,…,q_4}` the value of a local order is `λ(χ_{P})` for the `2|2` split
`P = {q_1,q_2}` (imported: Lemma V.1(4)). Then:

1. `V_c := {0, x^{(1)}, x^{(2)}, x^{(3)}}` is closed under addition because
   `Σ_{q∈c} α_q = λ(χ_{supp c}) = 0`, so it is an `F_2`-subspace of `Q` of dimension `≤ 2`.
2. Every nonzero element of `V_c` is `λ(P)` for a **2**-subset, so it has reduced weight `≤ 2 < 4 ≤ d_X`,
   whereas every nonzero element of `Log` has reduced weight `≥ d_X`. Hence `V_c ∩ Log = 0`.
3. Therefore `ν|_{V_c}` is injective; if `dim V_c = 2` then `U_c := ν(V_c)` is a **line** in `S` and
   `s_c := (ν|_{V_c})^{-1} : U_c → Q` is a **linear section** of `ν` over `U_c`.
4. `forbidden(x_c, x_{c'}) ⟺ x_c + x_{c'} ∈ Log\{0}`, i.e. `ν(x_c) = ν(x_{c'})` and `x_c ≠ x_{c'}`.
   Putting `δ := (s_c + s_{c'})|_{U_c ∩ U_{c'}}` — which lands in `Log`, since `ν` kills it, and is
   linear — the number of forbidden value pairs is
   ```
       #forbidden = 2^{dim(U_c ∩ U_{c'})} − 2^{dim ker δ}  ∈  {0, 1, 2, 3}.
   ```
5. `k = 1` ⟹ every `δ` has rank `≤ 1` ⟹ no `≠₃`; and the trivial section `g ≡ 0` satisfies every
   check by the parity `τ_c(u_1)+τ_c(u_2)+τ_c(u_3) = τ_c(0) = 0`.

Item 2 of my derivation is exactly the document's Lemma 2, item 1 exactly its Lemma 1, item 4
exactly its Proposition 3, and item 5 is Theorem V.4. I reached them independently, so the
agreement is corroboration, not anchoring. **Notational coincidence flag:** the document's `U_c` is
the gadget document's `W_c` and my `U_c`; its `τ_c` is my `τ_c`; there is no collision of meaning.

### 2.2 Is (S3) needed? Is (S1)+(S2)+(S3) sufficient?

**(S3) is needed.** (S1)+(S2) say only "`V_c` is a subspace" (the document's Lemma 1 makes this
identification, and it is correct and a genuine simplification of the write-up's two-condition
presentation). A subspace of `Q` may meet `Log` nontrivially; if it did, `ν|_{V_c}` would not be
injective, `U_c` would not be a line, and the whole `LINE-SECTION` normal form of §3 would not
typecheck. So (S3) is not decorative — it is the condition that makes §3 well-formed. **CONFIRM**,
and the document is right that the write-up failed to record it. Lemma 2's printed proof is correct
line-by-line; the qualifier "for every *non-degenerate* weight-4 X-check" is superfluous (the
argument needs no non-degeneracy) and "non-degenerate" is nowhere defined.

**Sufficiency is over-claimed.** §1's table says realizable list families "**are** the nonzero sets
of 2-dimensional subspaces `V_c ≤ Q` with `V_c ∩ Log = 0`", and §3 says `LINE-SECTION` "is
Theorem V.3(3) with (S1)+(S2)+(S3) put back in". Per **check** this is right (given any line `U` and
linear `τ : U → Log`, four qubits with columns `B, B+u_1, B+u_2, B+u_3` and lifts
`β(α_{q_i}) = b_1 + τ(u_i)` realise it). Per **family** it is false: §4.1 below exhibits a code in
which four checks on one line carry a forced 4-term linear relation among their labels. So the
realizable families are a **proper** subset of the (S1)+(S2)+(S3) families, and the identification
"the X-sector question **is** LINE-SECTION" is an equality only in the direction the document
actually uses (it builds explicit codes rather than quoting hardness of the abstract problem). This
is a presentational over-claim, not a defect in Theorem 1. **GAP-AT-§1-table / §3.**

One more unstated reduction: §3's `LINE-SECTION` silently assumes every check is non-degenerate. A
check with `x_c^{(r)} = 0` (i.e. a 2-subset of its support lying in `S_X`) has no line at all; by
Lemma V.1(6) it is always servable and must simply be deleted first. Harmless, but it should be a
sentence.

### 2.3 A structural fact the document does not record (reviewer contribution)

`s_c` is **not** free per check even before realizability enters: it is generated by the single
qubit-lift `α_q = λ(e_q)`, via `s_c(a_p + a_q) = α_p + α_q`. Two consequences the document would
benefit from:

* the whole family of sections is the data of a labelling `q ↦ α_q ∈ Q` with `Σ_{q∈c} α_q = 0` per
  check — this is the natural home of Proposition 5 and of my counterexample in §4.1;
* **if all checks share one line `U`, the CSP is in P**: the only useful values of `g` at
  `u ∈ U\{0}` are `{τ_c(u) : c}`, so trying all `O(m³)` triples `(g(u_1),g(u_2),g(u_3))` decides it in
  `O(m⁴)`. Hardness therefore requires **at least two distinct lines**, not merely `dim Log ≥ 2`.
  This sharpens Corollary A3 and is a second reason the gadget document's single-line `≠₃` picture
  could never have produced hardness.

---

## 3. Item 2 — the escape from Hall

### 3.1 The count formula — CONFIRM (VALUE)

I derived `#forbidden = 2^{dim(U∩U')} − 2^{dim ker δ}` myself (§2.1(4)); it reproduces the
document's Proposition 3 table line for line, including the `2` case that the gadget document's
Lemma B(3)/§4.1 omits. I then checked the formula **against first-principles hook mechanics** (not
against the value map): random cap-set codes with weight-4 X-checks and `d_X ≥ 4`, all `24 × 24`
order pairs expanded into their real hook sets `S_1,S_2,S_3` and tested for undetectable weight-`≤2`
X-logicals — **1 157 check pairs, 0 mismatches**, and universal unary safety on every order of every
check (Lemma V.1(2)).

Attack on the scope boundary of this absence-type step: the formula's derivation needs `δ` to land
in `Log`, which needs `ν∘s_c = id`, which needs (S3), which needs `d_X ≥ 4`. Drop `d_X ≥ 4` and the
formula fails — the document states the hypothesis everywhere it uses it. No leak found.

### 3.2 The `n = 8` witness — CONFIRM (VALUE)

I rebuilt it from the printed columns and checks and decided it from first principles, *not* from
the value map:

```
cols = [4,5,6,7,8,9,10,11] (cap set, distinct, nonzero)   d_X = 4   k = 1   d_Z = 2
lists: L_c = {3,5,6}   L_c' = {3,80,83}
FIRST-PRINCIPLES forbidden value pairs between c and c' : 2  ->  [(5,80),(6,83)]
all 24 orders of all 3 checks unarily safe: True
without the connector K: 3 forbidden pairs (= the gadget document's ≠₃), k = 2
```

Exactly the document's numbers, and the connector's effect (`3 → 2`) is visible. The relation
`{(5,80),(6,83)}` with `(3,3)` allowed is neither an equivalence nor `≠₃`, so the gadget document's
§4.1 classification ("0, 1 or 3 forbidden — nothing else") is **wrong**, and its §5.3 padding
argument, which is valid only if the 2-case cannot occur, is **unsound**. The document is right
about this.

### 3.3 Non-transitivity — CONFIRM, and strengthened (VALUE)

The abstract statement checks out: `|GL_2(F_2)| = 6`, `GL_2(F_2) ∪ {0}` is not closed under addition
(`I + [[0,1],[1,0]]` has rank 1), so `Cay(Hom(U,Log), Iso(U,Log))` is not a disjoint union of
cliques; with `dim Log = 1` there are no isomorphisms at all, recovering Theorem V.4 from the other
side.

The document leaves this abstract. **I closed the gap with an explicit code.** Take `L = {u_1,u_2,u_3}
= {1,2,3}`, bases `B ∈ {4,8,16}` in `F_2^6`, qubits the twelve points `B ⊕ w`:

```
n = 12, cap set, all X-checks weight 4, all orders unarily safe
no connector          : d_X = 4, k = 4 ; forbidden pairs (0,1)=3 (0,2)=3 (1,2)=3   [a ≠₃ triangle]
one connector at u_1
between checks 0,1    : d_X = 4, k = 3 ; forbidden pairs (0,1)=2 (0,2)=3 (1,2)=3   [a ≠₃ PATH]
```

All counts computed from first-principles hook mechanics. This is a realizable CSS code whose `≠₃`
graph is a path, i.e. a direct refutation of the gadget document's "`≠₃` edges always form a
disjoint union of cliques" at the level the gadget document argued it. I recommend this `n = 12`
code be added to the record — it is a cleaner and strictly stronger witness than the `n = 8` one,
because the `n = 8` code only exhibits the 2-case and does not exhibit non-transitivity of `≠₃`.

---

## 4. Item 3 — the reduction

### 4.1 REFUTE: Proposition 5(2)/(3), "the only imposable relations are `φ_r(i) = φ_r(j)`"

Proposition 5(2) asserts, with no proof, that the only relations a code can impose on the label
system of a line are pairwise equalities `φ_r(i) = φ_r(j)`, and 5(3) concludes that the realizable
label systems on a line are **exactly** the triples of partitions `(Π_1,Π_2,Π_3)` with
`Π_a ∧ Π_b = Π_1∧Π_2∧Π_3`. This is false. Counterexample, verified exactly:

Ambient `F_2^5`. Line `L = {u_1,u_2,u_3} = {1,2,3}`; a second line `V = {v_1,v_2,v_3} = {4,8,12}`;
`B_1 = 16` and `B_i = B_1 ⊕ v_{i-1}`. Qubits = the 16 points `B_1 ⊕ (L⊕V)`; this is a cap set
because `B_1 ∉ L⊕V`. Checks: the four cosets `c_i = B_i + L`, **plus** `F = {B_1,B_2,B_3,B_4}` and
`G = {B_1⊕u_1, …, B_4⊕u_1}`, both legal cosets of `V`. Since `F` and `G` are disjoint and
`F ∪ G = P_1 ∪ P_2 ∪ P_3 ∪ P_4` (the four `u_1`-pairs of `c_1…c_4`),

```
   χ_F + χ_G = χ_{P_1}+χ_{P_2}+χ_{P_3}+χ_{P_4} ∈ S_X ,
```

so `φ_{u_1}(1)+φ_{u_1}(2)+φ_{u_1}(3)+φ_{u_1}(4) = 0` is **forced**. Computed output:

```
c1..c4 only     : n=16 d_X=4 k=7 ; classes at u1 = [3, 48, 768, 12288] ; 4-term sum in S_X? False
c1..c4 + F + G  : n=16 d_X=4 k=5 ; classes at u1 = [3, 48, 768,   819] ; 4-term sum in S_X? True
                  all six pairwise equalities φ_{u1}(i)=φ_{u1}(j) : FALSE
                  all 24 orders of all 6 checks unarily safe : True
```

Neither `F` nor `G` lies on `L`, both are legal weight-4 zero-sum cosets, `d_X = 4` is certified by
the cap set, and no pairwise equality holds. So a code can impose a relation that is **not** in the
group generated by pairwise equalities, and the realizable label systems on a line are a proper
subset of Proposition 5(3)'s partition triples.

**Impact.** Proposition 5's *achievability* half ("any consistent system of such relations is
realisable") is what Theorem 1 actually uses, and that half is untouched. The refuted half is what
the document offers as the reason no *unintended* relation can creep into a built instance — which
is precisely the soundness question for the reduction. With Proposition 5(2) gone, the reduction's
correctness rests entirely on the per-instance numerical audit. That audit is real (see §4.3) but it
is not a proof, and §4.4's table entry "(i) prescribability … **HOLDS**" over-states what is
established. **Recommended relabel: Proposition 5(1) CONFIRMED; Proposition 5(2) achievability
CONJECTURED; Proposition 5(2) "only" and Proposition 5(3) REFUTED.**

Related, and unproved in the same way: **Lemma 4**'s converse ("classes in use at `u` are the
connected components of `G_u`") is argued by the phrase "with sums of checks generating the rest",
which is an assertion, not an argument — the counterexample above is exactly a merge generated by a
sum of checks that are *not* edges of `G_u`. Lemma 4's converse is used only where *more* classes
are wanted (the reduction); everywhere it is used for tractability (Theorem A, Corollaries A1/A2) an
extra merge only helps, so those are unaffected. I verified the classes directly from `λ` rather
than from Lemma 4 throughout.

### 4.2 CONFIRM: the forced relation, COPY/NEGATE, and the `Σu = 0` route-around

* `φ_1(i)+φ_2(i)+φ_3(i) = 0` is genuinely forced — it is just linearity of `τ_i` on `U_i`, i.e.
  (S1). Proposition 5(1)'s "cross 4-set" proof is a longer route to the same thing and is correct.
* The `(S2)` obstruction is real and the document's account of why the naive SAT padding fails is
  correct: two checks agreeing at two points of a line must agree at the third, so `(x ∨ ¬y ∨ z) ∧
  (x ∨ ¬y ∨ ¬z)` is not realizable on one line.
* I recomputed both gadget relations myself, over `Log = F_2^2`, `F_2^3` and `F_2^4` (i.e. with real
  larger alphabets, not just the document's symbolic `N`):
  ```
  COPY   (0,1,1)(0,2,2)(1,0,1)(1,1,0)(2,0,2) : relation on (y1,y2) = {(0,0),(1,1)}  for K=2,3,4
  NEGATE (0,0,0)(0,1,1)(1,1,0)(1,3,2)(2,0,2) : relation on (y1,y2) = {(0,1),(1,0)}  for K=2,3,4
  φ_3 = φ_1+φ_2 for every triple in both gadgets: True
  minimum #checks on one line realising either relation (exhaustive): 5
  ```
  So the gadgets do exactly what is claimed, they survive `dim Log > 2`, and 5 is minimal.
* Semantics check: `NEGATE` for a positive literal gives `¬Y_i = v`; `COPY` for a negative literal
  gives `¬Y_i = ¬v`; the clause check has labels `(0,0,0)` so it is served iff some `g(q_r)` is
  class `0`, i.e. iff `¬Y_1 ∨ ¬Y_2 ∨ ¬Y_3 = l_1 ∨ l_2 ∨ l_3`. Correct.
* One structural observation that makes the **soundness** direction (CSP YES ⟹ `ψ` SAT) robust and
  that the document does not state: every gadget check's only three points are its own line's three
  points, so adding anything to the instance can only **shrink** a gadget's relation, never enlarge
  it. Hence CSP YES forces `(y_1,y_2) ∈ {(0,0),(1,1)}` (resp. `{(0,1),(1,0)}`) at every gadget, and
  the Boolean read-off is valid — *provided* class `0 ≠` class `L1` at every named point. See §4.3.

### 4.3 CONFIRM (on all instances tested) / GAP as a general claim: connectors, and the two audits

Adding an X-check cannot hurt the distances: `H_Z` is unchanged (connectors reuse existing qubits),
so `ker H_Z` is unchanged and enlarging `S_X` only removes elements from `ker(H_Z)\S_X`, hence `d_X`
cannot drop; and enlarging `S_X` shrinks `ker H_X`, so `d_Z` cannot drop either. **CONFIRM**, with a
proof the document does not give.

Whether a connector is *free* is a different matter and is **not** enforced by `build2.py`:
`connect()` never registers its two "other" points, so nothing prevents a connector's third point
from colliding with a named point or another connector. The document says connectors' other points
"are generic and are used by nothing else"; that is an assertion about a random construction. It is
audited a posteriori by `run3.py`, and I re-audited it with my own code on **188 built codes**
(65 in the SAT/UNSAT battery, 123 in the 3-variable-subset battery): **0 violations** of "every
point that is neither named nor gadget-private carries exactly one class in use".

I then ran two audits the document does **not** run, and which are exactly what soundness needs
after Proposition 5(2) falls:

* **(L1)** within every gadget, at each of its three points, checks with equal designed label have
  equal actual class *and* checks with different designed labels have **different** actual classes;
* **(L2)** at every named point, class `0 ≠` class `L1`.

`run3.py`'s `thin-named` test is much weaker than (L2) — it only asks for `≥ 2` classes, and I
measured 3–14 classes in use at named points, so it would not have detected a `0`/`L1` merge. On
41 instances (`N ∈ {3,4,5}`, `M ≤ 12`): **0 (L1) violations, 0 (L2) violations**. So the audit
passes, but note that it is now load-bearing in a way the document does not acknowledge.

### 4.4 CONFIRM: the cap-set `d_X ≥ 4` certificate

A weight-1 vector of `ker H_Z` is a zero column; a weight-2 vector is a repeated column; a weight-3
vector is three columns summing to `0`. All three are excluded by "distinct, nonzero, cap set", so
`d(ker H_Z) ≥ 4`, hence `d_X = min\{|v| : v ∈ ker(H_Z)\S_X\} ≥ 4`. `O(n²)`, no enumeration.
**Correct**, and it is the right kind of certificate: an absence claim discharged by a complete case
split over weights `1,2,3`, not by sampling. I verified the cap-set property and the existence of a
weight-4 zero-sum 4-set outside `S_X` (so `d_X = 4` exactly) on every instance I built.

### 4.5 CONFIRM: the reduction decides 3-SAT — my own end-to-end reconstruction

I took `(H_X, H_Z)` from the proposer's builder as **data only** and decided everything myself.

*First-principles layer* (does the CSP being solved really equal the X-sector question?). On the
single-clause instance (`n = 64`, 37 X-checks) I expanded all 24 local orders of all 37 checks into
their real hook sets and tested every pair for undetectable weight-`≤2` X-logicals:

```
unarily UNSAFE orders                                : 0        (Lemma V.1(2) predicts 0)
hook mechanics vs the 2|2 value map                  : 0 mismatches / 383 616 order pairs
```

— independently reproducing the document's §5.2 figure, digit for digit, with my own code. On the
512-qubit UNSAT instance (338 checks) I repeated this on 600 randomly chosen check pairs:
**0 mismatches / 345 600 order pairs**, and universal unary safety over all 338 × 24 orders.

*Decision layer.* My own CNF encoding (variable `x_{u,χ}` = "`g(u)` is class `χ`", one 3-clause per
check, at-most-one per point) decided by Minisat22, versus my own exhaustive 3-SAT:

```
battery A: all C(8,r) subsets, r = 5..8, of the eight sign patterns on 3 variables
           93 instances (92 SAT, 1 UNSAT)                    mismatches 0
battery B: 30 random N ∈ {4,5}, M ∈ {8,…,14}                 mismatches 0
battery C: search targeted at UNSAT formulas
           40 UNSAT + 25 SAT instances                       mismatches 0
totals   : 188 codes, 41 of them NO instances; 0 mismatches, 0 audit failures,
           cap set / weight-4 / d_X = 4 verified on every one
```

The document reports 75 codes with 8 NO instances; I have 188 with 41 NO instances, decided by an
independent encoding and an external solver. This is a genuinely strong replication, and the
UNSAT-side coverage — the direction where a hidden cheat would show up — is 5× the document's.

### 4.6 GAP-AT-§4.1/§4.3: the map is not shown to be a polynomial-time (or total) reduction

Theorem 1 says "there is a **polynomial-time map** from 3-CNF formulas `ψ` to pairs `(H_X, H_Z)`".
What is exhibited is a **randomised** construction with a fixed ambient dimension and no termination
analysis:

* `T` is a constant — 30 in §4.3's "Sizes" line, 26 as `Builder`'s default. Nothing in the document
  says `T` must grow. Since the cap-set placement needs roughly `2^T ≳ n²` and `n = 64·(#clauses)`,
  the construction as specified simply stops working above a few hundred clauses. Demonstrated:
  ```
  N=6, M=8 (n = 512):  T=14 -> RuntimeError("placement failed");  T=16,18,20 -> OK
  ```
* `Builder.place` is rejection sampling with a magic bound of 200 000 tries and an explicit
  `raise RuntimeError`; `Builder.gadget` and `Builder.clause` carry `assert`s (`u3 not in
  pointset`, `q3 not in pointset`) that can fire. There is no argument that any of these succeed.
* The line points and the qubit columns are drawn from the same space with no mutual exclusion, yet
  a line point that happens to be a column destroys the cap property (`(B⊕u_i) ⊕ (B⊕u_j) = u_k`).

This is repairable and I believe cheaply: take `T = ⌈2log₂ n⌉ + O(1)`, note that each placement is
blocked by at most `4·C(n,2) + O(n)` values of `B`, and choose the least admissible `B`
deterministically. But as written, Theorem 1 establishes NP-hardness under a **randomised** map of
bounded reach, not a Karp reduction, and the document should either give the derandomisation or say
so. **GAP-AT-§4.1.**

---

## 5. Item 4 — scope honesty and the Z-sector companion

### 5.1 CONFIRM: no slide from the X-sector statement to the Eff-Preserve headline

I audited every occurrence of "NP-complete", "NP-hard" and "Eff-Preserve" in the file. Every
hardness claim carries the `^X` superscript or the words "the X-sector question": §0, §1's table,
§4.1, §7.1's table row, §7.2. §0 and §6 state plainly what is missing, §6.6-style scope clauses are
inherited correctly from the write-up, and §8's "NOT-REVIEWED" list is honest and matches what I
found. This is good discipline and I could not find a single sentence that promotes the X-sector
result to the headline problem. **CONFIRM.**

The one place where the scope discipline slips is not in the theorem but in the **repricing**: §7.2
sets `P(fixed-d NP-completeness lands) 0.35 → 0.7` "conditional on the sparsification, which I price
at 1 session and at high probability of success". That price is refuted in §5.3 below, so the 0.7 is
not supported by the evidence in the document.

### 5.2 GAP-AT-§4.1, repaired by §6(a): the promise `d(Q) = 3`

`Eff-Preserve≥^X[w ≤ 4, d_X ≥ 4]` is defined in the write-up's §6.1 with promise `d(Q) = 3`. The
constructed family has `d_X = 4` and `d_Z = 4`, hence `d = 4`: **as built, the reduction's output is
not an instance of the promise problem**, and §4.1's bullet list does not mention `d = 3` at all.
§6(a) supplies the fix (direct sum with `G_≠₃`) and marks it SETTLED, but no run of the composite is
reported anywhere, and §4.1 is never amended. Presentational, but it means Theorem 1 as stated in
§4.1 is not established by §5 alone.

I checked the fix myself, from first principles:

```
G_≠₃ (n=12) : d_X = 4, d_Z = 3, k = 2, all X-checks weight 4,
              X-logical spectrum {4:32, 6:36, 8:24, 10:4}, hypothesis (D) True,
              forbidden pairs (0,1)=3 [≠₃] and (3,4)=1 — every §5.1 number reproduced
direct sum with a reduction instance (n = 76, 42 checks):
              cross-block forbidden order pairs = 0 out of 106 560   (first principles)
              X-sector CSP: main alone True, composite True
```

So the composite has `d_X = 4`, `d_Z = 3`, `d = 3`, `k ≥ 2`, X-check weight 4, and an unchanged
X-sector answer: the promise is met and the fix is sound. **CONFIRM the repair; GAP-AT-§4.1 for
stating Theorem 1 without it.**

### 5.3 REFUTE: the Z-sector target "row weight ≤ 6, `d_Z ≥ 7`, price 1 session"

§6 says: "*Theorem A says row weight `≤ 3` is impossible … and that three classes per point need a
row of weight `≥ 6`; so `W = 6`, `d_Z ≥ 7` is the tight target for the COPY/NEGATE route … Price:
1 session. It is a construction task, not a conceptual one*". §7.3 repeats it: "the sharpest
achievable bounded-weight statement on this route is 'X-checks weight 4, Z-checks weight 6'".

**This is refuted by the document's own Theorem A.** Theorem A says `#u-pairs ≤ min\{wt(z) : z ∈
supp(u)}`. The bound "3 classes ⟹ 6 `u`-pairs" is the generic bound for *three components with one
edge each*. But a COPY/NEGATE gadget puts **five** checks `c_i = B_i + L` on one line, and the
cosets `B_i + L` are pairwise disjoint, so at the point `u_1` each `c_i` contributes **two distinct**
`u_1`-pairs, namely `{B_i, B_i⊕u_1}` and `{B_i⊕u_2, B_i⊕u_3}`. Hence

```
   #u_1-pairs ≥ 10   for every COPY/NEGATE gadget,
   so every Z-check meeting u_1 has weight ≥ 10,  i.e.  W ≥ 10 ,
```

and the document's own sufficient criterion `d_Z ≥ 2⌊W/2⌋ + 1` then demands `d_Z ≥ 11`, not 7.
Measured on the built single-clause instance (my own count):

```
point type            #u-pairs  #classes  #checks through  min wt(Z-row in supp(u))
NAMED (var/clause)      10–12      3          7–9                  22–26
gadget-private third      10       3            7                    30
aux / connector            4       1            1                    26
Z-row weights present: {22,26,30,32,34,36,38,40}
```

Worse for the plan: the count is `≥ 10` **per gadget attached to the point**, and a variable point
carries one gadget per literal occurrence, so `W` grows with the maximum number of occurrences of a
variable (bounded only by restricting to bounded-occurrence 3-SAT). The stated target is therefore
not merely optimistic, it is **impossible for the COPY/NEGATE route**, and the "1 session, standard
LDPC construction" pricing is unsupported.

The alternative two-classes-per-point (`NAE`) route fares better but not as advertised: two checks
per line give 4 `u`-pairs per line per point, so a point shared by `D` clause-lines needs
`W ≥ 4D` unless the design is changed to share `u`-pairs between lines; `D ≥ 2` is unavoidable for
any nontrivial instance, so `W = 5` is also out of reach without a new idea. And that route's
hardness rests on the question the document itself marks **OPEN** (is 2-colouring of line
hypergraphs of `PG(t−1,2)` NP-hard?).

The rest of the Z-sector plan is coherent and I confirm it: the reduced-weight bound `ρ(hook) ≤
⌊W/2⌋` is correct (take the shorter of hook and prefix), so `d_Z ≥ 2⌊W/2⌋+1` really does make every
Z-schedule safe; `W = 6 ⇒ d_Z ≥ 7` and `W = 5 ⇒ d_Z ≥ 5` are the right instantiations *of that
criterion*; and the direct-sum argument for combining a `d_Z ≥ 7` main block with `G_≠₃`'s `d_Z = 3`
block does work, because both sectors factor over a direct sum. What fails is the claim that the
COPY/NEGATE layout can be embedded with `W = 6`.

**Recommended action:** §6's third bullet and §7.3's bullet (1) should be rewritten with `W ≥ 10`
(and `W ≥ 10 × max-occurrences` for the layout as built); §7.2's `P → 0.7` should be re-derived
after that, and §7.3's "the two directions have converged" argument re-examined, since the honest
bounded-weight headline available on this route is now "X-checks weight 4, Z-checks weight ≥ 10",
which is outside 课题三's "stabilizer weight at most 4 or 6" target.

### 5.4 Minor: an unstated hypothesis in Theorem A

Theorem A's proof needs "`u`-pairs are pairwise disjoint", which needs the columns of `H_Z` to be
**distinct**. Distinct columns are guaranteed in the constructed family (cap set) but not by the
§6.1 promise: two qubits with equal columns give a weight-2 element of `ker H_Z`, which `d_X ≥ 4`
forces into `S_X` — legal for a degenerate code with a weight-2 X-stabiliser. Corollaries A1 and A2,
which are advertised as *code-intrinsic* tractable sub-islands recognisable from `H_Z` alone, inherit
this unstated hypothesis. Add "columns of `H_Z` distinct (equivalently, `S_X` has no weight-`≤2`
element)" to Theorem A. **GAP-AT-Theorem-A**, small and repairable in one line.

---

## 6. What I did not review

* Corollaries A1 and A2 beyond the hypothesis check in §5.4 — I did not re-run their random-code
  evidence or re-derive the 4-cycle "quad" argument of A2. **NOT-REVIEWED.**
* `zsector.py` / `zg2.py`: the claim that `G_≠₃`'s Z-sector is satisfiable with witness order-indices
  `[0,0,12,0,6,40,0]`, and the poly-time all-schedules-safe certificate. **NOT-REVIEWED.**
* `nae.py`'s negative search for `EQ`/`NEQ` gadgets in the Fano line hypergraph, and the open
  question it frames. **NOT-REVIEWED.**
* The imported results the target explicitly leans on and does not re-derive — Lemma 1.12,
  Lemma IV.1 (the mechanism taxonomy at `d = 3`), Proposition 2.1 (sector factorisation). My
  first-principles hook checks assume Lemma IV.1's taxonomy (hooks + data columns, budget 2).
  **NOT-REVIEWED** here; they were confirmed by the earlier islands review.
* The gadget document's wired `K₄` composite (`n = 24`). **NOT-REVIEWED**, as in the target.
* Whether the constructed family is in P for some *other* reason — irrelevant to the reduction's
  correctness, and not attempted.

## 7. Reproduction

All reviewer code is standalone Python 3, exact `F_2`, no dependency except `python-sat` for the
cross-check solver. Files (in the review scratchpad): `mine.py` (own `F_2` layer, own code class,
own first-principles hook mechanics), `mysolve.py` (own CNF encoding + own DPLL + Minisat22
cross-check + own 3-SAT brute force), `chk_formula.py` (§3.1), `chk_n8.py` (§3.2),
`chk_nontrans.py` (§3.3, includes the new `n = 12` witness), `chk_prop5.py` (§4.1 counterexample),
`chk_gadgets.py` (§4.2), `chk_labels.py` (the (L1)/(L2) audits), `chk_firstprinciples.py` (§4.5),
`chk_reduction.py` + `battery_mine.py` + `battery_unsat.py` (§4.5 batteries), `chk_promise.py`
(§5.2), `chk_thmA.py` (§5.3).

The three results a reader should reproduce first, because they are the ones that change the record:

1. `chk_nontrans.py` — an `n = 12`, `d_X = 4`, weight-4 CSS code whose `≠₃` graph is a **path**.
2. `chk_prop5.py` — an `n = 16`, `d_X = 4` code imposing a 4-term label relation with no pairwise
   equality, refuting Proposition 5(2)/(3).
3. `chk_thmA.py` — the `u`-pair counts that refute the `W = 6` Z-sector target.
