# flatpickr — Migration and compatibility

## Updating from v2 → v3+

Two breaking changes:

1. **`utc` option removed** → replace with `dateFormat: "Z"` (ISO format with timezone)
2. **`new Flatpickr()` → `flatpickr()`** → replace all capitalized `Flatpickr` references

```js
// v2 (obsolete)
new Flatpickr(element, { utc: true });

// v3+ (correct)
flatpickr(element, { dateFormat: "Z", altInput: true, altFormat: "F j, Y" });
```

## IE9 support

flatpickr runs out of the box in IE10+. For IE9:

```bash
npm install classlist-polyfill
```

```html
<!--[if IE 9]>
<link rel="stylesheet" href="https://npmcdn.com/flatpickr/dist/ie.css">
<![endif]-->
```

## Further reading
- [MIGRATION-DETAIL.md](MIGRATION-DETAIL.md) — complete migration and IE9 details
