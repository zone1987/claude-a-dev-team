# Playwright Agent CLI — Console & Eval

## Contents

- [Command overview](#command-overview)
- [console](#console)
- [eval](#eval)
- [run-code](#run-code)

## Command overview

| Command | Description |
|--------|-------------|
| `console [level]` | Show console messages |
| `eval <expression> [ref]` | Execute JavaScript in the context of the page or an element |
| `run-code <code>` | Execute Playwright code |
| `run-code --filename=<file>` | Execute Playwright code from a file |

---

## console

```bash
playwright-cli console
playwright-cli console error
playwright-cli console warning
playwright-cli console debug
playwright-cli console --clear
```

### console arguments and options

| Argument/Option | Type | Required | Default | Description |
|-----------------|-----|---------|---------|-------------|
| `[level]` | string | No | `info` | Minimum level: `error`, `warning`, `info`, `debug` |
| `--clear` | flag | No | false | Clear the message buffer |

### Level behavior

| Level argument | Shows |
|----------------|---------|
| (none) | info and higher |
| `error` | Errors only |
| `warning` | Warnings and errors |
| `debug` | All messages |

### Example output

```
$ playwright-cli console error
[error] Uncaught TypeError: Cannot read property 'map' of undefined
  at app.js:42:15
[error] Failed to fetch: GET /api/users 404
```

### Debugging workflow

```bash
playwright-cli goto https://app.example.com
playwright-cli console error          # Check errors
playwright-cli network --filter="api" # Find problematic requests
playwright-cli route "**/api/users" --status=200 --body='[]' --content-type=application/json
playwright-cli reload
playwright-cli console                # Check whether errors are fixed
```

---

## eval

```bash
# Page context
playwright-cli eval "() => document.title"
playwright-cli eval "() => window.innerWidth + 'x' + window.innerHeight"
playwright-cli eval "() => document.querySelectorAll('button').length"

# Element context
playwright-cli eval "(el) => el.getAttribute('data-id')" e15
playwright-cli eval "(el) => getComputedStyle(el).color" e15
playwright-cli eval "(el) => el.getBoundingClientRect()" e15
playwright-cli eval "(el) => el.innerHTML" "#main"
```

### eval arguments

| Argument | Type | Required | Description |
|----------|-----|---------|-------------|
| `<expression>` | string | Yes | JavaScript expression as an arrow function (`() => ...` or `(el) => ...`) |
| `[ref]` | string | No | Element ref or CSS selector; if given, `el` is passed in |

Prints the function's return value.

---

## run-code

```bash
# Inline code
playwright-cli run-code "await page.evaluate(() => navigator.geolocation)"

# From a file
playwright-cli run-code --filename=script.js
playwright-cli run-code --filename=setup.ts
```

### run-code arguments and options

| Argument/Option | Type | Required | Description |
|-----------------|-----|---------|-------------|
| `<code>` | string | Yes* | Playwright code as a string (alternative to `--filename`) |
| `--filename=<file>` | string | Yes* | Path to a JavaScript/TypeScript file |

*Either `<code>` or `--filename` must be provided.

### run-code usage examples

**Setting geolocation:**

```javascript
// geolocation.js
await context.grantPermissions(['geolocation']);
await page.evaluate(() => {
  navigator.geolocation.getCurrentPosition = (cb) =>
    cb({ coords: { latitude: 51.5074, longitude: -0.1278 } });
});
```

```bash
playwright-cli run-code --filename=geolocation.js
```

**Waiting for a DOM condition:**

```javascript
// wait-for.js
await page.waitForFunction(() =>
  document.querySelectorAll('.item').length > 5
);
```

**Scraping structured data:**

```javascript
// scrape.js
const data = await page.$$eval('.product', products =>
  products.map(p => ({
    name: p.querySelector('.name').textContent,
    price: p.querySelector('.price').textContent,
  }))
);
console.log(JSON.stringify(data, null, 2));
```

---

Source: https://playwright.dev/agent-cli/commands/console-eval
