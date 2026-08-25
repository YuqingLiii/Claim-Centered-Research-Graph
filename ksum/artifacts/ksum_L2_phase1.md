# KSUM.B4b.L2 phase 1 — joint-histogram dual polynomial

Date: 2026-07-19  
Status: **CONJECTURED · pending independent review.**  
Scope: cyclic 2-Sum over \(\mathbb Z_q\). All finite-instance numerics are structure evidence only; no exponent claim is inferred (G11).

## Decision

The route survives both commissioned gates.

1. The preregistered P2 projection test found that the full joint-histogram orbital algebra captures the extracted optimizer blocks exactly up to floating arithmetic, whereas the Hamming-shell coarsening captures only 72.96% and 74.75% of squared Frobenius mass. The gains, 27.04 and 25.25 percentage points, exceed the preregistered 10-point threshold.
2. The P3 rational LPs found strict joint-histogram gains over the ordinary single-histogram restriction. At error \(1/3\), the joint LP certifies degrees \(3,4,4\) at the three commissioned points, compared with \(2,2,4\) for the single-histogram LP.

P4 was therefore entered. This report states the needed asymptotic witness lemma and a proof plan only. It does not prove that lemma or an exponent lower bound.

## 1. The right invariant basis

Let \(A=\mathbb Z_q\), fix the target \(t\), and put
\[
  \sigma(a)=t-a.
\]
Write \(V=\{v:\sigma(v)=v\}\), \(\tau=|V|\), and choose one orientation
\((a_c,b_c)\) of each two-cycle \(c=\{a_c,b_c\}\); there are
\(r=(q-\tau)/2\) such cycles. For an input \(x\in A^N\), let
\[
 n_a(x)=|\{s:x_s=a\}|.
\]
Its complement-paired occupancy record is
\[
 {\cal H}_\sigma(x)=
 \left(
   \{\!\{(n_{a_c},n_{b_c}) : c\in [r]\}\!\}_{\text{pair swaps}},
   \{\!\{n_v:v\in V\}\!\}
 \right).
\]
Thus pair records may be permuted and either coordinate of each pair may be swapped; fixed-point counts may be permuted. Equivalently,
\[
 C(\sigma)\cong (C_2\wr S_r)\times S_\tau,
\]
and \({\cal H}_\sigma\) labels the \(S_N\times C(\sigma)\) input orbits. The exact class stores every count in \(\{0,\ldots,N\}\). Only the Boolean label truncates a fixed-point count to \(0,1,\ge2\):
\[
 F_{N,q,t}(x)=+1
 \iff
 \left[\exists c:\ n_{a_c}n_{b_c}>0\right]
 \ \text{or}\
 \left[\exists v\in V:\ n_v\ge2\right],
\]
with \(F=-1\) otherwise.

### Algebra and filtration

Let \({\cal A}_{N,q,t}\) be the restriction to \(\sum_a n_a=N\) of
\[
 \mathbb Q[n_a:a\in A]^{C(\sigma)}.
\]
A degree-filtered generating family is obtained from falling-factorial polarized power sums
\[
 P_{u,v}=\sum_{c=1}^r
 \left((n_{a_c})_{\underline u}(n_{b_c})_{\underline v}
 +(n_{a_c})_{\underline v}(n_{b_c})_{\underline u}\right),
 \qquad
 Q_s=\sum_{v\in V}(n_v)_{\underline s},
\]
and products of these generators. Their filtered degree is the sum of the falling-factorial orders. Orbit sums of monomials give an equivalent basis.

This is the wreath-product specialization of Tani's multisymmetric setup: row-orbit monomials and power sums are defined at source lines 848–907, the domain-symmetrization/no-degree-loss lemma begins at line 919, the range-vector power sums and replacement step are at lines 1044–1057, and the exact falling-factorial symmetrization is at lines 1898–1933 of
[the local source](references/tani_2410.02243_src/main.tex). Tani's theorem is not applied verbatim to additive 2-Sum: its full range-permutation hypothesis is unavailable. We use its filtered multisymmetric mechanism after replacing the full range group by the actual centralizer \(C(\sigma)\).

The degree here is query degree. With one-hot input indicators
\(X_{s,a}=\mathbf 1[x_s=a]\), each
\((n_a)_{\underline u}\) expands as a sum of degree-\(u\) products over distinct positions. Hence a falling-factorial occupancy monomial of total order \(d\) is the \(S_N\)-symmetrization of a degree-\(d\) query-indicator monomial, up to a nonzero constant. No ordinary polynomial degree in a compressed class label is being substituted for query degree.

### Relation to L33 and Front-L orbitals

The reviewed solver constructs the \(S_N\times C(\sigma)\) reduction through centralizer, input-orbit, pair-orbit, group-algebra, and aligned-isotypic routines in
[the L33 solver](../tools/ksum_l33_reduced_adv.py) at lines 38, 108, 138, 152, and 221. The Front-L extractor's stabilizer block uses
\(H=S_{N-1}\times C(\sigma)\). Its one-input signatures retain the distinguished symbol and the histogram on the remaining positions; its matrix orbitals retain the distinguished ordered symbol pair and the full \(q\times q\) joint count table on the remaining positions. See
[the extractor](../tools/ksum_expL_dual_extract.py) lines 25–71.

The present \({\cal H}_\sigma\) is the one-input, fully \(S_N\)-symmetrized analogue of those signatures. The P2 matrix projection deliberately used the extractor's two-input orbital version so that the test measured the actual saved optimizers rather than a surrogate diagonal statistic.

## 2. Dual witness and exact moment map

Let \({\cal O}\) be the set of \(S_N\times C(\sigma)\) input classes. A class-weight vector \(w=(w_h)_{h\in{\cal O}}\) lifts to the input measure
\[
 \mu(x)=\frac{w_h}{|h|}\quad(x\in h).
\]
It has unit \(\ell_1\) norm exactly when \(\sum_h|w_h|=1\).

For \(\alpha=(\alpha_a)_{a\in A}\in\mathbb Z_{\ge0}^q\), define
\[
 M_{\alpha,h}
 =
 \frac1{|C(\sigma)\cdot n(h)|}
 \sum_{n\in C(\sigma)\cdot n(h)}
 \prod_{a\in A}(n_a)_{\underline{\alpha_a}}.
 \tag{1}
\]
The omitted position-normalization \((N)_{\underline{|\alpha|}}^{-1}\) is nonzero and does not affect an orthogonality equation. By domain symmetrization, the rows (1) for \(|\alpha|<d\) span the restrictions of all query polynomials of degree below \(d\).

Thus \(w\) has pure high degree at least \(d\) exactly when
\[
 \sum_{h\in{\cal O}} w_h M_{\alpha,h}=0
 \quad\text{for every }|\alpha|<d.
 \tag{2}
\]
The standard approximate-degree dual criterion is:
\[
 \sum_h |w_h|=1,\qquad
 \sum_h w_hF(h)>\epsilon,\qquad
 \text{and (2)}
 \quad\Longrightarrow\quad
 \widetilde{\deg}_\epsilon(F)\ge d.
\]
The finite-band LP uses split variables \(w_h=w_h^+-w_h^-\):
\[
\begin{aligned}
 \text{maximize}\quad&
   \sum_h (w_h^+-w_h^-)F(h)\\
 \text{subject to}\quad&
   \sum_h (w_h^+-w_h^-)M_{\alpha,h}=0
       &&(|\alpha|<d),\\
 & \sum_h(w_h^++w_h^-)\le1,\\
 & w_h^+,w_h^-\ge0.
\end{aligned}
\tag{LP-JH}
\]
At every positive optimum below, the recovered signed weights have exact \(\ell_1\) norm one. Exact substitution verifies every rational moment residual as zero.

The comparison LP is the nested restriction in which weights are constant on the larger \(S_N\times S_q\) classes. Those classes remember only the ordinary multiset \(\{\!\{n_a\}\!\}\), discard which counts are paired by \(\sigma\), and use class-averaged \(F\) and moment rows. It is called the single-histogram LP below.

## 3. P2 preregistration and outcome

The gate was frozen in
[predictions.txt](logs_ksum_L2p1_20260719/predictions.txt) before either optimizer NPZ was opened.

For the saved natural stabilizer block \(A=M_0\), define mass capture by
\[
 \operatorname{cap}(U)=\frac{\|\operatorname{Proj}_U A\|_F^2}{\|A\|_F^2}.
\]
The full space is the exact symmetric \(S_{N-1}\times C(\sigma)\) orbital space: distinguished symbol pair plus the complete remaining-coordinate \(q\times q\) joint count table. The shell coarsening retains only the output-label pair, the centralizer orbit of the distinguished symbol pair, and remaining-coordinate Hamming distance.

Preregistered survival required a full-minus-shell gain of at least 10 percentage points at either point.

| case | shell classes | shell capture | joint classes | joint capture | gain |
|---|---:|---:|---:|---:|---:|
| \((5,4,1)\) | 44 | 72.9572% | 4,108 | 100.0000% | **27.0428 pp** |
| \((7,3,0)\) | 64 | 74.7543% | 6,944 | 100.0000% | **25.2457 pp** |

**Outcome: SURVIVE.** Full capture is expected from commutant membership; the discriminator is the 25–27% mass that is lost under the preregistered shell coarsening. This is direct evidence against empirical collapse to the tested BS-style Hamming-shell resolution.

## 4. P3 exact LP results

The expectation direction was preregistered before solving: joint value at least single value at every point, with a strict gain somewhere. SymPy's exact simplex solver returned rational optima and witnesses. The table gives the optimum correlation at each pure-high-degree band \(d\); bold entries exceed \(1/3\) and therefore certify \(\widetilde{\deg}_{1/3}\ge d\).

| case | \(d\) | single histogram | joint histogram |
|---|---:|---:|---:|
| \((3,3,0)\) | 1 | **2/3** | **1** |
|  | 2 | **2/3** | **1** |
|  | 3 | 1/9 | **1/2** |
| \((4,3,0)\) | 1 | **2/3** | **1** |
|  | 2 | **2/3** | **1** |
|  | 3 | 1/6 | **5/9** |
|  | 4 | 1/6 | **3/8** |
| \((5,4,1)\) | 1 | **1** | **1** |
|  | 2 | **1** | **1** |
|  | 3 | **11/21** | **5/7** |
|  | 4 | **25/63** | **3/5** |
|  | 5 | 1/11 | 1/11 |

Consequently:

| case | known \(OR_{N-1}\) restriction floor | single LP certified degree | joint LP certified degree |
|---|---:|---:|---:|
| \((3,3,0)\) | 2 | 2 | **3** |
| \((4,3,0)\) | 2 | 2 | **4** |
| \((5,4,1)\) | 2 | 4 | **4** |

The restriction floor is checked by exact dual LPs for \(OR_2,OR_3,OR_4\), not by an asymptotic constant hidden in \(\Omega(\sqrt N)\). To obtain the restriction, fix one coordinate to \(a\), restrict every other coordinate to \(a\) or \(\sigma(a)\), and choose \(a\ne\sigma(a)\); 2-Sum becomes \(OR_{N-1}\).

**Second-gate outcome: POSITIVE.** Joint dominates at every tested band and is strict at all bands for the two \(q=3\) points and at \(d=3,4\) for \((5,4,1)\). The exact values also show the limitation: at \((5,4,1)\), both bases fail at \(d=5\), so finite-instance expressiveness is not an asymptotic exponent proof.

## 5. P4 — first asymptotic lemma now owed

**Conjectured joint-histogram witness lemma.** There exist constants
\(\eta>1/6\), \(c_0>0\), and \(\delta>0\) such that, uniformly for
\(3\le q\le N\) and \(t\in\mathbb Z_q\), there is an
\(S_N\times C(\sigma)\)-invariant signed measure
\(\mu_{N,q,t}\) on \((\mathbb Z_q)^N\) satisfying
\[
 \|\mu_{N,q,t}\|_1=1,\qquad
 \langle\mu_{N,q,t},F_{N,q,t}\rangle\ge\frac13+\delta,
\]
and
\[
 \langle\mu_{N,q,t},p\rangle=0
 \quad\text{for every query polynomial }p
 \text{ of degree }<c_0\sqrt N\,q^\eta.
\]
The target value is \(\eta=1/4\). Any fixed \(\eta>1/6\) is already the route's required advance.

### Proof plan only

1. Work in the falling-factorial generators \(P_{u,v},Q_s\), keeping the filtration equal to query degree by the exact symmetrization map (1).
2. Construct a signed finite-band kernel on the pair-count lattice \((i,j)\), then symmetrize it over two-cycles and condition on total occupancy \(N\). The local kernel must distinguish the NO boundary \(ij=0\) from the YES interior \(ij>0\); a scalar total \(i+j\) cannot do this.
3. Use discrete orthogonal polynomials on occupancy slices to annihilate all generator products below degree \(D\). Prove that conditioning on \(\sum_a n_a=N\) preserves the required moment cancellations rather than reintroducing low-degree leakage.
4. Treat fixed points as a separate \(Q_s\) factor and obtain constants uniform in the cycle type \(\tau\); the \(\tau=0\) and \(\tau>0\) cases cannot be identified by target relabeling.
5. Bound the class-weight \(\ell_1\) norm and the signed mass on the YES/NO boundary by a discrete Christoffel-function or extremal-polynomial estimate, aiming for \(D=\Omega(\sqrt N\,q^\eta)\).
6. Lift class weights uniformly to inputs and verify pure high degree against the full one-hot query basis, not only against a chosen generator list.

This lemma is the node's next obligation. No step above has been proved here.

## 6. Reproducibility and limits

- Projection driver: [ksum/tools/ksum_l2p1_projection_test.py](../tools/ksum_l2p1_projection_test.py).
- Exact LP driver: [ksum/tools/ksum_l2p1_exact_moment_lp.py](../tools/ksum_l2p1_exact_moment_lp.py).
- Raw logs and machine-readable outputs:
  [logs_ksum_L2p1_20260719](logs_ksum_L2p1_20260719/).
- Commands and hashes are recorded in that directory's \(COMMANDS.txt\) and \(SHA256SUMS.txt\).

G11 applies throughout. The optimizer projections are numerical structure evidence; the LP optima are exact finite-instance statements. Neither licenses an exponent fit. Optimizer uniqueness, an asymptotic moment-kernel construction, uniform control in \(q,N,\tau\), and independent review were not checked.
