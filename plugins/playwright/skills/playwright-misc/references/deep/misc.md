# Playwright: Erweiterungen, Videos und Release-Kanaele

## Custom Selector Engines (Extensibility)

### `selectors.register()`

Registriert eine benutzerdefinierte Selector-Engine vor der Seiteninitialisierung.

```typescript
// tests/fixtures.ts
import { test as base, selectors } from '@playwright/test';

export const test = base.extend({
  // Worker-scoped Fixture fuer Selector-Registrierung
  selectorsRegistered: [async ({}, use) => {
    // Selector-Engine registrieren
    await selectors.register('tag', () => ({
      query(root, selector) {
        return root.querySelector(selector);
      },
      queryAll(root, selector) {
        return Array.from(root.querySelectorAll(selector));
      },
    }));
    await use(true);
  }, { scope: 'worker', auto: true }],
});
```

### Signatur

```typescript
await playwright.selectors.register(
  engineName: string,
  createEngineFunction: () => SelectorEngine,
  options?: { contentScript?: boolean }
);
```

### Parameter

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `engineName` | `string` | Praefix fuer Selektoren (z.B. `'tag'` -> `tag=button`) |
| `createEngineFunction` | `() => SelectorEngine` | Funktion, die die Engine-Instanz zurueckgibt |
| `options.contentScript` | `boolean` | `true`: Isoliert vom Frame-JavaScript (sicherer, wie Built-ins) |

### SelectorEngine-Interface

```typescript
interface SelectorEngine {
  // Erstes trefffendes Element im root-Teilbaum zurueckgeben
  query(root: Element, selector: string): Element | null;

  // Alle treffenden Elemente im root-Teilbaum zurueckgeben
  queryAll(root: Element, selector: string): Element[];
}
```

### Verwendung

```typescript
// Registrierten Selector benutzen
await page.locator('tag=button').click();

// Kombiniert mit Built-in-Locators
await page.locator('tag=article').getByText('Playwright').click();
await page.locator('tag=input').filter({ hasText: 'Name' }).fill('Alice');

// Assertions
await expect(page.locator('tag=li')).toHaveCount(3);
```

### Hinweise

- Registrierung muss vor Seiteninitialisierung erfolgen
- `contentScript: true` empfohlen fuer produktionsaehnliches Verhalten
- Engines laufen standardmaessig im JavaScript-Kontext des Frames

---

## Video-Aufnahme

### Konfiguration in `playwright.config.ts`

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    video: 'on-first-retry',
  },
});
```

### Video-Optionen

| Wert | Verhalten |
|------|-----------|
| `'off'` | Keine Videoaufnahme |
| `'on'` | Jeder Test |
| `'retain-on-failure'` | Aufnehmen, aber Erfolge loeschen |
| `'on-first-retry'` | Nur beim ersten Retry |

### Erweiterte Video-Konfiguration

```typescript
export default defineConfig({
  use: {
    video: {
      mode: 'on',
      size: { width: 1280, height: 720 },
      // Aktions-Annotationen einblenden (ab v1.59)
      show: {
        actions: {
          duration: 500,        // Anzeigedauer in ms (Standard: 500)
          position: 'top-right', // Position auf dem Video
          fontSize: 14,          // Schriftgroesse
        },
        test: {
          level: 'step',        // Verbositaet: 'step', 'test', 'suite'
          position: 'top-left',
          fontSize: 12,
        },
      },
    },
  },
});
```

### Video-Pfad abrufen

```typescript
test('example', async ({ page }) => {
  await page.goto('https://example.com');
  // ... Test-Aktionen
});

// Nach Testabschluss (Context/Page muss geschlossen sein):
const path = await page.video().path();
console.log('Video gespeichert unter:', path);
```

Wichtig: `page.video().path()` erst nach dem Schliessen von Page oder Context aufrufen.

### Hinweise

- Videos werden im `test-results/`-Verzeichnis gespeichert
- Standard-Skalierung: max 800x800 mit Viewport oben-links
- Format: WebM
- `page.screencast`-API (v1.59): Streaming, Chapter-Titel, Action-Annotationen

---

## Release-Kanaele

### NPM-Dist-Tags

| Tag | Inhalt |
|-----|--------|
| `latest` | Stabile Releases |
| `next` | Taegliche Canary-Releases aus dem `main`-Branch |
| `beta` | Beta-Releases (ca. eine Woche vor Stable) |

### Installation nach Kanal

```bash
# Stabil (Standard)
npm install -D @playwright/test

# Canary (taeglich)
npm install -D @playwright/test@next

# Beta
npm install -D @playwright/test@beta
```

### Canary-Eigenschaften

- Werden taeglich veroeffentlicht (bei Code-Commits auf `main`)
- Bestehen alle automatisierten Tests inkl. HTML-Report, Trace Viewer, Inspector
- Ermoeglicht Feedback an Maintainer vor dem stabilen Release
- Doku unter `/docs/next/...` (Shift 5x druecken auf playwright.dev)

---

## Aktuelle Release-Highlights

### v1.60
- HAR-Recording als First-Class-API: `tracing.startHar()` / `tracing.stopHar()`
- `locator.drop()` fuer Drag-and-Drop mit Dateien oder Clipboard-Daten
- `expect(page).toMatchAriaSnapshot()` direkt auf Pages
- `test.abort()` zum Fehlschlagen aus Fixtures oder Route-Handlern
- Browser-Lifecycle-Events: `browser.on('context')`
- Breaking Changes: `Locator.ariaRef()`, `videosPath`/`videoSize`, Logger-Konfiguration entfernt

### v1.59
- `page.screencast`-API: Video mit Action-Annotationen, Chapter-Titeln und Frame-Streaming
- `browser.bind()`: Gestartete Browser akzeptieren Verbindungen von mehreren Clients
- `page.ariaSnapshot()`, `locator.normalize()`, `page.pickLocator()`
- `browserContext.setStorageState()`: Storage ohne neuen Context zuruecksetzen
- `await using`-Syntax fuer automatisches Resource-Cleanup
- Breaking: macOS 14 fuer WebKit entfernt; `@playwright/experimental-ct-svelte` entfernt

### v1.58
- HTML-Reporter Timeline-Tab fuer merged Reports
- UI-Mode: System-Theme folgt OS-Einstellungen
- Trace-Viewer Netzwerk-Panel mit JSON-Formatierung
- `browserType.connectOverCDP()` mit `isLocal`-Option

### v1.57
- Playwright nutzt jetzt Chrome for Testing (statt Chromium)
- `testConfig.webServer.wait`: Regex-Pattern fuer Log-Matching
- `page.accessibility` nach drei Jahren Deprecation entfernt

### v1.56
- Playwright Test Agents: Planner-, Generator-, Healer-Agenten fuer LLM-guided Tests
- `page.consoleMessages()`, `page.pageErrors()`, `page.requests()`

---

## Quellen

- https://playwright.dev/docs/extensibility
- https://playwright.dev/docs/videos
- https://playwright.dev/docs/canary-releases
- https://playwright.dev/docs/release-notes
