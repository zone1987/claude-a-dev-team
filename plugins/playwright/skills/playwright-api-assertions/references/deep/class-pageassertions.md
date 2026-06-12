# class-pageassertions — Playwright API Reference

`PageAssertions` ist die Assertion-Klasse fuer `Page`-Objekte. Alle Matcher retrien automatisch. Standardtimeout: `TestConfig.expect` (Standard 5000 ms).

Zugriff via `expect(page).*`.

Matcher-Anzahl: 6 Matcher + Property `not`

---

## not

```typescript
not: PageAssertions
```

Invertiert die nachfolgende Assertion.

```typescript
await expect(page).not.toHaveURL('/error');
```

---

## toHaveScreenshot() — mit Name

```typescript
toHaveScreenshot(
  name: string | string[],
  options?: {
    animations?: 'disabled' | 'allow';
    caret?: 'hide' | 'initial';
    clip?: { x: number; y: number; width: number; height: number };
    fullPage?: boolean;
    mask?: Locator[];
    maskColor?: string;
    maxDiffPixelRatio?: number;
    maxDiffPixels?: number;
    omitBackground?: boolean;
    scale?: 'css' | 'device';
    stylePath?: string | string[];
    threshold?: number;
    timeout?: number;
  }
): Promise<void>
```

Vergleicht einen Seiten-Screenshot mit einem gespeicherten Snapshot. Wartet auf aufeinanderfolgende identische Screenshots, bevor verglichen wird.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `name` | `string \| string[]` | ja | — | Snapshot-Dateiname oder Pfad-Segmente |
| `options.animations` | `'disabled' \| 'allow'` | nein | `'disabled'` | CSS-Animationen behandeln |
| `options.caret` | `'hide' \| 'initial'` | nein | `'hide'` | Text-Cursor-Sichtbarkeit |
| `options.clip` | `{ x; y; width; height }` | nein | ganze Seite | Bereich des Screenshots |
| `options.fullPage` | `boolean` | nein | `false` | Vollstaendige scrollbare Seite aufnehmen |
| `options.mask` | `Locator[]` | nein | `[]` | Zu maskierende Elemente |
| `options.maskColor` | `string` | nein | `'#FF00FF'` | Farbe fuer Maskierung |
| `options.maxDiffPixelRatio` | `number` | nein | aus Config | Maximaler Anteil unterschiedlicher Pixel (0-1) |
| `options.maxDiffPixels` | `number` | nein | aus Config | Maximale Anzahl unterschiedlicher Pixel |
| `options.omitBackground` | `boolean` | nein | `false` | Hintergrund transparent (nur PNG) |
| `options.scale` | `'css' \| 'device'` | nein | `'css'` | Pixel-Masseinheit |
| `options.stylePath` | `string \| string[]` | nein | — | Zusaetzliche CSS-Dateien |
| `options.threshold` | `number` | nein | `0.2` | Farbdifferenz-Schwellenwert (YIQ, 0-1) |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page).toHaveScreenshot('startseite.png');
await expect(page).toHaveScreenshot('full.png', {
  fullPage: true,
  maxDiffPixelRatio: 0.02,
  mask: [page.locator('.live-clock')],
});
```

---

## toHaveScreenshot() — automatisch

```typescript
toHaveScreenshot(options?: {
  animations?: 'disabled' | 'allow';
  caret?: 'hide' | 'initial';
  clip?: { x: number; y: number; width: number; height: number };
  fullPage?: boolean;
  mask?: Locator[];
  maskColor?: string;
  maxDiffPixelRatio?: number;
  maxDiffPixels?: number;
  omitBackground?: boolean;
  scale?: 'css' | 'device';
  stylePath?: string | string[];
  threshold?: number;
  timeout?: number;
}): Promise<void>
```

Wie oben, aber Snapshot-Name wird automatisch aus Testname + Zaehlnummer generiert.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| alle `options.*` | — | nein | — | Identisch mit benannter Variante (ohne `name`) |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page).toHaveScreenshot({ fullPage: true });
```

---

## toHaveTitle()

```typescript
toHaveTitle(
  titleOrRegExp: string | RegExp,
  options?: { timeout?: number }
): Promise<void>
```

Prueft den Titel der aktuellen Seite.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `titleOrRegExp` | `string \| RegExp` | ja | — | Erwarteter Titel (exakter String oder Regex) |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page).toHaveTitle('Meine App - Dashboard');
await expect(page).toHaveTitle(/Dashboard/);
```

---

## toHaveURL()

```typescript
toHaveURL(
  url: string | RegExp | URLPattern | ((url: URL) => boolean),
  options?: {
    ignoreCase?: boolean;
    timeout?: number;
  }
): Promise<void>
```

Prueft die aktuelle URL der Seite.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `url` | `string \| RegExp \| URLPattern \| ((url: URL) => boolean)` | ja | — | Erwartete URL: exakter String, Regex, URLPattern oder Praedikat-Funktion |
| `options.ignoreCase` | `boolean` | nein | `false` | Gross-/Kleinschreibung ignorieren (nur bei String) |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page).toHaveURL('/dashboard');
await expect(page).toHaveURL(/\/user\/\d+/);
await expect(page).toHaveURL(url => url.searchParams.has('token'));
```

---

## toMatchAriaSnapshot() — inline

```typescript
toMatchAriaSnapshot(
  expected: string,
  options?: { timeout?: number }
): Promise<void>
```

Prueft, ob der `<body>` der Seite dem angegebenen ARIA-Snapshot entspricht.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `expected` | `string` | ja | — | ARIA-Snapshot als YAML-String |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page).toMatchAriaSnapshot(`
  - heading "Willkommen" [level=1]
  - link "Anmelden"
`);
```

---

## toMatchAriaSnapshot() — gespeichert

```typescript
toMatchAriaSnapshot(options?: {
  name?: string;
  timeout?: number;
}): Promise<void>
```

Vergleicht mit einer gespeicherten `.aria.yml`-Datei. Bei fehlendem `name` wird der Name automatisch generiert.

| Parameter | Typ | Pflicht | Default | Beschreibung |
|---|---|---|---|---|
| `options.name` | `string` | nein | auto | Dateiname der Snapshot-Datei |
| `options.timeout` | `number` | nein | `TestConfig.expect` | Maximale Wartezeit in ms |

**Rueckgabe:** `Promise<void>`

```typescript
await expect(page).toMatchAriaSnapshot({ name: 'homepage.aria.yml' });
```

---

## Matcher-Uebersicht (6 Matcher)

| Matcher | Prueft |
|---|---|
| `toHaveScreenshot` (2x) | Visuellen Seitenvergleich mit gespeichertem Baseline-Screenshot |
| `toHaveTitle` | `document.title` |
| `toHaveURL` | Aktuelle Seiten-URL |
| `toMatchAriaSnapshot` (2x) | ARIA-Baum des `<body>` |

---

Quelle: https://playwright.dev/docs/api/class-pageassertions
