# Independent adversarial review #2 of the direct canonical Gram bound

Date: 2026-07-19  
Role: independent adversarial reviewer #2 under DAG_PROTOCOL rule 6  
Object: se/artifacts/se_gramdirect_20260719.md

## Outcome

**OVERALL RULE-6 VERDICT: CONFIRMED.**

I found no counterexample, normalization loss, invalid frame/Bessel step, LR-multiplicity factor, or endpoint failure. The direct estimate
\[
 \|\mathsf G_{\rm can}^{\lambda,\xi}\|<\frac{15}{4}r_{\rm top}\qquad(n\ge3j)
\]
is proved by the BR operator itself, and the T4 assembly constant
\[
 \frac{27-6\sqrt6}{38}=0.3237647774552876687\ldots
\]
is correct.

I did not open reviewer #1's file until my A/B verdicts and full derivation had been frozen in [ab_verdicts_pre_crosscheck.md](logs_se_gramdirectrev2_20260719/ab_verdicts_pre_crosscheck.md).

## Reproduction record

The independent evaluator imports no proposer or reviewer module. It uses Young's orthogonal form, canonical low-rank fixed-set invariant projectors, exact LR enumeration, central-character sector isolation, and the full normalized trace over all \(f^\kappa f^\nu\) vectors.

A deliberately adversarial first implementation tried one vector per isotypic component and failed the known tables. I discarded it: the fixed-matching pre-twirl Gram is not scalar. The corrected program evaluates the entire sector trace in batches.

Validation:

- all j=1 internal/canonical identities and completed output branches for n=3,...,8;
- all five \((4,8,2)\) sectors;
- maximum validation error \(6.67\times10^{-16}\);
- direct fixed-set-projector versus factorial subgroup average error \(1.34\times10^{-15}\).

Scripts and SHA-256 hashes:

    9e230a3e462a3d8e0add6741661b36900d6bc90a50245b3ae32e23c57eebdd64  assembly_and_constants_check.py
    8eb05ad0359ea56d0dc504dfe9e2f05f7f00ce128a97a0fd3463baf9e9156082  independent_closed_form.py
    c53d40c37b113051c4754f9fdac8023ac9110321bee290ab81f84456b6faba1d  run_points_incremental.py
    ef357a71952a3861dae976e02cfca0451f8fa0cd71991b3f8cabb7d84135b0f3  run_remaining_n10_two.py
    f3ff2337fada4dc0f779d840ff9a46ed6cd9059a7011efb8f44021f71af21d89  summarize_numeric.py
The main artifacts are [independent_closed_form.py](logs_se_gramdirectrev2_20260719/independent_closed_form.py), [validation.json](logs_se_gramdirectrev2_20260719/validation.json), [requested_j2_j3.json](logs_se_gramdirectrev2_20260719/requested_j2_j3.json), and [numeric_summary.log](logs_se_gramdirectrev2_20260719/numeric_summary.log). The configured shell and patch writer both failed at their Windows sandbox helper, so the available local Python runtime was launched through the Node execution surface and the workspace filesystem API was used. No network or project computation code was used.

## A. Counterexample hunt

**Verdict: CONFIRMED on every mandatory j=2 and j=3 sector; no counterexample.**

All 40 admissible sectors pass both (5.8) and the \(15r_{\rm top}/4\) bound. An independent LR census found no \(c>1\) case among these \(j\le4\) shapes; the first relevant multiplicity-two gate is the reviewed j=6 example.

| n | theta | (a,b) | alpha; beta | canonical | (5.8) envelope | ratio |
|---:|:---:|:---:|:---|---:|---:|---:|
| 6 | (2,) | (0,2) | (); (2,) | 0.212525252525253 | 0.988552188552189 | 0.214986376 |
| 6 | (2,) | (1,1) | (1,); (1,) | 0.230787878787879 | 0.88969696969697 | 0.259400545 |
| 6 | (2,) | (2,0) | (2,); () | 0.303030303030304 | 1.77939393939394 | 0.170299728 |
| 6 | (1, 1) | (0,2) | (); (1, 1) | 0.2 | 0.781818181818182 | 0.255813953 |
| 6 | (1, 1) | (1,1) | (1,); (1,) | 0.187272727272727 | 0.781818181818182 | 0.239534884 |
| 6 | (1, 1) | (2,0) | (1, 1); () | 0.29090909090909 | 1.3030303030303 | 0.223255814 |
| 7 | (2,) | (0,2) | (); (2,) | 0.176651126651126 | 0.867278554778555 | 0.203684417 |
| 7 | (2,) | (1,1) | (1,); (1,) | 0.190449365449365 | 0.809459984459984 | 0.235279531 |
| 7 | (2,) | (2,0) | (2,); () | 0.234965034965035 | 1.34909997409997 | 0.174164287 |
| 7 | (1, 1) | (0,2) | (); (1, 1) | 0.168997668997669 | 0.722027972027972 | 0.234059726 |
| 7 | (1, 1) | (1,1) | (1,); (1,) | 0.160644910644911 | 0.722027972027972 | 0.222491256 |
| 7 | (1, 1) | (2,0) | (1, 1); () | 0.228438228438228 | 1.08304195804196 | 0.210922787 |
| 9 | (3,) | (0,3) | (); (3,) | 0.217852525625635 | 0.932651906916613 | 0.233583960 |
| 9 | (3,) | (1,2) | (1,); (2,) | 0.202160534543488 | 0.710591929079324 | 0.284495962 |
| 9 | (3,) | (2,1) | (2,); (1,) | 0.230589158740419 | 0.839386716224952 | 0.274711470 |
| 9 | (3,) | (3,0) | (3,); () | 0.320701357466064 | 1.59883184042848 | 0.200584795 |
| 9 | (2, 1) | (0,3) | (); (2, 1) | 0.210986982498181 | 0.809256842099569 | 0.260716958 |
| 9 | (2, 1) | (1,2) | (1,); (2,) | 0.181493537228216 | 0.674380701749641 | 0.269126232 |
| 9 | (2, 1) | (1,2) | (1,); (1, 1) | 0.190444644223959 | 0.650295676687154 | 0.292858543 |
| 9 | (2, 1) | (2,1) | (2,); (1,) | 0.206385908885601 | 0.796612203941763 | 0.259079522 |
| 9 | (2, 1) | (2,1) | (1, 1); (1,) | 0.217436112681314 | 0.758678289468346 | 0.286598570 |
| 9 | (2, 1) | (3,0) | (2, 1); () | 0.312847446670976 | 1.32768700656961 | 0.235633433 |
| 9 | (1, 1, 1) | (0,3) | (); (1, 1, 1) | 0.20546218487395 | 0.676890756302521 | 0.303538175 |
| 9 | (1, 1, 1) | (1,2) | (1,); (1, 1) | 0.172103841536615 | 0.580192076830732 | 0.296632526 |
| 9 | (1, 1, 1) | (2,1) | (1, 1); (1,) | 0.196113445378152 | 0.676890756302521 | 0.289726878 |
| 9 | (1, 1, 1) | (3,0) | (1, 1, 1); () | 0.306302521008404 | 1.08302521008403 | 0.282821229 |
| 10 | (3,) | (0,3) | (); (3,) | 0.190998329156224 | 0.815204678362573 | 0.234294937 |
| 10 | (3,) | (1,2) | (1,); (2,) | 0.179538920831491 | 0.655075187969925 | 0.274073761 |
| 10 | (3,) | (2,1) | (2,); (1,) | 0.201266829018807 | 0.754819146632012 | 0.266642453 |
| 10 | (3,) | (3,0) | (3,); () | 0.26733500417711 | 1.27375730994152 | 0.209879074 |
| 10 | (2, 1) | (0,3) | (); (2, 1) | 0.186244903483396 | 0.729647769375222 | 0.255253166 |
| 10 | (2, 1) | (1,2) | (1,); (2,) | 0.163692993734739 | 0.62541237375019 | 0.261736097 |
| 10 | (2, 1) | (1,2) | (1,); (1, 1) | 0.170761306951439 | 0.608039807812685 | 0.280839025 |
| 10 | (2, 1) | (2,1) | (2,); (1,) | 0.183109087647032 | 0.720639772222442 | 0.254092398 |
| 10 | (2, 1) | (2,1) | (1, 1); (1,) | 0.191671945677258 | 0.694902637500212 | 0.275825613 |
| 10 | (2, 1) | (3,0) | (2, 1); () | 0.262297901616788 | 1.11184422000034 | 0.235912457 |
| 10 | (1, 1, 1) | (0,3) | (); (1, 1, 1) | 0.182318541451669 | 0.624928333906662 | 0.291743119 |
| 10 | (1, 1, 1) | (1,2) | (1,); (1, 1) | 0.156518747850017 | 0.546812292168329 | 0.286238532 |
| 10 | (1, 1, 1) | (2,1) | (1, 1); (1,) | 0.175438596491228 | 0.624928333906662 | 0.280733945 |
| 10 | (1, 1, 1) | (3,0) | (1, 1, 1); () | 0.257997936016512 | 0.937392500859993 | 0.275229358 |

The maximum ratio is
\[
 0.30353817504655534
\]
at \((n,j,\theta,a,b,\alpha,\beta)=(9,3,(1,1,1),0,3,\varnothing,(1,1,1))\). Nothing approaches one. The pointwise maxima fall from n=6 to 7 for both j=2 shapes and from n=9 to 10 for all three j=3 shapes. At fixed j this is evidence for decay, not saturation; I would extrapolate the ratio downward with n.

The optional full j=4 calculation was not feasible here: the two \(S_{24}\) carrier dimensions are 17,480 and 26,334, with sector trace ranks up to 3,200. The exact b=0 endpoint identity \(L=r_{\rm top}\omega\) nevertheless gives

| theta | exact canonical | exact (5.8) envelope | ratio |
|:---:|---:|---:|---:|
| (2,2) | \(8064/24035\) | \(9759744/8244005\) | 0.283404154863 |
| (2,1,1) | \(56064/168245\) | \(2887744/2456377\) | 0.283451164646 |

Both pass \(15r_{\rm top}/4\). This optional computational limitation does not affect the analytic proof below, which includes all j=4 sectors and all LR multiplicities.

## B. From-scratch derivation

**Verdict: CONFIRMED. I found no missing normalization, frame non-orthogonality, multiplicity loss, or endpoint failure.**

I use a query alphabet label \(x\), \(G=S_{[q]\setminus\{x\}}\), and write \(Q_0,Q_c\) for the central branch idempotents of \(G\).

### 1. Completion and query branches

The completion projector is the average of the subgroup permuting the \(n\) second-half alphabet labels. That subgroup fixes \(x\), hence lies in \(G\). Each \(Q_\gamma\) is a central element of the group algebra of \(G\), so it commutes with every element of that algebra, in particular with the subgroup average \(P_{\rm comp}\). Thus distinct query branches remain orthogonal after completion.

On a fixed j-set \(D\), let \(E_D\) be an orthonormal synthesis matrix for the invariant range of its pointwise stabilizer, so \(E_DE_D^*=\Pi_D^\lambda\). For the BR partial injection \(p:D\to K\),
\[
 \rho_\lambda(\tau_p)\Pi_D^\lambda
 =E_K\,[\rho_\theta(\sigma_p)\otimes L_p]\,E_D^*.
\]
This follows by standardizing the source and target active words in one fixed Young/LR basis. Both factors are unitary: \(\rho_\theta(\sigma_p)\) is a symmetric-group representation matrix and \(L_p\) is the restriction of the same unitary permutation action to the LR multiplicity space. This is not the refuted identity transport.

Summing all free j-set frames gives the central identity
\[
 \sum_{|D|=j}\Pi_D^\lambda=B_\theta(q)I,
 \qquad B_\theta(q)=\binom qj f^\theta/f^\lambda.
\]
After strict orbit isolation, the selected \((a,b)\) orbit has the same scalar on the strict input carrier. For the pinned frame only the long child \(\tau_0\) survives. Its pinned scalar, including \(q/(q-j)\), is \(B_\theta(q)/p_0\), whereas the free scalar is \(B_\theta(q)\). Dividing by the common strict-frame normalization therefore gives
\[
 J=\left(p_0^{-1}Q_0-I\right)
   =\omega Q_0-\sum_cQ_c,\qquad \omega=(1-p_0)/p_0.
\]
This proves the exact reflection coefficients; no Jucys-Murphy gap factor belongs in \(J\).

### 2. Why the raw count is T and has no c factor

Use the orthonormal raw basis
\[
 |I_A,T_\alpha;I_B,T_\beta\rangle.
\]
A column is retained exactly when \(I_A\cap I_B=\varnothing\) and the unmatched/query second-half site is absent. There are
\[
 {\cal T}=\binom{n-1}{a}\binom{n-1-a}{b}f^\alpha f^\beta
\]
such columns. Before the orthogonal representation projections, the BR map sends each retained column through the unitary block \(\rho_\theta(\sigma_p)\otimes L_p\), so each column has norm one. Hilbert-Schmidt norm is the sum of squared column norms and does not require different output columns to be orthogonal. Projecting the domain to \(V_\kappa\otimes V_\nu\) and the active module to the entire theta-isotypic space is contractive, so
\[
 \|{\cal U}_{\rm BR}P\|_{\rm HS}^2\le {\cal T}.
\]
The projection includes all \(c_{\alpha\beta}^{\theta}\) copies at once. Since the count is taken before that projection, no multiplicative \(c\) can appear.

### 3. The two frame factors and weighted output inequality

The strict input analysis frame has Gram bounded by \(B_\theta(q)I\). This supplies one factor \(B_\theta(q)\) in a squared Hilbert-Schmidt estimate.

For a tail corner in column \(t\), define
\[
 \delta_c=q-j-t+\theta'_t.
\]
In the Pieri horizontal strip, the long query child omits the final first-row box. Replacing the box in column \(t\) by that final box changes the normalized Pieri Gram by
\[
 \frac1{\delta_c+1}.
\]
Consequently, on mutually orthogonal residual Pieri domains \(\Pi_0,\Pi_c\),
\[
 E_{{\rm out},0}^*E_{{\rm out},0}=B_\theta(q)\Pi_0,\qquad
 E_{{\rm out},c}^*E_{{\rm out},c}
 =\frac{B_\theta(q)}{\delta_c+1}\Pi_c.
\]
Hence
\[
 E_{{\rm out},0}^*E_{{\rm out},0}
 +\sum_c(\delta_c+1)E_{{\rm out},c}^*E_{{\rm out},c}
 \preceq B_\theta(q)I.
\]
This is a single weighted Bessel inequality; it never sums separate corner norm bounds. Compose it with the physical BR transport and the strict input frame. The output inequality gives one \(B_\theta(q)\), the input frame gives the other, and \(P_{\rm comp}\) is an orthogonal contraction. Therefore
\[
 \|P_{\rm comp}{\cal B}_0P\|_{\rm HS}^2\le B_\theta(q)^2{\cal T},
\]
\[
 \sum_c\|P_{\rm comp}{\cal B}_cP\|_{\rm HS}^2
 \le\frac{B_\theta(q)^2}{\delta_{\min}+1}{\cal T}.
\]

### 4. Multiplicity trace and (5.8)

Let
\[
 M_\xi=\frac1d\operatorname{Tr}_{V_\kappa\otimes V_\nu}
 \bigl(P R^*P_{\rm comp}RP\bigr),\qquad d=f^\kappa f^\nu .
\]
It is a positive \(c\times c\) matrix and
\[
 d\,\operatorname{Tr}M_\xi
 =\operatorname{Tr}(P R^*P_{\rm comp}RP).
\]
Branch orthogonality, the reflection eigenvalues, and the two preceding bounds give
\[
 d\,\operatorname{Tr}M_\xi\le
 B_\theta(q)^2{\cal T}
 \left(\omega^2+\frac1{\delta_{\min}+1}\right).
\]
For a positive matrix, \(\|M_\xi\|\le\operatorname{Tr}M_\xi\), with no dimension factor. Multiplying by the exact canonical scalar \(r_{\rm top}/(B_\theta(q)^2\omega)\) yields
\[
 \|\mathsf G_{\rm can}^{\lambda,\xi}\|
 \le r_{\rm top}\frac{\cal T}{d}
 \left(\omega+\frac1{\omega(\delta_{\min}+1)}\right),
\]
which is (5.8).

### 5. Hook estimate and constants

For a stable shape \((M-t,\gamma)\), direct hook cancellation gives
\[
 f^{(M-t,\gamma)}=\binom Mt f^\gamma h_M(\gamma),
\]
\[
 h_M(\gamma)=\prod_{s=1}^{\gamma_1}
 \left(1+\frac{\gamma'_s}{M-t-s+1}\right)^{-1}.
\]
Since \(\log(1+x)\le x\), \(\sum_s\gamma'_s=t\), and
\(M-t-\gamma_1+1\ge M-2t+1\),
\[
 h_M(\gamma)\ge\exp\left(-\frac{t}{M-2t+1}\right).
\]
Substitution for \(\kappa\) and \(\nu\) gives
\[
 \frac{\cal T}{d}
 =\frac{\binom{n-1-a}{b}}{\binom nb}
   \frac1{h_{n-1}(\alpha)h_n(\beta)}
 \le\exp\left(\frac a{n-2a}+\frac b{n-2b+1}\right)\le e
\]
when \(n\ge3j\).

Branching and the corner hook ratio give
\[
 \frac jq\le\omega\le\frac j{q-2j},\qquad
 \delta_{\min}\ge q-2j+1.
\]
At \(q=2n\), \(n\ge3j\),
\[
 \omega\le\frac14,\qquad
 \frac1{\omega(\delta_{\min}+1)}
 \le\frac q{j(q-2j+2)}.
\]
For \(j=1\), the last displayed bound equals one, so the parenthesis is at most \(5/4\) and the relative factor is \(<5e/4<15/4\). For \(j\ge2\), it is at most \(3/(2j)\le3/4\); the parenthesis is at most one and the relative factor is \(<e<3\). This proves the claimed strict \(15/4\) bound.

### 6. Endpoints and taper boundary

At \(n=2,j=1\), partition admissibility leaves only \((a,b)=(0,1)\); direct evaluation gives \(1/3\). At \(n=1\) there is no strict first-defect sector.

For \(j=1,n\ge3\), \(r_{\rm top}=2n/(2n-1)\le6/5\), hence \((15/4)r_{\rm top}\le9/2\). For \(j\ge2\) and \(j\le\lfloor n^{1/3}\rfloor\), \(n\ge j^3\ge3j\). From the hook formula,
\[
 r_{\rm top}\le e^{E_{2n}(j)},\qquad
 E_{2n}(j)=\frac{j(j-1)}{2(2n-j+1)}
 +\frac j{2n-2j+1}.
\]
Both denominators are at least \(3n/2\), so
\[
 E_{2n}(j)\le\frac1{3j}+\frac2{3j^2}\le\frac13.
\]
Thus \(r_{\rm top}<3/2\), and the sharper \(j\ge2\) relative constant \(3\) gives \(3r_{\rm top}<9/2\). The taper boundary itself is included.

## T4 assembly

**CONFIRMED.** With \(C_N=1/4\), \(C_Y=15/4\),
\[
 \sqrt{C_NC_Y}=\sqrt{15}/4,\qquad
 \sqrt{6C_Y}/2=3\sqrt{10}/4.
\]
The two Phi terms are \(O(K/\sqrt n)=O(n^{-1/6})\). Maximizing
\(\sqrt2(K-d)\sqrt{d/n}\) gives \(d=K/3\) and
\(2\sqrt2/(3\sqrt3)+o(1)\). After BR's factor-two mask the denominator is
\[
 2+\frac{4\sqrt2}{3\sqrt3}+o(1).
\]
Its reciprocal is exactly
\[
 \frac1{2+4\sqrt2/(3\sqrt3)}
 =\frac{27-6\sqrt6}{38}
 =0.3237647774552876687\ldots.
\]


## C. Cross-check of reviewer #1

I opened se/artifacts/se_gramdirect_review_20260719.md only after freezing A and B. The reviews agree analytically.

My evaluator independently reproduces reviewer #1's new \((n,q,j)=(5,10,2)\) table exactly:

| theta | (a,b) | canonical | (5.8) envelope |
|:---:|:---:|---:|---:|
| (2) | (0,2) | \(799/3024\) | \(1241/1008\) |
| (2) | (1,1) | \(1753/6048\) | \(6205/6048\) |
| (2) | (2,0) | \(80/189\) | \(6205/2016\) |
| (1,1) | (0,2) | \(61/252\) | \(445/504\) |
| (1,1) | (1,1) | \(37/168\) | \(445/504\) |
| (1,1) | (2,0) | \(25/63\) | \(445/252\) |

For G6, the independent LR/hook calculation gives
\[
 c_{(2,1),(2,1)}^{(3,2,1)}=2,\quad {\cal T}=990080,\quad
 d=1485120,\quad {\cal T}/d=2/3,
\]
\[
 \omega=6173/29667,\quad \delta_{\min}=28,\quad
 r_{\rm top}=39366/20825.
\]
The internal envelope is
\[
 \frac{136910540}{549403173},
\]
and the canonical envelope is exactly
\[
 \boxed{\frac{119769340392}{254251579505}}.
\]
**Agreement is exact; there is no discrepancy.** Raw output is in [reviewer1_crosscheck.log](logs_se_gramdirectrev2_20260719/reviewer1_crosscheck.log).

## D. Verdicts and promotion recommendation

| Task | Verdict |
|---|---|
| A: counterexample hunt | **CONFIRMED** for every mandatory sector; optional full j=4 infeasible, two exact endpoints pass |
| B: from-scratch Section 5 proof | **CONFIRMED** |
| C: reviewer #1 cross-check | **EXACT AGREEMENT** |
| T4 assembly | **CONFIRMED** |
| Overall rule 6 | **CONFIRMED** |

**PROMOTION RECOMMENDATION: PROVED** for both the tame-node claim and the T4 assembly, not merely CERTIFIED*. The reason is analytic rather than numerical: the BR coset operator supplies a coherent unitary tableau/LR transport; the strict input and weighted output frames contribute exactly two \(B_\theta(q)\) factors; completion commutes with the central query-branch projectors; and the positive multiplicity trace includes all LR copies without a dimension penalty. The hook and endpoint estimates then give the strict uniform constants, while T4 is a direct substitution into already reviewed denominator arithmetic. The finite sweep is corroboration and counterexample pressure, not a premise of the proof.

No DAG, node, or index file was edited.
