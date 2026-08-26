# SPDX-License-Identifier: AGPL-3.0-only
"""The naming rules that turn contract identifiers into Python ones.

ONE implementation, used by both generators and by the runtime adapter. Two
independent copies of these rules would drift, and a drifted argument name is a
silent 422 (or worse, a silently dropped argument).

WHY IT IS NEEDED AT ALL -- measured against the artifact, not assumed:

* dotted contract names were folded to snake_case in the contract itself. A dot
  is not legal in a Python parameter name, so a name such as ``conf_level`` or
  ``n_ahead`` is the only form a signature can carry.
* 101 arguments are named with a Python keyword. ``class``, ``from`` and
  ``lambda`` are HARD keywords and cannot be parameter names at all (``case``
  and ``type`` are soft keywords and are left alone).

THE WIRE NAME NEVER CHANGES. Only the Python-side parameter is renamed, and the
translation happens at exactly one place -- the adapter that calls a wrapper.
Verified over all 913 nodes: the rule produces ZERO collisions within any node.
"""

from __future__ import annotations

import keyword
import re

__all__ = ["category_package", "python_arg_name", "wrapper_module_name"]

# re.ASCII is load-bearing: on a str pattern a bare ``\W`` is Unicode-aware, and
# an accented letter would then survive into the identifier instead of folding.
_NON_IDENT = re.compile(r"\W+", re.ASCII)


def python_arg_name(wire_name: str) -> str:
    """``p.adjust.method`` -> ``p_adjust_method``; ``class`` -> ``class_``."""
    name = _NON_IDENT.sub("_", wire_name)
    if not name or name[0].isdigit():
        name = f"_{name}"
    if keyword.iskeyword(name):
        name = f"{name}_"
    return name


def category_package(category: str) -> str:
    """``00-data-utilities`` -> ``c00_data_utilities``.

    The ``c`` prefix exists because every category starts with its two-digit
    order number, and a Python identifier may not start with a digit.
    """
    return "c" + _NON_IDENT.sub("_", category.lower())


def wrapper_module_name(wrapper_file: str) -> str:
    """``c01_preparation_prechecks/auto_orders.py`` -> ``auto_orders``.

    The basename, minus ``.py``, non-alphanumerics folded to ``_``, lowercased.
    Verified over all 598 modules: every result is a valid identifier and no two
    collide inside a category.
    """
    base = wrapper_file.rsplit("/", 1)[-1]
    if not base.endswith(".py"):
        raise ValueError(f"wrapper_module_name: {wrapper_file!r} does not end in '.py'.")
    return _NON_IDENT.sub("_", base[: -len(".py")]).lower()
