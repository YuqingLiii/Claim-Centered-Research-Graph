# Product-Haar MOE to Holevo pair and self-channel pushforward assembly

Date: 2026-08-30

Status history: written as a proposer-side three-premise assembly while
`HCPREV.product-haar-unbounded`, its premises, and its route were `CONJECTURED`; they were
subsequently upgraded to `PROVED` by the hash-bound reviews recorded in the node YAML files. This
artifact is historical evidence, not a live status authority.

## 1. Registered objects and exact hashes

| object | exact repository-normalized hash |
|---|---|
| `HCPREV.product-haar-moe-unbounded` claim | `sha256:d440f868f357ab31ba91a26b622eb020b69f597a4f5c62e69c53661689c0bc9e` |
| `HCPREV.finite-weyl-moe-to-holevo-pair-transfer` claim | `sha256:5141db41a2972b86e9fbf83419dbfb5e739e4cb98656ec64c721858f6d793a9c` |
| `HCPREV.equal-holevo-flagged-pair-to-self` claim | `sha256:d598b38e12441325f6f51955be5080e1cbc3400739eba59dc01bd755ed4587d3` |
| route `atomic-moe-weyl-symmetric-self` implication | `sha256:13d1a2d71d7fa4d9b5324bf6c8ab836ec09e0636fb84b62c314eb238b612e0ad` |
| unchanged broader claim | `sha256:e50f0b1cf0c3a7640ca404b494d7a0f8a3d1a8cdcbaf9e7ee6cb9967097a78a9` |

## 2. Exact probability-preserving composition

Fix an integer `m>e^18`. The first premise states that for every `K>0` one may choose a fixed
depth `J` such that the product-Haar channel/conjugate-channel pair

\[
 (L_{J,D},\bar L_{J,D})
\]

has p=1 MOE pair defect `g_(J,D)>K` with probability tending to one as `D->infinity`.

For every realization, apply the finite dephasing-Weyl transformation from the second premise and
write the resulting channels as `(A_(J,D),B_(J,D))`. The transformation is deterministic and the
Holevo pair defect is exactly `g_(J,D)`. Since the original pair consists of a channel and its
conjugate, its two minimum output entropies are equal. Both Weyl extensions have the same padded
output dimension, so

\[
 \chi(A_{J,D})=\chi(B_{J,D}).                             \tag{1}
\]

Apply the third premise sample-by-sample and set

\[
 T_{J,D}=A_{J,D}\mathbin{\rm direct\_sum}B_{J,D}.
\]

Its Holevo self defect is at least

\[
 \log_2\left[1+{1\over2}(2^{g_{J,D}}-1)\right]
 \ge g_{J,D}-1.                                           \tag{2}
\]

Therefore:

- to obtain a Holevo pair target `G`, choose the MOE target `K=G` with a strict margin;
- to obtain a same-channel Holevo target `G`, choose the MOE target `K=G+1` with a strict margin.

The deterministic maps preserve the relevant success-event probabilities under their pushforward
laws. No independent event intersection is needed.

## 3. Dimension accounting

If the original channels have outputs padded to dimension `d`, each Weyl extension has output
dimension `d` and a classical label of dimension `d^2` appended to its input. The flagged
same-channel output dimension is `2d`; hence its output log-dimension is only

\[
 \log_2(2d)=\log_2d+1.                                    \tag{3}
\]

This is the precise one-bit direct-sum log-dimension overhead. It does not control the existential
large per-leg matrix threshold `D(J)` or assert full-size scaling.

## 4. Random-law boundary

There are three distinct probability spaces or laws:

1. the original independent product-Haar law on the tuples defining `(L,bar L)`;
2. its deterministic pushforward under the finite Weyl transformation, defining `(A,B)`; and
3. the further deterministic pushforward under flagged direct sum, defining `T`.

The numerical defect identities compare events sample-by-sample, so their probabilities agree or
are monotonically inherited. They do **not** turn the original channels into Holevo witnesses and
do not imply that either transformed law is Haar, Lebesgue, full-support, or generic on a whole
CPTP ambient body.

## 5. Promotion gate

Independent review must proceed in dependency order:

1. atomic product-Haar MOE claim at `d440f868...`;
2. finite dephasing-Weyl transfer at `5141db41...`;
3. equal-Holevo flagged reduction at `d598b38e...`;
4. exact assembled implication at `13d1a2d7...`; and only then
5. unchanged broader claim at `e50f0b1c...`.

No object may be promoted merely because an analogous statement is proved in another project.
