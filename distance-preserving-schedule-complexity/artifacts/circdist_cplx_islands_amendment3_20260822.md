# Amendment 3 to `circdist_cplx_islands_writeup_20260820.md`

**Node:** `CIRCDIST.cplx.islands` · **Date:** 2026-08-22 · **Role:** proposer applying frontier
task-007, the single wording correction registered by the independent Amendment-2 review
(`artifacts/circdist_amendments2_review_20260820.md` §§7.2, 8.2). The author of this amendment is
not that reviewer and does not treat the review as certification. This file is **append-only** and
changes no prior artifact. On the one point below, Amendment 3 governs Amendment 2, Amendment 1 and
the base write-up; elsewhere the existing governance order is untouched.

---

## 0. Scope, hash chain, epistemic status

This amendment does exactly one thing: it makes the statement of Proposition V.7′ multiset-valued,
propagates that convention to the direct quotations of V.7′/V.7 in the chain, exhibits the proof
step that needs repetitions, and records a scoped search for other dependencies on the set-valued
reading. **No mathematical conclusion of any island is changed, reopened, or promoted.** No new
reduction, no new theorem, no repricing.

```text
base write-up
  artifacts/circdist_cplx_islands_writeup_20260820.md
  SHA-256  af7560f28a9c9fff6bba46349f01aa7095855cff7cee4276c7186a6a54bb2f9f
  size     92234 bytes, 1431 lines

Amendment 1
  artifacts/circdist_cplx_islands_amendment1_20260820.md
  SHA-256  66ce9ac5f4b38474055137f578edd84fe3b0c075a4a076b449767ea7b05e9d60
  size     45797 bytes, 785 lines

Amendment 2  (hash-chain predecessor)
  artifacts/circdist_cplx_islands_amendment2_20260820.md
  SHA-256  33f7f5d801c941a305da062c9d38f0a9a3eef1824818d13c7f61079c2f7f348b
  size     11602 bytes, 208 lines

independent review acted on  (§7.2 wall, §8.2 reviewed_hash)
  artifacts/circdist_amendments2_review_20260820.md
  SHA-256  7b7ac0d5c78968ccf194fe176196d79d275fd82df79a3d3bb7f5666ead931842
  size     21003 bytes, 361 lines

frozen problem definitions (consulted; not modified)
  research/circdist/notes/CIRCDIST_PROBLEMS.md
  SHA-256  5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64
  size     10199 bytes, 243 lines
```

If any bound hash fails to reproduce, this amendment is void until re-derived against the changed
input. All arguments here are **CONJECTURED** proposer-side; the enumeration in §3.2 is
**NUMERICAL** with its code inline and its search space stated. Nothing is promoted to `PROVED` or
any `CERTIFIED*` status; the node stays `CONJECTURED` pending the binding review of task-007.

## 1. The correction (governing, one line)

> **In Proposition V.7′, and in every restatement of the abstract hitting problem of Theorem V.3(3),
> read "3-element lists `L_1,…,L_m ⊆ N × Log`" as "3-element multisets `L_1,…,L_m` over `N × Log`,
> repetitions allowed", with `(n,ε) ∈ L_t` meaning "the option `(n,ε)` occurs in `L_t`".**

Nothing else in Proposition V.7′ — hypotheses, gadgets, reduction, proof, or conclusion — changes.
The correction *widens* the printed problem to the witnesses its own proof already emits; the
NP-completeness conclusion is unaffected, and hardness for a wider class is not a weaker statement.
Membership in NP is likewise unaffected (`g` restricted to the `≤ 3m` used points is still a
polynomial certificate; the used-point count is an upper bound and repetitions only lower it).

## 2. Occurrence list, before → after

Every direct quotation of V.7′ / V.7 in the chain, located by file and line at the bound hashes.
Occurrences O1–O2 are the proposition itself; O3 is the deferral note that this amendment
discharges; O4–O5 are the base write-up's restatements of the same problem.

| # | file · line | before | after |
|---|---|---|---|
| O1 | `amendment1` §5.2, line 368 | *given a finite `F_2`-space `N` and 3-element lists `L_1,…,L_m ⊆ N × Log`, each satisfying (S1) …* | *given a finite `F_2`-space `N` and 3-element **multisets** `L_1,…,L_m` **over** `N × Log` (**repetitions allowed**), each satisfying (S1) …* |
| O2 | `amendment1` §5.2, line 370 | *… some `(n,ε) ∈ L_t` having `n ∈ dom(g)` and `g(n) = ε`* | *… some option `(n,ε)` **occurring in** `L_t` having `n ∈ dom(g)` and `g(n) = ε`* (multiset membership; hitting depends only on the support, so the meaning is unchanged) |
| O3 | `amendment2` §4, lines 181–183 | *The trivial focused-rereview precision note that Proposition V.7′ should say "3-element multisets over" rather than `3-element lists … subset N x Log` is outside the commissioned I1 repair and is not applied here. It remains a recorded wording issue …* | *That precision note is applied by Amendment 3 (`artifacts/circdist_cplx_islands_amendment3_20260822.md`) §1. It was outside the commissioned I1 scope of Amendment 2 and is no longer outstanding.* |
| O4 | `writeup` §6.5, lines 1256–1258 (Proposition V.7, the superseded `dim Log = 1` form) | *… choose a partial function `g : N ⇀ Log` hitting every 3-element list — is, as an abstract combinatorial problem, NP-complete* | *… hitting every 3-element **multiset** over `N × Log` — is, as an abstract combinatorial problem, NP-complete* (convention alignment only: V.7's own clause encoding emits three distinct pairs for distinct-literal 3-CNF, so V.7 does not *need* repetitions; it is superseded by V.7′ per Amendment 1 §5.4) |
| O5 | `writeup` §7.2, lines 1335–1336 | *"choose a partial section `g : N ⇀ Log` … that hits every check's 3-element list"* | *"… that hits every check's 3-element **multiset** of values"* |

Checked and **not** changed, because they already carry the multiset convention or are unaffected:

* `writeup` Lemma V.1(4), line 1096: `L_c := { x_c^{(1)},x_c^{(2)},x_c^{(3)} } ⊆ Q` is already
  glossed "*(a multiset; coincidences are possible, see (6))*" — the source of the convention.
* `writeup` Corollary V.2, line 1131, and Theorem V.3(3), lines 1158–1159: governed by V.1(4)'s
  gloss; quantification is over occurrences, and V.1(6) already declares coincident values harmless.
* `amendment1` §5.1, line 350 and `amendment2` §1.3, line 98: both already say "multiset".
* The node YAML claim string does not mention lists, so §8.2's `reviewed_hash`
  `sha256:b4325b447807dc93f9e5f96ab503cc96800dab3e3b5b8e70e0378601121d0590` is unchanged by this
  amendment. Frontier/event bookkeeping is the dispatcher's; no proof-DAG file is touched here.

## 3. The proof of V.7′ genuinely uses repetitions

### 3.1 The exact step

Amendment 1 §5.2, in the gadget table of the proof of Proposition V.7′, emits

```
  (G2)  { (π,0), (π,b), (π,b) }     0+b+b = 0   ⟹ g(π) ∈ {0,b}
  (G3)  { (p,0), (p,a), (p,a) }     0+a+a = 0   ⟹ g(p) ∈ {0,a}   for p ∈ {ν_j, ν′_j, τ_t}
```

Both repeat one option verbatim. Under the set-valued reading each collapses to a **2-element**
subset — `{(π,0),(π,b)}`, `{(p,0),(p,a)}` — which (i) is not a 3-element list as the statement
demands and (ii) fails (S1), since the two surviving labels sum to `b ≠ 0` resp. `a ≠ 0`. So under
the set reading these two lines are not legal instances at all.

They are load-bearing, not decorative. The proof's own sentences: "(G1)+(G2) ⟹ `g(π) = b`" and
"The literal `(π, 0)` is unsatisfiable because `g(π) = b`, so (G4), (G5), (G7) act as **2-clauses**";
(G3) is what makes the remaining points Boolean (`TRUE := a`, `FALSE := 0`). Delete (G2) and the
pin on `g(π)` goes, hence the 2-clause behaviour of (G4)/(G5)/(G7) goes, hence the
`(¬τ ∨ l_1 ∨ l_2) ∧ (τ ∨ l_3)` splitting no longer encodes `C_t`. Delete (G3) and points are not
Boolean. The same two gadgets carry the "what the `dim Log = 2` room buys" paragraph, which rules
out constant `g` using exactly `(G1) v ∈ {a,b,c}`, `(G2) v ∈ {0,b}`, `(G3) v ∈ {0,a}`.

By contrast (G1) `{(π,a),(π,b),(π,c)}` is a genuine 3-set, and (G4)–(G7) place their three options
at distinct points (for distinct-literal 3-CNF), so **the repetitions the proposition needs are
exactly (G2) and (G3)**.

### 3.2 NUMERICAL certificate: no set-valued list can replace (G2)/(G3)

Search space: all 3-element subsets and all 3-element multisets of `{p} × Log` for a single point
`p`, with `Log = F_2^2 = {0,a,b,c}`, `c = a+b` — i.e. all `C(4,3) = 4` subsets and all
`C(6,3) = 20` multisets of labels — retaining those with `Σ_r ε_r = 0` (S1) and recording which
label set each one constrains `g(p)` to.

```python
from itertools import combinations, combinations_with_replacement as cwr
Log = {'0':0,'a':1,'b':2,'c':3}            # F_2^2 as ints, XOR = addition
names = ['0','a','b','c']
def s1(t):
    x = 0
    for e in t: x ^= Log[e]
    return x == 0
sets_ok = sorted({tuple(sorted(set(t))) for t in combinations(names,3) if s1(t)})
mset_ok = sorted({tuple(sorted(set(t))) for t in cwr(names,3)          if s1(t)})
print(sets_ok); print(mset_ok)
G = {'G1':['a','b','c'],'G2':['0','b','b'],'G3':['0','a','a'],
     'G4':['0','a','a'],'G5':['0','0','0'],'G6':['0','a','a'],'G7':['0','a','a']}
print(all(s1(v) for v in G.values()),
      [k for k,v in G.items() if k in ('G1','G2','G3') and len(set(v)) < 3])
```

Output:

```text
S1-compliant 3-element SUBSETS  of {p} x Log, as label sets : [('a','b','c')]
S1-compliant 3-element MULTISETS over {p} x Log, label sets : [('0',), ('0','a'), ('0','b'),
                                                              ('0','c'), ('a','b','c')]
  target g(p) ∈ {0,b}   : subset-reachable = False   multiset-reachable = True
  target g(p) ∈ {0,a}   : subset-reachable = False   multiset-reachable = True
  target g(p) ∈ {a,b,c} : subset-reachable = True    multiset-reachable = True
(S1) holds for every emitted list: True | single-point lists with non-distinct pairs: ['G2','G3']
```

Reading: over `Log = F_2^2`, the **only** (S1)-compliant 3-element *subset* supported at one point
is `{a,b,c}`, i.e. (G1). The constraints `g(π) ∈ {0,b}` and `g(p) ∈ {0,a}` are unreachable by any
set-valued single-point list whatsoever, and reachable by multisets. The repetitions are therefore
forced by the mathematics, not by the drafting — which is why the correction must widen the
statement rather than rewrite the gadgets. (Scope of this absence claim: single-point, single-list,
`dim Log = 2`, (S1) only. It does not assert that *no* multi-point set-valued encoding of 3-SAT
exists; none is needed, and none is claimed.)

Amendment 1 §5.5's numerics (`[B4]`, 3 instances, 0 (S1) violations) and the reviewer's independent
rerun (5/5 vs brute-force 3-SAT, review §4.4) were run on the emitted lists, which include (G2) and
(G3); they are consistent with the multiset reading and **need no re-run** under this correction.
The line above re-verifies (S1) for all seven gadget families exactly.

## 4. Nothing else in the dossier depends on the set-valued reading

**Search scope (stated, as required for an absence claim).** Files searched, at the hashes bound in
§0: `circdist_cplx_islands_writeup_20260820.md` (1431 lines), `…_amendment1_20260820.md` (785),
`…_amendment2_20260820.md` (208), plus `research/circdist/proof-dag/nodes/CIRCDIST.cplx.islands.yaml`
read for its claim/frontier text only. Method: `grep -rn` over those files for
`3-element`, `multiset`, `N × Log`, `N x Log`, `N ⇀ Log`, `⊆ N`, `⊆ Q`, `L_c`, `L_t`, `L_1`, `∈ L`;
plus full manual reading of write-up §§6.2–6.5 and §§7.1–7.2 (lines 1080–1345), Amendment 1 §§4–5
(lines 282–460), and all of Amendment 2. **Not searched, and therefore not covered by this absence
claim:** `circdist_cplx_gadget_20260820.md`, `circdist_cplx_recon_20260820.md`,
`circdist_cplx_islandv_20260820.md`, the three review artifacts (read only at the sections cited
here), any other proof-DAG node, the scheduler, and generated views.

Within that scope, every statement quantifying over a list is a statement about *occurrences* or
about the list's *support*, and each is invariant under the change:

1. **Hypothesis (D)** (`writeup` Thm V.5, line 1216) is `L_c ∩ L_{c'} = ∅` — a *cross-list*
   condition. Multiplicities inside one list never enter; read as "no value occurs in both lists",
   the statement, the `≤ 9m²/2` pairwise test, and its cost are verbatim unchanged.
2. **Theorem V.5's matching argument** builds `B` on the *cosets* `ν(x)`, a genuine set by
   construction, and quantifies "for any `x ∈ L_c`, `x' ∈ L_{c'}`". A repeated value only lowers a
   left-degree; Hall's criterion and Hopcroft–Karp are untouched.
3. **Corollary V.2 / Theorem V.3** choose an option per check; two coincident options are simply two
   ways to make the same choice. Lemma V.1(6) already covers the coincidence case explicitly.
4. **Remark V.6 / Amendment 1 §4.2's Remark V.6′ (`K₄`)** is the one place in scope that *uses*
   three distinct values per check (`|ν(L_c)| = 3` for the four checks, giving `|N_B(S)| = 3 < 4`).
   That distinctness is an **imported property of the `K₄` instance** (gadget §5.3 data, flagged
   imported in Amendment 1 §4.3), not a consequence of how V.7′ is phrased. A multiset-valued
   general statement does not weaken an instance that happens to be set-valued.
5. **Theorem V.4 (`k ≤ 1`)** already argues over a multiset (`{ε_1,ε_2,ε_3}` with an even number of
   `ℓ`s), as quoted at Amendment 1 line 350.
6. **Definition 2.2's multiset→set passage** (a NOT-REVIEWED item in review §6 / Amendment 2 §5)
   concerns multisets of *columns/mechanisms*, a different object. It is untouched and remains open.

**The convention is forced concretely too, not only abstractly.** By Lemma V.1(5),
`x_c^{(1)}+x_c^{(2)}+x_c^{(3)} = 0` in `Q`; so if any value is `0`, the other two are *equal*, and
the realizable list literally repeats an option. Lemma V.1(6) then declares every pair involving it
harmless. Hence the set-valued reading would exclude not merely the abstract gadgets (G2)/(G3) but
also genuine degenerate Island-V lists — a second, independent reason the multiset convention is the
correct one. (Non-degenerate realizable triples, all three values nonzero, are the three nonzero
elements of a 2-dimensional subspace and are automatically distinct; the multiset convention agrees
with that case and additionally covers the degenerate one.)

## 5. Verification checklist and non-promotion

- [x] Reproduced the SHA-256 hashes and byte/line counts of the base write-up, Amendment 1,
      Amendment 2, the Amendment-2 review, and the frozen definitions before writing this file.
- [x] Applied exactly the correction demanded by review §7.2 — no more.
- [x] Listed every direct quotation of V.7′/V.7 in the chain with before/after (O1–O5) and named the
      places deliberately left unchanged, with reasons.
- [x] Located the exact proof step requiring repetitions ((G2), (G3) in Amendment 1 §5.2) and gave
      an exact enumeration showing no set-valued single-point list can replace them.
- [x] Stated the search scope of the "nothing else depends on it" claim and its exclusions.
- [x] No existing file, proof-DAG object, scheduler file, generated view, or canonical record was
      modified; this file is the only artifact written.

**NOT-REVIEWED / remaining.** Unchanged and outside this amendment: whether `(S1)+(S2)+(S3)` is in
P; whether realizable CSS instances give tractability or hardness (Island V general case, task-004);
primary-text verification of the Courcelle/ALS/Courcelle–Engelfriet theorem numbers (task-003);
Lemma 1.4's `d_ext`/mechanism bridge; Definition 2.2's multiset→set passage; the imported `K₄` data
and the three unrecomputed census families.

**No promotion.** This append-only proposer amendment supplies a checkable wording repair only. It
assigns no `PROVED`, `CERTIFIED`, `CERTIFIED-LEAN`, or other promoted status to the base write-up,
any amendment, or the `CIRCDIST.cplx.islands` node, and it is not a completion review of itself.
