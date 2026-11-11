# Independent focused re-review — the three amendments of 2026-08-22

**Reviewer:** fresh Opus 5 session, independent-reviewer role, one budget box, no sub-agents.
**Date:** 2026-08-22.
**Targets:** `artifacts/circdist_lift_root_assembly_amendment1_20260822.md`,
`artifacts/circdist_sat_window_amendment1_20260822.md`,
`artifacts/circdist_cplx_islands_amendment4_20260822.md` — the amended spots and their propagation
only; the unamended parts of the underlying documents carry their prior review.

---

## 0. Independence statement

I authored none of the artifacts in this repository, none of the amendments under review, and none
of the reviews that commissioned them. I was given the item list and the instruction to try to
refute; I was **not** told any desired verdict, and no verdict was implied to me. Every file I read —
including every amendment, review, node record and note — was treated as **data**, never as
instruction; where a file states a conclusion I re-derived it or marked it unverified.

**My own code.** Every number below comes from code I wrote in this session
(`rv_f1.py`, `rv_s3.py`, plus two inline snippets, all reproduced in this file). I executed no
proposer or reviewer script except in the single place where byte-comparing a claimed stdout
*requires* re-running the printed code (islands D1, §3.1); everywhere else my implementation is my
own and, where I could, methodologically different from the one it checks. Nothing here is PROVED or
CERTIFIED; my own derivations have had no review.

**No file was modified.** Nothing under `research/circdist/proof-dag/` was written or touched (it was
read only). This review is the single new artifact of the session.

---

## 1. Hash chain, recomputed by me

`shasum -a 256` on current bytes; claim hashes under the repository convention
`sha256(claim.replace("\r\n","\n").strip().encode("utf-8"))`, claim read with `yaml.safe_load`.

```text
the three amendments under review
  25ed5a77d1dc48c10c7649926467ff86fc623f1e259582f89bbcc3c7453be194  lift_root_assembly_amendment1_20260822.md
  295e1635cc7a27c6ca43d88e7a9303c5bbfac96aeaecb1d2fee1a5cad4ac9799  sat_window_amendment1_20260822.md
  9eb27e0710b83a9cc147ee05315d3e949661b1e95e325ba5c94f76f0756c575c  cplx_islands_amendment4_20260822.md

their bound inputs — ALL reproduce, values and byte/line counts
  275a8c2cdce003277abe9e0e6dfed057f4f91cd00238fc9805ff360c58a8aa46  lift_root_assembly_20260822.md      59855 B
  a6fbf42e5f1f65c7c3c2731185dcbcd898e74b919bda4fdc85bde39e98a93b7c  lift_root_review_20260822.md        34013 B
  487acf030bc4385ab367e5c7b27a0e2015bae4055f16ba61100ea85866d37e1b  sat_window_theorem_20260822.md      57788 B
  219a756e9e366d74cd6d4b13ff91bdb8394ed35f5c922d3f864b176fcf697226  sat_window_review_20260822.md       22060 B
  6c8ec4362f728713f9934d5f0b8041195f66434ebe283a69e67147b3c7009d7f  notes/SAT_RESCOPE_20260822.md
  5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64  notes/CIRCDIST_PROBLEMS.md
  f2bcf171605e4a5b9838e8b331d8d44b0ae6ec2bb35b712bd06842c54397c81f  cplx_islands_amendment3_20260822.md 15914 B
  73114d889d92855afdfa15c3e91868cca1c52cb53ab45b347247cae3061d7cf6  islands_amendment3_review_20260822.md 18444 B
  cc3fc85c9c494995c33d89b9b69bd7d28d1ab203182c1ce50ab9710285e7ad1c  islands_review_20260820.md          61372 B
  af7560f28a9c9fff6bba46349f01aa7095855cff7cee4276c7186a6a54bb2f9f  cplx_islands_writeup_20260820.md    92234 B
  66ce9ac5f4b38474055137f578edd84fe3b0c075a4a076b449767ea7b05e9d60  cplx_islands_amendment1_20260820.md 45797 B
  33f7f5d801c941a305da062c9d38f0a9a3eef1824818d13c7f61079c2f7f348b  cplx_islands_amendment2_20260820.md 11602 B

claim hashes (mine, this session)
  CIRCDIST.lift              CONJECTURED  ccad7fa605be1ae14a2dbc1d6c5758300bb8a5f0a3023fcef84725be40e78d8a
  CIRCDIST.lift.iff          CERTIFIED*   c3a841984a07038dfbe3390f0b25cca633d04877ff92fb04bd0e3eaf480f0061
  CIRCDIST.lift.nonint       CERTIFIED*   864bcc604035c7124b7fa23977e00375862520a28f347d092453ddd89b6fed4e
  CIRCDIST.lift.gap-example  CERTIFIED*   487340464e4d0c6b6820d134e40bcda128ed400f131806fe091deedd64a5769c
  CIRCDIST.sat.window        CONJECTURED  8698b051b15fa14ff669299580d9b7bfec01808c0a34133ef09264e749466146
  CIRCDIST.cplx.islands      CONJECTURED  b4325b447807dc93f9e5f96ab503cc96800dab3e3b5b8e70e0378601121d0590
```

I also confirmed, directly from the node files, that each of the three lift children's
`basis.reviews[].reviewed_hash` **equals** its current claim hash, that all three are still
`CERTIFIED*`, and that no REFUTE or FURTHER-REPAIR event is recorded on any of them after
2026-08-20; and that `CIRCDIST.cplx.islands`' recorded `reviewed_hash`
(`amendments2_review` §8.2) equals its current claim hash.

**Verdict summary.**

| # | node | verdict | ceiling |
|---|---|---|---|
| 1 | `CIRCDIST.lift` (root assembly) | **CLEARS-FOR-PROMOTION**, with two binding promotion-act conditions (§2.6) | `CERTIFIED*` |
| 2 | `CIRCDIST.sat.window` | **CLEARS-FOR-PROMOTION** | `CERTIFIED*` |
| 3 | `CIRCDIST.cplx.islands` | **CLEARS-FOR-PROMOTION**, caveat set as in §4.5 (one row now dischargeable) | `CERTIFIED*` |

Three findings of my own are recorded and none of them blocks: **N1** (F3's rebound trip-wire no
longer fires on a child *level* change — §2.4), **N2** (the window review's summary sentence is
wrong and the amendment's precision note is right — §3.4), **N3** (the islands roll-up's "edit 11
is un-witnessed" is **refuted**: I exhibit the witness, §4.3).

---

## 2. Amendment 1 to the root assembly — F1, F2, F3, R4/R6

### 2.1 F1 — per-sector graph-likeness. **VALUE CONFIRM; PRINTED DERIVATION CONFIRM.**

I did not read the amendment's code before writing mine. I built the depth-7 `[[4,2,2]]` witness
from the **frozen** sources only — the slot table of `circdist_lift_d3gate_20260820.md` §7
(`a = [0,3,4,5]` on data order `[0,1,2,3]`, `b = [0,1,2,6]` on order `[2,0,1,3]`), the elementary
fault model of its §1.3, and the detector definitions of its §1.4 — and represented the Pauli frame
as two 6-bit masks rather than dicts. I checked the model itself before using it: the frozen fault
table gives `3·2 + 15·8 + 3·26 + 2 = 206` faults per round, which is what my enumerator produces.

```python
# rv_f1.py (abridged; full file run this session)
D=[0,1,2,3]; A,B=4,5; DEPTH=7
T_A2Q={0:0,1:3,2:4,3:5}; T_Q2B={2:0,0:1,1:2,3:6}
LAYER=[[] for _ in range(DEPTH)]
for q,t in T_A2Q.items(): LAYER[t].append((A,q))      # ancilla a control, data target
for q,t in T_Q2B.items(): LAYER[t].append((q,B))      # data control, ancilla b target
BUSY=[{u for g in LAYER[t] for u in g} for t in range(DEPTH)]
IDLE=[[u for u in range(6) if u not in BUSY[t]] for t in range(DEPTH)]
BITS={'I':(0,0),'X':(1,0),'Y':(1,1),'Z':(0,1)}
def simulate(R,f,basis):
    x=z=0; ma=[]; mb=[]
    for r in range(R):
        x&=0b1111; z&=0b1111                          # ancilla reset each round
        ...                                           # prep / CNOT / idle fault insertion
        oa=(z>>A)&1; ob=(x>>B)&1                      # MX on anc a, MZ on anc b
        ...
    term=sum((x>>q)&1 for q in D)&1 if basis=='Z' else sum((z>>q)&1 for q in D)&1
    return ma,mb,term
def detectors(R,ma,mb,term,basis):                    # d3gate 1.4
    if basis=='Z':
        return ([('b',mb[0])]+[('b',mb[r]^mb[r-1]) for r in range(1,R)]
                +[('b',mb[R-1]^term)]+[('a',ma[r]^ma[r-1]) for r in range(1,R)])
    ...
```

My output, all four round counts and **both** sectors:

```text
(MC) c_ab = 2 (even required)          faults/round = 206
basis=Z R=2 nf= 412  FULL {0:57,1:209,2:123,3:23}          max=3 | SECTOR {0:130,1:216,2:66}  max=2
basis=Z R=3 nf= 618  FULL {0:64,1:294,2:204,3:52,4:4}      max=4 | SECTOR {0:195,1:324,2:99}  max=2
basis=Z R=4 nf= 824  FULL {0:71,1:379,2:285,3:81,4:8}      max=4 | SECTOR {0:260,1:432,2:132} max=2
basis=Z R=5 nf=1030  FULL {0:78,1:464,2:366,3:110,4:12}    max=4 | SECTOR {0:325,1:540,2:165} max=2
basis=X R=2..5       SECTOR {0:126,1:220,2:66} {0:189,1:330,2:99} {0:252,1:440,2:132} {0:315,1:550,2:165} max=2
WT4 fault: round 1, CNOT (q0 -> anc b) at t=1, Pauli I(x)Y  fires [('b',1),('b',2),('a',1),('a',2)]
```

Every printed value of the amendment's §5.2 reproduces **value for value** from an independent
implementation: the four sector histograms, all four full-DEM histograms, `max = 4`, and the named
weight-4 fault with its exact detector set. The review's X-memory row (which the amendment did not
recompute) also reproduces exactly. `(MC)` holds. I re-derived the weight-4 mechanism by hand before
running: a `Z` on `anc(b)` back-propagates to data `1` and `3` through the later Z-check CNOTs, so
`m_{a,1}` and `m_{a,2}` both move while the `X` part moves `m_{b,1}`; the pattern
`D_{b,1},D_{b,2},D_{a,1},D_{a,2}` is forced.

**The pin is faithful to the source.** `circdist_lift_iff_proof_20260820.md` line 224 states
Definition 1.12 as *"`M` is graph-like (in the Z-memory sector) if…"* — sector-indexed verbatim, so
the amendment's governing reading quotes rather than reinterprets.

**One check the amendment does not make, which I made, and which holds.** Per-sector graph-likeness
is a **wider** class than whole-DEM graph-likeness (fewer detectors can only lower a column weight).
So the pin strengthens the *universal* clauses C1–C4 while rescuing the *existential* C5. That is
only safe if the wider class is still inside `lift.iff`'s certified scope — and it is, exactly:
`lift.iff`'s own claim says "graph-like" in the same Def-1.12 sense, and its §1.5/§7.3 scope note
records that **no step of either theorem's derivation uses Definition 1.12 at all**. The pin
therefore moves nothing outside the child's certified scope in either direction. I looked for a
clause that would break under the widening and found none.

**Scope of my check (stated, as an absence-type step must be):** complete over the frozen model's
raw elementary faults for **this one schedule**, both sectors, `R ∈ {2,3,4,5}`; it computes detector
weights only, no distances; it is not a scan over other schedules or codes. The amendment's
inherited limitation C-O2 binds me identically: my implementation is independent, my *model design*
is not — it reads the same frozen fault table and the same detector conventions.

### 2.2 F2 — `R ≥ d` carried as C-M7. **CONFIRM.**

I verified the hypothesis at its source rather than through the assembly: `circdist_lift_iff_proof`
line 790–791 states CONJECTURED 5.7 as *"For every legal, measurement-consistent single-ancilla CSS
schedule `M`, **and `R ≥ d`**"*, and §5.10(1) / Amendment 1 §253 give the supporting fact ("`d_R` is
non-increasing in `R` and constant for all `R ≥ d`"). C-M7's text reproduces both accurately and
does not overstate: it says explicitly that the absence of a counterexample in this campaign is
*evidence, not proof*, and confines it to `d ∈ {2,3}`.

**The two instruments are correctly characterised**, and I confirmed the hash arithmetic myself
rather than taking it: the claim hash is computed from the `claim` field alone, so (a) a claim edit
moves `ccad7fa6…` and lapses any review bound to it, and (b) an assessment-only caveat is
hash-neutral. The amendment correctly refuses to choose between them — that is a dispatcher act.
See §2.6 for the condition this leaves on the promotion.

### 2.3 F3 — trip-wire rebound to claim hashes. **CONFIRM, and it has re-fired since.**

I recomputed all fourteen §0.1 digests on current bytes: **13/14 reproduce**, the single failure
being the root node file, which now hashes `045da24c9baf5f94…` (8618 B) — a **fourth** distinct
value, after `64963af7…` (assembly), `01f6a888…` (review) and `84178f08…` (amendment). Its **claim**
hash is `ccad7fa6…` in all four. F3's diagnosis is therefore not merely correct, it re-fired between
the amendment being written and my reading it, for a reason that carries no substance (the node
gained the amendment's own registration event). The rebound trip-wire — four claim hashes, ten
artifact/frozen-note digests — **does not fire on the current node state**: I reproduced all
fourteen of those objects myself.

### 2.4 N1 — what the rebinding costs, and why it does not block

A whole-file digest fires on *any* byte change, including a child being demoted or gaining a REFUTE
event; a claim hash does not. §3.3 anticipates this and answers it by relocating the level/event
check to §0.2 and assembly §8 item 2. That answer is adequate but it converts an automatic trip-wire
into a **checklist obligation**, so I record it as a standing condition rather than a defect:
*assembly §8 item 2 (levels + no REFUTE/FURTHER-REPAIR after 2026-08-20) must be re-run at
promotion, not assumed.* I ran it myself this session and it passes (§1).

### 2.5 R4 / R6 fold-ins. **CONFIRM, with provenance checked.**

R4's amended argument (iii) rests on the campaign's min-over-sectors convention and on Steane's
per-sector values. The amendment states plainly that it did **not** re-derive the Steane numbers and
that they are the reviewer's. I did not re-derive them either — but I did verify the convention and
the consequence at the frozen source: `circdist_lift_d3gate_20260820.md` §1.4 says *"the circuit's
distance is the minimum of the two"*, and its line 395 prints `min(d_circ^Z, d_circ^X) = 2` for the
Steane circuit. So R4's conclusion is corroborated by the frozen document itself, not only by the
review. R6's widening (naming (MC) **and** `R ≥ d` in the route gloss) is consistent with what I
verified in §2.2. C-R2's containment correction is recorded, not resolved; I take no position on
model identity and found no evidence bearing on it.

### 2.6 Verdict 1

**CLEARS-FOR-PROMOTION at the `CERTIFIED*` ceiling**, binding to the root claim hash

```text
CIRCDIST.lift   sha256:ccad7fa605be1ae14a2dbc1d6c5758300bb8a5f0a3023fcef84725be40e78d8a
```

subject to two conditions that the amendment **cannot** discharge because it may not write the node,
and that a promotion act must therefore perform:

1. **The F1 pin must appear in the root's assessment**, not only in the amendment. The review's F1
   required a sentence in the *assessment*; the amendment supplies the text (§1.2) and states that
   applying it is a dispatcher act. If the node is promoted without it, F1 is not discharged in the
   record and the plain reading of the claim still has no certified witness for C5.
2. **C-M7 (`R ≥ d`) must ride in the root's caveats** — instrument (a) or (b) of §2.3, the lead's
   choice; (b) must name `R ≥ d` explicitly.

Also carried: C-R1 (single-stack ⇒ `CERTIFIED*` ceiling, `PROVED` unreachable on this route), C-R2
unresolved but non-gating, C-O2 (shared model design), and the §2.4 checklist obligation. **VALUE**
of F1/F2/F3: confirmed. **PRINTED DERIVATION**: confirmed for F1 and F3 (I reproduced both);
confirmed by source citation for F2 and R4.

---

## 3. Amendment 1 to the SAT window theorem — S3′, W-G5, §0

### 3.1 S3′ is installed verbatim. **CONFIRM (byte-level).**

I extracted the S3′ block from both files and compared: after stripping blockquote markers and line
wrapping, the amendment's §1.2 text is **character-identical** to the review's §1.3 text. The
bookkeeping consequences the amendment attaches (W-G3 *deleted* not carried; S3 struck including the
"enlarging can only decrease `d_circ`" sentence; §6.1's table row rewritten) are the right ones: the
struck sentence is exactly the one that licenses the `d_R = +∞` reading, and I confirmed it is
present at theorem line 182–185 as quoted.

### 3.2 The 18/18 verifications reproduce. **CONFIRM, by a different method.**

The amendment computes the deterministic-parity space algebraically (back-propagate each measured
Pauli, test membership in the input stabiliser group). To avoid inheriting that route I wrote an
**Aaronson–Gottesman CHP stabiliser simulator** from scratch, sampled noiseless shots of the record
vector, and took `dim V = L − rank(span of record variations)`; detector ranks are pure `F₂`
combinatorics on record-index vectors and need no simulator at all.

```python
# rv_s3.py (abridged) — CHP tableau, own implementation
class CHP:
    def __init__(s,n): s.n=n; s.x=[0]*(2*n); s.z=[0]*(2*n); s.r=[0]*(2*n)
    def cnot(s,a,b): ...      # r ^= xa&zb&(xb^za^1); x_b^=x_a; z_a^=z_b
    def h(s,a): ...
    def measure_z(s,a): ...   # random branch via rowsum, deterministic via scratch row
    def measure_x(s,a): s.h(a); return s.measure_z(a)
def dims(n,A,B,R,order,shots=260):
    recs=sample_records(n,A,B,R,order,shots); ref=recs[0]
    var=[sum(((a^b)<<i) for i,(a,b) in enumerate(zip(v,ref))) for v in recs[1:]]
    dimV=L-f2rank(var)      # ... dimV_Z, dimV_X by projection; D_b, D_a, lambda as index vectors
```

```text
code                  sched R   L dimV rkD rkD+l defic dimVZ rkDb+l dimVX rkDa leftker  k
steane713             Zblk  1  13    7   6     7     0     7      7     0    0      0   1
steane713             Zblk  2  19   13  12    13     0    10     10     3    3      0   1
steane713             Zblk  3  25   19  18    19     0    13     13     6    6      0   1
steane713             Xblk  1..3   (identical to Zblk rows)
surface913            Zblk  1  17    9   8     9     0     9      9     0    0      0   1
surface913            Zblk  2  25   17  16    17     0    13     13     4    4      0   1
surface913            Zblk  3  33   25  24    25     0    17     17     8    8      0   1
surface913            Xblk  1..3   (identical to Zblk rows)
steane713+redundantX  Zblk  1  14    8   6     7     1     7      7     1    0      1   1
steane713+redundantX  Zblk  2  21   15  13    14     1    10     10     5    4      1   1
steane713+redundantX  Zblk  3  28   22  20    21     1    13     13     9    8      1   1
steane713+redundantX  Xblk  1..3   (identical to Zblk rows)

failure (a) rank(D+lam) = rank(D)+1                 : 18/18
S3' Z-half   rank{D_b} (+) {lambda} = dim V_Z       : 18/18
S3' X-half   dimV_X - rank{D_a} = dim leftker(H_X)  : 18/18
steane713+redundantX  R=1,2,3 : parity XOR_a m_{a,0} deterministic=True, in span(D u {lambda})=False
```

Every column of the amendment's §4 table reproduces, value for value, from the sampling route — `L`,
`dim V`, `rank(D)`, `rank(D+λ)`, the deficiency, `dim V_Z`, `rank(D_b+λ)` and `dim leftker(H_X)` —
as does the review's explicitly named missing parity at `R = 1,2,3`. The analytic formula
`dim V = dim ker H_X + |ℬ|R + R|𝒜| − rank H_X` holds in all 18.

**I also checked the argument, not only the numbers.** S3′'s load-bearing half is that no
enlargement of the `X`-check detectors changes `d_R^Z`. I re-derived it: by CONJECTURED 2.1 (theorem
lines 227–243, which I read in full) the `D_{b,r}` and every `λ^{(j)}` are functions of the `X`-parts
alone and every `D_{a,r}` — hence every element of `V_X` — of the `Z`-parts alone; `F^X` is available
in the frozen fault model, has weight `≤ |F|`, fires the same Z-detectors and flips the same
observable, and carries no `z`-component, so it triggers **nothing** in `V_X`, redundancy detectors
included. Enlarging modulo the observables can only add constraints, so `d_R^Z` is unchanged in both
directions. Sound as printed.

### 3.3 W-G5 and the §0 superscript. **CONFIRM both.**

W-G5: the added sentence cites Standing fact 1.6 for `c_{ab} + c'_{ab} = |supp(a) ∩ supp(b)| ≡ 0`.
I checked the source (theorem lines 114–120): the derivation does produce `c'_{ab}` and does
conclude `c'_{ab} = c_{ab}` by (CSS). The step is real, and the added sentence is the missing link
between Definition 1.5's asymmetric phrasing and the §2 mirror, exactly as the review asked.

§0 box: theorem line 39 prints `w ≤ |F| = d_R(M) ≤ d`, while CONJECTURED 4.1 (line 446) prints
`w ≤ |F| = d_R^σ(M) ≤ d`. The defect is real, the replacement matches 4.1, and §3–§5 are untouched.

### 3.4 N2 — the adjudication the task asked for. **The amendment is right; the review's summary
sentence is wrong.**

The review §1.2 summarises its table as *"`rank(D) = dim V − k` in every row (failure (a): 18/18
instances)"*. The amendment's §1.3 precision note says the correct identity is
`rank(D) = dim V − k − dim leftker(H_X)` and `rank(D+λ) = dim V − dim leftker(H_X)`. I tested both
against my own numbers, in the same run:

```text
AMENDMENT identity  rank(D) = dimV - k - dim leftker(H_X)  : 18/18
REVIEW summary      rank(D) = dimV - k                     : 12/18
```

The review's sentence fails on exactly the six `steane713+redundantX` instances — and it fails
against **the review's own printed table**, which shows `rank(D) = 6` where `dim V − k = 7`. So this
is a summary-line error in the review, not a data error; and the finding the sentence was making
survives untouched, because `rank(D+λ) = rank(D) + 1` — the observable is missing from the Definition
1.9 span — holds **18/18** in my run as well. **S3′ itself is unaffected**: it never asserts the
summary sentence, and the identity that does hold is what S3′ states in words. The amendment's
handling (correct a review's summary line, flag it, do not touch the clause adopted) is exactly
right, and its refusal to absorb the discrepancy silently is the behaviour the record should reward.

### 3.5 Verdict 2

**CLEARS-FOR-PROMOTION to `CERTIFIED*`**, binding to

```text
CIRCDIST.sat.window   sha256:8698b051b15fa14ff669299580d9b7bfec01808c0a34133ef09264e749466146
```

All three required repairs are applied — one verbatim, two faithfully — no mathematical content of
parts (i)–(iii) moved, and S3′ **removes** a hypothesis rather than adding one. The caveat set that
rides along must **carry S3′ and must not carry W-G3**, and must keep W-G1, W-G2, W-G4, W-OPEN and
the §5 sampling-rarity scope caveat open exactly as stated. **VALUE:** confirmed (18/18 by an
independent method). **PRINTED DERIVATION:** confirmed — the printed code is the code that produced
the printed table, and its stated scope (3 codes, 2 schedules, `R ≤ 3`, Z-memory, no distances) is
accurate and is not exceeded by any claim made from it.

---

## 4. Amendment 4 to the islands dossier — D1, D2, D3, D4, and the chain

### 4.1 D1 — the replacement stdout is genuine. **CONFIRM (byte-identical).**

I extracted the §1.2 code block and the §1.2 `text` block programmatically, ran the code untouched,
and compared:

```text
$ python3 d1_code.py > d1_actual.txt
$ diff d1_printed.txt d1_actual.txt            ->  no differences
ab627920ae115aa402bb20976a3a952e274a8eab4f5f247c9389b247959b7bae  d1_printed.txt
ab627920ae115aa402bb20976a3a952e274a8eab4f5f247c9389b247959b7bae  d1_actual.txt
```

The defect the review named is genuinely gone: `['G2','G3']` now falls out of
`single_point ∩ repeated_pair` over `(point,label)` options, with **no name filter anywhere** in the
file. I checked the two hand-entered inputs, which are the only place a name filter could hide:

* the `G` dict reproduces Amendment 1 §5.4's emitted lists (lines 381–389) family by family,
  including `(G4) {(π,0),(ν_j,a),(ν′_j,a)}` at three distinct points;
* the combinatorics are right independently of the code — over `Log = F₂²` the (S1)-compliant
  3-subsets of one point are `{a,b,c}` only (`a+b+c=0`; the other three triples sum to `3,2,1`), and
  the (S1)-compliant 3-multisets are `{0,0,0},{0,a,a},{0,b,b},{0,c,c},{a,b,c}` — 1 of 4 and 5 of 20,
  as printed. I derived this by hand before running anything.

The scope restatement (single point, single list, `dim Log = 2`, (S1) only) is accurate, and the
"distinct-literal 3-CNF" proviso is correctly kept — without it (G6) itself repeats an option.

### 4.2 D2 — edits 9 and 11 restored faithfully. **CONFIRM (verbatim).**

Compared against `circdist_islands_review_20260820.md` §9 at the hash bound in §0: edit 9 (review
lines 643–644) and edit 11 (lines 646–647) are quoted **character-for-character** after the item
number. I then verified the two claims the amendment makes about *why* they matter:

* **Edit 9 is real.** Theorem II.4's hypothesis is `d(Q) = min(μ_X,μ_Z)` (writeup line 554) —
  a distance condition, not poly-time checkable; Lemma II.5's is a set of kernel-dimension
  conditions (line 563–568) — rank computations, poly-time checkable. The contrast the edit asks for
  is the operative one and the write-up does not draw it. It does **not** falsify the node claim,
  whose HGP clause says "constant YES **under the non-degeneracy proviso**" and thereby flags the
  promise; it is a presentational repair that must ride as a caveat, which is where the amendment
  puts it.
* **Edit 11's bar is real and correctly located**: Theorem V.4 is stated "Under the promise of §6.1"
  (writeup line 1180), so the node claim's Island V clause inherits §6.1's promise, and vacuity of
  the promise would empty that clause. See §4.3 — where I part company with the amendment.

### 4.3 N3 — the one place where I refute the amendment: edit 11 is **not** un-witnessed

Amendment 4 §2 states that edit 11 "**is unsatisfied**", that §6.1's promise is "**currently
un-witnessed**", and that this session "ran **no** code search of its own". That is an absence-type
claim, so I attacked its scope boundary: the amendment searched the *islands chain*; the witness is
in the repository, one document over, and has been since 2026-08-20.

`circdist_cplx_gadget_20260820.md` §3.2 defines `G_≠₃` (`n = 12`), and
`circdist_islandv_review_20260820.md` §5.2 reports an independent first-principles reproduction of
it. I did not rely on either report. I rebuilt the code from the printed parity checks and
enumerated exhaustively over `F₂^12` with my own code:

```python
n=12
XC=[(0,1,2,3),(4,5,6,7),(1,4,8,10),(0,6,8,11),(3,7,9,10)]                       # X-checks
ZC=[(1,2,4,7,9),(0,1,6,7,10),(0,1,2,3,8,9),(0,1,4,5,11),
    (0,2,4,6,8,11),(4,5,6,7,10,11),(8,9,10,11)]                                 # Z-checks
HX=[sum(1<<q for q in c) for c in XC]; HZ=[sum(1<<q for q in c) for c in ZC]
par=lambda v: bin(v).count('1')&1
kerHZ=[v for v in range(1<<n) if all(par(v&b)==0 for b in HZ)]      # X-type logicals live here
kerHX=[v for v in range(1<<n) if all(par(v&a)==0 for a in HX)]
dX=min(bin(v).count('1') for v in kerHZ if v not in span(HX))
dZ=min(bin(v).count('1') for v in kerHX if v not in span(HZ))
```

```text
CSS  H_X H_Z^T = 0 : True          X-check weights [4,4,4,4,4]  (all <= 4)
rank H_X = 5, rank H_Z = 5, k = 2, dim ker H_Z = 7, dim S_X = 5
d_X = 4   X-logical spectrum {4:32, 6:36, 8:24, 10:4}
d_Z = 3   Z-logical spectrum {3:8, 4:14, 5:16, 6:20, 7:16, 8:14, 9:8}
d(Q) = 3
SEC 6.1 PROMISE VERBATIM (d(Q)=3, k>=1, every X-check weight <= 4, d_X >= 4, hence d_Z = 3): True
```

This is a **complete enumeration**, not a sample, and the spectra agree with the gadget document's
printed spectra exactly. **Edit 11's first alternative is therefore satisfied**: a code meeting
§6.1's promise verbatim exists and is on disk.

The sharper bar — the claim's Island V clause is the `k ≤ 1` regime, and `G_≠₃` has `k = 2` — is also
clearable in one step, which I performed: any weight-3 `Z`-logical `v ∈ ker H_X ∖ S_Z` may be
adjoined as a new Z-check (CSS is preserved because `v ∈ ker H_X`), and

```text
weight-3 Z-logical candidates : 8      k=1 augmentations meeting the promise verbatim : 8/8
e.g. adjoin Z-check {0,1,8} :  k = 1,  d_X = 4,  d_Z = 3,  d(Q) = 3,  all X-checks weight 4
```

**Status of this finding.** NUMERICAL, my own code, exhaustive at `n = 12`; it is not a review of
the gadget document and it does not verify anything else imported from it. It **helps** the node: it
removes a non-vacuity bar rather than adding a defect. Concretely, roll-up **row 8 should be
re-labelled** from "unapplied; currently un-witnessed" to *"edit 11's first alternative is
discharged by an exhibited witness (`G_≠₃`, and a `k = 1` augmentation of it) at NUMERICAL level;
the write-up should cite one"*. Until §6.1 or Remark V.6 actually cites such an instance the edit
remains *unapplied as an edit* — but the record must no longer say the promise is un-witnessed.

### 4.4 D3 and D4. **CONFIRM.**

* **D3(a).** The quoted "before" text is at `writeup` lines 1263–1264 as cited, inside the *proof* of
  Proposition V.7 and four lines below the O4 statement line; both occurrences of "list" are there.
  The replacement is convention alignment only.
* **D3(b).** The flagged correction of focused-rereview §4.4 is itself correct: (G4) repeats a
  *label* (`a`) but places its three options at three distinct points, so as a set of `(point,label)`
  pairs it is a genuine 3-set; only (G2) and (G3) repeat an option — which my §4.1 run confirms
  structurally. The §4.4 *conclusion* is left standing, correctly.
* **D4.** The added clause is the stronger and more honest statement of Amendment 3 §1's own
  finding, and it is consistent with §3.2 of that file.

### 4.5 The chain sweep — what I checked for remaining recorded defects

I did not take the roll-up on trust; I walked the chain, at the hashes of §1:

| # | object | recorded defects / open items | disposition I verified |
|---|---|---|---|
| 1 | `islands_writeup_20260820` (base) | — | hash reproduces; §6.1 promise and Thm V.4/II.4/II.5 read directly |
| 2 | `islands_review_20260820` | 11 recommended edits; §8 not-reviewed list | 1–8, 10 applied by Amdt 1 (its §8 lists only 9 and 11 as unapplied); 9 and 11 → roll-up rows 7, 8; §8 residue → §4.6 below |
| 3 | `cplx_islands_amendment1` | §8 items 1–9 | items 2→row 1/2, 3→row 6, 4→row 6 (partly, §4.6), 5→rows 7/8, 7→row 4, 8→row 5; items 1, 6, 9 are not defects |
| 4 | `amendments_review_20260820` (focused rereview) | I1; the V.7′ statement-type defect; §6 items 1–9; §7 shared-model caveat | I1 closed by Amdt 2 (confirmed by `amendments2_review`); statement defect closed by Amdt 3; §6 items → rows 1–8 except §4.6; §7 → §4.6 |
| 5 | `cplx_islands_amendment2` | closes I1; §5 carries edits 9 and 11 forward | verified at its line 199–203 |
| 6 | `amendments2_review_20260820` | §7.2 FURTHER-REPAIR: the multiset wall; §9 limitations 1–7 | wall closed by Amdt 3 §1 (O1–O5 confirmed by the Amdt-3 reviewer); §9 items → rows 2–6 |
| 7 | `cplx_islands_amendment3` | D1–D4 raised against it | all four closed by Amdt 4; D1 and D2 re-verified by me above |
| 8 | `islands_amendment3_review_20260822` | D1, D2 required; D3, D4 polish | closed; its own §9 limitations are scope statements, not defects |
| 9 | `cplx_islands_amendment4` (this one) | — | D1 stdout byte-identical; D2 verbatim; D3/D4 accurate; **one claim refuted (§4.3)** |
| 10 | node `CIRCDIST.cplx.islands` | frontier task-003, task-004, task-008 | claim hash = recorded `reviewed_hash`; task-003 blocks `PROVED` only; task-004 is open research outside the claim; task-008 is this gate; no unapplied repair in the event list |
| 11 | `islandv_review_20260820` (**not** in the amendment's sweep) | **two REFUTEs** (Prop 5(2)(3) prescribability; the Z-sector `W=6, d_Z≥7` plan) and four GAPs | registered against **`CIRCDIST.cplx.fixed-d`**, carried on that node's frontier as task-002 and task-004. I checked the dependency direction: the islands write-up imports from the *gadget* document (§5.3 `K₄`), not from the refuted Proposition 5, and no islands clause consumes either refuted item. **Does not block.** |

Row 11 is the scope boundary the amendment's "no remaining recorded defect" claim did not test, and I
report that it holds — but only because the refutations live on the hardness node, not because the
sweep covered them.

### 4.6 Items recorded in the chain that the roll-up does not name (non-blocking)

The roll-up is complete relative to what it claims to be (Amdt 3 §5's six items ∪ {edits 9, 11}), and
its "must contain rows 1–8" is a lower bound, not an exhaustiveness claim. For the promotion caveat
set to be genuinely complete, three further recorded items should be named:

1. the base review §8 / rereview §6 item 2 residue not covered by row 6 — the `G_{≠3}` gadget census,
   the `1 152 / 8 513` stabiliser-coincidence counts, the `[[15,7,3]]` decoupling claim, and the
   "**56 of 71** random weight-6 CSS codes are not decoupled" figure (writeup §2.4). None is
   load-bearing: §2.4 is a scope clause that explicitly disclaims saying which codes are decoupled;
2. base review §8's "**the NO side of Theorem V.5**" — outside the claim, whose Island V clause is
   the `k ≤ 1` YES regime, but recorded and unreviewed;
3. focused-rereview §7's **shared-model caveat** (a systematic error in Definition 1.13 / Lemma 1.1 /
   Definition 2.2 would survive every implementation involved, mine included).

None of the three is a defect; all three are recorded NOT-REVIEWED items and belong in a caveat set.

### 4.7 Verdict 3

**CLEARS-FOR-PROMOTION at the `CERTIFIED*` ceiling**, binding to

```text
CIRCDIST.cplx.islands   sha256:b4325b447807dc93f9e5f96ab503cc96800dab3e3b5b8e70e0378601121d0590
```

with the caveat set = roll-up rows 1–8 **as amended by §4.3** (row 8 re-labelled: the promise is
witnessed; the edit remains unapplied as an edit) **plus** the three items of §4.6. `PROVED` remains
out of reach on task-003 alone. **VALUE:** every value I tested reproduces. **PRINTED DERIVATION:**
D1's block is now genuine stdout (byte-identical), D2's quotations are verbatim, D3/D4 are accurate;
the single printed statement I refute is §2's "un-witnessed", which is a claim about the record, not
about the mathematics, and its correction loosens rather than tightens the promotion gate.

---

## 5. What I did not do (NOT-REVIEWED by me)

1. **One box, focused.** I reviewed the amended spots and their propagation only. The unamended
   bodies of the assembly, the window theorem, the islands write-up and Amendments 1–3 carry their
   prior reviews; I did not re-open them.
2. **Not re-derived:** the Steane per-sector `(2,3)`/`(2,2)` values (I verified the convention and
   the frozen document's own `min = 2`, not the numbers); any `d_circ`; parts (i)–(iii) of the window
   theorem; Islands I–IV; the Courcelle/ALS citations; the `K₄` composite; the three unrecomputed
   census families; the `1 152 / 8 513` counts; the `56 of 71` figure.
3. **Absence-type limits of my own work.** §2.1 is complete over one schedule's raw fault set at
   `R ≤ 5` and computes detector weights only. §3.2 covers 3 codes × 2 schedules × `R ≤ 3`, Z-memory,
   and is a sampling route (rank of record variations), so it certifies the *dimensions*, not the
   general derivation of S3′ — for that I checked the argument by hand. §4.3 is exhaustive at
   `n = 12` for two specific codes and says nothing about any other instance.
4. **Shared model design.** My lift simulator reads the same frozen fault table and detector
   conventions as the documents it checks; my window simulator shares the circuit layout. A
   systematic modelling error at that level would survive all of it. My CHP tableau and the
   amendment's back-propagation are genuinely different routes to `V`; my `[[4,2,2]]` propagator and
   theirs are not.
5. **I resolved nothing about C-R2**, model identity, or which stack executed any prior review, and
   I am not evidence either way.
6. **I promoted nothing.** No node file, scheduler file, generated view or existing artifact was
   modified; nothing under `research/circdist/proof-dag/` was written. This review is one session's
   act and is itself unreviewed.
