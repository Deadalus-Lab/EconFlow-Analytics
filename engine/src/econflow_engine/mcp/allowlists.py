# SPDX-License-Identifier: AGPL-3.0-only
"""Closed vocabularies, read from the artifact -- never hard-coded here.

Every name in this module comes from the ``vocabulary`` block of
``artifacts/node-specs.json``, the sealed contract, which the
generated tier copies verbatim. Re-typing any of these lists by hand would create
a second source of truth that drifts silently the moment the engine adds a kind
or a forecast function.

``forecastfn_names`` is a SECURITY allowlist: the alternative to a closed enum is
``eval(parse(text =...))`` on client input, i.e. remote code execution. Same for
``formula.allowed_calls`` -- see :mod:`econflow_engine.formula`.
"""

from __future__ import annotations

from typing import Final

try:
 from econflow_engine.generated.manifest import VOCABULARY
except ModuleNotFoundError as exc: # pragma: no cover - build-order guard
 raise ModuleNotFoundError(
 "econflow_engine.generated is missing. It is emitted from the committed "
 "artifact and is gitignored on purpose. Run: python scripts/gen_schemas.py"
 ) from exc

__all__ = [
 "EXPORT_FORMATS",
 "FORECASTFN_NAMES",
 "FORMULA_ALLOWED_CALLS",
 "FORMULA_MAX_DEPTH",
 "MAX_POINTER_ARRAY",
 "MEMORY_CLASSES",
 "NODE_ARG_KINDS",
 "POINTER_FORMATS",
 "POINTER_HANDLE_KINDS",
 "SCALAR_POINTER_HANDLE_KINDS",
 "STOCHASTIC_UNSEEDED_FNS",
 "is_array_pointer_handle_kind",
 "is_pointer_handle_kind",
 "is_scalar_pointer_handle_kind",
]

NODE_ARG_KINDS: Final[tuple[str,...]] = tuple(VOCABULARY["kinds"])
POINTER_HANDLE_KINDS: Final[tuple[str,...]] = tuple(VOCABULARY["pointer_handle_kinds"])
FORECASTFN_NAMES: Final[tuple[str,...]] = tuple(VOCABULARY["forecastfn_names"])
FORMULA_ALLOWED_CALLS: Final[tuple[str,...]] = tuple(VOCABULARY["formula"]["allowed_calls"])
FORMULA_MAX_DEPTH: Final[int] = int(VOCABULARY["formula"]["max_depth"])
POINTER_FORMATS: Final[tuple[str,...]] = tuple(VOCABULARY["pointer_formats"])
EXPORT_FORMATS: Final[tuple[str,...]] = tuple(VOCABULARY["export_formats"])
MEMORY_CLASSES: Final[tuple[str,...]] = tuple(VOCABULARY["memory_classes"])
STOCHASTIC_UNSEEDED_FNS: Final[frozenset[str]] = frozenset(VOCABULARY["stochastic_unseeded_fns"])

#: The only ARRAY-shaped handle socket in the vocabulary. Kept as a derived set
#: rather than a literal so that a second array kind is picked up automatically.
ARRAY_POINTER_HANDLE_KINDS: Final[tuple[str,...]] = tuple(
 k for k in POINTER_HANDLE_KINDS if k.endswith("_array")
)
SCALAR_POINTER_HANDLE_KINDS: Final[tuple[str,...]] = tuple(
 k for k in POINTER_HANDLE_KINDS if k not in ARRAY_POINTER_HANDLE_KINDS
)

#: Upper bound on the assets an array-handle socket may carry.
MAX_POINTER_ARRAY: Final[int] = 64

_POINTER_SET: Final[frozenset[str]] = frozenset(POINTER_HANDLE_KINDS)
_ARRAY_SET: Final[frozenset[str]] = frozenset(ARRAY_POINTER_HANDLE_KINDS)


def is_pointer_handle_kind(kind: str) -> bool:
 """True for every kind whose wire value is a store pointer or a registry handle."""
 return kind in _POINTER_SET


def is_scalar_pointer_handle_kind(kind: str) -> bool:
 """True for a handle socket that takes exactly ONE pointer."""
 return kind in _POINTER_SET and kind not in _ARRAY_SET


def is_array_pointer_handle_kind(kind: str) -> bool:
 """True for a handle socket that takes an ORDERED ARRAY of pointers."""
 return kind in _ARRAY_SET
