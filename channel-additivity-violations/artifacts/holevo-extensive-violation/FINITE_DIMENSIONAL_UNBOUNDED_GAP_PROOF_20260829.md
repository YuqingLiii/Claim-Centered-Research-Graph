# Finite-dimensional unbounded `p=1` additivity gaps from tensor strong convergence

Date: 2026-08-29

Status: historical pre-review proposer-side proof. The exact finite-dimensional unbounded-gap claim
was subsequently independently reviewed and promoted to `PROVED`; its canonical YAML is
authoritative for current status.

This note combines two primary-source ingredients that were not combined in the earlier audit:

1. the product-free-group Haagerup estimate of Collins--Youn; and
2. the finite-dimensional tensor strong-convergence theorem of Bordenave--Collins.

The resulting statement is stronger than the previously audited almost-one-bit result:
finite-dimensional minimum-output-entropy (`MOE`) pair gaps, and hence finite-dimensional Holevo
pair and same-channel gaps, are **unbounded in absolute size**. The construction does **not** yet
establish Hayden--Penington full-size extensivity, because the available strong-convergence theorem
is asymptotic for each fixed tensor depth and does not supply a sufficiently controlled dimension
rate as the depth grows.

All logarithms below are base two.

## Theorem

For every `G>0`, there are finite-dimensional quantum channels `L,R` such that

\[
  S_{\min}(L)+S_{\min}(R)-S_{\min}(L\otimes R)>G.
\]

Consequently, after the exact Weyl-flag transfer, there are finite-dimensional channel pairs with
Holevo defect greater than `G`. After the symmetric direct-sum pair-to-self reduction, there are
finite-dimensional channels `T` for which

\[
  \chi(T^{\otimes 2})-2\chi(T)>G-1.
\]

In particular, both finite-dimensional `p=1` MOE pair defects and finite-dimensional Holevo
same-channel defects are unbounded.

## Construction

Fix an integer

\[
  m>e^{18}
\]

and a hierarchy depth `J>=1`. For each tensor leg `j in {1,...,J}`, let

\[
  U_{1,j}^{(D)},\ldots,U_{m,j}^{(D)}\in U(D)
\]

be independent Haar unitaries. Define a random-unitary channel on the `j`th `D`-dimensional
system by

\[
  \Phi_{j,D}(\rho)=\frac1m\sum_{i=1}^m U_{i,j}^{(D)}\rho U_{i,j}^{(D)*}.
\]

Set

\[
  L_{J,D}=\bigotimes_{j=1}^J\Phi_{j,D},\qquad
  R_{J,D}=\overline{L_{J,D}}.
\]

For `v=(v_1,...,v_J) in [m]^J`, write

\[
  W_v^{(D)}=\bigotimes_{j=1}^J U_{v_j,j}^{(D)}.
\]

Then `L_{J,D}` has the `m^J` Kraus operators `m^{-J/2}W_v^{(D)}`.

## Step 1: uniform finite-dimensional norm bound

Let `u_{i,j}` denote the canonical generators of the direct product `F_m^J`, represented on
`ell_2(F_m)^{tensor J}`, and put `u_v=product_j u_{v_j,j}`. Collins--Youn, Theorem 3.3, proves
that every traceless scalar matrix `a=(a_{v,w})` satisfies

\[
 \left\|\sum_{v,w\in[m]^J}a_{v,w}u_v^*u_w\right\|
 \le K_{m,J}\|a\|_2,
\]

where

\[
 K_{m,J}=m^{J/2}\sqrt{(1+9/m)^J-1}.
\tag{1}
\]

Bordenave--Collins, Theorem 9.2, says that for every fixed pair `(m,J)`, the tuple consisting of
the independent Haar unitaries placed on the `J` tensor legs converges strongly in probability to
the corresponding canonical generators of `F_m^J`.

For completeness, this pointwise statement gives the uniform estimate needed here. For fixed
`m,J`, the traceless Hilbert--Schmidt unit sphere in `M_{m^J}` is compact. Both maps

\[
 a\longmapsto\left\|\sum a_{v,w}W_v^{(D)*}W_w^{(D)}\right\|,
 \qquad
 a\longmapsto\left\|\sum a_{v,w}u_v^*u_w\right\|
\]

are Lipschitz on that finite-dimensional coefficient space; the crude common Lipschitz constant
`m^J` follows from `sum|a_{v,w}|<=m^J||a||_2`. Apply strong convergence to a finite net and then
use the Lipschitz estimate. Thus, for every `eta>0`, with probability tending to one as `D` tends
to infinity,

\[
 \left\|\sum_{v,w}a_{v,w}W_v^{(D)*}W_w^{(D)}\right\|
 \le (1+\eta)K_{m,J}\|a\|_2
\tag{2}
\]

simultaneously for every traceless `a`. In particular, for every fixed `m,J,eta`, a finite `D` and
a deterministic realization satisfying (2) exist.

## Step 2: global side lower bound

Put `q=m^J`. A complementary channel of `L=L_{J,D}` is

\[
  L^c(S)_{v,w}=q^{-1}\operatorname{Tr}(W_vSW_w^*).
\]

For a density matrix `S`, set

\[
  X=L^c(S)-I_q/q.
\]

Every diagonal entry of `L^c(S)` is `1/q`, hence `X` is Hermitian, traceless, and has zero
diagonal. Using `Tr X=0`, duality, and (2),

\[
\begin{aligned}
 \|X\|_2^2
 &=\operatorname{Tr}(L^c(S)X)\\
 &=\operatorname{Tr}(S(L^c)^*(X))\\
 &\le \|(L^c)^*(X)\|_\infty\\
 &\le q^{-1}(1+\eta)K_{m,J}\|X\|_2.
\end{aligned}
\]

Therefore

\[
  \|X\|_2\le (1+\eta)m^{-J/2}\sqrt{(1+9/m)^J-1}.
\tag{3}
\]

Since `Tr X=0`, (3) implies

\[
\begin{aligned}
 \operatorname{Tr}(L^c(S)^2)
 &=m^{-J}+\|X\|_2^2\\
 &\le m^{-J}\left[1+(1+\eta)^2\big((1+9/m)^J-1\big)\right].
\end{aligned}
\]

Von Neumann entropy dominates Renyi-2 entropy, so

\[
 S(L^c(S))\ge J\log m-
 \log\left[1+(1+\eta)^2\big((1+9/m)^J-1\big)\right].
\tag{4}
\]

The minimum of output entropy is attained on a pure input. On a pure input a channel and its
complement have the same nonzero output spectrum. Hence (4) is a **global**, all-input lower
bound on `S_min(L)`. Complex conjugation preserves output spectra, so the same lower bound holds
for `R=bar L`.

For fixed `m,J`, choose `eta` sufficiently small and then choose a finite `D` satisfying (2). For
every `epsilon>0`, this gives

\[
 S_{\min}(L),S_{\min}(R)
 \ge J\big(\log m-\log(1+9/m)\big)-\epsilon.
\tag{5}
\]

## Step 3: matched Bell upper bound

For one layer, apply `Phi_{j,D} tensor bar(Phi_{j,D})` to a normalized maximally entangled state
`Omega_D`. In the resulting ensemble of `m^2` pure states, the `m` terms with equal indices all
coincide with `Omega_D`, because

\[
  (U\otimes\bar U)|\Omega_D\rangle=|\Omega_D\rangle.
\]

Merging these identical labels gives one probability `1/m` and `m^2-m` probabilities `1/m^2`.
The entropy of a mixture is at most the Shannon entropy of any pure-state ensemble realizing it;
therefore the one-layer output entropy is at most

\[
 -\frac1m\log\frac1m-(m^2-m)\frac1{m^2}\log\frac1{m^2}
 =2\log m-\frac{\log m}{m}.
\tag{6}
\]

Use the tensor product of `J` Bell states. The output is the tensor product of the `J` layer
outputs, so (6) gives

\[
 S_{\min}(L\otimes R)
 \le J\left(2\log m-\frac{\log m}{m}\right).
\tag{7}
\]

## Step 4: linear-in-depth defect

Combining (5) and (7),

\[
\begin{aligned}
 &S_{\min}(L)+S_{\min}(R)-S_{\min}(L\otimes R)\\
 &\quad\ge Jc_m-2\epsilon,
\end{aligned}
\tag{8}
\]

where

\[
 c_m=\frac{\log m}{m}-2\log(1+9/m).
\tag{9}
\]

The coefficient is positive whenever `ln m>18`, because

\[
 2\log_2(1+9/m)<\frac{18}{m\ln2}
 <\frac{\ln m}{m\ln2}=\frac{\log_2m}{m}.
\]

Fix any integer `m>e^18`, take `epsilon=Jc_m/4`, and choose the corresponding finite `D`.
Equation (8) then yields a finite-dimensional pair gap at least `Jc_m/2`. Letting `J` grow proves
absolute unboundedness.

### A concrete greater-than-one-bit parameter choice

The existence statement can be made numerically concrete before the final matrix dimension is
chosen. Take

\[
 m=J=2^{30}.
\]

Using `ln(1+t)<t`,

\[
 c_m>\frac{30-18/\ln2}{2^{30}}.
\]

Therefore the certified `Jc_m/2` defect is strictly greater than

\[
 \frac{30-18/\ln2}{2}>2.0157\ \text{bits}.
\]

For all sufficiently large but finite `D`, the successful product-Haar event thus gives a finite-
dimensional `p=1` MOE pair gap above two bits. This makes “greater than one bit” a direct corollary
with explicit `m,J`; the proof still does not give a practical threshold for `D` or printable
unitaries.

The size of this concrete certificate is already prohibitive before choosing `D`: the channel has
`m^J=(2^30)^(2^30)=2^(30*2^30)` product-word/Kraus labels. Each input leg then has dimension
`D^J`, where the strong-convergence theorem supplies only an ineffective existence threshold for
`D`. Hence this numerical choice quantifies the theorem's scale while also making precise why it
is not a practical printed witness. The computable-search refinement is likewise terminating but
has no useful resource bound.

## Step 5: transfer to Holevo and to one channel

Before applying the transfer one may replace `L,R` by their complementary channels. Minimum output
entropy is unchanged under complementation, including for the product pair, so the numerical MOE
gap is unchanged. This choice reduces each original output dimension from `D^J` to `m^J`, while
the input dimension remains `D^J`.

The Weyl-flag extension proved in `MOE_TO_HOLEVO_TRANSFER_PROOF_20260829.md` maps each finite
channel to a finite channel and preserves the numerical pair defect exactly:

\[
 \chi(\widetilde L\otimes\widetilde R)-\chi(\widetilde L)-\chi(\widetilde R)
 =S_{\min}(L)+S_{\min}(R)-S_{\min}(L\otimes R).
\]

Here the transferred channels have equal one-shot Holevo quantities because they are constructed
from a conjugate pair with equal dimensions and equal minimum output entropies. Thus the direct-sum
formula in `PAIR_TO_SELF_REDUCTION_2026-08-29.md` has balance weight `w=1/2` without adding a
classical balancing channel. It gives one finite channel `T` satisfying

\[
 \chi(T^{\otimes2})-2\chi(T)
 \ge\log_2\!\left[1+\frac12(2^g-1)\right]\ge g-1.
\]

Since the loss is constant, unbounded pair gaps imply unbounded same-channel Holevo gaps. Also
`C(T)>=chi(T^{tensor 2})/2`, so `C(T)-chi(T)` is unbounded along the resulting family (up to the
corresponding factor `1/2` and constant loss).

## What this does not prove

For depth `J`, each original random-unitary side channel acts on input and output dimension
`D(J)^J`; its complement maps the same input to output dimension `m^J`. After using the complement
and Weyl-flag transfer, the input dimension is `m^(2J)D(J)^J` and the output dimension is `m^J`.
The proof selects a sufficiently large but otherwise uncontrolled finite `D(J)` after fixing `J`.

Bordenave--Collins Theorem 9.2 is a fixed-`J` convergence statement. The argument above therefore
does not bound `log D(J)` as `J` grows. The obtained gap is `Omega(J)`, while the full input/output
logarithmic cost is `J log D(J)`. Without a bound such as `log D(J)=O(1)` (or another cost/gap
comparison), equation (8) does not imply a Hayden--Penington `Omega(full log dimension)` result.

Thus the correct split is:

- finite-dimensional absolute gap above one bit: **yes, proposer-side proved**;
- finite-dimensional absolute unbounded gap: **yes, proposer-side proved**;
- Hayden--Penington full-size extensive gap: **still open in this project**.

## Source audit

1. Benoit Collins and Sang-Gyun Youn, *Additivity Violation of the Regularized Minimum Output
   Entropy*, arXiv:1907.07856v2. Theorem 3.3 supplies (1); Theorems 3.4--3.5 contain the associated
   entropy argument; Theorem 4.1 supplies the free-group matched-witness mechanism.
   Local SHA-256:
   `70c97a9e4c17218e17f159e00f3bc554011fa6f87b8966be494c97af0d726714`.
2. Charles Bordenave and Benoit Collins, *Norm of matrix-valued polynomials in random unitaries
   and permutations*, arXiv:2304.05714v2. Theorem 9.2 gives tensor strong convergence to the
   regular representation of `F_m^J`; Lemmas 9.3--9.4 are its quantitative ingredients.
   Local SHA-256:
   `59e14a3334b24f5683d8a0a8919d6cf266cb587f9dbae8d78e8213ca3fe2d8ac`.

The finite-dimensional unbounded-gap theorem itself is a new synthesis/derivation in this project;
it is not claimed as a verbatim theorem from either source.
