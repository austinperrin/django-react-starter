# Phase 1: Own the Starter Identity

[Docs](../../README.md) > [Roadmap](../README.md) > [Milestone 1](README.md) > Phase 1

## Goal and Prerequisites

**Goal:** The repository identifies itself as the Django and React starter, and
its initialization flow can later initialize a project copied from this starter.

**Prerequisites:** Review the [initialization runbook](../../runbooks/initialize-repository.md)
and [helper](../../../scripts/dev/initialize-project.py) together. They guide
future adopters through project setup and remove themselves during cleanup.

## Development Checklist

- [x] Replace source-repository links in active GitHub forms and describe this
  starter in the root README; keep reporting contacts monitored.
- [x] Collapse the copied Milestone 0 phase history into a concise record of
  this repository's setup.
- [x] Replace source-only verification evidence with results from this repository.
- [x] Adapt the initializer and its tests to the new roadmap layout so a future
  copy uses this starter as its source and removes starter-only material without
  losing project standards.
- [x] Verify this repository's GitHub ruleset and merge settings separately from
  copied workflow files, and record the available hosted-check evidence.

## Review Checklist

- [x] Inspect source identity references and intentional historical attribution.
- [x] Run documentation, link, initializer, and applicable repository checks.
- [x] Review the future adopter's preview without applying it to this starter.

## Exit Criteria

- [x] Active links and identity point to this repository.
- [x] The future adopter's initialization procedure is preserved and can be
  previewed.

## Progress and Evidence

Completed. The root README and active GitHub links identify this starter.
Milestone 0 has a concise baseline record, and the initializer handles its
roadmap conversion in a future project copy. The
[starter verification record](../../architecture/starter-verification.md) captures
the current ruleset and merge settings, prior hosted runs, and cases still to
observe. The local repository suite passed on 2026-11-22: 36 developer tests,
64 CI tests (five external-tool integration tests skipped), and 13 operations
tests. A disposable project copy produced the expected cleanup preview without
applying it to this starter. [PR #2](https://github.com/austinperrin/django-react-starter/pull/2)
merged on 2026-11-24 after the Linux, macOS, external, and pull request title
checks passed. The [roadmap schedule](../README.md#schedule) records the closing
date. The starter verification record tracks later scheduled, fork, and
Dependabot observations separately.

## Related Documents

- [Milestone 1](README.md) - Outcome and phase order.
- [Starter repository verification](../../architecture/starter-verification.md) - Live controls and hosted evidence.
- [Initialization runbook](../../runbooks/initialize-repository.md) - Reusable setup procedure.
- [Roadmap index](../README.md) - Schedule and status.
