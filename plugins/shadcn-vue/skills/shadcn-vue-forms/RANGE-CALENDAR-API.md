# API Reference

Full reka-ui API reference: https://reka-ui.com/docs/components/range-calendar#api-reference

---

## Contents

- [RangeCalendar (root)](#rangecalendar-root)
- [RangeCalendarCell](#rangecalendarcell)
- [RangeCalendarCellTrigger](#rangecalendarcelltrigger)
- [RangeCalendarGrid](#rangecalendargrid)
- [RangeCalendarGridBody](#rangecalendargridbody)
- [RangeCalendarGridHead](#rangecalendargridhead)
- [RangeCalendarGridRow](#rangecalendargridrow)
- [RangeCalendarHeadCell](#rangecalendarheadcell)
- [RangeCalendarHeader](#rangecalendarheader)
- [RangeCalendarHeading](#rangecalendarheading)
- [RangeCalendarNextButton](#rangecalendarnextbutton)
- [RangeCalendarPrevButton](#rangecalendarprevbutton)

## RangeCalendar (root)

Extends all `RangeCalendarRootProps` from reka-ui plus an optional `class` prop.

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `modelValue` / `v-model` | `DateRange` | — | The selected date range. `DateRange` is `{ start: DateValue; end: DateValue }`. |
| `defaultValue` | `DateRange` | — | Uncontrolled default range. |
| `numberOfMonths` | `number` | `1` | Number of month grids to display side by side. |
| `locale` | `string` | `"en"` | BCP 47 locale string used for formatting weekday and month names. |
| `disabled` | `boolean` | `false` | Disables all interaction. |
| `readonly` | `boolean` | `false` | Prevents selection changes. |
| `minValue` | `DateValue` | — | Minimum selectable date. Dates before this are rendered as unavailable. |
| `maxValue` | `DateValue` | — | Maximum selectable date. Dates after this are rendered as unavailable. |
| `isDateUnavailable` | `(date: DateValue) => boolean` | — | Callback to mark individual dates as unavailable. |
| `weekStartsOn` | `0 \| 1 \| 2 \| 3 \| 4 \| 5 \| 6` | `0` | Day the week starts on (0 = Sunday). |
| `fixedWeeks` | `boolean` | `false` | Always render 6 weeks per month. |
| `calendarLabel` | `string` | — | Accessible label for the calendar. |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes on the root element. |

**Emits**

| Event | Payload | Description |
|-------|---------|-------------|
| `update:modelValue` | `DateRange` | Fired when the selected range changes. |

---

## RangeCalendarCell

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `date` | `DateValue` | required | The date this cell represents. |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. |

The cell applies `bg-accent` to cells within the selected range and rounds corners at the selection start and end using CSS `:has()` selectors.

---

## RangeCalendarCellTrigger

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `day` | `DateValue` | required | The date value for this button. |
| `month` | `DateValue` | required | The currently displayed month. Used to determine outside-view dates. |
| `as` | `string` | `"button"` | The element or component to render as. |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. |

**Data attributes set by reka-ui**

| Attribute | Description |
|-----------|-------------|
| `data-selected` | Present when the date is within the selected range. |
| `data-selection-start` | Present on the range start date. |
| `data-selection-end` | Present on the range end date. |
| `data-today` | Present when the date is today. |
| `data-outside-view` | Present when the date belongs to an adjacent month. |
| `data-disabled` | Present when the date is disabled. |
| `data-unavailable` | Present when `isDateUnavailable` returns `true`. |

---

## RangeCalendarGrid

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. Defaults include `w-full border-collapse space-x-1`. |

Renders a `<table>` element. Receives its month data from the parent `RangeCalendar` slot scope via iteration.

---

## RangeCalendarGridBody

Wraps `<tbody>`. Accepts `RangeCalendarGridBodyProps` from reka-ui (no additional props).

---

## RangeCalendarGridHead

Wraps `<thead>`. Accepts `RangeCalendarGridHeadProps` from reka-ui (no additional props).

---

## RangeCalendarGridRow

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. Defaults to `flex`. |

Renders a `<tr>` element.

---

## RangeCalendarHeadCell

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. Defaults include `w-8 rounded-md text-[0.8rem] font-normal text-muted-foreground`. |

Renders a `<th>` containing the abbreviated weekday name.

---

## RangeCalendarHeader

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. Defaults include `flex justify-center pt-1 relative items-center w-full`. |

---

## RangeCalendarHeading

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. Defaults to `text-sm font-medium`. |

**Slots**

| Slot | Props | Description |
|------|-------|-------------|
| `default` | `{ headingValue: string }` | Custom rendering of the month/year label. |

---

## RangeCalendarNextButton

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. |

Navigates to the next month (or set of months when `numberOfMonths > 1`). Renders a `ChevronRight` icon by default; override via the default slot.

---

## RangeCalendarPrevButton

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes. |

Navigates to the previous month. Renders a `ChevronLeft` icon by default; override via the default slot.
