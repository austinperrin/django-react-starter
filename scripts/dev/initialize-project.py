"""Preview or apply the one-time GitHub project initialization changes."""

import argparse
from datetime import datetime
import os
from pathlib import Path
import re
import subprocess
import sys
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[2]
SOURCE_REPOSITORY = 'austinperrin/django-react-starter'
SOURCE_ALIASES = (SOURCE_REPOSITORY, 'austinperrin/scaffolding', 'austinperrin/base')
SOURCE_URL = f'https://github.com/{SOURCE_REPOSITORY}'
SOURCE_EMAIL = 'perrinaustin@gmail.com'

URL_FILES = {
  '.github/ISSUE_TEMPLATE/config.yml': 1,
}
EMAIL_FILES = ('SECURITY.md', 'CODE_OF_CONDUCT.md')
PROJECT_MILESTONE_PATH = 'docs/roadmap/milestone-1-django-react-baseline.md'
REMOVALS = (
  'docs/architecture/starter-verification.md',
  'docs/roadmap/milestone-1-django-react-starter/README.md',
  'docs/roadmap/milestone-1-django-react-starter/phase-1-starter-identity.md',
  'docs/roadmap/milestone-1-django-react-starter/phase-2-stack-decisions.md',
  'docs/roadmap/milestone-1-django-react-starter/phase-3-backend.md',
  'docs/roadmap/milestone-1-django-react-starter/phase-4-frontend.md',
  'docs/roadmap/milestone-1-django-react-starter/phase-5-integration.md',
  'docs/roadmap/milestone-1-django-react-starter/phase-6-adoption.md',
  'docs/runbooks/initialize-repository.md',
  'scripts/dev/initialize-project.py',
  'scripts/dev/tests/test_initialize_project.py',
)

PROJECT_MILESTONE_1 = '''# Milestone 1: Django and React Baseline

[Docs](../README.md) > [Roadmap](README.md) > Milestone 1

- **Outcome:** Establish the Django REST Framework API and React/Vite TypeScript
  application baseline with local setup, checks, and operational guidance.
- **Owner and schedule:** [Roadmap schedule](README.md#schedule).
- **Status:** <span style="color: green;">Completed</span>
- **Target:** No recorded target.

This milestone records the completed application baseline. Its schedule dates
mark when this baseline was initialized; the estimate describes the typical
effort to build these components. Plan the next project goal as Milestone 2 using
the [milestone planning template](milestone-template.md).

## Completed Scope

| Area | Result |
| :--- | :--- |
| Backend | A Django REST Framework API provides the initial service structure and a verified local start path. |
| Frontend | A React/Vite TypeScript application provides the initial user interface structure and local API connection. |
| Decisions | Architecture Decision Records (ADRs) capture the approved stack and open project choices. |
| Verification | Local and hosted checks cover the application baseline alongside repository checks. |
| Operations | Runbooks describe local setup and the maintenance paths established for these components. |

## Verification and Handoff

The project setup pull request records this repository's local and hosted checks,
reporting contacts, and live settings. Recheck GitHub controls through the
[GitHub configuration runbook](../runbooks/configure-github.md). Copied workflow
files alone do not activate repository settings.

Review the [decision log](../adr/README.md) for approved baseline decisions and
choices the project still needs to make.

## Related Documents

- [Roadmap index](README.md) - Plan Milestone 2 and later project work.
- [Milestone 0](milestone-0-repository-scaffolding.md) - Repository practices supporting this baseline.
- [Architecture Decision Records (ADRs)](../adr/README.md) - Approved and open choices.
- [Repository settings](../architecture/repository-settings.md) - Controls to verify for this repository.
'''


def run_git(*arguments):
  return subprocess.run(
    ['git', *arguments], cwd=ROOT, capture_output=True, text=True, check=False)


def repository_root():
  result = run_git('rev-parse', '--show-toplevel')
  if result.returncode or Path(result.stdout.strip()).resolve() != ROOT:
    raise ValueError('Run this helper from a copy rooted at its Git repository.')
  remote = run_git('remote', 'get-url', 'origin')
  if remote.returncode:
    raise ValueError('Configure the destination as the origin remote first.')
  url = remote.stdout.strip().removesuffix('.git')
  for prefix in ('https://github.com/', 'git@github.com:', 'ssh://git@github.com/'):
    if url.startswith(prefix):
      name = url[len(prefix):]
      if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', name):
        break
      if name.lower() in SOURCE_ALIASES:
        raise ValueError('The origin remote still points to a source repository.')
      return name
  raise ValueError('The origin remote must identify the new GitHub repository.')


def read_file(name):
  path = ROOT / name
  if path.is_symlink() or not path.is_file():
    raise ValueError(f'Required regular file is missing: {name}')
  return path.read_text(encoding='utf-8')


def replace_count(name, old, new, count):
  content = read_file(name)
  if content.count(old) != count:
    raise ValueError(f'Expected {count} source value(s) in {name}; review edits manually.')
  return content.replace(old, new)


def validate_email(value):
  if not re.fullmatch(r'[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+', value):
    raise ValueError('Enter a single email address without spaces or markup.')


def configure_plan(repository, security_email, conduct_email, retain_source_contact=False):
  if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository):
    raise ValueError('Use OWNER/REPOSITORY for --repository.')
  if repository.lower() != repository_root().lower():
    raise ValueError('--repository must match the origin remote.')
  validate_email(security_email)
  validate_email(conduct_email)
  retains_contact = SOURCE_EMAIL in (security_email, conduct_email)
  if retains_contact and not retain_source_contact:
    raise ValueError('Use --retain-source-contact to keep the starter reporting address.')
  if retain_source_contact and not retains_contact:
    raise ValueError('--retain-source-contact requires a matching reporting address.')
  destination = f'https://github.com/{repository}'
  plan = {
    name: replace_count(name, SOURCE_URL, destination, count)
    for name, count in URL_FILES.items()
  }
  for name, address in (('SECURITY.md', security_email),
                        ('CODE_OF_CONDUCT.md', conduct_email)):
    updated = replace_count(name, SOURCE_EMAIL, address, 2)
    if updated != read_file(name):
      plan[name] = updated
  return plan


def tracked_and_unchanged(name):
  tracked = run_git('ls-files', '--error-unmatch', '--', name)
  changed = run_git('diff', '--quiet', 'HEAD', '--', name)
  if tracked.returncode or changed.returncode or (ROOT / name).is_symlink():
    raise ValueError(f'Setup file is missing or modified: {name}')
  read_file(name)


def finish_plan(setup_date, retain_source_contact=False):
  repository = repository_root()
  for name in REMOVALS:
    tracked_and_unchanged(name)
  destination = f'https://github.com/{repository}'
  for name, count in URL_FILES.items():
    content = read_file(name)
    if SOURCE_URL in content or content.count(destination) != count:
      raise ValueError(f'Confirm the new repository links in {name} before finishing.')
  retains_contact = any(SOURCE_EMAIL in read_file(name) for name in EMAIL_FILES)
  if retains_contact and not retain_source_contact:
    raise ValueError('Use --retain-source-contact to keep the starter reporting address.')
  if retain_source_contact and not retains_contact:
    raise ValueError('--retain-source-contact requires a matching reporting address.')
  readme = read_file('README.md')
  if ('# Repository Scaffolding' in readme or 'initialize-repository.md' in readme
      or any(alias in readme for alias in SOURCE_ALIASES)):
    raise ValueError('Replace the root README and its setup link before finishing.')
  owners = read_file('.github/CODEOWNERS')
  if '@your-maintainer' in owners or '@your-org' in owners:
    raise ValueError('Assign or remove the example CODEOWNERS accounts before finishing.')

  plan = {}
  name = 'docs/architecture/README.md'
  row = '| [Starter repository verification](starter-verification.md) | This repository\'s settings, hosted checks, and remaining verification cases |\n'
  plan[name] = replace_count(name, row, '', 1)

  name = 'docs/roadmap/milestone-0-repository-scaffolding.md'
  tracked_and_unchanged(name)
  plan[name] = replace_count(name, 'milestone-1-django-react-starter/README.md',
                             'milestone-1-django-react-baseline.md', 2)

  if (ROOT / PROJECT_MILESTONE_PATH).exists() or (ROOT / PROJECT_MILESTONE_PATH).is_symlink():
    raise ValueError(f'Project milestone already exists: {PROJECT_MILESTONE_PATH}')
  plan[PROJECT_MILESTONE_PATH] = PROJECT_MILESTONE_1

  name = 'docs/roadmap/README.md'
  tracked_and_unchanged(name)
  content = read_file(name)
  source_row = ('| [Milestone 0: Repository Scaffolding](milestone-0-repository-scaffolding.md) '
                '|  | Repository maintainers | 5–9 weeks | Not recorded | Not recorded '
                '| 2026-11-22 | 2026-11-22 | Not measured '
                '| <span style="color: green;">Completed</span> |')
  project_row = ('| [Milestone 0: Repository Scaffolding](milestone-0-repository-scaffolding.md) '
                 '|  | Repository maintainers | 5–9 weeks | Not recorded | Not recorded '
                 f'| {setup_date} | {setup_date} | Not measured '
                 '| <span style="color: green;">Completed</span> |')
  if content.count(source_row) != 1:
    raise ValueError('The source roadmap schedule changed; review it manually.')
  content = content.replace(source_row, project_row)
  rows = content.splitlines(keepends=True)
  if any(row.startswith('|  | [Phase ')
         and '(milestone-0-repository-scaffolding.md#phase-' in row for row in rows):
    raise ValueError('The source roadmap phases changed; review them manually.')
  milestone_rows = [row for row in rows if row.startswith('| [Milestone 1: Django and React starter]')]
  phase_rows = [row for row in rows if row.startswith('|  | [Phase ')
                and '(milestone-1-django-react-starter/' in row]
  if len(milestone_rows) != 1 or len(phase_rows) != 6:
    raise ValueError('The starter roadmap rows changed; review them manually.')
  completed = '<span style="color: green;">Completed</span>'
  cells_by_row = [[cell.strip() for cell in row.strip().strip('|').split('|')]
                  for row in milestone_rows + phase_rows]
  if any(len(cells) != 10 or cells[9] != completed or
         not re.fullmatch(r'\d{4}-\d{2}-\d{2}', cells[7])
         for cells in cells_by_row):
    raise ValueError('Complete Milestone 1 and each phase with actual end dates before finishing.')
  project_row = ('| [Milestone 1: Django and React Baseline](milestone-1-django-react-baseline.md) '
                 '|  | Repository maintainers | 3–5 weeks | Not recorded | Not recorded '
                 f'| {setup_date} | {setup_date} | Not measured '
                 '| <span style="color: green;">Completed</span> |\n')
  plan[name] = ''.join(project_row if row in milestone_rows else row
                       for row in rows if row not in phase_rows)

  name = 'docs/runbooks/README.md'
  row = '| [Initialize a project repository](initialize-repository.md) | Turn this starter into a new project repository |\n'
  plan[name] = replace_count(name, row, '', 1)

  name = 'scripts/README.md'
  row = '| [initialize-project.py](dev/initialize-project.py) | Previews or applies one-time project setup and cleanup | `python3 scripts/dev/initialize-project.py --help` |\n'
  content = replace_count(name, row, '', 1)
  section = (
    '## One-Time Project Initialization\n\n'
    'The [initialization runbook](../docs/runbooks/initialize-repository.md) owns the\n'
    'setup order. `initialize-project.py configure` previews the issue chooser URL and\n'
    'reporting-contact replacements; `finish` previews completed Milestone 0 and 1\n'
    'dates, a concise Milestone 1 record, and removal of one-time files. Each stage\n'
    'requires `--apply` to write changes. The helper checks the destination GitHub\n'
    'remote, refuses modified removal candidates, and checks documentation after\n'
    'applying changes. `finish` also requires Milestone 1 and all its phases to show\n'
    'Completed status and actual end dates in the roadmap. The helper leaves the root\n'
    'README, review owners, ADR outcomes, and live repository settings for the\n'
    'maintainer to resolve. To keep the monitored starter reporting address, pass\n'
    '`--retain-source-contact` to both `configure` and `finish`.\n\n'
  )
  if content.count(section) != 1:
    raise ValueError('The script-reference setup section changed; review it manually.')
  plan[name] = content.replace(section, '')

  name = 'docs/runbooks/configure-github.md'
  content = read_file(name)
  old = ('- Complete the [identity and contact setup](initialize-repository.md#set-identity-and-reporting-contacts)\n'
         '  for identity and reporting contacts before inviting reports or relying on\n'
         '  the issue forms.\n')
  if old in content:
    content = content.replace(old,
      '- Confirm the project identity and reporting contacts before inviting\n'
      '  reports or relying on the issue forms.\n')
    related = '- [Initialize a project repository](initialize-repository.md) - Identity and reporting-contact setup.\n'
    if content.count(related) != 1:
      raise ValueError('The GitHub runbook setup link changed; review it manually.')
    content = content.replace(related,
      '- [Security policy](../../SECURITY.md) - Private reporting channels.\n')
    plan[name] = content

  for name in REMOVALS:
    plan[name] = None

  for current, directories, files in os.walk(ROOT, followlinks=False):
    directories[:] = [directory for directory in directories
                      if directory != '.git' and not (Path(current) / directory).is_symlink()]
    for filename in files:
      path = Path(current) / filename
      if path.suffix != '.md' or path.is_symlink():
        continue
      name = path.relative_to(ROOT).as_posix()
      content = plan.get(name)
      if content is None and name in plan:
        continue
      content = content if content is not None else path.read_text(encoding='utf-8')
      if 'starter-verification.md' in content:
        raise ValueError(f'An incoming verification-record link remains in {name}.')
      if 'initialize-repository.md' in content:
        raise ValueError(f'An incoming initialization-runbook link remains in {name}.')
      if any(alias in content for alias in SOURCE_ALIASES):
        raise ValueError(f'A source-repository reference remains in {name}.')
  return plan


def apply_plan(plan):
  originals = {
    name: (ROOT / name).read_bytes() if (ROOT / name).exists() else None
    for name in plan
  }
  try:
    for name, content in plan.items():
      path = ROOT / name
      current = path.read_bytes() if path.exists() else None
      if path.is_symlink() or current != originals[name]:
        raise ValueError(f'{name} changed during setup; no further files were updated.')
      if content is None:
        path.unlink()
      else:
        path.write_text(content, encoding='utf-8')
    for check in ('check-links.sh', 'check-docs.sh'):
      result = subprocess.run(
        [str(ROOT / 'scripts/ci' / check)], cwd=ROOT,
        capture_output=True, text=True, check=False)
      if result.returncode:
        raise ValueError(f'{check} failed after setup:\n{result.stdout}{result.stderr}')
  except (OSError, ValueError):
    for name, content in originals.items():
      path = ROOT / name
      if path.is_symlink():
        path.unlink()
      if content is None:
        path.unlink(missing_ok=True)
      else:
        path.write_bytes(content)
    raise


def main():
  if sys.version_info < (3, 9):
    raise ValueError('Python 3.9 or newer is required.')
  parser = argparse.ArgumentParser(description=__doc__)
  commands = parser.add_subparsers(dest='command', required=True)
  configure = commands.add_parser('configure', help='Replace the issue chooser URL and reporting contacts')
  configure.add_argument('--repository', required=True, help='New GitHub OWNER/REPOSITORY')
  configure.add_argument('--security-email', required=True)
  configure.add_argument('--conduct-email', required=True)
  configure.add_argument('--retain-source-contact', action='store_true',
                         help='Explicitly keep the monitored starter reporting address')
  configure.add_argument('--apply', action='store_true', help='Apply the previewed changes')
  finish = commands.add_parser('finish', help='Remove one-time source records and setup files')
  finish.add_argument('--retain-source-contact', action='store_true',
                      help='Confirm the monitored starter reporting address is still intended')
  finish.add_argument('--apply', action='store_true', help='Apply the previewed changes')
  args = parser.parse_args()
  if args.command == 'configure':
    plan = configure_plan(args.repository, args.security_email, args.conduct_email,
                          args.retain_source_contact)
  else:
    setup_date = datetime.now(ZoneInfo('America/Chicago')).date().isoformat()
    plan = finish_plan(setup_date, args.retain_source_contact)
    print(f'Milestones 0 and 1 actual start and end: {setup_date} (America/Chicago)')
  for name, content in plan.items():
    action = ('remove' if content is None else
              'create' if not (ROOT / name).exists() else 'update')
    print(f'{"Will" if args.apply else "Would"} {action}: {name}')
  if args.apply:
    apply_plan(plan)
    print('Setup changes applied; review and commit the resulting diff.')
  else:
    print('Preview only. Re-run with --apply after reviewing every path.')


if __name__ == '__main__':
  try:
    main()
  except (OSError, ValueError) as error:
    sys.exit(f'Error: {error}')
