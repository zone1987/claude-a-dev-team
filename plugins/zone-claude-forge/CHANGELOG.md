# Changelog

## 1.0.0 — 2026-08-21

First release. An authoring instrument for this marketplace, and the first plugin here whose rules
are executable rather than prose.

### Added

- **`rules.json`**, 75 rules, each with a ground class (`documented`, `technique`, `convention`) and
  an enforcement class (`blocking`, `review`). `RULES.md` is generated from it, so the wording a
  reader sees is the wording the gate applies.
- **`scripts/validate_plugin.py`**, the gate the marketplace lacked: every blocking rule in one run
  with an exit code. Modes for a whole plugin, a single file, a working set, unlisted skills, and the
  catalogue itself.
- **`scripts/verify_sources.py`**, citations checked in both directions: every rule grounded, and
  every quotation verbatim on the page it cites.
- **Six skills**, three model-visible at 893 characters (11.2 % of budget) and three user-invoked at
  the cost of their names only. The first plugin here to use `disable-model-invocation`.
- **Two agents**: `claude-source-distiller` (`opus`, `maxTurns: 40`) and
  `claude-component-reviewer` (`sonnet`, read-only through both `tools` and `disallowedTools`).
- **Four commands**: `/zcf-new-skill`, `/zcf-validate`, `/zcf-audit`, `/zcf-distill`.
- **Four hooks**, in the order they fire: a `SessionStart` anchor that names the forge once per
  session and only inside this marketplace (821 characters, and nothing in another project), a
  `UserPromptSubmit` nudge, a `PreToolUse` gate that denies a non-compliant write with a structured
  `permissionDecision` **naming the skill that carries the fix**, and a `PostToolUse` whole-plugin
  check. The gate is registered both in the plugin and in the repo's `.claude/settings.json`, so it
  holds even when the plugin is disabled.
- **`scripts/anchor_inventory.py`**, which collects every `Use when` clause across the marketplace
  (119 skills, 27 plugins) so an anchor collision is visible before it ships.
- **`scripts/audit_coverage.py`** and **`scripts/scaffold_component.py`**, generalising the coverage
  proof and the measured-at-write-time scaffold.

### Corrected against the official documentation

Five assumptions this marketplace held turned out to be wrong. Each is now a rule with a citation:

- **`additionalContext` belongs at the top level**, not inside `hookSpecificOutput`. `CLAUDE.md`
  stated the opposite and called it the most common mistake. (`HOOK-02`)
- **A timed-out `PreToolUse` hook does not block.** A slow gate is an open gate, not a late one, which
  is why the path test runs first. (`HOOK-04`)
- **`skills[]` adds to the default `skills/` scan; it does not restrict it.** A skill under `skills/`
  loads whether or not it is listed, so work in progress kept there costs budget. (`BUDGET-05`)
- **`model:` and `effort:` are valid skill fields.** They are left unused here for portability, since
  only six fields survive outside Claude Code, which is a convention rather than a fact.
- **`disable-model-invocation` does not cost zero**: the listing always contains every skill name.
  (`BUDGET-01`)

### Known limits

- `verify_sources.py --fetch` needs network access. Where it is unavailable, pass `--pages DIR` and
  verify against a local mirror; 13 of the 35 documented rules are confirmed verbatim this way, and
  the remaining four pages were read in full when the catalogue was written.
- `audit_coverage.py --repo` needs a tree listing passed through `--map`.
- Aligning the other 26 plugins with this catalogue is deliberately out of scope for this release.
