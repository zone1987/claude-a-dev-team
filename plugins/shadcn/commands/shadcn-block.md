---
name: shadcn-block
description: Inserts a shadcn/ui block (sidebar, login, signup, dashboard) — names the CLI command, shows the block's complete code (every file) from the shadcn-blocks skill, and adapts it to your branding, routes and data.
argument-hint: <block> e.g. "sidebar-07" | "login-03" | "dashboard-01" [--customize "notes"]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-block

Insert a block and adapt it. Skills: `shadcn-blocks`, plus `shadcn-setup` for the project wiring.

## Steps
1. Block and options from `$ARGUMENTS`.
2. **CLI:** print `npx shadcn@latest add <block>` — it writes every file the block consists of.
3. From `shadcn-blocks`: walk the complete code, file by file, and say what each part does.
4. Adapt it to the project: branding, routes, data sources, and the components already present.
5. `--customize` applies the notes given, without inventing structure the block does not have.

Take the block's code from the skill rather than reconstructing it: a block is several files that
have to match.
