# Independent review — `circdist_lift_iff_proof_20260820.md` and `circdist_lift_nonint_proof_20260820.md`

**Date:** 2026-08-20 · **Node:** `CIRCDIST.lift` · **Role:** fresh Opus 5 independent reviewer,
one budget-boxed session, no sub-agents.

---

## 0. Independence statement

I did not author, edit, or read any part of either document before this session, and I was given
no target verdict. My instructions were to try to refute. Before opening either target file I read
only the frozen 公共定义 (`research/circdist/notes/CIRCDIST_PROBLEMS.md`) and then wrote my own
derivation of (a) the measurement-consistency condition, (b) the hook/vertical-edge parity
argument, and (c) the contiguity ("no idle round") argument, to a scratch file, so that the
anchoring ban could be enforced against a written record rather than against memory. That
pre-reading derivation is reproduced verbatim in §6.1 below; the reader can check for himself that
it reaches Theorem 1's `≥ 4` and the contiguity split independently, and that the notational
agreement with the proposers (`c_ab`, `u`, `s`, suffix hooks) is *derived*, not inherited.

All numerical work below is my own code, written this session from scratch (§6.2). I did not run
any proposer code, did not import the d3-gate base layer, and did not use `stim`. My detector
layer, my fault-location inventory and my propagator are independent re-implementations; where my
numbers agree with the documents' this is a genuine second measurement, and where the fault-model
*design* is shared (Definition 1.8 / Definition 2.5) I say so and do not claim independence.

I touched no file other than this one. `research/circdist/proof-dag/` was not read or written.

Convention for verdicts, per (7f): **[V]** = I reconstructed the value/statement myself and it
agrees; **[D]** = I checked the printed derivation line by line; **[N]** = supported by my own
computation. Most entries carry more than one.

---

## 1. Headline verdicts

| # | statement | verdict |
|---|---|---|
| A | **Theorem 1** (iff-doc §3.2): under (MC), a hook of X-check `a` with `u_b = 1, s_b = 0` forces `\|supp(a) ∩ supp(b)\| ≥ 4` | **CONFIRM** [V][D][N] |
| B | **(MC) ⟺ deterministic detectors**, both directions (iff-doc §2.2, nonint §3.1) | **CONFIRM** [V][D] |
| C | **Sharpness at overlap 2** (iff-doc §3.4): vertical ⟺ `{p,p'} ⊆ S` and `c_ab = 1` | **CONFIRM** [V][D][N] |
| D | **Correction §3.5**: `u ⊆ s` at overlap ≤ 2 does *not* imply horizontal; diagonal hooks are abundant; withdrawal of the d3-gate `CIRCDIST.gross` lead | **CONFIRM** [D][N] |
| E | **Theorem 2 lower bound** (iff-doc 5.4, `\|F\| ≥ \|γ\| + min(repair,2)`, the `n_∅ + 2m` accounting) | **CONFIRM** [D][N] |
| F | **Theorem 2 upper bound** (iff-doc 5.3, `ℓ(γ) ≤ \|γ\| + repair(γ)`) | **GAP-AT-5.3** — printed justification is false and self-contradicted; value not refuted; one-paragraph fix exists and is already written in the sibling document |
| G | **The node's biconditional** (iff-doc 5.7): `d_circ = d_eff ⟺ some minimum-weight γ has repair(γ) = 0` | **CONFIRM** [D][N] — survives F, but the printed (⟸) needs the one-line repair in §3.2 |
| H | **Contiguity** (iff-doc 5.9): minimum-weight undetectable logicals occupy contiguous rounds, span ≤ weight ≤ d | **CONFIRM** [V][D][N] |
| I | **`R_sat(M) ≤ d`** (iff-doc 5.10(1), repeated unconditionally in §8.4) | **REFUTE as stated** — false under the frozen `R_sat` definition; explicit counterexample in §3.3. The salvageable statement (`d_R` constant for `R ≥ d`) is CONFIRM |
| J | **Boundary-freeness** (iff-doc 4.1; nonint 2.13 + Rmk 2.14) | **CONFIRM** [D][N] |
| K | **Theorem 7.1** (nonint): every legal non-interleaved single-ancilla CSS schedule has `d_circ = d_eff` for all `R ≥ 1`, without graph-likeness | **CONFIRM** [D][N] |
| L | **Horizontal-representative lemma** (nonint 5.4) and its case enumeration | **CONFIRM** [V][D][N] |
| M | **Collision handling** (nonint Def. 2.8 + Lemma 7.2) | **CONFIRM** [D] — and it is the correct treatment of exactly the defect in F |
| N | **`R_sat ∈ {1,∞}` for non-interleaved** (nonint Cor. 7.3) | **CONFIRM** [D][N] — and it *contradicts* the iff-doc's I |
| O | `repair ≥ 3` regime, (ESC), gadget completeness (iff-doc §7.2) | **NOT-REVIEWED** (declared open by the authors; I confirmed only that the pair gadget is realisable, §2.9) |
| P | Proposer numerics at scale: the 98 811-schedule surface scan, the 349/349 Steane sweep, the 3 855/3 855 end-to-end run | **NOT-REVIEWED** as such; qualitatively reproduced at smaller scale by my own code (§4) |

Both documents carry an explicit epistemic ceiling ("nothing is labelled PROVED"). That ceiling is
respected throughout, and in the iff-doc's §7.4 the authors correctly nominate 5.4(3) and 5.10(3)
as likely error sites. **They did not nominate 5.3, which is where the one real defect is.**

---

## 2. Type audit and the anchoring-ban re-derivations (7a, 7c)

### 2.1 (MC), re-derived before reading

Spaces: `t(a→q), t(q→b) ∈ Z` are gate times in one round; `q` ranges over `supp(a) ∩ supp(b) ⊆ [n]`;
outputs live in `F₂`. Pulling `Z_{anc(b)}` back through the round: each CNOT `q→b` (target `b`)
emits `Z_q`; each `Z_q` pulled further back through `a→q` (target `q`) emits `Z_{anc(a)}` exactly
when `t(a→q) < t(q→b)`. So the measured observable is

```
   M_B = Z_b · Z_{anc(a)}^{ #{q : t(a→q) < t(q→b)} } ,   M_A = X_a · X_{anc(b)}^{ #{q : t(q→b) < t(a→q)} }.
```

`|supp(a) ∩ supp(b)|` is even (CSS), so the two exponents are equal mod 2. If the common parity is
odd, `M_A` and `M_B` **anticommute** (`X_a, Z_b` commute; `X_{anc(b)}, Z_{anc(b)}` do not), so the
two outcomes cannot both be deterministic — this is a cleaner "only if" than invoking the
measurement rule against the fresh ancilla state, and it is the *same* argument the iff-doc gives
only as a parenthetical consistency check in Step 1. If the parity is even, `M_B = Z_b`, `M_A = X_a`.

This is exactly Definition 2.1 / Proposition 3.1. **CONFIRM [V][D].** Notational coincidence
(`c_ab`) is a coincidence: I obtained the complementary count `χ(q) = [t(a→q) < t(q→b)]` and only
afterwards saw that the documents count the other side and then prove the two agree.

One scope boundary worth stating: (MC) is necessary for the *standard per-check detector*
construction of Definition 1.6 / 2.7. A schedule failing (MC) is not merely inconvenient — the two
ancillas' measured observables anticommute, so no relabelling of detectors rescues either check
alone. Both documents state this correctly; the iff-doc's §2.3 ("load-bearing rather than
hygienic") is right for Theorem 1 specifically, since Theorem 1's conclusion is *false* without it
(§4.1 below: 37 339 explicit overlap-2 vertical hooks in non-(MC) schedules).

### 2.2 The overlap parity argument, re-derived before reading

Types: `S ⊆ supp(a)` is a suffix of `a`'s CNOT order (`F₂^n` when convenient); `u(S), s(S) ∈ F₂^ℬ`;
`P = supp(a) ∖ S`. The X error reaches data qubit `q ∈ S` at time `t(a→q)`, **not** at the fault
time — this is the one place an off-by-one would be fatal, and both documents get it right
(iff 1.13.2, nonint 5.2's `θ_i(q)`). Hence

```
   s_b(S) = |supp(b) ∩ S| mod 2 ,    u_b(S) = #{q ∈ supp(b) ∩ S : t(q→b) > t(a→q)} mod 2,
   u_b(S) + s_b(S) = #{q ∈ supp(b) ∩ S : t(q→b) < t(a→q)}   (legality: no ties, Rmk 1.4),
```

and under (MC) the two complementary counts over `S` and over `P` sum to `c_ab = 0`, so
`u_b + s_b` is read off `P`. Then `u_b = 1, s_b = 0` ⟹ `|supp(b) ∩ S|` even and non-zero (`≥ 2`)
and `supp(b) ∩ P ≠ ∅` (`≥ 1`), so the overlap is `≥ 3`, hence `≥ 4` by CSS parity. **Identical to
§3.1–§3.2.** CONFIRM [V][D].

Round indices: Theorem 1 involves no round index at all — it is a statement about one round's
timestamps. The documents say so (§3.2 status line, "Not used: ... `R`, the boundary conditions").
Correct.

**Scope boundary, stated because the documents equivocate slightly.** Theorem 3.2's hypothesis is
the *per-pair* condition `u_b(S) = 1 ∧ s_b(S) = 0`. Definition 1.12's "vertical" is the *global*
condition `s(S) = 0 ≠ u(S)`. Per-pair is the weaker hypothesis, so Theorem 3.2 is the stronger
theorem — good. But NUMERICAL 3.6's table row "VERTICAL (`s = 0 ≠ u`)" measures the *global*
version, so that table does not test the theorem's actual hypothesis. I tested the per-pair version
(§4.1) and it survives; the table's `0` is therefore true but weaker than advertised. Flag, not a
defect.

### 2.3 The horizontal-representative lemma, re-derived before reading

For a Z-block-first schedule every `q ∈ S` receives its X at `t(a→q)`, which is after every
`t(q→b)`, so `u(S) = 0`; and a bare `{q}` can be given `u = 0` by inserting the X after `q`'s last
Z-CNOT. For X-block-first the mirror gives `u = s`. The *uniformity* of the flavour across all
residual classes simultaneously is the content, and it is what makes `Σ_i u_i` either `0` or
`∂_eff γ = 0`. This is nonint Lemma 5.4 and iff §5.11, reached independently. CONFIRM [V].

Type check on the assembled witness: `ι_r([E]) = x^r e_{σ(E)} ∈ C₁^{(R)}`, `∂ι_r = x^r ∂_eff`
(X-first) or `x^{r+1} ∂_eff` (Z-first). The two cases land in *different* detector slices; the
iff-doc's Remark 6.4 analogue (§5.8 `k = 1` branch) has the order `u = 0` first, `u = s` second and
notes the reverse does not close — I verified that asymmetry symbolically: with `A` in round `r`
(`u = 0`) and `B` in round `r+1` (`u = s`), `∂ = x^{r+1} Σ_γ s_i = 0`; with the assignment
reversed, `∂ = x^r Σ_B s_i + x^{r+2} Σ_A s_i`, which vanishes only if each half is separately a
cycle. Correct as printed.

### 2.4 `d_eff` / `d_circ` against the frozen definitions

`d_eff(M) := d_ext(E(M))` and `d_circ(C) = min{|F| : F` triggers no detector, flips a nontrivial
logical`}`, with `d_eff ≤ d_circ ≤ d`. Both documents index `C₁^eff` by **residual classes** `ℰ`,
not by fault types (iff Def. 1.16, nonint Def. 2.11 + Sharpening 0.3.1). This is the correct
reading of `d_ext` and it is *necessary* for `π₁` to be weight-non-increasing; indexing by fault
type would break the `≥` direction. Both documents flag this explicitly. Correct.

`|γ|` counts residuals, not qubits (iff §7.4.3). Correct and consistent with the 公共定义.

The 公共定义 asks for the criterion "in the graph-like, fixed-boundary model". Both documents
deliver something *stronger* (no graph-likeness). That is a legitimate over-delivery, not a scope
violation, and both say so rather than enjoying it silently. I verified the claim that
graph-likeness is unused by attempting to find a step that needs `|u| + |u+s| ≤ 2`: Definition 1.12
appears only in Lemma 7.1, Definition 2.17 nowhere. Confirmed by inspection, and corroborated by
running Theorem 7.1 on codes that are not graph-like (§4.4).

---

## 3. The three findings

### 3.1 GAP-AT-5.3 — the iff-doc's `≤` direction rests on a false claim it contradicts itself on

iff-doc §5.2, Lemma 5.3, says of the `|γ|` essential faults:

> "these are `w = |γ|` distinct circuit locations, since **distinct residuals force distinct
> locations**."

This is false, and the document proves it false three pages earlier. Its own Proposition 1.13.4
reads:

> "on a gate `a→q_j` the possible residuals are `∅, S_j, {q_j}, S_{j−1}`"

— four distinct residuals at one location. Since Definition 1.8 (and the frozen fault model) puts
**one Pauli per location**, two of those cannot be placed as two weight-1 faults; the `X⊗X`
composite is a *single* weight-1 fault whose residual is `S_{j−1}`, and whose `π₁` image is the
basis vector `[S_{j−1}]`, not `[S_j] + [{q_j}]`.

The same conflation is baked into Definition 5.1, which defines
`ℓ_R(γ) := min{|F| : F ⊆ 𝔽 × {0,…,R−1}, ∂F = 0, π₁F = γ}` — a minimum over *formal subsets of
(fault type) × (round)*, which is not the same as a minimum over realisable fault configurations.
The `≥` direction is unaffected (a real configuration has at most one type per location, so it *is*
such a subset). Only the `≤` direction, and hence Theorem 5.6(b)'s upper bound and 5.6(c)'s
equality, are exposed.

**Status of the value.** Not refuted. I searched for a *forced* collision — a pair
`(E₁,u₁) ≠ (E₂,u₂)` whose realising-location sets are both singletons and equal — over 180 legal
measurement-consistent schedules on three codes. Result: **every one of the 180 schedules has some
`(E,u)` pair sharing a location**, but **zero** forced collisions; there was always an alternative
representative. And the empirical sandwich/equality held 282/282 (§4.3).

**The fix already exists in the sibling document.** nonint Def. 2.8 states the per-location weight
convention explicitly, and nonint Lemma 7.2 (i) enumerates the collisions that can actually occur
under the chosen representatives (only `S_a(j)` vs `{q_j}` at the gate `a→q_j`), and (ii) shows that
if both lie in `γ` then `γ' := γ + [S_a(j)] + [{q_j}] + [S_a(j−1)]` is an effective logical of weight
`≤ |γ| − 1`, contradicting minimality. I checked that enumeration is exhaustive under nonint Lemma
5.4's choices (prep(`a`) carries only `S_a(0)`; idle(`q`,0) carries only `{q}`; gate `a→q_j` carries
`S_a(j)` and `{q_j}`), and that the `γ'` algebra is right (`s` and `λ` are `F₂`-linear in the
residual vector, `S_a(j) + {q_j} = S_a(j−1)`, and all three classes are distinct for `j ≤ w_a − 1`).
**CONFIRM for nonint Lemma 7.2.**

**Recommended edit to the iff-doc (one paragraph).** Replace the false sentence in 5.3 with:
"either the chosen representatives occupy `|γ|` distinct locations, or two of them collide, in
which case composing them at that location yields a fault set of weight `< |γ| + wt(D)` with the
same detector chain (`∂` is additive at a common location) and the same `λ`; the bound
`d_circ ≤ |γ| + repair(γ)` then holds a fortiori, and `ℓ(γ)` should be defined over realisable
configurations." Note that this weakens the statement about `ℓ(γ)` *for a fixed `γ`* while leaving
every downstream use intact.

### 3.2 The biconditional 5.7 survives the gap — but the printed (⟸) does not say why

`(⟹)` does not use 5.3 at all and is correct as printed (I re-checked: `|γ| = d_eff` forces
`n_∅ = 0` and `m = 0`, hence `A_∅ = 0`, hence `A_ess + xC = 0` by (LIFT), hence `repair(γ) = 0`).

`(⟸)` cites 5.3. It does not need it in full: it needs only *some* undetectable logical of weight
`≤ d_eff`. If a collision occurs, compose the two colliding Paulis at their common location. The
composite is a legal elementary fault (the 15 two-qubit Paulis include `X⊗X`); `∂` is additive at a
common location and round, so the configuration stays undetectable; `λ` is the parity of
`Σ_f E(f)`, which is unchanged. The result has weight `≤ |γ| − 1 = d_eff − 1`, so
`d_circ ≤ d_eff − 1`, contradicting `d_circ ≥ d_eff` (5.4(1)) — i.e. the collision cannot occur, and
either way `d_circ ≤ d_eff`. **The conclusion is safe; add this line.** Same remark applies to
§5.11.

### 3.3 REFUTE as stated — `R_sat(M) ≤ d`

iff-doc §5.10(1): "`d_R(M)` is non-increasing in `R` and **constant for all `R ≥ d`**; i.e.
`R_sat(M) ≤ d` in the sense of `CIRCDIST.sat`, for this model." Repeated without qualification in
§8 item 4: "`R_sat(M) ≤ d` for every single-ancilla CSS schedule with ideal boundaries, per sector."

The frozen definition (公共定义, 课题四) is

```
   R_sat(M) = min{ R_0 : d_R(M) = d  for all R ≥ R_0 },     = ∞ if no such R_0.
```

Saturation is at the **code distance `d`**, not at `lim_R d_R`. Contiguity gives the latter. When
`d_∞(M) < d` — the generic hook-damaged case — `R_sat(M) = ∞`, not `≤ d`.

**Explicit counterexample, computed this session.** Steane `[[7,1,3]]`, natural within-check orders
`X_i = Z_i = supp` in index order, non-interleaved (either block order), legal, `MC = ∅`:
`d_eff = 2 < 3 = d`, and my exhaustive weight-`≤3` search gives `d_R = 2` for `R = 1,2,3,4`. Hence
`R_sat = ∞`. The claim `R_sat ≤ d = 3` is false here. (Twelve further non-interleaved
configurations in §4.4 with `d_eff < d` are additional witnesses.)

**The sibling document gets this right and the two contradict each other.** nonint Corollary 7.3:
"`R_sat(M) = 1` if `d_eff(M) = d`, `R_sat(M) = ∞` if `d_eff(M) < d`." That is correct. The
iff-doc's §5.10(1) should be restated as: *`d_R` is constant for `R ≥ d`, with limiting value
`d_∞`; consequently `R_sat ≤ d` when `d_∞ = d` and `R_sat = ∞` otherwise, and in either case
`R_sat` is decided by finitely many `R`.* The finite-window content (`B(r,d) = d`) is untouched by
this correction and is a real `CIRCDIST.sat` deliverable — the error is only in the identification
with `R_sat`. A `CIRCDIST.sat` session adopting §8 item 4 verbatim would adopt a false statement,
which is why I am recording this as REFUTE-as-stated rather than as a wording nit.

### 3.4 Two smaller precision defects

**(a) "Every gross-code hook has `|s| ≥ 3`" (iff §8 item 3(ii), from NUMERICAL 3.7).** My
independent rebuild of the gross code (`ℓ=12, m=6, A = x³+y+y², B = y³+x+x²`) reproduces the
overlap histogram `{0: 4536, 2: 648}` exactly, and the syndrome-weight histogram
`{3:12, 4:18, 5:18, 6:12, 9:2}` over the 62 **proper** non-empty subsets of an X-check support. The
63rd subset, `S = supp(a) = S_a(0)`, has `|s| = 0`. So the literal statement "every gross-code hook
has `|s| ≥ 3`" is false for the full-support hook. It is harmless (that residual is a stabilizer:
`s = 0`, `λ = 0`, so it never enters a `γ`), but this is being registered as a cross-node premise
for `CIRCDIST.gross` and should read "every *proper* hook".

**(b) X-check detector index range (iff Def. 1.6).** "the Z-memory carries X-check detectors
`D_{a,r} = m_{a,r} + m_{a,r−1}` for `r ≥ 1` only" — the upper limit `r ≤ R−1` is missing (there is
no `m_{a,R}`; the terminal readout is Z-basis). nonint Def. 2.7 states the range correctly. Harmless
because sector decoupling removes X-check detectors from the Z-memory argument entirely, but it is
the kind of index slip (7e) that matters if anyone reuses Definition 1.6.

---

## 4. Attacks on the absence-type steps (evidence-asymmetry axiom)

Witness-type steps ((MC) fails ⟹ some schedule breaks; a diagonal hook exists; the pair gadget
exists) I checked by exhibiting the object. The list below is the absence-type steps — "no
counterexample exists", "all cases covered" — with the scope boundary of each and whether it
survives.

### 4.1 Theorem 1 — "no vertical hook at overlap ≤ 2"

*Scope:* one round, one `(a,b)` pair, legality (no ties) + (MC) + CSS parity. No `R`, no
boundary conditions, no graph-likeness, no code distance.

**Attack 1 — exhaustive at the abstract level.** Theorem 1 depends on the schedule only through
(i) which overlap qubits lie in the suffix `S` (necessarily a suffix of the overlap in `a`'s order)
and (ii) the bit `χ(q) = [t(q→b) > t(a→q)]` for each overlap qubit. I enumerated **all** such
configurations for overlap sizes `m = 0,2,4,6,8`:

```
m   #(u_b=1, s_b=0) under (MC)   #(u_b=1, s_b=0) without (MC)
0            0                              0
2            0                              2
4            4                             12
6           32                             64
8          192                            320
```

Zero at `m ≤ 2` under (MC); non-zero at `m ≥ 4`. This is a **complete** verification of Theorem 1
over all codes and all schedules simultaneously, conditional only on the propagation inventory
1.13.2 (which I verified separately by gate-level simulation, §4.2). It also shows the threshold is
tight. **Survives.**

**Attack 2 — real schedules.** 2 156 legal measurement-consistent random schedules on Steane
(overlaps `{4:3, 2:6}`), rotated surface `[[9,1,3]]` (`{2:8, 0:8}`) and `[[4,2,2]]` (`{4:1}`):
zero vertical hooks at overlap `< 4`; the 608 vertical hooks that do occur are all at overlap
exactly 4. Dropping (MC): **37 339** vertical hooks at overlap 2 appear immediately. So (MC) is
load-bearing exactly as §2.3 claims. **Survives.**

**Attack 3 — the overlap-2 iff (Lemma 3.4).** The 12-row table for `m = 2` (§6.2) matches the
claimed equivalence exactly: `u_b = 1 ∧ s_b = 0 ⟺ {p,p'} ⊆ S ∧ c_ab = 1`. **Survives.**

### 4.2 The suffix classification (nonint §4, Lemma 4.1) and the propagation inventory (iff 1.13)

*Scope:* any schedule, interleaved or not; single-ancilla CSS; the fault menu of Def. 2.5/1.8.

The claim is an "everything else is impossible" claim: `ℰ ∪ {∅}` is exactly
`{∅} ∪ {singletons} ∪ {suffixes of X-check orders}`. The proof partitions by which qubit the X
lands on (Z-ancilla → `∅`; X-ancilla → a suffix; data → a singleton) and closes the 2-qubit case
with `S_a(j) + {q_j} = S_a(j−1)`. I checked the partition is exhaustive given Def. 2.5's location
list, and then measured it: over 180 legal (MC) schedules on three codes, **1 994 / 1 994** realised
residual classes are singletons or X-check suffixes, zero unclassified. **Survives.**

The associated absence claim **(V)** `U(∅) ⊆ {0} ∪ {e_b}` — the single point the iff-doc identifies
as carrying the whole lower bound — I attacked directly: **440 / 440** distinct empty-residual
voltage vectors across those schedules have weight `≤ 1`. Structurally the reason is that a 2-qubit
fault lives on one CNOT, whose two qubits are never two Z-ancillas, so no elementary fault can put
`X` on two Z-ancillas at once. **Survives.** (The iff-doc's §7.3 warning that multi-ancilla/flag
schedules would break it is correct and important.)

### 4.3 The `n_∅ + 2m` projection-loss accounting (iff 5.4)

*Scope:* any undetectable observable-flipping `F` in `C_R(M)`; needs the ideal terminal readout and
(V); does **not** need (MC), graph-likeness, or non-interleaving.

Line-by-line reconstruction, all four parts:

1. `λ_circ = λ_eff ∘ π₁` **as an identity of linear maps**, because the observable is a functional
   of `Σ_f E(f)`, which is the image of `π₁F` under `[E] ↦ E`. So `λ(F) ≠ 0 ⟹ π₁F ≠ 0`. This is
   the step that answers the systolic-non-monotonicity warning, and Remark 5.5 is right that a
   general chain map between spacetime complexes with independently defined observables would not
   have it. Correct.
2. `|F| = n_∅ + Σ_{E≠∅} n_E`, `|γ| = #{E : n_E odd}`, `Σ_{E≠∅}(n_E − [n_E odd]) = 2m`. Correct.
3. `wt(A_∅) ≤ n_∅` by (V); `A_∅ = A_ess + xC` by (LIFT); so `n_∅ ≥ wt(A_ess + xC)`. Correct.
4. `m = 0` ⟹ the faults with non-empty residual are one per `E_i`, so `(r_i, u_i)` *is* a repair
   certificate and `wt(A_ess + xC) ≥ repair(γ)`; `m ≥ 1` ⟹ `|F| ≥ |γ| + 2`. Correct.

I also checked the boundary hazard the accounting could have hidden: the repair monomials added in
5.3 live in `[r_min, r_max] ⊆ [0, R−1]`, because `C = B/(1+x)` has support in `[r_min, r_max − 1]`
(`Σ_i s_i = 0` kills the tail) so `xC` cannot reach slice `R`, where there is no `m_{b,R}` to flip.
The construction therefore never asks for a measurement flip that does not exist. The documents do
not say this; it is true, and worth adding.

**Measured.** 282 (schedule, `R`) instances across Steane / rotated surface / `[[4,2,2]]`, `R ∈ {2,3}`,
every one legal and (MC):

```
   sandwich  |γ| + min(repair,2) ≤ d_circ ≤ |γ| + repair   : 282 / 282
   equality  d_circ = min_γ (|γ| + repair(γ))               : 282 / 282
   biconditional 5.7                                        : 282 / 282
   §5.8 closed form for |γ| = 2 vs my brute-force repair     : 331 / 331
```

All of these sit in `repair ∈ {0,1}`, i.e. inside the regime where 5.6(c) is a theorem — so, exactly
as the iff-doc's §7.2 says, this is evidence about the *implementation*, not about (ESC). I did not
find an instance with `repair ≥ 3` (that needs `d ≥ 5`). **Survives, with the scope boundary the
authors already state.**

### 4.4 The contiguity deletion argument (iff 5.9)

*Scope:* minimum-weight `F`; needs the initial detector `D_{b,0}` to pin the (LIFT') constant to 0
(the document says so, correctly — with noisy initialisation the lemma fails at the first
boundary); does not need (MC) or graph-likeness.

I derived the same argument before reading (§6.1): a fault-free round forces the accumulated
residual to be syndrome-free there, the two halves are then separately undetectable, and one of
them carries the logical class. The printed version does it through (LIFT') with the correct
index bookkeeping (`c_b(r−1) = 0` and `c_b(r) = 0`); I re-checked the two directions of the split
(`r' ≤ r` and `r' > r`) and both are right. Note the argument needs *round* to be a well-defined
attribute of every fault, which it is (Def. 1.8/2.5 locations are per-round).

**Measured: 203 186 / 203 186** minimum-weight undetectable logical fault sets, found by exhaustive
weight-`≤3` enumeration across the 282 instances at `R = 2,3`, occupy a contiguous block of rounds.
Zero exceptions. **Survives.**

### 4.5 The horizontal-representative lemma's case enumeration (nonint 5.4)

*Scope:* non-interleaved only; this is the one step that uses the hypothesis, and §8.1 correctly
identifies it as the step that fails under interleaving.

The enumeration is: X-first — `S_a(j)` for `1 ≤ j ≤ w_a − 1`, `S_a(0) = supp(a)`, `{q}` with
`q` in some X-check, `{q}` in no X-check; Z-first — the same four with the extra clause "acts only
on X-ancillas" carrying the `S_a(j)` and `S_a(0)` cases (needed because the X-ancilla's *preparation*
need not lie inside the X-block — a real corner, correctly closed), plus a sharper singleton case
using `q`'s own last Z-CNOT rather than `τ'`. Together with Lemma 4.1 this is exhaustive over `ℰ`.
The X-first `{q}`-in-no-X-check case needs an idle location at step 0, which exists because
`𝒳 ≠ ∅ ⟹ τ ≥ 1`; the `𝒳 = ∅` degenerate case is routed to the other branch. I checked all of
these and found no hole. The iff-doc's §5.11 covers the same ground more briefly and its
self-declared "one corner" footnote is the same corner, also correctly closed.

**Measured: 180 non-interleaved configurations** (Steane, rotated surface, `[[4,2,2]]` × 30 random
within-check order sets × both block orders): every residual class has a representative of the
predicted flavour — `u = s` on X-first, `u = 0` on Z-first — **0 failures**, both flavours.
**Survives.**

### 4.6 Theorem 7.1 itself, and settlement S1 (no graph-likeness)

**Measured: 112 non-interleaved configurations across four codes, at `R = 1,2,3,4`,
`d_circ = d_eff` in every case.** The fourth code is a `[[15,7,3]]` CSS code built from the
`[15,11,3]` Hamming parity-check matrix (`H_X = H_Z = H`), chosen because it is emphatically outside
the graph-like model: every data qubit has Z-degree 4, so a bare data error fires four detectors,
and the check overlaps are `{4: 12, 8: 4}` — far outside the surface/Steane regime that the campaign
has been testing. 40/40 configurations there give `d_circ = d_eff` at `R = 1,2`. This is a direct
test of settlement S1 in the regime where it claims to matter. **Survives.**

I also independently confirm S1's motivating facts: Steane's Z-memory sector is not graph-like
(qubit 6 has Z-degree 3), and the **gross code** has *every* data qubit of Z-degree exactly 3, so it
is not graph-like either — so the use of "non-interleaved ⟹ `d_circ = d_eff`" for the gross code
does require a proof that does not assume graph-likeness. That part of the S1 argument is correct
and materially useful.

### 4.7 Sector decoupling (iff 1.9, nonint 2.10)

*Scope:* absence claim — "no full-Pauli fault set beats the best X-sector one".

Rather than re-reading the argument only, I built a **full two-sector simulator** (X and Z frames,
Z-check detectors on `𝒵 × {0,…,R}`, X-check detectors on `𝒳 × {1,…,R−1}`, all 3 single-qubit and
15 two-qubit Paulis, plus both kinds of measurement flip) and computed `d_circ` by exhaustive
search over the full fault set, then compared with the X-sector-only value. **12 / 12 agreements**
on `[[4,2,2]]` at `R = 2,3` (up to 492 (location × Pauli × round) items per instance), including
both `d_circ = d_eff` and `d_circ > d_eff` instances. **Survives.**

### 4.8 Boundary-freeness (iff 4.1, nonint 2.13)

*Scope:* ideal `|0⟩^n` initialisation and ideal transversal Z readout, both of which the 公共定义
supplies; the documents correctly say the lemma dies without either.

The claim is that `∂(f,r) = x^r u_f + x^{r+1}(u_f + s_f)` holds **at both temporal boundaries with
no correction term**, so truncation to `R` rounds is isometric rather than a quotient. I tested this
by full gate-level multi-round simulation of every elementary X-sector fault at every round:

```
   Steane X-first  R=1: 141/141   R=2: 282/282   R=3: 423/423
   Steane Z-first  R=1: 141/141   R=2: 282/282   R=3: 423/423
```

Every fault's detector set was exactly the predicted two-slice pattern, including `r = 0` (where
`D_{b,0} = m_{b,0}` absorbs the `m_{b,−1} := 0` convention) and `r = R−1` (where `D_{b,R}` absorbs
the ideal readout), and the observable value matched `λ_i` in every case. `F₂`-linearity of the
composite was separately checked on 400 random 2- and 3-fault configurations against the full
simulation: **400/400**. **Survives.** This is the standing failure mode (7e) "boundary rounds
silently inheriting bulk formulas" — here the bulk formula is genuinely correct at the boundary,
and the reason (both boundary detectors exist and are deterministic) is stated correctly in both
documents.

### 4.9 The diagonal-hook regime `0 ⊊ u ⊊ s` (7e), checked against the theorems themselves

The iff-doc's §3.5 is the campaign's own correction of a prior misreading, so I checked it hardest.

- The explicit witness printed in §3.5 reproduces **exactly** in my code: the schedule is legal with
  `MC = ∅` at depth 8, and the hook of `XB` with `S = {6,7}` has `s = (0,1,0,1)`, `u = (0,0,0,1)` on
  `(ZA,ZB,ZC,ZD)`; `t(7→ZB) = 2 < t(XB→7) = 3` gives `u_{ZB} = 0` and `t(6→ZD) = 7 > t(XB→6) = 2`
  gives `u_{ZD} = 1`. So `0 ⊊ u ⊊ s`: diagonal, time-voltage 1, at a code whose maximum overlap is 2.
- At scale: over 3 000 legal (MC) rotated-surface schedules, the 36 000 hook classes split
  `{trivial 12 000, horizontal-early 10 369, horizontal-late 10 076, DIAGONAL 3 555, VERTICAL 0}`.
  Diagonals are abundant; verticals are absent, as Theorem 1 requires. The correction is right and
  the withdrawal of the "no gross-code hook can carry timelike voltage" lead is warranted.
- **Do the theorems survive their own correction?** Theorem 1 is only about verticals, so yes.
  Theorem 7.1 never classifies hooks at all — it needs only that *some* representative of each class
  is horizontal, and diagonal representatives of the same class are irrelevant; nonint's Sharpening
  0.3.4 and Settlement S2 say exactly this and my 180/180 measurement confirms the distinction is
  real (both documents measure 27–31 % non-horizontal *faults* while 100 % of *classes* have a
  horizontal representative). Theorem 2 works with `U(E)` as a set and so absorbs diagonals by
  construction. **All three survive the diagonal regime.**

### 4.10 The interleaved gap instance, reproduced independently

To make sure the biconditional is not vacuously true on the instances tested, I searched my own
random legal-(MC)-interleaved Steane schedules for `repair > 0` and found three at depths 7, 8, 10:
`d_eff = 2`, every minimum-weight `γ` has `repair(γ) = 1`, predicted `d_circ = 3`, and my exhaustive
enumeration gives `d_R = 3` for `R = 1,2,3,4,5`. This independently reproduces the campaign's
headline `g(C) = 1` phenomenon and the nonint §8.1 mechanism: on each of the three, the residuals
with *no* horizontal representative are exactly the ones that appear in the minimum-weight `γ`
(e.g. depth 8: obstructed `{1,2}, {3,4}, {2,4}`; minimum-weight `γ`s
`{0}+{1,2}`, `{0}+{3,4}`, `{5}+{2,4}`, …). **Confirms both documents' account of the gap.**

---

## 5. Residual concerns that are not defects

1. **The `repair ≥ 3` gap is real and the authors say so.** iff §7.2 is an honest, well-localised
   statement of what is open. I confirmed the pair gadget is realisable: the Steane residual `{6}`
   has `|s| = 3` and admits both `u = 0` and `u = s = (1,1,1)` in **40 / 40** measurement-consistent
   schedules I generated, so 5.6bis's "two faults repair three units at cost two" is not vacuous, and
   the recommendation to target the min-cost-covering form rather than the plain count is sound.
   Lemma 7.1's three-case algebra (`|s| = 0,1,2` under graph-likeness) I checked and it is correct.
2. **Shared model design is not independence.** iff §9.7 says this itself. My re-implementation
   shares Definition 1.8/2.5's *design* (which locations exist, which Paulis are available), so a
   systematic modelling error against `stim`'s conventions would survive my check too. I did not run
   `stim`. The one thing I can say is that the full two-sector search (§4.7) rules out an error of
   the "you forgot the Z sector" kind.
3. **`k > 1`.** Both documents fix a single observable `Z_L` (nonint Def. 2.1) or a vector `λ ∈ F₂^k`
   (iff Def. 1.10) and then use "`λ ≠ 0`". The arguments are insensitive to `k`; my tests used
   `k ≥ 1` codes including `[[4,2,2]]` (`k = 2`) and `[[15,7,3]]` (`k = 7`) with a single chosen
   observable, which is the conservative direction (a per-observable distance upper-bounds nothing
   incorrectly). Not a concern, but not exhaustively tested either.
4. **iff 5.10(3)** is flagged by its own status line as complete only in a weaker reading. I agree
   with the authors' assessment and did not push on it; it is not used by (a)–(d).
5. **The `321 059 / 321 059` symmetry** in NUMERICAL 3.6 between horizontal-early and horizontal-late
   counts is exactly equal, which is either a genuine time-reversal symmetry of the schedule family
   or a coincidence worth a sentence. I did not reproduce that scan (my own surface numbers,
   10 369 vs 10 076, are *not* exactly equal on a differently-generated family). NOT-REVIEWED.

---

## 6. Code

### 6.1 My pre-reading derivation (written before opening either target file)

```
X-check a: ancilla A prep |+>, A is CONTROL of CNOT(A -> q); measured in X.
Z-check b: ancilla B prep |0>, B is TARGET of CNOT(q -> B);  measured in Z.
For q in supp(a) cap supp(b): chi(q) = 1 iff t_a(q) < t_b(q).

(MC), my derivation
  Pull back Z_B: each CNOT(q->B) contributes Z_q; each Z_q pulled back through an EARLIER
  CNOT(A->q) contributes Z_A.   =>  M_B = Z_b * (Z_A)^{sum_q chi(q)}
  Similarly                          M_A = X_a * (X_B)^{sum_q (1-chi(q))}
  |supp(a) cap supp(b)| EVEN (CSS) so the two parities agree.
  Parity ODD  => M_A and M_B ANTICOMMUTE => both outcomes random => schedule ILLEGAL.
  Parity EVEN => M_A = X_a, M_B = Z_b.
  (MC): #{ q in overlap : a acts before b } EVEN.    [both directions]

Vertical-edge criterion, my derivation
  X-hook of a at fault time tau: S = { q in supp(a) : t_a(q) > tau }.
  X_q appears at TIME t_a(q), not tau; so b's round-t0 outcome is flipped by q iff chi(q)=1.
    D_b^{(t0)}   flipped iff |{ q in S cap supp(b) : chi(q)=1 }| odd
    D_b^{(t0+1)} flipped iff |{ q in S cap supp(b) : chi(q)=0 }| odd
  "vertical on b" needs BOTH odd => |S cap supp(b)| even and >= 2, with >=1 of each chi value.
  If |supp(a) cap supp(b)| = 2 = {p,q}: (MC) forces chi(p)=chi(q) => impossible.
  => overlap 0 and 2 impossible; overlap even => overlap >= 4.

Contiguity, my sketch
  If min-weight undetectable F has a completely fault-free round in its span, the accumulated
  data error E there commutes with all checks, so E in S*L. Split F = F1 + F2. Each is
  separately undetectable (no detector receives contributions from both). One of them carries
  the nontrivial logical class => a strictly smaller undetectable logical unless the other is
  empty. Hence contiguous; span <= weight since each round in the span holds >= 1 fault.
  CAVEATS to check in the doc: faults straddling the round boundary; the special first round
  and the final ideal readout; whether a fault lives in exactly one round.
```

### 6.2 Exhaustive abstract verification of Theorem 1 and of Lemma 3.4

```python
from itertools import product
# Theorem 1 depends on the schedule only through (i) which overlap qubits lie in the suffix S
# (necessarily a suffix of the overlap in a's CNOT order) and (ii) chi(q) = [t(q->b) > t(a->q)].
# (MC): #{q in overlap : t(q->b) < t(a->q)} = #{chi = 0} is even.
for m in (0, 2, 4, 6, 8):
    with_mc = without = 0
    for chi in product((0, 1), repeat=m):
        mc = (sum(1 for c in chi if c == 0) % 2 == 0)
        for k in range(m + 1):                      # |S cap overlap| = k, a suffix
            sub = chi[m - k:] if k > 0 else ()
            s = k % 2
            u = sum(sub) % 2
            if u == 1 and s == 0:
                if mc: with_mc += 1
                else:  without += 1
    print(m, with_mc, without)
# ->  0 0 0 / 2 0 2 / 4 4 12 / 6 32 64 / 8 192 320
```

### 6.3 Core of the independent simulator

Full file: session scratchpad `rev.py` (≈340 lines). The load-bearing pieces:

```python
def run_round(sch, inserts):
    """X-frame propagation through one round. inserts = [(pos, ('d',q) | ('anc',name))],
       pos = number of time-ordered gates already executed. Returns (E, u)."""
    c = sch.code; xb = {}; G = sch.gates()
    def flip(k): xb[k] = xb.get(k, 0) ^ 1
    ins = {}
    for p, k in inserts: ins.setdefault(p, []).append(k)
    for k in ins.get(0, []): flip(k)
    for i, (kind, name, q, t) in enumerate(G):
        if kind == 'X':                                  # control anc(a) -> target data q
            if xb.get(('anc', name), 0): flip(('d', q))
        else:                                            # control data q -> target anc(b)
            if xb.get(('d', q), 0): flip(('anc', name))
        for k in ins.get(i + 1, []): flip(k)
    u = {b: xb.get(('anc', b), 0) for b in c.zn}
    E = frozenset(q for q in range(c.n) if xb.get(('d', q), 0))
    return E, u

def run_multi(sch, R, inserts, measflips=()):
    """R rounds, gate level, ancillas reset each round, data frame persists.
       Detectors D[b,0]=m[b,0]; D[b,rho]=m[b,rho]+m[b,rho-1]; D[b,R]=m[b,R-1]+s(final)."""
    c = sch.code; G = sch.gates()
    data = {q: 0 for q in range(c.n)}; m = {}
    ins = {}
    for (r, p, k) in inserts: ins.setdefault((r, p), []).append(k)
    for r in range(R):
        anc = {nm: 0 for nm in c.xn + c.zn}
        def flip(k):
            if k[0] == 'd': data[k[1]] ^= 1
            else:           anc[k[1]]  ^= 1
        for k in ins.get((r, 0), []): flip(k)
        for i, (kind, name, q, t) in enumerate(G):
            if kind == 'X':
                if anc[name]: data[q] ^= 1
            else:
                if data[q]: anc[name] ^= 1
            for k in ins.get((r, i + 1), []): flip(k)
        for b in c.zn: m[(b, r)] = anc[b]
        for (rr, b) in measflips:
            if rr == r: m[(b, r)] ^= 1
    E = frozenset(q for q in range(c.n) if data[q]); s = sfun(c, E)
    D = {}
    for b in c.zn:
        D[(b, 0)] = m[(b, 0)]
        for rho in range(1, R): D[(b, rho)] = m[(b, rho)] ^ m[(b, rho - 1)]
        D[(b, R)] = m[(b, R - 1)] ^ s[b]
    return D, lfun(c, E)

def repair_cost(code, gamma, E2U, Kmax=None):
    """repair(gamma) = min over round assignments r_i and voltages u_i in U(E_i) of
       #{(b,r) : c_b(r-1) != U_b(r)}   -- the (LIFT') mismatch count. Brute force."""
    zn = code.zn; w = len(gamma); K = Kmax or max(2, w + 1)
    Us = [sorted(E2U[E]) for E in gamma]; ss = [sfun(code, E) for E in gamma]
    best = None
    for rounds in product(range(K), repeat=w):
        if min(rounds) != 0: continue                   # normalise the time shift
        for us in product(*Us):
            ud = [dict(u) for u in us]; cost = 0
            for r in range(0, max(rounds) + 1):
                for b in zn:
                    c_prev = 0; U = 0
                    for i in range(w):
                        if rounds[i] <= r - 1: c_prev ^= ss[i][b]
                        if rounds[i] == r:     U      ^= ud[i][b]
                    if c_prev != U: cost += 1
            if best is None or cost < best: best = cost
    return best
```

`enumerate_faults` (one-round elementary X-sector inventory: after-gate control/target/both, prep
on every ancilla, idle on every data qubit at every free step, measurement flip on every Z-check),
`d_eff` (brute force over subsets of `ℰ`), `d_circ_fast` (weight-≤3 meet-in-the-middle over detector
bitmasks produced by `run_multi`, with a distinct-`(location, round)` constraint enforcing the
one-Pauli-per-location convention), `full_locations`/`run_full`/`d_circ_fullpauli` (the two-sector
search of §4.7), `random_sched` (random legal schedules by randomised list scheduling),
`build_sched` (X-first / Z-first / interleaved block schedulers), and `hook_edge_scan` are in the
same file.

### 6.4 Measurement log

```
Theorem 1, abstract exhaustive (all m, all chi, all suffixes)      : 0 counterexamples under (MC)
Theorem 1, 2 156 legal (MC) random schedules, 3 codes              : 0 counterexamples; 608 verticals, all overlap 4
Theorem 1 without (MC)                                             : 37 339 overlap-2 verticals appear
Lemma 3.4 (overlap-2 iff), 12-row exhaustive table                 : exact match
single-fault detector-chain formula, gate level, R = 1,2,3         : 141/141, 282/282, 423/423 (x2 block orders)
F2-linearity of 2- and 3-fault configurations vs full simulation   : 400/400
residual classification (singleton or X-check suffix)              : 1 994/1 994
(V): |u| <= 1 for every empty-residual fault                       : 440/440
sector decoupling, full-Pauli vs X-sector d_circ, [[4,2,2]]        : 12/12
Theorem 2 sandwich / equality / biconditional 5.7                  : 282/282 each
§5.8 closed form for |gamma| = 2 vs brute-force repair             : 331/331
contiguity of minimum-weight undetectable logicals                 : 203 186/203 186
horizontal-representative lemma, both flavours                     : 180/180 configs, 0 failures
Theorem 7.1, 4 codes incl. [[15,7,3]] Hamming-CSS, R = 1..4        : 112/112 configs, d_circ = d_eff
pair gadget: Steane {6} admits u = 0 and u = s, |s| = 3            : 40/40 (MC) schedules
gross code overlap histogram                                       : {0: 4536, 2: 648}  (matches)
gross code hook |s| histogram, one X-check                         : {3:12,4:18,5:18,6:12,9:2} over 62 PROPER subsets
                                                                     + one |s| = 0 for S = supp(a)  (see §3.4a)
gross code data-qubit Z-degree                                     : 3 for all 144  -> not graph-like (matches)
counterexample to `R_sat <= d`: Steane NI, d_eff = 2 < d = 3       : d_R = 2 for R = 1,2,3,4  -> R_sat = infinity
forced representative collisions (both location sets singletons)   : 0 in 180 schedules; non-forced collisions in 180/180
```

---

## 7. Summary of required edits

| priority | file | edit |
|---|---|---|
| 1 | iff-doc §5.10(1) and §8 item 4 | Replace `R_sat(M) ≤ d` with the correct dichotomy (`d_R` constant for `R ≥ d`; `R_sat ≤ d` iff `d_∞ = d`, else `∞`). As written it contradicts the sibling document's Cor. 7.3 and would propagate a false statement into `CIRCDIST.sat`. |
| 2 | iff-doc §5.2 (Lemma 5.3) and Def. 5.1 | Delete "distinct residuals force distinct locations" (contradicted by its own 1.13.4); adopt the sibling document's per-location weight convention and its Lemma 7.2 argument, or the weaker phrasing in §3.1 above. Add the one-line collision repair to 5.7 (⟸) and 5.11. |
| 3 | iff-doc §8 item 3(ii) | "every gross-code hook has `|s| ≥ 3`" → "every *proper* gross-code hook"; `S_a(0) = supp(a)` has `|s| = 0`. |
| 4 | iff-doc §3.2 / NUMERICAL 3.6 | Note that the theorem's hypothesis is per-pair (`u_b = 1, s_b = 0`) while the table's VERTICAL row measures the global `s = 0 ≠ u`; add a per-pair row. |
| 5 | iff-doc Def. 1.6 | X-check detector range is `1 ≤ r ≤ R−1`, not `r ≥ 1`. |
| 6 | either document | Record that the repair monomials of 5.3 have support in `[r_min, r_max] ⊆ [0, R−1]` (because `ε(B) = 0` forces `C` to terminate), so the construction never asks to flip the non-existent `m_{b,R}`. Currently true but unstated. |

Nothing in the two documents' **headline results** — Theorem 1, the (MC) equivalence, the
contiguity/finite-window theorem, the biconditional `d_circ = d_eff ⟺ ∃ minimum-weight γ with
repair(γ) = 0`, and Theorem 7.1 — is refuted by this review. The `≤`-direction defect is a defect of
the printed argument, already correctly handled in the sibling document; the `R_sat` claim is a real
false statement but is confined to a cross-node corollary and does not feed any of the main proofs.

**Reviewer's overall assessment:** the nonint document is the more careful of the two — every
boundary case, the two non-interleaved flavours, the per-location weight convention, and the
`R_sat` dichotomy are all handled correctly, and its central absence-type step (Lemma 5.4's case
enumeration) is exhaustive. The iff document is more ambitious and its two theorems survive, but its
`≤` direction and its `CIRCDIST.sat` corollary were written faster than the rest and are where the
two defects are.
