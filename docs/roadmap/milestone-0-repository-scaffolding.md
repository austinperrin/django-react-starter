# Milestone 0: Repository Scaffolding

[Docs](../README.md) > [Roadmap](README.md) > Milestone 0

- **Outcome:** Establish the repository's policies, documentation, decisions,
  tooling, automation, and maintenance procedures.
- **Owner and schedule:** [Roadmap schedule](README.md#schedule).
- **Status:** <span style="color: green;">Completed</span>
- **Target:** No recorded target.

This milestone records the completed repository baseline. Its estimate describes
the typical effort to establish these practices; its actual dates mark when this
baseline was initialized. [Milestone 1](milestone-1-django-react-starter/README.md)
builds the Django and React application baseline on it.

## Completed Scope

| Area | Result |
| :--- | :--- |
| Identity and file hygiene | The root README, license, reporting contacts, ownership guidance, editor settings, Git attributes, and exclusions are in place. |
| Documentation and decisions | The documentation hub, standards, and Architecture Decision Records (ADRs) provide navigation and record established and open choices. |
| Contribution and security | Contribution guidance, issue and pull request forms, security reporting, and the Code of Conduct are available. |
| Local and hosted checks | Developer helpers, repository checks, and GitHub workflows provide the initial validation paths. |
| Maintenance | Runbooks cover issue triage, dependencies, releases, credential exposure, and GitHub settings. |

## Verification and Handoff

Repository checks and workflow files are present. Verify hosted results and live
GitHub controls for this repository through the
[GitHub configuration runbook](../runbooks/configure-github.md); copied workflow
files alone do not activate settings. The [decision log](../adr/README.md)
records accepted and open choices for Milestone 1.

## Related Documents

- [Roadmap index](README.md) - Schedule and current project work.
- [Milestone 1](milestone-1-django-react-starter/README.md) - Django and React application baseline.
- [Documentation hub](../README.md) - Standards, decisions, and runbooks.
- [Repository settings](../architecture/repository-settings.md) - GitHub controls to verify.
