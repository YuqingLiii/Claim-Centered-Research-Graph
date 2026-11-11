# Independent review of the antipodal-shift identity and six-root comparison point

Date: 2026-09-07.
Reviewer: `/root/orbit_d3_envelope`, a separate Codex review agent using the
inherited model. The exact model version is not independently verified.
This is author-independent role separation in the same model family and
shared task context, **not fresh-context or cross-model independence**.
The reviewer did not write, edit, or advise on either proof reviewed here
or the author's half-root checker. The reviewer previously authored a
different full-root D3 envelope computation. Neither that computation nor
its formula, checker, or claimed value is a dependency of this review.

## Scope and materials

This report covers precisely the two route-free claims
`GROTHORB.antipodal-shift-comparison` and `GROTHORB.d3-half-shift-value`.
It reviews every real square matrix C and lambda>=0 in the first claim,
including nonsymmetric and indefinite C, and the exact six-row matrix at
lambda=1/3 in the second. The subsequent `GROTHORB.shift-duplication-gap`
assembly (C10) is explicitly outside this report; that assembly depends on
the full-root result previously authored by this reviewer.

The reviewer read both target YAML files and both complete proof artifacts:
`antipodal-shift-comparison-20260907.md` (AD-1--AD-4),
`d3-half-shift-value-20260907.md` (HS-1--HS-4). The reviewer also inspected
the entire `check_d3_half_shift_value.py` and its author run record,
consulted the existing C8/C9 registrations and repository protocols, and
checked the target entries in the generated index and graph. The six
mathematical input-file hashes and exact run transcripts are preserved in
`grothendieck-group-orbit/artifacts/antipodal-half-shift-review-rerun-20260907.txt`,
R1--R4. The author proof hashes are:

| Proof artifact | SHA-256 |
|---|---|
| `antipodal-shift-comparison-20260907.md` | `a26f1cc2f4e561bb4bb46698bd2e9d458cb40d4972429049b21d0d90e51a6a05` |
| `d3-half-shift-value-20260907.md` | `41645cd84a2f70822e90b1ba41e984aaad54b61e16cd72503d229895fc28860a` |

Each finding is bound to SHA-256 of the UTF-8 encoding of the parsed YAML
`claim.strip()`; PyYAML 6.0.3 was used to extract those strings. The hashes
are distinct from the input-file hashes. Both claims have direct proofs
and no routes or unresolved project premises. No literature assertion,
numerical approximation, or full-root theorem is imported into either
mathematical argument.

## F1: GROTHORB.antipodal-shift-comparison — PASS

Reviewed claim hash:
`sha256:35ebd90ccd09ddcd28a125ed777c2e4dd11a76a66c27e1b144536cc0c4fce49b`.

Exact claim:

> For every real m by m matrix C and lambda>=0, set D(C)=(1/2)[C,-C;-C,C]. Then beta_cl(D(C)-lambda I_(2m))/2 equals the maximum over z in {-1,0,1}^m of sum_{i:z_i!=0}|(Cz)_i-lambda*z_i|+ sum_{i:z_i=0}max(|(Cz)_i|,lambda). In particular beta_cl(D(C)-lambda I_(2m))>=2*beta_cl(C-lambda I_m), with equality when lambda=0.

I independently expanded the doubled block matrix. For any real M, fixing
Bob signs and maximizing each Alice coordinate gives beta_cl(M)=max_t||Mt||_1.
This step does not require symmetry, positive semidefiniteness, or an
absolute-value convention for the original bilinear maximum.

Writing the doubled Bob vector as (a,b), the change of variables
z=(a-b)/2 and q=(a+b)/2 has exactly four possibilities per coordinate:
(z_i,q_i)=(1,0),(-1,0),(0,1),(0,-1). Conversely a=z+q and b=q-z are
signs for each such choice, proving a genuine bijection. Every ternary z
is represented, and all remaining freedom is the sign of q_i at zero
coordinates of z. Thus no ternary choice or doubled sign vector is lost.

Direct multiplication gives

```
(D(C)-lambda I)(a,b)=(v-lambda q, -v-lambda q),
v=Cz-lambda z.
```

The factor one half in D(C) is canceled by a-b=2z. Rowwise,
|v_i-lambda q_i|+|v_i+lambda q_i|=2max(|v_i|,lambda|q_i|), since
lambda>=0. For z_i nonzero, q_i=0 and this is exactly
2|(Cz)_i-lambda z_i|. For z_i=0, |q_i|=1 and it is exactly
2max(|(Cz)_i|,lambda). The result is independent of the residual q signs.
Maximizing over the full bijection proves the claimed identity for arbitrary
real C. Possible zero row values cause no issue: Alice may choose either
sign, and the norm identity remains exact. The argument explicitly uses
lambda>=0 where max(|(Cz)_i|,lambda) is written; it does not silently
extend that expression to negative lambda.

Restricting the ternary maximum to full sign vectors eliminates the second
sum and yields max_z||(C-lambda I)z||_1=beta_cl(C-lambda I), proving the
stated lower comparison with the correct factor two. At lambda=0 the
ternary objective reduces to ||Cz||_1 for all coordinates. For any zero
coordinate of z, linearity and the triangle inequality give

```
||Cz||_1 <= (||C(z+e_i)||_1 + ||C(z-e_i)||_1)/2.
```

At least one replacement has no smaller value, and each replacement removes
one zero without introducing another. After finitely many replacements a
sign vector attains at least the original ternary value. Since the sign
set is contained in the ternary set, their maxima agree. This proves
beta_cl(D(C))=2beta_cl(C), with no symmetry or definiteness assumption on C.

The only ingredients are finite sign maximization, an explicit linear
change of variables, the real absolute-value identity, and convexity of
the norm. They are proved or directly justified in the artifact. The proof
does not assert equality after positive shifts and does not depend on a
sample of matrices. No mathematical gap requiring repair was found.

## F2: GROTHORB.d3-half-shift-value — PASS

Reviewed claim hash:
`sha256:3905d276721ac794d0a04007c4ccaa948d1e392d904198da6899c70c81e24406`.

Exact claim:

> Let U have the six rows e_i-e_j and e_i+e_j for 1<=i<j<=3, and C=UU^T/4. Then beta_cl(C-(1/3)I_6)=3.

I checked the precise row convention
(12-,12+,13-,13+,23-,23+) and recomputed B=UU^T/4-I/3=H/12 with
H=3UU^T-4I. The integer matrix displayed in HS-1 is correct, including
diagonal entries 2 and the off-diagonal signs. Its all-ones image is
(2,14,8,8,2,2), so the all-ones pair supplies value 36/12=3. This establishes
a lower witness independently of any other root-family result.

For the global upper bound I reconstructed the signed-endpoint encoding.
On edge ij, the Bob pair (t_-,t_+) maps to
a_i=(t_-+t_+)/2, a_j=(t_+-t_-)/2. Exactly one coordinate is a sign and
the other is zero; the inverse t_-=a_i-a_j, t_+=a_i+a_j recovers the
pair. Three independent edges therefore encode all 4^3=64 Bob vectors
with no quotient. With v equal to the sum of these endpoint vectors,
U^Tt=2v. Substitution into Ht=3U(U^Tt)-4t gives for edge ij the two
entries 2[(3v_i-2a_i) minus/plus (3v_j-2a_j)]. Taking their absolute
values and using |u-w|+|u+w|=2max(|u|,|w|) proves HS.2, including its
factor four. The edge formula is symmetric in the endpoint labels, so
renaming vertices according to occupancy is legitimate even if the row
convention originally used i<j.

Let d_i count the selected endpoints. Every vertex has only two incident
edges, so 0<=d_i<=2 and the three occupancies sum to three. Up to vertex
names, the only patterns are (2,1,0) and (1,1,1). For (2,1,0), the double
vertex i must be selected by both incident edges ij and ik, and the remaining
edge jk selects the single vertex j. If its two signs at i agree,
v_i=2epsilon, v_j=delta, v_k=0 and the three edge maxima in HS.2 are
4,4,1. If those two signs cancel, v_i=0, v_j=delta, v_k=0 and the maxima
are 3,2,1. For (1,1,1), each selected endpoint has residual absolute
value |3v_i-2a_i|=1, while the unselected endpoint on that edge has
absolute value 3; all three edge maxima are 3. Thus the possible total
norms are 36,24,36, proving ||Ht||_1<=36 without trusting enumeration.

I separately checked that the case counts are exhaustive. The identities
of the double and single vertices give six unbalanced endpoint assignments;
their edge choices are then forced. Among the eight sign triples for each,
four agree and four cancel at the double vertex. This gives 24 vectors of
each type. Balanced occupancy allows the two directed cycles, each with
eight sign triples, giving 16 additional vectors. The total is 64, with
40 Bob vectors at norm 36 and 24 at norm 24. This excludes an omitted
orientation, sign choice, or zero-coordinate case. Alice's coordinatewise
maximum is exactly ||Ht||_1/12, so the hand proof bounds all ordered pairs.

For arithmetic validation I inspected and independently reran the entire
author checker, obtaining the stated 64-vector histogram, 24/24/16 case
counts, all row-pair identities, and a direct maximum over all 4096 ordered
pairs (R1). I then ran a separate implementation importing no author helper:
it builds the rational B matrix directly from the six root vectors using
Fraction and directly optimizes every ordered pair. It returned maximum 3,
the all-ones witness 3, and Bob-optimum histogram {2:24,3:40} (R2). These
checks agree with the independent hand derivation and the author run record.
No floating-point tolerance, full-root envelope, literature value, or
unresolved project claim is used. No mathematical gap requiring repair was
found.

## Verdict and boundaries

F1 and F2 both pass for their exact statements and inspected inputs. There
are no route implications to grade for these direct nodes. The arbitrary-C
claim is supported by algebra valid for its entire domain; the six-root
claim is supported by a complete hand certificate and two exact finite
implementations. The review is not a novelty assessment or a proof-assistant
formalization. Shared context and same-model-family limitations remain as
disclosed above. No author artifact or canonical node was modified, and no
verdict on the C10 assembly is issued here.
