# WJP Wiki

Source for the **WJP Wiki** — a living guide to the workflows, tools,
and best practices we use for code and data at WJP.

The site is built with [MkDocs](https://www.mkdocs.org/) and the
[Material](https://squidfunk.github.io/mkdocs-material/) theme, and published with
GitHub Pages.

## Run it locally

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run mkdocs serve
```

Then open <http://127.0.0.1:8000>. The preview reloads as you edit.

## Build

```bash
uv run mkdocs build --strict
```

## Contributing

The wiki is updated through pull requests — it models the workflow it teaches.
See the **Contributing to the Wiki** page in the site for the full process.

## Layout

```
docs/        Wiki content (Markdown)
mkdocs.yml   Site configuration and navigation
```
