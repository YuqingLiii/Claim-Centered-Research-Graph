# Exact classical certificate for the six-root D3 shifted matrix

Date: 2026-09-07. Author proof for independent review.
Canonical owner: `GROTHORB.d3-half-shift-value`.
Registration: `classical-family-registration-20260907.md`, C9.

This direct elementary certificate is independent of the full-root envelope
and of the literature motivation for this test point. It certifies the
specified value without asserting a new Grothendieck bound or novelty.

## HS-1: exact matrix, normalization, and witness

Order the six rows of U as

    (e_1-e_2, e_1+e_2, e_1-e_3, e_1+e_3, e_2-e_3, e_2+e_3).

Let C=UU^T/4 and B=C-I_6/3. Equivalently B=H/12, with the integer matrix

        [ 2  0  3  3 -3 -3 ]
        [ 0  2  3  3  3  3 ]
    H = [ 3  3  2  0  3 -3 ] = 3UU^T-4I_6.
        [ 3  3  0  2 -3  3 ]
        [-3  3  3 -3  2  0 ]
        [-3  3 -3  3  0  2 ]

For fixed Bob signs t, Alice can maximize each coordinate independently:

    max_s s^T B t = ||Ht||_1/12.                   (HS.1)

The all-ones vector 1 satisfies

    H1=(2,14,8,8,2,2)^T,    1^T H1=36.

Thus s=t=1 is an explicit witness of value 36/12=3. We next prove that
||Ht||_1<=36 for every Bob sign vector, by three elementary cases.

## HS-2: encode the three root pairs by signed edge choices

View the coordinate pairs 12,13,23 as the three edges of a triangle.
For an edge ij with i<j, let t_- and t_+ be its signs on e_i-e_j and
e_i+e_j, respectively. Define

    a^(ij) = ((t_-+t_+)/2)e_i + ((t_+-t_-)/2)e_j.

This vector is exactly one of +e_i,-e_i,+e_j,-e_j. Conversely every such
choice gives a unique pair (t_-,t_+). Thus an arbitrary Bob sign vector
corresponds bijectively to choosing one signed endpoint on each edge.
Define

    v=a^(12)+a^(13)+a^(23),    h=U^Tt=2v.

For the two rows on edge ij, substituting
t_-=a_i^(ij)-a_j^(ij) and t_+=a_i^(ij)+a_j^(ij) gives

    (Ht)_- = 2[(3v_i-2a_i^(ij))-(3v_j-2a_j^(ij))],
    (Ht)_+ = 2[(3v_i-2a_i^(ij))+(3v_j-2a_j^(ij))].

The elementary identity |u-w|+|u+w|=2max(|u|,|w|) now yields

    |(Ht)_-|+|(Ht)_+|
       = 4 max(|3v_i-2a_i^(ij)|,|3v_j-2a_j^(ij)|). (HS.2)

This unordered edge formula is unchanged if the endpoint names are
interchanged. We may therefore name the vertices by their roles in the
following cases, without any assumption about their numerical order.

## HS-3: complete three-case upper certificate

Let d_i count the edges that selected endpoint i, ignoring the signs.
Each d_i is at most two and d_1+d_2+d_3=3. Therefore, up to naming the
vertices, the only occupancy patterns are (2,1,0) and (1,1,1).

For (2,1,0), name the vertices i,j,k so that both edges ij,ik select i
and the remaining edge jk selects j. Write the two signs at i as
epsilon,eta, and the sign at j as delta, all in {-1,+1}.

- If epsilon=eta, then v_i=2epsilon, v_j=delta, v_k=0. The three
  maxima on the right of (HS.2), in edge order ij,ik,jk, are
  max(4,3)=4, max(4,0)=4, and max(1,0)=1. Their sum is nine, so
  ||Ht||_1=36.
- If eta=-epsilon, then v_i=0, v_j=delta, v_k=0. The three maxima
  are max(2,3)=3, max(2,0)=2, and max(1,0)=1. Their sum is six, so
  ||Ht||_1=24.

For (1,1,1), each vertex receives one signed choice, so v_i is exactly
the sign of that choice. On every edge, the selected endpoint contributes
an absolute residual |3v_i-2a_i|=1, while the other endpoint contributes
|3v_j|=3. Each maximum in (HS.2) is three. Thus ||Ht||_1=36.

These cases include every one of the 64 Bob sign vectors, and prove
||Ht||_1<=36. Together with (HS.1) and the all-ones witness, this proves

    beta_cl(UU^T/4-I_6/3)=3.                        (HS.3)

## HS-4: case counts and an exhaustive arithmetic replay

There are six ways to choose which named vertex receives two edges and
which receives one; the edge choices are then forced. For each such
assignment, four sign triples agree at the double endpoint and four
cancel there. The balanced occupancy has exactly two edge assignments:
the two directed cycles. Each has eight sign triples. Hence the complete
finite certificate has the following counts:

| Endpoint occupancy and signs | Bob sign count | ||Ht||_1 |
|---|---:|---:|
| (2,1,0), agreeing at the double endpoint | 24 | 36 |
| (2,1,0), canceling at the double endpoint | 24 | 24 |
| (1,1,1) | 16 | 36 |
| Total | 64 | maximum 36 |

The standard-library checker
`grothendieck-group-orbit/tools/check_d3_half_shift_value.py` constructs U
and H independently from their formulas, enumerates all 64 Bob vectors,
and checks (HS.2), the case counts, the exact maximum, and the all-ones
matching pair. Alice is maximized exactly using (HS.1); no symmetry
quotient or incomplete Bob sample is used by the checker. For an
additional check it directly enumerates all 64 times 64 ordered pairs.

Command from the candidate repository root:

    python3 grothendieck-group-orbit/tools/check_d3_half_shift_value.py

Run record: `d3-half-shift-exact-check-20260907.txt`.
The three-case proof already supplies a hand-verifiable global upper
bound. The checker replays its arithmetic; independent review must assess
the exact canonical claim and the argument before any completion-level
promotion. No statement here identifies this literature-motivated example
as a new construction or a new lower bound.
