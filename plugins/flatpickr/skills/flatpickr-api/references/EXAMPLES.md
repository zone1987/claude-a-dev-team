# flatpickr — Examples and patterns

```js
// DateTime picker
flatpickr("#dt", { enableTime: true, dateFormat: "Y-m-d H:i" });

// Date range
flatpickr("#range", { mode: "range" });

// Time selection without a calendar
flatpickr("#time", { enableTime: true, noCalendar: true, dateFormat: "H:i" });

// Display human-readable, submit machine format
flatpickr("#alt", { altInput: true, altFormat: "F j, Y", dateFormat: "Y-m-d" });

// Block weekends
flatpickr("#wd", {
  disable: [d => d.getDay() === 0 || d.getDay() === 6]
});
```

## Further reading
- [EXAMPLES-DETAIL.md](EXAMPLES-DETAIL.md) — all documented examples with complete configs and HTML
