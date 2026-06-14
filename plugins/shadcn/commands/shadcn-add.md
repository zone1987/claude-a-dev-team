---
name: shadcn-add
description: Fügt eine oder mehrere shadcn/ui-Komponenten hinzu — nennt den exakten CLI-Befehl (`npx shadcn@latest add …`), zeigt den Quellcode/Props aus dem passenden shadcn-<komponente>-Skill und baut ein lauffähiges Usage-Beispiel (Radix- oder Base-UI-Variante).
argument-hint: <komponente(n)> z.B. "button dialog form" [--base|--radix] [--usage "Login-Formular"]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-add

Komponente(n) hinzufügen und einsetzen. Skills: das jeweilige `shadcn-<komponente>` + `shadcn-cli`.

## Ablauf
1. Komponenten + Variante aus `$ARGUMENTS` (Default: vorhandene Projekt-Variante / sonst Radix).
2. **CLI:** `npx shadcn@latest add <comp> [<comp> …]` ausgeben (installiert Quellcode + Dependencies in `@/components/ui`).
3. Aus dem `shadcn-<komponente>`-Skill: Imports + Grund-Usage; bei Bedarf Props/Anatomy/Varianten nennen.
4. `--usage` → konkretes, lauffähiges Beispiel bauen (passende Examples des Skills als Vorlage; Code nicht raten).
5. Auf benötigte Peer-Komponenten/Provider hinweisen (z.B. `<TooltipProvider>`, `<SidebarProvider>`).

Feldnamen/Props/Varianten gegen das Komponenten-Skill prüfen. Variante (Radix vs. Base) konsistent halten — Imports unterscheiden sich.
