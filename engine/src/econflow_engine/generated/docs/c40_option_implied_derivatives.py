# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 40-option-implied-derivatives: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'opt_price': {
        'fn': 'opt_price',
        'description': 'opt_price -- category 40-option-implied-derivatives, method card #340.',
        'args': {'spot': 'Spot price of the underlying.', 'strike': 'Strike price.', 'time_to_expiry': 'Time to expiry in years.', 'rate': 'Risk-free rate.', 'volatility': 'Volatility input.', 'option_type': 'Option type.', 'model': 'Pricing model.', 'dividend': 'Continuous dividend yield.'},
        'input_example': {'spot': 1.0, 'strike': 1.0, 'time_to_expiry': 1.0, 'rate': 1.0, 'volatility': 1.0, 'option_type': 'call', 'model': 'black_scholes', 'dividend': 0.0},
    },
    'opt_implied_volatility': {
        'fn': 'opt_implied_volatility',
        'description': 'opt_implied_volatility -- category 40-option-implied-derivatives, method card #340.',
        'args': {'price': 'Observed option prices.', 'spot': 'Spot prices.', 'strike': 'Strikes.', 'time_to_expiry': 'Times to expiry in years.', 'rate': 'Risk-free rates.', 'option_type': 'Option types.', 'model': 'Pricing model.'},
        'input_example': {'price': '<series_handle>', 'spot': '<series_handle>', 'strike': '<series_handle>', 'time_to_expiry': '<series_handle>', 'rate': '<series_handle>', 'option_type': '<series_handle>', 'model': 'black_scholes'},
    },
    'opt_fit_surface': {
        'fn': 'opt_fit_surface',
        'description': 'opt_fit_surface -- category 40-option-implied-derivatives, method card #341.',
        'args': {'strikes': 'Quoted strikes.', 'expiries': 'Times to expiry in years.', 'implied_vols': 'Quoted implied volatilities.', 'forward': 'Forward price per expiry.', 'model': 'Surface parameterisation.', 'enforce_no_arbitrage': 'Constrain the fit to be arbitrage free.'},
        'input_example': {'strikes': '<series_handle>', 'expiries': '<series_handle>', 'implied_vols': '<series_handle>', 'forward': '<series_handle>', 'model': 'svi', 'enforce_no_arbitrage': True},
    },
    'opt_surface_evaluate': {
        'fn': 'opt_surface_evaluate',
        'description': 'opt_surface_evaluate -- category 40-option-implied-derivatives, method card #341.',
        'args': {'surface': 'Handle to a fitted surface.', 'strikes': 'Strikes to evaluate.', 'expiries': 'Expiries to evaluate.'},
        'input_example': {'surface': '<raw_handle>', 'strikes': [1.0, 2.0], 'expiries': [1.0, 2.0]},
    },
    'opt_arbitrage_check': {
        'fn': 'opt_arbitrage_check',
        'description': 'opt_arbitrage_check -- category 40-option-implied-derivatives, method card #341.',
        'args': {'surface': 'Handle to a fitted surface.', 'grid_size': 'Grid density for the check.'},
        'input_example': {'surface': '<raw_handle>', 'grid_size': 100},
    },
    'opt_risk_neutral_density': {
        'fn': 'opt_risk_neutral_density',
        'description': 'opt_risk_neutral_density -- category 40-option-implied-derivatives, method card #342.',
        'args': {'strikes': 'Strikes.', 'prices': 'Option prices or implied volatilities.', 'forward': 'Forward price.', 'time_to_expiry': 'Time to expiry in years.', 'rate': 'Risk-free rate.', 'smoothing': 'Smoothing applied before differentiation.', 'grid_size': 'Density grid points.'},
        'input_example': {'strikes': '<series_handle>', 'prices': '<series_handle>', 'forward': 1.0, 'time_to_expiry': 1.0, 'rate': 1.0, 'smoothing': 'svi', 'grid_size': 500},
    },
    'opt_model_free_variance': {
        'fn': 'opt_model_free_variance',
        'description': 'opt_model_free_variance -- category 40-option-implied-derivatives, method card #343.',
        'args': {'strikes': 'Strikes.', 'prices': 'Option prices.', 'option_type': 'Option types.', 'forward': 'Forward price.', 'time_to_expiry': 'Time to expiry in years.', 'rate': 'Risk-free rate.'},
        'input_example': {'strikes': '<series_handle>', 'prices': '<series_handle>', 'option_type': '<series_handle>', 'forward': 1.0, 'time_to_expiry': 1.0, 'rate': 1.0},
    },
    'opt_variance_risk_premium': {
        'fn': 'opt_variance_risk_premium',
        'description': 'opt_variance_risk_premium -- category 40-option-implied-derivatives, method card #343.',
        'args': {'implied_variance': 'Model-free implied variance series.', 'realised_variance': 'Realised variance series.', 'horizon': 'Horizon in days the two are aligned over.'},
        'input_example': {'implied_variance': '<series_handle>', 'realised_variance': '<series_handle>', 'horizon': 21},
    },
    'opt_risk_neutral_moments': {
        'fn': 'opt_risk_neutral_moments',
        'description': 'opt_risk_neutral_moments -- category 40-option-implied-derivatives, method card #344.',
        'args': {'strikes': 'Strikes.', 'prices': 'Option prices.', 'option_type': 'Option types.', 'forward': 'Forward price.', 'time_to_expiry': 'Time to expiry in years.', 'rate': 'Risk-free rate.'},
        'input_example': {'strikes': '<series_handle>', 'prices': '<series_handle>', 'option_type': '<series_handle>', 'forward': 1.0, 'time_to_expiry': 1.0, 'rate': 1.0},
    },
    'opt_implied_term_structure': {
        'fn': 'opt_implied_term_structure',
        'description': 'opt_implied_term_structure -- category 40-option-implied-derivatives, method card #345.',
        'args': {'maturities': 'Times to expiry in years.', 'implied_variance': 'Model-free implied variance per maturity.'},
        'input_example': {'maturities': [1.0, 2.0], 'implied_variance': [1.0, 2.0]},
    },
    'opt_density_fan': {
        'fn': 'opt_density_fan',
        'description': 'opt_density_fan -- category 40-option-implied-derivatives, method card #345.',
        'args': {'densities': 'Implied density per horizon.', 'grid': 'Value grid the densities are defined on.', 'quantiles': 'Quantile bands to report.'},
        'input_example': {'densities': '<matrix_handle>', 'grid': [1.0, 2.0], 'quantiles': [0.05, 0.25, 0.5, 0.75, 0.95]},
    },
    'opt_sv_calibrate': {
        'fn': 'opt_sv_calibrate',
        'description': 'opt_sv_calibrate -- category 40-option-implied-derivatives, method card #346.',
        'args': {'strikes': 'Strikes.', 'expiries': 'Times to expiry in years.', 'implied_vols': 'Quoted implied volatilities.', 'forward': 'Forward price per expiry.', 'model': 'Model family.', 'n_starts': 'Multi-start restarts for the calibration.', 'seed': 'Seed for the random number generator.'},
        'input_example': {'strikes': '<series_handle>', 'expiries': '<series_handle>', 'implied_vols': '<series_handle>', 'forward': '<series_handle>', 'model': 'heston', 'n_starts': 5},
    },
    'opt_sv_price': {
        'fn': 'opt_sv_price',
        'description': 'opt_sv_price -- category 40-option-implied-derivatives, method card #346.',
        'args': {'model': 'Handle to a calibrated model.', 'strikes': 'Strikes to price.', 'expiries': 'Expiries to price.'},
        'input_example': {'model': '<raw_handle>', 'strikes': [1.0, 2.0], 'expiries': [1.0, 2.0]},
    },
    'opt_sv_simulate': {
        'fn': 'opt_sv_simulate',
        'description': 'opt_sv_simulate -- category 40-option-implied-derivatives, method card #346.',
        'args': {'model': 'Handle to a calibrated model.', 'n_paths': 'Number of paths.', 'n_steps': 'Time steps per path.', 'scheme': 'Discretisation scheme.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'model': '<raw_handle>', 'n_paths': 10000, 'n_steps': 252, 'scheme': 'qe', 'seed': 1},
    },
}
