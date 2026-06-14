# Calendar — Source Code

## index.ts

```ts
export { default as Calendar } from "./Calendar.vue"
export { default as CalendarCell } from "./CalendarCell.vue"
export { default as CalendarCellTrigger } from "./CalendarCellTrigger.vue"
export { default as CalendarGrid } from "./CalendarGrid.vue"
export { default as CalendarGridBody } from "./CalendarGridBody.vue"
export { default as CalendarGridHead } from "./CalendarGridHead.vue"
export { default as CalendarGridRow } from "./CalendarGridRow.vue"
export { default as CalendarHeadCell } from "./CalendarHeadCell.vue"
export { default as CalendarHeader } from "./CalendarHeader.vue"
export { default as CalendarHeading } from "./CalendarHeading.vue"
export { default as CalendarNextButton } from "./CalendarNextButton.vue"
export { default as CalendarPrevButton } from "./CalendarPrevButton.vue"

export type LayoutTypes = "month-and-year" | "month-only" | "year-only" | undefined
```

## Calendar.vue (complete)

```vue
<script lang="ts" setup>
import type { CalendarRootEmits, CalendarRootProps, DateValue } from "reka-ui"
import type { HTMLAttributes, Ref } from "vue"
import type { LayoutTypes } from "."
import { getLocalTimeZone, today } from "@internationalized/date"
import { createReusableTemplate, reactiveOmit, useVModel } from "@vueuse/core"
import { CalendarRoot, useDateFormatter, useForwardPropsEmits } from "reka-ui"
import { createYear, createYearRange, toDate } from "reka-ui/date"
import { computed, toRaw } from "vue"
import { cn } from "@/lib/utils"
import { NativeSelect, NativeSelectOption } from "@/registry/new-york-v4/ui/native-select"
import { CalendarCell, CalendarCellTrigger, CalendarGrid, CalendarGridBody, CalendarGridHead, CalendarGridRow, CalendarHeadCell, CalendarHeader, CalendarHeading, CalendarNextButton, CalendarPrevButton } from "."

const props = withDefaults(defineProps<CalendarRootProps & { class?: HTMLAttributes["class"], layout?: LayoutTypes, yearRange?: DateValue[] }>(), {
  modelValue: undefined,
  layout: undefined,
})
const emits = defineEmits<CalendarRootEmits>()

const delegatedProps = reactiveOmit(props, "class", "layout", "placeholder")

const placeholder = useVModel(props, "placeholder", emits, {
  passive: true,
  defaultValue: props.defaultPlaceholder ?? today(getLocalTimeZone()),
}) as Ref<DateValue>

const formatter = useDateFormatter(props.locale ?? "en")

const yearRange = computed(() => {
  return props.yearRange ?? createYearRange({
    start: props?.minValue ?? (toRaw(props.placeholder) ?? props.defaultPlaceholder ?? today(getLocalTimeZone()))
      .cycle("year", -100),
    end: props?.maxValue ?? (toRaw(props.placeholder) ?? props.defaultPlaceholder ?? today(getLocalTimeZone()))
      .cycle("year", 10),
  })
})

const [DefineMonthTemplate, ReuseMonthTemplate] = createReusableTemplate<{ date: DateValue }>()
const [DefineYearTemplate, ReuseYearTemplate] = createReusableTemplate<{ date: DateValue }>()

const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <DefineMonthTemplate v-slot="{ date }">
    <div class="**:data-[slot=native-select-icon]:right-1">
      <div class="relative">
        <div class="absolute inset-0 flex h-full items-center text-sm pl-2 pointer-events-none">
          {{ formatter.custom(toDate(date), { month: 'short' }) }}
        </div>
        <NativeSelect
          class="text-xs h-8 pr-6 pl-2 text-transparent relative"
          :model-value="date.month"
          @change="(e: Event) => {
            placeholder = placeholder.set({
              month: Number((e?.target as any)?.value),
            })
          }"
        >
          <NativeSelectOption v-for="(month) in createYear({ dateObj: date })" :key="month.toString()" :value="month.month" :selected="date.month === month.month">
            {{ formatter.custom(toDate(month), { month: 'short' }) }}
          </NativeSelectOption>
        </NativeSelect>
      </div>
    </div>
  </DefineMonthTemplate>

  <DefineYearTemplate v-slot="{ date }">
    <div class="**:data-[slot=native-select-icon]:right-1">
      <div class="relative">
        <div class="absolute inset-0 flex h-full items-center text-sm pl-2 pointer-events-none">
          {{ formatter.custom(toDate(date), { year: 'numeric' }) }}
        </div>
        <NativeSelect
          class="text-xs h-8 pr-6 pl-2 text-transparent relative"
          :model-value="date.year"
          @change="(e: Event) => {
            placeholder = placeholder.set({
              year: Number((e?.target as any)?.value),
            })
          }"
        >
          <NativeSelectOption v-for="(year) in yearRange" :key="year.toString()" :value="year.year" :selected="date.year === year.year">
            {{ formatter.custom(toDate(year), { year: 'numeric' }) }}
          </NativeSelectOption>
        </NativeSelect>
      </div>
    </div>
  </DefineYearTemplate>

  <CalendarRoot
    v-slot="{ grid, weekDays, date }"
    v-bind="forwarded"
    v-model:placeholder="placeholder"
    data-slot="calendar"
    :class="cn('p-3', props.class)"
  >
    <CalendarHeader class="pt-0">
      <nav class="flex items-center gap-1 absolute top-0 inset-x-0 justify-between">
        <CalendarPrevButton>
          <slot name="calendar-prev-icon" />
        </CalendarPrevButton>
        <CalendarNextButton>
          <slot name="calendar-next-icon" />
        </CalendarNextButton>
      </nav>

      <slot name="calendar-heading" :date="date" :month="ReuseMonthTemplate" :year="ReuseYearTemplate">
        <template v-if="layout === 'month-and-year'">
          <div class="flex items-center justify-center gap-1">
            <ReuseMonthTemplate :date="date" />
            <ReuseYearTemplate :date="date" />
          </div>
        </template>
        <template v-else-if="layout === 'month-only'">
          <div class="flex items-center justify-center gap-1">
            <ReuseMonthTemplate :date="date" />
            {{ formatter.custom(toDate(date), { year: 'numeric' }) }}
          </div>
        </template>
        <template v-else-if="layout === 'year-only'">
          <div class="flex items-center justify-center gap-1">
            {{ formatter.custom(toDate(date), { month: 'short' }) }}
            <ReuseYearTemplate :date="date" />
          </div>
        </template>
        <template v-else>
          <CalendarHeading />
        </template>
      </slot>
    </CalendarHeader>

    <div class="flex flex-col gap-y-4 mt-4 sm:flex-row sm:gap-x-4 sm:gap-y-0">
      <CalendarGrid v-for="month in grid" :key="month.value.toString()">
        <CalendarGridHead>
          <CalendarGridRow>
            <CalendarHeadCell v-for="day in weekDays" :key="day">{{ day }}</CalendarHeadCell>
          </CalendarGridRow>
        </CalendarGridHead>
        <CalendarGridBody>
          <CalendarGridRow v-for="(weekDates, index) in month.rows" :key="`weekDate-${index}`" class="mt-2 w-full">
            <CalendarCell v-for="weekDate in weekDates" :key="weekDate.toString()" :date="weekDate">
              <CalendarCellTrigger :day="weekDate" :month="month.value" />
            </CalendarCell>
          </CalendarGridRow>
        </CalendarGridBody>
      </CalendarGrid>
    </div>
  </CalendarRoot>
</template>
```

## Sub-components (abbreviated)

### CalendarCell.vue

Wraps `CalendarCell` from `reka-ui`. Key classes:
```
relative p-0 text-center focus-within:relative focus-within:z-20 flex-1
[&:has([data-selected])]:rounded-md [&:has([data-selected])]:bg-accent
```
Renders `data-slot="calendar-cell"`.

### CalendarCellTrigger.vue

Wraps `CalendarCellTrigger` from `reka-ui`. Uses `buttonVariants({ variant: 'ghost' })` as base, then overrides for states:
- `data-selected` → `bg-primary text-primary-foreground hover:bg-primary`
- `data-today` → `bg-accent text-accent-foreground`
- `data-disabled` → `text-muted-foreground opacity-50`
- `data-unavailable` → `text-destructive-foreground line-through`
- `data-outside-view` → `text-muted-foreground opacity-50 hidden`

Size: `size-8 p-0`. Renders `data-slot="calendar-cell-trigger"`.

### CalendarGrid.vue

Wraps `CalendarGrid` from `reka-ui`. Classes: `w-full border-collapse space-y-1`. Renders `data-slot="calendar-grid"`.

### CalendarGridBody.vue

Wraps `CalendarGridBody` from `reka-ui`. No extra classes. Renders `data-slot="calendar-grid-body"`.

### CalendarGridHead.vue

Wraps `CalendarGridHead` from `reka-ui`. No extra classes. Renders `data-slot="calendar-grid-head"`.

### CalendarGridRow.vue

Wraps `CalendarGridRow` from `reka-ui`. Classes: `flex w-full mt-2`. Renders `data-slot="calendar-grid-row"`.

### CalendarHeadCell.vue

Wraps `CalendarHeadCell` from `reka-ui`. Classes: `text-muted-foreground rounded-md w-8 font-normal text-[0.8rem] flex-1`. Renders `data-slot="calendar-head-cell"`.

### CalendarHeader.vue

Wraps `CalendarHeader` from `reka-ui`. Classes: `flex justify-center pt-1 relative items-center w-full px-8`. Renders `data-slot="calendar-header"`.

### CalendarHeading.vue

Wraps `CalendarHeading` from `reka-ui`. Exposes default slot with `headingValue`. Classes: `text-sm font-medium`. Renders `data-slot="calendar-heading"`.

### CalendarNextButton.vue

Wraps `CalendarNext` from `reka-ui`. Uses `buttonVariants({ variant: 'outline' })` + `size-7 bg-transparent p-0 opacity-50 hover:opacity-100 absolute right-1`. Contains a `<ChevronRight class="size-4" />` icon (from `lucide-vue-next`) as default content, overrideable via default slot. Renders `data-slot="calendar-next-button"`.

### CalendarPrevButton.vue

Wraps `CalendarPrev` from `reka-ui`. Same as `CalendarNextButton` but positioned `left-1` and uses `<ChevronLeft class="size-4" />`. Renders `data-slot="calendar-prev-button"`.
