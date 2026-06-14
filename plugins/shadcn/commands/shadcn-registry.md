---
name: shadcn-registry
description: Scaffold einer eigenen shadcn-kompatiblen Registry — erzeugt registry.json und registry-item.json nach Schema, den shadcn-build-Schritt, Hosting-/Consumer-Hinweise (components.json registries) und optional MCP-Kompatibilität.
argument-hint: [--item-type ui|block|theme|hook|lib|page] [--name "@acme/my-component"] [--mcp]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-registry

Eigene Registry aufsetzen. Skills: `shadcn-registry`, `shadcn-registry-json`, `shadcn-registry-item-json`,
`shadcn-registry-api`, bei `--mcp` `shadcn-mcp`.

## Ablauf
1. **`registry.json`** erstellen (name, homepage, items[]) — Schema aus `shadcn-registry-json`.
2. **`registry-item.json`** je Item nach `$ARGUMENTS` — alle nötigen Felder (`name`, `type` registry:<…>, `title`,
   `description`, `files[]` mit path/type, `dependencies`, `registryDependencies`, `cssVars`, `tailwind`, `envVars`,
   `meta`, `docs`) — Schema aus `shadcn-registry-item-json`. Nur dokumentierte Felder.
3. **Build:** `npx shadcn@latest build` → statische `/r/<name>.json`; unter `public/r` hosten.
4. **Consumer:** Eintrag in `components.json` `registries` (`@namespace`) + `npx shadcn@latest add @namespace/<item>`.
5. `--mcp` → `registry.json` an der Wurzel für MCP-Kompatibilität (`shadcn-mcp`).

Schema-Felder/`type`-Werte gegen die Registry-Skills prüfen — nicht raten. Keine echten Secrets in `envVars` (nur Platzhalter).
