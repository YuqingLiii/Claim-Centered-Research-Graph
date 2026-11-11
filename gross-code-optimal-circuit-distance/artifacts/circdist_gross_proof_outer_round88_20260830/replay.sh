#!/bin/sh
set -eu
PKG=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PY=${CIRCDIST_PYTHON:-python3}
if [ "${ROUND88_SKIP_MANIFEST:-0}" != 1 ]; then
  "$PY" "$PKG/source/check_manifests.py" --root "$PKG"
fi
REPO=$(CDPATH= cd -- "$PKG/../../.." 2>/dev/null && pwd || true)
if [ -n "$REPO" ] && [ -f "$REPO/operations/circdist/SCHEDULER.yaml" ]; then
  "$PY" "$PKG/source/check_protected.py" --package "$PKG" --repository "$REPO"
else
  "$PY" "$PKG/source/check_protected.py" --package "$PKG"
fi
TMPROOT=$(mktemp -d "${TMPDIR:-/tmp}/circdist-r88-replay.XXXXXX")
trap 'rm -rf "$TMPROOT"' EXIT HUP INT TERM
for ITER in 109 110 111 112; do
  F="$PKG/formulas/iter$ITER"
  T="$TMPROOT/iter$ITER"
  mkdir -p "$T"
  "$PY" - "$F/outer.cnf.gz" "$T/stored.cnf" "$F/assertion_map.jsonl.gz" "$T/stored.map" <<'PY'
import gzip,sys
from pathlib import Path
Path(sys.argv[2]).write_bytes(gzip.decompress(Path(sys.argv[1]).read_bytes()))
Path(sys.argv[4]).write_bytes(gzip.decompress(Path(sys.argv[3]).read_bytes()))
PY
  "$PY" "$PKG/source/compile_outer_cnf.py" --source "$F/source.json.gz" --cnf "$T/fresh.cnf" --metadata "$T/fresh.metadata.json" --assertion-map "$T/fresh.map" --definitions "$T/fresh.trace.json.gz"
  cmp "$T/fresh.cnf" "$T/stored.cnf"
  cmp "$T/fresh.map" "$T/stored.map"
  cmp "$T/fresh.trace.json.gz" "$F/circuit_trace.json.gz"
  "$PY" "$PKG/source/compare_json.py" "$F/metadata.json" "$T/fresh.metadata.json" --ignore compile_seconds
  "$PY" "$PKG/source/check_outer_encoding.py" --source "$F/source.json.gz" --cnf "$T/fresh.cnf" --metadata "$T/fresh.metadata.json" --assertion-map "$T/fresh.map" --definitions "$T/fresh.trace.json.gz" --output "$T/fresh.check.json"
  "$PY" "$PKG/source/compare_json.py" "$F/encoding_check.json" "$T/fresh.check.json" --ignore seconds
done
for ITER in 109 110 111; do
  F="$PKG/formulas/iter$ITER"
  I="$PKG/iterations/iter$ITER"
  T="$TMPROOT/iter$ITER"
  "$PY" "$PKG/source/verify_outer_sat_model.py" --solver-log "$I/outer/solver.log" --cnf "$T/fresh.cnf" --source "$F/source.json.gz" --metadata "$F/metadata.json" --frozen "$PKG/vendor/round80" --assignment "$T/assignment.dimacs" --candidate "$T/candidate.json" --output "$T/outer_replay.json"
  "$PY" - "$I/outer/assignment.dimacs.gz" "$T/stored.assignment" <<'PY'
import gzip,sys
from pathlib import Path
Path(sys.argv[2]).write_bytes(gzip.decompress(Path(sys.argv[1]).read_bytes()))
PY
  cmp "$T/assignment.dimacs" "$T/stored.assignment"
  cmp "$T/candidate.json" "$I/outer/candidate.json"
  "$PY" "$PKG/source/compare_json.py" "$I/outer/replay.json" "$T/outer_replay.json" --ignore seconds
  "$PY" "$PKG/vendor/round80/src/replay_direct_candidate.py" --root "$I/direct" --output "$T/direct_replay.json"
  cmp "$T/direct_replay.json" "$I/direct/direct_verification.json"
done
"$PY" "$PKG/source/check_continuation.py" --root "$PKG" --output "$TMPROOT/continuation.json"
cmp "$TMPROOT/continuation.json" "$PKG/verification/continuation_audit.json"
"$PY" "$PKG/source/check_proof_controls.py" --root "$PKG" --output "$TMPROOT/proof_controls.json"
"$PY" - "$TMPROOT/proof_controls.json" "$PKG/verification/proof_controls.json" <<'PY'
import json,sys
a=json.load(open(sys.argv[1]));b=json.load(open(sys.argv[2]))
keys=['status','fixture_cnf_sha256','valid_drat_sha256','generated_lrat_sha256','valid_drat_accepted','generated_lrat_accepted','corrupt_drat_rejected','truncated_drat_rejected','corrupt_lrat_rejected','truncated_lrat_rejected','scope']
assert all(a[k]==b[k] for k in keys)
PY
test ! -e "$PKG/iterations/iter112"
printf '%s\n' ROUND88_PACKAGE_REPLAY_PASS
