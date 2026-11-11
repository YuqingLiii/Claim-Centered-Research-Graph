# Temperley--Lieb finite-channel regularization gate

Date: 2026-08-30

## Question tested

Can the finite-dimensional Temperley--Lieb (TL) channels of Brannan--Collins--Lee--Youn provide
the missing fixed finite pair for the Hayden--Penington route: individually controlled at every
tensor power, but with a strictly smaller regularized minimum output entropy for a matched pair?

Primary source:

- Michael Brannan, Benoit Collins, Hun Hee Lee, Sang-Gyun Youn, *Temperley-Lieb quantum
  channels*, arXiv:1810.08001.
- Local copy: `holevo-extensive-violation/artifacts/primary-sources/brannan-collins-lee-youn-1810.08001.pdf`
- SHA-256: `6226ad158cce3e659f8de276438fd4b7ee94cb1820723504f1cb280481edbe24`

## What the paper actually proves

### 1. Single-channel minimum output entropy

Theorem 4.3 gives, for every fixed admissible triple `(l,m,k)`, asymptotically sharp one-shot
minimum-output-entropy estimates as the quantum-group parameter `N` tends to infinity:

```text
((l+m-k)/2) log N - C(N)
  <= H_min(Phi_k^{l,bar m}) = H_min(Phi_k^{bar l,m})
  <= ((l+m-k)/2) log N + D(N),
```

with `C(N),D(N) -> 0`.  These estimates concern a single use of a finite-dimensional channel.
They do not state a bound for `H_min(Phi^{tensor r})` uniform over every tensor degree `r` for one
fixed finite `N`.

### 2. Tensor-product outputs on a specified covariant family

Theorem 6.3 gives an exact spectral decomposition for outputs

```text
(Phi_1 tensor Phi_2)(rho_i^{k1,k2})
```

when the input is one of the paper's covariant states.  Remark 6.4 specializes the formula to the
maximally entangled state.  This is an exact and useful witness calculation, but it is not a global
minimum over every input, and it is not an all-copy formula for a fixed channel.

### 3. The authors' additivity verdict is negative evidence, not a theorem

Section 6.3 explicitly asks whether those covariant outputs could prove strict MOE
subadditivity.  The reported numerical evaluations instead give entropy above the sum of the two
asymptotic one-channel lower bounds, with the excess tending to zero as `N -> infinity`.  The
authors call this strong evidence that the tested TL pairs are not strictly subadditive.  They do
not prove additivity for all inputs, so this cannot be upgraded to a mathematical no-go theorem.

### 4. The capacity statement is also only a coarse regularized bound

Table 1 and Section 5 state a bound of the form `C <= (2+epsilon) chi` for large `N`.  This does not
compute `C`, does not determine the absolute self-regularization loss `C-chi`, and does not show
that this loss is bounded independently of a hierarchy parameter.

## Quantifier audit

The missing object for the current project would need a statement of the form

```text
there exists one fixed finite pair (N,M) such that
  bar_H_min(N) + bar_H_min(M) - bar_H_min(N tensor M) > 0,
```

or at least an all-copy lower bound for each member of a one-shot violating family.  The TL paper
provides instead:

```text
for each fixed channel label, as the ambient parameter N -> infinity,
  the one-shot H_min is asymptotically known,

and for selected two-channel covariant inputs,
  the output spectrum is exactly computable.
```

Neither statement permits exchanging the ambient-dimension limit with the regularization limit.
The paper therefore does not close the self-leakage gate.

## Gate verdict

This candidate route does not yield a finite-dimensional regularized-MOE violation.  It is useful
as a sharply delimited negative lead:

- the channels are finite-dimensional and structured;
- their one-shot MOE is asymptotically controlled;
- their matched entangled outputs are explicitly computable;
- but the available calculation covers neither the global tensor-product minimum nor every tensor
  power of one fixed channel;
- and the numerical evidence in the paper points against, rather than toward, a one-shot
  violation in the tested covariant family.

This is a source-scope obstruction only.  It does not prove that all TL channels are additive or
that no other TL parameter regime can work.

## Next narrower search target

Search for a finite-dimensional channel family with an exact formula for its regularized minimum
output entropy (or a uniform all-copy lower bound) and a separately verified entangled-input upper
bound for a nontrivial pair.  Merely having a one-shot asymptotic estimate plus a distinguished
two-channel spectrum is insufficient.
