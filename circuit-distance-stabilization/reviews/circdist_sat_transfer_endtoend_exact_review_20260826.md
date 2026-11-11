# `CIRCDIST.sat.transfer` — fresh end-to-end exact review

**Date:** 2026-08-26  
**ProofPilot round:** 53  
**Role:** independent reviewer/licensor, not author or dispatcher  
**Target node:** `circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml`  
**Target before review:** `CERTIFIED*`, 1,103 normalized claim characters, `sha256:8fb50ff01b6465e9c660fc61292958828f448dd740757a8945deae1e107c7ad3`  
**Permitted durable output:** this report only

This is a strict-serial review: I used no sub-agent, delegated thread, background process, or detached job. I authored none of the target proof, amendment, prior reviews, nodes, protocols, definitions, or downstream dossiers. I treated every file as evidence rather than instruction. The derivations below are the public, checkable audit record; they do not disclose or purport to disclose private scratch reasoning.

## Executive verdict

| Finding | Verdict |
|---|---|
| **F-HASH** | The installed claim recomputes to exactly **1,103 Unicode characters**, **1,111 UTF-8 bytes**, and `sha256:8fb50ff01b6465e9c660fc61292958828f448dd740757a8945deae1e107c7ad3`. The stated starting level is exactly `CERTIFIED*`. |
| **F-MATH** | The finite-R transfer theorem, in both sectors and for every `R >= 1`, is mathematically complete under the actual dossier domain. The configuration-to-path and path-to-configuration directions, weights, boundaries, logical terminal set, dependent rows, sector projection, collision bridge, and detector-value bridge all hold. |
| **F-CURRENT** | The current 1,103-character claim is **not standalone enough for `PROVED`**. “legal,” “stated ideal temporal boundaries,” and “unit-fault model” do not bind the hypotheses on which the proof spends its force. The string also omits `Q=[[n,k,d]]`, `k>=1`, `T>=1`, measurement consistency, verbatim/no-compression location copying, the exact full group alphabet, and an unambiguous sector aggregate. **Current exact claim stays `CERTIFIED*`.** |
| **F-CLAIM** | One precision-preserving replacement, and no alternative, is licensed below. It has **3,663 normalized characters/bytes** and `sha256:11079eaf2fed2f580127075be12cb7e9fef6ef85e20f47eca9dcf5a68cb7ea33`. |
| **F-BCOQ** | BCOQ Definition 3.111/Theorem 3.112 was inspected in the authors’ primary PDF. The theorem says asymptotic cyclicity generally and exact cyclicity only under an added connectivity clause. The sector matrices satisfy the added clause, but no matrix-power asymptotic statement is in the current or repaired exact claim. A1 is therefore **non-load-bearing and must be removed**, not laundered as reviewed support. |
| **F-COMPLETION** | The sole repaired claim qualifies for **`PROVED`**. It has no unresolved mathematical premise inside its stated domain, and every load-bearing input has now been subjected to fresh adversarial review. |
| **F-DOWNSTREAM** | The repair is semantically compatible with window hash `6c50…1ccc4` and root hash `513496…b7572`. It licenses **no automatic change** to the root, instances node, any route, scheduler, or generated view. Instances and root remain `CERTIFIED*`; the root route remains at its already-installed level. |

The dispatcher may install the exact YAML in §15.6. No other phrasing is licensed.

## 1. Governing protocol and review threshold

I read the current root-level `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full. Their relevant consequences are:

1. A completion review binds to the normalized exact statement: CRLF is mapped to LF, leading/trailing whitespace is stripped, UTF-8 bytes are SHA-256 hashed, and `sha256:` is prepended.
2. `PROVED` requires a complete argument and independent adversarial review of every load-bearing input. It is not obtained from simulation, a route label, or inheritance.
3. A direct proof must state its assumptions. Published external theorems may be used only at their exact scope with a locatable source.
4. Reviews and historical events are immutable evidence. A changed claim lapses old `reviewed_hash` bindings; old reports move to historical evidence rather than being rewritten.
5. Generated views are derived. A reviewer does not hand-edit them, and a level change does not propagate to a parent automatically.
6. `frontier` records unfinished work. Work outside the proved proposition can remain as an engineering/corroboration task without lowering the theorem’s completion level.

The exact protocol source hashes were:

| Source | Bytes | SHA-256 |
|---|---:|---|
| `DAG_PROTOCOL.md` | 15,377 | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | 8,523 | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |

## 2. Materials and exact source chain

### 2.1 Load-bearing transfer record

| File | Lines | Bytes | SHA-256 | Use in this review |
|---|---:|---:|---|---|
| `circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md` | 243 | 10,199 | `5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64` | Frozen common model/problem statement |
| `circdist/artifacts/definitions/SAT_RESCOPE_20260822.md` | 98 | 6,112 | `6c8ec4362f728713f9934d5f0b8041195f66434ebe283a69e67147b3c7009d7f` | Frozen SAT rescope |
| `circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml` | 126 | 8,907 | `a3a5a635a8fe68e6645bfdabf8af9b1425a3a6305331f2491c42ab804347c5e6` | Exact installed object |
| `circdist/artifacts/circdist_sat_transfer_proof_20260823.md` | 1,485 | 90,772 | `4fce5371edc09fa153b41f6735d521d31500b84b55a0059c8b42dc000651da30` | Primary proof dossier |
| `circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md` | 1,024 | 61,291 | `6c7a8fb756cfba958f82c70f739ffa90aee19070c2cae8f358d44ccdc20ad07e` | Governing repairs F1–F5 |
| `circdist/reviews/circdist_sat_transfer_review_20260823.md` | 452 | 30,725 | `a9afbf93713634237dfcb795d98e71072537e7370a3fa675dcdf1ac766110003` | Earlier full review, historical input |
| `circdist/reviews/circdist_sat_transfer_rereview_20260823.md` | 424 | 25,369 | `3cc2b5784951b14b3ae534de5be1a5f3b3a303a1cc30fc539b04eab7c9a45a44` | Amendment conformance review |
| `circdist/reviews/circdist_transfer_bridgefold_20260823.md` | 639 | 44,971 | `9f5f93426b0f6cbf140339c30695ae6922ae5968001ddc9b5884b3dce3d84199` | Prior bridge re-derivation and current old-hash binding |

The primary proof locators are unusually good. The domain is at §§1–2 (lines 56–251), detector analysis at §3 (255–438), state and dictionary at §§4–5 (440–542), boundaries at §6 (544–618), the two transfer directions at §7 (620–675), the mirror/aggregate at §8 (677–712), spectrum/window material at §9 (714–802), and corroborating computation at §11 (815–1388). Amendment 1 governs the false alternate-split mitigation (§2), the no-left-boundary counterfactual (§3), the mirror-labelled program (§4), and two wording repairs (§5).

### 2.2 Window, root, and exact-review context

I read the current window/instances/root nodes, all three files named `*exact*review*`, and the current downstream scope-rebind review. I also read the earlier window/root dossiers and adjudications needed to distinguish old conditions from current ones.

| File | SHA-256 |
|---|---|
| `circdist/artifacts/circdist_sat_window_theorem_20260822.md` | `487acf030bc4385ab367e5c7b27a0e2015bae4055f16ba61100ea85866d37e1b` |
| `circdist/artifacts/circdist_sat_window_amendment1_20260822.md` | `295e1635cc7a27c6ca43d88e7a9303c5bbfac96aeaecb1d2fee1a5cad4ac9799` |
| `circdist/reviews/circdist_sat_window_review_20260822.md` | `219a756e9e366d74cd6d4b13ff91bdb8394ed35f5c922d3f864b176fcf697226` |
| `circdist/reviews/circdist_amendments4_review_20260822.md` | `49484a887416bf43649c4e7b45c65f7cb04328311989f1cafb56a4b2eac24763` |
| `circdist/reviews/circdist_readjudication_20260823.md` | `cec9c7ca489f85d215bfe06a880576ba7a2efc69ed41156ec3920f0854b914a2` |
| `circdist/artifacts/circdist_sat_window_selfcontained_exact_proof_20260826.md` | `bf0d6dd591ae0fb11ef5c75196ffaa89456b5cfd2cc40493fffd6274607f10f7` |
| `circdist/reviews/circdist_sat_window_selfcontained_exact_review_20260826.md` | `0d202d40a931faef7c09236f0f9b4413f979b59dfef335b582203d29ea7a3786` |
| `circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md` | `2d593bb7861665b3bdf017736ce1965870fbe161d4ab2fc3e3997fa9226e3d94` |
| `circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md` | `624456d295b5a2c07e154414b6a71652b33738f217c3b86d51d4e47a7d9888d7` |
| `circdist/reviews/circdist_sat_window_downstream_scope_rebind_review_20260826.md` | `475746e4186d0a176dcbc83d6849c0d953e385a7280d1ecc87de0ef765415c14` |
| `circdist/artifacts/circdist_sat_root_assembly_20260823.md` | `68babfe69cd1c988c897839466fdb3ddfd24802eb4e77667ac1ad53551edaead` |
| `circdist/reviews/circdist_sat_root_review_20260823.md` | `5e1fd365ce330a89c4f11c86cba3ac180446cb51a84c9a62b5eb8b004ec61579` |
| `circdist/reviews/circdist_sat_root_proved_adjudication_20260823.md` | `7b05b8f4509c51cde1407c5329e91b13abb33770d290df2fc4eab550a48e38d4` |

No PDF, PostScript, or DjVu file exists anywhere in the repository. The only external primary source that could plausibly bear on the exact transfer node was BCOQ; §10 records the retrieval and theorem mapping. A2/A3 in the dossier discuss generic transient bounds and multi-letter decidability, but neither is used by the finite-R proposition under review.

## 3. Finding F-HASH — exact installed string

The installed normalized claim is:

```text
For each fixed legal single-round single-ancilla CSS schedule M under the stated ideal temporal boundaries and unit-fault model, there is an explicitly constructible finite min-plus transfer system (u,A,v) such that d_R(M) = u^T min-plus A^R min-plus v for every R, with the two CSS sectors, boundary conditions, unreachable states, and logical terminal condition represented exactly. The d_R so computed is moreover invariant under the counting and detector-split conventions the surrounding route composes across: by Lemma 2.9 it is the same whether a witness is counted by its number of elementary faults, collisions permitted, or by its number of faulty locations; and in each CSS sector separately it is the same whether detectors are taken to be the Definition-2.7 set or the canonical detector space of Definition 3.5, this being Proposition 3.7 in the Z-sector and its mirror under section 8.1 in the X-sector. Definition 3.5 is named here as a specific space; that it is the detector/observable split the frozen 公共定义 intends is a lead decision recorded in the caveats, not a result proved here.
```

Independent normalization produced:

```text
characters = 1103
UTF-8 bytes = 1111
SHA-256 = sha256:8fb50ff01b6465e9c660fc61292958828f448dd740757a8945deae1e107c7ad3
assessment.level = CERTIFIED*
```

The hash matches the commission and the one extant `basis.reviews` binding. There is no hash mismatch to explain.

## 4. Finding F-CURRENT — why the current exact claim cannot be promoted

The old sentence is a fair summary of the intended theorem when read beside the dossier. It is not an adequate exact proposition at `PROVED` under the current protocol.

| Old phrase/omission | Actual load-bearing condition | Adversarial consequence |
|---|---|---|
| “each fixed … CSS schedule” | `Q=[[n,k,d]]`, `k>=1`, given possibly dependent check rows | At `k=0`, `ker H_Z/S_X` and `ker H_X/S_Z` have no nonzero logical terminal class, so the displayed `v` has empty finite support and the usual circuit-distance minimum has no logical witness. |
| “legal” | conflict freedom **and** measurement consistency `(MC)` | Conflict freedom alone permits a schedule whose check outcome is random and whose named detector is not deterministic. |
| no `T>=1` | depth is a positive integer | The proof of finite one-round weights uses an idle fault on a data qubit that participates in no CNOT. A zero-depth empty schedule would remove that location. |
| “single-round single-ancilla” | exact fresh ancilla preparation, one CNOT per support qubit, basis-specific measurement, no flags/cats/repeated gates | Round transparency and the two-coordinate effect dictionary fail outside this circuit form. |
| “stated ideal temporal boundaries” | ideal data preparation and terminal transversal readout, no boundary fault locations | The left detector fixes the recursion constant; the terminal detector supplies `H_Z sigma_R=0`. Removing either changes `u` or `v`. |
| no layout clause | `R` disjoint verbatim copies, no cross-round idle compression | The weight decomposition `|F|=sum_r |S_r|` and round-independent dictionary require disjoint copied location sets. |
| “unit-fault model” | full local Pauli **group**, uniform cost one per occupied location, classical record flips | Collision merging and `Y` projection can fail for an incomplete alphabet or nonuniform costs. |
| `d_R(M)` unexpanded | `min(d_R^Z,d_R^X)` | For asymmetric CSS codes the sector values differ, so an unspecified aggregate is material. |
| “unreachable states” | all within-sector entries are finite under the stated full model | There are no within-sector unreachable transition states. Only block-crossing and boundary-excluded entries are `+infinity`. |
| `u^T` | dossier uses a row boundary vector `u` | Not a mathematical failure, but an avoidable orientation ambiguity in an exact claim. |
| no complexity exclusion | construction is finite exhaustive enumeration | “Explicitly constructible” does not imply a polynomial algorithm; the current wording leaves room for that overreading. |

### 4.1 Concrete conflict-free but MC-failing attack

Take `H_X=H_Z=(1111)` on four data qubits. Schedule the eight CNOTs sequentially as

```text
q0->b, a->q0, a->q1, q1->b, a->q2, q2->b, a->q3, q3->b.
```

No qubit participates in two CNOTs in one time step, so the schedule is conflict-free. Exactly one common-support qubit has `t(q->b)<t(a->q)`, hence `c_ab=1`. Back-propagating the `Z` measurement of `anc(b)` produces a `Z` on the freshly `|+>`-prepared `anc(a)`; that anticommutes with its input stabilizer, so the check record is uniformly random. The Definition-2.7 parity is not a detector. This is not a marginal convention: the finite-state proof has no defined object to compute until MC is imposed.

### 4.2 `k=0` attack

For the stabilizer state with `n=2`, `H_X=H_Z=(11)`, `k=0`. Then

```text
dim(ker H_Z/S_X) = n-rank(H_X)-rank(H_Z) = 0.
```

There is no nonzero terminal class, so `v` is nowhere finite. One may choose a convention `min(empty)=+infinity`, but that is not the memory logical-distance proposition stated in the dossier. The theorem deliberately assumes `k>=1`; the exact claim must say so.

**Verdict on the current string:** preserve `CERTIFIED*`. The smallest residual is exact-statement scope, not a missing proof lemma.

## 5. Finding F-MATH — exact model reconstructed from the frozen record

### 5.1 CSS code and terminal logical classes

Let

```text
Q=[[n,k,d]],  k>=1,
H_X H_Z^T = 0,
S_X=row(H_X),  S_Z=row(H_Z).
```

The rows are the given generating rows and may be dependent. Standard CSS symplectic duality gives

```text
ker(H_Z)/S_X ≅ F_2^k,
ker(H_X)/S_Z ≅ F_2^k.
```

In the Z-memory sector, a residual data-X vector `E` is undetectable at ideal readout iff `H_Z E=0`; it is logical iff `[E]` is a nonzero class in `ker(H_Z)/S_X`. Thus there are exactly `2^k-1` accepted terminal classes. The X-memory statement is the mirror.

This proves why dependent rows are harmless: only row spaces and quotient classes enter. It also proves why `k>=1` is not decorative.

### 5.2 One-round circuit and legality

For every given X-check row `a`, a fresh `|+>` ancilla is the control of exactly one CNOT to every data qubit in `supp(a)` and is measured in X. For every Z-check row `b`, a fresh `|0>` ancilla is the target of exactly one CNOT from every data qubit in `supp(b)` and is measured in Z. There are no flags, cats, repeated support CNOTs, or changing generator lists.

A depth-`T`, `T>=1`, assignment is conflict-free if no physical qubit participates in two CNOTs in one time step. It is measurement-consistent iff

```text
c_ab(M) := #{q in supp(a)∩supp(b): t(q->b)<t(a->q)} = 0 mod 2
```

for every `a,b`. Since CSS orthogonality makes the complementary count equal modulo two, MC is mirror-symmetric.

### 5.3 Rounds and boundaries

`C_R^Z(M)` uses ideal `|0>^n` data initialization, `R>=1` verbatim copies of the round with disjoint copied location sets, and ideal transversal Z readout. `C_R^X(M)` is the X/Z mirror. No cross-round idle-layer compression is allowed.

For Z memory, with records `m_{b,r}` and readout bits `rho_q`, the temporal boundary convention is

```text
m_{b,-1}=0,
m_{b,R}=sum_{q in supp(b)} rho_q,
D_{b,r}=m_{b,r}+m_{b,r-1},  r=0,...,R.
```

The `r=0` detector is absolute. The `r=R` detector contains the ideal readout. These two endpoints do different jobs and neither can be inferred from the other.

### 5.4 Exact fault alphabet and cost

| Location | Allowed nonidentity assignment | Position |
|---|---|---|
| CNOT | all 15 two-qubit Paulis modulo phase | immediately after the gate |
| idle `(qubit,time)` | `X`, `Y`, or `Z` | at every copied idle location |
| ancilla preparation | `X`, `Y`, or `Z` | immediately after preparation |
| recorded outcome | classical bit flip | at each copied round record |
| data initialization / terminal readout | none | ideal, no fault location |

A configuration assigns at most one group element to a location and costs the number of locations carrying a nonidentity. The Pauli propagation rule is

```text
CNOT(c,t): x_t <- x_t+x_c,   z_c <- z_c+z_t,
```

with `x_c` and `z_t` unchanged. Ancilla frames are discarded at measurement/reset.

## 6. Complete effect dictionary and sector projection

### 6.1 One-round coordinates

For an X-sector one-round configuration `S`, let

```text
E(S) in F_2^n       residual data-X vector after the round,
u(S) in F_2^{|B|}   flips of that round's own Z-check records.
```

These coordinates include every schedule-specific hook. A Pauli after a CNOT may change both the residual and the current record; a data error already present at round entry is handled separately by round transparency. Record-flip locations give `(E,u)=(0,e_b)`. A data X placed after its last CNOT gives `(e_q,0)`. The full effect of products is XOR because Clifford propagation and record flips are linear over `F_2`.

A `Y` is not a third coupled sector. In the Z-memory optimization, keep each Pauli’s X part and each Z-check record flip, delete its Z part and X-check record flip. Full Pauli availability makes the projected assignment legal and uniform occupied-location cost makes its weight no larger. It preserves every Z-check record/readout/observable flip and gives zero on every X-check-record parity. The X-memory projection is the mirror.

This step fails if a pure projected Pauli is unavailable or more expensive. The repaired claim explicitly excludes those models.

### 6.2 Elementary-fault count versus occupied locations

Let `m(e)` be the least cardinality of a multiset of unit elementary faults with total effect `e`, allowing multiple members at one location, and let `c(e)` be the least number of occupied locations in a configuration.

A configuration is itself such a multiset, so `m(e)<=c(e)`. Conversely, in any multiset, replace two elements at one location by their product in that location’s full Pauli group. The effect is unchanged. If the product is nonidentity the multiset shrinks by one; if identity it shrinks by two. Repeat until at most one element remains per location. This produces a configuration of weight at most the original multiset size, so `c(e)<=m(e)`. Therefore

```text
m(e)=c(e).
```

Disjoint copied round-location sets then give exact additivity across rounds. This proves Lemma 2.9 with both hidden hypotheses exposed: linear effect and group closure with uniform unit cost.

A non-group alphabet gives an immediate counterexample. At one CNOT location allow `X_c` and `X_t` but not `X_cX_t`. The collision-permitting multiset realizes the product effect with two elementary faults at that location, while a one-assignment configuration cannot realize it there. A nonuniform model similarly invalidates the weight-nonincreasing projection if `Y` is cheap but its pure X or Z component is expensive.

### 6.3 Finite dictionary

On

```text
Sigma^Z=F_2^n/S_X
```

define

```text
w_M^Z([delta],mu)
  = min{|S|: [E(S)]=[delta], u(S)=mu}.
```

The minimum is attained because one round has finitely many locations and finite local groups. It is finite for every pair:

1. For each data qubit, put X immediately after its last CNOT; if it has no CNOT, use one of its `T>=1` idle locations. This realizes residual `e_q` with zero record flip.
2. Use classical record flips to realize any `mu` with zero residual.
3. Combine distinct singleton locations and merge any accidental same-location assignments by Lemma 2.9.

Hence

```text
w_M^Z([delta],mu) <= min_{delta' in [delta]} |delta'| + |mu| < infinity.
```

All within-sector transition weights are finite. The old phrase “unreachable states” must not be read as asserting otherwise.

## 7. Detector spaces and exact value bridge

### 7.1 Deterministic parity spaces

Represent a record parity in `C_R^Z` by `(alpha,beta,gamma)`, where `alpha` selects X-check records, `beta` selects Z-check records, and `gamma` selects terminal readout bits. Back-propagation through the MC circuit gives a direct sum

```text
V = V_Z direct-sum V_X,
V_Z = {(beta,gamma): gamma in ker(H_X)},
V_X = {alpha: sum_r H_X^T alpha_r = 0}.
```

Thus

```text
dim V_Z = |B|R+n-rank(H_X),
dim V_X = |A|R-rank(H_X).
```

MC kills the intra-round cross terms; CSS orthogonality kills the inter-round terms. Neither condition replaces the other.

### 7.2 Definition 3.5

Definition 3.5 first restricts to deterministic parities `V`. It then calls a parity a detector when its deterministic **value** is the same for every prepared logical-basis input in the specified family. That gives

```text
D = D_Z direct-sum D_X,
D_Z = {(beta,gamma): gamma in S_Z},
D_X = V_X.
```

The observable directions are the quotient `V_Z/D_Z`, of dimension `k`.

The full Z-check chain spans the Z half exactly:

```text
D_Z = span{D_{b,r}: b in B, r=0,...,R}.
```

The `r<R` chain is triangular in all `beta` coordinates; the terminal detectors add gamma-parts spanning `S_Z`. Dependent Z rows do not create a missing direction because the absolute `r=0` chain already contains their redundancy parities.

The short X-check chain has codimension

```text
dim leftker(H_X)
```

inside `D_X`. The missing parities are the dependent-row combinations at round zero. They are genuine detectors even though the individual first-round X-check outcomes are random.

### 7.3 Proposition 3.7 is value equality only

The Definition-2.7 set lies in `D`, so `d^{2.7}<=d^D`. Take a minimum short-set witness `F` and project it to `F^X`. It preserves the full Z-check detector chain and the logical observable. Since that chain spans `D_Z`, it annihilates `D_Z`; because it flips no X-check record at all, it annihilates every element of `D_X`, including dependent-row redundancy directions. Its weight does not increase. Hence `d^D<=d^{2.7}` and

```text
d_R^{Z,2.7}(M)=d_R^{Z,D}(M).
```

The mirror proves the same equality in X memory. This is equality of minima for one ordered pair of definitions. It is not detector-set equality and not arbitrary-split invariance.

### 7.4 Alternate-split attack and Amendment 1

On Steane with a redundant X row, let `P_X` be the round-zero dependent-row parity and let `lambda` be the logical observable. The old mitigation admitted

```text
D' = span(D_b) + span(D_a) + span(P_X+lambda),
```

because `D'` contains the short set and lies in `V`. Yet `P_X+lambda` detects the projected logical witness. The exact reproduced data are:

| R | record dimension | `dim V` | `dim D` | `rank span(D_b)` | `rank span(D_b,D_a)` | `d^{2.7}` | `d^{D'}` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 21 | 15 | 14 | 9 | 13 | 2 | 3 |
| 3 | 28 | 22 | 21 | 12 | 20 | 2 | 4 |

At `R=3` this is the recorded quintuple `28/22/21/12/20`. Amendment 1 correctly replaces the false condition by

```text
span(D_b) subseteq D' subseteq D.
```

That containment is sufficient by the same projection proof. No version with only `D' subseteq V` survives.

## 8. The finite-state/min-plus representation

### 8.1 State and round transparency

The Z-sector state is the class of accumulated residual data-X error:

```text
sigma_r = [sum_{j<r} E(S_j)] in Sigma^Z,
sigma_0=[0],
sigma_{r+1}=sigma_r+[E(S_r)].
```

A data X error present at round entry remains on the data through the round and flips that round’s Z-check record vector by `H_Z E`. The schedule-specific effects caused inside the round are already in `(E(S_r),u(S_r))`. Therefore the accumulated input affects the future only through `sigma_r`; `H_Z` and logical functionals descend to the quotient because `S_X` commutes with Z checks and logical Zs.

### 8.2 Boundary criterion

The flip of record `m_{b,r}` is

```text
(H_Z sigma_r)_b + u_b(S_r),
```

and the virtual terminal record is `(H_Z sigma_R)_b`. Vanishing of all consecutive differences is equivalent to

```text
u(S_r)=H_Z sigma_r   for r=0,...,R-1,
H_Z sigma_R=0.                                      (W)
```

The left boundary pins the otherwise-free constant to zero. The right boundary supplies the final kernel condition. Given that kernel condition, the physical fault is logical exactly when `sigma_R != [0]`.

For `R=1`, `(W)` reads `u(S_0)=0` and `H_Z[E(S_0)]=0`; the terminal class must be nonzero. Both boundaries remain present. Nothing in the derivation silently assumes `R>=2`.

### 8.3 Matrix and boundary vectors

Define over `Z_{>=0} union {+infinity}` with min as addition and ordinary addition as multiplication:

```text
A^Z[sigma,sigma'] = w_M^Z(sigma'-sigma,H_Z sigma),
u^Z[sigma] = 0 iff sigma=[0], else +infinity,
v^Z[sigma] = 0 iff H_Z sigma=0 and sigma!=[0], else +infinity.
```

Then

```text
d_R^Z(M) = u^Z min-plus (A^Z)^R min-plus v^Z.
```

### 8.4 Universal physical-to-path direction

Take any physical undetectable logical configuration. Sector-project it without increasing weight, split it by disjoint rounds, and form its states `sigma_0,...,sigma_R`. Criterion `(W)` makes each round admissible for the matrix entry

```text
A^Z[sigma_r,sigma_{r+1}].
```

By the definition of `w`, that entry is at most the round’s occupied-location weight. Summing gives a path whose cost is at most the physical weight and whose initial/terminal boundary costs are zero. Therefore the min-plus scalar is no larger than physical distance.

### 8.5 Universal path-to-physical direction

Take any finite-cost `R`-edge path accepted by `u^Z,v^Z`. For each edge, the finite minimum defining `w` is attained by a one-round configuration with

```text
[E(S_r)] = sigma_{r+1}-sigma_r,
u(S_r) = H_Z sigma_r,
|S_r| = A^Z[sigma_r,sigma_{r+1}].
```

Place that configuration in copied round `r`. Disjoint location sets make the union a valid configuration with exactly the summed path cost. Induction gives the selected state at every boundary; `(W)` makes the union undetectable; `v^Z` makes the final class nonzero in the kernel and hence logical. Therefore physical distance is no larger than the min-plus scalar.

The inequalities meet. This is a bijective correspondence at the level needed for minima: every physical configuration yields a no-more-expensive path, and every finite path has an exact-cost physical lift. No simulation or window theorem is used.

### 8.6 Mirror and aggregate

Swap X/Z, `H_X/H_Z`, control/target, and the ancilla families. MC is preserved because the two ordering counts sum to the even CSS overlap. This gives

```text
Sigma^X=F_2^n/S_Z,
d_R^X(M)=u^X min-plus (A^X)^R min-plus v^X.
```

On the disjoint union, use block diagonal `A=A^Z direct-sum A^X` and concatenate `u,v`. Every finite path remains in one block, so

```text
d_R(M)=min(d_R^Z(M),d_R^X(M))
      =u min-plus A^R min-plus v.
```

All within-block entries are finite. Cross-block entries and excluded boundary states are represented by `+infinity`. The construction is finite and explicit, but generally exponential; no minimal-state or polynomial-time theorem has been proved or is needed.

## 9. Amendment audit

| Repair | Fresh disposition | Effect on exact finite-`R` theorem |
|---|---|---|
| F1 / T-G3 mitigation | The old `D' subseteq V` claim is false; the corrected `span(D_b) subseteq D' subseteq D` condition and explicit counterexample reproduce. | Main Definition-3.5/Definition-2.7 equality remains correct. |
| F2 / no `D_{b,0}` counterfactual | Without the left boundary, the constant `kappa` also changes the terminal condition: `v_kappa`, not fixed `v`, is required. Reproduced `0/16` old versus `16/16` corrected. | Main theorem retains `D_{b,0}`, so unaffected. |
| F3 / mirror driver | The original six block X-sector rows constructed the opposite block order; circuit mirroring at the same time steps fixes labels. Patched program hash and all values reproduce. | Mathematical §8.1 mirror was already correct. |
| F4 / irreducibility | Irreducibility applies per finite-entry sector block, not to the two-block matrix with infinite cross entries. | Candidate states the exact block structure. |
| F5 / `w>2` wording | The theorem is for the canonical two-round detector chain. Larger windows would require memory unless separately derived. | Candidate fixes the named detector definition and makes no wider claim. |

Former “open minors” do not remain premises of the repaired proposition:

- T-G1 is discharged by writing the exact full fault model into the claim.
- T-G2 asks for Nerode-minimality, which the claim explicitly excludes.
- T-G3 is a definitional pin plus the proved exact-pair value bridge; arbitrary splits are explicitly excluded.
- T-G4 concerns complexity; finite enumeration is proved and polynomial complexity is explicitly excluded.
- T-G5 is the finiteness mechanism, proved from `T>=1`, terminal data singletons, and record flips.

## 10. Finding F-BCOQ — primary-source adjudication

The repository contains no local copy. I downloaded the [authors’ electronic edition](https://www.rocq.inria.fr/metalau/cohen/documents/BCOQ-book.pdf) to deleted scratch, SHA-256

```text
3926a8b13841fb96f7e4354a7e9e3b621a02daa0ce6e1031a8b1d3c8840f6856
```

and inspected PDF pages 159 and 164–167, including printed pages 143–151. The source first normalizes a max-plus matrix by its maximum cycle mean. Definition 3.111 distinguishes exact cyclicity from asymptotic cyclicity. Theorem 3.112 establishes asymptotic cyclicity for every normalized matrix and adds exact cyclicity when the graph of the matrix and the graph of the cyclicity power are connected.

### 10.1 Mapping to this matrix

For one transfer sector:

1. Negating finite min-plus entries gives a finite max-plus matrix.
2. All transfer costs are nonnegative and zero-cost loops exist, so the min-plus eigenvalue is zero; the max-plus normalization is already zero.
3. The critical graph consists of the zero-syndrome self-loops and has cyclicity one.
4. Every matrix entry is finite, so its graph and first power graph are connected (indeed complete as directed support graphs).
5. The source’s added clause therefore yields exact eventual one-cyclicity for each sector. The two-block assembled result follows blockwise after the larger of the two transients.

So the dossier’s more careful A1 application can be repaired into a correct argument. The **installed node assumption is still overbroad**: “min-plus matrix powers are eventually periodic” is false without normalization/rate and connectivity qualifications. The one-by-one min-plus matrix `[1]` has power `[R]`, not an eventually periodic unshifted sequence.

### 10.2 Load-bearing ruling

The exact transfer claim says only

```text
d_R=u A^R v for every finite R.
```

It says nothing about eventual matrix powers, `d_infinity`, or a transient. The dossier itself marks A1 load-bearing only for Corollary 9.2’s extra phrase. Its scalar window facts are directly derived in Corollaries 9.3–9.6, and the now-PROVED window node has a separate self-contained proof that explicitly does not import BCOQ or the transfer theorem.

**Ruling:** remove `assumptions.a1-bcoq-3112`. Do not retain it as a reviewed assumption for a claim that does not use it. If eventual matrix-power constancy is wanted later, place it in a separate exact claim with the normalization, per-sector finiteness/connectivity, critical graph, and blockwise conclusion stated and reviewed.

A2 (generic transient lower bounds) and A3 (one-letter versus multi-letter decidability) are likewise commentary on excluded generalizations, not inputs to the repaired finite-R claim. They need not be fetched or registered here.

## 11. Circularity and source-scope audit

The transfer construction is not imported from the window node:

- The primary transfer dossier restates the model and re-derives sector decoupling, round transparency, time locality, criterion `(W)`, the singleton finiteness mechanism, the detector-space equality, and both transfer inequalities.
- Its use of the earlier window amendment is superseded by the sharper derivation in transfer §3.
- Transfer §9 re-derives window consequences only after the finite-R formula; those consequences are not used to prove the formula.
- The 2026-08-26 self-contained window proof uses the transfer dossier only as a stable locator for Definition 3.5 and proves its theorem directly. It does not use `A`, BCOQ, instances, or the root.
- The root consumes transfer, window, and instances as separate premises. Neither the root claim nor route is used anywhere in the transfer derivation.

No circular import exists.

## 12. Adversarial attack ledger

| Attack | Result |
|---|---|
| `k=0` | Fatal to the old unqualified domain; terminal logical set is empty. Excluded explicitly. |
| conflict-free but MC-failing | Explicit 4-qubit schedule gives `c_ab=1` and a random would-be detector. Excluded explicitly. |
| cross-round compression | Destroys effect-preserving round bijections/disjointness and can create cross-round collisions. Excluded explicitly. |
| asymmetric CSS code | Fresh `[[3,1,1]]` test gives sector distances 1 and 2; block aggregation returns their minimum exactly. |
| dependent generating rows | Algebra uses row spaces/left kernels; fresh dependent `[[4,1,2]]` test and archived Steane+redundant-X checks agree. |
| same-location collisions | Full group merge proves equality; fresh multiset/configuration searches agree on all toy cases. |
| group-incomplete alphabet | Synthetic `{X_c,X_t}` without `X_cX_t` breaks collision merging. Excluded. |
| nonuniform costs | Can make sector projection cost-increasing. Excluded. |
| alternate detector complement | Steane+redundant-X moves distance from 2 to 3/4. Candidate licenses only Definition 2.7 versus Definition 3.5 in value. |
| `R=1` | Both absolute and terminal detectors survive; direct propagator and transfer formula agree. |
| missing terminal detector | Would remove `H_Z sigma_R=0` from `v` and compute a different value. Not in scope. |
| missing initial detector | Requires `(A_kappa,v_kappa)`; the old fixed-`v` counterfactual fails 16/16. Main claim retains the boundary. |
| unreachable/empty states | Full model makes every within-sector transition finite. Cross-block and boundary exclusions are the only infinities. |
| polynomial complexity | Not proved; candidate explicitly disclaims it. Finite exhaustive construction suffices. |
| source misquotation | Installed A1 is overbroad; it is removed as non-load-bearing. |
| window/root circularity | None; dependencies point outward only after the transfer result is established. |

## 13. Exact corroborating computations

Computations here are checks, not proof of the universal theorem.

### 13.1 Source/program checksum reconstruction

I extracted §11.4 from the proof’s own Markdown bytes:

```text
transfer_doc.py   1d3b8754b72d9dc77a8c16ecfab1c8b81f9dcfd5dd0a9abb2baf1b1a26e64c68
```

This exactly matches the proof’s declared digest. Applying only Amendment 1’s governing driver replacement produced:

```text
transfer_fixed.py f3dfa1f9048984de557cacee3cd0c6d56f04f7ae8a6036a256e5807552d19ced
```

This exactly matches the amendment’s repaired digest. Extracting its §6.1 harness produced:

```text
amend.py          9a3e7db73b6dffdd079c21c9abd06f900199752b18ee918dc311c3fc60128291
```

again matching the amendment.

Running `transfer_fixed.py` produced 16 legal `(schedule,sector)` rows, 48/48 equality values for `R=1,2,3`, all parity formulas true, and all within-sector entries finite. It found 16 of 576 interleaved direction-order pairs legal and MC. The output SHA-256 was `0405e7bfc67759fe14be0d41ad782070ee403201f7f79149437669460e284472`; its only nondeterministic field is elapsed time.

Running `amend.py` reproduced the old/corrected no-left-boundary totals (`0/16` versus `16/16`) and the complete alternate-split table above. Its output SHA-256 was `ceb72d5980c70d208abb2324097de8091e4f68efbdfd4835f8708d68a486a33f`; elapsed time again varies.

### 13.2 Fresh independent finite propagator

I wrote a new scratch-only symplectic propagator without importing repository code or constants. It:

- enumerated the exact full local Pauli groups one occupied location at a time;
- propagated raw X/Z frames through every CNOT and reset ancillas after measurement;
- constructed raw Definition-2.7 and canonical detector constraints;
- computed configuration minima and collision-permitting elementary-multiset minima independently;
- constructed `w`, quotient states, `A,u,v` from one-round effects;
- compared those transfer values with direct multi-round circuit enumeration;
- mirrored the physical circuit at the same time steps for the other sector.

Scratch script SHA-256: `b528af726d2871465017f5e975421c0dcf89b4c0018e1dbdd8c882bf1dac4050`.

```text
name                         sec R d  locations signatures shortD canon-rank |Sigma| |w|
dependent-[[4,1,2]]          Z   1 2       92       256       2      3          4    8
dependent-[[4,1,2]]          Z   2 2      184      4096       6      7          4    8
dependent-[[4,1,2]]          X   1 1       92       256       6      5          8   64
dependent-[[4,1,2]]          X   2 1      184      4096      10      9          8   64
asymmetric-[[3,1,1]]         Z   1 1       16        32       2      2          4    8
asymmetric-[[3,1,1]]         Z   2 1       32       128       4      4          4    8
asymmetric-[[3,1,1]]         X   1 2       16        32       2      2          4    8
asymmetric-[[3,1,1]]         X   2 2       32       128       4      4          4    8
```

For every row:

```text
d_direct-short-config
 = d_direct-canonical-config
 = d_direct-short-multiset
 = d_direct-canonical-multiset
 = d_transfer.
```

An additional abstract four-state min-plus test enumerated every path and matched dynamic matrix powers for `R=1,...,5`. The script also asserted the explicit MC-failing schedule and the empty terminal set at `k=0`. All assertions passed.

## 14. Finding F-CLAIM — the only licensed replacement

The following is one exact line. It has no leading/trailing whitespace and no newline inside the scalar.

```text
For every CSS code Q = [[n,k,d]] with k >= 1, with H_X and H_Z the matrices of the given (possibly dependent) X- and Z-check generating rows, and every depth-T, T >= 1, conflict-free (no physical qubit participates in two CNOTs in one time step) and measurement-consistent single-round single-ancilla CNOT schedule M in which each X-check has one freshly |+>-prepared, X-measured control ancilla coupled exactly once to each support qubit and each Z-check has one freshly |0>-prepared, Z-measured target ancilla coupled exactly once from each support qubit, where measurement consistency means #{q in supp(a) intersect supp(b): t(q->b) < t(a->q)} = 0 mod 2 for every X-check a and Z-check b, define C_R^Z(M) and C_R^X(M), R >= 1, by R verbatim copies of M with disjoint copied location sets and no cross-round idle compression, ideal |0> and |+> data initialization respectively, and ideal transversal Z and X terminal readout respectively. At every copied CNOT location allow the full 15-element nonidentity two-qubit Pauli menu after the gate, at every copied idle and post-ancilla-preparation location allow the full three-element nonidentity one-qubit Pauli menu, and at every copied record location allow a flip; a configuration costs its number of occupied locations, while data initialization and terminal readout are fault-free. Against the canonical detector space D of Definition 3.5 of circdist/artifacts/circdist_sat_transfer_proof_20260823.md, namely the deterministic record parities whose value is constant across the prepared logical-basis input family, put Sigma^Z = F_2^n/row(H_X), and let w_M^Z([delta],mu) be the minimum occupied-location cost of a one-round X-sector configuration with residual data-X class [delta] and own Z-check-record flip vector mu. Over the min-plus semiring S = (Z_{>=0} union {+infinity}, min, +), define A^Z[sigma,sigma'] = w_M^Z(sigma'-sigma,H_Z sigma), u^Z[sigma] = 0 exactly when sigma = [0] and +infinity otherwise, and v^Z[sigma] = 0 exactly when H_Z sigma = 0 and sigma != [0] and +infinity otherwise. The dictionary is finite everywhere and explicitly constructible by finite enumeration, and for every R >= 1, d_R^Z(M) = u^Z min-plus (A^Z)^R min-plus v^Z. Every physical undetectable logical configuration projects to an R-edge path of cost at most its occupied-location weight, and every finite such path lifts to a physical undetectable logical configuration of exactly its cost. Swapping X and Z, H_X and H_Z, controls and targets gives the mirror system (u^X,A^X,v^X) on Sigma^X = F_2^n/row(H_Z) and the identical equality for d_R^X(M). On Sigma^Z disjoint-union Sigma^X, the block-diagonal A = A^Z direct-sum A^X with concatenated u and v satisfies d_R(M) = min(d_R^Z(M),d_R^X(M)) = u min-plus A^R min-plus v for every R >= 1. Every within-sector entry of A is finite; the cross-sector entries are +infinity, and the +infinity entries of u and v encode exactly the excluded initial and terminal states. In each sector the same minimum value is obtained (i) with collision-permitting multisets of unit elementary faults or with occupied faulty locations, by Lemma 2.9 and the full per-location Pauli-group and uniform-cost hypotheses, and (ii) against the Definition-2.7 detector set or D, by Proposition 3.7 in the Z-memory sector and its section-8.1 mirror in the X-memory sector. Clause (ii) is equality of minimum values for that ordered pair of detector conventions, not equality of their detector spaces and not invariance under arbitrary detector/observable splits. No claim about eventual periodicity or constancy of matrix powers, state-space minimality, or polynomial construction time is made.
```

Exact normalization:

```text
characters = 3663
UTF-8 bytes = 3663
reviewed_hash = sha256:11079eaf2fed2f580127075be12cb7e9fef6ef85e20f47eca9dcf5a68cb7ea33
```

### 14.1 Semantic identity and precision

This is a precision repair, not a different research result:

| Current clause | Exact serialization in replacement |
|---|---|
| fixed legal CSS schedule | full code binder, `k>=1`, `T>=1`, conflict freedom, MC, exact ancilla/CNOT circuit |
| stated ideal temporal boundaries | explicit sector initializations and terminal readouts, fault-free boundaries |
| unit-fault model | exact full local groups, record flips, occupied-location weight |
| `A^R` represents boundaries/unreachable/logical | exact `Sigma,w,A,u,v`, finite within-sector transitions, cross/boundary infinities, terminal kernel/nonzero test |
| two CSS sectors | exact mirror and block-diagonal minimum |
| “represented exactly” | universal physical-to-path bound and exact path-to-physical lift |
| Lemma 2.9 | exact collision and group/uniform-cost scope |
| Proposition 3.7 and mirror | exact per-sector equality of values and explicit non-invariance warning |
| no asymptotic/complexity assertion | explicit exclusion of matrix-power asymptotics, minimality, and polynomial time |

The replacement does not add a new eventuality theorem, detector split, schedule class, fault alphabet, or distance convention. It states the proposition the dossier actually proves and that the current window/root records already consume.

## 15. Finding F-COMPLETION — level and field-by-field install contract

### 15.1 Mathematics and exact claims

- **Mathematics:** `PROVED` for the repaired finite-R proposition.
- **Current exact claim:** remains `CERTIFIED*`; mandatory precision repair.
- **Repaired exact claim:** `PROVED`, bound only to `sha256:11079eaf2fed2f580127075be12cb7e9fef6ef85e20f47eca9dcf5a68cb7ea33`.
- **Semantic identity:** precision-preserving at the intended dossier scope; no alternative wording licensed.
- **Node level after installation:** `PROVED`.
- **External assumptions:** remove `assumptions` entirely. No external theorem is load-bearing.

### 15.2 Reviews/evidence

- Replace `assessment.basis.reviews` with this report as the only completion review. Every old review hash binds an old claim and must not remain in `reviews` for the repaired hash.
- Preserve all old reports and artifacts under `basis.evidence` exactly as historical evidence. Do not rewrite them.
- Preserve the existing structured run as corroboration. Do not promote it into a proof premise.
- The repaired embedded-program and fresh-toy scratch outputs are intentionally not durable evidence objects; their methods and exact outputs are transcribed in §13.

### 15.3 Caveats, summary, frontier

The five caveats in the YAML below are scope/exclusion notes, not unresolved premises. They preserve the detector warning, model boundary, exponential construction, BCOQ exclusion, and evidence/proof distinction.

The existing packaging frontier remains useful, but is explicitly marked optional corroboration/engineering. T-G2/T-G4 are not proof gates because the claim disclaims minimality and polynomial complexity.

### 15.4 Events and immutable history

Append three current-format events: exact claim repair, review completion, and level change. Historical events in `circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml` remain byte-immutable. No event is backdated or rewritten.

### 15.5 Generated views and scheduler

The dispatcher, not this reviewer, should install the node and then regenerate derived views with

```text
PYTHONDONTWRITEBYTECODE=1 python3 tools/proof_dag_check.py --problem circdist --write-generated
```

followed by the full validators in §18. This review does not license editing `operations/circdist/SCHEDULER.yaml`, either protocol, any tool, or any other durable file.

### 15.6 Complete installable YAML

This is the complete node, not a fragment. It is the only licensed field serialization.

```yaml
id: CIRCDIST.sat.transfer
role: proof
aliases:
- SAT-TRANSFER
claim: 'For every CSS code Q = [[n,k,d]] with k >= 1, with H_X and H_Z the matrices of the given (possibly dependent)
  X- and Z-check generating rows, and every depth-T, T >= 1, conflict-free (no physical qubit participates in two
  CNOTs in one time step) and measurement-consistent single-round single-ancilla CNOT schedule M in which each X-check
  has one freshly |+>-prepared, X-measured control ancilla coupled exactly once to each support qubit and each Z-check
  has one freshly |0>-prepared, Z-measured target ancilla coupled exactly once from each support qubit, where measurement
  consistency means #{q in supp(a) intersect supp(b): t(q->b) < t(a->q)} = 0 mod 2 for every X-check a and Z-check
  b, define C_R^Z(M) and C_R^X(M), R >= 1, by R verbatim copies of M with disjoint copied location sets and no cross-round
  idle compression, ideal |0> and |+> data initialization respectively, and ideal transversal Z and X terminal readout
  respectively. At every copied CNOT location allow the full 15-element nonidentity two-qubit Pauli menu after the
  gate, at every copied idle and post-ancilla-preparation location allow the full three-element nonidentity one-qubit
  Pauli menu, and at every copied record location allow a flip; a configuration costs its number of occupied locations,
  while data initialization and terminal readout are fault-free. Against the canonical detector space D of Definition
  3.5 of circdist/artifacts/circdist_sat_transfer_proof_20260823.md, namely the deterministic record parities whose
  value is constant across the prepared logical-basis input family, put Sigma^Z = F_2^n/row(H_X), and let w_M^Z([delta],mu)
  be the minimum occupied-location cost of a one-round X-sector configuration with residual data-X class [delta]
  and own Z-check-record flip vector mu. Over the min-plus semiring S = (Z_{>=0} union {+infinity}, min, +), define
  A^Z[sigma,sigma''] = w_M^Z(sigma''-sigma,H_Z sigma), u^Z[sigma] = 0 exactly when sigma = [0] and +infinity otherwise,
  and v^Z[sigma] = 0 exactly when H_Z sigma = 0 and sigma != [0] and +infinity otherwise. The dictionary is finite
  everywhere and explicitly constructible by finite enumeration, and for every R >= 1, d_R^Z(M) = u^Z min-plus (A^Z)^R
  min-plus v^Z. Every physical undetectable logical configuration projects to an R-edge path of cost at most its
  occupied-location weight, and every finite such path lifts to a physical undetectable logical configuration of
  exactly its cost. Swapping X and Z, H_X and H_Z, controls and targets gives the mirror system (u^X,A^X,v^X) on
  Sigma^X = F_2^n/row(H_Z) and the identical equality for d_R^X(M). On Sigma^Z disjoint-union Sigma^X, the block-diagonal
  A = A^Z direct-sum A^X with concatenated u and v satisfies d_R(M) = min(d_R^Z(M),d_R^X(M)) = u min-plus A^R min-plus
  v for every R >= 1. Every within-sector entry of A is finite; the cross-sector entries are +infinity, and the
  +infinity entries of u and v encode exactly the excluded initial and terminal states. In each sector the same
  minimum value is obtained (i) with collision-permitting multisets of unit elementary faults or with occupied faulty
  locations, by Lemma 2.9 and the full per-location Pauli-group and uniform-cost hypotheses, and (ii) against the
  Definition-2.7 detector set or D, by Proposition 3.7 in the Z-memory sector and its section-8.1 mirror in the
  X-memory sector. Clause (ii) is equality of minimum values for that ordered pair of detector conventions, not
  equality of their detector spaces and not invariance under arbitrary detector/observable splits. No claim about
  eventual periodicity or constancy of matrix powers, state-space minimality, or polynomial construction time is
  made.'
assessment:
  level: PROVED
  caveats:
  - 'The proved domain is exactly the one written into the claim: k >= 1, depth T >= 1, conflict freedom plus measurement
    consistency, one fresh ancilla per given check row, verbatim uncompressed rounds, ideal data boundaries, and
    the uniform unit-cost full-Pauli per-location group. The review does not license extensions outside that domain.'
  - Definition 3.5 is pinned definitionally. Proposition 3.7 and the section-8.1 mirror establish equality of minimum
    values only between that canonical space and the corresponding Definition-2.7 set in each sector. They do not
    establish equality of detector spaces or invariance under arbitrary complements/splits; the amended Steane+redundant-X
    counterexample remains the sharp warning.
  - The displayed state spaces are sufficient, not proved minimal. Construction by exhaustive finite enumeration
    can be exponential. Under the stated full fault menu every within-sector transition is finite; +infinity is
    retained for cross-sector transitions and excluded initial/terminal states, not as evidence of undiscovered
    within-sector unreachable states.
  - No eventual-periodicity or eventual-constancy statement about matrix powers is part of the repaired claim. BCOQ
    Definition 3.111 and Theorem 3.112 were checked against the authors' public primary PDF; any future use must
    state asymptotic cyclicity versus exact cyclicity and verify normalization, critical cyclicity, and connectivity.
    The former A1 assumption is therefore removed rather than treated as reviewed support for this claim.
  - Archived implementations, tables, and independent finite enumerations are corroboration only. The universal
    result is carried by the reviewed algebraic proof, including the ratifying amendment; no numerical run is used
    to bridge an unproved quantifier.
  summary: PROVED at sha256:11079eaf2fed2f580127075be12cb7e9fef6ef85e20f47eca9dcf5a68cb7ea33. A fresh strict-serial
    end-to-end review established the exact repaired finite-R transfer proposition in both CSS sectors, including
    all boundaries, the universal physical-configuration/path correspondence, dependent check rows, collision and
    detector-value bridges, and explicit fault-model and layout scope. The non-load-bearing BCOQ assumption is removed;
    matrix-power asymptotics, minimality, and polynomial complexity are excluded.
  basis:
    reviews:
    - path: circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
      kind: review
      scope: 'Fresh strict-serial end-to-end adversarial audit: independently re-derived the complete finite-R transfer
        proof and both convention bridges; attacked k=0, MC failure, cross-round compression, asymmetric sectors,
        dependent rows, collisions, incomplete/nonuniform alphabets, alternate detector splits, R=1 boundaries,
        finite/unreachable states, complexity, circularity, exact source statements, hashes, and downstream compatibility;
        licensed exactly one standalone repair and PROVED.'
      locator: Finding F-COMPLETION
      reviewed_hash: sha256:11079eaf2fed2f580127075be12cb7e9fef6ef85e20f47eca9dcf5a68cb7ea33
    runs:
    - path: circdist/artifacts/circdist_sat_recon_20260820.md
      kind: run
      scope: Exact min-plus implementation for four rotated-surface-code d=3 schedules, compared with an independent
        Stim detector-model calculation for R=1 through 10.
      result: Every transfer sequence was constant (2 or 3 according to schedule) and agreed with the independent
        calculation throughout the tested window.
    evidence:
    - path: circdist/artifacts/circdist_sat_recon_20260820.md
      kind: text
    - path: circdist/reviews/circdist_sat_transfer_rereview_20260823.md
      kind: text
    - path: circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml
      kind: text
      note: Immutable pre-migration record, including every original event, former summary and frontier; historical
        evidence, not an additional completion review.
    - path: circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/reviews/circdist_sat_transfer_review_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_sat_transfer_proof_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/definitions/SAT_RESCOPE_20260822.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/reviews/circdist_transfer_bridgefold_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/reviews/circdist_sat_root_proved_adjudication_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
frontier:
  task-002:
    task: Package the repaired implementation and the d=3 comparisons as a reproducible command/output record with
      explicit code and schedule inputs, search bounds, checksums, and agreement criteria. This is optional corroboration
      and engineering, not a premise of the PROVED theorem.
    kind: task
    since: '2026-08-22'
events:
  standalone-transfer-claim-repaired-2026-08-26:
    date: '2026-08-26'
    type: repair-applied
    summary: Replaced the 1,103-character shorthand claim at sha256:8fb50ff01b6465e9c660fc61292958828f448dd740757a8945deae1e107c7ad3
      with the exact 3663-character standalone claim at sha256:11079eaf2fed2f580127075be12cb7e9fef6ef85e20f47eca9dcf5a68cb7ea33.
      The repair binds Q = [[n,k,d]] with k >= 1, T >= 1, conflict freedom and measurement consistency, the one-ancilla
      circuit, ideal boundaries, verbatim uncompressed rounds, the uniform unit-cost full-Pauli location group,
      canonical detectors, exact sector systems, boundaries, collision bridge, and detector-value bridge. It removes
      the non-load-bearing and overbroad A1 assumption and explicitly excludes matrix-power asymptotics, minimality,
      and polynomial complexity.
    sources:
    - path: circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
      kind: review
      locator: Finding F-CLAIM
  transfer-endtoend-reviewed-2026-08-26:
    date: '2026-08-26'
    type: review-completed
    summary: Fresh independent strict-serial review checked the entire repaired exact proposition from the frozen
      definitions through both sector transfer systems and the collision/detector bridges, inspected the primary
      BCOQ source, reran feasible exact checks, and found no residual mathematical premise inside the claim.
    sources:
    - path: circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
      kind: review
      locator: Finding F-MATH
  transfer-proved-2026-08-26:
    date: '2026-08-26'
    type: level-change
    from: CERTIFIED*
    to: PROVED
    summary: Promoted CIRCDIST.sat.transfer after the exact repaired claim and every load-bearing input passed fresh
      independent adversarial review. No downstream node, route, or generated view changes by inheritance.
    sources:
    - path: circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
      kind: review
      locator: Finding F-COMPLETION
```

## 16. Finding F-DOWNSTREAM — compatibility without inheritance

Current exact downstream hashes recomputed during this review:

| Object | Level | Claim/implication characters | Hash |
|---|---|---:|---|
| `CIRCDIST.sat.window` | `PROVED` | 1,261 | `sha256:6c50b4049ae908d6646e87f7446f8fb7ea9583182fb79da3cb6b935c7011ccc4` |
| `CIRCDIST.sat.instances` | `CERTIFIED*` | 422 | `sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3` |
| instances route `finite-prefix-window-closure` | `CERTIFIED*` | 1,310 | `sha256:255e42681cb10bece97c5f55d5548cc865a94b9b422230435403804a9fb27e05` |
| `CIRCDIST.sat` root | `CERTIFIED*` | 1,357 | `sha256:513496daac6fa18bf96d1f2b6cf8768929eb62e45e103df1123479aadeeb7572` |
| root route `asymptotic-stability-assembly` | `PROVED` | 718 | `sha256:03549fb0f9856952319ee3dfc1d9bdbb11e49a47a9babbc65b7b9f87405763e1` |

The repaired transfer claim retains every fact those objects consume:

1. It uses the same explicit `Q`, `k>=1`, conflict-free+MC schedule domain as the repaired window/root claims.
2. It pins the same ideal boundaries, verbatim rounds, uniform full-Pauli model, and sector minimum.
3. It retains the exact finite-R min-plus representation the root’s algorithmic clause needs.
4. It retains Lemma 2.9’s collision bridge.
5. It retains Proposition 3.7 and the §8.1 mirror as per-sector **value** equalities and preserves the no-arbitrary-split warning.
6. It removes only a matrix-power asymptotic assumption that the exact transfer claim never used. The window theorem supplies the scalar tail directly and independently.

Consequences:

- `CIRCDIST.sat.window` remains `PROVED`; its proof and hash do not change.
- `CIRCDIST.sat.instances` remains `CERTIFIED*`; this report does not review its finite certificates to `PROVED`.
- The root route remains at its existing `PROVED` level; its implication text does not change.
- The root node remains `CERTIFIED*` because instances remains `CERTIFIED*` and because parent completion never follows automatically.
- Root caveat text that still describes transfer A1 or transfer `CERTIFIED*` will become stale bookkeeping after installation. Correcting downstream prose requires a separate downstream review/dispatcher action. This report licenses no such edit and no downstream promotion.

## 17. External-source status

| Source/result | Exact transfer-claim status | Review result |
|---|---|---|
| BCOQ Definition 3.111/Theorem 3.112 | Not load-bearing | Primary PDF inspected; installed paraphrase overbroad; exact application recoverable under added hypotheses; remove A1 here. |
| Cohen–Dubois–Quadrat–Viot / Butkovič refinements | Not load-bearing | Not needed after exclusion of matrix-power asymptotics; no claim made about their theorem numbering. |
| Nowak–Charron-Bost transient bounds | Not load-bearing | Only motivates why a generic dimension bound is insufficient; repaired claim makes no transient assertion. |
| Gaubert/Molnárová–Pribiš/Krob decidability boundary | Not load-bearing | Only concerns generalizations to changing rounds or complexity; repaired claim fixes one verbatim round and disclaims polynomial complexity. |
| CSS symplectic duality and CNOT Pauli conjugation | Load-bearing mathematical facts | Re-derived at the exact uses in §§5–8; no unreviewed external theorem remains. |

## 18. Validation record

### 18.1 Baseline, before any durable write

All passed on the unchanged repository:

```text
PYTHONDONTWRITEBYTECODE=1 python3 tools/proof_dag_check.py --problem circdist
  circdist: 16 node files structurally valid

PYTHONDONTWRITEBYTECODE=1 python3 tools/proof_dag_check.py --problem all
  se: 85 node files structurally valid
  ksum: 144 node files structurally valid
  circdist: 16 node files structurally valid

PYTHONDONTWRITEBYTECODE=1 python3 tools/evidence_closure_check.py --problem all
  circdist: evidence closure OK, 119 structured paths; all evidence project-local and linked

PYTHONDONTWRITEBYTECODE=1 python3 tools/check_circdist_migration.py
  Migration preservation OK: 16 nodes, 143 original events, 728 byte-identical copies

PYTHONDONTWRITEBYTECODE=1 python3 tools/check_event_append_only.py --base-ref HEAD
  Append-only event check OK against HEAD

git diff --check
  exit 0
```

The working tree was already heavily modified/untracked before this review. Branch was `main`; HEAD was `e40a7ac40972ad5186018797efa390a8e3f784f0`. This review did not claim ownership of any pre-existing change.

### 18.2 Candidate shadow validation

I copied the repository to a temporary directory outside the repository, installed the exact candidate there, placed a validation-only placeholder at this review path, regenerated views **only in that copy**, and ran:

```text
proof_dag_check --problem circdist --write-generated    PASS
proof_dag_check --problem circdist                      PASS
proof_dag_check --problem all                           PASS
evidence_closure_check --problem all                    PASS (120 structured paths)
check_circdist_migration.py                             PASS
check_event_append_only.py --base-ref HEAD              PASS
git diff --check                                        PASS
```

The loaded candidate reported:

```text
candidate_chars 3663
candidate_hash sha256:11079eaf2fed2f580127075be12cb7e9fef6ef85e20f47eca9dcf5a68cb7ea33
candidate_level PROVED
assumptions_present False
```


No candidate validation wrote to the real repository.

### 18.3 Real repository after the authorized report write

I reran the read-only validators after writing this report. The structural, migration, append-only, and whitespace checks still passed:

```text
proof_dag_check --problem circdist                   PASS: circdist 16 node files structurally valid
proof_dag_check --problem all                        PASS: se 85, ksum 144, circdist 16 node files structurally valid
check_circdist_migration.py                          PASS: 16 nodes, 143 original events, 728 byte-identical copies
check_event_append_only.py --base-ref HEAD           PASS: append-only event check OK against HEAD
git diff --check                                     PASS (exit 0)
```

The evidence-closure checker produced the one expected failure:

```text
evidence_closure_check --problem all
ERROR: circdist: unlinked evidence: circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
```

That result is not a defect in the report or candidate. It is the direct consequence of the commission's two simultaneous requirements that this report be written durably and that the reviewer not edit the node that links it. The disposable candidate installation links this exact review path and passed evidence closure with 120 structured paths (§18.2). Until the dispatcher installs §15.6, the real repository must therefore have this one new unlinked review.

I also compared SHA-256 manifests of every regular file and symlink target in the repository except `.git` and this one authorized report. Both snapshots contained 2,809 paths; the path sets were identical, and there were zero changed, added, or removed entries. Canonicalizing each manifest as sorted `path NUL digest` records gave the same aggregate SHA-256 before and after:

```text
1102beb2b15071035ce1cacce32a325cc29fcffca62d4aada183c54a273e9d00
```

This establishes content preservation outside this report during my review; it does not assign ownership of the repository's pre-existing dirty/untracked state. Final report parsing also reconfirmed a 3,663-character/byte exact claim with hash `sha256:11079eaf2fed2f580127075be12cb7e9fef6ef85e20f47eca9dcf5a68cb7ea33`, byte-identical claim text in §14, the complete YAML, and both scratch candidate serializations, one review entry bound to that hash, `PROVED`, no `assumptions`, the unchanged current transfer hash/level, the required window/root hashes and levels, and balanced Markdown fences.

## 19. FIX-2 accounting

### 19.1 Processes and commands

All shell processes were foreground and bounded. Read-only source inspection used `rg`, `rg --files`, `find`, `wc`, `cat`, `sed`, `nl`, `sha256sum`, `git status --short`, `git rev-parse HEAD`, and Python/YAML readers against the exact files listed in §2. Independent command groups were batched only for reading; no concurrent agent or writer existed.

The complete process classes, in execution order, were:

1. Repository identity/status and absence-of-target-report checks; `AGENTS.md` search; protocol and target-node reads.
2. Python recomputation of the installed claim length/hash/level and current window/instances/root claim and route hashes.
3. Full/chunked reads and `rg` section maps for the frozen definitions, rescope, transfer proof, amendment, three transfer reviews, all exact reviews, current downstream review, window sources/reviews, root assembly/reviews, and current nodes.
4. Repository-wide searches for BCOQ references and local PDF/PS/DjVu files.
5. Web search for the official BCOQ source; foreground `curl -L --fail --silent --show-error` download to `/tmp`; PDF metadata with `pdfinfo`; page extraction with bundled Python `pypdf`.
6. SHA-256 reconstruction of all sources in §§1–2 and extraction/patch hashing of `transfer_doc.py`, `transfer_fixed.py`, and `amend.py`.
7. Foreground execution of `transfer_fixed.py` and `amend.py` with stdout redirected to scratch.
8. Creation and execution of fresh `toy_audit.py`; exact configuration, multiset, detector, and transfer checks.
9. Baseline validators and `git diff --check` in the real repository, all read-only.
10. Candidate-string generation and hash; complete candidate-node generation in scratch.
11. Two temporary repository-copy validation attempts, then successful candidate regeneration/validation in the copy.
12. Repository-excluding-report manifest generation before the sole durable write.
13. Assembly of this report in `/tmp`, copying to the authorized review path, the failed no-op insertion attempt recorded below, and the final corrected copy to that same sole durable path.
14. Post-write real-repository validators, candidate validation against the actual report, repository-excluding-report manifest comparison, scratch cleanup, process check, and report SHA-256 computation.

### 19.2 Failures and corrections

Every failure was in scratch or read-only validation; none mutated a canonical file.

1. `pdftotext` was unavailable after the BCOQ PDF download (`command not found`). I used the bundled workspace Python and `pypdf` to extract the exact pages instead.
2. The first candidate scratch-creation command was rejected before execution because it contained `rm -rf`. I created a new unique scratch directory without a deletion command.
3. The first toy run failed its GF(2) rank assertion because the scratch rank routine counted a zero row. I filtered zero rows during elimination and reran.
4. The second toy run found the system Python lacks `int.bit_count`. I replaced it with `bin(x).count('1')` and reran.
5. The first candidate-copy validator invocation used `/tmp` as working directory and therefore looked for `/tmp/tools/proof_dag_check.py`. I corrected by changing into the copied repository.
6. The next candidate-copy run correctly reported stale generated views after the candidate node changed. I ran `--write-generated` only inside the disposable copy and then all validators passed.
7. The post-write real-repository evidence-closure check failed exactly on the newly written, intentionally unlinked review path. This is an expected install-contract boundary, not a suppressed pass: the reviewer was forbidden to edit the node, while the fully installed disposable candidate linked the report and passed with 120 paths.
8. My first attempt to insert §18.3 into the scratch report used an exact needle that omitted the already-present sentence about candidate validation. Its assertion failed before changing the scratch file. Because the surrounding shell command did not use `set -e`, it then recopied the unchanged scratch report over the same authorized report path and printed the unchanged hash. No other repository file was touched. I corrected the needle, inserted this accounting, and recopied the finalized report.
9. Three read-only report-integrity parser attempts failed successively because I first looked for `basis` at the YAML top level, then looked for `reviewed_hash` directly under `assessment.basis`, and then used the nonexistent filename `CIRCDIST.root.yaml` instead of `CIRCDIST.sat.yaml`. Each failed before mutation. I inspected the parsed schema and actual node names, corrected those paths, and the fourth run verified the exact claim, embedded YAML, scratch candidate, current transfer/window/root hashes and levels, review binding, absence of `assumptions`, and balanced Markdown fences.
10. My first repository-manifest comparison sorted complete `digest  path` rows and therefore produced a large false ordering diff; the corrected path-sort still differed textually from the baseline's locale/directory traversal order at four file/directory-name boundaries. Parsing both 2,809-entry manifests by path showed identical path sets and digests with zero changed, added, or removed entries; canonical `path NUL digest` serialization then matched exactly at the aggregate hash reported in §18.3.

### 19.3 Temporary paths and cleanup contract

Temporary paths used:

```text
/tmp/circdist-r53-bcoq.ZO8el4
/tmp/circdist-transfer-r53-20260826
/private/tmp/circdist-transfer-r53-candidate.N64sLt
/private/tmp/circdist-transfer-r53-candidate.NsmU4L
```

Any additional `circdist-transfer-r53-candidate.*` directory created by a failed attempt is included in the cleanup glob. Cleanup uses Python `shutil.rmtree`, followed by `find` verification. No temporary file is intended to survive this review.

### 19.4 Background/detached jobs

None were launched. No shell command contained `&`, `nohup`, `disown`, or a detached process manager. Final `ps` filtering is recorded after cleanup. Any unrelated process present on the host was not inspected, signalled, or claimed.

## 20. Limitations

1. There is no proof-assistant formalization. The warrant is a complete finite-dimensional algebraic proof plus independent adversarial checking.
2. Fresh numerical checks are small (`n<=4`, `R<=2`) and the repaired archived program is `d=3`, `R<=3`; they corroborate rather than prove the universal quantifier.
3. The BCOQ PDF was external and deleted after inspection. Its URL, SHA-256, exact pages, and hypothesis map are recorded so a future reviewer can repeat the check.
4. I did not review the instances certificates, root instance claims, or window theorem anew beyond the exact compatibility needed here. Their installed levels remain unchanged.
5. I do not license matrix-power eventuality, minimal automata, polynomial construction, changing-round schedules, compressed layouts, non-CSS gates, nonuniform costs, or incomplete fault alphabets.

## 21. Final verdict matrix

| Object/field | Verdict |
|---|---|
| Mathematical finite-R theorem | **PROVED** under exact repaired scope |
| Installed current claim `8fb50ff0…` | **CERTIFIED***; mandatory precision repair |
| Sole replacement `11079eaf…` | **PROVED** |
| Semantic identity | Precision-preserving serialization of the dossier theorem |
| `assessment.level` | Set to `PROVED` only with the exact replacement |
| `reviewed_hash` | `sha256:11079eaf2fed2f580127075be12cb7e9fef6ef85e20f47eca9dcf5a68cb7ea33` |
| `assumptions` | Remove; A1 is not load-bearing and is overbroad as installed |
| Caveats/summary/frontier | Replace exactly as in §15.6 |
| `basis.reviews` | This report only; old hash-bound reviews remain historical evidence |
| Events | Append exactly the three events in §15.6; old history immutable |
| Generated views | Dispatcher regenerates; reviewer did not edit |
| Scheduler/protocols/tools | No edit licensed |
| Window | Remains `PROVED`, hash `6c50…1ccc4` |
| Instances | Remains `CERTIFIED*` |
| Root | Remains `CERTIFIED*`, hash `513496…b7572` |
| Root route | No level/text change licensed |
| Downstream promotion | **None** |

The reviewer stops here. Installation belongs to the dispatcher.
