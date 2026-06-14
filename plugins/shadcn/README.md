# shadcn

Die **ultimative, vollumfängliche Bibliothek für [shadcn/ui](https://ui.shadcn.com)** — die Copy-&-Paste-Komponentensammlung für React (Tailwind v4, **Radix-UI _und_ Base-UI**). shadcn/ui ist kein npm-Paket: Komponenten werden per CLI in dein Projekt **kopiert** und gehören dir.

Diese Bibliothek enthält **alles**, destilliert aus `shadcn-ui/ui` (`apps/v4`, Doku-MDX + Registry) und gegen den echten Quellcode verifiziert:

- **Alle 59 Komponenten** — je ein Skill mit **komplettem, ungekürztem Quellcode**, Props/Anatomy, **allen Examples** und den **Base-UI- vs. Radix-UI-Unterschieden**.
- **Alle 27 Blocks** (16× Sidebar, 5× Login, 5× Signup, Dashboard) — kompletter Code aller Block-Dateien.
- **Alle 70 Charts** (Area/Bar/Line/Pie/Radar/Radial/Tooltip) — kompletter Code + Chart-System (ChartContainer/ChartConfig).
- **Setup**: Installation für Next.js, Vite, Astro, Remix, Laravel, Gatsby, React Router, TanStack (Start/Router) + manuell; `components.json` (jedes Feld), CLI (jeder Befehl/Flag), Tailwind v4, Monorepo, React 19.
- **Theming**: alle CSS-Variablen-Tokens, Farbpaletten (oklch), Dark-Mode (5 Frameworks), eigenes Theme.
- **Forms** (react-hook-form/TanStack Form/Formisch/Next), **RTL**, **eigene Registry bauen** (registry.json + registry-item.json Schema, build, hosting, MCP), **Directory**, **shadcn create**, **Changelog**.
- **Mitgelieferter shadcn-MCP-Server** (`.mcp.json`) zum Live-Browsen/Installieren von Registry-Items.

Schlanke `SKILL.md`, Tiefe in mehreren strukturierten `references/`-Dateien (installation/source/api/examples/base-vs-radix). **96 Skills, 340+ Referenzdateien.**

Teil des Marketplace **[claude-a-dev-team](../../README.md)**.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shadcn@claude-a-dev-team
```

## MCP-Server (mitgeliefert)

Das Plugin bringt den offiziellen **shadcn-MCP-Server** über `.mcp.json` mit (`npx shadcn@latest mcp`). Claude kann damit Registries durchsuchen und Komponenten per natürlicher Sprache installieren. Konfiguriere zusätzliche Registries in `components.json` unter `registries`; Details + Client-Setup im Skill `shadcn-mcp`.

```jsonc
// plugins/shadcn/.mcp.json
{ "mcpServers": { "shadcn": { "command": "npx", "args": ["shadcn@latest", "mcp"] } } }
```

## Nutzung

- **Skills** laden automatisch (z.B. „shadcn button", „shadcn add dialog", „shadcn sidebar block", „shadcn area chart", „components.json", „shadcn theme").
- **Agents:** `shadcn-expert` (allgemein), `shadcn-setup` (Installation/CLI), `shadcn-theming-expert` (Farben/Dark-Mode), `shadcn-blocks-expert`, `shadcn-charts-expert`, `shadcn-registry-builder`.
- **Commands:** `/shadcn-init`, `/shadcn-add`, `/shadcn-block`, `/shadcn-chart`, `/shadcn-theme`, `/shadcn-registry`.
- **Hook** erinnert in `*.tsx`/`components.json`/`globals.css` an `cn()`, Theme-Tokens statt fester Farben, eine konsistente Variante (Radix/Base) und Credential-Hygiene.
- **Utils** (`utils/`): `components.json`, `lib-utils.ts` (cn), `globals.css` (Theme-Tokens), `registry.json` + `registry-item.example.json`.

## Agents

| Agent | Beschreibung |
|---|---|
| `shadcn-expert` | Allrounder: alle Komponenten (Code/Props/Examples), Usage, Variante Radix/Base, Verweis auf Spezialisten. |
| `shadcn-setup` | Installation je Framework, `components.json`, CLI, Tailwind-v4-Setup, cn-Util, Dark-Mode-Provider, Monorepo. |
| `shadcn-theming-expert` | Theme-Tokens (Light/Dark), Farbpaletten (oklch), Tailwind-v4 `@theme`, Radius, `--chart-*`. |
| `shadcn-blocks-expert` | Blocks einsetzen/anpassen: Sidebar/Login/Signup/Dashboard, kompletter Block-Code, Lift-Mode. |
| `shadcn-charts-expert` | Recharts-Charts: ChartContainer/ChartConfig, alle 70 Varianten, `--chart-*`-Theming. |
| `shadcn-registry-builder` | Eigene Registry: registry.json + registry-item.json, `shadcn build`, Hosting, Namespaces, MCP. |

## Commands

| Command | Beschreibung |
|---|---|
| `/shadcn-init` | Projekt-Setup: `init`, components.json, cn-Util, globals.css-Tokens, optional Dark-Mode. |
| `/shadcn-add` | Komponente(n) hinzufügen (`add`) + lauffähiges Usage-Beispiel (Radix/Base). |
| `/shadcn-block` | Block einfügen (`add sidebar-07` …) + Anpassung an Branding/Daten. |
| `/shadcn-chart` | Chart erstellen: Typ/Variante, ChartConfig + Daten + `--chart-*`-Farben. |
| `/shadcn-theme` | Theme erzeugen/ändern: alle Tokens (Light+Dark), Tailwind-v4-Mapping, Radius. |
| `/shadcn-registry` | Eigene Registry scaffolden: registry.json + registry-item.json, build, Consumer-Setup, MCP. |

## Hooks & Utils

| Artefakt | Beschreibung |
|---|---|
| `shadcn-reminder.py` (PostToolUse) | Warnt bei Template-String-Klassen statt `cn()`, gemischten Radix/Base-Imports, festen Farb-Utilities; prüft components.json-Aliase & `.dark`-Tokens. |
| `utils/` | `components.json`, `lib-utils.ts`, `globals.css`, `registry.json`, `registry-item.example.json` — einsatzfertige Vorlagen. |

## Skills

### Setup, CLI & Konfiguration

| Skill | Beschreibung |
|---|---|
| `shadcn-overview` | Was ist shadcn/ui, Philosophie (kein Paket, Copy-&-Paste), Base-UI vs. Radix-UI. |
| `shadcn-installation` | Installation für Next/Vite/Astro/Remix/Laravel/Gatsby/React-Router/TanStack + manuell (je `references/<fw>.md`). |
| `shadcn-components-json` | `components.json` — jedes Feld (style, rsc, tsx, tailwind.*, aliases.*, iconLibrary, registries). |
| `shadcn-cli` | CLI: `init`, `add`, `build`, `registry:*` — alle Flags. |
| `shadcn-tailwind-v4` | Tailwind-v4-Setup: `@theme`, oklch, `tw-animate-css`, Migration. |
| `shadcn-monorepo` · `shadcn-react-19` · `shadcn-package-imports` · `shadcn-javascript` · `shadcn-figma` · `shadcn-legacy` | Monorepo-Setup, React-19/RSC, Package-Imports, JS-statt-TS, Figma, Legacy-Doku. |

### Theming & Dark-Mode

| Skill | Beschreibung |
|---|---|
| `shadcn-theming` | Theme-Token-System (semantische CSS-Variablen), Konvention, komplettes Theme. |
| `shadcn-colors` | Alle Basisfarben + Mapping auf Theme-Variablen (oklch/hsl). |
| `shadcn-dark-mode` | Dark-Mode je Framework (Next/Vite/Astro/Remix/TanStack Start). |

### Komponenten (59 — je Skill: Code + Props + Examples + Base/Radix)

| Skills | Komponenten |
|---|---|
| `shadcn-accordion` · `shadcn-alert` · `shadcn-alert-dialog` · `shadcn-aspect-ratio` · `shadcn-avatar` · `shadcn-badge` · `shadcn-breadcrumb` · `shadcn-button` · `shadcn-button-group` · `shadcn-calendar` | Accordion, Alert, Alert-Dialog, Aspect-Ratio, Avatar, Badge, Breadcrumb, Button, Button-Group, Calendar |
| `shadcn-card` · `shadcn-carousel` · `shadcn-chart` · `shadcn-checkbox` · `shadcn-collapsible` · `shadcn-combobox` · `shadcn-command` · `shadcn-context-menu` · `shadcn-data-table` · `shadcn-date-picker` | Card, Carousel, Chart, Checkbox, Collapsible, Combobox, Command, Context-Menu, Data-Table, Date-Picker |
| `shadcn-dialog` · `shadcn-direction` · `shadcn-drawer` · `shadcn-dropdown-menu` · `shadcn-empty` · `shadcn-field` · `shadcn-hover-card` · `shadcn-input` · `shadcn-input-group` · `shadcn-input-otp` | Dialog, Direction, Drawer, Dropdown-Menu, Empty, Field, Hover-Card, Input, Input-Group, Input-OTP |
| `shadcn-item` · `shadcn-kbd` · `shadcn-label` · `shadcn-menubar` · `shadcn-native-select` · `shadcn-navigation-menu` · `shadcn-pagination` · `shadcn-popover` · `shadcn-progress` · `shadcn-radio-group` | Item, Kbd, Label, Menubar, Native-Select, Navigation-Menu, Pagination, Popover, Progress, Radio-Group |
| `shadcn-resizable` · `shadcn-scroll-area` · `shadcn-select` · `shadcn-separator` · `shadcn-sheet` · `shadcn-sidebar` · `shadcn-skeleton` · `shadcn-slider` · `shadcn-sonner` · `shadcn-spinner` | Resizable, Scroll-Area, Select, Separator, Sheet, Sidebar, Skeleton, Slider, Sonner, Spinner |
| `shadcn-switch` · `shadcn-table` · `shadcn-tabs` · `shadcn-textarea` · `shadcn-toast` · `shadcn-toggle` · `shadcn-toggle-group` · `shadcn-tooltip` · `shadcn-typography` | Switch, Table, Tabs, Textarea, Toast (→ Sonner), Toggle, Toggle-Group, Tooltip, Typography |

### Blocks

| Skill | Beschreibung |
|---|---|
| `shadcn-blocks-overview` | Was sind Blocks, Installation, Lift-Mode, Open-in-v0, Liste aller 27. |
| `shadcn-blocks-sidebar` | 16 Sidebar-Blocks (kompletter Code aller Dateien). |
| `shadcn-blocks-login` · `shadcn-blocks-signup` | 5 Login- + 5 Signup-Blocks. |
| `shadcn-blocks-dashboard` | dashboard-01 (komplette App inkl. Chart/Data-Table). |

### Charts

| Skill | Beschreibung |
|---|---|
| `shadcn-charts-overview` | Chart-System: ChartContainer/ChartConfig/ChartTooltip/ChartLegend, `--chart-*`-Theming, `chart.tsx`-Quellcode. |
| `shadcn-charts-area` · `-bar` · `-line` · `-pie` · `-radar` · `-radial` · `-tooltip` | Alle Beispiel-Charts je Typ mit komplettem Code (70 gesamt). |

### Registry, Forms, RTL & mehr

| Skill | Beschreibung |
|---|---|
| `shadcn-registry` | Eigene Registry bauen & hosten (Struktur, Build, Verteilung). |
| `shadcn-registry-json` | Schema von `registry.json` (alle Felder). |
| `shadcn-registry-item-json` | Schema von `registry-item.json` (alle Felder + `registry:*`-Typen). |
| `shadcn-registry-api` | Registry-API, Index, Namespaces, GitHub-Registries, Auth, Open-in-v0, FAQ. |
| `shadcn-mcp` | shadcn-MCP-Server: Setup je Client, `registries` in components.json, Debugging. |
| `shadcn-forms` | Formulare mit react-hook-form, TanStack Form, Formisch, Next.js + Zod (Field/Form). |
| `shadcn-rtl` | Right-to-Left-Support (Next/Vite/TanStack Start). |
| `shadcn-directory` | Registry-Directory (öffentliche Registries, Namespaces). |
| `shadcn-create` | `shadcn create` — Projekt-Templates/Presets, `shadcn apply`. |
| `shadcn-changelog` | Chronologische Feature-Historie von shadcn/ui. |

## Lizenz & Autor

proprietary — Andreas Gerhardt, A-Dev-Team. Quelle: offizielle shadcn/ui-Doku & `shadcn-ui/ui` (apps/v4).
