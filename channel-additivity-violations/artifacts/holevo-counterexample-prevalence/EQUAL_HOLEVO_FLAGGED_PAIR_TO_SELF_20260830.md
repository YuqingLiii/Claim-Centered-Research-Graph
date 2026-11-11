# Equal-Holevo flagged pair-to-self reduction with at most one-bit loss

Date: 2026-08-30

Status: historical Q2-local proposer-side direct-proof snapshot. No external theorem is imported:
the classical-flag direct-sum Holevo identity is proved below. The canonical atom was subsequently
promoted to `PROVED` after independent hash-bound review; this file records the proof as it stood
before that promotion and is not an authoritative status store.

All logarithms are base two.

## 1. Exact statement

Let `A` and `B` be finite-dimensional channels with

\[
 \chi(A)=\chi(B)=x,
\]

and define their pair defect

\[
 g=\chi(A\otimes B)-2x\ge0.                               \tag{1}
\]

Let `T=A direct_sum B` be the symmetric classical-flag channel. Then

\[
 \chi(T)=x+1,                                             \tag{2}
\]

and

\[
 \chi(T\otimes T)-2\chi(T)
 \ge\log_2\left[1+{1\over2}(2^g-1)\right]
 \ge g-1.                                                 \tag{3}
\]

The first lower bound in (3) is strictly positive whenever `g>0`; the weaker `g-1` form records
the universal at-most-one-bit loss useful for unbounded gaps.

If the output dimensions of `A,B` are `d_A,d_B`, the flagged output dimension is `d_A+d_B`, so

\[
 \log_2(d_A+d_B)\le\max\{\log_2d_A,\log_2d_B\}+1.         \tag{4}
\]

For the common `d`-dimensional outputs produced by the Weyl atom, this is exactly
`log_2(2d)=log_2d+1`.

## 2. Flagged direct-sum channel

On the direct-sum input and output spaces define

\[
 T(\rho)=A(P_A\rho P_A)\oplus B(P_B\rho P_B),             \tag{5}
\]

where `P_A,P_B` project onto the two input branches. Cross-branch coherences are discarded and the
output branch is an orthogonal classical flag. Equation (5) is finite-dimensional and CPTP.

## 3. Direct-sum Holevo identity from first principles

More generally, for a finite family of flagged channels `T_i`, every ensemble induces an average
branch distribution `p_i` and conditional signal ensembles inside the branches. The classical
flag entropy decomposition, or equivalently the chain rule for the classical-quantum mutual
information, gives

\[
 \chi(\text{one ensemble})
 \le H(p)+\sum_ip_i\chi(T_i).                             \tag{6}
\]

For fixed `p`, equality can be approached by using optimal branch ensembles. Maximizing over `p`
gives the elementary Gibbs variational identity

\[
 \max_p\left[H(p)+\sum_ip_i x_i\right]
 =\log_2\sum_i2^{x_i},                                    \tag{7}
\]

attained at `p_i=2^(x_i)/sum_j2^(x_j)`. Therefore

\[
 \boxed{\chi(\mathop{\rm direct\_sum}_iT_i)
 =\log_2\sum_i2^{\chi(T_i)}.}                             \tag{8}
\]

With two equal values `x`, equation (8) gives (2).

## 4. Four-block tensor-square calculation

The tensor square is the flagged direct sum of four channels:

\[
 T\otimes T=(A\otimes A)\oplus(A\otimes B)
 \oplus(B\otimes A)\oplus(B\otimes B).                   \tag{9}
\]

Product ensembles give

\[
 \chi(A\otimes A)\ge2x,
 \qquad
 \chi(B\otimes B)\ge2x.                                 \tag{10}
\]

Input/output swaps preserve Holevo quantity, so

\[
 \chi(B\otimes A)=\chi(A\otimes B)=2x+g.                 \tag{11}
\]

Applying (8) to (9)--(11),

\[
 \begin{aligned}
 2^{\chi(T\otimes T)}
 &\ge2\,2^{2x}+2\,2^{2x+g}\\
 &=2^{2x+1}(1+2^g).
 \end{aligned}                                           \tag{12}
\]

Since `2 chi(T)=2x+2`, subtraction after taking logarithms gives

\[
 \chi(T\otimes T)-2\chi(T)
 \ge\log_2(1+2^g)-1
 =\log_2\left[1+{1\over2}(2^g-1)\right].                \tag{13}
\]

Also `1+2^g>=2^g`, so (13) is at least `g-1`. This proves (3).

## 5. Pushforward random-family consequence

Suppose a transformed random pair `(A_omega,B_omega)` has equal one-shot Holevo quantities and
pair defect `g_omega` on an event of probability tending to one. Apply (5) deterministically to
each realization. Equations (2)--(3) hold sample-by-sample, hence under the pushforward law

\[
 \Pr\{\text{self defect of }T_\omega\ge g_\omega-1\}
\]

inherits that event probability. For any desired self-gap target `G`, it suffices to start with a
pair-gap target strictly larger than `G+1`.

This does not say that either original sampled channel equals `T_omega`, or that the pushforward
law is product-Haar, Haar on channels, or full-support on the whole CPTP body.

## 6. Strict boundary and review gate

The constant-loss statement depends on equal one-shot Holevo quantities. For an unbalanced pair,
additional balancing is required and the present one-bit formula cannot be imported unchanged.
This atom proves a two-copy one-shot Holevo self defect, not a minimum-output-entropy statement,
an all-copy rate, or a full-size extensive theorem.

A fresh reviewer must independently verify (8) for arbitrary flagged input ensembles, the four
block structure, swap invariance, product-ensemble lower bounds, both inequalities in (3), the
log-dimension statement, equal-quantity hypothesis, and pushforward-law boundary.

## 7. Registered exact hash

The repository-normalized exact claim hash of
`HCPREV.equal-holevo-flagged-pair-to-self` is

`sha256:d598b38e12441325f6f51955be5080e1cbc3400739eba59dc01bd755ed4587d3`.

This is a route-free direct proof with no external theorem assumption, so no artificial route hash
is registered.
