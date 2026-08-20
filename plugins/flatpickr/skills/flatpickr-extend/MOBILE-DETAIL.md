# flatpickr — Mobile Support (complete reference)

## Automatic detection

flatpickr detects mobile browsers automatically and switches to the **native datetime picker**
of the operating system. This gives the user the familiar OS experience.

Detection is based on the browser user agent. On mobile devices (iOS, Android) a native
`<input type="date">`, `<input type="datetime-local">` or
`<input type="time">` is used.

## Natively supported features

The following flatpickr features are forwarded to the native picker:

| Feature | Supported |
|---------|------------|
| `defaultDate` | yes |
| `minDate` | yes |
| `maxDate` | yes |
| `onChange` callback | yes |
| `disable` (array/function) | no* |
| `enableTime` | yes (native datetime-local) |
| `noCalendar` | yes (native time) |
| Plugins | no |

*When features are used that are not available natively (e.g. `disable` functions),
flatpickr automatically falls back to its own picker.

## Fallback behavior

When a configuration that cannot be supported natively is detected, the flatpickr picker
is shown on mobile devices as well:

```js
// automatically falls back to the flatpickr picker (no native picker)
flatpickr("#date", {
  disable: [function(date) { return date.getDay() === 0; }]
});
```

## Disabling the native picker

```js
flatpickr("#date", {
  disableMobile: true   // always the flatpickr picker, never the native one
});
```

**Recommendation:** Use only when flatpickr-specific features (e.g. themes, plugins,
`onDayCreate`) are strictly required on mobile devices. The native picker generally offers
better UX on mobile devices.

## Global mobile configuration

```js
// make all instances skip the native picker
flatpickr(".datepicker", {
  disableMobile: true
});
```

## Type mapping

| flatpickr configuration | Native input type |
|------------------------|-------------------|
| default (date only) | `type="date"` |
| `enableTime: true` | `type="datetime-local"` |
| `noCalendar: true`, `enableTime: true` | `type="time"` |

## Browser compatibility

| Browser/OS | Native picker |
|-----------|---------------|
| iOS Safari | yes (native) |
| iOS Chrome | yes (native) |
| Android Chrome | yes (native) |
| Android Firefox | yes (native) |
| Desktop Chrome | flatpickr |
| Desktop Firefox | flatpickr |
| Desktop Safari | flatpickr |

---

Source: https://flatpickr.js.org/mobile-support/
