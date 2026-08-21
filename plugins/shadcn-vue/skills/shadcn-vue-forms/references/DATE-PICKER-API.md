# Date Picker — API Reference

Reka-ui API: https://reka-ui.com/docs/components/date-picker#api-reference

The Date Picker is a composite of `<Popover />` and `<Calendar />`.
See their individual API docs for the full prop list.

---

## Contents

- [@internationalized/date types](#internationalizeddate-types)
- [Calendar Props (key props for date-picker usage)](#calendar-props-key-props-for-date-picker-usage)
- [RangeCalendar Props (additional)](#rangecalendar-props-additional)
- [Popover Props (used as wrapper)](#popover-props-used-as-wrapper)
- [Common patterns](#common-patterns)

## @internationalized/date types

### CalendarDate

Immutable date value without time zone.

```ts
import { CalendarDate } from '@internationalized/date'

const date = new CalendarDate(2024, 1, 15) // year, month (1-based), day
date.year   // number
date.month  // number (1-12)
date.day    // number (1-31)
```

### DateRange

```ts
import type { DateRange } from 'reka-ui'

interface DateRange {
  start: CalendarDate | undefined
  end: CalendarDate | undefined
}
```

### DateFormatter

```ts
import { DateFormatter, getLocalTimeZone } from '@internationalized/date'

const df = new DateFormatter('en-US', {
  dateStyle: 'long',
})
df.format(date.toDate(getLocalTimeZone())) // → "January 15, 2024"
```

### today + getLocalTimeZone

```ts
import { today, getLocalTimeZone } from '@internationalized/date'

const todayDate = today(getLocalTimeZone()) // CalendarDate for today
```

---

## Calendar Props (key props for date-picker usage)

| Prop                  | Type                     | Description                        |
| :-------------------- | :----------------------- | :--------------------------------- |
| `modelValue`          | `CalendarDate`           | Controlled selected date (v-model) |
| `defaultValue`        | `CalendarDate`           | Initial date (uncontrolled)        |
| `defaultPlaceholder`  | `CalendarDate`           | Initial focus date when empty      |
| `initialFocus`        | `boolean`                | Auto-focus on open                 |
| `layout`              | `"month" \| "month-and-year"` | Month-only vs month+year nav  |
| `minValue`            | `CalendarDate`           | Minimum selectable date            |
| `maxValue`            | `CalendarDate`           | Maximum selectable date            |
| `disabled`            | `boolean`                | Disable calendar                   |
| `readonly`            | `boolean`                | Read-only mode                     |
| `numberOfMonths`      | `number`                 | Number of months displayed         |

---

## RangeCalendar Props (additional)

| Prop          | Type        | Description                       |
| :------------ | :---------- | :-------------------------------- |
| `modelValue`  | `DateRange` | Controlled range (v-model)        |
| `numberOfMonths` | `number` | Typically 2 for range picker     |

---

## Popover Props (used as wrapper)

| Prop    | Type      | Default | Description              |
| :------ | :-------- | :------ | :----------------------- |
| `open`  | `boolean` | —       | Controlled open state    |
| `modal` | `boolean` | false   | Modal behavior           |

PopoverTrigger: use `as-child` to forward to Button.
PopoverContent: set `class="w-auto p-0"` for date-picker use.

---

## Common patterns

### Convert CalendarDate to JavaScript Date

```ts
const jsDate = new Date(date.value.year, date.value.month - 1, date.value.day)
```

### Convert with timezone (for DateFormatter)

```ts
import { getLocalTimeZone } from '@internationalized/date'

const jsDate = date.value.toDate(getLocalTimeZone())
```

### Format with toLocaleDateString

```ts
function formatDate(date?: CalendarDate): string {
  if (!date) return ""
  const jsDate = new Date(date.year, date.month - 1, date.day)
  return jsDate.toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  })
}
```

### Format range

```ts
function formatDateRange(range?: DateRange): string {
  if (!range?.start) return ""
  if (!range.end) return formatDate(range.start)
  return `${formatDate(range.start)} - ${formatDate(range.end)}`
}
```

### Conditional placeholder class (cn pattern)

```vue
<Button
  variant="outline"
  :class="cn(
    'w-[280px] justify-start text-left font-normal',
    !date && 'text-muted-foreground',
  )"
>
```
