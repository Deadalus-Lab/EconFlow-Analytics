#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
#
# check-vocabulary.sh -- this project documents itself in its own terms.
#
# WHAT IT ENFORCES. Documentation, argument names, enum values and error messages
# describe THIS implementation: Python types, this contract's argument kinds, and
# the statistical method itself. It refuses vocabulary carried in from another
# statistical-computing ecosystem -- a library name, a class name, a function
# call, a toolchain marker -- and it refuses the language of translation. A
# wrapper that documents itself in somebody else's dialect sends the reader
# somewhere this repository cannot take them, and names an object they cannot
# inspect here.
#
# WHY THE LIBRARY NAMES ARE THE LOAD-BEARING HALF, AND WHY THIS FILE WAS REPLACED.
# The previous version of this gate matched a LANGUAGE and its TOOLCHAIN -- a
# namespace operator, a package index, a package manager, a source-file
# extension -- and knew not one library name. On 2026-08-21 it reported a clean
# tree, with its floor met and both its controls firing, while the sealed
# artifacts described a spatial-weights list, a Johansen object, a panel
# estimator, a resampling harness and a clustering package by their upstream
# names, and while every generated category guide rendered them to the reader. A
# gate that checks the easy half of its subject and then reports success for the
# whole is worse than no gate: it converts an unexamined tree into a documented
# assurance.
#
# WHY THERE IS NO SINGLE-LETTER RULE ANY MORE. The version replaced here matched a
# bare capital letter as an ecosystem name, and needed twenty lines of exemptions
# to survive contact with mathematics -- R-hat, R^2, the Kalman covariances Q and
# R, a cointegration rank, and every author initial in the catalogue. It still
# flagged `chown -R` in the Dockerfile. Somebody removed the letter to make the
# gate green, the line became `chown -the engine`, an invalid option, and the
# image build stayed broken because no gate builds the image. A false positive a
# reader can only silence by damaging the tree is a defect in the gate. This one
# matches NAMES, never single letters.
#
# WHAT IT DELIBERATELY PERMITS, and why the omissions are listed rather than
# guessed at. Several library names collide exactly with the standard name of a
# statistical object, and the mathematics always wins:
#
#     sf      the Shapiro-Francia normality test
#     car     the cumulative abnormal return of an event study
#     gbm     geometric Brownian motion
#     np      nonparametric inference
#     vars    the variables of a model, and the argument that names them
#     AER     the American Economic Review, in roughly a dozen citations
#     coda    a Markov-chain diagnostic family named for its own literature
#     party   as in "third-party"
#     NA / NULL / FALSE   a missing value, a null hypothesis, a false alarm
#     copula, vine, smooth, forecast, seasonal, robust, leverage, pivotal
#     snaive  the seasonal-naive benchmark, an abbreviation the forecasting
#             literature and every Python forecasting library use alike
#     BSTS    a published method acronym; the 2026-08-19 register records the
#             rule that acronyms naming a METHOD are kept and only names of an
#             IMPLEMENTATION are removed
#     as.factor, I, poly, interaction  the formula mini-language is a
#             deliberately R-shaped dialect, which is also the Python convention
#             (patsy and formulaic both implement it); the allowlist in
#             `formula.py` is contract and security-critical, and is not prose
#     haven   as in "haven't"; counterpart, counterparty  as in `rpart`
#
# Each of these is ABSENT FROM THE TOKEN LIST rather than exempted after the
# fact, because an exemption that strips text before matching is the mechanism by
# which a list quietly widens into "match nothing". Author names and initials are
# safe for the same reason: this gate has no rule that can reach them.
#
# THE MATCHING IS DONE IN PYTHON, AND THAT IS LOAD-BEARING. An earlier version
# stripped its exemptions with `sed -E "s/${ALLOWED}//g"`. The list contained a
# `/`, which is sed's own delimiter, so sed exited with an error, printed
# nothing, and the gate reported a clean tree while examining nothing at all. No
# helper that can fail into silence may sit between this gate and its input.
#
# WHERE A FINDING IS FIXED. Anything under
# `engine/src/econflow_engine/wrappers/**/*.md` is GENERATED from `engine/corpus/`
# by `gen_wrappers.py`. Editing the guide is reverted by the next `--write`, so
# the fix belongs in the corpus card, and the artifacts are then rebuilt and
# resealed. Anything under `engine/src/econflow_engine/generated/**` is generated
# from `artifacts/node-specs.json` by `gen_schemas.py`, which is itself built
# from the corpus. The corpus is the only place any of this prose is written.
#
# FOUR ANTI-VACUITY GUARDS, because a scan that examined nothing must never read
# as a scan that passed:
#   1. it asserts it examined at least the floor in .github/inventory.json
#   2. POSITIVE controls it must catch on every invocation, ONE PER RULE FAMILY.
#      One string for all of them is satisfied by whichever rule fires first in
#      it, so every other rule could be narrowed to nothing and this would still
#      report success -- which is what happened to the first draft of the
#      namespace control, whose example names were themselves in LIBRARIES
#   3. a NEGATIVE control -- a line of real mathematics, a citation, an author's
#      initial and a pytest node ID -- that it must NOT flag, so the token list
#      cannot silently decay into one that matches nothing that matters
#   4. NEGATIVE-DIRECTION controls, one per narrowing of the one rule here
#      that has been narrowed, each asserting that its narrowing did not
#      reach further than intended
#
# Binary files are skipped: there is no prose in a parquet fixture to fix.
#
#   usage: check-vocabulary.sh [repo-root]
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

ALLOWLIST=".github/vocabulary-allowlist.txt"
MANIFEST=".github/inventory.json"
[ -f "$ALLOWLIST" ] || {
  echo "FAIL: no allowlist at $ALLOWLIST" >&2
  exit 2
}
[ -f "$MANIFEST" ] || {
  echo "FAIL: no manifest at $MANIFEST" >&2
  exit 2
}

python3 - "$ALLOWLIST" "$MANIFEST" <<'PY'
import json
import pathlib
import re
import sys

allowlist_path, manifest_path = sys.argv[1], sys.argv[2]

# ---------------------------------------------------------------- the tokens
# Every entry is UNAMBIGUOUS: it has no reading as an English word, an
# econometric object or a person's name. Ambiguous names are omitted entirely --
# see the header.
LIBRARIES = (
    # EVERY token is anchored on BOTH sides. An unanchored token is how a list
    # like this goes wrong: `rpart` without a leading boundary matches inside
    # "counterpart" and "counterparty", and the reader is asked to damage a
    # sentence about interbank exposures to make a gate green.
    # time series and forecasting
    r"\brugarch\b|\brmgarch\b|\bfGarch\b|\btseries\b|\burca\b|\bstrucchange\b|\blmtest\b|"
    r"\bfable\b|\bfabletools\b|\bfeasts\b|\btsibble\b|\bnnetar\b|\bthetam\b|\bstlm\b|"
    r"\bauto\.arima\b|\bStructTS\b|\bnnfor\b|\bcaretForecast\b|\bmidasr\b|\bfracdiff\b|\btsDyn\b|"
    # panel, spatial, networks
    r"\bplm\b|\bspdep\b|\bspatialreg\b|\blistw\b|\bnb2listw\b|\bsystemfit\b|\blme4\b|\bnlme\b|"
    r"\bVarCorr\b|\bfrequencyConnectedness\b|\bbvartools\b|\bMSwM\b|"
    # bayes and state space
    r"\brstan\b|\bbrms\b|\bMARSS\b|\bKFAS\b|\bstochvol\b|\bMCMCpack\b|\bnimbleCode\b|"
    r"\bbayesm\b|"
    # ml, clustering, robustness
    r"\bglmnet\b|\branger\b|\brandomForest\b|\bquantregForest\b|\bcaret\b|\be1071\b|"
    r"\bmclust\b|\bcovMcd\b|\bh\.alpha\.n\b|\bkernlab\b|\brpart\b|"
    # data handling and io
    r"\btibble\b|\bdplyr\b|\btidyr\b|\bggplot2?\b|\bpurrr\b|\bmagrittr\b|\blubridate\b|"
    r"\breadr\b|\bcellranger\b|\bdata\.table\b|"
    # classes and language builtins of other ecosystems
    r"\bPOSIXct\b|\bPOSIXlt\b|\bdifftime\b|\bdata\.frame\b|\bas\.Date\b|\bas\.numeric\b|"
    r"\bis\.na\b|\bna\.rm\b|\bset\.seed\b|\.Random\.seed|\bmatch\.arg\b|\bdo\.call\b|"
    r"\bas\.integer\b|\bas\.character\b|\bas\.logical\b|\bunlist\b|\blapply\b|\bsapply\b|"
    r"\bvapply\b|\bcharacter\(0\)|\bmcmc\.list\b|"
    r"\bstopifnot\b|\bca\.jo\b|\bur\.df\b|\bur\.pp\b|\bugarchspec\b|\bdccspec\b|\bsvydesign\b"
)
TOOLCHAINS = (
    r"\brenv\b|\bRscript\b|\btestthat\b|\broxygen\b|\bplumber\b|\.Rprofile|\.lintr|"
    r"install\.packages|\bR CMD\b|\bCRAN\b|\b[Rr]-project|[Rr]-lib\.org|\bknitr\b|"
    r"\bRmd\b|\bvignette\b|\bDESCRIPTION file\b|\bref manual\b|\bhelp pages?\b|"
    r"\bssc install\b|\bStatalist\b|\b\.ado\b|"          # another ecosystem's
    r"\bMathWorks\b|\bSimulink\b|\bmexFunction\b|"        # and another's
    r"\bPkg\.add\b|\bjulia>\b|"                           # and another's
    r"\bPROC MEANS\b|\bPROC REG\b"                        # and another's
)
SYNTAX = (
    # a namespace call, but NOT a workflow command such as ::warning:: -- the
    # lookbehind rejects a match that itself begins after a colon. `pkg::fn` and
    # `foo::bar` are the GENERIC FORM the formula allowlist refuses, named in its
    # own refusal message and in the fixtures that prove it; they are
    # placeholders, not a real namespace, and are exempted below.
    #
    # `(?<!\.py)` IS WHAT KEEPS A PYTEST NODE ID OUT, and it is not a courtesy.
    # `tests/test_cli.py::test_list_prints_every_node_one_per_line` is pytest's
    # own selector syntax and this project's own vocabulary; the mutmut deselect
    # list in engine/pyproject.toml is twenty-one of them and cannot be written
    # in any other form. Silencing it by editing that list would damage the tree
    # to make a gate green, which is the failure recorded in the header above.
    #
    # IT IS ONE EDIT AND IT COSTS NOTHING ELSE. The guard is evaluated at the
    # `::`, so it does not matter where the scan started: whatever precedes the
    # colons is what it reads, and only a node ID has `.py` there. A real
    # namespace call keeps matching from any position, `.mypkg::somefn` included.
    # A draft of this line ALSO widened the leading lookbehind to `(?<![:\w.])`,
    # on the reasoning that the scan would otherwise restart at the `py`. It does
    # not, and measuring the four combinations is what showed it: the widening
    # suppressed no node ID the guard had not already suppressed, and it dropped
    # a namespace call written after a dot. It is not here.
    # `(?!(?:error|ignore|always|default|module|once)::)` KEEPS A PYTEST WARNING
    # FILTER OUT, on the same terms. A filterwarnings entry is
    # `action:message:category:module:lineno`, so
    # `"ignore::statsmodels.tools.sm_exceptions.ConvergenceWarning"` names a
    # Python exception class in pytest's own filter syntax -- this project's own
    # vocabulary, not another ecosystem's namespace, and the two suites in
    # c16_limited_dependent cannot write it in any other form. `filterwarnings =
    # ["error", ...]` in engine/pyproject.toml makes every warning fatal exactly
    # so that a wrapper permitted to provoke one says so on its own test;
    # deleting the mark to quiet this gate would delete that statement.
    # MEASURED RATHER THAN ASSERTED, so the next reader is told no more than was
    # checked: neutering both marks leaves `run_verifications.sh` green on
    # today's fixtures, so they are a standing permission for an optimiser that
    # may give up, not a suppression that is currently firing. Either way the
    # string is the suites' own vocabulary, which is what this rule turns on.
    #
    # THOSE SIX ACTIONS ARE PYTEST'S WHOLE SET, and the exemption is anchored to
    # the set rather than to "anything before a `::`", which would delete the
    # rule. It is checked at the START of the match, not at the `::` where the
    # `.py` guard sits, because an action word is variable-width and a Python
    # lookbehind is not -- one wide enough to read `default` back from the
    # colons would read the tail of `mydefault::somefn` too and exempt a real
    # namespace call. The leading `(?<![:\w])` is what makes the start position
    # sufficient: inside `ignore::` no later position can begin a match, so
    # there is nothing for the scan to restart on. A package name that merely
    # begins or ends with an action still fires, which ACTION_LIKE_NAMES below
    # asserts in both directions.
    r"(?<![:\w])(?!pkg::fn|foo::bar)"
    r"(?!(?:error|ignore|always|default|module|once)::)"
    r"[A-Za-z][A-Za-z0-9._]*(?<!\.py)::[A-Za-z_.]|"
    r"%>%|%in%|"
    # a leading-dot function name, the "internal function" convention of another
    # ecosystem. Anchored to a known engine-internal prefix so it cannot reach a
    # dotfile (`.github`, `.venv`) or a file suffix.
    r"(?<![\w./\"'-])\.(?:mcp_|node_|dcc_|adapt_|resolve_)[a-z_]+\b|"
    # a list accessor from another ecosystem: `fit$model`. Anchored to an
    # identifier on BOTH sides so a shell variable (`$s`, `${x}`) cannot match.
    r"\b[A-Za-z_][A-Za-z0-9_]*\$[a-z_][a-z0-9_]*\b|\bsprintf\(|"
    r"\.R(?![A-Za-z0-9_])|\.Rmd\b"
)
TRANSLATION = (
    r"\bported from\b|\ba port of\b|\btranslated from\b|"
    r"\breimplementation of\b|\bthe reference implementation of\b|engine/R/|\bWrappers/|"
    # phrases an earlier scrub left behind, which read as a scrub rather than as
    # prose: a blanket substitution produced "An the reference Package" inside two
    # real citation titles, and grammar that broken is more conspicuous than the
    # word it replaced.
    r"\bthe reference Package\b|\bthe reference engine\b|\bwritten in another language\b"
)
PATTERN = re.compile("|".join((LIBRARIES, TOOLCHAINS, SYNTAX, TRANSLATION)))

# TOOL CACHES, NOT SOURCE. Every entry is generated, gitignored and holds no
# prose anybody could fix; `.hypothesis` is the example database and constant
# pool hypothesis writes beside the suite, and it is here for the same reason
# `.pytest_cache` and `.ruff_cache` are. A cache is absent from a fresh clone,
# so this changes what a CONTRIBUTOR sees locally and nothing about what CI
# examines: the floor below is measured over tracked files and still applies.
SKIP_DIRS = (".git", ".venv", "__pycache__", ".mypy_cache", ".ruff_cache",
             ".pytest_cache", ".import_linter_cache", ".private", ".claude",
             ".fastembed_cache", ".token-optimizer", ".hypothesis", "node_modules")
SKIP_NAMES = ("todo.md", "CLAUDE.md")

exempt = [line.strip() for line in pathlib.Path(allowlist_path).read_text().splitlines()
          if line.strip() and not line.startswith("#")]


def is_exempt(rel: str) -> bool:
    return any(rel.startswith(e) for e in exempt)


GENERATED = ("engine/src/econflow_engine/wrappers/",
             "engine/src/econflow_engine/generated/")

examined = 0
findings = []
for path in sorted(pathlib.Path(".").rglob("*")):
    if not path.is_file():
        continue
    rel = str(path)
    if any(part in SKIP_DIRS for part in path.parts) or path.name in SKIP_NAMES:
        continue
    if is_exempt(rel):
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue  # binary: no prose to fix
    examined += 1
    hits = [(n, line) for n, line in enumerate(text.splitlines(), 1)
            if PATTERN.search(line)]
    if hits:
        findings.append((rel, hits))

# --- anti-vacuity 1: the floor -------------------------------------------
floor = int(json.loads(pathlib.Path(manifest_path).read_text())
            .get("vocabulary", {}).get("min_files_scanned", 0))
if floor <= 0:
    sys.exit("FAIL: no vocabulary.min_files_scanned in the manifest; "
             "a floor of zero is not a floor.")
if examined < floor:
    sys.exit(f"FAIL: examined {examined} files, below the floor {floor}. "
             "The scan is wrong, not the tree.")

# --- anti-vacuity 2: the positive controls -------------------------------
# ONE PER RULE FAMILY, EACH MATCHED ON ITS OWN. A single control string is
# satisfied by whichever rule fires first in it, so every other rule in this
# file could be narrowed to nothing and the control would still report success.
# The namespace rule carries its own line here because it HAS been narrowed --
# see `(?<!\.py)` above.
# EACH CONTROL MUST BE CATCHABLE BY ITS RULE ALONE. The namespace control names
# `mypkg`, which appears in no token list, precisely so that the namespace rule
# is the only thing that can match it. The first draft of this line used real
# library names -- and neutering the namespace rule to `ZZZNOMATCHZZZ::` left
# the gate reporting success, because `urca` matched the LIBRARIES rule before
# the namespace rule was ever reached. A control another rule can satisfy is not
# a control for the rule it was written for.
POSITIVE = (
    "this was ported from a package installed with install.packages, using set.seed",
    "the estimate comes from mypkg::somefn, which names another ecosystem's namespace",
)
undetected = [control for control in POSITIVE if not PATTERN.search(control)]
if undetected:
    sys.exit(f"FAIL: {len(undetected)} of {len(POSITIVE)} positive control(s) were NOT "
             f"detected; the token list is broken: {undetected}")

# --- anti-vacuity 3: the negative control --------------------------------
# Real mathematics, a real citation and a real author initial. If any of this
# fires, the token list has grown a rule that mathematics cannot survive.
NEGATIVE = (
    "the R-hat is 1.01, the pseudo R^2 is 0.8, and R*beta = q; the sf and cvm "
    "normality tests rank ahead of lillie; car and bhar aggregate the event "
    "window; the gbm and vasicek asset models differ; inference type np; "
    "Hyndman, R.J. and Tsay, R. and D'Agostino, R.B.; Blanchard-Quah 1989 AER; "
    "robust standard errors, the leverage effect, and a pivotal statistic; "
    "chown -R the engine; a listwise drop; Granger causality; NA is missing; "
    # pytest's own selector syntax, in the three shapes the tree writes it.
    "tests/test_cli.py::test_list_prints_every_node_one_per_line; "
    '"tests/conformance/test_conformance.py::test_the_harness_compares_something_today"; '
    "# tests/test_gates_primitives.py::test_in_range_blocks_a_non_number; "
    # pytest's own warning-filter syntax, as the c16 suites write it.
    '"ignore::statsmodels.tools.sm_exceptions.ConvergenceWarning"'
)

# --- anti-vacuity 4: the namespace rule still reaches past a dot ----------
# The one construct the rejected lookbehind widening would have lost. It is
# asserted rather than left to the token list, because nothing else in this file
# would have gone red when that widening was in place.
AFTER_A_DOT = "as in .mypkg::somefn, a namespace written straight after a dot"
if not PATTERN.search(AFTER_A_DOT):
    sys.exit("FAIL: a namespace call written after a dot was NOT detected; the "
             "leading lookbehind has been widened and the rule now has a blind spot.")
# --- anti-vacuity 4b: the filter-action exemption reaches no further ------
# The six actions are exempt; a package name that merely BEGINS or ENDS with one
# is not. The two directions are asserted SEPARATELY, for the reason the
# positive controls are: one string holding both is satisfied by whichever half
# matches first, so the exemption could widen in the other direction and this
# would still report success. Neither `ignored` nor `myonce` appears in any
# token list here, so nothing else in this file would go red if the exemption
# widened into `(?!\w+::)` and took the whole rule with it.
ACTION_LIKE_NAMES = (
    "as in ignored::somefn, a package name that only begins like an action",
    "as in myonce::somefn, a package name that only ends like an action",
)
unmatched = [name for name in ACTION_LIKE_NAMES if not PATTERN.search(name)]
if unmatched:
    sys.exit(f"FAIL: {len(unmatched)} namespace call(s) whose package merely "
             "begins or ends with a pytest filter action were NOT detected; the "
             f"filter-action exemption has widened past the six: {unmatched}")
flagged = [m.group(0) for m in PATTERN.finditer(NEGATIVE)]
if flagged:
    sys.exit("FAIL: the negative control was flagged on "
             f"{flagged}; mathematics must survive this gate.")

if findings:
    for rel, hits in findings:
        note = ""
        if rel.startswith(GENERATED):
            note = "   <- GENERATED: fix the text in engine/corpus/, then rebuild and reseal"
        print(f"BORROWED  {rel}{note}")
        for n, line in hits[:5]:
            print(f"    {n}:{line.strip()[:150]}")
    total = sum(len(h) for _, h in findings)
    print()
    print(f"FAIL: vocabulary from another ecosystem appears {total} time(s) in "
          f"{len(findings)} file(s), examined {examined}.", file=sys.stderr)
    print("Name the method, the object or the operation instead. If the token is "
          "MATHEMATICS or a person's name, it does not belong in the token list at "
          "all -- remove it there and record the reading that protects it, rather "
          "than adding a path to the allowlist.", file=sys.stderr)
    sys.exit(1)

print(f"ok: the vocabulary is this project's own "
      f"(examined {examined} files, floor {floor}, "
      f"{len(POSITIVE)} positive control(s) and 4 negative control(s) all fired).")
PY
