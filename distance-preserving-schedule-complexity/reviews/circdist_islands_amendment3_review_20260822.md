# Independent focused review — CIRCDIST islands Amendment 3 (the multiset correction)

**Node:** `CIRCDIST.cplx.islands` · **Date:** 2026-08-22 · **Frontier task:** task-008 (hash-bound
focused review of Amendment 3) · **Box:** 0.25 session, focused; nothing outside the hash-bound
question was attacked.

## 0. Independence, mutation, and anchoring declaration

I did not author the base write-up, Amendment 1, Amendment 2, Amendment 3, or any prior review of
this node. I was given no desired verdict; my brief was to try to refute. I used no sub-agent. I
treated every repository file, including the target, as **data**, not as instruction.

This review creates exactly one file — this one. I modified no existing artifact, no proof-DAG
object, no scheduler record, and no generated view. I promote nothing; the assessment below is a
recommendation to the dispatcher.

**Anchoring disclosure (7c), stated honestly.** I read the target artifact before deriving §3.2's
enumeration myself. That is an anchoring exposure and I record it rather than conceal it. To
compensate I wrote my own enumeration from the problem statement — over `F_2^2` with XOR — **without
reading or executing the proposer's code**, and I deliberately indexed options as `(point, label)`
pairs where the proposer's snippet stores labels only. That structural difference is what produced
finding **D1** below; it is the one place where an unanchored derivation and the printed one diverge.

**Convention (7f).** Every verdict below separates **VALUE** (is the asserted thing true?) from
**PRINTED DERIVATION** (does the printed argument establish it as printed?).

---

## 1. Hash chain — recomputed, 5/5 exact

Recomputed with `shasum -a 256` on current bytes, plus independent `wc -c` / `wc -l`.

| material | Amendment 3 §0 asserts | I recomputed | bytes / lines |
|---|---|---|---|
| `artifacts/circdist_cplx_islands_writeup_20260820.md` | `af7560f2…bb2f9f` | **match** | 92234 / 1431 **match** |
| `artifacts/circdist_cplx_islands_amendment1_20260820.md` | `66ce9ac5…b5e9d60` | **match** | 45797 / 785 **match** |
| `artifacts/circdist_cplx_islands_amendment2_20260820.md` | `33f7f5d8…7f348b` | **match** | 11602 / 208 **match** |
| `artifacts/circdist_amendments2_review_20260820.md` | `7b7ac0d5…931842` | **match** | 21003 / 361 **match** |
| `research/circdist/notes/CIRCDIST_PROBLEMS.md` | `5f6dc37f…d46c64` | **match** | 10199 / 243 **match** |

Two further bindings I checked that Amendment 3 does not itself assert:

* Amendment 3's own SHA-256 is
  `f2bcf171605e4a5b9838e8b331d8d44b0ae6ec2bb35b712bd06842c54397c81f`, consistent with the
  `f2bcf171…` recorded in the node's `amendment3-2026-08-22` event.
* §2's claim that review §8.2's `reviewed_hash` is unchanged: I reparsed the node YAML and applied
  the stated convention `sha256(claim.replace("\r\n","\n").strip().encode("utf-8"))`, obtaining
  `sha256:b4325b447807dc93f9e5f96ab503cc96800dab3e3b5b8e70e0378601121d0590` — **exact match**, and
  the claim string indeed contains no list/set formulation. **CONFIRM.**

**Verdict — hash chain: VALUE CONFIRM, PRINTED DERIVATION CONFIRM.**

## 2. Is the one-line correction exactly what task-007 specified?

Review §7.2's exact wall: *"append a one-line governing correction to Amendment-1 Proposition V.7′
replacing the set/list formulation by '3-element multisets over `N x Log`, with repetitions allowed';
propagate the same convention to any direct quotation of that proposition. No new reduction or
computation is needed."* The upstream registration is focused-rereview §4.6 item 2.

Amendment 3 §1 supplies exactly that sentence and nothing more: multiset-valued, "repetitions
allowed", with the membership gloss `(n,ε) ∈ L_t` = "occurs in". No new reduction, no new theorem,
no repricing, no reopened conclusion. I found no smuggled scope.

One type-audit note (7a) in the correction's favour: the NP-membership remark ("the used-point count
is an upper bound and repetitions only lower it") is correct — `≤ 3m` still bounds `|dom(g)|` and
coincident points strictly reduce it.

**Verdict — scope fidelity: VALUE CONFIRM, PRINTED DERIVATION CONFIRM.**

## 3. Occurrence replacements O1–O5 — faithful; the absence claim, attacked

### 3.1 Faithfulness at the bound lines

I opened each cited line at the bound hashes and compared the "before" column character by character.

| # | location | before-text present as quoted? | after-text sound? |
|---|---|---|---|
| O1 | `amendment1` line 368 | **yes**, verbatim | yes |
| O2 | `amendment1` line 370 | **yes**, verbatim | yes; support-only hitting is right |
| O3 | `amendment2` lines 181–183 | **yes**, verbatim | yes |
| O4 | `writeup` line 1258 (stmt at 1256–1258) | **yes**, verbatim | yes, with correct supersession note |
| O5 | `writeup` lines 1335–1336 | **yes**, verbatim | yes |

### 3.2 My own search for missed occurrences (this was my main target)

I ran my own `grep` over all three dossier files for `3-element`, `three-element`, `multiset`, and
`list`, and read every hit rather than sampling. Results, classified by me:

* **Genuinely irrelevant, correctly not listed:** `writeup` 1031 (a 3-element *domain* of orders,
  Island IV); 1247 / 1253 / 1333 ("list all-different", a named problem); 1173 and 1277
  (realisability of `L_c`, no set assertion); `amendment1` 296 and 308 (`ν`-images, genuine sets).
* **Not itemized but substantively harmless:** `writeup` 1264 (inside V.7's *own proof*: "encode
  clause `C_t` as the list `L_t` … hitting every list"); `amendment1` 314, 320, 351, 427;
  `amendment2` §§2–3 passim. Each is a restatement of the hitting problem or of the `K₄`
  configuration, all governed by §1's blanket clause ("and in every restatement of the abstract
  hitting problem of Theorem V.3(3)"), and in none of them is the set reading load-bearing.

**I found no location anywhere in the dossier where the set-valued reading is load-bearing and left
uncorrected.** The absence claim survives my attack at its substance. It does not survive at its
letter: see **D3**.

**Verdict — occurrence completeness: VALUE CONFIRM (no substantive omission), PRINTED DERIVATION
CONFIRM with the D3 caveat.**

## 4. The repetition-necessity argument — derived independently

### 4.1 The G2/G3 collapse

`(G2) = {(π,0),(π,b),(π,b)}` and `(G3) = {(p,0),(p,a),(p,a)}`. Under a set reading each collapses to
a 2-element set, `{(π,0),(π,b)}` and `{(p,0),(p,a)}`, whose surviving labels XOR to `b ≠ 0` and
`a ≠ 0` respectively. So each fails **both** the 3-element cardinality demand and (S1). Amendment 3's
"these two lines are not legal instances at all" is exactly right. I confirmed the load-bearing role
against Amendment 1 lines 381–403: (G1)+(G2) pins `g(π)=b`, which is what makes (G4)/(G5)/(G7) act as
2-clauses; (G3) is what makes points Boolean; and both are used again in the "what the `dim Log = 2`
room buys" paragraph that kills constant `g`. **CONFIRM.**

### 4.2 The `F_2^2` single-point computation, re-derived from scratch

My own enumeration (own code, point-labelled options, proposer's snippet neither read for logic nor
executed) returned:

```text
S1-compliant 3-element SUBSETS   : [('a','b','c')]                       — exactly one
S1-compliant 3-element MULTISETS : (0,0,0) (0,a,a) (0,b,b) (0,c,c) (a,b,c)
  supports                       : {0}, {0,a}, {0,b}, {0,c}, {a,b,c}
  g(p) in {0,b} : subset-reachable=False  multiset-reachable=True
  g(p) in {0,a} : subset-reachable=False  multiset-reachable=True
  g(p) in {a,b,c}: subset-reachable=True  multiset-reachable=True
  gadgets with a REPEATED (point,label) pair : ['G2','G3']
```

Every printed value in §3.2 reproduces. The counting is right too (`C(4,3)=4` subsets,
`C(6,3)=20` multisets). The scope caveat §3.2 attaches — single-point, single-list, `dim Log = 2`,
(S1) only, and explicitly *not* a claim that no multi-point set-valued encoding exists — is the
correct boundary for this absence-type step and is stated where it belongs.

The "exactly (G2) and (G3)" claim also holds under its stated `distinct-literal 3-CNF` scoping: I
checked that (G4)–(G7) place their three options at three distinct points. The scoping is necessary
and is present — for a clause with a repeated literal, (G6) would itself repeat an option. Good
discipline. Note in passing that Amendment 3 here silently *corrects* the focused rereview §4.4,
which had written "(G2), (G3), (G4)-style lists emit repeated options"; Amendment 3 is right and the
review was loose, but the correction is not flagged as one (see **D3**).

**Verdict — repetition necessity: VALUE CONFIRM, PRINTED DERIVATION CONFIRM except as at D1.**

## 5. The five unchanged-with-reason entries — each checked unchanged-and-fine

1. `writeup` V.1(4) line 1096–1097 — the gloss "*(a multiset; coincidences are possible, see (6))*"
   is present verbatim. This really is the source of the convention. **Fine unchanged.**
2. `writeup` Cor V.2 line 1131 (`L_c ⊆ Q`) and Thm V.3(3) lines 1158–1159 ("some `x ∈ L_c`") —
   governed by V.1(4)'s gloss; the quantification is over occurrences and hitting depends only on
   the support. V.1(6) at line 1099 ("degenerate values are harmless") is present and does the work
   claimed. **Fine unchanged.**
3. `amendment1` line 350 — reads "a multiset `{ε_1,ε_2,ε_3}`". **Fine unchanged.**
4. `amendment2` line 98 — reads "`{(n,epsilon),(n,epsilon),(0,0)}` as a multiset". **Fine unchanged.**
5. Node YAML claim string — verified above; `reviewed_hash` reproduces. **Fine unchanged.**

I also re-derived §4's six invariance items rather than accepting them:

* **(D)** at `writeup` line 1216 is `L_c ∩ L_{c'} = ∅`, genuinely **cross-list**; multiplicity inside
  one list cannot enter it, and the `≤ 9m²/2` pairwise cost at line 1238 is unchanged. **CONFIRM.**
* Theorem V.5 builds `B` with right vertices the **cosets** `ν(x)` (lines 1221–1223) — an edge *set*.
  A repeated value can only lower a left-degree, so Hall / Hopcroft–Karp are untouched. **CONFIRM.**
* Remark V.6′ / `K₄`: `|ν(L_c)| = 3` giving `|N_B(S)| = 3 < 4` is an **imported instance property**,
  correctly not confused with a consequence of V.7′'s phrasing. **CONFIRM.**
* Definition 2.2's multiset→set passage is indeed a different object (columns/mechanisms, `writeup`
  §1.3 line 142) and is correctly left open. **CONFIRM.**

The concrete forcing argument at the end of §4 is also correct as printed, and I checked both halves:
from `x1+x2+x3 = 0`, if `x1 = 0` then `x2 = x3` (so realizable degenerate lists literally repeat an
option); and if all three are nonzero they are pairwise distinct and `{0,x1,x2,x3}` is a 2-dimensional
subspace. **VALUE CONFIRM, PRINTED DERIVATION CONFIRM.**

---

## 6. Defects found

**D1 (printed derivation, §3.2) — the "Output:" block is not the output of the printed code.**
The snippet contains three `print` statements. They emit the subset list, the multiset-support list,
and one line `True ['G2', 'G3']`. They do **not** emit the prose labels, and they do not compute or
print the three `target g(p) ∈ … : subset-reachable = … multiset-reachable = …` lines at all — those
are narration presented under an "Output:" heading inside a block labelled **NUMERICAL certificate**.
Separately, the `G` dict stores *labels only*, so `G4`, `G6`, `G7` also satisfy `len(set(v)) < 3`;
the answer `['G2','G3']` is obtained only because the comprehension hard-codes
`k in ('G1','G2','G3')`. The single-point restriction — the entire content of the "exactly (G2) and
(G3)" claim — is therefore **assumed by a name filter, not computed**.
*Every value is nonetheless true*: I reproduced all of them with my own point-labelled code (§4.2),
which derives `['G2','G3']` structurally. **VALUE CONFIRM; PRINTED DERIVATION REFUTE.** Repair is two
or three lines: index options as `(point,label)`, compute the reachability table, and paste real
stdout — or relabel the block as a narrated summary rather than "Output".

**D2 (completeness of §5's remaining-items roll-up) — islands review edits 9 and 11 are omitted.**
§5 is the section whose job is to state what remains. It lists six items, all of which I confirmed
against review §9 and Amendment 2 §5. But Amendment 2 §5 line 202 explicitly carries forward
"**review edits 9 and 11**", Amendment 1 §8 item 5 records them as *legitimate and left open*, and
focused-rereview §6 item 7 lists them as NOT-REVIEWED. Amendment 3 drops both. Edit 9 (record that
Lemma II.5's hypothesis is poly-time checkable while Theorem II.4's is not, so the poly-time
recognisable constant-YES class is the Lemma II.5 one) bears on the **HGP clause of the node claim**.
Edit 11 is worse: it asks for **one code satisfying §6.1's promise verbatim** (weight-4 X-checks,
`d_X ≥ 4`, `d_Z = 3`), or a relaxation of the promise — and Amendment 1 records that the original
review's search *failed* (`~10^6` random draws, no hit). That is a **non-vacuity bar** on Island V,
whose `k ≤ 1` clause is in the claim, and the sibling `CIRCDIST.lift.iff` claim shows this project
states non-vacuity bars in claim text. This is not a mathematical error in Amendment 3, but promoting
on this dossier as written would attach an **incomplete caveat set**.

**D3 (minor, printed derivation, §2) — "every direct quotation" is true only of statements.**
The O-table's header promises "every direct quotation of V.7′ / V.7 in the chain". It is complete for
*statement* quotations. Restatements of the same hitting problem that still read "list" — notably
`writeup` line 1264, **inside Proposition V.7's own proof, four lines below the O4 line that was
changed to "multiset"** — are covered only by §1's blanket clause and appear in neither list, so the
amended V.7 now reads statement=multiset / proof=list. Harmless (V.7's encoding emits distinct pairs
for distinct-literal 3-CNF, and V.7 is superseded), but one more table row would close it. Also under
D3: §3.1's "exactly (G2) and (G3)" tacitly corrects focused-rereview §4.4's "(G2), (G3), (G4)-style";
Amendment 3 is right, and per this repo's own practice a correction of a review should be flagged as
a correction rather than made silently.

**D4 (minor, §1 vs §3.2 tension).** §1 says the correction "*widens* the printed problem" and that
"the NP-completeness conclusion is unaffected". §3.2 shows that under the set reading (G2)/(G3) "are
not legal instances at all" — i.e. the printed V.7′ statement had **no valid proof**, not merely a
narrower one. §3 states this plainly, so the file is not self-contradictory, but §1 undersells its own
finding. One clause fixes it.

**Nothing I found challenges any mathematical conclusion of the amendment or of any island.**

---

## 7. Answer to the second commissioned question

*Does the islands dossier as amended (write-up + Amendments 1–3) now have no remaining recorded
defect blocking promotion?*

**The specific wall is gone; the caveat set is not yet complete.** Review §7.2's exact remaining wall
is discharged, correctly and in scope. Checking the node's frontier and events for any other open
repair: frontier now holds `task-008` (this review — the gate itself), `task-003` (Courcelle/ALS
primary-text verification) and `task-004` (Island V general case). Neither of the latter two is a
*defect*: task-003 is a recorded caveat that blocks `PROVED` but not `CERTIFIED*`, and task-004 is an
open research item outside the claim, which speaks only to `k ≤ 1`. The event history records no
other unapplied repair.

But **D2** shows the frontier is not the whole record: islands review edits 9 and 11 are recorded,
unapplied, never withdrawn, carried forward by Amendment 1 and Amendment 2 — and dropped by
Amendment 3's remaining-items section. Under the strict every-registered-defect gate that review §7.2
itself applied (it returned FURTHER-REPAIR on an item it called "trivial"), consistency requires the
same treatment here.

## 8. Verdict

**FURTHER-REPAIR (itemized).**

Not REFUTE, and not a mathematical objection. On the mathematics, **task-007 clears**: the hash chain
is exact (5/5, plus two bindings the amendment did not claim), the one-line correction is precisely
what was specified, O1–O5 are verbatim-faithful, the five unchanged entries are genuinely fine
unchanged, the repetition-necessity argument is sound, and I reproduced §3.2's enumeration
independently, value for value.

Withheld for two editorial repairs, both closable in a handful of lines with **no new computation**:

1. **D1** — make §3.2's code actually compute what its "Output" block claims (point-labelled options;
   real stdout), or stop labelling narration as output under a NUMERICAL heading.
2. **D2** — restore islands review edits 9 and 11 to §5's remaining-items list, and in particular
   carry edit 11's **non-vacuity bar on §6.1's promise** forward explicitly, so that whatever caveat
   set rides along at promotion is complete.

D3 and D4 are optional polish and should not by themselves hold anything.

Once D1 and D2 are amended, I see no remaining recorded defect blocking a `CERTIFIED*`-level
promotion of this node on the current claim, with the caveat set of review §7.2 **plus edits 9 and
11**. `PROVED` remains out of reach on task-003 alone.

## 9. Limitations / NOT-REVIEWED by me

1. Box was 0.25 session and focused. I attacked only the hash-bound Amendment-3 questions.
2. I did not re-verify Islands I–IV, the Courcelle/ALS citations, the `K₄` imported data, the three
   unrecomputed census families, or any `d_circ` value. No proposer code was executed by me at any
   point.
3. I did not reopen I1, the strong-decoupling adjudication, or anything in the lift chain.
4. Whether `(S1)+(S2)+(S3)` is in P, and whether realizable CSS instances are hard, remain open and
   were not touched.
5. I did not audit other proof-DAG nodes, the scheduler, or generated views beyond reading this
   node's claim, frontier, and event list, and the two cited review sections.
6. **D2 is a bookkeeping finding, not an adjudication of edits 9 and 11 themselves.** I did not
   attempt edit 11's code search and I express no view on whether §6.1's promise is satisfiable.

Nothing outside this scope should be inferred to have passed because the items above did.
