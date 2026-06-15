# shadcn-vue

Die **ultimative, vollumfängliche Bibliothek für [shadcn-vue](https://www.shadcn-vue.com)** — den **Vue-Port von shadcn/ui** auf Basis von **[reka-ui](https://reka-ui.com)** (Tailwind v4, Vue-3-SFC). Wie das Original ist shadcn-vue kein npm-Paket: Komponenten werden per CLI in dein Projekt **kopiert** und gehören dir.

Diese Bibliothek enthält **alles**, destilliert aus `unovue/shadcn-vue` (`apps/v4`, Doku + Registry) und gegen den echten Quellcode verifiziert:

- **Alle 64 Komponenten** — je ein Skill mit **komplettem, ungekürztem Vue-Quellcode** (alle `.vue` + `index.ts`), Props/Slots/Emits, **allen Demos** und der verlinkten **reka-ui-API**. Inkl. Vue-spezifischer Komponenten: number-field, pin-input, range-calendar, stepper, tags-input.
- **Alle Blocks** (16× Sidebar, 5× Login, 5× Signup, 5× OTP, Dashboard, Products) — kompletter Code aller Dateien.
- **Alle Charts** (Area/Bar/Line/Pie/Tooltip) — kompletter Vue-Code + Chart-System.
- **Setup**: Installation für Vite, Nuxt, Astro, Laravel + manuell; `components.json` (jedes Feld inkl. `framework`/`composables`), CLI, Tailwind v4.
- **Theming**: alle CSS-Variablen-Tokens, oklch, Dark-Mode (Vite/Nuxt/VitePress/Astro), Typografie.
- **Forms** (vee-validate + Zod **und** TanStack Form), **eigene Registry bauen** (registry.json + registry-item.json), **MCP-Server**, Changelog, Legacy, Figma.
- **Mitgelieferter shadcn-vue-MCP-Server** (`.mcp.json`).

Schlanke `SKILL.md`, Tiefe in strukturierten `references/`-Dateien (installation/source/api/examples). **93 Skills.**

Teil des Marketplace **[claude-a-dev-team](../../README.md)**.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shadcn-vue@claude-a-dev-team
```

## MCP-Server (mitgeliefert)

Das Plugin bringt den offiziellen **shadcn-vue-MCP-Server** über `.mcp.json` mit (`npx shadcn-vue@latest mcp`). Claude kann damit Registries durchsuchen und Komponenten per natürlicher Sprache installieren. Details + Client-Setup im Skill `shadcn-vue-mcp`.

```jsonc
// plugins/shadcn-vue/.mcp.json
{ "mcpServers": { "shadcn-vue": { "command": "npx", "args": ["shadcn-vue@latest", "mcp"] } } }
```

## Nutzung

- **Skills** laden automatisch (z.B. „shadcn-vue button", „shadcn vue add dialog", „shadcn vue sidebar block", „shadcn vue chart", „reka-ui", „components.json vue").
- **Agents:** `shadcn-vue-expert` (allgemein), `shadcn-vue-setup`, `shadcn-vue-theming-expert`, `shadcn-vue-blocks-expert`, `shadcn-vue-charts-expert`, `shadcn-vue-registry-builder`.
- **Commands:** `/shadcn-vue-init`, `/shadcn-vue-add`, `/shadcn-vue-block`, `/shadcn-vue-chart`, `/shadcn-vue-theme`, `/shadcn-vue-registry`.
- **Hook** erinnert in `*.vue`/`components.json`/CSS an `cn()`, Theme-Tokens statt fester Farben, `reka-ui` statt `radix-vue` und Credential-Hygiene.
- **Utils** (`utils/`): `components.json`, `lib-utils.ts` (cn), `globals.css` (Theme-Tokens), `registry.json` + `registry-item.example.json`.

## Agents

| Agent | Beschreibung |
|---|---|
| `shadcn-vue-expert` | Allrounder: alle Komponenten (Code/Props/Demos), Usage, reka-ui-Basis, Verweis auf Spezialisten. |
| `shadcn-vue-setup` | Installation je Framework, `components.json`, CLI, Tailwind-v4, cn-Util, Dark-Mode. |
| `shadcn-vue-theming-expert` | Theme-Tokens (Light/Dark), oklch, Tailwind-v4 `@theme`, Radius, `--chart-*`, Typografie. |
| `shadcn-vue-blocks-expert` | Blocks: Sidebar/Login/Signup/OTP/Dashboard/Products, kompletter Code. |
| `shadcn-vue-charts-expert` | Charts: ChartContainer/Config, alle Varianten, `--chart-*`-Theming. |
| `shadcn-vue-registry-builder` | Eigene Registry: registry.json + registry-item.json, `shadcn-vue build`, Hosting, MCP. |

## Commands

| Command | Beschreibung |
|---|---|
| `/shadcn-vue-init` | Projekt-Setup: `init`, components.json, cn-Util, globals.css-Tokens, optional Dark-Mode. |
| `/shadcn-vue-add` | Komponente(n) hinzufügen (`add`) + lauffähiges SFC-Usage-Beispiel. |
| `/shadcn-vue-block` | Block einfügen (`add sidebar-07` …) + Anpassung. |
| `/shadcn-vue-chart` | Chart erstellen: Typ/Variante, Daten + `--chart-*`-Farben. |
| `/shadcn-vue-theme` | Theme erzeugen/ändern: alle Tokens (Light+Dark), Tailwind-v4-Mapping. |
| `/shadcn-vue-registry` | Eigene Registry scaffolden: registry.json + registry-item.json, build, Consumer-Setup, MCP. |

## Hooks & Utils

| Artefakt | Beschreibung |
|---|---|
| `shadcn-vue-reminder.py` (PostToolUse) | Warnt bei Template-String-Klassen statt `cn()`, festen Farb-Utilities, veraltetem `radix-vue`; prüft components.json & `.dark`-Tokens. |
| `utils/` | `components.json`, `lib-utils.ts`, `globals.css`, `registry.json`, `registry-item.example.json`. |

## Skills

### Setup, CLI & Konfiguration

| Skill | Beschreibung |
|---|---|
| `shadcn-vue-overview` | Was ist shadcn-vue, reka-ui-Basis, Abgrenzung zu shadcn/ui (React). |
| `shadcn-vue-installation` | Installation für Vite/Nuxt/Astro/Laravel + manuell (je `references/<fw>.md`). |
| `shadcn-vue-components-json` | `components.json` — jedes Feld (style, typescript, tailwind.*, aliases.* inkl. composables, framework, registries). |
| `shadcn-vue-cli` | CLI: `init`, `add`, `build`, `registry` — alle Flags. |
| `shadcn-vue-tailwind-v4` | Tailwind-v4-Setup: `@theme`, oklch. |
| `shadcn-vue-javascript` · `shadcn-vue-figma` · `shadcn-vue-changelog` · `shadcn-vue-legacy` | JS-statt-TS, Figma, Feature-Historie, Legacy-Doku. |

### Theming & Dark-Mode

| Skill | Beschreibung |
|---|---|
| `shadcn-vue-theming` | Theme-Token-System (semantische CSS-Variablen), komplettes Theme. |
| `shadcn-vue-dark-mode` | Dark-Mode je Framework (Vite/Nuxt/VitePress/Astro). |
| `shadcn-vue-typography` | Text-Stil-Klassen (h1–h4, p, blockquote, list, table, code, lead, large, small, muted). |

### Komponenten (64 — je Skill: Vue-Code + Props/Slots/Emits + Demos)

accordion · alert · alert-dialog · aspect-ratio · avatar · badge · breadcrumb · button · button-group · calendar · card · carousel · chart · checkbox · collapsible · combobox · command · context-menu · data-table · date-picker · dialog · drawer · dropdown-menu · empty · field · form · hover-card · input · input-group · input-otp · item · kbd · label · menubar · native-select · navigation-menu · number-field · pagination · pin-input · popover · progress · radio-group · range-calendar · resizable · scroll-area · select · separator · sheet · sidebar · skeleton · slider · sonner · spinner · stepper · switch · table · tabs · tags-input · textarea · toast · toggle · toggle-group · tooltip · typography

(jeweils als Skill `shadcn-vue-<komponente>`)

### Blocks, Charts, Forms, Registry & MCP

| Skill | Beschreibung |
|---|---|
| `shadcn-vue-blocks-overview` · `-sidebar` · `-login` · `-signup` · `-otp` · `-dashboard` | Alle Blocks mit komplettem Code (Sidebar 16, Login 5, Signup 5, OTP 5, Dashboard + Products). |
| `shadcn-vue-charts-overview` · `-area` · `-bar` · `-line` · `-pie` · `-tooltip` | Chart-System + alle Beispiel-Charts mit komplettem Vue-Code. |
| `shadcn-vue-forms` | Formulare mit vee-validate + Zod und TanStack Form (Field/Form). |
| `shadcn-vue-registry` · `-registry-json` · `-registry-item-json` · `-registry-examples` | Eigene Registry bauen + vollständige Schemas + Beispiele/FAQ. |
| `shadcn-vue-mcp` | shadcn-vue-MCP-Server: Setup je Client, `registries`, skills.sh, Debugging. |

## Lizenz & Autor

proprietary — Andreas Gerhardt, A-Dev-Team. Quelle: offizielle shadcn-vue-Doku & `unovue/shadcn-vue` (apps/v4, reka-ui).
