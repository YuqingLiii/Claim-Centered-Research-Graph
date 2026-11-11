#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if [ "$#" -lt 1 ]; then
  echo "usage: $0 OUTPUT_DIR [replay options]" >&2
  exit 2
fi
OUT=$1
shift
exec /usr/bin/python3 "$ROOT/source/replay_round126.py" --root "$ROOT" --output "$OUT" "$@"
