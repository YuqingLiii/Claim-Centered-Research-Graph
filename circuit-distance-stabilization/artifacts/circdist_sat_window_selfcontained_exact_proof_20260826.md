# `CIRCDIST.sat.window`: self-contained exact proof and statement audit

**Date:** 2026-08-26  
**Role:** author/proposer, one strict-serial worker session, no sub-agents  
**Canonical target:** `CIRCDIST.sat.window`  
**Current exact claim hash checked:** `sha256:8698b051b15fa14ff669299580d9b7bfec01808c0a34133ef09264e749466146`  
**Repository action taken by this worker:** this artifact only; no canonical node, review, scheduler, protocol, generated view, prior artifact, tool, source package, or migration record was edited.

This document gives a complete mathematical argument for the intended current theorem. It also distinguishes that mathematical result from two separate record questions:

1. the current 489-character node claim is shorthand for several load-bearing conventions that do not appear in its own text; and
2. this document is authored evidence, not an independent completion review, so it cannot award `PROVED` or `CERTIFIED*` under the Proof-DAG protocol.

The productive settlement is therefore:

- **mathematics:** every substantive clause is proved below under the current named model;
- **exact standalone wording:** **NEEDS REPAIR**, not because a mathematical clause is false, but because the current sentence does not itself pin verbatim repetition, measurement consistency, min-over-sectors aggregation, the Definition-3.5/section-8.1 detector split, or the uniform full-Pauli location weight;
- **repository evidence level:** unchanged; a fresh independent adversarial review must check this artifact and any exact claim serialization before the dispatcher may alter a level.

No external eventual-periodicity theorem, composition theorem, finite-state pumping theorem, or numerical search is load-bearing.

---

## 0. Exact target, normalization, and verdict

The YAML-loaded current claim is exactly:

> For every fixed legal single-round single-ancilla CSS schedule M under ideal initialization and final data readout, the repeated-round distances satisfy d_(R+1)(M) <= d_R(M), the limit d_infinity(M) exists, every minimum-weight undetectable logical has a representative supported on contiguous rounds of span at most its weight, and therefore R_stab(M) <= d_infinity(M) <= d and d_R(M) = d_d(M) = d_infinity(M) for all R >= d; hence the first d distances decide both d_infinity and R_stab.

The repository normalization is

```text
"sha256:" + SHA256(UTF-8(claim.replace("\r\n","\n").strip()))
```

and gives

```text
sha256:8698b051b15fa14ff669299580d9b7bfec01808c0a34133ef09264e749466146.
```

### 0.1 Clause-by-clause mathematical verdict

| Clause | Verdict under Definitions 1.1-1.13 below | Load-bearing lemma |
|---|---|---|
| `d_(R+1)(M) <= d_R(M)` | **PROVED-AS-A-MATHEMATICAL-ARGUMENT** | explicit append map, Theorem 5.1 |
| `d_infinity(M)` exists | **PROVED-AS-A-MATHEMATICAL-ARGUMENT** | positive integer bound plus monotonicity, Theorem 6.1 |
| every minimum logical has a contiguous representative of span at most its weight | **PROVED-AS-A-MATHEMATICAL-ARGUMENT** | sector projection plus gap split, Theorem 7.1 |
| `R_stab <= d_infinity <= d` | **PROVED-AS-A-MATHEMATICAL-ARGUMENT** | aggregate ceiling, translation, minimal stabilization index, Theorem 9.2 |
| `d_R=d_d=d_infinity` for every `R>=d` | **PROVED-AS-A-MATHEMATICAL-ARGUMENT** | aggregate attaining-sector argument, Theorem 9.1 |
| first `d` values decide both quantities | **PROVED-AS-A-MATHEMATICAL-ARGUMENT** | Corollary 9.3 |

### 0.2 Overall exact-text verdict

The current sentence is mathematically correct **when its terms are expanded by the current root/transfer model**. As a standalone node claim, however, it is **NEEDS REPAIR** because different reasonable readings of its omitted conventions change either the proposition's domain or its truth value. Section 12 supplies an exact replacement and normalized hash. This is a precision repair, not a counterexample to the intended theorem.

---

## 1. Frozen definitions

All vector spaces and sums below are over `F_2`. Paulis are taken modulo global phase.

### 1.1 CSS code and the meaning of `d`

A CSS code is specified by finite, possibly redundant, generating sets:

- `A`, the X-check generators, with matrix `H_X`;
- `B`, the Z-check generators, with matrix `H_Z`;
- `H_X H_Z^T=0`.

Set

```text
S_X = rowspace(H_X),                    S_Z = rowspace(H_Z),
d_X = min{|v| : v in ker(H_Z) \ S_X},
d_Z = min{|v| : v in ker(H_X) \ S_Z},
d   = min(d_X,d_Z).
```

Here `d` is the **CSS code distance**, the minimum of the two spatial sector distances. It is not a per-sector upper bound. We assume `k>=1`, so both logical quotients are nonzero and the displayed minima are finite. Fix dual logical bases `X_L^(1),...,X_L^(k)` and `Z_L^(1),...,Z_L^(k)`. A vector in `ker(H_Z)` is outside `S_X` exactly when it pairs oddly with at least one `Z_L^(j)`; the mirror statement holds for `ker(H_X)/S_Z`.

The last assertion follows from the CSS dimension identity

```text
dim ker(H_Z) - dim S_X = n-rank(H_Z)-rank(H_X)=k
```

and the nondegenerate symplectic pairing between the two logical quotients. No independence of the listed check generators is assumed.

### 1.2 One round and legality

Each generator owns one ancilla in each round.

- For `a in A`, prepare `anc(a)` in `|+>`, apply exactly one `CNOT(anc(a) -> q)` for every `q in supp(a)`, then measure the ancilla in X.
- For `b in B`, prepare `anc(b)` in `|0>`, apply exactly one `CNOT(q -> anc(b))` for every `q in supp(b)`, then measure the ancilla in Z.
- There are no flag ancillas, cat states, repeated incidences, or changes of generating set.

A single-round schedule `M` assigns every CNOT a layer in `{0,...,T-1}`, `T>=1`. **Conflict legality** means that a physical qubit is in at most one two-qubit gate per layer.

For the standard per-check records also to be deterministic, the schedule must satisfy **measurement consistency**:

```text
c_ab = #{q in supp(a) intersect supp(b) : t(q->b) < t(a->q)} mod 2 = 0
```

for every `(a,b)`. In this proof, **legal** means conflict-legal **and** measurement-consistent. This is the only domain on which the named standard detector model is defined. If the current node intends “legal” to mean conflict legality alone, the claim is under-specified: a schedule with `c_ab=1` has a nondeterministic advertised check parity even without faults.

The mirror ordering count is

```text
c'_ab = #{q in supp(a) intersect supp(b) : t(a->q) < t(q->b)} mod 2.
```

Conflict legality makes the two inequalities complementary on each common qubit, and CSS commutation makes the total overlap even. Therefore

```text
c_ab + c'_ab = |supp(a) intersect supp(b)| = 0 mod 2,
```

so `c'_ab=c_ab`. Measurement consistency is therefore mirror-stable; the same schedule class serves both memory sectors.

### 1.3 Verbatim repetition and temporal boundaries

`C_R^Z(M)` is the Z-memory experiment:

1. initialize every data qubit ideally in `|0>`;
2. execute `R` **verbatim copies** of the fixed `T`-layer block `M`;
3. read every data qubit ideally in Z.

Rounds are indexed `0,...,R-1`. Each round has fresh ancillas, and its named fault locations are disjoint from every other round's locations. The bijection between the locations of two rounds preserves the one-round fault effect defined in Section 3. Within-round idle layers may be fixed or compressed before `M` is frozen. No layer is merged across a round boundary, and the layout does not depend on `R`.

`C_R^X(M)` is the mirror: ideal `|+>` data initialization, the same physical schedule with the CSS roles exchanged, and ideal X readout.

For Z-memory let `m_(b,r)` be the Z-check record in round `r`, and let `rho_q` be the terminal Z-readout bit. Define virtual boundary records

```text
m_(b,-1) = 0,
m_(b,R)  = sum_{q in supp(b)} rho_q.
```

The full-boundary difference detectors are

```text
D_(b,r) = m_(b,r)+m_(b,r-1),       b in B, r=0,...,R.
```

Thus `D_(b,0)` is absolute and `D_(b,R)` uses the ideal data readout. The conventional opposite-family differences are

```text
D_(a,r) = m_(a,r)+m_(a,r-1),       a in A, r=1,...,R-1.
```

The missing `r=0` opposite-family differences reflect individually random X-check outcomes in Z-memory. The X-memory formulas are the mirror, with the full interval on `A`.

### 1.4 Fault locations, configurations, collisions, and weight

Each named operation or idle slot is a location. The allowed assignment group at a location, with identity adjoined, is:

- after a CNOT: the 16 two-qubit Paulis modulo phase;
- an allowed one-qubit idle or post-preparation slot: the 4 one-qubit Paulis modulo phase;
- a recorded ancilla outcome: the two-element classical flip group.

A **fault configuration** assigns one group element to every location. Its weight is the number of locations assigned a nonidentity element. Initialization and final data readout are ideal and have no locations. All nonidentity assignments cost one, independent of Pauli type.

An elementary-fault multiset is an alternative syntax that permits several listed faults at the same named location. It gives the same minimum:

**Collision lemma.** At one location, replace two assignments by their Pauli product (or XOR for a classical flip). Clifford propagation and record/observable effects are linear over `F_2`, so the total effect is unchanged. Full group closure makes the product available. The count drops by one if the product is nonidentity and by two if it is identity. Repeating removes every collision. Hence

```text
minimum elementary-fault multiset count = minimum occupied-location count.
```

In particular, a minimum multiset cannot contain a same-location collision: merging it would produce a strictly lighter witness. Locations in distinct rounds never collide, so weight is additive across a split by rounds.

This lemma fails for a non-group fault menu or nonuniform costs. Those models are outside the theorem.

### 1.5 Canonical detector/observable split

The proof uses the current root convention, not arbitrary “detector-convention independence.”

For Z-memory, let `V` be the vector space of deterministic parities of all ancilla records and terminal data-readout bits in the fault-free circuit. Consider the family of otherwise identical experiments whose prepared logical basis label is varied. The **canonical detector space** `D_can^Z` is the kernel of logical-label dependence: a parity is a detector exactly when its fault-free value is the same for every logical basis label. Terminal logical readout parities supply the observable quotient. This is Definition 3.5 of the transfer dossier.

For X-memory use the direct section-8.1 mirror. Definition 3.5's status as the project-intended split is a lead-ratified model decision, not a mathematical theorem. Once that split is fixed, its algebraic consequences are proved in Section 2.

The designated Z-memory observables are

```text
lambda_j = sum_{q in supp(Z_L^(j))} rho_q,     j=1,...,k,
```

and the X-memory observables are their mirror.

### 1.6 Undetectable logicals and representatives

A configuration in one memory sector is **undetectable** when it flips no element of the corresponding canonical detector space. It is **logical** when its observable-flip vector in `F_2^k` is nonzero.

A **representative** of a minimum witness means a configuration in the same memory experiment which:

1. remains canonical-detector-undetectable;
2. has a nonzero logical flip in that same sector;
3. has the same minimum weight.

It need not reproduce irrelevant opposite-Pauli record flips. The representative constructed below is the sector projection of the original witness.

### 1.7 Distances, aggregation, limit, and stabilization

For `sigma in {Z,X}` define

```text
d_R^sigma(M) = min{|F| : F is an undetectable logical in C_R^sigma(M)},
d_R(M)       = min(d_R^Z(M),d_R^X(M)).
```

This min-over-memory-sectors aggregation is load-bearing. Define, once existence is proved,

```text
d_infinity(M) = lim_{R->infinity} d_R(M),
R_stab(M) = min{R_0>=1 : d_R(M)=d_infinity(M) for every R>=R_0}.
```

### 1.8 Round support and span

For a configuration `F`,

```text
supp_t(F) = {r : some nonidentity location of round r is occupied}.
```

If `F` is logical then this set is nonempty. Its span is

```text
span(F) = max supp_t(F) - min supp_t(F) + 1.
```

“Contiguous rounds” means `supp_t(F)` is the entire integer interval between its minimum and maximum.

---

## 2. Exact reconciliation of recon, window, lift, and transfer conventions

The four dossiers use the same two-boundary algebra with different symbols and, in the recon, a one-based round index.

| Object | recon | window/lift | transfer/current proof |
|---|---|---|---|
| residual data error created in a round | `Delta` | `E(f)` and sums thereof | `e_r` below |
| residual syndrome | `H_Z Delta` | `s(f)` | `s_r=H_Z e_r` |
| extra same-round record flip | `mu` | `u(f)` | `U_r` |
| incoming accumulated residual | `E_(r-1)` | prefix sum `c(r-1)` | `C_(r-1)` |
| measured-record error | `o_r=H_Z E_(r-1)+mu_r` | `c(r-1)+U(r)` | `y_r=C_(r-1)+U_r` |
| undetectability | `mu_r=H_ZE_(r-1)` plus terminal closure | `(W)` / `(LIFT')` | equation `(W)` below |
| full-boundary detector column | implicit two slices | `[u]_r+[u+s]_(r+1)` | same |
| weight in older window text | elementary-fault count | multiset count | occupied locations, equal by collision lemma |
| detector set used for direct recursion | short Definition-2.7 set | full `D_b` plus partial `D_a` | same direct set, bridged to canonical Definition 3.5 |
| sector aggregation | initially a caveat | min over mirrors | min over mirrors |

Index translation: recon rounds `1,...,R` correspond to rounds `0,...,R-1` here; its final detector `R+1` corresponds to boundary index `R` here.

Three distinctions matter.

1. **Detector sets are not being identified.** With dependent generators, the Definition-2.7 set omits deterministic round-zero redundancy parities. Only the **distance values** for the named Definition-2.7 and Definition-3.5 choices are equal, by the projection proof below.
2. **No arbitrary split invariance is used.** On Steane plus a redundant X row, the recorded alternative

   ```text
   D' = span{D_(b,r)} + span{D_(a,r)} + span{P_X+lambda}
   ```

   has `d^(2.7)=2` but `d^(D')=3` at `R=2` and `4` at `R=3`. The canonical value remains `2`. The safe named bridge is Definition 2.7 versus Definition 3.5 only.
3. **The code-distance ceiling is aggregate.** Per-sector one has `d_R^Z<=d_X` and `d_R^X<=d_Z`. The statement `d_R^sigma<=d=min(d_X,d_Z)` is false on asymmetric CSS codes. The proof of the current node uses only

   ```text
   d_R=min(d_R^Z,d_R^X) <= min(d_X,d_Z)=d.
   ```

---

## 3. One-round algebra and the exact boundary equation

The rest of the proof is given for Z-memory. Every statement has an X-memory mirror by Section 1.2.

### 3.1 Sector projection

For a full-Pauli configuration `F`, define `Pi_X F` location by location:

- retain the X component of every Pauli assignment;
- retain classical flips of Z-check records;
- delete Z components and flips of X-check records.

The full Pauli group makes every retained nonidentity component an allowed assignment. Therefore

```text
|Pi_X F| <= |F|.
```

CNOT propagation is type-preserving:

```text
X_c -> X_c X_t,    X_t -> X_t,
Z_c -> Z_c,        Z_t -> Z_c Z_t.
```

Consequently `Pi_X` preserves every Z-check record flip and every terminal Z-readout flip, hence all Z-memory logical observables. It flips no X-check record at all. The mirror projection `Pi_Z` has the analogous properties in X-memory.

### 3.2 Round transparency

An X error on a data qubit is:

- a target error in each `a->q` CNOT, so it remains on the target and does not flow to the X ancilla;
- a control error in each `q->b` CNOT, so it remains on data and contributes X to `anc(b)`.

Thus an incoming data-X vector `E` is unchanged by a fault-free round and flips that round's Z-check records by exactly `H_Z E`. Fresh ancillas erase all other inter-round frame data.

### 3.3 One-round fault data

For a sector-pure assignment `f` inside a fixed round define:

```text
E(f)       in F_2^n       residual data-X vector at the end of that round,
s(f)       = H_Z E(f)     residual Z-check syndrome,
u(f)       in F_2^B       extra flip of that same round's Z-check records,
ell(f)     in F_2^k       pairing of E(f) with the Z logical observables.
```

Verbatim repetition makes these data independent of the round index. For a round configuration `F_r`, sum the elementary data:

```text
e_r = sum_{f in F_r} E(f),
s_r = H_Z e_r,
U_r = sum_{f in F_r} u(f),
ell_r = sum_{f in F_r} ell(f).
```

The sums remain valid for one nonidentity Pauli assignment per location because propagation is linear.

### 3.4 Two-slice detector locality

A fault `f` in round `r` flips its own record by `u(f)`. In every later real round the persistent residual flips the record by `s(f)`, and the ideal final readout parity is also flipped by `s(f)`. Therefore all cancellations after the next boundary are pairwise, and the detector effect is exactly

```text
partial(f,r) = [u(f)]_r + [u(f)+s(f)]_(r+1).
```

This formula includes `r=0` because `m_(b,-1)=0`, and includes a fault in the last round because boundary `R` is a genuine ideal-readout detector coordinate.

### 3.5 Prefix form `(W)`

For a multi-round sector-pure configuration put

```text
C_t = sum_{i=0}^t s_i,          C_t=0 for t<0,
U_t = the round-t value above,  U_R=0.
```

The error in the real round-`t` Z-check record is

```text
y_t = C_(t-1)+U_t,              0<=t<=R-1,
```

and the virtual terminal record error is

```text
y_R = C_(R-1).
```

Set `y_(-1)=0`. The detector at boundary `t` flips by `y_t+y_(t-1)`. Vanishing of every full-boundary difference detector is therefore equivalent to the sequence `y_(-1),y_0,...,y_R` being constant. The initial value fixes that constant to zero. Hence:

> **Boundary equation `(W)`.** A sector-pure configuration is undetectable against all full-boundary Z-check differences if and only if
>
> ```text
> U_t = C_(t-1)        for t=0,...,R,
> ```
>
> where `U_R=0`. In particular, the terminal instance forces `C_(R-1)=0`.

Extending `U_t=0` outside the occupied circuit and using terminal closure extends `(W)` to every integer `t`. This all-integer form is what makes translation transparent.

### 3.6 Logical parity

Round transparency makes the terminal residual

```text
E_tot(F) = sum_{r=0}^{R-1} e_r.
```

The logical flip is

```text
ell(F)=sum_r ell_r.
```

It depends only on `E_tot`, not on the round assignment. A configuration is logical exactly when this vector is nonzero.

---

## 4. The named detector-convention bridge, re-derived

This section proves exactly the bridge needed by the current root convention.

### 4.1 Canonical detector decomposition

Write a Z-type record/readout parity as `(beta,gamma)`, where `beta` gives coefficients of the Z-check records and `gamma in F_2^n` gives coefficients of final readout bits. Back-propagation through the CNOT circuit gives:

- measurement consistency cancels the intra-round cross terms;
- CSS commutation cancels inter-round cross terms;
- the parity is deterministic exactly when `H_X gamma=0`; `beta` is arbitrary.

Thus

```text
V_Z = {(beta,gamma) : gamma in ker(H_X)}.
```

Varying the prepared logical basis label changes the value only by the pairing of `gamma` with the logical-X basis. Therefore logical-label independence is equivalent to `gamma in S_Z`, and

```text
D_can,Z = {(beta,gamma) : gamma in S_Z}.
```

Now consider the full-boundary differences `D_(b,r)`.

- For `r=0,...,R-1`, they are triangular differences of the `m_(b,r)` records and span every `beta` with `gamma=0`.
- The terminal `D_(b,R)` supplies `gamma=chi_supp(b)`. After subtracting already available record terms, these span every `gamma in S_Z`.

Therefore

```text
D_can,Z = span{D_(b,r) : b in B, r=0,...,R}.       (exact equality)
```

The X-record deterministic parities form another summand `D_can,X`. Every such parity is invariant under varying the Z-memory logical input. If `H_X` has dependent rows, this summand contains round-zero redundancy parities not spanned by the conventional `D_(a,r)`, `1<=r<=R-1`.

Hence

```text
D_can^Z = D_can,Z direct-sum D_can,X,
Definition-2.7 detector span is a subspace of D_can^Z,
```

and the inclusion can be strict.

### 4.2 Equality of the two named distance values

Let `d_short^Z` be the distance using the Definition-2.7 set and `d_can^Z` the canonical value.

Because the short set is contained in the canonical space,

```text
d_short^Z <= d_can^Z.
```

Conversely, let `F` attain `d_short^Z` and set `F'=Pi_X F`.

- `F'` preserves all Z-check difference effects and the logical observable, so it annihilates `D_can,Z`, which those differences span, and remains logical.
- `F'` flips no X-check record parity, so it annihilates the whole `D_can,X`, including every omitted redundancy direction.
- `|F'|<=|F|`.

Thus `F'` is a canonical-undetectable logical of no greater weight, giving

```text
d_can^Z <= d_short^Z.
```

The values are equal. The mirror proof gives equality in X-memory.

### 4.3 Same-weight representative for every canonical minimum

If `F` is a canonical minimum, `Pi_X F` is again canonical-undetectable and logical with weight at most `|F|`. Minimality forces equality. Therefore **every canonical minimum has a same-weight sector-pure representative**. This witness-level statement, not merely equality of numerical minima, is the bridge used in the contiguity and padding proofs.

Nothing here applies to an arbitrary complement of the observables in `V`. In particular it does not apply to the recorded `D'` counterexample of Section 2.

---

## 5. Monotonicity with explicit witness maps

### Theorem 5.1

For each sector and every `R>=1`,

```text
d_(R+1)^sigma(M) <= d_R^sigma(M).
```

Consequently `d_(R+1)(M)<=d_R(M)`.

### Proof in Z-memory

Let `F` be a canonical minimum in `C_R^Z`. Replace it by the same-weight sector-pure representative of Section 4.3. Define the append map

```text
iota_R(F) = the same assignments at the same named locations of rounds 0,...,R-1
```

inside `C_(R+1)^Z`; every location of the new round `R` is identity.

Verbatim repetition makes the map well-defined and preserves `(e_r,s_r,U_r,ell_r)` and weight. We verify `(W)` over the enlarged boundary range `0,...,R+1`.

1. **Initial boundary `t=0`.** It is unchanged. The old and new circuits both have the absolute detector `D_(b,0)=m_(b,0)`, and `U_0=C_(-1)=0` remains true.
2. **Old interior indices `1<=t<=R-1`.** The prefix data are identical, so the old equations transfer verbatim.
3. **Old terminal/new interior index `t=R`.** In `C_R`, this was the virtual readout equation `U_R=0=C_(R-1)`. In `C_(R+1)`, it is the measurement record of the new fault-free round. Round transparency says its error is exactly `C_(R-1)`, the same value the old ideal readout saw. The old terminal equation makes it zero.
4. **New terminal index `t=R+1`.** The added round has no new residual, so `C_R=C_(R-1)=0`; also `U_(R+1)=0`. Hence the new ideal-readout detector closes.

The terminal residual and therefore `ell(F)` are unchanged, so the image remains logical. Section 4.1 upgrades the verified full-boundary Z-check equations, together with sector purity, to canonical undetectability. Thus

```text
d_(R+1)^Z <= |iota_R(F)|=|F|=d_R^Z.
```

### Left-end attack: prepending

Define instead `tau(F)` by shifting every assignment from round `r` to round `r+1` and leaving the new round `0` fault-free.

- At the new initial boundary, `U'_0=C'_(-1)=0`.
- For `t=1,...,R+1`, `U'_t=U_(t-1)` and `C'_(t-1)=C_(t-2)`, so every equation is the old equation shifted by one.
- The new terminal equation is exactly the shifted old terminal equation.

Thus prepending also works. This is not needed for the inequality but is needed for unrestricted time translation.

### X-memory and aggregation

The mirror projection and mirror boundary equation give the same result in X-memory. Finally,

```text
d_(R+1)=min_sigma d_(R+1)^sigma
        <=min_sigma d_R^sigma
        =d_R.
```

This completes the proof. Notice that “more rounds give more locations” alone would not be a proof: appending a round also changes the old terminal readout parity into a real round record and changes the canonical parity space. The four boundary checks above are the missing map.

---

## 6. Finite positive bounds and existence of the limit

### Lemma 6.1: spatial terminal witnesses

For every data qubit `q`, choose its last two-qubit gate in a round. Immediately after that gate, assign the allowed one- or two-qubit Pauli whose only nontrivial component is X on `q`. If `q` participates in no gate, choose an idle X location. Call the assignment `f_q`.

No later `q->b` gate exists, so

```text
E(f_q)=e_q,       u(f_q)=0.
```

Let `v in ker(H_Z)\S_X` have weight `d_X`. Put all `f_q`, `q in supp(v)`, in the last round. Before that round, `C=0`; within it `U=0`; after it the terminal syndrome is `H_Zv=0`. Equation `(W)` holds, and `v` flips a Z-memory logical observable. Hence

```text
d_R^Z<=d_X.
```

The mirror gives `d_R^X<=d_Z`. Therefore

```text
1 <= d_R=min(d_R^Z,d_R^X) <= min(d_X,d_Z)=d.       (ceiling)
```

The lower bound holds because the empty configuration has zero observable effect. The construction also shows the minimization set is nonempty. Since each finite circuit has finitely many locations and finite assignment groups, a minimum is attained.

### Theorem 6.2: limit existence

By Theorem 5.1, `(d_R)` is nonincreasing. By the ceiling it takes values in the finite integer set `{1,...,d}`. Every strict decrease lowers the value by at least one, so there can be at most `d-1` strict decreases. The sequence is therefore eventually constant. Its eventual value is its global minimum, and

```text
d_infinity(M)=lim_R d_R(M)=min_{R>=1} d_R(M)
```

exists with `1<=d_infinity<=d`.

No finite-state eventual-periodicity theorem is used.

---

## 7. Contiguous minimum representatives

### Theorem 7.1

Fix `R` and a memory sector. Every canonical minimum-weight undetectable logical has a same-weight sector-pure representative whose round support is a contiguous interval and whose span is at most its occupied-location weight.

### Proof in Z-memory

Start from an arbitrary canonical minimum `F`. Apply `Pi_X`; Section 4.3 gives a canonical minimum representative `G` with

```text
|G|=|F|=d_R^Z.
```

By the collision lemma, `G` has at most one assignment per named location.

Assume its temporal support has an internal gap. Choose an integer `g` such that

```text
min supp_t(G) < g < max supp_t(G),       g notin supp_t(G).
```

Split by rounds:

```text
G_L = assignments in rounds <g,
G_R = assignments in rounds >g.
```

Both parts are nonempty, and their location sets are disjoint. The gap gives `U_g=0`; equation `(W)` for `G` at `g` gives

```text
C_(g-1)=0.                                      (gap closure)
```

#### The left part is independently undetectable

- For `t<=g`, the right part has contributed neither an in-round flip nor a prior residual, so the left equations equal the full equations.
- For `t>g`, the left part has no in-round flips, and its cumulative syndrome remains the gap value `C_(g-1)=0`.

Thus `G_L` satisfies `(W)` at every boundary, including the original initial and terminal boundaries.

#### The right part is independently undetectable

- For `t<=g`, it has neither current faults nor earlier residual, so both sides of `(W)` are zero.
- For `t>g`, its current flips equal those of `G`. Its accumulated syndrome equals that of `G` because the entire left contribution has closed to zero at the gap.

Thus `G_R` also satisfies `(W)` at every boundary.

Both parts are sector-pure, so Section 4.1 makes them canonical-undetectable, including every redundancy detector omitted by the short set.

Logical parity is additive:

```text
ell(G)=ell(G_L)+ell(G_R) != 0.
```

Therefore at least one part is logical. That part is strictly lighter than `G`, because the other part is nonempty and weights add across disjoint round-location sets. This contradicts minimality. Hence `supp_t(G)` is contiguous.

Every round in its span contains at least one occupied location, so

```text
span(G)=|supp_t(G)| <= |G|.
```

The X-memory proof is the mirror.

### What the proof does and does not delete

- It does not concatenate across a nonzero boundary charge. At a gap, `(W)` first proves exact zero charge.
- It does not assume a zero-fault round has no detector effect; it uses `U_g=0` together with the detector equation to infer closure.
- It discards one independently closed half only after observable additivity proves that a half is logical.
- It preserves input and output logical parity because each selected half is checked against the original absolute initial detector and original terminal closure.
- It proves a representative statement for an arbitrary full-Pauli minimum. If the starting witness is already sector-pure, it proves that witness itself is contiguous.

---

## 8. Exact time translation and deletion of exterior zero-fault rounds

### Lemma 8.1

Let a sector-pure canonical-undetectable logical `F` be supported in rounds `[a,b]`, with `w=b-a+1`. For every `R'>=w` and every shift `delta` placing `[a+delta,b+delta]` inside `{0,...,R'-1}`, the translated assignments form a canonical-undetectable logical of the same weight in `C_(R')`.

### Proof

Use the all-integer form of `(W)`. Translation gives

```text
U'_t = U_(t-delta),
C'_t = C_(t-delta).
```

Before the translated support both vanish because there are no earlier faults. After it, `C'` vanishes because the original terminal equation forced total syndrome zero. Thus every translated equation is an original equation with its index shifted. The interval condition guarantees that the two possibly nonzero detector slices lie inside boundary coordinates `0,...,R'`.

The translated locations exist with the same one-round effects by verbatim repetition. Weight is unchanged, and the terminal residual sum, hence logical parity, is unchanged. Sector purity again supplies canonical undetectability.

Taking `delta=-a` deletes all leading and trailing zero-fault rounds and produces the same-weight witness in `C_w`. This is the only shortening operation needed later.

---

## 9. Exact finite window and stabilization index

### Theorem 9.1: constancy from the aggregate code distance

For every `R>=d`,

```text
d_R(M)=d_d(M)=d_infinity(M).
```

### Proof

Fix `R>=d`. Monotonicity gives

```text
d_R<=d_d.
```

Choose a sector attaining the aggregate minimum at this particular `R`, and choose a canonical minimum witness in that sector. Theorem 7.1 supplies a same-weight contiguous representative `F` with

```text
span(F) <= |F| = d_R <= d.
```

The last inequality is the **aggregate** ceiling of Lemma 6.1. No claim that the nonattaining sector is bounded by `d` occurs here.

Translate `F` into a `d`-round circuit using Lemma 8.1. It remains a canonical-undetectable logical of weight `d_R`, so

```text
d_d<=d_R.
```

Equality follows. Thus the sequence is constant for every `R>=d`, and its eventual value is `d_d`.

### Theorem 9.2: the sharp stabilization bound

Let `S=R_stab`. Theorem 9.1 makes `S` well-defined and gives `S<=d`. Choose an attaining-sector minimum at `R=S`, and replace it by the contiguous representative `F` of Theorem 7.1. Write `w=span(F)`. Then

```text
w <= |F| = d_S = d_infinity.
```

If `w<S`, Lemma 8.1 translates `F` into `C_w`, giving `d_w<=d_infinity`. Since `d_infinity` is the global minimum, equality holds. Monotonicity then forces `d_R=d_infinity` for every `R>=w`, contradicting minimality of `S`. Hence `S<=w`. But `F` lies in an `S`-round circuit, so `w<=S`; in fact `w=S`. Therefore

```text
R_stab=S=w<=d_infinity<=d.
```

### Corollary 9.3: decision from the first `d` values

Theorem 9.1 gives

```text
d_infinity=d_d,
R_stab=min{R in {1,...,d} : d_R=d_d}.
```

Monotonicity ensures that once equality with `d_d` occurs, every later value equals it. Thus the list `d_1,...,d_d` decides both quantities, with no computation at `R>d`.

### Index audit

- Physical rounds of `C_R` are `0,...,R-1`.
- Detector boundaries are `0,...,R`.
- Appending a round adds physical round `R` and detector boundary `R+1`.
- A span of `w` rounds fits in `C_w` because its shifted physical support is `0,...,w-1`, and the closing detector is boundary `w`.
- The fixed window uses the code distance `d=min(d_X,d_Z)` only after choosing an **aggregate-attaining** witness of weight `d_R<=d`.

---

## 10. Alternative routes and adversarial attacks

### 10.1 Route comparison

#### Route A: direct boundary equation — selected

Derive `(W)`, project to a sector-pure canonical representative, split at an empty round, and translate. This route exposes every temporal boundary, proves the exact `d` window, and needs no external theorem.

#### Route B: min-plus eventual periodicity — rejected as the proof of this claim

The finite transfer system is useful for computation, but a general eventual-periodicity theorem yields at most eventual periodicity after its hypotheses and reducible-state issues are checked. It does not by itself prove:

- the monotonic direction;
- period one rather than a longer period;
- the explicit bound `R_stab<=d_infinity`;
- the exact prefix cutoff `d`;
- witness contiguity.

One can recover those facts by analyzing zero-cost loops and boundary states, but that analysis reproduces `(W)` and the split argument. It would also import the transfer node's un-rederived BCOQ theorem unnecessarily.

#### Route C: generic repeated-state pumping — rejected

Deleting an arbitrary fault-free interval after seeing a repeated finite state is unsafe unless the state records the absolute boundary charge and logical parity. A zero-fault round with nonzero incoming syndrome still produces record flips. The direct route deletes only exterior zero-fault rounds, or splits at an internal gap **after** `(W)` proves the charge there is zero. Generic pumping also gives a state-size-dependent window rather than the sharp `d` bound.

#### Route D: “more locations” — rejected

The circuit at `R+1` does not merely contain the circuit at `R`: the old terminal readout parity becomes a real round record, a new terminal parity appears, and the canonical deterministic-parity space changes. The explicit append map in Theorem 5.1 is required.

### 10.2 Small exhaustive boundary-equation stress test

As corroboration only, an inline Python 3.9 program enumerated every dictionary of one through four distinct nonzero abstract effects

```text
(s,u,ell) in F_2^3 \ {(0,0,0)}
```

for one syndrome bit and one logical bit, every configuration through four rounds, and all minimum supports. It checked monotonicity and the contiguity/span conclusion directly from `(W)`.

Successful output:

```text
dictionaries_tested 98
finite_R_cases 328
contiguity_or_monotonicity_violations 0
d2_less_than_d1_examples 2
(((0, 1, 0), (1, 0, 0), (1, 1, 1)), (3, 2, 2, 2))
(((0, 1, 0), (1, 0, 1), (1, 1, 0)), (3, 2, 2, 2))
```

The first decreasing example is transparent. Let

```text
A=(s,u,ell)=(0,1,0),
B=(1,0,0),
C=(1,1,1).
```

In one round, `A+B+C` is the unique weight-three pattern among these types that has zero `u`, zero total `s`, and odd logical parity. In two rounds, put `B` in round 0 and `C` in round 1:

```text
round 0: U_0=0=C_-1,  C_0=1;
round 1: U_1=1=C_0,   C_1=0;
logical parity=1.
```

Thus `(d_1,d_2,d_3,d_4)=(3,2,2,2)` and the abstract example attains `R_stab=d_infinity=2`. It is a test of the algebra, not a claim that this dictionary is realized by a physical CSS schedule.

The exact successful program was:

```python
from itertools import combinations

effects = [(s,u,l) for s in (0,1) for u in (0,1) for l in (0,1)
           if (s,u,l)!=(0,0,0)]

def solve(dictionary, R):
    n=len(dictionary)
    best=None
    supports=[]
    for mask in range(1 << (n*R)):
        wt=bin(mask).count("1")
        if best is not None and wt>best:
            continue
        c=0
        logical=0
        supp=set()
        ok=True
        for r in range(R):
            sr=ur=lr=0
            for i,(s,u,l) in enumerate(dictionary):
                if (mask >> (r*n+i)) & 1:
                    sr ^= s; ur ^= u; lr ^= l; supp.add(r)
            if ur != c:
                ok=False
                break
            c ^= sr
            logical ^= lr
        if ok and c==0 and logical==1:
            if best is None or wt<best:
                best=wt; supports=[tuple(sorted(supp))]
            elif wt==best:
                supports.append(tuple(sorted(supp)))
    return best, supports

tested=finite=0
drops=[]
violations=[]
for size in range(1,5):
    for dictionary in combinations(effects,size):
        tested += 1
        vals=[]
        for R in range(1,5):
            d,supp=solve(dictionary,R)
            vals.append(d)
            if d is not None:
                finite += 1
                for S in supp:
                    contiguous=(not S) or S==tuple(range(S[0],S[-1]+1))
                    span=(S[-1]-S[0]+1) if S else 0
                    if not contiguous or span>d:
                        violations.append((dictionary,R,d,S))
        if vals[0] is not None and vals[1] is not None and vals[1]<vals[0]:
            drops.append((dictionary,tuple(vals)))
        for a,b in zip(vals,vals[1:]):
            if a is not None and b is not None and b>a:
                violations.append(("monotonicity",dictionary,vals))

print("dictionaries_tested",tested)
print("finite_R_cases",finite)
print("contiguity_or_monotonicity_violations",len(violations))
print("d2_less_than_d1_examples",len(drops))
for item in drops[:5]:
    print(item)
```

### 10.3 Ambiguity and counterexample attack table

| Attack | Result | Protection in the final proof |
|---|---|---|
| remove the absolute initial detector | `(W)` is pinned only to an unknown constant `kappa`; an empty round gives `C=kappa`, not closure | ideal initialization and `D_(b,0)` |
| remove the terminal readout detector | total residual syndrome need not close; translation can leak at the right end | ideal final readout and boundary `R` |
| append without checking old terminal/new interior index | old readout and new measurement are different records | round transparency, Theorem 5.1 step 3 |
| cross-round idle compression | the round-location dictionary can depend on `R`; translation is not defined | verbatim fixed block, disjoint per-round locations |
| dependent generator rows | Definition 2.7 omits redundancy detectors | canonical decomposition plus sector projection |
| arbitrary detector/observable complement | distance can change (`2` versus `3,4` in recorded `D'`) | named Definition-2.7/Definition-3.5 pair only |
| full-Pauli minimum contains Y faults | a naive CSS-sector restriction could lower or alter weight | locationwise `Pi_X/Pi_Z`, full group, minimality forces same weight |
| two faults at one location | treating them as two independent occupied locations overcounts | collision lemma |
| non-group or nonuniform location costs | collision merge and sector projection can fail | explicitly out of scope |
| asymmetric sector distances | `d_R^sigma<=d` is false | use `d_R=min_sigma d_R^sigma<=d` only after choosing an attaining sector |
| gap with zero faults but nonzero state | deleting it directly is invalid | `(W)` proves zero state before the split |
| several logical qubits | a scalar parity argument could miss cancellation | use vector `ell in F_2^k`; nonzero sum implies a nonzero half |

---

## 11. External facts and exact residuals

### 11.1 Load-bearing mathematical inputs

| Input | Status here | Verification needed later |
|---|---|---|
| Pauli groups modulo phase are elementary `F_2` groups | fault-model algebra; used explicitly | check all named location menus are full groups |
| CNOT conjugation table and linear propagation | re-derived at the component level in Sections 3.1-3.2 | verify against the circuit direction conventions |
| CSS quotient dimensions and logical pairing | short derivation in Section 1.1 | verify `k=n-rank H_X-rank H_Z` and dual logical basis |
| deterministic-parity back-propagation | re-derived in Section 4.1 | check input stabilizers and MC cancellation |
| Definition 3.5 is the intended repository split | **model decision, not theorem** | verify the lead-ratification provenance; mathematics is conditional on the named definition |

No published theorem is load-bearing. In particular, BCOQ eventual periodicity and stabilizer-channel composition are not used. Archived numerical distance searches are not used.

### 11.2 Exact remaining semantic residual

The word **legal** in the current node sentence is not defined there. The proof requires conflict legality plus measurement consistency. Likewise, “repeated-round distances” must mean verbatim repetition, min over sectors, the named canonical detector spaces, and uniform full-Pauli occupied-location weight. If an independent reviewer confirms that all these meanings are definitionally inherited into the current sentence, the mathematics supports the current hash. If the reviewer applies the protocol's standalone-claim standard, Section 12's repair is needed.

### 11.3 Exact remaining evidential residual

This artifact has not been independently reviewed. A later reviewer must verify every definition bridge and proof step, bind the exact claim text reviewed, and be someone other than this author. Until then, no `PROVED` node-level recommendation is licensed.

---

## 12. Exact proposed standalone claim repair

Recommended YAML-loaded replacement string:

> For every fixed legal (conflict-free and measurement-consistent) single-round single-ancilla CSS syndrome-extraction schedule M, let C_R^Z(M) and C_R^X(M) be the ideal-boundary memory experiments formed by R verbatim repetitions of M with the uniform unit-cost full-Pauli per-location fault model, and let d_R(M) be the minimum of their circuit distances measured against, respectively, the canonical detector space of Definition 3.5 in the CIRCDIST.sat.transfer proof dossier and its section-8.1 mirror (equivalently in value only, not in detector-set equality, the corresponding Definition-2.7 detector sets). Then d_(R+1)(M) <= d_R(M) for every R >= 1; d_infinity(M) := lim_{R to infinity} d_R(M) exists; in each memory sector every minimum-weight undetectable logical has a same-weight sector-pure representative supported on a contiguous interval of rounds whose span is at most its faulty-location weight; and, writing d = min(d_X,d_Z) for the CSS code distance and R_stab(M) := min{R_0 >= 1 : d_R(M) = d_infinity(M) for all R >= R_0}, one has R_stab(M) <= d_infinity(M) <= d and d_R(M) = d_d(M) = d_infinity(M) for every R >= d. Consequently d_1(M),...,d_d(M) determine both d_infinity(M) and R_stab(M).

Normalized length and hash:

```text
1210 characters
sha256:301eee2dcc5bf16d363636af642e50e4376508614402c1213b5821e38ec11139
```

This repair makes four corrections without changing the intended mathematical result:

1. it defines legal schedule strongly enough for the detector model;
2. it pins verbatim layout, aggregation, detector split, and weight;
3. it states the witness result per sector and as a same-weight representative;
4. it identifies `d` as `min(d_X,d_Z)`, preventing the known false per-sector reading.

If the dispatcher keeps the current claim instead, a fresh review should state explicitly that these are definitional expansions of the current 489-character string and bind the current hash, not the proposed hash.

---

## 13. Source locators

All paths are repository-relative.

| Source | Exact locator used |
|---|---|
| `DAG_PROTOCOL.md` | §§2, 4, 6-7: route semantics, completion levels, independent review, node audit |
| `FILE_PROTOCOL.md` | §§2, 4, 6: canonical ownership, artifact placement, atomic update responsibilities |
| `circdist/proof-dag/nodes/CIRCDIST.sat.window.yaml` | claim lines 6-10; caveats lines 13-36; frontier `task-001` lines 102-108 |
| `circdist/proof-dag/nodes/CIRCDIST.sat.instances.yaml` | caveat `(W)` lines 12-13; route lines 96-179; dispatcher caveat `IW-C0` lines 140-145 |
| `circdist/proof-dag/nodes/CIRCDIST.sat.yaml` | exact V3 root claim; R-C2/R-C4/R-C12; route `asymptotic-stability-assembly` |
| `circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md` | common definitions lines 14-40; original repeated-round question lines 185-232 |
| `circdist/artifacts/definitions/SAT_RESCOPE_20260822.md` | ideal-boundary rescope §§0-3, especially lines 28-56 |
| `circdist/artifacts/circdist_sat_recon_20260820.md` | scope §§1-2; recursion §3.1; transfer §3.2; padding/window §§3.4-3.5 |
| `circdist/artifacts/circdist_sat_window_theorem_20260822.md` | Definitions 1.1-1.12; Lemmas 2.1-2.12; Theorems 3.1, 4.1, 4.3, 5.1 |
| `circdist/artifacts/circdist_sat_window_amendment1_20260822.md` | §§1-3: S3-prime, summary superscript, mirror-MC repair |
| `circdist/reviews/circdist_sat_window_review_20260822.md` | Items 2-5; both boundary attacks; gap split; mirror caveat |
| `circdist/reviews/circdist_amendments4_review_20260822.md` | Item 2, especially §§3.2-3.5 |
| `circdist/artifacts/circdist_lift_iff_proof_20260820.md` | Definitions 1.5-1.11; §§4.1-4.3 `(LIFT')`; §§5.9-5.10 |
| `circdist/reviews/circdist_lift_claimrepair2_review_20260823.md` | §§4.2-4.3, especially lines 194-229: per-sector `d` defect and asymmetric example |
| `circdist/artifacts/circdist_sat_transfer_proof_20260823.md` | Definitions 2.1-2.11; Lemma 2.9; §§3.1-3.7; §8.1 mirror |
| `circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md` | Repair 1: ratification, corrected safe containment, arbitrary-split counterexample |
| `circdist/reviews/circdist_transfer_bridgefold_20260823.md` | §§2.1-2.3: collision and named detector bridges; §3.2 counterexample calibration; §5 caveats |
| `circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md` | §§3-5 and Limitation 4: named-pair value equality and rejection of broad convention independence |
| `circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md` | §§3-7 and limitations: finite-prefix/tail boundary and weight bridge |

---

## 14. Later independent-review checklist

A fresh reviewer should not merely compare this document with the earlier theorem. The minimum adequate review is:

1. Recompute the current claim hash `8698b051...` and, if considering the repair, the proposed hash `301eee2d...` from YAML-loaded strings.
2. Decide explicitly whether “legal” includes measurement consistency and whether “repeated” means a fixed verbatim block with no cross-round compression.
3. Re-derive `c_ab=c'_ab` and verify that the X-memory mirror remains in scope.
4. Verify every location class is a full Pauli group at uniform unit cost and that locations are partitioned by round.
5. Re-derive the canonical detector decomposition, including dependent-generator redundancy parities.
6. Check that `Pi_X/Pi_Z` preserves the designated records and observables, annihilates the opposite record space, and cannot lower a canonical minimum's weight.
7. Check the single-fault two-slice formula at `r=0` and `r=R-1` directly from the CNOT table.
8. Derive `(W)` from the entire detector chain, including `U_R=0` and terminal closure.
9. Audit the append map at all four index classes in Theorem 5.1 and audit the prepend map separately.
10. Audit the gap split for both halves at `t<=g` and `t>g`, for a vector of `k` logical parities rather than one scalar.
11. Confirm that no same-location collision or irrelevant Pauli component can remain in the same-weight representative.
12. Re-derive translation into `C_w` and check both new temporal ends.
13. At Theorem 9.1, verify that the only `<=d` step is for the min-over-sectors value and the chosen attaining witness; compare against the asymmetric `d_X=3,d_Z=2,d=2` example.
14. At Theorem 9.2, verify the minimal-index argument gives `R_stab<=w<=d_infinity`, with no off-by-one shift.
15. Optionally rerun the 98-dictionary test; treat it only as corroboration.
16. Attack the proof using the recorded `D'` detector split and confirm that the proof refuses, rather than absorbs, that convention.
17. State every limitation and whether the review covers the current claim or the proposed repaired claim. Do not bind one hash while reviewing the other.
18. Only after all checks pass should the reviewer recommend a completion level. The author of this artifact cannot supply that recommendation.

---

## 15. Field-level dispatcher recommendations

These are recommendations, not repository mutations or review licenses.

### Recommended precision path

1. **`claim`:** replace with the exact 1210-character string of Section 12; expected normalized hash `sha256:301eee2dcc5bf16d363636af642e50e4376508614402c1213b5821e38ec11139`.
2. **`assessment.level`:** keep `CERTIFIED*` until a fresh independent reviewer checks this complete argument against the exact repaired string. This authored artifact alone cannot support a promotion.
3. **`assessment.basis.evidence`:** add this artifact as authored text evidence, not as a review.
4. **`assessment.basis.reviews`:** do not rebind an old review to the new hash. Add a new independent review entry only after that review exists.
5. **`frontier.task-001`:** keep it open until the artifact is independently reviewed. After a successful review, replace it with no task or with any exact residual the reviewer identifies; do not close it merely because this file exists.
6. **`events`:** if the claim is repaired, append a dated `repair-applied` event identifying the semantic pins and both hashes. Do not rewrite prior events.
7. **dependent routes:** because `CIRCDIST.sat.instances` uses this node as a premise and the root uses both, re-adjudicate the child route and the root implication against the then-current premise text. `IW-C0` and the finite-certificate gate remain untouched by this proof.
8. **generated views and validators:** after authorized canonical edits, regenerate derived views and run all protocol closeout commands. This author did not run any write-generating command.

### Minimal no-claim-change path

If the dispatcher judges all omitted terms definitionally inherited, keep the current claim and hash, link this artifact as evidence, and commission a fresh independent review explicitly covering Definitions 1.1-1.8 of this document as the expansion of the current string. The reviewer must explain why that incorporation is compatible with the protocol's standalone precision requirement.

Under either path, no self-authored `reviewed_hash` or completion review is proposed here.

---

## 16. FIX-2 command, process, scratch, and mutation disclosure

### 16.1 Execution model

All research and writing occurred in one worker session. No sub-agent, delegated task, solver, compiler, network client, browser, detached job, or background job was started. Independent read-only shell commands were sometimes submitted together through the orchestration layer and awaited to completion; they were ordinary foreground OS processes, not additional worker sessions.

Every `exec_command` used the repository root as its working directory and an ordinary foreground shell wrapper. Pipelines launched the named `nl`/`sed`, `ps`/`awk`, or similar children and were awaited. Tool-output transcripts are not repository files.

### 16.2 Complete command ledger

The following are all top-level OS commands issued by this worker, in order. Commands 48 and 49 are the exhaustive toy check; command 48 failed because this host's Python 3.9 lacks `int.bit_count`, and command 49 changed only that expression to `bin(mask).count("1")`. The complete successful source is reproduced in Section 10.2. Command 50 is the exact current/proposed claim hash script whose two strings and outputs are reproduced in Sections 0 and 12.

```text
01 git status --short
02 cat DAG_PROTOCOL.md FILE_PROTOCOL.md
03 cat circdist/proof-dag/nodes/CIRCDIST.sat.window.yaml circdist/proof-dag/nodes/CIRCDIST.sat.instances.yaml circdist/proof-dag/nodes/CIRCDIST.sat.yaml
04 wc -l DAG_PROTOCOL.md FILE_PROTOCOL.md circdist/proof-dag/nodes/CIRCDIST.sat.window.yaml circdist/proof-dag/nodes/CIRCDIST.sat.instances.yaml circdist/proof-dag/nodes/CIRCDIST.sat.yaml circdist/artifacts/circdist_sat_window_theorem_20260822.md circdist/artifacts/circdist_sat_window_amendment1_20260822.md circdist/reviews/circdist_sat_window_review_20260822.md circdist/reviews/circdist_amendments4_review_20260822.md circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md
05 nl -ba circdist/proof-dag/nodes/CIRCDIST.sat.window.yaml
06 nl -ba FILE_PROTOCOL.md
07 sed -n '1,240p' circdist/artifacts/circdist_sat_window_theorem_20260822.md
08 sed -n '241,480p' circdist/artifacts/circdist_sat_window_theorem_20260822.md
09 sed -n '481,720p' circdist/artifacts/circdist_sat_window_theorem_20260822.md
10 sed -n '721,980p' circdist/artifacts/circdist_sat_window_theorem_20260822.md
11 nl -ba circdist/artifacts/circdist_sat_window_theorem_20260822.md | sed -n '300,420p'
12 nl -ba circdist/artifacts/circdist_sat_window_theorem_20260822.md | sed -n '421,540p'
13 nl -ba circdist/artifacts/circdist_sat_window_theorem_20260822.md | sed -n '541,660p'
14 nl -ba circdist/artifacts/circdist_sat_window_theorem_20260822.md | sed -n '661,720p'
15 nl -ba circdist/artifacts/circdist_sat_window_amendment1_20260822.md | sed -n '1,180p'
16 nl -ba circdist/artifacts/circdist_sat_window_amendment1_20260822.md | sed -n '181,360p'
17 nl -ba circdist/artifacts/circdist_sat_window_amendment1_20260822.md | sed -n '361,520p'
18 nl -ba circdist/reviews/circdist_sat_window_review_20260822.md | sed -n '1,180p'
19 nl -ba circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml
20 rg -n "Definition 3\.5|Proposition 3\.7|Lemma 2\.9|8\.1|detector.*convention|Definition 2\.7" circdist/artifacts/circdist_sat_transfer_proof_20260823.md circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md circdist/reviews/circdist_transfer_bridgefold_20260823.md circdist/reviews/circdist_sat_transfer_review_20260823.md circdist/reviews/circdist_sat_transfer_rereview_20260823.md
21 rg -n "window|detector|Definition 3\.5|Definition 2\.7|weight|location|single-ancilla|ideal" circdist/artifacts/circdist_sat_recon_20260820.md circdist/artifacts/circdist_lift_iff_proof_20260820.md circdist/artifacts/circdist_lift_iff_amendment2_20260820.md circdist/reviews/circdist_lift_proofs_review_20260820.md circdist/reviews/circdist_lift_claimrepair2_review_20260823.md
22 wc -l circdist/artifacts/circdist_sat_transfer_proof_20260823.md circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md circdist/reviews/circdist_transfer_bridgefold_20260823.md circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md circdist/artifacts/circdist_sat_recon_20260820.md circdist/artifacts/circdist_lift_iff_proof_20260820.md circdist/artifacts/circdist_lift_iff_amendment2_20260820.md
23 rg -n '^## |^### |\*\*Definition 2\.|\*\*CONJECTURED 2\.|\*\*Lemma 2\.9|\*\*Definition 3\.5|\*\*CONJECTURED 3\.|\*\*Proposition 3\.7|\*\*CONJECTURED 8\.1' circdist/artifacts/circdist_sat_transfer_proof_20260823.md
24 nl -ba circdist/artifacts/circdist_sat_transfer_proof_20260823.md | sed -n '136,255p'
25 nl -ba circdist/artifacts/circdist_sat_transfer_proof_20260823.md | sed -n '256,360p'
26 nl -ba circdist/artifacts/circdist_sat_transfer_proof_20260823.md | sed -n '361,439p'
27 nl -ba circdist/artifacts/circdist_sat_transfer_proof_20260823.md | sed -n '677,713p'
28 nl -ba circdist/reviews/circdist_transfer_bridgefold_20260823.md | sed -n '1,120p'
29 nl -ba circdist/reviews/circdist_transfer_bridgefold_20260823.md | sed -n '121,240p'
30 nl -ba circdist/reviews/circdist_transfer_bridgefold_20260823.md | sed -n '241,360p'
31 nl -ba circdist/reviews/circdist_transfer_bridgefold_20260823.md | sed -n '361,480p'
32 nl -ba circdist/reviews/circdist_transfer_bridgefold_20260823.md | sed -n '481,639p'
33 rg -n "IW-C0|dispatcher|caveat|window|Definition 3\.5|Definition-2\.7|detector|weight|Claim hash|claim hash|hash" circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md
34 rg -n "window|Definition 3\.5|Definition-2\.7|detector|weight|R5|claim hash|Hash|hash|caveat" circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md
35 rg -n "IW-C0|finite-prefix-window-closure|dispatcher" circdist/proof-dag/nodes/CIRCDIST.sat.instances.yaml operations/circdist/SCHEDULER.yaml circdist -g '*.md' -g '*.yaml'
36 nl -ba circdist/proof-dag/nodes/CIRCDIST.sat.instances.yaml | sed -n '1,210p'
37 wc -l circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md circdist/artifacts/definitions/SAT_RESCOPE_20260822.md
38 rg -n "公共定义|legal|合法|idle|compression|压缩|single-ancilla|fault|distance|detector|R_stab|d_infinity|重复|verbatim" circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md circdist/artifacts/definitions/SAT_RESCOPE_20260822.md
39 nl -ba circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md | sed -n '1,80p'
40 nl -ba circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md | sed -n '180,243p'
41 nl -ba circdist/artifacts/definitions/SAT_RESCOPE_20260822.md
42 rg -n '^## |^### |Definition|fault|detector|weight|d_R|sector|round|location|boundary|Stim|transfer' circdist/artifacts/circdist_sat_recon_20260820.md
43 nl -ba circdist/artifacts/circdist_sat_recon_20260820.md | sed -n '62,180p'
44 nl -ba circdist/artifacts/circdist_sat_recon_20260820.md | sed -n '183,240p'
45 nl -ba circdist/artifacts/circdist_lift_iff_proof_20260820.md | sed -n '88,235p'
46 nl -ba circdist/artifacts/circdist_lift_iff_proof_20260820.md | sed -n '547,615p'
47 rg -n "detector|weight|sector|contigu|window|round|d_R|d_infinity|d_∞|R_stab|boundary" circdist/artifacts/circdist_lift_iff_amendment2_20260820.md circdist/reviews/circdist_lift_claimrepair2_review_20260823.md circdist/reviews/circdist_lift_proofs_review_20260820.md
48 python3 - <<'PY' [first 98-dictionary script; failed at mask.bit_count() under Python 3.9]
49 python3 - <<'PY' [successful 98-dictionary script reproduced in Section 10.2, using bin(mask).count("1")]
50 python3 - <<'PY' [YAML-load current claim; hash current and exact proposed strings; strings and output reproduced in Sections 0 and 12]
51 nl -ba circdist/reviews/circdist_lift_claimrepair2_review_20260823.md | sed -n '172,241p'
52 nl -ba circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md | sed -n '1,140p'
53 nl -ba circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md | sed -n '141,280p'
54 nl -ba circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md | sed -n '281,420p'
55 nl -ba circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md | sed -n '421,560p'
56 nl -ba circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md | sed -n '561,685p'
57 nl -ba circdist/reviews/circdist_sat_window_review_20260822.md | sed -n '181,342p'
58 nl -ba circdist/reviews/circdist_amendments4_review_20260822.md | sed -n '1,180p'
59 nl -ba circdist/reviews/circdist_amendments4_review_20260822.md | sed -n '181,360p'
60 nl -ba circdist/reviews/circdist_amendments4_review_20260822.md | sed -n '361,544p'
61 test ! -e circdist/artifacts/circdist_sat_window_selfcontained_exact_proof_20260826.md
62 git status --short -- circdist/artifacts/circdist_sat_window_selfcontained_exact_proof_20260826.md
63 python3 tools/proof_dag_check.py --problem circdist
64 python3 - <<'PY' [post-write artifact existence, UTF-8, marker, line-ending, trailing-whitespace, byte/line-count, and SHA-256 assertions]
65 git status --short -- circdist/artifacts/circdist_sat_window_selfcontained_exact_proof_20260826.md
66 find /tmp -maxdepth 1 -name 'circdist_sat_window_selfcontained*' -print
67 ps -axo pid=,ppid=,stat=,command= | awk '/[c]ircdist_sat_window_selfcontained|[w]indow_selfcontained_exact_proof/ {print}'
68 shasum -a 256 circdist/artifacts/circdist_sat_window_selfcontained_exact_proof_20260826.md
69 python3 tools/proof_dag_check.py --problem circdist
70 python3 - <<'PY' [final artifact existence, UTF-8, marker, line-ending, trailing-whitespace, byte/line-count, and SHA-256 assertions]
71 git status --short -- circdist/artifacts/circdist_sat_window_selfcontained_exact_proof_20260826.md
72 find /tmp -maxdepth 1 -name 'circdist_sat_window_selfcontained*' -print
73 ps -axo pid=,ppid=,stat=,command= | awk '/[c]ircdist_sat_window_selfcontained|[w]indow_selfcontained_exact_proof/ {print}'
74 shasum -a 256 circdist/artifacts/circdist_sat_window_selfcontained_exact_proof_20260826.md
```

Commands 63-68 are the first post-write verification pass. A reproducibility audit then noticed that Section 10.2's displayed program omitted only its five final output statements; a second non-OS patch added those statements and synchronized this disclosure. Commands 69-74 are the final read-only verification pass after that documentation-only correction. Their results are reported to the dispatcher with the final artifact digest.

### 16.3 Processes and exit status

Processes invoked by name were foreground `zsh` shell wrappers and the utilities `git`, `cat`, `wc`, `nl`, `sed`, `rg`, `python3`, `test`, `find`, `ps`, `awk`, and `shasum`. Python imported only standard-library modules, `yaml` for the already installed repository serialization check, and repository validator modules when command 63 ran. No subprocess was left unawaited.

Commands 01-47 and 49-74 exited zero. Command 48 exited nonzero with `AttributeError: 'int' object has no attribute 'bit_count'`; it created no file or child process that survived. Both post-write verification passes are recorded in the task handoff; the digest from command 74 is final.

### 16.4 Scratch and logs

- Worker-created scratch directories: **none**.
- Worker-created scratch files: **none**.
- Scratch paths used: **none**.
- New log files: **none**. Standard output/error exists only in the tool transcript.
- Network access: **none used**.
- Background or detached processes: **none**.
- Sub-agents: **none spawned**.
- Temporary paths expected to survive: **none**.

### 16.5 Durable mutations

The initial repository status already contained many unrelated modified and untracked paths. Before writing, commands 61-62 verified that the authorized target did not exist and had no status entry. This worker issued two non-OS `apply_patch` mutations, both targeting the same sole durable file: the first created it; the second added the five omitted print statements to the already reported toy-test source and synchronized this process disclosure. The only durable path is:

```text
circdist/artifacts/circdist_sat_window_selfcontained_exact_proof_20260826.md
```

No other mutation command was issued. The artifact is intentionally unlinked until the dispatcher performs an authorized canonical update.

---

## 17. Concise mathematical conclusion

Under verbatim repeated rounds, ideal absolute/terminal boundaries, the current canonical detector split, the uniform full-Pauli location model, and min-over-sectors aggregation, the boundary equation

```text
U_t=C_(t-1)
```

does all the work. It makes fault-free padding exact, makes an internal empty round a zero-charge cut, and makes a closed contiguous witness freely translatable. Minimum witnesses therefore have contiguous same-weight sector-pure representatives; aggregate minima have span at most `d_R<=d`; and translation into `d` rounds proves

```text
d_R=d_d=d_infinity for R>=d,
R_stab<=d_infinity<=d.
```

The mathematics is complete. Independent review and exact claim-field adjudication remain.
