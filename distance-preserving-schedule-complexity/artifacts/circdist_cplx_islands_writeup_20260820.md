# CIRCDIST.cplx — the five tractable islands, written up as mathematics

Session: Opus 5 executor / **proposer**, budget-boxed, 2026-08-20.
Target node: `CIRCDIST.cplx` (课题三 of `research/circdist/notes/CIRCDIST_PROBLEMS.md`).
Inputs: `research/circdist/notes/CIRCDIST_PROBLEMS.md`; `artifacts/circdist_cplx_recon_20260820.md`
(route recon, §7 islands); `artifacts/circdist_cplx_gadget_20260820.md` (the gadget gate, source of
the fifth island and the prefix-sum reformulation).

**No proof-DAG file, node file, route file or assessment was written or modified by this session.
No other artifact was modified.**

---

## 0. Labels, and how to read this file

Per `research/VALUATION_PROTOCOL.md` conventions used by the two predecessor sessions:

* **CONJECTURED** — a written-out mathematical argument by the proposer, complete to the best of
  the proposer's ability, **with no independent adversarial review**. Every theorem, lemma and
  proposition in this file carries this label. Nothing here is PROVED.
* **NUMERICAL** — a statement produced by exact `F_2` computation on a specific finite object; the
  enumeration is the certificate. All numerical statements quoted here are *imported* from
  `circdist_cplx_recon_20260820.md` §3 and `circdist_cplx_gadget_20260820.md` §§1,3,5,6; this
  session ran no new computation and re-verifies none of them.
* **ASSUMPTION** — an external result used as a premise, with source and verification status.

The file is meant to be reviewable in one pass: §1 fixes the model and the algebra once, and each
island (§§2–6) is then self-contained given §1. §7 collects the honest scope clauses, the one
**gap found** (Island V), and the repricing that follows from it.

**Executive line.** Islands I, II, III and IV came out with complete arguments. Island V did
**not**: the claim recorded in `circdist_cplx_gadget_20260820.md` §5.4 that the weight-4 / `d_X ≥ 4`
regime "is a bipartite matching problem, decided in polynomial time" is **over-stated**. The correct
reduction is to a *partial-section hitting* problem which, as an abstract CSP, is NP-complete
(§6.5). What survives rigorously is (a) the exact reduction, (b) a genuine bipartite-matching
theorem under one extra, polynomial-time-checkable hypothesis, and (c) the `k ≤ 1 ⇒` YES theorem,
whose linear-splitting parity argument is written out in full and does hold. See §6.5 and §7.2.

---

## 1. Common framework

### 1.1 Codes, sectors, logicals

Fix `H_X ∈ F_2^{m_X × n}` and `H_Z ∈ F_2^{m_Z × n}` with `H_X H_Z^T = 0`. Write

* `S_X := rowspace(H_X) ⊆ F_2^n`, `S_Z := rowspace(H_Z)`;
* `C_X := ker H_Z ⊇ S_X` ("X-patterns that trigger no Z-detector"), `C_Z := ker H_X ⊇ S_Z`;
* `L_X := C_X \ S_X` (nontrivial undetectable X-patterns), `L_Z := C_Z \ S_Z`;
* `d_X := min{ |v| : v ∈ L_X }` and `d_Z := min{ |v| : v ∈ L_Z }`, with `min ∅ = ∞`;
* `k := n − rank H_X − rank H_Z`, `d := d(Q) := min(d_X, d_Z)`.

Rows of `H_X` are **X-checks**; for an X-check `c` we write `supp(c) ⊆ [n]` and `w_c := |supp(c)|`,
and we identify `c` with the vector `χ_{supp(c)} ∈ S_X`. Mirror conventions for Z-checks. Every
statement below is written for the **X-sector**; the **Z-sector** statement is obtained by the
substitution `(H_X, H_Z, S_X, C_X, L_X, d_X) ↦ (H_Z, H_X, S_Z, C_Z, L_Z, d_Z)`, and we will say
"the mirror" for it. All of §1 is symmetric under that substitution, so this is legitimate.

Throughout, `Q := Q_X := F_2^n / S_X`, `λ := λ_X : F_2^n → Q` the quotient map, and

```
    Log := Log_X := C_X / S_X  ≅  F_2^{k}       (dim Log_X = k, likewise dim Log_Z = k)
    ν  := ν_X : Q → Q/Log  ≅  F_2^n / ker H_Z  ≅  im(v ↦ H_Z v)  ⊆ F_2^{m_Z}
```

so that `ν ∘ λ` is (up to the isomorphism) the **syndrome map** `v ↦ H_Z v`. The single fact that
organises everything:

> `v` is an **undetectable nontrivial X-pattern** ⟺ `λ(v) ∈ Log \ {0}`.

`dim Log_X = k` because `dim C_X = n − rank H_Z` and `dim S_X = rank H_X`.

### 1.2 The circuit model and the column set

**Model (M).** One round of single-ancilla, CNOT-based syndrome extraction, prepare-once /
measure-once, ideal terminal data readout, as fixed in 公共定义 of `CIRCDIST_PROBLEMS.md`:

* **M1.** One ancilla `a_c` per check `c`. For an X-check: `a_c` is prepared in `|+⟩`, acts as the
  **control** of one CNOT onto each `q ∈ supp(c)`, and is measured in the `X` basis. For a Z-check:
  `a_c` is prepared in `|0⟩`, is the **target** of one CNOT from each `q ∈ supp(c)`, and is measured
  in the `Z` basis.
* **M2.** A **schedule** `M` assigns to each check `c` a linear order `π_c = (q_1,…,q_{w_c})` of
  `supp(c)` (the order in which its CNOTs are executed), plus a global timing. We work in **variant
  V1** of `circdist_cplx_recon_20260820.md` §1: no depth bound, the only physical constraint is that
  a qubit does at most one two-qubit gate per time step. Consequently every tuple `(π_c)_c` is
  realisable (execute the checks one after another), and by Lemma 1.2 below `d_eff` depends on `M`
  only through `(π_c)_c`; we therefore *identify* `M` with the tuple `(π_c)_c`.
* **M3.** Elementary faults: an arbitrary Pauli after any state preparation, an arbitrary two-qubit
  Pauli after any CNOT, an arbitrary single-qubit Pauli on an idling data qubit, and a classical
  flip of any measurement outcome. `|F|` counts fault *locations*.
* **M4.** `d_eff(M) := d_ext(E(M))`, the distance of the extended code built from the **terminal
  residual data errors** of `M`; intermediate-time detector information is discarded by definition.

For a check `c` and order `π_c = (q_1,…,q_w)` put

```
    P_i(π_c) := {q_1,…,q_i}          (i-th proper prefix,  1 ≤ i ≤ w−1)
    S_i(π_c) := {q_{i+1},…,q_w}      (i-th proper suffix / "hook",  1 ≤ i ≤ w−1)
```

so `P_i ⊔ S_i = supp(c)`.

**Lemma 1.1 (column set) — CONJECTURED.** Under (M), the set of terminal residual X-type data
errors produced by *one* elementary fault is exactly

```
    Cols_X(M) = { e_q : q ∈ [n] }  ∪  { χ_{S_i(π_c)} : c an X-check, 1 ≤ i ≤ w_c − 1 } ,
```

together with `χ_{supp(c)} ∈ S_X`, which is a stabiliser and hence contributes nothing. The mirror
holds in the Z-sector with Z-checks.

*Argument.* Take an X-check `c` with order `π_c`. The ancilla is the control of every CNOT.
(i) An `X` fault on `a_c` occurring after CNOT `i` and before CNOT `i+1` propagates along every
later CNOT (control→target for `X`) and lands on `q_{i+1},…,q_w`: residual `χ_{S_i}`. A `Z` fault on
`a_c` commutes with the control side of every CNOT and is detected only by the terminal `X`
measurement of `a_c`: it perturbs the syndrome bit and leaves no data residual, which (M4) discards.
(ii) A two-qubit fault after CNOT `i` is `P_{a_c} ⊗ P_{q_i}`. Its `P_{a_c}` part contributes
`χ_{S_i}` if it has an `X` component and nothing otherwise; its `P_{q_i}` part contributes `e_{q_i}`
if it has an `X` component. The four combinations give `χ_{S_i}`, `χ_{S_i} + e_{q_i} = χ_{S_{i−1}}`
(using `S_{i−1} = {q_i} ⊔ S_i`), `e_{q_i}`, and `0`; all lie in the displayed set, and the `Z`
component of `P_{q_i}` is a Z-sector data column, also in the displayed set (mirror).
(iii) A preparation fault on `a_c` is (up to the stabiliser of `|+⟩`) an `X` fault before CNOT 1,
giving `χ_{S_0} = χ_{supp(c)} ∈ S_X`. (iv) A measurement flip perturbs the syndrome only.
(v) An idling data fault gives `e_q`. Nothing else occurs, and each displayed element is realised by
some single fault (for `χ_{S_i}`, an `X` fault on `a_c` after CNOT `i`). For a Z-check the ancilla is
the *target*, `Z` propagates target→control, and the same computation gives the mirror. ∎

*Remark.* This is the mathematical content of ASSUMPTION A13 (Dennis–Kitaev–Landahl–Preskill 2002;
Tomita–Svore 2014). Lemma 1.1 is argued here rather than assumed.

**Lemma 1.2 (order-determinacy) — CONJECTURED.** In V1, `Cols_X(M)` and `Cols_Z(M)`, and hence
`d_eff(M)`, depend only on the tuple `(π_c)_c`; global timing and X/Z interleaving are irrelevant.
*Immediate from Lemma 1.1: no displayed column mentions a time step.* ∎

(This is exactly the property that fails for `d_circ`; cf. node `CIRCDIST.lift`. It is what makes
the whole CSP picture available, and it is why every result in this file is a result about
`d_eff`, not about `d_circ`.)

### 1.3 Mechanisms; multiset and sector reductions

**Definition 1.3.** Fix a schedule `M`. An **X-mechanism** is a finite multiset `F` of elements of
`Cols_X(M)` — formally, of *fault locations*, so the same vector may occur through different
locations — with `Σ F ∈ L_X`, i.e. `λ(Σ F) ∈ Log \ {0}`. Its size is `|F|` (number of locations).
`d_eff^X(M) := min{ |F| : F an X-mechanism }`, and mirror for `d_eff^Z`.

**Lemma 1.4 (sector splitting) — CONJECTURED.** `d_eff(M) = min( d_eff^X(M), d_eff^Z(M) )`.

*Argument.* A fault set `F` of size `t` produces a terminal residual Pauli `P = X(v_X) Z(v_Z)`,
where `v_X` is a sum of at most `t` elements of `Cols_X(M)` and `v_Z` of at most `t` elements of
`Cols_Z(M)` (one elementary fault may contribute to both, e.g. a `Y ⊗ Y` CNOT fault). `P` is
undetectable iff `H_Z v_X = 0` and `H_X v_Z = 0`; `P` is a nontrivial logical iff additionally
**not** both `v_X ∈ S_X` and `v_Z ∈ S_Z`. Hence for a minimal such `F`, at least one of
`v_X ∈ L_X`, `v_Z ∈ L_Z` holds; that sector alone already supplies a mechanism of size `≤ t`.
Conversely a single-sector mechanism is a fault set. ∎

**Lemma 1.5 (sets suffice) — CONJECTURED.** In Definition 1.3 the minimum is attained on a multiset
in which no *vector* occurs twice. *If `u` occurs twice, deleting both occurrences leaves `Σ F`
unchanged and decreases `|F|` by 2.* ∎

We therefore treat mechanisms as **sets of columns with pairwise distinct vectors**, and we may
record a mechanism as a triple `(D, (I_c)_c)`: a set `D ⊆ [n]` of data columns, and for each X-check
`c` a set `I_c ⊆ {1,…,w_c−1}` of hook indices, with
`|F| = |D| + Σ_c |I_c|` and `Σ F = χ_D + Σ_c Σ_{i∈I_c} χ_{S_i(π_c)}`.

**Definition 1.6 (scope).** `scope(F) := { c : I_c ≠ ∅ }`. A mechanism is **unary** if
`|scope(F)| ≤ 1` and **coupling** if `|scope(F)| ≥ 2`.

### 1.4 The problem

**Definition 1.7 (Eff-Preserve, V1).** *Input:* `H_X, H_Z` with `H_X H_Z^T = 0`, and an integer
`d ≥ 1`. *Promise:* `d(Q) = d` exactly and `k ≥ 1`. *Question:* is there a schedule `M` with
`d_eff(M) = d`?

**Lemma 1.8 (`d_eff ≤ d`) — CONJECTURED.** For every `M`, `d_eff(M) ≤ d(Q)`.
*Argument.* Let `v` realise `d(Q)`; say `v ∈ L_X` with `|v| = d_X = d` (else use the mirror). Then
`F = { e_q : q ∈ supp(v) }` is an X-mechanism of size `d`, because `Cols_X(M) ⊇ {e_q}` for every `M`
and `Σ F = v ∈ L_X`. Enlarging the generator set of the extended code cannot change `S_X`, `C_X`,
hence cannot change the nontriviality of `v`. ∎

**Definition 1.9 (total surrogate).** `Eff-Preserve≥ := { (H_X,H_Z,d) : ∃M, d_eff(M) ≥ d }`. By
Lemma 1.8 it agrees with Eff-Preserve on every promise-satisfying input, and it is a *total*
language. **All algorithms in this file decide `Eff-Preserve≥`**, hence decide Eff-Preserve on the
promise. (This matters: verifying the promise is itself NP-hard — ASSUMPTION A5.)

**Lemma 1.10 (no scope-0 mechanism) — CONJECTURED.** Under the promise, no mechanism `F` with
`|F| ≤ d−1` has `scope(F) = ∅`. *A scope-0 mechanism has `Σ F = χ_D` with `|D| ≤ d−1`, so
`χ_D ∈ L_X` would be a nontrivial undetectable pattern of weight `< d ≤ d_X` — contradiction.* ∎

So every low-weight mechanism uses at least one hook, and the whole question is which orders are
chosen. This is the CSP of the recon's Lemma 3, restated here for the record:

**Proposition 1.11 (CSP form) — CONJECTURED.** Under the promise, `∃M : d_eff(M) ≥ d` is the
satisfiability of the constraint-satisfaction problem
*variables* `x_c` (one per check, both sectors, on disjoint variable sets by Lemma 1.4);
*domain of `x_c`* the `w_c!` linear orders of `supp(c)`;
*constraints* one for each mechanism `F` with `|F| ≤ d−1`, forbidding the tuple of orders that
realises it — of arity `|scope(F)| ≤ d−1`.
*Immediate from Definition 1.3, Lemma 1.4, Lemma 1.5, Lemma 1.10 and the V1 fact that every order
tuple is realisable.* ∎

### 1.5 Prefix–suffix duality and the master equation

**Lemma 1.12 (prefix–suffix duality) — CONJECTURED.** For every X-check `c`, every order `π_c` and
every `1 ≤ i ≤ w_c − 1`,

```
    λ( χ_{S_i(π_c)} ) = λ( χ_{P_i(π_c)} )   in  Q = F_2^n / S_X .
```

*`χ_{S_i} + χ_{P_i} = χ_{supp(c)} ∈ S_X`.* ∎

This is strictly stronger than the syndrome identity `H_Z χ_{S_i} = H_Z χ_{P_i}` of
`circdist_cplx_gadget_20260820.md` Lemma A: it says the hook and the prefix are equal *in `Q`*, not
merely equal modulo `Log`. Writing `a_q := λ(e_q) ∈ Q`, and noting `Σ_{q ∈ supp(c)} a_q = 0` (as
`χ_{supp(c)} ∈ S_X`), we get the object that replaces "search over `w!` orders":

**Definition 1.13 (value of an order).** `V(π_c) := { λ(χ_{P_i(π_c)}) : 1 ≤ i ≤ w_c − 1 }
= { a_{q_1}, a_{q_1}+a_{q_2}, …, a_{q_1}+⋯+a_{q_{w−1}} } ⊆ Q`, the set of **proper prefix sums** of
the sequence `(a_{q_1},…,a_{q_w})`, a sequence which sums to `0`.

**Proposition 1.14 (master equation) — CONJECTURED.** Let `M = (π_c)_c` and let
`F = (D, (I_c)_c)`. Then `F` is an X-mechanism iff

```
    Σ_{q ∈ D} a_q  +  Σ_c Σ_{i ∈ I_c} v_{c,i}   ∈   Log \ {0} ,
    where  v_{c,i} = λ(χ_{P_i(π_c)}) ∈ V(π_c)  is the i-th prefix sum of π_c.
```

*Immediate from Lemma 1.12, Definition 1.3 and `λ(v) ∈ Log \ {0} ⟺ v ∈ L_X`.* ∎

**The stabiliser-coincidence proviso, stated honestly.** In the special case `d = 3` (budget 2)
with a coupling mechanism `F = {S_i(π_c), S_j(π_{c'})}`, `c ≠ c'`, Proposition 1.14 reads

```
    forbidden(π_c, π_{c'})  ⟺  ∃ v ∈ V(π_c), v' ∈ V(π_{c'}) :  v + v' ∈ Log \ {0}
                            ⟺  ∃ v, v' :  ν(v) = ν(v')   AND   v ≠ v' .
```

The first clause `ν(v) = ν(v')` is "the two prefix-sum sets meet **in syndrome space**"; that is the
naive "prefix-sum disjointness" reading. It is **not** the criterion. The second clause is the
proviso: two hooks whose syndromes coincide are *harmless* when they differ by a stabiliser, i.e.
when they are equal in `Q`, not merely in `Q/Log`. Dropping the proviso gives a strictly wrong
relation — measured, `circdist_cplx_gadget_20260820.md` §2: on the gadget `G_{≠3}`, 1 152 X-sector
and 8 513 Z-sector order pairs have colliding syndromes but a stabiliser difference (NUMERICAL,
imported). The clean way to say it is: **work in `Q`, not in syndrome space; "meets" means meets in
`Q/Log` at a point where the `Q`-preimages differ.** When `k = 0` (`Log = 0`) the proviso is vacuous
and the criterion is literally `V(π_c) ∩ V(π_{c'}) = ∅` — but then `L_X = ∅` and the sector is
trivial anyway.

**Lemma 1.15 (chain realisability) — CONJECTURED.** Let `A_1 ⊋ A_2 ⊋ ⋯ ⊋ A_r` be a chain of
nonempty proper subsets of `supp(c)`. Then some order `π_c` has `{A_1,…,A_r} ⊆ Hooks(π_c) :=
{S_i(π_c)}_i`. *List `supp(c)` as the concatenation `(supp(c)\A_1), (A_1\A_2), …, (A_{r−1}\A_r),
A_r`, each block in arbitrary internal order; then each `A_j` is a suffix.* ∎

Conversely `Hooks(π_c)` is always a chain. So *the realisable families of hooks of one check are
exactly the chains of nonempty proper subsets of `supp(c)`.* This is the combinatorial content of
the domain, and it is what makes "does this instance couple?" a finite, enumerable question (§2.3).

---

## 2. Island I — factorising instances: no inter-check coupling ⇒ polynomial

### 2.1 Exact problem statement

**Problem `Eff-Preserve≥[decoupled]`.**
*Input:* `H_X ∈ F_2^{m_X×n}`, `H_Z ∈ F_2^{m_Z×n}` with `H_X H_Z^T = 0`; an integer `d`.
*Parameters held fixed:* `d` (a constant), `w := max_c w_c` (a constant, or a parameter).
*Promise:* `d(Q) = d`, `k ≥ 1`, and the instance is **safely decoupled** in the sense of
Definition 2.3 below (in both sectors).
*Question:* is there a schedule `M` with `d_eff(M) ≥ d` (equivalently, by Lemma 1.8 and the
promise, `= d`)?

**Proposition 2.1 (sector factorisation) — CONJECTURED.** `∃M : d_eff(M) ≥ d` holds iff
`∃M : d_eff^X(M) ≥ d` and `∃M : d_eff^Z(M) ≥ d`. *By Lemma 1.4 and Proposition 1.11 the two sector
CSPs have disjoint variable sets (X-checks resp. Z-checks), and by V1 every combination of the two
tuples is realisable.* ∎

Proposition 2.1 licenses **modular island composition**: one may certify the X-sector by one island
and the Z-sector by a different one. Island V (§6) needs this, because it settles one sector only.

### 2.2 Defining "coupling" precisely

Everything is stated for the X-sector; mirror for Z.

**Definition 2.2 (local safety, domain).** An order `π_c` of an X-check `c` is **locally safe** if
there is **no** mechanism `F = (D, (I_{c'})_{c'})` with `|F| ≤ d − 1`, `I_{c'} = ∅` for all
`c' ≠ c`, `I_c ≠ ∅`, and `I_c` indexing hooks of `π_c`. Write `D_c` for the set of locally safe
orders of `c` ("the domain of variable `x_c`"). By Proposition 1.14, `π_c ∈ D_c` iff for every
`D ⊆ [n]` and every `∅ ≠ J ⊆ V(π_c)` with `|D| + |J| ≤ d − 1`,

```
        Σ_{q∈D} a_q + Σ_{v ∈ J} v  ∉  Log \ {0} .
```

(Here `J` ranges over subsets of the prefix-sum set `V(π_c)`; multiplicities are irrelevant by
Lemma 1.5.)

**Definition 2.3 (coupling; safely decoupled).** For an X-check `c` let

```
    𝒞_c := { J : J ⊆ Hooks(π) for some π ∈ D_c }
```

be the families of hooks of `c` that are *simultaneously realisable by one locally safe order* — by
Lemma 1.15 these are exactly the chains contained in `Hooks(π)` for some `π ∈ D_c`. A **coupling
witness** is a tuple `(D, (J_c)_c)` with `J_c ∈ 𝒞_c` for every `c`, total size
`|D| + Σ_c |J_c| ≤ d − 1`, `|{c : J_c ≠ ∅}| ≥ 2`, and

```
        χ_D + Σ_c Σ_{A ∈ J_c} χ_A  ∈  L_X .
```

The instance is **safely decoupled** (in the X-sector) if no coupling witness exists. It is
**decoupled** if, more strongly, no such tuple exists even when `𝒞_c` is replaced by *all* chains of
nonempty proper subsets of `supp(c)` (i.e. dropping local safety). Decoupled ⇒ safely decoupled.

*Why this is the right definition.* By Lemma 1.15 a family of hooks of one check is realisable by a
single order iff it is a chain, and by Lemma 1.2 nothing else about the schedule matters. So
"coupling witness" is precisely "a mechanism of arity ≥ 2 that some *locally safe* schedule would
actually realise", quantified without a quantifier over the `∏_c w_c!` schedules.

*Prefix-sum reading.* By Proposition 1.14 a coupling witness is a choice of a *prefix sum* `v_{c,i}`
from each of at least two checks, plus at most `d − 1 − (#chosen)` data qubits, summing into
`Log \ {0}`. At `d = 3` this collapses to the statement in §1.5: the instance is safely decoupled iff
for all `c ≠ c'` and all locally safe `π_c, π_{c'}`, the sets `V(π_c)` and `V(π_{c'})` do not meet
*modulo `Log`* except at points where they are equal *in `Q`*. That is the honest
"prefix-sum-disjointness" formulation; the italicised clause is the stabiliser-coincidence proviso
and cannot be dropped (§1.5).

### 2.3 The theorem

**Theorem I — CONJECTURED.** Assume the promise of §2.1 (in particular `d(Q) = d`). Then:

1. If **some** check `c` has `D_c = ∅`, then `∀M : d_eff(M) ≤ d − 1`, i.e. the instance is a NO.
   (No decoupling hypothesis needed.)
2. If the instance is **safely decoupled** and `D_c ≠ ∅` for every check `c`, then any schedule `M`
   with `π_c ∈ D_c` for all `c` satisfies `d_eff(M) ≥ d`, i.e. the instance is a YES.
3. Hence on safely decoupled instances,
   `∃M : d_eff(M) ≥ d  ⟺  ∀c : D_c ≠ ∅`,
   and this is decided in time

```
        O( Σ_c w_c! · (w_c + n)^{d−1} · n^2 )   +   O(n^3)  ,
```

   which is polynomial in `n` for fixed `d` and bounded check weight, and is FPT in
   `w = max_c w_c` for fixed `d`.

*Proof.*

**(1)** Local safety of `π_c` is a property of `π_c` alone (Definition 2.2), so if `D_c = ∅` then for
*every* schedule `M` the order `π_c` chosen by `M` is not locally safe, which by definition exhibits
a mechanism `F` with `|F| ≤ d − 1`. Hence `d_eff(M) ≤ d − 1` for every `M`. (Note this uses only
Lemma 1.1 and Definition 1.3, not the promise.)

**(2)** Let `M` have `π_c ∈ D_c` for all `c`, and suppose towards a contradiction that `F` is a
mechanism for `M` with `|F| ≤ d − 1`. Write `F = (D, (I_c)_c)` as in Lemma 1.5 and put
`J_c := { S_i(π_c) : i ∈ I_c }`. Three cases.
*Case `scope(F) = ∅`.* Excluded by Lemma 1.10 (this is where the promise `d(Q) = d` is used).
*Case `scope(F) = {c}`.* Then `F` is exactly a witness that `π_c ∉ D_c` (Definition 2.2),
contradicting the choice of `M`.
*Case `|scope(F)| ≥ 2`.* Each `J_c` is a subset of `Hooks(π_c)` with `π_c ∈ D_c`, hence
`J_c ∈ 𝒞_c`; so `(D, (J_c)_c)` is a coupling witness, contradicting safe decoupling.
All cases are impossible, so `d_eff(M) ≥ d`.

**(3)** The equivalence is (1) + (2) (using Lemma 1.8 for `≥ d ⟹ = d` under the promise). For the
running time: compute once a reduced row-echelon form of `H_Z` and of `H_X` in `O(n^3)`; then the
predicate "`v ∈ L_X`" is `O(n^2)` per query (reduce `v` against `H_Z`'s RREF to test `H_Z v = 0`, and
against `H_X`'s RREF to test `v ∉ S_X`). Testing whether a given `π_c` is locally safe requires
scanning all `(D, J)` with `|D| + |J| ≤ d − 1`, `J ⊆ Hooks(π_c)` (at most `w_c − 1` hooks), i.e.
`Σ_{j≥1} C(w_c−1, j) C(n, d−1−j) ≤ (w_c + n)^{d−1}` queries. Doing this for all `w_c!` orders and
all checks gives the stated bound. ∎

**Corollary I.1 (the class is self-certifying) — CONJECTURED.** For fixed `d` and bounded check
weight `w`, whether an instance is *decoupled* (Definition 2.3, strong form) is itself decidable in
time `O( (n + Σ_c 2^{w_c})^{d−1} · n^2 )`, hence polynomial: enumerate all tuples of at most `d − 1`
elements of the ground set `{e_q}_{q} ∪ ⋃_c { χ_A : ∅ ≠ A ⊊ supp(c) }`, discard those whose
per-check parts are not chains (Lemma 1.15), and test `Σ ∈ L_X` on those with scope `≥ 2`. Safe
decoupling is decided by the same enumeration after computing the `D_c`. *Consequently the
algorithm of Theorem I can first verify its own hypothesis and only then answer* — the island is a
promise-free polynomial-time class, not merely a conditional one. ∎

**Corollary I.2 (unbounded weight) — CONJECTURED.** For fixed `d`, safely decoupled instances of
unbounded check weight are decided in `NP ∩ coNP`-style form: `∀c : D_c ≠ ∅` is a conjunction of `m`
independent `Σ_1`-statements `∃π_c ∀ (D,J) …`, each with a polynomial-time inner predicate for fixed
`d`. In particular a YES certificate is a single schedule, verifiable in polynomial time (this is
Corollary 2 of `circdist_cplx_recon_20260820.md` §5.2). We do **not** claim a polynomial algorithm
in this regime; see the scope clause. ∎

### 2.4 Scope clause — what Island I does not cover

* **It is a hypothesis, not a theorem about codes.** Island I says nothing about *which* codes are
  (safely) decoupled. Imported NUMERICAL evidence (`circdist_cplx_recon_20260820.md` §3): all five
  structured `d = 3` families probed (rotated `[[9,1,3]]`, `3×3` toric, unrotated `[[13,1,3]]`,
  Steane, quantum Hamming `[[15,7,3]]`) are decoupled, while **56 of 71** random self-orthogonal
  weight-6 CSS codes with `d_X = 3` are **not**. Decoupling is therefore a property of structure,
  and generic instances fall outside the island.
* **Fixed `d` and bounded `w` are both load-bearing** for the polynomial claim. With `d` part of the
  input the enumeration of `(D, J)` is exponential; with `w` unbounded the `w_c!` scan is
  exponential. We have no polynomial algorithm for "does check `c` admit a locally safe order?" at
  unbounded `w`, and we do not claim one. (For fixed `d` it is in NP; whether it is in P is open and
  is a clean, small, self-contained subquestion worth registering.)
* **V1 only.** Step (2) of the proof chooses `π_c ∈ D_c` *independently for each check*. Under a
  depth bound (variant V2) the chosen tuple need not be realisable as a depth-`T` schedule, and the
  argument collapses; under an arbitrary CNOT conflict graph (V3) even schedule *existence* is
  NP-complete (ASSUMPTION A8). Island I is a V1 statement.
* **`d_eff`, not `d_circ`.** Everything rests on Lemma 1.2, which fails for `d_circ`. Island I says
  nothing about Circ-Preserve.
* **It does not by itself refute hardness.** Decoupling is exactly the negation of the raw material
  a hardness reduction needs (`circdist_cplx_recon_20260820.md` §6); Island I is the reason a
  reduction *must* build coupling, not a reason none exists.

---

## 3. Island II — hypergraph product codes: constant YES, argued structurally
<!-- deliberately not "proved": like everything here, CONJECTURED pending independent review -->

The recon registered this island (premise P6.2) as *"cite Manes–Claes (ASSUMPTION A1) plus a scope
check"*, with the explicit caveat that nobody had checked the hypotheses of the cited theorem. This
section replaces the citation by an argument. What follows is a self-contained proof that the
coupling constraints of an HGP code vanish **structurally**, i.e. for a reason visible in the
product algebra and independent of the local orders.

### 3.1 Exact problem statement

**Problem `Eff-Preserve≥[HGP]`.**
*Input:* classical parity-check matrices `H_1 ∈ F_2^{m_1×n_1}`, `H_2 ∈ F_2^{m_2×n_2}` (the input is
the seed pair; `H_X, H_Z` are the derived matrices of §3.2), and an integer `d`.
*Promise:* the CSS code `Q = HGP(H_1,H_2)` has `d(Q) = d` and `k ≥ 1`.
*Question:* is there a schedule `M` with `d_eff(M) = d`?

### 3.2 The product, in matrix coordinates

Data qubits are `V_A ⊔ V_B` with `V_A = [n_1] × [n_2]`, `V_B = [m_1] × [m_2]`; so
`n = n_1 n_2 + m_1 m_2`. Identify an `X`-pattern with a pair of matrices
`(V, W) ∈ F_2^{n_1×n_2} × F_2^{m_1×m_2}` (`V[j,b]` is the `A`-block qubit `(j,b)`, `W[i,a]` the
`B`-block qubit `(i,a)`), and likewise for `Z`-patterns. The check matrices are

```
    H_X = [ H_1 ⊗ I_{n_2}  |  I_{m_1} ⊗ H_2^T ]      rows indexed by [m_1] × [n_2]
    H_Z = [ I_{n_1} ⊗ H_2  |  H_1^T ⊗ I_{m_2} ]      rows indexed by [n_1] × [m_2]
```

**Lemma 3.1 (coordinates) — CONJECTURED.** With the identification above:

1. `X`-check `(i,b)` has support `( R_i × {b} ) ⊔ ( {i} × C_b )`, where `R_i := supp(row i of H_1)
   ⊆ [n_1]` and `C_b := supp(column b of H_2) ⊆ [m_2]`. Its weight is `|R_i| + |C_b|`.
2. `ker H_Z = { (V,W) : V H_2^T = H_1^T W }`.
3. `S_X = { (H_1^T U, U H_2^T) : U ∈ F_2^{m_1 × n_2} }`.

*Argument.* (1) `(H_1 ⊗ I_{n_2})[(i,b),(j,b')] = H_1[i,j] δ_{bb'}`, giving the `A`-part
`{(j,b) : H_1[i,j]=1} = R_i × {b}`; `(I_{m_1} ⊗ H_2^T)[(i,b),(i',a)] = δ_{ii'} H_2^T[b,a] =
δ_{ii'} H_2[a,b]`, giving the `B`-part `{(i,a) : H_2[a,b]=1} = {i} × C_b`.
(2) The `(j,a)` component of `H_Z (V,W)` is `Σ_b δ_{jj'}…` — explicitly
`Σ_b H_2[a,b] V[j,b] + Σ_i H_1[i,j] W[i,a] = (V H_2^T)[j,a] + (H_1^T W)[j,a]`.
(3) `S_X` is spanned by the `X`-checks; taking `U = e_i e_b^T` in (1) gives `V = H_1^T e_i e_b^T
= H_1^T U` (whose column `b` is the `i`-th column of `H_1^T`, i.e. `χ_{R_i}`) and
`W = e_i e_b^T H_2^T = U H_2^T` (whose row `i` is `(H_2 e_b)^T = χ_{C_b}^T`); linearity in `U` gives
the whole span. ∎

Write `d(·)` for the minimum weight of a nonzero vector of a subspace, with `d(0) := ∞`, and put

```
    μ_X := min( d(ker H_2), d(ker H_1^T) ) ,      μ_Z := min( d(ker H_1), d(ker H_2^T) ) .
```

### 3.3 The structural theorem

**Lemma 3.2 (tensor intersection) — CONJECTURED.** Let `A ⊆ X` and `B ⊆ Y` be subspaces of finite
dimensional `F_2`-spaces. Then `(A ⊗ Y) ∩ (X ⊗ B) = A ⊗ B`.
*Argument.* `⊇` is clear. Extend a basis `(a_1,…,a_p)` of `A` to a basis `(a_1,…,a_p,a'_1,…)` of `X`,
and a basis `(b_1,…,b_q)` of `B` to a basis of `Y`. The products of basis vectors form a basis of
`X ⊗ Y`. Membership in `A ⊗ Y` forces all coefficients on `a'_• ⊗ (·)` to vanish; membership in
`X ⊗ B` forces all coefficients on `(·) ⊗ b'_•` to vanish. What remains is spanned by
`a_• ⊗ b_•`. ∎

(Concretely: a matrix all of whose *columns* lie in `A` and all of whose *rows* lie in `B` can be
written `Σ_r x_r y_r^T` with `x_r ∈ A`, `y_r ∈ B`.)

**Theorem II.1 (line-support cleaning) — CONJECTURED.** Let `(V,W) ∈ ker H_Z`. If

```
        #{ b : column b of V is nonzero }  <  d(ker H_2)      and
        #{ i : row i of W is nonzero }     <  d(ker H_1^T) ,
```

then `(V,W) ∈ S_X`.

*Proof.* Write `V_b ∈ F_2^{n_1}` for column `b` of `V`, `W_a ∈ F_2^{m_1}` for column `a` of `W`,
`V^j ∈ F_2^{n_2}` for row `j` of `V`, `W^i ∈ F_2^{m_2}` for row `i` of `W` (all as column vectors).
By Lemma 3.1(2) the constraint `V H_2^T = H_1^T W` has two readings:

```
    (col)   for every a ∈ [m_2]:   Σ_{b} H_2[a,b] · V_b  =  H_1^T W_a   ∈ Im(H_1^T)
    (row)   for every j ∈ [n_1]:   Σ_{i} H_1[i,j] · W^i  =  H_2 V^j     ∈ Im(H_2)
```

*Step 1 — every column of `V` lies in `Γ := Im(H_1^T)`.* Let `φ : F_2^{n_1} → F_2^{n_1}/Γ` be the
quotient map and suppose `φ(V_{b_0}) ≠ 0` for some `b_0`. Choose an `F_2`-linear functional
`ψ` on `F_2^{n_1}/Γ` with `ψ(φ(V_{b_0})) = 1` (possible as `φ(V_{b_0}) ≠ 0`), and set
`z ∈ F_2^{n_2}`, `z_b := ψ(φ(V_b))`. Applying `ψ ∘ φ` to (col) gives `Σ_b H_2[a,b] z_b = 0` for every
`a`, i.e. `z ∈ ker H_2`; and `z ≠ 0` since `z_{b_0} = 1`. Moreover `z_b = 1` forces `V_b ≠ 0`, so
`supp(z)` is contained in the set of nonzero columns of `V`, whence
`#{b : V_b ≠ 0} ≥ |z| ≥ d(ker H_2)` — contradicting the first hypothesis. So `V_b ∈ Γ` for all `b`,
and choosing preimages column by column we obtain `U ∈ F_2^{m_1×n_2}` with `V = H_1^T U`.

*Step 2 — every row of `W` lies in `Δ := Im(H_2)`.* Symmetrically, let `φ'` be the quotient map
`F_2^{m_2} → F_2^{m_2}/Δ`, suppose `φ'(W^{i_0}) ≠ 0`, pick `ψ'` with `ψ'(φ'(W^{i_0})) = 1`, and set
`y ∈ F_2^{m_1}`, `y_i := ψ'(φ'(W^i))`. Applying `ψ' ∘ φ'` to (row) gives `Σ_i H_1[i,j] y_i = 0` for
every `j`, i.e. `H_1^T y = 0`, `y ≠ 0`, and `supp(y) ⊆ {i : W^i ≠ 0}`; so
`#{i : W^i ≠ 0} ≥ d(ker H_1^T)`, contradicting the second hypothesis.

*Step 3 — assembly.* Put `W'' := W + U H_2^T` with `U` from Step 1. Then

* `H_1^T W'' = H_1^T W + H_1^T U H_2^T = V H_2^T + V H_2^T = 0`, so every **column** of `W''` lies in
  `ker H_1^T`;
* every **row** of `U H_2^T` lies in `Im(H_2)` (row `i` is `(H_2 (U^i))^T` for `U^i` the `i`-th row
  of `U`), and by Step 2 every row of `W` does too; hence every row of `W''` lies in `Δ = Im(H_2)`.

By Lemma 3.2, `W'' = Σ_r x_r y_r^T` with `x_r ∈ ker H_1^T` and `y_r = H_2 z_r ∈ Im(H_2)`. Setting
`U_0 := Σ_r x_r z_r^T ∈ F_2^{m_1×n_2}` we get `U_0 H_2^T = Σ_r x_r z_r^T H_2^T = Σ_r x_r y_r^T = W''`
and `H_1^T U_0 = Σ_r (H_1^T x_r) z_r^T = 0`. Therefore

```
    (V, W) = (H_1^T U, U H_2^T) + (0, W'') = (H_1^T (U + U_0), (U + U_0) H_2^T)  ∈  S_X .   ∎
```

**Corollary II.2 — CONJECTURED.** `d_X ≥ μ_X` and (by the duality of §3.5) `d_Z ≥ μ_Z`; hence
`d(Q) ≥ min(μ_X, μ_Z)`. *A nonzero `(V,W) ∈ ker H_Z` with `|(V,W)| < μ_X` has fewer than
`d(ker H_2)` nonzero columns in `V` and fewer than `d(ker H_1^T)` nonzero rows in `W`, since weight
bounds both counts; Theorem II.1 puts it in `S_X`.* ∎

**Theorem II.3 (structural absence of coupling) — CONJECTURED.** Let `Q = HGP(H_1,H_2)` and let `M`
be **any** schedule. Then every X-mechanism `F` (Definition 1.3) has `|F| ≥ μ_X`; that is,
`d_eff^X(M) ≥ μ_X`. Mirror: `d_eff^Z(M) ≥ μ_Z`. Consequently `d_eff(M) ≥ min(μ_X, μ_Z)` for every
`M`.

*Proof.* Let `F` be a set of `t` columns of `Cols_X(M)` (Lemma 1.5) and write its sum as `(V,W)`.
By Lemma 1.1 each element of `F` is one of:

| column | as `(V,W)` | columns of `V` touched | rows of `W` touched |
|---|---|---|---|
| data qubit `(j,b) ∈ V_A` | `(E_{jb}, 0)` | `{b}` | `∅` |
| data qubit `(i,a) ∈ V_B` | `(0, E_{ia})` | `∅` | `{i}` |
| hook `S ⊆ supp(X`-check `(i,b))` | `(χ_α e_b^{T},\; e_i χ_β^{T})` | `⊆ {b}` | `⊆ {i}` |

where, by Lemma 3.1(1), a subset `S` of the support of `X`-check `(i,b)` is uniquely
`S = (α × {b}) ⊔ ({i} × β)` with `α ⊆ R_i`, `β ⊆ C_b`. So **each single column touches at most one
column of `V` and at most one row of `W`**. Summing `t` of them, `V` has at most `t` nonzero columns
and `W` at most `t` nonzero rows. If `t ≤ μ_X − 1`, both hypotheses of Theorem II.1 hold, so
`(V,W) ∈ S_X` and `F` is not a mechanism. ∎

**Theorem II.4 (constant YES) — CONJECTURED.** Suppose `d(Q) = min(μ_X, μ_Z)` (by Corollary II.2
this is the same as `d(Q) ≤ min(μ_X,μ_Z)`). Then **every** schedule satisfies `d_eff(M) = d(Q)`. In
particular, on the class of HGP instances satisfying this condition, `Eff-Preserve` is the constant
function **YES**, and is decided in constant time (output "yes") — after the promise is granted.

*Proof.* Theorem II.3 gives `d_eff(M) ≥ min(μ_X,μ_Z) = d(Q)`; Lemma 1.8 gives `d_eff(M) ≤ d(Q)`. ∎

### 3.4 When the hypothesis of Theorem II.4 holds

**Lemma II.5 — CONJECTURED.** Write `k_1 = dim ker H_1`, `k_2 = dim ker H_2`,
`k_1^T = dim ker H_1^T`, `k_2^T = dim ker H_2^T`. If

```
        k_1 > 0  ⟺  k_2 > 0        and        k_1^T > 0  ⟺  k_2^T > 0 ,
```

then `d_X = μ_X`, `d_Z = μ_Z`, and hence `d(Q) = min(μ_X, μ_Z)` and Theorem II.4 applies.

*Proof.* By Corollary II.2 only `d_X ≤ μ_X` (and its mirror) needs proof; and only when `μ_X < ∞`.
*Case `μ_X = d(ker H_2) < ∞`.* Then `k_2 > 0`, so `k_1 > 0` by hypothesis; pick `0 ≠ u ∈ ker H_1` and
`j ∈ supp(u)`. Then `e_j ∉ Im(H_1^T) = rowspace(H_1) = (ker H_1)^⊥`, since `⟨e_j, u⟩ = 1`. Pick
`x ∈ ker H_2` with `|x| = d(ker H_2)` and set `V := e_j x^T`, `W := 0`. Then
`V H_2^T = e_j (H_2 x)^T = 0 = H_1^T W`, so `(V,W) ∈ ker H_Z`, and `|(V,W)| = |x| = μ_X`. If it were
in `S_X` we would have `e_j = ` (column `b` of `H_1^T U`) `= H_1^T U_b ∈ Im(H_1^T)` for any `b` with
`x_b = 1` — contradiction. So `(V,W) ∈ L_X` and `d_X ≤ μ_X`.
*Case `μ_X = d(ker H_1^T) < ∞`.* Then `k_1^T > 0`, so `k_2^T > 0`; pick `0 ≠ v ∈ ker H_2^T` and
`a ∈ supp(v)`, so `e_a ∉ Im(H_2) = (ker H_2^T)^⊥`. Pick `y ∈ ker H_1^T` with `|y| = d(ker H_1^T)`
and set `V := 0`, `W := y e_a^T`. Then `H_1^T W = (H_1^T y) e_a^T = 0 = V H_2^T`, and
`|(V,W)| = μ_X`. If `(0,W) ∈ S_X` then `W = U_0 H_2^T` with `H_1^T U_0 = 0`; row `i` of `U_0 H_2^T`
lies in `Im(H_2)` while row `i` of `y e_a^T` is `y_i e_a^T`, forcing `y_i = 0` for all `i` since
`e_a ∉ Im(H_2)` — contradicting `y ≠ 0`. So `d_X ≤ μ_X`. The `Z`-sector is the mirror under §3.5. ∎

The hypothesis of Lemma II.5 is satisfied in particular whenever `H_1 = H_2` (symmetric products),
and whenever both seeds have full row rank and nonzero kernel (`k_i^T = 0 < k_i`) — which covers the
unrotated planar surface code `HGP(rep_3, rep_3) = [[13,1,3]]` and the toric code
`HGP(C_3, C_3)`, the two families checked NUMERICALLY in
`circdist_cplx_recon_20260820.md` §3 (all local orders safe, zero coupling). It fails only in the
lopsided situations where one seed contributes logicals and its partner does not, in which case
`d(Q)` can exceed `min(μ_X,μ_Z)` and Theorem II.4 must not be invoked.

### 3.5 The `Z`-sector is the `X`-sector of the transposed product

**Lemma II.6 — CONJECTURED.** Under the relabelling `V_A ∋ (j,b) ↦ (b,j)`, `V_B ∋ (i,a) ↦ (a,i)`
and the matrix transposition `(V,W) ↦ (V^T, W^T)`, the `Z`-sector data of `HGP(H_1,H_2)` becomes the
`X`-sector data of `HGP(H_2,H_1)`, `Z`-checks becoming `X`-checks with the same supports.

*Proof.* By the computation of Lemma 3.1 applied to `H_X`: `ker H_X = {(V',W') : H_1 V' = W' H_2}`
and `S_Z = {(G H_2, H_1 G) : G ∈ F_2^{n_1×m_2}}`; `Z`-check `(j,a)` has support
`({j} × T_a) ⊔ (D_j × {a})` with `T_a = supp(row a of H_2)`, `D_j = supp(column j of H_1)`.
Transposing, `V'^T H_1^T = H_2^T W'^T` and `(V'^T, W'^T) = (H̃_1^T Ũ, Ũ H̃_2^T)` with `H̃_1 := H_2`,
`H̃_2 := H_1`, `Ũ := G^T`; and the support of `Z`-check `(j,a)` becomes `(T_a × {j}) ⊔ ({a} × D_j)`,
which is the support of the `X`-check `(ĩ, b̃) = (a, j)` of `HGP(H̃_1, H̃_2)` since
`R̃_a = supp(row a of H̃_1 = H_2) = T_a` and `C̃_j = supp(column j of H̃_2 = H_1) = D_j`. All the
dimensions match: `ñ_1 = n_2, ñ_2 = n_1, m̃_1 = m_2, m̃_2 = m_1`. Finally
`μ̃_X = min(d(ker H̃_2), d(ker H̃_1^T)) = min(d(ker H_1), d(ker H_2^T)) = μ_Z`. ∎

So every `X`-sector statement above transfers verbatim, hooks included. This is what licenses the
word "mirror" in Theorems II.3, II.4 and Lemma II.5.

### 3.6 Two remarks worth registering

**Remark II.7 (the robustness is much stronger than needed).** The proof of Theorem II.3 never uses
that a hook is a *suffix* of an order: it uses only that a single ancilla fault produces a residual
that is a **subset of one check's support**. So HGP codes preserve `d_eff` against any fault model
whose single-fault residuals are subsets of check supports — arbitrary local orders, arbitrary
re-orderings, and (as far as this counting argument is concerned) any single-ancilla variant with
that property. This is a genuinely structural statement: coupling constraints vanish because a hook
of `X`-check `(i,b)` lives in **column `b` of the `A`-block and row `i` of the `B`-block**, and the
product's kernel condition cannot be violated by fewer than `μ_X` lines.

**Remark II.8 (relation to ASSUMPTION A1).** `circdist_cplx_recon_20260820.md` A1 cites
A. G. Manes and J. Claes, *"Distance-preserving stabilizer measurements in hypergraph product
codes"*, **Quantum 9, 1618 (2025)**, arXiv:2308.15520, for the statement that HGP codes are
distance-robust, and flags honestly that its hypotheses were not read. §3.3 above supplies an
independent argument for the `d_eff`-preservation half, so **route R6/premise P6.2 no longer needs
A1 as an assumption** — modulo independent review of Theorem II.1, and modulo the hypothesis of
Theorem II.4 (Lemma II.5), which is exactly the "scope check" the recon asked for and which this
section now makes explicit. What A1 additionally claims (optimality of the Tremblay–Delfosse–
Beverland depth-optimal circuit, and the higher-dimensional extension of arXiv:2409.02193) is
**not** re-derived here and remains an assumption if used.

### 3.7 Scope clause — what Island II does not cover

* **The hypothesis `d(Q) = min(μ_X, μ_Z)` is required and is not automatic.** Corollary II.2 gives
  only `d(Q) ≥ min(μ_X,μ_Z)`. If the seeds are lopsided in the sense of Lemma II.5's hypothesis
  failing, `d(Q)` may be strictly larger, and then Theorem II.3 gives `d_eff(M) ≥ min(μ_X,μ_Z)`
  which may be **less** than `d(Q)` — the island says nothing there, and such an instance could in
  principle be a NO.
* **Only genuine hypergraph products.** The *rotated* surface code is not an HGP code, and is
  measurably not distance-robust (8 of 24 orders of each weight-4 check are locally unsafe —
  NUMERICAL, imported from `circdist_cplx_recon_20260820.md` §3). "Surface code" is ambiguous in
  this context and the ambiguity is not harmless.
* **Higher-dimensional / lifted / weight-reduced products are not covered.** The counting step of
  Theorem II.3 is specific to the two-factor product's "one row + one column per fault" structure.
  Balanced products, lifted products, and weight-reduced qLDPC codes need their own argument;
  arXiv:2409.02193 reportedly covers some of them and remains an unverified assumption.
* **`d_eff`, not `d_circ`.** Same caveat as Island I.
* **This is a constant-YES class, so it contributes tractability but no separation.** It cannot be
  used as raw material for hardness (Island I explains why: no coupling, no reduction).

---

## 4. Island III — bounded-treewidth Tanner graphs: FPT via CMSO / Courcelle

The recon (premise P6.3) flagged this island's **citation** as the one missing piece. §4.4 pins it.

### 4.1 Exact problem statement

**Problem `Eff-Preserve≥[tw ≤ t, w, d]`.**
*Input:* `H_X, H_Z` with `H_X H_Z^T = 0`, given together with the Tanner graph `𝔗` (§4.2) and a tree
decomposition of `𝔗` of width `≤ t`; an integer `d`.
*Parameters:* `t` (treewidth), `w` (maximum check weight), `d`. All three are **parameters, not
inputs**: the algorithm's running time is `f(t,w,d)·|𝔗|`.
*Promise:* `d(Q) = d`, `k ≥ 1` (as always, the algorithm actually decides the total surrogate
`Eff-Preserve≥` of Definition 1.9, so the promise is only needed to convert `≥ d` into `= d`).
*Question:* is there a schedule `M` with `d_eff(M) ≥ d`?

### 4.2 The structure

`𝔗` is the relational structure with universe `V ⊔ E`, where

* `V = Data ⊔ Chk_X ⊔ Chk_Z`: one element per data qubit (`n` of them), one per row of `H_X`, one
  per row of `H_Z`; unary predicates `Data`, `ChkX`, `ChkZ`;
* `E`: one element per incidence, i.e. per pair `(q,c)` with `q ∈ supp(c)`;
* a binary incidence relation `inc(e,x)` holding when `x` is an endpoint of `e`.

We abbreviate `adj(x,y) :≡ ∃e ( inc(e,x) ∧ inc(e,y) )`. Note `deg(c) = w_c ≤ w` for every check
vertex, while data-vertex degrees are **not** bounded by `t` or `w` — this is exactly why modular
counting is needed in §4.3.

The logic is **CMSO₂**: monadic second-order logic over `𝔗` with quantification over subsets of `V`
and over subsets of `E`, extended by the cardinality predicates
`card_{r,p}(S) :≡ |S| ≡ r (mod p)`. Only `p = 2` is used below.

If `G` denotes the Tanner graph as an ordinary graph, `𝔗` is its incidence structure, and
`tw(𝔗) ≤ tw(G) + 1` (take a tree decomposition of `G`; each edge `{u,v}` has a bag containing both;
add the corresponding edge element to one such bag). So "the Tanner graph has treewidth `≤ t`" is a
legitimate hypothesis for CMSO₂ model checking.

### 4.3 The sentence

**Schedule labelling.** Let `E_1,…,E_w` be edge-set variables; `e ∈ E_p` is read "the data endpoint
of `e` is the `p`-th qubit in the local order of the check endpoint of `e`".

```
  Sched(E_1,…,E_w)  :≡
        ∀e ( ⋁_{p=1}^{w} e ∈ E_p )                                              (total)
    ∧   ⋀_{p<p'} ¬∃e ( e ∈ E_p ∧ e ∈ E_{p'} )                                   (single-valued)
    ∧   ∀c ∀e ∀e' [ (¬Data(c) ∧ inc(e,c) ∧ inc(e',c) ∧ e ≠ e')
                     →  ⋀_{p=1}^{w} ¬( e ∈ E_p ∧ e' ∈ E_p ) ]                   (injective at c)
    ∧   ⋀_{p=2}^{w} ∀c [ (¬Data(c) ∧ ∃e(inc(e,c) ∧ e ∈ E_p))
                     →  ∃e'(inc(e',c) ∧ e' ∈ E_{p-1}) ]                         (initial segment)
```

The last two clauses force the labels used at a check `c` to be exactly `1,…,deg(c)` and pairwise
distinct, i.e. a bijection `supp(c) → {1,…,w_c}`, i.e. a linear order `π_c`. Conversely every
schedule `(π_c)_c` gives such a labelling. So **well-formed labellings are in bijection with
schedules** (Lemma 1.2 makes this the whole of `M`).

**Hooks.** For `1 ≤ p ≤ w − 1`,

```
  Hk_p(q, c)  :≡  Data(q) ∧ ∃e ( inc(e,q) ∧ inc(e,c) ∧ ⋁_{p'=p+1}^{w} e ∈ E_{p'} )
```

says `q ∈ S_p(π_c)`. (If `p ≥ w_c` the formula is unsatisfiable and the hook is empty — harmless.)

**Mechanism shapes.** Since `d` and `w` are parameters, the following is a *finite* disjunction. A
**shape** is a triple `σ = (δ, h, (p_1,…,p_h))` with `δ, h ≥ 0`, `δ + h ≤ d − 1`, `h ≥ 1`, and
`1 ≤ p_s ≤ w − 1`. For a shape `σ`, with first-order variables `q_1,…,q_δ` (data) and `c_1,…,c_h`
(X-checks), define the residual-membership formula

```
  In_σ(q)  :≡  ( ⊕_{s=1}^{δ} (q = q_s) )  ⊕  ( ⊕_{s=1}^{h} Hk_{p_s}(q, c_s) )
```

(`⊕` = exclusive or; a bounded Boolean combination of `≤ d − 1` first-order formulas), and

```
  Undet(Y)   :≡  ∀z [ ChkZ(z) → ∃S ( ∀x( x ∈ S ↔ (x ∈ Y ∧ adj(x,z)) ) ∧ card_{0,2}(S) ) ]

  InStab(Y)  :≡  ∃T [ ∀y( y ∈ T → ChkX(y) )
                      ∧ ∀q ( Data(q) →
                             [ ∃S ( ∀y( y ∈ S ↔ (y ∈ T ∧ adj(y,q)) ) ∧ card_{1,2}(S) )
                               ↔  q ∈ Y ] ) ]

  Mech_σ^X   :≡  ∃Y [ ∀q ( q ∈ Y ↔ ( Data(q) ∧ In_σ(q) ) )
                      ∧ Undet(Y) ∧ ¬InStab(Y) ]
```

`Undet(Y)` says `H_Z χ_Y = 0`; `InStab(Y)` says `χ_Y ∈ S_X`, since `Σ_{c ∈ T} χ_{supp(c)} = χ_Y`
holds iff for every data qubit `q` the number of checks of `T` incident to `q` has the same parity
as `[q ∈ Y]`. Note `0 ∈ S_X`, so `¬InStab(Y)` already implies `Y ≠ ∅`; no separate clause is needed.
Let `Mech_σ^Z` be the mirror (`c_s` ranging over `ChkZ`, `Undet` quantifying over `ChkX`, `InStab`
over `ChkZ`). Finally

```
  Φ_{t,w,d}  :≡  ∃E_1 … ∃E_w [  Sched(E_1,…,E_w)
                    ∧  ⋀_{σ} ∀q_1…∀q_δ ∀c_1…∀c_h ( ⋀_s ChkX(c_s) → ¬Mech_σ^X )
                    ∧  ⋀_{σ} ∀q_1…∀q_δ ∀c_1…∀c_h ( ⋀_s ChkZ(c_s) → ¬Mech_σ^Z )  ]
```

**Where counting is genuinely needed.** `Undet` could be written without `card_{0,2}` by enumerating
the `≤ w` neighbours of `z`. `InStab` could **not**: a data qubit may be incident to unboundedly many
X-checks, and the parity of `|T ∩ N(q)|` for a quantified set `T` is not first-order expressible.
This is the single place where CMSO strictly exceeds MSO in the construction, and it is
unavoidable in this encoding.

**Lemma III.1 (correctness) — CONJECTURED.** `𝔗 ⊨ Φ_{t,w,d}` iff there is a schedule `M` with
`d_eff(M) ≥ d`.

*Proof.* (⇐) Given `M`, let `E_p := { (q,c) : q` is the `p`-th qubit of `π_c }`; `Sched` holds.
Suppose some `Mech_σ^X` held for some shape `σ` and some witnesses. Its `Y` is, by the defining
clause, the support of `χ_{q_1} + ⋯ + χ_{q_δ} + χ_{S_{p_1}(π_{c_1})} + ⋯ + χ_{S_{p_h}(π_{c_h})}`
(the XOR `In_σ` computes exactly the parity of memberships). By `Undet ∧ ¬InStab`, this vector lies
in `L_X`. Hence the multiset `F` of the corresponding `δ + h ≤ d − 1` columns of `Cols_X(M)`
(Lemma 1.1) is a mechanism, so `d_eff(M) ≤ d − 1` — contradiction. Same for `Z`.
(⇒) Given a satisfying labelling, define `π_c` by the labels; `Sched` guarantees each `π_c` is a
linear order. If `d_eff(M) ≤ d − 1`, take a minimal mechanism `F`, written as a *set*
`(D, (I_c)_c)` by Lemma 1.5, in the sector where it lives, say `X`. It has `|D| = δ` data columns
and `h = Σ_c |I_c| ≥ 1` hook columns (`h ≥ 1` by Lemma 1.10 — this is where the promise is used),
`δ + h ≤ d − 1`, so it is an instance of the shape `σ = (δ,h,(p_1,…,p_h))` where `p_s` are the hook
indices (repetitions of the same check are allowed: the variables `c_s` need not be distinct). Its
`Y` is `supp(Σ F) ∈ L_X`, so `Undet(Y) ∧ ¬InStab(Y)` holds and `Mech_σ^X` is satisfied — contradicting
`Φ`. Note also that the universal quantification over *tuples* rather than sets is harmless: a tuple
with repetitions computes the sum of its odd-multiplicity elements, which is again the sum of at
most `d − 1` columns. ∎

`|Φ_{t,w,d}|` depends only on `w` and `d` (the number of shapes is at most
`Σ_{δ+h ≤ d−1} w^{h}`, and each conjunct has bounded size), not on `n`.

### 4.4 The pinned citation

> **Courcelle's theorem, CMSO₂ form (the exact statement used here).** There is a computable
> function `f` such that the following holds. Let `φ` be a sentence of counting monadic
> second-order logic with quantification over vertex sets and edge sets (CMSO₂), where the counting
> predicates are `card_{r,p}(S) :≡ |S| ≡ r (mod p)`. Let `G` be a finite graph with `N` vertices and
> edges in total, **given together with a tree decomposition of width `≤ t`**. Then whether
> `G ⊨ φ` is decidable in time `f(|φ|, t) · N`.

**Sources, split by which half each one supplies.**

* **[Cou90]** B. Courcelle, *"The monadic second-order logic of graphs I: Recognizable sets of
  finite graphs"*, **Information and Computation 85(1) (1990) 12–75**. This is the paper that
  introduces the cardinality-modulo predicates `card_{r,p}` and proves that every CMSO-definable
  class of graphs of bounded tree-width is *recognizable* — i.e. decided by a finite-state automaton
  running on the tree of a bounded-width decomposition. This is the half that supplies **CMSO**
  (as opposed to plain MSO). *Verification status this session: bibliographic data confirmed via an
  authoritative secondary source (the Wikipedia article "Courcelle's theorem", which cites exactly
  this paper both for the base theorem and for the CMSO₁/CMSO₂ extension with `card_{q,r}`); the
  primary text was **not** read this session.* **Flagged: a reviewer should read [Cou90] and record
  the theorem number.**
* **[ALS91]** S. Arnborg, J. Lagergren, D. Seese, *"Easy problems for tree-decomposable graphs"*,
  **Journal of Algorithms 12(2) (1991) 308–340**. This is the paper usually cited for the explicit
  **linear-time algorithmic form** (given the decomposition) and for the extension of the logic with
  counting/evaluation. *Verification status: bibliographic data (volume, issue, pages, year)
  confirmed by search; primary text not read.*
* **[CE12]** B. Courcelle, J. Engelfriet, *"Graph Structure and Monadic Second-Order Logic: A
  Language-Theoretic Approach"*, Encyclopedia of Mathematics and its Applications **138**, Cambridge
  University Press, 2012. Cited for the **MSO₂** half: quantification over edge sets is MSO₁ over
  the incidence structure, and the bounded-treewidth theorem applies there
  (*Proposition 5.13, p. 338* — theorem number taken from the secondary source above, **not**
  verified against the book).
* **Tree decomposition, if not supplied with the input:** H. L. Bodlaender, *"A linear-time
  algorithm for finding tree-decompositions of small treewidth"*, **SIAM J. Comput. 25(6) (1996)
  1305–1317** (time `2^{O(t^3)} n`); or, for a better parameter dependence at the cost of a
  5-approximation, H. L. Bodlaender, P. G. Drange, M. S. Dregi, F. V. Fomin, D. Lokshtanov,
  M. Pilipczuk, *"A `c^k n` 5-approximation algorithm for treewidth"*, **SIAM J. Comput. 45(2)
  (2016) 317–378**. *Standard; not re-verified.*
* **The parameter dependence is unavoidably bad:** M. Frick, M. Grohe, *"The complexity of
  first-order and monadic second-order logic revisited"*, **Annals of Pure and Applied Logic
  130(1–3) (2004) 3–31**: MSO model checking on trees cannot be done in time
  `f(|φ|)·n^{O(1)}` with `f` elementary, unless P = NP. *Bibliographic data confirmed via the same
  secondary source.*

**Honest note on the pin.** The *statement* above is standard and is what the island needs; what
this session could not do inside the box is quote a theorem number from a primary text. Two
secondary confirmations were obtained (the Wikipedia article's citation list, and a search-level
confirmation of the [ALS91] bibliographic data). A textbook restatement exists in M. Cygan,
F. V. Fomin, Ł. Kowalik, D. Lokshtanov, D. Marx, M. Pilipczuk, M. Pilipczuk, S. Saurabh,
*Parameterized Algorithms*, Springer 2015, §7.4 ("Courcelle's theorem"), but this session **could
not confirm the theorem number** and therefore does not assert one. The remaining action is a
15-minute primary-source check; it should be recorded as a premise, not as a discharged assumption.

### 4.5 The theorem

**Theorem III — CONJECTURED (modulo the pinned external theorem of §4.4).** Let `t, w, d` be fixed.
Given `H_X, H_Z` whose Tanner graph has treewidth `≤ t` and whose checks have weight `≤ w`,
`Eff-Preserve≥` is decidable in time `f(t,w,d) · (n + m_X + m_Z)` if a width-`t` tree decomposition
is supplied, and in time `2^{O(t^3)}·n + f(t,w,d)·n` otherwise. In particular Eff-Preserve restricted
to this class is fixed-parameter tractable in `(t,w,d)`, and polynomial (indeed linear) for each
fixed choice of the three.

*Proof.* Build `𝔗` (linear time) and, if necessary, a tree decomposition (Bodlaender). Build
`Φ_{t,w,d}`; its size is a function of `w` and `d` only. Apply the theorem of §4.4 to `𝔗` (whose
treewidth is `≤ t + 1`). Lemma III.1 gives correctness, and Lemma 1.8 converts `≥ d` to `= d` under
the promise. ∎

**Corollary III.1 (V2 also) — CONJECTURED.** If a depth bound `T` is added (variant V2 of the
recon), the problem stays FPT in `(t,w,d,T)`: add edge-set variables `Θ_1,…,Θ_T` for the time step
of each CNOT, require `⋀_{τ} ∀e ∀e' ( e ≠ e' ∧ e,e' ∈ Θ_τ → ¬∃x( inc(e,x) ∧ inc(e',x) ) )`
(properness: no qubit — data **or** check — repeats within a step), and require compatibility with
the order labelling: for each check `c` and each `p < p'`, the edge at `c` labelled `p` occurs in an
earlier `Θ` than the one labelled `p'`, a bounded disjunction over `T^2` pairs. Everything remains
CMSO₂ of bounded size. ∎

### 4.6 Scope clause — what Island III does not cover

* **`d` must be a parameter.** With `d` part of the input, the number of shapes and hence `|Φ|` grows
  with `n` and Courcelle does not apply. The island therefore lives in the *fixed-`d`* half of 课题三,
  and says nothing about the `Σ_2^P` classification.
* **`w` must be a parameter.** Bounded treewidth does not bound check weight; both are needed, `w` to
  bound the number of edge-label classes and the shape set.
* **The constant `f(t,w,d)` is non-elementary** (Frick–Grohe). This is a *classification* result:
  it places the restricted problem in FPT, and it is not an algorithm anyone should run. A direct
  dynamic program over the tree decomposition would give a far better — but much longer to
  write — bound, and is not attempted here.
* **Possible near-vacuity.** Bounded treewidth is a strong connectivity restriction, and
  separator-based trade-offs for quantum codes (ASSUMPTION A11 — Baspin–Krishna, *"Connectivity
  constraints on quantum codes"* / *"Quantifying nonlocality"*, 2021–2022) bound `k` and `d`
  together for codes with small separators. **This session did not verify the exact form of that
  trade-off**, so the honest statement is: the island is certainly non-vacuous at fixed small `d`
  (e.g. `d = 3, 4`), and whether it contains families with growing `d` is *not established here*. A
  reviewer should not read Island III as covering large-distance qLDPC codes; it almost certainly
  does not.
* **The hypothesis is on the Tanner graph, not on the connectivity of a layout.** No claim is made
  about geometrically local codes.
* **CMSO encoding is mine, not imported.** `Φ_{t,w,d}` is a construction of this session
  (as the recon's A10 note already said: "the CMSO encoding itself … is my own and is a premise").
  Lemma III.1 is the premise that needs review; §4.4 is the part that needs a citation check.

---

## 5. Island IV — `d = 3` with two allowed local orders per check: 2-SAT

This is Proposition D of `circdist_cplx_recon_20260820.md` §5.4, written out in full. It is the
island that **refutes a target proposed by the problem statement**, so it is worth stating with
unusual care about what "two allowed orders" means.

### 5.1 Exact problem statement

**Problem `Eff-Preserve≥[d = 3, |Λ| ≤ 2]`.**
*Input:* `H_X ∈ F_2^{m_X×n}`, `H_Z ∈ F_2^{m_Z×n}` with `H_X H_Z^T = 0`; the integer `d = 3`; and, for
every check `c` (both sectors), an explicitly listed set `Λ_c` of **allowed** local orders of
`supp(c)` with `|Λ_c| ≤ 2`.
*Promise:* `d(Q) = 3` exactly, and `k ≥ 1`.
*Question:* is there a schedule `M` with `π_c ∈ Λ_c` for every `c` and `d_eff(M) ≥ 3` (equivalently
`= 3`)?

**Where `Λ` comes from — the honest reading.** 课题三 proposes "每个 check 只允许两个或少数几个局部
CNOT order" as a *restriction* meant to make the problem harder. In V1 this restriction is **not a
property of the code**: nothing in `(H_X,H_Z)` forbids an order. So it must be one of

* **(Λ-input)** extra input, as in the statement above — the version handled by Theorem IV; or
* **(Λ-intrinsic)** a *derived* set, namely `Λ_c := D_c`, the locally safe orders of Definition 2.2 —
  handled by Corollary IV.2; or
* **(Λ-timing)** a consequence of V2 depth constraints — **not** covered here (see the scope clause).

Making the restriction extra input makes any hardness theorem *weaker* (the reduction gets a free
lever), and Theorem IV shows that even with that free lever the target is unreachable in V1.

### 5.2 Structure of the constraints at `d = 3`

**Lemma IV.1 (arity `≤ 2`) — CONJECTURED.** Under the promise `d(Q) = 3`, every mechanism `F` with
`|F| ≤ 2` (written as a set, Lemma 1.5) is of exactly one of the following four kinds:

| kind | `F` | scope |
|---|---|---|
| (a) | one hook `S_i(π_c)` | `{c}` |
| (b) | one hook `S_i(π_c)` and one data column `e_q` | `{c}` |
| (c) | two hooks `S_i(π_c), S_j(π_c)` of the **same** check | `{c}` |
| (d) | two hooks `S_i(π_c), S_j(π_{c'})` with `c ≠ c'` | `{c,c'}` |

In particular `|scope(F)| ≤ 2`, so the CSP of Proposition 1.11 has **arity `≤ 2`**.

*Proof.* By Lemma 1.10 (which uses the promise) `scope(F) ≠ ∅`, so `F` contains at least one hook.
If `|F| = 1` this is (a). If `|F| = 2`, the second element is a data column — case (b) — or a hook,
in which case it belongs to the same check (c) or a different one (d). The excluded configuration
"two data columns" would give `χ_{\{q,q'\}} ∈ L_X`, a nontrivial undetectable pattern of weight
`≤ 2 < 3 = d(Q) ≤ d_X`; likewise "one data column" alone. ∎

Kinds (a)–(c) are exactly the failure of local safety of `π_c` at `d = 3` (Definition 2.2), and
kind (d) is exactly the `d = 3` coupling relation of §1.5 / Definition 2.3.

### 5.3 The reduction

Fix the input. Preprocess `H_Z` and `H_X` into reduced row-echelon form, `O(n^3)`, so that the
predicate `v ∈ L_X` (`H_Z v = 0` and `v ∉ S_X`) costs `O(n^2)` per query; likewise `L_Z`.

**Step 0.** If `Λ_c = ∅` for some `c`, output **NO** and stop.

**Step 1 (variables).** For each check `c` with `|Λ_c| = 2`, write `Λ_c = {π_c^0, π_c^1}` and
introduce a Boolean variable `X_c`; define the literal
`ℓ_c(π_c^0) := ¬X_c`, `ℓ_c(π_c^1) := X_c`. For each check with `Λ_c = {π_c}` a singleton, introduce
`X_c` as well and add the unit clause `X_c`, and set `ℓ_c(π_c) := X_c` (so `ℓ_c` of the unique
allowed order is forced true; this keeps every clause below a genuine 2-clause).

**Step 2 (unary clauses).** For every check `c` and every `π ∈ Λ_c`: test local safety of `π` — i.e.
test whether any of the kinds (a), (b), (c) of Lemma IV.1 occurs for `π`. If `π` is **not** locally
safe, add the unit clause `¬ℓ_c(π)`.

**Step 3 (binary clauses).** For every unordered pair of distinct checks `c ≠ c'` **in the same
sector**, and every `π ∈ Λ_c`, `π' ∈ Λ_{c'}`: if there exist hooks `A ∈ Hooks(π)`,
`A' ∈ Hooks(π')` with `χ_A + χ_{A'} ∈ L_X` (resp. `L_Z`), add the clause
`¬ℓ_c(π) ∨ ¬ℓ_{c'}(π')`.

**Step 4.** Run a linear-time 2-SAT decision procedure on the resulting 2-CNF `Ψ`; output its
answer.

**Theorem IV — CONJECTURED.** Step 0–4 decides `Eff-Preserve≥[d = 3, |Λ| ≤ 2]` correctly, in time

```
        O( n^3  +  M · w · n · n^2  +  M^2 · w^2 · n^2 )     where M = Σ_c |Λ_c| ≤ 2(m_X + m_Z),
```

which is polynomial in the input size. **No bound on the check weight `w` is needed.**

*Proof.*

*Correctness of the encoding of schedules.* An assignment `α` of the `X_c` satisfying the unit
clauses of Step 1 for singleton lists corresponds to a tuple `(π_c)_c ∈ ∏_c Λ_c`, namely
`π_c := π_c^{α(X_c)}`; and conversely. The correspondence is a bijection onto `∏_c Λ_c` once the
Step-1 unit clauses are imposed. In V1 every such tuple is a legal schedule (Model M2).

*Correctness of the constraints.* Fix `M = (π_c)_c ∈ ∏_c Λ_c` and let `α` be the corresponding
assignment. We claim `d_eff(M) ≥ 3` iff `α ⊨ Ψ`.

(⇒) Suppose `d_eff(M) ≥ 3`, i.e. no mechanism of size `≤ 2` exists for `M`. If some Step-2 unit
clause `¬ℓ_c(π)` were violated then `α` picks `π_c = π`, and `π` is not locally safe, so one of
kinds (a),(b),(c) is a mechanism of size `≤ 2` for `M` — contradiction. If some Step-3 clause
`¬ℓ_c(π) ∨ ¬ℓ_{c'}(π')` were violated then `α` picks `π_c = π` and `π_{c'} = π'`, and the witnessing
pair `{A, A'}` is a kind-(d) mechanism of size 2 for `M` — contradiction. (Note `A ≠ A'` as vectors
is not needed: if `χ_A = χ_{A'}` then `χ_A + χ_{A'} = 0 ∉ L_X`, so such a pair is never a witness.)
The Step-1 unit clauses hold by construction. So `α ⊨ Ψ`.

(⇐) Suppose `α ⊨ Ψ` and suppose towards a contradiction that `F` is a mechanism for `M` with
`|F| ≤ 2`. By Lemma IV.1 it is of kind (a),(b),(c) — then the check `c` in its scope has `π_c` not
locally safe, so Step 2 added `¬ℓ_c(π_c)`, which `α` violates — or of kind (d) — then Step 3 added
`¬ℓ_c(π_c) ∨ ¬ℓ_{c'}(π_{c'})`, which `α` violates. Either way `α ⊭ Ψ`, a contradiction. Hence
`d_eff(M) ≥ 3`.

*Assembly.* `∃M ∈ ∏_c Λ_c : d_eff(M) ≥ 3` iff `Ψ` is satisfiable. Under the promise, Lemma 1.8
converts `≥ 3` into `= 3`.

*Running time.* Step 2 tests, for one order `π` of one check `c`: `w_c − 1` queries for kind (a),
`(w_c − 1)·n` for kind (b), `C(w_c−1, 2)` for kind (c) — `O(w_c n + w_c^2)` queries of cost `O(n^2)`
each, and `w_c ≤ n`. Summed over the `M` listed orders this is `O(M w n^3)` as displayed (absorbing
`w_c^2 ≤ w n`). Step 3 tests `O(M^2)` pairs of listed orders with `O(w^2)` hook pairs each, at
`O(n^2)` per query. 2-SAT is linear in `|Ψ| = O(M^2)`
(**[APT79]** B. Aspvall, M. F. Plass, R. E. Tarjan, *"A linear-time algorithm for testing the truth
of certain quantified Boolean formulas"*, Information Processing Letters **8(3)** (1979) 121–123;
also **[EIS76]** S. Even, A. Itai, A. Shamir, SIAM J. Comput. **5(4)** (1976) 691–703. *Standard,
not re-verified this session.*) ∎

**Corollary IV.2 (code-intrinsic version) — CONJECTURED.** Suppose `d = 3` and the *code itself*
admits at most two locally safe orders per check, i.e. `|D_c| ≤ 2` for every `c` (Definition 2.2).
Then Eff-Preserve is in P: compute the `D_c` (time `O(Σ_c w_c! · w_c n · n^2)`, polynomial when the
check weight is bounded), set `Λ_c := D_c`, and run Theorem IV — noting that Step 2 then adds no
unit clauses, and that by Theorem I(1) the answer is NO as soon as some `D_c = ∅`. ∎

**Corollary IV.3 (what this refutes) — CONJECTURED.** In V1, the combination proposed by 课题三 as a
target for a *strong* NP-completeness theorem — "fixed `d = 3`" together with "each check allows only
two local CNOT orders" — is **provably tractable**, in either the (Λ-input) or the (Λ-intrinsic)
reading. Any hardness attempt must move to one of the two open cells of the recon's frontier table:

| | domain `≤ 2` | domain `≥ 3` |
|---|---|---|
| `d = 3` (arity `≤ 2`) | **P** — Theorem IV | open; `≠₃` relations *are* realisable (gadget doc §3, NUMERICAL), but only in transitive cliques (gadget doc §5.3) |
| `d ≥ 4` (arity `≤ 3`) | open — NAE/1-in-3-shaped | open |

∎

### 5.4 Scope clause — what Island IV does not cover

* **`d = 3` exactly.** At `d ≥ 4` the budget is `≥ 3` columns and Lemma IV.1 fails: mechanisms may
  couple three checks, so the CSP has arity 3 and the Boolean encoding gives 3-CNF, not 2-CNF. The
  `(d ≥ 4, domain 2)` cell is genuinely open.
* **Domain `≤ 2` exactly.** With three allowed orders the CSP is binary over a 3-element domain,
  which is 3-colouring-shaped, and the `≠₃` relation is realisable by an explicit CSS gadget
  (imported NUMERICAL, `circdist_cplx_gadget_20260820.md` §3). What blocks hardness there is a
  *different* obstruction (the clique/transitivity phenomenon of gadget doc §5.3), not Theorem IV.
* **(Λ-timing) is not covered.** If the restriction to two orders is a *consequence* of a depth bound
  (V2), then the sets `Λ_c` are not independent: a tuple in `∏_c Λ_c` need not extend to a legal
  depth-`T` schedule. The bijection in the proof breaks, and Latin-square-completion hardness
  (ASSUMPTION A7) enters. Island IV is a V1 statement.
* **The promise is load-bearing** in exactly one place: Lemma 1.10 / Lemma IV.1, to exclude
  data-only mechanisms. Without the promise the same algorithm still decides `Eff-Preserve≥` after
  one extra check ("is there a nontrivial logical of weight `≤ 2`?", which is `O(n^3)` — but for
  general `d` that check *is* the NP-hard distance problem, ASSUMPTION A5).
* **It is a tractability result and gives no separation.** It removes a target; it does not settle
  the fixed-`d` complexity of Eff-Preserve.

---

## 6. Island V — the weight-4 / `d_X ≥ 4` regime — **and the gap**

This is `circdist_cplx_gadget_20260820.md` §5.4. Writing it out rigorously turned up a genuine
problem, so this section is organised as: the reduction (§6.3, correct and, I believe, exactly
right), the two theorems that survive (§6.4), and the **gap** (§6.5).

### 6.1 Exact problem statement

**Problem `Eff-Preserve≥^X[w ≤ 4, d_X ≥ 4]`.**
*Input:* `H_X, H_Z` with `H_X H_Z^T = 0`; the integer `d = 3`.
*Promise:* `d(Q) = 3` and `k ≥ 1`; **every X-check has weight `≤ 4`**; and `d_X ≥ 4`
(hence `d_Z = 3`, since `d = min(d_X,d_Z) = 3`).
*Question:* is there a tuple of local orders of the X-checks with `d_eff^X(M) ≥ 3`?

Note the hypothesis list forces this to be a **one-sector** problem: `d_X ≥ 4` and `d = 3` together
say the binding sector is `Z`. By Proposition 2.1 the full Eff-Preserve question factorises, so an
answer here is a genuine half of an answer — but it must be paired with a separate treatment of the
`Z`-sector (Island I, III or IV), and it is **not** by itself a decision procedure for
Eff-Preserve. `circdist_cplx_gadget_20260820.md` §5.4 states this correctly ("the X-sector is …")
but its executive summary ("the whole CSP collapses to a list-all-different problem") does not; the
weaker reading is the correct one.

*Generalisation over the source document.* The gadget document assumes every X-check has weight
**exactly** 4. Lemma V.1 below shows checks of weight `≤ 3` contribute no constraint at all, so the
hypothesis can be relaxed to weight `≤ 4`, with only the weight-4 checks carrying CSP variables.

### 6.2 The weight-4 law

Write `ρ(v) := min{ |u| : λ(u) = λ(v) }` for the **reduced weight** of the class of `v` in
`Q = F_2^n/S_X`; `ρ` is subadditive: `ρ(v + v') ≤ ρ(v) + ρ(v')`.

**Lemma V.0 — CONJECTURED.** If `λ(v) ∈ Log \ {0}` then `ρ(v) ≥ d_X`.
*Every `u` with `λ(u) = λ(v)` lies in `v + S_X ⊆ C_X` and is not in `S_X` (else `v ∈ S_X`), hence
`u ∈ L_X` and `|u| ≥ d_X`.* ∎

**Lemma V.1 (weight-`≤ 4` law) — CONJECTURED.** Assume the promise of §6.1. Let `c` be an X-check
with `w_c ≤ 4` and let `π = (q_1,…,q_{w_c})` be any local order. Then:

1. **(hook reduction)** `ρ(χ_{S_i(π)}) ≤ 1` for every `i`, **except** when `w_c = 4` and `i = 2`, in
   which case `ρ(χ_{S_2(π)}) ≤ 2`. Explicitly, by Lemma 1.12,
   `λ(S_1) = a_{q_1}`, `λ(S_2) = a_{q_1}+a_{q_2}`, `λ(S_3) = a_{q_4}` for `w_c = 4`;
   `λ(S_1) = a_{q_1}`, `λ(S_2) = a_{q_3}` for `w_c = 3`; `λ(S_1) = a_{q_2}` for `w_c = 2`.
2. **(unary safety)** *Every* local order of *every* X-check is locally safe (Definition 2.2 at
   `d = 3`).
3. **(only middle–middle couples)** The only mechanisms of size `≤ 2` with scope of size 2 are pairs
   `{ S_2(π_c), S_2(π_{c'}) }` with `c ≠ c'`, `w_c = w_{c'} = 4`.
4. **(value map)** For a weight-4 check `c`, `λ(χ_{S_2(π)}) = λ(χ_{P_2(π)})` depends only on the
   unordered `2|2` split `{P_2, S_2}` of `supp(c)`. There are exactly **three** such splits, each
   realised by exactly 8 of the 24 orders. Write `L_c := { x_c^{(1)}, x_c^{(2)}, x_c^{(3)} } ⊆ Q` for
   the resulting values (a multiset; coincidences are possible, see (6)).
5. **(the three values sum to zero)** `x_c^{(1)} + x_c^{(2)} + x_c^{(3)} = 0` in `Q`.
6. **(degenerate values are harmless)** If `x_c^{(r)} = 0` then no pair involving it is forbidden.

*Proof.* (1) `λ(χ_{S_i}) = λ(χ_{P_i})` by Lemma 1.12, and `|P_1| = 1`, `|P_2| = 2`,
`|P_3| = 3` while also `S_3 = \{q_4\}` has `|S_3| = 1`; take the smaller representative in each case.
For `w_c = 3`: `|P_1| = 1` and `S_2 = \{q_3\}`. For `w_c = 2`: `S_1 = \{q_2\}`.

(2) By Lemma IV.1 a unary mechanism is (a) one hook, (b) one hook + one data column, or (c) two
hooks of the same order. Data columns have `ρ ≤ 1`. Any order has **at most one** hook of reduced
weight 2 (namely `S_2` when `w_c = 4`), so by subadditivity all three kinds give
`ρ ≤ 2 + 1 = 3 < 4 ≤ d_X`, and Lemma V.0 says such a sum is not in `Log \ {0}`.

(3) By Lemma IV.1 the only scope-2 mechanism is `{S_i(π_c), S_j(π_{c'})}`, `c ≠ c'`. If not both
hooks are middle hooks of weight-4 checks, subadditivity gives `ρ ≤ 2 + 1 = 3 < d_X`, excluded by
Lemma V.0. (Two middle hooks give only `ρ ≤ 4`, which is not excluded.)

(4) `P_2(π) = \{q_1,q_2\}`, `S_2(π) = \{q_3,q_4\}`, and `λ` agrees on the two halves; so the value
depends only on the partition. A 4-set has three `2|2` partitions; the orders realising a given
partition `{P, P^c}` are those with `{q_1,q_2} ∈ \{P, P^c\}`: 2 choices of which half comes first,
`2! · 2!` internal orders, i.e. 8; and `3 × 8 = 24`.

(5) The three partitions correspond to the three 2-subsets containing `q_1`, and
`(a_{q_1}+a_{q_2}) + (a_{q_1}+a_{q_3}) + (a_{q_1}+a_{q_4}) = Σ_{q ∈ supp(c)} a_q = λ(χ_{supp(c)}) = 0`
since `χ_{supp(c)} ∈ S_X`.

(6) If `x_c = 0` then `x_c + x_{c'} = x_{c'}`, and `ρ(x_{c'}) ≤ 2 < 4 ≤ d_X`, so by Lemma V.0
`x_{c'} ∉ Log \ {0}` and the pair is not forbidden. ∎

**Corollary V.2 (the CSP, explicitly) — CONJECTURED.** Under the promise of §6.1, the X-sector
question is the following CSP:

* *variables*: the X-checks of weight exactly 4 (checks of weight `≤ 3` are unconstrained and may be
  ordered arbitrarily);
* *domain of `c`*: the three values `L_c ⊆ Q` of Lemma V.1(4); every value is attainable, and the
  eight orders realising a value are interchangeable;
* *constraints*: for `c ≠ c'`,
  `forbidden(x_c, x_{c'}) ⟺ x_c + x_{c'} ∈ Log \ {0} ⟺ ν(x_c) = ν(x_{c'}) and x_c ≠ x_{c'}`;
* there are **no** unary constraints (Lemma V.1(2)).

*Immediate from Lemma V.1, Lemma IV.1 and Proposition 1.14.* ∎

This is the precise sense of the gadget document's slogan "**two checks may share a `Log`-coset only
by choosing the identical value**".

### 6.3 The exact reduction: a partial-section problem

Fix an `F_2`-linear splitting `Q = Log ⊕ N` (which exists: extend a basis of `Log` to a basis of
`Q`), with projections `β : Q → Log` and `m : Q → N`, so `x = β(x) + m(x)`. Since
`ν(x) = ν(x') ⟺ x + x' ∈ Log ⟺ m(x) = m(x')`, Corollary V.2 becomes

```
    forbidden(x_c, x_{c'})   ⟺   m(x_c) = m(x_{c'})   and   β(x_c) ≠ β(x_{c'}) .
```

**Theorem V.3 (exact form of the island) — CONJECTURED.** Under the promise of §6.1, the following
are equivalent:

1. there is a schedule with `d_eff^X(M) ≥ 3`;
2. there is a choice `x_c ∈ L_c` (one per weight-4 X-check) such that
   `m(x_c) = m(x_{c'}) ⟹ β(x_c) = β(x_{c'})` for all `c, c'`;
3. there is a **partial function** `g : N ⇀ Log` such that every weight-4 X-check `c` has some
   `x ∈ L_c` with `m(x) ∈ dom(g)` and `g(m(x)) = β(x)`.

*Proof.* (1) ⟺ (2) is Corollary V.2 plus the displayed reformulation. (2) ⟹ (3): define `g` on
`{ m(x_c) : c }` by `g(m(x_c)) := β(x_c)`; the implication in (2) is exactly the statement that this
is well defined. (3) ⟹ (2): choose for each `c` a witness `x_c ∈ L_c` as in (3); if
`m(x_c) = m(x_{c'})` then `β(x_c) = g(m(x_c)) = g(m(x_{c'})) = β(x_{c'})`. ∎

Two structural side conditions come for free and must be recorded, because they are the only things
that distinguish this from an arbitrary instance of the abstract problem in §6.5:

```
    (S1)   Σ_{r=1}^{3} β(x_c^{(r)}) = 0  in Log,     (S2)   Σ_{r=1}^{3} m(x_c^{(r)}) = 0  in N ,
```

both immediate from Lemma V.1(5) and linearity of `β, m`. In addition, the *lists* `L_c` are not
arbitrary: they must be realisable by an actual CSS code of check weight `≤ 4` with `d_X ≥ 4` and
`d_Z = 3`, and the whole content of `circdist_cplx_gadget_20260820.md` §4–§5 is that this
realisability is severely constrained.

### 6.4 What survives: two theorems

**Theorem V.4 (`k ≤ 1` forces YES) — CONJECTURED.** Under the promise of §6.1, if `k ≤ 1` then
**every** choice-free instance is a YES: there is a schedule with `d_eff^X(M) ≥ 3`, and it is found
in linear time.

*Proof.* If `k = 0` then `Log = 0`, so `Log \ {0} = ∅` and no pair is forbidden (Corollary V.2); any
schedule works.

Let `k = 1`, so `Log = {0, ℓ}` with `ℓ ≠ 0`. Choose a linear splitting `Q = Log ⊕ N` and let
`β : Q → Log` be the projection along `N`; `β` is `F_2`-linear and `β|_{Log} = id`, in particular
`β(ℓ) = ℓ`.

*Every check has an option with `β = 0`.* By Lemma V.1(5),
`β(x_c^{(1)}) + β(x_c^{(2)}) + β(x_c^{(3)}) = β(0) = 0` in `Log = {0,ℓ} ≅ F_2`. Writing
`β(x_c^{(r)}) = ε_r ℓ` with `ε_r ∈ F_2`, this says `ε_1 + ε_2 + ε_3 = 0`, i.e. the number of `r` with
`ε_r = 1` is **even**, hence is `0` or `2`; in either case some `r` has `ε_r = 0`. (This is the
whole content of the parity argument: three values cannot all be "odd" when they sum to zero in a
one-dimensional `F_2`-space.)

*Choosing them all works.* Pick, for every weight-4 X-check `c`, an option `x_c ∈ L_c` with
`β(x_c) = 0`, and any of its 8 realising orders (Lemma V.1(4)); order the weight-`≤ 3` checks
arbitrarily. For any `c ≠ c'`, linearity gives `β(x_c + x_{c'}) = 0 + 0 = 0`. Suppose
`x_c + x_{c'} ∈ Log = \{0, ℓ\}`. If `x_c + x_{c'} = ℓ` then `β(x_c + x_{c'}) = β(ℓ) = ℓ ≠ 0`, a
contradiction; so `x_c + x_{c'} = 0`, which is **not** in `Log \ {0}`. By Corollary V.2 no pair is
forbidden, so no mechanism of size `≤ 2` exists and `d_eff^X(M) ≥ 3`.

*Running time.* Computing `Log` and a splitting is `O(n^3)` once; each check needs `O(1)` evaluations
of `β` on three vectors, `O(n^2)` each. ∎

*Consistency check.* The `K₄` counterexample of `circdist_cplx_gadget_20260820.md` §5.3 (a NO
instance in this regime) has `k = 6`, consistent with Theorem V.4: `k ≥ 2` is genuinely necessary
for a weight-4 NO instance. (NUMERICAL, imported.)

**Theorem V.5 (bipartite matching, under a disjointness hypothesis) — CONJECTURED.** Assume the
promise of §6.1 **and**

```
    (D)   L_c ∩ L_{c'} = ∅  in  Q,  for all pairs of distinct weight-4 X-checks c ≠ c'
```

— equivalently: no 2-subset of one check's support agrees, modulo `S_X`, with a 2-subset of a
different check's support. Then the X-sector question is exactly a **system of distinct
representatives**: build the bipartite graph `B` with left vertices the weight-4 X-checks, right
vertices the cosets `ν(x)`, `x ∈ ⋃_c L_c`, and an edge `c — s` whenever some `x ∈ L_c` has
`ν(x) = s`. Then

```
    ∃ schedule with d_eff^X(M) ≥ 3   ⟺   B has a matching saturating every left vertex
                                     ⟺   Hall's condition: |N_B(S)| ≥ |S| for every set S of checks.
```

Decidable in time `O(|E(B)| √{|V(B)|}) = O(m^{1.5})` by Hopcroft–Karp, after `O(m n^2 + n^3)`
preprocessing to compute the values and the hypothesis (D).

*Proof.* Under (D), for `c ≠ c'` and any `x ∈ L_c`, `x' ∈ L_{c'}` we have `x ≠ x'`, so Corollary V.2
reduces to `forbidden(x,x') ⟺ ν(x) = ν(x')`. Hence a valid assignment is precisely a choice
`x_c ∈ L_c` with the `ν(x_c)` pairwise distinct, which is precisely a saturating matching in `B`
(from an assignment, take `c ↦ ν(x_c)`, injective; from a matching `c ↦ s_c`, pick any `x_c ∈ L_c`
with `ν(x_c) = s_c`). Hall's theorem gives the criterion. Hypothesis (D) is tested by comparing the
`≤ 3m` values pairwise in `Q`, i.e. by reducing `≤ 9m^2/2` differences against a reduced row-echelon
form of `H_X`. ∎

**Remark V.6 (Theorem V.5 explains the `K₄` obstruction).** The wired composite of
`circdist_cplx_gadget_20260820.md` §5.3 has four X-checks `c_0, c_1, c_5, c_6` with
`ν(L_{c_0}) = ν(L_{c_1}) = ν(L_{c_5}) = ν(L_{c_6})`, a set of exactly 3 cosets. Taking
`S = \{c_0,c_1,c_5,c_6\}` gives `|N_B(S)| = 3 < 4 = |S|`: **Hall's condition fails**, and that is the
whole reason the instance is a NO. So the gadget session's exhaustive verification is reproduced by
a one-line Hall argument — and, more usefully, the reason no reduction of that shape can be hard is
now sharper than "the `≠₃` edges form cliques": *even without transitivity*, list-all-different is in
P, so any reduction whose output satisfies (D) is a reduction to a polynomial problem.

### 6.5 **The gap**: "bipartite matching" is not the general answer

`circdist_cplx_gadget_20260820.md` §5.4 states, as one of four bullets, "*therefore the X-sector is a
**list all-different / bipartite matching problem**, decided in polynomial time by Hall's theorem
when `Log` is trivial on the relevant cosets*". Writing the argument out, the following became clear:

**Proposition V.7 (the target of the reduction is not a matching problem) — CONJECTURED.** Without
hypothesis (D), the problem of Theorem V.3(3) — choose a partial function `g : N ⇀ Log` hitting
every 3-element list — is, **as an abstract combinatorial problem, NP-complete**.

*Proof.* Membership in NP is clear (`g` restricted to the `≤ 3m` used points is a polynomial
certificate). Hardness: reduce 3-SAT. Given a 3-CNF `ψ` over Boolean variables `v_1,…,v_M` with
clauses `C_1,…,C_m`, take `N := F_2^M` with basis `(μ_1,…,μ_M)` and `Log := F_2 = \{0, ℓ\}`. Encode
the literal `v_j` as the pair `(μ_j, 0)` and `¬v_j` as `(μ_j, ℓ)`; encode clause `C_t` as the list
`L_t` of the three pairs of its literals. Then a partial function `g : N ⇀ Log` hitting every list
is exactly a partial truth assignment satisfying every clause, and conversely (extend arbitrarily).
∎

Proposition V.7 does **not** show that Island V is hard; it shows that Theorem V.3 lands in a class
whose *generic* member is hard, so the words "bipartite matching" cannot be attached to the general
case. Concretely, three things separate the island's instances from the encoding in the proof:

* **(S1)** `Σ_r β(x_c^{(r)}) = 0` — in the 3-SAT encoding above this forces each clause to contain an
  **even** number of negated literals, so the encoding as written produces only a restricted (and
  possibly tractable) fragment;
* **(S2)** `Σ_r m(x_c^{(r)}) = 0` — the three *variables* of a clause must have identifiers summing
  to zero, which is a strong global linear condition on the clause structure;
* **realisability** — the lists must come from an actual weight-`≤ 4` CSS code with `d_X ≥ 4`,
  `d_Z = 3`, and the gadget session's census shows this is restrictive.

**Status: OPEN.** Whether `Eff-Preserve≥^X[w ≤ 4, d_X ≥ 4]` is in P is *not settled by this
write-up*. What is settled: (i) the exact reduction (Theorem V.3); (ii) the `k ≤ 1` case
(Theorem V.4); (iii) the (D) case (Theorem V.5); (iv) that the *route* "it is a matching problem"
is not available in general (Proposition V.7). Solving the general case now means deciding whether
the side conditions (S1)+(S2)+realisability tame the hitting problem — a well-posed, small,
self-contained question, and a natural next work item.

**Repricing.** The gadget session priced R6 at `P 0.7 → 0.8` partly on the strength of the weight-4
island being a completed matching algorithm. On the evidence of §6.5 that component should be
re-priced: R6 still holds four completed islands (I, II, III, IV of this file), so its overall `P`
need not drop, but the *specific* claim "weight-4 regime ⇒ matching ⇒ P" must be downgraded from a
result to a **conditional result plus an open question**, and the node's third minimal-acceptance
branch should be certified on Islands I–IV, not on Island V. Cost to close the open question:
estimate **1–2 sessions** (it is a pure finite-CSP question with two linear side conditions; the
realisability half can be probed by the existing `gate3.py`-style search). Note also the mild
upside: if (S1)+(S2)+realisability *fail* to tame it, that is a route to NP-hardness at weight 4
that the gadget session had ruled out for the wrong reason.

### 6.6 Scope clause — what Island V does not cover

* **One sector only.** The hypotheses force `d_Z = 3`; the Z-sector is untouched and must be settled
  separately (Proposition 2.1). Island V alone never decides an Eff-Preserve instance.
* **`d = 3` and X-check weight `≤ 4` and `d_X ≥ 4`, all three.** Mixed-weight codes with weight-5+
  X-checks are excluded: at weight 5–6 the value of an order is a genuine *set* of prefix sums and
  the relation becomes set-disjointness, not equality of a single value
  (`circdist_cplx_gadget_20260820.md` §4.2).
* **Theorem V.5 needs (D), which is a real restriction.** (D) fails whenever two 2-subsets from
  different checks differ by a stabiliser — for instance when their union is the support of a third
  weight-4 X-check. Codes with many weight-4 X-checks are exactly the ones where this is likely.
* **Theorem V.4 is a YES theorem, not an algorithm for the general `k`.** It says nothing for
  `k ≥ 2`, and the `K₄` instance shows `k ≥ 2` really does admit NO instances.
* **The gap is a gap in this island only.** Nothing in §6.5 affects Islands I–IV.

---

## 7. Status, deltas, assumptions, limits

### 7.1 Per-island status

| # | island | statement | status | complexity delivered |
|---|---|---|---|---|
| I | factorising / decoupled instances | Theorem I, Cor. I.1–I.2 | **argument complete** | P for fixed `d`, bounded `w`; class is self-certifying |
| II | HGP codes | Thm II.1–II.4, Lem. II.5–II.6 | **argument complete**, and stronger than asked | constant YES; `O(1)` after the promise |
| III | bounded-treewidth Tanner graphs | `Φ_{t,w,d}` + Lem. III.1 + Thm III | **argument complete**, external theorem pinned with one residual (theorem *number* unverified) | FPT in `(t,w,d)`; linear in `n` |
| IV | `d = 3`, `≤ 2` orders per check | Lem. IV.1 + Thm IV, Cor. IV.2–IV.3 | **argument complete** | P, no bound on `w` needed |
| V | weight-`≤ 4` / `d_X ≥ 4` | Lem. V.0–V.1, Cor. V.2, Thm V.3–V.5, Prop. V.7 | **GAP FOUND** — see §6.5 | P if `k ≤ 1` (Thm V.4) or under (D) (Thm V.5); **general case open** |

Nothing above is PROVED. Every item is CONJECTURED in the protocol's sense: written out, internally
checked, **never independently reviewed**.

### 7.2 The gap, in one paragraph

`circdist_cplx_gadget_20260820.md` §5.4 concludes that the weight-4 / `d_X ≥ 4` regime "is a
list all-different / bipartite matching problem, decided in polynomial time by Hall's theorem".
The reduction underlying that sentence is correct and is made exact here (Theorem V.3): the CSP is
"choose a partial section `g : N ⇀ Log` of the quotient `Q → Q/Log` that hits every check's
3-element list". But **that is not a matching problem.** It becomes one exactly when different
checks never share a value in `Q` (hypothesis (D) of Theorem V.5), in which case "same coset" and
"conflict" coincide and the problem is a system of distinct representatives. Without (D) the
abstract problem is NP-complete (Proposition V.7, by a two-line reduction from 3-SAT), so the
polynomial claim needs either (D), or `k ≤ 1` (Theorem V.4), or a new argument using the two linear
side conditions (S1), (S2) that the code structure supplies. The general case is **open**. A useful
by-product: hypothesis (D) *does* hold for the `K₄` counterexample of gadget §5.3, and Theorem V.5
reduces that whole construction to a one-line Hall violation (Remark V.6), which is a cleaner and
more general reason than "the `≠₃` relation is an equivalence" for why local `≠₃` gadgets cannot
give hardness.

### 7.3 What is new relative to the two input documents

1. **Lemma 1.12 (prefix–suffix duality) is upgraded from syndrome space to `Q = F_2^n/S_X`.** The
   gadget document's Lemma A says `σ(S_i) = σ(P_i)`; the correct statement is
   `λ(S_i) = λ(P_i)`, an equality in `Q`, not merely modulo `Log`. With that upgrade the
   "stabiliser-coincidence proviso" stops being an exception bolted onto the criterion and becomes
   the *definition* of the criterion: work in `Q`, and "conflict" means "equal in `Q/Log`, unequal in
   `Q`" (§1.5). Every island below is stated in `Q`.
2. **A definition of "coupling" that does not quantify over schedules** (Definition 2.3, via
   Lemma 1.15's chain characterisation), and the observation that the decoupled class is
   **recognisable in polynomial time** for fixed `d` and bounded `w` (Corollary I.1) — so Island I is
   a promise-free polynomial class, not a conditional one.
3. **A proof of the HGP island** (Theorem II.1 + II.3), replacing ASSUMPTION A1 for the purposes of
   premise P6.2. The proof is short, uses only the product's line structure, and is *stronger* than
   needed: it holds when a single ancilla fault produces an arbitrary **subset** of a check's
   support, not merely a suffix (Remark II.7). It also produces the exact side condition under which
   "constant YES" is legitimate (Lemma II.5), which is the "scope check" the recon asked for.
4. **An explicit CMSO₂ sentence** `Φ_{t,w,d}` (§4.3) with the place where modular counting is
   genuinely required isolated (`InStab`, because data-qubit degree is unbounded), and the Courcelle
   citation pinned (§4.4), plus a V2 extension (Corollary III.1).
5. **Island IV extended**: no bound on check weight is needed, and a code-intrinsic variant
   (Corollary IV.2) exists alongside the extra-input one.
6. **Island V extended and corrected**: the hypothesis relaxes from "every X-check has weight exactly
   4" to "weight `≤ 4`" (Lemma V.1 shows weight-`≤ 3` checks are unconstrained); the `k ≤ 1` parity
   argument is written out in full and holds; and the matching claim is corrected (§6.5).

### 7.4 External results relied on, and their status

| tag | statement used | source | status this session |
|---|---|---|---|
| C1 | Courcelle's theorem, CMSO₂ form (§4.4) | Courcelle, *Inform. and Comput.* **85**(1) (1990) 12–75; Arnborg–Lagergren–Seese, *J. Algorithms* **12**(2) (1991) 308–340; Courcelle–Engelfriet, CUP 2012 (EMA 138) | bibliographic data confirmed via secondary sources; **primary texts not read; theorem numbers not verified** |
| C2 | tree decomposition computable in `2^{O(t^3)}n` | Bodlaender, *SIAM J. Comput.* **25**(6) (1996) 1305–1317; 5-approx: Bodlaender–Drange–Dregi–Fomin–Lokshtanov–Pilipczuk, *SIAM J. Comput.* **45**(2) (2016) 317–378 | standard, not re-verified |
| C3 | MSO model checking on trees has non-elementary parameter dependence | Frick–Grohe, *Ann. Pure Appl. Logic* **130**(1–3) (2004) 3–31 | bibliographic data confirmed via secondary source |
| C4 | 2-SAT in linear time | Aspvall–Plass–Tarjan, *IPL* **8**(3) (1979) 121–123; Even–Itai–Shamir, *SIAM J. Comput.* **5**(4) (1976) 691–703 | standard, not re-verified |
| C5 | Hall's theorem; Hopcroft–Karp `O(E√V)` | standard | not re-verified |
| C6 | 3-SAT is NP-complete (used only in Prop. V.7) | Cook/Karp; Garey–Johnson | standard, not re-verified |
| A1 | HGP distance robustness | Manes–Claes, *Quantum* **9**, 1618 (2025), arXiv:2308.15520 | **no longer needed** for the `d_eff` half (§3 proves it); still assumed for the optimality and higher-dimensional claims, which are not used here |
| A5 | computing (quantum) code distance is NP-hard | Vardy 1997; Kapshikar–Kundu arXiv:2203.04262 | not re-verified; used only to justify why every algorithm here targets `Eff-Preserve≥` rather than the promise |
| A11 | connectivity/separator trade-offs bounding `k`, `d` | Baspin–Krishna 2021–2022 | **not verified; exact form matters**; used only as the honest caveat in §4.6 |
| A7, A8, A12 | Latin-square completion; 3-edge-colouring; CSP dichotomy | Colbourn 1984; Holyer 1981; Bulatov/Zhuk 2017 | not used in any proof here; referenced only in scope clauses |

### 7.5 Honest limits of this session

* **Proposer-side only.** No independent adversarial review of any lemma. The three most
  review-worthy items are Theorem II.1 (the cleaning argument — Step 3 in particular),
  Lemma III.1 (the CMSO encoding's correctness), and Lemma V.1(3) (the claim that *only*
  middle–middle pairs can couple).
* **No new computation.** Every NUMERICAL statement quoted is imported from the recon or the gadget
  document and was not re-run. In particular the claim that HGP(rep₃,rep₃) and the 3×3 toric code
  have zero coupling is imported, and Theorem II.4 *predicts* it rather than checking it — an
  agreement worth noting but not an independent verification.
* **V1 throughout.** Islands I, II, IV, V are V1 statements and break under a depth bound (each scope
  clause says where). Only Island III extends to V2, via Corollary III.1.
* **`d_eff`, never `d_circ`.** Every result rests on Lemma 1.2, which fails for `d_circ`. Nothing
  here bears on Circ-Preserve except through Addendum A1 of the recon.
* **The `Σ_2^P` classification is untouched.** These are all fixed-`d` (or fixed-parameter)
  tractability results. The node's parts (a) and (b) are unaffected.
* **The Courcelle pin has a residual.** The statement is pinned and the sources are named, but no
  theorem number was verified against a primary text. This is a 15-minute action and should be
  carried as an open premise, not as a discharged assumption.
* **A9 (`Π_2`-completeness of the covering radius problem) was again not checked.** The recon flagged
  it, the gadget session did not do it, and this session did not either — it is not needed by any
  island, but it still gates route R4.

### 7.6 Recommended next actions

1. **Review, in this order:** Theorem II.1 → Lemma V.1(3) → Lemma III.1 → Theorem I. The first two
   are short and load-bearing; the third is long and mechanical; the fourth is nearly definitional.
2. **Close the Island V gap** (1–2 sessions): decide whether the side conditions (S1)+(S2), together
   with realisability by a weight-`≤ 4` CSS code with `d_X ≥ 4`, make the partial-section hitting
   problem of Theorem V.3(3) polynomial. Both outcomes are publishable: tractability completes the
   island, hardness is an NP-hardness route at check weight 4 that the gadget session's clique
   obstruction had (for a different reason) closed off.
3. **Do the 15-minute primary-source checks** that are now twice-deferred: the Courcelle theorem
   number (§4.4) and A9.
4. **Certify the node's third minimal-acceptance branch on Islands I–IV**, not on Island V.
5. **Do not** start R1's full construction, R3 or R4 on the strength of this file; nothing here
   changes the gate verdict of `circdist_cplx_gadget_20260820.md` §7.

---

*Session scope note.* Everything above is proposer-side. The only file written by this session is
this one. No node file, route, assessment, or proof-DAG object was created or modified. No result in
this document has had independent adversarial review, and none is labelled PROVED.

