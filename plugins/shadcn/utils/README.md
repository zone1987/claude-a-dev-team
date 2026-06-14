# shadcn Utils

Einsatzfertige Vorlagen — kopieren und an dein Projekt anpassen. Keine echten Credentials einfügen (Registry-Auth via Env-Var).

| Datei | Zweck |
|---|---|
| `components.json` | shadcn-Projektkonfiguration (new-york, neutral, RSC, Aliase, Tailwind-v4 cssVariables). Ins Projekt-Root. Details: Skill `shadcn-components-json`. |
| `lib-utils.ts` | Der Pflicht-Helfer `cn()` (clsx + tailwind-merge) → nach `lib/utils.ts` bzw. `src/lib/utils.ts`. |
| `globals.css` | Tailwind-v4-Theme: alle CSS-Variablen-Tokens (`:root` + `.dark`, oklch) + `@theme inline`-Mapping. Details: Skills `shadcn-theming`, `shadcn-tailwind-v4`, `shadcn-colors`. |
| `registry.json` | Beispiel-Index einer EIGENEN Registry. Details: Skill `shadcn-registry-json`. |
| `registry-item.example.json` | Beispiel eines Registry-Items mit allen wichtigen Feldern. Details: Skill `shadcn-registry-item-json`. |

Der **shadcn-MCP-Server** wird über die `.mcp.json` im Plugin-Root mitgeliefert (Befehl `npx shadcn@latest mcp`). Details: Skill `shadcn-mcp`.
