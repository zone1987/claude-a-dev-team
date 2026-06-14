---
name: shadcn-vue-range-calendar
description: >
  shadcn-vue RangeCalendar component (reka-ui RangeCalendarRoot,
  @internationalized/date, Tailwind v4 SFC Vue).
  Triggers: "shadcn-vue range calendar", "datumsbereich kalender vue",
  "range calendar vue", "date range picker vue", "reka-ui range calendar"
---

# shadcn-vue RangeCalendar

The RangeCalendar component presents a calendar view for selecting date ranges. It is built on top of reka-ui's `RangeCalendarRoot` primitive and uses `@internationalized/date` for all date handling. The component renders one or more grids of months, each with a header containing navigation buttons and a month/year heading, week-day header cells, and date cells that highlight the selected range from start to end.

## Architecture

The component is composed of 12 sub-components that are each individually exported and composable:

- **RangeCalendar** — root wrapper (`RangeCalendarRoot`), iterates over `grid` and `weekDays` from the slot scope
- **RangeCalendarHeader** — flex row containing heading and navigation buttons
- **RangeCalendarHeading** — renders the month/year label via slot `headingValue`
- **RangeCalendarPrevButton** / **RangeCalendarNextButton** — navigate between months using `RangeCalendarPrev` / `RangeCalendarNext` from reka-ui with Lucide chevron icons
- **RangeCalendarGrid** — wraps a single month grid (`<table>`)
- **RangeCalendarGridHead** — `<thead>` containing one `RangeCalendarGridRow` with `RangeCalendarHeadCell` entries
- **RangeCalendarGridBody** — `<tbody>` containing multiple `RangeCalendarGridRow` entries (one per week)
- **RangeCalendarGridRow** — single `<tr>` row
- **RangeCalendarHeadCell** — `<th>` with abbreviated weekday name
- **RangeCalendarCell** — `<td>` that applies accent background to selected ranges and rounds the corners at start and end boundaries
- **RangeCalendarCellTrigger** — `<button>` inside each cell; applies primary colours at selection-start and selection-end, muted styles for outside-view or disabled dates, and destructive styling for unavailable dates

## Date Handling

All date values use `@internationalized/date` types (`CalendarDate`, `CalendarDateTime`, `ZonedDateTime`, collectively typed as `DateValue` in reka-ui). A range is represented as `DateRange` from reka-ui: `{ start: DateValue; end: DateValue }`.

## Multi-Month Layout

Pass `:number-of-months="2"` (or more) to `RangeCalendar` to render side-by-side month grids. The layout switches from a vertical column on small screens to a horizontal row on `sm:` breakpoints.

## References

- Source code: `references/source.md`
- API documentation: `references/api.md`
- Usage examples: `references/examples.md`
- Installation: `references/installation.md`
