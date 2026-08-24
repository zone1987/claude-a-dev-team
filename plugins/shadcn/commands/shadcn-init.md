---
name: shadcn-init
description: Scaffolds the shadcn/ui setup in a React project — detects the framework, walks through `npx shadcn@latest init`, writes or checks components.json, the cn util (@/lib/utils), the Tailwind v4 theme tokens (globals.css) and optionally a dark-mode provider.
argument-hint: [--framework next|vite|astro|remix|laravel|react-router|tanstack] [--base-color neutral|zinc|slate|stone|gray] [--rsc] [--dark-mode]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-init

Set a project up for shadcn/ui. Skills: `shadcn-setup`, plus `shadcn-theming` for the tokens.

## Steps
1. Framework and options from `$ARGUMENTS`; where none is given, detect it from the project.
2. **CLI:** `npx shadcn@latest init` with the fitting flags for that framework.
3. **`components.json`**: write or check it — style, base colour, `rsc`, `tailwind.cssVariables`,
   and the aliases (`components`, `utils`, `ui`, `lib`, `hooks`).
4. **`cn()`** in `@/lib/utils` (clsx plus tailwind-merge), and the Tailwind v4 theme tokens in
   `globals.css` (`:root` plus `.dark`, oklch, `@theme inline`).
5. `--dark-mode` adds the provider the framework calls for.

Use the documented components.json fields only (source: `shadcn-setup`). The alias paths have to
match the project's actual tsconfig paths.
