# Playwright Agent CLI — Navigation

## Contents

- [Command overview](#command-overview)
- [open](#open)
- [goto](#goto)
- [go-back / go-forward](#go-back-go-forward)
- [reload](#reload)
- [close](#close)
- [Complete navigation workflow](#complete-navigation-workflow)

## Command overview

| Command | Description |
|--------|-------------|
| `open [url]` | Open the browser, optionally navigating to a URL |
| `goto <url>` | Navigate to a URL |
| `go-back` | Go back to the previous page |
| `go-forward` | Go forward to the next page |
| `reload` | Reload the current page |
| `close` | Close the browser |

---

## open

```bash
playwright-cli open
playwright-cli open https://example.com
playwright-cli open https://example.com --headed
playwright-cli open https://example.com --browser=firefox
playwright-cli open https://example.com --persistent
playwright-cli open https://example.com --profile=./my-profile
playwright-cli open https://example.com --config=config.json
```

### open options

| Option | Type | Default | Description |
|--------|-----|---------|-------------|
| `[url]` | string | — | URL to open (optional) |
| `--headed` | flag | false | Show the browser window |
| `--browser=<name>` | string | `chrome` | Browser: `chrome`, `firefox`, `webkit`, `msedge` |
| `--persistent` | flag | false | Store the profile on disk |
| `--profile=<path>` | string | — | Custom profile directory |
| `--config=<file>` | string | — | Path to a JSON configuration file |

---

## goto

```bash
playwright-cli goto https://demo.playwright.dev/todomvc
```

### goto arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<url>` | string | Yes | Full URL including the protocol |

Output: page information (URL, title) and a snapshot file reference.

---

## go-back / go-forward

```bash
playwright-cli goto https://example.com/page1
playwright-cli goto https://example.com/page2
playwright-cli go-back
playwright-cli go-forward
```

No arguments or options.

---

## reload

```bash
playwright-cli reload
```

No arguments. Reloads the current page.

---

## close

```bash
playwright-cli close          # Close the current browser
playwright-cli close-all      # Close all sessions
```

---

## Complete navigation workflow

```bash
playwright-cli open https://example.com --headed --browser=firefox
playwright-cli goto https://example.com/products
playwright-cli goto https://example.com/products/123
playwright-cli go-back
playwright-cli goto https://example.com/products/456
playwright-cli reload
playwright-cli close
```

---

Source: https://playwright.dev/agent-cli/commands/navigation
