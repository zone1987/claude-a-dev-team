---
name: reui-sync
description: Regenerates this plugin's registry references from reui.io and reports what changed upstream.
argument-hint: [--check]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
model: sonnet
---

Refresh the ReUI registry references. `$ARGUMENTS` may carry `--check` to report drift without
writing anything.

## Steps

1. **Fetch** `https://reui.io/r/registry.json` into a scratch file and record its sha256.
2. **Compare** that hash with the one recorded in
   `skills/reui-registry/references/FREE-VS-PREMIUM.md`. Identical means no drift — say so and stop.
3. **Report the delta** before writing: items added and removed, and any change in the per-tier
   counts (free primitives, `c-*` examples, premium blocks per group).
4. **Regenerate**, unless `--check`:

   ```bash
   python3 scripts/gen_registry_refs.py --registry <scratch>/registry.json --out .
   ```

   The generated files carry the new hash. Never hand-edit them.
5. **Check the docs too.** `https://reui.io/llms.txt` states the upstream counts; if they disagree
   with the regenerated files, say so rather than papering over it — that means the registry
   document and the site index have diverged.
6. **Note anything the registry cannot tell you**: icons and templates are not in `registry.json`
   (`/r/icons.json` answers 401), so their counts come from `llms.txt` alone.

## Report

The old and new hashes, the counts per tier before and after, the items added and removed, and the
files rewritten.
