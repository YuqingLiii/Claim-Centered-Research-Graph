# Amendment 4 to `circdist_cplx_islands_writeup_20260820.md`

**Node:** `CIRCDIST.cplx.islands` · **Date:** 2026-08-22 · **Role:** Opus 5 executor, amendment
author applying the two repairs registered by the independent focused review of Amendment 3
(`artifacts/circdist_islands_amendment3_review_20260822.md` §8, items D1 and D2), plus its two
optional-polish items D3 and D4. **Box:** one session, stop-loss binding. No sub-agents. This file
is **append-only** and changes no prior artifact. **On the points below, Amendment 4 governs
Amendment 3, Amendment 2, Amendment 1 and the base write-up; elsewhere the existing governance
order is untouched.**

**Epistemic ceiling.** Nothing here is labelled PROVED or `CERTIFIED*`. Everything is
**CONJECTURED** proposer-side except §1's enumeration, which is **NUMERICAL** with its code inline,
its stdout reproduced, and its search space stated. **No mathematical conclusion of any island is
changed, reopened, or promoted**; the multiset correction of Amendment 3 §1 stands exactly as
written. The review is treated as **data in a file**, not as certification of anything.

---

## 0. Hash chain

```text
amended predecessor
  artifacts/circdist_cplx_islands_amendment3_20260822.md
  SHA-256  f2bcf171605e4a5b9838e8b331d8d44b0ae6ec2bb35b712bd06842c54397c81f
  size     15914 bytes, 230 lines

commissioning review (data, not certification)
  artifacts/circdist_islands_amendment3_review_20260822.md
  SHA-256  73114d889d92855afdfa15c3e91868cca1c52cb53ab45b347247cae3061d7cf6
  size     18444 bytes, 284 lines

review whose edits 9 and 11 are restored below (quoted, §2)
  artifacts/circdist_islands_review_20260820.md
  SHA-256  cc3fc85c9c494995c33d89b9b69bd7d28d1ab203182c1ce50ab9710285e7ad1c
  size     61372 bytes, 1042 lines

dossier under amendment (unchanged bytes, re-verified this session)
  artifacts/circdist_cplx_islands_writeup_20260820.md
  SHA-256  af7560f28a9c9fff6bba46349f01aa7095855cff7cee4276c7186a6a54bb2f9f   92234 B, 1431 L
  artifacts/circdist_cplx_islands_amendment1_20260820.md
  SHA-256  66ce9ac5f4b38474055137f578edd84fe3b0c075a4a076b449767ea7b05e9d60   45797 B,  785 L
  artifacts/circdist_cplx_islands_amendment2_20260820.md
  SHA-256  33f7f5d801c941a305da062c9d38f0a9a3eef1824818d13c7f61079c2f7f348b   11602 B,  208 L

frozen problem definitions (consulted; not modified)
  research/circdist/notes/CIRCDIST_PROBLEMS.md
  SHA-256  5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64
```

All seven digests were recomputed from current bytes with `shasum -a 256` before this file was
written; the first five reproduce the values Amendment 3 §0 and the review §1 assert. **If any bound
hash fails to reproduce, this amendment is void until re-derived against the changed input.** The
node YAML `reviewed_hash` `sha256:b4325b447807dc93f9e5f96ab503cc96800dab3e3b5b8e70e0378601121d0590`
is unaffected by this amendment: no claim text is touched here, and no proof-DAG file is written.

---

## 1. D1 — §3.2's "Output" block is replaced by genuine reproduced stdout

### 1.1 The defect, stated exactly

The review's D1 is a **printed-derivation** finding, not a value finding, and the distinction is
carried here: *every value in Amendment 3 §3.2 is true*, and the reviewer reproduced all of them
with independent point-labelled code. What was wrong is what the block claimed to be:

1. The snippet contains three `print` statements. They emit the subset list, the multiset-support
   list, and one line `True ['G2', 'G3']`. They do **not** emit the prose labels
   ("`S1-compliant 3-element SUBSETS of {p} x Log, as label sets :`" etc.), and they do **not**
   compute or print the three `target g(p) ∈ … : subset-reachable = … multiset-reachable = …` lines
   at all. Those three lines are narration, presented under an "Output:" heading inside a block
   headed **NUMERICAL certificate**.
2. The `G` dict stores **labels only**, so under `len(set(v)) < 3` the families `G4`, `G6`, `G7`
   also qualify; the answer `['G2','G3']` survives only because the comprehension hard-codes
   `k in ('G1','G2','G3')`. The single-point restriction — which *is* the entire content of the
   "exactly (G2) and (G3)" claim — was therefore **assumed by a name filter, not computed**.

### 1.2 The replacement (governing): Amendment 3 §3.2's code block and Output block are superseded

The block below replaces Amendment 3 §3.2's snippet and its "Output:" text in their entirety. It
indexes every option as a `(point, label)` pair, computes the reachability table instead of
narrating it, and derives the two repetition-bearing families **structurally** — as the gadgets that
are single-point *and* carry a repeated `(point, label)` option — with no name filter anywhere. It
was written for this amendment and run; what follows the code is its **actual stdout**, pasted
unedited.

```python
"""V.7' single-point enumeration, options indexed as (point, label) pairs.

Log = F_2^2 = {0,a,b,c}, c = a+b, addition = XOR on {0,1,2,3}.
(S1) is the condition sum_r eps_r = 0.
Everything printed below is computed; no value is narrated.
"""
from itertools import combinations, combinations_with_replacement as cwr

LOG = {'0': 0, 'a': 1, 'b': 2, 'c': 3}
NAMES = ['0', 'a', 'b', 'c']


def s1(options):
    """(S1): the labels of the three options sum to 0 in Log."""
    x = 0
    for (_pt, lab) in options:
        x ^= LOG[lab]
    return x == 0


def constraint(options):
    """The set of labels a hitting g may take at the (single) point of `options`."""
    return tuple(sorted({lab for (_pt, lab) in options}, key=NAMES.index))


# ---- single-point search space, options carried as (point, label) pairs ----
P = 'p'
opts = [(P, lab) for lab in NAMES]                       # the 4 options at point p

subsets = [t for t in combinations(opts, 3) if s1(t)]           # C(4,3) = 4 candidates
multisets = [t for t in cwr(opts, 3) if s1(t)]                  # C(6,3) = 20 candidates

sub_reach = sorted({constraint(t) for t in subsets})
mset_reach = sorted({constraint(t) for t in multisets})

print("search space : %d 3-element subsets, %d 3-element multisets of {p} x Log"
      % (len(list(combinations(opts, 3))), len(list(cwr(opts, 3)))))
print("(S1)-compliant: %d subsets, %d multisets" % (len(subsets), len(multisets)))
print("S1-compliant 3-element SUBSETS   of {p} x Log, as label sets : %s" % (sub_reach,))
print("S1-compliant 3-element MULTISETS over {p} x Log, label sets  : %s" % (mset_reach,))
print()

for target in [('0', 'b'), ('0', 'a'), ('a', 'b', 'c')]:
    print("  target g(p) in {%s} : subset-reachable = %-5s  multiset-reachable = %s"
          % (",".join(target), target in sub_reach, target in mset_reach))
print()

# ---- the seven emitted gadget families, as (point, label) options ----
G = {
    'G1': [('pi', 'a'), ('pi', 'b'), ('pi', 'c')],
    'G2': [('pi', '0'), ('pi', 'b'), ('pi', 'b')],
    'G3': [('p',  '0'), ('p',  'a'), ('p',  'a')],
    'G4': [('pi', '0'), ('nu_j', 'a'), ("nu'_j", 'a')],
    'G5': [('pi', '0'), ('nu_j', '0'), ("nu'_j", '0')],
    'G6': [('tau_t', '0'), ('p_1', 'a'), ('p_2', 'a')],
    'G7': [('pi', '0'), ('tau_t', 'a'), ('p_3', 'a')],
}

single_point = [k for k, v in G.items() if len({pt for pt, _ in v}) == 1]
repeated_pair = [k for k, v in G.items() if len(set(v)) < 3]
print("(S1) holds for every emitted gadget : %s" % all(s1(v) for v in G.values()))
print("single-point gadgets               : %s" % single_point)
print("gadgets with a repeated (point,label) option : %s" % repeated_pair)
print("=> repetitions are needed exactly at : %s"
      % sorted(set(single_point) & set(repeated_pair)))
print()
for k in sorted(G):
    v = G[k]
    pts = sorted({pt for pt, _ in v})
    line = "  %-3s %-46s S1=%s  points=%d  distinct options=%d" % (
        k, "{" + ", ".join("(%s,%s)" % o for o in v) + "}",
        s1(v), len(pts), len(set(v)))
    if len({pt for pt, _ in v}) == 1:
        line += "  constrains g(%s) in {%s}" % (pts[0], ",".join(constraint(v)))
    print(line)
```

Output (verbatim stdout of the block above, `python3 v7prime_pointlabel.py`):

```text
search space : 4 3-element subsets, 20 3-element multisets of {p} x Log
(S1)-compliant: 1 subsets, 5 multisets
S1-compliant 3-element SUBSETS   of {p} x Log, as label sets : [('a', 'b', 'c')]
S1-compliant 3-element MULTISETS over {p} x Log, label sets  : [('0',), ('0', 'a'), ('0', 'b'), ('0', 'c'), ('a', 'b', 'c')]

  target g(p) in {0,b} : subset-reachable = False  multiset-reachable = True
  target g(p) in {0,a} : subset-reachable = False  multiset-reachable = True
  target g(p) in {a,b,c} : subset-reachable = True   multiset-reachable = True

(S1) holds for every emitted gadget : True
single-point gadgets               : ['G1', 'G2', 'G3']
gadgets with a repeated (point,label) option : ['G2', 'G3']
=> repetitions are needed exactly at : ['G2', 'G3']

  G1  {(pi,a), (pi,b), (pi,c)}                       S1=True  points=1  distinct options=3  constrains g(pi) in {a,b,c}
  G2  {(pi,0), (pi,b), (pi,b)}                       S1=True  points=1  distinct options=2  constrains g(pi) in {0,b}
  G3  {(p,0), (p,a), (p,a)}                          S1=True  points=1  distinct options=2  constrains g(p) in {0,a}
  G4  {(pi,0), (nu_j,a), (nu'_j,a)}                  S1=True  points=3  distinct options=3
  G5  {(pi,0), (nu_j,0), (nu'_j,0)}                  S1=True  points=3  distinct options=3
  G6  {(tau_t,0), (p_1,a), (p_2,a)}                  S1=True  points=3  distinct options=3
  G7  {(pi,0), (tau_t,a), (p_3,a)}                   S1=True  points=3  distinct options=3
```

### 1.3 Reading, and what changed versus what did not

* **Values: unchanged, and now computed.** Over `Log = F₂²` the only (S1)-compliant 3-element
  *subset* supported at one point is `{a,b,c}`, i.e. (G1); the constraints `g(π) ∈ {0,b}` and
  `g(p) ∈ {0,a}` are unreachable by any set-valued single-point list whatsoever and reachable by
  multisets. The counting is unchanged (`C(4,3) = 4` subsets, `C(6,3) = 20` multisets, of which
  `1` and `5` satisfy (S1)). The conclusion is unchanged: the repetitions are forced by the
  mathematics, not by the drafting, which is why Amendment 3 §1's correction had to *widen the
  statement* rather than rewrite the gadgets.
* **Derivation: repaired.** `['G2','G3']` now falls out of `single_point ∩ repeated_pair` computed
  over `(point, label)` options. The per-gadget table at the end prints, for each of the seven
  families, whether (S1) holds, how many distinct points it touches, how many distinct options it
  carries, and — for the single-point ones — which label set it constrains `g` to. (G4)–(G7) touch
  three distinct points each and carry three distinct options each, which is the fact the old name
  filter was standing in for; it is now the output of a computation.
* **Scope of this absence claim, unchanged and restated:** single point, single list,
  `dim Log = 2`, (S1) only. It does **not** assert that no multi-point set-valued encoding of 3-SAT
  exists; none is needed and none is claimed. The `distinct-literal 3-CNF` scoping of "(G4)–(G7)
  place their three options at distinct points" is likewise unchanged and is still necessary — for
  a clause with a repeated literal, (G6) would itself repeat an option.
* Amendment 1 §5.5's numerics (`[B4]`, 3 instances, 0 (S1) violations) and the reviewer's
  independent rerun (5/5 against brute-force 3-SAT) were run on the emitted lists, which include
  (G2) and (G3); they remain consistent with the multiset reading and **need no re-run**. The block
  above re-verifies (S1) for all seven gadget families exactly, as a computed value.

---

## 2. D2 — islands review edits 9 and 11 are restored to the remaining-items roll-up

Amendment 3 §5's closing paragraph is the section whose job is to state what remains, and it dropped
two items that Amendment 1 §8 item 5 recorded as *legitimate and left open*, that Amendment 2 §5
explicitly carried forward, and that focused-rereview §6 item 7 lists as NOT-REVIEWED. Neither has
been withdrawn or discharged by anyone. They are restored here, **quoted verbatim** from
`artifacts/circdist_islands_review_20260820.md` §9 ("Recommended edits, in order of severity"), at
the hash bound in §0:

> **9. Theorem II.4 / Lemma II.5** — record that Lemma II.5's hypothesis is poly-time checkable
> while Theorem II.4's is not; the poly-time-recognisable constant-YES class is the former.

> **11. §6.1** — exhibit one code satisfying the promise verbatim (weight-4 X-checks, `d_X ≥ 4`,
> `d_Z = 3`), or relax the stated promise to what the proofs use (`d_X ≥ 4`, X-weight `≤ 4`).

**Why each matters at promotion, stated without overstating.**

* **Edit 9 bears on the HGP clause of the node claim.** The contrast it asks to be recorded is the
  operative one for a tractability statement: a class is *poly-time recognisable* only if its
  defining hypothesis is poly-time checkable, and only Lemma II.5's is. The write-up never draws the
  contrast. This is a presentational repair with claim-level reach; it is **unapplied**, and it is
  not applied here (this amendment commissions no new mathematics), so it rides forward as an open
  item.
* **Edit 11 is a non-vacuity bar on Island V, whose `k ≤ 1` clause is in the claim.** It asks for
  **one** code satisfying §6.1's promise *as literally written* — weight-4 X-checks, `d_X ≥ 4`,
  `d_Z = 3` — or for the promise to be relaxed to what the proofs actually use (`d_X ≥ 4`, X-weight
  `≤ 4`). **It is unsatisfied, and the evidence about it is absence evidence with a stated scope**:
  the islands review reports that in **roughly `10^6` random draws it found no CSS code with
  weight-4 X-checks, `d_X ≥ 4` and `d_Z = 3`; every hit had `d_Z ∈ {1,2}`**. That is exactly what
  it is and no more —
  * it is a **random-sampling absence result over an unstated distribution**, not a proof of
    emptiness, and under this project's evidence-asymmetry rule it may be used only at low
    confidence;
  * the review itself says so, and adds that the `K₄` code presumably satisfies §6.1 verbatim, so
    the bar may well be clearable by exhibiting a single known instance rather than by searching;
  * this session ran **no** code search of its own and expresses **no** view on whether §6.1's
    promise is satisfiable. Neither did the Amendment-3 reviewer, who records the same abstention.

  What follows for the record is only this: **§6.1's promise is currently un-witnessed**, the
  cheapest discharge is one exhibited instance (or the relaxation the edit offers as its
  alternative), and until one or the other happens the promise "risks being much narrower than its
  content" — the islands review's own words for the risk.

### 2.1 The remaining-items roll-up, complete

This list supersedes Amendment 3 §5's "NOT-REVIEWED / remaining" paragraph. It is the union of that
paragraph's six items with the two restored above; nothing is dropped and nothing new is added.

| # | item | status | source |
|---|---|---|---|
| 1 | whether the abstract `(S1)+(S2)+(S3)` problem is in P | open | Amdt. 3 §5; rereview §6 |
| 2 | Island V general case — whether realizable CSS instances give tractability or hardness | open, frontier `task-004` | Amdt. 3 §5 |
| 3 | primary-text verification of the Courcelle / ALS / Courcelle–Engelfriet theorem numbers | open, frontier `task-003`; blocks `PROVED`, not `CERTIFIED*` | Amdt. 3 §5 |
| 4 | Lemma 1.4's `d_ext` / mechanism bridge | open | Amdt. 3 §5 |
| 5 | Definition 2.2's multiset→set passage (multisets of *columns/mechanisms* — a different object from V.7′'s lists) | open, NOT-REVIEWED | Amdt. 3 §4 item 6, §5 |
| 6 | the imported `K₄` gadget data and the three unrecomputed five-family census members | open, imported / NOT-REVIEWED | Amdt. 3 §5 |
| **7** | **islands review edit 9** — record that Lemma II.5's hypothesis is poly-time checkable while Theorem II.4's is not; the poly-time-recognisable constant-YES class is the Lemma II.5 one | **unapplied, legitimate, left open** — bears on the HGP clause of the node claim | islands review §9 item 9; Amdt. 1 §8 item 5; Amdt. 2 §5 |
| **8** | **islands review edit 11** — exhibit one code meeting §6.1's promise verbatim (weight-4 X-checks, `d_X ≥ 4`, `d_Z = 3`), or relax the promise to `d_X ≥ 4`, X-weight `≤ 4` | **unapplied; non-vacuity bar on Island V, currently un-witnessed.** Absence evidence only: ~`10^6` random draws, no hit, every hit had `d_Z ∈ {1,2}` — low confidence, unstated distribution, no proof of emptiness | islands review §4.6 and §9 item 11; Amdt. 1 §8 item 5; Amdt. 2 §5 |

**Consequence for a promotion, stated plainly and without recommending one.** Whatever caveat set
rides along if the dispatcher promotes this node must contain rows 1–8 above. The Amendment-3
review's own summary is that once D1 and D2 are amended it sees no remaining *recorded defect*
blocking a `CERTIFIED*`-level promotion **on the current claim, with the caveat set of
`circdist_amendments2_review_20260820.md` §7.2 plus edits 9 and 11**, and that `PROVED` remains out
of reach on `task-003` alone. That is the reviewer's assessment, recorded here as data; this
amendment promotes nothing and is not a completion review of itself.

---

## 3. D3 and D4 — the two polish items, both applied in one line each

The review filed D3 and D4 as optional polish that "should not by themselves hold anything". Both
are one-line fixes, so both are applied rather than carried.

### 3.1 D3(a) — the missing occurrence row: `writeup` line 1263–1264, **inside V.7's own proof**

Amendment 3 §2's table header promises "every direct quotation of V.7′ / V.7 in the chain". It is
complete for *statement* quotations; a restatement of the same hitting problem four lines below the
O4 line still reads "list", so the amended V.7 currently reads **statement = multiset / proof =
list**. One more row closes it:

| # | file · line | before | after |
|---|---|---|---|
| **O6** | `writeup` §6.5, lines 1263–1264 (inside the *proof* of Proposition V.7) | *…encode clause `C_t` as the **list** `L_t` of the three pairs of its literals. Then a partial function `g : N ⇀ Log` hitting every **list** is exactly a partial truth assignment satisfying every clause…* | *…encode clause `C_t` as the **multiset** `L_t` of the three pairs of its literals. Then a partial function `g : N ⇀ Log` hitting every **multiset** is exactly a partial truth assignment satisfying every clause…* |

Convention alignment only, and harmless on its own terms: V.7's `dim Log = 1` encoding emits three
*distinct* pairs for distinct-literal 3-CNF, so V.7 does not need repetitions, and V.7 is superseded
by V.7′ (Amendment 1 §5.4). The other restatements the reviewer classified as "not itemized but
substantively harmless" (`amendment1` 314, 320, 351, 427; `amendment2` §§2–3 passim) remain governed
by Amendment 3 §1's blanket clause, as the review agreed they may be.

### 3.2 D3(b) — a correction of a review, flagged as one

Amendment 3 §3.1's "**the repetitions the proposition needs are exactly (G2) and (G3)**" tacitly
corrects the focused rereview `artifacts/circdist_amendments_review_20260820.md` §4.4, which had
written that "(G2), (G3), (G4)-style lists emit repeated options, i.e. **multisets**". Per this
repository's practice a correction of a review is flagged rather than made silently, so:

> **Flagged correction.** Focused-rereview §4.4's list "(G2), (G3), (G4)-style" is **too wide**.
> (G4)-style families repeat a *label*, not an *option*: (G4) `{(π,0), (ν_j,a), (ν′_j,a)}` places
> its three options at three **distinct points**, so as a set of `(point, label)` pairs it has three
> distinct elements and is a genuine 3-set. Only (G2) and (G3) repeat an `(point, label)` option.
> The §4.4 *conclusion* — that `⊆` should read "3-element multisets over", because the multiset
> structure is load-bearing and (G2) cannot be written with three distinct options — is **correct
> and unaffected**; it is the enumeration of which families are involved that was loose. §1.2 above
> computes the distinction rather than asserting it.

### 3.3 D4 — §1's framing clause

Amendment 3 §1 says the correction "*widens* the printed problem to the witnesses its own proof
already emits" and that "the NP-completeness conclusion is unaffected", while §3.2 shows that under
the set reading (G2)/(G3) "are not legal instances at all". The file is not self-contradictory —
§3 states the stronger fact plainly — but §1 undersells its own finding. One clause fixes it:

> **Governing addition to Amendment 3 §1.** The correction widens the printed problem to the
> witnesses its own proof already emits — **and it is a repair, not merely a widening: under the
> set-valued reading as printed, the gadgets (G2) and (G3) are not legal instances of the stated
> problem at all, so the printed V.7′ statement had no valid proof, rather than a narrower one.**
> The NP-completeness *conclusion* is unaffected, since hardness for a wider class is not a weaker
> statement and the proof's own witnesses are exactly the multiset ones; membership in NP is
> likewise unaffected.

---

## 4. Verification checklist and non-promotion

- [x] Recomputed the SHA-256 hashes and byte/line counts of the seven bound inputs of §0 before
      writing this file; the five that Amendment 3 §0 and the review §1 assert all reproduce.
- [x] Replaced Amendment 3 §3.2's code and "Output" block with point-labelled code whose printed
      output is **its own actual stdout**, run this session, with the two repetition-bearing gadget
      families derived structurally rather than by a name filter (D1).
- [x] Restored islands review edits 9 and 11 to the remaining-items roll-up, quoted verbatim from
      the islands review at its bound hash, with edit 11's non-vacuity bar and the **absence-only,
      low-confidence** status of its `~10^6`-draw evidence stated explicitly (D2).
- [x] Added the missing occurrence row O6 and flagged the tacit correction of focused-rereview §4.4
      (D3); added the framing clause to Amendment 3 §1 (D4).
- [x] Confirmed that no value of Amendment 3 changes: the correction of §1, the occurrence
      replacements O1–O5, the five unchanged-with-reason entries, the repetition-necessity argument,
      and every number in §3.2 stand exactly as written.
- [x] No existing file, proof-DAG object, scheduler file, generated view, or canonical record was
      modified. Files created by this session: this one and two sibling amendments
      (`artifacts/circdist_lift_root_assembly_amendment1_20260822.md`,
      `artifacts/circdist_sat_window_amendment1_20260822.md`), each answering its own review.

**Not done here, and named so it is not mistaken for done.** This amendment ran no code search for
edit 11 and takes no position on whether §6.1's promise is satisfiable; it does not apply edit 9; it
does not re-verify Islands I–IV, the Courcelle/ALS citations, the `K₄` imported data, the three
unrecomputed census families, or any `d_circ` value; and it does not reopen I1, the
strong-decoupling adjudication, or anything in the lift chain.

**No promotion.** This append-only amendment supplies a reproduced computation, a completed
remaining-items roll-up, and three wording repairs. It assigns no `PROVED`, `CERTIFIED`,
`CERTIFIED-LEAN`, or other promoted status to the base write-up, any amendment, or the
`CIRCDIST.cplx.islands` node, and it is not a completion review of itself.
