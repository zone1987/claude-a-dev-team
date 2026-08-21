# zone-claude-forge

The authoring instrument for this marketplace. It writes skills, agents, commands and hooks that
comply by construction, distils upstream sources into cited reference files with a coverage proof,
and audits plugins that already exist.

**3 model-visible skills, 893 characters, 11.2 % of the skill listing budget.**

## Why it exists

The marketplace's rules were prose. Nothing checked description length, the body ceiling, the
mandatory `## Source` section, reference depth, manifest parity or the language rule in one run with
an exit code, so every new plugin re-derived them by hand. Two of those rules turned out to be
factually wrong against the official documentation.

This plugin makes the rules executable: 75 of them in [`rules.json`](rules.json), each carrying what
it rests on, rendered for reading as [`RULES.md`](RULES.md), and applied by a gate that refuses a
non-compliant write.

## The rules

Every rule carries a **ground class**, and a rule with no ground does not enter the catalogue:

| Class | Carries | Count |
|---|---|---|
| `documented` | a URL, a verbatim quotation and a retrieval date | 35 |
| `technique` | the claimed effect plus its measurement | 29 |
| `convention` | its purpose, marked explicitly as **not** a platform requirement | 11 |

And an **enforcement class**: 52 are `blocking` (machine-decidable, the gate fails the build) and 23
are `review` (judgement-bound, each with a tell, applied by `claude-component-reviewer`). Claiming a
script enforces the second class would be a promise the plugin cannot keep.

`scripts/verify_sources.py` checks the citations in both directions: every rule is grounded, and
every quotation appears verbatim on the page it cites. The reverse direction is what catches a
plausible rule nobody can trace.

## Components

**Skills** — three the model can reach, three only you can:

| Skill | Invocation | For |
|---|---|---|
| `zcf-skill-authoring` | model | writing a `SKILL.md`, a description, frontmatter |
| `zcf-component-authoring` | model | agents, commands, `hooks.json` |
| `zcf-source-distillation` | model | upstream docs, OpenAPI, repositories into reference files |
| `zcf-forge` | user | the router: which skill, command or agent fits |
| `zcf-plugin-audit` | user | violations, missing components, redundant ones |
| `zcf-anchor-design` | user | anchors that fire on one domain only |

A user-invoked skill costs only its name in the listing, and nothing but a human can reach it. That
is the largest budget lever available, and `zcf-forge` is what keeps the three cheap ones findable.

**Commands**: `/zcf-new-skill`, `/zcf-validate`, `/zcf-audit`, `/zcf-distill`.

**Agents**: `claude-source-distiller` (`opus`, its own context window for bulk extraction) and
`claude-component-reviewer` (`sonnet`, read-only, so a review costs one summary and cannot rewrite
its own findings).

**Hooks**, four events in the order they fire:

| Event | Does |
|---|---|
| `SessionStart` | names the forge once per session, inside this marketplace only (821 characters) |
| `UserPromptSubmit` | nudges when a prompt names a plugin file or an event |
| `PreToolUse` | **denies** a write breaking a blocking rule, naming the skill that carries the fix |
| `PostToolUse` | reports what only the whole plugin can decide: budget sums, manifest parity, links |

## Enforcement, and its limit

**No mechanism forces a skill to load.** The documentation is explicit: a hook cannot, and
`use proactively` on an agent is a nudge. So enforcement inverts the goal and blocks the
**write** instead, which `PreToolUse` can do deterministically.

The gate denies with a structured reason naming the rule, the measured value, **and the skill that
carries the fix**:

```
[SRC-01] no '## Source' section naming where the knowledge came from. Call the Skill tool with
"zcf-skill-authoring" for how to write this file, then write it again. Rule wording and
grounding: plugins/zone-claude-forge/RULES.md (look up the rule id). Check the whole plugin with
/zcf-validate <plugin> --strict. To repair a plugin that is already failing, set ZCF_BYPASS=1
for that write.
```

A rule id says what is wrong; the skill says how to write the file correctly, which is the whole
reason the plugin exists.

**Three layers, and only one is a guarantee.** `SessionStart` and `UserPromptSubmit` raise the odds
that the right skill loads. `PreToolUse` is the guarantee, and it guarantees the **rules**, not the
route: a write that breaks nothing passes whether or not the forge was consulted.

It is registered twice: in `hooks/hooks.json` for anyone installing the plugin, and in the repo's
`.claude/settings.json` so it holds even when the plugin is disabled via `/plugin`.

Speed is correctness here rather than tidiness: a timed-out `PreToolUse` hook does **not** block, so
the path test runs first and only the file being written is checked. Measured at ~17 ms per call.

## Usage

```bash
python3 scripts/validate_plugin.py --plugin <name> --strict     # the gate
python3 scripts/validate_plugin.py --working-set <a> <b> <c>    # what actually overflows
python3 scripts/validate_plugin.py --unlisted                   # skills that load unlisted
python3 scripts/validate_plugin.py --rules                      # the catalogue and its classes
python3 scripts/verify_sources.py --check                       # every rule grounded
python3 scripts/render_rules.py --check                         # RULES.md matches rules.json
python3 scripts/anchor_inventory.py                             # regenerate the anchor inventory
python3 scripts/audit_coverage.py --plugin <name> --spec <file>  # coverage, both directions
```

## Source

Rules are distilled from the Claude Code documentation, retrieved 2026-08-21:
[skills](https://code.claude.com/docs/en/skills),
[skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices),
[subagents](https://code.claude.com/docs/en/sub-agents),
[hooks](https://code.claude.com/docs/en/hooks) and
[plugins reference](https://code.claude.com/docs/en/plugins-reference). That documentation is the
source of truth and outranks this plugin.

Writing levers (context pointers, the information hierarchy, completion criteria, leading words, the
no-op test) are distilled from [mattpocock/skills](https://github.com/mattpocock/skills)
`writing-for-agents`, MIT licensed, retrieved 2026-08-21. Distillation and coverage-proof method
generalised from `plugins/octo-api/scripts/` in this marketplace.

The 109-character per-entry listing overhead is measured rather than documented:
[anthropics/claude-code#64606](https://github.com/anthropics/claude-code/issues/64606).
