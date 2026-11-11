# Atomic product-Haar theorem for unbounded p=1 MOE pair gaps

Date: 2026-08-30

Status: historical proposer-side exact-repair snapshot. This artifact isolates only the
minimum-output von Neumann entropy statement. It does not assert a Holevo transfer or a
same-channel reduction. The canonical atom was subsequently promoted to `PROVED` after fresh
independent hash-bound review; this file is not an authoritative status store.

All logarithms below are base two. The Hilbert--Schmidt norm is denoted by `||.||_2`.

## 1. Atomic theorem

Fix an integer `m>e^18` and set

\[
 c_m={\log_2m\over m}-2\log_2(1+9/m)>0.
\]

For fixed depth `J>=1` and per-leg dimension `D`, draw independent Haar unitaries

\[
 U_{i,j}^{(D)}\in U(D),\qquad i\in[m],\quad j\in[J],
\]

and define

\[
 \Phi_{j,D}(\rho)={1\over m}\sum_{i=1}^m
 U_{i,j}^{(D)}\rho U_{i,j}^{(D)*},
 \qquad
 L_{J,D}=\bigotimes_{j=1}^J\Phi_{j,D}.
\]

Let `bar(L_(J,D))` be the entrywise-conjugate channel in the basis used to sample the unitaries,
and define the `p=1` MOE pair defect

\[
 \Delta_{J,D}=S_{\min}(L_{J,D})+S_{\min}(\bar L_{J,D})
 -S_{\min}(L_{J,D}\otimes\bar L_{J,D}).
\]

The atomic claim is

\[
 \lim_{D\to\infty}
 \Pr\{\Delta_{J,D}\ge Jc_m/2\}=1
 \qquad\text{for every fixed }J\ge1.                 \tag{1}
\]

Consequently, for every `G>0`, choose a fixed integer `J>2G/c_m`; then

\[
 \lim_{D\to\infty}\Pr\{\Delta_{J,D}>G\}=1.          \tag{2}
\]

The order is fixed `m`, then prescribed `G`, then fixed `J`, and only then `D->infinity`.

## 2. Exact Collins--Youn theorem interface

Theorem 3.3 of Collins--Youn uses the direct product of `J` copies of `F_infinity`. Restrict in
each factor to its first `m` free generators. For `v=(v_1,...,v_J) in [m]^J`, write `u_v` for the
corresponding product generator in the left regular representation. If
`a=(a_(v,w)) in M_(m^J)(C)` has ordinary matrix trace zero, then

\[
 \left\|\sum_{v,w\in[m]^J}a_{v,w}u_v^*u_w\right\|
 \le m^{J/2}\sqrt{(1+9/m)^J-1}\,\|a\|_2.             \tag{3}
\]

Here the norm on the left is the operator norm in the reduced group `C*`-algebra, and

\[
 \|a\|_2=(\operatorname{Tr}a^*a)^{1/2}.
\]

This is the exact specialization `N=m`, `k=J` of the source theorem. The trace-zero coefficient
space, both norms, direct-product representation, and constant are all load-bearing.

Local source:
`artifacts/primary-sources/collins-youn-1907.07856.pdf`, Theorem 3.3, PDF pp. 11--12.

## 3. Exact Bordenave--Collins theorem interface

For fixed integers `m>=2` and `J>=1`, let the `U_(i,j)^(D)` above be independent Haar matrices and
embed them on separate tensor legs by

\[
 V_{i,j}^{(D)}=I_D^{\otimes(j-1)}\otimes U_{i,j}^{(D)}
 \otimes I_D^{\otimes(J-j)}.                          \tag{4}
\]

Bordenave--Collins Eq. (69) and Theorem 9.2 state that, as `D->infinity`, the fixed tuple
`(V_(i,j)^(D))_(i,j)` converges strongly in probability to the left-regular generators
`(lambda(g_(i,j)))_(i,j)` of the direct product `F_m^J`. In the norm-convergence interface used
here, for every fixed matrix size and every fixed matrix-valued noncommutative star-polynomial
`P`,

\[
 \|P((V_{i,j}^{(D)})_{i,j})\|
 \longrightarrow
 \|P((\lambda(g_{i,j}))_{i,j})\|
 \quad\text{in probability}.                         \tag{5}
\]

The scalar case already suffices below. The generator count `m`, leg count `J`, polynomial, and
all of its coefficients are fixed before `D` tends to infinity.

Local source:
`artifacts/primary-sources/bordenave-collins-2304.05714.pdf`, strong-convergence definition and
matrix linearization in Section 9.1, Eqs. (66)--(68), PDF pp. 60--61; tensor-leg model Eq. (69)
and Theorem 9.2, PDF pp. 62--63.

## 4. Uniform coefficient event

Put `q=m^J` and, for `v in [m]^J`,

\[
 W_v=\bigotimes_{j=1}^J U_{v_j,j}^{(D)}.
\]

For a traceless coefficient matrix `a in M_q(C)`, define

\[
 T_D(a)=\sum_{v,w}a_{v,w}W_v^*W_w,
 \qquad
 T_\infty(a)=\sum_{v,w}a_{v,w}u_v^*u_w.
\]

For either map,

\[
 |\|T(a)\|-\|T(b)\||
 \le\sum_{v,w}|a_{v,w}-b_{v,w}|
 \le q\|a-b\|_2.                                    \tag{6}
\]

Fix `eta>0`. The traceless Hilbert--Schmidt unit sphere in `M_q(C)` has a finite net because
`m,J` are fixed. Apply (5) to the fixed polynomial associated with every net point, take a finite
union of failure events, use (3), and extend by (6). This gives one event `E_(D,eta)` with

\[
 \Pr(E_{D,\eta})\longrightarrow1                    \tag{7}
\]

on which

\[
 \|T_D(a)\|_\infty
 \le(1+\eta)m^{J/2}\sqrt{(1+9/m)^J-1}\,\|a\|_2     \tag{8}
\]

simultaneously for every traceless complex `a`. The net is selected after fixed `m,J,eta` and
before the sampled channel or any optimizing input.

## 5. Global side-entropy lower bound

A complementary channel of `L_(J,D)` has the coefficient form

\[
 L_{J,D}^c(S)_{v,w}=q^{-1}\operatorname{Tr}(W_vSW_w^*).
\]

Its diagonal is `1/q`. For any input state `S`, put

\[
 X=L_{J,D}^c(S)-I_q/q.
\]

Then `X` is Hermitian and traceless. On the simultaneous event (8), with

\[
 K_{m,J}=m^{J/2}\sqrt{(1+9/m)^J-1},
\]

duality gives

\[
 \|X\|_2^2
 =\operatorname{Tr}(S(L_{J,D}^c)^*(X))
 \le q^{-1}(1+\eta)K_{m,J}\|X\|_2.
\]

The zero case is immediate; otherwise divide by `||X||_2`. Therefore

\[
 \operatorname{Tr}(L_{J,D}^c(S)^2)
 \le q^{-1}\left[1+(1+\eta)^2((1+9/m)^J-1)\right].   \tag{9}
\]

Von Neumann entropy dominates Renyi-2 entropy. Minimum output entropy is attained on a pure input,
and a channel and its complement have the same nonzero output spectrum on pure inputs. Hence,
uniformly over all inputs and on the same event,

\[
 S_{\min}(L_{J,D})
 \ge J\log_2m
 -\log_2\left[1+(1+\eta)^2((1+9/m)^J-1)\right].      \tag{10}
\]

For fixed `m,J` and any fixed `epsilon>0`, choose fixed `eta>0` small enough that the last term is
at most `J log_2(1+9/m)+epsilon`. Complex conjugation gives
`S_min(bar(L_(J,D)))=S_min(L_(J,D))` deterministically, without a second random event.

## 6. Conjugate Bell upper bound

At one layer, feed a normalized maximally entangled vector into
`Phi_(j,D) tensor bar(Phi_(j,D))`. Each of the `m^2` Kraus labels initially has weight `1/m^2`.
For the `m` equal-index labels,

\[
 (U_i\otimes\bar U_i)|\Omega_D\rangle=|\Omega_D\rangle,
\]

so those outputs merge to one state of total weight `1/m`. The other `m^2-m` labels retain
weights `1/m^2`; any further collision only lowers the entropy. Thus

\[
 S_{\min}(\Phi_{j,D}\otimes\bar\Phi_{j,D})
 \le2\log_2m-{\log_2m\over m}.                       \tag{11}
\]

Use the tensor product of the `J` Bell inputs to obtain

\[
 S_{\min}(L_{J,D}\otimes\bar L_{J,D})
 \le J\left(2\log_2m-{\log_2m\over m}\right).       \tag{12}
\]

Combining (10) and (12) gives

\[
 \Delta_{J,D}\ge Jc_m-2\epsilon.                    \tag{13}
\]

Since `m>e^18`,

\[
 {\log_2m\over m}>{18\over m\ln2}
 >2\log_2(1+9/m),
\]

so `c_m>0`. Take `epsilon=Jc_m/4`; equations (7) and (13) prove (1), and the strict choice
`J>2G/c_m` proves (2).

## 7. Relation to the two broader canonical records

The older node `HCPREV.product-haar-unbounded` additionally claims a finite-dimensional exact
MOE-to-Holevo pair transfer and a symmetric pair-to-self Holevo reduction with at most one bit
loss. Those two deterministic interfaces are absent from the old Q2 proof dossier. This new node
does not repair them and therefore does not license promotion of that broader node.

The old `product-haar-unbounded-route` in `HCPREV.random-models` supplies only the product-Haar
clause of a parent claim that also contains Hastings, ASW, BCN, and LLW named-model clauses. It
cannot establish the compound parent. The product-Haar clause is now owned by this atomic node;
the old route is retained as a retired historical attempt.

## 8. Strict boundary and review gate

This theorem is model-specific and MOE-only. It does not give:

- a Holevo gap for the same sampled pair;
- a same-channel gap;
- a compact deterministic unitary tuple;
- a probability rate or usable threshold in `D`;
- full support, density, residuality, or full measure in the CPTP body;
- a depth `J=J(D)` growing inside one limit; or
- a full-size extensive-violation theorem.

Before canonical promotion, a fresh reviewer must hash-bind the exact new claim, verify both
external theorem interfaces against the local PDFs, reconstruct the finite-net uniformization and
all-input complementary-channel argument, check the Bell entropy and strict quantifier order, and
confirm every non-propagation boundary above.

## 9. Registered exact hashes

The repository-normalized exact claim hash of
`HCPREV.product-haar-moe-unbounded` is

`sha256:d440f868f357ab31ba91a26b622eb020b69f597a4f5c62e69c53661689c0bc9e`.

This atomic node uses a route-free direct proof with two exact external-theorem assumptions, so it
has no artificial route hash. The retired historical
`HCPREV.random-models.routes.product-haar-unbounded-route` implication remains byte-for-byte the
statement reviewed at

`sha256:b1418ad7bdb5616942a0cff29ac6e6a8c918477b72eeffc2dd11cf0b1cdd9f58`.
