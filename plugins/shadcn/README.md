# shadcn

The **ultimate, comprehensive library for [shadcn/ui](https://ui.shadcn.com)** — the copy-and-paste component collection for React (Tailwind v4, **Radix UI _and_ Base UI**). shadcn/ui is not an npm package: components are **copied** into your project by the CLI and they are yours.

This library contains **everything**, distilled from `shadcn-ui/ui` (`apps/v4`, documentation MDX + registry) and verified against the actual source code:

- **All 59 components** — grouped into domain skills with **complete, unabridged source code**, props/anatomy, **all examples** and the **Base UI vs. Radix UI differences**.
- **All 27 blocks** (16× sidebar, 5× login, 5× signup, dashboard) — complete code of every block file.
- **All 70 charts** (area/bar/line/pie/radar/radial/tooltip) — complete code + the chart system (ChartContainer/ChartConfig).
- **Setup**: installation for Next.js, Vite, Astro, Remix, Laravel, Gatsby, React Router, TanStack (Start/Router) + manual; `components.json` (every field), CLI (every command/flag), Tailwind v4, monorepo, React 19.
- **Theming**: all CSS variable tokens, colour palettes (oklch), dark mode (5 frameworks), custom themes.
- **Forms** (react-hook-form/TanStack Form/Formisch/Next), **RTL**, **building your own registry** (registry.json + registry-item.json schema, build, hosting, MCP), **directory**, **shadcn create**, **changelog**.
- **Bundled shadcn MCP server** (`.mcp.json`) for browsing/installing registry items live.

Lean `SKILL.md` files, with the depth in flat SCREAMING-CASE.md reference files next to each `SKILL.md`. **8 skills, 444 reference files.**

Part of the marketplace **[claude-a-dev-team](../../README.md)**.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shadcn@claude-a-dev-team
```

## MCP server (bundled)

The plugin ships the official **shadcn MCP server** via `.mcp.json` (`npx shadcn@latest mcp`). Claude can use it to search registries and install components through natural language. Configure additional registries in `components.json` under `registries`; details and client setup live in the `shadcn-setup` skill.

```jsonc
// plugins/shadcn/.mcp.json
{ "mcpServers": { "shadcn": { "command": "npx", "args": ["shadcn@latest", "mcp"] } } }
```

## Usage

- **Skills** load automatically (for example "shadcn button", "shadcn add dialog", "shadcn sidebar block", "shadcn area chart", "components.json", "shadcn theme").
- **Agents:** `shadcn-expert` (general), `shadcn-setup` (installation/CLI), `shadcn-theming-expert` (colours/dark mode), `shadcn-blocks-expert`, `shadcn-charts-expert`, `shadcn-registry-builder`.
- **Commands:** `/shadcn-init`, `/shadcn-add`, `/shadcn-block`, `/shadcn-chart`, `/shadcn-theme`, `/shadcn-registry`.
- **Hook** reminds you in `*.tsx`/`components.json`/`globals.css` about `cn()`, theme tokens instead of hard-coded colours, a consistent variant (Radix/Base) and credential hygiene.
- **Utils** (`utils/`): `components.json`, `lib-utils.ts` (cn), `globals.css` (theme tokens), `registry.json` + `registry-item.example.json`.

## Agents

| Agent | Description |
|---|---|
| `shadcn-expert` | All-rounder: all components (code/props/examples), usage, Radix/Base variant, referral to the specialists. |
| `shadcn-setup` | Installation per framework, `components.json`, CLI, Tailwind v4 setup, cn util, dark mode provider, monorepo. |
| `shadcn-theming-expert` | Theme tokens (light/dark), colour palettes (oklch), Tailwind v4 `@theme`, radius, `--chart-*`. |
| `shadcn-blocks-expert` | Using/adapting blocks: sidebar/login/signup/dashboard, complete block code, lift mode. |
| `shadcn-charts-expert` | Recharts charts: ChartContainer/ChartConfig, all 70 variants, `--chart-*` theming. |
| `shadcn-registry-builder` | Custom registry: registry.json + registry-item.json, `shadcn build`, hosting, namespaces, MCP. |

## Commands

| Command | Description |
|---|---|
| `/shadcn-init` | Project setup: `init`, components.json, cn util, globals.css tokens, optional dark mode. |
| `/shadcn-add` | Add component(s) (`add`) + a runnable usage example (Radix/Base). |
| `/shadcn-block` | Insert a block (`add sidebar-07` …) + adaptation to branding/data. |
| `/shadcn-chart` | Create a chart: type/variant, ChartConfig + data + `--chart-*` colours. |
| `/shadcn-theme` | Create/change a theme: all tokens (light+dark), Tailwind v4 mapping, radius. |
| `/shadcn-registry` | Scaffold your own registry: registry.json + registry-item.json, build, consumer setup, MCP. |

## Hooks & Utils

| Artifact | Description |
|---|---|
| `shadcn-reminder.py` (PostToolUse) | Warns about template-string classes instead of `cn()`, mixed Radix/Base imports, hard-coded colour utilities; checks components.json aliases and `.dark` tokens. |
| `utils/` | `components.json`, `lib-utils.ts`, `globals.css`, `registry.json`, `registry-item.example.json` — ready-to-use templates. |

## Skills (8)

| Skill | Description |
|---|---|
| `shadcn-setup` | shadcn/ui installation and configuration: CLI, components.json, Tailwind v4, Next.js, Vite, Remix, monorepo, React 19, MCP. Use when the request names shadcn setup, init or components.json. |
| `shadcn-theming` | shadcn/ui theming: CSS variable tokens, colour palettes, light and dark mode, Tailwind v4 @theme, RTL and direction. Use when the request names shadcn theming, colors or dark mode. |
| `shadcn-layout` | shadcn/ui layout components: Card, Sidebar, Sheet, Drawer, Tabs, Accordion, Collapsible, Resizable, ScrollArea, Skeleton. Use when structuring a page with shadcn/ui. |
| `shadcn-forms` | shadcn/ui form components: Form, Field, Input, Select, Checkbox, Switch, Slider, Combobox, DatePicker, Calendar, Label. Use when building a form with shadcn/ui. |
| `shadcn-navigation` | shadcn/ui navigation components: NavigationMenu, Menubar, DropdownMenu, ContextMenu, Command, Breadcrumb, Pagination, Kbd. Use when building navigation or a command palette with shadcn/ui. |
| `shadcn-feedback` | shadcn/ui feedback components: Dialog, Alert, Popover, Tooltip, Toast, Sonner, Progress, Badge, Button. Use when showing state or confirming with shadcn/ui. |
| `shadcn-data` | shadcn/ui data display: Table, DataTable with TanStack Table, 70 Recharts chart examples, Carousel. Use when the request names a shadcn table, data table or chart. |
| `shadcn-blocks` | shadcn/ui blocks and custom registries: dashboard, login, signup and sidebar blocks, registry.json, registry-item.json, the registry API. Use when the request names a shadcn block or registry. |

### What lives where

| Topic | Skill |
|---|---|
| What shadcn/ui is, philosophy (not a package, copy and paste), Base UI vs. Radix UI | `shadcn-setup` |
| Installation for Next/Vite/Astro/Remix/Laravel/Gatsby/React Router/TanStack + manual | `shadcn-setup` |
| `components.json` — every field (style, rsc, tsx, tailwind.*, aliases.*, iconLibrary, registries) | `shadcn-setup` |
| CLI: `init`, `add`, `build`, `registry:*` — all flags; `shadcn create`, `shadcn apply` | `shadcn-setup` |
| Tailwind v4 setup: `@theme`, oklch, `tw-animate-css`, migration | `shadcn-setup` |
| Monorepo setup, React 19/RSC, package imports, JS instead of TS, Figma, legacy docs | `shadcn-setup` |
| shadcn MCP server: setup per client, `registries` in components.json, debugging | `shadcn-setup` |
| Theme token system (semantic CSS variables), convention, complete theme | `shadcn-theming` |
| All base colours + mapping onto theme variables (oklch/hsl) | `shadcn-theming` |
| Dark mode per framework (Next/Vite/Astro/Remix/TanStack Start) | `shadcn-theming` |
| Right-to-left support (Next/Vite/TanStack Start), Direction, Typography | `shadcn-theming` |
| Card, Sidebar (source, API, recipes, theming), Sheet, Drawer, Tabs, Accordion, Collapsible, Resizable, ScrollArea, Skeleton, Spinner, AspectRatio, Separator, Item, Empty | `shadcn-layout` |
| Field, Input, InputGroup, InputOTP, NativeSelect, Select, Checkbox, RadioGroup, Switch, Slider, Textarea, Toggle, ToggleGroup, Combobox, DatePicker, Calendar, Label; forms with react-hook-form, TanStack Form, Formisch, Next.js server actions + Zod | `shadcn-forms` |
| NavigationMenu, Menubar, DropdownMenu, ContextMenu, Command, Breadcrumb, Pagination, Kbd | `shadcn-navigation` |
| Dialog, AlertDialog, Alert, Popover, HoverCard, Tooltip, Toast (→ Sonner), Sonner, Progress, Badge, Button, ButtonGroup, Avatar | `shadcn-feedback` |
| Table, DataTable (TanStack Table), Carousel; chart system (ChartContainer/ChartConfig/ChartTooltip/ChartLegend, `chart.tsx` source) and all 70 example charts (area/bar/line/pie/radar/radial/tooltip) | `shadcn-data` |
| Blocks: what they are, installation, lift mode, open-in-v0, list of all 27; 16 sidebar blocks, 5 login + 5 signup blocks, dashboard-01 (complete app including chart/data table) | `shadcn-blocks` |
| Building and hosting your own registry (structure, build, serve, test and publish), `registry.json` schema, `registry-item.json` schema (all fields + `registry:*` types), registry API, index, namespaces, GitHub registries, auth, open-in-v0, FAQ | `shadcn-blocks` |
| Registry directory (public registries, namespaces), `shadcn create` project templates/presets, chronological feature history of shadcn/ui (changelog) | `shadcn-setup` |

## License & source

MIT — [zone1987](https://github.com/zone1987). Distilled from the official [shadcn/ui documentation](https://ui.shadcn.com) and the `shadcn-ui/ui` repository (`apps/v4`); all rights in the original documentation remain with its authors.
