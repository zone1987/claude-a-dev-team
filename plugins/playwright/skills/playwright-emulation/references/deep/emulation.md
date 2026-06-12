# Playwright Emulation, Clock und Screenshots - Vollstaendige Referenz

---

## 1. Geraete-Emulation

Playwright beinhaltet eine Datenbank mit vordefinierten Geraete-Parametern.

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  projects: [
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 7'] },
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 15'] },
    },
    {
      name: 'Desktop Chrome',
      use: { ...devices['Desktop Chrome'] },
    },
  ],
});
```

Ein Geraete-Preset setzt automatisch: `userAgent`, `viewport`, `deviceScaleFactor`,
`isMobile`, `hasTouch`.

```typescript
// Plattform-agnostischer User-Agent (Preset ueberschreiben)
test.use({
  ...devices['iPhone 15'],
  userAgent: undefined, // Kein platform-spezifischer UA
});
```

---

## 2. Viewport

### Konfiguration

```typescript
// playwright.config.ts
use: {
  viewport: { width: 1280, height: 720 },
}

// Pro Test
test.use({
  viewport: { width: 1920, height: 1080 },
});

// Zur Laufzeit
await page.setViewportSize({ width: 375, height: 812 });
```

### Device Scale Factor (HiDPI)

```typescript
const context = await browser.newContext({
  viewport: { width: 2560, height: 1440 },
  deviceScaleFactor: 2, // Retina
});
```

---

## 3. isMobile

Steuert, ob der meta-viewport-Tag beachtet und Touch-Events aktiviert werden.

```typescript
use: { isMobile: true }  // Default bei mobilen Devices: true

// Zur Laufzeit kein direktes API - nur per Context-Erstellung
const context = await browser.newContext({ isMobile: true });
```

---

## 4. User Agent

```typescript
// Konfiguration
test.use({ userAgent: 'MyTestBot/1.0' });

// Per Context
const context = await browser.newContext({
  userAgent: 'Mozilla/5.0 (compatible; TestRunner/1.0)',
});

// Laufzeit (nur per neuer Page im Context)
```

---

## 5. Locale und Timezone

```typescript
// Konfiguration
use: {
  locale: 'de-DE',
  timezoneId: 'Europe/Berlin',
}

// Per Context
const context = await browser.newContext({
  locale: 'ja-JP',
  timezoneId: 'Asia/Tokyo',
});
```

**Hinweis:** `timezoneId` betrifft nur den Browser, nicht den Test-Runner.
Fuer Test-Runner: `TZ`-Umgebungsvariable setzen.

Gueltige Timezone-IDs: IANA-Format, z.B. `'America/New_York'`, `'UTC'`,
`'Europe/Paris'`, `'Asia/Shanghai'`.

---

## 6. Geolocation

```typescript
// Konfiguration
use: {
  geolocation: { longitude: 13.405, latitude: 52.52 }, // Berlin
  permissions: ['geolocation'],
}

// Zur Laufzeit aktualisieren (gilt fuer alle Pages im Context)
await context.setGeolocation({ longitude: 2.349, latitude: 48.864 }); // Paris

// Mit Genauigkeit
await context.setGeolocation({
  longitude: -0.1276,
  latitude: 51.5074,
  accuracy: 10, // Meter
});
```

**Wichtig:** Geolocation nur aenderbar fuer den gesamten Context, nicht
individuell pro Page.

---

## 7. Berechtigungen (Permissions)

### Vergeben

```typescript
// Konfiguration (alle Pages im Projekt)
use: {
  permissions: ['notifications', 'geolocation'],
}

// Per Context
const context = await browser.newContext({
  permissions: ['camera', 'microphone'],
});

// Domain-spezifisch
await context.grantPermissions(['notifications'], {
  origin: 'https://example.com',
});

// Mehrere Domains
await context.grantPermissions(['geolocation'], { origin: 'https://maps.google.com' });
await context.grantPermissions(['geolocation'], { origin: 'https://openstreetmap.org' });
```

### Zuruecksetzen

```typescript
await context.clearPermissions(); // Alle Permissions widerrufen
```

### Unterstuetzte Permissions

`'accelerometer'`, `'ambient-light-sensor'`, `'background-sync'`,
`'camera'`, `'clipboard-read'`, `'clipboard-write'`, `'geolocation'`,
`'gyroscope'`, `'magnetometer'`, `'microphone'`, `'midi'`,
`'notifications'`, `'payment-handler'`, `'persistent-storage'`,
`'push'`, `'screen-wake-lock'`, `'storage-access'`

---

## 8. Farbschema und Media

### Color Scheme

```typescript
// Konfiguration
use: { colorScheme: 'dark' } // 'light' | 'dark' | 'no-preference'

// Zur Laufzeit
await page.emulateMedia({ colorScheme: 'dark' });
await page.emulateMedia({ colorScheme: 'light' });
```

### Media Type

```typescript
// Druckvorschau emulieren
await page.emulateMedia({ media: 'print' }); // 'screen' | 'print' | null

// Reduzierte Bewegung
await page.emulateMedia({ reducedMotion: 'reduce' }); // 'reduce' | 'no-preference' | null

// Kontrastpraeferenz
await page.emulateMedia({ forcedColors: 'active' }); // 'active' | 'none' | null
```

### emulateMedia Vollstaendige Optionen

| Option | Typ | Default | Beschreibung |
|--------|-----|---------|--------------|
| `colorScheme` | `'light' \| 'dark' \| 'no-preference' \| null` | - | Farbschema-Praeferenz |
| `forcedColors` | `'active' \| 'none' \| null` | - | Forced Colors |
| `media` | `'screen' \| 'print' \| null` | - | CSS-Media-Type |
| `reducedMotion` | `'reduce' \| 'no-preference' \| null` | - | Animationsreduzierung |

```typescript
// Alle Optionen zusammen
await page.emulateMedia({
  colorScheme: 'dark',
  media: 'screen',
  reducedMotion: 'reduce',
});
```

---

## 9. Offline-Modus und JavaScript

```typescript
// Offline
use: { offline: true }

const context = await browser.newContext({ offline: true });
await context.setOffline(true);  // Zur Laufzeit
await context.setOffline(false);

// JavaScript deaktivieren
test.use({ javaScriptEnabled: false });

const context = await browser.newContext({ javaScriptEnabled: false });
```

---

## 10. Clock API

Die Clock API ermoeglicht vollstaendige Kontrolle ueber Zeit im Browser.

### Methoden-Uebersicht

| Methode | Beschreibung |
|---------|--------------|
| `page.clock.setFixedTime(time)` | Fixe Zeit fuer Date.now() und new Date() |
| `page.clock.install(options?)` | Vollstaendige Clock-Uebernahme |
| `page.clock.pauseAt(time)` | Zur Zeit springen und anhalten |
| `page.clock.fastForward(ticks)` | Zeit vorspulen (Timer max. einmal ausloesen) |
| `page.clock.runFor(ticks)` | Zeit vorspulen (alle Timer ausloesen) |
| `page.clock.resume()` | Pausierte Clock weiterlaufen lassen |
| `page.clock.setSystemTime(time)` | Systemzeit setzen ohne Timer auszuloesen |

---

### page.clock.setFixedTime(time)

Einfachste Methode: Fixiert `Date.now()` und `new Date()`. Timer laufen weiter.

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `time` | `number \| string \| Date` | Feste Zeit |

```typescript
// Datum fixieren
await page.clock.setFixedTime(new Date('2024-02-29T10:00:00'));
await page.goto('http://localhost:3000');
await expect(page.getByTestId('date-display')).toHaveText('Feb 29, 2024');

// Als Unix-Timestamp (ms)
await page.clock.setFixedTime(1709200000000);

// Als ISO-String
await page.clock.setFixedTime('2024-02-29');
```

---

### page.clock.install(options?)

Ersetzt alle nativen Zeit-Funktionen mit Fakes.

**Ueberschriebene Globals:**
`Date`, `setTimeout`, `clearTimeout`, `setInterval`, `clearInterval`,
`requestAnimationFrame`, `cancelAnimationFrame`, `requestIdleCallback`,
`cancelIdleCallback`, `performance`, `Event.timeStamp`

| Option | Typ | Default | Beschreibung |
|--------|-----|---------|--------------|
| `time` | `number \| string \| Date` | Systemzeit | Startzeitpunkt |

**Wichtig:** `install()` MUSS vor allen anderen Clock-Aufrufen stehen,
falls verwendet.

```typescript
await page.clock.install({ time: new Date('2024-01-01T09:00:00') });
await page.goto('http://localhost:3000/dashboard');
// Jetzt sind alle Timer und Date-Aufrufe kontrollierbar
```

---

### page.clock.pauseAt(time)

Springt zur angegebenen Zeit und haelt alle Timer an.

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `time` | `number \| string \| Date` | Zielzeit |

```typescript
await page.clock.install({ time: new Date('2024-12-10T08:00:00') });
await page.goto('http://localhost:3000');
await page.clock.pauseAt(new Date('2024-12-10T10:00:00'));
// Zeit ist jetzt 10:00 Uhr, keine Timer laufen

await expect(page.getByTestId('clock')).toHaveText('10:00:00');
```

---

### page.clock.fastForward(ticks)

Springt vorwaerts, jeder faellige Timer wird maximal einmal ausgefuehrt.
Simuliert z.B. Laptop-Klappvorgang.

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `ticks` | `number \| string` | Millisekunden oder `'HH:MM:SS'`-Format |

```typescript
// 30 Minuten vorspulen
await page.clock.fastForward('30:00');

// Als Millisekunden
await page.clock.fastForward(1800000);

// Pattern: install -> navigate -> pause -> fastForward
await page.clock.install({ time: new Date('2024-02-02T08:00:00') });
await page.goto('http://localhost:3000');
await page.clock.pauseAt(new Date('2024-02-02T10:00:00'));
await page.clock.fastForward('30:00'); // Bis 10:30
```

---

### page.clock.runFor(ticks)

Wie `fastForward`, aber alle Timer feuern in Echtzeit-Reihenfolge.

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `ticks` | `number \| string` | Millisekunden oder `'HH:MM:SS'`-Format |

```typescript
// 2 Sekunden simulieren (alle Timeouts/Intervals feuern)
await page.clock.runFor(2000);
await page.clock.runFor('00:02'); // 2 Sekunden

// Interval-Test
await page.clock.install();
await page.evaluate(() => {
  setInterval(() => document.body.setAttribute('data-tick', String(Date.now())), 1000);
});
await page.clock.runFor(5000); // 5 Ticks
```

---

### page.clock.resume()

Setzt eine pausierte Clock fort.

```typescript
await page.clock.install();
await page.clock.pauseAt(new Date('2024-06-15T12:00:00'));
// ... Tests zur Zeit 12:00 ...
await page.clock.resume(); // Timer laufen wieder
```

---

### page.clock.setSystemTime(time)

Setzt Systemzeit, loest aber keine Timer aus. Fuer Zeitzonensprung-Tests.

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `time` | `number \| string \| Date` | Neue Systemzeit |

```typescript
await page.clock.install();
await page.clock.setSystemTime(new Date('2024-12-31T23:59:00'));
// Seite reagiert auf Jahreswechsel-Logik
```

---

### Zeit-Format fuer ticks/time

| Format | Beispiel | Bedeutung |
|--------|---------|-----------|
| `number` | `3600000` | Millisekunden |
| `string HH` | `'30'` | 30 Sekunden |
| `string HH:MM` | `'01:30'` | 1 Minute 30 Sekunden |
| `string HH:MM:SS` | `'02:30:00'` | 2 Stunden 30 Minuten |
| `Date` | `new Date('2024-01-01')` | Datum-Objekt |
| ISO-String | `'2024-01-01T12:00:00'` | ISO-Datum |

---

## 11. Screenshots

### page.screenshot(options?)

| Option | Typ | Default | Beschreibung |
|--------|-----|---------|--------------|
| `path` | `string` | - | Speicherpfad (Endung bestimmt Format: .png, .jpg) |
| `type` | `'png' \| 'jpeg'` | `'png'` | Bildformat |
| `quality` | `number` | - | JPEG-Qualitaet 0-100 (nur JPEG) |
| `fullPage` | `boolean` | `false` | Gesamte scrollbare Seite |
| `clip` | `{x, y, width, height}` | - | Ausschnitt-Rechteck |
| `omitBackground` | `boolean` | `false` | Transparenz statt weissem Hintergrund (nur PNG) |
| `animations` | `'disabled' \| 'allow'` | `'disabled'` | CSS-Animationen |
| `caret` | `'hide' \| 'initial'` | `'hide'` | Cursor-Sichtbarkeit |
| `scale` | `'css' \| 'device'` | `'device'` | Rendermassstab |
| `mask` | `Locator[]` | - | Elemente maskieren |
| `maskColor` | `string` | `'#FF00FF'` | Maskierungsfarbe |
| `timeout` | `number` | `0` | Timeout in ms |

```typescript
// Einfacher Screenshot
await page.screenshot({ path: 'screenshot.png' });

// Ganze Seite
await page.screenshot({ path: 'full.png', fullPage: true });

// Ausschnitt
await page.screenshot({
  path: 'header.png',
  clip: { x: 0, y: 0, width: 1280, height: 80 },
});

// JPEG mit Qualitaet
await page.screenshot({
  path: 'preview.jpg',
  type: 'jpeg',
  quality: 80,
});

// Transparenter Hintergrund
await page.screenshot({
  path: 'transparent.png',
  omitBackground: true,
});

// Sensible Daten maskieren
await page.screenshot({
  path: 'masked.png',
  mask: [page.locator('.credit-card'), page.locator('#password')],
  maskColor: '#000000',
});

// Buffer (kein Dateipfad)
const buffer = await page.screenshot();
const base64 = buffer.toString('base64');
```

### locator.screenshot(options?)

Screenshot eines einzelnen Elements (gleiche Optionen wie page.screenshot).

```typescript
await page.locator('.product-card').first().screenshot({ path: 'card.png' });

// Element-Screenshot in Buffer
const cardBuffer = await page.locator('.hero-image').screenshot();
```

---

## 12. Vollstaendiges Emulations-Beispiel

```typescript
import { test, expect, devices } from '@playwright/test';

test.use({
  ...devices['iPhone 15 Pro'],
  locale: 'de-DE',
  timezoneId: 'Europe/Berlin',
  geolocation: { latitude: 48.137, longitude: 11.576 }, // Muenchen
  permissions: ['geolocation'],
  colorScheme: 'dark',
});

test('mobile dark mode with geolocation', async ({ page, context }) => {
  // Clock fixieren
  await page.clock.setFixedTime(new Date('2024-06-21T14:30:00+02:00'));

  await page.goto('http://localhost:3000');

  // Geolocation zur Laufzeit aktualisieren
  await context.setGeolocation({ latitude: 52.52, longitude: 13.405 }); // Berlin
  await page.reload();

  await page.screenshot({
    path: 'test-results/mobile-dark.png',
    fullPage: true,
    mask: [page.locator('.user-data')],
  });
});
```

---

Quelle: https://playwright.dev/docs/emulation | https://playwright.dev/docs/clock | https://playwright.dev/docs/screenshots | https://playwright.dev/docs/api/class-clock
