#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PY=${CIRCDIST_PYTHON:-python3}
TMP=$(mktemp -d "${TMPDIR:-/tmp}/circdist-r86-replay.XXXXXX")
trap 'find "$TMP" -depth -delete' EXIT HUP INT TERM
"$PY" - <<'PY'
import json, platform, sys
import pysat, z3
print(json.dumps({"python":sys.version,"platform":platform.platform(),"z3":z3.get_version_string(),"pysat":pysat.__version__},sort_keys=True))
PY
if [ -f "$ROOT/SHA256SUMS.txt" ]; then
  (cd "$ROOT" && shasum -a 256 -c SHA256SUMS.txt) > "$TMP/manifest_check.log"
  cat "$TMP/manifest_check.log"
fi
"$PY" "$ROOT/source/independent_state_replay.py" --root "$ROOT" --output "$TMP/state_replay.json"
cmp "$TMP/state_replay.json" "$ROOT/verification/expected_state_replay.json"
"$PY" "$ROOT/vendor/round80/src/replay_direct_candidate.py" --root "$ROOT/data/seed_iter102" --output "$TMP/seed_direct_replay.json"
cmp "$TMP/seed_direct_replay.json" "$ROOT/data/seed_iter102/direct_verification.json"
"$PY" "$ROOT/source/analyze_all_new_selector_domains.py" --package "$ROOT/vendor/round80" --state "$ROOT/continuation/final_state.json" --seed-direct "$ROOT/data/seed_iter102/direct_verification.json" --output "$TMP/domain_census.json"
cmp "$TMP/domain_census.json" "$ROOT/data/new_selector_domain_census.json"
"$PY" "$ROOT/source/rebuild_final_formula.py" --root "$ROOT" --compiler-smt2 "$ROOT/formulas/final_outer.smt2" --output-smt2 "$TMP/rebuilt_final_outer.smt2" --output-summary "$TMP/formula_rebuild.json"
cmp "$TMP/rebuilt_final_outer.smt2" "$ROOT/formulas/independent_rebuilt_final_outer.smt2"
cmp "$TMP/formula_rebuild.json" "$ROOT/verification/expected_formula_rebuild.json"
printf '%s\n' 'ROUND86_PACKAGE_REPLAY_PASS'
