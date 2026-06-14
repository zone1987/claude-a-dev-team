---
name: shadcn-block
description: Fügt einen shadcn/ui-Block ein (Sidebar/Login/Signup/Dashboard) — nennt den CLI-Befehl, zeigt den kompletten Block-Code (alle Dateien) aus dem passenden shadcn-blocks-*-Skill und passt ihn an Branding/Routen/Daten an.
argument-hint: <block> z.B. "sidebar-07" | "login-03" | "dashboard-01" [--customize "Hinweise"]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-block

Block einsetzen. Skills: `shadcn-blocks-overview` + `shadcn-blocks-sidebar`/`-login`/`-signup`/`-dashboard`.

## Ablauf
1. Block aus `$ARGUMENTS` (Liste/Beschreibung in `shadcn-blocks-overview`).
2. **CLI:** `npx shadcn@latest add <block>` (z.B. `sidebar-07`) — installiert alle Block-Dateien + abhängige Komponenten.
3. Aus dem passenden `shadcn-blocks-*`-Skill den kompletten Dateibaum + Code zeigen; Einstiegspunkt (`page.tsx`) erklären.
4. `--customize` → Branding/Navigation/Daten anpassen, ohne die Struktur zu brechen; Sidebar-Mechanik via `shadcn-sidebar`.
5. Abhängige Komponenten/Provider sicherstellen.

Block-Dateien/Code gegen das Block-Skill prüfen — nicht raten. Variante (Radix/Base) des Projekts beachten.
