# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 22-inequality: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'affluence_line': {
        'fn': 'affluence_line',
        'description': 'affluence_line -- category 22-inequality, METHOD-SELECTION card #228.',
        'args': {'x': 'Handle to a numeric vector of incomes (x > 0), length >= 2.', 'weight': 'Handle to optional weights (same length, > 0); omission => equal.', 'k': 'POVERTY line as a multiple of the median; 0 < k < 1 IS REQUIRED (LOWER threshold — opposite meaning from richness_index).'},
        'input_example': {'x': '<matrix_handle>', 'k': 0.5},
    },
    'arpr_gb2': {
        'fn': 'arpr_gb2',
        'description': 'arpr_gb2 -- category 22-inequality, METHOD-SELECTION card #227.',
        'args': {'prop': 'Poverty-line ratio in (0,1) (typically 0.6).', 'shape1': 'Positive shape parameter a of the GB2.', 'shape2': 'Positive shape parameter p (Beta-2).', 'shape3': 'Positive shape parameter q (Beta-2).'},
        'input_example': {'prop': 0.5, 'shape1': 0.5, 'shape2': 0.5, 'shape3': 0.5},
    },
    'compute_inequality': {
        'fn': 'compute_inequality',
        'description': 'compute_inequality -- category 22-inequality, METHOD-SELECTION card #91.',
        'args': {'x': 'Handle to a numeric vector (e.g. incomes/weights), length >= 2, without NA/Inf; Gini/Atkinson/Theil/entropy require x >= 0.', 'type': 'Inequality index (default Gini).', 'parameter': 'Optional scalar: affects Atkinson (default 0.5), Kolm (default 1), entropy (default 0.5; entropy@1 == Theil).'},
        'input_example': {'x': '<matrix_handle>'},
    },
    'dineq_change_decomp': {
        'fn': 'dineq_change_decomp',
        'description': 'dineq_change_decomp -- category 22-inequality, METHOD-SELECTION card #225.',
        'args': {'formula1': "Year 1 OLS formula 'income ~ x1 + x2 +...' (same structure/order as formula2).", 'data1': 'Handle to a year 1 micro-data DataFrame.', 'weights1': 'WEIGHTS COLUMN NAME in data1 (string, > 0, without NA); None => equal-weighted.', 'formula2': 'Year 2 OLS formula (same characteristics/order as formula1).', 'data2': 'Handle to a year 2 micro-data DataFrame.', 'weights2': 'WEIGHTS COLUMN NAME in data2 (string, > 0, without NA); None => equal-weighted.'},
        'input_example': {'formula1': 'y ~ x', 'data1': '<df_handle>', 'formula2': 'y ~ x', 'data2': '<df_handle>'},
    },
    'dineq_regression_decomp': {
        'fn': 'dineq_regression_decomp',
        'description': 'dineq_regression_decomp -- category 22-inequality, METHOD-SELECTION card #225.',
        'args': {'formula': "OLS formula 'income ~ x1 + x2 +...' (multiple characteristics). log(y) -> y<=0 is deleted (n_deleted is reported).", 'data': 'Handle to a micro-data DataFrame (response + covariates + weights col).', 'weights': 'WEIGHTS COLUMN NAME in data (string, > 0, without NA); None => equal-weighted.'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>'},
    },
    'fit_gb2': {
        'fn': 'fit_gb2',
        'description': 'fit_gb2 -- category 22-inequality, METHOD-SELECTION card #227.',
        'args': {'z': 'Handle to a numeric vector of POSITIVE income (z > 0), length >= 10, without NA/Inf.', 'w': 'Optional handle to a weight vector (same length as z, positive); if missing, all weights = 1.', 'prop': 'Poverty-line ratio for the ARPR in (0,1); default 0.6 (60% of the median).', 'allow_nonconvergence': 'If True, non-convergence of the full ML does not block (converged=False); default False => hard stop on non-convergence.'},
        'input_example': {'z': '<matrix_handle>'},
    },
    'gini_decomposition': {
        'fn': 'gini_decomposition',
        'description': 'gini_decomposition -- category 22-inequality, METHOD-SELECTION card #225.',
        'args': {'x': 'Handle to numeric non-negative income (x >= 0, length >= 2, without NA/Inf).', 'z': 'Handle to a grouping vector (categorical/string/numeric), length == length(x), >= 2 groups, without NA. Passes as is (raw) -> factor in the wrapper.', 'weights': 'Handle to numeric weights, length == length(x), > 0, without NA; None => equal-weighted.'},
        'input_example': {'x': '<matrix_handle>', 'z': '<raw_handle>'},
    },
    'gini_gb2': {
        'fn': 'gini_gb2',
        'description': 'gini_gb2 -- category 22-inequality, METHOD-SELECTION card #227.',
        'args': {'shape1': 'Positive shape parameter a of the GB2.', 'shape2': 'Positive shape parameter p (Beta-2).', 'shape3': 'Positive shape parameter q (Beta-2).'},
        'input_example': {'shape1': 0.5, 'shape2': 0.5, 'shape3': 0.5},
    },
    'ic2_atkinson': {
        'fn': 'ic2_atkinson',
        'description': 'ic2_atkinson -- category 22-inequality, METHOD-SELECTION card #224.',
        'args': {'x': 'Handle to a numeric distribution vector (income/wealth/tax), length >= 2, without NA/Inf, x >= 0, sum(x) > 0.', 'w': 'Handle to optional sampling weights w (same length as x, strictly > 0); absence => unweighted.', 'epsilon': 'Inequality aversion parameter epsilon (> 0; default 1); epsilon==1 requires x > 0 (geometric mean).'},
        'input_example': {'x': '<matrix_handle>'},
    },
    'ic2_decomp_atkinson': {
        'fn': 'ic2_decomp_atkinson',
        'description': 'ic2_decomp_atkinson -- category 22-inequality, METHOD-SELECTION card #224.',
        'args': {'x': 'Handle to a numeric distribution vector (income/wealth/tax), length >= 2, without NA/Inf, x >= 0, sum(x) > 0.', 'z': 'Array of group labels z (same length as x); converted into a factor; >= 2 non-empty groups are required.', 'w': 'Handle to optional sampling weights w (same length as x, strictly > 0); absence => unweighted.', 'epsilon': 'Aversion parameter epsilon (> 0; default 1; epsilon==1 requires x > 0).', 'decomp': "Decomposition: 'BDA' Blackorby-Donaldson-Auersperg (MULTIPLICATIVE: total=1-(1-w)(1-b); 3rd term 'cross'; default) or 'DP' Das-Parikh (ADDITIVE: within+between+residual).", 'ELMO': "ELMO: computation of the 'maximum' between-group inequality (Elbers et al. 2005; default True)."},
        'input_example': {'x': '<matrix_handle>', 'z': ['PROVIDER/DATASET/SERIES']},
    },
    'ic2_decomp_gei': {
        'fn': 'ic2_decomp_gei',
        'description': 'ic2_decomp_gei -- category 22-inequality, METHOD-SELECTION card #224.',
        'args': {'x': 'Handle to a numeric distribution vector (income/wealth/tax), length >= 2, without NA/Inf, x >= 0, sum(x) > 0.', 'z': 'Array of group labels z (same length as x); converted into a factor; >= 2 non-empty groups are required.', 'w': 'Handle to optional sampling weights w (same length as x, strictly > 0); absence => unweighted.', 'alpha': 'GE parameter alpha (default 1; alpha ∈ {0,1} requires x > 0).', 'ELMO': "ELMO: computation of the 'maximum' between-group inequality (Elbers et al. 2005; default True)."},
        'input_example': {'x': '<matrix_handle>', 'z': ['PROVIDER/DATASET/SERIES']},
    },
    'ic2_decomp_sgini': {
        'fn': 'ic2_decomp_sgini',
        'description': 'ic2_decomp_sgini -- category 22-inequality, METHOD-SELECTION card #224.',
        'args': {'x': 'Handle to a numeric distribution vector (income/wealth/tax), length >= 2, without NA/Inf, x >= 0, sum(x) > 0.', 'z': 'Array of group labels z (same length as x); converted into a factor; >= 2 non-empty groups are required.', 'w': 'Handle to optional sampling weights w (same length as x, strictly > 0); absence => unweighted.', 'param': 'Extended Gini parameter (> 0; default 2).', 'decomp': "Decomposition: 'BM' Bhattacharya-Mahalanobis (within+between+overlap; default) or 'YL' Yitzhaki-Lerman (within+between+stratif).", 'ELMO': "ELMO: computation of the 'maximum' between-group inequality (Elbers et al. 2005; default True)."},
        'input_example': {'x': '<matrix_handle>', 'z': ['PROVIDER/DATASET/SERIES']},
    },
    'ic2_gei': {
        'fn': 'ic2_gei',
        'description': 'ic2_gei -- category 22-inequality, METHOD-SELECTION card #224.',
        'args': {'x': 'Handle to a numeric distribution vector (income/wealth/tax), length >= 2, without NA/Inf, x >= 0, sum(x) > 0.', 'w': 'Handle to optional sampling weights w (same length as x, strictly > 0); absence => unweighted.', 'alpha': 'GE parameter alpha (any finite real; default 1); alpha=1 Theil-T/GE(1), alpha=0 mean log deviation/GE(0)· alpha ∈ {0,1} requires x > 0.'},
        'input_example': {'x': '<matrix_handle>'},
    },
    'ic2_lorenz': {
        'fn': 'ic2_lorenz',
        'description': 'ic2_lorenz -- category 22-inequality, METHOD-SELECTION card #224.',
        'args': {'x': 'Handle to a numeric distribution vector (income/wealth/tax), length >= 2, without NA/Inf, x >= 0, sum(x) > 0.', 'w': 'Handle to optional sampling weights w (same length as x, strictly > 0); absence => unweighted.'},
        'input_example': {'x': '<matrix_handle>'},
    },
    'ic2_sconc': {
        'fn': 'ic2_sconc',
        'description': 'ic2_sconc -- category 22-inequality, METHOD-SELECTION card #224.',
        'args': {'x': 'Handle to a numeric vector for concentration (e.g. tax/benefit/expenditure), length >= 2, without NA/Inf, x >= 0, sum(x) > 0.', 'y': 'Handle to a numeric RANKING variable (e.g. pre-tax income); same length as x; negative values allowed; without NA/Inf.', 'w': 'Handle to optional sampling weights w (same length as x, strictly > 0); absence => unweighted.', 'param': 'Concentration parameter (> 0; default 2).'},
        'input_example': {'x': '<matrix_handle>', 'y': '<matrix_handle>'},
    },
    'ic2_sgini': {
        'fn': 'ic2_sgini',
        'description': 'ic2_sgini -- category 22-inequality, METHOD-SELECTION card #224.',
        'args': {'x': 'Handle to a numeric distribution vector (income/wealth/tax), length >= 2, without NA/Inf, x >= 0, sum(x) > 0.', 'w': 'Handle to optional sampling weights w (same length as x, strictly > 0); absence => unweighted.', 'param': 'Extended Gini parameter (> 0; default 2 = classical Gini); param>1 weights the poor; 0<param<1 => NEGATIVE.'},
        'input_example': {'x': '<matrix_handle>'},
    },
    'income_share_top': {
        'fn': 'income_share_top',
        'description': 'income_share_top -- category 22-inequality, METHOD-SELECTION card #228.',
        'args': {'x': 'Handle to a numeric vector of incomes (x > 0), length >= 2.', 'weight': 'Handle to optional weights (same length, > 0); omission => equal.', 'p': 'Percentile threshold in (0,1); the index = the share of income of the richest (1-p) fraction (e.g. p=0.9 => top 10%).'},
        'input_example': {'x': '<matrix_handle>', 'p': 0.5},
    },
    'lorenz_curve': {
        'fn': 'lorenz_curve',
        'description': 'lorenz_curve -- category 22-inequality, METHOD-SELECTION card #91.',
        'args': {'x': 'Handle to a numeric non-negative vector (x >= 0), length >= 2, without NA/Inf, total > 0.'},
        'input_example': {'x': '<matrix_handle>'},
    },
    'mld_decomposition': {
        'fn': 'mld_decomposition',
        'description': 'mld_decomposition -- category 22-inequality, METHOD-SELECTION card #225.',
        'args': {'x': 'Handle to numeric income (length >= 2, without NA/Inf). MLD=log -> x<=0 is silently deleted (n_deleted is reported).', 'z': 'Handle to a grouping vector, length == length(x), >= 2 groups, without NA (raw -> factor).', 'weights': 'Handle to numeric weights, length == length(x), > 0, without NA; None => equal-weighted.'},
        'input_example': {'x': '<matrix_handle>', 'z': '<raw_handle>'},
    },
    'richness_index': {
        'fn': 'richness_index',
        'description': 'richness_index -- category 22-inequality, METHOD-SELECTION card #228.',
        'args': {'x': 'Handle to a numeric vector of incomes (x > 0), length >= 2, without NA/Inf.', 'weight': 'Handle to optional population weights (same length as x, > 0); omission => equal weights.', 'k': 'Multiple of the median for the affluence line; k > 1 IS REQUIRED (UPPER threshold — k<=1 => "everyone is rich").', 'index': 'hc=richness headcount ratio; cha=concave (Chakravarty,T1); fgt=convex (FGT,T2); med=mean affluence gap (Medeiros, absolute). default hc.', 'beta': "Parameter for index='cha' (beta > 0; default 2).", 'alpha': "Parameter for index='fgt' (alpha > 1; default 2)."},
        'input_example': {'x': '<matrix_handle>', 'k': 0.5},
    },
    'rif_influence': {
        'fn': 'rif_influence',
        'description': 'rif_influence -- category 22-inequality, METHOD-SELECTION card #225.',
        'args': {'x': "Handle to a numeric vector of income (length >= 2, without NA/Inf; method='gini' requires x >= 0). NEVER in the schema.", 'weights': 'Handle to numeric weights (population factors), length == length(x), STRICTLY > 0, without NA. None => equal-weighted.', 'method': 'Distributional statistic (default quantile· gini· variance).', 'quantile': "Quantile ∈ (0,1) when method='quantile' (default 0.5=median).", 'kernel': "Smoothing kernel for the density in method='quantile' (default gaussian)."},
        'input_example': {'x': '<matrix_handle>', 'quantile': 0.5},
    },
    'rif_regression': {
        'fn': 'rif_regression',
        'description': 'rif_regression -- category 22-inequality, METHOD-SELECTION card #225.',
        'args': {'formula': "RIF regression formula 'income ~ x1 + x2 +...' (numeric response).", 'data': 'Handle to a micro-data DataFrame (contains response + covariates + weights col).', 'weights': "WEIGHTS COLUMN NAME inside data (string; dineq's dual convention); numeric, > 0, without NA. None => equal-weighted.", 'method': 'Distributional statistic (default quantile· gini· variance).', 'quantile': "One or MULTIPLE quantiles ∈ (0,1) when method='quantile' (default 0.5). The output is returned stacked per quantile.", 'kernel': "Smoothing kernel for method='quantile' (default gaussian)."},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>'},
    },
    'rif_regression_se': {
        'fn': 'rif_regression_se',
        'description': 'rif_regression_se -- category 22-inequality, METHOD-SELECTION card #225.',
        'args': {'formula': "RIF regression formula 'income ~ x1 + x2 +...'.", 'data': 'Handle to a micro-data DataFrame (response + covariates + weights col).', 'weights': 'WEIGHTS COLUMN NAME in data (string, > 0, without NA); None => equal-weighted.', 'method': 'Distributional statistic (default quantile· gini· variance).', 'quantile': "ONE quantile ∈ (0,1) when method='quantile' (bootstrap: scalar only).", 'kernel': "Smoothing kernel for method='quantile' (default gaussian).", 'Nboot': 'Number of bootstrap replicates (positive integer; default 100).', 'confidence': 'CI confidence level ∈ (0,1) (default 0.95).', 'seed': 'Seed for DETERMINISTIC bootstrap (same seed => identical; default 42).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'quantile': 0.5, 'Nboot': 100, 'confidence': 0.95, 'seed': 42},
    },
    'svy_inequality': {
        'fn': 'svy_inequality',
        'description': 'svy_inequality -- category 22-inequality, METHOD-SELECTION card #226.',
        'args': {'data': 'Handle to a MICRODATA DataFrame; contains the income/weights/design columns. svydesign is built internally.', 'income': 'Income column name (numeric, non-negative).', 'ids': 'PSU/cluster ID column name; give "1" for no clustering (ids=~1).', 'weights': 'Sampling weights column name (positive, > 0).', 'strata': 'Strata column name (optional).', 'fpc': 'Finite population correction column name (optional).', 'nest': 'PSU IDs nested within strata (default False).', 'subset_var': 'Column name for domain estimation (optional).', 'subset_level': 'Value of subset_var that defines the domain.', 'na_rm': 'Removal of income NA (default False; NA + False => hard gate).', 'level': 'CI confidence level in (0,1) (default 0.95).', 'measure': 'Inequality index (default gini).', 'alpha1': 'QSR: lower quantile in (0,1) (default 0.2 => S80/S20).', 'alpha2': 'QSR: upper quantile in (0,1) (default 1-alpha1); alpha1<alpha2.'},
        'input_example': {'data': '<df_handle>', 'income': '...', 'ids': '...', 'weights': '...'},
    },
    'svy_poverty': {
        'fn': 'svy_poverty',
        'description': 'svy_poverty -- category 22-inequality, METHOD-SELECTION card #226.',
        'args': {'data': 'Handle to a MICRODATA DataFrame; contains the income/weights/design columns. svydesign is built internally.', 'income': 'Income column name (numeric, non-negative).', 'ids': 'PSU/cluster ID column name; give "1" for no clustering (ids=~1).', 'weights': 'Sampling weights column name (positive, > 0).', 'strata': 'Strata column name (optional).', 'fpc': 'Finite population correction column name (optional).', 'nest': 'PSU IDs nested within strata (default False).', 'subset_var': 'Column name for domain estimation (optional).', 'subset_level': 'Value of subset_var that defines the domain.', 'na_rm': 'Removal of income NA (default False; NA + False => hard gate).', 'level': 'CI confidence level in (0,1) (default 0.95).', 'measure': 'Poverty index (default fgt).', 'g': 'FGT: integer >=0 (0 headcount, 1 gap, 2 severity; default 0).', 'type_thresh': 'FGT threshold: abs (absolute) | relq (relative-to-quantile) | relm (relative-to-mean). Default abs.', 'abs_thresh': "FGT: absolute poverty line (>0); ONLY when type_thresh='abs'.", 'percent': 'Percentage of the threshold for relative/ARPR (default 0.6).', 'quantiles': 'Base threshold quantile (default 0.5 = median).'},
        'input_example': {'data': '<df_handle>', 'income': '...', 'ids': '...', 'weights': '...'},
    },
}
