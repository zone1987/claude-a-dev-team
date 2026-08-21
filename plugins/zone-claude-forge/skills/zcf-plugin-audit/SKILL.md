---
name: zcf-plugin-audit
description: Audits an installed plugin against every rule and proposes the components it lacks.
disable-model-invocation: true
---

# Auditing a plugin

Three questions, in this order: what does it **violate**, what is it **missing**, and what no longer
**earns its place**. The first is enforced by a script; the other two are proposals a human accepts
or declines.

This skill is user-invoked, so its description leaves context entirely and only its name remains in
the listing.

## 1. Violations

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

## 2. Missing components

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

## 3. Redundant components

The counterweight matters as much as the list, because an unearned component is pure cost: a command
nobody types, an agent whose result is as large as its input, a hook that fires on every prompt to
match nothing. Report a component no README, skill or agent mentions. `COMP-05`

## Repairs, in order

Apply the cheapest fix that holds, and stop there:
[`OPTIMISATION-MOVES.md`](OPTIMISATION-MOVES.md). Deleting facts to shorten a file is the one move
the gate rejects. `COV-04`

## Output

Three sections, in the order above. Violations carry rule IDs and are blocking; proposals carry their
trigger and are advisory. Say which is which, because a reader who cannot tell them apart treats all
of it as optional.

Report only what the files and the gate contain. Invent nothing.

## Reference map

- **[AUDIT-RULES.md](AUDIT-RULES.md)**: how to read a finding, which rules a script decides and which
  need judgement, and the exit codes.
- **[OPTIMISATION-MOVES.md](OPTIMISATION-MOVES.md)**: the repair sequence, cheapest first, and what
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
