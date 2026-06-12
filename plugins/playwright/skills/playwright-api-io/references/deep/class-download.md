# Playwright — class: Download

> **Manifest:** 9 Methoden, 0 Properties, 0 Events (1 externer Page-Event).
> Repraesentiert eine gestartete oder abgeschlossene Datei-Download-Operation.
> Instanzen werden ueber `page.on('download')` bzw. `page.waitForEvent('download')` erhalten.

---

## Uebersicht

`Download`-Objekte entstehen, wenn eine Seite einen Download ausloest.
Playwright speichert heruntergeladene Dateien temporaer im System-Temp-
Verzeichnis; diese werden beim Schliessen des Contexts automatisch geloescht.
Zum dauerhaften Speichern muss `saveAs()` aufgerufen werden.

```javascript
const downloadPromise = page.waitForEvent('download');
await page.getByText('Herunterladen').click();
const download = await downloadPromise;
await download.saveAs('/tmp/meine-datei.pdf');
```

---

## Methoden

### download.cancel()

Bricht den laufenden Download ab. Schlaegt nicht fehl, wenn der Download
bereits abgeschlossen oder abgebrochen wurde.

**Signatur:**
```typescript
download.cancel(): Promise<void>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<void>`

**Hinzugefuegt:** v1.13

**Beispiel:**
```javascript
await download.cancel();
```

---

### download.createReadStream()

Gibt einen lesbaren Node.js-Stream fuer den heruntergeladenen Inhalt zurueck.
Wirft einen Fehler bei fehlgeschlagenem oder abgebrochenem Download.

**Signatur:**
```typescript
download.createReadStream(): Promise<Readable>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<Readable>` — Node.js Readable Stream

**Hinzugefuegt:** v1.9

**Beispiel:**
```javascript
const stream = await download.createReadStream();
const chunks: Buffer[] = [];
for await (const chunk of stream) {
  chunks.push(Buffer.from(chunk));
}
const content = Buffer.concat(chunks).toString('utf-8');
```

---

### download.delete()

Loescht die heruntergeladene temporaere Datei. Wartet ggf. auf den Abschluss
des Downloads.

**Signatur:**
```typescript
download.delete(): Promise<void>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<void>`

**Hinzugefuegt:** v1.9

**Beispiel:**
```javascript
await download.delete();
```

---

### download.failure()

Gibt den Fehlertext zurueck, falls der Download fehlgeschlagen ist.
Gibt `null` bei erfolgreichem Download zurueck. Wartet ggf. auf Abschluss.

**Signatur:**
```typescript
download.failure(): Promise<null | string>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<null | string>` — Fehler-String oder `null`

**Hinzugefuegt:** v1.9

**Beispiel:**
```javascript
const error = await download.failure();
if (error) {
  console.error('Download fehlgeschlagen:', error);
}
```

---

### download.page()

Gibt die Seite zurueck, der dieser Download gehoert.

**Signatur:**
```typescript
download.page(): Page
```

**Parameter:** Keine

**Rueckgabe:** `Page`

**Hinzugefuegt:** v1.12

**Beispiel:**
```javascript
const sourcePage = download.page();
console.log('Download von:', sourcePage.url());
```

---

### download.path()

Gibt den absoluten Dateipfad zur heruntergeladenen temporaeren Datei zurueck.
Wirft einen Fehler bei fehlgeschlagenem oder abgebrochenem Download.
Wartet ggf. auf Abschluss.

**Signatur:**
```typescript
download.path(): Promise<string>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<string>` — absoluter Pfad zur temporaeren Datei

**Hinzugefuegt:** v1.9

**Hinweis:** Der Pfad ist nur gueltig, solange der BrowserContext offen ist.

**Beispiel:**
```javascript
const tmpPath = await download.path();
console.log('Temporaerer Pfad:', tmpPath);
```

---

### download.saveAs(path)

Kopiert die heruntergeladene Datei an den angegebenen Pfad. Sicher waehrend
laufendem Download aufrufbar.

**Signatur:**
```typescript
download.saveAs(path: string): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `path` | `string` | ja | — | Zieldateipfad (absolut oder relativ zum CWD) |

**Rueckgabe:** `Promise<void>`

**Hinzugefuegt:** v1.9

**Beispiel:**
```javascript
await download.saveAs('/downloads/' + download.suggestedFilename());
```

---

### download.suggestedFilename()

Gibt den vom Browser vorgeschlagenen Dateinamen zurueck (aus
`Content-Disposition`-Header oder `download`-Attribut).

**Signatur:**
```typescript
download.suggestedFilename(): string
```

**Parameter:** Keine

**Rueckgabe:** `string` — vorgeschlagener Dateiname

**Hinzugefuegt:** v1.9

**Beispiel:**
```javascript
console.log(download.suggestedFilename()); // z.B. "bericht-2024.pdf"
await download.saveAs('/tmp/' + download.suggestedFilename());
```

---

### download.url()

Gibt die URL zurueck, von der heruntergeladen wurde.

**Signatur:**
```typescript
download.url(): string
```

**Parameter:** Keine

**Rueckgabe:** `string` — Download-URL

**Hinzugefuegt:** v1.9

**Beispiel:**
```javascript
console.log('Download-URL:', download.url());
```

---

## Page-Event: 'download'

```javascript
page.on('download', async (download) => {
  console.log('Neuer Download:', download.suggestedFilename());
  await download.saveAs('./downloads/' + download.suggestedFilename());
});
```

Oder als einmaliges Warten:

```javascript
const download = await page.waitForEvent('download');
```

---

## Vollstaendiges Beispiel

```javascript
const { chromium } = require('playwright');

const browser = await chromium.launch();
const context = await browser.newContext({ acceptDownloads: true });
const page = await context.newPage();
await page.goto('https://example.com/downloads');

const downloadPromise = page.waitForEvent('download');
await page.click('#download-button');
const download = await downloadPromise;

// Fehlercheck
const err = await download.failure();
if (err) throw new Error(err);

// Speichern
await download.saveAs(`/tmp/${download.suggestedFilename()}`);
console.log('Gespeichert:', download.suggestedFilename());

await browser.close();
```

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 9      |
| Properties | 0     |
| Events    | 0 (1 Page-Event: 'download') |

**Fazit:** `saveAs()` + `suggestedFilename()` sind die Kern-Methoden fuer
typische Download-Tests. `failure()` sollte immer geprueft werden, bevor
`path()` aufgerufen wird. `createReadStream()` erlaubt In-Memory-Verarbeitung
ohne Zwischenspeicherung.

---

*Quelle: https://playwright.dev/docs/api/class-download*
