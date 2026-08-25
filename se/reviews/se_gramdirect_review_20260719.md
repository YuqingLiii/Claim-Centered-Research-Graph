# Independent Rule-6 review of se_gramdirect_20260719.md

Date: 2026-07-19  
Role: independent adversarial reviewer under DAG_PROTOCOL rule 6  
Object: se/artifacts/se_gramdirect_20260719.md

## Outcome and reproduction record

I found no normalization gap or analytic failure. The physical subset/tableau transport is unitary on every retained raw column; the input and output fixed-set frames supply exactly two factors of \(B_\theta(q)\). Completion commutes with the query-branch projectors, so all cross terms vanish before the multiplicity trace.

Independent script: se/artifacts/logs_se_gramdirectrev_20260719/independent_checks.mjs  
Raw log: se/artifacts/logs_se_gramdirectrev_20260719/independent_checks.log  
SHA-256: c43bce8bc15ce4490e58ebd7a23f0b9e98b9b600167db841918b8fa60d233206

The program imports no proposer module or saved output. It implements Young seminormal representations, fixed-set projectors by subgroup branching, input isotypic projectors by character averages, and the BR reflection contraction. PowerShell could not start because its sandbox helper was absent, and apply_patch also failed in the new requested directory; the in-scope Node/V8 filesystem surface was therefore used. The raw log records this exception.

## V1. Normalization chain

**Verdict: CONFIRMED.**

The Fourier coefficient squared is \(q^{-3n}/n!\). With \(q=2n\),

\[
d_Y=\frac{q!}{n!q^n},\qquad
C_{N,\mathrm{count}}=\frac{q!}{q^q}r_{\rm top}\omega,
\]

so

\[
\frac{q^{-3n}/n!}{d_YC_{N,\mathrm{count}}}
=\frac1{(q!)^2r_{\rm top}\omega}.
\]

This is (1.11), with no residual \(n!\), \(q^n\), or \(q!\). Also

\[
B_\theta(q)=\frac{\binom qj f^\theta}{f^\lambda},\qquad
\frac{r_{\rm top}}{B_\theta(q)}
=\frac{q^j(q-j)!}{q!}.
\]

Substituting \(\widehat b_jP=q^j(q-j)!RP\) gives
\(r_{\rm top}/(B_\theta^2\omega)\), hence (1.12); normalized partial trace and division by \(d=f^\kappa f^\nu\) give (1.13).

| point | \(d_Y\) | \(C_{N,\rm count}\) | \(r_{\rm top},p_0,\omega,B_\theta\) | (1.11) scalar |
|---|---:|---:|---:|---:|
| \((3,6,1)\) | \(5/9\) | \(1/216\) | \(6/5,4/5,1/4,6/5\) | \(1/155520\) |
| \((4,8,1)\) | \(105/256\) | \(15/32768\) | \(8/7,6/7,1/6,8/7\) | \(1/309657600\) |

At both points \(q^j(q-j)!/q!=r_{\rm top}/B_\theta=1\).

## V2. Seed, fixed-set reflection, and cosets

**Verdict: CONFIRMED.**

BR:544--553 has one queried \(\Pi_1\otimes e_0^*\) factor and \(j\) tail \(\Psi_1\) factors. In permutation coordinates these are \(q{\bf1}[g(1)=1]-1\) and \(qx_i(g)-2\), giving (1.3).

For \(|D|=j\), extensions of \(p\) are uniquely \(\tau_ps\), with \(s\) fixing \(D\) pointwise:

\[
\sum_{g:g|_D=p}\rho_\lambda(g)
=(q-j)!\rho_\lambda(\tau_p)\Pi_D^\lambda.
\]

Queried extensions number \((q-j-1)!\); relative to \((q-j)!\), their coefficient is \(q/(q-j)\). This proves (1.4), including its sign. The projector notation must be read cardinality-wise:
\(\Pi_E=(q-|E|)!^{-1}\sum_{s:s|_E={\rm id}}\rho(s)\); thus the \(D\cup\{1\}\) denominator is \((q-j-1)!\).

Expanding \(e_j\), strict \((a,b)\) support kills every term with fewer than \(j\) pins. The surviving \(A^\circ\)- and \(B\)-pin sets are disjoint because a permutation cannot map both \(i\) and \(\bar i\) to \(i\). Coset summation therefore gives exactly

\[
\widehat b_j(\lambda)P=q^j(q-j)!R_{a,b}^{\lambda,j}P.
\]

There is no extra binomial or \(2^j\).

## V3. Strict query reflection

**Verdict: CONFIRMED.**

The free fixed-set frame has scalar \(B_\theta(q)\). Strictness forces the input \(H\)-type through \(\tau_0\). The pinned \(S_{q-1}\)-central sum has scalar

\[
\frac q{q-j}\binom{q-1}{j}\frac{f^\theta}{f^{\tau_0}}
=\frac{B_\theta(q)}{p_0}
\]

on \(Q_0\) and vanishes on strict tail children. After division by the free frame, pinned minus free is

\[
p_0^{-1}Q_0-I=\omega Q_0-\sum_cQ_c.
\]

Thus (5.1) has neither an omitted \(B_\theta\) nor affine-content eigenvalues.

## V4. Hilbert--Schmidt count

**Verdict: CONFIRMED.**

A retained raw column is indexed by

\[
I_A\in\binom{[n-1]}a,\qquad
I_B\in\binom{[n-1]\setminus I_A}b,
\]

and a basis vector of \(V_\alpha\otimes V_\beta\). Hence

\[
\mathcal T=\binom{n-1}{a}\binom{n-1-a}{b}f^\alpha f^\beta.
\]

The unmatched \(B\)-site is excluded, and no pair is counted twice. Every raw column has norm one. The physical \(\rho_\theta(\sigma_{I_A,I_B})\) and LR-copy transports are unitary; the \((\kappa,\nu)\), complete-\(\theta\), and all-LR-copy projections are contractive. Therefore
\(\|\mathcal U_{\rm BR}P\|_{\rm HS}^2\le\mathcal T\).

Nonorthogonal output columns do not spoil this: a raw operator's HS norm is the sum of its column norms. Output overlap is controlled by the subsequent frame inequality.

## V5. Output frames and \(\delta_c\)

**Verdict: CONFIRMED.**

Let \(L=q-j\). The strip box in column \(s\) has content \(s-\theta'_s-1\). Replacing the column-\(t\) box by the last box gives tail ratio

\[
\frac1{q-j-t+\theta'_t+1}=\frac1{\delta_c+1}.
\]

Thus

\[
E_{{\rm out},0}^*E_{{\rm out},0}=B_\theta\Pi_0,\qquad
E_{{\rm out},c}^*E_{{\rm out},c}
=\frac{B_\theta}{\delta_c+1}\Pi_c.
\]

The residual Pieri projectors are mutually orthogonal, proving (5.5). Since \(t\le\theta_1\le j\) and \(\theta'_t\ge1\),

\[
\delta_c=q-j-t+\theta'_t\ge q-2j+1.
\]

## V6. Composition and the second \(B_\theta\)

**Verdict: CONFIRMED.**

\(P_{\rm comp}\) averages \(S_B\), and \(S_B\) fixes the queried alphabet value, so \(S_B\le S_{q-1}\). Hence \([P_{\rm comp},Q_\gamma]=0\). For \(\gamma\ne\eta\),

\[
\mathcal B_\gamma^*P_{\rm comp}\mathcal B_\eta
=\mathcal B^*Q_\gamma P_{\rm comp}Q_\eta\mathcal B=0.
\]

This kills \(Q_0/Q_c\) and \(Q_c/Q_{c'}\) cross terms.

The exact factorization is
\(\mathcal B_\gamma=E_{{\rm out},\gamma}\mathcal U_{\rm BR}E_{\rm in}^*\).
The output Gram contributes the first \(B_\theta\). The strict input fixed-set frame has
\(\|E_{\rm in}\|^2=B_\theta(q)\), supplying the second. V4 and completion contractivity give

\[
\|P_{\rm comp}\mathcal B_0P\|_{\rm HS}^2\le B_\theta^2\mathcal T,
\]

\[
\sum_c\|P_{\rm comp}\mathcal B_cP\|_{\rm HS}^2
\le\frac{B_\theta^2}{\delta_{\min}+1}\mathcal T.
\]

Equation (5.1) weights the orthogonal branches by \(\omega^2\) and \(1\), so the result is exactly
\(\omega^2+1/(\delta_{\min}+1)\). There is no third frame factor or mixed \(2\omega\) term.

## V7. Multiplicity trace

**Verdict: CONFIRMED.**

For \(d=f^\kappa f^\nu\),

\[
M_\xi=\frac1d\operatorname{Tr}_{V_\kappa\otimes V_\nu}
(PR^*P_{\rm comp}RP)\succeq0.
\]

Thus \(d\,\operatorname{Tr}M_\xi\) equals the full carrier trace and is bounded by V6. Since \(\|M_\xi\|\le\operatorname{Tr}M_\xi\), division by \(d\) and insertion of the (1.12) scalar gives (5.8).

All \(c\) LR directions are already inside one trace. A factor \(c\) would arise only from separately bounding and summing \(c\) columns; that is not done. The reasoning is unchanged for \(c\ge2\).

## V8. Hook bounds, constants, and endpoints

**Verdict: CONFIRMED.**

For \(m=n-1\),

\[
f^{(M-t,\gamma)}=\binom Mt f^\gamma h_M(\gamma),\qquad
h_M(\gamma)\ge\exp\left(-\frac t{M-2t+1}\right).
\]

Therefore

\[
\frac{\mathcal T}{d}
=\frac{\binom{m-a}b}{\binom nb}
\frac1{h_m(\alpha)h_n(\beta)}
\le\exp\left(\frac a{n-2a}+\frac b{n-2b+1}\right).
\]

For \(n\ge3j\), the exponent is at most
\((a+b)/(n-2j)=j/(n-2j)\le1\), so \(\mathcal T/d\le e<3\).

Also

\[
\frac jq\le\omega\le\frac j{q-2j},\qquad
\delta_{\min}+1\ge q-2j+2.
\]

At \(q=2n,n\ge3j\), \(\omega\le1/4\). For \(j=1\), the reciprocal term is at most one, so the relative factor is at most \(5e/4<15/4\). For \(j\ge2\),

\[
\frac1{\omega(\delta_{\min}+1)}
\le\frac q{j(q-2j+2)}\le\frac34;
\]

the bracket is at most one and the relative factor is below \(e<3\). An exact-shape scan over \(j\le8\), \(3j\le n\le40\), found maxima \(11/6\) and \(367/275\), respectively.

Finally,

\[
r_{\rm top}=\frac{q^j}{(q)_j}\frac1{h_q(\theta)}
\le\exp\left(\frac{j(j-1)}{2(q-j+1)}+\frac j{q-2j+1}\right).
\]

For \(j=1,n\ge3\), \(r_{\rm top}\le6/5\). For \(j\ge2\) in the taper, \(n\ge j^3\); both denominators are at least \(3n/2\), yielding the note's exponent at most \(1/(3j)+2/(3j^2)\le1/3\). The absolute \(9/2\) bound follows.

At \(n=2,j=1\), the apparent \(2/3\) formula belongs to the invalid sequence \((0,1)\); the only admissible sector is \(1/3\). At \(n=1\) the strict first-defect sector is empty.

## V9. Independent computations

**Verdict: CONFIRMED.**

The exact \(j=1\) tables are:

| \((n,q)\) | internal \(A,B\) | canonical \(A,B\) | branches |
|---|---|---|---|
| \((3,6)\) | \(7/36,1/4\) | \(7/30,3/10\) | \(1/15,1/6,0,3/10\) |
| \((4,8)\) | \(7/48,1/6\) | \(1/6,4/21\) | \(1/42,1/7,0,4/21\) |
| \((5,10)\) | \(23/200,1/8\) | \(23/180,5/36\) | \(1/90,7/60,0,5/36\) |

These reproduce all six known canonical \(=r_{\rm top}\) times internal identities. The same formulas give G5a \(17/165,6/55\) at \(n=6\).

The five \((4,8,2)\) sectors are independently reconstructed as

\[
\theta=(2):\quad106/315,\ 359/945,
\]

\[
\theta=(1,1):\quad31/105,\ 157/630,\ 64/105.
\]

Projector residuals are below \(6.6\times10^{-16}\).

At the new point \((5,10,2)\):

| \(\theta\) | \((a,b)\) | sector | (5.8) envelope |
|---|---:|---:|---:|
| \((2)\) | \((0,2)\) | \(799/3024\) | \(1241/1008\) |
| \((2)\) | \((1,1)\) | \(1753/6048\) | \(6205/6048\) |
| \((2)\) | \((2,0)\) | \(80/189\) | \(6205/2016\) |
| \((1,1)\) | \((0,2)\) | \(61/252\) | \(445/504\) |
| \((1,1)\) | \((1,1)\) | \(37/168\) | \(445/504\) |
| \((1,1)\) | \((2,0)\) | \(25/63\) | \(445/252\) |

Every slack is positive. The sector rationals are unique modest-denominator reconstructions at the observed precision; projector residuals are below \(3.2\times10^{-15}\).

For G6,

\[
T=990080,\quad d=1485120,\quad T/d=2/3,\quad
\omega=6173/29667,\quad\delta_{\min}=28.
\]

The exact internal envelope is

\[
\frac{136910540}{549403173},
\]

and multiplying by \(r_{\rm top}=39366/20825\) gives the exact canonical envelope

\[
\frac{119769340392}{254251579505}.
\]

G4 is also correct: \(\sigma=(12)\) acts on \(S^{(2,1)}\) as
\(\operatorname{diag}(1,-1)\), and \(8/5-1=3/5\), giving
\(\operatorname{diag}(3/5,-3/5)\).

At every computed point, (5.8) strictly dominates every canonical sector.

## V10. Assembly

**Verdict: CONFIRMED.**

With \(C_N=1/4\) and \(C_Y=15/4\),

\[
\sqrt{C_NC_Y}=\frac{\sqrt{15}}4,\qquad
\frac{\sqrt{6C_Y}}2=\frac{3\sqrt{10}}4.
\]

These give exactly (6.1), together with the reviewed
\(\sqrt2\,\alpha_d\sqrt{d/n}\) term, the
\(\sqrt6/\sqrt{n-2d+1}\) term, the shifted \(\Phi\) denominator, and
\(\rho_d\). For \(K=\lfloor n^{1/3}\rfloor\), both \(\Phi\) terms are
\(O(K/\sqrt n)=O(n^{-1/6})\), and uniformly \(\rho_d=1+o(1)\). Hence

\[
\|D\|\le1+\frac{2\sqrt2}{3\sqrt3}+o(1).
\]

BR's factor-two mask gives denominator
\(2+4\sqrt2/(3\sqrt3)+o(1)\), while
\(\|\Gamma_n\|\ge K=(1-o(1))n^{1/3}\). Finally,

\[
\frac1{2+4\sqrt2/(3\sqrt3)}
=\frac{27-6\sqrt6}{38}
=0.3237647774552877\ldots.
\]

Thus (6.2), including its \(o(1)\) statements, follows.

## Verdict table

| Check | Verdict |
|---|---|
| V1 | **CONFIRMED** |
| V2 | **CONFIRMED** |
| V3 | **CONFIRMED** |
| V4 | **CONFIRMED** |
| V5 | **CONFIRMED** |
| V6 | **CONFIRMED** |
| V7 | **CONFIRMED** |
| V8 | **CONFIRMED** |
| V9 | **CONFIRMED** |
| V10 | **CONFIRMED** |

OVERALL RULE-6 VERDICT: **CONFIRMED.**

No DAG, node, or index file was edited.
