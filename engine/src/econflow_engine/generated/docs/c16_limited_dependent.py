# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 16-limited-dependent: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'alpaca_apes': {
        'fn': 'alpaca_apes',
        'description': 'alpaca_apes -- category 16-limited-dependent, METHOD-SELECTION card #206.',
        'args': {'object': 'Handle to a fitted (+bias-corrected) feglm model from alpaca_feglm· ONLY binary choice (binomial).', 'n_pop': 'Finite-population correction (population size)· empty=delta-method only.', 'sampling_fe': 'Sampling assumptions for the FPC of the APE covariance (default independence).', 'weak_exo': 'True if some regressors are weakly exogenous/predetermined (default False).'},
        'input_example': {'object': '<raw_handle>', 'weak_exo': False},
    },
    'alpaca_feglm': {
        'fn': 'alpaca_feglm',
        'description': 'alpaca_feglm -- category 16-limited-dependent, METHOD-SELECTION card #206.',
        'args': {'formula': "FE GLM formula 'y ~ x1 + x2 | fe1 + fe2' — the '| fe' part (high-dim fixed effects) is REQUIRED.", 'data': 'Handle to a panel DataFrame· response binary (binomial) or non-negative integers/counts (poisson), without NA in the variables.', 'family': 'Family/link (default logit· probit=binomial probit· poisson=count).', 'bias_correct': 'Analytical incidental-parameter bias correction (Fernández-Val/Weidner)· ONLY binomial (default False).', 'L': 'Spectral density bandwidth (Hahn-Kuersteiner)· 0=strictly exogenous, 1-4 for weakly exogenous (lagged) regressors.', 'panel_structure': 'Panel structure for the bias correction (default classic· network=bilateral).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'bias_correct': False, 'L': 0},
    },
    'run_feglm_binom': {
        'fn': 'run_feglm_binom',
        'description': 'run_feglm_binom -- category 16-limited-dependent, METHOD-SELECTION card #83.',
        'args': {'formula': "Binary model formula, e.g. 'recession ~ spread'· high-dim fixed effects also via '| year'.", 'data': 'Handle to a DataFrame· LHS binary (0/1, logical or 2-level factor), without NA in the variables.', 'link': 'Link function (default probit — Estrella-Mishkin).', 'fixef': "Column name of the high-dim fixed effect (alternatively via '| col' in the formula)· the column must exist in the data."},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>'},
    },
    'run_roc': {
        'fn': 'run_roc',
        'description': 'run_roc -- category 16-limited-dependent, METHOD-SELECTION card #84.',
        'args': {'response': 'Handle to a binary target (logical, numeric 0/1 or categorical/string with 2 levels).', 'predictor': 'Handle to a numeric score/prediction (e.g. the fitted_probabilities of #83), of the same length as the response.', 'direction': "Relation of controls to cases (default auto· '<' = normal prob-score).", 'ci': 'Computation of the DeLong CI of the AUC (default True).', 'conf_level': 'Confidence level of the CI of the AUC, in (0,1) (default 0.95).'},
        'input_example': {'response': '<raw_handle>', 'predictor': '<raw_handle>', 'ci': True, 'conf_level': 0.95},
    },
}
