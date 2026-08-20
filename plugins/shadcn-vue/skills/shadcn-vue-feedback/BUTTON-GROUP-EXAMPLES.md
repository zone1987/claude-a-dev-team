# ButtonGroup — Examples

## Contents

- [1. Basic Horizontal Group](#1-basic-horizontal-group)
- [2. Vertical Orientation](#2-vertical-orientation)
- [3. Nested Groups](#3-nested-groups)
- [4. With Input](#4-with-input)
- [5. With Separator (non-outline variants)](#5-with-separator-non-outline-variants)

## 1. Basic Horizontal Group

Two outline buttons merged into a single row.

```vue
<script setup lang="ts">
import { ButtonGroup } from "@/components/ui/button-group"
import { Button } from "@/components/ui/button"
</script>

<template>
  <ButtonGroup aria-label="Text alignment">
    <Button variant="outline">Left</Button>
    <Button variant="outline">Right</Button>
  </ButtonGroup>
</template>
```

Three buttons — first/last keep their outer radius, middle loses both:

```vue
<ButtonGroup aria-label="View options">
  <Button variant="outline">Day</Button>
  <Button variant="outline">Week</Button>
  <Button variant="outline">Month</Button>
</ButtonGroup>
```

---

## 2. Vertical Orientation

Stack buttons top-to-bottom. Useful for toolbars or action panels in sidebars.

```vue
<script setup lang="ts">
import { ButtonGroup } from "@/components/ui/button-group"
import { Button } from "@/components/ui/button"
import { ChevronUp, ChevronDown } from "lucide-vue-next"
</script>

<template>
  <ButtonGroup orientation="vertical" aria-label="Adjust value">
    <Button variant="outline" size="icon" aria-label="Increment">
      <ChevronUp />
    </Button>
    <Button variant="outline" size="icon" aria-label="Decrement">
      <ChevronDown />
    </Button>
  </ButtonGroup>
</template>
```

---

## 3. Nested Groups

Wrap a `ButtonGroup` inside another to create complex toolbar layouts. The outer group automatically adds `gap-2` between nested `[data-slot=button-group]` children.

```vue
<script setup lang="ts">
import { ButtonGroup } from "@/components/ui/button-group"
import { Button } from "@/components/ui/button"
import { Bold, Italic, Underline, AlignLeft, AlignCenter, AlignRight } from "lucide-vue-next"
</script>

<template>
  <ButtonGroup aria-label="Text formatting toolbar">
    <!-- Inline formatting group -->
    <ButtonGroup aria-label="Inline styles">
      <Button variant="outline" size="icon" aria-label="Bold">
        <Bold />
      </Button>
      <Button variant="outline" size="icon" aria-label="Italic">
        <Italic />
      </Button>
      <Button variant="outline" size="icon" aria-label="Underline">
        <Underline />
      </Button>
    </ButtonGroup>

    <!-- Alignment group -->
    <ButtonGroup aria-label="Alignment">
      <Button variant="outline" size="icon" aria-label="Align left">
        <AlignLeft />
      </Button>
      <Button variant="outline" size="icon" aria-label="Align center">
        <AlignCenter />
      </Button>
      <Button variant="outline" size="icon" aria-label="Align right">
        <AlignRight />
      </Button>
    </ButtonGroup>
  </ButtonGroup>
</template>
```

---

## 4. With Input

Combine a `Button` and an `<input>` (or shadcn-vue `Input`) in a single group. The input expands to fill remaining space via `[&>input]:flex-1`.

```vue
<script setup lang="ts">
import { ref } from "vue"
import { ButtonGroup } from "@/components/ui/button-group"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Search } from "lucide-vue-next"

const query = ref("")
</script>

<template>
  <ButtonGroup aria-label="Search">
    <Input
      v-model="query"
      type="search"
      placeholder="Search…"
      aria-label="Search query"
    />
    <Button aria-label="Submit search">
      <Search />
    </Button>
  </ButtonGroup>
</template>
```

Prefix variant — label text on the left, input on the right:

```vue
<ButtonGroup aria-label="URL input">
  <ButtonGroupText>https://</ButtonGroupText>
  <Input placeholder="example.com" aria-label="Domain" />
</ButtonGroup>
```

---

## 5. With Separator (non-outline variants)

When using solid-background button variants (e.g. `default`, `secondary`) the merged borders are invisible. Insert a `ButtonGroupSeparator` to keep items visually distinct.

```vue
<script setup lang="ts">
import {
  ButtonGroup,
  ButtonGroupSeparator,
} from "@/components/ui/button-group"
import { Button } from "@/components/ui/button"
import { ChevronDown } from "lucide-vue-next"
</script>

<template>
  <!-- Split-button pattern: primary action + dropdown trigger -->
  <ButtonGroup aria-label="Create options">
    <Button>Create</Button>
    <ButtonGroupSeparator />
    <Button size="icon" aria-label="More create options">
      <ChevronDown />
    </Button>
  </ButtonGroup>
</template>
```

Vertical group with horizontal separators:

```vue
<ButtonGroup orientation="vertical" aria-label="Actions">
  <Button variant="secondary">Copy</Button>
  <ButtonGroupSeparator orientation="horizontal" />
  <Button variant="secondary">Paste</Button>
  <ButtonGroupSeparator orientation="horizontal" />
  <Button variant="secondary">Delete</Button>
</ButtonGroup>
```
