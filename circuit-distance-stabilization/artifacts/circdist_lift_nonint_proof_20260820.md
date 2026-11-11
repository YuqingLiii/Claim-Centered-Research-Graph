# CIRCDIST.lift — the non-interleaved corollary, proved in the Laurent/group-ring framework

**Date:** 2026-08-20 · **Node:** `CIRCDIST.lift` · **Frontier item:** route `R4`
(`noninterleaved-horizontal-representative`), commissioned as one budget-boxed executor session.
**Session type:** Opus 5 executor, proposer role. No sub-agents. No Lean.

**Target statement.** For every measurement-consistent, non-interleaved, single-ancilla CNOT
syndrome-extraction schedule `M` of a CSS code, in the detector model with standard
memory-experiment boundaries, `d_circ(C_R(M)) = d_eff(M)` for every `R ≥ 1`.

**Outcome: the corollary is proved, in full, with all boundary cases discharged.** Per the
commission's epistemic ceiling, everything below is labelled at most **CONJECTURED**; in this
document that label means *complete written proof, no independent review*, and is used in that
sense uniformly. Nothing is asserted on belief alone; every step has an argument, and the
arguments' hypotheses are stated where they are used.

**Two settlements that are corrections rather than gaps** (§0.2): the graph-like hypothesis is
**not** needed and is not used; and the round-1 recon's decomposition claim ("the derived graph
splits into `R` disjoint copies of `G_eff`") is **false as stated** and is replaced here by a
weight-preserving *section*, which is what the proof actually needs and all it can have.

---

## 0. Executive summary

### 0.1 What is proved

Fix a CSS code `Q = [[n,k,d]]`, a single-ancilla CNOT schedule `M` that is non-interleaved
(Def. 2.4), and the standard `R`-round memory experiment `C_R(M)` with ideal initialisation and
ideal transversal final readout (Def. 2.6). Then, per sector and hence overall,

```
    d_circ(C_R(M))  =  d_eff(M)        for every  R ≥ 1.
```

The proof is four steps, each self-contained:

| step | statement | where |
|---|---|---|
| 1 | non-interleaved ⟹ measurement-consistent, so the hypothesis "measurement-consistent" is redundant and the detector model is well posed | §3 |
| 2 | the residual set is exactly `{∅} ∪ {singletons} ∪ {suffixes of the X-check CNOT orders}` — a schedule-order invariant | §4 |
| 3 | **horizontal-representative lemma:** every residual class has a weight-1 representative with `u = s` (X-first) resp. `u = 0` (Z-first), *with one and the same flavour for all checks simultaneously* | §5 |
| 4 | those representatives assemble a weight-preserving chain **section** `ι_r : C^eff → C^{(R)}`, one per round; applying `ι_r` to a minimum-weight effective logical gives a closed lift of the same weight, so `d_circ ≤ d_eff`; the reverse inequality is the augmentation chain map | §6, §7 |

The Laurent frame is load-bearing, not decorative: the entire proof is the interplay of two maps
on `Λ = F₂[x,x⁻¹]`-modules, the augmentation `ε : x ↦ 1` (which gives `d_eff ≤ d_circ`) and the
multiplication-by-`x^r` section (which gives `d_circ ≤ d_eff`), plus the observation that the
standard memory boundaries are **exactly** the boundary conditions under which naive truncation
of the bulk `Λ`-complex to rounds `0..R−1` is exact (Lemma 2.13). That last point is where
sketches die and it is discharged explicitly.

### 0.2 The two settlements

**(S1) The graph-like assumption is not load-bearing and is not used.** It is stated (Def. 2.17),
and then never invoked. Every step above is valid for an arbitrary detector *hypergraph*. This
matters concretely rather than cosmetically:

- The Steane code is **not** graph-like in the Z-memory sector (qubit 6 lies in all three
  Z-checks, so the bare error `X₆` flips three detectors); the theorem nevertheless holds there,
  and is verified exhaustively (§9).
- The **gross code is not graph-like either** — every data qubit lies in exactly 3 Z-checks — so
  the non-interleaved equality that `CIRCDIST.gross` depends on (Strikis et al. Prop. 4 caps
  every non-interleaved gross circuit at `d_circ ≤ 11`) is a statement *outside* the graph-like
  model. A graph-like-only proof would not have covered it. This one does.

**(S2) "`G_circ` = `R` disjoint copies of `G_eff`" is false; the correct statement is a section.**
The recon (`circdist_lift_recon_20260820.md` §3.9) writes "the derived graph splits into `R`
disjoint copies of `G_eff`". In every non-interleaved schedule examined, 27–31% of
all elementary faults are **non**-horizontal — genuine diagonal spacetime edges — e.g. a bare data
`X` deposited in the middle of the Z-block, which is seen by the Z-checks whose CNOTs are still to
come and missed by those already done. Concretely (§9): 444 X-sector faults on one surface-code
schedule, of which only 324 are horizontal. `G_circ` therefore does **not** split. What is true,
and sufficient, is that `G_circ` *contains* `R` pairwise disjoint isomorphic copies of `G_eff`,
namely the images of the sections `ι_0,…,ι_{R−1}` (§6). Containment, not decomposition, is what a
distance upper bound needs; this is the same structural pattern as the weight-preserving-section
criterion of [SRB25, Thm. 4.9] (litverify note).

### 0.3 Definitions that had to be sharpened

Listed here because they are the reusable output; each is justified where it is introduced.

1. **`d_eff` is the distance of the complex on residual *classes*, not on fault types** (Def. 2.11).
   Several fault types share a residual; `d_ext` counts residual columns. The projection `π₁` must
   therefore factor through `ℰ`, or the weight bookkeeping in `d_eff ≤ d_circ` is wrong.
2. **The detector set must contain both temporal boundary detectors**, `D_{b,0}` (initial,
   deterministic because the data is prepared in the sector's basis) and `D_{b,R}` (terminal,
   deterministic because the readout is ideal). With them, `ε∘∂_circ = ∂_eff∘π₁` holds *exactly,
   including for round-0 and round-`(R−1)` faults*; without either one it fails (Rmk. 2.14). This
   is the precise content of "standard memory-experiment boundaries".
3. **Non-interleaved must be a condition on the CNOTs only**, and it has **two inequivalent
   cases** — X-block-first and Z-block-first — which produce *different* horizontal flavours
   (`u = s` vs `u = 0`). The recon's sketch conflates them (Def. 2.4, Lemma 5.2).
4. **Horizontality is a property of residual classes, not of faults** (Def. 5.1). "In a
   non-interleaved schedule every fault is horizontal" is false; "every residual class has a
   horizontal representative" is true, and is what the proof uses.
5. **Fault weight is per *location*, one Pauli per location** (Def. 2.8), so a fault configuration
   is a function from locations to Paulis. Collisions between chosen representatives can only
   *lower* the witness weight, and in fact cannot occur at a minimum-weight `γ` (Lemma 7.2).
6. **Measurement consistency (MC)** belongs in the definition of a legal schedule, but is
   *automatic* here (Prop. 3.3) — and the Z-first case of that proof needs CSS commutation, it is
   not the trivial "all counts are zero" argument the d3gate note gives for the X-first case.
7. **Graph-like** is defined as `|u_i| + |u_i + s_i| ≤ 2` (Def. 2.17) and flagged unused.

### 0.4 Numerical corroboration

Not a substitute for the proof; a check that the *model* in §2 is the model everyone else is
using. Twelve non-interleaved configurations (two codes × {X-first, Z-first} × {block-serial,
packed-parallel} × `R ∈ {2,3}`), independent re-implementation, all seven checks pass, including
**every** elementary fault matching the detector-chain formula at both temporal boundaries
(1332/1332, 1035/1035, …). Details and the failure-side check in §9.

---

## 1. Standing conventions

`F₂` throughout. `Λ := F₂[x, x⁻¹]`, the group ring of the time-translation group `Z`, with
augmentation `ε : Λ → F₂`, `ε(x) = 1`. For a finite set `S`, `F₂^S` is the `F₂`-vector space with
basis `S`; the weight `|v|` of `v ∈ F₂^S` is the number of nonzero coordinates. `Λ^S = Λ ⊗ F₂^S`
is the free `Λ`-module on `S`; its elements are written `Σ_ρ x^ρ v_ρ` with `v_ρ ∈ F₂^S`.

Sums of Pauli supports are `F₂` sums (symmetric differences). All statements are for the
**Z-memory sector**; the X-memory sector is obtained by the exchange
`X ↔ Z`, `𝒳 ↔ 𝒵`, `H_X ↔ H_Z`, control ↔ target, and every statement and proof transports
verbatim. §2.5 explains why treating the sectors separately is not a restriction.

---

## 2. Definitions

### 2.1 Code and circuit

**Definition 2.1 (code).** A CSS code `Q = [[n,k,d]]` on data qubits `[n] = {1,…,n}`, given by a
set `𝒳` of X-type stabilizer generators and a set `𝒵` of Z-type stabilizer generators, with
supports `supp(a) ⊆ [n]` for `a ∈ 𝒳` and `supp(b) ⊆ [n]` for `b ∈ 𝒵`. CSS commutation:
`|supp(a) ∩ supp(b)|` is even for all `a ∈ 𝒳, b ∈ 𝒵`. Fix a logical `Z`-observable `Z_L` with
support `supp(Z_L) ⊆ [n]`; `|supp(Z_L) ∩ supp(a)|` is even for every `a ∈ 𝒳`.

For `E ⊆ [n]` (an X-type data error) write

```
    s(E) ∈ F₂^𝒵,   s(E)_b = |E ∩ supp(b)| mod 2          (its terminal syndrome)
    λ(E) ∈ F₂,     λ(E)   = |E ∩ supp(Z_L)| mod 2        (its logical action)
```

Both are `F₂`-linear in `E`.

**Definition 2.2 (extraction circuit).** One ancilla per generator, prepared once and measured
once per round. Ancilla `a ∈ 𝒳` is prepared in `|+⟩`, is the **control** of one CNOT `a → q` for
each `q ∈ supp(a)`, and is measured in the X basis. Ancilla `b ∈ 𝒵` is prepared in `|0⟩`, is the
**target** of one CNOT `q → b` for each `q ∈ supp(b)`, and is measured in the Z basis. No other
gates.

**Definition 2.3 (schedule).** A schedule `M` assigns to each CNOT a time step in `{0,…,T−1}` such
that no qubit is involved in two CNOTs at the same step (*legality*), and assigns to each ancilla a
preparation step strictly before its first CNOT and a measurement step strictly after its last
CNOT. Write `t(a→q)` and `t(q→b)` for CNOT times. Write `q^a_1,…,q^a_{w_a}` for the data qubits of
`a ∈ 𝒳` in increasing CNOT time — the **within-check order** of `a`.

### 2.2 Non-interleaved

**Definition 2.4 (non-interleaved).** `M` is *non-interleaved* if either

- **(X-first)** `max_{a,q} t(a→q) < min_{b,q} t(q→b)`, or
- **(Z-first)** `max_{b,q} t(q→b) < min_{a,q} t(a→q)`,

i.e. the X-check CNOTs and the Z-check CNOTs occupy disjoint, non-interleaving blocks of time
steps. The condition constrains **CNOTs only**: ancilla preparations and measurements may fall
anywhere allowed by Def. 2.3. In the X-first case set `τ := min_{b,q} t(q→b)`; in the Z-first case
set `τ' := max_{b,q} t(q→b)`. If `𝒳 = ∅` or `𝒵 = ∅` both cases hold vacuously and either branch
of every proof below may be used.

> **Sharpening (0.3.3).** The two cases are genuinely different and produce opposite horizontal
> flavours (Lemma 5.2). Any argument that treats "non-interleaved" as a single case has a hole.
> The recon's §3.9 sketch derives `u = s` for X-ancilla faults and `u = 0` for Z-ancilla faults
> **in the same schedule**, which cannot happen: within one non-interleaved schedule the flavour is
> uniform.

### 2.3 Fault model

**Definition 2.5 (elementary fault locations).** Within one round the locations are

| kind | location | Paulis |
|---|---|---|
| prep | immediately after the preparation of an ancilla `c` | the 3 single-qubit Paulis on `c` |
| gate | immediately after a CNOT `g` | the 15 non-identity 2-qubit Paulis on (control, target) of `g` |
| idle | at a step `t`, on a qubit not involved in any CNOT at step `t` | the 3 single-qubit Paulis |
| meas | on the recorded classical outcome of an ancilla `c` | bit flip |

The location set is the same in every round (translation invariance). Data initialisation and the
final data readout carry **no** faults (ideal boundary, per the 公共定义).

Only three structural features of Def. 2.5 are used, and it is worth naming them so the theorem
can be transported to a variant model:

- **(L1)** the *gate* locations include, after each CNOT, the single-qubit `X` on the control alone
  and the single-qubit `X` on the target alone;
- **(L2)** the *prep* locations include a single-qubit `X` on each ancilla;
- **(L3)** *idle* locations exist (used only for a data qubit outside every X-check support, §5).

**Definition 2.6 (memory experiment).** `C_R(M)`: ideal preparation of the data in `|0⟩^n`, then
`R ≥ 1` identical rounds of `M`, then an ideal transversal `Z`-basis readout of the data. Write
`m_{c,r}` for the recorded outcome of ancilla `c` in round `r ∈ {0,…,R−1}`.

**Definition 2.7 (detectors and observable, Z-sector).**

```
    D_{b,0} = m_{b,0}                                        b ∈ 𝒵
    D_{b,ρ} = m_{b,ρ} + m_{b,ρ−1}                            b ∈ 𝒵, 1 ≤ ρ ≤ R−1
    D_{b,R} = m_{b,R−1} + Σ_{q ∈ supp(b)} (readout of q)     b ∈ 𝒵   (terminal)
```

so the Z-sector detector set is indexed by `𝒵 × {0,1,…,R}` — exactly `(R+1)|𝒵|` detectors. The
observable is `Σ_{q ∈ supp(Z_L)} (readout of q)`. (The X-sector detectors `D_{a,ρ}`, `1 ≤ ρ ≤ R−1`,
also exist in this circuit; §2.5 shows they are irrelevant here. There is no `D_{a,0}`: the
round-0 X-check outcome is random on `|0⟩^n`.)

Determinism of `D_{b,0}` and `D_{b,R}` is Lemma 3.4.

**Definition 2.8 (fault configuration, weight, circuit distance).** A *fault configuration* `F` is
a choice, for each location of `C_R(M)`, of a Pauli (or a bit flip, for `meas` locations), all but
finitely many trivial; `|F|` is the number of nontrivial locations. `F` *triggers* a detector if
that detector's value differs from its fault-free value, and *flips the observable* likewise.

```
    d_circ(C_R(M)) = min{ |F| : F triggers no detector and flips the observable }.
```

> **Sharpening (0.3.5).** Weight is counted per location, so two elementary Paulis at the same
> location compose into one fault of weight 1. This convention only ever makes `d_circ` smaller
> than the "sum of DEM columns" count, so it is the conservative choice for the upper bound and is
> handled explicitly in Lemma 7.2.

### 2.4 Per-fault data

**Definition 2.9.** Let `i` be an elementary X-type fault (a fault whose Pauli has trivial
Z-component, or a `meas` flip of an ancilla in `𝒵`) placed in round `r`. Define

- `E_i ⊆ [n]`: the X-type data error present at the end of round `r` (the **terminal residual**);
- `u_i ∈ F₂^𝒵`: `(u_i)_b = 1` iff the fault flips `m_{b,r}`, the round-`r` outcome of Z-check `b`;
- `s_i := s(E_i)`, `λ_i := λ(E_i)`.

All three depend only on the fault's location and Pauli inside the round, not on `r` (translation
invariance), and are computed by forward `F₂` symplectic propagation
`CNOT(c,t) : x_t ← x_t + x_c`, with ancilla errors cleared at each round's measurement/reset.

### 2.5 Sector decoupling

**Lemma 2.10 (CSS sector decoupling). [CONJECTURED — proof given]**
In `C_R(M)`: (i) an X-type Pauli fault never changes an X-check outcome `m_{a,r}`; (ii) a Z-type
Pauli fault never changes a Z-check outcome `m_{b,r}` and never changes the Z-basis readout.
Consequently `d_circ(C_R(M))` is attained by a configuration all of whose Paulis are X-type
(together, possibly, with `meas` flips of Z-checks).

*Proof.* Under CNOT the X-components and Z-components of a Pauli frame propagate independently
(`x_t ← x_t + x_c` and `z_c ← z_c + z_t`), so the X-component of the frame at any time depends only
on the X-components of the inserted faults, and dually. (i) `m_{a,r}` is the X-basis outcome of
ancilla `a`, i.e. the Z-component of the frame on `a`; an X-type fault leaves all Z-components
zero. (ii) `m_{b,r}` is the Z-basis outcome of `b`, i.e. the X-component on `b`, and the ideal
Z-readout of `q` is the X-component on `q`; a Z-type fault leaves all X-components zero. For the
consequence: the observable is a Z-basis readout parity, so by (ii) it is a function of the X-parts
alone; replacing every fault of `F` by its X-part leaves the observable and every Z-sector detector
unchanged, silences every X-sector detector by (i), and does not increase the weight (some
locations may become trivial). ∎

Lemma 2.10 is why "per sector" is a bookkeeping device and not a restriction: the Z-memory circuit
has no X-type observable, so its `d_circ` *is* the Z-sector quantity; the X-memory circuit dually;
and the frozen `d_circ(C(M))` of the 公共定义 is the minimum of the two, as is `d_eff(M)`. Proving
equality in each sector therefore proves it for the minimum.

### 2.6 The two complexes, the truncation, the projection

**Definition 2.11 (effective complex and `d_eff`).** Let `ℰ := { E_i : i an elementary X-type fault
in one round } \ {∅}`, the set of **residual classes**. Put

```
    C₁^eff = F₂^ℰ ,   C₀^eff = F₂^𝒵 ,   ∂_eff([E]) = s(E) ,   λ_eff([E]) = λ(E),
    d_eff  = min{ |v| : v ∈ C₁^eff, ∂_eff v = 0, λ_eff v = 1 }.
```

This is the frozen `d_eff(M) = d_ext(E(M))` of the 公共定义 with `ℰ` the columns of the extended
check matrix: `∂_eff` is `H^ext` and `λ_eff` is `L^ext` [A2, Defs. 1–3]. `ℰ` contains every
singleton `{q}` (Lemma 4.1), so `H^ext` contains `H_Z` as a submatrix and `d_eff ≤ d`.

> **Sharpening (0.3.1).** The index set is `ℰ`, not the set of fault types. Different fault types
> with the same residual give the same `H^ext` column and must be identified before weights are
> compared, otherwise the projection below is not weight-non-increasing in the right sense.

**Definition 2.12 (bulk spacetime complex over `Λ`).** Let `Φ` be the set of elementary X-type
fault types in one round. Put `C₁^bulk = Λ^Φ`, `C₀^bulk = Λ^𝒵`, and let `∂ : C₁^bulk → C₀^bulk` be
the `Λ`-linear map

```
    ∂ e_i  =  u_i (1 + x)  +  s_i x   =   u_i + x (u_i + s_i),          i ∈ Φ.        (2.1)
```

`x` is the one-round time shift. Also `λ : C₁^bulk → F₂`, `λ(x^r e_i) = λ_i`, extended `F₂`-linearly
(`λ` is *not* `Λ`-linear: the residual is read out once, at the end, regardless of when it was
created).

**Lemma 2.13 (exact truncation = standard memory boundaries). [CONJECTURED — proof given]**
Let

```
    C₁^{(R)} = ⊕_{r=0}^{R−1} x^r F₂^Φ  ⊆ C₁^bulk ,      C₀^{(R)} = ⊕_{ρ=0}^{R} x^ρ F₂^𝒵  ⊆ C₀^bulk,
```

where `x^ρ F₂^𝒵` is identified with the detectors `{D_{b,ρ} : b ∈ 𝒵}` of Def. 2.7 and `x^r F₂^Φ`
with the round-`r` copy of the fault locations. Then

1. `∂ ( C₁^{(R)} ) ⊆ C₀^{(R)}`: the truncation is exact, with no correction terms at either end;
2. for every elementary X-type fault `i` and every round `r ∈ {0,…,R−1}`, the detector values of
   `C_R(M)` are given by `∂(x^r e_i) = x^r u_i + x^{r+1}(u_i + s_i)`, and the observable by `λ_i`;
3. **(linearity)** for an arbitrary X-type fault configuration `F`, regarded as the element
   `Σ_{(i,r) ∈ F} x^r e_i ∈ C₁^{(R)}`, the vector of triggered detectors is `∂F` and the observable
   value is `λ(F)`.

*Proof.* (3) follows from (2) because the whole model is `F₂`-linear in the inserted Pauli frame:
propagation `x_t ← x_t + x_c` is linear, so the frame at any time is the `F₂` sum of the frames the
individual faults would have produced; the ancilla outcomes, the ideal readout and hence every
detector and the observable are `F₂`-linear functions of that frame, and the fault-free values are
`0` (Lemma 3.4), so the *triggered* pattern is the sum of the individual triggered patterns.
(Composition of two elementary Paulis at one location is the same `F₂` sum, so Def. 2.8's
per-location weight convention is consistent with this.)

(2) Insert the single fault `i` in round `r` of an otherwise ideal run. Fault-free, the
data stays in `|0⟩^n` and all `m_{b,ρ} = 0` (Lemma 3.4). With the fault: for `ρ < r`, nothing has
happened, `m_{b,ρ} = 0`. For `ρ = r`, by Def. 2.9, `m_{b,r} = (u_i)_b`. From the end of round `r`
the data carries the static error `E_i`; static because in a fault-free round the CNOTs `a→q` have
data as *target* (an X on the target is unchanged, and the freshly prepared `a` carries no error)
and the CNOTs `q→b` have data as *control* (an X on the control is copied to `b`, not moved). So
for `ρ > r`, every Z-check measures the full syndrome of `E_i`: `m_{b,ρ} = (s_i)_b`. The ideal
readout returns `E_i`, whose `b`-parity is `(s_i)_b`. Now read off Def. 2.7:

```
    D_{b,ρ} = 0                       ρ < r          (also for ρ = 0 < r, since D_{b,0} = m_{b,0})
    D_{b,r} = (u_i)_b                                (valid at r = 0 too: D_{b,0} = m_{b,0})
    D_{b,r+1} = (u_i)_b + (s_i)_b                    (valid at r + 1 = R: D_{b,R} = m_{b,R−1} + s_i)
    D_{b,ρ} = (s_i)_b + (s_i)_b = 0   ρ > r + 1      (and D_{b,R} = 0 when r + 1 < R)
```

which is exactly `x^r u_i + x^{r+1}(u_i + s_i)`. The observable is the readout parity over
`supp(Z_L)` of `E_i`, i.e. `λ_i`. (1) is immediate from (2): `r ∈ {0,…,R−1}` gives detector indices
in `{0,…,R}`. ∎

**Remark 2.14 (why both boundary detectors are needed).** The two `(valid at …)` parentheticals are
the whole content of "standard memory-experiment boundaries", and each is supplied by one boundary
convention:

- `D_{b,0}` exists **because the data is prepared in `|0⟩^n`**, an eigenstate of every Z-check, so
  `m_{b,0}` is deterministic. Delete it and a round-0 fault contributes only `x(u_i + s_i)`, whence
  `ε∂(e_i) = u_i + s_i ≠ s_i`: the chain-map identity (Lemma 2.16) fails and with it the direction
  `d_eff ≤ d_circ`. Note that the sector in which the initial detector is *missing* — the X-sector
  of a Z-memory experiment, where `m_{a,0}` is random — is precisely the sector that has no
  observable, so nothing is lost.
- `D_{b,R}` exists **because the final readout is ideal and transversal**. Delete it and a
  round-`(R−1)` fault contributes only `x^{R−1}u_i`, and again `ε∂ ≠ ∂_eff π₁`; worse, the
  observable becomes undefined.

**Definition 2.15 (the projection).** Define

```
    π₁ : C₁^{(R)} → C₁^eff ,  π₁(x^r e_i) = [E_i]   (and 0 if E_i = ∅) ;
    π₀ = ε|_{C₀^{(R)}} : C₀^{(R)} → C₀^eff ,  ε(Σ_ρ x^ρ v_ρ) = Σ_ρ v_ρ .
```

`π₁` is the composite of the two fibre collapses "forget the round" and "forget which fault
produced the residual"; both are weight-non-increasing, hence so is `π₁`: `|π₁ f| ≤ |f|`.

**Lemma 2.16 (chain map / telescoping). [CONJECTURED — proof given]**
`π₀ ∘ ∂ = ∂_eff ∘ π₁` on `C₁^{(R)}`, and `λ_eff ∘ π₁ = λ` on `C₁^{(R)}`.

*Proof.* On the basis, `π₀ ∂(x^r e_i) = ε(x^r u_i + x^{r+1}(u_i+s_i)) = u_i + u_i + s_i = s_i`,
while `∂_eff π₁(x^r e_i) = ∂_eff[E_i] = s(E_i) = s_i` (and both sides are `0` when `E_i = ∅`, since
then `s_i = 0`). Extend `F₂`-linearly. Likewise `λ_eff π₁(x^r e_i) = λ(E_i) = λ_i = λ(x^r e_i)`. ∎

This is the recon's Conjecture 3.1, now with the truncated complex and both boundary detectors in
place — which is the only version that is actually usable.

### 2.7 Graph-like (stated, not used)

**Definition 2.17 (graph-like).** The detector model is *graph-like* if every elementary fault
triggers at most two detectors, i.e. `|u_i| + |u_i + s_i| ≤ 2` for all `i ∈ Φ`. Then `C₀^{(R)}` is
the vertex space of a graph `G_circ` with vertex set `𝒵 × {0,…,R}` and one edge (or half-edge) per
fault type per round; `C₀^eff` is the vertex space of `G_eff` with vertex set `𝒵`; and the
taxonomy of the recon's Obs. 1.2 applies (horizontal-early `u = s`, horizontal-late `u = 0`,
diagonal, vertical).

> **Settlement (S1).** Definition 2.17 is **not used anywhere below**. Every proof in §§3–7 is
> valid for arbitrary `|u_i|, |s_i|`. Graph-likeness is needed only to *speak* of `G_circ`,
> `G_eff`, edges and voltages; the theorem itself does not require it. §8.3 records why this is
> materially important rather than a technicality.

---

## 3. Measurement consistency is automatic, and the model is well posed

### 3.1 The constraint

**Proposition 3.1 (measurement consistency). [CONJECTURED — proof given]**
For `a ∈ 𝒳`, `b ∈ 𝒵` put `c_{ab} := #{ q ∈ supp(a) ∩ supp(b) : t(q→b) < t(a→q) } mod 2`. Then the
outcomes `m_{a,r}`, `m_{b,r}` of one round of `M` are, expressed at the start of the round,

```
    m_{b,r} = value of   Z_b · ∏_{q ∈ supp(b)} Z_q · ∏_{a ∈ 𝒳} Z_a^{c'_{ab}}   ,  c'_{ab} = |supp(a)∩supp(b)| − c_{ab}
    m_{a,r} = value of   X_a · ∏_{q ∈ supp(a)} X_q · ∏_{b ∈ 𝒵} X_b^{c_{ab}}
```

Since ancilla `a` is freshly prepared in `|+⟩` (so `Z_a` is uniformly random) and `b` in `|0⟩` (so
`X_b` is uniformly random), the circuit measures the intended check operators — equivalently the
detectors of Def. 2.7 are deterministic functions of the data — **iff** `c_{ab} ≡ 0 (mod 2)` for
all `a, b`. Call this condition **(MC)**.

*Proof.* Back-propagate `Z_b` through the round in reverse time order. The only gates whose
Heisenberg action moves `Z_b` are the CNOTs `q → b` (target `b`): `Z_b ↦ Z_q Z_b`. Continuing
backwards past a CNOT `a → q'` (target `q'`): `Z_{q'} ↦ Z_a Z_{q'}`. So a factor `Z_q` acquired at
time `t(q→b)` picks up `Z_a` once for each `a` with `q ∈ supp(a)` and `t(a→q) < t(q→b)`. Collecting
over `q ∈ supp(a) ∩ supp(b)` gives the exponent `c'_{ab} = #{q : t(a→q) < t(q→b)}`, and
`c_{ab} + c'_{ab} = |supp(a) ∩ supp(b)| ≡ 0` by CSS commutation, so `c'_{ab} ≡ c_{ab}`. The `X_a`
computation is dual. A surviving `Z_a` (resp. `X_b`) factor makes the outcome uniformly random and
uncorrelated with the data, since the fresh ancilla state is an eigenstate of `X_a` (resp. `Z_b`)
only. ∎

Proposition 3.1 is the d3gate note's Conjecture 2.1, with its two halves reconciled: the note
derives the constraint from the X-side and asserts the Z-side coincides; the identity
`c_{ab} + c'_{ab} ≡ 0` above is the reason. It is corroborated there against
`stim`'s non-deterministic-detector oracle, 56/56 agreements.

**Definition 3.2 (legal schedule).** From here, *schedule* means a schedule in the sense of
Def. 2.3 that additionally satisfies (MC).

### 3.2 Non-interleaved ⟹ (MC)

**Proposition 3.3. [CONJECTURED — proof given]** Every non-interleaved schedule satisfies (MC).

*Proof.* X-first: for every `q ∈ supp(a) ∩ supp(b)`, `t(a→q) < τ ≤ t(q→b)`, so `c_{ab} = 0`.
Z-first: for every such `q`, `t(q→b) ≤ τ' < t(a→q)`, so `c_{ab} = |supp(a) ∩ supp(b)| ≡ 0 (mod 2)`
by CSS commutation. ∎

The Z-first case is *not* the trivial one: it is even only because the code is CSS. The d3gate
note's remark "non-interleaved schedules satisfy (MC) automatically (all counts are 0)" covers only
the X-first case.

Consequently the hypothesis "measurement-consistent" in the target statement is redundant. It is
retained in the theorem statement because it is not redundant for the interleaved case and because
`CIRCDIST.gross`/`CIRCDIST.cplx` need it in their search spaces.

### 3.3 The fault-free run

**Lemma 3.4 (determinism). [CONJECTURED — proof given]** In a fault-free run of `C_R(M)` with `M`
satisfying (MC) and data prepared in `|0⟩^n`: `m_{b,r} = 0` for every `b ∈ 𝒵` and every `r`, the
terminal readout has trivial syndrome, and the observable takes its nominal value. Hence every
Z-sector detector of Def. 2.7 is deterministic and its fault-free value is `0`.

*Proof.* By (MC) and Prop. 3.1 the circuit implements a projective measurement of each check
operator on the data. `|0⟩^n` is stabilized by `⟨Z_1,…,Z_n⟩`, which contains every Z-check and
`Z_L`. Measuring an X-check `X_a` replaces the stabilizer group by
`⟨ elements commuting with X_a , ± X_a ⟩`; every Z-check and `Z_L` commutes with every `X_a` (CSS
commutation, Def. 2.1), so they survive, with unchanged sign. By induction over the rounds, at
every time the state is stabilized by every Z-check with sign `+1` and by `Z_L` with sign `+1`.
Measuring a Z-check therefore returns `0` deterministically, and the ideal `Z`-readout is
consistent with all Z-checks and with `Z_L`. ∎

The X-sector detectors `D_{a,ρ}`, `ρ ≥ 1`, are deterministic too (the round-`ρ` and round-`(ρ−1)`
X-outcomes agree because the state is an eigenstate of `X_a` after the first measurement), while
`m_{a,0}` is random — which is why there is no `D_{a,0}`. By Lemma 2.10 none of this affects the
Z-sector, and by Remark 2.14 the missing initial detector sits in the sector with no observable.

---

## 4. The residual set

**Lemma 4.1 (classification of `ℰ`). [CONJECTURED — proof given]**
For **any** schedule (interleaved or not),

```
    ℰ ∪ {∅}  =  {∅}  ∪  { {q} : q ∈ [n] }  ∪  { S_a(j) : a ∈ 𝒳, 0 ≤ j ≤ w_a },
    S_a(j) := { q^a_{j+1}, …, q^a_{w_a} }   (the suffix of a's within-check order after its j-th CNOT).
```

In particular `ℰ` depends only on the within-check CNOT orders (recon Consequence 2.1), and
contains every singleton.

*Proof.* Every elementary X-type fault places `X` on a set `P` of at most two qubits at one time
`t`, where `P` is contained in `{c, t}` for a gate location, is a single ancilla for a prep
location, is a single qubit for an idle location, and is empty for a `meas` location. Propagate
forward to the end of the round; only `x_t ← x_t + x_c` acts.

- `X` on a Z-ancilla `b` at time `t`: `b` is only ever a *target*, so the error never leaves `b`,
  and `b` is reset at the end of the round. Contribution to the residual: `∅`.
- `X` on an X-ancilla `a` at time `t`: `a` is only ever a *control*, so the error is copied onto
  each `q` with `t(a→q) > t`, i.e. onto `S_a(j)` where `j = #{q : t(a→q) < t}`; and `a` is reset.
  Contribution: `S_a(j)`. As `t` ranges over the round, `j` ranges over `0,…,w_a`, and every value
  is realised (`j = 0` by the prep location, `j ≥ 1` by the gate location after the `j`-th CNOT).
- `X` on a data qubit `q` at time `t`: `q` is a target of `a→q` CNOTs (an X on the target is
  unchanged) and a control of `q→b` CNOTs (the X is copied to `b`, which is reset). Contribution:
  `{q}`. Realised for every `q` by (L1) or (L3): if `q` lies in some X-check use the target-`X`
  after a CNOT `a→q`; if `q` lies in some Z-check use the control-`X` after a CNOT `q→b`; if `q`
  lies in no check it is idle at every step.
- A 2-qubit Pauli after a CNOT contributes the `F₂` sum of the two single-qubit contributions at
  the same time. After `a → q_j`: `S_a(j) + {q_j} = S_a(j−1)`, again a suffix. After `q → b`:
  `{q} + ∅ = {q}`. So no new residual arises.

Every listed set is realised and nothing else is. ∎

Verified independently: the classification reproduces exactly the 18-element surface-code and
17-element Steane residual sets computed in the d3gate note, and is re-checked here on 12
configurations plus one interleaved one (§9).

---

## 5. The horizontal-representative lemma

This is the heart, and it is the only place where non-interleaving is used.

**Definition 5.1 (horizontality; representatives).** An elementary X-type fault `i` is
*early-horizontal* if `u_i = s_i`, *late-horizontal* if `u_i = 0`, and *horizontal* if either. A
fault `i` is a *representative* of `E ∈ ℰ` if `E_i = E`.

> **Sharpening (0.3.4).** Horizontality is asserted below for a *choice* of representative per
> residual class, never for all faults. §9 measures the failure of the universal version: in the
> non-interleaved schedules tested, 27–30% of elementary faults are non-horizontal.

### 5.1 The general one-round formula

**Lemma 5.2 (visibility formula). [CONJECTURED — proof given]** Let `i` be an elementary X-type
fault that does not act on a Z-ancilla. For `q ∈ E_i` let `θ_i(q)` be the time at which the `X`
first lands on `q` (the fault's own time if `q` is one of its qubits; otherwise `t(a→q)` for the
X-ancilla `a` the fault acts on). Then

```
    (u_i)_b  =  #{ q ∈ supp(b) ∩ E_i : t(q→b) > θ_i(q) }  mod 2 ,       b ∈ 𝒵.        (5.1)
```

*Proof.* `b`'s recorded outcome is the X-component of the frame on `b` at its measurement, which by
`x_b ← x_b + x_q` accumulates the X-component of `q` at each time `t(q→b)`, `q ∈ supp(b)`, plus
whatever the fault put on `b` directly (nothing, by hypothesis), plus its fresh-prep value `0`.
The X-component of `q` is `0` before `θ_i(q)` and `1` from `θ_i(q)` on: it never leaves `q`
(Lemma 4.1's third bullet), and no second arrival is possible because each `a` has exactly one CNOT
to `q` and the fault acts at most once. ∎

Formula (5.1) is a *comparison of two timestamps per (qubit, check) pair*. It contains the whole
mechanism: `u_i = s_i` iff every comparison is "later", `u_i = 0` iff every comparison is
"earlier", and everything in between is a genuinely diagonal spacetime edge.

### 5.2 Non-interleaving makes the residual atomic

**Lemma 5.3 (atomicity). [CONJECTURED — proof given]** Let `M` be non-interleaved and let `i` be an
elementary X-type fault that acts only on data qubits and X-ancillas.

1. **(X-first)** If `i` is located at a time `< τ`, then `u_i = s_i`.
2. **(Z-first)** If `i` acts only on X-ancillas, or is located at a time `> τ'`, then `u_i = 0`.

*Proof.* (1) Every `q ∈ E_i` receives its `X` either at the fault's own time (`< τ`) or at a time
`t(a→q) < τ` (all X-check CNOTs precede `τ`). So `θ_i(q) < τ ≤ t(q→b)` for every `b ∋ q`, and every
comparison in (5.1) is "later": `(u_i)_b = |supp(b) ∩ E_i| = s(E_i)_b`. (2) If `i` acts only on
X-ancillas, every `q ∈ E_i` receives its `X` at a time `t(a→q) > τ'`; if `i` is located at a time
`> τ'`, likewise every `θ_i(q) > τ'`. Either way `θ_i(q) > τ' ≥ t(q→b)` for every `b ∋ q`, every
comparison is "earlier", and `(u_i)_b = 0`. ∎

**This is why non-interleaving kills cross-round hook transport.** A hook is a residual deposited
on several data qubits at several times. Each Z-check `b` performs one timestamp comparison per
shared qubit (5.1); *the parity of the answers* decides whether `b` sees the hook this round, next
round, or — the dangerous case — half of it now and half of it later. Non-interleaving collapses
all of those comparisons to a single global comparison "X-block before Z-block?" whose answer is
the same for every `(q,b)` pair at once. The residual is therefore measured **atomically**: either
entirely in the round in which it was created (X-first) or entirely in the next one (Z-first).
There is no way to split it across the round boundary, so no spacetime edge with a nonzero
"voltage" can be produced from a hook. Interleaving restores the freedom to make the comparisons
disagree — and that is exactly and only what the counterexamples exploit (§8.1).

Two hypotheses in Lemma 5.3 are real and are used:

- *"acts only on data and X-ancillas"* — a fault putting `X` directly on a Z-ancilla `b` (a `prep`
  or `idle` fault on `b`, or a `meas` flip) contributes `(u)_b = 1` with residual `∅`, so
  `u = {b} ≠ 0 = s`: it is a **vertical** fault, non-horizontal, and it exists in every schedule
  including non-interleaved ones. It is harmless because its residual class is `∅ ∉ ℰ`, so it is
  never needed as a representative; and it is exactly the repair resource that the interleaved case
  has to pay for.
- *"located at a time `< τ`" / "`> τ'`"* — faults inside the opposite block are typically diagonal;
  this is the 27–30% measured in §9.

### 5.3 Existence of horizontal representatives

**Lemma 5.4 (horizontal-representative lemma). [CONJECTURED — proof given]**
Let `M` be non-interleaved. Then there is an injective map `σ : ℰ → Φ` with `E_{σ(E)} = E` for all
`E`, such that

- **(X-first)** `u_{σ(E)} = s(E)` for every `E ∈ ℰ`; or
- **(Z-first)** `u_{σ(E)} = 0` for every `E ∈ ℰ`,

with the *same* flavour for every `E` simultaneously.

*Proof.* Injectivity is automatic: a fault has one residual, so representatives of distinct classes
are distinct faults. By Lemma 4.1 it suffices to exhibit, for each class, a representative
satisfying the hypotheses of Lemma 5.3.

**X-first.** If `𝒳 = ∅` there are no suffixes and the schedule is also Z-first (Def. 2.4); use the
other branch. So assume `𝒳 ≠ ∅`, whence `τ ≥ 1` and the X-block is the nonempty set of steps
`{0,…,τ−1}` containing every X-check CNOT.

- `E = S_a(j)`, `1 ≤ j ≤ w_a − 1`: take the single-qubit `X` on the **control** immediately after
  the CNOT `a → q^a_j` (location (L1)). Its residual is `S_a(j)` (Lemma 4.1) and its time is
  `t(a→q^a_j) < τ`; it acts only on `a`. Lemma 5.3(1) gives `u = s`.
- `E = S_a(0) = supp(a)`: take the `X` on `a` immediately after its preparation (L2). The
  preparation is strictly before `a`'s first CNOT (Def. 2.3), hence at a time `< τ`. Same
  conclusion. (`S_a(0)` is a stabilizer, so `s = 0` and `λ = 0`; it never occurs in a
  minimum-weight `γ`, but a representative costs nothing to supply.)
- `E = {q}` with `q ∈ supp(a)` for some `a ∈ 𝒳`: take the single-qubit `X` on the **target**
  immediately after the CNOT `a → q` (L1), at a time `< τ`, acting only on `q`. Same conclusion.
- `E = {q}` with `q` in no X-check: then every CNOT touching `q` is a Z-check CNOT, hence at a time
  `≥ τ ≥ 1`, so `q` is idle at step `0`; take the idle `X` on `q` at step `0` (L3). Time `0 < τ`,
  acts only on `q`. Same conclusion.

**Z-first.** Symmetrically, with `τ'` the last Z-check CNOT time.

- `E = S_a(j)`, `j ≥ 1`: the control-`X` after `a → q^a_j`; it acts only on the X-ancilla `a`, so
  Lemma 5.3(2) applies regardless of where the fault sits. `u = 0`.
- `E = S_a(0)`: the `X` after `a`'s preparation — again acting only on `a`, so Lemma 5.3(2)
  applies even if the preparation is scheduled before `τ'`. `u = 0`. *(This case is the reason
  Lemma 5.3(2) is stated with the alternative "acts only on X-ancillas": the X-ancilla's
  preparation need not lie inside the X-block.)*
- `E = {q}` with `q ∈ supp(b)` for some `b ∈ 𝒵`: take the control-`X` immediately after the **last**
  CNOT `q → b_last`, at time `τ_q := t(q→b_last) `. Then every comparison in (5.1) reads
  `t(q→b) ≤ τ_q = θ(q)`, so `u = 0` directly by (5.1). *(This is slightly finer than
  Lemma 5.3(2): the fault need not be after `τ'`, only after `q`'s own last Z-CNOT.)*
- `E = {q}` with `q` in no Z-check: then `s(E) = 0`, and (5.1) gives `u = 0` for any representative;
  one exists by the last bullet of Lemma 4.1's proof. ∎

---

## 6. The decomposition: `R` disjoint copies — a section, not a splitting

**Definition 6.1 (the round-`r` section).** Fix `σ` from Lemma 5.4 and `r ∈ {0,…,R−1}`. Define the
`F₂`-linear map

```
    ι_r : C₁^eff → C₁^{(R)} ,      ι_r([E]) = x^r e_{σ(E)} .
```

**Proposition 6.2 (weight-preserving chain section). [CONJECTURED — proof given]**
For every `r ∈ {0,…,R−1}`:

1. `π₁ ∘ ι_r = id_{C₁^eff}`  (`ι_r` is a section of the projection);
2. `ι_r` is **weight-preserving**: `|ι_r(v)| = |v|` for all `v`;
3. `∂ ∘ ι_r = x^r · (∂_eff)` in the X-first case, and `∂ ∘ ι_r = x^{r+1} · (∂_eff)` in the Z-first
   case — in both cases the boundary of a lifted effective cycle lands in a **single** detector
   time-slice;
4. `λ ∘ ι_r = λ_eff`.

*Proof.* (1) `π₁(x^r e_{σ(E)}) = [E_{σ(E)}] = [E]`. (2) `σ` is injective, so `ι_r` maps the basis
`ℰ` injectively into the basis `{x^r e_i}` of the round-`r` summand. (3) By (2.1),
`∂(x^r e_{σ(E)}) = x^r u_{σ(E)} + x^{r+1}(u_{σ(E)} + s(E))`. X-first: `u_{σ(E)} = s(E)`, so the
second term vanishes and the first is `x^r s(E) = x^r ∂_eff[E]`. Z-first: `u_{σ(E)} = 0`, so the
first term vanishes and the second is `x^{r+1} s(E) = x^{r+1} ∂_eff[E]`. Extend linearly. (4)
`λ(x^r e_{σ(E)}) = λ_{σ(E)} = λ(E) = λ_eff([E])`. ∎

**Corollary 6.3 (the decomposition statement, correctly stated). [CONJECTURED]**
The spacetime complex `C^{(R)}` of a non-interleaved schedule **contains `R` pairwise disjoint
isomorphic copies of the effective complex**, namely `ι_0, …, ι_{R−1}`:

- in degree 1 the images have disjoint supports (distinct rounds);
- in degree 0 the images of `∂∘ι_r` have disjoint supports: slice `r` (X-first) or slice `r+1`
  (Z-first), for `r = 0,…,R−1`;
- consequently exactly one detector slice carries no copy: slice `R` (the **terminal** boundary) in
  the X-first case, slice `0` (the **initial** boundary) in the Z-first case. This is the precise
  sense in which "the copies are glued only through the boundary conventions": they are not glued
  at all, and the spare slice is exactly the one supplied by the ideal boundary of Def. 2.6.

In graph-like language (Def. 2.17, not needed): `G_circ ⊇ ⊔_{r=0}^{R−1} G_eff^{(r)}` with
`G_eff^{(r)} ≅ G_eff` a vertex-disjoint subgraph living in one time slice.

> **Settlement (S2): the containment is strict, and cannot be improved to an isomorphism.**
> `C^{(R)}` also contains
> (i) **vertical** faults — `X` on a Z-ancilla, or a `meas` flip — with `E = ∅`, `s = 0`, `u ≠ 0`,
>     present in every schedule whatsoever;
> (ii) **diagonal** faults — e.g. a bare data `X` deposited in the interior of the Z-block, for
>     which (5.1) gives a proper sub-parity of `s`;
> (iii) both horizontal flavours for some classes (bare data errors admit `u = s` *and* `u = 0`
>     representatives), so the "horizontal subgraph" is not a disjoint union either: detector slice
>     `ρ` receives the early edges of round `ρ` and the late edges of round `ρ−1` superimposed.
> Measured (§9): 120 of 444 X-sector faults on one non-interleaved surface-code schedule are
> non-horizontal. Hence the recon's "the derived graph splits into `R` disjoint copies of `G_eff`"
> is false. A distance **upper** bound needs only a weight-preserving section, which is what
> Prop. 6.2 supplies; the extra edges can only lower `d_circ`, and Theorem 7.1's lower bound proves
> they do not.

**Remark 6.4 (mixed-flavour closure, for robustness).** Suppose only the weaker hypothesis holds:
every `E ∈ ℰ` has a horizontal representative, but the flavour may vary with `E` (this is the
situation in the d3gate note's Conj. 4.1 for the surface code under *arbitrary* schedules). Split
`γ = A ⊔ B` by flavour (`u = 0` on `A`, `u = s` on `B`), place `A` in round `r` and `B` in round
`r+1` (`R ≥ 2`). Then

```
    ∂ ( Σ_{A} x^r e_i + Σ_{B} x^{r+1} e_i )
      =  Σ_A ( 0 + x^{r+1} s_i )  +  Σ_B ( x^{r+1} s_i + x^{r+2}·0 )
      =  x^{r+1} Σ_{γ} s_i  =  0 .
```

The order matters: `u = 0` first, `u = s` second — the late edges of round `r` and the early edges
of round `r+1` meet in detector slice `r+1`. The reverse assignment does not close. Under
non-interleaving the flavour is uniform (Lemma 5.4) and this two-round window is unnecessary, which
is why the theorem holds already at `R = 1`.

---

## 7. The theorem

**Theorem 7.1 (non-interleaved corollary). [CONJECTURED — proof given]**
Let `Q` be a CSS code, `M` a legal (Def. 3.2), non-interleaved (Def. 2.4) single-ancilla CNOT
syndrome-extraction schedule, and `C_R(M)` the standard memory experiment (Def. 2.6) with `R ≥ 1`.
Then, in each sector and hence for the circuit,

```
    d_circ(C_R(M))  =  d_eff(M) .
```

*Proof.*

**(≥) `d_eff ≤ d_circ`.** This direction is the general inequality of the frozen 公共定义,
`d_eff(M) ≤ d_circ(C(M)) ≤ d`, established in the pinned literature as [A2, Prop. 3]
(arXiv:2603.05481, `d_circ ≥ d_ext(ℰ)`, for any single-ancilla CNOT-based SEC — hypotheses:
single-ancilla, CNOT-based, CSS, same elementary-fault weights, ideal final readout, all of which
hold here). It needs no non-interleaving hypothesis. For self-containment, and because the frozen
statement must be matched to the fault model of §2, here is the proof in the present framework.

Let `F` be a fault configuration of `C_R(M)` with `|F| = d_circ` that triggers no detector and
flips the observable. By Lemma 2.10 we may take `F` to be X-type without increasing `|F|`. Regard
`F ∈ C₁^{(R)}`; by Lemma 2.13(3) the detector values of `F` are `∂F` and the observable value is
`λ(F)`, so `∂F = 0` and `λ(F) = 1`. Apply Lemma 2.16:

```
    ∂_eff (π₁ F)  =  π₀ (∂ F)  =  0 ,        λ_eff (π₁ F)  =  λ(F)  =  1 .
```

The second equation forces `π₁F ≠ 0`, so `π₁F` is a nontrivial effective logical, and `π₁` is
weight-non-increasing (Def. 2.15), whence `d_eff ≤ |π₁ F| ≤ |F| = d_circ`. ∎(≥)

**(≤) `d_circ ≤ d_eff`.** Let `γ ∈ C₁^eff` with `∂_eff γ = 0`, `λ_eff γ = 1`, `|γ| = d_eff`; write
`γ = {E_1,…,E_w}`, `w = d_eff`. Pick any round `r ∈ {0,…,R−1}` and set `F := ι_r(γ)`, i.e. the
configuration that inserts, in round `r`, the single elementary fault `σ(E_j)` for each `j`. By
Prop. 6.2,

```
    ∂F = ∂ι_r(γ) = x^{r} ∂_eff γ = 0    (X-first)          ∂F = x^{r+1} ∂_eff γ = 0    (Z-first)
    λ(F) = λ_eff(γ) = 1
    |F| ≤ |ι_r(γ)| = |γ| = d_eff        (Lemma 7.2 for the inequality)
```

By Lemma 2.13(3), `∂F = 0` says precisely that `F` triggers no Z-sector detector of `C_R(M)`; by
Lemma 2.10 it triggers no X-sector detector either (it is X-type); and `λ(F) = 1` says it flips the
observable. Hence `d_circ ≤ |F| ≤ d_eff`. ∎(≤)

Combining, `d_circ = d_eff`. ∎

**Lemma 7.2 (weight of the witness). [CONJECTURED — proof given]** With `γ` a minimum-weight
effective logical and `F = ι_r(γ)` as above, the chosen representatives `σ(E_1),…,σ(E_w)` occupy
`w` **distinct locations**, so `|F| = w` exactly; and in any case `|F| ≤ w`.

*Proof.* `|F| ≤ w` is immediate: `F` is supported on at most `w` locations (Def. 2.8 counts
locations, and two elementary Paulis at one location compose to one fault). Suppose two
representatives shared a location. Inspecting Lemma 5.4's choices, the only location carrying two
of them is a CNOT `a → q^a_j`, whose control-`X` represents `S_a(j)` and whose target-`X`
represents `{q^a_j}` (this pair can occur only in the X-first branch, where both are used). If both
`S_a(j)` and `{q^a_j}` lie in `γ`, then since `q^a_j ∉ S_a(j)` we have
`S_a(j) + {q^a_j} = S_a(j−1) ∈ ℰ` by Lemma 4.1, and

```
    γ' := γ + [S_a(j)] + [{q^a_j}] + [S_a(j−1)]
```

satisfies `∂_eff γ' = 0`, `λ_eff γ' = 1` and `|γ'| ≤ |γ| − 1`, contradicting minimality of `γ`.
(Should such a collision occur anyway — e.g. for a non-minimal `γ` — the composed 2-qubit fault
`XX` at that gate has residual `S_a(j−1)`, satisfies `u = s` by Lemma 5.3(1), and the witness
simply gets *cheaper*.) ∎

**Corollary 7.3 (`R`-independence; input to `CIRCDIST.sat`). [CONJECTURED]**
For a non-interleaved `M`, the function `R ↦ d_R(M) := d_circ(C_R(M))` is **constant**, equal to
`d_eff(M)`, for all `R ≥ 1`. Hence in the notation of `CIRCDIST.sat`,

```
    R_sat(M) = 1        if d_eff(M) = d ,
    R_sat(M) = ∞        if d_eff(M) < d .
```

*Proof.* Theorem 7.1 holds for every `R ≥ 1`; the construction in (≤) uses one round, and the
bound in (≥) is `R`-uniform. The saturation statement is then immediate from the definition of
`R_sat` together with `d_eff ≤ d`. ∎

So the entire non-interleaved class is settled for `CIRCDIST.sat` with no transfer-matrix or
pumping argument: there is nothing to saturate, because there is no `R`-dependence to begin with.
Whatever mechanism makes `R_sat` interesting must be an interleaving mechanism.

---

## 8. Honesty: hypotheses, failure modes, scope

### 8.1 Exactly which step fails under interleaving

**Lemma 5.4 is the only step that uses non-interleaving, and it is the step that fails.** This is
verified on the d3gate note's `d = 3` witness (Steane, depth 8, interleaved, measurement-consistent,
`d_eff = 2`, `d_circ = 3`): re-running the analysis of §9 on that schedule gives

```
    residual classification (Lemma 4.1)              : still exact (17 classes)   [as it must be]
    residuals with NO horizontal representative      :
        E = {0,6}   s = (1,1,0)   only achievable u = (1,1,1)
        E = {2,6}   s = (1,0,0)   only achievable u = (0,1,0)
        E = {4,5}   s = (0,1,1)   only achievable u = (1,1,1)
    the three weight-2 effective logicals            : {2}+{4,5} , {0,6}+{5} , {2,6}+{3}
        — each contains exactly one of the three obstructed hooks
```

So `σ` cannot be constructed, `ι_r` does not exist, and the upper bound evaporates — while the
lower bound (which never used non-interleaving) still holds, leaving `d_circ ≥ d_eff` with the gap
open. That the gap is then *exactly* 1 is the repair-cost statement, which is **not** proved here
and belongs to route R6.

The mechanism is visible in the numbers: `E = {2,6}` has `s = (1,0,0)` but `u = (0,1,0)` — check
`Z1` sees the hook although its total overlap parity is even (it saw `q6` but not `q2`, or
conversely), and check `Z2` misses it although its overlap parity is odd. That is precisely two
timestamp comparisons in (5.1) disagreeing, which Lemma 5.3 forbids under non-interleaving. It is
also consistent with the d3gate note's Conj. 3.1 (`|supp(a) ∩ supp(b)| ≥ 4` is necessary for hook
voltage): Steane's `X_i` and `Z_i` share their full weight-4 support.

### 8.2 What the theorem does *not* say

1. **It does not say every fault is horizontal.** It says every residual *class* has a horizontal
   representative. Vertical and diagonal spacetime edges exist in non-interleaved circuits and are
   ordinary features of them (Settlement S2).
2. **It does not compute `d_eff`.** `d_eff` is an invariant of the within-check CNOT orders alone
   (Lemma 4.1); the theorem says the interleaving pattern contributes nothing further when it is
   trivial. Hook-damaged within-check orders remain hook-damaged.
3. **It gives no lower bound on `g(C)` for interleaved schedules** and asserts nothing about them,
   beyond identifying the failing step (§8.1).
4. **It is a statement about `d_ext`-style effective distance**, i.e. about residuals of *single*
   faults. Nothing here addresses multi-fault residual interactions in a different model.
5. **`k = 0` degeneracy** is excluded implicitly: if no logical observable exists both sides are
   `+∞` by the usual convention and the statement is vacuous.

### 8.3 Where the graph-like assumption is (not) load-bearing

Definition 2.17 is never invoked. The places one might expect it, and why it is not needed:

- *Formula (2.1) and the "edge taxonomy".* The taxonomy is a convenience for `|s| ≤ 2`; the proofs
  use only the vectors `u_i, s_i` and never their weights.
- *"`γ` is a cycle in `G_eff`".* Replaced throughout by `γ ∈ ker ∂_eff` — a homological, not
  graph-theoretic, condition.
- *The `F₂`-vs-`Z` orientation problem* (recon Obs. 3.5), which is the technical crux of the
  voltage route R2, **does not arise at all**: everything here is `F₂`-valued, with the time
  grading carried by `x`. That was the recon's stated reason for preferring R1 over R2, and it is
  borne out.

Why this matters rather than being a technicality:

- **Steane is not graph-like** in the Z-sector (data qubit 6 lies in all three Z-checks, so `|s(X₆)|
  = 3` and the corresponding fault triggers three detectors). Theorem 7.1 covers it, and §9
  verifies `d_circ = d_eff = 2` there exhaustively.
- **The gross code is not graph-like**: with `H_X = [A|B]`, `H_Z = [Bᵀ|Aᵀ]` and `A, B` of weight 3,
  every data qubit lies in exactly 3 Z-checks. The non-interleaved equality that Strikis et al.
  Prop. 4 uses to cap every non-interleaved gross circuit at `d_circ ≤ 11` therefore lives outside
  the graph-like model. A graph-like-only proof of the corollary would not license that use;
  Theorem 7.1 does.

**Honest counterweight.** Graph-likeness *is* load-bearing for the node's main target — the general
`iff` — because the voltage/`T`-join formulations of the repair cost, and the "vertical edge"
picture of the obstruction, are graph statements. Removing it here does not remove it there.

### 8.4 Assumptions carried from outside this document

| # | assumption | status |
|---|---|---|
| A2 | [A2] arXiv:2603.05481 Prop. 3 (`d_circ ≥ d_ext(ℰ)`) and Defs. 1–3 (`ℰ`, `H^ext`, `d_ext`) — used for the frozen `≥` direction and for the meaning of `d_eff` | VERIFIED in the recon (full text fetched; direction re-checked twice). Also **re-proved here** (Theorem 7.1 (≥)), so the document does not depend on it |
| — | Theorem 7.1's statement coincides with [A2] Cor. 1 (non-interleaved `d'_circ = d_ext(ℰ)`) | The *statement* is theirs; the *proof* here is independent and is what the node's technical requirement 6 asks for. Their hypotheses (single-ancilla, CNOT-based, CSS, within-check orders preserved) are matched |
| MC | the (MC) predicate agrees with `stim`'s non-deterministic-detector oracle | NUMERICAL, 56/56, from the d3gate note. Not relied on: Prop. 3.1 proves the predicate from the stabilizer formalism, and Prop. 3.3 shows non-interleaved schedules satisfy it unconditionally |
| — | stabilizer formalism: measuring `P` on a stabilizer state is deterministic iff `±P` is in the stabilizer group | standard; used in Prop. 3.1 and Lemma 3.4 |

No claim below `PROVED` in this document depends on the voltage-graph literature (A1/[GT87]),
harmonic morphisms (A4/[BN09]), or the spacetime-code literature (A6). [SRB25, Thm. 4.9]
(weight-preserving sections) is cited in §0.2 as a structural analogue only.

---

## 9. Numerical corroboration of the model (not of the proof)

The proof stands on §§2–7. This section checks that the *model* of §2 is the model the rest of the
project (and `stim`) is using, and measures the two quantitative claims made in the settlements.
Independent re-implementation of the `F₂` propagator; the d3gate note's `stim` cross-check applies
to the same detector conventions.

**Configurations.** Two codes (rotated `[[9,1,3]]` surface; Steane `[[7,1,3]]`, with the d3gate
note's within-check orders) × {X-first, Z-first} × {block-serial (depth 24), packed-parallel
(depth 10/11)} × `R ∈ {2,3}` = **12 non-interleaved configurations**, plus the interleaved Steane
witness of §8.1.

| check | what it tests | result |
|---|---|---|
| C1 | Lemma 4.1 classification of `ℰ` | exact in 12/12 (18 classes surface, 17 Steane), and also on the interleaved schedule |
| C2 | Lemma 2.13(2): `∂(x^r e_i) = x^r u_i + x^{r+1}(u_i+s_i)` for **every** fault at **every** round, including `r = 0` (initial detector) and `r = R−1` (terminal detector) | **10 233 / 10 233 faults, zero mismatches** across the 12 configurations (e.g. 1332/1332, 1035/1035, 618/618) — the boundary bookkeeping is exactly as claimed. Residual and logical action checked at the same time |
| C3 | Lemma 5.4: every residual class has a representative of the predicted flavour | 12/12, flavour `u = s` on X-first, `u = 0` on Z-first, as predicted |
| C4 | Settlement S2: horizontality is **not** universal | non-horizontal faults present in 12/12; **2 820 of 3 937 one-round faults are horizontal, i.e. 28.4% are not** (e.g. 324/444, surface block-Z-first; 239/345, Steane) |
| C5 | Theorem 7.1 (≤): the single-round witness `ι_0(γ)` | 12/12: weight = `d_eff` = 2, distinct locations, **0 detectors fired**, observable flipped |
| C6 | `d_circ` by exhaustive weight-≤3 enumeration over the **full** two-sector fault set | `d_circ = d_eff = 2` in 12/12 |
| C7 | Prop. 3.3: (MC) automatic | 0 violations in 12/12 |
| — | graph-likeness | surface: Z-degrees `{1,2}` → graph-like. **Steane: Z-degrees `{1,2,3}` → not graph-like**, and the theorem holds there |

The failure-side check of §8.1 (interleaved Steane) is from the same harness.

*Scripts live in this session's scratchpad, not in the repository, and are deliberately not
load-bearing: C1–C7 corroborate the model, they do not prove anything. A reviewer should check
§§2–7 directly.*

---

## 10. What this changes for the node

- **Route R4 (`noninterleaved-horizontal-representative`) is discharged**, with all five of its
  premises `P4.1`–`P4.4` either proved (`P4.1` = Lemma 4.1 + Lemma 5.2; `P4.2` = Lemma 5.3;
  `P4.3` = Lemma 5.4) or replaced by something correct (`P4.4`, "same-round lift closes when
  `Σ u_i = 0`", is superseded by Prop. 6.2, which is sharper: uniform flavour makes the condition
  automatic, and Rmk. 6.4 handles mixed flavours in a two-round window — the `Σ u_i = 0` form is
  neither necessary nor the right invariant).
- **The recon's R4 implication sketch is corrected**: `⟹ G_circ ⊇ R disjoint copies of G_eff` must
  be a containment of *sections*, not a decomposition (Settlement S2), and the two non-interleaved
  cases must be separated (Sharpening 0.3.3).
- **The node's technical requirements 1, 3, 5 (partially) and 6 are met** by this document:
  requirement 1 (rigorous projection) = Def. 2.15 + Lemma 2.16; requirement 3 (spacetime logicals
  project to effective logicals) = Theorem 7.1 (≥); requirement 5 (boundaries) = Lemma 2.13 +
  Rmk. 2.14, *for the temporal boundary only* — the logical/code boundary of `G_eff` (route R3's
  "voltage sinks") is untouched here and remains open; requirement 6 (non-interleaved ⟹ equality
  from the framework) = Theorem 7.1.
- **New input to `CIRCDIST.sat`**: Corollary 7.3 settles the whole non-interleaved class —
  `d_R(M)` is constant in `R`, so `R_sat ∈ {1, ∞}` with the dichotomy decided by `d_eff = d`. No
  transfer matrix needed.
- **New input to `CIRCDIST.gross`**: the corollary is now available *without* graph-likeness
  (§8.3), which the gross code violates. Any use of "non-interleaved ⟹ `d_circ = d_eff`" for the
  gross code is licensed by Theorem 7.1 as stated.
- **Suggested repricing (advisory only; no file under `research/circdist/proof-dag/` was touched).**
  R4: `P = 0.70 → 0.95`, `D = 1 → 0` (proof written; the remaining 0.05 is independent review).
  Node `CIRCDIST.lift`: the acceptance clause "非交错等号" is discharged; the node claim (the `iff`)
  is unaffected — the corollary was always the easy half, and this document confirms it is easy for
  a specific structural reason (uniform-flavour horizontality) that provably fails in the
  interleaved case.
