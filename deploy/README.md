<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# `deploy/`

**Specified. Not built.** This directory holds one README on purpose. Nothing here has been written,
and nothing here has been run.

Compose is the deployment path. Everything needed to stand the system up on one host will live here,
and the reasoning behind each file lives in [`../ARCHITECTURE.md`](../ARCHITECTURE.md).

## What will be here

| Path | Contents |
|---|---|
| `images.lock` | Every image the system uses, mapped to an immutable digest. One file, one truth, one diff |
| `compose.yml` | Platform web processes, job handlers and workers; PostgreSQL; the broker; the canvas assets; the proxy |
| `compose.e2e.yml` | The same stack with an explicit memory limit on every service, for the end-to-end run |
| `.env.example` | Every variable the stack reads. All configuration lives in one `.env`; no secret lives in `compose.yml` |
| `proxy/` | Three route classes: canvas assets, the REST API, and the event stream |
| `preflight.sh` | Refuses to start below the measured hardware floor, quoting the measured number |
| `backup.sh` / `restore.sh` | One timestamped bundle with a manifest; restore targets an **empty** host |
| `collect-diagnostics.sh` | A support bundle — versions, digests, health, recent job logs, redacted configuration |

## Three things that are decided, and are easy to undo by accident

**The event-stream route must not be buffered.** `proxy_buffering off`, **`gzip off`**, HTTP/1.1, a
long read timeout, and honour `X-Accel-Buffering: no`. Gzip is the one people forget, and it buffers
regardless of the buffering setting. The test that proves this has a negative control: the same test
must go red against a buffering-enabled configuration, or it is passing for a reason nobody has
identified.

**Every service gets a healthcheck that tests a real endpoint, never `true`.** A healthcheck that
always passes makes the stack report healthy when it cannot serve a request.

**The engine container is the exception, and its absent healthcheck is the design.** It is not a
service. It computes one node and exits, so a liveness probe would report a fault precisely when the
design is working. Adding one is a misreading of the architecture, not an oversight.

## What is deliberately *not* here

**The engine `Dockerfile` lives at the repository root, not in this directory.** The build context
has to be the repository root for two reasons, and neither is cosmetic. The image `COPY`s `LICENSE` —
the AGPL requires the licence text to accompany the binaries — and it `COPY`s the workspace
`pyproject.toml` and the single `uv.lock`, both of which are root files because `engine/` and
`backend/` are two members of one `uv` workspace. Docker cannot reach outside its context. Moving the
Dockerfile here without moving the context would break all three; moving the context would break the
licence copy and the lockfile restore at once.

**Kubernetes and configuration-management roles are unsupported at v1** — not "not yet",
*unsupported*. Each supported path is a maintenance commitment, and the upstream chart pins its own
application version, which is a second upgrade cadence to track alongside ours.

## Deployment release checklist

These are the release steps no workflow performs, kept here because the only place a manual step can
live is a list someone reads.

- [ ] **Flip the container package to public** on the first publish. A first publish is private, and
      a private image makes anonymous pulls — and therefore third-party reproduction — impossible.
      Prove it with `docker logout && docker pull …@sha256:<digest>`.
- [ ] **Run `scripts/verify-release.sh` on a machine that did not build the image.** Pull by digest,
      verify both attestations, run the suite inside the image, re-run the inventory assertion
      against the image's contents.
- [ ] **Re-measure the hardware floor against the exact released digests.** The floor moves whenever
      the image, the platform version or the resource allocations move — which is every release.
- [ ] **Confirm `images.lock` re-resolves.** Every digest still points where it did, or the change is
      understood before it ships.
- [ ] **Confirm a restore drill inside the last thirty days.** A backup that has never been restored
      is not a backup.

## Why it does not exist yet

It depends on decisions that are open: which platform release line is pinned (`U8`), the object
store (`U16`), the broker (`U17`), the resource allocations (`U15`), and the measured hardware floor
(`U65`). The registry (`U60`), the supported paths (`U61`), the proxy definition (`U62`), backup
(`U63`) and observability (`U64`) are settled by Phase 7 itself.

Arrives in **Phase 7** of [`docs/ROADMAP.md`](../docs/ROADMAP.md).
