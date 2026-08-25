# Independent mathematical review of `se_bridge2_pin_20260718.md`

**Date:** 2026-07-18  
**Reviewed note:** `se/artifacts/se_bridge2_pin_20260718.md`  
**Review posture:** independent re-derivation; no intended verdict assumed.

## 1. Executive conclusion

The load-bearing mathematics is correct. The note does **not** identify alphabet defect with tensor weight in the ambient word space. It proves the two different inequalities it needs:

1. exact tensor weight \(k\) permits only alphabet defect at most \(k\); and
2. the primed carrier's position support, followed by restriction to legal NO words, kills every alphabet defect below \(k\).

Their conjunction pins every surviving legal alphabet type to defect exactly \(k\). The carrier projector commutes with the alphabet action, so the alphabet-isotypic decomposition is compatible with the carrier. The Peter--Weyl step, the transport to the YES side, the matched-degree legality estimates, and both middle-contraction arguments then assemble as claimed.

I found no false citation and no load-bearing gap. There is one harmless notational edge: Lemma 2.1 allows \(a=0\) or \(b=0\) but does not explicitly declare the first part of the empty partition to be \(0\). With that standard convention the statement is correct; all uses in the pinning proof have positive-sized factors anyway.

## 2. Per-step verdict table

| step | verdict | one-line reason | line(s) in the note |
|---|---|---|---|
| Setup: word spaces, weight, alphabet defect, and \(Q_k\) | **CONFIRMED** | BR's definitions give the stated factors, and the orthogonal \(\ell\)-sum has exact total weight \(k\). | 8--83 |
| LR induction rule and first-row lemma | **CONFIRMED** | The lattice condition forces the first read entry, hence the whole skew first row, to be \(1\), giving \(\tau_1-\sigma_1\le \sigma'_1\). | 85--127 |
| (a) Carrier subgroup position types | **CONFIRMED** | Each nonzero summand has defects \(k-\ell\) and \(\ell\) under \(S_{n-1}\times S_n\), while the first leg is \(S_1\)-trivial. | 141--157 |
| (b) LR control after two inductions | **CONFIRMED** | LR gives \(\tau_1\le\sigma_1+\sigma'_1\), then \(\nu_1\le1+\tau_1\). | 159--175 |
| (c) Induced-module containment | **CONFIRMED** | The canonical map \(\operatorname{Ind}_K^{S_{2n}}U\to\operatorname{span}(S_{2n}U)\) is a surjective intertwiner, so no new irreducible type can appear. | 177--191 |
| Full-position defect lower bound | **CONFIRMED** | Substitution yields \(2n-\nu_1\ge((n-1)-\sigma_1)+(n-\sigma'_1)=k\). | 193--203 |
| (d) Peter--Weyl pairing on legal NO words | **CONFIRMED** | Legal words form the regular left/right bimodule; \(S^\lambda\boxtimes S^\nu\) occurs only when \(\lambda=\nu\). | 205--216 |
| (e) Weight-to-alphabet inequality | **CONFIRMED** | A weight-\(k\) summand embeds in \(H^{\otimes k}\); every orbit with \(r\le k\) used letters forces \(\lambda_1\ge q-r\ge q-k\). | 218--227 |
| PIN, \(R_qQ_kA_{2n,=j}=0\) for \(j<k\) | **CONFIRMED** | Position defect is at least \(k\), whereas the alphabet type has defect \(j<k\), so legal regular-bimodule pairing annihilates it. | 132--137, 229 |
| Projector compatibility and adjoint form (3.8) | **CONFIRMED** | Position and alphabet actions commute, \(H_0,H_1\) are alphabet invariant, and hence \(Q_k\), weight, and alphabet projectors have the required commutations. | 231--236 |
| \(X/Y\) alphabet equivariance | **CONFIRMED** | \(\Pi_i\), \(e_0^*\), \(\Psi_i\), and \(e_0^*\otimes\Pi_1\) are alphabet intertwiners; tensoring and stacking preserve this. | 238--287 |
| Exact output weight | **CONFIRMED** | Every nonzero \(X\)-term has \(k\) \(\Psi_1\) outputs; every nonzero \(Y\)-term has one leading \(H_1\) output plus \(k-1\) others. | 290 |
| Equivariance transport and exact-\(k\) identity (4.7) | **CONFIRMED** | (3.8) pins the input, alphabet intertwining pins the output, and the carrier formulas supply exact input/output weight. | 292--308 |
| Matched-degree lemma used in (5.2) | **CONFIRMED** | The NO application is its \(m=q=2n\) equality case and the YES application is its \(m=n,q=2n\) upper-bound case. | 312--330 |
| Orthogonal block assembly | **CONFIRMED** | Legal restriction is alphabet-equivariant, so distinct \(\lambda\)-blocks are orthogonal on both sides and the norm is their maximum. | 332 |
| X-line corollary | **CONFIRMED** | Each outer factor has norm at most \(\sqrt r\), the projected middle has norm at most \(1\), and \(\sqrt r\,\sqrt r=r\). | 334--353 |
| Y-line corollary | **CONFIRMED** | The same factorization gives \(r\|\bar Y\|\); the cited ambient estimate then gives the displayed witness-range bound. | 355--380 |
| \(k=0\) endpoint | **CONFIRMED** | Matched degree is the constant type with scalar \(1\), while the \(Y_0\) defining sum is empty. | 382--394 |
| \(k=n\) boundary | **CONFIRMED** | Invalid \(\bar\Pi^{(n-1)}_n\) terms are zero; the LR argument still applies, and an empty \(X_n\) sum causes no exception. | 8, 143--151, 264--290 |
| Numerical envelope labeling | **CONFIRMED** | The note explicitly keeps \(\rho_{n,k}\le R_{n,k}\) numerical-only and does not use it in either analytic corollary. | 396--415 |
| \(n=3,k=1\) anchor | **CONFIRMED** | \(f^{(5,1)}=5\), so \(r_{\rm top}(6,1,(1))=6/5=1.2\). | 417--429 |
| Status table | **CONFIRMED** | Every row labeled PROVED has a complete argument in the note or a correctly invoked proved source; the envelope is correctly labeled numerical-only. | 431--451 |

## 3. Citation audit

Repeated composite citations in the status table are covered by the corresponding atomic ranges below. No mis-cite was found.

| citation checked | PASS/FAIL | what the cited lines establish |
|---|---|---|
| `se/artifacts/references/BR_1310.5185v4_collision.tex:326-354` | **PASS** | Ambient/legal row and column labels and the identification of a YES row with \((\mu,z)\). |
| `se/artifacts/references/BR_1310.5185v4_collision.tex:353-375` | **PASS** | The \(e\)-basis, constant \(e_0\), \(H_0/H_1\), projectors, and exact weight spaces. |
| `se/artifacts/references/BR_1310.5185v4_collision.tex:483-490` | **PASS** | The formulas for \(\Psi_0,\Psi_1\). |
| `se/artifacts/references/BR_1310.5185v4_collision.tex:525-531` | **PASS** | \(W_k^\mu\), its tensor-factor convention, and exact input/output weight \(k\). |
| `se/artifacts/references/BR_1310.5185v4_collision.tex:545-553` | **PASS** | The displayed \(X_k^\mu,Y_k^\mu,Z_k^\mu\) block formulas and leading-leg convention. |
| `se/artifacts/references/BR_1310.5185v4_collision.tex:600-611` | **PASS** | \(\bar\Pi_d^{(m)}\) selects exact weight and exactly \(d\) boxes below the first position row. |
| `se/artifacts/references/BR_1310.5185v4_collision.tex:632-646` | **PASS** | The primed SE projector \(\sum_\ell\bar\Pi_{k-\ell}^{(n-1)}\otimes\bar\Pi_\ell^{(n)}\) and its \(2n-1\)-leg domain. |
| `se/artifacts/references/BR_1310.5185v4_collision.tex:653-657` | **PASS** | Both \(\bar X_{\rm se,k}\) and \(\bar Y_{\rm se,k}\) use \(\Pi_0\otimes\bar\Pi'_{\rm se,k}\). |
| `se/artifacts/references/BR_1310.5185v4_collision.tex:678-686,1341-1346` | **PASS** | The hard bound \(\|\bar X_{\rm se,k}\|\le1\), including its proof endpoint. |
| `se/artifacts/se_bridge2_md_inst_20260718.md:7-15,43-59` | **PASS** | Matched-degree hypotheses, the shape \((q-k,\theta)\), \(r_{\rm top}\), and the lemma statement. |
| `se/artifacts/se_bridge2_md_inst_20260718.md:34-41` | **PASS** | Weight and alphabet projectors and their commutation. (That note calls the mean-zero space \(H_0\); this is only a local notation change.) |
| `se/artifacts/se_bridge2_md_inst_20260718.md:92-105` | **PASS** | The analogous induced-span containment under position completion and the absence of a multiplicity-one premise. |
| `se/artifacts/se_bridge2_md_inst_20260718.md:51-59,189-202` | **PASS** | The matched-degree bound and its exact full-permutation scalar. |
| `se/artifacts/se_bridge2_md_inst_20260718.md:204-206` | **PASS** | The separate \(k=0\) constant-function endpoint. |
| `se/artifacts/se_bridge2_md_inst_20260718.md:219-245` | **PASS** | Attainment/equality when \(m=q\). |
| `se/artifacts/se_bridge2_writeups_20260717.md:27-50` | **PASS** | Exact weight of \(Q_k\), orthogonality of its \(\ell\)-summands, and the coimage statement. |
| `se/artifacts/se_bridge2_writeups_20260717.md:54-111` | **PASS** | \(J_Y=\mathbf1_{M_{\rm se}}\otimes R_n\), including probability-\(L^2\) normalization. |
| `se/artifacts/se_bridge2_writeups_20260717.md:113-166` | **PASS** | Alphabet-isotypic projector commutation through legal NO inclusion/restriction. |
| `se/artifacts/se_bridge2_ytransfer_20260718.md:96-109` | **PASS** | Exact output weight \(k\) for \(\bar Y_{\rm se,k}\). |
| `se/artifacts/se_bridge2_ytransfer_20260718.md:139-152` | **PASS** | YES-side alphabet-projector commutation; it correctly does not commute weight through restriction. |
| `se/artifacts/se_bridge2_ytransfer_20260718.md:177-206` | **PASS** | The exact NO and bounded YES substitutions into the matched-degree lemma. |
| `se/artifacts/se_bridge2_ytransfer_20260718.md:224-232` | **PASS** | Identity (4.5) is precisely the missing exact-defect statement requested there; that earlier note did not itself claim to prove it. |
| `se/artifacts/se_leakage_lemma_verdict.md:12-57` | **PASS** | The legal permutation bimodule has multiplicity \(\delta_{\lambda,\nu}\), with no conjugate-partition error. |
| `se/artifacts/se_leakage_lemma_verdict.md:87-99` | **PASS** | Only finite exact-arithmetic evidence for the envelope, over the explicitly reported tested ranges. |
| `se/artifacts/se_legal_diamond_query_norm_audit.md:55-83` | **PASS** | The common conditional normalization and definition of \(\mathcal R\). |
| `se/artifacts/se_legal_diamond_query_norm_audit.md:348-359` | **PASS** | The formula defining \(R_{n,k}\). |
| `se/artifacts/se_one_defect_forgetting_bound.md:88-98` | **PASS** | The regular bimodule and the equal alphabet/full-position shape consequence. |
| `se/artifacts/se_stage2_py_verdict.md:11-31` | **PASS** | \(\|\bar Y_{\rm se,k}\|\le\sqrt2\sqrt{k/n}\) for \(0\le k<\lfloor n^{1/3}\rfloor\), including \(Y_0=0\). |
| `se/notes/SE_CARRIER_SUFFICIENCY_COMMISSION.md:820-835` | **PASS** | It distinguishes position type from alphabet type and states the needed weight-\(k\Rightarrow\) alphabet-defect-\(\le k\) fact. |
| `se/artifacts/logs_se_bridge2_20260717/bridge2_n3.log:1-15` | **PASS** | The quoted \(n=3\) numerical norms and \(r_{\rm top}(6,1)=1.2\) anchor. |

## 4. Independent re-derivations

### 4.1 Littlewood--Richardson first-row inequality

In the convention relevant here, \(c^\tau_{\sigma,\sigma'}\) counts semistandard fillings of the skew diagram \(\tau/\sigma\) with content \(\sigma'\), weakly increasing along rows, strictly increasing down columns, whose reverse row-reading word (right-to-left, top row first) is lattice: in every prefix, the number of \(i\)'s is at least the number of \(i+1\)'s for every \(i\). The induction rule is

\[
\operatorname{Ind}_{S_a\times S_b}^{S_{a+b}}
(S^\sigma\boxtimes S^{\sigma'})
\cong\bigoplus_{\tau\vdash a+b}c^\tau_{\sigma,\sigma'}S^\tau.
\]

Assume \(c^\tau_{\sigma,\sigma'}>0\), and choose one LR tableau. If the skew first row is empty, then \(\tau_1=\sigma_1\), so the inequality is immediate.

Otherwise the rightmost cell of the skew first row is the first letter read. If it contained \(r>1\), the one-letter prefix would have one \(r\) and no \(r-1\), contradicting the lattice inequality for \(r-1\). It therefore contains \(1\). Weak increase from left to right forces every skew cell to its left in that row also to contain \(1\). Hence the skew first row uses \(\tau_1-\sigma_1\) copies of \(1\), while the whole tableau has only \(\sigma'_1\) copies. Thus

\[
\tau_1-\sigma_1\le \sigma'_1,
\qquad\text{or}\qquad
\tau_1\le\sigma_1+\sigma'_1.
\]

Applying the same result to \(c^\nu_{(1),\tau}>0\) gives \(\nu_1\le1+\tau_1\), hence \(\nu_1\le1+\sigma_1+\sigma'_1\). This confirms the note's lattice-word and row argument. For a zero-sized factor, set the empty partition's first part to \(0\); that presentational convention is not needed in the carrier application.

### 4.2 Induced-module containment and the full-position lower bound

Fix a nonzero \(\ell\)-summand of \(Q_k\), with subgroup \(K=S_1\times S_{n-1}\times S_n\). Every irreducible \(K\)-submodule \(U\) has type

\[
\mathbf1\boxtimes S^\sigma\boxtimes S^{\sigma'},
\qquad
(n-1)-\sigma_1=k-\ell,\quad n-\sigma'_1=\ell.
\]

For such a \(U\), define

\[
\Phi:\mathbb C[S_{2n}]\otimes_{\mathbb C[K]}U
\longrightarrow \operatorname{span}(S_{2n}U),
\qquad g\otimes u\longmapsto gu.
\]

The balancing relation is respected because \(\Phi(gk\otimes u)=gku=\Phi(g\otimes ku)\). The map is \(S_{2n}\)-equivariant and surjective. Thus the generated module is a quotient of \(\operatorname{Ind}_K^{S_{2n}}U\); semisimplicity implies that every constituent of the quotient already occurs in the induced module.

By transitivity, induce first from \(S_{n-1}\times S_n\) and then add the \(S_1\) factor. The LR result gives every resulting shape \(\nu\)

\[
\nu_1\le1+\sigma_1+\sigma'_1.
\]

Consequently

\[
\begin{aligned}
2n-\nu_1
&\ge2n-(1+\sigma_1+\sigma'_1)\\
&=((n-1)-\sigma_1)+(n-\sigma'_1)\\
&=(k-\ell)+\ell=k.
\end{aligned}
\]

The range of \(Q_k\) is \(K\)-invariant and decomposes into such \(U\)'s, so every available full-position type has at least \(k\) boxes below its first row. This is a statement about **position** type only.

Compatibility with alphabet decomposition is valid. The diagonal alphabet action commutes with all position permutations; \(H_0=\mathbb Ce_0\) and \(H_1=e_0^\perp\) are alphabet invariant; hence exact-weight projectors and the \(\bar\Pi_d^{(m)}\) position projectors commute with the alphabet action. Therefore \(Q_k\) commutes with every alphabet-isotypic projector. Decomposing a carrier vector into alphabet types does not move it out of \(\operatorname{im}Q_k\).

### 4.3 Peter--Weyl pairing on legal words

At \(q=2n\), a legal NO word \(w:[q]\to[q]\) is a permutation. Alphabet permutations act on values from the left, while position permutations act on arguments from the right:

\[
(g,h):w\longmapsto gwh^{-1}.
\]

Thus the legal space is the regular bimodule

\[
\mathbb C[S_q]\cong
\bigoplus_{\lambda\vdash q}S^\lambda\boxtimes (S^\lambda)^*.
\]

Every complex Specht module of \(S_q\) is self-dual, so the second factor has the same partition label \(\lambda\), not the transpose partition. A legal \((\lambda,\nu)\) alphabet/position component is therefore zero unless \(\lambda=\nu\).

Restriction \(R_q\) is equivariant for both actions because bijections are invariant under alphabet and position permutations. Hence an ambient component of alphabet shape \(\lambda\) and full-position shape \(\nu\) can survive only if \(\lambda=\nu\).

Now take an alphabet shape of defect \(j<k\). It has \(2n-\lambda_1=j\), while every full-position shape generated from the carrier has \(2n-\nu_1\ge k\). Equality \(\lambda=\nu\) is impossible, so restriction kills that component. This proves PIN without equating the two gradings.

## 5. Equivariance transport and exact-defect identity

For \(g\in S_q\), \(U_ge_0=e_0\), so \(U_g\Pi_i=\Pi_iU_g\) and \(e_0^*U_g=e_0^*\). Direct substitution gives

\[
U_g\Psi_i=\Psi_i(U_g\otimes U_g),\qquad
U_g(e_0^*\otimes\Pi_1)=(e_0^*\otimes\Pi_1)(U_g\otimes U_g).
\]

Every \(X_k^\mu\) and \(Y_k^\mu\) block is a sum of tensor products of these maps. Stacking matching blocks leaves the matching label inert, so \(X_{\rm se,k}\) and \(Y_{\rm se,k}\) are alphabet intertwiners. Since \(Q_k\) commutes with the alphabet action, \(\bar X=XQ_k\) and \(\bar Y=YQ_k\) are intertwiners too.

PIN, commutation, and the weight/defect upper bound give

\[
Q_kJ_N^*=Q_kW_{2n,k}A_{2n,=k}J_N^*.
\]

Indeed, \(Q_k\) has exact weight \(k\), contains no alphabet defect above \(k\), and its lower-defect part annihilates \(J_N^*\) after taking the adjoint of PIN. Applying an alphabet intertwiner to the remaining defect-\(k\) input lands in defect \(k\) on the output. The explicit \(X/Y\) formulas put that output in exact weight \(k\). Since injective words are alphabet invariant, \(J_Y\) also intertwines the alphabet action. Therefore

\[
\mathcal R(\bar T_{\rm se,k})
=J_Y(\mathbf1_M\otimes W_{n,k}A_{n,=k})
\bar T_{\rm se,k}
(W_{2n,k}A_{2n,=k})J_N^*,
\qquad \bar T\in\{\bar X,\bar Y\}.
\]

No step here assumes that ambient tensor weight and alphabet defect are equal.

## 6. Matched-degree lemma and both corollaries

I checked the mechanism of `se_bridge2_md_inst_20260718.md` rather than treating its boxed result as opaque. Completion from \(m\) positions to \(q\) positions appends constant factors and is an isometry preserving exact degree and alphabet type. Forgetting a permutation down to its first \(m\) values is an isometry from injective words, and the restriction/completion square commutes pointwise. At \(m=q\), the regular bimodule kills every full-position type other than the alphabet type \(\lambda\). The full-permutation Gram scalar at degree \(d\) is

\[
r_d(\lambda)=\frac1{f^\lambda}
\sum_{t=0}^d q^t(-1)^{d-t}
\binom{q-t}{d-t}\frac{f^{\lambda/(q-t)}}{t!}.
\]

For \(d=k\) and \(\lambda=(q-k,\theta)\), every \(t<k\) term vanishes because the row \((q-t)\) does not fit in \(\lambda\), while the \(t=k\) skew shape is \(\theta\). Thus

\[
r_k(\lambda)=\frac{q^kf^\theta}{k!f^\lambda}=r_{\rm top}(q,k,\theta).
\]

The completion/projection argument gives

\[
\|R_mW_{m,k}A_{m,\lambda}\|^2\le r_{\rm top}(q,k,\theta),
\]

with equality for \(m=q\). This uses matched degree \(d=k\), not the different one-defect specialization \(d=j+1\).

Fix \(\lambda=(2n-k,\theta)\) and put \(r=r_{\rm top}(2n,k,\theta)\). The two outer factors in (4.7) satisfy

\[
\|W_{2n,k}A_{2n,\lambda}J_N^*\|=\sqrt r,\qquad
\|J_Y(\mathbf1_M\otimes W_{n,k}A_{n,\lambda})\|\le\sqrt r.
\]

For either carrier, the middle block is an orthogonal compression, so

\[
\|P_{\rm out}\bar T P_{\rm in}\|\le\|\bar T\|.
\]

Because distinct legal alphabet \(\lambda\)-isotypes are orthogonal on domain and codomain, the whole operator is an orthogonal direct sum and its norm is the maximum block norm. Hence

\[
\|\mathcal R(\bar X_{\rm se,k})\|
\le\max_{\theta\vdash k}r_{\rm top}(2n,k,\theta)
\]

using \(\|\bar X_{\rm se,k}\|\le1\), and

\[
\|\mathcal R(\bar Y_{\rm se,k})\|
\le\rho_{n,k}\|\bar Y_{\rm se,k}\|
\le\rho_{n,k}\sqrt2\sqrt{k/n}
\]

in the cited witness range for the last inequality. The two square-root legality factors multiply to \(r\), not \(\sqrt r\) or \(r^2\).

At \(k=0\), \(r_{\rm top}=1\), \(X\) has the constant block, and \(Y_0=0\). At \(n=3,k=1\), the unique \(\theta=(1)\) gives \(f^{(5,1)}=5\) and

\[
\rho_{3,1}=\frac{6^1f^{(1)}}{1!f^{(5,1)}}=\frac65=1.2,
\]

matching the cited anchor.

## 7. Targeted failure-mode audit

- **Silent assumption "alphabet defect = tensor degree": absent.** The proof uses only weight \(k\Rightarrow\) alphabet defect \(\le k\), then obtains equality after legal restriction from the independent position-defect/Peter--Weyl argument.
- **Carrier projector versus alphabet isotypes: compatible and proved.** Alphabet permutations commute with position permutations; \(H_0,H_1\) are invariant; therefore weight, position-isotypic, \(Q_k\), and alphabet-isotypic projectors commute as used.
- **Multiplicity issue: absent.** The induced-span map is a quotient statement, not a copywise norm estimate. In the matched-degree lemma, one orthogonal full-position projection bounds every vector in an entire isotypic component, so repeated copies create no uncontrolled cross terms.
- **\(k=0\): handled.** PIN is vacuous, defect \(\le0\) forces the trivial alphabet type, the matched-degree scalar is \(1\), and \(Y_0=0\).
- **Boundary \(k=n\): handled.** Zero projector summands and empty carrier sums are harmless; all nonzero subgroup factors satisfy the same first-row calculation.
- **Numerical versus analytic status: correctly separated.** Neither analytic corollary relies on the finite \(R_{n,k}\) scan.
- **Status table: no overclaim found.** Every PROVED row is supported; the only non-theorem is labeled NUMERICAL ONLY.

## FINAL VERDICT

**CONFIRMED.** Every load-bearing step holds. The exact unproved statement sought by the earlier transfer note is supplied here by Lemma 3.1, and its proof correctly keeps alphabet, position, and tensor-weight gradings distinct.
