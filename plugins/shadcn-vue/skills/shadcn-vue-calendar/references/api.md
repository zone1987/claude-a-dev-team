# Calendar — API Reference

## Calendar Props

The `Calendar` component extends `CalendarRootProps` from `reka-ui` and adds the following:

| Prop | Type | Default | Description |
|---|---|---|---|
| `layout` | `LayoutTypes` | `undefined` | Heading layout: `"month-and-year"`, `"month-only"`, `"year-only"`, or `undefined` (plain text) |
| `yearRange` | `DateValue[]` | computed ±100yr | Custom array of year `DateValue` objects for the year dropdown |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes applied to the root `<CalendarRoot>` |

## CalendarRoot Props (from reka-ui)

| Prop | Type | Default | Description |
|---|---|---|---|
| `modelValue` | `DateValue \| DateValue[] \| undefined` | `undefined` | The selected date(s); use `v-model` for two-way binding |
| `type` | `"single" \| "multiple"` | `"single"` | Selection mode — single date or multiple independent dates |
| `defaultValue` | `DateValue \| DateValue[] \| undefined` | `undefined` | Uncontrolled initial selected value |
| `placeholder` | `DateValue` | today | The date the calendar is currently "viewing"; use `v-model:placeholder` |
| `defaultPlaceholder` | `DateValue` | today | Uncontrolled initial placeholder date |
| `locale` | `string` | `"en"` | BCP 47 locale string for formatting (e.g. `"de"`, `"ar-SA"`) |
| `numberOfMonths` | `number` | `1` | Number of months to display side-by-side |
| `weekStartsOn` | `0 \| 1 \| 2 \| 3 \| 4 \| 5 \| 6` | `0` | First day of week (0 = Sunday, 1 = Monday, …) |
| `fixedWeeks` | `boolean` | `false` | Always render 6 weeks per month for a stable grid height |
| `isDateDisabled` | `(date: DateValue) => boolean` | — | Callback to mark specific dates as disabled |
| `isDateUnavailable` | `(date: DateValue) => boolean` | — | Callback to mark specific dates as unavailable (shown with strikethrough) |
| `minValue` | `DateValue` | — | Minimum selectable date |
| `maxValue` | `DateValue` | — | Maximum selectable date |
| `dir` | `"ltr" \| "rtl"` | `"ltr"` | Text direction |
| `pagedNavigation` | `boolean` | `false` | When `numberOfMonths > 1`, navigate by the full number of shown months |
| `preventDeselect` | `boolean` | `false` | Prevent deselecting an already-selected date |
| `initialFocus` | `boolean` | `false` | Move focus to the calendar on mount |
| `disabled` | `boolean` | `false` | Disable the entire calendar |
| `readonly` | `boolean` | `false` | Make the calendar read-only |

## CalendarRoot Emits (from reka-ui)

| Event | Payload | Description |
|---|---|---|
| `update:modelValue` | `DateValue \| DateValue[] \| undefined` | Fires when the selected value changes |
| `update:placeholder` | `DateValue` | Fires when the viewing placeholder changes |

## Named Slots

| Slot | Slot Props | Description |
|---|---|---|
| `calendar-heading` | `{ date: DateValue, month: Component, year: Component }` | Fully replaces the heading content. `month` and `year` are reusable template components that render the respective dropdowns |
| `calendar-prev-icon` | — | Replaces the default `<ChevronLeft>` icon inside `CalendarPrevButton` |
| `calendar-next-icon` | — | Replaces the default `<ChevronRight>` icon inside `CalendarNextButton` |

## LayoutTypes

```ts
export type LayoutTypes = "month-and-year" | "month-only" | "year-only" | undefined
```

## Calendar Systems

Supported via `@internationalized/date`. Import the calendar class and use `toCalendar()`:

| System | Import |
|---|---|
| Gregorian | Default, no import needed |
| Persian | `import { PersianCalendar } from "@internationalized/date"` |
| Japanese | `import { JapaneseCalendar } from "@internationalized/date"` |
| Buddhist | `import { BuddhistCalendar } from "@internationalized/date"` |
| Chinese | `import { ChineseCalendar } from "@internationalized/date"` |
| Coptic | `import { CopticCalendar } from "@internationalized/date"` |
| Ethiopian | `import { EthiopianCalendar } from "@internationalized/date"` |
| Hebrew | `import { HebrewCalendar } from "@internationalized/date"` |
| Indian | `import { IndianCalendar } from "@internationalized/date"` |
| Islamic (civil) | `import { IslamicCivilCalendar } from "@internationalized/date"` |
| Islamic (tabular) | `import { IslamicTabularCalendar } from "@internationalized/date"` |
| Islamic (Umm al-Qura) | `import { IslamicUmalquraCalendar } from "@internationalized/date"` |
| ROC | `import { ROCCalendar } from "@internationalized/date"` |

Usage:
```ts
import { toCalendar, today, getLocalTimeZone } from "@internationalized/date"
import { PersianCalendar } from "@internationalized/date"

const value = toCalendar(today(getLocalTimeZone()), new PersianCalendar())
```

## CalendarCell Sub-component Props

Each sub-component wraps the corresponding `reka-ui` primitive and passes all props through. Key props:

| Component | Key Props |
|---|---|
| `CalendarCell` | `date: DateValue` (required) |
| `CalendarCellTrigger` | `day: DateValue`, `month: DateValue` (both required) |
| `CalendarHeading` | exposes `headingValue` in default slot |
| `CalendarNextButton` / `CalendarPrevButton` | standard button attributes |
