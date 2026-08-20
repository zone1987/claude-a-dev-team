# flatpickr — Mobile Support

flatpickr detects mobile browsers automatically and switches to the native datetime picker.
This gives users the OS experience they are used to.

```js
// default: automatic detection (recommended)
flatpickr("#date", {});

// disable the forced native picker (not recommended)
flatpickr("#date", { disableMobile: true });
```

## Natively supported features

- Prefilling (`defaultDate`)
- `minDate` / `maxDate`
- `onChange` callbacks

## Limitations

When features such as `disable` functions are used that do not work natively,
flatpickr automatically falls back to its own picker.

## Further reading
- [MOBILE-DETAIL.md](MOBILE-DETAIL.md) — complete details, fallback behavior, compatibility table
