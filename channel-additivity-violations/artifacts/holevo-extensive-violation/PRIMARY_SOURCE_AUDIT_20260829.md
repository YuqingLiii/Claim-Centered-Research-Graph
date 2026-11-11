# Primary-source audit: one-bit, unbounded and extensive additivity gaps

Date: 2026-08-29

Scope: bind the known near-one-bit result, the quantitative MOE-to-Holevo extension, the
Hayden--Penington definition/dichotomy, and the fixed-partner obstruction to local primary PDFs.
This is a proposer-side audit, not an independent completion review.

**Post-audit project advance.** The literature-status statement below remains an accurate report
of what this audit found in the cited papers, but it is no longer the project's best mathematical
lower bound. A subsequent local synthesis of Collins--Youn arXiv:1907.07856 and
Bordenave--Collins arXiv:2304.05714 gives a proposer-side proof of finite-dimensional absolute-
unbounded `p=1` gaps; see `FINITE_DIMENSIONAL_UNBOUNDED_GAP_PROOF_20260829.md`. Full-size
extensivity remains open.

## Source ledger

| Source | Local file | SHA-256 | Relevant location |
|---|---|---|---|
| S. T. Belinschi, B. Collins and I. Nechita, *Almost one bit violation for the additivity of the minimum output entropy*, arXiv:1305.1567v3 | `primary-sources/bcn-1305.1567.pdf` | `5dd55c810f5bb3b244c6abd234600befd302f35ffd9d5610fa1303d22920b810` | Theorem 6.3 and remarks, PDF pp. 20-21 |
| M. Fukuda, *Simplification of additivity conjecture in quantum information theory*, arXiv:1307.0707 | `primary-sources/fukuda-1307.0707.pdf` | `bbb6248128249479273ae62d697f7e7db9043af851b4f77a7428dffac485e917` | Theorem 6.1 and Lemma 6.2, PDF pp. 11-12 |
| P. Hayden and G. Penington, *Black hole microstates vs the additivity conjectures*, arXiv:2012.07861v1 | `primary-sources/hayden-penington-2012.07861.pdf` | `e461f61e89bed46791974a6b2334e3aefb09d7824849b0f615744c1108397b21` | Possibilities 1/2, PDF pp. 2-3; quantitative definition Eq. (11), PDF p. 7 |
| B. Collins, M. Fukuda and I. Nechita, *On the convergence of output sets of quantum channels*, arXiv:1311.7571 | `primary-sources/cfn-1311.7571.pdf` | `c7303b21362b7e5c1c1b13b3bc224f1d69332189a384f7ee12e791f6d4420bdb` | Proposition 4.2, PDF p. 9; Theorem 8.1 and following discussion, PDF p. 18 |
| G. Gour and N. R. Wallach, *Entanglement of subspaces and error correcting codes*, arXiv:0704.0251 | `primary-sources/gour-wallach-0704.0251.pdf` | `9cb7343ae61aaa571060cebcd1011e0cd2ac31acbfae5fe4b14edf8d75997795` | Proposition 2, PDF p. 2 |
| A. Montanaro, *Weak Multiplicativity for Random Quantum Channels*, arXiv:1112.5271 | `primary-sources/montanaro-1112.5271.pdf` | `5412752f50f7c5690eddc9dd279840710a09db6b72d326f4f2b36d1a69869ee6` | Theorem 3 and von Neumann discussion, PDF pp. 4-5; precise estimates later in the paper |
| M. Fukuda and M. M. Wolf, *Simplifying additivity problems using direct sum constructions*, arXiv:0704.1092v2 | `primary-sources/fukuda-wolf-0704.1092.pdf` | `1a8890f8484d450894545190d306efd67b57ee7f646fc45be1e4a26fe6b653b7` | Proposition 1(4), statement on PDF p. 1 and proof on PDF p. 2; Proposition 2(2), PDF p. 3 |
| K. M. R. Audenaert, *A Sharp Fannes-type Inequality for the von Neumann Entropy*, arXiv:quant-ph/0610146 | `primary-sources/audenaert-0610146.pdf` | `dc2265209fd7fb86aa7ce03a541c15d8b9f5a29b70c281728650eef0ad87bdb7` | Theorem 1, PDF p. 2 |
| M. Kalantar and H. Shobeiri, *More examples of additivity violation of the regularized minimum output entropy in the commuting-operator setup*, arXiv:2501.15462 | `primary-sources/kalantar-shobeiri-2501.15462.pdf` | `a2237d7b2383baed55a9f38e93ae5800c172b927bd968f24ec8e7c8e4be4db20` | finite-dimensional status, PDF p. 1; commuting-operator Theorem 3 |
| M. Magee and M. de la Salle, *Strong asymptotic freeness of Haar unitaries in quasi-exponential dimensional representations*, arXiv:2409.03626v2 | `primary-sources/magee-de-la-salle-2409.03626.pdf` | `873d0bd1d874635ef75b092185c044c0e051f927eb5747a5bedfc86495a7d589` | Theorem 1.1 and Corollary 1.2, PDF pp. 3-5 |
| D. Leung, B. Lovitz and P. Wu, *Counterexamples to additivity of minimum output p-Renyi entropy of quantum channels for all p>3/4 and 0<=p<1/4*, arXiv:2607.15210v1 | `primary-sources/leung-lovitz-wu-2607.15210.pdf` | `688f09cb2a6800b4cfe290da80e26e6561b0144493ba94693f518c582164a5e0` | Theorem 3.1 and Corollary 3.2, PDF pp. 8-9; Theorem 4.1 and Corollary 4.2, PDF pp. 11-12 |

Online records: <https://arxiv.org/abs/1305.1567>, <https://arxiv.org/abs/1307.0707>,
<https://arxiv.org/abs/2012.07861>, <https://arxiv.org/abs/1311.7571>,
<https://arxiv.org/abs/0704.0251>, <https://arxiv.org/abs/1112.5271>,
<https://arxiv.org/abs/0704.1092>, <https://arxiv.org/abs/quant-ph/0610146>,
<https://arxiv.org/abs/2501.15462>, and <https://arxiv.org/abs/2409.03626>.
The 2026 projection-induced update is <https://arxiv.org/abs/2607.15210>.

## What is established near one bit

BCN Theorem 6.3 is a finite-output-dimension, random-Stinespring, conjugate-channel/Bell-witness
result. For every output dimension `k >= 183`, after choosing an appropriate parameter and taking
the auxiliary dimension limit, almost all sampled channels violate von Neumann minimum-output-
entropy additivity. As `k` grows, the certified lower bound can be made arbitrarily close to
`log_2 2 = 1` bit.

The paper explicitly contrasts this with the `p>1` Renyi setting: at `p=1` its violations are
bounded and approach one bit in this construction. This is a lower-bound construction, not a
universal one-bit upper bound for all channels.

## Exact quantitative transfer to Holevo

Fukuda Lemma 6.2 takes channels with output dimensions `k,k'` and constructs Weyl-flag extensions
whose Holevo quantities satisfy, for every nonnegative pair of tensor exponents `m,n`,

`chi(tilde(Phi)^m tensor tilde(Omega)^n)`

`= log_2(k^m (k')^n) - S_min(Phi^m tensor Omega^n)`.

Subtracting the cases `(1,0)` and `(0,1)` from `(1,1)` transfers a minimum-output-entropy pair gap
exactly, with no additive loss, to the Holevo pair gap of the extension channels. The construction
changes the channels. It does not assert that the original BCN random pair itself is Holevo-
nonadditive.

The extension maps an input of dimension `k^2 l` to output dimension `k` when the original map is
`L(C^l) -> L(C^k)`. Hence logarithmic input/output size changes only by a constant-factor linear
overhead, so an `Omega(m)` MOE family would remain `Omega(m)` after this transfer.

## Hayden--Penington target and dichotomy

Hayden--Penington define the extensive alternative using two sequences of finite-dimensional
channels. The input and output Hilbert spaces grow linearly in `n` when measured in qubits, while

`Delta_n = S_min(N_1^(n))+S_min(N_2^(n))-S_min(N_1^(n) tensor N_2^(n)) >= C n`

for a constant `C>0`; this is their Eq. (11). Their main conclusion is a nonexclusive disjunction:

1. such extensive violations exist; or
2. large AdS/CFT black holes have an almost-basis of approximately `exp(S_BH-O(1))`
   “disentangled” microstates, subject to the paper's holographic/semiclassical framework.

They do not select the first branch and do not construct an unconditional finite-dimensional
extensive counterexample. The phrase “disentangled” denotes a leading-order entanglement deficit,
not a product state.

Here the superscript `(n)` labels a growing channel family; it is not a tensor-power exponent.
Tensor powers of one fixed one-shot counterexample do not automatically satisfy Eq. (11), because
the two side minimum output entropies can each self-regularize. The exact leakage identities are
recorded separately in `TENSOR_COPY_LEAKAGE_PROOF_20260829.md`.

The paper states the size condition using input and output Hilbert spaces in qubit units. If a
project calculation also records the **minimal** Stinespring environment, this changes the cost by
at most a factor of two: the minimal environment dimension is the Choi rank and obeys
`dim E_min <= dim A * dim B`, hence

`log dim A + log dim B <= log dim A + log dim B + log dim E_min`

`<= 2(log dim A + log dim B)`.

An arbitrarily padded nonminimal environment is not part of the Hayden--Penington size measure.

## Fixed-partner gate

CFN Theorem 8.1 shows that tensoring its random sequence with any fixed finite-dimensional channel
has a deterministic limiting convex output body under the stated strong-convergence hypothesis.
Proposition 4.2 transfers output-set convergence to minimum output entropy and Holevo quantity.
Thus a fixed partner has a deterministic limiting defect, but CFN immediately warns that the
general limiting body is difficult to analyze even for the identity partner. The theorem does not
identify the limiting defect as zero.

Gour--Wallach Proposition 2 supplies only a constant dimensional loss
`log min(dim U,dim V)` for the corresponding entangled-subspace quantity. With a fixed partner this
uniformly bounds the possible defect, but does not force it to vanish.

Montanaro's weak multiplicativity theorem gives a uniform-in-tensor-power lower bound with a
constant per-copy loss (and in the BCN near-one-bit parameter regime a substantially coarser
dimension-dependent allowance). It does not yield the sublinear self-leakage required by the
tensor-copy amplification inequality.

## Literature-status boundary

The bound “arbitrarily close to one bit” is established. No primary source in the migrated and
date-bounded search establishes a finite-dimensional `p=1` defect greater than one bit, unbounded
absolute defect, or Hayden--Penington-size `Omega(log d)` defect. This is an audit status as of
2026-08-29, not a theorem that larger violations are impossible.

The source search was extended on 2026-08-30. Kalantar--Shobeiri still describe the
finite-dimensional regularized-MOE additivity problem as completely open and work in the
infinite-dimensional commuting-operator setup. Magee--de la Salle control representation degrees
up to `n^A` as `n -> infinity`; this does not supply one fixed finite-dimensional channel controlled
at every tensor exponent. The exact quantifier and representation mismatch is recorded in
`FINITE_REGULARIZED_MOE_LITERATURE_GATE_20260830.md`.

LLW's 2026 paper was also checked at the nonuniform boundary scaling omitted by its fixed-`t`
large-`k` expansion. For `t_k=c/k^2`, the exact output body contains a one-channel spectrum whose
spike cancels the Bell output's apparent `log k` advantage, leaving at most `h_2(1/c)<=1` bit in
that certificate. See `LLW_CRITICAL_SCALING_ONE_BIT_GATE_20260830.md`. This is a mechanism-specific
upper bound, not a universal one-bit theorem for arbitrary channels or inputs.

A subsequent elementary steering argument closes all other LLW boundary scalings. For any exact
isotropic channel/conjugate-channel Bell output, measuring one output leg produces a legal
one-channel output. The two resulting spike spectra obey an exact scalar entropy inequality that
caps the Bell certificate by one bit. Passing through LLW's fixed-`k,t` output-set convergence
therefore gives a bound uniform in every admissible `k,t`, including arbitrary sequences `t=t_k`.
See `ISOTROPIC_BELL_ONE_BIT_CAP_20260830.md`. The theorem is universal for the isotropic Bell
mechanism, but not for non-isotropic optimized inputs or general channel pairs.

## Review status

The main external statements are now locally hashed and page-bound. The local quantitative
transfer and tensor-copy calculations remain proposer-side until independently reviewed.
