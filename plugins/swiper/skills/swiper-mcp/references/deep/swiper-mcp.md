# Swiper MCP Server — Vollständige Referenz

Der Swiper MCP Server bietet programmatischen Zugriff auf die Swiper-Dokumentation
über das Model Context Protocol (MCP).

**Endpoint:** `https://swiperjs.com/mcp`
**Protokoll:** MCP 2024-11-05 / JSON-RPC 2.0
**Authentifizierung:** Keine (öffentlich zugänglich)
**Rate Limits:** Keine (aktuell)

---

## Was ist der Swiper MCP Server?

Ein HTTP-basierter MCP-Server, der KI-Assistenten (Claude, Cursor, Copilot, etc.) mit
Echtzeit-Zugriff auf die Swiper-Dokumentation versorgt. Anstatt auf möglicherweise veraltete
Trainingsdaten zurückzugreifen, können Modelle direkt aktuelle Swiper-Docs abfragen.

---

## Die 8 Tools

### 1. `search-api`

Durchsucht Swiper-Dokumentation nach Optionen, Methoden oder Events.

```json
{
  "name": "search-api",
  "arguments": {
    "query": "navigation",
    "type": "option"
  }
}
```

Parameter:
- `query` (string): Suchbegriff
- `type` (optional): `"option"` | `"method"` | `"event"` — filtert Ergebnistyp

Beispiele:
```json
{ "name": "search-api", "arguments": { "query": "autoplay" } }
{ "name": "search-api", "arguments": { "query": "pagination", "type": "option" } }
{ "name": "search-api", "arguments": { "query": "slideNext", "type": "method" } }
{ "name": "search-api", "arguments": { "query": "progress", "type": "event" } }
```

---

### 2. `get-option`

Ruft detaillierte Informationen zu einer spezifischen Konfigurations-Option ab.

```json
{
  "name": "get-option",
  "arguments": {
    "name": "slidesPerView"
  }
}
```

Liefert: Typ, Standardwert, Beschreibung, Beispiele.

Weitere Beispiele:
```json
{ "name": "get-option", "arguments": { "name": "spaceBetween" } }
{ "name": "get-option", "arguments": { "name": "loop" } }
{ "name": "get-option", "arguments": { "name": "breakpoints" } }
{ "name": "get-option", "arguments": { "name": "autoplay" } }
```

---

### 3. `get-method`

Ruft Methodensignaturen, Parameter und Beschreibungen ab.

```json
{
  "name": "get-method",
  "arguments": {
    "name": "slideNext"
  }
}
```

Weitere Beispiele:
```json
{ "name": "get-method", "arguments": { "name": "slidePrev" } }
{ "name": "get-method", "arguments": { "name": "slideTo" } }
{ "name": "get-method", "arguments": { "name": "update" } }
{ "name": "get-method", "arguments": { "name": "destroy" } }
```

---

### 4. `get-event`

Ruft Event-Details inkl. Parameter und Verwendungsinformationen ab.

```json
{
  "name": "get-event",
  "arguments": {
    "name": "slideChange"
  }
}
```

Weitere Beispiele:
```json
{ "name": "get-event", "arguments": { "name": "progress" } }
{ "name": "get-event", "arguments": { "name": "reachEnd" } }
{ "name": "get-event", "arguments": { "name": "autoplayTimeLeft" } }
{ "name": "get-event", "arguments": { "name": "click" } }
```

---

### 5. `get-module-options`

Gibt alle Optionen, Methoden und Events eines bestimmten Swiper-Moduls zurück.

```json
{
  "name": "get-module-options",
  "arguments": {
    "module": "navigation"
  }
}
```

Verfügbare Module:
- `a11y` | `autoplay` | `controller` | `coverflow-effect`
- `cube-effect` | `creative-effect` | `cards-effect` | `fade-effect` | `flip-effect`
- `free-mode` | `grid` | `hash-navigation` | `history` | `keyboard`
- `lazy` | `manipulation` | `mousewheel` | `navigation` | `pagination`
- `parallax` | `scrollbar` | `thumbs` | `virtual` | `zoom`

Weitere Beispiele:
```json
{ "name": "get-module-options", "arguments": { "module": "pagination" } }
{ "name": "get-module-options", "arguments": { "module": "autoplay" } }
{ "name": "get-module-options", "arguments": { "module": "thumbs" } }
{ "name": "get-module-options", "arguments": { "module": "virtual" } }
{ "name": "get-module-options", "arguments": { "module": "free-mode" } }
```

---

### 6. `list-demos`

Listet alle verfügbaren Swiper-Demos mit Framework-Varianten auf.

```json
{
  "name": "list-demos",
  "arguments": {}
}
```

Gibt verfügbare Demo-Slugs zurück (z.B. `navigation`, `pagination`, `autoplay`, `effect-fade`, etc.).

---

### 7. `get-demo`

Liefert vollständigen Demo-Code im gewünschten Framework.

```json
{
  "name": "get-demo",
  "arguments": {
    "slug": "navigation",
    "framework": "react"
  }
}
```

Parameter:
- `slug` (string): Demo-Identifier (von `list-demos`)
- `framework`: `"core"` | `"element"` | `"react"` | `"vue"`

Weitere Beispiele:
```json
{ "name": "get-demo", "arguments": { "slug": "autoplay", "framework": "vue" } }
{ "name": "get-demo", "arguments": { "slug": "effect-cards", "framework": "element" } }
{ "name": "get-demo", "arguments": { "slug": "thumbs", "framework": "core" } }
{ "name": "get-demo", "arguments": { "slug": "virtual", "framework": "react" } }
```

---

### 8. `get-premium-recommendations`

Schlägt Premium-Plugins basierend auf Effekten, Modulen, Keywords oder Anwendungsfällen vor.

```json
{
  "name": "get-premium-recommendations",
  "arguments": {
    "effect": "cards"
  }
}
```

Parameter (alternativ verwendbar):
- `effect` (string): z.B. `"cards"`, `"fade"`, `"3d"`
- `module` (string): z.B. `"navigation"`, `"autoplay"`
- `keyword` (string): z.B. `"tinder"`, `"stories"`, `"panorama"`
- `useCase` (string): z.B. `"portfolio"`, `"onboarding"`, `"gallery"`

Weitere Beispiele:
```json
{ "name": "get-premium-recommendations", "arguments": { "keyword": "tinder" } }
{ "name": "get-premium-recommendations", "arguments": { "useCase": "onboarding" } }
{ "name": "get-premium-recommendations", "arguments": { "effect": "3d" } }
```

---

## Installation & Konfiguration

### Claude Code (CLI)

```bash
# Hinzufügen (lokal, nur für aktuelle Session)
claude mcp add --transport http swiper https://swiperjs.com/mcp

# Mit Scope
claude mcp add --transport http swiper --scope project https://swiperjs.com/mcp
claude mcp add --transport http swiper --scope user https://swiperjs.com/mcp

# Status prüfen
claude mcp list
claude mcp get swiper

# Entfernen
claude mcp remove swiper
```

Scope-Optionen:
- `local` (default): Nur für aktuelle Claude-Code-Instanz
- `project`: Für das gesamte Projekt (`.claude/mcp.json`)
- `user`: Für alle Projekte des Users (`~/.claude/mcp.json`)

---

### Cursor

Datei `.cursor/mcp.json` erstellen/erweitern:

```json
{
  "mcpServers": {
    "swiper": {
      "url": "https://swiperjs.com/mcp"
    }
  }
}
```

---

### VS Code (ab v1.102)

Datei `.vscode/mcp.json` erstellen:

```json
{
  "servers": {
    "swiper": {
      "type": "http",
      "url": "https://swiperjs.com/mcp"
    }
  }
}
```

Alternativ via Command Palette:
1. `Ctrl/Cmd+Shift+P` → `MCP: Add Server`
2. HTTP auswählen
3. Name: `swiper`
4. URL: `https://swiperjs.com/mcp`

---

### Codex (OpenAI CLI)

```bash
# Via CLI
codex mcp add swiper --url https://swiperjs.com/mcp

# Oder manuell in ~/.codex/config.toml:
```

```toml
[mcp_servers.swiper]
url = "https://swiperjs.com/mcp"
startup_timeout_sec = 10
tool_timeout_sec = 60
enabled = true
```

---

### OpenCode

In `opencode.jsonc` oder `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "swiper": {
      "type": "remote",
      "url": "https://swiperjs.com/mcp",
      "enabled": true
    }
  }
}
```

---

## Technische Details

### Protokoll

- **Transport:** HTTP POST
- **Protokoll-Version:** MCP 2024-11-05
- **Format:** JSON-RPC 2.0
- **Endpoint:** `POST https://swiperjs.com/mcp`

### Request-Format (JSON-RPC 2.0)

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get-option",
    "arguments": {
      "name": "slidesPerView"
    }
  }
}
```

### Response-Format

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "..."
      }
    ]
  }
}
```

### Error-Codes (JSON-RPC 2.0)

| Code | Bedeutung |
|---|---|
| `-32700` | Parse Error |
| `-32600` | Invalid Request |
| `-32601` | Method Not Found |
| `-32602` | Invalid Params |
| `-32603` | Internal Error |

---

## Unterstützte Module (für `get-module-options`)

| Modul-ID | Swiper-Modul |
|---|---|
| `a11y` | Accessibility |
| `autoplay` | Autoplay |
| `controller` | Controller |
| `coverflow-effect` | Coverflow Effect |
| `cube-effect` | Cube Effect |
| `creative-effect` | Creative Effect |
| `cards-effect` | Cards Effect |
| `fade-effect` | Fade Effect |
| `flip-effect` | Flip Effect |
| `free-mode` | Free Mode |
| `grid` | Grid |
| `hash-navigation` | Hash Navigation |
| `history` | History |
| `keyboard` | Keyboard |
| `lazy` | Lazy Loading |
| `manipulation` | Manipulation |
| `mousewheel` | Mousewheel |
| `navigation` | Navigation |
| `pagination` | Pagination |
| `parallax` | Parallax |
| `scrollbar` | Scrollbar |
| `thumbs` | Thumbs |
| `virtual` | Virtual |
| `zoom` | Zoom |

---

*Quelle: https://swiperjs.com/swiper-mcp — Swiper v12.2.0*
