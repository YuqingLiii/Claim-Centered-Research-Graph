#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if [ "$#" -gt 1 ]; then
  echo "usage: $0 [output-directory]" >&2
  exit 2
fi
if [ "$#" -eq 1 ]; then
  OUT=$1
else
  OUT=$(mktemp -d "${TMPDIR:-/private/tmp}/circdist-round116-replay.XXXXXX")
fi
exec /usr/bin/python3 "$ROOT/source/replay_round116.py" --root "$ROOT" --output "$OUT"
