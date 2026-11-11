# Independent review — `CIRCDIST.sat.transfer` min-plus transfer theorem

**Reviewer:** fresh Opus 5 session, independent. **Date:** 2026-08-23. **Box:** one session, no
sub-agents, stop-loss binding. **Artifacts written:** exactly this one. **Files modified:** none.
`research/circdist/proof-dag/` not touched or read.

## 0. Independence statement

I did not author the work under review, and I was not told any desired verdict. I was instructed to
try to refute. Under the anchoring ban I derived the state space, the transfer matrix, the boundary
vectors and the undetectability recursion **myself, from the frozen definitions only**
(`research/circdist/notes/CIRCDIST_PROBLEMS.md` 公共定义 + `SAT_RESCOPE_20260822.md`), and wrote that
derivation to a sealed scratchpad file **before opening the target document**. All numerical work is
my own code, written from my own derivation; the target's `transfer.py` (§11.4) was read only after
my own program was written and run, and no line of it was copied or executed.

### Inputs (hashes as verified by me)

```text
4fce5371edc09fa153b41f6735d521d31500b84b55a0059c8b42dc000651da30  artifacts/circdist_sat_transfer_proof_20260823.md   (TARGET)
5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64  research/circdist/notes/CIRCDIST_PROBLEMS.md
6c8ec4362f728713f9934d5f0b8041195f66434ebe283a69e67147b3c7009d7f  research/circdist/notes/SAT_RESCOPE_20260822.md
487acf030bc4385ab367e5c7b27a0e2015bae4055f16ba61100ea85866d37e1b  artifacts/circdist_sat_window_theorem_20260822.md
```

The last two match the target's own declared hash chain (§0) exactly, so the document was written
against the governing statements it claims.

**Background processes.** I started none. The ~20 `job3.py` / `job7k.py` / `noclass.py` /
`witness2.py` + `kissat` workers on this machine belong to another work item; I did not kill,
signal, inspect or otherwise touch them. My own runs were `nice -n 19`, single process, < 6 s each.

---

## 1. My pre-read derivation (written before opening the target)

Sector: X-type data faults, detected by Z-checks. `f_r` = accumulated data X-error after round `r`,
`δ_r` its round-`r` increment, `g(φ_r) ∈ F₂^ℬ` the flips round-`r` faults induce in round `r`'s own
records with a zero incoming frame.

**My key lemma.** `m_{b,r} = (H_Z f_{r−1})_b + g_b(φ_r)`, because ancilla `b` accumulates the parity
of its support at its own CNOT times, all of round `r−1`'s error is complete before round `r` begins,
and the part of `δ_r` landing before CNOT`(b,q)` is inside `g`. Hence

```
D_{b,r} = m_{b,r} + m_{b,r−1} = (H_Z δ_{r−1})_b + g_b(φ_r) + g_b(φ_{r−1}).     (*)
```

**(i) w = 2 is forced, not stipulated.** (*) touches only rounds `r−1, r`. The *only* inter-round
channel is the accumulated `f`, and the differencing annihilates everything except `δ_{r−1}`. Hooks
and interleaving cannot widen this: a hook is a within-round object, entering either `g(φ_r)` or
`δ_r`. A `w > 2` window needs an ancilla whose prep/CNOTs/measurement straddle a round boundary, or
an un-zeroed ancilla frame — both excluded by the frozen model.

**(ii) The class is sufficient.** Put `h_r := H_Z δ_r + g(φ_r)`. All detectors vanish iff
`g(φ_r) = h_{r−1}`; then `h_r = h_{r−1} + H_Z δ_r`, and with `h_0 = 0` (ideal init) `h_r = H_Z f_r`.
Since `H_Z H_X^⊤ = 0`, `h_r` is a function of `[f_r] ∈ Σ = F₂^n/S_X` **alone**. This is a derivation,
not an assertion, and it hinges on the round-0 absolute detector existing in this sector.

**(iii) Consequences I derived before reading.** `A[σ,σ'] = min{|S| : [E(S)] = σ'−σ, u(S) = H_Z σ}`;
`u = 1_{[0]}`; `v` supported on `ker H_Z/S_X ∖ {0}`; `A[σ,σ] = 0` iff `H_Z σ = 0`, giving **exactly
`2^k`** zero-weight self-loops; monotonicity, `d_R ≤ d`, and `d_R = d_d` for `R ≥ d` by deleting
zero-cost self-loops.

**Every one of (i)–(iii) matches the target's §4–§7 and §9.** In particular my `h_{r−1}` is exactly
its `H_Z σ_r`, and my `g` is exactly its `u(S_r)`. This independent agreement is the strongest single
piece of evidence in this review, and it was obtained without reading the target's derivations.

---

## 2. Discipline

**(7a) Type audit.** I checked every displayed type. `H_Z` descends to `Σ` (`S_X ⊆ ker H_Z` by CSS) —
sound; `w_M : Σ × F₂^ℬ → ℤ_{≥0} ∪ {∞}` — sound; `V_X = {α : Σ_r H_X^⊤α_{·,r} = 0} = {α : Σ_r α_{·,r}
∈ leftker H_X}` — the two forms agree since `leftker H_X = ker H_X^⊤`; `ζ^{(r)} = γ + Σ_{r'≥r}
H_Z^⊤β_{·,r'} ∈ F₂^n` — sound; dimension bookkeeping `n − rank H_X = rank H_Z + k` — sound and
consistent across §3.3, 3.6, 4.3. Two type defects found, both cosmetic, recorded as F4 and F5.

**(7c) Anchoring ban.** Discharged as described in §1.

**Evidence asymmetry — absence-type steps attacked at their scope boundaries.** The five
absence-type claims I targeted: (a) "no measurement memory and no logical bookkeeping beyond the
class is needed"; (b) "there are **no** unreachable states"; (c) "`𝒟_Z = span{D_{b,r}}` **exactly**",
i.e. no Z-side detector escapes Definition 2.7; (d) "genuine sector coupling is impossible"; (e) the
T-G3 mitigation "**any** `𝒟` between Definition 2.7 and `V` leaves 3.7 intact". (a)–(d) survive; **(e)
does not** — see F1.

**(7f) VALUE vs PRINTED-DERIVATION.** Stated per item below. Throughout, "value confirmed" means the
mathematical content is right; "printed derivation confirmed" means the text as written establishes
it without a further step.

---

## 3. Item verdicts

### Item 1 — SUFFICIENCY (Lemma 6.4) and the `w = 2` scoping. **CONFIRM.**

*Value and printed derivation both confirmed.* My independent derivation (§1(ii)) reproduces
criterion (W) exactly, and the target's §6.1–§6.4 chain is correct as printed.

I attacked the `w = 2` scoping directly and empirically. For all 16 (schedule, sector) instances I
verified Lemma 6.1 **exactly**, not merely "the window looks like 2": for every elementary X-sector
fault `f` placed in every round `r` of a 4-round circuit, I checked that `D_{·,r}` is flipped by
`u(f)`, `D_{·,r+1}` by `u(f) + H_Z E(f)`, and every other detector by `0`.

```
detector predictions checked: 378,720    mismatches: 0
```

This covers both interleaved surface schedules and the dependent-generator code, i.e. exactly the
regimes where a hook or an interleaving effect could smuggle in a wider window. It does not.

One scope refinement the document undersells: Remark 6.6 says "Definition 2.7 fixes `w = 2`". That is
weaker than the truth. `w = 2` is *forced* by the model (ancilla frames zeroed each round + rounds
disjoint), and, more importantly, §3.6's **equality** `𝒟_Z = span{D_{b,r}}` is what rules out a
canonical Z-side detector spanning more than two rounds. The theorem is therefore better supported
than its own remark claims. Recorded as F5 (presentational).

### Item 2 — THE LIFTING DIRECTION (§7), the `A_κ` family, sector block-diagonality. **GAP-AT-Remark-6.5.**

*Theorem 7.1 itself: value and printed derivation confirmed.* I re-derived both directions.
Projection consumes sector decoupling, the round partition of locations, and (W)'s two boundary
instances — all sound. Lifting consumes attainment (5.6(ii)) and, critically, that the round-`r`
*constraint* `H_Z σ_r` is a function of the class and can therefore be fixed **before** the actual
representative `Σ_{r'<r} E(S_{r'})` is known. That is the real load-bearing step and it is correct:
`H_Z(f + s) = H_Z f` for `s ∈ S_X` by CSS. Remark 7.3's diagnosis (without descent, the theorem
degrades to an inequality) is right.

**Sector coupling is genuinely block-diagonal. CONFIRM.** The project's recurring trap — "X faults
triggering Z detectors via hooks" — is correctly diagnosed in the §8 box as *not* sector coupling: a
hook is one X-sector fault with `|E(f)| > 1` and `u(f) ≠ 0`, and the dictionary records exactly that
pair. Genuine coupling would need `m_{b,·}` (a `Z`-basis measurement, flipped only by `x`-components)
or `m_{a,·}` (an `X`-basis measurement, flipped only by `z`-components) to see the wrong type;
Lemma 3.1's type-preservation argument is correct. `Y` faults are handled by weight-non-increasing
projection to the `x`-part, which is legitimate **because Definition 2.8 makes all 15 (resp. 3)
Paulis available at unit cost at every location**. I confirm the document flags this as the exact
model-dependence; under non-uniform fault weights the projection would fail.

**The `A_κ` quantification is WRONG. (F2.)** Remark 6.5 states that dropping the round-0 detector
gives `d_R = min_κ ( u ⊙ A_κ^{⊙R} ⊙ v )` with `A_κ[σ,σ'] := w_M(σ'−σ, H_Z σ + κ)` and **the same
`v`**. My derivation says otherwise: without `D_{b,0}`, the terminal detector reads
`D_{b,R} = H_Z σ_R + (H_Z σ_{R−1} + u(S_{R−1})) = H_Z σ_R + κ`, so the terminal condition is
`H_Z σ_R = κ`, **not** `H_Z σ_R = 0`; and since `E_tot ∉ ker H_Z` in general, "logical" is no longer
`σ_R ≠ [0]` but `λ(σ_R) = 1`. The correct object is `v_κ[σ] = 0` iff `H_Z σ = κ` and `λ(σ) = 1`.
Holding `v` fixed forces `κ = 0` and collapses the family, so the displayed formula is not merely
imprecise — it computes the wrong number. Verified against direct simulation with `D_{b,0}` deleted:

```
instance                R=2                              R=3
steane713/blkZ/Z        truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
steane713/blkZ/X        truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
surface913/blkZ/Z       truth 1  Rem6.5 3  corrected 1   truth 1  Rem6.5 3  corrected 1
surface913/blkZ/X       truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
steane+redX/blkZ/Z      truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
steane+redX/blkZ/X      truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
surface913/ilv1/Z       truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
surface913/ilv1/X       truth 1  Rem6.5 3  corrected 1   truth 1  Rem6.5 3  corrected 1
```

Remark 6.5's formula is wrong in **16 of 16** cases; my corrected `v_κ` is right in 16 of 16.

**Severity: contained.** Remark 6.5 is a counterfactual about a model Theorem T does not use —
Theorem T *has* `D_{b,0}`, so no line of §7 or §9 inherits the error. But it is a displayed formula
presented as the "precise form of the round-0/terminal asymmetry", it is the exact object this review
was asked to check, and it is false as printed. It must be repaired before the text is certified.

### Item 3 — THE FAULT DICTIONARY. **CONFIRM (all four sub-claims, plus both recon corrections).**

*Value and printed derivation confirmed.* Verified on my own implementation:

* **Well-definedness.** `w_M` is a minimum over a finite non-empty set of one-round configurations
  with prescribed `([E], u)`; Lemma 2.9's collision merge makes the multiset and configuration minima
  agree. Sound.
* **Round-independence (Lemma 5.3).** Tested directly rather than accepted: for every elementary
  fault of every instance I compared the full round-local effect `(E, z-frame, m_b, m_a)` when placed
  in round 0, 1 and 2 of a 3-round circuit. **54,672 comparisons, 0 round-dependent.**
* **Finiteness (Lemma 5.5).** I re-derived the two weight-1 families. The zero-voltage singleton
  argument is correct, including its edge cases: `t*` is unique by legality, every CNOT joins exactly
  one data qubit to one ancilla so distinct data qubits have distinct `t*`-gates, and both the
  `q→b` and `a→q` branches leave `u = 0` because no later gate touches `q`. All `A` entries finite in
  **all 16 instances**.
* **Recon correction 1 — `2^k`, not `2^{2k}`, self-loops. CONFIRM, and I strengthened the test.**
  The document's own data is `k = 1`, where `2^k = 2` and `2^{2k} = 4`; that already discriminates,
  but weakly. I added a **`k = 2`** instance the document explicitly does not cover ([[4,2,2]],
  `𝒜 = ℬ = {0123}`), where the two formulas predict 4 vs 16:

  ```
  422/Z   |Sigma|=8   zero-loops=4 (= 2^k)   |v finite|=3 (= 2^k - 1)   transfer [1,1,1] == truth [1,1,1]
  422/X   |Sigma|=8   zero-loops=4 (= 2^k)   |v finite|=3 (= 2^k - 1)   transfer [1,1,1] == truth [1,1,1]
  ```

  This also gives the first independent confirmation of the `2^k − 1` count of finite `v` entries at
  `k > 1`, and the first `k > 1` transfer-vs-direct agreement anywhere in this node.
* **Recon correction 2 — "unreachable states" is vacuous. CONFIRM.** Every `A` entry finite in all
  16 instances plus both `k = 2` instances, so the transition graph is complete. The replacement
  (Remark 5.7's pruning to the optimal-path support) is the honest object; I confirm it is a
  statement about optimal paths, not reachability, and that the document says so.
* **Bonus: Corollary 9.1 sharpened empirically.** `A[σ,σ'] = 0` iff `σ = σ'` and `H_Z σ = 0`. I
  checked the "only if" half — the absence-type half — directly: **off-diagonal zero entries = 0** in
  all 8 instances tested, with diagonal zeros exactly at `H_Z σ = 0`. This is the fact Corollary 9.5's
  path-compression rests on, so it deserved a direct test rather than inheritance.

### Item 4 — T-G3 AND DEFINITION 3.5. **Def 3.5 CONFIRM; §3.6 CONFIRM; mitigation bullet (a) REFUTE.**

This item feeds a lead ratification, so I state the decision cleanly and separately for the three
sub-questions.

**(4a) Is Definition 3.5 well-posed? YES — CONFIRM.** My pre-read attack was that "parities
independent of the prepared logical basis state" fails to exclude parities that are *random* with a
state-independent distribution (e.g. a single `m_{a,0}` in a Z-memory). The definition survives:
Definition 3.2 first restricts to `V`, the parities that are **deterministic** (back-propagated Pauli
in `G_0`), and Definition 3.5 then selects those whose *value* is constant across the family. Both
conditions are present, so the definition is well-posed. It is also a genuine subspace: the value
shift is `Σ_j s_j⟨ζ^{(0)}, χ_{X_L^{(j)}}⟩`, linear in the parity, so `𝒟` is the kernel of a linear
map `V → Hom(F₂^k, F₂)`. And "flips some `λ^{(j)}`" is representative-independent for undetectable
faults, since such a fault has a well-defined image in `V_Z/𝒟_Z ≅ F₂^k`. I ratify Definition 3.5 as
well-posed and canonical.

**(4b) Do Definition 2.7's Z-detectors span `𝒟_Z` exactly? YES — CONFIRM.** I re-derived the
triangularity argument (`D_{b,0} = m_{b,0}`, `D_{b,r} = m_{b,r} + m_{b,r−1}` for `r ≤ R−1` span every
`(β,0)`; the `D_{b,R}` add `γ`-parts spanning `S_Z`; dimensions `|ℬ|R + rank H_Z` match) and then
recomputed the spaces independently by my own back-propagation on the dependent-generator code:

```
steane+redX / blkZ / Z-memory, R=3:  #records 28   dim V 22   dim D (Def 3.5) 21
  lambda in V: True    lambda in D: False        <- lambda deterministic but not a detector
  P_X in V:    True    P_X in D:    True         <- the round-0 redundancy parity IS a real detector
  rank span{D_b,r} = 12 = dim D_Z ;  rank span{D_b,r} u {D_a,r} = 20 = dim D - dim leftker(H_X)
```

`dim V = 22`, `dim 𝒟_Z = 12`, X-side codimension `= 1 = dim leftker(H_X)` — all matching §3.6 and
NUMERICAL 11.2, computed by my own code. The Z-side equality is real, and the asymmetry (the Z-side
has no analogous hole because `D_{b,0}` absorbs every Z-side redundancy parity) is correct.

**(4c) Is the mitigation proved or asserted? ASSERTED — and it is FALSE. REFUTE. (F1.)**

T-G3 bullet (a) reads: *"whatever `𝒟` is chosen, if it contains the Definition-2.7 set and is
contained in `V`, then Proposition 3.7's argument goes through verbatim, because `F^X` annihilates
*all* of `V_X` and all of `𝒟_Z`."* This is offered as the principal reason a ratifying reader need
not worry about which split is chosen. It is not proved anywhere, and it is false.

The gap in the reasoning: `F^X` annihilates `V_X` and `𝒟_Z`, hence annihilates
`𝒟_Z ⊕ V_X = 𝒟`. But `V = 𝒟_Z ⊕ span{λ} ⊕ V_X` is *strictly larger* than `𝒟`, and a `𝒟'` with
`𝒟' ⊆ V` may contain elements with a non-zero `λ`-component, which `F^X` — being logical — flips by
construction. The correct hypothesis is `𝒟' ⊆ 𝒟`, not `𝒟' ⊆ V`.

I built an explicit counterexample on the document's own dependent-generator code, and checked that
it satisfies not only the literal hypothesis but also the stronger, more charitable reading (a
*complement of the observables*, which is what T-G3's own headline says a detector space must be):

```
D' := span{D_b,r}  +  span{D_a,r}  +  span{ P_X + lambda },
      P_X := m_{a0,0} + m_{a1,0} + m_{a2,0} + m_{a3,0}   (round-0 redundancy parity)
```

`P_X` exists because the four X-checks of `steane+redX` sum to zero (verified: XOR of all four = 0).
Verified properties of `D'` (my own rank computations, R = 2 and R = 3):

```
R=3:  rank D' = 21 = dim V - 1        -> codimension 1 in V
      rank D' u {lambda} = 22 = dim V -> D' + span{lambda} = V
      lambda not in D'                -> D' is a genuine COMPLEMENT of span{lambda} in V
      D' contains the whole Definition-2.7 detector set, and D' is contained in V
```

So `D'` satisfies the bullet's hypothesis exactly. Yet the conclusion fails:

```
steane+redX, Z-memory:   R=2:  d_R against Def-2.7 = 2    d_R against D' = 3
                         R=3:  d_R against Def-2.7 = 2    d_R against D' = 4
```

The mechanism is precisely the one the bullet's own reasoning overlooks: the minimising `F^X` flips
`P_X` by `0` but flips `λ` by `1`, hence flips `P_X + λ`, hence is *detected* against `D'`; recovering
a witness costs extra faults. Note this bites exactly in the dependent-generator case, which is the
case §3 was written to handle, and it is the case `leftker(H_X) ≠ 0` that scope clause T0 puts
explicitly in scope.

**Ratification decision.** Ratify Definition 3.5 (well-posed, canonical) and Propositions 3.6 and 3.7
(correct as printed, for the canonical `𝒟`). **Do not ratify T-G3 mitigation bullet (a).** Replace it
with: *"any `𝒟'` with `span{D_{b,r}} ⊆ 𝒟' ⊆ 𝒟` gives the same `d_R^Z`"* — which is true, and follows
from 3.1(2) plus the equality in 3.6. The residual risk T-G3 identifies is therefore **larger** than
the document estimates: a reviewer who prefers a different canonical split is *not* automatically
covered, and the case for Definition 3.5 has to be made on its merits (which, per (4a), it can be).

### Item 5 — THE ALGEBRAIC RE-DERIVATION (§9). **CONFIRM: genuinely independent, not circular.**

*Value and printed derivation confirmed.* I checked §9 line by line against the criterion "does any
step consult the window theorem's conclusions?".

* 9.3 (`d_R ≤ d`): uses only 5.5 and 9.1. Correct — the weight-`d_X` logical placed after the last
  round-`R` CNOT has `g = 0 = H_Z[0]` and `h_R = 0`, so it is a legitimate path.
* 9.4 (monotonicity): `A ⊙ v ≤ v` entrywise because every `v`-finite state carries a zero self-loop.
  Correct, and pleasingly it is the algebraic image of "append a fault-free round".
* 9.5 (compression): rests on 9.1's *only-if* half, which I tested directly (0 off-diagonal zeros).
  A weight-`W` optimal path has ≤ `W` positive-cost steps; deleting the zero-cost self-loops preserves
  endpoints and cost. `W ≥ 1` always, so `R' ≥ 1`. Correct.
* 9.6: I re-verified all three clauses arithmetically. `R ≥ d ⟹ R' ≤ min(R, d_R) ≤ d ⟹ d_d ≤ d_{R'}
  = d_R ≤ d_d`. And for `R_stab`: if `d_{R'} = d_∞` with `R' ≤ R_stab`, monotonicity makes `R'` a
  valid `R_0`, so `R_stab ≤ R' ≤ d_∞`. Both correct.

**Circularity check: passes.** §9 consumes only `(u, A, v)`, 9.1, 5.5 and 4.3. It does not import
parts (i)–(iii) of the window theorem. What it *does* share with the window theorem is the §2 model
and the content of Lemmas 5.4 and 6.2 — and the document says so, in its own "Consistency check,
stated as such" box, explicitly declining to call it certification. I judge that box accurate and
appropriately hedged; it is the correct epistemic label for what §9 is. This is the strongest
epistemic hygiene in the document.

One precision defect, recorded as F4: Corollary 9.2 argues "all entries finite, so `A` is
irreducible", then Theorem T(e) applies the same spectral language to the **assembled two-sector**
`A = A^Z ⊕ A^X`, which is block-diagonal and therefore *reducible*. Assumption A1 as stated is for
irreducible matrices. The conclusion survives (each block is irreducible with eigenvalue 0 and
cyclicity 1, so the direct sum is eventually constant too), and A1 is declared non-load-bearing, so
this is cosmetic — but it should not stand in a certified text.

### Item 6 — NUMERICAL 11.1 / 11.2. **CONFIRM the values; GAP in the driver's row labels (F3).**

The task asked for at least 8 of the 48 transfer-vs-direct values. **I reproduced all 48**, with my
own ground-truth simulator and my own transfer construction, sharing no code with `transfer.py`:

```
instance                   sec MC   ground truth   transfer       match  |Sigma| zloops finite
steane713/blkZ             Z   yes  [2, 2, 2]      [2, 2, 2]      OK     16 2 True
steane713/blkZ             X   yes  [2, 2, 2]      [2, 2, 2]      OK     16 2 True
steane713/blkX             Z   yes  [2, 2, 2]      [2, 2, 2]      OK     16 2 True
steane713/blkX             X   yes  [2, 2, 2]      [2, 2, 2]      OK     16 2 True
surface913/blkZ            Z   yes  [3, 3, 3]      [3, 3, 3]      OK     32 2 True
surface913/blkZ            X   yes  [2, 2, 2]      [2, 2, 2]      OK     32 2 True
surface913/blkX            Z   yes  [3, 3, 3]      [3, 3, 3]      OK     32 2 True
surface913/blkX            X   yes  [2, 2, 2]      [2, 2, 2]      OK     32 2 True
steane+redX/blkZ           Z   yes  [2, 2, 2]      [2, 2, 2]      OK     16 2 True   <- dependent generators
steane+redX/blkZ           X   yes  [2, 2, 2]      [2, 2, 2]      OK     16 2 True   <- dependent generators
steane+redX/blkX           Z   yes  [2, 2, 2]      [2, 2, 2]      OK     16 2 True
steane+redX/blkX           X   yes  [2, 2, 2]      [2, 2, 2]      OK     16 2 True
surface913/ilv0            Z   yes  [3, 3, 3]      [3, 3, 3]      OK     32 2 True   <- interleaved
surface913/ilv0            X   yes  [2, 2, 2]      [2, 2, 2]      OK     32 2 True   <- interleaved
surface913/ilv1            Z   yes  [2, 2, 2]      [2, 2, 2]      OK     32 2 True   <- interleaved
surface913/ilv1            X   yes  [3, 3, 3]      [3, 3, 3]      OK     32 2 True   <- interleaved
ALL MATCH: True
```

Every value in Table 11.3 is reproduced, including the discriminating `ilv0`/`ilv1` pair whose
per-sector distances are transposed (3/2 vs 2/3) — a schedule-sensitive signature that a
model-independent bug would be unlikely to reproduce. The `16 of 576` legal-and-(MC) interleaved
count and both named corner-order pairs also reproduce exactly under my own enumeration. The §11.2
parity-space dimensions reproduce under my own back-propagation (see item 4b). NUMERICAL 11.1 and
11.2 are sound.

**F3 — a real defect in the verbatim-published driver.** The document's `build()` mirrors the *block*
schedules incorrectly. Mirroring should conjugate by `H^{⊗all}`, which maps CNOT`(c,t) → `CNOT`(t,c)`
at the **same time step** and swaps the ancilla families; the driver instead re-derives the block
order from `schedname[3]` **after** swapping `A ↔ B`, which reverses the two blocks. I confirmed this
mechanically:

```
steane713     blkZ X-sector: == my mirror of blkZ? False  == my mirror of blkX? True
steane713     blkX X-sector: == my mirror of blkX? False  == my mirror of blkZ? True
surface913    blkZ X-sector: == my mirror of blkZ? False  == my mirror of blkX? True
surface913    blkX X-sector: == my mirror of blkX? False  == my mirror of blkZ? True
steane+redX   blkZ X-sector: == my mirror of blkZ? False  == my mirror of blkX? True
steane+redX   blkX X-sector: == my mirror of blkX? False  == my mirror of blkZ? True
```

So six rows of Table 11.3 — the `blk*/X` rows for all three codes — carry transposed labels: the row
printed `blkZ / X` is the X-sector of `blkX`, and vice versa. **No reported value changes** (I
computed the correctly-labelled versions above and they are identical, because the `blkZ/X` and
`blkX/X` values coincide for all three codes), and the *set* of 16 instances is exactly the intended
one, so the coverage claim survives. The interleaved rows are unaffected — the mirror is done
correctly there, and in any case `ilv0` and `ilv1` both have `π_X = π_Z`. Severity: low, but a
verbatim-published verification program in a to-be-certified artifact should not mislabel its rows.

---

## 4. Findings

| id | where | claim | verdict | severity | load-bearing for Theorem T? |
|---|---|---|---|---|---|
| **F1** | §12, T-G3 mitigation bullet (a) | "any `𝒟` with Def-2.7 set `⊆ 𝒟 ⊆ V` leaves Prop 3.7 intact" | **REFUTED** by explicit `𝒟'` (a genuine complement of the observables) with `d^{2.7} = 2` vs `d^{𝒟'} = 3, 4` | **high for the ratification**, none for the theorem | No |
| **F2** | Remark 6.5 | the "no `D_{b,0}`" family `d_R = min_κ(u ⊙ A_κ^{⊙R} ⊙ v)` with `v` fixed | **REFUTED**; `v` must be `κ`-dependent (`H_Zσ_R = κ`, logical `= λ(σ)=1`). Wrong in 16/16 tested cases | medium | No |
| **F3** | §11.4 driver `build()` | block-schedule mirror | **defect**; 6 of 16 table rows mislabelled, no value changes | low | No |
| **F4** | Cor 9.2 / Thm T(e) | "all entries finite, so `A` is irreducible", applied to the block-diagonal assembled `A` | **imprecise**; conclusion survives blockwise | cosmetic | No (A1 declared non-load-bearing) |
| **F5** | Thm T(a) box / Rem 6.6 | "the statement for `w > 2` **is false**"; "Definition 2.7 fixes `w = 2`" | **asserted, not shown**; and it undersells §3.6, which is what actually forces `w = 2` | cosmetic | No |

**Nothing I found touches the derivation chain of Theorem T.** Items 1, 3, 5 and the core of items 2,
4 and 6 all survived deliberate attack, and my pre-read derivation independently reproduces the
theorem's state space, transfer matrix, boundary vectors, recursion and `2^k` spectrum.

## 5. Overall verdict

> ### FURTHER-REPAIR
>
> — narrowly, and with the core theorem recorded as independently confirmed.

**Why not CLEARS-FOR-PROMOTION.** Theorem T survived every attack I mounted, and I would have cleared
it on the mathematics alone. But promotion to `CERTIFIED*` endorses the *document*, and the document
contains two statements that are false as printed (F1, F2), one of which — F1 — is precisely the
mitigation offered to the lead as grounds for ratifying the T-G3 definitional choice. Certifying a
text whose stated risk-mitigation is refutable would propagate a false reassurance into the assembly
node. The document's own epistemic ceiling ("nothing here is labelled PROVED"; "Rule 6 requires an
independent claim-level review") is exactly right, and this review is that review: it says repair,
not rebuild.

**Repairs required (all local; none touches §4–§9's argument chain).**

1. **F1 — replace T-G3 bullet (a).** Correct text: *any `𝒟'` with `span{D_{b,r}} ⊆ 𝒟' ⊆ 𝒟` yields the
   same `d_R^Z`* (true, and it follows from 3.1(2) + the equality in 3.6). State plainly that the
   containment `𝒟' ⊆ V` is **not** sufficient, and record the `steane+redX` counterexample above so
   the residual risk in T-G3 is not understated. This is the item the lead ratification turns on.
2. **F2 — repair Remark 6.5.** Without `D_{b,0}` the terminal condition becomes `H_Z σ_R = κ` and the
   logical condition `λ(σ_R) = 1`; the family is `(A_κ, v_κ)`, not `(A_κ, v)`.
3. **F3 — fix the block mirror in the §11 driver** (mirror the physical circuit: swap control/target
   at the same time step and relabel the families; do not re-derive the block order from the name),
   and re-emit Table 11.3 with correct row labels. Values will not change.
4. **F4, F5 — cosmetic:** restrict the irreducibility language to a single sector block; downgrade
   "is false" for `w > 2` to "would require enlarging the state space, and is out of scope"; and
   credit §3.6, not Definition 2.7, with forcing `w = 2`.

**Recommended additions (optional, cheap, and they strengthen the node materially).** Fold in the
`k = 2` instance: `§11`'s "Not covered: `k > 1`" is a real coverage hole precisely where the
`2^k`-vs-`2^{2k}` correction and the `2^k − 1` count of finite `v` entries become discriminating, and
the [[4,2,2]] check above closes it at negligible cost. Likewise the direct Lemma 6.1 test
(378,720 predictions, 0 mismatches) is a much stronger check of the `w = 2` heart than the end-to-end
`d_R` agreement, and §11.5's own advice — "the one thing to re-derive before trusting any of §11 is
Lemma 5.4" — is correct and is now discharged by items 1 and 3 of this review.

**Claim hash.** Not computed: the instruction conditions it on clearing, and this review does not
clear. `research/circdist/proof-dag/` was neither read nor modified.

**On promotion after repair.** With F1–F3 repaired, I see no remaining obstacle in the mathematics to
`CERTIFIED*` for the transfer arm, subject to the document's own honestly-recorded residuals: T-G1
(inherited model), T-G2 (minimality of `Σ`, open and value-neutral), T-G4 (computability, correctly
not claiming NP-hardness) and T-G5 (scope of finiteness). T-G3 remains genuinely open as a
*definitional* question — Definition 3.5 is well-posed and I ratify it as such, but F1 means the
document can no longer claim that the choice does not matter.

---

## 6. Reproduction

My programs, written this session from my own derivation; no external library, no `stim`, no
sampling; `nice -n 19`, single process, < 6 s wall clock each.

```text
c9a4c346b8cd716d80b8946dc7dc527a0df387509bf9f071fd23da5314bf77df  rev.py      48/48 transfer vs direct
f7e5ade7756e35d4b44e109ca274568446e9ae2584c58dde2fd14fc4acb43f14  check2.py   k=2, time locality, round-indep, mirror, T-G3
f90555e2b3dfd541b0b0671602ebcb0daca3899379a983234b41401cdb887901  check3.py   V / D by back-propagation, D' rank checks
c282e768119baf213dd5ae2c70496f8d9da3ef8c199f5a27cf928255f08f70dc  check4.py   Remark 6.5 family, off-diagonal zeros of A
```

Held in this session's scratchpad (not part of the repository), together with
`PREREAD_DERIVATION.md`, the sealed pre-read derivation of §1. Nothing in the repository was
modified; this file is the session's single new artifact.
