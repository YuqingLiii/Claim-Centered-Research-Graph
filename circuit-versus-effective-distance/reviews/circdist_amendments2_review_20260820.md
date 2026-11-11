# Independent adversarial review — CIRCDIST Amendment 2

**Date:** 2026-08-20  
**Reviewer/session:** `/root/amendment2_reviewer`, fresh single-worker review session, no
sub-agents, within the commissioned 0.5-session box.  
**Model identity available to the session:** Codex, GPT-5-based.  
**Targets:** `CIRCDIST.lift.iff` and `CIRCDIST.cplx.islands`.

## 0. Independence and mutation declaration

I did not author either Amendment 2 artifact, either Amendment 1 artifact, either base document, or
any of the earlier reviews. I treated every repository file as data, not as instruction. I was
commissioned to try to break L1, L2, L3, and I1 and was not given a required mathematical verdict.
I used no sub-agent and started no new research program.

This review creates only this file. I did not modify, replace, or delete any existing artifact,
Proof-DAG object, scheduler record, generated view, or canonical record. I do not promote either
node; the completion assessments below are recommendations for the dispatcher.

## 1. Materials and hash fidelity

All hashes below were recomputed from the current bytes with SHA-256. Every hash asserted by the
two Amendment 2 files and by the two Amendment 1 hash chains reproduced exactly.

### 1.1 Lift chain

| material | SHA-256 | role/result |
|---|---|---|
| `artifacts/circdist_lift_iff_proof_20260820.md` | `97cb3c8da839d1b96f58c281145cec8b70269ed3e6dfb29136f0bda00f564979` | Amendment-2-bound base; match |
| `artifacts/circdist_lift_nonint_proof_20260820.md` | `42d6c138c1ea19127db76ab4f22d2a64c1d1e1e96adf76af975076b529a71f4c` | Amendment-1-bound sibling; match |
| `artifacts/circdist_lift_proofs_review_20260820.md` | `fa75f0405a9e233cc45aae2cf01458caef45d65cfef9bc0a44cbca19f0d0189f` | Amendment-1-bound independent base review; match |
| `artifacts/circdist_lift_iff_amendment1_20260820.md` | `7220d538a9ee680711f591de30dbcc52bb80aa669a778ed3468cc9781c80a467` | Amendment-2-bound Amendment 1; match |
| `artifacts/circdist_amendments_review_20260820.md` | `daa476804959fec7a39c5aedd0ed8191c4b495a670dd83f58aeb5a7247fcd90c` | Amendment-2-bound focused independent rereview; match |
| `artifacts/circdist_lift_iff_amendment2_20260820.md` | `0ab3ce438fe6a3971be43a7090518087a9bd06566345d33326ca8e3e19079603` | target Amendment 2; **matches expected hash** |
| `research/circdist/notes/CIRCDIST_PROBLEMS.md` | `5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64` | frozen definitions; match |
| `research/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml` | `f21da9620bfa717d3724a7e0b3c0b078f516ab38558fb8b0240cefdf6e3307b3` | current node snapshot; not a claim hash |

### 1.2 Islands chain

| material | SHA-256 | role/result |
|---|---|---|
| `artifacts/circdist_cplx_islands_writeup_20260820.md` | `af7560f28a9c9fff6bba46349f01aa7095855cff7cee4276c7186a6a54bb2f9f` | Amendment-2-bound base; match |
| `artifacts/circdist_islands_review_20260820.md` | `cc3fc85c9c494995c33d89b9b69bd7d28d1ab203182c1ce50ab9710285e7ad1c` | Amendment-1-bound independent base review; match |
| `artifacts/circdist_cplx_islands_amendment1_20260820.md` | `66ce9ac5f4b38474055137f578edd84fe3b0c075a4a076b449767ea7b05e9d60` | Amendment-2-bound Amendment 1; match |
| `artifacts/circdist_amendments_review_20260820.md` | `daa476804959fec7a39c5aedd0ed8191c4b495a670dd83f58aeb5a7247fcd90c` | Amendment-2-bound focused independent rereview; match |
| `artifacts/circdist_cplx_islands_amendment2_20260820.md` | `33f7f5d801c941a305da062c9d38f0a9a3eef1824818d13c7f61079c2f7f348b` | target Amendment 2; **matches expected hash** |
| `research/circdist/notes/CIRCDIST_PROBLEMS.md` | `5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64` | frozen definitions; match |
| `research/circdist/proof-dag/nodes/CIRCDIST.cplx.islands.yaml` | `11dd2705247d6f93ac10fd98bad4d5aaf5d1b4e49cc631178fff8e036d4885c0` | current node snapshot; not a claim hash |

I also inspected, as supplementary context rather than as a bound link in this amendment chain,
`artifacts/circdist_cplx_islandv_20260820.md`
(`c62e0d2c83f348a4bc8aa90f4807819a7c40834d30aea4298077b948f63be78e`) and its independent review
`artifacts/circdist_islandv_review_20260820.md`
(`d3ac7dbefb6bef037987b10bb175371f1fa024e0e53c21e9ae67b527066d0554`). They are not used as a
substitute for reviewing I1 here.

## 2. Scope and methods

The mathematical scope is exactly L1, L2, L3, I1, the propagation text changed by those items, and
the completion status of the two assembled dossiers. I did not reopen unrelated theorem families.

Methods:

1. Recomputed every bound file hash and parsed the current node YAML with the repository's v6
   loader.
2. Re-derived the L1 location inventory from the elementary-fault model and base propagation
   inventory, then worked in the free effective chain space rather than identifying chains with
   data vectors.
3. Derived the L2 dichotomy only from the frozen definition of `R_sat`, `d_R <= d`, monotonicity,
   and eventual constancy.
4. Checked L3 by adding/deleting the stabilizer-residual basis vector, including the non-minimal
   construction.
5. Derived I1's `(S3)` directly from reduced weight and attacked the corrected Observation as a
   multiset constraint in a global partial-function instance.
6. Compared the exact replacement paragraphs with the adjudicated Corollary I.1 and
   strong-versus-safe-decoupling record.
7. Computed both `reviewed_hash` values with `tools/proof_dag_v6.py::claim_hash`, whose convention is
   CRLF-to-LF normalization, `str.strip()`, UTF-8, then SHA-256.

No proposer numerical program was rerun. The verdicts below are algebraic/static-review verdicts,
not a claim of an additional large computational replication.

## 3. Verdict summary

`VALUE` judges the mathematical statement. `PRINTED DERIVATION` judges whether Amendment 2 supplies
the needed argument in its stated scope.

| item | VALUE | PRINTED DERIVATION | result |
|---|---|---|---|
| **L1** — schedule-independent minimum-weight collision exclusion | **CONFIRM** | **CONFIRM** | **CLEAN-PASS** |
| **L2** — exact `R_sat = 1` / `infinity` dichotomy | **CONFIRM** | **CONFIRM** | **CLEAN-PASS** |
| **L3** — minimum-weight qualifier on the improper gross hook | **CONFIRM** | **CONFIRM** | **CLEAN-PASS** |
| **I1** — withdraw `(S2)`-only Observation, derive `(S3)`, replace downstream text | **CONFIRM** | **CONFIRM** | **CLEAN-PASS** in the commissioned I1 scope |

The islands dossier nevertheless has one separately registered, still-unapplied wording defect;
see §§7.2 and 8.2. That defect is outside I1 but inside the requested strict “every registered
amendment defect” completion gate.

## 4. L1 — independent derivation and attacks

### 4.1 Complete one-round location inventory

In one memory sector, write `S_a(j)` for the suffix of the X-check `a` after its `j`-th CNOT. The
non-empty residual choices by physical location are:

| location | non-empty residual choices |
|---|---|
| preparation of `anc(a)` | `S_a(0) = supp(a)` |
| idle of `anc(a)` after its `j`-th and before its `(j+1)`-st CNOT | `S_a(j)` |
| data idle on `q` | `{q}` |
| CNOT `q -> b` | `{q}` |
| preparation/idle of `anc(b)` and measurement flips | none |
| CNOT `a -> q_j` | `S_a(j)`, `{q_j}`, `S_a(j-1)` |

An `anc(a)` idle after its last CNOT has empty residual. Empty choices at the displayed CNOTs are
irrelevant to `C_1^eff`. Global X/Z interleaving changes the voltage `u`, but not this residual
inventory: residual propagation depends only on whether `a -> q` is still to come in the local
order. Thus the inventory is schedule-independent for every legal interleaving.

Only an `a -> q_j` CNOT can offer two distinct non-empty residual values at one location. Put

```text
A = S_a(j),    B = {q_j},    C = S_a(j-1).
```

Then `A + B + C = 0` as data vectors. The duplicate/empty edge cases are benign and need no hidden
genericity assumption: if two of `A,B,C` are distinct and nonzero, the third is their nonzero sum,
so all three are distinct and nonzero. Conversely, if one is empty, the other two coincide; if two
coincide, the third is empty. Hence a collision between two *distinct* effective basis residuals
occurs only in the all-distinct, all-nonzero case.

### 4.2 Basis/multiset versus chain semantics

`C_1^eff` is the free `F_2`-space on distinct non-empty residual **values**. It is not the data
space, and it is not a multiset of fault origins. With `[empty] := 0`, define

```text
T := [A] + [B] + [C],      gamma' := gamma + T.
```

Although `T` need not be zero in the free chain space, its underlying data sum is zero. Both
`partial_eff` and `lambda_eff` factor linearly through the underlying data residual, so

```text
partial_eff(gamma') = partial_eff(gamma) = 0,
lambda_eff(gamma')  = lambda_eff(gamma)  != 0.
```

Thus `gamma'` remains an effective logical. If a collision says two triple members are in `gamma`,
toggling deletes those two and adds at most the third; the weight drops by one. If all three are
present, it deletes all three. Either case contradicts minimum weight.

This also proves the exact downstream fact, not merely a value inequality: a repair certificate
contains one representative per distinct basis residual in `gamma`; the argument rules out two of
those residuals being available at one physical location in one round. Representatives in
different rounds are already different circuit locations. Therefore an optimal certificate for a
minimum-weight `gamma` has distinct-location representatives, and Amendment-1 Lemma 5.3'(a) applies.

**L1 verdict:** the value and printed derivation are correct for arbitrary legal interleaving.
Amendment 2 properly distinguishes this from the sibling's non-interleaved representative lemma.

## 5. L2 and L3

### 5.1 L2 — exact saturation dichotomy

Rounds start at `R = 1`. Eventual constancy gives `d_R = d_infty` for `R >= d`, and the frozen
upper bound gives `d_R <= d` for every `R`.

If `d_infty = d`, then `d_d = d`. For `1 <= R < d`, non-increasingness gives
`d_R >= d_d = d`, while the ceiling gives `d_R <= d`; hence `d_R = d`. The same holds for
`R >= d` by constancy. Therefore `d_R = d` for every positive `R`, and the frozen minimum is
exactly `R_sat = 1`, including the boundary case `d = 1`.

If `d_infty < d`, every proposed `R_0` has a later round `R >= max(R_0,d)` with
`d_R = d_infty < d`; no tail is identically `d`, so `R_sat = infinity`. There is no missing third
case because `d_infty > d` is excluded by `d_R <= d`.

For a non-interleaved schedule, Corollary 7.3 supplies `d_R = d_eff` from `R = 1`; substituting
`d_infty = d_eff` makes its `{1,infinity}` statement exactly the specialization of the repaired
general dichotomy. There is no quantifier or endpoint mismatch.

**L2 verdict:** CLEAN-PASS.

### 5.2 L3 — the minimum-weight qualifier is necessary and sufficient

The improper residual `S_a(0) = supp(a)` is an X-stabilizer residual, so its effective syndrome
and logical parity both vanish. Because the effective chain space is free on residual values, its
basis vector can occur in a non-minimal `gamma`: from any effective logical not containing it, add
`[S_a(0)]`; effective syndrome and logical nontriviality are unchanged and the weight increases by
one. This is the advertised counterexample to “never enters a gamma”.

Conversely, if `[S_a(0)]` occurs in a minimum-weight effective logical, deleting it preserves both
defining conditions and lowers weight by one. It therefore never occurs in a **minimum-weight**
effective logical. (If the row/support is empty, it is not a non-empty effective basis residual and
the conclusion is vacuous.)

**L3 verdict:** CLEAN-PASS.

## 6. I1 — realizability, multisets, and downstream scope

### 6.1 Independent derivation of `(S3)`

For an actual weight-4 Island-V list value,
`x = lambda(chi_{P_2})` with `|P_2| = 2`, so the representative `chi_{P_2}` proves `rho(x) <= 2`.
Under the Section 6.1 promise, `d_X >= 4`, and Lemma V.0 says every nonzero element of `Log` has
reduced weight at least `d_X`.

With `Q = Log direct-sum N`, `m(x) = 0` implies `x = beta(x) in Log`. If `x` were nonzero, then
`4 <= d_X <= rho(x) <= 2`, a contradiction. Hence

```text
m(x) = 0  ==>  x = 0  ==>  beta(x) = 0.
```

This is a consequence of actual-code realizability, not of `(S1)` or `(S2)` alone.

### 6.2 Corrected Observation, including multiset and global attacks

Take a three-option **multiset** satisfying `(S1)+(S2)+(S3)`. If two options have the same nonzero
`N`-point `n`, `(S2)` forces the third point to be `0`; `(S3)` forces its label to be `0`; and `(S1)`
forces the two labels at `n` to coincide. The multiset is therefore

```text
{(n,epsilon), (n,epsilon), (0,0)}.
```

It imposes no unary constraint: the single global choice `g(0)=0` hits this list and every other
realizable option at point `0`. If a candidate partial function already assigned a different value
at `0`, normalize it by replacing that assignment with `0`; no hit at point `0` can be lost because
`(S3)` forbids every nonzero label there. Thus the argument is globally compatible, not merely a
per-list escape.

If all three options have one point, `(S2)` gives `n+n+n=n=0`, and `(S3)` makes all labels zero.
Repeated options are essential to the statement and are handled as a multiset throughout.

The old `(S2)`-only Observation is correctly withdrawn: absent `(S3)`, lists at point `0` may pin a
nonzero `g(0)` and then turn the nominal `(0,*)` escape in a two-copy list into a dead option.

### 6.3 Exact replacements and preserved adjudications

The new Amendment-1 §5.4 bullets and §8 item 2 make the correct scoped claims:

* the focused rereview's `(S1)+(S2)` hardness strengthening is explicitly called
  **CONJECTURED**, rather than silently promoted to a theorem;
* neither abstract hardness nor actual-code hardness is inferred for the realizable fragment;
* no polynomial-time result is inferred from `(S3)`; the full realizable fragment remains open;
* the established escapes `(D)` and `k <= 1` remain separate positive results; and
* the repricing is localized to realizability, including `(S3)`, rather than to `(S2)`.

Section 4 of Amendment 2 also preserves the prior adjudications exactly. The Corollary I.1
counterexample is safely decoupled and exposes the missing distance check; it need not be strongly
decoupled. The strong-form record remains “16 witnesses per sector, hence not decoupled”, while the
safe-form record remains “0 safe witnesses per sector, hence safely decoupled”. I1 changes neither
fact and does not use the erroneous old strong-form table row.

**I1 verdict:** CLEAN-PASS in the commissioned I1 scope.

## 7. Completion gates

### 7.1 `CIRCDIST.lift.iff` — CLEAN-PASS

**Was the unchanged dossier already independently reviewed?** Yes, in the necessary scoped sense.
The base iff proof and non-interleaved sibling were independently attacked in
`circdist_lift_proofs_review_20260820.md`; Amendment 1 was then independently rereviewed in
`circdist_amendments_review_20260820.md`. The latter confirmed the Amendment-1 value repairs and
registered exactly L1, L2, and L3 as the remaining amendment defects.

**Does Amendment 2 close every registered Amendment-1 defect for this node?** Yes. L1 supplies the
missing arbitrary-interleaving printed derivation; L2 supplies the exact finite branch; L3 removes
the false non-minimal overclaim. I found no new defect in those replacements.

**Completion verdict:** **CLEAN-PASS**. Under DAG_PROTOCOL rule 5, the assembled dossier licenses
**at most `CERTIFIED*`**, provided the dispatcher links this review with the exact `reviewed_hash`
below and records the scope caveats. It does **not** license `PROVED`: the shared residual-inventory
model caveat remains; the general `repair >= 3` formula and the pre-existing 5.6(d) concern remain
outside this claim/review; and the large proposer scans were not independently reproduced. None of
those may be silently imported as a stronger theorem.

### 7.2 `CIRCDIST.cplx.islands` — FURTHER-REPAIR

**Was the unchanged dossier already independently reviewed?** Yes, with explicit limits. The five
islands write-up was independently attacked in `circdist_islands_review_20260820.md`; Amendment 1
was independently rereviewed in `circdist_amendments_review_20260820.md`. The focused rereview
confirmed B1--B3 and B5, confirmed Proposition V.7' itself at value level, and registered I1 plus a
separate trivial statement-type defect.

**Does Amendment 2 close every registered Amendment-1 defect for this node?** It closes the sole
substantive I1 defect, but **not every registered defect**. The focused rereview also required
Proposition V.7' to say “3-element **multisets** over `N x Log`” rather than “3-element lists
`subset N x Log`”, because (G2)/(G3) use repeated options. Amendment 2 §4 expressly says this note
is outside I1 and does not apply it. The result's intended value is unchanged, but the printed
statement still excludes witnesses used by its own proof.

**Completion verdict:** **FURTHER-REPAIR**, not REFUTE. Exact remaining wall: append a one-line
governing correction to Amendment-1 Proposition V.7' replacing the set/list formulation by
“3-element multisets over `N x Log`, with repetitions allowed”; propagate the same convention to
any direct quotation of that proposition. No new reduction or computation is needed.

Under the strict every-registered-defect gate, the current assembled dossier **does not yet license
a completion promotion**. After that one-line repair and its binding review, the exact current node
claim would license **at most `CERTIFIED*`**, not `PROVED`, with at least these caveats: Lemma 1.4's
`d_ext`/mechanism bridge remains NOT-REVIEWED; the Definition-2.2 multiset-to-value-set gloss is only
harmless under the now-certified promise; the Courcelle/ALS claims are secondary-source verified
but still lack the registered primary-text check; and no general Island-V tractability or
realizable-CSS hardness theorem is established.

## 8. Exact current claims and `reviewed_hash`

The repository checker convention is
`sha256(claim.replace("\r\n","\n").strip().encode("utf-8"))`, prefixed by `sha256:`.

### 8.1 `CIRCDIST.lift.iff`

Exact current YAML-parsed claim:

> In graph-like detector error models with fixed boundaries, d_circ equals the minimum over
> nontrivial effective logicals gamma of the length of the shortest closed spacetime lift of gamma,
> with an intrinsic zero-voltage/monodromy condition characterizing same-weight liftability — and
> the voltage is computable without constructing the full multi-round circuit (non-vacuity bar).

```text
reviewed_hash: sha256:c3a841984a07038dfbe3390f0b25cca633d04877ff92fb04bd0e3eaf480f0061
```

### 8.2 `CIRCDIST.cplx.islands`

Exact current YAML-parsed claim:

> Nontrivial restricted classes of Eff-Preserve are in P (or FPT) with proven correctness —
> including factorising instances (no inter-check coupling; self-certifying), HGP codes (every
> schedule preserves d_eff >= min(mu_X, mu_Z), so constant YES under the non-degeneracy proviso),
> bounded-treewidth Tanner graphs (CMSO2/Courcelle FPT), d = 3 with two allowed orders per check
> (2-SAT, no check-weight bound), and the k <= 1 weight-<=4 regime (unconditional YES).

```text
reviewed_hash: sha256:b4325b447807dc93f9e5f96ab503cc96800dab3e3b5b8e70e0378601121d0590
```

The second hash records the exact claim reviewed; it is **not** a recommendation to attach this
review as a completion-level clean pass until §7.2's remaining wall is repaired.

## 9. Limitations / NOT-REVIEWED

1. The general `repair >= 3` lift formula, the proposed min-cost-covering extension, the large
   `321059/321059` symmetry, and the large proposer scans were not reviewed or rerun.
2. The pre-existing concern about the hypothesis/use in lift 5.6(d) was not reopened; it is not a
   premise of the exact current `lift.iff` claim reviewed here.
3. No general formula for `d_infty` was sought. L2 uses only its relation to the eventually
   constant tail.
4. The focused rereview's full `(S1)+(S2)` NP-hardness reduction was not independently promoted
   beyond its stated **CONJECTURED** status. I checked that Amendment 2 reports it with that status
   and that `(S3)` blocks its zero-point unary-forcing mechanism.
5. Whether `(S1)+(S2)+(S3)` is in P, whether `(S3)` captures all realizability restrictions, and
   whether realizable CSS instances are hard remain open.
6. Lemma 1.4's modelling bridge, the K4 imported data, three unrecomputed census families, the
   Island-V general case, and primary-text verification of the Courcelle/ALS citations were not
   completed here.
7. I did not audit unrelated Proof-DAG nodes, scheduler state, generated views, or canonical event
   histories beyond reading the two current node claims and their pending-review summaries.

No item outside this scope should be inferred to have passed merely because L1/L2/L3/I1 passed.
