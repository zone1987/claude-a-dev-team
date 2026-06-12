---
name: flatpickr-examples
description: >
  flatpickr Beispiele und Patterns: DateTime, Range, Multiple, Time-only, Inline, Disable,
  altInput, Preloading, Wrap/Input-Groups, Custom Parsing/Formatting.
  Trigger: "flatpickr beispiele", "flatpickr examples", "flatpickr datetime", "flatpickr range",
  "flatpickr multiple", "flatpickr time only", "flatpickr inline", "flatpickr disable dates",
  "flatpickr preload", "flatpickr input group", "flatpickr wrap", "flatpickr patterns".
---

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
- [references/deep/examples.md](references/deep/examples.md) — alle dokumentierten Beispiele mit vollständigen Configs und HTML
