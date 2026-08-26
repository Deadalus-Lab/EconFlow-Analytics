# SPDX-License-Identifier: AGPL-3.0-only

# ============================================================
# Dockerfile — the EconFlow Analytics engine image.
#
# Packages the Python compute engine as a reproducible, self-proving image.
#
# BUILD CONTEXT IS THE REPOSITORY ROOT, not engine/. That is not a convenience:
# step 2a COPYs LICENSE, which the AGPL requires to accompany the binaries, and
# a context rooted at engine/ could not reach it. The workspace manifest and the
# single uv.lock also live at the root, because engine/ and backend/ are two
# members of ONE uv workspace and a workspace has exactly one lockfile. Hence
# `engine/` prefixes on the COPY *sources* and bare paths on the destinations,
# so the in-image layout is unchanged.
#
# ON THE ENTRYPOINT. There is no long-running HTTP router and no healthcheck for
# one. ARCHITECTURE.md §2 states that the engine is not a service: Galaxy starts
# a container per job, the container computes one node and exits. The default
# command is therefore the worker entrypoint, and a liveness probe against a
# process that is *supposed* to exit would report a fault every time the design
# worked.
#
# REPRODUCIBLE, AND MEASURED RATHER THAN CLAIMED. With SOURCE_DATE_EPOCH set and
# BuildKit's rewrite-timestamp exporter, two consecutive builds of this file
# produced BYTE-IDENTICAL OCI archives on 2026-08-20 -- 509893120 bytes,
# sha256 edcba98949d223369b05e79f54295a2fe628258d4163bdb8dcbe7f2793a8f5e4, both
# exporting manifest sha256:c6bb90d3fb74044596dfcb4afc905df5e455b360218ff7429cf65e2fbafd0bb4.
# The builder stage was rebuilt from scratch on both runs (--no-cache-filter=builder),
# so the agreement is not a cache artifact. Reproduce with:
#
#   export SOURCE_DATE_EPOCH=$(git log -1 --format=%ct)
#   docker buildx build --no-cache-filter=builder \
#     --output type=oci,dest=img.tar,rewrite-timestamp=true .
#
# Deriving the epoch from the commit is what makes it useful: the same commit
# builds the same bytes, and a stranger can check that claim without asking us.
# `--output type=docker` CANNOT be used for this -- BuildKit refuses
# rewrite-timestamp with the docker exporter ("conflicts with unpack"), and the
# image loaded into the local store is not reproducible.
#
# Multi-stage:
#   base    — python:3.12-slim, pinned BY DIGEST (see PYTHON_IMAGE_DIGEST) + the small
#             set of system libraries the scientific wheels actually need.
#             Nothing is compiled from source: manylinux wheels carry their own
#             native code, which is why this stage is small: manylinux wheels carry their own native code.
#   builder — `uv sync --locked` as a cache-friendly layer, then the source tree,
#             then the engine itself. It stops there.
#   test    — `run_verifications.sh` over that tree. Reached only by
#             `docker build --target test --no-cache .`, and depended on by no
#             other stage, so the default build path never enters it.
#   pruned  — drops the test-only content from the builder tree — the test tree
#             and the gate scripts, and the `dev` group behind them — so the
#             layer runtime copies never held it.
#   runtime — copies that pruned tree, non-root, single-threaded linear algebra.
#
# THE SUITE IS A PIPELINE GATE, NOT A BUILD GATE, AND THE REASON IS THE CACHE.
# A `RUN ./run_verifications.sh` on the default path can be satisfied from a
# cached layer, so it reports success having examined nothing — the exact failure
# this repository has hit six times, arriving here through the build cache rather
# than through a bad assertion. Docker's own guidance is to put tests in a
# separate stage invoked on demand and to run it with `--no-cache`. The guarantee
# therefore lives in `.github/workflows/engine-suite.yml`, whose `full` path runs
#
#   docker build --target test --no-cache .
#
# before it builds the runtime image at all. A green run there is a suite that
# demonstrably executed; a green `RUN` layer here never was.
# ============================================================

ARG PYTHON_VERSION=3.12
ARG UV_VERSION=0.10.10

# THE BASE IS PINNED BY DIGEST, AND THE TAG ALONE NEVER WAS. The comment at the
# top of this file called `python:3.12-slim` an exact pin; it is not. Docker Hub
# republishes that tag on every Debian security update, so glibc, and with it the
# libraries installed by the unpinned apt-get below, could move under an image
# whose whole claim is reproducibility. The `tag@digest` form keeps the tag
# readable and fixes the bytes. Resolved with:
#   docker inspect --format='{{index .RepoDigests 0}}' python:3.12-slim
ARG PYTHON_IMAGE_DIGEST=sha256:2c941e860699f878900b0edc2403613c234d4b32eda3cc9fa7036991a2a63c4a

# ---------- base: interpreter + system libraries (shared by builder & runtime) ----------
FROM python:${PYTHON_VERSION}-slim@${PYTHON_IMAGE_DIGEST} AS base

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
#
# PYTHONHASHSEED, TZ AND THE LOCALE BELONG HERE TOO, and their absence had a
# sharp edge: PYTHONHASHSEED reached the build only through run_verifications.sh
# at step 3, so the gate proved the numbers under a fixed seed and the image then
# shipped a CMD that ran under a random one. The base stage is inherited by both
# builder and runtime, so declaring them here closes that gap in one place.
ENV OPENBLAS_NUM_THREADS=1 \
    OMP_NUM_THREADS=1 \
    MKL_NUM_THREADS=1 \
    NUMEXPR_NUM_THREADS=1 \
    PYTHONHASHSEED=0 \
    TZ=UTC \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
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
COPY engine/pyproject.toml engine/
COPY backend/pyproject.toml backend/
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
COPY engine/artifacts/ engine/artifacts/
# THE CORPUS IS AN INPUT TO THE SUITE THE `test` STAGE RUNS, not documentation. gen_artifacts.py
# rebuilds the v2 artifacts from engine/corpus/ and tests/test_gen_artifacts.py
# rebuilds the v1 pair from it as the roundtrip proof. Without this COPY the suite
# inside the image fails with FileNotFoundError on corpus/23-real-time-revisions.json
# -- measured, 3 failures and 14 collection errors -- while the host suite is green,
# which is the worst way to find out. check-dockerfile-paths.sh cannot catch it: that
# gate proves no COPY source is stale, never that a needed path was copied at all.
COPY engine/corpus/ engine/corpus/
# The anti-vacuity floor for step 5 of run_verifications.sh. See .dockerignore:
# excluded wholesale with this one file re-admitted, because a floor that cannot
# be read is a floor that is not enforced.
COPY .github/inventory.json .github/
# STEPS 9 AND 10 ARE THESE TWO SCRIPTS. run_verifications.sh shells out to them
# by path, so neither step exists inside the image unless the file does. Measured
# on 2026-08-22 without them: bash exits 127, `|| fail` fires, and the build dies
# printing "FAIL: a wrapper reaches the network; fetching belongs to the
# external-data node" -- a message accusing the wrapper tree of a network call
# when the real cause is an uncopied file, and step 10 never runs at all.
# check-dockerfile-paths.sh cannot catch this class: it proves no COPY source is
# stale, never that a needed path was copied.
#
# Neither script needs anything the image does not already hold.
# check-no-network.sh parses engine/src/econflow_engine/wrappers and takes its
# floor from the manifest above; assert.sh re-measures engine/ against that same
# manifest, reading engine/tests, engine/artifacts and the workspace uv.lock --
# all present here, and all still present when step 3 runs the gate, which is
# what makes step 4 free to delete them afterwards.
COPY .github/scripts/check-no-network.sh .github/scripts/
COPY .github/actions/assert-inventory/assert.sh .github/actions/assert-inventory/
COPY engine/run_verifications.sh engine/ruff.toml engine/.python-version engine/
COPY engine/METHOD-SOURCES.json engine/
# Step 8 of run_verifications.sh compares the 913 public wrapper signatures against
# this committed baseline. Without it in the context, `--target test` fails inside
# the image with a missing-baseline message, which reads like a broken gate rather
# than a missing file.
COPY engine/api-baseline/ engine/api-baseline/

# 2a) DISTRIBUTION COMPLIANCE — must travel WITH the binaries, not just live in
#     the repo. The image ships third-party packages in binary form, so it carries
#     the engine's own licence text (verbatim AGPL-3.0, which the licence requires
#     to accompany the binary) and the CycloneDX SBOM that names every shipped
#     package and its licence. Regenerate the SBOM with
#     `scripts/gen_third_party.py`; CI gates it against uv.lock.
#
#     THE ATTRIBUTION REGISTER IS NOT IN THIS IMAGE, and that is a gap rather
#     than a decision this file can close: engine/THIRD-PARTY-LICENSES.md is no
#     longer in the tree, so there is nothing to copy. The SBOM records which
#     licences apply; it is not the verbatim text those licences require.
COPY LICENSE ./
COPY engine/sbom.cdx.json engine/

# Install the engine itself, now that its source is present.
RUN uv sync --locked --all-extras

# ---------- test: the suite, under the locked package set, on demand ----------
# THE AUTHORITATIVE RUN OF THE SUITE, because here the numerical backend is fixed
# rather than whatever OpenBLAS a runner's NumPy wheel happens to carry. Nothing
# depends on this stage, so `docker build .` skips it entirely; the pipeline
# reaches it explicitly:
#
#   docker build --target test --no-cache .
#
# `--no-cache` is not decoration. Without it this RUN is satisfied from a cached
# layer whenever the inputs hash the same, and a test that did not execute
# reports success — which is the one thing this repository refuses everywhere.
FROM builder AS test

# README.md IS A TEST INPUT AND NOTHING ELSE, WHICH IS WHY IT ARRIVES HERE AND
# NOT IN THE BUILDER. The published "Methods carrying an implementation" row
# states the definition of an implemented body as a shell one-liner, and
# tests/test_stub_definition.py runs that line against the same tree the module
# walks, so the two spellings cannot drift apart unnoticed. That test needs the
# file. Measured 2026-08-26: with it absent this stage failed on
# `FileNotFoundError: '/app/README.md'` while the suite passed outside the image,
# because the run at the foot of this stage reads a tree assembled by COPY rather
# than the working tree. Copying it in the builder would carry a published
# document into the runtime image, which ships an engine and not its prose.
COPY README.md ./

WORKDIR /app/engine
RUN ./run_verifications.sh

# ---------- pruned: the builder tree with test-only content removed ----------
# SEPARATE STAGE, AND IT IS NOT COSMETIC. The removal has to happen in a stage
# runtime COPYs FROM — a post-COPY rm only whiteouts, leaving the bytes in the
# shipped image. It cannot sit in `builder` either, because `test` derives from
# builder and needs the tree this deletes. The two gate scripts go with it:
# nothing in the runtime image runs them. The manifest stays, as it always has.
#
# THE GATE TOOLCHAIN IS TEST-ONLY CONTENT TOO, and it is the larger half of what
# this stage drops. A member's `dev` group is a DEFAULT group of this workspace
# (engine/pyproject.toml says so, and uv 0.10.10 was measured doing it), so the
# syncs above install pyright, mutmut, hypothesis, deptry, griffe and interrogate
# alongside the seven runtime distributions. `pyright[nodejs]` alone carries a
# bundled Node runtime: 196699645 bytes, measured with `du -sb` inside the image.
# None of it is reachable from econflow_engine -- all 768 modules import in the
# runtime image without it -- so removing it is a deletion rather than a trade.
#
# `--no-dev` is an alias of `--no-group dev`, and a bare `uv sync` removes
# extraneous packages unless `--inexact` is passed, so this re-states the
# environment WITHOUT that group and uv uninstalls the difference. Same lock and
# the same `--locked` refusal to re-resolve as the syncs above: it narrows the
# installed set, it never chooses a different version of anything.
#
# IT BELONGS HERE AND NOT ON EITHER SYNC ABOVE. `test` derives from `builder`,
# and run_verifications.sh needs every one of those tools, so dropping the group
# earlier would strip the suite of the gates it IS. This stage is the one place
# the shipped tree may diverge from the tested tree.
FROM builder AS pruned
RUN rm -rf /app/engine/tests /app/engine/api-baseline /app/engine/corpus \
           /app/.github/scripts /app/.github/actions \
    && uv sync --locked --all-extras --no-dev

# ---------- runtime: slim, non-root, one job per container ----------
FROM base AS runtime
WORKDIR /app

# compute-identity baked into the image → mixed into the node cache key
# (econflow_engine.node.cache) so a rebuild from changed code or dependencies
# invalidates the durable cache.
# Pass at build: --build-arg NODE_COMPUTE_VERSION=$(git rev-parse --short HEAD).
ARG NODE_COMPUTE_VERSION=dev
ENV NODE_COMPUTE_VERSION=${NODE_COMPUTE_VERSION}

# non-root execution (the app owns only its dir; nothing here needs root). The
# account is created BEFORE the tree arrives so that the COPY below can set
# ownership as it writes.
RUN useradd --create-home --uid 10001 appuser

# environment + app from the pruned builder tree (already stripped of tests).
#
# `--chown` ON THE COPY, NOT A `chown --recursive` AFTER IT, AND THE REASON IS
# THE LAYER. Changing the owner of a file rewrites it into the layer being built,
# so a recursive chown over a freshly copied tree emits a SECOND copy of every
# byte and the image then ships both. Measured on this tree: the COPY layer and
# the chown layer were 547 MB each, one whole duplicate of /app, and
# `docker image inspect --format '{{.Size}}'` counts layers rather than the
# flattened filesystem -- so the duplicate is charged in full. Setting ownership
# during the copy leaves one layer holding one copy.
COPY --from=pruned --chown=appuser:appuser /app /app

# The environment is a plain virtualenv; putting it on PATH is all that is
# needed to run the engine without activating anything.
ENV PATH="/app/.venv/bin:${PATH}" \
    VIRTUAL_ENV=/app/.venv

USER appuser

WORKDIR /app/engine

# NO HEALTHCHECK, DELIBERATELY. A healthcheck describes a process that is meant
# to stay up. This container computes one node and exits, so a liveness probe
# would report a fault precisely when the design is working.
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["python", "-m", "econflow_engine"]
