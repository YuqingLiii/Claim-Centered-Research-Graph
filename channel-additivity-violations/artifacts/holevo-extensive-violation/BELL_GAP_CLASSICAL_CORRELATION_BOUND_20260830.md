# Bell-certificate gap is bounded by hidden versus locally accessible correlation

Date: 2026-08-30

Status: proposer-side elementary theorem; independent review pending.

All logarithms are base two.

## Statement

Let `Phi:M_d->M_k` be a finite channel satisfying

\[
 \Phi(I_d/d)=I_k/k,
\tag{1}
\]

and let

\[
 Z_{AB}=(\Phi\otimes\bar\Phi)(\Omega_d).
\tag{2}
\]

Both marginals of `Z` are maximally mixed. Define the one-way classical correlation

\[
 J_{A\to B}(Z)=\sup_{\{E_x\}} I(X:B)_{(\mathcal M\otimes\mathrm{id})(Z)},
\tag{3}
\]

where the supremum is over finite POVMs on `A`. Then the minimum-output-entropy defect certified
by the Bell input obeys

\[
 \boxed{
 2S_{\min}(\Phi)-S(Z)
 \le I(A:B)_Z-2J_{A\to B}(Z).}
\tag{4}
\]

In particular, a positive extensive Bell certificate requires the Bell output to contain total
mutual information that exceeds twice its maximum one-way measurement-accessible classical
correlation by an extensive amount.

## 1. Every conditional state is a legal conjugate-channel output

For a POVM `{E_x}` on the first output, the unnormalized conditional state on the second output is

\[
 p_x\tau_x
 =\frac1d\bar\Phi\!\left((\Phi^*(E_x))^T\right).
\tag{5}
\]

The operator in parentheses is positive. After division by its trace it is a density matrix, so
every `tau_x` with `p_x>0` is a genuine output of `bar(Phi)`. Conjugation preserves minimum output
entropy, hence

\[
 S_{\min}(\Phi)=S_{\min}(\bar\Phi)
 \le\sum_xp_xS(\tau_x)=S(B|X).
\tag{6}
\]

No assertion is made that the conditional input is pure; the minimum over all inputs is no larger
than the entropy of any such mixed-input output.

## 2. Mutual-information form

Condition (1) gives `S(A)=S(B)=log k`. For the measured classical-quantum state,

\[
 S(B|X)=S(B)-I(X:B)=\log k-I(X:B).
\tag{7}
\]

Also

\[
 S(Z)=2\log k-I(A:B)_Z.
\tag{8}
\]

Using (6)--(8), for every POVM,

\[
\begin{aligned}
 2S_{\min}(\Phi)-S(Z)
 &\le2S(B|X)-S(Z)\\
 &=I(A:B)_Z-2I(X:B).
\end{aligned}
\tag{9}
\]

Take the infimum of the right-hand side over POVMs, equivalently subtract twice the supremum in
(3), to obtain (4).

## 3. Recovery of the isotropic one-bit cap

For an isotropic state with spectrum `(alpha,beta,...,beta)`, a rank-one basis measurement gives
the conditional spike spectrum derived in `ISOTROPIC_BELL_ONE_BIT_CAP_20260830.md`. Substituting
that measurement into (9) gives exactly the scalar expression bounded there by one bit. Thus the
isotropic theorem is a sharp specialized entropy estimate inside the more general correlation
bound.

## 4. Products of isotropic layers

Let `Z=Z_1 tensor ... tensor Z_J`. Mutual information is additive, while product POVMs imply

\[
 J_{A\to B}(Z)\ge\sum_{j=1}^J J_{A_j\to B_j}(Z_j).
\tag{10}
\]

Therefore

\[
 I(A:B)_Z-2J_{A\to B}(Z)
 \le\sum_{j=1}^J\left[I(A_j:B_j)_{Z_j}-2J_{A_j\to B_j}(Z_j)\right].
\tag{11}
\]

If every factor is isotropic, the right-hand side is at most `J` bits. A tensor product of
isotropic states is generally not itself isotropic, but it still cannot beat the sum of the
one-layer caps.

This is compatible with absolute-unbounded gaps obtained by increasing `J`; it prevents one
isotropic layer from secretly contributing a growing number of bits.

## 5. Research consequence

Equation (4) supplies a necessary condition for a genuinely non-isotropic extensive Bell route:
construct Bell outputs with

\[
 I(A:B)-2J_{A\to B}=\Omega(\text{full logarithmic size}),
\tag{12}
\]

and simultaneously prove global one-channel minimum-output-entropy lower bounds. States with
large total correlation but small locally accessible classical correlation are data-hiding or
locking-like candidates. The correlation property alone is not sufficient: the state must arise
from the same finite channel whose entire output set obeys the required side bound.

## Scope

- The maximally mixed marginal condition (1) is essential to the displayed mutual-information
  simplification. Random-unitary channels satisfy it.
- The theorem bounds the maximally-entangled-input certificate, not the globally optimized joint
  minimum output entropy from an arbitrary non-Bell input.
- It is a necessary-condition and routing theorem, not a construction of an extensive violation.
