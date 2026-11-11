# Exact two-hop cut certificate for the 217-coordinate p-gauge

**Mathematical status.**  The Boolean inequality stated below has a complete
exact certificate and a replay checker.  It has not yet received the
independent adversarial review required for a canonical Proof-DAG promotion.
No canonical YAML, index, or graph file is changed by this draft.

## 1. Result

Let `A` be the frozen exact 300 by 300 integer matrix, let `(x,y)` be its
archived sign witness, and put

\[
 p=(x+y)/2,\qquad P=\operatorname{supp}p,\qquad |P|=217.
\]

In the archived gauge define

\[
 M=\operatorname{diag}(p_P)A_{PP}\operatorname{diag}(p_P),
 \qquad L_P=\operatorname{diag}(M\mathbf 1)-M.
\]

The exact path-flow certificate proves

\[
 \boxed{s^TL_Ps\geq 0\quad\hbox{for every }s\in\{\pm1\}^{217}.}
 \tag{1.1}
\]

Moreover equality in (1.1) holds only for the two constant sign vectors.
Equivalently, the archived `p` is, up to global sign, the unique maximizer of
the `p`-quadratic over this fixed support cell.

This closes the `217-cut gate` left open in
`d4-superlevel-cell-reduction-20260830.md`.  Combined with that note's
exact theorem that the archived `q` is, up to global sign, the unique minimizer
on its 83-coordinate support, it gives

\[
 B(p',q')\leq B(p,q)=C
\]

throughout the entire fixed `(217+83)` support cell, with equality only for
independent global signs of `p` and `q`.  In particular there is no fixed-cell
sign counterexample with `B>C`.

## 2. Weighted-cut form

For an unordered edge `e={i,j}`, write

\[
 \delta_e(s)=\mathbf 1[s_i\ne s_j].
\]

The Laplacian identity is

\[
 \frac14s^TL_Ps=\sum_{i<j}M_{ij}\delta_{ij}(s). \tag{2.1}
\]

Partition the nonzero off-diagonal entries of `M` into positive edges
`E_+` of capacity `c_e=M_e` and negative edges `E_-` of demand
`d_{uv}=-M_{uv}`.  Exact reconstruction gives

- 15,066 positive edges;
- 6,294 negative edges; and
- 2,076 zero edges.

The certificate assigns to every negative edge `{u,v}` nonnegative integer
flows `f_{uv,h}` along positive two-hop paths `u-h-v`.  It verifies

\[
 \sum_h f_{uv,h}=d_{uv}                                      \tag{2.2}
\]

for every negative edge, and

\[
 \sum_{(uv,h):e\in\{uh,hv\}} f_{uv,h}<c_e                  \tag{2.3}
\]

for every positive edge.  There are 473,676 nonzero integer path records.
The smallest exact residual capacity in (2.3) is

\[
 95{,}963{,}447{,}132>0.                                  \tag{2.4}
\]

## 3. Why the routing proves the cut inequality

For every two-hop path `u-h-v` and every cut,

\[
 \delta_{uv}\leq\delta_{uh}+\delta_{hv}.                  \tag{3.1}
\]

Let `U_e` be the total routed flow using positive edge `e`.  Equations
(2.2)--(2.3) and (3.1) give

\[
\begin{aligned}
 \sum_{e\in E_+}c_e\delta_e-
 \sum_{uv\in E_-}d_{uv}\delta_{uv}
 &=\sum_{e\in E_+}(c_e-U_e)\delta_e\\
 &\quad+\sum_{uv,h} f_{uv,h}
   (\delta_{uh}+\delta_{hv}-\delta_{uv})\\
 &\geq0.
\end{aligned}                                             \tag{3.2}
\]

This is exactly (2.1), so (1.1) follows without enumeration, floating point,
or an unverified optimization oracle.

Because every residual `c_e-U_e` is strictly positive, equality in (3.2)
forces every positive edge to be uncut.  The checker verifies that the
positive-edge graph is connected, hence equality forces `s` to be constant.

## 4. Durable evidence and replay

Certificate:

`grothendieck-d4/artifacts/certificates/d4-pcut-twohop-flow-certificate-20260830.npz`

Certificate SHA-256:

`1dda1ad4a4d79b370a0a93eb8bd22dad2ce5e87917aad45344db9dad9347253b`

Checker:

`grothendieck-d4/tools/h4_pcut_twohop_checker.py`

Replay from the repository root in an environment containing `numpy` and
`h5py`:

```text
python3 grothendieck-d4/tools/h4_pcut_twohop_checker.py
```

The checker pins the compressed certificate hash, reconstructs `A`, `p`, and
`M` from the frozen instance, rejects malformed path records, verifies all
6,294 demand equalities and all 15,066 capacity inequalities with Python
integers, checks the exact minimum slack, and checks connectivity of the
positive-edge graph.

## 5. Scope audit

- **Exact certificate:** the 217-variable Boolean cut gate (1.1), its strict
  equality classification, and therefore `B<=C` on the fixed `(217+83)`
  support cell when combined with the already checked `q` theorem.
- **Refuted route:** reusing a real PSD/SOS proof for `L_P`; the prior exact
  negative real direction remains valid, but it does not obstruct Boolean
  cut nonnegativity.
- **Still open:** the global classical upper bound outside this fixed support
  cell, and the independent review/promotion of this new certificate into the
  canonical claim graph.
