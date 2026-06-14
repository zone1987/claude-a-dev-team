# Field — Beispiele

Quellen: `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/field/`

## Input Fields (InputFields.vue)

Zeigt verschiedene Input-Varianten: basic, mit Beschreibung, required, disabled, Badge-Label, invalid, deaktiviertes Field.

```vue
<script setup lang="ts">
import { Badge } from "@/registry/bases/reka/ui/badge"
import {
  Field,
  FieldDescription,
  FieldGroup,
  FieldLabel,
} from "@/registry/bases/reka/ui/field"
import { Input } from "@/registry/bases/reka/ui/input"
</script>

<template>
  <FieldGroup>
    <Field>
      <FieldLabel html-for="input-basic">
        Basic Input
      </FieldLabel>
      <Input id="input-basic" placeholder="Enter text" />
    </Field>
    <Field>
      <FieldLabel html-for="input-with-desc">
        Input with Description
      </FieldLabel>
      <Input id="input-with-desc" placeholder="Enter your username" />
      <FieldDescription>
        Choose a unique username for your account.
      </FieldDescription>
    </Field>
    <Field>
      <FieldLabel html-for="input-required">
        Required Field <span class="text-destructive">*</span>
      </FieldLabel>
      <Input
        id="input-required"
        placeholder="This field is required"
        required
      />
      <FieldDescription>This field must be filled out.</FieldDescription>
    </Field>
    <Field>
      <FieldLabel html-for="input-badge">
        Input with Badge
        <Badge variant="secondary" class="ml-auto">
          Recommended
        </Badge>
      </FieldLabel>
      <Input id="input-badge" placeholder="Enter value" />
    </Field>
    <Field data-invalid>
      <FieldLabel html-for="input-invalid">
        Invalid Input
      </FieldLabel>
      <Input
        id="input-invalid"
        placeholder="This field has an error"
        :aria-invalid="true"
      />
      <FieldDescription>
        This field contains validation errors.
      </FieldDescription>
    </Field>
    <Field data-disabled>
      <FieldLabel html-for="input-disabled-field">
        Disabled Field
      </FieldLabel>
      <Input id="input-disabled-field" placeholder="Cannot edit" disabled />
    </Field>
  </FieldGroup>
</template>
```

## Checkbox Fields (CheckboxFields.vue)

Zeigt horizontale Checkboxes, Choice-Card-Pattern mit FieldLabel, FieldContent mit Description, FieldSet + FieldLegend fuer Gruppen.

```vue
<script setup lang="ts">
import { Checkbox } from "@/registry/bases/reka/ui/checkbox"
import {
  Field,
  FieldContent,
  FieldDescription,
  FieldGroup,
  FieldLabel,
  FieldLegend,
  FieldSet,
  FieldTitle,
} from "@/registry/bases/reka/ui/field"
</script>

<template>
  <FieldGroup>
    <!-- Einfache horizontale Checkbox -->
    <Field orientation="horizontal">
      <Checkbox id="checkbox-basic" :default-checked="true" />
      <FieldLabel html-for="checkbox-basic" class="font-normal">
        I agree to the terms and conditions
      </FieldLabel>
    </Field>

    <!-- Checkbox mit FieldContent (Label + Description) -->
    <Field orientation="horizontal">
      <Checkbox id="checkbox-with-desc" />
      <FieldContent>
        <FieldLabel html-for="checkbox-with-desc">
          Subscribe to newsletter
        </FieldLabel>
        <FieldDescription>
          Receive weekly updates about new features and promotions.
        </FieldDescription>
      </FieldContent>
    </Field>

    <!-- Choice Card: FieldLabel umschliesst Field -->
    <FieldLabel html-for="checkbox-with-title">
      <Field orientation="horizontal">
        <Checkbox id="checkbox-with-title" />
        <FieldContent>
          <FieldTitle>Enable Touch ID</FieldTitle>
          <FieldDescription>
            Enable Touch ID to quickly unlock your device.
          </FieldDescription>
        </FieldContent>
      </Field>
    </FieldLabel>

    <!-- FieldSet + FieldLegend fuer Gruppen -->
    <FieldSet>
      <FieldLegend variant="label">
        Preferences
      </FieldLegend>
      <FieldDescription>
        Select all that apply to customize your experience.
      </FieldDescription>
      <FieldGroup class="gap-3">
        <Field orientation="horizontal">
          <Checkbox id="pref-dark" />
          <FieldLabel html-for="pref-dark" class="font-normal">
            Dark mode
          </FieldLabel>
        </Field>
        <Field orientation="horizontal">
          <Checkbox id="pref-compact" />
          <FieldLabel html-for="pref-compact" class="font-normal">
            Compact view
          </FieldLabel>
        </Field>
      </FieldGroup>
    </FieldSet>
  </FieldGroup>
</template>
```

## Radio Fields (RadioFields.vue)

Radio-Gruppen mit FieldSet + FieldLegend, FieldContent, Choice Card Pattern.

```vue
<script setup lang="ts">
import {
  Field,
  FieldContent,
  FieldDescription,
  FieldGroup,
  FieldLabel,
  FieldLegend,
  FieldSet,
  FieldTitle,
} from "@/registry/bases/reka/ui/field"
import {
  RadioGroup,
  RadioGroupItem,
} from "@/registry/bases/reka/ui/radio-group"
</script>

<template>
  <FieldGroup>
    <FieldSet>
      <FieldLegend variant="label">
        Subscription Plan
      </FieldLegend>
      <RadioGroup default-value="free">
        <Field orientation="horizontal">
          <RadioGroupItem id="radio-free" value="free" />
          <FieldLabel html-for="radio-free" class="font-normal">
            Free Plan
          </FieldLabel>
        </Field>
        <Field orientation="horizontal">
          <RadioGroupItem id="radio-pro" value="pro" />
          <FieldLabel html-for="radio-pro" class="font-normal">
            Pro Plan
          </FieldLabel>
        </Field>
        <Field orientation="horizontal">
          <RadioGroupItem id="radio-enterprise" value="enterprise" />
          <FieldLabel html-for="radio-enterprise" class="font-normal">
            Enterprise
          </FieldLabel>
        </Field>
      </RadioGroup>
    </FieldSet>

    <!-- Radio mit FieldContent + FieldTitle (Choice Card) -->
    <RadioGroup class="gap-3">
      <FieldLabel html-for="radio-title-1">
        <Field orientation="horizontal">
          <RadioGroupItem id="radio-title-1" value="title1" />
          <FieldContent>
            <FieldTitle>Enable Touch ID</FieldTitle>
            <FieldDescription>
              Enable Touch ID to quickly unlock your device.
            </FieldDescription>
          </FieldContent>
        </Field>
      </FieldLabel>
      <FieldLabel html-for="radio-title-2">
        <Field orientation="horizontal">
          <RadioGroupItem id="radio-title-2" value="title2" />
          <FieldContent>
            <FieldTitle>Enable Touch ID and Face ID</FieldTitle>
            <FieldDescription>
              Enable Touch ID to quickly unlock your device.
            </FieldDescription>
          </FieldContent>
        </Field>
      </FieldLabel>
    </RadioGroup>
  </FieldGroup>
</template>
```

## Responsive Orientation (InputFields mit responsive)

```vue
<template>
  <FieldGroup>
    <Field orientation="responsive">
      <FieldLabel html-for="responsive-input">
        Email
      </FieldLabel>
      <Input id="responsive-input" type="email" placeholder="email@example.com" />
      <FieldDescription>
        Vertikal auf kleinen Bildschirmen, horizontal ab md Breite.
      </FieldDescription>
    </Field>
  </FieldGroup>
</template>
```

Hinweis: Orientierung `responsive` nutzt Container Query `@md/field-group`.
FieldGroup setzt `@container/field-group` — FieldGroup muss als Eltern vorhanden sein.

## FieldError (Fehlermeldungen)

```vue
<script setup lang="ts">
import { ref } from "vue"
import {
  Field,
  FieldDescription,
  FieldError,
  FieldGroup,
  FieldLabel,
} from "@/registry/bases/reka/ui/field"
import { Input } from "@/registry/bases/reka/ui/input"

// Kompatibel mit Zod, Valibot, ArkType
const errors = ref([
  { message: "This field is required" },
  { message: "Must be at least 2 characters" },
])
</script>

<template>
  <FieldGroup>
    <Field data-invalid>
      <FieldLabel html-for="error-input">Username</FieldLabel>
      <Input id="error-input" :aria-invalid="true" placeholder="johndoe" />
      <FieldError :errors="errors" />
    </Field>
  </FieldGroup>
</template>
```

Quellen:
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/field/InputFields.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/field/CheckboxFields.vue`
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/field/RadioFields.vue`
- `/tmp/shadcn-vue-repo/apps/v4/content/docs/components/field.md`
