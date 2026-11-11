# Primary-source audit: prevalence of p=1 additivity counterexamples

Date: 2026-08-29

Scope: separate six different meanings of “many counterexamples”: deterministic existence,
probability in a named random model, relative openness, intrinsic measure, density/genericity, and
explicit low-dimensional witnesses. This is a proposer-side audit, not an independent completion
review.

**Post-audit project advance.** A later local synthesis adds a product-Haar model in which, for
every fixed target gap, finite-dimensional gaps above that target occur with probability tending to
one after fixing a sufficiently large product depth. See
`PRODUCT_HAAR_UNBOUNDED_PREVALENCE_PROOF_20260829.md`. This does not alter the whole-CPTP-space
genericity or deterministic-explicitness caveats below.

## Source ledger

| Source | Local file | SHA-256 | Relevant location |
|---|---|---|---|
| K. M. R. Audenaert, *A Sharp Fannes-type Inequality for the von Neumann Entropy*, arXiv:quant-ph/0610146 | `primary-sources/audenaert-0610146.pdf` | `dc2265209fd7fb86aa7ce03a541c15d8b9f5a29b70c281728650eef0ad87bdb7` | Theorem 1, PDF p. 2 |
| P. W. Shor, *Additivity of the Classical Capacity of Entanglement-Breaking Quantum Channels*, arXiv:quant-ph/0201149v3 | `primary-sources/shor-eb-0201149.pdf` | `9e68b70e36383ceb42dbbfbd3cefdbad0d5757ee76941f1d590b6c15cefcbca4` | Theorems 1 and 2, PDF pp. 2 and 4 |
| L. Gurvits and H. Barnum, *Largest separable balls around the maximally mixed bipartite quantum state*, arXiv:quant-ph/0204159 | `primary-sources/gurvits-barnum-0204159.pdf` | `c35027eb1e981bf70b2767c229daac7812d3226773ad5d0f7a7a335c363adf85` | Theorem 1 and Corollary 3, PDF pp. 4-5 |
| M. B. Hastings, *Superadditivity of communication capacity using entangled inputs*, arXiv:0809.3972v4 | `primary-sources/hastings-0809.3972.pdf` | `b303560e5794e9b12b7c7f4145b4cd7958a6dd8ab83b61eb7947befca3348b98` | Theorem 1, PDF p. 2 |
| G. Aubrun, S. Szarek and E. Werner, *Hastings's additivity counterexample via Dvoretzky's theorem*, arXiv:1003.4925v2 | `primary-sources/asw-1003.4925.pdf` | `f621c6db8d4e442c6c322c8905dec68c6b328acf6862aa18f46ac05a480d2f38` | Theorem 1 and its probability convention, PDF p. 3 |
| S. T. Belinschi, B. Collins and I. Nechita, *Almost one bit violation for the additivity of the minimum output entropy*, arXiv:1305.1567v3 | `primary-sources/bcn-1305.1567.pdf` | `5dd55c810f5bb3b244c6abd234600befd302f35ffd9d5610fa1303d22920b810` | Theorem 6.3 and remarks, PDF pp. 20-21 |
| D. Leung, B. Lovitz and P. Wu, *Counterexamples to additivity of minimum output p-Renyi entropy of quantum channels for all p > 3/4 and 0 <= p < 1/4*, arXiv:2607.15210v1 | `primary-sources/llw-2607.15210.pdf` | `688f09cb2a6800b4cfe290da80e26e6561b0144493ba94693f518c582164a5e0` | Introduction, PDF p. 2; Proposition 5.1 and Proposition 5.3, PDF pp. 13-14 |
| P. W. Shor, *Equivalence of Additivity Questions in Quantum Information Theory*, arXiv:quant-ph/0305035 | `primary-sources/shor-quant-ph-0305035.pdf` | `300a97664fe8d05531230cd6f3a812b23e2c2cbf22c429436e50442993f415d6` | Theorem 1, PDF pp. 5-6 |

Online records: <https://arxiv.org/abs/quant-ph/0610146>,
<https://arxiv.org/abs/quant-ph/0201149>, <https://arxiv.org/abs/quant-ph/0204159>,
<https://arxiv.org/abs/0809.3972>, <https://arxiv.org/abs/1003.4925>,
<https://arxiv.org/abs/1305.1567>, <https://arxiv.org/abs/2607.15210>, and
<https://arxiv.org/abs/quant-ph/0305035>.

## Random-model quantifiers

The primary papers support the following distinct statements.

1. **Hastings:** after choosing sufficiently large finite random-unitary parameters, the event
   `S_min(E tensor Ebar) < S_min(E) + S_min(Ebar)` has nonzero probability. This yields a
   deterministic finite-dimensional pair by the probabilistic method.
2. **Aubrun--Szarek--Werner:** for output dimension `k`, input dimension `m = c k^2`, and
   environment dimension `d = C k^2` in their random-isometry model, the same conjugate-pair
   inequality holds “with large probability” for sufficiently large `k`. They define this as
   probability greater than any fixed preselected `theta in (0,1)` once `k` is large enough, and
   state the stronger exceptional-probability estimate `exp(-c' m)`.
3. **Belinschi--Collins--Nechita:** in their random-Stinespring asymptotic model, for every fixed
   output dimension `k >= 183` there are parameter values for which almost all channels violate
   minimum-output-entropy additivity using the conjugate channel and Bell input as `n -> infinity`.
4. **Leung--Lovitz--Wu:** in a different locally normalized Haar-projection model, Proposition 5.1
   says that for fixed `k,t,p` satisfying its strict Bell criterion, almost surely the pair
   `Phi_n, bar(Phi_n)` violates for every sufficiently large `n`. Proposition 5.3 proves that an
   appropriate criterion exists for every finite `p > 3/4`, including `p=1`.

These are not probability statements with respect to a canonical “uniform distribution on all
channels.” Each probability is attached to its construction, dimensions, parameter scaling,
conjugate partner and chosen witness.

## Dimension-threshold quantifiers

The two nearby numbers have narrower meanings than “smallest possible counterexample.”

- In BCN Theorem 6.3, `183` is the first output dimension found by the paper's
  random-Stinespring/conjugate-channel/Bell-state asymptotic criterion. Its proof explicitly uses a
  numerical study for the finite range `183,...,276`. For `k < 183`, the paper proves only that
  this Bell-state test does not exhibit a violation in that model; it does not exclude different
  inputs or different channels.
- LLW defines `k_high(p)` to be the smallest output dimension *detected by its present ensemble and
  Bell witness* and explicitly says it is not a universal threshold. The displayed value
  `k_high(1)=182` comes from “high-precision numerical optimization,” whereas Proposition 5.3 is the
  analytic sufficiently-large-`k` existence result.

Accordingly, neither `182` nor `183` is currently bound here as a rigorously certified global
minimum over all finite-dimensional channels.

## Explicitness frontier

The random theorems are deterministic existence proofs after selecting a successful sample, but
that is weaker than a compact printable witness with exact Kraus/Stinespring entries and a rigorous
global entropy certificate. LLW's July 2026 introduction states that the known `p=1` mechanisms
remain probabilistic and that a deterministic finite-dimensional realization remains elusive.

This is evidence about the literature status as of that paper, not an impossibility theorem and not
a substitute for a new date-bounded search.

## Holevo-transfer caveat

Shor's equivalence theorem relates universal finite-dimensional propositions. From a
minimum-output-entropy counterexample it permits an existential conclusion that some Holevo pair
is nonadditive. It does **not** preserve the sampled channel, random distribution, dimensions,
conjugate partner, Bell witness, success probability, or open subset. Therefore the random-model
and `182/183` statements above are minimum-output-entropy statements; they must not be advertised
as same-model prevalence theorems for Holevo `chi`.

## Qualified verdict

For fixed dimensions in which a strict witness exists, continuity gives a nonempty relative-open,
positive-intrinsic-measure counterexample set. Some named high-dimensional random ensembles place
probability tending to one, or almost-sure eventual occurrence, on minimum-output-entropy
counterexamples. Nevertheless counterexamples are not dense, residual, or full-measure in a fixed
CPTP space because entanglement-breaking channels contain a nonempty relatively open strongly
additive region. A low-dimensional explicit certified `p=1` witness and a universal minimum output
dimension remain open frontiers in this library.

## Review status

The source pages, local files, hashes and quantifiers are now bound. Remaining completion gate: an
independent reviewer must check the frozen claim statements and the two local topology/continuity
derivations.
