# Independent review: exact physical-purity subset expansion and conjugation-closed obstruction

Date: 2026-08-31

Reviewer: primary Codex context `/root`, independently checking proposer context
`/root/q3_real_4096_review`.

## Scope and immutable inputs

This review covers only two finite algebraic claims. It does not prove the all-copy physical-purity
inequality for a generic selected product-Haar tuple, and it does not promote `HEXT.goal`.

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| reviewed derivation artifact | `40b52957a0a5c87ed98f0e3736fd727afee5456755b8d30c6da56ab7dd2d162f` |
| centered-subset proposer YAML | `d9a2a96cc5557527517dfa844684c70c7d8353401fd750450bc29766cd20a42f` |
| conjugation-closed proposer YAML | `295b91e112ab4900b386f2ad4b61ed244f7647dc1912cf08181c04637bcbd3d6` |

The repository-normalized exact claim hashes are:

| node | exact claim hash |
|---|---|
| `HEXT.physical-purity-centered-subset-expansion` | `sha256:475cfa24817b886754b899ce5a8d1caea6d1ccfc5728e24ecaac33ba87a1a0e7` |
| `HEXT.conjugation-closed-self-purity-n2-obstruction` | `sha256:6eae14abe6af4beb91e413ec834b99ad9f155a270899757d2dc34fe7e7cc6b7e` |

## Finding HEXT-PP-IR-01 -- PASS: centered subset identity

Write `C=D_0+E`, with `D_0(X)=Tr(X)I_q/q`. Since both `C` and `D_0` preserve trace,
`Tr(E(X))=0`. Expanding `C^(tensor r)` gives one term for every subset `S` on which `E` acts;
the `D_0` factors trace out the complementary input systems and contribute `I_q/q` there.

For two different subsets, choose one output factor in their symmetric difference. One summand is
proportional to the identity on that factor, while the partial trace of the other summand over that
factor vanishes because `E` is trace-annihilating. Hence the summands are Hilbert--Schmidt
orthogonal. Squaring therefore gives exactly

`Tr[C^(tensor r)(rho)^2] = sum_S q^(-(r-|S|)) ||E^(tensor |S|)(rho_S)||_2^2`.

Multiplication by `q^r` proves the stated equivalence with the centered budget. At `r=3` the
proper-marginal inequalities contain only the empty, one-body, and two-body terms. Directly summing
them creates no coefficient for the fully centered three-body term. The revised claim correctly
limits this observation to that naive marginal-summation induction; it does not rule out an
additional structural inequality.

**Verdict:** PASS at exact claim hash `475cfa24...`.

## Finding HEXT-PP-IR-02 -- PASS: conjugation-closed two-copy collision

Assume `W_{pi(v)}=z_v conjugate(W_v)` with `pi` a permutation. For the normalized Bell vector,
`(W_v tensor W_{pi(v)}) Omega=z_v Omega`. Thus the `q` distinct ordered Kraus pairs
`(v,pi(v))` contribute mass `1/q` to one ray in the output of `L tensor L`.

Write the remaining positive operator as `R`. It has trace `1-1/q` and rank at most `q^2-q`, so
`Tr(R^2)>=(1-1/q)^2/(q^2-q)`. Dropping the nonnegative cross term with the Bell ray yields

`Tr[(L tensor L)(Omega)^2] >= 1/q^2 + (1-1/q)^2/(q^2-q)
 = 2/q^2-1/q^3`.

For a pure input, a channel output and its complementary output have the same nonzero spectrum.
The complement of `L tensor L` is `C tensor C`, so the same lower bound applies to the relevant
physical complementary output. Comparison with `(A/q)^2` gives failure exactly when
`A^2<2-1/q`.

The claim's scope is correct: exact conjugation closure is a special dependent subclass and does
not refute existence of a generic independent complex-Haar tuple.

**Verdict:** PASS at exact claim hash `6eae14ab...`.

## Final disposition

Both reviewed atomic claims may be promoted to `PROVED`. The all-copy inequality itself, the
generic-Haar `r=2` gate, and the full-size Hayden--Penington target remain `OPEN`.

