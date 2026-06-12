# Playwright Agent CLI — Einfuehrung, Quick-Start, Installation, Skills

## Was ist die Playwright Agent CLI?

Eine Kommandozeilen-Schnittstelle fuer Browser-Automatisierung, die speziell fuer Coding-Agents
entworfen wurde. Die CLI bietet token-effiziente Befehle und installierbare Skills, damit Agents
Browser-Automatisierung und grosse Codebasen innerhalb begrenzter Context-Windows ausbalancieren
koennen.

### Kernmerkmale

| Merkmal | Beschreibung |
|---------|-------------|
| Token-effizient | Kompakte CLI-Ausgabe vermeidet das Laden grosser Tool-Schemas in den Modell-Context |
| Skill-basiert | Agents entdecken Faehigkeiten ueber installierbare Skills |
| Daemon-Architektur | Persistenter Browser-Prozess eliminiert Startkosten je Befehl |
| Ref-basiert | Accessibility-Snapshots mit Element-Refs fuer deterministische Interaktion |
| Cross-Browser | Chrome, Firefox, WebKit und Edge |
| Sessions | Mehrere isolierte Browser-Instanzen mit eigenem State |

### Playwright CLI vs. MCP

| Aspekt | Playwright CLI | MCP |
|--------|---------------|-----|
| Beste fuer | Coding-Agents mit grossen Codebasen | Spezialisierte Agentic-Loops, explorative Automatisierung |
| Funktionsweise | Agent fuehrt Shell-Befehle aus | LLM ruft MCP-Tools mit strukturierten Parametern auf |
| Token-Kosten | Niedriger — kompakte Ausgabe, Skills on Demand | Hoeher — Tool-Schemas + Snapshots im Context |
| Standard-Modus | Headless | Headed |
| Setup | `npm install -g @playwright/cli` | JSON-Config im MCP-Client |

---

## Quick-Start

### Typischer Workflow

```bash
playwright-cli open https://demo.playwright.dev/todomvc --headed
playwright-cli type "Buy groceries"
playwright-cli press Enter
playwright-cli type "Water flowers"
playwright-cli press Enter
playwright-cli check e21
playwright-cli screenshot
```

### Beispielausgabe nach einem Befehl

```
### Page
- Page URL: https://demo.playwright.dev/todomvc/#/
- Page Title: React - TodoMVC

### Snapshot
[Snapshot](.playwright-cli/page-2026-02-14T19-22-42-679Z.yml)
```

Der Snapshot enthaelt den Accessibility-Tree mit Element-Refs (z. B. `e5`, `e21`) fuer
deterministische Folgebefehle.

### Kernablauf

1. URL oeffnen via `playwright-cli open <url>`
2. Snapshot liefert Accessibility-Tree mit Element-Refs
3. Interagieren mit Refs: `click`, `type`, `fill`
4. Erneuter Snapshot liefert aktualisierten State mit neuen Refs

---

## Installation

### Voraussetzungen

- Node.js 20 oder neuer
- Ein Coding-Agent (Claude Code, GitHub Copilot oder aequivalent)

### Globale Installation

```bash
npm install -g @playwright/cli@latest
playwright-cli --help
```

### Lokale Nutzung (ohne globale Installation)

```bash
npx playwright-cli --help
```

### Browser installieren

Der erste Aufruf laedt den Standard-Browser automatisch herunter. Fuer explizite Installation:

```bash
playwright-cli install-browser               # Standard (Chromium)
playwright-cli install-browser firefox       # spezifischer Browser
playwright-cli install-browser --with-deps   # inkl. System-Abhaengigkeiten (Linux)
```

#### install-browser Flags

| Flag | Beschreibung |
|------|-------------|
| `--with-deps` | System-Abhaengigkeiten installieren (Linux) |
| `--dry-run` | Vorschau: was wuerde installiert |
| `--list` | Verfuegbare Browser aller Installationen auflisten |
| `--force` | Reinstallieren, auch wenn bereits vorhanden |
| `--only-shell` | Nur Chromium Headless Shell installieren |
| `--no-shell` | Chromium Headless Shell ueberspringen |

---

## Skills

### Was Skills leisten

Skills lehren Coding-Agents die effektive Nutzung von `playwright-cli` durch strukturierte
Referenz-Dokumentation, die Agents entdecken und nutzen koennen.

Die Installation umfasst detaillierte Referenz-Guides fuer:

- Playwright-Tests ausfuehren und debuggen
- Request-Mocking (Netzwerk-Requests abfangen/mocken)
- Playwright-Code ausfuehren (beliebige Skripte)
- Browser-Session-Management
- Storage-State-Management (Cookies, localStorage)
- Test-Generierung aus Interaktionen
- Tracing (Ausfuehrungs-Traces aufzeichnen/inspizieren)
- Video-Aufnahme von Browser-Sessions
- Element-Attribute inspizieren (jenseits von Snapshots)

### Skills installieren

```bash
playwright-cli install --skills
```

### Unterstuetzte Agents

- Claude Code
- GitHub Copilot
- Cursor
- Jeder Coding-Agent mit Unterstuetzung fuer lokal installierte Skills

### Skills-loser Betrieb

Alternativ kann der Agent Befehle selbst entdecken:

```bash
playwright-cli --help
```

### Session-Voreinstellung per Umgebungsvariable

```bash
PLAYWRIGHT_CLI_SESSION=todo-app claude .
```

---

## Alle Befehle — Uebersicht

### Kern-Befehle
`open [url]`, `close`, `click <ref>`, `dblclick <ref>`, `fill <ref> <text>`, `type <text>`,
`select <ref> <val>`, `check <ref>`, `uncheck <ref>`, `hover <ref>`, `drag <start> <end>`,
`upload <file>`, `snapshot`, `screenshot [ref]`, `pdf`, `eval <func> [ref]`, `resize <w> <h>`,
`dialog-accept [prompt]`, `dialog-dismiss`

### Navigation
`go-back`, `go-forward`, `reload`

### Tastatur & Maus
`press <key>`, `keydown <key>`, `keyup <key>`, `mousemove <x> <y>`, `mousedown [btn]`,
`mouseup [btn]`, `mousewheel <dx> <dy>`

### Tabs
`tab-list`, `tab-new [url]`, `tab-select <idx>`, `tab-close [idx]`

### Storage
`state-save [file]`, `state-load <file>`, `cookie-list`, `cookie-get <name>`,
`cookie-set <name> <val>`, `cookie-delete <name>`, `cookie-clear`, `localstorage-list`,
`localstorage-get <key>`, `localstorage-set <k> <v>`, `localstorage-delete <key>`,
`localstorage-clear`, `sessionstorage-list`, `sessionstorage-get <key>`,
`sessionstorage-set <k> <v>`, `sessionstorage-delete <k>`, `sessionstorage-clear`

### Netzwerk
`network`, `route <pattern> [opts]`, `route-list`, `unroute [pattern]`

### DevTools
`console [min-level]`, `run-code <code>`, `tracing-start`, `tracing-stop`,
`video-start [file]`, `video-chapter <title>`, `video-stop`, `show`

### Sessions
`-s=<name> <cmd>`, `list`, `close-all`, `kill-all`, `delete-data`

---

Quelle: https://playwright.dev/agent-cli/introduction · https://playwright.dev/agent-cli/quick-start · https://playwright.dev/agent-cli/installation · https://playwright.dev/agent-cli/skills
