# SPDX-License-Identifier: AGPL-3.0-only
"""PLANTED CONTROLS. Every harness in this package proves itself on these.

WHY THIS PACKAGE EXISTS. Boxes 2.1.4, 2.1.13, 2.1.14, 2.1.16, 2.1.17 and 2.1.18
are all written against implemented wrapper bodies, and ``.github/inventory.json``
records ``engine.n_implemented = 0``: all 1456 wrapper functions are typed stubs
that raise. Run as written, every one of those harnesses would report success
while examining nothing -- which is the exact failure this repository has hit six
times, and the reason ARCHITECTURE.md 11.1 exists.

So each harness carries the same three-part guard that
``.github/scripts/check-no-network.sh`` established, and that script is the
reference implementation:

  1. a FLOOR read from ``.github/inventory.json``, so weakening it is a visible
     one-line diff in the manifest rather than an edit buried in a script;
  2. POSITIVE controls -- input the harness MUST reject on every run. If a
     positive control goes unflagged, the harness has a hole and says so;
  3. NEGATIVE controls -- input the harness MUST accept. If one is flagged, the
     rule has decayed into a stricter one that fires on legitimate code.

THE CONTROLS ARE THE PROOF TODAY, AND THE FLOORS ARE THE PROOF LATER. Each
wrapper-facing floor reads ``engine.n_implemented``, so it is satisfied by zero
today and rises on its own with the first body written in 2.2 -- no second edit,
and no chance of a harness quietly continuing to examine nothing after the
catalogue starts computing.

A CONTROL IS KEPT ON DISK SO THE WALK IS EXERCISED AS WELL AS THE RULE. A control
written as a string inside its own test proves the RULE works. A control written
as a FILE also proves the WALK works -- that the checker reads files off disk,
parses them and reaches the finding. Both halves have failed separately in this
repository, so both are exercised.

NOTHING HERE IS COLLECTED BY PYTEST. No module is named ``test_*``; the harnesses
import these deliberately, and the file-shaped controls exist to be read as text.

THIS PACKAGE IS NEVER IMPORTED BY THE ENGINE. It lives under ``tests/`` and not
under ``src/econflow_engine/wrappers/`` deliberately: a module in the wrapper
tree breaks ``gen_wrappers --check``, ``api-baseline/check_api.py``,
``interrogate`` and the exact-equality constant ``engine.wrappers = 598``, all at
once.
"""

from __future__ import annotations
