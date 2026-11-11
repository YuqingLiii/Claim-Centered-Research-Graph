# WHGAP antidegradability boundary commission P1

## Outcome

**STOPPED before gate G0; no boundary claim.**

The frozen commission requires every Python invocation to use:

```text
C:<home>/AppData/Local/Microsoft/WindowsApps/python.exe
```

The Step 0 invocation failed before the calibration script could start because PowerShell could not
resolve the pinned executable. A read-only follow-up probe returned `TestPath = False`,
`ParentExists = True`, together with `UnauthorizedAccessException` for the pinned executable.
Substituting another interpreter would violate the frozen conventions, so no substitution was made.

## Gate record

- G0: **NOT EVALUATED**. None of C1–C6 ran.
- G1: **NOT RUN** (forbidden until G0 passes).
- G2: **NOT RUN**.
- Exactness attempt S4: **NOT RUN**.
- Boundary bracket and value: **none**.

## Files and provenance

- Step 0 script prepared exactly for C1–C6:
  [`tools/whgap_p0_calibration.py`](../tools/whgap_p0_calibration.py)
- Failed invocation record:
  [`logs_whgap_20260728/whgap_p0_calibration.log`](logs_whgap_20260728/whgap_p0_calibration.log)
- Checksums:
  [`logs_whgap_20260728/SHA256SUMS.txt`](logs_whgap_20260728/SHA256SUMS.txt)

## Required validators

Neither validator was run. Both are Python commands and the commission requires the same inaccessible
pinned interpreter for every Python invocation. Their required exit-0 condition is therefore unmet.

## Runtime and budget

The stop occurred immediately at interpreter launch, well within the 60-minute compute budget. No SDP
solve was started.

## Run 2 — calibration and boundary scan

**Gate G0: PASS.** C1–C6 passed exactly under the environment addendum.

**Gate G1: PASS.** The endpoint tests match Zhu–Wang and RK24.

| label | x | t*(x) | final status | runtime (s) |
|---|---:|---:|---|---:|
| G1-low | 0.500000000000 | -6.944444443839e-04 | optimal | 0.363 |
| G1-high | 0.571428571429 | 9.912112677079e-13 | optimal | 0.024 |
| bisect-01 | 0.535714285714 | -1.778458024528e-04 | optimal | 0.010 |
| bisect-02 | 0.553571428571 | -4.501011886658e-05 | optimal | 0.015 |
| bisect-03 | 0.562500000000 | -1.132228618881e-05 | optimal | 0.018 |
| bisect-04 | 0.566964285714 | -2.839316370226e-06 | optimal | 0.014 |
| bisect-05 | 0.569196428571 | -7.109007153690e-07 | optimal | 0.011 |
| bisect-06 | 0.570312500000 | -1.778462747503e-07 | optimal | 0.012 |
| bisect-07 | 0.570870535714 | -4.448741804719e-08 | optimal | 0.058 |
| bisect-08 | 0.571149553571 | -1.112906467116e-08 | optimal | 0.056 |
| bisect-09 | 0.571289062500 | -2.783796548297e-09 | optimal | 0.035 |
| bisect-10 | 0.571358816964 | -6.962940384846e-10 | optimal | 0.055 |
| bisect-11 | 0.571393694196 | -1.743117624894e-10 | optimal | 0.027 |
| bisect-12 | 0.571411132812 | -4.369338524504e-11 | optimal | 0.022 |
| bisect-13 | 0.571419852121 | -1.098118983037e-11 | optimal | 0.023 |
| bisect-14 | 0.571424211775 | -2.773207910847e-12 | optimal | 0.018 |
| bisect-15 | 0.571426391602 | -7.078245773967e-13 | optimal | 0.017 |
| bisect-16 | 0.571427481515 | -1.858627004104e-13 | optimal | 0.021 |
| bisect-17 | 0.571428026472 | -5.023088127173e-14 | optimal | 0.017 |
| bisect-18 | 0.571428298950 | -1.310552952084e-14 | optimal | 0.019 |
| bisect-19 | 0.571428435189 | 5.171204572705e-12 | optimal | 0.016 |
| bisect-20 | 0.571428367070 | -2.591277813870e-12 | optimal | 0.016 |
| bisect-21 | 0.571428401130 | 1.289920730307e-12 | optimal | 0.017 |
| bisect-22 | 0.571428384100 | -5.804724180541e-13 | optimal | 0.015 |
| bisect-23 | 0.571428392615 | 2.824256025374e-13 | optimal | 0.026 |

### Boundary and gate G2

- Infeasible-side endpoint: `0.571428384100`.
- Feasible-side endpoint: `0.571428392615`.
- Bracket width: `8.515e-09`.
- Reported midpoint: `x* = 0.571428388357`.
- **G2 finding: 4/7 numerically tight.**

### Exactness attempt

- Rationalization: `{"denominator_le_200": "4/7", "midpoint": 0.5714283883571625, "quadratic_surd_candidate": "sqrt(3)/log(239/26 + 9*sqrt(1109)/26)", "quadratic_surd_numeric": 0.5714283883144421, "rational_error": 1.8307140892126483e-07, "rational_inside_bracket": false}`.
- Feasible-side rational projection: `{"affine_projection_exact": true, "exact_negative_rayleigh_quotient": "-220351515538070925056194478700405689270009061753999485158080218183495051401104570403607535671542260525152029962778169208238074145421852247295586532522458755231171122183160976283653762416387583/4576620472758856864007760157756787089907720889510773852862816346603197528587577909828987746056710199861486584193339895841768057535279278370025676206185996057673273678036558269574502308670000000000000000", "exact_psd": false, "exact_psd_outcome": "failed: the affine-projected rational candidate has an exact negative rational Rayleigh form", "numeric_min_eigenvalue_after_exact_projection": -4.8148158154015614e-11, "x_rational": "22548571244/39460012025"}`.
- Infeasible-side dual attempt: `{"dual_entries": 81, "exact_infeasibility_witness": false, "max_rounding_error": 2.1258689253400576e-12, "outcome": "candidate extracted and rationalized, but no exact dual-feasibility certificate was obtained", "x": 0.5714283840996878}`.

No exact feasibility certificate or exact infeasibility witness is claimed unless explicitly marked successful above.

### Run-2 provenance and runtime

- Calibration log: [`logs_whgap_20260728/whgap_p0_calibration_run2_final.log`](logs_whgap_20260728/whgap_p0_calibration_run2_final.log).
- SDP stdout log: [`logs_whgap_20260728/whgap_p1_antideg_boundary.log`](logs_whgap_20260728/whgap_p1_antideg_boundary.log).
- Full solve table: [`logs_whgap_20260728/whgap_p1_scan.csv`](logs_whgap_20260728/whgap_p1_scan.csv).
- Machine summary: [`logs_whgap_20260728/whgap_p1_summary.json`](logs_whgap_20260728/whgap_p1_summary.json).
- Total Step-1 runtime: `12.647 s`.

**Status discipline:** numerical evidence only; independent rule-7 review remains pending.

### Run-2 interpretation caveats (post-run audit)

- The final bisection signs have magnitude about `10^-12`, below the requested `10^-11`
  SCS accuracy setting in objective-value terms. The displayed width `8.515e-09` is therefore a
  solver-sign bracket, not an exact feasibility/infeasibility certificate. The stable numerical
  conclusion is only the pre-registered G2 statement **“4/7 numerically tight”**: the reported
  midpoint differs from `4/7` by `1.831e-07`, within the G2 tolerance `1e-6`.
- The denominator-`<=200` rationalization returned `4/7`, but it lies outside the solver-sign
  bracket for the same resolution-floor reason. It is a candidate supported by the G2 comparison,
  not an exact identification.
- The unrestricted `sympy.nsimplify(..., full=True)` diagnostic printed a transcendental
  log expression under the JSON key `quadratic_surd_candidate`. That expression is **rejected**:
  it is not a quadratic surd and carries no evidentiary weight.
- The feasible-side rational affine projection failed exact PSD via the exact negative Rayleigh
  form recorded above, and the dual rationalization did not yield an exact dual-feasibility
  certificate. Thus S4 produced no exact certificate on either side.

