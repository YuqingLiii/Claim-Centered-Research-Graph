# Exact refutation of the naive top-space sign lock

This note records a failed finite-reduction ansatz for the frozen (300\times
300) H4 Bell matrix.  It does not settle the classical upper bound.

## D4-TL1. Ansatz under test

Let

\[
 P=(X+Y\sqrt5)/8
\]

be the exact rank-four Gram matrix and let `ax,by` be the archived classical
sign witness.  The tempting reduction is to assert either

\[
 ax=\operatorname{sign}(Pby)
 \quad\text{or}\quad
 by=\operatorname{sign}(Pax).
\]

If true in a suitably global form, such an identity could reduce the sign
optimization to the central hyperplane arrangement of `range(P)`.

## D4-TL2. Exact countercheck

The checker reconstructs `X,Y` from the frozen integer matrix and evaluates
every coordinate sign in ℚ(√5) using integer comparisons.  It finds:

- `sign(P by)` agrees with `ax` at 257 coordinates, has the opposite sign at
  37 coordinates, and is zero at 6 coordinates;
- `sign(P ax)` agrees with `by` at 254 coordinates, has the opposite sign at
  40 coordinates, and is zero at 6 coordinates;
- in both cases the zero coordinates are
  `168,177,212,232,267,287` in zero-based indexing.

Thus both displayed identities are false on the archived equality witness
itself.  This is an exact counterexample, not a numerical tolerance effect.

## D4-TL3. Consequence for the open proof route

The strict top-space theorem remains valid, but it cannot be completed by
discarding the residual operator and replacing a best response by the sign of
its rank-four projection.  Any spectral proof must control the joint
top/residual sign profile, or introduce an additional lemma that is not
contradicted by D4-TL2.

## Replay

From the repository root, in an environment providing `numpy` and `h5py`:

```bash
python3 grothendieck-d4/tools/h4_top_sign_profile_checker.py \
  grothendieck-d4/artifacts/frozen-instance/d4_n1_300x300.mat
```

The checker also verifies the canonical SHA-256 identity of `A` before
reporting the coordinate counts and indices.
