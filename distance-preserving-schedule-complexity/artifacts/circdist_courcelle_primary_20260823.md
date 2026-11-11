# Primary-source verification of external theorem `C1` (Courcelle / ALS / Courcelle–Engelfriet)

**Frontier task-003** of `research/circdist/proof-dag/nodes/CIRCDIST.cplx.islands.yaml`.
Date: 2026-08-23. One budget-boxed session (box = 0.5), no sub-agents.

---

## 0. Independence statement

I am a fresh session. I did not write the islands write-up, any of its four amendments, any of the
five reviews, or the wave-11 re-adjudication. I read the Island III argument and the node record,
wrote down what the argument needs **before** retrieving anything (§1, pre-registered), and only
then went looking. I modified no canonical file; I touched no level; this file is the only thing I
wrote. My own work here is unreviewed.

Scope limit I want stated up front: I verified **citations**, not mathematics. I did not re-derive
Lemma III.1, did not check the CMSO₂ sentence `Φ_{t,w,d}` against its intended semantics, and did
not evaluate any other island. Those are explicitly *not* covered by this file.

---

## 1. Pre-registration — what Island III needs, written before retrieval

Read from `artifacts/circdist_cplx_islands_writeup_20260820.md` §4.1–4.5 and §7.4 row `C1`.

The write-up's own boxed statement (§4.4) is the thing to be verified:

> There is a computable function `f` such that: let `φ` be a CMSO₂ sentence (quantification over
> vertex sets and edge sets, plus `card_{r,p}(S) :≡ |S| ≡ r (mod p)`); let `G` be a finite graph
> with `N` vertices and edges in total, **given together with a tree decomposition of width `≤ t`**.
> Then `G ⊨ φ` is decidable in time `f(|φ|,t)·N`.

Decomposed into per-citation obligations, fixed before retrieval:

| # | Source | Statement it must supply |
|---|---|---|
| **P1** | `[Cou90]` | MSO extended by modular cardinality predicates `card_{r,p}` ("CMSO"), and: every CMSO-definable class of graphs of bounded tree-width is **recognizable** (finite-state automaton on the tree of a bounded-width decomposition). Island III needs `card_{0,2}` (`Undet`) and `card_{1,2}` (`InStab`); §4.3 argues `InStab` is *not* MSO-expressible because data-qubit degree is unbounded. So the **CMSO-over-MSO** half is load-bearing and must come from here. |
| **P2** | `[ALS91]` | The explicit **linear-time** algorithmic form: given the graph together with a tree decomposition of width `≤ t` and a fixed sentence, decide in time `f(|φ|,t)·N`; plus the counting/evaluation extension of the logic. |
| **P3** | `[CE12] Prop 5.13, p. 338` | **MSO₂** (edge-set quantification) on a graph is MSO₁ over the **incidence structure**, and the bounded-treewidth theorem applies there. This is what licenses Island III's carrier `𝔗` (universe `V ⊔ E`, relation `inc`) for the edge-set variables `E_1,…,E_w`. |

**Required input encoding:** incidence structure of the Tanner graph (universe `V ⊔ E`), *not* the
adjacency encoding; tree decomposition supplied with the input (or computed — Bodlaender is cited
separately, and is not part of `C1`).

**Pre-registered as *not* needed by Island III, to be checked at verdict time:** any
optimization / counting-*of-solutions* extension. `Φ_{t,w,d}` is a plain Boolean decision sentence
`∃E_1…∃E_w[…]`. The node's registered `C1` statement says "Courcelle's theorem **and its
optimization extension**" — flagged in advance as suspected over-registration relative to usage.

**Self-derived, therefore outside `C1`:** `tw(Inc(G)) ≤ tw(G)+1` (write-up §4.2); the sentence
`Φ_{t,w,d}` itself (§4.3, "mine, not imported"); Lemma III.1.

---

## 2. What was retrieved, and from where

Local disk first: `mdfind`/`find` over `<home>/Documents/`, including
`<home>/Documents/ChatGPT/circcert/papers/` (10 PDFs, all quantum-coding arXiv preprints)
and this repository. **No copy of any of the three texts exists on local disk** — every `mdfind` hit
for "Courcelle" was one of this project's own artifacts. Then the open web, author homepages first.

| Source | What I obtained | From |
|---|---|---|
| `[Cou90]` | **Full text**, 64 pp., scanned with an OCR text layer (extraction is noisy on symbols but clean on headers, theorem numbers and prose) | `https://www.labri.fr/perso/courcell/Textes1/MSOL01(1990).pdf` — the author's own homepage |
| `[ALS91]` | **Bibliographic record only.** No full text, no abstract | dblp record `journals/jal/ArnborgLS91`; Semantic Scholar via publisher DOI `10.1016/0196-6774(91)90006-K` |
| `[CE12]` | **Full text**, 741 PDF pp. — but of the **April 2011 authors' pre-publication version** ("to be published by Cambridge University Press"), *not* the printed 2012 CUP edition | `https://www.labri.fr/perso/courcell/Book/TheBook.pdf`, linked from the authors' book page `https://www.labri.fr/perso/courcell/TheBook.html` |

`[ALS91]` access attempts that failed: ScienceDirect article page → **HTTP 403**; `doi.org` →
redirect to `linkinghub.elsevier.com` (same wall); Semantic Scholar reports
`openAccessPdf: {status: "CLOSED"}` with the abstract elided at publisher request; targeted searches
of DiVA / CORE / CiteSeerX returned no repository copy. I did not attempt any circumvention route.

---

## 3. `[Cou90]` — B. Courcelle, *Inform. and Comput.* **85** (1990) 12–75

### 3(a) Bibliographic data — **CONFIRMED, exact**

First line of the paper, verbatim: `INFORMATION AND COMPUTATION 85, 12-75 (1990)`. Title
*"The Monadic Second-Order Logic of Graphs. I. Recognizable Sets of Finite Graphs"*; author Bruno
Courcelle, Bordeaux I University. Journal, volume, page range and year match the pin exactly.

### 3(b) Does it state what Island III needs?

**The CMSO half — YES, and the number is Definition (3.2) / Theorem (4.4).**

Definition (3.2), *"Counting monadic second-order logic"*, introduces atomic formulas
`card_{n,p}(U)` for `0 ≤ n < p, 2 ≤ p ≤ q`, with semantics given as: `card_{n,p}(U) = true iff
Card(X) = n mod p`. This is exactly the write-up's `card_{r,p}`. The same definition fixes the
terminology the main theorem uses: a set is *`ℒ`-definable* if defined without the `card` atoms, and
**definable** (unqualified) if defined *with* them — i.e. "definable" in this paper means
CMSO-definable. The paper's own abstract says so: the main theorem "is actually proved for this
extended logic."

> **(4.4) THEOREM.** Every definable subset of `FG(A)_k` is an effectively given recognizable set of
> graphs.

**The algorithmic half — also YES, which the write-up does not credit to this paper.**

> **(4.14) PROPOSITION.** Let `φ` be a formula in `CMS_{A,k,q}`. (1) Let `m ≥ k`. One can decide in
> time `O(size(e))` whether `φ` holds in the graph `val(e)` defined by a given expression `e` in
> `FE(A)^{[m]}_k`.

Its proof constructs "a deterministic bottom-up tree-automaton recognizing the set of graph
expressions `e` of width at most `m` and of type `k`, such that `val(e) ⊨ φ`", of "large but fixed
size, depending on `φ`, `k`, and `m`". That is the linear-time-given-the-decomposition statement,
in CMSO, in `[Cou90]` itself.

Also present and relevant: **Corollary (4.10)(1)** — the set of `k`-graphs of width at most `m` has
a decidable monadic theory; **Proposition (4.11)(2)** — the monadic theory of a set of graphs of
*unbounded* width is undecidable (the write-up's §4.6 "`w` and `t` must be parameters" scope clause
has a primary-source basis here).

### 3(c) Hypotheses the write-up's usage omits

1. **`[Cou90]` never says "tree-width" or "tree decomposition."** The only occurrence of the phrase
   in the entire paper is a bibliography entry (Bodlaender 1988). The paper's parameter is the
   **width of a graph expression** in the HR algebra (Definition (2.9)), and the algorithmic input
   in Prop (4.14)(1) is an **expression `e`**, not a tree decomposition. The standard equivalence
   (HR width `≤ m` ⟺ tree-width `≤ m−1`) is *not proved in, or stated by, `[Cou90]`*. So the
   write-up's boxed statement is not literally `[Cou90]`'s statement. This gap is closed elsewhere —
   see §5, `[CE12]` Theorem 6.4(1), which is stated directly in terms of `twd(G)`.
2. **Edge-set quantification is already in `[Cou90]`.** Definition (3.2) declares set variables
   "of sort `v` or `e`, denoting respectively sets of vertices or sets of edges", and the atomic
   formula `edg_a(u, u_1, …, u_k)` relates an edge object to its endpoints. The write-up outsources
   this "MSO₂ half" to `[CE12]`; on the primary text it is largely already here.
3. `[Cou90]`'s objects are directed hyperedge-labelled hypergraphs with distinguished sources
   (`FG(A)_k`), not plain graphs. Immaterial for Island III — its `𝔗` is a bipartite incidence
   structure, well inside this class — but it is a hypothesis the write-up's paraphrase drops.

### 3(d) Verdict — **VERIFIED-PRIMARY**

Full text read. Bibliographic data exact. The needed statement is present, in stronger form than
the write-up claimed, at **Definition (3.2)**, **Theorem (4.4)** and **Proposition (4.14)(1)**.
One genuine encoding caveat: the paper's parameter is HR-expression width, not tree-width (§3(c)1).

---

## 4. `[ALS91]` — Arnborg, Lagergren, Seese, *J. Algorithms* **12** (1991) 308–340

### 4(a) Bibliographic data — **CONFIRMED** by two independent indexes

dblp (`journals/jal/ArnborgLS91`) and Semantic Scholar (resolving the publisher DOI
`10.1016/0196-6774(91)90006-K`) agree: Stefan Arnborg, Jens Lagergren, Detlef Seese, *"Easy Problems
for Tree-Decomposable Graphs"*, *Journal of Algorithms* **12**(2), 308–340, 1991. Matches the pin
exactly, **including the issue number `(2)`** that the write-up supplies. dblp additionally records
the predecessor: *"Problems Easy for Tree-Decomposable Graphs (Extended Abstract)"*, ICALP 1988,
38–51, DOI `10.1007/3-540-19488-6_105`.

### 4(b) Does it state what Island III needs? — **NOT DETERMINED FROM THE PRIMARY TEXT**

I never obtained the text or even the abstract (§2). What remains unverified: the theorem number,
the exact statement of the linear-time form, and the exact statement of the EMS
(counting/evaluation) extension. I decline to assert a theorem number for this paper, and I decline
to treat search-engine summaries of its content as verification — that is exactly the secondary-
source route task-003 exists to replace.

### 4(c) The finding that makes this not matter

**`[ALS91]` is not load-bearing for `C1`.** Obligation **P2** (linear time given the decomposition)
is discharged *twice* by texts I did read in full: `[Cou90]` Proposition (4.14)(1) (§3(b)) and
`[CE12]` Theorem 6.4(1) (§5(b)). The pre-registered obligation P2 is met without `[ALS91]`. Its
counting/evaluation extension is not used by Island III at all (§6, item (d)).

### 4(d) Verdict — **VERIFIED-PARTIAL**

Bibliographic data verified against two authoritative indexes; **full text not obtained (publisher
paywall, HTTP 403 / `openAccessPdf: CLOSED`); theorem numbers not verified.** Because the citation
is corroborating rather than load-bearing, this residue does not block `C1` — but it must be
labelled honestly on the node rather than silently absorbed.

---

## 5. `[CE12]` — Courcelle & Engelfriet, EMA **138**, CUP 2012 — **the pinned locator is wrong**

### 5(a) Bibliographic data — confirmed with one gap

The authors' book page confirms: *"Graph structure and monadic second-order logic: a language-
theoretic approach"*, Bruno Courcelle and Joost Engelfriet, Cambridge University Press, **June 2012**,
728 pages, 9 chapters plus a preface by Maurice Nivat. The PDF I read is the **April 2011 authors'
version**; its title page reads "to be published by Cambridge University Press" and **does not carry
the series designation**. So *"Encyclopedia of Mathematics and its Applications 138"* is **not
verified from the primary text** — it remains secondary-source data, as does the exact print
pagination. All locators below are to the April 2011 draft. Numbering appears stable (see 5(b)).

### 5(b) Does Proposition 5.13 say what the write-up uses? — **NO. It says nearly the opposite.**

Chapter 5 ("Monadic second-order logic"), statement head on draft p. 337, items on draft p. 338,
verbatim:

> **Proposition 5.13** The following properties are not MS-expressible:
> (1) Two sets `X` and `Y` have equal cardinality.
> (2) A simple graph is Hamiltonian, or has a perfect matching.
> (3) In a simple directed graph, a set of vertices `X` is that of a directed path from `x` to `y`.
> (4) A simple graph has a nontrivial automorphism.

This is a **negative, inexpressibility result about MS₁** — proved by reduction to the
non-regularity of the language of words with equally many `a`s and `b`s. The write-up cites it for
"the **MSO₂** half: quantification over edge sets is MSO₁ over the incidence structure, and the
bounded-treewidth theorem applies there." Proposition 5.13 asserts no such thing; it contains no
incidence structure, no tree-width, and no algorithm.

Its actual role in the book is as the **motivation** for edge-set quantification. §5.2.5, "Edge set
quantifications", opens by observing that the vertex-only representation "allows neither to express
graph properties that depend on the multiplicity of edges nor certain properties of simple graphs of
the form 'there exists a set of edges such that…' like the property of being Hamiltonian or of
having a perfect matching, **see Proposition 5.13**." So the pinned pointer is the book's
*forward-reference to the motivation*, mistaken for the theorem it motivates.

**Note the failure mode.** The pin `Proposition 5.13, p. 338` is **internally self-consistent** —
5.13 really does sit at pp. 337–338. A page-level or existence-level check would have *passed*. Only
reading the statement catches it. This is precisely the defect class that secondary-source
verification cannot detect, and it is the one task-003 was opened to find.

### 5(c) The correct citations, in the same book

All three obligations are met by `[CE12]`, just not at 5.13:

* **Incidence structure (P3, first half) — Definition 5.17** ("Representation by incidence graphs"),
  draft p. 345: for undirected `G`, `Inc(G)` is the simple directed bipartite graph with vertex set
  `V_G ∪ E_G` and edges `e → v` for every `e ∈ E_G` and `v ∈ V_G` such that `v` is an end vertex of
  `e`; `⌈G⌉ := ⌊Inc(G)⌋ = ⟨V_G ∪ E_G, in_G⟩`. This *is* Island III's `𝔗` (§4.2), modulo the unary
  predicates `Data`/`ChkX`/`ChkZ`, which are vertex labels — accommodated by the book's `(K,Λ)`
  labelling throughout. MS₂ is defined as MS over `⌈G⌉`: "the index 2 recalls that there are two
  types of elements in the domain of `⌈G⌉`, vertices and edges."
* **Recognizability (P1, algebraic form) — Theorem 5.68(2)** ("Recognizability Theorem for graph
  algebras"), draft p. 397: *"Every `CMS₂`-definable set of (labelled) `s`-graphs is effectively
  HR-recognizable."* (HR = the tree-width algebra; part (1) is the CMS/clique-width analogue.)
* **The statement Island III actually needs (P2 + P3) — Theorem 6.4(1)**, draft p. 429, in §6.1
  "Fixed-parameter tractable algorithms for model-checking": *"For all finite sets `K` and `Λ` of
  vertex and edge labels, the model-checking problem `MC(JS[K,Λ][∅], CMS₂)` is fixed-parameter
  linear with respect to `(twd(G), φ)`, where `G` is the input graph and `φ` is the input
  sentence."* The term-level version is **Theorem 6.3(2)**, draft p. 428.

### 5(d) Hypotheses the write-up's usage omits — and one place it is safely conservative

* **Tree decomposition supplied vs computable.** The write-up's boxed statement *requires* the
  decomposition to be given. `[CE12]` Theorem 6.4(1) does **not**: it parameterizes by `twd(G)` and
  computes an optimal decomposition internally (its proof invokes Theorem 1.25 for the
  decomposition and Theorem 2.83 to convert it into an HR term). So the write-up assumes **less**
  than the literature grants. That is conservative, hence safe; and Theorem III's two-case
  bookkeeping ("if a width-`t` decomposition is supplied … otherwise Bodlaender") is licensed either
  way. It does mean the separately-cited Bodlaender results are, strictly, redundant.
* **CMSO₂/tree-width vs CMSO₁/clique-width pairing — correctly matched.** Island III genuinely needs
  edge-set variables (`E_1,…,E_w`), i.e. CMS₂, and pairs them with tree-width. `[CE12]` 6.4(1) is
  exactly that pairing and is *linear*. Had the argument used 6.4(2) (CMS with clique-width) the
  bound would be *cubic* and the logic too weak. The write-up does not make that error.
* **`tw(Inc(G)) ≤ tw(G)+1`.** Proved by the write-up itself (§4.2). Against 6.4(1) it is not even
  needed, since 6.4(1) is already stated for `⌈G⌉` with parameter `twd(G)`. Harmless surplus.

### 5(e) Verdict — **MISMATCH**

The pinned locator (Prop 5.13, p. 338) does not state the theorem the write-up uses; it states a
negative result of the opposite polarity. **Correct citations found and quoted:** Theorem 6.4(1)
(draft p. 429) for the FPT statement, Theorem 5.68(2) (draft p. 397) for recognizability, and
Definition 5.17 (draft p. 345) for the incidence representation. Residue: the series number
(EMA 138) and the printed pagination are still secondary-source only, since I read the 2011 draft.

---

## 6. Overall ruling on assumption `C1`

**The mathematics is sound and is now primary-source verified, twice over and independently.** The
proposition Island III relies on — *CMSO₂-definable properties are decidable in FPT-linear time on
structures of bounded tree-width* — is true, is what the primary sources say, and is established by
two disjoint chains I read in full:

* `[Cou90]` Definition (3.2) + Theorem (4.4) + Proposition (4.14)(1); and
* `[CE12]` Definition 5.17 + Theorem 5.68(2) + Theorem 6.4(1).

Island III's usage is *conservative* relative to both (§5(d)). I found **no mathematical defect** in
what the write-up assumes.

**But `C1` as currently registered does not yet qualify as an ESTABLISHED external theorem under
`DAG_PROTOCOL` §2**, which requires that "Every assumption records its exact statement and scope
together with a **locatable source**". One of the three pinned locators points at a proposition that
says the opposite kind of thing (§5(b)), and the registered statement over-describes the theorem
(item (d) below). That is a defect of the registration, not of the argument.

**What must change for `C1` to qualify** — four edits, all citation hygiene, none touching a line of
Island III's mathematics:

| | Edit |
|---|---|
| (a) | **Replace** `Courcelle-Engelfriet, EMA 138 (CUP 2012) Prop 5.13` with **`Theorem 6.4(1)`** (FPT-linear CMS₂ model-checking parameterized by tree-width), optionally citing **Theorem 5.68(2)** for recognizability and **Definition 5.17** for the incidence representation. Record that the series number EMA 138 and the print pagination remain secondary-source data. |
| (b) | **Add the `[Cou90]` theorem numbers:** Definition (3.2) for `card_{n,p}`, **Theorem (4.4)**, **Proposition (4.14)(1)**. Record that `[Cou90]` states its bound in terms of HR-expression width, not tree-width. |
| (c) | **Demote `[ALS91]`** to a corroborating citation marked *bibliographic data verified, full text paywalled, theorem numbers unverified* — or drop it, since it is not load-bearing (§4(c)). |
| (d) | **Strike "and its optimization extension"** from the registered statement. Island III uses no optimization and no counting *of solutions*; `Φ_{t,w,d}` is a plain Boolean sentence. The "counting" in CMSO is modular cardinality predicates — a different thing, and the one that *is* used. As registered, `C1` claims more than the argument needs, which is its own §2 scope defect. |

The parallel §4.4 text in the write-up carries the same three defects and warrants the same
correction; it is an append-only dossier, so this would be an amendment, not an edit in place.

---

## 7. What this verdict licenses — and what it does not

I changed no level and touched no canonical file. Stating plainly what follows:

1. **The task-003 caveat can be discharged once edits (a)–(d) land and are bound** by whatever
   review the protocol requires for an assumption edit. The substance the caveat was worried about —
   "are these theorems real and do they say this?" — is now answered: two of the three are read in
   full and say it; the third is paywalled but redundant. The one surprise (§5(b)) is a wrong
   pointer, cheaply fixed, with the right pointer supplied.
2. **This does not by itself promote the node.** Per the wave-11 adjudication
   `artifacts/circdist_readjudication_20260823.md` §11 item 3, the adjudicator recorded that they did
   not re-derive islands I–V, that their verdict "turns on one unverified external theorem citation",
   and that — quoting the section the task asked me to restate — *"If a session reads the primary
   texts and the numbers check out, the remaining question is whether the rest of the dossier (which
   no single hash-bound review has attacked end to end — the clearing review is focused, and the base
   review is not linked with a hash) meets the bar; I express no view on that."*
   So the next gate for `PROVED` is an **end-to-end, hash-bound claim-level review of the islands
   dossier**. That is now the binding constraint, not `C1`.
3. **The other caveats are untouched by this file** — the §4.6 items (unrecomputed census families,
   the unreviewed NO side of Theorem V.5, the shared model design), the Island V scope clause, the
   HGP non-degeneracy proviso, and reviewer note N3 all stand exactly as recorded. Nothing here
   speaks to them.

---

## 8. Surprises worth the lead's attention

1. **The `[CE12]` pin is a genuine mismatch, and it is the exact defect class that secondary-source
   verification is blind to.** Number and page are mutually consistent — 5.13 really is at
   pp. 337–338 — so any check short of reading the statement passes it. The pointer that was pinned
   is the book's cross-reference *to the motivation for* edge-set quantification, not the theorem.
2. **The three-way division of labour in §4.4 is wrong in two of its three places.** `[Cou90]`
   already contains the linear-time algorithmic form (Prop (4.14)(1)) that the write-up attributes
   to `[ALS91]`, and already has edge-set quantification (Def (3.2), set variables of sort `e`) that
   the write-up attributes to `[CE12]`. The citations are individually real; the story about who
   supplies what is not.
3. **`[Cou90]` never uses the words "tree-width" or "tree decomposition"** — the sole occurrence in
   the paper is a bibliography entry. The bridge from HR-expression width to tree-width is standard,
   but it is *not* in the paper the node pins for it.
4. **`[ALS91]` turns out not to be load-bearing at all** — which is fortunate, since it is the one
   text I could not get behind. Had the argument actually depended on it, task-003 would have closed
   at VERIFIED-PARTIAL rather than clearing.
5. **The registered statement of `C1` is broader than the argument's usage** ("optimization
   extension"). Over-registration is its own §2 problem and is easy to miss, because it makes the
   assumption look *more* standard rather than less.

---

## 9. Limitations of this verification

* **`[ALS91]`: no primary text.** Bibliographic data only, from two indexes. Not read.
* **`[CE12]`: I read the April 2011 authors' draft, not the printed 2012 CUP edition.** Theorem
  numbers, statements and page locators above are the draft's. The published numbering is very
  likely identical (the draft's own p. 338 matches the pinned page, which is evidence of stable
  pagination), but I did not verify a single number against the print edition, and the series
  designation EMA 138 does not appear in the draft at all.
* **`[Cou90]`: OCR text layer.** Prose, headers and theorem numbers extract cleanly; mathematical
  symbols are frequently mangled. Every quotation above is from a passage where the surrounding
  prose was unambiguous, but I did not read the rendered page images.
* **No mathematics was checked.** Lemma III.1, the sentence `Φ_{t,w,d}`, and the claim that
  `InStab` is not MSO-expressible are all outside this file's scope. In particular I did **not**
  verify that `Φ_{t,w,d}` is a well-formed CMS₂ sentence over `⌈𝔗⌉` in `[CE12]`'s exact signature —
  that is a modelling question, and it belongs to the end-to-end review of §7 item 2.
* **Bodlaender (1996) and Bodlaender et al. (2016), and Frick–Grohe (`C3`), were not verified.**
  Frick–Grohe is not load-bearing (it supports a scope clause, not a theorem); Bodlaender is
  redundant against `[CE12]` 6.4(1) (§5(d)) but is still cited in Theorem III's second time bound.
* **This file is unreviewed.**
