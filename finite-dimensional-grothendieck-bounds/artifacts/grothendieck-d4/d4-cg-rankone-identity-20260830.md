# d=4: the exact rank-one CG identity and a support-only no-go theorem

Status: **exact theorem plus exact counterexample**.  The theorem recovers the
factor of about fifteen missing from the full tensor singular-value bound.
The counterexample shows that the last \(0.6\%\) cannot be recovered from the
support split \(217+83\) alone.

The companion checker is
h4_cg_rankone_identity_checker.py.  It does not modify any
canonical node.

## 1. Three CG blocks

Let

\[
 {\cal M}:E\otimes F\longrightarrow\mathbb R^{300},
 \qquad {\cal M}(e\otimes f)=e\circ f,
\]

and let \(G={\cal M}^*{\cal M}\).  The preceding exact tensor calculation
showed that \(G\) has three eigenspaces

\[
 W_{30}\oplus W_{25}\oplus W_9=E\otimes F
\]

with eigenvalues

\[
 \gamma_1<\gamma_2<\gamma_3
\]

and dimensions \(30,25,9\), respectively.  For a pure tensor
\(z=e\otimes f\), write

\[
 w_{30}=\|\Pi_{30}z\|_2^2,\qquad
 w_{25}=\|\Pi_{25}z\|_2^2,\qquad
 w_9=\|\Pi_9z\|_2^2.                                     \tag{1.1}
\]

## 2. Exact pure-tensor identity

### Theorem 2.1

For every \(e\in E\) and \(f\in F\),

\[
 \boxed{\quad
 w_{25}-w_9=\frac14\|e\|_2^2\|f\|_2^2.
 \quad}                                                   \tag{2.1}
\]

Since the three weights sum to
\(L_0=\|e\|_2^2\|f\|_2^2\), there is a single remaining nonnegative
parameter \(r=w_9/L_0\):

\[
 \frac{w_{30}}{L_0}=\frac34-2r,\qquad
 \frac{w_{25}}{L_0}=\frac14+r,\qquad
 \frac{w_9}{L_0}=r.                                      \tag{2.2}
\]

Consequently

\[
\begin{aligned}
\|e\circ f\|_2^2
&=\gamma_1w_{30}+\gamma_2w_{25}+\gamma_3w_9\\
&=c_*L_0+\kappa w_9,                                     \tag{2.3}\\
c_*&=\frac{3\gamma_1+\gamma_2}{4},\\
\kappa&=\gamma_2+\gamma_3-2\gamma_1>0.
\end{aligned}
\]

The exact radical expressions for the three \(\gamma_i\) give

\[
                         \boxed{\quad c_*>\frac1{720}.\quad} \tag{2.4}
\]

Thus

\[
 c_{EF}\ge c_*>\frac1{720},                              \tag{2.5}
\]

improving the full-tensor bound \(c_{EF}>1/11000\) by a factor greater than
\(11000/720>15.27\).

### Exact verification

The projectors onto the three CG blocks are quadratic polynomials in \(G\).
Hence \(w_{25}-w_9-\frac14L_0\) is a biquadratic form on \(E\times F\).
The checker chooses four exact spanning columns of \(E\) and sixteen exact
spanning columns of \(F\), all in
\(\mathbb Q(\sqrt5,\sqrt D)\).  It computes

\[
 L_1=\langle z,Gz\rangle,\qquad
 L_2=\langle z,G^2z\rangle
\]

and the two Lagrange spectral projectors exactly.  Polarization reduces the
identity to

\[
 \binom{4+1}{2}\binom{16+1}{2}=10\cdot136=1360
\]

field coefficients.  Every coefficient is exactly zero.  No numerical
eigenvectors enter the certificate.

This is the rank-one algebraic constraint missed by the smallest singular
value of the unrestricted tensor map.

## 3. Block-weighted complementary-support inequality

For complementary ternary \(p,q\), set

\[
 e=Ep,\quad f=Fq,\quad
 \alpha=\|e\|_2^2,\quad\beta=\|f\|_2^2,
\]

\[
 s=\|p\|_2^2,\quad t=\|q\|_2^2,\quad
 u=s-\alpha,\quad v=t-\beta.
\]

Combining (2.3) with the exact support-localization upper bound gives

\[
\boxed{\quad
 c_*\alpha\beta+\kappa w_9
 \le\frac{\alpha v}{75}+\frac{4\beta u}{75}.
\quad}                                                    \tag{3.1}
\]

Dropping only the nonnegative \(w_9\) term and using \(c_*>1/720\) yields

\[
 \frac{v}{\beta}+4\frac{u}{\alpha}
 >\frac5{48}.                                             \tag{3.2}
\]

Therefore at least one of

\[
 \frac{u}{\alpha}>\frac1{48},\qquad
 \frac{v}{\beta}>\frac1{48},
\]

and hence at least one of

\[
                         u>\frac{s}{49},\qquad
                         v>\frac{t}{49}                   \tag{3.3}
\]

must hold.  Degenerate cases \(\alpha\beta=0\) satisfy (3.3) automatically.

This is the requested support-dependent block-weighted penalty.  It uses the
rank-one CG relation, not a uniform bound on all \(64\)-dimensional tensors.

## 4. Exact comparison at \(217+83\)

Let \(\sigma\) be the residual norm after removing \(E\) and \(F\).  As
before,

\[
 p^TAp-q^TAq
 \le\lambda s+\rho t-(\lambda-\sigma)u-(\rho-\sigma)v.   \tag{4.1}
\]

At \(s=217,t=83\), (3.3) guarantees at least

\[
 \min\left\{
 (\lambda-\sigma)\frac{217}{49},
 (\rho-\sigma)\frac{83}{49}
 \right\}.                                                \tag{4.2}
\]

Using the exact rational lower bounds for the two gaps, the smaller branch is

\[
 \frac{5889155527414333088}{833}
 >7069814558720688.                                      \tag{4.3}
\]

The archived ten-block correction satisfies

\[
 7114830222845879<\Delta_{\rm ten}<7114830222845880.
\]

Exact comparison proves

\[
 0.99\,\Delta_{\rm ten}
 <\frac{5889155527414333088}{833}
 <\Delta_{\rm ten}.                                      \tag{4.4}
\]

Thus the universal pure-tensor identity raises the certified energetic
benchmark from roughly \(6.6\%\) to more than \(99\%\) of the exact target.
It still falls short, so this alone is not the classical upper-bound proof.

## 5. The archived block weights

For the archived equality witness, the checker evaluates the CG projectors
exactly and proves

\[
 \frac1{1500}
 <\frac{w_9}{\alpha\beta}
 <\frac1{1480}.                                          \tag{5.1}
\]

Its numerical annotation is

\[
 \frac{w_9}{\alpha\beta}
 \simeq0.0006730635090345.
\]

By (2.2), the complete normalized weight profile is approximately

\[
 (w_{30},w_{25},w_9)/(\alpha\beta)
 =(0.748653873,\ 0.250673064,\ 0.000673064).              \tag{5.2}
\]

The corresponding effective mixed constant is

\[
 \frac{\|Ep\circ Fq\|_2^2}{\alpha\beta}
 \simeq0.0013985320955267,
\]

slightly above \(c_*\).  This is exactly the small additional invariant
needed after the universal \(>99\%\) result.  However, (5.1) is a fact about
the archived witness, not a uniform theorem for all ternary pairs.

## 6. Exact no-go for support-size-only closure

The checker contains a fully explicit pair

\[
 p,q\in\{-1,0,1\}^{300},\qquad
 |\operatorname{supp}p|=217,\quad
 |\operatorname{supp}q|=83,
\]

with complementary supports and

\[
 \frac{w_9}{\alpha\beta}<\frac1{6000}.                   \tag{6.1}
\]

Its numerical annotation is

\[
 \frac{w_9}{\alpha\beta}
 \simeq0.00014441750341424,
\]

more than four times smaller than the archived value.  The vector is stored
literally in the checker, and (6.1) is verified over the exact biquadratic
field.

Therefore no theorem depending only on the split \(217+83\) can impose the
archived-size \(W_9\) weight needed to supply the final fraction of the
correction.  In particular, the ansatz

\[
 \frac{w_9}{\alpha\beta}\ge\frac1{6000}
\]

is exactly false even at the target support sizes.

## 7. Remaining publishable gate

The \(30/25/9\) CG geometry and its rank-one relation are now closed.  The
remaining task is not another uniform tensor estimate.  It must couple
\(w_9\) to an additional statistic that distinguishes near-extremizers from
arbitrary equal-support ternary pairs.  Plausible choices are:

1. the Bell objective or primary excess itself;
2. the degree-twelve nonradial H4 invariant evaluated on the equal-weight
   atoms;
3. a stability statement showing that any pair with objective near the
   archived value must have \(w_9/(\alpha\beta)\) near (5.1).

The exact counterexample in Section 6 rules out support size as that missing
statistic.  The sharp next claim should therefore be a **near-extremizer
stability inequality**, with (5.1) as its equality-witness benchmark.
