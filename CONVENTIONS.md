# Conventions — plugin marketplace

Binding rules for the structure, naming and layout of every plugin, skill, agent, command and hook
in this marketplace.

**[`CLAUDE.md`](./CLAUDE.md) is the higher authority on efficiency and completeness, and wins on
conflict.** This document translates it into concrete naming and layout rules. Read both before
adding or changing a skill.

Canonical source **per plugin**, never repository-wide:

| Plugin family | Canonical source |
|---|---|
| `shopware-*` | Shopware 6.7 trunk (`src/`, `adr/`, `coding-guidelines/`, `AGENTS.md`, `UPGRADE-*`, `changelog/`) plus developer.shopware.com and docs.shopware.com |
| `octo-api` | The Ventrata OpenAPI document plus the 39 pages of docs.ventrata.com |
| `contao` | Contao 5 source plus docs.contao.org, developer documentation and end-user manual |
| `shadcn`, `shadcn-vue`, `swiper`, `flatpickr`, `playwright`, `panther`, `gotenberg` | The upstream repository and its official documentation |

## Marketplace layout

```
claude-a-dev-team/
├── CLAUDE.md                           # efficiency rules — the higher authority
├── CONVENTIONS.md                      # this document
├── README.md
├── scripts/                            # the tooling that enforces both
│   ├── measure-skill-budget.py         # listing cost per plugin
│   ├── bundle-skills.py                # group skills into domains
│   ├── finish-bundle.sh                # clean up after bundling
│   ├── write-domain-skills.py          # write the domain maps
│   ├── verify-bundle.py                # prove nothing was lost
│   ├── register-plugin.py              # write both manifests consistently
│   ├── add-toc.py                       # tables of contents
│   ├── fix-links.py                     # repair links after renames
│   └── domain-skills/<plugin>.{map,json}
├── .claude-plugin/marketplace.json     # registers every plugin and its skills
└── plugins/
    └── <plugin>/
        ├── .claude-plugin/plugin.json  # name, version, description, author, license,
        │                               # keywords, category, skills[]  ← skills[] required
        ├── README.md
        ├── CHANGELOG.md
        ├── .gitignore
        ├── skills/<skill>/SKILL.md     # plus flat SCREAMING-CASE.md siblings
        ├── agents/<agent>.md           # auto-discovered
        ├── commands/<command>.md       # auto-discovered
        ├── hooks/hooks.json            # optional
        ├── scripts/                    # optional: generators, verification
        └── .<name>-state.json          # optional: upstream drift tracking
```

`skills[]` must appear in **both** `plugin.json` and `marketplace.json`, and be identical in each.
It defines the shipped set, so work in progress can sit in the repository without entering anyone's
budget. **A path pointing at a directory without a `SKILL.md` breaks plugin loading** —
`scripts/register-plugin.py` refuses to write in that case rather than warning.

## Naming

| Artefact | Pattern | Example |
|---|---|---|
| Plugin | `<product>-<topic>` | `shopware-data`, `octo-api` |
| Skill | `<prefix>-<domain>` | `sw-entity`, `octo-products` |
| Agent | `<product>-<role>` | `shopware-dal-expert`, `octo-integrator` |
| Command | `/<prefix>-<verb-object>` | `/sw-entity`, `/octo-lookup` |
| Reference file | `SCREAMING-CASE.md` | `PRODUCT-SCHEMA.md`, `CRITERIA.md` |
| Introspection catalogue | `.<product>-catalog/<topic>.md` | `.shopware-catalog/entities.md` |

All kebab-case. **No agency, client or project abbreviations in identifiers** — this repository is
public.

**A skill name is itself a trigger anchor.** `octo-products` carries the brand word and is therefore
matchable; a bare `products` would not be.

## Token economy

The binding constraint is the **skill listing budget**: `len(description) + 109` per skill against
**8,000 characters** (1 % of a 200k context window). On overflow the *least-used* skills lose their
description and stop activating on their own. Derivation, sources and the measured state:
[`CLAUDE.md`](./CLAUDE.md).

1. **Description ≤ 200 characters**, single line, English, third person, pattern
   `<Statement>. Use when <anchor>, <anchor>.` No `when_to_use` (it counts against the same cap).
2. **≤ 12 model-visible skills per plugin.** More topics means grouping by domain and pushing depth
   into reference files. A pure lookup skill may carry `disable-model-invocation: true`: it then
   costs **nothing** and stays reachable through a router skill or `/<plugin>:<skill>`.
3. **Trigger anchors must be unambiguous.** Generic vocabulary (`product`, `booking`, `pricing`,
   `availability`, `cart`, `component`, `test`, `theme`) never belongs in the `Use when` clause — it
   collides across plugins. Bind it to a brand word: `OCTO or Ventrata products`.
4. **Skills carry no `model:` field.** Economy comes from **progressive disclosure**:
   - `SKILL.md` ≤ **120 lines** (≤ 40 for a domain map): purpose, core model, reference map.
   - Depth in flat siblings, **one** level deep. Files nested deeper are only partially read
     (`head -100`), so everything past line 100 is invisible. Hence **no** `references/deep/`.
   - Table of contents at the top of any file over 100 lines with more than two sections.
5. **Load-bearing content first.** After compaction only the first 5,000 tokens of each skill are
   re-attached, sharing a 25,000-token budget.
6. **Commands and agents pick the cheapest adequate model:**
   - `haiku` — mechanical and template-driven: scaffolders, mappers, lookups.
   - `sonnet` — focused specialists and commands that judge.
   - `opus` — orchestrators, migrators and knowledge sync only.
7. **Embed knowledge, do not link to it.** Reference files hold distilled knowledge, never pointers
   to upstream paths absent from the user's project.
8. **Reach another skill by tool call**, not by path: `Call the Skill tool with "octo-protocol".`
   A relative link into another skill's directory invokes nothing.

## Frontmatter templates

### Skill — `skills/<name>/SKILL.md`

Only `name` and `description`. No `triggers:` (no such field), no `model:`, no `when_to_use:`, no
`context: fork` on a reference skill (guidelines without a task return nothing), no `paths:` on a
prose-triggered knowledge skill (a filter, not an amplifier).

```markdown
---
name: octo-products
description: OCTO/Ventrata product catalogue: GET /products, Product, Option and Unit schemas, all fields and enums. Use when the request names OCTO or Ventrata products, options or units.
---

# OCTO Products

<one to three sentences of purpose; load-bearing content first>

## <Core model / endpoints / enums>

- **fieldName** (string, required): meaning.

## Reference map

- **`[PRODUCT-SCHEMA.md](PRODUCT-SCHEMA.md)`**: all 23 base fields, enums, sub-schemas.
- **`[CAPABILITY-EXTENSIONS.md](CAPABILITY-EXTENSIONS.md)`**: the 16 capability-gated fields.

## Related

Call the Skill tool with "octo-protocol" for headers and error codes.

## Source

Distilled from the [Ventrata OCTO API specification](https://docs.ventrata.com) —
`openapi.yaml` 3.0.3, sha256 `d7bec97a…`, retrieved 2026-08-20.
Reference files in this directory are generated; see `scripts/extract_spec.py`.
```

**`## Source` is mandatory** in every skill: upstream URL, file or version or hash, and retrieval
date. A reader must be able to check any claim against the original; a maintainer must know what a
refresh has to re-read. Generated files additionally carry a generator stamp on line 1. Details:
[`CLAUDE.md`](./CLAUDE.md) → "Cite the source".

Count characters before committing: `python3 -c "print(len('…'))"`.

### Agent — `agents/<name>.md`

```markdown
---
name: octo-integrator
description: >
  <role + when to delegate>. Use proactively when <anchor>, <anchor>.
tools: Read, Grep, Glob, Bash
model: sonnet
skills: octo-protocol, octo-products
---

# <Title>
<instructions, guardrails, approach>
```

- **`skills:` injects full content**, not just the description. Preload only the two or three the
  agent always needs; reach the rest through the Skill tool.
- **Least privilege on `tools`.** A lookup agent needs no `Edit`/`Write` — that also protects a
  source-of-truth plugin from accidental edits.
- **Omit `hooks`, `mcpServers`, `permissionMode`** — ignored for plugin subagents.
- **Agent teams are not shippable** (experimental, generated at runtime, and they ignore `skills:`).

### Command — `commands/<name>.md`

```markdown
---
name: octo-lookup
description: Look up an OCTO endpoint, schema, field or capability and print parameters, required flags and a curl example.
argument-hint: <endpoint|schema|field|capability> [--vendor ventrata|gocity]
allowed-tools: Read, Glob, Grep
model: haiku
---

<instructions; close with "Invent nothing.">
```

### Hook — `hooks/hooks.json`

Remind after a file change (`PostToolUse`, with a matcher):

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          { "type": "command", "command": ["python3", "${CLAUDE_PLUGIN_ROOT}/hooks/<name>-reminder.py"] }
        ]
      }
    ]
  }
}
```

Inject context on a prompt anchor (`UserPromptSubmit`, **no** matcher):

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          { "type": "command",
            "command": ["python3", "${CLAUDE_PLUGIN_ROOT}/hooks/<name>-anchor.py"],
            "timeout": 5 }
        ]
      }
    ]
  }
}
```

- **`UserPromptSubmit` supports no `matcher`** — one would be silently ignored. The regex belongs in
  the script, with an early return before any other work.
- **`additionalContext` must sit inside `hookSpecificOutput`** — at the top level it is silently
  dropped. The most common mistake with this event.
- **Exec form** (array) whenever a path placeholder is involved.
- **`timeout: 5`** and exit 0 on every path: the hook runs synchronously before every prompt.
- A hook **cannot** force a skill to load — no such mechanism exists. It only raises the odds.

## Reference skill versus introspection

- **Reference skill** — "how do I build X" or "what does the specification say": static, distilled
  from the canonical source.
- **Introspection** — "what exists in THIS project": a `haiku` mapper agent plus a command scans the
  user's project and writes a cached Markdown catalogue to `.<product>-catalog/`. Other skills and
  agents read the catalogue.

## Source of truth

When a plugin claims authority over an API or a standard, facts are **generated, not recalled**:

- **Generate from the machine-readable source** (OpenAPI, JSON schema, a typed export) with a script
  in `scripts/`. No model sits between specification and reference file.
- **Ship a field index and a verify script** that checks both directions: every specified field is
  documented, and every documented field exists in the specification. The second direction catches
  invention.
- **Track drift in a state file** (`.<name>-state.json`) with source URL, content hash and entity
  counts, plus a `--check` / `--apply` command. No network call at session start.
- **Stamp generated files** with the source hash and a do-not-edit note, so later hand edits show.
- **Add prose only after a green verify**, then verify again.
- **Cite the source in every file** — `## Source` in the skill, a generator stamp in generated files,
  the specific page (not the site root) in hand-written references, and the canonical source plus
  rights holder in the plugin README.

## Language and publication

This repository is public and international.

- **English for every file, without exception**: skills and their frontmatter, reference files,
  agents, commands, hooks, scripts, READMEs, changelogs, JSON descriptions, comments inside code,
  and the repository-level documents. Where a knowledge source is German — `docs.shopware.com/de`,
  the Contao manual — the distilled text is still written in English; only the source URL stays.
  `CLAUDE.md` states the full rule, including the two plugins where a German user interface is the
  subject rather than the medium, and the greps that prove a plugin is clean.
- **No personal, client or agency data**: no private e-mail addresses, no internal project names, no
  agency prefixes. `author` carries a GitHub handle.
- **`license` must match reality.** `proprietary` in a public repository is a contradiction. Where
  knowledge is distilled from third-party documentation, name the source in the README and in the
  generated files.

## Verify before shipping

```bash
python3 scripts/measure-skill-budget.py .                              # listing cost per plugin
find plugins/<name>/skills -mindepth 3 -name '*.md'                    # empty: references one level deep
grep -rn 'triggers:\|when_to_use:\|model:' plugins/<name>/skills/*/SKILL.md   # empty
awk 'FNR==1{if(p&&n>120)print p,n; p=FILENAME; n=0} {n++} END{if(n>120)print p,n}' \
  plugins/<name>/skills/*/SKILL.md                                     # no SKILL.md over 120 lines
python3 -c "import json,sys;[json.load(open(f)) for f in sys.argv[1:]]" \
  .claude-plugin/marketplace.json plugins/<name>/.claude-plugin/plugin.json   # valid JSON
```

In a session: `/doctor` estimates the listing cost and its biggest contributors, `/context` shows the
Skills row after the budget is applied, `--debug` logs the overflow warning.

Test triggering **in both directions**: do the intended prompts activate the skill, and do prompts
from a neighbouring domain leave it alone?

## Stack anchors

### Shopware plugins (Shopware 6.7)

PHP 8.2+, Symfony 7, Doctrine DBAL 4 (no ORM — DAL plus `Criteria`), Vue 3 with Pinia and Vite in the
administration (`mt-*` components), Twig with Bootstrap 5 in the Storefront, MySQL/MariaDB,
OpenSearch/Elasticsearch, PHPUnit/PHPStan/Jest/Playwright. Extensibility: **events before
decorators**. Three APIs: `/api/` (Admin), `/store-api/` (Store), `/api/_action/sync` (Sync).
Lint: `composer ecs[-fix]`, `composer phpstan`, `composer eslint:admin|storefront[:fix]`,
`composer stylelint`, `composer ludtwig:storefront`.

### octo-api

OCTO (Open Connection for Tourism), an open standard by OCTO Standards NP Inc. Base URL of the
Ventrata implementation: `https://api.ventrata.com/octo`. Auth: Bearer. **`Octo-Capabilities` is a
required header** — omitting it returns HTTP 400; an empty value is allowed. Core flow: products →
availability → reserve/confirm/cancel. Capabilities are additive and requested comma-separated in the
header.
