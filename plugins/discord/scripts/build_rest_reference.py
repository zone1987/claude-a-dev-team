#!/usr/bin/env python3
"""Generate the discord-rest reference files from a local mirror of the Discord docs.

No model sits between the mirrored page and the reference file: every table, enum value,
field type, endpoint path and code example is carried across by this script verbatim.
The only removals are MDX scaffolding (the documentation-index preamble, the
`export const Route`/`ManualAnchor` JS declarations, and `<ManualAnchor>` tags).

Usage:
    python3 build_rest_reference.py --mirror <dir> --out <dir> [--check]

`--check` re-runs the transform and reports whether the on-disk files match, without
writing. Exits non-zero on any drift.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

RETRIEVED = "2026-08-26"
DOCS_BASE = "https://docs.discord.com/developers"

# mirror filename stem -> (output file, page title, live URL path)
PAGES: dict[str, tuple[str, str]] = {
    "resources__application": ("APPLICATION.md", "Application Resource"),
    "resources__audit-log": ("AUDIT-LOG.md", "Audit Logs Resource"),
    "resources__auto-moderation": ("AUTO-MODERATION.md", "Auto Moderation"),
    "resources__channel": ("CHANNEL.md", "Channels Resource"),
    "resources__emoji": ("EMOJI.md", "Emoji Resource"),
    "resources__guild": ("GUILD.md", "Guild Resource"),
    "resources__guild-scheduled-event": (
        "GUILD-SCHEDULED-EVENT.md",
        "Guild Scheduled Event",
    ),
    "resources__guild-template": ("GUILD-TEMPLATE.md", "Guild Template Resource"),
    "resources__invite": ("INVITE.md", "Invite Resource"),
    "resources__message": ("MESSAGE.md", "Message Resource"),
    "resources__poll": ("POLL.md", "Poll Resource"),
    "resources__soundboard": ("SOUNDBOARD.md", "Soundboard Resource"),
    "resources__stage-instance": ("STAGE-INSTANCE.md", "Stage Instance Resource"),
    "resources__sticker": ("STICKER.md", "Sticker Resource"),
    "resources__user": ("USER.md", "User Resource"),
    "resources__voice": ("VOICE.md", "Voice Resource"),
    "resources__webhook": ("WEBHOOK.md", "Webhook Resource"),
}

# /developers/<path> of an in-scope page -> sibling reference file
SIBLINGS: dict[str, str] = {
    "resources/" + stem.split("__", 1)[1]: out for stem, (out, _) in PAGES.items()
}

ADMONITION_LABEL = {
    "Info": "Note",
    "Note": "Note",
    "Warning": "Warning",
    "Danger": "Danger",
}


def live_url(stem: str) -> str:
    return f"{DOCS_BASE}/{stem.replace('__', '/')}"


# --------------------------------------------------------------------------- links


def rewrite_link_target(target: str, self_file: str | None = None) -> str | None:
    """Map an upstream link target onto a sibling file or an absolute docs URL.

    Returns None when the link points at the page being rendered: a self-link adds
    no navigation, so the caller keeps the link text as plain prose instead.
    """
    if not target.startswith("/developers/"):
        return target
    rest = target[len("/developers/") :]
    path, _, anchor = rest.partition("#")
    sibling = SIBLINGS.get(path.rstrip("/"))
    if sibling is not None:
        if sibling == self_file:
            return None
        # Anchors are upstream-specific; link to the sibling file itself.
        return sibling
    return f"{DOCS_BASE}/{path}" + (f"#{anchor}" if anchor else "")


LINK_RE = re.compile(r"\[([^\]]*)\]\((/developers/[^)\s]*)\)")


def rewrite_links(text: str, self_file: str | None = None) -> str:
    def sub(m: re.Match[str]) -> str:
        label, target = m.group(1), m.group(2)
        new_target = rewrite_link_target(target, self_file)
        if new_target is None:
            return label
        return f"[{label}]({new_target})"

    return LINK_RE.sub(sub, text)


# --------------------------------------------------------------------------- routes

ROUTE_RE = re.compile(r"<Route\s+method=\"([A-Z]+)\">(.*?)</Route>")
# a path parameter rendered as a markdown link: [\{channel.id}](/developers/...)
PARAM_LINK_RE = re.compile(r"\[\\?\{([^}]*)\}\]\([^)]*\)")


def clean_route_path(raw: str) -> str:
    """Reduce a Route body to the bare path with {param} placeholders."""
    path = PARAM_LINK_RE.sub(lambda m: "{" + m.group(1).replace("\\_", "_") + "}", raw)
    # any residual markdown link keeps its text only
    path = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", path)
    path = path.replace("\\_", "_").replace("\\{", "{").replace("\\}", "}")
    return path.strip()


def convert_routes(line: str) -> str:
    def sub(m: re.Match[str]) -> str:
        return f"### {m.group(1)} {clean_route_path(m.group(2))}"

    return ROUTE_RE.sub(sub, line)


# --------------------------------------------------------------------------- body

PREAMBLE_RE = re.compile(r"^>\s*(## Documentation Index|Fetch the complete|Use this file)")
EXPORT_START_RE = re.compile(r"^export const (Route|ManualAnchor)\s*=")
MANUAL_ANCHOR_RE = re.compile(r"^\s*<ManualAnchor\s+id=\"[^\"]*\"\s*/>\s*$")
# Upstream also places an anchor inline inside a heading (e.g. soundboard's
# '###### JSON <ManualAnchor .../>'), so strip the tag anywhere it occurs.
MANUAL_ANCHOR_INLINE_RE = re.compile(r"\s*<ManualAnchor\s+id=\"[^\"]*\"\s*/>")
ADMONITION_OPEN_RE = re.compile(r"^(\s*)<(Info|Note|Warning|Danger)>\s*$")
ADMONITION_CLOSE_RE = re.compile(r"^(\s*)</(Info|Note|Warning|Danger)>\s*$")
ACCORDION_OPEN_RE = re.compile(r"^(\s*)<Accordion\s+(.*)>\s*$")
ACCORDION_CLOSE_RE = re.compile(r"^(\s*)</Accordion>\s*$")
ATTR_RE = re.compile(r'(\w+)="([^"]*)"')


def strip_scaffolding(lines: list[str]) -> list[str]:
    """Drop the MDX preamble and the export const JS declarations."""
    out: list[str] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if PREAMBLE_RE.match(line):
            i += 1
            continue
        if EXPORT_START_RE.match(line):
            # consume until the closing '};' at column 0
            i += 1
            while i < n and not lines[i].startswith("};"):
                i += 1
            i += 1  # the '};' itself
            continue
        if MANUAL_ANCHOR_RE.match(line):
            i += 1
            continue
        out.append(MANUAL_ANCHOR_INLINE_RE.sub("", line))
        i += 1
    return out


def dedent_block(block: list[str], indent: int) -> list[str]:
    """Remove `indent` leading spaces from every non-blank line."""
    res = []
    for line in block:
        if line.strip() and line.startswith(" " * indent):
            res.append(line[indent:])
        else:
            res.append(line)
    return res


def convert_containers(lines: list[str]) -> list[str]:
    """Turn <Info>/<Warning>/<Note>/<Danger> and <Accordion> into plain markdown.

    Admonitions become a bold-labelled blockquote; accordions become a bold title
    line plus their (dedented) body, so no content is hidden behind a widget.
    """
    out: list[str] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]

        m = ADMONITION_OPEN_RE.match(line)
        if m:
            base_indent, kind = m.group(1), m.group(2)
            body: list[str] = []
            i += 1
            while i < n and not ADMONITION_CLOSE_RE.match(lines[i]):
                body.append(lines[i])
                i += 1
            i += 1  # closing tag
            inner = len(base_indent) + 2
            body = dedent_block(body, inner)
            while body and not body[0].strip():
                body.pop(0)
            while body and not body[-1].strip():
                body.pop()
            label = ADMONITION_LABEL[kind]
            # Rendered as a bold label plus a plain body rather than a blockquote:
            # upstream admonitions contain fenced code blocks and tables, which a
            # '> ' prefix would break.
            out.append(f"{base_indent}**{label}:**")
            out.append("")
            out.extend(body)
            out.append("")
            continue

        m = ACCORDION_OPEN_RE.match(line)
        if m:
            base_indent, attrs = m.group(1), m.group(2)
            a = dict(ATTR_RE.findall(attrs))
            body = []
            i += 1
            while i < n and not ACCORDION_CLOSE_RE.match(lines[i]):
                body.append(lines[i])
                i += 1
            i += 1
            body = dedent_block(body, len(base_indent) + 2)
            while body and not body[0].strip():
                body.pop(0)
            while body and not body[-1].strip():
                body.pop()
            title = a.get("title", "")
            desc = a.get("description", "")
            heading = f"{base_indent}**{title}**"
            if desc:
                heading += f" — {desc}"
            out.append(heading)
            out.append("")
            out.extend(body)
            out.append("")
            continue

        out.append(line)
        i += 1
    return out


def normalise_headings(lines: list[str]) -> list[str]:
    """Promote the upstream's six-hash sub-labels to a level a reader can navigate.

    Upstream uses `######` for every table label ("Field", "JSON Params", enum names)
    and `###`/`####` for object sections, under a `##` per topic. The page's own `#`
    title is dropped: the reference file supplies its own H1.
    """
    out: list[str] = []
    in_fence = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        stripped = line.lstrip()
        if stripped.startswith("###### "):
            # Upstream uses '######' for every table label; promote it so the
            # heading is navigable. Accordion bodies are already dedented by
            # convert_containers, so a leading-space variant cannot survive here.
            out.append("#### " + stripped[len("###### ") :])
        else:
            out.append(line)
    return out


def collapse_blanks(lines: list[str]) -> list[str]:
    out: list[str] = []
    in_fence = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        if not line.strip() and out and not out[-1].strip():
            continue
        out.append(line.rstrip())
    return out


# --------------------------------------------------------------------------- TOC


def build_toc(lines: list[str]) -> list[str]:
    """Table of contents over the `##` sections, as required for files over 100 lines."""
    entries: list[str] = []
    in_fence = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith("## ") and not line.startswith("###"):
            title = line[3:].strip()
            slug = slugify(title)
            entries.append(f"- [{title}](#{slug})")
    if not entries:
        return []
    return ["## Contents", ""] + entries + [""]


def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"`", "", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[^a-z0-9 \-_]", "", s)
    s = s.strip().replace(" ", "-")
    return re.sub(r"-+", "-", s)


# --------------------------------------------------------------------------- render


def render_page(stem: str, raw: str) -> str:
    out_name, title = PAGES[stem]
    url = live_url(stem)
    sha = hashlib.sha256(raw.encode()).hexdigest()

    lines = raw.split("\n")
    lines = strip_scaffolding(lines)
    lines = convert_containers(lines)

    # drop the page's own H1 and the one-line blockquote subtitle beneath it
    body: list[str] = []
    subtitle = ""
    seen_h1 = False
    for line in lines:
        if not seen_h1 and line.startswith("# "):
            seen_h1 = True
            continue
        # The one-line blockquote directly beneath the H1 is the page subtitle; it is
        # re-emitted in the generated header, above the table of contents.
        if seen_h1 and not subtitle and line.startswith("> ") and not [b for b in body if b.strip()]:
            subtitle = line[2:].strip()
            continue
        body.append(line)

    body = normalise_headings(body)
    body = [convert_routes(ln) for ln in body]
    body = [rewrite_links(ln, out_name) for ln in body]
    body = collapse_blanks(body)

    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()

    header = [
        f"<!-- generated by scripts/build_rest_reference.py from {stem}.md "
        f"sha256:{sha[:12]} — do not edit by hand -->",
        "",
        f"# Discord REST: {title}",
        "",
    ]
    if subtitle:
        header += [f"{subtitle}", ""]
    header += [
        f"Source: [{url}]({url}) — retrieved {RETRIEVED}.",
        "",
    ]

    toc = build_toc(body) if len(body) + len(header) > 100 else []
    text = "\n".join(header + toc + body).rstrip() + "\n"
    return text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mirror", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    drift = 0
    for stem in sorted(PAGES):
        src = args.mirror / f"{stem}.md"
        if not src.exists():
            print(f"MISSING SOURCE {src}", file=sys.stderr)
            drift += 1
            continue
        text = render_page(stem, src.read_text())
        dest = args.out / PAGES[stem][0]
        if args.check:
            current = dest.read_text() if dest.exists() else ""
            status = "OK" if current == text else "DRIFT"
            if status == "DRIFT":
                drift += 1
            print(f"{status:6} {dest.name}")
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(text)
            print(f"wrote {dest.name} ({len(text.splitlines())} lines)")
    return 1 if drift else 0


if __name__ == "__main__":
    raise SystemExit(main())
