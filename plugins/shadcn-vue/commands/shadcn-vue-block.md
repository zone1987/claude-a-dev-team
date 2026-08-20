---
name: shadcn-vue-block
description: Fügt einen shadcn-vue-Block ein (Sidebar/Login/Signup/OTP/Dashboard/Products) — nennt den CLI-Befehl, zeigt den kompletten Block-Code (alle .vue-Dateien) aus dem passenden shadcn-vue-blocks-*-Skill und passt ihn an Branding/Routen/Daten an.
argument-hint: <block> z.B. "sidebar-07" | "login-03" | "dashboard-01" [--customize "Hinweise"]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-vue-block

Block einsetzen. Skills: `shadcn-vue-blocks` + `shadcn-vue-blocks`/`-login`/`-signup`/`-otp`/`-dashboard`.

## Ablauf
1. Block aus `$ARGUMENTS` (Liste in `shadcn-vue-blocks`).
2. **CLI:** `npx shadcn-vue@latest add <block>` — installiert alle .vue-Dateien + abhängige Komponenten.
3. Aus dem passenden `shadcn-vue-blocks-*`-Skill den kompletten Dateibaum + Code zeigen; Einstiegspunkt erklären.
4. `--customize` → Branding/Navigation/Daten anpassen, ohne die Struktur zu brechen; Sidebar-Mechanik via `shadcn-vue-layout`.
5. Abhängige Komponenten/Provider sicherstellen.

Block-Dateien/Code gegen das Block-Skill prüfen — nicht raten.
