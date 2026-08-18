# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``numeric_rescaling_axis`` -- METHOD-SELECTION card #120.

#120 Numeric rescaling (min-max / around-mid) + axis break positions (extended/log) + label strings
    (number/percent)

Category 00-data-utilities; module ``numeric_rescaling_axis``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "scale_breaks",
    "scale_labels",
    "scale_rescale",
    "scale_rescale_mid",
    "NODE_META",
    "wire_model",
]


def scale_rescale(
    *,
    x: pd.Series,
    to: Sequence[float] | None = None,
    from_: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``scale_rescale`` -- METHOD-SELECTION card #120.

    Numeric rescaling (min-max / around-mid) + axis break positions (extended/log) + label strings
    (number/percent).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a numeric series for linear (min-max) rescaling.
        to: [num_array, optional] Target range [min,max] — numeric of EXACTLY length 2 (default
            [0,1]). Default ``[0, 1]``.
        from_ (wire name ``from``): [num_array, optional] Source range [min,max]; None => range(x,
            the NA policy=True, finite=True).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "scale_rescale: not implemented. The method card is in ./README.md."
    )


def scale_rescale_mid(
    *,
    x: pd.Series,
    mid: float | None = None,
    to: Sequence[float] | None = None,
    from_: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``scale_rescale_mid`` -- METHOD-SELECTION card #120.

    Numeric rescaling (min-max / around-mid) + axis break positions (extended/log) + label strings
    (number/percent).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a numeric series (diverging around mid).
        mid: [number, optional] Value mapped to the center mean(to); a finite number (default 0).
            Default ``0``.
        to: [num_array, optional] Target range [min,max] — numeric of length 2 (default [0,1]).
            Default ``[0, 1]``.
        from_ (wire name ``from``): [num_array, optional] Source range [min,max]; None => range(x,
            the NA policy=True).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "scale_rescale_mid: not implemented. The method card is in ./README.md."
    )


def scale_breaks(
    *,
    x: pd.Series,
    n: int | None = None,
    type: Literal["extended", "log"] | None = None,
    base: float | None = None,
) -> dict[str, Any]:
    """Node ``scale_breaks`` -- METHOD-SELECTION card #120.

    Numeric rescaling (min-max / around-mid) + axis break positions (extended/log) + label strings
    (number/percent).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to numeric data/range; computes axis break positions AS
            DATA.
        n: [integer, optional] Desired number of breaks — integer >= 1 (default 5; it is a TARGET,
            not exact). Default ``5``.
        type: [enum, optional] extended=Wilkinson linear, log=logarithmic. Default extended.
        base: [number, optional] Logarithm base (only type='log'); > 1 (default 10). type='log'
            requires positive values. Default ``10``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "scale_breaks: not implemented. The method card is in ./README.md."
    )


def scale_labels(
    *,
    x: pd.Series,
    type: Literal["number", "percent"] | None = None,
    accuracy: float | None = None,
    big_mark: str | None = None,
) -> dict[str, Any]:
    """Node ``scale_labels`` -- METHOD-SELECTION card #120.

    Numeric rescaling (min-max / around-mid) + axis break positions (extended/log) + label strings
    (number/percent).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to numeric values to be formatted as label strings.
        type: [enum, optional] number=plain number, percent=x100 + '%'. Default number.
        accuracy: [number, optional] Rounding unit (e.g. 0.01); positive or None => auto.
        big_mark: [string, optional] Thousands separator (e.g. ','); string of length 1; '' => none.
            Default ``''``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "scale_labels: not implemented. The method card is in ./README.md."
    )
