# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 20-highdim-shrinkage-ml -- 12 nodes. No descriptions."""

from functools import cache

from pydantic import BaseModel

from econflow_engine.kinds import (
    NodeArgMeta,
    NodeExecutabilityMeta,
    NodeMeta,
    build_authoring_model,
    build_wire_model,
)

NODE_META: dict[str, NodeMeta] = {
    'bma_average': NodeMeta(
        fn='bma_average',
        category='20-highdim-shrinkage-ml',
        card_id=219,
        contract_hash='c-3f1b51eca1b021e1bdcd054bb19f1bf1f6a2235e916b108cca36a1b121510079',
        register_field='bma',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='mcmc',
        args=(
        NodeArgMeta(name='X_data', kind='matrix_handle', required=True),
        NodeArgMeta(name='mprior', kind='enum', required=False, enum=('uniform', 'fixed', 'random', 'pip', )),
        NodeArgMeta(name='g', kind='string', required=False),
        NodeArgMeta(name='mcmc', kind='enum', required=False, enum=('enumerate', 'bd', 'rev.jump', )),
        NodeArgMeta(name='nmodel', kind='integer', required=False),
        NodeArgMeta(name='burn', kind='integer', required=False),
        NodeArgMeta(name='iter', kind='integer', required=False),
        NodeArgMeta(name='mprior_size', kind='number', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'nmodel': 100, 'burn': 1000, 'iter': 3000, 'seed': 42},
    ),
    'bma_coefficients': NodeMeta(
        fn='bma_coefficients',
        category='20-highdim-shrinkage-ml',
        card_id=219,
        contract_hash='c-8f03c4825ea3349c7519a19e877ed5cf998938a3a0b7c6d97c1a8dc13e54a67e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        NodeArgMeta(name='exact', kind='boolean', required=False),
        NodeArgMeta(name='order_by_pip', kind='boolean', required=False),
        ),
        defaults={'exact': False, 'order_by_pip': True},
    ),
    'cv_glmnet': NodeMeta(
        fn='cv_glmnet',
        category='20-highdim-shrinkage-ml',
        card_id=216,
        contract_hash='c-02cd45374aa07cdb74425055b3576f05cd90e45872a2fc9298d1d993e0914a86',
        register_field='cv',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='matrix_handle', required=True),
        NodeArgMeta(name='y', kind='matrix_handle', required=True),
        NodeArgMeta(name='family', kind='enum', required=False, enum=('gaussian', 'binomial', 'poisson', 'multinomial', )),
        NodeArgMeta(name='alpha', kind='number', required=False),
        NodeArgMeta(name='nfolds', kind='integer', required=False),
        NodeArgMeta(name='type_measure', kind='enum', required=False, enum=('default', 'mse', 'deviance', 'mae', 'class', 'auc', )),
        NodeArgMeta(name='seed', kind='integer', required=False),
        NodeArgMeta(name='standardize', kind='boolean', required=False),
        NodeArgMeta(name='intercept', kind='boolean', required=False),
        ),
        defaults={'alpha': 1, 'nfolds': 10, 'seed': 42, 'standardize': True, 'intercept': True},
    ),
    'cv_group_penalized_regression': NodeMeta(
        fn='cv_group_penalized_regression',
        category='20-highdim-shrinkage-ml',
        card_id=220,
        contract_hash='c-1d5974e11d360f43744b774d5fc8a6e54807e81a69341ff21b5320f6f4a17c07',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='X', kind='matrix_handle', required=True),
        NodeArgMeta(name='y', kind='matrix_handle', required=True),
        NodeArgMeta(name='group', kind='int_array', required=False),
        NodeArgMeta(name='penalty', kind='enum', required=False, enum=('grLasso', 'grMCP', 'grSCAD', 'gel', 'cMCP', )),
        NodeArgMeta(name='family', kind='enum', required=False, enum=('gaussian', 'binomial', 'poisson', )),
        NodeArgMeta(name='nfolds', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        NodeArgMeta(name='nlambda', kind='integer', required=False),
        NodeArgMeta(name='gamma', kind='number', required=False),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'nfolds': 10, 'seed': 20240720, 'nlambda': 100, 'alpha': 1},
    ),
    'fit_glmnet': NodeMeta(
        fn='fit_glmnet',
        category='20-highdim-shrinkage-ml',
        card_id=216,
        contract_hash='c-9352e43d260aa972e88e57efd28add744646896fd22a3010cb3c74ef9c86e988',
        register_field='model',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='matrix_handle', required=True),
        NodeArgMeta(name='y', kind='matrix_handle', required=True),
        NodeArgMeta(name='family', kind='enum', required=False, enum=('gaussian', 'binomial', 'poisson', 'multinomial', )),
        NodeArgMeta(name='alpha', kind='number', required=False),
        NodeArgMeta(name='nlambda', kind='integer', required=False),
        NodeArgMeta(name='standardize', kind='boolean', required=False),
        NodeArgMeta(name='intercept', kind='boolean', required=False),
        ),
        defaults={'alpha': 1, 'nlambda': 100, 'standardize': True, 'intercept': True},
    ),
    'glmboost_cv_mstop': NodeMeta(
        fn='glmboost_cv_mstop',
        category='20-highdim-shrinkage-ml',
        card_id=218,
        contract_hash='c-2e026188ec1a67c490e65eca48c858e74b6bc5ebd98d34b98eeef08eb3fdc981',
        register_field='model',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='matrix_handle', required=True),
        NodeArgMeta(name='y', kind='matrix_handle', required=True),
        NodeArgMeta(name='family', kind='enum', required=False, enum=('Gaussian', 'QuantReg', 'Binomial', 'Poisson', 'Laplace', 'Huber', )),
        NodeArgMeta(name='tau', kind='number', required=False),
        NodeArgMeta(name='mstop_max', kind='integer', required=False),
        NodeArgMeta(name='nu', kind='number', required=False),
        NodeArgMeta(name='center', kind='boolean', required=False),
        NodeArgMeta(name='cv_type', kind='enum', required=False, enum=('subsampling', 'kfold', 'bootstrap', )),
        NodeArgMeta(name='cv_B', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'mstop_max': 200, 'cv_B': 25, 'seed': 42},
    ),
    'glmboost_fit': NodeMeta(
        fn='glmboost_fit',
        category='20-highdim-shrinkage-ml',
        card_id=218,
        contract_hash='c-e943e0d8058a6e94d4791f88a622f840844a331796da3618a226f343e6f54514',
        register_field='model',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='matrix_handle', required=True),
        NodeArgMeta(name='y', kind='matrix_handle', required=True),
        NodeArgMeta(name='family', kind='enum', required=False, enum=('Gaussian', 'QuantReg', 'Binomial', 'Poisson', 'Laplace', 'Huber', )),
        NodeArgMeta(name='tau', kind='number', required=False),
        NodeArgMeta(name='mstop', kind='integer', required=False),
        NodeArgMeta(name='nu', kind='number', required=False),
        NodeArgMeta(name='center', kind='boolean', required=False),
        ),
        defaults={'mstop': 100},
    ),
    'glmnet_coefficients': NodeMeta(
        fn='glmnet_coefficients',
        category='20-highdim-shrinkage-ml',
        card_id=216,
        contract_hash='c-6784818a578e1b75b88ee38903a3a8411c3848ce1e8e48cd281786835603d9da',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        NodeArgMeta(name='lambda', kind='number', required=False),
        NodeArgMeta(name='which', kind='enum', required=False, enum=('lambda.min', 'lambda.1se', )),
        ),
        defaults={},
    ),
    'glmnet_predict': NodeMeta(
        fn='glmnet_predict',
        category='20-highdim-shrinkage-ml',
        card_id=216,
        contract_hash='c-97557f4de1c983bf5da404ef7558c58f56568eb43e6bef57838178b42c7f9e57',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        NodeArgMeta(name='newx', kind='matrix_handle', required=True),
        NodeArgMeta(name='lambda', kind='number', required=False),
        NodeArgMeta(name='which', kind='enum', required=False, enum=('lambda.min', 'lambda.1se', )),
        NodeArgMeta(name='type', kind='enum', required=False, enum=('link', 'response', 'class', )),
        ),
        defaults={},
    ),
    'group_penalized_regression': NodeMeta(
        fn='group_penalized_regression',
        category='20-highdim-shrinkage-ml',
        card_id=220,
        contract_hash='c-cb809dee53ccb3ab9df0219d7bf78cf07ef2866bf868ec395258813ca95b5d5e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='X', kind='matrix_handle', required=True),
        NodeArgMeta(name='y', kind='matrix_handle', required=True),
        NodeArgMeta(name='group', kind='int_array', required=False),
        NodeArgMeta(name='penalty', kind='enum', required=False, enum=('grLasso', 'grMCP', 'grSCAD', 'gel', 'cMCP', )),
        NodeArgMeta(name='family', kind='enum', required=False, enum=('gaussian', 'binomial', 'poisson', )),
        NodeArgMeta(name='nlambda', kind='integer', required=False),
        NodeArgMeta(name='gamma', kind='number', required=False),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'nlambda': 100, 'alpha': 1},
    ),
    'rf_fit': NodeMeta(
        fn='rf_fit',
        category='20-highdim-shrinkage-ml',
        card_id=217,
        contract_hash='c-3c9fb626ad6b60535551250fb68553c7ee4f6914cb09d04feebfcdd34ec8c3d2',
        register_field='model',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='matrix_handle', required=True),
        NodeArgMeta(name='y', kind='matrix_handle', required=True),
        NodeArgMeta(name='num_trees', kind='integer', required=False),
        NodeArgMeta(name='mtry', kind='integer', required=False),
        NodeArgMeta(name='min_node_size', kind='integer', required=False),
        NodeArgMeta(name='importance', kind='enum', required=False, enum=('none', 'impurity', 'impurity_corrected', 'permutation', )),
        NodeArgMeta(name='quantreg', kind='boolean', required=False),
        NodeArgMeta(name='probability', kind='boolean', required=False),
        NodeArgMeta(name='classification', kind='boolean', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'num_trees': 500, 'quantreg': False, 'probability': False, 'classification': False, 'seed': 42},
    ),
    'rf_predict': NodeMeta(
        fn='rf_predict',
        category='20-highdim-shrinkage-ml',
        card_id=217,
        contract_hash='c-46a597517b1ad77afbcf6c56daa1c8e13377c981d5b6694ef061a21dadfbdcde',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        NodeArgMeta(name='newdata', kind='matrix_handle', required=True),
        NodeArgMeta(name='type', kind='enum', required=False, enum=('response', 'quantiles', 'se', )),
        NodeArgMeta(name='quantiles', kind='num_array', required=False),
        NodeArgMeta(name='se_method', kind='enum', required=False, enum=('infjack', 'jack', )),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'seed': 42},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'bma_average': {'nmodel': 100, 'burn': 1000, 'iter': 3000, 'seed': 42},
    'bma_coefficients': {'exact': False, 'order_by_pip': True},
    'cv_glmnet': {'alpha': 1, 'nfolds': 10, 'seed': 42, 'standardize': True, 'intercept': True},
    'cv_group_penalized_regression': {'nfolds': 10, 'seed': 20240720, 'nlambda': 100, 'alpha': 1},
    'fit_glmnet': {'alpha': 1, 'nlambda': 100, 'standardize': True, 'intercept': True},
    'glmboost_cv_mstop': {'mstop_max': 200, 'cv_B': 25, 'seed': 42},
    'glmboost_fit': {'mstop': 100},
    'glmnet_coefficients': {},
    'glmnet_predict': {},
    'group_penalized_regression': {'nlambda': 100, 'alpha': 1},
    'rf_fit': {'num_trees': 500, 'quantreg': False, 'probability': False, 'classification': False, 'seed': 42},
    'rf_predict': {'seed': 42},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
