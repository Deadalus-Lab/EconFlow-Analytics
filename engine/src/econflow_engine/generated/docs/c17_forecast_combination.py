# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 17-forecast-combination: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'reconcile_grouped': {
        'fn': 'reconcile_grouped',
        'description': 'reconcile_grouped -- category 17-forecast-combination, method card #209.',
        'args': {'data': 'Handle to a long-format DataFrame (index column + >=1 key columns + numeric value column).', 'index': 'Time column name (valid series index: Date/yearmonth/yearquarter/numeric).', 'keys': "Key/grouping column names (>=1; they define the hierarchy's nodes); grouped requires >=2.", 'value': 'Measured numeric column name (without NA; summed into the aggregates).', 'structure': 'Structure: nested (grp1/grp2 hierarchy) or grouped (grp1*grp2 crossed; default nested).', 'base_model': 'Base model per node (ARIMA/ETS/SNAIVE; default arima).', 'method': 'Reconciliation: min_trace(method) MinT variants or bottom_up (default wls_struct — robust structural MinT).', 'h': 'Forecast horizon (positive integer; default 8).'},
        'input_example': {'data': '<df_handle>', 'index': '...', 'keys': ['PROVIDER/DATASET/SERIES'], 'value': '...', 'h': 8},
    },
    'reconcile_cross_temporal': {
        'fn': 'reconcile_cross_temporal',
        'description': 'reconcile_cross_temporal -- category 17-forecast-combination, method card #208.',
        'args': {'type': "Reconciliation framework: 'cs' cross-sectional (csrec; agg_mat), 'te' temporal (terec; agg_order), 'ct' cross-temporal (ctrec; agg_mat+agg_order).", 'base': 'Handle to the base forecasts. cs: (h x n) matrix, columns [upper..., bottom...] (n=n_a+n_b). te: (h*(k*+m)) vector lowest->highest freq. ct: (n x h*(k*+m)) matrix.', 'agg_mat': "Handle to the (n_a x n_b) aggregation matrix (map bottom->upper). Required for type='cs' and 'ct'.", 'agg_order': "Max temporal aggregation m (e.g. 4 quarterly->annual, 12 monthly) or a vector of factors of m. Required for 'te'/'ct'.", 'comb': "Covariance/MinT method (closed set PER type). cs: ols/str/wls/shr/oasd/sam. te: ols/str/wlsh/wlsv/acov/strar1/sar1/har1/shr/sam. ct: ols/str/csstr/testr/wlsh/wlsv/acov/bdshr/bdsam/Sshr/Ssam/shr/sam/hbshr/hbsam/bshr/bsam/hshr/hsam. WLS/GLS/MinT require 'res'. Default 'ols'.", 'tew': 'Type of temporal aggregation (te/ct): sum/avg/first/last (default sum).', 'approach': 'Approach: proj(ection)/strc(structural)/*_osqp (default proj).', 'res': 'Handle to in-sample residuals/validation errors (required for WLS/GLS/MinT comb). cs: (N x n) matrix. te: (N*(k*+m)) vector. ct: (n x N*(k*+m)) matrix.', 'nn': "Non-negativity algorithm for reconciled forecasts (default 'none')."},
        'input_example': {'type': 'cs', 'base': '<matrix_handle>', 'comb': 'ols'},
    },
    'crps_learning': {
        'fn': 'crps_learning',
        'description': 'crps_learning -- category 17-forecast-combination, method card #207.',
        'args': {'y': 'Handle to a Tx1 matrix of realized values (probabilistic setting); without NA.', 'experts': 'Handle to a numeric 3D array [T x quantiles(P) x experts(K)]: experts[t,,k] = quantile forecasts of expert k at the tau levels; dim1==length(y), dim2==length(tau), K>=2, without NA.', 'tau': 'Probability levels in (0,1); STRICTLY increasing/unique; length P == dim(experts)[2].', 'method': 'Online-learning algorithm (default bewa· boa=full BOA, ewa=exp. weighting, ml_poly=ML-Poly).', 'loss_function': 'Loss (default quantile = pinball/CRPS scoring).', 'loss_parameter': 'Scaling of the loss power (> 0; default 1).', 'loss_gradient': 'Linearized (gradient) version of the loss (default True).', 'lead_time': 'Offset of expert forecasts (0 = t+1 at t); integer 0<=·<T.', 'forget_regret': 'Share of past regret to forget per iteration; in [0,1] (default 0).', 'fixed_share': 'Fixed share added to the weights; in [0,1] (1 => uniform; default 0).', 'gamma': 'Scaling of the learning rate (> 0; default 1).', 'soft_threshold': 'Soft-threshold on the weights (default -Inf = none).', 'hard_threshold': 'Hard-threshold on the weights (default -Inf = none).', 'allow_quantile_crossing': 'False => the forecasts are sorted ascending per t (default False).', 'seed': 'Seed (integer >=0) — determinism of any grid sampling.'},
        'input_example': {'y': '<matrix_handle>', 'experts': '<raw_handle>', 'tau': [0.5, 0.5], 'loss_parameter': 1, 'loss_gradient': True, 'lead_time': 0, 'forget_regret': 0, 'fixed_share': 0, 'gamma': 1, 'soft_threshold': None, 'hard_threshold': None, 'allow_quantile_crossing': False, 'seed': 2025},
    },
    'run_hybrid': {
        'fn': 'run_hybrid',
        'description': 'run_hybrid -- category 17-forecast-combination, method card #85.',
        'args': {'y': 'Handle to a univariate ts/numeric series to forecast.', 'models': "String of component-model letters (>=2 distinct): a=auto-ARIMA e=ETS f=theta n=neural-net s=STL t=TBATS z=seasonal-naive (default 'aefnst').", 'weights': 'Combination weighting method (default equal).', 'errorMethod': 'Error metric for the weights (when weights != equal; default RMSE).', 'h': 'Forecast horizon (positive integer); default 2*frequency if seasonal, otherwise 10.', 'PI_combination': "How the components' prediction intervals are combined (default extreme; the PI are OVER-CONSERVATIVE, non-nominal coverage).", 'cvHorizon': "CV horizon (only weights='cv.errors'; default frequency(y)).", 'windowSize': "CV window length (only weights='cv.errors'; default 84).", 'seed': "Seed for DETERMINISM (neural-net's 'n' is stochastic; default 42)."},
        'input_example': {'y': '<series_handle>', 'models': 'aefnst', 'windowSize': 84, 'seed': 42},
    },
    'fc_combination_weights': {
        'fn': 'fc_combination_weights',
        'description': 'fc_combination_weights -- category 17-forecast-combination, method card #530.',
        'args': {'actual': 'Realised values.', 'forecasts': 'Forecasts, one column per method.', 'method': 'Weighting method.', 'window': 'Rolling window for the weights; omitted = expanding.', 'constrain': 'Constrain weights to be non-negative and sum to one.'},
        'input_example': {'actual': '<series_handle>', 'forecasts': '<df_handle>', 'method': 'inverse_mse', 'constrain': True},
    },
    'fc_density_combination': {
        'fn': 'fc_density_combination',
        'description': 'fc_density_combination -- category 17-forecast-combination, method card #531.',
        'args': {'densities': 'Predictive densities or samples, one per component.', 'weights': 'Component weights; omitted = equal.', 'pool': 'Pooling rule.', 'grid': 'Evaluation grid.'},
        'input_example': {'densities': '<matrix_handle>', 'pool': 'linear'},
    },
    'fc_score_driven_weights': {
        'fn': 'fc_score_driven_weights',
        'description': 'fc_score_driven_weights -- category 17-forecast-combination, method card #531.',
        'args': {'actual': 'Realised values.', 'densities': 'Component predictive densities over time.', 'forgetting': 'Forgetting factor on past scores.'},
        'input_example': {'actual': '<series_handle>', 'densities': '<matrix_handle>', 'forgetting': 0.95},
    },
    'fc_dynamic_model_averaging': {
        'fn': 'fc_dynamic_model_averaging',
        'description': 'fc_dynamic_model_averaging -- category 17-forecast-combination, method card #532.',
        'args': {'actual': 'Realised values.', 'forecasts': 'Forecasts, one column per model.', 'forgetting_weights': 'Forgetting factor on model probabilities.', 'forgetting_variance': 'Forgetting factor on the variance.', 'mode': 'Averaging or selection.'},
        'input_example': {'actual': '<series_handle>', 'forecasts': '<df_handle>', 'forgetting_weights': 0.99, 'forgetting_variance': 0.95, 'mode': 'averaging'},
    },
    'fc_stacking': {
        'fn': 'fc_stacking',
        'description': 'fc_stacking -- category 17-forecast-combination, method card #533.',
        'args': {'actual': 'Realised values.', 'forecasts': 'Forecasts, one column per component.', 'meta_learner': 'Meta-learner.', 'n_folds': 'Time-series cross-validation folds.'},
        'input_example': {'actual': '<series_handle>', 'forecasts': '<df_handle>', 'meta_learner': 'constrained_ls', 'n_folds': 5},
    },
    'fc_temporal_hierarchy': {
        'fn': 'fc_temporal_hierarchy',
        'description': 'fc_temporal_hierarchy -- category 17-forecast-combination, method card #534.',
        'args': {'y': 'Series at the highest frequency.', 'h': 'Forecast horizon at the base frequency.', 'levels': 'Aggregation levels; omitted = divisors of the season.', 'base_model': 'Model fitted at each level.', 'reconciliation': 'Reconciliation method.'},
        'input_example': {'y': '<series_handle>', 'h': 1, 'base_model': 'auto_ets', 'reconciliation': 'wls_struct'},
    },
}
