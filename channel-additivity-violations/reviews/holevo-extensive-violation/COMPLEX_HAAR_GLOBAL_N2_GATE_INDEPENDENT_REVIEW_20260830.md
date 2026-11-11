# Independent adversarial review of the complex-Haar global n=2 gate

**Date:** 2026-08-30
**Reviewer:** OpenAI Codex review agent
**Reviewed nodes:** HEXT.complex-haar-global-n2-output-dual-gate and
HEXT.same-tuple-two-leg-scalar-strong-norm
**Primary artifact:** COMPLEX_HAAR_GLOBAL_N2_CONCENTRATION_GATE_20260830.md
**Review status:** completed and immutable; later corrections should be new review objects

## Independence and repository discipline

I performed this audit in a separately commissioned review context and did not participate in the
proposer derivation. I did not receive private proposer reasoning, did not contact the proposer,
and used no subagent. I reconstructed the output duality, metric-entropy comparison, replica
identities, partial-transpose direction, and hierarchy dimension costs independently.

The canonical YAML nodes, proposer artifacts, primary-source PDF, and generated views were
read-only. This report is the only durable repository file created for this review. I did not
stage, commit, push, regenerate a view, or change either canonical assessment.

## Executive verdict

**CHG2-IR-VERDICT-REDUCTION: PASS / PROVED as an exact conditional reduction.**

For $N=C\otimes C$, the equality

\[
 \sup_{\rho\in\mathcal D}\|N(\rho)\|_2
 =
 \sup_{\substack{Y=Y^*\\\|Y\|_2=1}}\|N^*(Y)\|_\infty
\]

is exact. The Hermitian coefficient space has real dimension $m^4$, independent of $d$, and the
adjoint map is one-Lipschitz from Hilbert--Schmidt coefficient norm to operator norm. Therefore a
fixed finite coefficient net does upgrade fixed-$Y$ convergence in probability whenever the
limiting free bound has uniform positive slack.

This is a reduction, not a proof of global $n=2$. The required same-tuple repeated-representation
strong-norm convergence is not supplied by Bordenave--Collins, whose tensor-leg variables are
independently sampled. The node HEXT.same-tuple-two-leg-scalar-strong-norm is correctly **OPEN**.
Proving it would settle only the stated one-layer global $n=2$ gate; it would not imply $n\ge3$ or
all-copy regularization.

**CHG2-IR-VERDICT-OBSTRUCTIONS: PASS, with one quantitative repair required.**

The pure-input net/Lipschitz comparison, deterministic replica lower bound, partial-transpose Bell
direction, and their proof-method-only scopes are correct. The standard input-net route compares

\[
 \exp\{\Theta(d^2\log m)-\Theta(d/m^5)\},
\]

the unrestricted replica relaxation is deterministically at least
$(2-1/m)/m^2$, and the partial transpose has an exact unit eigenvector.

Section 8 requires a quantitative hierarchy-cost repair. Substituting $h=d^2$ into the particular
ordinary 2007 permutation-invariant de Finetti estimate $O(h^2/k)$ does produce $O(d^4/k)$.
However, the exact target cone is the Hartree/symmetric separable cone, so a bosonic or full
exchangeable extension is a valid outer hierarchy. The Bose theorem in the same 2007 source
already gives $O(h/k)$, and the current optimal exchangeable trace-norm theorem gives the same
order. Thus a generic sufficient level is of order $m^3d^2$, not necessarily $m^3d^4$. The
qualitative conclusion survives: no fixed hierarchy level is dimension-uniform. This defect does
not affect either reviewed node claim.

Two additional presentation issues are nonfatal: the coefficient unit sphere has intrinsic
dimension $m^4-1$ rather than $m^4$ (the ambient Hermitian space and covering-number exponent are
$m^4$), and artifact equations (2) and (3) omit two TeX backslashes.

## 1. Immutable input and statement binding

| object | SHA-256 |
|---|---|
| DAG_PROTOCOL.md | d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095 |
| FILE_PROTOCOL.md | d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595 |
| proof-dag/nodes/HEXT.complex-haar-global-n2-output-dual-gate.yaml | 73435d95f2649070c7271fb18f7a7375d0de356b23a364afb2355f37485d07a0 |
| proof-dag/nodes/HEXT.same-tuple-two-leg-scalar-strong-norm.yaml | 2a40cfc3f7e7bfbf1cabf2bf5daf80482547a2aec8e95feaf5267ea443fbbcd9 |
| artifacts/COMPLEX_HAAR_GLOBAL_N2_CONCENTRATION_GATE_20260830.md | 1b21f7b405ae6afcfee885509c1dc7ea93ae0d3b45ab876b8098bb1508e23abf |
| artifacts/primary-sources/bordenave-collins-2304.05714.pdf | 59e14a3334b24f5683d8a0a8919d6cf266cb587f9dbae8d78e8213ca3fe2d8ac |

The repository-normalized exact claim hashes are:

| node | exact claim hash |
|---|---|
| HEXT.complex-haar-global-n2-output-dual-gate | sha256:26a33faa53c08abc12649e02115ca598d9898c12a97c2490a751a4b7bbc4d274 |
| HEXT.same-tuple-two-leg-scalar-strong-norm | sha256:f782bd3d6ea6f158cba4d91f13389f53df317690647918098d3da8a69e374647 |

The hashes use the repository rule
$\operatorname{sha256}(\operatorname{statement.strip}())$ after CRLF normalization. This review
becomes stale if either claim or any hash-bound primary disk input changes.

The external theorem interfaces were checked against:

1. [Bordenave--Collins, arXiv:2304.05714v2, Theorem 9.2](https://arxiv.org/html/2304.05714v2),
   especially the independent family $U_{i,j}$ in equations (69)--(70).
2. [Christandl--König--Mitchison--Renner, arXiv:quant-ph/0602130v4](https://arxiv.org/html/quant-ph/0602130v4),
   Theorems II.7 and II.8.
3. [Jeronimo--Wu--Xu, arXiv:2608.02590v1](https://arxiv.org/abs/2608.02590),
   especially Corollary 3.7.

## 2. Independent check ledger

The universal findings below are algebraic. As a separate smoke test, I generated independent
Haar matrices with standard-library complex Gaussian Gram--Schmidt for
$(d,m)=(2,2),(2,3),(3,2),(3,3)$ and independently constructed $R_U$. In all four cases:

1. the Hermiticity defect of $R_U$ was below $3.2\times10^{-17}$;
2. the two forms of $d^{-2}\operatorname{Tr}(R_U^2)$ agreed within
   $2.8\times10^{-16}$;
3. the collision lower bound $(2-1/m)/m^2$ held; and
4. the error in $R_U^\Gamma\Omega_d=\Omega_d$ was below $7.8\times10^{-16}$.

The smoke test is not used as proof.

## 3. Findings

### Finding CHG2-IR-01 — PASS: exact output duality

**Stable source locators:** artifact equations (33)--(35), lines 415--447; output-dual node claim
lines 5--10.

For every density operator $\rho$, $N(\rho)$ is positive and Hermitian, so Hilbert--Schmidt
duality may be restricted to Hermitian coefficients:

\[
 \|N(\rho)\|_2
 =\sup_{\substack{Y=Y^*\\\|Y\|_2=1}}
   \operatorname{Tr}[Y N(\rho)].
\]

Taking both suprema and using the adjoint gives

\[
\begin{aligned}
 \sup_{\rho\in\mathcal D}\|N(\rho)\|_2
 &=\sup_{\substack{Y=Y^*\\\|Y\|_2=1}}
   \sup_{\rho\in\mathcal D}\operatorname{Tr}[\rho N^*(Y)]\\
 &=\sup_{\substack{Y=Y^*\\\|Y\|_2=1}}
   \lambda_{\max}(N^*(Y)).
\end{aligned}
\]

The coefficient sphere is invariant under $Y\mapsto-Y$. Hence the outer supremum also captures
$-\lambda_{\min}(N^*(Y))$, and

\[
 \sup_Y\lambda_{\max}(N^*(Y))
 =\sup_Y\|N^*(Y)\|_\infty.
\]

The maximum over density operators can equivalently be restricted to pure inputs, either by the
last eigenvalue formula or by convexity. Squaring the norm target $A/m$ recovers the purity target
$A^2/m^2$.

**Verdict:** every equality is exact; no minimax interchange or positivity relaxation is hidden.

### Finding CHG2-IR-02 — PASS: adjoint polynomial, coefficient dimension, and finite net

**Stable source locators:** artifact equations (34)--(37), lines 431--468; output-dual node claim
lines 6--10.

The channel formula gives, up to transposing the coefficient convention,

\[
 N^*(Y)=\frac1{m^2}\sum_{v,a,w,b}
 Y_{(v,a),(w,b)}
 (U_v^*U_w)\otimes(U_a^*U_b).
\]

Since $N$ is trace preserving, $N^*$ is unital completely positive. For Hermitian $H$,

\[
 \|N^*(H)\|_\infty\le\|H\|_\infty\le\|H\|_2.
\]

Thus $Y\mapsto\|N^*(Y)\|_\infty$ is one-Lipschitz in Hilbert--Schmidt norm.

The real vector space of Hermitian matrices in $M_{m^2}$ has dimension
$(m^2)^2=m^4$. Its unit sphere has intrinsic dimension $m^4-1$, but it admits the standard
covering bound

\[
 N(\varepsilon)\le(1+2/\varepsilon)^{m^4}.
\]

Consequently the node's $m^4$ net exponent and independence from $d$ are correct. Calling the
sphere itself $m^4$-dimensional is only an off-by-one wording issue.

More explicitly, suppose for every fixed $Y$ the random norm $g_d(Y)$ converges in probability to
$g_\infty(Y)$, and

\[
 \sup_{\|Y\|_2=1}g_\infty(Y)\le A/m-\gamma
\]

for fixed $\gamma>0$. Choose a finite $\varepsilon$-net with $\varepsilon<\gamma/3$. Pointwise
convergence at its finitely many points, a union bound, and the one-Lipschitz estimate imply the
uniform target with probability tending to one. For the stated free and finite constants,

\[
 \gamma=\frac{9(c-1)}{m^2}
\]

before reserving interpolation error, so this step requires the inherited $\eta>0$ and $c>1$
slack.

**Verdict:** the finite-net implication is rigorous and conditional on the missing convergence
premise.

### Finding CHG2-IR-03 — PASS: the same-tuple strong-norm lemma remains OPEN

**Stable source locators:** artifact lines 470--480; same-tuple node claim lines 5--10 and caveats
lines 13--20; Bordenave--Collins Theorem 9.2, equations (69)--(70).

The repeated finite representation in the open node uses

\[
 (U_i\otimes I,\ I\otimes U_i)
\]

with the same sampled tuple on both tensor legs. In contrast, Bordenave--Collins define

\[
 V_{i,j}=I^{\otimes(j-1)}\otimes U_{i,j}\otimes
 I^{\otimes(k-j)}
\]

with the entire family $U_{i,j}$ independent over both $i$ and $j$. Their Theorem 9.2 proves
strong convergence for that independent-leg representation of
$F_m^k$. It does not identify the norm limit of the same-tuple tensor square.

Ordinary one-leg strong convergence also does not automatically pass to the tensor square of the
same finite representation. The desired fixed-$Y$ statement is substantially narrower than
growing completely bounded convergence, but it remains an additional theorem.

**Status verdict:** HEXT.same-tuple-two-leg-scalar-strong-norm is correctly OPEN. No proof or
counterexample was found in the audited interfaces. The output-dual node must not be read as
asserting this premise.

### Finding CHG2-IR-04 — PASS: target margin and input-state Lipschitz constant

**Stable source locators:** artifact equations (6)--(7), lines 74--108.

For an output state on dimension $m^2$, purity is at least $1/m^2$. With
$A=1+9c/m$,

\[
 s=\frac{A^2-1}{m^2}
 =\frac{18c}{m^3}+\frac{81c^2}{m^4}
 =\Theta(m^{-3}).
\]

For states $\sigma,\tau$,

\[
 |\operatorname{Tr}\sigma^2-\operatorname{Tr}\tau^2|
 \le2\|\sigma-\tau\|_1.
\]

Trace-norm contractivity of $C^{\otimes2}$ on Hermitian differences and
$\||\psi\rangle\langle\psi|-|\phi\rangle\langle\phi|\|_1
\le2\|\psi-\phi\|_2$ yield

\[
 |f_U(\psi)-f_U(\phi)|\le4\|\psi-\phi\|_2.
\]

An input-net radius $t/8$ therefore costs at most $t/2$, as stated.

**Verdict:** the available margin and input Lipschitz constants have the correct powers of $m$.

### Finding CHG2-IR-05 — PASS: Haar-tuple Lipschitz exponent and pure-state net obstruction

**Stable source locators:** artifact equations (8)--(16), lines 110--207.

For the Stinespring isometries,

\[
 \|V_U-V_V\|_\infty\le m^{-1/2}d_{\rm HS}(U,V)
\]

and the tensor-square telescoping identity gives the factor two in equation (10). Passing from
pure Stinespring outputs to reduced states costs another factor two in trace norm, and purity costs
two again. Hence

\[
 |f_U(\psi)-f_V(\psi)|
 \le8m^{-1/2}d_{\rm HS}(U,V).
\]

The function is invariant under the independent central phases. Standard concentration on the
product of projective/special unitary factors has exponent of order $d t^2/L^2$, where
$L=8/\sqrt m$, giving $\Theta(md t^2)$.

The unit sphere in $\mathbb C^{d^2}$ has real dimension $2d^2-1$. Quotienting the irrelevant
global input phase would reduce this by only one and does not change the scale. At
$t=\Theta(m^{-3})$,

\[
 \log N(t/8)=\Theta(d^2\log m),\qquad
 md t^2=\Theta(d/m^5).
\]

Thus the standard pointwise Lipschitz tail plus a direct full pure-state union bound becomes more
vacuous as $d$ grows, even with $m$ fixed first.

**Scope verdict:** this is a proved obstruction to that specific proof interface. It is not a
counterexample to the global purity target and does not rule out stronger polynomial-specific
tails.

### Finding CHG2-IR-06 — PASS: low-Schmidt-rank entropy comparison

**Stable source locators:** artifact equations (17)--(21), lines 209--258.

The rank-at-most-$r$ complex $d\times d$ matrices admit a net with exponent at most $4dr$.
The exact projective rank-$r$ stratum has real dimension $4dr-2r^2-2$; the coarser exponent is a
valid upper bound including lower-rank strata.

Combining it with the same Haar tail gives

\[
 4dr\log(C_0/t)-c_0mdt^2/64.
\]

At $t=\Theta(m^{-3})$, the positive coefficient of $d$ is
$\Theta(r\log m)$ and the negative coefficient is $\Theta(m^{-5})$. It is therefore positive for
the intended enormous $m$, even at $r=1$. If a new tail with exponent
$d^2t^2/m^\alpha$ were proved, the displayed closure range

\[
 r\ll\frac{d}{m^{\alpha+6}\log m}
\]

would follow.

**Scope verdict:** equations (19)--(21) are a proposed OPEN tail lemma and its conditional
consequence, not an established concentration theorem.

### Finding CHG2-IR-07 — PASS: replica factorization and deterministic lower bound

**Stable source locators:** artifact equations (22)--(27), lines 260--330.

Set $B_{v,w}=U_w^*U_v$. Then

\[
 R_U=\frac1{m^2}\sum_{v,w}B_{v,w}\otimes B_{v,w}^*
\]

is Hermitian. Regrouping the two physical legs across the two replicas gives
$Q_U\simeq R_U\otimes R_U$, while the physical objective uses only vectors
$\psi\otimes\psi$.

Cyclicity of trace gives

\[
 \frac1{d^2}\operatorname{Tr}(R_U^2)
 =\frac1{m^4d^2}\sum_{v,w,x,y}
 |\operatorname{Tr}(B_{v,w}B_{x,y})|^2.
\]

There are two identity-product families: $v=w,x=y$ and $x=w,y=v$. Each contains $m^2$ ordered
quadruples and their intersection contains exactly $m$. Every retained summand equals $d^2$.
Therefore

\[
 \frac1{d^2}\operatorname{Tr}(R_U^2)
 \ge\frac{2m^2-m}{m^4}
 =\frac{2-1/m}{m^2}.
\]

If $\lambda_i$ are the real eigenvalues of $R_U$, the largest eigenvalue of
$R_U\otimes R_U$ is $\max_i\lambda_i^2=\|R_U\|_\infty^2$. Since $R_U$ acts on dimension $d^2$,

\[
 \lambda_{\max}(Q_U)=\|R_U\|_\infty^2
 \ge d^{-2}\operatorname{Tr}(R_U^2).
\]

**Scope verdict:** this is a deterministic obstruction to the unrestricted operator-norm
relaxation for every complex tuple. It is not a physical-state violation because its maximizing
replica vector need not be $\psi\otimes\psi$.

### Finding CHG2-IR-08 — PASS: partial-transpose unit direction

**Stable source locators:** artifact equation (28), lines 332--345.

Partial transpose on the second factor gives

\[
 R_U^\Gamma=\frac1{m^2}\sum_{v,w}B_{v,w}\otimes\overline{B_{v,w}}.
\]

For every unitary $B$,

\[
 (B\otimes\overline B)|\Omega_d\rangle
 =d^{-1/2}\operatorname{vec}(BB^*)=|\Omega_d\rangle.
\]

Every summand fixes the same normalized vector, hence
$R_U^\Gamma|\Omega_d\rangle=|\Omega_d\rangle$ exactly and
$\|R_U^\Gamma\|_\infty\ge1$. This is incompatible with a desired one-factor scale $A/m$ for the
intended large $m$.

**Scope verdict:** this rules out discarding the physical cone through that partial-transpose/cb
norm. It does not create a physical output state of purity one.

### Finding CHG2-IR-09 — PASS: matrix-mean warning and deterministic deviation floor

**Stable source locators:** artifact equations (29)--(29a), lines 347--375.

The $m^2$ replica terms depend on only $m$ Haar matrices, so treating them as independent
summands is invalid. Direct Haar integration gives

\[
 \mathbb ER_U=\frac1mI+\frac{m-1}{md}F,
\]

where $F$ is swap. Combining
$\|R_U\|_\infty\ge\sqrt{2-1/m}/m$ with the exact norm of the mean gives

\[
 \|R_U-\mathbb ER_U\|_\infty
 \ge\frac{\sqrt{2-1/m}}m
 -\left(\frac1m+\frac{m-1}{md}\right).
\]

The limiting floor is $(\sqrt2-1)/m$, much larger than the finite-model
$\Theta(m^{-2})$ slack. No operator-norm concentration around the matrix mean at the target scale
can hold.

**Verdict:** the matrix-Bernstein warning and quantitative floor are correct.

### Finding CHG2-IR-10 — REPAIR REQUIRED: de Finetti rate, but not the fixed-level obstruction

**Stable source locators:** artifact equations (30)--(32), lines 377--413; CKMR Theorems II.7 and
II.8; Jeronimo--Wu--Xu Corollary 3.7.

The exact convex lift is correct. A positive separable state supported on the symmetric subspace
decomposes into vectors $a\otimes b$ lying in that subspace; each such vector has $a$ proportional
to $b$. Hence the feasible cone is precisely the convex hull of Hartree projectors
$|\psi\rangle\langle\psi|^{\otimes2}$.

For the particular ordinary permutation-invariant theorem quoted in the artifact, the local
dimension is

\[
 h=d^2,
\]

and its trace-norm error $O(h^2/k)$ becomes $O(d^4/k)$. With
$\|Q_U\|_\infty\le1$ and margin $s=\Theta(m^{-3})$, that theorem indeed gives the sufficient
condition $k\gg m^3d^4$. The substitution itself is not an algebra error.

It is not, however, the best available generic hierarchy interface for this target cone. Every
Hartree mixture has an extension supported on the fully symmetric subspace of
$(\mathbb C^h)^{\otimes k}$. Imposing such a bosonic extension is still a valid outer SDP
relaxation. CKMR Theorem II.8 gives trace error $O(h/k)$ for this hierarchy. Independently, the
current optimal exchangeable theorem gives

\[
 O(h/k)=O(d^2/k)
\]

for two-site exchangeable marginals. Thus a current generic sufficient scaling is

\[
 k\gg m^3d^2,
\]

up to universal constants, rather than $m^3d^4$. This is still not a lower bound on the level
needed for the special random objective, and an instance-specific certificate could do better.

**Severity:** repair-required quantitative overstatement in the artifact. The qualitative
method boundary remains valid because every cited generic trace-norm level still grows with $d$;
no fixed PPT/DPS/exchangeable level is dimension-uniformly certified.

### Finding CHG2-IR-11 — PASS WITH PRESENTATION PATCHES: exact status boundary

**Stable source locators:** artifact status lines 5--6, conclusions lines 39--72, boundary lines
482--492; both node assessment blocks.

The following items are proved in the artifact:

| item | audited status |
|---|---|
| Output Hilbert--Schmidt duality and coefficient-net reduction | PROVED |
| Failure of the standard full pure-state net plus generic Lipschitz tail | PROVED method obstruction |
| Failure of the same standard tail on fixed low Schmidt rank in the intended large-$m$ regime | PROVED method obstruction |
| Replica collision lower bound and unrestricted norm relaxation gap | PROVED deterministic obstruction |
| Partial-transpose unit direction | PROVED deterministic obstruction |
| No dimension-uniform guarantee from a fixed generic extension level | PROVED method obstruction, with Finding CHG2-IR-10 rate repair |

The following items remain open:

| item | audited status |
|---|---|
| Entry-sensitive $d^2$-exponent fixed-state tail | OPEN proposed lemma |
| Fixed-$Y$ same-tuple two-leg scalar strong-norm convergence | OPEN node |
| Global complex-Haar one-layer $n=2$ purity target | OPEN |
| Any $n\ge3$ or all-copy physical purity statement | OPEN |
| A special low-level PPT/DPS dual certificate for these random instances | OPEN |

The canonical assessment boundaries express this distinction correctly. The output-dual claim is
a proved conditional reduction; retaining a conservative CONJECTURED assessment does not license
promotion of the OPEN premise. The same-tuple node's OPEN level is necessary.

Artifact line 23 prints a literal comma followed by qquad rather than the TeX command
$\backslash\mathrm{qquad}$, and line 32 prints le rather than $\backslash\mathrm{le}$. These are
presentation defects only; the prose and all downstream formulas use the intended inequalities.

## 4. Limitations

1. I verified the stated standard Haar concentration scaling but did not re-prove the underlying
   log-Sobolev theorem on projective unitary groups.
2. I audited the external theorem scopes from the cited primary sources. I did not prove the
   Bordenave--Collins or quantum de Finetti theorems from first principles.
3. The hierarchy-rate correction is a generic sufficient guarantee, not a claim that level
   $\Theta(m^3d^2)$ is necessary or computationally practical.
4. Nothing in this review establishes the OPEN same-tuple norm limit, the global $n=2$ channel
   inequality, or any higher-copy statement.

## 5. Final disposition

The exact output-dual claim
sha256:26a33faa53c08abc12649e02115ca598d9898c12a97c2490a751a4b7bbc4d274
passes as a proved conditional reduction, subject only to the $m^4$ versus $m^4-1$ sphere wording
precision. The exact same-tuple claim
sha256:f782bd3d6ea6f158cba4d91f13389f53df317690647918098d3da8a69e374647
remains OPEN and is not implied by the independent-leg theorem.

The artifact's exact duality and deterministic/method obstructions pass. Section 8 should be
repaired so that $m^3d^4$ is not presented as the available generic hierarchy scale; a
bosonic/full-exchangeable interface gives $m^3d^2$ while preserving the conclusion that fixed
levels do not certify the $d\to\infty$ target. No canonical YAML or proposer artifact was modified.
