# shadcn-vue Calendar Component

## Triggers
shadcn-vue calendar, calendar vue, datepicker vue, kalender vue, date selector vue, calendar reka-ui vue, datumsauswahl vue, date picker component vue, calendar shadcn

## Overview

The `Calendar` component is a full-featured, accessible date picker calendar built on top of `reka-ui`'s `CalendarRoot` and `@internationalized/date`. It supports single date, multiple date, and range selection (via the separate `RangeCalendar` component), multiple calendar systems (Gregorian, Persian, Japanese, etc.), and flexible heading layouts with dropdown selectors for month and year navigation.

## Sub-components (12)

| Component | Description |
|---|---|
| `Calendar` | Root wrapper component — orchestrates all sub-components, layout, and dropdowns |
| `CalendarCell` | Wraps a single day cell in the grid |
| `CalendarCellTrigger` | The clickable button inside a cell; handles selected/today/disabled/unavailable/outside-view states |
| `CalendarGrid` | Container for a single month grid |
| `CalendarGridBody` | The `<tbody>` equivalent containing rows of week dates |
| `CalendarGridHead` | The `<thead>` equivalent containing the week-day header row |
| `CalendarGridRow` | A single row (week) inside the grid body or head |
| `CalendarHeadCell` | A single weekday header cell (e.g. "Mo", "Tu") |
| `CalendarHeader` | The top navigation bar containing prev/next buttons and the heading |
| `CalendarHeading` | Default month+year text label in the header |
| `CalendarNextButton` | Button to advance to the next month/year |
| `CalendarPrevButton` | Button to go back to the previous month/year |

## Layout Types

The `layout` prop controls how the calendar heading is rendered:

| Value | Description |
|---|---|
| `undefined` (default) | Plain text heading via `<CalendarHeading />` |
| `"month-and-year"` | Two `<NativeSelect>` dropdowns — one for month, one for year |
| `"month-only"` | Month dropdown + static year text |
| `"year-only"` | Static month text + year dropdown |

The heading can also be fully customized via the `#calendar-heading` scoped slot, which exposes `date`, `month` (MonthTemplate component), and `year` (YearTemplate component).

## Calendar Systems

`@internationalized/date` supports 13 calendar systems. Pass a `DateValue` created in any system via `toCalendar()`:

- Gregorian (default)
- Persian (`PersianCalendar`)
- Japanese (`JapaneseCalendar`)
- Buddhist, Chinese, Coptic, Ethiopian, Hebrew, Indian, Islamic (civil/tabular/umalqura), ROC

```ts
import { toCalendar, today, getLocalTimeZone } from "@internationalized/date"
import { PersianCalendar } from "@internationalized/date"

const persianDate = toCalendar(today(getLocalTimeZone()), new PersianCalendar())
```

## Range Calendar

For date range selection (start date + end date), use the separate `RangeCalendar` component — **not** the `Calendar` component with `type="range"`. `RangeCalendar` exposes the same layout/heading props and sub-components.

## Key Notes

- Requires `@internationalized/date` as a peer dependency alongside `reka-ui`
- The `yearRange` prop accepts a custom `DateValue[]` array; defaults to ±100 years from the current placeholder
- `numberOfMonths` (from `CalendarRootProps`) enables multi-month views
- All date values use `DateValue` from `@internationalized/date` — not native `Date` objects

## References

- [Installation](`CALENDAR-INSTALLATION.md`)
- [Source code](`CALENDAR-SOURCE.md`)
- [API / Props](`CALENDAR-API.md`)
- [Examples](`CALENDAR-EXAMPLES.md`)
