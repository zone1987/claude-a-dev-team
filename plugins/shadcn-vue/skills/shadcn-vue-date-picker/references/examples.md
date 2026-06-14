# Date Picker — Examples

Sources:
- `apps/v4/content/docs/components/date-picker.md`
- `apps/v4/registry/bases/reka/examples/calendar/DatePickerSimple.vue`
- `apps/v4/registry/bases/reka/examples/calendar/DatePickerWithRange.vue`
- `apps/v4/registry/bases/reka/examples/calendar/DatePickerWithDropdowns.vue`

---

## Simple Date Picker

`DatePickerSimple.vue` — Basic single-date picker using `CalendarDate`
with Popover + Calendar composition.

```vue
<script setup lang="ts">
import type { CalendarDate } from "@internationalized/date"
import { ref } from "vue"
import { Button } from "@/components/ui/button"
import { Calendar } from "@/components/ui/calendar"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"

const date = ref<CalendarDate>()

function formatDate(date?: CalendarDate): string {
  if (!date) return ""
  const jsDate = new Date(date.year, date.month - 1, date.day)
  return jsDate.toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  })
}
</script>

<template>
  <Popover>
    <PopoverTrigger as-child>
      <Button
        variant="outline"
        class="justify-start px-2.5 font-normal"
      >
        <span v-if="date">{{ formatDate(date) }}</span>
        <span v-else>Pick a date</span>
      </Button>
    </PopoverTrigger>
    <PopoverContent class="w-auto p-0" align="start">
      <Calendar v-model="date" />
    </PopoverContent>
  </Popover>
</template>
```

---

## Date Picker with Range

`DatePickerWithRange.vue` — Two-month range calendar using
`RangeCalendar` + `DateRange` + `CalendarDate`.

```vue
<script setup lang="ts">
import type { DateRange } from "reka-ui"
import { CalendarDate } from "@internationalized/date"
import { ref } from "vue"
import { Button } from "@/components/ui/button"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"
import { RangeCalendar } from "@/components/ui/range-calendar"

const date = ref({
  start: new CalendarDate(new Date().getFullYear(), 1, 20),
  end: new CalendarDate(new Date().getFullYear(), 2, 9),
} as DateRange)

function formatDate(date?: CalendarDate | unknown): string {
  if (!date) return ""
  const d = date as CalendarDate
  const jsDate = new Date(d.year, d.month - 1, d.day)
  return jsDate.toLocaleDateString("en-US", {
    year: "numeric",
    month: "short",
    day: "numeric",
  })
}

function formatDateRange(range?: DateRange): string {
  if (!range?.start) return ""
  if (!range.end) return formatDate(range.start)
  return `${formatDate(range.start)} - ${formatDate(range.end)}`
}
</script>

<template>
  <Popover>
    <PopoverTrigger as-child>
      <Button
        variant="outline"
        class="justify-start px-2.5 font-normal"
      >
        <span v-if="date?.start">
          {{ formatDateRange(date as any) }}
        </span>
        <span v-else>Pick a date</span>
      </Button>
    </PopoverTrigger>
    <PopoverContent class="w-auto p-0" align="start">
      <RangeCalendar
        v-model="(date as any)"
        :number-of-months="2"
      />
    </PopoverContent>
  </Popover>
</template>
```

---

## Date Picker with Dropdowns

`DatePickerWithDropdowns.vue` — Calendar with month+year dropdown
navigation and a "Done" close button. Uses `layout="month-and-year"`
and controlled `open` state.

```vue
<script setup lang="ts">
import type { CalendarDate } from "@internationalized/date"
import { ref } from "vue"
import { Button } from "@/components/ui/button"
import { Calendar } from "@/components/ui/calendar"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"

const date = ref<CalendarDate>()
const open = ref(false)

function formatDate(date?: CalendarDate): string {
  if (!date) return ""
  const jsDate = new Date(date.year, date.month - 1, date.day)
  return jsDate.toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  })
}
</script>

<template>
  <Popover v-model:open="open">
    <PopoverTrigger as-child>
      <Button
        variant="outline"
        class="justify-start px-2.5 font-normal"
      >
        <span v-if="date">{{ formatDate(date) }}</span>
        <span v-else>Pick a date</span>
      </Button>
    </PopoverTrigger>
    <PopoverContent class="w-auto p-0" align="start">
      <Calendar
        v-model="date"
        layout="month-and-year"
      />
      <div class="flex gap-2 border-t p-2">
        <Button
          variant="outline"
          size="sm"
          class="w-full"
          @click="open = false"
        >
          Done
        </Button>
      </div>
    </PopoverContent>
  </Popover>
</template>
```

---

## From Docs: Basic Pattern

From `apps/v4/content/docs/components/date-picker.md` —
uses `DateFormatter` and `getLocalTimeZone`.

```vue
<script setup lang="ts">
import { DateFormatter, getLocalTimeZone, today }
  from '@internationalized/date'
import { CalendarIcon } from '@lucide/vue'
import { ref } from 'vue'
import { Button } from '@/components/ui/button'
import { Calendar } from '@/components/ui/calendar'
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from '@/components/ui/popover'
import { cn } from '@/lib/utils'

const date = ref<Date>()
const defaultPlaceholder = today(getLocalTimeZone())
</script>

<template>
  <Popover>
    <PopoverTrigger as-child>
      <Button
        variant="outline"
        :class="cn(
          'w-[280px] justify-start text-left font-normal',
          !date && 'text-muted-foreground',
        )"
      >
        <CalendarIcon class="mr-2 h-4 w-4" />
        {{ date ? date.toDateString() : "Pick a date" }}
      </Button>
    </PopoverTrigger>
    <PopoverContent class="w-auto p-0">
      <Calendar
        v-model="date"
        :initial-focus="true"
        :default-placeholder="defaultPlaceholder"
        layout="month-and-year"
      />
    </PopoverContent>
  </Popover>
</template>
```
