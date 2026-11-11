#!/usr/bin/env python3
"""Parse all Round122 scratch Python sources without importing or writing bytecode."""
import ast
import json
from pathlib import Path

root = Path("/private/tmp/circdist-round122-proposer")
paths = sorted(root.glob("*.py"))
for path in paths:
    ast.parse(path.read_text(), filename=str(path))
print(json.dumps({"status": "PASS", "files": len(paths), "solver_invocations": 0}, sort_keys=True))
