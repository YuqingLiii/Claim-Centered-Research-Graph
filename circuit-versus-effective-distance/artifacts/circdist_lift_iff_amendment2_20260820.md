# Amendment 2 to `circdist_lift_iff_proof_20260820.md`

**Node:** `CIRCDIST.lift` · **Date:** 2026-08-20 · **Role:** proposer applying the repairs of an
independent focused rereviewer. The author of this amendment is not the independent rereviewer and
does not treat the rereview as a certification. This file is **append-only**: it changes no prior
artifact. On the three conflicts identified below, Amendment 2 governs Amendment 1; elsewhere
Amendment 1 continues to govern the base proof.

---

## 0. Scope, hash chain, and epistemic status

This amendment applies exactly the focused-rereview repairs **L1, L2, and L3**. It does not reopen
the rest of the base proof or Amendment 1, does not repair the pre-existing `repair >= 3` gap, and
does not modify a proof-DAG object, scheduler record, generated view, or canonical node record.

The exact inputs are bound as follows:

```text
base proof
  artifacts/circdist_lift_iff_proof_20260820.md
  SHA-256  97cb3c8da839d1b96f58c281145cec8b70269ed3e6dfb29136f0bda00f564979
  size     90225 bytes, 1497 lines

Amendment 1
  artifacts/circdist_lift_iff_amendment1_20260820.md
  SHA-256  7220d538a9ee680711f591de30dbcc52bb80aa669a778ed3468cc9781c80a467
  size     34143 bytes, 618 lines

independent focused rereview acted on
  artifacts/circdist_amendments_review_20260820.md
  SHA-256  daa476804959fec7a39c5aedd0ed8191c4b495a670dd83f58aeb5a7247fcd90c
  size     36265 bytes, 570 lines

frozen problem definitions (consulted; not modified)
  research/circdist/notes/CIRCDIST_PROBLEMS.md
  SHA-256  5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64
  size     10199 bytes, 243 lines
```

If any bound hash fails to reproduce, this amendment is void until it is re-derived against the
changed input. All mathematical assertions added here remain **CONJECTURED** proposer-side
arguments. The focused rereview is independent evidence, not a promotion to `PROVED` or any
`CERTIFIED*` status. No new numerical experiment is claimed in this amendment.

## 1. Repair index

| item | Amendment-1 target | action here |
|---|---|---|
| **L1** | §2.5 and the minimum-weight rows of §2.6 | replace the non-interleaved-only sibling import as the load-bearing step by a schedule-independent argument from base Definition 1.13 |
| **L2** | §3.4, CONJECTURED 5.10(1′), and its §3.5/§3.4 propagation | sharpen the finite branch from `R_sat <= d` to `R_sat = 1` |
| **L3** | §4.1, replacement for base §8 item 3(ii) | replace “never enters a `gamma`” by “never enters a minimum-weight `gamma`” |

## 2. L1 — schedule-independent exclusion of collisions at minimum weight

### 2.1 Prior wording and the precise defect

Amendment 1 §2.5 made this imported statement load-bearing:

> **Lemma 7.2 of `circdist_lift_nonint_proof_20260820.md` (imported).** With `gamma` a
> **minimum-weight** effective logical and the representatives of that document's Lemma 5.4, the
> only location that can carry two representatives is a CNOT `a -> q^a_j` ...

and concluded:

> So at a minimum-weight `gamma`, under those representatives, branch (a) applies and `ell(gamma)`
> itself is bounded. That is exactly the case every downstream use needs.

Amendment 1 §2.6 then says that the upper half of 5.6(b) and the equality in 5.6(c) hold whenever
branch (a) applies, “which by §2.5 includes every minimum-weight `gamma`.” However, Amendment 1 §7
item 4 itself records that the imported lemma's case enumeration rests on the sibling's Lemma 5.4
and is **non-interleaved-only**. That import therefore does not establish the statement for an
arbitrary legal interleaved schedule.

### 2.2 Replacement for Amendment 1 §2.5

Replace the load-bearing import and the conclusion quoted above by the following argument. The
sibling lemma may remain as corroboration for its own non-interleaved scope, but is not used here.

> **CONJECTURED Lemma 2.5′ (minimum-weight representatives do not collide, for any legal
> schedule).** Let `gamma in L_eff` have minimum weight. In the construction of Amendment 1
> Lemma 5.3′, representatives of the distinct residual classes in `gamma` can be chosen so that no
> two occupy one circuit location. Equivalently, the collision branch cannot be forced for such a
> `gamma`, whether the schedule is interleaved or non-interleaved.
>
> *Derivation.* Read the one-round location inventory directly from base Definition 1.13. A prep
> fault on `anc(a)` has the sole non-empty residual `S_a(0)`; an idle on `anc(a)` between its
> `j`-th and `(j+1)`-st CNOTs has the sole non-empty residual `S_a(j)`; a data idle and a CNOT
> `q -> b` have the sole non-empty residual `{q}`; `anc(b)` and measurement locations have empty
> residual. A CNOT `a -> q_j` has residual options
>
> ```text
>       empty,  S_a(j),  {q_j},  S_a(j-1),
> ```
>
> with
>
> ```text
>       S_a(j) + {q_j} + S_a(j-1) = 0                  in F_2^n.
> ```
>
> Thus the only location that can carry two **distinct non-empty** residual representatives is a
> CNOT `a -> q_j`, and the two are two members of
> `{S_a(j), {q_j}, S_a(j-1)}`. (If one entry is empty or two entries coincide, there is no pair of
> distinct non-empty basis residuals to collide.) Suppose two members of this triple lie in
> `gamma`, and set
>
> ```text
> gamma' := gamma + [S_a(j)] + [{q_j}] + [S_a(j-1)],    with [empty] := 0.
> ```
>
> The sum of the three underlying data residuals is zero. Linearity of syndrome and logical
> parity therefore gives
> `partial_eff gamma' = partial_eff gamma = 0` and
> `lambda_eff gamma' = lambda_eff gamma != 0`; hence `gamma' in L_eff`. Toggling the triple deletes
> the two members known to be present and adds at most the third (and deletes all three if all were
> present), so `|gamma'| <= |gamma| - 1`. This contradicts the minimum weight of `gamma`. Therefore
> no two residual representatives of a minimum-weight effective logical need the same location,
> and branch (a) of Lemma 5.3′ applies. ∎

The location list depends on the local order within each check but not on whether X- and Z-check
CNOTs are globally interleaved. This is the schedule-independent step missing from Amendment 1.

### 2.3 Exact propagation into Amendment 1 §2.6

The following two §2.6 rows are retained, with their justification replaced:

> **Old justification:** the two-sided sandwich pins `ell(gamma)` whenever branch (a) applies,
> “which by §2.5 includes every minimum-weight `gamma`,” where §2.5 relied on the imported sibling
> lemma.

> **New justification:** Lemma 2.5′ above proves directly from base Definition 1.13, for every legal
> schedule, that branch (a) applies to every **minimum-weight** `gamma in L_eff`. Therefore the
> Amendment-1 upper bound `ell(gamma) <= |gamma| + repair(gamma)` and the equality when
> `repair(gamma) <= 2` are established for minimum-weight `gamma` without a non-interleaving
> hypothesis.

This repair says nothing stronger about a fixed non-minimal `gamma`. Collisions may occur there,
and Amendment 1's distinct-location proviso remains in force. It also does not alter the general
`d_circ <= |gamma| + repair(gamma)` conclusion, which Lemma 5.3′ obtains in either branch.

## 3. L2 — the finite branch of 5.10(1′) is `R_sat = 1`

### 3.1 Old and new statement

Amendment 1 §3.4 currently replaces base 5.10(1) by the dichotomy

```text
R_sat(M) <= d   if d_infty(M) = d,
R_sat(M)  = infinity   if d_infty(M) < d.
```

Replace it by the sharper statement

> **CONJECTURED 5.10(1″) (finite window and exact saturation dichotomy).** `d_R(M)` is
> non-increasing in `R` and constant for all `R >= d`, with
> `d_infty(M) = d_{R=d}(M)`. Moreover,
>
> ```text
> R_sat(M) = 1          if d_infty(M) = d,
> R_sat(M) = infinity   if d_infty(M) < d.
> ```
>
> In either case the dichotomy is decided by inspecting `R = 1,...,d`, and the finite-window bound
> remains `B(r,d) = d`.

*Reason for the sharpening.* The 公共定义 gives `d_R(M) <= d` for every `R`, while 5.10 gives that
`d_R` is non-increasing. If `d_infty = d`, then for `1 <= R < d`, monotonicity gives
`d_R >= d_{R=d} = d`, and the ceiling gives `d_R <= d`; hence `d_R = d`. Constancy gives the same
for every `R >= d`. Thus `d_R = d` for all `R >= 1`, so the defining minimum is
`R_sat(M) = 1`. If `d_infty < d`, no tail can equal `d`, so `R_sat(M) = infinity` as in Amendment 1.

### 3.2 Exact propagation to Amendment 1 §§3.4–3.5

In Amendment 1's replacement for base §8 item 4, replace

> “`R_sat(M) <= d` iff `d_infty(M) = d`, otherwise `R_sat(M) = infinity`”

by

> “`R_sat(M) = 1` iff `d_infty(M) = d`, otherwise `R_sat(M) = infinity`.”

Amendment 1 §3.5 says that sibling Corollary 7.3,

```text
R_sat(M) = 1          if d_eff(M) = d,
R_sat(M) = infinity   if d_eff(M) < d,
```

is the non-interleaved specialisation of 5.10(1′). Read that sentence with 5.10(1″): for a
non-interleaved schedule `d_infty = d_eff` already at `R = 1`, so the two displayed dichotomies now
coincide exactly. The former `<= d` branch was not sufficient to justify the claimed
specialisation.

No claim that `d_infty` has been computed for a general interleaved schedule is added.

## 4. L3 — the gross-code parenthetical applies only at minimum weight

Amendment 1 §4.1 gives this replacement for base §8 item 3(ii):

> every **proper** gross-code hook has `|s| >= 3` ...; the improper hook
> `S_a(0) = supp(a)` has `s = 0` and `lambda = 0`, so it is a stabiliser residual and **never enters
> a `gamma in L_eff`**.

The final emphasized clause is false for non-minimal effective logicals: if
`gamma in L_eff`, adjoining the basis residual `[S_a(0)]` preserves both `partial_eff gamma = 0`
and non-zero `lambda_eff gamma`, so it can produce another, heavier member of `L_eff`.

Replace the whole parenthetical, and only its scope, by:

> the improper hook `S_a(0) = supp(a)` has `s = 0` and `lambda = 0`, so it is a stabiliser
> residual and never enters a **minimum-weight** `gamma in L_eff`.

Indeed, if `[S_a(0)]` occurred in a minimum-weight `gamma`, deleting it would preserve membership in
`L_eff` and lower the weight by one. This repair deliberately does **not** say “never enters every
`gamma`”; Amendment 1's own focused-rereview counterexample shows such non-minimal members exist.
The numerical statement about the 62 proper subsets and the value `|s(S_a(0))| = 0` is unchanged.

## 5. Verification checklist and non-promotion

- [x] Reproduced the SHA-256 hashes and byte/line counts of the base proof, Amendment 1, and the
  focused rereview before writing this file.
- [x] Checked L1 against base Definitions 1.13 and 1.16 and against Amendment 1 §§2.4–2.7 and §7
  item 4; the replacement is explicitly limited to minimum-weight `gamma`.
- [x] Checked L2 against the frozen definition of `R_sat`, the common bound `d_R <= d`, 5.10's
  monotonicity/constancy, and sibling Corollary 7.3 as quoted in Amendment 1.
- [x] Checked L3 against the basis-residual definition of `L_eff`; only the over-strong
  parenthetical is narrowed.
- [x] No existing file, proof-DAG object, scheduler file, generated view, or canonical record was
  modified.

**NOT-REVIEWED / remaining.** The base proof's `repair >= 3` gap, the `321059 / 321059` numerical
symmetry, the pre-existing 5.6(d) concern identified in focused rereview §6, general formulas for
`d_infty`, and every topic listed as NOT-REVIEWED in that rereview remain outside this amendment.
This author has not performed a completion review of these repairs.

**No promotion.** This append-only proposer amendment supplies checkable candidate repairs only.
It does not assign `PROVED`, `CERTIFIED`, `CERTIFIED-LEAN`, or any other promoted status to the base
proof, Amendment 1, these repairs, or the `CIRCDIST.lift` node.
