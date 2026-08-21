# flatpickr — Instance API

```js
const fp = flatpickr("#date", { enableTime: true });

fp.open();                        // open the calendar
fp.setDate("2024-06-15");         // set the date programmatically
fp.set("minDate", "today");       // change an option dynamically
fp.destroy();                     // remove the instance
```

## Most important methods

| Method | Description |
|---------|-------------|
| `open()` | Open the calendar |
| `close()` | Close the calendar |
| `toggle()` | Open/close the calendar |
| `clear()` | Clear the selection and the input |
| `destroy()` | Remove the instance completely |
| `setDate(date, triggerChange?)` | Set the date |
| `set(option, value)` | Change a config option |
| `changeMonth(n, isOffset?)` | Change the month |
| `jumpToDate(date)` | Jump to a date |

## Most important properties

| Property | Type | Description |
|----------|-----|-------------|
| `selectedDates` | `Date[]` | Currently selected dates |
| `currentYear` | `number` | Displayed year |
| `currentMonth` | `number` | Displayed month (0–11) |
| `config` | `object` | Active configuration |

## Further reading
- [INSTANCE-DETAIL.md](INSTANCE-DETAIL.md) — complete methods, properties, DOM elements, static helpers
