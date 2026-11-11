# `CIRCDIST.sat.window`: fresh self-contained exact-text review

**Date:** 2026-08-26
**Role:** fresh strict-serial independent reviewer, ProofPilot round 51
**Canonical target:** `circdist/proof-dag/nodes/CIRCDIST.sat.window.yaml`
**Authored proof reviewed:** `circdist/artifacts/circdist_sat_window_selfcontained_exact_proof_20260826.md`
**Review output:** `circdist/reviews/circdist_sat_window_selfcontained_exact_review_20260826.md`
**Worker restrictions observed:** no sub-agent; no network; no mutation of a canonical node, scheduler, protocol, generated view, tool, earlier artifact/review, migration record, or any durable repository path other than this review.

## 0. Executive disposition

### Finding F-COMPLETION

The authored proof is mathematically complete for the intended current proposition after one exact-text correction. It gives a direct, finite proof; it does not need an unresolved transfer theorem, the instances theorem, the root theorem, an eventual-periodicity theorem, or a computation. I independently re-derived every load-bearing step in both CSS memory sectors, including dependent stabilizer generators, same-location Pauli collisions, both temporal boundaries, asymmetric CSS distances, vector logical parity, and the minimal-index argument.

The exact 1,210-character claim proposed in artifact §12 is **not a complete standalone serialization**. It begins “For every fixed legal ... schedule M” and leaves the underlying CSS code and its load-bearing restriction `k >= 1` implicit. The proof itself assumes `k >= 1` in §1.1, the earlier window theorem assumes it, and transfer scope T0 assumes it. Without it, the logical quotients may be zero, the minima defining `d_X` and `d_Z` are over empty sets, a nonzero logical witness need not exist, and “the first `d` distances” need not denote a finite list. This is an exact-claim defect rather than a mathematical defect in the proved proposition.

A compact correction replaces that prefix by `For every CSS code Q = [[n,k,d]] with k >= 1 and every ... schedule M for Q`, explicitly binding both the code and schedule domain. The corrected claim is exactly 1,261 characters and has normalized hash

```text
sha256:6c50b4049ae908d6646e87f7446f8fb7ea9583182fb79da3cb6b935c7011ccc4
```

I license replacement of the current 489-character claim by that exact corrected string, and I license `assessment.level: PROVED` for that exact hash only. I do **not** license `PROVED` for the authored 1,210-character string/hash, for the current shorthand hash, or for any text that drops a pin named below.

### Verdict matrix

| Question | Independent verdict |
|---|---|
| Mathematics under the explicit intended model and `k >= 1` | **PASS; complete proof** |
| Current 489-character claim | **Too compressed for standalone completion; replace** |
| Artifact §12 1,210-character repair | **Reject as final text; omits `k >= 1`** |
| Corrected 1,261-character repair | **PASS; exact installable claim** |
| Semantic identity / precision repair | **Precision-preserving relative to the proposition consistently scoped by the proof dossier; it makes inherited restrictions explicit** |
| Material narrowing relative to a literal conflict-free-only, arbitrary-repetition reading | **Yes, but that broader reading was never proved and is contradicted by recorded boundary-compression and measurement-consistency issues** |
| Allowed canonical claim replacement | **Yes, only to the exact 1,261-character string in Finding F-CLAIM** |
| Node assessment level after exact replacement | **PROVED** |
| Required `reviewed_hash` | **`sha256:6c50b4049ae908d6646e87f7446f8fb7ea9583182fb79da3cb6b935c7011ccc4`** |
| Old review bindings | **Do not bind the new text; retain as historical evidence** |
| Reviews basis | **Replace the two completion-basis review entries by this fresh exact review; do not delete their files or historical evidence links** |
| Evidence basis | **Retain historical evidence; add the authored proof and the four definition/calibration sources specified below** |
| Caveats / summary / frontier | **Replace with the exact fields in §14** |
| Events | **Append the three exact events in §14; never rewrite old events** |
| Generated views | **Regenerate only after dispatcher installation; scratch generation predicts only the intended window level marks change** |
| `CIRCDIST.sat.instances` | **No inherited promotion; route applicability needs fresh re-adjudication against the changed premise text and finite-certificate gate remains** |
| `CIRCDIST.sat` root | **No inherited promotion; transfer and instances remain `CERTIFIED*`, and the root route needs fresh premise-text re-adjudication** |

## 1. Materials and protocol standard

I read the complete 1,154-line authored proof rather than relying on its abstract, checklist, or proposed disposition. I also read the current target and the present root, instances, and transfer nodes; the full current `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md`; the frozen problem definitions and ideal-boundary rescope; the transfer proof dossier and ratifying amendment; the earlier window theorem, amendment, and both earlier window reviews; the V3 exact-text review; the instances-window-edge exact review; and every source the proof identifies as load-bearing or provenance-bearing.

The principal paths were:

- `DAG_PROTOCOL.md`
- `FILE_PROTOCOL.md`
- `circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md`
- `circdist/artifacts/definitions/SAT_RESCOPE_20260822.md`
- `circdist/proof-dag/nodes/CIRCDIST.sat.window.yaml`
- `circdist/proof-dag/nodes/CIRCDIST.sat.instances.yaml`
- `circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml`
- `circdist/proof-dag/nodes/CIRCDIST.sat.yaml`
- `circdist/artifacts/circdist_sat_recon_20260820.md`
- `circdist/artifacts/circdist_lift_iff_proof_20260820.md`
- `circdist/artifacts/circdist_lift_iff_amendment2_20260820.md`
- `circdist/reviews/circdist_lift_proofs_review_20260820.md`
- `circdist/reviews/circdist_lift_claimrepair2_review_20260823.md`
- `circdist/artifacts/circdist_sat_window_theorem_20260822.md`
- `circdist/artifacts/circdist_sat_window_amendment1_20260822.md`
- `circdist/reviews/circdist_sat_window_review_20260822.md`
- `circdist/reviews/circdist_amendments4_review_20260822.md`
- `circdist/artifacts/circdist_sat_transfer_proof_20260823.md`
- `circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md`
- `circdist/reviews/circdist_transfer_bridgefold_20260823.md`
- `circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md`
- `circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md`
- `circdist/artifacts/circdist_sat_instances_20260823.md`
- `circdist/reviews/circdist_sat_instances_review_20260823.md`
- the complete authored proof named above.

The operative protocol standard is strict completion. A node may be `PROVED` only when its exact normalized claim is completely established by independently checked evidence and every load-bearing premise/import is at the required level. A review must bind the exact reviewed hash; claim repair invalidates the old hash as a current completion binding. Dependencies, route level, and premise level are distinct. A premise’s promotion does not propagate through a route or promote a downstream node. Events are append-only. Authored evidence may be blessed by an independent review, but installation is a later dispatcher action. Generated views derive from canonical state and are not edited directly.

Those rules determine the installation contract in §14. This report is the blessing. It is not the installation.

## 2. Exact-text and hash audit

### 2.1 Normalization

For all three candidate strings I used the repository rule

```text
"sha256:" + SHA256(UTF-8(claim.replace("\r\n", "\n").strip()))
```

on the YAML-loaded scalar or exact candidate scalar. I separately counted Unicode code points and UTF-8 bytes. These strings are ASCII, so the character and byte counts agree.

| Text | Exact length | Normalized SHA-256 |
|---|---:|---|
| Current YAML-loaded claim | 489 | `sha256:8698b051b15fa14ff669299580d9b7bfec01808c0a34133ef09264e749466146` |
| Artifact §12 proposed claim | 1,210 | `sha256:301eee2dcc5bf16d363636af642e50e4376508614402c1213b5821e38ec11139` |
| Corrected installable claim | 1,261 | `sha256:6c50b4049ae908d6646e87f7446f8fb7ea9583182fb79da3cb6b935c7011ccc4` |

The authored-proof file itself was 63,975 bytes, 1,154 lines, and had SHA-256

```text
bf0d6dd591ae0fb11ef5c75196ffaa89456b5cfd2cc40493fffd6274607f10f7
```

matching the commission. YAML dump/load round trips preserved both candidate claims exactly.

### Finding F-CLAIM

The exact installable claim is:

> For every CSS code Q = [[n,k,d]] with k >= 1 and every fixed legal (conflict-free and measurement-consistent) single-round single-ancilla CSS syndrome-extraction schedule M for Q, let C_R^Z(M) and C_R^X(M) be the ideal-boundary memory experiments formed by R verbatim repetitions of M with the uniform unit-cost full-Pauli per-location fault model, and let d_R(M) be the minimum of their circuit distances measured against, respectively, the canonical detector space of Definition 3.5 in the CIRCDIST.sat.transfer proof dossier and its section-8.1 mirror (equivalently in value only, not in detector-set equality, the corresponding Definition-2.7 detector sets). Then d_(R+1)(M) <= d_R(M) for every R >= 1; d_infinity(M) := lim_{R to infinity} d_R(M) exists; in each memory sector every minimum-weight undetectable logical has a same-weight sector-pure representative supported on a contiguous interval of rounds whose span is at most its faulty-location weight; and, writing d = min(d_X,d_Z) for the CSS code distance and R_stab(M) := min{R_0 >= 1 : d_R(M) = d_infinity(M) for all R >= R_0}, one has R_stab(M) <= d_infinity(M) <= d and d_R(M) = d_d(M) = d_infinity(M) for every R >= d. Consequently d_1(M),...,d_d(M) determine both d_infinity(M) and R_stab(M).

This block contains 1,261 characters after removing only the Markdown quotation prefix and final report newline. Its normalized hash is exactly the one above.

### 2.2 Why `k >= 1` is required

The CSS distances used by the proof are quotient minima. With row spaces

```text
S_X = row(H_X),     S_Z = row(H_Z),
L_X = ker(H_Z) / S_X,     L_Z = ker(H_X) / S_Z,
```

the spatial distances are

```text
d_X = min{|x| : x in ker(H_Z) \ S_X},
d_Z = min{|z| : z in ker(H_X) \ S_Z}.
```

For `k=0`, both logical quotients can be trivial. Then those minima are over empty sets unless one introduces an extra `+infinity` convention that the claim does not state. The circuit-distance minima likewise have no nonzero logical event, the existence proof in §6 cannot choose a spatial logical witness, and `d=min(d_X,d_Z)` does not supply a positive finite window. The sentence “the first `d` distances” also presumes a finite positive integer. The proof’s §1.1 explicitly assumes `k>=1`, as do the original window theorem and transfer scope. The omission is therefore load-bearing.

Adding the explicit code binder and `k >= 1` restriction does not alter any proved case. It makes the domain on which every displayed quantity is already defined explicit. The 51-character net expansion is exactly the replacement of the artifact prefix `For every fixed ... schedule M` by `For every CSS code Q = [[n,k,d]] with k >= 1 and every fixed ... schedule M for Q`.

### 2.3 Clause map: current shorthand, §12 repair, and corrected repair

| Proposition component | Current 489-character claim | Artifact §12, 1,210 characters | Corrected 1,261 characters | Review |
|---|---|---|---|---|
| CSS code domain | Implicit | Implicit through the schedule `M` | Explicit `Q=[[n,k,d]]`, `k>=1`, and `M for Q` | Correction required |
| Fixed one-round schedule | Present | Present | Present | Preserved |
| Conflict freedom | Hidden in `legal` | Explicit | Explicit | Precision pin |
| Measurement consistency | Omitted | Explicit | Explicit | Load-bearing precision pin |
| Single-ancilla extraction | Present | Explicit | Explicit | Preserved |
| Ideal boundaries | Present | Explicit via experiments | Explicit | Preserved |
| Repetition | “repeated-round” | `R verbatim repetitions` | Same | Load-bearing precision pin |
| No cross-round compression | Omitted | Entailed by verbatim blocks | Same | Load-bearing precision pin |
| Full Pauli faults | Omitted | Explicit | Same | Load-bearing precision pin |
| Unit occupied-location cost | Omitted | Explicit | Same | Load-bearing precision pin |
| Two memory sectors | Implicit | Explicit `C_R^Z,C_R^X` | Same | Precision pin |
| Aggregate distance | Ambiguous | Explicit minimum | Same | Load-bearing precision pin |
| Detector convention | Omitted | Named Def. 3.5 plus §8.1 mirror | Same | Load-bearing precision pin |
| Def. 2.7 relation | Omitted | Value-only equivalence, denies set equality | Same | Correctly scoped |
| Monotonicity and quantifier | Present | Explicit for every `R>=1` | Same | Preserved |
| Limit | Present | Defined | Same | Preserved |
| Sector projection | “a representative” | same-weight sector-pure, in each sector | Same | Clarifies proved content |
| Contiguity/span | Present | Explicit faulty-location weight | Same | Precision pin |
| Spatial distance | Bare `d` | `d=min(d_X,d_Z)` | Same | Corrected aggregation |
| Stabilization index | Used but not defined | Defined by minimal tail index | Same | Precision pin |
| Window equality | Present | Present | Same | Preserved |
| First-`d` determination | Present | Present | Same | Preserved |

### 2.4 Semantic identity

There are two comparisons, and conflating them would hide the history.

First, compare with the intended proposition actually scoped by the proof dossier. The original theorem opens with `k>=1`; Amendment 1 makes measurement consistency and the fixed repeated block load-bearing; the transfer dossier’s scope T0 uses the same nontrivial-code domain; the earlier reviews reject idle-layer compression across boundaries; and the asymmetric-code review requires min-over-sectors aggregation. Against that proposition, the corrected claim is a precision-preserving serialization. It does not remove a proved schedule or weaken a conclusion.

Second, compare with the current sentence read in isolation. A reader might take “legal” to mean conflict-free only, “repeated-round” to allow a compiler to compress adjacent idle layers, `d_R` to be a fixed sector, or `d` to bound each sector. Those broader readings are not established. Some are explicitly false or unsupported in the existing record. The replacement narrows those literal readings, but this is the repair’s purpose: the current claim overstates what its text alone pins. The protocol should preserve the proved proposition, not an accidental ambiguity.

The frozen common-definition file does not itself spell out measurement consistency in the word `legal`. That prevents treating measurement consistency as an invisible lexical fact. It does not prevent same-node precision repair because the historical theorem/amendment/reviews consistently use it as a hypothesis. The FILE protocol permits a canonical claim field to be repaired at the canonical owner, with old hashes retained as history. Creating a new theorem node is unnecessary because the object and conclusions are unchanged.

## 3. Model audit and definitions used in the proof

All algebra is over `F_2`, and Pauli operators are taken modulo phase.

### 3.1 CSS code and logical parities

Let `H_X` and `H_Z` list possibly redundant X- and Z-check generators, with

```text
H_X H_Z^T = 0.
```

Define

```text
S_X = row(H_X),                         S_Z = row(H_Z),
d_X = min{|x| : x in ker(H_Z)\S_X},
d_Z = min{|z| : z in ker(H_X)\S_Z},
d   = min(d_X,d_Z).
```

For `k>=1`, the quotient dimensions are

```text
dim ker(H_Z)-dim S_X
 = n-rank(H_Z)-rank(H_X)
 = k,
```

and likewise for the mirror quotient. Dual logical bases make membership outside the stabilizer row space equivalent to having nonzero pairing with at least one opposite-type logical. This justifies using a vector of `k` logical parity bits rather than one selected scalar.

Redundant rows cause no dimension or pairing problem: only ranks enter. They do matter for the detector split, handled in §5.

### 3.2 Legal means both scheduling conditions

Each X generator `a` owns a `|+>` ancilla, uses CNOTs `anc(a)->q`, and is measured in X. Each Z generator `b` owns a `|0>` ancilla, uses CNOTs `q->anc(b)`, and is measured in Z. Every incidence appears once. Conflict freedom requires at most one two-qubit gate per physical qubit per layer.

For a common data qubit of checks `a,b`, define

```text
c_ab  = #{q in supp(a)∩supp(b) :
          t(q->b) < t(a->q)} mod 2,
c'_ab = #{q in supp(a)∩supp(b) :
          t(a->q) < t(q->b)} mod 2.
```

Conflict freedom excludes equality of the two gate times on a common qubit, so the two strict inequalities partition the overlap. CSS commutation makes the overlap even. Therefore

```text
c_ab+c'_ab
 = |supp(a)∩supp(b)| mod 2
 = 0,
```

and consequently

```text
c_ab=c'_ab.
```

The standard check records are deterministic only when every `c_ab=0`. This is measurement consistency. The equation above proves that it is stable under the X/Z memory mirror. A merely conflict-free schedule with some `c_ab=1` does not have the advertised fault-free detector parity. The proof correctly takes `legal` to mean conflict-free plus measurement-consistent; the exact claim must say so because the frozen common definition does not silently provide the second condition.

### 3.3 Verbatim rounds and temporal boundaries

Fix a `T`-layer block `M`. The `R`-round experiment contains exact copies indexed `0,...,R-1`, with fresh ancillas and disjoint named location sets. The bijection between round copies preserves every one-round fault effect. A compiler may fix idle placement inside `M` before the block is frozen, but may not merge idle layers across copy boundaries or make the layout depend on `R`.

In Z-memory, data start ideally in `|0>` and are read ideally in Z. For a Z-check `b`, let `m_(b,r)` be its ancilla record and define virtual records

```text
m_(b,-1)=0,
m_(b,R)=sum_{q in supp(b)} rho_q,
```

where `rho_q` is the ideal terminal data-readout bit. The full temporal detector chain is

```text
D_(b,r)=m_(b,r)+m_(b,r-1),
b in B, r=0,...,R.
```

The `r=0` member is an absolute initial-boundary detector; the `r=R` member compares the last ancilla record with ideal terminal data parity. Opposite-family differences exist only at `r=1,...,R-1` in the usual short Definition-2.7 presentation because the initial opposite-family record is intrinsically random in this memory basis. X-memory mirrors all statements, with the full chain on X checks.

Both ends are essential. Dropping the initial absolute detector permits a nonzero constant record history. Dropping the final readout permits an open residual syndrome. Either deletion breaks gap closure and translation.

### 3.4 Full unit-cost Pauli location model and collisions

Each named location accepts the entire local group, identity included:

- 16 two-qubit Paulis after a CNOT;
- 4 one-qubit Paulis at a named idle or post-preparation slot;
- the two classical values at a record-flip location.

A configuration assigns one group element to every location. Its weight is the number of nonidentity occupied locations. Ideal initialization and ideal terminal readout have no fault locations. Every nonidentity group element costs one.

If an alternative description lists multiple elementary faults at the same location, multiply their Pauli assignments, or XOR record flips. Clifford propagation and all detector/observable effects are linear modulo two, and the full menu contains the product. Two entries become one if the product is nonidentity and disappear if it is identity. Repetition removes every collision and strictly reduces any colliding multiset’s count. Hence

```text
minimum elementary-fault multiset count
 = minimum nonidentity occupied-location count.
```

A minimum cannot contain a collision. Locations in different round copies are distinct, so weights of configurations split across disjoint round sets add exactly. The argument would fail for a menu not closed under multiplication or for Pauli-dependent costs; the claim properly excludes those variants.

### 3.5 Canonical distance and aggregation

In one memory sector, let `V` be the vector space of deterministic fault-free parities of all relevant records and terminal readout bits while the logical basis label ranges over all basis states. Definition 3.5 sets

```text
D_can = kernel(logical-label dependence on V).
```

A fault is canonical-undetectable when it flips no parity in `D_can`. It is logical when its designated terminal logical-readout vector in `F_2^k` is nonzero. Define

```text
d_R^Z = min weight of a canonical-undetectable logical in C_R^Z,
d_R^X = min weight of a canonical-undetectable logical in C_R^X,
d_R   = min(d_R^Z,d_R^X).
```

The X-memory definition is the direct §8.1 mirror of Definition 3.5. Definition 2.7 is used only through the value bridge proved in §5; the detector sets themselves are not claimed equal.

For a configuration `F`,

```text
supp_t(F)={r : a location of round r is occupied},
span(F)=max supp_t(F)-min supp_t(F)+1.
```

A logical has nonempty support. “Supported on a contiguous interval” means every integer round between the minimum and maximum belongs to `supp_t(F)`.

## 4. Independent derivation of the boundary equation

It suffices to derive Z-memory. The equality `c_ab=c'_ab` makes every step mirror-valid.

### 4.1 CSS sector projection and record preservation

Define the locationwise projection `Pi_X` of a full-Pauli configuration:

- keep only the X component at Pauli locations;
- keep classical flips of Z-check records;
- erase the Z components and flips of X-check records.

Because every local Pauli group is available, the retained component is legal at the same location. An occupied Y may become X, an occupied Z may become identity, and no identity becomes occupied, so

```text
|Pi_X F|<=|F|.
```

Under a CNOT,

```text
X_c -> X_c X_t,     X_t -> X_t,
Z_c -> Z_c,         Z_t -> Z_c Z_t.
```

X and Z components propagate independently. Therefore `Pi_X` preserves exactly the Z-check record effects and terminal Z-readout effects relevant to Z-memory, including the `k`-component logical vector. It erases all X-check record effects. The mirror `Pi_Z` has the corresponding X-memory properties.

This proves more than a numerical CSS reduction: if `F` is a canonical minimum, its projected witness remains logical and canonical-undetectable once the detector decomposition in §5 is established. Weight cannot fall strictly because that would contradict minimality; hence the representative has the same weight.

### 4.2 Round transparency

An incoming data-X error on qubit `q` is a target error for each X-check CNOT `anc(a)->q`, so it remains on data and does not propagate to that ancilla. It is a control error for each Z-check CNOT `q->anc(b)`, so it remains on data and flips the target ancilla. A fault-free round therefore:

1. preserves the entire incoming data-X vector `E`;
2. adds exactly `H_Z E` to the vector of Z-check records.

Fresh ancillas reset every other inter-round degree of freedom. This is the physical reason the boundary state can be represented by a syndrome prefix alone.

### 4.3 One-round effects

For a sector-pure location assignment `f` in the abstract one-round block, define

```text
E(f)   in F_2^n  = residual data-X vector after the round,
s(f)   in F_2^B  = H_Z E(f),
u(f)   in F_2^B  = extra same-round Z-record flip,
ell(f) in F_2^k  = logical pairing of E(f).
```

For all assignments in physical round `r`, sum linearly:

```text
e_r   = sum_f E(f),
s_r   = H_Z e_r,
U_r   = sum_f u(f),
ell_r = sum_f ell(f).
```

Verbatim repetition makes this dictionary independent of `r`. The occupied-location formulation is compatible with the sums because each occupied location contains one group element and Clifford propagation is linear.

A single fault in round `r` has full-boundary detector column

```text
[u(f)]_r + [u(f)+s(f)]_(r+1).                 (4.1)
```

To see this, its extra current-record error contributes at boundary `r`; the persistent data residual adds `s(f)` to every later real record and to the terminal virtual record. Adjacent detector differences cancel that constant tail everywhere after `r+1`. Formula (4.1) also covers `r=0` because the preceding virtual record is fixed to zero, and `r=R-1` because coordinate `R` is the terminal data parity.

### 4.4 Prefix equation `(W)`

Set

```text
C_t=sum_{i=0}^t s_i,        C_t=0 for t<0,
U_R=0.
```

The erroneous part of the Z-check record at real round `t` is

```text
y_t=C_(t-1)+U_t,            0<=t<=R-1,
```

and the terminal virtual record error is

```text
y_R=C_(R-1).
```

With `y_(-1)=0`, boundary detector `t` has error `y_t+y_(t-1)`. All boundary detectors vanish precisely when the sequence

```text
y_(-1),y_0,...,y_R
```

is constant. The absolute left boundary fixes the constant to zero. Thus full-boundary undetectability is equivalent to

```text
U_t=C_(t-1),                t=0,...,R,          (W)
```

with `U_R=0`. The last equation is not a harmless convention; it yields terminal closure

```text
C_(R-1)=0.                                      (4.2)
```

Extend `U_t` by zero outside the physical circuit. Before the first occupied round, `C=0`; after the last occupied round, (4.2) makes `C=0`. Hence `(W)` may be read over every integer index when translating a closed configuration.

The terminal data error is

```text
E_tot=sum_r e_r,
```

and the logical vector is

```text
ell(F)=sum_r ell_r in F_2^k.
```

It depends on the residual sum, not on where the round assignments occur.

## 5. Canonical Definition 3.5, its mirror, and Definition 2.7

### 5.1 Canonical decomposition

Represent a Z-type deterministic parity by `(beta,gamma)`: `beta` selects Z-check records and `gamma in F_2^n` selects terminal Z-readout bits. Direct backward propagation through the schedule gives two conditions.

Measurement consistency cancels within-round X/Z crossing terms, and CSS commutation cancels the remaining inter-round crossing terms. A selected terminal vector yields a deterministic parity exactly when

```text
H_X gamma=0.
```

No restriction remains on `beta`. Therefore the deterministic Z-type parity space is

```text
V_Z={(beta,gamma): gamma in ker(H_X)}.          (5.1)
```

Changing the prepared logical Z-basis label changes this parity by the logical pairing of `gamma`. The value is independent of every label exactly when `gamma` represents no Z logical, namely

```text
gamma in S_Z=row(H_Z).
```

Therefore

```text
D_can,Z={(beta,gamma): gamma in S_Z}.           (5.2)
```

The full-boundary differences span (5.2). For `r<R`, their triangular record-incidence matrix spans all `beta` with `gamma=0`: start from the absolute `r=0` differences and eliminate chronologically. A terminal difference at `r=R` supplies `gamma` equal to the support row of `b`; subtracting already-spanned record coordinates leaves that row. Varying `b` spans `S_Z`. Hence

```text
D_can,Z=span{D_(b,r): b in B, 0<=r<=R}.         (5.3)
```

The deterministic X-record parities form a complementary canonical summand `D_can,X`. They have no dependence on the prepared Z-memory logical label. With dependent X-check rows, `D_can,X` includes round-zero redundancy parities that the short Definition-2.7 difference list omits. Thus the full canonical detector space is

```text
D_can^Z=D_can,Z ⊕ D_can,X,                      (5.4)
```

whereas the Definition-2.7 span is generally a proper subspace. This is why set equality must not appear in the claim.

The same derivation with X and Z exchanged proves the section-8.1 mirror. The reference to Definition 3.5 is stable enough for the exact claim: it names the transfer proof dossier and the mirror section, while the claim also states the value-only relationship to Definition 2.7. More importantly, this proof derives (5.1)-(5.4) rather than importing the transfer theorem.

### 5.2 Equality of the named distance values

Let `d_short^Z` denote the distance against the named Definition-2.7 set and `d_can^Z` the Definition-3.5 value. Since the short detector span is contained in the canonical span,

```text
d_short^Z<=d_can^Z.                              (5.5)
```

Choose a minimum short-undetectable logical `F` and project it to `F'=Pi_X F`.

- The projection preserves all Z-check boundary effects and the logical vector.
- Thus `F'` annihilates `D_can,Z`, which is exactly the full-boundary span (5.3).
- It has no X-check record effect, so it annihilates all of `D_can,X`, including dependent-row redundancy directions absent from the short list.
- Its weight is at most `|F|`.

It follows that `F'` is a canonical-undetectable logical of no greater weight, so

```text
d_can^Z<=d_short^Z.                              (5.6)
```

Equations (5.5)-(5.6) prove equality of values. The X-memory projection proves the mirror equality.

Now begin instead with an arbitrary canonical minimum `F`. The same projection is a canonical-undetectable logical and cannot have smaller weight than a canonical minimum. Together with `|Pi_X F|<=|F|`, this forces

```text
|Pi_X F|=|F|.
```

Therefore every canonical minimum has a same-weight sector-pure representative. This witness-level fact supplies the exact quantifier in the claim.

The argument does not establish arbitrary detector-split invariance. In the recorded redundant-row Steane test, adding a mixed parity `P_X+lambda` to another admissible-looking complement changes the distance from 2 to 3 at `R=2` and to 4 at `R=3`, while the canonical value stays 2. The proposed claim correctly names only the proven pair.

## 6. Witness maps and monotonicity

Fix Z-memory and let `F` be a canonical minimum in `C_R^Z`. Replace it by the same-weight X-sector-pure representative just proved.

### 6.1 Append map

Embed its assignments at the identical named locations of rounds `0,...,R-1` in `C_(R+1)^Z`, and leave every location of new physical round `R` at identity. Verbatim repetition makes this an exact location map, not an analogy.

Check `(W)` at every enlarged boundary:

1. At `t=0`, the absolute detector and `U_0=C_(-1)=0` are unchanged.
2. At `1<=t<=R-1`, every `U_t` and prefix `C_(t-1)` is unchanged.
3. At `t=R`, the old circuit used its terminal equation `0=C_(R-1)`. The new circuit uses a real but fault-free round record. Round transparency says its error is the same `C_(R-1)`, so it vanishes.
4. At `t=R+1`, the new round adds neither residual nor record fault, so `C_R=C_(R-1)=0=U_(R+1)`.

The residual sum, logical vector, and occupied-location weight do not change. Sector purity plus (5.4) gives canonical undetectability. Therefore

```text
d_(R+1)^Z<=d_R^Z.                                (6.1)
```

### 6.2 Prepend map

The left boundary needs a separate check. Shift every assignment from round `r` to `r+1` and leave new round 0 fault-free. Then

```text
U'_0=0=C'_(-1),
U'_t=U_(t-1),
C'_(t-1)=C_(t-2),          1<=t<=R+1.
```

Every later equation is an old equation shifted by one, including the terminal equation. Weight and logical parity are unchanged. Thus fault-free padding is valid at either end, which will permit arbitrary placement of a closed interval.

The mirror construction proves

```text
d_(R+1)^X<=d_R^X.
```

Taking sector minima gives

```text
d_(R+1)
 =min(d_(R+1)^Z,d_(R+1)^X)
 <=min(d_R^Z,d_R^X)
 =d_R.                                            (6.2)
```

This is the claimed monotonicity for every `R>=1`. The proof does not appeal to the false slogan that a longer circuit merely contains a shorter one: the old terminal record changes type and the detector space changes, which is why steps 3 and 4 are explicit.

## 7. Positive finiteness and the aggregate spatial ceiling

For each data qubit `q`, choose a named Pauli insertion after its last two-qubit gate in the round; if no such gate exists, choose its named idle location. The full menu includes an assignment whose only surviving component is X on `q`. Since there is no later interaction involving `q`, this assignment has

```text
E(f_q)=e_q,       u(f_q)=0.
```

Choose `v in ker(H_Z)\S_X` of weight `d_X`, put the assignments `f_q` for `q in supp(v)` in the final round, and leave all other locations at identity. All earlier prefixes are zero, the last-round extra record vector is zero, and the terminal syndrome is

```text
H_Z v=0.
```

The residual `v` has nonzero logical pairing. This constructs a Z-memory witness and proves

```text
d_R^Z<=d_X.                                      (7.1)
```

The mirror construction gives

```text
d_R^X<=d_Z.                                      (7.2)
```

Thus, and only thus,

```text
d_R=min(d_R^Z,d_R^X)
    <=min(d_X,d_Z)
    =d.                                          (7.3)
```

On an asymmetric CSS code, (7.1) does not imply `d_R^Z<=d`; nor does (7.2) imply `d_R^X<=d`. The later proof always selects a sector attaining the aggregate before applying (7.3).

The empty configuration cannot have a nonzero logical vector, so every distance is at least one. A finite circuit has finitely many locations and each location has a finite group, while (7.1)-(7.2) provide at least one logical witness. Therefore every minimum exists and

```text
1<=d_R<=d.                                      (7.4)
```

The nonincreasing integer sequence `(d_R)` takes values in the finite set `{1,...,d}`. It can strictly decrease at most `d-1` times, so it is eventually constant. This proves

```text
d_infinity=lim_{R->infinity}d_R=min_{R>=1}d_R,
1<=d_infinity<=d.                               (7.5)
```

This existence proof is where `k>=1` is indispensable.

## 8. Gap splitting and contiguous representatives

Take an arbitrary canonical minimum `F` in one memory sector. In Z-memory let `G=Pi_X F`. It is canonical-undetectable and logical with

```text
|G|=|F|=d_R^Z.
```

Collision removal ensures no location is counted twice.

Suppose `G` has an internal empty physical round `g`, with occupied rounds on both sides. Write

```text
G_L = assignments in rounds r<g,
G_R = assignments in rounds r>g.
```

The gap gives `U_g=0`. Applying `(W)` to the full configuration at that index yields the decisive zero-charge equation

```text
C_(g-1)=0.                                      (8.1)
```

### 8.1 The left half closes independently

For `t<=g`, the right half has no current assignment or earlier residual, so the left-half equation is the full equation. For `t>g`, the left half has no current record flip and its cumulative syndrome is frozen at the value (8.1), namely zero. Thus `G_L` satisfies `(W)` at every boundary, including the original absolute left boundary and the original terminal boundary.

### 8.2 The right half closes independently

For `t<=g`, the right half has neither current faults nor earlier residual, so its two sides of `(W)` are zero. For `t>g`, its current `U_t` equals the full configuration’s value, and its syndrome prefix equals the full prefix because the entire left contribution has closed to zero at (8.1). Thus `G_R` also satisfies every boundary equation.

Each half is sector-pure, so the canonical decomposition upgrades its full-chain undetectability to all canonical detectors. Logical parity is a vector:

```text
ell(G)=ell(G_L)+ell(G_R) != 0 in F_2^k.          (8.2)
```

If both half-vectors were zero, their sum would be zero; therefore at least one half is logical. Both halves contain an occupied location and their location sets are disjoint, so that logical half has strictly smaller weight than `G`. This contradicts minimum weight.

Consequently `supp_t(G)` contains no internal gap. Every round in its span contains at least one distinct occupied location, so

```text
span(G)=|supp_t(G)|<=|G|.                        (8.3)
```

The mirror proves the same statement for every X-memory minimum. The quantifier is exact: every original minimum has a projected same-weight representative with the property. The proof does not claim that every full-Pauli minimum itself is sector-pure or preserves irrelevant opposite-family record flips.

## 9. Translation and deletion of exterior zero rounds

Let a closed sector-pure logical `F` be supported in `[a,b]`, with

```text
w=b-a+1.
```

For a shift `delta` that places `[a+delta,b+delta]` inside physical rounds `0,...,R'-1`, copy each assignment to the corresponding named location of the shifted round. Its one-round dictionary is unchanged. In the all-integer form of `(W)`,

```text
U'_t=U_(t-delta),       C'_t=C_(t-delta).        (9.1)
```

Before the shifted support both values vanish because there is no preceding fault. After the support, the cumulative syndrome vanishes because the original configuration obeyed terminal closure. Therefore every translated detector equation, including the two newly created temporal boundaries at the left and right of the support, is an old zero equation with shifted index.

The occupied-location count and residual sum do not change, so the logical vector is preserved. Sector purity again supplies every canonical detector. In particular, choose `delta=-a` and `R'=w`: leading and trailing zero-fault rounds are deleted, and the support becomes physical rounds `0,...,w-1` with closing detector at boundary `w`.

The requirement `R'>=w` is exact. Translation never cuts through a nonzero boundary state and never removes an internal fault-free round unless §8 first proves its charge zero and selects a closed half.

## 10. Finite-window equality

Let `R>=d`. Choose a sector that attains the aggregate value `d_R`, choose a canonical minimum in that sector, and replace it by the contiguous sector-pure representative `F`. Equations (7.3) and (8.3) give

```text
span(F)<=|F|=d_R<=d.                             (10.1)
```

Translate `F` into the `d`-round experiment. It remains a canonical-undetectable logical of weight `d_R`, hence

```text
d_d<=d_R.                                       (10.2)
```

Monotonicity, because `R>=d`, gives

```text
d_R<=d_d.                                       (10.3)
```

Therefore

```text
d_R=d_d for every R>=d.                         (10.4)
```

Together with eventual constancy,

```text
d_R=d_d=d_infinity for every R>=d.              (10.5)
```

This proof never needs `d_R^Z<=d` or `d_R^X<=d`. The asymmetric case `d_X!=d_Z` is handled because (10.1) is invoked only after choosing the aggregate-attaining sector.

## 11. Minimal stabilization index and first-`d` determination

Let

```text
S=R_stab
 =min{R_0>=1 : d_R=d_infinity for every R>=R_0}.
```

Equation (10.5) proves that the set is nonempty and `S<=d`. Choose an attaining-sector minimum at `R=S` and its contiguous representative `F`; put `w=span(F)`. Then

```text
w<=|F|=d_S=d_infinity.                          (11.1)
```

Because the witness lies in `S` physical rounds, `1<=w<=S`. If `w<S`, translate it into `C_w`. This gives `d_w<=d_infinity`; the definition of `d_infinity` as the global minimum gives the reverse inequality, so `d_w=d_infinity`. Monotonicity and the global lower bound then force `d_R=d_infinity` for every `R>=w`, contradicting minimality of `S`. Hence `w` cannot be smaller than `S`. Therefore `w=S`, and (11.1) yields

```text
R_stab<=d_infinity<=d.                          (11.2)
```

Since `(d_R)` is nonincreasing and constant from `d` onward,

```text
d_infinity=d_d,
R_stab=min{R in {1,...,d}: d_R=d_d}.             (11.3)
```

Thus `d_1,...,d_d` determine both quantities.

### 11.1 Off-by-one and edge-case audit

- `R=1`: physical support is `{0}` and detector boundaries are `{0,1}`. `(W)` reads `U_0=0` and `0=C_0`, exactly the one-round undetectability conditions. Append and prepend both create a genuine second physical round and third boundary.
- `d=1`: the spatial witness has one occupied location, (10.5) applies from `R=1`, and `R_stab=d_infinity=1`. The “first `d`” list contains exactly `d_1`.
- A span of `w` occupies shifted rounds `0,...,w-1`; terminal closure is tested at boundary `w`. There is no `w+1` shift in the theorem.
- A gap index `g` is a physical round strictly between the support extrema. The left half uses rounds `<g`; the right half uses rounds `>g`; no assignment is lost because round `g` is empty.
- Dependent check rows enlarge the canonical opposite-family summand but are annihilated by sector projection, so no rank-independence assumption enters.
- For `k>1`, equation (8.2) is vector addition. It is enough that one half vector be nonzero; no particular logical coordinate is fixed in advance.
- Same-location collision removal precedes the inequality `span<=weight`, ensuring an occupied round contributes at least one distinct occupied location.
- The mirror proof uses `c'_ab=c_ab`; it does not assume measurement consistency independently a second time.

## 12. Adversarial review and independent corroboration

### 12.1 Counterexample attempts and resolutions

| Attempted failure | Audit result |
|---|---|
| `k=0` code | **Found a real exact-claim defect.** The 1,210-character claim omits `k>=1`; repaired in Finding F-CLAIM. |
| Conflict-free but measurement-inconsistent schedule | Standard check records need not be deterministic. Such layouts are excluded explicitly; no conflict-only theorem is licensed. |
| X-memory has a different ordering condition | Rejected by the exact parity identity `c'_ab=c_ab` for even CSS overlaps. |
| Change the layout as `R` changes | Append/translation maps cease to exist. Exact claim now says verbatim repetition; cross-boundary compression remains out of scope. |
| Drop initial detector | Prefix history may equal a nonzero constant; gap closure fails. Ideal absolute initialization is load-bearing. |
| Drop terminal detector | Total syndrome may remain open; right translation leaks. Ideal terminal readout is load-bearing. |
| Append a zero round without handling the old terminal record | Invalid shortcut. The proof separately checks old-terminal/new-interior and new-terminal boundaries. |
| Prepend only by analogy with append | Invalid shortcut. §6.2 checks the absolute left boundary separately. |
| Full-Pauli minimum uses Y or irrelevant components | `Pi_X/Pi_Z` removes irrelevant components at no higher weight and preserves the designated sector. Minimum weight forces equality. |
| Dependent stabilizer rows | Definition-2.7 and canonical detector sets differ. Sector projection annihilates the omitted redundancy parities, giving value equality without set equality. |
| Same-location collision | Full local group multiplication preserves all effects and lowers count. A minimum has no collision. |
| Nonuniform or non-group fault menu | Collision and projection may fail. Exact claim does not cover it. |
| Empty middle round with nonzero incoming syndrome | A fault-free round alone is not deletable. Undetectability first forces `C_(g-1)=0`; only then do both halves close. |
| Logical cancellation between halves | The parity is a vector in `F_2^k`; a nonzero sum implies at least one nonzero half. |
| Asymmetric code `d_X!=d_Z` | The proof uses only aggregate `d_R<=min(d_X,d_Z)`. It never asserts the false per-sector minimum bound. |
| Arbitrary detector split | Recorded `D'` changes values. The exact claim confines the bridge to Definition 3.5/§8.1 and Definition 2.7 in value only. |
| `R=1` or `d=1` | Both boundary equations and the first-window formula remain well-defined; §11.1 checks indices. |
| Stabilization off by one | A `w`-round interval occupies `0,...,w-1` and closes at detector `w`; contradiction uses `C_w`, not `C_(w+1)`. |
| Circular use of this node | None found. The direct derivation never assumes window monotonicity, contiguity, stabilization, or finite-window equality. |
| Illicit use of transfer/instances/root | None found. Only an explicit detector definition and its ratification are used as model provenance; their theorem conclusions are not imported. |

### 12.2 Exhaustive scalar boundary audit

I wrote `/tmp/circdist_sat_window_exact_review_20260826_r51/audit.py` outside the repository. It had 228 lines, 8,236 bytes, and SHA-256

```text
30f58d26c33733fef8b59217574b397881a5638f9953980f559939d9b6727de7
```

It exhaustively considered all 98 dictionaries with one through four distinct nonzero effects `(s,u,ell) in F_2^3`, all bitmask configurations for `R=1,...,4`, and every closed logical. It checked:

- all minimum supports for contiguity and `span<=weight`;
- append and prepend maps;
- deletion/translation into the exact support span;
- every internal-gap split and the fact that some half stays logical;
- monotonicity;
- the first-`d` tail and `R_stab<=d_infinity` wherever the four-round horizon sufficed;
- the exact `R=1` equations;
- mirror stability for overlaps 0, 2, 4, and 6;
- all products of nonidentity elements in toy one- and two-qubit Pauli bit groups;
- every nonzero sector projection in those groups;
- an asymmetric CSS matrix pair;
- a dependent-row Steane dimension check.

The complete successful output was:

```text
dictionaries_tested 98
finite_R_cases 328
logical_closed_configurations 44200
append_checks 5952
prepend_checks 5952
translation_checks 44200
gap_split_checks 3708
R1_equivalence_checks 938
mirror_stability_checks 85
collision_group_pairs 234
sector_projection_menu_checks 18
violations 0
drop_examples 2
drop (((0, 1, 0), (1, 0, 0), (1, 1, 1)), (3, 2, 2, 2))
drop (((0, 1, 0), (1, 0, 1), (1, 1, 0)), (3, 2, 2, 2))
stabilization_rows_checked 76
asymmetric_dX_dZ_d 3 2 2
asymmetric_min_X_vectors ['010101', '010110', '011001', '011010', '100101', '100110', '101001', '101010']
asymmetric_min_Z_vectors ['000011', '001100', '110000']
dependent_leftker_short_canonical_dims 1 13 14
```

The asymmetric test used

```text
H_X={000011,001100,110000},
H_Z={001111,111100}.
```

Every X/Z row overlap is even. Direct enumeration gives `d_X=3`, `d_Z=2`, and `d=2`, confirming that a sector ceiling and the aggregate ceiling are different statements.

For the dependent-generator test, a three-row Steane matrix was enlarged by the sum of its first two rows. Rank remains three and the left-kernel dimension becomes one. At `R=2`, the modeled short detector dimension is 13 while the canonical dimension is 14, exactly the missing redundancy direction predicted by §5.

### 12.3 Vector logical-parity audit

The first script uses one logical bit. I therefore wrote a second independent enumeration, `/tmp/circdist_sat_window_exact_review_20260826_r51/vector_audit.py`, with 52 lines, 1,708 bytes, and SHA-256

```text
027f22daee46932cfd2d154bd2af611f89703fdbaa7239be789a47526f029782
```

It allowed `ell in F_2^2`, used every dictionary of one through three distinct nonzero `(s,u,ell)` effects, and checked all configurations through three rounds. Its final output was:

```text
vector_dictionaries_tested 575
vector_valid_logicals_checked 16158
vector_minima_checked 3756
vector_gap_splits_checked 630
vector_violations 0
```

The first version of this script examined only minima and happened to encounter zero minimum configurations with gaps. That was inadequate to exercise the split. I broadened it to every valid logical configuration; the corrected version checked 630 gap splits. This correction and both versions’ execution appear in the FIX-2 ledger.

### 12.4 Physical-layout adversarial audit

The proof is uniform over the within-round layout: once conflict legality and measurement consistency hold, layout dependence is completely captured by the finite one-round effects `(E,s,u,ell)`. I nevertheless checked the layout-sensitive failure modes against the earlier theorem/amendment tables.

- Z-block-first and X-block-first schedules exchange the relative CNOT order. The equation `c=c'` proves the same legal domain in both memories; no schedule-specific symmetry is assumed.
- The earlier 18-row tests cover Steane, rotated `[[9,1,3]]`, and Steane with a dependent X generator, for `R=1,2,3` and both noninterleaved block orders. Their ranks agree with the analytic canonical decomposition when the dependent-row correction is included. I checked those formulas and the reported missing redundancy direction independently; they are corroboration, not a premise.
- The earlier review’s additional legal measurement-consistent interleaved schedules in both memories exercise hook orderings. The present proof does not infer a family law from them; it uses only the one-round dictionary.
- Cross-round idle compression is an actual excluded layout transformation. It can change the location set and one-round dictionary when `R` changes, so neither append nor translation is defined. The exact word `verbatim` closes this attack. Within-round compression performed once before freezing `M` remains allowed.
- A data fault inserted after the final gate on its qubit exercises the schedule’s latest temporal location and proves the spatial ceiling regardless of whether that last gate is X-check or Z-check oriented.

No finite layout sample could establish the universal theorem. The boundary derivation supplies that proof; the layout cases check that its hypotheses are neither vacuous nor silently stronger.

### 12.5 Computation status

Both programs are exact finite enumerations with no random sampling, but I treat them only as corroboration. Their abstract dictionaries include effects that may not arise from a physical CSS layout, and their finite horizons cannot prove the universal statement. The mathematical license rests on §§3-11.

## 13. Premises, imports, and circularity audit

### 13.1 What is imported

The proof uses the following external material:

1. the frozen CSS circuit and ideal-boundary model;
2. the project decision that the canonical detector split is Definition 3.5 and that X-memory uses its §8.1 mirror;
3. the explicit local Pauli menus and unit occupied-location cost;
4. elementary CSS linear algebra and Clifford CNOT propagation.

Items 1-3 are definitions or ratified scope, not unproved mathematical conclusions. This review re-derived their mathematical consequences. Item 4 is displayed and checked directly in §§3-5.

The transfer dossier is used as a stable locator for the detector definition. Its BCOQ theorem, transfer identities, or completion status are not used. The instances artifact, its finite certificates, the prior window claim, and the root route are not used at all in the derivation.

### 13.2 Definition 3.5 stability

The exact claim’s phrase “the canonical detector space of Definition 3.5 in the `CIRCDIST.sat.transfer` proof dossier and its section-8.1 mirror” resolves to one current artifact and one explicit mirror section. The transfer amendment lead-ratifies that choice and expressly rejects arbitrary detector-split invariance. The V3 exact-text review independently records the same stable locator and value-only bridge. There is no ambiguous version number or implicit complement choice.

A future relocation of the dossier would require a textual migration, but that is ordinary reference maintenance. At review time the locator is sufficiently stable and self-contained because:

- the claim states which two sectors and which relationship to Definition 2.7 are intended;
- this report and the authored proof reproduce the defining kernel condition;
- the proof derives the full canonical decomposition and does not ask the reader to trust a transfer theorem.

### 13.3 Premise levels

No unresolved claim node is a load-bearing premise. Frozen definitions and the ratified scope are available at their required model-definition level. The authored proof is complete evidence and this report supplies the fresh independent adversarial review required for `PROVED`. Historical reviews at the old claim hash corroborate portions of the argument but are not counted as completion reviews for the new hash.

I found no circular import from `CIRCDIST.sat.window`, no use of `CIRCDIST.sat.instances` to prove the window it depends on, and no use of the root’s conditional route to prove one of its premises.

### 13.4 Mathematical completion verdict

For the exact 1,261-character claim and no broader model, every conclusion follows from independently checked definitions and finite derivations:

```text
per-sector monotonicity
=> aggregate monotonicity
+ finite positive aggregate ceiling
=> existence of d_infinity;
projection + (W) + zero-gap split
=> same-weight sector-pure contiguous representative;
translation + aggregate d ceiling
=> d_R=d_d=d_infinity for R>=d;
minimality of R_stab + span<=weight
=> R_stab<=d_infinity<=d;
monotonicity
=> first-d determination.
```

**Mathematics: PASS. Exact corrected claim: PASS. Required node level after installation: PROVED.**

## 14. Exact dispatcher installation contract

The dispatcher alone may install this contract. Each item is independently licensed only as part of the exact claim replacement; no old or alternative claim hash may be paired with this review.

### 14.1 Claim and assessment

Install the exact scalar from Finding F-CLAIM and verify:

```text
length: 1261
reviewed_hash: sha256:6c50b4049ae908d6646e87f7446f8fb7ea9583182fb79da3cb6b935c7011ccc4
```

Set:

```yaml
assessment:
  level: PROVED
```

This level is licensed because the corrected exact claim is completely proved by the authored artifact and independently checked here, with no unresolved load-bearing theorem premise.

### 14.2 Exact caveats

Replace the obsolete completion-blocking caveats with exactly:

```yaml
caveats:
- 'W-P1: PROVED is confined to CSS codes with k >= 1 and the exact stated model: conflict-free and measurement-consistent
  single-ancilla extraction, ideal initialization and terminal data readout, verbatim round blocks with no cross-round compression,
  uniform unit-cost full Pauli groups at every named fault location, and the Definition-3.5 canonical detector space with
  its section-8.1 mirror.'
- 'W-P2: The spatial ceiling used by the proof is aggregate: d_R = min(d_R^Z,d_R^X) <= min(d_X,d_Z). No per-sector inequality
  d_R^sigma <= min(d_X,d_Z) is asserted or used; asymmetric CSS codes can violate it.'
- 'W-P3: Tightness of R_stab <= d_infinity, the fitted hook-misaligned family law, arbitrary detector-split invariance,
  nonuniform or non-group fault costs, and layouts with cross-round compression are outside this claim.'
```

These caveats preserve the actual model limits. Old caveats remain recoverable in history and appended events; they should not remain as live blockers after the exact repair and review.

### 14.3 Exact summary

Install exactly:

```yaml
summary: Fresh independent end-to-end review verifies the direct boundary-equation proof of the exact repaired standalone
  claim at PROVED. The proof covers both CSS sectors, dependent generators, the named canonical detector split, collision-free
  occupied-location weight, all temporal boundaries, asymmetric code distances, contiguous representatives, the aggregate
  d-window, and the minimal stabilization index. It imports no unresolved theorem or premise. Stronger tightness and family-law
  questions remain outside the claim.
```

### 14.4 Reviews and evidence

The two current `assessment.basis.reviews` entries bind the old hash

```text
sha256:8698b051b15fa14ff669299580d9b7bfec01808c0a34133ef09264e749466146
```

and lapse as current completion bindings when the claim changes. Do not edit or delete their report files. Their existing duplicate entries under `basis.evidence`, marked as historical event sources, remain valid history.

Replace the current reviews array by exactly:

```yaml
reviews:
- path: circdist/reviews/circdist_sat_window_selfcontained_exact_review_20260826.md
  kind: review
  scope: Fresh strict-serial independent audit of the complete 1,154-line authored proof and exact standalone serialization,
    including all model definitions, both CSS sectors, canonical-versus-Definition-2.7 value bridge, dependent generators,
    boundary maps, gap splitting, asymmetric distances, hashes, counterexample attacks, and protocol install consequences;
    computations were used only as corroboration.
  locator: Finding F-COMPLETION
  reviewed_hash: sha256:6c50b4049ae908d6646e87f7446f8fb7ea9583182fb79da3cb6b935c7011ccc4
```

Retain every current evidence entry. For the already-listed authored proof, use:

```yaml
- path: circdist/artifacts/circdist_sat_window_selfcontained_exact_proof_20260826.md
  kind: text
  scope: Complete authored proof and standalone-claim audit for the intended current model; proposes an exact precision
    repair and expressly withholds self-certification pending fresh independent review.
  locator: Sections 0-16
```

Add these four provenance/corroboration entries:

```yaml
- path: circdist/artifacts/circdist_sat_transfer_proof_20260823.md
  kind: text
  scope: Definition 3.5 source, canonical-space decomposition, and section-8.1 mirror used only as model-definition provenance;
    the transfer theorem core is not imported.
- path: circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md
  kind: text
  scope: Lead-ratified Definition-3.5 scope and the corrected rejection of arbitrary detector-split invariance.
- path: circdist/reviews/circdist_transfer_bridgefold_20260823.md
  kind: text
  scope: Prior independent calibration of the named detector-value bridge, dependent-generator case, collision bridge,
    and alternate-split counterexample; corroborating evidence re-derived in the present review.
- path: circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md
  kind: text
  scope: Prior exact audit establishing the stable Definition-3.5/section-8.1 locator and value-only relationship to Definition
    2.7.
```

The new review file is the only completion review for the new hash. Authored proof, old reviews, and calibration reports are evidence, not substitute exact-hash bindings.

### 14.5 Exact frontier

Close/remove the live `selfcontained-proof-review` task because this report completes it. Replace it with:

```yaml
frontier:
  stabilization-tightness:
    task: Determine whether R_stab(M) <= d_infinity(M) is attained within the exact proved model, or prove a sharper universal
      bound; keep any fitted schedule-family law in a separate claim.
    kind: task
    since: '2026-08-26'
```

This does not reopen the proved window theorem. It records only a stronger question outside the claim.

### 14.6 Exact append-only events

Append, without modifying any earlier event:

```yaml
selfcontained-claim-scope-repaired-2026-08-26:
  date: '2026-08-26'
  type: repair-applied
  summary: Replaced the 489-character shorthand claim by the exact 1,261-character standalone serialization. The repair
    makes explicit k >= 1, conflict legality plus measurement consistency, verbatim repetition, min-over-sectors aggregation,
    the uniform full-Pauli occupied-location model, the named canonical detector spaces, same-weight sector-pure representatives,
    and d = min(d_X,d_Z). It preserves the proposition proved by the prior window dossier; old claim-review hashes remain
    historical evidence and do not bind the new claim.
  sources:
  - path: circdist/reviews/circdist_sat_window_selfcontained_exact_review_20260826.md
    kind: review
    locator: Finding F-CLAIM
selfcontained-proof-reviewed-2026-08-26:
  date: '2026-08-26'
  type: review-completed
  summary: Fresh independent strict-serial review checked the complete direct proof and the exact repaired claim, including
    all load-bearing algebra, adversarial boundary cases, asymmetric CSS codes, and protocol bindings.
  sources:
  - path: circdist/reviews/circdist_sat_window_selfcontained_exact_review_20260826.md
    kind: review
    locator: Finding F-COMPLETION
window-proved-2026-08-26:
  date: '2026-08-26'
  type: level-change
  from: CERTIFIED*
  to: PROVED
  summary: Promoted CIRCDIST.sat.window after the exact repaired claim and every load-bearing input passed fresh independent
    adversarial review. No downstream node or route level changed by inheritance.
  sources:
  - path: circdist/reviews/circdist_sat_window_selfcontained_exact_review_20260826.md
    kind: review
    locator: Finding F-COMPLETION
```

The event keys are new and dates are current. Old events and pre-protocol history remain immutable.

### 14.7 Field-by-field dispatcher matrix

| Canonical field | Action licensed | Exact constraint |
|---|---|---|
| `id`, `role`, `aliases` | Keep | No semantic change |
| `claim` | Replace | Exact 1,261-character string; hash `6c50...ccc4` |
| `assessment.level` | Replace | `PROVED` |
| `assessment.caveats` | Replace | Three W-P strings in §14.2 |
| `assessment.summary` | Replace | Exact paragraph in §14.3 |
| `assessment.basis.evidence` | Retain and extend | Retain all; use authored-proof scope and add four entries in §14.4 |
| `assessment.basis.reviews` | Replace | One new review entry with exact hash |
| `frontier` | Replace completed task | One `stabilization-tightness` task |
| `events` | Append | Three keys in §14.6; no deletion/rewrite |
| generated views | Regenerate | Never hand-edit |
| scheduler | No change | Dispatcher scheduling is outside this review |
| downstream nodes/routes | No direct change | Fresh adjudication required, §15 |

### 14.8 Candidate serialization test

I built a candidate copy outside the repository at

```text
/tmp/circdist_sat_window_exact_review_20260826_r51/candidate
```

using exactly the fields above and a placeholder copy of this review path. YAML load/dump/load preserved the 1,261-character scalar and its normalized hash. The candidate passed the repository structural, closure, migration, prior-state-retention, and whitespace checks described in §16.

Scratch generated-view comparison predicted only these semantic view changes:

```text
NODE_INDEX: CIRCDIST.sat.window  CERTIFIED* -> PROVED
GRAPH: corresponding window node status label/mark updated
```

The dispatcher must regenerate from the installed canonical node and review; it must not copy scratch views.

## 15. Downstream consequences

### 15.1 `CIRCDIST.sat.instances`

The node remains `CERTIFIED*`. Its route `finite-prefix-window-closure` remains `CERTIFIED*`. Promotion of the sole premise changes neither level automatically.

The route implication was reviewed against the old shorthand window claim and has its own exact implication binding. The corrected window claim makes explicit `k>=1`, measurement consistency, verbatim repetition, the aggregate sector minimum, full-Pauli occupied-location weight, and the canonical detector pair. The three named instance schedules appear to satisfy those restrictions, but protocol requires the dispatcher or a fresh reviewer to re-adjudicate applicability against the **then-current exact premise text**. This report does not silently perform or install that downstream adjudication.

Even if applicability is confirmed, caveat `IW-C0` remains: the finite computations, witness replays, and mechanism exclusions have not acquired proof-quality independently checkable certificates merely because the window premise is now `PROVED`. The finite-certificate gate survives unchanged. No instance result, family law, or mechanism classification is proved by this review.

Required next work is therefore:

1. bind the route’s use of `CIRCDIST.sat.window` to the exact 1,261-character scope;
2. verify each selected schedule has `k>=1`, is measurement-consistent, uses verbatim uncompressed copies, and shares the named fault/detector model;
3. retain the route and node at `CERTIFIED*` unless the separate finite-certificate gate is discharged by an authorized review;
4. append any later route event rather than rewriting its historical review.

### 15.2 `CIRCDIST.sat` root

The root remains `CERTIFIED*`. Its conditional route `asymptotic-stability-assembly` is presently `PROVED`, but that is a proof of a conditional implication, not proof of its premises. After installation the premise levels would be:

```text
CIRCDIST.sat.transfer   CERTIFIED*
CIRCDIST.sat.window     PROVED
CIRCDIST.sat.instances  CERTIFIED*
```

Two premises remain below `PROVED`; the root cannot promote.

The root route and V3 review bind the current root claim/implication text and historically treat the window premise through its old shorthand. The corrected premise is narrower in its explicit domain, particularly `k>=1` and measurement consistency. Fresh route applicability adjudication must verify that the root’s quantification and every named instance lie inside that exact domain. The root claim itself still says `legal` without spelling out `k>=1`, measurement consistency, or the uniform group-cost model. A later exact precision audit may choose to align it; this report licenses no root text edit.

The conditional route’s old review does not become false history. It remains evidence that the implication was checked for the then-recorded premise. It may remain at its current level until the dispatcher applies protocol policy, but it must not be cited as a fresh exact binding to the replacement window text without re-adjudication.

### 15.3 No inheritance

This report licenses no edit to either downstream node, either downstream route, the scheduler, or their generated views. It does not promote or demote them by inheritance. The only licensed canonical mutation is the window-node contract in §14, followed by ordinary regeneration.

## 16. Validation and candidate-install checks

### 16.1 Canonical baseline

Before any candidate work, I ran the repository’s read-only baseline checks on the canonical tree. Results:

```text
python3 tools/proof_dag_check.py --problem circdist
  PASS: 16 canonical CIRCDIST nodes

python3 tools/proof_dag_check.py --problem all
  PASS: SE 85, KSUM 144, CIRCDIST 16

python3 tools/proof_dag_evidence_closure.py
  PASS: all 117 referenced evidence paths resolve

python3 tools/proof_dag_migration_check.py
  PASS: 16 CIRCDIST, 143 total canonical nodes, 728 migrated records

git diff --check
  PASS
```

These are structural checks, not mathematical evidence.

### 16.2 Scratch candidate

The candidate tree was outside the repository. After correcting the documented scratch setup issues in §17, it passed:

```text
python3 tools/proof_dag_check.py --problem circdist --write-generated
  PASS

python3 tools/proof_dag_check.py --problem all
  PASS

python3 tools/proof_dag_evidence_closure.py
  PASS: 118 referenced evidence paths

python3 tools/proof_dag_migration_check.py
  PASS

python3 tools/proof_dag_previous_state_check.py
  PASS

custom trailing-whitespace scan
  PASS
```

The evidence count increases from 117 to 118 because this review becomes a referenced path. Candidate testing used a placeholder scratch copy of the report only; it did not mutate the canonical repository and is not an installation result.

### 16.3 Limitations of this review

- I did not prove a sharper bound than `R_stab<=d_infinity`, establish physical tightness, or prove the fitted hook-misaligned family law.
- I did not extend the theorem to `k=0`, nonuniform costs, a non-group fault menu, faulty ideal boundaries, flags/cat ancillas, repeated incidences, a changing generator set, cross-round compression, or arbitrary detector splits.
- I did not rerun the large historical physical-circuit searches. I checked their load-bearing algebra and used fresh finite dictionary enumerations only as corroboration.
- I did not review the finite instance certificates to `PROVED`, transfer BCOQ theorem, or root assembly premises.
- I did not mutate or regenerate the canonical repository. Scratch success predicts what an authorized installation should validate; it is not proof that installation has occurred.

## 17. FIX-2 command, process, scratch, and mutation ledger

### 17.1 Execution model

This was one strict-serial reviewer session. I did not spawn a sub-agent or create/delegate another task. I used no browser, network client, solver service, compiler, detached process, or background job. Independent read-only shell invocations were occasionally submitted in one orchestration call and awaited with `Promise.allSettled`; each was a foreground child process, and every result was inspected.

Repository reads used the absolute canonical root

```text
<repo>
```

or that root as `workdir`. All scratch was confined to

```text
/tmp/circdist_sat_window_exact_review_20260826_r51
```

### 17.2 Complete command/process sequence

The following records every OS command or interactive OS process, in chronological phases. A bracketed list of `sed` ranges means separate awaited foreground invocations over the same file. Tool-only `write_stdin` transfers are listed because they fed an interactive process, although they did not start additional OS children.

#### A. Initial inventory and protocol/source reads

1. `pwd`, `git status --short`, and `rg --files | sed -n '1,240p'`.
2. Four parallel inventory searches over target/protocol/relevant artifact paths and authored-proof headings.
3. `cat DAG_PROTOCOL.md FILE_PROTOCOL.md` and three parallel initial proof chunks.
4. `sed -n '1,240p'`, `'239,480p'`, `'473,740p'`, and `'741,1018p'` on the authored proof.
5. `wc -l` and `shasum -a 256` over the proof and target materials.
6. Parallel `cat` reads of the current window, instances, root, transfer, and project metadata.
7. Full `cat` of `CIRCDIST.sat.instances.yaml`.
8. Full `cat` of `CIRCDIST.sat.yaml`.
9. Full reads of `CIRCDIST_PROBLEMS.md` and `SAT_RESCOPE_20260822.md`.
10. `rg` heading/locator searches in the earlier window theorem.
11. Sequential `sed` reads of the theorem at ranges `1-240`, `241-520`, `521-720`, and `721-932`.
12. Full reads of Window Amendment 1 and the earlier window review.
13. `sed` reads of `circdist_amendments4_review_20260822.md` at `1-300` and `300-544`.
14. `rg` locators in the transfer proof, followed by `sed` reads at `1-440`, `620-714`, and `1388-1485`.
15. `rg` locators in the transfer amendment, followed by `sed` reads at `1-280` and `960-1024`.
16. `sed` reads of `circdist_transfer_bridgefold_20260823.md` at `1-340` and `340-639`.
17. `rg` locators in the V3 exact review, the instances-window-edge review, recon, and lift materials.
18. Several `sed` reads then failed with “No such file or directory” because I guessed stale date suffixes (`20260816` for one amendment locator and `20260825` for V3/instances exact reviews). No file was created. I corrected this by running:
    - `rg --files | rg '(lift_iff_proof|lift_iff_amendment|lift_claimrepair|sat_recon)'`
    - `rg --files | rg '(v3.*exact|instances.*window.*edge|transfer.*amendment|bridgefold)'`
19. Corrected full/section reads of the lift IFF proof, lift amendment, lift claim-repair review, V3 exact review, instances-window-edge exact review, and recon.
20. Four further `sed` chunks covering the complete V3 review and `sed -n '300,691p'` on the instances-window-edge review.
21. `sed -n '1,150p'` and `rg` over the authored proof, followed by locator searches across lift/transfer/claim-repair sources.
22. Four additional proof segment reads plus `sed -n '520,760p'`, ensuring the mathematical body rather than only headings was read.
23. Re-reads of frozen definitions/rescope and `rg -n 'k *>= *1|k≥1|k > 0'` over all scope sources.
24. Full rereads of both protocols and current target/root nodes.
25. `rg` of transfer scope T0/T1 and prior window theorem scope.

#### B. Exact hashes and canonical baseline

26. A Python 3 heredoc using `yaml.safe_load`, UTF-8 encoding, `strip()`, `hashlib.sha256`, and dump/load round trips. It printed:
    - current length/hash `489 / 8698...6146`;
    - §12 length/hash `1210 / 301e...139`;
    - corrected length/hash `1261 / 6c50...ccc4`.
27. Five foreground baseline checks:
    - `python3 tools/proof_dag_check.py --problem circdist`
    - `python3 tools/proof_dag_check.py --problem all`
    - `python3 tools/proof_dag_evidence_closure.py`
    - `python3 tools/proof_dag_migration_check.py`
    - `git diff --check`
    All passed with the counts in §16.1.

#### C. Scratch creation and mathematical enumerations

28. An attempted shell command containing `rm -rf` for scratch initialization was rejected by the command safety layer **before any shell or OS process started**. It caused no mutation.
29. Safe replacement:
    - `test ! -e /tmp/circdist_sat_window_exact_review_20260826_r51`
    - `mkdir /tmp/circdist_sat_window_exact_review_20260826_r51`
30. A Python heredoc wrote `audit.py`; Appendix A reproduces its complete source with report-only line wrapping.
31. `python3 /tmp/circdist_sat_window_exact_review_20260826_r51/audit.py`; passed with the output in §12.2.
32. A Python heredoc wrote the first `vector_audit.py`; running it passed but reported zero gap splits because it examined only minimum configurations. I treated that as inadequate coverage, not affirmative evidence.
33. A second Python heredoc replaced `vector_audit.py` by the broader all-valid-logical version reproduced with report-only line wrapping in Appendix B.
34. `python3 .../vector_audit.py`; passed with 630 gap splits and output in §12.3.
35. `wc -l -c` and `shasum -a 256` on both scripts.
36. Read-only inspection of the current instances node.
37. A second independent Python literal-string hash check of the 1,261-character candidate.
38. `test`/status checks confirming that the final review path did not yet exist.

#### D. Deleted candidate install

39. A Python heredoc constructed `/tmp/.../candidate`, copied/symlinked the needed read-only repository structure, loaded the window YAML, inserted the exact fields of §14, and placed a scratch placeholder at the review path.
40. First `python3 tools/proof_dag_check.py --problem circdist --write-generated` in the candidate failed. The frontier task used the phrase “completed theorem”; the validator treats the token `completed` as forbidden completion language in a live task. I changed the task to the exact text in §14.5 and reran; it passed.
41. Parallel candidate checks:
    - `proof_dag_check.py --problem all`
    - `proof_dag_evidence_closure.py`
    - `proof_dag_migration_check.py`
    - `proof_dag_previous_state_check.py`
    - `git diff --check`
    The circdist-local checks passed. `--problem all` failed because the minimal candidate lacked SE/KSUM inputs. `git diff --check` failed because scratch was not a Git worktree, not because of content.
42. I added a read-only `research` symlink and reran `--problem all`; it still failed because root-level `artifacts` was absent. A custom trailing-whitespace scanner passed. In this combined shell invocation, the final scanner exited zero and therefore masked the earlier validator’s nonzero status at the wrapper level; I read the validator error in the output and did not count the batch as a pass.
43. I added the missing read-only root `artifacts` symlink and reran `--problem all`; it passed.
44. `diff`/`sed` reads compared candidate generated views and the candidate node. Only the expected window status marks changed.
45. Further `rg`/`sed` reads checked recon headings and the transfer amendment’s ratification language.

All candidate mutations were outside the repository. The candidate directory is deleted in final closeout.

#### E. Report composition and interactive-process correction

46. A `functions.exec` JavaScript attempt to compose the long Markdown report failed with a JavaScript `SyntaxError` caused by unescaped Markdown backticks. The isolate failed before it called a tool; no OS process or file was created.
47. Started foreground PTY session 15652:
    - `stty -echo; cat > /tmp/.../report.md`
48. One tool-only empty `write_stdin` poll confirmed the process was waiting.
49. A large `write_stdin` transfer encountered the PTY’s canonical line buffer on the 1,261-character claim line. The terminal emitted BEL characters and the scratch file stopped at 8,558 bytes. Read-only `wc -c -l` and `tail -n 5` detected the truncation.
50. Tool-only Ctrl-C terminated session 15652; exit status 1. It was a foreground process, not detached.
51. A Python heredoc unlinked only the truncated scratch `report.md`.
52. Started replacement foreground PTY session 52780:
    - `stty -echo -icanon min 1 time 0; cat > /tmp/.../report.md`
53. Tool-only `write_stdin` transfers sent this report in bounded chunks. Between chunks, foreground `wc -c -l` and `tail` commands verified the last complete paragraph.
54. Additional read-only source checks during composition:
    - `cat` of scratch candidate node, canonical window node, and authored proof;
    - `rg` headings and `sed` ranges `59-238`, `150-520`, and `520-900` of the proof;
    - `rg` layout/dependent/compression terms across the prior theorem/amendment/reviews;
    - `cat` of both scratch enumeration scripts;
    - `rg` route/level/premise strings in window, instances, transfer, and root nodes;
    - `sed` of the root claim/caveats and both downstream route bodies.
55. Under noncanonical input, a tool-only EOT was written as one literal `0x04` byte rather than closing session 52780. A tool-only Ctrl-C then terminated the foreground session with status 1. A read-only byte check found the single terminal byte.
56. The first scratch-only Python correction attempt then failed before writing because Python 3.9 `Path.write_text` does not accept the `newline` keyword.
57. A corrected scratch-only Python command removed the terminal byte, fixed two initially detected §13/§14 cross-references, made this process disclosure accurate, changed Appendix A/B labels from byte-exact to line-wrapped complete sources, and stripped trailing spaces. No repository file was involved.
58. The final scratch cross-reference scan found one additional stale §13 event reference in the verdict matrix. A scratch-only Python replacement changed it to §14 and recorded this correction; no repository file was involved.
59. A diagnostic `rg` command used double-quoted shell text containing Markdown backticks; the shell attempted four harmless command substitutions and printed `command not found` before `rg` ran. No data were interpolated, no file was written, and the useful matches were still inspected. A subsequent Python/difflib comparison avoided shell interpolation.
60. That exact comparison exposed a wording error in the draft report: artifact §12 does not itself start with an explicit `Q` binder. A scratch-only Python correction accurately records the 51-character prefix expansion, updates the clause table and conclusion, and records this correction.

#### F. Final closeout commands

After the report body is sealed, the only remaining OS actions are exactly:

```text
python3 [scratch report UTF-8/marker/whitespace/cross-reference checks]
wc -l -c /tmp/circdist_sat_window_exact_review_20260826_r51/report.md
shasum -a 256 /tmp/circdist_sat_window_exact_review_20260826_r51/report.md
python3 [assert canonical review absent; copy2 scratch report to the one authorized canonical path]
python3 [delete /tmp/circdist_sat_window_exact_review_20260826_r51 with shutil.rmtree]
python3 [assert scratch absent; verify canonical UTF-8, markers, line endings, trailing whitespace]
shasum -a 256 <repo>/circdist/reviews/circdist_sat_window_selfcontained_exact_review_20260826.md
git status --short -- circdist/reviews/circdist_sat_window_selfcontained_exact_review_20260826.md
shasum -a 256 circdist/proof-dag/nodes/CIRCDIST.sat.window.yaml circdist/artifacts/circdist_sat_window_selfcontained_exact_proof_20260826.md
ps -axo pid=,ppid=,stat=,command= | awk '/[c]ircdist_sat_window_exact_review_20260826_r51|[s]at_window_selfcontained_exact_review/ {print}'
```

These final commands are read-only except for copying the authorized report and deleting scratch. Their final digest and survival result are reported to the dispatcher in the task handoff because a file cannot contain its own post-seal digest without changing it.

### 17.3 Temporary paths

The only worker-created temporary root was:

```text
/tmp/circdist_sat_window_exact_review_20260826_r51
```

Its contents before closeout were:

```text
audit.py
vector_audit.py
candidate/
report.md
```

The candidate contained copied or symlinked source material plus generated scratch views and one placeholder review. No temporary item is intended to survive final closeout.

### 17.4 Durable mutation declaration

The sole authorized durable path is:

```text
circdist/reviews/circdist_sat_window_selfcontained_exact_review_20260826.md
```

No other repository file was opened for writing. The target node, scheduler, protocols, generated views, tools, prior artifacts/reviews, and migration records remained untouched. Candidate node/view writes occurred only below `/tmp`.

### 17.5 Process declaration

There were no background or detached jobs. PTY session 15652 was terminated after the canonical-buffer failure. PTY session 52780 was the foreground writer used to seal this report; noncanonical EOT behavior and its Ctrl-C close are disclosed in items 55-57. Final `ps` checks for either scratch/review pattern; the task handoff states whether any match survives.

## Appendix A. Complete scalar audit source (line-wrapped in this report)

```python
from itertools import combinations

def popcount(x):
    return bin(x).count("1")

effects = [(s,u,l) for s in (0,1) for u in (0,1) for l in (0,1)
           if (s,u,l) != (0,0,0)]

def analyze(mask, dictionary, R):
    n = len(dictionary)
    c = 0
    logical = 0
    support = []
    round_data = []
    for r in range(R):
        sr = ur = lr = 0
        occupied = False
        for i,(s,u,l) in enumerate(dictionary):
            if (mask >> (r*n+i)) & 1:
                sr ^= s
                ur ^= u
                lr ^= l
                occupied = True
        if ur != c:
            return False, False, (), round_data
        c ^= sr
        logical ^= lr
        if occupied:
            support.append(r)
        round_data.append((sr,ur,lr,c))
    return c == 0, logical == 1, tuple(support), round_data

def solve(dictionary, R):
    n = len(dictionary)
    best = None
    minima = []
    for mask in range(1 << (n*R)):
        wt = popcount(mask)
        if best is not None and wt > best:
            continue
        closed, logical, support, _ = analyze(mask,dictionary,R)
        if closed and logical:
            if best is None or wt < best:
                best = wt
                minima = [(mask,support)]
            elif wt == best:
                minima.append((mask,support))
    return best,minima

tested = finite_cases = valid_configs = 0
append_checks = prepend_checks = translate_checks = split_checks = r1_checks = 0
violations = []
drop_examples = []
stabilization_rows = []
for size in range(1,5):
    for dictionary in combinations(effects,size):
        tested += 1
        vals=[]
        mins=[]
        for R in range(1,5):
            d,mm=solve(dictionary,R)
            vals.append(d)
            mins.append(mm)
            if d is not None:
                finite_cases += 1
                for mask,S in mm:
                    contiguous = S == tuple(range(S[0],S[-1]+1))
                    span = S[-1]-S[0]+1
                    if not contiguous or span > d:
                        violations.append(("minimum-support",dictionary,R,d,S))
            n=len(dictionary)
            for mask in range(1 << (n*R)):
                closed,logical,S,_=analyze(mask,dictionary,R)
                if not (closed and logical):
                    continue
                valid_configs += 1
                if R < 4:
                    c2,l2,_,_=analyze(mask,dictionary,R+1)
                    append_checks += 1
                    if not (c2 and l2):
                        violations.append(("append",dictionary,R,mask))
                    shifted=mask << n
                    c3,l3,_,_=analyze(shifted,dictionary,R+1)
                    prepend_checks += 1
                    if not (c3 and l3):
                        violations.append(("prepend",dictionary,R,mask))
                a,b=S[0],S[-1]
                w=b-a+1
                shifted=0
                for r in range(a,b+1):
                    block=(mask >> (r*n)) & ((1<<n)-1)
                    shifted |= block << ((r-a)*n)
                c4,l4,S4,_=analyze(shifted,dictionary,w)
                translate_checks += 1
                if not(c4 and l4) or S4 != tuple(x-a for x in S):
                    violations.append(("translate",dictionary,R,mask,S,S4))
                for g in range(a+1,b):
                    if g in S:
                        continue
                    left = mask & ((1 << (g*n))-1)
                    right = mask ^ left
                    cl,ll,_,_=analyze(left,dictionary,R)
                    cr,lr,_,_=analyze(right,dictionary,R)
                    split_checks += 1
                    if not(cl and cr and (ll or lr)):
                        violations.append(("split",dictionary,R,mask,g,cl,ll,cr,lr))
        for a,b in zip(vals,vals[1:]):
            if a is not None and b is not None and b>a:
                violations.append(("monotonicity",dictionary,tuple(vals)))
        if vals[0] is not None:
            d=vals[0]
            if d <= 4:
                tail=vals[d-1:]
                if any(x != vals[d-1] for x in tail):
                    violations.append(("first-d-tail",dictionary,tuple(vals),d))
                target=vals[d-1]
                S=next(i+1 for i,x in enumerate(vals) if x==target)
                if S>target:
                    violations.append(("stabilization-bound",
                                       dictionary,tuple(vals),S,target))
                stabilization_rows.append((dictionary,tuple(vals),
                                           d,target,S))
        if vals[0] is not None and vals[1] is not None and vals[1] < vals[0]:
            drop_examples.append((dictionary,tuple(vals)))
        n=len(dictionary)
        for mask in range(1<<n):
            closed,logical,_,rows=analyze(mask,dictionary,1)
            sr=ur=lr=0
            for i,(s,u,l) in enumerate(dictionary):
                if (mask>>i)&1:
                    sr^=s
                    ur^=u
                    lr^=l
            r1_checks += 1
            if (closed and logical) != (ur==0 and sr==0 and lr==1):
                violations.append(("R1",dictionary,mask,rows))

mirror_cases=0
for overlap in (0,2,4,6):
    for earlier_mask in range(1<<overlap):
        c=popcount(earlier_mask)&1
        cp=(overlap-popcount(earlier_mask))&1
        mirror_cases += 1
        if c != cp:
            violations.append(("mirror-MC",overlap,earlier_mask,c,cp))

def rank(rows,n):
    rows=[r for r in rows if r]
    rr=0
    for col in range(n-1,-1,-1):
        pivot=next((i for i in range(rr,len(rows))
                    if (rows[i]>>col)&1),None)
        if pivot is None:
            continue
        rows[rr],rows[pivot]=rows[pivot],rows[rr]
        for i in range(len(rows)):
            if i!=rr and ((rows[i]>>col)&1):
                rows[i]^=rows[rr]
        rr+=1
    return rr

def rowspace(rows):
    out={0}
    for r in rows:
        out |= {x^r for x in list(out)}
    return out

def kernel(rows,n):
    return {v for v in range(1<<n)
            if all(popcount(v&r)%2==0 for r in rows)}

def css_distances(hx,hz,n):
    sx=rowspace(hx)
    sz=rowspace(hz)
    kx=kernel(hz,n)-sx
    kz=kernel(hx,n)-sz
    return min(map(popcount,kx)),min(map(popcount,kz)),kx,kz

n=6
hx=[0b000011,0b001100,0b110000]
hz=[0b001111,0b111100]
assert all(popcount(a&b)%2==0 for a in hx for b in hz)
dX,dZ,kx,kz=css_distances(hx,hz,n)
assert (dX,dZ)==(3,2)
minX=sorted(v for v in kx if popcount(v)==dX)
minZ=sorted(v for v in kz if popcount(v)==dZ)

steane=[sum(1<<q for q in qs)
        for qs in ((0,2,4,6),(1,2,5,6),(3,4,5,6))]
hx_dep=steane+[steane[0]^steane[1]]
assert rank(steane,7)==3 and rank(hx_dep,7)==3
leftker_dim=len(hx_dep)-rank(hx_dep,7)
R=2
short_x_dim=len(hx_dep)*(R-1)
canonical_x_dim=short_x_dim+leftker_dim
z_record_count=len(steane)*R
zcan_dim=z_record_count+rank(steane,7)
short_total=zcan_dim+short_x_dim
canonical_total=zcan_dim+canonical_x_dim
assert (leftker_dim,short_total,canonical_total)==(1,13,14)

collision_pairs=projection_cases=0
for bits in (2,4):
    for a in range(1,1<<bits):
        half=bits//2
        xpart=a & ((1<<half)-1)
        if xpart:
            assert xpart < (1<<bits)
        projection_cases += 1
        for b in range(1,1<<bits):
            product=a^b
            assert 0 <= product < (1<<bits)
            collision_pairs += 1

print("dictionaries_tested",tested)
print("finite_R_cases",finite_cases)
print("logical_closed_configurations",valid_configs)
print("append_checks",append_checks)
print("prepend_checks",prepend_checks)
print("translation_checks",translate_checks)
print("gap_split_checks",split_checks)
print("R1_equivalence_checks",r1_checks)
print("mirror_stability_checks",mirror_cases)
print("collision_group_pairs",collision_pairs)
print("sector_projection_menu_checks",projection_cases)
print("violations",len(violations))
print("drop_examples",len(drop_examples))
for row in drop_examples[:2]:
    print("drop",row)
print("stabilization_rows_checked",len(stabilization_rows))
print("asymmetric_dX_dZ_d",dX,dZ,min(dX,dZ))
print("asymmetric_min_X_vectors",
      [format(v,"06b") for v in minX])
print("asymmetric_min_Z_vectors",
      [format(v,"06b") for v in minZ])
print("dependent_leftker_short_canonical_dims",
      leftker_dim,short_total,canonical_total)
if violations:
    for v in violations[:20]:
        print("VIOLATION",v)
    raise SystemExit(1)
```

## Appendix B. Complete vector audit source (line-wrapped in this report)

```python
from itertools import combinations

def pc(x):
    return bin(x).count("1")

effects=[(s,u,l)
         for s in (0,1)
         for u in (0,1)
         for l in range(4)
         if (s,u,l)!=(0,0,0)]

def state(mask,D,R):
    n=len(D)
    c=0
    l=0
    S=[]
    for r in range(R):
        sr=ur=lr=0
        block=(mask>>(r*n))&((1<<n)-1)
        for i,(s,u,v) in enumerate(D):
            if (block>>i)&1:
                sr^=s
                ur^=u
                lr^=v
        if ur!=c:
            return False,0,()
        c^=sr
        l^=lr
        if block:
            S.append(r)
    return c==0,l,tuple(S)

tested=minima_checked=split_checked=valid_checked=0
viol=[]
for size in range(1,4):
    for D in combinations(effects,size):
        tested+=1
        for R in range(1,4):
            best=None
            mins=[]
            for mask in range(1<<(size*R)):
                closed,l,S=state(mask,D,R)
                if closed and l:
                    valid_checked+=1
                    w=pc(mask)
                    if best is None or w<best:
                        best=w
                        mins=[(mask,S)]
                    elif w==best:
                        mins.append((mask,S))
                    for g in range(S[0]+1,S[-1]):
                        if g in S:
                            continue
                        left=mask&((1<<(g*size))-1)
                        right=mask^left
                        cl,ll,_=state(left,D,R)
                        cr,lr,_=state(right,D,R)
                        split_checked+=1
                        if not(cl and cr and (ll or lr) and (ll^lr)==l):
                            viol.append(("split",D,R,g,l,ll,lr))
            for mask,S in mins:
                minima_checked+=1
                if (S!=tuple(range(S[0],S[-1]+1))
                        or len(S)>best):
                    viol.append(("minimum",D,R,best,S))

print("vector_dictionaries_tested",tested)
print("vector_valid_logicals_checked",valid_checked)
print("vector_minima_checked",minima_checked)
print("vector_gap_splits_checked",split_checked)
print("vector_violations",len(viol))
if viol:
    print(viol[:10])
    raise SystemExit(1)
```

## Appendix C. Reproducible exact-claim hash check

The following standalone check uses the exact corrected scalar already printed in Finding F-CLAIM:

```python
from hashlib import sha256
from pathlib import Path
import yaml

node = yaml.safe_load(Path(
    "circdist/proof-dag/nodes/CIRCDIST.sat.window.yaml"
).read_text())
current = node["claim"]
candidate = (
    "For every CSS code Q = [[n,k,d]] with k >= 1 and every fixed legal "
    "(conflict-free and measurement-consistent) single-round single-ancilla "
    "CSS syndrome-extraction schedule M for Q, let C_R^Z(M) and C_R^X(M) be "
    "the ideal-boundary memory experiments formed by R verbatim repetitions "
    "of M with the uniform unit-cost full-Pauli per-location fault model, and "
    "let d_R(M) be the minimum of their circuit distances measured against, "
    "respectively, the canonical detector space of Definition 3.5 in the "
    "CIRCDIST.sat.transfer proof dossier and its section-8.1 mirror "
    "(equivalently in value only, not in detector-set equality, the "
    "corresponding Definition-2.7 detector sets). Then d_(R+1)(M) <= d_R(M) "
    "for every R >= 1; d_infinity(M) := lim_{R to infinity} d_R(M) exists; "
    "in each memory sector every minimum-weight undetectable logical has a "
    "same-weight sector-pure representative supported on a contiguous "
    "interval of rounds whose span is at most its faulty-location weight; "
    "and, writing d = min(d_X,d_Z) for the CSS code distance and R_stab(M) "
    ":= min{R_0 >= 1 : d_R(M) = d_infinity(M) for all R >= R_0}, one has "
    "R_stab(M) <= d_infinity(M) <= d and d_R(M) = d_d(M) = d_infinity(M) "
    "for every R >= d. Consequently d_1(M),...,d_d(M) determine both "
    "d_infinity(M) and R_stab(M)."
)

def normalized_hash(s):
    return "sha256:"+sha256(
        s.replace("\r\n","\n").strip().encode("utf-8")
    ).hexdigest()

print(len(current), normalized_hash(current))
print(len(candidate), normalized_hash(candidate))
assert len(candidate)==1261
assert normalized_hash(candidate)==(
    "sha256:6c50b4049ae908d6646e87f7446f8fb"
    "7ea9583182fb79da3cb6b935c7011ccc4"
)
assert yaml.safe_load(yaml.safe_dump({"claim":candidate}))["claim"]==candidate
```

Expected output:

```text
489 sha256:8698b051b15fa14ff669299580d9b7bfec01808c0a34133ef09264e749466146
1261 sha256:6c50b4049ae908d6646e87f7446f8fb7ea9583182fb79da3cb6b935c7011ccc4
```

## 18. Final review conclusion

The direct proof is complete and withstands the required boundary, sector, dependence, collision, asymmetry, detector-split, and index attacks. The current shorthand claim is too implicit, and the author’s 1,210-character repair still omits `k>=1`. The exact 1,261-character string in Finding F-CLAIM is the compact complete repair I reviewed and scratch-validated.

For that string and hash only, I independently license:

```text
CIRCDIST.sat.window: PROVED
```

subject to the exact field and append-only event contract in §14. No downstream promotion, route rebind, generated-view edit, or scheduler action is licensed by inheritance. The dispatcher must install and validate the authorized node change separately.

