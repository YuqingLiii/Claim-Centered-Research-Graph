# Defect pinning for the primed Set Equality carrier

**Date:** 2026-07-18  
**Verdict:** **PROVED.** For the primed BR carrier at (q=2n), legal NO restriction annihilates every alphabet-defect-(j) component with (j<k). Consequently the legally transferred (X)- and (Y)-carriers have alphabet defect exactly (k) on both sides. The two requested analytic legality bounds follow. The separate (R_{n,k}) envelope remains **NUMERICAL ONLY**, exactly as its source reports.

## 1. Setup and notation

Fix an integer (n\ge 2), put (q:=2n), and fix (k\in\{0,1,\ldots,n\}). For a positive integer (r), write ([r]:=\{1,\ldots,r\}), and write (S_r) for the symmetric group of ([r]). All word spaces below have uniform probability measure, and all (L^2)-norms use that measure.

Let (H:=L^2([q])\cong\mathbb C^q). BR chooses an orthonormal basis (e_0,e_1,\ldots,e_{q-1}) in which (e_0) is the constant unit vector. Set
\[
 H_0:=\operatorname{span}\{e_0\},\qquad H_1:=e_0^\perp,
\]
and let (\Pi_0) and (\Pi_1) be the orthogonal projectors onto (H_0) and (H_1), respectively. These definitions are at `se/artifacts/references/BR_1310.5185v4_collision.tex:353-375`.

For (m\ge 1), the **weight** of an (e)-basis tensor in (H^{\otimes m}) is the number of tensor factors in (H_1). Let (W_{m,d}) be the orthogonal projector onto exact weight (d). The diagonal **alphabet action** of (S_q) on (L^2([q]^m)) is
\[
 (g\cdot f)(x_1,\ldots,x_m)
 :=f(g^{-1}x_1,\ldots,g^{-1}x_m).
\]
For a partition (\lambda\vdash q), let (S^\lambda) denote the corresponding complex irreducible (S_q)-module, let (f^\lambda:=\dim S^\lambda), and let (A_{m,\lambda}) be the alphabet-(S^\lambda) isotypic projector on (L^2([q]^m)). Define the **alphabet defect**
\[
 \operatorname{def}(\lambda):=q-\lambda_1,
\]
where (\lambda_1) is the first-row length of (\lambda), and set
\[
 A_{m,=d}:=\sum_{\substack{\lambda\vdash q<machine-local-path-redacted>}}A_{m,\lambda},
 \qquad
 A_{m,<d}:=\sum_{j=0}^{d-1}A_{m,=j}.
\tag{1.1}
\]
On a space with a matching register, (A_{m,\lambda}), (A_{m,=d}), and (W_{m,d}) mean the identity on that register tensored with the displayed word-space projector. The alphabet definitions and the commutation of weight and alphabet projectors are recorded at `se/artifacts/se_bridge2_md_inst_20260718.md:34-41`.

Independently, (S_m) has the **position action** on (H^{\otimes m}) by permutation of tensor factors. For (0\le d\le m), let (\bar\Pi_d^{(m)}) be BR's orthogonal projector onto the part of exact weight (d) whose position-(S_m) irreducibles have exactly (d) boxes below their first row. Thus every such irreducible has shape (\rho\vdash m) with (m-\rho_1=d). This is BR's definition at `se/artifacts/references/BR_1310.5185v4_collision.tex:600-611`. Put
\[
 \bar\Pi'_{\mathrm{se},k}
 :=\sum_{\ell=0}^{k}
 \bar\Pi_{k-\ell}^{(n-1)}\otimes\bar\Pi_{\ell}^{(n)},
 \qquad
 Q_k:=\Pi_0\otimes\bar\Pi'_{\mathrm{se},k},
\tag{1.2}
\]
where the two factors after the first leg act on legs (2,\ldots,n) and (n+1,\ldots,2n), respectively. Equation (1.2) is BR's primed SE projector at `se/artifacts/references/BR_1310.5185v4_collision.tex:632-646`. Its image has exact total weight (k); a projector-level proof, including orthogonality of the (\ell)-summands, is at `se/artifacts/se_bridge2_writeups_20260717.md:27-50`.

Let (M_{\mathrm{se}}) be the set of bipartite perfect matchings between positions ([n]) and (\{n+1,\ldots,2n\}). Define the ambient NO and YES spaces
\[
 \mathcal H_N:=L^2([q]^{2n}),\qquad
 \mathcal H_Y:=\mathbb C^{M_{\mathrm{se}}}\otimes L^2([q]^n).
\]
BR identifies a YES row with a pair ((\mu,z)\in M_{\mathrm{se}}\times[q]^n) at `se/artifacts/references/BR_1310.5185v4_collision.tex:326-354`. Let
\[
 R_m:L^2([q]^m)\longrightarrow
 L^2(\operatorname{Inj}([m],[q]))
\]
be pointwise restriction to injective words. At (m=q=2n), injective words are bijections, so (R_q) is legal NO restriction. If (J_N) and (J_Y) denote probability-(L^2) legal restriction on the NO and YES sides, then
\[
 J_N=R_q,\qquad
 J_Y=\mathbf 1_{M_{\mathrm{se}}}\otimes R_n,
 \qquad
 \mathcal R(T):=J_YTJ_N^*.
\tag{1.3}
\]
The common normalization is proved at `se/artifacts/se_legal_diamond_query_norm_audit.md:55-83`, and the YES factorization is proved at `se/artifacts/se_bridge2_writeups_20260717.md:54-111`.

BR's two carriers used here are
\[
 \bar X_{\mathrm{se},k}:=X_{\mathrm{se},k}Q_k,
 \qquad
 \bar Y_{\mathrm{se},k}:=Y_{\mathrm{se},k}Q_k.
\tag{1.4}
\]
Both use the same (Q_k); these are the definitions at `se/artifacts/references/BR_1310.5185v4_collision.tex:653-657`.

For a partition (\theta\vdash k), including the empty partition (\varnothing\vdash0), define
\[
 \lambda(k,\theta):=(2n-k,\theta),\qquad
 r_{\mathrm{top}}(2n,k,\theta)
 :=\frac{(2n)^k f^\theta}{k!\,f^{(2n-k,\theta)}},
 \qquad
 \rho_{n,k}:=\max_{\theta\vdash k}r_{\mathrm{top}}(2n,k,\theta).
\tag{1.5}
\]
Because (k\le n), (2n-k\ge k\ge\theta_1), so (\lambda(k,\theta)) is a partition of (2n). The matched-degree scalar and its hypotheses are at `se/artifacts/se_bridge2_md_inst_20260718.md:7-15,43-59`.

## 2. Littlewood--Richardson first-row lemma

We first supply the LR fact used below rather than cite it as folklore.

**Lemma 2.1 (LR first-row inequality).** Let (a,b\ge0), let (\sigma\vdash a), (\sigma'\vdash b), and (\tau\vdash a+b). If the Littlewood--Richardson coefficient (c^\tau_{\sigma,\sigma'}) is nonzero, then
\[
 \tau_1\le \sigma_1+\sigma'_1.
\tag{2.1}
\]

**LR convention.** The Young diagram of a partition (\alpha=(\alpha_1,\alpha_2,\ldots)) consists of cells ((i,j)) with (1\le j\le\alpha_i), using left-justified rows. An LR tableau of skew shape (\tau/\sigma) and content (\sigma') is a filling of the cells of (\tau\setminus\sigma) by positive integers such that:

1. entries are weakly increasing from left to right in every row;
2. entries are strictly increasing from top to bottom in every column;
3. the reverse row-reading word, obtained by reading each row from right to left and the rows from top to bottom, is a lattice word: in every initial segment and for every (i\ge1), the number of entries (i) is at least the number of entries (i+1);
4. exactly (\sigma'_i) cells contain (i).

The LR induction rule is
\[
 \operatorname{Ind}_{S_a\times S_b}^{S_{a+b}}
 (S^\sigma\boxtimes S^{\sigma'})
 \cong\bigoplus_{\tau\vdash a+b}
 c^\tau_{\sigma,\sigma'}S^\tau,
\tag{2.0}
\]
where \(c^\tau_{\sigma,\sigma'}\) is the number of tableaux satisfying conditions 1--4. Thus a constituent \(S^\tau\) occurs exactly when the coefficient is nonzero. In particular, a nonzero coefficient supplies at least one such tableau and forces \(\sigma\subseteq\tau\).

**Proof.** Choose an LR tableau (T) of shape (\tau/\sigma) and content (\sigma'). If the skew diagram has no cell in row one, then (\tau_1=\sigma_1\), and (2.1) follows from (\sigma'_1\ge0).

Suppose instead that row one of (\tau/\sigma) is nonempty. Its rightmost cell is the first letter of the reverse row-reading word. That letter cannot be (r>1): the initial segment of length one would then contain one (r) and no (r-1), violating the lattice condition for (i=r-1). Hence the rightmost entry in row one is (1). Row entries are weakly increasing from left to right and all entries are positive integers, so every entry to its left in row one is also (1). Therefore row one of the skew diagram contains only (1)'s.

The number of skew cells in row one is (\tau_1-\sigma_1). The content condition says that the entire tableau contains exactly (\sigma'_1) entries equal to (1). Consequently
\[
 \tau_1-\sigma_1\le\sigma'_1,
\]
which is (2.1). \(\square\)

The same proof permits a one-box first factor: if (c^\nu_{(1),\tau}\ne0), then (\nu_1\le1+\tau_1). Combining this with (2.1), or applying (2.1) twice, gives
\[
 c^\tau_{\sigma,\sigma'}c^\nu_{(1),\tau}\ne0
 \quad\Longrightarrow\quad
 \nu_1\le1+\sigma_1+\sigma'_1.
\tag{2.2}
\]

## 3. The defect-pinning lemma

**Lemma 3.1 (DEFECT-PINNING / PIN).** For every (j<k),
\[
 R_qQ_kA_{2n,=j}=0.
\tag{3.1}
\]
Equivalently, if (v\in\operatorname{im}Q_k\) has alphabet defect exactly (j<k), then its probability-(L^2) restriction to legal NO words, namely to the bijections ([2n]\to[q]), is zero.

**Proof.** We verify the five commissioned links separately.

### (a) Subgroup position types in the carrier

Fix (\ell\in\{0,\ldots,k\}) for which the (\ell)-summand in (1.2) is nonzero. By BR's definition of (\bar\Pi_d^{(m)}), every position-(S_{n-1}\times S_n) irreducible in that summand has the form (S^\sigma\boxtimes S^{\sigma'}), where
\[
 \sigma\vdash n-1,\quad
 \sigma'\vdash n,\quad
 (n-1)-\sigma_1=k-\ell,\quad
 n-\sigma'_1=\ell.
\tag{3.2}
\]
Indeed, the two factors in (1.2) retain exactly (k-\ell) and (\ell) boxes below their respective first rows. This is precisely the content of BR's definition and primed decomposition at `se/artifacts/references/BR_1310.5185v4_collision.tex:600-611,632-646`. If (k-\ell>n-1), that factor is zero and contributes nothing.

The leading factor (\Pi_0) is one-dimensional and is fixed by the position group (S_1) on leg one. Thus every irreducible subgroup type in (\operatorname{im}Q_k), under
\[
 K:=S_1\times S_{n-1}\times S_n\le S_{2n},
\]
is (\mathbf1\boxtimes S^\sigma\boxtimes S^{\sigma'}) with (3.2).

### (b) First-row control under LR induction

Lemma 2.1 proves, with the LR convention stated there, that every (S_{2n-1})-constituent (S^\tau) of
\[
 \operatorname{Ind}_{S_{n-1}\times S_n}^{S_{2n-1}}
 (S^\sigma\boxtimes S^{\sigma'})
\]
satisfies (\tau_1\le\sigma_1+\sigma'_1). Applying the same lemma to induction with the one-box partition ((1)), every (S_{2n})-constituent (S^\nu) of
\[
 \operatorname{Ind}_{S_1\times S_{2n-1}}^{S_{2n}}
 (\mathbf1\boxtimes S^\tau)
\]
satisfies (\nu_1\le1+\tau_1\). Hence (2.2) gives
\[
 \nu_1\le1+\sigma_1+\sigma'_1.
\tag{3.3}
\]

### (c) Full-position types in the carrier

We justify that the induced modules in (b) actually control the full (S_{2n})-span. Let (U\subseteq\operatorname{im}Q_k) be one irreducible (K)-submodule of type (\mathbf1\boxtimes S^\sigma\boxtimes S^{\sigma'}). The map
\[
 \Phi:\mathbb C[S_{2n}]\otimes_{\mathbb C[K]}U
 \longrightarrow \operatorname{span}(S_{2n}U),
 \qquad g\otimes u\longmapsto g\cdot u,
\tag{3.4}
\]
is well-defined, (S_{2n})-equivariant, and surjective. Thus (\operatorname{span}(S_{2n}U)) is a quotient of
\[
 \operatorname{Ind}_{K}^{S_{2n}}
 (\mathbf1\boxtimes S^\sigma\boxtimes S^{\sigma'}).
\]
By transitivity of induction, this is the two-stage induction used in (b). Therefore every full-position constituent (S^\nu) generated by (U) obeys (3.3). This is the same induced-span argument used for a one-row completion at `se/artifacts/se_bridge2_md_inst_20260718.md:92-105`; (3.4) spells out the required containment rather than assuming it.

Substituting (3.2) into (3.3) yields
\[
\begin{aligned}
 2n-\nu_1
 &\ge 2n-(1+\sigma_1+\sigma'_1)\\
 &=((n-1)-\sigma_1)+(n-\sigma'_1)\\
 &=(k-\ell)+\ell=k.
\end{aligned}
\tag{3.5}
\]
Decomposing an arbitrary vector of (\operatorname{im}Q_k) into its orthogonal (K)-types and then into irreducible copies shows that **every** available full-position type (\nu\vdash2n) has at least (k) boxes below its first row.

### (d) Legal restriction pairs equal alphabet and full-position shapes

On legal NO words at (q=2n), a word is a bijection ([q]\to[q]). Identifying a bijection with a permutation gives the regular bimodule
\[
 L^2(S_q)\cong
 \bigoplus_{\lambda\vdash q}S^\lambda_{\mathrm{alph}}
 \boxtimes S^\lambda_{\mathrm{pos}}.
\tag{3.6}
\]
Here the alphabet group acts on values from the left and the full-position group acts on coordinates from the right; the two actions commute. Restriction \(R_q\) intertwines both actions, so it sends an ambient \((\lambda,\nu)\)-isotypic component into the legal \((\lambda,\nu)\)-isotypic component. By (3.6), that legal component is zero unless \(\nu=\lambda\). This bimodule statement and its character proof are at `se/artifacts/se_leakage_lemma_verdict.md:12-57`; the same restriction consequence is stated at `se/artifacts/se_one_defect_forgetting_bound.md:88-98`.

Now let (v\in\operatorname{im}Q_k\) have alphabet type (\lambda\) of defect (j<k). By (3.5), each full-position type (\nu) occurring in (v) has (2n-\nu_1\ge k), whereas (2n-\lambda_1=j<k). Hence (\nu\ne\lambda) for every such (\nu). Equation (3.6) therefore annihilates every position component of (v), and (R_qv=0).

### (e) Weight (k) supplies the opposite inequality

For completeness, we verify the alphabet fact used to identify the remaining defect. The permutation module (H\cong\mathbb C^q) is (H_0\oplus H_1), with (H_0) trivial and (H_1\cong S^{(q-1,1)}). A weight-(k) tensor is contained, after choosing its (k) nonconstant positions, in (H_1^{\otimes k}), hence in (H^{\otimes k}).

View \(H^{\otimes k}\) as the permutation module on \([q]^k\). A tuple with \(r\le k\) distinct alphabet values is fixed precisely by the copy of \(S_{q-r}\) that permutes the unused values, so its orbit module is \(\operatorname{Ind}_{S_{q-r}}^{S_q}\mathbf1\). If \(S^\lambda\) occurs in that orbit module, Frobenius reciprocity gives a nonzero \(S_{q-r}\)-fixed vector in \(S^\lambda\). Iterated Young branching from \(S_q\) to \(S_{q-r}\) then has a path from \(\lambda\) to the trivial shape \((q-r)\), so the row of \(q-r\) boxes must fit inside \(\lambda\). Thus \(\lambda_1\ge q-r\ge q-k\), or
\[
 \operatorname{def}(\lambda)\le k.
\tag{3.7}
\]
This is the independently stated weight-to-alphabet fact ((\dagger)) at `se/notes/SE_CARRIER_SUFFICIENCY_COMMISSION.md:820-835`; BR's basis facts used above are at `se/artifacts/references/BR_1310.5185v4_collision.tex:353-375`.

Since (\operatorname{im}Q_k\) has exact weight (k), (3.7) says that it has alphabet defect at most (k). Part (d) says that legal restriction kills every defect below (k). Therefore the only alphabet defect that can survive legal NO restriction is exactly (k). This proves (3.1). \(\square\)

Two useful operator forms follow. Position projectors commute with the diagonal alphabet action, (\Pi_0) is alphabet invariant, and hence (Q_kA_{2n,=j}=A_{2n,=j}Q_k). Taking the adjoint of (3.1), summing over (j<k), and using (3.7) gives
\[
 Q_kJ_N^*=Q_kW_{2n,k}A_{2n,=k}J_N^*.
\tag{3.8}
\]
The factor (W_{2n,k}) may be inserted because (Q_k=W_{2n,k}Q_k), proved at `se/artifacts/se_bridge2_writeups_20260717.md:27-50`.

## 4. Alphabet equivariance and transport to the YES side

We now prove, rather than assume, that (X), (Y), and the carrier projectors preserve alphabet isotypes.

Let (U_g:H\to H) be the permutation operator of (g\in S_q). Because (e_0) is constant, (U_ge_0=e_0), so
\[
 U_g\Pi_i=\Pi_iU_g\quad(i=0,1),
 \qquad e_0^*U_g=e_0^*.
\tag{4.1}
\]
BR defines maps (H\otimes H\to H)
\[
 \Psi_0:=\Pi_0\otimes e_0^*=e_0^*\otimes\Pi_0,
 \qquad
 \Psi_1:=\Pi_1\otimes e_0^*+e_0^*\otimes\Pi_1
\tag{4.2}
\]
at `se/artifacts/references/BR_1310.5185v4_collision.tex:483-490`. Equations (4.1)-(4.2) imply, term by term,
\[
 U_g\Psi_i=\Psi_i(U_g\otimes U_g)\quad(i=0,1),
 \qquad
 U_g(e_0^*\otimes\Pi_1)
 =(e_0^*\otimes\Pi_1)(U_g\otimes U_g).
\tag{4.3}
\]

For each matching (\mu), BR's formulas express (X_k^\mu) and (Y_k^\mu) as tensor products and sums of exactly the maps in (4.2)-(4.3):
\[
\begin{aligned}
 X_k^\mu&=\Psi_0\otimes
 \sum_{|c|=k}\Psi_{c_2}\otimes\cdots\otimes\Psi_{c_n},\\
 Y_k^\mu&=(e_0^*\otimes\Pi_1)\otimes
 \sum_{|c|=k-1}\Psi_{c_2}\otimes\cdots\otimes\Psi_{c_n}.
\end{aligned}
\tag{4.4}
\]
These formulas, including their leg convention, are at `se/artifacts/references/BR_1310.5185v4_collision.tex:525-531,545-553`. Thus every block intertwines the diagonal alphabet action. Stacking the blocks leaves the matching label fixed under alphabet permutations, so
\[
 (\mathbf1_M\otimes U_g^{\otimes n})T
 =T U_g^{\otimes2n},
 \qquad T\in\{X_{\mathrm{se},k},Y_{\mathrm{se},k}\}.
\tag{4.5}
\]

The position action commutes with the alphabet action. Therefore every position-isotypic projector (\bar\Pi_d^{(m)}), and hence (Q_k), commutes with the alphabet action. Equations (4.5) and (1.4) show that (\bar X_{\mathrm{se},k}) and (\bar Y_{\mathrm{se},k}) are alphabet intertwiners. Consequently, for every (\lambda\vdash q),
\[
 (\mathbf1_M\otimes A_{n,\lambda})\bar T_{\mathrm{se},k}
 =\bar T_{\mathrm{se},k}A_{2n,\lambda},
 \qquad \bar T\in\{\bar X,\bar Y\}.
\tag{4.6}
\]

Both carriers also have exact output weight (k). In (4.4), (X_k^\mu) has one (\Psi_0) output and exactly (k) (\Psi_1) outputs; (Y_k^\mu) has one (H_1) output from (e_0^*\otimes\Pi_1) and exactly (k-1) (\Psi_1) outputs. Since (\operatorname{im}\Psi_0\subseteq H_0) and (\operatorname{im}\Psi_1\subseteq H_1), both totals are (k). The Y count is audited at `se/artifacts/se_bridge2_ytransfer_20260718.md:96-109`; BR records the common weight support at `se/artifacts/references/BR_1310.5185v4_collision.tex:525-531`.

Finally, injective word sets are alphabet invariant, so (R_m) intertwines the ambient and legal alphabet actions. The corresponding YES projector commutation is proved at `se/artifacts/se_bridge2_ytransfer_20260718.md:139-152`, and the NO version at `se/artifacts/se_bridge2_writeups_20260717.md:113-166`. Combining those commutations, (3.8), (4.6), and the exact input/output weights proves, for (\bar T\in\{\bar X,\bar Y\}),
\[
\boxed{
 \mathcal R(\bar T_{\mathrm{se},k})
 =J_Y(\mathbf1_{M_{\mathrm{se}}}\otimes W_{n,k}A_{n,=k})
   \bar T_{\mathrm{se},k}
   (W_{2n,k}A_{2n,=k})J_N^*.
}
\tag{4.7}
\]
Thus every surviving block on both sides has
\[
 \lambda=(q-k,\theta)=(2n-k,\theta)
 \quad\text{for some }\theta\vdash k.
\tag{4.8}
\]
Equation (4.7) is exactly the identity requested as (4.5) in `se/artifacts/se_bridge2_ytransfer_20260718.md:224-232`.

## 5. Corollaries: assembled X-line and Y-line

The matched-degree legality lemma states that, for (q\ge m\), (\lambda=(q-k,\theta)), and exact weight (k),
\[
 \|R_mW_{m,k}A_{m,\lambda}\|^2
 \le r_{\mathrm{top}}(q,k,\theta),
\tag{5.1}
\]
with equality when (m=q). This is proved at `se/artifacts/se_bridge2_md_inst_20260718.md:51-59,189-202`; equality at (m=q) is proved at `se/artifacts/se_bridge2_md_inst_20260718.md:219-245`.

Fix (\theta\vdash k) and write (\lambda=(2n-k,\theta)). Applied to the two outer factors of (4.7), (5.1) gives
\[
\begin{aligned}
 \|W_{2n,k}A_{2n,\lambda}J_N^*\|^2
 &=r_{\mathrm{top}}(2n,k,\theta),\\
 \|J_Y(\mathbf1_M\otimes W_{n,k}A_{n,\lambda})\|^2
 &\le r_{\mathrm{top}}(2n,k,\theta).
\end{aligned}
\tag{5.2}
\]
The first line is the adjoint of the equality case (m=q=2n). The second is (5.1) with (m=n), using (J_Y=\mathbf1_M\otimes R_n) from (1.3). These are the parameter substitutions audited at `se/artifacts/se_bridge2_ytransfer_20260718.md:177-206`.

Distinct (\lambda)-isotypes are orthogonal on both the legal input and output spaces because the legal restrictions intertwine the alphabet action. Hence (4.7) is an orthogonal direct sum over (\theta\vdash k), and its operator norm is the maximum block norm.

**Corollary 5.1 (X-line).** For (0\le k\le n),
\[
 \boxed{
 \|\mathcal R(\bar X_{\mathrm{se},k})\|
 \le \max_{\theta\vdash k}r_{\mathrm{top}}(2n,k,\theta)
 =\rho_{n,k}.}
\tag{5.3}
\]

**Proof.** On the (\lambda)-block, factor (4.7) into the YES outer factor, the middle block
\[
 M_\lambda:=(\mathbf1_M\otimes W_{n,k}A_{n,\lambda})
 \bar X_{\mathrm{se},k}
 (W_{2n,k}A_{2n,\lambda}),
\]
and the NO outer factor. Orthogonal projections are contractions, so
\[
 \|M_\lambda\|\le\|\bar X_{\mathrm{se},k}\|\le1.
\]
The last inequality is BR's hard bound at `se/artifacts/references/BR_1310.5185v4_collision.tex:678-686,1341-1346`. The two square roots in (5.2) multiply to (r_{\mathrm{top}}(2n,k,\theta)). Taking the maximum over the orthogonal (\lambda)-blocks proves (5.3). \(\square\)

**Corollary 5.2 (Y-line).** For (0\le k\le n),
\[
 \boxed{
 \|\mathcal R(\bar Y_{\mathrm{se},k})\|
 \le \rho_{n,k}\,\|\bar Y_{\mathrm{se},k}\|.}
\tag{5.4}
\]
Moreover, in the certified witness range (0\le k<K:=\lfloor n^{1/3}\rfloor),
\[
 \boxed{
 \|\mathcal R(\bar Y_{\mathrm{se},k})\|
 \le \rho_{n,k}\sqrt2\sqrt{\frac{k}{n}}.}
\tag{5.5}
\]

**Proof.** Repeat the proof of Corollary 5.1 with
\[
 M_\lambda:=(\mathbf1_M\otimes W_{n,k}A_{n,\lambda})
 \bar Y_{\mathrm{se},k}
 (W_{2n,k}A_{2n,\lambda}).
\]
Then (\|M_\lambda\|\le\|\bar Y_{\mathrm{se},k}\|), and (5.2) proves (5.4). The independently certified ambient estimate
\[
 \|\bar Y_{\mathrm{se},k}\|\le\sqrt2\sqrt{k/n}
\]
holds for (0\le k<K), at (q=2n) (indeed for every (q\ge2)); its statement and range are `se/artifacts/se_stage2_py_verdict.md:11-31`. Substitution gives (5.5). \(\square\)

### Endpoints at (k=0)

For (k=0), (\theta=\varnothing), (\lambda=(2n)), and (r_{\mathrm{top}}(2n,0,\varnothing)=1). The matched-degree endpoint is proved separately by the constant function at `se/artifacts/se_bridge2_md_inst_20260718.md:204-206`, so the X argument gives
\[
 \|\mathcal R(\bar X_{\mathrm{se},0})\|\le1.
\tag{5.6}
\]
For Y, the sum ( |c|=k-1=-1) in (4.4) is empty, so (Y_{\mathrm{se},0}=\bar Y_{\mathrm{se},0}=0) and
\[
 \|\mathcal R(\bar Y_{\mathrm{se},0})\|=0.
\tag{5.7}
\]
This endpoint is also recorded at `se/artifacts/se_stage2_py_verdict.md:24-31`.

### NUMERICAL envelope only

Define
\[
 R_{n,k}:=\exp\!\left(
 \frac{k(k-1)}{2(2n-k+1)}+\frac{k}{2n-2k+1}
 \right).
\tag{5.8}
\]
This definition is at `se/artifacts/se_legal_diamond_query_norm_audit.md:348-359`. The only cited comparison with (\rho_{n,k}) is a finite exact-arithmetic scan, not an analytic proof: `se/artifacts/se_leakage_lemma_verdict.md:87-99` reports no violation on its tested ranges. Accordingly the envelope consequences are kept separate:

\[
\boxed{\text{NUMERICAL (tested parameters only):}\quad
 \rho_{n,k}\le R_{n,k},\qquad
 \|\mathcal R(\bar X_{\mathrm{se},k})\|\le R_{n,k},\qquad
 \|\mathcal R(\bar Y_{\mathrm{se},k})\|
 \le R_{n,k}\sqrt2\sqrt{k/n}.}
\tag{5.9-N}
\]
The last inequality additionally uses the certified ambient range (0\le k<K). Display (5.9-N) is not promoted to a theorem for unscanned (n,k).

### Sanity anchor, not used in the proof

At (n=3), the legal rebuild reports
\[
 \|\mathcal R(\bar X_k)\|=1,\ 1.2,\ 1.095445\ldots,
 \qquad
 \|\mathcal R(\bar Y_k)\|=0,\ 0.632455\ldots,\ 1.341640\ldots
\]
for (k=0,1,2), respectively (`se/artifacts/logs_se_bridge2_20260717/bridge2_n3.log:1-15`). For the requested consistency check, when (n=3,k=1), the only partition is (\theta=(1)), and (f^{(5,1)}=5); hence
\[
 \rho_{3,1}=r_{\mathrm{top}}(6,1,(1))=\frac{6}{5}=1.2,
\]
exactly the X-line anchor. No measured value enters any proof above.

## 6. Status summary

| step | verdict | sources |
|---|---|---|
| Setup, probability-(L^2) restriction, (J_Y=\mathbf1_M\otimes R_n) | **DEFINED / PROVED** | `se/artifacts/se_legal_diamond_query_norm_audit.md:55-83`; `se/artifacts/se_bridge2_writeups_20260717.md:54-111` |
| (a) Primed carrier subgroup types and first rows | **PROVED** | `se/artifacts/references/BR_1310.5185v4_collision.tex:600-611,632-646`; equation (3.2) |
| (b) LR first-row inequality | **PROVED IN THIS NOTE** | Lemma 2.1, including the LR convention and tableau proof |
| (c) Induced-module containment and full-position defect (\ge k) | **PROVED** | map (3.4); `se/artifacts/se_bridge2_md_inst_20260718.md:92-105` for the analogous induced-span step |
| (d) Legal regular bimodule pairs equal alphabet/position shapes | **PROVED** | `se/artifacts/se_leakage_lemma_verdict.md:12-57`; `se/artifacts/se_one_defect_forgetting_bound.md:88-98` |
| (e) Weight (k\Rightarrow) alphabet defect (\le k) | **PROVED** | proof around (3.7); `se/notes/SE_CARRIER_SUFFICIENCY_COMMISSION.md:820-835` |
| PIN: legal NO restriction kills every (j<k) | **PROVED** | Lemma 3.1, equations (3.1)-(3.8) |
| (f) (X/Y/Q_k) alphabet equivariance and YES transport | **PROVED** | `se/artifacts/references/BR_1310.5185v4_collision.tex:483-490,525-531,545-553,653-657`; `se/artifacts/se_bridge2_ytransfer_20260718.md:139-152` |
| Exact-(k) two-sided identity (the requested (4.5)) | **PROVED** | equation (4.7) |
| Matched-degree NO equality and YES bound | **PROVED** | `se/artifacts/se_bridge2_md_inst_20260718.md:51-59,189-202,219-245`; `se/artifacts/se_bridge2_ytransfer_20260718.md:177-206` |
| X-line analytic bound | **PROVED** | Corollary 5.1; BR norm at `se/artifacts/references/BR_1310.5185v4_collision.tex:678-686,1341-1346` |
| Y-line analytic bound | **PROVED** | Corollary 5.2; ambient bound at `se/artifacts/se_stage2_py_verdict.md:11-31` |
| (k=0) endpoints | **PROVED SEPARATELY** | `se/artifacts/se_bridge2_md_inst_20260718.md:204-206`; `se/artifacts/se_stage2_py_verdict.md:24-31` |
| (\rho_{n,k}\le R_{n,k}) envelope | **NUMERICAL ONLY** | `se/artifacts/se_leakage_lemma_verdict.md:87-99` |
| (n=3) rebuild | **SANITY CHECK ONLY** | `se/artifacts/logs_se_bridge2_20260717/bridge2_n3.log:1-15` |

**Final status.** Every analytic step (a)-(f), PIN, and both (r_{\mathrm{top}}) corollaries is proved. No analytic gap was found in the commissioned pinning route. The sole non-theorem retained in the requested package is the explicitly separated (R_{n,k}) envelope, for which the cited corpus supplies finite numerical verification but no all-parameter proof.
