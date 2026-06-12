---
name: flatpickr-formatting
description: >
  Alle flatpickr Datum/Zeit-Formatierungstokens: Zeichen, Beschreibung, Beispielwerte.
  Trigger: "flatpickr format", "flatpickr dateFormat", "flatpickr altFormat", "flatpickr datum formatieren",
  "flatpickr tokens", "flatpickr Y-m-d", "flatpickr H:i", "flatpickr date format tokens",
  "flatpickr formatting", "flatpickr Datumsformat".
---

# flatpickr — Formatierungstokens

`dateFormat` und `altFormat` werden mit diesen Tokens zusammengesetzt.

```js
flatpickr("#date", {
  dateFormat: "d.m.Y",      // 31.12.2024
  enableTime: true,
  dateFormat: "Y-m-d H:i",  // 2024-12-31 14:30
});
```

Kurzreferenz häufigster Tokens:

| Token | Beschreibung | Beispiel |
|-------|-------------|---------|
| `Y` | 4-stelliges Jahr | `2024` |
| `y` | 2-stelliges Jahr | `24` |
| `m` | Monat mit führender Null | `01`–`12` |
| `n` | Monat ohne führende Null | `1`–`12` |
| `d` | Tag mit führender Null | `01`–`31` |
| `j` | Tag ohne führende Null | `1`–`31` |
| `H` | Stunde 24h | `00`–`23` |
| `h` | Stunde 12h | `1`–`12` |
| `i` | Minuten | `00`–`59` |
| `S` | Sekunden (2-stellig) | `00`–`59` |
| `K` | AM/PM | `AM`/`PM` |

## Vertiefung
- [references/deep/formatting.md](references/deep/formatting.md) — vollständige Token-Tabelle inkl. Wochentag, Woche, Unix-Timestamp, ISO
