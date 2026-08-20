# Calendar — Examples

## Contents

- [1. Single Date Selection](#1-single-date-selection)
- [2. Multiple Date Selection](#2-multiple-date-selection)
- [3. Month and Year Dropdown Layout](#3-month-and-year-dropdown-layout)
- [4. Calendar with Preset Buttons](#4-calendar-with-preset-buttons)
- [5. Date Picker (Calendar inside Popover)](#5-date-picker-calendar-inside-popover)

## 1. Single Date Selection

Basic calendar with single date selection and a display of the chosen value.

```vue
<script setup lang="ts">
import { ref } from "vue"
import type { DateValue } from "@internationalized/date"
import { Calendar } from "@/components/ui/calendar"

const selected = ref<DateValue | undefined>(undefined)
</script>

<template>
  <div class="flex flex-col items-center gap-4">
    <Calendar v-model="selected" />
    <p class="text-sm text-muted-foreground">
      Selected: {{ selected ? selected.toString() : "None" }}
    </p>
  </div>
</template>
```

## 2. Multiple Date Selection

Allow selecting several independent dates simultaneously.

```vue
<script setup lang="ts">
import { ref } from "vue"
import type { DateValue } from "@internationalized/date"
import { Calendar } from "@/components/ui/calendar"

const selected = ref<DateValue[]>([])
</script>

<template>
  <div class="flex flex-col items-center gap-4">
    <Calendar
      v-model="selected"
      type="multiple"
    />
    <p class="text-sm text-muted-foreground">
      {{ selected.length }} date(s) selected
    </p>
  </div>
</template>
```

## 3. Month and Year Dropdown Layout

Use `layout="month-and-year"` to replace the static heading with native select dropdowns for month and year navigation.

```vue
<script setup lang="ts">
import { ref } from "vue"
import type { DateValue } from "@internationalized/date"
import { Calendar } from "@/components/ui/calendar"

const selected = ref<DateValue | undefined>(undefined)
</script>

<template>
  <Calendar
    v-model="selected"
    layout="month-and-year"
  />
</template>
```

You can also use `layout="month-only"` or `layout="year-only"` for a dropdown on just one part of the heading.

## 4. Calendar with Preset Buttons

Add quick-select preset buttons that programmatically set the calendar value.

```vue
<script setup lang="ts">
import { ref } from "vue"
import { type DateValue, today, getLocalTimeZone } from "@internationalized/date"
import { Calendar } from "@/components/ui/calendar"
import { Button } from "@/components/ui/button"

const tz = getLocalTimeZone()
const selected = ref<DateValue | undefined>(undefined)

const presets = [
  { label: "Today", value: () => today(tz) },
  { label: "Tomorrow", value: () => today(tz).add({ days: 1 }) },
  { label: "In 3 days", value: () => today(tz).add({ days: 3 }) },
  { label: "Next week", value: () => today(tz).add({ weeks: 1 }) },
  { label: "Next month", value: () => today(tz).add({ months: 1 }) },
]
</script>

<template>
  <div class="flex gap-4">
    <div class="flex flex-col gap-2">
      <p class="text-sm font-medium">Quick select</p>
      <Button
        v-for="preset in presets"
        :key="preset.label"
        variant="outline"
        size="sm"
        class="justify-start"
        @click="selected = preset.value()"
      >
        {{ preset.label }}
      </Button>
    </div>
    <Calendar v-model="selected" />
  </div>
</template>
```

## 5. Date Picker (Calendar inside Popover)

Combine `Calendar` with `Popover` for a compact date picker input field.

```vue
<script setup lang="ts">
import { ref, computed } from "vue"
import { type DateValue, today, getLocalTimeZone } from "@internationalized/date"
import { CalendarIcon } from "lucide-vue-next"
import { Calendar } from "@/components/ui/calendar"
import { Button } from "@/components/ui/button"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"
import { cn } from "@/lib/utils"

const selected = ref<DateValue | undefined>(undefined)

const displayValue = computed(() => {
  if (!selected.value) return "Pick a date"
  // Format using Intl.DateTimeFormat for display
  return new Intl.DateTimeFormat("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  }).format(selected.value.toDate(getLocalTimeZone()))
})
</script>

<template>
  <Popover>
    <PopoverTrigger as-child>
      <Button
        variant="outline"
        :class="cn(
          'w-[280px] justify-start text-left font-normal',
          !selected && 'text-muted-foreground'
        )"
      >
        <CalendarIcon class="mr-2 size-4" />
        {{ displayValue }}
      </Button>
    </PopoverTrigger>
    <PopoverContent class="w-auto p-0">
      <Calendar
        v-model="selected"
        layout="month-and-year"
        initial-focus
      />
    </PopoverContent>
  </Popover>
</template>
```

> **Note:** For date range selection (start + end date), use the separate `RangeCalendar` component instead of `Calendar`.
