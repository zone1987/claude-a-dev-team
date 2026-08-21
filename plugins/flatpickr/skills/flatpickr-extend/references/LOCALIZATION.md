# flatpickr — Localization

60+ locales available. Set the locale per instance or globally.

```js
// ES Modules — per instance
import flatpickr from "flatpickr";
import { German } from "flatpickr/dist/l10n/de.js";

flatpickr("#date", { locale: German });

// Global localization (all instances)
flatpickr.localize(German);
```

```html
<!-- Browser / CDN -->
<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
<script src="https://npmcdn.com/flatpickr/dist/l10n/de.js"></script>
<script>flatpickr("#date", { locale: "de" });</script>
```

Override the first day of the week:

```js
flatpickr("#date", { locale: { firstDayOfWeek: 1 } }); // Monday
```

## Further reading
- [LOCALIZATION-DETAIL.md](LOCALIZATION-DETAIL.md) — complete locale list, custom locale, locale type definition
