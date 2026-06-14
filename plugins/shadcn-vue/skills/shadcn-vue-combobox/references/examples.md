# Combobox — Examples

---

## 1. Basic (Inline Combobox, no popup)

A simple inline combobox with a search input that filters items directly without a floating popup.

```vue
<script setup lang="ts">
import { Example } from "@/registry/bases/reka/components/example"
import {
  Combobox,
  ComboboxEmpty,
  ComboboxInput,
  ComboboxItem,
  ComboboxList,
  ComboboxViewport,
} from "@/registry/bases/reka/ui/combobox"

const frameworks = [
  "Next.js",
  "SvelteKit",
  "Nuxt.js",
  "Remix",
  "Astro",
]
</script>

<template>
  <Example title="Basic">
    <Combobox :items="frameworks">
      <ComboboxInput placeholder="Select a framework" />
      <ComboboxList>
        <ComboboxViewport>
          <ComboboxEmpty>No items found.</ComboboxEmpty>
          <ComboboxItem
            v-for="item in frameworks"
            :key="item"
            :value="item"
          >
            {{ item }}
          </ComboboxItem>
        </ComboboxViewport>
      </ComboboxList>
    </Combobox>
  </Example>
</template>
```

---

## 2. Combobox in Popup (triggered with v-model)

A combobox triggered by a Button. The selected value is bound via `v-model`. Items are objects with `code`, `value`, and `label` fields.

```vue
<script setup lang="ts">
import { ref } from "vue"
import { Example } from "@/registry/bases/reka/components/example"
import { Button } from "@/registry/bases/reka/ui/button"
import {
  Combobox,
  ComboboxEmpty,
  ComboboxInput,
  ComboboxItem,
  ComboboxList,
  ComboboxTrigger,
  ComboboxViewport,
} from "@/registry/bases/reka/ui/combobox"

const countries = [
  { code: "us", value: "united-states", label: "United States" },
  { code: "gb", value: "united-kingdom", label: "United Kingdom" },
  { code: "ca", value: "canada", label: "Canada" },
  { code: "au", value: "australia", label: "Australia" },
  { code: "de", value: "germany", label: "Germany" },
  { code: "fr", value: "france", label: "France" },
  { code: "jp", value: "japan", label: "Japan" },
  { code: "cn", value: "china", label: "China" },
]

const selectedValue = ref(countries[0])
</script>

<template>
  <Example title="Combobox in Popup">
    <Combobox v-model="selectedValue" :items="countries">
      <ComboboxTrigger :as-child="true">
        <Button
          variant="outline"
          class="w-64 justify-between font-normal"
        >
          {{ selectedValue?.label || 'Select country' }}
        </Button>
      </ComboboxTrigger>
      <ComboboxList>
        <ComboboxInput :show-trigger="false" placeholder="Search" />
        <ComboboxViewport>
          <ComboboxEmpty>No items found.</ComboboxEmpty>
          <ComboboxItem
            v-for="item in countries"
            :key="item.code"
            :value="item"
          >
            {{ item.label }}
          </ComboboxItem>
        </ComboboxViewport>
      </ComboboxList>
    </Combobox>
  </Example>
</template>
```

---

## 3. Disabled

The entire combobox is disabled by passing `:disabled="true"` to the root `Combobox` component.

```vue
<script setup lang="ts">
import { Example } from "@/registry/bases/reka/components/example"
import {
  Combobox,
  ComboboxEmpty,
  ComboboxInput,
  ComboboxItem,
  ComboboxList,
  ComboboxViewport,
} from "@/registry/bases/reka/ui/combobox"

const frameworks = ["Next.js", "SvelteKit", "Nuxt.js", "Remix", "Astro"]
</script>

<template>
  <Example title="Disabled">
    <Combobox :items="frameworks" :disabled="true">
      <ComboboxInput placeholder="Select a framework" />
      <ComboboxList>
        <ComboboxViewport>
          <ComboboxEmpty>No items found.</ComboboxEmpty>
          <ComboboxItem
            v-for="item in frameworks"
            :key="item"
            :value="item"
          >
            {{ item }}
          </ComboboxItem>
        </ComboboxViewport>
      </ComboboxList>
    </Combobox>
  </Example>
</template>
```

---

## 4. With Groups

Items are organized into named groups using `ComboboxGroup` with the `heading` prop. Useful for categorized data like timezones, regions, or categories.

```vue
<script setup lang="ts">
import { Example } from "@/registry/bases/reka/components/example"
import {
  Combobox,
  ComboboxEmpty,
  ComboboxGroup,
  ComboboxInput,
  ComboboxItem,
  ComboboxList,
  ComboboxViewport,
} from "@/registry/bases/reka/ui/combobox"

const timezones = [
  {
    value: "Americas",
    items: [
      "(GMT-5) New York",
      "(GMT-8) Los Angeles",
      "(GMT-6) Chicago",
      "(GMT-5) Toronto",
      "(GMT-8) Vancouver",
      "(GMT-3) São Paulo",
    ],
  },
  {
    value: "Europe",
    items: [
      "(GMT+0) London",
      "(GMT+1) Paris",
      "(GMT+1) Berlin",
      "(GMT+1) Rome",
      "(GMT+1) Madrid",
      "(GMT+1) Amsterdam",
    ],
  },
  {
    value: "Asia/Pacific",
    items: [
      "(GMT+9) Tokyo",
      "(GMT+8) Shanghai",
      "(GMT+8) Singapore",
      "(GMT+4) Dubai",
      "(GMT+11) Sydney",
      "(GMT+9) Seoul",
    ],
  },
]
</script>

<template>
  <Example title="With Groups">
    <Combobox :items="timezones">
      <ComboboxInput placeholder="Select a timezone" />
      <ComboboxList>
        <ComboboxViewport>
          <ComboboxEmpty>No timezones found.</ComboboxEmpty>
          <ComboboxGroup
            v-for="group in timezones"
            :key="group.value"
            :heading="group.value"
          >
            <ComboboxItem
              v-for="item in group.items"
              :key="item"
              :value="item"
            >
              {{ item }}
            </ComboboxItem>
          </ComboboxGroup>
        </ComboboxViewport>
      </ComboboxList>
    </Combobox>
  </Example>
</template>
```

---

## 5. Classic Pattern: Popover + Command Composition

The shadcn-vue docs also show a classic Combobox pattern that does NOT use the dedicated Combobox UI components, but instead composes a `Popover` with a `Command` palette. This is the pattern shown on the main shadcn-vue Combobox docs page.

Use this pattern when you want a styled dropdown-button that opens a searchable command list.

```vue
<script setup lang="ts">
import { CheckIcon, ChevronsUpDownIcon } from '@lucide/vue'
import { ref } from 'vue'
import { Button } from '@/components/ui/button'
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from '@/components/ui/command'
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from '@/components/ui/popover'
import { cn } from '@/lib/utils'

const frameworks = [
  { value: 'next.js', label: 'Next.js' },
  { value: 'sveltekit', label: 'SvelteKit' },
  { value: 'nuxt.js', label: 'Nuxt.js' },
  { value: 'remix', label: 'Remix' },
  { value: 'astro', label: 'Astro' },
]

const open = ref(false)
const value = ref('')
</script>

<template>
  <Popover v-model:open="open">
    <PopoverTrigger as-child>
      <Button
        variant="outline"
        role="combobox"
        :aria-expanded="open"
        class="w-[200px] justify-between"
      >
        {{
          value
            ? frameworks.find(framework => framework.value === value)?.label
            : 'Select framework...'
        }}
        <ChevronsUpDownIcon class="ml-2 h-4 w-4 shrink-0 opacity-50" />
      </Button>
    </PopoverTrigger>
    <PopoverContent class="w-[200px] p-0">
      <Command>
        <CommandInput placeholder="Search framework..." />
        <CommandList>
          <CommandEmpty>No framework found.</CommandEmpty>
          <CommandGroup>
            <CommandItem
              v-for="framework in frameworks"
              :key="framework.value"
              :value="framework.value"
              @select="() => {
                value = value === framework.value ? '' : framework.value
                open = false
              }"
            >
              <CheckIcon
                :class="cn(
                  'mr-2 h-4 w-4',
                  value === framework.value ? 'opacity-100' : 'opacity-0',
                )"
              />
              {{ framework.label }}
            </CommandItem>
          </CommandGroup>
        </CommandList>
      </Command>
    </PopoverContent>
  </Popover>
</template>
```

**When to use which pattern:**

| Pattern | Use when |
|---|---|
| Combobox UI components (examples 1–4) | You want a native reka-ui ComboboxRoot with built-in filtering, multi-select, and the full `ComboboxRoot` API surface. |
| Popover + Command composition (example 5) | You want a styled dropdown button that looks like a select, and are already using the Command component for other purposes, or prefer the simpler controlled-open-state approach. |

---
Source: `registry/new-york-v4/ui/combobox/`, `registry/bases/reka/examples/combobox/`
