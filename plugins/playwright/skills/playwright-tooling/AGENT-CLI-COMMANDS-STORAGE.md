# Playwright Agent CLI — Storage & Authentication

## Contents

- [Command overview](#command-overview)
- [state-save / state-load](#state-save-state-load)
- [Cookies](#cookies)
- [localStorage](#localstorage)
- [sessionStorage](#sessionstorage)

## Command overview

| Group | Command | Description |
|--------|--------|-------------|
| State | `state-save [filename]` | Save the complete browser state (cookies + localStorage) |
| State | `state-load <filename>` | Restore state from a file |
| Cookies | `cookie-list` | List all cookies |
| Cookies | `cookie-get <name>` | Retrieve a specific cookie |
| Cookies | `cookie-set <name> <value>` | Create/modify a cookie |
| Cookies | `cookie-delete <name>` | Delete a cookie |
| Cookies | `cookie-clear` | Delete all cookies |
| localStorage | `localstorage-list` | List all key-value pairs |
| localStorage | `localstorage-get <key>` | Retrieve a value by key |
| localStorage | `localstorage-set <key> <value>` | Set a value |
| localStorage | `localstorage-delete <key>` | Delete a key |
| localStorage | `localstorage-clear` | Clear the entire storage |
| sessionStorage | `sessionstorage-list` | List all key-value pairs |
| sessionStorage | `sessionstorage-get <key>` | Retrieve a value by key |
| sessionStorage | `sessionstorage-set <key> <value>` | Set a value |
| sessionStorage | `sessionstorage-delete <key>` | Delete a key |
| sessionStorage | `sessionstorage-clear` | Clear the entire storage |

---

## state-save / state-load

Saves and restores the complete browser state (cookies + localStorage) in a
file.

```bash
playwright-cli state-save                         # automatically named file
playwright-cli state-save auth.json               # custom file name
playwright-cli state-load auth.json               # restore
```

### state-save arguments

| Argument | Type | Required | Default | Description |
|----------|-----|---------|---------|-------------|
| `[filename]` | string | No | Auto-generated | Target file (JSON) |

### state-load arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<filename>` | string | Yes | Source file (JSON) |

### Authentication persistence (example)

```bash
playwright-cli open https://app.example.com/login
playwright-cli fill e3 "user@example.com"
playwright-cli fill e5 "password123"
playwright-cli click e7
playwright-cli state-save auth.json

# Later: load the state and navigate directly to the protected page
playwright-cli state-load auth.json
playwright-cli goto https://app.example.com/dashboard
```

---

## Cookies

### cookie-list

```bash
playwright-cli cookie-list
playwright-cli cookie-list --domain=.github.com
playwright-cli cookie-list --path=/app
```

#### cookie-list options

| Option | Type | Description |
|--------|-----|-------------|
| `--domain=<domain>` | string | Filter by domain |
| `--path=<path>` | string | Filter by path |

### cookie-get

```bash
playwright-cli cookie-get session_id
playwright-cli cookie-get auth_token
```

#### cookie-get arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<name>` | string | Yes | Name of the cookie to retrieve |

### cookie-set

```bash
playwright-cli cookie-set theme light
playwright-cli cookie-set session abc123 --domain=.example.com --secure --http-only
playwright-cli cookie-set prefs "{\"lang\":\"de\"}" --domain=.example.com
playwright-cli cookie-set consent true --expires=1735689600 --same-site=Strict
```

#### cookie-set arguments and options

| Argument/Option | Type | Required | Default | Description |
|-----------------|-----|---------|---------|-------------|
| `<name>` | string | Yes | — | Cookie name |
| `<value>` | string | Yes | — | Cookie value |
| `--domain=<domain>` | string | No | Current domain | Cookie domain |
| `--path=<path>` | string | No | `/` | Cookie path |
| `--expires=<timestamp>` | number | No | Session | Unix timestamp for expiry |
| `--http-only` | flag | No | false | HTTP-Only flag (no JavaScript access) |
| `--secure` | flag | No | false | Secure flag (HTTPS only) |
| `--same-site=<value>` | string | No | — | `Strict`, `Lax` or `None` |

### cookie-delete

```bash
playwright-cli cookie-delete session_id
playwright-cli cookie-delete auth_token
```

### cookie-clear

```bash
playwright-cli cookie-clear
```

---

## localStorage

### localstorage-list

```bash
playwright-cli localstorage-list
```

### localstorage-get

```bash
playwright-cli localstorage-get user_preferences
playwright-cli localstorage-get theme
```

### localstorage-set

```bash
playwright-cli localstorage-set onboarding_done "false"
playwright-cli localstorage-set theme "dark"
playwright-cli localstorage-set user_prefs '{"lang":"de","currency":"EUR"}'
playwright-cli reload      # Reload the page to activate the change
```

### localstorage-delete

```bash
playwright-cli localstorage-delete user_preferences
```

### localstorage-clear

```bash
playwright-cli localstorage-clear
```

---

## sessionStorage

Note: data is deleted when the tab is closed.

```bash
playwright-cli sessionstorage-list
playwright-cli sessionstorage-get wizard_step
playwright-cli sessionstorage-set wizard_step "3"
playwright-cli sessionstorage-delete temp_data
playwright-cli sessionstorage-clear
```

All commands take identical arguments to their localStorage equivalents.

---

Source: https://playwright.dev/agent-cli/commands/storage
