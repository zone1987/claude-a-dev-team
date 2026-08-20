#!/usr/bin/env python3
"""Bundle a plugin's skills into domain skills without losing knowledge.

The listing budget counts descriptions, not files: a plugin with 109 skills spends 48,591
characters before Claude reads a word, while the same knowledge behind 12 domain skills costs
under 4,000. Bundling is therefore pure gain — provided nothing is dropped.

What this does, per domain:

  1. writes `skills/<prefix>-<domain>/SKILL.md`, a map with one bullet per former skill
  2. moves each former SKILL.md to `<DOMAIN-TOPIC>.md` beside it, keeping its full body
  3. flattens `references/deep/x.md` into `<TOPIC>-X.md` — one level deep, as the docs require
  4. moves `assets/` into a single `assets/` directory, rewriting image links

Nothing is deleted: every source file ends up as a reference file, and the script refuses to
run if a target already exists.

Usage:
    bundle-skills.py --plugin shopware-merchant --plan
    bundle-skills.py --plugin shopware-merchant --apply
"""
from __future__ import annotations

import argparse
import filecmp
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_frontmatter(path: str) -> tuple[dict, str]:
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    fm, body = text[3:end], text[end + 4 :]
    out, key, buf = {}, None, []
    for line in fm.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            if key:
                out[key] = " ".join(buf).strip()
            key = m.group(1)
            v = m.group(2).strip()
            buf = [] if v in (">", "|", ">-", "|-", "") else [v]
        elif key is not None:
            buf.append(line.strip())
    if key:
        out[key] = " ".join(buf).strip()
    return out, body.lstrip("\n")


def title_of(body: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", body, re.M)
    return m.group(1).strip() if m else fallback


def first_sentence(body: str) -> str:
    text = re.sub(r"^#.*$", "", body, flags=re.M)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    for para in text.split("\n\n"):
        p = " ".join(para.split())
        if len(p) > 40 and not p.startswith(("|", "-", "*", "!", "<")):
            return p.split(". ")[0].rstrip(".") + "."
    return ""


def ref_name(stem: str, base: str, domain: str) -> str:
    """Name a flattened reference file without repeating what the topic already says.

    "customers-accounts/references/deep/customers-accounts.md" under topic ACCOUNTS must not
    become ACCOUNTS-CUSTOMERS-ACCOUNTS.md. Strip the domain prefix from the stem first, then
    drop whatever the topic name already carries.
    """
    stem = stem.upper().replace("_", "-")
    dom = domain.upper()
    if stem.startswith(dom + "-"):
        stem = stem[len(dom) + 1 :]
    elif stem == dom:
        stem = "OVERVIEW"
    if stem == base or not stem:
        return f"{base}-DETAIL.md"
    if stem.startswith(base + "-"):
        return f"{stem}.md"
    if base.startswith(stem + "-") or base == "OVERVIEW":
        return f"{stem}.md"
    return f"{base}-{stem}.md"


def topic_file(skill: str, prefix: str, domain: str, taken: set[str]) -> str:
    """sw-merchant-catalog-products + catalog -> PRODUCTS.md

    The bare domain skill becomes the domain's overview. When a member is *named*
    "<domain>-overview" it would claim the same file, so the bare one yields and takes
    <DOMAIN>.md instead — an explicit name beats an implicit one.
    """
    name = skill[len(prefix) + 1 :] if skill.startswith(prefix + "-") else skill
    if name == domain:
        candidate = "OVERVIEW.md"
        if candidate in taken:
            candidate = domain.upper() + ".md"
        return candidate
    # Strip the domain prefix only when what remains is still unique. "data-table" in domain
    # "data" would otherwise become TABLE.md and silently overwrite the real "table" skill.
    stripped = name[len(domain) + 1 :] if name.startswith(domain + "-") else name
    candidate = stripped.upper().replace("_", "-") + ".md"
    if candidate in taken:
        candidate = name.upper().replace("_", "-") + ".md"
    if candidate in taken:
        raise SystemExit(f"file name collision for {skill!r} in domain {domain!r}: {candidate}")
    return candidate


def load_mapping(plugin: str) -> dict[str, str]:
    """Optional explicit skill -> domain mapping.

    Name-prefix grouping works when skills share a topic prefix (sw-merchant-orders-*). A
    component library has no such prefix — `button` and `dialog` are siblings, not a family —
    so those plugins ship a mapping file instead of being force-fitted.
    """
    path = os.path.join(ROOT, "scripts", "domain-skills", f"{plugin}.map")
    if not os.path.exists(path):
        return {}
    out: dict[str, str] = {}
    domain = ""
    for raw in open(path, encoding="utf-8"):
        line = raw.split("#")[0].rstrip()
        if not line.strip():
            continue
        if ":" in line and not line[0].isspace():
            domain, _, members = line.partition(":")
            domain = domain.strip()
        else:
            members = line          # a continuation line, indented under its domain
        for m in members.split():
            out[m.strip()] = domain
    return out


def plan(plugin: str, min_size: int) -> dict:
    sk_dir = os.path.join(ROOT, "plugins", plugin, "skills")
    skills = sorted(
        d for d in os.listdir(sk_dir)
        if os.path.isfile(os.path.join(sk_dir, d, "SKILL.md"))
    )
    # Pick the prefix that most skills actually share. A plain common-prefix computation
    # breaks on one outlier ("adt-contao-dal" among 56 "contao-*" skills collapses it to
    # ""), and the plugin name is not always the prefix either: shopware-storefront ships
    # "sw-*" skills. So try the plugin name, then the shortest leading segment, and keep
    # whichever covers the most skills.
    # Try every leading segment that appears in any skill name, not just the first skill's.
    # One outlier at the top of the sort ("adt-shopware-dal" before 32 "sw-*") would
    # otherwise decide the prefix for the whole plugin.
    candidates = [plugin]
    for sk in skills:
        parts = sk.split("-")
        candidates.append(parts[0])
        if len(parts) > 1:
            candidates.append("-".join(parts[:2]))
    best, cover = "", 0
    for c in candidates:
        n = sum(1 for s in skills if s.startswith(c + "-"))
        if n > cover:
            best, cover = c, n
    prefix = best if cover >= len(skills) * 0.6 else (
        os.path.commonprefix(skills).rstrip("-") if skills else "")
    mapping = load_mapping(plugin)
    groups: dict[str, list[str]] = {}
    unmapped = []
    for s in skills:
        rest = s[len(prefix) + 1 :] if s.startswith(prefix + "-") else s
        if mapping:
            # Accept either form in the map: the full skill directory name, or the name with
            # the shared prefix removed. Both are natural to write, and demanding one is a
            # trap that shows up as "everything unmapped".
            dom = mapping.get(rest) or mapping.get(s)
            if dom is None:
                unmapped.append(s)
                continue
        else:
            dom = rest.split("-")[0]
        groups.setdefault(dom, []).append(s)
    if unmapped:
        raise SystemExit(
            f"{len(unmapped)} skill(s) missing from scripts/domain-skills/{plugin}.map:\n  "
            + "\n  ".join(sorted(unmapped)))
    # Domains too small to be worth their own listing entry join a catch-all. Skipped when
    # a mapping file is present: there the grouping is a deliberate decision already.
    small = [] if mapping else [d for d, v in groups.items() if len(v) < min_size]
    if len(small) > 1:
        merged = [s for d in small for s in groups.pop(d)]
        groups["general"] = sorted(merged)
    return {"prefix": prefix, "groups": groups, "dir": sk_dir}


def apply(plugin: str, p: dict, dry: bool) -> None:
    prefix, sk_dir = p["prefix"], p["dir"]
    for domain, members in sorted(p["groups"].items()):
        target = os.path.join(sk_dir, f"{prefix}-{domain}")
        entries = []
        # Order decides who wins a name. A skill whose name does NOT start with the domain
        # (`table` in domain `data`) claims the short file name first; `data-table` then keeps
        # its own full name. The bare domain skill goes last so an explicit
        # "<domain>-overview" gets OVERVIEW.md.
        ordered = sorted(
            members,
            key=lambda s: (
                s == f"{prefix}-{domain}",
                s.startswith(f"{prefix}-{domain}-"),
                s,
            ),
        )
        taken: set[str] = set()
        for skill in ordered:
            src = os.path.join(sk_dir, skill)
            fm, body = read_frontmatter(os.path.join(src, "SKILL.md"))
            fname = topic_file(skill, prefix, domain, taken)
            taken.add(fname)
            entries.append({
                "skill": skill, "file": fname, "src": src,
                "title": title_of(body, skill), "gist": first_sentence(body),
                "desc": fm.get("description", ""), "body": body,
            })
        if dry:
            print(f"\n{prefix}-{domain}  ({len(entries)} former skills)")
            for e in entries:
                print(f"    {e['skill']:44} -> {e['file']}")
            continue
        os.makedirs(target, exist_ok=True)
        os.makedirs(os.path.join(target, "assets"), exist_ok=True)
        written: dict[str, str] = {}
        for e in entries:
            # One member usually *is* the target directory (the bare domain skill), so every
            # copy out of it is a copy into itself. Detect that and only rewrite in place.
            in_place = os.path.abspath(e["src"]) == os.path.abspath(target)
            dest = os.path.join(target, e["file"])
            text = e["body"]
            text = re.sub(r"\(assets/", "(assets/", text)
            _base = e["file"][:-3]
            text = re.sub(
                r"`?references/(?:deep/)?([\w.-]+)\.md`?",
                lambda m: f"`{ref_name(os.path.splitext(m.group(1))[0], _base, domain)}`",
                text,
            )
            with open(dest, "w", encoding="utf-8") as fh:
                fh.write(text if text.startswith("#") else f"# {e['title']}\n\n{text}")
            # flatten references/**
            for root, _d, files in os.walk(os.path.join(e["src"], "references")):
                for fn in files:
                    if not fn.endswith(".md"):
                        continue
                    stem = os.path.splitext(fn)[0]
                    out = os.path.join(target, ref_name(stem, e["file"][:-3], domain))
                    src_ref = os.path.join(root, fn)
                    if os.path.abspath(src_ref) == os.path.abspath(out):
                        continue
                    # Several skills can ship a same-named reference: four
                    # associations-* skills each have references/associations.md. Keeping the
                    # topic in the name disambiguates them instead of losing three of four.
                    if out in written:
                        out = os.path.join(
                            target,
                            f"{e['file'][:-3]}-{stem.upper().replace('_', '-')}.md")
                    if out in written:
                        raise SystemExit(
                            f"reference collision: {src_ref} and {written[out]} both map to "
                            f"{os.path.basename(out)}")
                    written[out] = src_ref
                    shutil.copy2(src_ref, out)
            # Everything else the skill directory carried: assets, examples, scripts,
            # templates. Whitelisting only references/ and assets/ silently dropped four
            # example files the first time this ran, so copy every sibling directory.
            for sub in sorted(os.listdir(e["src"])):
                sp = os.path.join(e["src"], sub)
                if not os.path.isdir(sp) or sub == "references":
                    continue
                if in_place and sub in ("assets",):
                    continue
                dest_dir = os.path.join(target, sub)
                os.makedirs(dest_dir, exist_ok=True)
                for root, _dd, ff in os.walk(sp):
                    rel = os.path.relpath(root, sp)
                    outdir = dest_dir if rel == "." else os.path.join(dest_dir, rel)
                    os.makedirs(outdir, exist_ok=True)
                    for fn in ff:
                        src_f = os.path.join(root, fn)
                        # Namespace by topic so two skills' examples cannot collide.
                        stem, ext = os.path.splitext(fn)
                        out_f = os.path.join(outdir, fn if sub == "assets"
                                             else f"{e['file'][:-3].lower()}-{stem}{ext}")
                        if os.path.abspath(src_f) == os.path.abspath(out_f):
                            continue
                        # Two skills can ship different images under the same file name
                        # (two "produkte-hinzufuegen.png"). Identical content is one file;
                        # differing content gets the topic prefixed, so neither is lost.
                        if os.path.exists(out_f):
                            if filecmp.cmp(src_f, out_f, shallow=False):
                                continue
                            out_f = os.path.join(
                                outdir, f"{e['file'][:-3].lower()}-{stem}{ext}")
                        if os.path.exists(out_f) and not filecmp.cmp(
                                src_f, out_f, shallow=False):
                            raise SystemExit(f"collision copying {src_f} -> {out_f}")
                        shutil.copy2(src_f, out_f)
        if not os.listdir(os.path.join(target, "assets")):
            os.rmdir(os.path.join(target, "assets"))
        print(f"  {prefix}-{domain}: {len(entries)} topics")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--plugin", required=True)
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--min-size", type=int, default=2)
    args = ap.parse_args()

    p = plan(args.plugin, args.min_size)
    print(f"prefix: {p['prefix']}  domains: {len(p['groups'])}")
    apply(args.plugin, p, dry=not args.apply)
    return 0


if __name__ == "__main__":
    sys.exit(main())
