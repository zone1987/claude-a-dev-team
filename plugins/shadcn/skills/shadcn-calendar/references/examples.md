# Calendar — Examples

## Demo (with dropdown caption)

```tsx
"use client"

import * as React from "react"
import { Calendar } from "@/registry/new-york-v4/ui/calendar"

export default function CalendarDemo() {
  const [date, setDate] = React.useState<Date | undefined>(new Date())

  return (
    <Calendar
      mode="single"
      selected={date}
      onSelect={setDate}
      className="rounded-md border shadow-sm"
      captionLayout="dropdown"
    />
  )
}
```

## Basic (label caption)

```tsx
"use client"

import * as React from "react"
import { Calendar } from "@/components/ui/calendar"

export default function CalendarBasic() {
  const [date, setDate] = React.useState<Date | undefined>(new Date())

  return (
    <Calendar
      mode="single"
      selected={date}
      onSelect={setDate}
      className="rounded-lg border"
    />
  )
}
```

## Range selection

```tsx
"use client"

import * as React from "react"
import type { DateRange } from "react-day-picker"
import { Calendar } from "@/components/ui/calendar"

export default function CalendarRange() {
  const [range, setRange] = React.useState<DateRange | undefined>()

  return (
    <Calendar
      mode="range"
      selected={range}
      onSelect={setRange}
      className="rounded-lg border"
    />
  )
}
```

## With timezone (SSR-safe)

```tsx
"use client"

import * as React from "react"
import { Calendar } from "@/components/ui/calendar"

export function CalendarWithTimezone() {
  const [date, setDate] = React.useState<Date | undefined>(undefined)
  const [timeZone, setTimeZone] = React.useState<string | undefined>(undefined)

  React.useEffect(() => {
    setTimeZone(Intl.DateTimeFormat().resolvedOptions().timeZone)
  }, [])

  return (
    <Calendar
      mode="single"
      selected={date}
      onSelect={setDate}
      timeZone={timeZone}
    />
  )
}
```

## Custom cell size (responsive)

```tsx
<Calendar
  mode="single"
  selected={date}
  onSelect={setDate}
  className="rounded-lg border [--cell-size:--spacing(11)] md:[--cell-size:--spacing(12)]"
/>
```

## Persian / Hijri calendar

Edit `calendar.tsx`:

```diff
- import { DayPicker } from "react-day-picker"
+ import { DayPicker } from "react-day-picker/persian"
```

## RTL with Arabic locale

```tsx
import { arSA } from "react-day-picker/locale"

<Calendar
  mode="single"
  selected={date}
  onSelect={setDate}
  locale={arSA}
  dir="rtl"
/>
```

---
Sources:
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/calendar-demo.tsx`
- `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/calendar-hijri.tsx`
