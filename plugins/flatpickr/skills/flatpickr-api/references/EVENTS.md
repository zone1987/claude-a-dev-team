# flatpickr — Events and hooks

Hooks are passed as options. Every hook receives `(selectedDates, dateStr, instance)`.
You can pass a single function or an array of functions.

```js
flatpickr("#date", {
  onChange: function(selectedDates, dateStr, instance) {
    console.log("Selected:", dateStr);
  },
  onClose: [fn1, fn2],  // array is allowed
});
```

## Available hooks

| Hook | Trigger |
|------|---------|
| `onChange` | A date/time was selected |
| `onOpen` | The calendar opens |
| `onClose` | The calendar closes |
| `onReady` | The calendar is ready |
| `onValueUpdate` | The input value is updated |
| `onMonthChange` | The month changes |
| `onYearChange` | The year changes |
| `onDayCreate` | Every day DOM element is created |

`onDayCreate` has an extended signature: `(dObj, dStr, fp, dayElem)`.

## Further reading
- [EVENTS-DETAIL.md](EVENTS-DETAIL.md) — complete signatures, parameters, CSS examples for onDayCreate
