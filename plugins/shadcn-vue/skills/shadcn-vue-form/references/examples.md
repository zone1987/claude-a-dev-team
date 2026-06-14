# Form — Beispiele

Quellen: `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/form/`

## Basic Form (FormBasic.vue)

Vollstaendiges Formular mit Zod-Schema, useForm, zwei Feldern (username, email) und Submit-Handling.

```vue
<script setup lang="ts">
import { toTypedSchema } from "@vee-validate/zod"
import { useForm } from "vee-validate"
import { z } from "zod"
import { Button } from "@/registry/bases/reka/ui/button"
import {
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/registry/bases/reka/ui/form"
import { Input } from "@/registry/bases/reka/ui/input"

const formSchema = toTypedSchema(z.object({
  username: z.string().min(2, {
    message: "Username must be at least 2 characters.",
  }),
  email: z.string().email({
    message: "Please enter a valid email address.",
  }),
}))

const form = useForm({
  validationSchema: formSchema,
})

const onSubmit = form.handleSubmit((values) => {
  console.log("Form submitted:", values)
})
</script>

<template>
  <form class="w-full max-w-sm space-y-6" @submit="onSubmit">
    <FormField v-slot="{ componentField }" name="username">
      <FormItem>
        <FormLabel>Username</FormLabel>
        <FormControl>
          <Input type="text" placeholder="johndoe" v-bind="componentField" />
        </FormControl>
        <FormDescription>
          This is your public display name.
        </FormDescription>
        <FormMessage />
      </FormItem>
    </FormField>

    <FormField v-slot="{ componentField }" name="email">
      <FormItem>
        <FormLabel>Email</FormLabel>
        <FormControl>
          <Input type="email" placeholder="john@example.com" v-bind="componentField" />
        </FormControl>
        <FormDescription>
          We'll never share your email with anyone else.
        </FormDescription>
        <FormMessage />
      </FormItem>
    </FormField>

    <Button type="submit">
      Submit
    </Button>
  </form>
</template>
```

## Form mit Checkbox (FormWithCheckbox.vue)

Formular mit Text-Input und zwei Checkbox-Feldern. Zeigt type="checkbox"-Pattern und Pflichtfeld-Validierung.

```vue
<script setup lang="ts">
import { toTypedSchema } from "@vee-validate/zod"
import { useForm } from "vee-validate"
import { z } from "zod"
import { Button } from "@/registry/bases/reka/ui/button"
import { Checkbox } from "@/registry/bases/reka/ui/checkbox"
import {
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/registry/bases/reka/ui/form"
import { Input } from "@/registry/bases/reka/ui/input"

const formSchema = toTypedSchema(z.object({
  username: z.string().min(2, {
    message: "Username must be at least 2 characters.",
  }),
  mobile: z.boolean().default(false).optional(),
  marketing: z.boolean().refine(val => val === true, {
    message: "You must accept marketing emails.",
  }),
}))

const form = useForm({
  validationSchema: formSchema,
})

const onSubmit = form.handleSubmit((values) => {
  console.log("Form submitted:", values)
})
</script>

<template>
  <form class="w-full max-w-sm space-y-6" @submit="onSubmit">
    <FormField v-slot="{ componentField }" name="username">
      <FormItem>
        <FormLabel>Username</FormLabel>
        <FormControl>
          <Input type="text" placeholder="johndoe" v-bind="componentField" />
        </FormControl>
        <FormMessage />
      </FormItem>
    </FormField>

    <FormField v-slot="{ value, handleChange }" type="checkbox" name="mobile">
      <FormItem class="flex flex-row items-start space-x-3 space-y-0 rounded-md border p-4">
        <FormControl>
          <Checkbox :checked="value" @update:checked="handleChange" />
        </FormControl>
        <div class="space-y-1 leading-none">
          <FormLabel>
            Use different settings for my mobile devices
          </FormLabel>
          <FormDescription>
            You can manage your mobile notifications in the mobile settings page.
          </FormDescription>
        </div>
      </FormItem>
    </FormField>

    <FormField v-slot="{ value, handleChange }" type="checkbox" name="marketing">
      <FormItem class="flex flex-row items-start space-x-3 space-y-0">
        <FormControl>
          <Checkbox :checked="value" @update:checked="handleChange" />
        </FormControl>
        <div class="space-y-1 leading-none">
          <FormLabel>
            Marketing emails
          </FormLabel>
          <FormDescription>
            Receive emails about new products, features, and more.
          </FormDescription>
          <FormMessage />
        </div>
      </FormItem>
    </FormField>

    <Button type="submit">
      Submit
    </Button>
  </form>
</template>
```

## Schema-Definition

```ts
import { toTypedSchema } from '@vee-validate/zod'
import * as z from 'zod'

// toTypedSchema macht Formularwerte typgeprueft (Input- und Output-Typen)
const formSchema = toTypedSchema(z.object({
  username: z.string().min(2).max(50),
  email: z.string().email(),
  age: z.number().min(18),
}))
```

## Composition API Ansatz (ohne Form-Komponente)

```ts
import { useForm } from 'vee-validate'
import { toTypedSchema } from '@vee-validate/zod'
import * as z from 'zod'

const formSchema = toTypedSchema(z.object({
  username: z.string().min(2).max(50),
}))

const form = useForm({
  validationSchema: formSchema,
})

const onSubmit = form.handleSubmit((values) => {
  console.log('Form submitted!', values)
})
```

Template:
```vue
<form @submit="onSubmit">
  <FormField v-slot="{ componentField }" name="username">
    <FormItem>
      <FormLabel>Username</FormLabel>
      <FormControl>
        <Input type="text" placeholder="shadcn" v-bind="componentField" />
      </FormControl>
      <FormDescription>
        This is your public display name.
      </FormDescription>
      <FormMessage />
    </FormItem>
  </FormField>
  <Button type="submit">Submit</Button>
</form>
```

Quellen:
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/form/FormBasic.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/form/FormWithCheckbox.vue`
- `/tmp/shadcn-vue-repo/apps/v4/content/docs/components/form.md`
