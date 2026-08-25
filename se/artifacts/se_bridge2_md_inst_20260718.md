# Matched-degree legality by completion to a permutation

Date: 2026-07-18

## 1. Precise statement and notation

For a positive integer \(r\), write \([r]=\{1,\ldots,r\}\), and let \(S_r\) be the symmetric group of \([r]\). Fix integers
\[
q\ge m\ge 1,\qquad 0\le k\le \min(m,q).
\]
Let \(\theta\vdash k\) mean that \(\theta=(\theta_1,\theta_2,\ldots)\) is a partition of \(k\). For \(k=0\), \(\theta=\varnothing\) is the empty partition and \(\theta_1:=0\). Assume \(q-k\ge\theta_1\), so
\[
\lambda=(q-k,\theta)\vdash q
\]
is a partition; write \(\lambda_1=q-k\) for its first part. For a partition \(\mu\), let \(S^\mu\) be the complex irreducible representation of the relevant symmetric group and put \(f^\mu=\dim S^\mu\). For a skew Young diagram \(\mu/\nu\), let \(f^{\mu/\nu}\) be its number of standard Young tableaux.

Put
\[
\mathcal P_m=[q]^m,\qquad
\mathcal I_m=\operatorname{Inj}([m],[q]),
\]
where \(\operatorname{Inj}([m],[q])\) is the set of injective maps from \([m]\) to \([q]\). Both sets have uniform probability measure. Thus \(L^2(X)\), for either set \(X\), has inner product
\[
\langle a,b\rangle_X=|X|^{-1}\sum_{x\in X}\overline{a(x)}b(x).
\]
Define
\[
R_m:L^2(\mathcal P_m)\longrightarrow L^2(\mathcal I_m),
\qquad (R_ma)(x)=a(x).
\tag{1.1}
\]
This is the probability-\(L^2\) restriction in the source (se/artifacts/se_one_defect_forgetting_bound.md:69-82).

Write \(L^2([q])=\mathbf 1\oplus H_0\), where \(\mathbf 1\) is the one-dimensional constant subspace and \(H_0\) is the mean-zero subspace. Under \(L^2([q]^m)=L^2([q])^{\otimes m}\), let \(\Pi^{\mathrm{wt}=k}\) be the orthogonal projector onto the sum of tensor summands with exactly \(k\) factors from \(H_0\) and \(m-k\) factors from \(\mathbf 1\). This is the exact tensor-degree projector called \(P_d\) in the source (se/artifacts/se_one_defect_forgetting_bound.md:162-170).

The alphabet group \(S_q\) acts diagonally on words and hence on functions by
\[
(g\cdot a)(x_1,\ldots,x_m)
 =a(g^{-1}x_1,\ldots,g^{-1}x_m).
\]
Let \(\Pi^{\mathrm{alph}}_\lambda\) be the orthogonal projector onto the sum of all alphabet subrepresentations isomorphic to \(S^\lambda\). It commutes with \(\Pi^{\mathrm{wt}=k}\), since both \(\mathbf 1\) and \(H_0\) are alphabet-invariant.

For a linear map \(T\), let \(\|T\|=\sup_{\|a\|=1}\|Ta\|\). Define
\[
r_{\mathrm{top}}(q,k,\theta)
 =\frac{q^k f^\theta}{k!\,f^{(q-k,\theta)}}.
\tag{1.2}
\]
This is the source's top scalar with \(j\) renamed \(k\) (se/artifacts/se_one_defect_forgetting_bound.md:36-41).

**Matched-degree legality lemma.**
\[
\boxed{\;
\bigl\|R_m\Pi^{\mathrm{wt}=k}\Pi^{\mathrm{alph}}_\lambda\bigr\|^2
\le r_{\mathrm{top}}(q,k,\theta).
\;}
\tag{1.3}
\]
Equality holds when \(m=q\). This is the commissioned statement (se/notes/SE_CARRIER_SUFFICIENCY_COMMISSION.md:857-868), whose proposed proof is (2.7) at \(d=k\) followed by (3.8) (se/notes/SE_CARRIER_SUFFICIENCY_COMMISSION.md:859-868).

## 2. Completion and forgetting at \(d=k\)

The forgetting-bound note's result section assumes \(j\ge1\) and sets \(d=j+1\) (se/artifacts/se_one_defect_forgetting_bound.md:7-15). The present proof does not invoke its boxed one-defect theorem. It audits the degree-parametric steps inside that theorem's proof. Set \(d=k\); when \(k\ge1\), set the source's shape parameter \(j=k\).

### (2.3): product-word completion

The source equation is
\[
I_m^qa(x_1,\ldots,x_q)=a(x_1,\ldots,x_m).
\tag{2.3 quoted}
\]
Its hypotheses are \(q\ge m\), uniform product measures, and \(a\in L^2([q]^m)\). Summing over the last \(q-m\) coordinates gives \(\|I_m^qa\|=\|a\|\). The appended coordinates are constant tensor factors, so \(I_m^q\) preserves exact degree \(d=k\). It is alphabet-equivariant because those factors are alphabet-invariant, so it preserves type \(\lambda\). The definition and isometry are se/artifacts/se_one_defect_forgetting_bound.md:102-109.

### (2.4): permutation forgetting

The source equation is
\[
F_m^qb(\pi)=b(\pi(1),\ldots,\pi(m)),\qquad \pi\in S_q.
\tag{2.4 quoted}
\]
Every injection has \((q-m)!\) permutation completions. Since \(|S_q|=q!\) and \(|\mathcal I_m|=(q)_m=q!/(q-m)!\), where \((q)_m\) is the falling factorial, a uniform permutation has a uniform injective prefix. Hence \(\|F_m^qb\|=\|b\|\) for every \(b\in L^2(\mathcal I_m)\). The only hypothesis, \(q\ge m\), holds. See se/artifacts/se_one_defect_forgetting_bound.md:112-122.

### (2.5): commuting square

The quoted identity is
\[
F_m^qR_m=R_qI_m^q.
\tag{2.5 quoted}
\]
Both sides evaluated at \(\pi\in S_q\) equal \(a(\pi(1),\ldots,\pi(m))\). It holds pointwise, independently of degree, alphabet shape, or multiplicity (se/artifacts/se_one_defect_forgetting_bound.md:121-126).

### (2.6): position completion

The position group \(S_m\) acts by permuting coordinates. Decompose the range of \(\Pi^{\mathrm{wt}=k}\Pi^{\mathrm{alph}}_\lambda\) orthogonally into position isotypic subspaces indexed by \(\rho\vdash m\). The projectors preserve that decomposition, and \(R_m\) is position-equivariant (se/artifacts/se_one_defect_forgetting_bound.md:85-86).

Fix \(v\) in one position-\(\rho\) isotypic subspace. The source equation is
\[
\operatorname{Ind}_{S_m\times S_{q-m}}^{S_q}
 (S^\rho\boxtimes\mathbf 1)
=\bigoplus_{\tau\vdash q}c^\tau_{\rho,(q-m)}S^\tau.
\tag{2.6 quoted}
\]
Here \(\mathbf 1\) is the trivial representation of \(S_{q-m}\), \(\boxtimes\) is the outer tensor product, \(\operatorname{Ind}\) is group induction, \(\tau\) ranges over partitions of \(q\), and \(c^\tau_{\rho,(q-m)}\) is the Littlewood--Richardson coefficient. The last \(q-m\) appended coordinates are position-inactive and fixed by \(S_{q-m}\). Thus the position-\(S_q\) span of \(I_m^qv\) is contained in this induced module, exactly as stated at se/artifacts/se_one_defect_forgetting_bound.md:129-138.

This step has no premise \(d=j+1\), \(j<d\), or “one defect.” It also does not require \(c^\lambda_{\rho,(q-m)}=1\): if that coefficient is zero, the position-\(\lambda\) component below is zero; otherwise the projection argument uses neither its value nor a multiplicity basis.

### (2.7): reduction to a full-permutation singular value

For \(m=q\), the injection space is \(L^2(S_q)\), and its alphabet-left and position-right actions give
\[
L^2(S_q)\cong\bigoplus_{\sigma\vdash q}S^\sigma\boxtimes S^\sigma,
\tag{2.2 quoted}
\]
where \(\sigma\) ranges over partitions of \(q\). Hence an alphabet-\(\lambda\) vector survives \(R_q\) only in full position type \(\lambda\) (se/artifacts/se_one_defect_forgetting_bound.md:88-98). Let \(P^{\mathrm{pos}}_\lambda\) be the orthogonal projector onto that position isotype. Write \(R_q|_{(\lambda,\lambda),d}\) for \(R_q\) restricted to exact degree \(d\), alphabet type \(\lambda\), and full position type \(\lambda\). For the vector \(v\) above, (2.7) is
\[
\begin{aligned}
\|R_mv\|
 &=\|F_m^qR_mv\|
  =\|R_qI_m^qv\|\\
 &=\|R_qP^{\mathrm{pos}}_\lambda I_m^qv\|
 \le \bigl\|R_q|_{(\lambda,\lambda),d}\bigr\|\,\|v\|.
\end{aligned}
\tag{2.7 quoted}
\]
The first equality uses the (2.4) isometry; the second uses (2.5); the third uses (2.2) and (2.6); the inequality uses that \(I_m^q\) is an isometry and \(P^{\mathrm{pos}}_\lambda\) is an orthogonal contraction. By (2.3), the completed projected vector has degree \(d=k\) and alphabet type \(\lambda\). Thus every hypothesis holds at \(d=k\). The complete chain and its degree label are se/artifacts/se_one_defect_forgetting_bound.md:140-153.

The bound is uniform in \(\rho\). Since \(R_m\) is position-equivariant, outputs in distinct position isotypes are orthogonal. Squaring and summing over the position decomposition gives
\[
\bigl\|R_m\Pi^{\mathrm{wt}=k}\Pi^{\mathrm{alph}}_\lambda\bigr\|
\le \bigl\|R_q|_{(\lambda,\lambda),k}\bigr\|.
\tag{2.8}
\]
Repeated copies inside one \(\rho\)-isotype need not be separated: (2.7) is a bound for every vector in that entire isotypic subspace.

## 3. Exact full-permutation scalar

Let \(P_d\) be the degree-\(d\) projector on \([q]^q\), let \(R_q^*\) be the Hilbert adjoint of \(R_q\), and set \(A_d=R_qP_dR_q^*\). If two permutations agree in \(h\) coordinates, the probability-normalized kernel is
\[
K_d(h)=\sum_{t=0}^d q^t(-1)^{d-t}
 \binom{q-t}{d-t}\binom ht.
\tag{3.1 quoted}
\]
Its only range premise is \(0\le d\le q\), which holds at \(d=k\) because \(k\le m\le q\). The reflection-factor derivation is se/artifacts/se_one_defect_forgetting_bound.md:162-174.

For \(g\in S_q\), let \(\operatorname{fix}(g)\) be its number of fixed points. For a representation \(V\), let \(\chi_V\) denote its character; abbreviate \(\chi_{S^\lambda}\) to \(\chi_\lambda\). Centrality makes \(A_d\) a scalar \(r_d(\lambda)\) on the \(\lambda\)-block:
\[
r_d(\lambda)=\frac{1}{q!f^\lambda}
 \sum_{g\in S_q}K_d(\operatorname{fix}g)\chi_\lambda(g).
\tag{3.2 quoted}
\]
The premises \(\lambda\vdash q\) and \(0\le d\le q\) hold. The scalar and character-orthogonality formula are se/artifacts/se_one_defect_forgetting_bound.md:173-182.

For \(0\le t\le d\), the falling factorial \((\operatorname{fix}g)_t\) is the ordered-injective-\(t\)-tuple character:
\[
(\operatorname{fix}g)_t
=\chi_{\operatorname{Ind}_{S_{q-t}}^{S_q}\mathbf1}(g).
\tag{3.3 quoted}
\]
Because \(\binom{\operatorname{fix}g}{t}=(\operatorname{fix}g)_t/t!\), Frobenius reciprocity gives
\[
\frac1{q!}\sum_{g\in S_q}
 \binom{\operatorname{fix}g}{t}\chi_\lambda(g)
=\frac{f^{\lambda/(q-t)}}{t!}.
\tag{3.4 quoted}
\]
Here \((q-t)\) is the one-row partition of \(q-t\), embedded in the upper-left of \(\lambda\). The premise \(0\le t\le d\le q\) holds at \(d=k\). These steps are se/artifacts/se_one_defect_forgetting_bound.md:185-201.

Substitution into (3.2) yields
\[
r_d(\lambda)=\frac1{f^\lambda}\sum_{t=0}^d
 q^t(-1)^{d-t}\binom{q-t}{d-t}
 \frac{f^{\lambda/(q-t)}}{t!}.
\tag{3.5 quoted}
\]
This is se/artifacts/se_one_defect_forgetting_bound.md:204-213; no one-defect premise enters.

Now take \(\lambda=(q-k,\theta)\). If \(t<k\), then \(q-t>q-k=\lambda_1\), so \((q-t)\) does not fit inside \(\lambda\):
\[
f^{\lambda/(q-t)}=0.
\tag{3.6 quoted}
\]
This is the source's argument with \(j=k\) (se/artifacts/se_one_defect_forgetting_bound.md:216-221). At \(t=k\), removing the first row of length \(q-k\) leaves \(\theta\), including the boundary \(q-k=\theta_1\):
\[
f^{\lambda/(q-k)}=f^\theta.
\tag{3.7 quoted}
\]
This is se/artifacts/se_one_defect_forgetting_bound.md:224-228. The partition premise \(q-k\ge\theta_1\) validates both row statements.

Set \(d=k\) in (3.5). There is no \(t>k\) term; (3.6) kills every \(t<k\) term; and (3.7) evaluates the remaining term:
\[
r_k(\lambda)
=\frac{q^k f^\theta}{k!f^\lambda}
=r_{\mathrm{top}}(q,k,\theta).
\tag{3.8 instantiated}
\]
The same matched-degree calculation is the source's (3.8) (se/artifacts/se_one_defect_forgetting_bound.md:231-237). Since \(A_k\) is the Gram operator of \(R_qP_k\), this scalar is the squared singular value on the \((\lambda,\lambda)\) block:
\[
\bigl\|R_q|_{(\lambda,\lambda),k}\bigr\|^2
=r_k(\lambda)=r_{\mathrm{top}}(q,k,\theta).
\tag{3.9}
\]
Combining (2.8) and (3.9) proves (1.3) for \(k\ge1\).

### Endpoint \(k=0\)

The source's opening premise \(j\ge1\) means “verbatim” does not literally cover \(k=0\) (se/artifacts/se_one_defect_forgetting_bound.md:11-15). Here \(\theta=\varnothing\), \(\lambda=(q)\), and the range of \(\Pi^{\mathrm{wt}=0}\Pi^{\mathrm{alph}}_{(q)}\) is the one-dimensional constant subspace. Restriction takes its unit constant function to the unit constant function, so the squared norm is \(1\). Also \(q^0=0!=f^\varnothing=f^{(q)}=1\), hence \(r_{\mathrm{top}}(q,0,\varnothing)=1\). This separately proves the endpoint and its equality case.

## 4. Where multiplicity-insensitivity enters

Multiplicity-insensitivity enters at the third equality of (2.7),
\[
\|R_qI_m^qv\|
=\|R_qP^{\mathrm{pos}}_\lambda I_m^qv\|,
\]
and the following contraction estimate on the one full-permutation \((\lambda,\lambda)\) block. The regular bimodule has only matching alphabet and position shapes (se/artifacts/se_one_defect_forgetting_bound.md:88-98). Thus every completed position component other than \(\lambda\) is annihilated. The surviving orthogonal projector has norm one, independently of the number or coordinates of lower Pieri copies. This is precisely the work done by the source's remark (se/artifacts/se_one_defect_forgetting_bound.md:155-158) inside the chain at se/artifacts/se_one_defect_forgetting_bound.md:140-153. The observation that the regular bimodule has one full-position \(\lambda\) copy confirms the same reduction (se/artifacts/se_one_defect_forgetting_bound.md:270-273).

No \(\rho\)-block-diagonality inside a repeated isotype and no Pieri/content-product formula is used. If the projection reduction were false, completed multiplicity components could contribute simultaneously; per-copy estimates would not control arbitrary linear combinations because cross terms could enlarge the norm. One would then need an operator-norm bound for the multiplicity matrix. Equation (2.7) avoids that requirement by bounding every vector after one orthogonal projection. The commission assigns this exact role to the remark (se/notes/SE_CARRIER_SUFFICIENCY_COMMISSION.md:864-868).

## 5. Equality when \(m=q\)

Assume \(m=q\). The regular decomposition supplies a nonzero \(\lambda\)-block \(W_\lambda\subset L^2(S_q)\) (se/artifacts/se_one_defect_forgetting_bound.md:88-98). Section 3 and the source's character identities give
\[
A_kw=R_qP_kR_q^*w=r_{\mathrm{top}}(q,k,\theta)w
\qquad(w\in W_\lambda)
\]
(se/artifacts/se_one_defect_forgetting_bound.md:162-237).

Put \(r=r_{\mathrm{top}}(q,k,\theta)>0\), choose \(0\ne w\in W_\lambda\), and define
\[
u=\frac{P_kR_q^*w}{\sqrt r\,\|w\|}.
\tag{5.1}
\]
The maps \(P_k\) and \(R_q^*\) are alphabet-equivariant, so \(u\) has exact weight \(k\) and alphabet type \(\lambda\). Moreover,
\[
\|P_kR_q^*w\|^2
=\langle w,R_qP_kR_q^*w\rangle
=r\|w\|^2,
\]
so \(\|u\|=1\), while
\[
R_qu=\frac{A_kw}{\sqrt r\,\|w\|}
=\frac{\sqrt r\,w}{\|w\|},
\qquad \|R_qu\|^2=r.
\]
Thus the **top-copy subspace** \(P_kR_q^*W_\lambda\) attains the bound, and (5.1) names an attaining unit vector. At \(k=0\), it reduces to the unit constant vector. This proves equality, not merely an upper bound.

## 6. Hidden-hypothesis audit, evidence, and status

The one-defect relation \(d=j+1\) is used only after the matched-degree scalar: the source introduces an extra skew box at \(t=j+1\), proves (3.9), and then specializes to \(d=j+1\) for the two-term ratio (3.10) (se/artifacts/se_one_defect_forgetting_bound.md:240-268). Those steps are unused. At \(d=j=k\), the sum stops at \(t=k\), so there is no extra-box term and no required inequality \(j<d\). The later substitution \(j=k-1\) belongs only to the BR one-defect application (se/artifacts/se_one_defect_forgetting_bound.md:295-329) and is unused. The commission likewise distinguishes the mismatched ratio from the matched ratio one (se/notes/SE_CARRIER_SUFFICIENCY_COMMISSION.md:892-895).

**Status: PROVED.** The literal source setup has one endpoint mismatch—\(j\ge1\) excludes \(k=0\)—but the separate constant-function proof above closes it. No hypothesis needed for \(1\le k\le m\) fails under \(j=d=k\).

The numerical log is support only. It contains 40 parameter-shape rows over
\[
(q,m)=(6,6),(6,3),(6,4),(5,5),(5,3),(7,3),
\]
with no violation and equality in every \(m=q\) row (se/artifacts/logs_se_carrier_steps35_20260716/se_matched_degree_lemma_check.log:5-61). Its heading states the tested operator inequality (se/artifacts/logs_se_carrier_steps35_20260716/se_matched_degree_lemma_check.log:1-3). No finite row is used in the proof.

| step | hypothesis checked | verdict | source lines |
|---|---|---|---|
| (2.1) normalization | uniform probability measures on \([q]^m\) and injections | PASS | se/artifacts/se_one_defect_forgetting_bound.md:69-82 |
| (2.3) | \(q\ge m\); inactive factors preserve \(d=k\) and alphabet type | PASS | se/artifacts/se_one_defect_forgetting_bound.md:102-109 |
| (2.4) | \(q\ge m\); each injection has \((q-m)!\) completions | PASS | se/artifacts/se_one_defect_forgetting_bound.md:112-122 |
| (2.5) | both composites have the same pointwise value | PASS | se/artifacts/se_one_defect_forgetting_bound.md:121-126 |
| (2.6) | position-\(\rho\) vector fixed by the last \(S_{q-m}\); no multiplicity value needed | PASS | se/artifacts/se_one_defect_forgetting_bound.md:129-138 |
| (2.7) | (2.4) isometric; (2.5) commutative; only matching regular shapes survive; completion preserves \(d=k\) | PASS | se/artifacts/se_one_defect_forgetting_bound.md:88-98,140-153 |
| full position sum | position equivariance gives orthogonal outputs; (2.7) is vector-level within multiplicities | PASS | se/artifacts/se_one_defect_forgetting_bound.md:85-86,129-158 |
| (3.1) | \(0\le d=k\le q\) | PASS | se/artifacts/se_one_defect_forgetting_bound.md:162-174 |
| (3.2) | \(\lambda\vdash q\); kernel is central | PASS | se/artifacts/se_one_defect_forgetting_bound.md:173-182 |
| (3.3)--(3.4) | \(0\le t\le d=k\le q\); tuple character and reciprocity | PASS | se/artifacts/se_one_defect_forgetting_bound.md:185-201 |
| (3.5) | substitution of (3.1) and (3.4), without one-defect premise | PASS | se/artifacts/se_one_defect_forgetting_bound.md:204-213 |
| (3.6) | \(t<k\Rightarrow q-t>\lambda_1=q-k\) | PASS | se/artifacts/se_one_defect_forgetting_bound.md:216-221 |
| (3.7) | \(q-k\ge\theta_1\); removing row \((q-k)\) leaves \(\theta\) | PASS | se/artifacts/se_one_defect_forgetting_bound.md:224-228 |
| (3.8) at \(d=k\) | only \(t=k\) survives in (3.5) | PASS | se/artifacts/se_one_defect_forgetting_bound.md:231-237 |
| multiplicity-insensitivity | one orthogonal full-position projection replaces copywise estimates | PASS | se/artifacts/se_one_defect_forgetting_bound.md:140-158,270-273 |
| equality at \(m=q\) | Gram scalar attained on \(P_kR_q^*W_\lambda\) | PASS | se/artifacts/se_one_defect_forgetting_bound.md:88-98,162-237 |
| \(k=0\) endpoint | \(j\ge1\) is inapplicable; constants make both sides one | PASS (separate proof) | se/artifacts/se_one_defect_forgetting_bound.md:11-15,69-82 |
| one-defect-only steps | (3.9)--(3.10), \(d=j+1\), and later \(j=k-1\) unused | NOT NEEDED | se/artifacts/se_one_defect_forgetting_bound.md:240-268,295-329 |
| finite support | 40 rows; no violations; equality in every tested \(m=q\) row | SUPPORT ONLY | se/artifacts/logs_se_carrier_steps35_20260716/se_matched_degree_lemma_check.log:5-61 |
