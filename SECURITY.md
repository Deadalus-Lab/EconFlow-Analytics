<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# Security policy

## Reporting a vulnerability

**Do not open a public issue.** Use GitHub's private vulnerability reporting on this repository:
*Security → Report a vulnerability*. That opens a private channel visible only to the maintainers.

Please include what the issue is, how to reproduce it, and what an attacker gains. A minimal
reproducible example is worth more than a description.

You will get an acknowledgement within **7 days** and an assessment within **30 days**. If a fix is
warranted you will be credited in the release notes unless you would rather not be.

## Supported versions

The project has not yet cut its first release. Until `v0.1.0`, the supported version is the tip of
`main`. This section will name maintained release branches once there are any — an explicit gap
rather than an implied promise.

## Where the boundaries are

The engine's security model is described in full in [`ARCHITECTURE.md` §10](ARCHITECTURE.md).
The parts most likely to matter to a reporter:

| Boundary | Enforcement |
|---|---|
| **Network** | No wrapper makes a network call. Verified: **0 of 251**. A wrapper that reaches the network is a vulnerability, not a feature. |
| **Formula parsing** | User-supplied model formulae are parsed into a restricted syntax tree by a default-deny allowlist of permitted calls with a depth limit. They are never passed to `eval`, `exec` or a namespace-evaluating formula library. |
| **Path arguments** | File-path arguments pass a structural gate rejecting traversal, absolute paths, control characters and disallowed extensions. |
| **Function-name arguments** | Arguments naming a function to apply are restricted to a closed enumeration mapped internally to fixed callables — never resolved by name at runtime, and never through `getattr` on a user-supplied string. |
| **Deserialisation** | `pickle` is never used on any input. Tabular data crosses the boundary as Arrow or CSV, both of which are data-only formats that cannot carry executable content. |
| **Job isolation** | Every job runs in a container as an unprivileged user. |

### A limitation that closed, and the one that would replace it

**Closed.** This section previously recorded a limitation inherent to the formula interface: a string
such as `y ~ system(...)` is dangerous in *any* program that passes user input to a model-fitting
call, because the formula is evaluated in a live environment. That property belonged to the language,
not to a wrapper, and it could only be mitigated rather than removed.

Python has no equivalent built-in, and the engine's formula handling is a parser that produces a
restricted tree rather than an evaluator. The class of report that used to land here has no target.

**A new one is owed the moment a formula library is adopted.** `patsy` and `formulaic` both evaluate
formula terms **in a namespace supplied by the caller** — that is the feature, since it is what makes
`log(gdp)` and `C(region)` work. It is also a code-execution surface with a different shape from the previous:
narrower, because the namespace is explicit and can be constrained, and easier to get wrong, because
the default is to hand over the caller's own frame.

Neither is a dependency today. If either is admitted, this document owes a section before the change
merges, stating which namespace is passed, what is in it, and what happens to a term naming something
outside it. A reporter reading this file should be able to tell which regime is in force; until that
section exists, the answer is that no such library is present. See
[`docs/decisions/python-engine.md`](docs/decisions/python-engine.md).

## What is not a vulnerability here

- A gate refusing to compute. That is the system working; see `ARCHITECTURE.md` §6.2.
- A finding in a third-party package that the engine does not call. Those are tracked through the OSV
  scan in continuous integration.
- A scanner alert against the deliberate non-ASCII test fixtures or the generated artifacts, both of
  which trip entropy heuristics by design.

## Dependencies

The locked Python packages are scanned by OSV on every pull request. That job asserts the package
count **before** trusting a "0 vulnerabilities" verdict — a scan that silently covered nothing must
fail rather than report success.

Unlike the arrangement it replaces, the compute layer is now also covered by Dependabot: `pip` is a
supported ecosystem, so `.github/dependabot.yml` proposes lockfile updates and the OSV scan is no
longer the only vulnerability coverage the engine has. Both remain in place — the scan is the one
that runs per pull request and the one whose verdict is gated on a count.
