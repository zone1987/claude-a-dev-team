# flatpickr — Lokalisierung

60+ Locales verfügbar. Locale per Instanz oder global setzen.

```js
// ES Modules — per Instanz
import flatpickr from "flatpickr";
import { German } from "flatpickr/dist/l10n/de.js";

flatpickr("#date", { locale: German });

// Globale Lokalisierung (alle Instanzen)
flatpickr.localize(German);
```

```html
<!-- Browser / CDN -->
<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
<script src="https://npmcdn.com/flatpickr/dist/l10n/de.js"></script>
<script>flatpickr("#date", { locale: "de" });</script>
```

Ersten Wochentag überschreiben:

```js
flatpickr("#date", { locale: { firstDayOfWeek: 1 } }); // Montag
```

## Vertiefung
- [LOCALIZATION-DETAIL.md](LOCALIZATION-DETAIL.md) — vollständige Locale-Liste, Custom Locale, Locale-Typ-Definition
