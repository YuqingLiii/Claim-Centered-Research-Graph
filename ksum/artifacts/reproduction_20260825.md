# Finite solver and audit reproductions

Recorded on 2026-08-25 (America/New_York; timestamps in the output are UTC).
These are fresh runs of the linked programs, not recovered July logs or new
independent mathematical reviews. All nine commands exited successfully.
No mathematical claim or evidence level was changed.

Install the numerical dependencies with
`python3 -m pip install -r ksum/tools/requirements.txt`.
The F1 and R3 checks use only the Python standard library. Run the following
commands from the repository root; they write to stdout by default.

## L32: direct solver

```bash
python3 ksum/tools/ksum_stage0_d_direct_adv.py 3 3 0 SCS 1e-4 60000
python3 ksum/tools/ksum_stage0_d_direct_adv.py 4 3 0 SCS 1e-4 60000
```

The outputs are 2.418636 and 2.712711, matching the displayed values in the
archived atlas. These are low-precision numerical optima, not exact SDP
certificates. Tighter tolerances give approximately 2.418246 and 2.71216.

## L33: reduced solver

```bash
python3 ksum/tools/ksum_l33_reduced_adv.py 3 3 0 --solver SCS --eps 1e-8 --max-iters 500000 --audit
python3 ksum/tools/ksum_l33_reduced_adv.py 4 3 0 --solver SCS --eps 1e-7 --max-iters 500000 --audit
python3 ksum/tools/ksum_l33r_structure_audit.py --instances '3,3,0;4,3,0'
python3 ksum/tools/ksum_l33r_unreduced_check.py 3 3 0 --solver SCS --eps 1e-6 --max-iters 500000
```

The reduced values are 2.4182463724571046 and 2.7121592868171587.
The separate unreduced n=3 check gives 2.4182464604918477.
The structure audit passes both instances.

The full reconstructed matrices have maximum equality residuals about
6.45e-12 and 6.94e-11, diagonal constraint violations about 1.54e-8 and
9.34e-8, and minimum eigenvalues about -7.85e-9 and -8.63e-8.
These residuals are retained rather than presented as exact feasibility.
The fresh checks do not repeat all historical large-instance MOSEK runs or
the timeout experiments.

## A1f: encoding, inherited floor, and parity

```bash
python3 ksum/tools/ksum_f1_embed.py
python3 ksum/tools/ksum_f1_floor.py
python3 ksum/tools/ksum_r3_parity.py
```

F1 checks 58,033 encoding inputs and 47,496 inherited-floor inputs, with all
tests passing. The same finite check results and negative controls appear
in the archived F1 logs; runtime and header information differ.
The R3 parity checks also pass. This does not prove the all-parameter lemmas.

The F1 programs accept `--output <new-file>` for an additional log and
refuse to overwrite an existing file. Importing either module writes nothing.
Fresh headers distinguish reruns from the original independent audit.
The R3 success label is PASS for the checked finite instances, not PROVED.

## Recorded output

[solver_reproduction_20260825.json](solver_reproduction_20260825.json)
contains the commands, current source hashes, runtime versions, exit codes,
and complete captured output. Local executable/workspace prefixes are
normalized for publication. The runtime was Python 3.12.13, NumPy 2.3.5,
SciPy 1.15.3, CVXPY 1.7.1, and SCS 3.2.8.

Historical checksum files continue to describe their original programs and
logs. They were not rewritten to describe these portable entry points.
