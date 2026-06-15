---
name: shadcn-vue-add
description: Fügt eine oder mehrere shadcn-vue-Komponenten hinzu — nennt den exakten CLI-Befehl (`npx shadcn-vue@latest add …`), zeigt Quellcode/Props aus dem passenden shadcn-vue-<komponente>-Skill und baut ein lauffähiges SFC-Usage-Beispiel.
argument-hint: <komponente(n)> z.B. "button dialog form" [--usage "Login-Formular"]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-vue-add

Komponente(n) hinzufügen und einsetzen. Skills: das jeweilige `shadcn-vue-<komponente>` + `shadcn-vue-cli`.

## Ablauf
1. Komponenten aus `$ARGUMENTS`.
2. **CLI:** `npx shadcn-vue@latest add <comp> [<comp> …]` (kopiert .vue-Quellcode + Dependencies, z.B. reka-ui, nach `@/components/ui`).
3. Aus dem `shadcn-vue-<komponente>`-Skill: Imports + Grund-Usage (SFC, `<script setup>`); Props/Slots/Emits nennen.
4. `--usage` → konkretes, lauffähiges SFC-Beispiel (passende Demos des Skills als Vorlage; Code nicht raten).
5. Auf benötigte Peer-Komponenten/Provider hinweisen (z.B. `<TooltipProvider>`, `<SidebarProvider>`).

Props/Slots/Emits gegen das Komponenten-Skill + die reka-ui-API prüfen. `v-model` statt React-State.
