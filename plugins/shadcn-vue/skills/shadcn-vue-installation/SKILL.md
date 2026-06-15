---
name: shadcn-vue-installation
description: >
  shadcn-vue Setup und Installation fuer alle unterstuetzten Frameworks: Vite, Nuxt, Astro,
  Laravel (Inertia), manuell. Alle Schritte, Befehle und Konfigurationen vollstaendig.
  Triggers: "shadcn-vue installieren", "shadcn vue setup", "shadcn vue vite",
  "shadcn vue nuxt", "shadcn vue astro", "shadcn vue laravel", "shadcn vue manual install",
  "npx shadcn-vue init", "shadcn vue tailwind setup", "shadcn vue getting started",
  "install shadcn vue", "shadcn vue project setup"
---

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

- `references/vite.md` — Vite-Projekt-Setup (npm create vite, Tailwind v4,
  tsconfig paths, vite.config.ts, init, add)
- `references/nuxt.md` — Nuxt-Setup (create nuxt, Tailwind via @tailwindcss/vite
  oder @nuxtjs/tailwindcss, shadcn-nuxt Modul, nuxt.config.ts, ssrWidth Plugin,
  npx nuxi prepare, init, add)
- `references/astro.md` — Astro-Setup (create-astro, tsconfig.json paths, init, add,
  .astro Import-Syntax)
- `references/laravel.md` — Laravel + Inertia (laravel new --vue, sofort add,
  resources/js Pfade)
- `references/manual.md` — Manuelle Installation (Abhaengigkeiten,
  path aliases, globals.css mit allen CSS-Variablen, cn-Helper, components.json)
