# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 16-limited-dependent: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'hdfe_average_partial_effects': {
        'fn': 'hdfe_average_partial_effects',
        'description': 'hdfe_average_partial_effects -- category 16-limited-dependent, method card #206.',
        'args': {'object': 'Handle to a fitted (+bias-corrected) feglm model from hdfe_glm· ONLY binary choice (binomial).', 'n_pop': 'Finite-population correction (population size)· empty=delta-method only.', 'sampling_fe': 'Sampling assumptions for the FPC of the APE covariance (default independence).', 'weak_exo': 'True if some regressors are weakly exogenous/predetermined (default False).'},
        'input_example': {'object': '<raw_handle>', 'weak_exo': False},
    },
    'hdfe_glm': {
        'fn': 'hdfe_glm',
        'description': 'hdfe_glm -- category 16-limited-dependent, method card #206.',
        'args': {'formula': "FE GLM formula 'y ~ x1 + x2 | fe1 + fe2' — the '| fe' part (high-dim fixed effects) is REQUIRED.", 'data': 'Handle to a panel DataFrame· response binary (binomial) or non-negative integers/counts (poisson), without NA in the variables.', 'family': 'Family/link (default logit· probit=binomial probit· poisson=count).', 'bias_correct': 'Analytical incidental-parameter bias correction (Fernández-Val/Weidner)· ONLY binomial (default False).', 'L': 'Spectral density bandwidth (Hahn-Kuersteiner)· 0=strictly exogenous, 1-4 for weakly exogenous (lagged) regressors.', 'panel_structure': 'Panel structure for the bias correction (default classic· network=bilateral).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'bias_correct': False, 'L': 0},
    },
    'run_binomial_fe_glm': {
        'fn': 'run_binomial_fe_glm',
        'description': 'run_binomial_fe_glm -- category 16-limited-dependent, method card #83.',
        'args': {'formula': "Binary model formula, e.g. 'recession ~ spread'· high-dim fixed effects also via '| year'.", 'data': 'Handle to a DataFrame· LHS binary (0/1, logical or 2-level factor), without NA in the variables.', 'link': 'Link function (default probit — Estrella-Mishkin).', 'fixef': "Column name of the high-dim fixed effect (alternatively via '| col' in the formula)· the column must exist in the data."},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>'},
    },
    'run_roc': {
        'fn': 'run_roc',
        'description': 'run_roc -- category 16-limited-dependent, method card #84.',
        'args': {'response': 'Handle to a binary target (logical, numeric 0/1 or categorical/string with 2 levels).', 'predictor': 'Handle to a numeric score/prediction (e.g. the fitted_probabilities of #83), of the same length as the response.', 'direction': "Relation of controls to cases (default auto· '<' = normal prob-score).", 'ci': 'Computation of the DeLong CI of the AUC (default True).', 'conf_level': 'Confidence level of the CI of the AUC, in (0,1) (default 0.95).'},
        'input_example': {'response': '<raw_handle>', 'predictor': '<raw_handle>', 'ci': True, 'conf_level': 0.95},
    },
    'ld_ordered_choice': {
        'fn': 'ld_ordered_choice',
        'description': 'ld_ordered_choice -- category 16-limited-dependent, method card #523.',
        'args': {'y': 'Ordered categorical outcome.', 'x': 'Covariate table.', 'link': 'Link function.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'y': '<series_handle>', 'x': '<df_handle>', 'link': 'logit', 'conf_level': 0.95},
    },
    'ld_proportional_odds_test': {
        'fn': 'ld_proportional_odds_test',
        'description': 'ld_proportional_odds_test -- category 16-limited-dependent, method card #523.',
        'args': {'fit': 'Handle to a fitted ordered model.', 'alpha': 'Significance level.'},
        'input_example': {'fit': '<raw_handle>', 'alpha': 0.05},
    },
    'ld_count_model': {
        'fn': 'ld_count_model',
        'description': 'ld_count_model -- category 16-limited-dependent, method card #524.',
        'args': {'y': 'Count outcome.', 'x': 'Covariate table.', 'family': 'Count family.', 'zeros': 'Zero handling.', 'exposure': 'Exposure entering as an offset.', 'inflation_covariates': 'Covariates in the inflation equation.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'y': '<series_handle>', 'x': '<df_handle>', 'family': 'negative_binomial', 'zeros': 'none', 'conf_level': 0.95},
    },
    'ld_overdispersion_test': {
        'fn': 'ld_overdispersion_test',
        'description': 'ld_overdispersion_test -- category 16-limited-dependent, method card #524.',
        'args': {'fit': 'Handle to a fitted count model.', 'alpha': 'Significance level.'},
        'input_example': {'fit': '<raw_handle>', 'alpha': 0.05},
    },
    'ld_tobit': {
        'fn': 'ld_tobit',
        'description': 'ld_tobit -- category 16-limited-dependent, method card #525.',
        'args': {'y': 'Outcome.', 'x': 'Covariate table.', 'left': 'Left censoring or truncation limit.', 'right': 'Right censoring or truncation limit.', 'model': 'Model.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'y': '<series_handle>', 'x': '<df_handle>', 'model': 'censored', 'conf_level': 0.95},
    },
    'ld_heckman': {
        'fn': 'ld_heckman',
        'description': 'ld_heckman -- category 16-limited-dependent, method card #526.',
        'args': {'y': 'Outcome, observed for the selected subsample.', 'x': 'Outcome-equation covariates.', 'selection': 'Selection indicator.', 'z': 'Selection-equation covariates, including the exclusion.', 'method': 'Estimator.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'y': '<series_handle>', 'x': '<df_handle>', 'selection': '<series_handle>', 'z': '<df_handle>', 'method': 'two_step', 'conf_level': 0.95},
    },
    'ld_fractional_response': {
        'fn': 'ld_fractional_response',
        'description': 'ld_fractional_response -- category 16-limited-dependent, method card #527.',
        'args': {'y': 'Bounded outcome.', 'x': 'Covariate table.', 'model': 'Model.', 'link': 'Link function.', 'precision_covariates': 'Covariates modelling the precision parameter.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'y': '<series_handle>', 'x': '<df_handle>', 'model': 'fractional', 'link': 'logit', 'conf_level': 0.95},
    },
    'ld_unordered_choice': {
        'fn': 'ld_unordered_choice',
        'description': 'ld_unordered_choice -- category 16-limited-dependent, method card #528.',
        'args': {'y': 'Categorical outcome.', 'x': 'Covariate table.', 'model': 'Model.', 'base': 'Base alternative.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'y': '<series_handle>', 'x': '<df_handle>', 'model': 'multinomial', 'conf_level': 0.95},
    },
    'ld_classification_evaluation': {
        'fn': 'ld_classification_evaluation',
        'description': 'ld_classification_evaluation -- category 16-limited-dependent, method card #529.',
        'args': {'y': 'Binary or categorical outcome.', 'probability': 'Predicted probability.', 'threshold': 'Classification threshold.', 'n_bins': 'Calibration buckets.', 'decompose': 'Decompose the Brier score.'},
        'input_example': {'y': '<series_handle>', 'probability': '<series_handle>', 'threshold': 0.5, 'n_bins': 10, 'decompose': True},
    },
}
