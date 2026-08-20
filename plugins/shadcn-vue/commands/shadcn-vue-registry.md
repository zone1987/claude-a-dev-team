---
name: shadcn-vue-registry
description: Scaffold einer eigenen shadcn-vue-kompatiblen Registry — erzeugt registry.json und registry-item.json nach Schema, den shadcn-vue-build-Schritt, Hosting-/Consumer-Hinweise (components.json registries) und optional MCP-Kompatibilität.
argument-hint: [--item-type ui|block|theme|composable|lib|page] [--name "@acme/my-component"] [--mcp]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-vue-registry

Eigene Registry aufsetzen. Skills: `shadcn-vue-registry`, `shadcn-vue-blocks`, `shadcn-vue-blocks`,
`shadcn-vue-blocks`, bei `--mcp` `shadcn-vue-setup`.

## Ablauf
1. **`registry.json`** erstellen (name, homepage, items[]) — Schema aus `shadcn-vue-blocks`.
2. **`registry-item.json`** je Item nach `$ARGUMENTS` — alle nötigen Felder (`name`, `type` registry:<…>, `title`,
   `description`, `files[]` mit path/type, `dependencies`, `registryDependencies`, `cssVars`, `tailwind`, `envVars`,
   `meta`, `docs`) — Schema aus `shadcn-vue-blocks`. Nur dokumentierte Felder. Vue: `.vue`-SFC, `composables`.
3. **Build:** `npx shadcn-vue@latest build` → statische `/r/<name>.json`; unter `public/r` hosten.
4. **Consumer:** Eintrag in `components.json` `registries` (`@namespace`) + `npx shadcn-vue@latest add @namespace/<item>`.
5. `--mcp` → `registry.json` an der Wurzel für MCP-Kompatibilität (`shadcn-vue-setup`).

Schema-Felder/`type`-Werte gegen die Registry-Skills prüfen. Keine echten Secrets in `envVars`.
