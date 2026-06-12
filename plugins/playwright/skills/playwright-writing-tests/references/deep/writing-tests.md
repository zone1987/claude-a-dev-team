# Playwright: Tests schreiben, ausfuehren, Codegen, VS Code

## Test-Struktur

### Minimaler Test

```typescript
import { test, expect } from '@playwright/test';

test('Seitentitel pruefen', async ({ page }) => {
  await page.goto('https://playwright.dev/');
  await expect(page).toHaveTitle(/Playwright/);
});
```

### Test-Fixtures

Jeder Test erhaelt automatisch isolierte Fixtures:
- `page` — neue Seite in einem frischen `BrowserContext`
- `context` — isolierter `BrowserContext`
- `browser` — gemeinsamer Browser-Prozess

---

## test() — Funktion

```typescript
test(title: string, fn: (fixtures) => Promise<void>): void
test(title: string, details: TestDetails, fn: (fixtures) => Promise<void>): void
```

Jeder Test laeuft in einem frischen, isolierten `BrowserContext` (automatische Isolation).

---

## test.describe() — Gruppierung

```typescript
test.describe('Gruppe', () => {
  test('Test 1', async ({ page }) => { /* ... */ });
  test('Test 2', async ({ page }) => { /* ... */ });
});

// Verschachtelt
test.describe('Aeussere Gruppe', () => {
  test.describe('Innere Gruppe', () => {
    test('tief verschachtelter Test', async ({ page }) => { /* ... */ });
  });
});
```

---

## Hooks

```typescript
test.describe('Mit Hooks', () => {
  test.beforeAll(async () => {
    // Einmalig vor allen Tests der Gruppe (kein page-Fixture hier)
  });

  test.afterAll(async () => {
    // Einmalig nach allen Tests der Gruppe
  });

  test.beforeEach(async ({ page }) => {
    // Vor jedem Test; page-Fixture verfuegbar
    await page.goto('https://playwright.dev/');
  });

  test.afterEach(async ({ page }) => {
    // Nach jedem Test
  });

  test('erster Test', async ({ page }) => {
    await expect(page).toHaveTitle(/Playwright/);
  });
});
```

---

## Seitennavigation

```typescript
await page.goto('https://example.com');
// Playwright wartet auf den Load-State vor dem Fortfahren
```

---

## Interaktionen (Kurzreferenz)

| Aktion | Methode |
|---|---|
| Klicken | `await locator.click()` |
| Text eingeben | `await locator.fill('text')` |
| Checkbox aktivieren | `await locator.check()` |
| Checkbox deaktivieren | `await locator.uncheck()` |
| Hover | `await locator.hover()` |
| Fokussieren | `await locator.focus()` |
| Taste druecken | `await locator.press('Enter')` |
| Datei hochladen | `await locator.setInputFiles('/pfad/datei.pdf')` |
| Option auswaehlen | `await locator.selectOption('wert')` |

---

## expect() — Assertions

### Web-First Assertions (mit `await` — haben Auto-Retry)

Diese Assertions warten, bis die Bedingung erfuellt ist oder ein Timeout eintritt.

| Assertion | Prueft |
|---|---|
| `await expect(locator).toBeChecked()` | Checkbox ist aktiviert |
| `await expect(locator).toBeChecked({ checked: false })` | Checkbox ist deaktiviert |
| `await expect(locator).toBeDisabled()` | Element ist deaktiviert |
| `await expect(locator).toBeEditable()` | Element ist editierbar |
| `await expect(locator).toBeEmpty()` | Element hat keinen Text / leeres Input |
| `await expect(locator).toBeEnabled()` | Element ist aktiviert |
| `await expect(locator).toBeFocused()` | Element hat den Fokus |
| `await expect(locator).toBeHidden()` | Element ist nicht sichtbar |
| `await expect(locator).toBeInViewport()` | Element ist im Viewport |
| `await expect(locator).toBeVisible()` | Element ist sichtbar |
| `await expect(locator).toContainText('text')` | Element enthaelt Text (Teil) |
| `await expect(locator).toContainText(/regex/)` | Element enthaelt Text (Regex) |
| `await expect(locator).toHaveAttribute('name', 'wert')` | Element hat Attribut mit Wert |
| `await expect(locator).toHaveClass('klasse')` | Element hat CSS-Klasse |
| `await expect(locator).toHaveCount(n)` | Anzahl der Elemente |
| `await expect(locator).toHaveCSS('prop', 'wert')` | Berechnetes CSS |
| `await expect(locator).toHaveId('id')` | Element-ID |
| `await expect(locator).toHaveJSProperty('prop', wert)` | JS-Eigenschaft |
| `await expect(locator).toHaveRole('button')` | ARIA-Rolle |
| `await expect(locator).toHaveText('exakt')` | Exakter Text |
| `await expect(locator).toHaveText(['a', 'b'])` | Texte aller Elemente |
| `await expect(locator).toHaveValue('wert')` | Input-Wert |
| `await expect(locator).toHaveValues(['a', 'b'])` | Mehrfach-Select-Werte |
| `await expect(page).toHaveTitle('Titel')` | Seitentitel |
| `await expect(page).toHaveTitle(/Regex/)` | Seitentitel per Regex |
| `await expect(page).toHaveURL('https://...')` | Seiten-URL |
| `await expect(page).toHaveURL(/regex/)` | Seiten-URL per Regex |
| `await expect(response).toBeOK()` | HTTP-Response ist OK (2xx) |

#### Negation

```typescript
await expect(locator).not.toBeVisible();
await expect(page).not.toHaveURL(/error/);
```

#### Optionen fuer alle Web-First Assertions

```typescript
await expect(locator).toBeVisible({ timeout: 5000 }); // ms, Default: 5000
```

| Option | Typ | Default | Beschreibung |
|---|---|---|---|
| `timeout` | `number` | `5000` | Max. Wartezeit in ms |
| `message` | `string` | — | Benutzerdefinierte Fehlermeldung |

### Synchrone Assertions (ohne `await` — kein Retry)

```typescript
expect(value).toEqual(erwarteterWert);
expect(array).toContain(element);
expect(value).toBeTruthy();
expect(value).toBeFalsy();
expect(value).toBeNull();
expect(value).toBeDefined();
expect(number).toBeGreaterThan(n);
expect(number).toBeLessThan(n);
expect(string).toMatch(/regex/);
```

### Soft Assertions

Sammeln Fehler, ohne den Test sofort abzubrechen:

```typescript
await expect.soft(locator).toHaveText('erwartet');
await expect.soft(locator2).toBeVisible();
// Test laeuft weiter, auch wenn Assertions fehlschlagen
```

---

## Vollstaendiges Test-Beispiel

```typescript
import { test, expect } from '@playwright/test';

test.describe('Todo-App', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('https://demo.playwright.dev/todomvc');
  });

  test('Todo hinzufuegen', async ({ page }) => {
    await page.getByPlaceholder('What needs to be done?').fill('Einkaufen');
    await page.getByPlaceholder('What needs to be done?').press('Enter');

    await expect(page.getByTestId('todo-title')).toHaveText('Einkaufen');
    await expect(page.getByRole('listitem')).toHaveCount(1);
  });

  test('Todo abschliessen', async ({ page }) => {
    await page.getByPlaceholder('What needs to be done?').fill('Aufgabe');
    await page.getByPlaceholder('What needs to be done?').press('Enter');
    await page.getByRole('checkbox').first().check();

    await expect(page.getByRole('checkbox').first()).toBeChecked();
  });
});
```

---

## CLI: Tests ausfuehren

### Grundbefehle

```bash
npx playwright test                       # Alle Tests headless
npx playwright test --headed              # Mit sichtbarem Browser
npx playwright test --ui                  # UI-Modus (Watch + Live-Debug)
npx playwright test --debug               # Inspector-Debugging
npx playwright show-report                # HTML-Report anzeigen
```

### Filter und Selektion

| Flag | Beschreibung | Beispiel |
|---|---|---|
| `<datei>` | Bestimmte Datei ausfuehren | `npx playwright test login.spec.ts` |
| `<dir1> <dir2>` | Mehrere Verzeichnisse | `npx playwright test tests/auth/ tests/shop/` |
| `<keyword>` | Dateiname enthaelt Keyword | `npx playwright test login home` |
| `-g "titel"` | Test-Titel per grep | `npx playwright test -g "add a todo"` |
| `--last-failed` | Nur zuletzt fehlgeschlagene | `npx playwright test --last-failed` |

### Browser und Parallelisierung

| Flag | Beschreibung | Beispiel |
|---|---|---|
| `--project <name>` | Bestimmtes Browser-Projekt | `npx playwright test --project webkit` |
| `--project a --project b` | Mehrere Projekte | `npx playwright test --project webkit --project firefox` |

### Ausgabe und Reporting

| Flag | Beschreibung |
|---|---|
| `--reporter=html` | HTML-Reporter |
| `--reporter=list` | Listen-Reporter |
| `--reporter=dot` | Kompakter Dot-Reporter |

---

## Codegen: Test-Recorder

### Grundbefehl

```bash
npx playwright codegen [URL]
# URL ist optional; kann auch im Browserfenster eingegeben werden
```

Oeffnet zwei Fenster:
1. Interaktiven Browser fuer Aktionen
2. Playwright Inspector mit generiertem Code

### Alle CLI-Flags

| Flag | Typ | Beschreibung | Beispiel |
|---|---|---|---|
| `--viewport-size` | `string` | Viewport-Groesse | `--viewport-size="800,600"` |
| `--device` | `string` | Geraete-Emulation | `--device="iPhone 13"` |
| `--color-scheme` | `string` | `dark` oder `light` | `--color-scheme=dark` |
| `--timezone` | `string` | Zeitzone | `--timezone="Europe/Berlin"` |
| `--geolocation` | `string` | GPS-Koordinaten | `--geolocation="52.52,13.40"` |
| `--lang` | `string` | Sprache/Locale | `--lang="de-DE"` |
| `--save-storage` | `string` | Auth-Zustand speichern | `--save-storage=auth.json` |
| `--load-storage` | `string` | Auth-Zustand laden | `--load-storage=auth.json` |
| `--user-data-dir` | `string` | Browser-Profilverzeichnis | `--user-data-dir=/pfad/profil` |

### Assertion-Typen im Recorder

| Typ | Prueft |
|---|---|
| Assert Visibility | Element sichtbar/unsichtbar |
| Assert Text | Bestimmten Text-Inhalt |
| Assert Value | Wert eines Inputs |

### Inspector-Steuerung

| Schaltflaeche | Funktion |
|---|---|
| Record | Aufnahme ein-/ausschalten |
| Copy | Generierten Code kopieren |
| Clear | Code zuruecksetzen / neue Aufnahme |
| Pick Locator | Element-Selektor auswaehlen |

### Auth-Zustand speichern und laden

```bash
# Login aufzeichnen und Auth speichern
npx playwright codegen github.com/login --save-storage=auth.json

# Spa	ter mit gespeichertem Auth weiterarbeiten
npx playwright codegen --load-storage=auth.json github.com/dashboard
```

### Codegen in eigenem Context (page.pause())

```typescript
import { chromium } from '@playwright/test';

(async () => {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext();
  // Eigene Routing-/Interzeptions-Logik
  await context.route('**/*', route => route.continue());
  const page = await context.newPage();
  // Oeffnet den Inspector innerhalb des eigenen Contexts
  await page.pause();
})();
```

---

## VS Code Extension

### Installation

1. Extensions (`Cmd+Shift+X`) oeffnen, "Playwright" suchen, Microsoft-Extension installieren
2. Command Palette (`Cmd+Shift+P`) → `Test: Install Playwright`
3. Browser auswaehlen (Chromium / Firefox / WebKit), optional GitHub Actions

### Tests ausfuehren

| Aktion | Methode |
|---|---|
| Einzeltest | Gruenes Play-Icon neben dem Test anklicken |
| Mehrere Tests | Play-Icon auf Datei- oder Projektebene |
| Multi-Browser | Projekte in der Playwright-Sidebar auswaehlen |
| Browserfenster sichtbar | "Show Browsers" in Sidebar aktivieren |

### Debugging

| Funktion | Beschreibung |
|---|---|
| Breakpoints | Gutter-Zeile anklicken, dann Rechtsklick → "Debug Test" |
| Live-Inspektion | Mit "Show Browsers": Lokator anklicken = Element hervorheben |
| Fehler-Details | "expected vs. received" + vollstaendiger Call-Log |
| AI-Hilfe | Sparkle-Icon: Copilot-Vorschlaege fuer Fehlerursachen |
| Trace Viewer | "Show Trace Viewer": Timeline + DOM-Snapshots + Netzwerk |

### Test-Aufnahme (CodeGen in VS Code)

| Funktion | Beschreibung |
|---|---|
| Record new | Neuen Test aufzeichnen → `test-1.spec.ts` |
| Record at cursor | Aktionen an Cursor-Position anhaengen |
| Pick locator | Element klicken → optimaler Lokator in Zwischenablage |

### Konfiguration wechseln

Zahnrad-Icon in der Sidebar: Zwischen mehreren `playwright.config.ts`-Dateien wechseln.

<!-- Quellen:
https://playwright.dev/docs/writing-tests
https://playwright.dev/docs/running-tests
https://playwright.dev/docs/codegen-intro
https://playwright.dev/docs/codegen
https://playwright.dev/docs/getting-started-vscode
-->
