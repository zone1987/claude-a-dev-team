---
name: reui-license
description: Checks and repairs the ReUI licence setup — the key, the authenticated registry form, and what each plan actually unlocks.
argument-hint: [--fix]
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
model: sonnet
---

Check this project's ReUI licence setup. `$ARGUMENTS` may carry `--fix` to repair what is wrong.

## Check both halves

A premium install needs both, and one without the other fails with a 401:

1. **`REUI_LICENSE_KEY`** — in the environment or `.env.local`.
2. **The authenticated registry form** — the `@reui` entry in `components.json` as an object with
   `"headers": { "Authorization": "Bearer ${REUI_LICENSE_KEY}" }`, not the plain string.

Also check `.env.local` is git-ignored, and that no real key or `reui_pat_` token sits in a tracked
file. Report a committed credential plainly and move it to the environment.

## Report what each tier gives

- **Free** — 22 primitives (plus the documented `file-upload` pattern), 1,105 `c-*` examples, the
  registry, and the MCP at 100 calls/day.
- **Pro** — adds all 533 premium blocks, and removes the MCP daily limit.
- **Ultimate** — adds the 638 icons and 14 full-page templates on top of Pro.

## Report

Each half as present or missing, what the current setup can install, and — with `--fix` — the files
changed. Never print the key itself.
