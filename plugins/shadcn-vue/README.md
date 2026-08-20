# shadcn-vue

The **ultimate, comprehensive library for [shadcn-vue](https://www.shadcn-vue.com)** — the **Vue port of shadcn/ui** built on **[reka-ui](https://reka-ui.com)** (Tailwind v4, Vue 3 SFC). Like the original, shadcn-vue is not an npm package: the CLI **copies** components into your project and they are yours.

This library contains **everything**, distilled from `unovue/shadcn-vue` (`apps/v4`, docs + registry) and verified against the real source code:

- **All 64 components** — with **complete, unabridged Vue source code** (all `.vue` files + `index.ts`), props/slots/emits, **all demos** and the linked **reka-ui API**. Including the Vue-specific components: number-field, pin-input, range-calendar, stepper, tags-input.
- **All blocks** (16× sidebar, 5× login, 5× signup, 5× OTP, dashboard, products) — the complete code of every file.
- **All charts** (area/bar/line/pie/tooltip) — complete Vue code plus the chart system.
- **Setup**: installation for Vite, Nuxt, Astro, Laravel and manual; `components.json` (every field including `framework`/`composables`), CLI, Tailwind v4.
- **Theming**: all CSS variable tokens, oklch, dark mode (Vite/Nuxt/VitePress/Astro), typography.
- **Forms** (vee-validate + Zod **and** TanStack Form), **building your own registry** (registry.json + registry-item.json), the **MCP server**, changelog, legacy, Figma.
- **Bundled shadcn-vue MCP server** (`.mcp.json`).

Each skill keeps a lean `SKILL.md` and loads its depth from flat SCREAMING-CASE.md reference files next to it (installation/source/api/examples). **8 skills.**

Part of the marketplace **[claude-a-dev-team](../../README.md)**.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shadcn-vue@claude-a-dev-team
```

## MCP server (included)

The plugin ships the official **shadcn-vue MCP server** via `.mcp.json` (`npx shadcn-vue@latest mcp`). Claude can use it to search registries and install components through natural language. Details and client setup are in the skill `shadcn-vue-setup`.

```jsonc
// plugins/shadcn-vue/.mcp.json
{ "mcpServers": { "shadcn-vue": { "command": "npx", "args": ["shadcn-vue@latest", "mcp"] } } }
```

## Usage

- **Skills** load automatically (for example "shadcn-vue button", "shadcn vue add dialog", "shadcn vue sidebar block", "shadcn vue chart", "reka-ui", "components.json vue").
- **Agents:** `shadcn-vue-expert` (general), `shadcn-vue-setup`, `shadcn-vue-theming-expert`, `shadcn-vue-blocks-expert`, `shadcn-vue-charts-expert`, `shadcn-vue-registry-builder`.
- **Commands:** `/shadcn-vue-init`, `/shadcn-vue-add`, `/shadcn-vue-block`, `/shadcn-vue-chart`, `/shadcn-vue-theme`, `/shadcn-vue-registry`.
- **Hook** reminds you, in `*.vue`/`components.json`/CSS files, about `cn()`, theme tokens instead of hard-coded colors, `reka-ui` instead of `radix-vue`, and credential hygiene.
- **Utils** (`utils/`): `components.json`, `lib-utils.ts` (cn), `globals.css` (theme tokens), `registry.json` + `registry-item.example.json`.

## Agents

| Agent | Description |
|---|---|
| `shadcn-vue-expert` | All-rounder: every component (code/props/demos), usage, the reka-ui foundation, pointers to the specialists. |
| `shadcn-vue-setup` | Installation per framework, `components.json`, CLI, Tailwind v4, the cn util, dark mode. |
| `shadcn-vue-theming-expert` | Theme tokens (light/dark), oklch, Tailwind v4 `@theme`, radius, `--chart-*`, typography. |
| `shadcn-vue-blocks-expert` | Blocks: sidebar/login/signup/OTP/dashboard/products, complete code. |
| `shadcn-vue-charts-expert` | Charts: ChartContainer/Config, all variants, `--chart-*` theming. |
| `shadcn-vue-registry-builder` | Your own registry: registry.json + registry-item.json, `shadcn-vue build`, hosting, MCP. |

## Commands

| Command | Description |
|---|---|
| `/shadcn-vue-init` | Project setup: `init`, components.json, the cn util, globals.css tokens, optionally dark mode. |
| `/shadcn-vue-add` | Add one or more components (`add`) plus a runnable SFC usage example. |
| `/shadcn-vue-block` | Insert a block (`add sidebar-07` …) plus adaptation. |
| `/shadcn-vue-chart` | Create a chart: type/variant, data and `--chart-*` colors. |
| `/shadcn-vue-theme` | Create or change a theme: all tokens (light + dark), Tailwind v4 mapping. |
| `/shadcn-vue-registry` | Scaffold your own registry: registry.json + registry-item.json, build, consumer setup, MCP. |

## Hooks & utils

| Artifact | Description |
|---|---|
| `shadcn-vue-reminder.py` (PostToolUse) | Warns about template-string classes instead of `cn()`, hard-coded color utilities and the outdated `radix-vue`; checks components.json and the `.dark` tokens. |
| `utils/` | `components.json`, `lib-utils.ts`, `globals.css`, `registry.json`, `registry-item.example.json`. |

## Skills (8)

The 64 components, all blocks and all charts are grouped into eight domain skills by what they do. Each skill's `SKILL.md` maps to the reference files next to it, one per component (source, API, installation, examples).

| Skill | Description |
|---|---|
| `shadcn-vue-setup` | Installation and configuration: what shadcn-vue is, the reka-ui foundation and the distinction from shadcn/ui (React); installation for Vite/Nuxt/Astro/Laravel and manual; `components.json` — every field (style, typescript, tailwind.*, aliases.* including composables, framework, registries); the CLI (`init`, `add`, `build`, `registry` — all flags); the Tailwind v4 setup (`@theme`, oklch); JavaScript instead of TypeScript; Figma; the feature history/changelog; the legacy documentation; and the shadcn-vue MCP server (setup per client, `registries`, skills.sh, debugging). |
| `shadcn-vue-theming` | Theming: the theme token system (semantic CSS variables) and a complete theme, dark mode per framework (Vite/Nuxt/VitePress/Astro), and the typography classes (h1–h4, p, blockquote, list, table, code, lead, large, small, muted). |
| `shadcn-vue-forms` | Form components with Vue code, props/slots/emits and demos: form, field, input, input-group, input-otp, label, native-select, select, checkbox, radio-group, switch, toggle, toggle-group, slider, textarea, combobox, calendar, range-calendar, date-picker, number-field, pin-input, stepper, tags-input — plus the two validation integrations shadcn-vue documents: vee-validate with Zod, and TanStack Form. |
| `shadcn-vue-layout` | Layout components for structuring a page: card, sidebar, sheet, drawer, tabs, accordion, collapsible, resizable, scroll-area, separator, skeleton, spinner, aspect-ratio, empty, item. |
| `shadcn-vue-navigation` | Navigation components and command palettes: navigation-menu, menubar, dropdown-menu, context-menu, command, breadcrumb, pagination, kbd. |
| `shadcn-vue-feedback` | Components that report state or ask for confirmation: dialog, alert-dialog, alert, popover, hover-card, tooltip, toast, sonner, progress, badge, button, button-group. Dialog and AlertDialog differ in intent: AlertDialog interrupts and requires an answer. |
| `shadcn-vue-data` | Data display: table (markup), data-table (TanStack Table for sorting, filtering and pagination), carousel, and the chart system — ChartContainer/Config/Tooltip/Legend plus all example charts (area, bar, line, pie, tooltip variants) with complete Vue source code and `--chart-*` theming. |
| `shadcn-vue-blocks` | Blocks and your own registry: all blocks with complete code (16 sidebar, 5 login, 5 signup, 5 OTP, dashboard and products), plus building and hosting your own registry — registry.json and registry-item.json with their full schemas, all `registry:*` types, `shadcn-vue build`, examples and FAQ. |

### The 64 components covered

accordion · alert · alert-dialog · aspect-ratio · avatar · badge · breadcrumb · button · button-group · calendar · card · carousel · chart · checkbox · collapsible · combobox · command · context-menu · data-table · date-picker · dialog · drawer · dropdown-menu · empty · field · form · hover-card · input · input-group · input-otp · item · kbd · label · menubar · native-select · navigation-menu · number-field · pagination · pin-input · popover · progress · radio-group · range-calendar · resizable · scroll-area · select · separator · sheet · sidebar · skeleton · slider · sonner · spinner · stepper · switch · table · tabs · tags-input · textarea · toast · toggle · toggle-group · tooltip · typography

## License & author

MIT. Source: the official shadcn-vue documentation and `unovue/shadcn-vue` (apps/v4, reka-ui).
