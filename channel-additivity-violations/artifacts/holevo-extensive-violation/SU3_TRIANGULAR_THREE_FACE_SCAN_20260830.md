# Formula scan for the two triangular SU(3) three-face clusters

Date: 2026-08-30

Status: reproducible numerical candidate filter; not an all-parameter proof.

The scanner constructs the complete labelled bipartite union for each of the two triangular
orientation classes. For every input vertex it samples its full incident-edge probability
simplex. It evaluates

1. the exact dimension-weighted local `chi^2` Gram contributions;
2. every pairwise cross term at each common environment vertex;
3. the isotropic conjugate-Bell entropy determined by the resulting Gram parameter; and
4. every block-highest explicit side-output entropy.

Before scanning, the generic union formula is checked against the established single elementary
face formula and the canonical two-face formula at fixed nontrivial parameter points; both agree
to tolerance `1e-12`.

For each orientation, the run used 120,000 mixed Dirichlet samples at each of 49 label pairs. The
offset grid was `(0,1,2,4,8,16,32)` above the smallest admissible `p` and `q`. Half the samples used
Dirichlet parameter one and half used parameter `0.15` to cover both interiors and near-corners.
The random seed was `20260830`.

Results:

- seven-input/six-environment triangle: smallest sampled
  `Bell - 2 min(side) = 0.36323259665301677` bit;
- six-input/seven-environment triangle: smallest sampled
  `Bell - 2 min(side) = 0.5397143354011438` bit.

No sampled candidate survived the explicit block-highest side filter. This supports a no-go
conjecture but does not control unsampled weights, all integer labels, or the global minimum output
entropy. An exact proof still requires a correlation-preserving convex reduction or a compact
multivariate certificate.

The scan also tested fixed subsets of side blocks, which is the relevant dimensional-reduction
question. For the seven-input/six-environment orientation, no fixed one- or two-block cover had a
positive sampled worst margin. The best fixed three-block cover uses input offsets
`(-1,1),(1,0),(2,-2)` and has sampled worst margin `0.162723789533` bit. Retaining those three
binary weights and applying separate convexity to the remaining three binary blocks and one
ternary block produces exactly `2^3*3=24` Gram endpoint branches in five variables.

For the six-input/seven-environment orientation, the binary offset `(0,2)` alone has a small
positive sampled worst margin, but the more robust fixed pair `(0,2),(1,0)` has margin
`0.142152526875` bit. The second block is ternary. Eliminating the other two binary and two ternary
blocks produces `2^2*3^2=36` endpoint branches, again in five variables. These are candidate exact
reductions, not consequences of the numerical scan.

Reproduction uses the bundled NumPy runtime:

```sh
<home>/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  holevo-extensive-violation/tools/scan_su3_triangular_three_face_clusters.py
```
