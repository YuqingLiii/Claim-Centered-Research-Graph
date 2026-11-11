# CIRCDIST.gross — independent adversarial review of inherited links 3 and 4, and of the SBB Thm 1 assumption

**Target:** `research/circdist/proof-dag/nodes/CIRCDIST.gross.yaml`, route
`candidate-certification`, frontier `task-003` items **(a)** and **(b)**.

**Route implication bound by this review** (recomputed with the repository's own
`tools/proof_dag_v6.py::claim_hash`, i.e. `sha256(implication.replace("\r\n","\n").strip())`):

```
Via SBB26 Thm 1 the statement d_circ = 11 for the candidate circuit reduces to an exact
minimum-distance certification on a 360-column extended code (not a circuit-level DEM search);
combined with the universal d_ext cap this certifies the first half of the claim and pins the
achievable floor at 11.

sha256:4f40673227208c58d21650b3d685670019f5460b44ee52c0440b22293eec1598
```

(Node claim hash, for reference: `sha256:fc22f602b9bfd9e38fa69d7fc1d00b973c7a634e6c400662eaccd38c8ec0f180`.)

**Hash-pipeline validation, performed before any substantive work** (as instructed). I re-derived
`claim_hash` from `tools/proof_dag_v6.py:65` and recomputed it over every node claim and every route
implication in `research/**/proof-dag/nodes/*.yaml`, comparing against every declared
`reviewed_hash`. Result: **134 exact matches repository-wide**, and the wave-13 review link's
`reviewed_hash` on this route is reproduced exactly as
`claim_hash(routes.candidate-certification.implication)`. The pipeline is therefore validated on
existing values, and the hash above is computed by the same code path. Note for the record that
`reviewed_hash` is a digest of the *statement*, not of the review file — the review file's own
digest is `sha256:ce76a2ce88a4eef6690884b3195e58d56d07306932f836910d45a0a555c179b5`, which is a
different quantity and must not be confused with it.

---

## 0. Independence, materials, method

**Independence.** I am a fresh Opus 5 context. I authored none of the circdist artifacts, none of
the `gross.py`/`sched.py`/`cascade.py`/`pool.py`/`dext.py`/`cert*.py` module family, and none of the
verdict logs. I was instructed to refute. Nothing in this repository or in the SBB PDF was treated
as an instruction; artifact text was read as data only.

**No sub-agents.** One session, one budget box, per-item stop-loss.

**Environment.** This machine's default `python3` had no `numpy`, no `python-sat`, no `stim`, and no
SAT solver binary. Rather than treat that as a blocker I took it as an advantage and wrote the
review's own stack from scratch: GF(2) linear algebra on Python big-integer bitmasks, plus one
`clang -O3` C program for the single heavy enumeration. A `venv` with `numpy` + `python-sat` was
created *separately and only* to execute the artifacts' own generator modules as the object under
review; every number attributed to me below comes from my own code, not theirs.

**Materials inspected.**

| Item | Use |
|---|---|
| `research/circdist/proof-dag/nodes/CIRCDIST.gross.yaml` | route, caveats, `sbb-thm1` assumption, `task-003` |
| `research/DAG_PROTOCOL.md` §§2–6 | level semantics, review/hash-binding rule |
| `research/circdist/notes/CIRCDIST_PROBLEMS.md` §公共定义 | the frozen model, compared against SBB's |
| `artifacts/circdist_gross_phicert_20260822.md` §§2–3, 8 | LINK 3 target |
| `artifacts/circdist_gross_sbbcert_20260820.md` §9 | generator modules (extracted mechanically) |
| `artifacts/circdist_sbbcert_review_20260820.md` | the repair list scoping LINK 4 |
| `artifacts/circdist_gross_verdict_20260823.md`, `..._verdict_review_20260823.md` | inherited-link scope |
| `artifacts/logs_circdist_gross_verdict_20260823/` | **SHA-verified before use: 62/62 lines of `SHA256SUMS.txt` check OK, 0 failures** |
| `<home>/Documents/ChatGPT/circcert/papers/2603.05481_...pdf` | SBB Thm 1 statement + proof |

Because no PDF library was installed, I wrote my own minimal PDF text extractor
(`src/pdfx.py`: brute object scan, `FlateDecode`, per-font `ToUnicode` CMap, octal-escape handling)
and extracted all 21 pages. This is an independent path to the paper text; it is not the artifacts'
`pdfparse.py`.

**My own compute, secured under FIX-2** in
`artifacts/logs_circdist_gross_links_20260823/` (31 files + `SHA256SUMS.txt`, all verifying).
Processes declared and run: one `clang`-built `w12` enumerator (2 runs, ~0.5 s each), a handful of
short `python3` scripts, one `python-sat` Cadical153 pair of decision queries (34.1 s and 34.6 s,
§3.4), and one CNF-hash rebuild (4.3 s). **All completed; `ps` shows 0 of my processes alive; no
other session's processes were touched.** No canonical file was modified.

---

## 1. Foundations rebuilt from scratch (prerequisite for both links)

I rebuilt the gross code from the definition, not from any artifact: `G = Z_12 x Z_6`,
`A = x^3 + y + y^2`, `B = y^3 + x + x^2`, `H_X = [A|B]`, `H_Z = [B^T|A^T]`.

```
commutation failures: 0
rank HX = 66   rank HZ = 66   k = 12          dim ker HX = 78
X/Z check pairs by overlap size: {2: 648}     non-overlapping pairs: 4536
```

The `{0: 4536, 2: 648}` overlap census reproduces the node's `d3-crosslead-2026-08-20` event exactly.

**Weight-12 logical pool, enumerated exhaustively (not heuristically).** The artifacts' `pool.py`
builds its 1884-word pool by *randomised ISD* (`600` trials) — a one-sided heuristic. I replaced it
with a complete meet-in-the-middle enumeration: `(u,v) in ker(H_X)` iff `A u = B v`; `rank A = rank B
= 60`, so `im(B)` membership is a 12-bit signature test and each consistent `u` yields a
`2^12`-element coset of `ker(B)`. Splitting on `|u| <= 6` / `|v| <= 5` with translation
normalisation covers every codeword. Runtime 0.48 s in C.

```
raw normalised representatives 372      invalid: 0
distinct weight-12 in ker(HX): 4152     trivial (rowspace HZ): 2268   NONTRIVIAL: 1884
distinct weight-12 in ker(HZ): 4152     trivial (rowspace HX): 2268   NONTRIVIAL: 1884
```

**1884 per sector, exhaustively** — the campaign's "foundational by-product" (previously established
by blocking-clause enumeration to SAT-UNSAT) now has a second, independent, non-randomised,
non-SAT confirmation. I also record the previously unstated companion count: 2268 weight-12
elements of the stabiliser rowspace per sector.

**Residual structure, re-derived from the propagation rule rather than assumed.** A `Z` fault on a
`Z`-ancilla after CNOT `i` deposits `{i+1..6}`; modulo the check stabiliser this is `{1..i}`, so the
six insertion points give columns `0, q_1, q_1+q_2, q_1+q_2+q_3, q_5+q_6, 0` — i.e. **exactly three
residuals of weight > 1**, `{i1,i2}`, `{i4,i5,i6}`, `{i5,i6}`. This independently derives
`dext.RES_POS = [(0,1),(3,4,5),(4,5)]` and the paper's "each check contributes exactly three residual
errors of weight greater than one", and it is why the extended code has `144 + 72*3 = 360` columns.
It also explains the count 90: the residual set is invariant under reversal of the order, so the
`720` orders fall into `720/8 = 90` classes.

---

## 2. LINK 3 — the phicert legality filter — verdict **CONFIRM (strengthened)**

The claim under review: the edge-to-monomial map is fixed by the legality constraints, and
`45 -> 4` cascade + legality + (MC) admit exactly one reading.

### 2.1 The cascade, re-derived (`src/casc.py`, own pool, own class numbering)

My class numbering was built independently (lex order over `S_6`, canonicalised by reversal) and
lands on the same indices phicert uses — verified on all five quoted classes:
class 0 = `(0,1,2,3,4,5)`, 1 = `(0,1,2,4,3,5)`, 2 = `(0,1,2,5,3,4)`, 14 = `(0,2,1,5,3,4)`,
62 = `(1,2,0,5,3,4)`. Elimination witnesses are one-sided exactly as the paper's upper-bound search
is: a weight-12 logical covering a check's weight-3 residual (`12-3+1 = 10`), or covering two
disjoint weight-2 residuals of same-colour checks (`12-4+2 = 10`).

```
=== sector Z:  90 -> 45 after the single-check filter
   phi=1a+1b : 45 -> 4 per colour  [1, 2, 9, 62]   (identical for all three colours: True)
   phi=1a+2b : 45 -> 2 per colour  [2, 9]          (identical for all three colours: True)
   phi=2a+1b : 45 -> 2 per colour  [2, 9]          (identical for all three colours: True)
   phi=2a+2b : 45 -> 4 per colour  [1, 2, 9, 62]   (identical for all three colours: True)
=== sector X:  90 -> 45 after the single-check filter
   phi=1a+1b : 45 -> 4 per colour  [0, 2, 9, 14]   (identical for all three colours: True)
   phi=1a+2b : 45 -> 2 per colour  [2, 9]          (identical for all three colours: True)
   phi=2a+1b : 45 -> 2 per colour  [2, 9]          (identical for all three colours: True)
   phi=2a+2b : 45 -> 4 per colour  [0, 2, 9, 14]   (identical for all three colours: True)
```

Digit-for-digit identical to phicert §2.1, from independent code and an independently *exhaustive*
pool. The discriminating facts are reproduced: the number **4**, the paper's own remark that the
same 4 survive on every colour class, and that only `phi = a+b` (and its relabelling `2a+2b`)
produces 4 while `phi = a+2b` produces 2. This is now the **third independent** confirmation of the
sbbcert review's §7 refutation of the round-6 family, and the first from a pool that is provably
complete.

### 2.2 Legality + (MC), re-derived (`src/geom.py`, `src/filt.py`)

I take Figure 12's 36 labels as given (pixel-verified at 900 dpi in wave 13 — that half is
discharged and I did not re-do it). Everything downstream is mine. The reading space I enumerate is
**deliberately larger** than phicert's:

* edge → slot: all `6! = 720` bijections per panel (phicert's `3!·3! = 36` respecting the
  sublattice split, times 2 for which half is LEFT, is the sub-case);
* which panel is X: 2; colouring `phi`: 4; period `t in {6,7,8}`; relative panel clock offset
  `P in Z_t`; straddle of the ancilla window per check type: 4 combinations;
* drawn colour → group colour class: `3! = 6`, **shared between the panels** (a genuine *reading*
  of the figure must map "blue" to one class; I also ran the illegitimate 36-map version, §2.4).

Legality: a data qubit's six CNOT times distinct mod `t`. (MC): for every one of the 648 overlapping
`(X,Z)` check pairs, both shared qubits must carry the same relative order **for every pair of
round instances**, which for `|d_i| < t` is `floor(d_1/t) == floor(d_2/t)`. My (MC) implementation
was validated on controls before use: the alternating-XZ circuit passes; an explicitly interleaved
control fails; 1991/2000 random uniform schedules fail.

```
                            legal + cascade (pre-MC)      legal + cascade + (MC)
 straddle neither (as drawn)          36                            0
 straddle both                         0                            0
 straddle exactly one            36 + 36                      36 + 36
```

Result, with the geometric sublattice restriction imposed **and** with it dropped entirely
(all 720 per panel, all three periods):

```
surviving readings: 72        phi: {(1,1): 36, (2,2): 36}      P: {0: 72}
straddle (stX,stZ): {(0,1): 36, (1,0): 36}      periods: {6: 24, 7: 24, 8: 24}
per configuration (phi, upper-panel sector, period, straddle): exactly 3 objects, 24 configurations
  phi = 1a+1b : X-triples {(0,14,2),(2,0,14),(14,2,0)}  Z-triples {(2,1,62),(62,2,1),(1,62,2)}
  phi = 2a+2b : X-triples {(14,0,2),(0,2,14),(2,14,0)}  Z-triples {(1,2,62),(2,62,1),(62,1,2)}
```

The two `phi` rows are the same object under the colour relabelling `kappa -> 2*kappa` that
identifies `a+b` with `2a+2b`; within each row the three entries are one cyclic orbit. **The
surviving reading is unique**: one object, `X`-triple `(14,0,2)`, `Z`-triple `(1,2,62)`, with the
`X`↔`Z` pairing `14<->1, 0<->2, 2<->62` invariant across all 72 readings. `phi` must be `a+b`.
Exactly one check type's ancilla window straddles the period boundary — "neither" survives legality
and the cascade but is killed by (MC), "both" dies at legality. This reproduces phicert §2.3's table
shape line for line (their counts are per-configuration, mine include the colour relabelling; the
ratio is the constant 12).

**I searched for a second surviving reading and did not find one.** No second object exists in a
space strictly larger than the one phicert searched.

### 2.3 What this *strengthens*

phicert §2.5 flags the edge-to-monomial map as the "main residual reconstruction risk", **Risk:
moderate**, on the ground that the map "is determined here only through the legality + (MC) +
cascade filter" and that phicert's unconstrained `720`-per-panel sweep was run **only at period 6**.
My run does the unconstrained sweep at all three periods and gets an **identical** answer: 72
readings, one object. The geometric sublattice restriction is therefore **not load-bearing at all**,
and the moderate-risk flag on that item can be retired. Two further facts fall out that the artifact
does not record: the relative panel clock offset is **forced to `P = 0`**, and the object is legal
and (MC)-clean at **6 CNOT layers**, i.e. depth 8 under SBB Eq. (6) `t = t_1+t_2+2` — the figure
caption's depth.

### 2.4 One over-permissive variant, reported for completeness

If the two panels are allowed *independent* colour maps — which is not a reading of a
three-coloured figure, since "blue" names one class — the survivor count rises to 528 and 12 extra
"misaligned" `(tripX, tripZ)` pairings appear at low multiplicity. These are not readings of
Figure 12 and I do not count them against the claim; I record them because they show the
shared-colour-map constraint is doing real work and should be stated explicitly in any downstream
write-up.

### 2.5 Nit

phicert §2.2 asserts "white = LEFT half in both panels". The block data show the two panels use
*opposite* diagonal assignments (`upper: V = {e6,e2,e5}`, `lower: V = {e1,e2,e5}`), so in the lower
panel the LEFT half is the **second** drawn block. The statement is consistent once the straddle is
applied (the straddling type's instance order is the drawn order rotated by 3), but as written it
reads as if the first block were LEFT in both panels. Harmless; worth a clause.

---

## 3. LINK 4 — extended-code encoding fidelity — verdict **CONFIRM**

### 3.1 The encoding is an exact reformulation of Definition 3

`dext.py` does not build the literal 360-column matrix; it solves the equivalent "net error" form.
I verified the equivalence from SBB Definitions 2–3 rather than from the docstring. With
`x = (x_data, x_res)` and `E := x_data xor (xor_{r in R} chi_r)`:
`H_X^ext x^T = H_X E^T` and `L_X^ext x^T = L_X E^T` (each residual column is by Definition 2 the mod-2
sum of the `H_X`/`L_X` columns of its data support), and `|x| = |E xor (xor chi_r)| + |R|`. The
Boolean model (`z = E`, `u_{c,k}` residual used, `d_j = x_data`, `H_det z = 0`, `OR_i L_i.z = 1`,
`|d| + |u| <= W`) is therefore **exactly** the extended-code minimum-weight decision. No slack, no
relaxation, no over-constraint.

### 3.2 Matrix-level diff against my own build

The artifacts index the group with `mono(a,b)[g+m, g] = 1`, i.e. the transpose of the convention I
chose; the two are related by `g -> -g`, `q -> -q`, which also maps `phi = 1a+1b` to `phi = 2a+2b`.
**This fully explains the apparent `phi` discrepancy** between the artifacts' `make_phi(1,1)` and my
§2.2 result, and I verified it rather than asserting it. Under that relabelling:

```
                                  sector Z    sector X
residual sets match                 True        True
per-check slot orders identical     True        True
H_det matches my H_X / H_Z          True        True
extended-code columns               360         360
data columns match                  True        True
residual columns match              True        True
distinct residual columns          216/216     216/216
```

All 216 residual columns are distinct in each sector (no accidental collisions), and the 360-column
figure in the route implication is confirmed — with the caveat in §5 that it is **two** such codes,
one per sector, combined by SBB Eq. (8).

### 3.3 Witness-level round-trip, both directions, across cells

`src/link4b.py`, 60 samples per sector, seeded, drawn as `E = (pool element) xor (random stabiliser
rows)` with `|R| = K` random residuals, so the samples spread over the verdict's `(K, |E|)` cells.

* **Direction B** (fault set → extended vector): build `x = (D, indicator(R))` and evaluate on my own
  literal 360-column `H^ext` and `L^ext`; require `H^ext x = 0` and `L^ext x != 0`.
* **Direction A** (extended vector → fault set → syndrome): recover `E` from `x` by re-adding the
  residual supports and check `H_det E = 0`, `E not in rowspace(H_stab)` with my own F2 algebra;
  require the two verdicts to agree with Direction B's, and `E` to be recovered bit-identically.
* **Cross-implementation**: the same sample, translated into the artifacts' index space, passed to
  `dext.verify_witness`; require agreement on `decomposition_ok`, `zero_syndrome`,
  `nontrivial_logical`, `weight` and `Ewt`.

```
sector Z : samples 60   cells covered 32   roundtrip 60/60   cross-impl agreement 60/60
sector X : samples 60   cells covered 34   roundtrip 60/60   cross-impl agreement 60/60
cells span K = 0..8 and |E| = 12,14,16,18,20,22,24 in both sectors
```

The round-trip predicate includes `L^ext x != 0  <->  E not in rowspace(H_stab)`, i.e. it checks that
the **12-row logical basis is a faithful nontriviality detector**. It is — which independently
substantiates the wave-13 review's "surprise" that the CNF depends only on the 12-row basis and not
on the 1884-pool. (In my first pass I mis-seeded that basis from the *same*-type pool and got 59/60;
with the correct opposite-type basis, 60/60. I record the mis-step because the 59/60 was my bug, not
the artifact's.)

**The two recorded `d_ext <= 11` witnesses re-checked on my extended code.** From
`logs.../w11.out`, sector Z: check 48, k 0; sector X: check 18, k 0. My independently reconstructed
residual supports are `[54, 60]` and `[0, 22]` — **identical to the recorded ones** — and on my own
matrices both witnesses give `decomposition_ok=True, zero_syndrome=True, nontrivial=True,
weight=11, |E|=12`.

### 3.4 Two bindings to the actual certificates

1. **CNF hash reproduction.** I extracted the generator family mechanically out of the artifact
   markdown into an empty directory and ran `rebuild.py post` in a fresh namespace:
   **5/5 recorded CNF hashes MATCH, 0 mismatch** (`27abef7a…`, `32cf5a25…`, `6f4aa59d…`,
   `bfd07e4b…`, `151cecf0…`). This proves the code I diffed against my own build is the code that
   produced the logged certificates — otherwise a matrix-level diff would be diffing the wrong
   object.
2. **End-to-end semantic validation.** Running the *same* encoding with the residual columns
   disabled must return the plain code distance. It does, and the SAT witness must be a genuine
   weight-12 logical:

```
Z: W=11 UNSAT (34.1 s)   W=12 SAT, witness weight 12, in my exhaustive 1884-pool: True
X: W=11 UNSAT (34.6 s)   W=12 SAT, witness weight 12, in my exhaustive 1884-pool: True
```

The encoding reproduces `d(gross) = 12` exactly and its decoded witness lands inside a pool I
enumerated exhaustively by a completely different method. I could not construct a sub-query on which
the encoded question differs from the `d_ext` question.

---

## 4. SBB Thm 1 disposition (task-003(b)) — **VERIFIED, with two defects in the paper's write-up
that do not affect the route**

### 4.1 The statement, recovered verbatim

Theorem 1 is a *set of bounds*, not the single equality the route assumption paraphrases. Let `C` be
any single-ancilla CNOT-based SEC for a CSS code, `C'` a non-interleaved circuit obtained from `C` by
preserving the relative CNOT ordering within each check, `E = E_X ⊔ E_Z` their common complete
residual set. Then

```
(9)  d'_circ <= Delta(E)      for all E in E
(10) d'_circ <= d_ext(R)      for all R subset of E
(11) d'_circ  = d_ext(E)
(12) d'_circ <= d_circ
```

Only **(11)** is load-bearing here, and its hypotheses are (i) `C'` non-interleaved and (ii) the
**full** residual set `E`, not a subset. Both hold for this route: the candidate is an LRC, and the
certified extended code carries all `72*3 = 216` residual columns per sector.

### 4.2 The proof, step by step against the frozen model

`Prop 2` (eq. 9, upper bound via a single hook plus `Delta(E)-1` data errors) — sound, and **not
load-bearing** for this route.

`Prop 3` (`d_circ >= d_ext(E)` for **any** SEC — the direction that yields `d_circ >= 11`). Four
steps, all re-derived:

1. *CSS separation.* Valid: CNOT-only circuits map no `X` to `Z`/`Y`, so `Z`-type faults suffice for
   `d^Z_circ`, and `Y = XZ ≡ Z`.
2. *Perfect final round.* A **model assumption**, and it matches the frozen 公共定义's
   "理想最终读出边界" exactly.
3. *Fault-mechanism table.* I checked every entry by direct CNOT conjugation. The one entry that
   could break the argument is a two-qubit CNOT fault on a `data/Z-ancilla` pair, whose `Z_d ⊗ Z_a`
   component naively yields *two* extended-code columns from *one* fault — which would falsify the
   whole lower bound. The paper's Fig. 5 remark disposes of it: `Z_d ⊗ Z_a` after CNOT `i` equals the
   single hook `Z_a` before CNOT `i`, i.e. one residual column. I verified this identity and checked
   the remaining `Z`-restricted components (`Z_d ⊗ I` → one data column; `I ⊗ Z_a` → one residual
   column; `Z` on an `X`-ancilla → zero data columns, detector-only). **Every mechanism maps to at
   most one column.** The table is complete and correct for the standard circuit-level model.
4. *Counting.* `#mechanisms >= |x| >= d_ext`, robust to cancellation (two mechanisms hitting the same
   column only lower `|x|`) and to the choice of residual representative (`{4,5,6}` vs `{1,2,3}`
   differ by a stabiliser row, so their `H^ext`/`L^ext` columns are literally equal).

`Corollary 1` (`d'_circ <= d_ext(R)`, hence with Prop 3 the equality (11)) — sound, with the caveat
in §4.4.

### 4.3 Model comparison: no mismatch

SBB defines `d^X_circ`/`d^Z_circ` as "the minimum number of error mechanisms in an X-basis or Z-basis
memory experiment that flip no detectors but flip at least one logical observable",
`d_circ = min(d^X_circ, d^Z_circ)`, memory experiment = `m` noisy rounds followed by a perfect round.
The frozen 公共定义 says `d_circ(C) = min{|F| : F 不触发任何 detector,但翻转非平凡逻辑量}` under
"标准 memory experiment、相同 elementary-fault 权重和理想最终读出边界". These are the **same
definition**. Single-ancilla, one prep, one measurement, one CNOT per support qubit likewise
coincide. Two robustness notes I add:

* Prop 3's bound is `m`-independent, and Corollary 1's construction needs only `m >= 1`, so
  `d_circ = d_ext(E)` holds for every round count — no round-count caveat is needed here (this is
  logically independent of `CIRCDIST.sat`).
* Corollary 1's construction uses only data-side and ancilla-side components of CNOT faults, so the
  equality does not depend on whether idling faults are in the model. The frozen model does not
  enumerate its fault set; this makes that gap harmless.

### 4.4 Two defects found in the paper's write-up

**(D1) Mis-citation, twice.** Corollary 1's proof closes: "combining this result with **Proposition
2**, we obtain the equality `d'_circ = d_ext(R)` for the case when `R = E`", and the theorem's proof
closes: "the final equation of Theorem 1 follows from combining the results of **Proposition 2** and
Corollary 1". Both need **Proposition 3**, not 2. Proposition 2 is an *upper* bound (`d'_circ <=
Delta(E)`); no equality and no `d'_circ <= d_circ` can be obtained by combining two upper bounds. The
required lower bound `d'_circ >= d_ext(E)` and `d_circ >= d_ext(E)` is Proposition 3, proved
immediately above. **This is a one-word typographical defect, not a gap**: the needed statement is
present and proved in the same passage. Recorded because it is exactly the kind of thing an
"unverified external assumption" flag exists to catch.

**(D2) An unargued step that is real work for a staggered LRC.** Corollary 1's proof says: "by
introducing additional error-free idling operations on data qubits, it is possible to partition each
round of SEC into X and Z parts". For an *alternating-XZ* circuit this is immediate. For a
**left–right circuit it is not**: by SBB Fig. 3, `L_X` and `R_Z` execute *in parallel* for `t_1`
steps, so `X`-check and `Z`-check CNOTs are concurrent and no global cut of a round exists as drawn.
The step is repairable — an order-preserving re-timing exists whenever, on *every* data qubit, the
CNOTs of `Z`-instance `k`, `X`-instance `k`, `Z`-instance `k+1` are consistently ordered — but the
paper neither states that condition nor checks it, and "introducing error-free idling" understates
what is required (a re-timing, not padding).

**I closed (D2) for the candidate rather than leaving it open** (`src/partition.py`). On the
reconstructed depth-8 reading, for all 144 data qubits:

```
reading phi=(2,2) upper=X st=(0,1): qubits without a consistent instance order: 0 ; direction X<Z
reading phi=(2,2) upper=X st=(1,0): qubits without a consistent instance order: 0 ; direction Z<X
reading phi=(2,2) upper=Z st=(1,0): qubits without a consistent instance order: 0 ; direction Z<X
GLOBAL X/Z INSTANCE PARTITION EXISTS (order-preserving re-timing): True
```

Zero exceptions, one uniform direction per reading. The candidate is therefore genuinely inside
Theorem 1 (11)'s hypothesis. I also record the clean structural fact that makes this checkable and
that the artifacts do not state: **for the gross code every overlapping `(X,Z)` check pair shares
exactly 2 qubits, so (MC) on such a pair is *identical* to "the pair is not interleaved on its shared
support"** — the (MC) property that phicert verified and that I re-verified in §2.2 is precisely the
per-pair half of Theorem 1's hypothesis. (This does not resurrect the sbbcert review's refuted item
8: (MC) still does not imply SBB's *full* non-interleaving, which also constrains non-shared CNOTs.
The candidate satisfies the full notion because it is an LRC, and now, by the partition check above,
demonstrably so.)

**Disposition: (i) VERIFY.** The proof of the load-bearing equality re-derives against the frozen
model with no gap, subject to the two write-up defects above, one typographical and one closed by my
own check for this candidate. `sbb-thm1` merits upgrade from *unverified external assumption* to
**established external theorem with independently verified proof, scoped to (11) with `R = E` and to
non-interleaved circuits**. It remains an *assumption* in the protocol's sense (an external result
used as an interface), so the `assumptions` block stays; what changes is the `statement` text and the
loss of the "PROOF has not been independently verified in this project" clause.

---

## 5. Adjudication under `research/DAG_PROTOCOL.md` §3

The route is at `NUMERICAL`. `CERTIFIED*` = "an independently reviewed conditional result with
explicit unresolved premises or scope caveats"; §5 additionally requires a locatable independent
adversarial review of the assembled argument, hash-bound to the exact statement.

The chain is now: the compute verdict (`circdist_gross_verdict_20260823.md`) → wave-13 independent
review (`circdist_gross_verdict_review_20260823.md`, CONFIRM on 990-slot completeness, 990/990 UNSAT,
`d_ext = 11` both sectors, Figure 12 pixel-verified) → **this review**, closing the two clauses the
wave-13 review left PARTIAL and the assumption it registered:

| wave-13 status | now |
|---|---|
| link 3 (phicert legality filter) proposer-grade | **CONFIRM**, re-derived in a strictly larger reading space, uniqueness reproduced, one risk flag retired |
| link 4 (extended-code encoding) proposer-grade | **CONFIRM**, matrices identical, 120/120 round-trips, 5/5 CNF hashes, `d=12` semantic control |
| SBB Thm 1 unverified external assumption | **proof VERIFIED**, two write-up defects, one closed for this candidate by my own check |

Everything load-bearing for the route implication has now been independently reviewed, and the
surviving conditionality is explicit and finite. That is exactly `CERTIFIED*` and not more:
`PROVED` is unavailable because the UNSAT half is solver-grade, and because the certified object is
the class the reading filter *selects* — the filter is now shown to select it uniquely out of the
full `720`-per-panel space, but that is still a reconstruction of a published figure, not a statement
the authors wrote down.

**I license: route `candidate-certification` NUMERICAL → CERTIFIED\***, bound to
`sha256:4f40673227208c58d21650b3d685670019f5460b44ee52c0440b22293eec1598`.

**I do not license a node-level promotion.** The node claim also demands the second half —
"either an explicit interleaved schedule with certified `d_circ = 12`, or a proof that every legal
schedule satisfies `d_circ <= 11`" — which this route does not address at all. The node stays
`CONJECTURED`; only route `candidate-certification` moves.

### Caveat set to carry on the promoted route

1. **UNSAT verdicts are solver-grade, not LRAT-checked** (no DRAT toolchain on this machine).
   Unchanged; `task-003(c)` remains open.
2. **Reconstruction, not authorship.** The certified object is the residual-class triple pair that
   legality + (MC) + the paper's own cascade uniquely select from Figure 12. The selection is now
   shown unique over all `6!` edge maps per panel at all three periods, but it is a reading.
3. **Colour-map constraint is load-bearing and must be stated:** uniqueness holds for readings that
   assign one drawn colour to one group colour class in both panels. Relaxing that admits 12 further
   misaligned pairings (§2.4).
4. **`sbb-thm1` scope:** the equality used is (11), which requires the **full** residual set and a
   **non-interleaved** circuit. The route may not silently use it for interleaved schedules; for
   those only (12) `d'_circ <= d_circ` is available.
5. **Implication wording nit:** it is *two* 360-column extended codes, one per sector, combined by
   SBB Eq. (8) `d_ext = min(d^X_ext, d^Z_ext)` — not "a 360-column extended code". Recommend
   rewording; note that any rewording **invalidates the hash above** and requires re-binding.
6. **Inherited, unchanged:** the wave-13 cross-checking downgrade (114 truly multiply-decided, not
   860; 1026 records, not 3000; max 3 real decisions per sub-query, not 9) must be carried into any
   downstream write-up.
7. **Figure-12 fill-convention conflict** (wave-13, HARMLESS): unchanged; my sweep re-confirms
   invariance under the `upper = X`/`upper = Z` swap (both give the same object).

---

## 6. Limitations of this review

* I did **not** re-run the 990-slot UNSAT campaign; wave 13 reviewed it and I inherit that.
* I did **not** LRAT-check any certificate; no DRAT toolchain here.
* I did **not** re-verify Figure 12's pixels; that half is discharged and I consumed its 36 labels
  as given data. **If those labels are wrong, my LINK 3 conclusion falls with them** — my
  contribution is that *given* the labels, the filter's selection is unique.
* My (MC) condition quantifies over all round-instance offsets (`floor(d_1/t) == floor(d_2/t)`),
  which is *stricter* than the artifacts' single-round parity test. It admits the same 72 readings,
  so the difference is immaterial here, but the two are not the same predicate in general.
* The round-trip is a 120-sample check over 32–34 cells, not an exhaustive proof of encoding
  fidelity; combined with the exact matrix identity of §3.2 it is strong but not a theorem.
* My weight-12 enumeration is exhaustive *by construction* (the meet-in-the-middle split covers
  `|u| <= 6` and `|v| <= 5`, which is all of `|u|+|v| = 12`); its correctness rests on that argument
  plus the independent agreement of the resulting 1884 with two prior methods.
* Proposition 2 and eq. (9)/(10) of Theorem 1 were read but not exhaustively stress-tested, since
  they are not load-bearing for this route.
* I ran the artifacts' generator modules in a `venv` to diff against; a defect confined to a module
  I did not extract (e.g. the drivers) would be outside this review's scope.

---

*Reviewer: Opus 5, fresh independent adversarial context, 2026-08-23. Compute secured under
`artifacts/logs_circdist_gross_links_20260823/` with `SHA256SUMS.txt` (31 files, all verifying).
0 processes left running. No canonical file modified.*
