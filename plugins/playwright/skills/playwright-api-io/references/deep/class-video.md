# Playwright — class: Video

> **Manifest:** 3 Methoden, 0 Properties, 0 Events.
> Repraesentiert die Video-Aufzeichnung einer Browser-Seite.
> Verfuegbar wenn BrowserContext mit `recordVideo`-Option erstellt wurde.
> Zugriff: `page.video()`.

---

## Uebersicht

`Video` erlaubt den Zugriff auf die aufgezeichnete Video-Datei einer Seiten-
Sitzung. Videos werden erst vollstaendig geschrieben, wenn der BrowserContext
geschlossen wird. `saveAs()` kann sicher aufgerufen werden, waehrend die
Aufnahme noch laeuft.

```javascript
const context = await browser.newContext({
  recordVideo: {
    dir: './videos/',
    size: { width: 1280, height: 720 }
  }
});
const page = await context.newPage();
await page.goto('https://example.com');
// ... Interaktionen ...
await context.close(); // Video wird jetzt gespeichert
const videoPath = await page.video().path();
```

---

## Methoden

### video.delete()

Loescht die Video-Datei. Wartet ggf. auf den Abschluss der Aufnahme.

**Signatur:**
```typescript
video.delete(): Promise<void>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<void>`

**Hinzugefuegt:** v1.11

**Beispiel:**
```javascript
// Video nach dem Test loeschen (z.B. wenn Test bestanden hat)
await page.video().delete();
```

---

### video.path()

Gibt den Dateisystem-Pfad zurueck, unter dem das Video gespeichert wird.
Das Video ist garantiert geschrieben, sobald der BrowserContext geschlossen
wurde.

**Signatur:**
```typescript
video.path(): Promise<string>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<string>` — absoluter Dateipfad zur Video-Datei

**Hinzugefuegt:** Vor v1.9

**Hinweis:** Wirft einen Fehler, wenn Playwright mit einem Remote-Browser
verbunden ist (keine lokale Dateisystem-Kontrolle).

**Beispiel:**
```javascript
const path = await page.video().path();
console.log('Video gespeichert unter:', path);
// z.B. "./videos/test-2024-01-15-abc123.webm"
```

---

### video.saveAs(path)

Speichert das Video an einem benutzerdefinierten Pfad. Sicher waehrend
laufender Aufnahme und nach dem Schliessen der Seite aufrufbar.

**Signatur:**
```typescript
video.saveAs(path: string): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `path` | `string` | ja | — | Zieldateipfad inkl. Dateiname (absolut oder relativ zum CWD) |

**Rueckgabe:** `Promise<void>`

**Hinzugefuegt:** v1.11

**Beispiel:**
```javascript
await page.video().saveAs('/recordings/test-login-flow.webm');
```

---

## BrowserContext-Konfiguration fuer Video

```javascript
const context = await browser.newContext({
  recordVideo: {
    dir: './test-videos/',     // Verzeichnis fuer automatische Videos
    size: {
      width: 1280,
      height: 720
    }
  }
});
```

Mit Playwright Test (`playwright.config.ts`):

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    video: 'on-first-retry',    // 'off' | 'on' | 'retain-on-failure' | 'on-first-retry'
  }
});
```

---

## Typische Einsatzszenarien

### Video nur bei Fehler behalten

```javascript
// In einem Playwright-Test
test('mein test', async ({ page }, testInfo) => {
  const context = await browser.newContext({ recordVideo: { dir: './videos' } });
  const page = await context.newPage();

  try {
    await page.goto('https://example.com');
    // ... Testschritte ...
  } finally {
    await context.close();
    if (testInfo.status !== 'passed') {
      await page.video()?.saveAs(testInfo.outputPath('video.webm'));
    } else {
      await page.video()?.delete();
    }
  }
});
```

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 3      |
| Properties | 0     |
| Events    | 0      |

**Fazit:** `saveAs()` ist die wichtigste Methode — sie erlaubt es, Videos
gezielt und unabhaengig vom Default-Speicherort zu sichern. `path()` gibt
den automatisch gewaehlten Pfad zurueck. `delete()` ermoeglicht explizites
Aufraeumen z.B. bei bestandenen Tests, um Speicherplatz zu sparen.

---

*Quelle: https://playwright.dev/docs/api/class-video*
