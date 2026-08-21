# flatpickr — Configuration options

All options are passed as the second argument to `flatpickr(el, { ... })`.

```js
flatpickr("#date", {
  enableTime: true,
  dateFormat: "Y-m-d H:i",
  minDate: "today",
  mode: "range",
});
```

The most important options at a glance:

| Option | Default | Description |
|--------|---------|--------------|
| `dateFormat` | `"Y-m-d"` | Format of the value in the input |
| `altInput` | `false` | Shows a readable date, submits the machine format |
| `enableTime` | `false` | Enable time selection |
| `mode` | `"single"` | `"single"`, `"multiple"`, `"range"` |
| `inline` | `false` | Calendar always open |
| `minDate`/`maxDate` | `null` | Date boundaries |
| `disable`/`enable` | `[]` | Block/allow days |
| `locale` | `"default"` | Language/localization |

## Further reading
- [OPTIONS-DETAIL.md](OPTIONS-DETAIL.md) — exhaustive table of all options with type, default and description
