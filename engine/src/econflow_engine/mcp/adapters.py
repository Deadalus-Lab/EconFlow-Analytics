# SPDX-License-Identifier: AGPL-3.0-only
"""Input adapters.

They turn a VALIDATED wire body into the real Python objects a wrapper expects,
before it is called.

THE SPLIT THE PREVIOUS DESIGN DID NOT HAVE. There, one step both validated and coerced,
because the engine has no schema layer. Here validation belongs to
:mod:`econflow_engine.kinds` (strict pydantic models mirroring ``.mcp_coerce_one``
one branch at a time) and this module does only the second half: MATERIALISATION.
That is why every reason code the parity corpus knows is produced by ``kinds``
and none by this file.

WHAT MATERIALISATION MEANS PER KIND -- the contract the wrapper signatures were
generated against:

    series_handle, irregular_series_handle          -> pandas.Series
    multiseries_handle, df_handle          -> pandas.DataFrame
    matrix_handle, exog_handle            -> numpy.ndarray
    raw_handle                     -> the stored object, untouched
    raw_handle_array               -> a list of stored objects, IN EDGE ORDER
    everything else                -> passed through unchanged

The contract names several time-series handle kinds; pandas has one Series and
one DataFrame, so the table above is the whole of it.

DEFAULTS ARE APPLIED RAW. A declared default is assigned directly while every
explicit value goes through coercion, and that asymmetry is deliberate rather
than an oversight: the wire model refuses to carry defaults for precisely this
reason, and if the two sides disagreed about what an omitted argument means, a
stored graph would compute
something different from the graph the user built.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from econflow_engine.errors import GateError
from econflow_engine.kinds import NodeArgMeta, NodeMeta
from econflow_engine.mcp.registry import HandleError, registry_get
from econflow_engine.naming import python_arg_name
from econflow_engine.node.store_pointers import HANDLE_STRING_RE

__all__ = ["adapt_args", "resolve_handle", "to_dataframe", "to_matrix", "to_series"]


def to_series(value: Any) -> pd.Series:
    """Coerce a stored object to a Series -- the single time-series shape."""
    if isinstance(value, pd.Series):
        return value
    if isinstance(value, pd.DataFrame):
        if value.shape[1] != 1:
            raise GateError(
                "handle-not-string",
                f"resolve_handle(ts): the frame has {value.shape[1]} columns; a univariate "
                "socket takes exactly one.",
            )
        return value.iloc[:, 0]
    array = np.asarray(value)
    if array.ndim == 1 and np.issubdtype(array.dtype, np.number):
        return pd.Series(array)
    raise GateError("handle-not-string", "resolve_handle(ts): cannot read as a univariate series.")


def to_dataframe(value: Any) -> pd.DataFrame:
    if isinstance(value, pd.DataFrame):
        return value
    if isinstance(value, pd.Series):
        return value.to_frame()
    array = np.asarray(value)
    if array.ndim == 2:
        return pd.DataFrame(array)
    if array.ndim == 1:
        return pd.DataFrame({"value": array})
    raise GateError("handle-not-string", "resolve_handle(df): cannot read as a data frame.")


def to_matrix(value: Any) -> np.ndarray:
    if isinstance(value, np.ndarray):
        return value if value.ndim == 2 else value.reshape(-1, 1)
    if isinstance(value, pd.DataFrame):
        numeric = value.select_dtypes(include="number")
        if numeric.shape[1] == 0:
            raise GateError(
                "handle-not-string", "resolve_handle(matrix): the frame has no numeric columns."
            )
        return numeric.to_numpy()
    if isinstance(value, pd.Series):
        return value.to_numpy().reshape(-1, 1)
    array = np.asarray(value)
    if np.issubdtype(array.dtype, np.number):
        return array if array.ndim == 2 else array.reshape(-1, 1)
    raise GateError("handle-not-string", "resolve_handle(matrix): cannot read as a matrix.")


_AS_KIND = {
    "series_handle": to_series,
    "irregular_series_handle": to_series,
    "multiseries_handle": to_dataframe,
    "df_handle": to_dataframe,
    "matrix_handle": to_matrix,
    "exog_handle": to_matrix,
}


def resolve_handle(handle: object, kind: str, fetch_pointer: Any = None) -> Any:
    """Turn a wire handle into the object the wrapper expects.

    A registry handle is looked up in the session store. A store pointer (an
    object, or a bare ``store://`` uri) needs the data plane, which this pure
    module does not own -- the caller injects ``fetch_pointer``. Without it a
    pointer raises rather than being silently treated as a missing input.
    """
    if isinstance(handle, str) and HANDLE_STRING_RE.match(handle) is not None:
        value = registry_get(handle)
    else:
        if fetch_pointer is None:
            raise GateError(
                "handle-not-string",
                "resolve_handle: a store pointer needs a data-plane reader; none was "
                "supplied to this call.",
            )
        value = fetch_pointer(handle)
    converter = _AS_KIND.get(kind)
    return value if converter is None else converter(value)


def _materialise(value: Any, arg: NodeArgMeta, fetch_pointer: Any) -> Any:
    if arg.kind == "raw_handle_array":
        # ORDER IS MEANING: the edge order is the asset order, and the columns of
        # the data supplied later must line up with it.
        return [resolve_handle(item, "raw_handle", fetch_pointer) for item in value]
    if arg.kind in _AS_KIND or arg.kind == "raw_handle":
        return resolve_handle(value, arg.kind, fetch_pointer)
    return value


def adapt_args(
    meta: NodeMeta, body: dict[str, Any], fetch_pointer: Any = None
) -> dict[str, Any]:
    """Project a VALIDATED wire body onto wrapper keyword arguments.

    Two things happen, and only these two: handles become objects, and wire
    argument names become Python parameter names. Validation already happened; if an
    unknown key reaches here it is a programming error in the caller, not a user
    error, so it raises rather than producing a 422 reason code.
    """
    by_name = {a.name: a for a in meta.args}
    unknown = sorted(set(body) - set(by_name))
    if unknown:
        raise GateError(
            "unknown-args",
            f"adapt_args({meta.fn}): unknown argument(s) {', '.join(unknown)} reached the "
            "adapter; the wire model should have refused them first.",
        )
    out: dict[str, Any] = {}
    for arg in meta.args:
        if arg.name not in body or body[arg.name] is None:
            if arg.required:
                raise GateError(
                    "missing-required", f"Missing required argument '{arg.name}'."
                )
            if arg.name in meta.defaults:
                out[python_arg_name(arg.name)] = meta.defaults[arg.name]
            continue
        try:
            value = _materialise(body[arg.name], arg, fetch_pointer)
        except HandleError as exc:
            raise GateError("handle-not-string", str(exc)) from exc
        out[python_arg_name(arg.name)] = value
    return out
