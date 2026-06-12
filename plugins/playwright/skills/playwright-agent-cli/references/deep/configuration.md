# Playwright Agent CLI — Konfiguration

## Headed / Headless-Modus

Standard ist Headless. Browser-Fenster anzeigen:

```bash
playwright-cli open https://playwright.dev --headed
```

## Browser-Auswahl

```bash
playwright-cli open --browser=chrome     # Google Chrome (Standard)
playwright-cli open --browser=firefox    # Mozilla Firefox
playwright-cli open --browser=webkit     # WebKit (Safari-Engine)
playwright-cli open --browser=msedge     # Microsoft Edge
```

## Profil-Modi

### In-Memory (Standard)
Cookies und Storage bleiben zwischen Befehlen erhalten, werden beim Schliessen geloescht:

```bash
playwright-cli open https://example.com
```

### Persistent (auf Disk)
Profil wird gespeichert und ueberlebt Neustarts:

```bash
playwright-cli open https://example.com --persistent
```

Standard-Speicherorte:
- macOS: `~/Library/Caches/ms-playwright/mcp-{channel}-profile`
- Linux: `~/.cache/ms-playwright/mcp-{channel}-profile`
- Windows: `%LOCALAPPDATA%\ms-playwright\mcp-{channel}-profile`

### Benutzerdefiniertes Profil-Verzeichnis

```bash
playwright-cli open https://example.com --profile=./my-profile
```

### Isoliert (explizit In-Memory via Config)

```json
{"browser": {"isolated": true}}
```

## Konfigurationsdatei

```bash
playwright-cli --config path/to/config.json open example.com
```

Automatisch geladen, wenn vorhanden: `.playwright/cli.config.json`

Aktuellen Config anzeigen:

```bash
playwright-cli config-print
```

## Vollstaendiges Config-Schema

```json
{
  "browser": {
    "browserName": "chromium | firefox | webkit",
    "isolated": false,
    "userDataDir": "./profil",
    "launchOptions": {
      "channel": "chrome | msedge | ...",
      "headless": true,
      "executablePath": "/pfad/zum/browser",
      "args": ["--no-sandbox"],
      "proxy": {
        "server": "http://proxy:8080",
        "bypass": "localhost,*.intern",
        "username": "user",
        "password": "pass"
      }
    },
    "contextOptions": {
      "viewport": { "width": 1280, "height": 720 },
      "locale": "de-DE",
      "userAgent": "...",
      "storageState": "./auth.json",
      "permissions": ["geolocation"],
      "serviceWorkers": "allow | block"
    },
    "cdpEndpoint": "http://localhost:9222",
    "cdpHeaders": { "Authorization": "Bearer token" },
    "cdpTimeout": 30000,
    "remoteEndpoint": "ws://localhost:3000",
    "initPage": ["./setup-page.ts"],
    "initScript": ["./setup.js"]
  },
  "extension": false,
  "saveVideo": { "width": 800, "height": 600 },
  "saveSession": false,
  "sharedBrowserContext": false,
  "snapshot": { "mode": "full | none" },
  "imageResponses": "allow | omit",
  "outputDir": "./test-output",
  "outputMode": "file | stdout",
  "console": { "level": "error | warning | info | debug" },
  "network": {
    "allowedOrigins": ["https://api.example.com"],
    "blockedOrigins": ["https://analytics.com"]
  },
  "secrets": { "API_KEY": "geheim" },
  "testIdAttribute": "data-testid",
  "timeouts": {
    "action": 5000,
    "navigation": 30000,
    "expect": 5000
  },
  "allowUnrestrictedFileAccess": false,
  "codegen": "typescript | none"
}
```

## Beispiel-Konfigurationen

### Lokale Entwicklung

```json
{"browser": {"launchOptions": {"headless": false}}}
```

### CI-Umgebung

```json
{
  "browser": {
    "launchOptions": {"headless": true},
    "contextOptions": {"viewport": {"width": 1280, "height": 720}}
  },
  "outputDir": "./test-output"
}
```

### Hinter einem Proxy

```json
{
  "browser": {
    "launchOptions": {
      "proxy": {
        "server": "http://proxy.corp.example.com:8080",
        "bypass": "localhost,*.internal.com"
      }
    }
  }
}
```

### Geraete-Emulation (mobil)

```json
{
  "browser": {
    "contextOptions": {
      "viewport": {"width": 375, "height": 812},
      "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)..."
    }
  }
}
```

### Init-Skripte

```json
{
  "browser": {
    "initScript": ["./setup.js"],
    "initPage": ["./setup-page.ts"]
  }
}
```

## Browser-Extension

Bestehende Browser-Tabs verbinden ohne neuen Browser zu starten:

```bash
playwright-cli attach --extension
```

## open-Befehl — alle Parameter

```bash
playwright-cli open [url]                  # Browser oeffnen
playwright-cli open --headed               # Browser-Fenster anzeigen
playwright-cli open --browser=firefox      # Spezifischer Browser
playwright-cli open --persistent           # Profil auf Disk speichern
playwright-cli open --profile=<pfad>       # Benutzerdefiniertes Profil
playwright-cli open --config=file.json     # Config-Datei
playwright-cli attach --extension          # via Extension verbinden
playwright-cli attach --cdp <url>          # via CDP verbinden
playwright-cli attach --endpoint <url>     # Playwright-Server verbinden
```

## Umgebungsvariablen

| Variable | Beschreibung |
|----------|-------------|
| `PLAYWRIGHT_CLI_SESSION` | Standard-Session-Name |
| `PLAYWRIGHT_MCP_BROWSER` | Browser-Auswahl (`chrome`, `firefox`, `webkit`, `msedge`) |
| `PLAYWRIGHT_MCP_HEADLESS` | Headless-Modus |
| `PLAYWRIGHT_MCP_CAPS` | Capabilities aktivieren (kommagetrennt) |
| `PLAYWRIGHT_MCP_CONFIG` | Pfad zur Config-Datei |
| `PLAYWRIGHT_MCP_ISOLATED` | In-Memory-Profil |
| `PLAYWRIGHT_MCP_EXTENSION` | Via Browser-Extension verbinden |
| `PLAYWRIGHT_MCP_USER_DATA_DIR` | Profil-Verzeichnis |
| `PLAYWRIGHT_MCP_STORAGE_STATE` | Storage-State-Datei |
| `PLAYWRIGHT_MCP_DEVICE` | Zu emulierendes Geraet |
| `PLAYWRIGHT_MCP_EXECUTABLE_PATH` | Benutzerdefinierter Browser-Pfad |
| `PLAYWRIGHT_MCP_VIEWPORT_SIZE` | Viewport-Groesse (z. B. `1280x720`) |
| `PLAYWRIGHT_MCP_PROXY_SERVER` | Proxy-Server-URL |
| `PLAYWRIGHT_MCP_PROXY_BYPASS` | Domains, die Proxy umgehen |
| `PLAYWRIGHT_MCP_USER_AGENT` | Benutzerdefinierter User-Agent |
| `PLAYWRIGHT_MCP_IGNORE_HTTPS_ERRORS` | HTTPS-Fehler ignorieren |
| `PLAYWRIGHT_MCP_TIMEOUT_ACTION` | Action-Timeout (ms) |
| `PLAYWRIGHT_MCP_TIMEOUT_NAVIGATION` | Navigation-Timeout (ms) |
| `PLAYWRIGHT_MCP_CONSOLE_LEVEL` | Console-Nachrichten-Level |
| `PLAYWRIGHT_MCP_TEST_ID_ATTRIBUTE` | Test-ID-Attribut |
| `PLAYWRIGHT_MCP_CDP_ENDPOINT` | CDP-Endpoint |
| `PLAYWRIGHT_MCP_OUTPUT_DIR` | Ausgabe-Verzeichnis |
| `PLAYWRIGHT_MCP_CODEGEN` | Code-Generierungs-Sprache |
| `PLAYWRIGHT_MCP_INIT_PAGE` | Page-Init-TypeScript |
| `PLAYWRIGHT_MCP_INIT_SCRIPT` | Page-Init-JavaScript |
| `PLAYWRIGHT_MCP_BLOCKED_ORIGINS` | Origins blockieren |
| `PLAYWRIGHT_MCP_ALLOWED_ORIGINS` | Origins erlauben |
| `PLAYWRIGHT_MCP_GRANT_PERMISSIONS` | Browser-Berechtigungen |
| `PLAYWRIGHT_MCP_BLOCK_SERVICE_WORKERS` | Service-Worker blockieren |
| `PLAYWRIGHT_MCP_NO_SANDBOX` | Sandbox deaktivieren |
| `PLAYWRIGHT_MCP_SAVE_SESSION` | Session-Daten speichern |
| `PLAYWRIGHT_MCP_SAVE_VIDEO` | Video automatisch aufzeichnen (z. B. `800x600`) |
| `PLAYWRIGHT_MCP_SECRETS_FILE` | Secrets-Datei (dotenv-Format) |

---

Quelle: https://playwright.dev/agent-cli/configuration
