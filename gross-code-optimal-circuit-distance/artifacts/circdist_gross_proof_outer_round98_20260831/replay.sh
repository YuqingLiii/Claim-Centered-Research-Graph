#!/bin/sh
set -eu
PKG=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
REPO=${ROUND98_REPOSITORY:-$(CDPATH= cd -- "$PKG/../../.." && pwd)}
PY=${CIRCDIST_PYTHON:-/private/tmp/circdist-r72-dispatcher-venv/bin/python}
"$PY" -c 'import z3,pysat;assert z3.get_version_string()=="5.1.0" and pysat.__version__=="1.9.dev15";print("ROUND98_DEPENDENCIES_PASS",z3.get_version_string(),pysat.__version__)'
"$PY" "$PKG/source/check_manifests.py" --root "$PKG"
if [ -n "${ROUND98_REPLAY_RECORD:-}" ]; then
  exec "$PY" "$PKG/source/replay_round98.py" --root "$PKG" --python "$PY" --repository "$REPO" --record-output "$ROUND98_REPLAY_RECORD"
else
  exec "$PY" "$PKG/source/replay_round98.py" --root "$PKG" --python "$PY" --repository "$REPO"
fi
