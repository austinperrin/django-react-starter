# Milestone 1: Django and React Starter

[Docs](../../README.md) > [Roadmap](../README.md) > Milestone 1

## Milestone Summary

- **Outcome:** A developer can copy this repository, initialize it as their own
  project, run a minimal Django REST Framework API and React/Vite application,
  and extend both under documented standards and working checks.
- **Owner and schedule:** [Roadmap schedule](../README.md#schedule).
- **Last review:** 2026-11-22.
- **Dependencies:** The completed [repository baseline](../milestone-0-repository-scaffolding.md),
  the [decision log](../../adr/README.md), and the
  [initialization runbook](../../runbooks/initialize-repository.md).
- **Scope:** Starter identity, stack decisions, backend and frontend structure,
  local development, automated checks, and a tested adoption path.

This milestone establishes a reusable application starting point. Domain models,
product UI, authentication, hosting, and production infrastructure require
project-specific decisions unless a later accepted decision adds them to this
starter's baseline.

## Milestone Readiness

- [x] The outcome and phase order are clear.
- [ ] Required decisions and dependencies are identified and reviewed.
- [x] Phase owners and reviewable work are identified in the roadmap grid.
- [x] Verification and exit criteria are defined before implementation starts.

## Phase Index

| Phase | Outcome |
| :--- | :--- |
| [Phase 1: Own the starter identity](phase-1-starter-identity.md) | The repository and reusable initialization flow identify this starter. |
| [Phase 2: Record stack decisions](phase-2-stack-decisions.md) | Required application choices are approved; adopter choices remain explicit. |
| [Phase 3: Build the backend baseline](phase-3-backend.md) | A minimal Django REST Framework API starts and passes backend checks. |
| [Phase 4: Build the frontend baseline](phase-4-frontend.md) | A React/Vite TypeScript app builds and communicates with the API locally. |
| [Phase 5: Integrate checks and operations](phase-5-integration.md) | Repository checks, dependency updates, and runbooks cover both applications. |
| [Phase 6: Verify adoption](phase-6-adoption.md) | A clean copy becomes an independent project and passes its own checks. |

## Progress and Changes

Phase 1 is in progress. The repository identity and Milestone 0 summary are in
place; the future adopter's initialization flow is under review. Phase 2 will
record decisions before packages or runtime configuration are introduced.

## Milestone Review and Handoff

- [ ] Every phase meets its exit criteria and has linked evidence.
- [ ] The reviewed pull requests are merged and applicable checks pass.
- [ ] Standards, ADRs, and documentation reflect delivered behavior.
- [ ] Accepted follow-ups have an owner and tracking destination.
- [ ] The [roadmap schedule](../README.md#schedule) records final dates and status.

## Related Documents

- [Roadmap index](../README.md) - Schedule and delivery rules.
- [Initialization runbook](../../runbooks/initialize-repository.md) - Current adoption procedure.
- [Architecture Decision Records (ADRs) index](../../adr/README.md) - Approved and open choices.
