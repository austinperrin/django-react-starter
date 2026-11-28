# ADR-0005: Django and React Application Baseline

[Docs](../README.md) > [ADR](README.md) > ADR-0005

* **Status**: Proposed
* **Date**: 2026-11-24
* **Authors**: @austinperrin
* **Deciders**: @austinperrin

## 1. Context and Problem Statement

The project plans a Django REST Framework API and React/Vite TypeScript
frontend. It needs a directory layout, supported runtime lines,
dependency-resolution tools, and a local API boundary before application files
are added. These choices must work in a clean checkout and remain understandable
as the application grows.

This record covers the application baseline. The development database and Django
signing-key supply are reviewed with the [secrets decision](0002-secret-management.md)
before backend configuration is implemented. Product models, authentication,
hosting, and release versioning remain project-specific choices.

## 2. Decision Drivers

- Keep the backend and frontend independently understandable while enabling one
  repository check path.
- Leave room for additional services without moving the initial applications.
- Use upstream-supported runtime and framework combinations, with a clear update
  path and documented minimum versions.
- Commit resolved dependency metadata so a clean checkout can reproduce installs.
- Let the browser reach a minimal API locally without embedding a deployment
  provider or relaxing cross-origin policy for every environment.
- Keep configuration changes localized as the project evolves.

## 3. Considered Options

### Repository Layout and API Boundary

| Option | Use case | Pros | Cons and responsibilities |
| :--- | :--- | :--- | :--- |
| **A. `services/backend/` and `services/frontend/` in one repository**, with a Django `/api/` JSON route and a Vite development proxy | A project that may add more independently runnable services | Keeps each service's code and dependencies together; frontend can use a relative API path locally; production deployment stays open | Two runtimes and development processes; production routing needs a later decision |
| **B. Root-level `backend/` and `frontend/` directories** | A project expecting only these two applications | Shorter paths and simple initial navigation | More top-level application directories as the repository grows; reorganizing them later changes paths and tooling |
| **C. Build the frontend into Django-served static assets** | A project that prefers one deployable application | One origin and deployment unit | Couples frontend builds to backend packaging and chooses a deployment shape before requirements are known |
| **D. Keep backend and frontend in separate repositories** | Teams with independent release and ownership cycles | Independent access and release controls | Complicates integrated setup and checks for this project |

The project places its initial applications under `services/` so additional
services can join the repository without moving them. Add shared packages or
workspace tooling only when concrete reuse or coordination requires them.

[Vite's proxy configuration](https://vite.dev/config/server-options#server-proxy)
supports forwarding a local `/api/` path to the backend. It is a development
feature; a project must choose its production routing and security controls.

### Runtime Lines

Python 3.14 is a candidate supported by both Django lines below and Django REST
Framework. The Django and Node.js choices are independent; selecting one row
does not select another.

| Component and option | Use case | Pros | Cons and responsibilities |
| :--- | :--- | :--- | :--- |
| **Django 6.1** | A current supported feature release | Django REST Framework lists it as supported | Extended support ends in December 2027; plan an upgrade sooner |
| **Django 5.2 LTS** | A longer support window | Extended support runs through April 2028 | Starts behind the current Django feature release |
| **Node.js 26 LTS** | A current LTS line | Longer remaining support window | Newer runtime; test Vite, plugins, and installation on target systems |
| **Node.js 24 LTS** | An established LTS line | More time for packages to have adopted it | Shorter remaining support window; plan a later runtime upgrade |

The [Django support schedule](https://www.djangoproject.com/download/),
[Django REST Framework compatibility list](https://www.django-rest-framework.org/),
and [Node.js release schedule](https://nodejs.org/en/about/previous-releases)
support this comparison as of the record date. Vite's
[Node.js requirement](https://vite.dev/guide/#compatibility-note) sets a minimum;
the chosen LTS line and exact package versions still need a clean-install test.
Use current patch releases within approved lines rather than freezing the
example numbers in this ADR.

### Dependency Resolution

Choose one Python resolver and one frontend package manager. Their selections
are independent.

| Component and option | Use case | Pros | Cons and responsibilities |
| :--- | :--- | :--- | :--- |
| **Python: `uv` with `pyproject.toml` and `uv.lock`** | A lockfile-managed application | Cross-platform resolution and locked verification with `uv sync --locked` | Extra local prerequisite; lockfile is specific to `uv` |
| **Python: `pip-tools` with input and compiled requirements files** | Teams that want pip-compatible resolved requirements | Uses pip's installation path and a committed resolution file | Extra compile tool; input and output files need coordinated updates |
| **Frontend: npm with `package.json` and `package-lock.json`** | Familiar Node.js tooling | Included with Node.js; `npm ci` verifies a clean locked install | Lockfile and package-manager version need maintenance |
| **Frontend: pnpm with its supported lockfile** | Teams already standardized on pnpm | Locked resolution with its own installation workflow | Adds a package-manager prerequisite for contributors |

The [uv project documentation](https://docs.astral.sh/uv/concepts/projects/layout/)
describes its lockfile, and [npm's clean-install documentation](https://docs.npmjs.com/cli/commands/npm-ci/)
describes the committed lockfile requirement. Follow the
[dependency standard](../standards/dependencies.md) for pins, update review, and
CI coverage once the tools are selected.

## 4. Decision Outcome

**Pending.** Django REST Framework and React/Vite TypeScript are the planned
application stack. The project has selected `services/backend/` and
`services/frontend/` for the initial layout. The `/api/` path and Vite proxy in
Option A remain proposals. Review the runtime lines, package managers, and API
boundary, then record the full rationale and declined alternatives before
accepting this ADR. Record exact supported versions and committed lockfiles
with the implementation.

## 5. Consequences and Trade-offs

- **Expected benefits**: A documented, testable baseline with explicit component
  boundaries and reproducible dependency resolution.
- **Pending costs**: Maintaining two runtimes, reviewing upstream support windows,
  and keeping both lockfiles and CI jobs current.
- **Reconsideration triggers**: A supported-line end date, incompatible package
  requirements, or a project need for a different deployment or API boundary.

## 6. Implementation and Verification

After approval, implement the backend, frontend, and integrated checks in
reviewable changes tracked by the [roadmap](../roadmap/README.md). The
implementation PRs must verify clean installs, local API access, and the
dependency and runtime versions they actually include. No application package
or runtime mechanism is authorized by this Proposed record alone.

## Related Documents

- [Architecture Decision Records (ADRs) index](README.md) - Decision status.
- [Roadmap](../roadmap/README.md) - Implementation progress and verification.
- [Secret Management](0002-secret-management.md) - Configuration and credential choices.
- [Dependency management](../standards/dependencies.md) - Package evaluation and update rules.
