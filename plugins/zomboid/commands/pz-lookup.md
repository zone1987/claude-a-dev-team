---
name: pz-lookup
description: Look up a Project Zomboid class, method, Lua global, event, item, property or command and print its exact signature and values.
argument-hint: <class|method|event|item|property|command> [--build 42]
allowed-tools: Read, Glob, Grep, Bash
model: haiku
---

# /pz-lookup

Find what $ARGUMENTS names in this plugin's reference files and print it exactly as documented.

## Steps

1. **Grep the reference files**, exact spelling first:
   `grep -rn "<term>" "${CLAUDE_PLUGIN_ROOT}/skills" --include='*.md'`
   Then case-insensitively. Zomboid mixes conventions, so try the variants: `camelCase` for Java
   methods and Lua globals, `PascalCase` for class names, `PascalCase` for script keys
   (`MaxRange`, `Capacity`), `SCREAMING_SNAKE` for some enum values.
2. **Open the file holding the definition**, not the first mention. A name appears in several files
   but is defined in one — the definition is the row in a table or the bullet under a class heading.
3. **Print what the reference states**, and nothing beyond it:
   - **A Java class**: package, kind, and every member signature the reference lists.
   - **A method**: the declaring class, the exact signature with parameter types, whether static.
   - **A Lua global**: signature, which side it exists on, the defining file.
   - **An event**: every argument in order with its type, when it fires, which side.
   - **An item**: its module-qualified name and every property the data table carries.
   - **A script property**: the block types it applies to, its value type, and every legal value
     where the catalogue enumerates them.
   - **A server command**: the exact command string, its arguments, and the required access level.
4. **Name the source file** for each answer, as `skills/<skill>/references/<FILE>.md`.
5. **Say when a term is absent.** If the grep finds nothing, the reference files do not carry that
   name — report that, then offer the closest names the search surfaced. Where the game is installed,
   add: the installation can settle it, at
   `~/Library/Application Support/Steam/steamapps/common/ProjectZomboid/Project Zomboid.app/Contents/Java/`.

Invent nothing. A signature this plugin cannot find is a signature to report as missing, never one to
reconstruct from a plausible pattern.
