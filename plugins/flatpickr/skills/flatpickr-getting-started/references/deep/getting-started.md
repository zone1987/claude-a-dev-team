# flatpickr — Getting Started (vollständige Referenz, v4.6.13)

## Version

**flatpickr v4.6.13** (aktuelle stabile Version)

## Installation

### npm

```bash
npm i flatpickr --save
# Installiert v4.6.13 (aktuelle Stable)
```

### CDN (jsDelivr)

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
```

### CDN (npmcdn / unpkg)

```html
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/flatpickr.min.css">
<script src="https://npmcdn.com/flatpickr"></script>
```

## Modul-Import

```js
// ES Modules (empfohlen für TypeScript / Webpack / Vite)
import flatpickr from "flatpickr";

// CommonJS (Node / older bundlers)
const flatpickr = require("flatpickr");
```

**CSS in Webpack/Bundler:**

```js
import "flatpickr/dist/flatpickr.min.css";
// oder für ein Theme:
import "flatpickr/dist/themes/dark.css";
```

## Initialisierung — alle Varianten

### 1. ID-Selektor (String)

```js
flatpickr("#myID", {});
```

### 2. CSS-Klassen-Selektor — mehrere Instanzen auf einmal

```js
flatpickr(".datepicker", {});
// Gibt ein Array von flatpickr-Instanzen zurück
```

### 3. DOM-Element direkt übergeben (empfohlen für Frameworks)

```js
const el = document.getElementById("myDate");
flatpickr(el, { enableTime: true });
```

### 4. NodeList

```js
const inputs = document.querySelectorAll(".date-input");
flatpickr(inputs, { dateFormat: "d.m.Y" });
```

### 5. jQuery Plugin

```js
$(".selector").flatpickr({ /* optionen */ });
```

> Hinweis: Bei Framework-Integrationen (React, Vue, Angular) sollte immer das DOM-Element direkt übergeben werden, nicht ein String-Selektor.

## Konfigurationsparameter

Alle Optionen sind optional. Das zweite Argument `{}` kann vollständig weggelassen werden:

```js
flatpickr("#date");                      // keine Optionen
flatpickr("#date", { inline: true });   // mit Optionen
```

Die vollständige Options-Referenz: siehe [flatpickr-options](../../flatpickr-options/SKILL.md).

## Unterstützte Input-Typen

flatpickr funktioniert mit allen Standard-HTML-Inputs und auch mit nicht-input-Elementen:

```html
<!-- Standard text input -->
<input type="text" id="date1" placeholder="Datum wählen">

<!-- Bereits vorausgefüllter Wert -->
<input type="text" id="date2" value="2024-01-15">

<!-- Inline auf einem div -->
<div id="inline-calendar"></div>
```

```js
flatpickr("#date1", {});
flatpickr("#date2", { dateFormat: "Y-m-d" });
flatpickr("#inline-calendar", { inline: true });
```

## Rückgabewert

`flatpickr()` gibt eine flatpickr-Instanz (oder ein Array davon bei Mehrfachselektion) zurück:

```js
const fp = flatpickr("#myDate", { enableTime: true });

// Später:
fp.open();
fp.setDate("2024-06-15");
fp.destroy();
```

## TypeScript

flatpickr enthält eigene Typdeklarationen (`@types` nicht nötig):

```ts
import flatpickr from "flatpickr";
import { Instance } from "flatpickr/dist/types/instance";
import { Options } from "flatpickr/dist/types/options";

const opts: Options = {
  enableTime: true,
  dateFormat: "Y-m-d H:i",
};

const fp: Instance = flatpickr("#myDate", opts) as Instance;
```

## Browser-Kompatibilität

| Browser | Unterstützt |
|---------|------------|
| Chrome | ja |
| Firefox | ja |
| Safari 6+ | ja |
| IE 10+ | ja |
| IE 9 | mit Polyfill (classList) |

Für IE9-Details: siehe [flatpickr-migration](../../flatpickr-migration/SKILL.md).

---

Quelle: `package.json` v4.6.13 | https://flatpickr.js.org/getting-started/ | https://flatpickr.js.org/
