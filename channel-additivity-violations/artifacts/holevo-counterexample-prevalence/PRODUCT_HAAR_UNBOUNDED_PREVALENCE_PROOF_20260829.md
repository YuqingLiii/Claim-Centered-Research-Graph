# Product-Haar prevalence of arbitrarily large finite-dimensional gaps

Date: 2026-08-29

Status: historical pre-review proposer-side proof. The exact product-Haar unbounded-prevalence
claim was subsequently independently reviewed and promoted to `PROVED`; its canonical YAML is
authoritative for current status.

This note records a stronger, model-specific answer to “are there many counterexamples?” than the
older one-shot random-channel statements.

## Theorem

Fix an integer `m>e^18` and define

\[
 c_m=\frac{\log_2m}{m}-2\log_2(1+9/m)>0.
\]

For a depth `J`, draw independent Haar unitaries

\[
 U_{i,j}^{(D)}\in U(D),\qquad i\in[m],\ j\in[J],
\]

and define

\[
 \Phi_{j,D}(\rho)=\frac1m\sum_iU_{i,j}^{(D)}\rho U_{i,j}^{(D)*},
 \quad
 L_{J,D}=\bigotimes_{j=1}^J\Phi_{j,D},
 \quad
 R_{J,D}=\overline{L_{J,D}}.
\]

For every fixed `J`,

\[
 \Pr\!\left[
 S_{\min}(L_{J,D})+S_{\min}(R_{J,D})-S_{\min}(L_{J,D}\otimes R_{J,D})
 \ge \frac12Jc_m
 \right]\longrightarrow1
\]

as `D` tends to infinity. Consequently, for every prescribed `G>0`, one may first choose a fixed
`J>2G/c_m`; then a product-Haar sampled finite-dimensional pair has `p=1` MOE gap greater than
`G` with probability tending to one as `D` grows.

For a concrete scale, choose `m=J=2^30`. Since

\[
 c_m>\frac{30-18/\ln2}{2^{30}},
\]

the displayed high-probability event has gap above `(30-18/ln2)/2>2.0157` bits for all
sufficiently large finite `D`. The remaining `D` threshold is existential, not practical.

Deterministic Weyl-flag extension gives the same probability statement for a specified random
family of finite-dimensional Holevo pair counterexamples, preserving the numerical gap. A
balanced direct-sum reduction then gives a specified random family of same-channel Holevo
counterexamples. Here the conjugate pair has equal one-shot Holevo quantities, so no classical
balancing channel is needed and the same-channel defect is at least

\[
 \log_2\!\left[1+\frac12(2^g-1)\right]\ge g-1.
\]

Thus the applicable constant loss for this symmetric family is one bit; `log_2(9/4)` is only the
weaker universal loss for an arbitrarily unbalanced pair.

## Proof and quantifier order

For `v in [m]^J`, set `W_v=tensor_j U_{v_j,j}`. Collins--Youn Theorem 3.3 bounds the free direct-
product operator

\[
 \left\|\sum_{v,w}a_{v,w}u_v^*u_w\right\|
 \le m^{J/2}\sqrt{(1+9/m)^J-1}\,\|a\|_2
\]

for every traceless coefficient matrix `a`.

Bordenave--Collins Theorem 9.2 says that for fixed `(m,J)` the finite tensor tuple converges
strongly in probability to these direct-product free generators. Compactness of the traceless
Hilbert--Schmidt unit sphere in `M_{m^J}` upgrades pointwise convergence to a simultaneous
coefficient bound: for every fixed `eta>0`, with probability tending to one,

\[
 \left\|\sum_{v,w}a_{v,w}W_v^*W_w\right\|
 \le(1+\eta)m^{J/2}\sqrt{(1+9/m)^J-1}\,\|a\|_2
\tag{1}
\]

for all traceless `a`. The upgrade uses a finite net; its size depends on fixed `m,J` but not on
`D`, so the finite union of failure events still has probability tending to zero.

Applying (1) to the centered output of the complementary channel and using
`S>=H_2=-log_2 Tr(rho^2)` yields, uniformly over all inputs,

\[
 S_{\min}(L_{J,D})=S_{\min}(R_{J,D})
 \ge J[\log_2m-\log_2(1+9/m)]-\epsilon
\tag{2}
\]

with probability tending to one, for arbitrary fixed `epsilon>0` after choosing `eta` small.

For the joint upper bound, use the tensor product of `J` maximally entangled states. At each layer
the `m` equal-index Kraus outcomes coincide and have total probability `1/m`; the remaining
`m^2-m` labels have probability `1/m^2`. Hence

\[
 S_{\min}(L_{J,D}\otimes R_{J,D})
 \le J\left(2\log_2m-\frac{\log_2m}{m}\right).
\tag{3}
\]

Equations (2)--(3) give a defect at least `Jc_m-2epsilon`. Set
`epsilon=Jc_m/4`. The event then implies the displayed `Jc_m/2` lower bound and its probability
tends to one.

The order of quantifiers is essential:

\[
 \forall G\;\exists J\;\forall\text{ sufficiently large }D:
 \Pr_D[\mathrm{gap}>G]\to1.
\]

This is not a theorem with `J=J(D)` growing inside one unquantified limit, and it is not a claim
about Haar/Lebesgue measure on the whole CPTP affine body.

## What “many” now means, and what it does not

The theorem establishes all of the following in one named model:

- arbitrarily large finite-dimensional `p=1` defects;
- high probability, not merely positive probability, after fixing the target gap/depth;
- an open neighborhood around every successful finite realization by entropy continuity;
- the same high-probability existence statement after the explicit MOE-to-Holevo extension.

It does not establish:

- density, residuality, or full measure in the entire CPTP space;
- a compact deterministic list of Kraus matrices with a checked exact/global certificate;
- a universal minimum dimension; or
- full-size extensive scaling when depth grows together with all dimensions.

## Sources

1. Collins--Youn, arXiv:1907.07856v2, Theorem 3.3 and the entropy argument in Theorems 3.4--3.5.
   Local SHA-256:
   `70c97a9e4c17218e17f159e00f3bc554011fa6f87b8966be494c97af0d726714`.
2. Bordenave--Collins, arXiv:2304.05714v2, Theorem 9.2 and Lemmas 9.3--9.4.
   Local SHA-256:
   `59e14a3334b24f5683d8a0a8919d6cf266cb587f9dbae8d78e8213ca3fe2d8ac`.

The high-probability finite-dimensional unbounded-gap conclusion is a new synthesis in this
project, not a verbatim theorem quoted from either paper.
