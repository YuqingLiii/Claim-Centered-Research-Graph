# STAGE 2P — The automorphism group of k-Sum: three theorems with exact boundaries

**Date:** 2026-07-16. **Author:** Opus 4.8 executor/verifier (two-model protocol; Fable 5 = strategist).
**Mandate:** turn the Stage-0 *numerical* symmetry facts (`KSUM_STAGE0_VERDICT.md` §1.4, §4.2; logs
`B1/B2/B3`) into theorems with exact excluded sets, or refute them.

**PROTOCOL FLAG (required by the tasking, and honoured).** The bundle states the three target group
identities in advance and supplies a "proof strategy to try" for each. That embeds a hoped-for answer, which
the protocol (`KSUM_SMALL_G_COMMISSION.md` §-1.2 item 1) says I must flag. I flag it here and proceeded to
verify each claim as genuinely open — willing to refute. Outcome: **Theorems 1 and 3 are PROVED outright;
Theorem 2 is PROVED under one explicit, checkable hypothesis and is confirmed by exhaustive computation at
every reachable point including both ground-truth points; no counterexample to any of the three was found.**
Where the supplied strategy failed I replaced it (Theorem 1's proof below is *not* the strategy handed to
me — that strategy's "isolate a pair with one background value" step does not control the OR/line terms after
the map scrambles the background; the working proof uses a **single background position** for `n=3` and a
**full-column-count + third-position** argument for `n≥4`, detailed in §1.4).

**Label discipline (G9).** Every displayed claim carries one of PROVED / NUMERICAL / CONJECTURED / OPEN.
PROVED means a complete proof appears here and (where finite) it is independently cross-checked by exhaustive
computation. Numbers read from computation are NUMERICAL. The exhaustive cross-checks are *disclosure*, not
certification (G1): the certifying object is the proof text.

**Provenance rule (hard).** Every number carries (command, log, script SHA-256) inline or via §5. Script
`ksum/tools/ksum_stage2p_verify.py` SHA-256 `573f70c8940a8e7a08c4b116fdf5d9170f65ea3c85d1f6e97e33409afbf733df`;
log `ksum/artifacts/logs_ksum_stage2_20260716/S2P_verify.log` SHA-256
`cc6ac0132be916f8d1779c1fe89b484e273571f3f16c804ff3ac4d20a50f1dd8`; interpreter
`<machine-local-path-redacted>` (Python 3.11.9, numpy 1.26.4, Windows).
Primary source `ksum/artifacts/references/BS_1206.6528v2_ksum.tex` SHA-256
`41fff42aab869c11fd77fb912245d2d5bd12d82e0eea4192a8755b22e0cd90d0` (matches the Stage-0 recorded hash).

---

## 0. Notation and standing definitions (G4 — every symbol defined at first use)

- `G`: a finite abelian group, written additively, with `q := |G|`. `0 ∈ G` the identity. `t ∈ G` a fixed
  target. `n ≥ 1` (number of positions), `k ≥ 1` (subset size). `[n] := {1,…,n}`.
- `G[m] := {x ∈ G : m·x = 0}` (`m`-torsion). `2G := {2x : x ∈ G}`. `exp(G)` the exponent (lcm of element
  orders).
- **k-Sum function** `f = f_{G,t,k,n} : G^n → {0,1}`: `f(x)=1` iff `∃ S ⊆ [n], |S|=k, Σ_{i∈S} x_i = t`.
  Inputs with `f(x)=1` are **positive**; `f(x)=0` **negative**. Matches BS Example 3
  (`BS:120–122`) and the k-sum problem `BS:100`.
- `Sym(G)`: the symmetric group on the `q` elements of `G` (all value relabellings), order `q!`.
- **Wreath group** `W := Sym(G) ≀ S_n = Sym(G)^n ⋊ S_n`. An element is `w=(π_1,…,π_n;ς)` with
  `π_i ∈ Sym(G)`, `ς ∈ S_n`, acting on `x ∈ G^n` by `(w·x)_i = π_i(x_{ς^{-1}(i)})`. `W` is exactly the group
  of permutations of `G^n` preserving every relation `Δ_i` (the pattern `x_i ≠ y_i`), i.e. the largest group
  a query lower bound can use.
- `Aut(f) := { w ∈ W : f(w·x)=f(x) ∀x } ≤ W` (the automorphisms *inside* `W`; this is what
  `B1/B2/B3` compute). Because `f` is Boolean, `w ∈ Aut(f)` iff `w` preserves the positive set setwise.
- **Diagonal embedding** `diag: Sym(G) → W`, `diag(π)=(π,…,π;id)`. For a set `H ⊆ Sym(G)`,
  `diag(H)={diag(π):π∈H}`.
- **k=2 involution** `σ = σ_{G,t} ∈ Sym(G)`, `σ(x) := t − x`. It is an involution (`σ²=id`); its fixed set
  is `Fix(σ)={x:2x=t}`, of size `τ := |Fix(σ)|`. For `i≠j`: `x_i+x_j=t ⟺ x_j = σ(x_i)`.
- **Centralizer** `C := C_{Sym(G)}(σ) = {π ∈ Sym(G) : πσ = σπ}`.
- `Aut(G)`: the group automorphisms of `(G,+)` (additive bijections; note `u∈Aut(G) ⟹ u(0)=0`).
- **Affine stabiliser** `Aff_{k,t}(G) := { x ↦ u(x)+c : u∈Aut(G), c∈G, u(t)+k·c=t }`, a set of affine
  permutations of `G` (a subgroup of `Sym(G)`; §2.1 verifies closure).
- **Orthogonal array** (BS Def 2, `BS:110–112`): `T ⊆ [q]^k`, `|T|=q^{k-1}`, such that fixing any `k−1`
  coordinates leaves **exactly one** completion in `T` ("index-1, length-k"). k-Sum's array is
  `T={x∈G^k:Σx_i=t}` (Ex 3); Element Distinctness is `T={(x,x):x∈[q]}` (Ex 4, `BS:124`).

Throughout, the **key reduction** (used in Theorems 1 and 2):

> **Lemma R (semidirect reduction).** For any `G,t,k,n`, `S_n ≤ Aut(f)` under the position action
> (`w=(id,…,id;ς)`). Consequently `Aut(f) = K ⋊ S_n`, where `K := Aut(f) ∩ {ς=id}` is the group of pure
> value-permutations preserving `f`, and `S_n` normalises `K`. In particular `|Aut(f)| = |K|·n!`, and it
> suffices to determine `K`. **PROVED.**
>
> *Proof.* `f` depends only on the multiset of unordered pairs/tuples of coordinate values, which is
> invariant under permuting positions; so `f((id;ς)·x)=f(x)`, giving `S_n ≤ Aut(f)`. The map `W→S_n`,
> `w↦ς`, is a homomorphism; `S_n` splits it (as a subgroup mapping isomorphically). For `w∈Aut(f)` with
> position part `ς`, `w·(id;ς)^{-1}∈Aut(f)∩{ς=id}=K`, so `Aut(f)=K·S_n`. Conjugating `(π_1,…,π_n;id)` by
> `(id;ς)` gives `(π_{ς^{-1}(1)},…,π_{ς^{-1}(n)};id)`, still pure-value and still in `Aut(f)` (conjugate of
> an automorphism by an automorphism); so `S_n` normalises `K` and `Aut(f)=K⋊S_n`. ∎

All three theorems therefore reduce to identifying `K`.

---

## 1. THEOREM 1 (k=2): the alphabet-side group is the diagonal centralizer

### 1.1 Constancy characterisation (needed to state the exact excluded set) — **PROVED**

> **Proposition 1.0.** Fix `k=2`, `n≥2`, any finite abelian `G`, any `t`.
> 1. `f` is **never constant-0**.
> 2. `f` is **constant-1** iff `σ=id` **and** `n>q`, equivalently `t=0 ∧ G=G[2] ∧ n>q`.
> 3. Hence for `n≥3` the *only* constant case is (2); for `n≥2` the excluded set is exactly
>    `{ t=0, G=G[2], n>q }`.

*Proof.* (1) For `n≥2` pick positions `i≠j`, set `x_i=a`, `x_j=t−a` (`∈G`), rest arbitrary; then
`x_i+x_j=t`, so `f(x)=1`. A positive input always exists ⇒ not constant-0.

(2) If `σ≠id` there is a **non-fixed** value `a` (`2a≠t`). The all-`a` input has every pair summing to
`2a≠t`, so it is negative ⇒ `f` not constant-1. Thus constant-1 ⟹ `σ=id`. `σ=id` means `t−x=x` i.e. `2x=t`
for **all** `x`; at `x=0` this gives `t=0`, and then `2x=0 ∀x`, i.e. `G=G[2]`. Conversely if `t=0, G=G[2]`
then `x_i+x_j=0 ⟺ x_i=x_j` (as `−x=x`), so `f` is **Element Distinctness** over the alphabet `G`;
`f(x)=0` iff all coordinates distinct, which is possible iff `n≤q` (pigeonhole). So under `σ=id`, `f` is
constant-1 iff `n>q`, and non-constant iff `n≤q`. ∎

Cross-check (NUMERICAL): predicted-vs-measured constancy agrees at every tested point (e.g. `Z2,t=0,n=3`
constant-1; `Z2xZ2,t=0,n=5` constant-1; `Z2xZ2,t=0,n=4` non-constant; `Z2,t=1` never constant), log
`S2P_verify.log` lines under "THEOREM 1".

### 1.2 The theorem — **PROVED**

> **Theorem 1.** Fix `k=2`, `n≥3`, any finite abelian `G`, any `t ∈ G`, and assume `f` is **not constant**
> (i.e. exclude `t=0 ∧ G=G[2] ∧ n>q`). Then
> `K = diag(C)`, and therefore
> `Aut(f) = diag(C_{Sym(G)}(σ)) ⋊ S_n`, of order `|C|·n! = τ! · 2^{(q−τ)/2} · ((q−τ)/2)! · n!`,
> with `σ(x)=t−x`, `τ=|{x:2x=t}|`. **There are no non-diagonal value-permutation automorphisms.**

The order formula for `|C|` is the standard centralizer of an involution of cycle type `1^τ 2^{(q−τ)/2}`
(fixed points permuted freely: `τ!`; transpositions permuted and internally flipped: `2^{(q−τ)/2}((q−τ)/2)!`);
`q−τ` is even because non-fixed points pair up under `σ`. The identity `|C|=τ!2^{(q−τ)/2}((q−τ)/2)!` is
re-verified against a brute centralizer count at all 20 tested points (log; matches Stage-0 `B2(a)` exactly).

### 1.3 Containment `diag(C)⋊S_n ⊆ Aut(f)` — **PROVED**

`S_n⊆Aut(f)` is Lemma R. For `π∈C`, `diag(π)` sends `x↦(π(x_1),…,π(x_n))`; a pair hits iff
`π(x_i)+π(x_j)=t ⟺ π(x_j)=σ(π(x_i))`. Since `π∈C` means `σπ=πσ`, `σ(π(x_i))=π(σ(x_i))`, so
`π(x_j)=π(σ(x_i)) ⟺ x_j=σ(x_i) ⟺ x_i+x_j=t`. Thus `diag(π)` preserves every pair's hit-status, hence `f`.
`diag(C)` and the position `S_n` commute, so `diag(C)⋊S_n = diag(C)×S_n ⊆ Aut(f)`. (NUMERICAL cross-check:
"predicted diag(C) subset of Aut: True" at all points.)

### 1.4 The hard direction `K ⊆ diag(C)` — **PROVED** (four exhaustive cases covering all `G,t,n≥3`)

By Lemma R it suffices to show: every `w=(π_1,…,π_n;id)∈K` has `π_1=…=π_n=:π` with `π∈C`. The proof splits
into four cases whose union is *all* non-constant instances; each case is complete on its own (no case is
closed by finite computation — the computation only cross-checks).

**Reduction target.** It suffices to prove the pair relation
`(‡)_{ij}: π_j∘σ = σ∘π_i` for all ordered `i≠j`. Indeed, given `(‡)`, pick a third index `l` (exists as
`n≥3`); `(‡)_{il}` and `(‡)_{jl}` give `π_l σ=σπ_i` and `π_l σ=σπ_j`, so `σπ_i=σπ_j ⟹ π_i=π_j`; hence all
`π` are equal to a common `π`, and `(‡)_{ij}` becomes `πσ=σπ`, i.e. `π∈C`. So the whole theorem is `(‡)`.

Fix `w∈K`. Restrict to two **active** positions `{i,j}` and set every other position to a chosen
**background** value; write the induced condition `f(x)=f(w·x)` as an identity of subsets of `G×G` in the
active coordinates `(a,b)=(x_i,x_j)`.

---

**Case A: `σ = id`** (⟺ `t=0, G=G[2]`; non-constant ⟺ `n≤q`; here `C=Sym(G)`, so the claim is
`K=diag(Sym(G))`, i.e. `π_1=…=π_n` arbitrary).

`f` is Element Distinctness. Suppose some `π_i≠π_j` as functions: pick `a` with `π_i(a)≠π_j(a)`. Build the
input `x` with `x_i=x_j=a` and the other `n−2` positions holding distinct values `≠a` and distinct from each
other (possible: needs `n−1≤q` distinct values, and `n≤q`). Then `f(x)=1` (positions `i,j` collide). Now
make `w·x` **all-distinct**: assign the images one position at a time; at each step the images already placed
number `≤ n−1 ≤ q−1 < q`, and the current `π_ℓ` is a bijection with `q` available images, so a fresh image
exists — including for positions `i,j` where `π_i(a)≠π_j(a)` are already distinct. Then `w·x` has all
coordinates distinct ⇒ `f(w·x)=0≠1=f(x)`, contradicting `w∈Aut(f)`. Hence all `π_i` equal; any common
`π∈Sym(G)=C` works (§1.3). ∎(A) *(Cross-checked: `Z2xZ2,t=0,n=3,4` give `K=diag(S_4)`, `|K|=24`.)*

---

For Cases B–C assume `σ≠id`, so a non-fixed value exists, and `q≥3`.

**Case B: `q≥3`, `σ≠id`, `n=3`.** There is exactly **one** background position. For the pair `{1,2}` with
background position `3` holding any value `d∈G` (a single coordinate never self-hits, so `d` may be a fixed
point):
`f(x) = [a+b=t] ∨ [a=σd] ∨ [b=σd]` — support `A = D ∪ V ∪ H`, where `D={b=σ(a)}` (the graph of `σ`, one
point per row and per column), `V={a=σd}` (a full column), `H={b=σd}` (a full row).
Applying `w`: `(w·x)_1=π_1(a)`, `(w·x)_2=π_2(b)`, `(w·x)_3=π_3(d)`, giving support `B = D' ∪ V' ∪ H'` with
`D'={b=ρ(a)}` (`ρ:=π_2^{-1}σπ_1`), `V'={a=π_1^{-1}σπ_3 d}`, `H'={b=π_2^{-1}σπ_3 d}`.
Since `q≥3`, a column is **full** (all `q` entries present) iff it is the `V`/`V'` column: any other column
meets `A` in `≤2<q` points (one from `D`, one from `H`). `A=B` therefore forces their unique full columns to
coincide: `σd=π_1^{-1}σπ_3 d`, i.e. `π_1(σd)=σ(π_3 d)`; and unique full rows: `π_2(σd)=σ(π_3 d)`. These hold
for **every** `d∈G`, so `π_1σ=σπ_3=π_2σ` as full functional equations, giving `π_1=π_2` (compose with `σ`
on the right, `σ` bijective). Cycling the roles over the three pairs `{1,2},{1,3},{2,3}` gives
`π_1=π_2=π_3=:π` and `πσ=σπ`. ∎(B)

**Case C: `q≥3`, `σ≠id`, `n≥4`.** Pair `{i,j}`; set all `n−2` other positions to a common **non-fixed**
value `c` (`2c≠t`). Backgrounds are inert among themselves (`c+c=2c≠t`), so
`f(x)=[a+b=t]∨[a=σc]∨[b=σc]`, support `A=D∪V∪H` as in Case B. Let `M:={π_ℓ(c):ℓ∉{i,j}}` (a multiset of
`n−2` background images). Then
`f(w·x)=[π_i a+π_j b=t] ∨ [π_i a∈σ(M)] ∨ [π_j b∈σ(M)] ∨ κ`, where `σ(M)={t−m}` and `κ=[∃ m≠m'∈M: m+m'=t]`
is a constant.

*Step 1 (`κ=0`).* If `κ=1` then `f(w·x)≡1`, but `A` has a negative point for `q≥3` (choose `a≠σc`, then `b∉
{σc,σa}`, `q−2≥1` choices), contradiction. So `κ=0`.

*Step 2 (all backgrounds agree at `c`).* With `κ=0`, `B = D'∪Vcols∪Hrows` where `D'`=graph of
`ρ=π_j^{-1}σπ_i`, `Vcols={a∈π_i^{-1}σM}` (a union of `|distinct M|` full columns), `Hrows` similarly. For
`q≥3`, `A` has **exactly one** full column. Counting full columns of `B`: if `|distinct M|≤q−2` then non-`Vcols`
columns hold `≤1+|distinct M|≤q−1<q` points, so `#full columns=|distinct M|`; matching `A` forces
`|distinct M|=1`. If `|distinct M|∈{q−1,q}` then `B` has `≥q−1≥2` full columns (or `B` is everything),
contradicting "exactly one". Hence **`|distinct M|=1`**: all `π_ℓ(c)` (`ℓ∉{i,j}`) are equal, `=:μ(c)`.

*Step 3 (all positions agree at `c`).* Repeat Step 2 for varying pairs. Any position `m` is a background of
some pair, and for `n≥4` the background-sets of pairs `{1,2},{1,3},{2,3}` share position `4` (and generally
overlap or chain), forcing `π_1(c)=…=π_n(c)=:μ(c)` for **every** non-fixed `c`. In particular `μ(c)=π_i(c)`.

*Step 4 (commuting on non-fixed values, and equality everywhere).* With backgrounds `≡μ(c)`, `B` has single
lines; matching unique full columns/rows gives `π_i(σc)=σ(μ(c))=σ(π_i(c))`, i.e. **`π_i σ=σπ_i` on all
non-fixed `c`** (holds for every `i`); and Step 3 gives all `π_m` equal on non-fixed values. For a **fixed**
point `a` (`2a=t`, so `a∉{c,σc}`), the point `(a,σa)=(a,a)` lies off the cross `V∪H`, where `A` and `B`
agree, so `ρ(a)=σ(a)=a`, i.e. `σπ_i(a)=π_j(a)`. Using a third position `l` (`n≥4`):
`σπ_i(a)=π_l(a)=σπ_j(a) ⟹ π_i(a)=π_j(a)` on fixed points too. Hence all `π_m` are equal to a common `π` on
**all** of `G`; `σπ(a)=π(a)` shows `π` maps fixed points to fixed points, and combined with `πσ=σπ` on
non-fixed values gives `πσ=σπ` on all of `G`, i.e. `π∈C`. ∎(C)

**Case D: `q=2`.** Then `σ=id` (`t=0`, Case A) or `σ=(01)` (`t=1`). For `t=1`, `x_i+x_j=1 ⟺ x_i≠x_j`, so
`f(x)=1` iff `x` is non-constant; `f^{-1}(0)={0^n,1^n}`. `w=(π_1,…,π_n;id)` preserves `{0^n,1^n}` iff
`w·0^n` and `w·1^n` are constant, iff all `π_i(0)` are equal and all `π_i(1)` are equal; in `Sym(Z_2)` a
permutation is determined by its value at `0`, so this forces `π_1=…=π_n∈Sym(Z_2)=C` (`|C|=2`). ∎(D)
*(Cross-checked: `Z2,t=1,n=3,4,5` give `|K|=2`, `|Aut|=12,48,240`.)*

Cases A–D are exhaustive over all non-constant `k=2` instances with `n≥3`. ∎ **Theorem 1 PROVED.**

### 1.5 Checks against Stage-0 ground truth

All Stage-0 `k=2` data reproduce from `|Aut|=|C|·n!` (`|C|` from the closed form): `(3,2,2,1)→2·6=12`;
`(4,2,2,1)→2·24=48`; `(3,2,3,·)→2·6=12`; `(4,2,3,·)→2·24=48`; `(3,2,4,0)→4·6=24`; `(3,2,4,1)→8·6=48`;
`(4,2,4,1)→8·24=192` — identical to `B1_aut_table.log` and `B2_abc_centralizer.log`. This script's
independent brute enumeration of `K` reproduces every `|K|` (log). Non-cyclic `Z2×Z2` (a group Stage-0 did
not brute at `k=2`) also matches: `t=1→|K|=8`, `t=0→|K|=24` (the `σ=id` ED case), confirming the theorem is
a statement about `σ` (cycle type), not about `G` being cyclic.

### 1.6 What Theorem 1 does *not* assert

It is about `Aut(f)∩W`. It says nothing about automorphisms outside `W` (permutations of `G^n` not
respecting the `Δ_i` pattern) — but those are irrelevant to the adversary bound, whose symmetry group is a
subgroup of `W`. The excluded constant case has `Aut(f)=W` trivially.

---

## 2. THEOREM 2 (k≥3, n>k): the alphabet-side group is the diagonal affine stabiliser

### 2.1 Preliminaries and constancy — **PROVED (necessary condition; sufficient bound)**

`Aff_{k,t}(G)` is a subgroup of `Sym(G)`: composing `x↦u(x)+c` and `x↦u'(x)+c'` gives
`x↦u'u(x)+(u'(c)+c')` with `u'u∈Aut(G)` and `(u'u)(t)+k(u'(c)+c') = u'(u(t)+kc)+kc' = u'(t)+kc' = t`
(using both stabiliser conditions), so it is closed; identity `(id,0)` qualifies; finite ⇒ subgroup.

**Constancy (Proposition 2.0).** For `k≥3`, `n≥k`: `f` is never constant-0 (set `k−1` positions to `0` and
one to `t`). `f` is constant-1 **only if** `t=0` and `exp(G)|k` (necessary: the all-`a` input forces
`k·a=t` for all `a`; at `a=0`, `t=0`; then `k·a=0 ∀a ⟺ exp(G)|k`). A **sufficient** condition is
`t=0, exp(G)|k, n>(k−1)q` (pigeonhole: some value repeats `≥k` times, and `k` copies sum to `k·a=0=t`).
The **exact** threshold is a zero-sum (Erdős–Ginzburg–Ziv-type) invariant of `(G,k)` and is generally
smaller than `(k−1)q` (e.g. `G=Z_3,k=3,t=0`: EGZ gives constant-1 already at `n≥5<(k−1)q+1=7`; measured
constant at `n=6`, log §"(3b)"). The exact zero-sum threshold is **not needed** for the automorphism theorem
and is left as a pointer, labelled **OPEN (exact value; it is a known-hard zero-sum constant)**.

### 2.2 The theorem — **PROVED under hypothesis (NC-ext); confirmed by exhaustive computation at all
reachable points including both ground-truth points**

> **Theorem 2.** Fix `k≥3`, `n>k`, finite abelian `G`, `t∈G`, `f` non-constant, and assume the
> **non-certificate extension hypothesis**:
> `(NC-ext)`: for every `k`-subset `S` and every `x_S∈G^S` with `Σ_{i∈S}x_i≠t`, there is a completion to a
> global **negative** input (some `x∈G^n` restricting to `x_S` on `S` with `f(x)=0`).
> Then `K = diag(Aff_{k,t}(G))`, hence
> `Aut(f) = diag(Aff_{k,t}(G)) ⋊ S_n`, of order `|Aff_{k,t}(G)|·n!`.
>
> `(NC-ext)` holds — so the conclusion holds — for **all** `n>k` whenever `q` is large enough for a
> "spread" background to exist; a clean sufficient form is **`G=Z_q` with `q` prime and `q>k·2^k`** (bound
> independent of `n`; §2.5). For small `q` where `(NC-ext)` is not guaranteed a priori, the conclusion is
> verified by **exhaustive enumeration** of `K` (§2.6), covering `Z_2,Z_3,Z_4,Z_2×Z_2` — in particular both
> Stage-0 ground-truth points.

### 2.3 Containment `diag(Aff_{k,t})⋊S_n ⊆ Aut(f)` — **PROVED**

`S_n⊆Aut(f)` (Lemma R). For `(u,c)∈Aff_{k,t}`, `diag` sends `x_i↦u(x_i)+c`; a subset `S` sums to
`Σ_{i∈S}(u(x_i)+c)=u(Σ_{i∈S}x_i)+k c`. If `Σ_{i∈S}x_i=t` this is `u(t)+kc=t`; conversely if it equals `t`
then `u(Σx_i)=t−kc=u(t)` (using `u(t)+kc=t`), so `Σx_i=t` (`u` injective). Thus each subset's hit-status is
preserved ⇒ `f` preserved. (NUMERICAL: "predicted diag(Aff) subset of Aut: True" at all points, incl. `n=k`.)

### 2.4 The hard direction — **PROVED given (★)**

By Lemma R, take `w=(π_1,…,π_n;id)∈K`. Define, for a `k`-subset `S`, the predicate
`P_S(x)=[Σ_{i∈S}x_i=t]` (a function of `x_S∈G^S` only), and `π_S:=(π_i)_{i∈S}∈Sym(G)^S` acting on `G^S`.

**Claim (★): for every `k`-subset `S`, `P_S(x_S)=P_S(π_S x_S)` for all `x_S∈G^S`** (per-subset certificate
preservation). Granting (★), the rest is algebra:

**(i) (★) from (NC-ext) + a bijection argument.** Fix `S`. Take any non-certificate `x_S` (`P_S=0`). By
`(NC-ext)` complete it to a global negative `x` (`f(x)=0`). Then `f(w·x)=0`, so **no** `k`-subset sums to
`t` in `w·x`; in particular `S` does not: `Σ_{i∈S}π_i(x_i)≠t`, i.e. `P_S(π_S x_S)=0`. Thus `π_S` maps the
non-certificate set `A^c:={x_S:P_S=0}` **into** `A^c`. But `π_S` is a bijection of `G^S`, so it maps `A^c`
*onto* `A^c` and therefore the certificate set `A={x_S:P_S=1}` onto `A`. Hence `P_S(x_S)=P_S(π_S x_S)` for
**all** `x_S` — this is (★). *(No property of `w` on the certificate side is used; `f(x)=0⟹f(w·x)=0` does all
the work. This is the correction to the supplied strategy, which tried to control the image side directly.)*

**(ii) Cauchy: `π_i(x)=u(x)+c_i` with a common additive `u∈Aut(G)`.** Fix `S={1,…,k}`. On the surface
`Σ_{i∈S}x_i=t` we have `x_k=t−Σ_{i<k}x_i` and, by (★),
`π_k(t−Σ_{i<k}x_i)=t−Σ_{i<k}π_i(x_i)`. The left side depends on `(x_1,…,x_{k-1})` only through
`Σ_{i<k}x_i`; hence so does the right, i.e.
`(B): Σ_{i<k}π_i(x_i)` depends only on `Σ_{i<k}x_i`, for all `(x_1,…,x_{k-1})∈G^{k-1}`. Since `k−1≥2` (here
`k≥3` is used), fix `x_3=…=x_{k-1}=0`: `π_1(x_1)+π_2(x_2)` depends only on `x_1+x_2`, say `=Φ(x_1+x_2)`.
Setting `x_2=0` and `x_1=0` gives `Φ(x)=π_1(x)+π_2(0)=π_2(x)+π_1(0)`, whence
`Φ(x_1+x_2)=Φ(x_1)+Φ(x_2)−Φ(0)`. Put `u(x):=Φ(x)−Φ(0)`; then `u(x_1+x_2)=u(x_1)+u(x_2)` (**additive**), and
`u(x)=π_1(x)−π_1(0)` is a **bijection**. An additive bijection of a finite abelian group is a group
automorphism (additive ⇒ endomorphism of `(G,+)`; a bijective endomorphism of a finite group is an
automorphism). So `u∈Aut(G)`, and `π_1(x)=u(x)+c_1`, `π_2(x)=u(x)+c_2` with `c_i=π_i(0)`. Repeating with the
pair `{1,i}` for each `i∈S` (and `u=π_1−π_1(0)` fixed) gives `π_i(x)=u(x)+c_i` for **all** `i∈S`, the **same**
`u`.

**(iii) The affine condition, and constants forced equal by overlap (`n>k`).** Plugging into (★) on `S`:
`Σ_{i∈S}(u(x_i)+c_i)=u(t)+Σ_{i∈S}c_i=t` whenever `Σ_{i∈S}x_i=t`, so `(C): Σ_{i∈S}c_i=t−u(t)` for every
`k`-subset `S`. The exponent `u` is globally well-defined: any two `k`-subsets can be chained through
subsets overlapping in `k−1≥2` coordinates (possible since `n>k`), and on an overlap of `≥1` coordinate the
two exponents agree (both `=π_i−π_i(0)` for a shared `i`). For constants: subsets `S` and
`S'=(S∖{a})∪{b}` (`n>k` supplies a fresh `b∉S`) both satisfy `(C)`, so `c_a=c_b`; connectivity gives all
`c_i` equal to a single `c`, and `(C)` becomes `k c=t−u(t)`, i.e. `u(t)+kc=t`. Hence
`π_i(x)=u(x)+c` for all `i`, with `(u,c)∈Aff_{k,t}(G)`, i.e. `w∈diag(Aff_{k,t})`. ∎ (given (★))

### 2.5 Exact coverage of the proof, and where (NC-ext) is guaranteed — **PROVED**

`(NC-ext)` is a statement about `f` alone (no `w`). A **single repeated background value** suffices to
witness it: given a non-certificate `x_S`, set all `n−k` background positions to one value `b`; a `k`-subset
with `m≥1` background positions and active partial sum `α` (a sum of `k−m` of the values in `x_S`) sums to
`α+m·b`, and `S` itself sums to `Σ_S x_S≠t`. So `f=0` on this completion provided
`α+m·b≠t` for all `m∈{1,…,min(k,n−k)}` and all achievable `α`. The number of forbidden `b` is at most
`(#α)·(#m) ≤ 2^k·k` in a field (each equation `m b=t−α` has `≤1` solution). Therefore:

> **`(NC-ext)` holds for every `n>k` whenever `G=Z_q`, `q` prime, `q>k·2^k`** (bound independent of `n`).
> More generally it holds whenever `G` has an element `b` avoiding the `≤k·2^k` forbidden cosets `{b:mb=t−α}`
> for each `S` — true for all sufficiently large `q` at fixed `k`, uniformly in `n`.

**Not covered by the analytic proof:** instances where `(NC-ext)` can fail — small `q` (`q≤k·2^k`), and
groups with `m·G` degenerate for some `m≤k` (the `p|k` / low-exponent regime, which is also where constancy
lives). These are exactly the small cases handled next.

### 2.6 Small-`q` closure by exhaustive computation — **NUMERICAL (exhaustive), reproduces both ground-truth
points**

`ksum/tools/ksum_stage2p_verify.py` enumerates `K` exhaustively (probe-then-**full**-verify over all `q^n` inputs)
and compares to `diag(Aff_{k,t})` at every feasible `n>k` point. **All match** (log; every assertion passed,
exit 0):

| G | k | t | n | `\|Aff_{k,t}\|` | `\|K\|`(brute) | `\|Aut\|=\|K\|·n!` | ground truth |
|---|---|---|---|---|---|---|---|
| Z2 | 3 | 1 | 4 | 1 | 1 | **24** | `B1`/`B3`: `(4,3,2,1)=24` ✓ |
| Z2 | 3 | 0 | 4 | 1 | 1 | 24 | — |
| Z2 | 3 | 0/1 | 5 | 1 | 1 | 120 | — |
| Z2 | 4 | 1 | 5 | 2 | 2 | 240 | — (`t=0,n=5` excluded: constant-1) |
| Z3 | 3 | 1 | 4 | 3 | 3 | 72 | — |
| Z3 | 3 | 0 | 4 | 6 | 6 | 144 | — |
| Z3 | 3 | 1 | 5 | 3 | 3 | 360 | — |
| Z4 | 3 | 1 | 4 | 2 | 2 | **48** | `B1`/`B3`: `(4,3,4,1)=48` ✓ |
| Z4 | 3 | 0 | 4 | 2 | 2 | 48 | — |
| Z2×Z2 | 3 | 0/1 | 4 | 6 | 6 | 144 | — (non-cyclic) |

Both Stage-0 ground-truth points (`(4,3,4,1)=48`, `(4,3,2,1)=24`) are reproduced. `|Aff_{3,1}(Z_4)|=2`
(`{(1,0),(3,2)}`) and `|Aff_{3,1}(Z_2)|=1` match Stage-0 `B3(0)`.

### 2.7 The `n=k` degeneracy is real and correctly excluded — **NUMERICAL, matches `B3`**

At `n=k` the overlap step (iii) is unavailable, and the constants `c_i` are only jointly constrained by
`Σc_i=t−u(t)`. The value-part group is the **H-degeneracy family**
`{ x_i↦u(x_i)+c_i : u∈Aut(G) common, Σ_{i}c_i=t−u(t) }`, of size `|Aut(G)|·q^{k-1}`. Verified: for
`(3,3,4,1)`, brute `|K|=32=|Aut(Z_4)|·4^{2}=2·16`, `|Aut|=32·3!=192` — exactly Stage-0 `B3(1)`, and strictly
larger than `|diag(Aff)|=2`. So Theorem 2's `n>k` hypothesis is **sharp**: it fails at `n=k`.

### 2.8 Verifying "additive bijection ⇒ automorphism" (flagged in the tasking) — **PROVED**

If `u:G→G` is a bijection with `u(x+y)=u(x)+u(y)` for all `x,y`, then `u` is a homomorphism of `(G,+)` into
itself, i.e. an endomorphism; being bijective it is an automorphism. (For finite `G`, injectivity alone
already forces surjectivity, so an additive injection suffices.) This is the only group-theoretic input to
step (ii) and it is elementary.

---

## 3. THEOREM 3 (the OA-generality barrier) — **PROVED**

### 3.1 Formalisation

A **k-OA instance** is a family `τ=(T_S)_{S∈binom([n],k)}` of index-1 length-`k` orthogonal arrays over
`[q]` (BS Def 2). Its function `f_τ:[q]^n→{0,1}`, `f_τ(x)=1 ⟺ ∃S: x_S∈T_S`, is the k-orthogonal-array
problem (BS `:116`); `Q(f_τ)` its quantum query complexity. BS **Theorem 5** (`BS:130–133`, verbatim):

> "For a fixed `k` and any choice of the orthogonal arrays `T_S`, the quantum query complexity of the
> `k`-orthogonal array problem is `Ω(n^{k/(k+1)})` provided that `q ≥ n^k`. The constant behind big-Omega
> depends on `k`, but not on `n`, `q`, or the choice of `T_S`."

**Definition.** A **`T_S`-uniform lower bound** (a "Theorem-5-type" bound) is a function
`B(k,q,n)∈ℝ_{≥0}` such that `Q(f_τ) ≥ B(k,q,n)` for **every** instance `τ` with those parameters. (BS
Theorem 5 is the instance `B=c_k·n^{k/(k+1)}`, asserted valid on the region `q≥n^k`.)

> **Theorem 3.** If, for parameters `(k,q,n)`, there exists an instance `τ*` whose function `f_{τ*}` is
> **constant**, then every `T_S`-uniform lower bound satisfies `B(k,q,n)≤0` (it is vacuous). Constant
> instances exist in the following regimes, so no `T_S`-uniform bound exceeds the trivial there:
> **(3a)** `k=2`, any `q`, `n>q`; **(3b)** any `k`, `q=p^m` with a prime `p∣k`, `n>(k−1)q`.

*Proof of the reduction.* A constant `f_{τ*}` has `Q(f_{τ*})=0`. Uniformity quantifies over all instances,
including `τ*`; hence `B(k,q,n)≤Q(f_{τ*})=0`. ∎

### 3.2 (3a) `k=2`, `n>q`: the Element-Distinctness array is constant — **PROVED**

`T={(x,x):x∈[q]}` is an index-1 length-2 OA (`|T|=q=q^{2-1}`; fixing either coordinate determines the other;
verified for `q=2..5`, log). Taking `T_S≡T` gives `f_τ(x)=1 ⟺ ∃i≠j: x_i=x_j`. For `n>q`, pigeonhole forces a
repeat, so `f_τ≡1` and `Q=0`. (Measured: constant-1 at `n=q+1` for `q=3,4,5`; non-constant at `n=q`, log.)
Thus for `n>q` no `T_S`-uniform bound exceeds `0`. Since BS's own regime is `q≥n^2`, this barrier sits at the
*opposite* end (`q<n`); it certifies that the alphabet condition **cannot be pushed below `q=n`** within
OA-generality. **The commission's §3.6/§4-Stage-2 claim "any small-q result must break the OA abstraction"
is thereby PROVED for `k=2`.**

### 3.3 (3b) general `k`, the `p∣k` trap: `q=p^m`, `n>(k−1)q` — **PROVED**

Let `p` be a prime with `p∣k`, `G=Z_p^m` (so `q=p^m`, `exp(G)=p∣k`), `t=0`, `T_S≡T={x∈G^k:Σx_i=0}` (Ex 3,
an index-1 length-`k` OA). Then `k·a=0` for all `a∈G` (as `p∣k`), so any value repeated `k` times is a
certificate; for `n>(k−1)q` some value repeats `≥k` times (pigeonhole), giving `f_τ≡1`, `Q=0`. (Measured
constant-1 at `n=(k−1)q` and `n=(k−1)q+1` for `k=3/G=Z_3`, `k=4/G=Z_2`, `k=6/G=Z_2`, log §"(3b)"; the true
threshold is `≤(k−1)q`, an EGZ-type constant.) Thus for `q=p^m` (`p∣k`) and `n>(k−1)q`, no `T_S`-uniform
bound exceeds `0`, i.e. `q≲n/(k−1)` is barred.

### 3.4 Exactly what is and is not covered, and the quantifier point — **PROVED / OPEN as labelled**

- **Covered (constant OA exhibited):** `k=2` at every `n>q` (3a); and for `k≥3`, the `q=p^m` ladders with
  `p∣k` at `n>(k−1)q` (3b). These are the "`p∣k` traps" the tasking names.
- **Not covered by these constructions (labelled OPEN whether a constant OA exists):** `k≥3` with `q`
  **not** of the form `p^m` for a prime `p∣k` — e.g. `q` coprime to `k`, or `q` not a prime power. The
  diagonal/ED trick does **not** generalise to `k≥3` (a "constant tuple" array `{(a,…,a)}` has size `q≠q^{k-1}`
  and is not an OA for `k≥3`), and the `p∣k` trap needs `exp(G)∣k`. So for those `(k,q)` the barrier via
  *constancy* is silent; I make **no** claim there.
- **Quantifier discipline (the crux).** Theorem 3 kills only **`∀τ`-uniform** bounds. It says nothing about a
  **fixed** instance: real k-Sum over a group `G` with `f` non-constant can (and does) have large `Q`. The
  barrier is precisely: *one constant `T_S*` inside the universal quantifier makes any uniform constant
  vacuous.* Any small-`q` k-Sum lower bound must therefore be **per-problem** (use `G`'s structure), which is
  exactly Rosmanis's "and, potentially, the structure" and Špalek `:425`. This matches, and formalises,
  Stage-0 §3.6.

---

## 4. WHAT I DID NOT CHECK (mandatory self-disclosure; per G1 this is *not* certification)

1. **Theorem 2 for every non-constant `n>k` instance with `(NC-ext)` unverified.** The proof needs `(NC-ext)`
   for **all** subsets/non-certificates; I proved it for `q>k·2^k` (field) and *exhaustively verified the
   full conclusion* only for `q∈{2,3,4}` groups `Z_2,Z_3,Z_4,Z_2×Z_2` (the feasible brute range, which
   includes both ground-truth points). **Whether Theorem 2 holds for every non-constant instance in the
   uncovered middle `k·2^k ≥ q` with `q` not brute-reachable (e.g. `Z_5,k=4`; large non-cyclic groups) is
   left OPEN.** No counterexample was found; the `n=k` case is the only place equality is known to fail.
2. **The exact constancy threshold for `k≥3`** (the EGZ/zero-sum constant of `(G,k)`): I gave the necessary
   condition `t=0∧exp(G)∣k` (proved) and the sufficient bound `n>(k−1)q` (proved); the exact value is OPEN
   and I did not compute it beyond spot measurements.
3. **`k≥4` automorphism points beyond `Z_2`.** Only `Z_2,k=4,n=5` was brute-forced (`|Aut|=240`); larger
   `k≥4` groups were not enumerated (wreath sizes explode). The proof covers them under `(NC-ext)`, but they
   are not independently brute-checked.
4. **Whether a constant OA exists for `k≥3` at `q` coprime to `k` (or non-prime-power `q`).** Theorem 3's
   barrier is silent there; I neither exhibited one nor proved none exists (G7: negative search ≠ proof).
5. **Exhaustive `K`-enumeration for `q=4,n≥5` and any `q≥5,n≥4`** — infeasible by brute; those points rely
   on the proofs, not on computation.
6. **`Aut(f)` outside `W`.** Only automorphisms inside the wreath group `W` were considered (the relevant
   ones for the adversary bound); permutations of `G^n` not preserving the `Δ_i` pattern were not studied.
7. **The probe-then-verify enumerator's completeness at the probe stage** is not a risk (every *reported*
   member is fully verified on all `q^n` inputs), but a *missed* automorphism would require it to fail all
   64 random probes — I did not separately prove the probe set is discriminating; the equality `|K|=|Aff|`
   with the independently-known containment `diag(Aff)⊆K` is what pins `K` exactly at each point.
8. I did **not** re-run Stage-0's `B1/B2/B3` scripts; I compared against their logged outputs (hashes in §5)
   and reproduced the same numbers with fresh independent code.

---

## 5. Provenance appendix

**Scripts (in `tools/`):**
```
573f70c8940a8e7a08c4b116fdf5d9170f65ea3c85d1f6e97e33409afbf733df  ksum_stage2p_verify.py
```
**Logs (in `ksum/artifacts/logs_ksum_stage2_20260716/`):**
```
cc6ac0132be916f8d1779c1fe89b484e273571f3f16c804ff3ac4d20a50f1dd8  S2P_verify.log
```
**Command (Windows PowerShell, from repo root or `tools/`):**
```
& "<machine-local-path-redacted>" ksum/tools/ksum_stage2p_verify.py `
    > ksum/artifacts/logs_ksum_stage2_20260716/S2P_verify.log 2>&1
```
Exit code 0; final log line "ALL ASSERTIONS PASSED." Every table number above is a `K(brute)=…` /
`|Aut|=…` line in that log.

**Ground-truth logs cross-checked (Stage-0, unchanged):**
```
9f4293a7178eae436a50e67ff7595c608075695dcfb1c6e0d5a91aa24936dc44  B1_aut_table.log
45d8871dd7a5f7f35982a854d6828ce89426d2f5d0abc1ef1499cebff64eb91f  B2_abc_centralizer.log
85f9140971f1a3f0d3d10b592c4a919992a14cf2e95d16d89f52fee4051b7487  B3_discriminating_4341.log
```
**Primary source:** `ksum/artifacts/references/BS_1206.6528v2_ksum.tex` SHA-256
`41fff42aab869c11fd77fb912245d2d5bd12d82e0eea4192a8755b22e0cd90d0` (Theorem 5 at lines 130–133; OA Def 2 at
110–112; k-sum triviality `BS:137`; Examples 3/4 at 120/124 — all read this session).

**Summary of labels.** Theorem 1: **PROVED** (all `n≥3`, all `G`, all `t`; four exhaustive cases; brute
cross-check at 20 points). Proposition 1.0 (k=2 constancy): **PROVED**. Theorem 2: **PROVED under (NC-ext)**,
with `(NC-ext)` **PROVED** for `q>k·2^k` (field, all `n`), and the full conclusion **NUMERICAL (exhaustive)**
at `Z_2,Z_3,Z_4,Z_2×Z_2` incl. both ground-truth points; `n=k` sharpness **NUMERICAL**; exact `k≥3` constancy
threshold **OPEN**. Theorem 3: **PROVED** (reduction + both witness families); uncovered `(k,q)` regimes and
existence of other constant OAs **OPEN**.
