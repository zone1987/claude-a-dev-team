# Playwright Agent CLI — Attach

## Contents

- [Command overview](#command-overview)
- [attach --cdp (channel name)](#attach---cdp-channel-name)
- [attach --cdp (URL/endpoint)](#attach---cdp-urlendpoint)
- [attach --endpoint](#attach---endpoint)
- [attach --extension](#attach---extension)
- [Named sessions with attach](#named-sessions-with-attach)
- [Complete workflows](#complete-workflows)

## Command overview

| Command | Description |
|--------|-------------|
| `attach --cdp=<channel>` | Connect to a running browser by channel name |
| `attach --cdp=<url>` | Connect via Chrome DevTools Protocol endpoint |
| `attach --endpoint=<url>` | Connect to a Playwright server endpoint |
| `attach --extension` | Connect via the Playwright extension (default: Chrome) |
| `attach --extension=<channel>` | Connect via the Playwright extension with a specific channel |
| `attach <session-name>` | Connect to a paused test (test debugging) |

---

## attach --cdp (channel name)

Connects to running Chrome or Edge instances. The browser must have remote debugging enabled:
Chrome: `chrome://inspect/#remote-debugging` → enable "Allow remote debugging for this browser instance".

### Supported channels

| Channel | Description |
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

## attach --cdp (URL/endpoint)

Connects to Chromium-based browsers via a CDP endpoint:

```bash
# Start the browser with remote debugging
google-chrome --remote-debugging-port=9222

# Connect
playwright-cli attach --cdp=http://localhost:9222
playwright-cli snapshot
playwright-cli click e5
```

### attach --cdp options

| Option | Type | Required | Description |
|--------|-----|---------|-------------|
| `--cdp=<channel\|url>` | string | Yes | Channel name (`chrome`, `msedge`, etc.) or a full CDP URL |

### Compatible with

- Chrome/Chromium with `--remote-debugging-port`
- Edge with remote debugging
- Electron apps that expose CDP
- Cloud browser services (Browserbase, etc.)

---

## attach --endpoint

Connects to a Playwright server endpoint:

```bash
playwright-cli attach --endpoint=ws://localhost:3000
playwright-cli snapshot
```

### attach --endpoint options

| Option | Type | Required | Description |
|--------|-----|---------|-------------|
| `--endpoint=<url>` | string | Yes | WebSocket URL of the Playwright server |

---

## attach --extension

Connects through the Playwright extension for existing browser sessions
(including cookies, extensions, logged-in sessions):

```bash
playwright-cli attach --extension
playwright-cli attach --extension=chrome-canary
playwright-cli attach --extension=msedge
playwright-cli attach --extension=msedge-dev
```

### attach --extension options

| Option | Type | Required | Default | Description |
|--------|-----|---------|---------|-------------|
| `--extension[=<channel>]` | string | — | `chrome` | Browser channel for the extension connection |

### Use cases

| Scenario | Benefit |
|----------|---------|
| Bypass SSO/2FA authentication | Reuse the existing login session |
| Integrate browser extensions | Extensions run as they do for a normal user |
| Automate an existing tab | No new browser launch required |

---

## Named sessions with attach

```bash
playwright-cli attach --cdp=chrome -s=debug-session
playwright-cli -s=debug-session snapshot
playwright-cli -s=debug-session click e5
```

### Session flag

| Flag | Type | Description |
|------|-----|-------------|
| `-s=<name>` | string | Session name for this attach command |

---

## Complete workflows

### Connecting to a running Chrome

```bash
playwright-cli attach --cdp=chrome
playwright-cli snapshot
playwright-cli screenshot --filename=current-state.png
playwright-cli state-save auth.json
```

### Remote browser debugging (SSH tunnel)

```bash
# On the remote server
google-chrome --remote-debugging-port=9222

# Local SSH tunnel
ssh -L 9222:localhost:9222 user@remote-host

# Connect
playwright-cli attach --cdp=http://localhost:9222
playwright-cli snapshot
playwright-cli screenshot --filename=remote-state.png
playwright-cli console error
```

### CDP connection to an Electron app

```bash
# Electron must expose CDP (e.g. --remote-debugging-port=9229)
playwright-cli attach --cdp=http://localhost:9229
playwright-cli snapshot
playwright-cli click e10
```

---

Source: https://playwright.dev/agent-cli/commands/attach
