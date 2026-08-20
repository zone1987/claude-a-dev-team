# flatpickr — Beispiele & Patterns

```js
// DateTime-Picker
flatpickr("#dt", { enableTime: true, dateFormat: "Y-m-d H:i" });

// Datumsbereich (Range)
flatpickr("#range", { mode: "range" });

// Zeitauswahl ohne Kalender
flatpickr("#time", { enableTime: true, noCalendar: true, dateFormat: "H:i" });

// Menschenlesbar anzeigen, Maschinenformat senden
flatpickr("#alt", { altInput: true, altFormat: "F j, Y", dateFormat: "Y-m-d" });

// Wochenenden sperren
flatpickr("#wd", {
  disable: [d => d.getDay() === 0 || d.getDay() === 6]
});
```

## Vertiefung
- [EXAMPLES-DETAIL.md](EXAMPLES-DETAIL.md) — alle dokumentierten Beispiele mit vollständigen Configs und HTML
