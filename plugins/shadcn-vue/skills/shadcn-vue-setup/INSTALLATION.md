# shadcn-vue: Installation

Complete installation guides for all supported frameworks.

The shared final step across all frameworks:

```bash
npx shadcn-vue@latest init
# Question: Which color would you like to use as base color? › Neutral
```

Then add components:

```bash
npx shadcn-vue@latest add button
```

VSCode extension: shadcn-vue by @selemondev (Marketplace:
`Selemondev.shadcn-vue`) — init CLI, install components, open docs,
snippets.

## Reference Files

- `INSTALLATION-VITE.md` — Vite project setup (npm create vite, Tailwind v4,
  tsconfig paths, vite.config.ts, init, add)
- `INSTALLATION-NUXT.md` — Nuxt setup (create nuxt, Tailwind via @tailwindcss/vite
  or @nuxtjs/tailwindcss, shadcn-nuxt module, nuxt.config.ts, ssrWidth plugin,
  npx nuxi prepare, init, add)
- `INSTALLATION-ASTRO.md` — Astro setup (create-astro, tsconfig.json paths, init, add,
  .astro import syntax)
- `INSTALLATION-LARAVEL.md` — Laravel + Inertia (laravel new --vue, add right away,
  resources/js paths)
- `INSTALLATION-MANUAL.md` — Manual installation (dependencies,
  path aliases, globals.css with all CSS variables, cn helper, components.json)
