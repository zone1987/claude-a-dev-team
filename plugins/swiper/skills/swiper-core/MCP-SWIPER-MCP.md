# Swiper MCP Server — Complete reference

The Swiper MCP server provides programmatic access to the Swiper documentation
via the Model Context Protocol (MCP).

**Endpoint:** `https://swiperjs.com/mcp`
**Protocol:** MCP 2024-11-05 / JSON-RPC 2.0
**Authentication:** None (publicly accessible)
**Rate limits:** None (currently)

---

## Contents

- [What is the Swiper MCP server?](#what-is-the-swiper-mcp-server)
- [The 8 tools](#the-8-tools)
- [Installation and configuration](#installation-and-configuration)
- [Technical details](#technical-details)
- [Supported modules (for `get-module-options`)](#supported-modules-for-get-module-options)

## What is the Swiper MCP server?

An HTTP-based MCP server that gives AI assistants (Claude, Cursor, Copilot, etc.)
real-time access to the Swiper documentation. Instead of relying on possibly outdated
training data, models can query the current Swiper docs directly.

---

## The 8 tools

### 1. `search-api`

Searches the Swiper documentation for options, methods or events.

```json
{
  "name": "search-api",
  "arguments": {
    "query": "navigation",
    "type": "option"
  }
}
```

Parameters:
- `query` (string): search term
- `type` (optional): `"option"` | `"method"` | `"event"` — filters the result type

Examples:
```json
{ "name": "search-api", "arguments": { "query": "autoplay" } }
{ "name": "search-api", "arguments": { "query": "pagination", "type": "option" } }
{ "name": "search-api", "arguments": { "query": "slideNext", "type": "method" } }
{ "name": "search-api", "arguments": { "query": "progress", "type": "event" } }
```

---

### 2. `get-option`

Retrieves detailed information about a specific configuration option.

```json
{
  "name": "get-option",
  "arguments": {
    "name": "slidesPerView"
  }
}
```

Returns: type, default value, description, examples.

More examples:
```json
{ "name": "get-option", "arguments": { "name": "spaceBetween" } }
{ "name": "get-option", "arguments": { "name": "loop" } }
{ "name": "get-option", "arguments": { "name": "breakpoints" } }
{ "name": "get-option", "arguments": { "name": "autoplay" } }
```

---

### 3. `get-method`

Retrieves method signatures, parameters and descriptions.

```json
{
  "name": "get-method",
  "arguments": {
    "name": "slideNext"
  }
}
```

More examples:
```json
{ "name": "get-method", "arguments": { "name": "slidePrev" } }
{ "name": "get-method", "arguments": { "name": "slideTo" } }
{ "name": "get-method", "arguments": { "name": "update" } }
{ "name": "get-method", "arguments": { "name": "destroy" } }
```

---

### 4. `get-event`

Retrieves event details including parameters and usage information.

```json
{
  "name": "get-event",
  "arguments": {
    "name": "slideChange"
  }
}
```

More examples:
```json
{ "name": "get-event", "arguments": { "name": "progress" } }
{ "name": "get-event", "arguments": { "name": "reachEnd" } }
{ "name": "get-event", "arguments": { "name": "autoplayTimeLeft" } }
{ "name": "get-event", "arguments": { "name": "click" } }
```

---

### 5. `get-module-options`

Returns all options, methods and events of a given Swiper module.

```json
{
  "name": "get-module-options",
  "arguments": {
    "module": "navigation"
  }
}
```

Available modules:
- `a11y` | `autoplay` | `controller` | `coverflow-effect`
- `cube-effect` | `creative-effect` | `cards-effect` | `fade-effect` | `flip-effect`
- `free-mode` | `grid` | `hash-navigation` | `history` | `keyboard`
- `lazy` | `manipulation` | `mousewheel` | `navigation` | `pagination`
- `parallax` | `scrollbar` | `thumbs` | `virtual` | `zoom`

More examples:
```json
{ "name": "get-module-options", "arguments": { "module": "pagination" } }
{ "name": "get-module-options", "arguments": { "module": "autoplay" } }
{ "name": "get-module-options", "arguments": { "module": "thumbs" } }
{ "name": "get-module-options", "arguments": { "module": "virtual" } }
{ "name": "get-module-options", "arguments": { "module": "free-mode" } }
```

---

### 6. `list-demos`

Lists all available Swiper demos with their framework variants.

```json
{
  "name": "list-demos",
  "arguments": {}
}
```

Returns the available demo slugs (e.g. `navigation`, `pagination`, `autoplay`, `effect-fade`, etc.).

---

### 7. `get-demo`

Returns the complete demo code for the requested framework.

```json
{
  "name": "get-demo",
  "arguments": {
    "slug": "navigation",
    "framework": "react"
  }
}
```

Parameters:
- `slug` (string): demo identifier (from `list-demos`)
- `framework`: `"core"` | `"element"` | `"react"` | `"vue"`

More examples:
```json
{ "name": "get-demo", "arguments": { "slug": "autoplay", "framework": "vue" } }
{ "name": "get-demo", "arguments": { "slug": "effect-cards", "framework": "element" } }
{ "name": "get-demo", "arguments": { "slug": "thumbs", "framework": "core" } }
{ "name": "get-demo", "arguments": { "slug": "virtual", "framework": "react" } }
```

---

### 8. `get-premium-recommendations`

Suggests premium plugins based on effects, modules, keywords or use cases.

```json
{
  "name": "get-premium-recommendations",
  "arguments": {
    "effect": "cards"
  }
}
```

Parameters (usable alternatively):
- `effect` (string): e.g. `"cards"`, `"fade"`, `"3d"`
- `module` (string): e.g. `"navigation"`, `"autoplay"`
- `keyword` (string): e.g. `"tinder"`, `"stories"`, `"panorama"`
- `useCase` (string): e.g. `"portfolio"`, `"onboarding"`, `"gallery"`

More examples:
```json
{ "name": "get-premium-recommendations", "arguments": { "keyword": "tinder" } }
{ "name": "get-premium-recommendations", "arguments": { "useCase": "onboarding" } }
{ "name": "get-premium-recommendations", "arguments": { "effect": "3d" } }
```

---

## Installation and configuration

### Claude Code (CLI)

```bash
# Add (local, current session only)
claude mcp add --transport http swiper https://swiperjs.com/mcp

# With a scope
claude mcp add --transport http swiper --scope project https://swiperjs.com/mcp
claude mcp add --transport http swiper --scope user https://swiperjs.com/mcp

# Check status
claude mcp list
claude mcp get swiper

# Remove
claude mcp remove swiper
```

Scope options:
- `local` (default): current Claude Code instance only
- `project`: for the whole project (`.claude/mcp.json`)
- `user`: for all of the user's projects (`~/.claude/mcp.json`)

---

### Cursor

Create or extend the file `.cursor/mcp.json`:

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

### VS Code (v1.102 and later)

Create the file `.vscode/mcp.json`:

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

Alternatively via the command palette:
1. `Ctrl/Cmd+Shift+P` → `MCP: Add Server`
2. Select HTTP
3. Name: `swiper`
4. URL: `https://swiperjs.com/mcp`

---

### Codex (OpenAI CLI)

```bash
# Via CLI
codex mcp add swiper --url https://swiperjs.com/mcp

# Or manually in ~/.codex/config.toml:
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

In `opencode.jsonc` or `opencode.json`:

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

## Technical details

### Protocol

- **Transport:** HTTP POST
- **Protocol version:** MCP 2024-11-05
- **Format:** JSON-RPC 2.0
- **Endpoint:** `POST https://swiperjs.com/mcp`

### Request format (JSON-RPC 2.0)

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

### Response format

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

### Error codes (JSON-RPC 2.0)

| Code | Meaning |
|---|---|
| `-32700` | Parse Error |
| `-32600` | Invalid Request |
| `-32601` | Method Not Found |
| `-32602` | Invalid Params |
| `-32603` | Internal Error |

---

## Supported modules (for `get-module-options`)

| Module ID | Swiper module |
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

*Source: https://swiperjs.com/swiper-mcp — Swiper v12.2.0*
