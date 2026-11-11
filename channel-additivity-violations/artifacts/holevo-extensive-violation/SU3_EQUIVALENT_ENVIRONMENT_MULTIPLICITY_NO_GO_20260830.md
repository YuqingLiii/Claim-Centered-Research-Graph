# Repeating one irreducible SU(3) environment does not create a Bell gap

Date: 2026-08-30

Status: proposer-side all-parameter theorem; independent review pending.

All logarithms are base two.

## Theorem

Let the qutrit output carry the fundamental representation of `SU(3)` and let the environment be

\[
 E=V_{(p,q)}\otimes\mathbb C^m,
\tag{1}
\]

where `SU(3)` acts trivially on the multiplicity factor. Let `R` be any invariant subspace of
`3 tensor E`, and restrict the partial trace to `R` to obtain `Phi_R`. Then

\[
 \boxed{
 2\overline S_{\min}(\Phi_R)
 \le2S_{\min}(\Phi_R)
 \le S\!\left((\Phi_R\otimes\bar\Phi_R)(\Omega_{\dim R})\right).}
\tag{2}
\]

Thus arbitrary repetition and partial coherence among copies of one irreducible environment do
not evade the qutrit conjugate-Bell no-go.

This does not yet cover coherent mixtures of *inequivalent* environment irreps, noncovariant
qutrit Gram factors, or non-Bell collective inputs.

## 1. Multiplicity-space normal form

For `p,q>=1`, write the three Pieri sectors as `R_+`, `R_m`, and `R_c`. Every invariant subspace
has the form

\[
 (R_+\otimes L_+)\oplus(R_m\otimes L_m)\oplus(R_c\otimes L_c),
\tag{3}
\]

for multiplicity subspaces `L_j` of `C^m`; absent boundary sectors are omitted. If `L_+` is
nonzero, the product highest-weight vector in `R_+`, tensored with any unit vector in `L_+`, gives
a pure channel output. Hence `S_min=0`.

If only one lower sector occurs, multiplicity merely gives orthogonally flagged copies of the
already classified irreducible channel. Its normalized Gram parameter and minimum output entropy
are unchanged. It remains only to treat nonzero `L_m` and `L_c`.

Put

\[
 r_m=\dim L_m,
 \qquad r_c=\dim L_c,
 \qquad h=\operatorname{Tr}(Q_mQ_c),
\tag{4}
\]

where `Q_m,Q_c` are their orthogonal projectors. Principal angles give

\[
 0\le h\le\min(r_m,r_c).
\tag{5}
\]

## 2. Exact convex Gram reduction

Let `d_m,d_c` be the two Pieri-sector dimensions, and let `t_m,t_c,t_low` be the normalized Gram
parameters of the middle sector, third sector, and their completely coherent direct sum. Expanding
the Hilbert--Schmidt quadratic form over the two representation sectors and tracing the
multiplicity factor gives

\[
 \boxed{
 t=
 \frac{
 h(d_m+d_c)t_{\mathrm{low}}
 +(r_m-h)d_mt_m
 +(r_c-h)d_ct_c}
 {h(d_m+d_c)+(r_m-h)d_m+(r_c-h)d_c}.}
\tag{6}
\]

The coefficient `h` multiplies exactly the cross-sector Hilbert--Schmidt term. Equation (6) is a
convex combination because of (5).

The exact Pieri formulas give two particularly simple differences:

\[
 t_{\mathrm{low}}-t_m
 =\frac{3q(p+q+1)}{8(q+1)(p+q+2)}>0,
\tag{7}
\]

and

\[
 t_{\mathrm{low}}-t_c
 =\frac{3p(q+2)}{8(p+1)(q+1)}>0.
\tag{8}
\]

Therefore

\[
 t\le t_{\mathrm{low}}.
\tag{9}
\]

## 3. Entropy comparison

Because `L_m` is nonzero, choosing a state supported in one middle-sector copy gives

\[
 S_{\min}(\Phi_R)
 \le h_2\!\left(\frac1{p+1}\right).
\tag{10}
\]

The Bell output is the isotropic Choi state of the depolarizing Gram channel. Its entropy `B(t)` is
decreasing in `t`. The invariant-subspace theorem proved

\[
 B(t_{\mathrm{low}})
 >2h_2\!\left(\frac1{p+1}\right).
\tag{11}
\]

Equations (9)--(11) imply

\[
 S\!\left((\Phi_R\otimes\bar\Phi_R)(\Omega)\right)
 =B(t)
 \ge B(t_{\mathrm{low}})
 >2S_{\min}(\Phi_R),
\tag{12}
\]

which proves (2).

## 4. Scope and consequence

This closes every invariant input subspace when the environment is an arbitrary number of
equivalent copies of one irreducible `SU(3)` representation. The remaining covariant qutrit case
must coherently combine inequivalent environment representations that produce a common input
irrep. That is a convex-mixture problem for distinct covariant extreme channels, not an ordinary
Pieri-sector direct sum.
