#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if [ "$#" -gt 2 ]; then echo "usage: $0 [REPOSITORY_ROOT] [EXTERNAL_OUTPUT_JSON]" >&2; exit 2; fi
REPO=${1:-$(CDPATH= cd -- "$ROOT/../../.." && pwd)}
OUTPUT=${2:-${TMPDIR:-/tmp}/circdist-round112-replay-$$.json}
exec /usr/bin/python3 "$ROOT/source/replay_round112.py" --package "$ROOT" --repo "$REPO" --output "$OUTPUT" --mode installed
