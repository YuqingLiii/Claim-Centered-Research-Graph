# CIRCDIST.cplx.sigma2 Round 84 fresh final exact review

**Date:** 2026-08-30  
**Reviewer role:** sole fresh strict-serial Round-84 exact reviewer  
**Primary subject:** the unchanged `CIRCDIST.cplx.sigma2` claim and the direct grouped-QSAT / affine-plane / full-kernel / RIN reduction  
**Independence:** I used no subagent, did not contact either the Round-82 proposer or the Round-83 author, and did not use private reasoning from either author. I reconstructed every load-bearing statement from disk, the frozen definition, explicit algebra, and independent programs.  
**Repository discipline:** canonical nodes, generated views, and `operations/circdist/SCHEDULER.yaml` were read-only. This report is the only licensed durable write. I did not stage, commit, push, or alter canonical state.

## Executive adjudication

**F84-RIN-VERDICT: PROVED by fresh review.** The exact theorem introduced as `F83-RIN-NEW` is correct for every normalized nonconstant source formula, every existential schedule, every deterministic fixed-coordinate RREF basis produced by the frozen algorithm, and every indexed singleton or proper suffix fault. The proof is symbolic and does not infer a universal statement from a finite census.

**F84-REDUCTION-VERDICT: PROVED by fresh review.** The assembled map is a total promise-preserving polynomial-time many-one reduction

\[
  \mathrm{QSAT}_{2,3\mathrm{DNF}}\le_m \mathrm{Eff\mbox{-}Preserve}_{d\text{ in input}}.
\]

For each nonconstant source instance and existential schedule \(\alpha\), the output schedule is unsafe below \(d=K+2\) exactly when there is a \(\beta\) with \(\psi(\alpha,\beta)=1\), equivalently when \(\Phi(\alpha,\beta)=0\). The two constant normalization outcomes have explicit promised outputs of the correct truth value. The cluster expansion and grid/direct-sum repair make the static distance exactly the requested \(d\) in both sectors and preserve the intended effective-distance predicate. The construction uses the frozen ordinary qubit-sharing conflicts, no optional depth bound, and has polynomial output size.

**F84-SIGMA2-VERDICT: PROVED by fresh review, with a precise scope boundary.** The unchanged 113-character `CIRCDIST.cplx.sigma2` claim is entailed. The direct reduction proves \(\Sigma_2^P\)-hardness. The independently current-PROVED `CIRCDIST.cplx.upper` claim proves membership for the same frozen promise problem and reduction convention, so the claim's parenthetical completeness statement is valid. This review licenses `CIRCDIST.cplx.sigma2` `OPEN -> PROVED` through the exact replacement YAML in section 13. It does **not** license promotion of the `CIRCDIST.cplx` root; the already-PROVED classification-assembly implication requires a later fresh root-composition review after its last premise changes.

Two reporting repairs are mandatory in any canonical application:

1. the sparse support-incidence/order-list count is \(O(s^3)\), while a dense explicit bit-matrix encoding can require \(O(s^4)\) bits; the old dense-cubic sentence must not be restored;
2. elapsed-time text in two sealed census runs is nondeterministic. Exact semantic projections match their seals, so this is a low-severity reporting defect rather than a mathematical discrepancy.

The fixed-\(d\) theorem, covering-radius route, Q1 padding route, and DEEP-FLAG route play no role in this proof.

## 1. Disk binding and protocol boundary

### 1.1 Primary seals

I read every byte of both commissioned primary objects, decoded all of their UTF-8 text, and read every embedded code listing:

| object | bytes | LF lines | SHA-256 | result |
|---|---:|---:|---|---|
| `circdist/reviews/circdist_cplx_sigma2_rin_exact_review_round83_20260830.md` | 61,080 | 1,036 | `eba3d902f8403a0cffe551624929b8e5f8f4f02bacb1934c05593ebdac8986b3` | exact commissioned Round-83 seal |
| `circdist/artifacts/circdist_cplx_sigma2_r5_deep_seed_round82_20260830.md` | 90,435 | 1,669 | `6994d8a62f38e684cdbdc61cf79b9ce1d64108e07430f19aeb8c952935c418a2` | exact commissioned Round-82 seal |

I treated Round 83's `F83-R82-CLEAR` only as a pointer to earlier material. It is not evidence for the new RIN theorem. Sections 5--8 below are my independent derivation of that theorem.

### 1.2 Complete load-bearing ledger

Every entry below was read in full. YAML objects were parsed, and disk contents control over older reports.

| path | bytes | LF | SHA-256 | use |
|---|---:|---:|---|---|
| `DAG_PROTOCOL.md` | 15,377 | 283 | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` | completion and propagation rules |
| `FILE_PROTOCOL.md` | 8,523 | 166 | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` | canonical/review discipline |
| `operations/circdist/README.md` | 1,507 | 26 | `d4bc4a7415344a1577a45f7277f71eef914f26203dfad5a71ef7065fa2995e12` | operations rules |
| `operations/circdist/SCHEDULER.yaml` | 201,515 | 2,532 | `a465e48bcaf46383a343a2dd68f7bb7324521fdf90691a299422744cd295c1bc` | current Round-84 authorization; expected concurrent drift |
| `circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md` | 10,199 | 243 | `5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64` | frozen problem |
| `circdist/proof-dag/PROJECT.yaml` | 107 | 7 | `c65a2cc0c65576dfdcaf6fbc787762708fe78b8b75daa440765ac08b1ba40d0d` | project root |
| `circdist/proof-dag/nodes/CIRCDIST.cplx.sigma2.yaml` | 3,885 | 48 | `89e2f92228c1a886636b807e8d838c3155d3029b7eca4a8d5cd3ba03dd97c791` | target, currently OPEN |
| `circdist/proof-dag/nodes/CIRCDIST.cplx.upper.yaml` | 5,453 | 80 | `47260df53e4491c86e10f6ccdebadf47b1161d2533339fd9c499f389a8eb2321` | current PROVED membership premise |
| `circdist/reviews/circdist_cplx_upper_membership_exact_review_20260828.md` | 52,336 | 875 | `5e593a927d7ad55966b2362d721f98c7d5dab75c30b334edede81bda4ccbac70` | membership review |
| `circdist/proof-dag/nodes/CIRCDIST.cplx.fixed-d.yaml` | 9,392 | 151 | `024a6d6d7d9a656c5ede53043b64601f13023fe0adbec6fe066ae67fb8303bbf` | current PROVED separate theorem |
| `circdist/reviews/circdist_cplx_fixed_d_private_sentinel_exact_review_20260829.md` | 46,380 | 947 | `e91f7290d5ffab53347fe0bfc477954c087895e133b9234539f120422092cddd` | fixed-\(d\) review, nonpremise |
| `circdist/artifacts/circdist_cplx_fixed_d_x_reduction_round64_20260828/README.md` | 20,689 | 357 | `0606b8b6377fae42a20f606250f7186258cccbd9d04aa7a4ca288cd6371639b5` | fixed-\(d\) input, nonpremise |
| `circdist/artifacts/circdist_cplx_fixed_d_z_companion_round66_20260829/THEOREM.txt` | 1,000 | 1 | `0b184c505c31760d7f333fdba019ea583c7686d55ab5796d126eb0dc2857f6ee` | fixed-\(d\) input, nonpremise |
| `circdist/proof-dag/nodes/CIRCDIST.cplx.yaml` | 7,148 | 123 | `e5fa3667bd9dec3b36f808f927156bd060a8ffcc35ea918ff5e1d353cf558b6a` | parent, currently CONJECTURED |
| `circdist/reviews/circdist_cplx_classification_assembly_exact_review_20260828.md` | 43,304 | 485 | `11340aca2b82c66097af024e6b3b528ea2bc6f75b3306ef965d3b544ce96895f` | PROVED assembly implication only |
| `circdist/artifacts/circdist_cplx_sigma2_20260822.md` | 52,264 | 934 | `b45e9803f717b0572521eda4877d290acec806433e7c16b2b2ef4daec1576e31` | historical route, not used |
| `circdist/artifacts/circdist_cplx_q1_20260822.md` | 40,756 | 770 | `28868e047511c2300356c3e0a15a09a42f422dcef65a056b7ddd2bbb214d2890` | historical route, not used |
| `circdist/artifacts/circdist_cplx_sigma2_covering_radius_primary_source_20260826.md` | 42,975 | 642 | `396216942cc18c2b06e61d7ed9fb220f164d0682d15e5bcf87eb6cfea8fa5958` | historical audit, not used |

The scheduler differs from its Round-82 and Round-83 seals because later review authorization was appended. That is control-plane drift, not corruption. It was never a mathematical premise.

### 1.3 Exact statement bindings

The target claim is the following exact ASCII string, 113 characters and 113 bytes:

> Eff-Preserve with d as part of the input is Sigma_2^P-hard (hence, with CIRCDIST.cplx.upper, Sigma_2^P-complete).

Its normalized SHA-256 is `9e76a1224bea068a1910bdabe189fab022282cca9a2d85df538612db79305a29`.

The licensed new route implication is the following exact 411-character string:

> The normalized grouped QSAT_{2,3DNF} construction, affine-plane/full-kernel fixed-coordinate-RREF bookend compiler, RIN theorem, R_d expansion, and d-by-d grid give a total promise-preserving polynomial-time many-one reduction from QSAT_{2,3DNF} to input-d Eff-Preserve, proving Sigma_2^P-hardness; CIRCDIST.cplx.upper supplies Sigma_2^P membership for the same promise problem, yielding Sigma_2^P-completeness.

Its normalized SHA-256 is `be6890b9433bc9a94eab2d5874556d83b83677635bfdef34e03b46ee3227b53c`.

The current root's already-PROVED classification-assembly implication has 220 characters and normalized SHA-256 `b8b58136bb6b546762020b30cae3595c8fdc9260abd6397c8a2ddc05f23a1a30`. I verified its text, its three premise names, and its current level. It is a later composition input; it does not automatically promote its parent.

## 2. Frozen model reconstructed

Everything is over \(\mathbb F_2\). For CSS matrices \((H_X,H_Z)\), write

\[
 S_X=\operatorname{row}H_X,\quad N_X=\ker H_Z,
 \qquad S_Z=\operatorname{row}H_Z,\quad N_Z=\ker H_X.
\]

The static sector distances are

\[
 d_X=\min\{\operatorname{wt}x:x\in N_X\setminus S_X\},\qquad
 d_Z=\min\{\operatorname{wt}z:z\in N_Z\setminus S_Z\},
\]

and the promised static distance is \(d=\min(d_X,d_Z)\). For a check row with a chosen local CNOT order \((q_1,\ldots,q_w)\), a single ancilla fault produces a singleton or a proper suffix of that ordered support. Thus the indexed catalogue \(\Gamma_X(M)\) (and analogously \(\Gamma_Z(M)\)) contains every physical singleton location and every proper suffix location of every measured row. Two locations remain distinct even when their binary labels coincide.

A multiset is unnecessary: each indexed binary fault variable is used at most once. A fault set is bad in sector \(X\) when the XOR of its catalogue vectors lies in \(N_X\setminus S_X\). Define

\[
 d_{\mathrm{eff}}^X(M)=\min\{|F|:\bigoplus_{f\in F}\gamma_f\in N_X\setminus S_X\},
 \quad d_{\mathrm{eff}}(M)=\min(d_{\mathrm{eff}}^X,d_{\mathrm{eff}}^Z).
\]

Singletons imply \(d_{\mathrm{eff}}(M)\le d\) on a static-distance-\(d\) instance. Therefore preservation is exactly the absence of a bad fault set of cardinality below \(d\) in both sectors.

The optional depth bound \(T\) is absent in this construction. The conflict relation is the frozen derived qubit-sharing relation. Any finite set of local orders has a legal global schedule by serializing all CNOTs, so legality cannot accidentally add a source predicate. The only schedule choices that matter are the two allowed selector-plane orders, one per existential variable.

## 3. Source normalization and grouped representation

### 3.1 Source and total normalization

Use the standard \(\Sigma_2^P\)-complete language

\[
 \mathrm{QSAT}_{2,3\mathrm{DNF}}
 =\{\Phi:\exists x_1\cdots x_p\ \forall y_1\cdots y_q\ \Phi(x,y)\},
\]

where \(\Phi\) is a 3DNF. Put \(\psi=\neg\Phi\), a CNF of width at most three.

Normalization is truth-preserving and polynomial:

1. collapse repeated equal literals within a clause;
2. delete a clause containing both signs of the same variable, because it is tautological in \(\psi\);
3. delete every quantified variable with no remaining occurrence;
4. if some clause becomes empty, \(\psi\equiv0\) and hence \(\Phi\equiv1\);
5. if no clauses remain, \(\psi\equiv1\) and hence \(\Phi\equiv0\).

Steps 1--3 preserve the quantified truth even for multiple existential variables, unused variables, duplicate clauses, and mixed signs. Duplicate clauses may remain; they are separate clause groups and separate indexed planes. The proof never assumes their payload labels differ.

The empty-clause case is a source YES instance and maps to the fixed safe requested-\(d=2\) grid. The no-clause case is source NO and maps to the four-qubit requested-\(d=2\) CSS code

\[
 H_Z=\begin{pmatrix}1&1&1&1\\0&0&1&1\end{pmatrix},\qquad
 H_X=\begin{pmatrix}1&1&1&1\end{pmatrix}.
\]

Use the sole \(X\)-row order \((2,3,0,1)\) and the sole \(Z\)-row orders \((0,1,2,3)\), \((2,3)\). Direct parity enumeration gives \(d_X=d_Z=2\), while the middle \(X\) suffix is the logical vector on \(\{0,1\}\), so \(d_{\mathrm{eff}}^X=1\). Thus the two constants are total promised outputs with the correct yes/no orientation.

### 3.2 Grouped vectors

For a nonconstant normalized formula, let \(m\) be the number of clauses and

\[
 K=p+q+m.
\]

Use marker coordinates \(g_v\) for each retained quantified variable, marker coordinates \(g_j\) for each clause, and an occurrence coordinate \(e_{j,r}\) for each literal position. For a variable \(v\) and bit \(b\), define

\[
 V_{v,b}=g_v+b\sum_{(j,r):v_{j,r}=v} e_{j,r}.
\]

For every assignment \(a\) to the variables in clause \(C_j\) that locally satisfies that clause, define

\[
 A_{j,a}=g_j+\sum_r a(v_{j,r})e_{j,r}.
\]

Set

\[
 \tau=\sum_v g_v+\sum_{j=1}^m g_j.
\]

For a fixed existential schedule assignment \(\alpha\), the abstract catalogue contains only \(V_{x_i,\alpha_i}\) from each existential group; it contains both \(V_{y,0},V_{y,1}\) from each universal group and every emitted locally satisfying \(A_{j,a}\) from each clause group.

### 3.3 Grouped Representation Theorem, rederived

Suppose at most \(K\) available columns XOR to \(\tau\). Every column contains exactly one group marker, while \(\tau\) is one in all \(K\) group coordinates. At least one selected column is required in every group. The budget is therefore tight: exactly \(K\) columns are selected, one in every group.

Let the selected variable value be \(b_v\) and the selected clause assignment be \(a_j\). The target has zero occurrence coordinates, so at every occurrence \((j,r)\),

\[
 b_{v_{j,r}}+a_j(v_{j,r})=0.
\]

The local assignments are consequently restrictions of one global assignment \((\alpha,\beta)\), and every one satisfies its emitted clause. Hence \(\psi(\alpha,\beta)=1\).

Conversely, if a global \((\alpha,\beta)\) satisfies \(\psi\), select its value column in each variable group and its restriction in each clause group. Every group marker appears once and every occurrence bit twice, so these exactly \(K\) columns XOR to \(\tau\). Therefore

\[
 \exists\beta\ \psi(\alpha,\beta)=1
 \iff
 \exists\text{ at most }K\text{ available columns with XOR }\tau.
\]

This argument is insensitive to unused variables already deleted, repeated clauses, identical local option labels in different indexed groups, and any number of existential variables.

### 3.4 Flagged abstraction

Adjoin a flag coordinate \(\ell\) and the sole flag-one abstract anchor

\[
 h=(\tau,1).
\]

All ordinary payloads have flag zero. A set containing the anchor sums to the pure flag \((0,1)\) exactly when its remaining columns sum to \(\tau\). Request

\[
 d_0=K+2.
\]

At the abstract level, a satisfying \(\beta\) produces exactly \(K+1<d_0\) faults. The physical compiler must preserve this dictionary, stabilize every homogeneous payload relation, exclude every unintended indexed equality witness, and meet the two-sector static-distance promise. The following sections verify each requirement.

## 4. Affine planes, full kernel, quotient, and deterministic complement basis

### 4.1 Four-qubit planes and intended hooks

For payloads \(a,b\) and a fresh private coordinate \(p\), use the affine plane

\[
 q_0=p,\quad q_1=p+a,\quad q_2=p+b,\quad q_3=p+a+b.
\]

The four columns XOR to zero. In a selector plane, \((a,b)=(V_{x,0},V_{x,1})\), and two allowed orders select the intended suffix \(V_{x,\alpha}\). In a fixed nonanchor payload plane, put \((a,b)=(a_j,r_j)\), with a new private \(r_j\); the sole order selects \(a_j\). In the anchor plane, put \((a,b)=(h,r_h)\), and its sole order selects \(h\). Every plane has its full four-qubit row as an \(X\) stabilizer.

The physical labels collectively form a matrix \(B\), including all nonflag syndrome rows and the flag row. Let \(S\) be \(B\) with the flag row removed and set

\[
 H_Z=S,\qquad \operatorname{row}H_X=\ker B.
\]

Then \(H_XH_Z^T=0\). Rank-nullity gives

\[
 k=n-\operatorname{rank}H_X-\operatorname{rank}H_Z
   =\operatorname{rank}B-\operatorname{rank}S\in\{0,1\}.
\]

On every nonconstant instance the pure flag row is independent, so \(k=1\). For any physical \(X\) vector \(z\),

\[
 z\in N_X\setminus S_X \iff Bz=(0,1).
\]

Thus the label equation is exactly the unique logical quotient, not merely a sufficient logical test. The nontrivial \(Z\) coset is the flag row modulo \(\operatorname{row}S\). This base code can have \(d_Z=2\), which is why the later cluster expansion is required.

### 4.2 Why the full kernel is generated by the frozen basis

For selector \(i\), define

\[
 \delta_i=V_{x_i,0}+V_{x_i,1}
\]

and physically lift it with the pair \(\{q_0,q_3\}\). Both endpoints have zero group marker. For each fixed nonanchor plane \(j\), orient

\[
 u_j=q_0=p_j,\qquad v_j=q_1=p_j+a_j.
\]

The pair \(\{u_j,v_j\}\) has label \(a_j\). The anchor coefficient is zero in every homogeneous relation because the anchor is the only source of the flag bit.

Let \(D\) have, in order, the selector-difference columns \(\delta_i\), all fixed nonanchor payload columns \(a_j\) in the frozen group/option order, and the anchor bookkeeping column last. Let

\[
 R=\ker D.
\]

Projection \(R\to\) fixed-payload coordinates is injective. Indeed, if every fixed coefficient is zero, the relation is a sum of selector differences. The occurrence support of \(\delta_i\) is the nonempty occurrence set of retained \(x_i\); those supports are pairwise disjoint for distinct variables. Each selector coefficient must therefore vanish. This also explains why deleting unused existential variables in normalization is load-bearing.

Start with any computed basis of \(R\), then deterministically RREF it using only fixed coordinates, left to right in the frozen order. Injectivity gives one fixed pivot for every row. Each output row has the form

\[
 r_i=e_{p_i}+\sum_{j\in S_i}e_j,
\]

where pivot \(p_i\) is absent from every other basis row. The choice is deterministic even with pivot collisions in the unreduced input basis: ordinary RREF resolves them, and injectivity prevents a row without a fixed pivot.

The local four-plane rows plus the physical pair lifts of these \(r_i\) span exactly \(\ker B\). To see this directly, a plane-private \(p\) coordinate forces even parity within its plane. Modulo the full-plane row, a fixed plane has two pair directions; its private \(r_j\) kills the wrong direction and leaves \(\{q_0,q_1\}\), labeled \(a_j\). In a selector plane, zero group marker forces equal coefficients on its two payload directions and leaves \(\{q_0,q_3\}\), labeled \(\delta_i\). The flag kills the anchor coefficient. The remaining coefficient vector is precisely a member of \(\ker D\). The converse lift is immediate.

### 4.3 Static \(X\) distance

Private \(p\) parity forces an even number of physical qubits in every plane. In a fixed plane the additional \(r\) parity identifies the surviving payload-pair coefficient, so each nonzero abstract fixed payload costs at least two physical qubits. The same lower bound holds for a nonzero selector coefficient. A pure flag uses the anchor and has odd group parity in every one of the \(K\) groups, hence at least \(K+1\) nonzero abstract coefficients. Therefore

\[
 d_X\ge 2(K+1)\ge K+2=d_0.
\]

This is truth-independent. Full-kernel stabilization is essential: without it, differences of two grouped witnesses would become additional low-weight logical classes.

## 5. Group-block bookend orders and complete indexed taxonomy

### 5.1 Complement-check order

Lift an RREF row \(r_i\) to a complement \(X\) check and order its physical endpoints as follows:

1. pivot \(u_{p_i}\);
2. all selected selector-pair endpoints and all nonpivot fixed \(u_j\)'s, in the frozen coordinate order;
3. all nonpivot fixed \(v_j\)'s, sorted into contiguous group blocks, with the pivot's group block last;
4. pivot \(v_{p_i}\).

Every endpoint in the first two zones has marker zero. A relation has even fixed-payload parity in every group. Hence the complete late zone has marker zero. Inside a nonpivot group block, a suffix has at most a partial parity in that group, followed by complete even blocks; inside the pivot block, the final pivot endpoint bookends the odd nonpivot parity and again leaves support in at most that group. Consequently every proper complement suffix has group-marker Hamming weight at most one.

This proof depends on group-block contiguity and the pivot bookends, not on a generic increasing-coordinate Gaussian order. It remains valid when two RREF rows share nonpivot planes, when their binary suffix labels coincide, or when a measured row is duplicated: it is a per-indexed-row parity statement.

### 5.2 Raw position table

Fix a schedule \(\alpha\). The table below enumerates all four singleton positions and every proper local suffix, including marker and private-coordinate behavior. Suffixes are displayed by increasing suffix length (one, two, three).

| plane | four singleton labels | three proper suffix labels | marker-one indexed types | marker-zero indexed types |
|---|---|---|---|---|
| selector \(x\) | \(p_x\), \(p_x+a_0\), \(p_x+a_1\), \(p_x+a_0+a_1\) | \(p_x+a_\alpha\), \(a_\alpha\), \(p_x+a_{1-\alpha}\) | the two middle singletons; the intended \(a_\alpha\) suffix; the two \(p_x\)-bearing outer suffixes | first/fourth singletons |
| fixed nonanchor \(j\) | \(p_j\), \(v_j=p_j+a_j\), \(p_j+r_j\), \(v_j+r_j\) | \(v_j\), \(a_j\), \(p_j+r_j\) | local \(v_j\) occurrences, intended \(a_j\), singleton \(v_j+r_j\) | \(p_j\), \(p_j+r_j\), and their suffix/singleton occurrences |
| anchor | \(p\), \(p+h\), \(p+r\), \(p+r+h\) | \(p+h\), \(h\), \(p+r\) | every flag-one location has marker \(\tau\): all indexed \(p+h\), \(p+r+h\), and \(h\) types | every flag-zero anchor location |

Here \(v_j=p_j+a_j\). Equal vector labels in a singleton and a suffix remain separate indexed locations; the classification is by raw position, not by deduplicated label.

Complement rows add the following exhaustive suffix families:

| start region | exact suffix form | marker weight | forbidden content |
|---|---|---:|---|
| any early selector/\(u\) position | an early partial tail plus the complete late zone | 0 | none needed; zero slack later excludes it |
| late fixed-\(v\) zone | \(\bigoplus_{j\in J}v_j\) for the remaining indexed endpoints \(J\) | 0 or 1 | no selector endpoint, no \(r_j\), no anchor endpoint |

Therefore every marker-one complement suffix starts strictly in the late fixed-\(v\) zone and has the exact form

\[
 \lambda(f)=\bigoplus_{j\in J_f}v_j
            =\bigoplus_{j\in J_f}(p_j+a_j).
\]

It is not merely congruent to this expression modulo stabilizers. It is its raw physical XOR label. Selector endpoints occur only in the early marker-zero zone; \(r_j\) endpoints are never used in complement lifts; the anchor never occurs in a homogeneous complement row.

Together with physical singletons, the selector/fixed/anchor local suffixes and both complement-suffix regions exhaust \(\Gamma_X(M)\). No later proof silently replaces indexed locations by unique labels.

## 6. Sharp \(K+1\) lower bound and zero slack

Consider a physical fault set whose label is the pure flag. Let \(t\) be its number of flag-one faults. Only anchor-plane indexed locations carry flag, so \(t\) is odd. Every such location has group projection \(\tau\), hence their aggregate group projection is \(\tau\). The final pure flag has group projection zero, so all flag-zero faults must XOR to \(\tau\), which has marker weight \(K\).

Every flag-zero catalogue location has marker weight at most one: this is immediate from the local table and was proved for every complement suffix. At least \(K\) flag-zero faults are necessary, while \(t\ge1\). Thus

\[
 |F|\ge K+1.
\]

The bound is sharp whenever a satisfying grouped representation exists: its \(K\) intended payload hooks plus the anchor hook achieve equality.

Now suppose \(|F|=K+1\). All inequalities above are equalities:

- \(t=1\);
- exactly \(K\) flag-zero faults occur;
- every flag-zero fault has marker weight exactly one;
- the \(K\) unit markers are all distinct, one per group.

The last statement follows because \(K\) unit vectors XOR to the all-one \(K\)-vector only if each coordinate appears exactly once. Every marker-zero location is excluded: inserting one would leave fewer than \(K\) slots for the \(K\) required odd group coordinates. This rules out all marker-zero selector, fixed, anchor, early complement, and late-even-suffix locations at once.

The sole flag-one location must be the private-free anchor hook \(h\). Every indexed \(p+h\) location contains the anchor-private \(p\), and \(p+r+h\) contains \(p\) and \(r\). None of the \(K\) unit-marker nonanchor faults can carry either anchor-private coordinate: complement rows exclude the anchor and every other plane has disjoint private coordinates. A marker-zero anchor fault that could cancel them is forbidden by zero slack. Hence the only surviving flag-one raw position is the length-two suffix \(h\).

This proves the lower bound and its full equality structure before invoking RIN.

## Finding F84-RIN

### 7. Exact RIN theorem

**Theorem F84-RIN (freshly PROVED).** For every normalized nonconstant QSAT formula, every existential schedule \(\alpha\), and the frozen affine-plane/full-kernel compiler with its deterministic fixed-coordinate RREF basis and group-block bookend orders, every indexed \(K\)-fault nonanchor equality solution consists exactly of the scheduled existential hook in each existential group, one intended value hook in every universal group, and one intended locally satisfying option hook in every clause group. Consequently such a solution exists if and only if there is one global \(\beta\) with \(\psi(\alpha,\beta)=1\).

### 7.1 Selector exclusion

Remove the already-forced anchor hook. Exactly \(K\) unit-marker faults remain, one per distinct group.

In selector plane \(x\), every marker-one nonintended singleton or suffix carries its unique private coordinate \(p_x\). The only marker-one selector location without \(p_x\) is the scheduled intended suffix \(a_\alpha\). No marker-one complement suffix contains any selector endpoint, no other plane contains \(p_x\), and only one fault can be chosen in group \(x\). Therefore a broken selector entry has no cancellation source. Every existential group must use its intended scheduled hook.

This argument covers both schedule values, all four selector singletons, all three proper selector suffixes, multiple existential variables, and any RREF pivot pattern.

### 7.2 Fixed \(r_j\) exclusion

For a fixed nonanchor plane, the only unit-marker type containing \(r_j\) is the singleton \(v_j+r_j\). The other local \(r_j\)-bearing locations have marker zero and were eliminated by zero slack. Complement suffixes contain only \(v\)'s and never \(r\)'s. No other plane has this private \(r_j\). Hence \(v_j+r_j\) cannot occur.

After this step, every remaining nonintended fixed-group fault is either a local indexed \(v_j\) or a marker-one complement suffix \(\bigoplus_{j\in J_f}v_j\).

### 7.3 Entire-\(v_j\) parity, including payload

Let \(N\) be the set of those remaining nonintended faults. For a local \(v_j\), take \(J_f=\{j\}\); for a complement suffix use its exact late-zone endpoint set. In all cases

\[
 \lambda(f)=\bigoplus_{j\in J_f}v_j
           =\bigoplus_{j\in J_f}(p_j+a_j).
\]

The anchor hook, intended selector hooks, and intended fixed hooks contain no fixed private \(p_j\). Because the total residual label is zero, each independent \(p_j\) coordinate gives

\[
 \bigoplus_{f\in N}\mathbf 1[j\in J_f]=0. \tag{7.1}
\]

Equation (7.1) is the coefficient of the *whole vector* \(v_j=p_j+a_j\), not only its private part. Consequently every entire \(v_j\), including all occurrence and group payload carried by \(a_j\), has even coefficient in the XOR over \(N\). Therefore

\[
 \bigoplus_{f\in N}\lambda(f)=0. \tag{7.2}
\]

This is the critical cross-row cancellation statement. Shared nonpivot planes merely contribute to the same parity equation. Repeated complement rows, different suffixes with the same \(J_f\), duplicate labels, and arbitrary cancellation between rows are counted correctly modulo two. A single indexed location cannot be selected twice, while distinct locations are separate Boolean terms in (7.1).

### 7.4 Distinct group markers force \(N=\varnothing\)

Every fault in \(N\) has one unit group marker. Equality has selected one fault per group, so these markers are distinct standard basis vectors. Projecting (7.2) to marker coordinates gives

\[
 \bigoplus_{f\in N}g_{G(f)}=0.
\]

A nonempty subset of distinct standard basis vectors cannot XOR to zero. Hence \(N=\varnothing\). This conclusion is stronger than a normalization lemma: no replacement is required because no nonintended indexed fault survives.

### 7.5 Global assignment and clause satisfaction

All remaining faults are intended. Each universal group selects exactly one value hook and thereby defines \(\beta_y\). Each clause group selects one emitted locally satisfying assignment \(a_j\). Since the aggregate of the \(K\) intended hooks is \(\tau\), every occurrence coordinate has parity zero:

\[
 \beta_{v_{j,r}}+a_j(v_{j,r})=0,
\]

with \(\alpha\) used for existential occurrences. Thus all clause options are restrictions of the same global \((\alpha,\beta)\), and each satisfies its clause. Therefore \(\psi(\alpha,\beta)=1\).

Conversely, any satisfying \((\alpha,\beta)\) chooses the intended selector hooks, universal-value hooks, and satisfying clause restrictions; these \(K\) labels XOR to \(\tau\). This completes both directions of F84-RIN.

### 7.6 Explicit adversarial coverage of the theorem

The proof above directly resolves all attacks requested for this review:

| attack | reason it cannot evade the proof |
|---|---|
| odd XOR of several satisfying options counterfeits a falsifying option | equality permits one indexed fault per group; any such mixture arising through complement suffixes lies in \(N\) and is killed by private-\(p_j\) parity plus distinct markers |
| multiple existential variables | every selector has a disjoint private \(p_x\); each broken selector is excluded independently |
| RREF pivot collisions | deterministic fixed-coordinate RREF gives distinct pivots; the proof uses only the resulting pivot uniqueness and bookend marker bound |
| unused variables | normalization deletes them; injectivity uses the nonempty disjoint occurrence supports of retained existentials |
| constants | handled before the compiler by two fixed promised outputs |
| duplicate clauses or options | clause groups and fault positions remain indexed; occurrence parity gives global consistency without requiring unique labels |
| repeated indexed suffix labels | equations (7.1)--(7.2) count indexed Boolean selections; equal labels do not collapse positions |
| repeated or duplicated complement rows | every selected suffix still has an exact \(J_f\), and parity is taken across all indexed rows |
| shared nonpivot planes and cross-row cancellation | the private coordinate \(p_j\) records the total parity of the entire \(v_j\) across all rows |
| anchor alternatives | zero slack excludes marker-zero anchor locations; anchor-private \(p,r\) exclude all flag-one alternatives except \(h\) |

Finite programs in section 14 corroborate these cases but are not premises of this proof.

## 8. Both truth directions and the total Karp map

Fix a nonconstant normalized input and schedule \(\alpha\).

**If there is a falsifying universal assignment.** If \(\psi(\alpha,\beta)=1\), choose the intended scheduled hook in every existential group, the \(\beta\)-value hook in every universal group, the restriction of \((\alpha,\beta)\) in every clause group, and the anchor hook. The \(K\) nonanchor labels XOR to \(\tau\); adding \(h=(\tau,1)\) yields the pure flag. It uses exactly

\[
 K+1<d_0=K+2
\]

indexed faults, so the schedule is unsafe.

**If the schedule is unsafe.** A bad mechanism below \(d_0\) has at most \(K+1\) faults. The sharp lower bound gives at least \(K+1\), so it is an equality mechanism. Zero slack forces the private-free anchor hook and one distinct unit-marker nonanchor fault per group. F84-RIN forces all of them to be intended and yields a single \(\beta\) with \(\psi(\alpha,\beta)=1\).

Therefore

\[
 \begin{aligned}
  \text{flagged schedule }\alpha\text{ unsafe below }d_0
   &\iff \exists\beta\;\psi(\alpha,\beta)=1,\\
  \text{flagged schedule }\alpha\text{ safe below }d_0
   &\iff \forall\beta\;\Phi(\alpha,\beta)=1.
 \end{aligned}
\]

The selector-plane local-order choice is a one-to-one dictionary with \(\alpha\); all other local orders are emitted as singletons. Hence

\[
 \exists\text{ safe output schedule}
 \iff \exists\alpha\ \forall\beta\;\Phi(\alpha,\beta)=1.
\]

The constant preprocessing from section 3.1 preserves this equivalence on every syntactic input, so the map is total. There is no appeal to a promise on the source syntax beyond the standard QSAT encoding.

## 9. Cluster expansion, multi-fault \(Z\) audit, and exact promise

### 9.1 Algebraic cluster expansion \(R_R\)

Replace each old qubit \(q\) by \((q,0),\ldots,(q,R-1)\). Add the \(X\) equality rows

\[
 e_{(q,j)}+e_{(q,j+1)}\qquad(0\le j<R-1),
\]

lift every old \(X\) row to layer zero, and replace every old \(Z\) row \(z\) by \(z\otimes\mathbf1_R\). Equality rows commute with repeated \(Z\) rows, and lifted \(X\) rows commute by the old CSS relation. The ranks are

\[
 \operatorname{rank}H_X^{(R)}=n(R-1)+\operatorname{rank}H_X,qquad
 \operatorname{rank}H_Z^{(R)}=\operatorname{rank}H_Z,
\]

so \(k\) is preserved.

For an \(X\) vector, take parity within every copy cluster. Equality stabilizers move its class to layer zero, and lifted old stabilizers act exactly as before. Thus both the quotient and its minimum physical weight are preserved:

\[
 d_X^{(R)}=d_X.
\]

The same map applies to indexed faults. Each new equality-row suffix is a singleton, equivalent to a layer-zero singleton. Every lifted old-row suffix is exactly its old suffix in layer zero. Projection cannot increase fault count, and lifting an old witness preserves it, so

\[
 d_{\mathrm{eff}}^{X,(R)}=d_{\mathrm{eff}}^X.
\]

For \(Z\), equality normalizer equations force a normalizer to be constant through every cluster: \(z\otimes\mathbf1_R\). Repeated old \(Z\) rows identify exactly the old stabilizer cosets. Therefore

\[
 d_Z^{(R)}=R,d_Z.
\]

### 9.2 Layer-major suffixes, including combinations

Order each repeated \(Z\) row layer-major: all support positions in layer 0, then all in layer 1, and so forth. Let

\[
 Q=\mathbb F_2^n/\operatorname{row}H_Z
\]

for the old code. A proper suffix of a repeated row contains a partial old row in at most one current layer plus complete copies of that old row in every later layer. Each complete row is zero in \(Q\). A physical singleton is also nonzero in at most its own layer. Hence **every one indexed \(Z\) fault has a possibly nonzero \(Q\)-class in at most one layer**.

This statement is additive and therefore covers arbitrary combinations of singletons and suffixes from different checks, not only one hook. A nontrivial expanded \(Z\) logical is \(z\otimes\mathbf1_R\) with the same nonzero class \([z]\in Q\) in all \(R\) layers. The XOR of \(t<R\) indexed faults can have nonzero quotient class in at most \(t\) layers, so it cannot equal a nontrivial logical class. Thus

\[
 d_{\mathrm{eff}}^{Z,(R)}\ge R.
\]

My independent exhaustive multi-fault checker in section 14 enumerated all indexed subsets of size below \(R\) for 116 small nontrivial CSS row-space pairs and found no violation; the proof above, rather than that finite result, establishes the general claim.

### 9.3 Exact \(d\times d\) grid

Begin with \(d\) qubits, no \(X\) rows, and adjacent-pair \(Z\) rows \(e_i+e_{i+1}\). The base has \(k=1\), \(d_X=d\), and \(d_Z=1\). Apply \(R_d\). The resulting \(d\times d\) block has

\[
 d_X=d_Z=d.
\]

Its \(X\) catalogue is singleton-equivalent and requires \(d\) faults for the all-one logical. The layer-major theorem gives \(d_{\mathrm{eff}}^Z\ge d\), while \(d\) singleton faults, one in each layer of a base odd-coset representative, attain equality. Hence

\[
 d_{\mathrm{eff}}^X=d_{\mathrm{eff}}^Z=d.
\]

### 9.4 Direct sum and the exact two-sector promise

Set \(R=d=d_0=K+2\) on the flagged block and direct-sum the exact grid. The expanded flagged block has

\[
 d_X\ge d,qquad d_Z\ge d,qquad
 d_{\mathrm{eff}}^Z\ge d,qquad
 d_{\mathrm{eff}}^X=\text{the base flagged value}.
\]

The grid has both static and effective sector distances exactly \(d\). Static and effective distances of a direct sum are the minima of the component distances: a nontrivial logical has a nontrivial component, and adding support in another component cannot lower its weight or fault cardinality. Consequently the total output satisfies

\[
 d_X^{\rm total}=d_Z^{\rm total}=d
\]

for every source truth value and every schedule. On a safe flagged schedule the total effective distance is exactly \(d\), pinned above and below by the grid; on an unsafe flagged schedule it is \(K+1<d\). There is no cross-block shortcut.

An independent parameter/rank/distance instance check gave, for a representative \(K=2,d=4\) compiler, base \((n,\operatorname{rank}H_X,\operatorname{rank}H_Z,k,d_X,d_Z)=(12,3,8,1,6,2)\); after expansion, \((n,\operatorname{rank}H_X,\operatorname{rank}H_Z,d_X,d_Z)=(48,39,8,6,8)\); the grid and direct sum both had exact sector distances four. The unsafe/safe effective \(X\) values were three/four as predicted.

## 10. Schedule legality, computability, and size

Only selector planes have two allowed local orders; choosing them gives exactly \(\alpha\). Fixed planes, anchor plane, RREF complement checks, expansion equality checks, repeated \(Z\) checks, and grid checks have the specified single local order. The construction supplies no optional \(T\). Under the frozen qubit-sharing conflict rule, globally serializing the checks realizes every tuple of local orders. Thus there is no hidden conflict or depth constraint and no loss of schedule assignments.

Let \(s=p+q+m\), so \(K=s\) after normalization. The number of payload planes is at most

\[
 p+2q+7m+1=O(s),
\]

because a width-three nonempty clause has at most seven satisfying local options. The base physical qubit count, label dimension, rank, number of RREF rows, and every base row length are \(O(s)\). Gaussian elimination and fixed-coordinate RREF are deterministic polynomial-time algorithms.

Expansion by \(R=d=O(s)\) and the grid give \(O(s^2)\) output qubits and checks. Counting nonzero support incidences and explicit order entries gives \(O(s^3)\): the dominant objects are \(O(s)\) repeated base \(Z\) rows, each with up to \(O(s^2)\) layer-expanded support. If every matrix is serialized densely, \(O(s^2)\) rows by \(O(s^2)\) columns require at most \(O(s^4)\) bits. Sparse integer indices add at most a logarithmic serialization factor, still polynomial. The prior claim that dense encoding was cubic is false and is repaired here; no complexity conclusion depended on the smaller exponent.

Every source transformation, payload enumeration, matrix construction, RREF pivot choice, local order, direct sum, and requested integer is explicitly writable in polynomial time. The output distance promise is proved structurally and is not checked by solving a hard distance problem.

## Finding F84-ROUTE

The exact 411-character `grouped-qsat-affine-rin` implication bound in section 1.3 is **PROVED by fresh independent review**. The proof comprises:

- total QSAT normalization and fixed promised constants;
- exact grouped representation and schedule-to-\(\alpha\) dictionary;
- affine-plane realization and full physical-kernel quotient;
- deterministic fixed-coordinate RREF plus group-block bookend marker bound;
- the sharp \(K+1\) equality analysis and F84-RIN;
- both truth directions;
- \(R_d\) preservation and layer-major multi-fault \(Z\) lower bound;
- exact grid/direct-sum promise in both static sectors;
- frozen legality and corrected polynomial output size.

The sole logical premise listed in the canonical route is current-PROVED `CIRCDIST.cplx.upper`, used only for the completeness conclusion. The hardness construction does not consume `CIRCDIST.cplx.fixed-d` or any historical alternative route.

## Finding F84-SIGMA2

The unchanged 113-character `CIRCDIST.cplx.sigma2` claim bound in section 1.3 is **PROVED by fresh independent review**. The reduction proves its hardness clause. The current exact `CIRCDIST.cplx.upper` node and its independent review supply \(\Sigma_2^P\) membership for input-\(d\) Eff-Preserve with the same promise convention, making the parenthetical \(\Sigma_2^P\)-completeness statement valid.

No parent propagation is licensed. `CIRCDIST.cplx` remains CONJECTURED on current disk even though its classification-assembly route is PROVED and, after applying this delta, its three premises would all be PROVED. A later root review must recheck and license that composition.

## 11. Adversarial decision trail and checker findings

I began with the two steps most likely to conceal a shortcut:

1. a complement suffix might carry a selector endpoint or a mixture of fixed payloads whose private parts cancel while their payload parts do not;
2. distinct RREF rows might share nonpivot planes, allowing cross-row cancellation of nonintended suffixes even though each row separately has the marker bound.

The raw-position table resolved the first: marker-one complement suffixes start strictly in the late \(v\) zone. The independent equality search and the symbolic entire-\(v_j\) parity argument resolved the second. There was no theorem repair and no counterexample.

I explicitly attacked formulas with odd XORs of multiple allowed options, repeated wide clauses, duplicate option labels, two existential variables, mixed literal signs, shared nonpivot planes, pivot competition, unused variables, syntactic constants, and duplicated complement rows. Two deliberately duplicated-row controls increased the indexed catalogue but produced no nonintended equality solution. The result follows algebraically because duplication changes the number of indexed terms, not the independent private-coordinate parity or the distinct-group-marker conclusion.

There were three nonmathematical issues during checking:

- the first scratch taxonomy run reversed the intended length-one/length-three suffix lookup in the reviewer program;
- the second scratch taxonomy run compared a tuple group key with a string;
- an overbroad \(v=4,e=2,m=4\) exploratory equality search reached its declared resource cap after 56,338,696 states and approximately 8.46 GB RSS, with no candidate and no verdict.

I repaired only scratch code, reran bounded exhaustive and targeted controls, and did not use the capped run as evidence. All final programs compiled and exited zero.

## 12. Licensed and nonlicensed state changes

| object/action | licensed? | exact scope |
|---|---|---|
| add route `grouped-qsat-affine-rin` to `CIRCDIST.cplx.sigma2` | yes | exact implication hash `sha256:be6890b9433bc9a94eab2d5874556d83b83677635bfdef34e03b46ee3227b53c` |
| route assessment `OPEN -> PROVED` | yes | based on `Finding F84-ROUTE` |
| node `CIRCDIST.cplx.sigma2` `OPEN -> PROVED` | yes | unchanged claim hash `sha256:9e76a1224bea068a1910bdabe189fab022282cca9a2d85df538612db79305a29` |
| remove sigma2 frontier after completion | yes | replacement YAML records complete basis and caveats |
| append Round-82/Round-83 evidence and Round-84 events | yes | historical entries retained; new entries append provenance |
| regenerate derived sigma2 views | later canonical operation | mechanical consequence after applying the node delta |
| settle scheduler task | later canonical operation | operations bookkeeping after canonical mutation |
| promote `CIRCDIST.cplx` root | **no** | requires a later fresh composition review |
| inherit fixed-\(d\), covering-radius, Q1, or DEEP-FLAG proof | **no** | these are explicitly not premises |
| change frozen model, optional-\(T\), or conflict convention | **no** | theorem is scoped to the unchanged frozen definition |

## 13. Sole precise licensed canonical delta

The complete licensed replacement for `circdist/proof-dag/nodes/CIRCDIST.cplx.sigma2.yaml` follows. It preserves the claim byte-for-byte, retains historical evidence and the prior covering-radius audit event, appends the new direct route/evidence/events, removes the completed frontier, and does not touch the root node.

```yaml
id: CIRCDIST.cplx.sigma2
role: proof
aliases:
- EFFP-SIGMA2
claim: Eff-Preserve with d as part of the input is Sigma_2^P-hard (hence, with CIRCDIST.cplx.upper, Sigma_2^P-complete).
routes:
  grouped-qsat-affine-rin:
    premises:
    - CIRCDIST.cplx.upper
    assumptions:
      qsat2-3dnf-completeness:
        kind: external-theorem
        statement: The language of 3DNF formulas Phi with prefix exists x forall y is Sigma_2^P-complete under polynomial-time many-one reductions; equivalently this is obtained by complementing the standard Pi_2^P-complete forall-exists 3CNF quantified-Boolean-formula language.
        source:
          path: circdist/artifacts/circdist_cplx_sigma2_r5_deep_seed_round82_20260830.md
          kind: text
          locator: Section 3.1, standard QSAT_{2,3DNF} source form
    implication: >-
      The normalized grouped QSAT_{2,3DNF} construction, affine-plane/full-kernel fixed-coordinate-RREF bookend compiler, RIN theorem, R_d expansion, and d-by-d grid give a total promise-preserving polynomial-time many-one reduction from QSAT_{2,3DNF} to input-d Eff-Preserve, proving Sigma_2^P-hardness; CIRCDIST.cplx.upper supplies Sigma_2^P membership for the same promise problem, yielding Sigma_2^P-completeness.
    proof:
      sketch: >-
        Normalize the negated 3DNF matrix to a nonconstant width-at-most-three CNF, with fixed promised outputs for the two constant cases. Group markers force any target representation of weight at most K to choose exactly one variable value and one locally satisfying option per clause. A selectable affine plane makes the schedule choose each existential value; fixed planes realize every universal value, clause option and the flagged anchor. Stabilizing the full physical label kernel with the deterministic fixed-coordinate RREF complement basis gives the exact one-logical-qubit quotient. Group-block bookend orders make every nonanchor indexed fault carry marker weight at most one, so every pure-flag mechanism has at least K+1 faults. At equality, the sole flag fault is the private-free anchor hook; selector private coordinates exclude broken selector entries; fixed r coordinates exclude v_j+r_j; and fixed p_j parity cancels every entire v_j=p_j+a_j contributed by local or complement suffix faults. Their distinct group markers then force the nonintended set empty. The surviving intended hooks give one global satisfying beta by occurrence parity. Thus a schedule alpha is safe below d=K+2 exactly when forall beta Phi(alpha,beta). Cluster expansion R_d preserves the X problem, raises static and effective Z distance to at least d, and a direct-summed d-by-d grid pins both static sector distances and the safe effective distance to exactly d. With no optional depth bound, serialization makes every emitted local-order tuple legal under qubit-sharing conflicts. The construction is total and polynomial: O(s^3) sparse support incidences and at most O(s^4) dense matrix bits.
      sources:
      - path: circdist/artifacts/circdist_cplx_sigma2_r5_deep_seed_round82_20260830.md
        kind: text
        locator: Sections 3-9 and embedded exact harnesses
      - path: circdist/reviews/circdist_cplx_sigma2_rin_exact_review_round83_20260830.md
        kind: text
        locator: F83-R82-CLEAR, F83-RIN-NEW, F83-SIZE-REPAIR
      - path: circdist/reviews/circdist_cplx_sigma2_rin_final_exact_review_round84_20260830.md
        kind: review
        locator: Finding F84-ROUTE
    assessment:
      level: PROVED
      caveats:
      - PROVED is bound to the unchanged 411-character implication at sha256:be6890b9433bc9a94eab2d5874556d83b83677635bfdef34e03b46ee3227b53c and consumes the current PROVED CIRCDIST.cplx.upper premise under the same frozen Eff-Preserve promise and reduction convention.
      - The hardness proof is the direct grouped-QSAT/affine-full-kernel/RIN route. It does not inherit from CIRCDIST.cplx.fixed-d and does not use the historical covering-radius, Q1 padding or DEEP-FLAG routes.
      - The output uses the ordinary qubit-sharing conflict relation and no optional depth bound T. Sparse support-list incidence count is O(s^3), while a dense explicit matrix encoding is at worst O(s^4); either encoding is polynomial.
      - This route proves only CIRCDIST.cplx.sigma2. The CIRCDIST.cplx root requires a later fresh composition review even though its classification-assembly implication and all three premise nodes are then PROVED.
      summary: Fresh strict-serial round-84 review independently rederived the complete indexed fault taxonomy, sharp K+1 bound, zero-slack RIN theorem, both reduction directions, total normalization and constants, full-kernel quotient, R_d two-sector repair, exact grid/direct-sum promise, legality and polynomial output size. The exact conditional implication and its current upper premise entail the unchanged sigma2 claim.
      basis:
        reviews:
        - path: circdist/reviews/circdist_cplx_sigma2_rin_final_exact_review_round84_20260830.md
          kind: review
          scope: Fresh independent exact review of the full grouped-QSAT reduction and every indexed singleton/local/complement suffix family, including RREF pivots, group-block orders, sharp zero slack, all private-coordinate exclusions and cross-row cancellation, repeated labels/rows, both truth directions, constants, normalization, quotient/rank/static sectors, R_d layer-major multi-fault Z behavior, exact grid/direct sum, schedule legality, totality and corrected sparse/dense size.
          locator: Finding F84-ROUTE
          reviewed_hash: sha256:be6890b9433bc9a94eab2d5874556d83b83677635bfdef34e03b46ee3227b53c
assessment:
  level: PROVED
  caveats:
  - PROVED is bound to the unchanged 113-character claim at sha256:9e76a1224bea068a1910bdabe189fab022282cca9a2d85df538612db79305a29 and to route grouped-qsat-affine-rin at implication hash sha256:be6890b9433bc9a94eab2d5874556d83b83677635bfdef34e03b46ee3227b53c.
  - The theorem concerns input-d Eff-Preserve in the frozen single-ancilla terminal-residual model, with ordinary qubit-sharing conflicts and total promise-preserving polynomial-time many-one reductions. It proves no Circ-Preserve or arbitrary-conflict-graph variant.
  - The direct proof bypasses covering radius, Q1 repetition padding, DEEP-FLAG and the fixed-d theorem. Those historical paths are neither premises nor inherited evidence.
  - The parenthetical completeness conclusion uses the independently PROVED CIRCDIST.cplx.upper membership claim. No CIRCDIST.cplx root promotion is licensed without a separate fresh review of the assembled parent.
  summary: Fresh round-84 review proves the unchanged hierarchy-hardness claim. The direct compiler maps normalized QSAT_{2,3DNF} to promised input-d Eff-Preserve instances, with schedule alpha safe exactly when every beta satisfies Phi; constants, both CSS sectors, exact static distance, legal schedules and polynomial output are total. Together with current PROVED membership, the parenthetical Sigma_2^P-completeness conclusion is valid.
  basis:
    routes:
    - grouped-qsat-affine-rin
    reviews:
    - path: circdist/reviews/circdist_cplx_sigma2_rin_final_exact_review_round84_20260830.md
      kind: review
      scope: Fresh independent exact-claim and assembled-route review, including the new Round-83 RIN theorem, all previously cleared construction components, both Karp directions and current upper-premise composition; excludes root promotion and all historical alternative routes.
      locator: Finding F84-SIGMA2
      reviewed_hash: sha256:9e76a1224bea068a1910bdabe189fab022282cca9a2d85df538612db79305a29
    evidence:
    - path: circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.cplx.sigma2.yaml
      kind: text
      note: Immutable pre-migration record, including every original event, former summary and frontier;
        historical evidence, not an additional completion review.
    - path: circdist/artifacts/circdist_cplx_q1_20260822.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its
        scope.
    - path: circdist/artifacts/circdist_cplx_sigma2_20260822.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its
        scope.
    - path: circdist/artifacts/circdist_cplx_recon_20260820.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its
        scope.
    - path: circdist/artifacts/circdist_cplx_sigma2_covering_radius_primary_source_20260826.md
      kind: text
      note: Round-58 source audit. IEEE publisher metadata and official/peer-reviewed later sources strongly support exact upper-bound binary linear-code covering radius as Π₂^P-complete, but no faithful McLoughlin full text was lawfully accessible on 2026-08-26; exact theorem hypotheses and reduction details remain primary-unverified.
    - path: circdist/artifacts/circdist_cplx_sigma2_r5_deep_seed_round82_20260830.md
      kind: text
      note: Sealed proposer construction supplying the grouped QSAT, affine/full-kernel, R_d, grid and deterministic bookend compiler source.
    - path: circdist/reviews/circdist_cplx_sigma2_rin_exact_review_round83_20260830.md
      kind: text
      note: Independent clearance of unchanged Round-82 components and public author source for F83-RIN-NEW; not by itself the independent review of that new theorem.
events:
  covering-radius-primary-source-audit-access-blocked-2026-08-26:
    date: '2026-08-26'
    type: repair-applied
    summary: Round-58 strict-serial source audit located the stable IEEE DOI record and publisher abstract and cross-checked an official GMR journal PDF plus later sources. The evidence strongly supports the standard exact upper-bound binary linear-code covering-radius Π₂^P-completeness attribution, with Σ₂^P-complete lower-bound complement, but no faithful McLoughlin full text was lawfully accessible. Exact theorem hypotheses and the reported Π₂-SAT/AE-3DM Karp chain remain primary-unverified; task-001 is retained. This source audit proves no Eff-Preserve reduction, no DEEP-FLAG result, and no level change.
    sources:
    - path: circdist/artifacts/circdist_cplx_sigma2_covering_radius_primary_source_20260826.md
      kind: text
      locator: Primary-source verdict; exact derivation; GMR cross-check; dispatcher installation contract
  sigma2-grouped-qsat-route-added-round84-2026-08-30:
    date: '2026-08-30'
    type: route-added
    route: grouped-qsat-affine-rin
    summary: Registered the direct grouped-QSAT/affine-full-kernel/RIN route with CIRCDIST.cplx.upper as its sole premise. The route bypasses the covering-radius, Q1 padding, DEEP-FLAG and fixed-d paths.
    sources:
    - path: circdist/artifacts/circdist_cplx_sigma2_r5_deep_seed_round82_20260830.md
      kind: text
    - path: circdist/reviews/circdist_cplx_sigma2_rin_exact_review_round83_20260830.md
      kind: text
      locator: F83-RIN-NEW
    - path: circdist/reviews/circdist_cplx_sigma2_rin_final_exact_review_round84_20260830.md
      kind: review
      locator: Finding F84-ROUTE
  sigma2-rin-final-reviewed-round84-2026-08-30:
    date: '2026-08-30'
    type: review-completed
    route: grouped-qsat-affine-rin
    summary: Fresh strict-serial round-84 review independently proved the Round-83 RIN theorem and rechecked the entire total promise-preserving reduction, both sectors, exact promise, legality, size and current-claim entailment.
    sources:
    - path: circdist/reviews/circdist_cplx_sigma2_rin_final_exact_review_round84_20260830.md
      kind: review
      locator: Finding F84-ROUTE
  sigma2-grouped-qsat-route-proved-round84-2026-08-30:
    date: '2026-08-30'
    type: level-change
    route: grouped-qsat-affine-rin
    from: OPEN
    to: PROVED
    summary: Promoted the exact 411-character direct route implication after the proposer construction, public RIN proof and fresh independent final review completed every load-bearing step.
    sources:
    - path: circdist/reviews/circdist_cplx_sigma2_rin_final_exact_review_round84_20260830.md
      kind: review
      locator: Finding F84-ROUTE
  sigma2-proved-round84-2026-08-30:
    date: '2026-08-30'
    type: level-change
    from: OPEN
    to: PROVED
    summary: Promoted only CIRCDIST.cplx.sigma2 after the direct hierarchy-hardness route and current PROVED upper premise entailed the unchanged claim. CIRCDIST.cplx remains CONJECTURED pending its own fresh composition review; no parent level is inherited.
    sources:
    - path: circdist/reviews/circdist_cplx_sigma2_rin_final_exact_review_round84_20260830.md
      kind: review
      locator: Finding F84-SIGMA2
```

## 14. Reproducible validation

### 14.1 Sealed Round-82 harness extraction and replay

I extracted the seven fenced Python listings from the exact Round-82 artifact by bounded section spans. Every extracted byte hash matched the published source seal, and every file compiled with `python3 -m py_compile`.

| listing | bytes | LF | SHA-256 |
|---|---:|---:|---|
| `abstract_census.py` | 3,958 | 109 | `4e6c8ebb42213781cbb3918cc344896ce696843cd7ad91d5e45d301430a65a7d` |
| `plane_gate.py` | 4,446 | 112 | `3db3a931ca6c8e58e34fdb42ef1e788be4d4ff4b19ebb47ab6c571c3807df182` |
| `compiler_audit.py` | 6,616 | 177 | `d090a4682ea3f23e756deb40ee4ee681ae0c5b82626c5de16498851e2e987dd1` |
| `grid_block_audit.py` | 1,711 | 57 | `106e7a3eaf6fa3da81d014da104288a2dfee3a079dd3b867603f2023b1333bb1` |
| `rin_xor_csp_search.py` | 13,171 | 303 | `ef80e03c9bcd49edecef30400bd08bbe745aa02984a713ef638fa0e653643cc4` |
| `kernel_shortcut_witness.py` | 5,200 | 145 | `465623e89e53e4f6f2c583d1867b6688e7e4982908741c5f1bdc3ad04d36ad2d` |
| `constant_instance_audit.py` | 864 | 29 | `5d0628b72f4e43b12bfddd360d7a98f099dbdff7e8dc26bbe0b9c0d780b472e5` |

All serial runs exited zero. The deterministic outputs and exact current hashes were:

| output | bytes | SHA-256 | semantic result |
|---|---:|---|---|
| `abstract_census.out` | 221 | `4e41f9f2a9aab2a73c84e0366abb3c91628717d8c7a6fec2b16dfaf595ffaf55` | exact sealed output |
| `plane_gate.out` | 611 | `4f52bdf05928cffaad1d627566efb387f19ee00ac7adf1856ed5a3406333b1c1` | exact sealed output |
| `compiler_audit.out` | 1,141 | `829599ef115ddfc4a1fa28b9db9650a784f43652a313abe91c2d6b78a2868671` | exact sealed output |
| `grid_block_audit.out` | 818 | `0faff3eea85e529322b9f8d384449a420ccf08b40e2984b8778d35eea981c7b5` | exact sealed output |
| `constant_instance_audit.out` | 112 | `21778d05637f97afe3ef56e6ac3b828dcdbc6dbf1d23570b485b8ef6e73c03b8` | exact sealed output |
| `kernel_shortcut_witness.out` | 6,523 | `8ebcac52bb04855a14d937c336ff3bc442325705be9d581e0e5d8d6c10977c8c` | exact sealed output |
| RIN v2/m2 | 172 | `53eea3f5ccde44cd3d9eaf908ad254a1b56f8c293f839ea3f28a032adb264718` | no counterexample |
| RIN v2/m3 | 176 | `6388d0d08032b8b8ea8753b2dc785967017e3e0d58faa7da2af3d48d35146ab2` | no counterexample |
| RIN v2/m4 | 182 | `7fab68b2fcb6242c0b1d985550ae55e5f74814e08ebb56b0ebb692c9ecf50c82` | no counterexample |
| RIN v3/m2 | 173 | `13adf4c15398d2d3dac6c746ba6ddc158e5cdecf3097059b79d8e67bb866b358` | no counterexample |

The RIN program includes terminal wall-clock text in stdout. Removing only ` elapsed=<decimal>` gives semantic SHA-256 values, respectively,

- `3d7a27ce8fc738cf86a1f84beb533e6a4b74e0be093e7f3ea4434129d3847a83`,
- `175419a9b70d4236f161d9da317e89928cc542187b8d3642fb1a3a7c295a6e2e`,
- `b4855df564d63c482469c6cdc1e313ecf782a7babb5fb5eb420a66c51d2b85ab`,
- `1ef1b5b1234fedfc59e86fe2cfde7d05362b41b28afde1219c1b74ddcaf08f98`.

All four match the semantic projections recorded by Round 83. Variation in exact stdout is exclusively the nondeterministic elapsed field. This is the low-severity seal/reporting repair described in the verdict.

Representative replay commands, run from the scratch extraction directory, were:

```sh
python3 -m py_compile harnesses/*.py
python3 harnesses/abstract_census.py > abstract_census.out
python3 harnesses/plane_gate.py > plane_gate.out
python3 harnesses/compiler_audit.py > compiler_audit.out
python3 harnesses/grid_block_audit.py > grid_block_audit.out
python3 harnesses/kernel_shortcut_witness.py > kernel_shortcut_witness.out
python3 harnesses/constant_instance_audit.py > constant_instance_audit.out
python3 harnesses/rin_xor_csp_search.py --variables 2 --exists 1 --clauses 2 --width 2 --progress 0 > rin_v2m2.out
python3 harnesses/rin_xor_csp_search.py --variables 2 --exists 1 --clauses 3 --width 2 --progress 0 > rin_v2m3.out
python3 harnesses/rin_xor_csp_search.py --variables 2 --exists 1 --clauses 4 --width 2 --progress 0 > rin_v2m4.out
python3 harnesses/rin_xor_csp_search.py --variables 3 --exists 1 --clauses 2 --width 3 --progress 0 > rin_v3m2.out
```

### 14.2 Independent Round-84 programs

These programs were written from the frozen definitions without importing the sealed proposer harness. The equality attack imports only my independent raw compiler. All five compiled and exited zero.

| program | bytes | LF | SHA-256 | exact output SHA-256 |
|---|---:|---:|---|---|
| `round84_raw_taxonomy.py` | 14,862 | 358 | `9b25591c194a54fc24380de51253b93f5db2934ded80807cdd3c5539154554f9` | `af0ef773ba00a571eb0856dc57cf096050a12e0f4e57987def89e35fa33caf60` |
| `round84_equality_attack.py` | 6,882 | 144 | `53e2125b1fad8d301bb600e4b8b68cbc401b9dd43c026e96acbe104a78b39bff` | `477976934d9e5a8105dd8a16f1ef9523743f6394274c5c33f0312592045b6067` |
| `round84_normalization_check.py` | 1,879 | 47 | `e44940903b00e23b18c4636b01ca49c648a0dc42505e42af2f30d49283c8fe43` | `e7fa6c7eeb0834bf30db5c4d04e60fd5e2ba9465d8b8cdf42dfe384735278088` |
| `round84_promise_check.py` | 4,698 | 138 | `a83824b2d0351fe1046ea3046995f25dcc80bb1cb78a22275a6fe002ab7a801f` | `977bf286757fa3012bf8daa2c87eb8f8467ee355cacf80991ade450f0d0dc634` |
| `round84_cluster_z_multifault.py` | 4,221 | 115 | `7a52b7a39ebc74d36d08d10a8cae5dceb2c7eefda3538d885ee36080de7b3003` | `3db30ba34cb569325ffc1154db73b4f075d33213024c60d92b4b307a6a803ed2` |

The raw taxonomy checker covered:

- 16,064 formulas and 32,128 schedules for three variables, one existential, three clauses;
- 174,720 complement rows and 5,667,040 raw indexed positions, of which 427,416 were marker-one late complement suffixes;
- 496 formulas and 1,984 schedules for three variables, two existential, two clauses;
- 10,368 complement rows and 275,232 raw indexed positions, of which 18,876 were marker-one late complement suffixes.

Every position-type assertion passed. The all-schedule equality attack covered 4,064 two-variable/four-clause formulas (8,128 schedules), 496 three-variable/two-existential formulas (1,984 schedules), and 49 targeted formulas/158 schedules including two duplicate-complement-row controls. No nonintended equality witness appeared. Its peak targeted DP layer was 661,932 states.

The normalization checker exhaustively verified 7,225 raw formulas in a one-existential/one-universal family and 67,081 in a two-existential/one-universal family. It exercised empty/no-clause constants, unused variables, repeated literals, and tautologies with no truth mismatch.

The promise checker verified the representative ranks/distances stated in section 9.4. The cluster checker examined all 116 nontrivial small CSS row-space-pair expansions in its scope for \(R=2,3\), checked 265 proper suffix layer-class assertions, and enumerated 4,865 indexed subsets below \(R\); no expanded \(Z\) logical occurred below the bound and all static \(d_Z\) values equaled \(R d_Z^{\rm base}\).

The independent replay commands were:

```sh
python3 -m py_compile round84_*.py
python3 round84_raw_taxonomy.py > round84_raw_taxonomy.out
python3 round84_equality_attack.py > round84_equality_attack.out
python3 round84_normalization_check.py > round84_normalization_check.out
python3 round84_promise_check.py > round84_promise_check.out
python3 round84_cluster_z_multifault.py > round84_cluster_z_multifault.out
```

### 14.3 Full independent source listings

The complete sources follow so the checks remain reproducible after scratch cleanup.

#### `round84_raw_taxonomy.py`

```python
#!/usr/bin/env python3
"""Independent raw-index audit of the frozen RIN compiler.

No Round-82/83 code is imported.  Physical positions and every proper cut are
kept as distinct records even when their labels coincide.
"""
from collections import Counter
from itertools import combinations, product


def wt(x):
    return bin(x).count('1')


def xor_all(xs):
    z = 0
    for x in xs:
        z ^= x
    return z


def rows_from_columns(cols, dim):
    return [sum(1 << j for j, x in enumerate(cols) if (x >> b) & 1)
            for b in range(dim)]


def kernel(equations, ncols):
    a = [x for x in equations if x]
    rank = 0
    pivots = []
    for col in range(ncols):
        hit = next((i for i in range(rank, len(a)) if (a[i] >> col) & 1), None)
        if hit is None:
            continue
        a[rank], a[hit] = a[hit], a[rank]
        for i in range(len(a)):
            if i != rank and ((a[i] >> col) & 1):
                a[i] ^= a[rank]
        pivots.append(col)
        rank += 1
        if rank == len(a):
            break
    pset = set(pivots)
    out = []
    for free in (c for c in range(ncols) if c not in pset):
        v = 1 << free
        for i, p in enumerate(pivots):
            if (a[i] >> free) & 1:
                v ^= 1 << p
        out.append(v)
    return out


def clause_sat(clause, assignment):
    return any(assignment[v] == satisfying_bit for v, satisfying_bit in clause)


def abstract_columns(formula, variables):
    groups = [('v', v) for v in variables] + [('c', j) for j in range(len(formula))]
    group_index = {g: i for i, g in enumerate(groups)}
    next_bit = len(groups)
    occ = {}
    for j, clause in enumerate(formula):
        for pos, (v, _) in enumerate(clause):
            occ[(v, j, pos)] = next_bit
            next_bit += 1
    cols = {}
    for v in variables:
        for b in (0, 1):
            label = 1 << group_index[('v', v)]
            if b:
                for (vv, j, pos), bit in occ.items():
                    if vv == v:
                        label ^= 1 << bit
            cols[('v', v, b)] = label
    for j, clause in enumerate(formula):
        clause_vars = tuple(sorted(v for v, _ in clause))
        for bits in product((0, 1), repeat=len(clause_vars)):
            a = dict(zip(clause_vars, bits))
            if not clause_sat(clause, a):
                continue
            label = 1 << group_index[('c', j)]
            for pos, (v, _) in enumerate(clause):
                if a[v]:
                    label ^= 1 << occ[(v, j, pos)]
            cols[('c', j, bits)] = label
    return cols, groups, next_bit


def group_of_name(name):
    if name[0] == 'v':
        return ('v', name[1])
    if name[0] == 'c':
        return ('c', name[1])
    raise AssertionError(name)


def compile_raw(formula, variables, exists, alpha):
    cols, groups, abstract_dim = abstract_columns(formula, variables)
    K = len(groups)
    group_mask = (1 << K) - 1
    flag = abstract_dim
    full = dict(cols)
    full[('anchor',)] = group_mask | (1 << flag)

    plane_specs = []
    for v in exists:
        plane_specs.append((('select', v), full[('v', v, 0)], full[('v', v, 1)], False))
    for name, a in full.items():
        if name[0] == 'v' and name[1] in exists:
            continue
        plane_specs.append((name, a, None, True))

    next_bit = abstract_dim + 1
    labels = []
    planes = []
    for plane_id, (name, a, b, fixed) in enumerate(plane_specs):
        p_bit = next_bit
        p = 1 << p_bit
        next_bit += 1
        r_bit = None
        if fixed:
            r_bit = next_bit
            b = 1 << r_bit
            next_bit += 1
        qs = tuple(range(len(labels), len(labels) + 4))
        labels.extend((p, p ^ a, p ^ b, p ^ a ^ b))
        planes.append(dict(id=plane_id, name=name, qs=qs, fixed=fixed,
                           a=a, b=b, p_bit=p_bit, r_bit=r_bit))

    # Quotient relation coordinates: selector delta or fixed payload.  Anchor is
    # retained as the last fixed coordinate but is forbidden as a pivot.
    rel_labels = []
    fixed_rel = []
    for pl in planes:
        q0, q1, q2, q3 = pl['qs']
        if pl['name'][0] == 'select':
            rel_labels.append(labels[q0] ^ labels[q3])
        else:
            rel_labels.append(labels[q0] ^ labels[q1])
            if pl['name'] != ('anchor',):
                fixed_rel.append(len(rel_labels) - 1)
    relations = kernel(rows_from_columns(rel_labels, next_bit), len(rel_labels))

    # Deterministic fixed-coordinate RREF, left to right.
    rank = 0
    pivots = []
    for coord in fixed_rel:
        hit = next((i for i in range(rank, len(relations))
                    if (relations[i] >> coord) & 1), None)
        if hit is None:
            continue
        relations[rank], relations[hit] = relations[hit], relations[rank]
        for i in range(len(relations)):
            if i != rank and ((relations[i] >> coord) & 1):
                relations[i] ^= relations[rank]
        pivots.append(coord)
        rank += 1
        if rank == len(relations):
            break
    assert rank == len(relations), ('fixed_projection_failure', rank, len(relations))
    for i, pivot in enumerate(pivots):
        assert (relations[i] >> pivot) & 1
        assert all(not ((relations[j] >> pivot) & 1)
                   for j in range(len(relations)) if j != i)

    records = []
    qinfo = {}
    for pl in planes:
        for pos, q in enumerate(pl['qs']):
            qinfo[q] = (pl, pos)
            records.append(dict(label=labels[q], kind='singleton', plane=pl,
                                pos=pos, q=q, indexed=('singleton', pl['id'], pos)))

    # Every local plane has three indexed proper suffix cuts.
    for pl in planes:
        q0, q1, q2, q3 = pl['qs']
        if pl['name'][0] == 'select':
            order = (q2, q3, q0, q1) if alpha[pl['name'][1]] == 0 else (q1, q3, q0, q2)
        else:
            order = (q2, q3, q0, q1)
        for cut in range(1, 4):
            records.append(dict(label=xor_all(labels[q] for q in order[cut:]),
                                kind='local_suffix', plane=pl, cut=cut, order=order,
                                indexed=('local_suffix', pl['id'], cut)))

    complement_orders = []
    for row_id, (rel, pivot_coord) in enumerate(zip(relations, pivots)):
        selected = [planes[i] for i in range(len(planes)) if (rel >> i) & 1]
        pivot = planes[pivot_coord]
        assert pivot in selected and pivot['fixed'] and pivot['name'] != ('anchor',)
        assert all(not ((other >> pivot_coord) & 1)
                   for j, other in enumerate(relations) if j != row_id)
        early = [pivot['qs'][0]]
        late = []
        pivot_group = group_of_name(pivot['name'])
        for pl in selected:
            if pl is pivot:
                continue
            if pl['name'][0] == 'select':
                early.extend((pl['qs'][0], pl['qs'][3]))
            else:
                assert pl['name'] != ('anchor',)
                early.append(pl['qs'][0])
                late.append((group_of_name(pl['name']), pl['name'], pl['qs'][1]))
        late.sort(key=lambda z: (z[0] == pivot_group, z[0], str(z[1])))
        order = tuple(early + [q for _, _, q in late] + [pivot['qs'][1]])
        assert len(order) == len(set(order))
        # Exact full row label is zero, and each support coordinate occurs once.
        assert xor_all(labels[q] for q in order) == 0
        assert len(order) == 2 * wt(rel)
        first_late = len(early)
        complement_orders.append((row_id, order, first_late, rel, pivot_coord))
        for cut in range(1, len(order)):
            records.append(dict(label=xor_all(labels[q] for q in order[cut:]),
                                kind='complement_suffix', row=row_id, cut=cut,
                                order=order, first_late=first_late,
                                indexed=('complement_suffix', row_id, cut)))
    return dict(labels=labels, planes=planes, records=records, orders=complement_orders,
                groups=groups, K=K, group_mask=group_mask, flag=flag,
                qinfo=qinfo, relations=relations, pivots=pivots, next_bit=next_bit)


def classify(compiled, alpha, counts):
    labels = compiled['labels']; gm = compiled['group_mask']; flag = compiled['flag']
    qinfo = compiled['qinfo']; groups = compiled['groups']
    selector_private_bits = {}
    fixed_private_bits = {}
    for pl in compiled['planes']:
        if pl['name'][0] == 'select':
            selector_private_bits[('v', pl['name'][1])] = pl['p_bit']
        elif pl['name'] != ('anchor',):
            fixed_private_bits[pl['id']] = (pl['p_bit'], pl['r_bit'])

    group_entries = {g: [] for g in groups}
    seen_index = set()
    for rec in compiled['records']:
        assert rec['indexed'] not in seen_index
        seen_index.add(rec['indexed'])
        z = rec['label']; marker = z & gm; marker_weight = wt(marker); flagbit = (z >> flag) & 1
        rec['marker'] = marker; rec['marker_weight'] = marker_weight; rec['flagbit'] = flagbit

        if rec['kind'] == 'singleton':
            pl, pos = rec['plane'], rec['pos']; name = pl['name']
            if name[0] == 'select':
                counts[f'singleton_selector_q{pos}'] += 1
                assert marker_weight == (1 if pos in (1, 2) else 0) and not flagbit
            elif name == ('anchor',):
                counts[f'singleton_anchor_q{pos}'] += 1
                assert marker in (0, gm)
                assert flagbit == (pos in (1, 3))
                assert bool(marker) == bool(flagbit)
            else:
                counts[f'singleton_fixed_q{pos}'] += 1
                assert marker_weight == (1 if pos in (1, 3) else 0) and not flagbit

        elif rec['kind'] == 'local_suffix':
            pl, cut = rec['plane'], rec['cut']; name = pl['name']; q0, q1, q2, q3 = pl['qs']
            # cut=1 has length 3, cut=2 length 2, cut=3 length 1 in forward order.
            suffix_len = 4 - cut
            if name[0] == 'select':
                a = alpha[name[1]]
                expected = {1: labels[q0] ^ (pl['a'] if a == 0 else pl['b']),
                            2: (pl['a'] if a == 0 else pl['b']),
                            3: labels[q0] ^ (pl['b'] if a == 0 else pl['a'])}[suffix_len]
                assert z == expected and marker_weight == 1 and not flagbit
                counts[f'local_selector_len{suffix_len}'] += 1
            elif name == ('anchor',):
                p = 1 << pl['p_bit']; r = 1 << pl['r_bit']; h = pl['a']
                expected = {1: p ^ h, 2: h, 3: p ^ r}[suffix_len]
                assert z == expected
                assert (flagbit, marker) == ((1, gm) if suffix_len in (1, 2) else (0, 0))
                counts[f'local_anchor_len{suffix_len}'] += 1
            else:
                p = 1 << pl['p_bit']; r = 1 << pl['r_bit']; a = pl['a']; v = p ^ a
                expected = {1: v, 2: a, 3: p ^ r}[suffix_len]
                assert z == expected and not flagbit
                assert marker_weight == (1 if suffix_len in (1, 2) else 0)
                counts[f'local_fixed_len{suffix_len}'] += 1

        else:
            order, cut, first = rec['order'], rec['cut'], rec['first_late']
            assert not flagbit and marker_weight <= 1
            if cut < first:
                # Starts in the early zero-marker zone and includes the whole late zone.
                assert marker == 0
                counts['complement_early_marker0'] += 1
            else:
                # Every endpoint in the suffix is literally q1 of a fixed nonanchor plane.
                js = []
                for q in order[cut:]:
                    pl, pos = qinfo[q]
                    assert pos == 1 and pl['fixed'] and pl['name'] != ('anchor',)
                    assert pl['name'][0] != 'select' and pl['r_bit'] is not None
                    js.append(pl)
                expected = xor_all((1 << pl['p_bit']) ^ pl['a'] for pl in js)
                assert z == expected
                counts['complement_late_marker1' if marker_weight else 'complement_late_marker0'] += 1
                rec['J'] = tuple(pl['id'] for pl in js)

        if not flagbit and marker_weight == 1:
            gi = (marker & -marker).bit_length() - 1
            group_entries[groups[gi]].append(rec)

    # Symbolic RIN premise audit over the complete raw indexed catalogue.
    for group, entries in group_entries.items():
        assert entries, group
        if group[0] == 'v' and group in selector_private_bits:
            px = selector_private_bits[group]
            for e in entries:
                # Selector groups have no marker-one complement suffix at all.
                assert e['kind'] != 'complement_suffix'
                intended = (e['kind'] == 'local_suffix' and e['label'] ==
                            next(pl['a'] if alpha[group[1]] == 0 else pl['b']
                                 for pl in compiled['planes'] if pl['name'] == ('select', group[1])))
                assert intended or ((e['label'] >> px) & 1)
        else:
            for e in entries:
                if e['kind'] == 'complement_suffix':
                    assert 'J' in e
                elif e['kind'] in ('singleton', 'local_suffix'):
                    pl = e['plane']; assert pl['fixed'] and pl['name'] != ('anchor',)
                    pbit, rbit = pl['p_bit'], pl['r_bit']; a = pl['a']; v = (1 << pbit) ^ a
                    assert e['label'] in (a, v, v ^ (1 << rbit))

    counts['raw_indexed_total'] += len(compiled['records'])
    counts['complement_rows'] += len(compiled['orders'])


def clause_types(variables, width):
    out = []
    for size in range(1, min(width, len(variables)) + 1):
        for vs in combinations(variables, size):
            for bits in product((0, 1), repeat=size):
                out.append(tuple(zip(vs, bits)))
    return out


def run_family(variables, exists, clauses_n, width):
    c = Counter(); formulas = schedules = 0
    templates = clause_types(variables, width)
    for formula in product(templates, repeat=clauses_n):
        if any(all(vv != v for clause in formula for vv, _ in clause) for v in variables):
            continue
        formulas += 1
        for bits in product((0, 1), repeat=len(exists)):
            schedules += 1
            alpha = dict(zip(exists, bits))
            compiled = compile_raw(formula, variables, exists, alpha)
            classify(compiled, alpha, c)
    print('RAW_TAXONOMY_PASS', dict(variables=len(variables), exists=len(exists),
          clauses=clauses_n, width=width, formulas=formulas, schedules=schedules))
    print('COUNTS', ' '.join(f'{k}={v}' for k, v in sorted(c.items())))


if __name__ == '__main__':
    run_family(('x', 'y', 'z'), ('x',), 3, 3)
    run_family(('x', 'y', 'z'), ('x', 'y'), 2, 3)
```

#### `round84_equality_attack.py`

```python
#!/usr/bin/env python3
"""Exact all-schedule attack on the equality case, preserving intended/nonintended status."""
from itertools import product, permutations
import random, sys
from round84_raw_taxonomy import compile_raw, clause_types, clause_sat, wt


def psi(formula, assignment):
    return all(clause_sat(c, assignment) for c in formula)


def has_beta(formula, variables, exists, alpha):
    univ = tuple(v for v in variables if v not in exists)
    return any(psi(formula, {**alpha, **dict(zip(univ, bits))})
               for bits in product((0, 1), repeat=len(univ)))


def exact_attack(formula, variables, exists, alpha, cap=30_000_000, duplicate_complement=False):
    d = compile_raw(formula, variables, exists, alpha)
    if duplicate_complement:
        clones=[]
        for rec in d['records']:
            if rec['kind'] == 'complement_suffix':
                x=dict(rec); x['indexed']=('duplicate_row_control',)+rec['indexed']; clones.append(x)
        d['records'].extend(clones)
    K, gm, flag = d['K'], d['group_mask'], d['flag']
    opts = [set() for _ in range(K)]
    indexed_unit = 0
    raw_duplicate_options = 0
    for rec in d['records']:
        z = rec['label']; marker = z & gm
        if ((z >> flag) & 1) or wt(marker) != 1:
            continue
        indexed_unit += 1
        gi = (marker & -marker).bit_length() - 1
        intended = rec['kind'] == 'local_suffix' and rec['cut'] == 2
        pair = (z ^ marker, not intended)
        if pair in opts[gi]:
            raw_duplicate_options += 1
        opts[gi].add(pair)
    assert all(opts)
    # flags[x] bit 0 = an all-intended path reaches x; bit 1 = a path with
    # at least one nonintended indexed location reaches x.
    states = {0: 1}; peak = 1
    for gi in sorted(range(K), key=lambda i: len(opts[i])):
        ns = {}
        for x, flags in states.items():
            for residual, bad_option in opts[gi]:
                y = x ^ residual
                out = 0
                if flags & 1:
                    out |= 2 if bad_option else 1
                if flags & 2:
                    out |= 2
                ns[y] = ns.get(y, 0) | out
        states = ns; peak = max(peak, len(states))
        if len(states) > cap:
            raise RuntimeError(('state_cap', len(states), gi, formula, alpha))
    zero_flags = states.get(0, 0)
    expected = has_beta(formula, variables, exists, alpha)
    assert bool(zero_flags & 1) == expected, ('truth_mismatch', formula, alpha, zero_flags)
    assert not (zero_flags & 2), ('NONINTENDED_EQUALITY', formula, alpha, zero_flags)
    return peak, indexed_unit, raw_duplicate_options, len(d['relations']), d


def normalized(formula, variables):
    return all(any(vv == v for c in formula for vv, _ in c) for v in variables)


def run_exhaustive(variables, exists, m, width):
    forms = schedules = unsafe = 0; peak = max_unit = duplicates = rows = shared = same_j = 0
    for formula in product(clause_types(variables, width), repeat=m):
        if not normalized(formula, variables):
            continue
        forms += 1
        for bits in product((0, 1), repeat=len(exists)):
            schedules += 1; alpha = dict(zip(exists, bits))
            if has_beta(formula, variables, exists, alpha): unsafe += 1
            pk, units, dup, nr, d = exact_attack(formula, variables, exists, alpha)
            peak = max(peak, pk); max_unit = max(max_unit, units); duplicates += dup; rows += nr
            # Count adversarial structure: relation-row overlap on nonpivot fixed planes.
            support_counts = {}
            for rel, pivot in zip(d['relations'], d['pivots']):
                for j in range(len(d['planes'])):
                    if j != pivot and ((rel >> j) & 1) and d['planes'][j]['fixed']:
                        support_counts[j] = support_counts.get(j, 0) + 1
            if any(v > 1 for v in support_counts.values()): shared += 1
            # Repeated complement suffix J labels are detected by exact label duplicates.
            labs = [r['label'] for r in d['records'] if r['kind'] == 'complement_suffix']
            if len(labs) != len(set(labs)): same_j += 1
    print('ALL_SCHEDULE_EQUALITY_PASS', dict(variables=len(variables), exists=len(exists),
          clauses=m, width=width, formulas=forms, schedules=schedules, unsafe=unsafe,
          peak_states=peak, max_indexed_unit=max_unit, raw_duplicate_options=duplicates,
          relation_rows=rows, schedules_shared_nonpivot=shared,
          schedules_repeated_complement_labels=same_j))


def targeted():
    V = ('x', 'y', 'z'); E = ('x',)
    wide = tuple(zip(V, (0, 0, 0)))
    units = ((('y', 1),), (('z', 1),))
    seen = set(); cases = peak = duplicate_controls = 0
    # Odd XOR of multiple allowed wide-clause options; all clause permutations.
    for f in set(permutations((wide,) + units)):
        seen.add(f)
        for xb in (0, 1):
            pk, *_ = exact_attack(f, V, E, {'x': xb}); peak = max(peak, pk); cases += 1
    # Duplicate wide clauses plus the same two units.
    for f in set(permutations((wide, wide) + units)):
        seen.add(f)
        for xb in (0, 1):
            pk, *_ = exact_attack(f, V, E, {'x': xb}); peak = max(peak, pk); cases += 1
    # Multiple existentials and four variables, bounded two-clause families.
    V4 = ('x', 'y', 'z', 'w'); E4 = ('x', 'y')
    hand = [
      ((('x',0),('z',0),('w',0)), (('y',1),('z',1),('w',1))),
      ((('x',1),('y',0),('z',1)), (('x',0),('y',1),('w',0))),
      ((('x',0),('z',1)), (('y',0),('w',1))),
    ]
    rng = random.Random(8403); templates = clause_types(V4, 3)
    while len(hand) < 30:
        f = tuple(rng.choice(templates) for _ in range(2))
        if normalized(f, V4): hand.append(f)
    for f in hand:
        for bits in product((0, 1), repeat=2):
            pk, *_ = exact_attack(f, V4, E4, dict(zip(E4, bits)), cap=8_000_000)
            peak = max(peak, pk); cases += 1
    # Duplicate every complement check row as a second indexed measured row.
    # Row space and labels are unchanged, but repeated indexed suffix labels are real.
    dup_formula = ((('x',0),('y',0)), (('x',1),('y',1)), (('x',0),('y',1)))
    for xb in (0, 1):
        pk, units_n, dup, nr, d = exact_attack(dup_formula, ('x','y'), ('x',), {'x':xb},
                                               duplicate_complement=True)
        assert nr and dup > 0
        peak=max(peak,pk); cases += 1; duplicate_controls += 1
    print('TARGETED_EQUALITY_PASS', dict(formulas=len(seen)+len(hand)+1, schedules=cases,
          duplicate_complement_controls=duplicate_controls, peak_states=peak,
          attacks='odd-xor,repeated-wide,multiple-existentials,pivot-sharing,mixed-signs,repeated-indexed-suffix-labels'))


if __name__ == '__main__':
    run_exhaustive(('x', 'y'), ('x',), 4, 2)
    run_exhaustive(('x', 'y', 'z'), ('x', 'y'), 2, 3)
    targeted()
```

#### `round84_normalization_check.py`

```python
#!/usr/bin/env python3
from itertools import product


def clause_sat(C,a): return any(a[v]==b for v,b in C)
def psi(F,a): return all(clause_sat(C,a) for C in F)

def qbf_yes(F,E,U):
    return any(not any(psi(F,{**dict(zip(E,eb)),**dict(zip(U,ub))})
                       for ub in product((0,1),repeat=len(U)))
               for eb in product((0,1),repeat=len(E)))

def normalize(F,E,U):
    out=[]
    for C in F:
        vals={}
        taut=False
        for v,b in C:
            if v in vals and vals[v]!=b: taut=True;break
            vals[v]=b
        if taut: continue
        out.append(tuple(sorted(vals.items())))
    if any(len(C)==0 for C in out): return 'YES_CONSTANT',(),(),()
    if not out: return 'NO_CONSTANT',(),(),()
    used={v for C in out for v,b in C}
    return 'NONCONSTANT',tuple(out),tuple(v for v in E if v in used),tuple(v for v in U if v in used)

def run(E,U):
    V=E+U;lits=tuple((v,b) for v in V for b in (0,1))
    clauses=[()]
    for L in (1,2,3): clauses.extend(product(lits,repeat=L))
    total=yes_c=no_c=non=unused=dups=tauts=0
    for F in product(clauses,repeat=2):
        total+=1; before=qbf_yes(F,E,U); kind,N,NE,NU=normalize(F,E,U)
        if kind=='YES_CONSTANT': after=True;yes_c+=1
        elif kind=='NO_CONSTANT': after=False;no_c+=1
        else:
            after=qbf_yes(N,NE,NU);non+=1
            if len(NE)+len(NU)<len(E)+len(U):unused+=1
        if any(len(set(C))<len(C) for C in F):dups+=1
        if any(any((v,0) in C and (v,1) in C for v in V) for C in F):tauts+=1
        assert before==after,(F,kind,N,NE,NU,before,after)
    print('NORMALIZATION_PASS',dict(exists=len(E),universals=len(U),raw_formulas=total,
          yes_constants=yes_c,no_constants=no_c,nonconstant=non,
          unused_deleted=unused,repeated_literal_formulas=dups,tautology_formulas=tauts))
run(('x',),('y',))
run(('x','y'),('z',))
```

#### `round84_promise_check.py`

```python
#!/usr/bin/env python3
"""Independent rank/static/effective promise audit on the smallest nonconstant instance."""
from round84_raw_taxonomy import compile_raw, rows_from_columns, xor_all, wt


def rank(rows):
    b=[]
    for x in rows:
        y=x
        for p,r in b:
            if (y>>p)&1: y^=r
        if not y: continue
        p=y.bit_length()-1
        for i,(q,r) in enumerate(b):
            if (r>>p)&1: b[i]=(q,r^y)
        b.append((p,y)); b.sort(reverse=True)
    return len(b)


def span(rows):
    s={0}
    for r in rows: s |= {x^r for x in tuple(s)}
    return s


def dot(a,b): return wt(a&b)&1


def distance(n, checks, stabilizers):
    S=span(stabilizers)
    for w in range(1,n+1):
        for e in range(1,1<<n):
            if wt(e)==w and e not in S and all(not dot(e,h) for h in checks):
                return w
    return None


def min_target(labels,target):
    dp={0:0}
    for x in labels:
        nd=dict(dp)
        for s,w in dp.items():
            t=s^x
            if w+1<nd.get(t,10**9): nd[t]=w+1
        dp=nd
    return dp.get(target)


def physical_code(d):
    labels=d['labels']; n=len(labels)
    B=rows_from_columns(labels,d['next_bit'])
    HZ=[row for i,row in enumerate(B) if i!=d['flag']]
    HX=[]
    for pl in d['planes']:
        HX.append(sum(1<<q for q in pl['qs']))
    for rel in d['relations']:
        row=0
        for i,pl in enumerate(d['planes']):
            if not ((rel>>i)&1): continue
            q0,q1,q2,q3=pl['qs']
            row ^= (1<<q0)|(1<<(q3 if pl['name'][0]=='select' else q1))
        HX.append(row)
    assert all(not dot(x,z) for x in HX for z in HZ)
    assert rank(HX)==n-rank(B)
    return labels,HX,HZ,B


def expand(HX,HZ,n,R):
    def bit(q,j): return 1<<(q*R+j)
    ex=[]
    for q in range(n):
        for j in range(R-1): ex.append(bit(q,j)^bit(q,j+1))
    for x in HX:
        ex.append(sum(bit(q,0) for q in range(n) if (x>>q)&1))
    ez=[]
    for z in HZ:
        ez.append(sum(bit(q,j) for q in range(n) if (z>>q)&1 for j in range(R)))
    assert all(not dot(x,z) for x in ex for z in ez)
    assert rank(ex)==n*(R-1)+rank(HX)
    assert rank(ez)==rank(HZ)
    return ex,ez


def grid(D):
    R=D; n=D*R
    def bit(i,j): return 1<<(i*R+j)
    HX=[bit(i,j)^bit(i,j+1) for i in range(D) for j in range(R-1)]
    HZ=[sum(bit(i,j)|bit(i+1,j) for j in range(R)) for i in range(D-1)]
    assert all(not dot(x,z) for x in HX for z in HZ)
    return n,HX,HZ


def run():
    formula=((('x',0),),); variables=('x',); exists=('x',)
    compiled=compile_raw(formula,variables,exists,{'x':0})
    K=compiled['K']; requested=K+2
    labels,HX,HZ,B=physical_code(compiled)
    n=len(labels); k=n-rank(HX)-rank(HZ)
    dX=distance(n,HZ,HX); dZ=distance(n,HX,HZ)
    assert k==1 and dX is not None and dZ is not None
    assert dX>=requested and dZ>=1
    ex,ez=expand(HX,HZ,n,requested)
    gn,gx,gz=grid(requested)
    gdX=distance(gn,gz,gx); gdZ=distance(gn,gx,gz)
    assert gdX==gdZ==requested
    expanded_dX=dX; expanded_dZ=requested*dZ
    direct_dX=min(expanded_dX,gdX); direct_dZ=min(expanded_dZ,gdZ)
    assert direct_dX==direct_dZ==requested

    # Exact base/expanded X catalogue minima for the two selector schedules.
    eff=[]
    for xb in (0,1):
        c=compile_raw(formula,variables,exists,{'x':xb})
        base=[r['label'] for r in c['records']]
        target=1<<c['flag']
        base_min=min_target(base,target)
        # Expanded X: every copied singleton and equality suffix maps to its old
        # singleton label; every lifted old proper suffix has its old label.
        old_single=[r['label'] for r in c['records'] if r['kind']=='singleton']
        old_suffix=[r['label'] for r in c['records'] if r['kind']!='singleton']
        expanded=(old_single*requested + old_single*(requested-1) + old_suffix)
        expanded_min=min_target(expanded,target)
        assert expanded_min==base_min
        eff.append(base_min)
    assert eff[0]==K+1 and (eff[1] is None or eff[1]>=requested)
    total_unsafe=min(eff[0],requested); total_safe=requested
    assert total_unsafe==K+1<requested and total_safe==requested
    print('PROMISE_CHECK_PASS',dict(K=K,requested_d=requested,base_n=n,
          base_rank_HX=rank(HX),base_rank_HZ=rank(HZ),base_k=k,
          base_dX=dX,base_dZ=dZ,expanded_n=n*requested,
          expanded_rank_HX=rank(ex),expanded_rank_HZ=rank(ez),
          expanded_dX=expanded_dX,expanded_dZ=expanded_dZ,
          grid_n=gn,grid_dX=gdX,grid_dZ=gdZ,
          direct_dX=direct_dX,direct_dZ=direct_dZ,
          base_effX_unsafe=eff[0],base_effX_safe=eff[1],
          total_eff_unsafe=total_unsafe,total_eff_safe=total_safe))

if __name__=='__main__': run()
```

#### `round84_cluster_z_multifault.py`

```python
#!/usr/bin/env python3
"""Exhaustive multi-fault check of the R_R layer-major Z theorem on all n<=3 CSS row-space pairs."""
from itertools import combinations


def wt(x): return bin(x).count('1')
def dot(a,b): return wt(a&b)&1

def span(rows):
    s={0}
    for r in rows: s |= {x^r for x in tuple(s)}
    return frozenset(s)

def basis_of(S):
    B=[]
    for x in sorted(S):
        y=x
        for p,r in B:
            if (y>>p)&1:y^=r
        if y:
            p=y.bit_length()-1
            for i,(q,r) in enumerate(B):
                if (r>>p)&1:B[i]=(q,r^y)
            B.append((p,y));B.sort(reverse=True)
    return tuple(r for p,r in B)

def subspaces(n):
    vals=range(1,1<<n); out={}
    for mask in range(1<<len(tuple(vals))):
        rows=[v for i,v in enumerate(vals) if (mask>>i)&1]
        S=span(rows);out[S]=basis_of(S)
    return list(out.items())

def expand_x(HX,n,R):
    def b(q,j):return 1<<(q*R+j)
    rows=[b(q,j)^b(q,j+1) for q in range(n) for j in range(R-1)]
    rows += [sum(b(q,0) for q in range(n) if (x>>q)&1) for x in HX]
    return rows

def expand_z(HZ,n,R):
    def b(q,j):return 1<<(q*R+j)
    return [sum(b(q,j) for q in range(n) if (z>>q)&1 for j in range(R)) for z in HZ]

def gamma_z(HZ,n,R):
    def b(q,j):return 1<<(q*R+j)
    g=[b(q,j) for q in range(n) for j in range(R)]
    per=[]
    for ri,z in enumerate(HZ):
        supp=[q for q in range(n) if (z>>q)&1]
        order=[b(q,j) for j in range(R) for q in supp]
        for cut in range(1,len(order)):
            col=0
            for e in order[cut:]:col^=e
            g.append(col);per.append((ri,cut,col,order))
    return g,per

def normalizer(v,checks):return all(not dot(v,x) for x in checks)
def min_fault_to_logical(gamma,HX,SZ,nR):
    dp={0:0}
    for col in gamma:
        nd=dict(dp)
        for v,w in dp.items():
            t=v^col
            if w+1<nd.get(t,10**9):nd[t]=w+1
        dp=nd
    ans=[w for v,w in dp.items() if normalizer(v,HX) and v not in SZ]
    return min(ans) if ans else None

def qclass(v,S):
    # canonical minimum integer representative of v+S
    return min(v^s for s in S)

def run():
    cases=finite=multi_checked=single_layer_ok=0; minima={}
    for n in (1,2,3):
      spaces=subspaces(n)
      for SX,HX in spaces:
       for SZ,HZ in spaces:
        if any(dot(x,z) for x in HX for z in HZ):continue
        if len(SX)*len(SZ)>=1<<n:continue # k=0 or invalid dimension
        base_norm=[z for z in range(1<<n) if normalizer(z,HX)]
        base_log=[z for z in base_norm if z not in SZ]
        if not base_log:continue
        dZ=min(wt(z) for z in base_log)
        for R in (2,3):
          cases+=1;nR=n*R
          ex=expand_x(HX,n,R);ez=expand_z(HZ,n,R);ESZ=span(ez)
          gam,per=gamma_z(HZ,n,R)
          # Every suffix has nonzero Q class in at most one layer.
          for ri,cut,col,order in per:
            layer_classes=[]
            for j in range(R):
                old=sum(1<<q for q in range(n) if (col>>(q*R+j))&1)
                layer_classes.append(qclass(old,SZ))
            assert sum(c!=0 for c in layer_classes)<=1
            single_layer_ok+=1
          actual=min_fault_to_logical(gam,ex,ESZ,nR)
          assert actual is None or actual>=R,(n,HX,HZ,R,actual)
          # Enumerate all sums of <R indexed faults directly as an independent control.
          for w in range(1,R):
            for inds in combinations(range(len(gam)),w):
              v=0
              for i in inds:v^=gam[i]
              assert not (normalizer(v,ex) and v not in ESZ),(n,HX,HZ,R,w,inds)
              multi_checked+=1
          # Static Z distance is exactly R*dZ by exhaustive physical enumeration here.
          static=[wt(v) for v in range(1<<nR) if normalizer(v,ex) and v not in ESZ]
          assert min(static)==R*dZ
          finite += actual is not None
          minima[(R,actual)] = minima.get((R,actual),0)+1
    print('CLUSTER_Z_MULTIFAULT_PASS',dict(css_expansions=cases,finite_effective=finite,
          proper_suffix_layer_class_checks=single_layer_ok,
          indexed_fault_subsets_below_R=multi_checked,
          minima={str(k):v for k,v in sorted(minima.items(),key=lambda x:str(x[0]))}))
if __name__=='__main__':run()
```

### 14.4 Exact independent outputs

#### `round84_raw_taxonomy.out`

```text
RAW_TAXONOMY_PASS {'variables': 3, 'exists': 1, 'clauses': 3, 'width': 3, 'formulas': 16064, 'schedules': 32128}
COUNTS complement_early_marker0=808432 complement_late_marker0=427416 complement_late_marker1=427416 complement_rows=174720 local_anchor_len1=32128 local_anchor_len2=32128 local_anchor_len3=32128 local_fixed_len1=507712 local_fixed_len2=507712 local_fixed_len3=507712 local_selector_len1=32128 local_selector_len2=32128 local_selector_len3=32128 raw_indexed_total=5667040 singleton_anchor_q0=32128 singleton_anchor_q1=32128 singleton_anchor_q2=32128 singleton_anchor_q3=32128 singleton_fixed_q0=507712 singleton_fixed_q1=507712 singleton_fixed_q2=507712 singleton_fixed_q3=507712 singleton_selector_q0=32128 singleton_selector_q1=32128 singleton_selector_q2=32128 singleton_selector_q3=32128
RAW_TAXONOMY_PASS {'variables': 3, 'exists': 2, 'clauses': 2, 'width': 3, 'formulas': 496, 'schedules': 1984}
COUNTS complement_early_marker0=46184 complement_late_marker0=18876 complement_late_marker1=18876 complement_rows=10368 local_anchor_len1=1984 local_anchor_len2=1984 local_anchor_len3=1984 local_fixed_len1=21376 local_fixed_len2=21376 local_fixed_len3=21376 local_selector_len1=3968 local_selector_len2=3968 local_selector_len3=3968 raw_indexed_total=275232 singleton_anchor_q0=1984 singleton_anchor_q1=1984 singleton_anchor_q2=1984 singleton_anchor_q3=1984 singleton_fixed_q0=21376 singleton_fixed_q1=21376 singleton_fixed_q2=21376 singleton_fixed_q3=21376 singleton_selector_q0=3968 singleton_selector_q1=3968 singleton_selector_q2=3968 singleton_selector_q3=3968
```

#### `round84_equality_attack.out`

```text
ALL_SCHEDULE_EQUALITY_PASS {'variables': 2, 'exists': 1, 'clauses': 4, 'width': 2, 'formulas': 4064, 'schedules': 8128, 'unsafe': 2332, 'peak_states': 208256, 'max_indexed_unit': 70, 'raw_duplicate_options': 102912, 'relation_rows': 5120, 'schedules_shared_nonpivot': 512, 'schedules_repeated_complement_labels': 0}
ALL_SCHEDULE_EQUALITY_PASS {'variables': 3, 'exists': 2, 'clauses': 2, 'width': 3, 'formulas': 496, 'schedules': 1984, 'unsafe': 1576, 'peak_states': 35330, 'max_indexed_unit': 95, 'raw_duplicate_options': 39680, 'relation_rows': 10368, 'schedules_shared_nonpivot': 1984, 'schedules_repeated_complement_labels': 0}
TARGETED_EQUALITY_PASS {'formulas': 49, 'schedules': 158, 'duplicate_complement_controls': 2, 'peak_states': 661932, 'attacks': 'odd-xor,repeated-wide,multiple-existentials,pivot-sharing,mixed-signs,repeated-indexed-suffix-labels'}
```

#### `round84_normalization_check.out`

```text
NORMALIZATION_PASS {'exists': 1, 'universals': 1, 'raw_formulas': 7225, 'yes_constants': 169, 'no_constants': 1600, 'nonconstant': 5456, 'unused_deleted': 1032, 'repeated_literal_formulas': 5544, 'tautology_formulas': 5200}
NORMALIZATION_PASS {'exists': 2, 'universals': 1, 'raw_formulas': 67081, 'yes_constants': 517, 'no_constants': 9216, 'nonconstant': 57348, 'unused_deleted': 27588, 'repeated_literal_formulas': 42432, 'tautology_formulas': 40512}
```

#### `round84_promise_check.out`

```text
PROMISE_CHECK_PASS {'K': 2, 'requested_d': 4, 'base_n': 12, 'base_rank_HX': 3, 'base_rank_HZ': 8, 'base_k': 1, 'base_dX': 6, 'base_dZ': 2, 'expanded_n': 48, 'expanded_rank_HX': 39, 'expanded_rank_HZ': 8, 'expanded_dX': 6, 'expanded_dZ': 8, 'grid_n': 16, 'grid_dX': 4, 'grid_dZ': 4, 'direct_dX': 4, 'direct_dZ': 4, 'base_effX_unsafe': 3, 'base_effX_safe': 4, 'total_eff_unsafe': 3, 'total_eff_safe': 4}
```

#### `round84_cluster_z_multifault.out`

```text
CLUSTER_Z_MULTIFAULT_PASS {'css_expansions': 116, 'finite_effective': 116, 'proper_suffix_layer_class_checks': 265, 'indexed_fault_subsets_below_R': 4865, 'minima': {'(2, 2)': 46, '(2, 4)': 11, '(2, 6)': 1, '(3, 3)': 46, '(3, 6)': 11, '(3, 9)': 1}}
```

## 15. FIX-1/FIX-2, validation, limitations, and settlement contract

### 15.1 FIX-1: exact canonical scope

The replacement YAML in section 13 is the sole licensed canonical content delta. Its raw candidate before embedding is 12,765 bytes with SHA-256 `610ab959703dbf7cbd727a839f6f18e9a1df295e72330161227788a591379c47`. It keeps the exact claim string unchanged, binds the two completion assessments to the correct reviewed statement hashes, preserves historical evidence and events, adds only the direct route and its Round-84 provenance, and expressly denies root promotion.

In a scratch overlay containing all current proof-DAG nodes and source artifacts, I installed the candidate plus this report, parsed every YAML with the repository `UniqueKeyLoader`, regenerated only scratch derived views, and ran `tools.proof_dag_schema.validate_problem`: 16 nodes, zero schema errors, and zero warnings. `validate_preservation` against the current canonical snapshot returned zero errors, confirming that no current node, route, or event was removed or rewritten. Candidate-overlay evidence closure found 151 structured paths and zero errors. On the deliberately unchanged canonical node, evidence closure still identifies the Round-82, Round-83, and this Round-84 files as unlinked until the licensed YAML is applied; that expected pending-link state is not a candidate defect. Canonical generated views remain untouched in this review task.

### 15.2 FIX-2 baseline and mutation accounting

Before any review write, the repository state was deliberately dirty from concurrent work. I preserved it rather than cleaning or resetting it:

- `git status --porcelain=v2 --untracked-files=all`: 1,345,901 bytes, 10,054 LF lines, SHA-256 `3dbd64c8dd3cd8e8b211e50583a9be3c362179156b41d7254940252d00874a53`;
- regular files outside `.git`: 12,292 files and 1,012,869,992 total bytes;
- the complete baseline file manifest: 2,831,095 bytes, SHA-256 `5c18bde7b89d8f5a5d48d02f8ac0c77bcb02b0650c6eec18172765c16605572c`.

All scratch work lived under `/tmp/circdist-cplx-sigma2-rin-final-round84-20260830`. The final settlement procedure rehashes every protected input, compares a fresh repository inventory with that baseline while preserving concurrent drift, deletes the scratch tree, checks for surviving reviewer processes/files, and verifies that this report is the sole attributable durable addition. The final artifact byte count, LF count, and SHA-256 are necessarily reported in the external handoff after the immutable file exists; embedding a file's own SHA-256 would change that hash.

### 15.3 Command and process ledger

Every substantive program ran in the foreground and terminated. No daemon, detached job, shell session, or child agent was created. Final successful operations were:

1. full-byte reads, UTF-8 reads, hashes, and YAML parses of every bound input;
2. bounded extraction and SHA verification of seven sealed programs;
3. `py_compile` plus serial execution of all seven sealed programs and four RIN parameter sets;
4. compilation and serial execution of the five independent Round-84 programs reproduced above;
5. independent raw taxonomy enumeration, all-schedule/targeted equality search, normalization truth check, rank/distance promise check, and multi-fault cluster-\(Z\) check;
6. `UniqueKeyLoader`, locator, statement-hash, and full proof-DAG schema validation in a scratch overlay;
7. protected-input rehash, Markdown/fence/source checks, repository inventory comparison, scratch removal, and survivor scan.

The non-success path was fully bounded:

- two early taxonomy runs failed reviewer assertions because of the suffix-table and tuple/string bugs described in section 11; both exited and were superseded;
- one large exploratory equality run reached its declared state/resource boundary after 56,338,696 states and exited without a verdict; it is not cited as evidence;
- the first candidate schema pass correctly reported only two stale scratch generated views; regenerating those scratch views made the pass clean;
- one attempted scratch-overlay reset command was rejected before execution by the command safety layer; a fresh overlay directory was used instead.

No candidate counterexample was observed in any completed or capped search. If one had appeared, the required procedure was to replay it end to end against raw indexed locations before drawing a conclusion.

### 15.4 Limitations

This review proves exactly the frozen single-ancilla terminal-residual Eff-Preserve theorem with ordinary qubit-sharing conflicts, no optional depth bound, and total promise-preserving many-one reductions. It assumes the standard external completeness theorem for `QSAT_{2,3DNF}`. It does not prove a Circ-Preserve variant, an arbitrary-conflict-graph variant, or the parent classification claim. The finite checkers corroborate the symbolic proof and expose implementation mistakes; they are not a formal proof-assistant development and are not used to infer universality.

## Final adjudication

`F83-RIN-NEW`, restated as F84-RIN, is **PROVED by fresh review**. The assembled exact `QSAT_{2,3DNF} <=_m Eff-Preserve` reduction is **PROVED by fresh review**. The unchanged exact `CIRCDIST.cplx.sigma2` claim is fully entailed, and its completeness parenthetical is valid with the current independently PROVED `CIRCDIST.cplx.upper` premise.

Apply only the complete replacement YAML in section 13, then mechanically regenerate derived views and settle operations state in a later authorized canonical task. Do not promote `CIRCDIST.cplx` without its own later fresh composition review.
