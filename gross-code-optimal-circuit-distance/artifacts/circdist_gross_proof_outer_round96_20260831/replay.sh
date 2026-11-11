#!/bin/sh
set -eu
PKG=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if [ -n "${ROUND96_REPOSITORY:-}" ]; then
  REPO=$ROUND96_REPOSITORY
else
  REPO=$(CDPATH= cd -- "$PKG/../../.." && pwd)
fi
if [ -n "${CIRCDIST_PYTHON:-}" ]; then
  PY=$CIRCDIST_PYTHON
elif [ -x /private/tmp/circdist-r72-dispatcher-venv/bin/python ]; then
  PY=/private/tmp/circdist-r72-dispatcher-venv/bin/python
else
  PY=python3
fi
"$PY" -c 'import z3,pysat; assert z3.get_version_string()=="5.1.0" and pysat.__version__=="1.9.dev15"; print("ROUND96_DEPENDENCIES_PASS",z3.get_version_string(),pysat.__version__)'
if [ -f "$PKG/SHA256SUMS.txt" ] || [ -f "$PKG/PAYLOAD_SHA256SUMS.txt" ]; then
  "$PY" "$PKG/source/check_manifests.py" --root "$PKG"
fi
args=""
if [ -n "${ROUND96_REPLAY_RECORD:-}" ]; then
  exec "$PY" "$PKG/source/replay_package.py" --root "$PKG" --python "$PY" --repository "$REPO" --record-output "$ROUND96_REPLAY_RECORD"
else
  exec "$PY" "$PKG/source/replay_package.py" --root "$PKG" --python "$PY" --repository "$REPO"
fi
