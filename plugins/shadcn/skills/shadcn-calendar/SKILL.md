---
name: shadcn-calendar
description: >
  shadcn/ui Calendar component — date picker calendar built on
  react-day-picker. Use when asked about Calendar, Kalender, shadcn calendar,
  Datumsauswahl, date picker, CalendarDayButton, range calendar,
  hijri persian calendar, react-day-picker shadcn.
---

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

- `references/installation.md` — CLI and manual install, dependencies
- `references/source.md` — full component source (Radix + Base)
- `references/api.md` — all props, CalendarDayButton, CSS variables
- `references/examples.md` — demo, hijri example
- `references/base-vs-radix.md` — differences (locale prop, cn-* classes)
