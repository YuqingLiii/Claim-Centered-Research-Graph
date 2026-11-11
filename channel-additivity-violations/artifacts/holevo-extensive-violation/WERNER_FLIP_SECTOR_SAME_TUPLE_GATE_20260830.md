# Same-tuple Werner/flip sector: exact spectral gate and failed concentration interfaces

Date: 2026-08-30

Status: proposer-side analysis for the one-layer coefficient problem.  No canonical YAML is
changed.  No claim in this note should be promoted beyond `CONJECTURED` without independent
review.  The generic complex-Haar high-probability bound remains **OPEN**.

All logarithms are base two unless `ln` is written explicitly.

## 1. Setup and outcome

For one fixed tuple `U_1,...,U_m in U(d)`, define

\[
 R_U=\frac1{m^2}\sum_{v,a=1}^m
 U_v^*U_a\otimes U_a^*U_v.
\tag{1}
\]

Let `F_m` be the flip on `C^m tensor C^m`, and let

\[
 P_\pm=(I\pm F_m)/2,qquad
 r_\pm=\operatorname{rank}P_\pm=\frac{m(m\pm1)}2.
\tag{2}
\]

For the two-leg scalar coefficient map `M_U=C^* tensor C^*`,

\[
 \mathcal M_U(I)=I,qquad \mathcal M_U(F_m)=R_U,
\tag{3}
\]

and therefore

\[
 \mathcal M_U(P_\pm/\sqrt{r_\pm})
 =\frac{I\pm R_U}{2\sqrt{r_\pm}}.
\tag{4}
\]

Write

\[
 A=1+\frac{9(1+\eta)^2}{m}.
\tag{5}
\]

The precise outcome is:

1. The normalized `P_+` target is equivalent to one upper-edge inequality for `R_U`; the
   normalized `P_-` target is equivalent to one lower-edge inequality.  For large `m`, both only
   require `spec(R_U)` to lie inside approximately `[-0.414,0.414]`.
2. The **entire real Werner sector** `span{I,F_m}` satisfies the target iff

   \[
    \boxed{\ \|R_U-I/m\|_\infty
    \le\sqrt{(A^2-1)(1-m^{-2})}.\ }
   \tag{6}
   \]

   The right side is asymptotic to `sqrt(18)(1+eta)/sqrt(m)`.  Thus an
   `O(m^-1/2)` same-tuple bound with an explicit constant below `sqrt(18)` would close this whole
   sector.
3. The matrix expectation is safely inside both gates, and normalized trace moments show a bulk
   scale `Theta(1/m)`.  Neither statement controls an adaptive extreme eigenvector.
4. The standard random-quantum-expander theorem controls a positive matrix whose partial
   transpose is `R_U`.  Partial transpose can amplify operator norm by a factor `d`; the expander
   gap therefore does not imply (6).
5. Haar Lipschitz concentration gives sharp concentration of the extreme eigenvalues around their
   unknown medians, but supplies no target-scale upper bound on those medians.
6. No generic complex-Haar counterexample was found.  The tuple with all `U_v` identical is an
   exact deterministic `P_+` counterexample in the relevant constant regime, proving that no
   deterministic all-tuple statement is possible; it is not a generic-Haar obstruction.

The smallest missing lemma is the centered bound (6), or the much weaker pair of edge bounds in
Section 2 if only `P_+` and `P_-` are needed.

## 2. Exact `P_+` and `P_-` spectral thresholds

The operator `R_U` is Hermitian and `||R_U||_infty<=1`, since (1) is an average of unitaries closed
under adjoint.  Hence `I plus/minus R_U` is positive.  Equation (4) gives

\[
 \left\|\mathcal M_U(P_+/\sqrt{r_+})\right\|_\infty
 =\frac{1+\lambda_{\max}(R_U)}{2\sqrt{r_+}},
\tag{7}
\]

and

\[
 \left\|\mathcal M_U(P_-/\sqrt{r_-})\right\|_\infty
 =\frac{1-\lambda_{\min}(R_U)}{2\sqrt{r_-}}.
\tag{8}
\]

Therefore the desired bound `<=A/m` is exactly

\[
 \boxed{
 \lambda_{\max}(R_U)
 \le g_+(m,A):=A\sqrt{2(1+1/m)}-1}
\tag{9}
\]

for `P_+`, and

\[
 \boxed{
 \lambda_{\min}(R_U)
 \ge-g_-(m,A),\qquad
 g_-(m,A):=A\sqrt{2(1-1/m)}-1}
\tag{10}
\]

for `P_-`.  At fixed small `eta` and large `m`,

\[
 g_\pm(m,A)=\sqrt2-1+O((1+\eta)^2/m).
\tag{11}
\]

Thus a high-probability estimate `||R_U||_infty<0.4` would be nearly sufficient but not quite;
any fixed bound strictly below `sqrt(2)-1` is sufficient for all large enough `m`.  No
`Theta(1/m)` estimate is required just for the two projectors.

## 3. Exact reduction of the whole Werner sector

Let

\[
 Y_{\alpha,\beta}=\alpha I+\beta F_m,
 \qquad \alpha,\beta\in\mathbb R.
\tag{12}
\]

Its Hilbert--Schmidt norm is

\[
 \|Y_{\alpha,\beta}\|_2^2
 =m^2(\alpha^2+\beta^2)+2m\alpha\beta,
\tag{13}
\]

while

\[
 \mathcal M_U(Y_{\alpha,\beta})=\alpha I+\beta R_U.
\tag{14}
\]

For a fixed eigenvalue `lambda` of `R_U`, optimize
`|alpha+beta lambda|` subject to (13).  The inverse of the coefficient Gram matrix is

\[
 \begin{pmatrix}m^2&m\\m&m^2\end{pmatrix}^{-1}
 =\frac1{m^4-m^2}
 \begin{pmatrix}m^2&-m\\-m&m^2\end{pmatrix}.
\tag{15}
\]

Consequently

\[
 \sup_{(\alpha,\beta)\ne0}
 \frac{|\alpha+\beta\lambda|^2}
 {\|Y_{\alpha,\beta}\|_2^2}
 =\frac{1+\lambda^2-2\lambda/m}{m^2-1}.
\tag{16}
\]

The desired estimate

\[
 \|\mathcal M_U(Y_{\alpha,\beta})\|_\infty
 \le\frac A m\|Y_{\alpha,\beta}\|_2
 \quad\text{for all real }\alpha,\beta
\tag{17}
\]

is therefore equivalent to

\[
 1+\lambda^2-2\lambda/m
 \le A^2(1-m^{-2})
 \quad\text{for every }\lambda\in\operatorname{spec}R_U.
\tag{18}
\]

Completing the square gives exactly (6):

\[
 (\lambda-1/m)^2
 \le(A^2-1)(1-m^{-2}).
\tag{19}
\]

Since

\[
 A^2-1
 =\frac{18(1+\eta)^2}{m}
 +\frac{81(1+\eta)^4}{m^2},
\tag{20}
\]

the allowed centered radius is

\[
 h_W(m,\eta)
 :=\sqrt{(A^2-1)(1-m^{-2})}
 =\frac{\sqrt{18}(1+\eta)}{\sqrt m}
  (1+O((1+\eta)^2/m)).
\tag{21}
\]

This exact two-dimensional optimization is stronger and cleaner than separately applying the
triangle inequality to `I` and `F_m`.

## 4. Expectation is safe but is not a norm bound

For `v!=a`, the product `U_v^*U_a` is Haar.  The first unitary moment gives

\[
 \mathbb E[(U_v^*U_a)\otimes(U_a^*U_v)]=F_d/d,
\tag{22}
\]

where `F_d` is the flip on `C^d tensor C^d`.  Including the `v=a` terms,

\[
 \boxed{
 \mathbb ER_U=\frac1mI+\frac{m-1}{md}F_d.}
\tag{23}
\]

In particular,

\[
 \|\mathbb ER_U-I/m\|_\infty=\frac{m-1}{md}=O(1/d),
\tag{24}
\]

far below the allowed Werner radius `h_W=Theta(m^-1/2)` for fixed `m` and large `d`.

The mean **output operators** for `P_+` and `P_-` are also safely below the target:

\[
 \left\|\mathbb E\mathcal M_U(P_+/\sqrt{r_+})\right\|_\infty
 =\frac{1+1/m+(m-1)/(md)}{2\sqrt{r_+}},
\tag{25}
\]

\[
 \left\|\mathbb E\mathcal M_U(P_-/\sqrt{r_-})\right\|_\infty
 =\frac{1-1/m+(m-1)/(md)}{2\sqrt{r_-}}.
\tag{26}
\]

Both are asymptotic to `1/(sqrt(2)m)`, leaving a constant margin below `A/m`.

However,

\[
 \|\mathbb ER_U\|_\infty
 \le\mathbb E\|R_U\|_\infty,
\tag{27}
\]

not the reverse.  Equations (23)--(26) do not control a tuple-dependent extremal eigenvector.

## 5. Bulk moments are safe but do not exclude outliers

Put

\[
 S_U=R_U-I/m
 =\frac1{m^2}\sum_{v\ne a}
 U_v^*U_a\otimes U_a^*U_v.
\tag{28}
\]

Ordinary asymptotic freeness gives the fixed-moment limit

\[
 \lim_{d\to\infty}
 \mathbb E\frac1{d^2}\operatorname{Tr}(S_U^2)
 =\frac{m(m-1)}{m^4}
 =\frac{m-1}{m^3}.
\tag{29}
\]

Indeed, in the free-group word

\[
 u_v^*u_a u_x^*u_y,
\tag{30}
\]

with `v!=a` and `x!=y`, the normalized trace is nonzero only for the inverse pairing
`x=a,y=v`.  Thus the bulk root-mean-square eigenvalue is `Theta(1/m)`, much smaller than the
Werner allowance `Theta(1/sqrt(m))`.

Every fixed higher normalized moment can likewise be computed by Weingarten/free-word
contractions.  But a bounded number of `O(1)` outlier eigenvalues contributes only `O(d^-2)` to
each fixed normalized moment.  Excluding such outliers requires moment order growing at least like
`log d`, or a genuine strong-norm theorem.  Fixed-moment convergence is therefore not enough.

## 6. Haar concentration: the missing median problem

For two tuples `U=(U_i)` and `V=(V_i)`, direct telescoping in (1) gives

\[
 \|R_U-R_V\|_\infty
 \le\frac4{\sqrt m}
 \left(\sum_i\|U_i-V_i\|_2^2\right)^{1/2}.
\tag{31}
\]

Both extreme-eigenvalue functions are therefore `4/sqrt(m)`-Lipschitz.  Standard phase-invariant
Haar concentration yields, for a universal `c_0>0`,

\[
 \Pr\{|\lambda_{\max}(R_U)-\operatorname{med}\lambda_{\max}|>t\}
 \le2e^{-c_0mdt^2/16},
\tag{32}
\]

and the same bound for `lambda_min` and `||R_U-I/m||`.

At the constant `P_+/-` threshold, (32) has exponent `Theta(md)`.  At the Werner radius
`t=Theta(m^-1/2)`, it still has exponent `Theta(d)`.  Thus concentration would finish the proof
once one establishes a median bound with any fixed margin inside (9)--(10), or inside (6).

The expectation (23) and bulk moment (29) do not supply such a median bound.  Applying matrix
bounded differences directly also leaves the same issue: it controls fluctuation around an
unknown central value, not that central value itself.

## 7. Quantum-expander factorization and its exact interface failure

Define the random-unitary conjugation matrix

\[
 G_U=\frac1m\sum_{v=1}^m U_v\otimes\overline{U_v},
 \qquad \Pi=|\Omega_d\rangle\langle\Omega_d|.
\tag{33}
\]

Every summand fixes `Omega_d`, so `G_U Pi=Pi G_U=Pi`.  A direct multiplication gives

\[
 G_U^*G_U
 =\frac1{m^2}\sum_{v,a}
 (U_v^*U_a)\otimes\overline{(U_v^*U_a)}
 =R_U^\Gamma,
\tag{34}
\]

where `Gamma` is partial transpose on the second `d`-dimensional factor.

Random-quantum-expander results control a second singular value of this conjugation
representation in the matching variants.  For the interface test, grant the optimistic
target-scale estimate

\[
 \|(I-\Pi)G_U(I-\Pi)\|_\infty
 \lesssim\frac2{\sqrt m}
\tag{35}
\]

with high probability in the relevant fixed-`m`, `d->infinity` regime.  The precise universal
constant and Hermitianization convention are immaterial below: any `O(m^-1/2)` bound leads to the
same interface loss.  Under (35),

\[
 R_U^\Gamma=\Pi+H_U,qquad
 0\preceq H_U\preceq(4/m+o(1))(I-\Pi).
\tag{36}
\]

Partial transposition returns

\[
 R_U=F_d/d+H_U^\Gamma.
\tag{37}
\]

This does **not** yield (6).  The induced operator norm of partial transpose on
`M_d tensor M_d` can be as large as `d`; the elementary estimate from (36) is only

\[
 \|H_U^\Gamma\|_\infty
 \le d\|H_U\|_\infty
 \lesssim\frac{4d}{m},
\tag{38}
\]

which diverges with `d` at fixed `m`.  Positivity of `H_U` and orthogonality to `Pi` do not, by
themselves, give the required dimension-free partial-transpose norm.  For example,

\[
 H_0=P_{\rm sym}^{(d)}-\Pi
\tag{38a}
\]

is positive, obeys `0<=H_0<=I-Pi`, and has operator norm one, whereas

\[
 H_0^\Gamma=\frac{I+d\Pi}{2}-F_d/d
\tag{38b}
\]

has norm of order `d/2`.  An additional instance-specific delocalization theorem for the
eigenvectors/eigenprojections of the actual `H_U` is needed.

Thus the Hastings quantum-expander theorem is a useful structural input but not a complete
interface for the Werner coefficient problem.

## 8. A deterministic counterexample outside the generic-Haar claim

If all `U_v` are equal, then every summand in (1) is the identity and

\[
 R_U=I.
\tag{39}
\]

For `P_+`, equation (7) becomes

\[
 \left\|\mathcal M_U(P_+/\sqrt{r_+})\right\|_\infty
 =\frac1{\sqrt{r_+}}
 =\frac1m\sqrt{\frac{2m}{m+1}}.
\tag{40}
\]

This exceeds `A/m` whenever

\[
 A^2<\frac{2m}{m+1}.
\tag{41}
\]

For `eta=0` and all sufficiently large `m`, including the intended `ln m>18` scale, (41) holds.
Therefore no deterministic theorem valid for every unitary tuple can prove the `P_+` target.

The all-equal tuple has Haar probability zero and is maximally nongeneric.  Equation (40) is not a
counterexample to the generic complex-Haar high-probability claim.  It only shows exactly where
randomness must enter.  For this tuple `P_-` maps to zero, so it is not a `P_-` obstruction.

## 9. What would close the sector

### 9.1 Only the two projectors

It is enough to prove, with probability tending to one as `d->infinity` at fixed `m`,

\[
 \lambda_{\max}(R_U)\le g_+(m,A),
 \qquad
 \lambda_{\min}(R_U)\ge-g_-(m,A).
\tag{42}
\]

A coarse high-probability bound `||R_U||<=sqrt(2)-1-epsilon` for some fixed `epsilon>0` would imply
(42) for all sufficiently large `m` and small fixed `eta`.

### 9.2 The whole Werner sector

The exact minimal statement is

\[
 \boxed{
 \Pr\left\{
 \|R_U-I/m\|_\infty>h_W(m,\eta)
 \right\}\longrightarrow0.}
\tag{43}
\]

An asymptotically stronger but cleaner lemma would be

\[
 \limsup_{d\to\infty}\|R_U-I/m\|_\infty
 \le\frac{K}{\sqrt m}
 \quad\text{in probability, for some }K<\sqrt{18}(1+\eta).
\tag{44}
\]

Proving (44) requires one of:

1. a growing-order Weingarten trace method that controls all contractions uniformly up to
   `k=Theta(log d)` and keeps the constant below `sqrt(18)`;
2. an instance-specific theorem bounding `||H_U^Gamma||` in (37), beyond the ordinary expander
   spectral gap;
3. the same-tuple two-leg scalar strong-convergence lemma specialized to the single flip
   coefficient, with a quantitative free-limit norm.

No existing repository theorem currently supplies any of these three interfaces.

## 10. Proposed atomic DAG updates (not applied)

The following are proposed as atomic nodes or evidence links.  Per instruction, every proposed
status is at most `CONJECTURED`; no canonical YAML is edited.

1. `HEXT.same-tuple-two-leg-Werner-exact-spectral-reduction`
   - proposed status: `CONJECTURED` pending independent audit;
   - claim: equation (17) for all real Werner coefficients is equivalent to (6);
   - evidence: Sections 2--3 of this artifact.
2. `HEXT.same-tuple-two-leg-Ppm-edge-gate`
   - proposed status: `CONJECTURED`;
   - claim: normalized `P_+` and `P_-` reduce exactly to (9) and (10);
   - evidence: Section 2.
3. `HEXT.same-tuple-two-leg-Werner-centered-R-bound`
   - proposed status: `CONJECTURED`;
   - claim: the high-probability bound (43), or stronger (44), holds for independent complex Haar
     unitaries at fixed `m` as `d->infinity`;
   - dependency: a growing-moment, partial-transpose delocalization, or specialized same-tuple
     strong-norm theorem;
   - this is the unresolved analytic node.
4. `HEXT.quantum-expander-gap-does-not-control-Werner-partial-transpose`
   - proposed status: `CONJECTURED` pending audit;
   - claim: equations (34)--(38) identify the exact interface loss; the standard expander gap alone
     does not imply (43).
5. Add this artifact as evidence to
   `HEXT.same-tuple-two-leg-scalar-strong-norm`, without changing that node's current open status.

## 11. Boundary statement

- Expectation safety, typical bulk scale, and high-probability operator-norm safety are three
  distinct assertions.  Only the first two are established here.
- The deterministic all-equal counterexample rules out an all-tuple theorem but not the generic
  Haar claim.
- Even a proof of the whole Werner sector would cover only a two-dimensional coefficient space.
  It would not prove a general Hermitian `Y`, global all-coefficient `n=2`, or any `n>=3` claim.

## Primary sources and repository interfaces

1. M. B. Hastings, *Random Unitaries Give Quantum Expanders*, arXiv:0706.0556, expander estimate
   used only through the limited interface (35)--(38).
2. `SAME_TUPLE_TWO_LEG_SCALAR_BASE_CASES_20260830.md`, normalized flip and unresolved `P_+/-`
   base cases.
3. `COMPLEX_HAAR_GLOBAL_N2_CONCENTRATION_GATE_20260830.md`, replica and concentration gates.
4. `PRODUCT_HAAR_PHYSICAL_SELF_PURITY_N2_ANALYSIS_20260830.md`, boundary between scalar
   coefficients, replica relaxations, and physical inputs.
