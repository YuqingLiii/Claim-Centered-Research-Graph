# WHGAP R15 — independent §7.10 review of LEAN-5 WP-H (the complex-Hermitian entropy glue)

Reviewer report, 2026-08-01/02. Commission:
[`WHGAP_COMMISSION_LEAN5_P15B_20260801.md`](../channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_LEAN5_P15B_20260801.md),
section **R15**. NODE_ID = `WHGAP.goal`. ROLE = reviewer.

## Verdict

**(B) FINDINGS — 1 MAJOR + 6 minors. No soundness defect: everything the batch proves
checks out, by three independent routes, and the machine gates all reproduce.** The MAJOR
is a residual-display accuracy defect (an *under*-claim left in a Lean source scope block),
which is exactly what menu item (A) — "the residual display is accurate" — asserts and what
commission item 4 makes reportable in both directions. With MAJOR-1 corrected, statement
(A) holds in full.

**Independence statement (DAG rule 6, rule 7c).** I am a fresh instance. I did not author
the LEAN-5 WP-H work, any part of the WHGAP Lean development, or any prior WHGAP review.
I was given no desired outcome: the commission states LICENSE and FINDINGS are equally
acceptable. My own-route verification (§2) was completed **before** I opened the executor's
report `artifacts/whgap_lean5_20260801.md`, and I did **not** read
`tools/whgap_lean5_wph_check.py` at any point.

---

## 0. PRE-ACTION REPORT (mandatory pre-task reload, executed from disk)

Read in the mandated order, complete, from disk: `research/PRETASK_RELOAD_PROMPT.md`;
`research/DAG_PROTOCOL.md` (whole file, §§1–7 incl. the eight hard rules and §7.10);
`research/RESEARCH_STRUCTURE_PROTOCOL.md`;
`channel-capacity/werner-holevo-gap/README.md`;
`channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md`;
`channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md`; the target node
`proof-dag/nodes/WHGAP.goal.md`; and its status-propagating children
(`WHGAP.qpositive-onset`, `WHGAP.zero-capacity-application`, `WHGAP.onset-two-fifths`) plus
the node whose module the batch edits (`WHGAP.no-ascent-hierarchy`) via `NODE_INDEX.md`.

* **Target node and status as read from disk:** `WHGAP.goal` — **OPEN**
  (`proof-dag/nodes/WHGAP.goal.md:7`, `status_source: problem-scaffold-2026-07-28`; the
  composition block's `rel` displays the reason: child P13 `WHGAP.onset-two-fifths` is
  CONJECTURED). `NODE_INDEX.md:113` agrees (`GOAL | proof | OPEN |
  composition-checked rel {P13, hS}`).
* **Role:** reviewer, fresh instance. **Independence:** I did not author the reviewed work
  and was told no desired outcome (see the verdict block above).
* **Highest status my planned evidence could license (§2 ladder):** a completed, archived,
  cited independent review of a proof node opens the **completion tier** — CERTIFIED\* /
  PROVED / REFUTED — but **only the decision layer / an independent checker may write it on
  the node**, and only for the scope my review actually covers. My own runs are themselves
  NUMERICAL evidence. I write **no** status field: R15 scope is a report only.
  Concretely, what this review can license is the promotion of the LEAN-5 build evidence out
  of `pending-review:`, at the scope stated in §9 — *not* any mathematical status of
  `WHGAP.goal`, `WHGAP.no-ascent-hierarchy` or the capacity claims, which the Lean layer
  cannot reach (a green build is a run, DAG §2 and structure protocol §4 item 7).
* **Gates and deliverables of my commission, one line each:**
  1. own-route verification, anchoring ban: rebuild both §6 outputs from the Kraus set
     transcribed by me, check `S(B) − S(E) = IcScalar` at ≥ 3 rational points, ≥ 40 digits,
     without reading the executor's check script;
  2. definition audit: `vnEntropyC` is the standard von Neumann entropy (nats) of the
     Hermitian eigenvalue enumeration; the multiset strip uses `ofReal` injectivity and
     assumes no ordering; the list-form lemma is non-vacuous and its length hypothesis is
     genuinely derived;
  3. statement fidelity: `exists_eps_entropy_pos` quantifier-congruent to
     `exists_eps_IcScalar_pos`; audit the executor's EQUIVALENCE account of `hach`/`hach'`
     and the wording that reports it; check for a §7.10.5 satisfiability instance;
  4. Trust/README wording: residual (b) "DISCHARGED" must carry the explicit named
     remainder; over-claim and under-claim both reportable;
  5. standard §7.10: uninterrupted clean rebuild, `#print axioms` on every new declaration,
     forbidden scan, freeze-check 8/8 unchanged, `lean_dag_check` 0 FAIL;
  6. rule-7 embedded set, visibly executed: type audit, c ≥ 2 identity gates (charpoly route
     AND direct eigendecomposition route), anchoring ban, frozen-input scopes, standing
     failure-mode list, value-vs-formula statements.
  Deliverables: this report, `tools/whgap_r15_*.py`, `r15_`-prefixed logs added to
  `artifacts/logs_whgap_lean5_20260801/`, a separate `SHA256SUMS_r15.txt`. Budget ≤ 60 min.
* **Conflicts between my commission text and the disk protocols:** **one, reported not
  silently resolved.** Commission item 3 asks me to check that `hach'` "is genuinely WEAKER
  than `hach` (or exactly the reduction claimed)". On disk it is **equivalent**, not weaker;
  the executor reported this as deviation D2 and proved the equivalence. The commission's
  own framing was therefore stronger than the mathematics, and the disk wins. My audit of
  that account is §4. (No conflict with `DAG_PROTOCOL.md` or the structure protocol was
  found; the commission's single-writer restriction on `proof-dag/nodes/` is stricter than,
  and compatible with, the atomic-update rule — the decision layer owns the node record and
  discharges rule 8c by linking this report.)

---

## 1. What I reproduced, and what I did not

| item | reproduced by me | evidence |
|---|---|---|
| clean rebuild, **uninterrupted single transcript** | yes — deleted only `.lake/build/lib/lean/WHGAP*` (Mathlib cache never touched), `lake build` in background | `r15_rebuild.txt`: `Build completed successfully (3203 jobs)`, **EXIT=0**, **20 `Built` lines, 0 `Replayed` lines** — the "stronger evidence" the executor's §8 said was the reviewer's to produce |
| `#print axioms` on every declaration | yes — my own `lake env lean WHGAP/Trust.lean` | `r15_print_axioms.txt`: **245** `depends on axioms` lines, **0** outside `[propext, Classical.choice, Quot.sound]` or a subset; all **13** new WP-H declarations individually listed and clean |
| declaration count 232 → 245 (+13) | yes | 10 in `Support/EntropyC.lean` + 3 in `no-ascent-hierarchy.lean`, enumerated in `r15_print_axioms.txt` |
| forbidden-construct scan | yes, 13 patterns | `r15_gates.txt` GATE A: **0 code occurrences** of `sorry` / `native_decide` / `implemented_by` / `axiom` / `admit` / `unsafe` / `partial def` / `@[extern]` / `nolint` / `maxHeartbeats 0`; every hit is docstring prose. The only `decide` in the tree is kernel `decide` at `Channel.lean:601-602` (pre-existing LEAN-4, commission-allowed); `EntropyC.lean` adds none |
| freeze-check 8/8, hashes UNCHANGED | yes | `r15_gates.txt` GATE B, exit 0; `WHGAP.no-ascent-hierarchy` still `542edac6…` — the module the batch edits did **not** touch its `## Frozen Claim` |
| `lean_dag_check --problem werner-holevo-gap` | yes | `r15_gates.txt` GATE C: **0 FAIL**, 2 WARN, 1 INFO — exactly the two documented scoped-input exceptions (P4/P6) and the goal's AND-style composition; unchanged |
| `proof_dag_check` / `literature_check` | yes | `r15_gates.txt` GATE E: both **exit 0** (16 nodes; 52 papers, 5 libraries) |
| the mathematics of the central identity | yes, by **three** independent routes | §2 below |
| satisfiability of the new bridge (§7.10.5) | yes, **out-of-tree, by me** (the tree has none) | `r15_satisfiability.txt`, `lake env lean` **EXIT=0** — see minor m3 |

**Not reproduced / out of scope:** the capacity content. Nothing in this development is a
channel, and no capacity statement is reached; per §7.9 a theorem proved against an abstract
interface is exactly as strong as the results that interface cites, and not one notch
stronger. I did not re-review the LEAN-2/3/4 layers except where WP-H load-bears on them
(§6, frozen-input scopes).

---

## 2. Own-route verification (commission item 1; rule 7c anchoring ban)

**Anchoring discipline actually followed.** I transcribed the Kraus set, the witness state
and the `IcScalar` formula myself, from the frozen Lean sources (`Support/Channel.lean:126–136`,
`:152`, `:156`, `:193`, `:205`, `:477–514`; `Support/IcScalar.lean:172–201`), with the exact
line cites recorded in the script header. I did **not** open
`tools/whgap_lean5_wph_check.py`, and I wrote and ran both of my scripts before reading
`artifacts/whgap_lean5_20260801.md`.

**Coincidence flag (7c requires it).** My transcription of the Kraus matrices necessarily
coincides notationally with the executor's, because both are transcriptions of the same
frozen `Channel.lean` displays — there is no independence to be had at the transcription
layer, and I flag that rather than present it as agreement. The independence is in the
**route**: the executor's GH1 uses `mp.eighe` on the Kraus-built matrices; my routes are
(i) an exact symbolic sympy computation, (ii) a Faddeev–LeVerrier characteristic polynomial
plus `mp.polyroots`, and only (iii) `mp.eighe` as a cross-check.

**Script:** `tools/whgap_r15_own_route.py`. **Log:** `r15_own_route.txt` (mp.dps = 60).

| gate | what it checks | result |
|---|---|---|
| R15-1a | symbolic: `Σ_a K_a ρ_ε K_aᵀ` on the chart `s²=x/2, t²=1−x, st=β` **equals** the `LamWit_eq` display, as a matrix identity in `(x, ε, β)` | **PASS**, residual identically `0` |
| R15-1b | symbolic: `Tr(K_a ρ_ε K_bᵀ)` **equals** the `LamCWit_eq` display | **PASS**, residual identically `0` |
| R15-1c | `Σ_a K_aᵀ K_a = 1` on the chart (trace preservation) | **PASS** |
| R15-1d | `Tr ρ_ε = 1` | **PASS** |
| R15-2 | `S(B) − S(E) = IcScalar x ε` at **8** rational points, **two spectral routes each** | **PASS at all 8**, worst residual over everything **1.09 × 10⁻⁵⁵** (tolerance 10⁻⁴⁰) |
| R15-3 | Hermiticity ≤ 10⁻⁴⁰, trace = 1, PSD, eigenvalue multiset = `specB`/`specE` | **PASS at all 8** |

Points, chosen by me and covering every qualitatively distinct regime (7b):

| point | regime | min spectral gap (7 eigenvalues) | `S(B)−S(E)` |
|---|---|---|---|
| `x=1/3, ε=1/5` | B-side eigenvalue coincidence `ε(1−x/2) = x/2` | `0` | `+0.03485…` |
| `x=2/7, ε=3/11` | generic, all 7 distinct | `4.18e-3` | `+0.09377…` |
| `x=7/25, ε=2/17` | generic, all 7 distinct | `1.65e-2` | — |
| `x=13/29, ε=5/23` | generic, all 7 distinct | `6.75e-3` | — |
| `x=9/20, ε=1/7` | **in the open strip; `IcScalar < 0`** — negative control | `2.25e-2` | `−0.04922…` |
| `x=7/20, ε=1/2` | **exactly degenerate** (B-side double root, E-side double root) | `1.1e-60` | `+0.02422…` |
| `x=7/20, ε=1/2−10⁻⁶` | near-degenerate | `9.6e-13` | `+0.02422…` |
| `x=1/100, ε=1/1000` | small `x`, small `ε` (the witness regime) | `5.0e-6` | `+0.00759…` |

*Numerical-hygiene note, recorded rather than smoothed:* at the exactly degenerate point,
root-finding on a repeated root loses ≈ half the working precision (route agreement
`2.4e-31` at 60 dps — textbook behaviour, not a defect). The **entropy identity is a
symmetric function of the roots and is unaffected**: residual `0.0` there. My script
therefore relaxes the *eigenvalue-level* tolerance to 10⁻²⁵ exactly at degenerate spectra,
prints the relaxation, and keeps the identity tolerance at 10⁻⁴⁰.

**The negative control matters:** at `x = 9/20, ε = 1/7` the identity holds to 2.3 × 10⁻⁶¹
while `IcScalar` is **negative**. The identity is not an artefact of the positivity regime.

---

## 3. Definition audit (commission item 2)

**`vnEntropyC` is the standard von Neumann entropy (nats).**
`EntropyC.lean:63` — `vnEntropyC {A : Matrix n n ℂ} (hA : A.IsHermitian) : ℝ :=
∑ i, Real.negMulLog (hA.eigenvalues i)`. `Matrix.IsHermitian.eigenvalues` is Mathlib's
`RCLike`-generic **real-valued** enumeration, and `Real.negMulLog z = −z log z` with the
`0 ↦ 0` convention, so this is `S(A) = −Σ λ log λ` in nats, over the full eigenvalue
enumeration with multiplicity. It is definitionally the same shape as the real
`Support.vnEntropy`. **No positivity, normalization or state structure is assumed** — the
module header, `Trust.lean` and README item 6 all say so explicitly, which is the honest
handling: for a non-state the number has no information-theoretic reading. **PASS.**

**The multiset strip uses `ofReal` injectivity and assumes NO ordering.**
`EntropyC.lean:80–88`: `h1` rewrites `roots_charpoly_eq_eigenvalues` into
`A.charpoly.roots = (map ofReal) (map eigenvalues univ.val)`, and the conclusion is obtained
by `Multiset.map_injective Complex.ofReal_injective (h1.symm.trans h)`. This is the only
place an ordering assumption could have hidden, and it does not: `Multiset.map_injective`
is injectivity of `Multiset.map f` for injective `f`, a statement about multisets with no
enumeration, no sort, no `List` structure. Nothing downstream separates or names individual
eigenvalues; `eigenvaluesC_multiset_eq` (`:99`) says exactly
`Multiset.map hA.eigenvalues univ.val = Multiset.map d univ.val`. **PASS** — and my gate
R15-2 at the exactly degenerate point `ε = 1/2` is the empirical counterpart: the identity
survives a repeated eigenvalue with no side condition. **PASS.**

**The list-form lemma, and the DERIVED length hypothesis (executor deviation D1).**
`vnEntropyC_eq_sum_of_charpoly_list` (`:122`) takes `l : List ℝ` with
`A.charpoly = ((l.map fun a : ℝ => X − C (a:ℂ)).prod)` and concludes
`vnEntropyC hA = (l.map Real.negMulLog).sum` — no length hypothesis. I audited the
derivation in `charpolyC_list_length` (`:139–146`): it coerces the list hypothesis to the
multiset form (`Multiset.map_coe`, `Multiset.prod_coe`), applies
`eigenvaluesC_multiset_eq_multiset`, and takes `congrArg Multiset.card`; since
`Multiset.card (Multiset.map f univ.val) = Fintype.card n` and
`Multiset.card (l : Multiset ℝ) = l.length`, the length is **forced**, not assumed. The
derivation is **not circular** (the executor asked me to check this specifically): it
consumes only the charpoly hypothesis and the already-proved multiset bridge, and nothing
in the multiset bridge consumes a length fact. **Delivering the lemma without the
hypothesis is strictly stronger than commissioned. PASS** — D1 confirmed as a
strengthening.

**Non-vacuity — with a labelling correction (minor m4).** The theorem is a *necessary
condition* (it excludes mismatched lists); it does not by itself establish that any list
satisfies the hypothesis. Actual satisfiability is witnessed in-tree by the payoff itself:
`IcScalar_eq_vnEntropyC_diff` applies the lemma to `specB` (3 reals, `Matrix (Fin 3) (Fin 3) ℂ`)
and `specE` (4 reals, `Matrix (Fin 4) (Fin 4) ℂ`), so the hypothesis is inhabited at both
arities. The lemma is therefore non-vacuous **and** the length claim is sound; only the
docstring headline word overreaches (m4).

---

## 4. Statement fidelity (commission item 3)

### 4a. `exists_eps_entropy_pos` vs `Support.exists_eps_IcScalar_pos` — quantifier congruence

Frozen (`Support/IcScalar.lean:487`):
`theorem exists_eps_IcScalar_pos (x : ℝ) (hx0 : 0 < x) (hx25 : x < 2 / 5) :
  ∃ ε : ℝ, 0 < ε ∧ ε < 1 ∧ 0 < IcScalar x ε`

New (`no-ascent-hierarchy.lean:273`):
`theorem exists_eps_entropy_pos (x : ℝ) (hx0 : 0 < x) (hx25 : x < 2 / 5) :
  ∃ ε : ℝ, 0 < ε ∧ ε < 1 ∧ 0 < vnEntropyC (Channel.LamWit_isHermitian x ε)
      − vnEntropyC (Channel.LamCWit_isHermitian x ε (Real.sqrt (x * (1 − x) / 2)))`

Binder-by-binder: `x` explicit in both; both hypotheses present, same statements, same names,
same order; identical existential with the identical three-conjunct body and the identical
first two conjuncts; **only the quantity after the third `0 <` differs.** No bound is
weakened, no quantifier dropped, no uniformity lost, no implication reversed. **PASS.**

### 4b. The `hach` / `hach'` relation — is the executor's EQUIVALENCE account correct?

**Yes, and I verified it in Lean by my own route rather than taking the claim.**
`entropy_witness_eq_IcScalar` (`:255`) proves, for `0 < x < 2/5` and **every** `ε`, that the
entropy difference at `β = √(x(1−x)/2)` equals `IcScalar x ε`. Both `hach` and `hach'`
carry the *same* guard hypotheses `0 < x`, `x < 2/5` in their implication chains, so on the
guarded region the two bodies are literally equal, and off it both implications are
vacuously true. Hence `hach ↔ hach'` as Props — not one-way weakening.

I did not accept this by reading. I wrote and compiled, out of tree,
`R15_hach_iff_hach' : (hach) ↔ (hach')` for an **arbitrary** `CapacityInterface I`,
proving **both** directions from `entropy_witness_eq_IcScalar` alone
(`r15_satisfiability.txt`, `lake env lean` EXIT=0, standard axioms). **PASS — the
commission's "genuinely WEAKER" framing is wrong and the executor's correction is right.**

**Is the claimed gain ("the charpoly→entropy identification leaves the trust boundary")
mathematically correct?** Yes, with the right reading, and the sources state exactly that
reading. Logical strength is unchanged; what changes is *what the hypothesis has to be
believed about*. Before WP-H, reading `Claim_of_witness` as a statement about the channel
required three things outside Lean: (i) `LamCK` is the complement, (ii) LSD/Devetak, and
(iii) that the number `IcScalar x ε` — a `negMulLog` sum over two hand-written **lists** — is
the entropy difference of the actual outputs. `hach'` is stated over the entropies of the
**matrices** `Lam x (rhoWit ε)` and `LamC x β (rhoWit ε)`, so (iii) is no longer something a
reader must grant: it is `IcScalar_eq_vnEntropyC_diff`, whose inputs are
`specB_charpoly_list` / `specE_charpoly_list`, themselves statements about `Lam`/`LamC` (and
`specB_charpoly_kraus`/`specE_charpoly_kraus` about `LamK`/`LamCK`). The remainder is
exactly (i) + (ii), both interface-tier. **The account is correct.**

**Do Trust / README / docstring match it?** Checked all three, word by word:
`Trust.lean:113–129` (explicit over-claim guard: "not logically weaker"; under-claim guard;
named remainder (i)+(ii)); README item 10 as amended (`"hach' is equivalent to the older
hach, not weaker"` + the same (i)/(ii)); `no-ascent-hierarchy.lean:285–298` (the same three
bullets); and the `hach` census row at `Trust.lean:25` marked **REDUCED, not discharged**,
with the row retained — correct append-only census discipline. **All three agree with each
other and with the mathematics. PASS.**

### 4c. Satisfiability instance for the new bridge (§7.10.5) — MISSING in tree

`WHGAP/Model.lean` carries `R12_hach` / `R12_P9_via_witness` for the `IcScalar` form (§3b,
added after R12 m3 flagged the identical omission for the LEAN-2 bridges) but has **no**
instance for `hach'`. The executor flagged this himself (report §7.4) rather than hiding
it. I supplied the missing certificate out of tree (`r15_satisfiability.txt`, EXIT=0):
`R15_hach'` inhabits `hach'` in the same model `R11I`; `R15_P9_via_entropy` derives the P9
`Claim` through the **new** route; and two `example`s show the model's `IcLB` is not the
trivial predicate (it fails at `c = 0` and at `x = 1/2`), so the certificate is not
discharged by a degenerate interface. **`Claim_of_entropy_witness` is therefore NOT
vacuous.** Recorded as **minor m3** (fold in, per the R11 m14 / R12 m3 precedent), not a
MAJOR: the executor disclosed it, and the vacuity question is now answered on disk.

---

## 5. Trust / README wording — residual (b) "DISCHARGED" (commission item 4)

**Where the wording is right (and it is unusually good).** `Trust.lean:97–132` states the
discharge with a table of the four Lean theorems that carry it, an **over-claim guard**
("`hach'` is not logically weaker"), an **under-claim guard** ("the passage really is in
Lean now, at full identity granularity and for the Kraus-built outputs"), and **the explicit
named remainder**: "(i) that `LamCK` is *the* complementary channel of `Lam` (a
Stinespring/dilation statement …) and (ii) LSD/Devetak achievability", both cited to
`Interface.lean`. README item 10 carries the same amendment with the previous text quoted
verbatim before it (append-only), and the "What a green build does NOT establish" list keeps
`vnEntropyC` inside item 6's no-positivity/no-normalization clause.
`Support/Entropy.lean`'s appended note is exactly right: the "Complex-Hermitian generality
is NOT claimed" sentence **stays** as the record of what *that* module claims. **PASS on
Trust.lean, README.md and Entropy.lean.**

**Where it is wrong — MAJOR-1, see §7.** The batch updated `Trust.lean`, `README.md` and
`Entropy.lean`, but **not** `Support/Channel.lean`, whose own scope block still tells the
reader that the glue does not exist.

---

## 6. Rule-7 embedded set, visibly executed

**(7a) Type audit — per display, dimensions as functions of all parameters.**

| display | domain → codomain | check |
|---|---|---|
| `vnEntropyC hA` | `{A : Matrix n n ℂ} (hA : A.IsHermitian) → ℝ`, `n` any `Fintype`+`DecidableEq` | `hA.eigenvalues : n → ℝ` (real-valued even over `ℂ`); `Real.negMulLog : ℝ → ℝ`; `∑` over `Finset.univ : Finset n`. Well typed; arity independent of the matrix entries' field |
| `charpolyC_roots_of_prod` | `Multiset ℝ → (roots : Multiset ℂ) = (map ofReal : Multiset ℂ)` | LHS and RHS both `Multiset ℂ`; `roots_multiset_prod_X_sub_C` needs a domain — `ℂ` is one |
| the strip step | `Multiset.map_injective (Complex.ofReal_injective : Function.Injective (↑· : ℝ → ℂ))` | consumes `Multiset ℂ = Multiset ℂ`, produces `Multiset ℝ = Multiset ℝ`. Injectivity is of `ofReal`, **not** of `eigenvalues` — no distinctness is smuggled in |
| list ↔ multiset | `(l : Multiset ℝ)` via `Multiset.map_coe` / `Multiset.prod_coe`; `card (l : Multiset ℝ) = l.length` | the coercion is the canonical `List → Multiset`; no reordering is possible because `Multiset` quotients by permutation |
| **the payoff, B side** | `Lam (x:ℂ) (rhoWit (ε:ℂ)) : Matrix (Fin 3) (Fin 3) ℂ`; `specB x ε : List ℝ`, **length 3 = Fintype.card (Fin 3)** | matches `LamWit_isHermitian x ε` (`x ε : ℝ`) exactly |
| **the payoff, E side** | `LamC (x:ℂ) (β:ℂ) (rhoWit (ε:ℂ)) : Matrix (Fin 4) (Fin 4) ℂ`; `specE x ε : List ℝ`, **length 4 = Fintype.card (Fin 4)** | matches `LamCWit_isHermitian x ε β` (`x ε β : ℝ`) exactly |
| **the coercion the executor asked me to check (report §7.5)** | WP-G list theorems use `fun z : ℝ => X − C ((z : ℂ))`; the new lemma's hypothesis is `fun a : ℝ => X − C ((a : ℂ))` | **the same** `Complex.ofReal` coercion, α-equivalent lambdas — no mismatch. Confirmed independently by the kernel: the payoff closes by direct application, which would fail on any coercion mismatch |
| `β` in `entropy_witness_eq_IcScalar` | `β := Real.sqrt (x*(1−x)/2) : ℝ`; `hβ` by `Real.sq_sqrt` needing `0 ≤ x(1−x)/2` | on `0 < x < 2/5` we have `x > 0` and `1 − x > 3/5 > 0`, so the argument is **strictly positive**; discharged by `nlinarith`. Correct |
| hypothesis narrowing | `IcScalar_eq_vnEntropyC_diff` needs `0 ≤ x ≤ 1`; the node lemma supplies it from `0 < x < 2/5` by `linarith` | sound, and strictly inside the domain |

No display in scope has a dimension or coercion mismatch. **PASS.**

**(7b) Regime-complete identity gates, c ≥ 2, at IDENTITY level.** The commission asked for
two routes on the central identity; I ran **three**, all at matrix/polynomial-identity level,
not aggregate level:

1. **Charpoly route, symbolic** (`tools/whgap_r15_charpoly_route.py`, log
   `r15_charpoly_route.txt`): from the Kraus set I computed `det(Z·1 − B)` and
   `det(Z·1 − E)` symbolically in `(x, ε, β)` and matched them against the two WP-G
   products — `R15-4a` residual identically `0` for the B side, `R15-4b` residual
   identically `0` for the E side after substituting `β² = x(1−x)/2`. This independently
   re-derives `specB_charpoly_list` / `specE_charpoly_list`, the two load-bearing inputs of
   the payoff.
2. **Direct eigendecomposition route, numeric** (`mp.eighe`, 60 dps) — §2, all 8 points.
3. **Faddeev–LeVerrier charpoly + `polyroots` route, numeric** — §2, all 8 points; the two
   numeric routes agree to `≤ 8.1e-60` at every non-degenerate point.

Regime coverage: generic (3 points, all 7 eigenvalues pairwise distinct), eigenvalue
coincidence on the B side, **exactly degenerate**, near-degenerate (`9.6e-13`),
small-`x`/small-`ε`, in-strip with **negative** `IcScalar`, and the domain endpoints `x = 0`
and `x = 1` in the charpoly route. **No regime of the claim is untested.**

**Load-bearing-hypothesis gates (a defect class this project has hit before — decorative
hypotheses).** I checked that the payoff's hypotheses are not decoration:
* `R15-4b'`: dropping `hβ : β² = x(1−x)/2` makes the E-side charpoly identity **false** —
  the residual is exactly `(2β² + x² − x)/8 · (2ε−1)² · (2Z − εx)(2Z + εx − x)`, nonzero
  off the hypothesis. `hβ` is load-bearing.
* `R15-4e`: `discE ≥ 0` holds on `x ∈ [0,1] × ε ∈ ℝ` (dense scan, min `1.56e-4` on the grid;
  and the SOS identity `discE = (1−3x/2)² + 2x(1−x)(1−2ε)²`, gate `R15-4d`, residual `0`,
  explains why), while **off** `[0,1]` there are 15 witnesses with `discE < 0` where
  `quad_eq_lamP_lamM` genuinely fails (`Real.sqrt` of a negative is `0` in Lean, so
  `lamP·lamM ≠ det`, gap up to `23.4`). The `0 ≤ x ≤ 1` hypothesis is load-bearing.

**(7c) Anchoring ban.** §2: own transcription from the frozen sources with line cites, own
scripts, executor's check script never opened, executor's report read only afterwards, and
the transcription-level coincidence explicitly flagged. **PASS.**

**(7d) Frozen-input scopes.** The payoff load-bears on exactly two frozen inputs:
`Channel.specB_charpoly_list` and `Channel.specE_charpoly_list` (LEAN-4 WP-G). Their
archived review is R14, whose scope covers precisely this use — "both WP-G charpolys
re-derived symbolically with `hβ` shown load-bearing" — i.e. identity level, over `ℂ`, with
the same hypothesis set. That is the same granularity and the same regime WP-H consumes, so
no uncovered aspect is inherited. **I nevertheless did not invoke frozen-input immunity:** I
re-derived both charpolys myself (gates R15-4a/4b) from the Kraus set. `Support/Entropy.lean`
is imported but not logically consumed by `EntropyC` — it is load-bearing only transitively,
for `Mathlib.Analysis.Matrix.Spectrum` (`Channel.lean` imports only
`Mathlib.LinearAlgebra.Matrix.Hermitian`), so the import is real, not dead.

**(7e) Standing failure-mode list, each addressed.**
* *Dropped/extra normalization factors:* both outputs verified trace-one at all 8 points;
  `negMulLog` is in **nats** on both sides of the identity (no `log 2` mismatch between
  `vnEntropyC` and `IcScalar` — they use the identical Mathlib function).
* *Type/dimension mismatches:* the per-display table above, including the arity match
  between the two spec lists and the two matrix dimensions.
* *Undefined terms of art / missing stability ranges:* (7g) below; the one range that matters
  is shown load-bearing above.
* *Partial sums silently substituted for full sums:* the analogue here would be summing over
  distinct or sorted eigenvalues instead of the full multiset. Explicitly excluded: the
  bridge is at multiset level, and the degenerate point `ε = 1/2` is an empirical check
  that multiplicity is carried.
* *Numerics validating values while the printed derivation is broken:* mitigated by making
  route 1 **symbolic on the identities the Lean proof actually consumes**, and by the kernel
  (clean rebuild + `#print axioms`). The Lean derivation itself is three lines and I read
  it: two applications of `vnEntropyC_eq_sum_of_charpoly_list` plus `IcScalar`'s definition;
  nothing is re-derived and no hypothesis is added beyond the ones `specE_charpoly_list`
  already carried.

**(7f) Value-vs-formula statement — explicit.** My gates R15-2/R15-3 compare the closed-form
`IcScalar` **formula** (transcribed from `IcScalar.lean`) against an **independent
construction** (matrices multiplied out from the Kraus set; eigenvalues from two solvers
that never see `specB`/`specE`). They therefore **corroborate the identity**
`IcScalar = S(B) − S(E)`; they do **not** verify any printed derivation. What verifies the
derivation is (a) gate R15-4a/4b, which is symbolic and checks the exact polynomial
identities the Lean proof consumes, and (b) the Lean kernel via my clean rebuild. Both are
stated here so the two kinds of evidence are not conflated.

**(7g) Quantifier hygiene — every term of art resolves.** `vnEntropyC` →
`EntropyC.lean:63`. `IcScalar` → `IcScalar.lean:200` (over `specB`/`specE`, `:192`/`:195`,
over `lamP`/`lamM`, `:185`/`:188`, over `discE`, `:172`). "the Kraus-built §6 witness
outputs" → `Channel.Lam`/`Channel.LamC` at `Channel.rhoWit`, tied to `LamK`/`LamCK` by
`LamK_eq`/`LamCK_eq`. "achievability reading" → `Interface.lean`'s `q_pos_of_ic_pos` and
`lsd_devetak`. "**the** complementary channel" → deliberately **not** resolved in this
development, and the sources say so in those words rather than leaving it undefined — which
is the correct handling of an unresolvable term of art. **PASS.**

---

## 7. Findings

### MAJOR-1 — `Support/Channel.lean`'s own scope block still says the WP-H layer does not exist, and states three things that are now FALSE

`Channel.lean:96–107`, scope item 4, is unchanged by this batch and currently reads:

> **What is still missing — residual (b) of `WHGAP/Trust.lean` is REDUCED, not removed.**
> … **"same characteristic polynomial ⟹ same von Neumann entropy" is NOT available for
> complex Hermitian matrices in this development.** … Until that layer exists, the passage
> from these two charpolys to `IcScalar x ε = S(Λ(ρ_ε)) − S(Λ^c(ρ_ε))` — and hence the
> reading of `IcScalar` as a coherent information — is not in Lean. That passage, plus the
> achievability reading `hach`, is what residual (b) still carries.

Three assertions there are contradicted by the tree as it now stands:

1. "residual (b) … is REDUCED, not removed" — `Trust.lean:97` declares it **DISCHARGED**;
2. "'same characteristic polynomial ⟹ same von Neumann entropy' is NOT available for complex
   Hermitian matrices in this development" — that is verbatim
   `Support.vnEntropyC_congr_charpoly` (`EntropyC.lean:151`), which exists and is on the
   standard axioms;
3. "Until that layer exists, the passage … is not in Lean" — that passage is
   `Support.IcScalar_eq_vnEntropyC_diff` (`EntropyC.lean:178`).

**Why this is a MAJOR and not a minor.** (i) Commission item 4 makes *under*-claim
reportable on the same footing as over-claim, and menu (A) asserts "the residual display is
accurate" — one of the four places that display the residual is now inaccurate. (ii) It is
the same file, the same scope block and the same defect class that **R13 MAJOR-1** already
struck once ("Channel.lean's own scope block referenced PHANTOM declarations … presenting
the honestly-degraded residual (b) as closed"), with the direction reversed. A source file
whose in-code scope block contradicts `Trust.lean` is precisely the drift this project has
paid for twice. (iii) `Trust.lean:99` opens the LEAN-5 section with "The glue named in *the
paragraph immediately above*" — the batch knew `Channel.lean` names the glue and updated the
Trust copy only.

**Not a soundness defect.** Nothing that is proved is affected; the Lean content is correct
and the axioms are clean. **Fix (source-side, cheap):** append a dated LEAN-5 amendment to
`Channel.lean` item 4 — append-only, quoting the superseded text, in the same style the same
item already uses for its R13 history note — pointing at `Support/EntropyC.lean` and
`IcScalar_eq_vnEntropyC_diff`. Attribution is shared: the commission's step list (steps 5–7)
named `Trust.lean`, `Entropy.lean` and the README but not `Channel.lean`, and the executor
followed it literally.

### Minors

* **m1 — stale sentence inside the section that declares (b) discharged.**
  `Trust.lean:167`: "The same qualification applies to `Claim_of_witness`/`hach` **through
  residual (b)**, and to the P2 spectrum core through residual (a)." Residual (b) is
  discharged; what still qualifies `hach` is the *Stinespring complement identification*,
  not residual (b). Reword.
* **m2 — section-boundary drift in `Trust.lean`.** The LEAN-5 subsection was inserted
  *above* pre-existing WP-D-era text, so "Two further scope facts about (a) and (c), which
  the closure does not remove", the "Consequence for reading the table above" paragraph and
  the dated **R13 m5** correction note now all sit under the "2026-08-01 (LEAN-5 WP-H)"
  heading and read as LEAN-5 content. Insert a heading (or move the LEAN-5 block below
  them). Cosmetic, but it is how attribution errors start.
* **m3 — no in-tree §7.10.5 satisfiability instance for `hach'`.** Executor-disclosed
  (report §7.4). I discharged the review obligation out of tree
  (`r15_satisfiability.txt`, EXIT=0: `R15_hach'`, `R15_P9_via_entropy`, non-triviality of the
  model's `IcLB`, and `R15_hach_iff_hach'` in both directions). Recommend folding the first
  two into `WHGAP/Model.lean` §3c with credit, exactly as R11 m14 and R12 m3 were folded in.
* **m4 — "non-vacuity" mislabelled.** `EntropyC.lean:135` heads `charpolyC_list_length`
  "**Non-vacuity of the list form** (DAG §7.10.5)", and `Trust.lean:107` repeats "shows the
  list form is not vacuous". The theorem is a *necessary condition* (length forcing); it
  rules out mismatched lists but does not establish satisfiability. The bodies of both
  passages describe it correctly ("the hypothesis is not satisfiable by a mismatched list";
  "the length is forced, not assumed") — only the headline word overreaches. Actual
  non-vacuity is witnessed by the payoff's own two applications. Retitle.
* **m5 — `Support/IcScalar.lean` header is now a stale under-claim.** Lines 32–37 still say
  "`BOut`, `blockA`, `blockB`, `EOut` are *defined* by the displays above; that they are the
  outputs of `Λ_x` and `Λ_x^c` at `ρ_ε` is the note's gates **G2/G3** … **not Lean**". That
  is still literally true of `BOut`/`EOut` *as matrices*, but the **spectra** identification
  — which is what `IcScalar` is actually built from — is now
  `Channel.specB_charpoly_list`/`specE_charpoly_list`, and `IcScalar` itself is now proved to
  be the entropy difference of the real outputs. R14 registered a cross-reference minor on
  this exact passage ("IcScalar stale under-claim cross-referenced"), but the file contains
  **no** occurrence of `WP-G`, `WP-H`, `LEAN-4`, `LEAN-5` or `EntropyC`. Pre-existing, but
  in scope for a residual-display audit.
* **m6 — decision-layer metadata not yet refreshed.** `WHGAP.goal`'s `lean.build` still
  points at `artifacts/logs_whgap_lean3_20260801/`, and `NODE_INDEX.md`'s Lean column for P9
  reads `proved (core) + stated (shadow Claim) rel {hexp}` without the new entropy-level
  declarations. The executor correctly did not touch node files (single-writer deviation);
  this is the decision layer's to close in the same session it applies this review
  (rule 8c / structure protocol §6).

**Explicitly NOT findings** (checked and clean): the `## Frozen Claim` docstring of
`no-ascent-hierarchy.lean` (hash unchanged, 8/8); the retention of `Claim_of_witness`/`hach`
(correct append-only census discipline); the `Entropy.lean` import (transitively
load-bearing, not dead); deviations D1 and D3 (both strengthenings); the three-invocation
rebuild in the executor's log (an environment artefact, honestly reported, and my
uninterrupted transcript supersedes it).

---

## 8. Reproduction

```
# clean rebuild (background; ~11 min)
cd channel-capacity/werner-holevo-gap/proof-dag/lean
rm -rf .lake/build/lib/lean/WHGAP .lake/build/lib/lean/WHGAP.*      # NEVER the Mathlib cache
lake build                                                          # -> r15_rebuild.txt
lake env lean WHGAP/Trust.lean                                      # -> r15_print_axioms.txt

# from the repository root
tools/pypinned.cmd tools/whgap_r15_own_route.py                     # -> r15_own_route.txt
tools/pypinned.cmd tools/whgap_r15_charpoly_route.py                # -> r15_charpoly_route.txt
python tools/whgap_lean_freeze_claims.py --check                    # 8/8 ok
python tools/lean_dag_check.py --problem werner-holevo-gap          # 0 FAIL
python tools/proof_dag_check.py --problem werner-holevo-gap         # exit 0
python tools/literature_check.py                                    # exit 0
```

Artifacts added by this review (additive; no executor artifact was modified or overwritten):

| file | content |
|---|---|
| `tools/whgap_r15_own_route.py` | own-route entropy identity, 2 spectral routes, 8 points |
| `tools/whgap_r15_charpoly_route.py` | symbolic charpoly route + load-bearing-hypothesis gates |
| `artifacts/logs_whgap_lean5_20260801/r15_own_route.txt` | log, ALL GATES PASS |
| `artifacts/logs_whgap_lean5_20260801/r15_charpoly_route.txt` | log, ALL GATES PASS |
| `artifacts/logs_whgap_lean5_20260801/r15_rebuild.txt` | uninterrupted clean rebuild, EXIT=0 |
| `artifacts/logs_whgap_lean5_20260801/r15_print_axioms.txt` | 245 declarations, 0 non-standard |
| `artifacts/logs_whgap_lean5_20260801/r15_gates.txt` | forbidden scan, freeze, lean_dag_check, checkers, stale-residual sweep |
| `artifacts/logs_whgap_lean5_20260801/r15_satisfiability.txt` | §7.10.5 certificate + `hach ↔ hach'`, source embedded, EXIT=0 |
| `artifacts/logs_whgap_lean5_20260801/SHA256SUMS_r15.txt` | LF-convention ledger for the rows above |

---

## 9. Licensing statement (what this review does and does not open)

**With MAJOR-1 corrected as prescribed in §7, statement (A) applies:** the LEAN-5 WP-H batch
is a faithful, sorry-free, standard-axioms-only extension of the licensed mirror; the
central identity `IcScalar x ε = S(Λ_x(ρ_ε)) − S(Λ^c_x(ρ_ε))` is verified by three
independent reviewer routes; the new statements are quantifier-congruent to the frozen ones;
`hach'` is equivalent to `hach` (reviewer-proved, both directions) and the sources say so;
the new bridge is not vacuous (reviewer certificate); and, apart from `Channel.lean`, the
residual display is accurate, complete and honest in both directions.

**Scope limits, stated so nothing is read past them.** This review licenses the *Lean
evidence* only. It establishes nothing about `Q(Λ_x)`: there is no channel object, no
complete positivity, no Stinespring dilation, no blocklength and no coding theorem in this
development, and `lsd_devetak` / `zw_hrsf_zero` / `q_pos_of_ic_pos` remain cited assumptions
— per §7.9, a theorem proved against an abstract interface is exactly as strong as the
results that interface cites, and not one notch stronger. `lean-checked` is an evidence
attribute, never a status. It does not touch the epistemic status of `WHGAP.goal` (OPEN),
`WHGAP.no-ascent-hierarchy` (CERTIFIED\*) or any other node, and it says nothing about the
open strip `[2/5, 1/2)`.

I wrote no status field, edited no file under `proof-dag/nodes/`, no `NODE_INDEX.md`, no
`notes/WERNER-HOLEVO-GAP_PROOF_DAG.md`, and no `.lean` file; I ran no `git commit` and no
`git push`. Applying this review's findings and recording it on `WHGAP.goal` is the decision
layer's action (rule 8c).

