# Independent adversarial review — `CIRCDIST.sat.instances` (wave 25)

**Reviewer:** fresh Opus 5 session, independent adversarial role. **Date:** 2026-08-23.
**Target:** `artifacts/circdist_sat_instances_20260823.md`
(`sha256:8984df0c51311f4ad80dd12fff58ac46829d5e4bd05b160122538ae9d415c3aa` — **verified**, matches
the dispatch).
**Node:** `research/circdist/proof-dag/nodes/CIRCDIST.sat.instances.yaml`
(`sha256:1d51b9363255b6f2be7b61f31b75a68b407baf2cddf8359badef717dd28eef15`).
**Bound claim hash:** `sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3`.

---

## 0. Independence statement

I authored no circdist artifact. I was instructed to **refute**, and I went after the headline
first. Concretely:

* I read, as **data**, only: the target `.md`; `CIRCDIST.sat.instances.yaml`;
  `CIRCDIST.sat.window.yaml`; `research/circdist/notes/CIRCDIST_PROBLEMS.md`;
  `research/circdist/notes/SAT_RESCOPE_20260822.md`; and **§2 only** (Definitions 2.1–2.11) of
  `artifacts/circdist_sat_transfer_proof_20260823.md`, to obtain the exact statements of legality,
  (MC), the detector set, the fault model and `d_R`.
* I read **no file** in `artifacts/logs_circdist_sat_instances_20260823/`. In particular I read
  none of `sat_core.py`, `transfer.c`, `stimx.py`, `milp.py`, `brute.py`, `bb.py`. Their integrity
  was checked (`shasum -a 256 -c SHA256SUMS.txt`: **247/247 OK**, 248 entries in the directory
  including the checksum file) but their contents were never opened.
* Every number below comes from code I wrote this session **from the definitions**, in
  `artifacts/logs_circdist_sat_instances_review_20260823/`.
* No canonical file was modified. `git status` shows only the two new review objects.

**Hash pipeline validated before use.** My `claim_hash` implementation (normalise CRLF, strip,
SHA-256 of the UTF-8 `claim` field) reproduces **4/4** existing `reviewed_hash` values in the
repository — `CIRCDIST.sat.window` `8698b051…`, `CIRCDIST.cplx.islands` `2e786e96…`,
`CIRCDIST.gross.dext-cap` `4bc0b5eb…`, `CIRCDIST.lift.nonint` `e2d1b292…`.

---

## 1. Materials and methods

Four independent instruments, none of them the proposer's:

| # | method | what it is | independence |
|---|---|---|---|
| **E** | exhaustive meet-in-the-middle over **distinct effect classes** | for target weight `w`, split `w = ⌊w/2⌋ + ⌈w/2⌉` and match XOR-complements; a minimum-weight configuration uses pairwise **distinct** signatures (two equal ones cancel), so this is exhaustive | no solver, no stim, no transfer representation |
| **I** | exact binary ILP (scipy 1.13.1 / HiGHS) on **my own** spacetime matrix, parity slacks, `mip_rel_gap = 0`; and a cap variant `Σx ≤ c` deciding `d_R > c` by infeasibility | independent search over the same matrix |
| **S** | **stim 1.16.0** `search_for_undetectable_logical_errors` on a circuit emitted from **my** `Schedule` and **my** reading of Definition 2.7 | different codebase entirely: stim's own propagation, DEM and search |
| **A** | **forward round-by-round replay** of raw fault locations (`audit_witness`), a code path fully separate from the backward signature engine | audits every witness independently of how it was found |

The signature engine is an exact `F2` **backward** recursion (`sig_before(X_c) = sig_after(X_c) ⊕
sig_after(X_t)`, `sig_before(Z_t) = sig_after(Z_t) ⊕ sig_after(Z_c)`, ancilla frames zeroed at
measurement), i.e. a different algorithm from anything the artifact describes.

I found and fixed **one bug in my own harness** mid-review (my first stim emitter omitted the
`D_{a,r}` detectors); it is recorded here because it changed my intermediate numbers, and all
figures below are post-fix.

**Model-equality, re-derived independently.** I compared the set of `(detector-set,
observable-set)` signatures of stim's DEM with the column set of my spacetime matrix, in a common
key space: **equal in 20/20 cases** (`d = 5` class D `R = 1..4`; `d = 7` class D `R = 1..6`;
`d = 9` class D `R = 1`, `R = 2` Z), **zero one-sided differences**. The artifact's central
licensing check therefore replicates.

---

## 2. Priority 1 — the headline `R_stab > 1` family

### 2.1 (a) Are the schedules legal and (MC)? — **YES**

I rebuilt the rotated surface code from the printed spec (data at `(r,c)`; centres `(i+½,j+½)`,
X-type iff `i+j` even; weight-2 X on top/bottom, weight-2 Z on left/right; `X_L` = column 0,
`Z_L` = row 0) and rebuilt legality (Def 2.4) and (MC) (Def 2.5) from their statements.

```
d=3  n=9   |A|=|B|=4   rank H_X=rank H_Z=4   k=1   H_X H_Z^T=0   d_X=d_Z=3  (exhaustive)
d=5  n=25  |A|=|B|=12  rank H_X=rank H_Z=12  k=1   H_X H_Z^T=0   d_X=d_Z=5  (exhaustive over 2^13)
d=7  n=49  |A|=|B|=24  rank H_X=rank H_Z=24  k=1   H_X H_Z^T=0

576 candidates -> 96 legal -> 16 legal AND (MC)      identical at d = 3, 5, 7
```

All three counts reproduce. The 16 survivors fall into **4 classes of 4** and my class assignment
matches the artifact's Table 4.2 **member index for member index**: A = {1,5,10,14},
B = {0,4,11,15}, C = {3,7,8,12}, D = {2,6,9,13}.

The two named schedules:

* **standard** `piX = NW,NE,SW,SE`, `piZ = NW,SW,NE,SE` — legal ✔, (MC) ✔, all 8 (resp. 18) bulk
  X-hooks **horizontal** (⊥ the vertical `X_L`), all bulk Z-hooks **vertical** (⊥ `Z_L`): the
  hook-optimal choice, as claimed.
* **class D** `piX = NW,SW,NE,SE`, `piZ = NW,NE,SW,SE` — legal ✔, (MC) ✔, all bulk X-hooks
  **vertical** (∥ `X_L`), all bulk Z-hooks **horizontal** (∥ `Z_L`): doubly misaligned, as claimed.

Layer occupancies of class D at `d = 5` are `[20,20,20,20]` — no globally idle layer, so (C2) is
satisfied without any reduction step, as stated.

**Attack (a) fails.** The schedules are exactly what the artifact says they are.

### 2.2 (b) Is `d_1` overcounted at `d = 5`? — **NO**

My own exhaustive search over **77** distinct nonzero effect classes at `d = 5`, class D, `R = 1`
finds **no** undetectable logical of weight `≤ 3` in either sector, and a weight-4 one exists.
Independently: ILP `= 4`; stim `= 4`.

```
        d = 5 class D, R = 1 :   d_1^Z = 4 ,  d_1^X = 4        E = I = S = 4
```

I could not reproduce the artifact's "**78** distinct one-round effect classes" (see §5, Defect 1);
my count and stim's DEM both give **77**, and the artifact's own §2 table also says 77. This is an
off-by-one in a bookkeeping figure, and it is in the **safe** direction (a 78-item enumeration is a
superset of the 77 real classes), so the exclusion it supports stands — and I re-establish it
independently.

**Attack (b) fails.**

### 2.3 (c) Are the `R ≥ 2` minima undercounted? — **NO**

Exact minima by **three** independent methods, both sectors, every witness audited by forward
replay (`distinct locations = weight`, all `D_{b,r}` and `D_{a,r}` silent, observable flipped):

| `d` | schedule | sector | `R=1` | 2 | 3 | 4 | 5 | 6 | 7 | my `d_∞` | my `R_stab` | methods |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | class D | Z / X | 2/2 | 2/2 | 2/2 | 2/2 | 2/2 | | | 2 | **1** | E |
| 5 | class D | Z / X | **4/4** | **3/3** | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 3 | **2** | E, I, S(`R≤4`) |
| 7 | class D | Z / X | 6/6 | 5/5 | 4/4 | 4/4 | 4/4 | 4/4 | | 4 | **3** | S (+ model-equality) |
| 9 | class D | Z / X | 8/8 | | | | | | | — | — | S |

Every value matches the artifact's Table 4.3. **The `R_stab = 2` cell is real**: at `d = 5`,
class D, `d_1 = 4 > d_2 = 3 = d_3 = ⋯ = d_7`, in **both** sectors, hence also under
min-over-sectors.

The artifact's **printed** headline witness (§4.4) — `('cnot',1,(27,5),'c')` in round 0,
`('cnot',1,(33,21),'c')` and `('cnot',0,(11,44),'ct')` in round 1 — was transcribed by hand from
the `.md` and fed to **my** circuit. All three gates exist in my independently built schedule at
the stated layers, and my forward replay returns: 3 distinct locations, **every** detector silent,
observable flipped. **The printed witness is genuine.**

**Attack (c) fails.**

### 2.4 (d) Could a convention slip manufacture the effect? — **NO**

Three hostile probes:

1. **Add the omitted `D_{a,0}`** (treating the round-0 X record as absolute — it is not, which is
   why Def 2.7 drops it). Adding detectors can only raise `d_R`; if it lifted `d_2` to 4 the effect
   would vanish. Result: `d_R` **unchanged** at `4, 3, 3` for `R = 1,2,3`.
2. **Drop `D_{b,0}`** (unknown-initialisation reading) or **drop `D_{b,R}`** (no terminal closure).
   Either collapses `d_R` to **1** — for *every* schedule. So the two temporal-boundary
   conventions are massively load-bearing in absolute terms. But they act through **identical
   code** on the standard and the class-D schedule, which differ only in `piX`/`piZ`; and under the
   convention as written the standard schedule gives `(5,1)` while class D gives `(3,2)`. A
   convention slip cannot produce a *difference between two schedules*, which is exactly what
   `R_stab > 1` consists of.
3. **Aggregation.** `(C1)`'s load-bearing witness is that the sectors genuinely separate. I checked
   member **[0]** (class B) at `d = 5` independently: `d_R^Z = 5` and `d_R^X = 3` for `R = 1..5`.
   Confirmed — the per-sector reading really would give a different answer, the artifact states
   min-over-sectors per table, and prints both sectors. `(C2)` idle compression is vacuous here as
   claimed.

**Attack (d) fails.**

### 2.5 (e) Does the `R_stab = (d−1)/2` law overfit? — the artifact's own label is correct

Fitted law `d_R = max(d − R, (d+1)/2)`, `R_stab = (d−1)/2`. Against **my** cells:

| `d` | my computed `d_R` | `max(d−R,(d+1)/2)` | agree? |
|---|---|---|---|
| 3 | 2,2,2,2,2 | 2,2,2,2,2 | ✔ |
| 5 | 4,3,3,3,3,3,3 | 4,3,3,3,3,3,3 | ✔ |
| 7 | 6,5,4,4,4,4 | 6,5,4,4,4,4 | ✔ |
| 9 | 8 (`R=1` only) | 8 | ✔ |

**What the cells support:** `R_stab = 1, 2, 3` at `d = 3, 5, 7` are established (by me, exactly).
`R_stab > 1` exists, so single-round dominance is **refuted by construction** — that conclusion is
not a fit, it is a witness, and it needs only the `d = 5` column.

**What they do not support:** (i) `R_stab = 4` at `d = 9` — I confirmed only `d_1 = 8`; my `d = 9`
`R = 2` run did not finish inside the box, so in *my* review that cell rests on the proposer's MILP
alone. (ii) The law at any `d ≥ 11`. (iii) "`R_stab` unbounded", which is a consequence of the
conjecture, not of any cell. The artifact labels (i)–(iii) **CONJECTURED** and says "four
`d`-values are a pattern, not a proof". That labelling is accurate and I have no objection to it.

**Verdict, priority 1: CONFIRM.**

---

## 3. Priority 2 — the qLDPC arm

Rebuilt from the printed algebra (`l = m = 3`, `A = 1 + y + x`, `B = 1 + y + x²y`,
`H_X = [A|B]`, `H_Z = [Bᵀ|Aᵀ]`):

```
n = 18   9 X-checks, 9 Z-checks   rank H_X = rank H_Z = 7   (DEPENDENT)   k = 4
check weights: all 6      qubit degree: 3 in H_X, 3 in H_Z      H_X H_Z^T = 0
d_X = d_Z = 4  exhaustive over both 2^11 kernels        ->   [[18,4,4]]
Standing fact 2.2, exhaustive over all 2^11 of ker H_Z :  0 mismatches
schedule NI: T = 12, legal, (MC) holds, 108 CNOTs, 9 per layer, no idle layer
```

Every parameter reproduces, including the rank-7 dependency and `k = 4`.

**`(d_∞, R_stab) = (3, 1)`, re-verified.** Exhaustive search (method E, no solver): `d_R = 3` for
`R = 1..6` in **both** sectors — the minimum found is 3, so no weight-1 or weight-2 undetectable
logical exists at any of those `R`. `d_∞ = 3 < d = 4`, as claimed.

The artifact's printed `R = 1` witness (§5.3) — `('cnot',3,(21,12),'c')`, `('cnot',0,(18,0),'c')`,
`('cnot',3,(20,11),'t')` — exists in my schedule, replays silent and logical at weight 3, and
reproduces the printed observable pattern `(0,1,1,0)` exactly on my independently chosen logical
representatives.

**Depth-6 (MC)-emptiness by-product, re-run exhaustively:**

```
518 400 candidates  ->  25 920 legal  ->  0 legal AND (MC)     (17 s, my own scan)
```

I also **re-derived the legal count in closed form**, which the artifact does not: at each slot the
X-side and Z-side monomials must touch different blocks, so the set `S` of slots carrying the
`A`-monomials is also the set carrying the `Aᵀ`-monomials, giving
`C(6,3)·(3!)⁴ = 20·1296 = 25 920`. Exact agreement.

**Extra probe the artifact does not run.** Because `H_X` is dependent, Definition 2.7 **omits** the
round-0 redundancy parities `⊕_{a∈T} m_{a,0}` for `T ∈ leftker(H_X)` (dimension 2 here) — the very
hole clause S3′ flags. I added them and recomputed: `d_R = 3` for `R = 1..4`, **unchanged**. The
qLDPC answer is robust to the one convention question that actually bites for dependent checks.

**Verdict, priority 2: CONFIRM.**

---

## 4. Priority 3 — surface grid and mechanism attribution

**Standard schedule, my own methods.**

| `d` | sector | result | how |
|---|---|---|---|
| 3 | Z, X | `d_R > 2` for `R = 1..5`, hence `= 3` | E (exhaustive) |
| 5 | Z | `d_R = 5` for `R = 1..6` | E (no weight `≤4`, `R=1,2`, solver-free) + ILP cap-4 **infeasible** + audited weight-5 witness |
| 5 | X | `d_R = 5` for `R = 1..3` | same |

The weight-5 witness is **constructed, not imported**: the minimum-weight element of
`ker H_Z ∖ rowsp H_X` placed as single-qubit faults after the last layer of the last round; my
replay confirms it is silent and logical at every `R` tested. So `d_R ≤ 5` is exhibited rather than
taken from the window theorem. `(d_∞, R_stab) = (5,1)` at `d = 5` — **confirmed**.
`d = 7` standard I did **not** reproduce (it is the most expensive cell and the artifact says so);
my `d = 5` `R = 7` Z-sector cap-ILP also hit my 300 s limit. Both are recorded as *not
independently checked*, not as disputed.

**Mechanism attribution, reproduced exhaustively without a solver** (`d = 5`, class D, Z-sector):

| `R` | `d_R` | single-round | no-hook | min without any measurement fault | artifact's label |
|---|---|---|---|---|---|
| 1 | 4 | 4 | **5** | 4 | single-round **hook** ✔ |
| 2 | 3 | **4** | **5** | 3 | mixed multi-round, hook-driven, measurement-free ✔ |
| 3 | 3 | **4** | **5** | 3 | same ✔ |

This reproduces the artifact's Table 6.2 rows exactly, and reproduces two exclusion claims by an
independent route: *every* minimum witness at `R ≥ 2` spans `≥ 2` rounds (single-round `4 > 3`),
and *every* minimum witness uses a hook fault (no-hook `5 > d_R`) at every `R`. My complementary
statistic (min weight using **no** measurement fault `= d_R`) gives the same conclusion as the
artifact's `need-meas > d_R`: no minimum witness needs a measurement fault. Three printed/exported
witnesses audited in total (§2.3, §3, and the class-B separation witness).

**Verdict, priority 3: CONFIRM.**

---

## 5. Priority 4 — honesty audit, and the defects I did find

**Honesty: good.** §7 N6 names the truncated cells; every absence claim I checked carries its
scope; the aggregation convention is stated and both sectors are printed in every table; the
window-theorem import is fenced (W) and used only to extend tails that were *already observed
constant* inside the computed window; the transfer method's conditionality is fenced (T) and no
reported number depends on it; the general pattern is labelled CONJECTURED. `d_R` is
non-increasing in **every** sequence I computed — corroboration of the window node's monotonicity,
not proof of it. All computed cells satisfy `R_stab ≤ d_∞ ≤ d`.

**Defect 1 (minor, real).** §3 and §4.4 say "**78** distinct one-round effect classes",
`C(78,3) = 76 076`, `C(78,4) = 1 426 425`. The true number at `d = 5`, `R = 1` is **77** — by my
count and by stim's DEM, for the standard *and* the class-D schedule — and **the artifact's own
§2 table says 77**. The document is internally inconsistent. The error is in the safe direction
(a 78-item enumeration is a superset), the exclusion it supports is independently re-established
here, and no reported `d_R` moves. **Fix: change 78 → 77 and recompute the two binomials.**

**Defect 2 (documentation, not computation).** §2's "classes" column (`23/39/55`, `77/133/189`,
`163/283`, `108/198/288`) sits under a sentence describing the set of DEM signatures, but those
figures are **not** the number of distinct DEM signatures at `R ≥ 2` (which is `415`, `821`, `953`,
`990`, `1737`, …). I reconciled it: they are exactly the **sector-reduced** counts, obtained by
deleting the `D_{a,r}` detector coordinates. I reproduce all of them **exactly** — `23/39/55`,
`77/133/189`, `163/283` — so the numbers are right and only the label is under-specified.
Importantly, the *substantive* model-equality claim is true as stated: I verified it on the full
signature sets in 20/20 cases with zero one-sided differences. **Fix: one clause saying the count
is over the sector-reduced model.**

**Defect 3 (bookkeeping).** The artifact's §0 hash chain records the target node at
`1e1521a6…`; the node is now `1d51b936…` (it was updated by the `three-arms-delivered-2026-08-23`
event after the artifact was finalised). Expected, but the chain no longer resolves as written.

I found **no** defect that moves any reported `(d_∞, R_stab)`.

---

## 6. Verdicts

| arm | verdict |
|---|---|
| **1b — headline `R_stab > 1` family** (priority 1) | **CONFIRM.** `d = 5` class D: `d_R = 4,3,3,3,3,3,3` for `R = 1..7`, both sectors, three independent methods, witness audited by a fourth path; `R_stab = 2`, `d_∞ = 3`. `d = 7`: `6,5,4,4,4,4`, `R_stab = 3`. `d = 9`: `d_1 = 8` only. Legality and (MC) rebuilt and confirmed. Single-round dominance is refuted by construction. |
| **1a — standard surface grid** (priority 3) | **CONFIRM at `d = 3, 5`** (`(d,1)`, exhaustive + ILP + constructed witness). `d = 7` **NOT INDEPENDENTLY CHECKED** (cost); not disputed. |
| **2 — qLDPC BB `[[18,4,4]]`** (priority 2) | **CONFIRM.** Code parameters, rank-7 dependency, `k = 4`, `d_X = d_Z = 4` all reproduced exhaustively; `(d_∞, R_stab) = (3,1)` for `R = 1..6` both sectors; depth-6 by-product `518400 → 25920 → 0` reproduced exhaustively **and** re-derived in closed form; robust to the omitted redundancy detectors. |
| **3 — mechanism attribution** (priority 3) | **CONFIRM** on the cells I re-ran. Two printed witnesses audited genuine; two exclusion claims reproduced by an independent exhaustive route. Not all 11 rows of Table 6.2 were re-run. |
| **4 — honesty / scope discipline** (priority 4) | **CONFIRM with three minor defects** (§5), none load-bearing. |
| **overall** | **CONFIRM.** The headline survives a hostile pass. |

---

## 7. What this review licenses under `research/DAG_PROTOCOL.md` §3

For `CIRCDIST.sat.instances`, bound to claim hash
`sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3`:

**Licensed: `NUMERICAL` → `CERTIFIED*`** — "an independently reviewed conditional result with
explicit unresolved premises or scope caveats". The rule-6 cap that held the node at `NUMERICAL`
(review pending) is discharged: an independent adversarial review has now reproduced the three arms
with instruments that share no code with the proposer.

**`PROVED` is NOT licensed**, and I would refuse it: this is an outcome node whose content is
computation, 公共定义 states that numerical simulation never substitutes for proof, and every
statement outside the computed window imports the CONJECTURED window theorem.

**Caveat set to attach:**

1. **(W)** Every `d_R` statement beyond the computed window imports `CIRCDIST.sat.window`
   (CONJECTURED/`CERTIFIED*` with its own W-G2 conditionality). Inside the computed window nothing
   is imported — I re-exhibited `d_R ≤ d` by explicit construction rather than by import.
2. **(N2)** Scope is the uniform `S₄ × S₄` family (576 → 96 → 16). No statement of the form "no
   legal schedule does X" is licensed; the positive existence statement is.
3. **`d = 9` `R_stab = 4` is NOT independently reviewed.** I confirmed `d_1 = 8` only. Carry it at
   proposer level.
4. **`d = 7` standard `(7,1)` is NOT independently reviewed.** Carry at proposer level.
5. **The fitted law and "`R_stab` unbounded" remain CONJECTURED** — correctly so in the artifact.
6. **Defects 1–3 of §5** should be corrected in the artifact; none changes a reported value.
7. **Aggregation is min-over-sectors** and is decisive (class-B witness independently confirmed:
   `d_R^Z = 5`, `d_R^X = 3` at `d = 5`). Inherited as W-G1, not settled here.
8. Attribution is confirmed on the cells re-run, not on all 11 rows of Table 6.2.

**Consequence for `CIRCDIST.sat.window`'s `W-OPEN`.** `W-OPEN` ("is there any in-scope schedule
with `R_stab ≥ 2`?") is **answered positively at reviewed level**, no longer only at proposer
level. The former absence-type discount and the sampling-rarity caveat are superseded by a
construction I independently rebuilt. The window theorem is **not** threatened: every cell I
computed satisfies `R_stab ≤ d_∞ ≤ d` (`1≤2≤3`, `2≤3≤5`, `3≤4≤7`), and `d_{R+1} ≤ d_R` held
without exception. `W-G4` ("is `R_stab ≤ d_∞` tight?") gains data but is not closed: the observed
ratio is `R_stab/d_∞ = (d−1)/(d+1) → 1`, so the bound is asymptotically tight *if* the conjectured
law holds — which is exactly the CONJECTURED part.

I license; the dispatcher executes. No proof-DAG object was touched by this session.

---

## 8. Limitations of this review

* One budget-boxed session, no sub-agents. `d = 7` standard, `d = 9` beyond `R = 1`, and `d = 5`
  standard `R = 7` (Z) were not completed by me; `d = 5` standard X-sector was checked to `R = 3`.
* Methods **E** and **I** consume the same spacetime matrix (built by me); they are independent
  *searches*, not independent *models*. Genuine model independence comes from **S** (stim) and from
  the 20/20 model-equality check, and from **A** (forward replay).
* My distinct-effect-class reduction is justified by a cancellation argument I give in §1; it is
  the same reduction the artifact uses, so it is not an independent check *of that reduction*.
* I did not re-run all 16 legal+(MC) members at `d = 3,5` individually; I checked the class
  structure and the four named representatives plus member [0].
* Table 6.2 was reproduced for `d = 5` class D `R = 1,2,3` (Z) only.

## 9. Logs

`artifacts/logs_circdist_sat_instances_review_20260823/` with `SHA256SUMS.txt`:
`rev_core.py`, `rev_stim.py`, `rev_cap.py`, `rev_bb.py`, `rev_step1_code_and_space.py`,
`rev_step2_d5.py`, `rev_step4_witness_and_attrib.py`, `rev_step5_conventions_attrib.py`;
logs `rev_step1.log`, `rev_step2_d5_classD_R12.log`, `rev_step2_d5_classD_R37.log`,
`rev_step2_d5_standard_exh.log`, `rev_cap_d5_standard.log`, `rev_stim_d5_classD.log`,
`rev_stim_d7_classD.log`, `rev_stim_d7_classD_R456.log`, `rev_stim_d9_classD.log`,
`rev_bb_dist.log`, `rev_bb_depth6_scan.log`, `rev_step4_A_printed_witnesses.log`,
`rev_step4_B_aggregation.log`, `rev_step4_D_altconvention.log`, `rev_step5_probe1.log`,
`rev_step5_probe2.log`, `rev_step5_probe3.log`, `rev_step6_classcount_reconcile.log`,
`rev_step6_d3.log`, and `rev_process_ledger.txt`.

**FIX-2 run termination.** Five background processes were declared and are listed with their
commands and log files in `rev_process_ledger.txt`, together with `ps` output **before** and
**after** termination. Three exited on their own; two (`rev_cap.py` d=5 standard, `rev_stim.py`
d=9) were killed by me before this document was written. `ps` after the kill shows **0 remaining**.
Logs that end mid-run (`rev_cap_d5_standard.log` at `R = 3` X, `rev_stim_d9_classD.log` at `R = 2`
Z) end because I terminated them; the last complete line of each is the last cell claimed above,
and §6/§7 name those cells as not independently reviewed.
