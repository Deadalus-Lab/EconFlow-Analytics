# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 32-matching-weighting: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'mw_pscore_fit': {
        'fn': 'mw_pscore_fit',
        'description': 'mw_pscore_fit -- category 32-matching-weighting, method card #274.',
        'args': {'data': 'One row per unit.', 'treatment': 'Binary treatment column.', 'covariates': 'Covariate columns entering the score.', 'model': 'Estimator for the score.', 'seed': 'Seed for the random number generator.'},
        'input_example': {'data': '<df_handle>', 'treatment': '...', 'model': 'logit'},
    },
    'mw_common_support': {
        'fn': 'mw_common_support',
        'description': 'mw_common_support -- category 32-matching-weighting, method card #274.',
        'args': {'pscore': 'Fitted propensity per unit.', 'treatment': 'Binary treatment indicator.', 'rule': 'Trimming rule.', 'threshold': 'Cut-off for the fixed and quantile rules.'},
        'input_example': {'pscore': '<series_handle>', 'treatment': '<series_handle>', 'rule': 'minmax', 'threshold': 0.1},
    },
    'mw_overlap_diagnostics': {
        'fn': 'mw_overlap_diagnostics',
        'description': 'mw_overlap_diagnostics -- category 32-matching-weighting, method card #274.',
        'args': {'pscore': 'Fitted propensity per unit.', 'treatment': 'Binary treatment indicator.', 'n_bins': 'Histogram bins for the by-arm score distribution.'},
        'input_example': {'pscore': '<series_handle>', 'treatment': '<series_handle>', 'n_bins': 20},
    },
    'mw_match': {
        'fn': 'mw_match',
        'description': 'mw_match -- category 32-matching-weighting, method card #275.',
        'args': {'data': 'One row per unit.', 'treatment': 'Binary treatment column.', 'pscore': 'Column holding a pre-computed propensity score.', 'covariates': 'Covariates used when matching directly.', 'method': 'Matching rule.', 'n_neighbors': 'Controls matched per treated unit.', 'caliper': 'Maximum admissible distance.', 'replace': 'Match with replacement.', 'seed': 'Seed for the random number generator.'},
        'input_example': {'data': '<df_handle>', 'treatment': '...', 'method': 'nearest', 'n_neighbors': 1, 'replace': True},
    },
    'mw_match_effect': {
        'fn': 'mw_match_effect',
        'description': 'mw_match_effect -- category 32-matching-weighting, method card #275.',
        'args': {'matched': 'Handle to a completed matching.', 'outcome': 'Outcome per unit.', 'estimand': 'Estimand to report.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'matched': '<raw_handle>', 'outcome': '<series_handle>', 'estimand': 'att', 'conf_level': 0.95},
    },
    'mw_bias_corrected_att': {
        'fn': 'mw_bias_corrected_att',
        'description': 'mw_bias_corrected_att -- category 32-matching-weighting, method card #276.',
        'args': {'data': 'One row per unit.', 'treatment': 'Binary treatment column.', 'outcome': 'Outcome column.', 'covariates': 'Covariates used for matching and for the bias correction.', 'n_neighbors': 'Controls matched per treated unit.', 'estimand': 'Estimand to report.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'treatment': '...', 'outcome': '...', 'n_neighbors': 1, 'estimand': 'att', 'conf_level': 0.95},
    },
    'mw_cem': {
        'fn': 'mw_cem',
        'description': 'mw_cem -- category 32-matching-weighting, method card #277.',
        'args': {'data': 'One row per unit.', 'treatment': 'Binary treatment column.', 'covariates': 'Covariates to coarsen and match on.', 'coarsening': 'Binning rule for continuous covariates.', 'n_bins': 'Bins per covariate when the rule is manual.'},
        'input_example': {'data': '<df_handle>', 'treatment': '...', 'coarsening': 'sturges', 'n_bins': 5},
    },
    'mw_imbalance_l1': {
        'fn': 'mw_imbalance_l1',
        'description': 'mw_imbalance_l1 -- category 32-matching-weighting, method card #277.',
        'args': {'data': 'One row per unit.', 'treatment': 'Binary treatment column.', 'covariates': 'Covariates to measure imbalance over.', 'weights': 'Matching weights; omitted = unweighted.'},
        'input_example': {'data': '<df_handle>', 'treatment': '...'},
    },
    'mw_ipw': {
        'fn': 'mw_ipw',
        'description': 'mw_ipw -- category 32-matching-weighting, method card #278.',
        'args': {'data': 'One row per unit.', 'treatment': 'Binary treatment column.', 'outcome': 'Outcome column.', 'pscore': 'Pre-computed propensity column.', 'covariates': 'Covariates for the treatment model when no score is supplied.', 'stabilised': 'Use stabilised weights.', 'trim': 'Trim propensities to [trim, 1-trim].', 'estimand': 'Estimand to report.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'treatment': '...', 'outcome': '...', 'stabilised': True, 'trim': 0.01, 'estimand': 'ate', 'conf_level': 0.95},
    },
    'mw_aipw': {
        'fn': 'mw_aipw',
        'description': 'mw_aipw -- category 32-matching-weighting, method card #278.',
        'args': {'data': 'One row per unit.', 'treatment': 'Binary treatment column.', 'outcome': 'Outcome column.', 'covariates': 'Covariates for both the treatment and outcome models.', 'outcome_model': 'Learner for the outcome regression.', 'treatment_model': 'Learner for the propensity.', 'n_folds': 'Cross-fitting folds; 1 disables cross-fitting.', 'seed': 'Seed for the random number generator.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'treatment': '...', 'outcome': '...', 'outcome_model': 'linear', 'treatment_model': 'logit', 'n_folds': 5, 'conf_level': 0.95},
    },
    'mw_weight_diagnostics': {
        'fn': 'mw_weight_diagnostics',
        'description': 'mw_weight_diagnostics -- category 32-matching-weighting, method card #278.',
        'args': {'weights': 'Estimated weights per unit.', 'treatment': 'Binary treatment indicator.'},
        'input_example': {'weights': '<series_handle>', 'treatment': '<series_handle>'},
    },
    'mw_balance': {
        'fn': 'mw_balance',
        'description': 'mw_balance -- category 32-matching-weighting, method card #279.',
        'args': {'data': 'One row per unit.', 'treatment': 'Binary treatment column.', 'covariates': 'Covariates to assess.', 'weights': 'Design weights; omitted = unadjusted.', 'threshold': 'Standardised difference regarded as balanced.'},
        'input_example': {'data': '<df_handle>', 'treatment': '...', 'threshold': 0.1},
    },
    'mw_balance_distribution': {
        'fn': 'mw_balance_distribution',
        'description': 'mw_balance_distribution -- category 32-matching-weighting, method card #279.',
        'args': {'data': 'One row per unit.', 'treatment': 'Binary treatment column.', 'covariates': 'Covariates to assess.', 'weights': 'Design weights.', 'statistic': 'Distance measure.'},
        'input_example': {'data': '<df_handle>', 'treatment': '...', 'statistic': 'ks'},
    },
    'mw_subclassify': {
        'fn': 'mw_subclassify',
        'description': 'mw_subclassify -- category 32-matching-weighting, method card #280.',
        'args': {'data': 'One row per unit.', 'treatment': 'Binary treatment column.', 'outcome': 'Outcome column.', 'pscore': 'Column holding the propensity score.', 'n_strata': 'Number of score strata.', 'estimand': 'Aggregation weighting.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'treatment': '...', 'outcome': '...', 'pscore': '...', 'n_strata': 5, 'estimand': 'ate', 'conf_level': 0.95},
    },
    'mw_rosenbaum_bounds': {
        'fn': 'mw_rosenbaum_bounds',
        'description': 'mw_rosenbaum_bounds -- category 32-matching-weighting, method card #281.',
        'args': {'matched': 'Handle to a completed matching.', 'outcome': 'Outcome per unit.', 'gamma_max': 'Largest hidden-bias odds ratio to scan.', 'gamma_step': 'Step of the gamma grid.', 'alpha': 'Significance level.'},
        'input_example': {'matched': '<raw_handle>', 'outcome': '<series_handle>', 'gamma_max': 3.0, 'gamma_step': 0.1, 'alpha': 0.05},
    },
    'mw_e_value': {
        'fn': 'mw_e_value',
        'description': 'mw_e_value -- category 32-matching-weighting, method card #281.',
        'args': {'estimate': 'The effect estimate, on the ratio scale.', 'lower': 'Lower confidence limit.', 'upper': 'Upper confidence limit.', 'scale': 'Scale the estimate is reported on.'},
        'input_example': {'estimate': 1.0, 'scale': 'risk_ratio'},
    },
    'mw_gcomputation': {
        'fn': 'mw_gcomputation',
        'description': 'mw_gcomputation -- category 32-matching-weighting, method card #282.',
        'args': {'data': 'One row per unit.', 'treatment': 'Binary treatment column.', 'outcome': 'Outcome column.', 'covariates': 'Covariates in the outcome model.', 'outcome_model': 'Learner for the outcome regression.', 'estimand': 'Population to standardise over.', 'nboot': 'Number of bootstrap replications.', 'seed': 'Seed for the random number generator.'},
        'input_example': {'data': '<df_handle>', 'treatment': '...', 'outcome': '...', 'outcome_model': 'linear', 'estimand': 'ate', 'nboot': 999},
    },
    'mw_tmle': {
        'fn': 'mw_tmle',
        'description': 'mw_tmle -- category 32-matching-weighting, method card #282.',
        'args': {'data': 'One row per unit.', 'treatment': 'Binary treatment column.', 'outcome': 'Outcome column.', 'covariates': 'Covariates for both models.', 'outcome_model': 'Learner for the outcome regression.', 'treatment_model': 'Learner for the propensity.', 'trim': 'Trim propensities to [trim, 1-trim].', 'seed': 'Seed for the random number generator.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'treatment': '...', 'outcome': '...', 'outcome_model': 'gradient_boosting', 'treatment_model': 'logit', 'trim': 0.01, 'conf_level': 0.95},
    },
}
