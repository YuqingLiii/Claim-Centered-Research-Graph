# CIRCDIST.lift — the overlap criterion and the distance formula

**Date:** 2026-08-20 · **Node:** `CIRCDIST.lift` · **Session:** Opus 5 executor, proposer role,
budget box = 2 sessions (main-theorem push), stop-loss binding. No sub-agents.

**Epistemic ceiling for this document: nothing is labelled PROVED.** Every mathematical statement
is labelled **CONJECTURED**; each one additionally carries a *derivation status* line saying
whether the argument given here is complete or where it stops. Every computation is labelled
**NUMERICAL** with the code inline (§9). The 公共定义 of
`research/circdist/notes/CIRCDIST_PROBLEMS.md` is the frozen base; §1 states every additional
definition before use.

---

## 0. Executive summary

**Theorem 1 (overlap criterion) — complete.** §3.2. In a measurement-consistent single-ancilla CSS
schedule, a hook of X-check `a` can be a **vertical** DEM edge on Z-check `b` (`u_b = 1`, `s_b = 0`)
only if `|supp(a) ∩ supp(b)| ≥ 4`. The derivation is four lines from one parity identity (§3.1) and
uses nothing but (MC) and CSS commutation — not graph-likeness. §3.3 upgrades it to an **iff** at
overlap exactly 2, which is where measurement consistency is shown to be load-bearing rather than
decorative: at overlap 2, hook voltage exists **iff** (MC) fails on that pair.

**Theorem 2 (distance formula) — complete on `repair ≤ 2`, gap named at `repair ≥ 3`.** §5.
`d_circ = min_{γ ∈ L_eff} ℓ(γ)` with exact weight accounting in both directions (§5.2, §5.3), and

```
   |γ| + min(repair(γ), 2)   ≤   ℓ(γ)   ≤   |γ| + repair(γ),
```

so `ℓ(γ) = |γ| + repair(γ)` **whenever `repair(γ) ≤ 2`** — unconditionally, for every code and
every schedule, with `repair` computed from **one round only**. Consequently the node's target
biconditional holds in full:

> **`d_circ = d_eff` ⟺ some minimum-weight `γ ∈ L_eff` has `repair(γ) = 0`.** (§5.5)

The residual gap is exactly one branch of the lower bound: closed lifts that spend two extra faults
on a residual *outside* `γ` in order to save three or more units of repair (§5.4, §7.2). **That
branch is not vacuous** — §5.6bis exhibits a weight-2 "pair gadget" whose detector chain equals
that of `|s(E')|` measurement flips, and NUMERICAL 7.2 finds `|s(E')| = 3` pair gadgets in 349 of
349 measurement-consistent Steane schedules. So the general formula is a **minimum-cost covering**
problem, `ℓ(γ) = |γ| + min_m(2m + repair_m(γ))`, and the plain count is provably optimal exactly in
the `repair ≤ 2` regime, which is where every instance in this campaign lives.

**Three results that were not asked for and that change the picture.**

1. **Contiguity / finite window (§5.7).** A minimum-weight undetectable logical of `C_R(M)` occupies
   a **contiguous** block of rounds and its round-span is at most its weight, hence `≤ d`. Proof:
   a fault-free round inside the span forces the accumulated syndrome to vanish there, which splits
   the fault set into two independently closed halves, one of which still flips the observable.
   This discharges the recon's premise `P1.4` for this model without the `CIRCDIST.sat` pumping
   theorem, gives `d_R(M) = d_∞(M)` for all `R ≥ d`, and makes `d_circ` computable from one round.
2. **The temporal boundary is not a branch point and not a voltage sink (§4.1).** With the 公共定义's
   ideal initialisation and ideal readout, the Z-check detector index set of the Z-memory sector is
   the *full* range `r = 0,…,R`, so the finite-`R` complex embeds isometrically into the bi-infinite
   `F₂[x,x⁻¹]` complex. Every boundary worry in the recon's §3.3 / route R3 dissolves: nothing can
   be dumped at either end. This is specific to the commissioned boundary conditions.
3. **A correction that inverts the `CIRCDIST.gross` lead (§3.5).** The d3-gate report's containment
   lemma (`overlap ≤ 2 ⟹ u ⊆ s`) is correct, but its gloss "every hook is horizontal" is **not**:
   `u ⊆ s` permits `0 ⊊ u ⊊ s`, which is a **diagonal** edge carrying timelike voltage ±1. Diagonal
   hooks are abundant in overlap-`≤2` codes: **NUMERICAL** — over 98 811 measurement-consistent
   rotated-surface-code schedules, 148 370 of 790 488 hook-edge classes are diagonal (0 vertical,
   as Theorem 1 requires), with an explicit witness in §3.5. And in the gross code **every** hook
   has `|s| ≥ 3`, so the `|s| = 1` step that makes the surface-code argument work has no analogue
   there. The d3-gate's §8 conclusion ("no hook in any gross-code schedule can carry timelike
   voltage", read as evidence for `D*_Gross = 11`) does **not** follow from Theorem 1.

**End-to-end check (§9.6).** The two steps everything rests on — the closed-lift criterion (LIFT')
and the exact weight accounting — were tested against exhaustive DEM enumeration on **3 855 / 3 855**
minimum-weight undetectable logicals across both sides of the campaign's A/B pair at `R = 2,3,4`:
zero violations. §9.4 independently reproduces the d3-gate's Steane numbers (`d_circ = 3` vs `2`,
149/285/421 columns, 12/18/24 detectors) under a separately written detector layer.

**Definitions sharpened.** Sector decoupling (§1.4) reduces `d_circ` of a Z-memory experiment to a
single `F₂` sector with Z-check detectors only; the uniform detector convention (§1.2) removes the
temporal boundary as a special case; `U(E)` (§1.6) — the set of voltages a residual admits at
weight 1 — is the object that makes `G_circ` a derived graph of a **multigraph over** `G_eff`
rather than of `G_eff` itself (§4.4), which is the precise reason the recon's `F₂`/`Z` orientation
problem (its Obs. 3.5) is not a defect of the theory but a defect of the formulation.

**Surprise.** Neither theorem uses graph-likeness anywhere — and the campaign's own headline gap
instance does not satisfy it. §7.3 records what graph-likeness is actually needed for (only the
*pictures*, and the recon's edge taxonomy), and what it would cost to drop the CSS single-ancilla
hypothesis (everything: `U(∅) ⊆ {0} ∪ {e_b}`, §1.6, is where the model enters). Where
graph-likeness *does* bite is the gap itself: §7.2's Lemma 7.1 shows it forces `|s(E)| ≤ 2` and
`|u' + u''| ≤ 2` for all `u',u'' ∈ U(E)`, which kills the same-round escape — but not the
split-pair escape, so the gap survives in both models. The Steane `d = 3` witness has a bare data
error flipping three detectors and is therefore outside the commissioned model; that fact is what
makes the escape mechanism visible there at all.

---

## 1. The model, stated completely

Everything below is inside the 公共定义: CSS code, single ancilla per stabilizer generator,
ancilla prepared once and measured once per round, one CNOT per data qubit of the generator's
support, standard memory experiment with ideal initialisation and ideal final readout, elementary
faults of unit weight.

### 1.1 Code, circuit, schedule

**Definition 1.1 (code).** A CSS code `Q = [[n,k,d]]` is given by a set `𝒜` of X-checks and a set
`ℬ` of Z-checks, with supports `supp(a), supp(b) ⊆ [n]`, subject to CSS commutation

```
   |supp(a) ∩ supp(b)|  ≡  0   (mod 2)      for all a ∈ 𝒜, b ∈ ℬ.                      (CSS)
```

Logical representatives: `Z_L^{(1)},…,Z_L^{(k)}` and `X_L^{(1)},…,X_L^{(k)}`.

**Definition 1.2 (circuit).** Each check `g ∈ 𝒜 ∪ ℬ` owns one ancilla `anc(g)`. Per round:
every `anc(a)`, `a ∈ 𝒜`, is prepared in `|+⟩`, is the **control** of one CNOT onto each
`q ∈ supp(a)`, and is measured in the X basis; every `anc(b)`, `b ∈ ℬ`, is prepared in `|0⟩`, is
the **target** of one CNOT from each `q ∈ supp(b)`, and is measured in the Z basis.

**Definition 1.3 (schedule).** A schedule `M` assigns an integer time step to every CNOT:
`t(a→q)` for the CNOT with control `anc(a)` and target `q ∈ supp(a)`, and `t(q→b)` for the CNOT
with control `q ∈ supp(b)` and target `anc(b)`. `M` is **legal** if at every step each qubit is in
at most one two-qubit gate. `M` is **non-interleaved** if `max_a,q t(a→q) < min_{q,b} t(q→b)`
(*X-block first*) or `max_{q,b} t(q→b) < min_{a,q} t(a→q)` (*Z-block first*); otherwise
**interleaved**.

**Remark 1.4 (legality forces strict comparison).** If `q ∈ supp(a) ∩ supp(b)` then
`t(a→q) ≠ t(q→b)`, since both gates act on `q`. So `t(q→b) < t(a→q)` and `t(q→b) > t(a→q)` are
complementary. Every parity count below silently uses this.

**Definition 1.5 (memory experiment).** `C_R(M)`: ideal data initialisation (`|0⟩^n` for the
**Z-memory**, `|+⟩^n` for the X-memory), `R` identical rounds of `M`, ideal transversal final data
readout (Z basis for the Z-memory). All statements below are for the Z-memory; the X-memory is the
mirror image under `𝒜 ↔ ℬ`, `X ↔ Z`, control ↔ target, and `d_circ(C) = min` of the two sectors.

### 1.2 Detectors, uniformly across the temporal boundary

Write `m_{g,r}` for the recorded outcome of check `g` in round `r ∈ {0,…,R−1}`.

**Definition 1.6 (detectors, Z-memory).** Adopt the conventions

```
   m_{b,−1} := 0                                  (data initialised in |0⟩^n)
   m_{b,R}  := ⊕_{q ∈ supp(b)} (ideal readout of q)      (terminal virtual outcome)
```

and define, for every `b ∈ ℬ` and every `r ∈ {0,1,…,R}`,

```
   D_{b,r} := m_{b,r} + m_{b,r−1}.                                                    (D)
```

`D_{b,0} = m_{b,0}` is the initial detector and `D_{b,R}` is the terminal detector; the definition
in the d3-gate report §1.4 is reproduced exactly, with no case distinction. In addition the
Z-memory carries X-check detectors `D_{a,r} = m_{a,r} + m_{a,r−1}` for `r ≥ 1` only (the round-0
X outcome is random). Observable: `λ^{(j)} = ⊕_{q ∈ supp(Z_L^{(j)})}` (ideal readout of `q`).

**Definition 1.7 (circuit distance).** `d_circ(C) = min{ |F| : F` triggers no detector and flips
some observable `}`, `|F|` = number of elementary faults.

The point of Definition 1.6 is Lemma 4.1 below: with the ideal boundaries of the 公共定义, the
Z-check detector index set is the *full* interval `{0,…,R}`, i.e. one detector per (check, round
boundary), with none missing at either end.

### 1.3 Elementary faults

**Definition 1.8 (fault set).** One elementary fault is one of: a single-qubit Pauli
(`X`,`Y`,`Z`) on an ancilla immediately after its preparation; one of the 15 non-identity
two-qubit Paulis immediately after a CNOT, on (control, target); a single-qubit Pauli on any qubit
(data or ancilla) at any step at which it is not in a gate; or a classical flip of one recorded
ancilla outcome. Data initialisation and final readout are ideal. Propagation is `F₂` symplectic:
`CNOT(c,t) : x_t ← x_t + x_c , z_c ← z_c + z_t`; ancilla Pauli frames are zeroed after each round's
measurement (reset).

### 1.4 Sector decoupling

**CONJECTURED 1.9 (CSS sector decoupling).** In the Z-memory experiment, let `F` be an
undetectable fault set that flips an observable. Let `F^X` be obtained from `F` by replacing each
Pauli fault by its X-part and deleting the faults whose X-part is trivial and the classical flips
of X-check outcomes. Then `F^X` is undetectable, flips the same observables, and `|F^X| ≤ |F|`.
Hence `d_circ` of the Z-memory experiment is attained inside the **X-sector**: fault components
are `X` Paulis and classical flips of **Z-check** outcomes, and only the **Z-check** detectors of
(D) constrain them.

*Derivation.* Propagation is `F₂`-linear and splits: `x` components propagate control→target and
`z` components target→control, never mixing. `m_{b,r}` is a Z-basis measurement of `anc(b)`, so it
is flipped only by `x` components; the final Z-basis data readout, hence every observable and every
Z-check detector in (D), likewise. `m_{a,r}` is an X-basis measurement of `anc(a)`, so it is
flipped only by `z` components, hence so is every X-check detector. Therefore the Z-check detectors
and the observables are functions of the X-parts alone, and the X-check detectors are functions of
the Z-parts alone. `F` undetectable ⟹ its X-parts trigger no Z-check detector; `F^X` has no `z`
component, so it triggers no X-check detector either. Availability: at each two-qubit location all
15 non-identity Paulis are present, so the X-part of any fault is itself an available fault when
non-trivial; likewise at one-qubit locations. ∎
*Derivation status: complete.*

From here on, "fault" means an X-sector elementary fault and "detector" means a Z-check detector.

### 1.5 One-round data

Because the rounds are identical and residual errors persist, a single fault is described by three
one-round quantities.

**Definition 1.10.** For a fault `f` placed in round `r`:

| symbol | definition | lives in |
|---|---|---|
| `E(f)` | the residual `X` error left on the **data** at the end of round `r` | `F₂^n` (a subset of `[n]`) |
| `s(f)` | `s_b(f) = |supp(b) ∩ E(f)| mod 2` — the syndrome of the residual | `F₂^ℬ` |
| `u(f)` | `u_b(f) = ` the flip that `f` induces in the **round-`r`** outcome `m_{b,r}` | `F₂^ℬ` |
| `λ(f)` | `λ^{(j)}(f) = |E(f) ∩ supp(Z_L^{(j)})| mod 2` | `F₂^k` |

None of `E, s, u, λ` depends on `r` (identical rounds, reset ancillas).

**CONJECTURED 1.11 (time locality).** A fault `f` in round `r` flips exactly the detectors

```
   ∂(f, r)  =  [u(f)]_r  +  [u(f) + s(f)]_{r+1}   ∈  F₂^{ℬ × {0,…,R}}.                (∂)
```

*Derivation.* `m_{b,r}` is flipped by `u_b(f)`. For `r' > r` the data carries `E(f)` throughout
round `r'`, and `anc(b)` is reset each round, so `m_{b,r'}` is flipped by `s_b(f)`; the virtual
`m_{b,R}` is flipped by `s_b(f)` too, because the ideal readout sees `E(f)`. Substituting into (D):
`D_{b,r}` gets `u_b`, `D_{b,r+1}` gets `u_b + s_b`, `D_{b,r'}` gets `s_b + s_b = 0` for
`r' ≥ r+2`. The convention `m_{b,−1} = 0` makes the `r = 0` case an instance of the same formula.
∎ *Derivation status: complete.*

**Definition 1.12 (graph-like).** `M` is *graph-like* (in the Z-memory sector) if
`|u(f)| + |u(f)+s(f)| ≤ 2` for every fault `f`, i.e. every DEM column of (∂) has weight `≤ 2`.
Following the recon's Obs. 1.2, a fault is **horizontal** if `u ∈ {0, s}` (voltage 0), **vertical**
if `s = 0 ≠ u`, and **diagonal** if `u ∉ {0,s}` and `s ≠ 0`; the last two carry time-voltage `±1`.

> **Scope note, stated once and used throughout.** Theorems 1 and 2 below are stated in the
> graph-like model as the node commissions, but **no step of either derivation uses Definition
> 1.12** (see §7.3), and this is not a cosmetic freedom: the campaign's only `d = 3` gap instance,
> the Steane `[[7,1,3]]` Z-memory sector, is **not** graph-like — qubit 6 lies in all three
> Z-checks, so the bare error `X₆` has `|s| = 3` and flips three detectors. Definition 1.12 is
> invoked exactly once in this document, in Lemma 7.1, where it constrains the size of the
> remaining gap.

### 1.6 What the residuals and voltages actually are

**CONJECTURED 1.13 (propagation inventory).** In the X-sector of a legal schedule:

1. An `X` on data qubit `q` inserted at time `t` never spreads to another data qubit; it gives
   `E = {q}` and `u_b = [q ∈ supp(b)]·[t(q→b) > t]`.
2. An `X` on `anc(a)`, `a ∈ 𝒜`, inserted at time `t` gives the **hook** residual
   `S = {q ∈ supp(a) : t(a→q) > t}` — a *suffix* of `a`'s CNOT order `q_1,…,q_w` — with
   ```
      s_b(S) = |supp(b) ∩ S| mod 2 ,      u_b(S) = #{ q ∈ supp(b) ∩ S : t(q→b) > t(a→q) } mod 2.
   ```
3. An `X` on `anc(b)`, `b ∈ ℬ`, at any time, and a classical flip of `m_{b,r}`, both give
   `E = ∅`, `u = e_b`, `s = 0` — a **vertical** fault of unit voltage.
4. Two-qubit faults are products of the atoms of 1–3 at a common time; on a gate `a→q_j` the
   possible residuals are `∅, S_j, {q_j}, S_{j−1}` (`S_j` = suffix after the `j`-th CNOT), on a
   gate `q→b` they are `∅` and `{q}`.

Consequently the realisable residual set is
`ℰ = {suffixes of X-check CNOT orders} ∪ {singletons} ∪ {∅}`, and

```
      U(∅) = {0} ∪ { e_b : b ∈ ℬ }.                                                   (V)
```

*Derivation.* Data qubits are controls only for gates into Z-ancillas and targets only for gates
from X-ancillas; `x` propagates control→target, so an `x` on a data qubit reaches only Z-ancillas,
and an `x` on `anc(a)` reaches only the data qubits `q` whose gate `a→q` is still to come. `anc(b)`
is never a control, so an `x` on it reaches nothing and only flips its own Z-basis outcome. For
(V): a fault with `E = ∅` cannot involve an `x` on any data qubit (that would leave `{q}`) nor on
`anc(a)` before its last CNOT; the only surviving atoms are those of item 3, plus the trivial `x`
on `anc(a)` after its last CNOT (`u = 0`). ∎ *Derivation status: complete.*

**NUMERICAL 1.14.** (V) verified exhaustively over every elementary fault of one round, for the
Steane interleaved and non-interleaved witnesses and for the surface-code schedule of §3.5:
`U(∅) = {0, e_{Z1}, e_{Z2}, e_{Z3}}` and `{0, e_{ZA}, e_{ZB}, e_{ZC}, e_{ZD}}` respectively, all of
weight `≤ 1`. Code and output in §9.2. (V) is the **only** place where the single-ancilla CSS
structure enters Theorem 2, and it is exactly what makes the repair cost a *count of monomials*.

**Definition 1.15 (voltage spectrum).** For `E ∈ ℰ`, `U(E) := { u(f) : f` a fault with
`E(f) = E }`. A residual is *rigid* if `|U(E)| = 1`. Suffixes of length `≥ 2` are typically rigid;
singletons never are (their `X` can be inserted at any of the `|{b : q ∈ supp(b)}| + 1` positions
relative to the gates `q→b`, giving all suffix patterns of that ordering).

### 1.7 The effective model

**Definition 1.16.** `C_1^eff = F₂^{ℰ∖{∅}}`, `C_0^eff = F₂^ℬ`, `∂_eff(E) = s(E)`,
`λ_eff(E) = λ(E)`, and

```
   L_eff := { γ ∈ C_1^eff  :  ∂_eff γ = 0 ,  λ_eff γ ≠ 0 } ,      d_eff(M) := min_{γ ∈ L_eff} |γ|.
```

This is `d_ext(E(M))` of the 公共定义 and of Strikis–Browne–Beverland Defs. 1–3: `∂_eff` is
`H_X^ext`, `λ_eff` is `L_X^ext`, and `|γ|` counts residuals, not qubits.

**Definition 1.17 (the projection).** `π_1 : F₂^{𝔽 × {0,…,R−1}} → C_1^eff`, `(f,r) ↦ [E(f)]`
(with `[∅] = 0`) — *fiber collapse*; `π_0 : F₂^{ℬ×{0,…,R}} → C_0^eff`, `(b,r) ↦ b` — *fiber sum*.

**CONJECTURED 1.18 (chain map).** `π_0 ∘ ∂ = ∂_eff ∘ π_1`, and `|π_1 F| ≤ |F|` for every `F`.
*Derivation.* `π_0 ∂(f,r) = u + (u+s) = s = ∂_eff π_1(f,r)` by (∂); weight non-increase because
`π_1` maps each basis vector to a basis vector or to 0. ∎ *Status: complete.*

---

## 2. Measurement consistency

### 2.1 Statement

**Definition 2.1.** For `a ∈ 𝒜`, `b ∈ ℬ`, put

```
   c_{ab}(M) := #{ q ∈ supp(a) ∩ supp(b) : t(q→b) < t(a→q) }   mod 2 .
```

`M` is **measurement-consistent** if `c_{ab}(M) = 0` for all `(a,b)`.

```
                                                                                      (MC)
```

**CONJECTURED 2.2 (validity).** A legal schedule `M` produces deterministic detectors — i.e.
`C_R(M)` is a syndrome-extraction circuit at all, and its `d_circ` is defined — **iff** `M`
satisfies (MC). Non-interleaved schedules satisfy (MC) automatically (`c_{ab} = 0` termwise:
either every `t(q→b) > t(a→q)` or every `t(q→b) < t(a→q)`, and `|supp(a)∩supp(b)|` is even).

### 2.2 Derivation

Let `U` be the unitary of one round (the CNOTs only). For a Pauli `P` measured at the end of the
round, write `Ô(P) := U† P U`, the observable whose value on the state at the *start* of the round
equals the recorded outcome. Conjugation by a CNOT with control `c` and target `t` sends
`X_c ↦ X_c X_t`, `X_t ↦ X_t`, `Z_t ↦ Z_c Z_t`, `Z_c ↦ Z_c`; back-propagation processes the gates in
reverse time order.

**Step 1 (back-propagated observables).**

```
   Ô(X_{anc(a)})  =  X_{anc(a)} · ∏_{q ∈ supp(a)} X_q · ∏_{b ∈ ℬ} X_{anc(b)}^{ c_{ab} } ,
   Ô(Z_{anc(b)})  =  Z_{anc(b)} · ∏_{q ∈ supp(b)} Z_q · ∏_{a ∈ 𝒜} Z_{anc(a)}^{ c'_{ab} } ,
      with  c'_{ab} = #{ q ∈ supp(a) ∩ supp(b) : t(a→q) < t(q→b) } mod 2 .
```

*Why.* Start from `X_{anc(a)}`. Going backwards, at the gate `a→q` the factor `X_{anc(a)}` (a
control) emits `X_q`; thereafter `X_q` is itself a control exactly for the gates `q→b`, and only
those with `t(q→b) < t(a→q)` are still to be processed, each emitting `X_{anc(b)}`; `anc(b)` is
never a control, so the process stops. `anc(a)` is never a target, so no further `X_{anc(a)}`
appears and each `q ∈ supp(a)` is emitted exactly once. The second identity is dual (`Z` travels
target→control). By (CSS), `c_{ab} + c'_{ab} = |supp(a)∩supp(b)| ≡ 0`, so `c'_{ab} = c_{ab}`: the
two conditions coincide. (Consistency check: the symplectic form of the two operators is
`|supp(a)∩supp(b)| + c_{ab} + c'_{ab} ≡ 0`, as it must be, since end-of-round measurements on
distinct ancillas commute.)

**Step 2 ((MC) fails ⟹ non-deterministic).** Suppose `c_{ab} = 1` for some pair. The round-`r`
outcome `m_{b,r}` is the outcome of measuring `Ô(Z_{anc(b)})` on the state at the start of round
`r`, whose ancilla factor is `|+⟩⟨+|` on `anc(a)`. `Ô(Z_{anc(b)})` contains `Z_{anc(a)}` to an odd
power, and `Z_{anc(a)}` anticommutes with the stabilizer `X_{anc(a)}` of the freshly prepared
`|+⟩`. By the stabilizer measurement rule the outcome is uniform and independent of everything
recorded earlier; hence `D_{b,r} = m_{b,r} + m_{b,r−1}` is uniform conditioned on the past, so it
is not deterministic. (Dually `D_{a,r}` fails via `X_{anc(b)}` versus `|0⟩`.)

**Step 3 ((MC) holds ⟹ deterministic, value 0).** With all `c_{ab} = 0`,
`Ô(Z_{anc(b)}) = Z_{anc(b)} ∏_{q∈supp(b)} Z_q`, and `Z_{anc(b)}` stabilises the fresh `|0⟩`; so
`m_{b,r}` is the value of `Z_{supp(b)}` on the **data** at the start of round `r`. Back-propagating
`Z_{supp(b)}` through one complete round: each `Z_q` (`q` a target of the gates `a→q`) emits
`Z_{anc(a)}` once per `a ∋ q`, so the total exponent of `Z_{anc(a)}` is `|supp(a)∩supp(b)| ≡ 0` by
(CSS), and `Z_q` on a control does not spread. Hence `Z_{supp(b)}` is invariant round by round, and
`m_{b,r}` equals its value on the initial data state `|0⟩^n`, namely `0`, for every `r`. So
`D_{b,r} = 0` for `0 ≤ r ≤ R−1`; and `D_{b,R} = m_{b,R−1} + Z_{supp(b)}(readout) = 0` likewise.
For the X-check detectors, `Ô(X_{anc(a)}) = X_{anc(a)} ∏_{q ∈ supp(a)} X_q` and `X_{supp(a)}` is
round-invariant by the same parity computation; it is *not* determined by `|0⟩^n`, which is why
`D_{a,0}` is excluded, but after the round-0 measurement the state is stabilised by
`(−1)^{m_{a,0}} X_{supp(a)}`, which survives every later round, so `m_{a,r} = m_{a,0}` and
`D_{a,r} = 0` for `r ≥ 1`. ∎

*Derivation status: complete, modulo the standard stabilizer-formalism facts used verbatim
(measurement of a Pauli anticommuting with a stabilizer yields a uniform bit; Heisenberg
conjugation table for CNOT).*

**NUMERICAL 2.3 (independent oracle, inherited).** The d3-gate report checked (MC) against
`stim.Circuit.detector_error_model()` on 56 schedules: 56 agreements, 0 disagreements, and every
schedule used in that report built a DEM successfully. This session re-used the same predicate;
all schedules in §9 report zero (MC) violations.

### 2.3 Why (MC) is load-bearing rather than hygienic

(MC) is not merely a well-definedness side condition; it is the hypothesis that makes Theorem 1
true. §3.3 shows that at overlap exactly 2 a hook carries vertical voltage **iff** (MC) fails on
that pair — so dropping (MC) does not weaken Theorem 1's conclusion, it destroys it. This is the
structural explanation of the d3-gate's §7 observation that the round-1 recon's `[[4,2,2]]` circuit
produced a "distance" from non-deterministic detectors.

---

## 3. Theorem 1 — the overlap criterion

Throughout §3, `a ∈ 𝒜` has CNOT order `q_1,…,q_w` (`w = |supp(a)|`, indices in time order); a
**hook** is a fault of type 1.13.2, with residual the suffix `S = S_j = {q_{j+1},…,q_w}` and
complementary prefix `P = P_j = {q_1,…,q_j}`, so `supp(a) = P ⊔ S`.

### 3.1 The parity identity

**CONJECTURED 3.1.** For every hook `S` of `a`, every `b ∈ ℬ`, and every legal schedule,

```
   u_b(S) + s_b(S)  =  #{ q ∈ supp(b) ∩ S : t(q→b) < t(a→q) }   mod 2 ,               (3.1a)
```

and if `M` satisfies (MC),

```
   u_b(S) + s_b(S)  =  #{ q ∈ supp(b) ∩ P : t(q→b) < t(a→q) }   mod 2 .               (*)
```

*Derivation.* (3.1a): by 1.13.2, `u_b(S)` counts `q ∈ supp(b) ∩ S` with `t(q→b) > t(a→q)` and
`s_b(S)` counts all of `supp(b) ∩ S`; adding, the terms with `t(q→b) > t(a→q)` cancel and the
complementary ones survive (Remark 1.4: there is no third case). For (*): `supp(a) ∩ supp(b)` is
the disjoint union of `P ∩ supp(b)` and `S ∩ supp(b)`, so the two counts in (3.1a) and in (*) sum
to `c_{ab} = 0`. ∎ *Status: complete.*

Identity (*) is the whole content of Theorem 1: **under (MC), the voltage of a hook is read off the
prefix, not the suffix.** A hook can only be non-horizontal on `b` if `b` also meets the part of
`supp(a)` that the fault did *not* damage.

### 3.2 Theorem 1

**CONJECTURED 3.2 (Theorem 1: overlap-4 necessary condition).** Let `M` be a legal,
measurement-consistent single-ancilla CSS schedule. If a hook `S` of an X-check `a` carries
non-zero **vertical** voltage on a Z-check `b` — that is, `u_b(S) = 1` and `s_b(S) = 0` — then

```
   |supp(a) ∩ supp(b)|  ≥  4 .
```

Equivalently: if `|supp(a) ∩ supp(b)| ≤ 2` for all pairs, no hook of any measurement-consistent
schedule is a vertical DEM edge.

*Derivation.*
(i) `u_b(S) = 1` forces `supp(b) ∩ S ≠ ∅` (an empty intersection gives `u_b = 0` by 1.13.2).
(ii) `s_b(S) = 0` says `|supp(b) ∩ S|` is even; with (i), `|supp(b) ∩ S| ≥ 2`.
(iii) `u_b(S) + s_b(S) = 1`, so by (*) the count `#{q ∈ supp(b) ∩ P : t(q→b) < t(a→q)}` is odd; in
particular `supp(b) ∩ P ≠ ∅`, so `|supp(b) ∩ P| ≥ 1`.
(iv) `|supp(a) ∩ supp(b)| = |supp(b) ∩ P| + |supp(b) ∩ S| ≥ 1 + 2 = 3`, and this number is even by
(CSS), hence `≥ 4`. ∎
*Derivation status: complete. Hypotheses used: (CSS), legality (Remark 1.4), (MC). Not used:
graph-likeness, `R`, the boundary conditions, the code's distance.*

**Remark 3.3 (where each hypothesis bites).** Step (iv) is the only place (CSS) is used, and it is
what turns `≥ 3` into `≥ 4`; step (iii) is the only place (MC) is used. Without (MC), (3.1a) gives
`u_b + s_b = c_{ab} + #{q ∈ supp(b)∩P : …}`, and the conclusion drops to `|supp(a)∩supp(b)| ≥ 2`.

### 3.3 Sharpness: at overlap 2 the criterion is an iff

**CONJECTURED 3.4.** Let `|supp(a) ∩ supp(b)| = 2`, say `supp(a) ∩ supp(b) = {p, p'}`, and let `S`
be any hook of `a`. Then

```
   u_b(S) = 1  and  s_b(S) = 0     ⟺     { p, p' } ⊆ S   and   c_{ab}(M) = 1 .
```

*Derivation.* `s_b(S) = |S ∩ {p,p'}| mod 2`. If `|S ∩ {p,p'}| = 1` then `s_b = 1`, excluded. If
`S ∩ {p,p'} = ∅` then `u_b = 0`, excluded. So `{p,p'} ⊆ S`, and then
`u_b(S) = [t(p→b) > t(a→p)] + [t(p'→b) > t(a→p')] = 2 − c_{ab} ≡ c_{ab} (mod 2)`. ∎
*Status: complete.*

So at overlap 2 the vertical hook edges are **exactly** the artefacts of measurement-inconsistent
schedules, and Theorem 1 is not merely necessary but tight. Theorem 1's threshold `≥ 4` is also
tight in the other direction: the Steane code has `|supp(X_i) ∩ supp(Z_i)| = 4` and the d3-gate's
§5.2 witness realises three vertical hooks simultaneously.

### 3.4 The containment lemma

**CONJECTURED 3.5 (containment).** If `|supp(a) ∩ supp(b)| ≤ 2` for every `a ∈ 𝒜`, `b ∈ ℬ`, then in
every legal measurement-consistent schedule every fault satisfies `u ⊆ s` componentwise.

*Derivation.* Hooks: fix `b`; `|supp(a)∩supp(b)| ∈ {0,2}` by (CSS). If `0`, then `u_b = s_b = 0`.
If `2` with `supp(a)∩supp(b) = {p,p'}`: for `|S ∩ {p,p'}| = 0`, `u_b = s_b = 0`; for `1`, `s_b = 1`
so `u_b ≤ s_b` trivially; for `2`, `s_b = 0` and `u_b = c_{ab} = 0` by (MC) and Lemma 3.4. Bare data
errors (1.13.1): `u_b ≤ [q ∈ supp(b)] = s_b`. Vertical faults have `s = 0` and `u = e_b`, so they
**violate** `u ⊆ s` — the lemma is about faults with non-empty residual, which is the d3-gate's
intent (its Conj. 3.2 speaks of "suffix residuals"). Two-qubit faults are sums of atoms with a
common time and inherit containment componentwise when both atoms do. ∎ *Status: complete for
hooks, bare data errors and their products; the statement should be read as "every fault with
non-empty residual", which is what the d3-gate's numerical table 3.3 measured.*

### 3.5 Correction: containment does **not** mean horizontal

This is the load-bearing correction of this session.

`u ⊆ s` with `|s| ≥ 2` permits `0 ⊊ u ⊊ s`, which by Definition 1.12 is a **diagonal** edge with
time-voltage `±1`. Theorem 1 forbids *vertical* hooks at overlap `≤ 2`; it says nothing about
diagonal ones. The d3-gate report's Conj. 3.2 is correct as stated, but its §8 gloss — "by Conj.
3.2 every hook is horizontal", and hence "no hook in any measurement-consistent gross-code schedule
can carry timelike voltage" — does not follow. The step that is genuinely used in the d3-gate's own
surface-code argument (its Conj. 4.1) is not containment but the *separate* exhaustive fact that
every weight-2 effective logical there has `|s| = 1`; when `|s| = 1`, `u ⊆ s` does upgrade to
`u ∈ {0,s}`.

**NUMERICAL 3.6 (diagonal hooks are abundant at overlap ≤ 2).** Rotated `[[9,1,3]]` surface code
(overlap histogram `{0: 8, 2: 8}`, max 2). Scanning the depth-8 offset family over all X-orders of
`XA`, restricted to legal **and** measurement-consistent schedules — 98 811 schedules, 790 488
(hook, Z-check) classes:

| class | count |
|---|---|
| horizontal-early (`u = s`) | 321 059 |
| horizontal-late (`u = 0`) | 321 059 |
| **DIAGONAL** (`u ∉ {0,s}`, `s ≠ 0`) | **148 370** |
| VERTICAL (`s = 0 ≠ u`) | **0** |

The `0` in the last row is Theorem 1, confirmed. The `148 370` in the third row is the correction.
Explicit witness (legal, `MC = ∅`, depth 8):

```
  X: XA=[1,2,4,5]@0,1,2,3   XB=[3,4,6,7]@0,1,2,3   XC=[0,1]@0,1   XD=[7,8]@0,1
  Z: ZA=[0,1,3,4]@1,2,3,4   ZB=[4,5,7,8]@0,1,2,3   ZC=[2,5]@3,4   ZD=[3,6]@6,7

  hook of XB with S = {6,7} :  s = (ZA,ZB,ZC,ZD) = (0,1,0,1),  u = (0,0,0,1)
        u ⊆ s ✓        u ≠ 0 ✓        u ≠ s ✓        ⇒ DIAGONAL, time-voltage 1
```

Check by hand: `S = {6,7}` meets `ZB = {4,5,7,8}` in `{7}` and `ZD = {3,6}` in `{6}`, so
`s = e_{ZB} + e_{ZD}`; `t(7→ZB) = 2 < t(XB→7) = 3` gives `u_{ZB} = 0`, while
`t(6→ZD) = 7 > t(XB→6) = 2` gives `u_{ZD} = 1`.

**NUMERICAL 3.7 (the gross code has no `|s| = 1` hooks at all).** For the gross code
`[[144,12,12]]` (bivariate bicycle, `ℓ=12, m=6, A = x³+y+y², B = y³+x+x²`, `H_X = [A|B]`,
`H_Z = [Bᵀ|Aᵀ]`; overlap histogram `{0: 4536, 2: 648}`, max 2 — reproducing the d3-gate's §8
computation): for the check `X_{0,0}` with support `{18,1,2,75,78,84}`, the syndrome weights `|s(S)|`
over all 62 non-trivial subsets `S` of the support are

```
   |s| :  3   4   5   6   9
   #   : 12  18  18  12   2          — minimum |s| = 3, never 1.
```

By translation invariance the same holds for every X-check. So the `|s| = 1` mechanism that closes
the surface-code case is *absent* in the gross code, and Theorem 1 alone gives no information about
its completion gap.

**Consequence for `CIRCDIST.gross`.** The d3-gate's cross-node lead (§8: "evidence against a
distance-12 interleaved gross circuit") should be **withdrawn as stated**. What survives is the
weaker and still useful statement: *in the gross code no single hook is a vertical DEM edge*, i.e.
`g(C) > 0` there cannot be produced by the `[[4,2,2]]`-style mechanism (an effective logical whose
base image is a loop). Diagonal hooks are not excluded, and by 3.7 they are the generic case. The
correct place to look for a distance-12 gross circuit is therefore `repair(γ) > 0` driven by
diagonals, which is exactly the quantity Theorem 2 makes computable.

---

## 4. The spacetime complex, and why the boundary is free

### 4.1 The finite circuit embeds in the bulk

Let `R = F₂[x, x⁻¹]` (Laurent polynomials, an integral domain) and `V = R^ℬ` (free `R`-module).
Identify `F₂^{ℬ × Z} ≅ V` by `[b]_r ↦ e_b x^r`. Then (∂) reads

```
   ∂( f, r )  =  x^r ( u_f (1+x)  +  s_f x )   ∈  V .                                 (∂-L)
```

**CONJECTURED 4.1 (no temporal boundary correction).** For the memory experiment of Definition 1.5
— ideal initialisation, `R` rounds, ideal final readout — the Z-check detector index set is exactly
`ℬ × {0,1,…,R}`, with no detector missing at either end (Definition 1.6). Consequently a fault set
`F` supported in rounds `{0,…,R−1}` triggers no detector in `C_R(M)` **iff** the Laurent element
`Σ_{(f,r) ∈ F} x^r(u_f(1+x) + s_f x)` vanishes in `V`. The truncation map is an isometric embedding
of chain complexes, not a quotient.

*Derivation.* The initial detector `D_{b,0} = m_{b,0}` exists and is deterministic because the data
are initialised in `|0⟩^n`, an eigenstate of every `Z_{supp(b)}` (§2.2 Step 3); the terminal
detector `D_{b,R}` exists and is deterministic because the final readout is ideal and transversal
in the Z basis. So every monomial `x^r`, `0 ≤ r ≤ R`, of the Laurent expression corresponds to an
actual detector of `C_R(M)`, and no cancellation-by-truncation can occur. ∎ *Status: complete, and
strictly dependent on the 公共定义's ideal boundaries; with noisy initialisation or a non-ideal
readout, `D_{b,0}` or `D_{b,R}` would be absent and the corresponding monomials would become free.*

This settles the node's technical requirement 5 (detector and logical boundary) in the affirmative
and **retires** the recon's `P3.3` ("boundary edges are voltage sinks") and its `P1.5` (boundary
quotient) for this model. Spatially there is nothing to do either: a fault triggering a single
detector is simply one with `|u| + |u+s| = 1`, handled by the same algebra.

### 4.2 The closed-lift criterion

**CONJECTURED 4.2 (divisibility form).** Let `F` be a fault set with `π_1 F = γ`, `∂_eff γ = 0`.
Put `A(x) = Σ_{(f,r) ∈ F} u_f x^r` and `B(x) = Σ_{(f,r) ∈ F} s_f x^r` in `V`. Then `B(1) = ∂_eff γ = 0`,
so `B = (1+x) C` for a unique `C ∈ V`, and

```
   ∂F = (1+x)( A + xC ) ,        hence      ∂F = 0   ⟺   A = x·C .                    (LIFT)
```

*Derivation.* Summing (∂-L) gives `∂F = (1+x)A + xB = (1+x)A + x(1+x)C = (1+x)(A + xC)`. `R` is a
domain and `V` is free, so `1+x` is a non-zero-divisor. Uniqueness of `C`: `R/(1+x) ≅ F₂` via the
augmentation `ε : x ↦ 1`, and `ε(B) = B(1) = 0`. ∎ *Status: complete.*

**CONJECTURED 4.3 (prefix-sum form — the physical reading of (LIFT)).** For `b ∈ ℬ` and `r ∈ Z` put

```
   c_b(r) := Σ_{ (f,r_f) ∈ F , r_f ≤ r }  s_{f,b}      (accumulated residual syndrome after round r)
   U_b(r) := Σ_{ (f,r_f) ∈ F , r_f = r }  u_{f,b}      (total round-r outcome flips on b)
```

Then `C = Σ_r c(r) x^r`, and (LIFT) is equivalent to

```
   U_b(r)  =  c_b(r−1)      for every  b ∈ ℬ  and every  r .                          (LIFT')
```

*Derivation.* `(1+x)Σ_r c(r)x^r = Σ_r (c(r) + c(r−1))x^r`, and `c(r)+c(r−1)` is the round-`r`
syndrome sum, which is the coefficient of `x^r` in `B`; so that series is `C`. Comparing
coefficients in `A = xC` gives (LIFT'). Directly: `m_{b,r}` is flipped by `c_b(r−1) + U_b(r)`, so
`D_{b,r} = 0` for all `r` says the sequence `r ↦ c_b(r−1) + U_b(r)` is constant, and the initial
detector `D_{b,0}` (Lemma 4.1) pins that constant to `0`. ∎ *Status: complete.*

> **(LIFT') in words.** *A fault set is undetectable iff, in every round and on every Z-check, the
> number of measurement flips equals the parity of the syndrome accumulated by all earlier rounds.*
> This is the intrinsic "voltage" the node asked for. It is `F₂`-valued (no orientation ambiguity),
> it is computed from one round's `(E, s, u)` data plus a round assignment, and no multi-round
> circuit is ever built.

### 4.3 Non-tautology check

The recon's ⚠ (its §3.1) warns that `d_circ = min_γ ℓ(γ)` alone is a renaming. The content added
here is: (a) `ℓ(γ)` is bounded above by `|γ| + repair(γ)` with `repair` an explicit one-round
quantity (§5.2); (b) `ℓ(γ)` is bounded below by the same expression whenever it is `≤ 2` (§5.3);
(c) the search space for `ℓ` is finite and `d`-bounded (§5.7). (a)+(b)+(c) together are a decision
procedure, which is what the node's "不需要构造完整多轮电路的等号判定算法" asks for.

### 4.4 Covering, branched covering, or chain map — the sharp answer

The node's technical requirement 2. The bulk `π_0` is the augmentation `ε : V → F₂^ℬ`; `π_1` is
fiber collapse; together they are a weight-non-increasing chain map (1.18) and *not* a graph
covering. The precise obstruction is **not** the boundary (§4.1 removes that) but Definition 1.15:

> A base "edge" of `G_eff` is a residual `E`; its lifts are the faults `f` with `E(f) = E`, and
> these can have **different voltages** `u ∈ U(E)` at the same weight 1. So `G_circ` is the derived
> graph of a voltage assignment on the **multigraph** `G̃_eff` in which `E` is replaced by `|U(E)|`
> parallel edges, not on `G_eff`.

This is why "the net voltage of `γ`" is a *set*, not a number (the recon's Obs. 3.5), and it is a
property of the model, not an artefact of `F₂` versus `Z`: the multiplicity is real. The
group-ring formulation absorbs it by minimising over `u_i ∈ U(E_i)` inside `repair` (§5.1). The
recon's route R2 (`voltage-monodromy-lift`) can only be completed after passing to `G̃_eff`;
stated on `G_eff` it is not merely hard, it is false.

---

## 5. Theorem 2 — the distance formula

### 5.1 Definitions

**Definition 5.1 (lift length).** For `γ ∈ L_eff`,
`ℓ_R(γ) := min{ |F| : F ⊆ 𝔽 × {0,…,R−1}, ∂F = 0, π_1 F = γ }` (`= +∞` if none), and
`ℓ(γ) := lim_{R→∞} ℓ_R(γ) = min over the bi-infinite model`.

**Definition 5.2 (repair cost — one round only).** For `γ = {E_1,…,E_w} ∈ L_eff`, a *repair
certificate* is a choice of rounds `r_1,…,r_w ∈ Z` and voltage representatives `u_i ∈ U(E_i)`.
Given one, set `s_i := s(E_i)`, `B := Σ_i s_i x^{r_i}`, `C := B/(1+x)` (well defined since
`Σ_i s_i = ∂_eff γ = 0`), `A_0 := Σ_i u_i x^{r_i}`, and

```
   repair(γ)  :=  min over repair certificates of   wt( A_0 + x·C ) ,
```

where `wt` counts non-zero coefficients over all pairs `(b, r) ∈ ℬ × Z`. Equivalently, by (LIFT'),
`repair(γ) = min Σ_{b,r} | c_b(r−1) + Σ_{i : r_i = r} u_{i,b} |`, the total number of
(check, round) slots at which the accumulated syndrome and the in-round flips disagree.

`repair(γ)` depends only on the one-round data `{(E, s(E), U(E), λ(E)) : E ∈ ℰ}`. Translation
invariance makes it independent of an overall time shift; §5.7 makes the minimisation finite.

### 5.2 The `≤` direction: constructing the lift from `γ` and its repair certificate

**CONJECTURED 5.3.** For every `γ ∈ L_eff`, `ℓ(γ) ≤ |γ| + repair(γ) < ∞`, and the same bound holds
for `ℓ_R(γ)` as soon as `R` exceeds the round-span of the optimal certificate. In particular
`d_circ ≤ |γ| + repair(γ)` for every `γ`.

*Derivation.* Take an optimal certificate `(r_i, u_i)`. For each `i` choose a fault `f_i` with
`E(f_i) = E_i` and `u(f_i) = u_i` (one exists, by definition of `U(E_i)`) and place it in round
`r_i`; these are `w = |γ|` distinct circuit locations, since distinct residuals force distinct
locations. Their detector chain is `(1+x)(A_0 + xC)` by 4.2. Let `D := A_0 + xC ∈ V` and write
`D = Σ_{(b,r) ∈ supp(D)} e_b x^r`; for each `(b,r) ∈ supp(D)` add the classical flip of `m_{b,r}`,
which by (V) is a fault with `E = ∅`, `s = 0`, `u = e_b`, contributing `(1+x)e_b x^r` to the
detector chain and `0` to `π_1`. These `wt(D)` faults are distinct from each other and from the
`f_i` (they have empty residual). The total chain is `(1+x)(D + D) = 0`, so `F` is undetectable;
`π_1 F = γ`, so `λ(F) = λ_eff(γ) ≠ 0` and `F` is a logical fault. `|F| = |γ| + wt(D)`. Finiteness:
the same-round certificate (`all r_i = 0`) always exists and gives `wt(A_0) ≤ Σ_i |u_i| < ∞`. ∎
*Derivation status: complete. The only model input is (V) — that a unit-weight fault of unit
voltage exists on **every** check in **every** round. In this fault model it is the classical
measurement flip.*

### 5.3 The `≥` direction: exact projection accounting

**CONJECTURED 5.4 (exact weight accounting).** Let `F` be any undetectable fault set of `C_R(M)`
flipping an observable, and `γ := π_1 F`. Then:

1. `γ ∈ L_eff`. In particular the projection **cannot** destroy non-triviality.
2. Writing `n_E := #{ f ∈ F : E(f) = E }` for `E ∈ ℰ ∪ {∅}`, one has `n_E ≡ [E ∈ γ] (mod 2)` for
   `E ≠ ∅`, `|γ| = #{E ≠ ∅ : n_E odd}`, and the exact weight loss is
   ```
      |F| − |γ|  =  n_∅  +  Σ_{E ≠ ∅} ( n_E − [n_E odd] )  =  n_∅ + 2m ,   m ∈ Z_{≥0}.
   ```
3. `|F| ≥ |γ| + 2m + wt(A_ess + xC)`, where `A_ess` collects the `u`-monomials of the faults with
   non-empty residual and `C = B/(1+x)` with `B` the full syndrome series of `F`.
4. Consequently `|F| ≥ |γ| + min( repair(γ), 2 )`, and if `m = 0` then `|F| ≥ |γ| + repair(γ)`.

*Derivation.*
(1) By 1.18, `∂_eff γ = π_0 ∂ F = 0`. For non-triviality: the observable is a linear functional of
the **final data error**, which is `Σ_{f ∈ F} E(f)`; that vector is the image of `γ` under the
linear map `C_1^eff → F₂^n`, so `λ_eff(γ) = λ(F) ≠ 0` **identically**, not merely generically.
Hence `γ ≠ 0` and `γ ∈ L_eff`.
(2) `π_1 F = Σ_f [E(f)]` in `F₂^{ℰ∖{∅}}`, giving the parities; `|F| = n_∅ + Σ_{E≠∅} n_E`; and
`Σ_{E≠∅}(n_E − [n_E odd])` is even, being a sum of even numbers.
(3) Split `A = A_ess + A_∅` by residual. By (V) every fault with `E = ∅` contributes at most one
monomial to `A`, so `wt(A_∅) ≤ n_∅`. (LIFT) gives `A_∅ = A_ess + xC`, hence
`n_∅ ≥ wt(A_ess + xC)`; add `Σ_{E≠∅} n_E = |γ| + 2m`.
(4) If `m = 0` the faults with non-empty residual are exactly one per `E_i ∈ γ`, so
`(r_i, u_i)` is a repair certificate and `wt(A_ess + xC) ≥ repair(γ)` by definition of the minimum;
if `m ≥ 1` then `|F| ≥ |γ| + 2`. ∎
*Derivation status: complete.*

**Remark 5.5 (why no systolic death — the level at which the claim is safe).** The literature
warning inherited from `artifacts/circdist_lift_litverify2_20260820.md` is that homology systole is
**not** monotone under covers: `p_*` is injective on `π_1` but not on `H_1`, so a lifted cycle can
become trivial downstairs and escape the base-distance bound. Step (1) shows the failure mode
cannot occur here, and the reason is structural rather than dimensional: **the logical functional
is pulled back from the base**, `λ_circ = λ_eff ∘ π_1` as an identity of linear maps, because the
observable is read exactly once, at the end, from the accumulated residual. There is no room for
`ker(π_1)` to contain the class: `γ` is certified non-trivial by the *same* functional that
certified `F`. This is the graph-like-model analogue of `sys_H = sys_π = girth`; stated at the
level of a general chain map between spacetime complexes with independently defined logical
observables, the statement would be false, and the litverify counterexample is precisely a witness
of that. What is used: the ideal terminal readout of Definition 1.5.

### 5.4 Theorem 2

**CONJECTURED 5.6 (Theorem 2).** Fix a legal, measurement-consistent single-ancilla CSS schedule
`M` and a memory sector. Then for `R` large enough (`R ≥ d` suffices, by §5.7):

```
   (a)   d_circ( C_R(M) )  =  min_{ γ ∈ L_eff }  ℓ(γ) ;

   (b)   |γ| + min( repair(γ), 2 )   ≤   ℓ(γ)   ≤   |γ| + repair(γ)      for every γ ∈ L_eff ;

   (c)   ℓ(γ) = |γ| + repair(γ)      whenever  repair(γ) ≤ 2 ;

   (d)   d_circ  =  min_{γ ∈ L_eff} ( |γ| + repair(γ) )      whenever the minimising γ has
                                                              repair(γ) ≤ 2 ,
```

with `repair(γ)` computed from one round of `M` alone.

*Derivation.* (a) `≤`: every closed lift of every `γ ∈ L_eff` is an undetectable fault set with
`λ ≠ 0` (5.3). `≥`: 5.4(1) sends a minimum-weight undetectable logical `F` to `γ = π_1 F ∈ L_eff`,
and `F` is itself a closed lift of `γ`, so `|F| ≥ ℓ(γ)`. (b) upper bound is 5.3, lower bound is
5.4(4). (c) if `repair(γ) ≤ 2` then `min(repair(γ),2) = repair(γ)`, and (b) collapses. (d) combine.
∎ *Derivation status: (a), (b), (c) complete. (d) inherits the hypothesis of (c).*

**The gap, located precisely.** The only slack in (b) is the branch `m ≥ 1` of 5.4(3): a closed
lift may spend `2m` extra faults on residuals outside `γ` (or on triple copies of residuals inside
it) in order to reduce `wt(A_ess + xC)` below `repair(γ)`. Two mechanisms are available to it:

* *same-round pairing.* Two faults with a common residual `E'` in the same round contribute
  `(u' + u'') x^r` to `A` and nothing to `B`. This beats `|u' + u''|` measurement flips iff
  `|u' + u''| ≥ 3`, which requires `E'` to admit two representatives whose voltages differ in at
  least three checks.
* *prefix-sum toggling.* Two faults with residual `E'` in rounds `r' < r''` shift `xC` by
  `s(E')·(x^{r'+1} + … + x^{r''})`, i.e. they toggle `|s(E')|·(r''−r')` slots at once.

Both are excluded when `repair(γ) ≤ 2`, because either mechanism already costs 2. Neither is
excluded in general; §7.2 states what is now known about them — including that the first mechanism
**is realisable**, so the clean formula should not be expected to hold for `repair ≥ 3`.

**CONJECTURED 5.6bis (the pair gadget).** Let `E'` be any residual with `{0, s(E')} ⊆ U(E')`. Then
two faults with residual `E'` placed in the same round `r`, one with voltage `0` and one with
voltage `s(E')`, form a fault set of weight **2** with `π_1 = 0` and detector chain
`(1+x)·s(E')·x^r` — the same chain as `|s(E')|` separate measurement flips. Hence the mismatch
vector `s(E')x^r` can always be paid for at cost `min(|s(E')|, 2)`.

*Derivation.* `∂(f',r) + ∂(f'',r) = x^r[(0)(1+x) + s'x] + x^r[s'(1+x) + s'x] = x^r s'(1+x)`, while
`|s'|` measurement flips on the checks of `s'` in round `r` give `(1+x)s'x^r` as well. Both faults
have residual `E'`, so they cancel in `π_1`. ∎ *Status: complete.*

So the correct general statement of Theorem 2(b) is

```
   ℓ(γ)  =  |γ| + min_{m ≥ 0} ( 2m + repair_m(γ) ) ,      repair_0 = repair ,
```

a *minimum-cost generation* problem in `V` — unit cost for each `e_b x^r`, cost 2 for each
`s(E')x^r` with `{0,s(E')} ⊆ U(E')`, cost 2 for each split-pair chain — rather than a plain count.
Theorem 5.6(c) is the regime in which the plain count is provably optimal.

### 5.5 The node's biconditional

**CONJECTURED 5.7 (the criterion).** For every legal, measurement-consistent single-ancilla CSS
schedule `M`, and `R ≥ d`,

```
   d_circ( C_R(M) )  =  d_eff(M)      ⟺      ∃ γ ∈ L_eff  with  |γ| = d_eff(M)  and  repair(γ) = 0 .
```

Moreover `repair(γ) = 0` is decidable from one round of `M`, and the completion gap satisfies
`0 ≤ g(C) ≤ min{ repair(γ) : γ ∈ L_eff, |γ| = d_eff }`.

*Derivation.* (⟸) 5.3 gives `d_circ ≤ ℓ(γ) ≤ |γ| = d_eff`; 5.4(1) with `|π_1 F| ≤ |F|` gives
`d_circ ≥ d_eff`. (⟹) Let `F` be undetectable, logical, `|F| = d_eff`. Then `γ = π_1 F ∈ L_eff`
and `d_eff ≤ |γ| ≤ |F| = d_eff`, so `|γ| = d_eff` and the weight loss of 5.4(2) is zero:
`n_∅ = 0` and `m = 0`. `n_∅ = 0` forces `A_∅ = 0`, so by (LIFT) `A_ess + xC = 0`, i.e. the
certificate read off `F` has `wt = 0`; hence `repair(γ) = 0`. The gap bound is 5.3 applied to a
minimum-weight `γ`. ∎ *Derivation status: complete. Note this direction needs no hypothesis on
`repair` — the case `repair(γ) ≥ 3` cannot arise when `d_circ = d_eff`.*

This is the node's requested iff, with `volt(γ) = 0` made precise as `repair(γ) = 0`, i.e. by
(LIFT'): *there is a round assignment and a choice of unit-weight representatives under which, in
every round and on every check, the in-round measurement flips already equal the accumulated
syndrome parity.* The recon's Conj. 3.8 (`Σ_i u_i = 0`) is the same-round special case.

### 5.6 The `|γ| = 2` formula, derived

**CONJECTURED 5.8.** Let `γ = {E_1, E_2} ∈ L_eff`, so `s_1 = s_2 =: s`. Placing `E_1` in round `0`
and `E_2` in round `k ≥ 0`,

```
   wt(A_0 + xC)  =   | u_1 ⊕ u_2 |                                if k = 0
                 =   | u_1 | + (k−1)|s| + | u_2 ⊕ s |             if k ≥ 1
```

and therefore `repair(γ) = min over u_1 ∈ U(E_1), u_2 ∈ U(E_2)` of
`min( |u_1 ⊕ u_2| , |u_1| + |u_2 ⊕ s| , |u_2| + |u_1 ⊕ s| )`. Round gaps `k ≥ 2` are never optimal.

*Derivation.* `B = s(1 + x^k)`, so `C = s(1 + x + … + x^{k−1})` and `xC = s(x + … + x^k)`;
`A_0 = u_1 + u_2 x^k`. Adding: coefficient of `x^0` is `u_1` (`k ≥ 1`) or `u_1 + u_2` (`k = 0`); of
`x^j` for `1 ≤ j ≤ k−1` is `s`; of `x^k` is `u_2 + s`. The `k ≥ 2` claim: the expression exceeds
the `k = 1` value by `(k−1)|s| ≥ 0`, with equality only if `s = 0`, in which case `k ≥ 1` gives
`|u_1| + |u_2|` independently of `k`. ∎ *Status: complete. This is the d3-gate's §6.1 table,
now derived rather than asserted, and its `5 129 / 5 129` agreement run is a validation of exactly
this formula together with Theorem 5.6(c) in the regime `repair ∈ {0,1}`.*

### 5.7 Contiguity, the finite window, and `R`-saturation

**CONJECTURED 5.9 (no idle round).** Let `F` be a **minimum-weight** undetectable logical fault set
of `C_R(M)` (Z-memory sector). Then the set of rounds containing at least one fault of `F` is a
contiguous interval, and hence

```
   round-span( F )  ≤  |F|  =  d_circ  ≤  d .
```

*Derivation.* Suppose round `r` contains no fault of `F` while rounds `< r` and `> r` both do. By
(LIFT') at round `r`, `0 = U_b(r) = c_b(r−1)` for every `b`; and `c_b(r) = c_b(r−1) + 0 = 0`. Split
`F = F_1 ⊔ F_2` at `r` (`F_1` in rounds `< r`, `F_2` in rounds `> r`), both non-empty. For
`r' ≤ r`, `F_2` contributes nothing to `U(r')` and nothing to `c(r'−1)`, so `F_1` satisfies (LIFT')
there; for `r' > r`, `F_1` contributes `U^{F_1}(r') = 0` and `c^{F_1}_b(r'−1) = c_b(r−1) = 0`, so
(LIFT') holds there too. Hence `F_1` is undetectable, and symmetrically `F_2`. Finally
`λ(F) = λ(F_1) + λ(F_2) ≠ 0`, so at least one of them flips an observable while having strictly
smaller weight — contradicting minimality. ∎ *Derivation status: complete. The initial detector
`D_{b,0}` of Lemma 4.1 is what pins the constant in (LIFT'); with a noisy initialisation the lemma
fails at the first boundary.*

**CONJECTURED 5.10 (saturation and one-round decidability).** Consequences of 5.9:

1. `d_R(M) := d_circ(C_R(M))` is non-increasing in `R` and **constant for all `R ≥ d`**; i.e.
   `R_sat(M) ≤ d` in the sense of `CIRCDIST.sat`, for this model.
2. `d_circ` is computable from the one-round data `{(E(f), s(f), u(f), λ(f)) : f ∈ 𝔽}` alone, by a
   search over fault multisets of size `≤ d` distributed over `≤ d` consecutive rounds. No
   multi-round circuit is constructed at any point.
3. The minimisation in Definition 5.2 may be restricted to certificates with round-span `≤ |γ| +
   repair(γ)`, so `repair(γ)` is a finite computation.

*Derivation.* (1) More rounds give more fault locations, so `d_R` is non-increasing; a
minimum-weight witness of weight `w ≤ d` has span `≤ w ≤ d` by 5.9 and the bulk is
time-translation invariant with both temporal boundaries fully detectored (4.1), so it can be
translated into any `C_{R'}` with `R' ≥ w`. (2) is 5.9 plus (LIFT'): membership in `ker ∂` is
decided by the one-round data and the round assignment. (3) a certificate of larger span is
dominated by the closed lift it produces, whose weight is `≥` its span by 5.9 applied to a minimal
sub-lift. ∎ *Derivation status: (1) and (2) complete; (3) complete only for the sub-lift that
survives the split — for the certificate of a **fixed** `γ` the split may change `γ`, so (3) should
be read as "the minimum over certificates that are realised by a minimum-weight closed lift", which
is all that (a)–(d) of Theorem 5.6 ever uses.*

**Cross-node note.** 5.10(1) is a `CIRCDIST.sat` result obtained for free here, with
`B(r,d) = d`, but only inside this model (single-ancilla CSS, graph-like or not, ideal boundaries,
one memory sector at a time). It is much sharper than a generic pumping bound because the "state"
that must repeat is just `c(r) ∈ F₂^ℬ` and the argument only needs the state `0`.

### 5.8 Non-interleaved ⟹ equality (node requirement 6)

**CONJECTURED 5.11.** If `M` is non-interleaved, then `repair(γ) = 0` for **every** `γ ∈ L_eff`,
hence `d_circ(C_R(M)) = d_eff(M)` for all `R ≥ 1`.

*Derivation.* It suffices to exhibit a same-round certificate with `A_0 = 0` (then `C = 0` too,
since all `r_i` are equal, and `wt(A_0 + xC) = 0`).

*Case Z-block first.* Claim `0 ∈ U(E)` for every `E ∈ ℰ`. Hooks: every `q ∈ S` receives its `X` at
`t(a→q)`, which lies in the X-block, after **all** gates `q→b`; so `u_b(S) = 0` by 1.13.2. Bare
data errors `{q}`: insert the `X` after the last gate involving `q` — if that gate is `a→q` use the
two-qubit fault `I⊗X` on it, if it is `q→b` use `X⊗I`, if `q` has no gate use an idle location; in
all cases no gate `q→b` follows, so `u = 0`. Products of atoms inherit `u = 0`. Take all `u_i = 0`:
`A_0 = 0`.

*Case X-block first.* Claim `s(E) ∈ U(E)` for every `E ∈ ℰ`. Hooks: every `q ∈ S` receives its `X`
in the X-block, before **all** gates `q→b`, so `u_b(S) = |supp(b) ∩ S| = s_b(S)`. Bare data errors
`{q}`: insert the `X` before the first gate `q→b` — if `q ∈ supp(a)` for some `a`, the fault
`I⊗X` on the gate `a→q` does it (X-block precedes the Z-block); otherwise `q` is idle throughout
the X-block, which is non-empty, so an idle location works. Then `u = s`. Take `u_i = s_i`:
`A_0 = Σ_i s_i = ∂_eff γ = 0`.

In both cases `repair(γ) = 0`, so 5.3 gives `d_circ ≤ |γ|` for a minimum-weight `γ`, i.e.
`d_circ ≤ d_eff`; with 5.4(1), equality. ∎
*Derivation status: complete. The one corner — a data qubit whose only gate is `q→b` at the very
first step of the round, in the X-block-first case — is empty: such a `q` lies in no X-check, and
if the X-block is non-empty it occupies step `0`, so every Z-check CNOT is at a time `≥ 1` and `q`
is idle at step `0`; if the X-block is empty the schedule is also Z-block-first and the other case
applies.*

**Cross-reference (important; read before citing 5.11).** The non-interleaved corollary has an
independent, longer and more careful treatment in
`artifacts/circdist_lift_nonint_proof_20260820.md` (route `R4`, same date), which proves it as its
main theorem with every boundary case discharged. **The two derivations agree**, including on the
three things it is easy to get wrong:

* it also finds that **graph-likeness is not used** (its settlement S1) — independent confirmation
  of §7.3 here;
* its Lemma 5.4 is 5.11's claim, with the four residual sub-cases (`S_a(j)`, `S_a(0) = supp(a)`,
  `{q}` inside an X-check, `{q}` in no X-check) enumerated separately, which is where the corner
  above is closed properly;
* its Remark 6.4 (mixed-flavour closure: place the `u = 0` faults in round `r` and the `u = s`
  faults in round `r+1`, *in that order*) is exactly the `k = 1` branch of 5.8 here,
  `|u₁| + |u₂ ⊕ s| = 0`, and its observation that "the reverse assignment does not close"
  is the asymmetry of the two mirror terms in 5.8.

It also corrects the recon's "`G_circ` splits into `R` disjoint copies of `G_eff`" to a
weight-preserving **section** (its Prop. 6.2), measuring 120 of 444 X-sector faults of a
non-interleaved surface-code schedule to be non-horizontal — the same phenomenon as §3.5 here,
seen from the non-interleaved side. **§5.11 should be read as a corollary of Theorem 5.6 that
happens to reproduce that document's result, not as a competing proof**; where the two differ in
detail, prefer the dedicated document.

**Remark 5.12 (shift identity).** `∂(f, r)` with `(E, u)` equals `x·∂(f', r−1)` with `(E, u+s)`;
placing a fault one round earlier with the complementary voltage is the same spacetime object up to
a time shift. This is the formal version of "a residual created at the end of round `r−1` and one
created at the start of round `r` are the same error", and it is why `U(E)` should be viewed
modulo the involution `u ↦ u + s` together with a shift of `r`.

**Remark 5.13 (an independent derivation of Strikis–Browne–Beverland Cor. 1).** 5.11 recovers the
non-interleaved equality theorem from the lift picture, as the node's requirement 6 demands. The
mechanism it identifies — that a non-interleaved schedule makes the *whole* voltage cocycle
exact on the cheapest representatives — is the recon's Conj. 3.9 made precise; note that it is the
existence of a **uniform** choice (all `0`, or all `s`) that matters, not a per-fault statement.

**NUMERICAL 5.14.** Verified on the list-scheduled non-interleaved partners of the d3-gate's Steane
order set and of the surface order set of §3.6 (both legal, both `MC = ∅`):

| code | block order | residual classes `E ≠ ∅` | `0 ∈ U(E)` | `s(E) ∈ U(E)` |
|---|---|---|---|---|
| Steane | X first (depth 11) | 16 | 10 | **16** |
| Steane | Z first (depth 11) | 16 | **16** | 10 |
| surface | X first (depth 8) | 17 | 13 | **17** |
| surface | Z first (depth 8) | 17 | **17** | 13 |

Exactly the predicted dichotomy: the claimed inclusion holds for **all** classes, the other one only
for some. Both Steane non-interleaved circuits give `d_circ = 2 = d_eff` at `R = 2,3,4`. Code and
output in §9.3.

---

## 6. The theorems on the known instances

All five instances below sit in the regime `repair ≤ 1`, so Theorem 5.6(c) applies unconditionally
and the formula is an equality, not a bound. The `d_circ` column is the d3-gate report's exhaustive
weight-`≤3` enumeration (independently reproduced this session for the Steane rows, §9.4).

| instance | `γ` | `|γ|` | `s(γ)` | `U` data | `repair(γ)` | route | `ℓ(γ)` | `d_circ` |
|---|---|---|---|---|---|---|---|---|
| `[[4,2,2]]` valid IL witness | `{hook{2,3}}` | 1 | `0` | `U = {1}` (rigid) | **1** | `A_0 = u`, `C = 0` | 2 | **2** ✓ |
| Steane `M_IL` | `{X₃, hook{2,6}}` | 2 | `(1,0,0)` | both rigid, `u₁ ⊕ u₂ ≠ 0` | **1** | same round | 3 | |
| | `{X₂, hook{4,5}}` | 2 | `(0,1,1)` | | **1** | same round | 3 | |
| | `{X₅, hook{0,6}}` | 2 | `(1,1,0)` | | **1** | same round | 3 | |
| | `{X₀,X₁,X₂}` (bare) | 3 | `0` | `0 ∈ U` each | 0 | same round | 3 | **3** ✓ |
| Steane `M_NI` | the same three weight-2 `γ` | 2 | — | `0 ∈ U(E)` each | **0** | same round | 2 | **2** ✓ |
| surface `M_IL` / `M_NI` | `{X₇, hook{1,4}}`, `{X₈, hook{1,4}}` | 2 | `(0,1,0,0)` | `|s| = 1`, so `u ∈ {0,s}` | **0** | same round or `k=1` | 2 | **2** ✓ |

**Reading the `[[4,2,2]]` row.** `γ` is a single residual with `s = 0` and `λ = 1`, so
`d_eff = 1`; `B = 0`, `C = 0`, and `repair(γ) = min_{u ∈ U(E)} |u| = 1` because the unique
achievable voltage is `u = e_b ≠ 0`. Theorem 5.6(c) then *forces* `ℓ(γ) = 2`, and 5.7 forces
`d_circ > d_eff`. This is the recon's "pure vertical edge" picture, and note that Theorem 1 is
consistent with it: `|supp(a) ∩ supp(b)| = 4` there, exactly at the threshold.

**Reading the Steane `M_IL` rows.** The three weight-2 effective logicals each have `repair = 1`,
so `ℓ = 3` for each; the weight-3 effective logicals (three bare data errors forming `Z_L`) have
`repair = 0`, so `ℓ = 3` as well. `min_γ ℓ(γ) = 3 = d_circ`. The gap `g(C) = 1` is therefore
*exactly* the statement "every minimum-weight `γ` has `repair(γ) = 1`", which is 5.7.

**The surface-code row and Theorem 1.** The d3-gate's exhaustive order scan established that every
weight-2 effective logical of the rotated `d = 3` surface code has `|s| = 1`. Combined with
Theorem 3.5 (containment) this gives `u ∈ {0, s}` for both members of any such `γ`, hence
`repair(γ) = 0` by 5.8 (`k = 0` if `u₁ = u₂`, `k = 1` otherwise), hence `d_circ = d_eff` for every
measurement-consistent schedule and every within-check order — the d3-gate's Conj. 4.1, now with
the `k = 1` step derived from 5.8 rather than asserted. **The `|s| = 1` input is essential and is a
fact about this specific small code**, not a consequence of overlap `≤ 2` (§3.5, §3.7).

---

## 7. Status, hypotheses, and the located gap

### 7.1 What each theorem needs

| statement | (CSS) | legality | (MC) | ideal boundaries | graph-like | (V) | derivation |
|---|---|---|---|---|---|---|---|
| 2.2 validity ⟺ (MC) | ✓ | ✓ | — | initialisation only | — | — | complete |
| 3.2 **Theorem 1** | ✓ | ✓ | ✓ | — | — | — | **complete** |
| 3.4 sharpness at overlap 2 | ✓ | ✓ | — | — | — | — | complete |
| 3.5 containment | ✓ | ✓ | ✓ | — | — | — | complete |
| 4.1 no boundary correction | — | — | — | ✓ **both ends** | — | — | complete |
| 4.2 / 4.3 (LIFT), (LIFT') | — | — | — | ✓ | — | — | complete |
| 5.3 `ℓ ≤ |γ| + repair` | — | — | — | ✓ | — | ✓ | complete |
| 5.4 exact accounting | — | — | — | ✓ | — | ✓ | complete |
| 5.6(c) **Theorem 2**, `repair ≤ 2` | — | — | — | ✓ | — | ✓ | **complete** |
| 5.6(b) general sandwich | — | — | — | ✓ | — | ✓ | complete |
| 5.7 **the iff** | — | — | — | ✓ | — | ✓ | **complete** |
| 5.9 contiguity | — | — | — | ✓ | — | — | complete |
| 5.11 non-interleaved | ✓ | ✓ | (automatic) | ✓ | — | — | complete up to a stated corner |
| 7.1 voltage spread `≤ 2` | — | — | — | — | **✓** | — | complete (the only use of Def. 1.12) |
| 5.6 for `repair ≥ 3` | — | — | — | ✓ | — | ✓ | **GAP — §7.2** |

(MC) is needed for Theorem 1 but **not** for Theorem 2: Theorem 2 only needs the circuit to have
deterministic detectors so that `d_circ` is defined, which is (MC) by 2.2 — i.e. (MC) enters
Theorem 2 as a well-definedness condition, not as a step of the argument.

### 7.2 The gap, stated so a future session can attack it directly

> **GAP (repair ≥ 3).** Is `ℓ(γ) = |γ| + repair(γ)` for all `γ`, or can a closed lift beat the
> repair certificate by using extra residuals?

Concretely, 5.4(3) leaves open whether

```
   min_{m ≥ 1} ( 2m + repair_m(γ) )  <  repair(γ)                                       (ESC)
```

is possible, where `repair_m(γ)` is the analogue of Definition 5.2 for certificates carrying `2m`
extra faults with residuals cancelling in `π_1`. (ESC) requires `repair(γ) ≥ 3`. Two sub-questions,
in increasing order of difficulty:

1. **Same-round escape — answered, and the answer splits on graph-likeness.**
   The question was: does a realisable residual `E'` admit `u', u'' ∈ U(E')` with `|u'+u''| ≥ 3`?

   **CONJECTURED 7.1 (graph-likeness kills the same-round escape).** If `M` is graph-like
   (Def. 1.12) then for every residual `E` and all `u', u'' ∈ U(E)`, `|u' + u''| ≤ 2`. More
   precisely `|s(E)| ≤ 2` and `U(E)` is contained in the subgroup generated by `{e_b : b ∈ supp
   s(E)}` when `s(E) ≠ 0`, and in `{0} ∪ {e_b}` when `s(E) = 0`.

   *Derivation.* Graph-likeness says `|u| + |u+s| ≤ 2`; since `s = u + (u+s)`, `|s| ≤ 2`.
   • `|s| = 0`: `2|u| ≤ 2`, so `|u| ≤ 1`, and `|u'+u''| ≤ 2`.
   • `|s| = 1`, `s = e_b`: if `u_b = 1` then `|u| + |u+e_b| = 1 + 2|u ∖ b| ≤ 2` forces `u = e_b`;
   if `u_b = 0` then `2|u| + 1 ≤ 2` forces `u = 0`. So `U(E) ⊆ {0, e_b}` and `|u'+u''| ≤ 1`.
   • `|s| = 2`, `s = e_b + e_c`: writing `u = αe_b + βe_c + v` with `v` disjoint from `{b,c}`,
   `|u| + |u+s| = 2 + 2|v| ≤ 2` forces `v = 0`, so `U(E) ⊆ {0, e_b, e_c, s}`, a subgroup of order 4
   all of whose elements have weight `≤ 2`. ∎ *Status: complete.*
   (Side effect: in a graph-like model `u ⊆ s` holds automatically whenever `s ≠ 0`, so Lemma 3.5's
   content is entirely in its `s_b = 0` components — which is exactly Theorem 1.)

   **NUMERICAL 7.2 (but the campaign's own witness is not graph-like).** In the Steane code the
   singleton residual `E' = {6}` — qubit 6 lies in **all three** Z-checks, so `|s| = 3` — admits
   `u' = (0,0,0)` and `u'' = (1,1,1) = s(E')`, spread **3**, in *every* measurement-consistent
   schedule tested: the d3-gate's interleaved witness, both non-interleaved partners, and **349 of
   349** Steane offset-family schedules at depths 9, 10, 11. By 5.6bis those two faults repair three
   units of mismatch at cost 2. The rotated surface code's maximum spread is 2 (no data qubit lies
   in three Z-checks). Code and output in §9.5.

   By 7.1 this can only happen because **the Steane Z-memory sector is not graph-like** — the bare
   error `X₆` flips three detectors. (`artifacts/circdist_lift_nonint_proof_20260820.md` reaches the
   same conclusion from the other side, its settlement S1.) So: *inside* the graph-like model the
   same-round escape is impossible; *outside* it — which is where the campaign's only `d = 3` gap
   instance actually lives — it is available and generic.
2. **Toggling escape — survives graph-likeness.** Two faults with residual `E'` in rounds
   `r' < r''` give the chain `s'x^{r'} + u''x^{r'+1} + (u''+s')x^{r'+2}` for `r'' = r'+1` with
   `u' = s'`. Taking `|s'| = 2`, `s' = e_b + e_c`, and `u'' = e_b` (both allowed by 7.1) gives
   `D` with `D_b = x^{r'}`, `D_c = x^{r'} + x^{r'+1}`, i.e. `wt(D) = 3` **for 2 faults**, inside a
   graph-like model. So (ESC) is not excluded even under graph-likeness, and 7.1 does not rescue
   the clean formula — it only localises the escape to the split-pair gadget. Contiguity (5.9)
   bounds `r'' − r' ≤ d`, so the search is finite; what is unknown is whether an optimal certificate
   can ever leave its mismatch in such an aligned pattern.
3. **Completeness of the gadget list.** Are the unit, pair and split-pair gadgets of 5.6bis all the
   irreducible `π_1`-null fault sets, and does decomposing an optimal lift into gadgets lose
   nothing (i.e. do gadgets interact with the essential faults)? This is the step that would turn
   `ℓ(γ) = |γ| + min_m(2m + repair_m(γ))` into a closed-form min-cost covering problem.

**Why the numerics do not settle it.** The d3-gate's `5 129 / 5 129` agreement run and this
session's reproductions are all in the regime `repair ∈ {0,1}`, where Theorem 5.6(c) is a theorem
and agreement is *forced*. The agreement is therefore evidence that the *implementation* and the
*model* are right; it is **not** evidence about (ESC). Exhibiting (ESC) needs `repair(γ) ≥ 3` with
`|γ| + 2 ≤ d`, hence `d ≥ d_eff + 2 ≥ 5` — outside every instance examined in this campaign.

**Recommended attack, revised in the light of 7.1.** Do **not** try to prove the clean formula; the
pair gadget makes it unlikely. Instead: (i) settle sub-question 3, which converts Theorem 2 into an
exact min-cost covering statement with an explicit generating set — that is a *better* theorem than
the clean formula and it is what the decision algorithm actually needs; and (ii) look for an
explicit (ESC) instance on a `d ≥ 5` code (a `[[n,k,5]]` HGP or a small bivariate-bicycle code) to
pin the formula's failure by example. Either outcome is a settlement.

### 7.3 Two hypotheses that are *not* used, and one that is everything

**Graph-likeness is not used.** No step of §2–§5 invokes Definition 1.12. Theorem 1 is a parity
count; Theorem 2 is bookkeeping over `F₂[x,x⁻¹]` plus (V). Graph-likeness is needed only for the
*pictures* — the recon's edge taxonomy, the derived-graph language of §4.4, and the phrase
"timelike voltage" — and for connecting to matching decoders. The theorems as stated therefore
apply verbatim to hypergraph-like detector error models of single-ancilla CSS extraction circuits.
This is a strict strengthening relative to the node's commission, and it should be reported as such
rather than silently enjoyed — the more so because the campaign's only `d = 3` gap instance (the
Steane Z-memory sector) is **not** graph-like: `X₆` flips three detectors. The one place
graph-likeness does have content is the *gap*, where Lemma 7.1 uses it to bound `|s(E)| ≤ 2` and
the voltage spread by 2; even there it does not close the gap.

**Time-translation invariance in the bulk is used and is safe.** Rounds are identical by
hypothesis (公共定义), so `E, s, u, λ` are round-independent (Definition 1.10). A schedule that
varied round to round would break Definition 5.2 but not (LIFT').

**(V) — `U(∅) ⊆ {0} ∪ {e_b}` — is everything.** It is what makes `repair` a *count* rather than a
covering number, and it is the single point where "single-ancilla CSS with one classical outcome
per check per round" enters. Multi-ancilla, flag, or cat-state schedules (out of scope per the
公共定义) would generally admit empty-residual faults of voltage weight 2, and then 5.4(3) fails at
`n_∅ ≥ wt(A_∅)` and the entire lower bound collapses. Any attempt to extend this node beyond the
公共定义 must re-derive (V) first.

### 7.4 Honest limitations

1. **Nothing is proved.** All derivations are mine, written this session, without independent
   review. The most likely error sites, in order: 2.2 Step 2 (the independence-between-rounds
   claim), 5.4(3) (the inequality `n_∅ ≥ wt(A_∅)`, which silently assumes every empty-residual
   fault contributes **at most** one monomial — true by (V), but (V) itself is an inventory claim),
   and 5.10(3) (flagged in its own status line).
2. **Per-sector.** Everything is stated for one memory sector. `d_circ(C) = min` of the two, and
   `repair` must be computed twice. The d3-gate's Steane witness lifts the Z-sector only; nothing
   here changes that.
3. **`d_eff` uses residual multiplicity, not qubit weight.** `|γ|` counts residuals. This matches
   `d_ext` of the 公共定义 and of arXiv:2603.05481, and is the reason `π_1` is weight-non-increasing.
4. **No Lean, and no claim of machine-checkability.** Per the node's ground rules.
5. **The literature anchors are inherited, not re-verified this session.** In particular
   arXiv:2603.05481 Thm. 1/Cor. 1 (of which 5.11 is an independent re-derivation) is used only as a
   consistency check, never as a premise; `[GT87, Thm. 2.1.2]` is cited only in §4.4, where it is
   explanatory. The systole warning of `circdist_lift_litverify2_20260820.md` is answered at the
   level of Remark 5.5 and nowhere assumed.

---

## 8. What this changes for the node

1. **The node's minimum acceptance condition is met, modulo the epistemic ceiling.** A non-trivial
   necessary-and-sufficient condition in the graph-like, fixed-boundary model is 5.7; it covers the
   non-interleaved equality (5.11, derived, not cited) and the interleaved strict inequality (the
   d3-gate's Steane pair, re-derived here as `repair = 1` in §6).
2. **Routes to reprice.** `R1 laurent-group-ring` — its premises `P1.1`, `P1.2`, `P1.3` are 1.11,
   4.1, 4.2; `P1.4` (finite window) is **discharged** by 5.9 with `B(r,d) = d`; `P1.5` (boundary
   quotient) is **retired** by 4.1 (there is no quotient). What remains of R1 is exactly §7.2.
   `R3 boundary-ramification` should be **closed as unnecessary** in this model. `R2
   voltage-monodromy-lift` should be re-registered on the multigraph `G̃_eff` (§4.4) or dropped.
   `R4 noninterleaved-horizontal-representative` is discharged by the dedicated parallel document
   `artifacts/circdist_lift_nonint_proof_20260820.md`, which §5.11 independently agrees with
   (cross-reference after 5.11). `R6 gap-formula-and-decision-algorithm` — its `P6.1` and `P6.3`
   are done (5.3, 5.10(2)); its `P6.2` (matching lower bound) is done for `repair ≤ 2` (5.6) and
   is §7.2 otherwise, where 5.6bis says the plain-count form of `P6.2` is probably **false** and
   should be replaced by the min-cost-covering form.
3. **A new premise for `CIRCDIST.gross`, replacing the d3-gate's §8 lead.** Withdraw "no gross-code
   hook can carry timelike voltage". Register instead: *(i)* no gross-code hook is a **vertical**
   edge (Theorem 1, since all overlaps are `≤ 2`); *(ii)* every gross-code hook has `|s| ≥ 3`
   (NUMERICAL 3.7), so diagonal hooks are the generic case and the surface-code `|s| = 1` argument
   has no analogue; *(iii)* the question "is there a distance-12 interleaved gross circuit?" is,
   under 5.7, exactly the question "does every weight-11 `γ ∈ L_eff` of every measurement-consistent
   schedule have `repair(γ) ≥ 1`, and does some `γ` achieve `|γ| + repair(γ) = 12`?". That is a
   one-round computation per schedule (5.10(2)) — expensive but not exponential in `R`.
4. **A `CIRCDIST.sat` deliverable falls out.** 5.10(1): `R_sat(M) ≤ d` for every single-ancilla CSS
   schedule with ideal boundaries, per sector. The `sat` node should check whether its commission's
   model coincides with §1 before adopting it.
5. **The gate that was going to be recommended was instead run, and it fired — with a twist.**
   §7.2 sub-question 1 ("does any realisable residual admit two unit-weight voltages differing on
   `≥ 3` checks?") is **yes outside the graph-like model** (NUMERICAL 7.2, 349/349 Steane
   schedules) and **no inside it** (7.1, proved). But the split-pair gadget of §7.2 item 2 escapes
   even under graph-likeness. Consequences: (a) the clean formula `ℓ = |γ| + repair` should **not**
   be the target of a future session — the min-cost-covering form (§7.2 sub-question 3) should be;
   (b) the campaign should stop describing its instances as graph-like without checking — the
   `d = 3` Steane witness, the campaign's only genuine gap instance, is **not** graph-like in the
   Z-memory sector, and neither is the `[[4,2,2]]` mechanism's natural generalisation. The node's
   commissioned scope ("graph-like detector error model") is therefore narrower than the phenomena
   the campaign is actually studying, which is a scope question for the dispatcher, not a defect —
   §7.3 shows the theorems do not need the hypothesis.

---

## 9. NUMERICAL — code and outputs

Python 3.9.6, stdlib only (`stim 1.16.0` is installed in this environment but is **not** used by
any run below; the `stim` cross-checks quoted in §6 are the d3-gate report's).

**Base layer.** `Code`, `build_steps`, `legal`, `qtime`, `Sim.run`, `Sim.locations` are reused
**unchanged** from `artifacts/circdist_lift_d3gate_20260820.md` §10.1–10.2, and `SURF`, `STEANE`
from its §10.2. The (MC) predicate is its `consistency_violations`, renamed `mc_violations`. Only
the new code is reproduced here. All schedules used below are reported with their legality and
(MC) status in the outputs.

### 9.1 Gross code, overlap and hook-syndrome histograms (Theorem 1 input, §3.7)

```python
def gross_code():
    """[[144,12,12]] bivariate bicycle, l=12, m=6, A=x^3+y+y^2, B=y^3+x+x^2."""
    l, m = 12, 6
    N = l * m
    def idx(i, j):
        return (i % l) * m + (j % m)
    xchecks, zchecks = {}, {}
    Aterms = [(3, 0), (0, 1), (0, 2)]
    Bterms = [(0, 3), (1, 0), (2, 0)]
    for i in range(l):
        for j in range(m):
            xchecks['X%d_%d' % (i, j)] = (
                [idx(i + a, j + b) for (a, b) in Aterms] +
                [N + idx(i + a, j + b) for (a, b) in Bterms])
            zchecks['Z%d_%d' % (i, j)] = (
                [idx(i - a, j - b) for (a, b) in Bterms] +
                [N + idx(i - a, j - b) for (a, b) in Aterms])
    return Code(2 * N, xchecks, zchecks, zl=[], xl=[], name="gross [[144,12,12]]")


def overlaps(code):
    h = {}
    for a, s in code.xchecks.items():
        for b, t in code.zchecks.items():
            k = len(set(s) & set(t)); h[k] = h.get(k, 0) + 1
    return h

# |s(S)| over all non-trivial subsets S of one X-check support
G = gross_code(); a0 = G.xnames[0]; supp = G.xchecks[a0]; hist = {}
for r in range(1, len(supp)):
    for S in combinations(supp, r):
        w = sum(G.syn(S, 'Z')); hist[w] = hist.get(w, 0) + 1
```

```
overlap histograms
  rotated [[9,1,3]] surface    {2: 8, 0: 8}
  Steane [[7,1,3]]             {4: 3, 2: 6}
  gross [[144,12,12]]          {0: 4536, 2: 648}

gross code, check X0_0, supp [18, 1, 2, 75, 78, 84]
  |s| histogram over all 62 non-trivial subsets: {3: 12, 4: 18, 5: 18, 6: 12, 9: 2}
    |s|=3  example S=(18,)      -> checks ['Z3_3', 'Z4_0', 'Z5_0']
    |s|=4  example S=(18, 75)   -> checks ['Z0_4', 'Z0_5', 'Z4_0', 'Z5_0']
    |s|=5  example S=(18, 1, 75)-> checks ['Z0_5','Z1_1','Z2_1','Z4_0','Z5_0']
    |s|=6  example S=(18, 1)    -> checks ['Z0_4','Z1_1','Z2_1','Z3_3','Z4_0','Z5_0']
    |s|=9  example S=(18, 1, 2) -> 9 checks
```

The `Code` constructor asserts `|supp(a) ∩ supp(b)|` even for all pairs, so `H_X H_Zᵀ = 0` is
re-verified as a side effect. Minimum `|s|` over gross-code hooks is **3**; `|s| = 1` never occurs.

### 9.2 Hook classification and the diagonal-hook search (§3.6)

```python
def hook_table(code, orders, times):
    """for every X-check a and every proper suffix S of its order, return (a,S,s,u)"""
    T = {c: qtime(orders, times, c) for c in code.names}
    out = []
    for a in code.xnames:
        oa = orders[a]
        for j in range(1, len(oa)):
            S = set(oa[j:]); s = []; u = []
            for b in code.znames:
                inter = S & set(orders[b])
                s.append(len(inter) % 2)
                u.append(sum(1 for q in inter if T[b][q] > T[a][q]) % 2)
            out.append((a, tuple(sorted(S)), tuple(s), tuple(u)))
    return out


def classify(s, u):
    if all(v == 0 for v in u):   return 'horizontal-late'
    if u == s:                   return 'horizontal-early'
    if all(v == 0 for v in s):   return 'VERTICAL'
    return 'DIAGONAL'

# scan: all X-orders of XA x all depth-8 offset schedules, keep legal AND (MC)
```

```
C1a  rotated surface code, depth-8 offset family, all XA orders
   measurement-consistent schedules scanned: 98811
   hook-edge classes: {'horizontal-early': 321059, 'horizontal-late': 321059,
                       'DIAGONAL': 148370, 'VERTICAL': 0}
   first DIAGONAL with |S| >= 2 :
     X orders : XA=[1,2,4,5] XB=[3,4,6,7] XC=[0,1] XD=[7,8]
     Z orders : ZA=[0,1,3,4] ZB=[4,5,7,8] ZC=[2,5] ZD=[3,6]
     times    : XA=[0,1,2,3] XB=[0,1,2,3] XC=[0,1] XD=[0,1]
                ZA=[1,2,3,4] ZB=[0,1,2,3] ZC=[3,4] ZD=[6,7]
     check XB, hook S=(6, 7),  s=(0,1,0,1)  u=(0,0,0,1)  (znames ZA,ZB,ZC,ZD)
     u contained in s: True   u==0: False   u==s: False   MC violations: []
```

`VERTICAL: 0` is Theorem 1 on 790 488 hook-edge classes; `DIAGONAL: 148 370` is §3.5.

### 9.3 `U(∅)` — verification of (V) (§1.14)

```python
def one_round_profiles(code, steps):
    """(residual -> set of achievable u) over all elementary faults of a single round"""
    sim = Sim(code, steps, 1); prof = {}
    for loc in sim.locations():
        m, fx, fz = sim.run(loc)
        E = frozenset(q for q in range(code.n) if fx[q])
        prof.setdefault(E, set()).add(tuple(m[(c, 0)] for c in code.znames))
    return prof
```

```
Steane M_IL  (legal=True, MC-violations=[], depth 8)
   U(0) = [(0,0,0), (0,0,1), (0,1,0), (1,0,0)]   all weight<=1 : True   17 residual classes
Steane M_NI  (legal=True, MC-violations=[], depth 11)
   U(0) = [(0,0,0), (0,0,1), (0,1,0), (1,0,0)]   all weight<=1 : True   17 residual classes
surface (the §9.2 diagonal schedule)
   U(0) = [(0,0,0,0),(0,0,0,1),(0,0,1,0),(0,1,0,0),(1,0,0,0)]  all weight<=1 : True
```

### 9.4 Contiguity (5.9) and reproduction of the d3-gate's Steane A/B pair (§6)

`all_min_logicals` is the d3-gate's `circuit_distance` meet-in-the-middle, modified to return
**every** minimum-weight solution rather than the first; `fault_round(loc)` extracts the round
index from a fault label.

```python
def fault_round(loc):
    return loc[2] if loc[0] in ('prep', 'meas') else loc[1]

for s in sols:
    rr = sorted(set(fault_round(l) for l in s))
    span = rr[-1] - rr[0] + 1
    contiguous = (rr == list(range(rr[0], rr[-1] + 1)))
```

```
  Steane M_IL R=2 : d_circ=3  #cols=149  #dets=12  #min-logicals=897
      span histogram {1: 441, 2: 456}     span<=weight: True   contiguous: True
  Steane M_IL R=3 : d_circ=3  #cols=285  #dets=18  #min-logicals=1242
      span histogram {1: 660, 2: 579, 3: 3}  span<=weight: True   contiguous: True
  Steane M_IL R=4 : d_circ=3  #cols=421  #dets=24  #min-logicals=1659
      span histogram {1: 879, 2: 777, 3: 3}  span<=weight: True   contiguous: True
  Steane M_NI R=2 : d_circ=2  #cols=149  #dets=12  #min-logicals=15
      span histogram {1: 11, 2: 4}        span<=weight: True   contiguous: True
  Steane M_NI R=3 : d_circ=2  #cols=281  #dets=18  #min-logicals=19
      span histogram {1: 12, 2: 7}        span<=weight: True   contiguous: True
  Steane M_NI R=4 : d_circ=2  #cols=413  #dets=24  #min-logicals=23
      span histogram {1: 13, 2: 10}       span<=weight: True   contiguous: True
```

`d_circ = 3` vs `2` and the column/detector counts (149/285/421, 12/18/24) reproduce the d3-gate's
§5.2/§5.3 tables exactly under an independently written detector layer, which is the intended
cross-check of Definition 1.6. **3 855 minimum-weight undetectable logicals, every one contiguous
with span `≤` weight** — Lemma 5.9 confirmed. (The `M_NI` used here is the list-scheduled legal
non-interleaved partner of §9.5, depth 11, not the depth-10 one quoted in the d3-gate; the
distances agree.)

### 9.5 Non-interleaved dichotomy (5.14) and the pair-gadget gate (7.2)

```python
def list_schedule(code, orders, group, t0):
    """earliest-step list scheduling of one block, preserving within-check order"""
    times = {}; busy = {}
    for c in group:
        a = code.anc[c]; prev = t0 - 1; ts = []
        for q in orders[c]:
            t = prev + 1
            while busy.get((t, a)) or busy.get((t, q)):
                t += 1
            busy[(t, a)] = True; busy[(t, q)] = True
            ts.append(t); prev = t
        times[c] = ts
    return times


def noninterleaved(code, orders, xfirst=True):
    g1 = code.xnames if xfirst else code.znames
    g2 = code.znames if xfirst else code.xnames
    t1 = list_schedule(code, orders, g1, 0)
    t2 = list_schedule(code, orders, g2, max(max(v) for v in t1.values()) + 1)
    t = dict(t1); t.update(t2); return t


def spread(code, steps):
    """max_E max_{u',u'' in U(E)} |u' xor u''|  -- the sec.7.2 sub-question 1 gate"""
    prof = one_round_profiles(code, steps); best = (0, None, None, None)
    for E, U in prof.items():
        for u1 in U:
            for u2 in U:
                w = sum(a ^ b for a, b in zip(u1, u2))
                if w > best[0]:
                    best = (w, sorted(E), u1, u2)
    return best
```

```
Steane non-interleaved, X-block first : depth=11 legal=True MC=[]
   non-empty residual classes: 16 ;  0 in U(E): 10 ;  s(E) in U(E): 16
   R=2,3,4 : d_circ = 2, 2, 2
   times: X1=[0,1,2,3] X2=[0,1,2,3] X3=[0,1,3,4] Z1=[5,6,7,8] Z2=[5,6,7,8] Z3=[6,7,9,10]
Steane non-interleaved, Z-block first : depth=11 legal=True MC=[]
   non-empty residual classes: 16 ;  0 in U(E): 16 ;  s(E) in U(E): 10
   R=2,3,4 : d_circ = 2, 2, 2
   times: Z1=[0,1,2,3] Z2=[0,1,2,3] Z3=[1,2,4,5] X1=[6,7,8,9] X2=[6,7,8,9] X3=[6,7,9,10]
surface non-interleaved, X-block first : depth=8 legal=True MC=[] ; 17 classes, 0 in U: 13, s in U: 17
surface non-interleaved, Z-block first : depth=8 legal=True MC=[] ; 17 classes, 0 in U: 17, s in U: 13

C6  max |u' xor u''| over u',u'' in U(E)
  Steane M_IL (d3gate witness)   legal MC  max spread = 3   E=[6]  u'=(0,0,0) u''=(1,1,1)
  Steane NI X-first              legal MC  max spread = 3   E=[6]  u'=(0,0,0) u''=(1,1,1)
  Steane NI Z-first              legal MC  max spread = 3   E=[6]  u'=(0,0,0) u''=(1,1,1)
  surface diagonal-hook sched              max spread = 2   E=[]   u'=(0,0,0,1) u''=(0,0,1,0)

  sweep of Steane offset-family schedules for spread >= 3 :
    depth  9 cumulative: scanned   7, spread>=3 in   7
    depth 10 cumulative: scanned  58, spread>=3 in  58
    depth 11 cumulative: scanned 349, spread>=3 in 349
    example: depth 9  X1=[0,1,2,3] X2=[0,1,2,3] X3=[1,2,3,4]
                      Z1=[3,4,5,6] Z2=[5,6,7,8] Z3=[4,5,6,7]
             E=[6]  u'=(0,0,0) u''=(1,1,1)  |xor|=3   (znames Z1,Z2,Z3)
```

The dichotomy table is exactly 5.11's prediction: the claimed inclusion holds for **all** residual
classes in each case, the other one for only some. The spread rows are NUMERICAL 7.2: qubit 6 lies
in all three Steane Z-checks, so its bare-data residual admits both `u = 0` and `u = s = (1,1,1)`,
and by 5.6bis two such faults in one round repair three units of mismatch at cost two. Note
`|s({6})| = 3`, so this residual violates graph-likeness (Def. 1.12) — consistent with Lemma 7.1,
which forbids spread `> 2` inside the graph-like model. The rotated surface code's maximum spread
is 2 (its maximum data Z-degree is 2), and it *is* graph-like, which is the structural reason the
same-round escape cannot occur there.

### 9.6 End-to-end check of (LIFT') and of the exact weight accounting (4.3, 5.4(2))

The central algebraic identity is checked directly against the DEM solutions, not assumed: for
every minimum-weight undetectable logical `F` found by exhaustive enumeration, each fault's
one-round `(E, s, u)` is recomputed at round 0 and (LIFT') `U_b(r) = c_b(r−1)` is tested for every
check `b` and every `r ∈ {0,…,R}`; separately, `|F| = |γ| + n_∅ + 2m` is tested with `γ` and `m`
read off the residual multiplicities.

```python
def to_round0(loc):
    l = list(loc); l[2 if loc[0] in ('prep', 'meas') else 1] = 0; return tuple(l)

for F in sols:
    info = [(fault_round(l),) + data[to_round0(l)] for l in F]     # (round, E, s, u)
    for r in range(0, R + 1):
        for bi in range(len(code.znames)):
            U = sum(u[bi] for (rr, E, s, u) in info if rr == r) % 2
            c = sum(s[bi] for (rr, E, s, u) in info if rr <= r - 1) % 2
            assert U == c                                          # (LIFT')
    n = {}
    for (rr, E, s, u) in info:
        n[E] = n.get(E, 0) + 1
    gamma = [E for E, k in n.items() if E and k % 2]
    m2 = sum(k for E, k in n.items() if E) - len(gamma)            # = 2m
    assert len(F) == len(gamma) + n.get(frozenset(), 0) + m2 and m2 % 2 == 0
```

```
  Steane M_IL           R=2  w=3  #logicals= 897   (LIFT') violations: 0   accounting violations: 0
  Steane M_IL           R=3  w=3  #logicals=1242   (LIFT') violations: 0   accounting violations: 0
  Steane M_IL           R=4  w=3  #logicals=1659   (LIFT') violations: 0   accounting violations: 0
  Steane M_NI (X-first) R=2  w=2  #logicals=  15   (LIFT') violations: 0   accounting violations: 0
  Steane M_NI (X-first) R=3  w=2  #logicals=  19   (LIFT') violations: 0   accounting violations: 0
  Steane M_NI (X-first) R=4  w=2  #logicals=  23   (LIFT') violations: 0   accounting violations: 0
```

**3 855 / 3 855 minimum-weight undetectable logicals satisfy (LIFT') and the exact weight
accounting, with zero violations**, on both sides of the campaign's A/B pair and at three round
counts. This is the strongest available check of Prop. 4.3 and 5.4(2), which are the two steps
everything else rests on; note it is a check of the *derivations*, not of the model, since both
sides are computed from the same propagator.

### 9.7 Reproducibility and independence

Two implementation layers were used: this session's own `F₂` propagator (inherited from the
d3-gate's §10.1, which is itself independent of `stim`) and this session's independently written
detector/observable layer (Definition 1.6). The agreement of §9.4's column and detector counts with
the d3-gate's `stim`-confirmed numbers transitively re-checks the detector definitions against
`stim`. **This is not full independence**: the fault-location set (Definition 1.8) is the same
design in all layers, so a systematic modelling error would survive. Scripts live in this session's
scratchpad and are reproduced above in full; nothing outside `artifacts/` was written.

---

## 10. One-paragraph statement of the result, for the node record

*In the graph-like (indeed arbitrary) detector error model of a single-ancilla CNOT-based CSS
syndrome-extraction schedule with ideal memory-experiment boundaries: (1) measurement consistency
is equivalent to determinism of the detectors, and under it a hook of an X-check `a` can flip a
Z-check `b`'s outcome without leaving syndrome on `b` only when `|supp(a) ∩ supp(b)| ≥ 4`, with the
converse holding at overlap exactly 2; (2) the spacetime detector complex is the effective complex
over `F₂[x,x⁻¹]` with `π₀` the augmentation, the finite-`R` truncation is isometric, a fault set is
undetectable exactly when in every round and on every check the in-round measurement flips equal
the accumulated syndrome parity, a minimum-weight undetectable logical occupies at most `d`
consecutive rounds, and consequently `d_circ = min_{γ ∈ L_eff}(|γ| + repair(γ))` with `repair`
computed from one round whenever `repair ≤ 2`, giving `d_circ = d_eff` if and only if some
minimum-weight effective logical has `repair = 0`; non-interleaved schedules always have
`repair ≡ 0`. The remaining gap is the exact repair cost when it exceeds 2, where a weight-2 pair
gadget can undercut the plain count.*
