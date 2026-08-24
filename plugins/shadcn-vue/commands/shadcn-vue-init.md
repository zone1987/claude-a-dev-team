---
name: shadcn-vue-init
description: Scaffolds the shadcn-vue setup in a Vue or Nuxt project — detects the framework, walks through `npx shadcn-vue@latest init`, writes or checks components.json, the cn util, the Tailwind v4 theme tokens and optionally dark mode.
argument-hint: [--framework vite|nuxt|astro|laravel] [--base-color neutral|zinc|slate|stone|gray] [--dark-mode]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-vue-init

Set a project up for shadcn-vue. Skills: `shadcn-vue-setup`, plus `shadcn-vue-theming` for tokens.

## Steps
1. Framework and options from `$ARGUMENTS`; where none is given, detect it from the project.
2. **CLI:** `npx shadcn-vue@latest init` with the fitting flags for that framework.
3. **`components.json`**: write or check it — style, base colour, `tailwind.cssVariables`, and the
   aliases (`components`, `utils`, `ui`, `lib`, `composables`).
4. **`cn()`** in the utils alias (clsx plus tailwind-merge), and the Tailwind v4 theme tokens in the
   global stylesheet (`:root` plus `.dark`, oklch, `@theme inline`).
5. `--dark-mode` wires up `useColorMode` from @vueuse, or Nuxt's color-mode module.

Use the documented components.json fields only (source: `shadcn-vue-setup`). The alias paths have to
match the project's actual tsconfig or Nuxt aliases.
