# Playwright Agent CLI — Introduction, quick start, installation, skills

## Contents

- [What is the Playwright Agent CLI?](#what-is-the-playwright-agent-cli)
- [Quick start](#quick-start)
- [Installation](#installation)
- [Skills](#skills)
- [All commands — overview](#all-commands-overview)

## What is the Playwright Agent CLI?

A command-line interface for browser automation that was designed specifically for coding
agents. The CLI provides token-efficient commands and installable skills so that agents
can balance browser automation and large codebases within limited context
windows.

### Core characteristics

| Characteristic | Description |
|---------|-------------|
| Token-efficient | Compact CLI output avoids loading large tool schemas into the model context |
| Skill-based | Agents discover capabilities via installable skills |
| Daemon architecture | A persistent browser process eliminates per-command startup cost |
| Ref-based | Accessibility snapshots with element refs for deterministic interaction |
| Cross-browser | Chrome, Firefox, WebKit and Edge |
| Sessions | Multiple isolated browser instances with their own state |

### Playwright CLI vs. MCP

| Aspect | Playwright CLI | MCP |
|--------|---------------|-----|
| Best for | Coding agents with large codebases | Specialised agentic loops, exploratory automation |
| How it works | The agent runs shell commands | The LLM calls MCP tools with structured parameters |
| Token cost | Lower — compact output, skills on demand | Higher — tool schemas + snapshots in the context |
| Default mode | Headless | Headed |
| Setup | `npm install -g @playwright/cli` | JSON config in the MCP client |

---

## Quick start

### Typical workflow

```bash
playwright-cli open https://demo.playwright.dev/todomvc --headed
playwright-cli type "Buy groceries"
playwright-cli press Enter
playwright-cli type "Water flowers"
playwright-cli press Enter
playwright-cli check e21
playwright-cli screenshot
```

### Example output after a command

```
### Page
- Page URL: https://demo.playwright.dev/todomvc/#/
- Page Title: React - TodoMVC

### Snapshot
[Snapshot](.playwright-cli/page-2026-02-14T19-22-42-679Z.yml)
```

The snapshot contains the accessibility tree with element refs (e.g. `e5`, `e21`) for
deterministic follow-up commands.

### Core flow

1. Open a URL via `playwright-cli open <url>`
2. The snapshot provides the accessibility tree with element refs
3. Interact using refs: `click`, `type`, `fill`
4. Another snapshot provides the updated state with new refs

---

## Installation

### Prerequisites

- Node.js 20 or newer
- A coding agent (Claude Code, GitHub Copilot or equivalent)

### Global installation

```bash
npm install -g @playwright/cli@latest
playwright-cli --help
```

### Local usage (without a global installation)

```bash
npx playwright-cli --help
```

### Installing browsers

The first invocation downloads the default browser automatically. For an explicit installation:

```bash
playwright-cli install-browser               # default (Chromium)
playwright-cli install-browser firefox       # specific browser
playwright-cli install-browser --with-deps   # incl. system dependencies (Linux)
```

#### install-browser flags

| Flag | Description |
|------|-------------|
| `--with-deps` | Install system dependencies (Linux) |
| `--dry-run` | Preview: what would be installed |
| `--list` | List available browsers of all installations |
| `--force` | Reinstall, even if already present |
| `--only-shell` | Install only the Chromium headless shell |
| `--no-shell` | Skip the Chromium headless shell |

---

## Skills

### What skills do

Skills teach coding agents the effective use of `playwright-cli` through structured
reference documentation that agents can discover and use.

The installation includes detailed reference guides for:

- Running and debugging Playwright tests
- Request mocking (intercepting/mocking network requests)
- Running Playwright code (arbitrary scripts)
- Browser session management
- Storage state management (cookies, localStorage)
- Test generation from interactions
- Tracing (recording/inspecting execution traces)
- Video recording of browser sessions
- Inspecting element attributes (beyond snapshots)

### Installing skills

```bash
playwright-cli install --skills
```

### Supported agents

- Claude Code
- GitHub Copilot
- Cursor
- Any coding agent with support for locally installed skills

### Operating without skills

Alternatively the agent can discover the commands itself:

```bash
playwright-cli --help
```

### Session preset via environment variable

```bash
PLAYWRIGHT_CLI_SESSION=todo-app claude .
```

---

## All commands — overview

### Core commands
`open [url]`, `close`, `click <ref>`, `dblclick <ref>`, `fill <ref> <text>`, `type <text>`,
`select <ref> <val>`, `check <ref>`, `uncheck <ref>`, `hover <ref>`, `drag <start> <end>`,
`upload <file>`, `snapshot`, `screenshot [ref]`, `pdf`, `eval <func> [ref]`, `resize <w> <h>`,
`dialog-accept [prompt]`, `dialog-dismiss`

### Navigation
`go-back`, `go-forward`, `reload`

### Keyboard & mouse
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

### Network
`network`, `route <pattern> [opts]`, `route-list`, `unroute [pattern]`

### DevTools
`console [min-level]`, `run-code <code>`, `tracing-start`, `tracing-stop`,
`video-start [file]`, `video-chapter <title>`, `video-stop`, `show`

### Sessions
`-s=<name> <cmd>`, `list`, `close-all`, `kill-all`, `delete-data`

---

Source: https://playwright.dev/agent-cli/introduction · https://playwright.dev/agent-cli/quick-start · https://playwright.dev/agent-cli/installation · https://playwright.dev/agent-cli/skills
