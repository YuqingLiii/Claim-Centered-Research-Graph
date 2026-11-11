#!/bin/sh
set -eu

PKG=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if [ -n "${CIRCDIST_PYTHON:-}" ]; then
  PY=$CIRCDIST_PYTHON
elif [ -x /private/tmp/circdist-r72-dispatcher-venv/bin/python ]; then
  PY=/private/tmp/circdist-r72-dispatcher-venv/bin/python
else
  PY=python3
fi
"$PY" -c 'import z3, pysat; print("DEPENDENCIES_PASS", z3.get_version_string(), pysat.__version__)'

if [ "${ROUND90_SKIP_MANIFEST:-0}" != 1 ]; then
  "$PY" "$PKG/source/check_manifests.py" --root "$PKG"
fi

REPO=$(CDPATH= cd -- "$PKG/../../.." 2>/dev/null && pwd || true)
if [ -n "$REPO" ] && [ -f "$REPO/operations/circdist/SCHEDULER.yaml" ]; then
  "$PY" "$PKG/source/check_protected.py" --package "$PKG" --repository "$REPO"
else
  "$PY" "$PKG/source/check_protected.py" --package "$PKG"
fi

TMPROOT=$(mktemp -d "${TMPDIR:-/tmp}/circdist-r90-replay.XXXXXX")
cleanup_round90_replay() {
  "$PY" - "$TMPROOT" <<'PY'
from pathlib import Path
import shutil,sys
shutil.rmtree(Path(sys.argv[1]), ignore_errors=True)
PY
}
trap cleanup_round90_replay EXIT HUP INT TERM

for ITER in 112 113 114 115 116 117 118 119 120 121 122 123 124; do
  F="$PKG/formulas/iter$ITER"
  T="$TMPROOT/iter$ITER"
  mkdir -p "$T"
  "$PY" - "$F/outer.cnf.gz" "$T/stored.cnf" "$F/assertion_map.jsonl.gz" "$T/stored.map" <<'PY'
import gzip,sys
from pathlib import Path
Path(sys.argv[2]).write_bytes(gzip.decompress(Path(sys.argv[1]).read_bytes()))
Path(sys.argv[4]).write_bytes(gzip.decompress(Path(sys.argv[3]).read_bytes()))
PY
  "$PY" "$PKG/source/compile_outer_cnf.py" \
    --source "$F/source.json.gz" \
    --cnf "$T/fresh.cnf" \
    --metadata "$T/fresh.metadata.json" \
    --assertion-map "$T/fresh.map" \
    --definitions "$T/fresh.trace.json.gz"
  cmp "$T/fresh.cnf" "$T/stored.cnf"
  cmp "$T/fresh.map" "$T/stored.map"
  cmp "$T/fresh.trace.json.gz" "$F/circuit_trace.json.gz"
  "$PY" "$PKG/source/compare_json.py" \
    "$F/metadata.json" "$T/fresh.metadata.json" --ignore compile_seconds
  "$PY" "$PKG/source/check_outer_encoding.py" \
    --source "$F/source.json.gz" \
    --cnf "$T/fresh.cnf" \
    --metadata "$T/fresh.metadata.json" \
    --assertion-map "$T/fresh.map" \
    --definitions "$T/fresh.trace.json.gz" \
    --output "$T/fresh.check.json"
  "$PY" "$PKG/source/compare_json.py" \
    "$F/encoding_check.json" "$T/fresh.check.json" --ignore seconds
done

for ITER in 112 113 114 115 116 117 118 119 120 121 122 123; do
  F="$PKG/formulas/iter$ITER"
  I="$PKG/iterations/iter$ITER"
  T="$TMPROOT/iter$ITER"
  "$PY" "$PKG/source/verify_outer_sat_model.py" \
    --solver-log "$I/outer/solver.log" \
    --cnf "$T/fresh.cnf" \
    --source "$F/source.json.gz" \
    --metadata "$F/metadata.json" \
    --frozen "$PKG/vendor/round80" \
    --assignment "$T/assignment.dimacs" \
    --candidate "$T/candidate.json" \
    --output "$T/outer_replay.json"
  "$PY" - "$I/outer/assignment.dimacs.gz" "$T/stored.assignment" <<'PY'
import gzip,sys
from pathlib import Path
Path(sys.argv[2]).write_bytes(gzip.decompress(Path(sys.argv[1]).read_bytes()))
PY
  cmp "$T/assignment.dimacs" "$T/stored.assignment"
  cmp "$T/candidate.json" "$I/outer/candidate.json"
  "$PY" "$PKG/source/compare_json.py" \
    "$I/outer/replay.json" "$T/outer_replay.json" --ignore seconds

  SELECTORS=$("$PY" - "$F/metadata.json" <<'PY'
import json,sys
print(json.load(open(sys.argv[1]))['selector_count'])
PY
  )
  D="$T/direct_rebuilt"
  "$PY" "$PKG/source/build_direct_from_candidate.py" \
    --candidate "$I/outer/candidate.json" \
    --output "$D" \
    --vendor "$PKG/vendor/round80" \
    --source-selector-count "$SELECTORS"
  cmp "$D/candidate.json" "$I/direct/candidate.json"
  cmp "$D/build_summary.json" "$I/direct/build_summary.json"
  for SECTOR in Xerr Zerr; do
    for SUFFIX in cnf variables.json columns.json clauses.jsonl summary.json; do
      cmp "$D/direct360/$SECTOR.$SUFFIX" "$I/direct/direct360/$SECTOR.$SUFFIX"
    done
  done
  mkdir -p "$D/solver"
  cp "$I/direct/solver/Xerr.solver.log" "$D/solver/Xerr.solver.log"
  cp "$I/direct/solver/Zerr.solver.log" "$D/solver/Zerr.solver.log"
  "$PY" "$PKG/vendor/round80/src/replay_direct_candidate.py" \
    --root "$D" --output "$T/direct_replay.json"
  cmp "$T/direct_replay.json" "$I/direct/direct_verification.json"
done

"$PY" "$PKG/source/check_continuation.py" \
  --root "$PKG" --output "$TMPROOT/continuation.json"
cmp "$TMPROOT/continuation.json" "$PKG/verification/continuation_audit.json"

cp "$PKG/bindings/round88/final_state.json" "$TMPROOT/state112.json"
STATE="$TMPROOT/state112.json"
for ITER in 112 113 114 115 116 117 118 119 120 121 122 123; do
  NEXT=$((ITER + 1))
  T="$TMPROOT/transition$ITER"
  mkdir -p "$T"
  "$PY" "$PKG/source/advance_round90.py" \
    --vendor "$PKG/vendor/round80" \
    --state-in "$STATE" \
    --source-in "$PKG/formulas/iter$ITER/source.json.gz" \
    --iteration "$ITER" \
    --candidate "$PKG/iterations/iter$ITER/outer/candidate.json" \
    --direct "$PKG/iterations/iter$ITER/direct/direct_verification.json" \
    --state-out "$T/state.json" \
    --record-out "$T/record.json" \
    --source-out "$T/source.json.gz"
  cmp "$T/record.json" "$PKG/iterations/iter$ITER/record.json"
  cmp "$T/source.json.gz" "$PKG/formulas/iter$NEXT/source.json.gz"
  STATE="$T/state.json"
done
cmp "$STATE" "$PKG/continuation/final_state.json"

"$PY" "$PKG/source/check_result.py" --root "$PKG"
"$PY" "$PKG/source/check_process_ledger.py" --root "$PKG"
"$PY" "$PKG/source/check_actual_sat_trace_controls.py" --root "$PKG"
"$PY" "$PKG/source/check_proof_controls.py" \
  --root "$PKG" --output "$TMPROOT/proof_controls.json"
"$PY" - "$TMPROOT/proof_controls.json" "$PKG/verification/proof_controls.json" <<'PY'
import json,sys
a=json.load(open(sys.argv[1])); b=json.load(open(sys.argv[2]))
keys=[
  'status','fixture_cnf_sha256','valid_drat_sha256','generated_lrat_sha256',
  'valid_drat_accepted','generated_lrat_accepted','corrupt_drat_rejected',
  'truncated_drat_rejected','corrupt_lrat_rejected','truncated_lrat_rejected','scope'
]
assert all(a[k] == b[k] for k in keys)
PY
test ! -e "$PKG/iterations/iter124"
printf '%s\n' ROUND90_PACKAGE_REPLAY_PASS
