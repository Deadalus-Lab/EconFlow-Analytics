<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# Third-party licences — Python compute engine

**Generated file. Do not edit by hand.** Regenerate with:

```sh
uv sync --all-extras && uv run python engine/scripts/gen_third_party.py
```

This distribution bundles **34 Python packages**, plus CPython itself.
Every package remains under its own licence, held by its own authors. This project
wraps and gates them; it does not reimplement them.

## Corresponding source

Every package is pinned in `uv.lock` by exact name, version and artefact hash.
PyPI artefacts are immutable, so a version identifier is a byte identifier — there
is no dated-snapshot caveat here. Sources are
reachable per package at `https://pypi.org/project/<NAME>/`, and `uv sync --locked`
against the committed lockfile retrieves the identical artefacts on any machine.

## Licence distribution

| Licence | Packages |
|---|---:|
| MIT | 16 |
| BSD-3-Clause | 9 |
| not resolved on this platform | 2 |
| Apache-2.0 | 1 |
| Apache-2.0 OR BSD-2-Clause | 1 |
| BSD-2-Clause | 1 |
| BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0 | 1 |
| MPL-2.0 | 1 |
| MPL-2.0 AND (Apache-2.0 OR MIT) | 1 |
| PSF-2.0 | 1 |

Unmapped to an SPDX identifier: **0**. An unmapped entry is reported
rather than guessed — a plausible-looking identifier nobody verified is worse than
an honest gap.

Present in `uv.lock` but not installed on this platform, and therefore not in the
Linux image: **2** (marked † below). The lockfile is cross-platform;
the image is not.

## Compatibility

This project is **AGPL-3.0-only**. AGPL-3.0 is one-way compatible with the GPL-3
family and is **not** compatible with GPL-2.0-only. A dependency published under
GPL-2.0-only cannot be admitted to this tree.

No dependency in the current lockfile conflicts.

## Packages

| Package | Version | Licence |
|---|---|---|
| `annotated-types` | 0.8.0 | MIT |
| `ast-serialize` | 0.8.0 | MIT |
| `click` | 8.4.2 | BSD-3-Clause |
| `colorama` † | 0.4.6 | not resolved on this platform |
| `grimp` | 3.15 | BSD-3-Clause |
| `import-linter` | 2.13 | BSD-3-Clause |
| `iniconfig` | 2.3.0 | MIT |
| `librt` | 0.15.0 | MIT |
| `markdown-it-py` | 4.2.0 | MIT |
| `mdurl` | 0.1.2 | MIT |
| `mypy` | 2.3.1 | MIT |
| `mypy-extensions` | 1.1.0 | MIT |
| `numpy` | 2.5.2 | BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0 |
| `orjson` | 3.12.0 | MPL-2.0 AND (Apache-2.0 OR MIT) |
| `packaging` | 26.3 | Apache-2.0 OR BSD-2-Clause |
| `pandas` | 3.0.5 | BSD-3-Clause |
| `pandas-stubs` | 3.0.5.260730 | BSD-3-Clause |
| `pathspec` | 1.1.1 | MPL-2.0 |
| `patsy` | 1.0.2 | BSD-3-Clause |
| `pluggy` | 1.6.0 | MIT |
| `pyarrow` | 25.0.1 | Apache-2.0 |
| `pydantic` | 2.13.4 | MIT |
| `pydantic-core` | 2.46.4 | MIT |
| `pygments` | 2.20.0 | BSD-2-Clause |
| `pytest` | 9.1.1 | MIT |
| `python-dateutil` | 2.9.0.post0 | BSD-3-Clause |
| `rich` | 15.0.0 | MIT |
| `ruff` | 0.16.3 | MIT |
| `scipy` | 1.18.0 | BSD-3-Clause |
| `six` | 1.17.0 | MIT |
| `statsmodels` | 0.14.6 | BSD-3-Clause |
| `typing-extensions` | 4.16.0 | PSF-2.0 |
| `typing-inspection` | 0.4.4 | MIT |
| `tzdata` † | 2026.3 | not resolved on this platform |
