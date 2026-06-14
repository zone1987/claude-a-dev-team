---
name: shadcn-init
description: Scaffold der shadcn/ui-Einrichtung in einem React-Projekt — erkennt das Framework, führt durch `npx shadcn@latest init`, erzeugt/prüft components.json, cn-Util (@/lib/utils), Tailwind-v4-Theme-Tokens (globals.css) und optional Dark-Mode-Provider.
argument-hint: [--framework next|vite|astro|remix|laravel|react-router|tanstack] [--base-color neutral|zinc|slate|stone|gray] [--rsc] [--dark-mode]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-init

Richte shadcn/ui ein. Skills: `shadcn-installation`, `shadcn-components-json`, `shadcn-cli`, `shadcn-tailwind-v4`,
bei `--dark-mode` `shadcn-dark-mode`.

## Ablauf
1. Framework aus `$ARGUMENTS`/Projekt erkennen → passende Schritte (`shadcn-installation/references/<framework>.md`).
2. `npx shadcn@latest init` vorschlagen (oder manuelle Schritte) inkl. Tailwind-v4-Setup.
3. **components.json** erzeugen/prüfen — nur dokumentierte Felder (`shadcn-components-json`): `style`, `rsc`,
   `tsx`, `tailwind.{css,baseColor,cssVariables}`, `aliases.{components,utils,ui,lib,hooks}`, `iconLibrary`.
4. **cn-Util** (`@/lib/utils`: clsx + tailwind-merge) + **globals.css** mit Theme-Tokens (`:root`/`.dark`, `@theme inline`,
   oklch) sicherstellen (Vorlagen in `utils/`).
5. `--dark-mode` → Provider je Framework ergänzen (`shadcn-dark-mode`).

Nur dokumentierte Felder/Befehle (Quelle: `shadcn-components-json`/`shadcn-cli`). Keine Secrets. Variante (Radix/Base) festhalten.
