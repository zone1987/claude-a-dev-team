# Calendar — API Reference

## Calendar

Extends all React DayPicker props.

| Prop | Type | Default | Notes |
|------|------|---------|-------|
| `mode` | `"single" \| "range" \| "multiple"` | — | Selection mode |
| `selected` | `Date \| DateRange \| Date[]` | — | Controlled selection |
| `onSelect` | function | — | Selection change handler |
| `showOutsideDays` | `boolean` | `true` | Show adjacent month days |
| `captionLayout` | `"label" \| "dropdown"` | `"label"` | Month/year nav style |
| `buttonVariant` | Button variant | `"ghost"` | Nav button style |
| `locale` | `Partial<Locale>` | — | react-day-picker locale |
| `timeZone` | `string` | — | Prevent date offset on SSR |
| `formatters` | object | — | Custom formatters |
| `components` | object | — | Custom sub-components |
| `showWeekNumber` | `boolean` | `false` | Show ISO week numbers |

## CSS Custom Properties

| Variable | Default | Description |
|----------|---------|-------------|
| `--cell-size` | `--spacing(8)` = 32px | Day cell size |

```tsx
// Responsive cell size
<Calendar className="[--cell-size:--spacing(11)] md:[--cell-size:--spacing(12)]" />

// Fixed value
<Calendar className="[--cell-size:2.75rem]" />
```

## CalendarDayButton

Internal component. Can be overridden via `components={{ DayButton: MyDayButton }}`.

| Prop | Type | Notes |
|------|------|-------|
| `day` | `Day` | react-day-picker Day object |
| `modifiers` | `DayModifiers` | selected, range_start, range_end, etc. |
| `locale` (Base) | `Partial<Locale>` | For locale-aware date strings |

## Timezone usage

```tsx
"use client"
import * as React from "react"

function CalendarWithTimezone() {
  const [date, setDate] = React.useState<Date | undefined>()
  const [timeZone, setTimeZone] = React.useState<string | undefined>()

  React.useEffect(() => {
    setTimeZone(Intl.DateTimeFormat().resolvedOptions().timeZone)
  }, [])

  return (
    <Calendar mode="single" selected={date} onSelect={setDate} timeZone={timeZone} />
  )
}
```

## Persian / Hijri

```diff
- import { DayPicker } from "react-day-picker"
+ import { DayPicker } from "react-day-picker/persian"
```

## External docs

- React DayPicker: https://react-day-picker.js.org

---
Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/calendar.mdx`
