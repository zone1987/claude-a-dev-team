# shadcn create: Full Reference

## Create command

```bash
npx shadcn@latest create
```

Interactive wizard that scaffolds a new project with:
- Framework choice
- Style selection
- Base color
- Icon library
- Font
- RTL toggle
- Preset option

## Flags

| Flag          | Values                              | Description                                |
|---------------|-------------------------------------|--------------------------------------------|
| `--template`  | `next`, `vite`, `start`             | Framework template                         |
| `--rtl`       | (boolean)                           | Enable RTL; sets `"rtl": true` in `components.json` |
| `--preset`    | preset code (e.g. `b2D0vQ7G4`)     | Apply a preset (theme, style, fonts, etc.) |
| `--pointer`   | (boolean)                           | Set `cursor: pointer` for all buttons      |

## Available styles (2026)

| Style  | Character                                                 |
|--------|-----------------------------------------------------------|
| Vega   | Classic shadcn/ui look                                    |
| Nova   | Reduced padding and margins, compact                      |
| Luma   | Rounded geometry, soft elevation, macOS-inspired          |
| Sera   | Minimal, editorial, typographic, print-design-inspired    |
| Rhea   | Compact Luma for focused product interfaces               |

## Apply preset to existing project

```bash
npx shadcn@latest apply --preset b2D0vQ7G4

# Apply only the theme
npx shadcn@latest apply --preset b2D0vQ7G4 --only theme

# Apply only the fonts
npx shadcn@latest apply --preset b2D0vQ7G4 --only fonts
```

## Decode a preset code

```bash
npx shadcn@latest preset decode b2D0vQ7G4
```

## Post-creation steps

```bash
# Add a component
npx shadcn@latest add button

# Add all components
npx shadcn@latest add --all

# Install AI skills
npx skills add shadcn/ui

# Connect the MCP server for AI assistants
npx shadcn@latest mcp init
```

## components.json fields set by create

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "base-nova",
  "rtl": true,
  "rsc": true,
  "tsx": true,
  "tailwind": { "baseColor": "neutral" },
  "aliases": {
    "components": "@/components",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  }
}
```

Source: (root)/new.mdx
