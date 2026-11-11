# SU(3) source-bound exact-certificate runner

Date: 2026-08-30 (America/New_York)

## Scope

This artifact documents an operational evidence tool.  It does **not** prove a Bell no-gap
inequality and it does not upgrade either of the two affected mathematical nodes.  Its narrow
purpose is to prevent the launch-source provenance failure that invalidated the historical
input-centered-triangle and weakest-bent fixed-three processes.

The implementation is
`holevo-extensive-violation/tools/run_source_bound_certificate.py` (SHA-256
`81c5bfca00fd200333080573c41a52cba5a49e1b34938704706e32280de56413`).  The fixture is
`holevo-extensive-violation/tools/test_source_bound_certificate.py` (SHA-256
`4437fe0bb9be729a20d7efed023f888b00b7a943455a529e7337b5bcb56a01d6`).

## SBCR-01 — Fail-closed protocol

Before launching a child interpreter the wrapper:

1. parses the entry script and every recursively resolved project-local Python import with the
   standard-library AST, without importing or executing any certificate module;
2. rejects nonliteral dynamic imports and unresolved relative imports;
3. records every closure file's repository-relative path, SHA-256, byte size, nanosecond mtime,
   and UTC mtime;
4. copies the closure into a run-specific source tree, verifies every copied hash, and makes the
   snapshot read-only;
5. records the exact Python executable, implementation, full version, `sys.path`, sanitized
   `PYTHONPATH`, working directory, argument vector, shell-escaped command, configuration name,
   UTC preparation time, and required terminal regular expressions; and
6. binds the wrapper itself by path, SHA-256, byte size and mtime, records its exact invocation,
   and atomically writes and fsyncs `manifest.prelaunch.json` before the child starts.

The child runs from the frozen entry file.  Its standard error is merged into standard output,
and every byte is simultaneously sent to the caller and to `stdout-stderr.log`.  While the child
runs, the wrapper rehashes/re-stats the original closure.  Any missing, modified, or merely
retimestamped closure file terminates the child and returns fail-closed exit code 86.  The wrapper
also rechecks the read-only snapshot and the working-tree closure after the child terminates.

`manifest.final.json` records start/end time, child and wrapper exit codes, output path/hash/size,
interrupt status, source-drift lists, final workspace closure, terminal-pattern matches, last
visible progress triple, final certified-leaf count, and the smallest-margin text.  A child exit
zero is insufficient: absent required terminal lines cause fail-closed exit code 87.

For these adaptive certifiers, a successful `adaptive compact boxes certified: L` line is printed
only after the stack is empty, and every rejected box creates exactly two children.  The wrapper
therefore records the exact full-binary-tree terminal counts

\[
\text{certified leaves}=L,\qquad
\text{internal splits}=L-1,\qquad
\text{processed boxes}=2L-1,\qquad
\text{pending}=0.
\]

This derivation is placed verbatim in the final manifest.  It avoids relying on the last periodic
`processed=..., certified=..., pending=...` checkpoint, which need not be the terminal count.

## SBCR-02 — Lightweight fixture verification

The fixture constructs a temporary two-file local import closure and runs a two-leaf mock
certificate.  It verifies:

- exact discovery of both local files;
- a `PASS` final manifest, output hash, required terminal tokens, and full-binary counts
  `(leaves, internal, processed, pending)=(2,1,3,0)`;
- source execution from the frozen copy; and
- fail-closed exit 86 after changing the original imported helper during a second run;
- fail-closed exit 87 for absent terminal certificate fields;
- propagation of a nonzero child exit and a `FAIL_CHILD_EXIT` manifest;
- fail-closed exit 87 for a nonliteral dynamic import; and
- refusal to overwrite an existing evidence directory.

Command and result:

```text
python3 holevo-extensive-violation/tools/test_source_bound_certificate.py
source-bound certificate wrapper success and fail-closed fixtures PASS
```

This is an operational regression fixture, not an independent review or a mathematical
certificate.

## Real-driver preparation-only checks

No heavy certificate was started.  Two `--prepare-only` checks exercised recursive closure
discovery and immutable snapshot creation on the actual drivers.

### Input-centered triangle

```text
python3 holevo-extensive-violation/tools/run_source_bound_certificate.py \
  --repo-root . \
  --project-root holevo-extensive-violation \
  --entry holevo-extensive-violation/tools/certify_su3_input_centered_triangle_sixdim.py \
  --config-name input-centered-four-side \
  --run-dir holevo-extensive-violation/artifacts/source-bound-wrapper-dry-run-input-centered-20260830-2256 \
  --prepare-only
```

Result: `PREPARED_ONLY_NOT_EXECUTED`; exactly seven project-local files were frozen.  The
prelaunch manifest SHA-256 is
`bc8ab5ceeae38a226e1b311bea0e2c2833ccbac26ce79e8b168ca3528ff87041`; the final preparation
manifest SHA-256 is
`3593893d3e0dc849b78ad0c5e5f856034d1aa2364e2d01f75b43ab6e5a01f05e`.

### Weakest bent fixed-three

```text
python3 holevo-extensive-violation/tools/run_source_bound_certificate.py \
  --repo-root . \
  --project-root holevo-extensive-violation \
  --entry holevo-extensive-violation/tools/certify_su3_weakest_bent_three_face_cluster.py \
  --config-name weakest-bent-fixed-three \
  --run-dir holevo-extensive-violation/artifacts/source-bound-wrapper-dry-run-weakest-bent-20260830-2256 \
  --prepare-only
```

Result: `PREPARED_ONLY_NOT_EXECUTED`; exactly seven project-local files were frozen.  The
prelaunch manifest SHA-256 is
`c6aa761bba4698a84b4a6cbc35c56c05c7f586172adacd8770ff907f2759a6c8`; the final preparation
manifest SHA-256 is
`c435a247af1293a245d991129afdee665d8709466aa1b8b76956756f226c9d0f`.

The seven-file closures exactly match the current-source closure enumerated independently in the
two static pre-reviews.  Because these were preparation-only runs, they provide no entropy
inequality evidence.

Two earlier development dry-runs remain preserved at
`source-bound-wrapper-dry-run-input-centered-20260830/` and
`source-bound-wrapper-dry-run-weakest-bent-20260830/`.  They also found seven files, but their
manifests predate the added self-hash of the wrapper.  They are retained as historical operational
records and are not the dossiers cited by the canonical tool node.

## Commands reserved for later fresh executions

The eventual heavy runs should use new, never-before-existing run directories.  For example:

```text
python3 holevo-extensive-violation/tools/run_source_bound_certificate.py \
  --repo-root . \
  --project-root holevo-extensive-violation \
  --entry holevo-extensive-violation/tools/certify_su3_input_centered_triangle_sixdim.py \
  --config-name input-centered-four-side \
  --run-dir holevo-extensive-violation/artifacts/source-bound-input-centered-<YYYYMMDD-HHMMSS>

python3 holevo-extensive-violation/tools/run_source_bound_certificate.py \
  --repo-root . \
  --project-root holevo-extensive-violation \
  --entry holevo-extensive-violation/tools/certify_su3_weakest_bent_three_face_cluster.py \
  --config-name weakest-bent-fixed-three \
  --run-dir holevo-extensive-violation/artifacts/source-bound-weakest-bent-<YYYYMMDD-HHMMSS>
```

The wrapper refuses to overwrite an existing run directory.  A future exit-zero dossier still
requires independent final review of the transcript, source manifest, terminal fields, and exact
claim/route hashes before any mathematical promotion.

## Limitations

- The static closure covers Python imports that resolve to project-local source.  Literal dynamic
  imports are included; nonliteral dynamic imports fail closed.  External packages are identified
  by the exact interpreter environment rather than copied.
- The stream is intentionally one complete merged stdout/stderr transcript so chronological byte
  order is preserved; separate stream identities are not retained.
- A read-only snapshot prevents accidental child-side edits but is not a cryptographic sandbox.
  Hash verification, source-drift termination, unique run directories, and independent review are
  the evidentiary controls.
- Preparation-only manifests demonstrate readiness and closure discovery only.  They do not count
  as certificate runs.
