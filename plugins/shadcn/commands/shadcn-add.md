---
name: shadcn-add
description: Adds one or more shadcn/ui components — names the exact CLI command (`npx shadcn@latest add …`), shows the source and props from the fitting shadcn skill, and builds a runnable usage example (Radix or Base UI variant).
argument-hint: <component(s)> e.g. "button dialog form" [--base|--radix] [--usage "login form"]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-add

Add components and put them to use. Skills: the fitting component skill (`shadcn-forms`,
`shadcn-layout`, `shadcn-data`, `shadcn-navigation`, `shadcn-feedback`) plus `shadcn-setup`.

## Steps
1. Components and variant from `$ARGUMENTS` (default: the variant already in the project, otherwise Radix).
2. **CLI:** print `npx shadcn@latest add <comp> [<comp> …]` (it installs the source and dependencies
   into `@/components/ui`).
3. From the component skill: the imports and basic usage; name props, anatomy and variants where needed.
4. `--usage` builds a concrete, runnable example, taking the skill's examples as the template — never
   guess the code.
5. Point out the peer components or providers required (e.g. `<TooltipProvider>`, `<SidebarProvider>`).

Check field names, props and variants against the component skill. Keep the variant (Radix vs. Base)
consistent — the imports differ.
