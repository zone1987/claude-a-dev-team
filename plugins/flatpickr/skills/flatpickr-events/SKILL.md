---
name: flatpickr-events
description: >
  Alle flatpickr Hooks und Events: onChange, onOpen, onClose, onReady, onValueUpdate,
  onMonthChange, onYearChange, onDayCreate, onKeyDown, onParseConfig — Signaturen und Beispiele.
  Trigger: "flatpickr events", "flatpickr hooks", "flatpickr onChange", "flatpickr onOpen",
  "flatpickr onClose", "flatpickr callback", "flatpickr onDayCreate", "flatpickr onReady".
---

# flatpickr — Events & Hooks

Hooks werden als Optionen übergeben. Jeder Hook erhält `(selectedDates, dateStr, instance)`.
Es kann eine einzelne Funktion oder ein Array von Funktionen angegeben werden.

```js
flatpickr("#date", {
  onChange: function(selectedDates, dateStr, instance) {
    console.log("Ausgewählt:", dateStr);
  },
  onClose: [fn1, fn2],  // Array möglich
});
```

## Verfügbare Hooks

| Hook | Auslöser |
|------|---------|
| `onChange` | Datum/Zeit wurde ausgewählt |
| `onOpen` | Kalender öffnet sich |
| `onClose` | Kalender schließt sich |
| `onReady` | Kalender ist bereit |
| `onValueUpdate` | Input-Wert wird aktualisiert |
| `onMonthChange` | Monat wechselt |
| `onYearChange` | Jahr wechselt |
| `onDayCreate` | Jedes Tages-DOM-Element wird erstellt |

`onDayCreate` hat eine erweiterte Signatur: `(dObj, dStr, fp, dayElem)`.

## Vertiefung
- [references/deep/events.md](references/deep/events.md) — vollständige Signaturen, Parameter, CSS-Beispiele für onDayCreate
