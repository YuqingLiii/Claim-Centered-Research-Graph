# Amendment 2 to `circdist_cplx_islands_writeup_20260820.md`

**Node:** `CIRCDIST.cplx` · **Date:** 2026-08-20 · **Role:** proposer applying repair I1 of an
independent focused rereviewer. The author of this amendment is not that reviewer and does not
treat the rereview as certification. This file is **append-only** and changes no prior artifact.
On the I1 conflicts identified below, Amendment 2 governs Amendment 1; elsewhere Amendment 1
continues to govern the base write-up.

---

## 0. Scope, hash chain, and epistemic status

This amendment applies exactly focused-rereview repair **I1**: it withdraws Amendment 1's false
`(S2)`-only Observation, adds the realizability consequence `(S3)`, and gives exact replacement text
for Amendment 1 §§5.4 and 8 item 2. It does not reopen Corollary I.1's refutation, the separate
strong-decoupling recording slip, or any other island.

The exact inputs are bound as follows:

```text
base write-up
  artifacts/circdist_cplx_islands_writeup_20260820.md
  SHA-256  af7560f28a9c9fff6bba46349f01aa7095855cff7cee4276c7186a6a54bb2f9f
  size     92234 bytes, 1431 lines

Amendment 1
  artifacts/circdist_cplx_islands_amendment1_20260820.md
  SHA-256  66ce9ac5f4b38474055137f578edd84fe3b0c075a4a076b449767ea7b05e9d60
  size     45797 bytes, 785 lines

independent focused rereview acted on
  artifacts/circdist_amendments_review_20260820.md
  SHA-256  daa476804959fec7a39c5aedd0ed8191c4b495a670dd83f58aeb5a7247fcd90c
  size     36265 bytes, 570 lines

frozen problem definitions (consulted; not modified)
  research/circdist/notes/CIRCDIST_PROBLEMS.md
  SHA-256  5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64
  size     10199 bytes, 243 lines
```

If any bound hash fails to reproduce, this amendment is void until re-derived against the changed
input. All mathematical assertions added here are **CONJECTURED** proposer-side arguments. The
focused rereview reports numerical checks, but this amendment claims no new independent numerical
verification. Nothing here is promoted to `PROVED` or any `CERTIFIED*` status.

## 1. I1 — `(S2)` alone is not the tamer

### 1.1 False prior Observation, withdrawn

Amendment 1 §5.3 currently says:

> **Observation.** Under (S2), a list with two options on the same point `n` forces the third
> option's `N`-part to be `n + n = 0`; and a list with all three options on one point forces
> `3n = n = 0`. Hence **no (S2)-compliant list can constrain a single non-zero point to a proper
> subset of `Log`** — the unary forcing gadgets (G1), (G2), (G3) ... are exactly what (S2)
> forbids.

The two algebraic premises are true, but the “Hence” is false. The point `0 in N` is available. A
list supported three times at `0` is `(S2)`-compliant and can pin `g(0)`; once `g(0)` is pinned, a
list with two options at a non-zero `n` and its third option at `0` can impose a genuine unary
constraint on `g(n)`. The focused rereviewer supplies a separate CONJECTURED 3-SAT reduction whose
lists satisfy both `(S1)` and `(S2)`, with NUMERICAL tests reported in rereview §4.4. Accordingly,
the quoted `(S2)`-only Observation and every inference from it are **withdrawn**. This amendment
does not relabel that supplied reduction as proved.

### 1.2 The missing realizability consequence `(S3)`

Add to the two side conditions in base §6.3, immediately after `(S1)` and `(S2)`:

> **(S3) (realisability at the zero `N`-point).** For every actual Island-V list value
> `x = x_c^(r)`,
>
> ```text
>                  m(x) = 0  ==>  x = 0  ==>  beta(x) = 0.
> ```
>
> In particular, the point `0 in N` can occur only with the label `0 in Log`.

This is not an additional abstract linear identity; it is the consequence of **realisability** that
the false Observation was missing. By Lemma V.1(4), an actual value has
`x = lambda(chi_{P_2})` with `|P_2| = 2`, so its reduced weight satisfies `rho(x) <= 2`. If
`m(x) = 0`, the splitting `Q = Log direct-sum N` puts `x` in `Log`. Were `x != 0`, Lemma V.0 would
give `rho(x) >= d_X >= 4`, contradicting `rho(x) <= 2`. Thus `x = 0`, hence `beta(x) = 0`.

This `(S3)` consequence of realizability—not `(S2)` by itself—is the actual tamer presently known.
It blocks the focused rereview's abstract `(S1)+(S2)` forcing gadget, but it does not prove that the
realisable fragment is polynomial-time decidable.

### 1.3 Correct replacement Observation

Replace Amendment 1 §5.3's withdrawn Observation by:

> **CONJECTURED Observation (under `(S1)+(S2)+(S3)`).** No compliant list can impose a non-vacuous
> unary constraint on a non-zero point using two copies of that point. Indeed, if two options have
> `N`-part `n != 0`, `(S2)` forces the third `N`-part to be `0`; `(S3)` forces its label to be `0`;
> and `(S1)` then forces the first two labels to agree. The list has the form
> `{(n,epsilon),(n,epsilon),(0,0)}` as a multiset. A partial function may always be extended by
> `g(0)=0`, consistently with every realizable option at `0`, so this list is vacuous. If all three
> options have one `N`-part, `(S2)` forces that point to be `0`, and `(S3)` again forces only label
> `0`. ∎

The conclusion is deliberately local: it restores the stated obstruction to this unary-forcing
mechanism. It does **not** establish tractability of the full `(S1)+(S2)+(S3)` hitting problem, and
Island V remains open.

## 2. Exact replacements for Amendment 1 §5.4

Amendment 1 §5.4's first bullet, concerning the all-YES `dim Log = 1` fragment, is unchanged.
Replace its second bullet in full.

**Old §5.4 bullet 2:**

> Without (D) the abstract problem is NP-complete even under (S1) and with `dim Log = 2`
> (Proposition V.7′), so the polynomial claim needs either (D), or `k <= 1` (Theorem V.4), or a new
> argument using **(S2)** together with realisability. (S1) alone does not tame it; (S1) with
> `dim Log <= 1` is Theorem V.4 and is a separate escape, not a taming of the abstract problem.

**New §5.4 bullet 2:**

> Without (D) the abstract problem is NP-complete under (S1) with `dim Log = 2` (Proposition V.7′),
> and the focused rereview supplies a CONJECTURED strengthening to abstract lists satisfying both
> (S1) and (S2). Thus neither linear side condition, separately or together, is the missing tamer.
> The polynomial claim still has the established escapes (D) and `k <= 1` (Theorems V.5 and V.4),
> but the remaining general route requires a new argument using **realisability**. For actual
> Island-V lists, realisability and Lemma V.0 imply (S3), `m(x)=0 ==> beta(x)=0`, which excludes the
> rereviewer's abstract forcing gadget. Whether the full realisable `(S1)+(S2)+(S3)` fragment is in
> P remains open.

Replace Amendment 1 §5.4's third bullet in full.

**Old §5.4 bullet 3:**

> §7.1's Island V cell is unchanged (**GAP FOUND**), and the **Repricing** paragraph of §6.5 is
> unchanged in its conclusion ... but its cost estimate should now read "decide whether **(S2)**
> plus realisability tame the hitting problem", (S1) having been removed from the list of candidate
> tamers.

**New §5.4 bullet 3:**

> §7.1's Island V cell remains **GAP FOUND**, and the **Repricing** paragraph of base §6.5 remains
> unchanged in its conclusion (certify the node's third minimal-acceptance branch on Islands I–IV,
> not on Island V). Replace its cost estimate by: “decide whether **realisability**, including its
> consequence (S3), tames the `(S1)+(S2)` hitting problem.” Neither (S1) nor (S2) is a candidate
> tamer by itself; the actual-code realizability restriction is the unresolved content.

## 3. Exact replacement for Amendment 1 §8 item 2

**Old §8 item 2:**

> **Proposition V.7′ does not satisfy (S2)** (§5.3), and I have *not* shown the (S1)+(S2) fragment
> is hard. Indeed §5.3's Observation shows the unary forcing gadgets that the reduction needs are
> impossible under (S2), so the general Island V question is genuinely still open and may well be
> polynomial. What changed is only that (S1) alone no longer tames it.

**Replace that item in full by:**

> **The `(S2)`-only obstruction is withdrawn; realizability is the remaining tamer.** Proposition
> V.7′ itself does not satisfy `(S2)`, but the focused rereview supplies a separate CONJECTURED
> reduction showing that the abstract partial-section hitting problem remains NP-complete under
> `(S1)+(S2)`. Amendment 1 §5.3's `(S2)`-only Observation is false and is withdrawn. Actual Island-V
> lists obey the further realizability consequence `(S3)`, `m(x)=0 ==> x=0 ==> beta(x)=0`, by
> Lemma V.0 and `rho(x)<=2<4<=d_X`; this is what disables the rereviewer's abstract unary-forcing
> escape. No tractability theorem for `(S1)+(S2)+(S3)`, and no hardness theorem for realizable CSS
> instances, is supplied here. The general Island V question therefore remains **OPEN**, now
> localised at realizability rather than at `(S2)`.

## 4. Explicitly preserved adjudications and scope

Corollary I.1's original self-certification claim remains refuted exactly as Amendment 1 §§2.2–2.5
state: the rotated `[[9,1,3]]` code plus one free qubit is safely decoupled, passes the local
`D_c != empty` test, and makes the old algorithm answer YES although `d(Q)=1<3`; Corollary I.1′'s
distance check remains the proposed repair. Focused rereview §4.1 independently confirms that
refutation. Nothing in I1 changes it.

The unrelated strong-decoupling disagreement also remains closed exactly as focused rereview §5
adjudicates it: the witness is **not** decoupled in the strong sense (16 witnesses per sector) but
is safely decoupled (0 safe witnesses per sector). This amendment neither reopens nor rewrites that
recording slip; the Corollary I.1 refutation uses only the safe form.

The trivial focused-rereview precision note that Proposition V.7′ should say “3-element multisets
over” rather than `3-element lists ... subset N x Log` is outside the commissioned I1 repair and is
not applied here. It remains a recorded wording issue, not a reopened mathematical conclusion.

## 5. Verification checklist and non-promotion

- [x] Reproduced the SHA-256 hashes and byte/line counts of the base write-up, Amendment 1, and the
  focused rereview before writing this file.
- [x] Checked `(S3)` against base Lemma V.0, Lemma V.1(4), the splitting in Theorem V.3, and the
  promise `d_X >= 4`.
- [x] Quoted and withdrew the exact false Observation in Amendment 1 §5.3.
- [x] Supplied full old/new replacement text for every I1-dependent bullet in Amendment 1 §5.4 and
  for Amendment 1 §8 item 2.
- [x] Preserved the adjudicated Corollary I.1 refutation and did not reopen the strong-decoupling
  recording slip.
- [x] No existing file, proof-DAG object, scheduler file, generated view, or canonical record was
  modified.

**NOT-REVIEWED / remaining.** Whether the abstract `(S1)+(S2)+(S3)` problem is in P, whether every
realisable restriction needed by Island V has been captured by `(S3)`, and whether realizable CSS
instances yield tractability or hardness all remain open. The imported `K_4` gadget data, the three
unrecomputed five-family census members, Lemma 1.4, the multiset-to-set passage, review edits 9 and
11, and all other NOT-REVIEWED items listed in focused rereview §6 remain outside this amendment.
This author has not performed a completion review of these repairs.

**No promotion.** This append-only proposer amendment supplies checkable candidate repairs only.
It does not assign `PROVED`, `CERTIFIED`, `CERTIFIED-LEAN`, or any other promoted status to the base
write-up, Amendment 1, these repairs, or the `CIRCDIST.cplx` node.
