# class-snapshotassertions — Playwright API Reference

`SnapshotAssertions` bietet Methoden zum Vergleich von Strings oder Buffer-Werten mit gespeicherten Snapshots. Kein auto-retry. Fuer Screenshots von Seiten oder Elementen sollte stattdessen `expect(page).toHaveScreenshot()` bzw. `expect(locator).toHaveScreenshot()` verwendet werden.

Zugriff via `expect(value).toMatchSnapshot(...)`.

Methoden-Anzahl: 2 (toMatchSnapshot mit und ohne Name)

---

## toMatchSnapshot() — mit Name

```typescript
toMatchSnapshot(
  name: string | string[],
  options?: {
    maxDiffPixels?: number;
    maxDiffPixelRatio?: number;
    threshold?: number;
  }
): Promise<void>
```

Vergleicht einen `string`- oder `Buffer`-Wert mit dem gespeicherten Snapshot unter dem angegebenen Namen.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `name` | `string \| string[]` | ja | — | Snapshot-Dateiname oder Array von Pfadsegmenten |
| `options.maxDiffPixels` | `number` | nein | aus `TestConfig.expect` | Maximale Anzahl erlaubter unterschiedlicher Pixel |
| `options.maxDiffPixelRatio` | `number` | nein | aus `TestConfig.expect` | Maximaler Anteil unterschiedlicher Pixel (0-1) |
| `options.threshold` | `number` | nein | `0.2` | Wahrgenommene Farbdifferenz-Toleranz im YIQ-Farbraum (0 = streng, 1 = permissiv) |

**Rueckgabe:** `Promise<void>`

```typescript
// String-Snapshot
expect(generatedCSV).toMatchSnapshot('export.csv');

// Buffer-Snapshot (z.B. PDF)
const pdfBuffer = await page.pdf();
expect(pdfBuffer).toMatchSnapshot('report.pdf');

// Pfad-Segmente
expect(xmlData).toMatchSnapshot(['exports', 'data.xml']);
```

---

## toMatchSnapshot() — automatisch

```typescript
toMatchSnapshot(options?: {
  name?: string | string[];
  maxDiffPixels?: number;
  maxDiffPixelRatio?: number;
  threshold?: number;
}): Promise<void>
```

Vergleicht mit einem Snapshot; Name wird aus dem Testnamen und einer Ordinalzahl generiert, wenn `name` fehlt.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.name` | `string \| string[]` | nein | auto (Testname + Zaehlnummer) | Optionaler Snapshot-Name |
| `options.maxDiffPixels` | `number` | nein | aus `TestConfig.expect` | Maximale Anzahl erlaubter unterschiedlicher Pixel |
| `options.maxDiffPixelRatio` | `number` | nein | aus `TestConfig.expect` | Maximaler Anteil unterschiedlicher Pixel (0-1) |
| `options.threshold` | `number` | nein | `0.2` | Farbdifferenz-Toleranz (YIQ-Farbraum, 0-1) |

**Rueckgabe:** `Promise<void>`

```typescript
// Automatisch benannt (erster Aufruf im Test = "-1", zweiter = "-2", usw.)
expect(jsonOutput).toMatchSnapshot();

// Mit explizitem Namen im options-Objekt
expect(htmlContent).toMatchSnapshot({ name: 'rendered-template.html' });
expect(imageBuffer).toMatchSnapshot({
  name: 'thumbnail.png',
  threshold: 0.1,
  maxDiffPixels: 100,
});
```

---

## Hinweise zur Verwendung

**Snapshot-Aktualisierung:** Beim ersten Aufruf wird der Snapshot erstellt. Zur Aktualisierung:

```bash
npx playwright test --update-snapshots
```

**Speicherort:** Snapshots werden standardmaessig in einem `__snapshots__`-Verzeichnis neben der Testdatei gespeichert. Konfigurierbar via `TestConfig.snapshotDir`.

**Abgrenzung zu `toHaveScreenshot`:**
- `toMatchSnapshot` fuer beliebige `string`- oder `Buffer`-Werte
- `expect(page).toHaveScreenshot()` fuer Seiten-Screenshots (mit Stabilisierungs-Wartezeit)
- `expect(locator).toHaveScreenshot()` fuer Element-Screenshots

---

## Methoden-Uebersicht (2 Methoden)

| Methode | Beschreibung |
|---|---|
| `toMatchSnapshot(name, options?)` | Vergleich mit benanntem Snapshot |
| `toMatchSnapshot(options?)` | Vergleich mit auto-benanntem Snapshot |

---

Quelle: https://playwright.dev/docs/api/class-snapshotassertions
