# Akemann--Ostrand free-generator norm source note

Date: 2026-08-30

## Imported theorem

Let `F_m` be the free group on standard generators `g_1,...,g_m`, let `lambda` be its left-regular
representation, and let `m>=2`. The exact external input used by the Werner return-count argument
is

\[
 \left\|\sum_{v=1}^m\lambda(g_v)\right\|=2\sqrt{m-1}.
\]

## Bibliographic source

C. A. Akemann and P. A. Ostrand, “Computing norms in group C*-algebras,” *American Journal of
Mathematics* **98**(4) (1976), 1015--1047. The imported statement is the paper's norm formula for
the sum of the free generators, specialized to equal coefficients.

## Exact local use

With

\[
 X_m=\sum_v\lambda(g_v),\qquad
 T_m=\sum_{v\ne a}\lambda(g_v^{-1}g_a)=X_m^*X_m-mI,
\]

the spectral inclusion `0<=X_m^*X_m<=4(m-1)I` gives

\[
 \|T_m\|\le\max\{m,|4(m-1)-m|\}=3m-4.
\]

For even `N`, the canonical trace satisfies
`tau(T_m^N)<=||T_m||^N<=(3m-4)^N`. This is the only place where the imported external theorem is
used in the centered Werner moment route.

