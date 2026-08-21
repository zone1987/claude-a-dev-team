---
name: zcf-source-distillation
description: 'Turns upstream docs, OpenAPI and repositories into linked reference files with a coverage audit. Use when distilling a docs site or openapi.yaml into SKILL.md reference files.'
---

# Distilling a source

Two obligations, and neither may be traded for the other. **Complete**: every endpoint, field,
option, value, default, error and caveat the upstream states, extracted rather than recalled.
**Frugal**: it costs almost nothing until read. These conflict only if you think in files: the
description spends budget, reference files do not.

`octo-api` is the proof in this marketplace: 139 schemas, 65 operations, 1,787 field entries across
7,736 lines, for **2,392 characters** of listing cost.

The full rule set is [`RULES.md`](../../RULES.md). IDs below name the rules each step applies.

## Enumerate before extracting

An inventory is what turns "we covered it" from a claim into a check, because it supplies the
denominator. Prefer the **original documentation** over any write-up of it. `SOURCE-01`, `SRC-05`

| Source | How to enumerate |
|---|---|
| Docs site | `/sitemap.xml`, then `/sitemap-pages.xml`, `/sitemap_index.xml`, `/sitemap-0.xml`; `robots.txt` names an unusual path |
| OpenAPI, JSON Schema | the document itself: paths, operations, schemas, enums |
| GitHub, GitLab | **no sitemap exists**; list the tree at a pinned ref, and record the commit sha as the version |
| Typed export, CLI | the type declarations, `--help` output |

Many docs sites serve a markdown twin of each page at the same path plus `.md`, far cheaper to read
than rendered HTML. Try it first.

## Generate, never recall

Facts from a machine-readable source are produced by a script, with **no model between the
specification and the reference file**. A model in that path paraphrases a type or drops an enum
value silently; a script cannot. `SOURCE-02`

## Every page, and everything on it

**A plugin claiming a product's developer documentation carries every page of it.** Not a selection,
not the important ones. A developer reaches for the plugin precisely on the question the
documentation answers in a corner, and one missing page sends them to the upstream site, where they
will go first next time too. Partial coverage is worth less than half of full coverage, because the
reader cannot tell which half they have. `COV-06`

The developer documentation carries the stricter bar of the two. A user manual describes a screen the
reader can also look at; developer documentation describes an API they cannot guess.

The unit of completeness is the **page**: it is done when every term a reader could look up on it
appears in a reference file. Mapping a page to a file is only half of that. `COV-03`

Distillation removes redundancy of expression, **never information**. A field keeps its type, an enum
every value with its meaning, a procedure every step, a command its exact form, a policy its exact
boundary. Where the upstream is silent, say so, because a blank reads as absence. `COV-04`, `COV-07`

**Where the upstream page is itself thin, say that too.** "The page states only a package name and
points at the vendor's own documentation" is a useful fact; a silently skipped page is not.

## Prove it, both directions

- **Forward**: every enumerated unit maps to a file, so a page added upstream later surfaces as
  `UNCOVERED` instead of going unnoticed. `COV-01`
- **Reverse**: every identifier the plugin documents exists in the source. **This is the direction
  that catches invention**, and it is why no parameter can be quietly dropped. `COV-02`

```bash
python3 scripts/audit_coverage.py --plugin <name> --sitemap <url>   # or --spec, --repo
```

Read a **local mirror** rather than the live site, and record its hash, so a coverage claim stays
reproducible months later. `COV-05`

## API sources have a fixed contract

An API plugin exists to be the specialist for that API, so nothing is summarised away: every
operation with its method, path, parameter groups, request body, **every** response status, and a
worked request and response example including the error shapes. Every parameter and property carries
its type, format, optionality, nullability, possible values, default, constraints, example and the
upstream description. The exact facet list is [`API-CONTRACT.md`](references/API-CONTRACT.md). `API-01` to `API-06`

## Reference map

- **[SOURCE-INVENTORY.md](references/SOURCE-INVENTORY.md)**: enumerating each source kind, the sitemap variants,
  and how to mirror a source reproducibly.
- **[EXTRACTION-STRATEGY.md](references/EXTRACTION-STRATEGY.md)**: script-generated versus hand-written, how to
  split a source into skills, and what belongs in the map rather than a reference.
- **[API-CONTRACT.md](references/API-CONTRACT.md)**: the per-operation and per-parameter facets, with the
  rendering shape and what to write when the upstream is silent.
- **[COVERAGE-AUDIT.md](references/COVERAGE-AUDIT.md)**: the two-direction proof, `UNCOVERED`/`DANGLING`/`STALE`,
  and why an exclusion list carries a reason per entry.
- **[CITATION.md](references/CITATION.md)**: what a citation must let a reader do, and the three places one goes.
- **[DRIFT-STATE.md](references/DRIFT-STATE.md)**: the state file, `--check` and `--apply`, and why nothing polls
  at session start.

## Related

Call the Skill tool with "zcf-skill-authoring" for the `SKILL.md` the references hang off.

## Source

Method generalised from `plugins/octo-api/scripts/` in this marketplace (`check_sitemap.py`,
`audit_pages.py`, `verify_spec.py`), read 2026-08-21. Platform facts from
[skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices),
retrieved 2026-08-21. Rule wording lives in [`rules.json`](../../rules.json) v1.0.0.
