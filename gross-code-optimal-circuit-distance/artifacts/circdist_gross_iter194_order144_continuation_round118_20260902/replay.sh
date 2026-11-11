#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if [ "$#" -ne 1 ]; then
  echo "usage: $0 OUTPUT_DIRECTORY" >&2
  exit 64
fi
exec /usr/bin/python3 "$ROOT/source/replay_round118.py" --root "$ROOT" --output "$1"
