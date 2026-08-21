# Playwright MCP Server

## Contents

- [What is Playwright MCP?](#what-is-playwright-mcp)
- [Installation](#installation)
- [Client-specific installation](#client-specific-installation)
- [Configuration options](#configuration-options)
- [Capabilities](#capabilities)
- [Profile modes](#profile-modes)
- [Accessibility snapshots](#accessibility-snapshots)
- [Vision mode](#vision-mode)
- [Configuration file (config.json)](#configuration-file-configjson)
- [Source](#source)

## What is Playwright MCP?

Playwright MCP is a Model Context Protocol server for browser automation by LLMs.
Instead of visual processing it uses structured **accessibility snapshots** (ARIA tree),
which enable deterministic interaction without a vision model.

### Core architecture points

- **Snapshot-based**: accessibility tree with unique `ref` IDs for interactive elements
- **Token-efficient**: ~200-400 tokens/snapshot vs. 3,000-5,000 tokens for screenshots
- **Determinism**: same structure = same interaction
- **Headed by default**: the browser is started visibly for real-time observation

---

## Installation

### Prerequisites

- Node.js 20 or newer
- A compatible MCP client

### Standard configuration (all clients)

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

The browser is **downloaded automatically on the first call**.

---

## Client-specific installation

### VS Code

```bash
# CLI installation
code --add-mcp '{"name":"playwright","command":"npx","args":["@playwright/mcp@latest"]}'
```

Or: VS Code Insiders:
```bash
code-insiders --add-mcp '{"name":"playwright","command":"npx","args":["@playwright/mcp@latest"]}'
```

Integrates into VS Code as a GitHub Copilot agent.

### Claude Code

```bash
claude mcp add playwright npx @playwright/mcp@latest
```

Available in the next Claude Code session.

### Cursor

Settings -> MCP -> "Add new MCP Server":
- Name: `playwright`
- Type: `command`
- Command: `npx @playwright/mcp@latest`

### Windsurf / Cline / Goose / Kiro / Codex / Copilot CLI

Standard MCP configuration (see the client documentation).

---

## Configuration options

### CLI flags

```bash
# Headless mode
npx @playwright/mcp@latest --headless

# Choose browser: chrome (default), firefox, webkit, msedge
npx @playwright/mcp@latest --browser=firefox

# HTTP transport (standalone server)
npx @playwright/mcp@latest --port 8931

# Enable capabilities
npx @playwright/mcp@latest --caps=vision,pdf,devtools

# All capabilities
npx @playwright/mcp@latest --caps=core,network,storage,testing,vision,pdf,devtools

# Isolated mode (no state between sessions)
npx @playwright/mcp@latest --isolated

# Browser extension mode
npx @playwright/mcp@latest --extension

# User profile directory
npx @playwright/mcp@latest --user-data-dir=/path/to/profile

# Load session state
npx @playwright/mcp@latest --storage-state=./auth-state.json

# Shared context for all clients
npx @playwright/mcp@latest --shared-browser-context

# Proxy
npx @playwright/mcp@latest --proxy-server=http://myproxy:3128

# Proxy bypass
npx @playwright/mcp@latest --proxy-bypass=localhost,*.internal.com

# Viewport
npx @playwright/mcp@latest --viewport=1280x720

# Device emulation
npx @playwright/mcp@latest --device="iPhone 15"
```

### HTTP transport configuration

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

Client endpoint: `http://localhost:8931/mcp`

### Complete options table

| Option | Type | Default | Description |
|--------|-----|---------|--------------|
| `--headless` | flag | headed | Start the browser without a UI |
| `--browser` | string | `chrome` | Browser engine: `chrome`/`firefox`/`webkit`/`msedge` |
| `--device` | string | — | Device emulation (e.g. `"iPhone 15"`) |
| `--viewport` | string | — | Viewport size (e.g. `1280x720`) |
| `--port` | number | — | HTTP transport port |
| `--host` | string | `localhost` | Bind address (`0.0.0.0` for containers) |
| `--caps` | string | `core` | Comma-separated capabilities |
| `--isolated` | flag | — | No persistent state between sessions |
| `--extension` | flag | — | Browser extension mode |
| `--user-data-dir` | string | Platform cache | Profile directory |
| `--storage-state` | string | — | Load a session state file |
| `--proxy-server` | string | — | Proxy URL |
| `--proxy-bypass` | string | — | Comma-separated bypass hosts |
| `--save-session` | flag | — | Record the session automatically |
| `--config` | string | — | Path to the configuration file |
| `--shared-browser-context` | flag | — | Single context for all clients |
| `--allow-unrestricted-file-access` | flag | — | File uploads without workspace restriction |

### Timeout configuration

| Timeout | Default | Description |
|---------|---------|--------------|
| Action | 5,000 ms | Single interaction |
| Navigation | 60,000 ms | Page navigation |
| Expect | 5,000 ms | Assertions |

---

## Capabilities

### Overview

| Capability | Always active | Tools | Description |
|-----------|------------|-------|--------------|
| `core` | Yes | 15+ | Basic browser automation |
| `core-navigation` | No | — | Navigation subset only |
| `core-tabs` | No | — | Tab management only |
| `core-input` | No | — | Input operations only |
| `network` | No | 4 | Request mocking, online/offline |
| `storage` | No | 15+ | Cookies, localStorage, state |
| `testing` | No | 5 | Assertions + locator generation |
| `vision` | No | 6 | Coordinate-based mouse tools |
| `pdf` | No | 1 | PDF export |
| `devtools` | No | 4 | Tracing, video, debugging |
| `config` | No | 1 | Retrieve configuration |

### Activation options

```bash
# CLI flag
npx @playwright/mcp@latest --caps=vision,pdf,devtools

# Environment variable
PLAYWRIGHT_MCP_CAPS=vision,devtools npx @playwright/mcp@latest

# In the MCP configuration
{
  "args": ["@playwright/mcp@latest", "--caps=storage,testing,devtools"]
}
```

### Design principle

Only enable the capabilities you need, in order to:
- reduce token cost
- minimise hallucinated tool calls
- speed up response times

---

## Profile modes

### Persistent (default)

Login state, cookies and localStorage are retained between sessions.

Platform-specific storage locations:
- macOS: `~/Library/Caches/ms-playwright/mcp-{channel}-profile`
- Linux: `~/.cache/ms-playwright/mcp-{channel}-profile`
- Windows: `%LOCALAPPDATA%\ms-playwright\mcp-{channel}-profile`

Override: `--user-data-dir=/path/to/profile`

### Isolated

Every session starts without stored state.

```json
{
  "args": ["@playwright/mcp@latest", "--isolated"]
}
```

Load initial credentials: `--storage-state=./auth-state.json`

### Browser extension mode

Connects to existing browser tabs instead of starting new ones.

```json
{
  "args": ["@playwright/mcp@latest", "--extension"]
}
```

Use cases:
- SSO/2FA: reuse an authenticated session
- Browser extensions: automate pages with installed add-ons
- Existing tabs: automate already opened pages

---

## Accessibility snapshots

### How it works

Every interaction returns a structured ARIA tree with `ref` IDs:

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

### Ref properties

| Property | Value |
|-------------|------|
| Format | `e` followed by a number (e.g. `e5`, `e203`) |
| Uniqueness | Per snapshot |
| Lifetime | Until the next navigation or DOM change |
| Assignment | Only interactive elements receive refs |

### Workflow pattern

```
1. browser_navigate -> snapshot returned
2. LLM reads the snapshot, identifies the ref
3. browser_type { ref: "e5", text: "..." }
4. Next snapshot automatically
5. Re-read refs after navigation
```

### Combining snapshot + screenshot

For visually intensive interfaces: combine the structured snapshot for interaction with a screenshot for understanding the layout.

---

## Vision mode

Extends snapshots with coordinate-based tools for elements without ARIA support.

### Activation

```json
{
  "args": ["@playwright/mcp@latest", "--caps=vision"]
}
```

### Use cases

| Scenario | Rationale |
|----------|-------------|
| Canvas/WebGL | No ARIA elements |
| Map interaction | Pan/zoom requires coordinates |
| Image editors | Drawing operations |
| Charts | Selecting data points |
| Custom widgets without ARIA | No accessibility tree |

### Recommendation

For normal web applications: **prefer the snapshot-based approach** (more reliable and more token-efficient). Use vision as a fallback.

---

## Configuration file (config.json)

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

Usage: `npx @playwright/mcp@latest --config path/to/config.json`

Schema: https://github.com/microsoft/playwright-mcp/blob/main/config.d.ts

---

## Source

- https://playwright.dev/docs/getting-started-mcp
- https://playwright.dev/mcp/introduction
- https://playwright.dev/mcp/installation
- https://playwright.dev/mcp/capabilities
- https://playwright.dev/mcp/snapshots
- https://playwright.dev/mcp/vision-mode
- https://playwright.dev/mcp/configuration/options
- https://playwright.dev/mcp/configuration/user-profile
- https://playwright.dev/mcp/configuration/browser-extension
