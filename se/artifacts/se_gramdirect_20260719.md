# Direct canonical Gram bound for Set Equality

Date: 2026-07-19  
Role: proposer on route (b), direct canonical-Gram bound  
DAG node: SE.denom.Phi.legal.tame  
Status: **CONJECTURED with exact numerical support — pending-review: an independent rule-6 reviewer must check the direct trace/Bessel derivation below.**  
No DAG, node, or index file was edited.

## 0. Outcome and target resolution

The canonical object in this note is

\[
 \mathsf G_{\rm can}^{\lambda,\xi}
 =\frac1{d_Y}C_N^{-1/2}
 \left(\frac1{n!}\sum_{h\in S_n}B_h^*B_h\right)
 C_N^{-1/2},
 \qquad d_Y=\frac{(q)_n}{q^n},
\]

on the gauge-fixed strict carrier, with \(h\) uniform over all \(n!\) bipartite matchings and query partner \(\bar h(1)\). This is the object defined as (0.2) and bounded in (0.3) of [se_bessel62_20260718.md](se_bessel62_20260718.md). The later opbridge3 note calls this canonical target (0.2). I resolve the numbering collision by the exact values: its maxima are \(3/10\) at \((n,q,j)=(3,6,1)\) and \(4/21\) at \((4,8,1)\). Thus “canonical target” below always means the displayed completed, matching-averaged, NO-whitened Gram, never the unscaled internal quantity whose corresponding maxima are \(1/4\) and \(1/6\).

T1 and all T2 gates land. T3 is not claimed: after the reviewed \(U_{\rm id}\) refutation, the ambient “internal sector” is not a source-defined gauge-independent matrix in the non-scalar cases. I therefore use the authorized T3′ fallback. Directly on the BR entries, the proposer derivation gives

\[
 \boxed{\|\mathsf G_{\rm can}^{\lambda,\xi}\|
 <\frac{15}{4}\,r_{\rm top}(q,j,\theta)}
 \tag{0.1}
\]

whenever \(n\ge3j\), including every LR multiplicity. In the taper this implies the absolute bound

\[
 \boxed{\|\mathsf G_{\rm can}^{\lambda,\xi}\|<\frac92.}
 \tag{0.2}
\]

The proof status is capped at CONJECTURED pending independent review.

## 1. T1: closed forms derived from the BR construction

Put

\[
 q=2n,\quad \lambda=(q-j,\theta),\quad \theta\vdash j,
\]
\[
 a+b=j,\quad \alpha\vdash a,\quad\beta\vdash b,
\]
\[
 \kappa=(n-1-a,\alpha),\quad \nu=(n-b,\beta),\quad
 c=c_{\alpha\beta}^{\theta},\quad d=f^\kappa f^\nu.
 \tag{1.1}
\]

Only tuples for which the displayed sequences are partitions are admissible. Let

\[
 H=S_{A\setminus\{1\}}\times S_B\cong S_{n-1}\times S_n
\]

and let \(P=P_{\kappa,\nu}^{\lambda,H}\) be its central isotypic projector:

\[
 P=\frac{f^\kappa f^\nu}{(n-1)!\,n!}
 \sum_{\sigma\in S_{n-1}}\sum_{\pi\in S_n}
 \chi_\kappa(\sigma^{-1})\chi_\nu(\pi^{-1})
 \rho_\lambda(\widehat\sigma_A\widehat\pi_B).
 \tag{1.2}
\]

Strictness forces the unique long query child
\(\tau_0=(q-j-1,\theta)\), and its multiplicity is exactly \(c\).

### 1.1 The BR seed

BR:544-553 gives the fixed-matching \(Z_{j+1}\) block. In permutation coordinates its canonical kernel is

\[
 b_j(g)=(q{\bf1}[g(1)=1]-1)
 e_j\!\left(qx_2(g)-2,\ldots,qx_n(g)-2\right),
 \tag{1.3}
\]

where \(x_i(g)={\bf1}[g(i)=i]+{\bf1}[g(\bar i)=i]\). Expanding the elementary symmetric polynomial and applying \(P\) kills every term with fewer than \(j\) tail pins. At degree \(j\), precisely \(a\) \(A^\circ\)-pins and \(b\) \(B\)-pins survive.

For disjoint \(I_A,I_B\subseteq\{2,\ldots,n\}\), with sizes \(a,b\), set

\[
 D=I_A\cup\{\bar i:i\in I_B\},\qquad
 p(i)=i,\quad p(\bar i)=i,
\]

and choose an extension \(\tau_p\in S_q\) that fixes 1. Define the exact fixed-set projector

\[
 \Pi_D^\lambda=\frac1{(q-j)!}
 \sum_{s:s|_D={\rm id}}\rho_\lambda(s).
\]

The direct BR reflection is

\[
 R_{I_A,I_B}
 =\rho_\lambda(\tau_p)
 \left(\frac q{q-j}\Pi_{D\cup\{1\}}^\lambda-\Pi_D^\lambda\right),
 \tag{1.4}
\]

and

\[
 R_{a,b}^{\lambda,j}
 =\sum_{\substack{I_A\cap I_B=\varnothing\\|I_A|=a,\ |I_B|=b}}
 R_{I_A,I_B}.
 \tag{1.5}
\]

No ambient map occurs here. Direct coset enumeration gives

\[
 \widehat b_j(\lambda)P
 =q^j(q-j)!\,R_{a,b}^{\lambda,j}P.
 \tag{1.6}
\]

The output completion projector is also explicit:

\[
 P_{\rm comp}^\lambda
 =\frac1{n!}\sum_{\pi\in S_{\{n+1,\ldots,q\}}}\rho_\lambda(\pi).
 \tag{1.7}
\]

### 1.2 Matching average and canonical whitening

Every SE matching is
\(\mu_h=\{(i,\bar h(i)):1\le i\le n\}\) for a unique \(h\in S_n\), and

\[
 \widehat b_h(\lambda)
 =\widehat b_0(\lambda)\rho_\lambda(r_h^{-1}).
 \tag{1.8}
\]

Thus the \(n!\)-matching stack is exactly the \(S_n^B\) twirl. Canonical-matching diagonal covariance upgrades it to the full \(H\)-twirl. On

\[
 PS^\lambda\cong V_\kappa\otimes V_\nu\otimes\mathbb C^c
\]

define the normalized multiplicity trace

\[
 \mathfrak m_\xi(X)
 =\frac1d\operatorname{Tr}_{V_\kappa\otimes V_\nu}(PXP).
 \tag{1.9}
\]

The correct Schur formula is
\(\mathcal T_H(X)=I_{V_\kappa\otimes V_\nu}\otimes\mathfrak m_\xi(X)\).

The actual fixed-matching Fourier coefficient is
\(q^{-3n/2}/\sqrt{n!}\). The canonical denominators are

\[
 d_Y=\frac{q!}{n!q^n},\qquad
 C_{N,\rm count}=\frac{q!}{q^q}r_{\rm top}\omega,
\]
\[
 r_{\rm top}=\frac{q^jf^\theta}{j!\,f^\lambda},\qquad
 p_0=\frac{f^{(q-j-1,\theta)}}{f^\lambda},\qquad
 \omega=\frac{1-p_0}{p_0}.
 \tag{1.10}
\]

Since \(q=2n\), the completed numerator divided by \(d_YC_{N,\rm count}\) has scalar \(1/((q!)^2r_{\rm top}\omega)\). Therefore the first closed form is

\[
 \boxed{
 \mathsf G_{\rm can}^{\lambda,\xi}
 =\frac1{(q!)^2r_{\rm top}\omega}
 \mathfrak m_\xi\!\left(
 \widehat b_j(\lambda)^*P_{\rm comp}^\lambda
 \widehat b_j(\lambda)\right).}
 \tag{1.11}
\]

Using (1.6), put

\[
 B_\theta(q)=\frac{\binom qj f^\theta}{f^\lambda}.
\]

Because
\(q^j(q-j)!/q!=r_{\rm top}/B_\theta(q)\), (1.11) becomes the no-\(q!\) formula

\[
 \boxed{
 \mathsf G_{\rm can}^{\lambda,\xi}
 =\frac{r_{\rm top}}{B_\theta(q)^2\omega}
 \mathfrak m_\xi\!\left(
 (R_{a,b}^{\lambda,j})^*P_{\rm comp}^\lambda
 R_{a,b}^{\lambda,j}\right).}
 \tag{1.12}
\]

For \(c=1\), the sector value is the scalar

\[
 \boxed{
 L_{n,j,\theta;\kappa,\nu}
 =\frac{r_{\rm top}}{B_\theta(q)^2\omega\,d}
 \left\|P_{\rm comp}^\lambda
 R_{a,b}^{\lambda,j}P\right\|_{\rm HS}^2.}
 \tag{1.13}
\]

For \(c>1\), (1.12) is a positive \(c\times c\) matrix and the sector value is its operator norm. Equations (1.2), (1.4), (1.5), (1.7), and (1.9) are finite character/Young-matrix sums, so (1.12) is an explicit closed form as a function of \((n,j,\theta,\xi)\).

### 1.3 Pieri/Young-6j resolution

Let \(Q_0,Q_c\) be the \(S_q\downarrow S_{q-1}\) branch projectors for

\[
 \tau_0=(q-j-1,\theta),\qquad
 \tau_c=(q-j,\theta-c).
\]

Because \(P_{\rm comp}\) commutes with these projectors,

\[
 R^*P_{\rm comp}R
 =\sum_\gamma R^*Q_\gamma P_{\rm comp}Q_\gamma R.
 \tag{1.14}
\]

In fixed subset/tableau/LR coordinates the physical BR transport in a colored block is

\[
 \rho_\theta(\sigma_{I_A,I_B})\otimes L_{I_A,I_B},
 \tag{1.15}
\]

not the refuted identity matrix. The short-injection output labels \((\rho,b)\) are obtained by the normalized Pieri associator \(F^\lambda\). Its entries are the Young-6j coefficients; for a two-path content gap \(\Delta\), their squared magnitudes are
\((\Delta-1)/(2\Delta)\) and \((\Delta+1)/(2\Delta)\). Thus (1.14), with (1.15) conjugated by \(F^\lambda\), is the explicit branch form. This retains the reflection signs and all LR-copy matrices.

## 2. Closed \(j=1\) specialization

There are two sectors:

\[
 A=((n-1),(n-1,1)),\qquad
 B=((n-2,1),(n)).
\]

Direct contraction of (1.13) in the standard representation gives

\[
 I_A=\frac{n^2-2}{2n^2(n-1)},\qquad
 I_B=\frac1{2(n-1)}
\tag{2.1}
\]

before the legal-conditioning factor, and

\[
 \boxed{
 L_A=\frac{n^2-2}{n(n-1)(2n-1)},\qquad
 L_B=\frac{n}{(n-1)(2n-1)}.}
\tag{2.2}
\]

The output-branch contributions are

\[
 L_{A,(n)}=\frac2{n(n-1)(2n-1)},\qquad
 L_{A,(n-1,1)}=\frac{n^2-4}{n(n-1)(2n-1)},
\]
\[
 L_{B,(n)}=0,\qquad
 L_{B,(n-1,1)}=\frac{n}{(n-1)(2n-1)}.
\tag{2.3}
\]

Equations (2.1)-(2.3) were evaluated by the closed-form script, not fitted from gate values.

## 3. T2: pre-registered gates

Provenance P1 for G1-G5 closed-form values: command
“node_repl dynamic import closed_form_eval.mjs; await run()”; raw log
[closed_form_eval.log](logs_se_gramdirect_20260719/closed_form_eval.log);
script [closed_form_eval.mjs](logs_se_gramdirect_20260719/closed_form_eval.mjs);
SHA-256
ed72269e73cf0e10687de3236c2063e99e3db2e5e9014e12f23935e55e38d6cb.

Provenance P2 for the independent G5 construction: command
“node_repl dynamic import brute_force_canonical.mjs; await run()”; raw log
[brute_force_canonical.log](logs_se_gramdirect_20260719/brute_force_canonical.log);
script [brute_force_canonical.mjs](logs_se_gramdirect_20260719/brute_force_canonical.mjs);
SHA-256
11e65320e0bafac4b68b3cbdfa8cfb5e4838d9220134488825196664b43968ab.

The two G5 programs share no helper functions. P1 uses the BR coset formula (1.12). P2 independently forms the BR Fourier kernel; at \(q=8\) it enumerates all \(40320\) permutations and all \(24\) matchings, while at \(q=12,j=1\) it sums all \(720\) matchings using direct partial-bijection extension counts.

| gate | exact result | verdict | provenance |
|---|---|---|---|
| G1, \((3,6,1)\) | internal \(A=7/36,B=1/4\); canonical \(A=7/30,B=3/10\); maximum \(3/10\); branches \(1/15,1/6,0,3/10\) | PASS | P1 |
| G2, \((4,8,1)\) | internal \(A=7/48,B=1/6\); canonical \(A=1/6,B=4/21\); maximum \(4/21\); branches \(1/42,1/7,0,4/21\) | PASS | P1 |
| G3, \((5,10,1)\) | internal \(A=23/200,B=1/8\); canonical \(A=23/180,B=5/36\); maximum \(5/36\) | PASS | P1 |
| G4, \((4,8,3,(2,1))\) | \(\sigma=(12)\), BR transport \(\operatorname{diag}(1,-1)\), reflected block \(\operatorname{diag}(3/5,-3/5)\) | PASS | P1 |
| G5a, \((6,12,1)\) | \(A=17/165,\ B=6/55\); independent maximum discrepancy \(4.302\times10^{-16}\) | PASS | P1, P2 |
| G5b, \((4,8,2),\theta=(2)\) | sectors \((a,b)=(0,2):106/315,\ (1,1):359/945\) | PASS | P1, P2 |
| G5b, \((4,8,2),\theta=(1,1)\) | sectors \((0,2):31/105,\ (1,1):157/630,\ (2,0):64/105\) | PASS | P1, P2 |
| G5b numerical comparison | maximum discrepancy over all five \(j=2\) sectors \(6.051\times10^{-14}\) | PASS | P1, P2 |

Aggregate gate command: “node_repl dynamic import verify_gates.mjs; await run()”; raw log
[verify_gates.log](logs_se_gramdirect_20260719/verify_gates.log);
script SHA-256
52c3d6ab1faf57c8ba6319bc3d13e4db3fad95f9407fa47b3214490c9d286b6b.

## 4. T3 verdict and G6 scope

The proposed equality

\[
 \mathsf G_{\rm can}=r_{\rm top}\,\mathsf G_{\rm internal}
\]

is not claimed here. The reviewed ambient source specifies support, column norms, and frame constants, but not a globally coherent tableau/LR transport or its matching parameter. The literal \(U_{\rm id}\) completion is refuted by G4. Therefore, beyond scalar \(j=1\) cases, “internal sector” has no source-fixed matrix whose entries can be compared at \(c=2\). Defining it to use the BR transports would make the identity a convention rather than a branching theorem.

Accordingly I stopped T3 and used T3′. Before the multiplicity-safe fallback argument, I ran the first \(c=2\) trace gate at

\[
 n=18,\ j=6,\ \theta=(3,2,1),\quad
 \alpha=\beta=(2,1),\quad
 c_{\alpha\beta}^{\theta}=2.
\]

The two LR lattice words are \(112\) and \(121\). The exact data are

\[
 d_\kappa=1105,\quad d_\nu=1344,\quad
 \mathcal T/(d_\kappa d_\nu)=2/3,
\]
\[
 \omega=6173/29667,\quad \delta_{\min}=28,
\]

and the direct multiplicity-safe trace envelope is
\(136910540/549403173\), approximately \(0.2491986699902077\).
After the out-of-taper \(r_{\rm top}=39366/20825\), its canonical envelope is approximately \(0.4710662589596407\).

This is explicitly a fallback trace gate, not a fabricated identity gate. Provenance P3: command
“node_repl dynamic import g6_multiplicity_trace.mjs; await run()”; raw log
[g6_multiplicity_trace.log](logs_se_gramdirect_20260719/g6_multiplicity_trace.log);
script [g6_multiplicity_trace.mjs](logs_se_gramdirect_20260719/g6_multiplicity_trace.mjs);
SHA-256
e0610bbf72c22407adb580134322341f7404b9e0920ea3ed999fe9cb29de1c2a.

## 5. T3′: direct canonical tail bound

This section is a proposer proof awaiting independent review.

### 5.1 Direct BR branch factorization

Resolve every term (1.4) into the query branches \(Q_0,Q_c\). After the strict input frame is normalized, the query reflection is

\[
 \omega Q_0-\sum_cQ_c.
 \tag{5.1}
\]

This follows directly from the free fixed-set sum and the pinned \(S_{q-1}\)-central sum: the long child has probability \(p_0\), so its coefficient is \(p_0^{-1}-1=\omega\), while every tail child has coefficient \(-1\).

Define \(\mathcal U_{\rm BR}\) on raw colored subset/tableau columns using the physical transport (1.15). Each retained raw column has norm one. Projection to \(V_\kappa\otimes V_\nu\) and to the full \(\theta\)-isotypic component, including all \(c\) LR copies, is contractive. Hence

\[
 \|\mathcal U_{\rm BR}P\|_{\rm HS}^2
 \le \mathcal T,\qquad
 \mathcal T=
 \binom{n-1}{a}\binom{n-1-a}{b}f^\alpha f^\beta.
 \tag{5.2}
\]

This count is insensitive to the reflection signs and transport matrices because they are unitary on each retained column. It does not replace them by identity.

### 5.2 Direct Pieri weighted Bessel estimate

For a removable corner \(c\) of \(\theta\), in column \(t(c)\), put

\[
 \delta_c=q-j-t(c)+\theta'_{t(c)},\qquad
 \delta_{\min}\ge q-2j+1.
 \tag{5.3}
\]

The normalized Pieri associator gives the exact output frame Grams

\[
 E_{{\rm out},0}^*E_{{\rm out},0}=B_\theta(q)\Pi_0,
\]
\[
 E_{{\rm out},c}^*E_{{\rm out},c}
 =\frac{B_\theta(q)}{\delta_c+1}\Pi_c,
 \tag{5.4}
\]

where the residual Pieri projectors are orthogonal. Equivalently,

\[
 E_{{\rm out},0}^*E_{{\rm out},0}
 +\sum_c(\delta_c+1)E_{{\rm out},c}^*E_{{\rm out},c}
 \preceq B_\theta(q)I.
 \tag{5.5}
\]

Compose (5.5) with the physical \(\mathcal U_{\rm BR}\) and the strict input frame. The input frame contributes a second \(B_\theta(q)\); completion is an orthogonal contraction. Thus

\[
 \|P_{\rm comp}\mathcal B_0P\|_{\rm HS}^2
 \le B_\theta(q)^2\mathcal T,
\]
\[
 \sum_c\|P_{\rm comp}\mathcal B_cP\|_{\rm HS}^2
 \le\frac{B_\theta(q)^2}{\delta_{\min}+1}\mathcal T.
 \tag{5.6}
\]

These are statements about the BR blocks with their transport retained. No ambient operator equality is invoked.

### 5.3 LR multiplicity is handled without scalarization

Let

\[
 M_\xi=\mathfrak m_\xi(R^*P_{\rm comp}R)\succeq0
\]

be the full \(c\times c\) multiplicity matrix. Equations (5.1) and (5.6) give

\[
 d\,\operatorname{Tr}M_\xi
 \le B_\theta(q)^2\mathcal T
 \left(\omega^2+\frac1{\delta_{\min}+1}\right).
 \tag{5.7}
\]

Since \(\|M_\xi\|\le\operatorname{Tr}M_\xi\), substituting (1.12) yields

\[
 \boxed{
 \|\mathsf G_{\rm can}^{\lambda,\xi}\|
 \le r_{\rm top}\frac{\mathcal T}{d}
 \left(\omega+
 \frac1{\omega(\delta_{\min}+1)}\right).}
 \tag{5.8}
\]

All LR directions were included before taking the trace. There is no factor \(c\), and (5.8) applies unchanged when \(c\ge2\).

### 5.4 Uniform constants

The hook formula gives

\[
 \frac{\mathcal T}{d}
 \le\exp\!\left(
 \frac a{n-2a}+\frac b{n-2b+1}\right)\le e
 \quad(n\ge3j).
 \tag{5.9}
\]

Also

\[
 \frac jq\le\omega\le\frac j{q-2j},\qquad
 \delta_{\min}\ge q-2j+1.
\]

For \(j=1\), (5.8)-(5.9) give a relative factor below \(15/4\). For \(j\ge2\), they give a relative factor below \(3\). Therefore (0.1) holds directly with

\[
 \boxed{C_Y=15/4.}
 \tag{5.10}
\]

For the absolute taper bound, use

\[
 r_{\rm top}\le e^{E_{2n}(j)},\qquad
 E_{2n}(j)=
 \frac{j(j-1)}{2(2n-j+1)}
 +\frac j{2n-2j+1}.
\]

When \(j=1,n\ge3\), \(r_{\rm top}\le6/5\), hence
\((15/4)r_{\rm top}\le9/2\). When \(j\ge2\) and
\(j\le\lfloor n^{1/3}\rfloor\), \(n\ge j^3\), and the two denominators are at least \(3n/2\). Hence

\[
 E_{2n}(j)\le\frac1{3j}+\frac2{3j^2}\le\frac13,
\]

so \(r_{\rm top}\le e^{1/3}<3/2\), and the sharper \(j\ge2\) estimate gives
\(3r_{\rm top}<9/2\). At \(n=2,j=1\), the only admissible direct sector has value \(1/3\); at \(n=1\) there is no strict first-defect sector. This proves the claimed absolute candidate (0.2) throughout the valid taper range.

## 6. T4: assembly arithmetic

Use the sharper relative constant \(C_Y=15/4\) from (5.10), not the looser absolute \(9/2\). With the established NO factor \(C_N=1/4\),

\[
 \sqrt{C_NC_Y}=\frac{\sqrt{15}}4,\qquad
 \frac{\sqrt{6C_Y}}2=\frac{3\sqrt{10}}4.
\]

The bessel62 defect envelope becomes

\[
\begin{aligned}
 \|D\|\le\max_{0\le d<K}\rho_d\Bigg[
 &|\beta_d|+\sqrt2\,\alpha_d\sqrt{d/n}
 +{\bf1}_{d\ge1}\frac{\sqrt6\,\alpha_d}{\sqrt{n-2d+1}}\\
 &+{\bf1}_{d\ge1}\frac{3\sqrt{10}}4
 \frac{\alpha_{d+1}}{\sqrt{n-2d-1}}
 \Bigg].
\end{aligned}
\tag{6.1}
\]

For \(K=\lfloor n^{1/3}\rfloor\), the two \(\Phi\) terms are
\(O(n^{-1/6})\), while the \(X/Y\) terms give

\[
 \|D\|\le1+\frac{2\sqrt2}{3\sqrt3}+o(1).
\]

After BR's factor-two mask,

\[
 \max_i\|\Gamma_n\circ\Delta_i\|
 \le2+\frac{4\sqrt2}{3\sqrt3}+o(1).
\]

Since \(\|\Gamma_n\|\ge K=(1-o(1))n^{1/3}\),

\[
 \boxed{
 \operatorname{Adv}^{\pm}(\mathrm{SE}(n,2n))
 \ge\left(\frac{27-6\sqrt6}{38}-o(1)\right)n^{1/3}}
\]
\[
 \boxed{
 \frac{27-6\sqrt6}{38}
 =0.3237647774552876\ldots.}
 \tag{6.2}
\]

In particular, any fixed \(c<(27-6\sqrt6)/38\), for example \(c=0.32\), holds for all sufficiently large \(n\), conditional only on independent acceptance of the direct derivation in Section 5.

Arithmetic provenance P4: command
“node_repl dynamic import assembly_arithmetic.mjs; await run()”; raw log
[assembly_arithmetic.log](logs_se_gramdirect_20260719/assembly_arithmetic.log);
script [assembly_arithmetic.mjs](logs_se_gramdirect_20260719/assembly_arithmetic.mjs);
SHA-256
c350cbffd2cc6e1bb2ada3aa3b645e018fed450cec45444a14b6c7f00c37abbd.

## 7. Execution note and final status

The configured WindowsApps Python command returned ENOENT, and the PowerShell runner could not start because its sandbox setup helper was missing. All computations stayed local and used repository-local standalone JavaScript modules in the persistent Node V8 runtime. No network or Mac execution was used. Raw record:
[environment.log](logs_se_gramdirect_20260719/environment.log).

Final status: **CONJECTURED with NUMERICAL gate support — pending-review: check equations (5.2), (5.6), and the multiplicity trace normalization (5.7) directly against the BR coset operator before any DAG promotion.**
