# Sharp-superlevel reduction on the fixed (217+83) cell

**Status.**  Exact SOS reduction plus complete exact orbit-shell closure
through Hamming radius three.  The global implication

\[
 B\ge C\Longrightarrow r\ge r_{\rm crit}
\]

is not proved here.  No (B\ge C) counterexample is found.  The result
eliminates the full (q)-sign cell of size (2^{83}) as an independent
source of Bell improvement and reduces the remaining sharp-superlevel
problem to a 217-variable Boolean cut inequality.

Replay checker:

```
grothendieck-d4/tools/h4_superlevel_cell_reduction_checker.py
```

Every decisive calculation uses integers or rational arithmetic.  The
checker reconstructs an exact (82\times82) (LDL^T) factorization and
enumerates (4{,}500{,}250) points in the first three nontrivial shells.

## 1. The two pseudo-Boolean polynomials

Let (P=\operatorname{supp}p), (Q=\operatorname{supp}q), with
(|P|=217,|Q|=83).  Introduce flip variables

\[
 z_i\in\{0,1\},\qquad i=0,\ldots,299,
\]

and flip the archived sign on coordinate (i) exactly when (z_i=1).
The exact Bell deficit is the degree-two pseudo-Boolean polynomial

\[
 D(z)=C-B(z)=\sum_i g_i z_i+
             \sum_{i<j}h_{ij}z_i z_j,                    \tag{1.1}
\]

where

\[
 g_i=
 \begin{cases}
 4p_i(Ap)_i-4A_{ii},&i\in P,\\
 -4q_i(Aq)_i+4A_{ii},&i\in Q,
 \end{cases}                                             \tag{1.2}
\]

and

\[
 h_{ij}=
 \begin{cases}
 -8p_ip_jA_{ij},&i,j\in P,\\
  8q_iq_jA_{ij},&i,j\in Q,\\
 0,&i\in P,j\in Q.
 \end{cases}                                             \tag{1.3}
\]

Thus the fixed-support Bell problem splits exactly into two uncoupled Ising
quadratics.

The CG closure statistic can also be written without a ratio.  Put

\[
 Z(p,q)=Ep\circ Fq,
\]

and let (Pi_9) be the exact nine-dimensional spectral projector of
(H=E\circ F).  Define

\[
 \mathcal W(p,q)=
 Z(p,q)^T\Pi_9Z(p,q)
 -r_{\rm crit}(p^TEp)(q^TFq).                             \tag{1.4}
\]

Since (Ep) and (Fq) are linear, (1.4) is a bidegree-((2,2)), total
degree-four pseudo-Boolean polynomial over the exact biquadratic field.  It
is invariant under the simultaneous signed (H_4) action.  For
(alpha\beta>0),

\[
 \mathcal W\ge0
 \quad\Longleftrightarrow\quad
 \frac{w_9}{\alpha\beta}\ge r_{\rm crit}.                \tag{1.5}
\]

The desired sharp statement on this cell is therefore the finite
semialgebraic implication

\[
 D(z)\le0\quad\Longrightarrow\quad\mathcal W(z)\ge0.     \tag{1.6}
\]

Both polynomials have degree at most four, hence lie well below the allowed
degree-twelve ceiling.

## 2. An exact SOS for the whole (q) cell

Gauge the (83\times83) (q)-principal matrix by the archived signs:

\[
 N=\operatorname{diag}(q_Q)A_{QQ}\operatorname{diag}(q_Q),
 \qquad
 L_Q=\operatorname{diag}(N\mathbf1)-N.                   \tag{2.1}
\]

For any (t\in\{\pm1\}^{83}), the corresponding sign vector
(q'=\operatorname{diag}(q_Q)t) satisfies

\[
 q'^TAq'-q^TAq=-t^TL_Qt.                                 \tag{2.2}
\]

The checker deletes one row and column from (-L_Q) and computes, over the
rationals,

\[
 (-L_Q)_{[82]}=R\Delta R^T,                              \tag{2.3}
\]

where (R) is unit lower triangular and all 82 diagonal entries of
(Delta) are strictly positive.  It multiplies the factors back and checks
every entry of (2.3).  Since (L_Q\mathbf1=0), this proves

\[
 -L_Q\succeq0,
 \qquad
 \ker(-L_Q)=\operatorname{span}\{\mathbf1\}.             \tag{2.4}
\]

Equations (2.2)--(2.4) give the exact SOS

\[
 \boxed{q'^TAq'\ge q^TAqquad
        \text{for every one of the }2^{83}\text{ sign choices on }Q.} \tag{2.5}
\]

Equality occurs only for (q'=q) or (q'=-q).  This is a global theorem,
not a neighborhood computation.

## 3. Sharp-superlevel consequence

Write (p',q') for an arbitrary pair in the fixed support cell.  From
(2.5),

\[
 B(p',q')-C
 =\bigl(p'^TAp'-p^TAp\bigr)
  -\bigl(q'^TAq'-q^TAq\bigr)
 \le p'^TAp'-p^TAp.                                     \tag{3.1}
\]

Therefore

\[
 \boxed{B(p',q')\ge C\Longrightarrow p'^TAp'\ge p^TAp.} \tag{3.2}
\]

The only remaining source of a fixed-cell superlevel competitor is a cut of
the 217-coordinate (p)-matrix.  In the archived gauge, define

\[
 M=\operatorname{diag}(p_P)A_{PP}\operatorname{diag}(p_P),
 \qquad L_P=\operatorname{diag}(M\mathbf1)-M.             \tag{3.3}
\]

For a sign vector (s\in\{\pm1\}^{217}), the missing fixed-cell gate is

\[
 s^TL_Ps\ge0.                                            \tag{3.4}
\]

Unlike the (q) block, (L_P) is not positive semidefinite over the reals;
the checker gives a 19-sparse integer vector (v) with

\[
 v^TL_Pv=-1160483848923607<0.                             \tag{3.5}
\]

Therefore the same quadratic SOS ansatz cannot prove (3.4).  This is an
exactly localized Boolean-copositivity/cut-cone problem, rather than another
two-party search.

## 4. Exact (H_4)-stabilizer and discrete tangents

The checker reconstructs all 14,400 signed (H_4) elements and finds that
the stabilizer of the archived pair ((p,q)) has order six.

### Radius one

The 300 flips form 67 exact stabilizer orbits, with orbit-size census

\[
 37\cdot6+24\cdot3+6\cdot1=300.                          \tag{4.1}
\]

The minimum deficit is

\[
 d_1=2353967343413440,                                   \tag{4.2}
\]

attained by the six-element orbit

\[
 \{46,56,85,99,131,148\}.                               \tag{4.3}
\]

### Radius two

The 44,850 pairs form 7,765 exact stabilizer orbits, with census

\[
 7195\cdot6+555\cdot3+15\cdot1=44850.                   \tag{4.4}
\]

Every orbit has positive deficit.  The minimum is

\[
 d_2=3299723804685584,                                   \tag{4.5}
\]

attained at

\[
 (46,148),\quad(56,131),\quad(85,99).                   \tag{4.6}
\]

### Radius three

The checker evaluates all

\[
 \binom{300}{3}=4455100
\]

triples by exact integer arithmetic.  Every triple has positive deficit.
The minimum is

\[
 d_3=4073853755325552,                                   \tag{4.7}
\]

attained at

\[
 (46,99,131),\qquad(56,85,148).                         \tag{4.8}
\]

Consequently the superlevel set (B\ge C) contains no nontrivial point
through Hamming radius three.  This closes a complete new flip layer, not a
sample of that layer.

## 5. A structural no-go for a “second (H)-moment”

For a rank-one tensor (e\otimes f), the preceding exact CG identities give

\[
 w_{30}+w_{25}+w_9=\alpha\beta,
 \qquad
 w_{25}-w_9=\frac14\alpha\beta.                          \tag{5.1}
\]

Hence every quadratic statistic of the form

\[
 Z^T\phi(H)Z
\]

is an affine combination of (alpha\beta) and (w_9).  It cannot supply a
second independent nonradial statistic.  Therefore a successful
degree-twelve strengthening must use another CG channel or a genuinely
different (H_4)-invariant tensor, not merely a higher polynomial moment of
(H=E\circ F).

## 6. Remaining publishable gate

This round reduces the fixed-cell theorem to the following exact statement:

> **217-cut gate.**  Prove (s^TL_Ps\ge0) for every
> (s\in\{\pm1\}^{217}), or exhibit a sign vector with negative value.

If the gate holds, (3.1) proves (B\le C) throughout the entire
(217+83) support cell, making the (W_9) implication vacuous except at its
equality set.  If it fails, the violating (p'), together with (q'=q), is
an exact (B>C) counterexample to the archived classical candidate.

The exact shell results show that any such counterexample must have Hamming
distance at least four from both ((p,q)) and its global sign equivalent.
The next appropriate certificate is thus a Boolean cut-cone/SOS certificate
for (3.4), not a wider objective-neighborhood estimate.
