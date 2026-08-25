# Set Equality numerator: fresh n=3 corroboration

- Date: 2026-08-19
- Command: `python3 tools/se_n3_ground_truth.py`
- Source: `tools/se_n3_ground_truth.py`
- Purpose: independently recompute the finite n=3 witness for K=1,2,3 after
  correcting the canonical numerator claim.

Relevant output:

```text
|Y|,|N| = 720 720   q! = 720
sum_k P_k == I ? True
P_k idempotent? True
P_0 uN = uN ? True   max_k>0 ||P_k uN|| = 2.351206340748488e-16

 K   ||Gamma||      ||Gamma uN - K uY||   ||Gamma||/K
 1   1.00000000    1.862e-16               1.00000000
 2   2.00000000    5.140e-16               1.00000000
 3   3.00000000    1.155e-15               1.00000000
```

This finite computation corroborates the formula `Gamma_n 1_N = K 1_Y` at
`n=3`. It is not a proof of the all-`n` claim; the proof is the symbolic
argument in `se/paper/se_explicit_witness.tex`, Lemma
`lem:numerator`.
