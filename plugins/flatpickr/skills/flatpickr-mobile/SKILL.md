---
name: flatpickr-mobile
description: >
  flatpickr Mobile-Support: natives Datetime-Input, automatische Erkennung, disableMobile.
  Trigger: "flatpickr mobile", "flatpickr smartphone", "flatpickr native input",
  "flatpickr disableMobile", "flatpickr ios", "flatpickr android", "flatpickr touch",
  "flatpickr mobile support", "flatpickr nativer picker".
---

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
- [references/deep/mobile.md](references/deep/mobile.md) — vollständige Details, Fallback-Verhalten, Kompatibilitätstabelle
