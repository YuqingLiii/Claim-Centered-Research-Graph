# Fixed-channel Bell extensivity requires an entanglement-cost surplus

Date: 2026-08-30

Status: proposer-side tensor-regularized consequence; independent review pending.

All logarithms are base two.

## Statement

Let `Phi:M_d->M_k` satisfy `Phi(I_d/d)=I_k/k`. Define

\[
 Z=(\Phi\otimes\bar\Phi)(\Omega_d),\qquad
 \Theta=(k/d)\Phi\Phi^*,
\tag{1}
\]

and let

\[
 \sigma_{BE}=V(I_k/k)V^\dagger
\tag{2}
\]

be the maximally mixed Stinespring output of the Gram channel `Theta`. Write

\[
 \overline S_{\min}(\Phi)
 =\lim_{n\to\infty}\frac1nS_{\min}(\Phi^{\otimes n})
\tag{3}
\]

and

\[
 E_C(\sigma)=\lim_{n\to\infty}\frac1nE_F(\sigma^{\otimes n})
\tag{4}
\]

for the regularized minimum output entropy and entanglement cost. Then

\[
 \boxed{
 2\overline S_{\min}(\Phi)-S(Z)
 \le 2E_C(\sigma_{BE})-S(E)_\sigma.}
\tag{5}
\]

Consequently, the fixed-channel conjugate-Bell route can have a positive asymptotic defect rate
only if

\[
 \boxed{E_C(\sigma_{BE})>\tfrac12 S(E)_\sigma.}
\tag{6}
\]

This is necessary, not sufficient: the right-hand side of (5) may be positive while the channel's
regularized minimum output entropy is too small.

## 1. Apply the one-shot identity at every tensor power

For each `n`, the tensor-power channel `Phi^tensor n` still maps maximally mixed input to maximally
mixed output. Its conjugate-Bell output is

\[
 Z_n=Z^{\otimes n},
\tag{7}
\]

its Gram channel is `Theta^tensor n`, and a Stinespring output at maximally mixed input is
`sigma_BE^tensor n`. Applying the one-shot Gram-channel correlation bound to this tensor-power
channel gives

\[
 2S_{\min}(\Phi^{\otimes n})-S(Z^{\otimes n})
 \le 2E_F(\sigma_{BE}^{\otimes n})-S(E^{\otimes n}).
\tag{8}
\]

Entropy additivity on product states turns (8) into

\[
 2S_{\min}(\Phi^{\otimes n})-nS(Z)
 \le 2E_F(\sigma_{BE}^{\otimes n})-nS(E)_\sigma.
\tag{9}
\]

The Choi purification gives `S(Z)=S(E)_sigma`, but keeping both labels in (9) records which side of
the argument each term comes from.

## 2. Regularize

Both sequences

\[
 S_{\min}(\Phi^{\otimes n})
 \quad\text{and}\quad
 E_F(\sigma^{\otimes n})
\tag{10}
\]

are subadditive under concatenation of tensor blocks. Fekete's lemma therefore gives the limits in
(3) and (4), each equal to the infimum of its normalized sequence. Divide (9) by `n` and take the
limit to obtain (5).

If the left-hand side of (5) is positive, then the right-hand side must be positive, which is
exactly (6).

## 3. Relation to the full-size question

If a fixed finite `Phi` satisfies

\[
 2\overline S_{\min}(\Phi)-S(Z)>0,
\tag{11}
\]

then ordinary tensor powers give a defect linear in the copy count, while every logarithmic system
dimension is also linear in the copy count. Thus (11) is a sufficient fixed-channel bootstrap to a
full-size extensive family.

Equation (6) is a new necessary gate for that bootstrap. It says that a promising one-shot Gram
state is not enough: its entanglement-of-formation surplus must survive regularization all the way
to entanglement cost. This is precisely where a one-shot hiding or locking effect can disappear.

## 4. Research consequence

The top fixed-channel target can now be screened in the following order:

1. verify that the candidate Choi state is realignment-positive and comes from a Gram channel;
2. verify the rectangular CP factorization `Theta=(k/d)Phi Phi^*`;
3. prove `E_C(sigma_BE)>S(E)/2`;
4. prove the stronger left-hand side of (5) is positive by a global all-input lower bound for every
   tensor power of `Phi`.

Failure at steps 1--3 kills the fixed-channel conjugate-Bell route before the hardest global
minimum-output-entropy analysis. Passing step 3 does not settle step 4.

## Scope and nonclaims

- The result applies to the product maximally entangled witness for `Phi^tensor n` and
  `bar(Phi)^tensor n`; it does not bound an optimized non-Bell joint input.
- It is a necessary condition for a positive fixed-channel Bell-certified regularized defect, not
  an existence theorem.
- No claim is made that entanglement cost is additive or computable for the candidate states.
- The complete full-size extensive question remains open.

