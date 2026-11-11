# Multiplicative entropy bounds cannot amplify a conjugate-pair witness

Date: 2026-08-29  
Scope: finite-dimensional minimum output von Neumann entropy (`p=1`)

## Claim

Let `F` be a channel functional with

1. `Smin(L) >= F(L)` for every channel in scope; and
2. `F(L tensor K) = F(L) + F(K)` for the pair under consideration and all of its tensor powers.

Then no product-of-copies witness for `L tensor K` can combine with `F` to certify a positive
linear tensor-copy defect. More explicitly, for every input state `rho` to `L tensor K`,

```text
S((L tensor K)(rho)) >= F(L) + F(K).
```

Consequently the standard proposed coefficient

```text
F(L) + F(K) - S((L tensor K)(rho))
```

is always nonpositive.

This is a no-go statement about a proof method. It does not imply that the true regularized
pair defect vanishes.

## Proof

The two assumptions give

```text
S((L tensor K)(rho))
  >= Smin(L tensor K)
  >= F(L tensor K)
   = F(L) + F(K).
```

For `r` copies, the product witness `rho^(tensor r)` gives

```text
Smin((L tensor K)^(tensor r))
  <= r S((L tensor K)(rho)),
```

while the same lower bound gives

```text
Smin(L^(tensor r)) >= r F(L),
Smin(K^(tensor r)) >= r F(K).
```

Subtracting these bounds produces only

```text
Delta_r(L,K)
  >= r [F(L)+F(K)-S((L tensor K)(rho))] <= 0.
```

The final inequality concerns the proposed lower-bound coefficient, not the unknown true value of
`Delta_r`.

## Application to Fukuda--Nechita additivity-rate bounds

Fukuda and Nechita define five channel quantities `B_i(L)` and prove in Lemma 4.2 that each
individual `B_i` is multiplicative under tensor products. Proposition 4.4 gives, for the relevant
Rényi entropies, additive lower bounds of the form

```text
F_i(L) = -log2 B_i(L).
```

For von Neumann entropy one may use the `p=2` bounds because `H_1 >= H_2`. Thus each fixed
choice of `i` satisfies the hypotheses above.

For a conjugate pair `L, conjugate(L)`, complex conjugation preserves all five operator norms.
Hence the best index is the same on both sides. Choosing a different index cannot improve either
side, and the minimum-over-indices additivity-rate bound reduces to one common multiplicative
functional. It follows that these bounds cannot certify a positive tensor-copy coefficient for a
conjugate-pair Bell witness.

In the random-channel notation of Fukuda--Nechita, the attempted coefficient based on the
partially-transposed Choi bound is

```text
-2 log2 ||C_L^Gamma|| - H((L tensor conjugate(L))(Bell)).
```

It is nonpositive identically, not merely in the large-dimension limit, because Proposition 4.4
applied to `L tensor conjugate(L)` lower-bounds every joint output entropy by the first term.
This explains the negative numerical scans without relying on them.

## What remains viable

The argument does not rule out:

- a genuinely non-additive lower bound that controls each side's regularization but does not also
  lower-bound the matched joint witness by the sum;
- a heterogeneous pair whose two strongest tensor-stable lower bounds come from different
  functionals, provided their sum can be proved larger than a joint witness entropy; or
- the fixed-partner hierarchy, which seeks asymptotically vanishing cross leakage rather than a
  common multiplicative certificate.

## Primary source

Motohisa Fukuda and Ion Nechita, *Additivity rates and PPT property for random quantum
channels*, arXiv:1411.6881, especially Lemma 4.2, Proposition 4.4, Proposition 4.6, and
Theorem 8.4.

