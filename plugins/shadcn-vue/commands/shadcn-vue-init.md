---
name: shadcn-vue-init
description: Scaffold der shadcn-vue-Einrichtung in einem Vue-/Nuxt-Projekt — erkennt das Framework, führt durch `npx shadcn-vue@latest init`, erzeugt/prüft components.json, cn-Util (@/lib/utils), Tailwind-v4-Theme-Tokens (globals.css) und optional Dark-Mode (useColorMode/nuxt color-mode).
argument-hint: [--framework vite|nuxt|astro|laravel] [--base-color neutral|zinc|slate|stone|gray] [--dark-mode]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-vue-init

Richte shadcn-vue ein. Skills: `shadcn-vue-installation`, `shadcn-vue-components-json`, `shadcn-vue-cli`,
`shadcn-vue-tailwind-v4`, bei `--dark-mode` `shadcn-vue-dark-mode`.

## Ablauf
1. Framework aus `$ARGUMENTS`/Projekt erkennen → passende Schritte (`shadcn-vue-installation/references/<fw>.md`).
2. `npx shadcn-vue@latest init` vorschlagen (oder manuelle Schritte) inkl. Tailwind-v4-Setup.
3. **components.json** erzeugen/prüfen — nur dokumentierte Felder (`shadcn-vue-components-json`): `style`, `typescript`,
   `tailwind.{css,baseColor,cssVariables}`, `aliases.{components,utils,ui,lib,composables}`, `iconLibrary`, `framework`.
4. **cn-Util** (`@/lib/utils`) + **globals.css** mit Theme-Tokens (`:root`/`.dark`, `@theme inline`, oklch) sicherstellen (Vorlagen in `utils/`).
5. `--dark-mode` → `useColorMode` (@vueuse) bzw. `@nuxtjs/color-mode` einrichten (`shadcn-vue-dark-mode`).

Nur dokumentierte Felder/Befehle (Quelle: `shadcn-vue-components-json`/`shadcn-vue-cli`). Keine Secrets.
