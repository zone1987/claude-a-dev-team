# Playwright Trace Viewer & Debugging

## Traces aufnehmen

### Konfiguration in `playwright.config.ts`

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  retries: 1,
  use: {
    // Trace-Modus waehlen:
    trace: 'on-first-retry',
  },
});
```

### Trace-Optionen

| Wert | Verhalten |
|------|-----------|
| `'off'` | Kein Trace |
| `'on'` | Jeder Test (performance-intensiv) |
| `'retain-on-failure'` | Trace bei jedem Test, loescht Erfolge am Ende |
| `'on-first-retry'` | Nur beim ersten Retry (empfohlen fuer CI) |
| `'on-all-retries'` | Alle Retry-Versuche |

### Trace per CLI erzwingen (lokal)

```bash
npx playwright test --trace on
npx playwright show-report
```

### Trace per Library-API (ohne Test-Runner)

```typescript
const context = await browser.newContext();

// Trace starten
await context.tracing.start({
  screenshots: true,   // Screenshots in Timeline
  snapshots: true,     // DOM-Snapshots bei jeder Aktion
  sources: true,       // Quellcode-Zeilen
});

const page = await context.newPage();
await page.goto('https://example.com');

// Trace stoppen und speichern
await context.tracing.stop({ path: 'trace.zip' });
```

### `tracing.start()` Optionen

| Option | Typ | Default | Beschreibung |
|--------|-----|---------|--------------|
| `screenshots` | boolean | false | Film-Strip-Screenshots aufnehmen |
| `snapshots` | boolean | false | DOM-Snapshots vor/nach jeder Aktion |
| `sources` | boolean | false | Quellcode-Zeilen einbinden |
| `title` | string | — | Optionaler Titel fuer den Trace |

### HAR-Recording (ab v1.60)

```typescript
await context.tracing.startHar({ path: 'network.har' });
// ... Test ausfuehren ...
await context.tracing.stopHar({ path: 'network.har' });
```

---

## Trace Viewer oeffnen

### Per CLI (lokal)

```bash
# Lokale ZIP-Datei
npx playwright show-trace path/to/trace.zip

# Remote URL
npx playwright show-trace https://example.com/trace.zip
```

### Per HTML-Report

```bash
npx playwright show-report
```
Im Report: Trace-Icon neben dem Testdateinamen anklicken.

### Per Web-Interface

URL: **https://trace.playwright.dev**

- Keine externe Datenuebertragung (statisch gehostet)
- Upload per Drag-and-Drop oder Dateiauswahl
- Remote-Trace: `https://trace.playwright.dev/?trace=https://example.com/trace.zip`

---

## Trace Viewer: UI-Tabs und Features

| Tab | Inhalt |
|-----|--------|
| **Actions** | Aktionsliste mit Locators, Timing, DOM-Snapshots (Before/After) |
| **Screenshots** | Film-Strip mit vergroesserter Timeline |
| **Snapshots** | DOM-Zustand: Before / Action / After |
| **Source** | Hervorgehobene Codezeile |
| **Call** | Aktionsdauer, Locator, Strict-Mode-Infos |
| **Log** | Detaillierte Aktionssequenz (Scrollen, Warten, Klicken) |
| **Errors** | Fehlermeldungen mit Timeline-Markierung |
| **Console** | Browser- und Test-Logs mit Quellenkennung |
| **Network** | Requests nach Typ/Status/Methode/Dauer filterbar |
| **Metadata** | Browser, Viewport, Testdauer |
| **Attachments** | Visual-Regression-Vergleiche mit Slider |

### Interaktionen im Viewer

- Doppelklick auf Aktion -> Zeitbereich filtern
- Timeline-Slider zum Auswaehlen von Aktionsbereichen
- Film-Strip hovern fuer vergroesserte Vorschau
- "Show all" zum Zuruecksetzen von Filtern

---

## Playwright Inspector

### Starten

```bash
# Alle Tests debuggen
npx playwright test --debug

# Einzelner Test nach Datei und Zeile
npx playwright test example.spec.ts:10 --debug

# Spezifischer Browser
npx playwright test --project=chromium --debug

# Kombiniert
npx playwright test example.spec.ts:10 --project=webkit --debug
```

### Inspector-Features

- **Playback-Controls**: Schritt vor/zurueck, Play, Pause
- **Aktueller Schritt**: Im Inspector und im Browser hervorgehoben
- **Pick Locator**: Interaktive Elementauswahl mit Echtzeit-Highlighting
- **Locator-Editor**: Live-Bearbeitung des Locators
- **Actionability-Log**: Zeigt Sichtbarkeit, Stabilitaet, Scroll-Notwendigkeit

### Breakpoints im Code

```typescript
// Test bleibt an dieser Stelle stehen
await page.pause();
```

---

## VS Code Debugger

### Voraussetzungen

- VS Code Extension: "Playwright Test for VS Code" installieren

### Features

- Rote Punkte als Breakpoints per Klick auf Zeilennummern setzen
- Rechtsklick auf Testzeile -> "Debug Test" startet den Browser und haelt an Breakpoints
- **Live-Locator-Picking**: Im VS Code-Panel Locatoren anklicken -> Browserhighlight
- **Multi-Browser-Debugging**: Debug-Icon Rechtsklick -> "Select Default Profile" -> Chromium/Firefox/WebKit/Mobile
- **Chrome DevTools**: Mit "Show Browser" + offenen DevTools weiterarbeiten

---

## PWDEBUG: Browser-Konsolen-API

### Aktivieren

```bash
# Gibt `playwright`-Objekt in der Browser-Konsole bereit
PWDEBUG=console npx playwright test

# Oeffnet Playwright Inspector
PWDEBUG=1 npx playwright test
```

### `playwright`-Objekt in der Konsole

| Methode | Beschreibung |
|---------|--------------|
| `playwright.$(selector)` | Erstes Element mit Playwright-Engine abfragen |
| `playwright.$$(selector)` | Alle Treffer zurueckgeben |
| `playwright.inspect(selector)` | Element im Elements-Panel hervorheben |
| `playwright.locator(selector)` | Locator mit Matching-Info erstellen |
| `playwright.selector(element)` | Selector fuer ein DOM-Element generieren |

Voraussetzung: `await page.pause();` vor dem Testlauf einfuegen.

---

## Weitere Debug-Methoden

### Verbose-Logging

```bash
# Alle API-Aufrufe loggen
DEBUG=pw:api npx playwright test

# Browser-spezifisch
DEBUG=pw:browser npx playwright test
```

### Headed-Modus + SlowMo

```typescript
const browser = await chromium.launch({
  headless: false,
  slowMo: 100,  // Jede Aktion um 100 ms verlangsamen
});
```

### Headed per Config

```typescript
export default defineConfig({
  use: {
    headless: false,
    launchOptions: {
      slowMo: 100,
    },
  },
});
```

---

## Quellen

- https://playwright.dev/docs/trace-viewer
- https://playwright.dev/docs/trace-viewer-intro
- https://playwright.dev/docs/debug
