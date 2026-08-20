# Source

## Contents

- [RangeCalendar.vue](#rangecalendarvue)
- [RangeCalendarCell.vue](#rangecalendarcellvue)
- [RangeCalendarCellTrigger.vue](#rangecalendarcelltriggervue)
- [RangeCalendarGrid.vue](#rangecalendargridvue)
- [RangeCalendarGridBody.vue](#rangecalendargridbodyvue)
- [RangeCalendarGridHead.vue](#rangecalendargridheadvue)
- [RangeCalendarGridRow.vue](#rangecalendargridrowvue)
- [RangeCalendarHeadCell.vue](#rangecalendarheadcellvue)
- [RangeCalendarHeader.vue](#rangecalendarheadervue)
- [RangeCalendarHeading.vue](#rangecalendarheadingvue)
- [RangeCalendarNextButton.vue](#rangecalendarnextbuttonvue)
- [RangeCalendarPrevButton.vue](#rangecalendarprevbuttonvue)
- [index.ts](#indexts)

## RangeCalendar.vue

```vue
<script lang="ts" setup>
import type { RangeCalendarRootEmits, RangeCalendarRootProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { RangeCalendarRoot, useForwardPropsEmits } from "reka-ui"
import { cn } from "@/lib/utils"
import { RangeCalendarCell, RangeCalendarCellTrigger, RangeCalendarGrid, RangeCalendarGridBody, RangeCalendarGridHead, RangeCalendarGridRow, RangeCalendarHeadCell, RangeCalendarHeader, RangeCalendarHeading, RangeCalendarNextButton, RangeCalendarPrevButton } from "."

const props = defineProps<RangeCalendarRootProps & { class?: HTMLAttributes["class"] }>()

const emits = defineEmits<RangeCalendarRootEmits>()

const delegatedProps = reactiveOmit(props, "class")

const forwarded = useForwardPropsEmits(delegatedProps, emits)
</script>

<template>
  <RangeCalendarRoot
    v-slot="{ grid, weekDays }"
    data-slot="range-calendar"
    :class="cn('p-3', props.class)"
    v-bind="forwarded"
  >
    <RangeCalendarHeader>
      <RangeCalendarHeading />

      <div class="flex items-center gap-1">
        <RangeCalendarPrevButton />
        <RangeCalendarNextButton />
      </div>
    </RangeCalendarHeader>

    <div class="flex flex-col gap-y-4 mt-4 sm:flex-row sm:gap-x-4 sm:gap-y-0">
      <RangeCalendarGrid v-for="month in grid" :key="month.value.toString()">
        <RangeCalendarGridHead>
          <RangeCalendarGridRow>
            <RangeCalendarHeadCell
              v-for="day in weekDays" :key="day"
            >
              {{ day }}
            </RangeCalendarHeadCell>
          </RangeCalendarGridRow>
        </RangeCalendarGridHead>
        <RangeCalendarGridBody>
          <RangeCalendarGridRow v-for="(weekDates, index) in month.rows" :key="`weekDate-${index}`" class="mt-2 w-full">
            <RangeCalendarCell
              v-for="weekDate in weekDates"
              :key="weekDate.toString()"
              :date="weekDate"
            >
              <RangeCalendarCellTrigger
                :day="weekDate"
                :month="month.value"
              />
            </RangeCalendarCell>
          </RangeCalendarGridRow>
        </RangeCalendarGridBody>
      </RangeCalendarGrid>
    </div>
  </RangeCalendarRoot>
</template>
```

## RangeCalendarCell.vue

```vue
<script lang="ts" setup>
import type { RangeCalendarCellProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { RangeCalendarCell, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<RangeCalendarCellProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <RangeCalendarCell
    data-slot="range-calendar-cell"
    :class="cn('relative p-0 text-center text-sm focus-within:relative focus-within:z-20 [&:has([data-selected])]:bg-accent first:[&:has([data-selected])]:rounded-l-md last:[&:has([data-selected])]:rounded-r-md [&:has([data-selected][data-selection-end])]:rounded-r-md [&:has([data-selected][data-selection-start])]:rounded-l-md', props.class)"
    v-bind="forwardedProps"
  >
    <slot />
  </RangeCalendarCell>
</template>
```

## RangeCalendarCellTrigger.vue

```vue
<script lang="ts" setup>
import type { RangeCalendarCellTriggerProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { RangeCalendarCellTrigger, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"
import { buttonVariants } from "@/registry/new-york-v4/ui/button"

const props = withDefaults(defineProps<RangeCalendarCellTriggerProps & { class?: HTMLAttributes["class"] }>(), {
  as: "button",
})

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <RangeCalendarCellTrigger
    data-slot="range-calendar-trigger"
    :class="cn(
      buttonVariants({ variant: 'ghost' }),
      'h-8 w-8 p-0 font-normal data-[selected]:opacity-100',
      '[&[data-today]:not([data-selected])]:bg-accent [&[data-today]:not([data-selected])]:text-accent-foreground',
      // Selection Start
      'data-[selection-start]:bg-primary data-[selection-start]:text-primary-foreground [&[data-selection-start]:hover]:bg-primary data-[selection-start]:hover:text-primary-foreground data-[selection-start]:focus:bg-primary data-[selection-start]:focus:text-primary-foreground',
      // Selection End
      'data-[selection-end]:bg-primary data-[selection-end]:text-primary-foreground [&[data-selection-end]:hover]:bg-primary data-[selection-end]:hover:text-primary-foreground data-[selection-end]:focus:bg-primary data-[selection-end]:focus:text-primary-foreground',
      // Outside months
      'data-[outside-view]:text-muted-foreground',
      // Disabled
      'data-[disabled]:text-muted-foreground data-[disabled]:opacity-50',
      // Unavailable
      'data-[unavailable]:text-destructive-foreground data-[unavailable]:line-through',
      props.class,
    )"
    v-bind="forwardedProps"
  >
    <slot />
  </RangeCalendarCellTrigger>
</template>
```

## RangeCalendarGrid.vue

```vue
<script lang="ts" setup>
import type { RangeCalendarGridProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { RangeCalendarGrid, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<RangeCalendarGridProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <RangeCalendarGrid
    data-slot="range-calendar-grid"
    :class="cn('w-full border-collapse space-x-1', props.class)"
    v-bind="forwardedProps"
  >
    <slot />
  </RangeCalendarGrid>
</template>
```

## RangeCalendarGridBody.vue

```vue
<script lang="ts" setup>
import type { RangeCalendarGridBodyProps } from "reka-ui"
import { RangeCalendarGridBody } from "reka-ui"

const props = defineProps<RangeCalendarGridBodyProps>()
</script>

<template>
  <RangeCalendarGridBody
    data-slot="range-calendar-grid-body"
    v-bind="props"
  >
    <slot />
  </RangeCalendarGridBody>
</template>
```

## RangeCalendarGridHead.vue

```vue
<script lang="ts" setup>
import type { RangeCalendarGridHeadProps } from "reka-ui"
import { RangeCalendarGridHead } from "reka-ui"

const props = defineProps<RangeCalendarGridHeadProps>()
</script>

<template>
  <RangeCalendarGridHead
    data-slot="range-calendar-grid-head"
    v-bind="props"
  >
    <slot />
  </RangeCalendarGridHead>
</template>
```

## RangeCalendarGridRow.vue

```vue
<script lang="ts" setup>
import type { RangeCalendarGridRowProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { RangeCalendarGridRow, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<RangeCalendarGridRowProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <RangeCalendarGridRow
    data-slot="range-calendar-grid-row"
    :class="cn('flex', props.class)" v-bind="forwardedProps"
  >
    <slot />
  </RangeCalendarGridRow>
</template>
```

## RangeCalendarHeadCell.vue

```vue
<script lang="ts" setup>
import type { RangeCalendarHeadCellProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { RangeCalendarHeadCell, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<RangeCalendarHeadCellProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <RangeCalendarHeadCell
    data-slot="range-calendar-head-cell"
    :class="cn('w-8 rounded-md text-[0.8rem] font-normal text-muted-foreground', props.class)"
    v-bind="forwardedProps"
  >
    <slot />
  </RangeCalendarHeadCell>
</template>
```

## RangeCalendarHeader.vue

```vue
<script lang="ts" setup>
import type { RangeCalendarHeaderProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { RangeCalendarHeader, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<RangeCalendarHeaderProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <RangeCalendarHeader
    data-slot="range-calendar-header"
    :class="cn('flex justify-center pt-1 relative items-center w-full', props.class)"
    v-bind="forwardedProps"
  >
    <slot />
  </RangeCalendarHeader>
</template>
```

## RangeCalendarHeading.vue

```vue
<script lang="ts" setup>
import type { RangeCalendarHeadingProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { reactiveOmit } from "@vueuse/core"
import { RangeCalendarHeading, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"

const props = defineProps<RangeCalendarHeadingProps & { class?: HTMLAttributes["class"] }>()

defineSlots<{
  default: (props: { headingValue: string }) => any
}>()

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <RangeCalendarHeading
    v-slot="{ headingValue }"
    data-slot="range-calendar-heading"
    :class="cn('text-sm font-medium', props.class)"
    v-bind="forwardedProps"
  >
    <slot :heading-value>
      {{ headingValue }}
    </slot>
  </RangeCalendarHeading>
</template>
```

## RangeCalendarNextButton.vue

```vue
<script lang="ts" setup>
import type { RangeCalendarNextProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { ChevronRight } from "@lucide/vue"
import { reactiveOmit } from "@vueuse/core"
import { RangeCalendarNext, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"
import { buttonVariants } from "@/registry/new-york-v4/ui/button"

const props = defineProps<RangeCalendarNextProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <RangeCalendarNext
    data-slot="range-calendar-next-button"
    :class="cn(
      buttonVariants({ variant: 'outline' }),
      'absolute right-1',
      'size-7 bg-transparent p-0 opacity-50 hover:opacity-100',
      props.class,
    )"
    v-bind="forwardedProps"
  >
    <slot>
      <ChevronRight class="size-4" />
    </slot>
  </RangeCalendarNext>
</template>
```

## RangeCalendarPrevButton.vue

```vue
<script lang="ts" setup>
import type { RangeCalendarPrevProps } from "reka-ui"
import type { HTMLAttributes } from "vue"
import { ChevronLeft } from "@lucide/vue"
import { reactiveOmit } from "@vueuse/core"
import { RangeCalendarPrev, useForwardProps } from "reka-ui"
import { cn } from "@/lib/utils"
import { buttonVariants } from "@/registry/new-york-v4/ui/button"

const props = defineProps<RangeCalendarPrevProps & { class?: HTMLAttributes["class"] }>()

const delegatedProps = reactiveOmit(props, "class")

const forwardedProps = useForwardProps(delegatedProps)
</script>

<template>
  <RangeCalendarPrev
    data-slot="range-calendar-prev-button"
    :class="cn(
      buttonVariants({ variant: 'outline' }),
      'absolute left-1',
      'size-7 bg-transparent p-0 opacity-50 hover:opacity-100',
      props.class,
    )"
    v-bind="forwardedProps"
  >
    <slot>
      <ChevronLeft class="size-4" />
    </slot>
  </RangeCalendarPrev>
</template>
```

## index.ts

```ts
export { default as RangeCalendar } from "./RangeCalendar.vue"
export { default as RangeCalendarCell } from "./RangeCalendarCell.vue"
export { default as RangeCalendarCellTrigger } from "./RangeCalendarCellTrigger.vue"
export { default as RangeCalendarGrid } from "./RangeCalendarGrid.vue"
export { default as RangeCalendarGridBody } from "./RangeCalendarGridBody.vue"
export { default as RangeCalendarGridHead } from "./RangeCalendarGridHead.vue"
export { default as RangeCalendarGridRow } from "./RangeCalendarGridRow.vue"
export { default as RangeCalendarHeadCell } from "./RangeCalendarHeadCell.vue"
export { default as RangeCalendarHeader } from "./RangeCalendarHeader.vue"
export { default as RangeCalendarHeading } from "./RangeCalendarHeading.vue"
export { default as RangeCalendarNextButton } from "./RangeCalendarNextButton.vue"
export { default as RangeCalendarPrevButton } from "./RangeCalendarPrevButton.vue"
```
