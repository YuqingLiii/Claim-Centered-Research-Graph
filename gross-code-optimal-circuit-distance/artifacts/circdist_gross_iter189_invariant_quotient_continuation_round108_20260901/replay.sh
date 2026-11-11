#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if [ "$#" -gt 1 ]; then
  echo "usage: $0 [EXTERNAL_OUTPUT_JSON]" >&2
  exit 2
fi
if [ "$#" -eq 1 ]; then
  OUTPUT=$1
else
  OUTPUT="${TMPDIR:-/tmp}/circdist-round108-replay-$$.json"
fi
exec /usr/bin/python3 "$ROOT/source/replay_round108.py" --root "$ROOT" --output "$OUTPUT"
