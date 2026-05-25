"""MkDocs hook: per-tag pages and a Tags section in the blog sidebar.

For every unique tag found in the frontmatter of `docs/blog/posts/*.md`, this
hook generates a virtual page at `blog/tag/<slug>/`. Each tag page is rendered
with the blog plugin's own `blog.html` template, and `on_page_context` injects
the list of post excerpts that carry that tag — so visually each tag landing
is indistinguishable from a category landing.

The blog navigation gains a "Tags" section right after the auto-generated
"Categories" section, with each tag rendered as a chip linking to its filtered
page.
"""

from __future__ import annotations

import json
from pathlib import Path

import yaml
from mkdocs.plugins import event_priority
from mkdocs.structure.files import File, InclusionLevel
from mkdocs.structure.nav import Section


_BLOG_SECTION_TITLE = "Blog"
_CATEGORIES_SECTION_TITLE = "Categories"
_TAGS_SECTION_TITLE = "Tags"

_slug_to_tag: dict[str, str] = {}


def _slug(tag: str) -> str:
    return tag.lower().replace(" ", "-")


def _read_post_tags(docs_dir: Path) -> set[str]:
    posts_dir = docs_dir / "blog" / "posts"
    if not posts_dir.is_dir():
        return set()
    tags: set[str] = set()
    for post in posts_dir.rglob("*.md"):
        text = post.read_text(encoding="utf-8-sig")
        if not text.startswith("---"):
            continue
        end = text.find("\n---", 3)
        if end == -1:
            continue
        try:
            meta = yaml.safe_load(text[3:end]) or {}
        except yaml.YAMLError:
            continue
        for tag in meta.get("tags") or []:
            tags.add(str(tag))
    return tags


def _tag_page_content(tag: str) -> str:
    title = json.dumps(f'Posts tagged "{tag}"')
    return (
        "---\n"
        f"title: {title}\n"
        "template: blog.html\n"
        "search:\n"
        "  exclude: true\n"
        "---\n\n"
        f"# {tag}\n"
    )


def on_files(files, config):
    docs_dir = Path(config.docs_dir)
    _slug_to_tag.clear()
    for tag in _read_post_tags(docs_dir):
        slug = _slug(tag)
        _slug_to_tag[slug] = tag
        src_uri = f"blog/tag/{slug}.md"
        files.append(
            File.generated(
                config,
                src_uri,
                content=_tag_page_content(tag),
                inclusion=InclusionLevel.NOT_IN_NAV,
            )
        )
    return files


def on_page_context(context, page, config, nav):
    src_uri = page.file.src_uri
    if not (src_uri.startswith("blog/tag/") and src_uri.endswith(".md")):
        return
    slug = src_uri[len("blog/tag/"):-len(".md")]
    tag = _slug_to_tag.get(slug)
    if tag is None:
        return

    blog_plugin = config.plugins.get("material/blog")
    if blog_plugin is None or not hasattr(blog_plugin, "blog"):
        return

    separator = blog_plugin.config.post_excerpt_separator
    excerpts = []
    for post in blog_plugin.blog.posts:
        if tag not in (post.meta.get("tags") or []):
            continue
        if post.excerpt is None:
            continue
        post.excerpt.render(page, separator)
        excerpts.append(post.excerpt)
    context["posts"] = excerpts
    context["pagination"] = None


@event_priority(-100)
def on_nav(nav, config, files):
    blog_section = next(
        (
            item
            for item in nav.items
            if getattr(item, "is_section", False) and item.title == _BLOG_SECTION_TITLE
        ),
        None,
    )
    if blog_section is None:
        return nav

    tags = sorted(_read_post_tags(Path(config.docs_dir)), key=str.lower)
    if not tags:
        return nav

    tag_pages = []
    for tag in tags:
        file = files.get_file_from_path(f"blog/tag/{_slug(tag)}.md")
        if file is None or file.page is None:
            continue
        page = file.page
        file.inclusion = InclusionLevel.INCLUDED
        # Match category-view behavior: keep the canonical title on the page.
        page.title = tag
        tag_pages.append(page)

    if not tag_pages:
        return nav

    tags_section = Section(title=_TAGS_SECTION_TITLE, children=tag_pages)
    tags_section.parent = blog_section
    for page in tag_pages:
        page.parent = tags_section
        if page not in nav.pages:
            nav.pages.append(page)

    for i, child in enumerate(blog_section.children):
        if (
            getattr(child, "is_section", False)
            and child.title == _CATEGORIES_SECTION_TITLE
        ):
            blog_section.children.insert(i + 1, tags_section)
            return nav

    blog_section.children.append(tags_section)
    return nav
