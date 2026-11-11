# Exact certificate for the 120-line E8 Grothendieck witness

Date: 2026-08-29  
Status: author-level exact proof with two independent local checkers; external adversarial review remains open.

This note is self-contained for the explicitly defined matrix below.  It does not rely on a
stored optimization scalar or on rounded coordinates from an external archive.

## E8-T1. Definitions and theorem

For a real matrix `M` and an integer `d >= 1`, write

\[
 \operatorname{SDP}_d(M)=
 \max_{x_i,y_j\in S^{d-1}}\sum_{i,j}M_{ij}\langle x_i,y_j\rangle .
\]

For `d=1`, the vectors are signs, so

\[
 \operatorname{SDP}_1(M)=
 \max_{\varepsilon,\eta\in\{\pm1\}^m}\varepsilon^T M\eta .
\]

Choose a positive system \(\Phi^+\) of the `E8` root system, with every root normalized to
have squared norm `2`.  The `120` positive roots give one representative from every
antipodal root line.  Enumerate them as \(r_1,\ldots,r_{120}\), put

\[
 R=[r_1\ \cdots\ r_{120}],\qquad G=R^TR,
\]

and define the integral Bell matrix

\[
 \boxed{B=3G-13I_{120}}. \tag{1}
\]

Thus \(B_{ii}=-7\) and \(B_{ij}\in\{-3,0,3\}\) for `i != j`.  Reversing any root-line
representative conjugates `B` by a diagonal sign matrix and does not change either
optimization value.

The exact claim proved here is

\[
 \boxed{\operatorname{SDP}_8(B)=9240,\qquad
        \operatorname{SDP}_1(B)=6104}. \tag{2}
\]

Consequently the real finite-dimensional Grothendieck constant satisfies

\[
 \boxed{K_G(8)\ge\frac{9240}{6104}=\frac{165}{109}}. \tag{3}
\]

If unit line representatives \(u_i=r_i/\sqrt2\) have Gram matrix \(P=G/2\), then

\[
 B=6\left(P-\frac{13}{6}I\right).
\]

This explains the integral normalization but is not used as an external identification
assumption in the proof.

## E8-T2. Tight-frame identity and spectrum

The tensor

\[
 S=\sum_{\alpha\in\Phi(E_8)}\alpha\alpha^T
\]

is Weyl invariant.  The natural real reflection representation of `E8` is irreducible, so
`S` is a scalar multiple of the identity.  Its trace is `240 * 2 = 480`, hence

\[
 S=60I_8.
\]

Each antipodal pair contributes twice the same rank-one tensor.  Therefore

\[
 \boxed{RR^T=30I_8}. \tag{4}
\]

It follows that

\[
 G^2=R^T(RR^T)R=30G,
\]

so `G` has spectrum \(30^{(8)},0^{(112)}\), while `B` has spectrum

\[
 \boxed{77^{(8)},(-13)^{(112)}}. \tag{5}
\]

In particular, \(\|B\|_{\mathrm{op}}=77\).

## E8-T3. Exact vector optimum

Let `X,Y` be matrices whose `120` columns are arbitrary unit vectors.  Then

\[
 \sum_{i,j}B_{ij}\langle x_i,y_j\rangle
 =\langle XB,Y\rangle_F
 \le \|B\|_{\mathrm{op}}\|X\|_F\|Y\|_F
 =77\cdot120=9240. \tag{6}
\]

Take \(x_i=y_i=u_i=r_i/\sqrt2\).  Their correlation matrix is `P=G/2`, and (4) gives

\[
 \operatorname{tr}G=240,
 \qquad
 \operatorname{tr}G^2=30\operatorname{tr}G=7200.
\]

Therefore

\[
 \langle B,P\rangle
 =\frac32\operatorname{tr}G^2-\frac{13}{2}\operatorname{tr}G
 =10800-1560=9240. \tag{7}
\]

This proves the first equality in (2), and in fact proves
\(\operatorname{SDP}_\infty(B)=9240\).

## E8-T4. Classical reduction

Fix signs \(\varepsilon,\eta\in\{\pm1\}^{120}\).  Let

\[
 C=\{i:\eta_i=\varepsilon_i\},\quad
 D=\{i:\eta_i=-\varepsilon_i\},\quad k=|C|,
\]

orient each root line by \(x_i=\varepsilon_i r_i\), and set

\[
 p=\sum_{i\in C}x_i,qquad v=\sum_{i\in D}x_i.
\]

Then

\[
 R\varepsilon=p+v,\qquad R\eta=p-v,
\]

and hence

\[
 \varepsilon^TG\eta=\|p\|^2-\|v\|^2,qquad
 \varepsilon^T\eta=2k-120.
\]

Thus the exact objective is

\[
 \boxed{
 \varepsilon^TB\eta
 =3(\|p\|^2-\|v\|^2)-26k+1560.} \tag{8}
\]

## E8-T5. Signed root sums reduce to upper filters

For `0 <= k <= 120`, define

\[
 F_k=\max_{\substack{T\subseteq\Phi^+\\|T|=k}}
 \left\|\sum_{\alpha\in T}\alpha\right\|^2. \tag{9}
\]

### Lemma

Every sum of `k` oriented distinct root lines has squared norm at most `F_k`.  Moreover a
positive-root subset attaining `F_k` can be chosen to be an upper filter in the root poset.

### Proof

Let \(z=\sum_i x_i\) be a sum of oriented distinct root lines.  Choose a Weyl element `w`
such that \(z'=wz\) is in the closed dominant chamber.  Uniquely write

\[
 wx_i=\sigma_i\beta_i,qquad \sigma_i\in\{\pm1\},\quad\beta_i\in\Phi^+.
\]

The \(\beta_i\) still represent distinct lines.  Dominance gives
\(z'\cdot\beta_i\ge0\) for every positive root, and therefore

\[
 \|z'\|^2
 =z'\cdot\sum_i\sigma_i\beta_i
 \le z'\cdot\sum_i\beta_i
 \le\|z'\|\left\|\sum_i\beta_i\right\|.
\]

After division when \(z'\ne0\), this proves \(\|z\|^2\le F_k\); the zero case is immediate.

Now begin with a positive-root subset attaining `F_k`, move its sum to the dominant
chamber, and reorient the transformed lines positively as above.  Maximality forces equality
in both displayed inequalities.  Equality in Cauchy--Schwarz, together with equality of the
two norms, shows that the reoriented positive-root sum is exactly the dominant transformed
sum.  Thus a maximizer exists whose sum `q` is dominant.

If this maximizer were not an upper filter, there would be
\(\alpha\in T\), \(\beta\notin T\), with \(\alpha<\beta\).  Put
\(\delta=\beta-\alpha\), a nonzero nonnegative integral combination of simple roots.
Dominance gives \(q\cdot\delta\ge0\), while replacing `alpha` by `beta` changes the norm by

\[
 \|q+\delta\|^2-\|q\|^2
 =2q\cdot\delta+\|\delta\|^2>0,
\]

contradicting maximality.  This proves the lemma.

## E8-T6. Exhaustive exact certificate for the envelope

The local certificate computes the complete sequence `F_0,...,F_120` and proves

\[
 \boxed{F_{98}=2366,\qquad F_{104}=2420}, \tag{10}
\]

with

\[
 \boxed{3F_k-26k\le4544\quad(k\ne98,104)}. \tag{11}
\]

The only values above `4544` are

\[
 (k,F_k,3F_k-26k)=(98,2366,4550),(104,2420,4556). \tag{12}
\]

This is not a floating-point search.  Two structurally different exact programs reproduce
the same literal `121`-entry table:

1. `e8_certificate_checker.py` constructs the standard `112+128` ambient roots, changes
   basis over `Fraction`, and enumerates upper filters directly in descending-height order.
   A root may be selected exactly when all strict upper roots have already been selected,
   so every upper filter is reached once and only once.
2. `e8_dual_certificate_checker.py` generates roots by Weyl-reflection closure in simple-root
   coordinates.  It enumerates antichains using comparability masks and takes each
   antichain's upper closure.  Every upper filter has a unique antichain of minimal elements,
   so again every intended object is reached once and only once.

Both enumerate exactly `25080` filters/antichains.  All root coordinates, Cartan products,
norms, and comparisons are integer or rational operations.  The second checker additionally
verifies `RR^T=30I`, `G^2=30G`, the Bell-matrix entries, the vector value, and the equality
witness below.

## E8-T7. The two exceptional cardinalities

Let `L` be the `E8` root lattice.  The Cartan determinant is `1`, hence the root and weight
lattices agree.  Therefore \(\rho\in L\) and

\[
 \sum_{\alpha\in\Phi^+}\alpha=2\rho\in2L.
\]

For every sign vector `s`,

\[
 Rs=2\rho-2\sum_{s_\alpha=-1}\alpha\in2L. \tag{13}
\]

Applying this to `epsilon` and `eta` gives \(p+v,p-v\in2L\).  Since `L` is integral,

\[
 \boxed{\|p\|^2\equiv\|v\|^2\pmod4}. \tag{14}
\]

Since `L` is even, all its squared norms are even integers.

For `k=98`, (10) gives \(\|p\|^2\le2366\).  If the norm is at most `2364`, the desired
bound is immediate.  If it equals `2366`, then (14) forces
\(\|v\|^2\equiv2\pmod4\), hence \(\|v\|^2\ge2\).  In both cases

\[
 \|p\|^2-\|v\|^2\le2364. \tag{15}
\]

For `k=104`, evenness leaves only the following cases above `2416`.  At `2418`, (14)
forces \(\|v\|^2\ge2\).  At `2420`, (14) says \(\|v\|^2\equiv0\pmod4\).  If `v=0`, then
\(p=p+v\in2L\), so \(p=2w\) with `w` in the even lattice `L`; consequently
\(\|p\|^2=4\|w\|^2\) is divisible by `8`, contradicting
\(2420\equiv4\pmod8\).  Thus `v` is nonzero and its norm is at least `4`.  Hence

\[
 \|p\|^2-\|v\|^2\le2416. \tag{16}
\]

## E8-T8. Classical upper bound

For `k` other than `98,104`, combine (8), the signed-sum lemma, and (11):

\[
 \varepsilon^TB\eta
 \le (3F_k-26k)+1560
 \le4544+1560=6104.
\]

For `k=98`, (15) gives

\[
 3(2364)-26(98)+1560=6104.
\]

For `k=104`, (16) gives

\[
 3(2416)-26(104)+1560=6104.
\]

All cardinalities are covered, proving

\[
 \operatorname{SDP}_1(B)\le6104. \tag{17}
\]

## E8-T9. Explicit equality witness

Use the simple roots in the two checkers, whose Dynkin edges are

\[
 1-3,\ 2-4,\ 3-4,\ 4-5,\ 5-6,\ 6-7,\ 7-8.
\]

Delete \(\alpha_3\).  The remaining parabolic subsystem is `A1+A6`, with positive-root
set `D` of size `1+21=22`; its complement `C` has size `98`.  Orient every root of `C`
positively.  The exact simple-root coordinate sums are

\[
 \sum_{\Phi^+}\alpha=(92,136,182,270,220,168,114,58),
\]

\[
 \sum_D\alpha=(1,6,0,10,12,12,10,6),
\]

and hence

\[
 p=\sum_C\alpha=(91,130,182,260,208,156,104,52)=13\omega_3,
\]

where

\[
 \omega_3=(7,10,14,20,16,12,8,4),\qquad
 C\omega_3=e_3,qquad \omega_3^2=14.
\]

Thus

\[
 \boxed{\|p\|^2=13^2\cdot14=2366}. \tag{18}
\]

Keep the isolated `A1` root oriented as \(+\alpha_1\).  Identify the `21` positive `A6`
root lines with the edges of `K_7`.  Orient the edge from `a` to `b` exactly when

\[
 b-a\pmod7\in\{1,2,3\}.
\]

This is a regular tournament: every vertex has indegree and outdegree `3`, so the signed
sum of its \(e_a-e_b\) roots is zero.  The total signed sum on `D` is therefore

\[
 v=\alpha_1,qquad\boxed{\|v\|^2=2}. \tag{19}
\]

Let `epsilon` encode these orientations, and let `eta=epsilon` on `C` and
`eta=-epsilon` on `D`.  Then (8), (18), and (19) give

\[
 \varepsilon^TB\eta
 =3(2366-2)-26(98)+1560
 =6104. \tag{20}
\]

Together with (17), this proves the second equality in (2).

## E8-T10. Explicit state and measurements

The dimension-eight vector strategy has a fully explicit binary-observable realization.
Let `X,Y,Z` be the Pauli matrices and, for `j=1,...,4`, define the eight Hermitian Clifford
generators on \((\mathbb C^2)^{\otimes4}\) by

\[
 \Gamma_{2j-1}=Z^{\otimes(j-1)}\otimes X\otimes I^{\otimes(4-j)},
 \qquad
 \Gamma_{2j}=Z^{\otimes(j-1)}\otimes Y\otimes I^{\otimes(4-j)}.
\]

They satisfy

\[
 \Gamma_a\Gamma_b+\Gamma_b\Gamma_a=2\delta_{ab}I_{16},
 \qquad
 \frac1{16}\operatorname{tr}(\Gamma_a\Gamma_b)=\delta_{ab}.
\]

For \(u_i=r_i/\sqrt2\), Alice measures

\[
 A_i=\Gamma(u_i)=\sum_{a=1}^8(u_i)_a\Gamma_a,
\]

and Bob measures

\[
 B_j^{\mathrm{obs}}=\Gamma(u_j)^T.
\]

Both are Hermitian involutions and therefore have outcomes `+1,-1`.  On the maximally
entangled state

\[
 |\Phi_{16}\rangle=\frac14\sum_{t=0}^{15}|t,t\rangle,
\]

the correlator is

\[
 \langle\Phi_{16}|A_i\otimes B_j^{\mathrm{obs}}|\Phi_{16}\rangle
 =\frac1{16}\operatorname{tr}(\Gamma(u_i)\Gamma(u_j))
 =u_i\cdot u_j=\frac12G_{ij}. \tag{21}
\]

Thus these `120+120` explicit observables attain the Bell value `9240` on local Hilbert
space dimension `16`.

## E8-T11. Reproduction commands and evidence boundary

Run from the repository root:

```text
python3 grothendieck-e8/tools/e8_certificate_checker.py
python3 grothendieck-e8/tools/e8_dual_certificate_checker.py
```

The preserved joint output and SHA-256 digests are in
`grothendieck-e8/artifacts/e8-dual-checker-run-20260829.txt`.

The exact theorem for the matrix (1), its equality witness, and its physical realization are
closed at author level.  The remaining gates before a `PROVED` label are independent
adversarial review of the proof/checkers and a separate primary-source audit if the matrix is
to be advertised as identical to a particular previously archived candidate.

