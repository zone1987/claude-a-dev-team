#!/usr/bin/env python3
"""Check a plugin against every blocking rule in rules.json.

lang-01-pattern-definitions: this file holds the German stopword patterns, so LANG-01 skips it.

The rules live in rules.json, not in this file, so the wording a reader sees in RULES.md is the
wording applied here. Judgement-bound rules are listed by --rules and applied by
claude-component-reviewer; this script decides only what a script can decide.

Usage:
    validate_plugin.py --plugin <name> [--strict] [--json]
    validate_plugin.py --file <path> [--json]          # one file, for the PreToolUse gate
    validate_plugin.py --working-set <name> [<name>…]  # combined listing cost
    validate_plugin.py --rules                          # the catalogue and its classes
    validate_plugin.py --unlisted                        # skills/ dirs absent from skills[]

Exit: 0 clean, 1 errors, 2 warnings only (--strict promotes to 1), 3 bad arguments.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

PLUGIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(PLUGIN_DIR))
RULES_PATH = os.path.join(PLUGIN_DIR, "rules.json")

OVERHEAD = 109          # measured per-entry listing overhead, anthropics/claude-code#64606
BUDGET = 8000           # 1% of a 200k context window
ENTRY_CAP = 1536        # documented per-entry cap
DESC_MAX = 200          # DESC-01
BODY_MAX = 120          # SIZE-01
TOC_MIN = 100           # TOC-01
MAX_VISIBLE = 12        # COUNT-01
MAX_PRELOAD = 3         # AGENT-03

SPEC_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
FORBIDDEN_SKILL_FIELDS = {"triggers", "when_to_use", "paths"}
AGENT_FORBIDDEN = {"hooks", "mcpServers", "permissionMode"}
AGENT_REQUIRED = {"name", "description"}
COMMAND_REQUIRED = {"name", "description", "argument-hint", "allowed-tools", "model"}
RESERVED_NAME_WORDS = ("anthropic", "claude")

GENERIC_ANCHORS = {
    "product", "products", "booking", "bookings", "pricing", "availability", "cart", "unit",
    "units", "option", "options", "component", "components", "test", "tests", "build", "theme",
    "skill", "skills", "agent", "agents", "command", "commands", "hook", "hooks", "plugin",
    "plugins", "source", "sources", "page", "pages", "field", "fields", "file", "files",
}

# Case-insensitive for words German capitalises at the start of a sentence. 'mit' is excluded
# here and checked case-sensitively below, because 'MIT' is the licence identifier in every
# plugin.json and would otherwise flag all of them.
GERMAN_WORDS = re.compile(
    r"\b(der|die|das|und|werden|müssen|wird|für|kann|sich)\b", re.I)
GERMAN_MIT = re.compile(r"\bmit\b")
GERMAN_TRANSLIT = re.compile(
    r"\b(fuer|ueber|koennen|muessen|vollstaendig|zusaetzlich|groesse)\b", re.I)
GERMAN_STEMS = re.compile(
    r"(plattform|uebersicht|einstellung|verwaltung|beispiel|anleitung|referenz)", re.I)
# A file carrying this marker defines the language patterns and would match every one of them.
SELF_EXEMPT = re.compile(r"lang-01-pattern-definitions")
# Reference files are SCREAMING-CASE.md (REF-01), which keeps them distinguishable from SKILL.md
# at a glance. Nothing in the platform requires it; see the rule's grounding in rules.json.
REFERENCE_NAME = re.compile(r"^[A-Z][A-Z0-9-]*\.md$")
LOWER_PATH = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
MD_LINK = re.compile(r"\[[^\]]+\]\(([^)\s#]+)")
TRUTHY = {"true", "yes", "on", "1"}


class Report:
    """Findings, ordered as they are added, each carrying its rule id."""

    def __init__(self) -> None:
        self.items: list[dict] = []

    def add(self, sev: str, rule: str, path: str, msg: str, line: int = 0) -> None:
        self.items.append({"severity": sev, "rule": rule, "path": path,
                           "line": line, "message": msg})

    def error(self, rule: str, path: str, msg: str, line: int = 0) -> None:
        self.add("error", rule, path, msg, line)

    def warn(self, rule: str, path: str, msg: str, line: int = 0) -> None:
        self.add("warning", rule, path, msg, line)

    @property
    def errors(self) -> int:
        return sum(1 for i in self.items if i["severity"] == "error")

    @property
    def warnings(self) -> int:
        return sum(1 for i in self.items if i["severity"] == "warning")


def frontmatter(path: str) -> tuple[dict, int, list[str]]:
    """Parse YAML frontmatter far enough for these checks.

    Returns the mapping, the line the body starts on, and the body lines. A full YAML parser is
    deliberately avoided: this runs inside a PreToolUse gate, where import cost is latency, and
    latency on that event means the gate silently stops gating.
    """
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError:
        return {}, 0, []
    return parse_frontmatter(text)


def parse_frontmatter(text: str) -> tuple[dict, int, list[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, 0, lines
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return {}, 0, lines
    out: dict[str, str] = {}
    key: str | None = None
    buf: list[str] = []
    for raw in lines[1:end]:
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if m:
            if key:
                out[key] = " ".join(buf).strip()
            key = m.group(1)
            val = m.group(2).strip()
            buf = [] if val in (">", "|", ">-", "|-", "") else [val]
        elif key is not None:
            buf.append(raw.strip().lstrip("- "))
    if key:
        out[key] = " ".join(buf).strip()
    for k, v in out.items():
        if len(v) > 1 and v[0] == v[-1] and v[0] in "\"'":
            out[k] = v[1:-1]
    return out, end + 1, lines[end + 1:]


def is_truthy(v: str) -> bool:
    return v.strip().lower() in TRUTHY


def model_visible(fm: dict) -> bool:
    return not is_truthy(fm.get("disable-model-invocation", ""))


def listing_cost(fm: dict, name: str) -> int:
    """Cost of one listing entry.

    A disable-model-invocation skill keeps its name in the listing, so it is not free: the
    documentation says the listing always contains every skill name.
    """
    if not model_visible(fm):
        return len(fm.get("name", name))
    return len(fm.get("description", "")) + len(fm.get("when_to_use", "")) + OVERHEAD


def load_rules() -> dict:
    with open(RULES_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def unbound_anchors(clause: str) -> list[str]:
    """Generic words in a Use when clause that no bound word rescues.

    A generic noun is fine once something identifies the domain: a brand word (OCTO, Shopware),
    a filename (SKILL.md), a path shape (agents/*.md), or an exact identifier (availabilityType).
    Reporting 'products' in 'OCTO or Ventrata products' would flag the very construction the rule
    asks for, so the test is whether the clause carries such a binder at all.
    """
    bound = bool(
        re.search(r"\b[A-Z][A-Za-z0-9]*[A-Z][A-Za-z0-9]*\b", clause)   # OCTO, PostToolUse
        or re.search(r"\b[a-z]+[A-Z][A-Za-z]*\b", clause)              # availabilityType
        or re.search(r"[\w*-]+\.(md|json|ya?ml|xml|php|py|ts|tsx|vue|js)\b", clause)
        or re.search(r"[\w-]+/[\w*.-]+", clause)                       # agents/*.md
        or re.search(r"\b[A-Z][a-z]+\b", clause)                       # Ventrata, Shopware
    )
    if bound:
        return []
    return [t for t in re.findall(r"[a-z][a-z-]{2,}", clause.lower()) if t in GENERIC_ANCHORS]


# What CLAUDE.md's language rule explicitly permits, so LANG-01 must not read it as prose:
# a source URL keeps its path (docs.shopware.com/de, docs.contao.org/manual/de), a code span or
# fenced block can hold German data, and a documented UI label stays with an English gloss beside
# it ("**Speichern** (Save)"). Reading any of these as a violation makes the check cry wolf, and a
# check nobody trusts is a check nobody runs.
URL_RE = re.compile(r"https?://\S+|\[[^\]]*\]\([^)]*\)")
CODE_SPAN_RE = re.compile(r"`[^`\n]*`")
GLOSSED_LABEL_RE = re.compile(r"\*\*[^*]+\*\*\s*\([A-Z][^)]*\)")
FENCE_RE = re.compile(r"^\s*```", re.M)


def prose_only(text: str) -> str:
    """Blank out what the language rule permits, keeping line numbers intact."""
    out, fenced = [], False
    for ln in text.split("\n"):
        if FENCE_RE.match(ln):
            fenced = not fenced
            out.append("")
            continue
        if fenced:
            out.append("")
            continue
        for rx in (URL_RE, GLOSSED_LABEL_RE, CODE_SPAN_RE):
            ln = rx.sub(lambda m: " " * len(m.group(0)), ln)
        out.append(ln)
    return "\n".join(out)


def first_german(text: str, rx) -> tuple[int, str] | None:
    """Line and word of the first German hit in prose, or None."""
    m = rx.search(prose_only(text))
    if not m:
        return None
    return text[:m.start()].count("\n") + 1, m.group(0)


def check_skill(path: str, rep: Report, cat: dict) -> None:
    """Every blocking rule that a single SKILL.md decides on its own."""
    fm, body_start, body = frontmatter(path)
    rel = os.path.relpath(path, REPO)
    if not fm:
        rep.error("FM-01", rel, "no YAML frontmatter")
        return

    name = fm.get("name", "")
    if not name:
        rep.error("NAME-02", rel, "no name field; the install directory name would be used, "
                                 "which for a marketplace install is a version string")
    else:
        if len(name) > 64:
            rep.error("NAME-01", rel, f"name is {len(name)} characters, limit 64")
        if not re.fullmatch(r"[a-z0-9-]+", name):
            rep.error("NAME-01", rel, f"name '{name}' allows only lowercase, digits and hyphens")
        for word in RESERVED_NAME_WORDS:
            if word in name.lower():
                rep.error("NAME-01", rel, f"name contains the reserved word '{word}'")

    desc = fm.get("description", "")
    if not desc:
        rep.error("DESC-03", rel, "no description; Claude cannot tell when the skill applies")
    else:
        if len(desc) > DESC_MAX:
            rep.error("DESC-01", rel,
                      f"description is {len(desc)} characters, limit {DESC_MAX}")
        if len(desc) + len(fm.get("when_to_use", "")) > ENTRY_CAP:
            rep.error("BUDGET-03", rel, f"listing entry exceeds the {ENTRY_CAP}-character cap")
        if "\n" in desc:
            rep.error("DESC-02", rel, "description spans more than one line")
        if model_visible(fm) and ". Use when " not in desc and not desc.startswith("Use when "):
            rep.warn("DESC-03", rel,
                     "description states no trigger; the pattern is "
                     "'<Statement>. Use when <anchor>, <anchor>.'")
        if re.match(r"^(I |You |Use this|This skill)", desc):
            rep.error("DESC-04", rel, "description is not third person")
        if DESC_MAX - len(desc) < 10 and model_visible(fm):
            rep.warn("BUDGET-04", rel,
                     f"description leaves {DESC_MAX - len(desc)} characters of headroom")
        if model_visible(fm):
            clause = desc.split(". Use when ", 1)
            if len(clause) == 2:
                unbound = unbound_anchors(clause[1])
                if unbound:
                    rep.warn("ANCHOR-01", rel,
                             f"'{unbound[0]}' stands alone in the Use when clause; bind it to a "
                             "brand word, a filename or an exact identifier")

    for field in FORBIDDEN_SKILL_FIELDS & set(fm):
        rule = {"when_to_use": "FM-03", "paths": "FM-04"}.get(field, "FM-01")
        rep.error(rule, rel, f"field '{field}' does not belong in a skill here")
    if fm.get("context", "").strip() == "fork" and "## Reference map" in "\n".join(body):
        rep.error("FM-05", rel, "context: fork on a reference skill returns no output")
    extra = set(fm) - SPEC_FIELDS
    if extra:
        rep.warn("FM-02", rel,
                 "outside the six spec-legal fields, so a claude.ai upload fails hard: "
                 + ", ".join(sorted(extra)))

    if len(body) > BODY_MAX:
        rep.error("SIZE-01", rel, f"body is {len(body)} lines, limit {BODY_MAX}")
    if "## Source" not in "\n".join(body):
        rep.error("SRC-01", rel, "no '## Source' section")
    else:
        tail = "\n".join(body)
        src = tail[tail.index("## Source"):]
        if not re.search(r"https?://", src):
            rep.error("SRC-01", rel, "'## Source' names no URL")
        if not re.search(r"\b(20\d\d-\d\d-\d\d|sha256|[0-9a-f]{7,40}\b|v?\d+\.\d+)", src):
            rep.error("SRC-06", rel,
                      "'## Source' names no date, version or hash, so the age of the claim "
                      "cannot be judged")

    check_siblings(path, body, rep)


def strip_code(lines: list[str]) -> str:
    """Prose only. A fenced block holds example text, so a placeholder link inside it is not a
    link: reading one turns every template into a broken-link report."""
    out, fenced = [], False
    for ln in lines:
        if ln.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            out.append(ln)
    return "\n".join(out)


def check_siblings(skill_md: str, body: list[str], rep: Report) -> None:
    """Reference files: depth, casing, links, tables of contents."""
    d = os.path.dirname(skill_md)
    rel = os.path.relpath(skill_md, REPO)
    prose = strip_code(body)

    # DEPTH-01: what breaks a read is indirection, not the directory. A file linked as
    # references/X.md straight from SKILL.md is a direct reference and is read in full; one
    # reachable only through another reference is previewed with head -100.
    linked_rel = {t for t in MD_LINK.findall(prose) if t.endswith(".md")}
    reachable = {os.path.normpath(os.path.join(d, t)) for t in linked_rel}
    for nested in glob.glob(os.path.join(d, "*", "**", "*.md"), recursive=True):
        if os.path.normpath(nested) in reachable:
            continue
        rep.error("DEPTH-01", os.path.relpath(nested, REPO),
                  "no link in SKILL.md resolves to this file, so it is reachable only through "
                  "another reference and a head -100 preview hides everything past line 100")
    # REF-04: references live in references/ only. An index file inside it is a DEPTH-01
    # error, since every file behind it drops to a head -100 preview.
    for sub in sorted(glob.glob(os.path.join(d, "*", "*.md"))):
        if re.match(r"(INDEX|README|CONTENTS)\.md$", os.path.basename(sub)):
            rep.error("DEPTH-01", os.path.relpath(sub, REPO),
                      "an index file only points at other references, which downgrades every file "
                      "behind it to a head -100 preview; SKILL.md's reference map is the index")

    # Every reference, wherever it sits: references/ is the required home (REF-04), but the
    # name, link, content and TOC rules apply to a misplaced file just the same.
    refs = sorted(glob.glob(os.path.join(d, "*.md")) + glob.glob(os.path.join(d, "*", "*.md")))
    for sib in refs:
        base = os.path.basename(sib)
        if base == "SKILL.md":
            continue
        srel = os.path.relpath(sib, REPO)
        parent = os.path.basename(os.path.dirname(sib))
        if parent != "references":
            rep.error("REF-04", srel,
                      "a reference sits beside SKILL.md; move it to references/ and link it "
                      "directly from SKILL.md")
        if not REFERENCE_NAME.match(base):
            rep.error("REF-01", srel, f"'{base}' is not SCREAMING-CASE.md")
        if os.path.normpath(sib) not in reachable:
            rep.error("LINK-01", rel, f"'{base}' is never linked from SKILL.md, so it is unreachable")
        lines = open(sib, encoding="utf-8", errors="replace").read().splitlines()
        # REF-02: a file whose only job is to point at a sibling costs two reads per lookup.
        body = [ln for ln in lines if ln.strip() and not ln.startswith("#")]
        if len(lines) < 15 and body:
            pointed = [m for m in re.findall(r"`?([A-Z][A-Z0-9-]*\.md)`?", " ".join(body))
                       if m != base]
            if pointed and len(body) <= 3:
                rep.error("REF-02", srel,
                          f"carries no content of its own, only a pointer to {pointed[0]}; "
                          "merge the two files")
        sections = sum(1 for ln in lines if ln.startswith("## "))
        if len(lines) > TOC_MIN and sections >= 3:
            head = "\n".join(lines[:20]).lower()
            if "contents" not in head and "## toc" not in head:
                rep.error("TOC-01", srel,
                          f"{len(lines)} lines and {sections} sections but no table of contents")

    for target in MD_LINK.findall(prose):
        if target.startswith(("http", "mailto:", "<")):
            continue
        if not os.path.exists(os.path.join(d, target)):
            rep.error("LINK-01", rel, f"link target '{target}' does not exist")


def check_agent(path: str, rep: Report) -> None:
    fm, _, body = frontmatter(path)
    rel = os.path.relpath(path, REPO)
    if not fm:
        rep.error("AGENT-01", rel, "no YAML frontmatter")
        return
    for field in sorted(AGENT_REQUIRED - set(fm)):
        rep.error("AGENT-01", rel, f"no {field} field")
    for field in sorted(AGENT_FORBIDDEN & set(fm)):
        rep.error("AGENT-02", rel,
                  f"'{field}' is ignored for plugin subagents, so writing it creates "
                  "false confidence")
    if fm.get("isolation", "").strip() not in ("", "worktree"):
        rep.error("AGENT-02", rel, "only isolation: worktree is valid for a plugin agent")
    preload = [s for s in re.split(r"[,\s]+", fm.get("skills", "")) if s]
    if len(preload) > MAX_PRELOAD:
        rep.error("AGENT-03", rel,
                  f"preloads {len(preload)} skills; full content is injected at startup, "
                  f"so keep it to {MAX_PRELOAD}")
    text = "\n".join(body)
    for skill in preload:
        if skill not in text:
            rep.error("AGENT-03", rel,
                      f"preloads '{skill}' but never names it in the body; as a teammate only "
                      "tools and model apply, so skills: cannot be the mechanism")


def check_command(path: str, rep: Report) -> None:
    fm, _, _ = frontmatter(path)
    rel = os.path.relpath(path, REPO)
    if not fm:
        rep.error("AGENT-01", rel, "no YAML frontmatter")
        return
    for field in sorted(COMMAND_REQUIRED - set(fm)):
        rep.error("AGENT-01", rel, f"no {field} field")
    if "tools" in fm and "allowed-tools" not in fm:
        rep.error("AGENT-01", rel, "a command declares allowed-tools, not tools")


def check_hooks(path: str, rep: Report) -> None:
    rel = os.path.relpath(path, REPO)
    try:
        with open(path, encoding="utf-8") as fh:
            cfg = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        rep.error("HOOK-01", rel, f"unreadable: {exc}")
        return
    for event, entries in (cfg.get("hooks") or {}).items():
        for entry in entries:
            if event == "UserPromptSubmit" and "matcher" in entry:
                rep.error("HOOK-01", rel,
                          "UserPromptSubmit supports no matcher; it is silently ignored, "
                          "so match inside the script and return early")
            for h in entry.get("hooks", []):
                if h.get("type") != "command":
                    continue
                cmd = h.get("command")
                if isinstance(cmd, list):
                    rep.error("HOOK-05", rel,
                              "command is an array; Claude Code 2.1.238 rejects the exec form and "
                              "then fails to load the whole hooks file, so every hook here stops "
                              'firing. Use a string with the placeholder quoted: python3 '
                              '"${CLAUDE_PLUGIN_ROOT}/hooks/x.py"')
                elif isinstance(cmd, str) and "${" in cmd and '"${' not in cmd:
                    rep.error("HOOK-05", rel,
                              "the path placeholder is unquoted, so a path containing a space "
                              "splits into two arguments")
                if "timeout" not in h:
                    rep.error("HOOK-04", rel,
                              f"{event} hook sets no timeout; the command default is 600s, and a "
                              "timed-out PreToolUse hook does not block at all")
                elif h["timeout"] > 10:
                    rep.warn("HOOK-04", rel,
                             f"timeout {h['timeout']}s is slow for a synchronous gate")


def check_language(root: str, rep: Report) -> None:
    """LANG-01 and LANG-02: content and every path segment."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")]
        for seg in dirnames:
            srel = os.path.relpath(os.path.join(dirpath, seg), REPO)
            if not LOWER_PATH.match(seg) and seg != ".claude-plugin":
                rep.error("LANG-02", srel, f"directory '{seg}' is not lowercase kebab-case")
            if GERMAN_STEMS.search(seg):
                rep.error("LANG-02", srel, f"directory '{seg}' carries a German stem")
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            frel = os.path.relpath(full, REPO)
            if GERMAN_STEMS.search(fn):
                rep.error("LANG-02", frel, f"filename '{fn}' carries a German stem")
            if (fn.endswith(".md") and not REFERENCE_NAME.match(fn)
                    and not LOWER_PATH.match(fn)):
                rep.error("LANG-02", frel,
                          f"'{fn}' is neither SCREAMING-CASE.md nor lowercase")
            if not fn.endswith((".md", ".py", ".json", ".sh", ".yaml", ".yml")):
                continue
            try:
                text = open(full, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            if SELF_EXEMPT.search(text):
                continue        # this file defines the patterns, so it matches all of them
            for rx, rule, what in ((GERMAN_WORDS, "LANG-01", "German prose"),
                                   (GERMAN_MIT, "LANG-01", "German prose"),
                                   (GERMAN_TRANSLIT, "LANG-01", "transliterated German")):
                hit = first_german(text, rx)
                if hit:
                    line, word = hit
                    rep.error(rule, frel, f"{what}: '{word}'", line)
                    break


def skill_dirs(pdir: str) -> list[str]:
    return sorted(glob.glob(os.path.join(pdir, "skills", "*", "SKILL.md")))


def manifest(pdir: str) -> dict:
    p = os.path.join(pdir, ".claude-plugin", "plugin.json")
    try:
        with open(p, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, json.JSONDecodeError):
        return {}


def check_plugin(name: str, rep: Report, cat: dict) -> None:
    pdir = os.path.join(REPO, "plugins", name)
    if not os.path.isdir(pdir):
        print(f"no such plugin: {name}", file=sys.stderr)
        sys.exit(3)

    man = manifest(pdir)
    if not man:
        rep.error("MANIFEST-01", f"plugins/{name}/.claude-plugin/plugin.json",
                  "missing or unparseable")
    listed = [p.rstrip("/").split("/")[-1] for p in man.get("skills", [])]

    skills = skill_dirs(pdir)
    visible = 0
    total = 0
    for sm in skills:
        check_skill(sm, rep, cat)
        fm, _, _ = frontmatter(sm)
        sname = os.path.basename(os.path.dirname(sm))
        total += listing_cost(fm, sname)
        if model_visible(fm):
            visible += 1
        if sname not in listed:
            rep.error("BUDGET-05", os.path.relpath(sm, REPO),
                      "under skills/ but absent from skills[]; the field adds to the default "
                      "scan rather than restricting it, so this skill loads and costs budget")

    if "category" in man:
        rep.error("MANIFEST-04", f"plugins/{name}/.claude-plugin/plugin.json",
                  "category belongs in the marketplace entry; Claude Code ignores it here and "
                  "claude plugin validate --strict fails on it")

    for entry in man.get("skills", []):
        target = os.path.join(pdir, entry, "SKILL.md")
        if not os.path.exists(target):
            rep.error("MANIFEST-02", f"plugins/{name}/.claude-plugin/plugin.json",
                      f"skills[] names '{entry}' but it holds no SKILL.md, which breaks loading")

    if visible > MAX_VISIBLE:
        rep.error("COUNT-01", f"plugins/{name}",
                  f"{visible} model-visible skills, limit {MAX_VISIBLE}")
    if total > BUDGET:
        rep.error("BUDGET-01", f"plugins/{name}",
                  f"listing cost {total} exceeds the {BUDGET}-character budget on its own")

    mp = os.path.join(REPO, ".claude-plugin", "marketplace.json")
    if os.path.exists(mp):
        with open(mp, encoding="utf-8") as fh:
            entries = {e["name"]: e for e in json.load(fh).get("plugins", [])}
        entry = entries.get(name)
        if entry is None:
            rep.error("MANIFEST-01", ".claude-plugin/marketplace.json",
                      f"'{name}' is not registered")
        elif entry.get("skills") != man.get("skills"):
            rep.error("MANIFEST-01", ".claude-plugin/marketplace.json",
                      "skills[] differs from plugin.json")

    for a in sorted(glob.glob(os.path.join(pdir, "agents", "*.md"))):
        check_agent(a, rep)
    for c in sorted(glob.glob(os.path.join(pdir, "commands", "*.md"))):
        check_command(c, rep)
    hj = os.path.join(pdir, "hooks", "hooks.json")
    if os.path.exists(hj):
        check_hooks(hj, rep)
    check_language(pdir, rep)

    rep.stats = {"skills": len(skills), "visible": visible, "chars": total,
                 "budget_pct": round(total / BUDGET * 100, 1)}


def check_file(path: str, rep: Report, cat: dict) -> None:
    """One file, for the PreToolUse gate. Ordered so the common case exits first."""
    rel = os.path.relpath(os.path.abspath(path), REPO)
    if not rel.startswith("plugins/"):
        return
    base = os.path.basename(path)
    if base == "SKILL.md":
        check_skill(path, rep, cat)
    elif "/agents/" in rel and base.endswith(".md"):
        check_agent(path, rep)
    elif "/commands/" in rel and base.endswith(".md"):
        check_command(path, rep)
    elif base == "hooks.json":
        check_hooks(path, rep)


def working_set(names: list[str]) -> int:
    print(f"{'plugin':32} {'visible':>8} {'chars':>8} {'% budget':>9}")
    print("-" * 62)
    total = 0
    for n in names:
        pdir = os.path.join(REPO, "plugins", n)
        cost = vis = 0
        for sm in skill_dirs(pdir):
            fm, _, _ = frontmatter(sm)
            cost += listing_cost(fm, os.path.basename(os.path.dirname(sm)))
            vis += model_visible(fm)
        total += cost
        print(f"{n:32} {vis:8} {cost:8} {cost / BUDGET * 100:8.1f}%")
    print("-" * 62)
    print(f"{'TOTAL':32} {'':8} {total:8} {total / BUDGET * 100:8.1f}%")
    if total > BUDGET:
        print(f"\nover budget by {total - BUDGET} characters: the least-used skills in this set "
              "lose their descriptions and stop activating", file=sys.stderr)
        return 1
    print(f"\ninside budget, {BUDGET - total} characters of headroom")
    return 0


def unlisted() -> int:
    """Skill directories that load but are not in skills[]. See BUDGET-05."""
    found = 0
    for pdir in sorted(glob.glob(os.path.join(REPO, "plugins", "*"))):
        if not os.path.isdir(pdir):
            continue
        listed = {p.rstrip("/").split("/")[-1] for p in manifest(pdir).get("skills", [])}
        present = {os.path.basename(os.path.dirname(s)) for s in skill_dirs(pdir)}
        empty = {os.path.basename(d) for d in glob.glob(os.path.join(pdir, "skills", "*"))
                 if os.path.isdir(d)} - present
        extra = sorted(present - listed)
        name = os.path.basename(pdir)
        if extra or empty:
            found += len(extra) + len(empty)
            print(f"{name}:")
            for s in extra:
                print(f"  UNLISTED  skills/{s} loads anyway and costs listing budget")
            for s in sorted(empty):
                print(f"  NO SKILL  skills/{s} holds no SKILL.md")
    print("every skills/ directory is listed" if not found else f"\n{found} finding(s)")
    return 1 if found else 0


def show_rules(cat: dict) -> int:
    by_class: dict[str, int] = {}
    print(f"{len(cat['rules'])} rules, retrieved {cat['retrieved']}\n")
    print(f"{'id':14} {'ground':11} {'enforcement':12} rule")
    print("-" * 100)
    for r in cat["rules"]:
        by_class[r["ground"]] = by_class.get(r["ground"], 0) + 1
        print(f"{r['id']:14} {r['ground']:11} {r['enforcement']:12} {r['rule'][:60]}")
    print("-" * 100)
    print("  ".join(f"{k}: {v}" for k, v in sorted(by_class.items())))
    print("\nA 'review' rule is judgement-bound: no script decides it, and claude-component-reviewer "
          "applies it using the tell recorded in RULES.md.")
    return 0


def emit(rep: Report, as_json: bool, strict: bool) -> int:
    if as_json:
        print(json.dumps({"findings": rep.items, "errors": rep.errors,
                          "warnings": rep.warnings,
                          "stats": getattr(rep, "stats", {})}, indent=2))
    else:
        for i in rep.items:
            loc = f"{i['path']}:{i['line']}" if i["line"] else i["path"]
            mark = "✗" if i["severity"] == "error" else "!"
            print(f"  {mark} {loc}: [{i['rule']}] {i['message']}")
        st = getattr(rep, "stats", None)
        if st:
            print(f"\n{st['skills']} skills, {st['visible']} model-visible, "
                  f"{st['chars']} characters, {st['budget_pct']}% of budget")
        if not rep.items:
            print("clean")
        else:
            print(f"\n{rep.errors} error(s), {rep.warnings} warning(s)")
    if rep.errors:
        return 1
    if rep.warnings:
        return 1 if strict else 2
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plugin")
    ap.add_argument("--file")
    ap.add_argument("--working-set", nargs="+")
    ap.add_argument("--rules", action="store_true")
    ap.add_argument("--unlisted", action="store_true")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    cat = load_rules()
    if args.rules:
        return show_rules(cat)
    if args.unlisted:
        return unlisted()
    if args.working_set:
        return working_set(args.working_set)

    rep = Report()
    if args.file:
        check_file(args.file, rep, cat)
    elif args.plugin:
        check_plugin(args.plugin, rep, cat)
    else:
        ap.print_usage(sys.stderr)
        return 3
    return emit(rep, args.json, args.strict)


if __name__ == "__main__":
    sys.exit(main())
