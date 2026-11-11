# WHGAP P2 R2 independent review - signed-lift extension (2026-07-28)

Target node: `WHGAP.signed-lift-extension`  
Role: fresh independent reviewer  
Reviewed artifact: `artifacts/whgap_signed_lift_extension_20260728.md`

## PRE-ACTION REPORT

- Target status read from disk: `NUMERICAL - pending-review`.
- Independence: I did not author the reviewed work and was given no desired outcome.
- Highest potentially licensable tier: `PROVED` after a completed fresh rule-7 review. This
  commission forbids the reviewer from making any status write; only the decision layer may apply
  a licensing statement.
- Gate: independently derive and test the general-\(x\) construction before reading the
  proposer's scripts, tables, or JSON; then execute checklist 7a-7g and adjudicate claims 1-9.
- Deliverables: this immutable report; independent scripts and logs plus redirected proposer
  reproduction and hashes; a dated node review link; both validators green.
- Protocol conflict: the generic pre-task prompt names WindowsApps Python for validators, while
  the node-specific commission and user pin `C:<home>/cpython3119/python.exe` for every
  Python invocation and explain that WindowsApps is inaccessible. The pinned CPython 3.11.9 was
  used throughout.
- Graph: the target has no children. Its parent `WHGAP.goal` remains `OPEN` under the explicit
  disk adjudication that the registered children are contributory and mechanical OR-max does not
  apply. No status or graph-structure write is made here.

## Executive verdict

Claims 1-8 are **PASS**. Claim 9 is **PASS as the commissioned hypothesis audit**, not as a new
proof claim by the executor. The exact covariant-family feasibility theorem, the three exact
certificates, and the two twirling ingredients survive an independent construction using
different residual coordinates and different spin multiplicity bases.

This review does **not** license the full node statement \(Q(\Lambda_x)=P(\Lambda_x)=0\) on the
new interval by itself: the executor explicitly stopped before the generic-theorem application,
and the commission asks only for its hypothesis audit. A separate write-up must apply the cited
theorems with the support, complement, tensor-power, and capacity quantifiers listed below.

## 7c anchoring record and independent construction

Before opening any proposer artifact, script, artifact table, or JSON, I read only the frozen P2
commission and wrote:

- `review_independent_derivation.py`;
- `review_independent_twirling.py`;
- exact derivation, elimination, type/adjoint, regime, covariance, and certificate logs;
- `ANCHORING_BOUNDARY_SHA256.txt`, which freezes the pre-comparison hashes.

These are under
[`artifacts/logs_whgap_p2_review_20260728/`](logs_whgap_p2_review_20260728/).
The first proposer material was opened only after that manifest was written. Notational
coincidences \(a,k,p,q,c_1,c_2,c_3\) are forced by the frozen commission. My free coordinates
\((p,r)\), \(r=qk\), and my Cartesian \(\delta/\epsilon\) tensor bases were chosen independently;
they do not coincide with the proposer's \((s_1,s_2)\) coordinates or Casimir-kernel bases.

### Complement and adjoint

From the frozen Kraus operators, with the positive branch
\(k=\sqrt{x(1-x)/2}\), I obtain

\[
\Lambda_x^c(X)=
\begin{bmatrix}
(1-x)\operatorname{Tr}X&k\,a(X)^T\\
-k\,a(X)&\frac{x}{2}(\operatorname{Tr}X\,I-X^T)
\end{bmatrix}.
\]

For \(Z=\left[\begin{smallmatrix}\alpha&u^T\\v&D\end{smallmatrix}\right]\), define

\[
[w]_\times=\begin{bmatrix}0&w_2&-w_1\\-w_2&0&w_0\\w_1&-w_0&0\end{bmatrix}.
\]

Direct matrix-unit adjunction gives

\[
(\Lambda_x^c)^\dagger(Z)
=(1-x)\alpha I+k[u-v]_\times
+\frac{x}{2}(\operatorname{Tr}D\,I-D^T).
\]

The independent \(9\to16\) superoperator and its \(16\to9\) Hilbert-Schmidt transpose agree
entrywise. The Kraus and block constructions agree entrywise after imposing the positive-\(k\)
branch.

### Ansatz, intertwining, and residual family

For the five-real-parameter frozen ansatz, \(a(Y^\dagger)=-\overline{a(Y)}\) proves
\(J(Y^\dagger)=J(Y)^\dagger\). Equivariance follows from
\(a(OYO^T)=\det(O)Oa(Y)\) and \(V(O)=\operatorname{diag}(1,\det(O)O)\).

On the scalar, symmetric-traceless, and skew sectors I independently obtain

\[
\begin{aligned}
3(1-x)p+x(3c_1+c_2+c_3)&=1,\\
-\frac{x}{2}(c_2+c_3)&=1-\frac{3x}{2},\\
4kq+\frac{x}{2}(c_2-c_3)&=1-\frac{x}{2}.
\end{aligned}
\]

The coefficient matrix has the nonzero \(3\times3\) minor \(3x^3/2\), so its rank is exactly
three for every \(0<x<1\), including \(x=2/3\). The scalar/quint/vector decomposition has
dimensions \(1+5+3=9\), and a separate full \(9\times9\) matrix-unit residual is zero; hence
there are no unexamined equations within the ansatz.

With independent free variables \(p\) and \(r=qk\),

\[
q=\frac r k,\quad
c_1=\frac{(1-x)(1-p)}x,\quad
c_2=1-\frac{4r}{x},\quad
c_3=2-\frac2x+\frac{4r}{x}.
\]

The coordinate change to the proposer is

\[
s_1=c_1=\frac{(1-x)(1-p)}x,\qquad
s_2=c_2-c_3=\frac{2-x-8r}{x}.
\]

At \(x=1/2,p=1/3,r=1/6\), this gives the Zhu-Wang lift exactly.

### Independent defect, blocks, elimination, and region

I used
\(\operatorname{Choi}(\Phi)=\sum_{ab}|a\rangle\langle b|\otimes\Phi(E_{ab})\)
on \(A\otimes B\otimes B'\), ordered \((a,b,b')\). The independently assembled defect Choi is
real symmetric \(27\times27\), and all \(k\)-dependence reduces through \(k^2=x(1-x)/2\).
At the Zhu-Wang point it equals the frozen \((2/9)\sum_\mu G_\mu(\cdot)G_\mu^\dagger\) Choi
entrywise and has rank three.

My multiplicity slices use:

- spin 0: \(\epsilon_{abc}\);
- spin 1: \(\delta_{ab}v_c,\delta_{ac}v_b,\delta_{bc}v_a\);
- spin 2: two independent \(\epsilon\)-contractions with a traceless symmetric \(Q\);
- spin 3: the symmetric traceless \(xyz\) tensor.

Their multiplicity Gram matrices are

\[
G_0=G_3=[6],\quad
G_1=\begin{bmatrix}3&1&1\\1&3&1\\1&1&3\end{bmatrix},\quad
G_2=\begin{bmatrix}4&2\\2&4\end{bmatrix}.
\]

Thus the multiplicities are \(1,3,2,1\), and
\(1\cdot1+3\cdot3+2\cdot5+1\cdot7=27\).

In this unrelated basis, a spin-1 diagonal minor is

\[
-\frac{1-x}{x}(3p-1)^2,
\]

so PSD forces \(p=1/3\). The remaining spin-1 order-two minor becomes

\[
-\frac{100}{9}(3r+x-1)^2,
\]

so \(r=(1-x)/3\). This solution satisfies every other vanishing square and is unique for
\(0<x<1\). It translates to

\[
s_1=\frac{2(1-x)}{3x},\qquad s_2=\frac{5x-2}{3x}.
\]

At that point my congruence blocks are

\[
\begin{aligned}
H_0&=H_3=0,\\
H_1&=\frac{4(1-x)(3x-1)}x
\begin{bmatrix}1&2/3&0\\2/3&4/9&0\\0&0&0\end{bmatrix},\\
H_2&=\frac{4(1-x)(2x-1)}x
\begin{bmatrix}4&2\\2&1\end{bmatrix}.
\end{aligned}
\]

Both nonzero matrices are rank one. Since \(0<x<1\), full PSD is equivalent to
\(x\ge1/2\). Therefore the exact feasible region is \(1/2\le x<1\). At \(x=1/2\), only the
spin-1 contribution survives, giving full rank three. For \(1/2<x<1\), the full rank is
\(3+5=8\). As \(x\to1^-\), both blocks vanish and
\(\Lambda_x^c(I)=\operatorname{diag}(3(1-x),x,x,x)\) loses faithfulness at the excluded endpoint.

The proposer's bases give different congruence matrices but identical generalized spectra.
After comparison, the proposer's displayed spin-0 factor, all three spin-1 negative-square
minors, \(\det B_2\), \(B_3=0\), and its two rank-one reduced blocks all agree exactly.

## 7a type, dimension, basis, and Choi audit

All dimensions below are constant over \(0<x<1\); \(x\) changes coefficients, not spaces.

| Object/identity | Domain and codomain | Matrix size / check |
|---|---|---|
| \(\Lambda_x\) | \(L(\mathbb C^3)\to L(\mathbb C^3)\) | \(9\to9\); scalar/quint/vector dimensions \(1,5,3\) |
| \(\Lambda_x^c\) | \(L(\mathbb C^3)\to L(\mathbb C^4)\) | \(9\to16\); block formula is \(1+3\) by \(1+3\) |
| \((\Lambda_x^c)^\dagger\) | \(L(\mathbb C^4)\to L(\mathbb C^3)\) | \(16\to9\); every term in the displayed adjoint is \(3\times3\) |
| \(J_x\) | \(L(\mathbb C^3)\to L(\mathbb C^4)\) | \(9\to16\); \(J^\dagger\Lambda_x^c\) is \(9\to9\) |
| \(L_{\Lambda_x(\tau)}\) | \(K_B=L(\mathbb C^3)\to K_B\) | \(9\times9\), represented by \(\Lambda_x(\tau)\otimes I_3\) |
| \(L_{\Lambda_x^c(\tau)}\) | \(K_E=L(\mathbb C^4)\to K_E\) | \(16\times16\), represented by \(\Lambda_x^c(\tau)\otimes I_4\) |
| \(\Delta_J\) | \(L(\mathbb C^3)\to L(K_B)\) | outer map \(9\to81\); each value is \(9\times9\) |
| \(C=\operatorname{Choi}(\Delta_J)\) | \(A\otimes K_B\simeq\mathbb C^3\otimes\mathbb C^9\) | \(27\times27\) |
| \(G_\mu\) | \(\mathbb C^3\to K_B\simeq\mathbb C^9\) | \(9\times3\); its outer CP-map Choi is \(27\times27\) |
| \(L_\mu,\mathcal C,P_j\) | \(A\otimes B\otimes B'\to A\otimes B\otimes B'\) | all \(27\times27\) |
| proposer \(U_j\) | multiplicity slice \(\mathbb C^{m_j}\to\mathbb C^{27}\) | \(27\times(1,3,2,1)\); not a full isotypic basis |
| \(G_j=U_j^TU_j,B_j=U_j^TCU_j\) | multiplicity space | \(m_j\times m_j\); \(B_j-zG_j\) is the correct generalized pencil |
| \(V(O)\) | \(\mathbb C^4\to\mathbb C^4\) | \(4\times4\); lower block is \(\det(O)O\) |
| congruence identity | \(J_i:K_B\to K_E,\ L:K_E\to K_E\) | \(J_i\) is \(16\times9\), \(L\) is \(16\times16\), result \(9\times9\) |

The proposer and reviewer both use row-major \(E_{ij}\leftrightarrow|i\rangle|j\rangle\) and
Choi input leg first. No transpose, sign, or Choi-leg drift was found. The positive branch
\(k>0\) is required. The only \(1/k\) occurs in \(q\) in residual coordinates; it is defined
for \(0<x<1\). At the forced point \(q=\frac13\sqrt{2(1-x)/x}\), so its limit at \(1^-\) is
zero even though the generic coordinate chart and faithful-output theorem exclude \(x=1\).

Every displayed scalar principal minor is dimensionless and is used with \(0<x<1\). The
three-by-three PSD test uses all seven principal minors, not leading minors only. The
spin multiplicity blocks collectively represent the full \(27\)-dimensional Choi, not a proper
subspace.

## 7b regime-complete identity gates

The independent gates check the full \(9\times9\) intertwining residual and the exact
direct-\(27\times27\)/generalized-block characteristic-polynomial identity at:

| Regime | \(x\) | Defect result | Full rank |
|---|---:|---|---:|
| boundary/rank drop | \(1/2\) | PSD | 3 |
| \(1/2<x<4/7\) | \(26/51\) | PSD | 8 |
| antidegradability marker | \(4/7\) | PSD | 8 |
| \(4/7<x<1\) | \(3/4\) | PSD | 8 |
| quint eigenvalue zero | \(2/3\) | PSD | 8 |
| near faithfulness loss | \(99/100\) | PSD | 8 |
| below \(1/2\) | \(49/100\) | not PSD | 8 |
| further below \(1/2\) | \(2/5\) | not PSD | 8 |

The \(x=2/3\) zero of \(1-3x/2\) causes no derivation degeneration: no step divides by that
eigenvalue, the intertwining rank minor \(3x^3/2\) remains nonzero, and the defect blocks are
regular.

Untested regimes: there is no untested regime inside the claimed real interval \(0<x<1\).
The maps at \(x=0\) and \(x=1\) are outside the residual \(1/k\) chart and outside the strict
faithfulness hypotheses; \(x=1\) is treated only as a one-sided degeneration. Nonreal \(x\),
non-equivariant lifts, and the full Haar-averaging/WLOG lemma are out of scope. The cited HRSF22
theorems were audited through the local Zhu-Wang statement, not re-proved or independently
checked from a separate HRSF22 PDF.

## 7d-7g audit

### 7d - no frozen-input immunity

The \(x=1/2\) calibration was rechecked entrywise. Every general-\(x\) complement,
intertwining, defect, block, elimination, endpoint, and covariance assertion was independently
derived; no P1 result was treated as covering a new parameter regime.

### 7e - standing failure modes

- Normalization: the \(k^2=x(1-x)/2\) and \(2/9\) defect factors agree entrywise.
- Types/dimensions: all compositions above are well typed.
- Undefined terms: resolved in 7g below.
- Partial substitution: the review used every principal minor and also the full \(27\times27\)
  characteristic polynomial.
- Value/derivation mismatch: independent matrix-unit constructions verify the formulas, not
  merely printed values.
- Sign/transpose/Choi drift: none found.
- Solver-status laundering: no optimizer is used; all certificates are exact SymPy algebra and
  rational/surd data.
- Rounding: `1.00000000` is labeled only as numerical endpoint corroboration; the mathematical
  statement is the exact supremum \(1\), not feasibility at \(x=1\).
- Branch loss: elimination uses negative squares with nonzero linear coefficients for \(x>0\),
  not a black-box `solve`. The unique solution is substituted into every remaining minor.
- Failed runs: JSON serialization, brittle expression-equality, and Groebner coefficient-domain
  failures are retained. None is used as evidence; the final runs exit zero.

### 7f - verification versus reproduction

Verification came from the independent scripts and different tensor bases frozen by
`ANCHORING_BOUNDARY_SHA256.txt`. This establishes the mathematical objects and formulas.
Reproduction separately imported the unchanged proposer sources after verifying their hashes,
redirected generated writes to `proposer_reproduction/`, and reran all three entry points.
After deleting only `runtime_seconds`, all three reproduced JSON files equal the originals.
Reproduction establishes provenance and repeatability; it is not counted as independent
verification.

### 7g - quantifier hygiene

- **feasible region:** \(\{x\in(0,1):\exists(s_1,s_2)\in\mathbb R^2,\ C(x,s_1,s_2)\succeq0\}\).
- **forced/unique:** every PSD Choi must make the listed negative-square principal minors zero;
  their rank-two linear system has exactly the displayed solution for \(x>0\).
- **rank-one form:** \(B=d\,\ell\ell^T\), with rational \(d\ge0\) and displayed \(\ell\).
- **solver-free certificate:** exact parameter values plus exact block congruence/LDL data and
  a direct characteristic-polynomial identity, with no numerical solver.
- **\(x_{\max}=\sup\):** the supremum of feasible \(x\in[1/2,1)\); it is \(1\), not an attained
  faithful endpoint.
- **covariant/equivariant:** the two displayed \(O(3)\) covariance identities with
  \(V(O)=\operatorname{diag}(1,\det(O)O)\).
- **adjoint preserving:** \(J(Y^\dagger)=J(Y)^\dagger\), equivalently on the real matrix-unit
  basis \(J(E_{ji})=J(E_{ij})^T\).

## Claim-by-claim adjudication

1. **PASS - general-\(x\) complement and adjoint.** Independent Kraus reconstruction,
   block formula, positive-\(k\) branch, and \(16\to9\) HS adjoint all agree entrywise.

2. **PASS - ansatz and intertwining.** The ansatz is equivariant and adjoint preserving.
   The three sector equations exhaust the \(1+5+3\) input decomposition, the full matrix residual
   vanishes, and rank is three for every \(0<x<1\), including \(2/3\).

3. **PASS - residual family and calibration.** The independent \((p,r)\) family maps exactly to
   the proposer's \((s_1,s_2)\) formulas and recovers the Zhu-Wang lift at \(x=1/2\).

4. **PASS - defect Choi, spin reduction, and minors.** The \(27\times27\) construction,
   multiplicities \(1,3,2,1\), all principal minors, spin-0 factor, the three spin-1
   negative squares, \(\det B_2\), and \(B_3=0\) agree. Independent bases give the same
   generalized spectra.

5. **PASS - elimination and reduced blocks.** PSD forces the unique displayed \(s_1,s_2\).
   No alternative branch survives. Both proposer reduced blocks are the stated rank-one forms.

6. **PASS - exact feasible region and endpoints.** The region is exactly
   \(1/2\le x<1\). Strictly below \(1/2\), the forced spin-2 block is negative. Rank is three at
   \(1/2\), eight in the open interior, and the faithful environment output degenerates at \(1\).

7. **PASS - three exact certificates and spectrum linkage.** At \(26/51,4/7,3/4\), the exact
   \(s_1,s_2,q\), rank-one block data, and direct/generalized characteristic polynomials agree.
   The full rank is eight at each point.

8. **PASS - twirling ingredients, limited scope.** The axial identity with the determinant
   twist, both covariance identities, and
   \[
   \tfrac12(J_1^\dagger LJ_1+J_2^\dagger LJ_2)
   -\bar J^\dagger L\bar J
   =\tfrac14(J_1-J_2)^\dagger L(J_1-J_2)\succeq0
   \]
   are correct. They establish covariance and convexity/concavity needed by an averaging
   argument. They do **not** establish closure of every admissibility constraint under the
   transformed lift, Haar integration, exhaustiveness of the five-parameter family after
   averaging, or a full WLOG lemma. The executor did not claim those conclusions.

9. **PASS - generic-theorem hypothesis audit only.** The local PDF's Theorem 3.3 requires:
   finite-dimensional channels; \(M(I)>0,N(I)>0\); linear adjoint-preserving \(J\);
   \(J^\dagger N=M\); and CP of the outer defect. These are exactly the channel-specific facts
   established for \(M=\Lambda_x,N=\Lambda_x^c\) on \(x\in[1/2,1)\).

   Lemma 3.2 retains finite dimensionality and strict output faithfulness. Corollary 3.7
   additionally requires that \(N\) be complementary to \(M\). HRSF22 hybrid tensorization acts
   on the complete relative-entropy order for every finite reference and state pairs satisfying
   \(\operatorname{supp}\rho\subseteq\operatorname{supp}\sigma\).

   A full application write-up must still state and discharge explicitly:

   1. the Kraus family is CPTP for every \(x\in[1/2,1)\), and the displayed \(N\) is its chosen
      complement;
   2. \(N^{\otimes n}\) is a complement of \(M^{\otimes n}\), up to the standard environment
      isometry;
   3. the complete-relative-entropy quantifier includes all finite references and all admissible
      support pairs;
   4. in the private-information step, zero-probability ensemble terms are discarded and
      \(\operatorname{supp}\rho_u\subseteq\operatorname{supp}\bar\rho\);
   5. in the coherent-information step, the purification support inclusion used in Corollary 3.1
      holds;
   6. tensorization is applied with the orientation
      \((\Lambda_x^c)^{\otimes n}\succeq_{\mathrm{cRE}}\Lambda_x^{\otimes n}\), followed by the
      one-shot optimizations and their regularizations;
   7. \(x=1\) is excluded because \(N(I)\) is not faithful there.

   These obligations are routine consequences stated in the local PDF, but the executor
   expressly did not claim or write this application.

## Solver-free certificate summary

| \(x\) | \((s_1,s_2)\) | proposer \(B_1=d_1\ell_1\ell_1^T\) | proposer \(B_2=d_2\ell_2\ell_2^T\) |
|---:|---:|---:|---:|
| \(26/51\) | \((25/39,14/39)\) | \(d_1=50/221,\ \ell_1=(1,-1,1)\) | \(d_2=50/1989,\ \ell_2=(1,-1)\) |
| \(4/7\) | \((1/2,1/2)\) | \(d_1=5/21,\ \ell_1=(1,-1,1)\) | \(d_2=1/7,\ \ell_2=(1,-1)\) |
| \(3/4\) | \((2/9,7/9)\) | \(d_1=5/27,\ \ell_1=(1,-1,1)\) | \(d_2=2/9,\ \ell_2=(1,-1)\) |

In every row \(B_0=B_3=0\), and the direct \(27\times27\) characteristic polynomial equals the
product of the generalized block polynomials with multiplicities \(2j+1\).

## Licensing statements

1. **this review does open the completion gate for the exact feasible-region theorem for the
   covariant family, at tier PROVED, with scope \(0<x<1\): within the frozen five-parameter real
   \(O(3)\)-equivariant adjoint-preserving ansatz, the defect Choi is PSD exactly for
   \(1/2\le x<1\), at the unique displayed residual point.**

2. **this review does open the completion gate for the three-point exact certificates, at tier
   PROVED, with scope \(x=26/51,4/7,3/4\): exact lift parameters, all four spin blocks, solver-free
   PSD congruences, and direct-\(27\times27\)/block spectrum linkage.**

3. **this review does open the completion gate for the twirling ingredients, at tier PROVED, with
   scope the two \(O(3)\) covariance identities (including the epsilon determinant twist) and the
   congruence-convexity identity only; it does not license a full averaging/WLOG or
   non-equivariant-infeasibility theorem.**

4. **this review does not open the completion gate for the generic-theorem application, at tier
   PROVED, with scope the conclusion \(Q(\Lambda_x)=P(\Lambda_x)=0\) for all
   \(x\in[1/2,1)\): the hypothesis audit passes, but the executor did not claim the application
   and a full write-up must explicitly discharge the seven support, complement, tensorization,
   and capacity obligations listed under claim 9.**

Consequently, **this review does not open the completion gate for the full current node claim as
worded**, because that claim includes the zero-capacity conclusion. It does open the three
separately scoped mathematical subclaims above. No node status is written by this reviewer.

## Provenance and budget

- Independent derivation and gates:
  [`independent_derivation.log`](logs_whgap_p2_review_20260728/independent_derivation.log),
  [`independent_elimination.log`](logs_whgap_p2_review_20260728/independent_elimination.log),
  [`independent_regime_gates.log`](logs_whgap_p2_review_20260728/independent_regime_gates.log),
  [`independent_types_adjoints.log`](logs_whgap_p2_review_20260728/independent_types_adjoints.log),
  and [`independent_twirling.log`](logs_whgap_p2_review_20260728/independent_twirling.log).
- Anchoring boundary:
  [`ANCHORING_BOUNDARY_SHA256.txt`](logs_whgap_p2_review_20260728/ANCHORING_BOUNDARY_SHA256.txt).
- Unchanged proposer reproduction:
  [`proposer_reproduction_comparison.log`](logs_whgap_p2_review_20260728/proposer_reproduction_comparison.log)
  and the `proposer_reproduction/` JSON.
- Literature audit: local PDF pages 5-10 were extracted and visually inspected; the text
  extraction and capability-failure record are in the review log directory.
- Failed independent attempts are append-only: one positive-square-root simplification gate, two
  twirling tooling-domain/PSD-check gates, and the unavailable-`pypdf` attempt. They do not
  support any verdict.
- Every Python invocation used `C:<home>/cpython3119/python.exe`.
- `tools/proof_dag_check.py --problem werner-holevo-gap` and
  `tools/literature_check.py` both exited zero. The repository-wide `git diff --check` reports
  only pre-existing trailing whitespace in unrelated generated
  `artifacts/quantum_query_progress_note.{aux,log}` files; the review-scoped diff check exited
  zero, and those user-owned files were not modified.
- The independent gates and reproduction remained well inside the 75-minute budget; no symbolic
  step approached the 15-minute stop-loss and no two information-free cycles occurred.

Final hashes are in
[`SHA256SUMS.txt`](logs_whgap_p2_review_20260728/SHA256SUMS.txt).

