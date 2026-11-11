# Werner centered moment: threshold refinement from the unabsorbed planar term

Date: 2026-08-30

Status: proposer-side refinement for Question 3. This note does not change any `PROVED` claim.
It derives a stronger, exactly scoped centered-Werner theorem from existing `PROVED` atoms, but
the new route and claim require independent hash-bound review before promotion. It does not use
or affect any running SU(3) certificate.

## 1. Outcome

Fix an integer `m>=2` and fixed `eta>=0` before taking `d` to infinity. Let

\[
 R_U={1\over m^2}\sum_{v,a=1}^m U_v^*U_a\otimes U_a^*U_v,
 \qquad S_U=R_U-I/m,
\]

and

\[
 A=1+{9(1+\eta)^2\over m},\qquad
 H=\sqrt{(A^2-1)(1-m^{-2})}.
\]

The already proved large-`m` route imposed `m>e^18` because it first absorbed the planar
polynomial into the uniform connected base `32768^N`. Keeping the independently proved planar
factor explicit instead gives the sufficient condition

\[
 \boxed{mH>4096.}                                             \tag{1}
\]

Under (1),

\[
 \Pr\{\|R_U-I/m\|_\infty>H\}\longrightarrow0.              \tag{2}
\]

Since

\[
 (mH)^2=
 [18m(1+\eta)^2+81(1+\eta)^4](1-m^{-2}),                    \tag{3}
\]

condition (1) is explicit for every fixed pair `(m,eta)`. Uniformly over `eta>=0`, it holds for
every integer

\[
 \boxed{m\ge 932064.}                                        \tag{4}
\]

This improves the previous sufficient integer range `m>e^18`, whose first possible integer is
`65659970`, by a factor greater than `70` in the lower threshold. It is not a statement for every
fixed `m`.

## 2. Why the earlier threshold was not intrinsic

The reviewed every-genus aggregate atom uses

\[
 S_{N,h}\le32768^N N^{43h}\qquad(h\ge0).
\]

Its base `32768` is convenient but is created at genus zero by absorbing

\[
 16N^2\,4096^N\le32768^N\qquad(N\ge2).                      \tag{5}
\]

The factor `8^N` used in (5) is not a new map entropy. It only removes the polynomial `16N^2`
from the public all-genus interface. At logarithmic moment order, a fixed polynomial in `N` is
harmless and should not be charged to the exponential base.

The existing `PROVED` atoms expose the two estimates before this absorption:

1. the rooted planar two-face map count and lossless Werner ribbon injection, together with the
   minimal Catalan weight, give
   \[
      S_{N,0}\le16N^2\,4096^N;                              \tag{6}
   \]
2. the positive-genus weighted-count atom gives
   \[
      S_{N,h}\le4096^N N^{43h}\qquad(h\ge1).                \tag{7}
   \]

Thus the current proof data already support the smaller common exponential base `4096`, provided
the planar polynomial is retained explicitly.

## 3. Refined master inequality

Define

\[
 u={3m-4\over m^2H},\qquad
 a={4096\over mH},\qquad
 x_{43}={m^2N^{43}\over d^2},\qquad
 x_{24}={m^2N^{24}\over d^2},\qquad
 \theta={6(2N)^{7/2}\over d^2}.                              \tag{8}
\]

For every even `N>=2` with `x_43,x_24,theta<1`, the same exhaustive return/connected/disconnected
partition as in `WERNER_CENTERED_MOMENT_ALL_GENUS_ASSEMBLY_20260830.md`, but with genus zero kept
separate, yields

\[
 \boxed{
 {\mathbb E\operatorname{Tr}(S_U^N)\over H^N}
 \le
 2d^2u^N
 +{m^2a^N\over1-\theta}
 \left[
   16N^2+{x_{43}\over1-x_{43}}
   +N^{24}{x_{24}\over1-x_{24}}
 \right].}                                                   \tag{9}
\]

The terms are as follows.

### 3.1 Return union

The proved reversal/return atom gives

\[
 2d^2\left({3m-4\over m^2}\right)^N,
\]

which becomes the first term of (9) after division by `H^N`.

### 3.2 Connected planar nonreturn sector

For `c=1,h=0`, the equality-component atom gives `kappa<=N+2`, and the Euler power is one. Using
(6), the normalized minimal mass is at most

\[
 m^{-2N}m^{N+2}\,16N^2 4096^N
 =16m^2N^2\left({4096\over m}\right)^N.                      \tag{10}
\]

After division by `H^N`, this is `16m^2N^2a^N`.

### 3.3 Connected positive-genus nonreturn sector

For `c=1,h>=1`, combine (7), `kappa<=N+2+2h`, and the exact Euler factor `d^(-2h)`. The genus-`h`
mass is at most

\[
 m^2\left({4096\over m}\right)^N x_{43}^h.                  \tag{11}
\]

Summing from `h=1` gives `m^2(4096/m)^N x_43/(1-x_43)`.

### 3.4 Two-component nonreturn sector

The proved separation theorem moves every `c=2,h<=1` sequence into the return union. The proved
residual atom gives, after summing `h>=2`,

\[
 m^2\left({4096\over m}\right)^N
 N^{24}{x_{24}\over1-x_{24}}.                               \tag{12}
\]

Finally, the proved skeletonwise monotone-Weingarten theorem multiplies every nonreturn minimal
mass by at most `(1-theta)^(-1)`. Equations (10)--(12) and the return estimate prove (9).

## 4. Logarithmic moment and exact parameter condition

Write `b=(1+eta)^2>=1`. Formula (3) becomes

\[
 (mH)^2=(18mb+81b^2)(1-m^{-2}).                              \tag{13}
\]

Assume (1), so `0<a<1`. Also `0<u<1` for every `m>=2` and `eta>=0`: the left side of

\[
 (3m-4)^2<m^2(mH)^2
\]

is maximized relative to the right side at `eta=0`, and there the difference between the right
and left sides is

\[
 (18m+81)(m^2-1)-(3m-4)^2
 =18m^3+72m^2+6m-97>0.                                      \tag{14}
\]

Choose

\[
 N(d)=2\left\lceil{\gamma\log d\over2}\right\rceil,
 \qquad \gamma>{2\over\log(1/u)}.                           \tag{15}
\]

Then `2d^2u^N->0`, while `N^2a^N->0`. The positive-genus and two-component terms also vanish,
and `x_43,x_24,theta->0`. Since `N` is even,

\[
 \|S_U\|_\infty^N\le\operatorname{Tr}(S_U^N),
\]

so Markov's inequality proves (2).

## 5. Exact uniform integer corollary

For fixed `m`, the expression in (13) is increasing in `b>=1`; its minimum over `eta>=0` is

\[
 q(m):=(18m+81)(1-m^{-2})
      =18m+81-{18\over m}-{81\over m^2}.                     \tag{16}
\]

It is strictly increasing for `m>0`. Exact integer arithmetic gives

\[
 q(932063)-4096^2
 =-{868758213184\over868741435969}<0,                        \tag{17}
\]

whereas

\[
 q(932064)-4096^2
 ={14768619324399\over868743300096}>0.                       \tag{18}
\]

Therefore `932064` is the smallest integer for which the present `4096`-base proof has
`mH>4096` uniformly over all `eta>=0`. This proves the numerical corollary (4) exactly, without a
floating-point comparison.

For smaller `m`, the same route still applies whenever the actual fixed `eta` satisfies (1).
Equivalently, with

\[
 y_*(m)={-m+\sqrt{m^2+4096^2/(1-m^{-2})}\over9},             \tag{19}
\]

it suffices that `(1+eta)^2>y_*(m)`.

## 6. What determines the threshold, and what does not

Within the present absolute-moment dossier:

- the return base does not impose a large-`m` threshold, because (14) proves `u<1` for every
  `m>=2`;
- the handle exponents `43` and `24`, the `D,alpha` existential interface, and the monotone-tail
  factor affect only polylogarithmic or `d^(-2)` corrections at `N=Theta(log d)`;
- the disconnected base `4096` also carries an initial `d^(-2)` suppression after low-genus
  return separation;
- the decisive unsuppressed term is the connected planar bound (10), whose current exponential
  base is exactly `4096` once its harmless polynomial is left unabsorbed.

Consequently, the old `32768` threshold is an interface artifact, while `mH>4096` is the sharp
condition obtainable from the current sectorwise upper bounds without new planar information.
This last sentence is a limitation of the proof route, not a lower bound on the true theorem. If
`mH<=4096`, the available planar upper bound contributes `16m^2N^2a^N`, which does not tend to
zero for any moment order `N(d)->infinity`; the data therefore cannot certify the claim by this
absolute planar estimate. A smaller threshold would require at least one genuinely new input,
such as a smaller exponential base for admissible planar weighted constellations, cancellation in
the signed planar sum, or a theorem placing the planar nonreturn sector inside a better-controlled
class.

## 7. Strict scope boundary

The proposed theorem concerns only the centered flip/Werner coefficient sector at one two-leg
reuse of one fixed Haar tuple. It does not establish arbitrary-Hermitian same-tuple strong
convergence, the physical global `n=2` bound, any all-copy theorem, absolute-unbounded leakage, or
the Hayden--Penington full-size extensive-violation root. Those claims remain unchanged.
