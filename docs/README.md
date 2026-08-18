<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# `docs/`

Five documents. One carries the plan; four record decisions that were made once and should not be
re-litigated without reading why.

| Document | Answers |
|---|---|
| [`ROADMAP.md`](ROADMAP.md) | What is built, what is specified, and what has to happen |
| [`decisions/python-engine.md`](decisions/python-engine.md) | Why the compute engine is Python, and what enforces the boundary now that a file extension no longer does |
| [`decisions/repository-layout.md`](decisions/repository-layout.md) | One directory per layer, and why the public root surface is asserted in both directions |
| [`decisions/marketplace-apps.md`](decisions/marketplace-apps.md) | Which third-party analysis apps are enabled, and why none of them can ever be a required check |
| [`decisions/first-push.md`](decisions/first-push.md) | The publication sequence, in the order that does not deadlock the repository against itself |

## Where the rest lives

Documentation sits next to the thing it describes, not here:

| For | Read |
|---|---|
| The system as a whole | [`../ARCHITECTURE.md`](../ARCHITECTURE.md) — authoritative; where it and `ROADMAP.md` disagree, it wins |
| Changing the code | [`../CONTRIBUTING.md`](../CONTRIBUTING.md) |
| A layer | that layer's `README.md` — `engine/`, `backend/`, `frontend/`, `deploy/` |
| A method | its category guide, `engine/src/econflow_engine/wrappers/<category>/README.md` |
| CI | [`../.github/README.md`](../.github/README.md) |
| Why the artifacts are inputs rather than outputs | [`../engine/artifacts/PROVENANCE.md`](../engine/artifacts/PROVENANCE.md) |

## Adding a decision record

A record exists to stop a settled question being reopened from scratch. It states the decision, the
reasoning **with the measurement that produced it**, and the alternatives rejected with their
reasons — that last part is what makes it useful a year later, when the obvious-looking alternative
occurs to someone again.

A superseded record is marked at the top and kept. Deleting it deletes the reasoning, and the next
person then rediscovers the same dead end at the same cost.
