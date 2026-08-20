# Input — Examples

Sources: `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/input/`

## Contents

- [Basic](#basic)
- [With Label (InputWithLabel.vue)](#with-label-inputwithlabelvue)
- [With Description (InputWithDescription.vue)](#with-description-inputwithdescriptionvue)
- [Disabled (InputDisabled.vue)](#disabled-inputdisabledvue)
- [Error State (InputInvalid.vue)](#error-state-inputinvalidvue)
- [With Button (InputWithButton.vue)](#with-button-inputwithbuttonvue)
- [All Input Types (InputTypes.vue)](#all-input-types-inputtypesvue)
- [With Select (InputWithSelect.vue)](#with-select-inputwithselectvue)
- [Form Example (InputForm.vue)](#form-example-inputformvue)

## Basic

```vue
<script setup lang="ts">
import { Input } from "@/registry/bases/reka/ui/input"
</script>

<template>
  <Input type="email" placeholder="Email" />
</template>
```

## With Label (InputWithLabel.vue)

```vue
<script setup lang="ts">
import { Field, FieldLabel } from "@/registry/bases/reka/ui/field"
import { Input } from "@/registry/bases/reka/ui/input"
</script>

<template>
  <Field>
    <FieldLabel html-for="input-demo-email">
      Email
    </FieldLabel>
    <Input
      id="input-demo-email"
      type="email"
      placeholder="name@example.com"
    />
  </Field>
</template>
```

## With Description (InputWithDescription.vue)

```vue
<script setup lang="ts">
import { Field, FieldDescription, FieldLabel } from "@/registry/bases/reka/ui/field"
import { Input } from "@/registry/bases/reka/ui/input"
</script>

<template>
  <Field>
    <FieldLabel html-for="input-demo-username">Username</FieldLabel>
    <Input id="input-demo-username" type="text" placeholder="Enter your username" />
    <FieldDescription>
      Choose a unique username for your account.
    </FieldDescription>
  </Field>
</template>
```

## Disabled (InputDisabled.vue)

```vue
<script setup lang="ts">
import { Field, FieldLabel } from "@/registry/bases/reka/ui/field"
import { Input } from "@/registry/bases/reka/ui/input"
</script>

<template>
  <Field>
    <FieldLabel html-for="input-demo-disabled">Email</FieldLabel>
    <Input id="input-demo-disabled" type="email" placeholder="Email" :disabled="true" />
  </Field>
</template>
```

## Error State (InputInvalid.vue)

```vue
<script setup lang="ts">
import { Input } from "@/registry/bases/reka/ui/input"
</script>

<template>
  <Input type="text" placeholder="Error" :aria-invalid="true" />
</template>
```

## With Button (InputWithButton.vue)

```vue
<script setup lang="ts">
import { Button } from "@/registry/bases/reka/ui/button"
import { Input } from "@/registry/bases/reka/ui/input"
</script>

<template>
  <div class="flex w-full gap-2">
    <Input type="search" placeholder="Search..." class="flex-1" />
    <Button>Search</Button>
  </div>
</template>
```

## All Input Types (InputTypes.vue)

```vue
<script setup lang="ts">
import { Field, FieldLabel } from "@/registry/bases/reka/ui/field"
import { Input } from "@/registry/bases/reka/ui/input"
</script>

<template>
  <div class="flex w-full flex-col gap-6">
    <Field>
      <FieldLabel html-for="input-demo-password">Password</FieldLabel>
      <Input id="input-demo-password" type="password" placeholder="Password" />
    </Field>
    <Field>
      <FieldLabel html-for="input-demo-tel">Phone</FieldLabel>
      <Input id="input-demo-tel" type="tel" placeholder="+1 (555) 123-4567" />
    </Field>
    <Field>
      <FieldLabel html-for="input-demo-url">URL</FieldLabel>
      <Input id="input-demo-url" type="url" placeholder="https://example.com" />
    </Field>
    <Field>
      <FieldLabel html-for="input-demo-search">Search</FieldLabel>
      <Input id="input-demo-search" type="search" placeholder="Search" />
    </Field>
    <Field>
      <FieldLabel html-for="input-demo-number">Number</FieldLabel>
      <Input id="input-demo-number" type="number" placeholder="123" />
    </Field>
    <Field>
      <FieldLabel html-for="input-demo-date">Date</FieldLabel>
      <Input id="input-demo-date" type="date" />
    </Field>
    <Field>
      <FieldLabel html-for="input-demo-time">Time</FieldLabel>
      <Input id="input-demo-time" type="time" />
    </Field>
    <Field>
      <FieldLabel html-for="input-demo-file">File</FieldLabel>
      <Input id="input-demo-file" type="file" />
    </Field>
  </div>
</template>
```

## With Select (InputWithSelect.vue)

```vue
<script setup lang="ts">
import { Input } from "@/registry/bases/reka/ui/input"
import {
  Select, SelectContent, SelectItem, SelectTrigger, SelectValue,
} from "@/registry/bases/reka/ui/select"
</script>

<template>
  <div class="flex w-full gap-2">
    <Input type="text" placeholder="Enter amount" class="flex-1" />
    <Select default-value="usd">
      <SelectTrigger class="w-32">
        <SelectValue />
      </SelectTrigger>
      <SelectContent>
        <SelectItem value="usd">USD</SelectItem>
        <SelectItem value="eur">EUR</SelectItem>
        <SelectItem value="gbp">GBP</SelectItem>
      </SelectContent>
    </Select>
  </div>
</template>
```

## Form Example (InputForm.vue)

```vue
<script setup lang="ts">
import { Button } from "@/registry/bases/reka/ui/button"
import {
  Field, FieldDescription, FieldGroup, FieldLabel,
} from "@/registry/bases/reka/ui/field"
import { Input } from "@/registry/bases/reka/ui/input"
</script>

<template>
  <form class="w-full">
    <FieldGroup>
      <Field>
        <FieldLabel html-for="form-name">Name</FieldLabel>
        <Input id="form-name" type="text" placeholder="John Doe" />
      </Field>
      <Field>
        <FieldLabel html-for="form-email">Email</FieldLabel>
        <Input id="form-email" type="email" placeholder="john@example.com" />
        <FieldDescription>We'll never share your email with anyone.</FieldDescription>
      </Field>
      <Field orientation="horizontal">
        <Button type="button" variant="outline">Cancel</Button>
        <Button type="submit">Submit</Button>
      </Field>
    </FieldGroup>
  </form>
</template>
```

Sources:
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/input/`
- `/tmp/shadcn-vue-repo/apps/v4/content/docs/components/input.md`
