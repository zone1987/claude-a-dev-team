---
name: zcf-anchor-design
description: Designs trigger anchors that fire on one domain only, checked against every installed plugin.
disable-model-invocation: true
---

# Designing an anchor

An **anchor** is a word in a description's `Use when` clause that identifies **this** domain and no
other. Get it wrong in either direction and the cost is a full skill load: too broad and the skill
fires while someone works in a neighbouring domain, too narrow and it never fires at all.

This skill is user-invoked on purpose. A skill about anchors that triggered on the word "anchor"
would collide with every conversation about skill authoring, which is the mistake it exists to
prevent.

## What qualifies

| Kind | Example | Why it holds |
|---|---|---|
| Brand or protocol | `OCTO`, `Ventrata`, `Shopware`, `Contao` | belongs to one product |
| Exact filename | `SKILL.md`, `openapi.yaml`, `hooks.json`, `composer.json` | names a file, not a topic |
| Path shape | `agents/*.md`, `src/Core/`, `.claude-plugin/` | matches what is being touched |
| Exact identifier | `PostToolUse`, `availabilityType`, `Octo-Capabilities`, `mt-button` | one API's vocabulary |
| CLI binary | `shopware-cli`, `gh`, `wrangler` | one tool |

## What never qualifies alone

Generic vocabulary appears in daily work across most plugins here: product, booking, pricing,
availability, cart, unit, option, component, test, build, theme, page, field, file, and every word for
a Claude Code artefact (skill, agent, command, hook, plugin).

**Bind it, or leave it in the statement.** The leading statement describes scope and matches nothing;
only the `Use when` clause triggers. So `OCTO or Ventrata products` is right and `products` is not,
and the fix is a bound noun rather than a deleted one. `ANCHOR-01`

## The inversion for meta-domains

A plugin whose subject is Claude Code itself cannot anchor on its activity words: every other plugin's
users discuss skills, agents and hooks constantly. Anchor on the **artefact being edited** instead:

- `SKILL.md`, `plugin.json`, `hooks.json`, `agents/*.md`, `commands/*.md`
- exact event names: `UserPromptSubmit`, `PostToolUse`, `PreToolUse`

"Write me a skill for X" then does not fire, while editing `plugins/foo/skills/bar/SKILL.md` does.
That is the intended asymmetry: the file is unambiguous, the topic is not.

## Check before shipping

```bash
python3 scripts/anchor_inventory.py            # regenerates ANCHOR-INVENTORY.md
grep -in "<candidate>" ANCHOR-INVENTORY.md     # who else claims it
```

The inventory collects every `Use when` clause from every installed plugin, so a collision is visible
rather than discovered in a session six weeks later. `ANCHOR-02`

## Test both directions

An anchor is finished when both hold:

- the prompts you intend **do** reach the skill, and
- prompts from a neighbouring domain **leave it alone**.

The second is where the cost hides, and it is the half people skip. Write three prompts of each kind
before shipping, and run them.

## Reference map

- **[ANCHOR-INVENTORY.md](ANCHOR-INVENTORY.md)**: every `Use when` clause across installed plugins,
  generated. The file to grep a candidate against.

## Related

Call the Skill tool with "zcf-skill-authoring" to write the description the anchor lives in.

## Source

Anchor rules and their grounding live in [`rules.json`](../../rules.json) v1.0.0 (`ANCHOR-01`,
`ANCHOR-02`), which cite
[writing effective descriptions](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#writing-effective-descriptions),
retrieved 2026-08-21.
