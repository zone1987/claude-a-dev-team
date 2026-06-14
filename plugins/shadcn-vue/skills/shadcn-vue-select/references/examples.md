# Select — Examples

## SelectBasic.vue

```vue
<script setup lang="ts">
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/registry/bases/reka/ui/select"
</script>

<template>
  <Select>
    <SelectTrigger>
      <SelectValue placeholder="Select a fruit" />
    </SelectTrigger>
    <SelectContent>
      <SelectGroup>
        <SelectItem value="apple">
          Apple
        </SelectItem>
        <SelectItem value="banana">
          Banana
        </SelectItem>
        <SelectItem value="blueberry">
          Blueberry
        </SelectItem>
        <SelectItem value="grapes" :disabled="true">
          Grapes
        </SelectItem>
        <SelectItem value="pineapple">
          Pineapple
        </SelectItem>
      </SelectGroup>
    </SelectContent>
  </Select>
</template>
```

## SelectWithGroups.vue (With Groups and Labels)

```vue
<script setup lang="ts">
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectSeparator,
  SelectTrigger,
  SelectValue,
} from "@/registry/bases/reka/ui/select"
</script>

<template>
  <Select>
    <SelectTrigger>
      <SelectValue placeholder="Select a fruit" />
    </SelectTrigger>
    <SelectContent>
      <SelectGroup>
        <SelectLabel>Fruits</SelectLabel>
        <SelectItem value="apple">
          Apple
        </SelectItem>
        <SelectItem value="banana">
          Banana
        </SelectItem>
        <SelectItem value="blueberry">
          Blueberry
        </SelectItem>
      </SelectGroup>
      <SelectSeparator />
      <SelectGroup>
        <SelectLabel>Vegetables</SelectLabel>
        <SelectItem value="carrot">
          Carrot
        </SelectItem>
        <SelectItem value="broccoli">
          Broccoli
        </SelectItem>
        <SelectItem value="spinach">
          Spinach
        </SelectItem>
      </SelectGroup>
    </SelectContent>
  </Select>
</template>
```

## SelectSizes.vue (Sizes)

```vue
<script setup lang="ts">
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/registry/bases/reka/ui/select"
</script>

<template>
  <div class="flex flex-col gap-4">
    <Select>
      <SelectTrigger size="sm">
        <SelectValue placeholder="Small size" />
      </SelectTrigger>
      <SelectContent>
        <SelectGroup>
          <SelectItem value="apple">
            Apple
          </SelectItem>
          <SelectItem value="banana">
            Banana
          </SelectItem>
          <SelectItem value="blueberry">
            Blueberry
          </SelectItem>
        </SelectGroup>
      </SelectContent>
    </Select>
    <Select>
      <SelectTrigger size="default">
        <SelectValue placeholder="Default size" />
      </SelectTrigger>
      <SelectContent>
        <SelectGroup>
          <SelectItem value="apple">
            Apple
          </SelectItem>
          <SelectItem value="banana">
            Banana
          </SelectItem>
          <SelectItem value="blueberry">
            Blueberry
          </SelectItem>
        </SelectGroup>
      </SelectContent>
    </Select>
  </div>
</template>
```

## SelectWithField.vue (With Field)

```vue
<script setup lang="ts">
import {
  Field,
  FieldDescription,
  FieldLabel,
} from "@/registry/bases/reka/ui/field"
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/registry/bases/reka/ui/select"
</script>

<template>
  <Field>
    <FieldLabel html-for="select-fruit">
      Favorite Fruit
    </FieldLabel>
    <Select>
      <SelectTrigger id="select-fruit">
        <SelectValue placeholder="Select a fruit" />
      </SelectTrigger>
      <SelectContent>
        <SelectGroup>
          <SelectItem value="apple">
            Apple
          </SelectItem>
          <SelectItem value="banana">
            Banana
          </SelectItem>
          <SelectItem value="blueberry">
            Blueberry
          </SelectItem>
          <SelectItem value="grapes">
            Grapes
          </SelectItem>
          <SelectItem value="pineapple">
            Pineapple
          </SelectItem>
        </SelectGroup>
      </SelectContent>
    </Select>
    <FieldDescription>
      Choose your favorite fruit from the list.
    </FieldDescription>
  </Field>
</template>
```

## SelectDisabled.vue

```vue
<script setup lang="ts">
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/registry/bases/reka/ui/select"
</script>

<template>
  <Select :disabled="true">
    <SelectTrigger>
      <SelectValue placeholder="Disabled" />
    </SelectTrigger>
    <SelectContent>
      <SelectGroup>
        <SelectItem value="apple">
          Apple
        </SelectItem>
        <SelectItem value="banana">
          Banana
        </SelectItem>
        <SelectItem value="blueberry">
          Blueberry
        </SelectItem>
        <SelectItem value="grapes" :disabled="true">
          Grapes
        </SelectItem>
        <SelectItem value="pineapple">
          Pineapple
        </SelectItem>
      </SelectGroup>
    </SelectContent>
  </Select>
</template>
```
