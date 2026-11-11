# CIRCDIST.lift — recon session report (Opus 5 executor, proposer role)

**Date:** 2026-08-20 · **Node:** `CIRCDIST.lift` · **Frontier item:** `task-001` (route registration)
**Session type:** one budget-boxed recon under stop-loss. No open-ended proving attempted.
**Epistemic ceiling for this document: nothing here is labelled PROVED.** The one concrete result
is labelled **NUMERICAL**; all framework statements are labelled **CONJECTURED** or **OBSERVATION**.

---

## 0. Executive summary

1. **The decisive gate was identified, and then it fired inside this session.** An explicit
   interleaved single-ancilla CSS syndrome-extraction circuit with `d_circ > d_eff` now exists:
   `[[4,2,2]]`, 4 data qubits, 2 ancillas, depth 5, `d_eff = 1`, `d_circ = 2`. A non-interleaved
   circuit with **the same within-check CNOT orders** (hence the same residual set and the same
   `d_eff`) has `d_circ = 1`. Exhaustive weight-1 and weight-2 enumeration, stable for
   `R = 2,3,4,5` rounds. This discharges the "至少一个交错严格不等号例子" half of the node's
   minimum acceptance condition, modulo an independent re-derivation of the fault-location model.
2. **The lifting obstruction was observed in its purest possible form.** The distance-reducing hook
   fault, which in the non-interleaved circuit triggers *no* detector, in the interleaved circuit
   triggers exactly two detectors: the **same** Z-check in **two consecutive rounds**. That is a
   purely timelike ("vertical") edge — an effective logical whose lift has net time-voltage 1 and
   therefore cannot close. Adding one measurement-flip fault on that same check cancels it exactly,
   producing a weight-2 closed lift. This is the conjectured
   `d_circ = |γ| + (voltage repair cost)` formula, realised concretely.
3. **A rigorous algebraic frame for the whole problem is available and is cheap.** The spacetime
   detector complex is the effective complex base-changed to the group ring `F₂[Z] = F₂[x,x⁻¹]` of
   the time-translation deck group; `π₀` is the **augmentation** `x ↦ 1`; and the chain-map
   property is a one-line telescoping identity. This yields the easy direction `d_eff ≤ d_circ`
   immediately and turns "closed lift" into a divisibility condition in a Laurent polynomial ring
   (§3.4). Route `laurent-group-ring` is the recommended primary attack.
4. **Load-bearing prior work exists and is very recent.** The `d_ext`/extended-code definition, the
   non-interleaved equality theorem, and the gross-code `≤ 11` bound are all in
   **arXiv:2603.05481** (Strikis, Browne, Beverland, Mar 2026). Its Theorem 1 contains the clause
   `d'_circ ≤ d_circ` ("interleaving cannot decrease the circuit distance"). Our example shows that
   inequality is **strict** for an explicit circuit — which appears to be new.
5. **Scheduling consequence the dispatcher should see:** `CIRCDIST.lift` and `CIRCDIST.gross` are
   **not value-disjoint**. Strikis et al. prove every non-interleaved gross-code circuit has
   `d_circ ≤ 11`; so a distance-12 gross circuit can only exist via exactly the interleaving gap
   this node studies. Quantifying `g(C)` for weight-6 checks is the direct theoretical input to
   `CIRCDIST.gross`. Round-1's "four disjoint subtrees" assumption is safe for *commit* purposes
   but wrong for *value* purposes.

---

## 1. Setup and notation (fixed for the rest of the document)

Ground model as in the commission's 公共定义, plus the following explicit choices. Deviations from
these choices are flagged in §7 as modelling assumptions.

- CSS code `Q = [[n,k,d]]` with check matrices `H_X`, `H_Z`; one dedicated ancilla per stabilizer
  generator, prepared once and measured once, one CNOT per data qubit in the generator's support.
- `M` = schedule (an assignment of time steps to CNOTs, one two-qubit gate per qubit per step).
- `C_R(M)` = memory experiment: ideal data initialisation, `R` identical rounds of `M`, ideal
  transversal final data readout.
- **Detectors.** For check `g` and round `r`: `D_{g,r} = m_{g,r} + m_{g,r-1}` (with `m_{g,0}` the
  deterministic initial value where the initialisation basis makes it deterministic), plus terminal
  detectors comparing the last round's outcomes to the checks recomputed from the ideal readout.
- **Elementary fault** = one Pauli inserted at one circuit location (2-qubit Pauli after a CNOT,
  1-qubit Pauli after a prep or on an idle qubit) or one classical measurement-outcome flip.
  `|F|` = number of elementary faults.
- `d_circ(C) = min{ |F| : F triggers no detector and flips a logical observable }`.
- `d_eff(M) = d_ext(E(M))`, the extended-code distance built from the terminal residual (hook)
  errors of single faults (arXiv:2603.05481 Defs. 1–3).

**Per-fault data.** For an elementary fault `i` occurring inside round `r`, define three objects:

| symbol | meaning | lives in |
|---|---|---|
| `s_i` | terminal syndrome of the residual data error `E_i` left by the fault | `F₂^{checks}` |
| `u_i` | set of checks whose **round-`r`** measurement outcome the fault flips | `F₂^{checks}` |
| `λ_i` | logical action of `E_i` on the tracked observables | `F₂^k` |

**OBSERVATION 1.1 (locality in time).** An elementary fault in round `r` can only affect detectors
of rounds `r` and `r+1`. *Reason:* the residual `E_i` sits on the data at the start of round `r+1`
and is measured in full by every subsequent round, so it cancels in every later
`D_{g,r'} = m_{g,r'} + m_{g,r'-1}` with `r' ≥ r+2`. Explicitly

```
∂_circ( fault i placed in round r )  =  [u_i]_r  +  [u_i + s_i]_{r+1}.
```

**OBSERVATION 1.2 (edge taxonomy).** In a graphlike model (`|u_i| + |u_i + s_i| ≤ 2`) every fault
is one of:

| type | condition | picture | time-voltage |
|---|---|---|---|
| horizontal-early | `u_i = s_i` | both endpoints in round `r` | 0 |
| horizontal-late | `u_i = 0` | both endpoints in round `r+1` | 0 |
| diagonal | `u_i ∉ {0, s_i}`, `s_i ≠ 0` | one endpoint each in `r`, `r+1` | ±1 |
| vertical | `s_i = 0`, `u_i ≠ 0` | `(g,r)—(g,r+1)`, same check | ±1 |

Horizontal-early in round `r` and horizontal-late in round `r-1` are the *same* spacetime edge;
both project to a genuine edge of `G_eff`. Vertical edges project to a **loop** (trivial base image)
— and, crucially, a vertical edge can still carry `λ_i ≠ 0`. §4 shows that is exactly what happens
in the minimal counterexample.

---

## 2. What is and is not already known (literature, with honesty flags)

**arXiv:2603.05481** — Strikis, Browne, Beverland, *High-performance syndrome extraction circuits
for quantum codes*, Mar 2026. **[VERIFIED: abstract and HTML full text fetched this session.]**
This is the paper the commission's definitions come from.

- Def. 1–3: residual errors `ℰ_Z,j`, extended matrices `H_X^ext(ℛ), L_X^ext(ℛ)`, and
  `d_ext^Z(ℛ)` = min weight `x` with `H_X^ext x^T = 0`, `L_X^ext x^T ≠ 0`.
- **Prop. 3:** `d_circ ≥ d_ext(ℰ)` for any single-ancilla CNOT-based SEC. (Direction re-verified
  twice by the literature agent.) So the hook-only analysis is a *lower* bound; intermediate-time
  detectors can only *raise* the true circuit distance.
- **Thm. 1 / Cor. 1:** for a single-ancilla, CNOT-based, CSS, **non-interleaved** SEC `C'` obtained
  from `C` by preserving the relative CNOT ordering *within each check*:
  `d'_circ = d_ext(ℰ)`, and `d'_circ ≤ d_circ` — glossed in that paper as "interleaving cannot
  decrease the circuit distance".
- **Prop. 4:** every non-interleaved SEC for the gross code has `d_circ ≤ 11`; an explicit depth-8
  non-uniform left–right circuit is *conjectured* (not proved) to reach 11.

**Two consequences that reframe this node.**

- **CONSEQUENCE 2.1.** Because the residual set `ℰ` depends only on the **within-check** CNOT
  orders, `d_eff(M)` is an invariant of the within-check orders alone. **The entire completion gap
  `g(C) = d_circ − d_eff` is a function of the interleaving pattern**, with the within-check orders
  held fixed. This is the right way to slice the problem and it is what the §4 example exploits.
- **CONSEQUENCE 2.2.** The commission's target theorem is the *quantitative refinement* of
  Strikis et al. Thm. 1's fourth clause. They prove `d'_circ ≤ d_circ`; the node asks for the
  structural criterion deciding when the inequality is strict, and by how much.

**Literature agent's negative findings, worth recording so they are not re-searched.**

- Manes & Claes (arXiv:2308.15520) do **not** define the extended code; their Thm. 2 is an
  effective-distance-preservation result for HGP codes under a no-data-spreading fault model.
  **[id/authors/abstract VERIFIED; theorem wording MEDIUM confidence — both PDFs unparseable.]**
- The Stim paper (arXiv:2103.02202) does **not** formally define "detector error model",
  "graphlike error", or "circuit distance"; only an informal detector note in §5.6. For a citable
  formal DEM treatment use **arXiv:2407.13826** (Derks, Townsend-Teague, Burchards, Eisert).
  **[VERIFIED.]**
- Delfosse & Paetznick, *Spacetime codes of Clifford circuits* (**arXiv:2304.05943**) does **not**
  define fault distance. **[VERIFIED full text.]** For a chain-complex spacetime formalism that
  *does* handle fault distance, use **arXiv:2509.09603** (Pesah, Daniel, Tzitrin, Vasmer,
  *Fault-tolerant transformations of spacetime codes*) — "fault-tolerant maps … preserve the number
  of encoded qubits, fault distance, and minimum-weight decoding problem". **[abstract VERIFIED.]**
- Gottesman *Opportunities and Challenges in Fault-Tolerant Quantum Computation* is
  **arXiv:2210.15844**, not 0904.2557. **[VERIFIED.]**
- **arXiv:2603.01628** (Hirai, Ikari, Ueno, Suzuki) uses ZX **interleaving** to *restore* full fault
  distance `d` in surface codes at depth 4 — empirical evidence, from the opposite direction, that
  interleaving buys strictly positive `g(C)`. **[abstract VERIFIED.]**
- No paper found that exhibits an explicit interleaved circuit with `d_circ > d_ext(ℰ)`.
  **[MEDIUM confidence on exhaustiveness of the search.]**

---

## 3. Framework sketch developed this session

All of §3 is **CONJECTURED**: the derivations are short and I believe them, but definitions at the
temporal and logical boundaries are not yet pinned down and no independent review has occurred.

### 3.1 The projection, defined

Let `C_1(circ) = F₂^{(fault type) × (round)}`, `C_0(circ) = F₂^{detectors}`, `∂_circ` the detector
incidence map. Let `C_1(eff) = F₂^{fault types}`, `C_0(eff) = F₂^{checks}`, `∂_eff = ` terminal
syndrome map `i ↦ s_i`. Define

- `π_1 : C_1(circ) → C_1(eff)`, `(i,r) ↦ i` — **fiber collapse**, weight non-increasing;
- `π_0 : C_0(circ) → C_0(eff)`, `(g,r) ↦ g` — **fiber sum**.

**CONJECTURED 3.1 (telescoping / chain-map property).** `π_0 ∘ ∂_circ = ∂_eff ∘ π_1`.
*Proof sketch.* By Obs. 1.1, `π_0 ∂_circ (i,r) = u_i + (u_i + s_i) = s_i = ∂_eff π_1 (i,r)`. ∎
The intermediate-time detectors are exactly the part of `C_0(circ)` that `π_0` telescopes away, so
"delete the intermediate detectors" and "sum over the time fiber" define the *same* map — which is
why the effective model is a chain-level quotient rather than an ad-hoc truncation.

**CONJECTURED 3.2 (easy direction).** `d_eff ≤ d_circ`.
*Proof sketch.* If `F` triggers no detector and flips a logical, then `∂_circ F = 0`, so
`∂_eff π_1 F = π_0 ∂_circ F = 0`; the tracked observable is read at the end, so
`λ_eff(π_1 F) = λ_circ(F) ≠ 0`; and `|π_1 F| ≤ |F|`. ∎ (This reproves Strikis et al. Prop. 3 in
chain-map language; the point is that it is now a *formal consequence of a chain map*, which is
what the node's technical requirement 3 asks for.)

**CONJECTURED 3.3 (lift formula — the target theorem's shape).**
`d_circ = min_{γ ∈ L_eff} ℓ(γ)`, where `L_eff` = nontrivial effective logical cycles and
`ℓ(γ) = min{ |f| : f ∈ ker ∂_circ, π_1 f = γ }` (`+∞` if none). Consequently
`d_circ = d_eff ⟺ some minimum-weight γ admits a closed lift of the same weight.`

⚠ **Sharpening the acceptance bar.** As stated, 3.3 is close to a tautology: it merely renames
"undetectable" as "closed lift". The scientific content the node requires is that `ℓ(γ) − |γ|` be
computed from an **intrinsic invariant of `M`** — the voltage — *without* constructing `C_R(M)`.
Any future session that produces 3.3 alone should not claim progress. This is the single most
important scoping judgement of this recon.

### 3.2 Voltage, and why the naive cohomological criterion is wrong

Assign to each oriented base edge the time displacement `α(e) ∈ {−1,0,+1}` of Obs. 1.2. The bulk of
`G_circ` is then the Gross–Tucker **derived graph** `G_eff^α` for the voltage group `Γ = Z`
(time translation), and the covering-space slogan applies: *a closed walk lifts to a closed walk iff
its net voltage is the identity.*

**OBSERVATION 3.4 (negative — kills the obvious formulation).** The criterion **cannot** be
"`[α] = 0` in `H¹(G_eff; Z)`", i.e. "`α` is a coboundary". Bare data errors realise every base edge
of the code's own Tanner-derived graph at voltage 0, which forces any potential `τ` to be constant
on a connected `G_eff`; but hook edges are genuinely diagonal, so `α ≠ δτ` whenever any hook edge
exists — which is essentially always. **The criterion is therefore necessarily a *pairing*
condition** — `α` evaluated on a *specific* minimum-weight logical class — not a global exactness
condition. Any route that starts from "trivialise the voltage cocycle" is dead on arrival.

**OBSERVATION 3.5 (the F₂/Z mismatch is the technical crux).** `γ` is an `F₂` cycle (an unoriented
fault *set*); `α` is `Z`-valued and orientation-sensitive. `⟨α, γ⟩` is therefore not well defined.
Two repairs, both must be evaluated by a future session:
 (a) reduce mod 2 — `α ∈ H¹(G_eff; F₂)`, giving a well-defined but only *necessary* condition
     (the double cover);
 (b) keep `Z` and define `V(γ) = { net voltage of γ̃ : γ̃ an Eulerian orientation of γ }`, so that
     `γ` lifts closed iff `0 ∈ V(γ)`. Every `F₂` cycle has even degree at every vertex, so Eulerian
     orientations exist; the non-uniqueness at degree-`≥4` vertices is exactly the freedom to pair
     up incident lifted edges differently. The correct combinatorial statement is then
     **"`γ` decomposes into closed walks each of net voltage 0"**, which smells like a flow /
     T-join feasibility problem and is the natural home for the requested equality-decision
     algorithm.

### 3.3 Covering, branched covering, or chain map (node technical requirement 2)

**CONJECTURED 3.6.** For the bi-infinite repeated circuit, `π` restricted to non-boundary vertices
is an honest covering projection onto `G_eff` with deck group `Z`. It fails to be a covering in
exactly two places, which are exactly the node's requirement 5:
 - the **temporal boundary** (initialisation round and ideal-readout round): degrees are deficient,
   so `π` is a covering *of a graph with boundary*. If one compactifies by identifying all temporal
   boundary detectors to a single vertex, that vertex becomes a **branch point** with full fiber —
   this is the honest sense in which "branched covering" is the right word;
 - the **logical/detector boundary** of `G_eff` (open boundaries of the code, where an error
   triggers one detector rather than two): dangling edges, whose lifts have a free endpoint and
   therefore *free voltage*. **Boundary edges are voltage sinks**: a cycle that reaches the
   boundary can dump arbitrary voltage there at no extra cost. Any correct iff must quantify this,
   and it is the most likely place for a clean criterion to break.
 - Away from both, `π` is a local isomorphism on stars, and everywhere it is a **weight-preserving
   chain map** (3.1). The three regimes therefore stratify cleanly.

### 3.4 The group-ring / Laurent formulation (recommended primary frame)

Because the bulk circuit is time-translation invariant, `C_•(circ)` is a module over
`F₂[Z] = F₂[x, x⁻¹]` with `x` = one-round time shift, and Obs. 1.1 reads

```
∂_circ ( fault i in round r )  =  x^r · ( u_i (1+x) + s_i x ).
```

`π_0` is the **augmentation** `ε : F₂[x,x⁻¹] → F₂`, `x ↦ 1`; then `ε(u_i(1+x) + s_i x) = s_i`,
recovering 3.1 in one line. Now fix an effective logical `γ = {i_1,…,i_w}` with `Σ s_i = 0`,
`Σ λ_i ≠ 0`, and choose rounds `r_i`. Put

```
A(x) = Σ_i u_i x^{r_i},      B(x) = Σ_i s_i x^{r_i}.
```

Since `B(1) = Σ s_i = 0`, we may write `B(x) = (1+x) C(x)` with `C ∈ F₂[x,x⁻¹]^{checks}`, and the
total detector chain is `(1+x)·( A(x) + x C(x) )`. As `F₂[x,x⁻¹]` is an integral domain:

**CONJECTURED 3.7 (closed-lift criterion, algebraic form).**
`γ` with round assignment `(r_i)` lifts closed **iff** `A(x) = x · C(x)`.
In particular, if all faults are placed in the same round then `C = 0` and the criterion collapses
to the strikingly simple

**CONJECTURED 3.8 (same-round criterion).** `Σ_{i ∈ γ} u_i = 0`.

This is the concrete, computable "voltage" the node is asking for: **`u` is the voltage, and the
obstruction lives in the augmentation ideal `(1+x)`.** It is manifestly `F₂`-valued (dodging Obs.
3.5's orientation problem entirely), manifestly computable from one round of the schedule, and it
specialises correctly (§4 verifies it on the counterexample). Its weakness is that 3.8 covers only
same-round lifts; the general multi-round case 3.7 is a divisibility problem whose min-weight
version needs a finite-window argument — **which is exactly the pumping theorem `CIRCDIST.sat` is
commissioned to prove.** That shared premise is the second cross-root coupling found this session.

### 3.5 Why non-interleaved gives equality — the mechanism

**CONJECTURED 3.9.** In a non-interleaved CSS schedule (all X-check CNOTs in one block, all
Z-check CNOTs in the other), every effective fault type has a **horizontal** representative of the
same weight, i.e. `u ∈ {0, s}` is achievable. Sketch, by CNOT propagation:
`Z` on an X-check ancilla (control) does not propagate to data (it is a pure measurement error);
`X` on an X-check ancilla propagates `X` onto the untouched data qubits, and since **all** Z-check
CNOTs lie in the other block, that residual is seen by *every* Z-check in the same round →
`u = s`. Symmetrically, `Z` on a Z-check ancilla (target) propagates `Z` onto untouched data, and
since all X-check CNOTs are already done, `u = 0`. Bare data errors always admit a start-of-round
(`u = s`) and an end-of-round (`u = 0`) weight-1 representative. Hence `α` restricted to the
cheapest representatives is exact, the derived graph splits into `R` disjoint copies of `G_eff`,
every effective logical lifts in a single round, and `d_circ ≤ d_eff`; with 3.2, equality. ∎(sketch)

This is an independent route to Strikis et al. Cor. 1 *from the covering picture*, which is what
the node's requirement 6 demands. It also predicts precisely where interleaving breaks it: a hook
created while **some** opposite-type checks have already finished their CNOTs on the affected
qubits and others have not. §4 is that prediction, instantiated.

---

## 4. NUMERICAL result — minimal interleaved circuit with `d_circ > d_eff`

**Label: NUMERICAL.** Exhaustive enumeration over an explicitly specified elementary-fault-location
set, in an independently written `F₂` Pauli-propagation simulator (no Stim in this environment;
`stim`, `pymatching`, `ldpc`, `galois`, `networkx` are all absent — only `numpy`, `scipy`, `sympy`).
The computation is small enough to be re-checked by hand, and §4.4 gives the hand argument.
It is **not** labelled PROVED: the fault-location set is a modelling choice and no independent
implementation has reproduced it.

### 4.1 The circuit

Code `[[4,2,2]]`: stabilizers `X₀X₁X₂X₃`, `Z₀Z₁Z₂Z₃`; Z-logicals `Z₀Z₁`, `Z₀Z₂`.
Register: data `q₀..q₃`; X-ancilla `a` (prep `|+⟩`, measured in X, CNOT control);
Z-ancilla `b` (prep `|0⟩`, measured in Z, CNOT target).

Within-check CNOT orders (**identical in both schedules**, so both have the same residual set `ℰ`
and the same `d_eff` — Consequence 2.1):
X-check touches `q₀,q₁,q₂,q₃`; Z-check touches `q₂,q₀,q₁,q₃`.

```
INTERLEAVED  (depth 5)                 NON-INTERLEAVED  (depth 8)
 t1:  CX a→q₀                           t1..t4:  CX a→q₀ , a→q₁ , a→q₂ , a→q₃
 t2:  CX a→q₁ ,  CX q₂→b                t5..t8:  CX q₂→b , q₀→b , q₁→b , q₃→b
 t3:  CX a→q₂ ,  CX q₀→b
 t4:  CX a→q₃ ,  CX q₁→b
 t5:                CX q₃→b
```
Both are legal (one two-qubit gate per qubit per step). Memory experiment: data prepared `|0000⟩`,
`R` rounds, ideal final `Z` readout. Detectors: `D_{b,r}` for `r ≥ 1` (`r=1` against the
deterministic `+1` value of `ZZZZ`), `D_{a,r}` for `r ≥ 2` (the first X outcome is random), and a
terminal detector comparing `Z₀Z₁Z₂Z₃` recomputed from the ideal readout against `m_{b,R}`.
Observables: `Z₀Z₁` and `Z₀Z₂`.

### 4.2 Results

Terminal residual set (identical for both schedules):
`ℰ = { ∅, X₀, X₁, X₂, X₃, X₂X₃, X₁X₂X₃, X₀X₁X₂X₃ }`.

**`d_eff = 1` for both.** Witness residual `X₂X₃` — even overlap with `Z₀Z₁Z₂Z₃` (trivial syndrome),
odd overlap with `Z₀Z₂` (nontrivial logical). It arises from a single `X` fault on ancilla `a`
immediately after `a`'s second CNOT. Note every CNOT order on a weight-4 check has such a halfway
point, so `d_eff([[4,2,2]]) = 1` for *every* schedule — the code has no hook-safe ordering.

| schedule | `d_eff` | `d_circ` | gap `g` |
|---|---|---|---|
| non-interleaved | 1 | **1** (10 distinct weight-1 undetectable logicals) | 0 |
| interleaved | 1 | **2** (no weight-1 undetectable logical; explicit weight-2 one) | **1** |

Stable for `R = 2, 3, 4, 5`. `d_circ = 2` is exact, not just a lower bound, because `d_circ ≤ d = 2`
always and a weight-2 witness was found explicitly.

### 4.3 The mechanism, observed directly

The same hook fault (X on `a` after its 2nd CNOT; residual `X₂X₃`; `s = 0`, `λ ≠ 0`) behaves as:

```
NON-INTERLEAVED :  detectors fired = { }                    logical flipped = yes   →  d_circ = 1
INTERLEAVED     :  detectors fired = { (b, r), (b, r+1) }   logical flipped = yes   →  detected
```

In the interleaved circuit `b` has already consumed `q₂` (at `t2`, before the fault) but not yet
`q₃` (at `t5`, after), so the residual flips `b`'s round-`r` outcome exactly once: `u = {b}`,
`s = 0`. By Obs. 1.2 this is a **vertical edge** — its base image in `G_eff` is a loop, its lift has
net voltage 1, and it cannot close. In the non-interleaved circuit `b` consumes both `q₂` and `q₃`
after the fault, so `u = s = 0`: no detector at all — precisely Conjecture 3.9's dichotomy.

**Voltage repair, verified.** Hook fault ⊕ one classical measurement-flip of `b` in the same round:
detector sets `{(b,r),(b,r+1)}` and `{(b,r),(b,r+1)}` cancel exactly, logical survives. Weight 2,
closed. So `ℓ(γ) = |γ| + 1` here, and `g(C) = 1` is *the cost of cancelling one unit of voltage* —
the conjectured `d_circ = min_γ ( |γ| + repair cost )` formula in its smallest instance.

### 4.4 Hand-checkable core

No simulator is needed for the essential claim. `X` on `a` after its second CNOT propagates `X` to
`q₂` (at `t3`) and `q₃` (at `t4`). `Z`-check `b` has CNOT order `q₂,q₀,q₁,q₃` at steps
`t2,t3,t4,t5`. Its `q₂` gate is at `t2` < fault, so the `X` on `q₂` is invisible to `b` this round;
its `q₃` gate is at `t5` > fault, so the `X` on `q₃` flips `b` once. Hence `b`'s round-`r` outcome
flips, and since `X₂X₃` commutes with `Z₀Z₁Z₂Z₃`, `b`'s round-`(r+1)` outcome flips too. Two
detectors. In the non-interleaved circuit both `b` gates are after the fault, so `b` flips twice in
round `r` and not at all in round `r+1`: zero detectors, `d_circ = 1`.

### 4.5 Robustness sweep

X-order fixed to `q₀,q₁,q₂,q₃`; interleaving template "Z lags X by one step"; all 24 Z-orders, of
which **11 are legal** under the one-gate-per-qubit-per-step rule (13 collide and are discarded):

- **8 of 11** legal Z-orders give `g = 1`;
- **3 of 11** give `g = 0`.

So the gap is generic under interleaving, not a fine-tuned coincidence — and the equality cases show
the criterion has content in both directions (there really is something to characterise).

### 4.6 Honest limitations

1. `d = 2`, so `g ≤ 1` is forced; the example cannot exhibit a large gap. A `d = 3` example
   (rotated surface code or Steane) is the publishable version and is the next gate (§5).
2. `[[4,2,2]]` is a detection code and `d_eff = 1` for every schedule, so a referee may object that
   the "effective logical" being killed is degenerate. The mechanism (§4.3) is not degenerate, but
   the instance is small.
3. The fault-location set is mine, not Stim's. Reproduction with `stim.Circuit.search_for_
   undetectable_logical_errors` is a cheap independent check and should be run before anything is
   promoted.
4. `d_circ = 2` was established by exhaustive weight-≤2 search; the weight-1 exhaustion is the
   load-bearing half and is the part the hand argument in §4.4 covers only for the single hook
   fault, not for all 522 mechanisms.

**Reproduction.** Scratch scripts `d422.py`, `d422b.py`, `d422c.py` (F₂ symplectic propagation,
~200 lines, stdlib only). They live in this session's scratchpad, not in the repository; a future
session should re-implement rather than trust them, or re-derive under Stim.

---

## 5. Registered routes

Six routes. `P` = probability the route's implication eventually closes; `D` = expected sessions to
the next evidence level or decisive failure. Estimates are mine, post-gate, and are deliberately
higher than the node's prior `P = 0.35` because the counterexample half is now essentially in hand.

### R1 · `laurent-group-ring` — **recommended primary**

- **Premises.**
  1. `P1.1` Time-locality: `∂_circ(i,r) = x^r ( u_i(1+x) + s_i x )` for every elementary fault, with
     the boundary rounds handled separately (Obs. 1.1).
  2. `P1.2` `C_•(circ)` is a free `F₂[x,x⁻¹]`-module in the bulk and `π_0 = ε` (augmentation).
  3. `P1.3` Divisibility lemma: `Σ s_i = 0 ⟹ B(x) = (1+x)C(x)`, and `F₂[x,x⁻¹]` a domain
     ⟹ closed lift `⟺ A(x) = xC(x)` (Conj. 3.7).
  4. `P1.4` Finite-window reduction: the min-weight closed lift uses rounds within a window of
     bounded size `B(r,d)`. **Shared premise with `CIRCDIST.sat`.**
  5. `P1.5` Boundary quotient: the truncated circuit's complex is the bulk module modulo an
     explicit boundary submodule, and boundary edges are voltage sinks (Conj. 3.6).
- **Implication sketch.** `d_circ = min` over `F₂[x,x⁻¹]`-solutions of `A = xC` with `Σλ ≠ 0`,
  weighted by number of monomial terms; `= min_γ ℓ(γ)`; equality with `d_eff` iff some minimum-weight
  `γ` admits an all-same-round solution (`Σ u_i = 0`, Conj. 3.8) or a windowed one. Non-interleaved
  corollary via R4; strict example already in §4.
- **P = 0.55.** OPEN band, placed high: the algebra is elementary, `F₂`-valued (no orientation
  problem), and §3.4/§4 already agree. Main risk is `P1.4`+`P1.5`, both genuinely open.
- **D = 2 sessions.**

### R2 · `voltage-monodromy-lift` — the Gross–Tucker route the commission named

- **Premises.** `P2.1` `G_circ|bulk = ` derived graph `G_eff^α`, `Γ = Z`; `P2.2` net-voltage /
  path-lifting theorem (external, §7 A1); `P2.3` the `F₂`↔`Z` orientation reconciliation of
  Obs. 3.5, in the "zero-voltage closed-walk decomposition" form; `P2.4` multi-edge voltage spectra
  `U(s,λ)` — which voltages a base edge admits *at weight 1*; `P2.5` boundary truncation.
- **Implication sketch.** Net voltage zero ⟺ closed lift ⟹ Conj. 3.3 with an intrinsic voltage.
- **P = 0.40.** Same band as R1 but placed lower: `P2.3` is a real technical wall (an `F₂` cycle has
  many Eulerian orientations, so "the" net voltage is a *set*), and Obs. 3.4 has already killed the
  attractive-looking cohomological shortcut. R1 routes around exactly this wall. Keep registered
  because it is the formulation the commission asked for and because it is the geometric intuition
  that generates conjectures.
- **D = 3 sessions.**

### R3 · `boundary-ramification` — covering vs branched covering vs chain map

- **Premises.** `P3.1` `π` is a covering away from temporal and logical boundaries (local star
  isomorphism); `P3.2` compactifying the temporal boundary makes it a branch point of full
  ramification — or, alternatively, that `π` is a **harmonic morphism** in the Baker–Norine sense
  (§7 A4) and the branched-covering language is licensed; `P3.3` boundary edges are voltage sinks,
  with an explicit accounting of how much voltage a boundary-touching logical can dump for free;
  `P3.4` an `R`-independence lemma: for `R` above an explicit threshold the criterion stabilises.
- **Implication sketch.** Gives the node's requirements 2 and 5 and makes the iff *statable* with
  boundaries, which is the thing most likely to break a clean criterion.
- **P = 0.35.** Placed mid-band. `P3.3` is the identified danger zone: a logical that reaches the
  boundary may always be closable, which would confine `g(C) > 0` to boundary-avoiding logicals and
  substantially weaken the theorem — or clarify it. Either outcome is informative.
- **D = 2 sessions.**

### R4 · `noninterleaved-horizontal-representative` — the corollary

- **Premises.** `P4.1` CNOT propagation table for CSS single-ancilla extraction (`Z` on X-ancilla is
  a pure measurement error; `X` on X-ancilla makes the hook; dually for Z); `P4.2` block-separation:
  in a non-interleaved schedule the opposite-type checks are uniformly before or uniformly after any
  fault; `P4.3` hence `u ∈ {0,s}` for every effective fault type; `P4.4` same-round lift closes when
  `Σ u_i = 0` (Conj. 3.8); combine.
- **Implication sketch.** `⟹ G_circ ⊇ R` disjoint copies of `G_eff ⟹ d_circ ≤ d_eff ⟹` equality
  with Conj. 3.2. Recovers Strikis et al. Cor. 1 from the covering picture (node requirement 6).
- **P = 0.70.** Highest of the six: the target statement is already an established theorem
  (arXiv:2603.05481 Thm. 1), so only *our* derivation can fail, and its mechanism was confirmed on
  both sides of §4's A/B pair.
- **D = 1 session.**

### R5 · `minimal-interleaved-gap-example` — **largely discharged this session**

- **Premises.** `P5.1` the `[[4,2,2]]` A/B pair of §4 (**done, NUMERICAL**); `P5.2` independent
  reproduction under a standard DEM tool; `P5.3` a `d = 3` instance with `d_eff = 2`, `d_circ = 3`;
  `P5.4` a certificate format (exhaustive enumeration log or ILP/SAT infeasibility proof) that a
  reviewer can check without rerunning a simulator.
- **Implication sketch.** Discharges the node's "至少一个交错严格不等号例子" acceptance clause and
  proves the criterion non-vacuous.
- **P = 0.85.** NUMERICAL band. The hard part happened; what remains is reproduction and escalation.
- **D = 1 session.**

### R6 · `gap-formula-and-decision-algorithm` — the extras

- **Premises.** `P6.1` repair-cost lemma: each vertical (measurement-error) edge shifts voltage by
  exactly 1 and is available at every check, so `ℓ(γ) ≤ |γ| + |volt(γ)|` — **verified in §4.3 at
  `|volt| = 1`**; `P6.2` matching lower bound; `P6.3` a poly-time decision procedure for
  "does *this* `γ` close?" via flow/T-join (Obs. 3.5(b)); `P6.4` an honest hardness caveat — finding
  the minimum-weight `γ` is already hard, so the algorithm must be conditional on a given `γ` or on
  a code family.
- **Implication sketch.** `g(C) = min_{γ: |γ|=d_eff} volt-repair(γ)` and an equality test that never
  builds `C_R(M)` — the node's "不需要构造完整多轮电路的等号判定算法".
- **P = 0.25.** Lowest: this is where an iff turns into a *theory*, and `P6.2` (the lower bound —
  showing you cannot be cleverer than paying `|volt|`) is the genuinely hard part.
- **D = 3 sessions.**

### Route table

| route | one-line idea | P | D |
|---|---|---|---|
| `laurent-group-ring` | spacetime complex = effective complex over `F₂[x,x⁻¹]`; `π₀` = augmentation; closed lift ⟺ `A(x)=xC(x)` | 0.55 | 2 |
| `voltage-monodromy-lift` | Gross–Tucker derived graph, `Γ=Z`; lift closes iff net voltage 0 | 0.40 | 3 |
| `boundary-ramification` | covering off the boundary, branch point at the compactified temporal boundary; boundary edges are voltage sinks | 0.35 | 2 |
| `noninterleaved-horizontal-representative` | non-interleaved ⟹ every effective fault has a `u∈{0,s}` representative ⟹ `R` disjoint copies of `G_eff` | 0.70 | 1 |
| `minimal-interleaved-gap-example` | `[[4,2,2]]` A/B pair, `d_eff=1`, `d_circ=1` vs `2` — **done, needs reproduction + `d=3`** | 0.85 | 1 |
| `gap-formula-and-decision-algorithm` | `g(C)` = voltage repair cost; poly-time equality test without building `C_R(M)` | 0.25 | 3 |

Node-level `P` under the protocol's `1 − Π(1 − P_route)` rule is not meaningful here because the
routes are not alternatives for the *same* claim — R4/R5 discharge named sub-clauses of the node
claim while R1/R2/R3 are genuine alternatives for the main theorem. A future dispatcher should
model the node as `(R1 ∨ R2 ∨ R3) ∧ R4 ∧ R5`, with R6 attached to the "further results" clause only.

---

## 6. The single cheapest decisive gate

**The gate identified at the start of this session was exactly the one the commission proposed** —
construct a minimal interleaved example with `d_circ > d_eff`, or discover that small examples all
close — **and it was run and passed within the session.** §4 is the outcome. The pre-registered
reading of the outcomes was:

- *example found* ⟹ the obstruction is real, the iff is non-vacuous, the necessary direction has
  content, and the voltage mechanism is validated → reprice `P` upward. **This is what happened.**
- *no example in a broad small search* ⟹ suspect `d_circ = d_eff` always in graphlike models, which
  would make the node's target theorem a much stronger and quite different result.

Because the gate has fired, the useful output of this section is the **next** cheapest decisive gate.

> ### Next gate: a `d = 3` gap instance with a checkable certificate.
>
> **Construct.** The rotated distance-3 surface code (9 data, 8 ancillas) — or Steane `[[7,1,3]]` —
> with (i) a within-check CNOT order chosen so that `d_eff = 2` (a hook error that halves the
> distance), and (ii) an interleaving in which that hook's residual is split across the round
> boundary by the opposite-type checks, i.e. `u ∉ {0, s}` for the hook fault. Then compute `d_eff`
> exactly from the residual set, and `d_circ` exactly by exhaustive weight-≤2 enumeration over the
> DEM (small enough to certify by enumeration, not heuristics).
>
> **Cost.** One session, most of it spent installing or re-deriving a DEM tool (`stim` is absent from
> this environment) or extending the ~200-line `F₂` propagator of §4.
>
> **Outcomes and what each implies.**
> - **`d_eff = 2`, `d_circ = 3` found** → the gap survives at `d = 3` with a non-degenerate logical;
>   the example becomes publishable, R5 closes, and R1's target theorem acquires a second data
>   point that distinguishes `|volt| = 1` from higher voltage. Reprice R1 to ~0.65.
> - **every `d = 3` interleaving closes (`g = 0`)** → the phenomenon is confined to detection codes
>   or to `d_eff = 1`, which would be a sharp and surprising structural fact: it would say the
>   obstruction only bites when the effective logical is a *single vertical edge*, i.e. when the
>   base image is a loop. That is a strictly stronger and cleaner theorem than the commissioned one,
>   and it would redirect R1 towards proving it. Reprice, do not abandon.
> - **`g = 2` or larger found** → `g(C)` is unbounded-looking, R6's repair-cost formula becomes the
>   headline, and `CIRCDIST.gross`'s distance-12 hope gains real support.
>
> **Why this and not something else.** It is the only cheap experiment whose three outcomes lead to
> three *different* theorems. Attacking R1's `P1.4` finite-window premise directly is more valuable
> per unit of proof but costs ≥2 sessions and duplicates `CIRCDIST.sat`; attacking the boundary
> premise `P3.3` is cheap but its outcome does not change what anyone would do next.

---

## 7. Load-bearing external results, as ASSUMPTIONS

Established results only. Honesty flags are literal.

**A1 — Net voltage / lifting theorem for voltage graphs.**
*Statement assumed:* Given an ordinary voltage graph `(G, α: E(G) → Γ)` and its derived graph
`G^α`, a closed walk `W` in `G` lifts to a closed walk in `G^α` **iff** the net voltage of `W` is
the identity of `Γ`; for abelian `Γ`, the derived graph is disconnected into `|Γ|` copies of `G`
iff `α` is a coboundary (equivalently, the net-voltage map `H₁(G) → Γ` is trivial).
*Source:* Gross & Tucker, *Topological Graph Theory* (Wiley 1987; Dover reprint), Chapter 2
(voltage graphs, derived graphs, permutation voltages).
**HONESTY FLAG: this statement is standard and I am confident of its content, but I have NOT
verified the exact theorem numbering or verbatim wording against the book in this session.** A
future session must pin the numbering before citing.

**A2 — Extended-code / effective-distance definitions and the non-interleaved equality.**
*Statement assumed:* arXiv:2603.05481 (Strikis, Browne, Beverland, 2026) Defs. 1–3, Prop. 3
(`d_circ ≥ d_ext(ℰ)`), Thm. 1 and Cor. 1 (non-interleaved single-ancilla CNOT-based CSS SEC:
`d'_circ = d_ext(ℰ)`, and `d'_circ ≤ d_circ`), Prop. 4 (gross code, non-interleaved `d_circ ≤ 11`;
depth-8 circuit *conjectured* to reach 11).
**HONESTY FLAG: VERIFIED — abstract and HTML full text fetched this session; the direction of
Prop. 3 was re-fetched and confirmed twice.** Hypotheses matter and must be carried: single-ancilla,
CNOT-based, CSS, and within-check CNOT order preserved.

**A3 — Detector error models and circuit distance.**
*Statement assumed:* the DEM formalism (detectors as deterministic measurement parities,
observables, error mechanisms as columns) and `d_circ` as the minimum number of error mechanisms
flipping no detector and at least one observable; "graphlike" = an error mechanism flipping at most
two detectors.
*Source:* arXiv:2407.13826 (Derks, Townsend-Teague, Burchards, Eisert, 2024) for the formal
treatment; Gidney arXiv:2103.02202 for Stim itself.
**HONESTY FLAG: the "graphlike = at most two detectors" definition is MEDIUM confidence — obtained
from Stim documentation snippets, not from a fetched primary definition. The Stim *paper* does not
formally define DEM, graphlike, or circuit distance; do not cite it for those.**

**A4 — Branched coverings / harmonic morphisms of graphs.**
*Statement assumed:* harmonic morphisms of graphs generalise covering maps, with a well-defined
local degree at each vertex, and reduce to coverings exactly when every local degree is 1.
*Source:* Baker & Norine, *Harmonic morphisms and hyperelliptic graphs* (arXiv:0707.1309, as best I
recall).
**HONESTY FLAG: UNVERIFIED this session — arXiv id and exact definition from memory. Needed only if
route R3 takes the branched-covering formulation seriously; if it does, verify first.**

**A5 — CSS codes as chain complexes; homological distance.**
*Statement assumed:* a CSS code is a length-3 `F₂` chain complex with `d` the minimum weight of a
nontrivial (co)homology class; chain maps induce maps on homology and are weight-non-increasing on
chains when they are fiber collapses.
*Source:* Tillich & Zémor, arXiv:0903.0566 (hypergraph product); Bravyi & Hastings for homological
product codes.
**HONESTY FLAG: standard and confidently stated; arXiv id for Tillich–Zémor from memory, not
verified this session.**

**A6 — Spacetime chain-complex formalism preserving fault distance.**
*Statement assumed:* arXiv:2509.09603 (Pesah, Daniel, Tzitrin, Vasmer) gives a chain-complex /
chain-map framework for spacetime codes in which fault-tolerant maps preserve the number of encoded
qubits, the **fault distance**, and the minimum-weight decoding problem.
**HONESTY FLAG: abstract VERIFIED; I have NOT read the body, and whether their morphisms include
our `π` (a fiber collapse that does *not* preserve fault distance) is unchecked — quite possibly
`π` is exactly a non-example in their framework, which would be useful to know.**

**A7 — Covering spaces ↔ modules over the deck group ring.**
*Statement assumed:* for a regular covering with deck group `Γ`, the chain complex of the cover is a
complex of free `F₂[Γ]`-modules whose augmentation `ε: F₂[Γ] → F₂` recovers the base complex; the
obstruction to lifting a base cycle lies in the augmentation ideal.
*Source:* standard algebraic topology (Hatcher, §1.3 and §3.H); the Laurent-ring specialisation
`Γ = Z` is the Alexander-module pattern.
**HONESTY FLAG: standard; no specific theorem number verified this session. Route R1 rests on the
elementary `F₂[x,x⁻¹]` computation of §3.4 rather than on the general theory, so A7 is orientation,
not load-bearing.**

**Not assumed, explicitly:** any claim that `π` is a covering at the boundary; any claim that
`d_circ = d_eff` holds generally (§4 refutes it); any claim about multi-ancilla, flag, or cat-state
schedules (all out of scope per the 公共定义).

---

## 8. Surprises and corrections worth propagating

1. **The gap is real and small examples already show it.** Prior expectation in the node record was
   that finding an interleaved strict inequality might be hard. It took one `[[4,2,2]]` circuit, and
   8 of the 11 legal Z-orders under one interleaving template exhibit it.
2. **`d_eff` is an invariant of the within-check orders alone** (Consequence 2.1). This makes
   "interleaving pattern" the sole variable in `g(C)` and is the cleanest available problem slicing.
   It also means an A/B pair sharing within-check orders is the canonical experimental design — and
   §4 uses exactly that, so the two numbers are comparable by construction.
3. **The obvious cohomological criterion is dead** (Obs. 3.4): `[α] = 0 in H¹(G_eff; Z)` is
   essentially never true, because bare data errors pin the potential to a constant while hook edges
   are diagonal. The criterion must be a pairing with a specific minimum-weight class. This should
   save a future session from a plausible-looking dead end.
4. **The `F₂`-vs-`Z` orientation mismatch is the real technical crux of the voltage route** (Obs.
   3.5), and the group-ring route (§3.4) sidesteps it entirely by keeping everything `F₂`-valued
   with the time grading carried by `x`. That is why R1 outranks R2 despite R2 being the formulation
   the commission named.
5. **Cross-root coupling.** `CIRCDIST.lift` supplies the only mechanism by which `CIRCDIST.gross`
   could reach 12 (Strikis et al. cap non-interleaved gross circuits at 11), and R1's premise
   `P1.4` is the same finite-window/pumping statement `CIRCDIST.sat` is commissioned to prove. The
   round-1 scheduling note treated the four roots as disjoint subtrees; that is correct for
   commit-safety but **understates `v(lift)`**.
6. **Tooling gap.** `stim`, `pymatching`, `ldpc`, `galois`, `networkx` are all absent from this
   environment; only `numpy`, `scipy`, `sympy` are present. Any session planning DEM computation
   should budget for installing tooling or for re-deriving a propagator. §4 chose the latter and it
   cost little at this size, but it will not scale to the gross code.

---

## 9. Suggested repricing (input to the dispatcher; not a status write)

The canonical node record is untouched by this session — no file under
`research/circdist/proof-dag/` was modified, per the commission. The following is advisory only.

- Node `CIRCDIST.lift`: prior `P = 0.35`, `D = 5`. After this session the "interleaved strict
  inequality" acceptance clause is essentially discharged (NUMERICAL) and the framework has a
  concrete algebraic form. Suggested: `P ≈ 0.45–0.50`, `D ≈ 4`, with the caveat that the *iff* — the
  part that must be intrinsic and not a tautology (⚠ in §3.1) — remains the whole difficulty.
- The node's `frontier: task-001` (route registration) is discharged by §5.
- Suggested next frontier item: the `d = 3` gap instance of §6, boxed at one session.
- Level: this session produces graph growth plus a numerical counterexample, i.e. productive under
  VALUATION_PROTOCOL §4 clauses 2 and 3. It does **not** by itself license promoting the node claim
  above OPEN, because the node claim is the iff, not the counterexample.
