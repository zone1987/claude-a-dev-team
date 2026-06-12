# Playwright — class: Coverage

> **Manifest:** 4 Methoden, 0 Properties, 0 Events.
> Erfasst JavaScript- und CSS-Codeabdeckung waehrend der Seitenausfuehrung.
> **Nur in Chromium-basierten Browsern verfuegbar.** Zugriff: `page.coverage`.

---

## Uebersicht

`Coverage` sammelt Informationen darueber, welche Teile von JavaScript- und
CSS-Code waehrend einer Sitzung tatsaechlich ausgefuehrt wurden. Die
gesammelten Daten koennen mit Tools wie `v8-to-istanbul` in Istanbul/NYC-
kompatible Coverage-Berichte konvertiert werden.

**Wichtig:** Coverage ist ausschliesslich in Chromium/Chrome verfuegbar.
In Firefox und WebKit sind diese APIs nicht unterstuetzt.

---

## Methoden

### coverage.startCSSCoverage(options?)

Startet die CSS-Coverage-Erfassung.

**Signatur:**
```typescript
coverage.startCSSCoverage(options?: {
  resetOnNavigation?: boolean;
}): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `options.resetOnNavigation` | `boolean` | nein | `true` | Ob die Coverage bei jeder Navigation zurueckgesetzt wird |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await page.coverage.startCSSCoverage({ resetOnNavigation: false });
await page.goto('https://example.com');
// ... Interaktionen ...
const coverage = await page.coverage.stopCSSCoverage();
```

---

### coverage.startJSCoverage(options?)

Startet die JavaScript-Coverage-Erfassung.

**Signatur:**
```typescript
coverage.startJSCoverage(options?: {
  reportAnonymousScripts?: boolean;
  resetOnNavigation?: boolean;
}): Promise<void>
```

**Parameter:**

| Name | Typ | Pflicht | Default | Beschreibung |
|------|-----|---------|---------|--------------|
| `options.reportAnonymousScripts` | `boolean` | nein | `false` | Anonyme Skripte (via `eval` oder `new Function`) erfassen; erhalten die URL `__playwright_evaluation_script__` |
| `options.resetOnNavigation` | `boolean` | nein | `true` | Ob die Coverage bei jeder Navigation zurueckgesetzt wird |

**Rueckgabe:** `Promise<void>`

**Beispiel:**
```javascript
await page.coverage.startJSCoverage({ reportAnonymousScripts: true });
```

---

### coverage.stopCSSCoverage()

Beendet die CSS-Coverage-Erfassung und gibt die gesammelten Daten zurueck.

**Signatur:**
```typescript
coverage.stopCSSCoverage(): Promise<Array<{
  url: string;
  text?: string;
  ranges: Array<{
    start: number;
    end: number;
  }>;
}>>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<Array<CSSCoverageEntry>>` mit:

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `url` | `string` | URL des Stylesheets |
| `text` | `string` (optional) | Stylesheet-Inhalt (falls verfuegbar) |
| `ranges` | `Array<{start, end}>` | Genutzte Bereiche (sortiert, nicht ueberlappend) |
| `ranges[].start` | `number` | Inklusiver Text-Offset (Zeichen) |
| `ranges[].end` | `number` | Exklusiver Text-Offset (Zeichen) |

**Hinweis:** Dynamisch injizierte Styles ohne `sourceURL` werden nicht
erfasst.

**Beispiel:**
```javascript
const cssCoverage = await page.coverage.stopCSSCoverage();
for (const entry of cssCoverage) {
  const totalChars = entry.text?.length ?? 0;
  const usedChars = entry.ranges.reduce((acc, r) => acc + (r.end - r.start), 0);
  const pct = totalChars > 0 ? (usedChars / totalChars * 100).toFixed(1) : 'N/A';
  console.log(`${entry.url}: ${pct}% CSS genutzt`);
}
```

---

### coverage.stopJSCoverage()

Beendet die JavaScript-Coverage-Erfassung und gibt die Daten im V8-Format
zurueck.

**Signatur:**
```typescript
coverage.stopJSCoverage(): Promise<Array<{
  url: string;
  scriptId: string;
  source?: string;
  functions: Array<{
    functionName: string;
    isBlockCoverage: boolean;
    ranges: Array<{
      count: number;
      startOffset: number;
      endOffset: number;
    }>;
  }>;
}>>
```

**Parameter:** Keine

**Rueckgabe:** `Promise<Array<JSCoverageEntry>>` mit:

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `url` | `string` | Skript-URL |
| `scriptId` | `string` | Interne Skript-ID des Browsers |
| `source` | `string` (optional) | Skript-Quellcode (falls verfuegbar) |
| `functions` | `Array<...>` | V8 Coverage-Daten pro Funktion |
| `functions[].functionName` | `string` | Funktionsname (leer fuer Anonym) |
| `functions[].isBlockCoverage` | `boolean` | Ob Block-Coverage oder Zeilen-Coverage |
| `functions[].ranges` | `Array<...>` | Abdeckungs-Bereiche |
| `functions[].ranges[].count` | `number` | Ausfuehrungs-Zaehler |
| `functions[].ranges[].startOffset` | `number` | Start-Offset im Quellcode |
| `functions[].ranges[].endOffset` | `number` | End-Offset im Quellcode |

**Hinweis:** Anonyme Skripte werden ausgeschlossen, sofern
`reportAnonymousScripts: true` nicht gesetzt wurde.

---

## Vollstaendiges Beispiel (Istanbul-Integration)

```javascript
const { chromium } = require('playwright');
const v8toIstanbul = require('v8-to-istanbul');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  await page.coverage.startJSCoverage();
  await page.goto('https://chromium.org');
  // ... Interaktionen ...
  const jsCoverage = await page.coverage.stopJSCoverage();

  for (const entry of jsCoverage) {
    const converter = v8toIstanbul('', 0, { source: entry.source });
    await converter.load();
    converter.applyCoverage(entry.functions);
    console.log(JSON.stringify(converter.toIstanbul()));
  }

  await browser.close();
})();
```

---

## Manifest

| Kategorie | Anzahl |
|-----------|--------|
| Methoden  | 4      |
| Properties | 0     |
| Events    | 0      |

**Fazit:** Die Coverage-API liefert V8-native Abdeckungsdaten, die fuer moderne
Code-Coverage-Reports geeignet sind. Fuer CSS-Optimierungen (unused CSS
entfernen) ist `stopCSSCoverage()` besonders wertvoll. Die Daten muessen
extern (z.B. via `v8-to-istanbul`) konvertiert werden, da Playwright selbst
keine Coverage-Reports generiert.

---

*Quelle: https://playwright.dev/docs/api/class-coverage*
