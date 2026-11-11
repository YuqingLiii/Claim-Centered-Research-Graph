#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PYTHON=${PYTHON:-python3}
RECORD=${1:-/private/tmp/circdist-round100-sealed-replay-record.json}
exec "$PYTHON" "$ROOT/source/replay_round100.py" --root "$ROOT" --python "$PYTHON" --record-output "$RECORD"
