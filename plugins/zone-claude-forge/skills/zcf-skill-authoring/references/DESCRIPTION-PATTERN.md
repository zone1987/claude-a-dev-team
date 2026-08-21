# The description

The description is the skill's **context pointer**: the only part of it Claude sees before deciding
whether to load anything. Its wording, not its target, decides when the skill is reached. A must-have
skill behind a weakly worded description is a variance bug, so sharpen the wording before you
consider moving the material. Rules: `DESC-01` to `DESC-04`, `ANCHOR-01/02`, `BUDGET-03/04`.

## The pattern

```
<Statement>. Use when <anchor>, <anchor>, or <anchor>.
```

- **Statement**: what the skill does, in the third person. The description is injected into the
  system prompt, and first or second person breaks discovery.
- **Use when**: the branches that should trigger it. One trigger per branch; synonyms that rename a
  single branch are one branch written twice.
- **Key use case first.** The entry truncates from the end, so what matters most must survive the
  cut.

Count before committing: `python3 -c "print(len('…'))"`. Limit 200, and leave headroom rather than
landing on it. `DESC-01`, `BUDGET-04`

## Anchors

An anchor identifies **this** domain and no other. Four kinds qualify:

| Kind | Example | Why it holds |
|---|---|---|
| Brand or protocol | `OCTO`, `Ventrata`, `Shopware` | belongs to one product |
| Exact filename | `SKILL.md`, `openapi.yaml`, `hooks.json` | names a file, not a topic |
| Path shape | `agents/*.md`, `commands/*.md` | matches the file being touched, not the subject discussed |
| Exact identifier | `PostToolUse`, `availabilityType`, `Octo-Capabilities` | one API's vocabulary |

**A generic noun is fine in the statement and never alone in the Use when clause.** Words like
product, booking, pricing, availability, cart, component, test, build, theme, skill, agent, hook and
plugin appear in daily work across most plugins here. Bind each to an anchor:

```yaml
# good: the generic noun rides along with a brand word
description: 'OCTO/Ventrata product catalogue: GET /products, Product, Option and Unit schemas. Use when the request names OCTO or Ventrata products, options or units.'

# bad: fires while someone edits an unrelated entity in another plugin
description: Handles products, options and units. Use when the user mentions products or availability.
```

For a plugin whose subject is Claude Code itself, this inverts the usual advice: anchor on the
**artifact being edited** rather than the activity being discussed. "Write me a skill" must not fire;
editing `plugins/foo/skills/bar/SKILL.md` must. `ANCHOR-01`

## Collision

Two skills answering one prompt both load, so the cost doubles and the outcome depends on ordering.
Before shipping an anchor, check it against every `Use when` clause in the marketplace: tell the user
to run `/zone-claude-forge:zcf-anchor-design`, which regenerates `ANCHOR-INVENTORY.md` from all
installed plugins. `ANCHOR-02`

## Test both directions

A description is finished when both hold:

- the prompts you intend **do** reach the skill, and
- prompts from a neighbouring domain **leave it alone**.

The second is the one people skip, and it is where the cost hides: a wrongly fired skill loads its
whole body, which dwarfs the listing entry a tighter description would have saved.

## Source

[Writing effective descriptions](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#writing-effective-descriptions)
and the [frontmatter reference](https://code.claude.com/docs/en/skills#frontmatter-reference),
retrieved 2026-08-21. The context-pointer framing is distilled from
[mattpocock/skills](https://github.com/mattpocock/skills) `writing-for-agents`, retrieved 2026-08-21.
