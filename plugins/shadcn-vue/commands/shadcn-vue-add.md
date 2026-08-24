---
name: shadcn-vue-add
description: Adds one or more shadcn-vue components — names the exact CLI command (`npx shadcn-vue@latest add …`), shows the Vue source, props, slots and emits from the fitting skill, and builds a runnable usage example.
argument-hint: <component(s)> e.g. "button dialog form" [--usage "login form"]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-vue-add

Add components and put them to use. Skills: the fitting component skill (`shadcn-vue-forms`,
`shadcn-vue-layout`, `shadcn-vue-data`, `shadcn-vue-navigation`, `shadcn-vue-feedback`) plus
`shadcn-vue-setup`.

## Steps
1. Components from `$ARGUMENTS`.
2. **CLI:** print `npx shadcn-vue@latest add <comp> [<comp> …]` (it installs the source and
   dependencies into the `components/ui` alias).
3. From the component skill: the imports and basic usage; name props, slots and emits where needed.
4. `--usage` builds a concrete, runnable single-file component, taking the skill's demos as the
   template — never guess the code.
5. Point out the peer components or providers required (e.g. `<TooltipProvider>`, `<SidebarProvider>`).

Check props, slots and emits against the component skill. The underlying primitive is `reka-ui`, so
its API is what the props ultimately follow.
