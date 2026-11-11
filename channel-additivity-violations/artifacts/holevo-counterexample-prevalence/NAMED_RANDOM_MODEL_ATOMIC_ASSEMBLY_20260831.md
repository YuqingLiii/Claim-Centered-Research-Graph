# Named p=1 random-model atoms and compound assembly

Date: 2026-08-31

Status: proposer-side source interface and assembly. This file is not an independent review and
does not license a completion-level promotion.

## 1. Common quantity and scope

For finite-dimensional channels \(\Phi,\Psi\), write

\[
\Delta_1(\Phi,\Psi)
 =S_{\min}(\Phi)+S_{\min}(\Psi)-S_{\min}(\Phi\otimes\Psi).
\]

Thus \(\Delta_1>0\) is strict nonadditivity of the minimum output von Neumann entropy. Every
named-model statement below concerns this quantity at \(p=1\). None asserts that the same sampled
channels, the same dimensions, or the same probability law have a Holevo-quantity gap. Shor's
universal equivalence is not used in this assembly.

The four imported papers use different probability spaces. “Random channel” is therefore not a
single ensemble shared by the four atoms.

## 2. Frozen primary-source ledger

| Atom | Local primary PDF | SHA-256 | Exact locator |
|---|---|---|---|
| Hastings random-unitary | `primary-sources/hastings-0809.3972.pdf` | `b303560e5794e9b12b7c7f4145b4cd7958a6dd8ab83b61eb7947befca3348b98` | Main-text Eqs. (6)--(11) and Theorem 1, PDF p. 2; Supplemental Eqs. (15)--(22), PDF p. 4 |
| Aubrun--Szarek--Werner random isometry | `primary-sources/asw-1003.4925.pdf` | `f621c6db8d4e442c6c322c8905dec68c6b328acf6862aa18f46ac05a480d2f38` | Channel model Eq. (2) and Theorem 1 with probability convention, PDF pp. 2--3; maximally-entangled upper-bound derivation, PDF p. 4 |
| Belinschi--Collins--Nechita random Stinespring | `primary-sources/bcn-1305.1567.pdf` | `5dd55c810f5bb3b244c6abd234600befd302f35ffd9d5610fa1303d22920b810` | Random-isometry model Eqs. (44)--(51), PDF pp. 17--18; Theorem 5.2, PDF p. 18; Bell witness Eqs. (55)--(56), PDF p. 19; Theorem 6.3 and proof, PDF pp. 20--22 |
| Leung--Lovitz--Wu locally normalized projection | `primary-sources/llw-2607.15210.pdf` | `688f09cb2a6800b4cfe290da80e26e6561b0144493ba94693f518c582164a5e0` | Model Eq. (9), PDF pp. 3--4; Corollary 4.2 and Proposition 5.1, PDF p. 13; Lemma 5.2, Proposition 5.3, and finite-output-dimension numerics, PDF p. 14 |

## 3. Hastings atom: positive probability only

Choose the number \(D\) of random-unitary terms sufficiently large and then choose the system
dimension \(N\), depending on \(D\), sufficiently large. Draw independent \(U_i\) from Haar measure
on \(U(N)\). Independently draw \(l_i\geq0\) with density proportional to
\(l_i^{2N-1}\exp(-NDl_i^2)\), put \(P_i=l_i^2/\sum_jl_j^2\), and define

\[
  \mathcal E(\rho)=\sum_{i=1}^D P_iU_i^\dagger\rho U_i.
\]

Theorem 1 gives strictly positive probability that
\(\Delta_1(\mathcal E,\overline{\mathcal E})>0\). The joint upper bound is obtained from the
maximally entangled input on \(\mathbb C^N\otimes\mathbb C^N\). The theorem does not say that the
probability tends to one in this model. Input and output dimensions are both \(N\); the environment
or Kraus-label size is \(D\).

## 4. Aubrun--Szarek--Werner atom: high probability

For appropriate absolute constants \(c,C>0\), put \(m=\lfloor ck^2\rfloor\) and
\(d=\lfloor Ck^2\rfloor\). Draw a Haar isometry
\(V:\mathbb C^m\to\mathbb C^k\otimes\mathbb C^d\) and let
\(\Phi(\rho)=\operatorname{Tr}_{\mathbb C^d}(V\rho V^\dagger)\). Theorem 1 states that, for large
\(k\),

\[
  \Delta_1(\Phi,\overline\Phi)>0
\]

with large probability. The paper defines this as probability above every fixed preselected
\(\theta\in(0,1)\) once \(k\) is large enough, and records the stronger bound that the exceptional
probability is at most \(\exp(-c'm)\) for an absolute \(c'>0\). The proof uses the maximally
entangled input on the two \(m\)-dimensional inputs to upper-bound the product-channel entropy.
Here the channel has input dimension \(m\), output dimension \(k\), and environment dimension \(d\).

## 5. Belinschi--Collins--Nechita atom: fixed-output Bell criterion

Fix output dimension \(k\). For environment size \(n\), let
\(d_n\sim tkn\) and draw a Haar isometry
\(W_n:\mathbb C^{d_n}\to\mathbb C^k\otimes\mathbb C^n\). Define
\(\Phi_n(X)=({\rm id}\otimes\operatorname{Tr})(W_nXW_n^*)\), pair it with
\(\overline{\Phi_n}\), and test the product channel on the maximally entangled state on
\(\mathbb C^{d_n}\otimes\mathbb C^{d_n}\).

At \(p=1\), Theorems 5.2 and 6.3 and the strict negativity of their limiting Bell entropy
difference imply: for each fixed \(k\geq183\), there is a fixed \(t\in(0,1)\) for which the
probability of \(\Delta_1(\Phi_n,\overline{\Phi_n})>0\) tends to one as \(n\to\infty\). The
appearance of \(k=183\) uses the exact limiting entropy expression together with a finite-range
numerical study. It is a threshold detected by this random-Stinespring/conjugate/Bell test, not a
global minimum dimension. For \(k<183\), the paper excludes only this Bell witness in this model.

## 6. Leung--Lovitz--Wu atom: analytic large-k theorem versus numerical 182

Fix \(k\geq2\), \(t\in(k^{-2},1)\), and let \(P_n\) be a Haar-distributed projection of rank
\(d_n\) in \(\mathbb C^n\otimes\mathbb C^k\), with \(d_n/(nk)\to t\). Put
\(P_{A,n}=\operatorname{Tr}_{\mathbb C^k}P_n\), locally normalize

\[
J_n=(P_{A,n}^{-1/2}\otimes I_k)P_n(P_{A,n}^{-1/2}\otimes I_k),
\]

and let \(\Phi_n:M_n\to M_k\) be the channel with Choi matrix \(J_n\). Pair it with
\(\overline{\Phi_n}\) and use the maximally entangled input on the two \(n\)-dimensional inputs.

For \(p=1\), Lemma 5.2 and Proposition 5.3 analytically show that there is a sufficiently large
output threshold \(k_0\) such that, for every \(k\geq k_0\), some fixed
\(t\in(k^{-2},1)\) satisfies Proposition 5.1's strict Bell criterion. Proposition 5.1 then gives,
almost surely, \(\Delta_1(\Phi_n,\overline{\Phi_n})>0\) for every sufficiently large \(n\).

Separately, the paper defines \(k_{\rm high}(p)\) as the least output dimension detected by this
particular ensemble and Bell-state criterion. High-precision numerical optimization reports
\(k_{\rm high}(1)=182\). The integer 182 is not the analytic conclusion of Proposition 5.3 and is
not a universal threshold over all channels.

## 7. Product-Haar atom

`HCPREV.product-haar-moe-unbounded` already owns the independently reviewed statement that, after
fixing a target gap and then a tensor depth, a specified product-Haar channel/conjugate-channel
model has a larger-than-target \(p=1\) MOE defect with probability tending to one in the per-leg
matrix dimension. This assembly imports that node directly and does not restate or weaken its
quantifier order.

## 8. Exact AND assembly

The compound node `HCPREV.random-models` is the conjunction of the four source atoms above and the
already-proved MOE-only atom `HCPREV.product-haar-moe-unbounded`. The new
`complete-named-model-and-route` has all five narrow nodes as premises. No one-premise route can
establish this compound claim, and the broader Holevo-containing `HCPREV.product-haar-unbounded`
is not load-bearing here.

Logical boundaries:

- Hastings's positive-probability theorem is not upgraded to high probability.
- ASW, BCN, and LLW use distinct ensembles and asymptotic regimes.
- BCN's 183 and LLW's 182 are local Bell-criterion dimensions, not global minima.
- LLW's sufficiently-large-\(k\) result is analytic; its exact 182 value is numerical.
- Every named source atom is MOE-only. No same-law Holevo statement is inferred.
- The product-Haar premise is used with its exact fixed-target/fixed-depth/large-dimension order.

## 9. Review gate

All four new atomic nodes, the five-premise route, and the revised compound parent remain
`CONJECTURED` pending a fresh independent, exact-hash-bound review of the local PDFs, this source
interface, every atomic claim, the route implication, and the compound claim.
