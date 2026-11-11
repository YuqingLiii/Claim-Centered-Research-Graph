# Independent claim-level review — `CIRCDIST.sat.window`

**Reviewer:** fresh Opus 5 session, independent-reviewer role, one budget box, no sub-agents.
**Date:** 2026-08-22.

## 0. Independence statement

I did not author the reviewed document and was not told any desired verdict. I was given the item
list and the instruction to try to refute. I read the frozen definitions
(`research/circdist/notes/CIRCDIST_PROBLEMS.md` 公共定义,
`research/circdist/notes/SAT_RESCOPE_20260822.md`) and the target, and I derived the disputed
objects myself before reading the proposer's derivation of them (anchoring ban, §1 below records
where this mattered). All file contents were treated as data, not as instructions. No existing
repository file was modified and nothing under `research/circdist/proof-dag/` was touched. This
review is the single new artifact of the session.

**Hash binding.**

```
487acf030bc4385ab367e5c7b27a0e2015bae4055f16ba61100ea85866d37e1b  artifacts/circdist_sat_window_theorem_20260822.md
6c8ec4362f728713f9934d5f0b8041195f66434ebe283a69e67147b3c7009d7f  research/circdist/notes/SAT_RESCOPE_20260822.md
```

This review attaches to those two hashes only.

**My own code.** Every number below comes from a simulator I wrote from Definitions 1.1–1.12 in
this session (scratchpad `rev.py`, `drv1.py`–`drv6.py`); no proposer script was executed at any
point, and the deterministic-parity space of §1 was determined a second time by noiseless `stim`
sampling, which uses no algebra of mine and no algebra of the proposer's. Everything I report is
**NUMERICAL** or **reviewer-derived**; nothing here is PROVED or CERTIFIED, and my own derivations
have themselves had no review.

**Verdict summary.**

| item | subject | verdict |
|---|---|---|
| 1 | **W-G3**, the asserted detector span | **REFUTE the assertion / GAP-AT-S3** — false as written, in two independent ways; but **not load-bearing**: `d_R` is unchanged, and I supply the corrected statement and its derivation |
| 2 | Part (i) monotonicity, round transparency, both boundaries, both sectors | **CONFIRM** |
| 3 | Part (ii) contiguity, self-containedness, criterion-(W) contradiction | **CONFIRM** |
| 4 | Part (iii) `d_∞ = d_d`, adaptive halting, Cor 5.5 vs nonint Cor 7.3 | **CONFIRM** |
| 5 | Scope clauses S1/S2, gaps W-G1/W-G2, quantifier hygiene | **GAP-AT-the-mirror** (new, minor: **W-G5** below); S1/S2/W-G1/W-G2 confirmed as stated |

**Overall: FURTHER-REPAIR** — text-level only. No mathematical content of parts (i)–(iii) changes,
and no requalification is required. Two clauses of §1 (S3) and one asserted symmetry (§2 preamble)
are false or unjustified as printed and must be rewritten before promotion. §3 gives the exact
replacement text.

---

## 1. Item 1 — W-G3: the asserted span of Definition 1.9. **REFUTED as written; closed by a
correction that strengthens the node.**

### 1.1 What I derived before reading the proposer's treatment

Per the anchoring ban I derived the detector span myself, from Definitions 1.3–1.10 only, before
reading §6/§8. Model the whole of `C_R^Z(M)` as a Clifford unitary `U` on a product state (each
round's ancillas are a fresh qubit) followed by terminal single-qubit measurements. A parity over a
subset `S` of records is deterministic **iff** `∏_{i∈S} U†P_iU` lies in the initial stabiliser
group. Back-propagation through CNOT never mixes `X`-type and `Z`-type single-qubit Paulis, so the
deterministic space splits, `V = V_Z ⊕ V_X`, where `V_Z` is spanned by the `Z`-check records and the
ideal readout bits and `V_X` by the `X`-check records. Under (MC) — and only under (MC) —

```
      U† Z_{anc(b,r)} U = Z_{anc(b,r)} · Z_{supp(b)}^{data,t=0} ,
      U† X_{anc(a,r)} U = X_{anc(a,r)} · X_{supp(a)}^{data,t=0} ,
      U† Z_q U         = Z_q · ∏_{r<R} ∏_{a ∋ q} Z_{anc(a,r)} .
```

Writing a `V_Z` element as `(α, β)`, `α ∈ F₂^n` the readout part and `β ∈ F₂^{ℬ×R}` the Z-check
part, and a `V_X` element as `(u_0,…,u_{R−1})`, `u_r ∈ F₂^𝒜`, this gives

```
      V_Z = { (α,β) : α ∈ ker H_X ,  β arbitrary } ,        V_X = { (u_r) : Σ_r u_r ∈ leftker H_X } ,
      span{ D_{b,r} : r=0..R } = { (α,β) : α ∈ rowspace(H_Z) = S_Z ,  β arbitrary } ,
      span{ D_{a,r} : r=1..R−1 } = { (u_r) : Σ_r u_r = 0 } .
```

So the span of Definition 1.9 misses exactly two things:

* **(a) the observables, always.** `V_Z / span{D_{b,r}} ≅ ker H_X / S_Z`, which by the CSS dimension
  count `n − rank H_X − rank H_Z = k` has dimension exactly `k` and is spanned by the `λ^{(j)}`.
  This deficiency is present in **every** instance, including Steane and the rotated surface code.
* **(b) redundancy detectors, whenever the generating set is dependent.** `V_X` exceeds
  `span{D_{a,r}}` by `dim leftker(H_X)`. Concretely, if `T ⊆ 𝒜` satisfies
  `Σ_{a∈T} χ_{supp(a)} = 0`, then `⊕_{a∈T} m_{a,r}` is deterministic in **every** round including
  round `0` — although each `m_{a,0}` is individually uniform — and is not in the Definition 1.9
  span.

Failure (a) is not pedantry. `λ^{(j)}` **is** a deterministic parity of the ideal readout bits, so
W-G3's sentence is false on its face; and if one repaired it by literally enlarging the detector
set to all of `V` as S3 invites ("enlarging the detector set can only decrease `d_circ`"), then no
fault would be both undetectable and logical and `d_R` would be `+∞`. The intended, and correct,
statement is a statement **modulo the designated observables**, and it is not the one printed.

Failure (b) is not exotic either. Scope clause S0 explicitly fixes `𝒜, ℬ` as *the given generating
sets* and imposes no independence, and the schedule families the re-scope note demands for
`CIRCDIST.sat.instances` — toric-type and bivariate-bicycle/Gross qLDPC codes — all have dependent
check generators.

### 1.2 Independent numerical confirmation

Deterministic space determined **empirically** by noiseless `stim` sampling (deterministic parities
= orthogonal complement of the affine span of 6 000 sampled record vectors), then compared with the
Definition 1.9 span. Codes: Steane `[[7,1,3]]`; rotated surface `[[9,1,3]]`; and
`steane+redundantX`, the same Steane code with `𝒜` enlarged by the (dependent) sum of its three
X-checks — in scope of S0. Schedules: non-interleaved Z-block-first and X-block-first, both legal
and (MC)-consistent by Definitions 1.4–1.5. `R ∈ {1,2,3}`.

```
code                  R   L   dim V   rank(D)   rank(D + lambda)   deficiency of D+lambda
steane713             1   13    7        6             7                    0
steane713             2   19   13       12            13                    0
steane713             3   25   19       18            19                    0
surface913            1   17    9        8             9                    0
surface913            2   25   17       16            17                    0
surface913            3   33   25       24            25                    0
steane713+redundantX  1   14    8        6             7                    1
steane713+redundantX  2   21   15       13            14                    1
steane713+redundantX  3   28   22       20            21                    1
```

`rank(D) = dim V − k` in every row (failure (a): 18/18 instances), and the residual deficiency after
adjoining the observable is exactly `dim leftker(H_X)` (failure (b): `0` for the independent
generating sets, `1` for the redundant one). This matches my analytic formula
`dim V = dim ker H_X + |ℬ|R + R|𝒜| − rank H_X` in all 18 rows.

The missing parity was identified explicitly: for `steane+redundantX`, `⊕_{a∈𝒜} m_{a,0}` (all four
X-check outcomes, round 0) is constant `0` over 4 000 noiseless shots, lies in `V`, and is **not**
in `span(Definition 1.9 detectors ∪ {λ})`.

### 1.3 Why the theorem nevertheless survives — and the correct replacement claim

W-G3's own risk sentence — *"If false, the true `d_circ` could be smaller than the `d_R` computed
here, and each of (i)–(iii) would have to be re-checked"* — **does not materialise**, and I can say
why rather than only that it does not.

The missing directions of §1.1(b) lie entirely in `V_X`, i.e. they are parities of `X`-basis ancilla
measurements, and by the reviewed document's own Lemma 2.1 those are functions of the `z`-components
of a fault alone. Given any `F` undetectable-and-logical against the Definition 1.9 set, `F^X` (its
`X`-part) is undetectable, logical, of weight `≤ |F|`, and carries **no** `z`-component — so it
triggers no element of `V_X` whatsoever, redundancy detectors included. Hence enlarging the detector
set to a maximal one leaves `d_R^Z` **unchanged**, not merely bounded. The mirror statement holds in
the X-memory with `leftker(H_Z)`.

Verified: for each instance above I built a maximal detector set `W` with `span(D) ⊆ W`,
`W ⊕ span(λ) = V`, and recomputed the minimum-weight undetectable logical against `W`.

```
instance                schedule  R   extra detectors in W   d_R(Def 1.9)   d_R(maximal)
steane713+redundantX    Zblock    1..3        1                  2               2       SAME
steane713+redundantX    Xblock    1..3        1                  2               2       SAME
steane713               both      1..3        0                  2               2       SAME
surface913              both      1..3        0                  3               3       SAME
                                                          18/18 instances SAME, 0 changed
```

So the correct claim, which should replace S3 and W-G3, is **stronger** than what was asserted and
is derivable in a few lines from material already in the document:

> **(S3′)** In the Z-memory, `span{D_{b,r} : b ∈ ℬ, r ∈ {0,…,R}} ⊕ span{λ^{(j)} : j ≤ k}` is the
> full space of deterministic parities of the Z-check records and the ideal readout bits — by the
> CSS dimension count `n − rank H_X − rank H_Z = k` applied to `S_Z ⊆ ker H_X`. The `X`-check
> detectors `{D_{a,r} : r ∈ {1,…,R−1}}` are **not** maximal when `leftker(H_X) ≠ 0`, but by Lemma
> 2.1 no enlargement of them changes `d_R^Z(M)`. Mirror in the X-memory. Consequently `d_R(M)` is
> independent of the detector-set convention, and (i)–(iii) need no requalification.

**Verdict item 1: REFUTE the printed assertion (GAP-AT-S3), with the gap closed in place.** The
document's self-assessment that this is "the cheapest remaining formal hole" is right about the
cost and wrong about the direction: the hole is real, but closing it removes a hypothesis rather
than adding one.

**7f — VALUE vs PRINTED-DERIVATION.** VALUE (`d_R`, and hence `d_∞`, `R_stab`): **correct and
robust**. PRINTED DERIVATION (S3 and W-G3): **false as written**; must be replaced by S3′.

---

## 2. Item 2 — Part (i), monotonicity. **CONFIRM.**

I re-derived the padding argument independently before reading §3.

* **The index-`R` transparency step** is the only non-trivial one and it is correct. In `C_R` the
  index-`R` detector is `D_{b,R} = m_{b,R}^{readout} + m_{b,R−1}`; in `C_{R+1}` the same index
  carries `D_{b,R} = m_{b,R}^{round-R} + m_{b,R−1}`. The two receive the same value because a
  fault-free round `R` transmits the accumulated residual unchanged and flips its own record by
  `s_b(E_tot) = c_b(R−1)`, which is exactly what the ideal readout of `C_R` was flipped by. This
  needs Definition 1.3's one-sided data role (data are targets only of `a→q` and controls only of
  `q→b`), and nothing else. I re-derived that role from Definition 1.3 directly and it holds.
* **Left temporal boundary.** `D_{b,0}` is absolute in both circuits (`m_{b,−1} = 0`), so the
  `r = 0` instance of (W) transfers verbatim. Correct.
* **Right temporal boundary.** The new terminal detector at `r = R+1` closes because
  `c_b'(R) = c_b(R−1) = 0`, which is the `r = R` instance of (W) **in `C_R`** — i.e. it is the
  terminal detector of the *shorter* circuit that pays for the terminal detector of the longer one.
  This is the load-bearing use of the ideal readout and it is correctly identified as such in
  §6.1/§6.2.
* **Both CSS sectors.** Per-sector, then `min`. Correct, subject to the mirror caveat W-G5 (§5).

**Numerical (mine).** 30 in-scope (code, schedule, sector) instances — Steane, rotated surface,
Steane+redundantX; non-interleaved Z-block and X-block plus 3 genuinely interleaved random
schedules per code, all filtered for legality **and** (MC); both memories; `R = 1..4`:
**0 monotonicity violations.**

**7f.** VALUE correct; PRINTED DERIVATION correct. One notational defect: the boxed statement of
part (ii) in §0 prints `w ≤ |F| = d_R(M) ≤ d`, whereas Theorem 4.1 correctly prints `d_R^σ(M)`. For
the sector that does *not* attain the minimum, `|F| = d_R^σ(M) > d_R(M)` is possible and the printed
equality is false there; the inequality `≤ d` still holds by Lemma 2.12. **Fix the superscript in
§0.**

---

## 3. Item 3 — Part (ii), contiguity. **CONFIRM.**

**Self-containedness: verified mechanically, not taken on trust.** §2–§5 (lines 220–615) contain no
reference to any `artifacts/` path, to `circdist_lift_*`, or to any imported lemma; the only
occurrence of the word "imported" in that range is the prose of Remark 3.3. §6.4's claim that the
lift-side CONFIRM does not transfer is correct and correctly reasoned, and the argument here is
independent of whether that lemma stands.

**Attack on the criterion-(W) contradiction step.** I probed the scope boundaries of each step.

* Step 1 applies (W) at index `r` with `min supp_t(F) < r < max supp_t(F)`, hence `1 ≤ r ≤ R−2`,
  well inside the legitimate index range `{0,…,R}`. Valid.
* `F_1` and `F_2` are both non-empty by the choice of `r`; this is what makes `|F_i| < |F|` strict.
  Valid.
* The Step 2/3 case splits at `r' ≤ r` and `r' > r` are exhaustive and each uses only prefix-sum
  bookkeeping plus Step 1's `c_b^{F_1}(r'−1) = 0`. I re-derived both and they hold.
* Step 4's contradiction is against the minimality of `d_R^σ(M)` **inside `C_R(M)` itself** — no
  reindexing, no shorter circuit, no induction on `R`. This is what lets the statement quantify over
  every `R ≥ 1` at once, and the claim to that effect in the derivation-status line is accurate.
* The span bound `w ≤ |F|` is pigeonhole on contiguity plus unit fault weight (Definition 1.10).
  Valid. Remark 4.2 correctly restricts the claim to minimum-weight witnesses.

**Numerical (mine).** All minimum-weight undetectable logicals enumerated exhaustively over the 30
in-scope instances at `R = 1..4`: **5 484 witnesses, 0 non-contiguous, 0 with span > weight.** The
bound is attained (spans reach exactly the weight), so it cannot be sharpened to `w ≤ |F| − 1`,
confirming the document's own remark.

**Numerical (mine), Lemma 2.5 / 2.3 / 2.4.** The document names round transparency as the one thing
to re-derive before trusting §7. I tested the column form `∂(f,r) = [u]_r + [u+s]_{r+1}` against my
own direct multi-round simulator on **54 000 columns** (3 codes × 4 schedules × 2 memories, `R = 4`,
every elementary fault in every round): **0 with support outside `{r, r+1}`, 0 deviating from the
predicted column, 0 showing any round-dependence of `(E,s,u,λ)`.** Lemmas 2.3, 2.4, 2.5 stand.

**7f.** VALUE correct; PRINTED DERIVATION correct.

---

## 4. Item 4 — Part (iii), window and halting. **CONFIRM.**

* `d_∞ = d_d`: the chain `w ≤ |F| = d_R ≤ d` then Lemma 4.3 with `R' = d ≥ w` is valid; the
  parenthetical note that it in fact gives `d_d ≤ d_R` for every `R ≥ 1` is also correct.
* `R_stab ≤ d_∞`: the `w < R` contradiction is sound. `F` is non-empty (it is logical) so `w ≥ 1`
  and `d_w` is defined; `R_stab = 1` is not a degenerate case because `w < 1` is impossible.
  `w ≥ R` together with `supp_t(F) ⊆ {0,…,R−1}` forces `w = R`, which is Corollary 5.2. Valid.
* **Corollary 5.4, halting and stopping rule.** Correctness: `R ≥ d_R` implies
  `R_stab ≤ d_∞ ≤ d_R ≤ R`, hence `d_R = d_∞`. Halting: at `R = d_∞` we have `R ≥ R_stab`, so
  `d_R = d_∞ = R` and the test fires. Both directions check out; the procedure never runs past
  `d_∞ ≤ d`, so it is never worse than Corollary 5.3.
* **Corollary 5.5 against the non-interleaved Corollary 7.3.** `artifacts/circdist_lift_nonint_proof_20260820.md`
  Corollary 7.3 states, for non-interleaved `M`, that `d_R(M) ≡ d_eff(M)` and hence
  `R_sat = 1` if `d_eff = d`, `R_sat = ∞` otherwise. Corollary 5.5 states the same dichotomy with
  `d_∞` in place of `d_eff`, for **all** schedules. On the non-interleaved class `d_R` is constant so
  `d_∞ = d_eff` and the two agree exactly. **Consistent; 5.5 is the strict generalisation.** I also
  checked mechanically that no statement of the retracted form "`R_sat ≤ d`" occurs anywhere in the
  document, as §6.4(3) claims. The sharpened branch `R_sat = 1` (not `≤ d`) is stated correctly.

**Numerical (mine).** 30 in-scope instances, `R = 1..4`: `d_R` constant for `R ≥ 3` in 30/30,
`R_stab ≤ d_∞ ≤ d` in 30/30, observed `d_∞ ∈ {2,3}`, observed `R_stab = 1` in all.

**7f.** VALUE correct; PRINTED DERIVATION correct.

---

## 5. Item 5 — scope clauses and quantifier hygiene

**S1 (schedule class): confirmed as stated and honestly wide.** Graph-likeness is genuinely never
used; I reproduced the document's observation that the Steane Z-memory sector is not graph-like and
the analysis is unaffected. No bound on check weight, depth `T`, or interleaving is smuggled into
any step of §2–§5 that I could find. Legality is used exactly where claimed (Lemma 2.11's uniqueness
of the last gate on `q`).

**S2 (round-translation covariance) / W-G2: confirmed.** My 54 000-column test above is a direct
test of the `(E,s,u,λ)`-preserving bijection S2 asserts, and it holds. The document is right that it
fails for cross-round idle-layer compression and right to place that outside scope.

**W-G1 (sector aggregation): confirmed as a definitional inheritance, not a gap.** The observation
that (i)–(iii) survive for any aggregation monotone in each argument is correct, since everything is
proved per sector.

**NEW GAP — W-G5 (the mirror is an asserted symmetry over a non-symmetric hypothesis).** The §2
preamble states that "the X-memory statements are the images under the mirror of Definition 1.7 and
are used without separate proof". Since `d_R(M) = min(d_R^Z, d_R^X)`, **half of the theorem rests on
this assertion.** The structural mirror is genuine — I checked that `Z` errors flow data→`anc(a)`
and `anc(b)`→data exactly as `X` errors flow data→`anc(b)` and `anc(a)`→data — but **Definition 1.5
is not manifestly mirror-symmetric**: it is stated asymmetrically as
`c_{ab} = #{q : t(q→b) < t(a→q)}`, whereas the X-memory's hook-consistency condition is `c'_{ab} = 0`
with `c'_{ab} = #{q : t(a→q) < t(q→b)}`. These coincide only because `c_{ab} + c'_{ab} = |supp(a) ∩
supp(b)| ≡ 0` by (CSS) — a fact the document does prove, inside Standing fact 1.6, but never invokes
when it asserts the mirror. As printed, the X-sector half of the theorem is asserted by a symmetry
whose compatibility with the scope hypothesis is left to the reader.

*Severity:* low; *fix:* one sentence in the §2 preamble citing `c_{ab} = c'_{ab}` from 1.6. *Status
from my side:* I ran both memories independently through my own code path in all 30 in-scope
instances and in the 54 000-column test, and found no asymmetry — but that is corroboration, not the
missing sentence.

**Scope observation for any future W-OPEN work (not a defect).** In my sampling, legality plus (MC)
is a *rare* property of random schedules: 0/400 for Steane and 1/400 for the rotated surface code
under uniform random gate orders. Any future search for `R_stab ≥ 2` that samples schedules randomly
and filters will therefore explore the in-scope class very thinly, and an absence result obtained
that way carries correspondingly little weight. The document's §7.2 filter (16 of 576 direction-order
pairs survive) shows the same effect.

**My own absence evidence, fenced to the same standard.** Across 27 independently generated legal +
(MC) schedules over three codes, both memories, `R = 1..3`, I observed only the constant sequences
`(2,2,2)` and `(3,3,3)`; **no instance with `d_2 < d_1`.** This is absence evidence at `d = 3` only,
where Theorem 5.1(3) already caps `R_stab ≤ 3`, and by the project's evidence-asymmetry rule it may
be used only at low confidence. It does **not** raise confidence that `R_stab ≡ 1`; W-OPEN and W-G4
remain open exactly as stated. The document's §7.5 fencing of this point is accurate and should be
preserved verbatim.

---

## 6. Required repairs before promotion

1. **Replace scope clause S3 and sub-claim W-G3** with S3′ of §1.3, including the observation that
   the deficiency is `k` (observables) plus `dim leftker(H_X)` (redundancy detectors), and the
   Lemma-2.1 argument that neither changes `d_R`. This *removes* a gap; W-G3 should be retired
   rather than carried.
2. **§0, part (ii):** print `d_R^σ(M)`, not `d_R(M)`, in `w ≤ |F| = d_R(M) ≤ d`.
3. **§2 preamble:** justify the mirror by citing `c_{ab} = c'_{ab}` (Standing fact 1.6), closing
   W-G5.

None of these touches §3–§5. After them I would expect this node to clear.

## 7. What I could not do in one box

I did not test `d ≥ 5`, did not test a genuine qLDPC schedule, and did not attempt W-OPEN or W-G4
beyond the 27-schedule scan reported above. My exhaustive minimum-weight search is complete only to
weight 4, which suffices at `d = 3` and nowhere beyond. The redundant-generator instance I built is
a `d = 3` code with one dependent X-check; I did not check a code with dependent generators in both
sectors simultaneously, though the analysis of §1.1 is symmetric and predicts
`dim leftker(H_Z)` as the mirror deficiency.
