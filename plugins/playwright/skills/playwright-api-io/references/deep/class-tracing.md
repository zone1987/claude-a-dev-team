# Playwright — class: Tracing

> **Manifest:** 8 Methoden, 0 Properties, 0 Events.
> Erstellt und verwaltet Playwright Traces fuer den Trace Viewer.
> Zugriff: `browserContext.tracing`.

---

## Uebersicht

`Tracing` zeichnet detaillierte Informationen ueber Netzwerk-Requests,
Seitenaktionen, Screenshots und DOM-Snapshots auf. Die resultierenden
`.zip`-Dateien koennen im Playwright Trace Viewer (`npx playwright show-trace
trace.zip`) geoeffnet werden.

```javascript
// Einfaches Beispiel
await context.tracing.start({ screenshots: true, snapshots: true });
const page = await context.newPage();
await page.goto('https://playwright.dev');
await context.tracing.stop({ path: 'trace.zip' });
```

---

## Methoden

### tracing.group(name, options?)

Erstellt eine benannte Gruppe im Trace, die alle folgenden API-Aufrufe
bis zum naechsten `groupEnd()` zusammenfasst.

**Signatur:**
```typescript
tracing.group(name: string, options?: {
  location?: {
    file: string;
    line?: number;
    column?: number;
  };
}): Promise<Disposable>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `name` | `string` | ja | — | Bezeichnung der Gruppe im Trace Viewer |
| `options.location` | `Object` | nein | — | Quellcode-Ort der Gruppe (fuer Test-Annotierungen) |
| `options.location.file` | `string` | nein | — | Quelldatei-Pfad |
| `options.location.line` | `number` | nein | — | Zeilennummer |
| `options.location.column` | `number` | nein | — | Spaltennummer |

**Rueckgabe:** `Promise<Disposable>` — beim Dispose wird die Gruppe geschlossen

**Beispiel:**
```javascript
await context.tracing.group('Login-Flow');
await page.fill('#username', 'user');
await page.fill('#password', 'pass');
await page.click('#submit');
await context.tracing.groupEnd();
```

---

### tracing.groupEnd()

Schliesst die zuletzt mit `group()` geoeffnete Gruppe.

**Signatur:**
```typescript
tracing.groupEnd(): Promise<void>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await context.tracing.groupEnd();
```

---

### tracing.start(options?)

Startet die Trace-Aufzeichnung fuer diesen BrowserContext.

**Signatur:**
```typescript
tracing.start(options?: {
  live?: boolean;
  name?: string;
  screenshots?: boolean;
  snapshots?: boolean;
  sources?: boolean;
  title?: string;
}): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `options.live` | `boolean` | nein | `false` | Trace-Datei wird nicht archiviert — erlaubt Live-Inspektion ueber `tracesDir` |
| `options.name` | `string` | nein | — | Praefix fuer temporaere Trace-Dateien in `tracesDir` |
| `options.screenshots` | `boolean` | nein | `false` | Screenshots fuer Timeline-Vorschau aufnehmen |
| `options.snapshots` | `boolean` | nein | `false` | DOM-Snapshots und Netzwerk-Aktivitaet aufzeichnen (ermoeglicht Inspect-Modus im Viewer) |
| `options.sources` | `boolean` | nein | `false` | Quell-Dateien in den Trace einbinden |
| `options.title` | `string` | nein | — | Angezeigter Name im Trace Viewer |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await context.tracing.start({
  screenshots: true,
  snapshots: true,
  sources: true,
  title: 'Checkout-Flow Test'
});
```

---

### tracing.startChunk(options?)

Startet einen neuen Trace-Chunk auf demselben bereits laufenden Context.
Ermaoglicht es, mehrere Teil-Traces aus einer einzigen Testsession zu
erzeugen.

**Signatur:**
```typescript
tracing.startChunk(options?: {
  name?: string;
  title?: string;
}): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `options.name` | `string` | nein | — | Praefix fuer temporaere Chunk-Dateien |
| `options.title` | `string` | nein | — | Angezeigter Name im Trace Viewer |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await context.tracing.start({ screenshots: true, snapshots: true });

// Erster Test
await context.tracing.startChunk({ title: 'Test: Login' });
await page.goto('/login');
await context.tracing.stopChunk({ path: 'trace-login.zip' });

// Zweiter Test auf demselben Context
await context.tracing.startChunk({ title: 'Test: Checkout' });
await page.goto('/checkout');
await context.tracing.stopChunk({ path: 'trace-checkout.zip' });
```

---

### tracing.startHar(path, options?)

Startet die HAR-Aufzeichnung von Netzwerk-Aktivitaet. Die Datei wird beim
Aufruf von `stopHar()` gespeichert.

**Signatur:**
```typescript
tracing.startHar(path: string, options?: {
  content?: 'omit' | 'embed' | 'attach';
  mode?: 'full' | 'minimal';
  resourcesDir?: string;
  urlFilter?: string | RegExp;
}): Promise<Disposable>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `path` | `string` | ja | — | Zieldateipfad fuer die HAR-Datei (`.zip` wird unterstuetzt) |
| `options.content` | `'omit' \| 'embed' \| 'attach'` | nein | — | Wie Response-Inhalte gespeichert werden: `'omit'` = nicht speichern, `'embed'` = in HAR einbetten, `'attach'` = als separate Dateien |
| `options.mode` | `'full' \| 'minimal'` | nein | — | `'full'` = alle Details, `'minimal'` = nur zum Routing noetige Daten |
| `options.resourcesDir` | `string` | nein | — | Verzeichnis fuer Response-Bodies (bei `'attach'`) |
| `options.urlFilter` | `string \| RegExp` | nein | — | Nur passende URLs aufzeichnen |

**Rueckgabe:** `Promise<Disposable>` — beim Dispose wird HAR-Recording gestoppt

**Beispiel:**
```javascript
await context.tracing.startHar('network.har', {
  content: 'attach',
  urlFilter: /api\./
});
await page.goto('https://example.com');
await context.tracing.stopHar();
```

---

### tracing.stop(options?)

Beendet die Trace-Aufzeichnung und exportiert optional in eine Datei.

**Signatur:**
```typescript
tracing.stop(options?: {
  path?: string;
}): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `options.path` | `string` | nein | — | Zieldateipfad fuer den Trace (`.zip`). Ohne Angabe wird der Trace verworfen. |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await context.tracing.stop({ path: 'trace.zip' });
// Viewer: npx playwright show-trace trace.zip
```

---

### tracing.stopChunk(options?)

Beendet den aktuellen Trace-Chunk und exportiert ihn.

**Signatur:**
```typescript
tracing.stopChunk(options?: {
  path?: string;
}): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `options.path` | `string` | nein | — | Zieldateipfad fuer den Chunk-Trace |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await context.tracing.stopChunk({ path: 'trace-chunk-1.zip' });
```

---

### tracing.stopHar()

Beendet die HAR-Aufzeichnung und schreibt die Datei in den in `startHar()`
angegebenen Pfad.

**Signatur:**
```typescript
tracing.stopHar(): Promise<void>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await context.tracing.stopHar();
```

---

## Vollstaendiges Beispiel (Playwright Test)

```typescript
import { test } from '@playwright/test';

test.describe('E-Commerce Flow', () => {
  test.beforeAll(async ({ browser }) => {
    const context = await browser.newContext();
    await context.tracing.start({ screenshots: true, snapshots: true, sources: true });
    // ... setup ...
  });

  test('Warenkorb hinzufuegen', async ({ page, context }) => {
    await context.tracing.startChunk({ title: 'Warenkorb' });
    await page.goto('/shop');
    await page.click('[data-testid="add-to-cart"]');
    await context.tracing.stopChunk({ path: 'trace-cart.zip' });
  });
});
```

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 8      |
| Properties | 0     |
| Events    | 0      |

**Fazit:** `start()` + `stop()` decken den Standardfall ab. `startChunk()` /
`stopChunk()` ermoeglicht granulare Traces pro Test bei gemeinsamem Context.
`startHar()` ist unabhaengig von der Trace-Aufzeichnung und dient gezielt der
Netzwerk-Analyse. `group()` / `groupEnd()` verbessern die Lesbarkeit im Trace
Viewer erheblich.

---

*Quelle: https://playwright.dev/docs/api/class-tracing*
