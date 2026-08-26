# Finite MDH structure reproduction

Recorded on 2026-08-25 (America/New_York; output timestamps are UTC).
This is a fresh computation, not a new independent proof review.
The node remains NUMERICAL.

## Run

```bash
python3 -m pip install -r se/tools/requirements.txt
python3 se/tools/check_mdh_structure.py --spectral
```

Without `--spectral`, the exact checks use only the Python standard library.
Use `--n 2 3` for the smaller exact cases.
Optional `--output <new-file>` saves a new JSON result and refuses overwrites.
The complete command currently exits with code 1 because of the reference
dimension discrepancy below; the check deliberately does not hide it.

## Results and one reference discrepancy

The n=2,3 checks pass. At n=4 the rebuilt full family table and within-tower
table agree exactly with the archived data. Orthogonality, recurrence, and
difference-operator checks also pass. There are respectively 8/26/94 cells,
6/19/61 canonical cells, and 5/13/51 orbits at n=2/3/4.

However, the recovered dimension dictionary gives (m_Y,m_N)=(4,1) for
(lambda,mu,nu)=((6,2),(3,1),(3,1)), while the block engine and archived
full table give (3,1). Accordingly the reference sum is 95, whereas the
rebuilt table has 94 cells. This disagreement is preserved in the input data
and `dimensions_match: false` in the output. Resolving which entry is
correct requires a separate check; no reference value was silently changed
to make this reproduction pass.

The n=3 random pencil-versus-SVD check has zero mismatches. The n=3 reference
spectrum agrees to about 3.11e-15. At n=4 the parity shape holds on all 51
orbit images, and the saved parameter vector reproduces the recorded block
singular values. These floating-point checks are narrower than an exact
all-n spectral theorem and do not rerun the optimization.

## Programs and inputs

The node links every program and input directly.

- `mdh_engine.py` and `mdh_blocks.py`: exact representation and block calculations.
- `mdh_family.py`: the full finite family, Gram, recurrence, and difference checks.
- `mdh_phi_tower.py`, `mdh_closed_tower.py`, and `mdh_marked_subset_d1.py`: within-tower generation.
- `mdh_sigma.py` and `mdh_certify.py`: pencil, direct reconstruction, and reference comparisons.
- `mdh_n4_d1.py` and `mdh_fast.py`: the saved n=4 parity and spectral calculation.
- `mdh_n4_block.py`: regeneration of the exact 3-by-2 block data.

`mdh_dimensions.json` is the dimension dictionary extracted from the
original reference dataset; unrelated sections were omitted.
`blocks_n3.json`, `mdh_family_n4.json`, `mdh_n4_521_block.json`, and
`mdh_opt_t_n4.npy` are the retained finite data used by those checks.
They are not assumed to be independently validated theorems.

All data paths resolve relative to the SE project, not a particular
computer. The table generator and optimizer write no files unless an
explicit new output path is given. Existing outputs are never overwritten.

## Output

[mdh_structure_reproduction_20260825.json](mdh_structure_reproduction_20260825.json)
records all checks, the failed reference comparison, source/input hashes,
Python 3.12.13, and NumPy 2.3.5. The exact formulas are evaluated at the
listed finite n only. This record neither proves an all-n statement nor
justifies a completion-level promotion.
