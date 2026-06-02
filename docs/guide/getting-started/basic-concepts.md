# Basic Concepts

*Core ideas behind version control, Git, and GitHub — and the vocabulary used
throughout this guide.*

!!! note "Before you start"
    This page is conceptual. You do not need to install anything yet. The goal
    is to understand the pieces before you start using commands, pull requests,
    and repositories in day-to-day work.

## The problem: project history gets messy fast

Most project work starts simply. One person writes a script, edits a document,
or prepares a small dataset. At that point, keeping track of changes may feel
easy: the current file is the file that matters.

The problem appears when the project becomes real. A second person edits the
same analysis. Someone needs to compare the current methodology with last
month's version. A bug appears in a dashboard and the team needs to know when it
was introduced. A report is published and, six months later, another team member
has to reproduce the result.

Without version control, teams often try to manage this with filenames, copied
folders, messages, and memory:

```text
Project without version control

analysis.R
  |
  +-- analysis_final.R
        |
        +-- analysis_final_v2.R
              |
              +-- analysis_final_real_final.R
                    |
                    +-- analysis_final_Daniel_edits.R
                    |
                    +-- analysis_final_Carlos_review.R

Questions after a few weeks:

- Which file is the real current version?
- What changed between versions?
- Who made the change?
- Why was the change made?
- Can we recover an earlier version?
- Which version produced the published result?
```

This pattern is familiar because it is quick in the moment. It is also fragile.
The history is spread across filenames, duplicated folders, email threads, chat
messages, and people's memory. That makes collaboration harder and makes
reproducibility weaker.

Version control solves this by turning project history into a structured record.
Instead of guessing which file matters, the team works from one project history
that records meaningful changes over time.

## What problem does Git solve?

Git is the tool that creates that structured record. It does not just save files;
it records snapshots of a project, connects those snapshots into a history, and
lets the team inspect, share, and recover that history.

With Git, the same project can be represented like this:

```text
Project with Git

main
  |
  o  Initial analysis script
  |
  o  Add data cleaning step
  |
  o  Fix weighting calculation
  |
  o  Update README with run instructions
  |
  o  Add chart for final report

Each point is a commit:

- It has an author.
- It has a date.
- It has a message.
- It stores exactly what changed.
- It can be inspected later.
```

This changes the team's basic questions. Instead of asking "which final file is
the real one?", the team can ask Git for the project history. Instead of relying
on memory to know why something changed, the team can read the commit message,
the changed files, and later, the pull request or issue connected to the change.

For WJP work, this matters because many projects involve code, data
documentation, methodology files, dashboards, questionnaires, and reports that
evolve over time. Git makes that evolution explicit instead of hiding it inside
attachments or copied folders.

Git helps with:

- **History** — Git records meaningful changes as commits, so the project has a
  timeline instead of a pile of copied files.
- **Comparison** — Git can show exactly what changed between two versions of a
  file.
- **Recovery** — earlier versions can be inspected or restored when something
  breaks.
- **Collaboration** — several people can work on related changes without
  overwriting each other's work.
- **Review** — changes can be examined before they become part of the stable
  project.
- **Reproducibility** — code and documentation can be tied to the exact version
  used to produce a result.
- **Handoff** — a future team member can understand how the project reached its
  current state.

!!! tip "The key idea"
    Git turns project work from an informal sequence of files into an explicit
    sequence of decisions and changes.

## Git and GitHub are not the same thing

Git and GitHub are related, but they are not interchangeable.

| Tool | What it is | What it does |
| --- | --- | --- |
| **Git** | A version control program that runs on your computer. | Tracks changes, creates commits, manages branches, and syncs project history. |
| **GitHub** | A web platform that hosts Git repositories. | Provides remote repositories, permissions, pull requests, issues, review tools, automation, and project visibility. |

You can use Git without GitHub. Git works locally on your computer and does not
require internet access for most operations. GitHub adds the shared online place
where the team collaborates around the Git repository.

!!! tip "Simple mental model"
    Git is the tracking system. GitHub is the shared workspace built around that
    system.

## The basic mental model

Git is easier to understand if you keep a few concepts separate.

### Working directory

The working directory is the project folder on your computer. It contains the
files you can open, edit, move, or delete.

When you edit a Markdown file, a Python script, an R script, or a README, you
are changing the working directory.

### Repository

A repository, often shortened to repo, is a project folder with Git history.
It contains the current files and the hidden Git database that stores previous
versions.

At WJP, a repository usually represents one project, tool, website, dashboard,
analysis workflow, or documentation source.

### Commit

A commit is a saved point in the project history. It is not just a file save. A
commit should represent a meaningful unit of work, such as:

- Add setup instructions to a README.
- Fix a calculation in an analysis script.
- Update documentation after a methodology change.
- Add a chart used by a report.

Each commit has an identifier, an author, a timestamp, and a message explaining
the change. Later, the team can inspect the commit to understand exactly what
changed.

### Branch

A branch is a line of work inside a repository. The main branch, usually named
`main`, represents the stable version of the project. A feature branch lets you
work on a change without directly modifying `main`.

Branches are how teams make changes safely. You can prepare work, review it,
and merge it only when it is ready.

### Remote

A remote is another copy of the same repository, usually hosted on GitHub. Your
computer has a local copy. GitHub has the shared remote copy.

The default remote is usually called `origin`.

### Push and pull

Pushing and pulling are how your local repository communicates with the remote
repository.

- **Pull** means bring changes from GitHub to your computer.
- **Push** means send your local commits to GitHub.

## What Git should track

Git works best for files that are small enough to review and meaningful enough
to keep in project history.

Good candidates for Git:

- Source code: `.py`, `.R`, `.do`, `.js`, `.sql`.
- Documentation: `README.md`, methodology notes, runbooks, wiki pages.
- Configuration: project metadata, dependency files, CI configuration.
- Small reference files needed to run the project.
- Reproducible scripts that create outputs from documented inputs.

Git should not be treated as a general storage drive.

Avoid committing:

- Passwords, tokens, API keys, or credentials.
- Personal, confidential, or sensitive data.
- Large raw datasets.
- Generated outputs that can be recreated.
- Local environment folders such as `.venv/`.
- Temporary files, caches, and system files.

!!! warning "Security rule"
    If a file contains a secret or sensitive data, it does not belong in Git.
    See [Data & Security](../wjp-standards/data-and-security.md) before adding
    anything that may be confidential.

## Basic GitHub concepts

The full workflow is covered later in [Using GitHub](../github/core-workflow.md).
For now, you only need the basic meaning of the terms.

| Concept | Basic meaning |
| --- | --- |
| **Pull request** | A proposed change to a repository. It lets others review the difference before it is merged. |
| **Review** | Feedback on a pull request before the change becomes part of the main project. |
| **Issue** | A tracked task, bug, question, or request. |
| **Discussion** | A place for broader questions, decisions, or conversations that are not yet a concrete task. |
| **Merge** | The act of bringing changes from one branch into another. |
| **Conflict** | A situation where Git needs human help because two changes affect the same part of a file. |
| **GitHub Actions** | Automation that can run checks, tests, builds, or deployments when something happens in a repository. |
| **GitHub Pages** | A GitHub feature for publishing static websites, such as this wiki. |

You do not need to master these yet. The important point is that GitHub adds a
collaboration layer on top of Git.

## Why WJP uses GitHub

WJP uses GitHub because it supports the way code, data, and documentation should
be managed in a professional research and policy environment.

### Reproducibility

WJP work often depends on data processing, analysis scripts, methodology notes,
dashboards, and report outputs. Those pieces should not exist as isolated files.
They should be connected in a way that lets someone understand how a result was
produced.

GitHub helps by keeping code, documentation, and review history together. A
repository can show which files existed at a given point in time, what changed
after that point, and which version of the project produced a result. This is
especially important when work needs to be checked, updated, repeated, or
explained months later.

### Collaboration

WJP projects are rarely isolated individual exercises. Analysts, researchers,
data specialists, developers, and project leads may all touch different parts of
the same work.

GitHub gives the team a shared place to propose changes, review them, discuss
them, and merge them into the main project. That makes collaboration less
dependent on meetings, private messages, or one person being available to explain
the current state of the project.

### Transparency

Some WJP work is internal, but some methods, tools, and documentation are meant
to be public or externally inspectable. GitHub makes it easier to publish the
parts of a project that should be visible while keeping private repositories for
work that is not ready or not appropriate for public release.

When a public repository is used well, external readers can see not only the
final files, but also the structure of the project, its documentation, and the
history of improvements. That strengthens trust in technical and methodological
work.

### Institutional memory

People move between projects, roles, and teams. Without a shared project record,
important context disappears into inboxes, private notes, and memory.

GitHub preserves more than files. It can preserve issues, pull requests, review
comments, discussions, release notes, and documentation. That record helps a new
team member understand not only what the project currently does, but how it got
there and which decisions shaped it.

These four pillars work together. Reproducibility makes results easier to trust;
collaboration makes work easier to improve; transparency makes appropriate work
easier to inspect; and institutional memory makes projects easier to maintain
after handoff.

## Common misconceptions

### "GitHub is the same as SharePoint"

It is not. SharePoint is better for shared office documents, large files, and
collaborative files that are not managed as code. GitHub is better for versioned
code, documentation, configuration, and project history.

Some projects use both: GitHub for code and documentation, SharePoint for data
or large supporting files.

### "Git is only for software engineers"

Git is useful whenever work needs history, review, and reproducibility. That
includes data cleaning, statistical analysis, methodology documentation,
dashboards, and report generation.

### "A repository is a dumping folder"

A repository should have a purpose. It should be possible for another person to
open it and understand what the project is, how to run it, and where the
important files live.

### "If I delete a file locally, the project history is gone"

Deleting a file changes the current version of the project, but previous commits
still contain the earlier history. This is one of the main reasons Git is useful.

## Key vocabulary

| Term | Meaning |
| --- | --- |
| **Repository / repo** | A project tracked by Git. |
| **Clone** | A local copy of a remote repository. |
| **Commit** | A saved change in the repository history. |
| **Branch** | A separate line of work inside the repository. |
| **Main** | The default stable branch in most WJP repositories. |
| **Remote** | A copy of the repository hosted somewhere else, usually GitHub. |
| **Origin** | The default name Git gives to the main remote. |
| **Pull** | Bring remote changes into your local repository. |
| **Push** | Send local commits to the remote repository. |
| **Merge** | Combine changes from one branch into another. |
| **Pull request / PR** | A request to review and merge changes. |
| **Conflict** | A change Git cannot combine automatically. |
| **`.gitignore`** | A file that tells Git which files should not be tracked. |

## Next step

Once these concepts are clear, set up the tools on your computer:
[Environment Setup](environment-setup.md).
