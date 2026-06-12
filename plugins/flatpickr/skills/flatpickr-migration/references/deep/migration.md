# flatpickr — Migration & Browser-Kompatibilität (vollständige Referenz)

## Updating from v2 → v3+

### Breaking Change 1: `utc`-Option entfernt

**Problem:** Die frühere `utc: true`-Option produzierte fehlerhafte Timezone-Daten.

**Vorher (v2):**

```js
flatpickr("#date", { utc: true });
```

**Nachher (v3+):**

```js
// Empfohlen: ISO-Format mit Timezone
flatpickr("#date", {
  dateFormat: "Z",          // ISO 8601: "2024-12-31T14:30:00.000Z"
  altInput: true,
  altFormat: "F j, Y H:i"  // Menschenlesbar für den Nutzer
});

// Wenn die alte dateFormat-Option bereits "Z" enthielt — escapen:
flatpickr("#date", {
  dateFormat: "dHi\\Z M y"  // "Z" als Literal, nicht als ISO-Token
});
```

**Vorteile des ISO-Formats:**
- Korrekte Timezone-Informationen
- Breite Datenbankunterstützung (MySQL, PostgreSQL, etc.)
- Standard-kompatibel (ISO 8601)

### Breaking Change 2: Konstruktor vereinheitlicht

**Vorher (v2):**

```js
// Element
new Flatpickr(element, config);

// Konfiguration
Flatpickr.defaultConfig.dateFormat = "Y-m-d";
```

**Nachher (v3+):**

```js
// Für Modul-Nutzer (Webpack etc.) — kein Änderungsbedarf
flatpickr(element, config);

// Für Script-Tag-Nutzer — einfaches Find & Replace:
// "Flatpickr" → "flatpickr" (überall)
flatpickr.defaultConfig.dateFormat = "Y-m-d";
```

**Migration für Script-Tag-Nutzer:**

Einfaches Suchen & Ersetzen: `Flatpickr` → `flatpickr` (case-sensitive)

Betrifft:
- `new Flatpickr()` → `flatpickr()`
- `Flatpickr.defaultConfig` → `flatpickr.defaultConfig`
- Alle anderen `Flatpickr`-Referenzen

---

## IE9 Support

flatpickr läuft out-of-the-box in **IE10+, Safari 6+, Firefox und Chrome**.

Für IE9-Support sind zwei Schritte nötig:

### Schritt 1: classList-Polyfill

```bash
npm install classlist-polyfill
```

```js
// In der Einstiegsdatei laden (vor flatpickr)
import "classlist-polyfill";
import flatpickr from "flatpickr";
```

Oder via CDN:

```html
<script src="https://npmcdn.com/classlist-polyfill"></script>
```

### Schritt 2: IE9-spezifisches CSS

```html
<!--[if IE 9]>
<link rel="stylesheet" type="text/css" href="https://npmcdn.com/flatpickr/dist/ie.css">
<![endif]-->
```

Oder via npm:

```css
/* In IE9-spezifischem Build */
@import "flatpickr/dist/ie.css";
```

### Webpack + html-webpack-plugin

Für bedingte Stylesheets mit Bundlern: [html-webpack-plugin Issue #155](https://github.com/jantimon/html-webpack-plugin/issues/155)

---

## Browser-Kompatibilitätsmatrix

| Browser | Version | Unterstützt | Anmerkung |
|---------|---------|------------|-----------|
| Chrome | alle modernen | ja | — |
| Firefox | alle modernen | ja | — |
| Safari | 6+ | ja | — |
| Edge | alle | ja | — |
| IE | 10+ | ja | — |
| IE | 9 | mit Polyfill | classList-Polyfill + ie.css |
| IE | < 9 | nein | — |
| iOS Safari | alle | ja | nativer Picker auf Touch-Geräten |
| Android Chrome | alle | ja | nativer Picker auf Touch-Geräten |

---

## Changelog — wichtige Änderungen

### v4.x
- `onKeyDown`-Hook hinzugefügt
- `onParseConfig`-Hook hinzugefügt
- `showMonths`-Option für mehrere Monate gleichzeitig
- `monthSelectorType`-Option (`dropdown` oder `static`)
- Verbesserte Accessibility (ARIA)

### v3.0
- `utc`-Option entfernt (→ `dateFormat: "Z"`)
- `Flatpickr` → `flatpickr` vereinheitlicht
- Plugin-System eingeführt
- Erweiterte Lokalisierung

---

Quelle: https://flatpickr.js.org/updating-from-v2/ | https://flatpickr.js.org/ie9/
