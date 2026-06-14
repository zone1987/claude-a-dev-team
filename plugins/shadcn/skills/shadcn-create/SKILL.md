---
name: shadcn-create
description: shadcn create — neue Projekte aus Templates/Presets per CLI erzeugen, shadcn apply. Trigger: shadcn create, shadcn Projekt erstellen, shadcn template, shadcn apply, scaffold shadcn app.
---

# shadcn-create

`shadcn create` / `npx shadcn@latest create` — scaffold new projects with a
fully configured style, component library, icons, base color, theme, and fonts.

## Create a project

```bash
npx shadcn@latest create
```

Flags:

| Flag          | Description                                        |
|---------------|----------------------------------------------------|
| `--template`  | Framework template: `next`, `vite`, `start`        |
| `--rtl`       | Enable RTL support (`rtl: true` in components.json)|
| `--preset`    | Apply a preset code e.g. `--preset b2D0vQ7G4`      |
| `--pointer`   | Enable `cursor: pointer` for buttons               |

## Available styles (as of 2026)

| Style      | Description                                                     |
|------------|-----------------------------------------------------------------|
| Vega       | The classic shadcn/ui look                                      |
| Nova       | Reduced padding and margins for compact layouts                 |
| Luma       | Rounded geometry, soft elevation, breathable (macOS-inspired)   |
| Sera       | Minimal, editorial, typographic, print-design-inspired          |
| Rhea       | Compact Luma — denser surfaces for focused product interfaces   |

## Apply a preset to existing project

```bash
npx shadcn@latest apply --preset b2D0vQ7G4

# Apply only the theme
npx shadcn@latest apply --preset b2D0vQ7G4 --only theme

# Apply only the fonts
npx shadcn@latest apply --preset b2D0vQ7G4 --only fonts
```

## Preset commands

```bash
npx shadcn@latest preset decode b5owWMfJ8l   # decode a preset code
```

## Add components after creation

```bash
npx shadcn@latest add button
npx shadcn@latest add --all
```

## Install skills for AI assistants

```bash
npx skills add shadcn/ui
```

## Connect the MCP server

```bash
npx shadcn@latest mcp init
```

Source: (root)/new.mdx
