# The environment-centered triangular SU(3) three-face cluster has no Bell gap

Date: 2026-08-30

Status: proposer-side all-parameter theorem with an exact rational Bernstein/logarithm
certificate; independent review pending.

For the face-base cluster `((-2,1),(-1,2),(0,0))`, the union has six input vertices, seven
environment vertices, and 15 distinct incidence edges. Retain the binary original input block at
offset `(0,2)` and the ternary original input block at `(1,0)`. Their three coordinates
parameterize one interval and one simplex. Separate convexity reduces the other two binary and two
ternary blocks to `2^2*3^2=36` Gram endpoint branches without modifying either retained side
output.

Let `P,Q>=0` be the residual labels above the smallest admissible base. For every environment
label `(r,s)`, its dimension factors are `(r+1)(s+1)(r+s+2)/2`. A common positive Gram denominator
is eight times the total input dimension times the product of the distinct linear factors appearing
in all seven environment dimensions. This cancels every local `chi^2` and common-environment cross
denominator. Its degrees in `P,Q` are `(12,12)` after the total input factor is included.

The checker reconstructs each cleared numerator by exact tensor Lagrange interpolation with
`Fraction` and verifies it at two additional rational points. The 36 Gram branches have degree
tuple `(12,12,2,2,2)`. The two retained side distributions use a common positive denominator and
have degree tuple `(4,4,1,1,1)`; they too pass an extra rational-point identity check.

Compactify `P,Q` to `P/(P+1),Q/(Q+1)`. Exact multivariate Bernstein control-point ratios and
rational de Casteljau subdivision upper-bound every Gram branch and retained side entropy, while
rational logarithm intervals lower-bound the isotropic Bell entropy. The checker certifies 2,263
adaptive five-dimensional boxes. Its smallest certified natural-log margin is greater than

\[
 1.915664030824\times10^{-4}.
\]

Therefore every channel in this environment-centered triangular family satisfies the Bell-route
no-gap inequality. This theorem does not cover the input-centered triangular orientation, chain
clusters, non-Bell inputs, or noncovariant channels.

Reproduction:

```sh
python3 holevo-extensive-violation/tools/certify_su3_triangular_three_face_clusters.py
```
