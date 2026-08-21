---
name: zcf-validate
description: Runs every blocking rule against a plugin and reports each violation with its file, line and rule id.
argument-hint: <plugin> [--strict] [--json]
allowed-tools: Read, Glob, Grep, Bash
model: haiku
---

# /zcf-validate

Check the plugin named in $ARGUMENTS against every blocking rule in the catalogue.

## Steps

1. Run the gate, passing through any flags:

   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/scripts/validate_plugin.py" --plugin <plugin> [--strict] [--json]
   ```

2. Run the working-set check as well, because a plugin inside its own budget can still overflow
   beside its siblings. Use the plugins a session would realistically enable together:

   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/scripts/validate_plugin.py" --working-set <plugin> <sibling> <sibling>
   ```

3. For each finding, look the rule ID up in `RULES.md` and report its **ground class** alongside:
   `documented` is not negotiable, `technique` is arguable against its measurement, `convention` is
   arguable against its purpose.

## Output

The gate's own lines, unchanged, then one line per finding naming the rule's ground class and the
smallest fix that would clear it. Close with the budget figure and the exit code.

Do not repair anything: this command reports. Report only what the gate and the files contain.
Invent nothing.
