---
date: 2026-05-25
authors:
  - dataguirre
categories:
  - Announcements
---

# Welcome to the WJP Wiki Blog

The wiki now has a **Blog**. A time-ordered, author-attributed space for
team updates, announcements, how-tos, and retrospectives that complement
the reference documentation in the rest of the site.

<!-- more -->

## What goes here

The reference sections of the wiki answer *how do we do X?*, while the blog
answers *what changed?* and *what did we learn?*. Use it for:

- **Announcements**: team or project news, new tools, process changes.
- **How-To**: step-by-step guides that don't yet have a home in the Guide.
- **Retrospectives**: lessons learned from a project wrapping up, incident
  reviews, sprint write-ups, and post-mortems.
- **Engineering**: technical deep-dives and decision write-ups.

This is the place to capture what a project taught us so the next team
benefits. Reference documentation for a single project, like its setup,
architecture, and runbooks, lives in that project's own GitHub
repository wiki.

## Writing a post

Posts live in `docs/blog/posts/` as Markdown files with frontmatter:

```yaml
---
date: 2026-05-25
authors:
  - dataguirre
categories:
  - Artificial Intelligence
tags:
  - Rule of Law
  - News data
---
```

Add yourself to `docs/blog/.authors.yml` the first time you post. The
archive sidebar groups posts by year automatically, and categories are
populated from each post's frontmatter.

Open a pull request just like any other change to the wiki. See
[Contributing to the Wiki](../../home/contributing.md).
