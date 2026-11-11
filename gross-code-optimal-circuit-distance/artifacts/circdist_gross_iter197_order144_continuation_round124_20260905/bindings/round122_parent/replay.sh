#!/bin/sh
set -eu
if [ "$#" -ne 1 ]; then
  echo "usage: $0 ABSOLUTE_EXTERNAL_OUTPUT_DIRECTORY" >&2
  exit 64
fi
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec /usr/bin/python3 "$ROOT/source/replay_round122.py" --root "$ROOT" --output "$1"
