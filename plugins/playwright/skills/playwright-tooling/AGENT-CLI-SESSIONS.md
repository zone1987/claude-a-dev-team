# Playwright Agent CLI — Sessions & dashboard

## Contents

- [Overview](#overview)
- [Named sessions](#named-sessions)
- [Default session via environment variable](#default-session-via-environment-variable)
- [Profile persistence](#profile-persistence)
- [Session management commands](#session-management-commands)
- [Dashboard](#dashboard)
- [State management](#state-management)
- [Isolated test workflow (example)](#isolated-test-workflow-example)

## Overview

By default the CLI keeps the browser profile in memory — cookies and storage state
persist between CLI invocations within a session, but are lost when the
browser is closed.

---

## Named sessions

Multiple isolated browser instances can run at the same time, each with:
- its own browser process
- its own cookies
- its own localStorage
- its own navigation history
- its own console log

```bash
playwright-cli open https://playwright.dev
playwright-cli -s=example open https://example.com --persistent
playwright-cli list
```

### Session flag

| Flag | Description |
|------|-------------|
| `-s=<name>` | Use a named session for this command |

---

## Default session via environment variable

Preset the session name for all CLI commands within an agent process:

```bash
PLAYWRIGHT_CLI_SESSION=todo-app claude .
```

---

## Profile persistence

### In-memory (default)

Profile data is only retained during the active session and is lost when it closes.

```bash
playwright-cli open https://example.com
```

### Persistent (on disk)

The profile is stored and survives browser restarts.

```bash
playwright-cli open https://example.com --persistent
```

Default storage locations:

| Platform | Path |
|-----------|------|
| macOS | `~/Library/Caches/ms-playwright/mcp-{channel}-profile` |
| Linux | `~/.cache/ms-playwright/mcp-{channel}-profile` |
| Windows | `%LOCALAPPDATA%\ms-playwright\mcp-{channel}-profile` |

### Custom directory

```bash
playwright-cli open https://example.com --profile=./my-profile
```

---

## Session management commands

| Command | Description |
|--------|-------------|
| `playwright-cli list` | List all sessions |
| `playwright-cli -s=<name> close` | Close a specific session |
| `playwright-cli close-all` | Close all browsers |
| `playwright-cli kill-all` | Force-terminate unresponsive browsers |
| `playwright-cli -s=<name> delete-data` | Delete profile data |

---

## Dashboard

```bash
playwright-cli show
```

Shows a session grid with:
- live screencast of all sessions
- session details with remote input options
- monitoring, taking over on errors, session management

---

## State management

```bash
playwright-cli state-save auth-state.json   # Save the authenticated state
playwright-cli state-load auth-state.json   # Restore the state in a new session
```

---

## Isolated test workflow (example)

Separate admin and user sessions with persistent authentication and simultaneous
monitoring of both sessions via the dashboard:

```bash
# Set up the admin session
playwright-cli -s=admin open https://app.example.com/login --persistent
playwright-cli -s=admin fill e3 "admin@example.com"
playwright-cli -s=admin fill e5 "admin-password"
playwright-cli -s=admin click e7
playwright-cli -s=admin state-save admin-auth.json

# Set up the user session
playwright-cli -s=user open https://app.example.com/login --persistent
playwright-cli -s=user fill e3 "user@example.com"
playwright-cli -s=user fill e5 "user-password"
playwright-cli -s=user click e7

# Monitor both sessions at the same time
playwright-cli show

# Check the session list
playwright-cli list
```

---

Source: https://playwright.dev/agent-cli/sessions
