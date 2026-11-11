# Independent adversarial review of the selected-line qutrit Weyl majorization theorem

**Date:** 2026-08-30  
**Reviewer:** OpenAI Codex review agent  
**Primary target:** `HEXT.f3-weyl-selected-line-majorization` and its exact odd-index KKT route  
**Downstream target:** `HEXT.qutrit-weyl-random-unitary-bell-no-go`  
**Review status:** completed, immutable; any later correction should be a new review object rather than an edit to this file

## Independence and repository discipline

I performed this review in a fresh, separately commissioned review context. I did not author any
of the theorem, checker, certificate, or node inputs. I did not receive or use private proposer
reasoning, did not communicate with the proposer, and used no subagent. I reconstructed the
load-bearing arguments from the disk objects listed below, independent algebra, independent exact
test programs entered at the terminal, and fresh full reproductions of all four certificates.

The theorem files, checker files, certificate files, canonical YAML nodes, and generated DAG views
were read-only throughout. The requested review directory and this report are the only durable
writes made by this review. I did not stage, commit, push, regenerate a view, or alter canonical
research state.

## Executive verdict

**F3W-IR-VERDICT-MATH: PASS / PROVED by independent adversarial review.** For every probability
distribution \(p\) on \(\mathbb F_3^2\), and for **every choice** of a direction containing a
maximum-mass affine line (including every tie case), if \(r\) is the sorted vector of masses of the
three parallel lines, then

\[
  p*\widetilde p\prec r\otimes r.
\]

The affine normalization is exhaustive, the paired sorting and odd-to-even interpolation are
correct, the \(k=5\) and \(k=7\) objective formulas are exact, the twenty inequalities define the
intended compact polytope without omissions, the KKT active-face enumeration is complete, the
multiplier sign convention is correct, and the exact solvers and recorded counts passed full fresh
reproduction. I found no fatal mathematical issue and no mathematical repair is required.

**F3W-IR-VERDICT-NOGO: PASS for the stated Weyl/Bell scope.** The reviewed majorization gives

\[
 H(p*\widetilde p)\ge 2H(r)\ge 2\min_L H(p\bmod L).
\]

The direct Weyl Bell-basis and stabilizer-coset identities then give

\[
 2\overline S_{\min}(\Phi_p)
 \le S((\Phi_p\otimes\overline{\Phi_p})(\Omega_3)).
\]

Thus the mathematical claim and route implication in
`HEXT.qutrit-weyl-random-unitary-bell-no-go` are valid. This excludes only qutrit Weyl
random-unitary factors with the conjugate maximally entangled witness. It does not exclude
non-Weyl Gram channels, non-Bell joint inputs, or settle the full-size extensive question.

Two nonfatal record issues remain:

1. **F3W-IR-09 is a low-severity wording/scope issue.** The first-three checker and certificate
   end by saying that their single run certified \(k=1,2,3\), although that script proves \(k=3\)
   and obtains \(k=2\) only after importing the separately certified \(k=1\) theorem. The theorem
   and DAG premise state this dependency correctly, so the assembled mathematics is unaffected.
2. **F3W-IR-10 requires a DAG-semantic patch before canonical promotion through the current
   dependency chain.** Two routes list broad, unresolved premises that their implications do not
   use. These conservative extra edges do not make any claim false, but they violate the protocol's
   “all and only load-bearing premises” rule and would unnecessarily block promotion.

## 1. Protocol and immutable input binding

I read all 283 lines of `DAG_PROTOCOL.md` and all 166 lines of `FILE_PROTOCOL.md` before auditing
the mathematical objects. The following SHA-256 values bind this review to the exact disk inputs.

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| `holevo-extensive-violation/artifacts/F3_WEYL_SELECTED_LINE_MAJORIZATION_THEOREM_20260830.md` | `352d4bd3774823a8b1cd58d51c06fd8d2b119f7ee639a601f527663c5a5d6158` |
| `holevo-extensive-violation/tools/certify_f3_weyl_majorization_k5.py` | `c674ad3607bf9811a48091c583142350bdb35fcc3332221295487e96fefa52bb` |
| `holevo-extensive-violation/tools/certify_f3_weyl_majorization_k7.py` | `1e990e83565358b2d6dddd8490dab2ce6816d9420eb9fe6823990c70b30e371a` |
| `holevo-extensive-violation/artifacts/F3_WEYL_MAJOR_K5_CERTIFICATE_20260830.txt` | `2e755be4887ed4ffb1a1f3e39c51f80fef542d46fc026d1984e1117f13dbe499` |
| `holevo-extensive-violation/artifacts/F3_WEYL_MAJOR_K7_CERTIFICATE_20260830.txt` | `43a1ae275c540dbdef7e2a1624f067d022dac2387f194151d3c530abd90c166b` |
| `holevo-extensive-violation/artifacts/F3_AFFINE_LINE_L2_MAXIMAL_THEOREM_20260830.md` | `126585afa694b274844c86df9c9cbc12074501b2877ab9d312e08d3c3f2d937e` |
| `holevo-extensive-violation/tools/certify_f3_affine_line_l2_maximal.py` | `eee01f866640c1bbc5aa2725fc16af36543d4f05b291468bd7db26fcb88cab28` |
| `holevo-extensive-violation/artifacts/F3_AFFINE_LINE_L2_MAXIMAL_CERTIFICATE_20260830.txt` | `638eb86a7a7d75fef01d496cd18f828bcd32da89b56fb674a55ce4c85ec9a40f` |
| `holevo-extensive-violation/artifacts/F3_WEYL_MAJOR_FIRST_THREE_THEOREM_20260830.md` | `df0767fbe8b95d9db6e308dc0efb12969cedb50b056b384d28ec175649d822c2` |
| `holevo-extensive-violation/tools/certify_f3_weyl_majorization_first_three.py` | `8b5af3fcebbffac287636c4fe93582a50203a14d80d13da2fbd5f883e3a68802` |
| `holevo-extensive-violation/artifacts/F3_WEYL_MAJOR_FIRST_THREE_CERTIFICATE_20260830.txt` | `28096f4df11e3ad4ae0bd3505b6b469ff9dc876e51d62c3b8b31f0359ba91e58` |
| `holevo-extensive-violation/proof-dag/nodes/HEXT.f3-affine-line-l2-maximal.yaml` | `d7ef972060862ef2713c069dc59475d3a8e59eb53afcced5efe98d485a943917` |
| `holevo-extensive-violation/proof-dag/nodes/HEXT.f3-weyl-majorization-first-three.yaml` | `b377b6c58bb1fd180cf7b33386f94d095f37925ec2795a53dee059955e07cfcb` |
| `holevo-extensive-violation/proof-dag/nodes/HEXT.f3-weyl-selected-line-majorization.yaml` | `8fd125bfc4a6c63bc3214493610f5a43c8348705e8759420766eb8158a8b8274` |
| `holevo-extensive-violation/proof-dag/nodes/HEXT.qutrit-weyl-random-unitary-bell-gate.yaml` | `e8310d0bebc8d2f6deed807496104dec12c7f01d95e5f2806215aa432ed4ba12` |
| `holevo-extensive-violation/artifacts/QUTRIT_WEYL_RANDOM_UNITARY_BELL_GATE_20260830.md` | `5bb43f4e147de3c060bd73c3099a8ad5b4ab2bff14716b1a0e6f4ff62570f88d` |
| `holevo-extensive-violation/proof-dag/nodes/HEXT.qutrit-weyl-random-unitary-bell-no-go.yaml` | `f298e6f0caeb28f394d75f760e5653415b9eeaa4ea3bbdae4d19041bf3fa75e3` |

### Exact statement hashes for review links

Hashes below use the repository rule `sha256(statement.strip())` after CRLF normalization.

| object | exact reviewed hash |
|---|---|
| `HEXT.f3-affine-line-l2-maximal` claim | `sha256:8cf676f4f11cef89d78d0a2c38ed918be816fe8158e701982b3816eb5f7d72d2` |
| route `exact-parametric-vertex-route` implication | `sha256:51c6ed02855fc6f8c352b8d9ac89abb071d2f15aaf58cc3ca0dd7097304afdd8` |
| `HEXT.f3-weyl-majorization-first-three` claim | `sha256:7a525abb25032b1fdce84fc07c5bf171abe3b74102c9a36fb4948829a4b216c8` |
| route `exact-k3-parametric-route` implication | `sha256:5d8bcd407b75e5642f76a96975eef0e8657348e49cd98f0cdc882dfbdf40357b` |
| `HEXT.f3-weyl-selected-line-majorization` claim | `sha256:db13a888f41bd724df53a5c3cf03c27a682419a0171f1a29c5ec6bf85e62a507` |
| route `exact-odd-index-kkt-route` implication | `sha256:d203bc181d4d206ac2f02e91842116e8110705895bbc7ab1d03a9a8267c99b4a` |
| `HEXT.qutrit-weyl-random-unitary-bell-gate` claim | `sha256:7ef8f24523339c6b19222ee9b209308769a6b7e712833f4994dfb429b9b1dd0d` |
| route `weyl-stabilizer-reduction` implication | `sha256:a980bdc267fcc79ad2861397b7d58f11a0a8cc309c65292dc775eaedc75684b7` |
| route `renyi2-shadow-route` implication | `sha256:e8bf1a64c6446cf28cf26d560d59afd655bb60e5a1dfc04803bdaf3b068a29da` |
| `HEXT.qutrit-weyl-random-unitary-bell-no-go` claim | `sha256:f502e1b657a950bf33225dc5c1dd551193a7040452ea50b4c211c9b545478276` |
| route `selected-line-majorization-route` implication | `sha256:7e38c098dc38df219e6c0c9047ae20b219932754775b2c7db9dfb9072a35e449` |

## 2. Fresh reproduction and independent cross-check ledger

The review environment was Darwin 25.6.0 arm64 with CPython 3.9.6 and `__debug__=True`.
All commands were read-only. The four official checkers use only the Python standard library.

### Full official reproductions

| checker | active/basis sets | nonsingular | feasible | dual feasible / unique families | exact minimum | result |
|---|---:|---:|---:|---:|---:|---|
| affine-line \(k=1\) | 203,490 | 107,136 | 10,458 | 5,238 unique families | 0 | exact match to certificate |
| first-three \(k=3\) | 18,564 | 11,934 | 3,123 | 2,367 unique families | 0 | exact match to certificate |
| stronger \(k=5\) | 263,950; 232,006 independent | 1,327,083 | 49,683 | 12,777 | 0 | exact match to certificate, including smallest record |
| \(k=7\) | 263,950; 232,006 independent | 881,269 | 38,367 | 17,773 | 0 | exact match to certificate, including smallest record |

The full commands were exactly the commands in the theorem/certificate records. Every process exited
with status zero. The \(k=5\) smallest record was
`((0, 11), (2, 3), (0,1/4,1/4,1/4,0,0,1/4,0), (2,1/2))`; the \(k=7\) smallest record was
`((0, 1), 0, (0,0,1,0,0,0,0,0), (2,2))`, with the entries interpreted as exact `Fraction`s.

### Independent checks not supplied by the proposer

1. I independently enumerated all subsets of the twenty constraint normals of size at most eight.
   The exact counts by size `(size, all, independent)` were

   ```text
   (0, 1, 1)
   (1, 20, 20)
   (2, 190, 190)
   (3, 1140, 1140)
   (4, 4845, 4845)
   (5, 15504, 15489)
   (6, 38760, 38418)
   (7, 77520, 73755)
   (8, 125970, 98148)
   ```

   This gives 263,950 total and 232,006 independent sets. The largest squared norm of a constraint
   normal is 15, so Hadamard bounds every relevant minor by \(15^4=50,625<1,000,003\);
   the independent modular count is therefore exact over the rationals.
2. A separately written rational reduced-row-echelon solver matched the KKT checker's
   fraction-free solver on 1,600 random integer systems, 100 at every size from 1 through 16.
   Separate tests of the two earlier solvers matched independent rational elimination on another
   1,000 random integer systems. No mismatch or unexpected divisibility failure occurred.
3. On 200 arbitrary rational point distributions, all four generated \(k=7\) quadratics and all
   six generated \(k=5\) quadratics agreed exactly with independently computed autocorrelations,
   quotient collision probabilities, and row masses.
4. I exhaustively enumerated every nine-cell nonnegative integer distribution of total mass 8 and
   9, checked every admissible selected maximum-line direction, and directly sorted both sides.
   Across 37,180 distributions and 54,040 selected-direction incidences, all eight nontrivial
   cumulative inequalities held. This census included 12,160 distributions with a tie between
   selected directions, including the uniform and other multiple-maximum-line cases.
5. A pre-write `python3 tools/proof_dag_check.py --problem holevo-extensive-violation` run reported
   all 86 then-present node files structurally valid. A post-write rerun observed 87 structurally
   valid node files after concurrent repository growth; none of the hash-bound target inputs had
   changed. This structural result does not replace the mathematical review and does not detect the
   extra-premise issue in Finding F3W-IR-10.

The exhaustive grids are adversarial diagnostics only. The universal verdict rests on the exact
symbolic reductions and complete active-set arguments reviewed below.

## 3. Findings

### Finding F3W-IR-01 — PASS: affine normalization is exhaustive, including ties

**Stable source locators:** selected-line theorem, Statement and lines 34–41; \(k=7\) checker,
`build_points_constraints_and_rows` lines 42–69; target node claim lines 6–9.

Let the selected maximum-mass affine line be

\[
 \ell=\{x:u(x)=t\}
\]

for a nonzero linear functional \(u\). Choose an independent linear functional \(v\). The affine
bijection \(x\mapsto(u(x)-t,v(x))\) sends \(\ell\) to row zero and its parallel class to the three
rows. Multiplying the first coordinate by \(-1=2\) fixes row zero and swaps rows one and two, so the
remaining masses can always be labeled \(b\ge c\). With \(a\) the selected line mass,

\[
 a\ge b\ge c,\qquad a+b+c=1.
\]

Because \(\ell\) is globally maximum among all twelve affine lines, every nonparallel affine line
has mass at most \(a\). Conversely, those bounds and \(a\ge b\ge c\) make row zero a global
maximum line. All inequalities are weak. If another row or another direction ties the chosen line,
the normalized point lies on the corresponding boundary face and remains in the checker domain.
The proof therefore works for any choice among tied maximum-line directions; it does not rely on a
unique maximizer.

**Verdict:** no omission and no repair.

### Finding F3W-IR-02 — PASS: paired sorting and every even interpolation are correct

**Stable source locators:** selected-line theorem equations (4)–(6), lines 43–66; first-three
theorem equations (13)–(14), lines 128–145.

For \(q_g=\sum_xp_xp_{x-g}\), one has \(q_g=q_{-g}\). The eight nonzero elements of
\(\mathbb F_3^2\) form four pairs \(\{g,-g\}\). Also

\[
 q_g\le \left(\sum_xp_x^2\right)^{1/2}
           \left(\sum_xp_{x-g}^2\right)^{1/2}=q_0,
\]

so after sorting the spectrum has the cumulative-equivalent form

\[
 q_0,y_1,y_1,y_2,y_2,y_3,y_3,y_4,y_4,
 \qquad y_1\ge y_2\ge y_3\ge y_4.
\]

Therefore \(2Q_{2j}=Q_{2j-1}+Q_{2j+1}\). For any sorted vector, its top-\(k\) cumulative sums are
concave in \(k\), hence \(2R_{2j}\ge R_{2j-1}+R_{2j+1}\). Odd inequalities at
\(k=1,3,5,7\) consequently imply all four even inequalities, including \(k=8\) using \(Q_9=R_9=1\).
Ties in \(q_0\), among the \(y_i\), or among product entries do not affect these identities.

**Verdict:** no sorting or interpolation error.

### Finding F3W-IR-03 — PASS: the \(k=5\) formula and stronger objective are exact

**Stable source locators:** selected-line theorem equations (7)–(10), lines 68–99; \(k=5\)
checker `quotient_lines` and `build_k5_objective`, lines 45–71.

For the four one-dimensional directions \(L_i\),

\[
 C_i=\Pr[X-Y\in L_i]=q_0+2x_i.
\]

The top five autocorrelation entries are \(q_0\) and the two largest equal pairs, so

\[
 Q_5=\max_{i<j}(C_i+C_j-q_0).
\]

For \(a\ge b\ge c\), the product multiset is

\[
 a^2,ab,ab,ac,ac,b^2,bc,bc,c^2.
\]

After the first three entries \(a^2,ab,ab\), the next two are \(ac\) and
\(\max\{ac,b^2\}\). Thus

\[
 R_5=a^2+2ab+ac+\max\{b^2,ac\}
     \ge a^2+2ab+2ac=2a-a^2.
\]

The script's exact objective is

\[
 f_{ij}=2a-a^2-C_i-C_j+q_0.
\]

The quotient normals `(1,0),(0,1),(1,1),(1,2)` enumerate all four projective directions, and all
six unordered pairs are checked. Direct exact objective reconstruction on arbitrary rational inputs
agreed with this formula.

**Verdict:** the stronger six inequalities imply the true sorted \(k=5\) inequality on both
branches \(b^2\ge ac\) and \(b^2\le ac\), including equality.

### Finding F3W-IR-04 — PASS: the \(k=7\) formula and four objectives are exact

**Stable source locators:** selected-line theorem equations (11)–(12), lines 101–120; \(k=7\)
checker constants `NORMALS`, `SHIFTS` and `build_k7_objective`, lines 24–27 and 85–100.

The two smallest autocorrelation entries are the equal pair \(y_4,y_4\). The two smallest product
entries are \(c^2\) and one of the two copies of \(bc\), since \(c^2\le bc\le ac\) and
\(bc\le b^2\). Hence

\[
 Q_7=1-2y_4,\qquad R_7=1-c^2-bc.
\]

It suffices to prove \(2x_i\ge c(b+c)\) for all four projective directions. The checker shifts

```text
(0,1), (1,0), (1,2), (1,1)
```

are respectively nonzero generators of the kernels of the four normals. Its quadratic is exactly
\(2q_g-cb-c^2\). The exact direct-objective cross-check confirmed all four mappings.

**Verdict:** no direction, factor-of-two, or bottom-entry error.

### Finding F3W-IR-05 — PASS: the twenty-inequality polytope is complete

**Stable source locators:** selected-line theorem lines 122–133; \(k=7\) checker
`build_points_constraints_and_rows`, lines 42–69.

After eliminating \(p_{22}=1-\sum_{x\ne(2,2)}p_x\), the checker has eight free variables and exactly:

1. nine point nonnegativity inequalities, including the eliminated point;
2. \(a-b\ge0\) and \(b-c\ge0\);
3. three line-mass bounds for each of the other three projective directions, for nine bounds total.

The selected parallel class is already controlled because its line masses are \(a,b,c\) and
\(a\ge b\ge c\). The other nine bounds cover every nonparallel affine line exactly once.
Normalization is built into the eliminated point; point nonnegativity gives \(a,b,c\ge0\), and
ordering plus normalization gives \(a\ge1/3\). The domain is a closed subset of the probability
simplex and is compact. There is no missing \(a\)-range or selected-row constraint.

**Verdict:** the checker domain equals the normalized theorem domain.

### Finding F3W-IR-06 — PASS: KKT active-face enumeration and singular-system omission are complete

**Stable source locators:** selected-line theorem lines 135–146; \(k=7\) checker
`independent_rows`, lines 155–193; `kkt_system`, lines 196–210; enumeration lines 253–285; analogous
\(k=5\) enumeration lines 98–128.

Write every constraint as \(g_i(x)=c_i+n_i^Tx\ge0\), and write a checked quadratic as

\[
 f(x)=c+\ell^Tx+\tfrac12x^THx.
\]

At a global minimizer \(x\), first-order optimality for a polyhedron gives

\[
 \nabla f(x)\in\operatorname{cone}\{n_i:g_i(x)=0\}.
\]

Choose an independent conic support for this representation and extend it, using active normals and
zero added multipliers, to a basis \(B\) for the full active-normal span. This is the small step that
must accompany the theorem's phrase “after a basis for the full active-normal span is chosen”; it
preserves nonnegative multipliers and has size at most eight. The enumeration includes \(B\).

Now choose, among all global minimizers, one whose minimal face has least dimension. If the bordered
KKT matrix for \(B\) were singular, independence of the rows of \(B\) would give a nonzero vector
\(v\) and some \(\mu\) with

\[
 Bv=0,\qquad Hv=B^T\mu.
\]

Thus \(v\) is tangent to the full face,

\[
 v^THv=v^TB^T\mu=0,
 \qquad
 \nabla f(x)^Tv=\lambda^TBv=0,
\]

and the quadratic is exactly constant on the line \(x+tv\). The compact face meets that line in a
nontrivial closed segment whose endpoint lies on a proper subface. That endpoint is another global
minimizer, contradicting the minimal-face choice. Therefore at least one dual-feasible KKT system
for the global minimizer is nonsingular and retained by the checker.

The proof works for indefinite quadratics and does not assume convexity. It also explains why it
would be insufficient merely to use an arbitrary independent conic support without extending it to
the full active-normal span; the zero-multiplier extension resolves that point.

**Verdict:** every global minimum appears among the retained exact candidates; no singular minimum
is lost.

### Finding F3W-IR-07 — PASS: multiplier signs and exact linear algebra are correct

**Stable source locators:** \(k=7\) checker `full_rank_mod_prime`, lines 103–121;
`solve_integer_system`, lines 124–152; `kkt_system`, lines 196–210; `feasible`, lines 213–217;
multiplier filter lines 273–285.

With \(g_i=c_i+n_i^Tx\ge0\), the appropriate minimum condition is
\(\nabla f=\sum_i\lambda_i n_i\) with \(\lambda_i\ge0\). The checker solves

\[
 Hx-N^T\lambda=-\ell,
 \qquad Nx=-c,
\]

which is exactly this convention, and filters `multiplier < 0`. Primal feasibility evaluates all
twenty affine forms as exact `Fraction`s.

The modular rank result is never used to discard a KKT matrix. A nonzero modular determinant proves
nonsingularity; a zero residue still goes to the fraction-free integer solver. The exact solver
decides singularity and reconstructs rational solutions. The independent Fraction-RREF tests
covered all possible KKT sizes and agreed exactly. The prime 1,000,003 is prime.

For the earlier fixed-size rank gates, the Hadamard bounds are also valid: the \(k=1\) active
matrices have row norm at most \(\sqrt8\), so \(|\det|\le4096\); the \(k=3\) active matrices have row
norm at most \(\sqrt6\), so \(|\det|\le216\). In those two checkers, modular singularity is therefore
equivalent to rational singularity.

**Verdict:** no sign reversal, modular false-negative discard, truncation, or inexact comparison.

### Finding F3W-IR-08 — PASS: the earlier \(k=1\) and \(k=1,2,3\) dependencies are sound

**Stable source locators:** affine-line theorem lines 35–103 and checker lines 78–179, 182–253;
first-three theorem lines 38–145 and checker lines 38–80, 144–268, 271–348.

For fixed \(M\), the affine-line checker maximizes the convex collision functional over the compact
line-capped polytope. A convex function attains a maximum at some vertex. Every vertex in the
eight-dimensional eliminated space has eight independent active normals, so all
\(\binom{21}{8}=203,490\) bases suffice. Exact affine vertex families, exact feasibility intervals,
and exact quadratic interval minima cover every \(M\in[1/3,1]\). The fresh full count and minimum
matched the certificate.

For fixed \(a,b\), each line collision \(C_i\) is a convex quadratic in the six point variables, so
its maximum occurs at a vertex. All \(\binom{18}{6}=18,564\) active bases are enumerated. Every
parameter polygon is the intersection of all substituted inequalities with the ordered
\((a,b,c)\) domain. The minimizer of a quadratic on a compact polygon is covered by polygon
vertices, stationary points on every edge, and interior stationary points. The implementation
checks all vertex-pair chords, a conservative superset that includes every edge. A singular
stationary affine set reaches the boundary; its boundary minimum is already among the edge/vertex
candidates. The fresh full count and minimum matched the certificate.

Finally, \(q_0+2\max_i x_i=\max_iC_i\), while the top three entries of \(r\otimes r\) are
\(a^2,ab,ab\). Thus \(C_i\le a^2+2ab\) proves \(k=3\), and the paired identity with the separately
proved \(k=1\) inequality gives \(k=2\).

**Verdict:** the premise chain supplies exact \(k=1,2,3\); no earlier certificate count or
mathematical scope is missing.

### Finding F3W-IR-09 — WORDING/SCOPE ISSUE: the first-three run does not alone certify \(k=1\)

**Stable source locators:** first-three checker docstring lines 2–7 and final line 346;
`F3_WEYL_MAJOR_FIRST_THREE_CERTIFICATE_20260830.txt` line 7; first-three node route premise lines
11–18 and evidence locator lines 51–54.

The checker correctly says in its docstring that \(k=1\) is supplied by
`certify_f3_affine_line_l2_maximal.py`. Its computation proves \(k=3\); the algebraic \(k=2\)
conclusion also needs that separate \(k=1\) result. Nevertheless its final message, repeated in the
certificate and evidence locator, says the single run “certified for cumulative \(k=1,2,3\).”

This does not create a mathematical gap because the canonical route explicitly lists
`HEXT.f3-affine-line-l2-maximal` as a premise and that premise passed a separate full exact review.
The accurate run scope is: “\(k=3\) certified; together with separately certified \(k=1\), paired
interpolation gives \(k=2\).”

**Classification:** low-severity wording/evidence-scope issue, not a theorem defect. It must not be
cited as a standalone \(k=1\) certificate.

### Finding F3W-IR-10 — NEEDS PATCH: two DAG premises are non-load-bearing

**Stable source locators:** `HEXT.f3-affine-line-l2-maximal.yaml` lines 10–18;
`HEXT.qutrit-weyl-random-unitary-bell-gate.yaml` lines 13–24; DAG protocol §2 and node-audit item 2.

The route `HEXT.f3-affine-line-l2-maximal/exact-parametric-vertex-route` lists
`HEXT.qutrit-weyl-random-unitary-bell-gate` as a premise. The pure affine-line inequality and its
elementary \(q_0\le M^2\) majorization consequence do not use that node; the proof source is direct.

Likewise `HEXT.qutrit-weyl-random-unitary-bell-gate/weyl-stabilizer-reduction` lists
`HEXT.gram-channel-entanglement-cost-gate`, but neither the Bell-basis autocorrelation spectrum nor
the stabilizer quotient spectra nor the tensor-product side bound use the general Gram-channel
entanglement-cost theorem. The route implication and its proof source do not invoke that premise.

These are conservative extra dependencies, not missing dependencies. They cannot license an
unsupported conclusion, but under the protocol they prevent the reviewed classical chain from
being promoted unless unrelated broad Gram nodes are also promoted. The direct proofs should be
represented without these unresolved premises (for example as route-free direct proofs, or by a
properly scoped route structure). The broader Gram subtree was not audited here because it is not
load-bearing for the selected-line theorem or Weyl/Bell no-go.

**Classification:** protocol/DAG repair required before applying completion-level promotions
through the current chain; no mathematical repair to the reviewed theorem.

### Finding F3W-IR-11 — PASS: entropy and downstream Weyl/Bell conclusion have the stated scope

**Stable source locators:** selected-line theorem lines 155–159; Weyl gate artifact lines 19–86 and
88–141; no-go node lines 6–18 and caveats lines 37–42.

The normalized Bell identity sends the term indexed by Weyl errors \(z,w\) to the Bell ray indexed
by \(z-w\), so the joint spectrum is \(q=p*\widetilde p\). For a stabilizer direction \(L\), errors
in one coset of \(L\) give the same ray and the three cosets give orthogonal rays, so the output
spectrum of that stabilizer input is \(r_L=p\bmod L\). Tensoring this same input gives

\[
 \overline S_{\min}(\Phi_p)\le\min_LH(r_L).
\]

Shannon entropy is Schur-concave and additive on tensor products, hence the selected-line
majorization gives

\[
 H(q)\ge H(r\otimes r)=2H(r)\ge2\min_LH(r_L)
      \ge2\overline S_{\min}(\Phi_p).
\]

The separate Rényi-2 formula in the gate artifact is also correct:

\[
 \sum_{i=1}^4C_i^2-4C_q
 =4\sum_{i=1}^4x_i(q_0-x_i)\ge0,
\]

using \(0\le x_i\le q_0\). It is not used to infer the Shannon result.

**Verdict:** the no-go claim follows, but only for the fixed-qutrit Weyl random-unitary family and
the conjugate maximally entangled witness. The report does not claim an optimized non-Bell no-go or
a solution of the full extensive Holevo/MOE question.

## 4. Node-by-node adjudication

| object | mathematical verdict | canonical-action boundary |
|---|---|---|
| `HEXT.f3-affine-line-l2-maximal` claim and exact implication | PASS / PROVED | repair its extra premise; link F3W-IR-08 and exact hashes |
| `HEXT.f3-weyl-majorization-first-three` claim and exact implication | PASS / PROVED | scope the old run accurately per F3W-IR-09; link F3W-IR-08 |
| `HEXT.f3-weyl-selected-line-majorization` claim and exact implication | PASS / PROVED | link F3W-IR-01 through F3W-IR-08 and exact hashes |
| `HEXT.qutrit-weyl-random-unitary-bell-gate` direct Weyl claims | PASS / PROVED | repair the non-load-bearing Gram premise; link F3W-IR-11 |
| `HEXT.qutrit-weyl-random-unitary-bell-no-go` claim and selected-line implication | PASS / PROVED for stated scope | link F3W-IR-11 after premises are canonically repaired/promoted |

No level changes are made by this report itself. Any canonical application must follow the atomic
update protocol, retain the exact reviewed hashes, link only the applicable findings, append the
appropriate events, refresh generated views, and run the repository validators.

## 5. Severity summary

| category | findings |
|---|---|
| fatal mathematical issue | none |
| mathematical repair required | none |
| DAG/protocol repair required | F3W-IR-10 |
| wording/evidence-scope issue | F3W-IR-09 |
| passed load-bearing checks | F3W-IR-01 through F3W-IR-08, F3W-IR-11 |

## 6. Limitations

1. This is an exact human/model audit plus executable rational verification, not a proof-assistant
   formalization. The universal proof is nevertheless symbolic; it does not extrapolate from the
   finite grids.
2. The fresh full reproductions validate the exact current script hashes listed in §1. Any change
   to a theorem statement, route implication, checker, or certificate makes the corresponding part
   of this review stale.
3. The review audited the direct Weyl Bell/stabilizer interface needed by the no-go. It did not audit
   the broader Gram-channel entanglement-cost subtree because Finding F3W-IR-10 establishes that it
   is not load-bearing for this result.
4. The conclusion is deliberately limited to selected-line qutrit Weyl majorization and its
   conjugate-Bell obstruction. It supplies no claim about non-Weyl qutrit channels, non-Bell inputs,
   higher prime dimensions, or the full-size extensive problem.
