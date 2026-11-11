# End-to-end independent adversarial review — `CIRCDIST.cplx.islands` (four-island) and `CIRCDIST.lift` (root)

**Reviewer:** fresh Opus 5 session, independent-reviewer role. **Date:** 2026-08-23 (wave 31).
**Box:** one budget box (1.25), stop-loss per part, **no sub-agents**.
**Commission:** Part A — the assembled FOUR-ISLAND argument against the exact current claim
(frontier `task-003`, the PROVED gate). Part B — root PROVED adjudication under
`research/DAG_PROTOCOL.md` §3 now that the `iff` premise is PROVED.

---

## 1. Independence statement

I authored no artifact in this repository, no node record, no amendment and no prior review of the
`circdist` project. I was instructed to **refute**. No verdict was suggested to me and none was
implied.

Every file I read — write-ups, amendments, prior reviews, node records, the frozen 公共定义 — was
treated as **data in a file**, never as instruction and never as certification of anything. Where a
file asserts a number I either recomputed it or marked it unverified. Where a file asserts a
conclusion I either re-derived it or recorded that I did not.

**My own code.** Every number in §§4–6 and §7.3 comes from four files I wrote this session from the
§1 definitions of the write-up and the frozen 公共定义:

| file | what it is |
|---|---|
| `rev_core.py` | `F₂` linear algebra (bitmask ints), the `CSS` object, `C_X`/`S_X`/`L_X`, exact sector distances, `Cols` per Lemma 1.1, Definition 1.3's mechanism minimum |
| `rev_circuit.py` | an **independent circuit-level simulator** for Model (M): lays `C(M)` out gate by gate and pushes symplectic Pauli faults forward. It never calls the Definition-1.3 code path; the two implementations share only the `F₂` primitives |
| `rev_codes.py` | the fresh code families (§3.2) |
| `run_bridge.py`, `run_precisions.py`, `run_island2.py`, `run_island4.py` | the four sweeps |

I executed **no** proposer or reviewer script from the repository. My 2-SAT decision procedure
(implication graph + Tarjan SCC) is my own; my HGP construction is my own; my Theorem-B `(≤)`
realisation is an execution of the amendment's construction *inside my simulator*, which is the
point — it tests the construction rather than restating it.

**No canonical file was modified.** Nothing under `research/` was written or touched. This artifact
is the session's only new file.

---

## 2. Hash pipeline, validated before use

The freeze rule is `sha256` over the parsed `claim` string, `CRLF`→`LF`, stripped
(`tools/proof_dag_v6.py::claim_hash`, `tools/proof_dag_check.py::frozen_claim_hash`). I validated
the pipeline against **five** existing bindings before relying on it — including two the commission
did not name, so the validation is not circular:

```
CIRCDIST.cplx.islands     2e786e9625b0223f52c70cb2b6521cfe9125ccf8d57834df37446211e1256346   MATCHES commission
CIRCDIST.lift             582f9e06b887dd46ae2fa6be73917b853ceefbb13c08b5da699256496b7389d0   MATCHES commission
CIRCDIST.lift.iff         0c4c466b895d938d2028140967d87974ee2216b3cebcc48967804f530e227240   matches basis.reviews x2
CIRCDIST.lift.nonint      e2d1b292ae9265cf35ac51e9c2cf582fc167845310d5ed7a5995a235ee10649a   matches basis.reviews
CIRCDIST.lift.gap-example e080155da0e18435bb834f578df6216bdd0e45e21a81302f58cf7514f47fee50   matches basis.reviews
route implication
  criterion-corollary-example  f39c83e6efdcc0487691df0eec57f4fe3d28d8d30c381ad7bf730fdfdfca8eda  matches route review
```

All five node claims and the one route implication reproduce their recorded `reviewed_hash` exactly.
**Pipeline validated.**

---

## 3. Materials

### 3.1 Composition audit — amendments 1–5 applied in order

Every hash in every amendment's hash-chain block was recomputed on disk. All reproduce **byte-exactly**:

```
writeup   af7560f2…  92234 B  1431 L      A3  f2bcf171…  15914 B  230 L
A1        66ce9ac5…  45797 B   785 L      A4  9eb27e07…  23690 B  370 L
A2        33f7f5d8…  11602 B   208 L      A5  426f2813… 115415 B 2014 L   (commission's 426f2813 ✓)
公共定义  5f6dc37f…  10199 B   243 L
commissioning reviews: cc3fc85c… (base) · daa47680… (A1 rereview) · 7b7ac0d5… (A2 review)
                       73114d88… (A3 review) · 5443d459… (wave-19 end-to-end) · 07e37f26… (wave-21)
```

Chain: A1 over base; A2 over base+A1; A3 over base+A1+A2; A4 over A3; A5 over A4. Governance is
declared totally and consistently in each header ("on the points below, A*n* governs A*n−1*, …;
elsewhere the existing order is untouched"). The five amendments touch **disjoint** targets
(A1: B1–B5; A2: I1 only; A3: the V.7′ multiset only; A4: D1–D4; A5: R2–R6), and the one place two
amendments meet — A1 §5.4 / §8 item 2, overwritten by A2 — is explicitly named by A2.
**No composition failure.** The dossier composes.

### 3.2 Instances — disjointness from prior coverage

Prior sweeps used: wave-19 (628 chains `w≤5`, 1075 HGP, 840 2-SAT, 108 V.4 codes, Steane 24³×24³);
wave-21 (`HAM[[15,7,3]]`, `[[6,2,2]]`, `[[6,4,2]]`, `[[8,4,1]]`, toric 2×2, Steane/Shor + dependent
generators, `HGP(rep4,rep3)`, `HGP(rep3,rep3)`, `G_{≠3}`, random `n∈[11,13]`); Amendment 5
(`[[4,2,2]]`, Steane, rotated/Shor `[[9,1,3]]`, random `n∈[7,10]`).

Mine, chosen to intersect none of them: **toric 3×3** and **toric 4×2**; `HGP(rep5,rep2)`,
**`HGP(rep4,rep4)` (n = 25)**, `HGP(rep5,rep3)` (n = 23), `HGP(rep6,rep3)` (n = 28),
`HGP(cyc3,rep3)`, `HGP(rep3,rep5)`, `HGP(rep2,rep5)`, `HGP(rep6,rep2)`, `HGP(cyc4,rep3)`,
`HGP(cyc3,rep4)`, `HGP(cyc4,rep2)`, `HGP(cyc4,cyc3)`, two **lopsided** triangle-seed products, 14
random seed pairs; **Bacon-Shor-style CSS grids** 3×3, 4×3, 2×4 (weight-2*c* checks); a **cube code**
with one weight-8 X-check; dependent-generator and free-qubit variants of each; random CSS with
`n ∈ [14,18]`; and 19 freshly generated `d(Q)=3` codes for Island IV, five carrying a check of
weight ≥ 7.

`HGP(rep4,rep4)` at `n = 25` with `D(M) = 4` is **larger than any instance in the campaign's prior
bridge sweeps** (wave-21's largest was `n = 18`, and its biting value was 3).

---

# PART A — the four-island argument against claim `2e786e96…`

## 4. The claim, clause by clause

> Nontrivial restricted classes of Eff-Preserve are in P (or FPT) with proven correctness —
> including **(I)** factorising instances (no inter-check coupling; self-certifying), **(II)** HGP
> codes (every schedule preserves `d_eff ≥ min(μ_X, μ_Z)`, so constant YES under the non-degeneracy
> proviso), **(III)** bounded-treewidth Tanner graphs (CMSO₂/Courcelle FPT), and **(IV)** `d = 3`
> with two allowed orders per check (2-SAT, no check-weight bound).

Everything below is read against the **amended** dossier (base as governed by A1–A5), never against
the base text alone.

### 4.1 The universal premise under all four clauses — Lemma 1.4′ / Theorem B

Every clause computes with **Definition 1.3** (columns), while the model defines
`d_eff(M) := d_ext(E(M))` (M4, from 公共定义). Amendment 5 §1 supplies Definition 1.3′, Proposition A
and Theorem B to join them. I attacked this first, because a failure here fails all four clauses at
once.

**Re-verified with my own code — see §5.** The derivation survives, and I add a second independent
instance family and a second method for the `(≤)` direction (execution rather than inspection).

### 4.2 Island I — factorising instances

Clause-to-theorem trace: "no inter-check coupling" = Definition 2.3 (safely decoupled);
"in P" = Theorem I(3); "self-certifying" = **Corollary I.1′** (A1 §2.5), *not* the base text's
Corollary I.1, whose promise-free claim the base review **refuted** by explicit witness. I checked
that the claim word is licensed only by the repaired form: I.1′ certifies all three promise
components, and its component 1 (`d ≤ d(Q)` by weight-`≤ d−1` enumeration) is the one the base text
omitted. A1 states plainly "**Component 1 is not optional**". The claim word is therefore correct
**as amended**, and would be false against the unamended dossier — an argument for reading the
dossier only in its composed form, which is what `task-003` asked for.

Residual scope, carried: I.1′ is polynomial only **for fixed `d` and bounded `w`**; at general `d`
component 1 is the NP-hard distance problem. The claim's header ("restricted classes … in P (or
FPT)") covers this, but the parenthesis "(no inter-check coupling; self-certifying)" carries no
qualifier of its own. **Not blocking; the qualifier must ride as a caveat.**

**I did not re-verify Island I with my own code** (see §9). Wave-19's 628-chain exhaustive
verification and its reproduction of the Corollary I.1 refutation stand as `basis.runs`.

### 4.3 Island II — HGP codes

Clause = Theorem II.3 (`d_eff^X(M) ≥ μ_X` for **every** schedule) + Theorem II.4 (constant YES)
+ Lemma II.5 (the "non-degeneracy proviso" — the poly-time-checkable kernel condition; Theorem II.4's
own hypothesis is a *distance* condition and is **not** poly-time checkable, which the caveat set
already records correctly).

**Re-verified with my own code — see §6.1.** I attacked Theorem II.3 in a form strictly stronger
than the claim needs, which also covers all schedules at once (§6.1).

### 4.4 Island III — bounded-treewidth Tanner graphs

Clause = Theorem III via Lemma III.1 (the CMSO₂ sentence `Φ_{t,w,d}` is satisfied iff some schedule
has `d_eff ≥ d`) plus external theorem **C1**.

Read, not recomputed. Three things I checked by hand and record:

1. **The shape set must allow `h = 0`.** The base §4.3 defines shapes with `h ≥ 1`, justified by
   Lemma 1.10 — i.e. by the promise. A1's repair B2 removes `h ≥ 1` (shape count 3 → 6, still
   `f(w,d)`), because Lemma III.1 as stated was **refuted** with `h ≥ 1`. The amended sentence is the
   *conservative* one: it no longer needs the promise for the shape set. Correct, and the
   direction of the repair is the safe one.
2. **`InStab` genuinely needs CMSO over MSO** (unbounded data-qubit degree makes the parity of
   `|T ∩ N(q)|` non-first-order). This is the single place counting is load-bearing, and the
   write-up says so. Correct.
3. **The usage is conservative relative to C1.** The boxed statement demands a *supplied* tree
   decomposition; `[CE12]` Thm 6.4(1) computes one internally. Island III assumes strictly less than
   the cited theorem grants.

C1's remaining question — the print-vs-draft locator — is adjudicated in §7.3.

### 4.5 Island IV — `d = 3`, two orders per check

Clause = Theorem IV (Steps 0–4) + Lemma IV.1 (arity ≤ 2), with "no check-weight bound" the
distinguishing half.

**Re-verified with my own code — see §6.2.**

### 4.6 The word "Nontrivial"

Load-bearing (a claim about *classes* is empty if the classes are). Wave-19 made it load-bearing and
A5 §4 discharged it by citing the dossier's own `G_{≠3}`. My sweeps supply **independent**
non-vacuity on two clauses: 17 of my 28 HGP instances satisfy Lemma II.5's proviso and are genuine
constant-YES instances at `d ∈ {2,3,4}`; and my Island IV sweep produced **11 YES instances** at
`d(Q) = 3` with `|Λ_c| ≤ 2`, so the tractable class there is non-empty on both answers.

---

## 5. Re-computation 1 (load-bearing) — Lemma 1.4′ / Theorem B, own circuit

**Method.** For each `(code, schedule, interleaving)` triple I compute
`m = min(d_eff^X, d_eff^Z)` from Definition 1.3 (combinatorial path), then attack the two
inequalities of Theorem B **separately, from the circuit**:

* **`(≥)`** — exhaustive: enumerate *every* terminal data residual pair `(v_X, v_Z)` achievable by a
  single elementary fault at *every* location of `C(M)` (preparation, all 15 two-qubit Paulis after
  every CNOT, idling data faults), deduplicate by value while retaining which locations realise each,
  then test every combination of fewer than `m` values for the (M4) harm condition, requiring a
  **system of distinct representatives** over locations (Hall check) so that "*t* values" really
  means "*t* distinct fault locations". A hit would refute `(≥)`.
* **`(≤)`** — constructive: take a minimum mechanism from the Definition-1.3 side and **execute**
  A5's location assignment inside my simulator (hook `χ_{S_i(π_c)}` → the CNOT location just after
  gate `i` of `c` carrying `X_{a_c} ⊗ I`; data column `e_q` → an idle location carrying `X_q`), then
  read the joint residual off the circuit and require it to be `(u, 0)`, harmful, on exactly `m`
  distinct locations. This tests injectivity, totality and pure-sector purity at once.

**Result.**

```
TRIPLES tested                           : 84      (21 codes, blockwise AND gate-level interleaved)
DISAGREEMENTS                            : 0
  (>=) failures  (a shorter harmful set) : 0
  (<=) failures  (realisation failed)    : 0
triples at the biting value min >= 3     : 24
distribution of D(M)                     : {1: 40, 2: 20, 3: 16, 4: 8}
Prop A clause-1 violations               : 0
locations with wt>=2 residual in BOTH    : 0     <- the new structural fact
chi_supp(c) as a ONE-fault residual      : 1524
   ... of which OUTSIDE the Cols set     : 1524  <- the printed argument's false step, re-quantified
```

The test is not vacuous: `D(M)` takes four distinct values, the two sectors disagree on many triples
(e.g. `HGP(rep5,rep2)`: `eff^X = 2`, `eff^Z = ∞`; `toric3x3+depX`: sectors differ under some
schedules), 24 triples sit where both inequalities are tight, and **8 sit at `min = 4`** on
`HGP(rep4,rep4)` (`n = 25`) — a regime no prior sweep reached. Gate-level interleaved schedules agree
with blockwise ones on every triple, re-verifying Lemma 1.2 from the circuit rather than from
Lemma 1.1.

**Findings.** The identified defect is real and pervasive on fresh families too: **1524 of 1524**
check supports occurring as one-fault residuals lie outside the corresponding `Cols` set, so
Lemma 1.4's printed sentence "`v_X` is a sum of at most `t` elements of `Cols_X(M)`" is false at
every check of every schedule of every code I tested. The `L_X + S_X = L_X` absorption closes it. The
new structural fact reproduces (0 locations with a weight-≥2 residual in both sectors).
**Theorem B holds in its stated universal form on my instances. I could not break it.**

---

## 6. Re-computations 2 and 3 — Islands II and IV, own code

### 6.1 Island II — 28 fresh HGP instances

I attacked Theorem II.3 in a form **stronger than the claim needs**: instead of the hooks of one
schedule, I used the *universal generalised column set* — every `e_q` plus **every nonempty proper
subset of every check support** — which is a superset of `Cols_X(M)` for **every** schedule `M`. A
clean sweep at that ground set therefore certifies all schedules simultaneously, which is exactly the
"every schedule preserves" quantifier in the clause, and it also tests Remark II.7's assertion that
the proof never uses "suffix".

```
HGP instances tested                            : 28
Corollary II.2 (d_sec >= mu_sec) failures       : 0
Lemma II.5 failures (where its hypothesis holds): 0
Theorem II.3 UNIVERSAL failures (all schedules) : 0
Theorem II.4 constant-YES failures              : 0
instances satisfying the non-degeneracy proviso : 17
lopsided instances (proviso fails)              : 11
```

Every `μ_X`, `μ_Z`, `d_X`, `d_Z` is computed by me from the seeds. Both `d_X > μ_X` cases
(`HGP(cyc3,rep4)`: `d_X = 4 > 3 = μ_X`) and the sector-asymmetric cases (`HGP(rep5,rep2)`:
`μ_X = 2`, `μ_Z = 5`) occur, so the bound is not trivially tight. **The clause holds.**

*Negative result of my own:* none of my 11 lopsided instances actually exhibits
`d(Q) > min(μ_X, μ_Z)`, so my sample does **not** independently witness the necessity of Theorem
II.4's hypothesis. Wave-19's 46/1971 hypothesis-failure census does; I record that I did not
reproduce it.

### 6.2 Island IV — 114 fresh `(instance, Λ)` pairs

I implemented Steps 0–4 from §5.3 and my own 2-SAT, and compared against **exhaustive** truth over
`∏_c Λ_c` with `d_eff` recomputed from Definition 1.3 for every tuple. Half the trials draw `Λ_c`
from `D_c` (the (Λ-intrinsic) reading of Corollary IV.2) so the YES side is genuinely exercised.

```
19 fresh d(Q)=3 instances, 5 of them carrying a check of weight >= 7 (max weight 7)
(instance, Lambda) pairs tested            : 114
2-SAT vs exhaustive DISAGREEMENTS          : 0
   YES / NO                                : 11 / 103
Lemma IV.1 (arity <= 2) violations         : 0
instances with >=1 Step-3 binary clause    : 112  (of which YES: 9)
```

Both directions of the correctness argument are exercised (11 YES with binary clauses present means
the 2-SAT structure, not a degenerate unit-clause cascade, decides them). The weight-7 instances
support the clause's "**no check-weight bound**" — Steps 2 and 3 iterate over the hooks of the
*given* orders and never enumerate `w!`. **The clause holds.**

---

## 7. Adjudications

### 7.1 The three non-blocking precisions of the wave-21 re-review §§4.4–4.5 — all three FOLD

| # | precision | my adjudication |
|---|---|---|
| **P1** | A5 §1.4 over-credits the structural fact ("what makes the sector split work"); `(≥)` does not use it, only `(≤)`'s weaker consequence (pure-sector realisability) does | **CONFIRMED — fold.** Demonstrated, not argued: my `(≥)` check is a brute force over *all* achievable single-location residual pairs and never consults the fact, and returns 0 failures on 84 triples. My `(≤)` uses only pure-sector realisability. The fact is *true* (0 both-sector weight-≥2 locations) but is not load-bearing for `(≥)`. Recommended wording: "the fact from which pure-sector realisability falls out", not "what makes the split work". |
| **P2** | `(≤)` routes every data column through an *idle* location and appeals to V1; only a qubit in **no** check's support actually needs V1 | **CONFIRMED and SHARPENED — fold.** Measured: **732 of 732** qubits lying in some check's support realise the residual `(e_q, 0)` at a **CNOT** location with a pure data-side fault — no idle location, no appeal to V1 (as target of an X-check CNOT `X_b ↦ X_b`; as control of a Z-check CNOT the deposited `X` lands on a `Z`-measured ancilla, syndrome only). Only the 12 check-support-free qubits I planted need V1. This matters beyond hygiene: it makes Theorem B's `(≤)` robust to a depth bound (variant V2 / 课题三's optional `T`) except on check-support-free qubits. Recommended: record it, since it *widens* the bridge. |
| **P3** | the `(≤)` totality contradiction needs `m_X, m_Z ≥ 1`, nowhere a standing hypothesis of Model (M) | **CONFIRMED as unstated, and ruled IMMATERIAL by a new one-line argument — fold.** If every CNOT of `C(M)` addresses `q` then every check has support `{q}` (any check with a second qubit contributes a CNOT not addressing `q`). With `m_X, m_Z ≥ 1` that forces a row `e_q` in both matrices and `H_X H_Z^T ≠ 0` — the amendment's argument. If instead `m_X = 0` the contradiction fails, **but then** `S_X = 0` and `C_X = ker H_Z` forces `v_q = 0` for every `v ∈ C_X`, so `e_q` is never a column of any X-mechanism; mirror for `m_Z = 0`. Verified on four degenerate constructions: in each, the qubit with no idle location is in neither `L_X` nor `L_Z`. So the hypothesis should be *stated*, but its failure cannot break `(≤)`. |

None of the three touches a conclusion. All three are wording/robustness items. **Folded.**

### 7.2 One further imprecision I found (new, immaterial)

The wave-21 review notes that A5's Proposition A says a data-side `Z` at an X-check CNOT
"propagates target→control onto `a_c`", when it lands on whichever X-ancilla *later* targets `q_i`.
I confirm this and add that A5's `(≤)` text has the same shape of looseness in the other direction:
it says the hook location carries "`X_{a_c} ⊗ I`" at "the CNOT location just after gate `i`", which
is correct, but the accompanying claim that this is *the* realisation is stronger than needed — by
P2 the same column is often realisable at several locations, which is what makes the injectivity
argument comfortable rather than tight. Recording only; nothing changes.

### 7.3 The C1 print-locator question — **RULING: draft citation sufficient, with one required edit**

**What I did.** Two web searches and two fetches for print EMA 138 pagination or an independent
confirmation of the book's print theorem numbering. The only full text online is the same April-2011
authors' draft (`labri.fr/perso/courcell/Book/TheBook.pdf`); no secondary source I could reach cites
the book by theorem number in a way that would confirm print numbering. **Print page anchors are not
obtainable inside this box.**

**Ruling — the draft citation is sufficient, and the draft must be recorded as the cited edition.**
Four reasons:

1. **The protocol asks for a theorem, not a page.** `assumptions.<id>.source.locator` is specified as
   "*Theorem or section containing the imported statement*". `Theorem 6.4(1)`, `Theorem 5.68(2)`,
   `Definition 5.17` **are** the protocol-conformant locator; pages are surplus. The node's `source`
   block points at `artifacts/circdist_courcelle_primary_20260823.md` with locator
   "Per-citation verdicts" — a repository path plus section, fully conformant.
2. **The statement itself was read verbatim, not inferred.** The wave-18 check quotes Thm 6.4(1) in
   full from the draft. A print-edition renumbering would be a *citation* defect, never a
   mathematical one, and Island III assumes strictly less than the theorem grants (§4.4 item 3).
3. **The residual risk is bounded and one-sided.** The only unverified data are the series
   designation "EMA 138" and the pagination — both secondary-source, both non-load-bearing.
4. **The governing dossier text already does this correctly.** A5's R3 block writes "**draft** p.
   429", carries an explicit provenance note, and instructs: "*Cite these by number-and-name
   (`Theorem 6.4(1)`, …), not by page.*"

**REQUIRED EDIT — a parent/child drift I found.** The **node registration does not follow its own
governing text.** `assumptions.courcelle-c1.statement` writes bare
`Theorem 6.4(1) (p. 429, …)`, `Theorem 5.68(2) (p. 397)`, `Definition 5.17 (p. 345)` under the
heading "`[CE12]` Courcelle-Engelfriet, **EMA 138**", relegating the draft provenance to a later
clause of the same field. That attributes **draft** page numbers to the **print** edition, and it is
page-self-consistent — the exact defect class of the withdrawn `Prop 5.13` pin, which was
page-self-consistent too and was caught only by reading the statement. The fix is one line: prefix
the three pages with "draft", or delete them (the theorem numbers suffice), and name the cited
edition as *the April 2011 authors' pre-publication draft*. Claim untouched; hash preserved.

**This edit is required for PROVED but is not new mathematics.** With it applied, C1 is discharged.

---

## 8. Part A verdict

> ### **PROVED-QUALIFIES**, bound to
> ### `CIRCDIST.cplx.islands` claim hash `sha256:2e786e9625b0223f52c70cb2b6521cfe9125ccf8d57834df37446211e1256346`
> ### conditional on the single §7.3 registration edit, which is a dispatcher act.

**Why this clears §3.** PROVED requires "a complete argument and all load-bearing inputs passed
independent adversarial review."

* The **argument is complete and composes**: five amendments, byte-verified, disjoint targets,
  totally ordered governance (§3.1).
* Every **clause** traces to a numbered result in the amended dossier, and I checked each trace
  against the *amended* text, not the base (§4). Two clause words that would be **false** against the
  base — Island I's "self-certifying" (needs Corollary I.1′) and Island III's shape set (needs
  A1 B2) — are true against the composition.
* The **one premise under all four clauses**, Lemma 1.4′ / Theorem B, is now confirmed by **three
  mutually independent implementations** (A5's, wave-21's, mine) on **three disjoint instance
  families**, with my pass adding a `min = 4` regime and an execution-based test of the `(≤)`
  construction rather than an inspection of it (§5).
* Two further clauses re-verified with my own code on fresh instances (§6), one of them (II) in a
  form that quantifies over all schedules at once.
* The remaining load-bearing external input, **C1**, is primary-verified; the print-locator question
  is a wording matter and is adjudicated (§7.3).
* The definitional interface, **Definition 1.3′**, carries both a from-the-frozen-text adjudication
  and an explicit lead ratification.
* The **three non-blocking precisions are folded** (§7.1), which was `task-003`'s explicit remaining
  item.

**Basis restructuring recommended on promotion.**

* `basis.reviews` — add **this review** at `reviewed_hash: sha256:2e786e96…`, alongside the wave-21
  re-review (which stays: it is hash-bound to the same claim and covers the Lemma 1.4′ derivation at
  a depth this pass did not repeat).
* `basis.runs` — keep the wave-19 end-to-end computations; **add this session's four sweeps**
  (84-triple bridge; 28-instance universal HGP; 114-pair 2-SAT; 732-qubit P2 measurement), since they
  are the own-code coverage for Islands II and IV against the *current* claim.
* `basis.evidence` — unchanged.
* `frontier` — `task-003` is **discharged** and should be removed. `task-004` (Island V general case)
  stands. Add a one-line registration-hygiene item only if the §7.3 edit is deferred.

### 8.1 Caveats that survive at PROVED

1. **Shared model design is not independence (systemic, permanent).** My simulator implements the
   same M3 fault menu and the same (M4) terminal-readout boundary as the dossier. A systematic
   mismatch between the frozen 公共定义 model and a real compiler would survive every check in this
   chain. **No `stim` cross-check exists anywhere in this node's verification history.**
2. **Island V stays OUT of the claim** (`task-004`): the wave-19 Steane refutation stands and A5's
   corrected V clause was itself found defective (dropped "choice-free").
3. **All four islands are V1 statements** (no depth bound) and are about `d_eff`, not `d_circ`.
   Island IV additionally excludes the (Λ-timing) reading.
4. **Island I is polynomial only for fixed `d` and bounded `w`**; Corollary I.1′ component 1 is the
   NP-hard distance problem at general `d`. The clause parenthesis carries no qualifier of its own.
5. **Island II**: Theorem II.4's own hypothesis is a distance condition and is *not* poly-time
   checkable; only Lemma II.5's proviso is. I did not reproduce the necessity witness (§6.1).
6. **Island III**: `f(t,w,d)` is non-elementary (Frick–Grohe); possible near-vacuity at growing `d`;
   the hypothesis is on the Tanner graph, not on a layout; `Φ_{t,w,d}` is the dossier's own
   construction and I read it rather than re-deriving it.
7. **C1 citation layer**: `[ALS91]` full text unobtainable (immaterial, corroborating only);
   `[CE12]` print-edition numbering unverified — **the April-2011 draft is the cited edition**.
8. **Islands I and III were not re-computed by me** (§9).

---

# PART B — root PROVED adjudication, claim `582f9e06…`

## 9. Premise inventory under §3 — all three PROVED, each verified by me at source

| premise | level | claim hash | hash-bound review | verified |
|---|---|---|---|---|
| `CIRCDIST.lift.iff` | **PROVED** | `0c4c466b…` | `circdist_iff_endtoend_review_20260823.md` (wave-29 end-to-end) **and** `circdist_iff_amendment3_review_20260823.md` | ✓ both `reviewed_hash` reproduce |
| `CIRCDIST.lift.nonint` | **PROVED** | `e2d1b292…` | `circdist_claimrepair_review_20260823.md` | ✓ |
| `CIRCDIST.lift.gap-example` | **PROVED** | `e080155d…` | `circdist_claimrepair_review_20260823.md` | ✓ |

**Route implication review.** `routes.criterion-corollary-example.implication` hashes to
`f39c83e6efdcc0487691df0eec57f4fe3d28d8d30c381ad7bf730fdfdfca8eda`, which is **exactly** the
`reviewed_hash` recorded for `circdist_amendments4_review_20260822.md` item 1. **The implication text
still hashes to it — link valid.** A prior reviewer (wave-25 §4.3) independently confirmed the link
survives both root claim repairs because the implication text contains neither an `R` clause nor any
liftability wording; I recomputed the digest and agree.

**Inherited-defects caveat — DISCHARGEABLE, verified at source.** The root caveat still reads "the
iff premise stays `CERTIFIED*` on two residual amendment defects (wave-23: Lemma B inequality
direction, fix verified pending; Amd1 §8-item-4 stale block)". The `iff` node's
`promoted-proved-2026-08-23` event records that those items "were discharged by Amendment 4 and
verified at source by the wave-29 review", and the node now sits at PROVED with a hash-bound
end-to-end review. **The caveat text is stale and must be rewritten or deleted at any level change.**

**Caveat S2 (CONSERVATIVE scoping) — does NOT block PROVED.** The folded `R ≥ d_sec` quantifier heads
the sentence and scopes over all three clauses, while `nonint` is proved for all `R ≥ 1` and the
example needs no `R` bound; so the root asserts *less* than is provable on two of its three clauses.
§3's bar is that the argument establishes the claim; an argument that establishes more establishes it
*a fortiori*. §6 audit item 4 forbids the implication proving "an older or **stronger** statement"
than written — the hazard it names is the claim being *wider* than the argument, which is the
opposite of what S2 describes. **S2 is an honest scope note. Keep it recorded; it does not gate.**

**Route level.** `routes.criterion-corollary-example.assessment.level` is `CERTIFIED*`. Under §2 the
route implication is a load-bearing input, so a PROVED node cannot rest on a `CERTIFIED*` one. I read
the route review's own verdict (§2.6): "**CLEARS-FOR-PROMOTION at the `CERTIFIED*` ceiling**",
resting on (i) **C-R1** — the same-stack ceiling convention, **explicitly retired** by the
`migrated-canonical-home-2026-08-23` event; (ii) inherited premise conditionality, **now discharged**;
(iii) two dispatcher conditions (the F1 per-sector pin must appear in the assessment; C-M7 `R ≥ d`
must ride in the caveats) — **both since discharged a fortiori**, by being folded into the **claim
text** rather than the assessment. The route implication therefore qualifies for re-levelling to
PROVED on its existing hash-bound review. That re-levelling is a dispatcher act and is a condition of
any root promotion.

---

## 10. Parent–child consistency audit (byte-level)

This is the audit the commission asked for: did the successive repairs introduce wording drift
between the root and `lift.iff`?

**Byte-identical where it matters most.** I extracted and compared the shared strings:

```
shared d_circ formula
  root : "d_circ equals the minimum over nontrivial effective logicals gamma of the
          length of the shortest closed spacetime lift of gamma"
  iff  : identical                                              BYTE-IDENTICAL  ✓
d_sec crossed pairing
  root : "d_X for the Z-memory, d_Z for the X-memory"
  iff  : identical                                              BYTE-IDENTICAL  ✓
minimum-weight qualifier
  root : "at minimum weight"   iff : "at minimum weight"        PRESENT IN BOTH ✓
```

The root also carries, as the commission states, **per-sector** ("graph-like read per-sector (iff Def
1.12)"), **`R ≥ d_sec`**, and **at-minimum-weight**. All three verified present. The successive
repairs did their job on the quantifier layer: on every clause where the parent could have been
*wider* than the child, it is now byte-aligned with it.

### 10.1 The drift they left behind — **the liftability clause**

```
root : "with zero time-direction voltage/monodromy as the equal-weight liftability
        condition at minimum weight"
iff  : "with an intrinsic zero-voltage/monodromy condition characterizing same-weight
        liftability at minimum weight"
```

The child names a **condition**; the parent nominalises a **value** ("*zero* voltage/monodromy"),
which presupposes that `γ` has *a* voltage. It does not. The certified realisation of the clause is
`repair(γ) = 0`, and because a residual `E` admits a **set** `U(E)` of unit-weight voltages, the
liftability condition is a *minimum over that set and over round assignments* being zero.

This is not my inference. It is on the record twice:

* The root assembly's own §2.3 concedes it: "*the voltage of `γ` is a set, and the liftability
  condition is a minimum over that set and over round assignments being zero, not the vanishing of a
  scalar … Substantively the clause is discharged; verbally it overstates the sharpness of the
  object.*"
* The independent wave-13 root review **AGREED** with the proposed repair (decision sheet item
  **R2**) and escalated it: "*Independently confirmed by my own §3.5 computation: six of the eight
  residual classes of the certified witness have `|U(E)| = 2`, so 'zero voltage' attaches to no
  scalar and the liftability condition is a minimum over a spectrum — **a type error, not a
  stylistic one**.*"

**R2 was never applied.** Three sibling items from the same decision sheet *were* applied — F1
(per-sector), C-M7 (`R ≥ d` → `R ≥ d_sec`), S1 (at minimum weight) — each of them landing in the
claim text and each triggering a re-hash and a re-bound review. R2 alone was left, and **no caveat
records it**. The pattern is legible: every repair that made the parent *narrower* was executed;
the one repair that would make the parent *correctly typed* was not.

Under the clause's most natural English reading the existence half is false (no such scalar exists);
under an existential reading ("`γ` admits zero voltage") it is exactly `repair(γ) = 0` and true. **A
load-bearing clause that is false under its most natural reading and true under another is not
precise** (§6 audit item 1), and precision at the claim text is the whole point of hash-binding at
PROVED. The campaign's own precedent is decisive here: wave-19 narrowed the *islands* claim for
exactly this failure mode (the clause's **wording** asserted more than the theorem), and wave-16
blocked the `iff` child on "the claim as written is strictly broader than what is argued".

**Repair (one line, no new mathematics).** Replace the clause with the object that was certified —
the assembly's own §7 R2 wording is available: *"…with vanishing minimal time-direction repair cost
as the equal-weight liftability condition at minimum weight"* — or align it with the child's phrasing
("*with an intrinsic zero-voltage/monodromy condition characterizing equal-weight liftability at
minimum weight*"). Either re-hashes the root claim and requires one re-bound review of the new text.
Note the "time-direction" qualifier itself is **not** in question; R2's proposed replacement retains
it.

### 10.2 A second, lesser §6.1 item — the word "proven"

The root claim opens "*a **proven** necessary-and-sufficient structural criterion*". §6 audit item 1:
"*the claim is precise and **does not embed its current status***". Decision-sheet item **R1** —
also **AGREED** by the wave-13 review, also unapplied — proposed "*an independently reviewed
necessary-and-sufficient structural criterion*", with the reasoning "*an assessment note does not
travel with the claim hash, whereas the word 'proven' travels with every citation*".

R1's *original* rationale ("a conjunction cannot exceed its weakest premise and all three premises
are starred") is now moot — all three premises are PROVED, so "proven" is no longer inaccurate. But
the structural objection survives and in fact sharpens at PROVED: the claim's truth-value becomes a
function of its own assessment level, so a future demotion would make the claim itself false rather
than merely unsupported. **Lesser than R2, same class, cheap to fix in the same edit.**

---

## 11. Part B verdict

> ### **STAYS-CERTIFIED\***, bound to
> ### `CIRCDIST.lift` claim hash `sha256:582f9e06b887dd46ae2fa6be73917b853ceefbb13c08b5da699256496b7389d0`

**The deciding conditionality is §10.1: the unrepaired R2 type error in the root's liftability
clause** — a load-bearing clause of the claim text, ruled "a type error, not a stylistic one" by an
independent review on 2026-08-22, AGREED for repair, and silently dropped while its three siblings
from the same decision sheet were executed.

Everything else clears. Explicitly:

* Premises: **nonint PROVED + gap-example PROVED + iff PROVED**, each hash-bound review verified by
  me at source (§9). The §3 premise inventory is satisfied for the first time in this node's history.
* Route implication review: **link valid**, digest reproduced (§9).
* Caveat **S2**: an honest scope note, **does not block** (§9).
* Inherited-defects caveat: **dischargeable**, verified at source (§9).
* Parent–child formula wording: **byte-identical** on the `d_circ` formula, the `d_sec` crossed
  pairing, and the minimum-weight qualifier (§10).

**Therefore 课题二 does not close in this pass.** What remains is a claim-text repair, not
mathematics: no theorem is in doubt, no premise is missing, no computation failed. The route to
PROVED is short and fully specified:

1. Apply **R2** (and, in the same edit, **R1**) to the root claim text; re-hash.
2. One hash-bound independent review of the repaired text (focused — the substance is already
   reviewed; what needs binding is the new wording against `lift.iff`'s Theorem 5.7 / the
   `repair(γ) = 0` criterion).
3. Re-level `routes.criterion-corollary-example` to PROVED on its existing review (§9), or record
   why not.
4. Rewrite or delete the stale inherited-defects caveat.

Surviving caveats at that point: **S2** (conservative scoping); the `repair ≥ 3` /
min-cost-covering / large-proposer-scan exclusions inherited from the children; the `[[4,2,2]]` sole
load-bearing witness for the existential clause under the min-over-sectors convention; the
per-sector scope; and the standing **shared-model-design** limitation (no `stim` cross-check anywhere
in this subtree).

---

## 12. Limitations of this review

1. **Islands I and III were read, not re-computed.** I traced every clause to a numbered result and
   audited hypotheses (§§4.2, 4.4), but I ran no code against the chain-realisability lemma, the
   Corollary I.1′ certifier, or the CMSO₂ sentence. Wave-19's own-code verification of both stands as
   `basis.runs` and I rely on it for those two clauses. **A reader who wants three independent
   code-level passes on all four islands does not have them; II, IV and the bridge have them.**
2. **Instance size.** `n ≤ 28` (bridge sweep capped at `n ≤ 26`); `d_eff` search capped at 4 columns;
   Island IV instances at `n ∈ [8,15]` with `≤ 9` checks so that `∏_c Λ_c` stays exhaustible. No
   campaign-scale instance (gross, rotated surface, BB codes) was measured.
3. **Shared model design.** My simulator reads the same M1–M4 fault menu the dossier does. My circuit
   path and my Definition-1.3 path are genuinely different routes to the same number; my model and
   the dossier's model are not. This is the systemic limitation, and it is not reduced by anything I
   did.
4. **Part B is a records-and-wording adjudication, not a re-derivation.** I did **not** re-derive
   Theorem 5.7, the `(LIFT′)` program, `repair(γ)`, the `[[4,2,2]]` witness, or `nonint`'s Theorem
   7.1. I did not re-verify the wave-29 end-to-end review's four filled holes or its 405-instance
   sweep. I verified levels, hashes, review bindings, the promotion event at source, and the claim
   texts against each other. **The `|U(E)| = 2` fact underlying §10.1 is the wave-13 reviewer's
   computation plus the root assembly's own concession; I did not recompute it.**
5. **Print pagination for `[CE12]` was not obtained** (§7.3) — my ruling makes it unnecessary, but a
   reader who rejects that ruling should treat C1 as still carrying a citation-layer residue.
6. **I promoted nothing.** No node file, scheduler file, generated view or existing artifact was
   modified. This review is one session's act and is itself unreviewed.

---

## 13. Surprises worth the lead's attention

1. **A repair sheet was executed three-quarters of the way.** The wave-13 root review AGREED with
   R1, R2, R3 and R5. R3's and R5's content landed; F1/C-M7/S1 landed (from adjacent sheets); **R1
   and R2 did not**, and no caveat, event or frontier task records their absence. The R2 item is the
   *only* one of the six that would have made the claim text **wider-to-narrower in type** rather
   than in scope — and it is precisely the one that fell through. Mechanically: repairs that trigger
   a re-hash get executed because the re-hash forces a re-bound review; repairs that *also* trigger a
   re-hash but arrive on a "revision sheet for the lead" apparently do not. That is a process gap,
   not a mathematical one, and it is the second time this campaign that a defect survived six review
   layers because no layer owned the *claim wording*.
2. **The child is better-worded than the parent.** `lift.iff`'s claim says "an intrinsic
   zero-voltage/monodromy **condition**" — exactly the correct type — while the root says "**zero**
   voltage/monodromy". The child's own repairs fixed the type; the parent inherited the pre-repair
   phrasing and kept it through three subsequent claim edits.
3. **P2 widens Theorem B rather than merely tidying it.** The wave-21 precision was filed as
   non-blocking hygiene. Measured (732/732), it says the `(≤)` direction needs V1 *only* for qubits
   in no check's support — so the bridge survives a depth bound on every realistic instance. Given
   that 公共定义 admits an optional depth bound `T` (课题三), this is a scope *gain* that has been
   sitting unclaimed in a "non-blocking" footnote.
4. **The bridge's false step is not a corner case at any scale.** 1524 of 1524 on my families, 456 of
   456 on wave-21's, 396 of 396 on Amendment 5's. Three disjoint instance sets, one hundred percent
   each. "Contributes nothing" was doing real work in a sentence nobody checked for three days.
5. **Island IV's YES side is thin by nature.** Uniformly random `Λ` gave 1 YES in 108. Only when I
   drew `Λ_c` from `D_c` did the YES side populate (11 in 114). Any future sweep of this island that
   samples orders uniformly is testing almost nothing, and the 2-SAT reduction's `(⇐)` direction will
   look verified when it has barely been exercised.
