# ToggleGroup — Examples

## Contents

- [Basic (Multiple, with spacing)](#basic-multiple-with-spacing)
- [Outline (Single, fused/connected)](#outline-single-fusedconnected)
- [Outline with Icons (Multiple, small)](#outline-with-icons-multiple-small)
- [Sizes](#sizes)
- [With Spacing](#with-spacing)
- [Filter](#filter)
- [Date Range](#date-range)
- [Sort (with Icons + Text)](#sort-with-icons-text)
- [With Icons (Filled on active)](#with-icons-filled-on-active)
- [With Input and Select](#with-input-and-select)
- [Vertical](#vertical)
- [Vertical Outline](#vertical-outline)
- [Vertical Outline with Icons](#vertical-outline-with-icons)
- [Vertical with Spacing](#vertical-with-spacing)

## Basic (Multiple, with spacing)

Three icon-only formatting toggles in multiple-selection mode with `spacing=1`.

```vue
<script setup lang="ts">
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
import { BoldIcon, ItalicIcon, UnderlineIcon } from "lucide-vue-next"
</script>

<template>
  <ToggleGroup type="multiple" :spacing="1">
    <ToggleGroupItem value="bold" aria-label="Toggle bold">
      <BoldIcon />
    </ToggleGroupItem>
    <ToggleGroupItem value="italic" aria-label="Toggle italic">
      <ItalicIcon />
    </ToggleGroupItem>
    <ToggleGroupItem value="underline" aria-label="Toggle underline">
      <UnderlineIcon />
    </ToggleGroupItem>
  </ToggleGroup>
</template>
```

Source: `registry/bases/reka/examples/toggle-group/ToggleGroupBasic.vue`

---

## Outline (Single, fused/connected)

Single-selection outline group fused into a segmented control (spacing=0, default).

```vue
<script setup lang="ts">
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
</script>

<template>
  <ToggleGroup variant="outline" type="single" default-value="all">
    <ToggleGroupItem value="all" aria-label="Toggle all">All</ToggleGroupItem>
    <ToggleGroupItem value="missed" aria-label="Toggle missed">Missed</ToggleGroupItem>
  </ToggleGroup>
</template>
```

Source: `registry/bases/reka/examples/toggle-group/ToggleGroupOutline.vue`

---

## Outline with Icons (Multiple, small)

Small outline group with icon-only items.

```vue
<script setup lang="ts">
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
import { BoldIcon, ItalicIcon, UnderlineIcon } from "lucide-vue-next"
</script>

<template>
  <ToggleGroup variant="outline" type="multiple" size="sm">
    <ToggleGroupItem value="bold" aria-label="Toggle bold"><BoldIcon /></ToggleGroupItem>
    <ToggleGroupItem value="italic" aria-label="Toggle italic"><ItalicIcon /></ToggleGroupItem>
    <ToggleGroupItem value="underline" aria-label="Toggle underline"><UnderlineIcon /></ToggleGroupItem>
  </ToggleGroup>
</template>
```

Source: `registry/bases/reka/examples/toggle-group/ToggleGroupOutlineWithIcons.vue`

---

## Sizes

Shows sm and default sizes with outline variant and single selection.

```vue
<script setup lang="ts">
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
</script>

<template>
  <div class="flex flex-col gap-4">
    <ToggleGroup type="single" size="sm" default-value="top" variant="outline">
      <ToggleGroupItem value="top" aria-label="Toggle top">Top</ToggleGroupItem>
      <ToggleGroupItem value="bottom" aria-label="Toggle bottom">Bottom</ToggleGroupItem>
      <ToggleGroupItem value="left" aria-label="Toggle left">Left</ToggleGroupItem>
      <ToggleGroupItem value="right" aria-label="Toggle right">Right</ToggleGroupItem>
    </ToggleGroup>
    <ToggleGroup type="single" default-value="top" variant="outline">
      <ToggleGroupItem value="top" aria-label="Toggle top">Top</ToggleGroupItem>
      <ToggleGroupItem value="bottom" aria-label="Toggle bottom">Bottom</ToggleGroupItem>
      <ToggleGroupItem value="left" aria-label="Toggle left">Left</ToggleGroupItem>
      <ToggleGroupItem value="right" aria-label="Toggle right">Right</ToggleGroupItem>
    </ToggleGroup>
  </div>
</template>
```

Source: `registry/bases/reka/examples/toggle-group/ToggleGroupSizes.vue`

---

## With Spacing

Outline single group with `spacing=2` — items separated with a visible gap.

```vue
<script setup lang="ts">
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
</script>

<template>
  <ToggleGroup type="single" size="sm" default-value="top" variant="outline" :spacing="2">
    <ToggleGroupItem value="top" aria-label="Toggle top">Top</ToggleGroupItem>
    <ToggleGroupItem value="bottom" aria-label="Toggle bottom">Bottom</ToggleGroupItem>
    <ToggleGroupItem value="left" aria-label="Toggle left">Left</ToggleGroupItem>
    <ToggleGroupItem value="right" aria-label="Toggle right">Right</ToggleGroupItem>
  </ToggleGroup>
</template>
```

Source: `registry/bases/reka/examples/toggle-group/ToggleGroupSpacing.vue`

---

## Filter

Status filter bar — single selection, small outline, pre-selected "all".

```vue
<script setup lang="ts">
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
</script>

<template>
  <ToggleGroup type="single" default-value="all" variant="outline" size="sm">
    <ToggleGroupItem value="all" aria-label="All">All</ToggleGroupItem>
    <ToggleGroupItem value="active" aria-label="Active">Active</ToggleGroupItem>
    <ToggleGroupItem value="completed" aria-label="Completed">Completed</ToggleGroupItem>
    <ToggleGroupItem value="archived" aria-label="Archived">Archived</ToggleGroupItem>
  </ToggleGroup>
</template>
```

Source: `registry/bases/reka/examples/toggle-group/ToggleGroupFilter.vue`

---

## Date Range

Date range selector with 4 options, small outline, pre-selected "today", `spacing=2`.

```vue
<script setup lang="ts">
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
</script>

<template>
  <ToggleGroup type="single" default-value="today" variant="outline" size="sm" :spacing="2">
    <ToggleGroupItem value="today" aria-label="Today">Today</ToggleGroupItem>
    <ToggleGroupItem value="week" aria-label="This Week">This Week</ToggleGroupItem>
    <ToggleGroupItem value="month" aria-label="This Month">This Month</ToggleGroupItem>
    <ToggleGroupItem value="year" aria-label="This Year">This Year</ToggleGroupItem>
  </ToggleGroup>
</template>
```

Source: `registry/bases/reka/examples/toggle-group/ToggleGroupDateRange.vue`

---

## Sort (with Icons + Text)

Sort control with icon + label in each item, single selection, small outline.

```vue
<script setup lang="ts">
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
import { ArrowDownIcon, ArrowUpIcon, TrendingUpIcon } from "lucide-vue-next"
</script>

<template>
  <ToggleGroup type="single" default-value="newest" variant="outline" size="sm">
    <ToggleGroupItem value="newest" aria-label="Newest">
      <ArrowDownIcon />Newest
    </ToggleGroupItem>
    <ToggleGroupItem value="oldest" aria-label="Oldest">
      <ArrowUpIcon />Oldest
    </ToggleGroupItem>
    <ToggleGroupItem value="popular" aria-label="Popular">
      <TrendingUpIcon />Popular
    </ToggleGroupItem>
  </ToggleGroup>
</template>
```

Source: `registry/bases/reka/examples/toggle-group/ToggleGroupSort.vue`

---

## With Icons (Filled on active)

Multiple-selection outline group; uses `aria-pressed:*:[svg]:fill-foreground` to fill icons when active.

```vue
<script setup lang="ts">
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
import { StarIcon, HeartIcon, BookmarkIcon } from "lucide-vue-next"
</script>

<template>
  <ToggleGroup type="multiple" variant="outline" :spacing="1" size="sm">
    <ToggleGroupItem
      value="star" aria-label="Toggle star"
      class="aria-pressed:*:[svg]:fill-foreground aria-pressed:*:[svg]:stroke-foreground aria-pressed:bg-transparent"
    >
      <StarIcon />Star
    </ToggleGroupItem>
    <ToggleGroupItem
      value="heart" aria-label="Toggle heart"
      class="aria-pressed:*:[svg]:fill-foreground aria-pressed:*:[svg]:stroke-foreground aria-pressed:bg-transparent"
    >
      <HeartIcon />Heart
    </ToggleGroupItem>
    <ToggleGroupItem
      value="bookmark" aria-label="Toggle bookmark"
      class="aria-pressed:*:[svg]:fill-foreground aria-pressed:*:[svg]:stroke-foreground aria-pressed:bg-transparent"
    >
      <BookmarkIcon />Bookmark
    </ToggleGroupItem>
  </ToggleGroup>
</template>
```

Source: `registry/bases/reka/examples/toggle-group/ToggleGroupWithIcons.vue`

---

## With Input and Select

ToggleGroup embedded in a toolbar alongside an Input and Select — grid/list view switcher.

```vue
<script setup lang="ts">
import { Input } from "@/components/ui/input"
import { Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
</script>

<template>
  <div class="flex items-center gap-2">
    <Input type="search" placeholder="Search..." class="flex-1" />
    <Select default-value="all">
      <SelectTrigger class="w-32"><SelectValue /></SelectTrigger>
      <SelectContent>
        <SelectGroup>
          <SelectItem value="all">All</SelectItem>
          <SelectItem value="active">Active</SelectItem>
          <SelectItem value="archived">Archived</SelectItem>
        </SelectGroup>
      </SelectContent>
    </Select>
    <ToggleGroup type="single" default-value="grid" variant="outline">
      <ToggleGroupItem value="grid" aria-label="Grid view">Grid</ToggleGroupItem>
      <ToggleGroupItem value="list" aria-label="List view">List</ToggleGroupItem>
    </ToggleGroup>
  </div>
</template>
```

Source: `registry/bases/reka/examples/toggle-group/ToggleGroupWithInputAndSelect.vue`

---

## Vertical

Multiple-selection vertical group with icon items and `spacing=2`.

```vue
<script setup lang="ts">
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
import { BoldIcon, ItalicIcon, UnderlineIcon } from "lucide-vue-next"
</script>

<template>
  <ToggleGroup type="multiple" orientation="vertical" :spacing="2">
    <ToggleGroupItem value="bold" aria-label="Toggle bold"><BoldIcon /></ToggleGroupItem>
    <ToggleGroupItem value="italic" aria-label="Toggle italic"><ItalicIcon /></ToggleGroupItem>
    <ToggleGroupItem value="underline" aria-label="Toggle underline"><UnderlineIcon /></ToggleGroupItem>
  </ToggleGroup>
</template>
```

Source: `registry/bases/reka/examples/toggle-group/ToggleGroupVertical.vue`

---

## Vertical Outline

Vertical single-selection outline group with text labels, small, `spacing=0` (fused).

```vue
<script setup lang="ts">
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
</script>

<template>
  <ToggleGroup variant="outline" type="single" default-value="all" orientation="vertical" size="sm">
    <ToggleGroupItem value="all" aria-label="Toggle all">All</ToggleGroupItem>
    <ToggleGroupItem value="active" aria-label="Toggle active">Active</ToggleGroupItem>
    <ToggleGroupItem value="completed" aria-label="Toggle completed">Completed</ToggleGroupItem>
    <ToggleGroupItem value="archived" aria-label="Toggle archived">Archived</ToggleGroupItem>
  </ToggleGroup>
</template>
```

Source: `registry/bases/reka/examples/toggle-group/ToggleGroupVerticalOutline.vue`

---

## Vertical Outline with Icons

Vertical multiple-selection outline icon group, small.

```vue
<script setup lang="ts">
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
import { BoldIcon, ItalicIcon, UnderlineIcon } from "lucide-vue-next"
</script>

<template>
  <ToggleGroup variant="outline" type="multiple" orientation="vertical" size="sm">
    <ToggleGroupItem value="bold" aria-label="Toggle bold"><BoldIcon /></ToggleGroupItem>
    <ToggleGroupItem value="italic" aria-label="Toggle italic"><ItalicIcon /></ToggleGroupItem>
    <ToggleGroupItem value="underline" aria-label="Toggle underline"><UnderlineIcon /></ToggleGroupItem>
  </ToggleGroup>
</template>
```

Source: `registry/bases/reka/examples/toggle-group/ToggleGroupVerticalOutlineWithIcons.vue`

---

## Vertical with Spacing

Vertical single-selection outline group with `spacing=2`, small.

```vue
<script setup lang="ts">
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group"
</script>

<template>
  <ToggleGroup type="single" size="sm" default-value="top" variant="outline" orientation="vertical" :spacing="2">
    <ToggleGroupItem value="top" aria-label="Toggle top">Top</ToggleGroupItem>
    <ToggleGroupItem value="bottom" aria-label="Toggle bottom">Bottom</ToggleGroupItem>
    <ToggleGroupItem value="left" aria-label="Toggle left">Left</ToggleGroupItem>
    <ToggleGroupItem value="right" aria-label="Toggle right">Right</ToggleGroupItem>
  </ToggleGroup>
</template>
```

Source: `registry/bases/reka/examples/toggle-group/ToggleGroupVerticalWithSpacing.vue`
