# Environment Setup

*Installing and configuring the tools needed to work with WJP repositories.*

!!! note "Goal"
    By the end of this page, you should have Git installed on your computer,
    your Git identity configured, GitHub authentication working, and GitHub
    Desktop ready for day-to-day repository work.

## The setup path

Before Git can fit naturally into your work, a few pieces need to be in place.
Some of them are required because Git cannot work properly without them. Others
make the workflow easier to see, edit, and review.

<div class="wjp-setup-flow" aria-label="Basic Git setup flow">
  <div class="wjp-setup-flow__group">
    <span class="wjp-setup-flow__label">Local foundation</span>
    <div class="wjp-setup-flow__track">
      <div class="wjp-setup-flow__node">
        <span class="wjp-setup-flow__step">1</span>
        <strong>Terminal</strong>
        <span>Run setup commands.</span>
      </div>
      <div class="wjp-setup-flow__node">
        <span class="wjp-setup-flow__step">2</span>
        <strong>Git</strong>
        <span>Track project history.</span>
      </div>
      <div class="wjp-setup-flow__node">
        <span class="wjp-setup-flow__step">3</span>
        <strong>Git identity</strong>
        <span>Name each commit author.</span>
      </div>
    </div>
  </div>
  <div class="wjp-setup-flow__bridge" aria-hidden="true">Connect</div>
  <div class="wjp-setup-flow__group">
    <span class="wjp-setup-flow__label">GitHub workflow</span>
    <div class="wjp-setup-flow__track">
      <div class="wjp-setup-flow__node">
        <span class="wjp-setup-flow__step">4</span>
        <strong>Authentication</strong>
        <span>Push and pull from GitHub.</span>
      </div>
      <div class="wjp-setup-flow__node">
        <span class="wjp-setup-flow__step">5</span>
        <strong>GitHub Desktop</strong>
        <span>Review, commit, push, and pull visually.</span>
      </div>
    </div>
  </div>
</div>

The order matters. First, install Git and configure it on your computer. Then
connect that local Git setup to GitHub, where WJP repositories live. Finally,
add GitHub Desktop so you can see changes, create commits, push, pull, and
switch branches through a visual interface.

This page follows that same order:

1. **Install Git on your computer** — terminal basics, Git installation, and Git
   identity.
2. **Connect your computer to GitHub** — GitHub CLI and authentication.
3. **Add GitHub Desktop for daily work** — a visual interface for common Git
   actions.

You do not need to become an expert in every tool immediately. The goal is to
have a working environment and understand what each piece is for.

## Part 1: Install Git on your computer

Git is the version control tool used by WJP repositories. Before using GitHub,
pull requests, branches, or repository workflows, your computer needs to know
how to run Git.

### Before you install anything

Confirm these items first:

- You have a GitHub account.
- You know which email address is associated with that account.
- You have been added to the relevant WJP GitHub organization or repository.
- You have permission to install software on your computer.
- You know your operating system: macOS, Windows, or Linux.

!!! tip "Use your work identity consistently"
    Use the same professional identity across Git, GitHub, and WJP
    repositories. This makes project history easier to understand later.

### Terminal basics

The terminal is a text-based interface for running commands. Git can be used
through graphical tools, but the terminal is the clearest way to understand what
is happening and to troubleshoot problems.

How to open a terminal:

- **macOS**: open **Terminal**.
- **Windows**: open **PowerShell**, **Windows Terminal**, or **Git Bash** after
  installing Git for Windows.
- **Linux**: open the default terminal application for your distribution.

Useful starter commands:

```bash
pwd
```

Shows the current folder.

```bash
ls
```

Lists files in the current folder. On Windows PowerShell, `dir` also works.

```bash
cd path/to/folder
```

Moves into another folder.

!!! note "Why the terminal matters"
    GitHub Desktop is useful, but the terminal remains the common setup and
    troubleshooting language. Documentation will often give commands because
    commands are precise and work across projects.

### Install Git

Install Git for your operating system.

#### macOS

If you have Homebrew installed:

```bash
brew install git
```

If you do not use Homebrew, running the following command may prompt macOS to
install Apple's command line developer tools:

```bash
git --version
```

You can also install Git from the official Git website:
[git-scm.com/downloads](https://git-scm.com/downloads).

#### Windows

Install **Git for Windows** from:
[git-scm.com/download/win](https://git-scm.com/download/win).

During installation, the default options are fine for most users. Make sure Git
Bash is installed; it gives Windows users a terminal that behaves similarly to
the examples in this guide.

#### Linux

Use your distribution's package manager.

For Debian or Ubuntu:

```bash
sudo apt update
sudo apt install git
```

For Fedora:

```bash
sudo dnf install git
```

#### Verify Git

After installation, run:

```bash
git --version
```

You should see a version number, such as:

```text
git version 2.45.0
```

If the terminal says `git: command not found`, Git is not installed correctly or
your terminal cannot find it.

### Configure your Git identity

Git records an author name and email address on every commit. Configure them
once on your computer:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.org"
```

Use the name and email you want associated with WJP work. The email should be
connected to your GitHub account. If you use GitHub's private no-reply email,
use that exact address here.

Check the configuration:

```bash
git config --global --list
```

You should see entries like:

```text
user.name=Your Name
user.email=your.email@example.org
```

Set the default branch name for new repositories:

```bash
git config --global init.defaultBranch main
```

!!! warning "Email matters"
    If your Git email is not associated with your GitHub account, your commits
    may not appear under your GitHub profile. Fix this before starting regular
    project work.

### Checklist

Before connecting to GitHub, confirm that Git is working locally:

- `git --version` returns a Git version.
- `git config --global user.name` returns your name.
- `git config --global user.email` returns the email connected to GitHub.
- `git config --global init.defaultBranch` returns `main`.

### Troubleshooting

#### `git: command not found`

Git is not installed, or your terminal cannot find it. Install Git again, then
restart the terminal. On Windows, make sure you are using Git Bash, Windows
Terminal, or a terminal where Git was added to the system path.

#### macOS asks to install command line developer tools

This is expected if Git is being installed through Apple's command line tools.
Accept the installation, wait for it to finish, then run:

```bash
git --version
```

#### Your commits show the wrong author

Check your Git identity:

```bash
git config --global --list
```

Update it if needed:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.org"
```

#### Your Git email is not connected to GitHub

Open your GitHub account settings and confirm which email addresses are linked
to your account. Then set Git to use one of those addresses. If you prefer to
keep your email private, GitHub provides a no-reply email address that can be
used in Git commits.

## Part 2: Connect your computer to GitHub

Git is local: it works on your computer. GitHub is remote: it hosts shared
repositories online. To collaborate with WJP repositories, your computer needs a
secure way to identify you to GitHub.

The recommended setup path is GitHub CLI. It handles authentication and can
configure Git so that pushing and pulling from GitHub works without entering a
password every time.

### Install GitHub CLI

GitHub CLI is called `gh`.

#### macOS

With Homebrew:

```bash
brew install gh
```

#### Windows

Install GitHub CLI from:
[cli.github.com](https://cli.github.com/).

You can also install it with Windows Package Manager:

```powershell
winget install --id GitHub.cli
```

#### Linux

Follow the official instructions for your distribution:
[github.com/cli/cli#installation](https://github.com/cli/cli#installation).

#### Verify GitHub CLI

Run:

```bash
gh --version
```

You should see a version number. If the command is not found, restart your
terminal and try again. If it still fails, reinstall GitHub CLI.

### Authenticate with GitHub

Run:

```bash
gh auth login
```

Use these choices for the standard WJP setup:

1. Choose `GitHub.com`.
2. Choose `HTTPS`.
3. When asked whether to authenticate Git with your GitHub credentials, choose
   `Yes`.
4. Choose `Login with a web browser`.
5. Copy the one-time code shown in the terminal.
6. Press Enter to open the browser.
7. Paste the code into GitHub and authorize GitHub CLI.

Verify authentication:

```bash
gh auth status
```

You should see that you are logged in to `github.com` and that Git operations
are configured.

!!! note "HTTPS vs SSH"
    HTTPS with GitHub CLI is the recommended starting point because it is simple
    and works well for most users. SSH is also valid, but it requires managing
    SSH keys and is better handled after the basic workflow is clear.

### Confirm repository access

Authentication only proves that GitHub knows who you are. You also need
permission to access the repositories where you will work.

The simplest check is to open the repository in the browser while logged in to
GitHub. If the page loads, you have access. If it does not load, ask the
repository owner or WJP GitHub administrator to confirm that your account has
been added to the correct organization, team, or repository.

### Checklist

Before moving to daily tools, confirm that your computer can talk to GitHub:

- `gh --version` returns a GitHub CLI version.
- `gh auth status` shows that you are logged in to `github.com`.
- `gh auth status` says Git operations are configured.
- You can open at least one WJP repository in the browser while logged in to
  GitHub.

### Troubleshooting

#### `gh: command not found`

GitHub CLI is not installed, or your terminal cannot find it. Install `gh`, then
restart the terminal. If the command still fails, confirm that the installation
finished successfully and that your terminal is using the expected system path.

#### GitHub authentication failed

Run:

```bash
gh auth status
```

If you are not logged in, run:

```bash
gh auth login
```

If you are logged into the wrong account:

```bash
gh auth logout
gh auth login
```

#### The browser login code expired

Run `gh auth login` again and use the new one-time code. The code is temporary,
so it must be pasted into GitHub soon after it appears in the terminal.

#### Git asks for a username or password when pushing

GitHub no longer accepts account passwords for Git operations. Run:

```bash
gh auth login
```

When asked whether to authenticate Git with your GitHub credentials, choose
`Yes`.

#### You are logged in but cannot see a repository

Authentication and authorization are different. Authentication proves your
identity; authorization controls which repositories you can access. Confirm that
you are using the correct GitHub account and that the repository owner has added
that account to the appropriate WJP organization, team, or repository.

## Part 3: Add GitHub Desktop for daily work

Once Git is installed and GitHub authentication works, add GitHub Desktop as the
main visual tool for day-to-day repository work. It helps new users understand
what Git is doing because it shows changes, branches, commits, pushes, and pulls
in one interface.

GitHub Desktop does not replace Git. It sits on top of Git. The commits it
creates are normal Git commits, and the pushes and pulls it performs are the
same operations you can run from the terminal.

![Screenshot of GitHub Desktop showing changed files, a visual diff, and the commit panel.](https://user-images.githubusercontent.com/634063/202742985-bb3b3b94-8aca-404a-8d8a-fd6a6f030672.png)

*Source: official [`desktop/desktop`](https://github.com/desktop/desktop)
repository.*

### What GitHub Desktop shows

The main GitHub Desktop window is organized around the work you do most often:

- **Current repository** — the project you are working on.
- **Current branch** — the branch where your changes will be committed.
- **Changed files** — the files that are different from the last commit.
- **Diff view** — the exact lines added, removed, or modified.
- **Commit summary and description** — the message that explains your change.
- **Push, pull, and fetch controls** — the actions that sync your local work
  with GitHub.

This view is useful because it forces a good habit: review what changed before
you commit. You should never commit blindly. Even small changes should be
checked before they become part of the project history.

### Install GitHub Desktop

Install GitHub Desktop from:
[desktop.github.com](https://desktop.github.com/).

After installing it:

1. Sign in with your GitHub account.
2. Let GitHub Desktop use the Git configuration already set on your computer.
3. Clone a repository you have access to.
4. Review the repository's changed files before committing.

### What GitHub Desktop is good for

GitHub Desktop is especially useful for:

- Cloning repositories from GitHub.
- Seeing which files changed.
- Reviewing a visual diff.
- Writing commit messages.
- Creating commits.
- Pushing local commits to GitHub.
- Pulling updates from GitHub.
- Switching between branches.
- Opening a repository on GitHub in the browser.

For many users, this is the best starting point because the interface makes the
workflow visible. Instead of memorizing every command immediately, you can see
the relationship between changed files, commits, branches, and sync actions.

### What GitHub Desktop does not replace

GitHub Desktop is a practical tool, but it does not replace understanding Git.
You still need to know the basic concepts: repository, commit, branch, push,
pull, and merge.

Some project documentation will also ask you to run commands in the terminal.
That is normal. The terminal remains important for setup, troubleshooting,
package installation, and project-specific commands.

!!! tip "Recommended starting workflow"
    Use GitHub Desktop to review changes visually, commit, push, pull, and
    switch branches. Learn the equivalent terminal commands gradually so you can
    troubleshoot and follow project documentation confidently.

### Choosing the right interface for the task

| Task | Recommended tool |
| --- | --- |
| Review changed files visually | GitHub Desktop |
| Make a simple commit | GitHub Desktop or terminal |
| Push or pull changes | GitHub Desktop or terminal |
| Switch branches | GitHub Desktop or terminal |
| Run documented setup commands | Terminal |
| Troubleshoot authentication or Git configuration | Terminal |
| Open or manage pull requests | GitHub website or GitHub CLI |

The important point is not which interface you prefer. The important point is
that all interfaces are working with the same Git repository.

## Security basics

Your local setup should make it easy to avoid committing secrets or sensitive
files.

Never commit:

- Passwords.
- API keys.
- Access tokens.
- `.env` files with real credentials.
- Personal or confidential data.
- Large raw data files that belong in SharePoint or another approved storage
  location.

Before starting work in a repository, check whether it has a `.gitignore` file.
That file tells Git which local files should be ignored.

See [Data & Security](../wjp-standards/data-and-security.md) for the full WJP
rules.

## Final setup checklist

Before moving on, confirm that the full setup is ready:

- Git is installed and configured with your name and GitHub email.
- GitHub CLI is installed and authenticated.
- You can access at least one repository you are expected to use.
- GitHub Desktop is installed and signed in to your GitHub account.
- You know where to troubleshoot local Git problems and where to troubleshoot
  GitHub authentication problems.

## Next step

After your environment is ready, continue with the everyday Git workflow:
[Core Workflow](../github/core-workflow.md).
