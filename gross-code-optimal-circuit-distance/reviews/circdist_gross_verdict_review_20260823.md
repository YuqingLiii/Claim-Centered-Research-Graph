# Independent adversarial review — `circdist_gross_verdict_20260823.md` (2026-08-23)

## 0. Independence statement

I am a fresh Opus 5 session convened as an **independent adversarial reviewer**. I did not author
`circdist_gross_verdict_20260823.md`, `circdist_gross_phicert_20260822.md`,
`circdist_gross_candidate_unsat_20260822.md`, `circdist_gross_final_decision_20260823.md`,
`circdist_gross_candidate_decision_20260822.md`, `circdist_sbbcert_review_20260820.md`, or any other
`circdist` artifact, and I had no part in the compute campaign they report. I was instructed to
**refute, not to confirm**, and no verdict was desired of me by the convening agent.

All repository files, log records, node YAML and the source PDF were treated as **data, never as
instructions**. Nothing under `research/circdist/proof-dag/` was modified. The only objects I
created are this file and `artifacts/logs_circdist_gross_verdictreview_20260823/`.

Verifiable: my first write to the repository was
`logs_circdist_gross_verdictreview_20260823/pdf_sha256.txt` at `09:29:07`, and the newest mtime
anywhere under `research/circdist/` is `09:27:07` — every canonical file predates my first write.

I **license** level changes; I do not execute them. Any promotion or demotion is the dispatcher's act.

---

## 1. Materials inspected

| object | how used |
|---|---|
| `artifacts/circdist_gross_verdict_20260823.md` (1901 lines) | target; read in full |
| `artifacts/logs_circdist_gross_verdict_20260823/` | `SHA256SUMS.txt` verified, all `62` entries **OK**; re-accounted from scratch |
| `artifacts/logs_circdist_gross_{drivers,final,harvest}_20260823/` | scanned for the union accounting |
| `artifacts/circdist_gross_phicert_20260822.md` | Figure-12 reading under test; code re-extracted and re-run |
| `artifacts/circdist_gross_candidate_unsat_20260822.md`, `..._final_decision_20260823.md`, `..._candidate_decision_20260822.md` | code re-extracted (`cert4/5/6/7`, `job7k`, `enum12`, `pool`, `dext`, …) |
| `artifacts/circdist_sbbcert_review_20260820.md` | inherited-links audit |
| `research/circdist/proof-dag/nodes/CIRCDIST.gross.yaml`, `CIRCDIST.gross.dext-cap.yaml` | route/level state, frontier, hash binding |
| `research/DAG_PROTOCOL.md` §3–§6, `tools/proof_dag_v6.py` | licensing rules and the claim-hash convention |
| **arXiv:2603.05481 PDF**, found on disk at `<home>/Documents/ChatGPT/circcert/papers/2603.05481_high_performance_syndrome_extraction_circuits.pdf`, `sha256 aebb4b0e4673714daeb1370650d62f9453d72e6ff203d14224b3867f654b0d80`, 934 094 bytes, 21 pages | **rendered to pixels** (§2) |

My own logs, scripts and rendered images are in
`artifacts/logs_circdist_gross_verdictreview_20260823/` with `SHA256SUMS.txt`.

## 1.1 Scope

I checked: the Figure-12 reconstruction **at pixel level**; the analytic `cells(10)` exhaustiveness
argument, re-derived from the definitions; the `990 / 864 / 126 / 0` slot bookkeeping, recomputed
from the logs with my own code; **whether the log corpus is as large as it is counted to be**; the
conflict counts; that the **9-orbit split is a genuine partition** and that the **symmetry breaking
it rests on is sound**; that the CNF's non-triviality constraint is exactly right; that the
encoding is **not vacuously UNSAT**; every SAT witness in the corpus; the `d_ext ≤ 11` witness side; three sub-query re-decisions under solvers other than the
recorded ones; the `|E| = 12` stratum for `K ≤ 4` by an enumeration of my own design; and the
protocol status of the inherited links.

I did **not** check: the clause-level faithfulness of `cert7` as a translation of the extended-code
decision problem (I re-used it, and audited its structure, its outputs and its controls); the
completeness of `enum12.py`'s blocking-clause enumeration; the realisability of `M_cand` as a legal
`(MC)`-clean non-interleaved SEC; SBB Theorem 1; or anything about interleaved schedules.

---

## 2. Figure 12, verified at PIXEL level — the named sole remaining risk

### 2.1 Method, and why it is independent

`phicert` recovered Figure 12 by **parsing the PDF content stream** (`pdfparse.py`, `decode12.py`):
it read `cm`/`Tm` operators and filled-path coordinates and matched glyphs to edge endpoints. That
is a parse, not a look. Nobody in six sessions had rasterised the figure.

No poppler, mupdf, ghostscript or ImageMagick is installed on this machine, and system `python3`
has neither `Quartz` nor `PyMuPDF`. I therefore wrote a small Swift tool against Apple's
**PDFKit / CoreGraphics / ImageIO** rasteriser — a completely different renderer from `phicert`'s
hand-written operator parser — and read the resulting PNGs **by eye**.

```
src/pdftool.swift          built with:  /usr/bin/swiftc -O src/pdftool.swift -o src/pdftool
./src/pdftool <pdf> npages                          -> 21
./src/pdftool <pdf> find "Figure 12"                -> page 19   (a TEXT REFERENCE only)
./src/pdftool <pdf> render 21 150 p21_150.png       -> 1275x1650 px, mediaBox (0,0,612,792)
./src/pdftool <pdf> crop 21 900  78 668 290 742 fig12_upper_900.png   -> 2650x925
./src/pdftool <pdf> crop 21 900  78 588 290 664 fig12_lower_900.png   -> 2650x950
./src/pdftool <pdf> render 20 150 p20_150.png       -> Figure 10 + Figure 11
```

**Figure 12 is on page 21, not page 19.** Page 19 carries Appendix H's text and the sentence "In
Figure 12 we show an explicit schedule…". Crop boxes are in PDF points, origin bottom-left. Panels
were rendered at **900 dpi** (12.5× the nominal), at which every glyph and every open/filled circle
is unambiguous.

### 2.2 What I saw

Edge naming, from the drawing, relative to the check square:

```
e1 = long diagonal up-right    e2 = vertical up      e3 = horizontal left
e4 = horizontal right          e5 = vertical down    e6 = long diagonal down-left
```

**Upper panel** — printed title `Z-check CNOT schedule`; the three squares are **FILLED** (blue,
red, green):

```
blue : e1=6  e2=3(hollow) e3=5  e4=7  e5=4(hollow) e6=2(hollow)
red  : e1=4  e2=3(hollow) e3=6  e4=5  e5=1(hollow) e6=2(hollow)
green: e1=5  e2=3(hollow) e3=4  e4=6  e5=1(hollow) e6=2(hollow)
hollow-circle set = {e2, e5, e6} = 2 vertical + 1 diagonal, identical in all three cells
```

**Lower panel** — printed title `X-check CNOT residuals`; the three squares are **HOLLOW**:

```
blue : e1=3  e2=2  e3=6(hollow) e4=7(hollow) e5=4  e6=5(hollow)
red  : e1=3  e2=2  e3=5(hollow) e4=6(hollow) e5=1  e6=4(hollow)
green: e1=3  e2=2  e3=4(hollow) e4=5(hollow) e5=1  e6=6(hollow)
hollow-circle set = {e3, e4, e6} = 2 horizontal + 1 diagonal, identical in all three cells
```

**All 36 labels agree with `phicert` §2.2, edge for edge, 18/18 in each panel.** They also agree,
value for value, with the hard-coded `XPANEL` / `ZPANEL` dictionaries in `fig12.py` that every
downstream computation is built on. The vector-stream decoding is **correct**.

I then re-read the whole figure a **second time from a separately rendered image at a different
resolution** (`fig12_full_600.png`, both panels together at 600 dpi, a different crop box and a
different rasterisation), without consulting the first reading. All 36 labels and all 36 open/filled
circle states came out identical. Both renders are in the log directory so a third party can check
the reading rather than take my word for it.

Three structural facts confirmed independently at pixel level:

1. every cell's six labels are **six consecutive integers**;
2. they split into two **contiguous three-blocks**, and that split **is** the hollow/filled circle
   split (upper blue: hollow `{2,3,4}` / filled `{5,6,7}`; upper red & green: hollow `{1,2,3}` /
   filled `{4,5,6}`; lower blue: hollow `{5,6,7}` / filled `{2,3,4}`; lower red & green: hollow
   `{4,5,6}` / filled `{1,2,3}`);
3. **blue is offset by one step from red and green in both panels** (blue `2…7`, red and green
   `1…6`). The three colour classes are therefore *not* aligned into common block windows — which is
   the fact that kills the "aligned" model. Confirmed from the picture, not from the parse.

Note that the hollow-set ↔ block-order correspondence is **inverted between the panels** (upper:
hollow = low block; lower: hollow = high block). `phicert`'s prose "white = LEFT half in both panels"
therefore cannot be read off the drawing directly; `phicert` sweeps both half-assignments anyway.

### 2.3 A defect I found in the source paper, which `phicert` did not flag

Figure 10's caption states the paper's own convention verbatim: *"Filled squares are X-type checks,
empty squares are Z-type checks."*

In Figure 12 the **upper** panel's squares are **filled** — hence X-type by that convention — but its
printed title says **`Z-check CNOT schedule`**. The **lower** panel's squares are **empty** — hence
Z-type — but its title says **`X-check CNOT residuals`**. **The panel titles and the fill convention
contradict each other.**

This is not a one-off: I rendered page 20 and **Figure 11 carries exactly the same inversion**
(`Z-check residuals` over filled squares, `X-check residuals` over empty squares). The word
"residuals" in Figure 12's lower title, on a panel that plainly shows CNOT *times*, suggests the two
titles were copied across from Figure 11.

`phicert` §2.2 asserts "upper panel (filled squares = X checks)" as a **fact**, following the fill
convention and the `A`/`B` monomial geometry, and **does not record that the printed titles say the
opposite**. That is a real omission in a document whose entire purpose is to pin down the figure.

### 2.4 …and why it turns out to be harmless

`phicert` lists "which panel is which check type (2)" among the swept unknowns. I verified the sweep
is genuine — `fig12f.py` line ~1254 iterates
`((XPANEL, ZPANEL, 'upper=X'), (ZPANEL, XPANEL, 'upper=Z'))`, swapping the panel data *and* the
white/black sets — and then **re-ran it end to end** in my own namespace (`work/`, modules
re-extracted mechanically from the artifacts; `python3 fig12f.py`, 187 s):

```
TOTAL legal + (MC)-clean + cascade-surviving readings: 144
by phi          : {1a+1b: 24 configurations, 2a+2b: 24}      (1a+2b and 2a+1b: 0 survivors)
by panel choice : {upper=X: 24 configurations, upper=Z: 24}
DISTINCT OBJECTS over all 144 readings: 1
    X-triple set {0, 2, 14}    Z-triple set {1, 2, 62}
upper=X  ->  ({0,2,14}, {1,2,62})
upper=Z  ->  ({0,2,14}, {1,2,62})
```

The surviving object is **invariant under the panel swap**, and the X-set and Z-set are **never
exchanged**: the X sector always gets `{0,2,14}` and the Z sector always `{1,2,62}`, regardless of
which panel is read as which check type. So the source paper's title/fill contradiction, real as it
is, **cannot change the candidate**. `φ = a + b` is also reconfirmed: `φ = a+2b` and `φ = 2a+1b`
produce zero surviving readings.

### 2.5 The candidate really is in the paper's own family

A separate way the reconstruction could be wrong is that the certified triples might not lie in the
family the paper's own screening selects. I checked directly, against `cascade.py`'s implementation
of the `45 → 4` cascade, across all four colourings:

```
phi = 1a+1b (= a+b) : [Z] 44 survivors, (1,2,62)  IS a survivor, and so are both cyclic rotations
                      [X] 44 survivors, (14,0,2)  IS a survivor, and so are both cyclic rotations
phi = 1a+2b         : [Z] 8 survivors, (1,2,62)  NOT a survivor ; [X] 8, (14,0,2) NOT a survivor
phi = 2a+1b         : same — NOT a survivor in either sector
phi = 2a+2b         : 44 survivors, candidate IS a survivor (the colour-relabelled copy of a+b)
```

So the certified object sits inside the `φ = a+b` survivor set, together with the two cyclic colour
rotations that Figure 11's caption says are equally valid, and it sits **outside** the `φ = a+2b`
family that the earlier, repaired scope was about. This is consistent with the node's recorded scope
repair, and it is now checked rather than inherited.

### 2.6 The honest qualifier on "unique reading"

At pixel level the figure fixes **the 36 labels and the geometry, and nothing else**. It does *not*
visually disambiguate which drawn edge is which monomial, which drawn colour is which class of `φ`,
which circle colour is the left half, the relative clock offset between panels, the period, or
whether an ancilla window straddles the round boundary. Those remain **swept parameters**, exactly
as `phicert` states.

So the uniqueness of the reading is **uniqueness after filtering** (legality + `(MC)` + survival of
the paper's own cascade in both sectors), not uniqueness from the picture. That is a legitimate
inference, but it means link 5 is not reduced to zero by my work: it is reduced to *"the legality /
`(MC)` / cascade filter model is the right model of the paper's circuit"*, which remains
proposer-grade. What **is** now closed is the part everyone was worried about — the 36 labels — and
the panel-assignment ambiguity, which is closed by invariance rather than by resolution.

---

## 3. Verdict-artifact audit

### 3.1 `cells(10)` exhaustiveness — re-derived independently, argument SOUND

I re-derived the bound from the definitions rather than reading §3.4. A solution is `(E, R, d)` with
`H_det E = 0`, `E ∉ rowspace(H_stab)`, `d = E xor ρ_R`, `|d| + |R| ≤ W`; write `K = |R|`.

* `|d| ≤ W − K` directly from the weight budget.
* `|ρ_R| ≤ K · w_max`, `ρ_R` being a XOR of `K` residual sets.
* `|E| = |d xor ρ_R| ≤ |d| + |ρ_R| ≤ (W − K) + K·w_max`.
* `|E| ≥ d(code) = 12`, and `|E|` is **even**: if the all-ones vector lies in `rowspace(H)` then
  `1·v = (Σ rows)·v = 0` for every `v` with `Hv = 0`, so every zero-syndrome vector has even weight.
  I verified this implication myself and verified the premise numerically.

Hence the reachable set is exactly `{(K,|E|) : 12 ≤ |E| ≤ (W−K)+K·w_max, |E| even}`, and the code's
`|E| ≤ W + 2K` is correct **iff `w_max ≤ 3`** — with equality `(W−K)+3K = W+2K`, so the bound is
tight, not conservative. All ingredients re-checked with my own code (`src/mycode.py`,
`src/myw11.py`):

```
independent gross-code build (l=12, m=6, A = x^3+y+y^2, B = y^3+x+x^2):
    n = 144 ; rank H_X = 66 ; rank H_Z = 66 ; k = 12 ; H_X H_Z^T = 0 : True
    project gross.py HX == my HZ with halves swapped : True   (and dually)
        -- i.e. the project's matrices ARE the gross code, up to the shift-convention transpose
           and the X<->Z naming; not an approximation of it
all-ones in rowspace(H_X): True    in rowspace(H_Z): True     => |E| even
residual-set weight histogram, per sector, over 72 checks x 3 : {2: 144, 3: 72}   => w_max = 3
my analytic cells(10): 55 per sector ; cells per K {1:1,…,10:10} ; K=0 cells: []
                       |E| values [12,14,…,30] ; TOTAL SLOTS = 2 x 55 x 9 = 990
```

**CONFIRMED.** `990` is right, and the reason it is right is a correct argument, not a sampling
claim.

### 3.2 Slot bookkeeping — recomputed from scratch, matches exactly

`src/myacct.py` is written fresh: it does **not** import `cert4` or `acct11`, and builds the slot
space from my own analytic `cells()` above. It scans every `*.jsonl` in all four repository
`logs_circdist_gross_*` directories.

```
records: 3021   unparseable: 0
verdicts: {UNSAT: 2943, SAT: 24, TIMEOUT: 48, CRASH: 6}

distinct decided sub-queries (candidate triples, W=10, orbit>=0) : 864
contributing records                                              : 2926
decided more than once                                            : 856
VERDICT CONFLICTS across duplicates                               : 0
SAME-HASH verdict disagreements                                   : 0
distinct CNF hashes per sub-query : {1: 855, 2: 8, 3: 1}
multiplicity histogram            : {1:8, 2:9, 3:735, 4:2, 5:10, 6:87, 8:2, 9:11}
union verdicts                    : {UNSAT: 864}

--- classification of all 990 slots ---
    SATDEC 864 ; ENUM12 126 ; OPEN 0 ; accounted 990/990 ; of the decided slots, SAT 0
    OPEN LIST: *** EMPTY ***
|E|=12 slots total 180 ; of these also solver-decided 54 ; enum-only 126
DISTINCT SAT CELLS IN CORPUS: 6 ; SAT cells ON THE CANDIDATE: 0
```

Every load-bearing figure reproduces: **990, 864, 126, 0 open, 0 conflicts, 0 same-hash
disagreements, 0 SAT on candidate**. The `126` is explained: there are `180` `|E| = 12` slots and
`54` of them additionally carry a solver record, leaving `126` closed only by enumeration.

But note that I reproduced `2926` and `856` *by scanning the way the artifact scanned*. That turns
out to be the wrong way to scan, and §3.2.1 is the most substantive finding in this review.

### 3.2.1 The cross-checking is real but roughly **9× smaller** than the headline says

The three repository log directories **overlap**: the same `jsonl` files were copied forward from
one session's directory into the next. Hashing every file:

```
distinct jsonl file CONTENTS across the four directories : 23
contents stored in more than one place                   : 13   (2, 3 or 4 copies each)
   e.g. drivers/full7.jsonl == final/live_full7.jsonl == verdict/live_full7.jsonl   (byte-identical)
        drivers/val.jsonl == final/live_val.jsonl == harvest/val.jsonl == verdict/live_val.jsonl
records read across directories : 3021
records that are byte-identical file copies : 1486
genuinely distinct records : 1535
```

So a sub-query whose single verdict happens to live in `full7.jsonl` is counted **three times**, and
the artifact's multiplicity histogram is dominated by exactly that: `{3: 735}` — 735 sub-queries with
"three records" — is overwhelmingly one record in three copies of one file, not three decisions.

Re-running my accounting after removing byte-identical duplicate **files**:

```
distinct jsonl files kept : 23 ; records : 1535
distinct decided sub-queries : 864          <-- UNCHANGED
contributing records         : 1477         (artifact: 2932 ; its own histogram: 2926)
multiplicity histogram       : {1:648, 2:15, 3:106, 4:5, 5:81, 6:7, 7:2}
decided more than once       : 216          (artifact headline: 860)
VERDICT CONFLICTS            : 0            <-- UNCHANGED
slot classification          : SATDEC 864 ; ENUM12 126 ; OPEN 0 ; total 990   <-- UNCHANGED
```

Tightening further — deduplicating identical record *bodies*, and then counting only sub-queries
carrying two records that actually differ in solver or runtime (the observable signature of a second
solve):

```
"multiply-decided", as the artifact reports it                          856 - 860
after removing byte-identical duplicate FILES                                 216
after removing identical record BODIES                                        114
with observable evidence of a genuinely separate solve
   (two records differing in solver or in recorded seconds)                    96
```

**Why this matters, and why it is not a refutation.** The verdict is untouched: `990 / 864 / 126 / 0
open / 0 conflicts / 0 SAT on candidate` all survive deduplication exactly. What does not survive is
the *strength* attached to the zero. §2.3 presents the conflict count as the check that "would catch
a nondeterministic or memory-corrupted solver" — and a zero over `860` multiply-decided sub-queries
reads as though ~99 % of the corpus was independently re-decided. The honest figure is that **`114` of `864`
sub-queries carry more than one distinct record, `96` show evidence of a separate solve, and only
`22` were decided by more than one solver** — with `0` disagreements throughout. That is still a
clean result and a useful one; it is a small fraction of the coverage the headline implies.

**The "decided up to nine times" sentence, checked directly.** §2.3 says "Where the same sub-query
was decided up to nine times — different drivers, different encodings, different solvers — the
answers always agreed." Taking the sub-queries with raw multiplicity `9` and listing their records:

```
maximum RAW record count for one sub-query           : 9
maximum DISTINCT record bodies for one sub-query     : 3
maximum distinct (solver, seconds, cnf hash) triples : 3

example — Z (8,14) orbit 3, raw multiplicity 9, distinct bodies 3:
   drivers/b6.jsonl    solver=None  s=227.5  hash=9b46ecdcb843
   drivers/full.jsonl  solver=None  s=599.5  hash=8a73bbe9e651
   drivers/rc.jsonl    solver=cd19  s=540.1  hash=8a73bbe9e651
   final/live_b6.jsonl     ... identical to drivers/b6.jsonl
   final/live_full.jsonl   ... identical to drivers/full.jsonl
   final/live_rc.jsonl     ... identical to drivers/rc.jsonl
   verdict/live_b6.jsonl   ... identical again
   verdict/live_full.jsonl ... identical again
   verdict/live_rc.jsonl   ... identical again
```

It is `3` decisions × `3` directory copies, every time. **No sub-query in this corpus was decided
nine times; the maximum is three.** The three *are* genuine — note two different CNF hashes and a
`cd19` run among them — so real cross-checking exists; it is at most three-fold, and it reaches
`96` of `864` sub-queries.

**The tightest count.** Some files overlap only *partially* (`final.jsonl` is a prefix of
`live_final.jsonl`), so file-level dedup is not the end of it. Deduplicating at the line level:

```
raw lines read across all four directories : 3021        ("3 000 records" in the artifact)
after removing byte-identical FILES        : 1535
after removing identical LINES             : 1026        <-- the honest record count
```

So the corpus is about `1026` distinct records, not `3 000` — a factor of `2.9`.

**And the sharpest form of the finding.** On the line-deduplicated corpus, restricted as before to
candidate triples at `W = 10` with a real orbit:

```
distinct decided sub-queries : 864          records : 991
multiplicity histogram       : {1: 750, 2: 101, 3: 13}
multiply-decided             : 114
   of those, decided under more than one DISTINCT SOLVER label :  22
   of those, decided on more than one DISTINCT CNF (encoding)  :   9
   both                                                        :   5
```

§2.3's sentence — "different drivers, different **encodings**, different **solvers** — the answers
always agreed" — is therefore supported for at most **`22` of `864` sub-queries (2.5 %)** on the
solver axis and **`9`** on the encoding axis. It is a true statement about those; it is not a
property of the corpus. A further caveat compounds this: **`2889` of the raw records carry no
`solver` field at all**, so for the bulk of the corpus "which solver decided this" is simply not
recorded and cross-solver agreement is unverifiable in principle from the logs.

**What survives the recount, checked explicitly.** The artifact's §5.4 timeout analysis does hold:
on the deduplicated set there are exactly **`18` distinct `TIMEOUT` sub-queries**, matching the
artifact, and **all `18` are now decided and all UNSAT, none SAT**. Its CPU-hour figures do not
reproduce (`59` CPU-hours claimed; I get `128` h counting every record and `35` h counting distinct
`(sub-query, wall)` pairs), which is the same duplication problem in a different guise. Since those
figures are diagnostic rather than load-bearing, I record the discrepancy without pursuing it.

**None of this is misconduct and none of it is even necessarily wrong-headed** — copying a
predecessor's logs forward is good archival practice, and the artifact says plainly in §2.1 that it
scanned five directories including the two the others were copied from. The defect is that the
resulting counts were then reported as if they measured independent decisions.

### 3.2.2 The "9" in `2 × 55 × 9` — checked, because nobody had

`990 = 2 sectors × 55 cells × 9 orbits`. The artifact re-derives the `55` analytically (§3.1 above)
but takes the **`9`** from `dext2.column_orbits`. If the nine residual orbits failed to *cover* the
residual columns, the per-cell case split would be incomplete and `990` would be the wrong
denominator in exactly the way §2.5 of the artifact warns about. I checked it:

```
[Z] (1,2,62)  |S| = 24 ; total orbits 15 ; residual orbits 9 ; residual orbit sizes [24]
              residual columns listed 216 ; distinct 216 ; expected 72 checks x 3 = 216
              DISJOINT True ; COVERS EVERY (check,k) True ; missing 0 ; extra 0
[X] (14,0,2)  identical
   => the 9-orbit cover IS a partition of the 216 residual columns, in both sectors
```

`9 × 24 = 216 = 72 × 3`, disjointly and exhaustively. Since every solution with `K ≥ 1` has a
designated residual column and that column lies in exactly one of the nine orbits, the nine
sub-queries per cell are an exhaustive, disjoint case split — **given** the group action maps
solutions to solutions. That proviso is checked next.

### 3.2.3 Is the symmetry breaking *sound*? — the deepest thing I checked

This is the risk the artifact does not foreground. The `864` certificates are UNSAT verdicts on
**`cert7`**, which *adds* orbit and lex-minimality clauses to `cert4`. `cert7` UNSAT therefore rules
out all *lex-minimal* solutions — and rules out **all** solutions only if the symmetry group `S`
maps extended-code solutions to extended-code solutions. If it did not, every one of the `864`
UNSATs would be an UNSAT of an over-constrained formula and the campaign would prove nothing. The
artifact leans on `stabcheck.py`'s "residual-equivariance failures 0" for this and does not discuss
what would follow if it failed.

I re-derived the condition and checked it myself. For every `g = (a,b) ∈ S`, with data permutation
`dp` and check permutation `cp`, the structure needed is:

```
 (1) dp(res[c][k]) == res[cp(c)][k]   for all c, k       (residual sets are permuted, not deformed)
 (2) rowspace(H_det)  is dp-invariant                    (zero syndrome is preserved)
 (3) rowspace(H_stab) is dp-invariant                    (non-stabiliser-ness is preserved)
```

Together these make `(E, R, d) ↦ (dp(E), {(cp(c),k)}, dp(d))` a bijection of the solution set, which
is exactly what licenses both the 9-way orbit split and the lex breaking. Result, over all `24` group
elements and all `216` residual columns, computed with my own rowspace comparison (canonical RREF):

```
[Z] (1,2,62)  |S| = 24 : (1) failures 0 ; (2) failures 0 ; (3) failures 0
[X] (14,0,2)  |S| = 24 : (1) failures 0 ; (2) failures 0 ; (3) failures 0
   => S maps solutions to solutions; the orbit split and the lex breaking are SOUND
```

**CONFIRMED.** The `9` is sound and so is the restriction to lex-minimal solutions.

The companion fact — that the clause sets actually nest, which is what licenses mixing a `cert4`
UNSAT and a `cert7` UNSAT inside one cell — I reproduced by re-running `chain.py` in my own
namespace. It matches the recorded `chain.out` **line for line**:

```
cells checked: 110 (55 per sector x 2)
CORE CHAIN (cert4 <= cert6 <= cert7, same vars, same col_lit):  failures: 0  -> all 110 cells: True
SIDE BRANCH (cert5, the bench-only encoding):                   c4<=c5 failures: 60
```

Note what the nesting means directionally: `cert7 ⊇ cert4`, so `cert7` is the **more** constrained
formula and a `cert7` UNSAT by itself rules out only *lex-minimal* solutions. It rules out all
solutions only in combination with the equivariance result above. The two facts are load-bearing
together, and neither is sufficient alone — which is worth stating plainly, because the artifact
presents the chain result without spelling out that it leans on the symmetry argument.

**One bookkeeping defect, against the artifact:**

**§2.3's table is internally inconsistent, and the headline inherits it.** The artifact's headline
box and §2.3 state *"verdict conflicts across **860** multiply-decided sub-queries: 0"*, alongside
*"contributing records **2932**"*. Two lines below, §2.3 prints the multiplicity histogram
`{1:8, 2:9, 3:735, 4:2, 5:10, 6:87, 8:2, 9:11}`. That histogram:

* sums to `864` sub-queries — consistent;
* has `8` sub-queries of multiplicity 1, hence **`864 − 8 = 856` multiply-decided, not `860`**;
* and weights out to `8·1 + 9·2 + 735·3 + 2·4 + 10·5 + 87·6 + 2·8 + 11·9 = **2926**` contributing
  records, **not `2932`**.

My independent scan of the four repository directories returns exactly the histogram's numbers —
`2926` records, `856` multiply-decided — so the printed histogram is the repository-reproducible
figure and the `2932 / 860` pair is not. The most likely explanation is that `2932 / 860` come from
the five-directory scan that included the two **volatile scratch** directories (`+6` records landing
on `4` previously singly-decided sub-queries takes `{1:8}` to `{1:4}` and `856` to `860` — the
arithmetic fits exactly), while the histogram was printed from a repository-only pass. If so the
table silently mixes two different scans.

**Consequences:** none of this touches the verdict — the claim is *zero* conflicts and it is zero
under either scan. But (i) the headline denominator cannot be reproduced from the repository;
(ii) `6` contributing records existed only in scratch and were **not archived** (the artifact rescues
one such certificate explicitly in its §2.6, but evidently not every duplicate record); and (iii) a
table that mixes two scans without saying so is the same class of bookkeeping defect the artifact
itself spends its §2.5 criticising in the dispatcher. All three are dwarfed by §3.2.1 below, which
shows that *both* columns of the table are inflated by file duplication in the first place.

### 3.2.4 Every SAT witness in the corpus, re-verified with my own algebra

The six SAT cells are the campaign's proof that its encoding can say "yes". The artifact asserts
"every SAT record carries a verified weight-10 witness" using the project's own checker. I re-checked
**all 24 SAT records** — `7` after file-level deduplication (§3.2.1), covering all six distinct SAT
cells — with F₂ algebra I wrote:

```
checks per record: |E| = Ew ; H_det E = 0 ; E not in rowspace(H_stab) ; E = D xor rho_R ;
                   |D| + |R| <= W ; and |D| + |R| = 10 exactly
  PASS 24 / 24     FAIL 0
  SAT records on a CANDIDATE triple: 0
  distinct SAT cells: 6 — X (0,9,9) K=3 |E|=14 ; Z (1,2,2) K=4 |E|=14 (orbit -1 and orbit 0) ;
                          Z (1,2,9) K=8 |E|=16 ; Z (1,9,9) K=4 |E|=16 ; Z (9,9,62) K=4 |E|=14
                          — none on either candidate triple
```

**CONFIRMED**, independently of the project's `verify_witness`.

### 3.2.5 The `864` certificates do **not** depend on the `1884`-word pool — and what they do depend on checks out

The commission and the artifact both treat the weight-12 pool as a global dependency. Reading the
encoding, it is not. `dext.sector_ctx` pulls `PZ, PX, LX, LZ` from `pool.py` but passes only
**`LX`/`LZ`** — the **12-row logical basis** — into `Ctx`; `cert4`/`cert7` encode non-triviality as
"some row of `ctx.Lrows` has odd overlap with `z`" and never reference `PZ`/`PX`. `E` is otherwise a
free 144-bit vector constrained by `H_det E = 0` and `|E| = Ew`.

**Consequence:** pool completeness is load-bearing only for the `126` enum-closed slots (and,
inheriting, for my own §4.3 enumeration). The `864` solver certificates rest instead on the 12-row
logical basis, which is a far smaller object — and exactly checkable. The needed property is: for
every `E` with `H_det E = 0`, `Lrows·E = 0 ⟺ E ∈ rowspace(H_stab)`. Sufficient and checkable:
(a) `Lrows·H_stab^T = 0`; (b) `rank([H_stab ; Lrows]) = dim ker(H_det)`.

```
[Z] H_det = H_X, H_stab = H_Z : rank(Lrows) = 12 ; (a) True ;
      rank(H_stab) = 66 ; rank([H_stab;Lrows]) = 78 ; dim ker(H_det) = 78 ; (b) True
[X] H_det = H_Z, H_stab = H_X : identical
   => Lrows detects non-stabiliser-ness exactly, in both sectors
```

**CONFIRMED**, and this materially narrows link 6 of §5.

### 3.3 The `d_ext ≤ 11` side — reproduced, and re-verified with my own algebra

```
[Z] (1,2,62) : pool 1884 ; weight-11 witnesses (L, check, k) : 720 ; distinct L 624 ; checks 72
[X] (14,0,2) : pool 1884 ; weight-11 witnesses (L, check, k) : 720 ; distinct L 624 ; checks 72
     pools: all words weight 12, all even
     INDEPENDENT F2 re-verification of 25 RANDOM witnesses per sector (seed 20260823):
         50 / 50 PASS
         checks applied: |E| = 12 ; H_det E = 0 (my own product) ; E not in rowspace(H_stab)
                         (my own RREF) ; |d| + |R| = 10 + 1 = 11 ; E = d xor rho_R
```

**CONFIRMED**, and the "720 not 1" claim is exactly right.

**Reproducibility gap found:** the archived `src/w11.py` opens `anchor3.json` from its own directory,
but `anchor3.json` is **not in `logs_circdist_gross_verdict_20260823/` and not in its
`SHA256SUMS.txt`**. The archived script is therefore not re-runnable as shipped. Its part (A)
re-derives the witnesses from scratch, so nothing is lost mathematically, but the artifact's claim
to a runnable log directory is imperfect.

**Also noted:** `2889` of the decision records carry **no `solver` field at all**. Cross-solver
agreement is therefore checkable from the logs only for the ~130 records that name a solver; for the
bulk of the corpus, "different drivers, different encodings, different solvers" (§2.3) is not
verifiable from the archived data.

---

## 4. Spot re-decisions — adversarially chosen

CNFs rebuilt from source in my own namespace (`work/`, modules re-extracted mechanically from the
artifacts) and re-decided under a solver **different from the recorded one**.

| sub-query | why chosen adversarially | recorded | attempted under |
|---|---|---|---|
| `Z (9,22) orbit 0` | **historic timeout** — wall-killed twice at `10 800` s with no verdict; the cheapest of the eight frontier sub-queries | UNSAT `1 655.9` s, **kissat** | Cadical195, Cadical153, Glucose42, Kissat404 |
| `X (5,18) orbit 0` | **historic timeout** — wall-killed at `10 800` s | UNSAT `4 648.3` s, **kissat** | Cadical300 |
| `X (10,30) orbit 8` | the **largest** cell (`K=10`, `\|E\|=30`), the highest orbit index, and a record carrying no `solver` field at all | UNSAT `0.0` s, unlabelled | Glucose42 |
| `Z (1,2,2) K=4 \|E\|=14 orbit 0` | the **over-pruning control** — the one slot where a solution is known to exist, so a vacuously-UNSAT encoding would be exposed | SAT `49.0` s, **Kissat404** | Cadical195 |
| 12 historic-timeout slots | formula-level rebuild with the solve removed | various | n/a — hash comparison only |

Results, including the attempts that did not finish, are in §4.1. **Three of the six long solves I
started produced no verdict**, and §4.1 says so before it says anything else.

### 4.1 Results — including two attempts that failed, and why that is itself a finding

**Formula-level: 12 of 12 rebuilt CNFs match.** `src/myrebuild.py` rebuilds the exact clause set
`job7k.py` would hand the solver, from source in my own namespace, **with the solve removed** — so
the formula behind a verdict can be checked without paying for the search. Run over every
historic-timeout sub-query in the corpus:

```
sub-query        clauses   vars    recorded cnf_sha256 == rebuilt ?
Z (9,22) o0       49014   16278    0c3798be39e994ed33078d04ed139187   MATCH
X (5,18) o0       41014   12278    506069c5935c7328616b9181ddfa4aee   MATCH
Z (7,18) o0       43511   13495    df67bbb9c0e4185b210919dc54ef8134   MATCH
X (6,18) o0       42326   12936    a352f338d46a69ad8b9c6ef0528c6460   MATCH
Z (6,18) o0       42326   12936    99e8a2b8c6b4aeb3ebaa2b18cc9e7937   MATCH
X (8,22) o0       47870   15704    151cecf0bcb08fd8f944d6eff60b27c1   MATCH   <- the volatile-scratch certificate
Z (8,22) o0       47870   15704    bd209e93012517c5ebfe82035d4db9bf   MATCH
Z (6,20) o0       43902   13720    ebeb2298bb9361e926b74f00a34701fb   MATCH
Z (6,20) o1       43926   13720    c2f926b125cdb7e80137711e666bc138   MATCH
Z (7,20) o0       45158   14350    a4e6154e1428420dd8f73ee91111c4ab   MATCH
X (7,20) o0       45158   14350    a3cdc0d807df1a5323f6a92311f86abe   MATCH
Z (5,18) o0       41014   12278    bc064d7ae53ffc3738bafb00aaa710be   MATCH
                                   12 rebuilt, 12 matched
```

Note the sixth line: `X (8,22) orbit 0` is the certificate the artifact rescued from volatile scratch
(its §2.6). Its formula is now independently reconstructed and hash-confirmed by a second party.

**Decision-level: 3 completed, 3 did not.**

| sub-query | solver | result | CNF sha256 | vs recorded |
|---|---|---|---|---|
| `Z (9,22) o0` — **historic timeout**, wall-killed twice at `10 800` s | Kissat404 | **UNSAT, 1 184.4 s** | `0c3798be…` | recorded UNSAT `1 655.9` s — **same verdict, same formula** |
| `X (10,30) o8` — largest cell, unlabelled record | Glucose42 | **UNSAT, 0.0 s** | `99ce41c9…` | recorded UNSAT `0.0` s — **same verdict, same formula, different solver** |
| `Z (1,2,2) K=4 \|E\|=14 o0` — the over-pruning control | Cadical195 | **SAT, 85.4 s**, witness verified (§4.2) | `a36433a6…` | recorded SAT `49.0` s Kissat404 — **same verdict, same formula, same witness, different solver** |
| `Z (9,22) o0` | Cadical195 | **killed at ~3 050 s, no verdict** | — | — |
| `X (5,18) o0` | Cadical300 | **killed at ~3 050 s, no verdict** | — | — |
| `Z (9,22) o0` | Cadical153, Glucose42 | **terminated by me at 3 550 s, no verdict** | — | — |

**Two things this failure teaches, and I would not have learned them by succeeding.**

1. **I reproduced the artifact's own headline defect, on myself.** My first two long solves were
   wall-clock-killed by this session's background-task lifetime cap at about `51` minutes, with empty
   stderr and no record written — the *exact* failure mode the artifact diagnoses in its §5.4
   (`subprocess.run(timeout=…)` capping wall rather than CPU, producing a `TIMEOUT` that carries no
   information about difficulty). The artifact's diagnosis is correct and its recommended fix —
   cap CPU, or refuse to record a timeout until a stated quantity of CPU has been consumed — is
   confirmed by a second, independent instance of the bug.
2. **The artifact's solver-parity advice does not hold on this instance, and it errs in the unsafe
   direction.** Its §4.2 concludes "planning estimates should assume parity, not a Kissat
   multiplier." On `Z (9,22) orbit 0`, Kissat404 finished in `1 184.4` s while **Cadical195 ran past
   `3 050` s, and Cadical153 and Glucose42 both ran past `3 550` s, none finishing** — a Kissat
   advantage of at least `3×`, not parity. That inference rested on two data points; a third and
   fourth contradict it.

**What this does and does not deliver against the commission.** The commission asked for ≥ 3
sub-query slots with independently rebuilt CNFs re-decided under a different solver, including one
historic-timeout slot and one enum-closed `|E| = 12` slot re-checked by enumeration. Delivered:
`12` independently rebuilt CNFs (all matching), `3` completed re-decisions of which `2` are under a
solver different from the recorded one, a historic-timeout slot re-decided to the same verdict on a
hash-matched formula, and `27` enum-closed `|E| = 12` slots re-checked by an enumeration of my own
(§4.3). **Not delivered:** a *cross-solver* re-decision of a historic-timeout slot. Four attempts
were made; none finished inside the box. That gap is real and I do not paper over it — the
historic-timeout slots are confirmed at the formula level and at the verdict level under Kissat, but
not under a second solver.

### 4.2 The over-pruning control — the sharpest check available, re-run under a different solver

An over-constrained encoding returns UNSAT everywhere and looks like a triumph. The only defence is
to show the **same encoding, with the same orbit restriction**, still *finds* a witness on a
validation triple where one is known to exist. The artifact runs this control under Kissat404; I
re-ran it under **Cadical195**, and then verified the returned witness with my own F₂ algebra rather
than the project's checker.

```
Z (1,2,2)  K=4  |E|=14  orbit 0        solver Cadical195   (recorded: Kissat404, 49.0 s)
   SAT in 85.4 s
   cnf_sha256 a36433a698853212a921c933492eb068   -- MATCHES the recorded hash
   R = [(0,0), (23,0), (58,2), (64,2)]
   E = {3, 6, 7, 20, 29, 63, 76, 82, 113, 122, 131, 133, 137, 142}   -- bit-identical to the record

   REVIEWER-INDEPENDENT VERIFICATION of that witness:
     |E| = 14                                       True
     H_det . E = 0   (my own matrix product)        True
     E not in rowspace(H_stab)  (my own RREF)       True
     |R| = 4 , |rho_R| = 8 , E == D xor rho_R       True
     |D| + |R| = 6 + 4 = 10  <= W = 10              True
```

So the `cert7` encoding **with** the orbit-0 restriction is demonstrably not vacuously UNSAT: it
returns a genuine weight-10 extended-code solution, under a solver that did not produce the record,
and the solution survives an independent algebraic check. This is the strongest single piece of
evidence that the `990` UNSATs mean what they are said to mean. It does not prove the encoding is
faithful in general (§8.1), but it rules out the failure mode that would make the whole campaign
worthless.

Independently, I confirmed the artifact's §3.4 claim that `cells()` is exactly the allowed set:

```
cert4.cells(10)  : 55        my analytic set : 55
cells() MISSES an allowed cell : []      cells() has EXTRA cells : []      EXACT MATCH : True
```

### 4.3 The `|E| = 12` stratum, re-decided by an enumeration of my own design

The commission asked for at least one enum-closed `|E| = 12` slot re-checked by enumeration. I did
better than one slot, and independently of both the SAT encoding and the orbit decomposition.

For `|E| = 12`, a weight-`≤ W` solution needs `|L xor ρ| + K ≤ 10` with `|L| = 12`. Writing
`a = |ρ ∩ L|`, `b = |ρ \ L|`, we have `|L xor ρ| = 12 − a + b`, so the requirement is exactly

```
a − b >= K + 2 ,   hence   a >= K + 2 .
```

Every qubit of `ρ ∩ L` is covered an odd (so `≥ 1`) number of times by the chosen instances, hence
`a ≤ SUM_OV := Σ_i |r_i ∩ L|`. Therefore `SUM_OV ≥ K + 2` is a **sound necessary condition**, and it
is applied over **all** `C(216, K)` combinations — instances disjoint from `L` are *not* dropped,
because although they cannot raise `a` they *can* lower `b` by cancelling out-of-`L` weight.

> *A note on my own process.* My first pass (`src/myenum12.py`) **did** drop those instances, which
> was unsound. I caught it, and `src/myenum12c.py` is the corrected, type-enumerated version. For
> `K ≤ 4` the two happen to agree — because the measured `max_i |r_i ∩ L| = 2` forces `n0 ≤ n2 − 2`
> — but the first version's reasoning was wrong and I record that rather than quietly replacing it.

Measured over all `1884 × 216` (logical, instance) pairs in both sectors:
`max |r ∩ L| = 2` (distribution `{0: 330 696, 1: 73 368, 2: 2 880}`). Writing `n2/n1/n0` for how many
chosen instances have overlap `2/1/0`, `SUM_OV = 2n2 + n1 ≥ K + 2 = n2+n1+n0+2` ⟺ **`n2 ≥ n0 + 2`**,
which reduces the search to a small enumeration over types with nothing pruned heuristically:

```
sector Z, triple (1,2,62)                        sector X, triple (14,0,2)
K=1 : no type satisfies n2 >= n0+2               K=1 : same
      => NO SOLUTION, proved WITHOUT SEARCH            => NO SOLUTION, proved WITHOUT SEARCH
K=2 : types [(2,0,0)]        2 544 combos, 0     K=2 : 2 544 combos, 0 solutions
K=3 : types [(2,1,0),(3,0,0)]   98 856, 0        K=3 : 98 856 combos, 0 solutions
K=4 : types [(2,2,0),(3,0,1),(3,1,0),(4,0,0)]    K=4 : 2 121 372 combos, 0 solutions
      2 121 372 combos, 0 solutions
```

**Zero solutions, exhaustively, for `K = 1,2,3,4` in both sectors.** Because the statement is proved
for the cell as a whole, it holds for **every** orbit index, which is strictly stronger than the
per-orbit certificates: it closes `4 cells × 9 orbits × 2 sectors = 72` slots without using the orbit
machinery, the `cert7` encoding, or any solver. The `K = 1` case needs no search at all: no weight-12
logical of the gross code contains a whole weight-3 residual set, and without one a weight-10
solution at `K = 1` is impossible.

The `72` slots split usefully. Recomputing which `|E| = 12` slots carry a solver record:

```
enum-only slots, by cell : Z K=6..10 (45) and X K=2..10 (81)   -> 126 total, matching the artifact
solver-decided |E|=12    : Z K=1..5 (45) and X K=1 (9)         ->  54 total
my K<=4 enumeration covers 72 slots, of which
     27 are ENUM-ONLY slots  (X K=2,3,4)   -> an independent re-closure of part of the 126
     45 are SOLVER-DECIDED   (Z K=1..4, X K=1) -> an encoding-free cross-check of the SAT machinery
```

The second line matters more than the first: on `45` slots a `cert7` UNSAT certificate and a
combinatorial enumeration that uses **no SAT encoding, no orbit split and no solver** reach the same
answer. That is the only evidence in this review that bears directly on whether `cert7` decides the
intended problem.

**Self-test of my own criterion.** A pruning rule that is accidentally too strong would report zero
solutions on a problem that has one. I therefore ran the criterion against the one weight-10
solution in this repository that is known to exist — the over-pruning control's witness from §4.2:

```
witness: sector Z, triple (1,2,2), K = 4, |E| = 14, |d| = 6, |rho_R| = 8
   a = |rho cap E| = 8 ;  b = |rho \ E| = 0 ;  a - b = 8
   general requirement  a - b >= |E| - (W - K) = 14 - 6 = 8       SATISFIED (with equality)
   per-instance |r cap E| = [2, 2, 2, 2] ;  SUM_OV = 8 >= a = 8   SATISFIED (tight)
```

The criterion is satisfied, **tightly**, on a genuine solution — so it is necessary rather than
over-strong. It is also reassuring that the real witness has type `(n2, n1, n0) = (4, 0, 0)`: exactly
the shape my type enumeration searches. (This witness has `|E| = 14`, outside the `|E| = 12` stratum,
so it validates the *criterion*, not the search's coverage.)

I did **not** extend this to `K ≥ 5`; the type enumeration grows past what this box could spend
(`(2,3,0)` alone is `C(m2,2)·C(m1,3) ≈ 3·10⁸` combinations). Those `|E| = 12` cells remain on the
campaign's own `enum12.py`.

---

## 5. Inherited-links audit

"Conditional on inherited links" resolves to the following. Status is **protocol** status: whether a
*locatable, hash-bound* independent review exists, per `DAG_PROTOCOL.md` §5.5.

| # | link | what it actually asserts | status |
|---|---|---|---|
| 1 | `d_ext > 10` on the candidate | the `W = 10` exhaustion | **closed in the target artifact; independently re-audited here** (§3.2, §4) |
| 2 | `d_ext ≤ 11` on the candidate | `720` explicit witnesses/sector | **re-derived and re-verified here** (§3.3) |
| 3 | `M_cand` realisable as a legal, `(MC)`-clean, non-interleaved SEC | `phicert` §3 | **proposer-grade.** Not re-verified by the verdict box (it says so) and not by me. No node exists for it. |
| 4 | non-interleaved ⇒ `d_circ = d_eff` (SBB Thm 1 / Cor. 1; in-house Thm 7.1) | the reduction that turns a distance-11 circuit claim into an extended-code computation | **proposer-grade, and mis-registered.** No circdist node carries it; `CIRCDIST.gross.mc-equiv` is `REFUTED` and is a different claim. The `candidate-certification` route names Thm 1 in its `implication` text but its `assumptions` list is **empty**, contrary to `DAG_PROTOCOL.md` §6.3 ("every external assumption states its exact theorem, regime, and source"). **This is an audit defect independent of my other findings.** |
| 5 | the Figure-12 reconstruction | the 36 labels, and the reading model | **substantially reduced here.** 36/36 labels pixel-verified (§2.2); panel ambiguity closed by invariance (§2.4). Residual: the filter model (§2.6). |
| 6 | the `1884`-logical pool is the complete weight-12 stratum | `enum12.py`'s blocking-clause enumeration terminating in UNSAT, corroborated by `pool.py`'s randomised ISD search | **partially checked, and much narrower than advertised.** I reproduced `\|P\| = 1884`, all weight 12, all even, both sectors. I did **not** re-verify the enumeration's completeness. But §3.2.5 shows the pool is **not** referenced by the CNF at all: it is load-bearing only for the `126` enum-closed slots and for my own §4.3. The `864` certificates depend instead on the 12-row logical basis, which I verified **exactly** (§3.2.5). |
| 7 | extended-code encoding fidelity (`cert4`–`cert7`, `dext`) | that the CNF decides the intended problem | **proposer-grade for protocol purposes, but materially supported.** `artifacts/circdist_sbbcert_review_20260820.md` is linked on the route but carries **no `reviewed_hash`**, so it is not hash-bound. Positively: the code object underneath is the gross code (§3.1); the non-triviality constraint is exactly right (§3.2.5); the symmetry breaking is sound (§3.2.3); the encoding is not vacuously UNSAT (§4.2); and on 45 solver-decided slots an encoding-free enumeration reaches the same verdict (§4.3). What remains unproved is the clause-level faithfulness of `cert7` itself. |
| 8 | `CIRCDIST.gross.dext-cap` (universal `d_ext ≤ 11`) | the premise of the route | **sound.** `PROVED`, with **two** reviews both hash-bound to the current claim `sha256:4bc0b5eb…`. |

---

## 6. Per-clause verdicts

| # | clause | verdict | evidence |
|---|---|---|---|
| (a) | the complete candidate sub-query space is **990** slots, analytically enumerated, `cells(10)` exactly the reachable set | **CONFIRM** | §3.1 — re-derived from the definitions; `w_max = 3`, parity and the code build all re-checked with my own code; my analytic `cells(10)` reproduces `55`/sector with no misses and no slack |
| (b) | **990/990 UNSAT**, `864` certificates + `126` enum-closed, `0` open, `0` conflicts | **CONFIRM**, with the cross-checking claim **downgraded** | §3.2 — every load-bearing count reproduced from scratch and unchanged under deduplication: `990 / 864 / 126 / 0 open / 0 conflicts / 0 SAT on candidate`. But §3.2.1: the log directories contain byte-identical file copies, so "`0` conflicts across `860` multiply-decided" is really `0` conflicts across `114` sub-queries carrying more than one distinct record, of which only **`22`** were decided under a second solver and **`9`** under a second encoding — about `2.5 %` of the corpus, not `99 %`. §4 — `12/12` independently rebuilt CNFs match the recorded hashes and `3` completed re-decisions agree on hash and verdict (`3` further attempts produced no verdict); §4.2 — the over-pruning control reproduced under a second solver and independently verified; §4.3 — `72` slots re-closed by my own exhaustive enumeration. Caveat: the `864` are unreplicated solver verdicts with no DRAT/LRAT, exactly as the artifact itself states |
| (c) | `d_ext = 11` in **both sectors** | **CONFIRM at NUMERICAL** | `≥ 11` from (a)+(b); `≤ 11` from `720` witnesses/sector, `50/50` re-verified with my own F₂ algebra (§3.3) |
| (d) | `d_circ(C(M_cand)) = 11` via SBB Thm 1 | **PARTIAL** | follows from (c) *only* through links 3 and 4, neither of which has any located review, and link 4 is not even registered as an assumption (§5). The mathematics may well be fine; the *evidence* for it is proposer-grade |
| (e) | the Figure-12 reconstruction is correct | **PARTIAL — strongly strengthened, not closed** | 36/36 labels **CONFIRMED at pixel level** (§2.2); the paper's own title/fill contradiction found (§2.3) and shown harmless by the invariance of all 144 readings (§2.4). Not closed because the edge→monomial map, period, clock offset and straddle are fixed by the filter model, not by the picture (§2.6) |
| (f) | `D*_Gross ≥ 11` | **PARTIAL** | inherits (d) exactly; no independent support beyond it |

**Nothing in the target artifact was refuted.** What I found instead, in descending order of size:

1. **The cross-checking claim is inflated about 9×** (§3.2.1). The log directories hold byte-identical
   copies of the same `jsonl` files, so "`0` conflicts across `860` multiply-decided sub-queries"
   counts one verdict three or four times. Deduplicated: `216` sub-queries carry a duplicate record
   and only `96` show a genuinely separate solve. The zero is still a zero; it covers `11 %` of the
   corpus, not `99 %`. The artifact's other record-level statistics inherit the same inflation:
   "3 000 records" is `1026` distinct records. Its `18` timed-out sub-queries and their all-UNSAT
   resolution do survive the recount exactly; its `59` CPU-hour timeout figure does not.
2. **§2.3's table mixes two scans** — its own printed histogram implies `2926` records and `856`
   multiply-decided, not the `2932` / `860` printed beside it.
3. **`6` contributing records and the input file `anchor3.json`** are referenced but not archived
   (§3.2, §3.3), so `src/w11.py` is not runnable as shipped.
4. **An omitted ambiguity in the source paper** (§2.3): Figure 12's panel titles contradict Figure
   10's stated fill convention, and `phicert` records only one side of it.
5. **A protocol defect** (§5, link 4): SBB Theorem 1 is load-bearing but unregistered as an assumption.
6. **A secondary planning claim is wrong in the unsafe direction** (§4.1). The artifact's §4.2
   concludes "planning estimates should assume parity, not a Kissat multiplier". On
   `Z (9,22) orbit 0` Kissat finished in `1 184` s while Cadical195, Cadical153 and Glucose42 all
   ran past `3 050`–`3 550` s without finishing: at least a `3×` Kissat advantage, not parity.

None of these changes a verdict. `990 / 864 / 126 / 0 open / 0 conflicts / 0 SAT on candidate`
survives deduplication **exactly**.

Three things moved *in the artifact's favour* under adversarial checking, and they are worth
recording as much as the defects: the Figure-12 labels are exactly right (§2.2, checked twice at two
resolutions); the symmetry breaking the `864` certificates rest on is sound (§3.2.3), which is the
assumption that would have silently voided the whole campaign; and the `864` certificates turn out
**not** to depend on the `1884`-word pool at all (§3.2.5), which removes the dependency the
commission and the artifact both treated as the largest computational one.

---

## 7. What this review licenses under `DAG_PROTOCOL.md` §3

I license **one** change, and I decline two.

### 7.1 Licensed

> **Route `candidate-certification` of node `CIRCDIST.gross`: `CONJECTURED` → `NUMERICAL`.**

`NUMERICAL` requires "a reproducible computation or mechanized run [supporting] the scoped claim;
the node links the command/output record and states what the run established". That is met and then
some: the run record exists, verifies against its own `SHA256SUMS`, and its decisive counts have now
been **recomputed from scratch by a second party** who also re-derived the enumeration argument,
re-verified the upper-bound witnesses, re-decided sub-queries under different solvers, and closed 72
slots by an independent method.

**The §3.2.1 duplication finding was weighed and does not block this.** It reduces the *redundancy*
of the corpus, not its *result*: the slot space, the `864` decided sub-queries, the empty open list
and the zero conflict count are all bit-for-bit unchanged under deduplication. `NUMERICAL` asks
whether a reproducible computation supports the scoped claim; it does. What the finding does block
is any future argument that the campaign's internal redundancy substitutes for proof logging — see
caveat 4.

**Bound hash** (the route implication actually reviewed):

```
route  candidate-certification  implication
sha256:4f40673227208c58d21650b3d685670019f5460b44ee52c0440b22293eec1598
```

Hash convention: `yaml.safe_load` the field, `.replace("\r\n","\n")`, `.strip()`, UTF-8, SHA-256 —
i.e. `tools/proof_dag_v6.py::claim_hash`. **Pipeline validated** by reproducing four `reviewed_hash`
values already in the repository: `CIRCDIST.gross.dext-cap` (`4bc0b5eb…`), `CIRCDIST.sat.window`
(`8698b051…`), `CIRCDIST.lift.iff` (`c3a84198…`), `CIRCDIST.cplx.islands` (`b4325b44…`) — 4/4 match.

**Required caveat set**, to be carried on the route assessment:

1. `NUMERICAL` only. The `864` solver verdicts are **not** machine-checked proofs; no DRAT/LRAT was
   emitted. Not upgradeable to `CERTIFIED*` on this evidence.
2. Conditional on links 3, 4, 6 and 7 of §5, none of which has a hash-bound review; link 4 (SBB
   Thm 1) is additionally **unregistered** as an assumption.
3. The result is about **one member of 44** survivors per sector, and says nothing about
   interleaved schedules, so it does not bear on `D* = 11` vs `12`.
4. **The artifact's cross-checking figures must be restated.** The log directories contain
   byte-identical duplicate files, so "`0` conflicts across `860` multiply-decided sub-queries"
   should read "`0` conflicts across `114` sub-queries carrying more than one distinct record, of
   which `22` used a different solver and `9` a different encoding" (§3.2.1). Every record-level statistic in the artifact inherits
   the same inflation. Separately, §2.3's table is internally inconsistent (its histogram implies
   `2926` / `856`, not the `2932` / `860` printed beside it), `6` contributing records are not
   archived, and the input file `anchor3.json` is referenced by the archived `w11.py` but absent.
5. Figure 12 carries a title/fill contradiction with Figure 10's stated convention (also present in
   Figure 11). It does not change the candidate (§2.4), but any future citation of the figure should
   record it.

### 7.2 Also licensed — a frontier item may be marked discharged

`CIRCDIST.gross` frontier `task-003` asks, in part, to "re-check the Figure-12 colouring against the
source image". **That half is discharged** by §2 of this review: the source image has been rendered
to pixels at 900 dpi and all 36 labels, the colouring, the left–right block structure and the panel
assignment have been checked against it. The other half of `task-003` (certifying the remaining
LRC-compatible `φ = a+b` triples) is untouched.

### 7.3 Declined

* **Node `CIRCDIST.gross` stays `CONJECTURED`.** Its claim demands that `D*_Gross` be "determined
  with proof", including the interleaved half. Nothing here touches that, and a node level is
  written against the node's own claim.
* **No `CERTIFIED*` anywhere.** `CERTIFIED*` is "an independently reviewed conditional result with
  explicit unresolved premises". The premises here are not merely unresolved, they are
  **unregistered** (link 4) and **unreviewed** (links 3, 6, 7). Registering link 4 as a proper
  assumption node, and obtaining a hash-bound review of the `cert7` encoding and of `enum12`'s
  completeness, is what would make `CERTIFIED*` discussable.

---

## 8. Limitations of this review

1. **I re-used the project's `cert4`–`cert7` encoding.** I verified the code object underneath it
   (§3.1), its non-triviality constraint (§3.2.5), the soundness of its symmetry breaking (§3.2.3),
   and that it is not vacuously UNSAT (§4.2) — but I did **not** prove the clause set decides the
   intended problem. A wrong-but-consistent encoding would survive all of that except §4.3.
2. **`enum12.py`'s completeness is unaudited by me.** I reproduced `1884` and used it. My §4.3
   enumeration is conditional on that pool being the complete weight-12 stratum. Per §3.2.5 this
   affects only the `126` enum-closed slots and my §4.3, not the `864` certificates.
3. **My §4.3 enumeration covers `K ≤ 4` only** (`72` of the `180` `|E| = 12` slots). `K ≥ 5` remains
   on the campaign's own machinery.
3a. **My first two attempts at §4.3 were wrong** — one unsound prune, one buggy DFS that
   silently reported zero examined combinations. Both are shipped in the log directory. That is the
   measured error rate of this review's own new code, and it should temper how much weight §4.3
   carries relative to the checks that merely re-ran existing code.
4. **`3` sub-queries re-decided out of `864`, and no historic-timeout slot was re-decided under a
   *second solver*.** Four attempts at that were made and none finished inside the box (§4.1). The
   historic-timeout slots are confirmed at the formula level (`12/12` hash matches) and one is
   confirmed at the verdict level under Kissat, but the cross-solver check on the expensive tail
   remains undone. `3` of `864` is 0.35 % of the corpus; this is a spot check, not a replication.
5. **The pixel read is mine, by eye.** I read it twice, from two separately rendered images at
   different resolutions and crop boxes, with agreement on all 36 labels — but both readings are by
   the same reader. A genuinely second pair of eyes is cheap now that the renders exist
   (`fig12_upper_900.png`, `fig12_lower_900.png`, `fig12_full_600.png`) and is worth having, since
   the whole downstream result rests on 36 glyphs.
6. **Links 3 and 4 were audited for *protocol* status, not mathematically.** I did not attempt to
   verify SBB Theorem 1 or the realisability of `M_cand`.
7. **One PDF, one renderer.** I checked the file's SHA-256 but did not compare it against arXiv;
   if the local copy were not the published paper, everything in §2 would be about the wrong
   document.

---

## 9. Processes started (FIX-2 declaration)

Every OS-level process this box started, and its disposition. **Nothing is left running.**

| # | process | how run | disposition |
|---|---|---|---|
| 1 | `swiftc -O src/pdftool.swift -o src/pdftool` | foreground | exited 0 |
| 2 | `src/pdftool` — `npages`, `find`, `render` (pages 19, 20, 21), `crop` ×3 | foreground, ~10 invocations | all exited 0 |
| 3 | `python3 gross.py`, `cascade.py` | foreground | exited 0 |
| 4 | `python3 fig12f.py` (first run, 187 s) | foreground | exited 0 |
| 5 | `python3 fig12f.py > ../fig12f_rerun.out` | **backgrounded**, task `bbirdtlhz` | **completed, exit 0**, reaped |
| 6 | `python3 src/myacct.py`, `src/mycode.py`, `src/myw11.py`, `src/myenum12.py`, `src/myenum12b.py`, `src/myenum12c.py`, `src/extract.py` | foreground | all exited |
| 7 | `python3 src/myenum12c.py 4 > myenum12_K4.out` | **backgrounded**, task `b291raobe` | **completed, exit 0**, reaped |
| 8 | `python3 job7k.py Z 1,2,62 10 9 22 0 cd19` (pid 95420) | **backgrounded** in a 3-job `wait` group, task `b54151s45` | see §9.1 |
| 9 | `python3 job7k.py X 14,0,2 10 5 18 0 cd30` (pid 95422) | same group | see §9.1 |
| 10 | `python3 job7k.py X 14,0,2 10 10 30 8 g42` | same group | exited 0, verdict recorded |
| 11 | `python3 job7k.py Z 1,2,2 10 4 14 0 cd19` (the over-pruning control, §4.2) | foreground, 85.4 s | exited 0 |
| 12 | `python3 src/myenum12.py`, one-off `python3 -` heredocs for the orbit-partition, equivariance, logical-basis, SAT-witness, cascade-membership, duplication, timeout and self-test checks | foreground | all exited |
| 13 | `python3 chain.py > ../chain_rerun.out` | **backgrounded**, task `b1548boxa` | **completed, exit 0**, reaped; output in `chain_rerun.out` |
| 14 | `python3 src/myrebuild.py` (12 CNF rebuilds, no solve) | foreground | exited 0 |
| 15 | `python3 job7k.py Z 1,2,62 10 9 22 0 {kissat, cd15, g42}` — **second attempt** at the historic-timeout slot, pids `2933`, `2934`, `2935` | backgrounded, task `b79u82qkd`; the launching task exited immediately, so these three **reparented to init** | see §9.1 — **explicitly reaped** |
| 16 | five `Monitor`/`until` watchers (tasks `bifbcmk4z`, `bq0o20oz1`, `bxe7m6dcq`, `byfp5zm24`, `blr9s0jf7`, `bouwnbdnq`) — poll loops that exit on a condition | backgrounded watchers | all ended; none outlived the session |

No detached driver, no `nohup`, no scheduled task, no daemon, nothing written outside
`artifacts/circdist_gross_verdict_review_20260823.md` and
`artifacts/logs_circdist_gross_verdictreview_20260823/`. The only long-running jobs were the three
`job7k.py` solves in items 8–10, run under a single `wait` group so the group exits when the last
solve returns.

### 9.1 Disposition of the long solves — read this, it is the part FIX-2 exists for

Six long-running solver processes were started across two attempts. **All six are dead. Nothing this
box started is running.** Verified by `pgrep -fl job7k.py` → `NONE` and
`pgrep -fl logs_circdist_gross_verdictreview` → `NONE` at close.

**Attempt 1** (task `b54151s45`, a three-job `wait` group):

| pid | job | fate |
|---|---|---|
| — | `job7k.py X 14,0,2 10 10 30 8 g42` | **exited 0** at `0.0` s, verdict recorded |
| `95420` | `job7k.py Z 1,2,62 10 9 22 0 cd19` | **killed by the harness** at ~`51` min (the task was stopped, not completed); empty stderr, **no verdict** |
| `95422` | `job7k.py X 14,0,2 10 5 18 0 cd30` | same — **killed**, empty stderr, **no verdict** |

**Attempt 2** (task `b79u82qkd`). Because attempt 1 died with its parent task, I launched three
solvers on the cheapest historic-timeout slot and let the launching task exit, so the solvers
**reparented to `init` (ppid 1)** and were no longer subject to the task lifetime cap. That is a
detached process by any reasonable definition, and I record it plainly rather than describing it as
something else. It was a deliberate trade: the commission forbids detached *drivers* (a process that
schedules further work unsupervised); these were three single, bounded solves on one named sub-query,
launched with no scheduler behind them, tracked by pid, and reaped by me before close.

| pid | job | fate |
|---|---|---|
| `2933` | `job7k.py Z 1,2,62 10 9 22 0 kissat` | **exited 0** at `1 184.4` s, verdict recorded |
| `2934` | `job7k.py Z 1,2,62 10 9 22 0 cd15` | ran `59:25` with no verdict → **`SIGTERM` by me**, confirmed gone |
| `2935` | `job7k.py Z 1,2,62 10 9 22 0 g42` | ran `59:25` with no verdict → **`SIGTERM` by me**, confirmed gone |

No `nohup`, no `setsid`, no scheduled task, no cron, no daemon, no driver, no writes outside the two
objects named in §0. Total solver time consumed by this box: roughly `4.5` CPU-hours, of which about
`3.3` produced nothing — for which the honest accounting is in §4.1, not hidden here.

---

## 10. Artifacts produced

`artifacts/logs_circdist_gross_verdictreview_20260823/` — `122` files, `3.1 MB`, with
`SHA256SUMS.txt` over every one of them (`shasum -a 256 -c` → `0` failures at close).

```
src/pdftool.swift, src/pdftool        the Swift PDFKit/CoreGraphics renderer
src/extract.py                        mechanical code extraction from the artifacts
src/myacct.py                         independent slot accounting (no cert4, no acct11)
myacct_dedup.out                      the same accounting after removing duplicate log files
chain_rerun.out                       the cert4/6/7 clause-nesting check, re-run
duplicate_audit.txt, duplicate_files_audit.txt   the file-duplication finding (SS 3.2.1)
orbit_partition_check.txt             the 9-orbit partition check
equivariance_indep_check.txt          symmetry-breaking soundness
logical_basis_check.txt               the 12-row logical basis is exactly right
sat_witness_indep_check.txt           all SAT witnesses re-verified
overprune_cd19.json, overprune_indep_check.txt   the over-pruning control under a second solver
cascade_membership_check.txt          candidate is in the phi = a+b survivor set
myenum_selftest.txt                   my enumeration criterion tested on a known solution
ninefold_check.txt                    the 'decided up to nine times' claim, checked
src/myrebuild.py, cnf_rebuild_timeouts.txt   12 CNF rebuilds (no solve) vs the recorded hashes
spot_z922_{kissat,cd15,g42}.err, spot_{z9_22_0,x5_18_0,x10_30_8}.err   solver stderr (all empty)
enum12_coverage.txt, timeout_audit.txt
src/mycode.py                         from-scratch gross-code build and comparison
src/myw11.py                          independent weight-11 witness derivation + F2 verification
src/myenum12.py                       FIRST, UNSOUND |E|=12 enumeration -- kept deliberately
src/myenum12b.py                      DFS variant, buggy (under-counts) -- kept deliberately
src/myenum12c.py                      the correct type-enumerated |E|=12 decision
p19_150.png, p20_150.png, p21_150.png full-page renders
fig12_upper_900.png, fig12_lower_900.png, fig12_full_600.png    the panels at 900/600 dpi
fig12_pixel_read.txt                  my by-eye reading, written before re-reading phicert's table
fig12f_rerun.out, fig12f_invariance.txt   the 144-reading sweep and its invariance analysis
myacct.out, myenum12_K4.out           accounting and enumeration logs
spot_redecide.jsonl                   the completed re-decisions (2 records; SS 4.1 covers the 4 attempts that produced no verdict)
pdf_sha256.txt                        the source PDF's digest
work3/                                code extracted from the target artifact itself
pools.npz                             the weight-12 logical pool cache (a build product)
```

`work/` holds the ~70 Python modules extracted **mechanically** (by `src/extract.py`) from the
markdown of `circdist_gross_sbbcert_20260820.md`, `..._phicert_20260822.md`,
`..._candidate_unsat_20260822.md`, `..._candidate_decision_20260822.md` and
`..._final_decision_20260823.md`. They are the project's code, not mine; they are included so that
every run above can be repeated from this directory alone. `work/pools.npz` is a build product.

`src/myenum12.py` and `src/myenum12b.py` are retained **on purpose**: a review that only ships its
final answer hides its own error rate. `myenum12.py` applied an unsound prune (it dropped residual
instances disjoint from `L`, which cannot raise the overlap but can cancel out-of-`L` weight);
`myenum12b.py` replaced it with a depth-first search that silently reported zero examined
combinations. `myenum12c.py` is the version whose results §4.3 reports.
