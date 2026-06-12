# Playwright Agent CLI — Capabilities

CLI und MCP teilen dieselben zugrundeliegenden Playwright-Tools, organisiert in
Faehigkeitsgruppen (capability groups). In der CLI sind alle Capabilities immer
verfuegbar — kein Gating.

---

## Core (immer verfuegbar)

Grundlegende Browser-Automatisierung.

| Befehl | Zweck |
|--------|-------|
| `open`, `goto`, `close` | Browser oeffnen, navigieren, schliessen |
| `go-back`, `go-forward`, `reload` | Navigations-History |
| `click`, `dblclick`, `hover`, `drag` | Element-Interaktion |
| `type`, `fill`, `select` | Texteingabe und Dropdowns |
| `check`, `uncheck` | Checkboxen und Radio-Buttons |
| `press`, `keydown`, `keyup` | Tastatur-Eingabe |
| `snapshot` | Accessibility-Tree erfassen |
| `screenshot` | Screenshot aufnehmen |
| `upload` | Dateien hochladen |
| `dialog-accept`, `dialog-dismiss` | Dialoge behandeln |
| `resize` | Browser-Fenster anpassen |
| `eval`, `run-code` | JavaScript/Playwright-Code ausfuehren |

---

## Network

Netzwerk-Inspektion und -Mocking.

| Befehl | Zweck |
|--------|-------|
| `network` | Netzwerk-Anfragen seit Seitenaufruf auflisten |
| `route` | Anfragen fuer URL-Muster mocken |
| `route-list` | Aktive Mock-Routen auflisten |
| `unroute` | Mock-Routen entfernen |
| `network-state-set` | Online/Offline-Zustand setzen |

---

## Storage

Cookie-, localStorage- und sessionStorage-Verwaltung sowie State-Persistenz.

| Befehl | Zweck |
|--------|-------|
| `state-save`, `state-load` | Kompletten Browser-State speichern/wiederherstellen |
| `cookie-list/get/set/delete/clear` | Cookies verwalten |
| `localstorage-list/get/set/delete/clear` | localStorage verwalten |
| `sessionstorage-list/get/set/delete/clear` | sessionStorage verwalten |

---

## Vision

Koordinatenbasierte Maus-Interaktion mit Pixel-Positionen aus Screenshots.
Nuetzlich fuer Canvas-Apps, Karten und benutzerdefinierte Widgets ohne
barrierefreie Elemente.

| Befehl | Zweck |
|--------|-------|
| `mousemove <x> <y>` | Maus zu Koordinaten bewegen |
| `mousedown [button]` | Maustaste druecken |
| `mouseup [button]` | Maustaste loslassen |
| `mousewheel <dx> <dy>` | Mit Mausrad scrollen |
| `screenshot` | Viewport fuer Koordinaten-Referenz erfassen |

---

## DevTools

Tracing, Video-Aufnahme und Test-Debugging.

| Befehl | Zweck |
|--------|-------|
| `console` | Console-Nachrichten anzeigen |
| `tracing-start`, `tracing-stop` | Ausfuehrungs-Traces aufzeichnen |
| `video-start`, `video-stop`, `video-chapter` | Session-Videos aufzeichnen |
| `show` | Visuelles Dashboard oeffnen |
| `pause-at`, `resume`, `step-over` | Test-Debugging |

---

## PDF

PDF-Generierung.

| Befehl | Zweck |
|--------|-------|
| `pdf` | Seite als PDF exportieren |

---

## Testing

Assertions und Test-Generierungs-Tools.

| Befehl | Zweck |
|--------|-------|
| `verify-element-visible` | Element per Rolle und Name als sichtbar pruefen |
| `verify-text-visible` | Text als sichtbar pruefen |
| `verify-list-visible` | Liste mit Eintraegen als sichtbar pruefen |
| `verify-value` | Formularfeld-Wert pruefen |
| `generate-locator` | Playwright-Locator fuer Test-Code generieren |

---

Quelle: https://playwright.dev/agent-cli/capabilities
