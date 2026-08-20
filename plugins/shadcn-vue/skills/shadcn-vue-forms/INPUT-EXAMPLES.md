# Input — Beispiele

Quellen: `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/input/`

## Contents

- [Basic](#basic)
- [Mit Label (InputWithLabel.vue)](#mit-label-inputwithlabelvue)
- [Mit Beschreibung (InputWithDescription.vue)](#mit-beschreibung-inputwithdescriptionvue)
- [Deaktiviert (InputDisabled.vue)](#deaktiviert-inputdisabledvue)
- [Fehlerzustand (InputInvalid.vue)](#fehlerzustand-inputinvalidvue)
- [Mit Button (InputWithButton.vue)](#mit-button-inputwithbuttonvue)
- [Alle Input-Typen (InputTypes.vue)](#alle-input-typen-inputtypesvue)
- [Mit Select (InputWithSelect.vue)](#mit-select-inputwithselectvue)
- [Formular-Beispiel (InputForm.vue)](#formular-beispiel-inputformvue)

## Basic

```vue
<script setup lang="ts">
import { Input } from "@/registry/bases/reka/ui/input"
</script>

<template>
  <Input type="email" placeholder="Email" />
</template>
```

## Mit Label (InputWithLabel.vue)

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

## Mit Beschreibung (InputWithDescription.vue)

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

## Deaktiviert (InputDisabled.vue)

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

## Fehlerzustand (InputInvalid.vue)

```vue
<script setup lang="ts">
import { Input } from "@/registry/bases/reka/ui/input"
</script>

<template>
  <Input type="text" placeholder="Error" :aria-invalid="true" />
</template>
```

## Mit Button (InputWithButton.vue)

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

## Alle Input-Typen (InputTypes.vue)

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

## Mit Select (InputWithSelect.vue)

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

## Formular-Beispiel (InputForm.vue)

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

Quellen:
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/input/`
- `/tmp/shadcn-vue-repo/apps/v4/content/docs/components/input.md`
