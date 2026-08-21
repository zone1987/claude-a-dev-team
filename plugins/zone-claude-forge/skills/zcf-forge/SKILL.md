---
name: zcf-forge
description: Routes to the right authoring skill, command or agent in this plugin.
disable-model-invocation: true
---

# The forge

You do not remember every skill in here, so ask. This is a router: it **points**, and it can call the
model-invoked skills. It cannot invoke the user-invoked ones, because nothing but a human can reach
those, so those appear as commands for you to type.

## Building something new

| You are writing | Reach for |
|---|---|
| a `SKILL.md`, a description, or skill frontmatter | Skill tool with **"zcf-skill-authoring"** |
| an agent, a slash command, or a hook | Skill tool with **"zcf-component-authoring"** |
| reference files from upstream docs, an OpenAPI spec, or a repository | Skill tool with **"zcf-source-distillation"** |
| a whole new plugin from nothing | `/zcf-new-skill <plugin> <skill>`, then the three above |

Start with the **description**, always. It is the hardest part, it constrains everything else, and it
is the only part of a skill that costs on every turn.

## Checking something that exists

| You want to know | Run |
|---|---|
| does this plugin break any rule | `/zcf-validate <plugin> --strict` |
| what does it violate, lack, and no longer need | `/zcf-audit <plugin>` |
| will a realistic session overflow the listing budget | `python3 scripts/validate_plugin.py --working-set <a> <b> <c>` |
| which skills load without being listed | `python3 scripts/validate_plugin.py --unlisted` |
| does the catalogue still match the documentation | `python3 scripts/verify_sources.py --check` |

The working-set run is the one that matters and the one people skip: a plugin at 30 % of the budget is
fine alone and ruinous beside three others.

## Deciding something

| The question | Where it is answered |
|---|---|
| will this anchor collide with another plugin | `/zone-claude-forge:zcf-anchor-design` |
| model-invoked or user-invoked | `INVOKE-01` in [`RULES.md`](../../RULES.md), and `FRONTMATTER.md` in `zcf-skill-authoring` |
| does this deserve an agent, a command, or a hook | `COMP-01` to `COMP-05`, and the table in `zcf-component-authoring` |
| does this plugin need an orchestrator | `AGENT-04`. Usually not: a router costs nothing, an orchestrator costs a context window per call |
| which model and effort | `MODEL-SELECTION.md` in `zcf-component-authoring` |
| what exactly are the rules | [`RULES.md`](../../RULES.md), 75 of them, each with its grounding |

## The order that avoids rework

1. **Name the anchors**, before writing anything. `/zone-claude-forge:zcf-anchor-design`
2. **Choose invocation.** Model-invoked spends its description permanently; user-invoked spends only
   your memory, which is what this router is for.
3. **Write the description and count it.** `python3 -c "print(len('…'))"`
4. **Draft the body as a map**, depth in flat siblings.
5. **Run the gate** after each step, not at the end: `/zcf-validate <plugin> --strict`

## Two things worth knowing up front

**The gate blocks.** A `PreToolUse` hook denies a write into `plugins/` that breaks a blocking rule,
naming the rule and the measured value. `ZCF_BYPASS=1` turns it into a warning, for the one honest
case: repairing a plugin that is already red, where the first fixing write would itself be refused.

**Nothing can force a skill to load.** No hook, no description, no agent instruction. The gate
enforces the rules; this router and the prompt nudge make the forge the obvious route. Anything
stronger would be a promise the platform cannot keep.

## Source

The routes above are the components of this plugin, read 2026-08-21. Rules and their grounding live in
[`rules.json`](../../rules.json) v1.0.0, rendered as [`RULES.md`](../../RULES.md); every documented
rule cites [code.claude.com/docs](https://code.claude.com/docs/en/skills) or a sibling page.
