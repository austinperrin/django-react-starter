# Repository Roadmap

[Docs](../README.md) > Roadmap

Use this index as the project's schedule and progress view. The schedule records
milestone and phase ownership, estimates, dates, variance, and status. Milestone
pages define outcomes, dependencies, review steps, and completion evidence.
Issues and pull requests track individual changes.

## Schedule

Estimates are planning ranges for focused maintainer work, including
implementation, review, and verification. They are not delivery commitments or
measured durations. One week means five working days.

Use `YYYY-MM-DD` dates in the `America/Chicago` time zone. For an initialized
repository baseline, record the setup date as both Milestone 0 actual dates.
Use the first commit for each phase start and the closing pull request's merge
date for its end. When a phase
has no pull request, use its completion commit. Set planned dates when the owner
commits to a target. Use `TBD` for a future estimate or date that is still open;
use `Not recorded` when a historical value was never recorded.

### Status and Variance Legend

Use the same status text in this schedule and any milestone or phase progress
notes. Inline color helps in renderers that support it; the text remains
readable without styling.

| Status | Meaning |
| --- | --- |
| <span style="color: #6b7280;">Planned</span> | Scope is proposed, but work has not started. |
| <span style="color: #ca8a04;">In Progress</span> | The owner has started work and is tracking delivery. |
| <span style="color: #b91c1c;">Blocked</span> | A named dependency or decision prevents the next planned work. |
| <span style="color: green;">Completed</span> | The exit criteria are met, reviewed, and supported by evidence. |

| Variance | Meaning |
| --- | --- |
| TBD | No planned end date exists yet. |
| On track | Current work is expected to meet the planned end date. |
| At risk | The planned end date may be missed; record a recovery action. |
| Delayed | The planned end date passed and work remains incomplete. |
| Completed early / on time / late | Compare actual completion with the planned end date. |
| Not measured | A historical planned end date was not recorded. |

| Milestone | Stage / Phase | Owner | Estimate | Planned Start | Planned End | Actual Start | Actual End | Variance | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Milestone 0: Repository Scaffolding](milestone-0-repository-scaffolding.md) |  | Repository maintainers | 5–9 weeks | Not recorded | Not recorded | 2026-11-22 | 2026-11-22 | Not measured | <span style="color: green;">Completed</span> |
| [Milestone 1: Django and React starter](milestone-1-django-react-starter/README.md) |  | Repository maintainers | 3–5 weeks | TBD | TBD | TBD | TBD | TBD | <span style="color: #6b7280;">Planned</span> |
|  | [Phase 1: Own the starter identity](milestone-1-django-react-starter/phase-1-starter-identity.md) | Repository maintainers | 1–2 days | TBD | TBD | TBD | TBD | TBD | <span style="color: #6b7280;">Planned</span> |
|  | [Phase 2: Record stack decisions](milestone-1-django-react-starter/phase-2-stack-decisions.md) | Repository maintainers | 2–4 days | TBD | TBD | TBD | TBD | TBD | <span style="color: #6b7280;">Planned</span> |
|  | [Phase 3: Build the backend baseline](milestone-1-django-react-starter/phase-3-backend.md) | Repository maintainers | 3–5 days | TBD | TBD | TBD | TBD | TBD | <span style="color: #6b7280;">Planned</span> |
|  | [Phase 4: Build the frontend baseline](milestone-1-django-react-starter/phase-4-frontend.md) | Repository maintainers | 3–5 days | TBD | TBD | TBD | TBD | TBD | <span style="color: #6b7280;">Planned</span> |
|  | [Phase 5: Integrate checks and operations](milestone-1-django-react-starter/phase-5-integration.md) | Repository maintainers | 3–5 days | TBD | TBD | TBD | TBD | TBD | <span style="color: #6b7280;">Planned</span> |
|  | [Phase 6: Verify adoption](milestone-1-django-react-starter/phase-6-adoption.md) | Repository maintainers | 2–4 days | TBD | TBD | TBD | TBD | TBD | <span style="color: #6b7280;">Planned</span> |

Milestone rows summarize their phase work. Link each milestone and phase to its
owning page or section. Record the accountable owner in each row; assign an owner
before committing a delivery target.

## Delivery Rules

Follow the dependencies and exit criteria in the active milestone page. The
[milestone planning template](milestone-template.md) supplies readiness,
development, review, and handoff checklists. Keep work small enough for focused
pull requests, and link issues or pull requests when they exist.

To add a milestone, copy the planning template, define its outcome, owner,
dependencies, and phases, then register its rows in the schedule. Check the
[ADR index](../adr/README.md) for decisions the work depends on; a Proposed ADR
does not establish its outcome.

For a milestone with multiple phases, create `milestone-N-short-name/`. Use its
`README.md` for the milestone outcome, dependencies, phase index, and final
review. Put each phase plan in a separate `phase-N-short-name.md` in that
directory, starting from the [phase planning template](phase-template.md).
Link the milestone row to its `README.md` and each phase row to its phase page.
Keep owners, estimates, dates, variance, and status in this schedule; milestone
and phase pages link here for those values. A short milestone with one phase can
remain a single file. Keep the completed
[Milestone 0 record](milestone-0-repository-scaffolding.md) at its existing path.

Review active milestones at least weekly. Update the schedule when ownership,
dates, variance, or status changes. Record progress, blockers, scope changes,
schedule changes, and completion evidence in the milestone page. When a target
changes, record the old and new dates and the reason there. Do not assign a
variance that requires a planned end date when none exists.

Keep detailed requirements in their canonical standards and decisions. Link to
them from the milestone instead of copying their rules. Keep each phase page
focused on its own work, review, and exit criteria. Follow the
[documentation standard](../standards/documentation.md) for navigation and page
scope.

## Related Documents

- [Milestone planning template](milestone-template.md) - Reusable outcome, phase, and evidence structure.
- [Phase planning template](phase-template.md) - Focused work, review, and exit criteria for one phase.
- [Documentation hub](../README.md) - Repository documentation categories.
- [Architecture Decision Records (ADRs) index](../adr/README.md) - Decisions that inform milestone work.
