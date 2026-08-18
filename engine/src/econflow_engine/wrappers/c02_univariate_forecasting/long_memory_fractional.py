# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``long_memory_fractional`` -- METHOD-SELECTION card #136.

#136 Long memory / fractional integration ARFIMA(p,d,q) (ML fit + GPH/Sperio semiparametric d +
    fractional differencing)

Category 02-univariate-forecasting; module ``long_memory_fractional``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c02_univariate_forecasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fdf_diffseries",
    "fdf_fit",
    "fdf_gph",
    "fdf_sperio",
    "NODE_META",
    "wire_model",
]


def fdf_fit(
    *,
    x: pd.Series,
    nar: int | None = None,
    nma: int | None = None,
    M: int | None = None,
) -> dict[str, Any]:
    """Node ``fdf_fit`` -- METHOD-SELECTION card #136.

    Long memory / fractional integration ARFIMA(p,d,q) (ML fit + GPH/Sperio semiparametric d +
    fractional differencing).

    Category 02-univariate-forecasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        x: [series_handle, required] Handle to a univariate ts/numeric (the series for the ARFIMA
            fit).
        nar: [integer, optional] Number of AR parameters p (non-negative integer; default 0).
        nma: [integer, optional] Number of MA parameters q (non-negative integer; default 0).
        M: [integer, optional] Terms in the likelihood approximation (Haslett-Raftery; default 100).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fdf_fit: not implemented. The method card is in ./README.md."
    )


def fdf_gph(
    *,
    x: pd.Series,
    bandw_exp: float | None = None,
) -> dict[str, Any]:
    """Node ``fdf_gph`` -- METHOD-SELECTION card #136.

    Long memory / fractional integration ARFIMA(p,d,q) (ML fit + GPH/Sperio semiparametric d +
    fractional differencing).

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts/numeric.
        bandw_exp: [number, optional] Bandwidth exponent bw=trunc(n^bandw.exp); strictly in (0,1);
            default 0.5.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fdf_gph: not implemented. The method card is in ./README.md."
    )


def fdf_sperio(
    *,
    x: pd.Series,
    bandw_exp: float | None = None,
    beta: float | None = None,
) -> dict[str, Any]:
    """Node ``fdf_sperio`` -- METHOD-SELECTION card #136.

    Long memory / fractional integration ARFIMA(p,d,q) (ML fit + GPH/Sperio semiparametric d +
    fractional differencing).

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts/numeric.
        bandw_exp: [number, optional] Bandwidth exponent; strictly in (0,1); default 0.5.
        beta: [number, optional] Bandwidth exponent of the Parzen lag window; strictly in (0,1);
            default 0.9.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fdf_sperio: not implemented. The method card is in ./README.md."
    )


def fdf_diffseries(
    *,
    x: pd.Series,
    d: float,
) -> dict[str, Any]:
    """Node ``fdf_diffseries`` -- METHOD-SELECTION card #136.

    Long memory / fractional integration ARFIMA(p,d,q) (ML fit + GPH/Sperio semiparametric d +
    fractional differencing).

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts/numeric.
        d: [number, required] Fractional differencing order (a single finite number).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fdf_diffseries: not implemented. The method card is in ./README.md."
    )
