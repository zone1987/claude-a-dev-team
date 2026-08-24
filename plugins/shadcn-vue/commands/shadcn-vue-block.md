---
name: shadcn-vue-block
description: Inserts a shadcn-vue block (sidebar, login, signup, OTP, dashboard, products) — names the CLI command, shows the block's complete code (every .vue file) from the shadcn-vue-blocks skill, and adapts it to your branding, routes and data.
argument-hint: <block> e.g. "sidebar-07" | "login-03" | "dashboard-01" [--customize "notes"]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-vue-block

Insert a block and adapt it. Skills: `shadcn-vue-blocks`, plus `shadcn-vue-setup` for the wiring.

## Steps
1. Block and options from `$ARGUMENTS`.
2. **CLI:** print `npx shadcn-vue@latest add <block>` — it writes every `.vue` file the block needs.
3. From `shadcn-vue-blocks`: walk the complete code, file by file, and say what each part does.
4. Adapt it to the project: branding, routes (vue-router or Nuxt pages), data sources, and the
   components already present.
5. `--customize` applies the notes given, without inventing structure the block does not have.

Take the block's code from the skill rather than reconstructing it: a block is several files that
have to match.
