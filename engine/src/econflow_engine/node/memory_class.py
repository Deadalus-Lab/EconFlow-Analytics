# SPDX-License-Identifier: AGPL-3.0-only
"""Per-node MEMORY CLASS.

WHY IT EXISTS: the orchestrator runs independent branches of a graph in
parallel, with a limit on concurrent engine calls. A limit that counts CALLS
instead of WEIGHT is wrong in both directions -- two simultaneous MCMC fits kill
the machine, while two simultaneous differencing operations bother nobody. The
canvas also needs to warn BEFORE the run, not after the container has died.

WHAT THE CLASS DECLARES, AND WHAT IT DOES NOT. It is NOT a prediction in
megabytes, and could not be: the memory of a call is dominated by the size of
the data the user uploads, which the spec does not know. What the spec DOES know,
structurally, is whether the method MULTIPLIES that data:

    light -- one pass over the data.                     O(data)
    heavy -- keeps a resampling/simulation store.        O(B x data)
    mcmc  -- runs a Markov chain; the draw store lives   O(chains x iter x pars)
             entirely in memory until it is written out.

THE RULE IS AN UPPER BOUND, WHICH IS WHY IT HAS NO EXCEPTION TABLE. A class that
is too high costs PARALLELISM and never correctness; a class that is too low
costs a killed container. So the rule errs upward and applies mechanically to all
913 nodes -- a hand-maintained per-node table would rot silently with every new
spec.

IT IS NOT A GATE. No call is refused for being ``mcmc``. It is ROUTING metadata,
which is why it does not enter the contract hash: it changes neither what the
node accepts nor what it returns, so a stored graph is unaffected.

WHAT THE RULE DELIBERATELY DOES NOT CATCH, stated openly: methods whose footprint
grows with the SQUARE of the sample and expose no sampling argument (distance
matrices, spatial weights). They stay ``light`` because their cost is set by
INPUT SIZE, which the orchestrator knows from the sidecar and this module does
not. The escape hatch is an explicit ``memory_class`` in the spec, never a second
heuristic here.
"""

from __future__ import annotations

from typing import Any, Final

from econflow_engine.mcp.allowlists import MEMORY_CLASSES, STOCHASTIC_UNSEEDED_FNS

__all__ = ["MCMC_ARGS", "RESAMPLE_ARGS", "memory_class_of"]

#: Argument names that declare a SAMPLE STORE. They are not exclusive to
#: samplers, and they do not need to be -- measured over the 913 specs, `iter`
#: and `niter` also appear in iterative optimisers and `draws` in diagnostics
#: over already-built chains. Both are classified UPWARD, the safe direction.
MCMC_ARGS: Final[frozenset[str]] = frozenset(
    {"chains", "iter", "warmup", "burnin", "burn", "thin", "draws", "niter", "n_burn"}
)

#: Argument names that declare a resampling or simulation store.
RESAMPLE_ARGS: Final[frozenset[str]] = frozenset(
    {"nboot", "n_boot", "bootstrap", "boot", "nsim", "n_sim", "sims", "nrep", "n_rep",
     "runs", "B"}
)


def memory_class_of(spec: Any) -> str:
    """Classify one node. Pure and TOTAL: every spec gets a value, never ``None``.

    Decision order, first match wins:

    1. an explicit ``memory_class`` on the spec -- for the node that knows better
       than the rule. An unknown value RAISES at export or boot, never a silent
       correction.
    2. a sampler argument                                   -> ``mcmc``
    3. a resampling argument, or a known stochastic node with no seed  -> ``heavy``
    4. otherwise                                            -> ``light``

    Step 3 reuses the vocabulary's ``stochastic_unseeded_fns`` rather than a
    second list of the same names: a new unseeded stochastic node picks up the
    right memory class the moment it is added there.
    """
    declared = _get(spec, "memory_class")
    if declared is not None:
        text = str(declared)
        if text not in MEMORY_CLASSES:
            fn = _get(spec, "fn") or "?"
            raise ValueError(
                f"memory_class: unknown value '{text}' in spec '{fn}'. "
                f"Permitted: {' | '.join(MEMORY_CLASSES)}."
            )
        return text
    arg_names = _argument_names(spec)
    if arg_names & MCMC_ARGS:
        return "mcmc"
    fn = str(_get(spec, "fn") or "")
    if (arg_names & RESAMPLE_ARGS) or fn in STOCHASTIC_UNSEEDED_FNS:
        return "heavy"
    return "light"


def _get(spec: Any, key: str) -> Any:
    if isinstance(spec, dict):
        return spec.get(key)
    return getattr(spec, key, None)


def _argument_names(spec: Any) -> set[str]:
    arguments = _get(spec, "arguments") or _get(spec, "args") or ()
    if isinstance(arguments, dict):
        return set(arguments)
    names: set[str] = set()
    for arg in arguments:
        name = arg.get("name") if isinstance(arg, dict) else getattr(arg, "name", None)
        if name is not None:
            names.add(str(name))
    return names
