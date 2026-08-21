# shadcn/ui — Calendar

A calendar component built on top of React DayPicker v9. Supports single
date, range, and multiple selection modes.

## Key props

- `mode` — `"single" | "range" | "multiple"`
- `selected` / `onSelect` — controlled selection
- `captionLayout` — `"label" | "dropdown"` (month/year dropdown)
- `showOutsideDays` — show days from adjacent months
- `buttonVariant` — variant for nav buttons
- `locale` — pass `react-day-picker/locale` object for i18n
- `timeZone` — prevents date offset on SSR pages
- `--cell-size` CSS variable — customize day cell size

## Persian / Hijri calendar

Import `DayPicker` from `react-day-picker/persian` instead.

## Reference files

- `CALENDAR-INSTALLATION.md` — CLI and manual install, dependencies
- `CALENDAR-SOURCE.md` — full component source (Radix + Base)
- `CALENDAR-API.md` — all props, CalendarDayButton, CSS variables
- `CALENDAR-EXAMPLES.md` — demo, hijri example
- `CALENDAR-BASE-VS-RADIX.md` — differences (locale prop, cn-* classes)
