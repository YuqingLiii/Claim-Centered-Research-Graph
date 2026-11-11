# CIRCDIST.cplx.sigma2 Round 83 exact review and RIN attack

**Date:** 2026-08-30 (America/New_York)  
**Role:** sole fresh strict-serial independent reviewer and RIN attacker  
**Reviewed object:** circdist/artifacts/circdist_cplx_sigma2_r5_deep_seed_round82_20260830.md  
**Reviewed seal:** 90,435 bytes; SHA-256 6994d8a62f38e684cdbdc61cf79b9ce1d64108e07430f19aeb8c952935c418a2  
**Independence:** I did not contact the Round-82 author, did not receive or rely on that author's private reasoning, used no sub-agent, and reconstructed the arguments from the durable record and frozen definitions.  
**Canonical-write boundary:** this report is the only durable path written by Round 83. Canonical proof-DAG nodes, generated views, protocols, the scheduler, and all reviewed artifacts remained read-only. No commit or push was made.

## Executive verdict

The Round-82 artifact is mathematically stronger than its OPEN verdict, but its status restraint was correct.

1. I independently confirm the normalized grouped QSAT encoding, abstract flagged quantifier equivalence, affine-plane dictionary, local-plane counterexample, full-kernel quotient, scoped anchor no-gos, cluster expansion, exact grid/direct-sum promise repair, Gaussian-order counterexample, failed triangle/shield repairs, deterministic fixed-coordinate RREF compiler, bookend suffix-marker lemma, and sharp \(K+1\) lower bound. These are findings about unchanged Round-82 content.
2. I found two repairable reporting defects: two hashed RIN outputs contain wall-clock time and therefore do not reproduce byte-for-byte; and the statement that a dense explicit matrix encoding has size \(O(s^3)\) is false. Dense encoding can be \(O(s^4)\), while sparse support-list encoding is \(O(s^3)\). Polynomiality is unaffected.
3. I found a complete proof of the Relation/Interval Normal-Form lemma. The proof is simpler and stronger than interval pairing: zero slack plus the independent plane-private coordinates force every equality-case nonanchor fault to be an intended hook already. Cross-row cancellation cannot create a counterfeit option.
4. The RIN proof is **NEW ROUND-83 AUTHOR CONTENT**. This report cannot independently review its own new mathematics. Under DAG_PROTOCOL.md, neither RIN, the resulting hardness reduction, the hierarchy-hardness claim, nor the target node is licensed for canonical promotion by this report. A later fresh adversarial reviewer must review the RIN proof and the assembled chain.
5. The current node must remain **OPEN**. That is the exact licensed/nonlicensed delta.

Stable findings are:

- **F83-BIND:** protected-input binding and disk-wins adjudication.
- **F83-R82-CLEAR:** independent confirmation of the listed unchanged Round-82 lemmas and scoped refutations.
- **F83-SEAL-DEFECT:** nondeterministic elapsed time inside two hashed stdout records.
- **F83-SIZE-REPAIR:** dense-size exponent correction \(O(s^3)\to O(s^4)\), without loss of polynomiality.
- **F83-RIN-NEW:** complete new zero-slack/private-coordinate proof of RIN; fresh review required.
- **F83-NO-PROMOTION:** no hardness, completeness, root inheritance, or canonical edit is licensed here.

## 1. Bound inputs, disk truth, and protocol effect

### 1.1 Complete input ledger

Every file below was read in full as bytes and UTF-8 text. YAML files were also parsed with Python yaml.safe_load. The primary artifact and every Round-82 section-1 mathematical input matched the Round-82 binding. The scheduler changed only because Round 83 was subsequently authorized; current disk wins.

| path | current bytes | current lines | current SHA-256 | adjudication |
|---|---:|---:|---|---|
| DAG_PROTOCOL.md | 15,377 | 283 | d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095 | exact Round-82 match |
| FILE_PROTOCOL.md | 8,523 | 166 | d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595 | exact match |
| operations/circdist/README.md | 1,507 | 26 | d4bc4a7415344a1577a45f7277f71eef914f26203dfad5a71ef7065fa2995e12 | current operations protocol |
| operations/circdist/SCHEDULER.yaml | 197,830 | 2,491 | cc1b992cd4bb3cd6cbbdc38f324498c7d57ff118ed2de01fd2ac4b9359a14a29 | expected post-Round-82 drift; parsed |
| circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md | 10,199 | 243 | 5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64 | exact match |
| circdist/proof-dag/PROJECT.yaml | 107 | 7 | c65a2cc0c65576dfdcaf6fbc787762708fe78b8b75daa440765ac08b1ba40d0d | exact match; parsed |
| circdist/proof-dag/nodes/CIRCDIST.cplx.sigma2.yaml | 3,885 | 48 | 89e2f92228c1a886636b807e8d838c3155d3029b7eca4a8d5cd3ba03dd97c791 | exact match; parsed; OPEN |
| circdist/artifacts/circdist_cplx_sigma2_20260822.md | 52,264 | 934 | b45e9803f717b0572521eda4877d290acec806433e7c16b2b2ef4daec1576e31 | exact match |
| circdist/artifacts/circdist_cplx_q1_20260822.md | 40,756 | 770 | 28868e047511c2300356c3e0a15a09a42f422dcef65a056b7ddd2bbb214d2890 | exact match |
| circdist/artifacts/circdist_cplx_sigma2_covering_radius_primary_source_20260826.md | 42,975 | 642 | 396216942cc18c2b06e61d7ed9fb220f164d0682d15e5bcf87eb6cfea8fa5958 | exact match |
| circdist/proof-dag/nodes/CIRCDIST.cplx.upper.yaml | 5,453 | 80 | 47260df53e4491c86e10f6ccdebadf47b1161d2533339fd9c499f389a8eb2321 | exact match; parsed |
| circdist/reviews/circdist_cplx_upper_membership_exact_review_20260828.md | 52,336 | 875 | 5e593a927d7ad55966b2362d721f98c7d5dab75c30b334edede81bda4ccbac70 | exact match |
| circdist/proof-dag/nodes/CIRCDIST.cplx.fixed-d.yaml | 9,392 | 151 | 024a6d6d7d9a656c5ede53043b64601f13023fe0adbec6fe066ae67fb8303bbf | exact match; parsed |
| circdist/reviews/circdist_cplx_fixed_d_private_sentinel_exact_review_20260829.md | 46,380 | 947 | e91f7290d5ffab53347fe0bfc477954c087895e133b9234539f120422092cddd | exact match |
| circdist/artifacts/circdist_cplx_fixed_d_x_reduction_round64_20260828/README.md | 20,689 | 357 | 0606b8b6377fae42a20f606250f7186258cccbd9d04aa7a4ca288cd6371639b5 | exact match |
| circdist/artifacts/circdist_cplx_fixed_d_z_companion_round66_20260829/THEOREM.txt | 1,000 | 1 | 0b184c505c31760d7f333fdba019ea583c7686d55ab5796d126eb0dc2857f6ee | exact match |
| Round-82 primary artifact | 90,435 | 1,669 | 6994d8a62f38e684cdbdc61cf79b9ce1d64108e07430f19aeb8c952935c418a2 | exact commissioned seal |

Round 82 bound the then-current scheduler at 193,886 bytes, 2,448 lines, SHA-256 83c0adad8f500075e93d151130783a559e61b15bd068d195816c86e3f8e9332a. The current scheduler contains the Round-83 authorization, budget 108/109 pending settlement, and the explicit instruction that a new RIN proof cannot self-license promotion. This is ordinary later control-plane drift, not protected-input corruption.

### 1.2 Protocol consequences

DAG_PROTOCOL.md requires a fresh independent adversarial review before completion-level promotion. It also distinguishes a reviewed implication from unresolved premises and forbids propagation from OPEN premises. FILE_PROTOCOL.md makes the node YAML authoritative and the review report immutable evidence. The current canonical claim is:

> Eff-Preserve with d as part of the input is Sigma_2^P-hard (hence, with CIRCDIST.cplx.upper, Sigma_2^P-complete).

Its level is OPEN. The historical Q1 Seed Barrier and covering-radius source gap remain correctly scoped and are not premises of the direct construction. CIRCDIST.cplx.upper supplies independently reviewed membership only. CIRCDIST.cplx.fixed-d supplies a separate fixed-\(d\) theorem only. Neither can supply hardness by inheritance.

## 2. Frozen model reconstructed

All spaces are over \(\mathbb F_2\). For a CSS pair,

\[
S_X=\operatorname{row}H_X,\quad N_X=\ker H_Z,\qquad
S_Z=\operatorname{row}H_Z,\quad N_Z=\ker H_X.
\]

The static sector distances are the minimum Hamming weights in \(N_X\setminus S_X\) and \(N_Z\setminus S_Z\), with an empty logical sector interpreted as infinity.

For an ordered check \((q_1,\ldots,q_w)\), one same-sector extraction fault can leave a singleton or a proper suffix. Let \(\Gamma_X(M)\) and \(\Gamma_Z(M)\) contain all indexed singleton and proper-suffix locations. Distinct locations remain distinct even if their physical residuals or quotient labels agree. An \(X\)-fault selector \(f\) is bad exactly when

\[
H_Z\Gamma_X f^T=0,\qquad \Gamma_Xf^T\notin S_X,
\]

and similarly for \(Z\). Since singleton locations are present, \(d_{\rm eff}(M)\le d_{\rm static}\). On the promise \(d_{\rm static}=d\), preservation is exactly the absence of a bad set of fewer than \(d\) indexed faults. With no optional depth bound, serializing all checks realizes any tuple of allowed local orders under the derived qubit-sharing conflict relation.

This agrees with the reviewed upper-membership interface. No static-distance oracle is imported into the verifier or the reduction.

## 3. Grouped QSAT encoding and constants

### 3.1 Source form and normalization

Use the standard \(\Sigma_2^P\)-complete form

\[
\exists x_1\cdots x_p\ \forall y_1\cdots y_q\ \Phi(x,y),
\]

with \(\Phi\) a 3DNF. Equivalently \(\psi=\neg\Phi\) is a CNF with clauses of width at most three. This source form follows by complementing the standard \(\forall\exists\)-3CNF form.

Normalization is truth preserving:

- collapse repeated equal literals inside a clause;
- delete a clause containing both signs of one variable, because it is tautological;
- delete quantified variables with no remaining occurrence;
- if an empty clause remains, \(\psi\) is false and \(\Phi\) is true;
- if no clauses remain, \(\psi\) is true and \(\Phi\) is false.

Thus each nonconstant clause is nonempty, has no repeated variable, and every retained variable occurs.

### 3.2 Grouped Representation Theorem

Let \(K=p+q+m\). Give each variable \(v\) a marker \(g_v\), each clause \(C_j\) a marker \(g_j\), and each literal occurrence \((j,r)\) a coordinate \(e_{j,r}\). Define

\[
V_{v,b}=g_v+b\sum_{(j,r):v_{j,r}=v}e_{j,r}
\]

and, for every locally satisfying assignment \(a\) of \(C_j\),

\[
A_{j,a}=g_j+\sum_r a(v_{j,r})e_{j,r}.
\]

Let

\[
\tau=\sum_v g_v+\sum_jg_j.
\]

For a fixed existential schedule \(\alpha\), the available catalogue contains only \(V_{x,\alpha_x}\) in each existential group, both universal value columns, and all locally satisfying clause columns.

If at most \(K\) columns sum to \(\tau\), every one of the \(K\) marker coordinates has odd parity. At least one column must come from every group; the budget therefore forces exactly one per group. At occurrence \((j,r)\), the selected variable bit and clause-local bit must agree. All clause-local choices are consequently restrictions of one global assignment \((\alpha,\beta)\), and each satisfies its clause. Conversely a satisfying global assignment selects exactly one column per group and cancels every occurrence coordinate twice. Therefore

\[
\tau\text{ has an available representation of weight }\le K
\iff
\exists\beta\ \psi(\alpha,\beta).
\]

The construction uses \(K+L\) coordinates with \(L\le3m\), and at most \(2(p+q)+7m\) abstract columns.

### 3.3 Flagged abstraction

Add a flag coordinate \(\ell\) and the anchor

\[
h=(\tau,1).
\]

With one anchor location, a pure flag \((0,1)\) of weight below \(d_0=K+2\) exists exactly when \(\tau\) has a representation of weight at most \(K\). Hence

\[
\exists\alpha\ \forall F,\ |F|<K+2:\ F\text{ is not a flagged relation}
\iff
\exists\alpha\ \forall\beta\ \Phi(\alpha,\beta).
\]

This is an exact abstract quantifier equivalence. It does not use seed depth or covering radius.

### 3.4 Constant outputs

For an empty clause in \(\psi\), the QBF is YES and the \(d=2\) safe grid of section 5 is a promised YES instance.

For no clauses, the QBF is NO. On four qubits,

\[
H_Z=\begin{pmatrix}1&1&1&1\\0&0&1&1\end{pmatrix},\qquad
H_X=\begin{pmatrix}1&1&1&1\end{pmatrix}.
\]

Both static sector distances are two. The sole \(X\)-row order \((2,3,0,1)\) has middle proper suffix \(\{0,1\}\), a weight-two static logical produced by one fault. Thus \(d_{\rm eff}^X=1<2\). The embedded constant-instance audit reproduced this exactly.

## 4. Affine planes, quotient compilation, and scoped failures

### 4.1 Four-qubit plane

For payloads \(a,b\) and private coordinate \(p\), use columns

\[
q_0=p,\quad q_1=p+a,\quad q_2=p+b,\quad q_3=p+a+b.
\]

Their sum is zero. In order \((q_2,q_3,q_0,q_1)\), the length-two suffix is \(a\); in order \((q_1,q_3,q_0,q_2)\), it is \(b\). Length-one suffixes are singletons, and length-three suffixes are singleton complements modulo the full-plane row.

A selector plane takes \(a=V_{x,0}\), \(b=V_{x,1}\). A fixed plane for payload \(a\) uses \(b=r\), with a fresh private coordinate \(r\), and only the \(a\)-order.

### 4.2 Why local planes alone fail

If only full-plane rows are stabilized, an anchor-free homogeneous relation among hook payloads is a new logical rather than a stabilizer. For

\[
\psi=x\wedge(y\vee z\vee w)
\]

the true QBF branch \(x=0\) has the four-fault zero relation

\[
V_{y,0}+V_{y,1}+A_{1,(0,0,1)}+A_{1,(0,1,1)}=0.
\]

The plane-gate replay found this relation for both schedules. Four hook faults are below \(d=8\), while the same relation made from physical singleton pairs has weight eight. This precisely refutes the undersized quotient.

### 4.3 Full-kernel compiler

Let \(B\) be the matrix of all full physical labels, including \(\ell\), and let \(S\) delete the flag row. Set

\[
H_Z=S,\qquad \operatorname{row}H_X=\ker B.
\]

Then \(H_XH_Z^T=0\), and

\[
k=n-\operatorname{rank}H_X-\operatorname{rank}H_Z
 =\operatorname{rank}B-\operatorname{rank}S\in\{0,1\}.
\]

When the flag row is independent, \(k=1\); an \(X\) vector is the nontrivial logical exactly when its full label is \((0,1)\). The nontrivial \(Z\) coset is the flag row modulo \(\operatorname{row}S\), so

\[
d_Z=\operatorname{dist}(\ell,\operatorname{row}S).
\]

The replayed 64-qubit example had \(\operatorname{rank}B=42\), \(\operatorname{rank}H_Z=41\), \(\operatorname{rank}H_X=22\), and \(k=1\).

### 4.4 Static \(X\) bound

A zero-nonflag-syndrome physical vector has even parity in every plane's \(p\) coordinate. In a fixed plane, the private \(r\) coordinate reduces a nonzero payload coefficient modulo the full-plane row to a two-qubit pair. A selector coefficient likewise costs at least two qubits.

A pure flag needs an odd anchor payload coefficient. That contributes every group marker, so the other coefficients must have odd total marker in all \(K\) groups. Every nonanchor payload coefficient has marker weight at most one. At least \(K\) nonanchor coefficients plus the anchor coefficient are needed, each at physical cost two:

\[
d_X\ge2(K+1)\ge K+2.
\]

If the flag row is dependent, the flagged logical sector is empty and the bound is vacuous in the correct direction.

### 4.5 Anchor dual no-gos

With one anchor plane, the physical flag row has weight two. If it is independent,

\[
d_Z=\operatorname{dist}(\ell,\operatorname{row}S)\le2.
\]

For an all-or-none coefficient code \(\ker G=\operatorname{span}\{c\}\) and a flag vector \(f\) satisfying \(f\cdot c=1\), one has \(\operatorname{row}G=c^\perp\). For any \(i\in\operatorname{supp}c\),

\[
(f+e_i)\cdot c=0,
\]

so \(\operatorname{dist}(f,\operatorname{row}G)=1\). The affine physical realization doubles this to at most two. This is a scoped obstruction to that replication pattern, not to arbitrary encoded flags.

## 5. Cluster expansion and exact promise repair

For a CSS code on \(n\) qubits, replace each qubit \(q\) by \(R\) copies. Add \(X\) equality rows between adjacent copies, lift each old \(X\) row to layer zero, and repeat each old \(Z\) row across all layers.

The equality rows are independent and commute with repeated \(Z\) rows. Rank counting gives

\[
\operatorname{rank}H_X^{(R)}=n(R-1)+\operatorname{rank}H_X,\qquad
\operatorname{rank}H_Z^{(R)}=\operatorname{rank}H_Z,
\]

so \(k\) is preserved.

Let \(\pi\) record parity in each copy block. Equality stabilizers move any \(X\) vector to layer zero and identify exactly vectors with the same \(\pi\). Therefore

\[
d_X^{(R)}=d_X.
\]

A \(Z\) normalizer must be constant across every copy block, and repeated old \(Z\) rows identify exactly the old stabilizer cosets. Hence

\[
d_Z^{(R)}=R\,d_Z.
\]

For the \(X\) fault catalogue, equality-check suffixes are singletons and every copied singleton is equality-equivalent to its layer-zero version. Lifted old checks have the old order. Mapping any expanded fault set through \(\pi\), then cancelling duplicate old locations if necessary, cannot increase its weight and preserves nontriviality. Conversely every old witness lifts. Thus

\[
d_{\rm eff}^{X,(R)}=d_{\rm eff}^X.
\]

For repeated \(Z\) rows, use layer-major order. In

\[
Q=\mathbb F_2^n/\operatorname{row}H_Z,
\]

one fault has a possibly nonzero class in at most one layer: later complete old-row pieces vanish in \(Q\). A repeated nontrivial \(Z\) logical has the same nonzero class in all \(R\) layers. Fewer than \(R\) faults cannot produce it, so

\[
d_{\rm eff}^{Z,(R)}\ge R.
\]

On \(d\) base qubits with no \(X\) rows and adjacent-pair \(Z\) rows, apply \(R_d\). The resulting \(d\times d\) grid has \(d_X=d_Z=d\), \(d_{\rm eff}^X=d\), and \(d_{\rm eff}^Z=d\). The blocked-order negative control correctly gives \(d_{\rm eff}^Z=1\); alternating/layer-major order gives exactly \(d\) for \(d=2,3,4\).

Apply \(R_d\), \(d=K+2\), to the flagged compiler and direct-sum the grid. The flagged block has both static sectors at least \(d\), its \(Z\) effective distance is at least \(d\), and its \(X\) effective problem is unchanged. The grid pins the total static distance to exactly \(d\) and supplies \(d_{\rm eff}\le d\). On a safe flagged schedule the total effective distance is exactly \(d\); on an unsafe one it is below \(d\). Direct-sum minima introduce no cross-block shortcut. Serial scheduling makes every emitted local-order tuple legal.

## 6. Frozen systematic compiler and the \(K+1\) theorem

For selector \(i\), let \(\delta_i=V_{x_i,0}+V_{x_i,1}\) and lift it by the pair \(\{q_0,q_3\}\). For fixed nonanchor plane \(j\), orient its payload pair as

\[
u_j=q_0,\qquad v_j=q_1.
\]

The anchor coefficient is zero in every homogeneous relation because its flag is unique.

Let \(D\) have selector-difference columns followed by fixed payload columns in the recorded order, with the anchor last. Its relation space is \(R=\ker D\). Projection from \(R\) to fixed coordinates is injective: a relation supported only on selector differences is a sum of occurrence vectors of distinct existential variables; their nonempty supports are pairwise disjoint after normalization.

RREF on fixed coordinates from left to right therefore supplies one distinct fixed pivot per relation row,

\[
r_i=e_{p_i}+\sum_{j\in S_i}e_j,
\]

and every pivot is absent from every other basis row. Lifting selector coordinates by \(\{q_0,q_3\}\) and fixed coordinates by \(\{q_0,q_1\}\), together with full-plane rows, spans exactly \(\ker B\).

The bookend order is:

1. pivot \(u\);
2. all selected selector endpoints and nonpivot fixed \(u\)'s;
3. nonpivot fixed \(v\)'s in group blocks, pivot group last;
4. pivot \(v\).

All early endpoints have group marker zero. The late endpoint \(v_j\) has the unit marker of its fixed payload group. Since a homogeneous relation has even fixed-payload parity in every group, all late markers sum to zero. A proper suffix beginning in the early zone therefore has marker zero. A suffix beginning in the late zone lies in one partial group block followed by complete even blocks, so its marker weight is at most one.

Every nonanchor singleton and local-plane suffix also has marker weight at most one. Every flag-one anchor-plane location has marker \(\tau\). If a pure-flag mechanism has \(t\) flag-one faults, then \(t\) is odd and their group projection is \(\tau\). The flag-zero faults must sum to \(\tau\), whose marker weight is \(K\), and each contributes marker weight at most one. Thus there are at least \(K\) flag-zero faults and \(t\ge1\) flag-one fault:

\[
|F|\ge K+1.
\]

At equality, \(t=1\), there are exactly \(K\) flag-zero faults, every one has marker weight one, and their marker groups are all distinct. Every marker-zero fault is excluded by zero slack.

The sole flag-one fault cannot be the anchor \(q_1=p+h\) or \(q_3=p+r+h\): no one of the \(K\) unit-marker nonanchor faults carries either anchor-private coordinate, and complement rows exclude the anchor plane. It is therefore the length-two anchor hook \(h\).

These arguments independently confirm Round-82 Lemmas 8.1, 8.2, and Theorem 8.3.

## 7. RIN attack

### 7.1 Counterexample-first decision trail

The natural attack is an odd clause-option XOR. For a width-three OR clause, three satisfying local assignments can XOR to the unique falsifying assignment. The smallest explicit source-safe attempt was

\[
C_0=(x=0\vee y=0\vee z=0),\quad C_1=(y=1),\quad C_2=(z=1),
\]

at schedule \(x=1\). Abstractly, three allowed \(C_0\) options can counterfeit \((1,1,1)\). The exact frozen compiler had no equality solution; its peak DP layer was 19,440.

I then tested all order-sensitive formulas consisting of one width-three clause and two unit clauses, and a repeated-wide-clause family designed to force shared nonpivot planes. I also tested two existential variables. No counterexample appeared. These computations were used only to locate an invariant.

| Round-83 search | scope | source-safe schedules | peak states | result |
|---|---:|---:|---:|---|
| final frozen v3/e1/m3 | 16,064 normalized formulas; 32,128 schedules | 5,496 | 1,093,100 | zero counterexamples |
| final frozen v3/e2/m2 | 496 formulas; 1,984 schedules | 408 | 35,312 | zero |
| v3/e2/m3 random, seed 8303 | 909 normalized formulas; 3,636 schedules | 1,432 | 1,077,144 | zero |
| one wide + two unit, all permutations | 864 formulas; 1,728 schedules | 768 | 23,004 | zero |
| repeated wide + two unit, all permutations | 1,728 formulas; 3,456 schedules | 1,536 | 699,192 | zero |
| v4/e1/m3 random, seed 8302 | 220 normalized formulas; 440 schedules | 15 | 1,153,728 | zero |

Absence in these searches is NUMERICAL. The proof below is not inferred from absence.

### 7.2 Complete indexed fault taxonomy

Fix a nonconstant normalized formula, schedule \(\alpha\), and equality-case mechanism after removing the anchor hook. Let \(p_x\) denote a selector plane's private coordinate. For a fixed nonanchor plane \(j\), let \(p_j,r_j\) be its private coordinates, \(a_j\) its intended payload, and

\[
v_j=p_j+a_j.
\]

All statements below concern indexed locations; equal labels do not identify locations.

#### Selector plane

The four singleton labels are

\[
q_0=p_x,\quad q_1=p_x+a_0,\quad q_2=p_x+a_1,\quad q_3=p_x+a_0+a_1.
\]

The first and fourth have marker zero; the middle two have the selector's unit marker. Under schedule \(\alpha\), the three proper suffixes by increasing suffix length are

\[
p_x+a_\alpha,\qquad a_\alpha,\qquad p_x+a_{1-\alpha}.
\]

Thus the only unit-marker selector locations are the intended scheduled hook \(a_\alpha\) and broken entries carrying \(p_x\).

#### Fixed nonanchor plane

The four singleton labels are

\[
q_0=p_j,\quad q_1=v_j,\quad q_2=p_j+r_j,\quad q_3=v_j+r_j.
\]

Its proper suffixes by increasing suffix length are

\[
v_j,\qquad a_j,\qquad p_j+r_j.
\]

The unit-marker locations are the intended hook \(a_j\), the broken entry \(v_j\), and the broken singleton \(v_j+r_j\). All other local entries have marker zero.

#### Anchor plane

With \(h=(\tau,1)\), its singletons are \(p\), \(p+h\), \(p+r\), \(p+r+h\). Its proper suffixes by increasing length are

\[
p+h,\qquad h,\qquad p+r.
\]

The flag-one entries have marker \(\tau\); the flag-zero entries have marker zero. Section 6 shows that zero slack leaves only \(h\).

#### Complement row

Every early endpoint is marker-zero: selector pairs use \(q_0,q_3\), and fixed \(u\)'s are \(q_0\). Every late endpoint is a fixed \(v_j=q_1=p_j+a_j\). All late markers XOR to zero.

A suffix starting in the early zone includes all late markers and hence has marker zero. Consequently every marker-one complement suffix starts strictly inside the late zone and is exactly

\[
\bigoplus_{j\in J}v_j
\]

for a suffix set \(J\) of fixed planes. It contains no selector endpoint, no \(r_j\), and no anchor endpoint. Repeated check rows, repeated suffixes, or equal labels do not alter this indexed identity.

This taxonomy exhausts physical singletons and every proper suffix of every measured \(X\) check.

### 7.3 F83-RIN-NEW — zero-slack/private-coordinate theorem

**Status: AUTHOR-PROVED-BUT-UNREVIEWED.**

**Theorem (RIN, new Round-83 content).** For every normalized nonconstant QSAT formula, every existential schedule \(\alpha\), and the frozen affine-plane/full-kernel compiler using the deterministic fixed-coordinate RREF basis and group-block bookend orders, every indexed solution of (8.3) consists of the scheduled existential hook, one intended universal-value hook per universal group, and one intended locally satisfying option hook per clause group. In particular it yields a global \(\beta\) with \(\psi(\alpha,\beta)=1\). Equivalently, every \(K\)-column nonanchor equality solution normalizes with no budget increase to the \(K\) intended hooks; here no replacement is needed.

**Proof.**

By the equality analysis in section 6, after removing the unique anchor hook there are exactly \(K\) indexed faults, each has marker weight one, and their marker groups are all distinct. No marker-zero location is present.

A broken selector entry carries \(p_x\). No marker-one complement suffix contains a selector endpoint. No other local plane contains \(p_x\), and only one fault can be selected in the existential group. Hence \(p_x\) could not cancel. Every existential fault is therefore the private-free scheduled hook \(a_\alpha\).

A fixed-plane singleton \(v_j+r_j\) contains the unique \(r_j\). Complement suffixes use only \(q_1=v_j\), intended hooks contain no private coordinate, and every other \(r_j\)-carrying local entry has marker zero. Hence \(v_j+r_j\) cannot occur.

Let \(N\) be the remaining nonintended fixed-group faults. Every \(f\in N\) is either a local \(v_j\) or a marker-one complement suffix. By the taxonomy, there is a set \(J_f\) of fixed planes such that

\[
\lambda(f)=\bigoplus_{j\in J_f}v_j
          =\bigoplus_{j\in J_f}(p_j+a_j). \tag{7.1}
\]

All other selected locations now known to be possible—the anchor hook, scheduled selector hooks, and intended fixed hooks—have zero coefficient on every fixed-plane \(p_j\). The aggregate residual has zero private syndrome. Therefore, for every fixed plane \(j\),

\[
\bigoplus_{f\in N}\mathbf 1[j\in J_f]=0. \tag{7.2}
\]

The coefficient of the whole vector \(v_j=p_j+a_j\) in the XOR of (7.1) is the same even coefficient detected by the independent coordinate \(p_j\). Hence every whole \(v_j\), including its payload part, cancels. Equations (7.1) and (7.2) give

\[
\bigoplus_{f\in N}\lambda(f)=0. \tag{7.3}
\]

This remains true when different indexed suffixes have the same label or the same set \(J_f\): the same indexed location cannot be chosen twice because (8.3) is Boolean, while distinct indexed contributions are counted modulo two in (7.2). The independent coordinate \(p_j\) records exactly that parity, even when several distinct suffixes contribute the same \(v_j\)-combination.

On the other hand, each \(f\in N\) has one unit group marker \(g_{G(f)}\). Equality selects one fault per group, so the groups \(G(f)\) are pairwise distinct. Projecting (7.3) to group-marker coordinates gives

\[
\bigoplus_{f\in N}g_{G(f)}=0.
\]

Distinct standard basis vectors have zero XOR only for the empty set. Hence \(N=\varnothing\).

Every nonanchor fault is therefore an intended hook. Existential hooks respect \(\alpha\); a universal hook chooses a bit \(\beta_y\); and every clause hook is one of the emitted locally satisfying assignments. Since the \(K\) hook labels sum to \(\tau\), every occurrence coordinate \(e_{j,r}\) has parity zero:

\[
\beta_{v_{j,r}}+a_j(v_{j,r})=0.
\]

Thus every local assignment is the restriction of the single global assignment \((\alpha,\beta)\), and it satisfies its clause. Therefore \(\psi(\alpha,\beta)=1\). No replacement and no budget increase are needed. ∎

This proof directly covers:

- repeated suffixes and repeated check rows;
- different rows sharing nonpivot planes;
- arbitrary cross-row cancellation on those planes;
- odd XORs of multiple allowed clause options;
- every fixed-coordinate RREF pivot choice produced by the frozen algorithm;
- selector, pivot, and anchor private coordinates;
- every normalized nonconstant formula and any number of existential or universal variables;
- indexed rather than label-collapsed fault sets.

The proof uses RREF only through the already reviewed bookend structure and marker bound. It does not assume the finite census.

### 7.4 Both truth directions and the assembled conditional chain

If \(\psi(\alpha,\beta)=1\), choose the scheduled existential hooks, the \(\beta\)-value universal hooks, the restrictions of \((\alpha,\beta)\) in every clause plane, and the anchor hook. Their \(K+1\) labels XOR to the pure flag, so \(d_{\rm eff}^X\le K+1<d=K+2\).

Conversely, any sub-\(d\) bad mechanism has at least \(K+1\) faults by the reviewed lower bound. At equality, the anchor analysis and F83-RIN-NEW give intended hooks and hence a satisfying \(\beta\). Therefore, subject to fresh review of the new proof,

\[
\text{flagged block safe for schedule }\alpha
\iff
\forall\beta\ \Phi(\alpha,\beta).
\]

Taking the existential schedule choice, applying the cluster expansion, and adjoining the exact grid gives the desired total promise-preserving reduction. This is a complete author-level chain, but it is **not independently licensed in Round 83** because its first new premise, RIN, was authored here.

## 8. Other adversarial checks

### 8.1 Gaussian/increasing-order false shortcut

For

\[
\psi=(x=0\vee y=0)\wedge(x=0\vee y=1)
\]

and schedule \(x=1\), no universal \(y\) satisfies \(\psi\). The Gaussian/increasing compiler nevertheless has the five labels

\[
0x004,\ 0x008,\ 0x051,\ 0x052,\ 0x10f.
\]

Their XOR is exactly \(0x100\), the flag bit:

\[
0x004\oplus0x008\oplus0x051\oplus0x052\oplus0x10f=0x100.
\]

Thus five faults violate \(d=6\). The exact embedded harness reproduced the 40-qubit instance, two complement rows of weights 12 and 14, and this witness. The failure is scoped to Gaussian/increasing order; the bookend proof does not use that order.

### 8.2 Triangle splitting

For \(b_1=e_1,b_2=e_2,b_3=e_3,b_4=e_1+e_2+e_3\), the original relation has weight four. An anchor with syndrome \(e_1+e_2\) needs the anchor plus two \(b\)'s. Splitting through \(a=b_1+b_2\) exposes \(a\) as a check-prefix/hook label, and anchor plus \(a\) is a two-fault pure flag. A freely independent marker cannot be attached to that prefix without changing the check complex. The stated naive split is refuted.

### 8.3 Private-circuit shield

Replacing a complement row \(r\) by \(r+m\), where \(m\) is a rank-\(L-1\) marker circuit on \(L\) new qubits, introduces one logical dimension unless the marker-only stabilizer is also added. If it is added, a suffix of \(r+m\) and the matched suffix of \(m\) cancel the marker in two faults and recover the old suffix. This directly refutes the stated shield, not every possible encoded shield.

### 8.4 Polynomial size correction

Let \(s=p+q+m\). The base compiler has \(O(s)\) qubits, rows, and label coordinates; \(d=O(s)\). Cluster expansion and the grid have \(O(s^2)\) qubits and \(O(s^2)\) \(X\) rows. In sparse support-list form, the emitted supports and order lists use \(O(s^3)\) bits/indices.

A dense \(H_X\) with \(O(s^2)\) rows and \(O(s^2)\) columns can require \(O(s^4)\) bits. Therefore Round-82 section 9's phrase “even a dense explicit bit-matrix/order-list encoding is \(O(s^3)\)” is false. Replace it by:

> A sparse support-list encoding is \(O(s^3)\); a dense rectangular check-matrix encoding is at worst \(O(s^4)\). Both are polynomial.

No correctness or many-one polynomiality claim depends on the cubic exponent.

## 9. Embedded harness replay and seal audit

### 9.1 Source extraction

The seven Python listings were extracted directly from the sealed Markdown by section boundaries. Their hashes all match the Round-82 table.

| listing | bytes | SHA-256 |
|---|---:|---|
| abstract_census.py | 3,958 | 4e6c8ebb42213781cbb3918cc344896ce696843cd7ad91d5e45d301430a65a7d |
| plane_gate.py | 4,446 | 3db3a931ca6c8e58e34fdb42ef1e788be4d4ff4b19ebb47ab6c571c3807df182 |
| compiler_audit.py | 6,616 | d090a4682ea3f23e756deb40ee4ee681ae0c5b82626c5de16498851e2e987dd1 |
| grid_block_audit.py | 1,711 | 106e7a3eaf6fa3da81d014da104288a2dfee3a079dd3b867603f2023b1333bb1 |
| rin_xor_csp_search.py | 13,171 | ef80e03c9bcd49edecef30400bd08bbe745aa02984a713ef638fa0e653643cc4 |
| kernel_shortcut_witness.py | 5,200 | 465623e89e53e4f6f2c583d1867b6688e7e4982908741c5f1bdc3ad04d36ad2d |
| constant_instance_audit.py | 864 | 5d0628b72f4e43b12bfddd360d7a98f099dbdff7e8dc26bbe0b9c0d780b472e5 |

The first extraction parser was defective: its permissive regular expression skipped every other heading and associated four listings with the wrong names. It exited 1 on an explicit section-number assertion. Those scratch files were deleted and re-extracted by bounded section spans. This failure changed no repository byte and is included in the FIX-2 ledger.

### 9.2 Exact results

Every harness exited 0 on the corrected extraction. The mathematical outputs reproduced:

- 702 abstract formulas, 1,404 schedules, zero abstract/flagged mismatches, 1,388 naive shortcuts, 136 source-safe false-NO schedules;
- the exact four-hook homogeneous relation;
- ranks \(42,41,22\), \(k=1\), and flag-row weight two;
- exact full-kernel minima: safe \(x=0\) none through seven, unsafe \(x=1\) minimum seven;
- grid blocked order one versus alternating/layer-major distances \(2,3,4\);
- constant instance \(d_X=d_Z=2\) and one-fault bad suffix;
- Gaussian false shortcut of weight five;
- all four final frozen RIN census counts and zero counterexamples.

The final validation reran the seven programs strictly serially. The six programs without an elapsed field reproduced their earlier stdout byte-for-byte. All four invocations of the one parameterized RIN program reproduced the same deterministic semantic projection; only their wall-clock fields changed. Every serial command exited 0.

The output-hash comparison was:

| output | Round-82 SHA | Round-83 SHA | result |
|---|---|---|---|
| abstract_census.out | 4e41f9f2a9aab2a73c84e0366abb3c91628717d8c7a6fec2b16dfaf595ffaf55 | same | exact |
| plane_gate.out | 4f52bdf05928cffaad1d627566efb387f19ee00ac7adf1856ed5a3406333b1c1 | same | exact |
| compiler_audit output | 829599ef115ddfc4a1fa28b9db9650a784f43652a313abe91c2d6b78a2868671 | same | exact |
| grid_block_audit.out | 0faff3eea85e529322b9f8d384449a420ccf08b40e2984b8778d35eea981c7b5 | same | exact |
| constant_instance_audit.out | 21778d05637f97afe3ef56e6ac3b828dcdbc6dbf1d23570b485b8ef6e73c03b8 | same | exact |
| kernel_shortcut_witness.out | 8ebcac52bb04855a14d937c336ff3bc442325705be9d581e0e5d8d6c10977c8c | same | exact |
| RIN v2/m2 | 53eea3f5ccde44cd3d9eaf908ad254a1b56f8c293f839ea3f28a032adb264718 | same | exact |
| RIN v2/m3 | a40f522a803570d6d16e0cbac5facb2a151d9b0bd391e92c46aa1a4c89be9d72 | 7a44ba93023e40aea789d2b0faee313d94e3e6ecf6faa6a84e38996d940ccd43 | elapsed only |
| RIN v2/m4 | d664ac80dadf8673414a549079b40c700161a4082f03ea243d797f0419778f5f | 0bbfea260797c95844e1c759109b4008f205168a517bce7e535200205e74a3e4 | elapsed only |
| RIN v3/m2 | 88e2be52d968125a0ea7a1388dc4aca17b5ea377fee0d5bfd2a0818769b82507 | same | exact |

The program prints wall-clock elapsed time into stdout. Brute-forcing only that three-decimal field against the Round-82 hashes recovered the exact prior lines: elapsed 0.462 for v2/m3 and 34.721 for v2/m4. Round 83 printed 0.470 and 34.995. Every other byte was thereby proved identical.

Deterministic semantic projections delete the terminal elapsed field. Their hashes are:

| scope | semantic SHA-256 |
|---|---|
| v2/m2 | 3d7a27ce8fc738cf86a1f84beb533e6a4b74e0be093e7f3ea4434129d3847a83 |
| v2/m3 | 175419a9b70d4236f161d9da317e89928cc542187b8d3642fb1a3a7c295a6e2e |
| v2/m4 | b4855df564d63c482469c6cdc1e313ecf782a7babb5fb5eb420a66c51d2b85ab |
| v3/m2 | 1ef1b5b1234fedfc59e86fe2cfde7d05362b41b28afde1219c1b74ddcaf08f98 |

**F83-SEAL-DEFECT classification:** documentation/reproducibility defect, low mathematical severity. It affects exact stdout hash reproducibility but no formula count, safe-schedule classification, pivot/cap count, state count, witness, theorem, or protected input binding. Future harnesses should print timing to stderr and hash a deterministic semantic stdout.

The Round-82 names compiler_audit2.out although the displayed compiler_audit.py listing contains both rank and meet-in-the-middle phases. The combined displayed script reproduced the named output hash, so this is a filename-description inconsistency only.

### 9.3 Nonembedded numerical rows

The 600 random-basis/order trial and the 1,000 earlier-pivot trial were not supplied as core listings or source hashes. Their exact random counts are therefore **NOT INDEPENDENTLY REPLAYED**. They are non-load-bearing numerical context. The pre-freeze v3/m3 run used a different pivot rule and likewise remains exploratory.

Round 83 independently replaced the most relevant omission with the full final-pivot v3/e1/m3 census: 16,064 normalized formulas, 32,128 schedules, 5,496 source-safe schedules, zero pivot/cap failures, zero counterexamples, peak 1,093,100 states, SHA-256 fcb201b0e539c94e973813acb8248f2301266308c123978d17b80ae6aef4ff07.

## 10. Independent symbolic classification checks

The final taxonomy audit checked every normalized v3/e1/m3 schedule, not only source-safe schedules:

~~~text
TAXONOMY_PASS {'variables': 3, 'exists': 1, 'clauses': 3, 'width': 3,
'formulas': 16064, 'schedules': 32128, 'safe': 5496, 'rows': 174720}
COUNTS anchor_single_flag=64256 anchor_single_zero=64256
anchor_suffix_flag=64256 anchor_suffix_zero=32128
extra_suffix_unit=427416 extra_suffix_zero=1235848
fixed_single_unit=1015424 fixed_single_zero=1015424
fixed_suffix_intended=507712 fixed_suffix_v=507712 fixed_suffix_zero=507712
selector_single_unit=64256 selector_single_zero=64256
selector_suffix_broken=64256 selector_suffix_intended=32128
singleton_total=2287872
~~~

The class counts sum to 2,287,872 singleton instances and 3,379,168 proper-suffix instances. Thus the checker classified, rather than sampled, every allowed singleton and suffix type in this census.

It also checked all 1,984 v3/e2/m2 schedules and 10,368 complement rows. Script SHA-256 is 716d65aa97e75d2d9b9915e01b7b45f5aaf413f3a3c079fea1f154fa33e32fa9; stdout SHA-256 is e68f2fb8e252cbf68b9c9db4eb2694ad6ba5899d30e5f1511950859a2a9ae943.

A separate intended-direction audit constructed the actual one-per-group hooks for every source-unsafe schedule:

~~~text
INTENDED_DIRECTION_PASS variables=3 exists=1 clauses=3 width=3
formulas=16064 schedules=32128 safe=5496 unsafe=26632 intended_verified=26632
INTENDED_DIRECTION_PASS variables=3 exists=2 clauses=2 width=3
formulas=496 schedules=1984 safe=408 unsafe=1576 intended_verified=1576
~~~

Script SHA-256 is 26557c921454fb6c10b6e9b6cfbad29fd36bab4ec7504829279593ee66d42f37; stdout SHA-256 is 0a9d2d2692321f331552d2bc0706c6138496739254c480da0eb09faf71f705b9.

The first taxonomy run failed an assertion because the audit script listed forward order cuts while comparing them to increasing suffix lengths. The compiler output was correct. Reversing the expected length-one/length-three entries repaired only the independent checker. The final all-schedule run above passed.

## 11. Licensing table

| item | Round-83 adjudication | canonical consequence |
|---|---|---|
| normalized QSAT source and constants | independently confirmed unchanged Round-82 content | may cite F83-R82-CLEAR |
| Grouped Representation Theorem | independently confirmed | may cite F83-R82-CLEAR |
| abstract flagged quantifier equivalence | independently confirmed | abstract theorem only |
| affine-plane schedule dictionary | independently confirmed | local compiler fact |
| local-plane homogeneous-kernel failure | exact counterexample confirmed | scoped construction refuted |
| full-kernel quotient/rank/\(k=1\) algebra | independently confirmed | may cite |
| single-anchor and all-or-none dual no-gos | independently confirmed at stated scope | no broader no-go |
| cluster \(R_R\) theorem | independently confirmed | may cite |
| exact grid and direct-sum promise bridge | independently confirmed | may cite |
| Gaussian/increasing order | exact counterexample confirmed | that order rule refuted |
| triangle split and direct circuit shield | independently confirmed at stated scope | those repairs refuted |
| fixed-coordinate RREF/full-kernel lift | independently confirmed | may cite |
| group-block marker lemma and \(K+1\) bound | independently confirmed | may cite |
| RIN | complete proof in F83-RIN-NEW | **new author content; fresh review required** |
| total QSAT-to-Eff-Preserve reduction | complete author-level chain after F83-RIN-NEW and size correction | **not licensed here** |
| \(\Sigma_2^P\)-hardness/completeness | would follow after a fresh review of RIN and assembly with the already PROVED upper premise | **not licensed here** |
| CIRCDIST.cplx.sigma2 | must remain OPEN | no canonical edit |
| CIRCDIST.cplx root | unchanged | no inheritance |

### 11.1 Exact target for the next fresh review

The exact new statement to review is:

> **RIN theorem candidate.** For every normalized nonconstant QSAT formula, every existential schedule \(\alpha\), and the frozen affine-plane/full-kernel fixed-coordinate RREF bookend compiler, every indexed solution of (8.3) consists exactly of the scheduled existential hook, one universal-value hook for each universal group, and one locally satisfying option hook for each clause group. Consequently (8.3) has a solution if and only if there is a global assignment \(\beta\) with \(\psi(\alpha,\beta)=1\).

Round 83 assigns that statement **AUTHOR-PROVED-BUT-UNREVIEWED**, not PROVED. The next reviewer should bind this report by its final externally reported hash, audit sections 6 and 7.2--7.4 without relying on private reasoning, and check the assembly through sections 3--5 and 8.

Only if that fresh review passes, the candidate canonical delta is:

1. Add a direct grouped-QSAT/affine-full-kernel route to `CIRCDIST.cplx.sigma2`, with `CIRCDIST.cplx.upper` as the membership premise; cite the sealed Round-82 construction as proof source, this report as public new-proof source, and the later report as the independent review.
2. Record the route implication as PROVED: normalization and constant cases make the reduction total; schedules encode \(\alpha\); RIN gives the exact unsafe iff \(\exists\beta\,\psi(\alpha,\beta)\) equivalence; expansion and the grid enforce the frozen two-sector promise and legal orders; sparse size is \(O(s^3)\) and dense size is \(O(s^4)\).
3. Change only `CIRCDIST.cplx.sigma2` from OPEN to PROVED, with a review-completed event and a level-change event. Retire the obsolete DEEP-FLAG/RIN frontier for this route. Do not use the covering-radius source gap as a premise.
4. Regenerate derived views and settle the scheduler only after that canonical mutation. Do not promote the CIRCDIST classification root by inheritance; its assembled implication requires its own protocol-compliant review.

This is a delta candidate for the later reviewer/settler, not authorization from Round 83 to edit canonical state.

## 12. Reproducible commands and code

All commands below were run from the repository root unless the working directory is the named scratch root.

~~~sh
wc -c -l circdist/artifacts/circdist_cplx_sigma2_r5_deep_seed_round82_20260830.md
shasum -a 256 circdist/artifacts/circdist_cplx_sigma2_r5_deep_seed_round82_20260830.md
python3 -c 'import yaml; yaml.safe_load(open("operations/circdist/SCHEDULER.yaml"))'
/usr/bin/time -lp python3 abstract_census.py
/usr/bin/time -lp python3 plane_gate.py
/usr/bin/time -lp python3 compiler_audit.py
/usr/bin/time -lp python3 grid_block_audit.py
/usr/bin/time -lp python3 constant_instance_audit.py
/usr/bin/time -lp python3 kernel_shortcut_witness.py
/usr/bin/time -lp python3 rin_xor_csp_search.py --variables 2 --exists 1 --clauses 2 --width 2
/usr/bin/time -lp python3 rin_xor_csp_search.py --variables 2 --exists 1 --clauses 3 --width 2
/usr/bin/time -lp python3 rin_xor_csp_search.py --variables 2 --exists 1 --clauses 4 --width 2 --progress 1000
/usr/bin/time -lp python3 rin_xor_csp_search.py --variables 3 --exists 1 --clauses 2 --width 3
/usr/bin/time -lp python3 rin_xor_csp_search.py --variables 3 --exists 1 --clauses 3 --width 3 --progress 1000
/usr/bin/time -lp python3 rin_xor_csp_search.py --variables 3 --exists 2 --clauses 2 --width 3
/usr/bin/time -lp python3 rin_fault_taxonomy_audit.py
/usr/bin/time -lp python3 rin_intended_direction_audit.py
~~~

The verbatim Round-83 load-bearing audit code follows. It imports the exact sealed rin_xor_csp_search.py listing after extraction.

### 12.1 Fault taxonomy audit

~~~python
#!/usr/bin/env python3
from itertools import product
from collections import Counter
import rin_xor_csp_search as r

def xx(xs):
 z=0
 for x in xs:z^=x
 return z

def case(F,V,E,a,C):
 ans,err=r.compile_catalogue(F,V,E,a);assert err is None,err
 by,d=ans;L=d['labels'];K=d['K'];gm=(1<<K)-1;fb=1<<d['flag']
 qinfo={q:(name,qs,fixed) for name,qs,fixed in d['meta'] for q in qs}
 # All four indexed physical singletons in every plane.
 for name,qs,fixed in d['meta']:
  p=L[qs[0]]
  for pos,q in enumerate(qs):
   z=L[q];m=z&gm;fl=bool(z&fb)
   C['singleton_total']+=1
   if name==('anchor',):
    assert (pos in (1,3))==fl
    assert m in (0,gm)
    C['anchor_single_flag' if fl else 'anchor_single_zero']+=1
   elif name[0]=='select':
    assert not fl
    if pos in (1,2): assert r.pop(m)==1;C['selector_single_unit']+=1
    else: assert m==0;C['selector_single_zero']+=1
   else:
    assert not fl
    if pos in (1,3): assert r.pop(m)==1;C['fixed_single_unit']+=1
    else: assert m==0;C['fixed_single_zero']+=1
 # Every local-plane proper suffix, with exact algebraic type.
 for pi,(name,qs,fixed) in enumerate(d['meta']):
  p=L[qs[0]]
  if name[0]=='select':
   b=a[name[1]];o=[qs[2],qs[3],qs[0],qs[1]] if b==0 else [qs[1],qs[3],qs[0],qs[2]]
   intended=L[qs[0]]^L[o[-1]]
   vals=[xx(L[q] for q in o[c:]) for c in range(1,4)]
   assert vals[1]==intended and not (intended&p)
   assert vals[0]&p and vals[2]&p
   assert all(r.pop(z&gm)==1 for z in vals)
   C['selector_suffix_broken']+=2;C['selector_suffix_intended']+=1
  elif name==('anchor',):
   o=[qs[2],qs[3],qs[0],qs[1]];vals=[xx(L[q] for q in o[c:]) for c in range(1,4)]
   assert not(vals[0]&fb) and (vals[0]&gm)==0
   assert vals[1]&fb and (vals[1]&gm)==gm
   assert vals[2]&fb and (vals[2]&gm)==gm
   C['anchor_suffix_flag']+=2;C['anchor_suffix_zero']+=1
  else:
   rr=L[qs[0]]^L[qs[2]];aa=L[qs[0]]^L[qs[1]];vv=p^aa
   o=[qs[2],qs[3],qs[0],qs[1]];vals=[xx(L[q] for q in o[c:]) for c in range(1,4)]
   assert vals==[p^rr,aa,vv]
   C['fixed_suffix_v']+=1;C['fixed_suffix_intended']+=1;C['fixed_suffix_zero']+=1
 # Complement suffixes. Every unit-marker suffix lies wholly in late fixed-v endpoints.
 for order in d['extra_orders']:
  marks=[L[q]&gm for q in order]
  first=next(i for i,m in enumerate(marks) if m)
  assert all(m==0 for m in marks[:first])
  assert all(r.pop(m)==1 for m in marks[first:])
  assert xx(marks[first:])==0
  for cut in range(1,len(order)):
   z=xx(L[q] for q in order[cut:]);m=z&gm
   assert r.pop(m)<=1
   if m:
    C['extra_suffix_unit']+=1
    assert cut>=first
    for q in order[cut:]:
     name,qs,fixed=qinfo[q]
     assert fixed and name!=('anchor',) and q==qs[1]
     p=L[qs[0]];aa=L[qs[0]]^L[qs[1]]
     assert L[q]==p^aa
   else:C['extra_suffix_zero']+=1
 return len(d['extra_rows'])

def run(V,E,m,w):
 C=Counter();forms=sched=safe=rows=0;cs=r.clause_types(V,w)
 for F in product(cs,repeat=m):
  if any(all(vv!=v for cl in F for vv,b in cl) for v in V):continue
  forms+=1
  for bits in product((0,1),repeat=len(E)):
   sched+=1;a=dict(zip(E,bits))
   if r.source_safe(F,V,E,a):safe+=1
   rows+=case(F,V,E,a,C)
 print('TAXONOMY_PASS',dict(variables=len(V),exists=len(E),clauses=m,width=w,formulas=forms,schedules=sched,safe=safe,rows=rows))
 print('COUNTS',' '.join('%s=%d'%x for x in sorted(C.items())))

run(('x','y','z'),('x',),3,3)
run(('x','y','z'),('x','y'),2,3)
~~~

### 12.2 Intended truth-direction audit

~~~python
#!/usr/bin/env python3
from itertools import product
import rin_xor_csp_search as r
def run(V,E,m,w):
 cs=r.clause_types(V,w);forms=sched=safe=unsafe=verified=0
 U=tuple(v for v in V if v not in E)
 for F in product(cs,repeat=m):
  if any(all(vv!=v for C in F for vv,b in C) for v in V):continue
  forms+=1
  for eb in product((0,1),repeat=len(E)):
   sched+=1;alpha=dict(zip(E,eb));wit=None
   for ub in product((0,1),repeat=len(U)):
    A={**alpha,**dict(zip(U,ub))}
    if r.psi(F,A):wit=A;break
   if wit is None:safe+=1;continue
   unsafe+=1;ans,err=r.compile_catalogue(F,V,E,alpha);assert err is None
   by,d=ans;cols,groups,D=r.build(F,V);resxor=0
   for gi,g in enumerate(groups):
    if g[0]=='v':name=('v',g[1],wit[g[1]])
    else:
     C=F[g[1]];cv=tuple(sorted(v for v,b in C));bits=tuple(wit[v] for v in cv);name=('c',g[1],bits)
    z=cols[name];assert ((z>>gi)&1) and r.pop(z&((1<<len(groups))-1))==1
    residual=z^(1<<gi);assert residual in by[gi];resxor^=residual
   assert resxor==0;verified+=1
 print('INTENDED_DIRECTION_PASS variables=%d exists=%d clauses=%d width=%d formulas=%d schedules=%d safe=%d unsafe=%d intended_verified=%d'% (len(V),len(E),m,w,forms,sched,safe,unsafe,verified))
run(('x','y','z'),('x',),3,3)
run(('x','y','z'),('x','y'),2,3)
~~~


### 12.3 Targeted odd-XOR drivers and captured results

These drivers import the exact extracted sealed `rin_xor_csp_search.py`. They are numerical attacks, not proof premises. Hashes bind the actual sources and captured stdout; elapsed time is intentionally not treated as semantic evidence.

#### Single odd-XOR probe

Source `targeted_rin.py`: 2040ca23c3a4517d1acf2e7d02624c0481bb34693a7192cb4f55e34c305cfbd3. Captured stdout SHA-256: 70c6a3ab4b9b22eab64e923a43bcc7d82c2e88116b066c228ea94faa5f993e2f. The elapsed field is observational and will vary.

~~~python
import rin_xor_csp_search as r
from itertools import product
def run(formula,variables=('x','y','z'),exists=('x',),alpha={'x':1}):
 print('formula',formula,'safe',r.source_safe(formula,variables,exists,alpha))
 ans,err=r.compile_catalogue(formula,variables,exists,alpha); print('err',err)
 by,data=ans
 for i,g in enumerate(data['groups']):
  print('GROUP',i,g,'options',len(by[i]))
 wit,peak,serr=r.solve_xor_exact_one(by)
 print('solution',wit,'peak',peak,'serr',serr)
 if wit is not None: print(r.witness_report(formula,variables,exists,alpha,by,data,wit))
 print('extra rows/orders')
 for i,(row,order) in enumerate(zip(data['extra_rows'],data['extra_orders'])): print(i,hex(row),order)
 print('abstract odd triple relation expected')
run(((('x',0),('y',0),('z',0)),(('y',1),),(('z',1),)))
~~~

~~~text
formula ((('x', 0), ('y', 0), ('z', 0)), (('y', 1),), (('z', 1),)) safe True
err None
GROUP 0 ('v', 'x') options 3
GROUP 1 ('v', 'y') options 6
GROUP 2 ('v', 'z') options 6
GROUP 3 ('c', 0) options 22
GROUP 4 ('c', 1) options 3
GROUP 5 ('c', 2) options 3
solution None peak 19440 serr None
extra rows/orders
0 0x3000300009 [20, 0, 3, 36, 37, 21]
1 0x30003000009 [24, 0, 3, 40, 41, 25]
2 0x300030000009 [28, 0, 3, 44, 45, 29]
3 0x333300000009 [32, 0, 3, 36, 40, 44, 37, 41, 45, 33]
abstract odd triple relation expected
~~~

#### One-wide/two-unit exhaustive family

Source `targeted_oddxor_search.py`: 646b30082ec52ab941fe982a05c1570b7694169292642c456266e946aa2776f0. Captured stdout SHA-256: c6c1d185e286474665b755eb1f1631ca9fb45a5ea7a1988671adb8b5ce762172. The elapsed field is observational and will vary.

~~~python
import rin_xor_csp_search as r
from itertools import product,permutations
import time,sys
V=('x','y','z'); E=('x',)
wide=[tuple(zip(V,b)) for b in product((0,1),repeat=3)]
unit=[((v,b),) for v in V for b in (0,1)]
seen=set(); total=safe=0; peak=0;t=time.time()
for W in wide:
 for U1 in unit:
  for U2 in unit:
   for F in set(permutations((W,U1,U2))):
    if F in seen: continue
    seen.add(F)
    if any(all(vv!=v for C in F for vv,b in C) for v in V): continue
    for xb in (0,1):
     total+=1;a={'x':xb}
     if not r.source_safe(F,V,E,a):continue
     safe+=1; ans,err=r.compile_catalogue(F,V,E,a)
     if err: print('ERR',F,a,err);sys.exit(3)
     by,data=ans; w,p,e=r.solve_xor_exact_one(by);peak=max(peak,p)
     if w is not None:
      print(r.witness_report(F,V,E,a,by,data,w));print('COUNTS',total,safe,peak,time.time()-t);sys.exit(2)
print('NO_COUNTEREXAMPLE formulas',len(seen),'schedules',total,'safe',safe,'peak',peak,'elapsed',time.time()-t)
~~~

~~~text
NO_COUNTEREXAMPLE formulas 864 schedules 1728 safe 768 peak 23004 elapsed 3.6155760288238525
~~~

#### Repeated-wide/two-unit exhaustive family

Source `targeted_repeated_oddxor_search.py`: 9dafc4aca49ee4d6845dbaf38fc610d559e6d04046a76080760cdbde9d7e7b4b. Captured stdout SHA-256: fe4235548c10c043dc387cb779408dd3631d82cabe6fc3c39bb5b31f27237eda. The elapsed field is observational and will vary.

~~~python
import rin_xor_csp_search as r
from itertools import product,permutations
import time,sys
V=('x','y','z'); E=('x',)
wide=[tuple(zip(V,b)) for b in product((0,1),repeat=3)]
unit=[((v,b),) for v in V for b in (0,1)]
seen=set();total=safe=0;peak=0;t=time.time()
for W in wide:
 for U1 in unit:
  for U2 in unit:
   for F in set(permutations((W,W,U1,U2))):
    if F in seen:continue
    seen.add(F)
    if any(all(vv!=v for C in F for vv,b in C) for v in V):continue
    for xb in (0,1):
     total+=1;a={'x':xb}
     if not r.source_safe(F,V,E,a):continue
     safe+=1;ans,err=r.compile_catalogue(F,V,E,a)
     if err:print('ERR',F,a,err);sys.exit(3)
     by,data=ans;w,p,e=r.solve_xor_exact_one(by);peak=max(peak,p)
     if w is not None:
      print(r.witness_report(F,V,E,a,by,data,w));print('COUNTS',len(seen),total,safe,peak,time.time()-t);sys.exit(2)
print('NO_COUNTEREXAMPLE formulas',len(seen),'schedules',total,'safe',safe,'peak',peak,'elapsed',time.time()-t)
~~~

~~~text
NO_COUNTEREXAMPLE formulas 1728 schedules 3456 safe 1536 peak 699192 elapsed 289.8941009044647
~~~

### 12.4 Additional exact and seeded commands

~~~sh
python3 rin_xor_csp_search.py --variables 3 --exists 1 --clauses 3 --width 3 --progress 1000
python3 rin_xor_csp_search.py --variables 3 --exists 2 --clauses 2 --width 3 --progress 100
python3 rin_xor_csp_search.py --variables 3 --exists 2 --clauses 3 --width 3 --random --limit 1000 --seed 8303 --progress 100
python3 rin_xor_csp_search.py --variables 4 --exists 1 --clauses 3 --width 3 --random --limit 300 --seed 8302 --progress 50
~~~

Their captured stdout hashes were, respectively,
`fcb201b0e539c94e973813acb8248f2301266308c123978d17b80ae6aef4ff07`,
`fc9486ce87ace4c8371ad2679e51522284d671a72f60cbd430debc74c0cf54c2`,
`222b0074d98ed518b11084eac6e7080ad262471a5d0ef73d1a129971f2cb14ba`, and
`7290fa042d6aee19a409e0651fe57cd4966ea55d516e92bca0299009744f052a`.
As with the embedded RIN census, a deterministic semantic projection should remove the final elapsed field before cross-machine hash comparison.

## 13. FIX-2, process, mutation, and cleanup ledger

### 13.1 Repository baseline and concurrent drift

At Round-83 start, git status --short --untracked-files=all had 10,024 lines and the repository had 15,714 regular files. Baseline scratch hashes were:

- git-status inventory: 612053a21bf33b1073f8eecab215ee3be059523ccab3e0dfd08db6749e05d7e3
- file inventory: ecefdc9903600d5d069191bf915f6d886cb0769edfcd6633dda4e2b8b14fd408
- process inventory: e237a988fd6017f035d26f9ecafa63f79b350ad5fab92a6b00e50a5efa835073

The baseline already contained modified tracked release/build files and thousands of unrelated untracked paths. Round 83 did not revert, stage, commit, push, or edit any of them. Final inventory comparison is performed after writing this report; its metrics are reported externally to avoid a self-hash paradox.

### 13.2 Command and failure ledger

**FIX-1:** clean. This was one strict-serial reviewer session. No sub-agent, delegated thread, or other worker was created or contacted.

The complete activity classes were:

1. Read-only git status, file discovery, heading inventory, byte count, and primary hash.
2. Full reads and hashes of protocols, frozen problem, current nodes, scheduler, reviewed upper/fixed-\(d\) material, and all Round-82 section-1 inputs.
3. YAML safe-load of scheduler, project, and three current nodes.
4. Scratch baseline inventories under /tmp/circdist-cplx-sigma2-rin-round83-20260830.
5. First listing extractor: exited 1 because a permissive regex paired alternating headings with the wrong code fences. Scratch only; corrected by section-bounded extraction.
6. Seven corrected listing extractions: every source hash matched.
7. Four short deterministic harnesses were initially issued in one foreground tool batch and briefly overlapped. This was mechanical replay inside one reviewer session, not sub-agent or detached compute. All seven extracted programs, including the four parameter rows of the RIN program, were then rerun strictly serially during final validation.
8. compiler_audit.py and kernel_shortcut_witness.py: foreground, exit 0.
9. Four final frozen RIN replay commands: foreground, exit 0. Two stdout hashes differed only in elapsed time.
10. Hash-preimage check over the elapsed field: recovered Round-82 values 0.462 and 34.721 exactly.
11. Targeted hand formula, wide/unit family, repeated-wide family, two-existential census, final v3/m3 census, and bounded random probes: all foreground. The 289.91-second repeated-family process remained attached to unified exec session 40764 and completed normally.
12. Full final v3/m3 process remained attached to unified exec session 11208 and completed normally.
13. Optional solver availability probe found no z3, pysat, or ortools installation; it wrote nothing.
14. Structural checker: foreground, exit 0.
15. First taxonomy checker: exited 1 on the audit script's reversed suffix expectation; no stdout evidence. The correction changed only scratch checker text.
16. Corrected safe-schedule taxonomy check: exit 0, then superseded by the stronger all-schedule taxonomy check.
17. All-schedule taxonomy and intended-direction audits: foreground, exit 0.
18. This single review write and the final read-only validation/cleanup commands.

No shell command used background ampersands, nohup, disown, detached subprocesses, solver workers, or handed-off computation. No OS process remains authorized for handoff.

**FIX-2 declaration:** every computation was foreground and attached to its tool session. The only long-lived tool sessions were unified exec 40764 (repeated-wide search), 11208 (full v3/m3 census), and 87817 (final serial replay); each reached exit 0 and closed. All other started processes were short-lived foreground shells or the explicitly listed Python, git, find, sed, hash, YAML, and inventory commands; all were awaited. There is no handed-off process. Every scratch result that affects the verdict is reproduced, summarized, or hash-bound in this report.

### 13.3 Post-write settlement boundary

The post-write settlement performs:

- rerun the seven embedded harnesses serially;
- parse all YAML again;
- rehash every protected input;
- compare baseline and final repository inventories;
- verify that the only attributable durable path is this report;
- delete the entire scratch root;
- scan for surviving Round-83 processes.

The resulting byte count, line count, SHA-256, exact inventory delta, process result, and FIX-2 closure are reported externally and are not self-embedded.

## 14. Final adjudication

**Layer 1 — F83-R82-CLEAR:** the unchanged Round-82 component lemmas listed in section 11 pass independent adversarial review, subject to F83-SEAL-DEFECT and F83-SIZE-REPAIR.

**Layer 2 — F83-RIN-NEW:** RIN has a complete public proof in section 7, but its status is **AUTHOR-PROVED-BUT-UNREVIEWED**. It requires another fresh reviewer.

**F83-NO-PROMOTION:** CIRCDIST.cplx.sigma2 remains OPEN. No total QSAT-to-Eff-Preserve reduction, \(\Sigma_2^P\)-hardness, completeness, classification-root promotion, canonical mutation, commit, or push is licensed by this report. The smallest next task is a fresh exact review of section 7.2–7.4 together with the already reviewed Round-82 chain and the \(O(s^4)\) dense-size correction.
