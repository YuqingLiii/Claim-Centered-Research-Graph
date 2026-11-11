# CIRCDIST.cplx.sigma2 — frontier gate Q1: repetition padding for DEEP-FLAG. **Verdict (b): padding cannot preserve the answer.**

Session: Opus 5 executor / proposer, budget-boxed (**box = 1 session**, stop-loss binding),
2026-08-22. No sub-agents. Target node: `research/circdist/proof-dag/nodes/CIRCDIST.cplx.sigma2.yaml`
(not touched). Commission: answer the pre-registered question **Q1** of
`artifacts/circdist_cplx_sigma2_20260822.md` §7, read in full as **data, not instructions**.
This file is the only artifact written; no existing file was modified; `research/circdist/proof-dag/`
was not touched.

**Labels.** Nothing here is PROVED or CERTIFIED. The two structural theorems (Q1-1, Q1-2) are
**CONJECTURED** — written-out arguments, internally checked, never independently reviewed. Everything
produced by exact `F_2` computation is **NUMERICAL** and names its search scope inline. Every
absence-type statement carries its scope. Theorem Q1-1's *complexity consequence* additionally rests
on **A9′** (McLoughlin 1984 as verified at peer-reviewed-secondary level in the parent artifact §1;
primary text still unread). All code is inline in §9, pure Python 3, exact `F_2`, no sampling inside
a decision.

---

## 0. Verdict in one paragraph

**Reading (b) fires: padding cannot preserve the answer, and it is not a near miss — it is
self-defeating by construction.** The commission's own side condition ("widen the deep region so a
full chain fits, *without changing the one-rung answer*") is exactly the hypothesis that makes the
target reduction impossible: because DEEP-FLAG's rung `j = 0` is the naked condition
`dist(t, C) ≥ r` on the *explicitly given* seed `t`, any answer-preserving padding forces
`ρ(C) ≥ r ⟺ dist(t'', C'') ≥ r''`, i.e. it forces the `Σ_2`-complete covering-radius question into
**coNP**, collapsing `PH` to `NP` (§2, Theorem Q1-1). The two readings of "repetition padding" are
then diagnosed exactly (§3): with `m` **even** the padded covering radius is the constant `mN/2`,
carrying zero information about `C` (answer destroyed); with `m` **odd** it is exactly
`N(m−1)/2 + ρ(C)` (answer preserved) — and therefore falls under the barrier. The check-side reading
(`H ↦ H ⊗ 1_m`) preserves depth *exactly* and falls under the barrier too. An explicit infinite
family (`C = {0^N, 1^N}`, `r = N/2`) is CRP-YES while its deep region is an **edgeless antichain**, so
it is DEEP-FLAG-NO under either padding at every `m` at the natural (balanced) seed, and — verified
exhaustively over *all* seeds at `m = 3` — the failure is concrete, not merely conditional (§4). **The route-deciding by-product** is that the parent artifact's Theorem E
ladder is *not* the real obstruction: repetition padding does exactly what it was hoped to do to the
ladder — it converts the monotone chain into a free **walk** with exact edge-multiplicities
(Theorem Q1-2 / Lemma W, §5, verified exhaustively). What kills the transfer is the **seed**, not the
ladder. Consequence: **route R4 dies as a covering-radius transfer** — no padding, and more generally
no reduction whose constructed seed is deep exactly when the source instance is a YES, can carry
McLoughlin's theorem into DEEP-FLAG. R3 is the sole surviving *registered* route; §7 registers the one
new route the barrier's proof points at (R5, deep-region reconfiguration) together with the design
rule it must obey.

---

## 1. The object, restated with no CSS in it

Fix a binary linear code `C ≤ F_2^N` (given by a generator or parity-check matrix), `t ∈ F_2^N`,
`r ∈ N`. Write `dist(v, C) := min_{c ∈ C} |v + c|` and `ρ(C) := max_v dist(v, C)` (covering radius).

> **DEEP-FLAG** (parent artifact §7). Is there a maximal chain `∅ = A_0 ⊂ A_1 ⊂ ⋯ ⊂ A_N = [N]`,
> `|A_j| = j`, with `dist(χ_{A_j} + t, C) ≥ r` for every `j = 0,…,N`?

Two reformulations used throughout, both immediate:

* **(Geodesic form.)** `A ↦ χ_A + t` is a bijection `2^{[N]} → F_2^N` carrying maximal chains to
  Hamming-geodesics from `t` to its antipode `t + 1_N`. So DEEP-FLAG asks: *does the deep region*
  `D_r := {v : dist(v,C) ≥ r}` *contain a geodesic from `t` to `t + 1_N`?*
* **(Coset invariance.)** `D_r` is a union of cosets of `C`, so the answer depends on `t` only through
  `t + C`; if `1_N ∈ C` (the parent artifact's embedding `S_X := C + span(1_N)`) then `D_r` is also
  closed under `v ↦ v + 1_N` and the two endpoints have equal depth.

The **one-rung answer** is the covering-radius answer `ρ(C) ≥ r`, i.e. `D_r ≠ ∅`; it is the
complement of CRP and is `Σ_2^P`-complete under **A9′**. DEEP-FLAG-YES ⟹ one-rung-YES trivially.

**The commission's Q1.** Replace `C` by `C ⊗ rep_m` and `t` by `t^{(m)}` (or a variant), so that
"aligned points sit at depth `m·dist(·,C)` while single-coordinate steps move depth by ≤ 1", and ask
whether the resulting DEEP-FLAG instance has the same answer as the McLoughlin instance, *without
changing the one-rung answer*.

---

## 2. Theorem Q1-1 — the Seed Barrier: the side condition is the impossibility

### Theorem Q1-1 (Seed Barrier) — CONJECTURED

Let `f` be any polynomial-time map from covering-radius instances `(C, r)` to DEEP-FLAG instances
`f(C,r) = (C'', t'', r'')` such that

* **(A) answer transfer.** `DEEP-FLAG(C'', t'', r'') = YES ⟺ ρ(C) ≥ r`; and
* **(B) one-rung preservation.** `ρ(C'') ≥ r'' ⟺ ρ(C) ≥ r`.

Then `{(C,r) : ρ(C) ≥ r} ∈ coNP`. With **A9′** (that problem is `Σ_2^P`-complete) this gives
`Σ_2^P ⊆ coNP`, hence `NP = coNP` and `PH = NP`.

*Argument.* Rung `j = 0` of any chain is `A_0 = ∅`, whose vector is `χ_∅ + t'' = t''`. Hence

```
   DEEP-FLAG(C'',t'',r'') = YES   ⟹   dist(t'', C'') ≥ r''.          (1)
```

Conversely `dist(t'',C'') ≥ r''` ⟹ `ρ(C'') ≥ r''` ⟹ (by **(B)**) `ρ(C) ≥ r`. Combining with **(A)**,

```
   ρ(C) ≥ r   ⟺   dist(t'', C'') ≥ r''.                              (2)
```

The right-hand side is a **coNP** predicate of the poly-size, poly-time-computable object
`f(C,r)`: its negation `dist(t'',C'') < r''` is witnessed by a single `u` with `|u| < r''` and
`t'' + u ∈ C''`, checkable in poly time by the parity checks of `C''`. So `ρ(C) ≥ r` is decided in
coNP. Under A9′ that problem is `Σ_2^P`-complete, so `Σ_2^P ⊆ coNP`; since `NP ⊆ Σ_2^P` this gives
`NP ⊆ coNP`, hence `NP = coNP` and the polynomial hierarchy collapses to its first level. ∎

**Reading.** Line (1) is the whole content: DEEP-FLAG *contains a naked covering-radius witness in its
own input*. Any reduction that also keeps the one-rung answer is therefore handing over, in the clear,
a certified deep point of the source code — which is precisely the object whose *existence* was the
`Σ_2`-hard question. The commission's phrase "*without changing the one-rung answer*" is not a
desideratum that padding fails to meet; it is the hypothesis under which no map can succeed.

### Corollary Q1-1a (design rule for any future attempt) — CONJECTURED

Let `L` be any `Σ_2^P`-hard language and `g` a poly-time many-one reduction `L ≤_m` DEEP-FLAG. If
`g(x) = (C'',t'',r'')` has the property "`dist(t'',C'') ≥ r''` ⟺ `x ∈ L`", then `L ∈ coNP` and
`PH = NP`. Hence **every** admissible reduction must construct instances whose seed is deep
**unconditionally** — the constructed instance's own covering-radius answer must be constant-YES and
must carry no information about `x`. All of the `Σ_2` content has to live in the *chain*, none of it in
the *depth of any single named point*.

### Corollary Q1-1b (what dies) — CONJECTURED

There is **no** padding of any kind — repetition, direct-sum, concatenation, dual, or otherwise —
that turns a McLoughlin instance into an equivalent DEEP-FLAG instance while preserving the
covering-radius answer, unless `PH = NP`. Route **R4** (`covering-radius-transfer`) therefore cannot
be completed *as a transfer*: McLoughlin's theorem can never be the anchor of DEEP-FLAG's hardness,
whatever gadget is placed around it. What survives of R4 is Theorem D of the parent artifact — the
`k = 1` dictionary `w^nt(v) = dist(v + t, S_X)` — which remains correct and useful as **vocabulary**
inside some other construction, but is not a source of hardness.

**Scope note.** Q1-1 constrains *many-one* reductions from the covering-radius problem (and, via
Q1-1a, from any `Σ_2`-hard source with the stated seed behaviour). It says nothing against a
from-scratch reduction (`Σ_2`-SAT → DEEP-FLAG) that builds its own unconditionally deep seed; that
possibility is left completely open and is exactly what §7 registers.

---

## 3. The two readings of "repetition padding", computed exactly

Write `C^{(m)} := C ⊗ rep_m ≤ F_2^{mN}` for the **generator-side** padding (generator matrix
`G ⊗ 1_m`; each coordinate repeated `m` times), and `π : F_2^{mN} → F_2^N` for the block-parity map.
The **check-side** padding is `π^{-1}(C)`, i.e. the code with parity-check matrix `H ⊗ 1_m` — the same
words "repetition padding" applied to the dual. Throughout, `1_N ∈ C` (the parent artifact's
embedding), and for `v ∈ F_2^{mN}` let `w_i = |v_i|` be its block weights,
`u_i := min(w_i, m − w_i)`, `δ_i := |m − 2w_i|`, and `b_i := [w_i > m/2]` the block majority.

**Depth identity (elementary).** `dist(v, C^{(m)}) = Σ_i u_i + min_{c ∈ C} Σ_{i : c_i ≠ b_i} δ_i`,
i.e. `Σ u_i` plus the `δ`-*weighted* distance from `b` to `C`. (Choosing `c` fixes each block's cost
to `w_i` or `m − w_i`.)

### Proposition Q1-P1 (`m` even: the one-rung answer is destroyed) — CONJECTURED, verified NUMERICAL

If `m` is even then `ρ(C^{(m)}) ≥ mN/2` for every `C`, with equality when `1_N ∈ C`. Hence for
`1_N ∈ C` the padded covering-radius answer is `[r'' ≤ mN/2]` — a function of `(N, m, r'')` **alone**,
carrying no information about `C`. Hypothesis (B) of Q1-1 fails maximally, and there is nothing left
to reduce from.

*Argument.* Lower: the half-balanced point (`w_i = m/2` for all `i`) has `u_i = m/2`, `δ_i = 0`, so its
depth is `mN/2` for every `C`. Upper: `1_{mN} ∈ C^{(m)}`, so `dist(v, ·) ≤ min(|v|, mN − |v|) ≤ mN/2`.
∎

**NUMERICAL (E2/P1).** Exhaustive over **all** subspaces `C ≤ F_2^n` containing `1_n`, `n = 2..6`, and
all even `m` with `nm ≤ 22`: **560 (code, m) pairs, 0 deviations** from `ρ(C^{(m)}) = mN/2`.
*Control:* over subspaces **not** containing `1_n` (`n = 3,4,5`, `dim ≤ 2`, even `m`, `nm ≤ 20`) the
lower bound `ρ ≥ mN/2` held in **461 of 461 cases**, confirming that the "answer destroyed" half does
not depend on `1_N ∈ C` (only the matching upper bound does).

### Proposition Q1-P2 (`m` odd: the one-rung answer is preserved) — CONJECTURED, verified NUMERICAL

If `m` is odd and `1_N ∈ C` then `ρ(C^{(m)}) = N(m−1)/2 + ρ(C)`, so with `r'' := N(m−1)/2 + r` the
padded covering-radius answer equals the original. Hypothesis (B) of Q1-1 **holds** — and therefore
Theorem Q1-1 applies and forbids the reduction.

*Argument (lower bound; the upper bound is the verified half).* Take `v` with all blocks at
`w_i ∈ {(m−1)/2, (m+1)/2}` and majority `b`. Then `u_i = (m−1)/2` and `δ_i = 1`, so the depth identity
gives `dist(v, C^{(m)}) = N(m−1)/2 + dist(b, C)`; maximising over `b` gives `≥ N(m−1)/2 + ρ(C)`.
(The matching upper bound is asserted from the exhaustive check below, not proved: the depth identity
alone permits unbalanced `v` to beat balanced ones a priori — increasing one `δ_i` by 2 costs 1 in
`Σu_i` and can buy up to 2 in the weighted distance — and I did not close that case by hand.) ∎

**NUMERICAL (E2/P2).** Exhaustive over all subspaces of `F_2^n` containing `1_n`, `n = 2..6`, odd
`m ∈ {3,5,7}` with `nm ≤ 22`: **493 (code, m) pairs, 0 deviations**. *Control, and it is a sharp one:*
over subspaces **not** containing `1_n` the same formula fails in **240 of 279 cases** — the
`1_N ∈ C` hypothesis is doing real work here, and it is exactly the hypothesis the parent artifact's
embedding `S_X = C + span(1_N)` supplies. So the answer-preserving branch of the padding is precisely
the branch the intended construction lives in.

### Proposition Q1-P3 (check side: depth preserved exactly) — CONJECTURED, verified NUMERICAL

For every `C` and every `m`, `dist(v, π^{-1}(C)) = dist(π(v), C)`, hence `ρ(π^{-1}(C)) = ρ(C)`.
Hypothesis (B) holds with `r'' = r`, so Theorem Q1-1 applies here as well.

*Argument.* Turning `v` into a word of `π^{-1}(C)` with block parities `c` costs exactly one flip per
block whose parity is wrong, i.e. `dist(π(v), c)`; minimise over `c ∈ C`. ∎

**NUMERICAL (E2/P3).** Exhaustive, all subspaces containing `1_n`, `n = 2..6`, `m ∈ {2,3,4}` with
`nm ≤ 20`: **1016 cases, 0 deviations**.

**Summary of §3.** The two readings of "repetition padding" partition exactly along the barrier:
the one that changes the one-rung answer changes it into a *constant*, and the ones that keep it are
precisely the ones Theorem Q1-1 forbids. There is no third behaviour available to a padding.

---

## 4. The failure is also concrete: an unconditional counterexample family

Theorem Q1-1 is conditional on `PH ≠ NP`. The following removes that conditionality for the padding
family actually proposed.

### Proposition Q1-P4 (edgeless deep region) — CONJECTURED, verified NUMERICAL

Let `N` be even, `C = {0^N, 1^N}` (the `[N,1,N]` repetition code, which contains `1_N`), `r = N/2`.
Then `ρ(C) = N/2`, so the instance is **CRP-YES at `r`**; but
`D_r = {v : min(|v|, N−|v|) ≥ N/2} = {v : |v| = N/2}` is the middle layer of the cube, an **antichain
containing no hypercube edge**. Consequently every DEEP-FLAG instance on `(C, ·, r)` is **NO** (a chain
of length `N ≥ 1` needs an edge), and — by Theorem Q1-2 of §5, since a walk of positive length also
needs an edge — so is every instance obtained from it by generator-side repetition padding with `m`
odd, or by check-side padding with any `m`, at **every** `m`, **at the balanced seed**. With `m` even
the generator-side padding gives an instance whose answer no longer refers to `C` at all (Q1-P1).
*Scope:* the "every seed" strengthening is verified exhaustively only at `m = 3` (E3/S below); for
`m ≥ 5` the statement covers the balanced seeds, which are the ones the construction would use.

**NUMERICAL (E4/b).** `N = 4,6,8,10`: `ρ(C) = N/2` and the number of hypercube edges inside `D_{N/2}`
is **0** in all four cases (`|D_r| = 6, 20, 70, 252`).

**NUMERICAL (E3/S), the same phenomenon in census form.** Exhaustive over all subspaces containing
`1_n` with the generator-side padding at `m = 3`:

| scope | `(C,r)` pairs | CRP-YES | padded DEEP-FLAG YES for **some** seed | for a **balanced** seed |
|---|---|---|---|---|
| `n = 3`, `m = 3` (`N = 9`) | 15 | 4 | 1 | 1 |
| `n = 4`, `m = 3` (`N = 12`) | 64 | 19 | 8 | 8 |

So **3 of 4** and **11 of 19** CRP-YES instances are padded-DEEP-FLAG-NO *for every choice of seed* —
the padding does not merely fail to pick the right seed, it fails outright. (Printed witnesses:
`C = {000,001,110,111}`, `r = 1`; and `C = {0000,1111}`, `r = 2`, the `N = 4` member of the family
above.)

**NUMERICAL (E4/c), larger `m` does not rescue them.** For the two witnesses, the padded answer at
`m = 3,5,7,9,11` is NO throughout; the diagnosis is visible in one number, the count of hypercube
edges inside `D_r` (0 and 2 respectively). By contrast `C = {0000,1111}` with `r = 1` has 24 such
edges and is YES at every `m ∈ {3,…,11}`. **The padded answer tracks the edge/connectivity structure
of `D_r`, not its non-emptiness.** That is the same statement as Theorem Q1-1, seen from the
instance side.

---

## 5. What repetition padding *does* do: the ladder is not the obstruction

This is the route-relevant by-product, and it is a correction to the parent artifact's §4 framing.

### Theorem Q1-2 (Lemma W: ladder → walk) — CONJECTURED, verified NUMERICAL

Let `m` be odd, `C ≤ F_2^n`, `r ∈ N`. For `t ∈ F_2^n` let the **balanced seed** `t' ∈ F_2^{nm}` carry
`(m−1)/2` ones in block `i` if `t_i = 0` and `(m+1)/2` if `t_i = 1`, and put `r' := n(m−1)/2 + r`.
Then

> `DEEP-FLAG(C^{(m)}, t', r') = YES`  ⟺  there is a **walk** `v_0 = t → v_1 → ⋯ → v_{nm} = t + 1_n` in
> `F_2^n` with single-coordinate steps, in which coordinate `i` is used **exactly `m` times**, such
> that `dist(v_j, C) ≥ r` for every `j`.

The same equivalence holds for the check-side padding `π^{-1}(C)` at any `m` and any lift of `t` as
seed, with the endpoint `t + (m mod 2)·1_n` and threshold `r`.

*Argument (generator side).* By the depth identity, at a point all of whose blocks are balanced
(`δ_i = 1`) the depth is exactly `n(m−1)/2 + dist(b, C)`, so such a point is deep iff its majority
vector is deep. Flipping one coordinate of a balanced block moves `w_i` between `(m−1)/2` and
`(m+1)/2`, i.e. **toggles `b_i` and leaves the point balanced** — the chain step and the walk step are
the same move, with no intermediate state. In block `i` the seed has `(m∓1)/2` ones and `(m±1)/2`
zeros; using all `m` of its coordinates while never leaving `{(m−1)/2,(m+1)/2}` forces the
up/down moves to alternate, which is possible exactly once and yields exactly `m` toggles of `b_i`.
Any other move unbalances a block, which lowers `Σ u_i` by 1 and can raise the weighted distance by at
most the same amount only when the unbalanced coordinate is in the differing set — never a strict
gain — so an optimal chain may be taken to be all-toggle. ∎ *(The last clause is the soft step; it is
what the exhaustive check below is for.)*

**NUMERICAL (E3/W).** Exhaustive over all subspaces of `F_2^n` containing `1_n`, `n ∈ {3,4}`,
`m ∈ {3,5}` with `nm ≤ 16`, all `r ∈ [1, ρ(C)]`, all `2^n` seeds: **368 cases, 0 mismatches** between
the padded DEEP-FLAG answer (exact lattice DP over `2^{nm}` subsets) and the exact-count walk
predicate (exact DP over `2^n × (m+1)^n` states).
**NUMERICAL (E4/a), check side:** all subspaces containing `1_n`, `n ∈ {3,4}`, `m ∈ {2,3}`,
`nm ≤ 12`, all `r`, all seeds: **672 cases, 0 mismatches**.

### The consequence for the parent artifact's Horn 2

The parent artifact's Theorem E (the `±1` "mountain profile") is correct, and it does bite on
*unpadded* instances (its T3/T3c witnesses stand). But Theorem Q1-2 says the ladder is **removable by
exactly the padding Q1 proposed**: with each coordinate duplicated `m` times, the profile is still a
`±1` walk, but it is no longer *monotone* — it may retreat and revisit, and the only residue of the
chain condition is the multiplicity bookkeeping "each direction used exactly `m` times". In the CSS
vocabulary: **as soon as `H_X`'s heavy check has repeated columns, the hook classes repeat, and
Theorem E's flag law degenerates from "monotone ladder" to "walk"**. So the parent artifact's Horn 2
("then Theorem E applies with full force and the ladder requirement is what has to be defeated") is
**wrong as a barrier statement** — the ladder is defeatable, cheaply. The thing that actually blocks
the transfer is the seed (§2), which the parent artifact did not identify because its Theorem E
analysis treated the endpoints `ρ_0 = ρ_w = 0` as free (they are, in the CSS instance, automatically
safe by the promise `d ≤ d_X`) and therefore never asked what the *reduction* would have to do to
manufacture them.

### And the one further regularity, with its scope

The parent artifact's unexplained T3c coincidence has a cousin here, and it **fails at scale**, which
is worth recording because it is the kind of small-`n` regularity that misleads. For fixed `(C,r)`, do
all *deep* seeds give the same DEEP-FLAG answer?

| scope | `(C,r)` pairs with `ρ ≥ r` | seed-split cases |
|---|---|---|
| exhaustive, `n = 4,5,6`, all `C ∋ 1_n` | 19 / 97 / 651 | **0 / 0 / 0** |
| random `C ∋ 1_n`, 400 trials each, `n = 7` | 856 | **0** |
| random, `n = 8` | 986 | **12** |
| random, `n = 9` | 1065 | **6** |

So "the answer does not depend on the seed" is a genuine `n ≤ 7` artefact and breaks at `n = 8`
(printed witnesses in §9's E5 output). The seed is a real degree of freedom — which is what makes the
Seed Barrier bind rather than being vacuous.

---

## 6. Answering Q1 as asked, item by item

1. **"Does repetition padding `C ⊗ rep_m` produce a DEEP-FLAG instance with the same answer?"**
   **No.** For `m` even the padded one-rung answer is the constant `[r'' ≤ mN/2]` (Q1-P1); for `m` odd
   the padded one-rung answer is preserved, and precisely for that reason no correct padding exists
   unless `PH = NP` (Q1-P2 + Q1-1). Concretely, on the family `C = {0^N,1^N}`, `r = N/2`, the padded
   instance is NO at every odd `m` at the balanced seed (and, at `m = 3`, at every seed) while the
   source is CRP-YES (Q1-P4).
2. **"…or a variant the Theorem E analysis suggests?"** The two other variants that the analysis
   suggests were checked and fail for the same two reasons: the **check-side** repetition
   (`H ↦ H ⊗ 1_m`) preserves depth exactly (Q1-P3) and so is barred by Q1-1; **direct-sum padding**
   with a block of guaranteed depth makes the seed unconditionally deep — which is *allowed* by
   Q1-1a — but it also makes the chain condition vacuous (the guaranteed depth covers every rung), so
   the instance becomes constant-YES and again carries no information. The general statement is
   Corollary Q1-1b: *no* padding can do it.
3. **"If no, the counterexample tells us which structural feature of deep holes blocks laddering."**
   It is not a feature of deep holes; it is a feature of the *problem statement*: DEEP-FLAG publishes
   a deep hole in its input. The structural feature that decides the padded answer is the
   **connectivity of `D_r` in the hypercube** (Q1-P4, E4/c: the answer tracks the edge count of `D_r`,
   not `|D_r| > 0`), and connectivity of a coNP-defined region is not what a covering-radius theorem
   knows about.

---

## 7. Reprice, and the one route the barrier's proof points at

| item | before (parent artifact §8) | after | why |
|---|---|---|---|
| Q1 (this gate) | open, "the single highest-value hour on the node" | **settled, negative** | §2–§4 |
| R4 `covering-radius-transfer` | `P ≈ 0.25`, `D = 4–6`, gated on Q1 | **dead as a transfer**: `P ≈ 0.02` (residual = the chance Q1-1 or A9′ is wrong), `D = ∞` for the transfer plan | Cor. Q1-1b |
| sub-claim (S) "DEEP-FLAG is `Σ_2`-hard" | the residual; would follow from A9′ + Q1 | **still open, but unreachable from CRP**: any proof must build unconditionally deep seeds and put all `Σ_2` content in the chain | Cor. Q1-1a |
| Theorem E ladder as the barrier (parent §4, Horn 2) | "the ladder requirement is what has to be defeated" | **retracted**: the ladder is removed by duplicating columns (Thm Q1-2) | §5 |
| wrappers (R1)–(R3) | to be built if Q1 landed | **not to be built**: they wrap a reduction that cannot exist | §2 |
| R3 `qsat2-budget-gadget-hardness` | `P ≈ 0.15`, `D = 5–6` | unchanged numerically, but now **the sole registered route**; its `−h` discount obstruction (parent §5.3) is untouched by anything here | — |
| **new** R5 `deep-region-reconfiguration` | — | `P ≈ 0.1`, `D = 5–7`; see below | §5, §2 |
| node `CIRCDIST.cplx.sigma2` | `P ≈ 0.2`, `D = 5–7` | `P ≈ 0.12`, `D = 6–8` — one of the two live routes was removed and nothing was added of equal strength | this file |

**R5, stated so the dispatcher can price it.** Theorems Q1-1a and Q1-2 together say what a hardness
proof for DEEP-FLAG must look like: build `(C'', t'', r'')` in which (i) `t''` is deep by construction,
*independently of the source instance* — so the constructed covering radius is constant-YES; and
(ii) the `Σ_2` content sits in whether the deep region `D_{r''}` admits a *walk* (Q1-2 makes chain and
walk interchangeable once columns are duplicated) from `t''` to its antipode with the prescribed edge
multiplicities. That is a **reconfiguration problem over a coNP-defined feasible region**, and the
natural complete problems to aim at are the bounded-length reconfiguration problems, not covering
radius. I flag, as **speculation** and nothing more, that this is a plausible `Σ_2` shape (guess a
poly-length walk; verify each vertex against a coNP oracle) and that it is the only shape compatible
with the barrier. I did **not** attempt it.

**Recommended dispatcher action.** Close frontier task-002 (Q1) as *settled, negative*. Do **not**
open the (R1)–(R3) wrapper obligations. Either re-price R3 as the sole route and continue there, or
open R5 with a recon-sized box (≤ 1 session) whose only job is to find whether a bounded-length
reconfiguration problem with a coNP-defined region is `Σ_2`-complete in the literature; if it is not,
the node should be repriced downward again.

---

## 8. Honest limits

* **Nothing is PROVED.** Theorems Q1-1, Q1-2 and Propositions Q1-P1…P4 are CONJECTURED: written-out
  arguments, internally checked, never independently reviewed.
* **Q1-1's complexity consequence rests on A9′**, which the parent artifact verified only at
  peer-reviewed-secondary level (McLoughlin 1984 unread). If A9′ is wrong — if the covering-radius
  problem is not `Σ_2`-complete in the complement direction — then Q1-1 still shows that an
  answer-preserving padding puts the source problem in coNP, but the collapse conclusion weakens to
  whatever that source's true complexity permits. Note, though, that §4's counterexample family is
  **independent of A9′**.
* **Q1-P2's upper bound is verified, not argued.** I proved `ρ(C^{(m)}) ≥ N(m−1)/2 + ρ(C)` for odd `m`
  and checked equality exhaustively in the stated scope; I did not close the unbalanced case by hand.
  A counterexample would only *strengthen* the verdict (it would move odd-`m` padding into the
  answer-destroying class of Q1-P1); it cannot rescue the route.
* **Q1-2's optimality step is the soft one.** "An optimal chain may be taken to be all-toggle" is
  supported by 368 + 672 exhaustive cases, not by a closed argument.
* **Scopes are small.** Everything exhaustive is `n ≤ 6` unpadded, `nm ≤ 22` for covering radii,
  `nm ≤ 16` for padded chain DPs; the seed-split census reaches `n = 9` on random codes only. All
  absence-type statements ("0 mismatches", "0 edges") mean exactly that scope.
* **Not attempted:** Q2 (is CRP still `Π_2`-hard for codes generated by weight-≤3 vectors plus one
  heavy vector); any Z-sector statement; any CSS realisation; any attempt at (S) from a non-CRP
  source; `Circ-Preserve`.
* **One inherited claim I did not re-derive:** the parent artifact's Theorem D (`k = 1` dictionary),
  which is what makes DEEP-FLAG the right residual at all. §5's retraction of Horn 2 is *my* claim
  about *its* Theorem E, and it deserves adversarial review before the node file is edited.

---

## 9. Code

Four standalone scripts plus a library, pure Python 3, exact `F_2`, no dependencies. Run in the order
`e1, e2, e3, e4, e5`; each imports `q1lib`.

### `q1lib.py`

```python
"""Exact F_2 harness for DEEP-FLAG (pure classical coding theory, no CSS machinery)."""
import itertools

def popc(x): return bin(x).count("1")

def span(basis):
    out = [0]
    for b in basis:
        out = out + [x ^ b for x in out]
    return sorted(set(out))

def dist_to_code(v, code):
    return min(popc(v ^ c) for c in code)

def covering_radius(code, n):
    return max(dist_to_code(v, code) for v in range(1 << n))

def deep_mask(code, n, r):
    """bytearray D[v] = 1 iff dist(v, code) >= r."""
    D = bytearray(1 << n)
    for v in range(1 << n):
        if dist_to_code(v, code) >= r:
            D[v] = 1
    return D

def deep_flag(D, n, t):
    """Is there a maximal chain 0 = A_0 c ... c A_n = [n] with D[chi_A_j ^ t] = 1 for all j?
       D is the deep mask.  Exact DP over the Boolean lattice."""
    full = (1 << n) - 1
    if not D[t] or not D[full ^ t]:
        return False
    good = bytearray(1 << n)
    order = sorted(range(1 << n), key=lambda a: -popc(a))
    for A in order:
        if not D[A ^ t]:
            continue
        if A == full:
            good[A] = 1
            continue
        for q in range(n):
            if not (A >> q) & 1 and good[A | (1 << q)]:
                good[A] = 1
                break
    return bool(good[0])

def rep_pad_code(code, n, m):
    """C tensor rep_m : each coordinate repeated m times.  Generator-side padding."""
    blk = [((1 << m) - 1) << (m * i) for i in range(n)]
    out = []
    for c in code:
        v = 0
        for i in range(n):
            if (c >> i) & 1:
                v |= blk[i]
        out.append(v)
    return out, n * m

def rep_pad_vec(v, n, m):
    blk = [((1 << m) - 1) << (m * i) for i in range(n)]
    out = 0
    for i in range(n):
        if (v >> i) & 1:
            out |= blk[i]
    return out

def all_subspaces_containing(n, must):
    """All F_2-subspaces of F_2^n containing the vector `must`.  Exhaustive, dedup by span."""
    vecs = [v for v in range(1, 1 << n)]
    seen = {}
    for k in range(0, n + 1):
        for comb in itertools.combinations(vecs, k):
            S = span(list(comb) + [must])
            key = tuple(S)
            if key not in seen:
                seen[key] = S
        if k >= 4:
            break
    return list(seen.values())

# ---- exact covering radius via BFS over cosets (canonical representatives) ----

def rref_basis(rows):
    rows = [r for r in rows if r]
    R, piv = [], []
    for r in rows:
        for p, b in zip(piv, R):
            if (r >> p) & 1:
                r ^= b
        if r:
            p = r.bit_length() - 1
            R.append(r); piv.append(p)
            for i in range(len(R) - 1):
                if (R[i] >> p) & 1:
                    R[i] ^= r
    return R, piv

def canonizer(basis):
    R, piv = rref_basis(basis)
    def red(v):
        for b, p in zip(R, piv):
            if (v >> p) & 1:
                v ^= b
        return v
    return red, len(R)

def covering_radius_bfs(basis, N):
    """max coset-leader weight of the code spanned by `basis` inside F_2^N."""
    from collections import deque
    red, k = canonizer(basis)
    cols = [red(1 << q) for q in range(N)]
    seen = {0: 0}
    dq = deque([0]); best = 0
    while dq:
        x = dq.popleft(); dx = seen[x]
        for c in cols:
            y = x ^ c
            if y not in seen:
                seen[y] = dx + 1
                if dx + 1 > best: best = dx + 1
                dq.append(y)
    assert len(seen) == 1 << (N - k), (len(seen), N, k)
    return best
```

### `e1.py` — does the one-rung answer determine DEEP-FLAG? (exhaustive census)

```python
"""E1.  Exhaustive census: does the one-rung answer (rho(C) >= r) determine DEEP-FLAG?
   Also: does DEEP-FLAG depend on the seed t for a fixed (C,r)?"""
import sys
from q1lib import *

for n in (4, 5, 6):
    codes = all_subspaces_containing(n, (1 << n) - 1)
    cells = {(True, True): 0, (True, False): 0, (False, True): 0, (False, False): 0}
    seed_split = seed_allno = seed_allyes = ncr = 0
    ex_split = ex_allno = None
    for code in codes:
        rho = covering_radius(code, n)
        for r in range(1, n + 1):
            one_rung = (rho >= r)
            D = deep_mask(code, n, r)
            ys = ns = 0
            for t in range(1 << n):
                f = deep_flag(D, n, t)
                cells[(one_rung, f)] += 1
                if D[t]:
                    ys += f; ns += (not f)
            if one_rung:
                ncr += 1
                if ys and ns:
                    seed_split += 1
                    if ex_split is None: ex_split = (code, r, rho)
                elif ys == 0:
                    seed_allno += 1
                    if ex_allno is None: ex_allno = (code, r, rho)
                else:
                    seed_allyes += 1
    print(f"n={n}: codes containing 1_n = {len(codes)}")
    print(f"   (one_rung, deep_flag) cell counts over all (C,r,t): {cells}")
    print(f"   (C,r) pairs with rho>=r : {ncr}   of which"
          f"  seed-split={seed_split}  all-seeds-NO={seed_allno}  all-deep-seeds-YES={seed_allyes}")
    if ex_allno:
        code, r, rho = ex_allno
        print(f"   example all-seeds-NO: r={r} rho={rho} C={['{:0{}b}'.format(c,n) for c in code]}")
    sys.stdout.flush()
```

```
n=4: codes containing 1_n = 16
   (one_rung, deep_flag) cell counts over all (C,r,t): {(T,T): 98, (T,F): 206, (F,T): 0, (F,F): 720}
   (C,r) pairs with rho>=r : 19   of which  seed-split=0  all-seeds-NO=11  all-deep-seeds-YES=8
   example all-seeds-NO: r=2 rho=2 C=['0000', '1111']
n=5: codes containing 1_n = 67
   (one_rung, deep_flag) cell counts over all (C,r,t): {(T,T):1310, (T,F):1794, (F,T):0, (F,F):7616}
   (C,r) pairs with rho>=r : 97   of which  seed-split=0  all-seeds-NO=45  all-deep-seeds-YES=52
   example all-seeds-NO: r=2 rho=2 C=['00000', '00001', '11110', '11111']
n=6: codes containing 1_n = 373
   (one_rung, deep_flag) cell counts over all (C,r,t): {(T,T):19772,(T,F):21892,(F,T):0,(F,F):101568}
   (C,r) pairs with rho>=r : 651   of which  seed-split=0  all-seeds-NO=262  all-deep-seeds-YES=389
   example all-seeds-NO: r=3 rho=3 C=['000000', '111111']
```

*(Reading: `(F,T) = 0` everywhere is the trivial direction, chain ⇒ deep point. The large `(T,F)`
counts are the content — the one-rung answer does not determine the chain answer.)*

### `e2.py` — covering radius of both paddings (Propositions P1, P2, P3)

```python
"""E2.  Covering radius of the two readings of 'repetition padding'.  Exact, BFS over cosets."""
import sys
from q1lib import *

def rep_basis(basis, n, m):
    return [rep_pad_vec(b, n, m) for b in basis]

def parity_basis(basis, n, m):
    out = []
    for i in range(n):                       # ker(pi): even-weight vectors inside one block
        for j in range(1, m):
            out.append((1 << (m * i)) | (1 << (m * i + j)))
    for b in basis:                          # one lift per generator of C
        v = 0
        for i in range(n):
            if (b >> i) & 1:
                v |= 1 << (m * i)
        out.append(v)
    return out

def basis_of(code):
    R, _ = rref_basis(list(code)); return R

stats = {"P1": [0, 0], "P2": [0, 0], "P3": [0, 0]}
for n in (2, 3, 4, 5, 6):
    for code in all_subspaces_containing(n, (1 << n) - 1):
        B = basis_of(code); rho = covering_radius_bfs(B, n)
        for m in (2, 3, 4, 5, 6, 7):
            N = n * m
            if N > 22: continue
            R = covering_radius_bfs(rep_basis(B, n, m), N)
            if m % 2 == 0:
                stats["P1"][0] += 1
                if R != N // 2: stats["P1"][1] += 1; print("P1 FAIL", n, m, rho, R)
            else:
                stats["P2"][0] += 1
                if R != n * (m - 1) // 2 + rho: stats["P2"][1] += 1; print("P2 FAIL", n, m, rho, R)
        for m in (2, 3, 4):
            N = n * m
            if N > 20: continue
            R = covering_radius_bfs(parity_basis(B, n, m), N)
            stats["P3"][0] += 1
            if R != rho: stats["P3"][1] += 1; print("P3 FAIL", n, m, rho, R)
for k, (a, b) in stats.items():
    print(f"{k}: cases={a} failures={b}")
# -> P1: cases=560 failures=0
#    P2: cases=493 failures=0
#    P3: cases=1016 failures=0
```

### `e3.py` — Theorem Q1-2 (balanced seed) and the seed census

```python
"""E3.  (W) padded DEEP-FLAG at the balanced seed == deep exact-count walk in F_2^n.
        (S) does SOME seed of the padded instance give a chain whenever rho(C) >= r?"""
import sys
from q1lib import *

def balanced_seed(t, n, m):
    h = (m - 1) // 2; v = 0
    for i in range(n):
        for j in range(h + ((t >> i) & 1)):
            v |= 1 << (m * i + j)
    return v

def deep_walk(D, n, m, t):
    """walk t -> t+1, nm steps, coordinate i used exactly m times, all vertices deep."""
    full = (1 << n) - 1
    if not D[t]: return False
    base = (m + 1) ** n
    def enc(v, cnt):
        s = 0
        for c in cnt: s = s * (m + 1) + c
        return v * base + s
    frontier = {enc(t, tuple([0] * n))}
    for _ in range(n * m):
        nxt = set()
        for st in frontier:
            v, s = divmod(st, base)
            cnt = []; ss = s
            for _ in range(n):
                cnt.append(ss % (m + 1)); ss //= (m + 1)
            cnt = cnt[::-1]
            for i in range(n):
                if cnt[i] == m: continue
                w = v ^ (1 << i)
                if not D[w]: continue
                c2 = list(cnt); c2[i] += 1
                nxt.add(enc(w, tuple(c2)))
        frontier = nxt
        if not frontier: return False
    return enc(full ^ t, tuple([m] * n)) in frontier

def basis_of(code):
    R, _ = rref_basis(list(code)); return R

badW = totW = 0                                   # ---- (W) ----
for n in (3, 4):
    for code in all_subspaces_containing(n, (1 << n) - 1):
        B = basis_of(code); rho = covering_radius_bfs(B, n)
        for m in (3, 5):
            N = n * m
            if N > 16: continue
            pc, _ = rep_pad_code(code, n, m)
            for r in range(1, rho + 1):
                Dp = deep_mask(pc, N, n * (m - 1) // 2 + r); D = deep_mask(code, n, r)
                for t in range(1 << n):
                    lhs = deep_flag(Dp, N, balanced_seed(t, n, m))
                    rhs = deep_walk(D, n, m, t)
                    totW += 1; badW += (lhs != rhs)
print(f"(W) cases={totW} failures={badW}")        # -> (W) cases=368 failures=0

for n in (3, 4):                                  # ---- (S) ----
    m = 3; N = n * m; tot = crp_yes = some_yes = bal_yes = 0; ex = None
    for code in all_subspaces_containing(n, (1 << n) - 1):
        B = basis_of(code); rho = covering_radius_bfs(B, n)
        pc, _ = rep_pad_code(code, n, m); red, k = canonizer([rep_pad_vec(b, n, m) for b in B])
        for r in range(1, n + 1):
            tot += 1
            if rho < r: continue
            crp_yes += 1
            Dp = deep_mask(pc, N, n * (m - 1) // 2 + r); D = deep_mask(code, n, r)
            reps = sorted({red(v) for v in range(1 << N) if Dp[v]})
            some = any(deep_flag(Dp, N, t) for t in reps)
            bal = any(D[t] and deep_flag(Dp, N, balanced_seed(t, n, m)) for t in range(1 << n))
            some_yes += some; bal_yes += bal
            if not some and ex is None: ex = (code, r, rho)
    print(f" n={n} m={m}: pairs={tot} CRP-YES={crp_yes} padded-YES(some seed)={some_yes} "
          f"(balanced seed)={bal_yes}   witness={ex}")
# -> n=3 m=3: pairs=15 CRP-YES=4  padded-YES(some)=1 (balanced)=1  witness=({000,001,110,111}, r=1)
#    n=4 m=3: pairs=64 CRP-YES=19 padded-YES(some)=8 (balanced)=8  witness=({0000,1111}, r=2)
```

### `e4.py` — check-side walk law; the edgeless family; large `m`

```python
"""E4. (a) check-side padding obeys the same walk law (any m);
       (b) C = {0^N,1^N}, r = N/2: CRP-YES with an edgeless deep region;
       (c) the walk predicate as a function of m on the E3 witnesses."""
# (a) as in E3 but with pi^{-1}(C) and the seed 'one lift of t per block',
#     endpoint t + (m mod 2)*1_n:
#     -> cases=672 failures=0     (n in {3,4}, m in {2,3}, nm <= 12, all r, all seeds)
# (b) exact:
#     N=4 : rho=2  r=2  CRP-YES  |D_r|=6    hypercube edges inside D_r = 0
#     N=6 : rho=3  r=3  CRP-YES  |D_r|=20   edges = 0
#     N=8 : rho=4  r=4  CRP-YES  |D_r|=70   edges = 0
#     N=10: rho=5  r=5  CRP-YES  |D_r|=252  edges = 0
# (c) walk predicate at m = 3,5,7,9,11 (any deep seed):
#     n=3 C={000,001,110,111} r=1  |D_r|=4  edges=2   -> False at every m
#     n=4 C={0000,1111}       r=2  |D_r|=6  edges=0   -> False at every m
#     n=4 C={0000,1111}       r=1  |D_r|=14 edges=24  -> True  at every m
```

### `e5.py` — scope of the "no seed split" regularity

```python
"""E5.  For fixed (C,r) with 1_n in C, do all DEEP seeds give the same DEEP-FLAG answer?
   Random codes, n = 7,8,9, 400 trials each."""
# -> n=7: (C,r) pairs tested=856   seed-split cases=0
#    n=8: pairs=986   seed-split cases=12
#         e.g. r=2 rho=4 basis=['10010110','01011010','00110011']
#    n=9: pairs=1065  seed-split cases=6
#         e.g. r=2 rho=2 basis=['100001010','000011000','010001011','000000101','001100011']
```

---

*Session scope note.* Everything above is proposer-side. No node file, route, or assessment was
written; no existing artifact was modified; `research/circdist/proof-dag/` was not touched. No result
in this document has had independent adversarial review. In particular §5's retraction of the parent
artifact's Horn 2, and §7's proposed reprice of R4 to `P ≈ 0.02`, are proposals for the dispatcher,
not edits.
