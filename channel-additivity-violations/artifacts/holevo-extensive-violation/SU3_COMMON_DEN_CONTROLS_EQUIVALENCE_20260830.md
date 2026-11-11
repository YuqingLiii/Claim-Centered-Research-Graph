# Exact equivalence of the common-denominator Bernstein backend

Date: 2026-08-30

Status: proposer-side tool proof and deterministic regression test; not a channel certificate.

## Purpose

The SU(3) compact certificates repeatedly split dense Bernstein control tensors at the midpoint.
The original implementation stored every control as a normalized Python `Fraction`, forcing a
large-integer gcd after every de Casteljau addition and division.  The replacement stores one
integer numerator per control and one positive common denominator per tensor.

## Exact split identity

Suppose an axis has Bernstein degree `r` and its input controls are `c_i=n_i/D`.  At de
Casteljau level `ell`, every value has the form

\[
 c_i^{(\ell)}
 =\frac{1}{2^\ell D}
 \sum_{j=0}^{\ell}\binom{\ell}{j}n_{i+j}.
\tag{1}
\]

The backend stores every output control over the single denominator `2^r D`.  A left control at
level `ell` therefore uses the integer numerator in (1) multiplied by `2^(r-ell)`; the matching
right control at level `r-ell` is multiplied by `2^ell`.  These are exactly the rational controls
returned by the original midpoint splitter, with no approximation and no change of interval.

## Exact ratio identity

If numerator and denominator control tensors are stored as `n_i/D_n` and `q_i/D_q`, their
projective control ratio is

\[
 \frac{n_i/D_n}{q_i/D_q}=\frac{n_iD_q}{q_iD_n}.
\tag{2}
\]

The replacement compares these integer pairs by cross multiplication, checks the same positivity
and projective-zero conditions, and constructs normalized `Fraction` objects only for the final
minimum and maximum.  Thus it returns exactly the same clamped interval as the original backend.
Control addition uses a common lcm denominator and is exact for the same reason.

## Deterministic regression coverage

`test_su3_common_den_controls.py` uses seeded rational grids in dimensions two, three, and four.
For every axis it verifies exact equality of:

1. conversion to and from the common-denominator representation;
2. every left and right split control;
3. numerator/denominator ratio intervals after each split; and
4. dense control addition.

The test prints:

```text
common-denominator Bernstein controls exactly match Fraction backend
```

A separate non-evidential microbenchmark on 675 controls observed approximately `3.06x` speedup
for one split and `3.70x` over 30 recursive splits.  Performance numbers are machine-specific and
support no mathematical claim.

## Boundary

This tool equivalence does not certify any SU(3) entropy inequality.  A channel node may use the
new backend only after its own complete exact run finishes and records the resulting branches,
boxes, strict margin, command, and transcript.  The four certificate processes already running
when this backend was introduced continue to use the old in-memory `Fraction` implementation.
