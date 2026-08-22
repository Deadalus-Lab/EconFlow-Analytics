#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
#
# check-no-network.sh -- no wrapper reaches the network, and this re-measures it.
#
# WHAT IT ENFORCES. A wrapper computes from what it was handed. It does not open a
# socket, fetch a URL or resolve a host. That is what makes a result reproducible
# from its inputs alone, what keeps a run auditable, and what lets the engine be
# executed in a sandbox with no egress at all. The single deliberate exception is
# the external-data node, which lives OUTSIDE the wrapper set precisely so that
# this rule can stay absolute here.
#
# WHY IT EXISTS, MEASURED. Until 2026-08-21 this claim was published in five
# places -- ARCHITECTURE.md called it "Verified" -- and NOTHING re-measured it.
# `grep -c network engine/run_verifications.sh` returned zero. The figure quoted
# was "0 of 251", taken by hand when the tree held 251 wrapper modules; it holds
# 598. The claim was still true, because every body is a stub, but its denominator
# named a tree that no longer existed and no gate would have noticed the day a
# body landed with `requests.get` in it. A claim without a gate is a memory.
#
# IT PARSES, IT DOES NOT GREP. A regular expression over source finds the word
# "socket" in a comment and misses a transport reached any other way. This walks the
# abstract syntax tree, so it sees imports and calls as the parser sees them, and
# a mention inside a docstring or a string literal is correctly ignored -- the
# wrapper prose legitimately discusses network access when explaining why a method
# does not do it.
#
# WHAT COUNTS AS REACHING THE NETWORK: importing a transport module, or calling
# one of its entry points. The list is the standard library's transports plus the
# third-party clients this project's dependency set could pull in. It is
# deliberately short and deliberately explicit: a name not on it is not caught,
# and the honest way to widen it is to add the name here where a reviewer sees it.
#
# THREE ANTI-VACUITY GUARDS:
#   1. a floor from .github/inventory.json -- fewer modules parsed than the floor
#      means the walk broke, not that the tree is clean
#   2. a POSITIVE control: synthetic source that MUST be flagged on every run
#   3. a NEGATIVE control: source that merely NAMES the network in a docstring and
#      a string, which must NOT be flagged, so the rule cannot decay into one that
#      fires on prose
#
#   usage: check-no-network.sh [repo-root]
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

MANIFEST=".github/inventory.json"
[ -f "$MANIFEST" ] || { echo "FAIL: no manifest at $MANIFEST" >&2; exit 2; }

python3 - "$MANIFEST" <<'PY'
import ast
import json
import pathlib
import sys

manifest_path = sys.argv[1]
WRAPPERS = pathlib.Path("engine/src/econflow_engine/wrappers")

# Transport modules. Importing one from a wrapper is the finding.
MODULES = {
    "socket", "ssl", "http", "http.client", "urllib", "urllib.request",
    "urllib3", "ftplib", "telnetlib", "smtplib", "poplib", "imaplib",
    "xmlrpc", "xmlrpc.client", "asyncio.streams", "requests", "httpx",
    "aiohttp", "websockets", "paramiko", "boto3", "botocore", "pycurl",
}
# Entry points. Calling one is the finding even if the import was indirect.
CALLS = {
    "urlopen", "urlretrieve", "socket", "create_connection", "getaddrinfo",
    "get", "post", "put", "patch", "delete", "head", "request", "Session",
    "ClientSession", "connect",
}
# `get`/`post`/... are far too common to flag alone; they count only when the
# receiver is one of these. `df.get(...)` is not a network call.
RECEIVERS = {"requests", "httpx", "session", "client", "aiohttp", "urllib", "urllib3"}


def findings(tree: ast.Module) -> list[str]:
    out: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                if alias.name in MODULES or root in MODULES:
                    out.append(f"line {node.lineno}: import {alias.name}")
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if mod in MODULES or mod.split(".")[0] in MODULES:
                out.append(f"line {node.lineno}: from {mod} import ...")
        elif isinstance(node, ast.Call):
            fn = node.func
            # A DYNAMIC IMPORT IS ITSELF THE FINDING, whatever it names. This gate
            # can only be enforced by reading the source, and `__import__(x)` or
            # `importlib.import_module(x)` defeats exactly that: the name may be
            # computed, so no static walk can tell what is being loaded. A wrapper
            # has no legitimate use for one. The first version of this gate walked
            # imports and calls and let `__import__('httpx')` straight through --
            # found by a planted probe, not by review.
            if isinstance(fn, ast.Name) and fn.id == "__import__":
                out.append(f"line {node.lineno}: __import__(...) -- a dynamic import "
                           "cannot be checked and is not permitted in a wrapper")
                continue
            if isinstance(fn, ast.Attribute) and fn.attr == "import_module":
                out.append(f"line {node.lineno}: import_module(...) -- a dynamic import "
                           "cannot be checked and is not permitted in a wrapper")
                continue
            if isinstance(fn, ast.Name) and fn.id in CALLS and fn.id not in {
                "get", "post", "put", "patch", "delete", "head", "request"
            }:
                out.append(f"line {node.lineno}: {fn.id}(...)")
            elif isinstance(fn, ast.Attribute) and fn.attr in CALLS:
                base = fn.value
                name = base.id.lower() if isinstance(base, ast.Name) else ""
                if name in RECEIVERS:
                    out.append(f"line {node.lineno}: {name}.{fn.attr}(...)")
    return out


if not WRAPPERS.is_dir():
    sys.exit(f"FAIL: no wrapper tree at {WRAPPERS}; this gate cannot start.")

parsed = 0
offenders: list[tuple[str, list[str]]] = []
for path in sorted(WRAPPERS.rglob("*.py")):
    if path.name == "__init__.py":
        continue
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except SyntaxError as exc:
        sys.exit(f"FAIL: {path} does not parse ({exc}); the gate refuses to guess.")
    parsed += 1
    hits = findings(tree)
    if hits:
        offenders.append((str(path), hits))

# --- anti-vacuity 1: the floor -------------------------------------------
floor = int(json.loads(pathlib.Path(manifest_path).read_text())
            .get("engine", {}).get("wrappers", 0))
if floor <= 0:
    sys.exit("FAIL: no engine.wrappers in the manifest; a floor of zero is not a floor.")
if parsed < floor:
    sys.exit(f"FAIL: parsed {parsed} wrapper module(s), below the floor {floor}. "
             "The walk is wrong, not the tree.")

# --- anti-vacuity 2: the positive control --------------------------------
POSITIVES = {
    "a plain import":   "import requests\ndef f():\n    return requests.get('http://x')\n",
    "a from-import":    "from urllib.request import urlopen\n",
    "a dynamic import": "def f():\n    return __import__('httpx')\n",
    "importlib":        "import importlib\ndef f():\n    return importlib.import_module('socket')\n",
}
for name, src in POSITIVES.items():
    if not findings(ast.parse(src)):
        sys.exit(f"FAIL: the positive control '{name}' was NOT flagged; this gate has a hole.")

# --- anti-vacuity 3: the negative control --------------------------------
# Prose that DISCUSSES the network, and ordinary calls that merely share a name.
NEGATIVE = (
    '"""This method makes no network call; it never opens a socket or fetches a URL."""\n'
    "def f(df, cfg):\n"
    "    note = 'requests are not made here'\n"
    "    return df.get('col'), cfg.get('key'), note\n"
)
flagged = findings(ast.parse(NEGATIVE))
if flagged:
    sys.exit(f"FAIL: the negative control was flagged on {flagged}; the rule now fires "
             "on prose and on ordinary attribute access.")

if offenders:
    for rel, hits in offenders:
        print(f"NETWORK  {rel}")
        for h in hits[:5]:
            print(f"    {h}")
    total = sum(len(h) for _, h in offenders)
    print()
    print(f"FAIL: {total} network access(es) in {len(offenders)} wrapper module(s), "
          f"parsed {parsed}.", file=sys.stderr)
    print("A wrapper computes from what it was handed. Fetching belongs to the "
          "external-data node, which lives outside the wrapper set so that this rule "
          "can stay absolute here.", file=sys.stderr)
    sys.exit(1)

print(f"ok: 0 of {parsed} wrapper modules reach the network "
      f"(floor {floor}, all controls fired).")
PY
