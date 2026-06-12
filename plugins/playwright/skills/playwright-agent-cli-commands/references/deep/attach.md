# Playwright Agent CLI — Attach

## Befehlsuebersicht

| Befehl | Beschreibung |
|--------|-------------|
| `attach --cdp=<channel>` | Verbinden mit laufendem Browser per Kanal-Name |
| `attach --cdp=<url>` | Verbinden via Chrome DevTools Protocol Endpoint |
| `attach --endpoint=<url>` | Verbinden mit Playwright-Server-Endpoint |
| `attach --extension` | Verbinden via Playwright-Extension (Standard: Chrome) |
| `attach --extension=<channel>` | Verbinden via Playwright-Extension mit spezifischem Kanal |
| `attach <session-name>` | Verbinden mit pausiertem Test (Test-Debugging) |

---

## attach --cdp (Kanal-Name)

Verbindet mit laufenden Chrome- oder Edge-Instanzen. Der Browser muss Remote-Debugging aktiviert haben:
Chrome: `chrome://inspect/#remote-debugging` → "Allow remote debugging for this browser instance" aktivieren.

### Unterstuetzte Kanaele

| Kanal | Beschreibung |
|-------|-------------|
| `chrome` | Google Chrome (Stable) |
| `chrome-beta` | Google Chrome Beta |
| `chrome-dev` | Google Chrome Dev |
| `chrome-canary` | Google Chrome Canary |
| `msedge` | Microsoft Edge (Stable) |
| `msedge-beta` | Microsoft Edge Beta |
| `msedge-dev` | Microsoft Edge Dev |
| `msedge-canary` | Microsoft Edge Canary |

```bash
playwright-cli attach --cdp=chrome
playwright-cli attach --cdp=chrome-canary
playwright-cli attach --cdp=msedge
playwright-cli attach --cdp=msedge-dev
```

---

## attach --cdp (URL/Endpoint)

Verbindet mit Chromium-basierten Browsern via CDP-Endpoint:

```bash
# Browser mit Remote-Debugging starten
google-chrome --remote-debugging-port=9222

# Verbinden
playwright-cli attach --cdp=http://localhost:9222
playwright-cli snapshot
playwright-cli click e5
```

### attach --cdp-Optionen

| Option | Typ | Pflicht | Beschreibung |
|--------|-----|---------|-------------|
| `--cdp=<channel\|url>` | string | Ja | Kanal-Name (`chrome`, `msedge` usw.) oder vollstaendige CDP-URL |

### Kompatibel mit

- Chrome/Chromium mit `--remote-debugging-port`
- Edge mit Remote-Debugging
- Electron-Apps, die CDP exponieren
- Cloud-Browser-Dienste (Browserbase usw.)

---

## attach --endpoint

Verbindet mit einem Playwright-Server-Endpoint:

```bash
playwright-cli attach --endpoint=ws://localhost:3000
playwright-cli snapshot
```

### attach --endpoint-Optionen

| Option | Typ | Pflicht | Beschreibung |
|--------|-----|---------|-------------|
| `--endpoint=<url>` | string | Ja | WebSocket-URL des Playwright-Servers |

---

## attach --extension

Verbindet ueber die Playwright-Extension fuer bestehende Browser-Sessions
(inkl. Cookies, Extensions, eingeloggte Sessions):

```bash
playwright-cli attach --extension
playwright-cli attach --extension=chrome-canary
playwright-cli attach --extension=msedge
playwright-cli attach --extension=msedge-dev
```

### attach --extension-Optionen

| Option | Typ | Pflicht | Standard | Beschreibung |
|--------|-----|---------|---------|-------------|
| `--extension[=<channel>]` | string | — | `chrome` | Browser-Kanal fuer Extension-Verbindung |

### Anwendungsfaelle

| Szenario | Vorteil |
|----------|---------|
| SSO/2FA-Authentifizierung umgehen | Bestehende Login-Session nutzen |
| Browser-Extensions integrieren | Extensions laufen wie beim normalen Nutzer |
| Bestehenden Tab automatisieren | Kein neuer Browser-Start noetig |

---

## Benannte Sessions mit attach

```bash
playwright-cli attach --cdp=chrome -s=debug-session
playwright-cli -s=debug-session snapshot
playwright-cli -s=debug-session click e5
```

### Session-Flag

| Flag | Typ | Beschreibung |
|------|-----|-------------|
| `-s=<name>` | string | Session-Name fuer diesen attach-Befehl |

---

## Vollstaendige Workflows

### Verbindung zu laufendem Chrome

```bash
playwright-cli attach --cdp=chrome
playwright-cli snapshot
playwright-cli screenshot --filename=current-state.png
playwright-cli state-save auth.json
```

### Remote-Browser-Debugging (SSH-Tunnel)

```bash
# Auf Remote-Server
google-chrome --remote-debugging-port=9222

# Lokaler SSH-Tunnel
ssh -L 9222:localhost:9222 user@remote-host

# Verbinden
playwright-cli attach --cdp=http://localhost:9222
playwright-cli snapshot
playwright-cli screenshot --filename=remote-state.png
playwright-cli console error
```

### CDP-Verbindung zu Electron-App

```bash
# Electron muss CDP exponieren (z. B. --remote-debugging-port=9229)
playwright-cli attach --cdp=http://localhost:9229
playwright-cli snapshot
playwright-cli click e10
```

---

Quelle: https://playwright.dev/agent-cli/commands/attach
