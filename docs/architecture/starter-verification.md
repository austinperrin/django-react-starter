# Starter Repository Verification

[Docs](../README.md) > [Architecture](README.md) > Starter Repository Verification

This record captures evidence for `austinperrin/django-react-starter` as of
2026-11-22. The [repository settings checklist](repository-settings.md) owns the
required controls. A project copied from this starter must verify its own
settings and checks; the [initialization runbook](../runbooks/initialize-repository.md)
removes this source-repository record during project setup.

## Target and Review Policy

The repository is a public GitHub template with `main` as its default branch.
The active [Main branch review and checks ruleset](https://github.com/austinperrin/django-react-starter/rules/27813952)
targets `main` and has no bypass actors. Its current rules require pull requests,
resolved review conversations, an up-to-date branch, and the four checks in the
[settings checklist](repository-settings.md#required-pull-request-checks). It
blocks deletion and force pushes and allows squash merges only. The required
approval count is zero for this single-maintainer repository; CODEOWNERS has no
active mappings.

Repository settings allow squash merging only, use the pull request title for
the squash commit, and delete merged branches. The ruleset and merge settings
were read from this repository on 2026-11-22; copied workflow files were not
treated as proof of those settings.

## Observed Results

| Area | Evidence |
| :--- | :--- |
| Pull request checks | [PR #1](https://github.com/austinperrin/django-react-starter/pull/1) passed the Linux and macOS repository jobs and the Linux external-check job in its [final repository-check run](https://github.com/austinperrin/django-react-starter/actions/runs/44956401057). The [title-check run](https://github.com/austinperrin/django-react-starter/actions/runs/44957014193) passed. |
| Default branch | The [main-branch run](https://github.com/austinperrin/django-react-starter/actions/runs/44957376618) passed all three repository-check jobs after PR #1 merged. Each job's checkout-cleanliness step passed. |
| Invalid pull request title | An [invalid title failed](https://github.com/austinperrin/django-react-starter/actions/runs/44956834828); restoring the valid title [passed](https://github.com/austinperrin/django-react-starter/actions/runs/44956864850). PR #1 recorded that the invalid title blocked merging. |
| Credential scan | A [manual default-branch run](https://github.com/austinperrin/django-react-starter/actions/runs/44956917682) passed full-history checkout, scanner installation, redacted scanning, and checkout cleanliness. |
| Dependabot | The [initial GitHub Actions update job](https://github.com/austinperrin/django-react-starter/actions/runs/44926616855) succeeded. An applicable update pull request has not been observed in this repository. |

The [PR #1 review record](https://github.com/austinperrin/django-react-starter/pull/1)
also reports read-only default workflow tokens, an action allowlist requiring
full SHA pins, enabled Dependabot alerts and security updates, and a monitored
email fallback for private security reports. Those settings were recorded during
that review; the connected GitHub API did not expose their current settings for
an independent recheck on 2026-11-22.

## Remaining Verification

- Observe this repository's first scheduled credential-scan event. The manual
  dispatch above verifies the workflow path, not schedule activation.
- Test a pull request from an external fork and record its workflow approval and
  required-check behavior.
- Inspect the title, checks, and review path of the first applicable Dependabot
  update pull request.
These cases remain open until observed. Record later results here without
claiming that the inherited scaffold's runs verified this repository.

## Related Documents

- [Repository settings and verification](repository-settings.md) - Required controls and evidence.
- [CI workflows and enforcement](ci-cd.md) - Jobs and activation boundaries.
- [Phase 1 starter identity](../roadmap/milestone-1-django-react-starter/phase-1-starter-identity.md) - Current project progress.
- [GitHub configuration runbook](../runbooks/configure-github.md) - Live setup and review procedure.
