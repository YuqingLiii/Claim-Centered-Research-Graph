#!/bin/sh
set -eu

PKG=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if [ -n "${ROUND92_REPOSITORY:-}" ]; then
  REPO=$ROUND92_REPOSITORY
else
  REPO=$(CDPATH= cd -- "$PKG/../../.." && pwd)
fi
DEP="$REPO/circdist/artifacts/circdist_gross_proof_outer_round90_20260830"
if [ -n "${CIRCDIST_PYTHON:-}" ]; then
  PY=$CIRCDIST_PYTHON
elif [ -x /private/tmp/circdist-r72-dispatcher-venv/bin/python ]; then
  PY=/private/tmp/circdist-r72-dispatcher-venv/bin/python
else
  PY=python3
fi
"$PY" -c 'import z3,pysat;print("DEPENDENCIES_PASS",z3.get_version_string(),pysat.__version__)'

if [ "${ROUND92_SKIP_MANIFEST:-0}" != 1 ]; then
  "$PY" "$PKG/source/check_manifests.py" --root "$PKG"
fi
"$PY" "$PKG/source/check_protected.py" --package "$PKG" --repository "$REPO"

TMPROOT=$(mktemp -d "${TMPDIR:-/tmp}/circdist-r92-replay.XXXXXX")
cleanup_round92_replay() {
  "$PY" - "$TMPROOT" <<'PY'
from pathlib import Path
import shutil,sys
shutil.rmtree(Path(sys.argv[1]),ignore_errors=True)
PY
}
trap cleanup_round92_replay EXIT HUP INT TERM

printf '%s\n' PHASE_A_SYNTHESIS_REPLAY_START
"$PY" "$PKG/source/weight9_synthesis.py" --repo "$REPO" --output "$TMPROOT/weight9_synthesis.json"
cmp "$TMPROOT/weight9_synthesis.json" "$PKG/synthesis/weight9_synthesis.json"
"$PY" "$PKG/source/install_preouter.py" \
  --source-in "$DEP/formulas/iter124/source.json.gz" \
  --state-in "$PKG/continuation/inherited_iter124_state.json" \
  --synthesis "$TMPROOT/weight9_synthesis.json" \
  --source-out "$TMPROOT/preouter.source.json.gz" \
  --state-out "$TMPROOT/preouter.state.json" \
  --record-out "$TMPROOT/preouter.record.json"
cmp "$TMPROOT/preouter.source.json.gz" "$PKG/formulas/iter124/source.json.gz"
cmp "$TMPROOT/preouter.state.json" "$PKG/continuation/preouter_iter124_state.json"
cmp "$TMPROOT/preouter.record.json" "$PKG/preouter/atomic_install.json"

for ITER in 124 125 126 127 128 129 130 131 132 133 134 135 136; do
  F="$PKG/formulas/iter$ITER"; T="$TMPROOT/iter$ITER"; mkdir -p "$T"
  "$PY" - "$F/outer.cnf.gz" "$T/stored.cnf" "$F/assertion_map.jsonl.gz" "$T/stored.map" <<'PY'
import gzip,sys
from pathlib import Path
Path(sys.argv[2]).write_bytes(gzip.decompress(Path(sys.argv[1]).read_bytes()))
Path(sys.argv[4]).write_bytes(gzip.decompress(Path(sys.argv[3]).read_bytes()))
PY
  "$PY" "$PKG/source/compile_outer_cnf.py" --source "$F/source.json.gz" --cnf "$T/fresh.cnf" --metadata "$T/fresh.metadata.json" --assertion-map "$T/fresh.map" --definitions "$T/fresh.trace.json.gz"
  cmp "$T/fresh.cnf" "$T/stored.cnf"; cmp "$T/fresh.map" "$T/stored.map"; cmp "$T/fresh.trace.json.gz" "$F/circuit_trace.json.gz"
  "$PY" "$PKG/source/compare_json.py" "$F/metadata.json" "$T/fresh.metadata.json" --ignore compile_seconds
  "$PY" "$PKG/source/check_outer_encoding.py" --source "$F/source.json.gz" --cnf "$T/fresh.cnf" --metadata "$T/fresh.metadata.json" --assertion-map "$T/fresh.map" --definitions "$T/fresh.trace.json.gz" --output "$T/fresh.check.json"
  "$PY" "$PKG/source/compare_json.py" "$F/encoding_check.json" "$T/fresh.check.json" --ignore seconds
  printf 'FORMULA_REPLAY_PASS %s\n' "$ITER"
done

"$PY" "$PKG/source/build_strict_expansion_query.py" --cnf "$TMPROOT/iter124/fresh.cnf" --map "$TMPROOT/iter124/fresh.map" --old-count 164 --output "$TMPROOT/strict.cnf" --summary "$TMPROOT/strict.query.json"
"$PY" - "$PKG/preouter/strict_expansion.cnf.gz" "$TMPROOT/stored.strict.cnf" "$PKG/preouter/strict_expansion.assignment.dimacs.gz" "$TMPROOT/stored.strict.assignment" <<'PY'
import gzip,sys
from pathlib import Path
Path(sys.argv[2]).write_bytes(gzip.decompress(Path(sys.argv[1]).read_bytes()))
Path(sys.argv[4]).write_bytes(gzip.decompress(Path(sys.argv[3]).read_bytes()))
PY
cmp "$TMPROOT/strict.cnf" "$TMPROOT/stored.strict.cnf"; cmp "$TMPROOT/strict.query.json" "$PKG/preouter/strict_expansion_query.json"
"$PY" "$PKG/source/verify_strict_expansion_sat.py" --solver-log "$PKG/preouter/strict_expansion.solver.log" --cnf "$TMPROOT/strict.cnf" --source "$PKG/formulas/iter124/source.json.gz" --metadata "$PKG/formulas/iter124/metadata.json" --vendor "$DEP/vendor/round80" --old-count 164 --assignment "$TMPROOT/strict.assignment" --candidate "$TMPROOT/strict.candidate.json" --output "$TMPROOT/strict.verification.json"
cmp "$TMPROOT/strict.assignment" "$TMPROOT/stored.strict.assignment"; cmp "$TMPROOT/strict.candidate.json" "$PKG/preouter/strict_expansion.candidate.json"; cmp "$TMPROOT/strict.verification.json" "$PKG/preouter/strict_expansion.verification.json"
printf '%s\n' PHASE_A_STRICT_EXPANSION_REPLAY_PASS

STATE="$PKG/continuation/preouter_iter124_state.json"
for ITER in 124 125 126 127 128 129 130 131 132 133 134 135; do
  F="$PKG/formulas/iter$ITER"; I="$PKG/iterations/iter$ITER"; T="$TMPROOT/iter$ITER"
  "$PY" "$PKG/source/verify_outer_sat_model.py" --solver-log "$I/outer/solver.log" --cnf "$T/fresh.cnf" --source "$F/source.json.gz" --metadata "$F/metadata.json" --frozen "$DEP/vendor/round80" --assignment "$T/assignment.dimacs" --candidate "$T/candidate.json" --output "$T/outer_replay.json"
  "$PY" - "$I/outer/assignment.dimacs.gz" "$T/stored.assignment" <<'PY'
import gzip,sys
from pathlib import Path
Path(sys.argv[2]).write_bytes(gzip.decompress(Path(sys.argv[1]).read_bytes()))
PY
  cmp "$T/assignment.dimacs" "$T/stored.assignment"; cmp "$T/candidate.json" "$I/outer/candidate.json"
  "$PY" "$PKG/source/compare_json.py" "$I/outer/replay.json" "$T/outer_replay.json" --ignore seconds
  SELECTORS=$((208 + 2 * (ITER - 124)))
  D="$T/direct_rebuilt"
  "$PY" "$PKG/source/build_direct_from_candidate.py" --candidate "$I/outer/candidate.json" --output "$D" --vendor "$DEP/vendor/round80" --source-selector-count "$SELECTORS"
  cmp "$D/candidate.json" "$I/direct/candidate.json"; cmp "$D/build_summary.json" "$I/direct/build_summary.json"
  for SECTOR in Xerr Zerr; do
    for SUFFIX in cnf variables.json columns.json clauses.jsonl summary.json; do cmp "$D/direct360/$SECTOR.$SUFFIX" "$I/direct/direct360/$SECTOR.$SUFFIX"; done
    mkdir -p "$D/solver"; cp "$I/direct/solver/$SECTOR.solver.log" "$D/solver/$SECTOR.solver.log"
  done
  "$PY" "$DEP/vendor/round80/src/replay_direct_candidate.py" --root "$D" --output "$T/direct_replay.json"
  cmp "$T/direct_replay.json" "$I/direct/direct_verification.json"
  NEXT=$((ITER + 1)); X="$TMPROOT/transition$ITER"; mkdir -p "$X"
  "$PY" "$PKG/source/advance_round92.py" --vendor "$DEP/vendor/round80" --state-in "$STATE" --source-in "$F/source.json.gz" --iteration "$ITER" --candidate "$I/outer/candidate.json" --direct "$I/direct/direct_verification.json" --state-out "$X/state.json" --record-out "$X/record.json" --source-out "$X/source.json.gz"
  cmp "$X/record.json" "$I/record.json"; cmp "$X/source.json.gz" "$PKG/formulas/iter$NEXT/source.json.gz"
  STATE="$X/state.json"
  printf 'CANDIDATE_REPLAY_PASS %s\n' "$ITER"
done
cmp "$STATE" "$PKG/continuation/final_state.json"

"$PY" "$PKG/source/check_continuation.py" --root "$PKG" --dependency "$DEP" --output "$TMPROOT/continuation.json"
cmp "$TMPROOT/continuation.json" "$PKG/verification/continuation_audit.json"
"$PY" "$PKG/source/check_result.py" --root "$PKG"
"$PY" "$PKG/source/check_process_ledger.py" --root "$PKG"
"$PY" "$PKG/source/check_actual_sat_trace_controls.py" --root "$PKG"

for NAME in full truncated corrupt; do
  set +e
  "$DEP/tooling/drat-trim-arm64-macos" "$PKG/iterations/iter127/direct/direct360/Zerr.cnf" "$PKG/controls/actual_sat_trace/$NAME.drat" >"$TMPROOT/$NAME.log" 2>"$TMPROOT/$NAME.stderr.log"
  CODE=$?
  set -e
  test "$CODE" -eq 1; grep 'NOT VERIFIED' "$TMPROOT/$NAME.log" >/dev/null
  # drat-trim prints the caller's formula path in its diagnostic.  Acceptance,
  # rejection, return code, and empty stderr are stable; the temporary path is not.
  test ! -s "$TMPROOT/$NAME.stderr.log"
done
printf '%s\n' ACTUAL_SAT_TRACE_PHYSICAL_CONTROLS_PASS

"$PY" "$DEP/source/check_proof_controls.py" --root "$DEP" --output "$TMPROOT/proof_controls.json"
"$PY" - "$TMPROOT/proof_controls.json" "$PKG/controls/proof_fixture_controls.json" <<'PY'
import json,sys
a=json.load(open(sys.argv[1]));b=json.load(open(sys.argv[2]));keys=['status','fixture_cnf_sha256','valid_drat_sha256','generated_lrat_sha256','valid_drat_accepted','generated_lrat_accepted','corrupt_drat_rejected','truncated_drat_rejected','corrupt_lrat_rejected','truncated_lrat_rejected','scope']
assert all(a[k]==b[k] for k in keys)
PY
test ! -e "$PKG/iterations/iter136"
printf '%s\n' ROUND92_PACKAGE_REPLAY_PASS
