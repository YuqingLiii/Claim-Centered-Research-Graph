# Primary-source audit: noisy qutrit Werner--Holevo capacity threshold

Date: 2026-08-29

Scope: distinguish published external inputs from the project's family-specific extensions and
bind the current arXiv theorem numbering. This is a proposer-side migration audit, not a new
independent review of the internal proofs.

## Source ledger

| Source | Local file | SHA-256 | Relevant location |
|---|---|---|---|
| C. Zhu and X. Wang, *Quantum Incapacity beyond No-Cloning and PPT Mechanisms*, arXiv:2607.24693v2 | `primary-sources/zhu-wang-2607.24693v2.pdf` | `6df428fc1be283f628c13210db213ff38056926a5db738db00f0f567812b76fe` | Corollary 3.1, PDF p. 5; Lemma 3.2, PDF p. 6; Definition 3.3/Proposition 3.4/Theorem 3.5, PDF pp. 7-11; Corollary 3.7, PDF p. 11; Theorem 4.3, PDF p. 15 |
| C. Hirche, C. Rouze and D. Stilck Franca, *Quantum Differential Privacy: An Information Theory Perspective*, arXiv:2011.05949 | `primary-sources/hirche-rouze-stilck-franca-2011.05949.pdf` | `fce5bf192d88aaee4d4d975a06683b27000d52e8dfe2a0cc0e7b1cce23e74c24` | Proposition 2.3, PDF pp. 8-9; Lemma 3.1 and Proposition 3.3, PDF pp. 11-12 |
| S. Roofeh and V. Karimipour, *The noisy Werner--Holevo channel and its properties*, arXiv:2310.15353 | `primary-sources/roofeh-karimipour-2310.15353.pdf` | `3e2752d3cb40b46b8457648dc652d3b8443676e8a3dd41c82155560026c62848` | Antidegradability construction for `4/7 <= x <= 1`, PDF pp. 15 onward |
| S. Roofeh and V. Karimipour, *Capacities of a two-parameter family of noisy Werner--Holevo channels*, arXiv:2405.11216 | `primary-sources/roofeh-karimipour-2405.11216.pdf` | `496f82fdf3fe930899eb09c306931322f6cdff27a5730178966ba58fd94c0118` | Quantum-capacity discussion and prior `4/7` boundary, PDF p. 9 |
| T. Belzig, R. Gaudio, M. A. Smith and P. Wu, *Reverse-type Data Processing Inequality*, arXiv:2411.19890v3 | `primary-sources/belzig-gaudio-smith-wu-2411.19890.pdf` | `6c59944e6a037d283c0a4a6ad6a48e3bce044e4cd077b5d769ac8a3b6c9948db` | BKM/relative-entropy comparison, Lemma 4.1, PDF p. 9 |

Online records: <https://arxiv.org/abs/2607.24693>, <https://arxiv.org/abs/2011.05949>,
<https://arxiv.org/abs/2310.15353>, <https://arxiv.org/abs/2405.11216>, and
<https://arxiv.org/abs/2411.19890>.

## Current Zhu--Wang numbering

The legacy notes cite a “Zhu--Wang Theorem 3.3.” In the currently downloaded arXiv v2 dated
2026-07-30/31, the relevant chain is instead:

1. Definition 3.3 defines a complete variance-dominating signed lift.
2. Proposition 3.4 gives its finite-dimensional operator certificate.
3. Theorem 3.5 converts complete variance domination into complete BKM domination.
4. Lemma 3.2 converts complete BKM domination into complete relative-entropy domination under
   faithful-output hypotheses.
5. Corollary 3.1 combines complete relative-entropy domination of a complement with HRSF
   tensorization to force optimized coherent and private information to vanish at every blocklength.
6. Corollary 3.7 packages this chain for a signed lift.

This is a bibliographic version-number correction. The mathematical interface used by the legacy
proof note matches the v2 chain, but future citations should use the v2 numbering above.

## External all-blocklength pipeline

HRSF Lemma 3.1 proves hybrid tensorization of the complete less-noisy preorder. HRSF Proposition
2.3 supplies its relative-entropy characterization. In Zhu--Wang's notation this is exactly the
step

`M >=_cRE N  and  M' >=_cRE N'  =>  M tensor M' >=_cRE N tensor N'`.

Zhu--Wang Corollary 3.1 then proves that if a channel complement completely relative-entropy
dominates the channel, both one-shot optimized quantities vanish at every tensor power and hence
`P=Q=0` after regularization. The support and orientation details are included in the published
proof, not merely asserted.

## What the external papers prove for this family

- Roofeh--Karimipour prove antidegradability for `4/7 <= x <= 1`, hence zero quantum capacity
  there by the standard no-cloning mechanism.
- Zhu--Wang Theorem 1.1/Theorem 4.3 proves `P=Q=0` at the single point `x=1/2`, at every
  blocklength, and proves that this channel is neither PPT nor antidegradable.

The interval extension from the point `x=1/2` to every `x in [1/2,1)` is **not** a theorem stated
in Zhu--Wang. It is the local project's new family-specific signed-lift/defect-Choi calculation plus
the external pipeline above. Likewise, the claims `Q>0` on `(0,2/5)` and `P>0` on `(0,1/2)` are
local derivations preserved in the legacy record, not claims of the five papers in this ledger.

## Current interval ledger

The migrated library therefore keeps the following conservative statuses pending new-format
independent review of the exact frozen claims:

| Interval | Quantum capacity `Q` | Private capacity `P` | Provenance |
|---|---|---|---|
| `0 < x < 2/5` | local proof says `Q>0` | local proof says `P>0` | reviewed legacy derivations |
| `2/5 <= x < 1/2` | OPEN | local proof says `P>0` | quantum regularization gate unresolved |
| `1/2 <= x < 1` | local proof says `Q=P=0` | local proof says `Q=P=0` | local signed-lift extension + external pipeline |
| `x=1` | zero by self-complementarity/antidegradability | zero by the corresponding standard mechanism | endpoint handled separately |

The exact quantum threshold at `2/5` is a conjecture, not a completed theorem. One-shot coherent
information equal to zero on the strip cannot replace an all-blocklength proof.

## Local formal-verification boundary

The migrated Lean project documents a T1/T2/minimal-T3 development and carefully states that its
capacity interfaces remain assumptions. A fresh build could not be rerun on 2026-08-29 because the
local host has no `lake` or `lean` executable installed. This is an environment limitation, not a
failed proof build; the archived historical build/review evidence remains untouched.

## Review status

Primary PDFs, pages and hashes are now rebound. The next legitimate promotion step is an independent
new-format review of the exact local interval claims, especially the x-dependent signed-lift defect
calculation, private ensemble and positive-coherent-information expansion.
