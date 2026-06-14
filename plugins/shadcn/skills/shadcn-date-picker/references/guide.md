# Date Picker — Composition Guide

The Date Picker is not a single component but a composition of `Popover` and `Calendar`. There is no `DatePicker` root component.

## Composition

```text
Popover
├── PopoverTrigger
└── PopoverContent
    └── Calendar
```

## Basic Usage

```tsx
"use client"

import * as React from "react"
import { format } from "date-fns"
import { Calendar as CalendarIcon } from "lucide-react"

import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Calendar } from "@/components/ui/calendar"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"

export function DatePickerDemo() {
  const [date, setDate] = React.useState<Date>()

  return (
    <Popover>
      <PopoverTrigger asChild>
        <Button
          variant="outline"
          data-empty={!date}
          className="w-[280px] justify-start text-left font-normal data-[empty=true]:text-muted-foreground"
        >
          <CalendarIcon />
          {date ? format(date, "PPP") : <span>Pick a date</span>}
        </Button>
      </PopoverTrigger>
      <PopoverContent className="w-auto p-0">
        <Calendar mode="single" selected={date} onSelect={setDate} />
      </PopoverContent>
    </Popover>
  )
}
```

## Calendar Modes

- `mode="single"` — single date selection
- `mode="range"` — date range selection (returns `DateRange | undefined`)
- `mode="multiple"` — multiple individual dates

## Date Formatting

Uses `date-fns` format tokens:
- `format(date, "PPP")` → "June 14, 2026"
- `format(date, "LLL dd, y")` → "Jun 14, 2026"
- `format(date, "P")` → "06/14/2026"

---

_Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/date-picker.mdx`_
