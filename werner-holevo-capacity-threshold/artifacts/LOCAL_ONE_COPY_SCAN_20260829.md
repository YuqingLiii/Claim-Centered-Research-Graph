# Local one-copy coherent-information scan

Date: 2026-08-29  
Status: numerical evidence only; not a global optimization certificate.

## Purpose

This reruns a one-copy qutrit-state search locally from the Kraus definition, independently of the
old Windows JSON outputs. The goal is to check the numerical landscape on the remaining strip
`[2/5,1/2)` and to retain a reproducible positive control below the proposed threshold.

Script: `scripts/whgap_one_copy_scan.py`  
SHA-256: `f27ea88936d0fbed2076088f35ff11cae5e1b52b48e172af893af2dc9384b224`

Interpreter used:

`<home>/Documents/Codex/Release-Audits/2026-08-25-clean-publication/program-recovery/.venv/bin/python`

Versions: CPython 3.12.13, NumPy 2.3.5, SciPy 1.15.3.

## Method

For each `x`, the script constructs

\[
K_0=\sqrt{1-x}I,\qquad K_i=\sqrt{x/2}\,A_i
\]

and independently checks their receiver output against

\[
\Lambda_x(\rho)=(1-x)\rho+\frac{x}{2}(I-\rho^T).
\]

It evaluates coherent information for:

- the exact pure-state zero baseline;
- the maximally mixed state;
- 34 isotropic rank-two near-pure states, down to mixing weight `10^-12`;
- 500 random rank-two and 500 random rank-three states; and
- 12 locally polished seeds on each of the rank-two and rank-three parameter strata.

Each parameterization is `rho=T T*/Tr(T T*)`, so positivity is automatic. The search covers
singular strata through the separate ranks and structured seeds, but finite starts do not prove a
global maximum.

Command:

```sh
<home>/Documents/Codex/Release-Audits/2026-08-25-clean-publication/program-recovery/.venv/bin/python \
  werner-holevo-capacity-threshold/artifacts/scripts/whgap_one_copy_scan.py \
  --x 0.39 0.4 0.41 0.45 0.49 --random-per-rank 500 --polish 12
```

## Results

There were 1,060 evaluated candidates per `x`. The Kraus/formula Frobenius residual stayed below
`9e-17`.

| `x` | best `I_c` (bits) | winner | candidates above `1e-9` bits | `I_c(I/3)` (bits) |
|---:|---:|---|---:|---:|
| 0.39 | `2.0275769348e-3` | maximally mixed | 34 | `2.0275769348e-3` |
| 0.40 | `8.82e-14` | numerical near-pure floor | 0 | `-1.9973094022e-2` |
| 0.41 | `8.73e-14` | numerical near-pure floor | 0 | `-4.1372593332e-2` |
| 0.45 | `1.16e-13` | numerical near-pure floor | 0 | `-1.2104507859e-1` |
| 0.49 | `4.17e-14` | numerical near-pure floor | 0 | `-1.9138056639e-1` |

At every strip point the reported numerical winner has spectrum within about `1e-14` of a pure
state, whose coherent information is exactly zero. No candidate exceeded `1e-9` bits. The `x=0.39`
positive control is macroscopic and is recovered at the maximally mixed state.

## Interpretation

This fresh run agrees with the legacy landscape: one-copy numerical searches collapse to the pure
zero floor at and above `2/5`. It supplies no upper bound on

\[
Q^{(1)}(\Lambda_x)=\max_\rho I_c(\rho,\Lambda_x),
\]

and even a proof that `Q^(1)=0` would not imply the regularized statement `Q=0`. The remaining
all-blocklength strip is therefore unchanged.

The useful narrowing is methodological: another generic one-copy optimizer run is unlikely to
decide the problem. A successful route must certify the one-copy global bound analytically and then
control entangled multi-copy inputs, or bypass coherent-information optimization via a tensorizing
order/certificate.
