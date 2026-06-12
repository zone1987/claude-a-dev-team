---
name: flatpickr-migration
description: >
  flatpickr Migration von v2 auf v3+: Breaking Changes, IE9-Polyfill, utc-Option entfernt.
  Trigger: "flatpickr migration", "flatpickr update", "flatpickr v2 v3", "flatpickr upgraden",
  "flatpickr utc", "flatpickr IE9", "flatpickr breaking changes", "flatpickr updating from v2",
  "flatpickr ie9 polyfill", "flatpickr classList".
---

# flatpickr — Migration & Kompatibilität

## Updating from v2 → v3+

Zwei Breaking Changes:

1. **`utc`-Option entfernt** → ersetzen durch `dateFormat: "Z"` (ISO-Format mit Timezone)
2. **`new Flatpickr()` → `flatpickr()`** → alle Großbuchstaben-`Flatpickr`-Referenzen ersetzen

```js
// v2 (veraltet)
new Flatpickr(element, { utc: true });

// v3+ (korrekt)
flatpickr(element, { dateFormat: "Z", altInput: true, altFormat: "F j, Y" });
```

## IE9 Support

flatpickr läuft out-of-the-box in IE10+. Für IE9:

```bash
npm install classlist-polyfill
```

```html
<!--[if IE 9]>
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/ie.css">
<![endif]-->
```

## Vertiefung
- [references/deep/migration.md](references/deep/migration.md) — vollständige Migration und IE9-Details
