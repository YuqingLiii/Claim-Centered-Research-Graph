# Independent Rule-7 review of se_frames2_20260719.md

Date: 2026-07-19  
Role: independent adversarial reviewer; I did not author R2  
Stop rule: no repairs and no DAG edits

## 0. Verdict

The scalar frame formula survives, but the rebuilt physical chain does not close.

On the single Specht module \(V_\lambda\), R2's frame satisfies

\[
 E_{\rm out,0}^{*}E_{\rm out,0}=B_\theta(q)Q_0,\qquad
 E_{\rm out,z}^{*}E_{\rm out,z}
 ={B_\theta(q)\over\delta_z+1}Q_z,\qquad
 B_\theta(q)={\binom qj f^\theta\over f^\lambda}.             \tag{R.1}
\]

The axial distance is \(\delta_z\); the changed top-row hook is
\(\delta_z+1\). The strict reflection is

\[
 J_{\rm refl}=p_0^{-1}Q_0-I
 ={1-p_0\over p_0}Q_0-\sum_zQ_z,\qquad
 p_0={f^{(q-j-1,\theta)}\over f^\lambda}.                    \tag{R.2}
\]

The break is R2's passage from these identities to the physical strict LR
carrier. R2 defines

\[
 E_{\rm out,z}:Q_zV_\lambda\longrightarrow\mathscr F_j^{\neg1},
 \qquad \dim Q_zV_\lambda=f^{\tau_z},                         \tag{R.3}
\]

but later tensors this map and its Gram with \(I_c\), claiming a domain of
dimension \(f^{\tau_z}c\). The earlier physical carrier is instead

\[
 \mathcal C=P_\xi V_\lambda
 \simeq(V_\kappa\boxtimes V_\nu)\otimes\mathbb C^c,\qquad
 \dim\mathcal C=f^\kappa f^\nu c,                            \tag{R.4}
\]

a subspace of one \(V_\lambda\), not \(V_\lambda\otimes\mathbb C^c\).
A non-\(H\)-normalizing partial injection moves between conjugate isotypic
carriers; it does not automatically produce \(Q_z\otimes I_c\).
The required recoupling/factorization is not defined or proved.

| Check | Verdict |
|---|---|
| Y1 independent Grams and reflection | **CONFIRMED**, subject to the freeze disclosure below |
| Y2 P1 definitions/identification | **GAP** |
| Y3 output frames | **CONFIRMED** on one \(V_\lambda\); **GAP/REFUTED AS TYPED** for the LR-\(c\) lift |
| Y4 canonical-Gram chain | **GAP**; constants are conditionally correct |
| Y5 gates | **CONFIRMED** in tested \(c=1\) regimes; \(c\ge2\) **UNTESTED** |
| Y6 honesty | **GAP**: ceiling respected, but “full analytic arbitrary \(c\)” is overstated |

**Overall Rule-7 verdict: GAP.** Do not promote the all-sector
\(C_Y'=15/4\) theorem or the resulting unconditional assembly claim.

## 1. Freeze protocol

The authoritative filesystem freeze time of
se/artifacts/logs_se_frames2rev_20260719/partA_frozen.md is
**2026-07-19T19:25:51-04:00**. I had not opened R2, the human review,
R1/reviews, BR:483--663, or the supplied tables. Part B inspection began
afterward, approximately **2026-07-19T19:26-04:00**, before the first gate
log was created at **19:29:40-04:00**.

Disclosure: the frozen file's manually typed line says 19:28:00, later than
its actual creation time. I left the frozen file unedited; the filesystem
time is authoritative.

Substantive disclosure: before R2 supplied the definition of \(\Phi_j\),
Part A used \(B_\theta(q)\) for the reciprocal fixed-fiber mass

\[
 {f^\lambda\over\binom qj f^\theta}.                         \tag{R.5}
\]

R2 uses \(B_\theta(q)\) for the analysis-frame redundancy. Trace forces
R2's convention once

\[
 \Phi_jv=(\Pi_D^\lambda v)_{|D|=j}                           \tag{R.6}
\]

is known. Thus Part A's symbol normalization and auxiliary last-step
coefficient are not a valid derivation of R2's map. Its content/hook
off-by-one conclusion and centered reflection were correct. The following
is my post-freeze derivation from R2's definitions, not a claim of accidental
pre-reading agreement.

## 2. Y1 and Y3: full independent derivation

Let

\[
 \theta\vdash j,\quad L=q-j,\quad\lambda=(L,\theta),\quad
 \eta=\theta-e_r,\quad t=\theta_r,\quad
 \tau_0=(L-1,\theta),\quad\tau_z=(L,\eta),\quad
 \delta_z=L-t+r.                                             \tag{R.7}
\]

The two contents are

\[
 c(1,L)=L-1,\qquad c(r+1,t)=t-r-1,\qquad
 c(1,L)-c(r+1,t)=\delta_z.                                  \tag{R.8}
\]

**Y1-ID-content: PASS.** Young orthogonal form gives squared \(+1\)
coordinates

\[
 {\delta_z-1\over2\delta_z},\qquad
 {\delta_z+1\over2\delta_z}.                                \tag{R.9}
\]

These rotate path coordinates; they do not determine the invariant trace.

### Full hook product

Define

\[
 D_\theta(L)=\prod_{s=1}^{L}(L-s+\theta'_s+1).               \tag{R.10}
\]

Every tail and head hook is respectively

\[
 h_\lambda(r+1,s)
 =\theta_r-s+(1+\theta'_s)-(r+1)+1=h_\theta(r,s),             \tag{R.11}
\]

\[
 h_\lambda(1,s)=L-s+\theta'_s+1.                             \tag{R.12}
\]

Hence

\[
 H(\lambda)=H(\theta)D_\theta(L),\qquad
 B_\theta(q)={D_\theta(L)\over L!}.                          \tag{R.13}
\]

Only column \(t\) changes:

\[
 \eta'_s=\begin{cases}\theta'_s-1,&s=t,\\
                       \theta'_s,&s\ne t.\end{cases}         \tag{R.14}
\]

The complete quotient is therefore

\[
\begin{aligned}
 {H(\lambda)H(\eta)\over H(\tau_z)H(\theta)}
 &= {D_\theta(L)\over D_\eta(L)}\\
 &=\prod_{s=1}^{L}{L-s+\theta'_s+1\over L-s+\eta'_s+1}\\
 &=\left(\prod_{s\ne t}1\right)
   {L-t+r+1\over L-t+(r-1)+1}\\
 &={\delta_z+1\over\delta_z}.
\end{aligned}                                                \tag{R.15}
\]

This is the written product demanded by the human review. R2's quotient is
correct and its category inventory is exhaustive, but R2 still says the
row/column factors “cancel pairwise” instead of writing (R.10)--(R.15).
**Y3-full-written-hook: GAP as spec compliance; formula CONFIRMED.**

### Frame trace

\[
 \sum_{|D|=j}\Pi_D^\lambda=B_\theta(q)I_{f^\lambda}.         \tag{R.16}
\]

Put

\[
 T_{\neg1}=\sum_{\substack{|D|=j\\1\notin D}}\Pi_D^\lambda,
 \qquad
 T_{\ni1}=\sum_{\substack{|D|=j\\1\in D}}\Pi_D^\lambda.      \tag{R.17}
\]

Both are \(f^\lambda\times f^\lambda\). On the long and tail children,

\[
 T_{\neg1}|_{V^{\tau_0}}=B_\theta(q)I_{f^{\tau_0}},          \tag{R.18}
\]

\[
 T_{\neg1}|_{V^{\tau_z}}
 =\left[B_\theta(q)-\binom{q-1}{j-1}{f^\eta\over f^{\tau_z}}\right]
 I_{f^{\tau_z}}.                                             \tag{R.19}
\]

With \(p_z=f^{\tau_z}/f^\lambda\) and \(r_z=f^\eta/f^\theta\),
(R.15) gives

\[
 {p_z\over(j/q)r_z}={\delta_z+1\over\delta_z}.               \tag{R.20}
\]

Since \(\binom{q-1}{j-1}/\binom qj=j/q\), (R.19) is exactly (R.1).
**Y1-frame-Gram: CONFIRMED on \(V_\lambda\).**

Branching gives

\[
 V^\lambda\downarrow S_{q-1}
 =V^{\tau_0}\oplus\bigoplus_zV^{\tau_z},\qquad
 I=Q_0+\sum_zQ_z.                                            \tag{R.21}
\]

Substitution into \(p_0^{-1}Q_0-I\) proves (R.2), whose normalized trace is

\[
 p_0{1-p_0\over p_0}-(1-p_0)=0.                             \tag{R.22}
\]

**Y1-reflection: CONFIRMED.**

## 3. Y2: definitions and Rule-7(g)

The literal kernel agrees with BR:483--490 and 522--553:

\[
 b_j(g)=\bigl(q\mathbf1[g(1)=1]-1\bigr)
 e_j(qx_2(g)-2,\ldots,qx_n(g)-2),\quad
 x_i(g)=\mathbf1[g(i)=i]+\mathbf1[g(\bar i)=i].              \tag{R.23}
\]

R2 now defines

\[
 r_h(\bar i)=\overline{h(i)},\quad
 \widehat b_h=\widehat b_0\rho(r_h^{-1}),\quad
 r_{h\cdot\pi}^{-1}=r_h^{-1}\pi,                             \tag{R.24}
\]

\[
 d_\sigma=\sigma\bar\sigma,\quad
 r_{h'}^{-1}=\bar\sigma^{-1}r_h^{-1},\quad
 L_\sigma=\rho(d_\sigma)|_{\mathcal O}.                     \tag{R.25}
\]

Here \(B_h:\mathcal C\to\mathcal O\) is \(R\times dc\). Direct
multiplication confirms both covariance reindexings. Therefore

\[
 G=I_d\otimes M_\xi,\qquad d=f^\kappa f^\nu,\qquad
 M_\xi={1\over d}\operatorname{Tr}_{V_\kappa\boxtimes V_\nu}G
 \in\operatorname{End}(\mathbb C^c).                         \tag{R.26}
\]

**Y2-matching covariance: CONFIRMED; CERTIFIED* ceiling because the actual
\(c\ge2\) compressed gate is absent.**

The induced dimensions are

\[
 M={q!f^\alpha f^\beta\over(q-j)!a!b!},\qquad
 T=\binom{n-1}{a}\binom{n-1-a}{b}f^\alpha f^\beta.           \tag{R.27}
\]

If its factors have the asserted norms, the typed \(dc\times T\) map obeys

\[
 U_h^*U_h\preceq I_T,\qquad\|U_h\|_{\rm HS}^2\le T.          \tag{R.28}
\]

That abstract no-\(c\) count is correct. The physical identification is not:

| Term | Finding |
|---|---|
| \(\widehat b_0,r_h,h\cdot\pi,h',d_\sigma,L_\sigma,P_{\rm comp},W_h,Q_{\lambda,\theta}\) | Resolved |
| \(J_{\rm raw}\) | Zero-one inclusion described, but retained-column predicate remains prose |
| \(\eta_{\rm BR}\) | Not a formula: extraction, normalization/nonzero proof, and raw-column dependence are absent |
| \(F_{\rm BR}\) | Depends on unresolved \(\eta_{\rm BR}\) |
| \(\mathcal B_\gamma\) in (4.5) | Undefined before use |
| Physical \(B_h\) factorization through \(U_h,J_{\rm refl},E_{\rm out,\gamma}\) | Asserted in prose, not a displayed typed identity |

R2 honestly denies the false equality \(\mathbb E_hU_hU_h^*=G\), but it
does not supply the replacement equality used in §4.2. This is an
all-parameter operator gap, not merely missing \(c=2\) corroboration.
**Y2-induced/physical identification: GAP; keep CONJECTURED.**

Literal unresolved source tokens also violate Rule 7(g): (2.5) prints
“ho_lambda” instead of rho; (3.7) prints “left[”; (5.1) has bare “quad”
three times.

## 4. Y3: per-sector multiplicity

The global maps are typed:

\[
 E_{\rm out,0}\;:\;Q_0V_\lambda\to\mathscr F_j^{\neg1}
 \quad\hbox{is}\quad
 \binom{q-1}{j}f^\theta\times f^{\tau_0},                    \tag{R.29}
\]

\[
 E_{\rm out,z}\;:\;Q_zV_\lambda\to\mathscr F_j^{\neg1}
 \quad\hbox{is}\quad
 \binom{q-1}{j}f^\theta\times f^{\tau_z}.                    \tag{R.30}
\]

R2 writes a genuine reduced-word Young-matrix path sum. **Y3-path-sum:
CONFIRMED**, though it is a generic seminormal matrix-element sum rather
than a closed Pieri coefficient.

The claimed per-sector lift

\[
 E_{\rm out,z}\otimes I_c:
 (Q_zV_\lambda)\otimes\mathbb C^c
 \longrightarrow\mathscr F_j^{\neg1}\otimes\mathbb C^c       \tag{R.31}
\]

is not the map defined in (3.2) and not the carrier (R.4). The absent
non-normalizing transport must be displayed on a \(dc\)-dimensional domain.
**Y3-\(c\)-tensor: REFUTED AS TYPED.** This does not refute global (R.1).

## 5. Y4: chain and constants

The one-copy weighted equality is correct:

\[
 E_{\rm out,0}^*E_{\rm out,0}
 +\sum_z(\delta_z+1)E_{\rm out,z}^*E_{\rm out,z}
 =B_\theta(q)I_{f^\lambda}.                                 \tag{R.32}
\]

The HS count (R.28), Schur reduction (R.26), and positivity
\(\|M_\xi\|\le\operatorname{Tr}M_\xi\) are correct. R2 nevertheless jumps
from prose factorization to

\[
 \|P_{\rm comp}\mathcal B_0P_\xi\|_{\rm HS}^2\le B_\theta(q)^2T,
 \qquad
 \sum_z\|P_{\rm comp}\mathcal B_zP_\xi\|_{\rm HS}^2
 \le {B_\theta(q)^2\over\delta_{\min}+1}T,                   \tag{R.33}
\]

without defining \(\mathcal B_\gamma\). It then replaces the complete
normalization derivation by a sentence about the coset coefficient and
\(d_Y/d_N\), despite the required scalars

\[
 \gamma^2={q^{-3n}\over n!},\qquad
 d_Y={q!\over n!q^n},\qquad d_N={q!\over q^q}.               \tag{R.34}
\]

Thus R2 does not derive from the physical map

\[
 \|\mathsf G_{\rm can}^{\lambda,\xi}\|
 \le r_{\rm top}{T\over d}
 \left(\omega+{1\over\omega(\delta_{\min}+1)}\right).        \tag{R.35}
\]

The subsequent scalar estimates are correct:

\[
 {T\over d}
 ={\binom{n-1-a}{b}\over\binom nb}
 {1\over h_{n-1}(\alpha)h_n(\beta)}
 \le\exp\left({a\over n-2a}+{b\over n-2b+1}\right)\le e,
 \quad n\ge3j,                                               \tag{R.36}
\]

\[
 \delta_{\min}\ge q-2j+1,\qquad
 {j\over q}\le\omega\le{j\over q-2j}.                       \tag{R.37}
\]

For \(j=1\), \(5e/4<15/4\); for \(j\ge2\), the parenthesis in
(R.35) is at most one and \(e<3\). I checked 14,568 split/shape instances
and 594 head/tail instances.

**Y4-hook/range: CONFIRMED. Y4-\(C_Y'\): GAP as an unconditional theorem;
CONFIRMED only conditional on (R.33) and its normalization bridge.**

Conditional arithmetic:

\[
 \|C_{j+1\to j}\|
 \le\sqrt{15/8}\,r_{\rm top}\sqrt{j/(n-j)},                  \tag{R.38}
\]

\[
 M'={2\over3\sqrt3}\left(\sqrt2+\sqrt{15/8}\right)
 ={4\sqrt6+3\sqrt{10}\over18},                              \tag{R.39}
\]

\[
 c'={1\over2(1+M')}
 ={9\over18+4\sqrt6+3\sqrt{10}}
 =0.2413852814754581733126245049897\ldots.                  \tag{R.40}
\]

**Y4-assembly arithmetic: CONFIRMED CONDITIONAL.**

## 6. Y5 gates

**G-FRAME-1 — \(c=1\), explicit matrices: PASS.**

\[
 \begin{array}{c|c|c|c}
 q&B_\theta(q)&\delta&B_\theta(q)/(\delta+1)\\ \hline
 6&6/5&5&1/5\\
 8&8/7&7&1/7
 \end{array}                                                 \tag{R.41}
\]

Both subgroup-average matrix residuals are exactly zero.

**G-CAN-1 — \(c=1\), fresh literal-BR construction: PASS.** My script
imports no proposer/reviewer module. It enumerates \(S_q\), forms (R.23),
averages all matchings, and independently builds completion and
\(H\)-central projectors in point, two-subset, and exterior-square modules:

\[
 \begin{array}{c|c|c}
 (n,q,j,\theta)&(a,b)&\mathsf G_{\rm can}\\ \hline
 (3,6,1,(1))&(1,0),(0,1)&3/10,\ 7/30\\
 (4,8,1,(1))&(1,0),(0,1)&4/21,\ 1/6\\
 (4,8,2,(2))&(0,2),(1,1)&106/315,\ 359/945\\
 (4,8,2,(1,1))&(0,2),(1,1),(2,0)&31/105,\ 157/630,\ 64/105
 \end{array}                                                 \tag{R.42}
\]

All nine compressed matrices have exact rational residual zero.

**G-BOUND-1: PASS.** All nine anchors, all six \((5,10,2)\) values, and
all 40 supplied \(j\le3\) sectors lie below \((15/4)r_{\rm top}\).
The largest value/cap ratios are \(0.106666666666667\) for the first 15 and
\(0.060606060606061\) for the 40-sector sweep. This is evidence, not the
missing operator proof.

**G-ID-1: PASS.** 594 stable shapes verify (R.15), (R.20), branching
probability one, (R.37), and the frame scalar exactly.

**G-ID-2: PASS.** 14,568 split/shape points verify (R.36).

**G-C2-1: UNTESTED.** The named regime remains

\[
 (n,q,j,\theta,\alpha,\beta,c)
 =(7,14,6,(3,2,1),(2,1),(2,1),2),\quad
 f^\lambda=23296,\quad\dim\mathcal C=16\cdot35\cdot2=1120. \tag{R.43}
\]

No recommendation exceeds **CERTIFIED*** across this regime.

## 7. Promotion recommendations

| Claim | Verdict | Recommendation |
|---|---|---|
| Literal kernel, matching covariance, Schur form | **CONFIRMED** | **CERTIFIED***, G-C2-1 named |
| Abstract \(U_h\) contraction | **CONFIRMED conditionally** | **CERTIFIED*** as an abstract map |
| \(U_h/F_{\rm BR}\) equals physical BR block | **GAP** | **CONJECTURED** |
| Global output frames/path matrices | **CONFIRMED** | **CERTIFIED*** |
| Global frame Gram and weighted equality | **CONFIRMED** | **CERTIFIED*** |
| Per-sector “tensor \(I_c\)” | **REFUTED AS TYPED** | Do not promote |
| Reflection split | **CONFIRMED** | **CERTIFIED*** with physical-chain caveat |
| Physical HS bound/normalization/(R.35) | **GAP** | **CONJECTURED** |
| All-sector \(C_Y'=15/4\) | **GAP** | **CONJECTURED** |
| Assembly constant | **CONFIRMED CONDITIONAL** | **CERTIFIED*** only as conditional arithmetic |

R2's overall pending-review ceiling is conservative, but “full analytic
arbitrary \(c\)” and “all-\(c\) lift by \(I_c\)” are unsupported. The
status must name both the untested \(c\ge2\) gate and the unresolved
physical factorization.

## 8. Reproduction

Python: <machine-local-path-redacted>

Logs and scripts are in se/artifacts/logs_se_frames2rev_20260719/.
independent_gates.py is the fresh matrix/literal-kernel constructor;
symbolic_checks.py performs the formula sweeps; proposer_rerun.log records
a clean R2 rerun; partA_frozen.md is the unedited freeze. SHA-256 values are
in SHA256SUMS.txt.
