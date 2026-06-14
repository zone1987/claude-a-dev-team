# shadcn/ui Full Changelog

## 2026

### June 2026
- GitHub Registries: any public GitHub repo becomes a registry via `registry.json`
- `shadcn add owner/repo/item[#ref]` syntax
- `shadcn registry validate owner/repo`
- `shadcn eject` command (eject from CLI configuration)

### May 2026
- `registry include` — compose registry from multiple `registry.json` files
- `shadcn registry validate` — validate local or GitHub registry
- Package imports (`package.json#imports`), target aliases (`@ui/`, `@lib/`, `@hooks/`, `@components/`)

### April 2026
- `shadcn apply` command — apply preset to existing project
- Partial preset apply: `--only theme`, `--only fonts`
- `shadcn preset decode <code>` — decode a preset code
- `--pointer` flag for `cursor: pointer` on buttons
- Sera style (minimal, editorial, typographic)

### March 2026
- shadcn/cli v4
- shadcn/skills package — install skill files for AI assistants
- Luma style (rounded, soft elevation, macOS-inspired)
- Rhea style (compact Luma)

### February 2026
- Blocks available for both Radix UI and Base UI
- Unified `radix-ui` package (single import instead of individual `@radix-ui/react-*`)

### January 2026
- First-class RTL support (`--rtl` flag, `rtl: true` in components.json, `DirectionProvider`)
- Base UI documentation published
- Inline-start/inline-end physical-to-logical style migration

## 2025

### December 2025
- `npx shadcn create` command (project scaffolding)
- 5 new styles: Vega, Nova, Luma, Sera, Rhea

### October 2025
- Registry Directory (curated open-source namespace index)
- New components: Spinner, Kbd, Field, Item, FieldGroup, FieldLabel, FieldError, FieldDescription
- Component composition patterns

### September 2025
- Registry Index: open-source namespace directory at `https://ui.shadcn.com/r/registries.json`

### August 2025
- shadcn CLI 3.0:
  - Namespaced registries (`@namespace/item` syntax)
  - Authenticated / private registries
  - MCP server (`shadcn mcp`, `shadcn mcp init --client <name>`)

### July 2025
- Universal registry items (`registry:item` type — no framework detection needed)
- Local file support: `shadcn add ./block.json`

### June 2025
- Calendar component upgrade (React DayPicker v9)
- `shadcn migrate radix` command

### April 2025
- MCP server support (`shadcn@latest mcp init`)
- shadcn 2.5.0 "resolve anywhere" — works without `components.json`

### February 2025
- Tailwind v4 and React 19 preview support
- Updated registry schema (new fields, `extends`, `config`)

## 2024

### November–December 2024
- Sidebar component
- Icon library selection at init
- Monorepo support

### October 2024
- React 19 support

### July–September 2024
- Lift Mode for blocks (edit individual block components in v0)
- `npx shadcn init` (simplified init command)

### April–June 2024
- Breadcrumb component
- OTP (one-time password) input

### January–March 2024
- Blocks system launched (pre-built full-page layouts)

## 2023

### Late 2023
- New CLI replacing legacy installer
- JavaScript (non-TypeScript) project support
- New components: Carousel, Drawer, Pagination, Resizable, Sonner, Toggle Group

Source: changelog/index.mdx + changelog/*.mdx
