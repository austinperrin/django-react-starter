# Phase 5: Integrate Checks and Operations

[Docs](../../README.md) > [Roadmap](../README.md) > [Milestone 1](README.md) > Phase 5

## Goal and Prerequisites

**Goal:** Local tooling, CI, dependency maintenance, and runbooks cover the
delivered backend and frontend together.

**Prerequisites:** [Phase 3](phase-3-backend.md) and
[Phase 4](phase-4-frontend.md) supply working applications and checks.

## Development Checklist

- [ ] Add backend and frontend checks to the existing repository suite and CI.
- [ ] Extend Dependabot for the package managers selected in
  [Phase 2](phase-2-stack-decisions.md) after their manifests are introduced.
- [ ] Document clean setup, local start, migrations, tests, and build operations.
- [ ] Add local agent instructions for backend and frontend only where they
  specialize repository-wide guidance.

## Review Checklist

- [ ] Verify local and hosted checks on a pull request.
- [ ] Confirm required GitHub checks match actual job names and settings.
- [ ] Review dependency update coverage and operational instructions.

## Exit Criteria

- [ ] One documented command path verifies the repository and both applications.
- [ ] Hosted checks pass on the reviewed changes.

## Progress and Evidence

Planned. Link reviewed pull requests, runs, and settings evidence here.

## Related Documents

- [Milestone 1](README.md) - Outcome and phase order.
- [Repository checks](../../architecture/repository-checks.md) - Existing local checks.
- [Dependency maintenance](../../runbooks/dependency-maintenance.md) - Update procedure.
