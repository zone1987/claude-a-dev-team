---
name: zcf-plugin-audit
description: Audits an installed plugin against every rule and proposes the components it lacks.
disable-model-invocation: true
---

# Auditing a plugin

Four questions, in this order: is it still **complete**, what does it **violate**, what is it
**missing**, and what no longer **earns its place**. The first two are enforced by scripts; the other
two are proposals a human accepts or declines.

Completeness comes first because it is the one property the other checks cannot see. A validator
verdict and a budget figure both stay green over a plugin that lost a page.

This skill is user-invoked, so its description leaves context entirely and only its name remains in
the listing.

## 1. Completeness, before anything else

A plugin claiming a product's online documentation carries **all** of it — every page, every term,
every field with its type and every enum value with its meaning. `COV-06`, `COV-07` This is
re-established on every touch, never assumed from the fact that the plugin once shipped: optimisation
moves and deletes text, so it is exactly the operation that can drop content. `COV-08`

**Read `INVENTORY.json` first, and decide from the hash rather than the date.** `COV-10`

```bash
python3 scripts/inventory.py --plugin <name> --check           # offline: what was recorded, when
python3 scripts/inventory.py --plugin <name> --check --fetch   # one request per page: what changed
```

Every hash matching means the source has not moved and there is nothing to re-extract, whatever the
recorded date says. Only changed, new or missing pages need work. Reach for a full re-enumeration in
three cases: no inventory exists, the source is unreachable and the record is over 30 days old, or
`--fetch` named pages to re-read.

A full pass enumerates from the machine-readable source, never from memory of what the plugin covers:
a docs site through `/sitemap.xml`, an API through its OpenAPI document, a repository through its
tree at a pinned ref. `SOURCE-01` The commands, the mirror, and the three findings to report by name
— UNCOVERED, DANGLING/STALE and thin — live in the distillation skill: call the Skill tool with
"zcf-source-distillation". `COV-01` to `COV-05`, `SHARE-01`

Report the coverage numbers beside the budget figure: a budget number alone reads as success while a
page is missing.

## 2. Violations

```bash
python3 scripts/validate_plugin.py --plugin <name> --strict
python3 scripts/validate_plugin.py --working-set <name> <sibling> <sibling>
python3 scripts/validate_plugin.py --unlisted
```

Each finding names a rule ID. Look it up in [`RULES.md`](../../RULES.md) rather than guessing at the
intent, because the rule records **why** it exists and whether a platform fact or a convention backs
it. A `convention` finding is negotiable in a way a `documented` one is not.

The `--working-set` run is the one people skip and the number that actually overflows: a plugin at
30 % is fine alone and ruinous beside three others.

## 3. Missing components

A plugin should carry every component that earns its place, not only the ones somebody wrote. Each
trigger below is a **tell**, not a rule of thumb: `COMP-01` to `COMP-05`.

| Missing | Tell |
|---|---|
| command | a skill body holds numbered steps someone types out each time |
| agent | a skill asks the main conversation to read many files |
| hook | the plugin states a deterministic rule and nothing checks it |
| router skill | more than three or four user-invoked skills and no index over them |
| introspection catalogue | a skill says "check your project" with no way to |
| rule | the audit finds guidance in prose that no rule ID covers |

Name the trigger with each proposal. A proposal without one is a guess.

## 4. Redundant components

The counterweight matters as much as the list, because an unearned component is pure cost: a command
nobody types, an agent whose result is as large as its input, a hook that fires on every prompt to
match nothing. Report a component no README, skill or agent mentions. `COMP-05`

## Repairs, in order

Apply the cheapest fix that holds, and stop there:
[`OPTIMISATION-MOVES.md`](references/OPTIMISATION-MOVES.md). Deleting facts to shorten a file is the one move
the gate rejects. `COV-04`

## Output

Three sections, in the order above. Violations carry rule IDs and are blocking; proposals carry their
trigger and are advisory. Say which is which, because a reader who cannot tell them apart treats all
of it as optional.

Report only what the files and the gate contain. Invent nothing.

## Reference map

- **[AUDIT-RULES.md](references/AUDIT-RULES.md)**: how to read a finding, which rules a script decides and which
  need judgement, and the exit codes.
- **[OPTIMISATION-MOVES.md](references/OPTIMISATION-MOVES.md)**: the repair sequence, cheapest first, and what
  each move costs.

## Related

Call the Skill tool with "zcf-skill-authoring" when a repair means rewriting a `SKILL.md`, or with
"zcf-component-authoring" for an agent, command or hook. For an anchor collision, tell the user to
run `/zone-claude-forge:zcf-anchor-design`.

## Source

Rules and their grounding live in [`rules.json`](../../rules.json) v1.0.0, rendered as
[`RULES.md`](../../RULES.md); every documented rule there cites
[code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) or a sibling page, retrieved
2026-08-21. Checks are implemented in `scripts/validate_plugin.py`.
