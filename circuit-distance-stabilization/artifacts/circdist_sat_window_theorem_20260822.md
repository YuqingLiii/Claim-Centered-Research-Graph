# CIRCDIST.sat.window — the stability-window theorem

**Date:** 2026-08-22 · **Node:** `CIRCDIST.sat.window` · **Session:** Opus 5 executor, proposer
role, budget box = 1 session, stop-loss binding. No sub-agents.

**Governing problem statement:** `research/circdist/notes/SAT_RESCOPE_20260822.md` (the 2026-08-22
re-scope of 课题四). The targets are `d_∞(M) = lim_R d_R(M)` and `R_stab(M)`; the historical
`R_sat` of `research/circdist/notes/CIRCDIST_PROBLEMS.md` 课题四 is frozen history and is treated
here only in Corollary 5.5. **Frozen base definitions:** `CIRCDIST_PROBLEMS.md` 公共定义, plus the
measurement-consistency legality constraint recorded across the round-2+ artifacts.

**Epistemic ceiling for this document: nothing is labelled PROVED or CERTIFIED\*.** Every
mathematical statement is labelled **CONJECTURED** and carries a *derivation status* line. Every
computation is labelled **NUMERICAL** with the code inline (§7) and an explicit search scope. This
document has had no independent review; completion levels require one and this session cannot
grant it.

**This document is self-contained.** §1–§2 restate the model and every preliminary from the frozen
definitions; §3–§5 prove the three parts. It does **not** import any step from
`artifacts/circdist_lift_iff_proof_20260820.md`. §6.4 records the relationship to that document's
§5.9/§5.10 honestly, including why its review CONFIRM cannot be transferred here.

---

## 0. Statement of the theorem

Fix a CSS code `Q = [[n,k,d]]` with `k ≥ 1` and a schedule `M` that is **legal** and
**measurement-consistent** in the single-round, single-ancilla class of 公共定义 (Definitions
1.3–1.5 below). Let `C_R(M)` be the `R`-round memory experiment with ideal initialisation and ideal
final transversal data readout (Definition 1.7), and `d_R(M) := d_circ(C_R(M))` (Definition 1.12).

> **THEOREM (stability window). CONJECTURED.**
>
> **(i) Monotonicity.** `d_{R+1}(M) ≤ d_R(M)` for every `R ≥ 1`, in each CSS sector separately and
> hence for `d_R(M) = min(d_R^Z(M), d_R^X(M))`.
>
> **(ii) Contiguity.** For every `R ≥ 1` and each sector, every **minimum-weight** undetectable
> logical fault set `F` of `C_R(M)` has contiguous round support, and its round-span `w` satisfies
> `w ≤ |F| = d_R(M) ≤ d`.
>
> **(iii) Window.** Consequently `d_∞(M) := lim_{R→∞} d_R(M)` exists, equals `min_R d_R(M)`, and
> ```
>        d_∞(M) = d_d(M) ,          R_stab(M) ≤ d_∞(M) ≤ d ,
> ```
> where `R_stab(M) := min{R_0 : d_R(M) = d_∞(M) for all R ≥ R_0}`. Both quantities are decided by
> the finite window `R ∈ {1,…,d}`, and in fact by the adaptive procedure of Corollary 5.4, which
> halts at the first `R` with `R ≥ d_R(M)`.

Derivation status by part: **(i) complete** (§3), **(ii) complete** (§4), **(iii) complete** (§5),
each *relative to* the preliminaries of §2, whose derivation statuses are given individually and
whose scope clauses are audited in §6. The residual gaps are stated as precise sub-claims in §8.

---

## 1. The model, stated completely

Nothing in §1 is new; it is the frozen model written out so that every quantifier in §3–§5 has an
explicit range. §6.1 tabulates which clause is load-bearing for which step.

### 1.1 Code

**Definition 1.1.** A CSS code `Q = [[n,k,d]]` is given by a finite set `𝒜` of **X-checks** and a
finite set `ℬ` of **Z-checks**, with supports `supp(a), supp(b) ⊆ [n] = {0,…,n−1}`, subject to

```
      | supp(a) ∩ supp(b) |  ≡  0   (mod 2)        for all a ∈ 𝒜, b ∈ ℬ.            (CSS)
```

Write `H_X ∈ F₂^{𝒜×n}` and `H_Z ∈ F₂^{ℬ×n}` for the corresponding check matrices, `S_X :=
rowspace(H_X)`, `S_Z := rowspace(H_Z)`. Fix logical representatives `X_L^{(1)},…,X_L^{(k)}` and
`Z_L^{(1)},…,Z_L^{(k)}`. Set

```
      d_X := min{ |v| : v ∈ ker H_Z ∖ S_X } ,      d_Z := min{ |v| : v ∈ ker H_X ∖ S_Z } .
```

**Standing fact 1.2 (CSS distance).** `d = min(d_X, d_Z)`, and for `v ∈ ker H_Z` one has
`v ∉ S_X` **iff** `|v ∩ supp(Z_L^{(j)})|` is odd for some `j`.

*Derivation.* A nontrivial logical `P = X(α)Z(β)` commutes with every stabiliser iff `α ∈ ker H_Z`
and `β ∈ ker H_X`, and is nontrivial iff not both `α ∈ S_X` and `β ∈ S_Z`; so at least one of
`α, β` is a nontrivial logical vector, whence `|supp(α) ∪ supp(β)| ≥ min(d_X,d_Z)`, and pure
`X`/`Z` logicals attain it. The second sentence is the standard symplectic-duality statement that
`S_X = (ker H_Z ∩ {Z_L^{(j)}}^⊥)` inside `ker H_Z`. ∎ *Status: complete; standard.*

**Scope clause S0.** `k ≥ 1`, so `d_X, d_Z < ∞`. `𝒜, ℬ` are the *given generating sets*; the
schedule extracts exactly these generators, and the theorem is a statement about that generating
set, not about the stabiliser group.

### 1.2 Schedule, legality, measurement consistency

**Definition 1.3 (circuit of one round).** Each check `g ∈ 𝒜 ∪ ℬ` owns one ancilla `anc(g)`. In
each round: every `anc(a)`, `a ∈ 𝒜`, is prepared in `|+⟩`, is the **control** of exactly one CNOT
onto each `q ∈ supp(a)`, and is measured in the `X` basis; every `anc(b)`, `b ∈ ℬ`, is prepared in
`|0⟩`, is the **target** of exactly one CNOT from each `q ∈ supp(b)`, and is measured in the `Z`
basis. No flag ancillas, no cat states, no repeated CNOTs, no change of generating set.

**Definition 1.4 (schedule; legality).** A schedule `M` assigns a time step in `{0,…,T−1}`,
`T ≥ 1`, to every CNOT: `t(a→q)` and `t(q→b)`. `M` is **legal** if at every time step each physical
qubit lies in at most one two-qubit gate.

**Definition 1.5 (measurement consistency).** For `a ∈ 𝒜, b ∈ ℬ` put
`c_{ab}(M) := #{ q ∈ supp(a) ∩ supp(b) : t(q→b) < t(a→q) } mod 2`. `M` is
**measurement-consistent** if `c_{ab}(M) = 0` for all pairs.

```
                                                                                      (MC)
```

**Standing fact 1.6 (why (MC) is part of legality).** A legal `M` produces **deterministic**
detectors — i.e. `C_R(M)` is a syndrome-extraction circuit at all and `d_circ` is defined — iff `M`
satisfies (MC); and when (MC) holds every detector of Definition 1.9 has deterministic value `0`.

*Derivation.* Back-propagating the end-of-round measured Paulis through the round's CNOTs gives
`Ô(X_{anc(a)}) = X_{anc(a)} ∏_{q∈supp(a)} X_q ∏_b X_{anc(b)}^{c_{ab}}` and
`Ô(Z_{anc(b)}) = Z_{anc(b)} ∏_{q∈supp(b)} Z_q ∏_a Z_{anc(a)}^{c'_{ab}}` with
`c'_{ab} = #{q ∈ supp(a)∩supp(b) : t(a→q) < t(q→b)}`; by (CSS), `c_{ab} + c'_{ab} ≡ 0`, so
`c'_{ab} = c_{ab}`. If some `c_{ab} = 1`, then `Ô(Z_{anc(b)})` contains `Z_{anc(a)}` to an odd
power and anticommutes with the stabiliser `X_{anc(a)}` of the freshly prepared `|+⟩`, so `m_{b,r}`
is a uniform bit independent of the past and `D_{b,r}` is not deterministic. If all `c_{ab} = 0`,
then `m_{b,r}` is the value of `Z_{supp(b)}` on the data at the start of round `r`; `Z_{supp(b)}`
back-propagates to itself through a full round (each `Z_q` emits `Z_{anc(a)}` once per `a ∋ q`,
total exponent `|supp(a)∩supp(b)| ≡ 0`), so `m_{b,r}` equals the value of `Z_{supp(b)}` on
`|0⟩^{⊗n}`, namely `0`, for every `r`; dually `X_{supp(a)}` is round-invariant, so
`m_{a,r} = m_{a,0}` for `r ≥ 1`. ∎ *Status: complete modulo the standard stabiliser-formalism
facts (Pauli measurement anticommuting with a stabiliser gives a uniform bit; the CNOT conjugation
table). This is a restatement of the (MC) validity criterion recorded in the round-2+ artifacts;
it is quoted here because §1.4's detector set exists only under it.*

**Scope clause S1 (schedule class).** Every statement below quantifies over
> **all** `(Q, M)` with `Q` a CSS code, `k ≥ 1`, and `M` a **legal, measurement-consistent**
> single-round single-ancilla schedule for the given generating sets — interleaved or not,
> graph-like or not, of any depth `T ≥ 1`, over any check weights.

No further hypothesis on `M` is used anywhere in §3–§5. In particular **graph-likeness is never
used** and the Steane `[[7,1,3]]` instance of §7, which is not graph-like, is inside the scope.

### 1.3 Rounds, and the round-translation clause

**Definition 1.7 (memory experiment).** `C_R^Z(M)` (the **Z-memory**) is: ideal data
initialisation in `|0⟩^{⊗n}`; then `R` **verbatim repetitions** of the round of Definitions 1.3–1.4;
then an ideal transversal `Z`-basis readout of all `n` data qubits. `C_R^X(M)` (the **X-memory**)
is the mirror image under `𝒜 ↔ ℬ`, `X ↔ Z`, control ↔ target: initialisation in `|+⟩^{⊗n}`, ideal
transversal `X`-basis readout. Rounds are indexed `r ∈ {0,…,R−1}`.

**Scope clause S2 (round-translation covariance).** "Verbatim repetition" is used with force: the
set of elementary fault locations of round `r` (Definition 1.10) is in bijection with that of round
`r'` for all `r, r' ∈ {0,…,R−1}`, compatibly with the one-round data of Definition 1.11, and this
bijection is independent of `R`. This holds because each round is the same `T`-step block executed
back to back. It **fails** if a compiler merges the tail of round `r` with the head of round
`r+1` (cross-round idle-layer compression), which is therefore outside the scope; the 公共定义's
instruction to compress meaningless idle layers is read as *within-round* compression, applied once
to `M` before `C_R(M)` is formed. See sub-claim **W-G2** (§8).

### 1.4 Detectors, observables, and the boundary convention

Write `m_{g,r}` for the recorded outcome of check `g` in round `r ∈ {0,…,R−1}`, in the Z-memory.

**Definition 1.8 (boundary conventions).**
```
      m_{b,−1} := 0                                     (data initialised in |0⟩^{⊗n})
      m_{b,R}  := ⊕_{q ∈ supp(b)} (ideal Z readout of q)      (terminal virtual outcome)
```

**Definition 1.9 (detector set; Z-memory).** For every `b ∈ ℬ` and every `r ∈ {0,1,…,R}`,
```
      D_{b,r} := m_{b,r} + m_{b,r−1} .                                                 (D)
```
For every `a ∈ 𝒜` and every `r ∈ {1,…,R−1}`, `D_{a,r} := m_{a,r} + m_{a,r−1}` (the round-0
`X`-outcome is random, so `D_{a,0}` does not exist). Observables:
`λ^{(j)} := ⊕_{q ∈ supp(Z_L^{(j)})}` (ideal readout of `q`), `j = 1,…,k`. The X-memory carries the
mirror set.

> **The boundary convention, stated as the theorem's central hypothesis.** The Z-check detector
> index set is the **full** interval `{0,1,…,R}`: there is one detector per (check, round boundary)
> with **none missing at either temporal end**. The initial detector `D_{b,0} = m_{b,0}` exists
> because `|0⟩^{⊗n}` is a `+1` eigenstate of every `Z_{supp(b)}`; the terminal detector `D_{b,R}`
> exists because the final readout is ideal and transversal in the `Z` basis. Both facts are
> Standing fact 1.6's Step-3 computation. Parts (i) and (ii) of the Theorem are **false** without
> them — see §6.2.

**Scope clause S3 (detector set is fixed).** `d_circ` below is computed against exactly the
detector set of Definition 1.9. Enlarging the detector set can only decrease `d_circ`; that the set
of (D) generates *all* deterministic outcome parities of `C_R(M)` is asserted here as the standard
convention and is **not** re-derived (sub-claim **W-G3**, §8).

### 1.5 Fault model

**Definition 1.10 (elementary faults, unit weight).** One elementary fault is one of:
a single-qubit Pauli (`X`,`Y`,`Z`) on an ancilla immediately after its preparation; one of the 15
non-identity two-qubit Paulis immediately after a CNOT, on (control, target); a single-qubit Pauli
on any qubit (data or ancilla) at any time step at which it is not in a two-qubit gate; or a
classical flip of one recorded ancilla outcome. Data initialisation and final readout are ideal.
Propagation is `F₂`-symplectic: `CNOT(c,t) : x_t ← x_t + x_c`, `z_c ← z_c + z_t`. Ancilla Pauli
frames are zeroed after each round's measurement (each ancilla is prepared afresh). Every
elementary fault has **weight 1**; `|F|` counts elementary faults.

### 1.6 Circuit distance and the three targets

**Definition 1.11 (undetectable logical).** `F` is *undetectable* in `C_R^σ(M)` if it triggers no
detector of Definition 1.9, and *logical* if it flips some observable `λ^{(j)}`.

**Definition 1.12.**
```
      d_R^σ(M) := min{ |F| : F undetectable and logical in C_R^σ(M) } ,     σ ∈ {Z, X} ,
      d_R(M)   := min( d_R^Z(M), d_R^X(M) ) ,
      d_∞(M)   := lim_{R→∞} d_R(M) ,
      R_stab(M):= min{ R_0 ≥ 1 : d_R(M) = d_∞(M) for all R ≥ R_0 } .
```

**Scope clause S4 (both CSS sectors).** `d_R(M)` is the **minimum over the two memory
experiments**, following 公共定义's `d_eff(M) ≤ d_circ(C(M)) ≤ d`. Everything in §2–§5 is proved
**per sector**; §5.3 assembles the minimum. Lemma 2.1 shows that the per-sector quantity `d_R^Z` is
also the circuit distance of the Z-memory circuit against *arbitrary* Pauli faults, so no
generality is lost inside a sector. The identification of 公共定义's `d_circ(C(M))` with
`min(d_R^Z, d_R^X)` is an inherited convention, not a result of this document (sub-claim **W-G1**).

---

## 2. Preliminaries

Everything in §2 is stated for the Z-memory; the X-memory statements are the images under the
mirror of Definition 1.7 and are used without separate proof (the mirror is an isomorphism of the
whole structure, verified numerically in §7 by running both sectors through the same code).

### 2.1 Sector decoupling

**CONJECTURED 2.1.** Let `F` be undetectable and logical in `C_R^Z(M)`. Let `F^X` be obtained from
`F` by replacing each Pauli fault by its `X`-part and deleting (a) the faults whose `X`-part is
trivial and (b) the classical flips of `X`-check outcomes. Then `F^X` is undetectable and logical
in `C_R^Z(M)`, flips the same observables, and `|F^X| ≤ |F|`. Hence `d_R^Z(M)` is attained inside
the **X-sector**: fault components are `X` Paulis and classical flips of **Z**-check outcomes, and
only the **Z-check** detectors of (D) constrain them.

*Derivation.* Propagation is `F₂`-linear and splits: `x`-components travel control→target,
`z`-components target→control, never mixing. `m_{b,r}` is a `Z`-basis measurement of `anc(b)` and
is flipped only by `x`-components; the final `Z`-basis data readout — hence every observable
`λ^{(j)}` and every `D_{b,r}` — likewise. `m_{a,r}` is an `X`-basis measurement of `anc(a)` and is
flipped only by `z`-components, hence so is every `D_{a,r}`. So the `D_{b,r}` and the `λ^{(j)}` are
functions of the `X`-parts alone and the `D_{a,r}` are functions of the `Z`-parts alone. `F`
undetectable ⟹ its `X`-parts trigger no `D_{b,r}`; `F^X` has no `z`-component, so it triggers no
`D_{a,r}` either. Availability: at a two-qubit location all 15 non-identity Paulis are present, so
the `X`-part of any fault is itself an available fault when non-trivial; likewise at one-qubit
locations. ∎ *Status: complete.*

From here to §5, "fault" means an X-sector elementary fault and "detector" means a Z-check
detector `D_{b,r}`, `r ∈ {0,…,R}`.

### 2.2 One-round data

**Definition 2.2.** For an elementary fault `f` placed in round `r`:

| symbol | definition | lives in |
|---|---|---|
| `E(f)` | the residual `X` error on the **data** at the end of round `r` | `F₂^n` |
| `s(f)` | `s_b(f) := |supp(b) ∩ E(f)| mod 2` | `F₂^ℬ` |
| `u(f)` | `u_b(f) :=` the flip `f` induces in the **round-`r`** outcome `m_{b,r}` | `F₂^ℬ` |
| `λ(f)` | `λ^{(j)}(f) := |E(f) ∩ supp(Z_L^{(j)})| mod 2` | `F₂^k` |

**CONJECTURED 2.3 (round-independence).** None of `E, s, u, λ` depends on `r`.

*Derivation.* Rounds are verbatim repetitions (S2); ancillas carry no incoming frame because they
are freshly prepared (Definition 1.10); the fault's own propagation within its round therefore sees
the same gate sequence with the same zero ancilla frame in every round. ∎ *Status: complete, and
this is exactly where S2 is consumed.*

**CONJECTURED 2.4 (round transparency).** A data `X` error `E` present at the start of round `r`
is unchanged at the end of round `r`, and its only effect on that round's records is to flip
`m_{b,r}` by `s_b(E)` for each `b ∈ ℬ`.

*Derivation.* A data qubit is the **target** only of gates `a→q` and the **control** only of gates
`q→b`. An `x` on data qubit `q` is therefore never overwritten (targets receive, controls keep) and
propagates to `anc(b)` exactly once for each `b` with `q ∈ supp(b)`, i.e. it flips `m_{b,r}` by
`[q ∈ supp(b)]`. Summing over `q ∈ E` gives `s_b(E)`. The `X`-ancillas start each round with zero
frame and are never targets, so nothing flows back onto the data. ∎ *Status: complete. This is the
lemma the entire node rests on, and it is exactly where a schedule outside Definition 1.3 (flag
ancillas, cat states, repeated CNOTs, un-reset ancillas) would break the analysis.*

### 2.3 Time locality

**CONJECTURED 2.5.** A fault `f` placed in round `r ∈ {0,…,R−1}` flips exactly the detectors

```
      ∂(f, r)  =  [ u(f) ]_r  +  [ u(f) + s(f) ]_{r+1}   ∈  F₂^{ ℬ × {0,…,R} } ,        (∂)
```

and flips the observables by `λ(f)`.

*Derivation.* `m_{b,r}` is flipped by `u_b(f)` by definition. For `r' > r` the data carries `E(f)`
throughout round `r'`, so by 2.4 `m_{b,r'}` is flipped by `s_b(f)`; the virtual `m_{b,R}` is
flipped by `s_b(f)` too, because the ideal readout sees `E(f)`. Substituting into (D):
`D_{b,r}` receives `u_b`; `D_{b,r+1}` receives `u_b + s_b`; `D_{b,r'}` receives `s_b + s_b = 0` for
`r' ≥ r+2`. The convention `m_{b,−1} = 0` makes `r = 0` an instance of the same formula, and
`r+1 ≤ R` is always a legitimate detector index because `r ≤ R−1`. The observable statement is
Definition 2.2 applied to the ideal readout. ∎ *Status: complete. Both boundary conventions of
Definition 1.8 are consumed here: `m_{b,−1} = 0` for `r = 0`, and the existence of `m_{b,R}` for a
fault in round `R−1`.*

**NUMERICAL 2.6.** (∂) verified against direct multi-round simulation for **every** elementary
fault, every round `r ∈ {0,…,R−1}` and every `R ∈ {1,…,6}`, on 12 (schedule, sector) instances:
**35 658 / 35 658** columns agree, `0` disagreements. Scope and code: §7.1.

### 2.4 The undetectability criterion

**Definition 2.7 (prefix sums).** For a fault set `F ⊆ 𝔽 × {0,…,R−1}` and `b ∈ ℬ`, `r ∈ Z`:
```
      c_b(r) := Σ_{ (f,r_f) ∈ F , r_f ≤ r }  s_b(f)      (accumulated residual syndrome after round r)
      U_b(r) := Σ_{ (f,r_f) ∈ F , r_f = r }  u_b(f)      (total round-r outcome flips on b)
```
so `c_b(r) = 0` for `r < 0` and `c_b(r) = c_b(R−1)` for `r ≥ R−1`.

**CONJECTURED 2.8 (criterion).** `F` is undetectable in `C_R^Z(M)` **iff**

```
      U_b(r)  =  c_b(r−1)      for every  b ∈ ℬ  and every  r ∈ {0,1,…,R} .            (W)
```

Moreover (W) for `r ∈ {0,…,R}` is equivalent to (W) for **all** `r ∈ Z`, and the instance `r = R`
reads `c_b(R−1) = 0`: **the total residual syndrome of any undetectable `F` vanishes.**

*Derivation.* By 2.4 and Definition 2.2 the recorded `m_{b,r}` is flipped by exactly
`c_b(r−1) + U_b(r)` for `r ∈ {0,…,R−1}`, and `m_{b,R}` is flipped by `c_b(R−1)` (ideal readout of
the accumulated residual), which is `c_b(R−1) + U_b(R)` with `U_b(R) := 0` since there is no round
`R`. Hence `D_{b,r} = [c_b(r−1) + U_b(r)] + [c_b(r−2) + U_b(r−1)]` for `r ∈ {0,…,R}` with the
convention that the second bracket is `0` at `r = 0`. So `D_{b,r} = 0` for all `r ∈ {0,…,R}` says
that the sequence `r ↦ c_b(r−1) + U_b(r)` is constant on `{0,…,R}`, and the `r = 0` instance
`D_{b,0} = c_b(−1) + U_b(0) = U_b(0)` pins that constant to `0`. This is (W). For the extension to
all `r ∈ Z`: for `r < 0` both sides are `0`; for `r > R` we have `U_b(r) = 0` and
`c_b(r−1) = c_b(R−1)`, which the `r = R` instance forces to `0`. ∎ *Status: complete.*

> **(W) in words.** *A fault set is undetectable iff, in every round and on every Z-check, the
> number of in-round measurement flips equals the parity of the residual syndrome accumulated by
> all strictly earlier rounds.* Both temporal boundaries appear: the initial detector supplies the
> constant `0` at `r = 0`, and the terminal detector supplies the closing condition at `r = R`.

**CONJECTURED 2.9 (the observable).** `F` flips observable `j` iff
`Σ_{(f,r_f) ∈ F} λ^{(j)}(f) = 1`; equivalently, writing `E_tot(F) := Σ_{(f,r_f)∈F} E(f) ∈ F₂^n`,
iff `|E_tot(F) ∩ supp(Z_L^{(j)})|` is odd. In particular the observable depends on `F` **only
through `E_tot(F)`**, not on the round assignment.

*Derivation.* The ideal readout measures each data qubit in the `Z` basis, so the recorded value of
`Z_L^{(j)}` is flipped exactly by the terminal residual `E_tot(F)` (2.4: residuals persist and add
over rounds). ∎ *Status: complete.*

**NUMERICAL 2.10.** (W) verified against direct simulation on **16 000 / 16 000** random fault
subsets (weights 1–4, `R ∈ {1,…,5}`, 8 (schedule, sector) instances): the direct-simulation
detector vector vanishes **iff** (W) holds, in every case. Code and scope: §7.3.

### 2.5 The ceiling lemma

**CONJECTURED 2.11 (zero-voltage terminal singleton).** For every data qubit `q ∈ [n]` there is an
elementary X-sector fault `f_q`, placeable in any round, with `E(f_q) = {q}` and `u(f_q) = 0`.

*Derivation.* Let `t*` be the largest time step at which `q` lies in a two-qubit gate (legality,
Definition 1.4, makes that gate unique). If the gate at `t*` is `q→b`, take the two-qubit fault
`X⊗I` immediately after it (an `X` on the control `q`); if it is `a→q`, take `I⊗X` immediately
after it (an `X` on the target `q`). In either case the residual on the data is `{q}` and, since
every gate `q→b'` has `t(q→b') ≤ t*` and has therefore already executed, the `X` reaches no
`anc(b')`: `u = 0`. If `q` lies in no gate at all, take a single-qubit `X` at any of the `T ≥ 1`
idle steps of `q`; again `E = {q}`, `u = 0`. ∎ *Status: complete.*

**CONJECTURED 2.12 (ceiling).** `d_R^Z(M) ≤ d_X` and `d_R^X(M) ≤ d_Z` for every `R ≥ 1`; hence
`d_R(M) ≤ d` for every `R ≥ 1`, and `1 ≤ d_R(M) ≤ d`.

*Derivation.* Take `v ∈ ker H_Z ∖ S_X` with `|v| = d_X` (Standing fact 1.2, non-empty by S0). Put
`F := { (f_q, R−1) : q ∈ v }` with `f_q` from 2.11; `|F| = d_X`. Check (W): for `r ≤ R−1`,
`U_b(r) = 0` (all `u(f_q) = 0`) and `c_b(r−1) = 0` (no fault lies in a round `< R−1`); for `r = R`,
`U_b(R) = 0` and `c_b(R−1) = s_b(v) = (H_Z v)_b = 0`. So `F` is undetectable. By 2.9 and
Standing fact 1.2, `E_tot(F) = v ∉ S_X` flips some `λ^{(j)}`, so `F` is logical. Hence
`d_R^Z ≤ d_X`; the mirror gives `d_R^X ≤ d_Z`; the minimum gives `d_R ≤ min(d_X,d_Z) = d`. The
lower bound `d_R ≥ 1` holds because `F = ∅` flips nothing. ∎ *Status: complete.*

**NUMERICAL 2.13.** The explicit witness of 2.12 built and verified by direct simulation
(undetectable and observable-flipping) on **40 / 40** (instance, `R`) pairs, `R ∈ {1,…,5}`, in both
sectors, with `d_X = 3` recomputed independently by brute force over `ker H_Z ∖ S_X`. Code: §7.3.

---

## 3. Part (i) — monotonicity

> **CONJECTURED 3.1 (padding).** For every `R ≥ 1` and each sector `σ ∈ {Z,X}`,
> `d_{R+1}^σ(M) ≤ d_R^σ(M)`. Hence `d_{R+1}(M) ≤ d_R(M)`.

*Derivation (Z-memory; the X-memory is the mirror).* Let `F` be undetectable and logical in
`C_R^Z(M)` with `|F| = d_R^Z(M)`; by 2.1 we may take `F` inside the X-sector. Define
`F' := F ⊆ 𝔽 × {0,…,R−1} ⊆ 𝔽 × {0,…,R}`, i.e. **the same faults at the same round indices**, with
round `R` of `C_{R+1}^Z(M)` left fault-free. By S2 every fault location used by `F` exists in
`C_{R+1}^Z(M)` at the same index and carries the same `(E,s,u,λ)` (2.3), so `F'` is a legitimate
fault set of `C_{R+1}` with `|F'| = |F|`.

**Detector bookkeeping, both temporal boundaries.** Write `U'_b, c'_b` for the prefix sums of `F'`
in `C_{R+1}`, and `U_b, c_b` for those of `F` in `C_R`. Since `F' = F` as a set of (fault, round)
pairs, `U'_b(r) = U_b(r)` and `c'_b(r) = c_b(r)` for all `r`. We must verify (W) for `F'` over the
**enlarged** index range `r ∈ {0,1,…,R+1}`.

* `r ∈ {0,…,R}`: `U'_b(r) = U_b(r) = c_b(r−1) = c'_b(r−1)`, by (W) for `F` in `C_R` — whose index
  range is exactly `{0,…,R}`. In particular:
  * the **initial** detector `D_{b,0}` of `C_{R+1}` is the initial detector of `C_R`, and both are
    absolute (`m_{b,−1} = 0`), so the `r = 0` instance transfers verbatim;
  * the **index-`R`** detector changes meaning between the two circuits — in `C_R` it is
    `D_{b,R} = m_{b,R}^{(readout)} + m_{b,R−1}`, in `C_{R+1}` it is
    `D_{b,R} = m_{b,R}^{(round-R measurement)} + m_{b,R−1}`. It nevertheless receives the same
    value, because by 2.4 the residual `E_tot` present throughout the fault-free round `R` flips
    the round-`R` measurement `m_{b,R}` by exactly `s_b(E_tot) = c_b(R−1)`, which is precisely what
    the ideal readout of `C_R` was flipped by. This is the one step where "appending a fault-free
    round" is not a triviality, and it is where round transparency (2.4) is consumed.
* `r = R+1` (the **new terminal** detector of `C_{R+1}`): `U'_b(R+1) = 0` because round `R` carries
  no fault and there is no round `R+1`; and `c'_b(R) = c'_b(R−1) = c_b(R−1) = 0` by the `r = R`
  instance of (W) for `F` in `C_R` (Lemma 2.8's closing condition). So `0 = 0`. ∎ (of the detector
  check)

**Observable.** `E_tot(F') = E_tot(F)`, so by 2.9 `F'` flips the same observables; `F` is logical,
hence so is `F'`. Therefore `d_{R+1}^Z ≤ |F'| = |F| = d_R^Z`.

Finally `d_{R+1} = min_σ d_{R+1}^σ ≤ min_σ d_R^σ = d_R`. ∎

*Derivation status: complete.*

**Remark 3.2 (prepending also works, and why one should check).** Define `F'' := F + 1` (all faults
moved one round later) inside `C_{R+1}`, leaving round `0` fault-free. (W) for `F''` at `r = 0`
reads `U''_b(0) = 0 = c''_b(−1)` ✓; for `r ≥ 1` it is the translate of (W) for `F`, using
`c''_b(r−1) = c_b(r−2)`. So prepending a fault-free round preserves the witness too. Both
directions are needed for §5: appending gives monotonicity, and the *combination* — free
translation of a fault set in time — is Lemma 4.3.

**Remark 3.3 (what monotonicity says physically).** Under the ideal spacelike readout of Definition
1.8, extra rounds add fault locations without adding protection, because the ideal readout already
supplies the terminal syndrome comparison. The sequence `d_R` therefore never rises. This is the
*opposite* of the intuition imported from settings where the logical output is itself a measurement
outcome; see §6.2 and §6.3.

**NUMERICAL 3.4.** `d_{R+1} ≤ d_R` on `R ∈ {1,…,5}` verified in **44 / 44** (schedule, sector)
instances (12 from §7.1 at `R ≤ 6`, 32 from the §7.2 sweep at `R ≤ 5`), `0` violations, and
independently in Stim for the standard rotated-surface schedule at `d = 3,5,7`, `R = 1..10`. Scope:
§7.

---

## 4. Part (ii) — contiguity and the span bound

> **CONJECTURED 4.1 (contiguity / no idle round).** Fix `R ≥ 1` and a sector `σ ∈ {Z,X}`. Let `F`
> be an undetectable logical fault set of `C_R^σ(M)` of **minimum weight**, `|F| = d_R^σ(M)`. Let
> `supp_t(F) := { r ∈ {0,…,R−1} : F has a fault in round r }`. Then `supp_t(F)` is a **contiguous
> interval**, and its length `w := |supp_t(F)|` satisfies
> ```
>        w  ≤  |F|  =  d_R^σ(M)  ≤  d ;
> ```
> and when `σ` attains the sector minimum, `d_R^σ(M) = d_R(M)`.

*Derivation (Z-memory; mirror for X-memory).* By 2.1 take `F` inside the X-sector, which does not
change `|F|` or the observables. Suppose `supp_t(F)` is not contiguous: there is
`r` with `min supp_t(F) < r < max supp_t(F)` and `r ∉ supp_t(F)`. Split

```
      F = F_1 ⊔ F_2 ,      F_1 := faults of F in rounds < r ,     F_2 := faults in rounds > r ,
```
both non-empty (by the choice of `r`), and `F_1 ∪ F_2 = F` (round `r` is fault-free).

**Step 1: the accumulated syndrome vanishes at `r`.** Apply (W) (Lemma 2.8) to `F` at index `r`.
Round `r` carries no fault, so `U_b(r) = 0`, hence `c_b(r−1) = 0` for every `b`. Since only `F_1`
contributes to rounds `≤ r−1`, this says
```
      c_b^{F_1}(r−1) = 0  for all b ,   and   c_b^{F_1}(r') = c_b^{F_1}(r−1) = 0  for all r' ≥ r−1 ,
```
i.e. `H_Z · E_tot(F_1) = 0`: **`F_1` closes on its own.**

**Step 2: `F_1` is undetectable in `C_R`.** Verify (W) for `F_1` at every `r' ∈ {0,…,R}`.
* `r' ≤ r`: `F_2` lives in rounds `> r ≥ r'`, so `U_b^{F_2}(r') = 0` and `c_b^{F_2}(r'−1) = 0`;
  hence `U_b^{F_1}(r') = U_b^{F}(r')` and `c_b^{F_1}(r'−1) = c_b^{F}(r'−1)`, and (W) for `F`
  gives (W) for `F_1`.
* `r' > r`: `F_1` lives in rounds `< r < r'`, so `U_b^{F_1}(r') = 0`; and `c_b^{F_1}(r'−1) = 0` by
  Step 1. So both sides vanish.

**Step 3: `F_2` is undetectable in `C_R`.** Symmetrically.
* `r' ≤ r`: `U_b^{F_2}(r') = 0` and `c_b^{F_2}(r'−1) = 0` (nothing of `F_2` lies in rounds `≤ r−1`).
* `r' > r`: `U_b^{F_2}(r') = U_b^{F}(r')`, and
  `c_b^{F_2}(r'−1) = c_b^{F}(r'−1) + c_b^{F_1}(r'−1) = c_b^{F}(r'−1) + 0`, by Step 1. So (W) for
  `F` gives (W) for `F_2`.

**Step 4: one half is still logical.** `E_tot(F) = E_tot(F_1) + E_tot(F_2)`, so by 2.9
`λ(F) = λ(F_1) + λ(F_2)` in `F₂^k`. `F` is logical, i.e. `λ(F) ≠ 0`, hence `λ(F_1) ≠ 0` or
`λ(F_2) ≠ 0`. Say `λ(F_i) ≠ 0`. Then `F_i` is an undetectable logical fault set **of the same
circuit `C_R(M)`** with `|F_i| < |F|` (the complementary half is non-empty). This contradicts the
minimality of `|F| = d_R(M)`. Hence `supp_t(F)` is contiguous.

**Span bound.** Contiguity means every round of the interval `[min supp_t(F), max supp_t(F)]`
carries at least one fault of `F`, so `w = |supp_t(F)| ≤ |F|` — this is where unit fault weight
(Definition 1.10) is consumed. And `|F| = d_R^σ(M) ≤ d` by 2.12. ∎

*Derivation status: complete. Note the contradiction is obtained **inside `C_R(M)` itself** — no
restriction to a shorter circuit, no reindexing, and no appeal to minimality of `R`. That is what
makes this statement quantify over every `R ≥ 1` at once.*

**Remark 4.2 (exactly what is and is not claimed).** 4.1 is a statement about **minimum-weight**
undetectable logicals only. Non-minimum ones need not be contiguous (Steps 2–3 still split them,
but Step 4's contradiction is unavailable). Also, the bound is `w ≤ |F|`, not `w ≤ d_∞`; the
sharper `w ≤ d_∞` at `R = R_stab` is Corollary 5.2.

> **CONJECTURED 4.3 (time translation).** Fix a sector `σ`. Let `F` be an undetectable logical
> fault set of `C_R^σ(M)` with `supp_t(F) ⊆ [r_0, r_1]`, `w := r_1 − r_0 + 1`. Then for every
> `R' ≥ w` and every shift `δ` with `[r_0+δ, r_1+δ] ⊆ {0,…,R'−1}`, the translated set `F + δ` is an
> undetectable logical fault set of `C_{R'}^σ(M)` of the same weight. In particular
> ```
>        d_{R'}(M)  ≤  d_{R'}^σ(M)  ≤  |F|      for every  R' ≥ w .
> ```

*Derivation.* By S2 and 2.3 the translated faults exist and carry the same `(E,s,u,λ)`, so
`|F+δ| = |F|` and `E_tot(F+δ) = E_tot(F)`; by 2.9 `F+δ` flips the same observables. For
undetectability, use the "all `r ∈ Z`" form of (W) (Lemma 2.8): the prefix sums of `F+δ` are
`U_b^{F+δ}(r) = U_b^{F}(r−δ)` and `c_b^{F+δ}(r) = c_b^{F}(r−δ)`, so (W) for `F` at `r−δ` is (W) for
`F+δ` at `r`. It remains to check that the index range of `C_{R'}` is large enough: (W) for `F+δ`
is non-trivial only at indices `r ∈ [r_0+δ, r_1+δ+1]`, and `r_1+δ+1 ≤ R'` because
`r_1+δ ≤ R'−1`; while `r_0+δ ≥ 0`. Outside that range both sides of (W) vanish, as computed in
Lemma 2.8. Taking `δ = −r_0` and `R' ≥ w` gives the displayed inequality. ∎
*Status: complete. This is where the "no detector missing at either end" convention is consumed a
second time: the translated witness must find a genuine detector at every index it touches, at both
ends of the shorter circuit.*

**NUMERICAL 4.4.** Every minimum-weight undetectable logical found by exhaustive search — **10 487**
of them: 3 399 over the 12 instances of §7.1 at `R ∈ {1,…,6}`, plus 7 088 over the 32 sweep
instances of §7.2 at `R ∈ {1,…,5}` — has contiguous round support with span `≤` weight:
**10 487 / 10 487**, `0` violations. Separately, **1 772 / 1 772**
minimum-weight witnesses were explicitly translated down to `C_w` (`w` = their own span) and
re-verified undetectable and logical by direct simulation, certifying 4.3 constructively. Scope and
code: §7.

---

## 5. Part (iii) — the window, and the decision procedure

> **CONJECTURED 5.1 (stability window).** For every `(Q,M)` in the scope of S0–S4:
>
> 1. `(d_R(M))_{R≥1}` is a non-increasing sequence of integers in `[1, d]`, hence eventually
>    constant; `d_∞(M) := lim_R d_R(M) = min_{R≥1} d_R(M)` exists and lies in `[1, d]`.
> 2. `d_R(M) = d_d(M)` for every `R ≥ d`; in particular **`d_∞(M) = d_d(M)`**.
> 3. `R_stab(M)` is well defined and `R_stab(M) ≤ d_∞(M) ≤ d`.

*Derivation.*

**(1)** Monotonicity is Theorem 3.1; `1 ≤ d_R ≤ d` is 2.12. A non-increasing integer sequence
bounded below converges and its limit is its minimum.

**(2)** Let `R ≥ d`. Monotonicity gives `d_R ≤ d_d`. For the converse, let `F` be a minimum-weight
undetectable logical of `C_R(M)` in the sector attaining the minimum, so `|F| = d_R(M)`. By
Theorem 4.1, `supp_t(F)` is contiguous with span `w ≤ |F| = d_R ≤ d`. By Lemma 4.3 applied with
`R' = d ≥ w`, `d_d(M) ≤ |F| = d_R(M)`. Hence `d_R = d_d`. Combining with monotonicity on
`R ≤ d`, `min_{R≥1} d_R = d_d`, i.e. `d_∞ = d_d`.

*(Note the argument in fact gives `d_d(M) ≤ d_R(M)` for **every** `R ≥ 1`, since `w ≤ d` always;
for `R < d` this is also immediate from monotonicity.)*

**(3)** Well-definedness: by (2) the set `{R_0 : d_R = d_∞ ∀R ≥ R_0}` contains `d`, so its minimum
exists and `R_stab ≤ d`. For the sharper bound put `R := R_stab(M)`, so `d_R = d_∞`. Let `F` be a
minimum-weight undetectable logical of `C_R(M)` in the attaining sector, `|F| = d_∞`, with
contiguous span `w ≤ |F| = d_∞` (Theorem 4.1). Suppose `w < R`. By Lemma 4.3 with `R' = w`,
`d_w(M) ≤ |F| = d_∞`; and `d_w ≥ d_∞` since `d_∞` is the minimum. So `d_w = d_∞` with `w < R`. But
`(d_R)` is non-increasing, so `d_{R'} = d_∞` for **all** `R' ≥ w`, contradicting the minimality of
`R = R_stab`. Hence `w ≥ R`, i.e. `R_stab = R ≤ w ≤ d_∞ ≤ d`. ∎

*Derivation status: complete, relative to §2–§4.*

**Corollary 5.2 (every round of a critical witness is faulty).** At `R = R_stab(M)`, a
minimum-weight undetectable logical of `C_R(M)` has a fault in **every** one of the `R` rounds, and
`R_stab(M) ≤ d_∞(M)` is exactly the pigeonhole `#rounds ≤ #faults`. *(This is the content extracted
in the proof of 5.1(3): `w ≥ R` together with `supp_t ⊆ {0,…,R−1}` forces `w = R`.)*

**Corollary 5.3 (finite-window decision procedure — fixed window).** For every `(Q,M)` in scope:
```
      d_∞(M)    = d_d(M) ,
      R_stab(M) = min{ R ∈ {1,…,d} : d_R(M) = d_d(M) } .
```
Both are computed from the finite list `d_1(M), d_2(M), …, d_d(M)`, i.e. from `d` circuit-distance
computations on circuits of at most `d` rounds. No circuit with more than `d` rounds is ever
constructed, and no property of `d_R` for `R > d` is ever tested.

*Derivation.* `d_∞ = d_d` is 5.1(2). By monotonicity, `d_R = d_∞` for all `R ≥ R_0` iff
`d_{R_0} = d_∞`; and `R_stab ≤ d` by 5.1(3), so the minimum may be taken over `{1,…,d}`. ∎

**Corollary 5.4 (adaptive procedure — strictly smaller window).**
```
      R := 1
      loop:  compute d_R(M)
             if R ≥ d_R(M):  return  d_∞ = d_R(M),
                                     R_stab = min{ j ≤ R : d_j(M) = d_R(M) }
             R := R + 1
```
This halts at `R ≤ d_∞(M) ≤ d`, hence never later than Corollary 5.3 and usually much earlier
(at `R = 1` whenever `d_1(M) = 1`, at `R ≤ 2` whenever `d_1(M) ≤ 2`, and so on).

*Derivation.* Correctness of the stopping rule: suppose `R ≥ d_R(M)`. By 5.1(3) and 5.1(1),
`R_stab ≤ d_∞ ≤ d_R ≤ R`, so `R ≥ R_stab` and therefore `d_R = d_∞`; the displayed `R_stab` is then
correct by monotonicity, as in 5.3. Halting: at `R = d_∞` we have `d_R = d_∞ = R` (since
`R = d_∞ ≥ R_stab` gives `d_R = d_∞`), so the test fires no later than `R = d_∞ ≤ d`. ∎

**Corollary 5.5 (the frozen historical `R_sat`, corrected).** With
`R_sat(M) := min{R_0 : d_R(M) = d for all R ≥ R_0}` (`= ∞` if none), as frozen in
`CIRCDIST_PROBLEMS.md` 课题四:
```
      R_sat(M) = 1        if  d_∞(M) = d ,
      R_sat(M) = ∞        if  d_∞(M) < d ,
```
and which case holds is decided by the single test `d_d(M) = d`.

*Derivation.* If `d_∞ = d`, then for every `R ≥ 1` monotonicity gives `d_R ≥ min_{R'} d_{R'} =
d_∞ = d` while 2.12 gives `d_R ≤ d`; so `d_R = d` for all `R ≥ 1` and `R_sat = 1`. If `d_∞ < d`,
then for every `R ≥ R_stab` we have `d_R = d_∞ < d`; so no `R_0` can satisfy "`d_R = d` for all
`R ≥ R_0`" (it fails already at `R = max(R_0, R_stab)`), and `R_sat = ∞`. ∎ *This is the corrected
form; the value `1` (not `≤ d`) matters — see §6.4.*

**NUMERICAL 5.6.** `d_R = d_{R=d}` for all `R ≥ d`, and `R_stab ≤ d_∞ ≤ d`, verified in **44 / 44**
(schedule, sector) instances. Observed values: `d_∞ ∈ {2, 3}`, `R_stab = 1` in every instance.
Scope: §7; the `R_stab = 1` observation is **absence evidence with the scope stated**, not a
theorem — see §7.5.

---

## 6. Quantifier and convention audit

The review's known attack surface for this node is quantifier hygiene. This section makes every
dependency explicit.

### 6.1 Which clause is load-bearing where

| clause | statement | consumed by |
|---|---|---|
| **S0** | CSS code, `k ≥ 1`, fixed generating sets `𝒜, ℬ` | 1.2, 2.12 |
| **S1** | `M` legal **and** measurement-consistent, single-round, single-ancilla, one CNOT per (check, data qubit), any depth, interleaved or not, graph-like or not | 1.6 (detectors exist at all), 2.4, 2.11 |
| **S2** | rounds are verbatim repetitions; fault locations of round `r` ≅ those of round `r'` | 2.3, 3.1, 4.3 |
| **S3** | detector set = exactly Definition 1.9 | 2.8 |
| **S4** | `d_R = min` over the two memory experiments; each sector proved separately | 5.1, 5.3 |
| **ideal init** (`m_{b,−1} = 0`, `D_{b,0}` exists) | 1.8, 1.9 | 2.5 (`r = 0` case), 2.8 (pins the constant to `0`), 3.1 (`r = 0`), 4.3 (left end) |
| **ideal readout** (`m_{b,R}` exists, `D_{b,R}` exists) | 1.8, 1.9 | 2.5 (fault in round `R−1`), 2.8 (closing condition `c_b(R−1) = 0`), 3.1 (index-`R` and new terminal detector), 4.3 (right end) |
| **unit fault weight** | 1.10 | 4.1 span bound (`w ≤ |F|` counts one fault per round), 5.1(3) |
| **ancilla reset each round** | 1.10 | 2.3, 2.4 |

**Never used anywhere:** graph-likeness; any bound on check weight; any bound on `T`;
non-interleaving; any property of the min-plus transfer matrix of the sibling node
`CIRCDIST.sat.transfer`; any numerical result of §7.

### 6.2 What breaks if a boundary is relaxed

* **Noisy / non-ideal initialisation.** `D_{b,0}` does not exist. Lemma 2.8's constant is no longer
  pinned to `0`: (W) becomes `U_b(r) = c_b(r−1) + κ_b` for an unconstrained `κ ∈ F₂^ℬ`. Every
  statement of §3–§5 must then be re-derived; Step 1 of Theorem 4.1 in particular concludes
  `c_b(r−1) = κ_b` rather than `0`, and the split of Steps 2–3 no longer produces two independently
  closed halves. **Out of scope.**
* **Non-ideal / absent final data readout.** `D_{b,R}` does not exist. Lemma 2.8's closing
  condition `c_b(R−1) = 0` is lost, so the total residual syndrome is free at the last boundary;
  Theorem 3.1's new-terminal-detector check and Lemma 4.3's right-end check both fail.
  **Out of scope.**
* **Logical output taken as a measurement outcome (timelike logical).** This is a *different
  observable*, not a relaxed boundary, and it is exactly the setting the re-scope note removes from
  the current problem. In that setting the received statement is the opposite sign (`≈ d` rounds
  are *required*); this document makes no claim about it, and no step of §3–§5 should be quoted in
  support of, or against, any statement there. See §6.3 A2.
* **Cross-round idle-layer compression.** Violates S2; 2.3 and 4.3 fail. **Out of scope**
  (sub-claim W-G2).

### 6.3 External statements used, as ASSUMPTIONS

Only two external items are touched, and **neither is load-bearing** for §3–§5.

**A1 — Composition theorem for stabilizer channels is SUFFICIENT, not necessary.** Beverland,
Huang, Kliuchnikov, "Fault tolerance of stabilizer channels" (arXiv:2401.12017), **Theorem VI.2**
(cite §VI, not the abstract, which says "necessary"): for compatible time-local channels with
unit-weight faults, if two consecutive compositions have fault distance `≥ d` and the middle
channel's time-local partition has size `≥ d`, then the triple composition has fault distance
`≥ d`. *Relation to this document:* their contiguity observation for time-local channels is the
ancestor of Theorem 4.1's shape, but their conclusion is one-sided (`≥ d`, never an equality) and
calibrated to a pre-chosen `d`. Theorem 4.1 is re-derived here from (W), not imported. *Not
load-bearing.*

**A2 — The timelike-logical folklore lives under a different observable.** BHK §VIII B states, for
a channel whose logical output is a **measurement outcome**, that `d` repeated rounds are required.
*Relation to this document:* it is the contrast case of §6.2 bullet 3. *Not load-bearing, and not
contradicted:* the two statements concern different observables.

*(Bibliographic verification status of A1/A2 is inherited from
`artifacts/circdist_sat_recon_20260820.md` §6 A5, which reports them as arXiv-verified in that
session; this session did not re-fetch them, and does not need to, since neither is load-bearing.)*

### 6.4 Relation to the lift-side material — and why its review does not transfer

`artifacts/circdist_lift_iff_proof_20260820.md` §5.9 ("no idle round") contains a contiguity
argument of the same shape, and its §5.10 draws consequences. Three things must be said plainly.

1. **This document does not cite or depend on it.** §4.1 is derived here from Definitions 1.1–1.12
   and Lemmas 2.1–2.12 only. The reader may compare, but nothing here fails if §5.9 is withdrawn.
2. **The review CONFIRM on that lemma is bound to `CIRCDIST.lift`, not to this node.**
   `artifacts/circdist_lift_proofs_review_20260820.md` row `H` records a CONFIRM for the contiguity
   statement *as a lemma of the lift document*. Under rule 6 that confirmation attaches to the node
   and hash it was issued against; it is **not** a review of `CIRCDIST.sat.window`, whose statement
   (Theorem 4.1 here) differs in its quantifier over `R`, in carrying both sectors explicitly, and
   in being coupled to Lemma 4.3 and Theorem 5.1. **This node still requires its own independent
   claim-level review.**
3. **The known error in that neighbourhood is not reproduced here.** The lift document's original
   §5.10(1) asserted "`R_sat(M) ≤ d`"; that clause was **retracted as false** in
   `artifacts/circdist_lift_iff_amendment1_20260820.md` §3, and the retraction was value-confirmed
   in `artifacts/circdist_amendments_review_20260820.md` §3.6, which further sharpened the
   corrected first branch from `R_sat ≤ d` to `R_sat = 1` (its finding **L2**). Corollary 5.5 above
   states the sharpened form. No statement of the form "`R_sat ≤ d`" appears anywhere in this
   document.

### 6.5 Relation to the sibling sub-nodes

`CIRCDIST.sat` is assembled by an AND-route over `transfer`, `window`, `instances`. This document
discharges **`window` only**. It does **not** establish the min-plus transfer representation
(`CIRCDIST.sat.transfer`), and no step above uses one: Theorem 5.1 is proved by a direct splitting
and translation argument, not by any spectral or tropical property of a transfer matrix. It does
**not** compute `(d_∞, R_stab)` for the schedule families the problem statement names
(`CIRCDIST.sat.instances`); §7 is corroboration of the *theorem*, not delivery of those instances.

---

## 7. NUMERICAL corroboration — scope stated, code inline

**Nothing in §7 is used by any proof step in §2–§5.** These are independent checks that the
theorem's conclusions and its three load-bearing lemmas hold where they can be tested exhaustively.

**Common scope for §7.1–§7.4.**
* Codes: rotated surface `[[9,1,3]]` (`𝒜 = {12, 0134, 4578, 67}`, `ℬ = {03, 1245, 3467, 58}`,
  `X_L = {0,3,6}`, `Z_L = {0,1,2}`) and Steane `[[7,1,3]]` (Hamming checks `{3456, 1256, 0246}`,
  `X_L = Z_L = {0,1,2}`). The Steane Z-memory sector is **not graph-like** (`X₆` flips three
  detectors), so it exercises the hypergraph case.
* Both CSS sectors for every schedule (the X-memory is obtained by the mirror of Definition 1.7 and
  run through the identical code path).
* Fault model: Definition 1.10, X-sector, including idle locations; unit weight.
* Ground truth is **direct multi-round simulation** of `C_R(M)` with an explicit `F₂` frame over all
  `n + |𝒜| + |ℬ|` qubits and explicit detectors `D_{b,r}`, `r = 0..R`. Lemma 2.5's column form is
  *tested against* that ground truth, never assumed.
* Exhaustive minimum-weight search by meet-in-the-middle over deduplicated `(round, column)` pairs,
  weights `1,2,3,4`; all instances resolve at weight `≤ 3`, so the searches are exhaustive at the
  reported minimum, and the enumeration of *all* minimum-weight witnesses is complete.
* `R` ranges: `1..6` (§7.1), `1..5` (§7.2, §7.3).

### 7.1 Per-schedule run (12 instances, `R = 1..6`)

```
rotated-surface-d3 :: ZN-order, interleaved (standard)
  Z-memory (X-sector)      d_R(R=1..6)=[3,3,3,3,3,3]  d_inf=3 R_stab=1
     time-locality 2184/2184 | monotone True | const R>=d True | R_stab<=d_inf<=d True
     min-wt witnesses 579/579 contiguous & span<=weight | spans/R [[1],[1,2],[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
  X-memory (Z-sector)      d_R(R=1..6)=[3,3,3,3,3,3]  d_inf=3 R_stab=1
     time-locality 2184/2184 | monotone True | const R>=d True | R_stab<=d_inf<=d True
     min-wt witnesses 579/579 contiguous & span<=weight | spans/R [[1],[1,2],[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
rotated-surface-d3 :: ZZ-order, interleaved (hook-misaligned)
  Z-memory (X-sector)      d_R=[3,3,3,3,3,3]  d_inf=3 R_stab=1  | 2184/2184 | 579/579
  X-memory (Z-sector)      d_R=[2,2,2,2,2,2]  d_inf=2 R_stab=1  | 2184/2184 |  72/72
rotated-surface-d3 :: ZN-order, non-interleaved (X-block first)
  Z-memory (X-sector)      d_R=[3,3,3,3,3,3]  d_inf=3 R_stab=1  | 3612/3612 | 579/579
  X-memory (Z-sector)      d_R=[3,3,3,3,3,3]  d_inf=3 R_stab=1  | 3612/3612 | 579/579
rotated-surface-d3 :: NZ-order, interleaved
  Z-memory (X-sector)      d_R=[2,2,2,2,2,2]  d_inf=2 R_stab=1  | 2184/2184 |  72/72
  X-memory (Z-sector)      d_R=[2,2,2,2,2,2]  d_inf=2 R_stab=1  | 2184/2184 |  72/72
steane-713 :: non-interleaved, index order (T=12)
  Z-memory (X-sector)      d_R=[2,2,2,2,2,2]  d_inf=2 R_stab=1  | 3969/3969 |  72/72
  X-memory (Z-sector)      d_R=[2,2,2,2,2,2]  d_inf=2 R_stab=1  | 3969/3969 |  72/72
steane-713 :: non-interleaved, reversed Z order (T=11)
  Z-memory (X-sector)      d_R=[2,2,2,2,2,2]  d_inf=2 R_stab=1  | 3696/3696 |  72/72
  X-memory (Z-sector)      d_R=[2,2,2,2,2,2]  d_inf=2 R_stab=1  | 3696/3696 |  72/72

AGGREGATE over 12 (schedule, sector) instances:
  time-locality columns verified : 35658/35658      (Lemma 2.5)
  monotone d_{R+1} <= d_R        : 12/12            (Theorem 3.1)
  d_R constant for R >= d        : 12/12            (Theorem 5.1(2))
  R_stab <= d_inf <= d           : 12/12            (Theorem 5.1(3))
  min-wt witnesses contiguous    : 3399/3399        (Theorem 4.1)
  R_stab values observed         : [1]
  d_inf values observed          : [2, 3]
```

Note the span histograms: at `d_∞ = 3` the observed spans reach exactly `3` once `R ≥ 3`, and at
`d_∞ = 2` they reach exactly `2` — i.e. the bound `w ≤ |F|` of Theorem 4.1 is **attained**, so it
cannot be improved to `w ≤ |F| − 1`.

### 7.2 Direction-order sweep (surface `d = 3`, interleaved, `R = 1..5`)

Scope: **all 576** ordered pairs (X-check corner order, Z-check corner order) drawn from the 24
permutations of `(NW, NE, SW, SE)`, giving depth-4 interleaved schedules; filtered by legality and
(MC) as computed from Definitions 1.4–1.5.

```
direction-order pairs enumerated         : 576
legal AND measurement-consistent         : 16   (=> 32 (schedule,sector) instances)
monotone d_{R+1}<=d_R                    : 32/32
d_R constant for R >= d=3                : 32/32
R_stab <= d_inf <= d                     : 32/32
min-weight witnesses contiguous, span<=w : 7088/7088
distinct d_R sequences (R=1..5)          : {(2,2,2,2,2): 16, (3,3,3,3,3): 16}
R_stab values observed                   : [1]
d_inf values observed                    : [2, 3]
```

### 7.3 Targeted certification of the three load-bearing lemmas

```
Lemma 2.8  (W) <=> undetectable, random weight-1..4 subsets : 16000/16000
Lemma 2.12 explicit terminal weight-d_X witness closes      :    40/40
Lemma 4.3  min-wt witness translates into C_w and re-closes :  1772/1772
```
Scope: 8 (schedule, sector) instances, `R ∈ {1,…,5}`, seed `20260822`; `d_X` recomputed
independently by brute force over `ker H_Z ∖ rowspace(H_X)` (`= 3` in all instances). Lemma 4.3's
check translates each minimum-weight witness down to `C_w` with `w` its own round span and
re-verifies undetectability and observable-flipping by direct simulation.

### 7.4 Independent cross-check with Stim (upper bound)

```
rotated_memory_z d=3  R=1..10 : [3,3,3,3,3,3,3,3,3,3]  monotone=True  constant-from-R=d=True
rotated_memory_z d=5  R=1..10 : [5,5,5,5,5,5,5,5,5,5]  monotone=True  constant-from-R=d=True
rotated_memory_z d=7  R=1..10 : [7,7,7,7,7,7,7,7,7,7]  monotone=True  constant-from-R=d=True
stim 1.16.0
```
`stim.Circuit.shortest_graphlike_error` returns an **upper** bound on `d_circ` in general (it is
exact only within the graph-like restriction); this arm is corroboration of monotonicity and
constancy at `d = 5, 7`, where the exhaustive search of §7.1 is out of reach, and nothing more.

### 7.5 The absence claim, fenced

> **NUMERICAL, absence-type.** Across the **44** (schedule, sector) instances of §7.1–§7.2 — two
> code families, `d = 3`, depths `T ∈ {4, 11, 12}`, interleaved and non-interleaved, both CSS
> sectors, `R` up to `6` — **no instance with `R_stab ≥ 2` was found**; every observed `R_stab` is
> `1`. Together with the 7 610-schedule scan reported in
> `artifacts/circdist_sat_recon_20260820.md` §7 (rotated surface `d = 3`, Steane `[[7,1,3]]`, Shor
> `[[9,1,3]]`, depths `T ∈ {4,5,6,8,10}`, `R` up to `8`), which likewise found no non-constant
> `d_R` sequence, this is the total evidence available.

**This is absence evidence within a stated search scope, and it is not a theorem.** It is
**not used** in any step of §2–§5, and no step of §2–§5 asserts, implies, or requires
`R_stab(M) = 1`. Theorem 5.1 bounds `R_stab ≤ d_∞` and is fully compatible with `R_stab ≥ 2`
existing. Note also that the scope is structurally weak for this particular question: all instances
have `d = 3`, which by Theorem 5.1(3) already forces `R_stab ≤ 3`, so the search has almost no room
to exhibit a large `R_stab`. Deciding sub-claim **W-OPEN** (§8) requires `d ≥ 5`.

### 7.6 Reproduction

Scripts written to this session's scratchpad; **no repository file other than this artifact was
created or modified**. Python 3.9.6, `stim 1.16.0` (already present in the environment).

```
<scratchpad>/window.py    # model, direct simulator, distance search; §7.1 aggregate   (~2 s)
<scratchpad>/sweep.py     # 576 direction-order pairs, legality+MC filter; §7.2        (~5 s)
<scratchpad>/lemmas.py    # targeted certification of 2.8 / 2.12 / 4.3; §7.3           (~4 s)
<scratchpad>/stimarm.py   # Stim cross-check d=3,5,7, R=1..10; §7.4                    (<1 s)
```

Run order: `window.py`, then `sweep.py` and `lemmas.py` (both import `window.py` from the working
directory), then `stimarm.py`.

**The one thing to re-derive before trusting any of §7:** Lemma 2.4 (round transparency). Every
numerical result above inherits its correctness through the simulator's propagation rule, and it is
the cheapest thing to get subtly wrong.

---

## 8. Residual gaps, as precise sub-claims

The Theorem's three parts are derived above; these are the statements this document **assumes,
inherits, or leaves open**, each written so it can become its own DAG node.

**W-G1 (inherited convention — sector aggregation).**
> `d_circ(C(M))` of 公共定义 equals `min( d_circ(C^Z_R(M)), d_circ(C^X_R(M)) )`, i.e. the memory
> experiment's circuit distance is the minimum over the two initialisation/readout bases.

Used only in the aggregation step of S4/5.1. Everything in §3–§5 is proved **per sector** and is
unaffected if a reviewer prefers a different aggregation: replace `min` by whichever aggregation is
adopted, and (i)–(iii) survive verbatim provided the aggregation is monotone in each argument. This
is a definitional inheritance, not a mathematical gap, but it must be named because the theorem's
statement quantifies over it.

**W-G2 (scope clause S2 — round-translation covariance).**
> For `C_R(M)` formed as `R` verbatim repetitions of the `T`-step block `M`, the elementary fault
> locations of round `r` are in `(E,s,u,λ)`-preserving bijection with those of round `r'`, for all
> `r, r' ∈ {0,…,R−1}` and all `R`.

Asserted in S2 and consumed by 2.3, 3.1 and 4.3. It is immediate for the verbatim layout, but it is
**false** for a layout that compresses idle layers across round boundaries. A reviewer who reads
公共定义's idle-layer compression as applying to the concatenated circuit rather than to `M` will
find (i)–(iii) unproved for that layout. *Minimal fix if challenged:* state 1.7 as the definition
of `C_R(M)` (this document does) and record cross-round compression as a distinct, unaddressed
model.

**W-G3 (scope clause S3 — maximality of the detector set).**
> The `F₂`-span of `{ D_{b,r} : b ∈ ℬ, r ∈ {0,…,R} } ∪ { D_{a,r} : a ∈ 𝒜, r ∈ {1,…,R−1} }` is the
> full space of deterministic parities of the recorded outcomes and the ideal readout bits of
> `C_R(M)`.

Not derived here. Standing fact 1.6 shows every listed parity **is** deterministic; the converse
(that there are no others) is asserted as the standard convention. If false, the true `d_circ`
could be smaller than the `d_R` computed here, and each of (i)–(iii) would have to be re-checked
against the larger detector set. *This is the cheapest remaining formal hole in the document.*

**W-G4 (tightness of the bound `R_stab ≤ d_∞`).**
> Is `R_stab(M) ≤ d_∞(M)` attained? I.e. does there exist `(Q,M)` in scope with
> `R_stab(M) = d_∞(M) ≥ 2`?

Theorem 5.1(3) gives the inequality; nothing here says it is tight. §7 cannot address it (all
instances have `R_stab = 1`).

**W-OPEN (the sharpest open sub-question of this node).**
> Does there exist a CSS code `Q` with `k ≥ 1` and a legal, measurement-consistent single-ancilla
> schedule `M` with `R_stab(M) ≥ 2`, equivalently with `d_2(M) < d_1(M)`?

**Status: OPEN.** The window theorem is *silent* on this: it is consistent with `R_stab ≡ 1` and
with `R_stab` taking every value in `[1, d]`. The only evidence is absence-type and confined to
`d = 3` (§7.5), where Theorem 5.1(3) itself caps `R_stab ≤ 3`. A decisive experiment needs `d ≥ 5`,
where the exhaustive weight-`≤4` search of §7 is no longer sufficient and a weight-capped Dijkstra
over the one-round dictionary is required. **This document must not be read as evidence either
way.**

**Epistemic residual (not a mathematical gap).** Every statement here is labelled CONJECTURED with
a derivation status; none has been independently reviewed. Rule 6 requires an independent
claim-level review before `CIRCDIST.sat.window` may carry a completion level, and §6.4(2) explains
why the existing lift-side review cannot be transferred.

---

## 9. One-paragraph summary for the assembly node

For every legal, measurement-consistent, single-round, single-ancilla CSS schedule `M`, under the
frozen ideal-boundary memory model and per CSS sector: appending (or prepending) a fault-free round
carries any undetectable logical witness across unchanged, because the terminal detector of the
shorter circuit already forces the accumulated residual syndrome to vanish — so `d_R` never rises
(§3). A fault-free round strictly inside a minimum-weight witness would force the accumulated
syndrome to vanish there too, splitting the witness into two independently undetectable halves of
which one is still logical and strictly lighter — impossible at minimum weight, so minimum-weight
witnesses occupy contiguous rounds and span at most their own weight, which is at most `d` (§4).
Contiguity plus free time translation then pushes every witness into a `d`-round circuit, giving
`d_∞ = d_d`, `R_stab ≤ d_∞ ≤ d`, and a decision procedure that halts at the first `R` with
`R ≥ d_R` (§5). The window is `B(r,d) = d`, with **no dependence on the cross-round state-space
dimension `r`**. What remains open is not the window but its interior: whether any schedule in this
class has `R_stab ≥ 2` at all (§8, W-OPEN).
