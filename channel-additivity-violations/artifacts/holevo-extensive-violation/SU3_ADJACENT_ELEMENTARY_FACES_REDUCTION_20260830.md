# Two adjacent elementary SU(3) faces: exact reduction and numerical gate

Date: 2026-08-30

Status: exact structural reduction plus reproducible numerical routing evidence; the all-parameter
entropy inequality is not yet certified.

## Graph and variables

Join the elementary face based at `(p,q)` to the face based at `(p+1,q+1)`. They share one input,
one environment, and their common incidence edge. The union has environment labels

\[
 (p,q),(p+2,q-1),(p+1,q-2),(p+1,q+1),(p+3,q)
\]

and input labels

\[
 (p+1,q),(p+2,q-2),(p,q-1),(p+2,q+1),(p+3,q-1).
\]

The shared input is incident to three environments. Four outer inputs are incident to two
environments each, so the full weight space is one 2-simplex times four intervals.

## Exact convex reduction

The diagonal Gram term of each input block is a positive chi-square quadratic in that block's
edge weights. Every cross term is bilinear in weights from two different input blocks. Therefore
the total Gram parameter is convex in each input block separately.

Retain the two binary weights `u,v` on the two outer inputs of the added face. Maximizing over the
other three input blocks reduces exactly to

\[
 3\cdot2\cdot2=12
\]

endpoint patterns: three vertices of the shared-input simplex and two endpoints for each of the
two original-face outer blocks. For each pattern, the Gram parameter is a quadratic polynomial in
`u,v` with one bilinear term.

The retained highest-weight side distributions are

\[
 q_u=\left(u+\frac{1-u}{p+4},\frac{(1-u)(p+3)}{p+4},0\right)
\]

and

\[
 q_v=(1-v)e_1+v\left(
 \frac1{p+q+5},
 \frac{p+q+4}{(q+1)(p+q+5)},
 \frac{q(p+q+4)}{(q+1)(p+q+5)}
 \right).
\]

Thus it is enough to prove

\[
 B\left(\max_{12\text{ patterns}}t_{\rm pattern}(p,q,u,v)\right)
 >2\min\{H(q_u),H(q_v)\}.
\]

## Numerical gate

The formula scan compactifies `p,q`, uses a `31 x 31` grid away from the projective boundary, and
checks a `101 x 101` grid in `u,v`. The smallest Bell-minus-twice-side margin is approximately
`0.149904828738` bit, at the largest sampled `p`, `q=2`, `u=0.46`, and `v=0.24`. No candidate is
seen.

This is evidence for an exact four-variable rational Bernstein certificate, not a uniform proof.
The projective limits, continuous boxes between grid points, and the qutrit side-entropy interval
bounds remain to be certified.

Reproduction (requires `numpy`):

```sh
<home>/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  holevo-extensive-violation/tools/scan_su3_adjacent_elementary_faces.py
```
