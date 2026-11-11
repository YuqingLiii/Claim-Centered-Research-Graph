# CIRCDIST.cplx.sigma2 — Round 82 R5 deep-seed / direct flagged-quotient construction

**Date:** 2026-08-30 (America/New_York)  
**Role:** strict-serial proposer, explicit lead override of the recorded stop-loss  
**Exact target:** “Eff-Preserve with `d` as part of the input is `Sigma_2^P`-hard (hence, with `CIRCDIST.cplx.upper`, `Sigma_2^P`-complete).”  
**Verdict:** **NOT PROVED; canonical level must remain `OPEN`.**  
**Useful settlement:** a complete `QSAT_2` flagged-syndrome encoding, a complete input-`d` opposite-sector/static-promise repair, two exact compiler counterexamples, and a single finite equality-normal-form residual.

This is a public mathematical argument and reproducibility record. It does not purport to expose hidden reasoning. The status words below are literal:

- **PROVED-IN-ARTIFACT** means a complete proof is given here.
- **CONDITIONAL** means every stated premise is displayed and the missing premise is named.
- **REFUTED** means an explicit counterexample or general scoped obstruction is given.
- **NUMERICAL** means exact finite enumeration, useful for falsification but not a universal proof.
- **OPEN RESIDUAL** means no node promotion follows.

## 0. Executive adjudication

The requested hardness theorem is not established. The from-scratch route does, however, get much closer to the frozen problem than the legacy DEEP-FLAG route:

1. Starting from
   \[
     \exists x\;\forall y\;\Phi(x,y),
   \]
   with `Phi` in 3DNF, §3 constructs in polynomial time a grouped binary syndrome system. A schedule chooses `x`; a fault set chooses `y` and one locally satisfying assignment per clause of `psi = not Phi`. A target representation of weight at most `K` exists exactly when `psi(x,y)` is true. This theorem is **PROVED-IN-ARTIFACT** and does not use a seed-depth predicate, covering radius, or repetition-padding transfer.
2. Adding one flagged anchor turns that representation theorem into the exact abstract quantifier chain
   \[
   \exists\alpha\;\forall F, |F|<K+2:\ F\text{ is not flagged}
   \iff
   \exists x\;\forall y\;\Phi(x,y).
   \]
   This abstract theorem is **PROVED-IN-ARTIFACT**.
3. A four-qubit affine plane realizes the local schedule choice between two abstract columns. The naive code that stabilizes only the planes is **REFUTED**: homogeneous zero relations become unintended logicals. A concrete true QBF is rejected by a four-fault shortcut (§5).
4. Taking `H_X` to generate the full kernel of the physical label matrix fixes that quotient error and is polynomial. The single-anchor version then has a weight-two `Z` logical, so it violates the static-distance promise for every requested `d>2`. All-or-none replicated anchors have the same dual obstruction (§6).
5. That opposite-sector failure is repairable. The cluster expansion `R_R` in §7 preserves static and effective `X` behavior, multiplies static `Z` distance by `R`, and—under an explicit layer-major order—forces `d_eff^Z >= R`. An explicit `d x d` repetition-grid CSS block has static and effective distance exactly `d`. Direct sum with that block pins the promised total static distance to exactly `d`. These are **PROVED-IN-ARTIFACT** and are independent of the fixed-`d` private-sentinel theorem.
6. The remaining compiler obligation is measuring the complement of the local plane rows inside `ker B`. Arbitrary Gaussian-basis orders fail on a 40-qubit instance: a complement-check suffix replaces the inconsistent universal assignment and creates a five-fault logical at requested `d=6` (§8.2).
7. A systematic basis and group-block order prove a sharp lower bound: every bad flag mechanism uses at least `K+1` faults (§8.4). The intended counterexample mechanism uses exactly `K+1`. The sole missing statement is the equality case: every `K+1`-fault mechanism must normalize to one genuine allowed option per group. Section 8.5 freezes this as the finite **Relation/Interval Normal-Form Lemma (RIN)**. No counterexample to RIN was found in the exact bounded census, but no universal proof was found either.

Therefore a later exact reviewer may license the independent lemmas in §§3, 4, 5.1, 6.1, 7, 8.3–8.4 and the scoped no-go results. A reviewer may **not** license `QSAT_2 <=_m Eff-Preserve`, hierarchy hardness, completeness, a canonical node edit, or inheritance from the fixed-`d` theorem.

## 1. Bound inputs and source boundary

All load-bearing inputs were hashed before mathematical work and rehashed before the sole durable write. Every row below was unchanged at the second check.

| path | bytes | lines | SHA-256 |
|---|---:|---:|---|
| `DAG_PROTOCOL.md` | 15,377 | 283 | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | 8,523 | 166 | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| `operations/circdist/SCHEDULER.yaml` | 193,886 | 2,448 | `83c0adad8f500075e93d151130783a559e61b15bd068d195816c86e3f8e9332a` |
| `circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md` | 10,199 | 243 | `5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64` |
| `circdist/proof-dag/PROJECT.yaml` | 107 | 7 | `c65a2cc0c65576dfdcaf6fbc787762708fe78b8b75daa440765ac08b1ba40d0d` |
| `circdist/proof-dag/nodes/CIRCDIST.cplx.sigma2.yaml` | 3,885 | 48 | `89e2f92228c1a886636b807e8d838c3155d3029b7eca4a8d5cd3ba03dd97c791` |
| `circdist/artifacts/circdist_cplx_sigma2_20260822.md` | 52,264 | 934 | `b45e9803f717b0572521eda4877d290acec806433e7c16b2b2ef4daec1576e31` |
| `circdist/artifacts/circdist_cplx_q1_20260822.md` | 40,756 | 770 | `28868e047511c2300356c3e0a15a09a42f422dcef65a056b7ddd2bbb214d2890` |
| `circdist/artifacts/circdist_cplx_sigma2_covering_radius_primary_source_20260826.md` | 42,975 | 642 | `396216942cc18c2b06e61d7ed9fb220f164d0682d15e5bcf87eb6cfea8fa5958` |
| `circdist/proof-dag/nodes/CIRCDIST.cplx.upper.yaml` | 5,453 | 80 | `47260df53e4491c86e10f6ccdebadf47b1161d2533339fd9c499f389a8eb2321` |
| `circdist/reviews/circdist_cplx_upper_membership_exact_review_20260828.md` | 52,336 | 875 | `5e593a927d7ad55966b2362d721f98c7d5dab75c30b334edede81bda4ccbac70` |
| `circdist/proof-dag/nodes/CIRCDIST.cplx.fixed-d.yaml` | 9,392 | 151 | `024a6d6d7d9a656c5ede53043b64601f13023fe0adbec6fe066ae67fb8303bbf` |
| `circdist/reviews/circdist_cplx_fixed_d_private_sentinel_exact_review_20260829.md` | 46,380 | 947 | `e91f7290d5ffab53347fe0bfc477954c087895e133b9234539f120422092cddd` |
| round-64 `README.md` | 20,689 | 357 | `0606b8b6377fae42a20f606250f7186258cccbd9d04aa7a4ca288cd6371639b5` |
| round-66 `THEOREM.txt` | 1,000 | 1 | `0b184c505c31760d7f333fdba019ea583c7686d55ab5796d126eb0dc2857f6ee` |

The recorded node is `OPEN`. The historical Theorems A, D, E and DEEP-FLAG residual are marked conjectural/numerical in their source artifact and are not used as proved premises. The Q1 Seed Barrier forbids putting hardness into a named seed's naked depth; this construction has no deep-seed predicate at all and attacks the frozen problem directly. The covering-radius source audit is only a source boundary and is not used as a reduction. No attempt was made to reacquire McLoughlin's text.

The private-sentinel review is used only to check that its exact scope cannot repair this input-`d` construction: its map preserves static `d_Z` and its effective `Z` theorem is specific to the one/two-fault, `d=3` regime. The general `R_R` theorem below is rederived from first principles.

## 2. Frozen model, rederived

All vector spaces are over `F_2`. For a CSS pair with `H_X H_Z^T=0`, write

\[
 S_X=\operatorname{row}H_X,\quad N_X=\ker H_Z,\qquad
 S_Z=\operatorname{row}H_Z,\quad N_Z=\ker H_X.
\]

The static sector distances are

\[
 d_X=\min\{\operatorname{wt}e:e\in N_X\setminus S_X\},\qquad
 d_Z=\min\{\operatorname{wt}e:e\in N_Z\setminus S_Z\},
\]

with an empty sector interpreted as infinite, and `d=min(d_X,d_Z)`.

For an ordered check `(q_1,...,q_w)`, the terminal same-sector residuals of one fault are the physical singletons and proper suffixes

\[
 T_i=e_{q_{i+1}}+\cdots+e_{q_w},\qquad 1\le i<w.
\]

Let `Gamma_X(M)` contain every physical singleton and every proper suffix of every ordered `X` check; define `Gamma_Z(M)` by the mirror construction. A sector-`X` fault vector `f` is bad exactly when

\[
 H_Z\Gamma_X f^T=0,\qquad \Gamma_Xf^T\notin S_X,
\]

and analogously in `Z`. Thus

\[
 d_{\rm eff}^X(M)=\min\{\operatorname{wt}f:f\text{ is bad in }X\},qquad
 d_{\rm eff}(M)=\min(d_{\rm eff}^X,d_{\rm eff}^Z).
\]

Singleton columns give `d_eff(M)<=d`. On a promised static-distance-`d` input, preservation is exactly the absence of a bad fault set of size `<d` in both sectors. With no optional depth bound, a global serial execution realizes every tuple of allowed local orders under the frozen qubit-sharing conflict relation. These facts are the only bridge from schedules to the algebra below.

## 3. A from-scratch `QSAT_2` grouped-syndrome encoding

### 3.1 Source and construction

Use the canonical language

\[
 \mathrm{QSAT}_{2,3DNF}=\{\Phi:\exists x_1\ldots x_p\ \forall y_1\ldots y_q\ \Phi(x,y)\},
\]

where `Phi` is a 3DNF. Put `psi=not Phi`, a CNF with clauses `C_1,...,C_m` of size at most three. Repeated equal literals are collapsed and tautological CNF clauses are deleted. Quantified variables with no remaining occurrence are deleted as well; deleting either an unused existential or an unused universal variable preserves the QBF. Empty-clause and no-clause constants are handled by the explicit promised instances in §3.4. Thus the nonconstant construction may assume that every clause is nonempty, no clause repeats a variable, and every retained variable occurs. Let

\[
 K=p+q+m.
\]

Create a vector space `U` with:

- a marker `g_v` for every existential or universal variable `v`;
- a marker `g_j` for every clause;
- an occurrence coordinate `e_{j,r}` for every literal position `r` of clause `C_j`.

For a variable `v` and bit `b`, define

\[
 V_{v,b}=g_v+b\sum_{(j,r):v_{j,r}=v}e_{j,r}. \tag{3.1}
\]

For every locally satisfying assignment `a` to the variables occurring in `C_j`, define

\[
 A_{j,a}=g_j+\sum_{r}a(v_{j,r})e_{j,r}. \tag{3.2}
\]

Finally set

\[
 \tau=\sum_v g_v+\sum_{j=1}^m g_j. \tag{3.3}
\]

For an existential assignment `alpha`, the available catalogue `P_alpha` contains only `V_{x_i,alpha_i}` for each existential group, both `V_{y_i,0},V_{y_i,1}` for each universal group, and every clause column `A_{j,a}`.

The construction has `K+L` syndrome coordinates where `L<=3m`, and at most

\[
 2(p+q)+\sum_j(2^{|C_j|}-1)\le 2(p+q)+7m
\]

columns. A generator or parity-check description is therefore explicitly computable in polynomial time.

### 3.2 Grouped Representation Theorem — PROVED-IN-ARTIFACT

**Theorem 3.1.** For fixed `alpha`, the following are equivalent:

1. there exists `beta` with `psi(alpha,beta)=1`;
2. some subset of at most `K` columns of `P_alpha` sums to `tau`;
3. exactly `K` columns of `P_alpha`, one from every group, sum to `tau`.

**Proof.** Every column has exactly one group marker. In a sum equal to `tau`, every one of the `K` group-marker coordinates has odd parity. Hence at least one column was selected from every group. If at most `K` columns were selected, exactly one was selected from every group. This proves `(2)=>(3)`.

Write the selected variable column in group `v` as `V_{v,b_v}` and the selected clause column in group `j` as `A_{j,a_j}`. At occurrence `(j,r)`, equations (3.1)–(3.2) make the total occurrence coordinate

\[
 b_{v_{j,r}}+a_j(v_{j,r}).
\]

The target has zero occurrence coordinates, so these two bits agree at every occurrence. Thus all local assignments are restrictions of the single global assignment `(alpha,beta)`. Each `a_j` was included only if it satisfies `C_j`, so the global assignment satisfies every clause of `psi`. This proves `(3)=>(1)`.

Conversely, a satisfying global assignment selects its value column in every variable group and its restriction in every clause group. Every group marker appears once and every occurrence coordinate appears twice, so the sum is `tau`. This proves `(1)=>(3)`, and `(3)=>(2)` is immediate. ∎

### 3.3 Flagged abstraction and the exact quantifiers — PROVED-IN-ARTIFACT

Adjoin one flag coordinate `ell`. Give every catalogue column flag zero and add one anchor

\[
 h=(\tau,1). \tag{3.4}
\]

A subset containing the unique anchor has total label `(0,1)` exactly when its other columns sum to `tau`. Let

\[
 d_0=K+2. \tag{3.5}
\]

Theorem 3.1 gives, for every fixed schedule assignment `alpha`,

\[
 \exists F,\ |F|<d_0,\ \sum_{c\in F}c=(0,1)
 \iff \exists\beta\ \psi(\alpha,\beta)
 \iff \exists\beta\ \neg\Phi(\alpha,\beta). \tag{3.6}
\]

Taking complements and the outer schedule choice,

\[
 \exists\alpha\ \forall F, |F|<d_0:\sum_{c\in F}c\ne(0,1)
 \iff
 \exists\alpha\ \forall\beta\ \Phi(\alpha,\beta). \tag{3.7}
\]

This is the required existential-schedule/universal-fault map at the abstract label level. The universal content is not seed depth. It is the absence of a short flagged relation after the schedule fixes the existential value columns.

### 3.4 Total handling of syntactic constants — PROVED-IN-ARTIFACT

The normalization just stated can expose either an empty clause in `psi` or no clauses. These cases do not require RIN and are mapped to fixed promised instances.

If `psi` has an empty clause, then `Phi=not psi` is identically true and the QBF is YES. Emit the `d=2` safe grid of §7.2; its static and effective distances are both exactly two.

If `psi` has no clauses, then `Phi` is identically false and the QBF is NO. Emit the following forced-order instance with requested `d=2`. On qubits `0,1,2,3`, in syndrome-coordinate order `(p,r,ell)`, take physical label columns

\[
 (1,0,0),(1,0,1),(1,1,0),(1,1,1).
\]

Equivalently,

\[
 H_Z=\begin{pmatrix}1&1&1&1\\0&0&1&1\end{pmatrix},\qquad
 H_X=\begin{pmatrix}1&1&1&1\end{pmatrix}.
\]

The pair is CSS. Direct enumeration of the two parity constraints gives `d_X=2`; the even-parity `Z` normalizer modulo `row H_Z` gives `d_Z=2`. Give the `X` row the sole allowed order `(2,3,0,1)`, and give the two `Z` rows the sole orders `(0,1,2,3)` and `(2,3)`. Use no `T` and the frozen derived conflict relation, so a serial execution is legal. The middle `X` suffix is the weight-two logical on qubits `{0,1}`, so one fault is bad and every schedule has `d_eff^X=1<2`. Thus this is a promised NO instance. This makes the source preprocessing total. The only conditional part of the eventual reduction remains RIN on nonconstant normalized inputs.

## 4. The affine-plane local hook gadget

For payloads `a,b` and a fresh private syndrome coordinate `p`, use four physical columns

\[
 B_0=p,\quad B_1=p+a,\quad B_2=p+b,\quad B_3=p+a+b. \tag{4.1}
\]

Their sum is zero, so `c=(1,1,1,1)` is an `X` stabilizer row. In order

\[
 O_a=(2,3,0,1),
\]

the length-two suffix is qubits `{0,1}` and has label `a`. In order

\[
 O_b=(1,3,0,2),
\]

the length-two suffix is `{0,2}` and has label `b`. A length-one suffix is a physical singleton. A length-three suffix differs from the complementary singleton by the full stabilizer and therefore has the same label. Thus the only nonsingleton quotient class introduced by `O_a` is `a`, and the only one introduced by `O_b` is `b`.

For each existential variable, one selectable plane uses `a=V_{x,0}`, `b=V_{x,1}`. For a fixed available column `a`, use `b=r` with a fresh private coordinate `r` and the singleton order `O_a`. Universal value columns, clause-option columns, and the anchor receive fixed planes. Local orders are explicit; with no `T`, serial execution is legal. This is a complete local schedule gadget.

A pure flagged physical data vector must have even parity in each plane's private `p` coordinate. In a fixed plane, its fresh `r` coordinate also forces the selected physical columns into two pairs; one nonzero payload coefficient costs at least two physical qubits. In a selector plane, any nonzero coefficient pattern also costs at least two. A pure flag uses the anchor coefficient and has odd marker parity in every group, so it uses at least `K+1` abstract payload coefficients. Therefore, when the full plane-label kernel is stabilized,

\[
 d_X\ge 2(K+1)\ge K+2=d_0. \tag{4.2}
\]

This static bound is truth-independent.

## 5. Why local planes alone do not compile the quotient

### 5.1 The homogeneous-kernel mechanism — PROVED-IN-ARTIFACT

If `S_X` contains only the disjoint full-plane rows, then two physical errors are equivalent only plane by plane. Any nonempty abstract homogeneous relation among available payload columns becomes an unintended logical class, even though it should be a stabilizer in the flagged quotient.

Differences of two satisfying grouped representations are exactly such anchor-free homogeneous relations. This is not a rare degeneracy; it is forced whenever the same flagged logical has two abstract witnesses.

### 5.2 Exact four-fault counterexample — REFUTED construction

Take

\[
 \psi=x\wedge(y\vee z\vee w),\qquad
 \Phi=\neg x\vee(\neg y\wedge\neg z\wedge\neg w).
\]

The QBF is true at `x=0`. Here `K=6`, `d_0=8`, there are 16 abstract payload columns and 10 syndrome coordinates. The abstract model has no bad relation for `x=0`; for `x=1` it has seven universal witnesses and minimum flagged weight seven.

In the naive plane quotient, both schedules have the anchor-free four-hook relation

```text
V_(y,0) + V_(y,1) + A_(clause 1,(0,0,1)) + A_(clause 1,(0,1,1)) = 0.
```

It is declared logical by the undersized `S_X`, so both schedules have `d_eff^X<=4<8`; the true QBF is mapped to NO. The same relation represented by physical singletons has weight eight, exactly the requested threshold, so this is specifically a quotient/stabilizer failure and not merely a static-distance failure.

## 6. Full-kernel algebra and the anchor dual obstruction

### 6.1 Polynomial CSS quotient compiler — PROVED-IN-ARTIFACT

Let `B` be the matrix whose physical columns are the full labels from all affine planes, including nonflag syndrome coordinates and flag `ell`. Let `S` be `B` with the flag row deleted. Define

\[
 H_Z=S,\qquad \operatorname{row}H_X=\ker B. \tag{6.1}
\]

A basis for `ker B` is produced by Gaussian elimination in polynomial time. Since every row of `ker B` is orthogonal to every row of `B`, `H_XH_Z^T=0`. Moreover

\[
 k=n-\operatorname{rank}H_X-\operatorname{rank}H_Z
   =\operatorname{rank}B-\operatorname{rank}S\in\{0,1\}. \tag{6.2}
\]

When the flag row is independent, `k=1`, and an `X` error `z` is the nontrivial logical exactly when

\[
 Bz=(0,1). \tag{6.3}
\]

The nontrivial `Z` logical coset is the flag row modulo `row S`, so

\[
 d_Z=\operatorname{dist}(\ell,\operatorname{row}S). \tag{6.4}
\]

This proves the quotient dictionary at exactly the scope used here; no legacy Theorem D is invoked.

### 6.2 Single-anchor opposite-sector no-go — PROVED-IN-ARTIFACT

Only the anchor payload has flag one. In its affine plane, exactly two of the four physical columns have flag one. Therefore the physical flag row has weight two. If the flag is independent, equation (6.4) gives

\[
 d_Z\le 2. \tag{6.5}
\]

For every nontrivial instance `d_0=K+2>2`, the output is off-promise. In the audited `K=6` example, the compiler has 16 planes, `n=64`, label rank 42, `rank H_Z=41`, `rank H_X=22`, `k=1`, and a weight-two `Z` logical. The intended bad hook relation costs seven faults; the same physical `X` vector has weight 14. The off-by-one and physical-weight accounting therefore do not repair the `Z` sector.

### 6.3 All-or-none replicated anchors do not help — PROVED-IN-ARTIFACT, scoped

Suppose guard rows force the anchor coefficient vector to lie in `ker G=span{c}` and a flag vector `f` satisfies `f dot c=1`. Then `row G=c^perp`. Pick any `i` in `supp(c)`. Since `(f+e_i) dot c=0`, one has `f+e_i in row G`; hence

\[
 \operatorname{dist}(f,\operatorname{row}G)=1. \tag{6.6}
\]

The affine-plane physical realization doubles this to `d_Z<=2`. Replication raises the intended hook cost from `K+1` to `K+wt(c)` but leaves the dual obstruction unchanged. This refutes the natural all-or-none replicated/distributed-anchor repair. It is not a no-go for arbitrary encoded flag blocks.

## 7. A complete input-`d` opposite-sector and promise repair

### 7.1 Cluster expansion `R_R` — PROVED-IN-ARTIFACT

Start with any CSS code `(H_X,H_Z)` on `n` qubits. Replace qubit `q` by copies `(q,0),...,(q,R-1)`. Define:

1. for every `q` and `j<R-1`, an `X` equality row `e_(q,j)+e_(q,j+1)`;
2. for every old `X` row, its lift on layer zero;
3. for every old `Z` row `z`, the repeated row `z tensor 1_R`.

Equality rows commute with repeated `Z` rows because each touched old coordinate occurs twice. Lifted `X` rows commute because the old pair was CSS. Rank counting gives

\[
 \operatorname{rank}H_X^{(R)}=n(R-1)+\operatorname{rank}H_X,qquad
 \operatorname{rank}H_Z^{(R)}=\operatorname{rank}H_Z,
\]

so `k` is preserved.

For an `X` error, let `pi` take the parity in each copy block. Equality stabilizers move every error to layer zero without changing `pi`; the lifted old `X` stabilizers act exactly as before. Thus the `X` logical quotient and minimum weight are unchanged:

\[
 d_X^{(R)}=d_X. \tag{7.1}
\]

A `Z` normalizer must be constant across every copy block, by the equality checks. It is therefore `z tensor 1_R` for an old `Z` normalizer `z`, and repeated old `Z` stabilizers identify exactly the old stabilizer cosets. Hence

\[
 d_Z^{(R)}=R d_Z. \tag{7.2}
\]

Give each lifted old `X` row its old local order on layer zero; equality checks have weight two. Every equality suffix is a singleton, and every singleton in another layer is equality-equivalent to its layer-zero copy. Consequently

\[
 d_{\rm eff}^{X,(R)}=d_{\rm eff}^X. \tag{7.3}
\]

For every repeated `Z` row, use a layer-major order: traverse all support qubits in layer zero, then layer one, and so on. Let

\[
 Q=\mathbb F_2^n/\operatorname{row}H_Z.
\]

A proper suffix consists of a partial old row in one current layer and full old rows in later layers. Full old rows are zero in `Q`. Thus one `Z` fault has a possibly nonzero `Q` class in at most one layer. A repeated nontrivial `Z` logical has the same nonzero class `[z]` in all `R` layers. A sum of fewer than `R` fault columns cannot produce it. Therefore

\[
 d_{\rm eff}^{Z,(R)}\ge R. \tag{7.4}
\]

This proof works for arbitrary old row weights and does not rely on the private-sentinel `d=3` theorem.

### 7.2 Exact safe promise block — PROVED-IN-ARTIFACT

On `d` base qubits, take no `X` rows and take adjacent-pair `Z` rows `e_i+e_(i+1)`. This base code has `k=1`, `d_X=d`, and `d_Z=1`. Apply `R_d`. The resulting `d x d` grid has:

- weight-two `X` equality checks within each old-qubit row;
- `Z` checks equal to two adjacent full rows;
- static distances `d_X=d_Z=d`;
- `d_eff^X=d`, because its `X` catalogue is only singleton classes;
- `d_eff^Z>=d` by (7.4), and `d_eff^Z<=d` by `d` singleton faults forming a minimum repeated `Z` logical.

Hence both static and effective distance are exactly `d`. The layer-major order is the alternating two-row order tested in §10.

### 7.3 Promise composition — PROVED-IN-ARTIFACT, conditional only on the base `X` compiler

Apply `R_d` with `d=K+2` to the base flagged-plane code. Equation (4.2) gives base `d_X>=d`; (7.1) preserves it. Every nonempty base `Z` logical has distance at least one, so (7.2) gives expanded `d_Z>=d`, and (7.4) gives expanded `d_eff^Z>=d`. Equation (7.3) preserves the intended `X` hook problem exactly.

Direct-sum the expanded code with the safe grid block. Static and effective sector distances of a direct sum are the minima of the summands' distances. Therefore the total static distance is **exactly** `d`, both `Z` sectors are safe below `d`, the grid `X` sector is safe below `d`, and the only possible sub-`d` mechanism is the flagged compiler's `X` mechanism.

This closes the static-distance promise, the opposite sector, exact equality `d_eff=d`, polynomial size (`O(d)` repetition blowup and `d^2` grid qubits), schedule legality, and the absence of convention drift. It does **not** close the remaining base `X` order lemma.

## 8. The sole remaining compiler gate

### 8.1 Why complement checks are mandatory

Local plane rows span only a subspace of `ker B`. If the remainder is not stabilized, homogeneous payload relations become extra logicals (§5). Since a basis of `ker B` is polynomial, the algebraic problem is not generation but measurement: every added `X` row contributes every proper suffix to `Gamma_X`.

Checks of weight at most three are hook-inert: every proper suffix is a singleton or differs from a singleton by the full stabilizer. If all nonlocal selector content were replaced by weight-`<=3` checks, then `d_eff^X=d_X` and no sub-static-distance witness could encode the universal assignment. Weight-four selector planes or another genuinely nontrivial hook interface are necessary.

### 8.2 Canonical Gaussian/increasing order fails — exact counterexample

Let

\[
 \psi=(x=0\vee y=0)\wedge(x=0\vee y=1).
\]

For schedule `x=1`, the two clauses require simultaneously `y=0` and `y=1`, so no `y` satisfies `psi`; equivalently `Phi=not psi` is true for every `y`. This is the safe existential branch. Here `K=4`, `d=6`. The compiler has 10 planes, 40 physical qubits, 28 label rows, 10 local plane generators, and two complement generators of weights 12 and 14.

Choose the deterministic Gaussian complement basis and increasing-support local order. Exhaustive meet-in-the-middle search finds a five-fault pure flag:

| fault class | full label in hex |
|---|---:|
| clause 0 option `(x,y)=(0,0)` | `0x004` |
| clause 1 option `(x,y)=(0,0)` | `0x008` |
| selected existential hook `x=1` | `0x051` |
| suffix 10 of the weight-14 complement row | `0x052` |
| anchor hook | `0x10f` |

Their XOR is `0x100`, the pure flag bit, and `5<d=6`. The construction therefore maps a true QBF branch to unsafe. This counterexample is scoped to that basis/order rule; it is not an all-order impossibility theorem. Indeed 480 of 600 deterministic-seed random basis/order trials on this same instance had no bad subset through weight five.

### 8.3 Two generic repairs also fail in exact scope

**Triangle splitting.** Let zero-flag payload labels be

\[
 b_1=e_1,\ b_2=e_2,\ b_3=e_3,\ b_4=e_1+e_2+e_3,
\]

so `b_1+b_2+b_3+b_4=0`. Let the flagged anchor have syndrome `e_1+e_2`. Before splitting, a pure flag needs the anchor plus either `{b_1,b_2}` or `{b_3,b_4}`, weight three. Splitting the weight-four relation into triangles forces an auxiliary column `a=b_1+b_2`; then anchor plus `a` has weight two. CSS orthogonality forces this prefix label in a three-check, so a free independent private marker cannot be attached without adding another column/check. Naive weight-three subdivision is not distance preserving.

**Circuit shield.** Replace a complement row `r` by `r+m`, where `m` is a length-`L` private-marker circuit whose label columns have rank `L-1`. Adding `L` qubits and only this replacement increases `k` by one; the new logical is represented both by `m` and by the old `r`, so a short `r` violates the promise. Adding the marker-only `X` stabilizer `m` restores the dimension, but matched suffixes of `r+m` and `m` cancel the marker circuit in two faults and recover the unshielded suffix. This refutes the direct private-circuit shield.

The reviewed private sentinel cannot help: it preserves, rather than raises, the base `d_Z`, and its effective theorem stops at one/two faults for `d=3`. Direct sum with a good block also cannot erase a weight-two logical in another summand; §7's cluster expansion is why the opposite-sector repair succeeds.

### 8.4 Frozen systematic group-block compiler and the `K+1` lower bound — PROVED-IN-ARTIFACT

This subsection freezes the basis and order algorithm, rather than merely asserting that a favorable basis exists.

For selector plane `i`, put

\[
 \delta_i=V_{x_i,0}+V_{x_i,1}
\]

and represent it physically by the pair `{q_0,q_3}`. Both endpoints have zero group-marker projection. For every fixed nonanchor payload plane `j` with payload `a_j`, represent `a_j` by `{q_0,q_1}` and orient this pair as `u_j=q_0`, of marker zero, and `v_j=q_1`, of marker `g_{G(j)}`. The anchor is retained as the last bookkeeping coordinate; its unique flag bit forces its coefficient to zero in every homogeneous relation, and it is excluded from the pivot set.

Let `D` be the binary matrix with selector-difference columns `delta_i`, followed by all fixed payload columns `a_j` in variable-group, clause-group, and lexicographic option order, with the anchor last. Its relation space is

\[
 R=\ker D. \tag{8.1}
\]

**Lemma 8.1 (full-kernel quotient).** The local plane rows together with physical pair lifts of a basis of `R` span exactly `ker B`.

**Proof.** A plane-private `p` coordinate forces every vector in `ker B` to have even weight in that plane. Modulo the full four-qubit plane row, a fixed plane has two possible pair directions. Its unique `r` coordinate kills the `{q_0,q_2}` direction, leaving only `{q_0,q_1}`, whose label is `a_j`. In a selector plane the only group marker for `x_i` occurs in its two payload directions, so zero group syndrome forces equal coefficients on them, leaving `{q_0,q_3}` with label `delta_i`. The unique flag coordinate kills the anchor coefficient. What remains is exactly a coefficient vector in `ker D`. Conversely, every relation in `ker D` lifts to a physical zero-label row, and the local plane rows account for the quotient choices. ∎

Projection from `R` to the fixed-payload coordinates is injective. Indeed, a relation with every fixed coefficient zero is a sum of selector differences. The occurrence support of `delta_i` is the nonempty set of occurrences of `x_i`; these supports are pairwise disjoint after the normalization of §3.1. Hence every selector coefficient is zero.

Compute any basis of `R`, then perform deterministic RREF using only the fixed-payload coordinates, from left to right in the order above. Injectivity guarantees one pivot for every basis row. Record those pivots. The resulting rows have the form

\[
 r_i=e_{p_i}+\sum_{j\in S_i}e_j, \tag{8.2}
\]

where each `p_i` is a fixed plane and is absent from every other basis row. This is a polynomial-time, explicitly computable basis of the full complement inside `ker B` by Lemma 8.1.

For lifted row `r_i`, use this deterministic **group-block bookend order**:

1. put `u_(p_i)` first;
2. append selector-pair endpoints in quantifier order and all `u_j` for nonpivot fixed pairs in relation-coordinate order;
3. append the nonpivot `v_j` endpoints sorted first by their displayed group tag (the code's tuple order), then by the displayed payload name, except that the pivot group is last;
4. put `v_(p_i)` last.

Every physical support coordinate occurs exactly once.

**Lemma 8.2 (suffix-marker bound).** Every proper suffix of a complement check in this order has group-marker Hamming weight at most one.

**Proof.** A relation has even payload parity in every group. Its pivot contributes one in the pivot group, so its nonpivot fixed payloads have odd parity in that group and even parity in every other group; selector-difference pairs contribute zero marker. A suffix beginning in the zero-marker zone includes every later marker endpoint, whose total is zero. A suffix beginning inside an ordinary group block has a possibly odd partial block in that group, followed by complete even blocks and then the complete pivot block plus pivot endpoint, which is even. A suffix beginning inside the pivot block or at the final pivot endpoint has support in that one group only. ∎

The same weight-at-most-one property holds for all nonanchor physical singletons and local-plane suffix labels. In the anchor plane, every flag-one catalogue column has group projection `tau`, and no complement check touches either anchor-private coordinate.

**Theorem 8.3 (`K+1` lower bound).** Every pure-flag fault mechanism under the frozen group-block bookend orders has at least `K+1` faults.

**Proof.** Flag parity one forces an odd number of flag-one anchor-plane fault columns. Their total group-marker projection is `tau`. The final pure flag has zero group-marker syndrome, so all remaining faults together project to `tau`, of Hamming weight `K`. By Lemma 8.2 and the local catalogue, each remaining fault contributes marker weight at most one. At least `K` such faults and at least one flag-one anchor fault are necessary. ∎

At equality there is exactly one flag-one anchor fault and exactly `K` other faults. Every other fault has a unit marker, one for each distinct group. It cannot include a marker-zero anchor-private singleton. No other catalogue column carries an anchor-private coordinate, so the sole flag-one fault must be the anchor hook `h`. This is the strongest universal compiler theorem obtained in this round.

### 8.5 Relation/Interval Normal-Form Lemma (RIN) — OPEN RESIDUAL

Fix a normalized formula, an existential schedule `alpha`, the planes, the deterministic fixed-coordinate RREF basis (8.2), and the bookend orders above. Let `C_alpha` be the **indexed** catalogue of nonanchor `Gamma_X` fault locations whose labels have group-marker weight one. Equal labels at distinct fault locations remain distinct catalogue entries.

For group `G`, let `C_G` be its entries and write

\[
 \rho(c)=\operatorname{label}(c)+g_G
\]

for the residual occurrence/private-coordinate vector. The exact equality case is the finite Boolean system

\[
 z_{G,c}\in\{0,1\},\qquad
 \sum_{c\in C_G}z_{G,c}=1\quad(\text{over the integers}),\qquad
 \bigoplus_{G,c:z_{G,c}=1}\rho(c)=0. \tag{8.3}
\]

Thus (8.3) is neither a depth predicate nor a covering-radius transfer: it is exactly one chosen indexed fault per group, with every occurrence and plane-private coordinate cancelled.

> **RIN.** Every solution of (8.3) can be replaced, without changing its aggregate label or its `K`-fault budget, by `K` intended payload hooks, one per group and respecting the scheduled existential values. Equivalently, a solution exists only if some global assignment `(alpha,beta)` satisfies `psi`.

RIN is sufficient: Theorem 8.3 reduces every sub-`d` bad mechanism to this equality system; RIN and Theorem 3.1 then identify it with a falsifying universal assignment. It is necessary for this compiler: on a source-safe schedule, a solution of (8.3), together with the anchor hook, is exactly an unintended `K+1<d` pure-flag mechanism.

A useful interval form pairs suffix columns from one complement row. The XOR of two suffixes is an interval in that row's ordered support. An interval crossing the two halves contains full payload pairs in consecutive group blocks plus at most two boundary fragments. Within one row, locally cancelled boundary fragments let relation (8.2) replace the full-pair block by the pivot and its complement without increasing the catalogue budget. The unresolved case is cancellation of boundary private markers between intervals from different systematic rows that share nonpivot planes. RIN asserts that such cross-row cancellations also admit the intended one-option-per-group normal form.

No counterexample to RIN was found in the frozen exact census of §10. No proof was found. This is the first unproved implication, the sole residual, and the reason the reduction is not complete.

### 8.6 The `k>1`/high-girth fallback boundary

Keeping only local low-weight kernel generators leaves homogeneous relations as extra `X` logical homology. The `R_R` expansion raises only `Z` distance; it preserves those `X` distances exactly. A bounded-weight-`<=3` completion is hook-inert and cannot create the intended sub-`d` mechanism. Subdivision can make leftover cycles long with polynomial size, but then a one-fault interface must still create the intended long payload representative; a bare coordinate-once high-weight check reintroduces the same suffix/interval problem. No total quotient- and distance-preserving factor-complex lift was constructed. This fallback is therefore not a second residual; it reduces again to a guarded interval normal form of the same kind as RIN.

## 9. Conditional end-to-end theorem, with every condition visible

If RIN holds for the construction in §8.5, then the following polynomial many-one reduction is complete:

1. normalize `Phi`; map syntactic constants to §3.4 and every nonconstant input to the grouped matrix (§3);
2. build selector/fixed affine planes and the full-kernel systematic basis (§§4, 8.4);
3. request `d=K+2`;
4. apply `R_d` and add the exact-distance-`d` grid block (§7);
5. emit explicit local order domains: the two affine orders for each existential selector plane, the single intended affine order elsewhere, group-block bookend orders for complement rows, layer-zero lifts for `X`, and layer-major repeated `Z` orders;
6. use no optional `T` and only the derived qubit-sharing conflict relation.

Let `s=p+q+m`. There are at most `p+2q+7m+1=O(s)` planes and `n_0=O(s)` base qubits. The label dimension, number of full-kernel rows, and every base order length are `O(s)`. Expansion by `d=K+2=O(s)` gives `O(s^2)` qubits and checks; even a dense explicit bit-matrix/order-list encoding is `O(s^3)`. The grid adds `O(s^2)` qubits. Every matrix, rank, order and the requested integer is therefore computable and writable in polynomial time. Every output is a CSS instance of static distance exactly `d`, regardless of truth. The schedule selects `alpha`; equations (3.6)–(3.7), Theorem 8.3 and RIN give both truth directions. The grid and `R_d` theorems give the opposite sector and exact promise.

Because RIN is open, this paragraph is **CONDITIONAL** and cannot be cited as a hardness theorem.

## 10. Exact falsification harnesses and results

All programs used Python's integer bitsets and exact `F_2` arithmetic. No random result is used as proof. The important outputs were:

| harness | scope | exact result | real time / max RSS |
|---|---|---|---|
| `abstract_census.py` | all 702 one-existential/two-universal CNFs with one or two clauses from 26 clause templates; 1,404 schedules | abstract and flagged mismatches `0`; naive shortcuts in 1,388 schedules; 136 false-NO schedules | 0.91 s / 9,551,872 B |
| `plane_gate.py` | `psi=x and (y or z or w)` | exact four-hook homogeneous shortcut; abstract truth directions pass | 0.02 s / 10,158,080 B |
| `compiler_audit.py` | 64-qubit full-kernel example | `rankB=42`, `rankHZ=41`, `rankHX=22`, `k=1`, flag-row weight 2 | 0.02 s / 10,829,824 B |
| `compiler_audit2.py` | same, meet in middle through weight 7 | safe `x=0`: none; unsafe `x=1`: minimum 7 | 2.22 s / 749,453,312 B |
| `grid_block_audit.py` | `d=2,3,4`, three `Z` orders | blocked order gives distance 1; alternating/layer-major gives exactly `d` | 0.07 s / 12,304,384 B |
| `constant_instance_audit.py` | four-qubit fixed NO instance of §3.4 | CSS; `d_X=d_Z=2`; forced order has a one-fault bad suffix | 0.01 s / 8,732,672 B |
| `kernel_shortcut_witness.py` | Gaussian/increasing compiler search | first exact false shortcut at `K=4,d=6,n=40`, weight 5, labels printed in §8.2 | 5.74 s / 743,882,752 B |
| `kernel_order_random.py` | 600 seeded basis/order trials on counterexample | 480 with no bad set through 5; 114 min 5; 6 min 4 | 7.89 s / 743,227,392 B |
| `rin_xor_csp_search.py`, final `v2,m2` | all 56 normalized one-existential/one-universal two-clause incidences; 112 schedules | 36 source-safe; zero RIN failures; peak 1,808 states; pivot/cap failures 0 | 0.03 s / 13,811,712 B |
| same, final `v2,m3` | all 496 normalized incidences; 992 schedules | 552 source-safe; zero RIN failures; peak 19,536 states; pivot/cap failures 0 | 0.48 s / 18,710,528 B |
| same, final `v2,m4` | all 4,064 normalized incidences; 8,128 schedules | 5,796 source-safe; zero RIN failures; peak 208,256 states; pivot/cap failures 0 | 34.74 s / 80,396,288 B |
| same, final `v3,m2` | all 496 normalized one-existential/two-universal incidences; 992 schedules | 48 source-safe; zero RIN failures; peak 7,596 states; pivot/cap failures 0 | 0.09 s / 15,532,032 B |
| pre-freeze `v3,m3` exploratory run | 16,064 normalized incidences; 32,128 schedules, using an arbitrary unique fixed pivot rather than the recorded RREF pivot | 5,496 source-safe; zero shortcuts; peak 2,110,047 states; **not** a census of the final frozen order | 218.80 s / 630,472,704 B |
| `kernel_pivot_random_m4.py` | 1,000 seeded four-clause formulas / 2,000 schedules, earlier pivot-private order | 666 safe schedules; zero shortcut of weight at most 5; related evidence, not RIN evidence for the frozen order | 118.34 s / 892,452,864 B |

Negative controls mattered. The blocked grid order puts one full base row in a proper suffix and correctly reports `d_eff^Z=1`. The naive-plane census reports many false negatives. The Gaussian/increasing compiler reports the exact five-fault counterexample. The pivot census was not treated as proof.

### 10.1 Exact Boolean/XOR formulation of the equality search

The outer loop enumerated normalized clause-incidence tensors and all existential schedules. A schedule was sent to the inner solver only after exhaustive universal-assignment enumeration certified it source-safe. The compiler was then rebuilt from the physical labels, `ker D` was RREF-reduced on the fixed coordinates, every order was checked coordinate-once, and every suffix label was recomputed.

The inner solver used exactly the Boolean variables and constraints (8.3). It processed one group at a time and stored one witness per reachable residual XOR syndrome. This state merge is lossless: all future constraints see a partial choice only through its XOR syndrome. Equal residual labels within one group were collapsed only for the existence query, because exactly one entry must be chosen from that group; the retained entry's full provenance identifies an indexed fault location. A zero terminal state is therefore an exact RIN counterexample, not a heuristic collision. `peak_states` in the table is the largest exact dynamic-programming layer.

The final frozen search covers one existential and one universal variable through four nonempty clauses of width at most two, and one existential plus two universal variables through two clauses of width at most three. It does not cover two existential variables, four or more total variables, three clauses in the three-variable frozen compiler, or any unbounded family. The completed exploratory `v3,m3` run used a different admissible pivot rule and is reported only as process evidence. Absence of a bounded counterexample is NUMERICAL and does not license RIN.

### 10.2 Process failures, superseded runs, and killed searches

The complete XOR-CSP process evolution is retained because basis/order revisions change the statement being tested:

| stage / scope | exit | result | real time / max RSS |
|---|---:|---|---|
| initial portable-Python check | 1 | `int.bit_count` unavailable | 0.03 s / 13,287,424 B |
| initial normalization check | 3 | fixed-pivot failure on an unused `x`; exposed missing preprocessing | 0.02 s / 13,352,960 B |
| A: physical-kernel/any-unique pivot, `v2,m2` | 0 | zero counterexamples; peak 2,055 states | 0.03 s / 13,631,488 B |
| A: same, `v2,m3` | 0 | zero; peak 22,229 | 0.49 s / 20,086,784 B |
| A: same, `v3,m2` | 0 | zero; peak 14,103 | 0.14 s / 17,055,744 B |
| A: same, `v2,m4` | 0 | zero; peak 237,003 | 35.62 s / 86,687,744 B |
| A: same, `v3,m3` | 0 | zero; peak 2,110,047 | 218.80 s / 630,472,704 B |
| B: quotient RREF/any-unique pivot, `v2,m2` | 0 | zero; peak 1,873 | 0.03 s / 13,713,408 B |
| B: same, `v2,m3` | 0 | zero; peak 20,263 | 0.50 s / 18,448,384 B |
| B: same, `v3,m2` | 0 | zero; peak 7,596 | 0.10 s / 15,548,416 B |
| B: same, `v2,m4` | 0 | zero; peak 216,049 | 36.78 s / 81,395,712 B |
| C: frozen recorded RREF pivot, `v2,m2` | 0 | zero; peak 1,808 | 0.03 s / 13,811,712 B |
| C: same, `v2,m3` | 0 | zero; peak 19,536 | 0.48 s / 18,710,528 B |
| C: same, `v2,m4` | 0 | zero; peak 208,256 | 34.74 s / 80,396,288 B |
| C: same, `v3,m2` | 0 | zero; peak 7,596 | 0.09 s / 15,532,032 B |

The short stage-A `v2,m3` and `v3,m2` processes were launched together in one tool batch; no subagent or second proposer was used. Every later dependency and every final frozen run was sequential. The fixed-constant audit was run three times after comment/blank-line-only synchronization of its embedded listing; all exited 0 in 0.01 s, with final max RSS 8,732,672 B and identical output hash.

- The first cleanup command included an `rm -rf` token and was rejected by the execution safeguard before it ran. No repository byte was written.
- The first `abstract_census.py` run exited 1 after an intentionally surfaced assertion mismatch. The bug was in the test oracle: it compared existence of an arbitrary representation instead of existence of a representation of weight `<=K`. Some false formulas have representations of weight `K+2`; the flagged threshold test was already correct. The corrected run had zero mismatches.
- The first `plane_gate.py` run exited 1 because the host Python 3.9 lacks `int.bit_count`; it was replaced by `bin(x).count('1')`.
- The first grid sweep attempted `d<=6`, grew to about 912 MB RSS after roughly 44 seconds, and was explicitly killed; its redirected output/time files were empty. The bounded `d<=4` rerun completed.
- The first broad kernel shortcut sweep grew to about 602 MB RSS after roughly 34 seconds and was explicitly killed; its output/time files were empty. The exact search was reduced and then replaced by meet-in-the-middle enumeration.
- The first exact group-block harness edit exited 1 with an indentation error caused by a stale duplicated block; the stale lines were removed and the exact coordinate-once harness reran successfully.
- One earlier pivot-order harness accidentally duplicated the pivot endpoints because Python object identity was used instead of tuple equality. That order violated the coordinate-once convention and was discarded. The corrected order had distinct coordinates and was rerun.
- One final hash-check shell used the zsh special variable name `path`, overwriting the command search path inside that disposable shell and producing `command not found`; it wrote no repository file. The rerun used `relfile` and confirmed every input unchanged.
- The first `rin_xor_csp_search.py` run exited 1 in 0.03 s / 13,287,424 B because it initially reused `int.bit_count`; the portable population-count routine fixed it.
- The next `rin_xor_csp_search.py` run exited 3 in 0.02 s / 13,352,960 B on a formula in which existential `x` had no occurrence. This exposed a missing implementation of the normalization assumed by the fixed-projection proof. The search now deletes unused quantified variables before compilation; all final runs have pivot failure count zero.
- An attempted scratch-only patch of the compiler block failed context verification and changed no byte. It was immediately reapplied against the exact displayed context.
- The first `update_artifact.py` execution exited 1 before its sole write because the expected §11.6 heading string was too specific. The in-memory edit was discarded automatically, the exact heading was substituted, and the rerun exited 0; both executions touched scratch only.
- The XOR-CSP search was run in three explicitly superseded stages: physical-kernel basis plus any unique fixed pivot (`v2,m2/m3/m4`, `v3,m2/m3`), quotient-relation RREF plus any unique fixed pivot (`v2,m2/m3/m4`, `v3,m2`), and finally quotient-relation RREF plus its recorded pivot. Only the last stage's `v2,m2/m3/m4` and `v3,m2` rows are evidence for the frozen algorithm. Every exploratory run exited 0; the largest was the completed pre-freeze `v3,m3` run in §10.

### 10.3 Commands

Representative commands, all run from the repository root, were:

```text
ROUND82_TMP=/tmp/circdist-cplx-sigma2-r5-round82-20260830
/usr/bin/time -lp python3 "$ROUND82_TMP/abstract_census.py"
/usr/bin/time -lp python3 "$ROUND82_TMP/plane_gate.py"
/usr/bin/time -lp python3 "$ROUND82_TMP/compiler_audit.py"
/usr/bin/time -lp python3 "$ROUND82_TMP/grid_block_audit.py"
/usr/bin/time -lp python3 "$ROUND82_TMP/constant_instance_audit.py"
/usr/bin/time -lp python3 "$ROUND82_TMP/kernel_shortcut_witness.py"
/usr/bin/time -lp python3 "$ROUND82_TMP/rin_xor_csp_search.py" --variables 2 --exists 1 --clauses 2 --width 2
/usr/bin/time -lp python3 "$ROUND82_TMP/rin_xor_csp_search.py" --variables 2 --exists 1 --clauses 3 --width 2
/usr/bin/time -lp python3 "$ROUND82_TMP/rin_xor_csp_search.py" --variables 2 --exists 1 --clauses 4 --width 2 --progress 1000
/usr/bin/time -lp python3 "$ROUND82_TMP/rin_xor_csp_search.py" --variables 3 --exists 1 --clauses 2 --width 3
/usr/bin/time -lp python3 "$ROUND82_TMP/kernel_pivot_random_m4.py"
```

The actual scratch root was `/tmp/circdist-cplx-sigma2-r5-round82-20260830`; it is deleted at settlement. The verbatim core listings follow so the tests can be reconstructed.

### 10.4 Reproducibility hashes for final harnesses and outputs

| scratch file | SHA-256 |
|---|---|
| `abstract_census.py` | `4e6c8ebb42213781cbb3918cc344896ce696843cd7ad91d5e45d301430a65a7d` |
| `abstract_census.out` | `4e41f9f2a9aab2a73c84e0366abb3c91628717d8c7a6fec2b16dfaf595ffaf55` |
| `plane_gate.py` | `3db3a931ca6c8e58e34fdb42ef1e788be4d4ff4b19ebb47ab6c571c3807df182` |
| `plane_gate.out` | `4f52bdf05928cffaad1d627566efb387f19ee00ac7adf1856ed5a3406333b1c1` |
| `compiler_audit.py` | `d090a4682ea3f23e756deb40ee4ee681ae0c5b82626c5de16498851e2e987dd1` |
| `compiler_audit2.out` | `829599ef115ddfc4a1fa28b9db9650a784f43652a313abe91c2d6b78a2868671` |
| `grid_block_audit.py` | `106e7a3eaf6fa3da81d014da104288a2dfee3a079dd3b867603f2023b1333bb1` |
| `grid_block_audit.out` | `0faff3eea85e529322b9f8d384449a420ccf08b40e2984b8778d35eea981c7b5` |
| `constant_instance_audit.py` | `5d0628b72f4e43b12bfddd360d7a98f099dbdff7e8dc26bbe0b9c0d780b472e5` |
| `constant_instance_audit.out` | `21778d05637f97afe3ef56e6ac3b828dcdbc6dbf1d23570b485b8ef6e73c03b8` |
| `kernel_shortcut_witness.py` | `465623e89e53e4f6f2c583d1867b6688e7e4982908741c5f1bdc3ad04d36ad2d` |
| `kernel_shortcut_witness.out` | `8ebcac52bb04855a14d937c336ff3bc442325705be9d581e0e5d8d6c10977c8c` |
| `rin_xor_csp_search.py` | `ef80e03c9bcd49edecef30400bd08bbe745aa02984a713ef638fa0e653643cc4` |
| final `v2,m2` output | `53eea3f5ccde44cd3d9eaf908ad254a1b56f8c293f839ea3f28a032adb264718` |
| final `v2,m3` output | `a40f522a803570d6d16e0cbac5facb2a151d9b0bd391e92c46aa1a4c89be9d72` |
| final `v2,m4` output | `d664ac80dadf8673414a549079b40c700161a4082f03ea243d797f0419778f5f` |
| final `v3,m2` output | `88e2be52d968125a0ea7a1388dc4aca17b5ea377fee0d5bfd2a0818769b82507` |

## 11. Core code listings

### 11.1 `abstract_census.py`

```python
#!/usr/bin/env python3
from itertools import combinations, product

# One existential x and two universal variables y,z. A clause is a tuple of
# signed literals (var, satisfying_bit), with no repeated variable.
VARS = ('x','y','z')
clauses=[]
for size in (1,2,3):
    for vs in combinations(VARS,size):
        for bits in product((0,1), repeat=size):
            clauses.append(tuple(zip(vs,bits)))


def clause_sat(clause,a):
    return any(a[v]==b for v,b in clause)

def psi_sat(formula,a):
    return all(clause_sat(c,a) for c in formula)

def build(formula):
    # markers: variable groups then clause groups; occurrence bits follow.
    group_count=3+len(formula)
    occ=[]
    for j,c in enumerate(formula):
        for pos,(v,b) in enumerate(c): occ.append((j,pos,v))
    occ_index={o:group_count+i for i,o in enumerate(occ)}
    cols=[] # (name,group,label,kind)
    for vi,v in enumerate(VARS):
        for b in (0,1):
            lab=1<<vi
            if b:
                for o,idx in occ_index.items():
                    if o[2]==v: lab ^= 1<<idx
            cols.append((f'V:{v}:{b}',vi,lab,'x' if v=='x' else 'u'))
    for j,c in enumerate(formula):
        cvars=tuple(v for v,_ in c)
        for bits in product((0,1),repeat=len(cvars)):
            a=dict(zip(cvars,bits))
            if clause_sat(c,a):
                lab=1<<(3+j)
                for pos,(v,_) in enumerate(c):
                    if a[v]: lab ^= 1<<occ_index[(j,pos,v)]
                cols.append((f'C:{j}:{bits}',3+j,lab,'u'))
    target=(1<<group_count)-1
    return group_count,cols,target

def min_subset(labels,target,nonempty=False):
    inf=10**9
    dp={0:0}
    for lab in labels:
        nxt=dict(dp)
        for s,w in dp.items():
            ns=s^lab
            if w+1<nxt.get(ns,inf): nxt[ns]=w+1
        dp=nxt
    if target==0 and nonempty:
        # DP loses nonempty zero. Pair-state DP records whether anything chosen.
        dp={(0,0):0}
        for lab in labels:
            nxt=dict(dp)
            for (s,used),w in dp.items():
                ns=(s^lab,1)
                if w+1<nxt.get(ns,inf): nxt[ns]=w+1
            dp=nxt
        return dp.get((0,1))
    return dp.get(target)

formula_count=0
schedule_count=0
abstract_mismatch=0
flagged_mismatch=0
naive_false_no=0
naive_shortcuts=0
min_shortcut=None
first_false_no=None
for m in (1,2):
  for formula in product(clauses,repeat=m):
    formula_count += 1
    K,cols,target=build(formula)
    d=K+2
    for xb in (0,1):
      schedule_count += 1
      allowed=[c for c in cols if c[3]=='u' or c[0]==f'V:x:{xb}']
      labs=[c[2] for c in allowed]
      rep=min_subset(labs,target)
      witness=any(psi_sat(formula,{'x':xb,'y':yb,'z':zb}) for yb,zb in product((0,1),repeat=2))
      if ((rep is not None and rep<=K) != witness): abstract_mismatch += 1
      # Any representation of weight at most K must have exactly K by marker count.
      if rep is not None and rep <= K and rep != K: abstract_mismatch += 1
      flagged=None if rep is None else 1+rep
      unsafe=(flagged is not None and flagged<d)
      if unsafe != witness: flagged_mismatch += 1
      zero=min_subset(labs,0,nonempty=True)
      if zero is not None and zero<d:
        naive_shortcuts += 1
        min_shortcut=zero if min_shortcut is None else min(min_shortcut,zero)
        # QBF branch is safe iff psi has no universal witness.
        if not witness:
          naive_false_no += 1
          if first_false_no is None: first_false_no=(formula,xb,K,d,zero)
print('clause_templates',len(clauses))
print('formulae',formula_count,'schedules',schedule_count)
print('abstract_mismatch',abstract_mismatch,'flagged_mismatch',flagged_mismatch)
print('naive_shortcut_schedules',naive_shortcuts,'min_shortcut',min_shortcut)
print('naive_false_no_schedules',naive_false_no)
print('first_false_no',first_false_no)
assert abstract_mismatch==0 and flagged_mismatch==0
assert naive_false_no>0
print('ALL_CHECKS_PASS')
```

### 11.2 `plane_gate.py`

```python
#!/usr/bin/env python3
from itertools import product, combinations
from collections import deque

# Literals are (variable_name, positive). Clause local columns enumerate satisfying assignments.
def sat_clause(clause, a):
    return any((a[v] if pos else 1-a[v]) for v,pos in clause)

def xor_all(xs):
    z=0
    for x in xs: z ^= x
    return z

def build(clauses, xvars, yvars):
    vars_ = list(xvars)+list(yvars)
    occ={v:[] for v in vars_}
    for j,C in enumerate(clauses):
        for r,(v,pos) in enumerate(C): occ[v].append((j,r))
    groups=[('var',v) for v in vars_]+[('clause',j) for j in range(len(clauses))]
    bit={g:i for i,g in enumerate(groups)}
    nxt=len(bit)
    edge={}
    # One star edge from variable-value group to each occurrence.
    for v in vars_:
        for o in occ[v]: edge[(v,o)]=nxt; nxt+=1
    cols={}
    for v in vars_:
        for b in (0,1):
            z=1<<bit[('var',v)]
            if b:
                for o in occ[v]: z ^= 1<<edge[(v,o)]
            cols[('var',v,b)]=z
    for j,C in enumerate(clauses):
        cv=sorted(set(v for v,_ in C))
        for bits in product((0,1), repeat=len(cv)):
            a=dict(zip(cv,bits))
            if not sat_clause(C,a): continue
            z=1<<bit[('clause',j)]
            for r,(v,pos) in enumerate(C):
                if a[v]: z ^= 1<<edge[(v,(j,r))]
            cols[('clause',j,tuple(bits))]=z
    target=sum(1<<bit[g] for g in groups)
    return cols,target,len(groups),nxt,groups

def min_xor(columns, target, cap=None):
    # exact BFS in syndrome space, retaining witness, each column at most once
    dist={0:(0,())}
    for name,val in columns:
        old=list(dist.items())
        for s,(w,W) in old:
            t=s^val
            if t not in dist or dist[t][0]>w+1:
                dist[t]=(w+1,W+(name,))
    return dist.get(target)

def available(cols, xassign, xvars):
    out=[]
    for name,z in cols.items():
        if name[0]=='var' and name[1] in xvars and name[2]!=xassign[name[1]]: continue
        out.append((name,z))
    return out

def source_psi(clauses,a): return all(sat_clause(C,a) for C in clauses)

# QBF Phi = not psi, psi = x AND (y OR z OR w).  x=0 makes Phi true for every y,z,w.
clauses=[(('x',True),), (('y',True),('z',True),('w',True))]
xvars=('x',); yvars=('y','z','w')
cols,target,K,D,groups=build(clauses,xvars,yvars)
print('columns',len(cols),'groups_K',K,'syndrome_dim',D,'target_weight',bin(target).count('1'))
# Verify source truth and the exact <=K target representation equivalence for each x.
for xb in (0,1):
    xa={'x':xb}
    bad=[]
    for ybits in product((0,1),repeat=len(yvars)):
        a=xa|dict(zip(yvars,ybits))
        if source_psi(clauses,a): bad.append(a)
    A=available(cols,xa,xvars)
    rep=min_xor(A,target)
    print('x',xb,'psi_witnesses',len(bad),'target_min',None if rep is None else rep[0])
    assert (rep is not None and rep[0]<=K)==bool(bad)
    if rep is not None: assert rep[0]==K
# Flagged abstract model: anchor=(target,flag 1); only an odd anchor count is logical.
# With one anchor slot, a bad logical has size K+1 iff a target representation exists.
d=K+2
for xb in (0,1):
    A=available(cols,{'x':xb},xvars)
    rep=min_xor(A,target)
    flagged=None if rep is None else 1+rep[0]
    print('flagged_x',xb,'min_logical',flagged,'threshold_d',d,'safe',flagged is None or flagged>=d)
# Naive plane quotient (S_X only disjoint full-plane rows): every nonempty zero-syndrome
# hook combination is a logical. Find the minimum anchor-free zero relation among available hooks.
def min_nonempty_zero(columns):
    # DP: syndrome -> min nonempty weight and witness
    dp={}
    for name,val in columns:
        nd=dict(dp)
        if val==0 and (0 not in nd or nd[0][0]>1): nd[0]=(1,(name,))
        for s,(w,W) in dp.items():
            t=s^val
            if t not in nd or nd[t][0]>w+1: nd[t]=(w+1,W+(name,))
        if val not in nd or nd[val][0]>1: nd[val]=(1,(name,))
        dp=nd
    return dp.get(0)
for xb in (0,1):
    A=available(cols,{'x':xb},xvars)
    zr=min_nonempty_zero(A)
    print('naive_x',xb,'anchor_free_zero_min',zr[0], 'witness',zr[1])
    assert zr[0]==4
print('qbf_truth', any(all(not source_psi(clauses, {'x':xb}|dict(zip(yvars,yb))) for yb in product((0,1),repeat=3)) for xb in (0,1)))
print('naive_plane_verdict','NO for both schedules because 4 < d=8')
print('static_weight_of_shortcut',2*4,'equals_d',d)
print('ALL_CHECKS_PASS')
```

### 11.3 `compiler_audit.py`

```python
#!/usr/bin/env python3
from itertools import product, combinations
from plane_gate import build, available

def pop(x): return bin(x).count('1')
def xor(xs):
    z=0
    for x in xs:z^=x
    return z

def rref(rows):
    R=[]; piv=[]
    for x in rows:
        for b,p in zip(R,piv):
            if (x>>p)&1:x^=b
        if not x:continue
        p=x.bit_length()-1
        for i,b in enumerate(R):
            if (b>>p)&1:R[i]^=x
        R.append(x);piv.append(p)
    return R,piv

def inspan(x,rows):
    R,piv=rref(rows)
    for b,p in zip(R,piv):
        if (x>>p)&1:x^=b
    return x==0

def kernel_of_rows(rows,n):
    # equations rows dot x=0. conventional low-pivot elimination
    A=[r for r in rows if r]
    rank=0;piv=[]
    for c in range(n):
        k=next((i for i in range(rank,len(A)) if (A[i]>>c)&1),None)
        if k is None:continue
        A[rank],A[k]=A[k],A[rank]
        for i in range(len(A)):
            if i!=rank and ((A[i]>>c)&1):A[i]^=A[rank]
        piv.append(c);rank+=1
        if rank==len(A):break
    free=[c for c in range(n) if c not in piv]
    basis=[]
    for f in free:
        v=1<<f
        for i,p in enumerate(piv):
            if (A[i]>>f)&1:v|=1<<p
        basis.append(v)
    return basis

def rows_from_column_labels(labels,dim):
    rows=[]
    for b in range(dim):
        r=0
        for j,x in enumerate(labels):
            if (x>>b)&1:r|=1<<j
        rows.append(r)
    return rows

clauses=[(('x',True),), (('y',True),('z',True),('w',True))]
xvars=('x',);yvars=('y','z','w')
cols,tau,K,D,groups=build(clauses,xvars,yvars)
flagbit=D
abstract={name:(s | (0<<flagbit)) for name,s in cols.items()}
abstract[('anchor',)]=tau | (1<<flagbit)
# Planes: one selectable x plane with its two values; every other abstract column one fixed plane.
planes=[]
x0=abstract[('var','x',0)];x1=abstract[('var','x',1)]
planes.append(('x-select',x0,x1,False))
for name,wv in abstract.items():
    if name in (('var','x',0),('var','x',1)):continue
    planes.append((name,wv,None,True))
# Allocate p for every plane and r for fixed planes, as new syndrome (not flag) dimensions.
nextbit=D+1
labels=[]; plane_qubits=[]
for name,a,b,fixed in planes:
    p=1<<nextbit;nextbit+=1
    if fixed:
        r=1<<nextbit;nextbit+=1
        bb=r
    else:bb=b
    qs=[p,p^a,p^bb,p^a^bb]
    base=len(labels);labels.extend(qs);plane_qubits.append((name,tuple(range(base,base+4)),a,bb,fixed))
dim=nextbit
B_rows=rows_from_column_labels(labels,dim)
HZ_rows=[r for i,r in enumerate(B_rows) if i!=flagbit]
ell=B_rows[flagbit]
HX_basis=kernel_of_rows(B_rows,len(labels))
plane_rows=[sum(1<<q for q in qs) for _,qs,_,_,_ in plane_qubits]
assert all(not pop(r & z)%2 for r in HX_basis+plane_rows for z in HZ_rows)
rankB=len(rref(B_rows)[0]); rankHZ=len(rref(HZ_rows)[0]); rankHX=len(rref(HX_basis+plane_rows)[0])
print('planes',len(planes),'n',len(labels),'label_dim',dim,'rankB',rankB,'rankHZ',rankHZ,'rankHX',rankHX,'k',len(labels)-rankHZ-rankHX)
print('ell_weight',pop(ell),'ell_in_HZ',inspan(ell,HZ_rows),'therefore_dZ_upper',pop(ell))
assert pop(ell)==2 and not inspan(ell,HZ_rows)
assert len(labels)-rankHZ-rankHX==1
# The full-kernel equality.
assert rankHX==len(labels)-rankB
print('SX_equals_kerB',True)
# Desired static X relation at x=1 uses two physical columns per selected abstract hook.
print('K',K,'threshold_d',K+2,'anchor_plus_K_hook_faults',K+1,'same_relation_physical_singletons',2*(K+1))
# Canonical dense-kernel schedule attack: increasing support for kernel-basis rows; selected plane orders.
def suffixes(order):
    out=[];v=0
    for q in reversed(order):
        v^=1<<q;out.append(v)
    return out[:-1]
def class_label(mask):
    z=0
    for q,a in enumerate(labels):
        if (mask>>q)&1:z^=a
    return z
# Build schedules for x=0,1. Definition basis checks plus dependent plane checks.
for xb in (0,1):
    hook_classes=[]
    for row in HX_basis:
        order=[q for q in range(len(labels)) if (row>>q)&1]
        hook_classes += [class_label(h) for h in suffixes(order)]
    for name,qs,a,b,fixed in plane_qubits:
        if name=='x-select':
            # last pair {0,1} for x0, {0,2} for x1
            order=[qs[2],qs[3],qs[0],qs[1]] if xb==0 else [qs[1],qs[3],qs[0],qs[2]]
        else: order=[qs[2],qs[3],qs[0],qs[1]]
        hook_classes += [class_label(h) for h in suffixes(order)]
    single_classes=labels
    allc=single_classes+hook_classes
    one=[c for c in allc if c==(1<<flagbit)]
    # Find two-column pure logical.
    seen={}
    pair=None
    for i,c in enumerate(allc):
        want=c^(1<<flagbit)
        if want in seen:pair=(seen[want],i);break
        seen[c]=i
    print('x',xb,'columns',len(allc),'pure_logical_one',len(one),'pure_logical_pair',pair)
print('ALL_CHECKS_PASS')
# Exact meet-in-the-middle minimum through d-1, collapsing duplicate class labels.
def combinations_xor(classes,maxw):
    # Maps XOR to (minimum weight,witness tuple). Dynamic 0/1 construction.
    levels=[{0:()}]
    for w in range(1,maxw+1): levels.append({})
    # Enumeration by increasing last index prevents reuse.
    states={(0,0):()} # unused placeholder
    def rec(start,left,x,idxs,out):
        if left==0:
            if x not in out: out[x]=idxs
            return
        for i in range(start,len(classes)-left+1): rec(i+1,left-1,x^classes[i],idxs+(i,),out)
    for w in range(maxw+1): rec(0,w,0,(),levels[w])
    return levels

for xb in (0,1):
    hook_classes=[]
    for row in HX_basis:
        order=[q for q in range(len(labels)) if (row>>q)&1]
        hook_classes += [class_label(h) for h in suffixes(order)]
    for name,qs,a,b,fixed in plane_qubits:
        if name=='x-select':
            order=[qs[2],qs[3],qs[0],qs[1]] if xb==0 else [qs[1],qs[3],qs[0],qs[2]]
        else: order=[qs[2],qs[3],qs[0],qs[1]]
        hook_classes += [class_label(h) for h in suffixes(order)]
    classes=sorted(set(labels+hook_classes)-{0})
    levels=combinations_xor(classes,4)
    target=1<<flagbit
    best=None;wit=None
    for wa in range(4):
      for wb in range(5):
        if wa+wb>7:continue
        A=levels[wa];BB=levels[wb]
        for s,ia in A.items():
          ib=BB.get(s^target)
          if ib is not None:
            # Symmetric difference is a valid subset and no larger.
            ii=tuple(sorted(set(ia)^set(ib)))
            val=0
            for i in ii:val^=classes[i]
            assert val==target
            if best is None or len(ii)<best:best=len(ii);wit=ii
    print('exact_through_7_x',xb,'unique_classes',len(classes),'min',best,'witness_labels',None if wit is None else tuple(hex(classes[i]) for i in wit))
```

### 11.4 `grid_block_audit.py`

```python
#!/usr/bin/env python3
from itertools import product

def bit(i,j,R): return 1<<(i*R+j)

def label(z,D,R):
    s=0;k=0
    # HX adjacent-pair syndrome: dot z with e_ij+e_i,j+1.
    for i in range(D):
      for j in range(R-1):
        if ((z>>(i*R+j))^(z>>(i*R+j+1)))&1: s ^= 1<<k
        k+=1
    ell=0
    for i in range(D): ell ^= (z>>(i*R))&1
    return s | (ell<<k)

def min_fault(D,R,order_kind):
    gam=[]
    # physical singletons
    for i in range(D):
      for j in range(R): gam.append(('e',i,j,bit(i,j,R)))
    # HZ adjacent whole-row-pair checks
    for i in range(D-1):
      if order_kind=='blocked':
        order=[bit(i,j,R) for j in range(R)]+[bit(i+1,j,R) for j in range(R)]
      elif order_kind=='alternating':
        order=[]
        for j in range(R): order += [bit(i,j,R),bit(i+1,j,R)]
      elif order_kind=='snake':
        order=[]
        for j in range(R): order += [bit(i,j,R),bit(i+1,R-1-j,R)]
      else: raise ValueError
      suf=0
      for q in reversed(order[1:]): # wrong construction? build all proper suffixes below
        pass
      for cut in range(1,len(order)):
        v=0
        for q in order[cut:]: v^=q
        gam.append(('h',i,cut,v))
    L=D*(R-1)+1
    target=1<<(L-1)
    dp={0:(0,())}
    for name in gam:
      lab=label(name[-1],D,R)
      nxt=dict(dp)
      for s,(w,path) in dp.items():
        ns=s^lab
        if ns not in nxt or w+1<nxt[ns][0]: nxt[ns]=(w+1,path+(name[:-1],))
      dp=nxt
    return dp.get(target),len(gam),L

for D in range(2,5):
  R=D
  for kind in ('blocked','alternating','snake'):
    ans,ng,L=min_fault(D,R,kind)
    print('D',D,'R',R,'order',kind,'gamma',ng,'labels',L,'d_eff_Z',ans[0], 'witness',ans[1])
print('DONE')
```

### 11.5 Exact frozen RIN XOR-CSP census implementation

This single parameterized program generated every final frozen RIN row in §10.

```python
#!/usr/bin/env python3
"""Exact bounded RIN counterexample search.

The outer loop enumerates normalized CNF incidence tensors.  For every source-safe
existential schedule it builds the frozen affine-plane/full-kernel compiler and
the group-block bookend orders.  The inner problem is the Boolean XOR-CSP

  exactly_one({z[g,c] : c in catalogue group g})  for every group g,
  XOR_{g,c:z[g,c]} residual(c) = 0.

This is precisely the K-nonanchor-column equality case after the proved marker
charging lemma.  The solver is exact dynamic programming over XOR syndromes;
states with the same partial syndrome are interchangeable for all remaining
constraints, so retaining one witness per state is lossless.
"""
from itertools import combinations, product
import argparse, random, sys, time

def pop(x): return bin(x).count('1')
def sat_clause(C,a): return any(a[v] == b for v,b in C)
def psi(formula,a): return all(sat_clause(C,a) for C in formula)

def build(formula, variables):
    groups=[('v',v) for v in variables]+[('c',j) for j in range(len(formula))]
    gb={g:i for i,g in enumerate(groups)}
    nxt=len(groups); occ={}
    for j,C in enumerate(formula):
        for r,(v,b) in enumerate(C): occ[(v,j,r)]=nxt; nxt+=1
    cols={}
    for v in variables:
        for b in (0,1):
            z=1 << gb[('v',v)]
            if b:
                for (vv,j,r),k in occ.items():
                    if vv == v: z ^= 1 << k
            cols[('v',v,b)]=z
    for j,C in enumerate(formula):
        cv=tuple(sorted(v for v,b in C))
        for bits in product((0,1), repeat=len(cv)):
            a=dict(zip(cv,bits))
            if not sat_clause(C,a): continue
            z=1 << gb[('c',j)]
            for r,(v,b) in enumerate(C):
                if a[v]: z ^= 1 << occ[(v,j,r)]
            cols[('c',j,bits)]=z
    return cols,groups,nxt

def rows_from_labels(labels,dim):
    return [sum(1 << j for j,x in enumerate(labels) if (x >> b)&1)
            for b in range(dim)]

def rref_add(basis,x):
    y=x
    for p,b in basis:
        if (y >> p)&1: y ^= b
    if not y: return False
    p=y.bit_length()-1
    for i,(q,b) in enumerate(basis):
        if (b >> p)&1: basis[i]=(q,b^y)
    basis.append((p,y)); basis.sort(reverse=True)
    return True

def kernel(rows,n):
    A=[r for r in rows if r]; rank=0; piv=[]
    for c in range(n):
        k=next((i for i in range(rank,len(A)) if (A[i] >> c)&1),None)
        if k is None: continue
        A[rank],A[k]=A[k],A[rank]
        for i in range(len(A)):
            if i != rank and ((A[i] >> c)&1): A[i] ^= A[rank]
        piv.append(c); rank+=1
        if rank == len(A): break
    free=[c for c in range(n) if c not in piv]; out=[]
    for f in free:
        z=1 << f
        for i,p in enumerate(piv):
            if (A[i] >> f)&1: z ^= 1 << p
        out.append(z)
    return out

def suffix_catalogue(order,labels,tag):
    out=[]; z=0
    for cut,q in enumerate(reversed(order),1):
        z ^= labels[q]
        if cut < len(order): out.append((z,(tag,'suffix-last',cut)))
    return out

def compile_catalogue(formula, variables, exists, alpha):
    cols,groups,D=build(formula,variables); K=len(groups); flag=D
    abstract=dict(cols); tau=(1 << K)-1
    abstract[('anchor',)]=tau | (1 << flag)
    planes=[]
    for v in exists:
        planes.append((('select',v),abstract[('v',v,0)],abstract[('v',v,1)],False))
    for name,a in abstract.items():
        if name[0]=='v' and name[1] in exists: continue
        planes.append((name,a,None,True))
    labels=[]; meta=[]; nxt=D+1
    for name,a,b,fixed in planes:
        p=1 << nxt; nxt+=1
        if fixed:
            r=1 << nxt; nxt+=1; b=r
        qs=tuple(range(len(labels),len(labels)+4))
        labels += [p,p^a,p^b,p^a^b]
        meta.append((name,qs,fixed))

    Brows=rows_from_labels(labels,nxt); ker=kernel(Brows,len(labels))
    prows=[sum(1 << q for q in qs) for _,qs,_ in meta]

    # Build the quotient relation matrix directly: one coordinate a0+a1 for
    # each selector plane, and one coordinate a for every fixed plane.  RREF
    # its kernel using fixed coordinates first.  The fixed-coordinate
    # projection is injective after unused variables are deleted, so this gives
    # one distinct fixed pivot per relation row.
    rel_labels=[]; rel_plane=[]; fixed_rel=[]
    for pi,(name,qs,fixed) in enumerate(meta):
        if name[0]=='select':
            rel_labels.append(labels[qs[0]] ^ labels[qs[3]])
        else:
            rel_labels.append(labels[qs[0]] ^ labels[qs[1]])
            if name != ('anchor',): fixed_rel.append(len(rel_labels)-1)
        rel_plane.append(pi)
    rel_basis=kernel(rows_from_labels(rel_labels,nxt),len(rel_labels))
    rel_basis=list(rel_basis); rank=0; pivot_rel=[]
    for c in fixed_rel:
        k=next((i for i in range(rank,len(rel_basis)) if (rel_basis[i] >> c)&1),None)
        if k is None: continue
        rel_basis[rank],rel_basis[k]=rel_basis[k],rel_basis[rank]
        for i in range(len(rel_basis)):
            if i != rank and ((rel_basis[i] >> c)&1):
                rel_basis[i] ^= rel_basis[rank]
        pivot_rel.append(c); rank+=1
        if rank == len(rel_basis): break
    if rank != len(rel_basis):
        return None,('fixed-projection-rank-fail',rank,len(rel_basis))

    extra_rows=[]
    for rr in rel_basis:
        row=0
        for ri,pi in enumerate(rel_plane):
            if not ((rr >> ri)&1): continue
            name,qs,fixed=meta[pi]
            other=qs[3] if name[0]=='select' else qs[1]
            row ^= (1 << qs[0]) | (1 << other)
        assert row and all((pop(row & br)&1)==0 for br in Brows)
        extra_rows.append(row)
    checks=[('plane',r) for r in prows]+[('extra',r) for r in extra_rows]
    basis=[]
    for typ,r in checks: assert rref_add(basis,r)
    assert len(checks)==len(ker),(len(checks),len(ker))

    def group_of(name):
        if name[0]=='v': return ('v',name[1])
        if name[0]=='c': return ('c',name[1])
        raise AssertionError(name)

    catalogue=[(x,('singleton',q)) for q,x in enumerate(labels)]
    extra_orders=[]
    for ei,row in enumerate(extra_rows):
        selected=[]
        for name,qs,fixed in meta:
            hit=[q for q in qs if (row >> q)&1]
            if hit: selected.append((name,hit,qs))
        pivot_pi=rel_plane[pivot_rel[ei]]
        p_name,p_qs,p_fixed=meta[pivot_pi]
        p_hit=[q for q in p_qs if (row >> q)&1]
        piv=(p_name,p_hit,p_qs)
        if (p_name[0] in ('select','anchor') or len(p_hit)!=2 or
            any(any((o >> q)&1 for q in p_qs)
                for j,o in enumerate(extra_rows) if j != ei)):
            return None,('pivot-fail',ei,row,pivot_rel[ei])
        early=[piv[2][0]]; late=[]; pg=group_of(piv[0])
        for name,hit,qs in selected:
            if name == piv[0]: continue
            if name[0]=='select': early += [qs[0],qs[3]]
            else:
                assert name != ('anchor',)
                early.append(qs[0]); late.append((group_of(name),name,qs[1]))
        late.sort(key=lambda z:(z[0] == pg,z[0],str(z[1])))
        order=early+[q for g,nm,q in late]+[piv[2][1]]
        assert len(order)==pop(row) and len(set(order))==len(order)
        extra_orders.append(order)
        catalogue += suffix_catalogue(order,labels,('extra',ei,tuple(order)))

    for pi,(name,qs,fixed) in enumerate(meta):
        if name[0]=='select':
            b=alpha[name[1]]
            order=[qs[2],qs[3],qs[0],qs[1]] if b==0 else [qs[1],qs[3],qs[0],qs[2]]
        else:
            order=[qs[2],qs[3],qs[0],qs[1]]
        catalogue += suffix_catalogue(order,labels,('plane',pi,name,tuple(order)))

    # Boolean XOR-CSP variables: one distinct residual label per group.  Equal
    # labels at different indexed fault locations are interchangeable for this
    # existence query; preserve one provenance witness for audit.
    bygroup=[{} for _ in groups]; gmask=(1 << K)-1
    for z,prov in catalogue:
        gp=z & gmask
        if pop(gp) != 1 or ((z >> flag)&1): continue
        gi=(gp & -gp).bit_length()-1
        residual=z ^ gp
        bygroup[gi].setdefault(residual,prov)
    assert all(bygroup)
    data=dict(labels=labels,meta=meta,checks=checks,extra_rows=extra_rows,
              extra_orders=extra_orders,catalogue=catalogue,nxt=nxt,flag=flag,
              K=K,groups=groups)
    return (bygroup,data),None

def solve_xor_exact_one(bygroup,max_states=20_000_000):
    # Sort only for the state search; retain original group indices in witness.
    order=sorted(range(len(bygroup)),key=lambda g:len(bygroup[g]))
    states={0:()}; peak=1
    for gi in order:
        ns={}
        for x,w in states.items():
            for r in bygroup[gi]: ns.setdefault(x^r,w+((gi,r),))
        states=ns; peak=max(peak,len(states))
        if len(states)>max_states: return None,peak,('state-cap',gi,len(states))
    return states.get(0),peak,None

def source_safe(formula, variables, exists, alpha):
    univ=[v for v in variables if v not in exists]
    return not any(psi(formula,{**alpha,**dict(zip(univ,bits))})
                   for bits in product((0,1),repeat=len(univ)))

def clause_types(variables,max_width):
    out=[]
    for size in range(1,min(max_width,len(variables))+1):
        for vs in combinations(variables,size):
            for bits in product((0,1),repeat=size): out.append(tuple(zip(vs,bits)))
    return out

def witness_report(formula,variables,exists,alpha,bygroup,data,wit):
    lines=[]
    lines.append('COUNTEREXAMPLE')
    lines.append('variables='+repr(variables)+' exists='+repr(exists)+' alpha='+repr(alpha))
    lines.append('formula='+repr(formula))
    lines.append('K=%d d=%d n=%d extra_rows=%d' %
                 (data['K'],data['K']+2,len(data['labels']),len(data['extra_rows'])))
    z=0
    for gi,r in sorted(wit):
        gp=1 << gi; full=gp^r; z ^= full
        lines.append('group=%r full=0x%x residual=0x%x provenance=%r' %
                     (data['groups'][gi],full,r,bygroup[gi][r]))
    lines.append('xor_nonanchor=0x%x expected_tau=0x%x' % (z,(1<<data['K'])-1))
    for i,(row,order) in enumerate(zip(data['extra_rows'],data['extra_orders'])):
        lines.append('extra[%d]=0x%x order=%r' % (i,row,order))
    return '\n'.join(lines)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--variables',type=int,default=3)
    ap.add_argument('--exists',type=int,default=1)
    ap.add_argument('--clauses',type=int,default=3)
    ap.add_argument('--width',type=int,default=3)
    ap.add_argument('--limit',type=int,default=0,help='0 means exhaustive')
    ap.add_argument('--random',action='store_true')
    ap.add_argument('--seed',type=int,default=8205)
    ap.add_argument('--progress',type=int,default=1000)
    args=ap.parse_args()
    names=tuple('xyzuvw'[:args.variables]); exists=names[:args.exists]
    clauses=clause_types(names,args.width); rng=random.Random(args.seed)
    if args.random:
        formulas=(tuple(rng.choice(clauses) for _ in range(args.clauses))
                  for _ in range(args.limit))
    else:
        formulas=product(clauses,repeat=args.clauses)
    total=safe=compiled=counter=pivot_fail=capped=0; peak=0; t0=time.time()
    for fi,formula in enumerate(formulas):
        if args.limit and not args.random and fi>=args.limit: break
        # Canonical normalization deletes quantified variables with no occurrence;
        # the fixed-pivot existence proof is stated only after this deletion.
        if any(all(vv != v for C in formula for vv,b in C) for v in names):
            continue
        for abits in product((0,1),repeat=len(exists)):
            total+=1; alpha=dict(zip(exists,abits))
            if not source_safe(formula,names,exists,alpha): continue
            safe+=1
            ans,err=compile_catalogue(formula,names,exists,alpha)
            if err:
                pivot_fail+=1
                print('PIVOT_FAIL',formula,alpha,err); return 3
            bygroup,data=ans; compiled+=1
            wit,pk,serr=solve_xor_exact_one(bygroup); peak=max(peak,pk)
            if serr:
                capped+=1
                print('STATE_CAP',formula,alpha,serr); return 4
            if wit is not None:
                counter+=1
                print(witness_report(formula,names,exists,alpha,bygroup,data,wit))
                print('SUMMARY total=%d safe=%d compiled=%d counter=%d peak_states=%d elapsed=%.3f' %
                      (total,safe,compiled,counter,peak,time.time()-t0))
                return 2
        if args.progress and (fi+1)%args.progress==0:
            print('PROGRESS formulas=%d total=%d safe=%d peak_states=%d elapsed=%.3f' %
                  (fi+1,total,safe,peak,time.time()-t0),file=sys.stderr,flush=True)
    print('NO_COUNTEREXAMPLE variables=%d exists=%d clauses=%d width=%d mode=%s formulas=%d schedules=%d safe=%d compiled=%d pivot_fail=%d capped=%d peak_states=%d elapsed=%.3f' %
          (args.variables,args.exists,args.clauses,args.width,
           'random' if args.random else 'exhaustive',
           total//(1<<len(exists)),total,safe,compiled,pivot_fail,capped,peak,time.time()-t0))
    return 0

if __name__=='__main__': raise SystemExit(main())
```

### 11.6 Exact Gaussian/increasing counterexample implementation

```python
#!/usr/bin/env python3
from itertools import combinations, product

def pop(x): return bin(x).count('1')
def sat_clause(C,a): return any(a[v]==b for v,b in C)
def psi(formula,a): return all(sat_clause(C,a) for C in formula)
def build(formula):
  vars_=('x','y');groups=[('v',v) for v in vars_]+[('c',j) for j in range(len(formula))]
  gb={g:i for i,g in enumerate(groups)};nxt=len(groups);occ={}
  for j,C in enumerate(formula):
    for r,(v,b) in enumerate(C):occ[(v,j,r)]=nxt;nxt+=1
  cols={}
  for v in vars_:
    for b in (0,1):
      z=1<<gb[('v',v)]
      if b:
        for (vv,j,r),k in occ.items():
          if vv==v:z^=1<<k
      cols[('v',v,b)]=z
  for j,C in enumerate(formula):
    cv=tuple(sorted(v for v,b in C))
    for bits in product((0,1),repeat=len(cv)):
      a=dict(zip(cv,bits))
      if not sat_clause(C,a):continue
      z=1<<gb[('c',j)]
      for r,(v,b) in enumerate(C):
        if a[v]:z^=1<<occ[(v,j,r)]
      cols[('c',j,bits)]=z
  return cols,(1<<len(groups))-1,len(groups),nxt

def rows_from_labels(labels,dim):
  return [sum(1<<j for j,x in enumerate(labels) if (x>>b)&1) for b in range(dim)]
def rref_add(basis,x):
  y=x
  for p,b in basis:
    if (y>>p)&1:y^=b
  if not y:return False
  p=y.bit_length()-1
  for i,(q,b) in enumerate(basis):
    if (b>>p)&1:basis[i]=(q,b^y)
  basis.append((p,y));basis.sort(reverse=True)
  return True
def kernel(rows,n):
  A=[r for r in rows if r];rank=0;piv=[]
  for c in range(n):
    k=next((i for i in range(rank,len(A)) if (A[i]>>c)&1),None)
    if k is None:continue
    A[rank],A[k]=A[k],A[rank]
    for i in range(len(A)):
      if i!=rank and ((A[i]>>c)&1):A[i]^=A[rank]
    piv.append(c);rank+=1
    if rank==len(A):break
  free=[c for c in range(n) if c not in piv];out=[]
  for f in free:
    z=1<<f
    for i,p in enumerate(piv):
      if (A[i]>>f)&1:z^=1<<p
    out.append(z)
  return out

def suffix_labels(order,labels):
  out=[];z=0
  for q in reversed(order):
    z^=labels[q];out.append(z)
  return out[:-1]
def min_target(classes,target,cap):
  dp={0:(0,())}
  for i,c in enumerate(classes):
    old=list(dp.items())
    for s,(w,W) in old:
      if w>=cap:continue
      t=s^c
      if t not in dp or dp[t][0]>w+1:dp[t]=(w+1,W+(i,))
  ans=dp.get(target)
  return ans if ans is not None and ans[0]<=cap else None

def compile_case(formula,xb):
  cols,tau,K,D=build(formula);flag=D
  abstract={name:z for name,z in cols.items()};abstract[('anchor',)]=tau|(1<<flag)
  planes=[(('x-select',),abstract[('v','x',0)],abstract[('v','x',1)],False)]
  for name,a in abstract.items():
    if name in (('v','x',0),('v','x',1)):continue
    planes.append((name,a,None,True))
  labels=[];meta=[];nxt=D+1
  for name,a,b,fixed in planes:
    p=1<<nxt;nxt+=1
    if fixed:r=1<<nxt;nxt+=1;b=r
    qs=tuple(range(len(labels),len(labels)+4));labels += [p,p^a,p^b,p^a^b]
    meta.append((name,qs,fixed))
  Brows=rows_from_labels(labels,nxt);ker=kernel(Brows,len(labels))
  prows=[sum(1<<q for q in qs) for _,qs,_ in meta]
  basis=[];checks=[]
  for r in prows:
    assert rref_add(basis,r);checks.append(('plane',r))
  for r in ker:
    if rref_add(basis,r):checks.append(('extra',r))
  assert len(checks)==len(ker)
  provenance={}
  def add_class(c,name):
    if c: provenance.setdefault(c,[]).append(name)
  for q,c in enumerate(labels): add_class(c,('singleton',q))
  extra_count=0;max_extra_w=0
  for typ,row in checks:
    if typ=='plane':continue
    extra_count+=1;max_extra_w=max(max_extra_w,pop(row))
    order=[q for q in range(len(labels)) if (row>>q)&1]
    for cut,c in enumerate(suffix_labels(order,labels),1): add_class(c,('extra',extra_count-1,cut,tuple(order)))
  for name,qs,fixed in meta:
    if name==('x-select',):
      order=[qs[2],qs[3],qs[0],qs[1]] if xb==0 else [qs[1],qs[3],qs[0],qs[2]]
    else:order=[qs[2],qs[3],qs[0],qs[1]]
    for cut,c in enumerate(suffix_labels(order,labels),1): add_class(c,('plane',name,cut,tuple(order)))
  classes=sorted(provenance);d=K+2
  ans=min_target(classes,1<<flag,d-1)
  intended=any(psi(formula,{'x':xb,'y':yb}) for yb in (0,1))
  return intended,ans,K,d,len(labels),len(classes),extra_count,max_extra_w,labels,checks,meta,classes,provenance

# Nonempty clauses over x,y without repeated variables.
clauses=[]
for size in (1,2):
  for vs in combinations(('x','y'),size):
    for bits in product((0,1),repeat=size):clauses.append(tuple(zip(vs,bits)))
count=safe=bad=0;first=None
for m in (2,):
 for formula in product(clauses,repeat=m):
  for xb in (0,1):
   count+=1
   intended0=any(psi(formula,{'x':xb,'y':yb}) for yb in (0,1))
   if intended0: continue
   safe+=1
   intended,ans,*rest=compile_case(formula,xb)
   assert not intended
   if ans is not None:
      bad+=1;first=(formula,xb,ans,rest);break
  if first:break
 if first:break
print('clauses',len(clauses),'cases_examined',count,'safe_schedules',safe,'false_shortcuts',bad)
print('first',first)
if first:
 formula,xb,ans,rest=first
 print('FIRST_FORMULA',formula,'x',xb,'min',ans[0],'witness_class_indices',ans[1])
 print('K,d,n,unique,extra,max_extra_weight',rest[:6])
 classes=rest[-2];provenance=rest[-1]
 for i in ans[1]: print('WITNESS_CLASS',i,hex(classes[i]),provenance[classes[i]])
print('DONE')
```

### 11.7 Fixed promised-NO constant instance audit

```python
#!/usr/bin/env python3

HX=(0b1111,)
HZ=(0b1111,0b1100)
order=(2,3,0,1)

def dot(a,b): return bin(a&b).count('1')&1
def xor_span(rows):
    out={0}
    for r in rows: out |= {x^r for x in tuple(out)}
    return out
def dist(norm_checks,stabs):
    S=xor_span(stabs)
    return min(bin(e).count('1') for e in range(1,16)
               if all(dot(e,h)==0 for h in norm_checks) and e not in S)

assert all(dot(x,z)==0 for x in HX for z in HZ)
dX=dist(HZ,HX); dZ=dist(HX,HZ)
suffix=[]; e=0
for q in reversed(order):
    e ^= 1<<q; suffix.append(e)
suffix=suffix[:-1]
SX=xor_span(HX)
bad=[e for e in suffix if all(dot(e,z)==0 for z in HZ) and e not in SX]
print('CSS',True,'dX',dX,'dZ',dZ,'static',min(dX,dZ))
print('order',order,'proper_suffixes',[hex(e) for e in suffix],
      'one_fault_bad',[hex(e) for e in bad])
assert dX==dZ==2 and 0b0011 in bad
print('DONE')
```

## 12. Licensing, no-inheritance, and FIX-2 settlement contract

### 12.1 Theorem ledger

| item | status | what a fresh reviewer may do |
|---|---|---|
| Grouped Representation Theorem 3.1 | PROVED-IN-ARTIFACT | review/license independently |
| Abstract flagged `QSAT_2` equivalence (3.7) | PROVED-IN-ARTIFACT | review/license as an abstract theorem |
| Affine-plane local order catalogue | PROVED-IN-ARTIFACT | review/license locally |
| Naive-plane four-fault failure | REFUTED construction | cite as exact counterexample |
| Full-kernel CSS quotient algebra | PROVED-IN-ARTIFACT | review/license |
| Single/all-or-none anchor `d_Z<=2` | PROVED-IN-ARTIFACT, scoped | cite only at stated scope |
| `R_R` static/effective theorem | PROVED-IN-ARTIFACT | review/license independently |
| Exact safe `d x d` grid and promise direct sum | PROVED-IN-ARTIFACT | review/license independently |
| Gaussian/increasing five-fault compiler failure | REFUTED construction | cite as exact counterexample |
| Frozen full-kernel quotient, suffix-marker lemma, and `K+1` lower bound | PROVED-IN-ARTIFACT | review/license |
| RIN equality lemma | OPEN RESIDUAL | do not assume |
| `QSAT_2 <=_m Eff-Preserve` | CONDITIONAL ON RIN | no promotion |
| exact target node | NOT PROVED | must remain `OPEN` |

No fact inherits from `CIRCDIST.cplx.upper` except that a later hardness proof would combine with its independently reviewed membership theorem. No fact inherits from the fixed-`d` theorem. The legacy Theorems A/D/E and DEEP-FLAG remain conjectural at their recorded scope. This artifact requests no canonical edit and is not an exact review.

### 12.2 Exact next task

A next proposer needs no covering-radius work, no seed construction, no CSS distance padding, and no opposite-sector sentinel. The task is only:

> Prove or refute RIN for the explicit grouped option matrix, deterministic fixed-coordinate RREF relation basis, and group-block bookend orders of §8.4. A refutation must give a normalized QSAT formula, schedule, exact relation basis/orders, and a `K`-column nonanchor equality witness. A proof must normalize cross-row interval cancellations without increasing the `K`-column budget.

### 12.3 Repository discipline

The baseline `git status --short --untracked-files=all` already contained 10,021 lines of unrelated modified/untracked state. The baseline inventory contained 15,710 regular files. Examples included modified build/status/manifests and thousands of untracked artifacts from other work. None was reverted, staged, committed, or pushed. The only intended durable path from this task is this Markdown artifact. Canonical proof-DAG nodes, scheduler, protocols, reviews, and generated views were read-only and their load-bearing hashes were unchanged at the pre-write recheck.

Post-write validation must report externally (to avoid a self-hash paradox): artifact byte count/SHA-256; baseline-versus-final inventory delta; canonical input rehash; YAML parse status; scratch deletion; and survivor-process scan. No canonical promotion is licensed.
