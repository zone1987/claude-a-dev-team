# Playwright Agent CLI — Console & Eval

## Befehlsuebersicht

| Befehl | Beschreibung |
|--------|-------------|
| `console [level]` | Console-Nachrichten anzeigen |
| `eval <expression> [ref]` | JavaScript im Kontext der Seite oder eines Elements ausfuehren |
| `run-code <code>` | Playwright-Code ausfuehren |
| `run-code --filename=<datei>` | Playwright-Code aus Datei ausfuehren |

---

## console

```bash
playwright-cli console
playwright-cli console error
playwright-cli console warning
playwright-cli console debug
playwright-cli console --clear
```

### console-Argumente und Optionen

| Argument/Option | Typ | Pflicht | Standard | Beschreibung |
|-----------------|-----|---------|---------|-------------|
| `[level]` | string | Nein | `info` | Mindest-Level: `error`, `warning`, `info`, `debug` |
| `--clear` | flag | Nein | false | Nachrichten-Buffer leeren |

### Level-Verhalten

| Level-Argument | Zeigt an |
|----------------|---------|
| (kein) | info und hoeher |
| `error` | Nur Fehler |
| `warning` | Warnungen und Fehler |
| `debug` | Alle Nachrichten |

### Beispielausgabe

```
$ playwright-cli console error
[error] Uncaught TypeError: Cannot read property 'map' of undefined
  at app.js:42:15
[error] Failed to fetch: GET /api/users 404
```

### Debugging-Workflow

```bash
playwright-cli goto https://app.example.com
playwright-cli console error          # Fehler pruefen
playwright-cli network --filter="api" # Problematische Anfragen finden
playwright-cli route "**/api/users" --status=200 --body='[]' --content-type=application/json
playwright-cli reload
playwright-cli console                # Pruefen ob Fehler behoben
```

---

## eval

```bash
# Seiten-Kontext
playwright-cli eval "() => document.title"
playwright-cli eval "() => window.innerWidth + 'x' + window.innerHeight"
playwright-cli eval "() => document.querySelectorAll('button').length"

# Element-Kontext
playwright-cli eval "(el) => el.getAttribute('data-id')" e15
playwright-cli eval "(el) => getComputedStyle(el).color" e15
playwright-cli eval "(el) => el.getBoundingClientRect()" e15
playwright-cli eval "(el) => el.innerHTML" "#main"
```

### eval-Argumente

| Argument | Typ | Pflicht | Beschreibung |
|----------|-----|---------|-------------|
| `<expression>` | string | Ja | JavaScript-Ausdruck als Pfeil-Funktion (`() => ...` oder `(el) => ...`) |
| `[ref]` | string | Nein | Element-Ref oder CSS-Selektor; wenn angegeben, wird `el` uebergeben |

Gibt den Rueckgabewert der Funktion aus.

---

## run-code

```bash
# Inline-Code
playwright-cli run-code "await page.evaluate(() => navigator.geolocation)"

# Aus Datei
playwright-cli run-code --filename=script.js
playwright-cli run-code --filename=setup.ts
```

### run-code-Argumente und Optionen

| Argument/Option | Typ | Pflicht | Beschreibung |
|-----------------|-----|---------|-------------|
| `<code>` | string | Ja* | Playwright-Code als String (alternativ zu `--filename`) |
| `--filename=<datei>` | string | Ja* | Pfad zur JavaScript/TypeScript-Datei |

*Entweder `<code>` oder `--filename` muss angegeben werden.

### run-code Anwendungsbeispiele

**Geolocation setzen:**

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

**Auf DOM-Bedingung warten:**

```javascript
// wait-for.js
await page.waitForFunction(() =>
  document.querySelectorAll('.item').length > 5
);
```

**Strukturierte Daten scrapen:**

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

Quelle: https://playwright.dev/agent-cli/commands/console-eval
