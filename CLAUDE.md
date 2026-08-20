# Plugin Authoring Rules

Binding rules for every plugin, skill, agent, command and hook in this marketplace.
`CONVENTIONS.md` covers naming and layout; this file covers efficiency, and it wins on conflict.

Read this before adding or editing any skill.

## The skill listing budget is the binding constraint

Claude Code loads a listing of skill names and descriptions into the system prompt so it knows
what is available. That listing has a hard character budget:

> "The listing always contains every skill name, but if you have many skills, Claude Code shortens
> descriptions to fit the listing's character budget, which can strip the keywords Claude needs to
> match your request. The budget scales at 1% of the model's context window."
> — [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)

Three consequences that decide how we write skills:

- **Cost per skill** is `len(description) + len(when_to_use) + 109`. The 109 is measured overhead
  (XML tags, name, location) — see [anthropics/claude-code#64606](https://github.com/anthropics/claude-code/issues/64606).
- **Budget** is 1% of the context window: **8,000 characters at 200k**.
- **On overflow, Claude Code drops descriptions starting with the skills invoked least.** A skill
  without a description is still listed by name, but it never auto-activates again. Rarely used
  skills are the first to go silent — which is exactly backwards from what an author wants.

Two further limits, both documented:

> "each entry's combined text is capped at 1,536 characters regardless of budget. The cap is
> configurable with `skillListingMaxDescChars`."
> — [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills#skill-listing-budget)

The frontmatter reference says the same from the other side: the combined `description` and
`when_to_use` text "is truncated at 1,536 characters in the skill listing to reduce context usage".
Treat 1,536 as the ceiling to design against, not as a fixed property of the platform — a user who
raises `skillListingMaxDescChars` is not who we are writing for.

> "Plugin skills are not affected by `skillOverrides`. Manage those through `/plugin` instead."
> — [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills#override-skill-visibility-from-settings)

That is the load-bearing one. `skillOverrides` is how a user reclaims budget from a skill they
rarely need — setting it to `"name-only"` keeps the name and drops the description. It does not
reach plugin skills. A user who installs from this marketplace therefore cannot trim our
descriptions from their settings; their only lever is enabling or disabling the whole plugin via
`/plugin`. Staying inside the budget is the author's job, not the user's.

### Where this repository stands

Measured with `scripts/measure-skill-budget.py`:

| plugin | skills | chars | avg desc | % of budget |
|---|---:|---:|---:|---:|
| shopware-merchant | 16 | 4,569 | 177 | 57% |
| octo-api | 8 | 2,392 | 190 | 30% |
| shadcn-vue | 8 | 2,282 | 176 | 29% |
| shadcn | 8 | 2,265 | 174 | 28% |
| contao | 8 | 2,257 | 173 | 28% |
| playwright | 5 | 1,463 | 184 | 18% |
| … 20 more | 64 | 18,347 | 178 | 229% |

Read those shares against a working set, never as a sum: a session enables three to five
plugins, and any such set lands inside the limit — `shopware-core` plus `shopware-data` plus
`shopware-storefront` is 43 %. Enabling all 26 is not a supported configuration.

A new plugin joining this repository holds that line. The limits below are how.

`octo-api` is the reference implementation of these rules: 8 skills, 2,392 characters, 30 % of the
budget, with all 65 operations and 254 capability fields covered and machine-verified.

## The standard every plugin meets

Two obligations, and neither may be traded for the other.

**Complete.** A plugin must carry everything the thing it documents can do. Every endpoint,
every field, every option, every possible value, every default, every error, every caveat the
upstream documentation states — extracted from that documentation, not recalled. If a page
exists upstream and the plugin claims that subject, the page's content is in the plugin. No
detail is too small: an enum value without its meaning, a parameter without its type, a field
without its optionality are all gaps. When the upstream itself is silent, say so explicitly
rather than leaving a blank that reads as absence.

**Efficient.** The knowledge is organised so it costs almost nothing until it is needed:
`mattpocock/skills` is the benchmark. Few skills, sharp descriptions, short maps, depth behind
one-level references. Every limit below is binding at all times, not on first authoring.

These pull in opposite directions only if you think in files. They do not conflict in fact:
descriptions cost budget, reference files do not. `octo-api` documents 139 schemas and 65
operations — 1,800 rendered field entries across 7,736 lines — and spends 2,392 characters,
30 % of the budget, because the depth sits in references that load on demand.

Reproduce those numbers rather than trusting them:

```bash
python3 scripts/measure-skill-budget.py . | grep octo-api             # 8 skills, 2,392 chars
find plugins/octo-api/skills -name '*.md' | xargs wc -l | tail -1     # 7,736 lines
grep -rhoE '^- \*\*[A-Za-z_][A-Za-z0-9_]*\*\* \(' plugins/octo-api/skills | wc -l   # 1,800 fields
python3 -c "import json; print(json.load(open('plugins/octo-api/.spec-state.json'))['counts'])"
```

So the rule for restructuring is absolute: **bundling may never drop content.** Move a body
into a reference file, rename it, split it — but verify afterwards that every source body still
appears in the result. `scripts/verify-bundle.py` exists for exactly that check, and a
restructuring is not finished until it reports zero losses.

## Hard limits

- **`description` ≤ 200 characters.** Single line, English, third person.
- **≤ 12 model-visible skills per plugin.** Beyond that, bundle by domain and push detail into
  reference files, or make the detail skills user-invoked only.
- **No `when_to_use`.** It is appended to `description` and counts against the same 1,536-character
  cap, so it buys nothing and doubles the maintenance surface. Put the triggers in `description`.
- **`skills[]` in `plugin.json` is mandatory.** It defines the shipped set, so work in progress can
  live in the repo without entering anyone's budget.
- **`SKILL.md` ≤ 120 lines, ≤ 40 for a domain map.** The documented ceiling is higher — "Keep
  SKILL.md body under 500 lines for optimal performance"
  ([best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#token-budgets))
  — and we stay well inside it, because a loaded skill is a recurring cost on every turn. A map that
  grows past 40 lines is listing files rather than orienting a reader: drop the per-file gist and
  group companions onto their topic's line.
- **Every reference file over 100 lines carries a table of contents** — unless it has fewer
  than three `##` sections, where a two-entry list is noise rather than navigation.
  `scripts/add-toc.py` applies exactly that rule.
- **Every skill names its source.** A `## Source` section at the end of `SKILL.md` states where
  the knowledge comes from — the upstream URL, the specification file, the version or commit it was
  distilled from, and the date. A reader must be able to check any claim against the original, and
  a maintainer must be able to tell what a refresh has to re-read. See [Cite the source](#cite-the-source).

## Description pattern

```
<Statement>. Use when <anchor>, <anchor>, or <anchor>.
```

Put the key use case first — the entry is truncated from the end. Write in third person:
the text is injected into the system prompt, and first or second person breaks discovery.

```yaml
# good — 198 chars, anchors unambiguous
description: OCTO/Ventrata wire protocol: auth, the mandatory Octo-Capabilities header, error codes, localization. Use when the request names OCTO, Ventrata, Octo-Capabilities, Octo-Env, or an octo/* capability.

# bad — generic anchors collide with every other plugin
description: Handles products, options and units. Use when the user mentions products or availability.
```

### Anchors must be unambiguous

An anchor is a word that identifies **this** domain and no other. Brand names, protocol
identifiers, header names, file extensions, CLI binaries and API paths qualify.

**Generic vocabulary never belongs in the `Use when` clause.** Words like `product`, `booking`,
`pricing`, `availability`, `cart`, `unit`, `option`, `component`, `test`, `build` or `theme` appear
in daily work across most plugins here. An anchor on `product` fires the OCTO skill while someone
edits a Shopware entity, and it fires the Shopware skill while someone reads OCTO docs. Both are
wrong, and both cost a full skill load.

Bind generic nouns to a brand word instead: `OCTO or Ventrata products`, not `products`. Generic
nouns are fine in the leading statement, where they describe scope rather than trigger matching.

## Cite the source

Knowledge without a citation cannot be maintained: nobody can tell whether it is still true, and
nobody knows what to re-read when the upstream changes. Every skill therefore carries its origin.

**In `SKILL.md`**, a closing section:

```markdown
## Source

Distilled from the [Ventrata OCTO API specification](https://docs.ventrata.com) —
`openapi.yaml` 3.0.3, sha256 `d7bec97a…`, retrieved 2026-08-20.
Reference files in this directory are generated; see `scripts/extract_spec.py`.
```

**In a generated file**, a stamp on line 1 naming the generator and the source hash, so later hand
edits are visible:

```markdown
<!-- generated by scripts/extract_spec.py from openapi.yaml sha256:d7bec97a — do not edit above the prose marker -->
```

**In a hand-written reference file**, the specific page rather than the site root: cite
`docs.ventrata.com/capabilities/pricing`, not `docs.ventrata.com`. A precise citation is checkable;
a vague one is decoration.

**In the plugin `README.md`**, the canonical source for the whole plugin plus the rights holder of
the original documentation. This repository is public: crediting the source is both an accuracy
measure and a courtesy.

What a citation must let a reader do:

- **Check a claim** — follow the link and find the same statement.
- **Judge the age** — a version, hash or date, not just a URL.
- **Plan a refresh** — know which upstream file or page feeds which reference file.

Never cite a path that only exists on the author's machine, and never cite an upstream path that the
user's project does not contain. Embed the knowledge, cite the origin.

## Progressive disclosure

`SKILL.md` is a map, not the territory. Detail lives in sibling reference files:

```
skills/octo-products/
├── SKILL.md                    # ≤ 120 lines: what this is, the model, a reference map
├── ENDPOINTS.md
├── PRODUCT-SCHEMA.md
└── CAPABILITY-EXTENSIONS.md
```

- **One level deep, flat siblings, `SCREAMING-CASE.md`.** This is the documented mechanism, not a
  preference:

  > "Claude may partially read files when they're referenced from other referenced files. When
  > encountering nested references, Claude might use commands like `head -100` to preview content
  > rather than reading entire files, resulting in incomplete information."
  >
  > "**Keep references one level deep from SKILL.md**. All reference files should link directly
  > from SKILL.md to ensure Claude reads complete files when needed."
  > — [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#avoid-deeply-nested-references)

  So a `references/deep/x.md` layout silently loses most of its own content: anything past line 100
  of a nested file is effectively invisible.
- **Link every reference from `SKILL.md`** with a note on what it contains, so Claude can decide
  whether to open it: `- **[PRODUCT-SCHEMA.md](PRODUCT-SCHEMA.md)**: all 23 base fields and enums.`
- **Table of contents at the top of any file over 100 lines.** Same source, same reason: "For
  reference files longer than 100 lines, include a table of contents at the top. This ensures
  Claude can see the full scope of available information even when previewing with partial reads."
  The 100 is not arbitrary — it is the `head -100` preview boundary above.
- **Reach other skills by tool call, not by path**: `Call the Skill tool with "octo-protocol".`
  A relative link into another skill's directory is not an invocation and loads nothing.

## Write for compaction

> "Claude Code re-attaches the most recent invocation of each skill after the summary, keeping the
> first 5,000 tokens of each. Re-attached skills share a combined budget of 25,000 tokens."
> — [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)

Put load-bearing content first. Anything past the first 5,000 tokens of a skill disappears at the
first compaction and does not come back.

And because "once a skill loads, its content stays in context across turns, so every line is a
recurring token cost" ([same source](https://code.claude.com/docs/en/skills)): state what to do, not how you arrived at it. When a sentence adds nothing
the model would not already do, delete the whole sentence rather than trimming its words.

## Body style

Imperative, second person, addressed to the agent. Force comes from precise words, not volume:
`never`, `only`, `first`. Reserve capitals for one or two genuine gates per skill.

- **Bullets carry a bold lead term**: `- **seam**: the public boundary you test at.`
- **Define terms inline at first use**, then reuse the term as a token without re-explaining it.
- **State the positive.** Prohibitions drag the forbidden behaviour into context and make it more
  available, not less. "Verify each field against the specification" beats "do not invent fields".
- **Anti-patterns get a tell** — how to recognise the mistake, not just its name.

## Never

- **`context: fork` on a reference skill.** Documented to fail: "If your skill contains guidelines
  like 'use these API conventions' without a task, the subagent receives the guidelines but no
  actionable prompt, and returns without meaningful output."
  ([skills](https://code.claude.com/docs/en/skills#run-a-skill-in-a-subagent))
- **A `triggers:` field.** It does not exist — it is absent from the frontmatter reference, so it is
  parsed as unknown and silently does nothing. Triggers belong in `description`.
  ([frontmatter reference](https://code.claude.com/docs/en/skills#skill-frontmatter))
- **`model:` in a skill.** Not a skill frontmatter field; model selection belongs to agents and
  commands. Same reference.
- **`hooks`, `mcpServers` or `permissionMode` in a plugin agent.** Writing them creates false
  confidence:

  > "For security reasons, plugin subagents don't support the `hooks`, `mcpServers`, or
  > `permissionMode` frontmatter fields. These fields are ignored when loading agents from a plugin."
  > — [Subagents](https://code.claude.com/docs/en/sub-agents)

- **`paths:` on a prose-triggered knowledge skill.** It is a filter, not an amplifier: "When set,
  Claude loads the skill automatically **only** when working with files matching the patterns."
  ([skills](https://code.claude.com/docs/en/skills)) A question with no matching file open then
  matches nothing — which is the main case for a knowledge plugin.

## Agents

An agent runs in its own context window, so it is the right place for bulk reference work: the main
conversation pays only for the summary it returns.

- **`skills:` injects full content**, not just descriptions — "The full skill content is injected,
  not only the description." ([Subagents](https://code.claude.com/docs/en/sub-agents)) Preload the
  two or three skills the agent always needs; let it reach the rest through the Skill tool.
- **Least privilege on `tools`.** A lookup agent needs no `Edit`/`Write`. Withholding them also
  protects a source-of-truth plugin from accidental edits.
- **`use proactively` in the description** is the documented way to encourage delegation: "To
  encourage proactive delegation, include phrases like 'use proactively' in your subagent's
  description field." ([Subagents](https://code.claude.com/docs/en/sub-agents)) Note what that
  sentence does not promise — it is a nudge, not a guarantee. `@agent-<plugin>:<name>` is the
  guarantee.
- **A team is not a plugin component.** Teams are experimental and off by default
  ("Agent teams are experimental and disabled by default"), and the config is session-derived state:
  "Claude Code generates both of these automatically at session startup … so don't edit it by hand
  or pre-author it: your changes are overwritten on the next state update."
  ([Agent teams](https://code.claude.com/docs/en/agent-teams#architecture))

  What we *can* ship is the agent definition, which the same page endorses reusing as a teammate —
  with one caveat that shapes how we write ours: "The `skills` and `mcpServers` frontmatter fields
  in a subagent definition are not applied when that definition runs as a teammate."
  So an agent whose usefulness rests on preloaded `skills:` degrades silently in that role. Write
  the agent so its body tells it which skills to call, and treat `skills:` as an optimisation rather
  than the mechanism.

Model choice: `haiku` for mechanical scanning and scaffolding, `sonnet` for specialists that judge,
`opus` only for orchestrators, migrators and knowledge sync.

## Hooks

A hook is the deterministic layer. It cannot force a skill to load — there is no such mechanism —
but it can inject context that makes the right choice obvious.

- **`UserPromptSubmit` has no `matcher`.** The events table lists it under "no matcher support —
  always fires on every occurrence" ([Hooks](https://code.claude.com/docs/en/hooks#matcher-patterns)).
  It fires on every prompt; do the matching in the script and return early.
- **`additionalContext` must sit inside `hookSpecificOutput`.** The documentation is explicit:
  "Return `additionalContext` inside `hookSpecificOutput` alongside the event name"
  ([Hooks](https://code.claude.com/docs/en/hooks#add-context-for-claude)), and the
  `UserPromptSubmit` example nests it under `hookEventName: "UserPromptSubmit"`. At the top level it
  is not picked up. This is the most common mistake with this event.
- **Use exec form** (`"command": ["python3", "${CLAUDE_PLUGIN_ROOT}/hooks/x.py"]`) whenever a path
  placeholder is involved.
- **Set `timeout: 5`.** The `command` default is 600 s, which `UserPromptSubmit` lowers to 30 s
  ([Hooks](https://code.claude.com/docs/en/hooks)) — still far too long for something that runs
  synchronously before every prompt. And a hook that times out has its output discarded entirely:
  "A `UserPromptSubmit` command, HTTP, or MCP tool hook that reaches its timeout is canceled and
  its output, including any `additionalContext`, is discarded." So a slow hook is not a late hook,
  it is no hook. Exit 0 on every path; never block the user's work.

## Source of truth

When a plugin claims to be authoritative for an API or a standard, facts must be generated, not
recalled:

- **Generate from the machine-readable source** (OpenAPI, JSON schema, a typed export) with a
  script. No model in the path between specification and reference file.
- **Ship a field index** and a verify script that checks both directions: every specified field is
  documented, and every documented field exists in the specification. The second direction is what
  catches invention.
- **Track drift in a state file** — source URL, content hash, entity counts — and expose a
  `--check` / `--apply` command. Do not poll on session start.
- **Stamp generated files** with the source hash and a do-not-edit note, so later hand edits are
  visible.
- **Cache what cannot be looked up.** Conventions, rationale and gotchas earn their tokens;
  restating what one fetch would answer only creates a second version that goes stale.
- **Cite the source in every file** — see [Cite the source](#cite-the-source). For a generated
  plugin this is not optional: the citation plus the state file is what lets anyone confirm the
  plugin still matches upstream.

## Every file is written in English

This is absolute and admits no exception. The marketplace is public and international, so the
language of the repository is English — not the language the knowledge was distilled from, and not
the language of the conversation in which a plugin was built.

**Every file in every plugin, without exception:** `SKILL.md` bodies and their frontmatter,
every reference file, agents, commands, hooks, scripts, `README.md`, `CHANGELOG.md`, JSON
descriptions, and the comments inside code blocks and source files. Repository-level files too:
this document, `CONVENTIONS.md`, `README.md`, `marketplace.json`.

- **The source language is irrelevant.** Knowledge distilled from `docs.shopware.com/de`, from a
  German manual, or from a German-language conversation is written up in English. Keep the source
  URL as it is — that is where the knowledge came from — and translate the prose around it.
- **Translating never condenses.** A 200-line German file becomes a ~200-line English file. These
  plugins are complete by design; a translation that summarises destroys the property the plugin
  exists for. Verify by line count, file by file.
- **Technical identifiers are not prose.** Class names, method names, paths, commands, environment
  variables, API field names, URLs and CSS classes stay exactly as they are. Translate the prose
  around them and the comments inside code blocks — never the code.
- **The one exception is German as the subject, not the medium.** Two plugins document a
  German-language user interface (`shopware-merchant` describes the Shopware administration,
  `contao`'s manual domains the German Contao backend). Removing a menu label would make the text
  useless — nobody could find the item being described. Keep the label and gloss it on first use:
  "Click **Speichern** (Save)", "under **Seitenstruktur** (Page Structure)". The surrounding prose
  is still fully English. The same holds for German string literals inside a code example that
  demonstrates German data — an Austrian month-name array, a German translation payload: the data
  stays, the explanation around it is English.

Check a plugin before shipping it:

```bash
# German prose left anywhere in the plugin — must be empty
grep -rlE '\b(der|die|das|und|werden|müssen|wird|für|mit|kann|sich)\b' plugins/<name>
# German written without umlauts is still German — must also be empty
grep -rliE '\b(fuer|ueber|koennen|muessen|vollstaendig|zusaetzlich|groesse)\b' plugins/<name>
```

The second check matters: transliterated German passes the first one. Treat both as blocking.

## Public repository

This marketplace is public and international.

- **No personal, client or agency data** — no private e-mail addresses, no internal project names,
  no agency prefixes in identifiers. Author fields carry a GitHub handle.
- **`license` must match reality.** `proprietary` in a public repository is a contradiction.
  Where knowledge is distilled from third-party documentation, credit the source in the README and
  in the generated files.

## Restructuring an existing plugin

The tooling in `scripts/` does this in a fixed order, and each step is verifiable:

```bash
# 1. back the skills up — every later check compares against this
cp -R plugins/<name>/skills /tmp/backup-<name>

# 2. group: by name prefix, or by an explicit scripts/domain-skills/<name>.map when the
#    skills share no prefix (a component library has none: button and dialog are siblings)
python3 scripts/bundle-skills.py --plugin <name> --plan
python3 scripts/bundle-skills.py --plugin <name> --apply

# 3. remove the source directories, flatten leftover depth, add tables of contents
bash scripts/finish-bundle.sh <name>

# 4. write the domain maps from scripts/domain-skills/<name>.json
python3 scripts/write-domain-skills.py --plugin <name>

# 5. prove nothing was lost, then register
python3 scripts/verify-bundle.py --plugin <name> --backup /tmp/backup-<name>
python3 scripts/register-plugin.py --plugin <name> --version <x.y.z>
```

Step 5 is the gate. `bundle-skills.py` refuses to overwrite a file rather than silently
merging two skills into one name — a collision is a defect to fix in the mapping, never
something to accept.

## Verify before shipping

```bash
python3 scripts/measure-skill-budget.py .        # per-plugin listing cost
find plugins/<name>/skills -mindepth 3 -name '*.md'   # must be empty: references stay one level deep
grep -rn 'triggers:\|when_to_use:\|model:' plugins/<name>/skills/*/SKILL.md   # must be empty
```

In a session: `/doctor` estimates the listing's context cost and its biggest contributors,
`/context` reports the Skills row after the budget is applied, and `--debug` logs the overflow
warning. Confirm both directions of triggering — that the intended prompts activate the skill, and
that neighbouring-domain prompts do not.

`skillListingBudgetFraction`, `SLASH_COMMAND_TOOL_CHAR_BUDGET` and `skillListingMaxDescChars` exist
as escape hatches for users. They are not a substitute for authoring discipline.

## Sources

- [Extend Claude with skills](https://code.claude.com/docs/en/skills) — listing budget, frontmatter, compaction, `paths`, `context: fork`
- [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) — descriptions, 500-line ceiling, one-level references
- [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) — progressive disclosure, ~100 tokens per skill
- [Subagents](https://code.claude.com/docs/en/sub-agents) — full frontmatter, `skills:` injection, ignored plugin fields
- [Agent teams](https://code.claude.com/docs/en/agent-teams) — why they are not shippable
- [Hooks](https://code.claude.com/docs/en/hooks) — events, `additionalContext`, matcher support, timeouts
- [Create plugins](https://code.claude.com/docs/en/plugins) · [Plugins reference](https://code.claude.com/docs/en/plugins-reference) — components, `plugin.json` schema
- [anthropics/claude-code#64606](https://github.com/anthropics/claude-code/issues/64606) — measured per-skill overhead and real-world overflow
- [mattpocock/skills](https://github.com/mattpocock/skills) — the efficiency benchmark this file is calibrated against
