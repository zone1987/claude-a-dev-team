# Playwright Agent CLI — Network & Routing

## Contents

- [Command overview](#command-overview)
- [network](#network)
- [route](#route)
- [route-list](#route-list)
- [unroute](#unroute)
- [network-state-set](#network-state-set)
- [Complete test workflow](#complete-test-workflow)

## Command overview

| Command | Description |
|--------|-------------|
| `network` | List network requests since the page was loaded |
| `route <pattern> [options]` | Mock requests for a URL pattern |
| `route-list` | List active mock routes |
| `unroute [pattern]` | Remove mock route(s) |
| `network-state-set <state>` | Set the online/offline state |

---

## network

```bash
playwright-cli network
playwright-cli network --filter="api"
playwright-cli network --static
playwright-cli network --request-body
playwright-cli network --request-headers
playwright-cli network --clear
```

### network options

| Option | Type | Default | Description |
|--------|-----|---------|-------------|
| `--filter=<pattern>` | string | — | URL pattern used as a filter (substring match) |
| `--static` | flag | false | Include static resources (images, CSS, fonts) |
| `--request-body` | flag | false | Include request bodies |
| `--request-headers` | flag | false | Include request headers |
| `--clear` | flag | false | Clear the log |

---

## route

```bash
playwright-cli route "**/api/users" \
  --body='[{"name":"Alice"},{"name":"Bob"}]' \
  --content-type=application/json

playwright-cli route "**/api/data" --status=500
playwright-cli route "**/api/data" --status=503
playwright-cli route "**/*.jpg" --status=404
playwright-cli route "**/analytics/**" --status=204
playwright-cli route "**/*" --remove-header=cookie,authorization
```

### route arguments and options

| Argument/Option | Type | Required | Default | Description |
|-----------------|-----|---------|---------|-------------|
| `<pattern>` | string | Yes | — | Glob pattern of the URLs to intercept (e.g. `**/api/**`) |
| `--status=<code>` | number | No | 200 | HTTP status code of the mock response |
| `--body=<text>` | string | No | `""` | Response body (text or JSON string) |
| `--content-type=<type>` | string | No | `text/plain` | Content-Type header of the response |
| `--header=<name:value>` | string | No | — | Additional response header (repeatable) |
| `--remove-header=<names>` | string | No | — | Comma-separated header names to remove from the request |

### route usage examples

**Mocking an API response:**

```bash
playwright-cli route "**/api/users" \
  --body='[{"id":1,"name":"Alice"},{"id":2,"name":"Bob"}]' \
  --content-type=application/json
```

**Testing error handling:**

```bash
playwright-cli route "**/api/data" --status=500
playwright-cli route "**/api/timeout" --status=503
```

**Blocking resources:**

```bash
playwright-cli route "**/*.jpg" --status=404
playwright-cli route "**/analytics/**" --status=204
playwright-cli route "**/ads/**" --status=204
```

**Removing authentication headers:**

```bash
playwright-cli route "**/*" --remove-header=cookie,authorization
```

**Complex scenarios with run-code:**

Use `run-code` for conditional responses, delays or request body inspection.

---

## route-list

```bash
playwright-cli route-list
```

Lists all active mock routes. No arguments.

---

## unroute

```bash
playwright-cli unroute "**/api/users"   # Remove a specific route
playwright-cli unroute                  # Remove all routes
```

### unroute arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `[pattern]` | string | No | Glob pattern of the route to remove; without an argument, remove all |

---

## network-state-set

```bash
playwright-cli network-state-set offline   # Go offline
playwright-cli reload                      # The page shows its offline state
playwright-cli network-state-set online    # Restore the connection
```

### network-state-set arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<state>` | string | Yes | `online` or `offline` |

---

## Complete test workflow

```bash
# Load the page and inspect the network
playwright-cli open https://app.example.com
playwright-cli network

# Mock the API
playwright-cli route "**/api/products" \
  --body='[{"id":1,"name":"Widget","price":9.99}]' \
  --content-type=application/json

playwright-cli reload
playwright-cli snapshot

# Check the active routes
playwright-cli route-list

# Test error handling
playwright-cli route "**/api/products" --status=500
playwright-cli reload
playwright-cli screenshot --filename=error-state.png

# Remove all routes
playwright-cli unroute

# Test offline behavior
playwright-cli network-state-set offline
playwright-cli reload
playwright-cli screenshot --filename=offline.png
playwright-cli network-state-set online
```

---

Source: https://playwright.dev/agent-cli/commands/network-routing
