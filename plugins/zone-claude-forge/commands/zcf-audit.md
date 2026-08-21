---
name: zcf-audit
description: Audits a plugin for violations, missing components and components that no longer earn their place.
argument-hint: <plugin>
allowed-tools: Read, Glob, Grep, Bash
model: sonnet
---

# /zcf-audit

Audit the plugin named in $ARGUMENTS on three axes, and keep them clearly apart: violations are
blocking, the other two are proposals a human accepts or declines.

## Steps

1. Call the Skill tool with "zcf-plugin-audit" for the method.
2. **Violations**: run `validate_plugin.py --plugin <plugin> --strict`, then `--working-set` with the
   plugins a session would enable together, then `--unlisted`.
3. **Missing components**: work the tells in `zcf-plugin-audit`. Name the tell with each proposal; a
   proposal without one is a guess.
4. **Redundant components**: find any command, agent or hook that no README, skill or agent mentions.
5. For anything judgement-bound, dispatch `claude-component-reviewer` rather than deciding here: it
   holds no write tools, so its findings stay reviewable.

## Output

Three sections in that order, each labelled with whether it is blocking or advisory. Every violation
carries a rule ID and its ground class; every proposal carries its tell.

Report only what the gate and the files contain. Invent nothing.
