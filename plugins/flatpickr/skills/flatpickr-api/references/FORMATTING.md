# flatpickr — Formatting tokens

`dateFormat` and `altFormat` are composed from these tokens.

```js
flatpickr("#date", {
  dateFormat: "d.m.Y",      // 31.12.2024
  enableTime: true,
  dateFormat: "Y-m-d H:i",  // 2024-12-31 14:30
});
```

Quick reference of the most common tokens:

| Token | Description | Example |
|-------|-------------|---------|
| `Y` | 4-digit year | `2024` |
| `y` | 2-digit year | `24` |
| `m` | Month with leading zero | `01`–`12` |
| `n` | Month without leading zero | `1`–`12` |
| `d` | Day with leading zero | `01`–`31` |
| `j` | Day without leading zero | `1`–`31` |
| `H` | Hour, 24h | `00`–`23` |
| `h` | Hour, 12h | `1`–`12` |
| `i` | Minutes | `00`–`59` |
| `S` | Seconds (2-digit) | `00`–`59` |
| `K` | AM/PM | `AM`/`PM` |

## Further reading
- [FORMATTING-DETAIL.md](FORMATTING-DETAIL.md) — complete token table including weekday, week, Unix timestamp, ISO
