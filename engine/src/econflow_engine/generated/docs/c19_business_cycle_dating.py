# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 19-business-cycle-dating: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'average_over_phases': {
        'fn': 'average_over_phases',
        'description': 'average_over_phases -- category 19-business-cycle-dating, METHOD-SELECTION card #88.',
        'args': {'series': 'Handle to a univariate ts series of the same frequency as the dating.', 'dates': 'Handle to a BCDating object (from date_business_cycles register).'},
        'input_example': {'series': '<series_handle>', 'dates': '<raw_handle>'},
    },
    'changepoint_segments': {
        'fn': 'changepoint_segments',
        'description': 'changepoint_segments -- category 19-business-cycle-dating, METHOD-SELECTION card #213.',
        'args': {'fit': "Handle to an S4 'cpt' object (from detect_changepoints register field 'fit')."},
        'input_example': {'fit': '<raw_handle>'},
    },
    'date_business_cycles': {
        'fn': 'date_business_cycles',
        'description': 'date_business_cycles -- category 19-business-cycle-dating, METHOD-SELECTION card #88.',
        'args': {'y': 'Handle to a QUARTERLY (frequency == 4) univariate ts series.', 'mincycle': 'Minimum full-cycle duration in quarters (default 5; > minphase).', 'minphase': 'Minimum phase duration in quarters (default 2).', 'name': 'Optional name label of the dating.'},
        'input_example': {'y': '<series_handle>', 'mincycle': 5, 'minphase': 2},
    },
    'detect_change_points': {
        'fn': 'detect_change_points',
        'description': 'detect_change_points -- category 19-business-cycle-dating, METHOD-SELECTION card #214.',
        'args': {'y': 'Handle to a univariate numeric series (ts); without NA/Inf; length >= 4.', 'p0': 'Prior probability of a change U(0,p0) per position; ∈ (0,1] (default 0.2).', 'w0': 'Prior signal-to-noise ratio· ∈ (0,1] (default 0.2).', 'burnin': 'Number of MCMC burnin iterations (default 50).', 'mcmc': 'Number of MCMC iterations after burnin (default 500).', 'threshold': 'posterior.prob threshold for change-point detection; ∈ (0,1) (default 0.5).', 'seed': 'Seed for MCMC reproducibility (default 20240719).'},
        'input_example': {'y': '<series_handle>', 'p0': 0.2, 'w0': 0.2, 'burnin': 50, 'mcmc': 500, 'threshold': 0.5, 'seed': 20240719},
    },
    'detect_changepoints': {
        'fn': 'detect_changepoints',
        'description': 'detect_changepoints -- category 19-business-cycle-dating, METHOD-SELECTION card #213.',
        'args': {'x': 'Handle to a univariate numeric/ts series (without NA/Inf; not a matrix).', 'statistic': 'Which structure changes: mean (cpt.mean) / variance (cpt.var) / meanvar (cpt.meanvar). Default mean.', 'penalty': 'Penalty for selecting the number of change-points. Default MBIC. Manual/Asymptotic require pen_value.', 'pen_value': 'Penalty value: Manual => >0; Asymptotic => type-I error in (0,1]. A number only (not a formula).', 'method': 'Search algorithm. Default PELT (exact, fast). AMOC=at most 1 cp. CSS/CUSUM do NOT work with PELT.', 'Q': 'Maximum number of change-points (BinSeg) / segments (SegNeigh). Q < n/minseglen is required.', 'test_stat': 'Distribution/statistic: mean∈{Normal,CUSUM}; variance∈{Normal,CSS}; meanvar∈{Normal,Gamma,Exponential,Poisson}. Default Normal.', 'minseglen': 'Minimum segment length. Default: 1 (mean) / 2 (variance,meanvar).', 'know_mean': "ONLY statistic='variance': if True, the mean is considered known (mu).", 'mu': "ONLY statistic='variance' with know_mean=True: the known value of the mean.", 'shape': "ONLY statistic='meanvar' with test_stat='Gamma': the known shape parameter."},
        'input_example': {'x': '<series_handle>', 'pen_value': 0, 'Q': 5, 'know_mean': False, 'shape': 1},
    },
    'detect_changepoints_agglo': {
        'fn': 'detect_changepoints_agglo',
        'description': 'detect_changepoints_agglo -- category 19-business-cycle-dating, METHOD-SELECTION card #215.',
        'args': {'X': 'Handle to an n×d numeric matrix (multivariate series; without NA/Inf).', 'member': 'Optional initial segmentation vector of length the row count of X (default: each obs its own segment).', 'alpha': 'Moment index of the energy distance in (0,2] (default 1).', 'penalty': "Penalized GOF penalty: 'none' (none, default) or 'num_cp' (penalty on the number of change points)."},
        'input_example': {'X': '<matrix_handle>', 'alpha': 1},
    },
    'detect_changepoints_divisive': {
        'fn': 'detect_changepoints_divisive',
        'description': 'detect_changepoints_divisive -- category 19-business-cycle-dating, METHOD-SELECTION card #215.',
        'args': {'X': 'Handle to an n×d numeric matrix (multivariate series; without NA/Inf; nrow>=2*min.size).', 'sig_lvl': 'Significance level of the permutation test in the open interval (0,1) (default 0.05).', 'n_permutations': 'Number of permutations of the significance test (positive integer; default 199).', 'min_size': 'Minimum segment size (integer >=2; default 30; requires nrow>=2*min.size).', 'alpha': 'Moment index of the energy distance in (0,2] (default 1).', 'k': 'Optional: fixed requested number of change points (None=data-driven via permutation).', 'seed': 'Seed for reproducibility (e.divisive is stochastic; default 20240101).'},
        'input_example': {'X': '<matrix_handle>', 'sig_lvl': 0.05, 'n_permutations': 199, 'min_size': 30, 'alpha': 1, 'seed': 20240101},
    },
}
