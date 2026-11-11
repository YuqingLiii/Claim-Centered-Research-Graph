# d=4: an exact tensor lower bound for complementary spectral leakage

Status: **proved exact strengthening, still insufficient for the full
classical upper bound**.  This note turns the qualitative no-zero-divisor
statement for the top rank-four eigenspace \(E\) and bottom rank-sixteen
eigenspace \(F\) into an explicit global constant.  It also removes the loose
\(\|a\circ b\|_2\) term from the previous complementary-support inequality.

The companion exact checker is
h4_ef_tensor_bound_checker.py.  No canonical YAML, index, or
graph file is modified.

## 1. The full tensor map is injective

Choose orthonormal basis matrices

\[
 U\in\mathbb R^{300\times4},\qquad
 V\in\mathbb R^{300\times16},
\]

so that \(E=UU^T\) and \(F=VV^T\).  Define

\[
 {\cal M}:E\otimes F\longrightarrow\mathbb R^{300},
 \qquad {\cal M}(e\otimes f)=e\circ f.                    \tag{1.1}
\]

In the tensor-product bases, row \(i\) of \({\cal M}\) is
\(U_{i,*}\otimes V_{i,*}\).  Consequently

\[
 {\cal M}{\cal M}^T=E\circ F=:H.                         \tag{1.2}
\]

Thus the nonzero eigenvalues of the \(300\times300\) Hadamard product \(H\)
are the squared singular values of the \(300\times64\) tensor map.

### Theorem 1.1 (exact)

The map \({\cal M}\) has rank \(64\).  The nonzero spectrum of \(H\) consists
of three positive eigenvalues

\[
 \gamma_1<\gamma_2<\gamma_3
\]

with respective multiplicities

\[
                         30,\quad25,\quad9.               \tag{1.3}
\]

Numerically, only for readability,

\[
\begin{aligned}
\gamma_1&\simeq0.0000931563734367905916,\\
\gamma_2&\simeq0.00527743950927125898,\\
\gamma_3&\simeq0.00873362826649423790.
\end{aligned}                                             \tag{1.4}
\]

Put

\[
 D=27825235685041889271593617164468.
\]

The smallest eigenvalue has the exact radical expression

\[
\begin{aligned}
\gamma_1={}&\frac1{375}
-\frac{220524777030959\sqrt{5D}}
 {1159384820210078719649734048519500}\\
&-\frac{435142604279029\sqrt D}
 {6956308921260472317898404291117000}.
\end{aligned}                                             \tag{1.5}
\]

Exact algebraic comparison gives

\[
                 \boxed{\quad
 \frac1{11000}<\gamma_1<\frac1{10700}.\quad}              \tag{1.6}
\]

### Certificate construction

Let \(Q\) be the rational projector onto the two roots of

\[
 f_4(t)=t^2+6416438611362062t
       +3336362192084004310572308931844.
\]

The bottom projector is

\[
 F=\frac12Q-
 \frac{A+(6416438611362062/2)I}{\sqrt D}\,Q.              \tag{1.7}
\]

The checker computes the first column of \(Q\) exactly as a degree-eleven
rational polynomial in the integer matrix \(A\).  Since

\[
 E=\frac{X+Y\sqrt5}{600},
\]

the first row of \(H=E\circ F\) lies in the biquadratic field
\(\mathbb Q(\sqrt5,\sqrt D)\).  Ordinary H4 permutation invariance
reconstructs the entire matrix from that row.

Six exact trace moments produce a cubic recurrence for the three nonzero
eigenvalues.  The checker verifies

\[
 H(H-\gamma_1I)(H-\gamma_2I)(H-\gamma_3I)e_0=0.          \tag{1.8}
\]

Because \(H\) commutes with the transitive H4 permutation action, (1.8)
propagates from \(e_0\) to every coordinate vector.  Exact factorization over
\(\mathbb Q(\sqrt5,\sqrt D)\) gives the three linear factors.  Finally the
first three trace moments certify the multiplicities \(30,25,9\), whose sum
is \(64\).  This is an exact H4/Clebsch--Gordan block decomposition, not a
floating-point SVD.

## 2. Explicit lower bound for \(c_{EF}\)

Recall

\[
 c_{EF}=\min_{\substack{e\in E,\ f\in F\\
                        \|e\|_2=\|f\|_2=1}}
                   \|e\circ f\|_2^2.
\]

For unit \(e,f\), the tensor \(e\otimes f\) is a unit vector in
\(E\otimes F\).  Theorem 1.1 therefore gives

\[
             \|e\circ f\|_2^2
 =\|{\cal M}(e\otimes f)\|_2^2\ge\gamma_1.
\]

Hence

\[
             \boxed{\quad c_{EF}\ge\gamma_1>\frac1{11000}.\quad} \tag{2.1}
\]

This is stronger than the preceding no-zero-divisor result: it proves that
the linear map on the entire \(64\)-dimensional tensor product is injective,
not merely that its rank-one cone avoids the kernel.

The inequality in (2.1) need not be sharp for rank-one tensors.  A numerical
rank-one search had suggested \(c_{EF}\) is substantially larger; that
observation is not used anywhere in this certificate.

## 3. Removing the \(\|a\circ b\|_2\) loss

Let \(p,q\in\{-1,0,1\}^{300}\) have complementary supports and put

\[
 s=\|p\|_2^2,\qquad t=\|q\|_2^2=300-s,
\]

\[
 \alpha=p^TEp,\qquad\beta=q^TFq,\qquad
 u=s-\alpha,\quad v=t-\beta.                             \tag{3.1}
\]

### Theorem 3.1 (exact complementary-support inequality)

\[
\boxed{\quad
 \gamma_1\alpha\beta
 \le\frac{\alpha v}{75}+\frac{4\beta u}{75}.
\quad}                                                    \tag{3.2}
\]

Consequently, whenever \(\alpha\beta>0\),

\[
 \frac{v}{\beta}+4\frac{u}{\alpha}
 \ge75\gamma_1>\frac3{440}.                              \tag{3.3}
\]

In particular, at least one of

\[
 \frac{u}{\alpha}>\frac3{2200},\qquad
 \frac{v}{\beta}>\frac3{2200}                            \tag{3.4}
\]

must hold.  Equivalently, at least one absolute leakage satisfies

\[
 u>\frac{3s}{2203},\qquad v>\frac{3t}{2203}.              \tag{3.5}
\]

If \(\alpha\beta=0\), one of \(u=s\) or \(v=t\), so the corresponding
conclusion in (3.5) is automatic.

### Proof

Let \(S=\operatorname{supp}p\) and \(T=\operatorname{supp}q=S^c\).  Set
\(e=Ep\), \(f=Fq\), \(a=p-e\), and \(b=q-f\).  On \(S\), \(q=0\), hence
\(f=-b\); on \(T\), \(p=0\), hence \(e=-a\).  Therefore

\[
\begin{aligned}
\|e\circ f\|_2^2
&=\sum_{i\in S}e_i^2f_i^2+\sum_{i\in T}e_i^2f_i^2\\
&\le\|e\|_\infty^2\|f_S\|_2^2
   +\|f\|_\infty^2\|e_T\|_2^2.
\end{aligned}
\]

Since \(\|f_S\|_2\le\|b\|_2=\sqrt v\) and
\(\|e_T\|_2\le\|a\|_2=\sqrt u\), while signed-H4 transitivity gives

\[
 \|e\|_\infty^2\le\frac{\alpha}{75},\qquad
 \|f\|_\infty^2\le\frac{4\beta}{75},
\]

the desired upper bound follows.  The tensor lower bound is
\(\|e\circ f\|_2^2\ge\gamma_1\alpha\beta\), proving (3.2).
Equations (3.3)--(3.5) are elementary rearrangements.

This is strictly stronger than the earlier triangle-inequality estimate: the
mixed remainder \(\|a\circ b\|_2\) disappears completely.

## 4. Comparison with the exact correction threshold

Let \(\sigma\) denote the norm of the remaining spectrum after removing
\(E\) and \(F\).  Spectral decomposition gives

\[
 p^TAp-q^TAq
 \le \lambda s+\rho t-(\lambda-\sigma)u-(\rho-\sigma)v.  \tag{4.1}
\]

At the archived support split \(s=217,t=83\), (3.5) forces a primary spectral
penalty of at least

\[
 \min\left\{
 (\lambda-\sigma)\frac{3\cdot217}{2203},
 (\rho-\sigma)\frac{3\cdot83}{2203}
 \right\}.                                                \tag{4.2}
\]

Using only the exact rational isolating bounds

\[
 \sqrt5>\frac{559}{250},\qquad
 \rho>\frac{11691401709341221}{2},\qquad
 \sigma<\frac{56846466952431285}{34},
\]

the smaller branch in (4.2) is certified to exceed

\[
 \frac{17667466582242999264}{37451}
 >471748860704467.                                       \tag{4.3}
\]

The previously isolated ten-block correction lies in

\[
 7114830222845879<\Delta_{\rm ten}<7114830222845880.      \tag{4.4}
\]

Exact rational comparison yields

\[
 \frac1{16}
 <\frac{17667466582242999264/37451}{\Delta_{\rm ten}}
 <\frac1{15}.                                             \tag{4.5}
\]

Thus the new tensor certificate supplies a universal penalty on the correct
scale, but only guarantees between \(6.25\%\) and \(6.67\%\) of the exact
remaining correction threshold.  It does not close the archived equality
case, much less the global classical upper bound.

For a second diagnostic, substituting the archived projector energies into
(3.2) gives a certified lower side near \(0.94\) using \(1/11000\), whereas
the elementary support upper side is about \(192.92\).  The remaining factor
of roughly \(205\) is therefore in the support-localization estimate, not in
the existence of an explicit tensor singular-value bound.

## 5. Precise next gate

The tensor/CG part is now exact and closed.  Further progress must exploit
that \(e=Ep\) and \(f=Fq\) arise from **equal-weight ternary atoms**, not
arbitrary vectors of \(E\) and \(F\).  Two concrete routes remain:

1. Refine
   \(\|f_S\|_2^2\le v\) and \(\|e_T\|_2^2\le u\) using the signed orbit
   equations for \(p\) and \(q\).  A factor of at least \(15\) in the
   resulting energetic guarantee is needed at the archived split.
2. Decompose the three exact CG blocks of \(H=E\circ F\) against the
   degree-twelve nonradial H4 invariant.  The target is a lower bound on
   \(\|Ep\circ Fq\|_2^2\) specific to complementary equal-weight atoms,
   rather than all unit tensors.

Any next claim should be measured against the exact number in (4.4).  Merely
improving the decimal approximation of \(c_{EF}\) cannot by itself close the
remaining gap.
