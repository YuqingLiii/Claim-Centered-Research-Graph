# Repair amendment review: tensor-strong-convergence quantitative rate gate

Date: 2026-08-31

Reviewer: independent Codex review context `/root/q1_weyl_transfer_review`.

## Scope and immutable inputs

This amendment checks only the four Bordenave--Collins assumptions registered after Finding
HEXT-RG-IR-07 of the initial independent review. It does not enlarge the claim or review the true
defect of the channel family.

| object | SHA-256 |
|---|---|
| repaired node YAML | `b0d890b71fedd922753487a3abb2c3f67c73e062513fe6a11f3c8c48b2183b17` |
| Bordenave--Collins PDF | `59e14a3334b24f5683d8a0a8919d6cf266cb587f9dbae8d78e8213ca3fe2d8ac` |

The canonical claim is unchanged at
`sha256:4dadeb060c65e6b31e4db969da267e732d758d5f609ae0914d2bcb3c4ec7f37d`.

## Amendment finding HEXT-RG-AR-01 -- PASS: Theorem 9.2

The first assumption correctly fixes `m>=2` and `J>=1`, uses independent Haar unitaries embedded
on separate tensor legs, and sends only the per-leg dimension `D` to infinity. The target is the
regular representation of `F_m^J`, and convergence is strong in probability. Its statement that
the theorem supplies no growing-`J` threshold is a correct scope observation, not an extra theorem.
The locator, Theorem 9.2 on PDF pp. 62--63, is exact.

**Verdict:** PASS.

## Amendment finding HEXT-RG-AR-02 -- PASS: Lemma 9.3

The second assumption correctly records `m^70<=D`, an even integer
`2<=p<=D^(1/(16m+80))`, coefficient size `n`, and the complete upper expectation factor

```text
(2n)^((J+1)/p) D^(J(J+1)/(2p))
p^(3J(J+1)/(2p)) (1+c/sqrt(D))^J.
```

It correctly identifies the comparison norm as the regular `F_m^J` linear-pencil norm and limits
the interface to one-pencil expectation, not a coefficient-sphere probability event. Lemma 9.3 and
its proof occupy PDF pp. 63--65.

**Verdict:** PASS.

## Amendment finding HEXT-RG-AR-03 -- PASS: Corollary 8.2 and Theorem 8.3

Under the node's renaming of the source's positive generator count from `d` to `s`, the registered
linearization bounds agree with PDF pp. 58--59:

```text
n_lin <= 2^l(2s)^(2l),
relative-error amplification <=4l^2(2s)^(2l),
epsilon <=(2s)^(-l)l^(-2).
```

The assumption explicitly restricts this interface to a candidate quantitative blueprint and does
not claim that Corollary 8.2/Theorem 8.3 assemble the missing tensor-leg tail, algebraic-kernel, or
coefficient-net theorem.

**Verdict:** PASS.

## Amendment finding HEXT-RG-AR-04 -- PASS: Lemma 7.4

The fourth assumption matches the one-pencil Haar concentration theorem on PDF pp. 52--53. For
`d` independent Haar unitaries, source-normalized Schatten norm, `t>0`, and
`2<=p<=infinity`, it states

```text
Pr{| ||A_D||_p-E||A_D||_p | >= t||A_F||}
 <=2 exp[-c D^(1+2/p)t^2/d].
```

The assumption also accurately states what the lemma does not provide: it is not already a tail
for the tensor-leg, coefficient-dependent-linearization, algebraic-kernel, simultaneous-net event
needed by the entropy proof.

**Verdict:** PASS.

## Final amendment verdict

**PASS.** All four machine-visible assumptions have the correct formulas, quantifiers, locators,
and strict one-pencil/candidate-blueprint scope. They close the sole completion blocker identified
by the initial review.

The exact proof-method obstruction at
`sha256:4dadeb060c65e6b31e4db969da267e732d758d5f609ae0914d2bcb3c4ec7f37d`
is eligible for proposer-side promotion to `PROVED` after this amendment is linked. This reviewer
does not modify the canonical node.

The authorization is limited to the published-certificate obstruction. It does not establish a
channel impossibility theorem, refute stronger estimates, or authorize any change to `HEXT.goal`.

