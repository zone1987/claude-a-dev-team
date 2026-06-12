# Playwright Downloads, Dialoge, Navigation und Touch-Events - Vollstaendige Referenz

---

## 1. Downloads

### Grundprinzip

Jeder Download loest das `'download'`-Event auf der Page aus. Die Datei wird
zunaechst in einem temporaeren Verzeichnis abgelegt. Downloads werden beim
Schliessen des Browser-Contexts geloescht.

### Download abfangen

```typescript
// Sicher: Promise vor dem Klick setzen
const downloadPromise = page.waitForEvent('download');
await page.getByText('Download Report').click();
const download = await downloadPromise;

// Dateiname und Pfad
console.log(download.suggestedFilename()); // z.B. 'report-2024.pdf'
const tmpPath = await download.path();     // Temporaerer Pfad

// Als eigene Datei speichern
await download.saveAs('./downloads/' + download.suggestedFilename());
```

### Download-Objekt - Alle Methoden

| Methode | Rueckgabe | Beschreibung |
|---------|-----------|--------------|
| `download.url()` | `string` | Original-URL des Downloads |
| `download.suggestedFilename()` | `string` | Empfohlener Dateiname (aus Content-Disposition oder URL) |
| `download.path()` | `Promise<string>` | Pfad zur temp. Datei (wartet auf Abschluss, wirft bei Fehler) |
| `download.saveAs(path)` | `Promise<void>` | Kopiert Download zu eigenem Pfad |
| `download.failure()` | `Promise<string \| null>` | Fehlermeldung falls fehlgeschlagen |
| `download.createReadStream()` | `Promise<Readable>` | Readable Stream (nur bei erfolg.) |
| `download.cancel()` | `Promise<void>` | Download abbrechen (keine Exception wenn bereits fertig) |
| `download.delete()` | `Promise<void>` | Temp-Datei loeschen |
| `download.page()` | `Page` | Ausloesendes Page-Objekt |

### Event-basiertes Handling

```typescript
// Alle Downloads einer Session protokollieren
page.on('download', async download => {
  const path = await download.path();
  console.log(`Downloaded: ${download.suggestedFilename()} -> ${path}`);
});
```

### Download-Pfad konfigurieren

```typescript
// Persistent Download-Verzeichnis (kein automatisches Loeschen)
const browser = await chromium.launch();
const context = await browser.newContext({
  acceptDownloads: true, // Default: true
});
```

### Download mit Praedikat abwarten

```typescript
const pdfDownload = await page.waitForEvent('download', {
  predicate: d => d.suggestedFilename().endsWith('.pdf'),
  timeout: 30000,
});
```

### Vollstaendiges Beispiel

```typescript
test('download and verify CSV', async ({ page }) => {
  await page.goto('/reports');

  const downloadPromise = page.waitForEvent('download');
  await page.getByRole('button', { name: 'Export CSV' }).click();
  const download = await downloadPromise;

  expect(download.suggestedFilename()).toMatch(/report.*\.csv$/);

  const savePath = `./test-results/${download.suggestedFilename()}`;
  await download.saveAs(savePath);

  const content = fs.readFileSync(savePath, 'utf-8');
  expect(content).toContain('Date,Amount');
});
```

---

## 2. Dialoge

Playwright schliesst Dialoge standardmaessig automatisch (dismiss). Eigene
Handler muessen VOR der ausloesenden Aktion registriert werden.

**Wichtig:** Ein nicht behandelter Dialog blockiert die Seite (modal). Ohne
Handler wird er automatisch dismissed.

### Dialog-Typen

| Typ | Beschreibung | accept()-Verhalten |
|-----|--------------|-------------------|
| `'alert'` | Einfache Meldung | Schliessen |
| `'confirm'` | Bestaetigung | OK (true) |
| `'prompt'` | Texteingabe | OK mit eingegebenem Text |
| `'beforeunload'` | Navigationswarnung | Verlassen bestaetigen |

### Dialog-Methoden

| Methode | Rueckgabe | Beschreibung |
|---------|-----------|--------------|
| `dialog.type()` | `string` | `'alert'`, `'confirm'`, `'prompt'`, `'beforeunload'` |
| `dialog.message()` | `string` | Angezeigte Nachricht |
| `dialog.defaultValue()` | `string` | Vorbelegung bei Prompt (sonst leer) |
| `dialog.accept(promptText?)` | `Promise<void>` | Dialog akzeptieren; bei Prompt: Text eingeben |
| `dialog.dismiss()` | `Promise<void>` | Dialog abweisen (Cancel) |
| `dialog.page()` | `Page \| null` | Ausloesendes Page-Objekt |

### Alert

```typescript
page.on('dialog', dialog => dialog.dismiss()); // oder accept()
await page.evaluate(() => alert('Hallo!'));
```

### Confirm

```typescript
// Bestaetigen
page.on('dialog', dialog => {
  expect(dialog.type()).toBe('confirm');
  expect(dialog.message()).toBe('Wirklich loeschen?');
  dialog.accept();
});
await page.getByRole('button', { name: 'Loeschen' }).click();

// Abweisen
page.on('dialog', dialog => dialog.dismiss());
await page.getByRole('button', { name: 'Loeschen' }).click();
```

### Prompt

```typescript
page.on('dialog', async dialog => {
  expect(dialog.type()).toBe('prompt');
  expect(dialog.defaultValue()).toBe('Ihr Name');
  await dialog.accept('Alice');
});
await page.evaluate("prompt('Ihr Name', 'Ihr Name')");
```

### once-Pattern (empfohlen)

```typescript
// Einmaligen Dialog-Handler mit once registrieren
page.once('dialog', dialog => dialog.accept('2024-01-01'));
await page.getByRole('button', { name: 'Datum eingeben' }).click();
```

### beforeunload

```typescript
page.on('dialog', async dialog => {
  expect(dialog.type()).toBe('beforeunload');
  await dialog.dismiss(); // Auf der Seite bleiben
  // oder: await dialog.accept(); // Seite verlassen
});

// runBeforeUnload triggert den Dialog
await page.close({ runBeforeUnload: true });
// Hinweis: page.close() wartet NICHT auf vollstaendiges Schliessen
```

### Print-Dialog (window.print)

```typescript
// window.print ueberschreiben bevor der Button geklickt wird
await page.goto('/invoice');
await page.evaluate(() => {
  window.waitForPrintDialog = new Promise(resolve => {
    window.print = resolve as any;
  });
});
await page.getByText('Drucken').click();
await page.waitForFunction(() => (window as any).waitForPrintDialog);
```

---

## 3. Navigation und Warten

### page.goto(url, options?)

| Option | Typ | Default | Beschreibung |
|--------|-----|---------|--------------|
| `url` | `string` | - | Ziel-URL |
| `waitUntil` | `'load' \| 'domcontentloaded' \| 'networkidle' \| 'commit'` | `'load'` | Wann als abgeschlossen gelten |
| `timeout` | `number` | `30000` | Timeout in ms |
| `referer` | `string` | - | Referer-Header |

```typescript
await page.goto('https://example.com');
await page.goto('/dashboard', { waitUntil: 'networkidle' });
await page.goto('/fast-page', { waitUntil: 'domcontentloaded' });
```

### waitUntil-Werte

| Wert | Beschreibung |
|------|--------------|
| `'load'` | Load-Event gefeuert |
| `'domcontentloaded'` | DOMContentLoaded gefeuert |
| `'networkidle'` | Keine Netzwerkanfragen fuer 500ms |
| `'commit'` | Netzwerkantwort erhalten und Navigation begonnen |

### page.waitForURL(url, options?)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `url` | `string \| RegExp \| (url: URL) => boolean` | Erwartete URL |
| `options.waitUntil` | wie goto | Warte-Zustand |
| `options.timeout` | `number` | Timeout in ms |

```typescript
// Nach Klick auf Link warten
await page.getByRole('button', { name: 'Abschicken' }).click();
await page.waitForURL('/confirmation');

// Mit Regex
await page.waitForURL(/\/orders\/\d+/);

// Mit Praedikat
await page.waitForURL(url => url.searchParams.get('status') === 'success');
```

### page.waitForLoadState(state?, options?)

| Parameter | Typ | Default | Beschreibung |
|-----------|-----|---------|--------------|
| `state` | `'load' \| 'domcontentloaded' \| 'networkidle'` | `'load'` | Ziel-Zustand |
| `options.timeout` | `number` | - | Timeout in ms |

```typescript
await page.waitForLoadState('networkidle');
await page.waitForLoadState('domcontentloaded', { timeout: 5000 });
```

### Navigations-Pattern (Klick + Warten)

```typescript
// Gleichzeitig auf Navigation und Klick warten
await Promise.all([
  page.waitForURL('/dashboard'),
  page.getByRole('button', { name: 'Login' }).click(),
]);

// Auf Netzwerkanfrage warten
const [response] = await Promise.all([
  page.waitForResponse('**/api/user'),
  page.click('#refresh'),
]);
const data = await response.json();

// Navigation abwarten nach SPA-Routing
await page.locator('nav a').filter({ hasText: 'Profile' }).click();
await page.waitForURL('**/profile');
await page.waitForLoadState('networkidle');
```

### Navigations-Events

```typescript
page.on('domcontentloaded', () => console.log('DOM ready'));
page.on('load', () => console.log('Page loaded'));
page.on('framenavigated', frame => {
  if (frame === page.mainFrame()) {
    console.log('Main frame navigated to:', frame.url());
  }
});
```

### Hydration-Probleme

Bei SSR-Frameworks kann die Seite visuell fertig sein, aber JS noch nicht
hydratisiert haben.

```typescript
// Warten bis Element interaktiv ist (nicht nur sichtbar)
await page.locator('#checkout-button').click(); // Auto-waits bis enabled

// Explizit warten
await expect(page.locator('#form')).toBeEnabled();
await page.locator('#form input[name="email"]').fill('test@example.com');
```

---

## 4. Touch-Events und Gesten

Playwright unterstuetzt Legacy-Touch-Events (TouchEvent-API) ueber
`locator.dispatchEvent()`.

**Hinweis:** `dispatchEvent()` setzt `Event.isTrusted = false`. Apps, die
auf isTrusted pruefen, muessen angepasst werden.

### locator.dispatchEvent(type, eventInit?)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `type` | `string` | Event-Typ: `'touchstart'`, `'touchmove'`, `'touchend'` |
| `eventInit` | `Object` | TouchEvent-Eigenschaften |

### TouchEvent-Eigenschaften

| Eigenschaft | Typ | Beschreibung |
|-------------|-----|--------------|
| `touches` | `Touch[]` | Aktuelle Beruehrungspunkte |
| `targetTouches` | `Touch[]` | Beruehrungspunkte auf Target |
| `changedTouches` | `Touch[]` | Geaenderte Beruehrungspunkte |

### Touch-Objekt-Eigenschaften

| Eigenschaft | Typ | Beschreibung |
|-------------|-----|--------------|
| `identifier` | `number` | Eindeutige ID des Touchpoints |
| `clientX` | `number` | X-Koordinate relativ zum Viewport |
| `clientY` | `number` | Y-Koordinate relativ zum Viewport |
| `pageX` | `number` | X-Koordinate relativ zur Seite |
| `pageY` | `number` | Y-Koordinate relativ zur Seite |

### Geraet-Konfiguration fuer Touch

```typescript
test.use({ ...devices['Pixel 7'] });
// oder manuell:
test.use({ hasTouch: true, isMobile: true });
```

---

### Pan-Geste (Wischen/Verschieben)

```typescript
async function pan(
  locator: Locator,
  deltaX = 0,
  deltaY = 0,
  steps = 5
): Promise<void> {
  const box = await locator.boundingBox();
  if (!box) throw new Error('Element nicht sichtbar');

  const centerX = box.x + box.width / 2;
  const centerY = box.y + box.height / 2;

  await locator.dispatchEvent('touchstart', {
    touches: [{ identifier: 0, clientX: centerX, clientY: centerY }],
    targetTouches: [{ identifier: 0, clientX: centerX, clientY: centerY }],
    changedTouches: [{ identifier: 0, clientX: centerX, clientY: centerY }],
  });

  for (let i = 1; i <= steps; i++) {
    const x = centerX + (deltaX * i) / steps;
    const y = centerY + (deltaY * i) / steps;
    await locator.dispatchEvent('touchmove', {
      touches: [{ identifier: 0, clientX: x, clientY: y }],
      targetTouches: [{ identifier: 0, clientX: x, clientY: y }],
      changedTouches: [{ identifier: 0, clientX: x, clientY: y }],
    });
  }

  await locator.dispatchEvent('touchend', {
    touches: [],
    targetTouches: [],
    changedTouches: [{ identifier: 0, clientX: centerX + deltaX, clientY: centerY + deltaY }],
  });
}

// Verwendung
test('map pan', async ({ page }) => {
  test.use({ ...devices['Pixel 7'] });
  await page.goto('https://www.google.com/maps');
  const map = page.locator('#map');
  for (let i = 0; i < 5; i++) {
    await pan(map, 100, 0); // 100px nach rechts
  }
  await expect(page).toHaveScreenshot('map-panned.png');
});
```

---

### Pinch-Geste (Zoom rein/raus)

```typescript
async function pinch(
  locator: Locator,
  arg: { deltaX?: number; steps?: number; direction?: 'in' | 'out' } = {}
): Promise<void> {
  const { deltaX = 50, steps = 5, direction = 'in' } = arg;
  const box = await locator.boundingBox();
  if (!box) throw new Error('Element nicht sichtbar');

  const centerX = box.x + box.width / 2;
  const centerY = box.y + box.height / 2;

  // Starteingabe: zwei Punkte um Zentrum
  const startDistance = direction === 'in' ? deltaX : 0;
  await locator.dispatchEvent('touchstart', {
    touches: [
      { identifier: 0, clientX: centerX - startDistance, clientY: centerY },
      { identifier: 1, clientX: centerX + startDistance, clientY: centerY },
    ],
    targetTouches: [
      { identifier: 0, clientX: centerX - startDistance, clientY: centerY },
      { identifier: 1, clientX: centerX + startDistance, clientY: centerY },
    ],
    changedTouches: [
      { identifier: 0, clientX: centerX - startDistance, clientY: centerY },
      { identifier: 1, clientX: centerX + startDistance, clientY: centerY },
    ],
  });

  for (let i = 1; i <= steps; i++) {
    const offset = direction === 'in'
      ? deltaX - (deltaX * i) / steps  // Punkte zusammenfuehren
      : (deltaX * i) / steps;           // Punkte auseinanderziehen

    await locator.dispatchEvent('touchmove', {
      touches: [
        { identifier: 0, clientX: centerX - offset, clientY: centerY },
        { identifier: 1, clientX: centerX + offset, clientY: centerY },
      ],
      targetTouches: [
        { identifier: 0, clientX: centerX - offset, clientY: centerY },
        { identifier: 1, clientX: centerX + offset, clientY: centerY },
      ],
      changedTouches: [
        { identifier: 0, clientX: centerX - offset, clientY: centerY },
        { identifier: 1, clientX: centerX + offset, clientY: centerY },
      ],
    });
  }

  const endOffset = direction === 'in' ? 0 : deltaX;
  await locator.dispatchEvent('touchend', {
    touches: [],
    targetTouches: [],
    changedTouches: [
      { identifier: 0, clientX: centerX - endOffset, clientY: centerY },
      { identifier: 1, clientX: centerX + endOffset, clientY: centerY },
    ],
  });
}

// Verwendung
test('map zoom', async ({ page }) => {
  await page.goto('https://www.google.com/maps');
  const map = page.locator('#map');

  // Reinzoomen
  for (let i = 0; i < 3; i++) {
    await pinch(map, { direction: 'out', deltaX: 80 }); // Finger auseinanderziehen = zoom in
  }
  // Rauszoomen
  for (let i = 0; i < 3; i++) {
    await pinch(map, { direction: 'in', deltaX: 80 }); // Finger zusammenfuehren = zoom out
  }
});
```

---

## 5. File Chooser (Datei-Upload)

```typescript
// Datei-Upload ueber Datei-Dialog
const fileChooserPromise = page.waitForEvent('filechooser');
await page.getByLabel('Avatar hochladen').click();
const fileChooser = await fileChooserPromise;

// Einzelne Datei
await fileChooser.setFiles('./fixtures/avatar.png');

// Mehrere Dateien
await fileChooser.setFiles(['./a.pdf', './b.pdf']);

// Datei-Objekt ohne Disk-Datei
await fileChooser.setFiles({
  name: 'test.txt',
  mimeType: 'text/plain',
  buffer: Buffer.from('file content'),
});
```

---

Quelle: https://playwright.dev/docs/downloads | https://playwright.dev/docs/dialogs | https://playwright.dev/docs/navigations | https://playwright.dev/docs/touch-events | https://playwright.dev/docs/api/class-download | https://playwright.dev/docs/api/class-dialog
