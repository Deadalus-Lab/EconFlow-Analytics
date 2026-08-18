# ============================================================
# Dockerfile — the EconFlow Analytics engine image.
#
# Packages the Python compute engine as a reproducible, self-proving image.
#
# BUILD CONTEXT IS THE REPOSITORY ROOT, not engine/. That is not a convenience:
# step 2a COPYs LICENSE, which the AGPL requires to accompany the binaries, and
# a context rooted at engine/ could not reach it. The workspace manifest and the
# single uv.lock also live at the root, for the reason in
# docs/decisions/python-engine.md. Hence `engine/` prefixes on the COPY
# *sources* and bare paths on the destinations, so the in-image layout is
# unchanged.
#
# ON THE ENTRYPOINT. There is no long-running HTTP router and no healthcheck for
# one. ARCHITECTURE.md §2 states that the engine is not a service: Galaxy starts
# a container per job, the container computes one node and exits. The default
# command is therefore the worker entrypoint, and a liveness probe against a
# process that is *supposed* to exit would report a fault every time the design
# worked.
#
# Multi-stage:
#   base    — python:3.12-slim (exact pin, matches .python-version) + the small
#             set of system libraries the scientific wheels actually need.
#             Nothing is compiled from source: manylinux wheels carry their own
#             native code, which is why this stage is small: manylinux wheels carry their own native code.
#   builder — `uv sync --locked` as a cache-friendly layer, then the source
#             tree, then the FULL test suite as a HARD BUILD GATE
#             (`run_verifications.sh` — image cannot build unless green).
#   runtime — copies only the validated environment + app (drops tests),
#             non-root, single-threaded linear algebra.
# ============================================================

ARG PYTHON_VERSION=3.12
ARG UV_VERSION=0.10.10

# ---------- base: interpreter + system libraries (shared by builder & runtime) ----------
FROM python:${PYTHON_VERSION}-slim AS base

# DETERMINISTIC LINEAR ALGEBRA. This is the direct sibling of the reference
# netlib BLAS pin the engine image carried, and it exists for the same measured
# reason: the optimised, multithreaded backend perturbs sensitive fits. NumPy
# and SciPy ship a threaded OpenBLAS inside their wheels, and its reduction
# order depends on how the work was split across threads -- so the same input
# can land on a different last bit from one run to the next on the SAME machine,
# with no code change and no seed change. Pinning every thread pool to one
# removes that source of variation, and it is what the suite below is validated
# against. THIS MUST BE PRESERVED. Removing it does not break the build; it
# quietly stops the numbers being reproducible, which is worse.
ENV OPENBLAS_NUM_THREADS=1 \
    OMP_NUM_THREADS=1 \
    MKL_NUM_THREADS=1 \
    NUMEXPR_NUM_THREADS=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# hadolint ignore=DL3008
RUN apt-get update && apt-get install -y --no-install-recommends \
        # linear programming and graph routines: the wheels for the optimisation
        # stack link libglpk at run time rather than vendoring it.
        libglpk40 \
        # arbitrary precision, used by the copula and dependence methods.
        libgmp10 libmpfr6 \
        # PID-1 init: reaps workers and forwards SIGTERM cleanly.
        tini \
    && rm -rf /var/lib/apt/lists/*

# ---------- builder: restore the locked environment, copy source, run the gate ----------
FROM base AS builder
ARG UV_VERSION
WORKDIR /app

# Byte-compile nothing on install and copy rather than hardlink, so the whole
# environment can be moved between stages as a plain directory.
ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=0 \
    UV_PYTHON_DOWNLOADS=never \
    VIRTUAL_ENV=/app/.venv

RUN pip install --no-cache-dir "uv==${UV_VERSION}"

# 1) MANIFESTS AND THE LOCK FIRST -> the sync is its own cached layer, which
#    survives source edits; only a manifest or lock change busts it.
#
#    There is ONE uv.lock and it sits at the repository root, because engine/ and
#    backend/ are two members of one uv workspace. uv must be able to LOAD every
#    member to honour that lock, which is why backend/pyproject.toml is copied
#    here even though no backend code ships in this image.
COPY pyproject.toml uv.lock ./
COPY engine/pyproject.toml engine/README.md engine/
COPY backend/pyproject.toml backend/README.md backend/
# The backend package is empty and ships anyway, at a cost of two files. Step 3
# of run_verifications.sh asserts "no statistic is ever computed outside
# engine/" via import-linter, and that contract names econflow_backend as a root
# package. Without the source, import-linter cannot build the graph and the gate
# reports a broken contract -- so the boundary would be proven everywhere except
# in the artifact that actually ships.
COPY backend/src/ backend/src/

# `--locked` refuses to re-resolve: if the lockfile does not already satisfy the
# manifests the build FAILS rather than quietly installing a different set.
# `--no-install-workspace` installs only third-party dependencies at this point,
# so the layer does not depend on our own source.
RUN uv sync --locked --all-extras --no-install-workspace

# 2) source tree (engine, generated tier, specs, tests, normative cards).
COPY engine/src/ engine/src/
COPY engine/scripts/ engine/scripts/
COPY engine/tests/ engine/tests/
# The committed contract fixtures ARE part of the suite: it regenerates them in
# memory and compares byte for byte. Without this COPY, step (3) below -- which
# is a HARD BUILD GATE -- fails inside the image with a missing-fixture message.
COPY engine/fixtures/ engine/fixtures/
COPY engine/artifacts/ engine/artifacts/
# The anti-vacuity floor for step 5 of run_verifications.sh. See .dockerignore:
# excluded wholesale with this one file re-admitted, because a floor that cannot
# be read is a floor that is not enforced.
COPY .github/inventory.json .github/
COPY engine/run_verifications.sh engine/ruff.toml engine/.python-version engine/
COPY engine/METHOD-SELECTION.md engine/METHOD-SELECTION.yaml \
     engine/METHOD-SELECTION-TREES.yaml engine/METHOD-SOURCES.json engine/

# 2a) DISTRIBUTION COMPLIANCE — must travel WITH the binaries, not just live in
#     the repo. The image ships third-party packages in binary form, so it has to
#     carry: the engine's own licence text (verbatim AGPL-3.0, which the licence
#     requires to accompany the binary), the attribution register, and the
#     written offer for corresponding source. Regenerate the last two with
#     `scripts/gen_third_party.py`; CI gates them against uv.lock.
COPY LICENSE ./
COPY engine/THIRD-PARTY-LICENSES.md engine/sbom.cdx.json engine/

# Install the engine itself, now that its source is present.
RUN uv sync --locked --all-extras

# 3) HARD BUILD GATE: the inviolable suite must pass INSIDE the image, under the
#    exact locked package set and the single-threaded backend above. Build fails
#    on any failure or error. An image that has not proven itself cannot exist.
WORKDIR /app/engine
RUN ./run_verifications.sh

# 4) drop test-only content HERE (in the builder) so it never enters the layer
#    runtime COPYs — a post-COPY rm only whiteouts, leaving the bytes in the
#    shipped image.
RUN rm -rf /app/engine/tests /app/engine/fixtures

# ---------- runtime: slim, non-root, one job per container ----------
FROM base AS runtime
WORKDIR /app

# compute-identity baked into the image → mixed into the node cache key
# (econflow_engine.node.cache) so a rebuild from changed code or dependencies
# invalidates the durable cache.
# Pass at build: --build-arg NODE_COMPUTE_VERSION=$(git rev-parse --short HEAD).
ARG NODE_COMPUTE_VERSION=dev
ENV NODE_COMPUTE_VERSION=${NODE_COMPUTE_VERSION}

# validated environment + app from the builder (already stripped of tests).
COPY --from=builder /app /app

# The environment is a plain virtualenv; putting it on PATH is all that is
# needed to run the engine without activating anything.
ENV PATH="/app/.venv/bin:${PATH}" \
    VIRTUAL_ENV=/app/.venv

# non-root execution (the app owns only its dir; nothing here needs root).
RUN useradd --create-home --uid 10001 appuser \
    && chown -the engine appuser:appuser /app
USER appuser

WORKDIR /app/engine

# NO HEALTHCHECK, DELIBERATELY. A healthcheck describes a process that is meant
# to stay up. This container computes one node and exits, so a liveness probe
# would report a fault precisely when the design is working.
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["python", "-m", "econflow_engine"]
