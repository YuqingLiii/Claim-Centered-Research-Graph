# L3 hidden-frequency-mask: exact promise and lossless embeddings

Date: 2026-07-21  
Canonical scope: `KSUM.B4b.L3.ALT.hidden-frequency-mask`  
Status of this memo: construction only; **no lower bound is attempted or claimed**  
Method: local corpus only; no web; no DAG-file edits

## 1. Outcome

This memo freezes one total, permutation-invariant two-list promise that exactly realizes ABI's
rare-singleton/heavy-decoy profile at every integer parameter

\[
 N\ge 12,\qquad 5\le q\le \lfloor N^{2/3}\rfloor .
 \tag{HF.1}
\]

Here `q` is the common range size of the claw instance.  The two lists have equal length
`n=floor(N/2)`.  Each list contains `Theta(q)` singleton labels and `Theta(q)` side-exclusive
heavy labels, the latter with multiplicities differing by at most one and all
`Theta(N/q)`.  A YES input has exactly one common label, occurring once on each side; a NO input
has disjoint supports.  Thus YES has exactly the two matching singleton occurrences described in
ABI, while NO has none.

The promise is an exact restriction of `Claw_(n,n->q)`.  It embeds into cyclic 2-SUM of exact
length `N`, arbitrary target, and modulus

\[
 Q=2q+1=O(q)
 \tag{HF.2}
\]

with one value-oracle query per live coordinate (at most two in the standard coherent XOR
simulation convention).  There are no dummy labels inside either list.  If `N` is odd, the sole
public padding coordinate is proved inert.

At `q=Theta(N^(2/3))` the frozen type specializes to ABI's displayed profile: `Theta(N^(2/3))`
singleton occurrences, only two or none matching, and all remaining positions carried by heavy
decoys of multiplicity `Theta(N^(1/3))`.

## 2. Exact integer parameters

Fix `N,q` satisfying (HF.1), and define

\[
 n:=\lfloor N/2\rfloor,\qquad
 a:=\lfloor q/4\rfloor,
 \tag{HF.3}
\]

\[
 d:=\left\lfloor {n-a\over a}\right\rfloor,
 \qquad
 p:=(n-a)-ad.
 \tag{HF.4}
\]

Then

\[
 1\le a,\qquad 0\le p<a,
 \qquad n=a+(a-p)d+p(d+1).
 \tag{HF.5}
\]

The range condition supplies all rounding facts needed below:

1. `4a<=q`, so four disjoint size-`a` label palettes fit in `[q]`.
2. Since `N>=12` and `q<=floor(N^(2/3))`, one has `q<n`: check `N=12`
   directly, while for `N>=13` the strict inequality
   `2N^(2/3)<N-1` holds (it holds at `13` and its difference has positive derivative thereafter).
   Thus `N^(2/3)<(N-1)/2<=n`, so `q<n`.  Hence
   `a<n/4` and `d>=3`.  In particular, frequency `1` is never confused with a heavy frequency.
3. `a=Theta(q)` and `d,d+1=Theta(N/q)` uniformly in (HF.1).  The split into `p` labels of
   frequency `d+1` and `a-p` labels of frequency `d` is only the exact division remainder; it
   does not mark any label publicly.

The claw input uses two lists of length `n`, so it contains `2n` oracle positions.  For even `N`,
`2n=N`.  For odd `N`, `2n=N-1`; Section 5 adds one public inert cyclic coordinate after the claw
encoding.  There is no internal list padding.

## 3. The frozen YES and NO orbits

For lists `x,y in [q]^n`, let

\[
 r_v:=|\{i:x_i=v\}|,\qquad s_v:=|\{j:y_j=v\}|,
 \tag{HF.6}
\]

and let their joint frequency histogram be

\[
 H_{u,v}:=|\{z\in[q]:(r_z,s_z)=(u,v)\}|.
 \tag{HF.7}
\]

The promise consists of exactly the following two joint-histogram types.  Cells not displayed have
count zero.

### NO type

\[
\begin{array}{c|c}
\text{joint label frequency }(r_z,s_z)&H_{r_z,s_z}\\ \hline
(0,0)&q-4a\\
(1,0)&a\\
(0,1)&a\\
(d,0)&a-p\\
(d+1,0)&p\\
(0,d)&a-p\\
(0,d+1)&p
\end{array}
\tag{HF.8}
\]

Thus the left and right supports are disjoint.  Concretely, choose pairwise disjoint palettes
`S_L,S_R,H_L,H_R subset [q]`, each of size `a`.  Labels in `S_L,S_R` occur once on their indicated
side.  On each side, `p` labels in its `H` palette occur `d+1` times and the other `a-p` occur `d`
times.  All position assignments are allowed.

### YES type

\[
\begin{array}{c|c}
\text{joint label frequency }(r_z,s_z)&H_{r_z,s_z}\\ \hline
(0,0)&q-4a+1\\
(1,1)&1\\
(1,0)&a-1\\
(0,1)&a-1\\
(d,0)&a-p\\
(d+1,0)&p\\
(0,d)&a-p\\
(0,d+1)&p
\end{array}
\tag{HF.9}
\]

Concretely, choose one label `z_*`, two disjoint rare palettes `S_L,S_R` of size `a-1`, and two
heavy palettes `H_L,H_R` of size `a`, all mutually disjoint and disjoint from `z_*`.  Put `z_*`
once on each side; use `S_L,S_R` as the remaining singletons and the heavy palettes as in the NO
type.  This uses `4a-1<=q` distinct labels.

Both types are nonempty by `4a<=q` and (HF.5).  They are each a single orbit under

\[
 S_n\times S_n\times S_q,
 \tag{HF.10}
\]

where the first two factors independently permute positions and the last factor commonly relabels
the range.  Therefore the promise is exactly permutation invariant.  No rare/heavy palette, label
identity, position block, or latent address is supplied with the input.

## 4. Exact restriction to small-range claw

Let `Claw_(n,n->q)(x,y)=1` iff some `i,j` satisfy `x_i=y_j`.

**Proposition 1.** On the promise (HF.8)--(HF.9),

\[
 \operatorname{Claw}_{(n,n)\to q}(x,y)=
 \begin{cases}
 0,&(x,y)\text{ has type NO},\\
 1,&(x,y)\text{ has type YES}.
 \end{cases}
 \tag{HF.11}
\]

**Proof.** In the NO type every nonzero joint-histogram cell lies on one coordinate axis, so no
label occurs on both sides.  In the YES type the only label occurring on both sides is the unique
`(1,1)` label `z_*`.  Hence there is exactly one equal cross-position pair, namely the two
occurrences of `z_*`.  All heavy labels are side-exclusive, so none is a hidden additional claw.
This proves both directions exactly. ∎

Since `q<n` in (HF.1), this is literally a restriction of the ordinary small-range two-list claw
problem, not a relation problem and not a bucket-composed surrogate.  The restriction oracle is
the ordinary input-value oracle; no promise metadata is queryable.

## 5. Constant-query embedding into cyclic 2-SUM

Fix

\[
 Q:=2q+1
 \tag{HF.12}
\]

and an arbitrary target `t in Z_Q`.  Since `Q` is odd, there is a unique
`c in Z_Q` satisfying

\[
 2c=t.
 \tag{HF.13}
\]

Given `(x,y) in [q]^n x [q]^n`, form the live cyclic string

\[
 E_t(x,y):=
 (c+x_1,\ldots,c+x_n,\ c-y_1,\ldots,c-y_n)
 \in\mathbb Z_Q^{2n}.
 \tag{HF.14}
\]

Here labels `1,...,q` are interpreted as their indicated residues.  If `N` is even, (HF.14) is
the whole 2-SUM input.  If `N` is odd, append one public coordinate of value `c`; call the resulting
length-`N` string `E_t^+(x,y)`.  This is the only padding.

**Proposition 2.** For every claw input, not merely promised ones,

\[
 \operatorname{2SUM}_{\mathbb Z_Q,t,2n}(E_t(x,y))
 =\operatorname{Claw}_{(n,n)\to q}(x,y).
 \tag{HF.15}
\]

For odd `N`, the same equality holds with `E_t^+` and length `N`.

**Proof.** Consider two distinct live positions.

* Two left values sum to `t+x_i+x_j`.  The integer `x_i+x_j` lies in `[2,2q]`, hence is nonzero
  modulo `Q=2q+1`; this pair never hits `t`.  This also covers repeated heavy labels.
* Two right values sum to `t-(y_i+y_j)`.  Again `y_i+y_j in [2,2q]` is nonzero modulo `Q`; this
  pair never hits `t`.
* A cross pair sums to `t+x_i-y_j`.  The integer difference lies in `[-(q-1),q-1]`, whose only
  multiple of `Q` is zero.  Thus the pair hits `t` iff `x_i=y_j`.

This proves (HF.15), including exact completeness and soundness and the absence of within-half
target errors.

If `N` is odd, the padding value `c` is used once.  It is distinct from every live value because
all live offsets are `+u` or `-u` with `1<=u<=q<Q`.  A padding/live sum equals `t=2c` only if the
live value is `c`, which never occurs.  There is no pair of two padding coordinates.  Hence the
padding creates no witness and removes none. ∎

There are no dummy symbols to audit: the entire claw range is encoded uniformly.  A query to a
left coordinate makes one query for `x_i` and applies the fixed map `u -> c+u`; a right query does
the same with `u -> c-u`; the possible last coordinate is public.  Thus the simulation is one
query in a value-return oracle and `O(1)` (at most two) in the coherent XOR-oracle convention.
It never discovers or computes the hidden label partition.

Combining Propositions 1 and 2, the promised YES/NO bit is exactly cyclic 2-SUM at every target,
with total length exactly `N` and alphabet `Q=2q+1=O(q)`.

## 6. Endpoint and cap sweep

The proposed future lower-bound scale is

\[
 L(N,q):=\min\{\sqrt N\,q^{1/4},N^{2/3}\}.
 \tag{HF.16}
\]

Within (HF.1), the first term never exceeds the second.

### Fixed endpoint `q=5`

Here `a=1`.  Each side has exactly one singleton label and one heavy label of multiplicity
`d=n-1` (`p=0`).  NO uses four distinct labels and leaves one unused; YES shares the singleton
label, uses two side-exclusive heavy labels, and leaves two labels unused.  The cyclic modulus is
`Q=11`.  The target scale is

\[
 L(N,5)=5^{1/4}\sqrt N=\Theta(\sqrt N).
\]

Thus the construction does not disappear or require a zero-size palette at the fixed endpoint.

### Power-law interior `q=N^rho`, `0<rho<2/3`

Up to rounding,

\[
 a=\Theta(N^\rho),\qquad d=\Theta(N^{1-\rho}),
 \qquad L(N,q)=N^{1/2+\rho/4}.
 \tag{HF.17}
\]

The singleton positions form a fraction `Theta(q/N)` of each list, while almost all positions are
heavy decoys.

### Capped endpoint `q=floor(N^(2/3))`

Now

\[
 a=\Theta(N^{2/3}),\qquad d=\Theta(N^{1/3}),
 \qquad \sqrt N\,q^{1/4}=\Theta(N^{2/3}).
 \tag{HF.18}
\]

Across both lists there are `2a=Theta(N^(2/3))` singleton occurrences.  Exactly two of them match
in YES and none match in NO.  All other positions are divided among `2a=Theta(N^(2/3))`
side-exclusive heavy labels, with `Theta(N^(1/3))` copies each.  This is ABI's stated obstruction
up to fixed constants and the unavoidable integer remainder.

The modulus `Q=2q+1` changes all three scales only by absolute constants.  No endpoint exceeds the
standard `N^(2/3)` walk cap.

## 7. Exhaustive low-dimensional leakage audit

The promise hides label identities and positions, but it does not magically make frequency data
information-theoretically invisible.  This section records every invariant low-dimensional route
by which the partition could be exposed, so a later lower-bound attempt cannot silently ignore an
easy statistic.

### 7.1 Exhaustive invariant description

Under the symmetry (HF.10), the full joint histogram `H=(H_{u,v})` is a complete orbit invariant.
Consequently **every** statistic invariant under independent position permutations and common
range permutations is a function of `H`.  Between NO and YES, the entire change is the unit
four-cell switch

\[
 \Delta H_{1,1}=+1,\quad
 \Delta H_{1,0}=-1,\quad
 \Delta H_{0,1}=-1,\quad
 \Delta H_{0,0}=+1,
 \tag{HF.19}
\]

and all heavy cells are identical.  Equation (HF.19) is therefore an exhaustive ledger, not a
sampled list of possible invariants.

For any linear histogram statistic `T_w=sum_(u,v) w_(u,v) H_(u,v)`, its complete YES-minus-NO
change is

\[
 \Delta T_w=w_{1,1}-w_{1,0}-w_{0,1}+w_{0,0}.
 \tag{HF.20}
\]

Thus every additive statistic whose weight separates as `w_(u,v)=A_u+B_v` is exactly blind.
Any invariant distinguisher must use a genuinely joint interaction or a nonlinear function that
detects the same four-cell switch.

### 7.2 Statistics that are exactly blind

The following are identical in YES and NO:

1. each list length and its complete marginal occupancy multiset;
2. the number `a` of singleton labels on either side;
3. the number `a` of heavy labels on either side and the exact `d/(d+1)` split;
4. every one-list frequency moment, falling-factorial moment, collision count, number of distinct
   labels, maximum frequency, and frequency-of-frequencies statistic;
5. every statistic that is a sum of a left-only and a right-only statistic;
6. the probability `a/n` that a uniformly sampled position carries a singleton label.

Therefore no marginal count tells an algorithm whether it has a YES or NO input, although
marginal frequency tests can help it classify a queried label as rare or heavy.

### 7.3 Statistics that expose the joint switch

All of the following distinguish the two exact types, and must be controlled in any future lower
bound:

1. **Support intersection:** `|supp(x) intersect supp(y)|` is `0` versus `1`.
2. **Cross-equal-pair count:**
   \[
     C_\times=\sum_z r_zs_z
   \]
   is `0` versus `1`; this is exactly the claw predicate on the frozen promise.
3. **Union support size:** it is `4a` versus `4a-1`; equivalently, the number of globally unused
   labels is `q-4a` versus `q-4a+1`.
4. **Overlap mass:** `sum_z min(r_z,s_z)` is `0` versus `1`.
5. **Combined-list collision count:** `sum_z binom(r_z+s_z,2)` increases by exactly one in YES,
   while the two marginal collision counts stay fixed.
6. **Combined frequency-of-frequencies:** NO has `2a` labels of combined frequency one; YES has
   `2a-2` such labels and one extra label of combined frequency two.  Since `d>=3`, this extra
   frequency-two cell cannot merge with a heavy cell.
7. **Mixed moments:** every ordinary mixed moment `sum_z r_z^u s_z^v` with `u,v>=1` is `0` versus
   `1`.  For falling-factorial moments, only the `(u,v)=(1,1)` moment changes, because the shared
   label is a singleton on both sides.
8. **Labelwise two-sided frequency:** for an encountered label `z`, the pair `(r_z,s_z)` directly
   classifies it as unused, left/right rare, left/right heavy, or the unique shared singleton.

Items 1--8 are different presentations of (HF.19), not independent promise defects.  They show
precisely what a promise-aware algorithm could try to estimate.

### 7.4 How the hidden partition can be searched

The label partition is hidden only by permutations; it is not supplied as an oracle field.  A
queried occurrence reveals its raw label but not its multiplicity.  The following primitive tests
could nevertheless expose roles and must be included in a later hostile algorithm audit:

* search for a second same-list occurrence of a queried label (singleton versus heavy);
* estimate a label's same-list frequency (`1`, `d`, or `d+1`);
* test whether a sampled label occurs on the opposite side;
* estimate union distinctness, the global combined collision count, or the four relevant joint
  histogram cells;
* exploit the known values of `a,d,p` to condition sampling on likely singleton or heavy labels.

There is no lower-dimensional address, bucket number, public color, or label predicate that names
`S_L,S_R,H_L,H_R`.  The only exact answer-bearing interaction is the shared `(1,1)` label, but the
large heavy multiplicities may make singleton certification algorithmically cheaper than treating
the input as an arbitrary claw.  This memo deliberately leaves that lower-bound/upper-algorithm
question open.

Raw label order, parity, or numerical value and raw position indices provide no further promised
statistic: the full `S_q` and independent `S_n` actions can move every role to every compatible
label or position.  Such non-invariant predicates may be used by an algorithm, but an adversarial
input can relabel them arbitrarily; they have no fixed correlation with the hidden partition.

## 8. Checklist and scope boundary

| Obligation | Result |
|---|---|
| one exact promise for all asymptotic `5<=q<=N^(2/3)` | **PASS**, (HF.3)--(HF.9) |
| integer rounding and even/odd `N` | **PASS**, (HF.4)--(HF.5), one inert odd pad |
| permutation invariance | **PASS**, one `S_n x S_n x S_q` orbit per answer |
| rare-singleton/heavy-decoy ABI profile | **PASS**, exactly two or zero matching singleton occurrences |
| exact restriction of small-range claw | **PASS**, Proposition 1 |
| cyclic alphabet `O(q)` and arbitrary target | **PASS**, `Q=2q+1`, (HF.13)--(HF.15) |
| constant-query simulation | **PASS**, one value query / at most two coherent XOR queries |
| dummy, padding, within-half, cross, target errors | **NONE**, Proposition 2 |
| endpoint cap sweep | **PASS**, Section 6 |
| invariant low-dimensional leakage audit | **COMPLETE at histogram level**, Section 7 |
| lower bound | **NOT ATTEMPTED** |

The construction satisfies the requested freezing/embedding step only.  It does not license a
status change for the canonical node and does not show that the promise has quarter-power query
complexity.

## 9. Out-of-node approaches

None generated during this construction.
