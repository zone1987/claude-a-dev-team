#!/usr/bin/env python3
"""Verify that every rule in rules.json is grounded, and that every quotation is real.

Checks both directions, which is what makes the catalogue trustworthy:

  forward   every rule carries the grounding its class demands
  reverse   every quotation appears verbatim on the page it cites

The reverse check is the one that catches invention: a plausible-sounding rule with a quotation
nobody can find on the cited page fails here. Without it, a remembered claim acquires authority
merely by sitting in a table with a URL beside it.

Network access is needed only for --fetch. The default run is offline and checks structure,
so nothing here runs at session start.

Usage:
    verify_sources.py [--check] [--fetch] [--apply] [--pages DIR]
Exit code is non-zero on any discrepancy.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request

PLUGIN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULES = os.path.join(PLUGIN, "rules.json")
STATE = os.path.join(PLUGIN, ".forge-state.json")

REQUIRED = {
    "documented": (("source",), ("url", "quote", "retrieved")),
    "technique": (("effect", "measurement"), ()),
    "convention": (("purpose", "not-a-platform-requirement"), ()),
}


def normalise(text: str) -> str:
    """Reduce page and quotation to the same plain prose before comparing.

    Three transforms, each answering a real false negative seen while building this catalogue:
    a renderer turns straight quotes curly and hyphens into dashes; the page keeps Markdown
    inline code around identifiers a quotation writes bare (`description` against description);
    and the page wraps terms in doc links whose target the quotation never carries. Without
    these, a quotation genuinely present reports as absent, which is worse than no check at all:
    it teaches the reader to distrust a passing run.
    """
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'),
                 ("\u2013", "-"), ("\u2014", "-"), ("\u00a0", " ")):
        text = text.replace(a, b)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)      # [label](target) -> label
    text = text.replace("`", "").replace("**", "").replace("*", "")
    return re.sub(r"\s+", " ", text).strip()


def check_structure(cat: dict) -> list[str]:
    """Forward: every rule carries the grounding its class demands."""
    problems = []
    seen: set[str] = set()
    for r in cat["rules"]:
        rid = r.get("id", "<no id>")
        if rid in seen:
            problems.append(f"{rid}: duplicate id")
        seen.add(rid)
        ground = r.get("ground")
        if ground not in REQUIRED:
            problems.append(f"{rid}: ground '{ground}' is not one of {sorted(REQUIRED)}")
            continue
        top, nested = REQUIRED[ground]
        for key in top:
            if not r.get(key):
                problems.append(f"{rid}: {ground} rule carries no '{key}'")
        for key in nested:
            if not (r.get("source") or {}).get(key):
                problems.append(f"{rid}: no source.{key}")
        if r.get("enforcement") not in ("blocking", "review"):
            problems.append(f"{rid}: enforcement '{r.get('enforcement')}' is not blocking or review")
        if r.get("enforcement") == "review" and ground != "documented" and not r.get("tell"):
            problems.append(f"{rid}: judgement-bound but carries no tell, so a reviewer has "
                            "nothing to recognise the mistake by")
        if not r.get("rule"):
            problems.append(f"{rid}: no rule text")
    return problems


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "zone-claude-forge/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def strip_html(html: str) -> str:
    html = re.sub(r"<(script|style)\b.*?</\1>", " ", html, flags=re.S | re.I)
    html = re.sub(r"<[^>]+>", " ", html)
    for ent, ch in (("&quot;", '"'), ("&#x27;", "'"), ("&#39;", "'"), ("&amp;", "&"),
                    ("&lt;", "<"), ("&gt;", ">"), ("&nbsp;", " "), ("&mdash;", "-"),
                    ("&ndash;", "-"), ("&rsquo;", "'"), ("&lsquo;", "'"),
                    ("&ldquo;", '"'), ("&rdquo;", '"')):
        html = html.replace(ent, ch)
    return html


def page_text(url: str, pages_dir: str, cache: dict) -> str | None:
    """Page body, from a local mirror when one is given, otherwise fetched once per URL."""
    base = url.split("#", 1)[0]
    if base in cache:
        return cache[base]
    text = None
    if pages_dir:
        slug = re.sub(r"[^a-z0-9]+", "-", base.split("://", 1)[-1].lower()).strip("-")
        for cand in (slug, slug + ".md", slug + ".html", slug + ".txt"):
            p = os.path.join(pages_dir, cand)
            if os.path.exists(p):
                text = open(p, encoding="utf-8", errors="replace").read()
                break
    if text is None and pages_dir:
        cache[base] = None
        return None
    if text is None:
        try:
            text = fetch(base)
        except (urllib.error.URLError, urllib.error.HTTPError, OSError) as exc:
            print(f"  fetch failed: {base}: {exc}", file=sys.stderr)
            cache[base] = None
            return None
    cache[base] = normalise(strip_html(text))
    return cache[base]


def check_quotes(cat: dict, pages_dir: str) -> tuple[list[str], dict]:
    """Reverse: every quotation appears verbatim on the page it cites."""
    problems: list[str] = []
    cache: dict[str, str | None] = {}
    hashes: dict[str, str] = {}
    documented = [r for r in cat["rules"] if r["ground"] == "documented"]
    for r in documented:
        src = r["source"]
        text = page_text(src["url"], pages_dir, cache)
        if text is None:
            problems.append(f"{r['id']}: could not read {src['url']}")
            continue
        hashes[src["url"].split('#', 1)[0]] = hashlib.sha256(text.encode()).hexdigest()[:16]
        quote = normalise(src["quote"])
        if quote in text:
            continue
        # A quotation assembled from a table row or two adjacent sentences is legitimate; check
        # its fragments before calling it absent, and say which fragment failed.
        parts = [p for p in re.split(r"(?<=[.;])\s+|\s*\|\s*", quote) if len(p) > 25]
        missing = [p for p in parts if p not in text]
        if parts and not missing:
            continue
        problems.append(f"{r['id']}: quotation not found on {src['url']}"
                        + (f" (fragment: {missing[0][:70]!r})" if missing else ""))
    return problems, hashes


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="structure only, offline (default)")
    ap.add_argument("--fetch", action="store_true", help="also verify every quotation")
    ap.add_argument("--apply", action="store_true", help="record hashes in .forge-state.json")
    ap.add_argument("--pages", default="", help="read pages from a local mirror instead")
    args = ap.parse_args()

    with open(RULES, encoding="utf-8") as fh:
        cat = json.load(fh)

    problems = check_structure(cat)
    counts = {c: sum(1 for r in cat["rules"] if r["ground"] == c) for c in REQUIRED}
    print(f"{len(cat['rules'])} rules: "
          + ", ".join(f"{v} {k}" for k, v in counts.items()))
    print("forward: every rule grounded"
          + (f" — {len(problems)} problem(s)" if problems else " — ok"))

    hashes: dict[str, str] = {}
    if args.fetch or args.pages:
        qp, hashes = check_quotes(cat, args.pages)
        print("reverse: every quotation verbatim on its page"
              + (f" — {len(qp)} problem(s)" if qp else " — ok"))
        problems += qp

    for p in problems:
        print(f"  ✗ {p}", file=sys.stderr)

    if args.apply and hashes:
        state = {}
        if os.path.exists(STATE):
            with open(STATE, encoding="utf-8") as fh:
                state = json.load(fh)
        state["rulesVersion"] = cat["version"]
        state["retrieved"] = cat["retrieved"]
        state["pages"] = hashes
        with open(STATE, "w", encoding="utf-8") as fh:
            json.dump(state, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"recorded {len(hashes)} page hash(es) in .forge-state.json")

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
