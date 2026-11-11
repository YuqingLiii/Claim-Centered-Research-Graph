# Failure of the fixed three-side-block reduction for the input-centered triangle

Date: 2026-08-30

Status: exact formula witness refuting one proposed proof route; it is not a channel
nonadditivity witness.

For the seven-input/six-environment triangular three-face cluster with bases
`((-2,1),(-1,-1),(0,0))`, a first reduction retained the three binary input blocks at offsets
`(-1,1),(1,0),(2,-2)` and used separate convexity to reduce the other four blocks to 24 Gram
endpoint patterns.

This selected-side inequality fails in the one-sided large-label regime. Set the compact residual
labels to

```text
P = 1000000, Q = 64
```

so the actual base is `(P+2,Q+3)`, and use retained weights

```text
x = 466419/1000000
y = 532878/1000000
z = 623301/1000000.
```

The maximizing endpoint pattern is `(1,0,0,1)`, selecting branches `(m,c,h,c)` on the eliminated
blocks. Exact rational evaluation gives Gram parameter

```text
t = 0.6066382794601293...
```

and conjugate-Bell entropy `1.9827240288512042` bit. The three retained side entropies are

```text
0.9967438459936331
0.9968786600812782
0.9978332634645171
```

bit, so

```text
Bell - 2 min(selected sides) = -0.010763663136061918 bit.
```

This refutes only the fixed-three selected-side inequality. It is not a Bell-gap witness because
the channel also has other input blocks; in this endpoint pattern one of them is a pure `h` block.
More importantly, endpoint weights used to upper-bound the Gram parameter cannot be substituted
for the original channel's side outputs. A pattern-specific endpoint-side repair would reverse
the required quantifier order and is invalid.

The legal repair is to retain the additional original binary block at offset `(-2,0)`. Then four
original side blocks remain available, the other blocks reduce to 12 endpoints, and the exact
problem becomes six-dimensional. A dedicated large-label scan found a positive worst sampled
margin about `0.2348194` bit for this four-block route, but an all-parameter certificate is still
required.
