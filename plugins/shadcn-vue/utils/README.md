# shadcn-vue Utils

Einsatzfertige Vorlagen — kopieren und an dein Projekt anpassen. Keine echten Credentials einfügen (Registry-Auth via Env-Var).

| Datei | Zweck |
|---|---|
| `components.json` | shadcn-vue-Projektkonfiguration (new-york, neutral, `framework`, Aliase inkl. `composables`, Tailwind-v4 cssVariables). Ins Projekt-Root. Details: Skill `shadcn-vue-components-json`. |
| `lib-utils.ts` | Der Pflicht-Helfer `cn()` (clsx + tailwind-merge) → nach `src/lib/utils.ts`. |
| `globals.css` | Tailwind-v4-Theme: alle CSS-Variablen-Tokens (`:root` + `.dark`, oklch) + `@theme inline`-Mapping. Details: Skills `shadcn-vue-theming`, `shadcn-vue-tailwind-v4`. |
| `registry.json` | Beispiel-Index einer EIGENEN Registry. Details: Skill `shadcn-vue-registry-json`. |
| `registry-item.example.json` | Beispiel eines Registry-Items mit allen wichtigen Feldern (`.vue`/`composable`). Details: Skill `shadcn-vue-registry-item-json`. |

Der **shadcn-vue-MCP-Server** wird über die `.mcp.json` im Plugin-Root mitgeliefert (`npx shadcn-vue@latest mcp`). Details: Skill `shadcn-vue-mcp`.
