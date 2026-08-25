# Fresh independent Rule-7 review — β1 profile-lattice obstruction identities (C1–C4)

- **Target node:** `KSUM.B4b.L2.ALT.nonproduct.profile-lattice-core`
- **Work product under review:** `ksum/artifacts/ksum_beta1_profile_lattice_ansatz_q5_20260723.md` +
  scripts `ksum_beta1_profile_lattice_ansatz_q5_20260723_{core,k2_germ,k1_trend,k1_qgain,k1_ceiling}.py`,
  logs `ksum/artifacts/logs_ksum_beta1_20260723/`, manifest `…_q5_20260723.sha256`.
- **Reviewer:** fresh Opus 4.8 instance; did NOT author the work; not told the wanted verdict.
- **Date:** 2026-07-23. **Repo:** `<machine-local-path-redacted>`.
- **Reviewer scripts (this review):**
  `ksum/artifacts/ksum_beta1_obstruction_identities_rule7_review_20260723_{core,c1,c2,c3,c4}.py`
  (SHA-256 in §9). No existing file was edited; no git command was run.

## 0. Verdict summary

| Claim | one line | verdict | tier it would survive to |
|---|---|---|---|
| **C1** | `≤2-active-pair` restricted LP value is exactly q-independent (q=5,7,9) | **MINOR** | PROVED scoped (if justification cites kernel-invariance, prose relabelled) |
| **C2** | product-over-pairs witness correlation `= 2^{1-(q-1)/2}` (q=5..13) | **PASS** | PROVED scoped |
| **C3** | q=5 family correlation crosses `2/3` at degree `~√N` ("scalar-Chebyshev cap") | **MINOR** | stays **NUMERICAL** (finite observation, correctly disclaimed) |
| **C4** | PROVED q=5 shared-NO germ is an exactly-feasible point of the ansatz LP | **PASS** | PROVED scoped (leans on frozen germ; transferred facts covered) |

**Overall:** all four scoped claims are substantiated at the exact-rational / NUMERICAL tier they were
filed at; there is **no MAJOR defect and no broken derivation**. My independently-written machinery
reproduced *every* logged rational (not floats) and I extended each identity to a regime the proposer
did not table (C1 to q=11, C2 to q=15,17, C3 to a second family/N, C4 via an independent moment map).
The two MINORs are named-correction issues (imprecise support labels; a heuristic one-line justification;
mild wording overreach on C3's asymptotic status) — none blocks promotion; each is spelled out below.

**SHA-256 manifest:** `sha256sum -c` on `…_q5_20260723.sha256` → **all 11 files OK** (§8).
**Scripts reproduce logs:** `k1_trend.py` and `k2_germ.py` both **reproduce their committed JSON
bit-for-bit** (ignoring timing fields), run under the proposer's own interpreter (Python 3.11.9 +
SymPy 1.13.1); `qceiling9.log` is INTERRUPTED **by design** and no C1–C4 claim leans on it (§8).

---

## 1. Anchoring-ban compliance and the notational-coincidence flag (7c)

I followed the mandated sequence: (1) read `DAG_PROTOCOL.md` and the target node; (2) read
ONLY §0–§2 of the artifact (scope / formulation / ansatz definitions), plus the two **frozen** upstream
nodes it cites (`…two-orientation-shared-no-cascade`, `…M2`) and the frozen tool
`ksum/tools/ksum_l2p27_shared_no_rule7_independent.py`; (3) built my own implementation of every object
(`…_review_20260723_core.py`: group `C(σ)=C₂≀S_P`, falling-factorial moment rows `R_α`, YES/NO
predicate, single-flip atoms, an **exact rational two-phase simplex** with Dantzig entering +
lexicographic ratio test, and an **exact rational RREF/row-space** engine — scipy/sympy are absent
from my env, so I wrote the LP from scratch) and computed my own gate values; (4) only then read the
artifact's result sections §3–§7 and the proposer scripts.

**7c coincidence flag (mandatory).** My independent `R_α = Σ_{g∈C(σ)} Π_a falling((g·n)_a, α_a)` and my
unit-`l1` sign-correlation LP coincide *notationally and semantically* with the proposer's `central_row`
and `max_correlation_lp`. This is **expected** — both are the object *defined* in the frozen tools
`ksum_l2p1_exact_moment_lp.py` / `ksum_l2p27_…` — but I flag it: bare re-computation of an identical
formula corroborates **values**, not the printed **derivation**. I therefore added two derivation-level
checks that do NOT reuse the proposer's route: (a) for C1, an **exact row-space (kernel) identity** over
ℚ that *explains* the q-independence structurally; (b) for C2, an **independent closed-form derivation**
of `2^{1-P}` from first principles. Where a verdict rests only on value-agreement I say so (7f).

---

## 2. C1 — `≤2-active-pair` restricted LP is exactly q-independent

**Claim scope I certify.** For the support of profile *classes* touching **at most 2 non-empty
involution pairs**, the max-sign-correlation LP value (unit-`l1` signed class-measure annihilating every
falling-factorial occupancy moment of total degree `<D`) is **identical as an exact rational** across
`q = 5, 7, 9, 11` at every tested `(N,D)`.

**What I ran.**
`python ksum_beta1_obstruction_identities_rule7_review_20260723_c1.py` (log `logs_review_c1.txt`), plus
an inline check reproducing the proposer's *exact* `two_pair_support` (f=0). Two support definitions
were tested independently of the proposer's, and then the proposer's own support:

- **full `≤2`-active** (all classes, ≤2 non-empty pairs) and **ansatz∩`≤2`** (NO backbones ∪
  single-flip-YES, ≤2 non-empty), f∈{0,1}: `EXACT-EQUAL` for q=5,7,9,**11** at
  `(N,D)∈{(6,4),(8,4),(8,5),(10,5),(12,5)}` — verified by **exact RREF row-space identity + identical
  sgn + identical class columns** (which *forces* an identical feasible polytope and objective, hence an
  exactly equal LP value); LP solved exactly at q=5 gave the common values `27/37, 15180/18169,
  49624/93149, …`.
- **proposer `two_pair_support` (f=0)**: rowspace identical across q=5,7,9,**11**, and my exact q=5 LP
  values **reproduce the committed `k1_trend.json` rationals**: `N=8 → 6/7, 9/16, 18/83`;
  `N=12 D5 → 20/57`; `N=20 D5 → 1296/2375`.

**7b (regime-complete, identity level).** Extended one higher q (**q=11**) not in the proposer's
`{5,7,9}` table, at the **exact-rational** (row-space) level, in three different support definitions.
No infeasible regime; the identity is structural, not a coincidence of small `(N,D)`.

**Why it's q-independent (my structural check, not the proposer's one-liner).** The LP value depends on
`(ker M, sgn, l1-ball)` only. Aligning class-columns across q by *reduced signature* `(f, multiset of
non-empty splits)` — a genuine bijection for all q≥5 — the exact RREF row-space of the moment matrix
`M_q` is **identical** across q=5,7,9,11, and sgn is a function of the reduced signature (identical).
Identical kernel + identical objective + identical `l1` ball ⇒ **exactly equal value**. This is the
rigorous ground for the claim.

**Named MINOR corrections.**
1. **Terminology.** §4B's prose calls the support *"one active pair + one spectator"* and §4D
   *"scalar single-active-pair family"*, but the code (`two_pair_support`) puts **two one-sided pairs**
   `{(a,0),(N−a,0)}` partitioning N (plus single-flips of the active pair), with `f` **fixed to 0**.
   It is a *one-scalar-parameter* family with **two** active pairs, not one; and the `f=0` restriction is
   never stated in prose. The scope is well-defined *by the code*; the textual definition needs the
   relabel + the `f=0` clause.
2. **Justification rigor.** §4B's one-line reason ("empty spectator pairs contribute only the identity
   factor … only fixed positive `|G|`-scaling") is **heuristic, not a proof**: for `α` carrying mass on a
   spectator colour, `R_α` on a ≤2-active class is generally non-zero (the group permutes active mass
   into that slot), so it is not literally an "identity factor." The correct, exact ground is the
   **row-space (kernel) invariance** I verified. Fine at NUMERICAL; for a PROVED promotion the cited
   proof must be the kernel argument, not the one-liner.

**C1 verdict: MINOR** — the mathematical claim (exact q-independence, q=5,7,9,11) is **verified
exactly**; the two corrections are about the support's textual definition and the justification's rigor.

---

## 3. C2 — product-over-pairs correlation is exactly `2^{1-(q-1)/2}`

**Claim scope I certify.** A product-over-pairs witness activating all `P=(q-1)/2` pairs has
`|correlation| = 2^{1-P} = 2^{1-(q-1)/2}` for `q = 5,7,9,11,13` (proposer) — I verified `q = 5,7,9,11,13,15,17`.

**What I ran.** `python …_c2.py` (log `logs_review_c2.txt`). Two independent methods, both exact:
- **direct enumeration** over all `3^P` product states with per-pair factor `φ(axis)=−½` (each of the two
  one-sided states), `φ(interior)=+1`: `|corr| = 1/2, 1/4, 1/8, 1/16, 1/32, 1/64, 1/128` for
  q=5..17 — equal to `2^{1-P}` in every case.
- **independent closed form (my derivation, first principles):** each factor has total 0 ⇒ `ΣW = 0`;
  `NO = all-axis` ⇒ `⟨W,sgn⟩ = −2·∏A_i`; axis-mass `A_i=−1`, `‖φ_i‖₁=2` ⇒ `A_i/‖φ_i‖₁ = −½` ⇒
  `⟨W,sgn⟩ = −2·(−½)^P`, `‖W‖₁ = 2^P` ⇒ `|corr| = 2^{1-P}`.

This matches the proposer's §4C ("`‖·‖₁ = 2^P`, correlation numerator `= 2`") exactly, and M2's PROVED
`2^{1-(q-1)/2}`. **7f:** the value AND the closed-form derivation are established independently. (Note:
the *signed* correlation alternates `−½,+¼,−⅛,…`; the reported quantity is its magnitude — a benign
orientation convention.)

**C2 verdict: PASS** — exact for q=5..17 by two independent methods; promotable to a PROVED scoped
statement.

---

## 4. C3 — q=5 crossing of `2/3` near degree `√N` ("scalar-Chebyshev cap")

**What the object actually is.** The §4D "scalar single-active-pair family" is, in code, the same
`two_pair_support` (f=0, ≤2 one-sided pairs; one scalar parameter `a`). Its LP optimum vs `D` is a
scalar moment / Chebyshev-type extremal problem — hence the "Chebyshev" language.

**What I ran / verified.**
- **Independent crossing** (my own `≤1`-active "SAP" family, `python …_c3.py 9 12 16 20 25`, exact
  rational, log `logs_review_c3.txt`): correlation brackets `2/3` from both sides at **N=9,12,16,20,25**;
  `D_crit` (largest D with corr`>2/3`) = `4,4,4,4,6`, i.e. it **grows with N ~ √N**. (7b: both sides of
  the crossing at multiple N.)
- **Exact reproduction of the proposer's headline numbers** on their *own* `two_pair_support` at N=64:
  `D=6 → 6413/8205 = 0.7816` (`>2/3`), `D=7 → 1011585775200/1622679667997 = 0.6234` (`<2/3`) —
  i.e. §4D's "0.782 / 0.623", to the exact rational.

**Tier finding (the question C3 asks).** This is a **finite NUMERICAL observation**, **not** an analytic
cap theorem. There is **no proof** of a `Θ(√N)` cap in the artifact, and the finite ratio `D_crit/√N`
computed from the committed log **wobbles** — `1.00, 0.82, 0.83, 0.87, 0.75` for N=16,24,36,48,64 — it
does not converge, so "a **clean** `Θ(√N)` threshold" and the noun "**cap**" (which connotes a proven
upper bound) mildly **oversell** what is shown. Crucially the artifact itself files this under
**"G11: no asymptotic claim"** and "finite falsification diagnostic," so the **tier is honestly stated**;
the overreach is only in two adjectives and the "single-active-pair" misnomer (§2 correction 1).

**C3 verdict: MINOR** — the crossing and the exact N=64 values are confirmed; the claim sits at
**NUMERICAL / finite-observation**, which the artifact correctly disclaims (G11); named corrections:
"clean Θ(√N)"/"cap" wording and the "single-active-pair" label. It should **not** be promoted above
NUMERICAL (and the artifact does not try to).

---

## 5. C4 — the PROVED germ is an exactly-feasible point of the ansatz LP

**Claim scope I certify.** The frozen, PROVED q=5 shared-NO germ (bridge `¾` + shared-NO `¼`,
node `…two-orientation-shared-no-cascade`) is, expressed on the profile lattice, a point with
(a) **support ⊆ ansatz support**, (b) **moment residual exactly 0** under the reviewer's own `R_α` for
all total(α)`<D`, (c) **`l1 = 1`**, (d) **correlation `> 2/3`**, on the germ schedule
`D=⌊√(N/512)⌋+2`, for `N = 513, 2049, 4609, 8193, 20003, 32769`.

**What I ran.** `python …_c4.py` (log `logs_review_c4.txt`). I rebuilt the germ measure from its frozen
barycentric coefficient formulas, mapped each germ histogram to my class signature, and then used **my
own** `group_perms/falling/orbit/moment_value` (not the germ tool's `central_row`) to test feasibility:

| N | D | atoms | all in ansatz support | my moment residual | l1 | correlation |
|---|---|---|---|---|---|---|
| 513 | 3 | 8 | yes | **0** | 1 | `8/11 = 0.72727` |
| 2049 | 4 | 10 | yes | **0** | 1 | `4608/6401 = 0.71989` |
| 4609 | 5 | 14 | yes | **0** | 1 | `442368/617837 = 0.71599` |
| 8193 | 6 | 16 | yes | **0** | 1 | `44040192/61723301 = 0.71351` |
| 20003 | 8 | 22 | yes | **0** | 1 | `241089399226368/339359454714409 = 0.71042` |
| 32769 | 10 | 28 | yes | **0** | 1 | `…/… = 0.70852` |

These exact rationals match the committed `k2_germ.json` **exactly**, and the node's C4 wording
"**8/11 … 0.7104**" is precisely this correlation **range** across N=513→20003 (my `0.71042` at N=20003 =
the node's `0.7104`; the germ's own `0.711752` is a different, off-schedule `(20003,7)` datapoint — no
contradiction). Every germ atom is a **NO backbone** `(0,0,s,0,N−s)` or a **single-flip minimal-YES**
`(0,1,s−1,0,N−s)` (minority exactly 1) — structurally inside the ansatz support.

**Cross-implementation identity (independent).** My `R_α` equals the germ tool's `central_row` on every
sampled `(class, α)` (e.g. `s=7,α=(0,2,0,1,0) → 1803890` both; `α=0 → 8` both) — confirming my moment
machinery against the frozen tool, and that "moment residual 0" is a *convention-independent* fact.

**7d (no frozen-input immunity) — explicitly checked.** The germ's archived Rule-7 review verified
residual-0 / l1 / correlation in **the same `R_α`/sgn/l1 language** the ansatz LP uses; those facts
therefore transfer to "feasible point of the ansatz LP" unchanged. The only **new** content is
**support-containment** (that `yes_hist/no_hist` are ansatz atoms) and the **moment-map identity**
(ansatz `R_α` = germ `central_row`) — I **re-opened and independently verified both**, so the new use is
covered. C4 is a corollary of the germ's PROVED properties + these two checks; it does not silently
inherit anything uncovered.

**C4 verdict: PASS** — germ feasibility inside the ansatz LP is exact and independently reproduced;
promotable to a PROVED scoped ("germ ∈ feasible set of the β1 ansatz LP") statement.

---

## 6. Rule-7 checklist — each item addressed

- **7a Type audit.** Objects and dimensions as functions of `(N,q,D,#active pairs)`:
  profile `∈{n∈ℕ^q:Σn=N}`, `dim=\binom{N+q-1}{q-1}`; group `|C(σ)|=2^P·P!`, `P=(q-1)/2`; class = `C(σ)`-orbit;
  moment row `R_α:classes→ℤ`, one per `C(σ)`-orbit of `α` with `total(α)<D` (row *count* grows with q but
  the row *space* on ≤2-active support is q-invariant — the content of C1); witness `w:classes→ℚ`,
  `w=p−n`, `2·#classes` LP vars; correlation `∈ℚ`. Every constituent map is well typed: `g·n` is a
  genuine `C(σ)`-relabelling (colour perm fixing 0); `falling(0,0)=1`, `falling(n,k)=0` for `n<k`, so
  empty colours contribute identity and kill dominated `α`; sgn, `C_t` are `C(σ)`-invariant. The
  artifact's §2 type table is correct. The two moment-map implementations (mine and the germ tool's)
  agree at the integer level (§5). **No type mismatch found.**
- **7b Regime-complete identity gates.** C1: exact-rational **row-space** identity at q=5,7,9,**11** in
  three support definitions. C2: exact `2^{1-P}` at q=5,7,9,11,13,**15,17** + independent closed form.
  C3: crossing bracketed at **N=9,12,16,20,25** (independent family) and the N=64 headline reproduced
  exactly. C4: exact moment residual **0** in exact arithmetic at 6 schedule points to N=32769. No
  in-scope regime left untested; nothing capped by an infeasible regime.
- **7c Anchoring ban.** Followed (see §1); the notational coincidence with the proposer's core is flagged
  and offset by an independent kernel argument (C1) and an independent closed form (C2).
- **7d No frozen-input immunity.** The germ dependency is re-opened for its **new** uses
  (support-containment, moment-map identity) and both verified independently (§5). The germ's own PROVED
  facts are reused only in the same `R_α`/sgn/l1 language its review already covered.
- **7e Standing failure-mode list.** *Dropped/extra normalization*: `l1=1` and net-mass-0 re-checked
  exactly (C4); the `|G|`-stabilizer factor is a per-column scaling that cancels in the `=0` moment
  constraints (checked — this is *why* C1's kernel is q-independent). *Type/dimension mismatch*: none
  (7a). *Undefined terms / missing stability ranges*: "active pair", "single-flip", "profile support",
  "NO backbone", "super-threshold" all resolve to code definitions; the **imprecise ones are named**
  ("single-active-pair" is a 2-pair support; `f=0` unstated) (§2, §4). *Colored-orbit vs full central
  sum*: the moment rows ARE full central sums over `C(σ)` (verified: `R_α`=`central_row`), not colour-orbit
  partials. *Numerics validating a broken derivation*: the only broken-derivation risk is C1's §4B
  one-liner — named, and the correct kernel proof supplied (§2).
- **7f Value-vs-formula decoupling.** C1: value by both my LP and my kernel identity; the **q-independence
  structure** is established by the kernel identity (independent of the proposer's route). C2: value by
  enumeration AND an independent closed form. C3: value reproduced (my family + proposer support); **no**
  cap *theorem* is claimed or established — value only. C4: residual/l1/corr by my own `R_α` (independent
  construction) — corroborates the germ's PROVED facts and, via the cross-impl identity, the printed
  moment-map.
- **7g Quantifier hygiene.** Every reviewed term resolves to a definition in the artifact or the cited
  frozen tools. Two resolvable-but-**misleading** labels flagged: "scalar single-active-pair" (→ 2-pair,
  scalar, f=0) and "clean Θ(√N) cap" (→ finite, wobbling ratio, no theorem). No *unresolvable* term.

---

## 7. What would move any verdict

- C1 → PASS/PROVED: relabel the support (2 one-sided pairs, `f=0`) and cite the **row-space-invariance**
  proof (which I verified identity-level) instead of the "identity-factor" one-liner.
- C3 stays NUMERICAL by construction; to become a theorem it needs an actual Chebyshev/`√N` *proof*, not
  a finite table — the artifact does not claim one (G11), which is the honest posture.
- A MAJOR/GAP would have required a non-zero moment residual, a q-*dependent* row space on ≤2-active
  support, a product correlation `≠2^{1-P}`, or a germ atom outside the ansatz support — **none occurred**.

---

## 8. SHA-256 manifest and script→log reproduction

- `sha256sum -c ksum/artifacts/ksum_beta1_profile_lattice_ansatz_q5_20260723.sha256` → **11/11 OK**
  (`…md, _core.py, _k2_germ.py, _k1_trend.py, _k1_qgain.py, _k1_ceiling.py`, and the five logs).
  Note: `logs_ksum_beta1_20260723/k1_trend_run.log` exists on disk but is **not** in the manifest — it is
  a byte-identical duplicate of `k1_trend.json`; harmless, worth pruning.
- **Reproduction** (proposer interpreter `…/WindowsApps/python.exe`, Python 3.11.9 + SymPy 1.13.1):
  - `k1_trend.py --output …` → **committed `k1_trend.json` == reproduced** (ignoring `sec` timing) —
    covers §4A/B/C/D, i.e. C1/C2/C3.
  - `k2_germ.py --output …` → **committed `k2_germ.json` == reproduced** — covers C4.
  - `k1_qgain.py`/`k1_ceiling.py`: `qceiling9.log` is **INTERRUPTED by design** at `(N=10,D=5,q=9)`; no
    C1–C4 claim depends on it. My own full-support LP independently reproduced the §4E/qgain ceiling
    rationals it does contain (e.g. `15180/18169`, `49624/93149`, `310099/481653`, `260414592/421698403`).

## 9. Reviewer script SHA-256 (this review)

```
7f615b0feeff5fe56fec165ea3972d0e910f031436f46456594000c8e517f4be  ..._review_20260723_c1.py
707c751e170c04a31d4a7316af34f5f7cf04acb642a2e35161fc2c11ac50a6fb  ..._review_20260723_c2.py
fd07c4e3ad0c4a5ea3a2e261c37ac3d8cb14639d4b977751af3158174d8ed4e2  ..._review_20260723_c3.py
aac0358e09a1afa1c2e3031f120b09d8e9c588c21ad2f72f44a9b0f356c66948  ..._review_20260723_c4.py
90f907b590ae206ed0d4b2a1fd79f6bc8554c8c35ced1d454a4f50af0e7cfeaa  ..._review_20260723_core.py
```
Logs: `ksum/artifacts/logs_review_c1.txt`, `logs_review_c2.txt`, `logs_review_c3.txt`, `logs_review_c4.txt`;
reproductions in `ksum/artifacts/rev_repro_out/`.

**Commands (from `ksum/artifacts/`):**
```
sha256sum -c ksum_beta1_profile_lattice_ansatz_q5_20260723.sha256
python ksum_beta1_obstruction_identities_rule7_review_20260723_c1.py
python ksum_beta1_obstruction_identities_rule7_review_20260723_c2.py
python ksum_beta1_obstruction_identities_rule7_review_20260723_c3.py 9 12 16 20 25
python ksum_beta1_obstruction_identities_rule7_review_20260723_c4.py
"…/WindowsApps/python.exe" ksum_beta1_profile_lattice_ansatz_q5_20260723_k1_trend.py --output rev_repro_out/k1_trend.json
"…/WindowsApps/python.exe" ksum_beta1_profile_lattice_ansatz_q5_20260723_k2_germ.py  --output rev_repro_out/k2_germ.json
```

---

*This review meets Rule-7 (7a–7g). It licenses, at the reviewers-completed level required by the
completion gate: **C2, C4 → PROVED-scoped** eligibility; **C1 → PROVED-scoped** eligibility conditional
on the two named corrections (relabel + kernel-invariance justification); **C3 → NUMERICAL** (no higher
tier is warranted, and the artifact does not claim one). No completion status is written by this review.*
