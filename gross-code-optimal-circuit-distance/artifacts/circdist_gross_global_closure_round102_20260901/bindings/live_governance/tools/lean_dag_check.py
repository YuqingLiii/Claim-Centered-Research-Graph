#!/usr/bin/env python
"""Lean <-> proof-DAG anti-drift checker (DAG_PROTOCOL.md §7, pre-v6 §7.6).

Section numbering note: this file was written against the PRE-v6 protocol, whose
formalization section was §7.6.  Schema v6 (`research/DAG_PROTOCOL.md`) has eight
top-level sections and no subsections; the formalization contract is plain §7.
`§7.6` below is kept as the historical name of the check list.

Implements the seven checks §7.6 specifies, at the severities assigned by the WHGAP M7
commission (`channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_M7_20260730.md`,
origin finding R11 m7: none of §7.6's checks was implemented anywhere, so a `lean.state:
"composition-checked"` recorded on a module that contains NO composition theorem went
uncaught until a human-grade review found it).

    1  [FAIL] existence          declared module/file/Claim/composition theorems exist
    2  [FAIL] bijection          node-shaped .lean files  <->  nodes carrying a `lean:` block
    3  [FAIL] hash triple        recomputed == node `claim_hash` == docstring digest
    3b [WARN] verbatim body      docstring frozen text == canonical node claim (extra;
                                 closes the "edited claim, intact hash line" hole)
    4  [WARN] AND coverage       composition theorem text mentions every child's Claim
                                 (TEXTUAL APPROXIMATION -- a real check needs elaboration)
    5  [FAIL] OR route match     `composition_via_*` suffixes == the ENABLED alternatives
                                 (AND-style accepted; a §4-disabled route is not required, and
                                 an unrendered enabled route must be DECLARED -- see below)
    6  [FAIL] import graph       node-module imports == `children`, up to deviations DECLARED
                                 one-by-one in `formalization.lean.rel` (see below)
    rel[FAIL] declaration hygiene  a `lean.rel` deviation declaration must name one real subject
                                 and a substantive mechanism, and must not be contradicted by
                                 the module or the graph
    7a [FAIL] state vs content   every §7.1 token asserted in `state` is backed by content
    7b [FAIL] rel display        composition-checked/proved require a `rel` key
       [WARN]                    ... empty `rel` with undeterminable extra hypotheses
    7c [WARN] status arithmetic  header status <= min(composition status, child statuses),
                                 unless the composition `rel` documents a scoped-input
                                 exception (the rel text is printed when invoked)

This tool is READ-ONLY: it never writes to any tree.

Usage (from the repository root):

    python tools/lean_dag_check.py --problem werner-holevo-gap
    python tools/lean_dag_check.py --problem se
    python tools/lean_dag_check.py --selftest
    python tools/lean_dag_check.py --problem werner-holevo-gap --nodes-dir <dir>   # patched copy

Exit code 0 iff no FAIL was emitted (WARNs never fail the run).

TWO RECORD SCHEMAS (2026-08-17, review item F6 of
`artifacts/se_lean_t2_review_20260817.md`)
---------------------------------------------------------------------------
The checker originally read only PRE-v6 `<node>.md` records through
`proof_dag_check.parse_front_matter`.  `se` and `ksum` now store schema-v6 YAML
(`research/DAG_PROTOCOL.md`), on which that parser raises
`ValueError: invalid front matter line: '- COR'`.  `channel-capacity/werner-holevo-gap`
is still on the legacy layout that `research/FILE_PROTOCOL.md` §1 explicitly keeps
valid, so the loader DISPATCHES on the record format actually found in the nodes
directory (`*.yaml` -> v6, otherwise `*.md` -> legacy) instead of replacing one
schema with the other.  The v6 side reuses `tools/proof_dag_v6.py` -- its
`load_problem` and its `claim_hash` -- rather than adding a second YAML parser.

All seven checks and their severities are unchanged.  The v6 adapter (`V6Node`)
maps the fields the checks were written against onto v6 as follows:

    pre-v6 field            schema-v6 source
    ----------------------  ------------------------------------------------
    status                  assessment.level
    kind                    DERIVED (§2: routes are alternatives, premises are
                            jointly required) -- 0 live routes -> leaf,
                            1 -> AND, >1 -> OR
    children                ordered union of the live routes' premises
    lean:                   formalization.lean
    lean.composition        formalization.lean.theorems  (renamed in v6)
    claim (for the hash)    claim, hashed by proof_dag_v6.claim_hash
    composition.status/rel  per-route assessment.level / node assessment.caveats

Two things the v6 schema no longer carries, so they are REPORTED rather than
silently dropped (see also `artifacts/se_lean_dagcheck_v6_20260817.md`):

  * §7.4 SILENCE (the extra `0` check, not one of the seven).  Pre-v6 nodes wrote
    `lean: none` plus a reason; v6 omits `formalization` entirely for a node with
    no formal mirror (`DAG_PROTOCOL.md` §1 "optional blocks are omitted", §7
    "present only when a real module, file, and claim declaration exist").  There
    is no reason field to test, so on v6 records the check emits ONE INFO stating
    that, plus the count of unmechanized nodes, instead of a per-node WARN.
  * The pre-v6 auto-justification of an unrendered OR route (a route whose child
    carried `lean: none` WITH a reason) has no v6 field either.  Check 5 was
    therefore first applied with NO exemption; since 2026-08-17 the replacement is
    an EXPLICIT per-route declaration on the node (see "EXPLICIT DEVIATION
    DECLARATIONS" below), which is stricter than the pre-v6 inference because it
    must be written, must name a reason, and must not be contradicted by the module.

EXPLICIT DEVIATION DECLARATIONS (2026-08-17, frontier task-006 of `SE.formal.t2`)
---------------------------------------------------------------------------
Checks 5 and 6 compared the Lean module against the child/route lists alone, so a
premise that legitimately arrives as an `Interface.Cited` field or as a declared
relative hypothesis (DAG_PROTOCOL §1), and a route with no formal rendering at
all, produced FAILs that no honest bookkeeping could clear -- which is a standing
invitation to fabricate a stub theorem.  The repair keeps the comparison and adds
a REQUIREMENT: each deviation must be declared, one entry per subject, in
`formalization.lean.rel`.  Declared -> INFO; undeclared -> FAIL, unchanged.  The
grammar and the six anti-rubber-stamp rules are documented at `REL_DECL_RE`.

WHAT THIS CHECKER DOES NOT DECIDE (2026-08-17, frontier task-011 of `SE.formal.t2`,
answering F2/F5/F6 of `artifacts/se_task006_review_20260817.md`)
---------------------------------------------------------------------------
The 2026-08-17 independent review broke the declaration channel with six deliberate
probes.  Three of them (F1 junk mechanism, F3 import across a MECHANIZED
intermediate, F4 un-imported MECHANIZED premise) were mechanically fixable and now
FAIL; see `MIN_MECHANISM_WORDS`, `MECHANISM_TOKEN_RE` and check 6.  The other three
are NOT mechanically decidable by this tool, so they are named here instead of
being left for a future session to rediscover as a trick:

  * F2 RELEVANCE IS NEVER CHECKED.  For a `Cited.<field>` named in a declaration
    this tool checks existence, never RELEVANCE: swapping a real-but-wrong field
    into a real declaration (`Cited.numerator` -> `Cited.maskNorm_pos` on
    `SE.br.num`) passes, because deciding whether an English mechanism is TRUE
    needs a reader.  Judging the truth of every declaration is therefore a
    STANDING REVIEW OBLIGATION under DAG_PROTOCOL §6.2/§6.4, not a gate this tool
    can hold.  The tool now says so at the point of use: one INFO per run naming
    the residual risk and the number of declarations it covers.  (The obligation
    was discharged for all 26 SE declarations by
    `artifacts/se_task006_review_20260817.md` §V3; a NEW declaration is UNREVIEWED
    until some later review says otherwise.)

  * F5 A `REFUTED` WRITE LEGITIMATELY SILENCES CHECK 5.  DAG_PROTOCOL §4 disables
    every route whose implication is REFUTED or which requires a REFUTED premise,
    and a disabled route is not an alternative anyone can be asked to mirror.  So
    writing `REFUTED` on a premise removes its route from check 5's REQUIRED set
    and no `route-not-formalized` declaration is needed either.  That is correct,
    it is the same predicate check 7c already applies, and the exclusion is
    printed as INFO rather than hidden.  It is also, stated plainly, a laundering
    path: a dishonest `REFUTED` would silence a rendering obligation.  It is
    policed elsewhere and deliberately not here -- `tools/check_event_append_only.py`
    rejects an unlogged level change and `tools/proof_dag_check.py` requires the
    §4 reason and DEAD/PARKED disposition -- so do not "fix" it by weakening the
    §4 exemption.

  * F6 `sync_state: current` IS ABOUT TEXT AND DIGESTS, NOT ABOUT MEANING.  It
    means: the module quotes the CURRENT claim text verbatim and the three digests
    agree (checks 3/3b).  It does NOT mean the Lean `Claim : Prop` expresses the
    node claim -- a module may quote its claim perfectly and still render a
    deliberately weaker SHADOW of it (in SE: `gram.interface`, `omega.interface`,
    `sect` and `tame` all do, each declared in its own module header and in its
    node's caveats).  DAG_PROTOCOL §7's phrase "until the formal statement,
    imports, proof, and hash are synchronized" invites the stronger reading; this
    tool cannot check it, because comparing a `Prop` with English prose is a
    review act.  The tool restates this wherever it reports the value.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

from proof_dag_check import normalize_grouped, parse_front_matter, parse_node
from proof_dag_v6 import _load_yaml as v6_load_yaml
from proof_dag_v6 import claim_hash as v6_claim_hash
from proof_dag_v6 import load_problem as v6_load_problem

REPO = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------------
# problem registry.  `schema="auto"` detects the record format in the nodes
# directory: any `*.yaml` -> schema v6, otherwise the legacy `*.md` front matter.
# ---------------------------------------------------------------------------


class ProblemSpec:
    def __init__(self, nodes_dir, lean_dir, module_prefix,
                 non_node_modules=("Interface", "Trust", "SelfTest", "Model"),
                 non_node_prefixes=("Support",), enabled=True, schema="auto"):
        self.nodes_dir = nodes_dir            # repo-relative or absolute Path/str
        self.lean_dir = lean_dir              # directory holding the node-shaped modules
        self.module_prefix = module_prefix
        self.non_node_modules = set(non_node_modules)
        self.non_node_prefixes = tuple(non_node_prefixes)
        self.enabled = enabled
        self.schema = schema                  # "auto" | "v6" | "legacy-md"


REGISTRY = {
    "werner-holevo-gap": ProblemSpec(
        nodes_dir="channel-capacity/werner-holevo-gap/proof-dag/nodes",
        lean_dir="channel-capacity/werner-holevo-gap/proof-dag/lean/WHGAP",
        module_prefix="WHGAP",
        enabled=True,
    ),
    # Enabled 2026-08-17 together with the schema-v6 loader (review item F6 of
    # artifacts/se_lean_t2_review_20260817.md: `enabled=False` gave exit 2 and
    # flipping it crashed in the pre-v6 front-matter parser).
    "se": ProblemSpec(
        nodes_dir="research/se/proof-dag/nodes",
        lean_dir="research/se/proof-dag/lean/SE",
        module_prefix="SE",
        enabled=True,
    ),
    # k-Sum is part of the canonical release gate.  Keeping it disabled allowed
    # stale claim quotations and module metadata to survive a green SE-only run.
    "ksum": ProblemSpec(
        nodes_dir="research/ksum/proof-dag/nodes",
        lean_dir="research/ksum/proof-dag/lean/KSUM",
        module_prefix="KSUM",
        enabled=True,
    ),
}

LADDER = {"REFUTED": -1, "OPEN": 0, "CONJECTURED": 1, "NUMERICAL": 2,
          "CERTIFIED*": 3, "PROVED": 4}
STATE_VOCAB = {"none", "stated", "composition-checked", "proved", "refuted"}

IDENT = r"[A-Za-z_][A-Za-z0-9_'!?]*"
DECL_START = re.compile(
    r"^(?:/--|/-!|@\[|theorem |lemma |def |abbrev |noncomputable |structure |"
    r"instance |end |namespace |section |open |variable )")


# ---------------------------------------------------------------------------
# diagnostics
# ---------------------------------------------------------------------------

class Report:
    def __init__(self):
        self.items = []          # (severity, check, subject, message)
        self.stats = {}          # check id -> number of (node, check) evaluations

    def count(self, check, n=1):
        self.stats[check] = self.stats.get(check, 0) + n

    def add(self, severity, check, subject, message):
        self.items.append((severity, check, subject, message))

    def fail(self, check, subject, message):
        self.add("FAIL", check, subject, message)

    def warn(self, check, subject, message):
        self.add("WARN", check, subject, message)

    def info(self, check, subject, message):
        self.add("INFO", check, subject, message)

    @property
    def n_fail(self):
        return sum(1 for s, *_ in self.items if s == "FAIL")

    @property
    def n_warn(self):
        return sum(1 for s, *_ in self.items if s == "WARN")

    def fails_for(self, check):
        return [i for i in self.items if i[0] == "FAIL" and i[1] == check]

    def render(self):
        out = []
        for sev, check, subject, msg in self.items:
            out.append("%-4s [%s] %s: %s" % (sev, check, subject, msg))
        out.append("")
        if self.stats:
            out.append("coverage (evaluations actually performed):")
            for k in sorted(self.stats):
                out.append("  %-12s : %d" % (k, self.stats[k]))
            out.append("")
        out.append("summary: %d FAIL, %d WARN, %d INFO"
                   % (self.n_fail, self.n_warn,
                      sum(1 for s, *_ in self.items if s == "INFO")))
        return "\n".join(out)


# ---------------------------------------------------------------------------
# small YAML-ish parsing (no external dependency)
# ---------------------------------------------------------------------------

def strip_comment(value: str) -> str:
    """Drop a trailing `# ...` comment that is outside quotes."""
    out, in_q = [], False
    for ch in value:
        if ch == '"':
            in_q = not in_q
        if ch == "#" and not in_q:
            break
        out.append(ch)
    return "".join(out).strip()


def parse_scalar(value: str):
    value = value.strip()
    if value.startswith('"') or value.startswith("'"):
        q = value[0]
        end = value.find(q, 1)
        return value[1:end] if end > 0 else value[1:]
    value = strip_comment(value)
    if value.startswith("["):
        depth, end = 0, None
        for i, ch in enumerate(value):
            if ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0:
                    end = i
                    break
        raw = value[:end + 1] if end is not None else value
        try:
            return json.loads(raw)
        except Exception:
            return [p.strip().strip('"') for p in raw.strip("[]").split(",") if p.strip()]
    if value in ("null", "~", ""):
        return None
    return value


def parse_block_mapping(lines, indent):
    """Parse `key: value` pairs at the given indent from `lines` (a list of raw lines).

    Handles inline scalars/lists, `null # comment`, and multi-line `- ` item lists.
    """
    out = {}
    i = 0
    pad = " " * indent
    while i < len(lines):
        line = lines[i].rstrip("\n")
        if not line.strip() or line.strip().startswith("#"):
            i += 1
            continue
        cur_indent = len(line) - len(line.lstrip(" "))
        if cur_indent != indent or not line.startswith(pad):
            i += 1
            continue
        m = re.match(r"^%s([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$" % re.escape(pad), line)
        if not m:
            i += 1
            continue
        key, rest = m.group(1), m.group(2)
        if rest.strip() in (">", "|", ">-", "|-", ""):
            # folded / literal / nested block: gather the deeper-indented body
            body = []
            j = i + 1
            while j < len(lines):
                nxt = lines[j].rstrip("\n")
                if nxt.strip() and (len(nxt) - len(nxt.lstrip(" "))) <= indent:
                    break
                body.append(nxt.strip())
                j += 1
            if body and body[0].startswith("- "):
                out[key] = [b[2:].strip().strip('"') for b in body if b.startswith("- ")] \
                    if all(b.startswith("- ") or not b for b in body) else \
                    _fold_items(body)
            else:
                out[key] = " ".join(b for b in body if b)
            i = j
            continue
        out[key] = parse_scalar(rest)
        i += 1
    return out


def _fold_items(body):
    """Fold a `- "..."` list whose entries wrap over several lines."""
    items, cur = [], None
    for b in body:
        if b.startswith("- "):
            if cur is not None:
                items.append(cur)
            cur = b[2:].strip()
        elif cur is not None and b:
            cur += " " + b
    if cur is not None:
        items.append(cur)
    return [i.strip().strip('"') for i in items]


# ---------------------------------------------------------------------------
# node files
# ---------------------------------------------------------------------------

class Node:
    schema = "legacy-md"

    def __init__(self, path: Path):
        self.path = path
        self.raw = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        self.front, self.body = parse_node(path)
        self.id = self.front.get("id") or path.stem
        self.kind = (self.front.get("kind") or "").strip()
        self.status = normalize_status(self.front.get("status") or "")
        self.children = as_list(self.front.get("children"))
        self.lean = self.front.get("lean") if isinstance(self.front.get("lean"), dict) else None
        self.lean_none_reason = self.front.get("lean_reason")
        self.has_lean_section = False
        self._parse_lean_section()
        self.composition = self._parse_composition_block()

    def _front_matter(self):
        m = re.match(r"^---\n(.*?)\n---\n", self.raw, re.S)
        if not m:
            return {}
        raw = parse_front_matter(m.group(1))
        return normalize_grouped(raw) if "identity" in raw else raw

    def section(self, heading):
        m = re.search(r"^## %s\n(.*?)(?=^## |\Z)" % re.escape(heading),
                      self.body, re.S | re.M)
        return m.group(1) if m else None

    def claim_text(self):
        """EXACTLY the normalization of tools/whgap_lean_freeze_claims.py."""
        if isinstance(self.front.get("claim"), str):
            return self.front["claim"].strip("\n")
        m = re.search(r"^## Claim\n(.*?)(?=^## )", self.body, re.S | re.M)
        if m is None:
            return None
        return m.group(1).strip("\n")

    def claim_hash(self):
        text = self.claim_text()
        if text is None:
            return None
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    def _parse_lean_section(self):
        if self.lean is not None:
            return
        body = self.section("Lean")
        if body is None:
            return
        self.has_lean_section = True
        fence = re.search(r"```ya?ml\n(.*?)```", body, re.S)
        if fence:
            inner = fence.group(1).split("\n")
            top = parse_block_mapping(inner, 0)
            if "lean" in top and isinstance(top["lean"], (str, type(None))) \
                    and str(top.get("lean")).strip() in ("", "None"):
                pass
            self.lean = parse_block_mapping(inner, 2)
            return
        m = re.search(r"lean:\s*`?none`?", body)
        if m:
            reason = body[m.end():].strip(" \n`—-:.")
            self.lean_none_reason = reason
            return
        m = re.search(r"`lean:\s*none`", body)
        if m:
            self.lean_none_reason = body[m.end():].strip(" \n`—-:.")

    def _parse_composition_block(self):
        if self.front.get("__schema__") == "structured-v5":
            return self.front.get("composition")
        body = self.section("Composition proof")
        if body is None:
            return None
        fence = re.search(r"```ya?ml\n(.*?)```", body, re.S)
        if not fence:
            return None
        inner = fence.group(1).split("\n")
        if re.search(r"^composition:\s*none", fence.group(1), re.M):
            return {"__none__": True}
        return parse_block_mapping(inner, 2)


class V6Node:
    """Schema-v6 node record behind the attribute surface the seven checks use.

    See the module docstring for the field-by-field mapping.  Nothing is
    invented: every attribute is either a v6 field, a view derived by the rules
    of `DAG_PROTOCOL.md` §2, or `None`/empty when v6 carries no such field.
    """

    schema = "v6"

    def __init__(self, path: Path, data: dict):
        self.path = Path(path)
        self.data = data
        self.raw = self.path.read_text(encoding="utf-8").replace("\r\n", "\n")
        self.front = data
        self.body = ""
        self.id = data.get("id") or self.path.stem
        assessment = data.get("assessment") or {}
        self.status = normalize_status(assessment.get("level") or "")
        self.caveats = [str(c) for c in (assessment.get("caveats") or [])]
        self.frontier = data.get("frontier") or {}

        self.routes = data.get("routes") or {}
        self.live_routes = {rid: r for rid, r in self.routes.items()
                            if isinstance(r, dict) and not r.get("retired")}
        # §2: the routes of one node are ALTERNATIVES (OR); the premises inside a
        # route are JOINTLY required (AND).  A node with no route is a leaf.
        if not self.live_routes:
            self.kind = ""
        elif len(self.live_routes) > 1:
            self.kind = "OR"
        else:
            self.kind = "AND"

        seen, kids = set(), []
        for route in self.live_routes.values():
            for premise in route.get("premises") or []:
                premise = str(premise)
                if premise not in seen:
                    seen.add(premise)
                    kids.append(premise)
        self.children = kids

        lean = (data.get("formalization") or {}).get("lean")
        if isinstance(lean, dict):
            lean = dict(lean)
            # v6 renamed the pre-v6 `composition:` key to `theorems:`.
            if "composition" not in lean:
                lean["composition"] = lean.get("theorems")
            self.lean = lean
        else:
            self.lean = None
        # v6 records the absence of a formal mirror by OMITTING `formalization`;
        # there is no `lean: none` marker and no reason field (see docstring).
        self.has_lean_section = self.lean is not None
        self.lean_none_reason = None
        # v6 stores no single per-node composition block: a route owns its own
        # assessment.  Check 7c uses `live_routes` instead.
        self.composition = None

    def section(self, heading):
        return None

    def claim_text(self):
        claim = self.data.get("claim")
        return claim if isinstance(claim, str) else None

    def claim_hash(self):
        """The v6 claim digest, computed by proof_dag_v6.claim_hash (authoritative)."""
        claim = self.claim_text()
        if claim is None:
            return None
        return v6_claim_hash(claim).split(":")[-1]


def detect_schema(nodes_dir: Path) -> str:
    if any(nodes_dir.glob("*.yaml")):
        return "v6"
    return "legacy-md"


def load_nodes(spec: ProblemSpec, nodes_dir: Path, rep: "Report"):
    """Load node records with the loader the directory's schema requires."""
    schema = spec.schema if spec.schema in ("v6", "legacy-md") else detect_schema(nodes_dir)
    nodes = {}
    if schema == "v6":
        strays = sorted(p.name for p in nodes_dir.glob("*.md"))
        if strays:
            rep.warn("0", nodes_dir.name,
                     "schema-v6 nodes directory also contains pre-v6 `*.md` files, "
                     "which were NOT loaded: %s" % strays)
        for path, data in load_v6_records(nodes_dir):
            node = V6Node(path, data)
            nodes[node.id] = node
    else:
        for path in sorted(nodes_dir.glob("*.md")) + sorted(nodes_dir.glob("*.yaml")):
            node = Node(path)
            nodes[node.id] = node
    return schema, nodes


def load_v6_records(nodes_dir: Path):
    """(path, mapping) pairs, via proof_dag_v6.load_problem when the tree is whole."""
    problem_root = nodes_dir.parent.parent
    if (nodes_dir.parent / "PROJECT.yaml").is_file() \
            and (problem_root / "proof-dag" / "nodes").resolve() == nodes_dir.resolve():
        loaded = v6_load_problem(problem_root)
        return [(loaded.paths[nid], data) for nid, data in sorted(loaded.nodes.items())]
    out = []
    for path in sorted(nodes_dir.glob("*.yaml")):
        data = v6_load_yaml(path)
        if not isinstance(data, dict):
            raise ValueError("%s: node must be a mapping" % path)
        out.append((path, data))
    return out


def as_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v).strip().strip('"') for v in value]
    value = str(value).strip()
    if value.startswith("["):
        parsed = parse_scalar(value)
        return as_list(parsed)
    return [value] if value else []


def normalize_status(s):
    s = str(s).replace("\\", "").strip().strip('"')
    return s


# ---------------------------------------------------------------------------
# Lean module helpers
# ---------------------------------------------------------------------------

def denorm(module: str) -> str:
    """Strip Lean guillemet identifiers: WHGAP.«no-ascent-hierarchy» -> WHGAP.no-ascent-hierarchy."""
    return module.replace("«", "").replace("»", "").strip().strip('"')


def module_of_file(lean_dir: Path, path: Path, prefix: str) -> str:
    rel = path.relative_to(lean_dir).with_suffix("")
    return ".".join([prefix] + list(rel.parts))


def module_of_declared_file(root: Path, path: Path) -> str | None:
    """Return the Lean module implied by a repository path.

    Node modules normally live below ``proof-dag/lean/<Namespace>``.  Some
    audited support modules live in a sibling namespace (for example
    ``proof-dag/lean/KsumAudit``), so deriving every module relative to the
    node-shaped ``KSUM`` directory incorrectly rejected valid declarations.
    """
    try:
        rel = path.resolve().relative_to(root.resolve()).with_suffix("")
    except ValueError:
        return None
    parts = list(rel.parts)
    try:
        lean_index = max(i for i, part in enumerate(parts) if part == "lean")
    except ValueError:
        return None
    module_parts = parts[lean_index + 1:]
    return ".".join(module_parts) if module_parts else None


def is_explicit_nonformalization_file(path: Path) -> bool:
    """Recognize a documentation-only ``.lean`` placeholder.

    Such a file is not a Lean module and therefore is not part of the
    node/module bijection.  The marker is explicit so arbitrary stray files do
    not become invisible to the checker.
    """
    try:
        head = path.read_text(encoding="utf-8")[:4096]
    except OSError:
        return False
    return bool(re.search(r"(?im)^\s*(?:--\s*)?lean\s*:\s*none\b", head))


def is_non_node_module(spec: ProblemSpec, lean_dir: Path, path: Path) -> bool:
    rel = path.relative_to(lean_dir).with_suffix("")
    parts = list(rel.parts)
    if parts[0] in spec.non_node_prefixes:
        return True
    return parts[-1] in spec.non_node_modules and len(parts) == 1


def docstring_of(src: str) -> str:
    """The module header comment.

    WHGAP node modules open with a `/-! ... -/` module docstring; the SE and KSUM
    node modules open with a plain `/- ... -/` block comment carrying the same
    node-id / claim_hash / FROZEN CLAIM header.  Both are accepted: the LEADING
    comment wins (a bare `re.search` for `/-!` would otherwise skip past a `/-`
    header and return some later section docstring), with the old search as the
    fallback for a module whose header does not start the file.  This widens WHERE
    the digest is looked for; it changes no comparison and no severity.
    """
    m = re.match(r"\s*/-!?(.*?)-/", src, re.S)
    if m:
        return m.group(1)
    m = re.search(r"/-!(.*?)-/", src, re.S)
    return m.group(1) if m else ""


def has_decl(src: str, kind_re: str, name: str) -> bool:
    pat = r"^[ \t]*(?:private\s+|protected\s+|noncomputable\s+)*(?:%s)\s+«?%s»?\b" % (
        kind_re, re.escape(name))
    return re.search(pat, src, re.M) is not None


def decl_text(src: str, name: str) -> str:
    pat = r"^[ \t]*(?:private\s+|protected\s+)*(?:theorem|lemma)\s+«?%s»?\b" % re.escape(name)
    m = re.search(pat, src, re.M)
    if not m:
        return ""
    lines = src[m.start():].split("\n")
    out = [lines[0]]
    for line in lines[1:]:
        if DECL_START.match(line):
            break
        out.append(line)
    return "\n".join(out)


def imports_of(src: str):
    return re.findall(r"^import\s+(\S+)", src, re.M)


def dedent_block(text: str) -> str:
    """Strip a uniform left indent, so a claim quoted INSIDE a comment can be compared."""
    lines = [ln for ln in text.strip("\n").split("\n")]
    pads = [len(ln) - len(ln.lstrip(" ")) for ln in lines if ln.strip()]
    pad = min(pads) if pads else 0
    return "\n".join(ln[pad:] if ln.strip() else "" for ln in lines).strip()


def drift_note(node, hexes) -> str:
    """Name the v6 fields that explain a digest mismatch. DIAGNOSIS ONLY.

    Severity is unaffected: check 3 still FAILs.  A schema-v6 `lean:` block can
    carry `source_claim_hash` (the digest of the claim text the module actually
    quotes) and `sync_state`.  When the docstring digest is that recorded source
    hash and the node declares `sync_state: stale`, the mismatch is the OPEN
    DAG_PROTOCOL §7 synchronization gate rather than an unrecorded edit -- worth
    saying in the message, not worth silencing.

    Review item F6 (2026-08-17): `sync_state` is a statement about TEXT AND
    DIGESTS only.  `current` says the module quotes the current claim and the
    digests agree; it says NOTHING about whether the Lean `Claim : Prop` expresses
    the node claim, which no digest can witness.  The message spells that out
    rather than letting DAG_PROTOCOL §7's "the formal statement, imports, proof,
    and hash are synchronized" be read as the stronger guarantee.
    """
    lean = node.lean or {}
    source = str(lean.get("source_claim_hash") or "").split(":")[-1].strip().lower()
    sync = str(lean.get("sync_state") or "").strip()
    bits = []
    if source and source in hexes:
        bits.append("docstring digest == the node's recorded `source_claim_hash`")
    if sync:
        bits.append("node declares `sync_state: %s` (a claim about the QUOTED TEXT and the "
                    "DIGESTS only -- never about whether the Lean `Claim : Prop` expresses "
                    "the node claim)" % sync)
    if not bits:
        return ""
    return " [%s -- §7 requires the formal statement, imports, proof and hash to be " \
           "synchronized, so this FAIL is that open gate]" % "; ".join(bits)


# ---------------------------------------------------------------------------
# EXPLICIT DEVIATION DECLARATIONS in `formalization.lean.rel`
# (added 2026-08-17, frontier task-006 of `SE.formal.t2`)
#
# DAG_PROTOCOL §1 licenses a composition premise to arrive as "a child, a cited
# external interface, or an explicit relative hypothesis", and §7 requires the
# formal mirror to be auditable from the node.  Checks 5 and 6 were written
# against the child/route lists ALONE, so a premise that legitimately arrives as
# an `Interface.Cited` field, or a route that has no formal rendering at all,
# produced a FAIL that no amount of honest bookkeeping could clear.
#
# The repair is NOT to relax the comparison.  It is to require the deviation to
# be WRITTEN DOWN, one entry per deviating premise/import/route, in the node's
# `formalization.lean.rel` list (an existing schema-v6 field -- see
# `tools/proof_dag_v6.py` LEAN_KEYS; no new key is introduced).  A DECLARED
# deviation is INFO; an UNDECLARED one is still FAIL.  Recognized entry forms:
#
#     premise-not-imported: <child-node-id>   - <mechanism the premise arrives by>
#     import-not-child:     <imported-module> - <why this non-child is imported>
#     route-not-formalized: <route-id>        - <why no composition_via_* exists>
#
# and the tool enforces, so that a declaration cannot become a rubber stamp:
#
#   * one subject per entry -- no lists, no wildcards, no blanket declaration;
#   * a SUBSTANTIVE mechanism, which since 2026-08-17 (review item F1) is three
#     independent conditions, not one: at least MIN_MECHANISM_CHARS non-space
#     characters, at least MIN_MECHANISM_WORDS whitespace-separated words, and at
#     least one MECHANISM_TOKEN_RE anchor -- a backticked identifier, a dotted node
#     id, or a ruling/deviation reference.  The length gate alone was a pure
#     character count: 26 literal `q` characters cleared it;
#   * the subject must REALLY deviate: a `premise-not-imported` for a premise the
#     module does import, an `import-not-child` for an actual child, or a
#     `route-not-formalized` for a route that HAS a `composition_via_*` theorem is
#     a FALSE record and FAILs;
#   * a subject that is not a child / not an import / not a route of this node FAILs;
#   * an `import-not-child` module must be a DAG DESCENDANT of the declaring node
#     (a skipped intermediate node is licensed; an import from outside the subtree
#     is exactly the undeclared dependency check 6 exists to catch);
#   * every `Cited.<field>` named in a mechanism must actually exist in the
#     problem's `Interface.lean`;
#   * an `import-not-child` module must additionally be reachable ONLY across
#     UNMECHANIZED intermediates (2026-08-17, review item F3): every node lying on
#     a premise path from the declaring node down to the imported one must LACK a
#     `formalization` block.  That is the property the real declarations already
#     assert in prose ("neither of which carries a formalization block, so no
#     module for them exists to import").  If an intermediate IS mechanized, a
#     module for it demonstrably exists and the import must go through it;
#   * a `premise-not-imported` premise must LACK a `formalization` block
#     (2026-08-17, review item F4).  The licensed arrivals of DAG_PROTOCOL §1 --
#     a cited interface field, an explicit relative hypothesis -- are the ways a
#     premise with NO module reaches the composition.  When the premise HAS a
#     module, "it could not be imported" is false on its face.
#
# What the tool does NOT do, stated plainly: it cannot decide whether an English
# mechanism description is TRUE.  It enforces that each deviation is individually
# named, substantively explained, really present, and consistent with the module
# and the graph.  Judging the truth of the mechanism remains a review obligation
# (DAG_PROTOCOL §6.2/§6.4) -- see "WHAT THIS CHECKER DOES NOT DECIDE" (F2) in the
# module docstring, and the INFO this tool prints once per run that carries any
# declaration.
# ---------------------------------------------------------------------------

DECL_KINDS = ("premise-not-imported", "import-not-child", "route-not-formalized")
REL_DECL_RE = re.compile(
    r"^\s*(%s)\s*:\s*([A-Za-z0-9_.«»'*-]+)\s*(?:[—–:-]+\s*)?(.*)$"
    % "|".join(DECL_KINDS), re.S | re.I)
MIN_MECHANISM_CHARS = 24
MIN_MECHANISM_WORDS = 4
# An anchor into something CHECKABLE: a backticked identifier (`Cited.numerator`,
# `tame.Claim`), a dotted node/module id (`SE.denom.Phi.legal.trace`), or a named
# coordinator ruling / declared deviation (`ruling R4`, `deviation D3`).  Prose
# alone -- and a wall of one repeated character -- carries none of these.
MECHANISM_TOKEN_RE = re.compile(
    r"`[^`\n]+`"                                    # backticked identifier
    r"|\b[A-Z][A-Za-z0-9]*(?:\.[A-Za-z0-9_-]+)+\b"  # dotted node / module id
    r"|\b(?:ruling|deviation)\s+[A-Z]\d+\b",        # ruling / deviation reference
    re.I)
# Printed once per run that parsed at least one declaration (review item F2).
RELEVANCE_NOTICE = (
    "this tool checks that a declared `Cited.<field>` EXISTS, never that it is "
    "RELEVANT: a plausible but FALSE mechanism naming a real field passes. "
    "Judging the truth of a declared mechanism is a STANDING REVIEW OBLIGATION "
    "(DAG_PROTOCOL §6.2/§6.4), discharged for the 26 SE declarations by "
    "artifacts/se_task006_review_20260817.md §V3 and UNDISCHARGED for any "
    "declaration added since. %d declaration(s) parsed in this run.")
# Printed once per run in which any node declares `sync_state` (review item F6).
SYNC_STATE_NOTICE = (
    "`sync_state: current` asserts ONLY that the module quotes the current claim "
    "text and that the digests agree (checks 3/3b). It does NOT assert that the "
    "Lean `Claim : Prop` expresses the node claim: a module may quote its claim "
    "perfectly and still render a deliberately weaker SHADOW of it. That "
    "correspondence is a review act this tool cannot perform; read each module "
    "header and the node's own caveats. current=%d, stale=%d.")


def rel_entries(node):
    rel = (node.lean or {}).get("rel")
    if isinstance(rel, list):
        return [str(r) for r in rel]
    if rel in (None, ""):
        return []
    return [str(rel)]


def parse_rel_declarations(node, nid, rep):
    """`{kind: {subject: mechanism}}` from `lean.rel`; hygiene failures under `rel`.

    A `rel` entry that does not begin with a recognized key is ordinary prose and
    is ignored here (it is still read by check 7b as before).
    """
    out = {kind: {} for kind in DECL_KINDS}
    for entry in rel_entries(node):
        m = REL_DECL_RE.match(entry)
        if not m:
            continue
        rep.count("rel")
        kind = m.group(1).lower()
        subject = denorm(m.group(2)).strip().strip(".,;")
        mechanism = " ".join(m.group(3).split())
        if not subject or "*" in subject:
            rep.fail("rel", nid, "declaration `%s` names no single subject (wildcards and "
                                 "blanket declarations are rejected)" % entry.strip()[:80])
            continue
        # F1 (2026-08-17): three independent conditions, because a pure length
        # gate is cleared by 26 literal `q` characters.  A mechanism must be long
        # enough, be several WORDS, and ANCHOR in something checkable.
        deficits = []
        if len(re.sub(r"\s", "", mechanism)) < MIN_MECHANISM_CHARS:
            deficits.append("needs >= %d non-space characters, has %d"
                            % (MIN_MECHANISM_CHARS, len(re.sub(r"\s", "", mechanism))))
        if len(mechanism.split()) < MIN_MECHANISM_WORDS:
            deficits.append("needs >= %d words, has %d"
                            % (MIN_MECHANISM_WORDS, len(mechanism.split())))
        if not MECHANISM_TOKEN_RE.search(mechanism):
            deficits.append("names no `backticked identifier`, dotted node id, or "
                            "ruling/deviation reference")
        if deficits:
            rep.fail("rel", nid, "declaration `%s: %s` carries no substantive mechanism "
                                 "(%s) -- it must name HOW the premise arrives / WHY the "
                                 "route is unrendered, in terms a reviewer can check"
                     % (kind, subject, "; ".join(deficits)))
            continue
        if subject in out[kind]:
            rep.fail("rel", nid, "duplicate `%s` declaration for `%s`" % (kind, subject))
            continue
        out[kind][subject] = mechanism
    return out


def check_cited_fields(mechanism, nid, check, iface_src, iface_name, rep):
    """Every `Cited.<field>` named in a declaration must exist in `Interface.lean`."""
    if iface_src is None:
        return
    for field in sorted(set(re.findall(r"\bCited\.(%s)" % IDENT, mechanism))):
        if not re.search(r"^[ \t]+%s\s*:" % re.escape(field), iface_src, re.M):
            rep.fail(check, nid, "declaration names the cited field `Cited.%s`, which does NOT "
                                 "exist in %s -- the declared mechanism cannot be the real one"
                     % (field, iface_name))


def descendants_of(nid, nodes):
    """Transitive premise closure of `nid` (schema-v6 routes / pre-v6 children)."""
    seen, stack = set(), [nid]
    while stack:
        cur = stack.pop()
        node = nodes.get(cur)
        if node is None:
            continue
        for kid in node.children:
            if kid not in seen:
                seen.add(kid)
                stack.append(kid)
    return seen


def skipped_intermediates(nid, subject, nodes, desc_cache):
    """Nodes strictly BETWEEN `nid` and `subject` on some premise path.

    `v` is skipped by a direct `nid -> subject` import iff `v` is a descendant of
    `nid`, `subject` is a descendant of `v`, and `v` is neither endpoint.  Review
    item F3: `import-not-child` is licensed because the intermediates have NO
    module to route the import through, so EVERY skipped node must lack a
    `formalization` block -- exactly what the real declarations assert in prose.
    Any path through a mechanized node is enough to void the licence, which is why
    the union over paths (not one chosen path) is the right set.
    """
    def desc(x):
        if x not in desc_cache:
            desc_cache[x] = descendants_of(x, nodes)
        return desc_cache[x]
    return sorted(v for v in desc(nid)
                  if v != subject and v != nid and subject in desc(v))


def route_disabled_reason(route, nodes):
    """§4: why this route is DISABLED, or `None` if it is a live alternative.

    A refuted route implication kills that route; a refuted premise disables every
    route requiring it.  Check 7c already uses exactly this predicate for the
    epistemic floor; checks that ask "which alternatives must be rendered?" use it
    too, because a dead route is not an alternative anyone can be asked to mirror.
    """
    level = normalize_status((route.get("assessment") or {}).get("level") or "")
    if level == "REFUTED":
        return "route implication REFUTED"
    for premise in route.get("premises") or []:
        pn = nodes.get(str(premise))
        if pn is not None and pn.status == "REFUTED":
            return "premise %s is REFUTED" % premise
    return None


def decl_key(dmap, *aliases):
    for alias in aliases:
        if alias and alias in dmap:
            return alias
    return None


def as_name_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    v = str(value).strip()
    if not v or v.lower() == "null":
        return []
    return [v]


# ---------------------------------------------------------------------------
# the seven checks
# ---------------------------------------------------------------------------

def run_checks(spec: ProblemSpec, root: Path, rep: Report,
               nodes_dir: Path = None, lean_dir: Path = None):
    nodes_dir = Path(nodes_dir) if nodes_dir else (root / spec.nodes_dir)
    lean_dir = Path(lean_dir) if lean_dir else (root / spec.lean_dir)

    if not nodes_dir.is_dir():
        rep.fail("0", str(nodes_dir), "nodes directory does not exist")
        return
    if not lean_dir.is_dir():
        rep.fail("0", str(lean_dir), "lean directory does not exist")
        return

    schema, nodes = load_nodes(spec, nodes_dir, rep)
    rep.count("schema:" + schema)

    # source cache -------------------------------------------------------
    src_cache = {}

    def src_of(node):
        f = node.lean.get("file")
        if not f:
            return None
        path = Path(f)
        if not path.is_absolute():
            path = root / f
        if not path.is_file():
            return None
        if path not in src_cache:
            src_cache[path] = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        return src_cache[path]

    mech = {nid: n for nid, n in nodes.items() if n.lean}
    rep.count("nodes", len(nodes))
    rep.count("mechanized", len(mech))
    rep.count("lean-none", len(nodes) - len(mech))

    # ---- explicit deviation declarations (parsed ONCE per node) --------
    # Hygiene failures are emitted here under check id `rel`, so a malformed
    # declaration is reported once instead of once per consuming check.
    iface_path = lean_dir / "Interface.lean"
    iface_src = (iface_path.read_text(encoding="utf-8").replace("\r\n", "\n")
                 if iface_path.is_file() else None)
    iface_name = (spec.module_prefix + ".Interface") if iface_src is not None else "(none)"
    rel_decls = {nid: parse_rel_declarations(n, nid, rep) for nid, n in sorted(mech.items())}
    empty_decls = {kind: {} for kind in DECL_KINDS}
    desc_cache = {}
    # F2 (2026-08-17, review item F2 of artifacts/se_task006_review_20260817.md):
    # the residual risk is stated AT THE POINT OF USE, not only in the docstring,
    # because the reader of a green run is who needs to know it.  It is not
    # mechanically fixable -- see "WHAT THIS CHECKER DOES NOT DECIDE" above.
    n_decl = sum(len(m) for d in rel_decls.values() for m in d.values())
    if n_decl:
        rep.info("rel", nodes_dir.name, RELEVANCE_NOTICE % n_decl)
    # F6: say what `sync_state` does and does not assert, wherever it is reported.
    sync_counts = {}
    for n in mech.values():
        s = str((n.lean or {}).get("sync_state") or "").strip().lower()
        if s:
            sync_counts[s] = sync_counts.get(s, 0) + 1
    if sync_counts:
        rep.info("3", nodes_dir.name,
                 SYNC_STATE_NOTICE % (sync_counts.get("current", 0), sync_counts.get("stale", 0)))

    # ---- silence check (§7.4): lean: none must carry a reason ----------
    # NOT one of the seven.  Under schema v6 the field it tests does not exist:
    # a node with no formal mirror OMITS `formalization` (DAG_PROTOCOL §1, §7),
    # so there is no `lean: none` reason to grade.  Reported once, explicitly,
    # instead of emitting a protocol-compliant WARN on every unmechanized node.
    if schema == "v6":
        rep.info("0", nodes_dir.name,
                 "schema v6 has no `lean: none` + reason field: absence of a formal "
                 "mirror is recorded by OMITTING `formalization` (DAG_PROTOCOL §1/§7), "
                 "so the §7.4 per-node silence check is NOT PORTABLE and is not run. "
                 "%d of %d nodes carry no `formalization.lean` block."
                 % (len(nodes) - len(mech), len(nodes)))
    for nid, n in sorted(nodes.items()):
        if n.lean or schema == "v6":
            continue
        if not n.has_lean_section:
            rep.warn("0", nid, "no `## Lean` section at all (§7.4: silence is invalid)")
        elif n.lean_none_reason is None:
            rep.warn("0", nid, "`## Lean` section present but neither a `lean:` block "
                               "nor a `lean: none` marker was found")
        elif len(n.lean_none_reason.strip()) < 10:
            rep.warn("0", nid, "`lean: none` is bare -- §7.4 requires a reason")

    # ---- check 1: existence -------------------------------------------
    for nid, n in sorted(mech.items()):
        declared_file = n.lean.get("file")
        if not declared_file:
            rep.fail("1", nid, "`lean:` block has no `file:` key")
            continue
        path = Path(declared_file)
        if not path.is_absolute():
            path = root / declared_file
        if not path.is_file():
            rep.fail("1", nid, "declared module file does not exist: %s" % declared_file)
            continue
        src = src_of(n)
        rep.count("1")
        claim_name = n.lean.get("claim") or "Claim"
        claim_kinds = "def|abbrev|noncomputable def|theorem|lemma"
        if not has_decl(src, claim_kinds, claim_name):
            rep.fail("1", nid, "claim declaration `%s` not found in %s"
                     % (claim_name, declared_file))
        for name in as_name_list(n.lean.get("composition")):
            if not has_decl(src, "theorem|lemma", name):
                rep.fail("1", nid, "declared composition theorem `%s` not found in %s"
                         % (name, declared_file))
        # declared module name must match the declared file path
        declared_mod = denorm(str(n.lean.get("module") or ""))
        actual_mod = module_of_declared_file(root, path)
        if actual_mod and declared_mod and denorm(actual_mod) != declared_mod:
            rep.fail("1", nid, "declared module `%s` != module implied by file path `%s`"
                     % (declared_mod, actual_mod))

    # ---- check 2: bijection -------------------------------------------
    declared_files = {}
    for nid, n in mech.items():
        declared = n.lean.get("file")
        if declared:
            path = Path(declared)
            if not path.is_absolute():
                path = root / path
            declared_files[path.resolve()] = nid

    lean_modules = {}
    for p in sorted(lean_dir.rglob("*.lean")):
        if is_non_node_module(spec, lean_dir, p):
            continue
        if is_explicit_nonformalization_file(p):
            rep.info("2", p.name,
                     "explicit `lean: none` documentation file excluded from the module bijection")
            continue
        lean_modules[denorm(module_of_file(lean_dir, p, spec.module_prefix))] = p
    internal_node_modules = {}
    for nid, n in mech.items():
        declared = n.lean.get("file")
        if not declared:
            continue
        path = Path(declared)
        if not path.is_absolute():
            path = root / path
        try:
            path.resolve().relative_to(lean_dir.resolve())
        except ValueError:
            continue
        internal_node_modules[denorm(str(n.lean.get("module") or ""))] = nid

    rep.count("2", len(lean_modules) + len(mech))
    for mod, p in sorted(lean_modules.items()):
        if p.resolve() not in declared_files:
            rep.fail("2", mod, "node-shaped Lean module has no DAG node carrying a "
                               "`lean:` block (file %s)" % p.name)
    for mod, nid in sorted(internal_node_modules.items()):
        if mod not in lean_modules:
            rep.fail("2", nid, "node declares module `%s` but no such node-shaped "
                               ".lean file exists under the lean dir" % mod)
        elif mod != nid:
            rep.fail("2", nid, "module name `%s` != node id `%s`" % (mod, nid))

    # ---- check 3 / 3b: hash triple-agreement + verbatim body ----------
    for nid, n in sorted(mech.items()):
        src = src_of(n)
        if src is None:
            continue
        rep.count("3")
        recomputed = n.claim_hash()
        if recomputed is None:
            rep.fail("3", nid, "no canonical claim -- cannot recompute the frozen hash")
            continue
        declared = str(n.lean.get("claim_hash") or "").strip()
        declared_hex = declared.split(":")[-1].strip().lower()
        if declared_hex != recomputed:
            rep.fail("3", nid, "node `claim_hash` %s != recomputed %s"
                     % (declared_hex or "(absent)", recomputed))
        doc = docstring_of(src)
        current_digest = re.search(
            r"(?im)^\s*current_claim_hash:\s*sha256:([0-9a-fA-F]{64})\s*$", doc
        )
        hexes = ([current_digest.group(1).lower()] if current_digest else
                 sorted(set(h.lower() for h in re.findall(r"\b[0-9a-fA-F]{64}\b", doc))))
        if not hexes:
            rep.fail("3", nid, "no SHA-256 digest embedded in the Lean docstring")
        elif len(hexes) > 1:
            rep.warn("3", nid, "docstring carries %d distinct 64-hex digests %s"
                     % (len(hexes), hexes))
            if recomputed not in hexes:
                rep.fail("3", nid, "recomputed %s is not among the docstring digests%s"
                         % (recomputed, drift_note(n, hexes)))
        elif hexes[0] != recomputed:
            rep.fail("3", nid, "docstring digest %s != recomputed %s%s"
                     % (hexes[0], recomputed, drift_note(n, hexes)))
        # 3b (extra, WARN): the frozen body itself, not just the hash line
        # The body runs from the frozen-claim heading (WHGAP `## Frozen Claim`,
        # SE/KSUM `FROZEN CLAIM (verbatim ...)`) to the first terminator: the
        # WHGAP hash line, the SE/KSUM "(Indentation added ...)" disclaimer, a
        # box-drawing rule, or the end of the header comment.
        m = re.search(
            r"^[ \t]*CURRENT CANONICAL CLAIM[^\n]*\n(.*?)"
            r"(?=^[ \t]*END CURRENT CANONICAL CLAIM)", doc, re.S | re.M
        )
        if not m:
            m = re.search(r"^(?:## Frozen Claim|[ \t]*FROZEN CLAIM)[^\n]*\n(.*?)"
                          r"(?=^\*\s*frozen-claim SHA-256|^[ \t]*\(Indentation added"
                          r"|^[ \t]*[─—-]{10,}|\Z)", doc, re.S | re.M)
        if m:
            frozen = dedent_block(m.group(1))
            if frozen != (n.claim_text() or "").strip():
                rep.warn("3b", nid, "docstring frozen Claim body differs from the node's "
                                    "canonical claim (hash line may be stale-but-intact)")
        else:
            rep.warn("3b", nid, "could not locate a frozen-Claim body in the docstring "
                                "-- verbatim comparison skipped")

    # ---- check 4: AND coverage (textual approximation) ----------------
    for nid, n in sorted(mech.items()):
        if n.kind != "AND":
            continue
        src = src_of(n)
        if src is None:
            continue
        names = as_name_list(n.lean.get("composition"))
        if not names:
            continue
        text = "\n".join(decl_text(src, nm) for nm in names)
        rep.count("4")
        for child in n.children:
            short = child.split(".", 1)[-1]
            if short not in text:
                rep.warn("4", nid, "composition theorem text does not mention child `%s` "
                                   "(TEXTUAL APPROXIMATION: a sound check needs elaboration)"
                         % child)
        for other in mech:
            if other == nid or other in n.children:
                continue
            short = other.split(".", 1)[-1]
            if re.search(r"«%s»" % re.escape(short), text):
                rep.warn("4", nid, "composition theorem text mentions non-child node module "
                                   "`%s` (textual approximation)" % other)

    # ---- check 5: OR route match --------------------------------------
    for nid, n in sorted(mech.items()):
        if n.kind != "OR":
            continue
        src = src_of(n)
        if src is None:
            continue
        rep.count("5")
        vias = re.findall(r"^[ \t]*theorem\s+composition_via_«?([^\s(»]+)»?",
                          src, re.M)
        # The alternatives of an OR node are its CHILDREN pre-v6 and its live
        # ROUTES under v6 (§2: "the different routes of one node are
        # alternatives").  Same check, same FAIL, on the object that carries the
        # alternation in each schema.
        registered = list(n.live_routes) if n.schema == "v6" else list(n.children)
        label = "live routes" if n.schema == "v6" else "children"
        decls = rel_decls.get(nid, empty_decls)
        # §4: a route whose implication is REFUTED, or which requires a REFUTED
        # premise, is DISABLED.  It is not an alternative anyone can be asked to
        # mirror in Lean, so it is removed from the REQUIRED set -- and the removal
        # is REPORTED, never silent.  (Same predicate check 7c already applies to
        # the epistemic floor; see `route_disabled_reason`.)
        disabled = {}
        if n.schema == "v6":
            for rid, route in sorted(n.live_routes.items()):
                why = route_disabled_reason(route, nodes)
                if why:
                    disabled[rid] = why
            if disabled:
                rep.info("5", nid, "route(s) DISABLED per §4 and therefore not required to carry a "
                                   "`composition_via_*` theorem: %s"
                         % "; ".join("%s (%s)" % (r, w) for r, w in sorted(disabled.items())))
        alternatives = [r for r in registered if r not in disabled]
        suffix_of = {
            r: re.sub(r"[^A-Za-z0-9_'!?]", "_", r.split(".", 1)[-1])
            for r in registered
        }
        by_suffix = {}
        for r in registered:
            by_suffix.setdefault(suffix_of[r], r)
        if vias:
            got = set(vias)
            want = set(suffix_of[r] for r in alternatives)
            # a rendered route theorem that matches NO registered route: a renamed
            # or silently deleted route.  Unchanged severity: FAIL.
            unknown = sorted(got - set(by_suffix))
            if unknown:
                rep.fail("5", nid, "composition_via_* theorem(s) %s correspond to no %s of this "
                                   "node -- a renamed or silently dropped route" % (unknown, label))
            declared, undeclared = [], []
            for suf in sorted(want - got):
                if decl_key(decls["route-not-formalized"], suf, by_suffix.get(suf)):
                    declared.append(suf)
                else:
                    undeclared.append(suf)
            if undeclared:
                rep.fail("5", nid, "composition_via_* suffixes %s != %s %s; UNDECLARED unrendered "
                                   "route(s) %s -- each needs either a rendered theorem or an "
                                   "explicit `route-not-formalized: <route> - <reason>` entry in "
                                   "formalization.lean.rel"
                         % (sorted(got), label, sorted(want), undeclared))
            if declared:
                rep.info("5", nid, "unrendered route(s) %s, each DECLARED not-formalized in "
                                   "lean.rel: %s"
                         % (declared, " | ".join(
                             "%s: %s" % (s, decls["route-not-formalized"][
                                 decl_key(decls["route-not-formalized"], s, by_suffix.get(s))])
                             for s in declared)))
            # a declaration contradicted by the module, or naming a route this node
            # does not have, is a FALSE record: FAIL.
            for subject, mechanism in sorted(decls["route-not-formalized"].items()):
                if subject not in by_suffix and subject not in registered:
                    rep.fail("5", nid, "lean.rel declares route `%s` not-formalized, but this node "
                                       "registers no such route (%s: %s)"
                             % (subject, label, sorted(registered)))
                elif suffix_of.get(subject, subject) in got:
                    rep.fail("5", nid, "lean.rel declares route `%s` not-formalized, but "
                                       "`composition_via_%s` EXISTS in the module -- the "
                                       "declaration is false"
                             % (subject, suffix_of.get(subject, subject)))
                else:
                    check_cited_fields(mechanism, nid, "5", iface_src, iface_name, rep)
        else:
            names = as_name_list(n.lean.get("composition"))
            if not names:
                rep.fail("5", nid, "%s node declares neither composition_via_* theorems "
                                   "nor an AND-style composition" % n.kind)
            else:
                rep.info("5", nid, "no composition_via_* theorems; single AND-style "
                                   "composition %s accepted (§7.6 note)" % names)

    # ---- check 6: import graph == children ----------------------------
    for nid, n in sorted(mech.items()):
        src = src_of(n)
        if src is None:
            continue
        rep.count("6")
        imported = set()
        for imp in imports_of(src):
            mod = denorm(imp)
            if not mod.startswith(spec.module_prefix + "."):
                continue
            tail = mod[len(spec.module_prefix) + 1:]
            if tail.split(".")[0] in spec.non_node_prefixes:
                continue
            if tail in spec.non_node_modules:
                continue
            imported.add(mod)
        all_children = set(n.children)
        if n.schema == "v6":
            # Premises of a disabled route are retained in the public graph as
            # failed history, but they are not dependencies of the live Lean
            # composition and therefore must not be imported merely to satisfy
            # the bijection check.
            want = {
                str(premise)
                for route in n.live_routes.values()
                if route_disabled_reason(route, nodes) is None
                for premise in (route.get("premises") or [])
            }
        else:
            want = set(n.children)
        decls = rel_decls.get(nid, empty_decls)
        pni = decls["premise-not-imported"]
        inc = decls["import-not-child"]
        extra = sorted(imported - want)
        missing = sorted(want - imported)
        # Both directions, as before: an import that is not a child is a possible
        # undeclared dependency; a child that is not imported is an unmirrored
        # premise (typically routed through `Interface.Cited`).  DAG_PROTOCOL §1
        # licenses the latter -- but only when it is WRITTEN DOWN.  So the two
        # lists are split into DECLARED (INFO) and UNDECLARED (still FAIL).
        und_extra = [m for m in extra if m not in inc]
        und_missing = [c for c in missing if c not in pni]
        if und_extra or und_missing:
            detail = []
            if und_extra:
                detail.append("UNDECLARED imports not among children: %s" % und_extra)
            if und_missing:
                detail.append("UNDECLARED children not imported: %s" % [
                    "%s (%s)" % (c, "mechanized" if c in mech else "no formal mirror")
                    for c in und_missing])
            rep.fail("6", nid, "node-module imports %s != children %s (%s) -- DAG_PROTOCOL §1 lets "
                               "a premise arrive as a child, a cited interface or an explicit "
                               "relative hypothesis, but every such arrival must be NAMED in "
                               "formalization.lean.rel as `premise-not-imported: <child> - "
                               "<mechanism>` / `import-not-child: <module> - <mechanism>`"
                     % (sorted(imported), sorted(want), "; ".join(detail)))
        elif extra or missing:
            bits = ["%s <- %s" % (c, pni[c]) for c in missing] \
                 + ["%s (non-child import) <- %s" % (m, inc[m]) for m in extra]
            rep.info("6", nid, "imports %s != children %s, and EVERY difference is declared in "
                               "lean.rel: %s" % (sorted(imported), sorted(want), " | ".join(bits)))
        # declaration hygiene: a declaration contradicted by the module or by the
        # graph is a FALSE record and FAILs.  This is strictly more work for the
        # author than the old unconditional FAIL, not less.
        descendants = None
        for subject, mechanism in sorted(pni.items()):
            if subject in imported:
                rep.fail("6", nid, "lean.rel declares premise `%s` not imported, but the module "
                                   "DOES import it -- the declaration is false" % subject)
                continue
            if subject in all_children and subject not in want:
                rep.info("6", nid, "lean.rel retains the non-import declaration for disabled-route "
                                   "premise `%s`; it is historical metadata and is not required by "
                                   "the live composition" % subject)
                continue
            if subject not in want:
                rep.fail("6", nid, "lean.rel declares premise `%s` not imported, but `%s` is not a "
                                   "premise of any live route of this node (children: %s)"
                         % (subject, subject, sorted(want)))
                continue
            # F3/F4 companion (2026-08-17, review item F4): the §1 arrivals this
            # declaration channel exists for -- a cited interface field, an
            # explicit relative hypothesis -- are how a premise with NO module
            # reaches the composition.  A MECHANIZED premise has a module, so
            # "it could not be imported" is false on its face and the import must
            # be made (or the premise removed from the route).
            if subject in mech:
                rep.fail("6", nid, "lean.rel declares premise `%s` not imported, but `%s` CARRIES A "
                                   "`formalization` BLOCK (module `%s`) -- a module for it "
                                   "demonstrably exists, so the composition must import it rather "
                                   "than route it around the DAG"
                         % (subject, subject,
                            denorm(str((mech[subject].lean or {}).get("module") or subject))))
                continue
            check_cited_fields(mechanism, nid, "6", iface_src, iface_name, rep)
        for subject, mechanism in sorted(inc.items()):
            if subject in want:
                rep.fail("6", nid, "lean.rel declares `%s` a non-child import, but it IS a child of "
                                   "this node -- the declaration is false" % subject)
                continue
            if subject not in imported:
                rep.fail("6", nid, "lean.rel declares the non-child import `%s`, but the module "
                                   "does not import it (imports: %s)"
                         % (subject, sorted(imported)))
                continue
            if descendants is None:
                descendants = descendants_of(nid, nodes)
            if subject not in descendants:
                rep.fail("6", nid, "declared non-child import `%s` is NOT a DAG descendant of `%s`: "
                                   "skipping an unmechanized intermediate node is licensed, "
                                   "importing from outside the subtree is the undeclared "
                                   "dependency this check exists to catch" % (subject, nid))
                continue
            # F3 (2026-08-17): descendancy alone was not the licence.  The licence
            # is that the skipped nodes have NO module to import, which is what all
            # four real declarations assert.  If a skipped intermediate IS
            # mechanized, the import must go through it.
            skipped = skipped_intermediates(nid, subject, nodes, desc_cache)
            skipped_mech = [v for v in skipped if v in mech]
            if skipped_mech:
                rep.fail("6", nid, "declared non-child import `%s` is a DAG descendant of `%s`, but "
                                   "it is reached ACROSS the MECHANIZED intermediate node(s) %s, "
                                   "which do carry a `formalization` block -- the licence for a "
                                   "non-child import is that the skipped nodes have NO module to "
                                   "import (skipped: %s)"
                         % (subject, nid, skipped_mech, skipped))
                continue
            check_cited_fields(mechanism, nid, "6", iface_src, iface_name, rep)

    # ---- check 7a/7b: state backing + rel display ---------------------
    for nid, n in sorted(mech.items()):
        src = src_of(n)
        if src is None:
            continue
        rep.count("7a")
        raw_state = str(n.lean.get("state") or "").strip()
        parens = re.findall(r"\(([^()]*)\)", raw_state)
        bare = re.sub(r"\([^()]*\)", " ", raw_state)
        tokens = [t.strip() for t in re.split(r"[+,]", bare) if t.strip()]
        if not tokens:
            rep.fail("7a", nid, "`state` is empty or unparseable: %r" % raw_state)
            continue
        unknown = [t for t in tokens if t not in STATE_VOCAB]
        if unknown:
            rep.fail("7a", nid, "state token(s) outside the §7.1 vocabulary: %s (state=%r)"
                     % (unknown, raw_state))
        named = []
        for grp in parens:
            if ":" not in grp:
                continue
            for seg in grp.split(":", 1)[1].split(","):
                seg = seg.strip()
                if re.fullmatch(IDENT, seg):
                    named.append(seg)
        comp_names = as_name_list(n.lean.get("composition"))
        claim_name = n.lean.get("claim") or "Claim"

        for tok in tokens:
            if tok == "stated":
                if not has_decl(src, "def|abbrev|noncomputable def|theorem|lemma", claim_name):
                    rep.fail("7a", nid, "state asserts `stated` but claim declaration `%s` is absent"
                             % claim_name)
            elif tok == "composition-checked":
                if not comp_names:
                    rep.fail("7a", nid, "state asserts `composition-checked` but "
                                        "`composition` is null -- UNBACKED (the R11 MAJOR-2 class)")
                else:
                    missing = [c for c in comp_names if not has_decl(src, "theorem|lemma", c)]
                    if missing:
                        rep.fail("7a", nid, "state asserts `composition-checked` but the "
                                            "named theorem(s) %s do not exist in the module "
                                            "-- UNBACKED (the R11 MAJOR-2 class)" % missing)
            elif tok == "proved":
                ok = False
                if comp_names and all(has_decl(src, "theorem|lemma", c) for c in comp_names):
                    ok = True
                if has_decl(src, "theorem|lemma", "holds"):
                    ok = True
                present = [nm for nm in named if has_decl(src, "theorem|lemma", nm)]
                if present:
                    ok = True
                missing_named = [nm for nm in named
                                 if not has_decl(src, "theorem|lemma", nm)]
                if missing_named:
                    rep.fail("7a", nid, "state names theorem(s) %s that do not exist in "
                                        "the module" % missing_named)
                if not ok:
                    rep.fail("7a", nid, "state asserts `proved` but neither a declared "
                                        "composition theorem, nor `theorem holds`, nor any "
                                        "named theorem exists -- UNBACKED")
            elif tok == "refuted":
                if not has_decl(src, "theorem|lemma", "not_%s" % claim_name):
                    rep.fail("7a", nid, "state asserts `refuted` but `theorem not_%s` is absent"
                             % claim_name)

        if any(t in ("composition-checked", "proved") for t in tokens):
            rep.count("7b")
            if "rel" not in n.lean:
                rep.fail("7b", nid, "state %r requires the `rel` key to be present (§7.1)"
                         % raw_state)
            else:
                rel = n.lean.get("rel")
                rel_list = rel if isinstance(rel, list) else ([] if rel in (None, "") else [rel])
                if not rel_list and comp_names:
                    extras = []
                    for cname in comp_names:
                        sig = decl_text(src, cname).split(":=")[0]
                        for binder in re.findall(r"[\(\{\[]([^\(\)\{\}\[\]]*)[\)\}\]]", sig):
                            if ".Claim" in binder or "Claim " in binder:
                                continue
                            if "Interface" in binder:
                                continue
                            extras.append(binder.strip())
                    if extras:
                        rep.warn("7b", nid, "`rel: []` but the composition signature carries "
                                            "binders that are not child Claims: %s -- cannot "
                                            "decide textually whether these are extra "
                                            "hypotheses" % extras)

    # ---- check 7c: epistemic recomputation (WARN) ---------------------
    # v6 has no per-node `composition:` block: each ROUTE owns an assessment, and
    # routes are alternatives.  So the floor is max over live routes of
    # min(route level, premise levels) -- which reduces to the pre-v6 AND formula
    # for a single-route node -- and the scoped-input exception is read from the
    # node's `assessment.caveats` (v6's home for a declared dependency, cf.
    # proof_dag_v6's completion lint) instead of the retired `composition.rel`.
    for nid, n in sorted(nodes.items()):
        if n.schema != "v6" or not n.live_routes or n.status not in LADDER:
            continue
        best, labels_best, candidates = None, None, 0
        for rid, route in sorted(n.live_routes.items()):
            route_status = normalize_status((route.get("assessment") or {}).get("level") or "")
            if route_status not in LADDER:
                continue
            # §4: a refuted route implication kills that route, and a refuted
            # premise disables every route that requires it.  A disabled route is
            # not a candidate support -- it must not drag the floor to REFUTED.
            premises = [nodes.get(str(p)) for p in (route.get("premises") or [])]
            if route_status == "REFUTED" or any(
                    p is not None and p.status == "REFUTED" for p in premises):
                continue
            candidates += 1
            vals = [LADDER[route_status]]
            labels = ["route %s=%s" % (rid, route_status)]
            for premise, pn in zip(route.get("premises") or [], premises):
                if pn is None or pn.status not in LADDER:
                    continue
                vals.append(LADDER[pn.status])
                labels.append("%s=%s" % (premise, pn.status))
            floor = min(vals)
            if best is None or floor > best:
                best, labels_best = floor, labels
        rep.count("7c")
        if not candidates:
            # every registered route is disabled: §4 caps the parent at OPEN or
            # PARKED unless the parent's OWN claim was refuted.
            if LADDER[n.status] > LADDER["OPEN"]:
                rep.warn("7c", nid, "node level %s while every registered route is "
                                    "disabled by a REFUTED implication or premise (§4 caps "
                                    "such a parent at OPEN/PARKED)" % n.status)
            continue
        if best is None:
            continue
        if LADDER[n.status] > best:
            invoked = [c for c in n.caveats
                       if any(lbl.split("=")[0] in c for lbl in labels_best[1:])]
            # §2 makes the shortfall load-bearing only at a completion tier; §3
            # explicitly denies that the ladder is graph arithmetic below that, so
            # the two cases are reported with different force (same severity).
            force = ("" if LADDER[n.status] >= LADDER["CERTIFIED*"] else
                     " [below the completion tier, where §3 permits a mother to sit "
                     "above her premises -- reported for review, not as a defect]")
            if invoked:
                rep.warn("7c", nid, "node level %s exceeds min(%s) on its best live route; "
                                    "scoped-input exception invoked, caveat reads: %s%s"
                         % (n.status, ", ".join(labels_best), " | ".join(invoked), force))
            else:
                rep.warn("7c", nid, "node level %s exceeds min(%s) on its best live route "
                                    "and NO assessment caveat names the shortfall%s"
                         % (n.status, ", ".join(labels_best), force))

    for nid, n in sorted(nodes.items()):
        if n.schema == "v6" or n.kind != "AND":
            continue
        comp = n.composition
        if not comp or comp.get("__none__"):
            continue
        comp_status = normalize_status(comp.get("status") or "")
        if comp_status not in LADDER:
            continue
        vals = [LADDER[comp_status]]
        labels = ["composition=%s" % comp_status]
        for child in n.children:
            cn = nodes.get(child)
            if cn is None or cn.status not in LADDER:
                continue
            vals.append(LADDER[cn.status])
            labels.append("%s=%s" % (child, cn.status))
        if n.status not in LADDER:
            continue
        rep.count("7c")
        floor = min(vals)
        if LADDER[n.status] > floor:
            rel = comp.get("rel")
            rel_list = rel if isinstance(rel, list) else ([] if rel in (None, "") else [rel])
            if rel_list:
                rep.warn("7c", nid, "header status %s exceeds min(%s); scoped-input "
                                    "exception invoked, composition rel reads: %s"
                         % (n.status, ", ".join(labels), " | ".join(rel_list)))
            else:
                rep.warn("7c", nid, "header status %s exceeds min(%s) and the composition "
                                    "block documents NO rel exception"
                         % (n.status, ", ".join(labels)))


# ---------------------------------------------------------------------------
# self-test fixtures
# ---------------------------------------------------------------------------

CLEAN_CHILD_CLAIM = "Child claim body: P(y) holds for every y. **[PROVED]**"
CLEAN_PARENT_CLAIM = "Parent claim body: R(z) holds for every z. **[OPEN]**"


def _node_md(nid, kind, status, children, claim_body, lean_yaml):
    kids = json.dumps(children)
    return (
        "---\n"
        'id: "%s"\n'
        "kind: %s\n"
        "status: %s\n"
        "children: %s\n"
        "---\n\n"
        "# %s\n\n"
        "## Claim\n\n"
        "%s\n\n"
        "## Role in DAG\n\nfixture.\n\n"
        "## Lean\n\n"
        "```yaml\n%s```\n"
    ) % (nid, kind, status, kids, nid, claim_body, lean_yaml)


def _lean_module(module, node_file, claim_text, digest, body, imports):
    imp = "".join("import %s\n" % i for i in imports)
    return (
        "%s\n/-!\n# `%s`\n\n"
        "* node file: `%s`\n\n"
        "## Frozen Claim (verbatim from the node file, `## Claim` section)\n\n"
        "%s\n\n"
        "* frozen-claim SHA-256: `%s`\n-/\n\n"
        "namespace %s\n\n"
        "%s\n"
        "end %s\n"
    ) % (imp, module, node_file, claim_text, digest, module, body, module)


def build_fixture(base: Path, variant: str):
    """Write a synthetic (nodes/, lean/) pair; never touches any real tree."""
    root = base / variant
    nodes = root / "nodes"
    lean = root / "lean" / "FIX"
    nodes.mkdir(parents=True)
    lean.mkdir(parents=True)

    child_claim = CLEAN_CHILD_CLAIM
    parent_claim = CLEAN_PARENT_CLAIM
    ch = hashlib.sha256(child_claim.encode("utf-8")).hexdigest()
    ph = hashlib.sha256(parent_claim.encode("utf-8")).hexdigest()

    child_lean_yaml = (
        "lean:\n"
        '  module: "FIX.child"\n'
        '  file: "%s"\n'
        '  claim: "Claim"\n'
        "  composition: null\n"
        '  state: "stated"\n'
        "  rel: []\n"
        '  claim_hash: "sha256:%s"\n'
    ) % ((lean / "child.lean").as_posix(), ch)

    parent_state = '"composition-checked"'
    parent_comp = '"composition"'
    parent_children = ["FIX.child"]
    parent_imports = ["FIX.child"]
    parent_body = (
        "def Claim : Prop := True\n\n"
        "theorem composition (h : FIX.child.Claim) : Claim := trivial\n"
    )
    parent_hash_in_node = ph
    parent_hash_in_doc = ph
    parent_claim_body = parent_claim

    if variant == "major2_unbacked_state":
        # the R11 MAJOR-2 class: state claims composition-checked, module has none
        parent_comp = "null"
        parent_body = "def Claim : Prop := True\n"
    elif variant == "stale_hash":
        # Claim body edited on the node; the recorded hash was left intact
        parent_claim_body = parent_claim + " EDITED AFTER FREEZING."
    elif variant == "import_mismatch":
        parent_imports = ["FIX.Interface"]
        parent_body = "def Claim : Prop := True\n\ntheorem composition : Claim := trivial\n"

    parent_lean_yaml = (
        "lean:\n"
        '  module: "FIX.parent"\n'
        '  file: "%s"\n'
        '  claim: "Claim"\n'
        "  composition: %s\n"
        "  state: %s\n"
        '  rel: ["fixture"]\n'
        '  claim_hash: "sha256:%s"\n'
    ) % ((lean / "parent.lean").as_posix(), parent_comp, parent_state, parent_hash_in_node)

    (nodes / "FIX.child.md").write_text(
        _node_md("FIX.child", "null", "PROVED", [], child_claim, child_lean_yaml),
        encoding="utf-8")
    (nodes / "FIX.parent.md").write_text(
        _node_md("FIX.parent", "AND", "OPEN", parent_children, parent_claim_body,
                 parent_lean_yaml),
        encoding="utf-8")

    (lean / "Interface.lean").write_text("/-! fixture interface -/\n",
                                         encoding="utf-8")
    (lean / "child.lean").write_text(
        _lean_module("FIX.child", "nodes/FIX.child.md", child_claim, ch,
                     "def Claim : Prop := True\n", []),
        encoding="utf-8")
    (lean / "parent.lean").write_text(
        _lean_module("FIX.parent", "nodes/FIX.parent.md", parent_claim, parent_hash_in_doc,
                     parent_body, parent_imports),
        encoding="utf-8")

    spec = ProblemSpec(nodes_dir="nodes", lean_dir="lean/FIX", module_prefix="FIX")
    return spec, root, nodes, lean


def _v6_node_yaml(nid, claim, level, routes_yaml, lean_yaml):
    return (
        "id: %s\n"
        "claim: %s\n"
        "%s"
        "assessment:\n"
        "  level: %s\n"
        "  summary: fixture assessment.\n"
        "%s"
        "events:\n"
        "  created-2026-01-01:\n"
        "    date: '2026-01-01'\n"
        "    type: created\n"
        "    summary: fixture.\n"
        "    sources:\n"
        "    - path: tools/lean_dag_check.py\n"
        "      kind: text\n"
    ) % (nid, json.dumps(claim), routes_yaml, level, lean_yaml)


def build_v6_fixture(base: Path, variant: str):
    """Write a synthetic schema-v6 (nodes/, lean/) pair; never touches any real tree."""
    root = base / variant
    nodes = root / "nodes"
    lean = root / "lean" / "FIX"
    nodes.mkdir(parents=True)
    lean.mkdir(parents=True)

    child_claim = CLEAN_CHILD_CLAIM.replace(" **[PROVED]**", "")
    parent_claim = CLEAN_PARENT_CLAIM.replace(" **[OPEN]**", "")
    ch = v6_claim_hash(child_claim).split(":")[-1]
    ph = v6_claim_hash(parent_claim).split(":")[-1]

    child_lean = (
        "formalization:\n"
        "  lean:\n"
        "    module: FIX.child\n"
        "    file: %s\n"
        "    claim: Claim\n"
        "    state: stated\n"
        "    rel: []\n"
        "    sync_state: current\n"
        "    claim_hash: sha256:%s\n"
    ) % ((lean / "child.lean").as_posix(), ch)

    parent_theorems = "    theorems: [composition]\n"
    parent_body = ("def Claim : Prop := True\n\n"
                   "theorem composition (h : FIX.child.Claim) : Claim := trivial\n")
    parent_imports = ["FIX.child"]
    parent_claim_body = parent_claim
    parent_hash_in_node = ph
    parent_hash_in_doc = ph
    parent_rel = ["fixture"]
    # a second route makes the fixture an OR node, so check 5 is exercised
    second_route = ""
    good_mechanism = ("enters as the cited interface field `Cited.fixture_field`, "
                      "which the fixture Interface declares")
    # 2026-08-17 (review item F4): a `premise-not-imported` premise must have NO
    # module.  The import-mismatch family models exactly that licensed case, so
    # FIX.child loses its formalization block there; the new
    # `v6_premise_not_imported_mechanized` fixture keeps it and must FAIL.
    child_mechanized = True
    child_routes = ""
    grand_lean = ""          # non-empty -> a third node FIX.grand is written

    if variant == "v6_major2_unbacked_state":
        parent_theorems = ""
        parent_body = "def Claim : Prop := True\n"
    elif variant == "v6_stale_hash":
        # the claim was edited on the node; `claim_hash` and the header digest
        # were both left intact, and the mirror still declares itself current
        parent_claim_body = parent_claim + " EDITED AFTER FREEZING."
    elif variant.startswith("v6_import_mismatch") or variant == "v6_relevance_notice":
        child_mechanized = False
        parent_imports = ["FIX.Interface"]
        parent_body = "def Claim : Prop := True\n\ntheorem composition : Claim := trivial\n"
        if variant in ("v6_import_mismatch_declared", "v6_relevance_notice"):
            parent_rel = ["premise-not-imported: FIX.child — " + good_mechanism]
        elif variant == "v6_import_mismatch_blanket":
            parent_rel = ["premise-not-imported: FIX.child — declared"]
        elif variant == "v6_import_mismatch_junk":
            # review item F1: 26 non-space characters, no words, no anchor
            parent_rel = ["premise-not-imported: FIX.child — " + "q" * 26]
        elif variant == "v6_import_mismatch_bogus_field":
            parent_rel = ["premise-not-imported: FIX.child — enters as the cited field "
                          "`Cited.no_such_field`, which does not exist anywhere"]
    elif variant == "v6_premise_not_imported_mechanized":
        # review item F4: the SAME declared mismatch, but the premise HAS a module.
        parent_imports = ["FIX.Interface"]
        parent_body = "def Claim : Prop := True\n\ntheorem composition : Claim := trivial\n"
        parent_rel = ["premise-not-imported: FIX.child — " + good_mechanism]
    elif variant.startswith("v6_import_not_child"):
        # review item F3: FIX.parent -> FIX.child -> FIX.grand, and the parent
        # imports the GRANDCHILD directly.  Licensed only while the skipped
        # intermediate FIX.child carries no `formalization` block.
        grand_claim = "A grandchild obligation. Fixture node."
        gh = v6_claim_hash(grand_claim).split(":")[-1]
        grand_lean = (
            "formalization:\n"
            "  lean:\n"
            "    module: FIX.grand\n"
            "    file: %s\n"
            "    claim: Claim\n"
            "    state: stated\n"
            "    rel: []\n"
            "    sync_state: current\n"
            "    claim_hash: sha256:%s\n"
        ) % ((lean / "grand.lean").as_posix(), gh)
        child_routes = (
            "routes:\n"
            "  down:\n"
            "    premises: [FIX.grand]\n"
            "    implication: The grandchild claim gives the child claim.\n"
            "    assessment:\n"
            "      level: OPEN\n"
            "      summary: fixture route assessment.\n"
        )
        inc_decl = ("import-not-child: FIX.grand — GRANDCHILD reached by skipping the "
                    "intermediate node `FIX.child`; `FIX.grand.Claim` is consumed directly "
                    "as a parameter of `composition`. Ruling R3 / deviation D2.")
        if variant == "v6_import_not_child_mechanized":
            parent_imports = ["FIX.child", "FIX.grand"]
            parent_body = ("def Claim : Prop := True\n\n"
                           "theorem composition (h : FIX.child.Claim) (g : FIX.grand.Claim) : "
                           "Claim := trivial\n")
            parent_rel = [inc_decl]
        else:                                   # v6_import_not_child_unmechanized
            child_mechanized = False
            parent_imports = ["FIX.grand"]
            parent_body = ("def Claim : Prop := True\n\n"
                           "theorem composition (g : FIX.grand.Claim) : Claim := trivial\n")
            parent_rel = [inc_decl,
                          "premise-not-imported: FIX.child — the node carries no "
                          "`formalization` block, so no module for it exists to import; the "
                          "obligation lives on the grandchild `FIX.grand`. Ruling R3."]
    elif variant == "v6_false_import_declaration":
        # the premise IS imported, yet the node declares that it is not
        parent_rel = ["premise-not-imported: FIX.child — " + good_mechanism]
    elif variant.startswith("v6_route"):
        parent_theorems = "    theorems: [composition_via_only]\n"
        parent_body = ("def Claim : Prop := True\n\n"
                       "theorem composition_via_only (h : FIX.child.Claim) : Claim := trivial\n")
        second_route = (
            "  alt:\n"
            "    premises: [FIX.child]\n"
            "    implication: An alternative way to the same parent claim.\n"
            "    assessment:\n"
            "      level: OPEN\n"
            "      summary: fixture alternative route, no argument yet.\n"
        )
        if variant == "v6_route_declared":
            parent_rel = ["route-not-formalized: alt — the route carries no `proof:` key on the "
                          "node, so rendering a `composition_via_*` theorem would invent "
                          "content. Ruling R5 / deviation D6."]
        elif variant == "v6_route_false_declaration":
            parent_rel = ["route-not-formalized: only — the route carries no `proof:` key on the "
                          "node, so rendering a `composition_via_*` theorem would invent "
                          "content. Ruling R5 / deviation D6."]
        elif variant == "v6_route_disabled":
            # the alternative requires a REFUTED premise: §4 disables it, so check 5
            # requires no `composition_via_alt` and no route declaration.  Check 6
            # is a DIFFERENT obligation and still wants to know how the disabled
            # route's premise reaches the module (here: it does not), so that one
            # entry is present -- exactly as `SE.goal` handles its `ros` route.
            second_route = second_route.replace("premises: [FIX.child]",
                                                "premises: [FIX.dead]")
            parent_rel = ["premise-not-imported: FIX.dead — premise of the §4-disabled route "
                          "`alt`; the node carries no formalization block, so no module for it "
                          "exists to import and nothing here assumes it"]

    parent_routes = (
        "routes:\n"
        "  only:\n"
        "    premises: [FIX.child]\n"
        "    implication: The child claim gives the parent claim.\n"
        "    assessment:\n"
        "      level: NUMERICAL\n"
        "      summary: fixture route assessment.\n"
        + second_route
    )
    parent_lean = (
        "formalization:\n"
        "  lean:\n"
        "    module: FIX.parent\n"
        "    file: %s\n"
        "    claim: Claim\n"
        "    state: composition-checked\n"
        "%s"
        "    rel: %s\n"
        "    sync_state: current\n"
        "    claim_hash: sha256:%s\n"
    ) % ((lean / "parent.lean").as_posix(), parent_theorems,
         json.dumps(parent_rel, ensure_ascii=False), parent_hash_in_node)

    (nodes / "FIX.child.yaml").write_text(
        _v6_node_yaml("FIX.child", child_claim, "PROVED", child_routes,
                      child_lean if child_mechanized else ""),
        encoding="utf-8")
    (nodes / "FIX.parent.yaml").write_text(
        _v6_node_yaml("FIX.parent", parent_claim_body, "OPEN", parent_routes, parent_lean),
        encoding="utf-8")
    if "FIX.dead" in parent_routes:
        (nodes / "FIX.dead.yaml").write_text(
            _v6_node_yaml("FIX.dead", "A refuted premise. No formal mirror.", "REFUTED", "", ""),
            encoding="utf-8")
    if grand_lean:
        (nodes / "FIX.grand.yaml").write_text(
            _v6_node_yaml("FIX.grand", grand_claim, "PROVED", "", grand_lean),
            encoding="utf-8")
        (lean / "grand.lean").write_text(
            _lean_module_v6("FIX.grand", "nodes/FIX.grand.yaml", grand_claim, gh,
                            "def Claim : Prop := True\n", []),
            encoding="utf-8")

    (lean / "Interface.lean").write_text(
        "/-! fixture interface -/\nstructure Cited : Prop where\n  fixture_field : True\n",
        encoding="utf-8")
    # the v6 fixtures use the SE/KSUM `/-` header style on purpose, so the
    # docstring locator is regression-tested on both comment forms
    if child_mechanized:
        (lean / "child.lean").write_text(
            _lean_module_v6("FIX.child", "nodes/FIX.child.yaml", child_claim, ch,
                            "def Claim : Prop := True\n", []),
            encoding="utf-8")
    (lean / "parent.lean").write_text(
        _lean_module_v6("FIX.parent", "nodes/FIX.parent.yaml", parent_claim, parent_hash_in_doc,
                        parent_body, parent_imports),
        encoding="utf-8")

    spec = ProblemSpec(nodes_dir="nodes", lean_dir="lean/FIX", module_prefix="FIX")
    return spec, root, nodes, lean


def _lean_module_v6(module, node_file, claim_text, digest, body, imports):
    imp = "".join("import %s\n" % i for i in imports)
    quoted = "\n".join("  " + line if line else "" for line in claim_text.split("\n"))
    return (
        "/-\n`%s` — NODE MODULE.\n\n"
        "node file      : %s\n"
        "claim_hash     : sha256:%s\n\n"
        "FROZEN CLAIM (verbatim from the node file):\n\n"
        "%s\n\n"
        "  (Indentation added only to nest the quote inside this comment.)\n-/\n\n"
        "%s\nnamespace %s\n\n"
        "%s\n"
        "end %s\n"
    ) % (module, node_file, digest, quoted, imp, module, body, module)


# Documentation-regression sentinels (2026-08-17, review items F2/F5/F6).  F2, F5
# and F6 are NOT mechanically decidable, so what the selftest can protect is the
# DISCLOSURE: deleting it from the docstring must break the selftest, exactly so
# that a later session cannot quietly rediscover the hole as a trick.
DOC_SENTINELS = {
    "F2": "* F2 RELEVANCE IS NEVER CHECKED.",
    "F5": "* F5 A `REFUTED` WRITE LEGITIMATELY SILENCES CHECK 5.",
    "F6": "It does NOT mean the Lean `Claim : Prop` expresses the",
}


def _has_info(rep, needle):
    return any(sev == "INFO" and needle in msg for sev, _, _, msg in rep.items)


def selftest(stream=sys.stdout):
    results = []
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        cases = [
            ("clean", None, "clean fixture must produce no FAIL and exit 0"),
            ("major2_unbacked_state", "7a",
             "`state: composition-checked` with no composition theorem must FAIL (MAJOR-2 class)"),
            ("stale_hash", "3", "edited Claim body with a stale hash must FAIL"),
            ("import_mismatch", "6", "import not matching `children` must FAIL"),
            ("v6_clean", None, "clean SCHEMA-V6 fixture must produce no FAIL and exit 0"),
            ("v6_major2_unbacked_state", "7a",
             "v6: `state: composition-checked` with `theorems:` absent must FAIL"),
            ("v6_stale_hash", "3", "v6: edited claim with an intact claim_hash must FAIL"),
            ("v6_import_mismatch", "6",
             "v6: import not matching the route premises must FAIL"),
            # --- the 2026-08-17 declaration channel (frontier task-006) -------
            ("v6_import_mismatch_declared", None,
             "v6: the SAME import mismatch, DECLARED per-premise in lean.rel, must NOT FAIL"),
            ("v6_import_mismatch_blanket", "rel",
             "v6: a declaration with no substantive mechanism must FAIL (no rubber stamps)"),
            ("v6_import_mismatch_bogus_field", "6",
             "v6: a declaration naming a `Cited.<field>` absent from Interface.lean must FAIL"),
            ("v6_false_import_declaration", "6",
             "v6: declaring a premise not-imported while the module DOES import it must FAIL"),
            ("v6_route_undeclared", "5",
             "v6: an unrendered ENABLED route with no declaration must FAIL"),
            ("v6_route_declared", None,
             "v6: the SAME unrendered route, DECLARED in lean.rel, must NOT FAIL"),
            ("v6_route_false_declaration", "5",
             "v6: declaring a route not-formalized while its theorem EXISTS must FAIL"),
            ("v6_route_disabled", None,
             "v6: a route disabled by a REFUTED premise (§4) needs no theorem and no declaration"),
            # --- the 2026-08-17 hardening (frontier task-011, review F1-F6) ----
            ("v6_import_mismatch_junk", "rel",
             "F1: a 26-character mechanism with no words and no anchor must FAIL "
             "(the pure length gate is gone)"),
            ("v6_relevance_notice",
             lambda rep: rep.n_fail == 0 and _has_info(rep, "never that it is RELEVANT")
             and DOC_SENTINELS["F2"] in (__doc__ or ""),
             "F2: relevance is undecidable here, so a run carrying declarations must PRINT "
             "the residual risk and the docstring must keep the disclosure"),
            ("v6_import_not_child_mechanized", "6",
             "F3: a non-child import reached ACROSS a MECHANIZED intermediate must FAIL"),
            ("v6_import_not_child_unmechanized", None,
             "F3 control: the SAME non-child import across an UNMECHANIZED intermediate is "
             "still licensed and must NOT FAIL"),
            ("v6_premise_not_imported_mechanized", "6",
             "F4: declaring a premise not-imported while it CARRIES a formalization block "
             "must FAIL"),
            ("doc_refuted_silences_check5", DOC_SENTINELS["F5"],
             "F5: the docstring must keep naming the §4 REFUTED-route exemption as a "
             "legitimate silencer of check 5"),
            ("v6_sync_state_notice",
             lambda rep: rep.n_fail == 0
             and _has_info(rep, "It does NOT assert that the Lean `Claim : Prop`")
             and DOC_SENTINELS["F6"] in (__doc__ or ""),
             "F6: every run reporting `sync_state` must say it is about quoted TEXT and "
             "DIGESTS only, in the output and in the docstring"),
        ]
        for variant, want_check, desc in cases:
            if variant.startswith("doc_"):
                # documentation regression: no fixture tree, the artifact IS the text
                ok = want_check in (__doc__ or "")
                results.append((variant, ok, desc, None))
                stream.write("=== selftest fixture: %s ===\n" % variant)
                stream.write("documentation regression; sentinel %r %s in the module "
                             "docstring\n" % (want_check, "FOUND" if ok else "MISSING"))
                stream.write("assertion: %s -> %s\n\n" % (desc, "PASS" if ok else "FAIL"))
                continue
            builder = build_v6_fixture if variant.startswith("v6_") else build_fixture
            spec, root, nodes, lean = builder(base, variant)
            rep = Report()
            run_checks(spec, root, rep, nodes_dir=nodes, lean_dir=lean)
            if want_check is None:
                ok = rep.n_fail == 0
            elif callable(want_check):
                ok = bool(want_check(rep))
            else:
                ok = bool(rep.fails_for(want_check))
            results.append((variant, ok, desc, rep))
            stream.write("=== selftest fixture: %s ===\n" % variant)
            stream.write(rep.render() + "\n")
            stream.write("assertion: %s -> %s\n\n" % (desc, "PASS" if ok else "FAIL"))
    n_ok = sum(1 for _, ok, _, _ in results if ok)
    stream.write("SELFTEST: %d/%d assertions passed\n" % (n_ok, len(results)))
    return 0 if n_ok == len(results) else 1


# ---------------------------------------------------------------------------

def main(argv=None):
    try:                      # §/« » must survive a cp1252/gbk console and log redirect
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--problem", help="registered problem slug (only enabled ones run)")
    ap.add_argument("--selftest", action="store_true",
                    help="run the synthetic regression fixtures and exit")
    ap.add_argument("--nodes-dir", help="override the nodes directory (e.g. a patched copy)")
    ap.add_argument("--lean-dir", help="override the lean module directory")
    ap.add_argument("--root", default=str(REPO), help="repository root")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    if not args.problem:
        ap.error("either --problem or --selftest is required")
    spec = REGISTRY.get(args.problem)
    if spec is None:
        print("unknown problem %r; registered: %s"
              % (args.problem, ", ".join(sorted(REGISTRY))))
        return 2
    if not spec.enabled and not (args.nodes_dir and args.lean_dir):
        print("problem %r is registered but NOT enabled in this checker.\n"
              "Run it explicitly with:\n"
              "  python tools/lean_dag_check.py --problem %s --nodes-dir %s --lean-dir %s"
              % (args.problem, args.problem, spec.nodes_dir, spec.lean_dir))
        return 2

    rep = Report()
    run_checks(spec, Path(args.root), rep,
               nodes_dir=args.nodes_dir, lean_dir=args.lean_dir)
    print("lean_dag_check.py -- DAG_PROTOCOL.md §7 (pre-v6 §7.6) anti-drift checks")
    print("problem: %s" % args.problem)
    print("nodes:   %s" % (args.nodes_dir or spec.nodes_dir))
    print("lean:    %s" % (args.lean_dir or spec.lean_dir))
    print("schema:  %s" % ", ".join(sorted(k.split(":", 1)[1] for k in rep.stats
                                           if k.startswith("schema:")) or ["(none)"]))
    print("")
    print(rep.render())
    return 1 if rep.n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
