# NativeSelect — Examples

## Contents

- [Example 1: Basic Native Select (NativeSelectBasic.vue)](#example-1-basic-native-select-nativeselectbasicvue)
- [Example 2: Native Select with OptGroup (NativeSelectWithOptGroup.vue)](#example-2-native-select-with-optgroup-nativeselectwithoptgroupvue)
- [Sources](#sources)

## Example 1: Basic Native Select (NativeSelectBasic.vue)

Simple select with options.

```vue
<script setup lang="ts">
import {
  NativeSelect,
  NativeSelectOption,
} from "@/components/ui/native-select"
</script>

<template>
  <div class="grid w-full max-w-sm items-center gap-4">
    <NativeSelect>
      <NativeSelectOption value="">
        Choose an option
      </NativeSelectOption>
      <NativeSelectOption value="option1">
        Option 1
      </NativeSelectOption>
      <NativeSelectOption value="option2">
        Option 2
      </NativeSelectOption>
      <NativeSelectOption value="option3">
        Option 3
      </NativeSelectOption>
    </NativeSelect>

    <NativeSelect>
      <NativeSelectOption value="">
        Select a country
      </NativeSelectOption>
      <NativeSelectOption value="us">United States</NativeSelectOption>
      <NativeSelectOption value="uk">United Kingdom</NativeSelectOption>
      <NativeSelectOption value="ca">Canada</NativeSelectOption>
      <NativeSelectOption value="au">Australia</NativeSelectOption>
    </NativeSelect>
  </div>
</template>
```

---

## Example 2: Native Select with OptGroup (NativeSelectWithOptGroup.vue)

`NativeSelectOptGroup` groups options with a `label` attribute.

```vue
<script setup lang="ts">
import {
  NativeSelect,
  NativeSelectOptGroup,
  NativeSelectOption,
} from "@/components/ui/native-select"
</script>

<template>
  <div class="grid w-full max-w-sm items-center gap-4">
    <NativeSelect>
      <NativeSelectOption value="">
        Select a fruit
      </NativeSelectOption>
      <NativeSelectOptGroup label="Citrus">
        <NativeSelectOption value="orange">Orange</NativeSelectOption>
        <NativeSelectOption value="lemon">Lemon</NativeSelectOption>
        <NativeSelectOption value="lime">Lime</NativeSelectOption>
      </NativeSelectOptGroup>
      <NativeSelectOptGroup label="Berries">
        <NativeSelectOption value="strawberry">Strawberry</NativeSelectOption>
        <NativeSelectOption value="blueberry">Blueberry</NativeSelectOption>
        <NativeSelectOption value="raspberry">Raspberry</NativeSelectOption>
      </NativeSelectOptGroup>
    </NativeSelect>

    <NativeSelect>
      <NativeSelectOption value="">
        Select a programming language
      </NativeSelectOption>
      <NativeSelectOptGroup label="Frontend">
        <NativeSelectOption value="javascript">JavaScript</NativeSelectOption>
        <NativeSelectOption value="typescript">TypeScript</NativeSelectOption>
      </NativeSelectOptGroup>
      <NativeSelectOptGroup label="Backend">
        <NativeSelectOption value="python">Python</NativeSelectOption>
        <NativeSelectOption value="java">Java</NativeSelectOption>
        <NativeSelectOption value="go">Go</NativeSelectOption>
      </NativeSelectOptGroup>
    </NativeSelect>
  </div>
</template>
```

---

## Sources
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/native-select/NativeSelectBasic.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/native-select/NativeSelectWithOptGroup.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/native-select/NativeSelectExample.vue`
