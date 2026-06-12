---
name: flatpickr-getting-started
description: >
  flatpickr installieren und initialisieren: npm, CDN, CSS, Basis-Init, Selektoren, jQuery.
  Trigger: "flatpickr installieren", "flatpickr einbinden", "flatpickr setup", "flatpickr init",
  "datetime picker install", "flatpickr getting started", "flatpickr npm", "flatpickr CDN".
---

# flatpickr — Getting Started

Leichtgewichtiger Datetime-Picker ohne externe Abhängigkeiten. Läuft in IE10+, Safari 6+, FF, Chrome.

```html
<!-- CDN (schnellster Einstieg) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
<script>flatpickr("#myDate", {});</script>
```

```bash
npm i flatpickr --save
```

```js
import flatpickr from "flatpickr";         // ES Modules / TypeScript
const flatpickr = require("flatpickr");    // CommonJS
```

## Vertiefung
- [references/deep/getting-started.md](references/deep/getting-started.md) — vollständige Installations- und Init-Referenz mit allen Input-Typen
