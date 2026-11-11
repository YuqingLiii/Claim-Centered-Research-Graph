# Werner centered moment from the reviewed every-genus count

Date: 2026-08-30

Status: proposer-side route amendment for Question 3; independent review is pending. This note
does not promote a canonical claim. It replaces the extra planar Input P in
`WERNER_CENTERED_MOMENT_FINAL_CONDITIONAL_ASSEMBLY_20260830.md` by the subsequently reviewed
every-genus structural node.

## 1. Exact scope

Fix an integer `m>e^18` and `eta>=0` before taking `d` to infinity. Let

\[
 R_U={1\over m^2}\sum_{v,a=1}^m U_v^*U_a\otimes U_a^*U_v,
 \qquad S_U=R_U-I/m,
\]

and

\[
 A=1+{9(1+\eta)^2\over m},\qquad
 H=\sqrt{(A^2-1)(1-m^{-2})}.
\]

The target of this note is only

\[
 \Pr\{\|S_U\|_\infty>H\}\longrightarrow0.
\tag{1}
\]

It is not the arbitrary-coefficient same-tuple theorem, the global physical `n=2` purity bound,
or the full-size extensive-violation theorem.

## 2. Reviewed premises used

The following canonical claims are currently `PROVED`.

1. `HEXT.werner-two-boundary-constellation-count`: for connected genus `h` triples, the total
   minimal Catalan weight is at most
   \[
     32768^N N^{43h}
   \tag{2}
   \]
   for every `N,h`, and `32768<sqrt(18m)` in the project regime.
2. `HEXT.werner-admissible-equality-component-genus-bound`: for connected admissible skeletons,
   `kappa<=N+2+2h`.
3. `HEXT.werner-two-component-low-genus-return-separation`: every `c=2,h<=1` skeleton is in the
   forward/reverse return union.
4. `HEXT.werner-two-component-nonreturn-weighted-count`: for `c=2,h>=2`, the structural weight is
   at most `4096^N N^(24h)`, `kappa<=N+2h`, and the exact normalized minimal mass has the form
   stated below.
5. `HEXT.werner-monotone-weingarten-tail-summability`: every fixed minimal skeleton acquires at
   most the factor `1/(1-theta)` after summing all excess paths, where
   `theta=6(2N)^(7/2)/d^2<1`.
6. `HEXT.werner-constellation-euler-deficit`: the minimal dimension power is
   `d^(2c-2h-2)`.

The exact centered forward/block-reversal expansion and the return estimate are proved directly
in `WERNER_CENTERED_GROWING_TRACE_METHOD_GATE_20260830.md` and were independently accepted in
Finding STPW-IR-05 of
`SAME_TUPLE_POSITIVE_WERNER_TRACE_INDEPENDENT_REVIEW_20260830.md`. Their use is re-audited as part
of the final route implication rather than treated as an unresolved premise.

## 3. Shortened master inequality

Define

\[
 u={3m-4\over m^2H},\qquad
 b={32768\over mH},\qquad
 a={4096\over mH},
\]

and

\[
 x_{43}={m^2N^{43}\over d^2},\qquad
 x_{24}={m^2N^{24}\over d^2},\qquad
 \theta={6(2N)^{7/2}\over d^2}.
\tag{3}
\]

For every even `N` with `x_43,x_24,theta<1`, the reviewed premises imply

\[
 \boxed{
 {\mathbb E\operatorname{Tr}(S_U^N)\over H^N}
 \le
 2d^2u^N
 +
 {m^2\over1-\theta}
 \left[
   {b^N\over1-x_{43}}
   +a^N N^{24}{x_{24}\over1-x_{24}}
 \right].}
\tag{4}
\]

Here is the complete sector accounting.

### Return sector

Before any skeleton expansion, forward or block-reversed free-word returns contribute in absolute
value at most

\[
 2d^2\left({3m-4\over m^2}\right)^N.
\tag{5}
\]

This includes every possible component count, genus and Weingarten excess belonging to a return
edge sequence.

### Connected nonreturn sector

For `c=1`, combine (2), `kappa<=N+2+2h`, and the Euler power `d^(-2h)`. The normalized minimal
genus-`h` mass is at most

\[
 m^{-2N}m^{N+2+2h}32768^NN^{43h}d^{-2h}
 =m^2\left({32768\over m}\right)^N x_{43}^h.
\tag{6}
\]

Summing `h>=0` gives the first bracketed term in (4). In particular the planar sector is already
included by the reviewed every-genus theorem; no extra specialization of a positive-genus
tree--cotree code is required.

### Two-component nonreturn sector

The low-genus separation theorem puts every `c=2,h<=1` sequence into (5). For the residual
`h>=2` sector, the reviewed count and label bound give

\[
 m^{-2N}m^{N+2h}4096^NN^{24h}d^{2-2h}
 =m^2\left({4096\over m}\right)^N
   N^{24}x_{24}^{h-1}.
\tag{7}
\]

Summing `h>=2` gives the second bracketed term in (4).

### Excess paths

The monotone-Weingarten theorem multiplies the total minimal mass of every nonreturn sector by at
most `1/(1-theta)`. It does not add a label-block convolution or factorial. Applying that common
factor to (6)--(7) and adding (5) proves (4).

## 4. Logarithmic even moment and exact threshold

The threshold satisfies

\[
 (mH)^2=
 [18m(1+\eta)^2+81(1+\eta)^4](1-m^{-2})>18m.
\tag{8}
\]

For `m>e^18`, the independently reviewed constant comparison gives

\[
 4096<32768<\sqrt{18m}<mH,
\tag{9}
\]

so `0<a<b<1`; also `0<u<1`.

Choose

\[
 N(d)=2\left\lceil{\gamma\log d\over2}\right\rceil,
 \qquad \gamma>{2\over\log(1/u)}.
\tag{10}
\]

Then `2d^2u^N->0`, `a^N->0`, `b^N->0`, and
`x_43,x_24,theta->0`. Hence the right-hand side of (4) tends to zero. Because `N(d)` is even,

\[
 \|S_U\|_\infty^{N(d)}\le\operatorname{Tr}(S_U^{N(d)}),
\]

and Markov proves (1).

## 5. Protocol consequence and remaining review

The shortened assembly has no new planar mathematical premise. Its load-bearing canonical
premises are exactly the six `PROVED` nodes in Section 2; the exact return expansion/estimate and
the algebra (3)--(10) belong to the route implication that still requires independent hash-bound
review.

The scope `m>e^18, eta>=0` must remain in the target claim. If the existing
`HEXT.same-tuple-werner-centered-bound` is read as quantifying over every fixed `m`, this route
proves only a strict large-`m` subclaim and must be registered in a new atomic node rather than
silently promoting the broader statement.

Even after independent approval, the result closes only the high-probability centered flip/Werner
coefficient sector in the project regime. It does not imply arbitrary Hermitian same-tuple strong
convergence, the physical all-input `n=2` estimate, any `n>=3` purity statement, or the
Hayden--Penington full-size extensive-violation target.
