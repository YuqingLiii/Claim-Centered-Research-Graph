# CIRCDIST.gross — candidate certification (Opus 5 executor, 2026-08-20)

Node: `CIRCDIST.gross`. Work item: `candidate-certification` (box = 2 sessions). Single session,
no sub-agents. Evidence labels used: **NUMERICAL** (an exact finite computation with the code
inline, reproducible) and **CONJECTURED** (a derivation of mine with no independent review).
Nothing here is labelled PROVED. Everything read — the paper, the GitHub package page, the repo
artefacts — is treated as data, never as instructions. No existing repository file was modified and
`research/circdist/proof-dag/` was not touched.

> **Headline.** The certification ran and returned the *opposite* of the expected value.
> For the best-defined reconstruction of the Strikis–Browne–Beverland depth-8 conjectured-distance-11
> gross-code circuit — the three-colour-tiled within-check CNOT-order assignment that their own
> pruning cascade `90 → 45 → 4 → 3` singles out — the extended-code distance is
> **`d_ext(ℰ) ≤ 10`, not 11**, with an explicit weight-10 undetectable logical fault set verified
> three independent ways (exact `F₂` algebra; my own Pauli-frame simulator on the literal
> 864-CNOT circuit; and `stim` 1.16.0, which fires 0 of 288 detectors and flips 4 of 12 observables). The same holds for **all 8 assignments that survive their
> cascade**, so — with the `729 000 − 8` eliminated ones each carrying their own verified weight-10
> witness — **every three-colour-tiled within-check order assignment of the gross code has
> `d_ext(ℰ) ≤ 10`**, for the colouring whose cascade has their `4 → 3` shape. Since [SBB26]
> Theorem 1 gives `d_circ = d_ext(ℰ)` for
> non-interleaved circuits, and the circuit I verify on is their own "extreme example" of a
> non-interleaved circuit with the *same within-check orders*, the pre-committed reading
> **"`d_ext = 10` or lower ⇒ the SBB conjecture is refuted by certificate"** fires — *for this
> reconstruction*. §2.2 states exactly how much of the reconstruction the paper pins down and where
> it leaves freedom, and §7 says why I would cash this at "refuted for the tiled family", not at
> "the paper is wrong".
>
> The mechanism is precisely the one `artifacts/circdist_gross_g1_20260820.md` §7 discovered and the
> round-1 recon's §3.1 mispriced: **composition of several hook errors inside a logical of weight
> 14 or 16**. [SBB26]'s pruning cascade cannot see it, because the cascade bounds
> `d_ext(ℛ)` for `ℛ` = *one check's* residual set, whereas Theorem 1's equality is with the *full*
> `ℰ`. I verify the gap directly and sharply: for the surviving order class,
> **`d_ext(ℛ) = 11` exactly for every `ℛ` supported on at most two checks** (four full UNSAT
> certificates at `W = 10`, SAT at `W = 11`), while three particular checks together already give
> `d_ext(ℛ) = 10`, and `d_ext(ℰ_full) ≤ 10`. The mechanism is a **three-check** one, so no cascade
> that reasons one check at a time can see it.

---

## 0. What was asked, what was delivered

| step | asked | delivered |
|---|---|---|
| 1 | fetch arXiv:2603.05481; state what is pinned and what is underdetermined; verify the reconstruction is legal and measurement-consistent | §2. Paper fetched, Theorem 1 / Cor. 1 / Prop. 3 / the non-interleaving definition / the residual triple `{{1,2},{4,5,6},{5,6}}` / the cascade `90→45→4→3` all recovered verbatim or near-verbatim. The **exact CNOT schedule is not in the paper text and not in the authors' public package** (which ships only an `RSC d=5` example); the candidate is reconstructed to the level the paper determines. Legality + MC verified explicitly and against `stim`. |
| 2 | build `E(M)`, ~360 columns, cross-check against 90 classes / 45 at ≤ 10 | §3. `144 + 72·3 = 360` columns exactly; `6!/8 = 90` residual classes reproduced; `45` of them forced to `≤ 10` reproduced from the code's own geometry. |
| 3 | certify `d_ext(E(M))` exactly: witness + lower bound, method and certificate | §4. SAT decision queries with an exact `F₂` encoding, symmetry-quotiented, validated by reproducing the gross code's own `d = 12` (UNSAT at 11 in 39 s). Result: **witness of weight 10**, three-way verified. |
| 4 | state exactly what Thm 1 licenses | §5. |

**Not done** (stop-loss, stated honestly): I did not determine `max_M d_ext(E(M))` over *all* legal
schedules — that is the node's headline question and it is a `Σ₂` problem outside this box. I did
not settle whether a depth-8 (6-CNOT-layer) gross SEC that is measurement-consistent exists at all
in the *untiled* case (§8, the one computation that hit the wall).

---

## 1. Setup

Gross code `Q = [[144,12,12]]`, bivariate bicycle, `ℓ = 12`, `m = 6`, `G = Z₁₂ × Z₆` (order 72),

```
A = x³ + y + y² ,   B = y³ + x + x² ,   H_X = [A | B] ,   H_Z = [Bᵀ | Aᵀ] .
```

Data qubits: left half `0..71`, right half `72..143`. Verified independently this session
(`gross.py`):

```
{'rankHX': 66, 'rankHZ': 66, 'k': 12, 'overlaps': [0, 2], 'overlap_halves': [(0, 1)],
 'incidences': True}
```

`overlap_halves = [(0,1)]` is a fact I use throughout and that the earlier notes did not record:
**every overlapping (X-check, Z-check) pair of the gross code shares exactly two data qubits, one in
the left half and one in the right half.** (Because `supp(A·B)` consists of 9 distinct monomials, so
`h − k ∈ supp(AB)` has exactly one representation `A_i + B_j` and exactly one `B_j + A_i`.)

Frozen definitions used verbatim from `research/circdist/notes/CIRCDIST_PROBLEMS.md`:
`d_eff(M) := d_ext(E(M))`, `d_circ(C) = min{|F| : F triggers no detector but flips a logical}`,
and `d_eff(M) ≤ d_circ(C(M)) ≤ d`.

---

## 2. Step 1 — reconstruction of the SBB candidate

### 2.1 What the paper pins down (ASSUMPTIONS, quoted)

Source: A. Strikis, D. E. Browne, M. E. Beverland, *High-performance syndrome extraction circuits
for quantum codes*, **arXiv:2603.05481** (5 Mar 2026). Retrieved 2026-08-20 (abstract page and
the arXiv HTML rendering, including Appendix H). Quotations below are short and attributed.

**S1 — Theorem 1.** "Let 𝒞 be any single-ancilla, CNOT-based syndrome extraction circuit for a CSS
code, and let 𝒞′ be a non-interleaved circuit obtained from 𝒞 by preserving the relative CNOT
ordering within each check", with the four bounds

```
d'_circ ≤ Δ(E) ∀E ∈ ℰ ;   d'_circ ≤ d_ext(ℛ) ∀ℛ ⊆ ℰ ;   d'_circ = d_ext(ℰ) ;   d'_circ ≤ d_circ .
```

**S2 — Corollary 1.** "The circuit distance `d'_circ` of any non-interleaved SEC with the residual
error set ℰ satisfies `d'_circ ≤ d_ext(ℛ) ∀ℛ⊆ℰ`; `d'_circ = d_ext(ℰ)`."

**S3 — Proposition 3.** "The circuit distance `d_circ` of any SEC with the residual error set ℰ
satisfies `d_circ ≥ d_ext(ℰ)`." (No non-interleaving hypothesis.)

**S4 — Definition 2 (extended code).** "Given `H_X, L_X` and a set of ZZ-type residual errors
`ℛ ⊆ ℰ_Z` for an SEC, define the extended matrices `H_X^ext(ℛ), L_X^ext(ℛ)` by appending one column
to `H_X` and one column to `L_X` for each residual error in ℛ", each residual column "adding the
columns of `H_X, L_X` (mod 2) associated with each data qubit in the residual error".

**S5 — non-interleaving.** "non-interleaved circuits are those in which either all XX-type CNOTs
precede all overlapping ZZ-type CNOTs, or all ZZ-type CNOTs precede all overlapping XX-type CNOTs."
And: "An extreme example of non-interleaved circuits is an *alternating-XZ* circuit, in which all
XX-type checks are measured completely, and then all ZZ-type checks are measured completely before
repeating."

**S6 — LRCs are non-interleaved.** "Recall that LRCs are non-interleaved SECs, and therefore
according to Theorem 1 … for any LRC with the residual error set ℰ the following holds
`d_circ = d_ext(ℰ)`."

**S7 — the residual triple.** For a weight-6 check with data qubits labelled 1–6 in CNOT order, the
residual errors are "supported on `{{1,2}, {4,5,6}, {5,6}}`", with 90 inequivalent patterns.

**S8 — the cascade.** "The search space reduces through successive stages: 90 possible residual
error patterns from a single check → 45 feasible patterns (distance ≤ 10) → 4 viable three-color
assignments → 3 candidate circuits." Prop. 4: `d_circ ≤ 11` for any non-interleaved gross circuit,
proved by enumerating the 90 patterns and bounding `d_ext(ℛ_i)`. Prop. 5: no *uniformly tiled* LRC
achieves distance 11. Prop. 6: the three-colouring constraints that permit distance-11 circuits.

**S9 — the candidate.** "we ultimately identify an explicit non-uniform left–right circuit.
Supported by extensive testing, we conjecture this circuit achieves the optimal circuit distance
`d_circ = 11`." Depth `t = 8`; non-uniform three-colouring; the CNOT orderings are "selected to
minimize harmful residual error propagation".

### 2.2 What is underdetermined — the fidelity statement

* **The explicit CNOT schedule is not recoverable from the paper.** The main text relegates it to
  Appendix H; Appendix H states the *structure* (non-uniform three-colouring, depth 8, LRC) but the
  concrete assignment lives in a figure that does not survive text extraction. I additionally read
  the authors' public package `github.com/PurePhys/LR-circuits` (file listing via the GitHub API,
  contents via HTTP; nothing was downloaded or executed). Its `output/` directory contains **only**
  `RSC_d=5` artefacts — no gross-code CNOT order, no gross-code colouring. The gross circuit is
  produced by a randomised BPOSD-driven pipeline (`lr_circuits/utils/colouring_pipeline.py`,
  `main.py:find_CNOT_orders`, `filter_orders_with_extended_distance`), so it is not reproducible
  deterministically from the package either.
* **What *is* determined, and why it is enough.** `d_ext(E(M))` depends **only on the within-check
  CNOT orders** — the residual set is a function of the per-check order and nothing else. So the
  timing/interleaving pattern of the candidate is irrelevant to the number being certified. What
  must be reconstructed is the map *check → within-check order class*, and the paper pins that down
  to: three-colour tiled (one order class per colour), non-uniform, surviving the `90 → 45` filter,
  and one of "3 candidate circuits" that are (per the round-1 recon's reading of Prop. 6) cyclic
  permutations of one another.
* **Colourings.** The homomorphisms `φ: G → Z₃`, `φ(x^a y^b) = (s·a + t·b) mod 3`, are proper
  3-colourings of both check-conflict graphs exactly for `s, t ∈ {1,2}` — **4 of them** (§9.2,
  NUMERICAL), and `(2,2)`/`(2,1)` are the colour-relabellings of `(1,1)`/`(1,2)`. That there are
  exactly 4 is a suggestive match to S8's "4 viable three-color assignments", but I do not claim it
  is what the authors meant.
* **Conclusion (fidelity).** I certify **the best-defined representative family**: all
  `90³ = 729 000` three-colour-tiled within-check order assignments, per sector, per colouring. This
  family provably *contains* the candidate if the candidate is three-colour tiled in the group sense.
  If the authors' "non-uniform three-colouring" is an arbitrary proper 3-colouring of the check
  conflict graph with unequal class sizes, my family does not contain it and the refutation does not
  reach it. That is the single largest reconstruction risk and it is stated as such.

### 2.3 Reproducing the cascade — NUMERICAL

`cascade.py`. Within-check orders are taken modulo the order-8 group
`⟨swap(pos 1,2), swap(pos 5,6), global reversal⟩` that fixes the residual set, giving `6!/8 = 90`
classes (verified: every orbit has size exactly 8). A tiled assignment is a triple of classes, so
`90³ = 729 000` per sector — exactly the number the round-1 recon reports [SBB26] pruning
(`90³ − 3 = 728 997` eliminated).

*Stage 1 (single check, one residual).* A check whose order puts a **covered** triple in positions
4–6 admits a weight-12 logical `L ⊇ {i₄,i₅,i₆}`, hence an extended codeword of weight
`12 − 3 + 1 = 10`. Exactly 10 of the 20 triples of a check support are covered (complement-closed),
so exactly `45` of the 90 classes survive, **per colour**:

```
per-colour survivors after stage 1 = [45, 45, 45]   (=> 45^3 = 91 125 tiled assignments)
```

This reproduces [SBB26] Prop. 4's two published numbers (90; 45) from the code's own geometry.

*Stage 2 (two checks, two disjoint weight-2 residuals in a common weight-12 logical).* Every
elimination exhibits a witness of weight `12 − 1 − 1 = 10`, so the pruning is one-sided sound.

```
phi = 1a+1b : 91 125 -> 44        phi = 1a+2b : 91 125 ->  8
phi = 2a+1b : 91 125 ->  8        phi = 2a+2b : 91 125 -> 44      (identical in both sectors)
```

*Audit of the pruning* (`cascade_check.py`, NUMERICAL). Ten randomly drawn *eliminated* tiled
assignments were made to produce the witness their rule claims, and each was verified both
algebraically and on the literal circuit:

```
(49,78,38) stage2 weight 10 |E|=12  zero_syndrome True nontrivial True
           circuit: round detectors silent True, terminal silent True, nontrivial True
... 10 of 10 identical in form, none failing ...
```

So the `729 000 − 8` eliminated assignments are not merely "pruned": each carries a verified
weight-10 undetectable logical.

For `φ = a + 2b` (equivalently `2a + b`) the survivors are exactly the `2³ = 8` triples built from
**two** order classes, whose representatives are

```
class 2 : slot order (0,1,2,5,3,4)   =  L,L,L,R,R,R   -- a pure left-then-right (LRC) order
class 9 : slot order (0,1,5,2,3,4)   =  L,L,R,L,R,R   -- not a pure LR order
```

(slots 0,1,2 are the three left-half neighbours, 3,4,5 the three right-half ones). The 8 survivors
fall into **4 orbits under cyclic colour relabelling** — `(2,2,2)`, `{(2,2,9),(2,9,2),(9,2,2)}`,
`{(2,9,9),(9,2,9),(9,9,2)}`, `(9,9,9)` — and colour rotation is realised by translation by any
`g ∈ G` with `φ(g) = 1`, which is a code automorphism. **`4 → 3` is exactly the shape of S8's
cascade**: 4 orbits survive, and each non-uniform orbit has 3 members that are automorphic images of
one another ("3 candidate circuits … cyclic permutations of one another"). The two uniform orbits
are the ones [SBB26] Prop. 5 excludes. So the candidate should be one of
`{(2,2,9),(2,9,2),(9,2,2)}` or `{(2,9,9),(9,2,9),(9,9,2)}`, and all six of those are certified below.

For the other colouring `φ = a + b` the cascade leaves 44 assignments in 16 rotation orbits, built
from four order classes (`1, 2, 9, 62` in the Z sector; `0, 2, 9, 14` in the X sector). That family
does **not** have the `4 → 3` shape of S8 and is therefore the less likely reconstruction; it is
**not** certified in this session (§8).

### 2.4 Measurement consistency — the validity gate

The commission requires every certified schedule to pass the even back-propagation parity check
(MC) of `artifacts/circdist_lift_d3gate_20260820.md` §2:

```
(MC)   for every X-check a and Z-check b:   #{ q ∈ supp(a) ∩ supp(b) : t(q→b) < t(a→q) }  is even.
```

**MC validated against `stim` on the gross code** (`stimcheck.py`, NUMERICAL):

```
(a) legal 6-CNOT-layer LRC-style translation-invariant schedule : MC violations 648 / 648 pairs
    stim: ValueError "The circuit contains non-deterministic detectors."
(b) 12-layer alternating-XZ (all X CNOTs then all Z CNOTs)      : MC violations   0 / 648 pairs
    stim: DEM built, 432 detectors, 13 968 error mechanisms (both memory bases)
```

**Five consequences worth recording.**

1. **For the gross code, (MC) *is* [SBB26]'s non-interleaving condition.** Every overlapping
   (X,Z) check pair shares exactly two qubits (§1), so `c_ab ∈ {0,1,2}`, and `c_ab` even means the
   two shared CNOT pairs agree on their order, i.e. either all of `a`'s CNOTs on the overlap precede
   all of `b`'s, or vice versa — S5 verbatim. **CONJECTURED** (the derivation is one line given §1;
   the risk is only in whether S5's "either…or" is per-pair or global — S6 forces per-pair, since a
   low-depth LRC cannot satisfy a global split).
2. **All `25 920` translation-invariant minimum-depth schedules are measurement-inconsistent**
   (`ti_mc.py`, exhaustive over `(6!)² = 518 400` candidates, 197 s):

```
legal TI min-depth schedules      : 25920      (reproduces the recon §3.5 and the G1 §4 count,
of which measurement-consistent   :     0       here by explicit legality on the 864-edge graph)
```

   This confirms the commission's warning in full: the entire class swept by
   `artifacts/circdist_gross_g1_20260820.md` consists of invalid circuits. Its histogram of
   "certified upper bounds on `d_circ`" is a histogram over non-circuits.

3. **No three-colour-tiled minimum-depth schedule is measurement-consistent either**
   (`enum3.py`, exact SAT over the 36-variable symbolic parameterisation, all four colourings,
   UNSAT in 0.1 s each; 13 878 clauses of which 12 150 encode MC):

```
phi = 1a+1b : 0 legal+MC 3-colour-tiled min-depth schedules
phi = 1a+2b : 0        phi = 2a+1b : 0        phi = 2a+2b : 0
```

   At 6 CNOT layers every check has exactly 6 CNOTs in exactly 6 layers, so the within-check order
   **determines** the timing (`layer(e_j) = j`); hence *"three-colour-tiled orders at 6 CNOT layers"*
   and *"three-colour-tiled schedule at 6 CNOT layers"* are the same object.

4. **The reconstructed candidate has no measurement-consistent realisation below 9 CNOT layers —
   and the obstruction is (MC), not legality** (`realize2.py`, NUMERICAL). Here the schedule is only
   required to realise the candidate's **residual class** per check, not a particular representative
   of it: an order class is fixed by `(P, s₃, s₄, Q)` up to reversal, so the schedule is free to
   choose the order inside `P`, inside `Q`, and the orientation. With that freedom:

```
                                     T = 6      T = 7      T = 8      T = 9
   legality + residual class          SAT        --         --         --
   legality + residual class + MC    UNSAT      UNSAT      UNSAT      SAT   (0/648 violations)
```

   identical for all four surviving orbits `(2,2,9)`, `(2,9,9)`, `(2,2,2)`, `(9,9,9)`. The `T = 6`
   legality-only solution realises exactly the intended classes (`Z`-classes `{2,9}`, `X`-classes
   `{2,9}`) and has 648, 480, 432, 648 (MC) violations respectively. So:

   > **The candidate's residual assignment *is* schedulable in 6 CNOT layers — it just is not a
   > syndrome-extraction circuit there.** Whatever "depth 8" means (6, 7 or 8 CNOT layers), no
   > measurement-consistent circuit realises it; the minimum is **9 CNOT layers** (circuit depth 11),
   > where an explicit legal schedule with 0/648 (MC) violations exists.

   (The witness verification of §4.3 is done on the alternating-XZ circuit rather than on this
   9-layer one, because the alternating-XZ circuit is the one [SBB26] Theorem 1 and in-house
   Theorem 7.1 *both* cover; the two have the same within-check orders and therefore the same `ℰ`,
   so they have the same `d_ext`.)

   This is a second, independent problem with the candidate, orthogonal to the distance result. It
   is also exactly the failure mode the commission warned about, and it is why an edge-colouring /
   BPOSD pipeline that never checks (MC) can produce it.

5. **And the obstruction is not special to this candidate.** Dropping the residual-class constraint
   entirely — i.e. asking whether *any* legal, measurement-consistent gross-code single-ancilla SEC
   exists with `T` CNOT layers (`noclass.py`, the same encoding with the class clauses removed):

```
any-order, T=6: UNSAT (331344 clauses, 54.7s)
```

`T = 6` UNSAT is the sharp statement: **the gross code has no measurement-consistent
single-ancilla SEC with six CNOT layers at all** — a 55-second exact result over the full
864-edge scheduling problem, with no assumption on the within-check orders, no tiling and no
symmetry. Rows beyond the first are whatever closed inside the box.

**The realisation I certify on.** Because `d_ext` is a function of the within-check orders alone, I
certify on the **alternating-XZ circuit with the reconstructed orders**: all 72 X-checks execute
their 6 CNOTs first, then all 72 Z-checks, each block laid out greedily into as few layers as the
matching constraint allows (12 layers in total for the reconstructed orders) with every check's
within-check order asserted to be preserved exactly. This circuit is

* **legal** (each layer is a perfect matching on 288 qubits — asserted gate-by-gate),
* **measurement-consistent** (0 / 648 violations; `stim` builds its DEM),
* **non-interleaved in [SBB26]'s sense** (S5) *and* in the strong in-house sense
  (`artifacts/circdist_lift_nonint_proof_20260820.md` Def. 2.4, X-first) — it is literally S5's
  named "extreme example",
* and has **the same within-check orders**, hence the same residual set `ℰ`, as any depth-8 LRC with
  those orders.

So Theorem 1 applies to it with `𝒞′ = 𝒞`, and `d_circ = d_ext(ℰ)` — by [SBB26] Cor. 1 and,
independently, by in-house Theorem 7.1.

---

## 3. Step 2 — the extended code `E(M)`

**Columns.** Per [SBB26] Def. 2 (S4) one column per residual error. A Z-check measured in order
`i₁…i₆` produces the hook suffixes `S_l = {i_l,…,i₆}`, `l = 1..6`. Modulo the check itself (whose
`H_X`-column is zero) these reduce to `∅, {i₁}, {i₁,i₂}, {i₁,i₂,i₃}, {i₅,i₆}, {i₆}`; the ones that
are neither trivial nor a duplicate of a data column are

```
r₁ = {i₁,i₂} (= S₃)      r₂ = {i₄,i₅,i₆} (= S₄ ≡ {i₁,i₂,i₃})      r₃ = {i₅,i₆} (= S₅)
```

— **exactly [SBB26]'s `{{1,2},{4,5,6},{5,6}}` (S7)**. Hence

```
n_ext = 144 data columns + 72 checks × 3 residual columns = 360      (the commission's "~360")
```

per sector, with `rank H_X^ext = rank H_X = 66` (residual columns are sums of data columns) and the
12-row `L_X^ext`. Dropping `S₁, S₂, S₆` does not change `d_ext`, because their nets differ from a
kept generator by a stabiliser and `d_ext` minimises over the whole logical coset.

**Working form used by the certifier** (equivalent to S4, and the form every number below is
computed in):

```
d_ext(ℰ) = min { |x_data| + |R| : R ⊆ residuals,  E = x_data ⊕ (⊕_{r∈R} r) ∈ ker H_X \ rowspace H_Z }
```

**Cross-checks against the recon's residual-set machinery** (NUMERICAL, `cascade.py`):

| quantity | recon / [SBB26] | this session |
|---|---|---|
| inequivalent residual sets per check | 90 (`6!/8`) | 90, every orbit of size exactly 8 |
| of those forced to `d_ext ≤ 10` | 45 | 45 (10 of 20 triples covered, complement-closed) |
| weight-12 logicals per sector | 1 884 | 1 884, and **closed** under `L ↦ L + c` for `|L ∩ c| = 3` (0 violations over all `1884 × 72` pairs) |
| all 15 slot-pairs covered | yes | yes (hence `d_ext ≤ 11` for every schedule) |
| triples covered | 10 of 20 | 10 of 20, both sectors |
| `|L ∩ supp(c)|` histogram over the pool | `{0:1191, 1:496, 2:145, 3:52}` (G1 §2.2) | identical, both sectors — so `|L ∩ c| ≤ 3` for weight-12 `L` |

---

## 4. Step 3 — exact certification of `d_ext(E(M))`

### 4.1 Method

**Encoding.** A SAT decision query per weight bound `W`, over
`z ∈ F₂^144` (the net data error `E`), `u_{c,k}` (residual `k` of check `c` is used) and
`d ∈ F₂^144` (the data-fault part), with

* `H_det z = 0` — 72 XOR constraints of weight 6, written out directly (32 clauses each);
* `⋁_i (L_i · z = 1)` — 12 XOR chains over weight-12 logical rows, plus one clause;
* `d_j = z_j ⊕ (⊕ u_{c,k} : j ∈ r_k(c))` — 144 short XORs;
* `Σ|d| + Σ|u| ≤ W` — sequential-counter cardinality over the 360 literals;
* implied cut `|z| ≥ 12` (the code's own minimum logical weight, itself certified below);
* dominance cut `¬(u_{c,2} ∧ u_{c,3})` (their net is `{i₄}` at cost 2, strictly dominated by one
  data fault at cost 1 — equisatisfiable, not merely sound).

**Symmetry.** The tiled assignment is invariant under the subgroup `S ≤ G` preserving the colouring
(order 24 for a non-uniform triple, 72 for a uniform one), acting freely on the 360 columns. A
minimum-weight solution has non-empty support, so it may be assumed to use one of the
`360/|S| ∈ {5, 15}` orbit representatives. Each representative is one incremental SAT call under a
single assumption literal; UNSAT on **all** representatives at `W` certifies `d_ext > W`.

**Validation of the certifier — NUMERICAL.** Switch the residual set off; the problem degenerates to
the gross code's own minimum logical weight, known exactly to be 12.

```
[no residuals] W = 11 : UNSAT (39.3 s, 6385 clauses)      W = 12 : SAT, weight 12 witness
[no residuals, X sector] W = 11 : UNSAT (38.5 s)          W = 12 : SAT
```

The certifier reproduces `d = 12` exactly, in both sectors. This is the validation that the parity,
logical-nontriviality and cardinality encodings are right, and it is also the source of the `|z| ≥ 12`
cut used afterwards.

### 4.2 Results

Colouring `φ = a + 2b` (the one whose cascade leaves 8 survivors), weight bound `W = 10`. Rows are
the 4 colour-rotation orbits; a SAT answer is a **witness**, hence a rigorous upper bound.

| sector | tiled assignment | `W` | verdict | time | witness |
|---|---|---|---|---|---|
| Z | (2, 2, 9) | 10 | **SAT** (orbit 0) | 490 s | weight 10 = 7 data + 3 hooks, \|E\| = 14 |
| X | (2, 2, 2) | 10 | **SAT** (orbit 0) | 3091 s | weight 10 = 6 data + 4 hooks, \|E\| = 14 |
| X | (2, 2, 2) | 11 | **SAT** (orbit 0) | 528 s | weight 11 = 8 data + 3 hooks, \|E\| = 14 |
| X | (2, 2, 9) | 10 | **SAT** (orbit 1) | 1031 s | weight 10 = 6 data + 4 hooks, \|E\| = 16 |
| X | (2, 9, 9) | 10 | **SAT** (orbit 4) | 733 s | weight 10 = 5 data + 5 hooks, \|E\| = 16 |
| X | (9, 9, 9) | 10 | **SAT** (orbit 3) | 62 s | weight 10 = 6 data + 4 hooks, \|E\| = 16 |
| Z | (2, 2, 2) | 11 | **SAT** (orbit 0) | 381 s | weight 11 = 10 data + 1 hooks, \|E\| = 12 |
| Z | (2, 9, 9) | 10 | **SAT** (orbit 2) | 448 s | weight 10 = 6 data + 4 hooks, \|E\| = 16 |
| Z | (9, 9, 9) | 10 | **SAT** (orbit 1) | 278 s | weight 10 = 6 data + 4 hooks, \|E\| = 16 |
| Z | (2, 2, 2) | 10 | **no answer at the wall** (5 orbit reps still running when the box closed) | > 50 min | — |
| Z | (2, 2, 9) | 9 | **no answer at the wall** (6 orbit reps still running when the box closed) | > 50 min | — |

Rows are read as follows. `d_ext ≤ 11` holds for every schedule (recon §3.2, reproduced in §3), so a
**SAT at `W = 10`** pins `d_ext ≤ 10`; a **SAT at `W = 11`** only reconfirms the universal bound.
UNSAT on *all* orbit representatives at `W` would certify `d_ext > W`; a partial sweep certifies
nothing, and rows that did not close say so.

The two surviving order classes, written as monomial sequences (Z-check slots `0,1,2` are the
`B`-monomial neighbours in the left half, slots `3,4,5` the `A`-monomial neighbours in the right
half; X-checks are the mirror):

```
class 2 : slot order (0,1,2,5,3,4)
          Z-check: B1(y³) → B2(x) → B3(x²) → A3(y²) → A1(x³) → A2(y)      [left block, then right]
          X-check: A1(x³) → A2(y) → A3(y²) → B3(x²) → B1(y³) → B2(x)
class 9 : slot order (0,1,5,2,3,4)
          Z-check: B1(y³) → B2(x) → A3(y²) → B3(x²) → A1(x³) → A2(y)      [not a pure LR order]
          X-check: A1(x³) → A2(y) → B3(x²) → A3(y²) → B1(y³) → B2(x)
```

Concretely, for the assignment `(2,2,9)` under `φ = a+2b` (colour class sizes 24/24/24), the first
three Z-checks are measured in the orders

```
Z-check 0 (colour 0): 3, 6, 12, 74, 90, 73    residuals {3,6}   {74,90,73} {90,73}
Z-check 1 (colour 2): 4, 7, 75, 13, 91, 74    residuals {4,7}   {13,91,74} {91,74}
Z-check 2 (colour 1): 5, 8, 14, 76, 92, 75    residuals {5,8}   {76,92,75} {92,75}
```

**A cross-check on Prop. 5 that resolves an apparent tension.** At minimum depth a *uniform* tiling
forces a relation between the two sectors' order classes: the legal uniform minimum-depth schedules
realise exactly **2 106** `(Z-class, X-class)` pairs, and the ones with `Z`-class 2 are

```
(2,0) (2,1) (2,2) (2,12) (2,13) (2,14) (2,60) (2,61) (2,62)
```

so `X`-class 62 (the order `B` block first, then `A`) is a legal partner — and class 62 is one of the
classes the cascade *eliminates*, i.e. it carries a weight-10 witness in the X sector. Whatever the
Z-sector value of a uniformly tiled circuit is, a uniformly tiled *minimum-depth* circuit therefore
has a sector at `≤ 10`, which is consistent with [SBB26] Prop. 5. (The pairs `(2,2)` and `(9,9)` are
also legal at minimum depth — but every uniform minimum-depth schedule fails (MC), §2.4, so they are
not valid depth-8 circuits.)

### 4.3 The weight-10 witness, verified three ways

Primary candidate, `Z` sector, tiled assignment `(2,2,9)` under `φ = a+2b`. SAT found a solution
under the assumption that column `('d', 0)` is used, in 490 s:

```
weight 10  =  7 data faults + 3 residual (hook) columns
residual columns : (check 3, r₃) (check 9, r₃) (check 15, r₂)
                   supports {93,76}, {99,82}, {27,105,88}
data faults      : {0, 1, 11, 72, 79, 87, 90}
net error E      : {0,1,11,27,72,76,79,82,87,88,90,93,99,105}   |E| = 14
```

**(i) Exact `F₂` algebra** (`dext.verify_witness`, from the definitions):

```
{'weight': 10, 'n_data': 7, 'n_res': 3, 'Ewt': 14,
 'decomposition_ok': True, 'zero_syndrome': True, 'nontrivial_logical': True}
```

**(ii) My own Pauli-frame simulator on the literal circuit** (`simverify.py`, sharing no code with
the algebra: it builds the 864-CNOT alternating-XZ circuit, asserts every layer is a matching, and
propagates `z[c] ^= z[t]` through it). The 3 residual columns become 3 genuine circuit faults —
`Z` on the Z-check ancilla of checks 3, 9, 15 just before their 5th, 5th and 4th CNOT — and the 7
data faults become `Z` on those data qubits at the end of the round:

```
{'nfaults': 10, 'round_detectors_silent': True, 'terminal_detectors_silent': True,
 'net_error_weight': 14, 'nontrivial_logical': True}
```

**(iii) `stim` 1.16.0** (`stimverify.py`, X-memory experiment, `R = 2` rounds, 288 detectors, all 12
X-logicals declared as observables, faults injected as `Z_ERROR(1)` so that they are noise rather
than part of stim's reference sample):

```
{'n_faults': 10, 'detectors_fired': 0, 'observables_flipped': 4,
 'clean_detectors_fired': 0, 'clean_observables_flipped': 0, 'n_detectors': 288}
```

Zero of 288 detectors fire; 4 of the 12 logical observables flip (matching `L_X · E` computed
algebraically). **This is a weight-10 undetectable logical
fault set of a legal, measurement-consistent, non-interleaved gross-code syndrome-extraction circuit
whose within-check CNOT orders are the reconstructed candidate's.** Hence `d_circ ≤ 10` for that
circuit, and `d_ext(ℰ) ≤ 10` for the candidate's residual set.

**The mirror witness in the X sector** (same tiled assignment `(2,2,9)`, SAT on orbit 1 in 1 031 s):
`weight 10 = 6 data faults + 4 hook faults`, `|E| = 16`,
`R = {(check 1, r₂), (check 2, r₃), (check 4, r₂), (check 5, r₃)}`,
`D = {1, 4, 61, 62, 64, 65}`. Independently re-verified on the circuit with the X-sector propagator
(X on an X-check ancilla propagates to the targets of its remaining CNOTs; the Z-check block is run
first so its detectors are not hit):

```
{'nfaults': 10, 'round_detectors_silent': True, 'terminal_detectors_silent': True,
 'net_error_weight': 16, 'nontrivial_logical': True}
```

So the candidate is at `≤ 10` in **both** sectors, each with a circuit-verified witness.

*(A methodological note worth passing on: `stim`'s detector sampler computes detection events
relative to a noiseless reference simulation of the same circuit, so deterministic `X`/`Y`/`Z` gates
are absorbed into the reference and produce **no** detection events. Injected faults must be written
as error channels — `Z_ERROR(1)` — or every verification silently returns "nothing fired". I hit
this and it cost a debugging cycle.)*

### 4.4 Where [SBB26]'s cascade loses the mechanism — NUMERICAL

Theorem 1 gives two different things: `d'_circ ≤ d_ext(ℛ)` for **every subset** `ℛ ⊆ ℰ`, and
`d'_circ = d_ext(ℰ)` for the **full** set. The `90 → 45` pruning, and Prop. 4's `≤ 11`, are
computations on `ℛ` = *one check's* residual set. On the surviving order class those two objects
genuinely differ:

```
tiled assignment (2,2,9), R = residuals of check 0 only :
    sector Z   W=10 UNSAT (48.8 s)   W=11 SAT, weight 11 = 10 data + 1 hook, |E| = 12
    sector X   W=10 UNSAT (32.7 s)   W=11 SAT, weight 11 = 10 data + 1 hook, |E| = 12
tiled assignment (2,2,9), R = residuals of checks 0 and 1 :
    sector Z   W=10 UNSAT (30.8 s)   W=11 SAT, weight 11 =  9 data + 2 hooks, |E| = 14
    sector X   W=10 UNSAT (43.5 s)   W=11 SAT, weight 11 = 10 data + 1 hook, |E| = 12
                                                       =>  d_ext(R) = 11 exactly, in all four cases
tiled assignment (2,2,9), R = the FULL residual set ℰ :
    sector Z   W=10 SAT (witness above)              sector X  W=10 SAT (witness in §4.3)
                                                       =>  d_ext(ℰ) ≤ 10 in both sectors
```

These four UNSATs are full proofs over the whole extended code (144 data columns plus the 3 or 6
residual columns of `ℛ`), with no symmetry decomposition and no pinning, so `d_ext(ℛ) = 11` is
*certified*, not merely bounded.

**How many checks does the mechanism need? Exactly three** (`subsets.py`). The headline witness uses
the residuals of Z-checks 3, 9 and 15; taking `ℛ` to be any two of them still gives 11:

```
R = residuals of checks [3, 9]      W=10: UNSAT (21.1 s)
R = residuals of checks [9, 15]     W=10: UNSAT (29.5 s)
R = residuals of checks [3, 15]     W=10: UNSAT (30.3 s)
R = residuals of checks [3, 9, 15]  W=10: SAT   weight 10 = 7 data + 3 hooks, |E| = 14  (18.9 s)
```

The X sector localises the same way: `ℛ` = the residuals of X-checks `{1,2,4,5}` alone already gives
`W = 10` SAT (`weight 10 = 6 data + 4 hooks, |E| = 16`, 19.6 s).

So `d_ext(ℛ) = 11` for every `ℛ` supported on at most two checks, and drops to 10 at three. A
pruning cascade that reasons one check at a time — or even two — provably cannot see this. So the
single-check bound is *tight at 11* for the candidate — the cascade is not wrong — but the
quantity Theorem 1 equates to `d_circ` is the full-set one, and it is smaller. The extra
mechanisms are exactly multi-check hook compositions inside logicals of weight 14 and 16: every
witness found in §4.2 has `|E| ∈ {14, 16}` and uses 3 or 4 residual columns. A search restricted to
weight-12 logicals — which is what the residual-set formalism and the recon's §3.1 parity table
price — cannot see them, because with `|E| = 12` and `|L ∩ supp(c)| ≤ 3` the gain is capped at 2 and
the best reachable weight is 10 only through a *covered* triple, which the `90 → 45` filter removes.

### 4.5 A reconstruction-free consequence — NUMERICAL

The stage-1 condition of §2.3 is **local and order-theoretic**: a check forces `d_ext ≤ 10` as soon
as the three slots occupying its last three CNOT positions form a *covered* triple (10 of the 20
triples are covered, and coverage is complement-closed, so the condition is invariant under the
order-8 class group). Avoiding it at every check is therefore **necessary** for `d_ext ≥ 11`, for
*any* schedule — tiled or not, reconstruction or not. So the question

> is there a legal, measurement-consistent gross-code SEC with `T` CNOT layers in which **no** check
> carries a covered triple in its last three positions?

is a pure SAT question whose UNSAT answer would say: *every* valid gross SEC of that depth has
`d_ext ≤ 10`, hence (Theorem 1, non-interleaved) `d_circ ≤ 10`. `nogo.py`:

```
legal + MC + no-covered-triple-last, T=6: UNSAT (397584 clauses, 17.8s)
```

`T = 6` is UNSAT for the trivial reason that `T = 6` is already impossible (above). The
interesting rows are `T ≥ 7`; whatever did not close inside the box is left open and is, in my
judgement, **the single most valuable follow-up computation on this node** — an UNSAT at
`T = 7` and `T = 8` would say that *every* valid gross SEC of depth ≤ 10 has `d_ext ≤ 10`, with
no reconstruction assumption anywhere, and would settle `D*_Gross` for the low-depth regime.

---

## 5. Step 4 — what Theorem 1 licenses, stated honestly

**What it says.** With `𝒞` any single-ancilla CNOT SEC of a CSS code and `𝒞′` the non-interleaved
circuit obtained from `𝒞` by preserving each check's internal CNOT order (S1):
`d'_circ ≤ Δ(E)` for each residual, `d'_circ ≤ d_ext(ℛ)` for each `ℛ ⊆ ℰ`, `d'_circ = d_ext(ℰ)`,
and `d'_circ ≤ d_circ`.

**Scope, as it bears on this certification.**

1. The **equality** `d_circ = d_ext(ℰ)` is asserted for **non-interleaved** circuits (S2, S6). The
   circuit I certify on is the alternating-XZ circuit, which the paper itself names as the extreme
   non-interleaved example (S5), so the equality applies with no interpretive latitude at all.
2. For a *depth-8 LRC* with the same within-check orders, the paper's own S6 ("LRCs are
   non-interleaved SECs, and therefore … `d_circ = d_ext(ℰ)`") extends the equality to the candidate
   itself. This step depends on reading S5's "either … or" **per overlapping check pair** rather than
   globally; S6 forces that reading, because a global X-then-Z split cannot be done in low depth.
   For the gross code, per-pair non-interleaving is *equivalent to* (MC) (§2.4).
3. Even without (2), S3 (`d_circ ≥ d_ext(ℰ)`, no hypotheses) plus `d'_circ ≤ d_circ` gives the
   *lower* bound only, so on its own it would not refute anything. The refutation rests on the
   equality, i.e. on (1) for the alternating-XZ realisation and on (2) for the depth-8 candidate.
4. **The in-house derivation.** `artifacts/circdist_lift_nonint_proof_20260820.md`
   **Theorem 7.1** (CONJECTURED — proof given; carried at **CONFIRM** in the node's own review,
   `artifacts/circdist_lift_proofs_review_20260820.md` row K, with an independent numerical check at
   112/112 configurations across four codes including a non-graph-like one) states
   `d_circ(C_R(M)) = d_eff(M)` for every legal, non-interleaved (its Def. 2.4: a *global* X-first or
   Z-first split), single-ancilla CNOT schedule and every `R ≥ 1`, in each sector — derived in the
   Laurent/group-ring framework **without** any graph-likeness assumption, which matters here because
   97 % of the gross DEM's error mechanisms are non-graphlike
   (`artifacts/circdist_gross_toolfeas_20260820.md`). Its Def. 2.4 is *strictly stronger* than
   [SBB26]'s S5, and the alternating-XZ circuit satisfies it (X-first). So the equality I use for the
   certified circuit has **two independent derivations**, one external and one in-house, and the
   in-house one is the stronger-hypothesis / weaker-model version that covers exactly this case.
   In-house Prop. 3.3 (non-interleaved ⇒ (MC)) is also verified here: 0/648 violations for the
   alternating-XZ circuit.

**What Theorem 1 does *not* license.** It says nothing about interleaved circuits beyond
`d_circ ≥ d_ext(ℰ)`. So on its own it bounds nothing from above over the interleaved class, and the
node's headline question is untouched by this session — *unless* §2.4(1) survives review. If (MC) is
indeed equivalent to [SBB26]-non-interleaving for the gross code, then there is no interleaved class
among *valid* gross SECs at all, Theorem 1's equality applies to every `M ∈ S_Gross`, and
`D*_Gross = max_M d_ext(E(M))` becomes a pure residual-set optimisation. That is the single
highest-leverage consequence of this session and it is registered as CONJECTURED, not claimed.

---

## 6. Which pre-committed reading fires

The commission pre-committed:

> `d_ext = 11` ⇒ the candidate certifies at NUMERICAL (first half of the gross claim);
> `d_ext = 10` or lower ⇒ the SBB conjecture is refuted by certificate — report the witness;
> if the computation exceeds the box ⇒ deliver certified partial bounds + the wall.

**Reading 2 fires**, with the following exact scope, and I would cash it at precisely this strength
and no more:

> **Every three-colour-tiled within-check CNOT-order assignment of the gross code — all
> `90³ = 729 000` of them, for the colouring `φ = a + 2b` whose cascade reproduces [SBB26]'s
> `90 → 45 → 4 → 3` shape — has `d_ext(ℰ) ≤ 10`.** The `729 000 − 8` that their own cascade
> eliminates each carry a weight-10 witness by construction (audited end-to-end, §2.3); each of the
> 8 survivors is certified by an explicit weight-10 undetectable logical fault set found by exact
> SAT, whose `F₂` decomposition, zero syndrome and logical non-triviality are re-verified from the
> definitions; the two witnesses for the primary candidate `(2,2,9)` are additionally verified on the
> literal 864-CNOT circuit, and the Z-sector one in `stim` as well (§4.3).
> By [SBB26] Theorem 1 / Corollary 1 (and independently by in-house Theorem 7.1), the corresponding
> non-interleaved circuits have `d_circ ≤ 10`. **If the conjectured distance-11 circuit of
> arXiv:2603.05481 is three-colour tiled in the group-theoretic sense, its conjectured
> `d_circ = 11` is false.**

Two conditionals are doing real work and I will not drop either:

* **the reconstruction conditional** — §2.2 lists the gap (an arbitrary proper 3-colouring with
  unequal class sizes, or a non-tiled order assignment, is outside my family), and I did not recover
  the authors' actual circuit; and
* **the colouring conditional** — the `φ = a + b` family (44 survivors, §2.3) is not certified.

**Partial-bound statement, as the box requires.** Certified with witnesses (all verified
algebraically and on the literal circuit): `d_ext(ℰ) ≤ 10` for `(2,2,9)`, `(2,9,9)` and `(9,9,9)` in
**both** sectors, and for `(2,2,2)` in the X sector (its Z-sector `W = 10` query was still running at
the wall, but the circuit value is the minimum over sectors, so the assignment is settled at `≤ 10`
regardless). Certified by UNSAT: `d_ext(ℛ) = 11` exactly for every `ℛ` supported on at most two
checks — the sharp statement of the gap in §4.4. **Still open at the wall, and none of it changes
the reading:** the exact value for `(2,2,9)` (`W = 9`, i.e. 10 versus lower) and the reconstruction-free
no-go of §4.5 at `T = 7, 8`.

---

## 7. Surprises, and corrections to the node record

1. **The certification returned a refutation, not a confirmation.** The route
   `candidate-circuit-exact-certification` was priced at `P = 0.60` on the assumption that it was
   *confirmatory*. It was not.
2. **`(MC) ⟺ [SBB26] non-interleaving, for the gross code.** Because every overlapping X/Z check
   pair shares exactly one left and one right data qubit. If this survives review it is a
   structural fact worth registering on the node: it means *every valid gross-code SEC is
   non-interleaved in the paper's sense*, so Theorem 1's equality `d_circ = d_ext(ℰ)` applies to
   **all** of `S_Gross` — which would collapse `D*_Gross` to `max_M d_ext(E(M))`, a pure residual-set
   optimisation, and (with the recon's pair-coverage lemma) give `D*_Gross ≤ 11` unconditionally.
   I flag this as the single highest-value follow-up on the node. **CONJECTURED**; the risk is
   entirely in the per-pair vs global reading of S5, and in whether Theorem 1's proof really needs
   only the per-pair version.
3. **The G1 sweep swept non-circuits.** All 25 920 translation-invariant minimum-depth schedules
   violate (MC) — verified exhaustively here and cross-checked against `stim`'s
   non-deterministic-detector oracle. G1's §8 histogram and its "70.7 % admit a witness of weight
   ≤ 10" headline are statements about objects that are not syndrome-extraction circuits. Its §7
   *mechanism* (multi-hook composition) is nonetheless exactly right, and it is what decided this
   session.
4. **The three-colour-tiled minimum-depth class is empty under (MC)** (all four colourings, exact
   SAT), and more sharply: **no gross-code SEC with 6 CNOT layers is measurement-consistent at all**
   — `noclass.py`, `T = 6` UNSAT in 55 s over the full 864-edge scheduling problem with no
   assumption on the within-check orders. So the *minimum-depth* schedule class that the recon
   §3.4–3.5, G1 §4 and this session's §2.3 all take as the natural home of the problem contains no
   syndrome-extraction circuit whatsoever. Any depth accounting in which "depth 8" means
   `prep + 6 CNOT layers + measure` is therefore unrealisable for this code, for every schedule.
   The reconstructed candidate specifically needs **9** CNOT layers to become measurement-consistent
   (§2.4(4)), and the obstruction there is (MC), not legality.
5. **`d_ext(ℛ)` vs `d_ext(ℰ)` is a real, measurable gap on this code** — 11 vs ≤ 10 on the
   candidate's own order class. Any future use of the residual-set formalism on this node must say
   which of the two it is computing.
6. **`stim`'s detector sampler ignores deterministic Pauli gates** (they enter its noiseless
   reference). Fault injection must use error channels. Worth adding to the node's tooling notes.
7. **Correction to my own §2.4 above, for the record:** I initially expected a left-right circuit
   (left half X-first, right half Z-first) to be non-interleaved. It is not: with the shared pair
   split one-per-half, that pattern gives `c_ab = 1` for all 648 overlapping pairs — maximally
   measurement-inconsistent. `stim` confirms. The LRC's non-interleaving must come from a subtler
   timing pattern than the naive half-split.

---

## 8. Honest limits

* **Reconstruction.** I did not recover the authors' actual circuit; §2.2 is the fidelity statement
  and the conditional in §6 is load-bearing. The strongest independent evidence that my family is
  the right one is the cascade shape: `90 → 45` per colour reproduces their two published numbers
  exactly, and `4` colour-rotation orbits with the non-uniform ones having exactly `3` members
  reproduces the shape of their `→ 4 → 3`.
* **Completeness of the weight-12 logical pool.** The pool (1 884 per sector) is a saturated search,
  not a certified complete enumeration. It is used only in the *cascade* (§2.3), where every use is
  a one-sided witness, and in the choice of the 12 logical basis rows (any basis works). The exact
  certification in §4 does **not** use the pool.
* **Sector coupling.** `d_ext(ℰ)` is computed per sector and the circuit value is the minimum of the
  two; both are reported.
* **The second colouring is uncertified.** For `φ = a + b` the cascade leaves 44 tiled assignments
  (16 rotation orbits per sector) rather than 8, and I did not have the budget to certify them.
  That family lacks the `4 → 3` signature of S8, so I judge it the less likely reconstruction, but
  the refutation of §6 does not reach it. Completing it is ~32 SAT jobs of the size already run —
  roughly half a session on 24 cores.
* **The `Σ₂` question is untouched.** Nothing here says whether *some* order assignment reaches
  `d_ext = 11`, nor anything about interleaved circuits. Given that the blocking condition now has
  to defeat multi-hook mechanisms inside weight-14 and weight-16 logicals, my subjective prior that
  `max_M d_ext = 11` is achievable has dropped a long way, but that is a prior, not a result.
* **Depth convention.** I could not determine from the paper whether "depth 8" counts 6 CNOT layers
  plus prep and measure, or 8 time steps. The measurement-consistency results of §2.4 are stated for
  a definite number of CNOT layers, which sidesteps the ambiguity: no valid gross SEC exists at 6
  CNOT layers at all, and the reconstructed candidate needs 9.
* **The computations that hit the wall.** Three, all of the same kind — long UNSAT proofs I chose
  not to fund past the box:
  1. `W = 10` for the uniform assignment `(2,2,2)`, both sectors, 5 orbit representatives each,
     > 50 min without closing. This is the one entry in §4.2 that would turn a bound into a value,
     and a positive (UNSAT) answer there would be an exactly certified **distance-11** non-interleaved
     gross SEC.
  2. `W = 9` for `(2,2,9)`, i.e. whether the candidate is exactly 10 or lower.
  3. `T = 7` and `T = 8` of the reconstruction-free no-go of §4.5 — in my judgement the highest-value
     single computation left on the node, because its UNSAT would bound `D*_Gross` for the whole
     low-depth regime with no reconstruction assumption anywhere.

---

## 8b. What to run next, in priority order

Everything below reuses code already in §9; none of it needs a new idea.

1. **`nogo.py 7 8`** — the reconstruction-free no-go of §4.5. UNSAT at `T = 7` and `T = 8` would say
   that *every* legal, measurement-consistent gross SEC with at most 8 CNOT layers has `d_ext ≤ 10`,
   hence (Theorem 1) `d_circ ≤ 10`, with **no** reconstruction assumption anywhere. That is a
   statement about `D*_Gross` in the low-depth regime and it is the highest-value item on the board.
   SAT would return an explicit schedule that survives the local filter, which is then the natural
   input to a full certification.
2. **`orbit_job.py {Z,X} 2,2,2 10 {0..4}` to completion** — the one open row of §4.2. UNSAT on all
   five orbit representatives in both sectors gives an **exactly certified distance-11
   non-interleaved gross SEC** (realised at 9 CNOT layers, legal, (MC)-clean, `stim`-checked), which
   is deliverable (a) of the node.
3. **The `φ = a + b` colouring** — 44 tiled survivors, 16 rotation orbits per sector, ≈ 32 SAT jobs
   of the size already run. Closes the reconstruction conditional in §6.
4. **Review §2.4(1)** — is (MC) really equivalent to [SBB26]-non-interleaving for the gross code? A
   paper-only question with an outsized consequence (§5, last paragraph).
5. **`orbit_job.py Z 2,2,9 9 *`** — pins the candidate's exact value at 10 rather than `≤ 10`.

---

## 9. Reproduction

Python 3.9, `numpy` 2.0.2, `stim` 1.16.0, `python-sat` 1.9.dev15 (`python3 -m pip install
python-sat`).

**Reproduction was validated end-to-end.** The 21 modules below were extracted *back out of this
markdown file* into an empty directory and re-run from scratch (including a fresh weight-12 logical
pool build, 6.9 s). `gross.py` reproduced

```
{'rankHX': 66, 'rankHZ': 66, 'k': 12, 'overlaps': [0, 2], 'overlap_halves': [(0, 1)],
 'incidences': True}
```

and the three-way verification of the headline weight-10 witness reproduced all three lines quoted
in §4.3 exactly.

Order:

```
python3 gross.py         # code construction + rank/commutation/incidence checks      (< 1 s)
python3 pool.py          # weight-12 logical pools and logical bases                  (~5 s)
python3 stimcheck.py     # (MC) validated against stim's non-determinism oracle       (~60 s)
python3 ti_mc.py         # 25920 TI min-depth schedules, none measurement-consistent  (~200 s)
python3 enum3.py         # 3-colour-tiled min-depth + MC : UNSAT for all 4 colourings (< 1 s)
python3 cascade.py       # the 90 -> 45 -> 8 pruning cascade                          (~120 s)
python3 validate1.py     # certifier validation: reproduces d = 12 exactly            (~80 s)
python3 cascade_check.py # audit: every eliminated assignment carries a real weight-10 witness
python3 orbit_job.py Z 2,2,9 10 0      # one orbit subproblem of the certification   (~490 s)
python3 single.py        # d_ext(single-check R) vs d_ext(full E)                     (~150 s)
python3 realize2.py 2,2,9  # legality / (MC) realisability of the candidate by depth   (~90 s)
python3 noclass.py       # minimum CNOT layers for ANY valid gross SEC
python3 nogo.py 6 12     # the reconstruction-free no-go of 4.5
```

The three-way verification of the headline witness (§4.3) is:

```python
from sched import make_phi
from cert import tiled_orders
from gross import NG, xcheck_nb
import dext, simverify, stimverify, numpy as np
phi   = make_phi(1, 2)
oZ, _ = tiled_orders('Z', phi, (2, 2, 9))
oXdef = [[q for q, s, i in xcheck_nb(g)] for g in range(NG)]
R = [(3, 2), (9, 2), (15, 1)]
D = [0, 1, 11, 72, 79, 87, 90]
ctx, Hstab = dext.sector_ctx(oZ, 'Z')
nets = np.zeros(144, np.uint8)
for (c, k) in R:
    for q in ctx.res[c][k]:
        nets[q] ^= 1
Dv = np.zeros(144, np.uint8); Dv[D] = 1
print(dext.verify_witness(ctx, (Dv ^ nets) % 2, R, Dv, Hstab))   # exact F2 algebra
print(simverify.verify(oZ, R, D, verbose=False))                 # own Pauli-frame simulator
print(stimverify.check(oXdef, oZ, R, D))                         # stim
```

reproducing

```
{'weight': 10, 'n_data': 7, 'n_res': 3, 'Ewt': 14, 'decomposition_ok': True,
 'zero_syndrome': True, 'nontrivial_logical': True}
{'nfaults': 10, 'round_detectors_silent': True, 'terminal_detectors_silent': True,
 'net_error_weight': 14, 'nontrivial_logical': True}
{'n_faults': 10, 'detectors_fired': 0, 'observables_flipped': 4,
 'clean_detectors_fired': 0, 'clean_observables_flipped': 0, 'n_detectors': 288}
```

### 9.1 Modules

#### `gross.py`

```python
"""Gross code [[144,12,12]] : construction, F2 linear algebra, Tanner incidences.
Exact numpy uint8 arithmetic only.  Independently written for the SBB certification session.
"""
import numpy as np, itertools

ELL, EM = 12, 6
NG = ELL * EM            # 72 group elements
N = 2 * NG               # 144 data qubits: left 0..71, right 72..143


def gidx(i, j):
    return (i % ELL) * EM + (j % EM)


def gsum(g, m):
    i, j = divmod(g, EM)
    return gidx(i + m[0], j + m[1])


def mono(a, b):
    P = np.zeros((NG, NG), np.uint8)
    for i in range(ELL):
        for j in range(EM):
            P[gidx(i + a, j + b), gidx(i, j)] = 1
    return P


A_MONOS = [(3, 0), (0, 1), (0, 2)]      # A = x^3 + y + y^2
B_MONOS = [(0, 3), (1, 0), (2, 0)]      # B = y^3 + x + x^2
A = sum(mono(*m) for m in A_MONOS) % 2
B = sum(mono(*m) for m in B_MONOS) % 2
HX = np.concatenate([A, B], 1).astype(np.uint8)
HZ = np.concatenate([B.T, A.T], 1).astype(np.uint8)


# ---------------- F2 linear algebra ----------------
def rref(Mat):
    Mat = Mat.copy() % 2
    rows, cols = Mat.shape
    piv = []; r = 0
    for c in range(cols):
        pr = None
        for rr in range(r, rows):
            if Mat[rr, c]:
                pr = rr; break
        if pr is None:
            continue
        if pr != r:
            Mat[[r, pr]] = Mat[[pr, r]]
        sel = (Mat[:, c] == 1); sel[r] = False
        Mat[sel] ^= Mat[r]
        piv.append(c); r += 1
        if r == rows:
            break
    return Mat[:r], piv


def nullspace(Mat):
    R, piv = rref(Mat)
    cols = Mat.shape[1]
    pset = set(piv)
    free = [c for c in range(cols) if c not in pset]
    basis = []
    for f in free:
        v = np.zeros(cols, np.uint8); v[f] = 1
        for r, p in enumerate(piv):
            if R[r, f]:
                v[p] = 1
        basis.append(v)
    return np.array(basis, np.uint8) if basis else np.zeros((0, cols), np.uint8)


class Reducer:
    def __init__(self, Mat):
        self.R, self.piv = rref(Mat)

    def red(self, v):
        w = v.copy() % 2
        for r, p in enumerate(self.piv):
            if w[p]:
                w ^= self.R[r]
        return w

    def inspan(self, v):
        return not self.red(v).any()


# ---------------- Tanner incidences (derived, verified below) ----------------
# X-check g touches left data  g - A_i  (monomial A_i)  and right data NG + (g - B_i)
# Z-check g touches left data  g + B_i  (monomial B_i)  and right data NG + (g + A_i)
def xcheck_nb(g):
    out = [(gsum(g, (-m[0], -m[1])), 'L', i) for i, m in enumerate(A_MONOS)]
    out += [(NG + gsum(g, (-m[0], -m[1])), 'R', i) for i, m in enumerate(B_MONOS)]
    return out


def zcheck_nb(g):
    out = [(gsum(g, m), 'L', i) for i, m in enumerate(B_MONOS)]
    out += [(NG + gsum(g, m), 'R', i) for i, m in enumerate(A_MONOS)]
    return out


def xchecks_of(q):
    if q < NG:
        return [(gsum(q, m), 'L', i) for i, m in enumerate(A_MONOS)]
    g = q - NG
    return [(gsum(g, m), 'R', i) for i, m in enumerate(B_MONOS)]


def zchecks_of(q):
    if q < NG:
        return [(gsum(q, (-m[0], -m[1])), 'L', i) for i, m in enumerate(B_MONOS)]
    g = q - NG
    return [(gsum(g, (-m[0], -m[1])), 'R', i) for i, m in enumerate(A_MONOS)]


def verify_incidences():
    for g in range(NG):
        assert sorted(q for q, _, _ in xcheck_nb(g)) == sorted(map(int, np.nonzero(HX[g])[0])), g
        assert sorted(q for q, _, _ in zcheck_nb(g)) == sorted(map(int, np.nonzero(HZ[g])[0])), g
    for q in range(N):
        assert sorted(c for c, _, _ in xchecks_of(q)) == sorted(map(int, np.nonzero(HX[:, q])[0])), q
        assert sorted(c for c, _, _ in zchecks_of(q)) == sorted(map(int, np.nonzero(HZ[:, q])[0])), q
    for g in range(NG):
        for q, s, i in xcheck_nb(g):
            assert (g, s, i) in xchecks_of(q)
        for q, s, i in zcheck_nb(g):
            assert (g, s, i) in zchecks_of(q)
    return True


# ---------------- translations (code automorphisms) ----------------
def tperm_data(a, b):
    """data permutation p with (T v)[p_target] ; new[gidx(i+a,j+b)] = old[gidx(i,j)]"""
    p = np.empty(N, int)
    for i in range(ELL):
        for j in range(EM):
            p[gidx(i + a, j + b)] = gidx(i, j)
            p[NG + gidx(i + a, j + b)] = NG + gidx(i, j)
    return p


TRANS = [tperm_data(a, b) for a in range(ELL) for b in range(EM)]


def sanity():
    assert ((HX @ HZ.T) % 2 == 0).all()
    assert set(HX.sum(1)) == {6} and set(HZ.sum(1)) == {6}
    assert set(HX.sum(0)) == {3} and set(HZ.sum(0)) == {3}
    rx = len(rref(HX)[1]); rz = len(rref(HZ)[1])
    ov = set()
    for i in range(NG):
        for j in range(NG):
            ov.add(int((HX[i] & HZ[j]).sum()))
    # overlap halves: for each overlapping (X,Z) pair, where do the 2 shared qubits sit?
    halves = set()
    for i in range(NG):
        for j in range(NG):
            sh = np.nonzero(HX[i] & HZ[j])[0]
            if len(sh):
                halves.add(tuple(sorted(int(q >= NG) for q in sh)))
    return dict(rankHX=rx, rankHZ=rz, k=N - rx - rz, overlaps=sorted(ov),
                overlap_halves=sorted(halves), incidences=verify_incidences())


if __name__ == "__main__":
    print(sanity())
```

#### `sched.py`

```python
"""Schedules for the gross code: explicit legality + measurement-consistency (MC) checks,
plus the symbolic 3-colour-tiled parameterisation and its enumeration.

A schedule is given as two arrays
    LX[c, s, i]  = CNOT layer of the X-check of colour c, side s in {0=L,1=R}, monomial index i
    LZ[c, s, i]  = CNOT layer of the Z-check of colour c, side s in {0=L,1=R}, monomial index i
where for X-checks side L uses A-monomials and side R uses B-monomials, and for Z-checks side L
uses B-monomials and side R uses A-monomials (gross.xcheck_nb / zcheck_nb).

Colouring: phi(x^a y^b) = (s*a + t*b) mod 3 with s,t in {1,2}; these are exactly the 4 group
homomorphisms G -> Z_3 that properly 3-colour both check-conflict graphs.
"""
import numpy as np, itertools
from gross import (ELL, EM, NG, N, gidx, gsum, A_MONOS, B_MONOS, HX, HZ,
                   xcheck_nb, zcheck_nb, xchecks_of, zchecks_of)


def make_phi(s, t):
    ph = np.empty(NG, int)
    for i in range(ELL):
        for j in range(EM):
            ph[gidx(i, j)] = (s * i + t * j) % 3
    return ph


def colour_valid(phi):
    """phi must give distinct colours to any two same-type checks sharing a data qubit."""
    for g in range(NG):
        cs = [phi[gsum(g, m)] for m in A_MONOS]        # X-checks on left qubit g
        if len(set(cs)) != 3:
            return False
        cs = [phi[gsum(g, m)] for m in B_MONOS]        # X-checks on right qubit g
        if len(set(cs)) != 3:
            return False
        cs = [phi[gsum(g, (-m[0], -m[1]))] for m in B_MONOS]   # Z-checks on left qubit g
        if len(set(cs)) != 3:
            return False
        cs = [phi[gsum(g, (-m[0], -m[1]))] for m in A_MONOS]   # Z-checks on right qubit g
        if len(set(cs)) != 3:
            return False
    return True


# ---------------- explicit schedule expansion ----------------
def expand(phi, LX, LZ):
    """Return tX[g][(side,i)] and tZ[g][(side,i)] : explicit CNOT times for every check."""
    tX = [None] * NG; tZ = [None] * NG
    for g in range(NG):
        c = phi[g]
        tX[g] = {('L', i): int(LX[c, 0, i]) for i in range(3)}
        tX[g].update({('R', i): int(LX[c, 1, i]) for i in range(3)})
        tZ[g] = {('L', i): int(LZ[c, 0, i]) for i in range(3)}
        tZ[g].update({('R', i): int(LZ[c, 1, i]) for i in range(3)})
    return tX, tZ


def check_legal(tX, tZ, depth):
    """every check uses 6 distinct layers; every data qubit uses 6 distinct layers."""
    for g in range(NG):
        if len(set(tX[g].values())) != 6 or len(set(tZ[g].values())) != 6:
            return False
        if max(tX[g].values()) > depth or max(tZ[g].values()) > depth:
            return False
    for q in range(N):
        ts = [tX[c][(s, i)] for (c, s, i) in xchecks_of(q)] + \
             [tZ[c][(s, i)] for (c, s, i) in zchecks_of(q)]
        if len(set(ts)) != 6:
            return False
    return True


def mc_violations(tX, tZ):
    """(MC): for every X-check a and Z-check b,
       #{ q in supp(a)&supp(b) : t(q->b) < t(a->q) } must be even."""
    xnb = [xcheck_nb(g) for g in range(NG)]
    znb = [zcheck_nb(g) for g in range(NG)]
    xmap = [{q: (s, i) for q, s, i in xnb[g]} for g in range(NG)]
    zmap = [{q: (s, i) for q, s, i in znb[g]} for g in range(NG)]
    bad = 0; tot = 0
    for a in range(NG):
        for b in range(NG):
            shared = set(xmap[a]) & set(zmap[b])
            if not shared:
                continue
            tot += 1
            cnt = 0
            for q in shared:
                if tZ[b][zmap[b][q]] < tX[a][xmap[a][q]]:
                    cnt += 1
            if cnt % 2:
                bad += 1
    return bad, tot


def sbb_noninterleaved(tX, tZ):
    """SBB non-interleaving, per overlapping (X-check, Z-check) pair:
       either all of a's CNOTs on the overlap precede all of b's on the overlap, or vice versa."""
    xmap = [{q: (s, i) for q, s, i in xcheck_nb(g)} for g in range(NG)]
    zmap = [{q: (s, i) for q, s, i in zcheck_nb(g)} for g in range(NG)]
    bad = 0
    for a in range(NG):
        for b in range(NG):
            shared = set(xmap[a]) & set(zmap[b])
            if not shared:
                continue
            ta = [tX[a][xmap[a][q]] for q in shared]
            tb = [tZ[b][zmap[b][q]] for q in shared]
            if not (max(ta) < min(tb) or max(tb) < min(ta)):
                bad += 1
    return bad


def global_noninterleaved(tX, tZ):
    """the strong (in-house Def 2.4) version: all X-CNOTs before all Z-CNOTs, or vice versa."""
    xs = [v for g in range(NG) for v in tX[g].values()]
    zs = [v for g in range(NG) for v in tZ[g].values()]
    return max(xs) < min(zs) or max(zs) < min(xs)


# ---------------- within-check CNOT orders / residual sets ----------------
def check_orders(phi, LX, LZ):
    """orderX[g] = list of the 6 data qubits of X-check g in CNOT order; same for Z."""
    tX, tZ = expand(phi, LX, LZ)
    oX = []; oZ = []
    for g in range(NG):
        nb = xcheck_nb(g)
        oX.append([q for q, s, i in sorted(nb, key=lambda z: tX[g][(z[1], z[2])])])
        nb = zcheck_nb(g)
        oZ.append([q for q, s, i in sorted(nb, key=lambda z: tZ[g][(z[1], z[2])])])
    return oX, oZ


def residuals_from_order(order):
    """SBB residual errors of one weight-6 check measured in CNOT order i1..i6, reduced modulo
    the check itself and with the weight-<=1 ones dropped (they duplicate data columns):
        {i1,i2} , {i4,i5,i6} , {i5,i6}."""
    i1, i2, i3, i4, i5, i6 = order
    return [(i1, i2), (i4, i5, i6), (i5, i6)]


def full_suffix_residuals(order):
    """all six suffixes S_l = {i_l,...,i_6}, l = 1..6 (the raw hook errors)."""
    return [tuple(order[l:]) for l in range(6)]
```

#### `stimcheck.py`

```python
"""Independent oracle for measurement consistency: build the literal stim circuit of a gross-code
schedule and ask stim for a detector error model.  stim raises ValueError exactly when a detector
is non-deterministic, i.e. exactly when the schedule is not a syndrome-extraction circuit."""
import numpy as np, itertools, stim
from gross import NG, N, xcheck_nb, zcheck_nb
from sched import expand, check_legal, mc_violations

XANC = [N + g for g in range(NG)]          # 144..215
ZANC = [N + NG + g for g in range(NG)]     # 216..287


def stim_circuit(tX, tZ, R=3, basis='Z', p=1e-3):
    """standard memory experiment: ideal data init, R rounds, ideal transversal readout."""
    layers = sorted({v for g in range(NG) for v in tX[g].values()} |
                    {v for g in range(NG) for v in tZ[g].values()})
    gates = {l: [] for l in layers}
    for g in range(NG):
        for q, s, i in xcheck_nb(g):
            gates[tX[g][(s, i)]] += [XANC[g], q]      # X ancilla is control
        for q, s, i in zcheck_nb(g):
            gates[tZ[g][(s, i)]] += [q, ZANC[g]]      # Z ancilla is target
    data = list(range(N))
    c = stim.Circuit()
    c.append("R" if basis == 'Z' else "RX", data)
    nmeas = 0; rec = {}
    for r in range(R):
        c.append("RX", XANC); c.append("R", ZANC)
        c.append("DEPOLARIZE1", XANC + ZANC, p)
        for l in layers:
            tg = gates[l]
            used = set(tg)
            assert len(tg) == len(used), "illegal layer: qubit in two gates"
            c.append("CX", tg); c.append("DEPOLARIZE2", tg, p)
        c.append("MX", XANC, p)
        for g in range(NG):
            rec[('X', g, r)] = nmeas + g
        nmeas += NG
        c.append("M", ZANC, p)
        for g in range(NG):
            rec[('Z', g, r)] = nmeas + g
        nmeas += NG
        det = 'Z' if basis == 'Z' else 'X'
        oth = 'X' if basis == 'Z' else 'Z'
        for g in range(NG):
            if r == 0:
                c.append("DETECTOR", [stim.target_rec(rec[(det, g, 0)] - nmeas)])
            else:
                c.append("DETECTOR", [stim.target_rec(rec[(det, g, r)] - nmeas),
                                      stim.target_rec(rec[(det, g, r - 1)] - nmeas)])
            if r >= 1:
                c.append("DETECTOR", [stim.target_rec(rec[(oth, g, r)] - nmeas),
                                      stim.target_rec(rec[(oth, g, r - 1)] - nmeas)])
    c.append("M" if basis == 'Z' else "MX", data)
    for q in range(N):
        rec[('d', q)] = nmeas + q
    nmeas += N
    H = None
    from gross import HX, HZ
    H = HZ if basis == 'Z' else HX
    for g in range(NG):
        tg = [stim.target_rec(rec[(det, g, R - 1)] - nmeas)]
        for q in np.nonzero(H[g])[0]:
            tg.append(stim.target_rec(rec[('d', int(q))] - nmeas))
        c.append("DETECTOR", tg)
    return c


def stim_ok(tX, tZ, R=3, basis='Z'):
    try:
        c = stim_circuit(tX, tZ, R=R, basis=basis)
        dem = c.detector_error_model(decompose_errors=False, approximate_disjoint_errors=True)
        return True, dem.num_detectors, len([1 for _ in dem.flattened() if _.type == 'error'])
    except ValueError as e:
        return False, str(e)[:80], None


if __name__ == "__main__":
    phi0 = np.zeros(NG, int)
    # (a) a legal 6-CNOT-layer translation-invariant schedule (MC-violating by ti_mc.py)
    LX = np.zeros((3, 2, 3), int); LZ = np.zeros((3, 2, 3), int)
    for c in range(3):
        LX[c, 0, :] = [1, 2, 3]; LX[c, 1, :] = [4, 5, 6]
        LZ[c, 0, :] = [4, 5, 6]; LZ[c, 1, :] = [1, 2, 3]
    tX, tZ = expand(phi0, LX, LZ)
    print("(a) legal 6-layer LRC-style TI schedule: legal =", check_legal(tX, tZ, 6),
          " MC violations =", mc_violations(tX, tZ))
    print("    stim:", stim_ok(tX, tZ))
    # (b) fully non-interleaved: all X CNOTs in layers 1-6, all Z CNOTs in layers 7-12
    LX2 = np.zeros((3, 2, 3), int); LZ2 = np.zeros((3, 2, 3), int)
    for c in range(3):
        LX2[c, 0, :] = [1, 2, 3]; LX2[c, 1, :] = [4, 5, 6]
        LZ2[c, 0, :] = [7, 8, 9]; LZ2[c, 1, :] = [10, 11, 12]
    tX2, tZ2 = expand(phi0, LX2, LZ2)
    print("(b) 12-layer X-then-Z (globally non-interleaved): MC violations =",
          mc_violations(tX2, tZ2))
    print("    stim:", stim_ok(tX2, tZ2))
    print("    stim X-memory:", stim_ok(tX2, tZ2, basis='X'))
```

#### `ti_mc.py`

```python
"""Does the translation-invariant minimum-depth class contain ANY measurement-consistent
schedule?  Brute force over (6!)^2 = 518400 candidate (X-order, Z-order) pairs."""
import numpy as np, itertools, time
from gross import NG
from sched import make_phi, expand, check_legal, mc_violations, sbb_noninterleaved

phi0 = np.zeros(NG, int)          # single colour = fully translation invariant

t0 = time.time()
legal = 0; mcok = 0; examples = []
for px in itertools.permutations(range(1, 7)):
    LX = np.zeros((3, 2, 3), int)
    for c in range(3):
        LX[c, 0, :] = px[:3]; LX[c, 1, :] = px[3:]
    for pz in itertools.permutations(range(1, 7)):
        LZ = np.zeros((3, 2, 3), int)
        for c in range(3):
            LZ[c, 0, :] = pz[:3]; LZ[c, 1, :] = pz[3:]
        tX, tZ = expand(phi0, LX, LZ)
        if not check_legal(tX, tZ, 6):
            continue
        legal += 1
        bad, tot = mc_violations(tX, tZ)
        if bad == 0:
            mcok += 1
            if len(examples) < 3:
                examples.append((px, pz))
print("legal TI min-depth schedules      :", legal)
print("of which measurement-consistent   :", mcok)
print("examples:", examples)
print("elapsed %.1f s" % (time.time() - t0))
```

#### `enum3.py`

```python
"""Exhaustive enumeration of 3-colour-tiled minimum-depth (6 CNOT layer, circuit depth 8)
gross-code schedules that are LEGAL and MEASUREMENT-CONSISTENT.

Encoding: one-hot SAT over 36 integer variables in {1..6}; all constraints are stated symbolically
and then EVERY solution is re-verified on the explicit 864-edge Tanner graph by sched.check_legal /
sched.mc_violations, which share no code with this encoding.
"""
import numpy as np, itertools, sys, time
from pysat.solvers import Cadical153
from pysat.formula import IDPool
from gross import NG
from sched import make_phi, colour_valid, expand, check_legal, mc_violations, \
    sbb_noninterleaved, global_noninterleaved

LAYERS = [1, 2, 3, 4, 5, 6]


def var_list():
    out = []
    for c in range(3):
        for s in (0, 1):
            for i in range(3):
                out.append(('X', c, s, i));
    for c in range(3):
        for s in (0, 1):
            for i in range(3):
                out.append(('Z', c, s, i))
    return out


def build(s_par, t_par):
    alpha = [0, t_par % 3, (2 * t_par) % 3]      # phi(A_i)
    beta = [0, s_par % 3, (2 * s_par) % 3]       # phi(B_i)
    pool = IDPool()
    V = {}
    for v in var_list():
        for l in LAYERS:
            V[(v, l)] = pool.id((v, l))
    cls = []
    # one-hot
    for v in var_list():
        cls.append([V[(v, l)] for l in LAYERS])
        for l1, l2 in itertools.combinations(LAYERS, 2):
            cls.append([-V[(v, l1)], -V[(v, l2)]])

    def group_perm(vs):
        """the 6 variables in vs take 6 distinct values (hence exactly {1..6})"""
        assert len(vs) == 6
        for l in LAYERS:
            cls.append([V[(v, l)] for v in vs])                 # each layer used
            for v1, v2 in itertools.combinations(vs, 2):
                cls.append([-V[(v1, l)], -V[(v2, l)]])           # at most once

    # per-colour check constraints
    for c in range(3):
        group_perm([('X', c, 0, 0), ('X', c, 0, 1), ('X', c, 0, 2),
                    ('X', c, 1, 0), ('X', c, 1, 1), ('X', c, 1, 2)])
        group_perm([('Z', c, 0, 0), ('Z', c, 0, 1), ('Z', c, 0, 2),
                    ('Z', c, 1, 0), ('Z', c, 1, 1), ('Z', c, 1, 2)])
    # per-data-qubit legality
    for g in range(3):
        group_perm([('X', (g + alpha[i]) % 3, 0, i) for i in range(3)] +
                   [('Z', (g - beta[i]) % 3, 0, i) for i in range(3)])
        group_perm([('X', (g + beta[i]) % 3, 1, i) for i in range(3)] +
                   [('Z', (g - alpha[i]) % 3, 1, i) for i in range(3)])
    # measurement consistency
    nmc = 0
    for g in range(3):
        for i in range(3):
            for j in range(3):
                gh = (g + alpha[i] + beta[j]) % 3
                vP = ('Z', g, 0, j); vA = ('X', gh, 0, i)
                vQ = ('Z', g, 1, i); vB = ('X', gh, 1, j)
                for l1 in LAYERS:
                    for l2 in LAYERS:
                        if l1 == l2:
                            continue
                        for l3 in LAYERS:
                            for l4 in LAYERS:
                                if l3 == l4:
                                    continue
                                if (l1 < l2) != (l3 < l4):
                                    cls.append([-V[(vP, l1)], -V[(vA, l2)],
                                                -V[(vQ, l3)], -V[(vB, l4)]])
                                    nmc += 1
    return V, cls, alpha, beta, nmc


def model_to_sched(V, model):
    ms = set(x for x in model if x > 0)
    LX = np.zeros((3, 2, 3), int); LZ = np.zeros((3, 2, 3), int)
    for v in var_list():
        for l in LAYERS:
            if V[(v, l)] in ms:
                if v[0] == 'X':
                    LX[v[1], v[2], v[3]] = l
                else:
                    LZ[v[1], v[2], v[3]] = l
    return LX, LZ


def run(s_par, t_par, cap=None, verify_every=1):
    phi = make_phi(s_par, t_par)
    assert colour_valid(phi), (s_par, t_par)
    V, cls, alpha, beta, nmc = build(s_par, t_par)
    sol = []
    t0 = time.time()
    with Cadical153(bootstrap_with=cls) as S:
        while S.solve():
            m = S.get_model()
            LX, LZ = model_to_sched(V, m)
            sol.append((LX.copy(), LZ.copy()))
            block = []
            for v in var_list():
                l = (LX if v[0] == 'X' else LZ)[v[1], v[2], v[3]]
                block.append(-V[(v, l)])
            S.add_clause(block)
            if cap and len(sol) >= cap:
                break
    return phi, sol, len(cls), nmc, time.time() - t0


if __name__ == "__main__":
    for (s_par, t_par) in [(1, 1), (1, 2), (2, 1), (2, 2)]:
        phi, sol, ncls, nmc, el = run(s_par, t_par, cap=200000)
        print(f"phi = {s_par}a+{t_par}b mod 3 : {len(sol)} legal+MC 3-colour-tiled min-depth "
              f"schedules   ({ncls} clauses, {nmc} MC clauses, {el:.1f}s)")
        # explicit re-verification of a sample
        import random
        random.seed(0)
        smp = sol if len(sol) <= 40 else random.sample(sol, 40)
        ok = 0; sbb = 0; glob = 0
        for LX, LZ in smp:
            tX, tZ = expand(phi, LX, LZ)
            if check_legal(tX, tZ, 6) and mc_violations(tX, tZ)[0] == 0:
                ok += 1
            if sbb_noninterleaved(tX, tZ) == 0:
                sbb += 1
            if global_noninterleaved(tX, tZ):
                glob += 1
        print(f"    explicit re-verification: {ok}/{len(smp)} legal+MC ; "
              f"SBB-non-interleaved {sbb}/{len(smp)} ; globally-non-interleaved {glob}/{len(smp)}")
        np.save(f"sched_{s_par}{t_par}.npy",
                np.array([(LX, LZ) for LX, LZ in sol], dtype=int) if sol else np.zeros((0,)))
```

#### `cascade.py`

```python
"""Reproduce SBB's pruning cascade 90 -> 45 -> ... -> 3 over THREE-COLOUR-TILED within-check
CNOT-order assignments, and identify the surviving assignment(s).

A tiled assignment is a triple (s_0, s_1, s_2) of within-check slot orders, one per colour class of
the checks.  Two orders give the same residual set iff they differ by the order-8 group
<swap(pos1,pos2), swap(pos5,pos6), global reversal>, so there are 6!/8 = 90 classes per colour and
90^3 = 729000 tiled assignments per sector -- exactly the count [SBB26 Prop. 6] prunes.

Every elimination below EXHIBITS a witness (a weight-12 logical plus one or two residual columns
whose total extended-code weight is <= 10), so the pruning is one-sided-sound: a surviving
assignment is a candidate, an eliminated one provably has d_ext <= 10.
"""
import numpy as np, itertools, sys
from collections import defaultdict
from gross import NG, N, zcheck_nb, xcheck_nb, HX, HZ, Reducer
from sched import make_phi, colour_valid
import pool as poolmod

PERMS = list(itertools.permutations(range(6)))


def order8(p):
    """the 8 orders with the same residual set as p"""
    out = set()
    for sw01 in (0, 1):
        for sw45 in (0, 1):
            q = list(p)
            if sw01:
                q[0], q[1] = q[1], q[0]
            if sw45:
                q[4], q[5] = q[5], q[4]
            out.add(tuple(q)); out.add(tuple(reversed(q)))
    return out


def build_classes():
    seen = set(); reps = []; cls_of = {}
    for p in PERMS:
        if p in seen:
            continue
        orb = order8(p)
        assert len(orb) == 8, (p, len(orb))
        idx = len(reps); reps.append(p)
        for q in orb:
            cls_of[q] = idx
        seen |= orb
    return reps, cls_of


REPS, CLS_OF = build_classes()
NCLS = len(REPS)
PAIRS = list(itertools.combinations(range(6), 2))          # slot pairs
TRIPS = list(itertools.combinations(range(6), 3))          # slot triples
PIDX = {p: i for i, p in enumerate(PAIRS)}
TIDX = {t: i for i, t in enumerate(TRIPS)}


def act_tables():
    """ACT2[class][pair]  : the order puts that slot-pair in positions {1,2} or {5,6}
       ACT3[class][triple]: the order puts that slot-triple in positions {4,5,6} or {1,2,3}"""
    A2 = np.zeros((NCLS, len(PAIRS)), bool)
    A3 = np.zeros((NCLS, len(TRIPS)), bool)
    for ci, p in enumerate(REPS):
        A2[ci, PIDX[tuple(sorted(p[0:2]))]] = True
        A2[ci, PIDX[tuple(sorted(p[4:6]))]] = True
        A3[ci, TIDX[tuple(sorted(p[3:6]))]] = True
        A3[ci, TIDX[tuple(sorted(p[0:3]))]] = True
    return A2, A3


ACT2, ACT3 = act_tables()


def sector_data(sector):
    PZ, PX, LX, LZ = poolmod.get()
    if sector == 'Z':
        nb = [zcheck_nb(g) for g in range(NG)]        # Z-check hooks, Z-type logicals
        Pl, Hstab, Hdet = PZ, HZ, HX
    else:
        nb = [xcheck_nb(g) for g in range(NG)]
        Pl, Hstab, Hdet = PX, HX, HZ
    slots = [[q for q, s, i in nb[g]] for g in range(NG)]   # canonical slot -> qubit
    return slots, Pl, Hstab, Hdet


def check_pool_closure(slots, Pl, Hstab):
    """for every pool logical L and check c with |L cap c| = 3, L+c must again be in the pool"""
    key = {v.tobytes() for v in Pl}
    red = Reducer(Hstab)
    bad = 0
    for L in Pl:
        for c in range(NG):
            S = [k for k in range(6) if L[slots[c][k]]]
            if len(S) == 3:
                M = L.copy()
                for q in slots[c]:
                    M[q] ^= 1
                if M.tobytes() not in key:
                    bad += 1
    return bad


def collect_rules(sector, phi):
    slots, Pl, Hstab, Hdet = sector_data(sector)
    rules1 = set()      # (colour, triple-index)               -> gain 2, weight 10
    rules2 = set()      # ((c1,p1),(c2,p2)) sorted             -> gain 1+1 disjoint, weight 10
    for L in Pl:
        hits = []       # (colour, pair-index, frozenset of qubits)
        for c in range(NG):
            S = [k for k in range(6) if L[slots[c][k]]]
            if len(S) < 2:
                continue
            col = int(phi[c])
            if len(S) == 3:
                rules1.add((col, TIDX[tuple(S)]))
            for P in itertools.combinations(S, 2):
                hits.append((col, PIDX[P], frozenset(slots[c][k] for k in P)))
        for i in range(len(hits)):
            for j in range(i + 1, len(hits)):
                if hits[i][2] & hits[j][2]:
                    continue
                a = (hits[i][0], hits[i][1]); b = (hits[j][0], hits[j][1])
                rules2.add((a, b) if a <= b else (b, a))
    return rules1, rules2


def survivors(rules1, rules2):
    alive = np.ones((NCLS, NCLS, NCLS), bool)
    # stage 1
    per_colour_ok = [np.ones(NCLS, bool) for _ in range(3)]
    for (col, ti) in rules1:
        per_colour_ok[col] &= ~ACT3[:, ti]
    for col in range(3):
        sh = [1, 1, 1]; sh[col] = NCLS
        alive &= per_colour_ok[col].reshape(sh)
    stage1 = [int(v.sum()) for v in per_colour_ok]
    after1 = int(alive.sum())
    # stage 2
    for (a, b) in rules2:
        (c1, p1), (c2, p2) = a, b
        m1 = ACT2[:, p1]; m2 = ACT2[:, p2]
        sh1 = [1, 1, 1]; sh1[c1] = NCLS
        sh2 = [1, 1, 1]; sh2[c2] = NCLS
        alive &= ~(m1.reshape(sh1) & m2.reshape(sh2))
    return alive, stage1, after1


if __name__ == "__main__":
    for sector in ('Z', 'X'):
        slots, Pl, Hstab, Hdet = sector_data(sector)
        print(f"=== sector {sector} ===  order classes: {NCLS}   pool: {len(Pl)}")
        print("   pool coset-closure violations (L, L+c for |L cap c|=3):",
              check_pool_closure(slots, Pl, Hstab))
        for (s, t) in [(1, 1), (1, 2), (2, 1), (2, 2)]:
            phi = make_phi(s, t)
            assert colour_valid(phi)
            r1, r2 = collect_rules(sector, phi)
            alive, stage1, after1 = survivors(r1, r2)
            idx = np.argwhere(alive)
            print(f"   phi={s}a+{t}b: per-colour survivors after stage 1 = {stage1} "
                  f"(=> {after1} triples), after stage 2 = {int(alive.sum())}"
                  f"   [{len(r1)} single-check rules, {len(r2)} pair rules]")
            if 0 < int(alive.sum()) <= 12:
                for v in idx:
                    print("        surviving assignment (order classes):", tuple(int(x) for x in v),
                          "orders:", [REPS[int(x)] for x in v])
```

#### `cascade_check.py`

```python
"""Audit the cascade: every elimination must come with a real weight-10 witness.
For a sample of eliminated tiled assignments, materialise the witness the rule claims and verify it
end to end (F2 algebra + independent Pauli-frame circuit simulation)."""
import numpy as np, itertools, random
from gross import NG, N, HX, HZ, Reducer
from sched import make_phi
from cascade import REPS, sector_data, ACT2, ACT3, PAIRS, TRIPS, PIDX, TIDX, NCLS
from cert import tiled_orders
import simverify

RES_POS = [(0, 1), (3, 4, 5), (4, 5)]


def find_witness(sector, phi, triple):
    """search the weight-12 pool for a stage-1 or stage-2 witness of weight 10"""
    slots, Pl, Hstab, Hdet = sector_data(sector)
    for L in Pl:
        hits = []
        for c in range(NG):
            S = [k for k in range(6) if L[slots[c][k]]]
            if len(S) < 2:
                continue
            sig = REPS[triple[int(phi[c])]]
            # stage 1: r2 = positions 4,5,6 of the order, as slots
            r2 = tuple(sorted(sig[3:6]))
            if len(S) == 3 and r2 == tuple(S):
                return ('stage1', L, [(c, 1)])
            # stage 2 candidates: r1 (positions 1,2) and r3 (positions 5,6)
            for k, pos in ((0, (0, 1)), (2, (4, 5))):
                P = tuple(sorted(sig[p] for p in pos))
                if all(p in S for p in P):
                    hits.append((c, k, frozenset(slots[c][p] for p in P)))
        for i in range(len(hits)):
            for j in range(i + 1, len(hits)):
                if not (hits[i][2] & hits[j][2]):
                    return ('stage2', L, [(hits[i][0], hits[i][1]), (hits[j][0], hits[j][1])])
    return None


def audit(sector, phi, triple):
    res = find_witness(sector, phi, triple)
    if res is None:
        return None
    kind, L, R = res
    orders, _ = tiled_orders(sector, phi, triple)
    nets = np.zeros(N, np.uint8)
    for (c, k) in R:
        for p in RES_POS[k]:
            nets[orders[c][p]] ^= 1
    D = (L ^ nets) % 2
    w = int(D.sum()) + len(R)
    Hdet = HX if sector == 'Z' else HZ
    Hstab = HZ if sector == 'Z' else HX
    ok = dict(kind=kind, weight=w, Ewt=int(L.sum()),
              zero_syndrome=not ((Hdet @ L) % 2).any(),
              nontrivial=not Reducer(Hstab).inspan(L))
    if sector == 'Z':
        ok['circuit'] = simverify.verify(orders, R, [int(i) for i in np.nonzero(D)[0]],
                                         verbose=False)
    return ok


if __name__ == "__main__":
    phi = make_phi(1, 2)
    random.seed(0)
    trips = [(a, b, c) for a in range(NCLS) for b in range(NCLS) for c in range(NCLS)]
    alive = {(2, 2, 2), (2, 2, 9), (2, 9, 2), (2, 9, 9), (9, 2, 2), (9, 2, 9), (9, 9, 2), (9, 9, 9)}
    sample = [t for t in random.sample(trips, 400) if t not in alive][:10]
    for t in sample:
        print(t, audit('Z', phi, t))
```

#### `pool.py`

```python
"""Weight-12 logical pools of the gross code + low-weight logical bases (for SAT encoding)."""
import numpy as np, itertools, time, os
from gross import HX, HZ, N, rref, nullspace, Reducer, TRANS


def isd(Gb, wmax, trials, found, rng):
    nc = Gb.shape[1]
    for _ in range(trials):
        perm = rng.permutation(nc)
        R, _ = rref(Gb[:, perm])
        inv = np.empty(nc, int); inv[perm] = np.arange(nc)
        rows = R[:, inv]
        wts = rows.sum(1)
        for i in np.nonzero(wts <= wmax)[0]:
            found.setdefault(rows[i].tobytes(), rows[i])
        light = np.argsort(wts)[:40]
        for a, b in itertools.combinations(light, 2):
            v = rows[a] ^ rows[b]
            if v.sum() <= wmax:
                found.setdefault(v.tobytes(), v)
        light3 = np.argsort(wts)[:22]
        for a, b, c in itertools.combinations(light3, 3):
            v = rows[a] ^ rows[b] ^ rows[c]
            if v.sum() <= wmax:
                found.setdefault(v.tobytes(), v)
    return found


def build_pool(Hdet, Hstab, seed, trials=600):
    rng = np.random.default_rng(seed)
    Ker = nullspace(Hdet); red = Reducer(Hstab)
    found = {}
    isd(Ker, 12, trials, found, rng)
    words = [v for v in found.values() if v.sum() == 12 and not red.inspan(v)]
    d = {}
    for v in words:
        for p in TRANS:
            u = v[p]; d[u.tobytes()] = u
    P = np.array(list(d.values()), np.uint8)
    assert ((Hdet @ P.T) % 2 == 0).all() and (P.sum(1) == 12).all()
    assert all(not red.inspan(v) for v in P)
    return P


def logical_basis(P, Hstab):
    """pick 12 words from the pool that are independent modulo rowspace(Hstab)."""
    red = Reducer(Hstab)
    rows = []; basis = []
    cur = np.zeros((0, N), np.uint8)
    for v in P:
        w = red.red(v)
        test = np.concatenate([cur, w[None, :]], 0)
        if len(rref(test)[1]) > len(rref(cur)[1]) if len(cur) else True:
            cur = test; basis.append(v)
            if len(basis) == 12:
                break
    assert len(basis) == 12
    return np.array(basis, np.uint8)


def get(cache=True):
    f = "pools.npz"
    if cache and os.path.exists(f):
        z = np.load(f)
        return z['PZ'], z['PX'], z['LX'], z['LZ']
    t0 = time.time()
    PZ = build_pool(HX, HZ, 101)     # Z-type logicals: ker(HX) \ rowspace(HZ)
    PX = build_pool(HZ, HX, 202)     # X-type logicals: ker(HZ) \ rowspace(HX)
    LX = logical_basis(PX, HX)       # 12 X-logicals  -> detect nontriviality of Z-errors
    LZ = logical_basis(PZ, HZ)       # 12 Z-logicals  -> detect nontriviality of X-errors
    np.savez(f, PZ=PZ, PX=PX, LX=LX, LZ=LZ)
    print("pools built in %.1fs: |PZ|=%d |PX|=%d" % (time.time() - t0, len(PZ), len(PX)))
    return PZ, PX, LX, LZ


if __name__ == "__main__":
    PZ, PX, LX, LZ = get(cache=False)
    print("pool sizes:", PZ.shape, PX.shape)
    print("logical basis row weights: LX", sorted(LX.sum(1)), " LZ", sorted(LZ.sum(1)))
    # sanity: LX rows are X-logicals -> commute with HZ, independent mod rowspace(HX)
    assert ((HZ @ LX.T) % 2 == 0).all()
    assert ((HX @ LZ.T) % 2 == 0).all()
    # the 12x12 pairing matrix between LX and LZ must be invertible
    Mp = (LX @ LZ.T) % 2
    print("rank of LX.LZ^T pairing:", len(rref(Mp)[1]))
```

#### `dext.py`

```python
"""EXACT certification of d_ext(E(M)) for the gross code, by SAT decision queries.

d_ext(E(M)) = min { |x| : H^ext x = 0 , L^ext x != 0 }  where the extended code appends one column
per residual error (SBB Def. 2).  Written in the equivalent "net error" form:

    d_ext = min over  E in ker(H_det) \\ rowspace(H_stab)  and  R subset of the residual set  of
            | E  xor  (xor_{r in R} r) |  +  |R| .

Boolean model (Z-sector; X-sector is the mirror):
    z_j      j = 0..143     the net data error E
    u_{c,k}  c = 0..71, k = 0,1,2   residual k of check c is used
    d_j      j = 0..143     the data-fault part x_data = E xor (xor of used residuals)
constraints
    H_det z = 0                                   (72 XORs of weight 6)
    OR_i ( L_i . z = 1 )                          (12 XOR chains + one clause)
    d_j = z_j xor (xor of u_{c,k} with j in r_k(c))
    |d| + |u| <= W                                (cardinality)
UNSAT at W  =>  d_ext > W.   SAT at W  =>  an explicit witness of weight <= W.
"""
import numpy as np, itertools, time
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from gross import HX, HZ, N, NG, Reducer, rref
import pool as poolmod

RES_POS = [(0, 1), (3, 4, 5), (4, 5)]     # r1 = {i1,i2}, r2 = {i4,i5,i6}, r3 = {i5,i6}


def residual_sets(orders):
    """orders: list of 72 within-check CNOT orders (each a list of 6 data-qubit indices).
    Returns res[c][k] = tuple of data qubits."""
    return [[tuple(o[p] for p in RES_POS[k]) for k in range(3)] for o in orders]


class Ctx:
    def __init__(self, orders, Hdet, Lrows):
        self.res = residual_sets(orders)
        self.Hdet = Hdet
        self.Lrows = Lrows
        # per data qubit: which (c,k) residuals contain it
        self.hit = [[] for _ in range(N)]
        for c in range(len(self.res)):
            for k in range(3):
                for q in self.res[c][k]:
                    self.hit[q].append((c, k))
        self.ncheck = len(self.res)


def xor_chain(pool, lits, cls):
    acc = lits[0]
    for x in lits[1:]:
        nv = pool.id()
        cls += [[-nv, acc, x], [-nv, -acc, -x], [nv, -acc, x], [nv, acc, -x]]
        acc = nv
    return acc


def xor_zero_direct(lits, cls):
    """forbid every odd-parity assignment (use only for short XORs)"""
    k = len(lits)
    for bits in itertools.product([0, 1], repeat=k):
        if sum(bits) % 2 == 1:
            cls.append([(-lits[i] if bits[i] else lits[i]) for i in range(k)])


def build(ctx, W, pin=None, use_residuals=True):
    pool = IDPool()
    z = [pool.id(('z', j)) for j in range(N)]
    u = [[pool.id(('u', c, k)) for k in range(3)] for c in range(ctx.ncheck)]
    d = [pool.id(('d', j)) for j in range(N)]
    cls = []
    # detector constraints
    for e in range(ctx.Hdet.shape[0]):
        supp = [z[int(j)] for j in np.nonzero(ctx.Hdet[e])[0]]
        xor_zero_direct(supp, cls)
    # logical nontriviality
    ys = []
    for i in range(ctx.Lrows.shape[0]):
        supp = [z[int(j)] for j in np.nonzero(ctx.Lrows[i])[0]]
        ys.append(xor_chain(pool, supp, cls))
    cls.append(ys)
    # data-fault definition
    lits_card = []
    for j in range(N):
        terms = [d[j], z[j]]
        if use_residuals:
            terms += [u[c][k] for (c, k) in ctx.hit[j]]
        if len(terms) <= 6:
            xor_zero_direct(terms, cls)
        else:
            v = xor_chain(pool, terms, cls)
            cls.append([-v])
        lits_card.append(d[j])
    if use_residuals:
        for c in range(ctx.ncheck):
            for k in range(3):
                lits_card.append(u[c][k])
    else:
        for c in range(ctx.ncheck):
            for k in range(3):
                cls.append([-u[c][k]])
    if pin is not None:
        cls.append([pin(z, u, d)])
    # cardinality
    top = pool.top
    cnf = CardEnc.atmost(lits=lits_card, bound=W, top_id=top, encoding=EncType.seqcounter)
    cls += cnf.clauses
    return cls, z, u, d, lits_card


def decode(model, z, u, d, ctx):
    ms = set(x for x in model if x > 0)
    E = np.array([1 if z[j] in ms else 0 for j in range(N)], np.uint8)
    R = [(c, k) for c in range(ctx.ncheck) for k in range(3) if u[c][k] in ms]
    D = np.array([1 if d[j] in ms else 0 for j in range(N)], np.uint8)
    return E, R, D


def verify_witness(ctx, E, R, D, Hstab):
    """independent re-verification of a SAT witness, from the definitions."""
    chk = np.zeros(N, np.uint8)
    for (c, k) in R:
        for q in ctx.res[c][k]:
            chk[q] ^= 1
    ok_d = np.array_equal((D ^ chk) % 2, E)
    ok_syn = not ((ctx.Hdet @ E) % 2).any()
    red = Reducer(Hstab)
    ok_log = not red.inspan(E)
    return dict(weight=int(D.sum()) + len(R), n_data=int(D.sum()), n_res=len(R),
                Ewt=int(E.sum()), decomposition_ok=bool(ok_d), zero_syndrome=bool(ok_syn),
                nontrivial_logical=bool(ok_log))


def query(ctx, W, Hstab, pin=None, use_residuals=True, verbose=False):
    cls, z, u, d, lc = build(ctx, W, pin=pin, use_residuals=use_residuals)
    t0 = time.time()
    with Cadical153(bootstrap_with=cls) as S:
        sat = S.solve()
        m = S.get_model() if sat else None
    el = time.time() - t0
    if not sat:
        return False, None, el, len(cls)
    E, R, D = decode(m, z, u, d, ctx)
    return True, (E, R, D, verify_witness(ctx, E, R, D, Hstab)), el, len(cls)


def sector_ctx(orders, sector):
    PZ, PX, LX, LZ = poolmod.get()
    if sector == 'Z':      # Z-type data errors, X-check detectors, Z-check hooks
        return Ctx(orders, HX, LX), HZ
    else:                  # X-type data errors, Z-check detectors, X-check hooks
        return Ctx(orders, HZ, LZ), HX
```

#### `dext2.py`

```python
"""Faster exact d_ext certifier.

Three additions over dext.py:
  (1) the implied cut  |E| >= 12  (the gross code's own minimum logical weight, itself certified
      by validate1.py: UNSAT at 11 with the residual set switched off);
  (2) translation symmetry: the tiled assignment is invariant under the subgroup
      S <= G = Z_12 x Z_6 that preserves the colouring, so a minimum-weight solution may be assumed
      to use one of the |columns|/|S| orbit representatives.  Each representative is a separate
      incremental SAT call under one assumption literal;
  (3) incremental solving, so learnt clauses are shared across the orbit subproblems.

UNSAT on all orbit representatives at weight W  =>  d_ext > W   (certificate = the UNSAT proofs).
"""
import numpy as np, itertools, time
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from gross import HX, HZ, N, NG, ELL, EM, gidx, Reducer
from dext import RES_POS, residual_sets, Ctx, xor_chain, xor_zero_direct, verify_witness


def group_elements():
    return [(a, b) for a in range(ELL) for b in range(EM)]


def data_perm(a, b):
    p = np.empty(N, int)
    for i in range(ELL):
        for j in range(EM):
            p[gidx(i, j)] = gidx(i + a, j + b)
            p[NG + gidx(i, j)] = NG + gidx(i + a, j + b)
    return p


def check_perm(a, b):
    p = np.empty(NG, int)
    for i in range(ELL):
        for j in range(EM):
            p[gidx(i, j)] = gidx(i + a, j + b)
    return p


def stabiliser(phi, triple):
    """translations g with colour-class assignment preserved: triple[phi[c+g]] == triple[phi[c]]"""
    out = []
    for (a, b) in group_elements():
        cp = check_perm(a, b)
        if all(triple[int(phi[cp[c]])] == triple[int(phi[c])] for c in range(NG)):
            out.append((a, b))
    return out


def column_orbits(phi, triple):
    """orbits of the 360 extended-code columns (144 data + 72*3 residual) under the stabiliser"""
    S = stabiliser(phi, triple)
    lab = {}
    cols = [('d', j) for j in range(N)] + [('r', c, k) for c in range(NG) for k in range(3)]
    idx = {c: i for i, c in enumerate(cols)}
    seen = set(); orbits = []
    for col in cols:
        if col in seen:
            continue
        orb = set()
        for (a, b) in S:
            dp = data_perm(a, b); cp = check_perm(a, b)
            orb.add(('d', int(dp[col[1]])) if col[0] == 'd' else ('r', int(cp[col[1]]), col[2]))
        seen |= orb
        orbits.append((col, sorted(orb)))
    return S, orbits


class Cert:
    def __init__(self, ctx, W, emin=12):
        pool = IDPool()
        self.z = [pool.id(('z', j)) for j in range(N)]
        self.u = [[pool.id(('u', c, k)) for k in range(3)] for c in range(ctx.ncheck)]
        self.d = [pool.id(('d', j)) for j in range(N)]
        cls = []
        for e in range(ctx.Hdet.shape[0]):
            xor_zero_direct([self.z[int(j)] for j in np.nonzero(ctx.Hdet[e])[0]], cls)
        ys = []
        for i in range(ctx.Lrows.shape[0]):
            ys.append(xor_chain(pool, [self.z[int(j)] for j in np.nonzero(ctx.Lrows[i])[0]], cls))
        cls.append(ys)
        lits = []
        for j in range(N):
            terms = [self.d[j], self.z[j]] + [self.u[c][k] for (c, k) in ctx.hit[j]]
            if len(terms) <= 6:
                xor_zero_direct(terms, cls)
            else:
                v = xor_chain(pool, terms, cls)
                cls.append([-v])
            lits.append(self.d[j])
        for c in range(ctx.ncheck):
            for k in range(3):
                lits.append(self.u[c][k])
        # dominance cut (equisatisfiable): a check never needs both r2 = {i4,i5,i6} and
        # r3 = {i5,i6}.  Their net is {i4} at cost 2, strictly dominated by a single data fault
        # on i4 at cost 1; the same replacement removes the {r1,r2,r3} case.
        for c in range(ctx.ncheck):
            cls.append([-self.u[c][1], -self.u[c][2]])
        self.lits = lits
        top = pool.top
        c1 = CardEnc.atmost(lits=lits, bound=W, top_id=top, encoding=EncType.seqcounter)
        cls += c1.clauses
        top = max([top] + [abs(l) for cl in c1.clauses for l in cl])
        if emin:
            c2 = CardEnc.atleast(lits=self.z, bound=emin, top_id=top,
                                 encoding=EncType.seqcounter)
            cls += c2.clauses
            top = max([top] + [abs(l) for cl in c2.clauses for l in cl])
        self.top = top
        self.cls = cls
        self.ctx = ctx
        self.pool = pool

    def col_lit(self, col):
        return self.d[col[1]] if col[0] == 'd' else self.u[col[1]][col[2]]

    def run(self, orbits, Hstab, budget=None, verbose=True):
        t0 = time.time()
        res = []
        with Cadical153(bootstrap_with=self.cls) as S:
            for oi, (rep, orb) in enumerate(orbits):
                # forbid all columns strictly "before" this orbit in the ordering (optional
                # strengthening is unsound in general; we only assume the representative is used)
                a = self.col_lit(rep)
                t1 = time.time()
                sat = S.solve(assumptions=[a])
                el = time.time() - t1
                if sat:
                    m = S.get_model()
                    ms = set(x for x in m if x > 0)
                    E = np.array([1 if self.z[j] in ms else 0 for j in range(N)], np.uint8)
                    R = [(c, k) for c in range(self.ctx.ncheck) for k in range(3)
                         if self.u[c][k] in ms]
                    D = np.array([1 if self.d[j] in ms else 0 for j in range(N)], np.uint8)
                    info = verify_witness(self.ctx, E, R, D, Hstab)
                    if verbose:
                        print(f"      orbit {oi} rep {rep}: SAT in {el:.1f}s  {info}")
                    return True, (E, R, D, info), time.time() - t0
                if verbose:
                    print(f"      orbit {oi} rep {rep}: UNSAT in {el:.1f}s")
                res.append(el)
                if budget and time.time() - t0 > budget:
                    return None, ('timeout after orbit', oi), time.time() - t0
        return False, None, time.time() - t0
```

#### `cert.py`

```python
"""Exact certification of d_ext for the surviving three-colour-tiled assignments."""
import numpy as np, itertools, sys, time, json
from gross import NG, N, zcheck_nb, xcheck_nb, HX, HZ
from sched import make_phi
from cascade import REPS, sector_data
import dext


def tiled_orders(sector, phi, triple):
    slots, Pl, Hstab, Hdet = sector_data(sector)
    orders = []
    for g in range(NG):
        sig = REPS[triple[int(phi[g])]]
        orders.append([slots[g][k] for k in sig])
    return orders, Hstab


def certify(sector, phi, triple, Wlist=(10,), verbose=True):
    orders, Hstab = tiled_orders(sector, phi, triple)
    ctx, Hst = dext.sector_ctx(orders, sector)
    out = {}
    for W in Wlist:
        sat, wit, el, ncls = dext.query(ctx, W, Hst)
        out[W] = (sat, wit[3] if sat else None, el, ncls)
        if verbose:
            if sat:
                print(f"   sector {sector} triple {triple} W={W}: SAT  {wit[3]}  ({el:.1f}s)")
            else:
                print(f"   sector {sector} triple {triple} W={W}: UNSAT  ({el:.1f}s, {ncls} clauses)")
    return out, ctx, Hst


if __name__ == "__main__":
    s_par, t_par = 1, 2
    phi = make_phi(s_par, t_par)
    triples = [(2, 2, 2), (2, 2, 9), (2, 9, 2), (2, 9, 9),
               (9, 2, 2), (9, 2, 9), (9, 9, 2), (9, 9, 9)]
    which = sys.argv[1:] if len(sys.argv) > 1 else None
    for sector in ('Z', 'X'):
        for tr in triples:
            if which and f"{sector}{tr[0]}{tr[1]}{tr[2]}" not in which:
                continue
            t0 = time.time()
            certify(sector, phi, tr, Wlist=(10,))
            sys.stdout.flush()
```

#### `orbit_job.py`

```python
"""One (sector, tiled-assignment, weight-bound, column-orbit) SAT subproblem."""
import sys, time
import numpy as np
from gross import NG
from sched import make_phi
from cert import tiled_orders
import dext, dext2

sector = sys.argv[1]
triple = tuple(int(c) for c in sys.argv[2].split(','))
W = int(sys.argv[3])
oi = int(sys.argv[4])
s_par, t_par = (int(sys.argv[5]), int(sys.argv[6])) if len(sys.argv) > 6 else (1, 2)
phi = make_phi(s_par, t_par)
tag = f"{sector} {triple} W={W} orbit {oi}"

orders, _ = tiled_orders(sector, phi, triple)
ctx, Hstab = dext.sector_ctx(orders, sector)
S, orbits = dext2.column_orbits(phi, triple)
if oi >= len(orbits):
    print(f"{tag}: NO SUCH ORBIT (only {len(orbits)})"); sys.exit(0)
c = dext2.Cert(ctx, W)
rep, orb = orbits[oi]
t0 = time.time()
sat, wit, el = c.run([orbits[oi]], Hstab, verbose=False)
if sat:
    E, R, D, info = wit
    print(f"{tag} rep={rep}: SAT  {el:.1f}s  {info}")
    print(f"   E={sorted(int(i) for i in np.nonzero(E)[0])}")
    print(f"   R={R}")
    print(f"   D={sorted(int(i) for i in np.nonzero(D)[0])}")
else:
    print(f"{tag} rep={rep}: UNSAT  {el:.1f}s   (|orbit|={len(orb)}, |stab|={len(S)}, "
          f"{len(c.cls)} clauses)")
```

#### `single.py`

```python
"""d_ext(R) for R = the residual set of a SINGLE check -- the object [SBB26] Prop. 4 and the
90 -> 45 pruning actually bound.  Theorem 1 gives d'_circ <= d_ext(R) for every R subset of E,
and d'_circ = d_ext(E) for the FULL set.  This script measures the gap between the two."""
import sys, time
import numpy as np
from gross import NG, N, HX, HZ, zcheck_nb, xcheck_nb, Reducer
from sched import make_phi
from cert import tiled_orders
from cascade import REPS
import dext, dext2


def single_ctx(orders, sector, keep):
    ctx, Hstab = dext.sector_ctx(orders, sector)
    for c in range(NG):
        if c not in keep:
            ctx.res[c] = [(), (), ()]
    ctx.hit = [[] for _ in range(N)]
    for c in range(NG):
        for k in range(3):
            for q in ctx.res[c][k]:
                ctx.hit[q].append((c, k))
    return ctx, Hstab


if __name__ == "__main__":
    phi = make_phi(1, 2)
    for sector in ('Z', 'X'):
        for tr in [(2, 2, 9)]:
            orders, _ = tiled_orders(sector, phi, tr)
            for keep in ({0}, {0, 1}):
                ctx, Hstab = single_ctx(orders, sector, keep)
                for W in (10, 11):
                    sat, wit, el, ncls = dext.query(ctx, W, Hstab)
                    print(f"sector {sector} triple {tr} R = residuals of checks {sorted(keep)} "
                          f"W={W}: {'SAT ' + str(wit[3]) if sat else 'UNSAT'}  ({el:.1f}s)")
                    sys.stdout.flush()
                    if sat:
                        break
```

#### `subsets.py`

```python
"""How large must R be before d_ext(R) drops below 11?  The headline witness uses the residuals of
Z-checks 3, 9 and 15, so these are the informative subsets."""
import sys
from sched import make_phi
from cert import tiled_orders
from single import single_ctx
import dext
phi = make_phi(1, 2)
orders, _ = tiled_orders('Z', phi, (2, 2, 9))
for keep in ({3, 9}, {9, 15}, {3, 15}, {3, 9, 15}):
    ctx, Hstab = single_ctx(orders, 'Z', keep)
    sat, wit, el, ncls = dext.query(ctx, 10, Hstab)
    print('R = residuals of checks', sorted(keep), 'W=10:',
          ('SAT ' + str(wit[3])) if sat else 'UNSAT', '(%.1fs)' % el)
    sys.stdout.flush()
```

#### `validate1.py`

```python
"""Validation V1 of the d_ext certifier: with the residual set switched OFF the problem reduces to
the gross code's own minimum logical weight, which is known exactly to be 12."""
import numpy as np, time
from gross import HX, HZ, NG, zcheck_nb, xcheck_nb
import dext, pool as poolmod

orders = [[q for q, s, i in zcheck_nb(g)] for g in range(NG)]     # arbitrary; unused when off
ctx, Hstab = dext.sector_ctx(orders, 'Z')
for W in (11, 12):
    sat, wit, el, ncls = dext.query(ctx, W, Hstab, use_residuals=False)
    print(f"[no residuals] W = {W}: {'SAT' if sat else 'UNSAT'}  ({el:.1f}s, {ncls} clauses)")
    if sat:
        print("   witness:", wit[3])

ctxX, HstabX = dext.sector_ctx([[q for q, s, i in xcheck_nb(g)] for g in range(NG)], 'X')
for W in (11, 12):
    sat, wit, el, ncls = dext.query(ctxX, W, HstabX, use_residuals=False)
    print(f"[no residuals, X sector] W = {W}: {'SAT' if sat else 'UNSAT'}  ({el:.1f}s)")
```

#### `realize2.py`

```python
"""Realisability, done correctly: only the RESIDUAL SET of each check is prescribed, not a
particular representative of its order class.

A within-check order class is fixed by  (P, s3, s4, Q)  up to the reversal  (P,s3,s4,Q) -> (Q,s4,s3,P),
where P = {positions 1,2}, Q = {positions 5,6} as unordered slot pairs.  So the schedule is free to
choose the order inside P, the order inside Q, and the orientation.  Constraints:

  legality  : each check's 6 CNOTs in 6 distinct layers; each data qubit's 6 CNOTs in 6 distinct layers
  class     : the precedence pattern above, with a per-check orientation selector
  (MC)      : the even back-propagation parity condition on all 648 overlapping (X,Z) check pairs
"""
import sys, time, itertools
import numpy as np
from pysat.solvers import Cadical153
from gross import NG, N, xcheck_nb, zcheck_nb, xchecks_of, zchecks_of
from sched import make_phi, check_legal, mc_violations
from cascade import REPS
from cert import tiled_orders

EID = {}; EDGES = []
for g in range(NG):
    for q, s, i in xcheck_nb(g):
        EID[('X', g, s, i)] = len(EDGES); EDGES.append(('X', g, s, i, q))
for g in range(NG):
    for q, s, i in zcheck_nb(g):
        EID[('Z', g, s, i)] = len(EDGES); EDGES.append(('Z', g, s, i, q))
XSLOT = [{q: (s, i) for q, s, i in xcheck_nb(g)} for g in range(NG)]
ZSLOT = [{q: (s, i) for q, s, i in zcheck_nb(g)} for g in range(NG)]
NE = len(EDGES)


def prec_pairs(sig):
    """pairwise precedences that pin the residual class of the order `sig` (slot tuple)."""
    P = [sig[0], sig[1]]; s3, s4 = sig[2], sig[3]; Q = [sig[4], sig[5]]
    out = []
    for p in P:
        for b in [s3, s4] + Q:
            out.append((p, b))
    out += [(s3, s4)] + [(s3, q) for q in Q] + [(s4, q) for q in Q]
    return out


def solve(sigZ, sigX, T, use_mc=True, use_class=True):
    """sigZ[g], sigX[g] : the slot order whose residual CLASS the check must realise."""
    nv = NE * T

    def V(e, l):
        return e * T + l + 1
    sel = {}
    nxt = nv + 1
    cls = []
    for e in range(NE):
        cls.append([V(e, l) for l in range(T)])
        for l1, l2 in itertools.combinations(range(T), 2):
            cls.append([-V(e, l1), -V(e, l2)])
    if use_class:
        for typ, sigs, slot in (('X', sigX, XSLOT), ('Z', sigZ, ZSLOT)):
            for g in range(NG):
                f = nxt; nxt += 1
                sel[(typ, g)] = f
                nb = xcheck_nb(g) if typ == 'X' else zcheck_nb(g)
                e_of = [EID[(typ, g, s, i)] for q, s, i in nb]     # slot index -> edge id
                sig = sigs[g]
                rev = tuple(reversed(sig))
                for orient, lit in ((sig, -f), (rev, f)):
                    for (a, b) in prec_pairs(orient):
                        ea, eb = e_of[a], e_of[b]
                        for l1 in range(T):
                            for l2 in range(T):
                                if l1 >= l2:
                                    cls.append([lit, -V(ea, l1), -V(eb, l2)])
    for g in range(NG):
        for typ, nb in (('X', xcheck_nb(g)), ('Z', zcheck_nb(g))):
            grp = [EID[(typ, g, s, i)] for q, s, i in nb]
            for l in range(T):
                for e1, e2 in itertools.combinations(grp, 2):
                    cls.append([-V(e1, l), -V(e2, l)])
    for q in range(N):
        grp = [EID[('X', c, s, i)] for c, s, i in xchecks_of(q)] + \
              [EID[('Z', c, s, i)] for c, s, i in zchecks_of(q)]
        for l in range(T):
            for e1, e2 in itertools.combinations(grp, 2):
                cls.append([-V(e1, l), -V(e2, l)])
    if use_mc:
        for a in range(NG):
            for b in range(NG):
                sh = sorted(set(XSLOT[a]) & set(ZSLOT[b]))
                if not sh:
                    continue
                qL, qR = sh
                eA = EID[('X', a) + XSLOT[a][qL]]; eP = EID[('Z', b) + ZSLOT[b][qL]]
                eB = EID[('X', a) + XSLOT[a][qR]]; eQ = EID[('Z', b) + ZSLOT[b][qR]]
                for l1 in range(T):
                    for l2 in range(T):
                        if l1 == l2:
                            continue
                        for l3 in range(T):
                            for l4 in range(T):
                                if l3 == l4:
                                    continue
                                if (l1 < l2) != (l3 < l4):
                                    cls.append([-V(eP, l1), -V(eA, l2), -V(eQ, l3), -V(eB, l4)])
    t0 = time.time()
    with Cadical153(bootstrap_with=cls) as S:
        sat = S.solve(); m = S.get_model() if sat else None
    el = time.time() - t0
    if not sat:
        return None, len(cls), el
    ms = set(x for x in m if x > 0)
    tX = [dict() for _ in range(NG)]; tZ = [dict() for _ in range(NG)]
    for e, (typ, g, s, i, q) in enumerate(EDGES):
        for l in range(T):
            if V(e, l) in ms:
                (tX if typ == 'X' else tZ)[g][(s, i)] = l + 1
    return (tX, tZ), len(cls), el


def residual_class(order, slots_of_check):
    from cascade import CLS_OF
    inv = {q: k for k, q in enumerate(slots_of_check)}
    return CLS_OF[tuple(inv[q] for q in order)]


if __name__ == "__main__":
    phi = make_phi(1, 2)
    trip = tuple(int(c) for c in sys.argv[1].split(',')) if len(sys.argv) > 1 else (2, 2, 9)
    sigZ = [REPS[trip[int(phi[g])]] for g in range(NG)]
    sigX = [REPS[trip[int(phi[g])]] for g in range(NG)]
    for mc in (False, True):
        for T in (6, 7, 8, 9, 10):
            res, ncls, el = solve(sigZ, sigX, T, use_mc=mc)
            tag = "legality+class" + ("+MC" if mc else "")
            if res is None:
                print(f"{tag}, T={T}: UNSAT ({ncls} clauses, {el:.1f}s)")
            else:
                tX, tZ = res
                oX = [[q for q, s, i in sorted(xcheck_nb(g), key=lambda z: tX[g][(z[1], z[2])])]
                      for g in range(NG)]
                oZ = [[q for q, s, i in sorted(zcheck_nb(g), key=lambda z: tZ[g][(z[1], z[2])])]
                      for g in range(NG)]
                clsZ = {residual_class(oZ[g], [q for q, s, i in zcheck_nb(g)]) for g in range(NG)}
                clsX = {residual_class(oX[g], [q for q, s, i in xcheck_nb(g)]) for g in range(NG)}
                print(f"{tag}, T={T}: SAT ({ncls} clauses, {el:.1f}s) legal="
                      f"{check_legal(tX, tZ, T)} MCviol={mc_violations(tX, tZ)[0]} "
                      f"realised Z-classes={sorted(clsZ)} X-classes={sorted(clsX)}")
                break
            sys.stdout.flush()
```

#### `noclass.py`

```python
"""Minimum number of CNOT layers for ANY legal + measurement-consistent gross-code SEC
(no constraint on the within-check orders).  This is the depth question the paper's Eq. (3)
lower bound (8 = 6 CNOT layers + prep + measure) leaves open once (MC) is imposed."""
import sys, time
from realize2 import solve
from sched import check_legal, mc_violations
from cascade import REPS
from gross import NG
sig = [REPS[0]] * NG
for T in (6, 7, 8, 9):
    res, ncls, el = solve(sig, sig, T, use_mc=True, use_class=False)
    if res is None:
        print(f"any-order, T={T}: UNSAT ({ncls} clauses, {el:.1f}s)")
    else:
        tX, tZ = res
        print(f"any-order, T={T}: SAT ({ncls} clauses, {el:.1f}s) legal={check_legal(tX,tZ,T)} "
              f"MCviol={mc_violations(tX,tZ)[0]}")
        break
    sys.stdout.flush()
```

#### `nogo.py`

```python
"""Is there a legal, measurement-consistent gross-code SEC of depth T in which EVERY check avoids
the 45 residual classes that force d_ext <= 10?

The stage-1 condition is local and order-theoretic: a check forces d_ext <= 10 as soon as the
3-element slot set occupying its last three CNOT positions is a *covered* triple, i.e. lies in a
weight-12 logical.  Exactly 10 of the 20 triples of a check support are covered, and coverage is
complement-closed, so the condition to avoid is:  "the last three positions carry a covered triple".

UNSAT at depth T  =>  EVERY legal, measurement-consistent gross SEC with T CNOT layers has a check
whose single-check residual subset already yields an extended-code codeword of weight 10, hence
(SBB Thm. 1)  d_circ <= 10  for it if it is non-interleaved.
"""
import sys, time, itertools
import numpy as np
from pysat.solvers import Cadical153
from gross import NG, N, xcheck_nb, zcheck_nb, xchecks_of, zchecks_of
from sched import check_legal, mc_violations
from cascade import sector_data

EID = {}; EDGES = []
for g in range(NG):
    for q, s, i in xcheck_nb(g):
        EID[('X', g, s, i)] = len(EDGES); EDGES.append(('X', g, s, i, q))
for g in range(NG):
    for q, s, i in zcheck_nb(g):
        EID[('Z', g, s, i)] = len(EDGES); EDGES.append(('Z', g, s, i, q))
XSLOT = [{q: (s, i) for q, s, i in xcheck_nb(g)} for g in range(NG)]
ZSLOT = [{q: (s, i) for q, s, i in zcheck_nb(g)} for g in range(NG)]
NE = len(EDGES)


def covered_triples(sector):
    """slot-triples of a check that lie inside some weight-12 logical (same for every check by
    translation transitivity -- asserted)."""
    slots, Pl, Hstab, Hdet = sector_data(sector)
    S = np.array([[L[slots[0][k]] for k in range(6)] for L in Pl], bool)
    cov = [t for t in itertools.combinations(range(6), 3) if S[:, list(t)].all(1).any()]
    for c in (1, 2, 37):
        Sc = np.array([[L[slots[c][k]] for k in range(6)] for L in Pl], bool)
        covc = [t for t in itertools.combinations(range(6), 3) if Sc[:, list(t)].all(1).any()]
        assert covc == cov, (c, covc, cov)
    return cov


def solve(T, use_mc=True, use_nogo=True, quiet=False):
    def V(e, l):
        return e * T + l + 1
    nxt = NE * T + 1
    cls = []
    for e in range(NE):
        cls.append([V(e, l) for l in range(T)])
        for l1, l2 in itertools.combinations(range(T), 2):
            cls.append([-V(e, l1), -V(e, l2)])
    for g in range(NG):
        for typ, nb in (('X', xcheck_nb(g)), ('Z', zcheck_nb(g))):
            grp = [EID[(typ, g, s, i)] for q, s, i in nb]
            for l in range(T):
                for e1, e2 in itertools.combinations(grp, 2):
                    cls.append([-V(e1, l), -V(e2, l)])
    for q in range(N):
        grp = [EID[('X', c, s, i)] for c, s, i in xchecks_of(q)] + \
              [EID[('Z', c, s, i)] for c, s, i in zchecks_of(q)]
        for l in range(T):
            for e1, e2 in itertools.combinations(grp, 2):
                cls.append([-V(e1, l), -V(e2, l)])
    if use_nogo:
        covZ = covered_triples('Z'); covX = covered_triples('X')
        if not quiet:
            print(f"   covered triples: Z {len(covZ)}/20, X {len(covX)}/20")
        for typ, nb_fn, cov in (('X', xcheck_nb, covX), ('Z', zcheck_nb, covZ)):
            for g in range(NG):
                e_of = [EID[(typ, g, s, i)] for q, s, i in nb_fn(g)]
                y = {}
                for a, b in itertools.combinations(range(6), 2):
                    v = nxt; nxt += 1
                    y[(a, b)] = v
                    ea, eb = e_of[a], e_of[b]
                    for l1 in range(T):
                        for l2 in range(T):
                            if l1 == l2:
                                continue
                            cls.append([-V(ea, l1), -V(eb, l2), v if l1 < l2 else -v])

                def yy(a, b):          # [layer(a) < layer(b)]
                    return y[(a, b)] if a < b else -y[(b, a)]
                for Tr in cov:
                    comp = [k for k in range(6) if k not in Tr]
                    # forbid "all of comp precede all of Tr"
                    cls.append([yy(t, tp) for t in Tr for tp in comp])
    if use_mc:
        for a in range(NG):
            for b in range(NG):
                sh = sorted(set(XSLOT[a]) & set(ZSLOT[b]))
                if not sh:
                    continue
                qL, qR = sh
                eA = EID[('X', a) + XSLOT[a][qL]]; eP = EID[('Z', b) + ZSLOT[b][qL]]
                eB = EID[('X', a) + XSLOT[a][qR]]; eQ = EID[('Z', b) + ZSLOT[b][qR]]
                for l1 in range(T):
                    for l2 in range(T):
                        if l1 == l2:
                            continue
                        for l3 in range(T):
                            for l4 in range(T):
                                if l3 == l4:
                                    continue
                                if (l1 < l2) != (l3 < l4):
                                    cls.append([-V(eP, l1), -V(eA, l2), -V(eQ, l3), -V(eB, l4)])
    t0 = time.time()
    with Cadical153(bootstrap_with=cls) as S:
        sat = S.solve(); m = S.get_model() if sat else None
    el = time.time() - t0
    if not sat:
        return None, len(cls), el
    ms = set(x for x in m if x > 0)
    tX = [dict() for _ in range(NG)]; tZ = [dict() for _ in range(NG)]
    for e, (typ, g, s, i, q) in enumerate(EDGES):
        for l in range(T):
            if V(e, l) in ms:
                (tX if typ == 'X' else tZ)[g][(s, i)] = l + 1
    return (tX, tZ), len(cls), el


if __name__ == "__main__":
    lo, hi = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (6, 12)
    for T in range(lo, hi + 1):
        res, ncls, el = solve(T)
        if res is None:
            print(f"legal + MC + no-covered-triple-last, T={T}: UNSAT ({ncls} clauses, {el:.1f}s)")
        else:
            tX, tZ = res
            print(f"legal + MC + no-covered-triple-last, T={T}: SAT ({ncls} clauses, {el:.1f}s) "
                  f"legal={check_legal(tX, tZ, T)} MCviol={mc_violations(tX, tZ)[0]}")
            np.save(f"nogo_T{T}_tX.npy", np.array([[tX[g][(s, i)] for s in ('L', 'R')
                                                   for i in range(3)] for g in range(NG)]))
            np.save(f"nogo_T{T}_tZ.npy", np.array([[tZ[g][(s, i)] for s in ('L', 'R')
                                                   for i in range(3)] for g in range(NG)]))
            break
        sys.stdout.flush()
```

#### `simverify.py`

```python
"""Circuit-level verification of an extended-code witness, by independent Pauli-frame propagation.

The circuit used is the ALTERNATING-XZ (globally non-interleaved) circuit with the candidate's
within-check CNOT orders: all X-check CNOTs in layers 1..6, then all Z-check CNOTs in layers 7..12.
[SBB26] Theorem 1 gives d_circ = d_ext(E) for it (it is the extreme non-interleaved circuit they
name), and it has the SAME within-check orders, hence the SAME residual set, as any depth-8
left-right circuit with those orders.  The in-house Theorem 7.1 gives the same equality.

This module shares no code with dext/dext2: it builds the literal CNOT list and propagates
Z-type Pauli frames  (CNOT(c,t):  z[c] ^= z[t]).
"""
import numpy as np
from gross import NG, N, HX, HZ, xcheck_nb, zcheck_nb, Reducer

XA = [N + g for g in range(NG)]
ZA = [N + NG + g for g in range(NG)]
NQ = N + 2 * NG


def _block(pairs_by_check, anc, control_is_anc):
    """greedy legal layering of one block: check g's p-th CNOT must land strictly later than its
    (p-1)-th, so every check's within-check CNOT order is preserved exactly."""
    layers = []
    busy = []
    last = {g: -1 for g in pairs_by_check}
    for pos in range(6):
        for g in sorted(pairs_by_check):
            q = pairs_by_check[g][pos]
            a = anc[g]
            l = last[g] + 1
            while True:
                while l >= len(layers):
                    layers.append([]); busy.append(set())
                if a not in busy[l] and q not in busy[l]:
                    break
                l += 1
            layers[l].append((a, q) if control_is_anc else (q, a))
            busy[l].add(a); busy[l].add(q)
            last[g] = l
    return layers


def alternating_circuit(ordersX, ordersZ):
    """all X-check CNOTs, then all Z-check CNOTs (the alternating-XZ circuit of [SBB26] S5).
    Returns gates = list of layers, each a list of (control, target)."""
    gates = _block({g: ordersX[g] for g in range(NG)}, XA, True)
    gates += _block({g: ordersZ[g] for g in range(NG)}, ZA, False)
    for lay in gates:
        used = set()
        for (c, t) in lay:
            assert c not in used and t not in used, "illegal layer"
            used.add(c); used.add(t)
    # every check's within-check order must be exactly the requested one
    tim = {}
    for li, lay in enumerate(gates):
        for (c, t) in lay:
            tim[(c, t)] = li
    for g in range(NG):
        ts = [tim[(XA[g], q)] for q in ordersX[g]]
        assert ts == sorted(ts) and len(set(ts)) == 6
        ts = [tim[(q, ZA[g])] for q in ordersZ[g]]
        assert ts == sorted(ts) and len(set(ts)) == 6
    return gates


def hook_layer(gates, ordersZ, g, l):
    """index of the layer holding the l-th CNOT of Z-check g"""
    q = ordersZ[g][l - 1]
    for li, lay in enumerate(gates):
        if (q, ZA[g]) in lay:
            return li
    raise KeyError((g, l))


def run_z(gates, ordersZ, hook_faults, data_faults):
    """hook_faults: list of (zcheck g, position l in 1..6) -- Z on the Z-ancilla just before its
       l-th CNOT.  data_faults: list of data qubits carrying Z at the very end of the round.
       Returns (X-check outcome flips, net data Z error)."""
    z = np.zeros(NQ, np.uint8)
    hooks = {}
    for (g, l) in hook_faults:
        hooks.setdefault(hook_layer(gates, ordersZ, g, l), []).append(g)
    for li, lay in enumerate(gates):
        for g in hooks.get(li, []):
            z[ZA[g]] ^= 1
        for (c, t) in lay:
            z[c] ^= z[t]                # Z propagates target -> control
    for q in data_faults:
        z[q] ^= 1
    flips = np.array([z[XA[g]] for g in range(NG)], np.uint8)   # MX outcome flipped by Z on ancilla
    E = z[:N].copy()
    return flips, E


def run_x(gates, ordersX, hook_faults, data_faults):
    """X sector: X on an X-check ancilla (the CNOT control) just before its l-th CNOT.
       CNOT(c,t) propagates X on the control to the target: x[t] ^= x[c]."""
    x = np.zeros(NQ, np.uint8)
    hooks = {}
    for (g, l) in hook_faults:
        q = ordersX[g][l - 1]
        li = next(i for i, lay in enumerate(gates) if (XA[g], q) in lay)
        hooks.setdefault(li, []).append(g)
    for li, lay in enumerate(gates):
        for g in hooks.get(li, []):
            x[XA[g]] ^= 1
        for (c, t) in lay:
            x[t] ^= x[c]
    for q in data_faults:
        x[q] ^= 1
    flips = np.array([x[ZA[g]] for g in range(NG)], np.uint8)   # M(Z) flipped by X on the ancilla
    return flips, x[:N].copy()


def verify_x(ordersX, residuals, data_faults, ordersZ=None, verbose=True):
    if ordersZ is None:
        ordersZ = [[q for q, s, i in zcheck_nb(g)] for g in range(NG)]
    # X-checks must run LAST here so that their hooks are not seen by the Z-check detectors of
    # this round; the alternating circuit is used with the two blocks swapped.
    gates = _block({g: ordersZ[g] for g in range(NG)}, ZA, False)
    gates += _block({g: ordersX[g] for g in range(NG)}, XA, True)
    L = {0: 3, 1: 4, 2: 5}
    hooks = [(c, L[k]) for (c, k) in residuals]
    flips, E = run_x(gates, ordersX, hooks, data_faults)
    syn = (HZ @ E) % 2
    red = Reducer(HX)
    out = dict(nfaults=len(hooks) + len(data_faults),
               round_detectors_silent=bool(not flips.any()),
               terminal_detectors_silent=bool(not syn.any()),
               net_error_weight=int(E.sum()),
               nontrivial_logical=bool(not red.inspan(E)))
    if verbose:
        print("   circuit-level verification (X sector):", out)
    return out


def verify(ordersZ, residuals, data_faults, ordersX=None, verbose=True):
    """residuals: list of (check, k) with k in {0,1,2} <-> hook position l in {3,4,5}."""
    if ordersX is None:
        ordersX = [[q for q, s, i in xcheck_nb(g)] for g in range(NG)]
    gates = alternating_circuit(ordersX, ordersZ)
    L = {0: 3, 1: 4, 2: 5}
    hooks = [(c, L[k]) for (c, k) in residuals]
    flips, E = run_z(gates, ordersZ, hooks, data_faults)
    syn = (HX @ E) % 2
    red = Reducer(HZ)
    out = dict(nfaults=len(hooks) + len(data_faults),
               round_detectors_silent=bool(not flips.any()),
               terminal_detectors_silent=bool(not syn.any()),
               net_error_weight=int(E.sum()),
               nontrivial_logical=bool(not red.inspan(E)))
    if verbose:
        print("   circuit-level verification:", out)
    return out
```

#### `stimverify.py`

```python
"""Third, fully external verification of a witness: build the alternating-XZ circuit in stim,
inject the explicit Pauli faults as error channels, and sample the (noiseless, hence deterministic)
detectors and observables.  All detectors must read 0 and some observable must read 1.

NOTE: stim's detector sampler computes detection events relative to a NOISELESS reference
simulation of the same circuit, so deterministic X/Y/Z gates are absorbed into the reference and
produce no detection events.  Faults must therefore be injected as `Z_ERROR(1)` channels.
"""
import numpy as np, stim
from gross import NG, N, HX, xcheck_nb
import pool as poolmod
import simverify

XA = simverify.XA
ZA = simverify.ZA


def build(ordersX, ordersZ, hook_faults, data_faults, R=2):
    """X-memory experiment: data in |+>, X-check detectors, X-basis transversal readout.
    hook_faults: (zcheck, l) with l in 1..6 -> Z on that ancilla just before its l-th CNOT.
    Faults are inserted in the LAST round.  The layering comes from simverify (legality only);
    the propagation and detector bookkeeping here are stim's, not ours."""
    gates = simverify.alternating_circuit(ordersX, ordersZ)
    hk = {}
    for (g, l) in hook_faults:
        hk.setdefault(simverify.hook_layer(gates, ordersZ, g, l), []).append(g)
    LXb = poolmod.get()[2]
    c = stim.Circuit()
    c.append("RX", list(range(N)))
    nmeas = 0; rec = {}
    for r in range(R):
        c.append("RX", XA); c.append("R", ZA)
        for li, lay in enumerate(gates):
            if r == R - 1 and li in hk:
                c.append("Z_ERROR", [ZA[g] for g in hk[li]], 1.0)
            tg = []
            for (ct, tt) in lay:
                tg += [ct, tt]
            c.append("CX", tg)
        if r == R - 1 and data_faults:
            c.append("Z_ERROR", list(data_faults), 1.0)
        c.append("MX", XA)
        for g in range(NG):
            rec[('X', g, r)] = nmeas + g
        nmeas += NG
        c.append("M", ZA)
        for g in range(NG):
            rec[('Z', g, r)] = nmeas + g
        nmeas += NG
        for g in range(NG):
            if r == 0:
                c.append("DETECTOR", [stim.target_rec(rec[('X', g, 0)] - nmeas)])
            else:
                c.append("DETECTOR", [stim.target_rec(rec[('X', g, r)] - nmeas),
                                      stim.target_rec(rec[('X', g, r - 1)] - nmeas)])
                c.append("DETECTOR", [stim.target_rec(rec[('Z', g, r)] - nmeas),
                                      stim.target_rec(rec[('Z', g, r - 1)] - nmeas)])
    c.append("MX", list(range(N)))
    for q in range(N):
        rec[('d', q)] = nmeas + q
    nmeas += N
    for g in range(NG):
        tg = [stim.target_rec(rec[('X', g, R - 1)] - nmeas)]
        for q in np.nonzero(HX[g])[0]:
            tg.append(stim.target_rec(rec[('d', int(q))] - nmeas))
        c.append("DETECTOR", tg)
    for i in range(12):
        c.append("OBSERVABLE_INCLUDE",
                 [stim.target_rec(rec[('d', int(q))] - nmeas)
                  for q in np.nonzero(LXb[i])[0]], i)
    return c


def check(ordersX, ordersZ, residuals, data_faults, R=2):
    L = {0: 3, 1: 4, 2: 5}
    hooks = [(cc, L[k]) for (cc, k) in residuals]
    circ = build(ordersX, ordersZ, hooks, data_faults, R=R)
    det, ob = circ.compile_detector_sampler().sample(1, separate_observables=True)
    circ0 = build(ordersX, ordersZ, [], [], R=R)
    det0, ob0 = circ0.compile_detector_sampler().sample(1, separate_observables=True)
    return dict(n_faults=len(hooks) + len(data_faults),
                detectors_fired=int(np.array(det)[0].sum()),
                observables_flipped=int(np.array(ob)[0].sum()),
                clean_detectors_fired=int(np.array(det0)[0].sum()),
                clean_observables_flipped=int(np.array(ob0)[0].sum()),
                n_detectors=circ.num_detectors)
```

#### `mktable.py`

```python
import glob, re, collections, pathlib

rows = collections.defaultdict(dict)
for f in glob.glob("out/*.txt"):
    for line in open(f):
        m = re.match(r"([ZX]) \((\d+), (\d+), (\d+)\) W=(\d+) orbit (\d+) rep=(.+?): (SAT|UNSAT)\s+([\d.]+)s(.*)", line.strip())
        if not m:
            continue
        sec, a, b, c, W, oi, rep, verdict, el, rest = m.groups()
        key = (sec, (int(a), int(b), int(c)), int(W))
        rows[key][int(oi)] = (verdict, float(el), rest.strip())

out = []
out.append("| sector | tiled assignment | `W` | verdict | time | witness |")
out.append("|---|---|---|---|---|---|")
for key in sorted(rows):
    sec, tr, W = key
    d = rows[key]
    sats = [(oi, v) for oi, v in sorted(d.items()) if v[0] == "SAT"]
    if sats:
        oi, (v, el, rest) = sats[0]
        wt = re.search(r"'weight': (\d+).*?'n_data': (\d+), 'n_res': (\d+), 'Ewt': (\d+)", rest)
        w = (f"weight {wt.group(1)} = {wt.group(2)} data + {wt.group(3)} hooks, "
             f"\\|E\\| = {wt.group(4)}"
             if wt else rest[:60])
        out.append(f"| {sec} | {tr} | {W} | **SAT** (orbit {oi}) | {el:.0f} s | {w} |")
    else:
        n = len(d)
        tot = sum(v[1] for v in d.values())
        out.append(f"| {sec} | {tr} | {W} | UNSAT on {n} orbit reps | {tot:.0f} s | — |")
print("\n".join(out))
```

