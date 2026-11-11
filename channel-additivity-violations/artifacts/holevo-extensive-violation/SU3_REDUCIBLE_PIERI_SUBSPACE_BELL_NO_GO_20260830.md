# No invariant subspace of a single SU(3) Pieri product has a Bell gap

Date: 2026-08-30

Status: proposer-side all-parameter theorem; independent review pending.

All logarithms are base two.

## Theorem

Let the qutrit output carry the fundamental representation of `SU(3)`, let the environment be an
arbitrary irreducible representation `V_(p,q)`, and let `R` be any invariant subspace of

\[
 3\otimes V_{(p,q)}.
\tag{1}
\]

Restrict the partial trace to `R` to obtain a channel

\[
 \Phi_R:M_{\dim R}\longrightarrow M_3.
\tag{2}
\]

Then its conjugate Bell output obeys

\[
 \boxed{
 2\overline S_{\min}(\Phi_R)
 \le 2S_{\min}(\Phi_R)
 \le S\!\left((\Phi_R\otimes\bar\Phi_R)(\Omega_{\dim R})\right).}
\tag{3}
\]

Consequently, allowing an arbitrary direct sum of irreducible Pieri sectors inside one fixed
irreducible environment does not evade the single-sector no-go.

This theorem does not cover a reducible environment, equivalent environment multiplicities,
noncovariant qutrit Gram factors, or non-Bell collective inputs.

## 1. Reduction to the sum of the two lower branches

The multiplicity-free Pieri decomposition is

\[
 3\otimes V_{(p,q)}
 =V_{(p+1,q)}\oplus V_{(p-1,q+1)}\oplus V_{(p,q-1)},
\tag{4}
\]

with negative labels omitted. Every invariant subspace is therefore a direct sum of a subset of
these three sectors.

The highest sector `V_(p+1,q)` contains a product highest-weight vector. Any invariant subspace
containing that sector has `S_min=0`, and (3) is immediate. A one-sector subspace was classified
in the irreducible Pieri theorem. The only new case is therefore `p,q>=1` and

\[
 R_{\mathrm{low}}
 =V_{(p-1,q+1)}\oplus V_{(p,q-1)}
 =(3\otimes V_{(p,q)})\ominus V_{(p+1,q)}.
\tag{5}
\]

## 2. Exact Gram parameter of the lower direct sum

Let `P_low` be the projector onto (5), `d_low=dim R_low`, and let `X` be any traceless qutrit
matrix with Hilbert--Schmidt norm one. Covariance makes the normalized Gram channel depolarizing:

\[
 \frac3{d_{\mathrm{low}}}\Phi_{\mathrm{low}}\Phi_{\mathrm{low}}^*
 =\Delta_{t_{\mathrm{low}}}.
\tag{6}
\]

The Casimir projector calculation gives

\[
 \boxed{
 t_{\mathrm{low}}(p,q)
 =\frac{(5p+2)q+5p^2+9p-2}
 {8(p+1)(p+q+2)}.}
\tag{7}
\]

One economical derivation uses `P_low=I-P_+`. Decompose `X tensor I` into the high/low block
matrix. Covariance gives

\[
 \operatorname{Tr}\!\left(P_+(X^2\otimes I)\right)=\frac{d_+}{3}.
\tag{8}
\]

The high/high block is the Gram quadratic form of the highest Pieri channel; subtracting its two
equal off-diagonal block norms from
`Tr((X tensor I)^2)=dim V_(p,q)` yields (7). Equivalently, substituting the Lagrange polynomial in
the total quadratic Casimir directly into

\[
 \frac3{d_{\mathrm{low}}}
 \operatorname{Tr}\!\left(
 P_{\mathrm{low}}(X\otimes I)P_{\mathrm{low}}(X\otimes I)
 \right)
\tag{9}
\]

gives the same rational function. The deterministic checker reconstructs all mixed-weight
representations and verifies (7) on every `p,q>=1` with `p+q<=6`.

## 3. An explicit side input is already enough

The middle sector is contained in `R_low`. Its highest-weight input has output spectrum

\[
 \left(\frac p{p+1},\frac1{p+1},0\right).
\tag{10}
\]

Hence an exact upper bound, without needing the global minimum of the reducible channel, is

\[
 S_{\min}(\Phi_{\mathrm{low}})
 \le h_2\!\left(\frac1{p+1}\right).
\tag{11}
\]

The Bell output is the isotropic Choi state of `Delta_(t_low)`. Write its entropy as

\[
 B(t)=H\!\left(
 \frac{1+8t}{9},
 \underbrace{\frac{1-t}{9},\ldots,\frac{1-t}{9}}_{8\text{ times}}
 \right).
\tag{12}
\]

The function `B(t)` is decreasing for `0<=t<=1`.

If `p=1`, (7) gives

\[
 t_{\mathrm{low}}(1,q)
 =\frac{7q+12}{16(q+3)}<\frac7{16},
\tag{13}
\]

while

\[
 B\!\left(\frac7{16}\right)
 =H\!\left(\frac12,\underbrace{\frac1{16},\ldots,\frac1{16}}_{8\text{ times}}\right)
 =\frac52>2
 =2h_2\!\left(\frac12\right).
\tag{14}
\]

If `p>=2`, (7) is increasing in `q` and satisfies

\[
 t_{\mathrm{low}}(p,q)
 <\frac{5p+2}{8(p+1)}<\frac58.
\tag{15}
\]

Therefore

\[
 \begin{aligned}
 B(t_{\mathrm{low}})
 &>B\!\left(\frac58\right)\\
 &=1+h_2\!\left(\frac13\right)\\
 &>2h_2\!\left(\frac13\right)\\
 &\ge 2h_2\!\left(\frac1{p+1}\right).
 \end{aligned}
\tag{16}
\]

Combining (11), (14), and (16) proves (3), strictly for the only new two-sector case.

## 4. Scope and consequence

Together with the single-irrep theorem, this closes every `SU(3)`-invariant input subspace in
`3 tensor V_(p,q)` for one irreducible environment. The remaining covariant route must use a
reducible environment with genuine multiplicity coherence; merely selecting more Pieri sectors
inside one product is not enough.

The result is a route obstruction, not a proof that full-size extensive violation is impossible.
