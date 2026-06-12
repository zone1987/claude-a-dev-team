# Playwright — class: FileChooser

> **Manifest:** 4 Methoden, 0 Properties, 0 Events (1 externer Page-Event).
> Repraesentiert einen vom Browser geoeffneten Dateiauswahl-Dialog.
> Instanzen werden ueber `page.on('filechooser')` bzw. `page.waitForEvent('filechooser')` erhalten.

---

## Uebersicht

`FileChooser` entsteht, wenn ein `<input type="file">`-Element aktiviert wird.
Der Dialog wird nicht wirklich geoeffnet — Playwright interceptiert ihn und
erlaubt das programmatische Setzen von Dateien ueber `setFiles()`.

```javascript
const fileChooserPromise = page.waitForEvent('filechooser');
await page.getByText('Datei hochladen').click();
const fileChooser = await fileChooserPromise;
await fileChooser.setFiles('/path/to/myfile.pdf');
```

---

## Methoden

### fileChooser.element()

Gibt das `<input type="file">`-Element zurueck, das den FileChooser
ausgeloest hat.

**Signatur:**
```typescript
fileChooser.element(): ElementHandle
```

**Parameter:** Keine

**Rueckgabe:** `ElementHandle` — das Input-Element

**Hinzugefuegt:** Vor v1.9

**Beispiel:**
```javascript
const input = fileChooser.element();
const accept = await input.getAttribute('accept');
console.log('Erlaubte Typen:', accept); // z.B. ".pdf,.docx"
```

---

### fileChooser.isMultiple()

Gibt an, ob der FileChooser mehrere Dateien gleichzeitig akzeptiert
(`multiple`-Attribut gesetzt).

**Signatur:**
```typescript
fileChooser.isMultiple(): boolean
```

**Parameter:** Keine

**Rueckgabe:** `boolean` — `true` wenn `multiple` gesetzt ist

**Hinzugefuegt:** Vor v1.9

**Beispiel:**
```javascript
if (fileChooser.isMultiple()) {
  await fileChooser.setFiles(['/path/file1.jpg', '/path/file2.jpg']);
} else {
  await fileChooser.setFiles('/path/file1.jpg');
}
```

---

### fileChooser.page()

Gibt die Seite zurueck, zu der dieser FileChooser gehoert.

**Signatur:**
```typescript
fileChooser.page(): Page
```

**Parameter:** Keine

**Rueckgabe:** `Page`

**Hinzugefuegt:** Vor v1.9

**Beispiel:**
```javascript
const p = fileChooser.page();
console.log('Seite:', p.url());
```

---

### fileChooser.setFiles(files, options?)

Setzt die Dateien fuer das Input-Element. Setzt damit den Dialog-Auswahl.

**Signatur:**
```typescript
fileChooser.setFiles(
  files: string | Array<string> | {
    name: string;
    mimeType: string;
    buffer: Buffer;
  } | Array<{
    name: string;
    mimeType: string;
    buffer: Buffer;
  }>,
  options?: {
    noWaitAfter?: boolean;
    timeout?: number;
  }
): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `files` | `string \| string[] \| FilePayload \| FilePayload[]` | ja | — | Dateipfad(e) oder Datei-Buffer-Objekte. Relative Pfade werden relativ zum CWD aufgeloest. Leeres Array loescht die Auswahl. |
| `files[].name` | `string` | ja (bei Buffer) | — | Dateiname inkl. Endung |
| `files[].mimeType` | `string` | ja (bei Buffer) | — | MIME-Typ, z.B. `"application/pdf"` |
| `files[].buffer` | `Buffer` | ja (bei Buffer) | — | Datei-Inhalt als Buffer |
| `options.noWaitAfter` | `boolean` | nein | — | Deprecated; hat keinen Effekt mehr |
| `options.timeout` | `number` | nein | `0` | Maximale Wartezeit in Millisekunden (`0` = kein Timeout) |

**Rueckgabe:** `Promise<void>`

**Hinzugefuegt:** Vor v1.9

**Beispiele:**

```javascript
// Einfacher Pfad
await fileChooser.setFiles('/home/user/dokument.pdf');

// Mehrere Pfade
await fileChooser.setFiles([
  '/home/user/bild1.jpg',
  '/home/user/bild2.jpg'
]);

// In-Memory Buffer (kein echtes Filesystem noetig)
await fileChooser.setFiles({
  name: 'test.txt',
  mimeType: 'text/plain',
  buffer: Buffer.from('Dateiinhalt hier')
});

// Auswahl zuruecksetzen
await fileChooser.setFiles([]);
```

---

## Page-Event: 'filechooser'

```javascript
page.on('filechooser', async (fileChooser) => {
  await fileChooser.setFiles('/path/to/file.jpg');
});
```

Oder als einmaliges Warten vor dem ausloesenden Klick:

```javascript
const [fileChooser] = await Promise.all([
  page.waitForEvent('filechooser'),
  page.click('#upload-button')
]);
await fileChooser.setFiles('/path/to/file.jpg');
```

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 4      |
| Properties | 0     |
| Events    | 0 (1 Page-Event: 'filechooser') |

**Fazit:** `setFiles()` ist die einzige relevante Aktionsmethode. `isMultiple()`
sollte vor dem Setzen mehrerer Dateien geprueft werden. Die Buffer-Variante
von `setFiles()` ist besonders nuetzlich in CI-Umgebungen, wo kein echtes
Filesystem-Fixture benoetigt wird.

---

*Quelle: https://playwright.dev/docs/api/class-filechooser*
