# flatpickr — Mobile Support

flatpickr erkennt automatisch mobile Browser und schaltet auf den nativen Datetime-Picker um.
Das gibt Nutzern die gewohnte OS-Erfahrung.

```js
// Standard: automatische Erkennung (empfohlen)
flatpickr("#date", {});

// Nativen Picker erzwingen deaktivieren (nicht empfohlen)
flatpickr("#date", { disableMobile: true });
```

## Nativ unterstützte Features

- Vorausfüllen (`defaultDate`)
- `minDate` / `maxDate`
- `onChange`-Callbacks

## Einschränkungen

Wenn Features wie `disable`-Funktionen verwendet werden, die nativ nicht funktionieren,
fällt flatpickr automatisch auf den eigenen Picker zurück.

## Vertiefung
- [MOBILE-DETAIL.md](MOBILE-DETAIL.md) — vollständige Details, Fallback-Verhalten, Kompatibilitätstabelle
