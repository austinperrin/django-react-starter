# Phase 2: Record Stack Decisions

[Docs](../../README.md) > [Roadmap](../README.md) > [Milestone 1](README.md) > Phase 2

## Goal and Prerequisites

**Goal:** Record the Django, Django REST Framework, React, Vite, and TypeScript
baseline and approve choices needed to run and verify it.

**Prerequisites:** [Phase 1](phase-1-starter-identity.md) identifies this
repository. Follow the [ADR standard](../../standards/architecture-decisions.md)
and [dependency standard](../../standards/dependencies.md).

## Development Checklist

- [ ] Record the stack, repository layout, supported runtime versions, package
  managers, and backend/frontend API boundary in an ADR.
- [ ] Resolve the development database and Django signing-key supply needed by
  the baseline; update the [secrets decision](../../adr/0002-secret-management.md)
  before implementing its mechanism.
- [ ] Identify which choices stay with adopters, including product models,
  authentication, hosting, and release versioning.
- [ ] Define dependency-resolution files and update coverage for both ecosystems.

## Review Checklist

- [ ] Check choices against current upstream documentation and support windows.
- [ ] Keep the ADR index aligned with approved and Proposed records.
- [ ] Review consequences for local setup, CI, and future adoption.

## Exit Criteria

- [ ] The baseline's required implementation choices are approved.
- [ ] Unresolved project choices are explicit and do not block baseline setup.

## Progress and Evidence

Planned. Link decisions and review evidence here.

## Related Documents

- [Milestone 1](README.md) - Outcome and phase order.
- [Architecture Decision Records (ADRs) index](../../adr/README.md) - Decision status.
- [Dependency management](../../standards/dependencies.md) - Selection and update rules.
