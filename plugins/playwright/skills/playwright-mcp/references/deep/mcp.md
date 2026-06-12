# Playwright MCP-Server

## Was ist Playwright MCP?

Playwright MCP ist ein Model Context Protocol-Server fuer Browser-Automation durch LLMs.
Statt visueller Verarbeitung nutzt er strukturierte **Accessibility-Snapshots** (ARIA-Baum),
die deterministische Interaktion ohne Vision-Modell ermoeglichen.

### Architektur-Kernpunkte

- **Snapshot-basiert**: Accessibility-Tree mit eindeutigen `ref`-IDs fuer interaktive Elemente
- **Token-effizient**: ~200-400 Token/Snapshot vs. 3.000-5.000 Token fuer Screenshots
- **Determinismus**: Gleiche Struktur = gleiche Interaktion
- **Headed by default**: Browser wird sichtbar gestartet fuer Echtzeit-Beobachtung

---

## Installation

### Voraussetzungen

- Node.js 20 oder neuer
- Kompatibler MCP-Client

### Standard-Konfiguration (alle Clients)

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Der Browser wird **beim ersten Aufruf automatisch heruntergeladen**.

---

## Client-spezifische Installation

### VS Code

```bash
# CLI-Installation
code --add-mcp '{"name":"playwright","command":"npx","args":["@playwright/mcp@latest"]}'
```

Oder: VS Code Insiders:
```bash
code-insiders --add-mcp '{"name":"playwright","command":"npx","args":["@playwright/mcp@latest"]}'
```

Integriert sich als GitHub Copilot-Agent in VS Code.

### Claude Code

```bash
claude mcp add playwright npx @playwright/mcp@latest
```

Verfuegbar in der naechsten Claude-Code-Session.

### Cursor

Einstellungen -> MCP -> "Add new MCP Server":
- Name: `playwright`
- Type: `command`
- Command: `npx @playwright/mcp@latest`

### Windsurf / Cline / Goose / Kiro / Codex / Copilot CLI

Standard-MCP-Konfiguration (siehe Client-Dokumentation).

---

## Konfigurationsoptionen

### CLI-Flags

```bash
# Headless-Modus
npx @playwright/mcp@latest --headless

# Browser waehlen: chrome (Standard), firefox, webkit, msedge
npx @playwright/mcp@latest --browser=firefox

# HTTP-Transport (Standalone-Server)
npx @playwright/mcp@latest --port 8931

# Capabilities aktivieren
npx @playwright/mcp@latest --caps=vision,pdf,devtools

# Alle Capabilities
npx @playwright/mcp@latest --caps=core,network,storage,testing,vision,pdf,devtools

# Isolierter Modus (kein State zwischen Sessions)
npx @playwright/mcp@latest --isolated

# Browser-Extension-Modus
npx @playwright/mcp@latest --extension

# Benutzerprofil-Verzeichnis
npx @playwright/mcp@latest --user-data-dir=/path/to/profile

# Session-State laden
npx @playwright/mcp@latest --storage-state=./auth-state.json

# Gemeinsamer Context fuer alle Clients
npx @playwright/mcp@latest --shared-browser-context

# Proxy
npx @playwright/mcp@latest --proxy-server=http://myproxy:3128

# Proxy-Bypass
npx @playwright/mcp@latest --proxy-bypass=localhost,*.internal.com

# Viewport
npx @playwright/mcp@latest --viewport=1280x720

# Device-Emulation
npx @playwright/mcp@latest --device="iPhone 15"
```

### HTTP-Transport-Konfiguration

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--port", "8931",
        "--host", "0.0.0.0"
      ]
    }
  }
}
```

Client-Endpunkt: `http://localhost:8931/mcp`

### Vollstaendige Optionen-Tabelle

| Option | Typ | Default | Beschreibung |
|--------|-----|---------|--------------|
| `--headless` | flag | headed | Browser ohne UI starten |
| `--browser` | string | `chrome` | Browser-Engine: `chrome`/`firefox`/`webkit`/`msedge` |
| `--device` | string | — | Device-Emulation (z.B. `"iPhone 15"`) |
| `--viewport` | string | — | Viewport-Groesse (z.B. `1280x720`) |
| `--port` | number | — | HTTP-Transport-Port |
| `--host` | string | `localhost` | Bind-Adresse (`0.0.0.0` fuer Container) |
| `--caps` | string | `core` | Komma-getrennte Capabilities |
| `--isolated` | flag | — | Kein persistenter State zwischen Sessions |
| `--extension` | flag | — | Browser-Extension-Modus |
| `--user-data-dir` | string | Plattform-Cache | Profil-Verzeichnis |
| `--storage-state` | string | — | Session-State-Datei laden |
| `--proxy-server` | string | — | Proxy-URL |
| `--proxy-bypass` | string | — | Komma-getrennte Bypass-Hosts |
| `--save-session` | flag | — | Session automatisch aufzeichnen |
| `--config` | string | — | Pfad zur Konfigurationsdatei |
| `--shared-browser-context` | flag | — | Einzelner Context fuer alle Clients |
| `--allow-unrestricted-file-access` | flag | — | Datei-Uploads ohne Workspace-Beschraenkung |

### Timeout-Konfiguration

| Timeout | Default | Beschreibung |
|---------|---------|--------------|
| Action | 5.000 ms | Einzelne Interaktion |
| Navigation | 60.000 ms | Seitennavigation |
| Expect | 5.000 ms | Assertions |

---

## Capabilities

### Uebersicht

| Capability | Stets aktiv | Tools | Beschreibung |
|-----------|------------|-------|--------------|
| `core` | Ja | 15+ | Basis-Browser-Automation |
| `core-navigation` | Nein | — | Nur Navigation-Subset |
| `core-tabs` | Nein | — | Nur Tab-Management |
| `core-input` | Nein | — | Nur Input-Operationen |
| `network` | Nein | 4 | Request-Mocking, Online/Offline |
| `storage` | Nein | 15+ | Cookies, localStorage, State |
| `testing` | Nein | 5 | Assertions + Locator-Generierung |
| `vision` | Nein | 6 | Koordinaten-basierte Maus-Tools |
| `pdf` | Nein | 1 | PDF-Export |
| `devtools` | Nein | 4 | Tracing, Video, Debugging |
| `config` | Nein | 1 | Konfiguration abrufen |

### Aktivierungsoptionen

```bash
# CLI-Flag
npx @playwright/mcp@latest --caps=vision,pdf,devtools

# Umgebungsvariable
PLAYWRIGHT_MCP_CAPS=vision,devtools npx @playwright/mcp@latest

# In MCP-Konfiguration
{
  "args": ["@playwright/mcp@latest", "--caps=storage,testing,devtools"]
}
```

### Designprinzip

Nur benoettigte Capabilities aktivieren, um:
- Token-Kosten zu reduzieren
- Halluzinierte Tool-Aufrufe zu minimieren
- Antwortzeiten zu beschleunigen

---

## Profil-Modi

### Persistent (Standard)

Login-State, Cookies und localStorage werden zwischen Sessions beibehalten.

Plattform-spezifische Speicherorte:
- macOS: `~/Library/Caches/ms-playwright/mcp-{channel}-profile`
- Linux: `~/.cache/ms-playwright/mcp-{channel}-profile`
- Windows: `%LOCALAPPDATA%\ms-playwright\mcp-{channel}-profile`

Ueberschreiben: `--user-data-dir=/pfad/zum/profil`

### Isoliert

Jede Session startet ohne gespeicherten State.

```json
{
  "args": ["@playwright/mcp@latest", "--isolated"]
}
```

Initiale Credentials laden: `--storage-state=./auth-state.json`

### Browser-Extension-Modus

Verbindet sich mit bestehenden Browser-Tabs statt neue zu starten.

```json
{
  "args": ["@playwright/mcp@latest", "--extension"]
}
```

Anwendungsfaelle:
- SSO/2FA: Authentifizierte Session wiederverwenden
- Browser-Extensions: Seiten mit installierten Add-ons automatisieren
- Bestehende Tabs: Bereits geoeffnete Seiten automatisieren

---

## Accessibility-Snapshots

### Funktionsprinzip

Jede Interaktion gibt einen strukturierten ARIA-Baum mit `ref`-IDs zurueck:

```
- heading "TodoMVC" [level=1]
- textbox "New todo" [ref=e5]
- list
  - listitem
    - checkbox "Buy groceries" [ref=e8]
    - text "Buy groceries"
  - listitem
    - checkbox "Read Playwright docs" [ref=e10] [checked]
```

### Ref-Eigenschaften

| Eigenschaft | Wert |
|-------------|------|
| Format | `e` gefolgt von Zahl (z.B. `e5`, `e203`) |
| Eindeutigkeit | Pro Snapshot |
| Lebensdauer | Bis zur naechsten Navigation oder DOM-Aenderung |
| Vergabe | Nur interaktive Elemente erhalten refs |

### Workflow-Muster

```
1. browser_navigate -> Snapshot zurueck
2. LLM liest Snapshot, identifiziert ref
3. browser_type { ref: "e5", text: "..." }
4. Naechster Snapshot automatisch
5. Refs neu einlesen nach Navigation
```

### Snapshot + Screenshot kombinieren

Fuer visuell-intensive Interfaces: Strukturierten Snapshot fuer Interaktion + Screenshot fuer Layout-Verstaendnis kombinieren.

---

## Vision-Modus

Ergaenzt snapshots um koordinaten-basierte Tools fuer Elemente ohne ARIA-Unterstuetzung.

### Aktivierung

```json
{
  "args": ["@playwright/mcp@latest", "--caps=vision"]
}
```

### Anwendungsfaelle

| Szenario | Begruendung |
|----------|-------------|
| Canvas/WebGL | Keine ARIA-Elemente |
| Karten-Interaktion | Pan/Zoom benoetigt Koordinaten |
| Bild-Editoren | Zeichen-Operationen |
| Charts | Datenpunkte anwaehlen |
| Custom-Widgets ohne ARIA | Kein Accessibility-Tree |

### Empfehlung

Fuer normale Web-Anwendungen: **Snapshot-basierter Ansatz bevorzugen** (zuverlaessiger und token-effizienter). Vision als Fallback nutzen.

---

## Konfigurationsdatei (config.json)

```json
{
  "browser": {
    "browserName": "chromium",
    "headless": false,
    "launchOptions": {
      "slowMo": 0
    },
    "contextOptions": {
      "viewport": { "width": 1280, "height": 720 },
      "locale": "de-DE"
    }
  },
  "capabilities": ["core", "network", "storage"],
  "network": {
    "allowedOrigins": ["https://example.com"],
    "blockedOrigins": []
  },
  "timeout": {
    "action": 5000,
    "navigation": 60000
  }
}
```

Verwenden: `npx @playwright/mcp@latest --config path/to/config.json`

Schema: https://github.com/microsoft/playwright-mcp/blob/main/config.d.ts

---

## Quellen

- https://playwright.dev/docs/getting-started-mcp
- https://playwright.dev/mcp/introduction
- https://playwright.dev/mcp/installation
- https://playwright.dev/mcp/capabilities
- https://playwright.dev/mcp/snapshots
- https://playwright.dev/mcp/vision-mode
- https://playwright.dev/mcp/configuration/options
- https://playwright.dev/mcp/configuration/user-profile
- https://playwright.dev/mcp/configuration/browser-extension
