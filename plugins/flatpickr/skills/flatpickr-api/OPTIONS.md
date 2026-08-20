# flatpickr — Konfigurationsoptionen

Alle Optionen werden als zweites Argument an `flatpickr(el, { ... })` übergeben.

```js
flatpickr("#date", {
  enableTime: true,
  dateFormat: "Y-m-d H:i",
  minDate: "today",
  mode: "range",
});
```

Wichtigste Optionen auf einen Blick:

| Option | Default | Beschreibung |
|--------|---------|--------------|
| `dateFormat` | `"Y-m-d"` | Format des Werts im Input |
| `altInput` | `false` | Zeigt lesbares Datum, sendet Maschinenformat |
| `enableTime` | `false` | Zeitauswahl aktivieren |
| `mode` | `"single"` | `"single"`, `"multiple"`, `"range"` |
| `inline` | `false` | Kalender immer offen |
| `minDate`/`maxDate` | `null` | Datum-Grenzen |
| `disable`/`enable` | `[]` | Tage sperren/freigeben |
| `locale` | `"default"` | Sprache/Lokalisierung |

## Vertiefung
- [OPTIONS-DETAIL.md](OPTIONS-DETAIL.md) — erschöpfende Tabelle aller Optionen mit Typ, Default und Beschreibung
