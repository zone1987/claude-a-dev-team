# shadcn-vue: Installation

Vollstaendige Installationsanleitungen fuer alle unterstuetzten Frameworks.

Der gemeinsame Abschluss-Schritt in allen Frameworks:

```bash
npx shadcn-vue@latest init
# Frage: Which color would you like to use as base color? › Neutral
```

Danach Komponenten hinzufuegen:

```bash
npx shadcn-vue@latest add button
```

VSCode Extension: shadcn-vue von @selemondev (Marketplace:
`Selemondev.shadcn-vue`) — init CLI, Komponenten installieren, Doku oeffnen,
Snippets.

## Reference Files

- `INSTALLATION-VITE.md` — Vite-Projekt-Setup (npm create vite, Tailwind v4,
  tsconfig paths, vite.config.ts, init, add)
- `INSTALLATION-NUXT.md` — Nuxt-Setup (create nuxt, Tailwind via @tailwindcss/vite
  oder @nuxtjs/tailwindcss, shadcn-nuxt Modul, nuxt.config.ts, ssrWidth Plugin,
  npx nuxi prepare, init, add)
- `INSTALLATION-ASTRO.md` — Astro-Setup (create-astro, tsconfig.json paths, init, add,
  .astro Import-Syntax)
- `INSTALLATION-LARAVEL.md` — Laravel + Inertia (laravel new --vue, sofort add,
  resources/js Pfade)
- `INSTALLATION-MANUAL.md` — Manuelle Installation (Abhaengigkeiten,
  path aliases, globals.css mit allen CSS-Variablen, cn-Helper, components.json)
