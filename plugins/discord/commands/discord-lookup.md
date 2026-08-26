---
name: discord-lookup
description: Look up a Discord endpoint, object, field, intent, permission, opcode or error code and print its exact type, values and constraints.
argument-hint: <endpoint|object|field|intent|permission|opcode|error-code>
allowed-tools: Read, Glob, Grep, Bash
model: haiku
---

# /discord-lookup

Find what $ARGUMENTS names in this plugin's reference files and print it exactly as documented.

## Steps

1. **Grep the reference files** for the term:
   `grep -rn "<term>" "${CLAUDE_PLUGIN_ROOT}/skills" --include='*.md'`
   Try the exact spelling first, then a case-insensitive search, then the snake_case and
   PascalCase variants — Discord uses `snake_case` for JSON fields, `SCREAMING_SNAKE_CASE` for
   events and intents, and `PascalCase` for object names.
2. **Open the file with the definitive table**, not the first mention. A field is usually named in
   several files but defined in exactly one — the definition is the row inside a
   `| Field | Type | Description |` table.
3. **Print what the documentation states**, and nothing more:
   - **A field**: name, exact type, optional (`name?`) or nullable (`?type`), description, default
     and constraints if stated.
   - **An endpoint**: method, full path with `{placeholders}`, every query and body parameter with
     its type and optionality, the success response, and the documented errors.
   - **An enum or flag**: every value with its number or bit and its meaning. Print the complete
     list, never a sample.
   - **An intent**: its bit value, the events it gates, and whether it is privileged.
   - **A permission**: its bit value in decimal and hex, and where it applies.
   - **An opcode or error code**: its number, name, direction and meaning.
4. **Name the source file** for each answer, as `skills/<skill>/<FILE>.md`.
5. **Say when a term is absent.** If the grep finds nothing across every reference file, the
   documentation does not carry that name. Report that, and offer the closest documented names the
   search did surface.

Invent nothing. A field this plugin cannot find is a field Discord does not document under that
name — report the absence rather than a plausible spelling.
