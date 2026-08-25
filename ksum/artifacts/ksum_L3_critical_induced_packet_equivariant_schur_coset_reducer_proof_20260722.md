# Proposer proof: the finite equivariant Schur--coset reducer

Date: 2026-07-22

Controlling node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-rectangular-transfer-resolvent-law`

## 0. Verdict and exact scope

**Proposer verdict: EXACT FINITE FORMULA PASS, pending a fresh independent Rule-7 review.**

At

\[
 (s,a,d,q)=(4,16,17,64),\qquad
 \tau=(61,2)\vdash63,
\]

let

\[
 P=\{(62,2),(61,3),(61,2,1)\}\subset\operatorname{Par}(64).
\]

For either query side `s=L,R`, the common-child filtered equality transfer preserves the
`S_64`-equivariant rectangular coefficient subspace.  On that subspace its exact multiplicity
formula is

\[
 \boxed{
 (\mathcal E_{s,\tau}B)_\mu
 =\frac{64f^\tau}{f^\mu}
  \sum_{\nu\in P}
  A^{1,s}_{\mu\nu}B_\nu A^{0,s}_{\nu\mu}.}
 \tag{0.1}
\]

The factors in parent order `(62,2),(61,3),(61,2,1)` are exactly

\[
 \boxed{\frac{3780}{61},\quad\frac{180}{59},\quad\frac{189}{124}},
 \tag{0.2}
\]

and the carrier-suppressed equivariant coefficient space has dimension

\[
 \boxed{19456}.
 \tag{0.3}
\]

This is a proof of the registered **common-child, finite, equivariant-subspace reducer**.  It is
not a Rule-7 review and licenses no completion-tier DAG status.  In particular, it is not the
literal native transfer: four private point children are missing.  It is not the superoperator on
the full rectangular Hilbert--Schmidt space, and it gives no spectrum, resolvent, optimizer,
attenuation, norm, numerator, uniform-family statement, or exponent.

## 1. Typed setup

Put `G=S_64` and let `K=S_63` be the stabilizer of a reference raw mark `z_0`.  For `t=0` (NO)
and `t=1` (YES), restrict to the three-parent sector and write

\[
 \mathcal H_t^P
 =\bigoplus_{\nu\in P}V_\nu\otimes M_{t,\nu},
 \qquad V_\nu=S^\nu,
 \tag{1.1}
\]

where every non-Specht factor is included in `M_(t,nu)`.  Thus

\[
 \rho_t(g)=\bigoplus_{\nu\in P}\rho_\nu(g)\otimes I_{M_{t,\nu}}.
 \tag{1.2}
\]

The restriction `V_nu downarrow K` is multiplicity-free.  Since every `nu in P` is obtained from
`tau` by adding one box, choose a `K`-equivariant isometry

\[
 J_{\nu\tau}:V_\tau\longrightarrow V_\nu,
 \qquad J_{\nu\tau}^*J_{\nu\tau}=I_{V_\tau}.
 \tag{1.3}
\]

The reviewed common-child fixed-mark effect is `K`-equivariant and supported on the `tau`
isotypic part.  Hence its parent block has the unique form

\[
 Q^{t,s}_{z_0;\tau}[\mu,\nu]
 =J_{\mu\tau}J_{\nu\tau}^*\otimes A^{t,s}_{\mu\nu},
 \tag{1.4}
\]

where

\[
 A^{t,s}_{\mu\nu}:M_{t,\nu}\longrightarrow M_{t,\mu}.
 \tag{1.5}
\]

If the effect is written in a different coherent branching gauge, the phases of the two `J`
maps are absorbed by `A_(mu,nu)`.  They cancel in (0.1), so the reducer is gauge-independent.

An unmarked physical coefficient in the equivariant subspace is precisely a `G`-intertwiner

\[
 B\in\operatorname{Hom}_G(\mathcal H_0^P,\mathcal H_1^P).
 \tag{1.6}
\]

The parent irreducibles are pairwise inequivalent, so Schur's lemma gives

\[
 B=\bigoplus_{\nu\in P}I_{V_\nu}\otimes B_\nu,
 \qquad
 B_\nu:M_{0,\nu}\longrightarrow M_{1,\nu}.
 \tag{1.7}
\]

No NO-to-YES padding or orientation isometry occurs in (1.7): unequal multiplicity dimensions
are allowed because each `B_nu` is rectangular.

## 2. Reference-mark sandwich and the compulsory order

The `(mu,alpha)` parent block of the reference-mark sandwich is

\[
 \begin{aligned}
 (Q^{1,s}_{z_0;\tau}B Q^{0,s}_{z_0;\tau})[\mu,\alpha]
 &=\sum_{\nu\in P}
  (J_{\mu\tau}J_{\nu\tau}^*\otimes A^{1,s}_{\mu\nu})
  (I_{V_\nu}\otimes B_\nu)
  (J_{\nu\tau}J_{\alpha\tau}^*\otimes A^{0,s}_{\nu\alpha})\\
 &=J_{\mu\tau}J_{\alpha\tau}^*\otimes
   \sum_{\nu\in P}A^{1,s}_{\mu\nu}B_\nu A^{0,s}_{\nu\alpha}.
 \end{aligned}
 \tag{2.1}
\]

Here `J_(nu,tau)^* J_(nu,tau)=I_(V_tau)` is the only carrier contraction.  The multiplicity
composition in (2.1), read right to left, is

\[
 M_{0,\alpha}
 \xrightarrow{A^{0,s}_{\nu\alpha}}M_{0,\nu}
 \xrightarrow{B_\nu}M_{1,\nu}
 \xrightarrow{A^{1,s}_{\mu\nu}}M_{1,\mu}.
 \tag{2.2}
\]

Consequently the order `A^1 B A^0` is forced.  It is not a convention.  The rightmost source
effect acts first.  Although self-adjointness implies
`A^(0,s)_(nu,mu)=(A^(0,s)_(mu,nu))^*`, (0.1) uses the actual row-`nu`, column-`mu` block; no
unprinted adjoint or reversal may be inserted.

For the finite dimensions used below, all nine summands have the exact type

\[
 (m_{1,\mu}\times m_{1,\nu})
 (m_{1,\nu}\times m_{0,\nu})
 (m_{0,\nu}\times m_{0,\mu})
 =m_{1,\mu}\times m_{0,\mu}.
 \tag{2.3}
\]

## 3. Exact coset twirl

For every raw mark `z`, choose `g_z in G` with `g_z z_0=z` and set

\[
 Q^{t,s}_{z;\tau}
 =\rho_t(g_z)Q^{t,s}_{z_0;\tau}\rho_t(g_z)^*.
 \tag{3.1}
\]

Because the seed commutes with `rho_t(K)`, (3.1) is independent of the representative.  Define

\[
 \mathcal E_{s,\tau}(B)
 =\sum_{gK\in G/K}Q^{1,s}_{g z_0;\tau}\,B\,Q^{0,s}_{g z_0;\tau}.
 \tag{3.2}
\]

Since `B` is a `G`-intertwiner,

\[
 \rho_1(g)^*B\rho_0(g)=B.
 \tag{3.3}
\]

Thus (3.2) is the correlated coset twirl of the one reference sandwich (2.1); the NO and YES
carriers use the **same** coset representative.  There are not two independent twirls.

For parent labels `mu,alpha in P`, define the carrier sum

\[
 T_{\mu\alpha}
 =\sum_{gK\in G/K}
  \rho_\mu(g)J_{\mu\tau}J_{\alpha\tau}^*\rho_\alpha(g)^*.
 \tag{3.4}
\]

The seed in (3.4) is a `K`-intertwiner.  Therefore the summand is independent of coset
representatives, and left multiplication permutes the cosets; hence

\[
 T_{\mu\alpha}\in\operatorname{Hom}_G(V_\alpha,V_\mu).
 \tag{3.5}
\]

Schur's lemma now gives

\[
 T_{\mu\alpha}=0\quad(\mu\ne\alpha).
 \tag{3.6}
\]

For `mu=alpha`, it is a scalar multiple of `I_(V_mu)`.  Every conjugated projector has rank and
trace `f^tau`, while `|G/K|=64`.  Taking traces fixes the scalar:

\[
 T_{\mu\mu}
 =\frac{64f^\tau}{f^\mu}I_{V_\mu}.
 \tag{3.7}
\]

Combining (2.1), (3.6), and (3.7) shows that the output is again `G`-equivariant and that its
`mu` multiplicity block is exactly (0.1).  The proof is identical for `s=L` and `s=R`; the side
label changes only the finite matrices `A^(t,s)`.

## 4. Exact dimensions and scalar coefficients

The hook-length formula and the multiplicity-free `S_64 downarrow S_63` branching rule give

| partition `lambda` | `f^lambda` |
|---|---:|
| `(61,2)` | `1890` |
| `(62,1)` | `62` |
| `(60,3)` | `37758` |
| `(60,2,1)` | `75579` |
| `(61,1,1)` | `1891` |
| `(62,2)` | `1952` |
| `(61,3)` | `39648` |
| `(61,2,1)` | `79360` |

In particular,

\[
 \begin{aligned}
 1952&=1890+62,\\
 39648&=1890+37758,\\
 79360&=1890+75579+1891.
 \end{aligned}
 \tag{4.1}
\]

Substitution into (3.7) gives

\[
 \begin{aligned}
 \frac{64f^{(61,2)}}{f^{(62,2)}}
 &=\frac{64\cdot1890}{1952}=\frac{3780}{61},\\
 \frac{64f^{(61,2)}}{f^{(61,3)}}
 &=\frac{64\cdot1890}{39648}=\frac{180}{59},\\
 \frac{64f^{(61,2)}}{f^{(61,2,1)}}
 &=\frac{64\cdot1890}{79360}=\frac{189}{124}.
 \end{aligned}
 \tag{4.2}
\]

These are output-parent factors: the coefficient depends on `mu`, not on the summation parent
`nu`.

## 5. Why the reduced coefficient dimension is 19456

The reviewed finite common-child data have a passive occurrence factor of dimension
`dim(Z_L tensor Z_R)=4^2=16`.  Multiplying it by the NO alphabet parent multiplicities
`(1,3,6)` and YES multiplicities `(1,5,10)` gives

\[
 (m_{0,\nu})_{\nu\in P}=(16,48,96),\qquad
 (m_{1,\nu})_{\nu\in P}=(16,80,160).
 \tag{5.1}
\]

By (1.7), carrier suppression means the exact canonical identification

\[
 \operatorname{Hom}_G(\mathcal H_0^P,\mathcal H_1^P)
 \cong\bigoplus_{\nu\in P}\operatorname{Hom}(M_{0,\nu},M_{1,\nu}).
 \tag{5.2}
\]

It follows that

\[
 \begin{aligned}
 \dim\operatorname{Hom}_G(\mathcal H_0^P,\mathcal H_1^P)
 &=16\cdot16+48\cdot80+96\cdot160\\
 &=256+3840+15360\\
 &=\boxed{19456}.
 \end{aligned}
 \tag{5.3}
\]

This number is not the dimension of the full native rectangular space
`Hom(H_0^P,H_1^P)`.  It is exactly the dimension of its `G`-intertwiner subspace.

## 6. Carrier suppression: exact meaning and strict boundary

The reduction is exact on `Hom_G`, not an approximate deletion of Specht carriers.  Equivalently,
it is the trivial `G`-type for the natural conjugation action on rectangular coefficients.  The
coset twirl maps this subspace to itself, and (0.1) computes that restriction without constructing
a full Clebsch--Gordan/Racah/Wigner table.

Three boundaries are load-bearing.

1. **Common child versus literal effect.**  The three parents restrict to five point children:
   `(61,2),(62,1),(60,3),(60,2,1),(61,1,1)`.  For equivariant `B`, different intermediate
   children are orthogonal, so the full equivariant transfer is a sum of same-child reducers.
   Formula (0.1) is only the `(61,2)` summand.  The other four physical fixed-mark effects are
   still required.
2. **Equivariant coefficients versus full Hilbert--Schmidt space.**  A general rectangular map
   has carrier components in `V_mu tensor V_nu^*`, including nontrivial `G`-types and off-diagonal
   parents.  Cross-child pairs can survive there.  Computing the correlated coset action on those
   modes needs the carrier/Wigner kernel or an exact direct 64-term carrier sum.  Equation (3.7),
   which is only the trivial Schur block, cannot determine that kernel.
3. **Filtered diagnostic versus native transfer.**  Even an exact spectrum of (0.1) would be only
   a finite diagnostic for one child and one invariant subspace.  It cannot be reported as the
   spectrum, kernel, resolvent, or feasibility of the full native transfer.

In particular, neither `64` times one fixed-mark sandwich nor independent NO and YES averages can
replace the correlated twirl (3.2).

## 7. Exact symbolic checker

The proposer checker is

`ksum/tools/ksum_l3_equivariant_schur_coset_reducer_check.py`, SHA-256
`418FDE6FCEB6DC0D80A23C449861F256BD8EE44BF9CE9317548DD47350D892F5`.

It was run as

```text
python ksum/tools/ksum_l3_equivariant_schur_coset_reducer_check.py --output ksum/artifacts/logs_ksum_L3_equivariant_schur_coset_reducer_20260722/run.json --log ksum/artifacts/logs_ksum_L3_equivariant_schur_coset_reducer_20260722/run.log
```

The exact JSON is
`ksum/artifacts/logs_ksum_L3_equivariant_schur_coset_reducer_20260722/run.json`, SHA-256
`DBC19C6E51AE40B2FDCE2BFFD75E31F794F1CA34B33C5569F53F65269AE813F9`.
The concise log is
`ksum/artifacts/logs_ksum_L3_equivariant_schur_coset_reducer_20260722/run.log`, SHA-256
`C5D4BF94D7FCEA1AED70F944D04F9CCD9B0694DCF88C643AF3A2071053FC6F59`.
The run prints

```text
ALL_EQUIVARIANT_SCHUR_COSET_REDUCER_GATES_PASS
coefficients=3780/61,180/59,189/124
coefficient_space_dimension=19456
toy_direct_residual_rank=0
toy_wrong_order_residual_rank=8
```

The checker independently applies the hook-length formula, enumerates every removable corner,
checks all three branching dimension sums, reduces the three fractions, and audits all nine Hom
compositions with the unequal finite dimensions in (5.1).

It also constructs an exact `S_4/S_3` coset model.  The trivial and standard `S_4` parents share
the trivial `S_3` child; the four-term carrier twirl gives the exact factors `4` and `4/3` and
kills the two cross-parent carrier blocks.  Positive-semidefinite reference effects with
noncommuting `2 by 2` multiplicity blocks are then twirled directly.  The residual of the printed
`A^1 B A^0` formula has rank zero, while an accidentally typed reversed-order formula has residual
rank eight.

This toy gate exercises the printed coset formula and order, not an independent construction of
the physical k-Sum matrices.  The physical common-child matrices remain inputs from their
separately reviewed assembly.

## 8. Frozen input scope

This proof uses the following prior results only at their reviewed finite scope:

* `ksum/artifacts/ksum_L3_critical_induced_packet_direct_coset_cross_side_factorization_rule7_review_20260722.md`,
  SHA-256 `C3A7DFD24286F6C74A111DD01981D284E9A17F08B10E007766AC22AF0DDDECEB`,
  for native unequal-answer typing and exact marked covariance;
* `ksum/artifacts/ksum_L3_critical_induced_packet_first_target_yes_physical_central_transfer_decision_a16_rule7_review_20260722.md`,
  SHA-256 `A2DA44F5BE33F73CB4C84F4AD8C586F8AC7407C6E57059D4E3C764816B965052`,
  for the finite common-child effects, exact five-child inventory, and the fact that the common
  block does not determine the literal transfer;
* the reviewed NO and YES parent multiplicities and occurrence dimension already cited by that
  assembly review.

The earlier planning artifact
`ksum/artifacts/ksum_L3_critical_induced_packet_rectangular_transfer_scope_audit_20260722.md`, SHA-256
`0E1BF0D0B471182BF11AB00CD170F9DF9EF5DF8EBA02EDF215DF965B3B94FB86`,
registered the candidate formula but was not treated as proof evidence.  The derivation above is
self-contained.

## 9. Review commission boundary

A fresh reviewer must independently reconstruct the coset-intertwiner argument before reading
this derivation; audit every displayed domain and codomain, both `s=L,R`, all three output parents,
all nine unequal Hom compositions, the normalization `|G/K| f^tau/f^mu`, and the distinction
between formula verification and physical-value verification.  The review must explicitly attack
dropped/extra normalization, source-side order reversal, independent rather than correlated
twirls, parent pinching, common-child/full-effect conflation, carrier-suppressed/full-HS dimension
conflation, and any attempt to infer a spectrum or exponent.

Until that independent review is archived, the strict license is only: **proposer proof and exact
finite gates completed; canonical node remains OPEN.**
