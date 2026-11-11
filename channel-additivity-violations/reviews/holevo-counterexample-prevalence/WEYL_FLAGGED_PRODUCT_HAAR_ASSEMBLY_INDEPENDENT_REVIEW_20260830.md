# Independent review: finite Weyl transfer, equal-Holevo flagged reduction, and product-Haar assembly

Date: 2026-08-30

Reviewer: independent Codex review context `/root/q1_weyl_transfer_review`.

## Independence declaration and scope

I did not author either atomic transfer node, their proposer artifacts, the assembled route, or the
broader `HCPREV.product-haar-unbounded` node. I read `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md`
in full, inspected Shor's local primary PDF directly, and reconstructed both local transfer proofs
and the route arithmetic.

The review proceeds in dependency order:

1. `HCPREV.finite-weyl-moe-to-holevo-pair-transfer`;
2. `HCPREV.equal-holevo-flagged-pair-to-self`;
3. route `atomic-moe-weyl-symmetric-self`; and
4. the unchanged broader claim `HCPREV.product-haar-unbounded`.

The already isolated atomic MOE premise is used only at its independently reviewed exact claim and
current `PROVED` status. This review does not promote or support `HCPREV.random-models`,
`HCPREV.goal`, Q3, or WHGAP.

## Executive verdict and staged disposition

All four reviewed statements **PASS** at their exact hashes:

| object | exact hash | disposition |
|---|---|---|
| finite Weyl MOE-to-Holevo pair claim | `sha256:5141db41a2972b86e9fbf83419dbfb5e739e4cb98656ec64c721858f6d793a9c` | eligible for `PROVED` |
| equal-Holevo flagged pair-to-self claim | `sha256:d598b38e12441325f6f51955be5080e1cbc3400739eba59dc01bd755ed4587d3` | eligible for `PROVED` |
| route implication `atomic-moe-weyl-symmetric-self` | `sha256:13d1a2d71d7fa4d9b5324bf6c8ab836ec09e0636fb84b62c314eb238b612e0ad` | eligible after all three premises are `PROVED` |
| unchanged broader product-Haar claim | `sha256:e50f0b1cf0c3a7640ca404b494d7a0f8a3d1a8cdcbaf9e7ee6cb9967097a78a9` | eligible after the route is completion-level |

The required promotion order is therefore:

```text
finite Weyl atom and equal-Holevo flagged atom;
then assembled route (the atomic MOE premise is already PROVED);
then HCPREV.product-haar-unbounded.
```

The Weyl transformation preserves the numerical MOE pair defect exactly as a one-shot Holevo pair
defect, but it changes the channels and induces a pushforward law. The flagged transformation then
turns the equal-Holevo pair into a single channel whose two-copy Holevo defect is strictly positive
for every positive pair defect and is at least `g-1`. Thus, to obtain a self-gap target `G`, the
MOE atom must be invoked at the strictly exceeded target `G+1` before depth is fixed.

No reviewed statement says that the original product-Haar sampled channels themselves have a
Holevo defect.

## Immutable inputs

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| finite Weyl node YAML | `7a0f5ea14e9e3e8014f07844e60dbd97c87adeb2cc77761369d942a127a86554` |
| equal-Holevo flagged node YAML | `c33b8f56cef58bf2b3c931b176029b0a4e95376d569760619b7655aee96e720d` |
| broader product-Haar node YAML | `6992260ae1c1c6aef30e7e993f28e52b8d326b13aa5b58de1389e00917544666` |
| current atomic-MOE node YAML | `994e2d24b961ea1f41b455bd592f0ba96bf600e65df8214f1df68734e9eb6d8b` |
| finite Weyl proposer artifact | `02556c800f1e6e3813a24b2a47bbe09238f45becb7aeda50d85689671ecd6596` |
| equal-Holevo flagged proposer artifact | `10a876c84485558fcd0e09396784c1f3ec207b4abd1c5dc72c8fc4a7b7392f08` |
| pushforward assembly artifact | `415d67df759c653bd716b14b2c242c26459efadbac1af4319a169683edd591d1` |
| Shor primary PDF | `300a97664fe8d05531230cd6f3a812b23e2c2cbf22c429436e50442993f415d6` |

The four exact statement hashes in the executive table were independently recomputed from the
current canonical YAML.

## Finding HCP-WF-IR-01 -- PASS: exact Shor interface and finite dephasing completion

Shor Section 9, PDF p. 18, first embeds the two finite outputs in one common `d`-dimensional
space. It defines generalized Pauli operators indexed by `z=da+b`,
`W_z=T^aR^b`, and the classical-labelled action

```text
N_i'(rho tensor |z><z|)=W_z N_i(rho) W_z^*.
```

For a one-channel minimum-output input, the paper uses all `d^2` labels uniformly. PDF p. 19 uses
all `d^4` label pairs uniformly on a joint lower-output-entropy input. The paper explicitly uses the
Weyl average to obtain the maximally mixed output. This matches the machine-visible source
assumption; the assumption does not attribute the later arbitrary-input completion to Shor.

The local completion

```text
tilde(N)(omega)=sum_z W_z N(omega_z) W_z^*,
omega_z=(I tensor <z|)omega(I tensor |z>)
```

is a finite CPTP map: it measures/dephases the label, applies the channel to each positive
subnormalized diagonal block, and performs a conditional unitary. The sum of block traces equals
`Tr(omega)`. Off-diagonal label coherences are discarded, so this is not the invalid coherent
controlled-label map.

**Verdict:** PASS.

## Finding HCP-WF-IR-02 -- PASS: global single and product minimum-output entropy preservation

For an arbitrary one-channel input, including label coherence, the output is a convex combination
of unitary conjugates of `N(rho_z)`. Entropy concavity and unitary invariance give the global lower
bound `S_min(N)`, while a minimizing input with one fixed label gives equality.

For the product of two extensions, an arbitrary state may be entangled across the two quantum
inputs and arbitrarily coherent or correlated across both label registers. The double dephasing
produces positive conditional states `rho_(z1,z2)` on the full joint quantum input, and

```text
(tilde(N1) tensor tilde(N2))(omega)
 = sum_(z1,z2) p_(z1,z2) (W_z1 tensor W_z2)
   (N1 tensor N2)(rho_(z1,z2))
   (W_z1 tensor W_z2)^*.
```

Concavity therefore bounds every product-extension output below by the global
`S_min(N1 tensor N2)`. A joint minimizing input with a fixed label pair gives the reverse
inequality. No additivity hypothesis and no restriction to product quantum inputs is used.

Isometric output padding only appends zero eigenvalues, so it preserves all single and product
output entropies before this construction.

**Verdict:** PASS. Both `S_min` equalities are genuinely global over all inputs.

## Finding HCP-WF-IR-03 -- PASS: one-channel and product Holevo identities

For a channel with output dimension `D`, every ensemble satisfies

```text
chi <= log_2(D)-S_min,
```

because the average output entropy is at most `log_2 D` and every signal output entropy is at least
the global minimum.

For one Weyl extension, fix a minimizing quantum input and use all classical labels uniformly.
The discrete Weyl twirl makes the average output `I_d/d`, while every signal output is a unitary
conjugate of the minimizing output. The upper bound is attained, giving

```text
chi(tilde(N_i))=log_2(d)-S_min(N_i).
```

For the product extension, fix a global joint minimizing input and use all label pairs uniformly.
The two-leg Weyl twirl sends its joint output to `I_d/d tensor I_d/d`; every signal has entropy
`S_min(N1 tensor N2)`. This attains the output-`d^2` upper bound and gives the exact product identity.
Subtracting the three identities yields

```text
Holevo pair defect = S_min(N1)+S_min(N2)-S_min(N1 tensor N2)
```

with the correct sign.

For a conjugate original pair, the two one-channel minimum output entropies are equal by the
bijection `rho -> conjugate(rho)` and spectral conjugation. Because both extensions use the same
common padded output dimension, their one-shot Holevo quantities are therefore equal. The
extensions themselves need not be asserted to remain a literal conjugate pair.

**Verdict:** PASS.

## Finding HCP-WF-IR-04 -- PASS: pushforward probability, not same sampled channels

At every finite dimension, output padding and the dephasing-Weyl extension are deterministic finite
maps on channel pairs. The numerical defect equality holds sample-by-sample. Therefore the event
probability is preserved under the deterministic pushforward of the original product-Haar law.

The transformation enlarges the input by a `d^2`-dimensional classical label and changes the
channel identity. Its pushed-forward distribution need not be product-Haar, Haar on a channel
space, full-support, or generic. Consequently this atom supplies an existential/model-specific
Holevo pair family but no Holevo statement about the original sampled `L` and `bar(L)`.

**Verdict:** PASS. The claim and caveats state the correct law boundary.

## Finding HCP-WF-IR-05 -- PASS: flagged direct-sum Holevo identity for arbitrary inputs

For a direct-sum family of channels `T_i`, the defining map discards cross-branch coherences and
places outputs in orthogonal flagged blocks. For an arbitrary input ensemble, let `p_i` be the
average branch distribution and condition the signals within each branch. The block-entropy
formula gives

```text
chi(one ensemble)=I(signal:branch)+sum_i p_i chi(conditional ensemble_i)
                 <= H(p)+sum_i p_i chi(T_i).
```

Conversely, choose the branch as part of the classical signal with probability `p_i` and use an
optimal (or arbitrarily near-optimal) ensemble inside each branch. This reaches
`H(p)+sum_i p_i chi(T_i)`. Maximization over `p` gives

```text
chi(direct_sum_i T_i)=log_2 sum_i 2^(chi(T_i)).
```

For two equal values `chi(A)=chi(B)=x`, this yields `chi(T)=x+1` exactly. The proof covers coherent
inputs because the channel dephases the branch before the flagged entropy decomposition.

**Verdict:** PASS.

## Finding HCP-WF-IR-06 -- PASS: four-block self defect, strictness, and output overhead

The tensor square is the flagged direct sum of `A tensor A`, `A tensor B`, `B tensor A`, and
`B tensor B`. Product ensembles give `chi(A tensor A),chi(B tensor B)>=2x`, while input/output
swaps give `chi(B tensor A)=chi(A tensor B)=2x+g`. Applying the exact direct-sum formula yields

```text
chi(T tensor T)-2chi(T)
 >= log_2(1+2^g)-1
  = log_2(1+(2^g-1)/2)
 >= g-1.
```

If `g>0`, then `(1+2^g)/2>1`, so the first lower bound is strictly positive even when the weaker
`g-1` bound is nonpositive. The constant-loss conclusion requires the exact equal-`chi` hypothesis
and makes no claim for an unbalanced pair.

The flagged output is an orthogonal direct sum of dimensions `d_A` and `d_B`, hence

```text
log_2(d_A+d_B)<=max(log_2 d_A,log_2 d_B)+1.
```

For the common `d`-dimensional Weyl outputs, the overhead is exactly one output-dimension bit.
This is not a bound on the enlarged label-input dimension or on the required large original matrix
dimension.

**Verdict:** PASS.

## Finding HCP-WF-IR-07 -- PASS: assembled route and `G`/`G+1` quantifiers

The first premise is currently `PROVED` at
`sha256:d440f868f357ab31ba91a26b622eb020b69f597a4f5c62e69c53661689c0bc9e`.
It states that for any strictly positive target `K`, one first chooses a fixed depth `J`, after
which the event `g_(J,D)>K` has probability tending to one as `D -> infinity`.

For a desired Holevo pair target `G>0`, take `K=G`; exact Weyl defect preservation turns the same
event into a pushed-forward pair event `g>G`. For a desired self target `G>0`, take
`K=G+1`; on the strict event `g>G+1`, the flagged bound gives `self defect >=g-1>G`. Both finite
transformations are deterministic sample-by-sample, so no new random event or independence
assumption is introduced.

The route also correctly accounts for equal one-shot Holevo quantities after the Weyl step and for
the one-bit output-log-dimension overhead. It keeps fixed depth before the large-`D` limit.

**Verdict:** the exact route implication at
`sha256:13d1a2d71d7fa4d9b5324bf6c8ab836ec09e0636fb84b62c314eb238b612e0ad`
PASSes. It becomes eligible for completion-level promotion only after both newly reviewed atomic
transfer premises have first been promoted to `PROVED`.

## Finding HCP-WF-IR-08 -- PASS: exact broader claim and strict non-propagation

The unchanged broader claim has exactly the clauses supplied by the assembled route:

1. arbitrarily large fixed-depth high-probability MOE defects in the original product-Haar
   channel/conjugate-channel family;
2. exact finite deterministic transfer to Holevo pair defects under a Weyl pushforward; and
3. transfer to a same-channel two-copy Holevo defect with at most one bit loss under a further
   flagged pushforward for the equal-quantity family.

The claim's assessment caveats make clear that the target/depth is fixed first, the transformed
models are pushforwards rather than the original samples, and no explicit successful tuple or
whole-CPTP genericity result is supplied.

**Verdict:** the exact broader claim at
`sha256:e50f0b1cf0c3a7640ca404b494d7a0f8a3d1a8cdcbaf9e7ee6cb9967097a78a9`
PASSes and is eligible for proposer-side `PROVED` only after the three premises and assembled route
are completion-level.

This disposition does not authorize any change to `HCPREV.random-models`, whose compound named-
model clauses require their own exhaustive premises, or to `HCPREV.goal`. It also supplies no
full-size/extensive Q3 theorem and no WHGAP result.

## Required link and promotion order

The proposer should link this review separately to:

1. the finite Weyl atom at Finding HCP-WF-IR-01--04 and exact hash `5141db41...`;
2. the equal-Holevo flagged atom at Finding HCP-WF-IR-05--06 and exact hash `d598b38e...`;
3. the assembled route at Finding HCP-WF-IR-07 and exact hash `13d1a2d7...`; and
4. the broader claim at Finding HCP-WF-IR-08 and exact hash `e50f0b1c...`.

Then promote in that order, stopping if any exact statement changes.

