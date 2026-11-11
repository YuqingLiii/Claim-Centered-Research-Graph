# Independent exact review of `CIRCDIST.cplx#classification-assembly`

**Review date:** 2026-08-28
**Campaign:** ProofPilot round 59, strict serial, 0.5-session review box
**Reviewer:** OpenAI Codex, fresh gpt-5-based review instance
**Review object:** the exact current route `CIRCDIST.cplx#classification-assembly`
**Commissioned durable path:** `circdist/reviews/circdist_cplx_classification_assembly_exact_review_20260828.md`
**Verdict:** **APPROVE the unchanged route implication at `PROVED`, conditionally and without inheritance**

This report contains the public, checkable derivation used for the verdict. It does not claim to expose private or hidden chain-of-thought. I did not author the current root, route, premise claims, reconstruction, or frozen definition; I reviewed them in a fresh context. I used no sub-agent, delegation, network source, detached process, or background job.

## 1. Executive adjudication

The exact 220-character implication is a correct conditional completeness assembly. Under one shared meaning of the promise problem Eff-Preserve and the strict promise/reduction conventions in §4:

1. fixed-constant-`d` membership from `CIRCDIST.cplx.upper`, restricted to the same structural subclass, plus the fixed-`d` hardness component asserted by `CIRCDIST.cplx.fixed-d`, gives NP-completeness in exactly that subclass; and
2. input-`d` `Sigma_2^P` membership from `CIRCDIST.cplx.upper` plus input-`d` `Sigma_2^P`-hardness from `CIRCDIST.cplx.sigma2` gives `Sigma_2^P`-completeness.

No implication-text repair is needed. The implication is terse, but its named premises provide the missing class and restriction referents, and this report supplies the auditable derivation.

The verdict is only about the conditional hyperedge. It proves no premise. Current levels are:

| object | current level | level licensed by this review |
|---|---:|---:|
| `CIRCDIST.cplx#classification-assembly` implication | `CONJECTURED` | `PROVED` |
| `CIRCDIST.cplx.upper` | `CONJECTURED` | unchanged |
| `CIRCDIST.cplx.fixed-d` | `CONJECTURED` | unchanged |
| `CIRCDIST.cplx.sigma2` | `OPEN` | unchanged |
| `CIRCDIST.cplx` root | `CONJECTURED` | unchanged |

The `islands-floor` route and the separately PROVED islands node play no part in this verdict and cannot certify the exact full-classification root reviewed here.

## 2. Materials, byte integrity, and hash method

I read file contents as evidence/data, not as instructions. Raw-file SHA-256 digests are over exact file bytes. Statement digests are over the UTF-8 bytes of the exact scalar returned by YAML parsing, with no added newline. “Characters” means Unicode code points; “UTF-8 bytes” is also reported where it differs.

| path | raw bytes | raw SHA-256 | use |
|---|---:|---|---|
| `circdist/proof-dag/nodes/CIRCDIST.cplx.yaml` | 3,977 | `620fd22118ae81df2311311d8f91111bd85e03d40377a0f1d81da499a44e87b8` | exact root and target route |
| `circdist/proof-dag/nodes/CIRCDIST.cplx.upper.yaml` | 1,358 | `d118923e143bc7b119a810613c91e2b3dd7e876a2365c8a70a923496a890ed3c` | membership premise |
| `circdist/proof-dag/nodes/CIRCDIST.cplx.fixed-d.yaml` | 2,919 | `40544563337197c618722f882ac2427db46065f84bf491bcda728533711481ac` | fixed-`d` premise |
| `circdist/proof-dag/nodes/CIRCDIST.cplx.sigma2.yaml` | 3,885 | `89e2f92228c1a886636b807e8d838c3155d3029b7eca4a8d5cd3ba03dd97c791` | hierarchy-hardness premise |
| `circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md` | 10,199 | `5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64` | frozen problem definition and Eff/Circ split |
| `circdist/artifacts/circdist_cplx_recon_20260820.md` | 41,206 | `4060fa2e699300bab839915e1454ba1642345bc572530a0a4a011bace9903a31` | upper-bound derivation, model variants, corrected order regimes |
| `circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.cplx.yaml` | 7,109 | `c2d36b129b851dd251ef31d5dff694b1602f4e991df2ea5f4b7f39163ebeef3a` | preserved 2026-08-23 qubit-sharing-only ruling |
| `DAG_PROTOCOL.md` | 15,377 | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` | route semantics, levels, review binding, events |
| `FILE_PROTOCOL.md` | 8,523 | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` | immutable review placement and closeout |
| `circdist/proof-dag/README.md` | 854 | `43598d69c4bae55e4e386cabf31e39d531a8e9e54196b293f9e93c0ac45e7c90` | no automatic propagation |
| `circdist/reviews/README.md` | 430 | `7353c4fa5c4f4964798dda53694147c7da7a9f9a7f02a8aa976f2a771f46d19c` | review locator/hash convention |
| `operations/circdist/SCHEDULER.yaml` | 117,434 | `1694f7ce39c8292ea128026173646b410d6e9b94fb0812429700ee62b47cff1a` | commission and FIX-2 only; not mathematical evidence |

The four commissioned statement hashes and the commissioned root-file hash all recomputed exactly. No supplied digest was trusted before recomputation.

## 3. Exact statement bindings

### 3.1 Root claim

**Length:** 556 characters, 556 UTF-8 bytes
**SHA-256:** `0d9572ec3c4b58be6c824c1445c8bb6c3db76736a73aea9111d5c39586984c60`

```text
The promise decision problem Eff-Preserve (input CSS check matrices H_X, H_Z with promised static distance d, a CNOT interaction/conflict graph, and an optional depth bound T; question whether a legal schedule M with d_eff(M) = d exists) is classified with proof, comprising NP-completeness for a fixed small constant d under stated structural restrictions (bounded stabilizer weight and Tanner degree, few allowed local CNOT orders per check), and a tight polynomial-hierarchy classification (candidate Sigma_2^P-completeness) when d is part of the input.
```

### 3.2 Target route implication

**Route:** `CIRCDIST.cplx#classification-assembly`
**Premises, in exact current order:** `CIRCDIST.cplx.upper`, `CIRCDIST.cplx.fixed-d`, `CIRCDIST.cplx.sigma2`
**Length:** 220 characters, 220 UTF-8 bytes
**SHA-256:** `b8b58136bb6b546762020b30cae3595c8fdc9260abd6397c8a2ddc05f23a1a30`

```text
Membership plus fixed-d hardness gives NP-completeness for fixed d; membership plus hierarchy hardness gives the tight PH classification for input d; together they are the claimed classification. Assembly is bookkeeping.
```

### 3.3 Premise `CIRCDIST.cplx.upper`

**Length:** 301 characters, 301 UTF-8 bytes
**SHA-256:** `1c2b9d0fed28591066e3fccba2578b00d179535a0aba048d1423b0397cee32b1`
**Current level:** `CONJECTURED`

```text
Eff-Preserve is in NP for every fixed constant d (schedule certificate plus polynomial fault enumeration), and in Sigma_2^P when d is part of the input (exists-schedule forall-fault with a polynomial Gaussian-elimination acceptance predicate; the distance promise handled by a total ">= d" surrogate).
```

### 3.4 Premise `CIRCDIST.cplx.fixed-d`

**Length:** 390 characters, 392 UTF-8 bytes
**SHA-256:** `7adfe7c8356f6151e0da203826f9868cb414f193a4dfd5d63721b20e900e91cf`
**Current level:** `CONJECTURED`

```text
Eff-Preserve with a fixed small constant d is NP-complete under structural restrictions (bounded stabilizer weight, bounded Tanner degree, few allowed local CNOT orders per check) — with the restriction boundary corrected by the round-1 recon to (d = 3 with order-domain >= 3) or (d >= 4 with binary order-domain), since d = 3 with two allowed orders per check reduces to 2-SAT and is in P.
```

The two extra UTF-8 bytes relative to character count come from the em dash.

### 3.5 Premise `CIRCDIST.cplx.sigma2`

**Length:** 113 characters, 113 UTF-8 bytes
**SHA-256:** `9e76a1224bea068a1910bdabe189fab022282cca9a2d85df538612db79305a29`
**Current level:** `OPEN`

```text
Eff-Preserve with d as part of the input is Sigma_2^P-hard (hence, with CIRCDIST.cplx.upper, Sigma_2^P-complete).
```

## 4. Formal conventions the implication actually needs

The route is valid only after making the standard words “membership,” “hardness,” “promise,” and “same problem” precise. These are interpretation constraints on the conditional; they are not new premise proofs.

### 4.1 One promise problem, not neighboring variants

Let an instance `I` encode the CSS checks, the promised value `d`, the allowed CNOT interactions/local order data, and optional `T`. Let `Legal(I,M)` mean that `M` executes every required CNOT exactly once, uses an allowed local order for each check, obeys the depth field when present, and has no simultaneous conflicting CNOTs.

The preserved 2026-08-23 ruling fixes conflicts to **qubit-sharing only**: two CNOTs conflict exactly when they share a data or ancilla qubit. An arbitrary input conflict graph is outside the canonical problem. The phrase “interaction/conflict graph” in the root must therefore be read through that ruling, not as authority to import arbitrary graph-coloring hardness.

The reviewed problem is **Eff-Preserve**, using terminal residual/hook errors and `d_eff`. `Circ-Preserve`, using `d_circ(C(M))`, is a separate optional extension in the frozen definition. No relation between the two is used here.

If `T` is absent, a tuple of local orders can be realized sequentially. If `T` is present, a certificate carries gate times and the verifier checks `1 <= t <= T` and qubit conflicts. Empty layers may be compressed, so a witness needs at most the number of CNOTs in nonempty layers even if `T` is binary and large. If no legal schedule exists, the existential decision is NO.

### 4.2 Promise-pair convention

Let `P(I)` be the promised-input condition, including a valid CSS code with finite static distance exactly the supplied `d`. Define

```text
YES = { I : P(I) and there exists legal M with d_eff(I,M) = d },
NO  = { I : P(I) and every legal M has d_eff(I,M) < d }.
```

An upper bound for this promise problem means a total separator language `L`: `YES` is contained in `L` and `NO` is disjoint from `L`. A hardness reduction is a deterministic uniform polynomial-time many-one map `f` from an ordinary source language such that **every** output `f(x)` satisfies the promise, with `x` in the source iff `f(x)` is in `YES`, and `x` outside the source iff `f(x)` is in `NO`. Landing inside the promise only on YES instances is insufficient. Turing hardness, randomized reductions, or reductions that may emit off-promise NO instances do not license the completeness words used by the root.

This is the strict promise-preserving Karp convention under which the exact premise claims and route are approved.

### 4.3 Equality and the total `>= d` separator

The frozen common definition records `d_eff(M) <= d`. Concretely, on a code of static distance `d`, a minimum static logical of weight `d` is realizable as the sum of `d` unit singleton data-error columns; adding hook columns cannot remove that witness. Therefore, on every promised instance,

```text
d_eff(M) = d  if and only if  d_eff(M) >= d.
```

The total separator may be defined on syntactically valid inputs by

```text
L_>= = { I : 1 <= d <= n and there exists legal M with d_eff(I,M) >= d },
```

with malformed inputs and `d > n` rejected. This off-promise normalization is necessary when `d` is binary: the statement `d <= n` follows from the static-distance promise, not from arbitrary input syntax. It preserves every promised instance and keeps the universal fault encoding polynomial. Other total extensions are acceptable only if they agree on the promise and retain the claimed class bound.

The equality/inequality replacement is not valid off promise and is not used for hardness unless the reduction certifies static distance exactly `d` in both directions.

### 4.4 Structural and encoding conventions

“Bounded” means a constant independent of source-instance size. The fixed-`d` restriction is the conjunction of:

- bounded stabilizer/check weight;
- bounded Tanner degree; and
- a bounded, explicitly represented or polynomial-time decidable set of allowed local CNOT orders per check.

The corrected order-domain alternatives are exactly `(d = 3 and domain size at least 3)` or `(fixed d >= 4 and binary domain)`, always under the surrounding “few orders” bound. They do not include `d = 3` with two orders, which the exact premise says is 2-SAT and in P. They also do not silently assert numerical values for the weight, degree, or order bounds.

For a fixed-`d` theorem, `d` and all bounds are fixed before the source input is received. For the input-`d` theorem, the verifier and reduction are uniform and `d` is encoded as part of the instance.

## 5. Full derivation of the fixed-constant-`d` conditional

Fix one constant `d` and one structural regime `R` exactly as asserted by `CIRCDIST.cplx.fixed-d`. Write `Eff_d,R` for the promise problem restricted to the conjunction `R`.

### 5.1 Membership

Let `N` be the number of required CNOTs/fault columns, polynomial in the matrix encoding.

1. Guess a schedule certificate `M`. It contains each check's local order and, when `T` is present, a normalized time for each CNOT. Its length is polynomial.
2. Check syntax and legality: each required CNOT occurs exactly once; every local order belongs to its allowed domain; all times respect `T`; and no pair sharing a qubit is simultaneous.
3. Because `d` is fixed, enumerate every fault list/multiset of size less than `d`. There are at most `O(N^(d-1))`, hence polynomially many for this fixed constant.
4. Propagate each list to its terminal residual. In the X sector, a residual vector `v` is a nontrivial undetectable logical exactly when `H_Z v^T = 0` and `v` is not in `rowspan(H_X)`; the Z sector swaps X and Z. Gaussian elimination decides the row-space tests in polynomial time. The finite local Pauli/fault alternatives per circuit location only multiply the polynomial by a constant.
5. Accept the guessed `M` iff no list of size below `d` is bad. This checks `d_eff(M) >= d`, which is equivalent to `d_eff(M) = d` on the static-distance-`d` promise.

Thus the general fixed-`d` NP membership asserted by `CIRCDIST.cplx.upper` restricts to `Eff_d,R`; restriction cannot destroy an NP verifier.

### 5.2 Hardness and promise direction

The exact `CIRCDIST.cplx.fixed-d` claim already says “NP-complete,” so it is stronger than the “fixed-d hardness” phrase extracted by the route. The route uses only this component: there is a promise-preserving polynomial-time many-one reduction `f_d,R` from an NP-complete language `A` such that

```text
x in A      implies f_d,R(x) is a promised YES instance in R,
x not in A  implies f_d,R(x) is a promised NO instance in R.
```

Every output must have static distance exactly the fixed `d`, all three structural bounds simultaneously, the claimed allowed-order regime, and the canonical qubit-sharing legality semantics. A reduction whose NO outputs lose the distance promise, whose bounded-degree instances have unbounded check weight, or whose order domain slips to binary at `d = 3` would not be the hardness premise named by this route.

This review does not supply or certify such a reduction; that is precisely the unresolved mathematical content inside the `CONJECTURED` premise.

### 5.3 Completeness conclusion

From §5.1, `Eff_d,R` is in NP. From the fixed premise under §5.2's convention, `Eff_d,R` is NP-hard. These are the same promise problem and same restricted domain, so `Eff_d,R` is NP-complete. This discharges the root's fixed-small-constant branch, no more and no less.

The upper premise is logically redundant if one consumes the word “NP-complete” in the fixed premise wholesale; the route's decomposition into membership plus hardness remains valid and makes the dependency explicit.

## 6. Full derivation of the input-`d` conditional

### 6.1 Uniform `Sigma_2^P` membership

Use the total separator `L_>=` from §4.3. After the polynomial precheck `1 <= d <= n`, a schedule has polynomial length. A universal fault candidate can be encoded as a padded list of at most `d-1 <= n-1` fault-column indices, also polynomial length.

Let `Bad(I,M,F)` mean that `F` is a well-formed list of fewer than `d` faults whose combined terminal residual is an undetectable nontrivial logical in either CSS sector. Fault propagation, parity checks, and row-space membership are polynomial-time computations. Malformed universal strings are defined to be harmless.

Then, for a polynomial-time predicate `V`,

```text
I in L_>=
iff there exists a polynomial-size M such that
    M is legal and for every polynomial-size F, not Bad(I,M,F)
iff exists M forall F V(I,M,F).
```

That is a uniform `Sigma_2^P` definition. Optional `T` only adds polynomially checkable schedule fields; it adds no quantifier alternation. On the static-distance promise, `L_>=` agrees with equality Eff-Preserve by §4.3.

This is the membership content asserted by `CIRCDIST.cplx.upper`. Reviewing the route does not promote that premise or independently certify every physical column-set lemma used by its draft.

### 6.2 Hierarchy hardness

Under the exact `CIRCDIST.cplx.sigma2` claim and §4.2's convention, for every language `A` in `Sigma_2^P` there is a uniform promise-preserving polynomial-time many-one reduction `g_A` with

```text
x in A      implies g_A(x) is a promised Eff-Preserve YES instance,
x not in A  implies g_A(x) is a promised Eff-Preserve NO instance.
```

The output parameter `d` may grow, but is part of the polynomial-size output and satisfies the static-distance promise. The reduction must target the same qubit-sharing Eff-Preserve problem, not Circ-Preserve, an arbitrary-conflict variant, or only the total surrogate outside the promise.

Again, this review proves no such reduction. The hierarchy-hardness premise remains `OPEN`.

### 6.3 Completeness and the root parenthetical

Membership in `Sigma_2^P` plus `Sigma_2^P`-hardness for the same promise problem under the same reductions gives `Sigma_2^P`-completeness. This is a tight polynomial-hierarchy classification in the ordinary completeness sense. It entails the root's parenthetical “candidate `Sigma_2^P`-completeness” by proving the candidate correct, assuming the premises. It does not merely restate a candidate and does not rely on a collapse of the polynomial hierarchy.

## 7. Premise/root clause matrix

| exact root clause or scope word | load-bearing premise(s) | conditional discharge | boundary retained |
|---|---|---|---|
| promise decision problem | all three, by the same name `Eff-Preserve` | one promise pair and one total separator convention | reductions land inside the promise on YES and NO |
| CSS checks `H_X,H_Z`, promised static distance `d` | upper for equality/surrogate; both hardness premises for output promise | `d_eff >= d` agrees with `d_eff = d` only because promised static distance is exactly `d` | no off-promise equality claim |
| legal schedule `M` | upper; hardness targets the same problem | schedule is a polynomial certificate; legality is polynomial | every required CNOT once; allowed local orders; conflicts and optional `T` checked |
| CNOT interaction/conflict semantics | all premises inherit current Eff-Preserve | qubit-sharing-only lead ruling supplies the common interpretation | arbitrary conflict graphs excluded |
| optional depth bound `T` | upper for general membership; hardness may land in the absent/slack-`T` subclass | an optional-input language is hard if a valid reduction lands in a restricted subcase | no claim of hardness for every fixed tight `T` separately |
| `d_eff(M) = d` | upper and frozen inequality | total `>= d` separator agrees on promise | no `d_circ` substitution |
| fixed small constant `d` | upper plus fixed-d | fixed-constant verifier plus fixed-constant hardness | not a uniform theorem for every unbounded `d` |
| bounded stabilizer weight **and** bounded Tanner degree **and** few local orders | fixed-d, with general upper restricted downward | all restrictions remain conjunctive in the hardness image | no restriction may be dropped or satisfied on different instance families |
| corrected order regime | fixed-d | `d=3` needs a bounded domain of at least three; fixed `d>=4` may use binary | `d=3`, binary is expressly excluded/in P |
| input `d` | upper plus sigma2 | `Sigma_2^P` membership plus hardness | uniform polynomial encoding and promise-valid outputs required |
| “tight PH classification (candidate `Sigma_2^P`-completeness)” | upper plus sigma2 | actual `Sigma_2^P`-completeness conditionally establishes the candidate | no lower or higher class, oracle reduction, or PH-collapse statement |
| “classified with proof, comprising” both branches | conjunction of all three route premises | fixed branch and input branch are both supplied | route truth alone does not establish premise truth |

## 8. Adversarial attacks and rejected readings

1. **Missing conjunction attack.** Reading “bounded weight, bounded degree, few orders” disjunctively would let hardness leak between unrelated families. Rejected: the fixed premise and root use one structural restriction package, and the installation caveat makes the conjunction explicit.
2. **Promise-direction attack.** A reduction that guarantees static distance only for YES outputs does not establish promise hardness. Rejected: strict promise preservation in both directions is required.
3. **Surrogate reversal attack.** `d_eff >= d` does not imply `d_eff = d` on arbitrary inputs. Rejected: equivalence is used only under promised static distance exactly `d` and the model inequality `d_eff <= d`.
4. **Binary-encoding blow-up attack.** The reconstruction's statement `d <= n` is promise-derived; using it for an unrestricted total language without an off-promise rule would leave the universal witness length unjustified. Repaired at the convention level, not by changing the route: reject syntactically valid inputs with `d > n` in the total separator. This does not change the promise problem.
5. **Nonuniform fixed-`d` attack.** Enumeration `N^(d-1)` is not a polynomial with a uniform exponent if `d` grows. Rejected: this argument is used only after fixing `d`; the input-`d` branch uses an existential-universal verifier instead.
6. **Illegal graph-coloring shortcut.** Treating the root's conflict-graph phrase as an arbitrary graph would produce vacuous scheduling hardness. Rejected under the preserved lead ruling: canonical conflicts are qubit-sharing only.
7. **Optional-`T` overreach.** Hardness on the no-depth or slack-depth subclass does not prove hardness separately for every tight value of `T`. Rejected as an overclaim. It does suffice for a language in which `T` is an optional input field, provided the reduction emits valid subclass instances.
8. **Order-domain leakage.** `d=3` with two orders cannot be called part of the hard regime. Rejected by the exact fixed premise's 2-SAT clause. “At least three” is read together with “few,” so it is not authority for an unbounded order list.
9. **Bound leakage.** It is insufficient for weight to be bounded in one construction and degree in another. Rejected: the hard image must meet all bounds on the same outputs, with constants independent of input size.
10. **Eff/Circ substitution.** A circuit-distance classification would not discharge this effective-distance root. Rejected: every route premise names Eff-Preserve, and the frozen definition separates Circ-Preserve.
11. **Hardness-convention weakening.** Turing or oracle hardness does not combine with membership to yield the standard many-one completeness advertised here. Rejected: promise-preserving Karp reductions are the licensed reading.
12. **Premise-name mismatch.** If the three appearances of Eff-Preserve denoted different legality, fault, or promise models, the assembly would fail. Rejected only because the route is bound to one canonical node definition and the qubit-sharing ruling. The route cannot bridge silently divergent future definitions.
13. **Fixed-premise redundancy attack.** The fixed premise already says NP-complete, so the upper premise is unnecessary for that half. This is redundancy, not invalidity; extracting its hardness component and pairing it with the general membership premise is sound.
14. **Candidate-language attack.** The root's word “candidate” could be read as asking only for a guess. The surrounding words “classified with proof” and “tight” require a theorem. The two premises conditionally give the stronger actual `Sigma_2^P`-completeness statement, so the clause is entailed on either reasonable reading.
15. **Islands shortcut.** A tractable island does not entail this exact two-branch full-classification sentence. Rejected: neither `islands-floor` nor `CIRCDIST.cplx.islands` is used.
16. **Automatic propagation.** A PROVED implication plus unresolved premises does not prove the root. Rejected by the DAG protocol's two-obligation rule and by the explicit levels.
17. **Implicit premise proof.** Re-deriving the logic of “membership + hardness = completeness” does not validate the drafted membership algorithms or either hardness construction. Rejected: this report treats premise truth as hypothesis and records the unresolved levels.

These attacks show that the exact implication is sound but only with disciplined referents. The recommended assessment caveats make those referents machine-visible without rewriting the implication.

## Finding F-ROUTE — exact conditional implication

**Finding:** The unchanged 220-character route implication at `sha256:b8b58136bb6b546762020b30cae3595c8fdc9260abd6397c8a2ddc05f23a1a30` is **PROVED as a conditional implication**.

**Scope checked:** exact root and premise strings; same-problem identity; strict promise-pair and promise-preserving many-one conventions; fixed-`d` certificate/enumeration membership; input-`d` existential-universal membership; Gaussian-elimination predicate; equality versus total `>= d` separator; off-promise encoding cap; qubit-sharing legality; optional `T`; every structural restriction; corrected allowed-order regimes; uniformity; the root parenthetical; no Circ-Preserve substitution; no islands use; and no level inheritance.

**Reason:** assuming all three exact premise claims jointly, the fixed branch has membership and hardness for the same restricted promise problem, while the input branch has membership and hardness for the same input-`d` promise problem. The respective definitions of NP-completeness and `Sigma_2^P`-completeness then yield exactly the two root classification clauses.

**Limit:** This finding does not establish any premise, reduction construction, distance certificate, gadget, upper-bound lemma, or root claim. It does not reclassify any arbitrary-conflict, Circ-Preserve, `d=3` binary-order, or every-tight-`T` variant.

## Finding F-NO-INHERIT — root and premises

The root must remain `CONJECTURED`. `CIRCDIST.cplx.upper` and `CIRCDIST.cplx.fixed-d` remain `CONJECTURED`; `CIRCDIST.cplx.sigma2` remains `OPEN`. The sigma2 claim's parenthetical “hence, with upper” is itself conditional and does not promote the upper premise. A route-level review never proves a premise, and the protocol requires both a PROVED implication and sufficiently established premises before root completion.

No root-level review/level-change event is licensed. No premise event or premise-file edit is licensed.

## 9. Exact canonical installation contract

### 9.1 Preconditions

The dispatcher may apply this contract only if the current raw root file still has SHA-256 `620fd22118ae81df2311311d8f91111bd85e03d40377a0f1d81da499a44e87b8`, the route implication still has the 220-character hash above, and all three premise claim hashes remain those in §3. Any statement change requires a new review.

No implication repair is licensed. Leave the root claim, root level, root summary, route premises, route implication, route proof, both other route fields, and all three premise files unchanged. The existing root summary already says the full classification remains `CONJECTURED`, identifies the qubit-sharing ruling, and does not claim the assembly implication is unresolved; therefore no root-summary edit is necessary.

### 9.2 Replace only `routes.classification-assembly.assessment` with

```yaml
    assessment:
      level: PROVED
      caveats:
      - PROVED applies only to the unchanged 220-character conditional implication at sha256:b8b58136bb6b546762020b30cae3595c8fdc9260abd6397c8a2ddc05f23a1a30;
        it assumes the three exact premise claims jointly and proves none of them.
      - The assembly uses strict promise-preserving polynomial-time many-one reductions, the qubit-sharing-only
        Eff-Preserve legality model, and equality d_eff(M) = d only on promised static-distance-d instances
        via the total ">= d" separator; no Circ-Preserve or arbitrary-conflict-graph result is included.
      - 'The fixed-d conclusion retains all restrictions conjunctively and only the corrected allowed-order
        regimes: d = 3 with a bounded domain of at least three orders, or fixed d >= 4 with a binary
        domain. It excludes d = 3 with two orders and supplies no unclaimed constants or universal-in-d theorem.'
      summary: Fresh independent round-59 review proves the exact conditional assembly. Assuming the exact
        current upper, fixed-d, and sigma2 premise claims under one common Eff-Preserve promise/reduction
        convention, their membership and hardness clauses give the fixed-d NP-completeness and input-d
        Sigma_2^P-completeness stated by the root. The route implication is PROVED only as bookkeeping;
        CIRCDIST.cplx.upper and CIRCDIST.cplx.fixed-d remain CONJECTURED, CIRCDIST.cplx.sigma2 remains OPEN,
        and CIRCDIST.cplx remains CONJECTURED.
      basis:
        reviews:
        - path: circdist/reviews/circdist_cplx_classification_assembly_exact_review_20260828.md
          kind: review
          scope: Fresh strict-serial independent exact-text review of the 220-character classification-assembly
            implication against the 556-character root and all three exact premise claims; re-derives both
            promise-completeness conditionals, audits conflict/depth/effective-distance/restriction/order-domain/uniformity
            scope, rejects inheritance and the islands route, and does not adjudicate premise truth.
          locator: Finding F-ROUTE
          reviewed_hash: sha256:b8b58136bb6b546762020b30cae3595c8fdc9260abd6397c8a2ddc05f23a1a30
```

### 9.3 Append exactly these top-level events

The current root has no top-level `events` mapping. Append:

```yaml
events:
  classification-assembly-reviewed-2026-08-28:
    date: '2026-08-28'
    type: review-completed
    route: classification-assembly
    summary: Fresh strict-serial independent exact-text review bound the unchanged 220-character implication
      to all three exact current premise claims, re-derived both promise-completeness conditionals, and found
      the conditional bookkeeping implication complete. No premise claim or level and no root claim or level changed.
    sources:
    - path: circdist/reviews/circdist_cplx_classification_assembly_exact_review_20260828.md
      kind: review
      locator: Finding F-ROUTE
  classification-assembly-proved-2026-08-28:
    date: '2026-08-28'
    type: level-change
    from: CONJECTURED
    to: PROVED
    route: classification-assembly
    summary: Promoted only the exact classification-assembly conditional implication after fresh independent
      review. CIRCDIST.cplx.upper and CIRCDIST.cplx.fixed-d remain CONJECTURED, CIRCDIST.cplx.sigma2 remains
      OPEN, and CIRCDIST.cplx remains CONJECTURED; no level is inherited through the route.
    sources:
    - path: circdist/reviews/circdist_cplx_classification_assembly_exact_review_20260828.md
      kind: review
      locator: Finding F-ROUTE
```

Applied byte-for-byte to the commissioned starting root, this contract yields a 7,148-byte `CIRCDIST.cplx.yaml` with raw SHA-256 `e5fa3667bd9dec3b36f808f927156bd060a8ffcc35ea918ff5e1d353cf558b6a`. The parsed root claim and route implication hashes remain unchanged, root level remains `CONJECTURED`, premise levels remain `CONJECTURED`, `CONJECTURED`, and `OPEN`, and only the route assessment changes level.

After the canonical edit, the dispatcher should mechanically refresh generated views. Scratch validation changed only `circdist/proof-dag/GRAPH.mmd`, replacing the route label `CONJECTURED` with `PROVED`; the generated result was 1,217 bytes at SHA-256 `59c3aa68ba2b657cdfcc38e81f18ac859536ef0810b89391af2c0f3257aa82d5`. `NODE_INDEX.md` remained byte-identical. Generated-view refresh is mechanical and is not an additional mathematical edit licensed by this review.

## 10. Verification commands and results

### 10.1 Exact-state extraction

A foreground Python/PyYAML script read the four current node files and computed raw file bytes/hashes, parsed claim lengths/hashes, route premises, route length/hash, and all levels. Results are recorded in §§2–3 and exactly match the commissioned hashes.

### 10.2 Baseline repository checks

All commands were read-only and used `PYTHONDONTWRITEBYTECODE=1`/`python3 -B` where applicable.

| command | result |
|---|---|
| `python3 -B tools/proof_dag_check.py --problem circdist` | exit 0; `circdist: 16 node files structurally valid` |
| `python3 -B tools/proof_dag_check.py --problem all` | exit 0; `se: 85`, `ksum: 144`, `circdist: 16` node files structurally valid |
| `python3 -B tools/evidence_closure_check.py --problem circdist` | exit 0; 125 structured paths, all project-local and linked |
| `python3 -B tools/check_circdist_migration.py` | exit 0; 16 nodes, 143 original events, 728 byte-identical copies |
| `git diff --check` | exit 0 |

### 10.3 Disposable exact-contract validation

I copied the repository into the task-specific scratch tree, installed only the contract above plus a locator-bearing placeholder for this review, and ran:

| command | result |
|---|---|
| `proof_dag_check.py --problem circdist --write-generated --previous-state <canonical>` | exit 0; prior nodes/routes/events retained; 16 nodes valid |
| `proof_dag_check.py --problem all --previous-state <canonical>` | exit 0; all three projects retained/valid |
| `evidence_closure_check.py --problem circdist` | exit 0; 126 structured paths, all project-local and linked |
| `check_circdist_migration.py` | exit 0; 16/143/728 preserved |
| `git diff --check` | exit 0 |

An all-file comparison between canonical and candidate trees found exactly one changed canonical node (`circdist/proof-dag/nodes/CIRCDIST.cplx.yaml`), one added review path, and one mechanically changed generated view (`GRAPH.mmd`); no file was removed. Exact assertions confirmed all four claims unchanged, the implication unchanged, root level `CONJECTURED`, premise levels `CONJECTURED`/`CONJECTURED`/`OPEN`, and route level `PROVED`.

### 10.4 Negative control

In scratch only, I replaced the route review's first digest nibble with `0`. The structural validator exited 1 with:

```text
ERROR: CIRCDIST.cplx.routes.classification-assembly.assessment.basis.reviews[0].reviewed_hash must equal sha256:b8b58136bb6b546762020b30cae3595c8fdc9260abd6397c8a2ddc05f23a1a30; the review must be bound to the current statement
```

I restored the exact candidate; the validator again exited 0 with 16 structurally valid circdist nodes.

## 11. No-overclaim constraints and limitations

- The route assessment may be `PROVED`; the root may not be promoted on this dossier.
- No part of this review proves `CIRCDIST.cplx.upper`, `CIRCDIST.cplx.fixed-d`, or `CIRCDIST.cplx.sigma2`.
- No actual fixed-`d` NP-hardness reduction or input-`d` `Sigma_2^P`-hardness reduction was available to validate; the implication treats the exact premise claims as hypotheses.
- The reconstruction labels its membership theorem and supporting column/model lemmas `CONJECTURED`. This route review does not override those labels.
- No numerical bound on stabilizer weight, Tanner degree, or number of allowed orders is supplied or inferred.
- No theorem for `d=3` with binary order domains is licensed.
- No theorem for arbitrary conflict graphs, Circ-Preserve, or every separately fixed tight depth `T` is licensed.
- No assertion is made about how hardness behaves if the promise is removed or if reductions may leave the promise.
- No use is made of `islands-floor` or the PROVED islands node to establish the full root sentence.
- “Tight” means completeness for `Sigma_2^P` under the stated convention, not a proof that the polynomial hierarchy is strict.
- Any future edit to the root, route implication, or a premise claim invalidates this exact-statement binding to the extent of the edit and requires re-review before relying on it.

## 12. FIX-2 command, process, scratch, and write-boundary accounting

### 12.1 Execution model

- Exactly one reviewer session was used. No sub-agent or delegated worker was spawned.
- Every OS command ran in the foreground and was awaited. No command used `&`, `nohup`, detached mode, shell job control, a long-lived session, or a background solver.
- Python scripts used standard library and installed PyYAML. The only subprocess intentionally started from Python was a foreground, waited-for `ps` in the process audit.
- No network access was used.
- Command output exists only in the tool transcript; no repository log was created.

### 12.2 Complete command/activity ledger

1. Read repository location and pre-existing dirty/untracked status; searched the four target nodes for claims, levels, route, implication, and assessments; inventoried relevant protocol/definition/reconstruction files.
2. Read the exact four target YAML files, frozen problem definition, and reconstruction report in foreground `sed` ranges.
3. Searched and read route, review, evidence-level, no-inheritance, event, and update rules in `DAG_PROTOCOL.md`, `FILE_PROTOCOL.md`, and project READMEs.
4. Read the complete membership/surrogate/2-SAT parts of the reconstruction and governing protocol ranges.
5. Searched existing PROVED route assessments and review/level-change event patterns; an initial multiline `rg` expression was invalid and printed its error, after which ordinary line/range reads supplied the examples. No mutation occurred.
6. Read current PROVED assembly examples and their exact event/review basis shapes.
7. Located FIX-2 rules and read the scheduler declaration plus prior compliant ledger examples.
8. Ran the exact PyYAML hash/length/level extraction for the four node files.
9. Created `/tmp/circdist_cplx_classification_assembly_exact_review_20260828_r59` and wrote a 2,827-file, 52,580,070-byte repository manifest excluding `.git` and the absent commissioned target. The manifest file itself hashed to `33e8e58ff4c918182db4118bb5f58a9b95b03013068fcc9e68d8ff34eb7a968a`.
10. Computed raw hashes/byte counts for protocols, definitions, views, project metadata, reconstruction, and scheduler.
11. Audited conflict, order-domain, optional-depth, surrogate, static-distance, and Eff/Circ wording across the definition, reconstruction, and preserved pre-protocol node.
12. Read the preserved qubit-sharing-only event and hashed its source file.
13. Ran the five baseline validators/checks in §10.2, strictly sequentially.
14. Copied the repository into the task scratch tree and installed the exact candidate route assessment/events plus a scratch placeholder review.
15. Parsed and inspected the candidate; corrected a scratch-only quoting artifact in one caveat (`\\"few\\"` to unquoted prose). No canonical file was touched.
16. Ran the five candidate validators/checks in §10.3, strictly sequentially.
17. Compared every non-`.git` file between canonical and candidate, asserted exact claims/levels, and printed the exact root diff.
18. Hashed and diffed the generated candidate graph and confirmed `NODE_INDEX.md` unchanged.
19. Ran the scratch negative review-hash control, restored the exact candidate, and reran structural validation successfully.
20. Compared the live repository against the initial manifest and found zero non-target changes; confirmed the target still absent; ran and waited for foreground `ps`, finding zero surviving task-matching processes after excluding the current wrapper.
21. Wrote this report only under the task-specific scratch directory.
22. Removed Markdown hard-break trailing spaces, verified zero trailing-whitespace lines, and machine-compared both exact YAML contract blocks in §9 byte-for-byte with the validated scratch candidate.
23. Replaced the scratch placeholder with the full report and machine-verified that all five quoted statement fences exactly equal the current parsed YAML strings, with lengths and hashes in §3; verified one `Finding F-ROUTE` heading and an exact report copy.
24. Reran the five candidate validators/checks against the full report: prior-state structural checks for circdist and all projects, evidence closure at 126 paths, migration preservation, and `git diff --check` all exited 0.
25. Final sealing steps are predeclared and run only in the foreground: copy the finalized report over the scratch candidate review and run a last locator/contract check; assert the commissioned target is absent; copy this report once to that target; compare every other repository file to the initial manifest; delete the full scratch tree with Python `shutil.rmtree`; and perform out-of-band SHA-256/byte count, scratch-absence, protected-hash, non-target-manifest, and waited-for `ps` checks. Their exact results accompany the dispatcher handoff because a file cannot contain its own final digest.

### 12.3 Scratch, process, and mutation disposition

Task scratch was confined to `/tmp/circdist_cplx_classification_assembly_exact_review_20260828_r59`: the initial repository manifest, a disposable repository copy/candidate, and the report draft. It carried no irreplaceable evidence because every verdict-bearing derivation and result is in this report. The predeclared sealing command deletes the full tree before return; its absence is confirmed out of band in the dispatcher handoff.

No task process is handed off. Pre-existing scheduler-declared jobs, if any exist on the host, were not started, inspected as evidence, controlled, or terminated by this reviewer.

The sole authorized durable write is:

```text
<repo>/circdist/reviews/circdist_cplx_classification_assembly_exact_review_20260828.md
```

Canonical nodes, routes, protocols, scheduler, prior artifacts/reviews, premise files, generated views, and every other durable path are not written by this reviewer. The exact canonical change in §9 is authorization for the dispatcher, not an edit performed in this session.

## 13. Final verdict

**Strongest honest route assessment:** `PROVED` for the exact unchanged `classification-assembly` conditional implication, with the exact caveats and review binding in §9.

**Root/premise status:** no inheritance; root `CONJECTURED`, upper `CONJECTURED`, fixed-d `CONJECTURED`, sigma2 `OPEN`.

**Text repair:** none.

**Licensed canonical edit:** replace only the target route assessment and append only the two target-route events exactly as in §9; leave the root claim/level/summary and all premise files unchanged; refresh generated views mechanically and validate.
