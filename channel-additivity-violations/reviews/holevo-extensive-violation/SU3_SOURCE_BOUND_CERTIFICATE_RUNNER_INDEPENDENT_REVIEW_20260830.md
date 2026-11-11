# Independent review of the SU(3) source-bound certificate runner

Date: 2026-08-30 (America/New_York)

Reviewer: Codex root research agent. The runner implementation and initial fixtures were authored
by the separate `su3_source_bound_runner` agent. This review was performed after that author had
finished. The reviewer did not modify the runner implementation; the reviewer added negative
fixture cases before recording the verdict below.

## Reviewed objects and hashes

- canonical tool claim `HEXT.su3-source-bound-certificate-runner`:
  `sha256:ff2d6776ce8a490247e6c9fa9954da77aa3b62d784c91f5807bf0f67b72d6c05`;
- `tools/run_source_bound_certificate.py`:
  `sha256:81c5bfca00fd200333080573c41a52cba5a49e1b34938704706e32280de56413`;
- strengthened `tools/test_source_bound_certificate.py`:
  `sha256:4437fe0bb9be729a20d7efed023f888b00b7a943455a529e7337b5bcb56a01d6`;
- `artifacts/SU3_SOURCE_BOUND_CERTIFICATE_RUNNER_20260830.md`;
- both `20260830-2256` preparation-only manifest pairs and their frozen source trees; and
- the exact adaptive loops and terminal print sites in
  `certify_su3_input_centered_triangle_sixdim.py` and
  `certify_su3_triangular_three_face_clusters.py`.

The review also reran `python3 holevo-extensive-violation/tools/test_source_bound_certificate.py`
and the project structure/evidence checks.

## Finding SBCR-IR-01 — PASS: closure discovery is complete for the intended drivers

The implementation parses imports without importing the certificate, recursively resolves only
files inside the declared project root, and rejects the directly recognized nonliteral dynamic-
import forms. Each of the two intended fresh-run drivers has an ordinary static import graph with
no runtime loader, `exec`, aliased `import_module`, or generated module path. Manual enumeration
matches the seven records in each preparation manifest exactly. Every copied file is hash-checked
against the pre-copy record before launch.

This is a scoped verdict for the two audited SU(3) drivers and other certificates satisfying the
node's “statically resolvable” hypothesis. The wrapper is not a complete detector for arbitrary
Python metaprogramming; aliased loaders and non-import file dependencies require an explicit
manual audit or a future extension.

**Verdict:** PASS at claim hash `ff2d...`; no mathematical certificate is inferred.

## Finding SBCR-IR-02 — PASS: launch binding, snapshot isolation and drift policy

The prelaunch manifest is atomically written and fsynced before child creation. It binds the exact
wrapper, interpreter probe, command, working directory, environment, source hashes/sizes/mtimes,
configuration name and required terminal regular expressions. The child executes the copied entry
from the read-only source tree. During and after execution the wrapper rechecks the working-tree
records; it separately rehashes the frozen snapshot at the end. Content changes, disappearance,
or even a source retimestamp terminate or invalidate the run. Treating a pure retimestamp as drift
is conservative and intentional.

The two preparation-only dossiers correctly say `PREPARED_ONLY_NOT_EXECUTED`; they are operational
readiness evidence and cannot be mistaken for mathematical runs.

**Verdict:** PASS.

## Finding SBCR-IR-03 — PASS: transcript, termination and fail-closed branches

The child merges stderr into stdout, and the wrapper tees the byte stream to both the user and one
durable log, fsyncing the log before the final manifest. Signals are forwarded by terminating the
child and are recorded. The strengthened fixtures independently exercised:

1. a successful two-leaf run with an output hash;
2. mid-run source drift, returning wrapper code 86;
3. absent terminal certificate fields, returning code 87;
4. a nonzero child exit, retained in a `FAIL_CHILD_EXIT` manifest;
5. a nonliteral canonical `__import__` call, rejected before launch; and
6. attempted reuse of an evidence directory, rejected without overwrite.

All six branches produced the expected result.

**Verdict:** PASS.

## Finding SBCR-IR-04 — PASS: terminal-tree metadata for the audited adaptive certifiers

The two audited cores initialize one root box, increment `processed` once per popped box, and on
every uncertified nonterminal box append exactly two children. The terminal leaf line is printed
only after `while stack` exits. Consequently a successful explored tree is full binary, so a final
leaf count `L` implies exactly `L-1` internal splits, `2L-1` processed boxes and zero pending boxes.
The runner parses the last progress line, final leaf count and margin text and requires the leaf
and Bell-no-go terminal tokens by default. A future nonbinary certificate must not reuse this tree
interpretation without changing the runner or its evidence claim.

**Verdict:** PASS for the intended input-centered and weakest-bent fresh reruns.

## Overall verdict and limitations

The exact tool claim at `sha256:ff2d...` passes independent operational review. Keeping the node at
`NUMERICAL` is appropriate: the runner preserves provenance and fails closed, but it does not
validate entropy mathematics or promote any SU(3) orientation. A future heavy exit-zero dossier
still needs an independent mathematical review of the frozen checker, terminal transcript, exact
claim/route hashes, configuration and smallest certified margin.

No currently running legacy process is retroactively source-bound by this review. The wrapper is
for new run directories only.
