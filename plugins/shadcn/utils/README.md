# shadcn Utils

Ready-to-use templates — copy one and adapt it to your project. Never paste real credentials
(registry auth belongs in an env var).

| File | Purpose |
|---|---|
| `components.json` | The shadcn project configuration (new-york, neutral, RSC, aliases, Tailwind v4 cssVariables). Goes in the project root. Details: skill `shadcn-setup`. |
| `lib-utils.ts` | The mandatory `cn()` helper (clsx plus tailwind-merge) — put it in `lib/utils.ts` or `src/lib/utils.ts`. |
| `globals.css` | The Tailwind v4 theme: every CSS variable token (`:root` plus `.dark`, oklch) and the `@theme inline` mapping. Details: skill `shadcn-theming`. |
| `registry.json` | An example index for a registry of YOUR OWN. Details: skill `shadcn-setup`. |
| `registry-item.example.json` | An example registry item with every field that matters. Details: skill `shadcn-setup`. |

The **shadcn MCP server** ships with the plugin through `.mcp.json` in its root (command
`npx shadcn@latest mcp`). Details: skill `shadcn-setup`.
